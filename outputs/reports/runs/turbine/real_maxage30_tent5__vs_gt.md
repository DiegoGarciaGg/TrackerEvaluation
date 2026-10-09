# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 5}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=e28828c611e3 git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage30_tent5/tracks.csv sha256=c5c6b5c412d0789b
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage30_tent5
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
| observations | none | 4 | 241 | 308 | 0.679 | 0.585 | 0.787 | 0.41 | 0.726 | 0.473 | 0.46 | 0 | 3.0 | 0.769 | 0.685 | 0.876 | 0.876 | 0.685 | 211 | 30 | 97 | 1 | 0 | 0 |
| observations | none | 6 | 241 | 308 | 0.702 | 0.605 | 0.815 | 0.44 | 0.726 | 0.473 | 0.46 | 0 | 3.0 | 0.769 | 0.685 | 0.876 | 0.876 | 0.685 | 211 | 30 | 97 | 1 | 0 | 0 |
| observations | none | 8 | 241 | 308 | 0.710 | 0.611 | 0.824 | 0.45 | 0.726 | 0.473 | 0.46 | 0 | 3.0 | 0.769 | 0.685 | 0.876 | 0.876 | 0.685 | 211 | 30 | 97 | 1 | 0 | 0 |
| observations | none | 12 | 241 | 308 | 0.731 | 0.629 | 0.850 | 0.59 | 0.726 | 0.473 | 0.46 | 0 | 3.0 | 0.769 | 0.685 | 0.876 | 0.876 | 0.685 | 211 | 30 | 97 | 1 | 0 | 0 |
| updates | none | 4 | 241 | 509 | 0.523 | 0.370 | 0.740 | 0.42 | 0.556 | -0.361 | 0.46 | 0 | 3.0 | 0.563 | 0.415 | 0.876 | 0.876 | 0.415 | 211 | 30 | 298 | 1 | 0 | 0 |
| updates | none | 6 | 241 | 509 | 0.543 | 0.383 | 0.770 | 0.46 | 0.560 | -0.353 | 0.49 | 0 | 3.0 | 0.565 | 0.417 | 0.880 | 0.880 | 0.417 | 212 | 29 | 297 | 1 | 0 | 0 |
| updates | none | 8 | 241 | 509 | 0.550 | 0.387 | 0.781 | 0.49 | 0.560 | -0.353 | 0.49 | 0 | 3.0 | 0.565 | 0.417 | 0.880 | 0.880 | 0.417 | 212 | 29 | 297 | 1 | 0 | 0 |
| updates | none | 12 | 241 | 509 | 0.573 | 0.402 | 0.817 | 0.74 | 0.565 | -0.344 | 0.52 | 0 | 4.0 | 0.568 | 0.418 | 0.884 | 0.884 | 0.418 | 213 | 28 | 296 | 1 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 8; matched pairs: 211; unmatched reference entries: 30; unmatched candidate entries: 97
- identity switches: 0; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 7

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 211 | 3 | 10 (211) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 11 | 60..86 | 27 | 0 | 17 |
| 19 | 113..116 | 4 | 0 | 4 |
| 22 | 125..160 | 36 | 0 | 27 |
| 28 | 151..170 | 20 | 0 | 2 |
| 37 | 204..222 | 19 | 0 | 19 |
| 48 | 276..293 | 18 | 0 | 18 |
| 54 | 291..291 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 8; lifespan min/median/max: 1/20/236; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 3; tracks ending in coasting: 7 (trailing rows total 88)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 57..292 | 236 | 220 | 211 | 9 | 3 | 3 | 0 | 78914 |
| 11 | 60..86 | 27 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 19 | 113..116 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 22 | 125..160 | 36 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 28 | 151..170 | 20 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 37 | 204..222 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 48 | 276..293 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 54 | 291..291 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 8; matched pairs: 212; unmatched reference entries: 29; unmatched candidate entries: 297
- identity switches: 0; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 7

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 212 | 3 | 10 (212) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 11 | 60..115 | 56 | 0 | 56 |
| 19 | 113..145 | 33 | 0 | 33 |
| 22 | 125..189 | 65 | 0 | 65 |
| 28 | 151..199 | 49 | 0 | 49 |
| 37 | 204..251 | 48 | 0 | 48 |
| 48 | 276..293 | 18 | 0 | 18 |
| 54 | 291..293 | 3 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 8; lifespan min/median/max: 3/49/237; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 14; tracks ending in coasting: 7 (trailing rows total 272)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 57..293 | 237 | 237 | 212 | 25 | 3 | 14 | 0 | 78914 |
| 11 | 60..115 | 56 | 56 | 0 | 56 | 0 | 0 | 56 | - |
| 19 | 113..145 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 22 | 125..189 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 28 | 151..199 | 49 | 49 | 0 | 49 | 0 | 0 | 49 | - |
| 37 | 204..251 | 48 | 48 | 0 | 48 | 0 | 0 | 48 | - |
| 48 | 276..293 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 54 | 291..293 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
