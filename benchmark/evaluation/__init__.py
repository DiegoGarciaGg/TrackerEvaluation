"""Tracker evaluation: contracts, adapters, store, metrics and diagnostics.

Reads finished CSV outputs plus a reference and reports. Never runs the tracker, never opens a
video. Depends on the standard library, numpy and scipy only (TrackEval for the MOT metrics).
Designed to be portable to the repo's ``edge/evaluation`` built on ``spoorpredictioneval``:
the contracts keep that library's names and meaning.
"""

from evaluation.contracts import (
    Box,
    Detection,
    FrameDetections,
    Provenance,
    RunResult,
    StageStat,
    StageTiming,
    Track,
    TrackUpdate,
    box_center,
    reconstruct_tracks,
)
from evaluation.store import JsonlResultStore, ResultStore, content_run_id

__all__ = [
    "Box",
    "Detection",
    "FrameDetections",
    "Provenance",
    "RunResult",
    "StageStat",
    "StageTiming",
    "Track",
    "TrackUpdate",
    "box_center",
    "reconstruct_tracks",
    "JsonlResultStore",
    "ResultStore",
    "content_run_id",
]
