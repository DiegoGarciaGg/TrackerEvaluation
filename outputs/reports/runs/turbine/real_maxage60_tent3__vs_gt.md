# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 60, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=4fd3461db627 git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage60_tent3/tracks.csv sha256=74696a8b51b7cdeb
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage60_tent3
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
| observations | none | 4 | 0.652 | 0.782 | 0.353 | 0.46 | 0.731 | 0 | 3.0 |
| observations | none | 6 | 0.675 | 0.811 | 0.361 | 0.48 | 0.734 | 0 | 3.0 |
| observations | none | 8 | 0.682 | 0.821 | 0.361 | 0.48 | 0.734 | 0 | 3.0 |
| observations | none | 12 | 0.707 | 0.850 | 0.361 | 0.48 | 0.734 | 0 | 3.0 |
| updates | none | 4 | 0.375 | 0.747 | -2.573 | 0.46 | 0.330 | 0 | 3.0 |
| updates | none | 6 | 0.391 | 0.780 | -2.548 | 0.52 | 0.335 | 0 | 4.0 |
| updates | none | 8 | 0.397 | 0.793 | -2.548 | 0.52 | 0.335 | 0 | 4.0 |
| updates | none | 12 | 0.414 | 0.834 | -2.531 | 0.63 | 0.338 | 2 | 4.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 12; matched pairs: 213; unmatched reference entries: 28; unmatched candidate entries: 126
- identity switches: 0; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 11

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
| 8 | 62..62 | 1 | 0 | 1 |
| 18 | 111..116 | 6 | 0 | 6 |
| 19 | 115..116 | 2 | 0 | 2 |
| 20 | 122..146 | 25 | 0 | 3 |
| 21 | 123..160 | 38 | 0 | 29 |
| 22 | 126..144 | 19 | 0 | 5 |
| 30 | 193..222 | 30 | 0 | 25 |
| 41 | 269..269 | 1 | 0 | 1 |
| 44 | 274..293 | 20 | 0 | 20 |
| 49 | 289..291 | 3 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 12; lifespan min/median/max: 1/20/238; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 6; tracks ending in coasting: 11 (trailing rows total 114)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 55..292 | 238 | 225 | 213 | 12 | 3 | 6 | 0 | 78914 |
| 11 | 58..86 | 29 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 8 | 62..62 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 18 | 111..116 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 19 | 115..116 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 20 | 122..146 | 25 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 21 | 123..160 | 38 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 22 | 126..144 | 19 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 30 | 193..222 | 30 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 41 | 269..269 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 44 | 274..293 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 49 | 289..291 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 15; matched pairs: 215; unmatched reference entries: 26; unmatched candidate entries: 829
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
| 4 | 53..85 | 33 | 0 | 33 |
| 6 | 53..94 | 42 | 0 | 42 |
| 7 | 53..101 | 49 | 0 | 49 |
| 8 | 53..121 | 69 | 0 | 69 |
| 11 | 58..145 | 88 | 0 | 88 |
| 18 | 111..175 | 65 | 0 | 65 |
| 19 | 115..175 | 61 | 0 | 61 |
| 20 | 122..205 | 84 | 0 | 84 |
| 21 | 123..219 | 97 | 0 | 97 |
| 22 | 126..203 | 78 | 0 | 78 |
| 30 | 193..281 | 89 | 0 | 89 |
| 41 | 269..293 | 25 | 0 | 25 |
| 44 | 274..293 | 20 | 0 | 20 |
| 49 | 289..293 | 5 | 0 | 5 |

### Gaps and durations of candidate tracks
- tracks: 15; lifespan min/median/max: 5/65/239; tracks with internal gaps: 1; total internal gaps: 4; longest internal gap: 11; tracks ending in coasting: 14 (trailing rows total 805)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 4 | 53..85 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 6 | 53..94 | 42 | 42 | 0 | 42 | 0 | 0 | 42 | - |
| 7 | 53..101 | 49 | 49 | 0 | 49 | 0 | 0 | 49 | - |
| 8 | 53..121 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 10 | 55..293 | 239 | 239 | 215 | 24 | 4 | 11 | 0 | 78914 |
| 11 | 58..145 | 88 | 88 | 0 | 88 | 0 | 0 | 88 | - |
| 18 | 111..175 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 19 | 115..175 | 61 | 61 | 0 | 61 | 0 | 0 | 61 | - |
| 20 | 122..205 | 84 | 84 | 0 | 84 | 0 | 0 | 84 | - |
| 21 | 123..219 | 97 | 97 | 0 | 97 | 0 | 0 | 97 | - |
| 22 | 126..203 | 78 | 78 | 0 | 78 | 0 | 0 | 78 | - |
| 30 | 193..281 | 89 | 89 | 0 | 89 | 0 | 0 | 89 | - |
| 41 | 269..293 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 44 | 274..293 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 49 | 289..293 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
