"""Shared translation of an ``obj_id`` + ``x1,y1,x2,y2`` tracks CSV into contracts.

Both the hand-labelled ground truth (``*_reference_tracks_corrected.csv``) and the cloud
tracker's export (``*_cloud_reference_tracks.csv``) use this schema:
``frame_number, obj_id, x1, y1, x2, y2, bbox_size[, frame_timestamp]``, with ``(x1, y1)`` the
top-left and ``(x2, y2)`` the bottom-right corner in pixels. Every row is an observation
(confidence 1.0, ``obj_id`` as the track id, class ``bird``) and a track update positioned at
the box center. Neither source has a coasting notion, so ``missed_frame_count`` is always 0 and
``detection_count`` is the running count of the identity's rows.
"""

from __future__ import annotations

from pathlib import Path

from evaluation.adapters._csv import as_int, read_rows
from evaluation.contracts import Detection, FrameDetections, Track, TrackUpdate, box_center, reconstruct_tracks

REQUIRED_COLUMNS = ("frame_number", "obj_id", "x1", "y1", "x2", "y2")


def load_xyxy_tracks(
    path: Path | str, class_name: str = "bird", confidence: float = 1.0
) -> tuple[FrameDetections, tuple[Track, ...], dict]:
    """Parse the CSV into ``(correctness, tracks, facts)``.

    ``facts`` carries the counts a provenance should record: rows, frames, identities, frame
    range, and the number of ``(frame, obj_id)`` duplicates (refused, since one identity cannot
    be in two places in one frame) and of identical boxes shared by two identities in one
    frame (kept and counted: the flock GT has one at frame 517).
    """
    rows = read_rows(path, REQUIRED_COLUMNS)
    correctness: FrameDetections = {}
    updates: list[tuple[str, TrackUpdate]] = []
    seen_rows: dict[str, int] = {}
    first_frame: dict[str, int] = {}
    seen_pairs: set[tuple[int, str]] = set()
    boxes_in_frame: dict[int, dict[tuple, list[str]]] = {}

    for row in sorted(rows, key=lambda r: (as_int(r["frame_number"], "frame_number"), r["obj_id"])):
        frame = as_int(row["frame_number"], "frame_number")
        track_id = str(as_int(row["obj_id"], "obj_id"))
        x1, y1, x2, y2 = (float(row[key]) for key in ("x1", "y1", "x2", "y2"))
        if x2 <= x1 or y2 <= y1:
            raise ValueError(f"{path}: degenerate box at frame {frame}, obj_id {track_id}: {(x1, y1, x2, y2)}")
        if (frame, track_id) in seen_pairs:
            raise ValueError(f"{path}: obj_id {track_id} appears twice in frame {frame}")
        seen_pairs.add((frame, track_id))
        box = (x1, y1, x2 - x1, y2 - y1)
        boxes_in_frame.setdefault(frame, {}).setdefault(box, []).append(track_id)

        correctness.setdefault(frame, []).append(
            Detection(box_xywh=box, confidence=confidence, track_id=track_id, class_name=class_name)
        )
        seen_rows[track_id] = seen_rows.get(track_id, 0) + 1
        first_frame.setdefault(track_id, frame)
        updates.append(
            (
                track_id,
                TrackUpdate(
                    frame_number=frame,
                    position_xy=box_center(box),
                    confidence=confidence,
                    detection_count=seen_rows[track_id],
                    missed_frame_count=0,
                    age_frames=frame - first_frame[track_id] + 1,
                    box_xywh=box,
                ),
            )
        )

    shared_boxes = [
        {"frame": frame, "box": list(box), "obj_ids": ids}
        for frame, boxes in sorted(boxes_in_frame.items())
        for box, ids in boxes.items()
        if len(ids) > 1
    ]
    frames = sorted(correctness)
    facts = {
        "rows": len(rows),
        "frames_with_boxes": len(frames),
        "frame_range": [frames[0], frames[-1]] if frames else None,
        "identities": len(seen_rows),
        "identical_box_shared_by_two_identities": shared_boxes,
    }
    return correctness, reconstruct_tracks(updates), facts
