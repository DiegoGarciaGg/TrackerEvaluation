"""Adapter: cloud tracker export CSV -> ``RunResult`` (claim: parity, NOT ground truth).

``<video_id>_cloud_reference_tracks.csv`` has ``frame_number, obj_id, x1, y1, x2, y2,
bbox_size, frame_timestamp``. Same translation as the ground truth (every row is an
observation and an update, confidence 1.0, ``obj_id`` as text id) but the provenance names the
producer ``cloud`` and the claim ``parity``: a comparison against it says whether the kit
agrees with the heavier cloud pipeline, not whether either is right.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from evaluation.adapters.xyxy_tracks import load_xyxy_tracks
from evaluation.contracts import RunResult
from evaluation.provenance import build_provenance, hashed_inputs


def load_cloud_run(
    tracks_csv: Path | str,
    video_id: str,
    video_path: Optional[Path | str] = None,
    dataset: Optional[str] = None,
    notes: Optional[list[str]] = None,
) -> RunResult:
    correctness, tracks, facts = load_xyxy_tracks(tracks_csv, class_name="bird", confidence=1.0)
    provenance = build_provenance(
        predictor="cloud",
        claim="parity",
        video_id=video_id,
        dataset=dataset,
        config={},
        model_hash="cloud-tracker-export",
        inputs=hashed_inputs(cloud_tracks_csv=tracks_csv, video=video_path),
        notes=[
            "stored output of the cloud tracking pipeline for the same frame window; a reference for parity only",
            "confidence 1.0 on every row: the export carries no score",
        ]
        + list(notes or []),
        facts=facts,
    )
    return RunResult(correctness=correctness, performance={}, provenance=provenance, tracks=tracks)
