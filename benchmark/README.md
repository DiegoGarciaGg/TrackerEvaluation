# benchmark/

Everything that measures the trackers: the hand-labelled ground truth, the clip registry, the
code that runs trackers and the code that scores them, the tests, and every generated result.
The tracker under test lives in `../tracker_kit/` and is never modified from here.

```
benchmark/
  clips.json         the clip registry: one entry per video (paths, labelled frame range, ignore region, note)
  paths.py           where things are (repo root, tracker_kit, outputs); every script imports it first
  ground_truth/      hand labels per clip + the semrev clip itself, sha256 in SHA256SUMS
  experiments/       RUN trackers: Spoor's SimpleSORT and Roboflow Trackers, degraded detections, sweeps, rendering
  evaluation/        SCORE runs: run_birdeval.py, the bridge to ../evaluationScripts (the metric engine); clips registry; hashing
  tests/             14 pytest tests (runner, library trackers, registry, renderers, evaluator bridge)
  outputs/           generated: runs/, reports/, detections/, store/, docs/
```

## The pipeline, in four commands

```
# 1. run a tracker -> outputs/runs/<clip>/<tracker>/<run>/tracks.csv + tracks.csv.manifest.json
.venv/bin/python benchmark/experiments/run_experiment.py --tracker cbiou \
    --video tracker_kit/data/20251012_164031_1DAC.mp4 \
    --detections tracker_kit/data/20251012_164031_1DAC_detections.csv --detection-source real \
    --out benchmark/outputs/runs/flock/cbiou/real_default/tracks.csv
#    (or many at once: benchmark/experiments/sweep.py --spec benchmark/experiments/specs/<spec>.json --jobs 4)

# 2. score every run with the team's evaluator -> outputs/reports/birdeval/metrics_per_video.csv (+ runs_index.csv)
.venv/bin/python benchmark/evaluation/run_birdeval.py        # about 15 minutes for all runs; --only-defaults for 2

# 3. render what the runs look like -> tracks.png and tracked.mp4 next to each tracks.csv
.venv/bin/python benchmark/experiments/render_all.py

# 4. look at it
.venv/bin/streamlit run dashboard/dashboard.py
```

Run folders are named by what they received and how: `real_default` (detector output, default
parameters), `gt_default` (ground-truth boxes as detections), `real_maxage15_tent3` (parameter
sweep), `gtdeg_drop0.10_noise1.0_fp0.5_seed1` (degraded ground truth). A new tracker is a new
folder under the clip; the batch report and the dashboard discover it.

## outputs/

| folder | content | regenerable? |
|---|---|---|
| `runs/<clip>/<tracker>/<run>/` | `tracks.csv` (10 columns), `tracks.csv.manifest.json` (provenance: input hashes, parameters, library, timing), `tracks.png`, `tracked.mp4` | the CSV is the evidence (hours of compute for the flock); images and videos by `render_all.py` |
| `reports/birdeval/metrics_per_video.csv`, `metrics_pooled.csv`, `runs_index.csv`, `run_info.json` | the team evaluator's output: every metric per run, variant, similarity and video; the index maps rows to our run folders. Feeds the dashboard | yes, `run_birdeval.py` |
| `birdeval/` | the runs exported in birdeval's layout, video links and metadata cache (gitignored) | yes |
| `detections/` | degraded ground-truth detection files + manifests (deterministic from seed) | yes |
| `docs/` | the phase reports written during the work (phase0..phase6) and the plain-language report `INFORME_GENERAL.md` | no, history |

## Ground truth and references

Ground truth is the reference for accuracy; the cloud export is evaluated alongside as an
external reference (`input = cloud`), never pooled with the trackers.

| clip | labels | detector output | notes |
|---|---|---|---|
| flock | 25 birds, 10,142 boxes, all 1009 frames; first flock only, a second flock is unlabelled | yes | 9x7 px birds; 471 detector boxes sit on the burnt-in timestamp and count as false positives |
| turbine | 1 bird over frames 53..293 of 671 | yes | every frame is scored, so output outside 53..293 counts as false positives |
| semrev | 2 birds over frames 32..457 of 500, landscape 3840x2160 | no | only ground-truth boxes can be fed to the trackers |

Metrics: the team's evaluator (`../evaluationScripts`, TrackEval with DotD similarity, every
frame scored, no ignore regions); `evaluationScripts/METRICS.md` documents every column. The
bridge `evaluation/run_birdeval.py` maps our runs to its layout: detector output = input `yolo`,
ground-truth boxes = input `gt`, experiment = `<tracker>__<configuration>`, matched rows =
`row_type matched`, SimpleSORT coasting rows = `row_type predicted` (so its `predicted` and
`frozen` variants coincide; the default `matched_final` ignores them).

## Tests

```
.venv/bin/python -m pytest -q          # from the repo root; pytest.ini points here
```
