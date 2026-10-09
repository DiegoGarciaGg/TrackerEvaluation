# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=ee92caaca298
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise0.0_fp0.0_seed2/tracks.csv sha256=df7759f29bf295ba
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise0.0_fp0.0_seed2.csv sha256=ee92caaca298739d
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise0.0_fp0.0_seed2
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
| observations | none | 4 | 0.429 | 0.233 | 0.733 | 0.01 | 0.414 | 577 | 1603.0 |
| observations | none | 6 | 0.428 | 0.235 | 0.732 | 0.01 | 0.415 | 579 | 1601.0 |
| observations | none | 8 | 0.428 | 0.236 | 0.733 | 0.02 | 0.417 | 577 | 1599.0 |
| observations | none | 12 | 0.429 | 0.242 | 0.736 | 0.25 | 0.438 | 534 | 1568.0 |
| observations | ignore | 4 | 0.429 | 0.233 | 0.733 | 0.01 | 0.414 | 577 | 1603.0 |
| observations | ignore | 6 | 0.428 | 0.235 | 0.732 | 0.01 | 0.415 | 579 | 1601.0 |
| observations | ignore | 8 | 0.428 | 0.236 | 0.733 | 0.02 | 0.417 | 577 | 1599.0 |
| observations | ignore | 12 | 0.429 | 0.242 | 0.736 | 0.25 | 0.438 | 534 | 1568.0 |
| updates | none | 4 | 0.395 | 0.225 | 0.534 | 0.09 | 0.381 | 612 | 1509.0 |
| updates | none | 6 | 0.422 | 0.242 | 0.636 | 0.39 | 0.408 | 627 | 1095.0 |
| updates | none | 8 | 0.438 | 0.254 | 0.749 | 0.79 | 0.442 | 580 | 673.0 |
| updates | none | 12 | 0.459 | 0.269 | 0.787 | 1.19 | 0.473 | 503 | 516.0 |
| updates | ignore | 4 | 0.395 | 0.225 | 0.534 | 0.09 | 0.381 | 612 | 1509.0 |
| updates | ignore | 6 | 0.422 | 0.242 | 0.636 | 0.39 | 0.408 | 627 | 1095.0 |
| updates | ignore | 8 | 0.438 | 0.254 | 0.749 | 0.79 | 0.442 | 580 | 673.0 |
| updates | ignore | 12 | 0.459 | 0.269 | 0.787 | 1.19 | 0.473 | 503 | 516.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8008; unmatched reference entries: 2134; unmatched candidate entries: 0
- identity switches: 577; fragmentation (coverage interruptions): 1607; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 3 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 2 -> 3 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 2 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 4 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f95: ref 79037: 3 -> 1 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 4 -> 9 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 78897: 2 -> 3 at (2112.5, 3033), 1 frames after previous cover
- f97: ref 78971: 8 -> 1 at (2072, 3034.5), 2 frames after previous cover
- f97: ref 79045: 1 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 7 -> 2 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 1 -> 8 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 8 -> 1 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 7 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 3 -> 2 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 1 -> 3 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 2 -> 3 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 3 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 3 -> 15 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 7 -> 14 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 7 -> 16 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 3 -> 15 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 15 -> 1 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 7 -> 16 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 16 -> 14 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 1 -> 20 at (2014.5, 3034), 6 frames after previous cover
- f108: ref 79103: 16 -> 21 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 16 -> 18 at (2113.5, 3025), 2 frames after previous cover
- f108: ref 79110: 7 -> 19 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 14 -> 2 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79108: 7 -> 16 at (2125, 3025), 4 frames after previous cover
- f110: ref 79098: 2 -> 14 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 18 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 18 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 19 -> 16 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 7 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 2 -> 14 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 21 -> 18 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 18 -> 16 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 14 -> 21 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 16 -> 19 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 21 -> 16 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 3 -> 20 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 20 -> 8 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 2 -> 15 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 21 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 18 -> 3 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 16 -> 18 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 19 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 15 -> 20 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 20 -> 14 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 1 -> 20 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 8 -> 1 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79116: 7 -> 22 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 79037: 20 -> 1 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 14 -> 15 at (2010.5, 3030), 3 frames after previous cover
- f118: ref 79098: 15 -> 2 at (2024.5, 3030.5), 1 frames after previous cover
- ... 517 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 171 | 0 (799) |
| 78896 | 350 (76..429) | 285 | 46 | 20 (232), 9 (42), 4 (6), 1 (5) |
| 78969 | 352 (80..434) | 276 | 55 | 9 (194), 8 (37), 4 (35), 20 (6), 1 (4) |
| 78971 | 352 (84..439) | 267 | 61 | 8 (121), 2 (86), 9 (45), 1 (5), 4 (5), 20 (4), 3 (1) |
| 79045 | 355 (84..443) | 282 | 52 | 8 (114), 23 (81), 16 (31), 1 (23), 2 (20), 20 (8), 3 (3), 9 (2) |
| 79037 | 355 (86..445) | 273 | 56 | 23 (111), 2 (99), 1 (22), 4 (18), 20 (8), 8 (8), 3 (5), 15 (1), 16 (1) |
| 78897 | 345 (89..450) | 273 | 58 | 4 (158), 2 (42), 23 (31), 20 (16), 15 (10), 3 (6), 33 (3), 14 (2), 8 (2), 16 (2), 1 (1) |
| 78899 | 365 (91..455) | 274 | 66 | 16 (97), 35 (76), 33 (44), 14 (18), 23 (10), 4 (10), 3 (7), 1 (6), 2 (3), 7 (1), 20 (1), 26 (1) |
| 79097 | 366 (94..461) | 292 | 57 | 33 (157), 14 (42), 1 (40), 35 (19), 23 (11), 2 (9), 26 (7), 15 (4), 7 (3) |
| 79098 | 360 (97..467) | 296 | 50 | 1 (164), 4 (65), 14 (25), 15 (11), 2 (9), 23 (9), 26 (8), 7 (3), 33 (2) |
| 79102 | 371 (98..477) | 297 | 59 | 26 (79), 14 (57), 29 (53), 1 (37), 15 (29), 33 (21), 23 (7), 7 (3), 2 (3), 21 (2), 18 (2), 4 (2), +2 more |
| 79103 | 380 (99..481) | 297 | 57 | 29 (77), 26 (74), 14 (33), 16 (28), 19 (24), 33 (22), 2 (10), 1 (10), 15 (8), 18 (4), 3 (4), 21 (3) |
| 79105 | 379 (101..484) | 288 | 71 | 14 (115), 26 (73), 19 (22), 16 (20), 29 (16), 2 (13), 3 (10), 15 (10), 18 (5), 21 (2), 7 (1), 28 (1) |
| 79108 | 385 (104..492) | 313 | 55 | 28 (120), 19 (87), 15 (35), 14 (30), 16 (18), 26 (15), 7 (2), 3 (2), 29 (2), 18 (1), 35 (1) |
| 79110 | 388 (106..497) | 308 | 60 | 18 (87), 28 (83), 19 (58), 26 (33), 16 (32), 15 (8), 21 (5), 7 (1), 3 (1) |
| 79111 | 386 (109..500) | 304 | 62 | 19 (97), 16 (40), 3 (39), 18 (34), 15 (32), 27 (32), 28 (27), 7 (2), 21 (1) |
| 79115 | 421 (111..531) | 319 | 75 | 21 (134), 3 (56), 19 (41), 18 (30), 27 (18), 15 (15), 28 (10), 29 (8), 16 (3), 7 (2), 22 (1), 35 (1) |
| 79116 | 411 (114..530) | 344 | 52 | 24 (126), 18 (73), 28 (66), 15 (21), 27 (15), 3 (14), 16 (9), 21 (7), 22 (4), 35 (4), 7 (3), 29 (2) |
| 79122 | 404 (118..532) | 325 | 65 | 22 (97), 21 (58), 29 (56), 18 (56), 27 (33), 35 (12), 16 (5), 7 (3), 3 (3), 28 (1), 15 (1) |
| 79132 | 391 (120..515) | 299 | 65 | 35 (140), 29 (61), 18 (34), 3 (32), 27 (17), 15 (6), 24 (3), 21 (3), 7 (2), 22 (1) |
| 79128 | 402 (124..527) | 321 | 64 | 27 (215), 3 (33), 15 (31), 24 (16), 21 (11), 35 (11), 7 (3), 22 (1) |
| 79134 | 407 (127..533) | 329 | 63 | 21 (131), 7 (95), 22 (38), 24 (29), 35 (15), 3 (12), 15 (7), 27 (2) |
| 79135 | 409 (129..542) | 322 | 61 | 24 (160), 3 (62), 15 (33), 38 (33), 22 (22), 7 (7), 35 (5) |
| 79139 | 406 (132..537) | 323 | 62 | 22 (159), 3 (70), 15 (53), 7 (29), 38 (12) |
| 79136 | 393 (136..538) | 302 | 64 | 7 (193), 38 (45), 15 (43), 22 (16), 3 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 112/381/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 799 | 799 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..460 | 383 | 317 | 317 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 2 | 84..450 | 367 | 294 | 294 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 3 | 87..542 | 456 | 365 | 365 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 4 | 87..467 | 381 | 299 | 299 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79098, 79102 |
| 7 | 93..533 | 441 | 353 | 353 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 94..434 | 341 | 282 | 282 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 9 | 96..439 | 344 | 283 | 283 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 14 | 103..484 | 382 | 322 | 322 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 15 | 103..536 | 434 | 358 | 358 | 0 | 0 | 0 | 0 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 103..443 | 341 | 287 | 287 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 18 | 108..495 | 388 | 326 | 326 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 108..500 | 393 | 329 | 329 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 108..429 | 322 | 275 | 275 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 108..531 | 424 | 357 | 357 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 117..532 | 416 | 339 | 339 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 122..445 | 324 | 260 | 260 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 24 | 126..530 | 405 | 334 | 334 | 0 | 0 | 0 | 0 | 79116, 79128, 79132, 79134, 79135 |
| 26 | 126..481 | 356 | 290 | 290 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 27 | 126..527 | 402 | 332 | 332 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 28 | 136..491 | 356 | 309 | 309 | 0 | 0 | 0 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 138..477 | 340 | 275 | 275 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79132 |
| 33 | 158..455 | 298 | 249 | 249 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 35 | 158..515 | 358 | 284 | 284 | 0 | 0 | 0 | 0 | 78899, 79097, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 38 | 427..538 | 112 | 90 | 90 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8008; unmatched reference entries: 2134; unmatched candidate entries: 0
- identity switches: 577; fragmentation (coverage interruptions): 1607; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 3 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 2 -> 3 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 2 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 4 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f95: ref 79037: 3 -> 1 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 4 -> 9 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 78897: 2 -> 3 at (2112.5, 3033), 1 frames after previous cover
- f97: ref 78971: 8 -> 1 at (2072, 3034.5), 2 frames after previous cover
- f97: ref 79045: 1 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 7 -> 2 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 1 -> 8 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 8 -> 1 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 7 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 3 -> 2 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 1 -> 3 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 2 -> 3 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 3 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 3 -> 15 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 7 -> 14 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 7 -> 16 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 3 -> 15 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 15 -> 1 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 7 -> 16 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 16 -> 14 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 1 -> 20 at (2014.5, 3034), 6 frames after previous cover
- f108: ref 79103: 16 -> 21 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 16 -> 18 at (2113.5, 3025), 2 frames after previous cover
- f108: ref 79110: 7 -> 19 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 14 -> 2 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79108: 7 -> 16 at (2125, 3025), 4 frames after previous cover
- f110: ref 79098: 2 -> 14 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 18 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 18 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 19 -> 16 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 7 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 2 -> 14 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 21 -> 18 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 18 -> 16 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 14 -> 21 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 16 -> 19 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 21 -> 16 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 3 -> 20 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 20 -> 8 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 2 -> 15 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 21 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 18 -> 3 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 16 -> 18 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 19 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 15 -> 20 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 20 -> 14 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 1 -> 20 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 8 -> 1 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79116: 7 -> 22 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 79037: 20 -> 1 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 14 -> 15 at (2010.5, 3030), 3 frames after previous cover
- f118: ref 79098: 15 -> 2 at (2024.5, 3030.5), 1 frames after previous cover
- ... 517 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 171 | 0 (799) |
| 78896 | 350 (76..429) | 285 | 46 | 20 (232), 9 (42), 4 (6), 1 (5) |
| 78969 | 352 (80..434) | 276 | 55 | 9 (194), 8 (37), 4 (35), 20 (6), 1 (4) |
| 78971 | 352 (84..439) | 267 | 61 | 8 (121), 2 (86), 9 (45), 1 (5), 4 (5), 20 (4), 3 (1) |
| 79045 | 355 (84..443) | 282 | 52 | 8 (114), 23 (81), 16 (31), 1 (23), 2 (20), 20 (8), 3 (3), 9 (2) |
| 79037 | 355 (86..445) | 273 | 56 | 23 (111), 2 (99), 1 (22), 4 (18), 20 (8), 8 (8), 3 (5), 15 (1), 16 (1) |
| 78897 | 345 (89..450) | 273 | 58 | 4 (158), 2 (42), 23 (31), 20 (16), 15 (10), 3 (6), 33 (3), 14 (2), 8 (2), 16 (2), 1 (1) |
| 78899 | 365 (91..455) | 274 | 66 | 16 (97), 35 (76), 33 (44), 14 (18), 23 (10), 4 (10), 3 (7), 1 (6), 2 (3), 7 (1), 20 (1), 26 (1) |
| 79097 | 366 (94..461) | 292 | 57 | 33 (157), 14 (42), 1 (40), 35 (19), 23 (11), 2 (9), 26 (7), 15 (4), 7 (3) |
| 79098 | 360 (97..467) | 296 | 50 | 1 (164), 4 (65), 14 (25), 15 (11), 2 (9), 23 (9), 26 (8), 7 (3), 33 (2) |
| 79102 | 371 (98..477) | 297 | 59 | 26 (79), 14 (57), 29 (53), 1 (37), 15 (29), 33 (21), 23 (7), 7 (3), 2 (3), 21 (2), 18 (2), 4 (2), +2 more |
| 79103 | 380 (99..481) | 297 | 57 | 29 (77), 26 (74), 14 (33), 16 (28), 19 (24), 33 (22), 2 (10), 1 (10), 15 (8), 18 (4), 3 (4), 21 (3) |
| 79105 | 379 (101..484) | 288 | 71 | 14 (115), 26 (73), 19 (22), 16 (20), 29 (16), 2 (13), 3 (10), 15 (10), 18 (5), 21 (2), 7 (1), 28 (1) |
| 79108 | 385 (104..492) | 313 | 55 | 28 (120), 19 (87), 15 (35), 14 (30), 16 (18), 26 (15), 7 (2), 3 (2), 29 (2), 18 (1), 35 (1) |
| 79110 | 388 (106..497) | 308 | 60 | 18 (87), 28 (83), 19 (58), 26 (33), 16 (32), 15 (8), 21 (5), 7 (1), 3 (1) |
| 79111 | 386 (109..500) | 304 | 62 | 19 (97), 16 (40), 3 (39), 18 (34), 15 (32), 27 (32), 28 (27), 7 (2), 21 (1) |
| 79115 | 421 (111..531) | 319 | 75 | 21 (134), 3 (56), 19 (41), 18 (30), 27 (18), 15 (15), 28 (10), 29 (8), 16 (3), 7 (2), 22 (1), 35 (1) |
| 79116 | 411 (114..530) | 344 | 52 | 24 (126), 18 (73), 28 (66), 15 (21), 27 (15), 3 (14), 16 (9), 21 (7), 22 (4), 35 (4), 7 (3), 29 (2) |
| 79122 | 404 (118..532) | 325 | 65 | 22 (97), 21 (58), 29 (56), 18 (56), 27 (33), 35 (12), 16 (5), 7 (3), 3 (3), 28 (1), 15 (1) |
| 79132 | 391 (120..515) | 299 | 65 | 35 (140), 29 (61), 18 (34), 3 (32), 27 (17), 15 (6), 24 (3), 21 (3), 7 (2), 22 (1) |
| 79128 | 402 (124..527) | 321 | 64 | 27 (215), 3 (33), 15 (31), 24 (16), 21 (11), 35 (11), 7 (3), 22 (1) |
| 79134 | 407 (127..533) | 329 | 63 | 21 (131), 7 (95), 22 (38), 24 (29), 35 (15), 3 (12), 15 (7), 27 (2) |
| 79135 | 409 (129..542) | 322 | 61 | 24 (160), 3 (62), 15 (33), 38 (33), 22 (22), 7 (7), 35 (5) |
| 79139 | 406 (132..537) | 323 | 62 | 22 (159), 3 (70), 15 (53), 7 (29), 38 (12) |
| 79136 | 393 (136..538) | 302 | 64 | 7 (193), 38 (45), 15 (43), 22 (16), 3 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 112/381/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 799 | 799 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..460 | 383 | 317 | 317 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 2 | 84..450 | 367 | 294 | 294 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 3 | 87..542 | 456 | 365 | 365 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 4 | 87..467 | 381 | 299 | 299 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79098, 79102 |
| 7 | 93..533 | 441 | 353 | 353 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 94..434 | 341 | 282 | 282 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 9 | 96..439 | 344 | 283 | 283 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 14 | 103..484 | 382 | 322 | 322 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 15 | 103..536 | 434 | 358 | 358 | 0 | 0 | 0 | 0 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 103..443 | 341 | 287 | 287 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 18 | 108..495 | 388 | 326 | 326 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 108..500 | 393 | 329 | 329 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 108..429 | 322 | 275 | 275 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 108..531 | 424 | 357 | 357 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 117..532 | 416 | 339 | 339 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 122..445 | 324 | 260 | 260 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 24 | 126..530 | 405 | 334 | 334 | 0 | 0 | 0 | 0 | 79116, 79128, 79132, 79134, 79135 |
| 26 | 126..481 | 356 | 290 | 290 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 27 | 126..527 | 402 | 332 | 332 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 28 | 136..491 | 356 | 309 | 309 | 0 | 0 | 0 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 138..477 | 340 | 275 | 275 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79132 |
| 33 | 158..455 | 298 | 249 | 249 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 35 | 158..515 | 358 | 284 | 284 | 0 | 0 | 0 | 0 | 78899, 79097, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 38 | 427..538 | 112 | 90 | 90 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9322; unmatched reference entries: 820; unmatched candidate entries: 1145
- identity switches: 580; fragmentation (coverage interruptions): 587; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 3 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 2 -> 3 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 2 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 4 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f96: ref 78896: 4 -> 9 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 79037: 3 -> 1 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 2 -> 3 at (2107, 3033), 1 frames after previous cover
- f97: ref 78971: 8 -> 1 at (2072, 3034.5), 1 frames after previous cover
- f97: ref 79045: 1 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 7 -> 2 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 1 -> 8 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 8 -> 1 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 7 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 3 -> 2 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 1 -> 3 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 2 -> 3 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 3 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 3 -> 15 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 7 -> 14 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 7 -> 16 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 3 -> 15 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 15 -> 1 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 7 -> 16 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 16 -> 14 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 1 -> 20 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79103: 16 -> 21 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 16 -> 18 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 7 -> 16 at (2131, 3027), 3 frames after previous cover
- f108: ref 79110: 7 -> 19 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79097: 2 -> 3 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 14 -> 2 at (2077.5, 3029.5), 3 frames after previous cover
- f110: ref 79097: 3 -> 2 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 2 -> 14 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 18 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 18 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 19 -> 16 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 7 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 2 -> 14 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 21 -> 18 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 18 -> 16 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 14 -> 21 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 16 -> 19 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 21 -> 16 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 3 -> 20 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79045: 20 -> 8 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 2 -> 15 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 21 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 18 -> 3 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 16 -> 18 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 19 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 15 -> 20 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 20 -> 14 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 1 -> 20 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 8 -> 1 at (1956.5, 3034.5), 2 frames after previous cover
- f118: ref 79037: 20 -> 1 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 14 -> 15 at (2010.5, 3030), 2 frames after previous cover
- ... 520 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 994 | 12 | 0 (994) |
| 78896 | 350 (76..429) | 322 | 16 | 20 (264), 9 (46), 1 (6), 4 (6) |
| 78969 | 352 (80..434) | 320 | 20 | 9 (222), 8 (45), 4 (42), 20 (7), 1 (4) |
| 78971 | 352 (84..439) | 313 | 24 | 8 (139), 2 (105), 9 (54), 1 (5), 4 (5), 20 (4), 3 (1) |
| 79045 | 355 (84..443) | 319 | 25 | 8 (132), 23 (91), 16 (36), 1 (26), 2 (21), 20 (8), 3 (3), 9 (2) |
| 79037 | 355 (86..445) | 310 | 32 | 23 (132), 2 (114), 1 (21), 4 (19), 20 (9), 8 (7), 3 (6), 15 (1), 16 (1) |
| 78897 | 345 (89..450) | 316 | 23 | 4 (190), 2 (48), 23 (34), 20 (16), 15 (11), 3 (5), 33 (3), 16 (3), 14 (2), 8 (2), 1 (2) |
| 78899 | 365 (91..455) | 322 | 29 | 16 (114), 35 (88), 33 (51), 14 (21), 4 (13), 23 (12), 3 (11), 1 (6), 2 (3), 7 (1), 20 (1), 26 (1) |
| 79097 | 366 (94..461) | 335 | 23 | 33 (179), 1 (51), 14 (48), 35 (20), 23 (13), 2 (9), 26 (7), 15 (4), 7 (3), 3 (1) |
| 79098 | 360 (97..467) | 335 | 18 | 1 (189), 4 (78), 14 (26), 15 (11), 2 (9), 23 (9), 26 (8), 7 (3), 33 (2) |
| 79102 | 371 (98..477) | 338 | 25 | 26 (93), 14 (65), 29 (64), 1 (38), 15 (31), 33 (24), 23 (8), 2 (4), 7 (3), 21 (2), 18 (2), 4 (2), +2 more |
| 79103 | 380 (99..481) | 332 | 30 | 29 (93), 26 (79), 14 (37), 16 (31), 19 (25), 33 (24), 1 (11), 2 (10), 15 (9), 3 (6), 18 (4), 21 (3) |
| 79105 | 379 (101..484) | 342 | 30 | 14 (140), 26 (90), 19 (25), 16 (24), 29 (18), 2 (14), 15 (11), 3 (10), 18 (6), 21 (2), 7 (1), 28 (1) |
| 79108 | 385 (104..492) | 360 | 21 | 28 (134), 19 (99), 15 (45), 14 (36), 16 (20), 26 (17), 7 (2), 3 (2), 35 (2), 29 (2), 18 (1) |
| 79110 | 388 (106..497) | 359 | 20 | 18 (108), 28 (96), 19 (66), 16 (36), 26 (36), 15 (9), 21 (5), 3 (2), 7 (1) |
| 79111 | 386 (109..500) | 346 | 29 | 19 (114), 3 (47), 16 (44), 18 (38), 15 (36), 27 (36), 28 (28), 7 (2), 21 (1) |
| 79115 | 421 (111..531) | 368 | 37 | 21 (157), 3 (63), 19 (47), 18 (33), 27 (20), 15 (19), 28 (13), 29 (8), 7 (3), 16 (2), 35 (2), 22 (1) |
| 79116 | 411 (114..530) | 385 | 21 | 24 (148), 18 (80), 28 (72), 15 (22), 3 (17), 27 (15), 16 (10), 21 (8), 7 (4), 35 (4), 22 (3), 29 (2) |
| 79122 | 404 (118..532) | 374 | 25 | 22 (120), 18 (67), 21 (67), 29 (52), 27 (41), 35 (14), 16 (5), 7 (3), 3 (3), 28 (1), 15 (1) |
| 79132 | 391 (120..515) | 355 | 27 | 35 (169), 29 (77), 3 (37), 18 (34), 27 (20), 15 (7), 21 (4), 7 (3), 24 (3), 22 (1) |
| 79128 | 402 (124..527) | 377 | 20 | 27 (255), 3 (40), 15 (34), 24 (18), 35 (13), 21 (11), 7 (4), 22 (2) |
| 79134 | 407 (127..533) | 383 | 18 | 21 (151), 7 (111), 22 (42), 24 (35), 35 (19), 3 (14), 15 (8), 27 (3) |
| 79135 | 409 (129..542) | 376 | 20 | 24 (187), 3 (72), 15 (39), 38 (39), 22 (26), 7 (7), 35 (6) |
| 79139 | 406 (132..537) | 382 | 19 | 22 (189), 3 (92), 15 (54), 7 (34), 38 (13) |
| 79136 | 393 (136..538) | 359 | 23 | 7 (228), 15 (57), 38 (55), 22 (19) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 141/410/1007; tracks with internal gaps: 25; total internal gaps: 366; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 685)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 994 | 13 | 12 | 2 | 0 | 78911 |
| 1 | 78..489 | 412 | 412 | 359 | 53 | 19 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 2 | 84..479 | 396 | 396 | 337 | 59 | 24 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 3 | 87..571 | 485 | 485 | 432 | 53 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 4 | 87..496 | 410 | 410 | 355 | 55 | 22 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79098, 79102 |
| 7 | 93..562 | 470 | 470 | 413 | 57 | 20 | 3 | 29 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 94..463 | 370 | 370 | 325 | 45 | 15 | 2 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 9 | 96..468 | 373 | 373 | 324 | 49 | 16 | 2 | 29 | 78896, 78969, 78971, 79045 |
| 14 | 103..513 | 411 | 411 | 375 | 36 | 10 | 5 | 21 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 15 | 103..565 | 463 | 463 | 409 | 54 | 20 | 3 | 28 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 103..472 | 370 | 370 | 327 | 43 | 14 | 1 | 29 | 78897, 78899, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 18 | 108..524 | 417 | 417 | 373 | 44 | 12 | 3 | 27 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 108..529 | 422 | 422 | 376 | 46 | 13 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 108..458 | 351 | 351 | 309 | 42 | 10 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 108..560 | 453 | 453 | 411 | 42 | 12 | 2 | 29 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 117..561 | 445 | 445 | 403 | 42 | 12 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 122..474 | 353 | 353 | 299 | 54 | 18 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 24 | 126..559 | 434 | 434 | 391 | 43 | 13 | 2 | 29 | 79116, 79128, 79132, 79134, 79135 |
| 26 | 126..510 | 385 | 385 | 331 | 54 | 17 | 3 | 32 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 27 | 126..556 | 431 | 431 | 390 | 41 | 10 | 2 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 28 | 136..520 | 385 | 385 | 346 | 39 | 7 | 2 | 31 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 138..506 | 369 | 369 | 316 | 53 | 18 | 4 | 25 | 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79132 |
| 33 | 158..484 | 327 | 327 | 283 | 44 | 11 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 35 | 158..544 | 387 | 387 | 337 | 50 | 18 | 2 | 29 | 78899, 79097, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 38 | 427..567 | 141 | 141 | 107 | 34 | 5 | 1 | 29 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9322; unmatched reference entries: 820; unmatched candidate entries: 1145
- identity switches: 580; fragmentation (coverage interruptions): 587; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 3 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 2 -> 3 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 2 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 4 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f96: ref 78896: 4 -> 9 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 79037: 3 -> 1 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 2 -> 3 at (2107, 3033), 1 frames after previous cover
- f97: ref 78971: 8 -> 1 at (2072, 3034.5), 1 frames after previous cover
- f97: ref 79045: 1 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 7 -> 2 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 1 -> 8 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 8 -> 1 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 7 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 3 -> 2 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 1 -> 3 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 2 -> 3 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 3 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 3 -> 15 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 7 -> 14 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 7 -> 16 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 3 -> 15 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 15 -> 1 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 7 -> 16 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 16 -> 14 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 1 -> 20 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79103: 16 -> 21 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 16 -> 18 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 7 -> 16 at (2131, 3027), 3 frames after previous cover
- f108: ref 79110: 7 -> 19 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79097: 2 -> 3 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 14 -> 2 at (2077.5, 3029.5), 3 frames after previous cover
- f110: ref 79097: 3 -> 2 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 2 -> 14 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 18 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 18 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 19 -> 16 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 7 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 2 -> 14 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 21 -> 18 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 18 -> 16 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 14 -> 21 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 16 -> 19 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 21 -> 16 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 3 -> 20 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79045: 20 -> 8 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 2 -> 15 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 21 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 18 -> 3 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 16 -> 18 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 19 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 15 -> 20 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 20 -> 14 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 1 -> 20 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 8 -> 1 at (1956.5, 3034.5), 2 frames after previous cover
- f118: ref 79037: 20 -> 1 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 14 -> 15 at (2010.5, 3030), 2 frames after previous cover
- ... 520 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 994 | 12 | 0 (994) |
| 78896 | 350 (76..429) | 322 | 16 | 20 (264), 9 (46), 1 (6), 4 (6) |
| 78969 | 352 (80..434) | 320 | 20 | 9 (222), 8 (45), 4 (42), 20 (7), 1 (4) |
| 78971 | 352 (84..439) | 313 | 24 | 8 (139), 2 (105), 9 (54), 1 (5), 4 (5), 20 (4), 3 (1) |
| 79045 | 355 (84..443) | 319 | 25 | 8 (132), 23 (91), 16 (36), 1 (26), 2 (21), 20 (8), 3 (3), 9 (2) |
| 79037 | 355 (86..445) | 310 | 32 | 23 (132), 2 (114), 1 (21), 4 (19), 20 (9), 8 (7), 3 (6), 15 (1), 16 (1) |
| 78897 | 345 (89..450) | 316 | 23 | 4 (190), 2 (48), 23 (34), 20 (16), 15 (11), 3 (5), 33 (3), 16 (3), 14 (2), 8 (2), 1 (2) |
| 78899 | 365 (91..455) | 322 | 29 | 16 (114), 35 (88), 33 (51), 14 (21), 4 (13), 23 (12), 3 (11), 1 (6), 2 (3), 7 (1), 20 (1), 26 (1) |
| 79097 | 366 (94..461) | 335 | 23 | 33 (179), 1 (51), 14 (48), 35 (20), 23 (13), 2 (9), 26 (7), 15 (4), 7 (3), 3 (1) |
| 79098 | 360 (97..467) | 335 | 18 | 1 (189), 4 (78), 14 (26), 15 (11), 2 (9), 23 (9), 26 (8), 7 (3), 33 (2) |
| 79102 | 371 (98..477) | 338 | 25 | 26 (93), 14 (65), 29 (64), 1 (38), 15 (31), 33 (24), 23 (8), 2 (4), 7 (3), 21 (2), 18 (2), 4 (2), +2 more |
| 79103 | 380 (99..481) | 332 | 30 | 29 (93), 26 (79), 14 (37), 16 (31), 19 (25), 33 (24), 1 (11), 2 (10), 15 (9), 3 (6), 18 (4), 21 (3) |
| 79105 | 379 (101..484) | 342 | 30 | 14 (140), 26 (90), 19 (25), 16 (24), 29 (18), 2 (14), 15 (11), 3 (10), 18 (6), 21 (2), 7 (1), 28 (1) |
| 79108 | 385 (104..492) | 360 | 21 | 28 (134), 19 (99), 15 (45), 14 (36), 16 (20), 26 (17), 7 (2), 3 (2), 35 (2), 29 (2), 18 (1) |
| 79110 | 388 (106..497) | 359 | 20 | 18 (108), 28 (96), 19 (66), 16 (36), 26 (36), 15 (9), 21 (5), 3 (2), 7 (1) |
| 79111 | 386 (109..500) | 346 | 29 | 19 (114), 3 (47), 16 (44), 18 (38), 15 (36), 27 (36), 28 (28), 7 (2), 21 (1) |
| 79115 | 421 (111..531) | 368 | 37 | 21 (157), 3 (63), 19 (47), 18 (33), 27 (20), 15 (19), 28 (13), 29 (8), 7 (3), 16 (2), 35 (2), 22 (1) |
| 79116 | 411 (114..530) | 385 | 21 | 24 (148), 18 (80), 28 (72), 15 (22), 3 (17), 27 (15), 16 (10), 21 (8), 7 (4), 35 (4), 22 (3), 29 (2) |
| 79122 | 404 (118..532) | 374 | 25 | 22 (120), 18 (67), 21 (67), 29 (52), 27 (41), 35 (14), 16 (5), 7 (3), 3 (3), 28 (1), 15 (1) |
| 79132 | 391 (120..515) | 355 | 27 | 35 (169), 29 (77), 3 (37), 18 (34), 27 (20), 15 (7), 21 (4), 7 (3), 24 (3), 22 (1) |
| 79128 | 402 (124..527) | 377 | 20 | 27 (255), 3 (40), 15 (34), 24 (18), 35 (13), 21 (11), 7 (4), 22 (2) |
| 79134 | 407 (127..533) | 383 | 18 | 21 (151), 7 (111), 22 (42), 24 (35), 35 (19), 3 (14), 15 (8), 27 (3) |
| 79135 | 409 (129..542) | 376 | 20 | 24 (187), 3 (72), 15 (39), 38 (39), 22 (26), 7 (7), 35 (6) |
| 79139 | 406 (132..537) | 382 | 19 | 22 (189), 3 (92), 15 (54), 7 (34), 38 (13) |
| 79136 | 393 (136..538) | 359 | 23 | 7 (228), 15 (57), 38 (55), 22 (19) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 141/410/1007; tracks with internal gaps: 25; total internal gaps: 366; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 685)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 994 | 13 | 12 | 2 | 0 | 78911 |
| 1 | 78..489 | 412 | 412 | 359 | 53 | 19 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 2 | 84..479 | 396 | 396 | 337 | 59 | 24 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 3 | 87..571 | 485 | 485 | 432 | 53 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 4 | 87..496 | 410 | 410 | 355 | 55 | 22 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79098, 79102 |
| 7 | 93..562 | 470 | 470 | 413 | 57 | 20 | 3 | 29 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 94..463 | 370 | 370 | 325 | 45 | 15 | 2 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 9 | 96..468 | 373 | 373 | 324 | 49 | 16 | 2 | 29 | 78896, 78969, 78971, 79045 |
| 14 | 103..513 | 411 | 411 | 375 | 36 | 10 | 5 | 21 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 15 | 103..565 | 463 | 463 | 409 | 54 | 20 | 3 | 28 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 103..472 | 370 | 370 | 327 | 43 | 14 | 1 | 29 | 78897, 78899, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 18 | 108..524 | 417 | 417 | 373 | 44 | 12 | 3 | 27 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 108..529 | 422 | 422 | 376 | 46 | 13 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 108..458 | 351 | 351 | 309 | 42 | 10 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 108..560 | 453 | 453 | 411 | 42 | 12 | 2 | 29 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 117..561 | 445 | 445 | 403 | 42 | 12 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 122..474 | 353 | 353 | 299 | 54 | 18 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 24 | 126..559 | 434 | 434 | 391 | 43 | 13 | 2 | 29 | 79116, 79128, 79132, 79134, 79135 |
| 26 | 126..510 | 385 | 385 | 331 | 54 | 17 | 3 | 32 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 27 | 126..556 | 431 | 431 | 390 | 41 | 10 | 2 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 28 | 136..520 | 385 | 385 | 346 | 39 | 7 | 2 | 31 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 138..506 | 369 | 369 | 316 | 53 | 18 | 4 | 25 | 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79132 |
| 33 | 158..484 | 327 | 327 | 283 | 44 | 11 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 35 | 158..544 | 387 | 387 | 337 | 50 | 18 | 2 | 29 | 78899, 79097, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 38 | 427..567 | 141 | 141 | 107 | 34 | 5 | 1 | 29 | 79135, 79136, 79139 |
