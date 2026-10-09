"""The similarity matches exactly at the configured distance and not a hair beyond."""

import numpy as np

from evaluation.evaluate import evaluate
from evaluation.trackeval_bridge import build_sequence, center_distance_similarity, run_metrics
from evaluation.views import observations_view
from tests.helpers import run_from_centers, straight_line


def _offset_run(px_offset: float, frames: int = 10):
    reference = run_from_centers(straight_line("x", range(frames), 100, 100, 3, 0))
    candidate = run_from_centers(straight_line("a", range(frames), 100 + px_offset, 100, 3, 0))
    return candidate, reference


def test_offset_equal_to_match_px_is_matched():
    candidate, reference = _offset_run(8.0)
    metrics = evaluate(candidate, reference, match_px=(8.0,)).rows[0].metrics
    assert metrics["CLR_TP"] == 10 and metrics["CLR_FP"] == 0 and metrics["IDF1"] == 1.0
    assert abs(metrics["MOTP_px"] - 8.0) < 1e-6


def test_offset_just_beyond_match_px_is_not_matched():
    candidate, reference = _offset_run(8.01)
    metrics = evaluate(candidate, reference, match_px=(8.0,)).rows[0].metrics
    assert metrics["CLR_TP"] == 0 and metrics["CLR_FP"] == 10 and metrics["CLR_FN"] == 10
    assert metrics["IDF1"] == 0.0
    assert evaluate(candidate, reference, match_px=(12.0,)).rows[0].metrics["CLR_TP"] == 10


def test_diagonal_offset_uses_euclidean_distance():
    reference = run_from_centers(straight_line("x", range(5), 0, 0, 0, 0))
    candidate = run_from_centers(straight_line("a", range(5), 3, 4, 0, 0))  # distance 5
    assert evaluate(candidate, reference, match_px=(5.0,)).rows[0].metrics["CLR_TP"] == 5
    assert evaluate(candidate, reference, match_px=(4.9,)).rows[0].metrics["CLR_TP"] == 0


def test_hota_at_alpha_half_equals_configured_distance():
    candidate, reference = _offset_run(8.0)
    sequence = build_sequence(observations_view(reference), observations_view(candidate), center_distance_similarity(8.0))
    sims = np.array([s[0, 0] for s in sequence.data["similarity_scores"]])
    assert np.allclose(sims, 0.5)
    metrics = run_metrics(sequence, scale_px=16.0)
    assert metrics["HOTA_TP_a50"] == 10
    assert metrics["DetA_a50"] == 1.0
