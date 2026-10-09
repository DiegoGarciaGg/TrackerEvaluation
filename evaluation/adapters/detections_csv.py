"""Adapter: detector CSV (birdwatcher schema) -> ``RunResult`` with observations only.

``frame_number, frame_timestamp, x, y, w, h, area, classifier_name``; ``(x, y)`` top-left. No
confidence column exists, so every observation gets confidence 1.0 and the provenance says so.
No ``track_id`` (a detector has no identities) and no tracks. The same adapter reads the
ground-truth detections CSV (``classifier_name == "corrected"``) and any degraded detections
written by ``experiments/``, which must keep this schema.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Optional

from evaluation.adapters._csv import as_int, read_rows
from evaluation.contracts import Detection, FrameDetections, RunResult
from evaluation.provenance import build_provenance, hashed_inputs

REQUIRED_COLUMNS = ("frame_number", "x", "y", "w", "h")


def load_detections(path: Path | str, class_name: str = "bird") -> tuple[FrameDetections, dict]:
    rows = read_rows(path, REQUIRED_COLUMNS)
    correctness: FrameDetections = {}
    classifiers: Counter = Counter()
    for row in rows:
        frame = as_int(row["frame_number"], "frame_number")
        box = (float(row["x"]), float(row["y"]), float(row["w"]), float(row["h"]))
        if box[2] <= 0 or box[3] <= 0:
            raise ValueError(f"{path}: degenerate box at frame {frame}: {box}")
        correctness.setdefault(frame, []).append(
            Detection(box_xywh=box, confidence=1.0, track_id=None, class_name=class_name)
        )
        classifiers[row.get("classifier_name", "")] += 1
    frames = sorted(correctness)
    facts = {
        "rows": len(rows),
        "frames_with_boxes": len(frames),
        "frame_range": [frames[0], frames[-1]] if frames else None,
        "classifier_name": dict(classifiers),
    }
    return {frame: correctness[frame] for frame in frames}, facts


def load_detections_run(
    path: Path | str,
    video_id: str,
    video_path: Optional[Path | str] = None,
    dataset: Optional[str] = None,
    predictor: str = "detector",
    notes: Optional[list[str]] = None,
) -> RunResult:
    correctness, facts = load_detections(path)
    provenance = build_provenance(
        predictor=predictor,
        claim="detections",
        video_id=video_id,
        dataset=dataset,
        config={},
        model_hash=facts and ",".join(sorted(facts["classifier_name"])) or "none",
        inputs=hashed_inputs(detections_csv=path, video=video_path),
        notes=["no confidence column in the detector schema: confidence set to 1.0 on every box"]
        + list(notes or []),
        facts=facts,
    )
    return RunResult(correctness=correctness, performance={}, provenance=provenance, tracks=())
