"""Evaluate every finished run under ``outputs/runs`` and assemble the experiment summary.

    python evaluation/batch_report.py [--jobs 4] [--runs-root outputs/runs] [--out outputs/reports]

Per run: one accuracy report against the clip's ground truth (``runs/<clip>/<name>.md|.json``,
same content as ``evaluation/cli.py``), skipped when a report for the same output sha256
already exists. Plus parity reports of the default runs against the cloud export. Then
``SUMMARY.md`` with the experiment tables:

- E1 accuracy: frozen baseline against ground truth, both clips.
- E2 parity: frozen baseline against the cloud export, both clips.
- E3 association ceiling: ground truth as detections.
- E4 robustness: degraded ground truth, mean and spread over seeds per degradation level.
- E5 parameters: max_age x tentative_threshold grid with real detections.

Reads CSVs and manifests only; never runs the tracker.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from evaluation.adapters import load_cloud_run, load_gt_run  # noqa: E402
from evaluation.cli import TURBINE_GT_FRAMES, load_candidate  # noqa: E402
from evaluation.evaluate import evaluate, render_markdown  # noqa: E402
from evaluation.views import FLOCK_TIMESTAMP_OVERLAY  # noqa: E402

CLIPS = {
    "flock": {"video_id": "20251012_164031_1DAC", "region": FLOCK_TIMESTAMP_OVERLAY, "frames": None, "frozen": "results/flock/baseline_tracks.csv"},
    "turbine": {"video_id": "20250920_063942_6C42", "region": None, "frames": TURBINE_GT_FRAMES, "frozen": "results/turbine/baseline_tracks.csv"},
}
FIELDS = ("HOTA", "DetA", "AssA", "HOTA_a50", "MOTA", "IDF1", "IDSW", "Frag", "CLR_TP", "CLR_FP", "CLR_FN", "num_tracker_ids", "num_gt_ids")


def gt_path(clip: str) -> Path:
    return KIT_ROOT / "ground_truth" / f"{CLIPS[clip]['video_id']}_reference_tracks_corrected.csv"


def cloud_path(clip: str) -> Path:
    return KIT_ROOT / "data" / f"{CLIPS[clip]['video_id']}_cloud_reference_tracks.csv"


def evaluate_one(clip: str, name: str, tracks: Path, out_dir: Path, reference_kind: str) -> dict:
    """Worker: evaluate ``tracks`` against gt or cloud; write report files; return summary rows."""
    video_id = CLIPS[clip]["video_id"]
    manifest_path = tracks.with_suffix(tracks.suffix + ".manifest.json")
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    output_sha = manifest.get("output", {}).get("sha256", "")
    report_base = out_dir / "runs" / clip / f"{name}__vs_{reference_kind}"
    json_path = Path(str(report_base) + ".json")
    if json_path.exists() and output_sha:
        previous = json.loads(json_path.read_text())
        if previous.get("settings", {}).get("candidate_output_sha256") == output_sha:
            return {"clip": clip, "name": name, "reference": reference_kind, "manifest": manifest, "rows": previous["rows"], "diag": previous["diag_summary"], "reused": True}

    candidate = load_candidate(tracks, video_id, None, None, name)
    video_item = candidate.provenance.extra.get("inputs", {}).get("video")
    video = Path(video_item["path"]) if video_item and Path(video_item["path"]).exists() else None
    if reference_kind == "gt":
        reference = load_gt_run(gt_path(clip), video_id, video_path=video, detections_csv=KIT_ROOT / "ground_truth" / f"{video_id}_detections_corrected.csv")
        frames = CLIPS[clip]["frames"]
    else:
        reference = load_cloud_run(cloud_path(clip), video_id, video_path=video)
        frames = None
    report = evaluate(candidate, reference, region=CLIPS[clip]["region"], frame_range=frames)
    report.settings["candidate_output_sha256"] = output_sha
    payload = report.to_json()
    diag_summary = {
        key: {"switches": len(d.identity_switches), "fragmentation": d.fragmentation, "orphans": len(d.orphan_candidate_ids), "ids": d.candidate_ids, "objects": d.reference_objects}
        for key, d in report.diagnostics.items()
    }
    payload["diag_summary"] = diag_summary
    report_base.parent.mkdir(parents=True, exist_ok=True)
    Path(str(report_base) + ".md").write_text(render_markdown(report))
    json_path.write_text(json.dumps(payload, indent=1))
    return {"clip": clip, "name": name, "reference": reference_kind, "manifest": manifest, "rows": payload["rows"], "diag": diag_summary, "reused": False}


def pick(rows: list[dict], view: str, px: float, region: bool) -> dict | None:
    for row in rows:
        if row["view"] == view and row["match_px"] == px and row["ignore_region"] == region:
            return row
    # fall back to the only region option available (turbine has no region)
    for row in rows:
        if row["view"] == view and row["match_px"] == px:
            return row
    return None


def fmt(row: dict | None, key: str) -> str:
    if row is None:
        return "-"
    value = row["metrics"][key]
    return f"{value:.3f}" if isinstance(value, float) and key not in ("IDSW", "Frag") else f"{int(value)}"


def discover(runs_root: Path) -> list[tuple[str, str, Path]]:
    found = []
    for clip in CLIPS:
        for tracks in sorted((runs_root / clip).glob("*/tracks.csv")):
            found.append((clip, tracks.parent.name, tracks))
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--runs-root", type=Path, default=KIT_ROOT / "outputs/runs")
    parser.add_argument("--out", type=Path, default=KIT_ROOT / "outputs/reports")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--px", type=float, default=8.0)
    args = parser.parse_args()

    jobs = []
    for clip, name, tracks in discover(args.runs_root):
        jobs.append((clip, name, tracks, "gt"))
        if name in ("real_default",):
            jobs.append((clip, name, tracks, "cloud"))
    for clip, cfg in CLIPS.items():  # frozen baselines from results/
        frozen = KIT_ROOT / cfg["frozen"]
        jobs.append((clip, "frozen_baseline", frozen, "gt"))
        jobs.append((clip, "frozen_baseline", frozen, "cloud"))

    results = []
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(evaluate_one, clip, name, tracks, args.out, kind): (clip, name, kind) for clip, name, tracks, kind in jobs}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"[{'reused' if result['reused'] else 'done'}] {result['clip']}/{result['name']} vs {result['reference']}", flush=True)

    by_key = {(r["clip"], r["name"], r["reference"]): r for r in results}
    px = args.px
    lines = ["# Experiment summary", "",
             f"Match distance {px:g} px (T = {2 * px:g}); HOTA/DetA/AssA = TrackEval mean over alphas; flock scored with the timestamp overlay ignored; turbine accuracy restricted to frames {TURBINE_GT_FRAMES[0]}..{TURBINE_GT_FRAMES[1]}. "
             "`obs` = matched rows only (10-column runs), `all` = every row as written. Per-run reports with provenance, sensitivity (4/6/8/12 px), both views, with/without region, and the identity-switch lists are in runs/<clip>/.", ""]

    def table(title: str, keys: list[tuple[str, str, str, str]], view_label: bool = True):
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| run | claim | view | HOTA | DetA | AssA | MOTA | IDF1 | IDSW | Frag | TP | FP | FN | ids | objects | switches (diag) | orphans |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for clip, name, kind, label in keys:
            r = by_key.get((clip, name, kind))
            if r is None:
                lines.append(f"| {label} | {kind} | missing | | | | | | | | | | | | | | |")
                continue
            claim = "accuracy" if kind == "gt" else "parity"
            region = clip == "flock"
            for view in ("observations", "updates"):
                row = pick(r["rows"], view, px, region)
                if row is None:
                    continue
                diag = r["diag"].get(f"{view}|{'region' if region else 'noregion'}", {})
                lines.append(
                    f"| {label} | {claim} | {'obs' if view == 'observations' else 'all'} | {fmt(row, 'HOTA')} | {fmt(row, 'DetA')} | {fmt(row, 'AssA')} | {fmt(row, 'MOTA')} | {fmt(row, 'IDF1')} | "
                    f"{fmt(row, 'IDSW')} | {fmt(row, 'Frag')} | {fmt(row, 'CLR_TP')} | {fmt(row, 'CLR_FP')} | {fmt(row, 'CLR_FN')} | {fmt(row, 'num_tracker_ids')} | {fmt(row, 'num_gt_ids')} | "
                    f"{diag.get('switches', '-')} | {diag.get('orphans', '-')} |"
                )
        lines.append("")

    table("E1 accuracy: frozen baseline against ground truth", [
        ("flock", "frozen_baseline", "gt", "flock results/flock/baseline_tracks.csv"),
        ("flock", "real_default", "gt", "flock real_default (same run, 10 columns)"),
        ("turbine", "frozen_baseline", "gt", "turbine results/turbine/baseline_tracks.csv"),
        ("turbine", "real_default", "gt", "turbine real_default (same run, 10 columns)"),
    ])
    table("E2 parity: frozen baseline against the cloud export", [
        ("flock", "frozen_baseline", "cloud", "flock baseline vs cloud"),
        ("flock", "real_default", "cloud", "flock real_default vs cloud"),
        ("turbine", "frozen_baseline", "cloud", "turbine baseline vs cloud"),
        ("turbine", "real_default", "cloud", "turbine real_default vs cloud"),
    ])
    table("E3 association ceiling: ground truth as detections", [
        ("flock", "gt_default", "gt", "flock gt-as-detections"),
        ("turbine", "gt_default", "gt", "turbine gt-as-detections"),
    ])

    # E4: degraded GT, grouped by (drop, noise, fp) over seeds
    e4 = [r for r in results if r["clip"] == "flock" and r["name"].startswith("gtdeg_") and r["reference"] == "gt"]
    if e4:
        groups: dict[tuple, list] = {}
        for r in e4:
            params = r["manifest"].get("inputs", {}).get("detections", {}).get("details", {}).get("params", {})
            key = (params.get("drop_rate"), params.get("center_noise_px"), params.get("false_positives_per_frame"))
            groups.setdefault(key, []).append(r)
        lines.append("## E4 robustness: ground truth degraded (flock), matched rows, mean +- spread over seeds")
        lines.append("")
        lines.append("| drop | noise px | FP/frame | seeds | HOTA | DetA | AssA | IDF1 | IDSW | ids | FP | FN |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for key in sorted(groups, key=lambda k: tuple(x if x is not None else -1 for x in k)):
            rows = [pick(r["rows"], "observations", px, True) for r in groups[key]]
            rows = [row for row in rows if row]
            if not rows:
                continue

            def ms(field):
                values = [row["metrics"][field] for row in rows]
                mean = statistics.mean(values)
                spread = (max(values) - min(values)) / 2 if len(values) > 1 else 0.0
                return f"{mean:.3f} +- {spread:.3f}" if field not in ("IDSW", "num_tracker_ids", "CLR_FP", "CLR_FN") else f"{mean:.1f} +- {spread:.1f}"

            lines.append(f"| {key[0]} | {key[1]} | {key[2]} | {len(rows)} | {ms('HOTA')} | {ms('DetA')} | {ms('AssA')} | {ms('IDF1')} | {ms('IDSW')} | {ms('num_tracker_ids')} | {ms('CLR_FP')} | {ms('CLR_FN')} |")
        lines.append("")
        lines.append("Curves (HOTA / IDF1 against drop rate, one line per noise and FP level):")
        lines.append("")
        drops = sorted({k[0] for k in groups})
        lines.append("| noise px | FP/frame | metric | " + " | ".join(f"drop {d}" for d in drops) + " |")
        lines.append("|---|---|---|" + "---|" * len(drops))
        for noise in sorted({k[1] for k in groups}):
            for fp in sorted({k[2] for k in groups}):
                for metric in ("HOTA", "IDF1", "IDSW"):
                    cells = []
                    for d in drops:
                        rows = [pick(r["rows"], "observations", px, True) for r in groups.get((d, noise, fp), [])]
                        rows = [row for row in rows if row]
                        cells.append(f"{statistics.mean(row['metrics'][metric] for row in rows):.3f}" if rows and metric != "IDSW" else (f"{statistics.mean(row['metrics'][metric] for row in rows):.1f}" if rows else "-"))
                    lines.append(f"| {noise} | {fp} | {metric} | " + " | ".join(cells) + " |")
        lines.append("")

    # E5: parameter grid
    for clip in ("flock", "turbine"):
        e5 = [r for r in results if r["clip"] == clip and (r["name"].startswith("real_maxage") or r["name"] == "real_default") and r["reference"] == "gt"]
        if not e5:
            continue
        region = clip == "flock"
        lines.append(f"## E5 parameters ({clip}, real detections, matched rows, against ground truth)")
        lines.append("")
        lines.append("| max_age | tentative_threshold | HOTA | DetA | AssA | MOTA | IDF1 | IDSW | Frag | TP | FP | FN | ids | orphans |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        entries = []
        for r in e5:
            params = r["manifest"].get("tracker", {}).get("params", {})
            entries.append((params.get("max_age"), params.get("tentative_threshold"), r))
        for max_age, tentative, r in sorted(entries, key=lambda e: (e[0] or 0, e[1] or 0)):
            row = pick(r["rows"], "observations", px, region)
            diag = r["diag"].get(f"observations|{'region' if region else 'noregion'}", {})
            lines.append(f"| {max_age} | {tentative} | {fmt(row, 'HOTA')} | {fmt(row, 'DetA')} | {fmt(row, 'AssA')} | {fmt(row, 'MOTA')} | {fmt(row, 'IDF1')} | {fmt(row, 'IDSW')} | {fmt(row, 'Frag')} | {fmt(row, 'CLR_TP')} | {fmt(row, 'CLR_FP')} | {fmt(row, 'CLR_FN')} | {fmt(row, 'num_tracker_ids')} | {diag.get('orphans', '-')} |")
        lines.append("")

    # sensitivity for the headline runs
    lines.append("## Sensitivity to the match distance (matched rows, overlay ignored for the flock)")
    lines.append("")
    lines.append("| run | px | HOTA | DetA | AssA | IDF1 | IDSW | TP | FP | FN |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for clip, name in (("flock", "real_default"), ("flock", "gt_default"), ("turbine", "real_default"), ("turbine", "gt_default")):
        r = by_key.get((clip, name, "gt"))
        if r is None:
            continue
        for row in r["rows"]:
            if row["view"] == "observations" and row["ignore_region"] == (clip == "flock"):
                lines.append(f"| {clip}/{name} | {row['match_px']:g} | {fmt(row, 'HOTA')} | {fmt(row, 'DetA')} | {fmt(row, 'AssA')} | {fmt(row, 'IDF1')} | {fmt(row, 'IDSW')} | {fmt(row, 'CLR_TP')} | {fmt(row, 'CLR_FP')} | {fmt(row, 'CLR_FN')} |")
    lines.append("")

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "SUMMARY.md").write_text("\n".join(lines) + "\n")
    (args.out / "summary_rows.json").write_text(json.dumps([{k: v for k, v in r.items() if k != "manifest"} | {"params": r["manifest"].get("tracker", {}).get("params"), "degradation": r["manifest"].get("inputs", {}).get("detections", {}).get("details", {}).get("params")} for r in results], indent=1))
    print(f"wrote {args.out / 'SUMMARY.md'} ({len(results)} evaluations)")


if __name__ == "__main__":
    main()
