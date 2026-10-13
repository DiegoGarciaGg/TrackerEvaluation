"""Score every run with the team's evaluator (``evaluationScripts/birdeval``) and write the tables
the dashboard reads.

    python benchmark/evaluation/run_birdeval.py [--only-defaults] [--variants matched_final,predicted] \
        [--s-schemes per_track,fixed] [--measures dotd,iou]

What it does, in order:

1. Exports every ``benchmark/outputs/runs/<clip>/<tracker>/<run>/tracks.csv`` into birdeval's
   labelled layout, ``outputs/birdeval/runs_v2/<input>/<experiment>/<video>_tracks.csv``, with
   ``input`` = ``yolo`` (detector output) or ``gt`` (ground-truth boxes as detections) and
   ``experiment`` = ``<tracker>__<configuration>`` (``simplesort__default``, ``cbiou__default``,
   ``simplesort__maxage15_tent3``, ...). Row mapping: our matched rows become ``row_type =
   matched``; SimpleSORT's coasting rows (the last matched box repeated) become ``row_type =
   predicted``, so birdeval's ``predicted`` and ``frozen`` variants coincide for us and the
   default ``matched_final`` variant ignores them. Our runner never writes pre-confirmation rows,
   so ``matched_final`` equals ``matched_online``. Every track in our CSVs is confirmed.
2. Links the three clips into one videos folder (birdeval reads frame counts from the videos),
   writes ``config.yaml`` and runs ``birdeval.batch.run_batch`` with the cloud exports as the
   external reference. Similarity: DotD per_track (primary), DotD fixed 9 px and IoU, as in the
   team's defaults; see ``evaluationScripts/README.md`` for every column.
3. Writes ``outputs/reports/birdeval/metrics_per_video.csv`` (ALL metrics, one row per
   experiment, input, variant, similarity and video), ``metrics_pooled.csv``, ``run_info.json``,
   and ``runs_index.csv`` (experiment, input, video -> our run folder, tracker, parameters,
   degradation), which the dashboard joins with the metrics to show a few of them.

Scoring rules inherited from the team evaluator: no ignore region (the flock's timestamp-overlay
detections count as false positives) and no labelled frame range (every frame is scored, so
turbine output outside frames 53..293 counts as false positives); matching is DotD
``exp(-d/s)`` with ``s`` the bird's size (primary), a fixed 9 px scale, or IoU.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from paths import OUTPUTS, REPO_ROOT, RUNS  # noqa: E402

sys.path.insert(0, str(REPO_ROOT / "evaluationScripts"))

from evaluation.clips import load_clips  # noqa: E402

BIRDEVAL_OUT = OUTPUTS / "birdeval"
REPORT_OUT = OUTPUTS / "reports" / "birdeval"
INPUT_OF_SOURCE = {"real": "yolo", "gt": "gt"}


def configuration_of(run: str) -> str:
    """``real_default`` -> ``default``, ``gt_default`` -> ``default``, ``real_maxage15_tent3`` -> ``maxage15_tent3``."""
    for prefix in ("real_", "gt_"):
        if run.startswith(prefix):
            return run[len(prefix):]
    return run


def export_runs(only_defaults: bool) -> list[dict]:
    """Write birdeval's labelled CSVs and return the index rows."""
    clips = load_clips(REPO_ROOT)
    index = []
    root = BIRDEVAL_OUT / "runs_v2"
    for clip_name, clip in clips.items():
        for tracks in sorted((RUNS / clip_name).glob("*/*/tracks.csv")):
            tracker, run = tracks.parent.parent.name, tracks.parent.name
            if only_defaults and run not in ("real_default", "gt_default"):
                continue
            manifest_path = tracks.with_suffix(tracks.suffix + ".manifest.json")
            manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
            source = manifest.get("inputs", {}).get("detections", {}).get("source", "real" if run.startswith("real") else "gt")
            input_name = INPUT_OF_SOURCE.get(source, "gt" if source.startswith("gt") else "yolo")
            experiment = f"{tracker}__{configuration_of(run)}"
            out = root / input_name / experiment / f"{clip['video_id']}_tracks.csv"
            out.parent.mkdir(parents=True, exist_ok=True)
            with tracks.open(newline="") as src, out.open("w", newline="") as dst:
                reader = csv.DictReader(src)
                writer = csv.writer(dst)
                writer.writerow(["frame_number", "track_id", "x", "y", "w", "h", "row_type", "track_confirmed"])
                for row in reader:
                    matched = row.get("matched", "1") == "1"
                    writer.writerow([row["frame_number"], row["track_id"], row["x"], row["y"], row["w"], row["h"],
                                     "matched" if matched else "predicted", "True"])
            index.append({
                "experiment": experiment, "input": input_name, "video": clip["video_id"], "clip": clip_name,
                "tracker": tracker, "run": run, "library": manifest.get("tracker", {}).get("library", ""),
                "params": json.dumps(manifest.get("tracker", {}).get("params") or {}, sort_keys=True),
                "degradation": json.dumps(manifest.get("inputs", {}).get("detections", {}).get("details", {}).get("params") or {}, sort_keys=True),
                "tracks_csv": str(tracks.relative_to(REPO_ROOT)),
            })
    return index


