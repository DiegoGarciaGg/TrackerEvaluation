"""Report one tracker run against one reference, from explicit paths.

    python evaluation/cli.py \
        --tracks outputs/runs/flock/real_default/tracks.csv \
        --reference ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv --reference-kind gt \
        --video-id 20251012_164031_1DAC \
        --out outputs/reports/flock_real_default_vs_gt \
        [--px 4 6 8 12] [--default-px 8] [--ignore-rect 0 0 721 400] [--frames 53 293] \
        [--video data/20251012_164031_1DAC.mp4] [--detections data/..._detections.csv]

Writes ``<out>.md`` (human report) and ``<out>.json`` (everything, including the full switch
list and per-track durations) and persists both runs in the store (``outputs/store``) under
references ``<dataset>|<video_id>|<dimension>``. The claim printed at the top of the report
follows the reference kind: ``gt`` -> accuracy, ``cloud`` -> parity, ``tracks`` (another tracker
CSV, e.g. the frozen baseline) -> regression. Never runs the tracker, never opens a video.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from evaluation.adapters import load_cloud_run, load_gt_run, load_tracker_run  # noqa: E402
from evaluation.evaluate import evaluate, render_markdown  # noqa: E402
from evaluation.hashing import sha256_tree  # noqa: E402
from evaluation.provenance import store_ref  # noqa: E402
from evaluation.store import JsonlResultStore  # noqa: E402
from evaluation.views import FLOCK_TIMESTAMP_OVERLAY, IgnoreRegion  # noqa: E402

TURBINE_GT_FRAMES = (53, 293)


def load_candidate(tracks: Path, video_id: str, video: Path | None, detections: Path | None, label: str | None, claim: str = "candidate"):
    manifest_path = tracks.with_suffix(tracks.suffix + ".manifest.json")
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    params = manifest.get("tracker", {}).get("params")
    detection_source = manifest.get("inputs", {}).get("detections", {}).get("source")
    detections = detections or (Path(manifest["inputs"]["detections"]["path"]) if manifest else None)
    video = video or (Path(manifest["inputs"]["video"]["path"]) if manifest else None)
    extra = {}
    if manifest:
        extra["run_manifest"] = {
            "run_key": manifest.get("run_key"),
            "label": manifest.get("label"),
            "created_utc": manifest.get("created_utc"),
            "elapsed_seconds": manifest.get("elapsed_seconds"),
            "degradation": manifest.get("inputs", {}).get("detections", {}).get("details", {}).get("params"),
            "baseline_check": manifest.get("baseline_check"),
        }
    return load_tracker_run(
        tracks,
        video_id,
        claim=claim,
        tracker_params=params,
        detections_csv=detections if detections and Path(detections).exists() else None,
        detection_source=detection_source,
        tracker_source_hash=manifest.get("tracker", {}).get("source_hash") or sha256_tree(KIT_ROOT / "tracker"),
        video_path=video if video and Path(video).exists() else None,
        notes=[label] if label else None,
        **extra,
    )


def load_reference(kind: str, path: Path, video_id: str, video: Path | None):
    if kind == "gt":
        detections_csv = path.with_name(path.name.replace("_reference_tracks_corrected", "_detections_corrected"))
        return load_gt_run(path, video_id, video_path=video, detections_csv=detections_csv if detections_csv.exists() else None)
    if kind == "cloud":
        return load_cloud_run(path, video_id, video_path=video)
    if kind == "tracks":
        return load_candidate(path, video_id, video, None, "frozen reference run", claim="regression")
    raise SystemExit(f"unknown --reference-kind {kind}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tracks", type=Path, required=True, help="candidate tracker CSV (6 or 10 columns)")
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--reference-kind", choices=["gt", "cloud", "tracks"], required=True)
    parser.add_argument("--video-id", required=True)
    parser.add_argument("--out", type=Path, required=True, help="report path without extension")
    parser.add_argument("--px", type=float, nargs="+", default=[4.0, 6.0, 8.0, 12.0])
    parser.add_argument("--default-px", type=float, default=8.0)
    parser.add_argument("--ignore-rect", type=float, nargs=4, action="append", metavar=("X1", "Y1", "X2", "Y2"), default=None,
                        help="ignore rectangle (repeatable); default: the flock timestamp overlay for the flock clip, none otherwise")
    parser.add_argument("--no-ignore", action="store_true", help="disable the default ignore region")
    parser.add_argument("--frames", type=int, nargs=2, metavar=("FIRST", "LAST"), default=None,
                        help="restrict scoring to this frame range; default: 53..293 for the turbine clip against gt")
    parser.add_argument("--reference-proximity-px", type=float, default=None,
                        help="drop candidate rows farther than this from every labelled object in their frame (partially labelled clips)")
    parser.add_argument("--video", type=Path, default=None)
    parser.add_argument("--detections", type=Path, default=None)
    parser.add_argument("--label", default=None)
    parser.add_argument("--store", type=Path, default=KIT_ROOT / "outputs/store")
    parser.add_argument("--candidate-ref", default=None, help="store reference dimension for the candidate, e.g. kit:maxage15")
    args = parser.parse_args()

    candidate = load_candidate(args.tracks, args.video_id, args.video, args.detections, args.label)
    video_item = candidate.provenance.extra.get("inputs", {}).get("video")
    video = args.video or (Path(video_item["path"]) if video_item else None)
    reference = load_reference(args.reference_kind, args.reference, args.video_id, video if video and video.exists() else None)

    region = None
    if args.ignore_rect:
        region = IgnoreRegion(rects=tuple(tuple(r) for r in args.ignore_rect), label="user rectangles")
    elif not args.no_ignore and args.video_id == "20251012_164031_1DAC":
        region = FLOCK_TIMESTAMP_OVERLAY
    frames = tuple(args.frames) if args.frames else (TURBINE_GT_FRAMES if (args.video_id == "20250920_063942_6C42" and args.reference_kind == "gt") else None)

    report = evaluate(candidate, reference, match_px=args.px, default_px=args.default_px, region=region, frame_range=frames,
                      reference_proximity_px=args.reference_proximity_px)

    store = JsonlResultStore(args.store)
    reference_dim = {"gt": "gt", "cloud": "baseline:cloud", "tracks": "kit:reference"}[args.reference_kind]
    reference_id = store.persist(reference, ref=store_ref(reference.provenance, reference_dim))
    candidate_id = store.persist(candidate, ref=store_ref(candidate.provenance, args.candidate_ref) if args.candidate_ref else None)
    report.settings["store"] = {"root": str(args.store), "candidate_run_id": candidate_id, "reference_run_id": reference_id}

    args.out.parent.mkdir(parents=True, exist_ok=True)
    Path(str(args.out) + ".md").write_text(render_markdown(report))
    Path(str(args.out) + ".json").write_text(json.dumps(report.to_json(), indent=1))
    row = report.row(report.settings["candidate_views"][0], args.default_px, region is not None) or report.rows[0]
    m = row.metrics
    print(f"claim={report.claim} view={row.view} px={row.match_px:g} region={'on' if row.ignore_region else 'off'}: "
          f"HOTA={m['HOTA']:.3f} DetA={m['DetA']:.3f} AssA={m['AssA']:.3f} MOTA={m['MOTA']:.3f} IDF1={m['IDF1']:.3f} IDSW={m['IDSW']} "
          f"ids={m['num_tracker_ids']} vs objects={m['num_gt_ids']}")
    print(f"wrote {args.out}.md and .json; store ids candidate={candidate_id} reference={reference_id}")


if __name__ == "__main__":
    main()
