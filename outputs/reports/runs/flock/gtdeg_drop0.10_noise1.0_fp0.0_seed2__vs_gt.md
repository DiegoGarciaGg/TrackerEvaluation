# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=40f24e341aa1
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise1.0_fp0.0_seed2/tracks.csv sha256=adb5aea14575b551
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise1.0_fp0.0_seed2.csv sha256=40f24e341aa1c965
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise1.0_fp0.0_seed2
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
| observations | none | 4 | 0.631 | 0.545 | 0.865 | 1.28 | 0.832 | 237 | 980.0 |
| observations | none | 6 | 0.680 | 0.597 | 0.866 | 1.28 | 0.835 | 233 | 976.0 |
| observations | none | 8 | 0.708 | 0.639 | 0.867 | 1.30 | 0.842 | 227 | 973.0 |
| observations | none | 12 | 0.746 | 0.694 | 0.867 | 1.34 | 0.856 | 203 | 981.0 |
| observations | ignore | 4 | 0.631 | 0.545 | 0.865 | 1.28 | 0.832 | 237 | 980.0 |
| observations | ignore | 6 | 0.680 | 0.597 | 0.866 | 1.28 | 0.835 | 233 | 976.0 |
| observations | ignore | 8 | 0.708 | 0.639 | 0.867 | 1.30 | 0.842 | 227 | 973.0 |
| observations | ignore | 12 | 0.746 | 0.694 | 0.867 | 1.34 | 0.856 | 203 | 981.0 |
| updates | none | 4 | 0.578 | 0.505 | 0.713 | 1.30 | 0.774 | 250 | 894.0 |
| updates | none | 6 | 0.649 | 0.576 | 0.779 | 1.44 | 0.805 | 240 | 610.0 |
| updates | none | 8 | 0.691 | 0.629 | 0.847 | 1.64 | 0.842 | 226 | 312.0 |
| updates | none | 12 | 0.743 | 0.696 | 0.872 | 1.82 | 0.868 | 205 | 220.0 |
| updates | ignore | 4 | 0.578 | 0.505 | 0.713 | 1.30 | 0.774 | 250 | 894.0 |
| updates | ignore | 6 | 0.649 | 0.576 | 0.779 | 1.44 | 0.805 | 240 | 610.0 |
| updates | ignore | 8 | 0.691 | 0.629 | 0.847 | 1.64 | 0.842 | 226 | 312.0 |
| updates | ignore | 12 | 0.743 | 0.696 | 0.872 | 1.82 | 0.868 | 205 | 220.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9021; unmatched reference entries: 1121; unmatched candidate entries: 2
- identity switches: 227; fragmentation (coverage interruptions): 932; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 7 -> 14 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 11 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78971: 6 -> 3 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 10 -> 17 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 7 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 18 -> 7 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 19 -> 18 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 19 -> 22 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 6 -> 16 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 3 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 13 -> 6 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 7 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 7 -> 18 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 18 -> 19 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 15 -> 7 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 18 -> 15 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 19 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 22 -> 19 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 19 -> 22 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 10 -> 7 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79115: 21 -> 22 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 7 -> 23 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79105: 15 -> 10 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 18 -> 15 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 19 -> 18 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 22 -> 19 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 11 -> 6 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 6 -> 14 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 14 -> 13 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 23 -> 11 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 7 -> 23 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 14 -> 16 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 13 -> 14 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 16 -> 6 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 6 -> 17 at (1988.5, 3032), 2 frames after previous cover
- f120: ref 79098: 11 -> 6 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 23 -> 11 at (2025.5, 3030.5), 2 frames after previous cover
- f120: ref 79105: 10 -> 23 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 15 -> 10 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 18 -> 15 at (2077, 3028), 3 frames after previous cover
- f120: ref 79111: 19 -> 18 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 22 -> 19 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 21 -> 22 at (2120, 3023.5), 3 frames after previous cover
- f121: ref 78897: 6 -> 11 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 17 -> 7 at (1992.5, 3031), 1 frames after previous cover
- f121: ref 79102: 11 -> 23 at (2019.5, 3029), 1 frames after previous cover
- f121: ref 79105: 23 -> 10 at (2040, 3025), 1 frames after previous cover
- ... 167 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 910 | 85 | 2 (910) |
| 78896 | 350 (76..429) | 312 | 30 | 26 (269), 3 (43) |
| 78969 | 352 (80..434) | 295 | 42 | 29 (252), 8 (33), 3 (9), 13 (1) |
| 78971 | 352 (84..439) | 315 | 27 | 30 (265), 6 (24), 13 (24), 3 (1), 14 (1) |
| 79045 | 355 (84..443) | 304 | 35 | 13 (268), 14 (28), 3 (4), 27 (2), 7 (1), 8 (1) |
| 79037 | 355 (86..445) | 312 | 36 | 27 (268), 13 (17), 16 (11), 6 (4), 14 (4), 11 (3), 7 (2), 3 (2), 10 (1) |
| 78897 | 345 (89..450) | 314 | 27 | 14 (275), 11 (19), 16 (8), 8 (4), 10 (3), 7 (2), 6 (2), 27 (1) |
| 78899 | 365 (91..455) | 330 | 32 | 3 (290), 16 (11), 11 (9), 8 (6), 7 (3), 10 (3), 17 (3), 6 (2), 27 (2), 14 (1) |
| 79097 | 366 (94..461) | 327 | 34 | 8 (291), 17 (19), 7 (7), 11 (6), 10 (2), 16 (2) |
| 79098 | 360 (97..467) | 316 | 38 | 16 (283), 10 (11), 7 (6), 11 (6), 17 (4), 23 (2), 6 (2), 8 (1), 3 (1) |
| 79102 | 371 (98..477) | 335 | 30 | 11 (305), 7 (16), 23 (6), 10 (3), 6 (2), 16 (2), 17 (1) |
| 79103 | 380 (99..481) | 343 | 33 | 7 (322), 15 (12), 23 (6), 10 (1), 6 (1), 17 (1) |
| 79105 | 379 (101..484) | 335 | 33 | 23 (312), 10 (7), 18 (6), 15 (6), 17 (2), 7 (1), 6 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 31 (314), 15 (18), 18 (5), 19 (3), 10 (3), 24 (1) |
| 79110 | 388 (106..497) | 341 | 41 | 15 (312), 18 (18), 19 (5), 22 (2), 24 (2), 10 (1), 11 (1) |
| 79111 | 386 (109..500) | 333 | 43 | 18 (315), 24 (9), 19 (6), 22 (2), 17 (1) |
| 79115 | 421 (111..531) | 368 | 43 | 17 (240), 24 (111), 22 (6), 19 (4), 21 (3), 10 (3), 6 (1) |
| 79116 | 411 (114..530) | 377 | 30 | 24 (245), 17 (112), 10 (7), 21 (4), 6 (4), 22 (3), 19 (2) |
| 79122 | 404 (118..532) | 349 | 46 | 6 (333), 21 (5), 10 (4), 22 (3), 19 (3), 17 (1) |
| 79132 | 391 (120..515) | 350 | 36 | 10 (333), 19 (7), 21 (3), 22 (3), 6 (3), 24 (1) |
| 79128 | 402 (124..527) | 358 | 39 | 19 (348), 22 (6), 21 (3), 25 (1) |
| 79134 | 407 (127..533) | 362 | 35 | 22 (318), 25 (37), 21 (7) |
| 79135 | 409 (129..542) | 363 | 41 | 21 (295), 28 (60), 25 (8) |
| 79139 | 406 (132..537) | 380 | 22 | 25 (327), 22 (42), 21 (10), 28 (1) |
| 79136 | 393 (136..538) | 348 | 39 | 28 (289), 21 (53), 25 (5), 22 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 298/396/1003; tracks with internal gaps: 2; total internal gaps: 2; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 910 | 910 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 78..455 | 378 | 350 | 350 | 0 | 0 | 0 | 0 | 78896, 78899, 78969, 78971, 79037, 79045, 79098 |
| 6 | 86..532 | 447 | 379 | 379 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79132 |
| 7 | 86..481 | 396 | 360 | 360 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 88..461 | 374 | 336 | 336 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79045, 79097, 79098 |
| 10 | 90..515 | 426 | 382 | 382 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132 |
| 11 | 91..477 | 387 | 349 | 349 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79110 |
| 13 | 95..443 | 349 | 310 | 310 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 14 | 98..449 | 352 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 15 | 100..497 | 398 | 348 | 348 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110 |
| 16 | 100..467 | 368 | 317 | 317 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 17 | 101..531 | 431 | 384 | 384 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122 |
| 18 | 105..500 | 396 | 344 | 344 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111 |
| 19 | 106..527 | 422 | 378 | 378 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..537 | 427 | 383 | 383 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 22 | 111..538 | 428 | 386 | 386 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 23 | 115..484 | 370 | 327 | 326 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105 |
| 24 | 122..530 | 409 | 369 | 369 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 126..533 | 408 | 379 | 378 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 26 | 127..429 | 303 | 269 | 269 | 0 | 0 | 0 | 0 | 78896 |
| 27 | 132..445 | 314 | 273 | 273 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 28 | 135..542 | 408 | 350 | 350 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 29 | 136..434 | 299 | 252 | 252 | 0 | 0 | 0 | 0 | 78969 |
| 30 | 142..439 | 298 | 265 | 265 | 0 | 0 | 0 | 0 | 78971 |
| 31 | 144..492 | 349 | 314 | 314 | 0 | 0 | 0 | 0 | 79108 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9021; unmatched reference entries: 1121; unmatched candidate entries: 2
- identity switches: 227; fragmentation (coverage interruptions): 932; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 7 -> 14 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 11 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78971: 6 -> 3 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 10 -> 17 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 7 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 18 -> 7 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 19 -> 18 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 19 -> 22 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 6 -> 16 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 3 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 13 -> 6 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 7 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 7 -> 18 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 18 -> 19 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 15 -> 7 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 18 -> 15 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 19 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 22 -> 19 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 19 -> 22 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 10 -> 7 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79115: 21 -> 22 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 7 -> 23 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79105: 15 -> 10 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 18 -> 15 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 19 -> 18 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 22 -> 19 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 11 -> 6 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 6 -> 14 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 14 -> 13 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 23 -> 11 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 7 -> 23 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 14 -> 16 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 13 -> 14 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 16 -> 6 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 6 -> 17 at (1988.5, 3032), 2 frames after previous cover
- f120: ref 79098: 11 -> 6 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 23 -> 11 at (2025.5, 3030.5), 2 frames after previous cover
- f120: ref 79105: 10 -> 23 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 15 -> 10 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 18 -> 15 at (2077, 3028), 3 frames after previous cover
- f120: ref 79111: 19 -> 18 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 22 -> 19 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 21 -> 22 at (2120, 3023.5), 3 frames after previous cover
- f121: ref 78897: 6 -> 11 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 17 -> 7 at (1992.5, 3031), 1 frames after previous cover
- f121: ref 79102: 11 -> 23 at (2019.5, 3029), 1 frames after previous cover
- f121: ref 79105: 23 -> 10 at (2040, 3025), 1 frames after previous cover
- ... 167 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 910 | 85 | 2 (910) |
| 78896 | 350 (76..429) | 312 | 30 | 26 (269), 3 (43) |
| 78969 | 352 (80..434) | 295 | 42 | 29 (252), 8 (33), 3 (9), 13 (1) |
| 78971 | 352 (84..439) | 315 | 27 | 30 (265), 6 (24), 13 (24), 3 (1), 14 (1) |
| 79045 | 355 (84..443) | 304 | 35 | 13 (268), 14 (28), 3 (4), 27 (2), 7 (1), 8 (1) |
| 79037 | 355 (86..445) | 312 | 36 | 27 (268), 13 (17), 16 (11), 6 (4), 14 (4), 11 (3), 7 (2), 3 (2), 10 (1) |
| 78897 | 345 (89..450) | 314 | 27 | 14 (275), 11 (19), 16 (8), 8 (4), 10 (3), 7 (2), 6 (2), 27 (1) |
| 78899 | 365 (91..455) | 330 | 32 | 3 (290), 16 (11), 11 (9), 8 (6), 7 (3), 10 (3), 17 (3), 6 (2), 27 (2), 14 (1) |
| 79097 | 366 (94..461) | 327 | 34 | 8 (291), 17 (19), 7 (7), 11 (6), 10 (2), 16 (2) |
| 79098 | 360 (97..467) | 316 | 38 | 16 (283), 10 (11), 7 (6), 11 (6), 17 (4), 23 (2), 6 (2), 8 (1), 3 (1) |
| 79102 | 371 (98..477) | 335 | 30 | 11 (305), 7 (16), 23 (6), 10 (3), 6 (2), 16 (2), 17 (1) |
| 79103 | 380 (99..481) | 343 | 33 | 7 (322), 15 (12), 23 (6), 10 (1), 6 (1), 17 (1) |
| 79105 | 379 (101..484) | 335 | 33 | 23 (312), 10 (7), 18 (6), 15 (6), 17 (2), 7 (1), 6 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 31 (314), 15 (18), 18 (5), 19 (3), 10 (3), 24 (1) |
| 79110 | 388 (106..497) | 341 | 41 | 15 (312), 18 (18), 19 (5), 22 (2), 24 (2), 10 (1), 11 (1) |
| 79111 | 386 (109..500) | 333 | 43 | 18 (315), 24 (9), 19 (6), 22 (2), 17 (1) |
| 79115 | 421 (111..531) | 368 | 43 | 17 (240), 24 (111), 22 (6), 19 (4), 21 (3), 10 (3), 6 (1) |
| 79116 | 411 (114..530) | 377 | 30 | 24 (245), 17 (112), 10 (7), 21 (4), 6 (4), 22 (3), 19 (2) |
| 79122 | 404 (118..532) | 349 | 46 | 6 (333), 21 (5), 10 (4), 22 (3), 19 (3), 17 (1) |
| 79132 | 391 (120..515) | 350 | 36 | 10 (333), 19 (7), 21 (3), 22 (3), 6 (3), 24 (1) |
| 79128 | 402 (124..527) | 358 | 39 | 19 (348), 22 (6), 21 (3), 25 (1) |
| 79134 | 407 (127..533) | 362 | 35 | 22 (318), 25 (37), 21 (7) |
| 79135 | 409 (129..542) | 363 | 41 | 21 (295), 28 (60), 25 (8) |
| 79139 | 406 (132..537) | 380 | 22 | 25 (327), 22 (42), 21 (10), 28 (1) |
| 79136 | 393 (136..538) | 348 | 39 | 28 (289), 21 (53), 25 (5), 22 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 298/396/1003; tracks with internal gaps: 2; total internal gaps: 2; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 910 | 910 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 78..455 | 378 | 350 | 350 | 0 | 0 | 0 | 0 | 78896, 78899, 78969, 78971, 79037, 79045, 79098 |
| 6 | 86..532 | 447 | 379 | 379 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79132 |
| 7 | 86..481 | 396 | 360 | 360 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 88..461 | 374 | 336 | 336 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79045, 79097, 79098 |
| 10 | 90..515 | 426 | 382 | 382 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132 |
| 11 | 91..477 | 387 | 349 | 349 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79110 |
| 13 | 95..443 | 349 | 310 | 310 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 14 | 98..449 | 352 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 15 | 100..497 | 398 | 348 | 348 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110 |
| 16 | 100..467 | 368 | 317 | 317 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 17 | 101..531 | 431 | 384 | 384 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122 |
| 18 | 105..500 | 396 | 344 | 344 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111 |
| 19 | 106..527 | 422 | 378 | 378 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..537 | 427 | 383 | 383 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 22 | 111..538 | 428 | 386 | 386 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 23 | 115..484 | 370 | 327 | 326 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105 |
| 24 | 122..530 | 409 | 369 | 369 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 126..533 | 408 | 379 | 378 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 26 | 127..429 | 303 | 269 | 269 | 0 | 0 | 0 | 0 | 78896 |
| 27 | 132..445 | 314 | 273 | 273 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 28 | 135..542 | 408 | 350 | 350 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 29 | 136..434 | 299 | 252 | 252 | 0 | 0 | 0 | 0 | 78969 |
| 30 | 142..439 | 298 | 265 | 265 | 0 | 0 | 0 | 0 | 78971 |
| 31 | 144..492 | 349 | 314 | 314 | 0 | 0 | 0 | 0 | 79108 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9828; unmatched reference entries: 314; unmatched candidate entries: 1008
- identity switches: 226; fragmentation (coverage interruptions): 219; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 7 -> 14 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 11 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78971: 6 -> 3 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 10 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 18 -> 7 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 19 -> 18 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 19 -> 22 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 6 -> 16 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 3 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 13 -> 6 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 7 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 7 -> 18 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 18 -> 19 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 15 -> 7 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 18 -> 15 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 19 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 22 -> 19 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 19 -> 22 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 10 -> 7 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79103: 7 -> 10 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79115: 21 -> 22 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 7 -> 23 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79103: 10 -> 7 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 15 -> 10 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 18 -> 15 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 19 -> 18 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 22 -> 19 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 11 -> 6 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 6 -> 14 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 14 -> 13 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 23 -> 11 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 7 -> 23 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 14 -> 16 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 13 -> 14 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 16 -> 6 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 6 -> 17 at (1988.5, 3032), 1 frames after previous cover
- f120: ref 79098: 11 -> 6 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 23 -> 11 at (2025.5, 3030.5), 1 frames after previous cover
- f120: ref 79105: 10 -> 23 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 15 -> 10 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 18 -> 15 at (2077, 3028), 2 frames after previous cover
- f120: ref 79111: 19 -> 18 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 22 -> 19 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 21 -> 22 at (2120, 3023.5), 2 frames after previous cover
- f121: ref 78897: 6 -> 11 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 17 -> 7 at (1992.5, 3031), 1 frames after previous cover
- ... 166 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 997 | 6 | 2 (997) |
| 78896 | 350 (76..429) | 334 | 12 | 26 (290), 3 (44) |
| 78969 | 352 (80..434) | 326 | 16 | 29 (282), 8 (34), 3 (9), 13 (1) |
| 78971 | 352 (84..439) | 336 | 10 | 30 (285), 6 (25), 13 (24), 3 (1), 14 (1) |
| 79045 | 355 (84..443) | 331 | 10 | 13 (295), 14 (29), 3 (4), 7 (1), 8 (1), 27 (1) |
| 79037 | 355 (86..445) | 343 | 10 | 27 (299), 13 (17), 16 (11), 6 (4), 14 (4), 11 (3), 7 (2), 3 (2), 10 (1) |
| 78897 | 345 (89..450) | 331 | 11 | 14 (291), 11 (19), 16 (9), 8 (4), 10 (3), 7 (2), 6 (2), 27 (1) |
| 78899 | 365 (91..455) | 354 | 9 | 3 (312), 16 (12), 11 (9), 8 (6), 7 (3), 10 (3), 6 (3), 17 (3), 27 (2), 14 (1) |
| 79097 | 366 (94..461) | 355 | 8 | 8 (319), 17 (19), 7 (7), 11 (6), 10 (2), 16 (2) |
| 79098 | 360 (97..467) | 349 | 8 | 16 (315), 10 (12), 7 (6), 11 (6), 17 (4), 23 (2), 6 (2), 8 (1), 3 (1) |
| 79102 | 371 (98..477) | 360 | 8 | 11 (328), 7 (16), 23 (8), 10 (3), 6 (2), 16 (2), 17 (1) |
| 79103 | 380 (99..481) | 370 | 8 | 7 (346), 15 (13), 23 (6), 10 (2), 6 (2), 17 (1) |
| 79105 | 379 (101..484) | 367 | 8 | 23 (341), 18 (7), 15 (7), 10 (7), 17 (3), 7 (1), 6 (1) |
| 79108 | 385 (104..492) | 373 | 6 | 31 (342), 15 (19), 18 (5), 19 (3), 10 (3), 24 (1) |
| 79110 | 388 (106..497) | 380 | 7 | 15 (346), 18 (19), 19 (5), 31 (4), 22 (2), 24 (2), 10 (1), 11 (1) |
| 79111 | 386 (109..500) | 367 | 13 | 18 (349), 24 (9), 19 (6), 22 (2), 17 (1) |
| 79115 | 421 (111..531) | 408 | 11 | 17 (269), 24 (121), 22 (6), 19 (4), 21 (3), 10 (3), 6 (1), 18 (1) |
| 79116 | 411 (114..530) | 405 | 6 | 24 (261), 17 (122), 10 (7), 21 (5), 6 (5), 22 (3), 19 (2) |
| 79122 | 404 (118..532) | 390 | 11 | 6 (375), 21 (5), 10 (4), 22 (3), 19 (3) |
| 79132 | 391 (120..515) | 380 | 8 | 10 (363), 19 (7), 21 (3), 22 (3), 6 (3), 24 (1) |
| 79128 | 402 (124..527) | 391 | 8 | 19 (380), 22 (7), 21 (3), 25 (1) |
| 79134 | 407 (127..533) | 398 | 7 | 22 (352), 25 (39), 21 (7) |
| 79135 | 409 (129..542) | 402 | 6 | 21 (322), 28 (71), 25 (9) |
| 79139 | 406 (132..537) | 399 | 4 | 25 (329), 21 (69), 28 (1) |
| 79136 | 393 (136..538) | 382 | 8 | 28 (317), 22 (44), 25 (21) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 327/425/1003; tracks with internal gaps: 25; total internal gaps: 262; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 693)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 1003 | 997 | 6 | 6 | 1 | 0 | 78911 |
| 3 | 78..484 | 407 | 407 | 373 | 34 | 5 | 1 | 29 | 78896, 78899, 78969, 78971, 79037, 79045, 79098 |
| 6 | 86..561 | 476 | 476 | 425 | 51 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79132 |
| 7 | 86..510 | 425 | 425 | 384 | 41 | 10 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 88..490 | 403 | 403 | 365 | 38 | 7 | 2 | 29 | 78897, 78899, 78969, 79045, 79097, 79098 |
| 10 | 90..544 | 455 | 455 | 414 | 41 | 11 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132 |
| 11 | 91..506 | 416 | 416 | 372 | 44 | 13 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79110 |
| 13 | 95..472 | 378 | 378 | 337 | 41 | 10 | 3 | 29 | 78969, 78971, 79037, 79045 |
| 14 | 98..478 | 381 | 381 | 326 | 55 | 20 | 5 | 28 | 78897, 78899, 78971, 79037, 79045 |
| 15 | 100..526 | 427 | 427 | 385 | 42 | 10 | 1 | 32 | 79103, 79105, 79108, 79110 |
| 16 | 100..496 | 397 | 397 | 351 | 46 | 13 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 17 | 101..560 | 460 | 460 | 423 | 37 | 8 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116 |
| 18 | 105..529 | 425 | 425 | 381 | 44 | 12 | 2 | 29 | 79105, 79108, 79110, 79111, 79115 |
| 19 | 106..556 | 451 | 451 | 410 | 41 | 10 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..566 | 456 | 456 | 417 | 39 | 9 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 111..567 | 457 | 457 | 422 | 35 | 4 | 3 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 23 | 115..513 | 399 | 399 | 357 | 42 | 11 | 3 | 29 | 79098, 79102, 79103, 79105 |
| 24 | 122..559 | 438 | 438 | 395 | 43 | 11 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 126..562 | 437 | 437 | 399 | 38 | 7 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 26 | 127..458 | 332 | 332 | 290 | 42 | 11 | 3 | 29 | 78896 |
| 27 | 132..474 | 343 | 343 | 303 | 40 | 9 | 2 | 29 | 78897, 78899, 79037, 79045 |
| 28 | 135..571 | 437 | 437 | 389 | 48 | 15 | 4 | 29 | 79135, 79136, 79139 |
| 29 | 136..463 | 328 | 328 | 282 | 46 | 15 | 3 | 29 | 78969 |
| 30 | 142..468 | 327 | 327 | 285 | 42 | 10 | 3 | 29 | 78971 |
| 31 | 144..521 | 378 | 378 | 346 | 32 | 7 | 2 | 24 | 79108, 79110 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9828; unmatched reference entries: 314; unmatched candidate entries: 1008
- identity switches: 226; fragmentation (coverage interruptions): 219; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79045: 7 -> 14 at (2075.5, 3033), 12 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f111: ref 78897: 11 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78971: 6 -> 3 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 10 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 18 -> 7 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 19 -> 18 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 19 -> 22 at (2129, 3027), 1 frames after previous cover
- f112: ref 78897: 6 -> 16 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78971: 3 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 13 -> 6 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 7 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79105: 7 -> 18 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 18 -> 19 at (2109, 3027), 1 frames after previous cover
- f113: ref 79103: 15 -> 7 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 18 -> 15 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 19 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 22 -> 19 at (2117, 3027.5), 1 frames after previous cover
- f113: ref 79111: 19 -> 22 at (2132.5, 3027.5), 2 frames after previous cover
- f114: ref 79102: 10 -> 7 at (2061.5, 3029), 1 frames after previous cover
- f114: ref 79103: 7 -> 10 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79115: 21 -> 22 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79098: 7 -> 23 at (2042.5, 3029), 3 frames after previous cover
- f115: ref 79103: 10 -> 7 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 15 -> 10 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 18 -> 15 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 19 -> 18 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 22 -> 19 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78899: 11 -> 6 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 6 -> 14 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 14 -> 13 at (1963.5, 3035.5), 1 frames after previous cover
- f116: ref 79098: 23 -> 11 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 7 -> 23 at (2049.5, 3030.5), 2 frames after previous cover
- f117: ref 79037: 14 -> 16 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 13 -> 14 at (1956.5, 3034.5), 1 frames after previous cover
- f119: ref 78897: 16 -> 6 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 6 -> 17 at (1988.5, 3032), 1 frames after previous cover
- f120: ref 79098: 11 -> 6 at (2012, 3030), 1 frames after previous cover
- f120: ref 79102: 23 -> 11 at (2025.5, 3030.5), 1 frames after previous cover
- f120: ref 79105: 10 -> 23 at (2044.5, 3026.5), 1 frames after previous cover
- f120: ref 79108: 15 -> 10 at (2064, 3027), 2 frames after previous cover
- f120: ref 79110: 18 -> 15 at (2077, 3028), 2 frames after previous cover
- f120: ref 79111: 19 -> 18 at (2091.5, 3030), 1 frames after previous cover
- f120: ref 79115: 22 -> 19 at (2108, 3020), 1 frames after previous cover
- f120: ref 79116: 21 -> 22 at (2120, 3023.5), 2 frames after previous cover
- f121: ref 78897: 6 -> 11 at (1958, 3035.5), 2 frames after previous cover
- f121: ref 79097: 17 -> 7 at (1992.5, 3031), 1 frames after previous cover
- ... 166 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 997 | 6 | 2 (997) |
| 78896 | 350 (76..429) | 334 | 12 | 26 (290), 3 (44) |
| 78969 | 352 (80..434) | 326 | 16 | 29 (282), 8 (34), 3 (9), 13 (1) |
| 78971 | 352 (84..439) | 336 | 10 | 30 (285), 6 (25), 13 (24), 3 (1), 14 (1) |
| 79045 | 355 (84..443) | 331 | 10 | 13 (295), 14 (29), 3 (4), 7 (1), 8 (1), 27 (1) |
| 79037 | 355 (86..445) | 343 | 10 | 27 (299), 13 (17), 16 (11), 6 (4), 14 (4), 11 (3), 7 (2), 3 (2), 10 (1) |
| 78897 | 345 (89..450) | 331 | 11 | 14 (291), 11 (19), 16 (9), 8 (4), 10 (3), 7 (2), 6 (2), 27 (1) |
| 78899 | 365 (91..455) | 354 | 9 | 3 (312), 16 (12), 11 (9), 8 (6), 7 (3), 10 (3), 6 (3), 17 (3), 27 (2), 14 (1) |
| 79097 | 366 (94..461) | 355 | 8 | 8 (319), 17 (19), 7 (7), 11 (6), 10 (2), 16 (2) |
| 79098 | 360 (97..467) | 349 | 8 | 16 (315), 10 (12), 7 (6), 11 (6), 17 (4), 23 (2), 6 (2), 8 (1), 3 (1) |
| 79102 | 371 (98..477) | 360 | 8 | 11 (328), 7 (16), 23 (8), 10 (3), 6 (2), 16 (2), 17 (1) |
| 79103 | 380 (99..481) | 370 | 8 | 7 (346), 15 (13), 23 (6), 10 (2), 6 (2), 17 (1) |
| 79105 | 379 (101..484) | 367 | 8 | 23 (341), 18 (7), 15 (7), 10 (7), 17 (3), 7 (1), 6 (1) |
| 79108 | 385 (104..492) | 373 | 6 | 31 (342), 15 (19), 18 (5), 19 (3), 10 (3), 24 (1) |
| 79110 | 388 (106..497) | 380 | 7 | 15 (346), 18 (19), 19 (5), 31 (4), 22 (2), 24 (2), 10 (1), 11 (1) |
| 79111 | 386 (109..500) | 367 | 13 | 18 (349), 24 (9), 19 (6), 22 (2), 17 (1) |
| 79115 | 421 (111..531) | 408 | 11 | 17 (269), 24 (121), 22 (6), 19 (4), 21 (3), 10 (3), 6 (1), 18 (1) |
| 79116 | 411 (114..530) | 405 | 6 | 24 (261), 17 (122), 10 (7), 21 (5), 6 (5), 22 (3), 19 (2) |
| 79122 | 404 (118..532) | 390 | 11 | 6 (375), 21 (5), 10 (4), 22 (3), 19 (3) |
| 79132 | 391 (120..515) | 380 | 8 | 10 (363), 19 (7), 21 (3), 22 (3), 6 (3), 24 (1) |
| 79128 | 402 (124..527) | 391 | 8 | 19 (380), 22 (7), 21 (3), 25 (1) |
| 79134 | 407 (127..533) | 398 | 7 | 22 (352), 25 (39), 21 (7) |
| 79135 | 409 (129..542) | 402 | 6 | 21 (322), 28 (71), 25 (9) |
| 79139 | 406 (132..537) | 399 | 4 | 25 (329), 21 (69), 28 (1) |
| 79136 | 393 (136..538) | 382 | 8 | 28 (317), 22 (44), 25 (21) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 327/425/1003; tracks with internal gaps: 25; total internal gaps: 262; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 693)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 1003 | 997 | 6 | 6 | 1 | 0 | 78911 |
| 3 | 78..484 | 407 | 407 | 373 | 34 | 5 | 1 | 29 | 78896, 78899, 78969, 78971, 79037, 79045, 79098 |
| 6 | 86..561 | 476 | 476 | 425 | 51 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79132 |
| 7 | 86..510 | 425 | 425 | 384 | 41 | 10 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 88..490 | 403 | 403 | 365 | 38 | 7 | 2 | 29 | 78897, 78899, 78969, 79045, 79097, 79098 |
| 10 | 90..544 | 455 | 455 | 414 | 41 | 11 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132 |
| 11 | 91..506 | 416 | 416 | 372 | 44 | 13 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79110 |
| 13 | 95..472 | 378 | 378 | 337 | 41 | 10 | 3 | 29 | 78969, 78971, 79037, 79045 |
| 14 | 98..478 | 381 | 381 | 326 | 55 | 20 | 5 | 28 | 78897, 78899, 78971, 79037, 79045 |
| 15 | 100..526 | 427 | 427 | 385 | 42 | 10 | 1 | 32 | 79103, 79105, 79108, 79110 |
| 16 | 100..496 | 397 | 397 | 351 | 46 | 13 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 17 | 101..560 | 460 | 460 | 423 | 37 | 8 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79111, 79115, 79116 |
| 18 | 105..529 | 425 | 425 | 381 | 44 | 12 | 2 | 29 | 79105, 79108, 79110, 79111, 79115 |
| 19 | 106..556 | 451 | 451 | 410 | 41 | 10 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..566 | 456 | 456 | 417 | 39 | 9 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 111..567 | 457 | 457 | 422 | 35 | 4 | 3 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 23 | 115..513 | 399 | 399 | 357 | 42 | 11 | 3 | 29 | 79098, 79102, 79103, 79105 |
| 24 | 122..559 | 438 | 438 | 395 | 43 | 11 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 126..562 | 437 | 437 | 399 | 38 | 7 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 26 | 127..458 | 332 | 332 | 290 | 42 | 11 | 3 | 29 | 78896 |
| 27 | 132..474 | 343 | 343 | 303 | 40 | 9 | 2 | 29 | 78897, 78899, 79037, 79045 |
| 28 | 135..571 | 437 | 437 | 389 | 48 | 15 | 4 | 29 | 79135, 79136, 79139 |
| 29 | 136..463 | 328 | 328 | 282 | 46 | 15 | 3 | 29 | 78969 |
| 30 | 142..468 | 327 | 327 | 285 | 42 | 10 | 3 | 29 | 78971 |
| 31 | 144..521 | 378 | 378 | 346 | 32 | 7 | 2 | 24 | 79108, 79110 |
