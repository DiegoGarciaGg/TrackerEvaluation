"""Similarity matrices fed to TrackEval: center distance (the default) and IoU (validation).

TrackEval's metrics take, per frame, a matrix ``similarity[i, j]`` in ``[0, 1]`` between
reference object ``i`` and candidate object ``j``. CLEAR and Identity accept a pair when
``similarity >= threshold`` (0.5 by default); HOTA sweeps the threshold over 0.05..0.95 and
averages. For boxes the stock similarity is IoU. For birds nine pixels across, IoU collapses on
a few pixels of offset, so this kit scores by center distance instead:

    s = max(0, 1 - d / T)        with d the center-to-center distance in pixels.

A pair is accepted when ``s >= threshold``, i.e. ``d <= T * (1 - threshold)``. The user chooses
the match distance in pixels and the scale follows: with threshold 0.5, ``T = 2 * match_px``
(8 px -> T = 16). Under HOTA's sweep, alpha = 0.5 is exactly the configured distance; smaller
alpha accepts farther pairs (alpha 0.05 -> 0.95 T), larger alpha stricter ones (0.95 -> 0.05 T),
so the averaged HOTA integrates over distances from 0.05 T to 0.95 T. The report prints both the
average and the value at alpha = 0.5.

``LocA`` and ``MOTP`` are then mean similarity over matches, i.e. ``1 - mean(d) / T``; the
report converts them back to pixels as ``T * (1 - value)``.
"""

from __future__ import annotations

import numpy as np

DEFAULT_THRESHOLD = 0.5


def scale_for_match_px(match_px: float, threshold: float = DEFAULT_THRESHOLD) -> float:
    """``T`` such that ``s >= threshold`` exactly when ``d <= match_px``."""
    if not 0.0 < threshold < 1.0:
        raise ValueError("threshold must be in (0, 1)")
    if match_px <= 0:
        raise ValueError("match_px must be positive")
    return match_px / (1.0 - threshold)


def match_px_for_alpha(scale: float, alpha: float) -> float:
    """The distance accepted at HOTA's ``alpha`` for a given scale ``T``."""
    return scale * (1.0 - alpha)


def center_distance_matrix(reference: np.ndarray, candidate: np.ndarray) -> np.ndarray:
    """``(n_ref, n_cand)`` euclidean distances between center arrays of shape ``(n, 2)``."""
    reference = np.asarray(reference, dtype=float).reshape(-1, 2)
    candidate = np.asarray(candidate, dtype=float).reshape(-1, 2)
    if len(reference) == 0 or len(candidate) == 0:
        return np.zeros((len(reference), len(candidate)))
    delta = reference[:, None, :] - candidate[None, :, :]
    return np.sqrt((delta**2).sum(axis=2))


def distance_similarity(distances: np.ndarray, scale: float) -> np.ndarray:
    """``max(0, 1 - d / T)`` elementwise."""
    return np.maximum(0.0, 1.0 - np.asarray(distances, dtype=float) / scale)


def iou_matrix(reference: np.ndarray, candidate: np.ndarray) -> np.ndarray:
    """``(n_ref, n_cand)`` IoU between ``(x, y, w, h)`` box arrays."""
    reference = np.asarray(reference, dtype=float).reshape(-1, 4)
    candidate = np.asarray(candidate, dtype=float).reshape(-1, 4)
    if len(reference) == 0 or len(candidate) == 0:
        return np.zeros((len(reference), len(candidate)))
    rx1, ry1 = reference[:, 0], reference[:, 1]
    rx2, ry2 = rx1 + reference[:, 2], ry1 + reference[:, 3]
    cx1, cy1 = candidate[:, 0], candidate[:, 1]
    cx2, cy2 = cx1 + candidate[:, 2], cy1 + candidate[:, 3]
    inter_w = np.maximum(0.0, np.minimum(rx2[:, None], cx2[None, :]) - np.maximum(rx1[:, None], cx1[None, :]))
    inter_h = np.maximum(0.0, np.minimum(ry2[:, None], cy2[None, :]) - np.maximum(ry1[:, None], cy1[None, :]))
    intersection = inter_w * inter_h
    area_r = (reference[:, 2] * reference[:, 3])[:, None]
    area_c = (candidate[:, 2] * candidate[:, 3])[None, :]
    union = area_r + area_c - intersection
    with np.errstate(divide="ignore", invalid="ignore"):
        iou = np.where(union > 0, intersection / union, 0.0)
    return iou
