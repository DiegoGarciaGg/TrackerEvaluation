"""Adapters for the two labelled-tracks CSVs: hand-made ground truth and the cloud export.

Both share the schema ``frame_number, obj_id, x1, y1, x2, y2, bbox_size[, frame_timestamp]``
with ``(x1, y1)`` the top-left and ``(x2, y2)`` the bottom-right corner in pixels. Every row
becomes an observation (confidence 1.0, ``obj_id`` as text id, class ``bird``) and a track
update at the box center. Neither has a coasting notion, so ``missed_frame_count`` is 0 and
``detection_count`` is the running count of the identity's rows.

- ``load_gt_run``: claim **accuracy**. Mirrors the repo's ``gt_adapter.py``. Provenance says the
  labels are an independent manual annotation, hashes both GT CSVs and the clip, and for the
  flock notes that the clip is frames 4001..5009 of the original.
- ``load_cloud_run``: claim **parity**. The cloud tracker's output for the same window: a
  comparison against it says whether the kit agrees with the heavier pipeline, not who is right.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from evaluation.adapters._csv import as_int, read_rows
from evaluation.contracts import Detection, FrameDetections, RunResult, Track, TrackUpdate, box_center, reconstruct_tracks
from evaluation.provenance import build_provenance, hashed_inputs

REQUIRED_COLUMNS = ("frame_number", "obj_id", "x1", "y1", "x2", "y2")
GT_CURATION = "independent manual annotation (not traced from the cloud tracker output)"


def load_xyxy_tracks(path: Path | str) -> tuple[FrameDetections, tuple[Track, ...], dict]:
    """Parse the CSV into ``(correctness, tracks, facts)``.

    ``facts`` records rows, frames, identities, frame range and the identical boxes shared by
    two identities in one frame (kept and counted: the flock GT has one at frame 517). An
    identity appearing twice in one frame or a degenerate box is refused.
    """
    rows = read_rows(path, REQUIRED_COLUMNS)
    correctness: FrameDetections = {}
    updates: list[tuple[str, TrackUpdate]] = []
    rows_per_id: dict[str, int] = {}
    first_frame: dict[str, int] = {}
    seen: set[tuple[int, str]] = set()
    boxes_in_frame: dict[int, dict[tuple, list[str]]] = {}

    for row in sorted(rows, key=lambda r: (as_int(r["frame_number"], "frame_number"), r["obj_id"])):
        frame = as_int(row["frame_number"], "frame_number")
        track_id = str(as_int(row["obj_id"], "obj_id"))
        x1, y1, x2, y2 = (float(row[key]) for key in ("x1", "y1", "x2", "y2"))
        if x2 <= x1 or y2 <= y1:
            raise ValueError(f"{path}: degenerate box at frame {frame}, obj_id {track_id}: {(x1, y1, x2, y2)}")
        if (frame, track_id) in seen:
            raise ValueError(f"{path}: obj_id {track_id} appears twice in frame {frame}")
        seen.add((frame, track_id))
        box = (x1, y1, x2 - x1, y2 - y1)
        boxes_in_frame.setdefault(frame, {}).setdefault(box, []).append(track_id)
        correctness.setdefault(frame, []).append(Detection(box_xywh=box, confidence=1.0, track_id=track_id, class_name="bird"))
        rows_per_id[track_id] = rows_per_id.get(track_id, 0) + 1
        first_frame.setdefault(track_id, frame)
        updates.append(
            (
                track_id,
                TrackUpdate(
                    frame_number=frame,
                    position_xy=box_center(box),
                    confidence=1.0,
                    detection_count=rows_per_id[track_id],
                    missed_frame_count=0,
                    age_frames=frame - first_frame[track_id] + 1,
                    box_xywh=box,
                ),
            )
        )

    frames = sorted(correctness)
    facts = {
        "rows": len(rows),
        "frames_with_boxes": len(frames),
        "frame_range": [frames[0], frames[-1]] if frames else None,
        "identities": len(rows_per_id),
        "identical_box_shared_by_two_identities": [
            {"frame": frame, "box": list(box), "obj_ids": ids}
            for frame, boxes in sorted(boxes_in_frame.items())
            for box, ids in boxes.items()
            if len(ids) > 1
        ],
    }
    return correctness, reconstruct_tracks(updates), facts


def load_gt_run(
    tracks_csv: Path | str,
    video_id: str,
    video_path: Optional[Path | str] = None,
    detections_csv: Optional[Path | str] = None,
    dataset: Optional[str] = None,
) -> RunResult:
    """Ground truth. ``detections_csv`` (same boxes without ids, detector schema) is hashed and
    checked row for row when given."""
    correctness, tracks, facts = load_xyxy_tracks(tracks_csv)
    notes = ["confidence 1.0 on every box: labels carry no score", "track_id is the annotator's obj_id as text"]
    if detections_csv is not None:
        mismatches = _mismatches_with_detections_csv(tracks_csv, detections_csv)
        if mismatches:
            raise ValueError(f"{detections_csv} differs from {tracks_csv} in {mismatches} rows")
        notes.append("companion detections CSV holds the same boxes without ids (checked row for row)")
    provenance = build_provenance(
        predictor="gt",
        claim="accuracy",
        video_id=video_id,
        dataset=dataset,
        model_hash="gt",
        inputs=hashed_inputs(gt_tracks_csv=tracks_csv, gt_detections_csv=detections_csv, video=video_path),
        notes=notes,
        curation=GT_CURATION,
        facts=facts,
    )
    return RunResult(correctness=correctness, performance={}, provenance=provenance, tracks=tracks)


def load_cloud_run(tracks_csv: Path | str, video_id: str, video_path: Optional[Path | str] = None, dataset: Optional[str] = None) -> RunResult:
    """Cloud export: a parity reference, not truth."""
    correctness, tracks, facts = load_xyxy_tracks(tracks_csv)
    provenance = build_provenance(
        predictor="cloud",
        claim="parity",
        video_id=video_id,
        dataset=dataset,
        model_hash="cloud-tracker-export",
        inputs=hashed_inputs(cloud_tracks_csv=tracks_csv, video=video_path),
        notes=["stored output of the cloud tracking pipeline for the same frame window; a reference for parity only",
               "confidence 1.0 on every row: the export carries no score"],
        facts=facts,
    )
    return RunResult(correctness=correctness, performance={}, provenance=provenance, tracks=tracks)


def _mismatches_with_detections_csv(tracks_csv: Path | str, detections_csv: Path | str) -> int:
    tracks = read_rows(tracks_csv, ("frame_number", "x1", "y1", "x2", "y2"))
    detections = read_rows(detections_csv, ("frame_number", "x", "y", "w", "h"))
    if len(tracks) != len(detections):
        return abs(len(tracks) - len(detections)) + min(len(tracks), len(detections))
    mismatches = 0
    for t, d in zip(tracks, detections):
        same = (
            int(float(t["frame_number"])) == int(float(d["frame_number"]))
            and float(t["x1"]) == float(d["x"]) and float(t["y1"]) == float(d["y"])
            and float(t["x2"]) - float(t["x1"]) == float(d["w"]) and float(t["y2"]) - float(t["y1"]) == float(d["h"])
        )
        mismatches += 0 if same else 1
    return mismatches
