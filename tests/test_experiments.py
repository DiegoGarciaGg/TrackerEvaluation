"""Experiment runner: degraded sources are deterministic and schema-true; the runner reproduces a frozen baseline."""

import csv

import pytest

from evaluation.hashing import sha256_file
from experiments.detection_sources import SCHEMA, write_degraded_gt
from experiments.run_experiment import run_experiment


def test_degraded_gt_is_deterministic_and_keeps_the_schema(kit_root, tmp_path):
    gt = kit_root / "ground_truth/20250920_063942_6C42_detections_corrected.csv"
    a = write_degraded_gt(gt, tmp_path / "a.csv", drop_rate=0.2, center_noise_px=2.0, false_positives_per_frame=0.3, seed=7, frame_count=671)
    b = write_degraded_gt(gt, tmp_path / "b.csv", drop_rate=0.2, center_noise_px=2.0, false_positives_per_frame=0.3, seed=7, frame_count=671)
    c = write_degraded_gt(gt, tmp_path / "c.csv", drop_rate=0.2, center_noise_px=2.0, false_positives_per_frame=0.3, seed=8, frame_count=671)
    assert sha256_file(tmp_path / "a.csv") == sha256_file(tmp_path / "b.csv")
    assert sha256_file(tmp_path / "a.csv") != sha256_file(tmp_path / "c.csv")
    assert a["effects"]["dropped"] + a["effects"]["kept"] == 241
    assert a["effects"]["spurious"] > 0
    with (tmp_path / "a.csv").open(newline="") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == SCHEMA
        rows = list(reader)
    for row in rows:
        assert int(row["area"]) == int(row["w"]) * int(row["h"])
        assert int(row["frame_timestamp"]) == round(int(row["frame_number"]) * 1000 / 25)
        assert int(row["w"]) > 0 and int(row["h"]) > 0


def test_no_degradation_reproduces_the_gt_boxes(kit_root, tmp_path):
    gt = kit_root / "ground_truth/20250920_063942_6C42_detections_corrected.csv"
    write_degraded_gt(gt, tmp_path / "same.csv", seed=1, frame_count=671)
    with gt.open(newline="") as a, (tmp_path / "same.csv").open(newline="") as b:
        rows_a = [(r["frame_number"], r["x"], r["y"], r["w"], r["h"]) for r in csv.DictReader(a)]
        rows_b = [(r["frame_number"], r["x"], r["y"], r["w"], r["h"]) for r in csv.DictReader(b)]
    assert sorted(rows_a) == sorted(rows_b)


def test_runner_reproduces_the_synthetic_baseline(kit_root, tmp_path):
    video = kit_root / "data/synthetic/synthetic.mp4"
    if not video.exists():
        pytest.skip("synthetic clip not present")
    manifest = run_experiment(
        video_path=video,
        detections_path=kit_root / "data/synthetic/synthetic_detections.csv",
        out_path=tmp_path / "tracks.csv",
        check_baseline=kit_root / "results/synthetic/baseline_tracks.csv",
    )
    assert manifest["baseline_check"]["identical_bytes"] is True
    assert manifest["output"]["columns"][-4:] == ["matched", "detection_count", "missed_frame_count", "age_frames"]
    assert manifest["tracker"]["source_hash"] and manifest["inputs"]["video"]["sha256"]
    reused = run_experiment(video_path=video, detections_path=kit_root / "data/synthetic/synthetic_detections.csv", out_path=tmp_path / "tracks.csv")
    assert reused["reused"] is True
