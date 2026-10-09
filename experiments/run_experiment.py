"""Run the kit tracker over a detections CSV and write the track CSV with provenance.

    python experiments/run_experiment.py \
        --video data/20251012_164031_1DAC.mp4 \
        --detections data/20251012_164031_1DAC_detections.csv --detection-source real \
        --out outputs/runs/flock_real_default/tracks.csv \
        [--max-age 30 --tentative-threshold 3 --euclidean-matching-threshold 250] \
        [--check-baseline results/flock/baseline_tracks.csv]

The tracker is imported from ``tracker/`` without modification and driven exactly as
``run_tracker.py`` drives it (its own ``load_detections_by_frame``, ``build_detections`` and
``check_frame_alignment`` are reused, one ``match_and_track`` call per video frame, in order).
The video is opened only for its frame count and fps; no frame is decoded and no annotated
video is written, which is why a run here takes the same ~4 minutes the tracker needs and not
the extra decode/encode time.

Output CSV columns: the six ``run_tracker.py`` writes (``frame_number, track_id, x, y, w, h``,
same values and formatting, one row per CONFIRMED track per frame) plus four with the repo's
``TrackUpdate`` semantics:

- ``matched``: 1 if the track was matched to a detection in this frame, else 0 (coasting). The
  criterion is ``track.detections[-1].frame_number == frame_number``; Phase 0 verified it agrees
  with the kit's ``age == 1`` after ``match_and_track`` on every baseline row.
- ``detection_count``: ``len(track.detections)``, detections accumulated so far (the first row of
  a track therefore shows ``tentative_threshold``).
- ``missed_frame_count``: consecutive frames without a match, this one included; the kit's
  ``age - 1``. 0 on a matched row.
- ``age_frames``: frames since the track's first detection, inclusive.

``--check-baseline`` compares the six-column projection of the output byte for byte with the
given file and exits non-zero on any difference. A manifest ``<out>.manifest.json`` is written
next to the CSV with every input's sha256, the tracker parameters, the hash of ``tracker/`` and
``run_tracker.py``, the detection source label, the environment and the output's sha256.
Re-running with identical inputs and parameters finds the manifest and skips the run unless
``--force`` is given.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

KIT_ROOT = Path(__file__).resolve().parent.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

import numpy  # noqa: E402

import run_tracker  # noqa: E402  (the kit's runner: reused helpers, unchanged)
from evaluation.hashing import sha256_file, sha256_json, sha256_tree  # noqa: E402
from tracker.simple_sort_tracker import SimpleSORTTracker  # noqa: E402
from tracker.tracked_object_state import TrackedObjectState  # noqa: E402

BASELINE_FIELDS = ["frame_number", "track_id", "x", "y", "w", "h"]
EXTENDED_FIELDS = BASELINE_FIELDS + ["matched", "detection_count", "missed_frame_count", "age_frames"]
DEFAULT_PARAMS = {
    "euclidean_matching_threshold": run_tracker.REFERENCE_EUCLIDEAN_MATCHING_THRESHOLD,
    "max_age": run_tracker.DEFAULT_MAX_AGE,
    "tentative_threshold": run_tracker.DEFAULT_TENTATIVE_THRESHOLD,
}


def video_frame_count_and_fps(video_path: Path) -> tuple[int, float]:
    """Frame count and fps as ``run_tracker.py`` reads them (no frame is decoded)."""
    import cv2

    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise RuntimeError(f"could not open video {video_path}")
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = capture.get(cv2.CAP_PROP_FPS) or 10.0
    capture.release()
    return frame_count, fps


def track_rows(
    detections_by_frame: dict,
    frame_count: int,
    fps: float,
    params: dict,
) -> list[dict]:
    """Drive the tracker exactly like ``run_tracker.run`` and collect extended rows."""
    tracker = SimpleSORTTracker(
        euclidean_matching_threshold=params["euclidean_matching_threshold"],
        max_age=params["max_age"],
        tentative_threshold=params["tentative_threshold"],
    )
    rows: list[dict] = []
    for frame_number in range(frame_count):
        frame_timestamp = round(frame_number * 1000 / fps)
        boxes = detections_by_frame.get(frame_number, [])
        detections = run_tracker.build_detections(frame_number, frame_timestamp, boxes)
        tracker.match_and_track(detections)
        for tracked_object in tracker.tracked_objects:
            if tracked_object.state != TrackedObjectState.CONFIRMED:
                continue
            last = tracked_object.detections[-1]
            box = last.bounding_box
            matched = last.frame_number == frame_number
            rows.append(
                {
                    "frame_number": frame_number,
                    "track_id": tracked_object.id,
                    "x": box.x1,
                    "y": box.y1,
                    "w": box.width,
                    "h": box.height,
                    "matched": int(matched),
                    "detection_count": len(tracked_object.detections),
                    "missed_frame_count": tracked_object.age - 1,
                    "age_frames": frame_number - tracked_object.detections[0].frame_number + 1,
                }
            )
    tracker.finalize_tracking()
    return rows


def rows_to_csv_text(rows: list[dict], fields: list[str]) -> str:
    """Render rows with ``csv.DictWriter`` so numbers format exactly as ``run_tracker.py``'s."""
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, extrasaction="ignore", lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def run_key(detections_path: Path, video_path: Path, params: dict, tracker_hash: str) -> str:
    return sha256_json(
        {
            "detections_sha256": sha256_file(detections_path),
            "video_sha256": sha256_file(video_path),
            "params": params,
            "tracker_source_hash": tracker_hash,
            "run_tracker_sha256": sha256_file(KIT_ROOT / "run_tracker.py"),
            "extended_fields": EXTENDED_FIELDS,
        }
    )


