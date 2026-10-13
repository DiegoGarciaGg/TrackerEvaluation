"""Shared fixtures: where things are."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from paths import BENCH_ROOT, KIT_ROOT, REPO_ROOT  # noqa: E402


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def kit_root() -> Path:
    """The Spoor tracker kit: tracker/, run_tracker.py, data/, results/."""
    return KIT_ROOT


@pytest.fixture(scope="session")
def bench_root() -> Path:
    """This benchmark: ground_truth/, outputs/, clips.json."""
    return BENCH_ROOT
