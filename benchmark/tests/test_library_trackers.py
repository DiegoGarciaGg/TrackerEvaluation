"""Roboflow Trackers adapter: same input boxes in, extended rows out, matched only."""

import pytest

pytest.importorskip("trackers")

from experiments.library_trackers import library_track_rows, make_tracker  # noqa: E402
from experiments.run_experiment import run_experiment  # noqa: E402
from tracker.shim import BoundingBoxXYWH  # noqa: E402


def _two_birds(frames: int = 20):
    """Two boxes moving apart, 30 px each so IoU-based association can follow them."""
    by_frame = {}
    for f in range(frames):
        by_frame[f] = [BoundingBoxXYWH(100 + 3 * f, 100, 30, 30), BoundingBoxXYWH(400 - 3 * f, 300, 30, 30)]
    return by_frame


@pytest.mark.parametrize("algorithm", ["sort", "bytetrack", "ocsort", "botsort", "cbiou"])
def test_rows_are_input_boxes_with_stable_ids(algorithm):
    rows, params = library_track_rows(algorithm, _two_birds(), 20, 25.0)
    assert rows, algorithm
    assert all(r["matched"] == 1 and r["missed_frame_count"] == 0 for r in rows)
    ids = {r["track_id"] for r in rows}
    assert len(ids) == 2, (algorithm, ids)
    for r in rows:  # every row is one of the input boxes of its frame
        assert (r["x"], r["y"], r["w"], r["h"]) in {(b.x, b.y, b.width, b.height) for b in _two_birds()[r["frame_number"]]}
    assert params["frame_rate"] == 25.0


def test_make_tracker_rejects_unknown_name():
    with pytest.raises(ValueError):
        make_tracker("deepsort", 25.0)


def test_runner_writes_manifest_with_algorithm(kit_root, bench_root, repo_root, tmp_path):
    video = kit_root / "data/synthetic/synthetic.mp4"
    if not video.exists():
        pytest.skip("synthetic clip not present")
    manifest = run_experiment(video_path=video, detections_path=kit_root / "data/synthetic/synthetic_detections.csv",
                              out_path=tmp_path / "tracks.csv", algorithm="sort")
    assert manifest["tracker"]["algorithm"] == "sort" and manifest["tracker"]["library"].startswith("roboflow trackers")
    assert manifest["output"]["coasting_rows"] == 0
    assert manifest["output"]["columns"][-4:] == ["matched", "detection_count", "missed_frame_count", "age_frames"]
