"""Content hashes used in provenance and store ids. Stdlib only."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def sha256_file(path: Path | str, chunk_size: int = 1 << 20) -> str:
    """Hex sha256 of a file's bytes."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def sha256_tree(root: Path | str, suffixes: tuple[str, ...] = (".py",)) -> str:
    """Hex sha256 over the sorted ``(relative path, file sha256)`` pairs of a source tree.

    Used to pin the exact ``tracker/`` sources a run imported. ``__pycache__`` and files whose
    suffix is not in ``suffixes`` are ignored, so byte-code caches cannot change the hash.
    """
    root = Path(root)
    entries = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in suffixes or "__pycache__" in path.parts:
            continue
        entries.append((path.relative_to(root).as_posix(), sha256_file(path)))
    return hashlib.sha256(json.dumps(entries).encode()).hexdigest()


def sha256_json(payload: object) -> str:
    """Hex sha256 of a JSON-serialisable payload, with sorted keys so dict order cannot matter."""
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()
