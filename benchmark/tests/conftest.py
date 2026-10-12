"""Shared fixtures: the kit root on sys.path, the populated store, real runs."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from paths import BENCH_ROOT, KIT_ROOT, OUTPUTS, REPO_ROOT  # noqa: E402

from evaluation.store import JsonlResultStore  # noqa: E402


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


@pytest.fixture(scope="session")
def store() -> JsonlResultStore:
    return JsonlResultStore(OUTPUTS / "store")


@pytest.fixture(scope="session")
def flock_gt(store):
    return store.resolve("flock|20251012_164031_1DAC|gt")


@pytest.fixture(scope="session")
def turbine_gt(store):
    return store.resolve("turbine|20250920_063942_6C42|gt")


@pytest.fixture(scope="session")
def turbine_baseline(store):
    return store.resolve("turbine|20250920_063942_6C42|kit:baseline")
