# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 2}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=55dda32e8049 git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage30_tent2/tracks.csv sha256=cbad470e2a87f02b
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage30_tent2
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
| observations | none | 4 | 241 | 373 | 0.626 | 0.500 | 0.785 | 0.42 | 0.667 | 0.220 | 0.47 | 0 | 4.0 | 0.694 | 0.571 | 0.884 | 0.884 | 0.571 | 213 | 28 | 160 | 1 | 0 | 0 |
| observations | none | 6 | 241 | 373 | 0.649 | 0.517 | 0.814 | 0.45 | 0.673 | 0.228 | 0.49 | 0 | 3.0 | 0.697 | 0.574 | 0.888 | 0.888 | 0.574 | 214 | 27 | 159 | 1 | 0 | 0 |
| observations | none | 8 | 241 | 373 | 0.656 | 0.523 | 0.824 | 0.46 | 0.673 | 0.228 | 0.49 | 0 | 3.0 | 0.697 | 0.574 | 0.888 | 0.888 | 0.574 | 214 | 27 | 159 | 1 | 0 | 0 |
| observations | none | 12 | 241 | 373 | 0.680 | 0.542 | 0.853 | 0.68 | 0.673 | 0.228 | 0.49 | 0 | 3.0 | 0.697 | 0.574 | 0.888 | 0.888 | 0.574 | 214 | 27 | 159 | 1 | 0 | 0 |
| updates | none | 4 | 241 | 1057 | 0.374 | 0.187 | 0.750 | 0.44 | 0.395 | -2.618 | 0.47 | 0 | 4.0 | 0.328 | 0.202 | 0.884 | 0.884 | 0.202 | 213 | 28 | 844 | 1 | 0 | 0 |
| updates | none | 6 | 241 | 1057 | 0.390 | 0.194 | 0.783 | 0.51 | 0.403 | -2.593 | 0.53 | 0 | 4.0 | 0.333 | 0.204 | 0.896 | 0.896 | 0.204 | 216 | 25 | 841 | 1 | 0 | 0 |
| updates | none | 8 | 241 | 1057 | 0.396 | 0.197 | 0.796 | 0.55 | 0.403 | -2.593 | 0.53 | 0 | 4.0 | 0.333 | 0.204 | 0.896 | 0.896 | 0.204 | 216 | 25 | 841 | 1 | 0 | 0 |
| updates | none | 12 | 241 | 1057 | 0.413 | 0.204 | 0.838 | 0.84 | 0.409 | -2.577 | 0.64 | 2 | 4.0 | 0.336 | 0.206 | 0.905 | 0.909 | 0.207 | 219 | 22 | 838 | 1 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 19; matched pairs: 214; unmatched reference entries: 27; unmatched candidate entries: 159
- identity switches: 0; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 18

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 214 | 3 | 7 (214) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 8 | 57..86 | 30 | 0 | 20 |
| 4 | 62..62 | 1 | 0 | 1 |
| 2 | 70..146 | 77 | 0 | 10 |
| 9 | 100..100 | 1 | 0 | 1 |
| 11 | 110..116 | 7 | 0 | 7 |
| 13 | 114..116 | 3 | 0 | 3 |
| 14 | 122..160 | 39 | 0 | 30 |
| 15 | 125..144 | 20 | 0 | 6 |
| 16 | 127..127 | 1 | 0 | 1 |
| 18 | 182..189 | 8 | 0 | 4 |
| 19 | 186..186 | 1 | 0 | 1 |
| 20 | 191..205 | 15 | 0 | 4 |
| 21 | 192..222 | 31 | 0 | 26 |
| 26 | 233..271 | 39 | 0 | 5 |
| 29 | 268..269 | 2 | 0 | 2 |
| 31 | 273..293 | 21 | 0 | 21 |
| 32 | 273..273 | 1 | 0 | 1 |
| 36 | 288..291 | 4 | 0 | 4 |

### Gaps and durations of candidate tracks
- tracks: 19; lifespan min/median/max: 1/8/239; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 6; tracks ending in coasting: 18 (trailing rows total 147)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 7 | 54..292 | 239 | 226 | 214 | 12 | 3 | 6 | 0 | 78914 |
| 8 | 57..86 | 30 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 4 | 62..62 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 2 | 70..146 | 77 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 9 | 100..100 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 11 | 110..116 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 13 | 114..116 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 14 | 122..160 | 39 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 15 | 125..144 | 20 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 16 | 127..127 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 18 | 182..189 | 8 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 19 | 186..186 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 20 | 191..205 | 15 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 21 | 192..222 | 31 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 26 | 233..271 | 39 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 29 | 268..269 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 31 | 273..293 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 32 | 273..273 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 36 | 288..291 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 22; matched pairs: 216; unmatched reference entries: 25; unmatched candidate entries: 841
- identity switches: 0; fragmentation (coverage interruptions): 4; orphan candidate ids (never on a reference object): 21

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 216 | 4 | 7 (216) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 2 | 53..175 | 123 | 0 | 123 |
| 3 | 53..55 | 3 | 0 | 3 |
| 4 | 53..91 | 39 | 0 | 39 |
| 5 | 53..71 | 19 | 0 | 19 |
| 6 | 53..75 | 23 | 0 | 23 |
| 8 | 57..115 | 59 | 0 | 59 |
| 9 | 100..129 | 30 | 0 | 30 |
| 11 | 110..145 | 36 | 0 | 36 |
| 13 | 114..145 | 32 | 0 | 32 |
| 14 | 122..189 | 68 | 0 | 68 |
| 15 | 125..173 | 49 | 0 | 49 |
| 16 | 127..156 | 30 | 0 | 30 |
| 18 | 182..218 | 37 | 0 | 37 |
| 19 | 186..215 | 30 | 0 | 30 |
| 20 | 191..234 | 44 | 0 | 44 |
| 21 | 192..251 | 60 | 0 | 60 |
| 26 | 233..293 | 61 | 0 | 61 |
| 29 | 268..293 | 26 | 0 | 26 |
| 31 | 273..293 | 21 | 0 | 21 |
| 32 | 273..293 | 21 | 0 | 21 |
| 36 | 288..293 | 6 | 0 | 6 |

### Gaps and durations of candidate tracks
- tracks: 22; lifespan min/median/max: 3/36/240; tracks with internal gaps: 1; total internal gaps: 4; longest internal gap: 11; tracks ending in coasting: 21 (trailing rows total 817)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 53..175 | 123 | 123 | 0 | 123 | 0 | 0 | 123 | - |
| 3 | 53..55 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 4 | 53..91 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 5 | 53..71 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 6 | 53..75 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 7 | 54..293 | 240 | 240 | 216 | 24 | 4 | 11 | 0 | 78914 |
| 8 | 57..115 | 59 | 59 | 0 | 59 | 0 | 0 | 59 | - |
| 9 | 100..129 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 11 | 110..145 | 36 | 36 | 0 | 36 | 0 | 0 | 36 | - |
| 13 | 114..145 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 14 | 122..189 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 15 | 125..173 | 49 | 49 | 0 | 49 | 0 | 0 | 49 | - |
| 16 | 127..156 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 18 | 182..218 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 19 | 186..215 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 20 | 191..234 | 44 | 44 | 0 | 44 | 0 | 0 | 44 | - |
| 21 | 192..251 | 60 | 60 | 0 | 60 | 0 | 0 | 60 | - |
| 26 | 233..293 | 61 | 61 | 0 | 61 | 0 | 0 | 61 | - |
| 29 | 268..293 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 31 | 273..293 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 32 | 273..293 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 36 | 288..293 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
