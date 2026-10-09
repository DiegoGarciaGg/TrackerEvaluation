# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=902be54c9776
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise0.0_fp0.0_seed1/tracks.csv sha256=71b78497830922ca
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise0.0_fp0.0_seed1.csv sha256=902be54c97764ac7
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise0.0_fp0.0_seed1
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- reference: config_hash=44136fa355b3 git=none model=gt
  - gt_tracks_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv sha256=a89c6bc9f4e8148d
  - gt_detections_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20251012_164031_1DAC_detections_corrected.csv sha256=503255dd69b114a5
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - note: confidence 1.0 on every box: labels carry no score
  - note: track_id is the annotator's obj_id as text
  - note: companion detections CSV holds the same boxes without ids (0 row mismatches)
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}
- ignore region 'burnt-in timestamp overlay, top-left': entries with center inside it are dropped on both sides before scoring

## Metrics (center-distance matching)
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 0.803 | 0.725 | 0.879 | 0.01 | 0.873 | 150 | 959.0 |
| observations | none | 6 | 0.803 | 0.729 | 0.879 | 0.01 | 0.873 | 145 | 958.0 |
| observations | none | 8 | 0.802 | 0.740 | 0.879 | 0.01 | 0.874 | 145 | 959.0 |
| observations | none | 12 | 0.807 | 0.752 | 0.879 | 0.09 | 0.877 | 126 | 954.0 |
| observations | ignore | 4 | 0.803 | 0.725 | 0.879 | 0.01 | 0.873 | 150 | 959.0 |
| observations | ignore | 6 | 0.803 | 0.729 | 0.879 | 0.01 | 0.873 | 145 | 958.0 |
| observations | ignore | 8 | 0.802 | 0.740 | 0.879 | 0.01 | 0.874 | 145 | 959.0 |
| observations | ignore | 12 | 0.807 | 0.752 | 0.879 | 0.09 | 0.877 | 126 | 954.0 |
| updates | none | 4 | 0.724 | 0.659 | 0.728 | 0.06 | 0.812 | 162 | 896.0 |
| updates | none | 6 | 0.757 | 0.693 | 0.793 | 0.23 | 0.842 | 160 | 603.0 |
| updates | none | 8 | 0.775 | 0.720 | 0.871 | 0.49 | 0.878 | 145 | 251.0 |
| updates | none | 12 | 0.798 | 0.749 | 0.885 | 0.63 | 0.888 | 131 | 185.0 |
| updates | ignore | 4 | 0.724 | 0.659 | 0.728 | 0.06 | 0.812 | 162 | 896.0 |
| updates | ignore | 6 | 0.757 | 0.693 | 0.793 | 0.23 | 0.842 | 160 | 603.0 |
| updates | ignore | 8 | 0.775 | 0.720 | 0.871 | 0.49 | 0.878 | 145 | 251.0 |
| updates | ignore | 12 | 0.798 | 0.749 | 0.885 | 0.63 | 0.888 | 131 | 185.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9062; unmatched reference entries: 1080; unmatched candidate entries: 0
- identity switches: 145; fragmentation (coverage interruptions): 930; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 1 -> 2 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 4 -> 3 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 3 -> 5 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 5 -> 1 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 1 -> 7 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 3 -> 5 at (2099, 3033.5), 2 frames after previous cover
- f97: ref 78897: 6 -> 3 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 8 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 4 -> 8 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 6 -> 3 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 8 -> 6 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 5 -> 10 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 3 -> 5 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 8 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 9 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 5 -> 10 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 6 -> 3 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 1 -> 7 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 10 -> 1 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 3 -> 6 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 3 -> 5 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 7 -> 1 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 1 -> 10 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 6 -> 3 at (2088, 3029), 1 frames after previous cover
- f106: ref 79102: 8 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 8 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 9 -> 4 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 6 -> 3 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 5 -> 13 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 13 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 5 -> 13 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 14 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 10 -> 2 at (2000.5, 3033.5), 5 frames after previous cover
- f110: ref 79097: 3 -> 5 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 3 -> 15 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 6 -> 3 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 8 -> 6 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 4 -> 8 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 9 -> 4 at (2118, 3025), 4 frames after previous cover
- f110: ref 79110: 9 -> 16 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 2 -> 18 at (1928, 3035), 4 frames after previous cover
- f118: ref 79105: 8 -> 6 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 4 -> 8 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 16 -> 4 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 9 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 9 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 19 -> 17 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 6 -> 8 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 8 -> 4 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 10 -> 14 at (1966, 3033.5), 1 frames after previous cover
- f120: ref 78899: 13 -> 10 at (1982.5, 3033.5), 1 frames after previous cover
- f120: ref 79037: 14 -> 2 at (1951, 3035), 1 frames after previous cover
- f120: ref 79045: 2 -> 1 at (1938, 3036.5), 1 frames after previous cover
- f120: ref 79097: 5 -> 13 at (1998, 3031), 1 frames after previous cover
- ... 85 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 898 | 97 | 0 (898) |
| 78896 | 350 (76..429) | 312 | 29 | 18 (283), 2 (27), 1 (2) |
| 78969 | 352 (80..434) | 316 | 27 | 22 (279), 7 (26), 1 (11) |
| 78971 | 352 (84..439) | 313 | 32 | 20 (266), 1 (31), 7 (11), 3 (2), 5 (2), 22 (1) |
| 79045 | 355 (84..443) | 309 | 32 | 7 (275), 2 (9), 20 (7), 5 (6), 1 (5), 3 (3), 10 (3), 4 (1) |
| 79037 | 355 (86..445) | 313 | 38 | 2 (279), 14 (9), 10 (7), 3 (4), 5 (4), 1 (4), 20 (3), 4 (2), 7 (1) |
| 78897 | 345 (89..450) | 307 | 33 | 1 (276), 10 (8), 6 (6), 2 (4), 5 (3), 14 (3), 4 (2), 3 (2), 13 (2), 20 (1) |
| 78899 | 365 (91..455) | 332 | 27 | 14 (301), 13 (10), 3 (5), 5 (5), 4 (3), 2 (3), 6 (2), 8 (1), 10 (1), 1 (1) |
| 79097 | 366 (94..461) | 330 | 33 | 10 (294), 5 (10), 21 (8), 14 (5), 6 (4), 4 (3), 3 (3), 8 (2), 13 (1) |
| 79098 | 360 (97..467) | 321 | 35 | 21 (290), 15 (9), 10 (7), 5 (5), 6 (3), 3 (3), 4 (2), 8 (2) |
| 79102 | 371 (98..477) | 332 | 35 | 5 (304), 3 (10), 10 (5), 8 (4), 6 (3), 4 (2), 15 (2), 13 (2) |
| 79103 | 380 (99..481) | 329 | 40 | 26 (291), 6 (9), 13 (8), 4 (5), 5 (5), 8 (4), 10 (3), 15 (2), 9 (1), 3 (1) |
| 79105 | 379 (101..484) | 340 | 37 | 13 (314), 8 (9), 15 (8), 4 (3), 9 (2), 6 (2), 3 (2) |
| 79108 | 385 (104..492) | 347 | 32 | 15 (323), 4 (8), 3 (8), 9 (3), 6 (3), 8 (2) |
| 79110 | 388 (106..497) | 343 | 42 | 3 (323), 16 (7), 6 (7), 8 (3), 9 (2), 4 (1) |
| 79111 | 386 (109..500) | 363 | 21 | 6 (342), 9 (8), 8 (7), 4 (4), 16 (2) |
| 79115 | 421 (111..531) | 373 | 43 | 8 (355), 4 (7), 17 (5), 16 (4), 9 (2) |
| 79116 | 411 (114..530) | 366 | 41 | 4 (352), 16 (6), 9 (4), 19 (2), 17 (2) |
| 79122 | 404 (118..532) | 366 | 35 | 16 (353), 9 (7), 17 (4), 19 (2) |
| 79132 | 391 (120..515) | 351 | 37 | 9 (339), 17 (7), 19 (4), 4 (1) |
| 79128 | 402 (124..527) | 357 | 43 | 17 (352), 19 (5) |
| 79134 | 407 (127..533) | 354 | 43 | 24 (349), 19 (5) |
| 79135 | 409 (129..542) | 376 | 31 | 19 (299), 25 (72), 23 (5) |
| 79139 | 406 (132..537) | 362 | 36 | 23 (299), 19 (63) |
| 79136 | 393 (136..538) | 352 | 31 | 25 (290), 23 (62) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 307/389/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 898 | 898 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..450 | 373 | 330 | 330 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 2 | 83..445 | 363 | 322 | 322 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 79037, 79045 |
| 3 | 86..497 | 412 | 366 | 366 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 86..530 | 445 | 396 | 396 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 5 | 89..477 | 389 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 6 | 91..500 | 410 | 381 | 381 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 7 | 94..443 | 350 | 313 | 313 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 8 | 96..531 | 436 | 389 | 389 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 9 | 100..515 | 416 | 368 | 368 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 100..461 | 362 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 108..484 | 377 | 337 | 337 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103, 79105 |
| 14 | 110..455 | 346 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 15 | 110..492 | 383 | 344 | 344 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 16 | 110..532 | 423 | 372 | 372 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 17 | 113..527 | 415 | 370 | 370 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 18 | 113..429 | 317 | 283 | 283 | 0 | 0 | 0 | 0 | 78896 |
| 19 | 116..537 | 422 | 380 | 380 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 124..439 | 316 | 277 | 277 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045 |
| 21 | 124..467 | 344 | 298 | 298 | 0 | 0 | 0 | 0 | 79097, 79098 |
| 22 | 128..434 | 307 | 280 | 280 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 23 | 129..538 | 410 | 366 | 366 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 24 | 137..533 | 397 | 349 | 349 | 0 | 0 | 0 | 0 | 79134 |
| 25 | 138..542 | 405 | 362 | 362 | 0 | 0 | 0 | 0 | 79135, 79136 |
| 26 | 144..481 | 338 | 291 | 291 | 0 | 0 | 0 | 0 | 79103 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9062; unmatched reference entries: 1080; unmatched candidate entries: 0
- identity switches: 145; fragmentation (coverage interruptions): 930; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 1 -> 2 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 4 -> 3 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 3 -> 5 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 5 -> 1 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 1 -> 7 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 3 -> 5 at (2099, 3033.5), 2 frames after previous cover
- f97: ref 78897: 6 -> 3 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 8 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 4 -> 8 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 6 -> 3 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 8 -> 6 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 5 -> 10 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 3 -> 5 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 8 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 9 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 5 -> 10 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 6 -> 3 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 1 -> 7 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 10 -> 1 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 3 -> 6 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 3 -> 5 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 7 -> 1 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 1 -> 10 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 6 -> 3 at (2088, 3029), 1 frames after previous cover
- f106: ref 79102: 8 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 8 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 9 -> 4 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 6 -> 3 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 5 -> 13 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 13 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 5 -> 13 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 14 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 10 -> 2 at (2000.5, 3033.5), 5 frames after previous cover
- f110: ref 79097: 3 -> 5 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 3 -> 15 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 6 -> 3 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 8 -> 6 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 4 -> 8 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 9 -> 4 at (2118, 3025), 4 frames after previous cover
- f110: ref 79110: 9 -> 16 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 2 -> 18 at (1928, 3035), 4 frames after previous cover
- f118: ref 79105: 8 -> 6 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 4 -> 8 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 16 -> 4 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 9 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 9 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 19 -> 17 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 6 -> 8 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 8 -> 4 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 10 -> 14 at (1966, 3033.5), 1 frames after previous cover
- f120: ref 78899: 13 -> 10 at (1982.5, 3033.5), 1 frames after previous cover
- f120: ref 79037: 14 -> 2 at (1951, 3035), 1 frames after previous cover
- f120: ref 79045: 2 -> 1 at (1938, 3036.5), 1 frames after previous cover
- f120: ref 79097: 5 -> 13 at (1998, 3031), 1 frames after previous cover
- ... 85 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 898 | 97 | 0 (898) |
| 78896 | 350 (76..429) | 312 | 29 | 18 (283), 2 (27), 1 (2) |
| 78969 | 352 (80..434) | 316 | 27 | 22 (279), 7 (26), 1 (11) |
| 78971 | 352 (84..439) | 313 | 32 | 20 (266), 1 (31), 7 (11), 3 (2), 5 (2), 22 (1) |
| 79045 | 355 (84..443) | 309 | 32 | 7 (275), 2 (9), 20 (7), 5 (6), 1 (5), 3 (3), 10 (3), 4 (1) |
| 79037 | 355 (86..445) | 313 | 38 | 2 (279), 14 (9), 10 (7), 3 (4), 5 (4), 1 (4), 20 (3), 4 (2), 7 (1) |
| 78897 | 345 (89..450) | 307 | 33 | 1 (276), 10 (8), 6 (6), 2 (4), 5 (3), 14 (3), 4 (2), 3 (2), 13 (2), 20 (1) |
| 78899 | 365 (91..455) | 332 | 27 | 14 (301), 13 (10), 3 (5), 5 (5), 4 (3), 2 (3), 6 (2), 8 (1), 10 (1), 1 (1) |
| 79097 | 366 (94..461) | 330 | 33 | 10 (294), 5 (10), 21 (8), 14 (5), 6 (4), 4 (3), 3 (3), 8 (2), 13 (1) |
| 79098 | 360 (97..467) | 321 | 35 | 21 (290), 15 (9), 10 (7), 5 (5), 6 (3), 3 (3), 4 (2), 8 (2) |
| 79102 | 371 (98..477) | 332 | 35 | 5 (304), 3 (10), 10 (5), 8 (4), 6 (3), 4 (2), 15 (2), 13 (2) |
| 79103 | 380 (99..481) | 329 | 40 | 26 (291), 6 (9), 13 (8), 4 (5), 5 (5), 8 (4), 10 (3), 15 (2), 9 (1), 3 (1) |
| 79105 | 379 (101..484) | 340 | 37 | 13 (314), 8 (9), 15 (8), 4 (3), 9 (2), 6 (2), 3 (2) |
| 79108 | 385 (104..492) | 347 | 32 | 15 (323), 4 (8), 3 (8), 9 (3), 6 (3), 8 (2) |
| 79110 | 388 (106..497) | 343 | 42 | 3 (323), 16 (7), 6 (7), 8 (3), 9 (2), 4 (1) |
| 79111 | 386 (109..500) | 363 | 21 | 6 (342), 9 (8), 8 (7), 4 (4), 16 (2) |
| 79115 | 421 (111..531) | 373 | 43 | 8 (355), 4 (7), 17 (5), 16 (4), 9 (2) |
| 79116 | 411 (114..530) | 366 | 41 | 4 (352), 16 (6), 9 (4), 19 (2), 17 (2) |
| 79122 | 404 (118..532) | 366 | 35 | 16 (353), 9 (7), 17 (4), 19 (2) |
| 79132 | 391 (120..515) | 351 | 37 | 9 (339), 17 (7), 19 (4), 4 (1) |
| 79128 | 402 (124..527) | 357 | 43 | 17 (352), 19 (5) |
| 79134 | 407 (127..533) | 354 | 43 | 24 (349), 19 (5) |
| 79135 | 409 (129..542) | 376 | 31 | 19 (299), 25 (72), 23 (5) |
| 79139 | 406 (132..537) | 362 | 36 | 23 (299), 19 (63) |
| 79136 | 393 (136..538) | 352 | 31 | 25 (290), 23 (62) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 307/389/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 898 | 898 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..450 | 373 | 330 | 330 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 2 | 83..445 | 363 | 322 | 322 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 79037, 79045 |
| 3 | 86..497 | 412 | 366 | 366 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 86..530 | 445 | 396 | 396 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 5 | 89..477 | 389 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 6 | 91..500 | 410 | 381 | 381 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 7 | 94..443 | 350 | 313 | 313 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 8 | 96..531 | 436 | 389 | 389 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 9 | 100..515 | 416 | 368 | 368 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 100..461 | 362 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 108..484 | 377 | 337 | 337 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103, 79105 |
| 14 | 110..455 | 346 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 15 | 110..492 | 383 | 344 | 344 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 16 | 110..532 | 423 | 372 | 372 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 17 | 113..527 | 415 | 370 | 370 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 18 | 113..429 | 317 | 283 | 283 | 0 | 0 | 0 | 0 | 78896 |
| 19 | 116..537 | 422 | 380 | 380 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 124..439 | 316 | 277 | 277 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045 |
| 21 | 124..467 | 344 | 298 | 298 | 0 | 0 | 0 | 0 | 79097, 79098 |
| 22 | 128..434 | 307 | 280 | 280 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 23 | 129..538 | 410 | 366 | 366 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 24 | 137..533 | 397 | 349 | 349 | 0 | 0 | 0 | 0 | 79134 |
| 25 | 138..542 | 405 | 362 | 362 | 0 | 0 | 0 | 0 | 79135, 79136 |
| 26 | 144..481 | 338 | 291 | 291 | 0 | 0 | 0 | 0 | 79103 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9918; unmatched reference entries: 224; unmatched candidate entries: 941
- identity switches: 145; fragmentation (coverage interruptions): 156; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 1 -> 2 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 4 -> 3 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 3 -> 5 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 5 -> 1 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 1 -> 7 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 3 -> 5 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 6 -> 3 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 8 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 4 -> 8 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 6 -> 3 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 8 -> 6 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 5 -> 10 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 3 -> 5 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 8 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 9 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 5 -> 10 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 6 -> 3 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 1 -> 7 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 10 -> 1 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 3 -> 6 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 3 -> 5 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 7 -> 1 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 1 -> 10 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 6 -> 3 at (2088, 3029), 1 frames after previous cover
- f106: ref 79102: 8 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 8 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 9 -> 4 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 6 -> 3 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 5 -> 13 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 13 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 5 -> 13 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 14 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 10 -> 2 at (2000.5, 3033.5), 5 frames after previous cover
- f110: ref 79097: 3 -> 5 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 3 -> 15 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 6 -> 3 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 8 -> 6 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 4 -> 8 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 9 -> 4 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 9 -> 16 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 2 -> 18 at (1928, 3035), 4 frames after previous cover
- f118: ref 79105: 8 -> 6 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 4 -> 8 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 16 -> 4 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 9 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 9 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 19 -> 17 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 6 -> 8 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 8 -> 4 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 10 -> 14 at (1966, 3033.5), 1 frames after previous cover
- f120: ref 78899: 13 -> 10 at (1982.5, 3033.5), 1 frames after previous cover
- f120: ref 79037: 14 -> 2 at (1951, 3035), 1 frames after previous cover
- f120: ref 79045: 2 -> 1 at (1938, 3036.5), 1 frames after previous cover
- f120: ref 79097: 5 -> 13 at (1998, 3031), 1 frames after previous cover
- ... 85 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1001 | 6 | 0 (1001) |
| 78896 | 350 (76..429) | 338 | 5 | 18 (309), 2 (27), 1 (2) |
| 78969 | 352 (80..434) | 336 | 12 | 22 (296), 7 (29), 1 (11) |
| 78971 | 352 (84..439) | 339 | 10 | 20 (291), 1 (32), 7 (11), 3 (2), 5 (2), 22 (1) |
| 79045 | 355 (84..443) | 333 | 12 | 7 (297), 2 (10), 20 (7), 5 (6), 1 (6), 3 (3), 10 (3), 4 (1) |
| 79037 | 355 (86..445) | 343 | 10 | 2 (306), 14 (10), 10 (7), 3 (5), 5 (4), 20 (4), 1 (4), 4 (2), 7 (1) |
| 78897 | 345 (89..450) | 333 | 9 | 1 (298), 10 (8), 6 (6), 2 (6), 5 (4), 14 (4), 4 (2), 3 (2), 13 (2), 20 (1) |
| 78899 | 365 (91..455) | 354 | 7 | 14 (323), 13 (10), 3 (5), 5 (5), 4 (3), 2 (3), 6 (2), 8 (1), 10 (1), 1 (1) |
| 79097 | 366 (94..461) | 357 | 6 | 10 (321), 5 (10), 21 (8), 14 (5), 6 (4), 4 (3), 3 (3), 8 (2), 13 (1) |
| 79098 | 360 (97..467) | 349 | 11 | 21 (317), 15 (10), 10 (7), 5 (5), 6 (3), 3 (3), 4 (2), 8 (2) |
| 79102 | 371 (98..477) | 366 | 4 | 5 (335), 3 (10), 10 (6), 8 (5), 6 (4), 4 (2), 15 (2), 13 (2) |
| 79103 | 380 (99..481) | 367 | 8 | 26 (328), 6 (9), 13 (9), 4 (5), 5 (5), 8 (4), 10 (3), 15 (2), 9 (1), 3 (1) |
| 79105 | 379 (101..484) | 375 | 3 | 13 (347), 8 (9), 15 (8), 4 (4), 3 (3), 9 (2), 6 (2) |
| 79108 | 385 (104..492) | 378 | 5 | 15 (352), 4 (9), 3 (8), 9 (4), 6 (3), 8 (2) |
| 79110 | 388 (106..497) | 383 | 4 | 3 (362), 16 (8), 6 (7), 8 (3), 9 (2), 4 (1) |
| 79111 | 386 (109..500) | 383 | 2 | 6 (362), 9 (8), 8 (7), 4 (4), 16 (2) |
| 79115 | 421 (111..531) | 417 | 2 | 8 (398), 4 (7), 17 (5), 16 (4), 9 (2), 3 (1) |
| 79116 | 411 (114..530) | 403 | 5 | 4 (388), 16 (7), 9 (4), 19 (2), 17 (2) |
| 79122 | 404 (118..532) | 399 | 5 | 16 (386), 9 (7), 17 (4), 19 (2) |
| 79132 | 391 (120..515) | 388 | 3 | 9 (376), 17 (7), 19 (4), 4 (1) |
| 79128 | 402 (124..527) | 399 | 2 | 17 (394), 19 (5) |
| 79134 | 407 (127..533) | 389 | 11 | 24 (384), 19 (5) |
| 79135 | 409 (129..542) | 405 | 4 | 19 (325), 25 (75), 23 (5) |
| 79139 | 406 (132..537) | 398 | 4 | 23 (331), 19 (67) |
| 79136 | 393 (136..538) | 385 | 6 | 25 (315), 23 (70) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 336/418/1007; tracks with internal gaps: 25; total internal gaps: 210; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1001 | 6 | 6 | 1 | 0 | 78911 |
| 1 | 78..479 | 402 | 402 | 354 | 48 | 17 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 2 | 83..474 | 392 | 392 | 352 | 40 | 9 | 2 | 29 | 78896, 78897, 78899, 79037, 79045 |
| 3 | 86..526 | 441 | 441 | 408 | 33 | 4 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 4 | 86..559 | 474 | 474 | 434 | 40 | 8 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 5 | 89..506 | 418 | 418 | 376 | 42 | 13 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 6 | 91..529 | 439 | 439 | 402 | 37 | 6 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 7 | 94..472 | 379 | 379 | 338 | 41 | 10 | 2 | 29 | 78969, 78971, 79037, 79045 |
| 8 | 96..560 | 465 | 465 | 433 | 32 | 3 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 9 | 100..544 | 445 | 445 | 406 | 39 | 9 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 100..490 | 391 | 391 | 356 | 35 | 4 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 108..513 | 406 | 406 | 371 | 35 | 5 | 2 | 29 | 78897, 78899, 79097, 79102, 79103, 79105 |
| 14 | 110..484 | 375 | 375 | 342 | 33 | 4 | 1 | 29 | 78897, 78899, 79037, 79097 |
| 15 | 110..521 | 412 | 412 | 374 | 38 | 8 | 2 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 16 | 110..561 | 452 | 452 | 407 | 45 | 15 | 2 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 17 | 113..556 | 444 | 444 | 412 | 32 | 3 | 1 | 29 | 79115, 79116, 79122, 79128, 79132 |
| 18 | 113..458 | 346 | 346 | 309 | 37 | 5 | 3 | 29 | 78896 |
| 19 | 116..566 | 451 | 451 | 410 | 41 | 10 | 3 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 124..468 | 345 | 345 | 303 | 42 | 11 | 3 | 29 | 78897, 78971, 79037, 79045 |
| 21 | 124..496 | 373 | 373 | 325 | 48 | 16 | 2 | 29 | 79097, 79098 |
| 22 | 128..463 | 336 | 336 | 297 | 39 | 8 | 3 | 29 | 78969, 78971 |
| 23 | 129..567 | 439 | 439 | 406 | 33 | 4 | 1 | 29 | 79135, 79136, 79139 |
| 24 | 137..562 | 426 | 426 | 384 | 42 | 10 | 3 | 29 | 79134 |
| 25 | 138..571 | 434 | 434 | 390 | 44 | 14 | 2 | 29 | 79135, 79136 |
| 26 | 144..510 | 367 | 367 | 328 | 39 | 8 | 2 | 29 | 79103 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9918; unmatched reference entries: 224; unmatched candidate entries: 941
- identity switches: 145; fragmentation (coverage interruptions): 156; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 1 -> 2 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 4 -> 3 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 3 -> 5 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 5 -> 1 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 1 -> 7 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 3 -> 5 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 6 -> 3 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 8 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 4 -> 8 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 6 -> 3 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 8 -> 6 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 5 -> 10 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 3 -> 5 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 8 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 9 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 5 -> 10 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 6 -> 3 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 1 -> 7 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 10 -> 1 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 3 -> 6 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 3 -> 5 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 7 -> 1 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 1 -> 10 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 6 -> 3 at (2088, 3029), 1 frames after previous cover
- f106: ref 79102: 8 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 8 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 9 -> 4 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 6 -> 3 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 5 -> 13 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 13 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 5 -> 13 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 14 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 10 -> 2 at (2000.5, 3033.5), 5 frames after previous cover
- f110: ref 79097: 3 -> 5 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 3 -> 15 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 6 -> 3 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 8 -> 6 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 4 -> 8 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 9 -> 4 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 9 -> 16 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 2 -> 18 at (1928, 3035), 4 frames after previous cover
- f118: ref 79105: 8 -> 6 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 4 -> 8 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 16 -> 4 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 9 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 9 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 19 -> 17 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 6 -> 8 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 8 -> 4 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 10 -> 14 at (1966, 3033.5), 1 frames after previous cover
- f120: ref 78899: 13 -> 10 at (1982.5, 3033.5), 1 frames after previous cover
- f120: ref 79037: 14 -> 2 at (1951, 3035), 1 frames after previous cover
- f120: ref 79045: 2 -> 1 at (1938, 3036.5), 1 frames after previous cover
- f120: ref 79097: 5 -> 13 at (1998, 3031), 1 frames after previous cover
- ... 85 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1001 | 6 | 0 (1001) |
| 78896 | 350 (76..429) | 338 | 5 | 18 (309), 2 (27), 1 (2) |
| 78969 | 352 (80..434) | 336 | 12 | 22 (296), 7 (29), 1 (11) |
| 78971 | 352 (84..439) | 339 | 10 | 20 (291), 1 (32), 7 (11), 3 (2), 5 (2), 22 (1) |
| 79045 | 355 (84..443) | 333 | 12 | 7 (297), 2 (10), 20 (7), 5 (6), 1 (6), 3 (3), 10 (3), 4 (1) |
| 79037 | 355 (86..445) | 343 | 10 | 2 (306), 14 (10), 10 (7), 3 (5), 5 (4), 20 (4), 1 (4), 4 (2), 7 (1) |
| 78897 | 345 (89..450) | 333 | 9 | 1 (298), 10 (8), 6 (6), 2 (6), 5 (4), 14 (4), 4 (2), 3 (2), 13 (2), 20 (1) |
| 78899 | 365 (91..455) | 354 | 7 | 14 (323), 13 (10), 3 (5), 5 (5), 4 (3), 2 (3), 6 (2), 8 (1), 10 (1), 1 (1) |
| 79097 | 366 (94..461) | 357 | 6 | 10 (321), 5 (10), 21 (8), 14 (5), 6 (4), 4 (3), 3 (3), 8 (2), 13 (1) |
| 79098 | 360 (97..467) | 349 | 11 | 21 (317), 15 (10), 10 (7), 5 (5), 6 (3), 3 (3), 4 (2), 8 (2) |
| 79102 | 371 (98..477) | 366 | 4 | 5 (335), 3 (10), 10 (6), 8 (5), 6 (4), 4 (2), 15 (2), 13 (2) |
| 79103 | 380 (99..481) | 367 | 8 | 26 (328), 6 (9), 13 (9), 4 (5), 5 (5), 8 (4), 10 (3), 15 (2), 9 (1), 3 (1) |
| 79105 | 379 (101..484) | 375 | 3 | 13 (347), 8 (9), 15 (8), 4 (4), 3 (3), 9 (2), 6 (2) |
| 79108 | 385 (104..492) | 378 | 5 | 15 (352), 4 (9), 3 (8), 9 (4), 6 (3), 8 (2) |
| 79110 | 388 (106..497) | 383 | 4 | 3 (362), 16 (8), 6 (7), 8 (3), 9 (2), 4 (1) |
| 79111 | 386 (109..500) | 383 | 2 | 6 (362), 9 (8), 8 (7), 4 (4), 16 (2) |
| 79115 | 421 (111..531) | 417 | 2 | 8 (398), 4 (7), 17 (5), 16 (4), 9 (2), 3 (1) |
| 79116 | 411 (114..530) | 403 | 5 | 4 (388), 16 (7), 9 (4), 19 (2), 17 (2) |
| 79122 | 404 (118..532) | 399 | 5 | 16 (386), 9 (7), 17 (4), 19 (2) |
| 79132 | 391 (120..515) | 388 | 3 | 9 (376), 17 (7), 19 (4), 4 (1) |
| 79128 | 402 (124..527) | 399 | 2 | 17 (394), 19 (5) |
| 79134 | 407 (127..533) | 389 | 11 | 24 (384), 19 (5) |
| 79135 | 409 (129..542) | 405 | 4 | 19 (325), 25 (75), 23 (5) |
| 79139 | 406 (132..537) | 398 | 4 | 23 (331), 19 (67) |
| 79136 | 393 (136..538) | 385 | 6 | 25 (315), 23 (70) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 336/418/1007; tracks with internal gaps: 25; total internal gaps: 210; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1001 | 6 | 6 | 1 | 0 | 78911 |
| 1 | 78..479 | 402 | 402 | 354 | 48 | 17 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 2 | 83..474 | 392 | 392 | 352 | 40 | 9 | 2 | 29 | 78896, 78897, 78899, 79037, 79045 |
| 3 | 86..526 | 441 | 441 | 408 | 33 | 4 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 4 | 86..559 | 474 | 474 | 434 | 40 | 8 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 5 | 89..506 | 418 | 418 | 376 | 42 | 13 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 6 | 91..529 | 439 | 439 | 402 | 37 | 6 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 7 | 94..472 | 379 | 379 | 338 | 41 | 10 | 2 | 29 | 78969, 78971, 79037, 79045 |
| 8 | 96..560 | 465 | 465 | 433 | 32 | 3 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 9 | 100..544 | 445 | 445 | 406 | 39 | 9 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 100..490 | 391 | 391 | 356 | 35 | 4 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 108..513 | 406 | 406 | 371 | 35 | 5 | 2 | 29 | 78897, 78899, 79097, 79102, 79103, 79105 |
| 14 | 110..484 | 375 | 375 | 342 | 33 | 4 | 1 | 29 | 78897, 78899, 79037, 79097 |
| 15 | 110..521 | 412 | 412 | 374 | 38 | 8 | 2 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 16 | 110..561 | 452 | 452 | 407 | 45 | 15 | 2 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 17 | 113..556 | 444 | 444 | 412 | 32 | 3 | 1 | 29 | 79115, 79116, 79122, 79128, 79132 |
| 18 | 113..458 | 346 | 346 | 309 | 37 | 5 | 3 | 29 | 78896 |
| 19 | 116..566 | 451 | 451 | 410 | 41 | 10 | 3 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 124..468 | 345 | 345 | 303 | 42 | 11 | 3 | 29 | 78897, 78971, 79037, 79045 |
| 21 | 124..496 | 373 | 373 | 325 | 48 | 16 | 2 | 29 | 79097, 79098 |
| 22 | 128..463 | 336 | 336 | 297 | 39 | 8 | 3 | 29 | 78969, 78971 |
| 23 | 129..567 | 439 | 439 | 406 | 33 | 4 | 1 | 29 | 79135, 79136, 79139 |
| 24 | 137..562 | 426 | 426 | 384 | 42 | 10 | 3 | 29 | 79134 |
| 25 | 138..571 | 434 | 434 | 390 | 44 | 14 | 2 | 29 | 79135, 79136 |
| 26 | 144..510 | 367 | 367 | 328 | 39 | 8 | 2 | 29 | 79103 |