def link_videos() -> Path:
    videos = BIRDEVAL_OUT / "videos"
    videos.mkdir(parents=True, exist_ok=True)
    for clip in load_clips(REPO_ROOT).values():
        link = videos / f"{clip['video_id']}.mp4"
        if not link.exists():
            os.symlink(clip["video"], link)
    return videos


def write_config(videos_dir: Path, variants: list[str], s_schemes: list[str], measures: list[str]) -> dict:
    config = {
        "paths": {
            "videos_dir": str(videos_dir),
            "gt_dir": str(REPO_ROOT / "benchmark" / "ground_truth"),
            "gt_suffix": "_reference_tracks_corrected.csv",
            "results": [{"path": str(BIRDEVAL_OUT / "runs_v2"), "layout": "v2", "inputs": ["gt", "yolo"]}],
            "aliases": None,
            "external": [{"name": "cloud", "dir": str(REPO_ROOT / "tracker_kit" / "data"), "suffix": "_cloud_reference_tracks.csv"}],
            "cache_dir": str(BIRDEVAL_OUT / "cache"),
        },
        "similarity": {"measures": measures, "primary": "dotd",
                       "dotd": {"s_schemes": s_schemes, "primary_s_scheme": "per_track", "s_fixed": 9.0, "s_min": 4.0}},
        "variants": {"default": "matched_final", "derived": variants},
        "trackeval": {"use_parallel": False, "num_cores": 1},
    }
    import yaml

    (BIRDEVAL_OUT / "config.yaml").write_text(yaml.safe_dump(config, sort_keys=False))
    return config


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only-defaults", action="store_true", help="score only the real_default / gt_default runs")
    parser.add_argument("--variants", default="matched_final,predicted", help="birdeval variants to derive (comma-separated)")
    parser.add_argument("--s-schemes", default="per_track,fixed", help="DotD scales: per_track, fixed, per_box")
    parser.add_argument("--measures", default="dotd,iou")
    args = parser.parse_args()

    index = export_runs(args.only_defaults)
    REPORT_OUT.mkdir(parents=True, exist_ok=True)
    with (REPORT_OUT / "runs_index.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(index[0].keys()))
        writer.writeheader()
        writer.writerows(index)
    print(f"exported {len(index)} run files to {BIRDEVAL_OUT / 'runs_v2'}", flush=True)

    config = write_config(link_videos(), args.variants.split(","), args.s_schemes.split(","), args.measures.split(","))
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s",
                        handlers=[logging.StreamHandler(), logging.FileHandler(REPORT_OUT / "evaluate.log", mode="w")])
    from birdeval.batch import run_batch

    info = run_batch(config, REPORT_OUT, REPO_ROOT, sys.argv)
    print(f"wrote {REPORT_OUT / 'metrics_per_video.csv'} ({info['n_videos']} videos, {info['n_runs']} runs, {len(info['skipped'])} skipped)")


if __name__ == "__main__":
    main()
