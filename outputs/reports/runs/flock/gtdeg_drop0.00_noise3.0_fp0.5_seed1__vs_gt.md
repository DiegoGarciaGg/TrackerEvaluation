# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=e5fdd94c46fe
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise3.0_fp0.5_seed1/tracks.csv sha256=aea6ebcc11c76dfd
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise3.0_fp0.5_seed1.csv sha256=e5fdd94c46fe6ac8
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise3.0_fp0.5_seed1
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
| observations | none | 4 | 0.340 | 0.268 | 0.154 | 2.40 | 0.449 | 187 | 2500.0 |
| observations | none | 6 | 0.483 | 0.387 | 0.708 | 3.20 | 0.669 | 174 | 1269.0 |
| observations | none | 8 | 0.562 | 0.461 | 0.912 | 3.58 | 0.756 | 164 | 436.0 |
| observations | none | 12 | 0.648 | 0.545 | 0.969 | 3.83 | 0.806 | 140 | 166.0 |
| observations | ignore | 4 | 0.340 | 0.268 | 0.154 | 2.40 | 0.449 | 187 | 2500.0 |
| observations | ignore | 6 | 0.483 | 0.387 | 0.708 | 3.20 | 0.669 | 174 | 1269.0 |
| observations | ignore | 8 | 0.562 | 0.461 | 0.912 | 3.58 | 0.756 | 164 | 436.0 |
| observations | ignore | 12 | 0.648 | 0.545 | 0.969 | 3.83 | 0.806 | 140 | 166.0 |
| updates | none | 4 | 0.320 | 0.254 | 0.071 | 2.41 | 0.431 | 199 | 2498.0 |
| updates | none | 6 | 0.452 | 0.366 | 0.625 | 3.20 | 0.642 | 174 | 1264.0 |
| updates | none | 8 | 0.526 | 0.435 | 0.829 | 3.59 | 0.726 | 158 | 434.0 |
| updates | none | 12 | 0.605 | 0.512 | 0.887 | 3.84 | 0.775 | 126 | 165.0 |
| updates | ignore | 4 | 0.320 | 0.254 | 0.071 | 2.41 | 0.431 | 199 | 2498.0 |
| updates | ignore | 6 | 0.452 | 0.366 | 0.625 | 3.20 | 0.642 | 174 | 1264.0 |
| updates | ignore | 8 | 0.526 | 0.435 | 0.829 | 3.59 | 0.726 | 158 | 434.0 |
| updates | ignore | 12 | 0.605 | 0.512 | 0.887 | 3.84 | 0.775 | 126 | 165.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 9760; unmatched reference entries: 382; unmatched candidate entries: 346
- identity switches: 164; fragmentation (coverage interruptions): 334; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 33 -> 35 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78897: 33 -> 35 at (2148.5, 3030.5), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78969: 30 -> 29 at (2089.5, 3031.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 30 at (2108.5, 3033.5), 3 frames after previous cover
- f91: ref 79037: 35 -> 37 at (2129, 3033.5), 2 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f93: ref 78896: 38 -> 29 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 29 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 38 -> 30 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 30 -> 38 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78897: 33 -> 41 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78971: 38 -> 32 at (2077, 3034.5), 1 frames after previous cover
- f96: ref 79037: 37 -> 38 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 32 -> 37 at (2087.5, 3033.5), 1 frames after previous cover
- f97: ref 78899: 33 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 35 -> 33 at (2135, 3028), 1 frames after previous cover
- f98: ref 79098: 35 -> 38 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 41 -> 44 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 38 -> 41 at (2080, 3034.5), 3 frames after previous cover
- f99: ref 79102: 35 -> 38 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 38 -> 46 at (2104, 3030.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 35 at (2142.5, 3026), 1 frames after previous cover
- f100: ref 79103: 35 -> 38 at (2150, 3022.5), 1 frames after previous cover
- f102: ref 79102: 35 -> 47 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 38 -> 35 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 38 -> 48 at (2113.5, 3027), 5 frames after previous cover
- f104: ref 79105: 38 -> 35 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 47 -> 50 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 35 -> 47 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 44 -> 41 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79097: 33 -> 46 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 35 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 35 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78899: 46 -> 44 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 41 -> 37 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 37 -> 53 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79098: 48 -> 33 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 50 at (2092.5, 3023.5), 2 frames after previous cover
- f113: ref 79037: 37 -> 53 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 53 -> 37 at (1982.5, 3034), 2 frames after previous cover
- f116: ref 78897: 41 -> 53 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 79037: 53 -> 41 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79115: 56 -> 57 at (2130, 3021), 3 frames after previous cover
- f119: ref 78971: 32 -> 37 at (1933, 3034.5), 1 frames after previous cover
- f119: ref 79111: 38 -> 51 at (2098.5, 3028.5), 1 frames after previous cover
- f120: ref 79045: 37 -> 32 at (1938, 3036.5), 3 frames after previous cover
- f120: ref 79111: 51 -> 38 at (2091.5, 3030), 1 frames after previous cover
- f129: ref 79105: 47 -> 48 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 35 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 51 -> 35 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 38 -> 51 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 56 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 56 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 62 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 62 -> 61 at (2107.5, 3023), 1 frames after previous cover
- ... 104 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 340 | 8 | 29 (339), 38 (1) |
| 78969 | 352 (80..434) | 333 | 16 | 30 (330), 29 (2), 38 (1) |
| 78971 | 352 (84..439) | 337 | 10 | 32 (303), 37 (28), 30 (3), 38 (2), 35 (1) |
| 79045 | 355 (84..443) | 341 | 11 | 41 (186), 37 (119), 32 (34), 53 (2) |
| 79037 | 355 (86..445) | 339 | 15 | 37 (193), 41 (138), 33 (3), 53 (3), 35 (1), 38 (1) |
| 78897 | 345 (89..450) | 333 | 11 | 53 (308), 41 (10), 44 (10), 33 (4), 35 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 44 (332), 46 (8), 35 (3), 33 (3), 38 (1) |
| 79097 | 366 (94..461) | 355 | 11 | 46 (340), 33 (12), 35 (3) |
| 79098 | 360 (97..467) | 346 | 11 | 50 (275), 33 (63), 48 (6), 35 (1), 38 (1) |
| 79102 | 371 (98..477) | 361 | 10 | 33 (286), 50 (46), 48 (20), 47 (4), 35 (3), 38 (1), 53 (1) |
| 79103 | 380 (99..481) | 371 | 8 | 48 (237), 70 (106), 50 (19), 35 (3), 47 (3), 33 (2), 38 (1) |
| 79105 | 379 (101..484) | 361 | 16 | 70 (233), 48 (100), 47 (20), 35 (6), 38 (2) |
| 79108 | 385 (104..492) | 374 | 9 | 35 (166), 57 (115), 47 (89), 38 (2), 51 (1), 48 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 47 (195), 35 (147), 51 (19), 57 (19), 38 (2) |
| 79111 | 386 (109..500) | 368 | 17 | 57 (195), 47 (75), 35 (51), 51 (29), 38 (18) |
| 79115 | 421 (111..531) | 403 | 14 | 61 (239), 51 (84), 57 (42), 38 (29), 56 (7), 35 (2) |
| 79116 | 411 (114..530) | 395 | 15 | 51 (271), 38 (59), 56 (41), 61 (24) |
| 79122 | 404 (118..532) | 390 | 11 | 56 (327), 61 (63) |
| 79132 | 391 (120..515) | 374 | 15 | 38 (198), 65 (79), 61 (65), 56 (25), 62 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 65 (284), 38 (95), 62 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 62 (333), 73 (36), 65 (9), 51 (4), 69 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 69 (325), 71 (70), 62 (1), 73 (1) |
| 79139 | 406 (132..537) | 389 | 14 | 71 (322), 62 (46), 73 (20), 69 (1) |
| 79136 | 393 (136..538) | 378 | 13 | 73 (309), 69 (64), 62 (3), 71 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 224 | 469..469 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 1/390/1007; tracks with internal gaps: 25; total internal gaps: 329; longest internal gap: 3; tracks ending in coasting: 3 (trailing rows total 4)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 29 | 78..429 | 352 | 348 | 341 | 7 | 7 | 1 | 0 | 78896, 78969 |
| 30 | 82..434 | 353 | 350 | 333 | 17 | 16 | 2 | 0 | 78969, 78971 |
| 32 | 86..439 | 354 | 351 | 337 | 14 | 14 | 1 | 0 | 78971, 79045 |
| 33 | 86..479 | 394 | 385 | 373 | 12 | 11 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 35 | 87..492 | 406 | 402 | 388 | 14 | 13 | 2 | 0 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 37 | 91..445 | 355 | 351 | 340 | 11 | 11 | 1 | 0 | 78971, 79037, 79045 |
| 38 | 92..527 | 436 | 427 | 414 | 13 | 12 | 2 | 0 | 78896, 78899, 78969, 78971, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132 |
| 41 | 96..443 | 348 | 342 | 334 | 8 | 8 | 1 | 0 | 78897, 79037, 79045 |
| 44 | 99..455 | 357 | 357 | 342 | 15 | 14 | 2 | 0 | 78897, 78899 |
| 46 | 100..469 | 370 | 361 | 348 | 13 | 12 | 1 | 1 | 78899, 79097 |
| 47 | 101..497 | 397 | 395 | 386 | 9 | 9 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 48 | 103..481 | 379 | 373 | 364 | 9 | 9 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 50 | 106..467 | 362 | 351 | 340 | 11 | 11 | 1 | 0 | 79098, 79102, 79103 |
| 51 | 108..533 | 426 | 422 | 408 | 14 | 12 | 3 | 0 | 79108, 79110, 79111, 79115, 79116, 79134 |
| 53 | 110..450 | 341 | 326 | 314 | 12 | 12 | 1 | 0 | 78897, 79037, 79045, 79102 |
| 56 | 113..532 | 420 | 414 | 400 | 14 | 13 | 2 | 0 | 79115, 79116, 79122, 79132 |
| 57 | 116..500 | 385 | 382 | 371 | 11 | 10 | 2 | 0 | 79108, 79110, 79111, 79115 |
| 61 | 120..531 | 412 | 408 | 391 | 17 | 16 | 2 | 0 | 79115, 79116, 79122, 79132 |
| 62 | 122..537 | 416 | 416 | 399 | 17 | 17 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 126..515 | 390 | 386 | 372 | 14 | 13 | 2 | 0 | 79128, 79132, 79134 |
| 69 | 129..538 | 410 | 405 | 393 | 12 | 12 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 70 | 132..484 | 353 | 352 | 339 | 13 | 12 | 2 | 0 | 79103, 79105 |
| 71 | 134..542 | 409 | 408 | 394 | 14 | 13 | 2 | 0 | 79135, 79136, 79139 |
| 73 | 138..535 | 398 | 386 | 366 | 20 | 18 | 1 | 2 | 79134, 79135, 79136, 79139 |
| 224 | 469..469 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 9760; unmatched reference entries: 382; unmatched candidate entries: 346
- identity switches: 164; fragmentation (coverage interruptions): 334; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 33 -> 35 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78897: 33 -> 35 at (2148.5, 3030.5), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78969: 30 -> 29 at (2089.5, 3031.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 30 at (2108.5, 3033.5), 3 frames after previous cover
- f91: ref 79037: 35 -> 37 at (2129, 3033.5), 2 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f93: ref 78896: 38 -> 29 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 29 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 38 -> 30 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 30 -> 38 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78897: 33 -> 41 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78971: 38 -> 32 at (2077, 3034.5), 1 frames after previous cover
- f96: ref 79037: 37 -> 38 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 32 -> 37 at (2087.5, 3033.5), 1 frames after previous cover
- f97: ref 78899: 33 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 35 -> 33 at (2135, 3028), 1 frames after previous cover
- f98: ref 79098: 35 -> 38 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 41 -> 44 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 38 -> 41 at (2080, 3034.5), 3 frames after previous cover
- f99: ref 79102: 35 -> 38 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 38 -> 46 at (2104, 3030.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 35 at (2142.5, 3026), 1 frames after previous cover
- f100: ref 79103: 35 -> 38 at (2150, 3022.5), 1 frames after previous cover
- f102: ref 79102: 35 -> 47 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 38 -> 35 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 38 -> 48 at (2113.5, 3027), 5 frames after previous cover
- f104: ref 79105: 38 -> 35 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 47 -> 50 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 35 -> 47 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 44 -> 41 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79097: 33 -> 46 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 35 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 35 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78899: 46 -> 44 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 41 -> 37 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 37 -> 53 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79098: 48 -> 33 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 50 at (2092.5, 3023.5), 2 frames after previous cover
- f113: ref 79037: 37 -> 53 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 53 -> 37 at (1982.5, 3034), 2 frames after previous cover
- f116: ref 78897: 41 -> 53 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 79037: 53 -> 41 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79115: 56 -> 57 at (2130, 3021), 3 frames after previous cover
- f119: ref 78971: 32 -> 37 at (1933, 3034.5), 1 frames after previous cover
- f119: ref 79111: 38 -> 51 at (2098.5, 3028.5), 1 frames after previous cover
- f120: ref 79045: 37 -> 32 at (1938, 3036.5), 3 frames after previous cover
- f120: ref 79111: 51 -> 38 at (2091.5, 3030), 1 frames after previous cover
- f129: ref 79105: 47 -> 48 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 35 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 51 -> 35 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 38 -> 51 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 56 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 56 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 62 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 62 -> 61 at (2107.5, 3023), 1 frames after previous cover
- ... 104 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 340 | 8 | 29 (339), 38 (1) |
| 78969 | 352 (80..434) | 333 | 16 | 30 (330), 29 (2), 38 (1) |
| 78971 | 352 (84..439) | 337 | 10 | 32 (303), 37 (28), 30 (3), 38 (2), 35 (1) |
| 79045 | 355 (84..443) | 341 | 11 | 41 (186), 37 (119), 32 (34), 53 (2) |
| 79037 | 355 (86..445) | 339 | 15 | 37 (193), 41 (138), 33 (3), 53 (3), 35 (1), 38 (1) |
| 78897 | 345 (89..450) | 333 | 11 | 53 (308), 41 (10), 44 (10), 33 (4), 35 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 44 (332), 46 (8), 35 (3), 33 (3), 38 (1) |
| 79097 | 366 (94..461) | 355 | 11 | 46 (340), 33 (12), 35 (3) |
| 79098 | 360 (97..467) | 346 | 11 | 50 (275), 33 (63), 48 (6), 35 (1), 38 (1) |
| 79102 | 371 (98..477) | 361 | 10 | 33 (286), 50 (46), 48 (20), 47 (4), 35 (3), 38 (1), 53 (1) |
| 79103 | 380 (99..481) | 371 | 8 | 48 (237), 70 (106), 50 (19), 35 (3), 47 (3), 33 (2), 38 (1) |
| 79105 | 379 (101..484) | 361 | 16 | 70 (233), 48 (100), 47 (20), 35 (6), 38 (2) |
| 79108 | 385 (104..492) | 374 | 9 | 35 (166), 57 (115), 47 (89), 38 (2), 51 (1), 48 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 47 (195), 35 (147), 51 (19), 57 (19), 38 (2) |
| 79111 | 386 (109..500) | 368 | 17 | 57 (195), 47 (75), 35 (51), 51 (29), 38 (18) |
| 79115 | 421 (111..531) | 403 | 14 | 61 (239), 51 (84), 57 (42), 38 (29), 56 (7), 35 (2) |
| 79116 | 411 (114..530) | 395 | 15 | 51 (271), 38 (59), 56 (41), 61 (24) |
| 79122 | 404 (118..532) | 390 | 11 | 56 (327), 61 (63) |
| 79132 | 391 (120..515) | 374 | 15 | 38 (198), 65 (79), 61 (65), 56 (25), 62 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 65 (284), 38 (95), 62 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 62 (333), 73 (36), 65 (9), 51 (4), 69 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 69 (325), 71 (70), 62 (1), 73 (1) |
| 79139 | 406 (132..537) | 389 | 14 | 71 (322), 62 (46), 73 (20), 69 (1) |
| 79136 | 393 (136..538) | 378 | 13 | 73 (309), 69 (64), 62 (3), 71 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 224 | 469..469 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 1/390/1007; tracks with internal gaps: 25; total internal gaps: 329; longest internal gap: 3; tracks ending in coasting: 3 (trailing rows total 4)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 29 | 78..429 | 352 | 348 | 341 | 7 | 7 | 1 | 0 | 78896, 78969 |
| 30 | 82..434 | 353 | 350 | 333 | 17 | 16 | 2 | 0 | 78969, 78971 |
| 32 | 86..439 | 354 | 351 | 337 | 14 | 14 | 1 | 0 | 78971, 79045 |
| 33 | 86..479 | 394 | 385 | 373 | 12 | 11 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 35 | 87..492 | 406 | 402 | 388 | 14 | 13 | 2 | 0 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 37 | 91..445 | 355 | 351 | 340 | 11 | 11 | 1 | 0 | 78971, 79037, 79045 |
| 38 | 92..527 | 436 | 427 | 414 | 13 | 12 | 2 | 0 | 78896, 78899, 78969, 78971, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132 |
| 41 | 96..443 | 348 | 342 | 334 | 8 | 8 | 1 | 0 | 78897, 79037, 79045 |
| 44 | 99..455 | 357 | 357 | 342 | 15 | 14 | 2 | 0 | 78897, 78899 |
| 46 | 100..469 | 370 | 361 | 348 | 13 | 12 | 1 | 1 | 78899, 79097 |
| 47 | 101..497 | 397 | 395 | 386 | 9 | 9 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 48 | 103..481 | 379 | 373 | 364 | 9 | 9 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 50 | 106..467 | 362 | 351 | 340 | 11 | 11 | 1 | 0 | 79098, 79102, 79103 |
| 51 | 108..533 | 426 | 422 | 408 | 14 | 12 | 3 | 0 | 79108, 79110, 79111, 79115, 79116, 79134 |
| 53 | 110..450 | 341 | 326 | 314 | 12 | 12 | 1 | 0 | 78897, 79037, 79045, 79102 |
| 56 | 113..532 | 420 | 414 | 400 | 14 | 13 | 2 | 0 | 79115, 79116, 79122, 79132 |
| 57 | 116..500 | 385 | 382 | 371 | 11 | 10 | 2 | 0 | 79108, 79110, 79111, 79115 |
| 61 | 120..531 | 412 | 408 | 391 | 17 | 16 | 2 | 0 | 79115, 79116, 79122, 79132 |
| 62 | 122..537 | 416 | 416 | 399 | 17 | 17 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 126..515 | 390 | 386 | 372 | 14 | 13 | 2 | 0 | 79128, 79132, 79134 |
| 69 | 129..538 | 410 | 405 | 393 | 12 | 12 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 70 | 132..484 | 353 | 352 | 339 | 13 | 12 | 2 | 0 | 79103, 79105 |
| 71 | 134..542 | 409 | 408 | 394 | 14 | 13 | 2 | 0 | 79135, 79136, 79139 |
| 73 | 138..535 | 398 | 386 | 366 | 20 | 18 | 1 | 2 | 79134, 79135, 79136, 79139 |
| 224 | 469..469 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 9761; unmatched reference entries: 381; unmatched candidate entries: 1195
- identity switches: 158; fragmentation (coverage interruptions): 332; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 33 -> 35 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78897: 33 -> 35 at (2148.5, 3030.5), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78969: 30 -> 29 at (2089.5, 3031.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 30 at (2108.5, 3033.5), 3 frames after previous cover
- f91: ref 79037: 35 -> 37 at (2129, 3033.5), 2 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f93: ref 78896: 38 -> 29 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 29 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 38 -> 30 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 30 -> 38 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78897: 33 -> 41 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78971: 38 -> 32 at (2077, 3034.5), 1 frames after previous cover
- f96: ref 79037: 37 -> 38 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 32 -> 37 at (2087.5, 3033.5), 1 frames after previous cover
- f97: ref 78899: 33 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 35 -> 33 at (2135, 3028), 1 frames after previous cover
- f98: ref 79098: 35 -> 38 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 41 -> 44 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 38 -> 41 at (2080, 3034.5), 3 frames after previous cover
- f99: ref 79102: 35 -> 38 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 38 -> 46 at (2104, 3030.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 35 at (2142.5, 3026), 1 frames after previous cover
- f100: ref 79103: 35 -> 38 at (2150, 3022.5), 1 frames after previous cover
- f102: ref 79102: 35 -> 47 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 38 -> 35 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 38 -> 48 at (2113.5, 3027), 5 frames after previous cover
- f104: ref 79105: 38 -> 35 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 47 -> 50 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 35 -> 47 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 44 -> 41 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79097: 33 -> 46 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 35 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 35 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78899: 46 -> 44 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 41 -> 37 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 37 -> 53 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79098: 48 -> 33 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 50 at (2092.5, 3023.5), 2 frames after previous cover
- f113: ref 79037: 37 -> 53 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 53 -> 37 at (1982.5, 3034), 2 frames after previous cover
- f116: ref 78897: 41 -> 53 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 79037: 53 -> 41 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79115: 56 -> 57 at (2130, 3021), 3 frames after previous cover
- f119: ref 78971: 32 -> 37 at (1933, 3034.5), 1 frames after previous cover
- f120: ref 79045: 37 -> 32 at (1938, 3036.5), 3 frames after previous cover
- f129: ref 79105: 47 -> 48 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 35 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 51 -> 35 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 38 -> 51 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 56 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 56 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 62 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 62 -> 61 at (2107.5, 3023), 1 frames after previous cover
- f130: ref 79102: 48 -> 50 at (1965, 3030), 2 frames after previous cover
- f130: ref 79103: 50 -> 48 at (1974, 3024.5), 1 frames after previous cover
- ... 98 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 340 | 8 | 29 (339), 38 (1) |
| 78969 | 352 (80..434) | 333 | 16 | 30 (330), 29 (2), 38 (1) |
| 78971 | 352 (84..439) | 338 | 9 | 32 (304), 37 (28), 30 (3), 38 (2), 35 (1) |
| 79045 | 355 (84..443) | 341 | 11 | 41 (186), 37 (119), 32 (34), 53 (2) |
| 79037 | 355 (86..445) | 339 | 15 | 37 (193), 41 (138), 33 (3), 53 (3), 35 (1), 38 (1) |
| 78897 | 345 (89..450) | 333 | 11 | 53 (308), 41 (10), 44 (10), 33 (4), 35 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 44 (332), 46 (8), 35 (3), 33 (3), 38 (1) |
| 79097 | 366 (94..461) | 356 | 10 | 46 (338), 33 (12), 35 (3), 44 (3) |
| 79098 | 360 (97..467) | 346 | 11 | 50 (275), 33 (63), 48 (6), 35 (1), 38 (1) |
| 79102 | 371 (98..477) | 361 | 10 | 33 (286), 50 (46), 48 (20), 47 (4), 35 (3), 38 (1), 53 (1) |
| 79103 | 380 (99..481) | 371 | 8 | 48 (235), 70 (106), 50 (19), 33 (4), 35 (3), 47 (3), 38 (1) |
| 79105 | 379 (101..484) | 361 | 16 | 70 (233), 48 (100), 47 (20), 35 (6), 38 (2) |
| 79108 | 385 (104..492) | 374 | 9 | 35 (166), 57 (115), 47 (89), 38 (2), 51 (1), 48 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 47 (195), 35 (147), 51 (19), 57 (19), 38 (2) |
| 79111 | 386 (109..500) | 368 | 17 | 57 (195), 47 (75), 35 (51), 51 (28), 38 (19) |
| 79115 | 421 (111..531) | 403 | 14 | 61 (238), 51 (85), 57 (42), 38 (29), 56 (7), 35 (2) |
| 79116 | 411 (114..530) | 395 | 15 | 51 (271), 38 (59), 56 (41), 61 (24) |
| 79122 | 404 (118..532) | 389 | 12 | 56 (334), 61 (55) |
| 79132 | 391 (120..515) | 372 | 16 | 38 (199), 65 (79), 61 (72), 56 (15), 62 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 65 (285), 38 (94), 62 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 62 (333), 73 (36), 65 (9), 51 (4), 69 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 69 (325), 71 (70), 62 (1), 73 (1) |
| 79139 | 406 (132..537) | 390 | 13 | 71 (323), 62 (46), 73 (20), 69 (1) |
| 79136 | 393 (136..538) | 379 | 12 | 73 (309), 69 (63), 62 (3), 71 (2), 65 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 224 | 469..498 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 30/419/1007; tracks with internal gaps: 25; total internal gaps: 420; longest internal gap: 21; tracks ending in coasting: 25 (trailing rows total 716)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 29 | 78..458 | 381 | 381 | 341 | 40 | 9 | 3 | 29 | 78896, 78969 |
| 30 | 82..463 | 382 | 382 | 333 | 49 | 17 | 2 | 29 | 78969, 78971 |
| 32 | 86..468 | 383 | 383 | 338 | 45 | 16 | 1 | 29 | 78971, 79045 |
| 33 | 86..508 | 423 | 423 | 375 | 48 | 20 | 2 | 27 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 35 | 87..521 | 435 | 435 | 388 | 47 | 16 | 2 | 29 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 37 | 91..474 | 384 | 384 | 340 | 44 | 13 | 2 | 29 | 78971, 79037, 79045 |
| 38 | 92..556 | 465 | 465 | 415 | 50 | 19 | 2 | 29 | 78896, 78899, 78969, 78971, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132 |
| 41 | 96..472 | 377 | 377 | 334 | 43 | 13 | 2 | 29 | 78897, 79037, 79045 |
| 44 | 99..484 | 386 | 386 | 345 | 41 | 15 | 3 | 23 | 78897, 78899, 79097 |
| 46 | 100..498 | 399 | 399 | 346 | 53 | 13 | 1 | 40 | 78899, 79097 |
| 47 | 101..526 | 426 | 426 | 386 | 40 | 11 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 48 | 103..510 | 408 | 408 | 362 | 46 | 11 | 4 | 32 | 79098, 79102, 79103, 79105, 79108 |
| 50 | 106..496 | 391 | 391 | 340 | 51 | 20 | 3 | 29 | 79098, 79102, 79103 |
| 51 | 108..562 | 455 | 455 | 408 | 47 | 16 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79134 |
| 53 | 110..479 | 370 | 370 | 314 | 56 | 25 | 2 | 29 | 78897, 79037, 79045, 79102 |
| 56 | 113..561 | 449 | 449 | 397 | 52 | 20 | 2 | 30 | 79115, 79116, 79122, 79132 |
| 57 | 116..529 | 414 | 414 | 371 | 43 | 13 | 2 | 29 | 79108, 79110, 79111, 79115 |
| 61 | 120..560 | 441 | 441 | 389 | 52 | 22 | 2 | 28 | 79115, 79116, 79122, 79132 |
| 62 | 122..566 | 445 | 445 | 399 | 46 | 17 | 1 | 29 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 126..544 | 419 | 419 | 375 | 44 | 15 | 21 | 6 | 79128, 79132, 79134, 79136 |
| 69 | 129..567 | 439 | 439 | 392 | 47 | 16 | 1 | 31 | 79134, 79135, 79136, 79139 |
| 70 | 132..513 | 382 | 382 | 339 | 43 | 12 | 2 | 29 | 79103, 79105 |
| 71 | 134..571 | 438 | 438 | 395 | 43 | 13 | 2 | 29 | 79135, 79136, 79139 |
| 73 | 138..564 | 427 | 427 | 366 | 61 | 24 | 2 | 34 | 79134, 79135, 79136, 79139 |
| 224 | 469..498 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 9761; unmatched reference entries: 381; unmatched candidate entries: 1195
- identity switches: 158; fragmentation (coverage interruptions): 332; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 33 -> 35 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78897: 33 -> 35 at (2148.5, 3030.5), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78969: 30 -> 29 at (2089.5, 3031.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 30 at (2108.5, 3033.5), 3 frames after previous cover
- f91: ref 79037: 35 -> 37 at (2129, 3033.5), 2 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f93: ref 78896: 38 -> 29 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 29 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 38 -> 30 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 30 -> 38 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78897: 33 -> 41 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78971: 38 -> 32 at (2077, 3034.5), 1 frames after previous cover
- f96: ref 79037: 37 -> 38 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 32 -> 37 at (2087.5, 3033.5), 1 frames after previous cover
- f97: ref 78899: 33 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 35 -> 33 at (2135, 3028), 1 frames after previous cover
- f98: ref 79098: 35 -> 38 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 41 -> 44 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 38 -> 41 at (2080, 3034.5), 3 frames after previous cover
- f99: ref 79102: 35 -> 38 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 38 -> 46 at (2104, 3030.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 35 at (2142.5, 3026), 1 frames after previous cover
- f100: ref 79103: 35 -> 38 at (2150, 3022.5), 1 frames after previous cover
- f102: ref 79102: 35 -> 47 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 38 -> 35 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 38 -> 48 at (2113.5, 3027), 5 frames after previous cover
- f104: ref 79105: 38 -> 35 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 47 -> 50 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 35 -> 47 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 44 -> 41 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79097: 33 -> 46 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 35 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 35 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78899: 46 -> 44 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 41 -> 37 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 37 -> 53 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79098: 48 -> 33 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 50 at (2092.5, 3023.5), 2 frames after previous cover
- f113: ref 79037: 37 -> 53 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 53 -> 37 at (1982.5, 3034), 2 frames after previous cover
- f116: ref 78897: 41 -> 53 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 79037: 53 -> 41 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79115: 56 -> 57 at (2130, 3021), 3 frames after previous cover
- f119: ref 78971: 32 -> 37 at (1933, 3034.5), 1 frames after previous cover
- f120: ref 79045: 37 -> 32 at (1938, 3036.5), 3 frames after previous cover
- f129: ref 79105: 47 -> 48 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 35 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 51 -> 35 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 38 -> 51 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 56 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 56 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 62 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 62 -> 61 at (2107.5, 3023), 1 frames after previous cover
- f130: ref 79102: 48 -> 50 at (1965, 3030), 2 frames after previous cover
- f130: ref 79103: 50 -> 48 at (1974, 3024.5), 1 frames after previous cover
- ... 98 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 340 | 8 | 29 (339), 38 (1) |
| 78969 | 352 (80..434) | 333 | 16 | 30 (330), 29 (2), 38 (1) |
| 78971 | 352 (84..439) | 338 | 9 | 32 (304), 37 (28), 30 (3), 38 (2), 35 (1) |
| 79045 | 355 (84..443) | 341 | 11 | 41 (186), 37 (119), 32 (34), 53 (2) |
| 79037 | 355 (86..445) | 339 | 15 | 37 (193), 41 (138), 33 (3), 53 (3), 35 (1), 38 (1) |
| 78897 | 345 (89..450) | 333 | 11 | 53 (308), 41 (10), 44 (10), 33 (4), 35 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 44 (332), 46 (8), 35 (3), 33 (3), 38 (1) |
| 79097 | 366 (94..461) | 356 | 10 | 46 (338), 33 (12), 35 (3), 44 (3) |
| 79098 | 360 (97..467) | 346 | 11 | 50 (275), 33 (63), 48 (6), 35 (1), 38 (1) |
| 79102 | 371 (98..477) | 361 | 10 | 33 (286), 50 (46), 48 (20), 47 (4), 35 (3), 38 (1), 53 (1) |
| 79103 | 380 (99..481) | 371 | 8 | 48 (235), 70 (106), 50 (19), 33 (4), 35 (3), 47 (3), 38 (1) |
| 79105 | 379 (101..484) | 361 | 16 | 70 (233), 48 (100), 47 (20), 35 (6), 38 (2) |
| 79108 | 385 (104..492) | 374 | 9 | 35 (166), 57 (115), 47 (89), 38 (2), 51 (1), 48 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 47 (195), 35 (147), 51 (19), 57 (19), 38 (2) |
| 79111 | 386 (109..500) | 368 | 17 | 57 (195), 47 (75), 35 (51), 51 (28), 38 (19) |
| 79115 | 421 (111..531) | 403 | 14 | 61 (238), 51 (85), 57 (42), 38 (29), 56 (7), 35 (2) |
| 79116 | 411 (114..530) | 395 | 15 | 51 (271), 38 (59), 56 (41), 61 (24) |
| 79122 | 404 (118..532) | 389 | 12 | 56 (334), 61 (55) |
| 79132 | 391 (120..515) | 372 | 16 | 38 (199), 65 (79), 61 (72), 56 (15), 62 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 65 (285), 38 (94), 62 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 62 (333), 73 (36), 65 (9), 51 (4), 69 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 69 (325), 71 (70), 62 (1), 73 (1) |
| 79139 | 406 (132..537) | 390 | 13 | 71 (323), 62 (46), 73 (20), 69 (1) |
| 79136 | 393 (136..538) | 379 | 12 | 73 (309), 69 (63), 62 (3), 71 (2), 65 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 224 | 469..498 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 30/419/1007; tracks with internal gaps: 25; total internal gaps: 420; longest internal gap: 21; tracks ending in coasting: 25 (trailing rows total 716)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 29 | 78..458 | 381 | 381 | 341 | 40 | 9 | 3 | 29 | 78896, 78969 |
| 30 | 82..463 | 382 | 382 | 333 | 49 | 17 | 2 | 29 | 78969, 78971 |
| 32 | 86..468 | 383 | 383 | 338 | 45 | 16 | 1 | 29 | 78971, 79045 |
| 33 | 86..508 | 423 | 423 | 375 | 48 | 20 | 2 | 27 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 35 | 87..521 | 435 | 435 | 388 | 47 | 16 | 2 | 29 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 37 | 91..474 | 384 | 384 | 340 | 44 | 13 | 2 | 29 | 78971, 79037, 79045 |
| 38 | 92..556 | 465 | 465 | 415 | 50 | 19 | 2 | 29 | 78896, 78899, 78969, 78971, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132 |
| 41 | 96..472 | 377 | 377 | 334 | 43 | 13 | 2 | 29 | 78897, 79037, 79045 |
| 44 | 99..484 | 386 | 386 | 345 | 41 | 15 | 3 | 23 | 78897, 78899, 79097 |
| 46 | 100..498 | 399 | 399 | 346 | 53 | 13 | 1 | 40 | 78899, 79097 |
| 47 | 101..526 | 426 | 426 | 386 | 40 | 11 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 48 | 103..510 | 408 | 408 | 362 | 46 | 11 | 4 | 32 | 79098, 79102, 79103, 79105, 79108 |
| 50 | 106..496 | 391 | 391 | 340 | 51 | 20 | 3 | 29 | 79098, 79102, 79103 |
| 51 | 108..562 | 455 | 455 | 408 | 47 | 16 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79134 |
| 53 | 110..479 | 370 | 370 | 314 | 56 | 25 | 2 | 29 | 78897, 79037, 79045, 79102 |
| 56 | 113..561 | 449 | 449 | 397 | 52 | 20 | 2 | 30 | 79115, 79116, 79122, 79132 |
| 57 | 116..529 | 414 | 414 | 371 | 43 | 13 | 2 | 29 | 79108, 79110, 79111, 79115 |
| 61 | 120..560 | 441 | 441 | 389 | 52 | 22 | 2 | 28 | 79115, 79116, 79122, 79132 |
| 62 | 122..566 | 445 | 445 | 399 | 46 | 17 | 1 | 29 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 126..544 | 419 | 419 | 375 | 44 | 15 | 21 | 6 | 79128, 79132, 79134, 79136 |
| 69 | 129..567 | 439 | 439 | 392 | 47 | 16 | 1 | 31 | 79134, 79135, 79136, 79139 |
| 70 | 132..513 | 382 | 382 | 339 | 43 | 12 | 2 | 29 | 79103, 79105 |
| 71 | 134..571 | 438 | 438 | 395 | 43 | 13 | 2 | 29 | 79135, 79136, 79139 |
| 73 | 138..564 | 427 | 427 | 366 | 61 | 24 | 2 | 34 | 79134, 79135, 79136, 79139 |
| 224 | 469..498 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
