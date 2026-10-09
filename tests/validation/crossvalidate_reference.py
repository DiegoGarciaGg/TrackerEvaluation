"""Cross-validation against ``spoorpredictioneval.track_quality.evaluate_track_quality``.

Not part of ``evaluation/``: this script imports the reference library from
``tracker-kit-Changing/tracker-eval-reference`` only to compare numbers. For each case it builds
the reference library's ``RunResult`` objects from our views (same frames, boxes and ids), runs
``evaluate_track_quality`` in ``center_distance`` mode at the same pixel threshold, and compares
its IDF1, identity switches and fragmentation with ours (TrackEval Identity for IDF1, our
diagnostics for switches and fragmentation).

Expected differences, and how each is explained in the report:

- The reference associates per frame greedily (nearest pair first); we use the Hungarian
  assignment with CLEAR's continuation bonus. Where the two choose different pairs, switches and
  coverage differ; the report lists every switch present on one side only, with its frame.
- The reference IDF1 is computed from its per-frame one-to-one matches. TrackEval's IDF1 counts
  as potential matches EVERY (reference, candidate) pair within threshold in a frame, not one per
  object, then solves one global assignment. With two candidates within threshold of one object
  (or two objects within threshold of one candidate, common in the flock) the two IDF1 values
  legitimately differ; the report counts the frames where such ambiguity exists.
"""

from __future__ import annotations

