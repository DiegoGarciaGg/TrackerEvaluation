"""One evaluation of a candidate run against a reference: metrics table plus diagnostics.

The report names its claim from the reference's provenance (``accuracy`` against ground truth,
``parity`` against the cloud, ``regression`` against a frozen baseline), scores every available
view of the candidate (matched rows only, every row as written) at every match distance asked
for, with and without the ignore region, and attaches the diagnostics once, for the default
distance and the primary view. No metric here is an acceptance gate; the report is evidence.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, Sequence

from evaluation.contracts import Provenance, RunResult
from evaluation.diagnostics import Diagnostics, diagnose
from evaluation.similarity import DEFAULT_THRESHOLD, scale_for_match_px
from evaluation.trackeval_bridge import build_sequence, center_distance_similarity, run_metrics, trackeval_provenance
from evaluation.views import (
    IgnoreRegion,
    ViewKind,
    apply_reference_proximity,
    apply_region,
    available_views,
    count_entries,
    restrict_frames,
    view_of,
)

DEFAULT_MATCH_PX: tuple[float, ...] = (4.0, 6.0, 8.0, 12.0)
DEFAULT_PX = 8.0
TABLE_METRICS = ("HOTA", "AssA", "MOTA", "MOTP_px", "IDF1", "IDSW", "Frag")


@dataclass(frozen=True)
class MetricRow:
    view: ViewKind
    match_px: float
    ignore_region: bool
    reference_entries: int
    candidate_entries: int
    metrics: dict


@dataclass
class EvaluationReport:
    claim: str
    candidate_provenance: Provenance
    reference_provenance: Provenance
    settings: dict
    rows: list[MetricRow]
    diagnostics: Diagnostics
    diagnostics_setting: dict  # which view / region / px the diagnostics were computed on
    notes: list[str] = field(default_factory=list)

    def row(self, view: ViewKind, match_px: float, ignore_region: bool) -> Optional[MetricRow]:
        for row in self.rows:
            if row.view == view and row.match_px == match_px and row.ignore_region == ignore_region:
                return row
        return None

    def to_json(self) -> dict:
        return {
            "claim": self.claim,
            "candidate_provenance": _provenance_json(self.candidate_provenance),
            "reference_provenance": _provenance_json(self.reference_provenance),
            "settings": self.settings,
            "rows": [
                {"view": r.view, "match_px": r.match_px, "ignore_region": r.ignore_region,
                 "reference_entries": r.reference_entries, "candidate_entries": r.candidate_entries, "metrics": r.metrics}
                for r in self.rows
            ],
            "diagnostics_setting": self.diagnostics_setting,
            "diagnostics": self.diagnostics.to_json(),
            "notes": self.notes,
        }


def evaluate(
    candidate: RunResult,
    reference: RunResult,
    match_px: Sequence[float] = DEFAULT_MATCH_PX,
    default_px: float = DEFAULT_PX,
    region: Optional[IgnoreRegion] = None,
    frame_range: Optional[tuple[int, int]] = None,
    views: Optional[Sequence[ViewKind]] = None,
    threshold: float = DEFAULT_THRESHOLD,
    reference_proximity_px: Optional[float] = None,
) -> EvaluationReport:
    notes: list[str] = []
    candidate_views = list(views) if views is not None else available_views(candidate)
    if candidate.tracks and candidate.provenance.extra.get("coasting_known") is False:
        notes.append("candidate is in the 6-column baseline format: coasting rows are indistinguishable, so only "
                     "the 'updates' view (every row as written) is scored")
    if frame_range is not None:
        notes.append(f"frames restricted to {frame_range[0]}..{frame_range[1]} on both sides")
    use_region_options = [False] + ([True] if region is not None and not region.is_empty() else [])
    if len(use_region_options) == 2:
        notes.append(f"ignore region '{region.label}': entries with center inside it are dropped on both sides before scoring")
    if reference_proximity_px is not None:
        notes.append(f"reference proximity filter: candidate entries farther than {reference_proximity_px:g} px from every "
                     "labelled object in their frame are dropped before scoring, so false positives far from the labelled objects are NOT counted")

    reference_kind: ViewKind = "observations" if "observations" in available_views(reference) else "updates"
    reference_full = restrict_frames(view_of(reference, reference_kind), frame_range)
    num_timesteps = _num_timesteps(candidate, reference)

    rows: list[MetricRow] = []
    diagnostics: Optional[Diagnostics] = None
    diagnostics_setting: dict = {}
    for kind in candidate_views:
        candidate_full = restrict_frames(view_of(candidate, kind), frame_range)
        for use_region in use_region_options:
            reference_view = apply_region(reference_full, region) if use_region else reference_full
            candidate_view = apply_region(candidate_full, region) if use_region else candidate_full
            if reference_proximity_px is not None:
                candidate_view = apply_reference_proximity(candidate_view, reference_view, reference_proximity_px)
            for px in match_px:
                sequence = build_sequence(reference_view, candidate_view, center_distance_similarity(px, threshold), num_timesteps)
                metrics = run_metrics(sequence, threshold, scale_px=scale_for_match_px(px, threshold))
                rows.append(MetricRow(kind, float(px), use_region, count_entries(reference_view), count_entries(candidate_view), metrics))
            # diagnostics once: primary view, region applied when there is one
            if kind == candidate_views[0] and use_region == use_region_options[-1]:
                diagnostics = diagnose(reference_view, candidate_view, default_px)
                diagnostics_setting = {"view": kind, "ignore_region": use_region, "match_px": default_px}

    settings = {
        "match_px": [float(px) for px in match_px],
        "default_px": default_px,
        "similarity": "s = max(0, 1 - d / T), T = match_px / (1 - threshold)",
        "threshold": threshold,
        "scales_T": {str(float(px)): scale_for_match_px(px, threshold) for px in match_px},
        "reference_view": reference_kind,
        "candidate_views": candidate_views,
        "ignore_region": region.to_json() if region is not None else None,
        "frame_range": list(frame_range) if frame_range else None,
        "reference_proximity_px": reference_proximity_px,
        "num_timesteps": num_timesteps,
        "trackeval": trackeval_provenance(),
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    return EvaluationReport(
        claim=reference.provenance.extra.get("claim", "unknown"),
        candidate_provenance=candidate.provenance,
        reference_provenance=reference.provenance,
        settings=settings,
        rows=rows,
        diagnostics=diagnostics,
        diagnostics_setting=diagnostics_setting,
        notes=notes,
    )


def _num_timesteps(candidate: RunResult, reference: RunResult) -> int:
    last = -1
    for result in (candidate, reference):
        video = result.provenance.extra.get("inputs", {}).get("video", {})
        if "frame_count" in video:
            last = max(last, int(video["frame_count"]) - 1)
        last = max([last] + list(result.correctness) + [track.last_frame for track in result.tracks])
    return last + 1


def _provenance_json(provenance: Provenance) -> dict:
    return {"config_hash": provenance.config_hash, "git_commit": provenance.git_commit, "model_hash": provenance.model_hash, "extra": provenance.extra}


# ----------------------------------------------------------------------------- rendering


def render_markdown(report: EvaluationReport, max_switches: int = 60, max_tracks: int = 60) -> str:
    candidate = report.candidate_provenance.extra
    reference = report.reference_provenance.extra
    lines = [f"# Tracker evaluation: claim = {report.claim.upper()}", ""]
    lines.append(f"Candidate: predictor={candidate.get('predictor')} dataset={candidate.get('dataset')} video={candidate.get('video_id')} "
                 f"detections={candidate.get('detection_source', 'n/a')} config={json.dumps(candidate.get('config', {}), sort_keys=True)}")
    lines.append(f"Reference: predictor={reference.get('predictor')} claim={reference.get('claim')} curation={reference.get('curation', 'n/a')}")

    lines += ["", "## Provenance"]
    for role, provenance in (("candidate", report.candidate_provenance), ("reference", report.reference_provenance)):
        lines.append(f"- {role}: config_hash={provenance.config_hash[:12]} git={provenance.git_commit} model={str(provenance.model_hash)[:12]}")
        for label, item in provenance.extra.get("inputs", {}).items():
            lines.append(f"  - {label}: {item['path']} sha256={item['sha256'][:16]}")
        if provenance.extra.get("tracker_source_hash"):
            lines.append(f"  - tracker/ hash={str(provenance.extra['tracker_source_hash'])[:16]} coasting_known={provenance.extra.get('coasting_known')}")
        for note in provenance.extra.get("notes", []):
            lines.append(f"  - note: {note}")
    te = report.settings["trackeval"]
    lines.append(f"- metrics engine: {te['library']} {te['commit'][:12]} ({te['url']}); {te['numpy_alias_shim']}")
    lines.append(f"- similarity: {report.settings['similarity']}, threshold {report.settings['threshold']}; T per px: {report.settings['scales_T']}")
    lines += [f"- {note}" for note in report.notes]

    lines += ["", "## Metrics (center-distance matching)", "",
              "| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |", "|---|---|---|---|---|---|---|---|---|---|"]
    for r in report.rows:
        m = r.metrics
        lines.append(f"| {r.view} | {'ignore' if r.ignore_region else 'none'} | {r.match_px:g} | {m['HOTA']:.3f} | {m['AssA']:.3f} | "
                     f"{m['MOTA']:.3f} | {m['MOTP_px']:.2f} | {m['IDF1']:.3f} | {m['IDSW']} | {m['Frag']} |")
    lines += ["", "HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas. AssA = association accuracy (one bird, one id). "
              "MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. "
              "IDF1 = identity F1. IDSW = identity switches. Frag = fragmentations (CLEAR definition: resumptions after any interruption, "
              "including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). "
              "`observations` = matched rows only; `updates` = every row as written. Other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, "
              "OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report."]

    d = report.diagnostics
    s = report.diagnostics_setting
    lines += ["", f"## Diagnostics (view={s.get('view')}, region={'ignored' if s.get('ignore_region') else 'none'}, match {d.match_px:g} px)"]
    lines.append(f"- reference objects: {d.reference_objects}; candidate ids: {d.candidate_ids}; matched pairs: {d.matched_pairs}; "
                 f"unmatched reference entries: {d.unmatched_reference}; unmatched candidate entries: {d.unmatched_candidate}")
    lines.append(f"- identity switches: {len(d.identity_switches)}; fragmentation (coverage interruptions within labelled frames): {d.fragmentation}; "
                 f"orphan candidate ids (never on a reference object): {len(d.orphan_candidate_ids)}")

    lines += ["", "### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous cover)"]
    lines += [f"- f{sw.frame}: ref {sw.reference_id}: {sw.previous_candidate_id} -> {sw.new_candidate_id} at ({sw.position_xy[0]:g}, {sw.position_xy[1]:g}), "
              f"{sw.frames_since_previous} frames after previous cover" for sw in d.identity_switches[:max_switches]] or ["- none"]
    if len(d.identity_switches) > max_switches:
        lines.append(f"- ... {len(d.identity_switches) - max_switches} more in the JSON report")

    lines += ["", "### Candidate ids per reference object", "| reference id | frames | covered | fragments | candidate ids (frames) |", "|---|---|---|---|---|"]
    for c in d.coverage:
        ids = ", ".join(f"{k} ({v})" for k, v in list(c.candidate_ids.items())[:12])
        lines.append(f"| {c.reference_id} | {c.frames} ({c.first_frame}..{c.last_frame}) | {c.covered} | {c.fragments} | {ids} |")

    lines += ["", "### Candidate tracks (gaps and durations)"]
    if d.durations:
        lifespans = sorted(t.lifespan for t in d.durations)
        lines.append(f"- tracks: {len(d.durations)}; lifespan min/median/max: {lifespans[0]}/{lifespans[len(lifespans) // 2]}/{lifespans[-1]}; "
                     f"orphans: {len(d.orphan_candidate_ids)}; tracks ending uncovered: {sum(1 for t in d.durations if t.trailing_coasting)}")
        lines += ["| id | frames | lifespan | rows | rows on a reference object | internal uncovered runs | longest run | trailing uncovered | covers |", "|---|---|---|---|---|---|---|---|---|"]
        for t in d.durations[:max_tracks]:
            lines.append(f"| {t.track_id} | {t.first_frame}..{t.last_frame} | {t.lifespan} | {t.rows} | {t.matched_rows} | {t.internal_gaps} | "
                         f"{t.longest_internal_gap} | {t.trailing_coasting} | {', '.join(t.covered_reference_ids) or '-'} |")
        if len(d.durations) > max_tracks:
            lines.append(f"| ... | {len(d.durations) - max_tracks} more in JSON | | | | | | | |")
    return "\n".join(lines) + "\n"
