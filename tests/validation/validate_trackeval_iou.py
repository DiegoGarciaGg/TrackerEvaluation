"""Our TrackEval bridge versus TrackEval's own MOTChallenge pipeline, with IoU similarity.

Exports a reference and a candidate run with ``evaluation.adapters.motchallenge``, scores them
with ``trackeval.Evaluator`` + ``MotChallenge2DBox`` (preprocessing off, stock IoU similarity)
and with our ``build_sequence`` + ``run_metrics`` using ``iou_similarity`` on the same views,
then compares HOTA, MOTA, IDF1 and every other shared field. Run as a script for a report
(``outputs/phase4/trackeval_iou_validation.md``) or through ``tests/test_trackeval_validation.py``.
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
from pathlib import Path

import numpy as np

KIT_ROOT = Path(__file__).resolve().parents[2]
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

import evaluation.trackeval_bridge as bridge  # noqa: E402  (installs the numpy alias shim first)
from evaluation.adapters.motchallenge import write_motchallenge  # noqa: E402
from evaluation.contracts import RunResult  # noqa: E402
from evaluation.views import observations_view, view_of  # noqa: E402

import trackeval  # noqa: E402
from trackeval.datasets import MotChallenge2DBox  # noqa: E402
from trackeval.metrics import CLEAR, HOTA, Identity  # noqa: E402

COMPARED_FIELDS = (
    "HOTA", "DetA", "AssA", "LocA", "DetRe", "DetPr", "AssRe", "AssPr",
    "MOTA", "MOTP", "IDSW", "Frag", "CLR_TP", "CLR_FN", "CLR_FP", "MT", "PT", "ML", "CLR_Re", "CLR_Pr",
    "IDF1", "IDP", "IDR", "IDTP", "IDFN", "IDFP",
)


def trackeval_standard(gt: RunResult, candidate: RunResult, source: str, seq: str, seq_length: int, threshold: float = 0.5) -> dict:
    """Score through TrackEval's file-based pipeline on files written by our exporter."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        write_motchallenge(root, seq, seq_length, gt, {"cand": (candidate, source)}, benchmark="MOT17", split="all")
        dataset_config = {
            **MotChallenge2DBox.get_default_dataset_config(),
            "GT_FOLDER": str(root / "gt"),
            "TRACKERS_FOLDER": str(root / "trackers"),
            "OUTPUT_FOLDER": str(root / "out"),
            "TRACKERS_TO_EVAL": ["cand"],
            "BENCHMARK": "MOT17",
            "SPLIT_TO_EVAL": "all",
            "DO_PREPROC": False,
            "PRINT_CONFIG": False,
            "SEQMAP_FILE": str(root / "gt" / "seqmaps" / "MOT17-all.txt"),
        }
        eval_config = {
            **trackeval.Evaluator.get_default_eval_config(),
            "PRINT_RESULTS": False, "PRINT_CONFIG": False, "TIME_PROGRESS": False, "DISPLAY_LESS_PROGRESS": True,
            "OUTPUT_SUMMARY": False, "OUTPUT_DETAILED": False, "PLOT_CURVES": False, "LOG_ON_ERROR": None,
        }
        with contextlib.redirect_stdout(io.StringIO()):
            evaluator = trackeval.Evaluator(eval_config)
            dataset = MotChallenge2DBox(dataset_config)
            metric_config = {"THRESHOLD": threshold, "PRINT_CONFIG": False}
            results, _ = evaluator.evaluate([dataset], [HOTA(), CLEAR(metric_config), Identity(metric_config)])
    per_seq = results["MotChallenge2DBox"]["cand"][seq]["pedestrian"]
    flat: dict = {}
    for metric_name, values in per_seq.items():
        for field, value in values.items():
            if isinstance(value, np.ndarray) and value.ndim == 1:
                flat[field] = float(np.mean(value))
            else:
                flat[field] = float(value)
    return flat


