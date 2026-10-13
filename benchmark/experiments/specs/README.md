# benchmark/experiments/specs/

JSON lists of runs for `sweep.py` (`python benchmark/experiments/sweep.py --spec <file> --jobs 4`).
Each entry is one call to `run_experiment.py`: tracker, video, detections, detection source,
output path, parameters, optional degradation of the ground-truth boxes.

| file | runs |
|---|---|
| `e3_gt.json` | SimpleSORT with ground-truth boxes as detections (association ceiling), flock and turbine |
| `e4_degraded_flock.json` | SimpleSORT on degraded ground truth: drop 0/10/20/30 %, center noise 0/1/3 px, 0 or 0.5 false positives per frame, 3 seeds (70 runs) |
| `e5_params.json` | SimpleSORT parameter grid, max_age 5/15/30/60 x tentative_threshold 2/3/5, real detections, both clips |
| `library_trackers.json` | SORT, ByteTrack, OC-SORT, BoT-SORT, C-BIoU on flock and turbine, real and ground-truth detections |
| `semrev_gt.json` | all six trackers on the semrev clip with ground-truth boxes |

Finished runs are reused (same inputs and parameters), so a spec can be re-run safely.
