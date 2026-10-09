"""Properties rather than values: a perfect candidate, and invariance to candidate id names."""

from evaluation.contracts import Detection, RunResult, Track
from evaluation.evaluate import evaluate
from tests.helpers import merge, run_from_centers, straight_line


def test_ground_truth_against_itself_is_perfect(flock_gt):
    report = evaluate(flock_gt, flock_gt, match_px=(8.0,))
    metrics = report.rows[0].metrics
    assert metrics["HOTA"] == 1.0 and metrics["IDF1"] == 1.0 and metrics["MOTA"] == 1.0
    assert metrics["IDSW"] == 0 and metrics["CLR_FP"] == 0 and metrics["CLR_FN"] == 0
    diag = report.diagnostics["observations|noregion"]
    assert diag.identity_switches == [] and diag.fragmentation == 0 and diag.orphan_candidate_ids == []


def _rename(run: RunResult, mapping) -> RunResult:
    correctness = {
        frame: [Detection(d.box_xywh, d.confidence, mapping(d.track_id), d.class_name) for d in detections]
        for frame, detections in run.correctness.items()
    }
    tracks = tuple(Track(mapping(t.track_id), t.updates) for t in run.tracks)
    return RunResult(correctness, run.performance, run.provenance, tracks)


def test_renaming_candidate_ids_changes_no_metric(turbine_baseline, turbine_gt):
    renamed = _rename(turbine_baseline, lambda i: f"id-{int(i) * 7 + 1000}")
    before = evaluate(turbine_baseline, turbine_gt, match_px=(8.0,)).rows[0].metrics
    after = evaluate(renamed, turbine_gt, match_px=(8.0,)).rows[0].metrics
    for key, value in before.items():
        assert after[key] == value, key


def test_renaming_on_synthetic_swap_keeps_switch_count():
    reference = run_from_centers(merge(straight_line("p", range(6), 0, 0, 10, 0), straight_line("q", range(6), 0, 100, 10, 0)))
    centers = {f: [("a" if f < 3 else "b", 10 * f, 0), ("b" if f < 3 else "a", 10 * f, 100)] for f in range(6)}
    candidate = run_from_centers(centers)
    renamed = _rename(candidate, {"a": "9", "b": "3"}.get)
    m1 = evaluate(candidate, reference, match_px=(5.0,)).rows[0].metrics
    m2 = evaluate(renamed, reference, match_px=(5.0,)).rows[0].metrics
    assert m1 == m2 and m1["IDSW"] == 2
