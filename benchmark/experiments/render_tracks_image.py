"""Draw a run's complete tracks on one frame of the clip: a still image to compare trackers.

    python experiments/render_tracks_image.py --video <clip.mp4> --tracks <run>/tracks.csv --out <run>/tracks.png \
        [--gt ground_truth/<clip>_reference_tracks_corrected.csv] [--frame last] [--scale 0.5]

Every track is a polyline through its box centers in the track's own colour (the same colour
the video uses), with the id written at its last point; ground-truth trajectories are thin
green lines. Drawn over one frame of the clip (the last one by default), so a whole run is
readable at a glance: fragments show as colour changes along one path, orphan tracks as lines
on nothing, missed birds as green lines without a coloured companion.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import paths  # noqa: E402,F401

from experiments.render_video import GT_COLOR, load_tracks, track_color  # noqa: E402


def track_polylines(rows_by_frame: dict) -> dict:
    """Ordered center points per track id: ``{id: [(frame, cx, cy), ...]}``."""
    paths: dict = {}
    for frame in sorted(rows_by_frame):
        for track_id, x, y, w, h, _matched in rows_by_frame[frame]:
            paths.setdefault(track_id, []).append((frame, x + w / 2, y + h / 2))
    return paths


def gt_polylines(gt_path: Path) -> dict:
    import csv

    paths: dict = {}
    with gt_path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            x1, y1, x2, y2 = (float(row[k]) for k in ("x1", "y1", "x2", "y2"))
            paths.setdefault(row["obj_id"], []).append((int(float(row["frame_number"])), (x1 + x2) / 2, (y1 + y2) / 2))
    return {k: sorted(v) for k, v in paths.items()}


def render_image(video: Path, tracks_path: Path, out: Path, gt_path: Path | None, frame: str | int = "last", scale: float = 0.5, label: str = "") -> dict:
    capture = cv2.VideoCapture(str(video))
    if not capture.isOpened():
        raise RuntimeError(f"could not open {video}")
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    index = frame_count - 1 if frame == "last" else int(frame)
    capture.set(cv2.CAP_PROP_POS_FRAMES, index)
    ok, image = capture.read()
    capture.release()
    if not ok:
        raise RuntimeError(f"could not read frame {index} of {video}")

    if gt_path:
        for points in gt_polylines(gt_path).values():
            pts = np.array([[x, y] for _, x, y in points], dtype=np.int32)
            cv2.polylines(image, [pts], False, GT_COLOR, 3)
    paths = track_polylines(load_tracks(tracks_path))
    for track_id, points in paths.items():
        pts = np.array([[x, y] for _, x, y in points], dtype=np.int32)
        color = track_color(track_id)
        cv2.polylines(image, [pts], False, color, 4)
        cv2.circle(image, tuple(pts[-1]), 8, color, -1)
        cv2.putText(image, str(track_id), (int(pts[-1][0]) + 10, int(pts[-1][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    title = f"{label or tracks_path.parent.name}: {len(paths)} track ids" + (f", ground truth in green" if gt_path else "")
    # below the burnt-in timestamp some clips carry in the top-left corner
    cv2.putText(image, title, (16, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (255, 255, 255), 6)
    cv2.putText(image, title, (16, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (20, 20, 20), 2)
    small = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    out.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out), small)
    return {"out": str(out), "frame": index, "track_ids": len(paths)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--video", type=Path, required=True)
    parser.add_argument("--tracks", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--gt", type=Path, default=None)
    parser.add_argument("--frame", default="last", help="frame index to draw on, or 'last'")
    parser.add_argument("--scale", type=float, default=0.5)
    parser.add_argument("--label", default="")
    args = parser.parse_args()
    info = render_image(args.video, args.tracks, args.out, args.gt, args.frame, args.scale, args.label)
    print(f"wrote {info['out']} (frame {info['frame']}, {info['track_ids']} track ids)")


if __name__ == "__main__":
    main()
