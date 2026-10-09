# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 5, "tentative_threshold": 2}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=2d7bd1d230eb git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage5_tent2/tracks.csv sha256=9fb95ca455424a1e
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage5_tent2
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
| view | region | px | ref | cand | HOTA | DetA | AssA | LocA px | HOTA@a.5 | MOTA | MOTP px | IDSW | Frag | IDF1 | IDP | IDR | Re | Pr | TP | FN | FP | MT | PT | ML |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 241 | 360 | 0.472 | 0.517 | 0.432 | 0.42 | 0.503 | 0.270 | 0.47 | 1 | 4.0 | 0.449 | 0.375 | 0.560 | 0.884 | 0.592 | 213 | 28 | 147 | 1 | 0 | 0 |
| observations | none | 6 | 241 | 360 | 0.489 | 0.535 | 0.447 | 0.45 | 0.505 | 0.278 | 0.49 | 1 | 3.0 | 0.449 | 0.375 | 0.560 | 0.888 | 0.594 | 214 | 27 | 146 | 1 | 0 | 0 |
| observations | none | 8 | 241 | 360 | 0.494 | 0.540 | 0.451 | 0.46 | 0.505 | 0.278 | 0.49 | 1 | 3.0 | 0.449 | 0.375 | 0.560 | 0.888 | 0.594 | 214 | 27 | 146 | 1 | 0 | 0 |
| observations | none | 12 | 241 | 360 | 0.509 | 0.558 | 0.465 | 0.65 | 0.505 | 0.278 | 0.49 | 1 | 3.0 | 0.449 | 0.375 | 0.560 | 0.888 | 0.594 | 214 | 27 | 146 | 1 | 0 | 0 |
| updates | none | 4 | 241 | 477 | 0.411 | 0.399 | 0.424 | 0.43 | 0.436 | -0.216 | 0.47 | 1 | 4.0 | 0.376 | 0.283 | 0.560 | 0.884 | 0.447 | 213 | 28 | 264 | 1 | 0 | 0 |
| updates | none | 6 | 241 | 477 | 0.427 | 0.414 | 0.440 | 0.48 | 0.442 | -0.199 | 0.51 | 1 | 3.0 | 0.379 | 0.285 | 0.564 | 0.892 | 0.451 | 215 | 26 | 262 | 1 | 0 | 0 |
| updates | none | 8 | 241 | 477 | 0.432 | 0.419 | 0.446 | 0.50 | 0.442 | -0.199 | 0.51 | 1 | 3.0 | 0.379 | 0.285 | 0.564 | 0.892 | 0.451 | 215 | 26 | 262 | 1 | 0 | 0 |
| updates | none | 12 | 241 | 477 | 0.450 | 0.437 | 0.463 | 0.80 | 0.444 | -0.191 | 0.55 | 1 | 4.0 | 0.379 | 0.285 | 0.564 | 0.896 | 0.453 | 216 | 25 | 261 | 1 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 27; matched pairs: 214; unmatched reference entries: 27; unmatched candidate entries: 146
- identity switches: 1; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 25

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f152: ref 78914: 9 -> 28 at (821.5, 3257.5), 15 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 214 | 3 | 28 (135), 9 (79) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 10 | 57..75 | 19 | 0 | 19 |
| 14 | 96..96 | 1 | 0 | 1 |
| 15 | 100..100 | 1 | 0 | 1 |
| 17 | 109..109 | 1 | 0 | 1 |
| 19 | 110..116 | 7 | 0 | 7 |
| 20 | 114..116 | 3 | 0 | 3 |
| 21 | 121..122 | 2 | 0 | 2 |
| 22 | 122..150 | 29 | 0 | 28 |
| 23 | 125..126 | 2 | 0 | 2 |
| 24 | 127..127 | 1 | 0 | 1 |
| 27 | 146..146 | 1 | 0 | 1 |
| 29 | 160..160 | 1 | 0 | 1 |
| 31 | 182..189 | 8 | 0 | 4 |
| 32 | 186..186 | 1 | 0 | 1 |
| 33 | 191..197 | 7 | 0 | 3 |
| 34 | 192..194 | 3 | 0 | 3 |
| 35 | 201..222 | 22 | 0 | 22 |
| 36 | 206..208 | 3 | 0 | 2 |
| 39 | 233..233 | 1 | 0 | 1 |
| 40 | 246..246 | 1 | 0 | 1 |
| 43 | 268..269 | 2 | 0 | 2 |
| 44 | 271..271 | 1 | 0 | 1 |
| 46 | 273..293 | 21 | 0 | 21 |
| 47 | 273..273 | 1 | 0 | 1 |
| 51 | 288..291 | 4 | 0 | 4 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 1/2/145; tracks with internal gaps: 2; total internal gaps: 3; longest internal gap: 4; tracks ending in coasting: 26 (trailing rows total 136)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 9 | 54..143 | 90 | 85 | 79 | 6 | 1 | 3 | 3 | 78914 |
| 10 | 57..75 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 14 | 96..96 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 15 | 100..100 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 17 | 109..109 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 19 | 110..116 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 20 | 114..116 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 21 | 121..122 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 22 | 122..150 | 29 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 23 | 125..126 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 24 | 127..127 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 27 | 146..146 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 28 | 148..292 | 145 | 142 | 135 | 7 | 2 | 4 | 0 | 78914 |
| 29 | 160..160 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 31 | 182..189 | 8 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 32 | 186..186 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 33 | 191..197 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 34 | 192..194 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 35 | 201..222 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 36 | 206..208 | 3 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 39 | 233..233 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 40 | 246..246 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 43 | 268..269 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 44 | 271..271 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 46 | 273..293 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 47 | 273..273 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 51 | 288..291 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 27; matched pairs: 215; unmatched reference entries: 26; unmatched candidate entries: 262
- identity switches: 1; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 25

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f152: ref 78914: 9 -> 28 at (821.5, 3257.5), 15 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 215 | 3 | 28 (136), 9 (79) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 10 | 57..79 | 23 | 0 | 23 |
| 14 | 96..100 | 5 | 0 | 5 |
| 15 | 100..104 | 5 | 0 | 5 |
| 17 | 109..113 | 5 | 0 | 5 |
| 19 | 110..120 | 11 | 0 | 11 |
| 20 | 114..120 | 7 | 0 | 7 |
| 21 | 121..126 | 6 | 0 | 6 |
| 22 | 122..154 | 33 | 0 | 33 |
| 23 | 125..130 | 6 | 0 | 6 |
| 24 | 127..131 | 5 | 0 | 5 |
| 27 | 146..150 | 5 | 0 | 5 |
| 29 | 160..164 | 5 | 0 | 5 |
| 31 | 182..193 | 12 | 0 | 12 |
| 32 | 186..190 | 5 | 0 | 5 |
| 33 | 191..201 | 11 | 0 | 11 |
| 34 | 192..198 | 7 | 0 | 7 |
| 35 | 201..226 | 26 | 0 | 26 |
| 36 | 206..212 | 7 | 0 | 7 |
| 39 | 233..237 | 5 | 0 | 5 |
| 40 | 246..250 | 5 | 0 | 5 |
| 43 | 268..273 | 6 | 0 | 6 |
| 44 | 271..275 | 5 | 0 | 5 |
| 46 | 273..293 | 21 | 0 | 21 |
| 47 | 273..277 | 5 | 0 | 5 |
| 51 | 288..293 | 6 | 0 | 6 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 5/6/146; tracks with internal gaps: 2; total internal gaps: 3; longest internal gap: 6; tracks ending in coasting: 26 (trailing rows total 247)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 9 | 54..147 | 94 | 94 | 79 | 15 | 1 | 5 | 10 | 78914 |
| 10 | 57..79 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 14 | 96..100 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 15 | 100..104 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 17 | 109..113 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 19 | 110..120 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 20 | 114..120 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 21 | 121..126 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 22 | 122..154 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 23 | 125..130 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 24 | 127..131 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 27 | 146..150 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 28 | 148..293 | 146 | 146 | 136 | 10 | 2 | 6 | 0 | 78914 |
| 29 | 160..164 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 31 | 182..193 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 32 | 186..190 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 33 | 191..201 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 34 | 192..198 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 35 | 201..226 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 36 | 206..212 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 39 | 233..237 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 40 | 246..250 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 43 | 268..273 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 44 | 271..275 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 46 | 273..293 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 47 | 273..277 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 51 | 288..293 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
