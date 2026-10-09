"""JSONL result store with content-addressed run ids and repo-style references.

The evaluator depends on the ``ResultStore`` protocol only. ``JsonlResultStore`` writes one
``<run_id>.jsonl`` per run under ``root`` and keeps a ``refs.json`` index mapping references such
as ``"flock|20251012_164031_1DAC|gt"`` to run ids. ``resolve`` accepts either a run id or a
reference. The file format is an implementation detail behind the port.

``content_run_id`` hashes provenance plus output with no clock and no randomness, so a
byte-identical run yields the same id and "did anything change?" is a string comparison.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Optional, Protocol

from evaluation.contracts import (
    Detection,
    FrameDetections,
    Provenance,
    RunResult,
    StageStat,
    StageTiming,
    Track,
    TrackUpdate,
)

REFS_FILENAME = "refs.json"


class ResultStore(Protocol):
    """Persist a run and resolve one back by id or reference. Ids are opaque to callers."""

    def persist(self, result: RunResult, ref: Optional[str] = None) -> str: ...

    def resolve(self, run_id_or_ref: str) -> RunResult: ...


def content_run_id(result: RunResult) -> str:
    """Deterministic id from provenance plus full output content (observations and updates)."""
    provenance = result.provenance
    payload = {
        "config_hash": provenance.config_hash,
        "git_commit": provenance.git_commit,
        "model_hash": provenance.model_hash,
        "extra": provenance.extra,
        "correctness": [
            [frame, list(detection.box_xywh), detection.confidence, detection.track_id, detection.class_name]
            for frame in sorted(result.correctness)
            for detection in result.correctness[frame]
        ],
        "performance": sorted((stage, stat.calls, stat.total_seconds) for stage, stat in result.performance.items()),
        "tracks": [
            [track.track_id, [_update_to_json(update) for update in track.updates]]
            for track in sorted(result.tracks, key=lambda track: (track.first_frame, track.track_id))
        ],
    }
    encoded = json.dumps(payload, sort_keys=True, default=str).encode()
    return hashlib.sha256(encoded).hexdigest()[:16]


def write_run_result_jsonl(path: Path | str, result: RunResult) -> None:
    """Serialize a RunResult: a provenance line, a performance line, one line per detection,
    one line per track."""
    with Path(path).open("w") as handle:
        handle.write(json.dumps({"kind": "provenance", **_provenance_to_json(result.provenance)}) + "\n")
        handle.write(json.dumps({"kind": "performance", "stages": _performance_to_json(result.performance)}) + "\n")
        for frame_number in sorted(result.correctness):
            for detection in result.correctness[frame_number]:
                handle.write(json.dumps({"kind": "detection", "frame": frame_number, **_detection_to_json(detection)}) + "\n")
        for track in result.tracks:
            handle.write(json.dumps({"kind": "track", **_track_to_json(track)}) + "\n")


def read_run_result_jsonl(path: Path | str) -> RunResult:
    """Rebuild a RunResult from a file written by ``write_run_result_jsonl``."""
    provenance: Optional[Provenance] = None
    performance: StageTiming = {}
    correctness: FrameDetections = {}
    tracks: list[Track] = []
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        kind = record["kind"]
        if kind == "provenance":
            provenance = _provenance_from_json(record)
        elif kind == "performance":
            performance = {
                stage: StageStat(calls=value["calls"], total_seconds=value["total_seconds"])
                for stage, value in record["stages"].items()
            }
        elif kind == "detection":
            correctness.setdefault(record["frame"], []).append(_detection_from_json(record))
        elif kind == "track":
            tracks.append(_track_from_json(record))
        else:
            raise ValueError(f"Unknown record kind {kind!r} in {path}")
    if provenance is None:
        raise ValueError(f"No provenance line in {path}")
    return RunResult(correctness=correctness, performance=performance, provenance=provenance, tracks=tuple(tracks))


class JsonlResultStore:
    """Persist/resolve runs as JSONL files under ``root``, with a reference index."""

    def __init__(self, root: Path | str):
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)

    @property
    def root(self) -> Path:
        return self._root

    def persist(self, result: RunResult, ref: Optional[str] = None) -> str:
        """Write the run under its content id; optionally bind ``ref`` to that id (overwriting)."""
        run_id = content_run_id(result)
        write_run_result_jsonl(self._root / f"{run_id}.jsonl", result)
        if ref is not None:
            self.bind(ref, run_id)
        return run_id

    def resolve(self, run_id_or_ref: str) -> RunResult:
        run_id = self.refs().get(run_id_or_ref, run_id_or_ref)
        path = self._root / f"{run_id}.jsonl"
        if not path.exists():
            raise KeyError(f"No run {run_id_or_ref!r} in {self._root}")
        return read_run_result_jsonl(path)

    def bind(self, ref: str, run_id: str) -> None:
        refs = self.refs()
        refs[ref] = run_id
        (self._root / REFS_FILENAME).write_text(json.dumps(refs, indent=2, sort_keys=True) + "\n")

    def refs(self) -> dict[str, str]:
        path = self._root / REFS_FILENAME
        return json.loads(path.read_text()) if path.exists() else {}

    def run_ids(self) -> list[str]:
        return sorted(path.stem for path in self._root.glob("*.jsonl"))


def _provenance_to_json(provenance: Provenance) -> dict:
    return {
        "config_hash": provenance.config_hash,
        "git_commit": provenance.git_commit,
        "model_hash": provenance.model_hash,
        "extra": provenance.extra,
    }


def _provenance_from_json(record: dict) -> Provenance:
    return Provenance(
        config_hash=record["config_hash"],
        git_commit=record["git_commit"],
        model_hash=record["model_hash"],
        extra=record.get("extra", {}),
    )


def _performance_to_json(performance: StageTiming) -> dict:
    return {stage: {"calls": stat.calls, "total_seconds": stat.total_seconds} for stage, stat in performance.items()}


def _detection_to_json(detection: Detection) -> dict:
    return {
        "box": list(detection.box_xywh),
        "confidence": detection.confidence,
        "track_id": detection.track_id,
        "class_name": detection.class_name,
    }


def _detection_from_json(record: dict) -> Detection:
    box = record["box"]
    return Detection(
        box_xywh=(box[0], box[1], box[2], box[3]),
        confidence=record["confidence"],
        track_id=record.get("track_id"),
        class_name=record.get("class_name"),
    )


def _update_to_json(update: TrackUpdate) -> list:
    return [
        update.frame_number,
        update.position_xy[0],
        update.position_xy[1],
        update.confidence,
        update.detection_count,
        update.missed_frame_count,
        update.age_frames,
        list(update.box_xywh) if update.box_xywh is not None else None,
    ]


def _update_from_json(row: list) -> TrackUpdate:
    box = row[7] if len(row) > 7 else None
    return TrackUpdate(
        frame_number=row[0],
        position_xy=(row[1], row[2]),
        confidence=row[3],
        detection_count=row[4],
        missed_frame_count=row[5],
        age_frames=row[6],
        box_xywh=tuple(box) if box is not None else None,
    )


def _track_to_json(track: Track) -> dict:
    return {"track_id": track.track_id, "updates": [_update_to_json(update) for update in track.updates]}


def _track_from_json(record: dict) -> Track:
    return Track(track_id=record["track_id"], updates=tuple(_update_from_json(row) for row in record["updates"]))