import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parents[2]
REFERENCE_ROOT = Path("/Users/diegogarciagonzalez/tracker-kit-Changing/tracker-eval-reference")
for path in (KIT_ROOT, REFERENCE_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import numpy as np  # noqa: E402

import spoorpredictioneval.contracts as ref_contracts  # noqa: E402
from spoorpredictioneval.track_quality import ASSOCIATION_CENTER_DISTANCE, evaluate_track_quality  # noqa: E402

from evaluation.diagnostics import diagnose  # noqa: E402
from evaluation.similarity import center_distance_matrix  # noqa: E402
from evaluation.trackeval_bridge import build_sequence, center_distance_similarity, run_metrics  # noqa: E402
from evaluation.views import FLOCK_TIMESTAMP_OVERLAY, FrameView, apply_region, observations_view, restrict_frames, view_of  # noqa: E402


def to_reference_run(view: FrameView) -> ref_contracts.RunResult:
    correctness = {}
    for frame, entries in view.items():
        correctness[frame] = [
            ref_contracts.Detection(
                box_xywh=entry.box if entry.box is not None else (entry.center[0] - 0.5, entry.center[1] - 0.5, 1.0, 1.0),
                confidence=1.0,
                track_id=entry.track_id,
                class_name="bird",
            )
            for entry in entries
        ]
    return ref_contracts.RunResult(correctness=correctness, performance={}, provenance=ref_contracts.Provenance("x", "none", "x"), tracks=())


def reference_switch_set(reference: FrameView, candidate: FrameView, px: float) -> set[tuple[int, str]]:
    """Re-derive the reference's switch list (frame, reference id) with its own greedy matching."""
    from spoorpredictioneval.track_quality import _associate

    trajectories = _associate(to_reference_run(candidate), to_reference_run(reference), ASSOCIATION_CENTER_DISTANCE, px)
    switches = set()
    for reference_id, frames in trajectories.items():
        last = None
        for frame in frames:
            if frame.candidate_id is None:
                continue
            if last is not None and frame.candidate_id != last:
                switches.add((frame.frame_number, reference_id))
            last = frame.candidate_id
    return switches


def ambiguous_frames(reference: FrameView, candidate: FrameView, px: float) -> tuple[int, int]:
    """Frames where some object has more than one candidate within px, or vice versa."""
    multi_candidate = multi_object = 0
    for frame in set(reference) & set(candidate):
        d = center_distance_matrix([e.center for e in reference[frame]], [e.center for e in candidate[frame]])
        within = d <= px
        if (within.sum(axis=1) > 1).any():
            multi_candidate += 1
        if (within.sum(axis=0) > 1).any():
            multi_object += 1
    return multi_candidate, multi_object


def crossvalidate(label: str, reference: FrameView, candidate: FrameView, px: float, num_timesteps: int) -> dict:
    ref_report = evaluate_track_quality(to_reference_run(candidate), to_reference_run(reference), association=ASSOCIATION_CENTER_DISTANCE, threshold=px)
    sequence = build_sequence(reference, candidate, center_distance_similarity(px), num_timesteps)
    ours_metrics = run_metrics(sequence)
    diag = diagnose(reference, candidate, px)
    ours_switches = {(s.frame, s.reference_id) for s in diag.identity_switches}
    theirs_switches = reference_switch_set(reference, candidate, px)
    multi_candidate, multi_object = ambiguous_frames(reference, candidate, px)
    return {
        "label": label,
        "px": px,
        "idf1_reference": ref_report.idf1,
        "idf1_ours": ours_metrics["IDF1"],
        "switches_reference": ref_report.identity_switches,
        "switches_ours": len(diag.identity_switches),
        "switches_only_reference": sorted(theirs_switches - ours_switches),
        "switches_only_ours": sorted(ours_switches - theirs_switches),
        "fragmentation_reference": ref_report.fragmentation,
        "fragmentation_ours": diag.fragmentation,
        "idtp_reference": ref_report.id_true_positives,
        "idtp_ours": ours_metrics["IDTP"],
        "frames_with_two_candidates_near_one_object": multi_candidate,
        "frames_with_two_objects_near_one_candidate": multi_object,
    }


def main() -> int:
    from evaluation.adapters import load_tracker_run
    from evaluation.store import JsonlResultStore

    store = JsonlResultStore(KIT_ROOT / "outputs/store")
    gt_flock = observations_view(store.resolve("flock|20251012_164031_1DAC|gt"))
    gt_turbine = restrict_frames(observations_view(store.resolve("turbine|20250920_063942_6C42|gt")), (53, 293))
    cases = []
    e3 = KIT_ROOT / "outputs/runs/flock/gt_default/tracks.csv"
    if e3.exists():
        cases.append(("flock E3 gt-as-detections, matched rows", gt_flock, view_of(load_tracker_run(e3, "20251012_164031_1DAC", detection_source="gt"), "observations"), 1009))
    real = KIT_ROOT / "outputs/runs/flock/real_default/tracks.csv"
    if real.exists():
        run = load_tracker_run(real, "20251012_164031_1DAC", detection_source="real")
        cases.append(("flock real_default, matched rows, overlay ignored", apply_region(gt_flock, FLOCK_TIMESTAMP_OVERLAY), apply_region(view_of(run, "observations"), FLOCK_TIMESTAMP_OVERLAY), 1009))
    cases.append(("flock baseline (6 col), all rows, overlay ignored", apply_region(gt_flock, FLOCK_TIMESTAMP_OVERLAY), apply_region(view_of(store.resolve("flock|20251012_164031_1DAC|kit:baseline"), "updates"), FLOCK_TIMESTAMP_OVERLAY), 1009))
    cases.append(("turbine baseline, all rows, frames 53..293", gt_turbine, restrict_frames(view_of(store.resolve("turbine|20250920_063942_6C42|kit:baseline"), "updates"), (53, 293)), 671))

    lines = ["# Cross-validation against spoorpredictioneval.evaluate_track_quality (center_distance)", "",
             "| case | px | IDF1 ref | IDF1 ours | IDTP ref/ours | switches ref/ours | only ref | only ours | frag ref/ours | frames with 2 cand near 1 obj | frames with 2 obj near 1 cand |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    details = []
    for label, reference, candidate, num_timesteps in cases:
        for px in (4.0, 8.0):
            r = crossvalidate(label, reference, candidate, px, num_timesteps)
            lines.append(
                f"| {r['label']} | {px:g} | {r['idf1_reference']:.4f} | {r['idf1_ours']:.4f} | {r['idtp_reference']}/{r['idtp_ours']} | "
                f"{r['switches_reference']}/{r['switches_ours']} | {len(r['switches_only_reference'])} | {len(r['switches_only_ours'])} | "
                f"{r['fragmentation_reference']}/{r['fragmentation_ours']} | {r['frames_with_two_candidates_near_one_object']} | {r['frames_with_two_objects_near_one_candidate']} |"
            )
            if r["switches_only_reference"] or r["switches_only_ours"]:
                details.append(f"- {label} at {px:g} px: switches only in the reference (greedy): {r['switches_only_reference'][:15]}{' ...' if len(r['switches_only_reference']) > 15 else ''}; only in ours (Hungarian + continuation): {r['switches_only_ours'][:15]}{' ...' if len(r['switches_only_ours']) > 15 else ''}")
    lines += ["", "## Explanation of differences", "",
              "- IDF1: the reference computes IDTP from its per-frame greedy one-to-one matches; TrackEval's Identity counts every pair within threshold as a potential match and solves one global assignment, so IDTP (and IDF1) can only be equal or higher on our side, and differs exactly when a frame has two candidates near one object or two objects near one candidate (last two columns).",
              "- Identity switches: both count a change of the remembered candidate id per reference object across gaps. They differ only where the per-frame association differs: greedy nearest-first versus Hungarian with CLEAR's preference for the id that covered the object in the previous frame. The lists below give each such switch by (frame, reference id).",
              "- Fragmentation: both count coverage interruptions that resume; differences come from the same association differences.", ""]
    lines += details
    text = "\n".join(lines) + "\n"
    out = KIT_ROOT / "outputs/phase4/crossvalidation_reference.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
