"""One evaluation of a candidate run against a reference: metrics table, sensitivity, diagnostics.

The report names its claim from the reference's provenance (``accuracy`` against ground truth,
``parity`` against the cloud, ``regression`` against a frozen baseline), scores every available
view of the candidate (all rows as written, matched rows only) at every match distance asked
for, with and without the ignore region, and attaches the diagnostics at the default distance.
No metric here is an acceptance gate; the report is evidence.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, Sequence

from evaluation.contracts import Provenance, RunResult
from evaluation.diagnostics import Diagnostics, diagnose
from evaluation.similarity import DEFAULT_THRESHOLD, scale_for_match_px
from evaluation.trackeval_bridge import (
    SUMMARY_FIELDS,
    build_sequence,
    center_distance_similarity,
    run_metrics,
    trackeval_provenance,
)
from evaluation.views import (
    FrameView,
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
    diagnostics: dict[str, Diagnostics]  # keyed "<view>|region" / "<view>|noregion"
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
                {
                    "view": row.view,
                    "match_px": row.match_px,
                    "ignore_region": row.ignore_region,
                    "reference_entries": row.reference_entries,
                    "candidate_entries": row.candidate_entries,
                    "metrics": row.metrics,
                }
                for row in self.rows
            ],
            "diagnostics": {key: value.to_json() for key, value in self.diagnostics.items()},
            "notes": self.notes,
        }


def claim_of(reference: RunResult) -> str:
    return reference.provenance.extra.get("claim", "unknown")


def reference_view_kind(reference: RunResult) -> ViewKind:
    return "observations" if "observations" in available_views(reference) else "updates"


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
    if reference_proximity_px is not None:
        notes.append(
            f"reference proximity filter: candidate entries farther than {reference_proximity_px:g} px from every "
            "labelled object in their frame are dropped before scoring (partially labelled clip); false positives "
            "far from the labelled objects are therefore NOT counted"
        )
    candidate_views = list(views) if views is not None else available_views(candidate)
    if candidate.tracks and candidate.provenance.extra.get("coasting_known") is False and "observations" not in candidate_views:
        notes.append(
            "candidate is in the 6-column baseline format: coasting rows are indistinguishable, so only "
            "the 'updates' view (every row as written) is scored; matched-rows-only needs the 10-column format"
        )
    reference_kind = reference_view_kind(reference)
    reference_full = restrict_frames(view_of(reference, reference_kind), frame_range)
    if frame_range is not None:
        notes.append(f"frames restricted to {frame_range[0]}..{frame_range[1]} on both sides")
    region_options = [False] + ([True] if region is not None and not region.is_empty() else [])
    if region is not None and not region.is_empty():
        notes.append(f"ignore region '{region.label}': entries with center inside it are dropped on both sides before scoring")

    num_timesteps = _num_timesteps(candidate, reference)
    rows: list[MetricRow] = []
    diagnostics: dict[str, Diagnostics] = {}
    for kind in candidate_views:
        candidate_full = restrict_frames(view_of(candidate, kind), frame_range)
        for use_region in region_options:
            reference_view = apply_region(reference_full, region) if use_region else reference_full
            candidate_view = apply_region(candidate_full, region) if use_region else candidate_full
            if reference_proximity_px is not None:
                candidate_view = apply_reference_proximity(candidate_view, reference_view, reference_proximity_px)
            for px in match_px:
                sequence = build_sequence(reference_view, candidate_view, center_distance_similarity(px, threshold), num_timesteps)
                metrics = run_metrics(sequence, threshold, scale_px=scale_for_match_px(px, threshold))
                rows.append(MetricRow(kind, float(px), use_region, count_entries(reference_view), count_entries(candidate_view), metrics))
            diagnostics[f"{kind}|{'region' if use_region else 'noregion'}"] = diagnose(reference_view, candidate_view, default_px)

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
        claim=claim_of(reference),
        candidate_provenance=candidate.provenance,
        reference_provenance=reference.provenance,
        settings=settings,
        rows=rows,
        diagnostics=diagnostics,
        notes=notes,
    )


def _num_timesteps(candidate: RunResult, reference: RunResult) -> int:
    last = -1
    for result in (candidate, reference):
        video = result.provenance.extra.get("inputs", {}).get("video", {})
        if "frame_count" in video:
            last = max(last, int(video["frame_count"]) - 1)
        for frame in result.correctness:
            last = max(last, frame)
        for track in result.tracks:
            last = max(last, track.last_frame)
    return last + 1


def _provenance_json(provenance: Provenance) -> dict:
    return {
        "config_hash": provenance.config_hash,
        "git_commit": provenance.git_commit,
        "model_hash": provenance.model_hash,
        "extra": provenance.extra,
    }


# ----------------------------------------------------------------------------------------------
# Rendering


def render_markdown(report: EvaluationReport, max_switches: int = 60) -> str:
    lines: list[str] = []
    candidate = report.candidate_provenance.extra
    reference = report.reference_provenance.extra
    lines.append(f"# Tracker evaluation: claim = {report.claim.upper()}")
    lines.append("")
    lines.append(
        f"Candidate: predictor={candidate.get('predictor')} dataset={candidate.get('dataset')} "
        f"video={candidate.get('video_id')} detections={candidate.get('detection_source', 'n/a')} "
        f"config={json.dumps(candidate.get('config', {}), sort_keys=True)}"
    )
    lines.append(
        f"Reference: predictor={reference.get('predictor')} claim={reference.get('claim')} "
        f"curation={reference.get('curation', 'n/a')}"
    )
    lines.append("")
    lines.append("## Provenance")
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
    for note in report.notes:
        lines.append(f"- {note}")
    lines.append("")

    lines.append("## Metrics (center-distance matching)")
    header = "| view | region | px | ref | cand | HOTA | DetA | AssA | LocA px | HOTA@a.5 | MOTA | MOTP px | IDSW | Frag | IDF1 | IDP | IDR | Re | Pr | TP | FN | FP | MT | PT | ML |"
    lines.append(header)
    lines.append("|" + "---|" * (header.count("|") - 1))
    for row in report.rows:
        m = row.metrics
        lines.append(
            f"| {row.view} | {'ignore' if row.ignore_region else 'none'} | {row.match_px:g} | {row.reference_entries} | {row.candidate_entries} | "
            f"{m['HOTA']:.3f} | {m['DetA']:.3f} | {m['AssA']:.3f} | {m['LocA_px']:.2f} | {m['HOTA_a50']:.3f} | "
            f"{m['MOTA']:.3f} | {m['MOTP_px']:.2f} | {m['IDSW']} | {m['Frag']} | {m['IDF1']:.3f} | {m['IDP']:.3f} | {m['IDR']:.3f} | "
            f"{m['CLR_Re']:.3f} | {m['CLR_Pr']:.3f} | {m['CLR_TP']} | {m['CLR_FN']} | {m['CLR_FP']} | {m['MT']} | {m['PT']} | {m['ML']} |"
        )
    lines.append("")
    lines.append("HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. "
                 "LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. "
                 "CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, "
                 "so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.")
    lines.append("")

    for key, diag in report.diagnostics.items():
        view, region = key.split("|")
        lines.append(f"## Diagnostics: view={view}, region={'ignored' if region == 'region' else 'none'}, match {diag.match_px:g} px")
        lines.append(
            f"- reference objects: {diag.reference_objects}; candidate ids: {diag.candidate_ids}; "
            f"matched pairs: {diag.matched_pairs}; unmatched reference entries: {diag.unmatched_reference}; "
            f"unmatched candidate entries: {diag.unmatched_candidate}"
        )
        lines.append(f"- identity switches: {len(diag.identity_switches)}; fragmentation (coverage interruptions): {diag.fragmentation}; "
                     f"orphan candidate ids (never on a reference object): {len(diag.orphan_candidate_ids)}")
        lines.append("")
        lines.append("### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)")
        if not diag.identity_switches:
            lines.append("- none")
        for switch in diag.identity_switches[:max_switches]:
            lines.append(
                f"- f{switch.frame}: ref {switch.reference_id}: {switch.previous_candidate_id} -> {switch.new_candidate_id} "
                f"at ({switch.position_xy[0]:g}, {switch.position_xy[1]:g}), {switch.frames_since_previous} frames after previous cover"
            )
        if len(diag.identity_switches) > max_switches:
            lines.append(f"- ... {len(diag.identity_switches) - max_switches} more in the JSON report")
        lines.append("")
        lines.append("### Candidate ids per reference object (fragmentation)")
        lines.append("| reference id | frames | covered | fragments | candidate ids (frames) |")
        lines.append("|---|---|---|---|---|")
        for item in diag.coverage:
            ids = ", ".join(f"{k} ({v})" for k, v in list(item.candidate_ids.items())[:12])
            more = f", +{len(item.candidate_ids) - 12} more" if len(item.candidate_ids) > 12 else ""
            lines.append(f"| {item.reference_id} | {item.frames} ({item.first_frame}..{item.last_frame}) | {item.covered} | {item.fragments} | {ids}{more} |")
        lines.append("")
        lines.append("### Orphan candidate ids")
        orphans = [d for d in diag.durations if not d.covered_reference_ids]
        if not orphans:
            lines.append("- none")
        else:
            lines.append("| id | frames | lifespan | rows on a reference object | rows on none |")
            lines.append("|---|---|---|---|---|")
            for d in orphans[:40]:
                lines.append(f"| {d.track_id} | {d.first_frame}..{d.last_frame} | {d.lifespan} | {d.matched_rows} | {d.coasting_rows} |")
            if len(orphans) > 40:
                lines.append(f"| ... | {len(orphans) - 40} more | | | |")
        lines.append("")
        lines.append("### Gaps and durations of candidate tracks")
        durations = diag.durations
        if durations:
            lifespans = sorted(d.lifespan for d in durations)
            lines.append(
                f"- tracks: {len(durations)}; lifespan min/median/max: {lifespans[0]}/{lifespans[len(lifespans) // 2]}/{lifespans[-1]}; "
                f"tracks with internal gaps: {sum(1 for d in durations if d.internal_gaps)}; "
                f"total internal gaps: {sum(d.internal_gaps for d in durations)}; longest internal gap: {max(d.longest_internal_gap for d in durations)}; "
                f"tracks ending in coasting: {sum(1 for d in durations if d.trailing_coasting)} (trailing rows total {sum(d.trailing_coasting for d in durations)})"
            )
            lines.append("| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |")
            lines.append("|---|---|---|---|---|---|---|---|---|---|")
            for d in durations[:80]:
                lines.append(
                    f"| {d.track_id} | {d.first_frame}..{d.last_frame} | {d.lifespan} | {d.rows} | {d.matched_rows} | {d.coasting_rows} | "
                    f"{d.internal_gaps} | {d.longest_internal_gap} | {d.trailing_coasting} | {', '.join(d.covered_reference_ids) or '-'} |"
                )
            if len(durations) > 80:
                lines.append(f"| ... | {len(durations) - 80} more in JSON | | | | | | | | |")
        else:
            lines.append("- no candidate tracks")
        lines.append("")
    return "\n".join(lines)


def summary_table(report: EvaluationReport, fields: Sequence[str] = ("HOTA", "DetA", "AssA", "MOTA", "IDF1", "IDSW", "Frag")) -> list[dict]:
    """Compact rows for cross-run tables."""
    return [
        {"view": row.view, "region": row.ignore_region, "px": row.match_px, **{f: row.metrics[f] for f in fields}}
        for row in report.rows
    ]
