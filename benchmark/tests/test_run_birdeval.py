"""The bridge to the team's evaluator: run names map to experiments, rows map to birdeval row types."""

import csv

from evaluation.run_birdeval import configuration_of


def test_configuration_strips_the_detection_source_prefix():
    assert configuration_of("real_default") == "default"
    assert configuration_of("gt_default") == "default"
    assert configuration_of("real_maxage15_tent3") == "maxage15_tent3"
    assert configuration_of("gtdeg_drop0.10_noise1.0_fp0.5_seed1") == "gtdeg_drop0.10_noise1.0_fp0.5_seed1"


def test_exported_rows_keep_boxes_and_label_coasting_as_predicted(bench_root):
    ours = bench_root / "outputs/runs/flock/simplesort/real_default/tracks.csv"
    theirs = bench_root / "outputs/birdeval/runs_v2/yolo/simplesort__default/20251012_164031_1DAC_tracks.csv"
    if not ours.exists() or not theirs.exists():
        import pytest

        pytest.skip("run run_birdeval.py first")
    with ours.open(newline="") as a, theirs.open(newline="") as b:
        rows_a, rows_b = list(csv.DictReader(a)), list(csv.DictReader(b))
    assert len(rows_a) == len(rows_b) == 7571
    for ra, rb in zip(rows_a, rows_b):
        assert (ra["frame_number"], ra["track_id"], ra["x"], ra["y"], ra["w"], ra["h"]) == (rb["frame_number"], rb["track_id"], rb["x"], rb["y"], rb["w"], rb["h"])
        assert rb["row_type"] == ("matched" if ra["matched"] == "1" else "predicted")
        assert rb["track_confirmed"] == "True"
    assert sum(r["row_type"] == "predicted" for r in rows_b) == 3398
