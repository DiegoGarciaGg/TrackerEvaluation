# Phase 6: dashboard redesign, other trackers, videos (2026-10-12)

## What changed

- **Simplification pass** on the evaluation code: the three reference adapters merged into
  `evaluation/adapters/reference_tracks.py`; diagnostics computed once per report instead of
  four times (reports shrank from 59 MB to a few MB); frozen-baseline duplicate rows removed
  from the summary (the `real_default` run reproduces `results/*/baseline_tracks.csv` byte for
  byte, verified); unused helpers and leftover sweep specs deleted. 42 tests pass.
- **Roboflow Trackers integrated** (`experiments/library_trackers.py`, 70 lines):
  `run_experiment.py --tracker sort|bytetrack|ocsort|botsort|cbiou` runs the same detections
  through the library, writes the same 10-column CSV and manifest (`tracker.algorithm`,
  `tracker.library`, effective parameters). The Spoor tracker is untouched. Installed with
  `--no-deps` so `opencv-python-headless` stays. McByte not integrated (torch and mask
  dependencies).
- **Videos**: `experiments/render_video.py` draws a run over the clip (H.264, half resolution,
  ground truth as green outlines, boxes padded to a visible minimum) and composes two runs side
  by side, frame-synchronous by construction. `experiments/render_all.sh` renders every default
  run.
- **Dashboard redesigned** (`dashboard.py`): video + detection-source selectors on top; one
  comparison table (HOTA, AssA, MOTA, MOTP px, IDF1, IDSW, Frag, best per column marked);
  HOTA/IDF1/MOTA bar panels in one hue with the Spoor tracker emphasised; DetA versus AssA
  breakdown in an expander; video viewer for one tracker and side by side (rendered on demand);
  the SimpleSORT E4/E5 studies collapsed. Trackers are discovered from `summary_rows.json`.

## Real results (8 px, matched rows, default parameters, ground truth reference)

Flock, detector output:

| tracker | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| C-BIoU | 0.276 | 0.614 | -0.040 | 1.77 | 0.184 | 153 | 374 |
| ByteTrack | 0.276 | 0.617 | -0.044 | 1.70 | 0.181 | 186 | 338 |
| SimpleSORT (Spoor) | 0.273 | 0.594 | -0.069 | 1.80 | 0.180 | 156 | 416 |
| BoT-SORT | 0.145 | 0.194 | -0.032 | 1.80 | 0.088 | 131 | 316 |
| SORT | 0.071 | 0.064 | -0.042 | 1.70 | 0.044 | 94 | 190 |
| OC-SORT | 0.069 | 0.067 | 0.008 | 1.37 | 0.041 | 44 | 92 |

Flock, ground-truth boxes as detections:

| tracker | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| C-BIoU | 0.990 | 0.987 | 0.993 | 0.01 | 0.995 | 15 | 122 |
| ByteTrack | 0.971 | 0.951 | 0.989 | 0.01 | 0.969 | 41 | 132 |
| SimpleSORT (Spoor) | 0.962 | 0.934 | 0.993 | 0.01 | 0.973 | 17 | 116 |
| BoT-SORT | 0.566 | 0.482 | 0.587 | 0.03 | 0.618 | 811 | 555 |
| SORT | 0.411 | 0.323 | 0.510 | 0.02 | 0.471 | 152 | 220 |
| OC-SORT | 0.353 | 0.300 | 0.410 | 0.03 | 0.450 | 50 | 125 |

Turbine (frames 53..293): detector output SimpleSORT 0.682, C-BIoU 0.565, ByteTrack 0.468,
OC-SORT 0.189, BoT-SORT 0.162, SORT 0.075; ground-truth boxes ByteTrack 0.996, C-BIoU 0.996,
SimpleSORT 0.992, BoT-SORT 0.905, OC-SORT 0.423, SORT 0.232. Full tables in
`outputs/reports/SUMMARY.md` ("Trackers compared").

## Reading

- With detector output the three best trackers are within 0.003 HOTA of each other: the
  detector's 17 % coverage of the labelled birds is the ceiling, not the association.
- With perfect boxes, C-BIoU (buffered IoU, a BoT-SORT variant without re-identification) beats
  the Spoor tracker on association (AssA 0.987 vs 0.934, 15 vs 17 switches); ByteTrack is
  close. SORT, OC-SORT and BoT-SORT with library defaults fail on nine-pixel birds: their IoU
  gates (0.3, 0.2) are too strict for boxes that move most of their own size per frame.
- Caveats recorded in every manifest: no confidence given to the libraries (ByteTrack
  single-stage fallback), BoT-SORT camera motion compensation off, library defaults otherwise
  untuned. A fair tuning of the IoU gates would be the next experiment, not a conclusion here.

## Not done

- McByte (heavy dependencies). No tuning of library parameters.
- The dashboard's design was checked headlessly (Streamlit AppTest across every selector) and
  the server verified to serve; no browser screenshot was taken.
- The palette validator of the dataviz skill needs node, which is not installed; charts use a
  single hue plus grey (emphasis form) so no categorical palette is at stake.

## Added the same day: third clip (semrev) and complete-track images

- `clips.json` is now the clip registry (paths, labelled frame range, ignore region, note),
  read by the batch report, the CLI, the renderers and the dashboard. Adding a clip is one
  entry plus its files.
- New clip `semrev_collision_20250419_073201_2B6B_176-196`: landscape 3840x2160, 500 frames,
  converted from Supervisely with `~/convert/supervisely_json_to_csv.py`; two labelled birds
  (79248 over frames 32..457, 79276 over 359..409), boxes about 35 px, no duplicates. CSVs and
  clip copied to `ground_truth/` with sha256 in `SHA256SUMS`. There is no detector output for
  it, so only the "ground-truth boxes as detections" configuration exists; accuracy is scored on
  frames 32..457.
- Results (HOTA, 8 px): SimpleSORT 0.992, ByteTrack 0.969, C-BIoU 0.969, BoT-SORT 0.790,
  SORT 0.724, OC-SORT 0.698. With bigger birds the IoU trackers do far better than on the
  flock; SimpleSORT loses nothing but the first detections of each track.
- `experiments/render_tracks_image.py` draws a run's complete trajectories on the clip's last
  frame (`tracks.png`, one per run, a second to render); `render_all.py` produces images and
  videos for every default run. The dashboard shows the images of all trackers in a grid above
  the videos, which is the cheap way to compare runs visually.
