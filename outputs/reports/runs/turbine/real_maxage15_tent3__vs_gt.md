# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 15, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=0da8d97d2ca0 git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage15_tent3/tracks.csv sha256=85f59435bd66f8a5
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage15_tent3
  - note: clip = frames 2000..2670 of the original recording 20250920_063942_6C42 (671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)
- reference: config_hash=44136fa355b3 git=none model=gt
  - gt_tracks_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20250920_063942_6C42_reference_tracks_corrected.csv sha256=0c09f3ba788df47c
  - gt_detections_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20250920_063942_6C42_detections_corrected.csv sha256=9a7b813bcc26a1cf
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - note: confidence 1.0 on every box: labels carry no score
  - note: track_id is the annotator's obj_id as text
  - note: companion detections CSV holds the same boxes without ids (0 row mismatches)
  - note: clip = frames 2000..2670 of the original recording 20250920_063942_6C42 (671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}
- frames restricted to 53..293 on both sides

## Metrics (center-distance matching)
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 0.654 | 0.782 | 0.365 | 0.46 | 0.735 | 0 | 3.0 |
| observations | none | 6 | 0.678 | 0.811 | 0.373 | 0.48 | 0.738 | 0 | 3.0 |
| observations | none | 8 | 0.685 | 0.821 | 0.373 | 0.48 | 0.738 | 0 | 3.0 |
| observations | none | 12 | 0.710 | 0.850 | 0.373 | 0.48 | 0.738 | 0 | 3.0 |
| updates | none | 4 | 0.527 | 0.747 | -0.373 | 0.46 | 0.562 | 0 | 3.0 |
| updates | none | 6 | 0.549 | 0.780 | -0.349 | 0.52 | 0.570 | 0 | 4.0 |
| updates | none | 8 | 0.558 | 0.793 | -0.349 | 0.52 | 0.570 | 0 | 4.0 |
| updates | none | 12 | 0.584 | 0.834 | -0.332 | 0.63 | 0.575 | 2 | 4.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 11; matched pairs: 213; unmatched reference entries: 28; unmatched candidate entries: 123
- identity switches: 0; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 10

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 213 | 3 | 10 (213) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 11 | 58..86 | 29 | 0 | 19 |
| 19 | 111..116 | 6 | 0 | 6 |
| 20 | 115..116 | 2 | 0 | 2 |
| 21 | 122..122 | 1 | 0 | 1 |
| 22 | 123..160 | 38 | 0 | 29 |
| 23 | 126..144 | 19 | 0 | 5 |
| 32 | 193..222 | 30 | 0 | 25 |
| 43 | 269..269 | 1 | 0 | 1 |
| 46 | 274..293 | 20 | 0 | 20 |
| 51 | 289..291 | 3 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 11; lifespan min/median/max: 1/19/238; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 6; tracks ending in coasting: 10 (trailing rows total 111)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 55..292 | 238 | 225 | 213 | 12 | 3 | 6 | 0 | 78914 |
| 11 | 58..86 | 29 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 19 | 111..116 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 20 | 115..116 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 21 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 22 | 123..160 | 38 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 23 | 126..144 | 19 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 32 | 193..222 | 30 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 43 | 269..269 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 46 | 274..293 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 51 | 289..291 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 13; matched pairs: 215; unmatched reference entries: 26; unmatched candidate entries: 299
- identity switches: 0; fragmentation (coverage interruptions): 4; orphan candidate ids (never on a reference object): 12

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 215 | 4 | 10 (215) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 7 | 53..56 | 4 | 0 | 4 |
| 8 | 53..60 | 8 | 0 | 8 |
| 11 | 58..100 | 43 | 0 | 43 |
| 19 | 111..130 | 20 | 0 | 20 |
| 20 | 115..130 | 16 | 0 | 16 |
| 21 | 122..136 | 15 | 0 | 15 |
| 22 | 123..174 | 52 | 0 | 52 |
| 23 | 126..158 | 33 | 0 | 33 |
| 32 | 193..236 | 44 | 0 | 44 |
| 43 | 269..283 | 15 | 0 | 15 |
| 46 | 274..293 | 20 | 0 | 20 |
| 51 | 289..293 | 5 | 0 | 5 |

### Gaps and durations of candidate tracks
- tracks: 13; lifespan min/median/max: 4/20/239; tracks with internal gaps: 1; total internal gaps: 4; longest internal gap: 11; tracks ending in coasting: 12 (trailing rows total 275)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 7 | 53..56 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 8 | 53..60 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 10 | 55..293 | 239 | 239 | 215 | 24 | 4 | 11 | 0 | 78914 |
| 11 | 58..100 | 43 | 43 | 0 | 43 | 0 | 0 | 43 | - |
| 19 | 111..130 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 20 | 115..130 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 21 | 122..136 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 22 | 123..174 | 52 | 52 | 0 | 52 | 0 | 0 | 52 | - |
| 23 | 126..158 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 32 | 193..236 | 44 | 44 | 0 | 44 | 0 | 0 | 44 | - |
| 43 | 269..283 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 46 | 274..293 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 51 | 289..293 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
