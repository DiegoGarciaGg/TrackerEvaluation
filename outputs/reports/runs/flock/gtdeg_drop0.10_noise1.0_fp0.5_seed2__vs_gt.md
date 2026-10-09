# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=82b5e52d7240
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise1.0_fp0.5_seed2/tracks.csv sha256=4f03686b36faecf6
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise1.0_fp0.5_seed2.csv sha256=82b5e52d72405db4
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise1.0_fp0.5_seed2
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
| observations | none | 4 | 0.449 | 0.276 | 0.842 | 1.28 | 0.548 | 420 | 981.0 |
| observations | none | 6 | 0.483 | 0.301 | 0.843 | 1.29 | 0.549 | 416 | 980.0 |
| observations | none | 8 | 0.501 | 0.319 | 0.844 | 1.30 | 0.551 | 404 | 977.0 |
| observations | none | 12 | 0.525 | 0.342 | 0.845 | 1.45 | 0.567 | 368 | 986.0 |
| observations | ignore | 4 | 0.449 | 0.276 | 0.842 | 1.28 | 0.548 | 420 | 981.0 |
| observations | ignore | 6 | 0.483 | 0.301 | 0.843 | 1.29 | 0.549 | 416 | 980.0 |
| observations | ignore | 8 | 0.501 | 0.319 | 0.844 | 1.30 | 0.551 | 404 | 977.0 |
| observations | ignore | 12 | 0.525 | 0.342 | 0.845 | 1.45 | 0.567 | 368 | 986.0 |
| updates | none | 4 | 0.416 | 0.266 | 0.683 | 1.30 | 0.510 | 435 | 896.0 |
| updates | none | 6 | 0.462 | 0.297 | 0.741 | 1.42 | 0.527 | 423 | 644.0 |
| updates | none | 8 | 0.489 | 0.321 | 0.804 | 1.61 | 0.546 | 397 | 377.0 |
| updates | none | 12 | 0.521 | 0.349 | 0.824 | 1.86 | 0.568 | 368 | 301.0 |
| updates | ignore | 4 | 0.416 | 0.266 | 0.683 | 1.30 | 0.510 | 435 | 896.0 |
| updates | ignore | 6 | 0.462 | 0.297 | 0.741 | 1.42 | 0.527 | 423 | 644.0 |
| updates | ignore | 8 | 0.489 | 0.321 | 0.804 | 1.61 | 0.546 | 397 | 377.0 |
| updates | ignore | 12 | 0.521 | 0.349 | 0.824 | 1.86 | 0.568 | 368 | 301.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9009; unmatched reference entries: 1133; unmatched candidate entries: 42
- identity switches: 404; fragmentation (coverage interruptions): 934; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 36 -> 50 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 43 -> 35 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78971: 35 -> 31 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 42 -> 54 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 36 -> 42 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 55 -> 36 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 56 -> 55 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 56 -> 60 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 35 -> 51 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 31 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 47 -> 35 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 36 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 36 -> 55 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 55 -> 56 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 52 -> 36 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 55 -> 52 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 56 -> 55 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 60 -> 56 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 56 -> 60 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 42 -> 36 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79115: 61 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 36 -> 64 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79105: 52 -> 42 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 55 -> 52 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 56 -> 55 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 60 -> 56 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 43 -> 35 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 35 -> 50 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 50 -> 47 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 64 -> 43 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 36 -> 64 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 50 -> 51 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 47 -> 50 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 51 -> 35 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 35 -> 54 at (1988.5, 3032), 2 frames after previous cover
- f120: ref 79098: 43 -> 35 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 64 -> 43 at (2025.5, 3030.5), 2 frames after previous cover
- f120: ref 79105: 42 -> 64 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 52 -> 42 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 55 -> 52 at (2077, 3028), 3 frames after previous cover
- f120: ref 79111: 56 -> 55 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 60 -> 56 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 61 -> 60 at (2120, 3023.5), 3 frames after previous cover
- f121: ref 78897: 35 -> 43 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 54 -> 36 at (1992.5, 3031), 1 frames after previous cover
- f121: ref 79102: 43 -> 64 at (2019.5, 3029), 1 frames after previous cover
- f121: ref 79105: 64 -> 42 at (2040, 3025), 1 frames after previous cover
- ... 344 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 910 | 85 | 3 (910) |
| 78896 | 350 (76..429) | 312 | 30 | 71 (263), 31 (43), 73 (6) |
| 78969 | 352 (80..434) | 295 | 42 | 77 (141), 73 (109), 40 (33), 31 (9), 47 (1), 80 (1), 51 (1) |
| 78971 | 352 (84..439) | 315 | 27 | 80 (151), 51 (42), 73 (40), 50 (30), 47 (25), 35 (24), 77 (2), 31 (1) |
| 79045 | 355 (84..443) | 304 | 35 | 80 (121), 47 (79), 31 (58), 50 (36), 73 (8), 36 (1), 40 (1) |
| 79037 | 355 (86..445) | 312 | 36 | 47 (170), 73 (89), 51 (28), 31 (7), 35 (4), 50 (4), 80 (4), 43 (3), 36 (2), 42 (1) |
| 78897 | 345 (89..450) | 314 | 27 | 40 (132), 50 (58), 31 (45), 47 (32), 43 (19), 73 (13), 51 (8), 42 (3), 36 (2), 35 (2) |
| 78899 | 365 (91..455) | 330 | 32 | 31 (181), 51 (118), 43 (9), 40 (7), 36 (3), 42 (3), 54 (3), 73 (3), 35 (2), 50 (1) |
| 79097 | 366 (94..461) | 325 | 34 | 40 (149), 156 (130), 54 (19), 36 (7), 47 (7), 43 (6), 51 (3), 42 (2), 31 (2) |
| 79098 | 360 (97..467) | 316 | 38 | 82 (149), 51 (104), 123 (28), 42 (11), 36 (6), 43 (6), 54 (4), 40 (3), 64 (2), 35 (2), 31 (1) |
| 79102 | 371 (98..477) | 333 | 30 | 123 (161), 43 (83), 36 (44), 156 (26), 64 (6), 51 (6), 42 (3), 35 (2), 54 (1), 40 (1) |
| 79103 | 380 (99..481) | 343 | 33 | 36 (230), 43 (58), 123 (34), 52 (12), 64 (6), 42 (1), 35 (1), 54 (1) |
| 79105 | 379 (101..484) | 335 | 33 | 43 (171), 64 (79), 36 (33), 82 (30), 42 (7), 55 (6), 52 (6), 54 (2), 35 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 64 (169), 82 (100), 36 (43), 52 (18), 55 (7), 56 (3), 42 (3), 67 (1) |
| 79110 | 388 (106..497) | 340 | 40 | 61 (183), 52 (64), 55 (47), 64 (35), 56 (5), 60 (2), 67 (2), 42 (1), 43 (1) |
| 79111 | 386 (109..500) | 333 | 43 | 55 (235), 64 (53), 61 (14), 67 (9), 35 (9), 56 (6), 52 (4), 60 (2), 54 (1) |
| 79115 | 421 (111..531) | 366 | 45 | 52 (158), 67 (98), 42 (83), 60 (6), 35 (6), 54 (5), 56 (4), 61 (3), 55 (2), 140 (1) |
| 79116 | 411 (114..530) | 377 | 31 | 140 (149), 54 (68), 52 (68), 35 (52), 61 (14), 42 (14), 67 (6), 60 (3), 56 (2), 55 (1) |
| 79122 | 404 (118..532) | 347 | 46 | 35 (258), 42 (28), 52 (26), 54 (12), 61 (9), 140 (7), 60 (3), 56 (3), 67 (1) |
| 79132 | 391 (120..515) | 349 | 36 | 42 (241), 55 (63), 52 (26), 56 (7), 61 (4), 35 (4), 60 (3), 67 (1) |
| 79128 | 402 (124..527) | 358 | 39 | 69 (227), 61 (49), 56 (28), 54 (28), 67 (15), 60 (6), 42 (2), 35 (2), 52 (1) |
| 79134 | 407 (127..533) | 362 | 35 | 54 (167), 140 (46), 61 (35), 67 (35), 56 (31), 60 (28), 35 (18), 69 (2) |
| 79135 | 409 (129..542) | 363 | 41 | 67 (164), 69 (98), 54 (60), 61 (33), 60 (8) |
| 79139 | 406 (132..537) | 379 | 23 | 60 (278), 140 (42), 69 (36), 67 (22), 76 (1) |
| 79136 | 393 (136..538) | 347 | 38 | 76 (156), 160 (100), 60 (53), 54 (32), 67 (5), 140 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 116/367/1003; tracks with internal gaps: 18; total internal gaps: 31; longest internal gap: 2; tracks ending in coasting: 5 (trailing rows total 10)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 914 | 910 | 4 | 4 | 1 | 0 | 78911 |
| 31 | 78..455 | 378 | 349 | 347 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 35 | 86..532 | 447 | 389 | 387 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 36 | 86..492 | 407 | 371 | 371 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 40 | 88..449 | 362 | 327 | 326 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 79045, 79097, 79098, 79102 |
| 42 | 90..531 | 442 | 404 | 403 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 43 | 91..484 | 394 | 356 | 356 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110 |
| 47 | 95..461 | 367 | 315 | 314 | 1 | 1 | 1 | 0 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 50 | 98..252 | 155 | 132 | 129 | 3 | 1 | 1 | 2 | 78897, 78899, 78971, 79037, 79045 |
| 51 | 100..439 | 340 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102 |
| 52 | 100..530 | 431 | 384 | 383 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 54 | 101..542 | 442 | 405 | 403 | 2 | 2 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 55 | 105..515 | 411 | 361 | 361 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 56 | 106..221 | 116 | 92 | 89 | 3 | 0 | 0 | 3 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 60 | 111..537 | 427 | 393 | 392 | 1 | 1 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 111..497 | 387 | 346 | 344 | 2 | 2 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 115..500 | 386 | 351 | 350 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 67 | 122..533 | 412 | 362 | 359 | 3 | 3 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 126..527 | 402 | 365 | 363 | 2 | 2 | 1 | 0 | 79128, 79134, 79135, 79139 |
| 71 | 127..429 | 303 | 266 | 263 | 3 | 2 | 2 | 0 | 78896 |
| 73 | 132..434 | 303 | 268 | 268 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 76 | 135..320 | 186 | 159 | 157 | 2 | 0 | 0 | 2 | 79136, 79139 |
| 77 | 136..299 | 164 | 144 | 143 | 1 | 0 | 0 | 1 | 78969, 78971 |
| 80 | 142..443 | 302 | 277 | 277 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 82 | 144..467 | 324 | 281 | 279 | 2 | 2 | 1 | 0 | 79098, 79105, 79108 |
| 123 | 235..481 | 247 | 223 | 223 | 0 | 0 | 0 | 0 | 79098, 79102, 79103 |
| 140 | 267..538 | 272 | 246 | 246 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79134, 79136, 79139 |
| 156 | 306..477 | 172 | 158 | 156 | 2 | 2 | 1 | 0 | 79097, 79102 |
| 160 | 322..452 | 131 | 103 | 100 | 3 | 1 | 1 | 2 | 79136 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9009; unmatched reference entries: 1133; unmatched candidate entries: 42
- identity switches: 404; fragmentation (coverage interruptions): 934; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 36 -> 50 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 43 -> 35 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78971: 35 -> 31 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 42 -> 54 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 36 -> 42 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 55 -> 36 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 56 -> 55 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 56 -> 60 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 35 -> 51 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 31 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 47 -> 35 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 36 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 36 -> 55 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 55 -> 56 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 52 -> 36 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 55 -> 52 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 56 -> 55 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 60 -> 56 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 56 -> 60 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 42 -> 36 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79115: 61 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 36 -> 64 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79105: 52 -> 42 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 55 -> 52 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 56 -> 55 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 60 -> 56 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 43 -> 35 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 35 -> 50 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 50 -> 47 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 64 -> 43 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 36 -> 64 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 50 -> 51 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 47 -> 50 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 51 -> 35 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 35 -> 54 at (1988.5, 3032), 2 frames after previous cover
- f120: ref 79098: 43 -> 35 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 64 -> 43 at (2025.5, 3030.5), 2 frames after previous cover
- f120: ref 79105: 42 -> 64 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 52 -> 42 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 55 -> 52 at (2077, 3028), 3 frames after previous cover
- f120: ref 79111: 56 -> 55 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 60 -> 56 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 61 -> 60 at (2120, 3023.5), 3 frames after previous cover
- f121: ref 78897: 35 -> 43 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 54 -> 36 at (1992.5, 3031), 1 frames after previous cover
- f121: ref 79102: 43 -> 64 at (2019.5, 3029), 1 frames after previous cover
- f121: ref 79105: 64 -> 42 at (2040, 3025), 1 frames after previous cover
- ... 344 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 910 | 85 | 3 (910) |
| 78896 | 350 (76..429) | 312 | 30 | 71 (263), 31 (43), 73 (6) |
| 78969 | 352 (80..434) | 295 | 42 | 77 (141), 73 (109), 40 (33), 31 (9), 47 (1), 80 (1), 51 (1) |
| 78971 | 352 (84..439) | 315 | 27 | 80 (151), 51 (42), 73 (40), 50 (30), 47 (25), 35 (24), 77 (2), 31 (1) |
| 79045 | 355 (84..443) | 304 | 35 | 80 (121), 47 (79), 31 (58), 50 (36), 73 (8), 36 (1), 40 (1) |
| 79037 | 355 (86..445) | 312 | 36 | 47 (170), 73 (89), 51 (28), 31 (7), 35 (4), 50 (4), 80 (4), 43 (3), 36 (2), 42 (1) |
| 78897 | 345 (89..450) | 314 | 27 | 40 (132), 50 (58), 31 (45), 47 (32), 43 (19), 73 (13), 51 (8), 42 (3), 36 (2), 35 (2) |
| 78899 | 365 (91..455) | 330 | 32 | 31 (181), 51 (118), 43 (9), 40 (7), 36 (3), 42 (3), 54 (3), 73 (3), 35 (2), 50 (1) |
| 79097 | 366 (94..461) | 325 | 34 | 40 (149), 156 (130), 54 (19), 36 (7), 47 (7), 43 (6), 51 (3), 42 (2), 31 (2) |
| 79098 | 360 (97..467) | 316 | 38 | 82 (149), 51 (104), 123 (28), 42 (11), 36 (6), 43 (6), 54 (4), 40 (3), 64 (2), 35 (2), 31 (1) |
| 79102 | 371 (98..477) | 333 | 30 | 123 (161), 43 (83), 36 (44), 156 (26), 64 (6), 51 (6), 42 (3), 35 (2), 54 (1), 40 (1) |
| 79103 | 380 (99..481) | 343 | 33 | 36 (230), 43 (58), 123 (34), 52 (12), 64 (6), 42 (1), 35 (1), 54 (1) |
| 79105 | 379 (101..484) | 335 | 33 | 43 (171), 64 (79), 36 (33), 82 (30), 42 (7), 55 (6), 52 (6), 54 (2), 35 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 64 (169), 82 (100), 36 (43), 52 (18), 55 (7), 56 (3), 42 (3), 67 (1) |
| 79110 | 388 (106..497) | 340 | 40 | 61 (183), 52 (64), 55 (47), 64 (35), 56 (5), 60 (2), 67 (2), 42 (1), 43 (1) |
| 79111 | 386 (109..500) | 333 | 43 | 55 (235), 64 (53), 61 (14), 67 (9), 35 (9), 56 (6), 52 (4), 60 (2), 54 (1) |
| 79115 | 421 (111..531) | 366 | 45 | 52 (158), 67 (98), 42 (83), 60 (6), 35 (6), 54 (5), 56 (4), 61 (3), 55 (2), 140 (1) |
| 79116 | 411 (114..530) | 377 | 31 | 140 (149), 54 (68), 52 (68), 35 (52), 61 (14), 42 (14), 67 (6), 60 (3), 56 (2), 55 (1) |
| 79122 | 404 (118..532) | 347 | 46 | 35 (258), 42 (28), 52 (26), 54 (12), 61 (9), 140 (7), 60 (3), 56 (3), 67 (1) |
| 79132 | 391 (120..515) | 349 | 36 | 42 (241), 55 (63), 52 (26), 56 (7), 61 (4), 35 (4), 60 (3), 67 (1) |
| 79128 | 402 (124..527) | 358 | 39 | 69 (227), 61 (49), 56 (28), 54 (28), 67 (15), 60 (6), 42 (2), 35 (2), 52 (1) |
| 79134 | 407 (127..533) | 362 | 35 | 54 (167), 140 (46), 61 (35), 67 (35), 56 (31), 60 (28), 35 (18), 69 (2) |
| 79135 | 409 (129..542) | 363 | 41 | 67 (164), 69 (98), 54 (60), 61 (33), 60 (8) |
| 79139 | 406 (132..537) | 379 | 23 | 60 (278), 140 (42), 69 (36), 67 (22), 76 (1) |
| 79136 | 393 (136..538) | 347 | 38 | 76 (156), 160 (100), 60 (53), 54 (32), 67 (5), 140 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 116/367/1003; tracks with internal gaps: 18; total internal gaps: 31; longest internal gap: 2; tracks ending in coasting: 5 (trailing rows total 10)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 914 | 910 | 4 | 4 | 1 | 0 | 78911 |
| 31 | 78..455 | 378 | 349 | 347 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 35 | 86..532 | 447 | 389 | 387 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 36 | 86..492 | 407 | 371 | 371 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 40 | 88..449 | 362 | 327 | 326 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 79045, 79097, 79098, 79102 |
| 42 | 90..531 | 442 | 404 | 403 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 43 | 91..484 | 394 | 356 | 356 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110 |
| 47 | 95..461 | 367 | 315 | 314 | 1 | 1 | 1 | 0 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 50 | 98..252 | 155 | 132 | 129 | 3 | 1 | 1 | 2 | 78897, 78899, 78971, 79037, 79045 |
| 51 | 100..439 | 340 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102 |
| 52 | 100..530 | 431 | 384 | 383 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 54 | 101..542 | 442 | 405 | 403 | 2 | 2 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 55 | 105..515 | 411 | 361 | 361 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 56 | 106..221 | 116 | 92 | 89 | 3 | 0 | 0 | 3 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 60 | 111..537 | 427 | 393 | 392 | 1 | 1 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 111..497 | 387 | 346 | 344 | 2 | 2 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 115..500 | 386 | 351 | 350 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 67 | 122..533 | 412 | 362 | 359 | 3 | 3 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 126..527 | 402 | 365 | 363 | 2 | 2 | 1 | 0 | 79128, 79134, 79135, 79139 |
| 71 | 127..429 | 303 | 266 | 263 | 3 | 2 | 2 | 0 | 78896 |
| 73 | 132..434 | 303 | 268 | 268 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 76 | 135..320 | 186 | 159 | 157 | 2 | 0 | 0 | 2 | 79136, 79139 |
| 77 | 136..299 | 164 | 144 | 143 | 1 | 0 | 0 | 1 | 78969, 78971 |
| 80 | 142..443 | 302 | 277 | 277 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 82 | 144..467 | 324 | 281 | 279 | 2 | 2 | 1 | 0 | 79098, 79105, 79108 |
| 123 | 235..481 | 247 | 223 | 223 | 0 | 0 | 0 | 0 | 79098, 79102, 79103 |
| 140 | 267..538 | 272 | 246 | 246 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79134, 79136, 79139 |
| 156 | 306..477 | 172 | 158 | 156 | 2 | 2 | 1 | 0 | 79097, 79102 |
| 160 | 322..452 | 131 | 103 | 100 | 3 | 1 | 1 | 2 | 79136 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9737; unmatched reference entries: 405; unmatched candidate entries: 1188
- identity switches: 397; fragmentation (coverage interruptions): 287; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 36 -> 50 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 43 -> 35 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78971: 35 -> 31 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 42 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 36 -> 42 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 55 -> 36 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 56 -> 55 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 56 -> 60 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 35 -> 51 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 31 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 47 -> 35 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 36 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 36 -> 55 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 55 -> 56 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 52 -> 36 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 55 -> 52 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 56 -> 55 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 60 -> 56 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 56 -> 60 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 42 -> 36 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79103: 36 -> 42 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79115: 61 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 36 -> 64 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79103: 42 -> 36 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 52 -> 42 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 55 -> 52 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 56 -> 55 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 60 -> 56 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 43 -> 35 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 35 -> 50 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 50 -> 47 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 64 -> 43 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 36 -> 64 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 50 -> 51 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 47 -> 50 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 51 -> 35 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 35 -> 54 at (1988.5, 3032), 1 frames after previous cover
- f120: ref 79098: 43 -> 35 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 64 -> 43 at (2025.5, 3030.5), 1 frames after previous cover
- f120: ref 79105: 42 -> 64 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 52 -> 42 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 55 -> 52 at (2077, 3028), 2 frames after previous cover
- f120: ref 79111: 56 -> 55 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 60 -> 56 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 61 -> 60 at (2120, 3023.5), 2 frames after previous cover
- f121: ref 78897: 35 -> 43 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 54 -> 36 at (1992.5, 3031), 1 frames after previous cover
- ... 337 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 993 | 10 | 3 (993) |
| 78896 | 350 (76..429) | 333 | 13 | 71 (283), 31 (44), 73 (6) |
| 78969 | 352 (80..434) | 323 | 17 | 77 (151), 73 (126), 40 (34), 31 (9), 47 (1), 80 (1), 51 (1) |
| 78971 | 352 (84..439) | 331 | 14 | 80 (157), 51 (46), 73 (42), 50 (33), 35 (25), 47 (25), 77 (2), 31 (1) |
| 79045 | 355 (84..443) | 325 | 15 | 80 (127), 47 (85), 31 (65), 50 (38), 73 (8), 36 (1), 40 (1) |
| 79037 | 355 (86..445) | 339 | 14 | 47 (189), 73 (96), 51 (29), 31 (7), 35 (4), 50 (4), 80 (4), 43 (3), 36 (2), 42 (1) |
| 78897 | 345 (89..450) | 329 | 13 | 40 (140), 50 (61), 31 (46), 47 (33), 43 (19), 73 (14), 51 (9), 42 (3), 36 (2), 35 (2) |
| 78899 | 365 (91..455) | 352 | 11 | 31 (193), 51 (127), 43 (9), 40 (7), 36 (3), 42 (3), 35 (3), 54 (3), 73 (3), 50 (1) |
| 79097 | 366 (94..461) | 348 | 12 | 40 (159), 156 (139), 54 (19), 47 (11), 36 (7), 43 (6), 51 (3), 42 (2), 31 (2) |
| 79098 | 360 (97..467) | 348 | 8 | 82 (167), 51 (114), 123 (31), 42 (12), 36 (6), 43 (6), 54 (4), 40 (3), 64 (2), 35 (2), 31 (1) |
| 79102 | 371 (98..477) | 357 | 9 | 123 (170), 43 (89), 36 (46), 156 (30), 64 (8), 51 (6), 42 (3), 35 (2), 40 (2), 54 (1) |
| 79103 | 380 (99..481) | 369 | 9 | 36 (246), 43 (64), 123 (35), 52 (13), 64 (6), 42 (2), 35 (2), 54 (1) |
| 79105 | 379 (101..484) | 364 | 9 | 43 (185), 64 (87), 36 (35), 82 (32), 55 (7), 52 (7), 42 (7), 54 (3), 35 (1) |
| 79108 | 385 (104..492) | 371 | 8 | 64 (182), 82 (109), 36 (47), 52 (19), 55 (7), 56 (3), 42 (3), 67 (1) |
| 79110 | 388 (106..497) | 376 | 10 | 61 (202), 52 (72), 55 (48), 64 (39), 56 (5), 36 (3), 60 (2), 67 (2), 42 (1), 43 (1), 82 (1) |
| 79111 | 386 (109..500) | 362 | 17 | 55 (261), 64 (55), 61 (15), 67 (9), 35 (9), 56 (6), 52 (4), 60 (2), 54 (1) |
| 79115 | 421 (111..531) | 405 | 13 | 52 (179), 67 (108), 42 (89), 60 (6), 35 (6), 54 (5), 56 (4), 55 (4), 61 (3), 140 (1) |
| 79116 | 411 (114..530) | 401 | 9 | 140 (159), 54 (73), 52 (72), 35 (56), 61 (15), 42 (14), 67 (6), 60 (3), 56 (2), 55 (1) |
| 79122 | 404 (118..532) | 381 | 17 | 35 (290), 42 (28), 52 (27), 54 (13), 61 (9), 140 (7), 60 (3), 56 (3), 67 (1) |
| 79132 | 391 (120..515) | 374 | 14 | 42 (256), 55 (70), 52 (28), 56 (7), 61 (5), 35 (4), 60 (3), 67 (1) |
| 79128 | 402 (124..527) | 388 | 11 | 69 (248), 61 (52), 56 (31), 54 (30), 67 (15), 60 (7), 42 (2), 35 (2), 52 (1) |
| 79134 | 407 (127..533) | 394 | 10 | 54 (179), 140 (53), 61 (38), 67 (37), 56 (36), 60 (31), 35 (18), 69 (2) |
| 79135 | 409 (129..542) | 400 | 7 | 67 (179), 69 (107), 54 (71), 61 (35), 60 (8) |
| 79139 | 406 (132..537) | 397 | 6 | 60 (351), 69 (37), 67 (8), 76 (1) |
| 79136 | 393 (136..538) | 377 | 11 | 76 (169), 160 (110), 140 (44), 54 (33), 67 (21) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 145/396/1003; tracks with internal gaps: 29; total internal gaps: 253; longest internal gap: 7; tracks ending in coasting: 28 (trailing rows total 857)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 1003 | 993 | 10 | 10 | 1 | 0 | 78911 |
| 31 | 78..484 | 407 | 407 | 368 | 39 | 8 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 35 | 86..561 | 476 | 476 | 426 | 50 | 13 | 6 | 29 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 36 | 86..521 | 436 | 436 | 398 | 38 | 11 | 2 | 24 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 40 | 88..478 | 391 | 391 | 346 | 45 | 13 | 2 | 28 | 78897, 78899, 78969, 79045, 79097, 79098, 79102 |
| 42 | 90..560 | 471 | 471 | 426 | 45 | 14 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 43 | 91..513 | 423 | 423 | 382 | 41 | 9 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110 |
| 47 | 95..490 | 396 | 396 | 344 | 52 | 14 | 5 | 29 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 50 | 98..281 | 184 | 184 | 137 | 47 | 8 | 2 | 38 | 78897, 78899, 78971, 79037, 79045 |
| 51 | 100..468 | 369 | 369 | 335 | 34 | 4 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102 |
| 52 | 100..559 | 460 | 460 | 422 | 38 | 8 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 54 | 101..571 | 471 | 471 | 436 | 35 | 6 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 55 | 105..544 | 440 | 440 | 398 | 42 | 10 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 56 | 106..250 | 145 | 145 | 97 | 48 | 2 | 1 | 46 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 60 | 111..566 | 456 | 456 | 416 | 40 | 7 | 5 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 61 | 111..526 | 416 | 416 | 374 | 42 | 8 | 3 | 32 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 115..529 | 415 | 415 | 379 | 36 | 7 | 1 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 67 | 122..562 | 441 | 441 | 388 | 53 | 16 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 126..556 | 431 | 431 | 394 | 37 | 6 | 2 | 29 | 79128, 79134, 79135, 79139 |
| 71 | 127..458 | 332 | 332 | 283 | 49 | 12 | 7 | 29 | 78896 |
| 73 | 132..463 | 332 | 332 | 295 | 37 | 7 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 76 | 135..349 | 215 | 215 | 170 | 45 | 11 | 4 | 31 | 79136, 79139 |
| 77 | 136..328 | 193 | 193 | 153 | 40 | 8 | 1 | 32 | 78969, 78971 |
| 80 | 142..472 | 331 | 331 | 289 | 42 | 11 | 3 | 29 | 78969, 78971, 79037, 79045 |
| 82 | 144..496 | 353 | 353 | 309 | 44 | 9 | 5 | 29 | 79098, 79105, 79108, 79110 |
| 123 | 235..510 | 276 | 276 | 236 | 40 | 11 | 1 | 29 | 79098, 79102, 79103 |
| 140 | 267..567 | 301 | 301 | 264 | 37 | 5 | 3 | 29 | 79115, 79116, 79122, 79134, 79136 |
| 156 | 306..506 | 201 | 201 | 169 | 32 | 2 | 2 | 29 | 79097, 79102 |
| 160 | 322..481 | 160 | 160 | 110 | 50 | 3 | 2 | 46 | 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 9737; unmatched reference entries: 405; unmatched candidate entries: 1188
- identity switches: 397; fragmentation (coverage interruptions): 287; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 36 -> 50 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 43 -> 35 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78971: 35 -> 31 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 42 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 36 -> 42 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 55 -> 36 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 56 -> 55 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 56 -> 60 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 35 -> 51 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 31 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 47 -> 35 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 36 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 36 -> 55 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 55 -> 56 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 52 -> 36 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 55 -> 52 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 56 -> 55 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 60 -> 56 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 56 -> 60 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 42 -> 36 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79103: 36 -> 42 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79115: 61 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 36 -> 64 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79103: 42 -> 36 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 52 -> 42 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 55 -> 52 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 56 -> 55 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 60 -> 56 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 43 -> 35 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 35 -> 50 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 50 -> 47 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 64 -> 43 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 36 -> 64 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 50 -> 51 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 47 -> 50 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 51 -> 35 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 35 -> 54 at (1988.5, 3032), 1 frames after previous cover
- f120: ref 79098: 43 -> 35 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 64 -> 43 at (2025.5, 3030.5), 1 frames after previous cover
- f120: ref 79105: 42 -> 64 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 52 -> 42 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 55 -> 52 at (2077, 3028), 2 frames after previous cover
- f120: ref 79111: 56 -> 55 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 60 -> 56 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 61 -> 60 at (2120, 3023.5), 2 frames after previous cover
- f121: ref 78897: 35 -> 43 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 54 -> 36 at (1992.5, 3031), 1 frames after previous cover
- ... 337 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 993 | 10 | 3 (993) |
| 78896 | 350 (76..429) | 333 | 13 | 71 (283), 31 (44), 73 (6) |
| 78969 | 352 (80..434) | 323 | 17 | 77 (151), 73 (126), 40 (34), 31 (9), 47 (1), 80 (1), 51 (1) |
| 78971 | 352 (84..439) | 331 | 14 | 80 (157), 51 (46), 73 (42), 50 (33), 35 (25), 47 (25), 77 (2), 31 (1) |
| 79045 | 355 (84..443) | 325 | 15 | 80 (127), 47 (85), 31 (65), 50 (38), 73 (8), 36 (1), 40 (1) |
| 79037 | 355 (86..445) | 339 | 14 | 47 (189), 73 (96), 51 (29), 31 (7), 35 (4), 50 (4), 80 (4), 43 (3), 36 (2), 42 (1) |
| 78897 | 345 (89..450) | 329 | 13 | 40 (140), 50 (61), 31 (46), 47 (33), 43 (19), 73 (14), 51 (9), 42 (3), 36 (2), 35 (2) |
| 78899 | 365 (91..455) | 352 | 11 | 31 (193), 51 (127), 43 (9), 40 (7), 36 (3), 42 (3), 35 (3), 54 (3), 73 (3), 50 (1) |
| 79097 | 366 (94..461) | 348 | 12 | 40 (159), 156 (139), 54 (19), 47 (11), 36 (7), 43 (6), 51 (3), 42 (2), 31 (2) |
| 79098 | 360 (97..467) | 348 | 8 | 82 (167), 51 (114), 123 (31), 42 (12), 36 (6), 43 (6), 54 (4), 40 (3), 64 (2), 35 (2), 31 (1) |
| 79102 | 371 (98..477) | 357 | 9 | 123 (170), 43 (89), 36 (46), 156 (30), 64 (8), 51 (6), 42 (3), 35 (2), 40 (2), 54 (1) |
| 79103 | 380 (99..481) | 369 | 9 | 36 (246), 43 (64), 123 (35), 52 (13), 64 (6), 42 (2), 35 (2), 54 (1) |
| 79105 | 379 (101..484) | 364 | 9 | 43 (185), 64 (87), 36 (35), 82 (32), 55 (7), 52 (7), 42 (7), 54 (3), 35 (1) |
| 79108 | 385 (104..492) | 371 | 8 | 64 (182), 82 (109), 36 (47), 52 (19), 55 (7), 56 (3), 42 (3), 67 (1) |
| 79110 | 388 (106..497) | 376 | 10 | 61 (202), 52 (72), 55 (48), 64 (39), 56 (5), 36 (3), 60 (2), 67 (2), 42 (1), 43 (1), 82 (1) |
| 79111 | 386 (109..500) | 362 | 17 | 55 (261), 64 (55), 61 (15), 67 (9), 35 (9), 56 (6), 52 (4), 60 (2), 54 (1) |
| 79115 | 421 (111..531) | 405 | 13 | 52 (179), 67 (108), 42 (89), 60 (6), 35 (6), 54 (5), 56 (4), 55 (4), 61 (3), 140 (1) |
| 79116 | 411 (114..530) | 401 | 9 | 140 (159), 54 (73), 52 (72), 35 (56), 61 (15), 42 (14), 67 (6), 60 (3), 56 (2), 55 (1) |
| 79122 | 404 (118..532) | 381 | 17 | 35 (290), 42 (28), 52 (27), 54 (13), 61 (9), 140 (7), 60 (3), 56 (3), 67 (1) |
| 79132 | 391 (120..515) | 374 | 14 | 42 (256), 55 (70), 52 (28), 56 (7), 61 (5), 35 (4), 60 (3), 67 (1) |
| 79128 | 402 (124..527) | 388 | 11 | 69 (248), 61 (52), 56 (31), 54 (30), 67 (15), 60 (7), 42 (2), 35 (2), 52 (1) |
| 79134 | 407 (127..533) | 394 | 10 | 54 (179), 140 (53), 61 (38), 67 (37), 56 (36), 60 (31), 35 (18), 69 (2) |
| 79135 | 409 (129..542) | 400 | 7 | 67 (179), 69 (107), 54 (71), 61 (35), 60 (8) |
| 79139 | 406 (132..537) | 397 | 6 | 60 (351), 69 (37), 67 (8), 76 (1) |
| 79136 | 393 (136..538) | 377 | 11 | 76 (169), 160 (110), 140 (44), 54 (33), 67 (21) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 145/396/1003; tracks with internal gaps: 29; total internal gaps: 253; longest internal gap: 7; tracks ending in coasting: 28 (trailing rows total 857)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 1003 | 993 | 10 | 10 | 1 | 0 | 78911 |
| 31 | 78..484 | 407 | 407 | 368 | 39 | 8 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 35 | 86..561 | 476 | 476 | 426 | 50 | 13 | 6 | 29 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 36 | 86..521 | 436 | 436 | 398 | 38 | 11 | 2 | 24 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 40 | 88..478 | 391 | 391 | 346 | 45 | 13 | 2 | 28 | 78897, 78899, 78969, 79045, 79097, 79098, 79102 |
| 42 | 90..560 | 471 | 471 | 426 | 45 | 14 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 43 | 91..513 | 423 | 423 | 382 | 41 | 9 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110 |
| 47 | 95..490 | 396 | 396 | 344 | 52 | 14 | 5 | 29 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 50 | 98..281 | 184 | 184 | 137 | 47 | 8 | 2 | 38 | 78897, 78899, 78971, 79037, 79045 |
| 51 | 100..468 | 369 | 369 | 335 | 34 | 4 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102 |
| 52 | 100..559 | 460 | 460 | 422 | 38 | 8 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 54 | 101..571 | 471 | 471 | 436 | 35 | 6 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 55 | 105..544 | 440 | 440 | 398 | 42 | 10 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 56 | 106..250 | 145 | 145 | 97 | 48 | 2 | 1 | 46 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 60 | 111..566 | 456 | 456 | 416 | 40 | 7 | 5 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 61 | 111..526 | 416 | 416 | 374 | 42 | 8 | 3 | 32 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 115..529 | 415 | 415 | 379 | 36 | 7 | 1 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 67 | 122..562 | 441 | 441 | 388 | 53 | 16 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 126..556 | 431 | 431 | 394 | 37 | 6 | 2 | 29 | 79128, 79134, 79135, 79139 |
| 71 | 127..458 | 332 | 332 | 283 | 49 | 12 | 7 | 29 | 78896 |
| 73 | 132..463 | 332 | 332 | 295 | 37 | 7 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 76 | 135..349 | 215 | 215 | 170 | 45 | 11 | 4 | 31 | 79136, 79139 |
| 77 | 136..328 | 193 | 193 | 153 | 40 | 8 | 1 | 32 | 78969, 78971 |
| 80 | 142..472 | 331 | 331 | 289 | 42 | 11 | 3 | 29 | 78969, 78971, 79037, 79045 |
| 82 | 144..496 | 353 | 353 | 309 | 44 | 9 | 5 | 29 | 79098, 79105, 79108, 79110 |
| 123 | 235..510 | 276 | 276 | 236 | 40 | 11 | 1 | 29 | 79098, 79102, 79103 |
| 140 | 267..567 | 301 | 301 | 264 | 37 | 5 | 3 | 29 | 79115, 79116, 79122, 79134, 79136 |
| 156 | 306..506 | 201 | 201 | 169 | 32 | 2 | 2 | 29 | 79097, 79102 |
| 160 | 322..481 | 160 | 160 | 110 | 50 | 3 | 2 | 46 | 79136 |