def ours(gt: RunResult, candidate: RunResult, source: str, seq_length: int, threshold: float = 0.5) -> dict:
    sequence = bridge.build_sequence(observations_view(gt), view_of(candidate, source), bridge.iou_similarity(), seq_length)
    return bridge.run_metrics(sequence, threshold)


def compare(gt: RunResult, candidate: RunResult, source: str, seq: str, seq_length: int) -> tuple[dict, dict, list[str]]:
    standard = trackeval_standard(gt, candidate, source, seq, seq_length)
    mine = ours(gt, candidate, source, seq_length)
    mismatches = [
        f"{field}: standard={standard[field]!r} ours={mine[field]!r}"
        for field in COMPARED_FIELDS
        if not np.isclose(float(standard[field]), float(mine[field]), rtol=1e-9, atol=1e-9)
    ]
    return standard, mine, mismatches


def main() -> int:
    from evaluation.adapters import load_tracker_run
    from evaluation.store import JsonlResultStore

    store = JsonlResultStore(KIT_ROOT / "outputs/store")
    cases = [
        ("turbine baseline (all rows) vs GT", store.resolve("turbine|20250920_063942_6C42|gt"), store.resolve("turbine|20250920_063942_6C42|kit:baseline"), "updates", "20250920_063942_6C42", 671),
        ("flock baseline (all rows) vs GT", store.resolve("flock|20251012_164031_1DAC|gt"), store.resolve("flock|20251012_164031_1DAC|kit:baseline"), "updates", "20251012_164031_1DAC", 1009),
        ("flock cloud vs GT", store.resolve("flock|20251012_164031_1DAC|gt"), store.resolve("flock|20251012_164031_1DAC|baseline:cloud"), "observations", "20251012_164031_1DAC", 1009),
    ]
    real = KIT_ROOT / "outputs/runs/flock/real_default/tracks.csv"
    if real.exists():
        run = load_tracker_run(real, "20251012_164031_1DAC", detection_source="real")
        cases.append(("flock real_default matched rows vs GT", store.resolve("flock|20251012_164031_1DAC|gt"), run, "observations", "20251012_164031_1DAC", 1009))
    e3 = KIT_ROOT / "outputs/runs/flock/gt_default/tracks.csv"
    if e3.exists():
        run = load_tracker_run(e3, "20251012_164031_1DAC", detection_source="gt")
        cases.append(("flock E3 gt-as-detections matched rows vs GT", store.resolve("flock|20251012_164031_1DAC|gt"), run, "observations", "20251012_164031_1DAC", 1009))

    lines = ["# TrackEval bridge validation with IoU similarity", "",
             f"TrackEval commit {bridge.TRACKEVAL_COMMIT}; standard pipeline = Evaluator + MotChallenge2DBox on files from evaluation/adapters/motchallenge.py (DO_PREPROC off).", "",
             "| case | HOTA std | HOTA ours | MOTA std | MOTA ours | IDF1 std | IDF1 ours | IDSW std/ours | fields compared | mismatches |", "|---|---|---|---|---|---|---|---|---|---|"]
    failures = 0
    for label, gt, candidate, source, seq, seq_length in cases:
        standard, mine, mismatches = compare(gt, candidate, source, seq, seq_length)
        failures += bool(mismatches)
        lines.append(f"| {label} | {standard['HOTA']:.6f} | {mine['HOTA']:.6f} | {standard['MOTA']:.6f} | {mine['MOTA']:.6f} | {standard['IDF1']:.6f} | {mine['IDF1']:.6f} | {int(standard['IDSW'])}/{int(mine['IDSW'])} | {len(COMPARED_FIELDS)} | {len(mismatches)} |")
        for mismatch in mismatches:
            lines.append(f"|  | {mismatch} | | | | | | | | |")
    text = "\n".join(lines) + "\n"
    out = KIT_ROOT / "outputs/phase4/trackeval_iou_validation.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(text)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
