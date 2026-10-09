# Tracker evaluation: claim = PARITY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=unknown config={}
Reference: predictor=cloud claim=parity curation=n/a

## Provenance
- candidate: config_hash=44136fa355b3 git=none model=unknown
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/results/turbine/baseline_tracks.csv sha256=f4fc4bab19093488
  - tracker/ hash=7b65976a888fbd3c coasting_known=False
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: 6-column format: coasting rows unknown, every row counted as an observation
  - note: frozen_baseline
  - note: clip = frames 2000..2670 of the original recording 20250920_063942_6C42 (671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)
- reference: config_hash=44136fa355b3 git=none model=cloud-tracke
  - cloud_tracks_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/data/20250920_063942_6C42_cloud_reference_tracks.csv sha256=a6d520260c2db89f
  - note: stored output of the cloud tracking pipeline for the same frame window; a reference for parity only
  - note: confidence 1.0 on every row: the export carries no score
  - note: clip = frames 2000..2670 of the original recording 20250920_063942_6C42 (671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}
- candidate is in the 6-column baseline format: coasting rows are indistinguishable, so only the 'updates' view (every row as written) is scored; matched-rows-only needs the 10-column format

## Metrics (center-distance matching)
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| updates | none | 4 | 0.353 | 0.676 | -2.836 | 0.09 | 0.314 | 0 | 8.0 |
| updates | none | 6 | 0.356 | 0.684 | -2.831 | 0.10 | 0.315 | 0 | 8.0 |
| updates | none | 8 | 0.357 | 0.684 | -2.831 | 0.10 | 0.315 | 0 | 8.0 |
| updates | none | 12 | 0.358 | 0.686 | -2.826 | 0.13 | 0.315 | 0 | 8.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 8; candidate ids: 35; matched pairs: 349; unmatched reference entries: 48; unmatched candidate entries: 1473
- identity switches: 0; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 29

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- none

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 363 | 4 (0..13) | 0 | 0 |  |
| 353 | 21 (20..118) | 0 | 0 |  |
| 372 | 227 (53..292) | 225 | 0 | 10 (225) |
| 381 | 35 (121..168) | 25 | 1 | 21 (25) |
| 390 | 27 (191..222) | 25 | 0 | 30 (25) |
| 440 | 27 (482..514) | 25 | 0 | 80 (25) |
| 458 | 27 (556..590) | 23 | 1 | 97 (23) |
| 468 | 29 (628..670) | 26 | 1 | 109 (26) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 4 | 25..55 | 31 | 0 | 31 |
| 6 | 35..64 | 30 | 0 | 30 |
| 7 | 42..71 | 30 | 0 | 30 |
| 8 | 46..91 | 46 | 0 | 46 |
| 11 | 58..115 | 58 | 0 | 58 |
| 18 | 111..145 | 35 | 0 | 35 |
| 19 | 115..145 | 31 | 0 | 31 |
| 20 | 122..175 | 54 | 0 | 54 |
| 22 | 126..173 | 48 | 0 | 48 |
| 41 | 269..298 | 30 | 0 | 30 |
| 44 | 274..324 | 51 | 0 | 51 |
| 49 | 289..335 | 47 | 0 | 47 |
| 52 | 322..351 | 30 | 0 | 30 |
| 54 | 349..396 | 48 | 0 | 48 |
| 55 | 352..384 | 33 | 0 | 33 |
| 58 | 359..393 | 35 | 0 | 35 |
| 61 | 361..414 | 54 | 0 | 54 |
| 62 | 370..416 | 47 | 0 | 47 |
| 67 | 422..457 | 36 | 0 | 36 |
| 68 | 424..470 | 47 | 0 | 47 |
| 73 | 446..475 | 30 | 0 | 30 |
| 76 | 453..497 | 45 | 0 | 45 |
| 79 | 482..516 | 35 | 0 | 35 |
| 86 | 522..585 | 64 | 0 | 64 |
| 87 | 523..591 | 69 | 0 | 69 |
| 94 | 547..646 | 100 | 0 | 100 |
| 99 | 594..627 | 34 | 0 | 34 |
| 107 | 622..670 | 49 | 0 | 49 |
| 110 | 649..670 | 22 | 0 | 22 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 22/47/267; tracks with internal gaps: 6; total internal gaps: 13; longest internal gap: 10; tracks ending in coasting: 34 (trailing rows total 1414)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 4 | 25..55 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 6 | 35..64 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 7 | 42..71 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 8 | 46..91 | 46 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 10 | 55..321 | 267 | 267 | 225 | 42 | 3 | 8 | 29 | 372 |
| 11 | 58..115 | 58 | 58 | 0 | 58 | 0 | 0 | 58 | - |
| 18 | 111..145 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 19 | 115..145 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 20 | 122..175 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |
| 21 | 123..189 | 67 | 67 | 25 | 42 | 4 | 8 | 29 | 381 |
| 22 | 126..173 | 48 | 48 | 0 | 48 | 0 | 0 | 48 | - |
| 30 | 193..251 | 59 | 59 | 25 | 34 | 1 | 5 | 29 | 390 |
| 41 | 269..298 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 44 | 274..324 | 51 | 51 | 0 | 51 | 0 | 0 | 51 | - |
| 49 | 289..335 | 47 | 47 | 0 | 47 | 0 | 0 | 47 | - |
| 52 | 322..351 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 54 | 349..396 | 48 | 48 | 0 | 48 | 0 | 0 | 48 | - |
| 55 | 352..384 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 58 | 359..393 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 61 | 361..414 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |
| 62 | 370..416 | 47 | 47 | 0 | 47 | 0 | 0 | 47 | - |
| 67 | 422..457 | 36 | 36 | 0 | 36 | 0 | 0 | 36 | - |
| 68 | 424..470 | 47 | 47 | 0 | 47 | 0 | 0 | 47 | - |
| 73 | 446..475 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 76 | 453..497 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 79 | 482..516 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 80 | 484..543 | 60 | 60 | 25 | 35 | 1 | 6 | 29 | 440 |
| 86 | 522..585 | 64 | 64 | 0 | 64 | 0 | 0 | 64 | - |
| 87 | 523..591 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 94 | 547..646 | 100 | 100 | 0 | 100 | 0 | 0 | 100 | - |
| 97 | 558..616 | 59 | 59 | 23 | 36 | 2 | 6 | 29 | 458 |
| 99 | 594..627 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 107 | 622..670 | 49 | 49 | 0 | 49 | 0 | 0 | 49 | - |
| 109 | 630..670 | 41 | 41 | 26 | 15 | 2 | 10 | 0 | 468 |
| 110 | 649..670 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
