# experiments/

The only place that runs the tracker. `tracker/` and `run_tracker.py` are imported unchanged.

- `run_experiment.py`: one run. Drives `SimpleSORTTracker` exactly like `run_tracker.run`
  (same helpers, one `match_and_track` per frame), opens the video only for frame count and fps,
  writes the 6 baseline columns plus `matched, detection_count, missed_frame_count, age_frames`
  and a manifest with every input's sha256, the tracker parameters and the hash of `tracker/`.
  `--check-baseline` verifies the 6-column projection byte for byte. Re-running with the same
  inputs reuses the output. `--allow-partial-coverage` accepts a detections CSV whose frames lie
  inside the clip without touching frame 0 or the last frame (turbine GT, degraded GT).
- `detection_sources.py`: degraded ground truth (`drop_rate`, `center_noise_px`,
  `false_positives_per_frame`, `seed`) written in the detector's schema with its own manifest.
- `sweep.py`: runs a JSON spec of runs in parallel processes, reusing finished ones and
  reporting failed ones without aborting. Specs for E3, E4 and E5 are in `specs/`.

A flock run takes 5 to 11 minutes on this machine; the turbine clip takes seconds.

```
.venv/bin/python experiments/run_experiment.py --video data/20251012_164031_1DAC.mp4 \
  --detections data/20251012_164031_1DAC_detections.csv --detection-source real \
  --out outputs/runs/flock/real_default/tracks.csv --check-baseline results/flock/baseline_tracks.csv
.venv/bin/python experiments/sweep.py --spec experiments/specs/e5_params.json --jobs 4
```
