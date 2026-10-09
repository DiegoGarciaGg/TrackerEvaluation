"""Shared CSV reading for the adapters: strict headers, numeric parsing, frame ordering."""

from __future__ import annotations

import csv
from pathlib import Path


def read_rows(path: Path | str, required: tuple[str, ...]) -> list[dict[str, str]]:
    """Read a CSV into dict rows, refusing a file that lacks any ``required`` column."""
    with Path(path).open(newline="") as handle:
        reader = csv.DictReader(handle)
        header = tuple(reader.fieldnames or ())
        missing = [column for column in required if column not in header]
        if missing:
            raise ValueError(f"{path}: missing columns {missing}; header is {list(header)}")
        return list(reader)


def header_of(path: Path | str) -> tuple[str, ...]:
    with Path(path).open(newline="") as handle:
        return tuple(csv.DictReader(handle).fieldnames or ())


def as_int(value: str, what: str) -> int:
    """Parse an integer that may be written as ``"3"`` or ``"3.0"``."""
    number = float(value)
    if not number.is_integer():
        raise ValueError(f"{what}: expected an integer, got {value!r}")
    return int(number)
