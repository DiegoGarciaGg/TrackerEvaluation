"""Canonical evaluation inputs, aligned name-for-name with ``spoorpredictioneval.contracts``.

The evaluator speaks only these types. Every producer (hand-labelled ground truth, the kit's
detector CSV, the kit tracker's CSV, the cloud tracker's CSV) is translated into them by one
adapter each (``evaluation.adapters``); nothing downstream knows which file a run came from.

Three terms are kept strictly distinct, exactly as in the repo:

- **observation** (``Detection``): one detection in one frame, a box plus confidence, tagged with
  the ``track_id`` it fed. A tracker row that was matched to a detection in that frame is an
  observation. A coasting row is NOT.
- **track update** (``TrackUpdate``): the tracker's per-frame emission of one track's state. A
  per-frame event, not a track. Both matched and coasting rows are track updates.
- **track** (``Track``): one distinct object hypothesis (one stable ``track_id``) as the projection
  over its ordered updates.

Field names and meanings of ``Detection``, ``TrackUpdate``, ``Track``, ``Provenance`` and
``RunResult`` are the repo's. Fields this kit adds on top (never renaming or re-meaning the
repo's) are marked ``# added`` and all have defaults, so a repo-shaped constructor call still
works unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

Box = tuple[float, float, float, float]
"""A bounding box as ``(x, y, width, height)`` in image pixels, ``(x, y)`` the top-left corner."""


def box_center(box: Box) -> tuple[float, float]:
    """Center ``(cx, cy)`` of an ``(x, y, w, h)`` box."""
    x, y, w, h = box
    return (x + w / 2.0, y + h / 2.0)


@dataclass(frozen=True)
class Detection:
    """One observation: a single detection in a single frame, tagged with the track it fed."""

    box_xywh: Box
    confidence: float
    track_id: Optional[str] = None
    class_name: Optional[str] = None


FrameDetections = dict[int, list[Detection]]
"""Correctness surface: frame number -> observations in that frame."""


@dataclass(frozen=True)
class TrackUpdate:
    """One track update: the tracker's state for one track at one frame.

    Repo semantics, mirrored for the kit tracker's CSV (see ``adapters/tracker_csv.py``):

    - ``confidence``: 1.0 on a matched row, 0.0 on a coasting row (the kit has no confidences).
    - ``detection_count``: detections the track has accumulated so far, including the ones it
      collected while still tentative (so the first written row of a kit track has 3).
    - ``missed_frame_count``: consecutive frames without a match up to and including this one
      (0 on a matched row; the kit's ``age - 1``).
    - ``age_frames``: frames since the track's first detection, inclusive (1 on its birth frame).

    ``box_xywh`` is an addition: the box the kit writes for this row (its last matched box, also
    on coasting rows), kept so an "all rows as written" evaluation can use the same box the
    annotated video shows. ``position_xy`` is the center of that box.
    """

    frame_number: int
    position_xy: tuple[float, float]
    confidence: float
    detection_count: int
    missed_frame_count: int
    age_frames: int
    box_xywh: Optional[Box] = None  # added

    @property
    def is_matched(self) -> bool:
        """Repo convention: a coasting update carries confidence 0.0 and a missed count > 0."""
        return self.missed_frame_count == 0


@dataclass(frozen=True)
class Track:
    """A distinct object hypothesis (one ``track_id``) as the projection over its ordered updates."""

    track_id: str
    updates: tuple[TrackUpdate, ...]

    @property
    def first_frame(self) -> int:
        return self.updates[0].frame_number

    @property
    def last_frame(self) -> int:
        return self.updates[-1].frame_number

    @property
    def lifespan(self) -> int:
        """Frames spanned from first to last update, inclusive (held life, coasting included)."""
        return self.last_frame - self.first_frame + 1

    @property
    def observation_count(self) -> int:
        """Detections the tracker assigned to this track (its own running count)."""
        return max((update.detection_count for update in self.updates), default=0)

    @property
    def matched_update_count(self) -> int:  # added
        """Updates of this track that were matched to a detection (the ones that are observations)."""
        return sum(1 for update in self.updates if update.is_matched)

    @property
    def mean_confidence(self) -> float:
        return sum(update.confidence for update in self.updates) / len(self.updates) if self.updates else 0.0

    @property
    def max_confidence(self) -> float:
        return max((update.confidence for update in self.updates), default=0.0)

    @property
    def trajectory(self) -> tuple[tuple[int, float, float], ...]:
        return tuple((update.frame_number, *update.position_xy) for update in self.updates)


@dataclass(frozen=True)
class StageStat:
    """Accumulated timing for one pipeline stage over a run."""

    calls: int
    total_seconds: float

    @property
    def ms_per_call(self) -> float:
        return (self.total_seconds / self.calls * 1000.0) if self.calls > 0 else 0.0


StageTiming = dict[str, StageStat]
"""Performance surface: stage name -> accumulated timing."""


@dataclass(frozen=True)
class Provenance:
    """What produced a run. Travels with the result so a comparison can be trusted.

    ``extra`` is free-form but this kit always fills (see ``evaluation.provenance``):
    ``predictor`` (``"gt"``, ``"detector"``, ``"kit"``, ``"cloud"``), ``dataset``, ``video_id``,
    ``claim`` (what a comparison against this run asserts: ``accuracy``, ``parity``, ``regression``),
    the sha256 of every input file, and for tracker runs the tracker parameters, the detection
    source, the hash of ``tracker/`` and whether coasting rows are distinguishable
    (``coasting_known``).
    """

    config_hash: str
    git_commit: str
    model_hash: str
    extra: dict = field(default_factory=dict)


@dataclass(frozen=True)
class RunResult:
    """A single producer's evaluation inputs plus its provenance.

    ``correctness`` holds observations; ``tracks`` holds the reconstructed tracks; ``performance``
    holds per-stage timing (empty for CSV-derived runs).
    """

    correctness: FrameDetections
    performance: StageTiming
    provenance: Provenance
    tracks: tuple[Track, ...] = ()

    @property
    def observation_count(self) -> int:  # added
        return sum(len(detections) for detections in self.correctness.values())

    @property
    def update_count(self) -> int:  # added
        return sum(len(track.updates) for track in self.tracks)

    @property
    def track_ids(self) -> tuple[str, ...]:  # added
        return tuple(track.track_id for track in self.tracks)


def reconstruct_tracks(track_updates: list[tuple[str, TrackUpdate]]) -> tuple[Track, ...]:
    """Group ``(track_id, update)`` pairs into ``Track``s, updates ordered by frame.

    Deterministic: tracks are returned ordered by ``(first_frame, track_id)``. Raises if a track
    has two updates for the same frame, since that would make its trajectory ambiguous.
    """
    grouped: dict[str, list[TrackUpdate]] = {}
    for track_id, update in track_updates:
        grouped.setdefault(track_id, []).append(update)
    tracks = []
    for track_id, updates in grouped.items():
        ordered = tuple(sorted(updates, key=lambda update: update.frame_number))
        frames = [update.frame_number for update in ordered]
        if len(frames) != len(set(frames)):
            raise ValueError(f"track {track_id!r} has more than one update in the same frame")
        tracks.append(Track(track_id=track_id, updates=ordered))
    return tuple(sorted(tracks, key=lambda track: (track.first_frame, track.track_id)))
