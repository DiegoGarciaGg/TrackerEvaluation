"""Adapter: hand-labelled ground truth CSV -> ``RunResult`` (claim: accuracy).

Mirrors the repo's ``gt_adapter.py``: confidence 1.0, the bird's id as ``track_id`` (text),
class ``bird``, and a ``TrackUpdate`` positioned at the box center. Its provenance states that
the labels are an independent manual annotation (not traced from the cloud output, unlike the
repo's current ground truth), the sha256 of each GT CSV and of the clip, and for the flock
that the clip is frames 4001..5009 of the original recording.

Input: ``<video_id>_reference_tracks_corrected.csv`` (``frame_number, obj_id, x1, y1, x2, y2,
bbox_size``). The companion ``<video_id>_detections_corrected.csv`` holds the same boxes without
ids in the detector's schema; when given, it is hashed into the provenance and checked to be
the same boxes row for row.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from evaluation.adapters._csv import read_rows
from evaluation.adapters.xyxy_tracks import load_xyxy_tracks
from evaluation.contracts import RunResult
from evaluation.provenance import build_provenance, hashed_inputs

CURATION = "independent manual annotation (not traced from the cloud tracker output)"


def load_gt_run(
    tracks_csv: Path | str,
    video_id: str,
    video_path: Optional[Path | str] = None,
    detections_csv: Optional[Path | str] = None,
    dataset: Optional[str] = None,
    notes: Optional[list[str]] = None,
) -> RunResult:
    correctness, tracks, facts = load_xyxy_tracks(tracks_csv, class_name="bird", confidence=1.0)
    extra_notes = [
        "confidence 1.0 on every box: labels carry no score",
        "track_id is the annotator's obj_id as text",
    ]
    if detections_csv is not None:
        mismatches = _compare_with_detections_csv(tracks_csv, detections_csv)
        extra_notes.append(
            f"companion detections CSV holds the same boxes without ids ({mismatches} row mismatches)"
        )
        if mismatches:
            raise ValueError(f"{detections_csv} differs from {tracks_csv} in {mismatches} rows")
    provenance = build_provenance(
        predictor="gt",
        claim="accuracy",
        video_id=video_id,
        dataset=dataset,
        config={},
        model_hash="gt",
        inputs=hashed_inputs(gt_tracks_csv=tracks_csv, gt_detections_csv=detections_csv, video=video_path),
        notes=extra_notes + list(notes or []),
        curation=CURATION,
        facts=facts,
    )
    return RunResult(correctness=correctness, performance={}, provenance=provenance, tracks=tracks)


def _compare_with_detections_csv(tracks_csv: Path | str, detections_csv: Path | str) -> int:
    """Rows where the detections CSV box differs from the tracks CSV box (same order)."""
    tracks = read_rows(tracks_csv, ("frame_number", "x1", "y1", "x2", "y2"))
    detections = read_rows(detections_csv, ("frame_number", "x", "y", "w", "h"))
    if len(tracks) != len(detections):
        return abs(len(tracks) - len(detections)) + min(len(tracks), len(detections))
    mismatches = 0
    for track_row, detection_row in zip(tracks, detections):
        same = (
            int(float(track_row["frame_number"])) == int(float(detection_row["frame_number"]))
            and float(track_row["x1"]) == float(detection_row["x"])
            and float(track_row["y1"]) == float(detection_row["y"])
            and float(track_row["x2"]) - float(track_row["x1"]) == float(detection_row["w"])
            and float(track_row["y2"]) - float(track_row["y1"]) == float(detection_row["h"])
        )
        mismatches += 0 if same else 1
    return mismatches
