"""Builders for small synthetic runs used across the tests."""

from __future__ import annotations

from evaluation.contracts import Detection, Provenance, RunResult, TrackUpdate, reconstruct_tracks

BOX = 10.0


def run_from_centers(
    centers_by_frame: dict[int, list[tuple[str, float, float]]],
    predictor: str = "test",
    claim: str = "accuracy",
    coasting_known: bool = True,
    box: float = BOX,
) -> RunResult:
    """One observation and one update per ``(track_id, cx, cy)`` entry."""
    correctness = {}
    updates = []
    seen: dict[str, int] = {}
    first: dict[str, int] = {}
    for frame in sorted(centers_by_frame):
        for track_id, cx, cy in centers_by_frame[frame]:
            b = (cx - box / 2, cy - box / 2, box, box)
            correctness.setdefault(frame, []).append(Detection(b, 1.0, track_id, "bird"))
            seen[track_id] = seen.get(track_id, 0) + 1
            first.setdefault(track_id, frame)
            updates.append((track_id, TrackUpdate(frame, (cx, cy), 1.0, seen[track_id], 0, frame - first[track_id] + 1, b)))
    return RunResult(
        correctness=correctness,
        performance={},
        provenance=Provenance("cfg", "none", "model", {"predictor": predictor, "claim": claim, "dataset": "test", "video_id": "test", "coasting_known": coasting_known}),
        tracks=reconstruct_tracks(updates),
    )


def straight_line(track_id: str, frames: range, x0: float, y0: float, dx: float, dy: float):
    return {frame: [(track_id, x0 + dx * i, y0 + dy * i)] for i, frame in enumerate(frames)}


def merge(*runs: dict) -> dict:
    out: dict = {}
    for run in runs:
        for frame, entries in run.items():
            out.setdefault(frame, []).extend(entries)
    return out
