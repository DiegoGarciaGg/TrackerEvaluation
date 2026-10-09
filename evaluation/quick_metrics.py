"""Quick HOTA / MOTA / IDF1 for one or more tracker CSVs against a ground-truth CSV. Standalone.

    python evaluation/quick_metrics.py \
        --gt ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv \
        --tracks outputs/runs/flock/real_default/tracks.csv results/flock/baseline_tracks.csv \
        [--px 8] [--matched-only] [--ignore-rect 0 0 721 400] [--frames 53 293]

Reads the CSVs directly (no store, no adapters, no report), builds TrackEval's per-sequence
dict with the center-distance similarity s = max(0, 1 - d / (2 * px)) and prints one line per
file. Needs only numpy, scipy and trackeval (pinned commit 12c8791b). Nothing else in
``evaluation/`` is imported, so this file can be copied anywhere on its own.

Ground truth: ``frame_number, obj_id, x1, y1, x2, y2`` (the ``*_reference_tracks_corrected.csv``
files). Tracks: ``frame_number, track_id, x, y, w, h`` with or without the extra
``matched, ...`` columns; ``--matched-only`` keeps rows with ``matched == 1`` (10-column files only).
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import numpy as np

if "float" not in np.__dict__:  # TrackEval at that commit still spells np.float / np.int
    np.float = float
if "int" not in np.__dict__:
    np.int = int

import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    from trackeval.metrics import CLEAR, HOTA, Identity


def load_gt(path: Path) -> dict[int, list[tuple[str, float, float]]]:
    out = defaultdict(list)
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle):
            x1, y1, x2, y2 = (float(row[k]) for k in ("x1", "y1", "x2", "y2"))
            out[int(float(row["frame_number"]))].append((str(row["obj_id"]), (x1 + x2) / 2, (y1 + y2) / 2))
    return out


def load_tracks(path: Path, matched_only: bool) -> dict[int, list[tuple[str, float, float]]]:
    out = defaultdict(list)
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if matched_only and "matched" not in (reader.fieldnames or []):
            raise SystemExit(f"{path}: --matched-only needs the 'matched' column (10-column format)")
        for row in reader:
            if matched_only and int(float(row["matched"])) != 1:
                continue
            x, y, w, h = (float(row[k]) for k in ("x", "y", "w", "h"))
            out[int(float(row["frame_number"]))].append((str(row["track_id"]), x + w / 2, y + h / 2))
    return out


def filter_entries(entries, rect, frames):
    out = {}
    for frame, items in entries.items():
        if frames and not (frames[0] <= frame <= frames[1]):
            continue
        kept = [it for it in items if not (rect and rect[0] <= it[1] <= rect[2] and rect[1] <= it[2] <= rect[3])]
        if kept:
            out[frame] = kept
    return out


def sequence(gt, tr, px: float) -> dict:
    scale = 2.0 * px  # threshold 0.5 -> match when d <= px
    frames = sorted(set(gt) | set(tr))
    num_timesteps = (max(frames) + 1) if frames else 0
    gt_table = {i: n for n, i in enumerate(sorted({it[0] for its in gt.values() for it in its}))}
    tr_table = {i: n for n, i in enumerate(sorted({it[0] for its in tr.values() for it in its}))}
    data = {"num_timesteps": num_timesteps, "num_gt_ids": len(gt_table), "num_tracker_ids": len(tr_table),
            "num_gt_dets": 0, "num_tracker_dets": 0, "gt_ids": [], "tracker_ids": [], "similarity_scores": []}
    for t in range(num_timesteps):
        g = gt.get(t, [])
        c = tr.get(t, [])
        data["gt_ids"].append(np.array([gt_table[it[0]] for it in g], dtype=int))
        data["tracker_ids"].append(np.array([tr_table[it[0]] for it in c], dtype=int))
        data["num_gt_dets"] += len(g)
        data["num_tracker_dets"] += len(c)
        if g and c:
            gc = np.array([[it[1], it[2]] for it in g])
            cc = np.array([[it[1], it[2]] for it in c])
            d = np.sqrt(((gc[:, None, :] - cc[None, :, :]) ** 2).sum(axis=2))
            data["similarity_scores"].append(np.maximum(0.0, 1.0 - d / scale))
        else:
            data["similarity_scores"].append(np.zeros((len(g), len(c))))
    return data


def score(data: dict) -> dict:
    hota = HOTA().eval_sequence(data)
    clear = CLEAR({"THRESHOLD": 0.5, "PRINT_CONFIG": False}).eval_sequence(data)
    ident = Identity({"THRESHOLD": 0.5, "PRINT_CONFIG": False}).eval_sequence(data)
    return {
        "HOTA": float(np.mean(hota["HOTA"])), "DetA": float(np.mean(hota["DetA"])), "AssA": float(np.mean(hota["AssA"])),
        "MOTA": float(clear["MOTA"]), "IDF1": float(ident["IDF1"]), "IDSW": int(clear["IDSW"]), "Frag": int(clear["Frag"]),
        "TP": int(clear["CLR_TP"]), "FP": int(clear["CLR_FP"]), "FN": int(clear["CLR_FN"]),
        "gt_ids": data["num_gt_ids"], "track_ids": data["num_tracker_ids"], "rows": data["num_tracker_dets"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--gt", type=Path, required=True)
    parser.add_argument("--tracks", type=Path, nargs="+", required=True)
    parser.add_argument("--px", type=float, nargs="+", default=[8.0])
    parser.add_argument("--matched-only", action="store_true")
    parser.add_argument("--ignore-rect", type=float, nargs=4, metavar=("X1", "Y1", "X2", "Y2"), default=None)
    parser.add_argument("--frames", type=int, nargs=2, metavar=("FIRST", "LAST"), default=None)
    args = parser.parse_args()

    gt = filter_entries(load_gt(args.gt), args.ignore_rect, args.frames)
    print(f"{'file':60s} {'px':>4} {'HOTA':>6} {'DetA':>6} {'AssA':>6} {'MOTA':>7} {'IDF1':>6} {'IDSW':>5} {'Frag':>5} {'TP':>6} {'FP':>6} {'FN':>6} {'ids':>4} {'rows':>6}")
    for path in args.tracks:
        tr = filter_entries(load_tracks(path, args.matched_only), args.ignore_rect, args.frames)
        for px in args.px:
            r = score(sequence(gt, tr, px))
            print(f"{str(path)[-60:]:60s} {px:4g} {r['HOTA']:6.3f} {r['DetA']:6.3f} {r['AssA']:6.3f} {r['MOTA']:7.3f} {r['IDF1']:6.3f} "
                  f"{r['IDSW']:5d} {r['Frag']:5d} {r['TP']:6d} {r['FP']:6d} {r['FN']:6d} {r['track_ids']:4d} {r['rows']:6d}")


if __name__ == "__main__":
    main()
