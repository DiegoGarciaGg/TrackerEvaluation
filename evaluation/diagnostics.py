"""Our own diagnostics: not scores, but the list of what went wrong and where.

Per frame, reference and candidate entries are matched one-to-one by the Hungarian algorithm
under a center-distance gate, with CLEAR's tie-break (a candidate id that covered the same
reference object in the previous frame is preferred), so the identity switches listed here are
the ones CLEAR's ``IDSW`` counts. From that association:

- **identity switches**: for each reference object, every frame where the covering candidate id
  differs from the last candidate id that covered it. A gap does not reset the memory, so losing
  and recovering an object under the same id is not a switch; a mutual swap of two objects' ids
  is two switches.
- **candidate ids per reference object** (fragmentation of the identity across tracks);
- **orphan candidate ids**: tracker ids that never covered any reference object;
- **ids versus objects**: counts on both sides;
- **gaps and durations**: per candidate track, lifespan, matched and coasting rows, internal
  runs of coasting rows and the trailing run; per reference object, coverage and the number of
  interruptions (fragments).
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Optional

import numpy as np
from scipy.optimize import linear_sum_assignment

from evaluation.contracts import RunResult
from evaluation.similarity import center_distance_matrix
from evaluation.views import FrameView


@dataclass(frozen=True)
class IdentitySwitch:
    frame: int
    reference_id: str
    previous_candidate_id: str
    new_candidate_id: str
    position_xy: tuple[float, float]
    frames_since_previous: int


@dataclass(frozen=True)
class ReferenceCoverage:
    reference_id: str
    frames: int
    covered: int
    fragments: int  # coverage interruptions that later resume
    candidate_ids: dict[str, int]  # candidate id -> frames it covered this object
    first_frame: int
    last_frame: int


@dataclass(frozen=True)
class TrackDuration:
    track_id: str
    first_frame: int
    last_frame: int
    lifespan: int
    rows: int
    matched_rows: int  # rows of this track that covered a reference object (not the kit's "matched" column)
    coasting_rows: int  # rows that covered no reference object
    internal_gaps: int  # runs of uncovered rows later followed by a covered row
    longest_internal_gap: int
    trailing_coasting: int  # uncovered rows at the end of the track
    covered_reference_ids: tuple[str, ...]


@dataclass
class Diagnostics:
    match_px: float
    reference_objects: int
    candidate_ids: int
    matched_pairs: int
    unmatched_reference: int
    unmatched_candidate: int
    identity_switches: list[IdentitySwitch]
    coverage: list[ReferenceCoverage]
    orphan_candidate_ids: list[str]
    durations: list[TrackDuration]

    @property
    def fragmentation(self) -> int:
        return sum(item.fragments for item in self.coverage)

    def to_json(self) -> dict:
        payload = asdict(self)
        payload["fragmentation"] = self.fragmentation
        return payload


def associate(reference: FrameView, candidate: FrameView, match_px: float) -> dict[int, list[tuple[int, int]]]:
    """Per frame, matched ``(reference_index, candidate_index)`` pairs under the gate.

    Hungarian on ``score = 1000 * same_as_previous + (1 - d / match_px)``, zeroed where
    ``d > match_px``; the same objective CLEAR uses with the distance similarity at scale
    ``2 * match_px`` and threshold 0.5.
    """
    previous: dict[str, str] = {}  # reference id -> candidate id in the previous frame
    pairs: dict[int, list[tuple[int, int]]] = {}
    for frame in sorted(set(reference) | set(candidate)):
        reference_entries = reference.get(frame, [])
        candidate_entries = candidate.get(frame, [])
        current: dict[str, str] = {}
        if reference_entries and candidate_entries:
            distances = center_distance_matrix(
                [e.center for e in reference_entries], [e.center for e in candidate_entries]
            )
            score = np.maximum(0.0, 1.0 - distances / (2.0 * match_px))
            same = np.array(
                [[previous.get(r.track_id) == c.track_id for c in candidate_entries] for r in reference_entries],
                dtype=float,
            )
            score = 1000.0 * same + score
            score[distances > match_px + 1e-9] = 0.0
            rows, cols = linear_sum_assignment(-score)
            kept = [(int(r), int(c)) for r, c in zip(rows, cols) if score[r, c] > 0]
            pairs[frame] = kept
            for r, c in kept:
                current[reference_entries[r].track_id] = candidate_entries[c].track_id
        else:
            pairs[frame] = []
        previous = current
    return pairs


def diagnose(reference: FrameView, candidate: FrameView, match_px: float) -> Diagnostics:
    pairs = associate(reference, candidate, match_px)
    frames = sorted(set(reference) | set(candidate))

    covering: dict[str, list[tuple[int, Optional[str], tuple[float, float]]]] = {}
    matched_candidate_rows: dict[str, set[int]] = {}
    covered_by: dict[str, set[str]] = {}
    matched_pairs = unmatched_reference = unmatched_candidate = 0

    for frame in frames:
        reference_entries = reference.get(frame, [])
        candidate_entries = candidate.get(frame, [])
        by_reference = {r: c for r, c in pairs.get(frame, [])}
        matched_pairs += len(by_reference)
        unmatched_reference += len(reference_entries) - len(by_reference)
        unmatched_candidate += len(candidate_entries) - len(by_reference)
        for index, entry in enumerate(reference_entries):
            candidate_index = by_reference.get(index)
            candidate_id = candidate_entries[candidate_index].track_id if candidate_index is not None else None
            covering.setdefault(entry.track_id, []).append((frame, candidate_id, entry.center))
            if candidate_id is not None:
                matched_candidate_rows.setdefault(candidate_id, set()).add(frame)
                covered_by.setdefault(candidate_id, set()).add(entry.track_id)

    switches: list[IdentitySwitch] = []
    coverage: list[ReferenceCoverage] = []
    for reference_id, history in covering.items():
        last_id: Optional[str] = None
        last_frame_with_id: Optional[int] = None
        fragments = 0
        previously_covered = False
        runs = 0
        per_candidate: dict[str, int] = {}
        for frame, candidate_id, center in history:
            covered = candidate_id is not None
            if covered and not previously_covered:
                runs += 1
            previously_covered = covered
            if candidate_id is None:
                continue
            per_candidate[candidate_id] = per_candidate.get(candidate_id, 0) + 1
            if last_id is not None and candidate_id != last_id:
                switches.append(
                    IdentitySwitch(
                        frame=frame,
                        reference_id=reference_id,
                        previous_candidate_id=last_id,
                        new_candidate_id=candidate_id,
                        position_xy=(round(center[0], 1), round(center[1], 1)),
                        frames_since_previous=frame - (last_frame_with_id if last_frame_with_id is not None else frame),
                    )
                )
            last_id = candidate_id
            last_frame_with_id = frame
        fragments = max(0, runs - 1)
        coverage.append(
            ReferenceCoverage(
                reference_id=reference_id,
                frames=len(history),
                covered=sum(1 for _, candidate_id, _ in history if candidate_id is not None),
                fragments=fragments,
                candidate_ids=dict(sorted(per_candidate.items(), key=lambda item: -item[1])),
                first_frame=history[0][0],
                last_frame=history[-1][0],
            )
        )
    switches.sort(key=lambda s: (s.frame, s.reference_id))

    durations: list[TrackDuration] = []
    candidate_frames: dict[str, list[int]] = {}
    for frame in frames:
        for entry in candidate.get(frame, []):
            candidate_frames.setdefault(entry.track_id, []).append(frame)
    for track_id, track_frames in candidate_frames.items():
        track_frames = sorted(track_frames)
        matched = matched_candidate_rows.get(track_id, set())
        flags = [frame in matched for frame in track_frames]
        internal_gaps = 0
        longest = 0
        run = 0
        trailing = 0
        for flag in flags:
            if flag:
                if run:
                    internal_gaps += 1
                    longest = max(longest, run)
                run = 0
            else:
                run += 1
        trailing = run
        durations.append(
            TrackDuration(
                track_id=track_id,
                first_frame=track_frames[0],
                last_frame=track_frames[-1],
                lifespan=track_frames[-1] - track_frames[0] + 1,
                rows=len(track_frames),
                matched_rows=sum(flags),
                coasting_rows=len(flags) - sum(flags),
                internal_gaps=internal_gaps,
                longest_internal_gap=longest,
                trailing_coasting=trailing,
                covered_reference_ids=tuple(sorted(covered_by.get(track_id, ()), key=_id_key)),
            )
        )
    durations.sort(key=lambda d: (d.first_frame, _id_key(d.track_id)))
    orphans = sorted((d.track_id for d in durations if not d.covered_reference_ids), key=_id_key)

    return Diagnostics(
        match_px=match_px,
        reference_objects=len(covering),
        candidate_ids=len(candidate_frames),
        matched_pairs=matched_pairs,
        unmatched_reference=unmatched_reference,
        unmatched_candidate=unmatched_candidate,
        identity_switches=switches,
        coverage=sorted(coverage, key=lambda c: (c.first_frame, _id_key(c.reference_id))),
        orphan_candidate_ids=orphans,
        durations=durations,
    )


def _id_key(track_id: str):
    return (0, int(track_id)) if track_id.lstrip("-").isdigit() else (1, track_id)
