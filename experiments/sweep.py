"""Run many tracker experiments in parallel processes, reusing finished ones.

    python experiments/sweep.py --spec experiments/specs/e5_params.json --jobs 4

A spec is a JSON list of runs; each entry has the ``run_experiment`` arguments::

    {"out": "outputs/runs/flock/maxage_15/tracks.csv",
     "video": "data/20251012_164031_1DAC.mp4",
     "detections": "data/20251012_164031_1DAC_detections.csv",
     "detection_source": "real",
     "params": {"max_age": 15},
     "label": "E5 max_age=15"}

Optionally a ``degrade`` block generates the detections first (``experiments.detection_sources
.write_degraded_gt`` arguments plus ``gt_detections``); its manifest is attached to the run's
provenance. One tracker run takes about four minutes on the flock clip, so ``--jobs`` matters.
Already-finished runs (matching manifest and output hash) are skipped unless ``--force``.
"""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from experiments.detection_sources import write_degraded_gt  # noqa: E402
from experiments.run_experiment import run_experiment  # noqa: E402


def _one(entry: dict, force: bool) -> dict:
    details = {}
    detections = Path(entry["detections"])
    if "degrade" in entry:
        degrade = dict(entry["degrade"])
        gt_csv = Path(degrade.pop("gt_detections"))
        manifest_path = detections.with_suffix(detections.suffix + ".manifest.json")
        if manifest_path.exists() and detections.exists() and not force:
            details = json.loads(manifest_path.read_text())
            if details.get("params", {}) != {**details.get("params", {}), **degrade}:
                details = write_degraded_gt(gt_csv, detections, **degrade)
        else:
            details = write_degraded_gt(gt_csv, detections, **degrade)
    return run_experiment(
        video_path=Path(entry["video"]),
        detections_path=detections,
        out_path=Path(entry["out"]),
        params=entry.get("params"),
        detection_source=entry.get("detection_source", "real"),
        detection_source_details=details,
        label=entry.get("label"),
        check_baseline=Path(entry["check_baseline"]) if entry.get("check_baseline") else None,
        force=force,
        allow_partial_coverage=bool(entry.get("allow_partial_coverage", False)),
    )


def run_spec(entries: list[dict], jobs: int, force: bool = False) -> list[dict]:
    results = []
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        futures = {pool.submit(_one, entry, force): entry for entry in entries}
        for future in as_completed(futures):
            entry = futures[future]
            try:
                manifest = future.result()
            except BaseException as error:  # one failed run must not abort the sweep
                print(f"[failed] {entry.get('label') or entry['out']}: {type(error).__name__}: {str(error)[:200]}", flush=True)
                results.append({"label": entry.get("label"), "out": entry["out"], "error": str(error)})
                continue
            output = manifest["output"]
            print(
                f"[{'reused' if manifest['reused'] else 'done'}] {entry.get('label') or entry['out']}: "
                f"{output['rows']} rows, {output['track_ids']} ids, {manifest['elapsed_seconds']} s",
                flush=True,
            )
            results.append(manifest)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    entries = json.loads(args.spec.read_text())
    run_spec(entries, args.jobs, args.force)


if __name__ == "__main__":
    main()
