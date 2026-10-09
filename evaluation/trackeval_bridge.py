"""Feed our per-frame views to TrackEval's HOTA, CLEAR and Identity metric classes directly.

TrackEval (https://github.com/JonathonLuiten/TrackEval, MIT) is pinned to commit
``12c8791b303e0a0b50f753af204249e622d0281a``; the metrics are not re-implemented here. Each
metric's ``eval_sequence(data)`` takes one sequence as a dict (format read from
``trackeval/datasets/mot_challenge_2d_box.py:get_preprocessed_seq_data``):

- ``num_timesteps``; ``gt_ids[t]`` / ``tracker_ids[t]``: int arrays of the ids present at
  timestep ``t``, relabelled to contiguous ``0..num_gt_ids-1`` / ``0..num_tracker_ids-1``;
- ``similarity_scores[t]``: ``(len(gt_ids[t]), len(tracker_ids[t]))`` matrix;
- ``num_gt_ids``, ``num_tracker_ids``, ``num_gt_dets``, ``num_tracker_dets``.

Dataset classes (file loading, class filtering, crowd-ignore handling) are bypassed on purpose:
the views already hold exactly what should be scored. The ignore region is applied to the views
before this point.

numpy compatibility: that commit still uses ``np.float`` (hota.py) and ``np.int``
(identity.py), aliases removed in numpy 1.24. They are restored here as plain ``float`` /
``int`` before ``trackeval`` is imported, which is what those aliases meant; the TrackEval
sources are not modified.
"""

from __future__ import annotations

import contextlib
import io
import warnings
from dataclasses import dataclass
from typing import Callable, Optional

import numpy as np

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for _name, _alias in (("float", float), ("int", int)):
        if _name not in np.__dict__:
            setattr(np, _name, _alias)

with contextlib.redirect_stdout(io.StringIO()):  # TrackEval prints about optional datasets it cannot import
    import trackeval  # noqa: E402
    from trackeval.metrics import CLEAR, HOTA, Identity  # noqa: E402

from evaluation.similarity import (  # noqa: E402
    DEFAULT_THRESHOLD,
    center_distance_matrix,
    distance_similarity,
    iou_matrix,
    scale_for_match_px,
)
from evaluation.views import FrameView  # noqa: E402

TRACKEVAL_COMMIT = "12c8791b303e0a0b50f753af204249e622d0281a"
TRACKEVAL_URL = "https://github.com/JonathonLuiten/TrackEval"

SimilarityFn = Callable[[list, list], np.ndarray]
"""``(reference_entries, candidate_entries) -> (n_ref, n_cand)`` similarity matrix."""


def center_distance_similarity(match_px: float, threshold: float = DEFAULT_THRESHOLD) -> SimilarityFn:
    scale = scale_for_match_px(match_px, threshold)

    def similarity(reference_entries, candidate_entries) -> np.ndarray:
        distances = center_distance_matrix(
            [entry.center for entry in reference_entries], [entry.center for entry in candidate_entries]
        )
        return distance_similarity(distances, scale)

    return similarity


def iou_similarity() -> SimilarityFn:
    def similarity(reference_entries, candidate_entries) -> np.ndarray:
        for entry in list(reference_entries) + list(candidate_entries):
            if entry.box is None:
                raise ValueError("IoU similarity needs a box on every entry")
        return iou_matrix([entry.box for entry in reference_entries], [entry.box for entry in candidate_entries])

    return similarity


@dataclass
class SequenceData:
    data: dict
    gt_id_table: dict[str, int]
    tracker_id_table: dict[str, int]


