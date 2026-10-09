"""Helpers that build a ``Provenance`` with the fields every run in this kit must carry.

``Provenance`` itself is the repo's shape (``config_hash``, ``git_commit``, ``model_hash``,
``extra``). This module fixes what goes in ``extra`` so reports can rely on it:

- ``predictor``: who produced the boxes (``gt``, ``detector``, ``kit``, ``cloud``).
- ``claim``: what a comparison AGAINST this run asserts: ``accuracy`` for ground truth,
  ``parity`` for the cloud, ``regression`` for a frozen baseline. Reports print it verbatim.
- ``dataset`` / ``video_id``: the store-reference components (``"<dataset>|<video_id>|<dim>"``).
- ``inputs``: ``{label: {"path": ..., "sha256": ...}}`` for every file read.
- ``notes``: free-text facts a reader must know (frame window of the clip, confidence policy).

``git_commit`` is ``"none"`` when the working folder is not a git repository; the hash of the
``tracker/`` sources (``tracker_source_hash``) is the thing that actually pins the tracker.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from evaluation.contracts import Provenance
from evaluation.hashing import sha256_file, sha256_json

CLIP_NOTES: dict[str, str] = {
    "20251012_164031_1DAC": (
        "clip = frames 4001..5009 of the original recording 20251012_164031_1DAC "
        "(1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)"
    ),
    "20250920_063942_6C42": (
        "clip = frames 2000..2670 of the original recording 20250920_063942_6C42 "
        "(671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)"
    ),
}

DATASET_OF_VIDEO: dict[str, str] = {
    "20251012_164031_1DAC": "flock",
    "20250920_063942_6C42": "turbine",
}


def hashed_inputs(**paths: Optional[Path | str]) -> dict[str, dict[str, str]]:
    """``{label: {"path", "sha256"}}`` for every non-None path given."""
    return {
        label: {"path": str(Path(path)), "sha256": sha256_file(path)}
        for label, path in paths.items()
        if path is not None
    }


def build_provenance(
    *,
    predictor: str,
    claim: str,
    video_id: str,
    dataset: Optional[str] = None,
    config: Optional[dict] = None,
    model_hash: str = "none",
    git_commit: str = "none",
    inputs: Optional[dict[str, dict[str, str]]] = None,
    notes: Optional[list[str]] = None,
    **extra_fields,
) -> Provenance:
    """Assemble a ``Provenance`` with this kit's mandatory ``extra`` keys.

    ``config_hash`` is the sha256 of ``config`` (the producer's parameters; ``{}`` for a labelled
    reference). ``model_hash`` is whatever identifies the producer's model: the detector CSV's
    sha256 for a tracker run, ``"gt"`` for labels. Extra keyword arguments land in ``extra``.
    """
    dataset = dataset or DATASET_OF_VIDEO.get(video_id, "unknown")
    notes = list(notes or [])
    if video_id in CLIP_NOTES and CLIP_NOTES[video_id] not in notes:
        notes.append(CLIP_NOTES[video_id])
    extra = {
        "predictor": predictor,
        "claim": claim,
        "dataset": dataset,
        "video_id": video_id,
        "config": dict(config or {}),
        "inputs": dict(inputs or {}),
        "notes": notes,
    }
    extra.update(extra_fields)
    return Provenance(
        config_hash=sha256_json(config or {}),
        git_commit=git_commit,
        model_hash=model_hash,
        extra=extra,
    )


def store_ref(provenance: Provenance, dimension: str) -> str:
    """Repo-style reference ``"<dataset>|<video_id>|<dimension>"`` for a run's provenance."""
    return f"{provenance.extra['dataset']}|{provenance.extra['video_id']}|{dimension}"
