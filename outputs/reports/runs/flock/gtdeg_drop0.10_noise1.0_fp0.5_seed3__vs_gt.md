# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=b8fa13cb6b9d
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise1.0_fp0.5_seed3/tracks.csv sha256=71201968a4f23b04
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise1.0_fp0.5_seed3.csv sha256=b8fa13cb6b9d9cf7
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise1.0_fp0.5_seed3
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
| observations | none | 4 | 0.409 | 0.227 | 0.839 | 1.27 | 0.448 | 543 | 943.0 |
| observations | none | 6 | 0.441 | 0.245 | 0.840 | 1.27 | 0.449 | 538 | 939.0 |
| observations | none | 8 | 0.456 | 0.257 | 0.840 | 1.30 | 0.451 | 538 | 941.0 |
| observations | none | 12 | 0.476 | 0.280 | 0.840 | 1.48 | 0.471 | 488 | 936.0 |
| observations | ignore | 4 | 0.409 | 0.227 | 0.839 | 1.27 | 0.448 | 543 | 943.0 |
| observations | ignore | 6 | 0.441 | 0.245 | 0.840 | 1.27 | 0.449 | 538 | 939.0 |
| observations | ignore | 8 | 0.456 | 0.257 | 0.840 | 1.30 | 0.451 | 538 | 941.0 |
| observations | ignore | 12 | 0.476 | 0.280 | 0.840 | 1.48 | 0.471 | 488 | 936.0 |
| updates | none | 4 | 0.378 | 0.218 | 0.681 | 1.29 | 0.417 | 552 | 865.0 |
| updates | none | 6 | 0.419 | 0.240 | 0.734 | 1.40 | 0.431 | 558 | 612.0 |
| updates | none | 8 | 0.440 | 0.255 | 0.785 | 1.57 | 0.444 | 527 | 393.0 |
| updates | none | 12 | 0.466 | 0.280 | 0.804 | 1.83 | 0.469 | 468 | 313.0 |
| updates | ignore | 4 | 0.378 | 0.218 | 0.681 | 1.29 | 0.417 | 552 | 865.0 |
| updates | ignore | 6 | 0.419 | 0.240 | 0.734 | 1.40 | 0.431 | 558 | 612.0 |
| updates | ignore | 8 | 0.440 | 0.255 | 0.785 | 1.57 | 0.444 | 527 | 393.0 |
| updates | ignore | 12 | 0.466 | 0.280 | 0.804 | 1.83 | 0.469 | 468 | 313.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9102; unmatched reference entries: 1040; unmatched candidate entries: 45
- identity switches: 538; fragmentation (coverage interruptions): 885; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 47 -> 45 at (2115, 3033.5), 1 frames after previous cover
- f90: ref 79037: 46 -> 47 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 46 -> 47 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 45 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78897: 47 -> 53 at (2132, 3032), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 46 -> 53 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 47 -> 46 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79097: 46 -> 53 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 47 -> 46 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 53 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 53 -> 58 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 46 -> 53 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 46 at (2147.5, 3026.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 58 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 53 -> 60 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 79098: 58 -> 61 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79102: 53 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 46 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 47 -> 46 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79102: 58 -> 46 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 46 -> 53 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 60 -> 56 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 56 -> 45 at (2038, 3034.5), 2 frames after previous cover
- f106: ref 79097: 58 -> 60 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 61 -> 58 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 46 -> 61 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 53 -> 46 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 45 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 44 -> 64 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 47 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 56 -> 45 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 54 -> 56 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 45 -> 44 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 44 -> 64 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 58 -> 60 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 61 -> 58 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 53 -> 61 at (2101.5, 3024.5), 2 frames after previous cover
- f110: ref 79110: 47 -> 66 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 58 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 46 -> 58 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 61 -> 46 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 53 -> 61 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 66 -> 53 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 47 -> 66 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 56 -> 45 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 54 -> 56 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 60 -> 54 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 45 -> 56 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 64 -> 69 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 56 -> 54 at (2040.5, 3031), 1 frames after previous cover
- ... 478 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 921 | 73 | 2 (921) |
| 78896 | 350 (76..429) | 319 | 27 | 73 (231), 41 (88) |
| 78969 | 352 (80..434) | 310 | 32 | 58 (144), 41 (94), 73 (43), 44 (15), 59 (14) |
| 78971 | 352 (84..439) | 309 | 31 | 155 (103), 58 (95), 78 (51), 44 (46), 59 (4), 47 (3), 45 (2), 56 (2), 69 (2), 64 (1) |
| 79045 | 355 (84..443) | 312 | 31 | 78 (112), 44 (76), 89 (49), 155 (47), 45 (18), 64 (5), 69 (2), 59 (2), 58 (1) |
| 79037 | 355 (86..445) | 308 | 37 | 44 (149), 78 (66), 89 (57), 59 (12), 56 (6), 45 (4), 69 (4), 46 (3), 64 (3), 47 (2), 54 (2) |
| 78897 | 345 (89..450) | 305 | 31 | 89 (162), 78 (49), 44 (34), 59 (22), 69 (11), 60 (4), 56 (4), 45 (4), 64 (4), 54 (4), 46 (3), 53 (3), +1 more |
| 78899 | 365 (91..455) | 325 | 37 | 54 (205), 59 (44), 69 (24), 64 (12), 45 (8), 89 (8), 44 (8), 56 (6), 46 (4), 78 (4), 53 (2) |
| 79097 | 366 (94..461) | 334 | 27 | 56 (156), 59 (70), 54 (44), 69 (26), 58 (23), 45 (5), 60 (4), 47 (2), 46 (2), 53 (1), 64 (1) |
| 79098 | 360 (97..467) | 326 | 30 | 56 (72), 59 (63), 69 (60), 54 (45), 45 (38), 64 (17), 58 (15), 61 (10), 53 (2), 60 (2), 47 (1), 46 (1) |
| 79102 | 371 (98..477) | 337 | 33 | 61 (214), 64 (31), 59 (28), 54 (23), 58 (9), 60 (8), 56 (7), 69 (7), 46 (4), 45 (3), 53 (2), 47 (1) |
| 79103 | 380 (99..481) | 349 | 29 | 61 (97), 59 (85), 60 (59), 45 (48), 69 (21), 58 (10), 56 (9), 46 (8), 64 (8), 47 (2), 53 (2) |
| 79105 | 379 (101..484) | 332 | 43 | 45 (122), 60 (60), 46 (55), 56 (50), 61 (16), 69 (11), 64 (7), 129 (5), 53 (4), 47 (1), 81 (1) |
| 79108 | 385 (104..492) | 340 | 39 | 69 (100), 60 (63), 46 (63), 182 (54), 66 (21), 56 (16), 61 (9), 45 (5), 47 (3), 71 (3), 53 (2), 77 (1) |
| 79110 | 388 (106..497) | 351 | 34 | 182 (72), 69 (63), 77 (60), 81 (41), 45 (29), 46 (23), 60 (23), 66 (10), 71 (10), 129 (7), 56 (6), 53 (3), +2 more |
| 79111 | 386 (109..500) | 351 | 31 | 66 (132), 129 (79), 45 (57), 46 (52), 77 (10), 53 (6), 71 (4), 60 (4), 182 (3), 47 (2), 81 (1), 56 (1) |
| 79115 | 421 (111..531) | 387 | 29 | 60 (172), 46 (79), 72 (72), 47 (16), 77 (12), 53 (8), 129 (8), 66 (7), 81 (7), 71 (6) |
| 79116 | 411 (114..530) | 372 | 34 | 129 (89), 46 (71), 66 (67), 72 (66), 64 (23), 77 (22), 47 (18), 71 (13), 53 (1), 81 (1), 85 (1) |
| 79122 | 404 (118..532) | 366 | 31 | 71 (132), 64 (99), 129 (77), 72 (20), 66 (18), 47 (15), 77 (5) |
| 79132 | 391 (120..515) | 344 | 40 | 72 (102), 71 (80), 47 (79), 66 (40), 77 (39), 53 (4) |
| 79128 | 402 (124..527) | 378 | 21 | 71 (128), 64 (95), 66 (74), 53 (51), 47 (14), 72 (10), 77 (3), 129 (2), 69 (1) |
| 79134 | 407 (127..533) | 364 | 40 | 47 (139), 64 (87), 85 (59), 53 (39), 72 (33), 77 (5), 69 (2) |
| 79135 | 409 (129..542) | 349 | 51 | 53 (113), 85 (95), 47 (92), 72 (44), 77 (5) |
| 79139 | 406 (132..537) | 359 | 40 | 85 (198), 53 (138), 90 (14), 72 (9) |
| 79136 | 393 (136..538) | 354 | 34 | 90 (336), 53 (13), 85 (5) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 437 | 910..910 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 1/376/1004; tracks with internal gaps: 15; total internal gaps: 30; longest internal gap: 2; tracks ending in coasting: 9 (trailing rows total 14)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 926 | 921 | 5 | 5 | 1 | 0 | 78911 |
| 41 | 78..289 | 212 | 184 | 182 | 2 | 0 | 0 | 2 | 78896, 78969 |
| 44 | 82..455 | 374 | 329 | 328 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 45 | 86..467 | 382 | 344 | 343 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 46 | 86..484 | 399 | 368 | 368 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 47 | 87..577 | 491 | 399 | 393 | 6 | 3 | 2 | 2 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 53 | 93..533 | 441 | 394 | 394 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 96..448 | 353 | 324 | 323 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 56 | 97..461 | 365 | 336 | 335 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 58 | 99..434 | 336 | 299 | 297 | 2 | 2 | 1 | 0 | 78969, 78971, 79045, 79097, 79098, 79102, 79103 |
| 59 | 102..481 | 380 | 346 | 344 | 2 | 2 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 60 | 102..531 | 430 | 400 | 399 | 1 | 1 | 1 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 61 | 103..478 | 376 | 349 | 348 | 1 | 0 | 0 | 1 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 64 | 109..532 | 424 | 394 | 393 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79116, 79122, 79128, 79134 |
| 66 | 110..500 | 391 | 369 | 369 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 113..539 | 427 | 338 | 334 | 4 | 3 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128, 79134 |
| 71 | 117..527 | 411 | 377 | 376 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 72 | 120..514 | 395 | 356 | 356 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 73 | 120..429 | 310 | 277 | 274 | 3 | 3 | 1 | 0 | 78896, 78969 |
| 77 | 127..337 | 211 | 164 | 162 | 2 | 0 | 0 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 78 | 127..443 | 317 | 282 | 282 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 81 | 133..192 | 60 | 53 | 51 | 2 | 0 | 0 | 2 | 79105, 79110, 79111, 79115, 79116 |
| 85 | 138..537 | 400 | 362 | 358 | 4 | 4 | 1 | 0 | 79116, 79134, 79135, 79136, 79139 |
| 89 | 145..449 | 305 | 276 | 276 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 90 | 145..538 | 394 | 351 | 350 | 1 | 1 | 1 | 0 | 79136, 79139 |
| 129 | 231..530 | 300 | 268 | 267 | 1 | 1 | 1 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128 |
| 155 | 282..439 | 158 | 150 | 150 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 182 | 350..499 | 150 | 131 | 129 | 2 | 0 | 0 | 2 | 79108, 79110, 79111 |
| 437 | 910..910 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9102; unmatched reference entries: 1040; unmatched candidate entries: 45
- identity switches: 538; fragmentation (coverage interruptions): 885; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 47 -> 45 at (2115, 3033.5), 1 frames after previous cover
- f90: ref 79037: 46 -> 47 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 46 -> 47 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 45 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78897: 47 -> 53 at (2132, 3032), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 46 -> 53 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 47 -> 46 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79097: 46 -> 53 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 47 -> 46 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 53 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 53 -> 58 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 46 -> 53 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 46 at (2147.5, 3026.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 58 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 53 -> 60 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 79098: 58 -> 61 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79102: 53 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 46 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 47 -> 46 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79102: 58 -> 46 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 46 -> 53 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 60 -> 56 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 56 -> 45 at (2038, 3034.5), 2 frames after previous cover
- f106: ref 79097: 58 -> 60 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 61 -> 58 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 46 -> 61 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 53 -> 46 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 45 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 44 -> 64 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 47 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 56 -> 45 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 54 -> 56 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 45 -> 44 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 44 -> 64 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 58 -> 60 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 61 -> 58 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 53 -> 61 at (2101.5, 3024.5), 2 frames after previous cover
- f110: ref 79110: 47 -> 66 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 58 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 46 -> 58 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 61 -> 46 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 53 -> 61 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 66 -> 53 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 47 -> 66 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 56 -> 45 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 54 -> 56 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 60 -> 54 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 45 -> 56 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 64 -> 69 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 56 -> 54 at (2040.5, 3031), 1 frames after previous cover
- ... 478 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 921 | 73 | 2 (921) |
| 78896 | 350 (76..429) | 319 | 27 | 73 (231), 41 (88) |
| 78969 | 352 (80..434) | 310 | 32 | 58 (144), 41 (94), 73 (43), 44 (15), 59 (14) |
| 78971 | 352 (84..439) | 309 | 31 | 155 (103), 58 (95), 78 (51), 44 (46), 59 (4), 47 (3), 45 (2), 56 (2), 69 (2), 64 (1) |
| 79045 | 355 (84..443) | 312 | 31 | 78 (112), 44 (76), 89 (49), 155 (47), 45 (18), 64 (5), 69 (2), 59 (2), 58 (1) |
| 79037 | 355 (86..445) | 308 | 37 | 44 (149), 78 (66), 89 (57), 59 (12), 56 (6), 45 (4), 69 (4), 46 (3), 64 (3), 47 (2), 54 (2) |
| 78897 | 345 (89..450) | 305 | 31 | 89 (162), 78 (49), 44 (34), 59 (22), 69 (11), 60 (4), 56 (4), 45 (4), 64 (4), 54 (4), 46 (3), 53 (3), +1 more |
| 78899 | 365 (91..455) | 325 | 37 | 54 (205), 59 (44), 69 (24), 64 (12), 45 (8), 89 (8), 44 (8), 56 (6), 46 (4), 78 (4), 53 (2) |
| 79097 | 366 (94..461) | 334 | 27 | 56 (156), 59 (70), 54 (44), 69 (26), 58 (23), 45 (5), 60 (4), 47 (2), 46 (2), 53 (1), 64 (1) |
| 79098 | 360 (97..467) | 326 | 30 | 56 (72), 59 (63), 69 (60), 54 (45), 45 (38), 64 (17), 58 (15), 61 (10), 53 (2), 60 (2), 47 (1), 46 (1) |
| 79102 | 371 (98..477) | 337 | 33 | 61 (214), 64 (31), 59 (28), 54 (23), 58 (9), 60 (8), 56 (7), 69 (7), 46 (4), 45 (3), 53 (2), 47 (1) |
| 79103 | 380 (99..481) | 349 | 29 | 61 (97), 59 (85), 60 (59), 45 (48), 69 (21), 58 (10), 56 (9), 46 (8), 64 (8), 47 (2), 53 (2) |
| 79105 | 379 (101..484) | 332 | 43 | 45 (122), 60 (60), 46 (55), 56 (50), 61 (16), 69 (11), 64 (7), 129 (5), 53 (4), 47 (1), 81 (1) |
| 79108 | 385 (104..492) | 340 | 39 | 69 (100), 60 (63), 46 (63), 182 (54), 66 (21), 56 (16), 61 (9), 45 (5), 47 (3), 71 (3), 53 (2), 77 (1) |
| 79110 | 388 (106..497) | 351 | 34 | 182 (72), 69 (63), 77 (60), 81 (41), 45 (29), 46 (23), 60 (23), 66 (10), 71 (10), 129 (7), 56 (6), 53 (3), +2 more |
| 79111 | 386 (109..500) | 351 | 31 | 66 (132), 129 (79), 45 (57), 46 (52), 77 (10), 53 (6), 71 (4), 60 (4), 182 (3), 47 (2), 81 (1), 56 (1) |
| 79115 | 421 (111..531) | 387 | 29 | 60 (172), 46 (79), 72 (72), 47 (16), 77 (12), 53 (8), 129 (8), 66 (7), 81 (7), 71 (6) |
| 79116 | 411 (114..530) | 372 | 34 | 129 (89), 46 (71), 66 (67), 72 (66), 64 (23), 77 (22), 47 (18), 71 (13), 53 (1), 81 (1), 85 (1) |
| 79122 | 404 (118..532) | 366 | 31 | 71 (132), 64 (99), 129 (77), 72 (20), 66 (18), 47 (15), 77 (5) |
| 79132 | 391 (120..515) | 344 | 40 | 72 (102), 71 (80), 47 (79), 66 (40), 77 (39), 53 (4) |
| 79128 | 402 (124..527) | 378 | 21 | 71 (128), 64 (95), 66 (74), 53 (51), 47 (14), 72 (10), 77 (3), 129 (2), 69 (1) |
| 79134 | 407 (127..533) | 364 | 40 | 47 (139), 64 (87), 85 (59), 53 (39), 72 (33), 77 (5), 69 (2) |
| 79135 | 409 (129..542) | 349 | 51 | 53 (113), 85 (95), 47 (92), 72 (44), 77 (5) |
| 79139 | 406 (132..537) | 359 | 40 | 85 (198), 53 (138), 90 (14), 72 (9) |
| 79136 | 393 (136..538) | 354 | 34 | 90 (336), 53 (13), 85 (5) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 437 | 910..910 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 1/376/1004; tracks with internal gaps: 15; total internal gaps: 30; longest internal gap: 2; tracks ending in coasting: 9 (trailing rows total 14)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 926 | 921 | 5 | 5 | 1 | 0 | 78911 |
| 41 | 78..289 | 212 | 184 | 182 | 2 | 0 | 0 | 2 | 78896, 78969 |
| 44 | 82..455 | 374 | 329 | 328 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 45 | 86..467 | 382 | 344 | 343 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 46 | 86..484 | 399 | 368 | 368 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 47 | 87..577 | 491 | 399 | 393 | 6 | 3 | 2 | 2 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 53 | 93..533 | 441 | 394 | 394 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 96..448 | 353 | 324 | 323 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 56 | 97..461 | 365 | 336 | 335 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 58 | 99..434 | 336 | 299 | 297 | 2 | 2 | 1 | 0 | 78969, 78971, 79045, 79097, 79098, 79102, 79103 |
| 59 | 102..481 | 380 | 346 | 344 | 2 | 2 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 60 | 102..531 | 430 | 400 | 399 | 1 | 1 | 1 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 61 | 103..478 | 376 | 349 | 348 | 1 | 0 | 0 | 1 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 64 | 109..532 | 424 | 394 | 393 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79116, 79122, 79128, 79134 |
| 66 | 110..500 | 391 | 369 | 369 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 113..539 | 427 | 338 | 334 | 4 | 3 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128, 79134 |
| 71 | 117..527 | 411 | 377 | 376 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 72 | 120..514 | 395 | 356 | 356 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 73 | 120..429 | 310 | 277 | 274 | 3 | 3 | 1 | 0 | 78896, 78969 |
| 77 | 127..337 | 211 | 164 | 162 | 2 | 0 | 0 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 78 | 127..443 | 317 | 282 | 282 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 81 | 133..192 | 60 | 53 | 51 | 2 | 0 | 0 | 2 | 79105, 79110, 79111, 79115, 79116 |
| 85 | 138..537 | 400 | 362 | 358 | 4 | 4 | 1 | 0 | 79116, 79134, 79135, 79136, 79139 |
| 89 | 145..449 | 305 | 276 | 276 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 90 | 145..538 | 394 | 351 | 350 | 1 | 1 | 1 | 0 | 79136, 79139 |
| 129 | 231..530 | 300 | 268 | 267 | 1 | 1 | 1 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128 |
| 155 | 282..439 | 158 | 150 | 150 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 182 | 350..499 | 150 | 131 | 129 | 2 | 0 | 0 | 2 | 79108, 79110, 79111 |
| 437 | 910..910 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9749; unmatched reference entries: 393; unmatched candidate entries: 1260
- identity switches: 527; fragmentation (coverage interruptions): 294; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 47 -> 45 at (2115, 3033.5), 1 frames after previous cover
- f90: ref 79037: 46 -> 47 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 46 -> 47 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 45 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78897: 47 -> 53 at (2125, 3030), 1 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 46 -> 53 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 47 -> 46 at (2135, 3028), 1 frames after previous cover
- f98: ref 79097: 46 -> 53 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 47 -> 46 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 53 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79097: 53 -> 58 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 46 -> 53 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 46 at (2147.5, 3026.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 58 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 53 -> 60 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 79098: 58 -> 61 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79102: 53 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 46 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 47 -> 46 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79102: 58 -> 46 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 46 -> 53 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 60 -> 56 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 56 -> 45 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79097: 58 -> 60 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 61 -> 58 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 46 -> 61 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 53 -> 46 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 45 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 44 -> 64 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 47 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 56 -> 45 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 54 -> 56 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 45 -> 44 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 44 -> 64 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 58 -> 60 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 61 -> 58 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 53 -> 61 at (2101.5, 3024.5), 2 frames after previous cover
- f110: ref 79110: 47 -> 66 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 58 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 46 -> 58 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 61 -> 46 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 53 -> 61 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 66 -> 53 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 47 -> 66 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 56 -> 45 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 54 -> 56 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 60 -> 54 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 45 -> 56 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 64 -> 69 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 56 -> 54 at (2040.5, 3031), 1 frames after previous cover
- ... 467 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 992 | 9 | 2 (992) |
| 78896 | 350 (76..429) | 337 | 10 | 73 (243), 41 (94) |
| 78969 | 352 (80..434) | 330 | 14 | 58 (153), 41 (98), 73 (50), 44 (15), 59 (14) |
| 78971 | 352 (84..439) | 326 | 15 | 155 (107), 58 (101), 78 (54), 44 (50), 59 (4), 47 (3), 45 (2), 56 (2), 69 (2), 64 (1) |
| 79045 | 355 (84..443) | 331 | 13 | 78 (118), 44 (80), 89 (53), 155 (51), 45 (18), 64 (5), 59 (3), 69 (2), 58 (1) |
| 79037 | 355 (86..445) | 331 | 17 | 44 (164), 78 (70), 89 (59), 59 (12), 56 (7), 45 (4), 69 (4), 46 (3), 54 (3), 64 (3), 47 (2) |
| 78897 | 345 (89..450) | 327 | 12 | 89 (175), 78 (53), 44 (36), 59 (23), 69 (13), 60 (4), 56 (4), 45 (4), 64 (4), 54 (4), 46 (3), 47 (2), +1 more |
| 78899 | 365 (91..455) | 350 | 14 | 54 (225), 59 (47), 69 (25), 64 (13), 89 (8), 44 (8), 56 (7), 45 (7), 46 (4), 78 (4), 53 (2) |
| 79097 | 366 (94..461) | 346 | 16 | 56 (162), 59 (73), 54 (46), 69 (26), 58 (24), 45 (5), 60 (4), 47 (3), 46 (1), 53 (1), 64 (1) |
| 79098 | 360 (97..467) | 347 | 12 | 56 (77), 59 (68), 69 (66), 54 (45), 45 (40), 64 (20), 58 (15), 61 (10), 53 (2), 60 (2), 47 (1), 46 (1) |
| 79102 | 371 (98..477) | 355 | 15 | 61 (225), 64 (33), 59 (29), 54 (25), 58 (11), 60 (8), 56 (7), 69 (7), 46 (4), 45 (3), 53 (2), 47 (1) |
| 79103 | 380 (99..481) | 365 | 14 | 61 (101), 59 (92), 60 (60), 45 (50), 69 (21), 56 (11), 58 (10), 46 (8), 64 (8), 47 (2), 53 (2) |
| 79105 | 379 (101..484) | 365 | 12 | 45 (136), 60 (64), 46 (59), 56 (56), 61 (18), 69 (12), 64 (8), 129 (6), 53 (4), 47 (1), 81 (1) |
| 79108 | 385 (104..492) | 366 | 16 | 69 (110), 46 (68), 60 (67), 182 (60), 66 (21), 56 (16), 61 (10), 45 (5), 47 (3), 71 (3), 53 (2), 77 (1) |
| 79110 | 388 (106..497) | 374 | 11 | 182 (78), 77 (67), 69 (66), 81 (43), 45 (30), 46 (25), 60 (24), 71 (11), 66 (10), 129 (7), 56 (6), 53 (3), +2 more |
| 79111 | 386 (109..500) | 375 | 10 | 66 (139), 129 (86), 45 (60), 46 (54), 77 (14), 53 (6), 71 (4), 60 (4), 182 (4), 47 (2), 81 (1), 56 (1) |
| 79115 | 421 (111..531) | 408 | 10 | 60 (186), 72 (82), 46 (77), 47 (15), 77 (12), 53 (8), 129 (8), 66 (7), 81 (7), 71 (6) |
| 79116 | 411 (114..530) | 397 | 10 | 129 (96), 46 (82), 66 (73), 72 (63), 64 (26), 77 (22), 47 (19), 71 (12), 53 (2), 81 (1), 85 (1) |
| 79122 | 404 (118..532) | 390 | 10 | 71 (143), 64 (103), 129 (84), 66 (24), 72 (21), 47 (9), 77 (6) |
| 79132 | 391 (120..515) | 375 | 12 | 72 (112), 47 (95), 71 (83), 77 (43), 66 (37), 53 (5) |
| 79128 | 402 (124..527) | 396 | 4 | 71 (135), 64 (100), 66 (77), 53 (53), 47 (15), 72 (10), 77 (3), 129 (3) |
| 79134 | 407 (127..533) | 397 | 10 | 47 (154), 64 (91), 85 (64), 53 (42), 72 (37), 77 (5), 69 (3), 182 (1) |
| 79135 | 409 (129..542) | 394 | 10 | 53 (122), 47 (108), 85 (102), 72 (53), 77 (7), 69 (2) |
| 79139 | 406 (132..537) | 394 | 10 | 85 (217), 53 (167), 72 (10) |
| 79136 | 393 (136..538) | 381 | 8 | 90 (375), 85 (4), 71 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 437 | 910..939 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 30/405/1004; tracks with internal gaps: 26; total internal gaps: 241; longest internal gap: 28; tracks ending in coasting: 28 (trailing rows total 876)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 992 | 12 | 9 | 3 | 0 | 78911 |
| 41 | 78..318 | 241 | 241 | 192 | 49 | 2 | 1 | 47 | 78896, 78969 |
| 44 | 82..484 | 403 | 403 | 353 | 50 | 12 | 5 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 45 | 86..496 | 411 | 411 | 364 | 47 | 8 | 11 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 46 | 86..513 | 428 | 428 | 389 | 39 | 10 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 47 | 87..606 | 520 | 520 | 437 | 83 | 16 | 2 | 64 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 53 | 93..562 | 470 | 470 | 425 | 45 | 11 | 5 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79139 |
| 54 | 96..477 | 382 | 382 | 348 | 34 | 4 | 1 | 30 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 56 | 97..490 | 394 | 394 | 356 | 38 | 8 | 2 | 29 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 58 | 99..463 | 365 | 365 | 315 | 50 | 15 | 3 | 29 | 78969, 78971, 79045, 79097, 79098, 79102, 79103 |
| 59 | 102..510 | 409 | 409 | 365 | 44 | 11 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 60 | 102..560 | 459 | 459 | 423 | 36 | 5 | 3 | 29 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 61 | 103..507 | 405 | 405 | 366 | 39 | 9 | 1 | 30 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 64 | 109..561 | 453 | 453 | 416 | 37 | 8 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79116, 79122, 79128, 79134 |
| 66 | 110..529 | 420 | 420 | 388 | 32 | 3 | 1 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 113..568 | 456 | 456 | 359 | 97 | 20 | 25 | 35 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79134, 79135 |
| 71 | 117..556 | 440 | 440 | 399 | 41 | 11 | 9 | 18 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136 |
| 72 | 120..543 | 424 | 424 | 388 | 36 | 5 | 3 | 28 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 73 | 120..458 | 339 | 339 | 293 | 46 | 12 | 4 | 29 | 78896, 78969 |
| 77 | 127..366 | 240 | 240 | 180 | 60 | 3 | 1 | 57 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 78 | 127..472 | 346 | 346 | 299 | 47 | 14 | 3 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 81 | 133..221 | 89 | 89 | 53 | 36 | 0 | 0 | 36 | 79105, 79110, 79111, 79115, 79116 |
| 85 | 138..566 | 429 | 429 | 388 | 41 | 9 | 2 | 29 | 79116, 79134, 79135, 79136, 79139 |
| 89 | 145..478 | 334 | 334 | 295 | 39 | 11 | 1 | 28 | 78897, 78899, 79037, 79045 |
| 90 | 145..567 | 423 | 423 | 375 | 48 | 14 | 2 | 31 | 79136 |
| 129 | 231..559 | 329 | 329 | 290 | 39 | 9 | 2 | 29 | 79105, 79110, 79111, 79115, 79116, 79122, 79128 |
| 155 | 282..468 | 187 | 187 | 158 | 29 | 0 | 0 | 29 | 78971, 79045 |
| 182 | 350..528 | 179 | 179 | 143 | 36 | 2 | 28 | 7 | 79108, 79110, 79111, 79134 |
| 437 | 910..939 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9749; unmatched reference entries: 393; unmatched candidate entries: 1260
- identity switches: 527; fragmentation (coverage interruptions): 294; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 47 -> 45 at (2115, 3033.5), 1 frames after previous cover
- f90: ref 79037: 46 -> 47 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 46 -> 47 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 45 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78897: 47 -> 53 at (2125, 3030), 1 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 46 -> 53 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 47 -> 46 at (2135, 3028), 1 frames after previous cover
- f98: ref 79097: 46 -> 53 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 47 -> 46 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 53 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79097: 53 -> 58 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 46 -> 53 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 46 at (2147.5, 3026.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 58 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 53 -> 60 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 79098: 58 -> 61 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79102: 53 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 46 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 47 -> 46 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79102: 58 -> 46 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 46 -> 53 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 60 -> 56 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 56 -> 45 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79097: 58 -> 60 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 61 -> 58 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 46 -> 61 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 53 -> 46 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 45 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 44 -> 64 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 47 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 56 -> 45 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 54 -> 56 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 45 -> 44 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 44 -> 64 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 58 -> 60 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 61 -> 58 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 53 -> 61 at (2101.5, 3024.5), 2 frames after previous cover
- f110: ref 79110: 47 -> 66 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 58 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 46 -> 58 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 61 -> 46 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 53 -> 61 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 66 -> 53 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 47 -> 66 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 56 -> 45 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 54 -> 56 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 60 -> 54 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 45 -> 56 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 64 -> 69 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 56 -> 54 at (2040.5, 3031), 1 frames after previous cover
- ... 467 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 992 | 9 | 2 (992) |
| 78896 | 350 (76..429) | 337 | 10 | 73 (243), 41 (94) |
| 78969 | 352 (80..434) | 330 | 14 | 58 (153), 41 (98), 73 (50), 44 (15), 59 (14) |
| 78971 | 352 (84..439) | 326 | 15 | 155 (107), 58 (101), 78 (54), 44 (50), 59 (4), 47 (3), 45 (2), 56 (2), 69 (2), 64 (1) |
| 79045 | 355 (84..443) | 331 | 13 | 78 (118), 44 (80), 89 (53), 155 (51), 45 (18), 64 (5), 59 (3), 69 (2), 58 (1) |
| 79037 | 355 (86..445) | 331 | 17 | 44 (164), 78 (70), 89 (59), 59 (12), 56 (7), 45 (4), 69 (4), 46 (3), 54 (3), 64 (3), 47 (2) |
| 78897 | 345 (89..450) | 327 | 12 | 89 (175), 78 (53), 44 (36), 59 (23), 69 (13), 60 (4), 56 (4), 45 (4), 64 (4), 54 (4), 46 (3), 47 (2), +1 more |
| 78899 | 365 (91..455) | 350 | 14 | 54 (225), 59 (47), 69 (25), 64 (13), 89 (8), 44 (8), 56 (7), 45 (7), 46 (4), 78 (4), 53 (2) |
| 79097 | 366 (94..461) | 346 | 16 | 56 (162), 59 (73), 54 (46), 69 (26), 58 (24), 45 (5), 60 (4), 47 (3), 46 (1), 53 (1), 64 (1) |
| 79098 | 360 (97..467) | 347 | 12 | 56 (77), 59 (68), 69 (66), 54 (45), 45 (40), 64 (20), 58 (15), 61 (10), 53 (2), 60 (2), 47 (1), 46 (1) |
| 79102 | 371 (98..477) | 355 | 15 | 61 (225), 64 (33), 59 (29), 54 (25), 58 (11), 60 (8), 56 (7), 69 (7), 46 (4), 45 (3), 53 (2), 47 (1) |
| 79103 | 380 (99..481) | 365 | 14 | 61 (101), 59 (92), 60 (60), 45 (50), 69 (21), 56 (11), 58 (10), 46 (8), 64 (8), 47 (2), 53 (2) |
| 79105 | 379 (101..484) | 365 | 12 | 45 (136), 60 (64), 46 (59), 56 (56), 61 (18), 69 (12), 64 (8), 129 (6), 53 (4), 47 (1), 81 (1) |
| 79108 | 385 (104..492) | 366 | 16 | 69 (110), 46 (68), 60 (67), 182 (60), 66 (21), 56 (16), 61 (10), 45 (5), 47 (3), 71 (3), 53 (2), 77 (1) |
| 79110 | 388 (106..497) | 374 | 11 | 182 (78), 77 (67), 69 (66), 81 (43), 45 (30), 46 (25), 60 (24), 71 (11), 66 (10), 129 (7), 56 (6), 53 (3), +2 more |
| 79111 | 386 (109..500) | 375 | 10 | 66 (139), 129 (86), 45 (60), 46 (54), 77 (14), 53 (6), 71 (4), 60 (4), 182 (4), 47 (2), 81 (1), 56 (1) |
| 79115 | 421 (111..531) | 408 | 10 | 60 (186), 72 (82), 46 (77), 47 (15), 77 (12), 53 (8), 129 (8), 66 (7), 81 (7), 71 (6) |
| 79116 | 411 (114..530) | 397 | 10 | 129 (96), 46 (82), 66 (73), 72 (63), 64 (26), 77 (22), 47 (19), 71 (12), 53 (2), 81 (1), 85 (1) |
| 79122 | 404 (118..532) | 390 | 10 | 71 (143), 64 (103), 129 (84), 66 (24), 72 (21), 47 (9), 77 (6) |
| 79132 | 391 (120..515) | 375 | 12 | 72 (112), 47 (95), 71 (83), 77 (43), 66 (37), 53 (5) |
| 79128 | 402 (124..527) | 396 | 4 | 71 (135), 64 (100), 66 (77), 53 (53), 47 (15), 72 (10), 77 (3), 129 (3) |
| 79134 | 407 (127..533) | 397 | 10 | 47 (154), 64 (91), 85 (64), 53 (42), 72 (37), 77 (5), 69 (3), 182 (1) |
| 79135 | 409 (129..542) | 394 | 10 | 53 (122), 47 (108), 85 (102), 72 (53), 77 (7), 69 (2) |
| 79139 | 406 (132..537) | 394 | 10 | 85 (217), 53 (167), 72 (10) |
| 79136 | 393 (136..538) | 381 | 8 | 90 (375), 85 (4), 71 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 437 | 910..939 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 30/405/1004; tracks with internal gaps: 26; total internal gaps: 241; longest internal gap: 28; tracks ending in coasting: 28 (trailing rows total 876)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 992 | 12 | 9 | 3 | 0 | 78911 |
| 41 | 78..318 | 241 | 241 | 192 | 49 | 2 | 1 | 47 | 78896, 78969 |
| 44 | 82..484 | 403 | 403 | 353 | 50 | 12 | 5 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 45 | 86..496 | 411 | 411 | 364 | 47 | 8 | 11 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 46 | 86..513 | 428 | 428 | 389 | 39 | 10 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 47 | 87..606 | 520 | 520 | 437 | 83 | 16 | 2 | 64 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 53 | 93..562 | 470 | 470 | 425 | 45 | 11 | 5 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79139 |
| 54 | 96..477 | 382 | 382 | 348 | 34 | 4 | 1 | 30 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 56 | 97..490 | 394 | 394 | 356 | 38 | 8 | 2 | 29 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 58 | 99..463 | 365 | 365 | 315 | 50 | 15 | 3 | 29 | 78969, 78971, 79045, 79097, 79098, 79102, 79103 |
| 59 | 102..510 | 409 | 409 | 365 | 44 | 11 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 60 | 102..560 | 459 | 459 | 423 | 36 | 5 | 3 | 29 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 61 | 103..507 | 405 | 405 | 366 | 39 | 9 | 1 | 30 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 64 | 109..561 | 453 | 453 | 416 | 37 | 8 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79116, 79122, 79128, 79134 |
| 66 | 110..529 | 420 | 420 | 388 | 32 | 3 | 1 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 113..568 | 456 | 456 | 359 | 97 | 20 | 25 | 35 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79134, 79135 |
| 71 | 117..556 | 440 | 440 | 399 | 41 | 11 | 9 | 18 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136 |
| 72 | 120..543 | 424 | 424 | 388 | 36 | 5 | 3 | 28 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 73 | 120..458 | 339 | 339 | 293 | 46 | 12 | 4 | 29 | 78896, 78969 |
| 77 | 127..366 | 240 | 240 | 180 | 60 | 3 | 1 | 57 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 78 | 127..472 | 346 | 346 | 299 | 47 | 14 | 3 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 81 | 133..221 | 89 | 89 | 53 | 36 | 0 | 0 | 36 | 79105, 79110, 79111, 79115, 79116 |
| 85 | 138..566 | 429 | 429 | 388 | 41 | 9 | 2 | 29 | 79116, 79134, 79135, 79136, 79139 |
| 89 | 145..478 | 334 | 334 | 295 | 39 | 11 | 1 | 28 | 78897, 78899, 79037, 79045 |
| 90 | 145..567 | 423 | 423 | 375 | 48 | 14 | 2 | 31 | 79136 |
| 129 | 231..559 | 329 | 329 | 290 | 39 | 9 | 2 | 29 | 79105, 79110, 79111, 79115, 79116, 79122, 79128 |
| 155 | 282..468 | 187 | 187 | 158 | 29 | 0 | 0 | 29 | 78971, 79045 |
| 182 | 350..528 | 179 | 179 | 143 | 36 | 2 | 28 | 7 | 79108, 79110, 79111, 79134 |
| 437 | 910..939 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
