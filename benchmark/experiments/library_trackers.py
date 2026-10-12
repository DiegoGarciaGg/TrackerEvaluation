"""Adapter from our detections to Roboflow Trackers (SORT, ByteTrack, OC-SORT, BoT-SORT, C-BIoU).

Library: https://github.com/roboflow/trackers (Apache 2.0), pinned in ``requirements.txt``.
Every tracker takes a ``supervision.Detections`` per frame and returns detections with a
``tracker_id`` (``-1`` for unmatched or not yet confirmed). Only SORT returns them in input
order, so rows are built from the RETURNED boxes, which are the input boxes themselves (checked
on every frame). The libraries emit no coasting rows, so every row is a matched row:
``matched = 1``, ``missed_frame_count = 0``.

Inputs preserved: frame number and order, box coordinates and sizes. Our detections carry no
confidence, so none is passed; ByteTrack then uses a single IoU stage (its documented
fallback), SORT/BoT-SORT treat every detection as fully confident. BoT-SORT's camera motion
compensation is off (static camera; it would need every 4K frame). All other parameters are
the library defaults, captured into the manifest.
"""

from __future__ import annotations

import importlib.metadata
import inspect

import numpy as np

LIBRARY = "roboflow trackers"


def library_version() -> str:
    return importlib.metadata.version("trackers")


def make_tracker(algorithm: str, fps: float, params: dict | None = None):
    """Instantiate a library tracker; returns ``(tracker, effective_params)``."""
    import trackers

    classes = {
        "sort": trackers.SORTTracker,
        "bytetrack": trackers.ByteTrackTracker,
        "ocsort": trackers.OCSORTTracker,
        "botsort": trackers.BoTSORTTracker,
        "cbiou": trackers.CBIoUTracker,
    }
    if algorithm not in classes:
        raise ValueError(f"unknown library tracker {algorithm!r}; choose from {sorted(classes)}")
    kwargs = {"frame_rate": fps}
    if algorithm == "botsort":
        kwargs["enable_cmc"] = False
    kwargs.update(params or {})
    tracker = classes[algorithm](**kwargs)
    signature = inspect.signature(classes[algorithm].__init__)
    effective = {
        name: kwargs.get(name, parameter.default)
        for name, parameter in signature.parameters.items()
        if name != "self" and not inspect.isclass(parameter.default) and parameter.default is not inspect.Parameter.empty
    }
    effective.update({k: v for k, v in kwargs.items() if not inspect.isclass(v)})
    return tracker, effective


def library_track_rows(algorithm: str, detections_by_frame: dict, frame_count: int, fps: float, params: dict | None = None) -> tuple[list[dict], dict]:
    """Run a library tracker frame by frame; returns extended rows and the effective parameters."""
    import supervision as sv

    tracker, effective = make_tracker(algorithm, fps, params)
    rows: list[dict] = []
    detection_count: dict[int, int] = {}
    first_frame: dict[int, int] = {}
    for frame_number in range(frame_count):
        boxes = detections_by_frame.get(frame_number, [])
        xyxy = np.array([[b.x, b.y, b.x + b.width, b.y + b.height] for b in boxes], dtype=float).reshape(-1, 4)
        detections = sv.Detections(xyxy=xyxy) if len(xyxy) else sv.Detections.empty()
        out = tracker.update(detections)
        if len(out) == 0 or out.tracker_id is None:
            continue
        input_boxes = {tuple(b) for b in xyxy.tolist()}
        for box, track_id in zip(out.xyxy.tolist(), out.tracker_id.tolist()):
            if track_id == -1:
                continue
            if tuple(box) not in input_boxes:
                raise RuntimeError(f"{algorithm} returned a box that is not an input detection at frame {frame_number}: {box}")
            detection_count[track_id] = detection_count.get(track_id, 0) + 1
            first_frame.setdefault(track_id, frame_number)
            x1, y1, x2, y2 = box
            rows.append(
                {
                    "frame_number": frame_number,
                    "track_id": int(track_id),
                    "x": x1,
                    "y": y1,
                    "w": x2 - x1,
                    "h": y2 - y1,
                    "matched": 1,
                    "detection_count": detection_count[track_id],
                    "missed_frame_count": 0,
                    "age_frames": frame_number - first_frame[track_id] + 1,
                }
            )
    return rows, effective
