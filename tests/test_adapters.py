"""Adapters preserve frames, ids and boxes (counts verified in Phase 0) and honour the coasting rule."""

import csv

import pytest

from evaluation.adapters import load_cloud_run, load_detections_run, load_gt_run, load_tracker_csv, load_tracker_run
from evaluation.adapters.tracker_csv import FORMAT_BASELINE, FORMAT_EXTENDED, detect_format
from evaluation.views import available_views, view_of


def test_flock_gt_counts(kit_root):
    run = load_gt_run(
        kit_root / "ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv",
        "20251012_164031_1DAC",
        detections_csv=kit_root / "ground_truth/20251012_164031_1DAC_detections_corrected.csv",
    )
    assert run.observation_count == 10142
    assert len(run.tracks) == 25
    assert sorted(run.correctness)[0] == 0 and sorted(run.correctness)[-1] == 1008
    assert len(run.correctness) == 1009
    first = run.correctness[0][0]
    assert first.box_xywh == (1857.0, 3450.0, 17.0, 19.0) and first.track_id == "78911" and first.confidence == 1.0
    assert run.provenance.extra["predictor"] == "gt" and run.provenance.extra["claim"] == "accuracy"
    assert "manual annotation" in run.provenance.extra["curation"]
    assert run.provenance.extra["facts"]["identical_box_shared_by_two_identities"][0]["frame"] == 517


def test_turbine_gt_counts(kit_root):
    run = load_gt_run(kit_root / "ground_truth/20250920_063942_6C42_reference_tracks_corrected.csv", "20250920_063942_6C42")
    assert run.observation_count == 241 and len(run.tracks) == 1
    assert run.tracks[0].first_frame == 53 and run.tracks[0].last_frame == 293


def test_cloud_and_detector_counts(kit_root):
    cloud = load_cloud_run(kit_root / "data/20251012_164031_1DAC_cloud_reference_tracks.csv", "20251012_164031_1DAC")
    assert cloud.observation_count == 3542 and len(cloud.tracks) == 17
    assert cloud.provenance.extra["claim"] == "parity"
    det = load_detections_run(kit_root / "data/20251012_164031_1DAC_detections.csv", "20251012_164031_1DAC")
    assert det.observation_count == 4424 and det.tracks == ()
    assert all(d.track_id is None for ds in det.correctness.values() for d in ds)


def test_baseline_six_column_format_marks_coasting_unknown(kit_root):
    path = kit_root / "results/flock/baseline_tracks.csv"
    assert detect_format(path) == FORMAT_BASELINE
    run = load_tracker_run(path, "20251012_164031_1DAC")
    assert run.observation_count == 7571 and run.update_count == 7571 and len(run.tracks) == 78
    assert run.provenance.extra["coasting_known"] is False
    assert available_views(run) == ["updates"]
    with pytest.raises(ValueError):
        view_of(run, "observations")


def test_extended_format_coasting_rows_are_never_detections(kit_root):
    path = kit_root / "outputs/runs/flock/real_default/tracks.csv"
    if not path.exists():
        pytest.skip("run outputs/runs/flock/real_default first")
    assert detect_format(path) == FORMAT_EXTENDED
    correctness, tracks, facts = load_tracker_csv(path)
    assert facts["coasting_known"] is True
    assert facts["rows"] == 7571 and facts["matched_rows"] == 4173 and facts["coasting_rows"] == 3398
    assert sum(len(d) for d in correctness.values()) == 4173
    assert sum(len(t.updates) for t in tracks) == 7571
    for track in tracks:
        for update in track.updates:
            if update.missed_frame_count > 0:
                assert update.confidence == 0.0
                assert all(d.track_id != track.track_id for d in correctness.get(update.frame_number, []))
            else:
                assert update.confidence == 1.0


def test_extended_format_synthetic_coasting_row(tmp_path):
    path = tmp_path / "t.csv"
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["frame_number", "track_id", "x", "y", "w", "h", "matched", "detection_count", "missed_frame_count", "age_frames"])
        writer.writerow([5, 7, 10.0, 20.0, 4.0, 4.0, 1, 3, 0, 3])
        writer.writerow([6, 7, 10.0, 20.0, 4.0, 4.0, 0, 3, 1, 4])
        writer.writerow([7, 7, 12.0, 20.0, 4.0, 4.0, 1, 4, 0, 5])
    correctness, tracks, facts = load_tracker_csv(path)
    assert sorted(correctness) == [5, 7]
    assert 6 not in correctness
    assert [u.confidence for u in tracks[0].updates] == [1.0, 0.0, 1.0]
    assert [u.missed_frame_count for u in tracks[0].updates] == [0, 1, 0]
    assert tracks[0].updates[1].box_xywh == (10.0, 20.0, 4.0, 4.0)
    assert tracks[0].observation_count == 4


def test_extended_format_rejects_inconsistent_rows(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("frame_number,track_id,x,y,w,h,matched,detection_count,missed_frame_count,age_frames\r\n5,7,1,1,2,2,1,3,2,3\r\n")
    with pytest.raises(ValueError):
        load_tracker_csv(path)
