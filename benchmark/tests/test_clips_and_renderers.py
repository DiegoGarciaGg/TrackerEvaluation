"""The clip registry points at existing files; the still-image renderer draws every track."""

import cv2
import pytest

from evaluation.clips import clip_of_video_id, load_clips
from experiments.render_tracks_image import render_image


def test_every_registered_clip_has_its_files(kit_root, bench_root, repo_root):
    clips = load_clips(repo_root)
    assert {"flock", "turbine", "semrev"} <= set(clips)
    for clip in clips.values():
        assert clip["video"].exists() and clip["gt_tracks"].exists() and clip["gt_detections"].exists(), clip["name"]
        for key in ("detections", "cloud"):
            assert clip[key] is None or clip[key].exists(), (clip["name"], key)
    assert clip_of_video_id("20251012_164031_1DAC", repo_root)["name"] == "flock"
    assert clip_of_video_id("nope", repo_root) is None


def test_track_image_is_written_at_half_size(kit_root, bench_root, repo_root, tmp_path):
    clip = load_clips(repo_root)["turbine"]
    tracks = bench_root / "outputs/runs/turbine/simplesort/real_default/tracks.csv"
    if not tracks.exists():
        pytest.skip("turbine real_default run not present")
    info = render_image(clip["video"], tracks, tmp_path / "tracks.png", clip["gt_tracks"], "last", 0.25, "test")
    image = cv2.imread(str(tmp_path / "tracks.png"))
    assert image.shape[:2] == (960, 540) and info["track_ids"] == 35
