# benchmark/experiments/

The only place that runs trackers. Spoor's `tracker_kit/tracker/` and `run_tracker.py` are imported unchanged; the Roboflow trackers go through a small adapter.

- `run_experiment.py`: one run. Drives `SimpleSORTTracker` exactly like `run_tracker.run`
  (same helpers, one `match_and_track` per frame), opens the video only for frame count and fps,
  writes the 6 baseline columns plus `matched, detection_count, missed_frame_count, age_frames`
  and a manifest with every input's sha256, the tracker parameters and the hash of `tracker/`.
  `--check-baseline` verifies the 6-column projection byte for byte. Re-running with the same
  inputs reuses the output. `--allow-partial-coverage` accepts a detections CSV whose frames lie
  inside the clip without touching frame 0 or the last frame (turbine GT, degraded GT).
- `detection_sources.py`: degraded ground truth (`drop_rate`, `center_noise_px`,
  `false_positives_per_frame`, `seed`) written in the detector's schema with its own manifest.
- `library_trackers.py`: adapter to Roboflow Trackers (SORT, ByteTrack, OC-SORT, BoT-SORT,
  C-BIoU). `run_experiment.py --tracker <name>` uses it; same output format and manifest.
- `sweep.py`: runs a JSON spec of runs in parallel processes, reusing finished ones and
  reporting failed ones without aborting. Specs for E3, E4, E5 and the library trackers are in `specs/`.
- `render_video.py`: draws a run (or two, side by side) over the clip as an H.264 mp4 for the
  dashboard.
- `render_tracks_image.py`: a run's complete trajectories drawn on the clip's last frame (`tracks.png`).
- `render_all.py`: `tracks.png` and `tracked.mp4` next to every default run of every clip in `clips.json`.
- `specs/`: the JSON lists of runs used so far (E3, E4, E5, the Roboflow trackers, the semrev clip).

Output layout: `benchmark/outputs/runs/<clip>/<tracker>/<run>/` with `tracks.csv`, its manifest, and later `tracks.png` and `tracked.mp4`.

A flock run takes 5 to 11 minutes on this machine; the turbine clip takes seconds.

```
.venv/bin/python benchmark/experiments/run_experiment.py --video tracker_kit/data/20251012_164031_1DAC.mp4 \
  --detections tracker_kit/data/20251012_164031_1DAC_detections.csv --detection-source real \
  --out benchmark/outputs/runs/flock/simplesort/real_default/tracks.csv --check-baseline tracker_kit/results/flock/baseline_tracks.csv
.venv/bin/python benchmark/experiments/sweep.py --spec benchmark/experiments/specs/e5_params.json --jobs 4
.venv/bin/python benchmark/experiments/render_all.py
```
