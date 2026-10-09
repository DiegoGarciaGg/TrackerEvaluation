# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=gt config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=9a7b813bcc26
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/turbine/gt_default/tracks.csv sha256=add583f356515084
  - detections_csv: ground_truth/20250920_063942_6C42_detections_corrected.csv sha256=9a7b813bcc26a1cf
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gt_default
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
| observations | none | 4 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |
| observations | none | 6 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |
| observations | none | 8 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |
| observations | none | 12 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |
| updates | none | 4 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |
| updates | none | 6 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |
| updates | none | 8 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |
| updates | none | 12 | 241 | 239 | 0.992 | 0.992 | 0.992 | 0.00 | 0.992 | 0.992 | 0.00 | 0 | 0.0 | 0.996 | 1.000 | 0.992 | 0.992 | 1.000 | 239 | 2 | 0 | 1 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 1; candidate ids: 1; matched pairs: 239; unmatched reference entries: 2; unmatched candidate entries: 0
- identity switches: 0; fragmentation (coverage interruptions): 0; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 239 | 0 | 0 (239) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 1; lifespan min/median/max: 239/239/239; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 55..293 | 239 | 239 | 239 | 0 | 0 | 0 | 0 | 78914 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 1; candidate ids: 1; matched pairs: 239; unmatched reference entries: 2; unmatched candidate entries: 0
- identity switches: 0; fragmentation (coverage interruptions): 0; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78914 | 241 (53..293) | 239 | 0 | 0 (239) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 1; lifespan min/median/max: 239/239/239; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 55..293 | 239 | 239 | 239 | 0 | 0 | 0 | 0 | 78914 |
