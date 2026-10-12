"""The clip registry: ``benchmark/clips.json``, one entry per evaluation video.

Every path is relative to the repository root (``tracker_kit/...``, ``benchmark/...``). ``detections`` and ``cloud`` are null for a clip that
has no detector output or cloud export (then only ground-truth boxes can be fed to the
trackers). ``gt_frames`` restricts accuracy scoring to the labelled frame range when the labels
do not cover the whole clip. Adding a clip = adding an entry here and its files.
"""

from __future__ import annotations

import json
from pathlib import Path

from evaluation.views import IgnoreRegion

BENCH_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = BENCH_ROOT.parent


def load_clips(root: Path = REPO_ROOT) -> dict[str, dict]:
    clips = json.loads((root / "benchmark" / "clips.json").read_text())
    for name, clip in clips.items():
        clip["name"] = name
        for key in ("video", "detections", "cloud", "gt_tracks", "gt_detections"):
            clip[key] = (root / clip[key]) if clip.get(key) else None
        clip["region"] = IgnoreRegion(rects=tuple(tuple(r) for r in clip.get("ignore_rects", [])), label=clip.get("ignore_label", "")) if clip.get("ignore_rects") else None
        clip["frames"] = tuple(clip["gt_frames"]) if clip.get("gt_frames") else None
    return clips


def clip_of_video_id(video_id: str, root: Path = REPO_ROOT) -> dict | None:
    return next((clip for clip in load_clips(root).values() if clip["video_id"] == video_id), None)
