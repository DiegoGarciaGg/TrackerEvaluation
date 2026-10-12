"""Round trip through the store port, content ids, references."""

from evaluation.store import JsonlResultStore, content_run_id
from tests.helpers import run_from_centers, straight_line


def test_persisted_run_resolves_back_unchanged(tmp_path):
    store = JsonlResultStore(tmp_path)
    original = run_from_centers(straight_line("x", range(3), 0, 0, 5, 5))
    run_id = store.persist(original, ref="test|video|gt")
    resolved = store.resolve(run_id)
    assert resolved.correctness == original.correctness
    assert resolved.tracks == original.tracks
    assert resolved.provenance == original.provenance
    assert store.resolve("test|video|gt").tracks == original.tracks
    assert store.refs() == {"test|video|gt": run_id}


def test_identical_runs_share_an_id_and_different_runs_do_not():
    a = run_from_centers(straight_line("x", range(3), 0, 0, 5, 5))
    b = run_from_centers(straight_line("x", range(3), 0, 0, 5, 5))
    c = run_from_centers(straight_line("x", range(3), 0, 0, 5, 6))
    assert content_run_id(a) == content_run_id(b)
    assert content_run_id(a) != content_run_id(c)


def test_real_store_round_trip_keeps_content_id(store, flock_gt):
    assert content_run_id(flock_gt) == store.refs()["flock|20251012_164031_1DAC|gt"]
