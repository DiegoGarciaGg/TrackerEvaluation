# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=06fdf0c60665
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise3.0_fp0.0_seed1/tracks.csv sha256=682f217bc8cbb17d
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise3.0_fp0.0_seed1.csv sha256=06fdf0c60665d0db
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise3.0_fp0.0_seed1
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
| observations | none | 4 | 0.360 | 0.301 | 0.160 | 2.40 | 0.481 | 131 | 2497.0 |
| observations | none | 6 | 0.512 | 0.439 | 0.714 | 3.20 | 0.715 | 115 | 1269.0 |
| observations | none | 8 | 0.599 | 0.530 | 0.920 | 3.59 | 0.809 | 101 | 431.0 |
| observations | none | 12 | 0.694 | 0.629 | 0.977 | 3.84 | 0.862 | 86 | 162.0 |
| observations | ignore | 4 | 0.360 | 0.301 | 0.160 | 2.40 | 0.481 | 131 | 2497.0 |
| observations | ignore | 6 | 0.512 | 0.439 | 0.714 | 3.20 | 0.715 | 115 | 1269.0 |
| observations | ignore | 8 | 0.599 | 0.530 | 0.920 | 3.59 | 0.809 | 101 | 431.0 |
| observations | ignore | 12 | 0.694 | 0.629 | 0.977 | 3.84 | 0.862 | 86 | 162.0 |
| updates | none | 4 | 0.339 | 0.285 | 0.081 | 2.40 | 0.463 | 143 | 2495.0 |
| updates | none | 6 | 0.480 | 0.413 | 0.634 | 3.20 | 0.687 | 115 | 1264.0 |
| updates | none | 8 | 0.560 | 0.498 | 0.840 | 3.59 | 0.778 | 97 | 428.0 |
| updates | none | 12 | 0.649 | 0.591 | 0.897 | 3.84 | 0.830 | 74 | 162.0 |
| updates | ignore | 4 | 0.339 | 0.285 | 0.081 | 2.40 | 0.463 | 143 | 2495.0 |
| updates | ignore | 6 | 0.480 | 0.413 | 0.634 | 3.20 | 0.687 | 115 | 1264.0 |
| updates | ignore | 8 | 0.560 | 0.498 | 0.840 | 3.59 | 0.778 | 97 | 428.0 |
| updates | ignore | 12 | 0.649 | 0.591 | 0.897 | 3.84 | 0.830 | 74 | 162.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9760; unmatched reference entries: 382; unmatched candidate entries: 332
- identity switches: 101; fragmentation (coverage interruptions): 329; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f94: ref 78899: 4 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78971: 3 -> 5 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 5 -> 3 at (2100.5, 3033), 4 frames after previous cover
- f96: ref 78897: 7 -> 8 at (2112.5, 3033), 3 frames after previous cover
- f98: ref 79097: 4 -> 7 at (2129, 3028), 2 frames after previous cover
- f99: ref 79102: 4 -> 9 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 7 -> 10 at (2104, 3030.5), 3 frames after previous cover
- f102: ref 79102: 9 -> 11 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 4 -> 9 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 4 -> 12 at (2113.5, 3027), 6 frames after previous cover
- f104: ref 79105: 4 -> 9 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 11 -> 13 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 9 -> 11 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 4 -> 14 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 4 -> 14 at (2139.5, 3026.5), 1 frames after previous cover
- f111: ref 79108: 14 -> 15 at (2113.5, 3026), 3 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f119: ref 79111: 4 -> 14 at (2098.5, 3028.5), 1 frames after previous cover
- f120: ref 79111: 14 -> 4 at (2091.5, 3030), 1 frames after previous cover
- f129: ref 79105: 9 -> 13 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 15 -> 9 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 14 -> 15 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 4 -> 14 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 16 -> 4 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 18 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 19 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 19 -> 18 at (2107.5, 3023), 1 frames after previous cover
- f130: ref 79102: 13 -> 11 at (1965, 3030), 2 frames after previous cover
- f130: ref 79103: 11 -> 13 at (1974, 3024.5), 1 frames after previous cover
- f132: ref 79105: 13 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f138: ref 79128: 19 -> 20 at (2075, 3024), 1 frames after previous cover
- f139: ref 79134: 20 -> 19 at (2085, 3025), 2 frames after previous cover
- f147: ref 78971: 5 -> 3 at (1748.5, 3031), 1 frames after previous cover
- f147: ref 79045: 3 -> 5 at (1758.5, 3031.5), 2 frames after previous cover
- f158: ref 79111: 14 -> 17 at (1873.5, 3022), 1 frames after previous cover
- f158: ref 79115: 17 -> 14 at (1882, 3022), 1 frames after previous cover
- f168: ref 79115: 14 -> 4 at (1819, 3023.5), 1 frames after previous cover
- f168: ref 79116: 4 -> 14 at (1834, 3021), 1 frames after previous cover
- f175: ref 79098: 12 -> 11 at (1669.5, 3026.5), 2 frames after previous cover
- f176: ref 79102: 11 -> 12 at (1676.5, 3023.5), 2 frames after previous cover
- f194: ref 79132: 18 -> 16 at (1692.5, 3016), 1 frames after previous cover
- f195: ref 79122: 16 -> 18 at (1681, 3019), 2 frames after previous cover
- f198: ref 79116: 14 -> 4 at (1644.5, 3011.5), 2 frames after previous cover
- f200: ref 79115: 4 -> 14 at (1623, 3011), 1 frames after previous cover
- f202: ref 79110: 15 -> 17 at (1592.5, 3012), 2 frames after previous cover
- f202: ref 79111: 17 -> 15 at (1601.5, 3011.5), 1 frames after previous cover
- f210: ref 79132: 16 -> 18 at (1586.5, 3007.5), 2 frames after previous cover
- f211: ref 79132: 18 -> 16 at (1579, 3004.5), 1 frames after previous cover
- f244: ref 79132: 16 -> 4 at (1374, 2986), 1 frames after previous cover
- f245: ref 79116: 4 -> 18 at (1358, 2997), 2 frames after previous cover
- f246: ref 79110: 17 -> 15 at (1325, 2990.5), 1 frames after previous cover
- f246: ref 79111: 15 -> 17 at (1335, 2995.5), 1 frames after previous cover
- f246: ref 79122: 18 -> 16 at (1360, 2994.5), 2 frames after previous cover
- f247: ref 79037: 6 -> 5 at (1119.5, 2987), 2 frames after previous cover
- f247: ref 79045: 5 -> 6 at (1105.5, 2986.5), 1 frames after previous cover
- f248: ref 79116: 18 -> 16 at (1340.5, 2995), 1 frames after previous cover
- f248: ref 79122: 16 -> 18 at (1349, 2995.5), 2 frames after previous cover
- f256: ref 79115: 14 -> 18 at (1284.5, 2991.5), 1 frames after previous cover
- ... 41 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 341 | 7 | 1 (341) |
| 78969 | 352 (80..434) | 333 | 16 | 2 (333) |
| 78971 | 352 (84..439) | 342 | 8 | 3 (289), 5 (53) |
| 79045 | 355 (84..443) | 336 | 11 | 6 (186), 5 (102), 3 (48) |
| 79037 | 355 (86..445) | 341 | 13 | 5 (185), 6 (153), 4 (3) |
| 78897 | 345 (89..450) | 331 | 12 | 8 (328), 4 (2), 7 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 10 (340), 7 (4), 4 (3) |
| 79097 | 366 (94..461) | 354 | 12 | 7 (351), 4 (3) |
| 79098 | 360 (97..467) | 345 | 11 | 11 (275), 12 (69), 4 (1) |
| 79102 | 371 (98..477) | 360 | 11 | 12 (288), 11 (46), 13 (22), 9 (3), 4 (1) |
| 79103 | 380 (99..481) | 372 | 7 | 13 (344), 11 (23), 4 (2), 9 (2), 12 (1) |
| 79105 | 379 (101..484) | 361 | 16 | 22 (332), 9 (25), 4 (2), 13 (2) |
| 79108 | 385 (104..492) | 372 | 10 | 9 (351), 15 (18), 4 (2), 14 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 17 (274), 15 (87), 14 (19), 4 (2) |
| 79111 | 386 (109..500) | 369 | 15 | 15 (264), 17 (58), 14 (29), 4 (18) |
| 79115 | 421 (111..531) | 404 | 13 | 14 (305), 17 (42), 4 (29), 18 (21), 16 (7) |
| 79116 | 411 (114..530) | 395 | 15 | 18 (245), 4 (83), 14 (41), 16 (26) |
| 79122 | 404 (118..532) | 390 | 12 | 16 (321), 18 (60), 14 (9) |
| 79132 | 391 (120..515) | 375 | 14 | 4 (179), 20 (79), 18 (64), 16 (46), 19 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 20 (287), 4 (92), 19 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 19 (334), 24 (39), 20 (9), 23 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (303), 23 (93), 24 (1) |
| 79139 | 406 (132..537) | 389 | 14 | 23 (231), 21 (92), 19 (46), 24 (20) |
| 79136 | 393 (136..538) | 378 | 13 | 24 (310), 23 (64), 19 (3), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 352/382/1007; tracks with internal gaps: 25; total internal gaps: 316; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 341 | 7 | 7 | 1 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 333 | 17 | 16 | 2 | 0 | 78969 |
| 3 | 86..439 | 354 | 351 | 337 | 14 | 13 | 2 | 0 | 78971, 79045 |
| 4 | 86..527 | 442 | 434 | 422 | 12 | 11 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132 |
| 5 | 88..445 | 358 | 353 | 340 | 13 | 11 | 3 | 0 | 78971, 79037, 79045 |
| 6 | 91..443 | 353 | 347 | 339 | 8 | 8 | 1 | 0 | 79037, 79045 |
| 7 | 93..461 | 369 | 367 | 356 | 11 | 11 | 1 | 0 | 78897, 78899, 79097 |
| 8 | 96..450 | 355 | 338 | 328 | 10 | 10 | 1 | 0 | 78897 |
| 9 | 99..492 | 394 | 390 | 381 | 9 | 8 | 2 | 0 | 79102, 79103, 79105, 79108 |
| 10 | 100..455 | 356 | 356 | 340 | 16 | 15 | 2 | 0 | 78899 |
| 11 | 101..467 | 367 | 356 | 344 | 12 | 12 | 1 | 0 | 79098, 79102, 79103 |
| 12 | 103..479 | 377 | 368 | 358 | 10 | 9 | 2 | 0 | 79098, 79102, 79103 |
| 13 | 106..481 | 376 | 373 | 368 | 5 | 5 | 1 | 0 | 79102, 79103, 79105 |
| 14 | 108..531 | 424 | 423 | 404 | 19 | 16 | 3 | 0 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 15 | 111..500 | 390 | 385 | 369 | 16 | 14 | 3 | 0 | 79108, 79110, 79111 |
| 16 | 113..532 | 420 | 413 | 400 | 13 | 13 | 1 | 0 | 79115, 79116, 79122, 79132 |
| 17 | 116..497 | 382 | 379 | 374 | 5 | 5 | 1 | 0 | 79110, 79111, 79115 |
| 18 | 120..530 | 411 | 402 | 390 | 12 | 12 | 1 | 0 | 79115, 79116, 79122, 79132 |
| 19 | 122..537 | 416 | 416 | 399 | 17 | 17 | 1 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 20 | 126..515 | 390 | 388 | 375 | 13 | 12 | 2 | 0 | 79128, 79132, 79134 |
| 21 | 129..542 | 414 | 410 | 396 | 14 | 14 | 1 | 0 | 79135, 79136, 79139 |
| 22 | 132..484 | 353 | 348 | 332 | 16 | 15 | 2 | 0 | 79105 |
| 23 | 134..538 | 405 | 403 | 391 | 12 | 11 | 2 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 138..533 | 396 | 387 | 370 | 17 | 17 | 1 | 0 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9760; unmatched reference entries: 382; unmatched candidate entries: 332
- identity switches: 101; fragmentation (coverage interruptions): 329; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f94: ref 78899: 4 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78971: 3 -> 5 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 5 -> 3 at (2100.5, 3033), 4 frames after previous cover
- f96: ref 78897: 7 -> 8 at (2112.5, 3033), 3 frames after previous cover
- f98: ref 79097: 4 -> 7 at (2129, 3028), 2 frames after previous cover
- f99: ref 79102: 4 -> 9 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 7 -> 10 at (2104, 3030.5), 3 frames after previous cover
- f102: ref 79102: 9 -> 11 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 4 -> 9 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 4 -> 12 at (2113.5, 3027), 6 frames after previous cover
- f104: ref 79105: 4 -> 9 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 11 -> 13 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 9 -> 11 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 4 -> 14 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 4 -> 14 at (2139.5, 3026.5), 1 frames after previous cover
- f111: ref 79108: 14 -> 15 at (2113.5, 3026), 3 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f119: ref 79111: 4 -> 14 at (2098.5, 3028.5), 1 frames after previous cover
- f120: ref 79111: 14 -> 4 at (2091.5, 3030), 1 frames after previous cover
- f129: ref 79105: 9 -> 13 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 15 -> 9 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 14 -> 15 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 4 -> 14 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 16 -> 4 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 18 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 19 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 19 -> 18 at (2107.5, 3023), 1 frames after previous cover
- f130: ref 79102: 13 -> 11 at (1965, 3030), 2 frames after previous cover
- f130: ref 79103: 11 -> 13 at (1974, 3024.5), 1 frames after previous cover
- f132: ref 79105: 13 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f138: ref 79128: 19 -> 20 at (2075, 3024), 1 frames after previous cover
- f139: ref 79134: 20 -> 19 at (2085, 3025), 2 frames after previous cover
- f147: ref 78971: 5 -> 3 at (1748.5, 3031), 1 frames after previous cover
- f147: ref 79045: 3 -> 5 at (1758.5, 3031.5), 2 frames after previous cover
- f158: ref 79111: 14 -> 17 at (1873.5, 3022), 1 frames after previous cover
- f158: ref 79115: 17 -> 14 at (1882, 3022), 1 frames after previous cover
- f168: ref 79115: 14 -> 4 at (1819, 3023.5), 1 frames after previous cover
- f168: ref 79116: 4 -> 14 at (1834, 3021), 1 frames after previous cover
- f175: ref 79098: 12 -> 11 at (1669.5, 3026.5), 2 frames after previous cover
- f176: ref 79102: 11 -> 12 at (1676.5, 3023.5), 2 frames after previous cover
- f194: ref 79132: 18 -> 16 at (1692.5, 3016), 1 frames after previous cover
- f195: ref 79122: 16 -> 18 at (1681, 3019), 2 frames after previous cover
- f198: ref 79116: 14 -> 4 at (1644.5, 3011.5), 2 frames after previous cover
- f200: ref 79115: 4 -> 14 at (1623, 3011), 1 frames after previous cover
- f202: ref 79110: 15 -> 17 at (1592.5, 3012), 2 frames after previous cover
- f202: ref 79111: 17 -> 15 at (1601.5, 3011.5), 1 frames after previous cover
- f210: ref 79132: 16 -> 18 at (1586.5, 3007.5), 2 frames after previous cover
- f211: ref 79132: 18 -> 16 at (1579, 3004.5), 1 frames after previous cover
- f244: ref 79132: 16 -> 4 at (1374, 2986), 1 frames after previous cover
- f245: ref 79116: 4 -> 18 at (1358, 2997), 2 frames after previous cover
- f246: ref 79110: 17 -> 15 at (1325, 2990.5), 1 frames after previous cover
- f246: ref 79111: 15 -> 17 at (1335, 2995.5), 1 frames after previous cover
- f246: ref 79122: 18 -> 16 at (1360, 2994.5), 2 frames after previous cover
- f247: ref 79037: 6 -> 5 at (1119.5, 2987), 2 frames after previous cover
- f247: ref 79045: 5 -> 6 at (1105.5, 2986.5), 1 frames after previous cover
- f248: ref 79116: 18 -> 16 at (1340.5, 2995), 1 frames after previous cover
- f248: ref 79122: 16 -> 18 at (1349, 2995.5), 2 frames after previous cover
- f256: ref 79115: 14 -> 18 at (1284.5, 2991.5), 1 frames after previous cover
- ... 41 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 341 | 7 | 1 (341) |
| 78969 | 352 (80..434) | 333 | 16 | 2 (333) |
| 78971 | 352 (84..439) | 342 | 8 | 3 (289), 5 (53) |
| 79045 | 355 (84..443) | 336 | 11 | 6 (186), 5 (102), 3 (48) |
| 79037 | 355 (86..445) | 341 | 13 | 5 (185), 6 (153), 4 (3) |
| 78897 | 345 (89..450) | 331 | 12 | 8 (328), 4 (2), 7 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 10 (340), 7 (4), 4 (3) |
| 79097 | 366 (94..461) | 354 | 12 | 7 (351), 4 (3) |
| 79098 | 360 (97..467) | 345 | 11 | 11 (275), 12 (69), 4 (1) |
| 79102 | 371 (98..477) | 360 | 11 | 12 (288), 11 (46), 13 (22), 9 (3), 4 (1) |
| 79103 | 380 (99..481) | 372 | 7 | 13 (344), 11 (23), 4 (2), 9 (2), 12 (1) |
| 79105 | 379 (101..484) | 361 | 16 | 22 (332), 9 (25), 4 (2), 13 (2) |
| 79108 | 385 (104..492) | 372 | 10 | 9 (351), 15 (18), 4 (2), 14 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 17 (274), 15 (87), 14 (19), 4 (2) |
| 79111 | 386 (109..500) | 369 | 15 | 15 (264), 17 (58), 14 (29), 4 (18) |
| 79115 | 421 (111..531) | 404 | 13 | 14 (305), 17 (42), 4 (29), 18 (21), 16 (7) |
| 79116 | 411 (114..530) | 395 | 15 | 18 (245), 4 (83), 14 (41), 16 (26) |
| 79122 | 404 (118..532) | 390 | 12 | 16 (321), 18 (60), 14 (9) |
| 79132 | 391 (120..515) | 375 | 14 | 4 (179), 20 (79), 18 (64), 16 (46), 19 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 20 (287), 4 (92), 19 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 19 (334), 24 (39), 20 (9), 23 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (303), 23 (93), 24 (1) |
| 79139 | 406 (132..537) | 389 | 14 | 23 (231), 21 (92), 19 (46), 24 (20) |
| 79136 | 393 (136..538) | 378 | 13 | 24 (310), 23 (64), 19 (3), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 352/382/1007; tracks with internal gaps: 25; total internal gaps: 316; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 341 | 7 | 7 | 1 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 333 | 17 | 16 | 2 | 0 | 78969 |
| 3 | 86..439 | 354 | 351 | 337 | 14 | 13 | 2 | 0 | 78971, 79045 |
| 4 | 86..527 | 442 | 434 | 422 | 12 | 11 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132 |
| 5 | 88..445 | 358 | 353 | 340 | 13 | 11 | 3 | 0 | 78971, 79037, 79045 |
| 6 | 91..443 | 353 | 347 | 339 | 8 | 8 | 1 | 0 | 79037, 79045 |
| 7 | 93..461 | 369 | 367 | 356 | 11 | 11 | 1 | 0 | 78897, 78899, 79097 |
| 8 | 96..450 | 355 | 338 | 328 | 10 | 10 | 1 | 0 | 78897 |
| 9 | 99..492 | 394 | 390 | 381 | 9 | 8 | 2 | 0 | 79102, 79103, 79105, 79108 |
| 10 | 100..455 | 356 | 356 | 340 | 16 | 15 | 2 | 0 | 78899 |
| 11 | 101..467 | 367 | 356 | 344 | 12 | 12 | 1 | 0 | 79098, 79102, 79103 |
| 12 | 103..479 | 377 | 368 | 358 | 10 | 9 | 2 | 0 | 79098, 79102, 79103 |
| 13 | 106..481 | 376 | 373 | 368 | 5 | 5 | 1 | 0 | 79102, 79103, 79105 |
| 14 | 108..531 | 424 | 423 | 404 | 19 | 16 | 3 | 0 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 15 | 111..500 | 390 | 385 | 369 | 16 | 14 | 3 | 0 | 79108, 79110, 79111 |
| 16 | 113..532 | 420 | 413 | 400 | 13 | 13 | 1 | 0 | 79115, 79116, 79122, 79132 |
| 17 | 116..497 | 382 | 379 | 374 | 5 | 5 | 1 | 0 | 79110, 79111, 79115 |
| 18 | 120..530 | 411 | 402 | 390 | 12 | 12 | 1 | 0 | 79115, 79116, 79122, 79132 |
| 19 | 122..537 | 416 | 416 | 399 | 17 | 17 | 1 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 20 | 126..515 | 390 | 388 | 375 | 13 | 12 | 2 | 0 | 79128, 79132, 79134 |
| 21 | 129..542 | 414 | 410 | 396 | 14 | 14 | 1 | 0 | 79135, 79136, 79139 |
| 22 | 132..484 | 353 | 348 | 332 | 16 | 15 | 2 | 0 | 79105 |
| 23 | 134..538 | 405 | 403 | 391 | 12 | 11 | 2 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 138..533 | 396 | 387 | 370 | 17 | 17 | 1 | 0 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9761; unmatched reference entries: 381; unmatched candidate entries: 1149
- identity switches: 97; fragmentation (coverage interruptions): 326; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f94: ref 78899: 4 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78971: 3 -> 5 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 5 -> 3 at (2100.5, 3033), 4 frames after previous cover
- f96: ref 78897: 7 -> 8 at (2112.5, 3033), 3 frames after previous cover
- f98: ref 79097: 4 -> 7 at (2129, 3028), 2 frames after previous cover
- f99: ref 79102: 4 -> 9 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 7 -> 10 at (2104, 3030.5), 3 frames after previous cover
- f102: ref 79102: 9 -> 11 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 4 -> 9 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 4 -> 12 at (2113.5, 3027), 6 frames after previous cover
- f104: ref 79105: 4 -> 9 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 11 -> 13 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 9 -> 11 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 4 -> 14 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 4 -> 14 at (2139.5, 3026.5), 1 frames after previous cover
- f111: ref 79108: 14 -> 15 at (2113.5, 3026), 3 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 9 -> 13 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 15 -> 9 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 14 -> 15 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 4 -> 14 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 16 -> 4 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 18 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 19 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 19 -> 18 at (2107.5, 3023), 1 frames after previous cover
- f130: ref 79102: 13 -> 11 at (1965, 3030), 2 frames after previous cover
- f130: ref 79103: 11 -> 13 at (1974, 3024.5), 1 frames after previous cover
- f132: ref 79105: 13 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f138: ref 79128: 19 -> 20 at (2075, 3024), 1 frames after previous cover
- f139: ref 79134: 20 -> 19 at (2085, 3025), 2 frames after previous cover
- f147: ref 78971: 5 -> 3 at (1748.5, 3031), 1 frames after previous cover
- f147: ref 79045: 3 -> 5 at (1758.5, 3031.5), 2 frames after previous cover
- f158: ref 79111: 14 -> 17 at (1873.5, 3022), 1 frames after previous cover
- f158: ref 79115: 17 -> 14 at (1882, 3022), 1 frames after previous cover
- f168: ref 79115: 14 -> 4 at (1819, 3023.5), 1 frames after previous cover
- f168: ref 79116: 4 -> 14 at (1834, 3021), 1 frames after previous cover
- f175: ref 79098: 12 -> 11 at (1669.5, 3026.5), 2 frames after previous cover
- f176: ref 79102: 11 -> 12 at (1676.5, 3023.5), 2 frames after previous cover
- f198: ref 79116: 14 -> 4 at (1644.5, 3011.5), 2 frames after previous cover
- f200: ref 79115: 4 -> 14 at (1623, 3011), 1 frames after previous cover
- f202: ref 79110: 15 -> 17 at (1592.5, 3012), 2 frames after previous cover
- f202: ref 79111: 17 -> 15 at (1601.5, 3011.5), 1 frames after previous cover
- f204: ref 79122: 16 -> 18 at (1622, 3014.5), 1 frames after previous cover
- f204: ref 79132: 18 -> 16 at (1625.5, 3009), 3 frames after previous cover
- f210: ref 79132: 16 -> 18 at (1586.5, 3007.5), 2 frames after previous cover
- f211: ref 79132: 18 -> 16 at (1579, 3004.5), 1 frames after previous cover
- f245: ref 79116: 4 -> 18 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 18 -> 4 at (1366, 2994.5), 1 frames after previous cover
- f246: ref 79110: 17 -> 15 at (1325, 2990.5), 1 frames after previous cover
- f246: ref 79111: 15 -> 17 at (1335, 2995.5), 1 frames after previous cover
- f247: ref 79037: 6 -> 5 at (1119.5, 2987), 2 frames after previous cover
- f247: ref 79045: 5 -> 6 at (1105.5, 2986.5), 1 frames after previous cover
- f247: ref 79132: 16 -> 4 at (1355.5, 2984.5), 1 frames after previous cover
- f248: ref 79116: 18 -> 16 at (1340.5, 2995), 1 frames after previous cover
- f248: ref 79122: 4 -> 18 at (1349, 2995.5), 3 frames after previous cover
- f256: ref 79115: 14 -> 18 at (1284.5, 2991.5), 1 frames after previous cover
- f256: ref 79122: 18 -> 14 at (1301, 2991), 2 frames after previous cover
- f260: ref 79116: 16 -> 14 at (1269, 2989), 1 frames after previous cover
- ... 37 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 341 | 7 | 1 (341) |
| 78969 | 352 (80..434) | 333 | 16 | 2 (333) |
| 78971 | 352 (84..439) | 343 | 7 | 3 (290), 5 (53) |
| 79045 | 355 (84..443) | 336 | 11 | 6 (186), 5 (102), 3 (48) |
| 79037 | 355 (86..445) | 341 | 13 | 5 (185), 6 (153), 4 (3) |
| 78897 | 345 (89..450) | 331 | 12 | 8 (328), 4 (2), 7 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 10 (340), 7 (4), 4 (3) |
| 79097 | 366 (94..461) | 355 | 11 | 7 (349), 4 (3), 10 (3) |
| 79098 | 360 (97..467) | 345 | 11 | 11 (275), 12 (69), 4 (1) |
| 79102 | 371 (98..477) | 360 | 11 | 12 (288), 11 (46), 13 (22), 9 (3), 4 (1) |
| 79103 | 380 (99..481) | 372 | 7 | 13 (342), 11 (23), 12 (3), 4 (2), 9 (2) |
| 79105 | 379 (101..484) | 361 | 16 | 22 (332), 9 (25), 4 (2), 13 (2) |
| 79108 | 385 (104..492) | 372 | 10 | 9 (351), 15 (18), 4 (2), 14 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 17 (274), 15 (87), 14 (19), 4 (2) |
| 79111 | 386 (109..500) | 369 | 15 | 15 (264), 17 (58), 14 (28), 4 (19) |
| 79115 | 421 (111..531) | 404 | 13 | 14 (304), 17 (42), 4 (29), 18 (22), 16 (7) |
| 79116 | 411 (114..530) | 395 | 15 | 18 (245), 4 (83), 14 (41), 16 (26) |
| 79122 | 404 (118..532) | 389 | 12 | 16 (327), 18 (51), 14 (10), 4 (1) |
| 79132 | 391 (120..515) | 373 | 15 | 4 (177), 20 (79), 18 (71), 16 (39), 19 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 20 (287), 4 (92), 19 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 19 (334), 24 (39), 20 (9), 23 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (303), 23 (93), 24 (1) |
| 79139 | 406 (132..537) | 390 | 13 | 23 (232), 21 (92), 19 (46), 24 (20) |
| 79136 | 393 (136..538) | 379 | 12 | 24 (310), 23 (63), 19 (3), 18 (2), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 381/411/1007; tracks with internal gaps: 25; total internal gaps: 415; longest internal gap: 6; tracks ending in coasting: 24 (trailing rows total 688)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 341 | 40 | 9 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 333 | 49 | 17 | 2 | 29 | 78969 |
| 3 | 86..468 | 383 | 383 | 338 | 45 | 15 | 2 | 29 | 78971, 79045 |
| 4 | 86..556 | 471 | 471 | 422 | 49 | 19 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 5 | 88..474 | 387 | 387 | 340 | 47 | 14 | 3 | 29 | 78971, 79037, 79045 |
| 6 | 91..472 | 382 | 382 | 339 | 43 | 13 | 2 | 29 | 79037, 79045 |
| 7 | 93..490 | 398 | 398 | 354 | 44 | 12 | 1 | 32 | 78897, 78899, 79097 |
| 8 | 96..479 | 384 | 384 | 328 | 56 | 25 | 2 | 29 | 78897 |
| 9 | 99..521 | 423 | 423 | 381 | 42 | 12 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 10 | 100..484 | 385 | 385 | 343 | 42 | 16 | 3 | 23 | 78899, 79097 |
| 11 | 101..496 | 396 | 396 | 344 | 52 | 21 | 3 | 29 | 79098, 79102, 79103 |
| 12 | 103..508 | 406 | 406 | 360 | 46 | 18 | 2 | 27 | 79098, 79102, 79103 |
| 13 | 106..510 | 405 | 405 | 366 | 39 | 6 | 2 | 32 | 79102, 79103, 79105 |
| 14 | 108..560 | 453 | 453 | 403 | 50 | 19 | 3 | 28 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 15 | 111..529 | 419 | 419 | 369 | 50 | 17 | 3 | 29 | 79108, 79110, 79111 |
| 16 | 113..561 | 449 | 449 | 399 | 50 | 19 | 2 | 30 | 79115, 79116, 79122, 79132 |
| 17 | 116..526 | 411 | 411 | 374 | 37 | 8 | 1 | 29 | 79110, 79111, 79115 |
| 18 | 120..559 | 440 | 440 | 391 | 49 | 21 | 6 | 21 | 79115, 79116, 79122, 79132, 79136 |
| 19 | 122..566 | 445 | 445 | 399 | 46 | 17 | 1 | 29 | 79128, 79132, 79134, 79136, 79139 |
| 20 | 126..544 | 419 | 419 | 375 | 44 | 13 | 3 | 29 | 79128, 79132, 79134 |
| 21 | 129..571 | 443 | 443 | 396 | 47 | 18 | 1 | 29 | 79135, 79136, 79139 |
| 22 | 132..513 | 382 | 382 | 332 | 50 | 18 | 2 | 29 | 79105 |
| 23 | 134..567 | 434 | 434 | 391 | 43 | 11 | 2 | 31 | 79134, 79135, 79136, 79139 |
| 24 | 138..562 | 425 | 425 | 370 | 55 | 23 | 2 | 29 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9761; unmatched reference entries: 381; unmatched candidate entries: 1149
- identity switches: 97; fragmentation (coverage interruptions): 326; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f94: ref 78899: 4 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78971: 3 -> 5 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 5 -> 3 at (2100.5, 3033), 4 frames after previous cover
- f96: ref 78897: 7 -> 8 at (2112.5, 3033), 3 frames after previous cover
- f98: ref 79097: 4 -> 7 at (2129, 3028), 2 frames after previous cover
- f99: ref 79102: 4 -> 9 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78899: 7 -> 10 at (2104, 3030.5), 3 frames after previous cover
- f102: ref 79102: 9 -> 11 at (2130.5, 3027), 1 frames after previous cover
- f102: ref 79103: 4 -> 9 at (2139, 3022), 2 frames after previous cover
- f103: ref 79098: 4 -> 12 at (2113.5, 3027), 6 frames after previous cover
- f104: ref 79105: 4 -> 9 at (2137, 3025), 1 frames after previous cover
- f106: ref 79102: 11 -> 13 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 9 -> 11 at (2116.5, 3023), 3 frames after previous cover
- f108: ref 79108: 4 -> 14 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 4 -> 14 at (2139.5, 3026.5), 1 frames after previous cover
- f111: ref 79108: 14 -> 15 at (2113.5, 3026), 3 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 9 -> 13 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 15 -> 9 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 14 -> 15 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 4 -> 14 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 16 -> 4 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 18 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 19 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 19 -> 18 at (2107.5, 3023), 1 frames after previous cover
- f130: ref 79102: 13 -> 11 at (1965, 3030), 2 frames after previous cover
- f130: ref 79103: 11 -> 13 at (1974, 3024.5), 1 frames after previous cover
- f132: ref 79105: 13 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f138: ref 79128: 19 -> 20 at (2075, 3024), 1 frames after previous cover
- f139: ref 79134: 20 -> 19 at (2085, 3025), 2 frames after previous cover
- f147: ref 78971: 5 -> 3 at (1748.5, 3031), 1 frames after previous cover
- f147: ref 79045: 3 -> 5 at (1758.5, 3031.5), 2 frames after previous cover
- f158: ref 79111: 14 -> 17 at (1873.5, 3022), 1 frames after previous cover
- f158: ref 79115: 17 -> 14 at (1882, 3022), 1 frames after previous cover
- f168: ref 79115: 14 -> 4 at (1819, 3023.5), 1 frames after previous cover
- f168: ref 79116: 4 -> 14 at (1834, 3021), 1 frames after previous cover
- f175: ref 79098: 12 -> 11 at (1669.5, 3026.5), 2 frames after previous cover
- f176: ref 79102: 11 -> 12 at (1676.5, 3023.5), 2 frames after previous cover
- f198: ref 79116: 14 -> 4 at (1644.5, 3011.5), 2 frames after previous cover
- f200: ref 79115: 4 -> 14 at (1623, 3011), 1 frames after previous cover
- f202: ref 79110: 15 -> 17 at (1592.5, 3012), 2 frames after previous cover
- f202: ref 79111: 17 -> 15 at (1601.5, 3011.5), 1 frames after previous cover
- f204: ref 79122: 16 -> 18 at (1622, 3014.5), 1 frames after previous cover
- f204: ref 79132: 18 -> 16 at (1625.5, 3009), 3 frames after previous cover
- f210: ref 79132: 16 -> 18 at (1586.5, 3007.5), 2 frames after previous cover
- f211: ref 79132: 18 -> 16 at (1579, 3004.5), 1 frames after previous cover
- f245: ref 79116: 4 -> 18 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 18 -> 4 at (1366, 2994.5), 1 frames after previous cover
- f246: ref 79110: 17 -> 15 at (1325, 2990.5), 1 frames after previous cover
- f246: ref 79111: 15 -> 17 at (1335, 2995.5), 1 frames after previous cover
- f247: ref 79037: 6 -> 5 at (1119.5, 2987), 2 frames after previous cover
- f247: ref 79045: 5 -> 6 at (1105.5, 2986.5), 1 frames after previous cover
- f247: ref 79132: 16 -> 4 at (1355.5, 2984.5), 1 frames after previous cover
- f248: ref 79116: 18 -> 16 at (1340.5, 2995), 1 frames after previous cover
- f248: ref 79122: 4 -> 18 at (1349, 2995.5), 3 frames after previous cover
- f256: ref 79115: 14 -> 18 at (1284.5, 2991.5), 1 frames after previous cover
- f256: ref 79122: 18 -> 14 at (1301, 2991), 2 frames after previous cover
- f260: ref 79116: 16 -> 14 at (1269, 2989), 1 frames after previous cover
- ... 37 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 34 | 0 (973) |
| 78896 | 350 (76..429) | 341 | 7 | 1 (341) |
| 78969 | 352 (80..434) | 333 | 16 | 2 (333) |
| 78971 | 352 (84..439) | 343 | 7 | 3 (290), 5 (53) |
| 79045 | 355 (84..443) | 336 | 11 | 6 (186), 5 (102), 3 (48) |
| 79037 | 355 (86..445) | 341 | 13 | 5 (185), 6 (153), 4 (3) |
| 78897 | 345 (89..450) | 331 | 12 | 8 (328), 4 (2), 7 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 10 (340), 7 (4), 4 (3) |
| 79097 | 366 (94..461) | 355 | 11 | 7 (349), 4 (3), 10 (3) |
| 79098 | 360 (97..467) | 345 | 11 | 11 (275), 12 (69), 4 (1) |
| 79102 | 371 (98..477) | 360 | 11 | 12 (288), 11 (46), 13 (22), 9 (3), 4 (1) |
| 79103 | 380 (99..481) | 372 | 7 | 13 (342), 11 (23), 12 (3), 4 (2), 9 (2) |
| 79105 | 379 (101..484) | 361 | 16 | 22 (332), 9 (25), 4 (2), 13 (2) |
| 79108 | 385 (104..492) | 372 | 10 | 9 (351), 15 (18), 4 (2), 14 (1) |
| 79110 | 388 (106..497) | 382 | 6 | 17 (274), 15 (87), 14 (19), 4 (2) |
| 79111 | 386 (109..500) | 369 | 15 | 15 (264), 17 (58), 14 (28), 4 (19) |
| 79115 | 421 (111..531) | 404 | 13 | 14 (304), 17 (42), 4 (29), 18 (22), 16 (7) |
| 79116 | 411 (114..530) | 395 | 15 | 18 (245), 4 (83), 14 (41), 16 (26) |
| 79122 | 404 (118..532) | 389 | 12 | 16 (327), 18 (51), 14 (10), 4 (1) |
| 79132 | 391 (120..515) | 373 | 15 | 4 (177), 20 (79), 18 (71), 16 (39), 19 (7) |
| 79128 | 402 (124..527) | 388 | 11 | 20 (287), 4 (92), 19 (9) |
| 79134 | 407 (127..533) | 385 | 20 | 19 (334), 24 (39), 20 (9), 23 (3) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (303), 23 (93), 24 (1) |
| 79139 | 406 (132..537) | 390 | 13 | 23 (232), 21 (92), 19 (46), 24 (20) |
| 79136 | 393 (136..538) | 379 | 12 | 24 (310), 23 (63), 19 (3), 18 (2), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 381/411/1007; tracks with internal gaps: 25; total internal gaps: 415; longest internal gap: 6; tracks ending in coasting: 24 (trailing rows total 688)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 973 | 34 | 34 | 1 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 341 | 40 | 9 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 333 | 49 | 17 | 2 | 29 | 78969 |
| 3 | 86..468 | 383 | 383 | 338 | 45 | 15 | 2 | 29 | 78971, 79045 |
| 4 | 86..556 | 471 | 471 | 422 | 49 | 19 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 5 | 88..474 | 387 | 387 | 340 | 47 | 14 | 3 | 29 | 78971, 79037, 79045 |
| 6 | 91..472 | 382 | 382 | 339 | 43 | 13 | 2 | 29 | 79037, 79045 |
| 7 | 93..490 | 398 | 398 | 354 | 44 | 12 | 1 | 32 | 78897, 78899, 79097 |
| 8 | 96..479 | 384 | 384 | 328 | 56 | 25 | 2 | 29 | 78897 |
| 9 | 99..521 | 423 | 423 | 381 | 42 | 12 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 10 | 100..484 | 385 | 385 | 343 | 42 | 16 | 3 | 23 | 78899, 79097 |
| 11 | 101..496 | 396 | 396 | 344 | 52 | 21 | 3 | 29 | 79098, 79102, 79103 |
| 12 | 103..508 | 406 | 406 | 360 | 46 | 18 | 2 | 27 | 79098, 79102, 79103 |
| 13 | 106..510 | 405 | 405 | 366 | 39 | 6 | 2 | 32 | 79102, 79103, 79105 |
| 14 | 108..560 | 453 | 453 | 403 | 50 | 19 | 3 | 28 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 15 | 111..529 | 419 | 419 | 369 | 50 | 17 | 3 | 29 | 79108, 79110, 79111 |
| 16 | 113..561 | 449 | 449 | 399 | 50 | 19 | 2 | 30 | 79115, 79116, 79122, 79132 |
| 17 | 116..526 | 411 | 411 | 374 | 37 | 8 | 1 | 29 | 79110, 79111, 79115 |
| 18 | 120..559 | 440 | 440 | 391 | 49 | 21 | 6 | 21 | 79115, 79116, 79122, 79132, 79136 |
| 19 | 122..566 | 445 | 445 | 399 | 46 | 17 | 1 | 29 | 79128, 79132, 79134, 79136, 79139 |
| 20 | 126..544 | 419 | 419 | 375 | 44 | 13 | 3 | 29 | 79128, 79132, 79134 |
| 21 | 129..571 | 443 | 443 | 396 | 47 | 18 | 1 | 29 | 79135, 79136, 79139 |
| 22 | 132..513 | 382 | 382 | 332 | 50 | 18 | 2 | 29 | 79105 |
| 23 | 134..567 | 434 | 434 | 391 | 43 | 11 | 2 | 31 | 79134, 79135, 79136, 79139 |
| 24 | 138..562 | 425 | 425 | 370 | 55 | 23 | 2 | 29 | 79134, 79135, 79136, 79139 |
