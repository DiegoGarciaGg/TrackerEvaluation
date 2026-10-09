"""Export a ``RunResult`` to MOTChallenge text files (for TrackEval's standard pipeline).

Used in Phase 4 to validate our own TrackEval bridge: the same run exported here and scored by
TrackEval's stock ``MotChallenge2DBox`` loader must give the same HOTA, MOTA and IDF1 (with IoU
similarity) as our in-memory path.

Layout written (TrackEval's MOT17-style expectation)::

    <root>/gt/<benchmark>-<split>/<seq>/gt/gt.txt
    <root>/gt/<benchmark>-<split>/<seq>/seqinfo.ini
    <root>/gt/seqmaps/<benchmark>-<split>.txt
    <root>/trackers/<benchmark>-<split>/<tracker>/data/<seq>.txt

Rows: ``frame, id, x, y, w, h, conf, class, visibility`` for gt (class 1 = pedestrian, the only
class TrackEval's MOT loader evaluates by default; visibility 1.0) and
``frame, id, x, y, w, h, conf, -1, -1, -1`` for a tracker. Frames are 1-based, as the format
requires. Coordinates are written unchanged (the kit's pixel coordinates); the official format
nominally uses 1-based pixels, but since both sides are exported the same way no similarity
changes. Track ids must be integers in the format; non-integer ids are mapped through a sorted
table that is returned to the caller.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from evaluation.contracts import RunResult

RowSource = Literal["observations", "updates"]


def _rows(result: RunResult, source: RowSource) -> list[tuple[int, str, float, float, float, float]]:
    rows = []
    if source == "observations":
        for frame, detections in result.correctness.items():
            for detection in detections:
                if detection.track_id is None:
                    continue
                x, y, w, h = detection.box_xywh
                rows.append((frame, detection.track_id, x, y, w, h))
    elif source == "updates":
        for track in result.tracks:
            for update in track.updates:
                if update.box_xywh is None:
                    raise ValueError(f"track {track.track_id} update at frame {update.frame_number} has no box")
                x, y, w, h = update.box_xywh
                rows.append((update.frame_number, track.track_id, x, y, w, h))
    else:
        raise ValueError(f"unknown row source {source!r}")
    return sorted(rows, key=lambda row: (row[0], _sort_key(row[1])))


def _sort_key(track_id: str):
    return (0, int(track_id)) if track_id.lstrip("-").isdigit() else (1, track_id)


def id_table(result: RunResult, source: RowSource) -> dict[str, int]:
    """Deterministic ``track_id -> positive integer`` map (integers keep their own value when
    possible, others are numbered after the largest)."""
    ids = sorted({row[1] for row in _rows(result, source)}, key=_sort_key)
    table: dict[str, int] = {}
    used: set[int] = set()
    for track_id in ids:
        if track_id.lstrip("-").isdigit() and int(track_id) > 0 and int(track_id) not in used:
            table[track_id] = int(track_id)
            used.add(int(track_id))
    next_id = (max(used) if used else 0) + 1
    for track_id in ids:
        if track_id not in table:
            table[track_id] = next_id
            used.add(next_id)
            next_id += 1
    return table


def write_motchallenge(
    root: Path | str,
    seq: str,
    seq_length: int,
    gt: RunResult,
    trackers: dict[str, tuple[RunResult, RowSource]],
    benchmark: str = "KIT",
    split: str = "all",
    image_size: tuple[int, int] = (2160, 3840),
) -> dict[str, dict[str, int]]:
    """Write one sequence with its gt and one or more tracker outputs. Returns the id tables."""
    root = Path(root)
    tag = f"{benchmark}-{split}"
    gt_dir = root / "gt" / tag / seq / "gt"
    gt_dir.mkdir(parents=True, exist_ok=True)
    tables: dict[str, dict[str, int]] = {}

    gt_table = id_table(gt, "observations")
    tables["gt"] = gt_table
    with (gt_dir / "gt.txt").open("w") as handle:
        for frame, track_id, x, y, w, h in _rows(gt, "observations"):
            handle.write(f"{frame + 1},{gt_table[track_id]},{x:g},{y:g},{w:g},{h:g},1,1,1\n")
    (root / "gt" / tag / seq / "seqinfo.ini").write_text(
        "[Sequence]\n"
        f"name={seq}\n"
        "imDir=img1\n"
        "frameRate=25\n"
        f"seqLength={seq_length}\n"
        f"imWidth={image_size[0]}\n"
        f"imHeight={image_size[1]}\n"
        "imExt=.jpg\n"
    )
    seqmaps = root / "gt" / "seqmaps"
    seqmaps.mkdir(parents=True, exist_ok=True)
    seqmap_path = seqmaps / f"{tag}.txt"
    existing = seqmap_path.read_text().splitlines() if seqmap_path.exists() else ["name"]
    if seq not in existing:
        existing.append(seq)
    seqmap_path.write_text("\n".join(existing) + "\n")

    for tracker_name, (result, source) in trackers.items():
        table = id_table(result, source)
        tables[tracker_name] = table
        data_dir = root / "trackers" / tag / tracker_name / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        with (data_dir / f"{seq}.txt").open("w") as handle:
            for frame, track_id, x, y, w, h in _rows(result, source):
                handle.write(f"{frame + 1},{table[track_id]},{x:g},{y:g},{w:g},{h:g},1,-1,-1,-1\n")
    return tables
