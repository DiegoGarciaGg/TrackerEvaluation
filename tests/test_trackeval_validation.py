"""With IoU similarity, our bridge equals TrackEval's standard MOTChallenge pipeline."""

import pytest

from tests.validation.validate_trackeval_iou import compare


def test_turbine_baseline_matches_standard_pipeline(turbine_gt, turbine_baseline):
    standard, mine, mismatches = compare(turbine_gt, turbine_baseline, "updates", "20250920_063942_6C42", 671)
    assert mismatches == []
    assert standard["HOTA"] == pytest.approx(mine["HOTA"]) and standard["MOTA"] == pytest.approx(mine["MOTA"]) and standard["IDF1"] == pytest.approx(mine["IDF1"])


def test_flock_cloud_matches_standard_pipeline(store, flock_gt):
    cloud = store.resolve("flock|20251012_164031_1DAC|baseline:cloud")
    _, _, mismatches = compare(flock_gt, cloud, "observations", "20251012_164031_1DAC", 1009)
    assert mismatches == []


def test_flock_baseline_matches_standard_pipeline(store, flock_gt):
    baseline = store.resolve("flock|20251012_164031_1DAC|kit:baseline")
    _, _, mismatches = compare(flock_gt, baseline, "updates", "20251012_164031_1DAC", 1009)
    assert mismatches == []
