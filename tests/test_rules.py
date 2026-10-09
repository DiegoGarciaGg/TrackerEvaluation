"""Rules that are not obvious from the code, each on the smallest input that exhibits it."""

from evaluation.diagnostics import diagnose
from evaluation.evaluate import evaluate
from evaluation.views import observations_view
from tests.helpers import merge, run_from_centers, straight_line


def _switches(candidate, reference, px=5.0):
    return diagnose(observations_view(reference), observations_view(candidate), px)


def test_relabelling_one_object_midway_is_one_switch():
    reference = run_from_centers(straight_line("x", range(4), 10, 50, 10, 0))
    candidate = run_from_centers({0: [("a", 10, 50)], 1: [("a", 20, 50)], 2: [("b", 30, 50)], 3: [("b", 40, 50)]})
    diag = _switches(candidate, reference)
    assert len(diag.identity_switches) == 1
    assert diag.identity_switches[0].frame == 2 and diag.identity_switches[0].previous_candidate_id == "a"
    assert evaluate(candidate, reference, match_px=(5.0,)).rows[0].metrics["IDSW"] == 1


def test_mutual_swap_counts_two_switches():
    reference = run_from_centers(merge(straight_line("p", range(6), 0, 0, 10, 0), straight_line("q", range(6), 0, 100, 10, 0)))
    centers = {}
    for frame in range(6):
        a, b = ("a", "b") if frame < 3 else ("b", "a")
        centers[frame] = [(a, 10 * frame, 0), (b, 10 * frame, 100)]
    candidate = run_from_centers(centers)
    diag = _switches(candidate, reference)
    assert len(diag.identity_switches) == 2
    assert {s.frame for s in diag.identity_switches} == {3}
    assert evaluate(candidate, reference, match_px=(5.0,)).rows[0].metrics["IDSW"] == 2


def test_losing_and_recovering_with_the_same_id_is_not_a_switch_but_is_a_fragment():
    # A second, always-covered object keeps every frame non-empty on the candidate side: TrackEval's
    # CLEAR skips a frame with no candidate at all before updating its "previously tracked" memory,
    # so without it the interruption would not register as a Frag there (our diagnostics do count it).
    reference = run_from_centers(merge(straight_line("x", range(6), 0, 0, 10, 0), straight_line("y", range(6), 0, 500, 10, 0)))
    centers = straight_line("a", range(6), 0, 0, 10, 0)
    del centers[2]
    del centers[3]
    candidate = run_from_centers(merge(centers, straight_line("b", range(6), 0, 500, 10, 0)))
    diag = _switches(candidate, reference)
    assert diag.identity_switches == []
    assert diag.fragmentation == 1
    metrics = evaluate(candidate, reference, match_px=(5.0,)).rows[0].metrics
    assert metrics["IDSW"] == 0 and metrics["Frag"] == 1


def test_trackeval_frag_ignores_interruptions_in_candidate_empty_frames_but_diagnostics_do_not():
    reference = run_from_centers(straight_line("x", range(6), 0, 0, 10, 0))
    centers = straight_line("a", range(6), 0, 0, 10, 0)
    del centers[2]
    del centers[3]
    candidate = run_from_centers(centers)
    assert _switches(candidate, reference).fragmentation == 1
    assert evaluate(candidate, reference, match_px=(5.0,)).rows[0].metrics["Frag"] == 0


def test_recovering_under_a_new_id_is_a_switch_even_across_a_gap():
    reference = run_from_centers(straight_line("x", range(6), 0, 0, 10, 0))
    centers = {0: [("a", 0, 0)], 1: [("a", 10, 0)], 4: [("b", 40, 0)], 5: [("b", 50, 0)]}
    candidate = run_from_centers(centers)
    diag = _switches(candidate, reference)
    assert len(diag.identity_switches) == 1 and diag.identity_switches[0].frames_since_previous == 3


def test_orphan_ids_and_ids_per_object():
    reference = run_from_centers(straight_line("x", range(4), 0, 0, 10, 0))
    candidate = run_from_centers(merge(straight_line("a", range(4), 0, 0, 10, 0), straight_line("z", range(4), 500, 500, 0, 0)))
    diag = _switches(candidate, reference)
    assert diag.orphan_candidate_ids == ["z"]
    assert diag.coverage[0].candidate_ids == {"a": 4}
    assert diag.candidate_ids == 2 and diag.reference_objects == 1
