# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 5, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=b658b17d67e5 git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage5_tent3/tracks.csv sha256=05411e4f939c7b90
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage5_tent3
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
| observations | none | 4 | 0.493 | 0.433 | 0.398 | 0.46 | 0.475 | 1 | 3.0 |
| observations | none | 6 | 0.510 | 0.447 | 0.407 | 0.48 | 0.475 | 1 | 3.0 |
| observations | none | 8 | 0.515 | 0.452 | 0.407 | 0.48 | 0.475 | 1 | 3.0 |
| observations | none | 12 | 0.531 | 0.465 | 0.407 | 0.48 | 0.475 | 1 | 3.0 |
| updates | none | 4 | 0.457 | 0.425 | 0.183 | 0.46 | 0.435 | 1 | 3.0 |
| updates | none | 6 | 0.474 | 0.441 | 0.199 | 0.50 | 0.439 | 1 | 3.0 |
| updates | none | 8 | 0.480 | 0.446 | 0.199 | 0.50 | 0.439 | 1 | 3.0 |
| updates | none | 12 | 0.500 | 0.463 | 0.207 | 0.54 | 0.439 | 1 | 4.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 13; matched pairs: 213; unmatched reference entries: 28; unmatched candidate entries: 114
- identity switches: 1; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 11

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f152: ref 78914: 10 -> 29 at (821.5, 3257.5), 15 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 213 | 3 | 29 (135), 10 (78) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 11 | 58..75 | 18 | 0 | 18 |
| 20 | 111..116 | 6 | 0 | 6 |
| 21 | 115..116 | 2 | 0 | 2 |
| 22 | 122..122 | 1 | 0 | 1 |
| 23 | 123..150 | 28 | 0 | 27 |
| 24 | 126..126 | 1 | 0 | 1 |
| 37 | 193..194 | 2 | 0 | 2 |
| 40 | 202..222 | 21 | 0 | 21 |
| 49 | 269..269 | 1 | 0 | 1 |
| 52 | 274..293 | 20 | 0 | 20 |
| 57 | 289..291 | 3 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 13; lifespan min/median/max: 1/6/144; tracks with internal gaps: 2; total internal gaps: 3; longest internal gap: 3; tracks ending in coasting: 12 (trailing rows total 105)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 55..143 | 89 | 84 | 78 | 6 | 1 | 3 | 3 | 78914 |
| 11 | 58..75 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 20 | 111..116 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 21 | 115..116 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 22 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 23 | 123..150 | 28 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 24 | 126..126 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 29 | 149..292 | 144 | 141 | 135 | 6 | 2 | 3 | 0 | 78914 |
| 37 | 193..194 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 40 | 202..222 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 49 | 269..269 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 52 | 274..293 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 57 | 289..291 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 13; matched pairs: 214; unmatched reference entries: 27; unmatched candidate entries: 165
- identity switches: 1; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 11

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f152: ref 78914: 10 -> 29 at (821.5, 3257.5), 15 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 214 | 3 | 29 (136), 10 (78) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 11 | 58..79 | 22 | 0 | 22 |
| 20 | 111..120 | 10 | 0 | 10 |
| 21 | 115..120 | 6 | 0 | 6 |
| 22 | 122..126 | 5 | 0 | 5 |
| 23 | 123..154 | 32 | 0 | 32 |
| 24 | 126..130 | 5 | 0 | 5 |
| 37 | 193..198 | 6 | 0 | 6 |
| 40 | 202..226 | 25 | 0 | 25 |
| 49 | 269..273 | 5 | 0 | 5 |
| 52 | 274..293 | 20 | 0 | 20 |
| 57 | 289..293 | 5 | 0 | 5 |

### Gaps and durations of candidate tracks
- tracks: 13; lifespan min/median/max: 5/10/145; tracks with internal gaps: 2; total internal gaps: 3; longest internal gap: 6; tracks ending in coasting: 12 (trailing rows total 151)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 55..147 | 93 | 93 | 78 | 15 | 1 | 5 | 10 | 78914 |
| 11 | 58..79 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 20 | 111..120 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 21 | 115..120 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 22 | 122..126 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 23 | 123..154 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 24 | 126..130 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 29 | 149..293 | 145 | 145 | 136 | 9 | 2 | 6 | 0 | 78914 |
| 37 | 193..198 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 40 | 202..226 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 49 | 269..273 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 52 | 274..293 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 57 | 289..293 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
