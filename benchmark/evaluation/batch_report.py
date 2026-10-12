"""Evaluate every run under ``outputs/runs`` and write the experiment summary.

    python evaluation/batch_report.py [--jobs 4]

For each ``outputs/runs/<clip>/<tracker>/<run>/tracks.csv``: one accuracy report against the
clip's ground truth (``outputs/reports/runs/<clip>/<tracker>__<run>__vs_gt.md|.json``), skipped when a report
for the same output sha256 already exists; the default run is also scored against the cloud
export (parity). Then ``SUMMARY.md`` with the experiment tables and ``summary_rows.json`` for
the dashboard. Reads CSVs and manifests only; never runs the tracker.

Run names under each tracker: ``real_default`` (real detections, default parameters; for
simplesort byte-identical to the frozen baseline in ``tracker_kit/results/``), ``gt_default``
(ground-truth boxes as detections, E3), ``gtdeg_*`` (E4), ``real_maxage*_tent*`` (E5). Each summary row
carries the tracker algorithm, library and detection source from the run manifest.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from paths import REPORTS, RUNS  # noqa: E402  (also puts benchmark/ and tracker_kit/ on sys.path)

from evaluation.adapters import load_cloud_run, load_gt_run  # noqa: E402
from evaluation.cli import load_candidate  # noqa: E402
from evaluation.clips import load_clips  # noqa: E402
from evaluation.evaluate import TABLE_METRICS, evaluate, render_markdown  # noqa: E402

CLIPS = load_clips()
HEADER = "| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |"
RULE = "|---|---|---|---|---|---|---|---|"


def evaluate_one(clip: str, tracker: str, name: str, tracks: Path, out_dir: Path, reference_kind: str) -> dict:
    """Worker: evaluate ``tracks`` against gt or cloud, write the report files, return a summary."""
    video_id = CLIPS[clip]["video_id"]
    manifest_path = tracks.with_suffix(tracks.suffix + ".manifest.json")
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    output_sha = manifest.get("output", {}).get("sha256", "")
    base = out_dir / "runs" / clip / f"{tracker}__{name}__vs_{reference_kind}"
    json_path = Path(str(base) + ".json")
    summary = {"clip": clip, "name": name, "reference": reference_kind,
               "tracker": manifest.get("tracker", {}).get("algorithm", tracker),
               "library": manifest.get("tracker", {}).get("library", "spoor tracker-kit (tracker/)"),
               "detection_source": manifest.get("inputs", {}).get("detections", {}).get("source", "unknown"),
               "label": manifest.get("label"),
               "params": manifest.get("tracker", {}).get("params"),
               "degradation": manifest.get("inputs", {}).get("detections", {}).get("details", {}).get("params")}

    if json_path.exists() and output_sha:
        previous = json.loads(json_path.read_text())
        if previous.get("settings", {}).get("candidate_output_sha256") == output_sha:
            return {**summary, "rows": previous["rows"], "reused": True}

    candidate = load_candidate(tracks, video_id, None, None, f"{tracker}/{name}")
    video_item = candidate.provenance.extra.get("inputs", {}).get("video")
    video = Path(video_item["path"]) if video_item and Path(video_item["path"]).exists() else None
    if reference_kind == "gt":
        reference = load_gt_run(CLIPS[clip]["gt_tracks"], video_id, video_path=video, detections_csv=CLIPS[clip]["gt_detections"], dataset=clip)
        frames = CLIPS[clip]["frames"]
    else:
        reference = load_cloud_run(CLIPS[clip]["cloud"], video_id, video_path=video, dataset=clip)
        frames = None
    report = evaluate(candidate, reference, region=CLIPS[clip]["region"], frame_range=frames)
    report.settings["candidate_output_sha256"] = output_sha
    base.parent.mkdir(parents=True, exist_ok=True)
    Path(str(base) + ".md").write_text(render_markdown(report))
    payload = report.to_json()
    json_path.write_text(json.dumps(payload, indent=1))
    return {**summary, "rows": payload["rows"], "reused": False}


def pick(rows: list[dict], view: str, px: float, region: bool) -> dict | None:
    """The row for a view/px, with the region when the clip has one."""
    candidates = [r for r in rows if r["view"] == view and r["match_px"] == px]
    with_region = [r for r in candidates if r["ignore_region"] == region]
    return (with_region or candidates or [None])[0]


def cells(row: dict | None) -> str:
    if row is None:
        return " | ".join("-" for _ in TABLE_METRICS)
    m = row["metrics"]
    return " | ".join(f"{m[k]:.2f}" if k == "MOTP_px" else (f"{m[k]:.0f}" if k in ("IDSW", "Frag") else f"{m[k]:.3f}") for k in TABLE_METRICS)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--runs-root", type=Path, default=RUNS)
    parser.add_argument("--out", type=Path, default=REPORTS)
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--px", type=float, default=8.0)
    args = parser.parse_args()

    jobs = []
    for clip in CLIPS:
        for tracks in sorted((args.runs_root / clip).glob("*/*/tracks.csv")):
            tracker, name = tracks.parent.parent.name, tracks.parent.name
            jobs.append((clip, tracker, name, tracks, "gt"))
            if name == "real_default" and CLIPS[clip]["cloud"] is not None:
                jobs.append((clip, tracker, name, tracks, "cloud"))

    results = []
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(evaluate_one, clip, tracker, name, tracks, args.out, kind): name for clip, tracker, name, tracks, kind in jobs}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"[{'reused' if result['reused'] else 'done'}] {result['clip']}/{result['tracker']}/{result['name']} vs {result['reference']}", flush=True)
    by_key = {(r["clip"], r["tracker"], r["name"], r["reference"]): r for r in results}
    px = args.px

    def has_region(clip):
        return CLIPS[clip]["region"] is not None

    def row_for(clip, name, kind, view, tracker="simplesort"):
        r = by_key.get((clip, tracker, name, kind))
        return pick(r["rows"], view, px, has_region(clip)) if r else None

    clip_notes = "; ".join(f"{name}: {c['note']}" for name, c in CLIPS.items())
    lines = ["# Experiment summary", "",
             f"Match distance {px:g} px (T = {2 * px:g}). Clips: {clip_notes}. Ignore regions and labelled frame ranges from clips.json. "
             "`obs` = matched rows only, `all` = every row as written (coasting included). "
             "Per-run reports (provenance, 4/6/8/12 px, both views, with/without region, identity-switch lists) are in runs/<clip>/.", "",
             "HOTA = sqrt(DetA * AssA), the overall score. AssA = association accuracy (one bird keeps one id, one id keeps one bird). "
             "MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. "
             "IDF1 = identity F1. IDSW = identity switches. Frag = fragmentations (CLEAR definition; the flock GT's own 111 gaps give a floor "
             "of about 111 even to a perfect tracker). Other TrackEval fields stay in the per-run JSON reports.", ""]

    def section(title: str, entries: list[tuple[str, str, str, str]]):
        lines.extend([f"## {title}", "", HEADER, RULE])
        for clip, name, kind, label in entries:
            for view, tag in (("observations", "obs"), ("updates", "all")):
                row = row_for(clip, name, kind, view)
                if row is not None:
                    lines.append(f"| {label} ({tag}) | {cells(row)} |")
        lines.append("")

    for clip in CLIPS:
        for source, title in (("real", "real detections"), ("gt", "ground-truth boxes as detections")):
            runs = sorted((r for r in results if r["clip"] == clip and r["reference"] == "gt" and r["detection_source"] == source
                           and r["name"] in ("real_default", "gt_default")), key=lambda r: r["tracker"])
            if runs:
                lines.extend([f"## Trackers compared ({clip}, {title}, matched rows, default parameters)", "", HEADER, RULE])
                for r in runs:
                    label = f"{r['tracker']} ({r['library']})"
                    lines.append(f"| {label} | {cells(pick(r['rows'], 'observations', px, has_region(clip)))} |")
                lines.append("")

    section("E1 accuracy: baseline (real detections, default parameters) against ground truth",
            [("flock", "real_default", "gt", "flock"), ("turbine", "real_default", "gt", "turbine")])
    section("E2 parity: baseline against the cloud export",
            [("flock", "real_default", "cloud", "flock"), ("turbine", "real_default", "cloud", "turbine")])
    section("E3 association ceiling: ground truth as detections",
            [("flock", "gt_default", "gt", "flock"), ("turbine", "gt_default", "gt", "turbine")])

    e4 = [r for r in results if r["clip"] == "flock" and r["tracker"] == "simplesort" and r["name"].startswith("gtdeg_") and r["reference"] == "gt" and r["degradation"]]
    if e4:
        groups: dict[tuple, list] = {}
        for r in e4:
            d = r["degradation"]
            groups.setdefault((d["drop_rate"], d["center_noise_px"], d["false_positives_per_frame"]), []).append(pick(r["rows"], "observations", px, True))
        lines += ["## E4 robustness: degraded ground truth (flock, matched rows), mean +- half-range over seeds", "",
                  "| drop | noise px | FP/frame | seeds | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for key in sorted(groups):
            rows = [r for r in groups[key] if r]
            def ms(metric, digits):
                values = [r["metrics"][metric] for r in rows]
                return f"{statistics.mean(values):.{digits}f} +- {(max(values) - min(values)) / 2:.{digits}f}"
            lines.append(f"| {key[0]} | {key[1]} | {key[2]} | {len(rows)} | {ms('HOTA', 3)} | {ms('AssA', 3)} | {ms('MOTA', 3)} | "
                         f"{ms('MOTP_px', 2)} | {ms('IDF1', 3)} | {ms('IDSW', 1)} | {ms('Frag', 1)} |")
        lines.append("")

    for clip in CLIPS:
        e5 = [r for r in results if r["clip"] == clip and r["reference"] == "gt" and r["tracker"] == "simplesort" and (r["name"].startswith("real_maxage") or r["name"] == "real_default")]
        if len(e5) > 1:
            lines += [f"## E5 parameters ({clip}, real detections, matched rows)", "",
                      "| max_age | tentative_threshold | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |", "|---|---|---|---|---|---|---|---|---|"]
            for r in sorted(e5, key=lambda r: (r["params"]["max_age"], r["params"]["tentative_threshold"])):
                lines.append(f"| {r['params']['max_age']} | {r['params']['tentative_threshold']} | {cells(pick(r['rows'], 'observations', px, has_region(clip)))} |")
            lines.append("")

    lines += ["## Sensitivity to the match distance (matched rows)", "", "| run | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |", "|---|---|---|---|---|---|---|---|---|"]
    for clip, name in (("flock", "real_default"), ("flock", "gt_default"), ("turbine", "real_default"), ("turbine", "gt_default")):
        r = by_key.get((clip, "simplesort", name, "gt"))
        for row in (r["rows"] if r else []):
            if row["view"] == "observations" and row["ignore_region"] == has_region(clip):
                lines.append(f"| {clip}/{name} | {row['match_px']:g} | {cells(row)} |")
    lines.append("")

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "SUMMARY.md").write_text("\n".join(lines))
    (args.out / "summary_rows.json").write_text(json.dumps(results, indent=1))
    print(f"wrote {args.out / 'SUMMARY.md'} ({len(results)} evaluations)")


if __name__ == "__main__":
    main()
