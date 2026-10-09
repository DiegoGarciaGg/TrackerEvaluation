# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 5, "tentative_threshold": 5}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=679e182e4d04 git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage5_tent5/tracks.csv sha256=9b429b731f70d16f
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage5_tent5
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
| observations | none | 4 | 241 | 304 | 0.507 | 0.592 | 0.434 | 0.41 | 0.541 | 0.485 | 0.46 | 1 | 3.0 | 0.495 | 0.444 | 0.560 | 0.876 | 0.694 | 211 | 30 | 93 | 1 | 0 | 0 |
| observations | none | 6 | 241 | 304 | 0.524 | 0.612 | 0.449 | 0.44 | 0.541 | 0.485 | 0.46 | 1 | 3.0 | 0.495 | 0.444 | 0.560 | 0.876 | 0.694 | 211 | 30 | 93 | 1 | 0 | 0 |
| observations | none | 8 | 241 | 304 | 0.530 | 0.618 | 0.453 | 0.45 | 0.541 | 0.485 | 0.46 | 1 | 3.0 | 0.495 | 0.444 | 0.560 | 0.876 | 0.694 | 211 | 30 | 93 | 1 | 0 | 0 |
| observations | none | 12 | 241 | 304 | 0.544 | 0.637 | 0.465 | 0.59 | 0.541 | 0.485 | 0.46 | 1 | 3.0 | 0.495 | 0.444 | 0.560 | 0.876 | 0.694 | 211 | 30 | 93 | 1 | 0 | 0 |
| updates | none | 4 | 241 | 336 | 0.481 | 0.542 | 0.427 | 0.42 | 0.511 | 0.353 | 0.46 | 1 | 3.0 | 0.468 | 0.402 | 0.560 | 0.876 | 0.628 | 211 | 30 | 125 | 1 | 0 | 0 |
| updates | none | 6 | 241 | 336 | 0.499 | 0.563 | 0.443 | 0.46 | 0.516 | 0.361 | 0.49 | 1 | 3.0 | 0.471 | 0.405 | 0.564 | 0.880 | 0.631 | 212 | 29 | 124 | 1 | 0 | 0 |
| updates | none | 8 | 241 | 336 | 0.505 | 0.570 | 0.448 | 0.49 | 0.516 | 0.361 | 0.49 | 1 | 3.0 | 0.471 | 0.405 | 0.564 | 0.880 | 0.631 | 212 | 29 | 124 | 1 | 0 | 0 |
| updates | none | 12 | 241 | 336 | 0.525 | 0.594 | 0.463 | 0.74 | 0.518 | 0.369 | 0.52 | 1 | 4.0 | 0.471 | 0.405 | 0.564 | 0.884 | 0.634 | 213 | 28 | 123 | 1 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 8; matched pairs: 211; unmatched reference entries: 30; unmatched candidate entries: 93
- identity switches: 1; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 6

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f152: ref 78914: 10 -> 29 at (821.5, 3257.5), 15 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 211 | 3 | 29 (135), 10 (76) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 11 | 60..75 | 16 | 0 | 16 |
| 20 | 113..116 | 4 | 0 | 4 |
| 23 | 125..150 | 26 | 0 | 25 |
| 40 | 204..222 | 19 | 0 | 19 |
| 51 | 276..293 | 18 | 0 | 18 |
| 57 | 291..291 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 8; lifespan min/median/max: 1/19/142; tracks with internal gaps: 2; total internal gaps: 3; longest internal gap: 3; tracks ending in coasting: 7 (trailing rows total 86)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 57..143 | 87 | 82 | 76 | 6 | 1 | 3 | 3 | 78914 |
| 11 | 60..75 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 20 | 113..116 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 23 | 125..150 | 26 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 29 | 151..292 | 142 | 139 | 135 | 4 | 2 | 3 | 0 | 78914 |
| 40 | 204..222 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 51 | 276..293 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 57 | 291..291 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 8; matched pairs: 212; unmatched reference entries: 29; unmatched candidate entries: 124
- identity switches: 1; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 6

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f152: ref 78914: 10 -> 29 at (821.5, 3257.5), 15 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 212 | 3 | 29 (136), 10 (76) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 11 | 60..79 | 20 | 0 | 20 |
| 20 | 113..120 | 8 | 0 | 8 |
| 23 | 125..154 | 30 | 0 | 30 |
| 40 | 204..226 | 23 | 0 | 23 |
| 51 | 276..293 | 18 | 0 | 18 |
| 57 | 291..293 | 3 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 8; lifespan min/median/max: 3/23/143; tracks with internal gaps: 2; total internal gaps: 3; longest internal gap: 6; tracks ending in coasting: 7 (trailing rows total 112)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 57..147 | 91 | 91 | 76 | 15 | 1 | 5 | 10 | 78914 |
| 11 | 60..79 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 20 | 113..120 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 23 | 125..154 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 29 | 151..293 | 143 | 143 | 136 | 7 | 2 | 6 | 0 | 78914 |
| 40 | 204..226 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 51 | 276..293 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 57 | 291..293 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
