# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=3782d1e217ba
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise3.0_fp0.0_seed3/tracks.csv sha256=a563ad1d46211149
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise3.0_fp0.0_seed3.csv sha256=3782d1e217ba6b7c
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise3.0_fp0.0_seed3
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
| observations | none | 4 | 0.309 | 0.240 | 0.114 | 2.41 | 0.420 | 351 | 2500.0 |
| observations | none | 6 | 0.435 | 0.347 | 0.617 | 3.22 | 0.633 | 432 | 1737.0 |
| observations | none | 8 | 0.505 | 0.419 | 0.797 | 3.61 | 0.717 | 433 | 1152.0 |
| observations | none | 12 | 0.588 | 0.515 | 0.848 | 3.90 | 0.772 | 354 | 965.0 |
| observations | ignore | 4 | 0.309 | 0.240 | 0.114 | 2.41 | 0.420 | 351 | 2500.0 |
| observations | ignore | 6 | 0.435 | 0.347 | 0.617 | 3.22 | 0.633 | 432 | 1737.0 |
| observations | ignore | 8 | 0.505 | 0.419 | 0.797 | 3.61 | 0.717 | 433 | 1152.0 |
| observations | ignore | 12 | 0.588 | 0.515 | 0.848 | 3.90 | 0.772 | 354 | 965.0 |
| updates | none | 4 | 0.293 | 0.230 | -0.019 | 2.41 | 0.401 | 382 | 2514.0 |
| updates | none | 6 | 0.422 | 0.341 | 0.524 | 3.25 | 0.612 | 455 | 1509.0 |
| updates | none | 8 | 0.499 | 0.419 | 0.743 | 3.69 | 0.708 | 436 | 704.0 |
| updates | none | 12 | 0.589 | 0.522 | 0.838 | 4.12 | 0.777 | 325 | 324.0 |
| updates | ignore | 4 | 0.293 | 0.230 | -0.019 | 2.41 | 0.401 | 382 | 2514.0 |
| updates | ignore | 6 | 0.422 | 0.341 | 0.524 | 3.25 | 0.612 | 455 | 1509.0 |
| updates | ignore | 8 | 0.499 | 0.419 | 0.743 | 3.69 | 0.708 | 436 | 704.0 |
| updates | ignore | 12 | 0.589 | 0.522 | 0.838 | 4.12 | 0.777 | 325 | 324.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8815; unmatched reference entries: 1327; unmatched candidate entries: 296
- identity switches: 433; fragmentation (coverage interruptions): 1108; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 6 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 6 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 5 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 6 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 6 -> 8 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79098: 6 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 10 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 8 -> 4 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 6 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 4 -> 10 at (2083, 3033.5), 6 frames after previous cover
- f101: ref 79097: 4 -> 9 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 6 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 9 -> 13 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 10 -> 14 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 4 -> 9 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 79097: 9 -> 4 at (2093.5, 3029.5), 2 frames after previous cover
- f104: ref 79103: 11 -> 6 at (2126, 3022.5), 2 frames after previous cover
- f106: ref 78897: 10 -> 14 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 14 -> 5 at (2038, 3034.5), 2 frames after previous cover
- f106: ref 79097: 4 -> 10 at (2082.5, 3028.5), 1 frames after previous cover
- f107: ref 79045: 5 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 9 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79102: 8 -> 9 at (2101.5, 3029.5), 2 frames after previous cover
- f108: ref 79105: 6 -> 8 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 79037: 5 -> 15 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 3 -> 5 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 11 -> 8 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 14 -> 15 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 13 -> 14 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 15 -> 5 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 5 -> 3 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 13 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 4 -> 10 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 9 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 78897: 15 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 14 -> 13 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 5 -> 15 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 3 -> 5 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 13 -> 10 at (2052, 3030), 1 frames after previous cover
- f112: ref 78899: 13 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 10 -> 13 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79103: 6 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 8 -> 6 at (2091.5, 3025.5), 4 frames after previous cover
- f113: ref 78897: 14 -> 13 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79097: 13 -> 10 at (2040.5, 3031), 1 frames after previous cover
- f113: ref 79098: 10 -> 4 at (2054, 3030), 1 frames after previous cover
- f113: ref 79102: 4 -> 9 at (2067, 3028.5), 1 frames after previous cover
- ... 373 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 886 | 106 | 1 (886) |
| 78896 | 350 (76..429) | 309 | 36 | 2 (309) |
| 78969 | 352 (80..434) | 307 | 35 | 12 (290), 3 (15), 2 (2) |
| 78971 | 352 (84..439) | 302 | 38 | 5 (263), 3 (36), 10 (2), 22 (1) |
| 79045 | 355 (84..443) | 300 | 40 | 3 (157), 22 (101), 5 (37), 4 (4), 12 (1) |
| 79037 | 355 (86..445) | 294 | 44 | 22 (164), 3 (105), 15 (11), 5 (5), 4 (2), 9 (2), 10 (2), 14 (2), 6 (1) |
| 78897 | 345 (89..450) | 295 | 38 | 15 (252), 4 (18), 14 (6), 10 (5), 3 (4), 22 (4), 6 (3), 19 (2), 13 (1) |
| 78899 | 365 (91..455) | 305 | 53 | 4 (249), 15 (20), 19 (12), 14 (10), 13 (8), 6 (2), 9 (2), 3 (2) |
| 79097 | 366 (94..461) | 329 | 33 | 19 (279), 4 (18), 15 (7), 10 (6), 13 (6), 14 (6), 8 (3), 6 (2), 9 (2) |
| 79098 | 360 (97..467) | 323 | 33 | 8 (276), 4 (15), 19 (14), 10 (5), 14 (5), 9 (4), 13 (2), 6 (1), 11 (1) |
| 79102 | 371 (98..477) | 330 | 38 | 14 (288), 8 (11), 4 (9), 10 (8), 9 (7), 13 (4), 6 (2), 11 (1) |
| 79103 | 380 (99..481) | 339 | 37 | 6 (284), 10 (24), 14 (19), 9 (9), 11 (2), 8 (1) |
| 79105 | 379 (101..484) | 323 | 49 | 10 (286), 9 (19), 6 (9), 8 (9) |
| 79108 | 385 (104..492) | 329 | 45 | 9 (288), 8 (19), 6 (12), 11 (4), 13 (3), 18 (1), 10 (1), 20 (1) |
| 79110 | 388 (106..497) | 339 | 45 | 23 (157), 20 (97), 18 (46), 13 (16), 11 (6), 6 (6), 9 (6), 8 (5) |
| 79111 | 386 (109..500) | 335 | 41 | 20 (219), 23 (53), 18 (39), 6 (13), 13 (5), 16 (3), 11 (3) |
| 79115 | 421 (111..531) | 378 | 35 | 11 (190), 18 (70), 23 (49), 27 (33), 20 (14), 13 (11), 6 (6), 16 (4), 17 (1) |
| 79116 | 411 (114..530) | 355 | 44 | 18 (178), 23 (57), 27 (42), 13 (34), 11 (31), 24 (5), 17 (4), 16 (2), 6 (2) |
| 79122 | 404 (118..532) | 355 | 41 | 27 (208), 11 (70), 13 (40), 18 (14), 23 (11), 16 (6), 6 (4), 17 (2) |
| 79132 | 391 (120..515) | 336 | 48 | 13 (224), 11 (65), 27 (30), 18 (6), 16 (5), 17 (3), 24 (3) |
| 79128 | 402 (124..527) | 364 | 34 | 24 (336), 16 (11), 11 (7), 18 (4), 17 (3), 21 (3) |
| 79134 | 407 (127..533) | 357 | 46 | 21 (231), 16 (84), 17 (42) |
| 79135 | 409 (129..542) | 341 | 54 | 16 (200), 21 (74), 26 (60), 24 (4), 17 (3) |
| 79139 | 406 (132..537) | 347 | 50 | 17 (273), 21 (51), 26 (12), 16 (11) |
| 79136 | 393 (136..538) | 337 | 45 | 26 (263), 16 (48), 17 (21), 24 (4), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 317/381/1004; tracks with internal gaps: 25; total internal gaps: 280; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 921 | 886 | 35 | 35 | 1 | 0 | 78911 |
| 2 | 78..429 | 352 | 321 | 311 | 10 | 10 | 1 | 0 | 78896, 78969 |
| 3 | 82..445 | 364 | 329 | 319 | 10 | 10 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 4 | 86..455 | 370 | 333 | 315 | 18 | 16 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..439 | 354 | 319 | 305 | 14 | 14 | 1 | 0 | 78971, 79037, 79045 |
| 6 | 88..481 | 394 | 360 | 347 | 13 | 12 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 8 | 96..467 | 372 | 327 | 324 | 3 | 2 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 9 | 96..492 | 397 | 351 | 339 | 12 | 11 | 2 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 97..484 | 388 | 346 | 339 | 7 | 7 | 1 | 0 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 99..530 | 432 | 390 | 380 | 10 | 9 | 2 | 0 | 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 12 | 102..434 | 333 | 296 | 291 | 5 | 5 | 1 | 0 | 78969, 79045 |
| 13 | 102..514 | 413 | 368 | 354 | 14 | 13 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 14 | 103..477 | 375 | 340 | 336 | 4 | 4 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 15 | 109..449 | 341 | 301 | 290 | 11 | 11 | 1 | 0 | 78897, 78899, 79037, 79097 |
| 16 | 110..535 | 426 | 380 | 374 | 6 | 6 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 113..533 | 421 | 370 | 352 | 18 | 17 | 2 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 117..532 | 416 | 375 | 358 | 17 | 15 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 120..461 | 342 | 314 | 307 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098 |
| 20 | 120..500 | 381 | 346 | 331 | 15 | 14 | 2 | 0 | 79108, 79110, 79111, 79115 |
| 21 | 127..538 | 412 | 371 | 360 | 11 | 11 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 22 | 127..443 | 317 | 280 | 270 | 10 | 9 | 2 | 0 | 78897, 78971, 79037, 79045 |
| 23 | 133..497 | 365 | 339 | 327 | 12 | 11 | 2 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 24 | 138..527 | 390 | 366 | 352 | 14 | 14 | 1 | 0 | 79116, 79128, 79132, 79135, 79136 |
| 26 | 145..542 | 398 | 345 | 335 | 10 | 9 | 2 | 0 | 79135, 79136, 79139 |
| 27 | 172..531 | 360 | 323 | 313 | 10 | 8 | 2 | 0 | 79115, 79116, 79122, 79132 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8815; unmatched reference entries: 1327; unmatched candidate entries: 296
- identity switches: 433; fragmentation (coverage interruptions): 1108; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 6 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 6 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 5 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 6 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 6 -> 8 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79098: 6 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 10 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 8 -> 4 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 6 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 4 -> 10 at (2083, 3033.5), 6 frames after previous cover
- f101: ref 79097: 4 -> 9 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 6 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 9 -> 13 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 10 -> 14 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 4 -> 9 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 79097: 9 -> 4 at (2093.5, 3029.5), 2 frames after previous cover
- f104: ref 79103: 11 -> 6 at (2126, 3022.5), 2 frames after previous cover
- f106: ref 78897: 10 -> 14 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 14 -> 5 at (2038, 3034.5), 2 frames after previous cover
- f106: ref 79097: 4 -> 10 at (2082.5, 3028.5), 1 frames after previous cover
- f107: ref 79045: 5 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 9 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79102: 8 -> 9 at (2101.5, 3029.5), 2 frames after previous cover
- f108: ref 79105: 6 -> 8 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 79037: 5 -> 15 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 3 -> 5 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 11 -> 8 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 14 -> 15 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 13 -> 14 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 15 -> 5 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 5 -> 3 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 13 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 4 -> 10 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 9 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 78897: 15 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 14 -> 13 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 5 -> 15 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 3 -> 5 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 13 -> 10 at (2052, 3030), 1 frames after previous cover
- f112: ref 78899: 13 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 10 -> 13 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79103: 6 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 8 -> 6 at (2091.5, 3025.5), 4 frames after previous cover
- f113: ref 78897: 14 -> 13 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79097: 13 -> 10 at (2040.5, 3031), 1 frames after previous cover
- f113: ref 79098: 10 -> 4 at (2054, 3030), 1 frames after previous cover
- f113: ref 79102: 4 -> 9 at (2067, 3028.5), 1 frames after previous cover
- ... 373 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 886 | 106 | 1 (886) |
| 78896 | 350 (76..429) | 309 | 36 | 2 (309) |
| 78969 | 352 (80..434) | 307 | 35 | 12 (290), 3 (15), 2 (2) |
| 78971 | 352 (84..439) | 302 | 38 | 5 (263), 3 (36), 10 (2), 22 (1) |
| 79045 | 355 (84..443) | 300 | 40 | 3 (157), 22 (101), 5 (37), 4 (4), 12 (1) |
| 79037 | 355 (86..445) | 294 | 44 | 22 (164), 3 (105), 15 (11), 5 (5), 4 (2), 9 (2), 10 (2), 14 (2), 6 (1) |
| 78897 | 345 (89..450) | 295 | 38 | 15 (252), 4 (18), 14 (6), 10 (5), 3 (4), 22 (4), 6 (3), 19 (2), 13 (1) |
| 78899 | 365 (91..455) | 305 | 53 | 4 (249), 15 (20), 19 (12), 14 (10), 13 (8), 6 (2), 9 (2), 3 (2) |
| 79097 | 366 (94..461) | 329 | 33 | 19 (279), 4 (18), 15 (7), 10 (6), 13 (6), 14 (6), 8 (3), 6 (2), 9 (2) |
| 79098 | 360 (97..467) | 323 | 33 | 8 (276), 4 (15), 19 (14), 10 (5), 14 (5), 9 (4), 13 (2), 6 (1), 11 (1) |
| 79102 | 371 (98..477) | 330 | 38 | 14 (288), 8 (11), 4 (9), 10 (8), 9 (7), 13 (4), 6 (2), 11 (1) |
| 79103 | 380 (99..481) | 339 | 37 | 6 (284), 10 (24), 14 (19), 9 (9), 11 (2), 8 (1) |
| 79105 | 379 (101..484) | 323 | 49 | 10 (286), 9 (19), 6 (9), 8 (9) |
| 79108 | 385 (104..492) | 329 | 45 | 9 (288), 8 (19), 6 (12), 11 (4), 13 (3), 18 (1), 10 (1), 20 (1) |
| 79110 | 388 (106..497) | 339 | 45 | 23 (157), 20 (97), 18 (46), 13 (16), 11 (6), 6 (6), 9 (6), 8 (5) |
| 79111 | 386 (109..500) | 335 | 41 | 20 (219), 23 (53), 18 (39), 6 (13), 13 (5), 16 (3), 11 (3) |
| 79115 | 421 (111..531) | 378 | 35 | 11 (190), 18 (70), 23 (49), 27 (33), 20 (14), 13 (11), 6 (6), 16 (4), 17 (1) |
| 79116 | 411 (114..530) | 355 | 44 | 18 (178), 23 (57), 27 (42), 13 (34), 11 (31), 24 (5), 17 (4), 16 (2), 6 (2) |
| 79122 | 404 (118..532) | 355 | 41 | 27 (208), 11 (70), 13 (40), 18 (14), 23 (11), 16 (6), 6 (4), 17 (2) |
| 79132 | 391 (120..515) | 336 | 48 | 13 (224), 11 (65), 27 (30), 18 (6), 16 (5), 17 (3), 24 (3) |
| 79128 | 402 (124..527) | 364 | 34 | 24 (336), 16 (11), 11 (7), 18 (4), 17 (3), 21 (3) |
| 79134 | 407 (127..533) | 357 | 46 | 21 (231), 16 (84), 17 (42) |
| 79135 | 409 (129..542) | 341 | 54 | 16 (200), 21 (74), 26 (60), 24 (4), 17 (3) |
| 79139 | 406 (132..537) | 347 | 50 | 17 (273), 21 (51), 26 (12), 16 (11) |
| 79136 | 393 (136..538) | 337 | 45 | 26 (263), 16 (48), 17 (21), 24 (4), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 317/381/1004; tracks with internal gaps: 25; total internal gaps: 280; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 921 | 886 | 35 | 35 | 1 | 0 | 78911 |
| 2 | 78..429 | 352 | 321 | 311 | 10 | 10 | 1 | 0 | 78896, 78969 |
| 3 | 82..445 | 364 | 329 | 319 | 10 | 10 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 4 | 86..455 | 370 | 333 | 315 | 18 | 16 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..439 | 354 | 319 | 305 | 14 | 14 | 1 | 0 | 78971, 79037, 79045 |
| 6 | 88..481 | 394 | 360 | 347 | 13 | 12 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 8 | 96..467 | 372 | 327 | 324 | 3 | 2 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 9 | 96..492 | 397 | 351 | 339 | 12 | 11 | 2 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 97..484 | 388 | 346 | 339 | 7 | 7 | 1 | 0 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 99..530 | 432 | 390 | 380 | 10 | 9 | 2 | 0 | 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 12 | 102..434 | 333 | 296 | 291 | 5 | 5 | 1 | 0 | 78969, 79045 |
| 13 | 102..514 | 413 | 368 | 354 | 14 | 13 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 14 | 103..477 | 375 | 340 | 336 | 4 | 4 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 15 | 109..449 | 341 | 301 | 290 | 11 | 11 | 1 | 0 | 78897, 78899, 79037, 79097 |
| 16 | 110..535 | 426 | 380 | 374 | 6 | 6 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 113..533 | 421 | 370 | 352 | 18 | 17 | 2 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 117..532 | 416 | 375 | 358 | 17 | 15 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 120..461 | 342 | 314 | 307 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098 |
| 20 | 120..500 | 381 | 346 | 331 | 15 | 14 | 2 | 0 | 79108, 79110, 79111, 79115 |
| 21 | 127..538 | 412 | 371 | 360 | 11 | 11 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 22 | 127..443 | 317 | 280 | 270 | 10 | 9 | 2 | 0 | 78897, 78971, 79037, 79045 |
| 23 | 133..497 | 365 | 339 | 327 | 12 | 11 | 2 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 24 | 138..527 | 390 | 366 | 352 | 14 | 14 | 1 | 0 | 79116, 79128, 79132, 79135, 79136 |
| 26 | 145..542 | 398 | 345 | 335 | 10 | 9 | 2 | 0 | 79135, 79136, 79139 |
| 27 | 172..531 | 360 | 323 | 313 | 10 | 8 | 2 | 0 | 79115, 79116, 79122, 79132 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9390; unmatched reference entries: 752; unmatched candidate entries: 1423
- identity switches: 436; fragmentation (coverage interruptions): 615; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 6 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 6 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 5 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 6 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 6 -> 8 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 4 -> 9 at (2100, 3031), 3 frames after previous cover
- f98: ref 79098: 6 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 10 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 8 -> 4 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 6 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 9 -> 10 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79097: 4 -> 9 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 6 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 9 -> 13 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 10 -> 14 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 4 -> 9 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 79097: 9 -> 4 at (2093.5, 3029.5), 2 frames after previous cover
- f104: ref 79103: 11 -> 6 at (2126, 3022.5), 2 frames after previous cover
- f106: ref 78897: 10 -> 14 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 14 -> 5 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79097: 4 -> 10 at (2082.5, 3028.5), 1 frames after previous cover
- f107: ref 79045: 5 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 9 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79102: 8 -> 9 at (2101.5, 3029.5), 2 frames after previous cover
- f108: ref 79105: 6 -> 8 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 79037: 5 -> 15 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 3 -> 5 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 11 -> 8 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 14 -> 15 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 13 -> 14 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 15 -> 5 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 5 -> 3 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 13 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 4 -> 10 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 9 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 78897: 15 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 14 -> 13 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 5 -> 15 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 3 -> 5 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 13 -> 10 at (2052, 3030), 1 frames after previous cover
- f112: ref 78899: 13 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 10 -> 13 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79103: 6 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 8 -> 6 at (2091.5, 3025.5), 4 frames after previous cover
- f113: ref 78897: 14 -> 13 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79097: 13 -> 10 at (2040.5, 3031), 1 frames after previous cover
- f113: ref 79098: 10 -> 4 at (2054, 3030), 1 frames after previous cover
- ... 376 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 949 | 49 | 1 (949) |
| 78896 | 350 (76..429) | 322 | 24 | 2 (322) |
| 78969 | 352 (80..434) | 325 | 20 | 12 (308), 3 (15), 2 (2) |
| 78971 | 352 (84..439) | 319 | 24 | 5 (281), 3 (36), 10 (2) |
| 79045 | 355 (84..443) | 318 | 24 | 3 (167), 22 (107), 5 (39), 4 (4), 12 (1) |
| 79037 | 355 (86..445) | 318 | 28 | 22 (178), 3 (115), 15 (10), 5 (5), 14 (3), 4 (2), 9 (2), 10 (2), 6 (1) |
| 78897 | 345 (89..450) | 314 | 27 | 15 (270), 4 (18), 14 (6), 10 (5), 3 (4), 22 (4), 6 (3), 19 (2), 9 (1), 13 (1) |
| 78899 | 365 (91..455) | 333 | 27 | 4 (276), 15 (20), 19 (13), 14 (10), 13 (8), 6 (2), 9 (2), 3 (2) |
| 79097 | 366 (94..461) | 342 | 22 | 19 (291), 4 (20), 10 (6), 13 (6), 14 (6), 15 (6), 6 (3), 8 (2), 9 (2) |
| 79098 | 360 (97..467) | 342 | 16 | 8 (295), 4 (15), 19 (14), 10 (5), 14 (5), 9 (4), 13 (2), 6 (1), 11 (1) |
| 79102 | 371 (98..477) | 347 | 23 | 14 (302), 8 (12), 4 (9), 10 (8), 9 (7), 13 (5), 6 (3), 11 (1) |
| 79103 | 380 (99..481) | 353 | 25 | 6 (298), 10 (24), 14 (19), 9 (9), 11 (2), 8 (1) |
| 79105 | 379 (101..484) | 356 | 18 | 10 (318), 9 (20), 6 (9), 8 (9) |
| 79108 | 385 (104..492) | 354 | 23 | 9 (312), 8 (20), 6 (13), 11 (4), 13 (3), 18 (1), 10 (1) |
| 79110 | 388 (106..497) | 360 | 26 | 23 (165), 20 (105), 18 (48), 13 (17), 6 (7), 9 (7), 11 (6), 8 (5) |
| 79111 | 386 (109..500) | 353 | 27 | 20 (230), 23 (58), 18 (41), 6 (13), 13 (5), 16 (3), 11 (3) |
| 79115 | 421 (111..531) | 397 | 17 | 11 (205), 18 (71), 23 (50), 27 (35), 20 (14), 13 (11), 6 (6), 16 (4), 17 (1) |
| 79116 | 411 (114..530) | 378 | 24 | 18 (190), 23 (62), 27 (45), 13 (34), 11 (33), 24 (6), 17 (4), 16 (2), 6 (2) |
| 79122 | 404 (118..532) | 373 | 24 | 27 (223), 11 (69), 13 (43), 18 (14), 23 (11), 16 (7), 6 (4), 17 (2) |
| 79132 | 391 (120..515) | 358 | 30 | 13 (237), 11 (73), 27 (30), 16 (6), 18 (6), 17 (3), 24 (3) |
| 79128 | 402 (124..527) | 381 | 19 | 24 (349), 16 (12), 11 (7), 18 (5), 17 (3), 21 (3), 13 (2) |
| 79134 | 407 (127..533) | 385 | 22 | 21 (246), 16 (89), 17 (49), 27 (1) |
| 79135 | 409 (129..542) | 376 | 24 | 16 (215), 21 (85), 26 (69), 24 (4), 17 (3) |
| 79139 | 406 (132..537) | 374 | 28 | 17 (296), 21 (55), 26 (12), 16 (11) |
| 79136 | 393 (136..538) | 363 | 24 | 26 (280), 16 (56), 17 (22), 24 (4), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/410/1004; tracks with internal gaps: 25; total internal gaps: 624; longest internal gap: 10; tracks ending in coasting: 24 (trailing rows total 682)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 949 | 55 | 49 | 3 | 0 | 78911 |
| 2 | 78..458 | 381 | 381 | 324 | 57 | 23 | 4 | 29 | 78896, 78969 |
| 3 | 82..474 | 393 | 393 | 339 | 54 | 22 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 4 | 86..484 | 399 | 399 | 344 | 55 | 24 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..468 | 383 | 383 | 325 | 58 | 23 | 3 | 29 | 78971, 79037, 79045 |
| 6 | 88..510 | 423 | 423 | 365 | 58 | 24 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 8 | 96..496 | 401 | 401 | 344 | 57 | 23 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 9 | 96..521 | 426 | 426 | 366 | 60 | 27 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 97..513 | 417 | 417 | 371 | 46 | 16 | 2 | 29 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 99..559 | 461 | 461 | 404 | 57 | 22 | 3 | 29 | 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 12 | 102..463 | 362 | 362 | 309 | 53 | 19 | 3 | 29 | 78969, 79045 |
| 13 | 102..543 | 442 | 442 | 374 | 68 | 36 | 10 | 16 | 78897, 78899, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 103..506 | 404 | 404 | 351 | 53 | 22 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 15 | 109..478 | 370 | 370 | 306 | 64 | 34 | 3 | 28 | 78897, 78899, 79037, 79097 |
| 16 | 110..564 | 455 | 455 | 405 | 50 | 20 | 2 | 27 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 113..562 | 450 | 450 | 383 | 67 | 32 | 3 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 117..561 | 445 | 445 | 376 | 69 | 32 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 120..490 | 371 | 371 | 320 | 51 | 20 | 2 | 29 | 78897, 78899, 79097, 79098 |
| 20 | 120..529 | 410 | 410 | 349 | 61 | 26 | 3 | 29 | 79110, 79111, 79115 |
| 21 | 127..567 | 441 | 441 | 390 | 51 | 20 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 22 | 127..472 | 346 | 346 | 289 | 57 | 24 | 3 | 29 | 78897, 79037, 79045 |
| 23 | 133..526 | 394 | 394 | 346 | 48 | 16 | 2 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 24 | 138..556 | 419 | 419 | 366 | 53 | 21 | 2 | 31 | 79116, 79128, 79132, 79135, 79136 |
| 26 | 145..571 | 427 | 427 | 361 | 66 | 30 | 2 | 29 | 79135, 79136, 79139 |
| 27 | 172..560 | 389 | 389 | 334 | 55 | 19 | 4 | 29 | 79115, 79116, 79122, 79132, 79134 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9390; unmatched reference entries: 752; unmatched candidate entries: 1423
- identity switches: 436; fragmentation (coverage interruptions): 615; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 6 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 6 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 5 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 6 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 6 -> 8 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 4 -> 9 at (2100, 3031), 3 frames after previous cover
- f98: ref 79098: 6 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 10 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 8 -> 4 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 6 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 9 -> 10 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79097: 4 -> 9 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 6 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 9 -> 13 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 10 -> 14 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 4 -> 9 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 79097: 9 -> 4 at (2093.5, 3029.5), 2 frames after previous cover
- f104: ref 79103: 11 -> 6 at (2126, 3022.5), 2 frames after previous cover
- f106: ref 78897: 10 -> 14 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 14 -> 5 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79097: 4 -> 10 at (2082.5, 3028.5), 1 frames after previous cover
- f107: ref 79045: 5 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 9 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79102: 8 -> 9 at (2101.5, 3029.5), 2 frames after previous cover
- f108: ref 79105: 6 -> 8 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 79037: 5 -> 15 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 3 -> 5 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 11 -> 8 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 14 -> 15 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 13 -> 14 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 15 -> 5 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 5 -> 3 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 13 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 4 -> 10 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 9 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 78897: 15 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 14 -> 13 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 5 -> 15 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 3 -> 5 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 13 -> 10 at (2052, 3030), 1 frames after previous cover
- f112: ref 78899: 13 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 10 -> 13 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79103: 6 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 8 -> 6 at (2091.5, 3025.5), 4 frames after previous cover
- f113: ref 78897: 14 -> 13 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79097: 13 -> 10 at (2040.5, 3031), 1 frames after previous cover
- f113: ref 79098: 10 -> 4 at (2054, 3030), 1 frames after previous cover
- ... 376 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 949 | 49 | 1 (949) |
| 78896 | 350 (76..429) | 322 | 24 | 2 (322) |
| 78969 | 352 (80..434) | 325 | 20 | 12 (308), 3 (15), 2 (2) |
| 78971 | 352 (84..439) | 319 | 24 | 5 (281), 3 (36), 10 (2) |
| 79045 | 355 (84..443) | 318 | 24 | 3 (167), 22 (107), 5 (39), 4 (4), 12 (1) |
| 79037 | 355 (86..445) | 318 | 28 | 22 (178), 3 (115), 15 (10), 5 (5), 14 (3), 4 (2), 9 (2), 10 (2), 6 (1) |
| 78897 | 345 (89..450) | 314 | 27 | 15 (270), 4 (18), 14 (6), 10 (5), 3 (4), 22 (4), 6 (3), 19 (2), 9 (1), 13 (1) |
| 78899 | 365 (91..455) | 333 | 27 | 4 (276), 15 (20), 19 (13), 14 (10), 13 (8), 6 (2), 9 (2), 3 (2) |
| 79097 | 366 (94..461) | 342 | 22 | 19 (291), 4 (20), 10 (6), 13 (6), 14 (6), 15 (6), 6 (3), 8 (2), 9 (2) |
| 79098 | 360 (97..467) | 342 | 16 | 8 (295), 4 (15), 19 (14), 10 (5), 14 (5), 9 (4), 13 (2), 6 (1), 11 (1) |
| 79102 | 371 (98..477) | 347 | 23 | 14 (302), 8 (12), 4 (9), 10 (8), 9 (7), 13 (5), 6 (3), 11 (1) |
| 79103 | 380 (99..481) | 353 | 25 | 6 (298), 10 (24), 14 (19), 9 (9), 11 (2), 8 (1) |
| 79105 | 379 (101..484) | 356 | 18 | 10 (318), 9 (20), 6 (9), 8 (9) |
| 79108 | 385 (104..492) | 354 | 23 | 9 (312), 8 (20), 6 (13), 11 (4), 13 (3), 18 (1), 10 (1) |
| 79110 | 388 (106..497) | 360 | 26 | 23 (165), 20 (105), 18 (48), 13 (17), 6 (7), 9 (7), 11 (6), 8 (5) |
| 79111 | 386 (109..500) | 353 | 27 | 20 (230), 23 (58), 18 (41), 6 (13), 13 (5), 16 (3), 11 (3) |
| 79115 | 421 (111..531) | 397 | 17 | 11 (205), 18 (71), 23 (50), 27 (35), 20 (14), 13 (11), 6 (6), 16 (4), 17 (1) |
| 79116 | 411 (114..530) | 378 | 24 | 18 (190), 23 (62), 27 (45), 13 (34), 11 (33), 24 (6), 17 (4), 16 (2), 6 (2) |
| 79122 | 404 (118..532) | 373 | 24 | 27 (223), 11 (69), 13 (43), 18 (14), 23 (11), 16 (7), 6 (4), 17 (2) |
| 79132 | 391 (120..515) | 358 | 30 | 13 (237), 11 (73), 27 (30), 16 (6), 18 (6), 17 (3), 24 (3) |
| 79128 | 402 (124..527) | 381 | 19 | 24 (349), 16 (12), 11 (7), 18 (5), 17 (3), 21 (3), 13 (2) |
| 79134 | 407 (127..533) | 385 | 22 | 21 (246), 16 (89), 17 (49), 27 (1) |
| 79135 | 409 (129..542) | 376 | 24 | 16 (215), 21 (85), 26 (69), 24 (4), 17 (3) |
| 79139 | 406 (132..537) | 374 | 28 | 17 (296), 21 (55), 26 (12), 16 (11) |
| 79136 | 393 (136..538) | 363 | 24 | 26 (280), 16 (56), 17 (22), 24 (4), 21 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/410/1004; tracks with internal gaps: 25; total internal gaps: 624; longest internal gap: 10; tracks ending in coasting: 24 (trailing rows total 682)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 949 | 55 | 49 | 3 | 0 | 78911 |
| 2 | 78..458 | 381 | 381 | 324 | 57 | 23 | 4 | 29 | 78896, 78969 |
| 3 | 82..474 | 393 | 393 | 339 | 54 | 22 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 4 | 86..484 | 399 | 399 | 344 | 55 | 24 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..468 | 383 | 383 | 325 | 58 | 23 | 3 | 29 | 78971, 79037, 79045 |
| 6 | 88..510 | 423 | 423 | 365 | 58 | 24 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 8 | 96..496 | 401 | 401 | 344 | 57 | 23 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 9 | 96..521 | 426 | 426 | 366 | 60 | 27 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 97..513 | 417 | 417 | 371 | 46 | 16 | 2 | 29 | 78897, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 99..559 | 461 | 461 | 404 | 57 | 22 | 3 | 29 | 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 12 | 102..463 | 362 | 362 | 309 | 53 | 19 | 3 | 29 | 78969, 79045 |
| 13 | 102..543 | 442 | 442 | 374 | 68 | 36 | 10 | 16 | 78897, 78899, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 103..506 | 404 | 404 | 351 | 53 | 22 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 15 | 109..478 | 370 | 370 | 306 | 64 | 34 | 3 | 28 | 78897, 78899, 79037, 79097 |
| 16 | 110..564 | 455 | 455 | 405 | 50 | 20 | 2 | 27 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 113..562 | 450 | 450 | 383 | 67 | 32 | 3 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 117..561 | 445 | 445 | 376 | 69 | 32 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 120..490 | 371 | 371 | 320 | 51 | 20 | 2 | 29 | 78897, 78899, 79097, 79098 |
| 20 | 120..529 | 410 | 410 | 349 | 61 | 26 | 3 | 29 | 79110, 79111, 79115 |
| 21 | 127..567 | 441 | 441 | 390 | 51 | 20 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 22 | 127..472 | 346 | 346 | 289 | 57 | 24 | 3 | 29 | 78897, 79037, 79045 |
| 23 | 133..526 | 394 | 394 | 346 | 48 | 16 | 2 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 24 | 138..556 | 419 | 419 | 366 | 53 | 21 | 2 | 31 | 79116, 79128, 79132, 79135, 79136 |
| 26 | 145..571 | 427 | 427 | 361 | 66 | 30 | 2 | 29 | 79135, 79136, 79139 |
| 27 | 172..560 | 389 | 389 | 334 | 55 | 19 | 4 | 29 | 79115, 79116, 79122, 79132, 79134 |
