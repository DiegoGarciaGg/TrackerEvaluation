# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 15, "tentative_threshold": 5}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=8ba9d6b50d24 git=none model=8f211754bc50
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/real_maxage15_tent5/tracks.csv sha256=569f674547f89187
  - detections_csv: data/20250920_063942_6C42_detections.csv sha256=8f211754bc5052c1
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage15_tent5
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
| observations | none | 4 | 0.680 | 0.787 | 0.477 | 0.46 | 0.770 | 0 | 3.0 |
| observations | none | 6 | 0.703 | 0.815 | 0.477 | 0.46 | 0.770 | 0 | 3.0 |
| observations | none | 8 | 0.711 | 0.824 | 0.477 | 0.46 | 0.770 | 0 | 3.0 |
| observations | none | 12 | 0.732 | 0.850 | 0.477 | 0.46 | 0.770 | 0 | 3.0 |
| updates | none | 4 | 0.575 | 0.740 | 0.029 | 0.46 | 0.643 | 0 | 3.0 |
| updates | none | 6 | 0.597 | 0.770 | 0.037 | 0.49 | 0.646 | 0 | 3.0 |
| updates | none | 8 | 0.605 | 0.781 | 0.037 | 0.49 | 0.646 | 0 | 3.0 |
| updates | none | 12 | 0.631 | 0.817 | 0.046 | 0.52 | 0.649 | 0 | 4.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 8; matched pairs: 211; unmatched reference entries: 30; unmatched candidate entries: 96
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
| 28 | 151..151 | 1 | 0 | 1 |
| 38 | 204..222 | 19 | 0 | 19 |
| 49 | 276..293 | 18 | 0 | 18 |
| 55 | 291..291 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 8; lifespan min/median/max: 1/19/236; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 3; tracks ending in coasting: 7 (trailing rows total 87)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 57..292 | 236 | 220 | 211 | 9 | 3 | 3 | 0 | 78914 |
| 11 | 60..86 | 27 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 19 | 113..116 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 22 | 125..160 | 36 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 28 | 151..151 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 38 | 204..222 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 49 | 276..293 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 55 | 291..291 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 8; matched pairs: 212; unmatched reference entries: 29; unmatched candidate entries: 203
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
| 11 | 60..100 | 41 | 0 | 41 |
| 19 | 113..130 | 18 | 0 | 18 |
| 22 | 125..174 | 50 | 0 | 50 |
| 28 | 151..165 | 15 | 0 | 15 |
| 38 | 204..236 | 33 | 0 | 33 |
| 49 | 276..293 | 18 | 0 | 18 |
| 55 | 291..293 | 3 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 8; lifespan min/median/max: 3/33/237; tracks with internal gaps: 1; total internal gaps: 3; longest internal gap: 14; tracks ending in coasting: 7 (trailing rows total 178)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 57..293 | 237 | 237 | 212 | 25 | 3 | 14 | 0 | 78914 |
| 11 | 60..100 | 41 | 41 | 0 | 41 | 0 | 0 | 41 | - |
| 19 | 113..130 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 22 | 125..174 | 50 | 50 | 0 | 50 | 0 | 0 | 50 | - |
| 28 | 151..165 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 38 | 204..236 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 49 | 276..293 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 55 | 291..293 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
