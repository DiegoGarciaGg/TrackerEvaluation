"""Render the visual outputs of every default run: tracked.mp4 and tracks.png next to tracks.csv.

    python benchmark/experiments/render_all.py [--images-only] [--videos-only] [--force]

Uses clips.json for the video and ground-truth paths; skips files that already exist.
``tracks.png`` is the whole run drawn as trajectories on the clip's last frame (cheap, one per
run); ``tracked.mp4`` is the frame-by-frame video (about a minute per run).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from paths import RUNS  # noqa: E402

from evaluation.clips import load_clips  # noqa: E402
from experiments.render_tracks_image import render_image  # noqa: E402
from experiments.render_video import render  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--images-only", action="store_true")
    parser.add_argument("--videos-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    for clip_name, clip in load_clips().items():
        for run in sorted((RUNS / clip_name).glob("*/*_default")):
            tracks = run / "tracks.csv"
            if not tracks.exists():
                continue
            if not args.videos_only and (args.force or not (run / "tracks.png").exists()):
                label = f"{run.parent.name} {run.name}"
                info = render_image(clip["video"], tracks, run / "tracks.png", clip["gt_tracks"], "last", 0.5, label)
                print(f"image  {clip_name}/{run.parent.name}/{run.name}: {info['track_ids']} track ids", flush=True)
            if not args.images_only and (args.force or not (run / "tracked.mp4").exists()):
                info = render(clip["video"], [tracks], [f"{run.parent.name} {run.name}"], run / "tracked.mp4", clip["gt_tracks"], 0.5)
                print(f"video  {clip_name}/{run.parent.name}/{run.name}: {info['frames']} frames", flush=True)


if __name__ == "__main__":
    main()
