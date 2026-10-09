"""Detection sources for the experiments, all written in the detector's own CSV schema.

``frame_number, frame_timestamp, x, y, w, h, area, classifier_name`` with integer pixel boxes,
``(x, y)`` the top-left corner, ``frame_timestamp = frame_number * 1000 / fps`` rounded, which
is what ``run_tracker.load_detections_by_frame`` and the evaluation adapter read.

- **real**: ``data/<video_id>_detections.csv`` as delivered (nothing to generate).
- **gt**: ``ground_truth/<video_id>_detections_corrected.csv`` as delivered: the hand-labelled
  boxes without ids, already in this schema (Phase 0 verified it row for row against the
  reference tracks file). Perfect detections, so the tracker's output is its association
  ceiling.
- **gt-degraded** (``write_degraded_gt``): the GT boxes with three independent, seeded
  corruptions, each written into the manifest next to the CSV:
    * ``drop_rate``: each box is removed with this probability (missed detections);
    * ``center_noise_px``: each kept box center is shifted by a Gaussian offset with this
      standard deviation per axis, rounded to whole pixels, size unchanged (localisation noise);
    * ``false_positives_per_frame``: per frame, a Poisson-distributed number of spurious boxes
      placed uniformly in ``fp_region`` (default: the labelled band of the flock clip) with
      sizes drawn from the GT boxes' own size distribution.
  The random stream is ``numpy.random.default_rng(seed)``; identical arguments give an identical
  file, whose sha256 goes into the tracker run's provenance through the manifest.
"""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import numpy as np

KIT_ROOT = Path(__file__).resolve().parent.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from evaluation.hashing import sha256_file  # noqa: E402

SCHEMA = ["frame_number", "frame_timestamp", "x", "y", "w", "h", "area", "classifier_name"]
DEFAULT_FP_REGION = (0, 2703, 2160, 3470)  # x_min, y_min, x_max, y_max: the flock clip's labelled band
IMAGE_SIZE = (2160, 3840)


def read_schema_rows(path: Path | str) -> list[dict]:
    with Path(path).open(newline="") as handle:
        return [{key: int(float(row[key])) if key != "classifier_name" else row[key] for key in SCHEMA} for row in csv.DictReader(handle)]


def write_schema_rows(path: Path | str, rows: list[dict]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(rows)


def write_degraded_gt(
    gt_detections_csv: Path | str,
    out_csv: Path | str,
    *,
    drop_rate: float = 0.0,
    center_noise_px: float = 0.0,
    false_positives_per_frame: float = 0.0,
    seed: int = 0,
    fps: float = 25.0,
    frame_count: Optional[int] = None,
    fp_region: tuple[int, int, int, int] = DEFAULT_FP_REGION,
) -> dict:
    """Write a degraded copy of the GT detections and a manifest; returns the manifest."""
    if not 0.0 <= drop_rate < 1.0:
        raise ValueError("drop_rate must be in [0, 1)")
    if center_noise_px < 0 or false_positives_per_frame < 0:
        raise ValueError("center_noise_px and false_positives_per_frame must be >= 0")
    rng = np.random.default_rng(seed)
    source_rows = read_schema_rows(gt_detections_csv)
    frames = sorted({row["frame_number"] for row in source_rows})
    frame_count = frame_count or (frames[-1] + 1 if frames else 0)
    sizes = np.array([(row["w"], row["h"]) for row in source_rows], dtype=int)

    kept: list[dict] = []
    dropped = 0
    shifted = 0
    for row in source_rows:
        if drop_rate > 0 and rng.random() < drop_rate:
            dropped += 1
            continue
        x, y, w, h = row["x"], row["y"], row["w"], row["h"]
        if center_noise_px > 0:
            dx, dy = np.rint(rng.normal(0.0, center_noise_px, size=2)).astype(int)
            x = int(np.clip(x + dx, 0, IMAGE_SIZE[0] - w))
            y = int(np.clip(y + dy, 0, IMAGE_SIZE[1] - h))
            shifted += int(dx != 0 or dy != 0)
        kept.append({**row, "x": x, "y": y, "w": w, "h": h, "area": w * h, "classifier_name": "gt-degraded"})

    spurious: list[dict] = []
    if false_positives_per_frame > 0:
        x_min, y_min, x_max, y_max = fp_region
        for frame_number in range(frame_count):
            count = int(rng.poisson(false_positives_per_frame))
            for _ in range(count):
                w, h = (int(v) for v in sizes[rng.integers(len(sizes))])
                x = int(rng.integers(x_min, max(x_min + 1, x_max - w)))
                y = int(rng.integers(y_min, max(y_min + 1, y_max - h)))
                spurious.append(
                    {
                        "frame_number": frame_number,
                        "frame_timestamp": round(frame_number * 1000 / fps),
                        "x": x, "y": y, "w": w, "h": h, "area": w * h,
                        "classifier_name": "gt-degraded-fp",
                    }
                )

    rows = sorted(kept + spurious, key=lambda row: (row["frame_number"], row["x"], row["y"], row["w"], row["h"]))
    write_schema_rows(out_csv, rows)
    manifest = {
        "source": "gt-degraded",
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "gt_detections_csv": {"path": str(gt_detections_csv), "sha256": sha256_file(gt_detections_csv), "rows": len(source_rows)},
        "params": {
            "drop_rate": drop_rate,
            "center_noise_px": center_noise_px,
            "false_positives_per_frame": false_positives_per_frame,
            "seed": seed,
            "fps": fps,
            "frame_count": frame_count,
            "fp_region": list(fp_region),
            "rng": "numpy.random.default_rng(seed)",
        },
        "effects": {"dropped": dropped, "kept": len(kept), "shifted": shifted, "spurious": len(spurious), "rows": len(rows)},
        "output": {"path": str(out_csv), "sha256": sha256_file(out_csv)},
    }
    Path(out_csv).with_suffix(Path(out_csv).suffix + ".manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--gt-detections", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--drop-rate", type=float, default=0.0)
    parser.add_argument("--center-noise-px", type=float, default=0.0)
    parser.add_argument("--false-positives-per-frame", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--frame-count", type=int, default=None)
    args = parser.parse_args()
    manifest = write_degraded_gt(
        args.gt_detections,
        args.out,
        drop_rate=args.drop_rate,
        center_noise_px=args.center_noise_px,
        false_positives_per_frame=args.false_positives_per_frame,
        seed=args.seed,
        frame_count=args.frame_count,
    )
    print(json.dumps(manifest["effects"]))


if __name__ == "__main__":
    main()
