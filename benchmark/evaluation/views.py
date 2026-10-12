"""Per-frame views of a run for scoring, plus ignore regions and frame restriction.

A tracker run has two legitimate per-frame readings, and the report shows both:

- ``"observations"``: only rows matched to a detection (the ``Detection``s of the finished
  surface). Requires a run whose coasting rows are known (10-column format); on a 6-column
  baseline it is refused, since every row there was recorded as an observation.
- ``"updates"``: every row as the kit writes it (all ``TrackUpdate``s, coasting included), the
  same thing the annotated video shows.

Ground truth and the cloud export have only observations. Every view is a mapping
``frame_number -> [Entry]``, with the entry's center as the position scored by center-distance
similarity and its box (when present) for IoU.

An ``IgnoreRegion`` marks unlabelled image space (for the flock clip, the burnt-in timestamp at
the top-left). Candidate entries whose center lies inside it are dropped before scoring so they
cannot count as false positives; reference entries inside it are dropped too, for symmetry.
Reports always score with and without the region.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, Optional

from evaluation.contracts import Box, RunResult

ViewKind = Literal["observations", "updates"]


@dataclass(frozen=True)
class Entry:
    track_id: str
    center: tuple[float, float]
    box: Optional[Box] = None


FrameView = dict[int, list[Entry]]


def observations_view(result: RunResult) -> FrameView:
    view: FrameView = {}
    for frame, detections in result.correctness.items():
        entries = []
        for detection in detections:
            if detection.track_id is None:
                raise ValueError("observations without a track_id cannot be scored as a tracker output")
            x, y, w, h = detection.box_xywh
            entries.append(Entry(detection.track_id, (x + w / 2.0, y + h / 2.0), detection.box_xywh))
        if entries:
            view[frame] = entries
    return view


def updates_view(result: RunResult) -> FrameView:
    view: FrameView = {}
    for track in result.tracks:
        for update in track.updates:
            view.setdefault(update.frame_number, []).append(Entry(track.track_id, update.position_xy, update.box_xywh))
    return view


def view_of(result: RunResult, kind: ViewKind) -> FrameView:
    """Build the requested view, refusing ``observations`` on a run with unknown coasting."""
    if kind == "observations":
        if result.provenance.extra.get("coasting_known") is False:
            raise ValueError(
                "matched-rows-only evaluation needs the 10-column tracker format; this run is the "
                "6-column baseline format where coasting rows are indistinguishable"
            )
        return observations_view(result)
    if kind == "updates":
        if not result.tracks:
            return observations_view(result)
        return updates_view(result)
    raise ValueError(f"unknown view kind {kind!r}")


def available_views(result: RunResult) -> list[ViewKind]:
    """Views a report can show for this run: both for a 10-column run, ``updates`` alone otherwise."""
    if result.provenance.extra.get("predictor") in ("gt", "cloud") or not result.tracks:
        return ["observations"]
    if result.provenance.extra.get("coasting_known") is False:
        return ["updates"]
    return ["observations", "updates"]


@dataclass(frozen=True)
class IgnoreRegion:
    """Rectangles ``(x1, y1, x2, y2)`` and polygons ``[(x, y), ...]`` in image pixels."""

    rects: tuple[tuple[float, float, float, float], ...] = ()
    polygons: tuple[tuple[tuple[float, float], ...], ...] = ()
    label: str = ""

    def contains(self, x: float, y: float) -> bool:
        for x1, y1, x2, y2 in self.rects:
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True
        return any(_point_in_polygon(x, y, polygon) for polygon in self.polygons)

    def is_empty(self) -> bool:
        return not self.rects and not self.polygons

    def to_json(self) -> dict:
        return {"label": self.label, "rects": [list(r) for r in self.rects], "polygons": [[list(p) for p in poly] for poly in self.polygons]}

    @staticmethod
    def from_json(payload: dict) -> "IgnoreRegion":
        return IgnoreRegion(
            rects=tuple(tuple(r) for r in payload.get("rects", [])),
            polygons=tuple(tuple(tuple(p) for p in poly) for poly in payload.get("polygons", [])),
            label=payload.get("label", ""),
        )


FLOCK_TIMESTAMP_OVERLAY = IgnoreRegion(rects=((0.0, 0.0, 721.0, 400.0),), label="burnt-in timestamp overlay, top-left")


def _point_in_polygon(x: float, y: float, polygon: tuple[tuple[float, float], ...]) -> bool:
    inside = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            x_cross = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_cross:
                inside = not inside
    return inside


def apply_region(view: FrameView, region: Optional[IgnoreRegion]) -> FrameView:
    if region is None or region.is_empty():
        return view
    filtered: FrameView = {}
    for frame, entries in view.items():
        kept = [entry for entry in entries if not region.contains(*entry.center)]
        if kept:
            filtered[frame] = kept
    return filtered


def restrict_frames(view: FrameView, frame_range: Optional[tuple[int, int]]) -> FrameView:
    if frame_range is None:
        return view
    first, last = frame_range
    return {frame: entries for frame, entries in view.items() if first <= frame <= last}


def count_entries(view: FrameView) -> int:
    return sum(len(entries) for entries in view.values())


def apply_reference_proximity(candidate: FrameView, reference: FrameView, radius_px: float) -> FrameView:
    """Keep only candidate entries within ``radius_px`` of some reference entry in the same frame.

    For a partially labelled clip (the flock clip has a second, unlabelled flock; the turbine
    clip has unlabelled birds and the blade) this turns the scoring into "within the labelled
    objects' neighbourhood": tracker output far from every labelled object is not counted as a
    false positive. Recall-side quantities are unchanged. Reports that use it say so, since it
    hides genuine false positives that happen to be far from the labelled birds.
    """
    import numpy as np

    kept: FrameView = {}
    for frame, entries in candidate.items():
        reference_entries = reference.get(frame, [])
        if not reference_entries:
            continue
        ref = np.array([e.center for e in reference_entries], dtype=float)
        cand = np.array([e.center for e in entries], dtype=float)
        distances = np.sqrt(((ref[:, None, :] - cand[None, :, :]) ** 2).sum(axis=2)).min(axis=0)
        close = [entry for entry, d in zip(entries, distances) if d <= radius_px]
        if close:
            kept[frame] = close
    return kept
