"""Adapter: the kit tracker's CSV -> ``RunResult`` following the repo's finished-surface rule.

Two formats are accepted:

- **baseline (6 columns)** ``frame_number, track_id, x, y, w, h``, as ``run_tracker.py`` writes
  it. For every CONFIRMED track in every frame the row carries the box of the track's LAST
  matched detection, also on frames where the track was not matched (coasting). Nothing in the
  file tells the two apart. The adapter therefore turns EVERY row into an observation and an
  update, and records ``coasting_known = False`` in the provenance. A matched-rows-only
  evaluation of such a file is refused by the evaluator (it checks ``coasting_known``).
- **extended (10 columns)** the same six plus ``matched, detection_count, missed_frame_count,
  age_frames`` as ``experiments/run_experiment.py`` writes them. Repo convention
  (``adapter.py``, ``_finished_surface``): a matched row becomes a ``Detection`` (with
  ``track_id``) AND a ``TrackUpdate`` with confidence 1.0; a coasting row becomes ONLY a
  ``TrackUpdate`` with confidence 0.0 and its ``missed_frame_count``. The kit's detections carry
  no confidence, so matched observations get 1.0 and the provenance notes it.

Column meanings in the extended format (set by the experiment runner, verified against the
tracker source in Phase 0): ``matched`` is 1 when ``track.detections[-1].frame_number`` equals
the row's frame (equivalently the kit's ``age == 1`` after ``match_and_track``);
``detection_count`` is ``len(track.detections)``; ``missed_frame_count`` is the kit's
``age - 1``; ``age_frames`` is frames since the track's first detection, inclusive.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from evaluation.adapters._csv import as_int, header_of, read_rows
from evaluation.contracts import (
    Detection,
    FrameDetections,
    RunResult,
    Track,
    TrackUpdate,
    box_center,
    reconstruct_tracks,
)
from evaluation.provenance import build_provenance, hashed_inputs

BASELINE_COLUMNS = ("frame_number", "track_id", "x", "y", "w", "h")
EXTENDED_COLUMNS = BASELINE_COLUMNS + ("matched", "detection_count", "missed_frame_count", "age_frames")

FORMAT_BASELINE = "baseline-6col"
FORMAT_EXTENDED = "extended-10col"


def detect_format(path: Path | str) -> str:
    header = header_of(path)
    if all(column in header for column in EXTENDED_COLUMNS):
        return FORMAT_EXTENDED
    if all(column in header for column in BASELINE_COLUMNS):
        return FORMAT_BASELINE
    raise ValueError(f"{path}: header {list(header)} is neither the 6-column nor the 10-column tracker format")


def load_tracker_csv(path: Path | str) -> tuple[FrameDetections, tuple[Track, ...], dict]:
    """Parse either format into ``(correctness, tracks, facts)``.

    ``facts["coasting_known"]`` says whether coasting rows were distinguishable. In the baseline
    format ``detection_count`` is the running count of the track's written rows and
    ``age_frames`` counts from the first WRITTEN row, both approximations that the facts flag.
    """
    fmt = detect_format(path)
    rows = read_rows(path, EXTENDED_COLUMNS if fmt == FORMAT_EXTENDED else BASELINE_COLUMNS)
    correctness: FrameDetections = {}
    updates: list[tuple[str, TrackUpdate]] = []
    written_rows: dict[str, int] = {}
    first_frame: dict[str, int] = {}
    matched_rows = coasting_rows = 0

    for row in sorted(rows, key=lambda r: (as_int(r["frame_number"], "frame_number"), as_int(r["track_id"], "track_id"))):
        frame = as_int(row["frame_number"], "frame_number")
        track_id = str(as_int(row["track_id"], "track_id"))
        box = (float(row["x"]), float(row["y"]), float(row["w"]), float(row["h"]))
        if box[2] <= 0 or box[3] <= 0:
            raise ValueError(f"{path}: degenerate box at frame {frame}, track {track_id}: {box}")
        written_rows[track_id] = written_rows.get(track_id, 0) + 1
        first_frame.setdefault(track_id, frame)

        if fmt == FORMAT_EXTENDED:
            matched = as_int(row["matched"], "matched") == 1
            detection_count = as_int(row["detection_count"], "detection_count")
            missed = as_int(row["missed_frame_count"], "missed_frame_count")
            age_frames = as_int(row["age_frames"], "age_frames")
            if matched and missed != 0:
                raise ValueError(f"{path}: matched row with missed_frame_count {missed} at frame {frame}, track {track_id}")
            if not matched and missed == 0:
                raise ValueError(f"{path}: coasting row with missed_frame_count 0 at frame {frame}, track {track_id}")
        else:
            matched = True
            detection_count = written_rows[track_id]
            missed = 0
            age_frames = frame - first_frame[track_id] + 1

        if matched:
            matched_rows += 1
            correctness.setdefault(frame, []).append(
                Detection(box_xywh=box, confidence=1.0, track_id=track_id, class_name="bird")
            )
        else:
            coasting_rows += 1
        updates.append(
            (
                track_id,
                TrackUpdate(
                    frame_number=frame,
                    position_xy=box_center(box),
                    confidence=1.0 if matched else 0.0,
                    detection_count=detection_count,
                    missed_frame_count=missed,
                    age_frames=age_frames,
                    box_xywh=box,
                ),
            )
        )

    frames = sorted(correctness)
    facts = {
        "format": fmt,
        "coasting_known": fmt == FORMAT_EXTENDED,
        "rows": len(rows),
        "matched_rows": matched_rows if fmt == FORMAT_EXTENDED else None,
        "coasting_rows": coasting_rows if fmt == FORMAT_EXTENDED else None,
        "observations": matched_rows,
        "track_ids": len(written_rows),
        "frame_range": [frames[0], frames[-1]] if frames else None,
        "approximations": (
            []
            if fmt == FORMAT_EXTENDED
            else [
                "every row treated as matched (coasting rows are indistinguishable in the 6-column format)",
                "detection_count = running count of written rows (the kit's first two detections are never written)",
                "age_frames counted from the first written row",
            ]
        ),
    }
    return correctness, reconstruct_tracks(updates), facts


def load_tracker_run(
    path: Path | str,
    video_id: str,
    *,
    predictor: str = "kit",
    claim: str = "regression",
    tracker_params: Optional[dict] = None,
    detections_csv: Optional[Path | str] = None,
    detection_source: Optional[str] = None,
    tracker_source_hash: Optional[str] = None,
    video_path: Optional[Path | str] = None,
    dataset: Optional[str] = None,
    notes: Optional[list[str]] = None,
    **extra_fields,
) -> RunResult:
    """Build the ``RunResult`` for a tracker CSV with full provenance.

    ``claim`` is what a comparison AGAINST this run asserts; for a frozen baseline that is
    ``regression``. ``tracker_params``, ``detections_csv`` (hashed), ``detection_source`` (a
    label: ``real``, ``gt``, ``gt-degraded:...``) and ``tracker_source_hash`` (``sha256_tree`` of
    ``tracker/``) are the provenance the run manifest must carry; they are optional here so a
    bare CSV of unknown origin can still be loaded, with the gaps visible in the provenance.
    """
    correctness, tracks, facts = load_tracker_csv(path)
    config = dict(tracker_params or {})
    inputs = hashed_inputs(tracker_csv=path, detections_csv=detections_csv, video=video_path)
    provenance = build_provenance(
        predictor=predictor,
        claim=claim,
        video_id=video_id,
        dataset=dataset,
        config=config,
        model_hash=inputs["detections_csv"]["sha256"] if "detections_csv" in inputs else "unknown",
        inputs=inputs,
        notes=[
            "matched rows carry confidence 1.0: the kit's detections have no confidence",
            "coasting rows are track updates only (confidence 0.0), never observations",
        ]
        + ([] if facts["coasting_known"] else ["6-column format: coasting rows unknown, every row counted as an observation"])
        + list(notes or []),
        coasting_known=facts["coasting_known"],
        detection_source=detection_source or "unknown",
        tracker_source_hash=tracker_source_hash or "unknown",
        facts=facts,
        **extra_fields,
    )
    return RunResult(correctness=correctness, performance={}, provenance=provenance, tracks=tracks)
