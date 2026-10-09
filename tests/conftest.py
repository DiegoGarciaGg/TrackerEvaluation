"""Shared fixtures: the kit root on sys.path, the populated store, real runs."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

KIT_ROOT = Path(__file__).resolve().parent.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from evaluation.store import JsonlResultStore  # noqa: E402


@pytest.fixture(scope="session")
def kit_root() -> Path:
    return KIT_ROOT


@pytest.fixture(scope="session")
def store() -> JsonlResultStore:
    return JsonlResultStore(KIT_ROOT / "outputs" / "store")


@pytest.fixture(scope="session")
def flock_gt(store):
    return store.resolve("flock|20251012_164031_1DAC|gt")


@pytest.fixture(scope="session")
def turbine_gt(store):
    return store.resolve("turbine|20250920_063942_6C42|gt")


@pytest.fixture(scope="session")
def turbine_baseline(store):
    return store.resolve("turbine|20250920_063942_6C42|kit:baseline")