def build_sequence(
    reference: FrameView,
    candidate: FrameView,
    similarity: SimilarityFn,
    num_timesteps: Optional[int] = None,
) -> SequenceData:
    """Assemble TrackEval's per-sequence dict from two views and a similarity function."""
    frames = set(reference) | set(candidate)
    if num_timesteps is None:
        num_timesteps = (max(frames) + 1) if frames else 0
    gt_table = {track_id: index for index, track_id in enumerate(sorted({e.track_id for es in reference.values() for e in es}, key=_id_key))}
    tracker_table = {track_id: index for index, track_id in enumerate(sorted({e.track_id for es in candidate.values() for e in es}, key=_id_key))}

    data = {
        "num_timesteps": num_timesteps,
        "num_gt_ids": len(gt_table),
        "num_tracker_ids": len(tracker_table),
        "num_gt_dets": 0,
        "num_tracker_dets": 0,
        "gt_ids": [None] * num_timesteps,
        "tracker_ids": [None] * num_timesteps,
        "similarity_scores": [None] * num_timesteps,
    }
    for t in range(num_timesteps):
        reference_entries = reference.get(t, [])
        candidate_entries = candidate.get(t, [])
        data["gt_ids"][t] = np.array([gt_table[e.track_id] for e in reference_entries], dtype=int)
        data["tracker_ids"][t] = np.array([tracker_table[e.track_id] for e in candidate_entries], dtype=int)
        data["num_gt_dets"] += len(reference_entries)
        data["num_tracker_dets"] += len(candidate_entries)
        data["similarity_scores"][t] = (
            np.asarray(similarity(reference_entries, candidate_entries), dtype=float)
            if reference_entries and candidate_entries
            else np.zeros((len(reference_entries), len(candidate_entries)))
        )
    return SequenceData(data=data, gt_id_table=gt_table, tracker_id_table=tracker_table)


def _id_key(track_id: str):
    return (0, int(track_id)) if track_id.lstrip("-").isdigit() else (1, track_id)


def run_metrics(sequence: SequenceData, threshold: float = DEFAULT_THRESHOLD, scale_px: Optional[float] = None) -> dict:
    """Run HOTA, CLEAR and Identity on one sequence; return a flat ``{name: value}`` dict.

    HOTA-family arrays (19 alphas) are reported as their mean (TrackEval's summary value) and
    at alpha = 0.5 (``*_a50``). With ``scale_px`` given, ``LocA`` and ``MOTP`` are also converted
    to mean pixel distance (``*_px``).
    """
    hota = HOTA()
    clear = CLEAR({"THRESHOLD": threshold, "PRINT_CONFIG": False})
    identity = Identity({"THRESHOLD": threshold, "PRINT_CONFIG": False})
    out: dict = {}

    hota_res = hota.eval_sequence(sequence.data)
    alpha_index = int(np.argmin(np.abs(hota.array_labels - 0.5)))
    for name in hota.float_array_fields:
        out[name] = float(np.mean(hota_res[name]))
        out[f"{name}_a50"] = float(hota_res[name][alpha_index])
    for name in hota.integer_array_fields:
        out[f"{name}_a50"] = int(hota_res[name][alpha_index])
    for name in hota.float_fields:
        out[name] = float(hota_res[name])

    clear_res = clear.eval_sequence(sequence.data)
    for name in clear.fields:
        out[name] = _scalar(clear_res[name])

    identity_res = identity.eval_sequence(sequence.data)
    for name in identity.fields:
        out[name] = _scalar(identity_res[name])

    if scale_px is not None:
        out["LocA_px"] = scale_px * (1.0 - out["LocA"])
        out["LocA_a50_px"] = scale_px * (1.0 - out["LocA_a50"])
        out["MOTP_px"] = scale_px * (1.0 - out["MOTP"])
    out["num_gt_dets"] = sequence.data["num_gt_dets"]
    out["num_tracker_dets"] = sequence.data["num_tracker_dets"]
    out["num_gt_ids"] = sequence.data["num_gt_ids"]
    out["num_tracker_ids"] = sequence.data["num_tracker_ids"]
    return out


def _scalar(value):
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, np.ndarray) and value.ndim == 0:
        return value.item()
    return value


SUMMARY_FIELDS = (
    "HOTA", "DetA", "AssA", "LocA", "HOTA_a50", "DetA_a50", "AssA_a50", "LocA_a50",
    "MOTA", "MOTP", "IDSW", "Frag", "CLR_Re", "CLR_Pr", "CLR_TP", "CLR_FN", "CLR_FP", "MT", "PT", "ML",
    "IDF1", "IDP", "IDR", "IDTP", "IDFN", "IDFP",
)


def trackeval_provenance() -> dict:
    return {"library": "TrackEval", "url": TRACKEVAL_URL, "commit": TRACKEVAL_COMMIT, "license": "MIT",
            "numpy_alias_shim": "np.float and np.int restored as float/int before import; sources unmodified",
            "installed_from": getattr(trackeval, "__file__", "unknown")}
