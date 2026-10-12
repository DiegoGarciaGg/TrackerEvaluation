"""One adapter per producer, all targeting ``evaluation.contracts``.

- ``reference_tracks``: ground truth (accuracy) and cloud export (parity).
- ``detections_csv``: the detector's per-frame boxes (no identities).
- ``tracker_csv``: the kit tracker's output, 6-column baseline or 10-column extended format.
- ``motchallenge``: exporter used to validate the metrics against TrackEval's own pipeline.
"""

from evaluation.adapters.detections_csv import load_detections, load_detections_run
from evaluation.adapters.motchallenge import write_motchallenge
from evaluation.adapters.reference_tracks import load_cloud_run, load_gt_run
from evaluation.adapters.tracker_csv import FORMAT_BASELINE, FORMAT_EXTENDED, detect_format, load_tracker_csv, load_tracker_run

__all__ = [
    "load_cloud_run",
    "load_gt_run",
    "load_detections",
    "load_detections_run",
    "write_motchallenge",
    "FORMAT_BASELINE",
    "FORMAT_EXTENDED",
    "detect_format",
    "load_tracker_csv",
    "load_tracker_run",
]
