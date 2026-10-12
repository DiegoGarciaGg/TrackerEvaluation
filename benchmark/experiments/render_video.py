"""Render a tracking result over its clip as an H.264 mp4 for the dashboard's video viewer.

    python experiments/render_video.py --video data/20251012_164031_1DAC.mp4 \
        --tracks outputs/runs/flock/real_default/tracks.csv --out outputs/runs/flock/real_default/tracked.mp4 \
        [--gt ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv] [--scale 0.5]

    python experiments/render_video.py --video ... --tracks A/tracks.csv B/tracks.csv --labels "SimpleSORT" "SORT" \
        --out outputs/videos/flock/real_default__vs__sort_real_default.mp4      # side by side, frame-synchronous

Draws, per frame, every row of the tracks CSV as a box in the track's own colour with its id
(matched rows thick, coasting rows thin), the track's trail so far as a line in the same colour,
and the ground-truth boxes as thin green outlines when ``--gt`` is given. Birds are about nine pixels, so each box is padded to a
minimum visible size. Output is scaled (default 0.5: 1080x1920 for the 2160x3840 clips) and
encoded with OpenCV's ``avc1`` (H.264) writer, which browsers play. Two track files produce one
composite video with both results side by side, synchronised by construction.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

MIN_BOX_PX = 28  # minimum drawn box side at full resolution, so 9-px birds stay visible
GT_COLOR = (80, 200, 80)


def load_tracks(path: Path) -> dict[int, list[tuple[int, float, float, float, float, bool]]]:
    rows = defaultdict(list)
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            matched = row.get("matched", "1") == "1"
            rows[int(float(row["frame_number"]))].append(
                (int(float(row["track_id"])), float(row["x"]), float(row["y"]), float(row["w"]), float(row["h"]), matched)
            )
    return rows


def load_gt(path: Path) -> dict[int, list[tuple[float, float, float, float]]]:
    rows = defaultdict(list)
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            x1, y1, x2, y2 = (float(row[k]) for k in ("x1", "y1", "x2", "y2"))
            rows[int(float(row["frame_number"]))].append((x1, y1, x2 - x1, y2 - y1))
    return rows


def track_color(track_id: int) -> tuple[int, int, int]:
    digest = hashlib.sha1(str(track_id).encode()).digest()
    # keep colours saturated and bright enough to read on sky and sea
    return int(60 + digest[0] % 196), int(60 + digest[1] % 196), int(60 + digest[2] % 196)


def padded(x: float, y: float, w: float, h: float) -> tuple[int, int, int, int]:
    cx, cy = x + w / 2, y + h / 2
    w, h = max(w, MIN_BOX_PX), max(h, MIN_BOX_PX)
    return int(cx - w / 2), int(cy - h / 2), int(cx + w / 2), int(cy + h / 2)


def draw(frame: np.ndarray, tracks, gt, label: str, frame_number: int, trails: dict | None = None) -> np.ndarray:
    for x, y, w, h in gt:
        x1, y1, x2, y2 = padded(x, y, w, h)
        cv2.rectangle(frame, (x1, y1), (x2, y2), GT_COLOR, 1)
    for track_id, x, y, w, h, matched in tracks:
        x1, y1, x2, y2 = padded(x, y, w, h)
        color = track_color(track_id)
        if trails is not None:
            trail = trails.setdefault(track_id, [])
            if matched:
                trail.append((int(x + w / 2), int(y + h / 2)))
            if len(trail) > 1:
                cv2.polylines(frame, [np.array(trail, dtype=np.int32)], False, color, 3)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4 if matched else 1)
        cv2.putText(frame, str(track_id), (x1, max(12, y1 - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    cv2.putText(frame, f"{label}  frame {frame_number}", (12, 36), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 3)
    cv2.putText(frame, f"{label}  frame {frame_number}", (12, 36), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (20, 20, 20), 1)
    return frame


def render(video: Path, tracks_paths: list[Path], labels: list[str], out: Path, gt_path: Path | None, scale: float, max_frames: int | None = None) -> dict:
    tracks = [load_tracks(path) for path in tracks_paths]
    trails = [{} for _ in tracks_paths]  # per tracks file: track id -> centers seen so far
    gt = load_gt(gt_path) if gt_path else {}
    capture = cv2.VideoCapture(str(video))
    if not capture.isOpened():
        raise RuntimeError(f"could not open {video}")
    width, height = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = capture.get(cv2.CAP_PROP_FPS) or 25.0
    out_w, out_h = int(width * scale), int(height * scale)
    out.parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(str(out), cv2.VideoWriter_fourcc(*"avc1"), fps, (out_w * len(tracks), out_h))
    if not writer.isOpened():
        raise RuntimeError("OpenCV could not open an H.264 (avc1) writer")
    frame_number = 0
    while True:
        ok, frame = capture.read()
        if not ok or (max_frames is not None and frame_number >= max_frames):
            break
        panels = []
        for rows, label, trail in zip(tracks, labels, trails):
            panel = draw(frame.copy(), rows.get(frame_number, []), gt.get(frame_number, []), label, frame_number, trail)
            panels.append(cv2.resize(panel, (out_w, out_h), interpolation=cv2.INTER_AREA))
        writer.write(np.hstack(panels) if len(panels) > 1 else panels[0])
        frame_number += 1
    capture.release()
    writer.release()
    return {"frames": frame_number, "size": [out_w * len(tracks), out_h], "fps": fps, "out": str(out)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--video", type=Path, required=True)
    parser.add_argument("--tracks", type=Path, nargs="+", required=True, help="one tracks CSV, or two for a side-by-side video")
    parser.add_argument("--labels", nargs="+", default=None, help="one label per tracks CSV (default: the run folder names)")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--gt", type=Path, default=None, help="ground-truth tracks CSV drawn as thin green outlines")
    parser.add_argument("--scale", type=float, default=0.5)
    parser.add_argument("--max-frames", type=int, default=None)
    args = parser.parse_args()
    labels = args.labels or [path.parent.name for path in args.tracks]
    if len(labels) != len(args.tracks):
        raise SystemExit("--labels must have one entry per --tracks file")
    info = render(args.video, args.tracks, labels, args.out, args.gt, args.scale, args.max_frames)
    print(f"wrote {info['out']}: {info['frames']} frames, {info['size'][0]}x{info['size'][1]} at {info['fps']:g} fps")


if __name__ == "__main__":
    main()