def run_experiment(
    video_path: Path,
    detections_path: Path,
    out_path: Path,
    params: Optional[dict] = None,
    detection_source: str = "real",
    detection_source_details: Optional[dict] = None,
    label: Optional[str] = None,
    check_baseline: Optional[Path] = None,
    force: bool = False,
    allow_partial_coverage: bool = False,
) -> dict:
    """Run (or reuse) one tracker run; returns the manifest dict.

    ``allow_partial_coverage`` relaxes ``run_tracker.check_frame_alignment`` for a CSV whose frames
    lie strictly inside ``0..frame_count-1`` without starting at 0 or ending at the last frame
    (the turbine ground truth covers frames 53..293 of 671). The check exists to catch a cut
    CSV fed to an uncut video; a CSV already in the clip's numbering that simply has no boxes
    on the first or last frames is legitimate input (absent frames are empty frames), and the
    manifest records that the check was relaxed.
    """
    params = {**DEFAULT_PARAMS, **(params or {})}
    out_path = Path(out_path)
    manifest_path = out_path.with_suffix(out_path.suffix + ".manifest.json")
    tracker_hash = sha256_tree(KIT_ROOT / "tracker")
    key = run_key(detections_path, video_path, params, tracker_hash)

    if manifest_path.exists() and out_path.exists() and not force:
        previous = json.loads(manifest_path.read_text())
        if previous.get("run_key") == key and sha256_file(out_path) == previous["output"]["sha256"]:
            previous["reused"] = True
            return previous

    frame_count, fps = video_frame_count_and_fps(video_path)
    detections_by_frame = run_tracker.load_detections_by_frame(detections_path)
    alignment = "run_tracker.check_frame_alignment passed"
    inside = detections_by_frame and 0 <= min(detections_by_frame) and max(detections_by_frame) <= frame_count - 1
    if allow_partial_coverage and inside:
        alignment = (
            f"check relaxed (--allow-partial-coverage): CSV frames {min(detections_by_frame)}..{max(detections_by_frame)} "
            f"lie inside the video's 0..{frame_count - 1}; absent frames are treated as empty"
        )
    else:
        run_tracker.check_frame_alignment(detections_by_frame, frame_count, video_path, detections_path)

    started = time.time()
    rows = track_rows(detections_by_frame, frame_count, fps, params)
    elapsed = time.time() - started

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(rows_to_csv_text(rows, EXTENDED_FIELDS).encode())

    baseline_check = None
    if check_baseline is not None:
        projection = rows_to_csv_text(rows, BASELINE_FIELDS).encode()
        expected = Path(check_baseline).read_bytes()
        baseline_check = {
            "path": str(check_baseline),
            "sha256": sha256_file(check_baseline),
            "identical_bytes": projection == expected,
            "rows_ours": len(rows),
            "rows_baseline": expected.count(b"\n") - 1,
        }

    matched_rows = sum(row["matched"] for row in rows)
    manifest = {
        "run_key": key,
        "label": label,
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "command": " ".join(sys.argv),
        "inputs": {
            "video": {"path": str(video_path), "sha256": sha256_file(video_path), "frame_count": frame_count, "fps": fps},
            "detections": {
                "path": str(detections_path),
                "sha256": sha256_file(detections_path),
                "source": detection_source,
                "details": detection_source_details or {},
                "rows": sum(len(boxes) for boxes in detections_by_frame.values()),
                "frame_alignment": alignment,
            },
        },
        "tracker": {
            "params": params,
            "source_dir": str(KIT_ROOT / "tracker"),
            "source_hash": tracker_hash,
            "run_tracker_sha256": sha256_file(KIT_ROOT / "run_tracker.py"),
            "driver": "experiments/run_experiment.py (no frames decoded, no annotated video)",
        },
        "output": {
            "path": str(out_path),
            "sha256": sha256_file(out_path),
            "columns": EXTENDED_FIELDS,
            "rows": len(rows),
            "matched_rows": matched_rows,
            "coasting_rows": len(rows) - matched_rows,
            "track_ids": len({row["track_id"] for row in rows}),
            "column_semantics": {
                "matched": "1 if track.detections[-1].frame_number == frame_number (kit age == 1), else coasting",
                "detection_count": "len(track.detections) after this frame's update",
                "missed_frame_count": "consecutive unmatched frames up to and including this one (kit age - 1)",
                "age_frames": "frame_number - first detection frame + 1",
                "confidence_policy": "kit detections carry no confidence; matched rows are observations with confidence 1.0",
            },
        },
        "baseline_check": baseline_check,
        "environment": {
            "python": platform.python_version(),
            "numpy": numpy.__version__,
            "platform": platform.platform(),
        },
        "elapsed_seconds": round(elapsed, 1),
        "reused": False,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--video", type=Path, required=True)
    parser.add_argument("--detections", type=Path, required=True)
    parser.add_argument("--detection-source", default="real", help="label: real, gt, gt-degraded, ...")
    parser.add_argument("--out", type=Path, required=True, help="track CSV to write (manifest goes next to it)")
    parser.add_argument("--label", default=None)
    parser.add_argument("--euclidean-matching-threshold", type=float, default=DEFAULT_PARAMS["euclidean_matching_threshold"])
    parser.add_argument("--max-age", type=int, default=DEFAULT_PARAMS["max_age"])
    parser.add_argument("--tentative-threshold", type=int, default=DEFAULT_PARAMS["tentative_threshold"])
    parser.add_argument("--check-baseline", type=Path, default=None, help="6-column CSV the output must reproduce")
    parser.add_argument("--force", action="store_true", help="re-run even if a matching manifest exists")
    parser.add_argument("--allow-partial-coverage", action="store_true", help="accept a CSV whose frames lie inside the video without touching frame 0 or the last frame")
    args = parser.parse_args()

    details = {}
    candidate_manifest = args.detections.with_suffix(args.detections.suffix + ".manifest.json")
    if candidate_manifest.exists():
        details = json.loads(candidate_manifest.read_text())

    manifest = run_experiment(
        video_path=args.video,
        detections_path=args.detections,
        out_path=args.out,
        params={
            "euclidean_matching_threshold": args.euclidean_matching_threshold,
            "max_age": args.max_age,
            "tentative_threshold": args.tentative_threshold,
        },
        detection_source=args.detection_source,
        detection_source_details=details,
        label=args.label,
        check_baseline=args.check_baseline,
        force=args.force,
        allow_partial_coverage=args.allow_partial_coverage,
    )
    output = manifest["output"]
    print(f"{'reused' if manifest['reused'] else 'wrote'} {output['path']}: {output['rows']} rows, "
          f"{output['matched_rows']} matched, {output['coasting_rows']} coasting, {output['track_ids']} track ids "
          f"({manifest['elapsed_seconds']} s)")
    check = manifest.get("baseline_check")
    if check is not None:
        print(f"baseline check against {check['path']}: identical bytes = {check['identical_bytes']} "
              f"(rows {check['rows_ours']} vs {check['rows_baseline']})")
        if not check["identical_bytes"]:
            raise SystemExit(2)


if __name__ == "__main__":
    main()
