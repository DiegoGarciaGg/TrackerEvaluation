"""One adapter per producer, all targeting ``evaluation.contracts``."""

from evaluation.adapters.cloud_csv import load_cloud_run
from evaluation.adapters.detections_csv import load_detections, load_detections_run
from evaluation.adapters.gt_csv import load_gt_run
from evaluation.adapters.motchallenge import write_motchallenge
from evaluation.adapters.tracker_csv import (
    FORMAT_BASELINE,
    FORMAT_EXTENDED,
    detect_format,
    load_tracker_csv,
    load_tracker_run,
)

__all__ = [
    "load_cloud_run",
    "load_detections",
    "load_detections_run",
    "load_gt_run",
    "write_motchallenge",
    "FORMAT_BASELINE",
    "FORMAT_EXTENDED",
    "detect_format",
    "load_tracker_csv",
    "load_tracker_run",
]
