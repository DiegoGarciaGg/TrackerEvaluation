# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=unknown config={}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=44136fa355b3 git=none model=unknown
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/results/turbine/baseline_tracks.csv sha256=f4fc4bab19093488
  - tracker/ hash=7b65976a888fbd3c coasting_known=False
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: 6-column format: coasting rows unknown, every row counted as an observation
  - note: frozen_baseline
  - note: clip = frames 2000..2670 of the original recording 20250920_063942_6C42 (671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)
- reference: config_hash=44136fa355b3 git=none model=gt
  - gt_tracks_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20250920_063942_6C42_reference_tracks_corrected.csv sha256=0c09f3ba788df47c
  - gt_detections_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20250920_063942_6C42_detections_corrected.csv sha256=9a7b813bcc26a1cf
  - note: confidence 1.0 on every box: labels carry no score
  - note: track_id is the annotator's obj_id as text
  - note: companion detections CSV holds the same boxes without ids (0 row mismatches)
  - note: clip = frames 2000..2670 of the original recording 20250920_063942_6C42 (671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}
- candidate is in the 6-column baseline format: coasting rows are indistinguishable, so only the 'updates' view (every row as written) is scored; matched-rows-only needs the 10-column format
- frames restricted to 53..293 on both sides

## Metrics (center-distance matching)
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| updates | none | 4 | 0.451 | 0.747 | -1.203 | 0.46 | 0.444 | 0 | 3.0 |
| updates | none | 6 | 0.470 | 0.780 | -1.178 | 0.52 | 0.450 | 0 | 4.0 |
| updates | none | 8 | 0.477 | 0.793 | -1.178 | 0.52 | 0.450 | 0 | 4.0 |
| updates | none | 12 | 0.498 | 0.834 | -1.162 | 0.63 | 0.454 | 2 | 4.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 15; matched pairs: 215; unmatched reference entries: 26; unmatched candidate entries: 499
- identity switches: 0; fragmentation (coverage interruptions): 4; orphan candidate ids (never on a reference object): 14

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 215 | 4 | 10 (215) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 4 | 53..55 | 3 | 0 | 3 |
| 6 | 53..64 | 12 | 0 | 12 |
| 7 | 53..71 | 19 | 0 | 19 |
| 8 | 53..91 | 39 | 0 | 39 |
| 11 | 58..115 | 58 | 0 | 58 |
| 18 | 111..145 | 35 | 0 | 35 |
| 19 | 115..145 | 31 | 0 | 31 |
| 20 | 122..175 | 54 | 0 | 54 |
| 21 | 123..189 | 67 | 0 | 67 |
| 22 | 126..173 | 48 | 0 | 48 |
| 30 | 193..251 | 59 | 0 | 59 |
| 41 | 269..293 | 25 | 0 | 25 |
| 44 | 274..293 | 20 | 0 | 20 |
| 49 | 289..293 | 5 | 0 | 5 |

### Gaps and durations of candidate tracks
- tracks: 15; lifespan min/median/max: 3/35/239; tracks with internal gaps: 1; total internal gaps: 4; longest internal gap: 11; tracks ending in coasting: 14 (trailing rows total 475)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 4 | 53..55 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 6 | 53..64 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 7 | 53..71 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 8 | 53..91 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 10 | 55..293 | 239 | 239 | 215 | 24 | 4 | 11 | 0 | 78914 |
| 11 | 58..115 | 58 | 58 | 0 | 58 | 0 | 0 | 58 | - |
| 18 | 111..145 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 19 | 115..145 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 20 | 122..175 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |
| 21 | 123..189 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 22 | 126..173 | 48 | 48 | 0 | 48 | 0 | 0 | 48 | - |
| 30 | 193..251 | 59 | 59 | 0 | 59 | 0 | 0 | 59 | - |
| 41 | 269..293 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 44 | 274..293 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 49 | 289..293 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
