"""Pure functions at their boundaries."""

import math

import numpy as np
import pytest

from evaluation.similarity import (
    center_distance_matrix,
    distance_similarity,
    iou_matrix,
    match_px_for_alpha,
    scale_for_match_px,
)


def test_scale_doubles_match_px_at_threshold_half():
    assert scale_for_match_px(8.0) == 16.0
    assert scale_for_match_px(4.0, threshold=0.5) == 8.0
    assert scale_for_match_px(8.0, threshold=0.75) == 32.0


def test_scale_rejects_bad_inputs():
    with pytest.raises(ValueError):
        scale_for_match_px(0.0)
    with pytest.raises(ValueError):
        scale_for_match_px(8.0, threshold=1.0)


def test_distance_similarity_is_one_at_zero_half_at_match_and_zero_beyond_scale():
    scale = 16.0
    assert distance_similarity(np.array([0.0]), scale)[0] == 1.0
    assert distance_similarity(np.array([8.0]), scale)[0] == 0.5
    assert distance_similarity(np.array([16.0]), scale)[0] == 0.0
    assert distance_similarity(np.array([100.0]), scale)[0] == 0.0


def test_alpha_half_is_the_configured_distance():
    assert match_px_for_alpha(16.0, 0.5) == 8.0
    assert math.isclose(match_px_for_alpha(16.0, 0.95), 0.8)


def test_center_distance_matrix_shapes_and_values():
    d = center_distance_matrix([(0, 0), (3, 4)], [(0, 0)])
    assert d.shape == (2, 1)
    assert d[0, 0] == 0.0 and d[1, 0] == 5.0
    assert center_distance_matrix([], [(1, 1)]).shape == (0, 1)


def test_iou_identical_disjoint_and_half_overlap():
    a = (10.0, 10.0, 20.0, 20.0)
    assert iou_matrix([a], [a])[0, 0] == 1.0
    assert iou_matrix([(0, 0, 10, 10)], [(100, 100, 10, 10)])[0, 0] == 0.0
    assert math.isclose(iou_matrix([(0, 0, 10, 10)], [(5, 0, 10, 10)])[0, 0], 50 / 150)
