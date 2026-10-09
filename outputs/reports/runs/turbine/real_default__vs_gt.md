# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_default/tracks.csv sha256=e2d85e82bb596331
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_default
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
| observations | none | 4 | 241 | 339 | 0.652 | 0.543 | 0.782 | 0.42 | 0.693 | 0.353 | 0.46 | 0 | 3.0 | 0.731 | 0.625 | 0.880 | 0.880 | 0.625 | 212 | 29 | 127 | 1 | 0 | 0 |
| observations | none | 6 | 241 | 339 | 0.675 | 0.562 | 0.811 | 0.45 | 0.699 | 0.361 | 0.48 | 0 | 3.0 | 0.734 | 0.628 | 0.884 | 0.884 | 0.628 | 213 | 28 | 126 | 1 | 0 | 0 |
| observations | none | 8 | 241 | 339 | 0.682 | 0.567 | 0.821 | 0.46 | 0.699 | 0.361 | 0.48 | 0 | 3.0 | 0.734 | 0.628 | 0.884 | 0.884 | 0.628 | 213 | 28 | 126 | 1 | 0 | 0 |
| observations | none | 12 | 241 | 339 | 0.707 | 0.589 | 0.850 | 0.68 | 0.699 | 0.361 | 0.48 | 0 | 3.0 | 0.734 | 0.628 | 0.884 | 0.884 | 0.628 | 213 | 28 | 126 | 1 | 0 | 0 |
| updates | none | 4 | 241 | 714 | 0.451 | 0.272 | 0.747 | 0.43 | 0.475 | -1.203 | 0.46 | 0 | 3.0 | 0.444 | 0.297 | 0.880 | 0.880 | 0.297 | 212 | 29 | 502 | 1 | 0 | 0 |
| updates | none | 6 | 241 | 714 | 0.470 | 0.283 | 0.780 | 0.50 | 0.486 | -1.178 | 0.52 | 0 | 4.0 | 0.450 | 0.301 | 0.892 | 0.892 | 0.301 | 215 | 26 | 499 | 1 | 0 | 0 |
| updates | none | 8 | 241 | 714 | 0.477 | 0.287 | 0.793 | 0.54 | 0.486 | -1.178 | 0.52 | 0 | 4.0 | 0.450 | 0.301 | 0.892 | 0.892 | 0.301 | 215 | 26 | 499 | 1 | 0 | 0 |
| updates | none | 12 | 241 | 714 | 0.498 | 0.298 | 0.834 | 0.83 | 0.493 | -1.162 | 0.63 | 2 | 4.0 | 0.454 | 0.304 | 0.900 | 0.905 | 0.305 | 218 | 23 | 496 | 1 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

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
