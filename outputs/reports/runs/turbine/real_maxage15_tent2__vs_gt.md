# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 15, "tentative_threshold": 2}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=799d24d98a8c git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage15_tent2/tracks.csv sha256=8e083fdf99e3930f
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage15_tent2
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
| observations | none | 4 | 0.630 | 0.785 | 0.241 | 0.47 | 0.700 | 0 | 4.0 |
| observations | none | 6 | 0.653 | 0.814 | 0.249 | 0.49 | 0.703 | 0 | 3.0 |
| observations | none | 8 | 0.661 | 0.824 | 0.249 | 0.49 | 0.703 | 0 | 3.0 |
| observations | none | 12 | 0.684 | 0.853 | 0.249 | 0.49 | 0.703 | 0 | 3.0 |
| updates | none | 4 | 0.448 | 0.750 | -1.253 | 0.47 | 0.440 | 0 | 4.0 |
| updates | none | 6 | 0.467 | 0.783 | -1.228 | 0.53 | 0.446 | 0 | 4.0 |
| updates | none | 8 | 0.475 | 0.796 | -1.228 | 0.53 | 0.446 | 0 | 4.0 |
| updates | none | 12 | 0.496 | 0.838 | -1.212 | 0.64 | 0.450 | 2 | 4.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 20; matched pairs: 214; unmatched reference entries: 27; unmatched candidate entries: 154
- identity switches: 0; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 19

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 214 | 3 | 8 (214) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 9 | 57..86 | 30 | 0 | 20 |
| 12 | 96..122 | 27 | 0 | 6 |
| 13 | 100..100 | 1 | 0 | 1 |
| 16 | 110..116 | 7 | 0 | 7 |
| 17 | 114..116 | 3 | 0 | 3 |
| 18 | 122..160 | 39 | 0 | 30 |
| 19 | 125..144 | 20 | 0 | 6 |
| 20 | 127..127 | 1 | 0 | 1 |
| 21 | 146..146 | 1 | 0 | 1 |
| 23 | 182..189 | 8 | 0 | 4 |
| 24 | 186..186 | 1 | 0 | 1 |
| 25 | 191..205 | 15 | 0 | 4 |
| 26 | 192..222 | 31 | 0 | 26 |
| 31 | 233..246 | 14 | 0 | 3 |
| 34 | 268..269 | 2 | 0 | 2 |
| 35 | 271..271 | 1 | 0 | 1 |
| 37 | 273..293 | 21 | 0 | 21 |
| 38 | 273..273 | 1 | 0 | 1 |
| 42 | 288..291 | 4 | 0 | 4 |

### Gaps and durations of candidate tracks
- tracks: 20; lifespan min/median/max: 1/8/239; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 6; tracks ending in coasting: 19 (trailing rows total 142)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 54..292 | 239 | 226 | 214 | 12 | 3 | 6 | 0 | 78914 |
| 9 | 57..86 | 30 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 12 | 96..122 | 27 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 13 | 100..100 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 16 | 110..116 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 17 | 114..116 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 18 | 122..160 | 39 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 19 | 125..144 | 20 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 20 | 127..127 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 21 | 146..146 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 23 | 182..189 | 8 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 24 | 186..186 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 25 | 191..205 | 15 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 26 | 192..222 | 31 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 31 | 233..246 | 14 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 34 | 268..269 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 35 | 271..271 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 37 | 273..293 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 38 | 273..273 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 42 | 288..291 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 23; matched pairs: 216; unmatched reference entries: 25; unmatched candidate entries: 512
- identity switches: 0; fragmentation (coverage interruptions): 4; orphan candidate ids (never on a reference object): 22

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 216 | 4 | 8 (216) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 5 | 53..56 | 4 | 0 | 4 |
| 6 | 53..60 | 8 | 0 | 8 |
| 7 | 53..61 | 9 | 0 | 9 |
| 9 | 57..100 | 44 | 0 | 44 |
| 12 | 96..136 | 41 | 0 | 41 |
| 13 | 100..114 | 15 | 0 | 15 |
| 16 | 110..130 | 21 | 0 | 21 |
| 17 | 114..130 | 17 | 0 | 17 |
| 18 | 122..174 | 53 | 0 | 53 |
| 19 | 125..158 | 34 | 0 | 34 |
| 20 | 127..141 | 15 | 0 | 15 |
| 21 | 146..160 | 15 | 0 | 15 |
| 23 | 182..203 | 22 | 0 | 22 |
| 24 | 186..200 | 15 | 0 | 15 |
| 25 | 191..219 | 29 | 0 | 29 |
| 26 | 192..236 | 45 | 0 | 45 |
| 31 | 233..260 | 28 | 0 | 28 |
| 34 | 268..283 | 16 | 0 | 16 |
| 35 | 271..285 | 15 | 0 | 15 |
| 37 | 273..293 | 21 | 0 | 21 |
| 38 | 273..287 | 15 | 0 | 15 |
| 42 | 288..293 | 6 | 0 | 6 |

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 4/17/240; tracks with internal gaps: 1; total internal gaps: 4; longest internal gap: 11; tracks ending in coasting: 22 (trailing rows total 488)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 53..56 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 6 | 53..60 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 7 | 53..61 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 8 | 54..293 | 240 | 240 | 216 | 24 | 4 | 11 | 0 | 78914 |
| 9 | 57..100 | 44 | 44 | 0 | 44 | 0 | 0 | 44 | - |
| 12 | 96..136 | 41 | 41 | 0 | 41 | 0 | 0 | 41 | - |
| 13 | 100..114 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 16 | 110..130 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 17 | 114..130 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 18 | 122..174 | 53 | 53 | 0 | 53 | 0 | 0 | 53 | - |
| 19 | 125..158 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 20 | 127..141 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 21 | 146..160 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 23 | 182..203 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 24 | 186..200 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 25 | 191..219 | 29 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 26 | 192..236 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 31 | 233..260 | 28 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 34 | 268..283 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 35 | 271..285 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 37 | 273..293 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 38 | 273..287 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 42 | 288..293 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
