# Tracker evaluation: claim = PARITY

Candidate: predictor=kit dataset=turbine video=20250920_063942_6C42 detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=cloud claim=parity curation=n/a

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
- reference: config_hash=44136fa355b3 git=none model=cloud-tracke
  - cloud_tracks_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/data/20250920_063942_6C42_cloud_reference_tracks.csv sha256=a6d520260c2db89f
  - video: data/20250920_063942_6C42.mp4 sha256=d16e8f3b6ae47c0f
  - note: stored output of the cloud tracking pipeline for the same frame window; a reference for parity only
  - note: confidence 1.0 on every row: the export carries no score
  - note: clip = frames 2000..2670 of the original recording 20250920_063942_6C42 (671 frames, renumbered 0..670; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}

## Metrics (center-distance matching)
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 0.722 | 0.918 | 0.353 | 0.09 | 0.730 | 0 | 7.0 |
| observations | none | 6 | 0.731 | 0.930 | 0.358 | 0.10 | 0.732 | 0 | 7.0 |
| observations | none | 8 | 0.732 | 0.931 | 0.358 | 0.10 | 0.732 | 0 | 7.0 |
| observations | none | 12 | 0.734 | 0.934 | 0.358 | 0.10 | 0.732 | 0 | 7.0 |
| updates | none | 4 | 0.353 | 0.676 | -2.836 | 0.09 | 0.314 | 0 | 8.0 |
| updates | none | 6 | 0.356 | 0.684 | -2.831 | 0.10 | 0.315 | 0 | 8.0 |
| updates | none | 8 | 0.357 | 0.684 | -2.831 | 0.10 | 0.315 | 0 | 8.0 |
| updates | none | 12 | 0.358 | 0.686 | -2.826 | 0.13 | 0.315 | 0 | 8.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 8; candidate ids: 35; matched pairs: 349; unmatched reference entries: 48; unmatched candidate entries: 207
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
| 4 | 25..26 | 2 | 0 | 2 |
| 6 | 35..35 | 1 | 0 | 1 |
| 7 | 42..42 | 1 | 0 | 1 |
| 8 | 46..62 | 17 | 0 | 2 |
| 11 | 58..86 | 29 | 0 | 19 |
| 18 | 111..116 | 6 | 0 | 6 |
| 19 | 115..116 | 2 | 0 | 2 |
| 20 | 122..146 | 25 | 0 | 3 |
| 22 | 126..144 | 19 | 0 | 5 |
| 41 | 269..269 | 1 | 0 | 1 |
| 44 | 274..295 | 22 | 0 | 21 |
| 49 | 289..306 | 18 | 0 | 5 |
| 52 | 322..322 | 1 | 0 | 1 |
| 54 | 349..367 | 19 | 0 | 19 |
| 55 | 352..355 | 4 | 0 | 3 |
| 58 | 359..364 | 6 | 0 | 6 |
| 61 | 361..385 | 25 | 0 | 14 |
| 62 | 370..387 | 18 | 0 | 4 |
| 67 | 422..428 | 7 | 0 | 7 |
| 68 | 424..441 | 18 | 0 | 17 |
| 73 | 446..446 | 1 | 0 | 1 |
| 76 | 453..468 | 16 | 0 | 4 |
| 79 | 482..487 | 6 | 0 | 6 |
| 86 | 522..556 | 35 | 0 | 14 |
| 87 | 523..562 | 40 | 0 | 5 |
| 94 | 547..617 | 71 | 0 | 20 |
| 99 | 594..598 | 5 | 0 | 5 |
| 107 | 622..670 | 49 | 0 | 5 |
| 110 | 649..650 | 2 | 0 | 2 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 1/18/238; tracks with internal gaps: 2; total internal gaps: 4; longest internal gap: 2; tracks ending in coasting: 29 (trailing rows total 201)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 4 | 25..26 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 6 | 35..35 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 7 | 42..42 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 8 | 46..62 | 17 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 10 | 55..292 | 238 | 225 | 225 | 0 | 0 | 0 | 0 | 372 |
| 11 | 58..86 | 29 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 18 | 111..116 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 19 | 115..116 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 20 | 122..146 | 25 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 21 | 123..160 | 38 | 29 | 25 | 4 | 2 | 2 | 0 | 381 |
| 22 | 126..144 | 19 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 30 | 193..222 | 30 | 25 | 25 | 0 | 0 | 0 | 0 | 390 |
| 41 | 269..269 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 44 | 274..295 | 22 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 49 | 289..306 | 18 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 52 | 322..322 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 54 | 349..367 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 55 | 352..355 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 58 | 359..364 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 61 | 361..385 | 25 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 62 | 370..387 | 18 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 67 | 422..428 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 68 | 424..441 | 18 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 73 | 446..446 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 76 | 453..468 | 16 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 79 | 482..487 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 80 | 484..514 | 31 | 25 | 25 | 0 | 0 | 0 | 0 | 440 |
| 86 | 522..556 | 35 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 87 | 523..562 | 40 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 94 | 547..617 | 71 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 97 | 558..587 | 30 | 25 | 23 | 2 | 2 | 1 | 0 | 458 |
| 99 | 594..598 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 107 | 622..670 | 49 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 109 | 630..670 | 41 | 26 | 26 | 0 | 0 | 0 | 0 | 468 |
| 110 | 649..650 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |

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
