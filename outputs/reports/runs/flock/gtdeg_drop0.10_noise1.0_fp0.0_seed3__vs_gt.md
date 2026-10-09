# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=8ae10b4a93d4
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise1.0_fp0.0_seed3/tracks.csv sha256=3990ff3a12b2813a
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise1.0_fp0.0_seed3.csv sha256=8ae10b4a93d4b2c6
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise1.0_fp0.0_seed3
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
| observations | none | 4 | 0.644 | 0.559 | 0.867 | 1.27 | 0.846 | 300 | 938.0 |
| observations | none | 6 | 0.693 | 0.610 | 0.868 | 1.27 | 0.848 | 300 | 931.0 |
| observations | none | 8 | 0.720 | 0.648 | 0.868 | 1.29 | 0.849 | 298 | 933.0 |
| observations | none | 12 | 0.753 | 0.700 | 0.869 | 1.43 | 0.859 | 265 | 935.0 |
| observations | ignore | 4 | 0.644 | 0.559 | 0.867 | 1.27 | 0.846 | 300 | 938.0 |
| observations | ignore | 6 | 0.693 | 0.610 | 0.868 | 1.27 | 0.848 | 300 | 931.0 |
| observations | ignore | 8 | 0.720 | 0.648 | 0.868 | 1.29 | 0.849 | 298 | 933.0 |
| observations | ignore | 12 | 0.753 | 0.700 | 0.869 | 1.43 | 0.859 | 265 | 935.0 |
| updates | none | 4 | 0.590 | 0.517 | 0.726 | 1.29 | 0.790 | 308 | 854.0 |
| updates | none | 6 | 0.659 | 0.584 | 0.786 | 1.41 | 0.818 | 312 | 578.0 |
| updates | none | 8 | 0.698 | 0.633 | 0.842 | 1.60 | 0.846 | 294 | 328.0 |
| updates | none | 12 | 0.744 | 0.696 | 0.864 | 1.85 | 0.866 | 265 | 231.0 |
| updates | ignore | 4 | 0.590 | 0.517 | 0.726 | 1.29 | 0.790 | 308 | 854.0 |
| updates | ignore | 6 | 0.659 | 0.584 | 0.786 | 1.41 | 0.818 | 312 | 578.0 |
| updates | ignore | 8 | 0.698 | 0.633 | 0.842 | 1.60 | 0.846 | 294 | 328.0 |
| updates | ignore | 12 | 0.744 | 0.696 | 0.864 | 1.85 | 0.866 | 265 | 231.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9104; unmatched reference entries: 1038; unmatched candidate entries: 7
- identity switches: 298; fragmentation (coverage interruptions): 879; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 5 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 5 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 6 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 5 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 5 -> 8 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79097: 8 -> 4 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 5 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 6 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79045: 6 -> 10 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 5 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 5 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 4 -> 13 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 79102: 8 -> 14 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 11 -> 8 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 5 -> 11 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 4 -> 14 at (2093.5, 3029.5), 4 frames after previous cover
- f104: ref 79102: 14 -> 11 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 11 -> 8 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 13 -> 6 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 6 -> 10 at (2038, 3034.5), 2 frames after previous cover
- f106: ref 79097: 14 -> 13 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 4 -> 14 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 11 -> 4 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 8 -> 11 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 10 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 3 -> 15 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 5 -> 8 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 6 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 6 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 3 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 3 -> 15 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 13 -> 9 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 14 -> 13 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79110: 5 -> 16 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 14 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 14 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 8 -> 4 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 8 -> 11 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 16 -> 8 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 5 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 10 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 9 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 13 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 10 -> 6 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 15 -> 17 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 6 -> 9 at (2040.5, 3031), 1 frames after previous cover
- ... 238 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 921 | 73 | 1 (921) |
| 78896 | 350 (76..429) | 319 | 27 | 2 (319) |
| 78969 | 352 (80..434) | 310 | 32 | 20 (279), 3 (15), 12 (14), 2 (2) |
| 78971 | 352 (84..439) | 308 | 31 | 3 (295), 6 (4), 12 (4), 10 (2), 17 (2), 15 (1) |
| 79045 | 355 (84..443) | 316 | 29 | 12 (273), 22 (10), 3 (8), 6 (7), 10 (7), 15 (5), 4 (4), 17 (2) |
| 79037 | 355 (86..445) | 308 | 37 | 22 (267), 12 (12), 6 (6), 3 (5), 10 (4), 17 (4), 5 (3), 15 (3), 4 (2), 9 (2) |
| 78897 | 345 (89..450) | 304 | 30 | 15 (249), 11 (17), 17 (11), 12 (5), 4 (4), 13 (4), 6 (4), 10 (4), 5 (3), 22 (2), 3 (1) |
| 78899 | 365 (91..455) | 323 | 38 | 11 (263), 14 (17), 15 (12), 9 (11), 10 (7), 6 (5), 17 (3), 5 (2), 4 (2), 12 (1) |
| 79097 | 366 (94..461) | 334 | 27 | 14 (286), 15 (18), 10 (6), 9 (5), 6 (5), 13 (4), 4 (3), 11 (3), 5 (2), 8 (2) |
| 79098 | 360 (97..467) | 326 | 30 | 9 (282), 14 (13), 11 (7), 15 (6), 4 (5), 10 (3), 17 (3), 8 (2), 13 (2), 6 (2), 5 (1) |
| 79102 | 371 (98..477) | 337 | 33 | 17 (296), 14 (6), 13 (6), 11 (5), 9 (5), 4 (4), 6 (4), 15 (4), 8 (3), 10 (3), 5 (1) |
| 79103 | 380 (99..481) | 349 | 29 | 6 (318), 14 (11), 11 (7), 9 (7), 5 (2), 8 (2), 13 (2) |
| 79105 | 379 (101..484) | 333 | 43 | 16 (277), 13 (20), 9 (9), 11 (7), 17 (7), 6 (5), 8 (4), 4 (3), 5 (1) |
| 79108 | 385 (104..492) | 340 | 39 | 13 (297), 16 (11), 11 (9), 23 (8), 9 (7), 5 (3), 18 (3), 8 (2) |
| 79110 | 388 (106..497) | 353 | 34 | 23 (306), 13 (13), 16 (12), 18 (10), 4 (4), 8 (3), 5 (2), 11 (2), 10 (1) |
| 79111 | 386 (109..500) | 350 | 30 | 21 (298), 10 (15), 4 (13), 23 (9), 8 (6), 18 (4), 5 (2), 16 (2), 13 (1) |
| 79115 | 421 (111..531) | 386 | 30 | 27 (274), 4 (67), 21 (15), 8 (8), 23 (7), 16 (6), 10 (6), 5 (3) |
| 79116 | 411 (114..530) | 371 | 34 | 4 (285), 27 (54), 16 (11), 21 (8), 5 (6), 18 (3), 10 (2), 8 (1), 23 (1) |
| 79122 | 404 (118..532) | 367 | 30 | 10 (331), 18 (19), 16 (7), 5 (6), 21 (2), 19 (1), 4 (1) |
| 79132 | 391 (120..515) | 344 | 40 | 18 (320), 19 (7), 16 (6), 8 (4), 5 (3), 21 (3), 24 (1) |
| 79128 | 402 (124..527) | 378 | 21 | 24 (346), 8 (14), 19 (11), 5 (4), 21 (3) |
| 79134 | 407 (127..533) | 365 | 39 | 19 (340), 5 (11), 8 (7), 21 (5), 24 (2) |
| 79135 | 409 (129..542) | 349 | 51 | 8 (328), 5 (9), 19 (7), 21 (5) |
| 79139 | 406 (132..537) | 360 | 39 | 5 (326), 26 (14), 24 (11), 19 (9) |
| 79136 | 393 (136..538) | 353 | 33 | 26 (336), 5 (13), 24 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 315/374/1004; tracks with internal gaps: 1; total internal gaps: 5; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 921 | 921 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 78..429 | 352 | 321 | 321 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 3 | 82..439 | 358 | 324 | 324 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 4 | 86..530 | 445 | 404 | 397 | 7 | 5 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79105, 79110, 79111, 79115, 79116, 79122 |
| 5 | 86..537 | 452 | 403 | 403 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 6 | 88..481 | 394 | 360 | 360 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 96..542 | 447 | 386 | 386 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 9 | 96..467 | 372 | 328 | 328 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 10 | 97..532 | 436 | 391 | 391 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122 |
| 11 | 99..455 | 357 | 320 | 320 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 102..443 | 342 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 13 | 102..492 | 391 | 349 | 349 | 0 | 0 | 0 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 103..461 | 359 | 333 | 333 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103 |
| 15 | 109..449 | 341 | 298 | 298 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 16 | 110..484 | 375 | 332 | 332 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 113..477 | 365 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79105 |
| 18 | 117..514 | 398 | 359 | 359 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79116, 79122, 79132 |
| 19 | 120..533 | 414 | 375 | 375 | 0 | 0 | 0 | 0 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 120..434 | 315 | 279 | 279 | 0 | 0 | 0 | 0 | 78969 |
| 21 | 127..500 | 374 | 339 | 339 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 22 | 127..445 | 319 | 279 | 279 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 23 | 133..497 | 365 | 331 | 331 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116 |
| 24 | 138..527 | 390 | 364 | 364 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 26 | 145..538 | 394 | 350 | 350 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 27 | 172..531 | 360 | 328 | 328 | 0 | 0 | 0 | 0 | 79115, 79116 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9104; unmatched reference entries: 1038; unmatched candidate entries: 7
- identity switches: 298; fragmentation (coverage interruptions): 879; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 5 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 5 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 6 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 5 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 5 -> 8 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79097: 8 -> 4 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 5 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 6 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79045: 6 -> 10 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 5 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 5 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 4 -> 13 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 79102: 8 -> 14 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 11 -> 8 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 5 -> 11 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 4 -> 14 at (2093.5, 3029.5), 4 frames after previous cover
- f104: ref 79102: 14 -> 11 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 11 -> 8 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 13 -> 6 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 6 -> 10 at (2038, 3034.5), 2 frames after previous cover
- f106: ref 79097: 14 -> 13 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 4 -> 14 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 11 -> 4 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 8 -> 11 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 10 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 3 -> 15 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 5 -> 8 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 6 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 6 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 3 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 3 -> 15 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 13 -> 9 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 14 -> 13 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79110: 5 -> 16 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 14 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 14 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 8 -> 4 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 8 -> 11 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 16 -> 8 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 5 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 10 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 9 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 13 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 10 -> 6 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 15 -> 17 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 6 -> 9 at (2040.5, 3031), 1 frames after previous cover
- ... 238 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 921 | 73 | 1 (921) |
| 78896 | 350 (76..429) | 319 | 27 | 2 (319) |
| 78969 | 352 (80..434) | 310 | 32 | 20 (279), 3 (15), 12 (14), 2 (2) |
| 78971 | 352 (84..439) | 308 | 31 | 3 (295), 6 (4), 12 (4), 10 (2), 17 (2), 15 (1) |
| 79045 | 355 (84..443) | 316 | 29 | 12 (273), 22 (10), 3 (8), 6 (7), 10 (7), 15 (5), 4 (4), 17 (2) |
| 79037 | 355 (86..445) | 308 | 37 | 22 (267), 12 (12), 6 (6), 3 (5), 10 (4), 17 (4), 5 (3), 15 (3), 4 (2), 9 (2) |
| 78897 | 345 (89..450) | 304 | 30 | 15 (249), 11 (17), 17 (11), 12 (5), 4 (4), 13 (4), 6 (4), 10 (4), 5 (3), 22 (2), 3 (1) |
| 78899 | 365 (91..455) | 323 | 38 | 11 (263), 14 (17), 15 (12), 9 (11), 10 (7), 6 (5), 17 (3), 5 (2), 4 (2), 12 (1) |
| 79097 | 366 (94..461) | 334 | 27 | 14 (286), 15 (18), 10 (6), 9 (5), 6 (5), 13 (4), 4 (3), 11 (3), 5 (2), 8 (2) |
| 79098 | 360 (97..467) | 326 | 30 | 9 (282), 14 (13), 11 (7), 15 (6), 4 (5), 10 (3), 17 (3), 8 (2), 13 (2), 6 (2), 5 (1) |
| 79102 | 371 (98..477) | 337 | 33 | 17 (296), 14 (6), 13 (6), 11 (5), 9 (5), 4 (4), 6 (4), 15 (4), 8 (3), 10 (3), 5 (1) |
| 79103 | 380 (99..481) | 349 | 29 | 6 (318), 14 (11), 11 (7), 9 (7), 5 (2), 8 (2), 13 (2) |
| 79105 | 379 (101..484) | 333 | 43 | 16 (277), 13 (20), 9 (9), 11 (7), 17 (7), 6 (5), 8 (4), 4 (3), 5 (1) |
| 79108 | 385 (104..492) | 340 | 39 | 13 (297), 16 (11), 11 (9), 23 (8), 9 (7), 5 (3), 18 (3), 8 (2) |
| 79110 | 388 (106..497) | 353 | 34 | 23 (306), 13 (13), 16 (12), 18 (10), 4 (4), 8 (3), 5 (2), 11 (2), 10 (1) |
| 79111 | 386 (109..500) | 350 | 30 | 21 (298), 10 (15), 4 (13), 23 (9), 8 (6), 18 (4), 5 (2), 16 (2), 13 (1) |
| 79115 | 421 (111..531) | 386 | 30 | 27 (274), 4 (67), 21 (15), 8 (8), 23 (7), 16 (6), 10 (6), 5 (3) |
| 79116 | 411 (114..530) | 371 | 34 | 4 (285), 27 (54), 16 (11), 21 (8), 5 (6), 18 (3), 10 (2), 8 (1), 23 (1) |
| 79122 | 404 (118..532) | 367 | 30 | 10 (331), 18 (19), 16 (7), 5 (6), 21 (2), 19 (1), 4 (1) |
| 79132 | 391 (120..515) | 344 | 40 | 18 (320), 19 (7), 16 (6), 8 (4), 5 (3), 21 (3), 24 (1) |
| 79128 | 402 (124..527) | 378 | 21 | 24 (346), 8 (14), 19 (11), 5 (4), 21 (3) |
| 79134 | 407 (127..533) | 365 | 39 | 19 (340), 5 (11), 8 (7), 21 (5), 24 (2) |
| 79135 | 409 (129..542) | 349 | 51 | 8 (328), 5 (9), 19 (7), 21 (5) |
| 79139 | 406 (132..537) | 360 | 39 | 5 (326), 26 (14), 24 (11), 19 (9) |
| 79136 | 393 (136..538) | 353 | 33 | 26 (336), 5 (13), 24 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 315/374/1004; tracks with internal gaps: 1; total internal gaps: 5; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 921 | 921 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 78..429 | 352 | 321 | 321 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 3 | 82..439 | 358 | 324 | 324 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 4 | 86..530 | 445 | 404 | 397 | 7 | 5 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79105, 79110, 79111, 79115, 79116, 79122 |
| 5 | 86..537 | 452 | 403 | 403 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 6 | 88..481 | 394 | 360 | 360 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 96..542 | 447 | 386 | 386 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 9 | 96..467 | 372 | 328 | 328 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 10 | 97..532 | 436 | 391 | 391 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122 |
| 11 | 99..455 | 357 | 320 | 320 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 102..443 | 342 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 13 | 102..492 | 391 | 349 | 349 | 0 | 0 | 0 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 103..461 | 359 | 333 | 333 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103 |
| 15 | 109..449 | 341 | 298 | 298 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 16 | 110..484 | 375 | 332 | 332 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 113..477 | 365 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79105 |
| 18 | 117..514 | 398 | 359 | 359 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79116, 79122, 79132 |
| 19 | 120..533 | 414 | 375 | 375 | 0 | 0 | 0 | 0 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 120..434 | 315 | 279 | 279 | 0 | 0 | 0 | 0 | 78969 |
| 21 | 127..500 | 374 | 339 | 339 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 22 | 127..445 | 319 | 279 | 279 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 23 | 133..497 | 365 | 331 | 331 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116 |
| 24 | 138..527 | 390 | 364 | 364 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 26 | 145..538 | 394 | 350 | 350 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 27 | 172..531 | 360 | 328 | 328 | 0 | 0 | 0 | 0 | 79115, 79116 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9824; unmatched reference entries: 318; unmatched candidate entries: 991
- identity switches: 294; fragmentation (coverage interruptions): 227; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 5 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 5 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 6 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 5 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 5 -> 8 at (2135, 3028), 1 frames after previous cover
- f98: ref 79097: 8 -> 4 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 5 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 6 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 6 -> 10 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 5 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 5 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 4 -> 13 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 79102: 8 -> 14 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 11 -> 8 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 5 -> 11 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 4 -> 14 at (2093.5, 3029.5), 4 frames after previous cover
- f104: ref 79102: 14 -> 11 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 11 -> 8 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 13 -> 6 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 6 -> 10 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79097: 14 -> 13 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 4 -> 14 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 11 -> 4 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 8 -> 11 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 10 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 3 -> 15 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 5 -> 8 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 6 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 6 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 3 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 3 -> 15 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 13 -> 9 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 14 -> 13 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79110: 5 -> 16 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 14 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 14 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 8 -> 4 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 8 -> 11 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 16 -> 8 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 5 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 10 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 9 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 13 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 10 -> 6 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 15 -> 17 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 6 -> 9 at (2040.5, 3031), 1 frames after previous cover
- ... 234 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 6 | 1 (996) |
| 78896 | 350 (76..429) | 339 | 8 | 2 (339) |
| 78969 | 352 (80..434) | 332 | 12 | 20 (301), 3 (15), 12 (14), 2 (2) |
| 78971 | 352 (84..439) | 327 | 13 | 3 (314), 6 (4), 12 (4), 10 (2), 17 (2), 15 (1) |
| 79045 | 355 (84..443) | 338 | 9 | 12 (295), 22 (10), 3 (8), 6 (7), 10 (7), 15 (5), 4 (4), 17 (2) |
| 79037 | 355 (86..445) | 334 | 14 | 22 (291), 12 (12), 6 (7), 3 (5), 10 (4), 17 (4), 5 (3), 9 (3), 15 (3), 4 (2) |
| 78897 | 345 (89..450) | 329 | 9 | 15 (271), 11 (17), 17 (13), 10 (5), 12 (5), 4 (4), 13 (4), 6 (4), 5 (3), 22 (2), 3 (1) |
| 78899 | 365 (91..455) | 354 | 9 | 11 (292), 14 (18), 15 (13), 9 (11), 10 (7), 6 (5), 17 (3), 5 (2), 4 (2), 12 (1) |
| 79097 | 366 (94..461) | 350 | 14 | 14 (302), 15 (18), 10 (6), 9 (5), 6 (5), 13 (4), 5 (3), 4 (3), 11 (3), 8 (1) |
| 79098 | 360 (97..467) | 350 | 9 | 9 (305), 14 (13), 11 (7), 15 (6), 4 (5), 17 (4), 10 (3), 8 (2), 13 (2), 6 (2), 5 (1) |
| 79102 | 371 (98..477) | 362 | 9 | 17 (318), 14 (6), 13 (6), 6 (6), 11 (5), 15 (5), 9 (5), 4 (4), 8 (3), 10 (3), 5 (1) |
| 79103 | 380 (99..481) | 371 | 9 | 6 (339), 14 (11), 9 (8), 11 (7), 5 (2), 8 (2), 13 (2) |
| 79105 | 379 (101..484) | 371 | 7 | 16 (311), 13 (22), 9 (10), 11 (8), 17 (7), 6 (5), 8 (4), 4 (3), 5 (1) |
| 79108 | 385 (104..492) | 370 | 12 | 13 (325), 16 (11), 11 (10), 23 (9), 9 (7), 5 (3), 18 (3), 8 (2) |
| 79110 | 388 (106..497) | 385 | 3 | 23 (336), 13 (13), 16 (12), 18 (11), 4 (5), 8 (3), 5 (2), 11 (2), 10 (1) |
| 79111 | 386 (109..500) | 371 | 11 | 21 (317), 10 (16), 4 (13), 23 (9), 8 (6), 18 (4), 16 (3), 5 (2), 13 (1) |
| 79115 | 421 (111..531) | 411 | 7 | 27 (286), 4 (78), 21 (17), 8 (8), 23 (7), 16 (6), 10 (6), 5 (3) |
| 79116 | 411 (114..530) | 401 | 6 | 4 (298), 27 (70), 16 (12), 21 (8), 5 (6), 8 (2), 18 (2), 10 (2), 23 (1) |
| 79122 | 404 (118..532) | 393 | 9 | 10 (356), 18 (18), 5 (7), 16 (7), 21 (3), 19 (1), 4 (1) |
| 79132 | 391 (120..515) | 376 | 11 | 18 (350), 19 (7), 16 (6), 8 (5), 5 (3), 21 (3), 24 (1), 10 (1) |
| 79128 | 402 (124..527) | 397 | 4 | 24 (364), 8 (14), 19 (11), 5 (5), 21 (3) |
| 79134 | 407 (127..533) | 398 | 8 | 19 (371), 5 (12), 8 (8), 21 (5), 24 (2) |
| 79135 | 409 (129..542) | 394 | 10 | 8 (370), 5 (9), 19 (8), 21 (7) |
| 79139 | 406 (132..537) | 394 | 10 | 5 (368), 24 (14), 19 (10), 8 (2) |
| 79136 | 393 (136..538) | 381 | 8 | 26 (375), 24 (6) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 344/403/1004; tracks with internal gaps: 25; total internal gaps: 252; longest internal gap: 9; tracks ending in coasting: 24 (trailing rows total 685)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 996 | 8 | 6 | 2 | 0 | 78911 |
| 2 | 78..458 | 381 | 381 | 341 | 40 | 7 | 4 | 29 | 78896, 78969 |
| 3 | 82..468 | 387 | 387 | 343 | 44 | 12 | 3 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 4 | 86..559 | 474 | 474 | 422 | 52 | 16 | 4 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79105, 79110, 79111, 79115, 79116, 79122 |
| 5 | 86..566 | 481 | 481 | 436 | 45 | 11 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 6 | 88..510 | 423 | 423 | 384 | 39 | 8 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 96..571 | 476 | 476 | 432 | 44 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79139 |
| 9 | 96..496 | 401 | 401 | 354 | 47 | 15 | 2 | 29 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 10 | 97..561 | 465 | 465 | 419 | 46 | 17 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122, 79132 |
| 11 | 99..484 | 386 | 386 | 351 | 35 | 6 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 102..472 | 371 | 371 | 331 | 40 | 10 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 13 | 102..521 | 420 | 420 | 379 | 41 | 12 | 1 | 29 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 103..490 | 388 | 388 | 350 | 38 | 9 | 1 | 29 | 78899, 79097, 79098, 79102, 79103 |
| 15 | 109..478 | 370 | 370 | 322 | 48 | 19 | 2 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 16 | 110..513 | 404 | 404 | 368 | 36 | 7 | 1 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 113..506 | 394 | 394 | 353 | 41 | 12 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79105 |
| 18 | 117..543 | 427 | 427 | 388 | 39 | 10 | 2 | 28 | 79108, 79110, 79111, 79116, 79122, 79132 |
| 19 | 120..562 | 443 | 443 | 408 | 35 | 5 | 2 | 29 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 120..463 | 344 | 344 | 301 | 43 | 10 | 3 | 29 | 78969 |
| 21 | 127..529 | 403 | 403 | 363 | 40 | 9 | 2 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 22 | 127..474 | 348 | 348 | 303 | 45 | 11 | 2 | 29 | 78897, 79037, 79045 |
| 23 | 133..526 | 394 | 394 | 362 | 32 | 3 | 1 | 29 | 79108, 79110, 79111, 79115, 79116 |
| 24 | 138..556 | 419 | 419 | 387 | 32 | 6 | 9 | 18 | 79128, 79132, 79134, 79136, 79139 |
| 26 | 145..567 | 423 | 423 | 375 | 48 | 14 | 2 | 31 | 79136 |
| 27 | 172..560 | 389 | 389 | 356 | 33 | 4 | 1 | 29 | 79115, 79116 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9824; unmatched reference entries: 318; unmatched candidate entries: 991
- identity switches: 294; fragmentation (coverage interruptions): 227; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 5 -> 4 at (2135, 3035.5), 2 frames after previous cover
- f92: ref 78897: 5 -> 4 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 4 -> 6 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78969: 3 -> 2 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 2 -> 3 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 5 -> 4 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 4 -> 9 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 3 -> 10 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 5 -> 8 at (2135, 3028), 1 frames after previous cover
- f98: ref 79097: 8 -> 4 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 5 -> 8 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 4 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78971: 10 -> 3 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 9 -> 6 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 6 -> 10 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 8 -> 11 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 5 -> 8 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 11 -> 8 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 8 -> 11 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 79098: 8 -> 4 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 11 -> 8 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 5 -> 11 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78897: 4 -> 13 at (2077, 3031.5), 7 frames after previous cover
- f102: ref 78969: 3 -> 12 at (2021, 3032), 4 frames after previous cover
- f103: ref 79102: 8 -> 14 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 11 -> 8 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 5 -> 11 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 4 -> 14 at (2093.5, 3029.5), 4 frames after previous cover
- f104: ref 79102: 14 -> 11 at (2119, 3027), 1 frames after previous cover
- f105: ref 79105: 11 -> 8 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 13 -> 6 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79037: 6 -> 10 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79097: 14 -> 13 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 4 -> 14 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 11 -> 4 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 8 -> 11 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 79045: 10 -> 3 at (2019, 3033.5), 2 frames after previous cover
- f109: ref 78971: 3 -> 15 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79108: 5 -> 8 at (2125, 3025), 2 frames after previous cover
- f110: ref 78897: 6 -> 10 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 6 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 10 -> 3 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 3 -> 15 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 13 -> 9 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 14 -> 13 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79110: 5 -> 16 at (2134, 3026), 2 frames after previous cover
- f111: ref 79102: 14 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 14 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 8 -> 4 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 8 -> 11 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 16 -> 8 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 5 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 10 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 9 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 13 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f113: ref 78899: 10 -> 6 at (2025, 3032), 1 frames after previous cover
- f113: ref 78971: 15 -> 17 at (1971.5, 3035), 4 frames after previous cover
- f113: ref 79097: 6 -> 9 at (2040.5, 3031), 1 frames after previous cover
- ... 234 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 6 | 1 (996) |
| 78896 | 350 (76..429) | 339 | 8 | 2 (339) |
| 78969 | 352 (80..434) | 332 | 12 | 20 (301), 3 (15), 12 (14), 2 (2) |
| 78971 | 352 (84..439) | 327 | 13 | 3 (314), 6 (4), 12 (4), 10 (2), 17 (2), 15 (1) |
| 79045 | 355 (84..443) | 338 | 9 | 12 (295), 22 (10), 3 (8), 6 (7), 10 (7), 15 (5), 4 (4), 17 (2) |
| 79037 | 355 (86..445) | 334 | 14 | 22 (291), 12 (12), 6 (7), 3 (5), 10 (4), 17 (4), 5 (3), 9 (3), 15 (3), 4 (2) |
| 78897 | 345 (89..450) | 329 | 9 | 15 (271), 11 (17), 17 (13), 10 (5), 12 (5), 4 (4), 13 (4), 6 (4), 5 (3), 22 (2), 3 (1) |
| 78899 | 365 (91..455) | 354 | 9 | 11 (292), 14 (18), 15 (13), 9 (11), 10 (7), 6 (5), 17 (3), 5 (2), 4 (2), 12 (1) |
| 79097 | 366 (94..461) | 350 | 14 | 14 (302), 15 (18), 10 (6), 9 (5), 6 (5), 13 (4), 5 (3), 4 (3), 11 (3), 8 (1) |
| 79098 | 360 (97..467) | 350 | 9 | 9 (305), 14 (13), 11 (7), 15 (6), 4 (5), 17 (4), 10 (3), 8 (2), 13 (2), 6 (2), 5 (1) |
| 79102 | 371 (98..477) | 362 | 9 | 17 (318), 14 (6), 13 (6), 6 (6), 11 (5), 15 (5), 9 (5), 4 (4), 8 (3), 10 (3), 5 (1) |
| 79103 | 380 (99..481) | 371 | 9 | 6 (339), 14 (11), 9 (8), 11 (7), 5 (2), 8 (2), 13 (2) |
| 79105 | 379 (101..484) | 371 | 7 | 16 (311), 13 (22), 9 (10), 11 (8), 17 (7), 6 (5), 8 (4), 4 (3), 5 (1) |
| 79108 | 385 (104..492) | 370 | 12 | 13 (325), 16 (11), 11 (10), 23 (9), 9 (7), 5 (3), 18 (3), 8 (2) |
| 79110 | 388 (106..497) | 385 | 3 | 23 (336), 13 (13), 16 (12), 18 (11), 4 (5), 8 (3), 5 (2), 11 (2), 10 (1) |
| 79111 | 386 (109..500) | 371 | 11 | 21 (317), 10 (16), 4 (13), 23 (9), 8 (6), 18 (4), 16 (3), 5 (2), 13 (1) |
| 79115 | 421 (111..531) | 411 | 7 | 27 (286), 4 (78), 21 (17), 8 (8), 23 (7), 16 (6), 10 (6), 5 (3) |
| 79116 | 411 (114..530) | 401 | 6 | 4 (298), 27 (70), 16 (12), 21 (8), 5 (6), 8 (2), 18 (2), 10 (2), 23 (1) |
| 79122 | 404 (118..532) | 393 | 9 | 10 (356), 18 (18), 5 (7), 16 (7), 21 (3), 19 (1), 4 (1) |
| 79132 | 391 (120..515) | 376 | 11 | 18 (350), 19 (7), 16 (6), 8 (5), 5 (3), 21 (3), 24 (1), 10 (1) |
| 79128 | 402 (124..527) | 397 | 4 | 24 (364), 8 (14), 19 (11), 5 (5), 21 (3) |
| 79134 | 407 (127..533) | 398 | 8 | 19 (371), 5 (12), 8 (8), 21 (5), 24 (2) |
| 79135 | 409 (129..542) | 394 | 10 | 8 (370), 5 (9), 19 (8), 21 (7) |
| 79139 | 406 (132..537) | 394 | 10 | 5 (368), 24 (14), 19 (10), 8 (2) |
| 79136 | 393 (136..538) | 381 | 8 | 26 (375), 24 (6) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 344/403/1004; tracks with internal gaps: 25; total internal gaps: 252; longest internal gap: 9; tracks ending in coasting: 24 (trailing rows total 685)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 996 | 8 | 6 | 2 | 0 | 78911 |
| 2 | 78..458 | 381 | 381 | 341 | 40 | 7 | 4 | 29 | 78896, 78969 |
| 3 | 82..468 | 387 | 387 | 343 | 44 | 12 | 3 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 4 | 86..559 | 474 | 474 | 422 | 52 | 16 | 4 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79105, 79110, 79111, 79115, 79116, 79122 |
| 5 | 86..566 | 481 | 481 | 436 | 45 | 11 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 6 | 88..510 | 423 | 423 | 384 | 39 | 8 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 8 | 96..571 | 476 | 476 | 432 | 44 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79139 |
| 9 | 96..496 | 401 | 401 | 354 | 47 | 15 | 2 | 29 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 10 | 97..561 | 465 | 465 | 419 | 46 | 17 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122, 79132 |
| 11 | 99..484 | 386 | 386 | 351 | 35 | 6 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 102..472 | 371 | 371 | 331 | 40 | 10 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 13 | 102..521 | 420 | 420 | 379 | 41 | 12 | 1 | 29 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 103..490 | 388 | 388 | 350 | 38 | 9 | 1 | 29 | 78899, 79097, 79098, 79102, 79103 |
| 15 | 109..478 | 370 | 370 | 322 | 48 | 19 | 2 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 16 | 110..513 | 404 | 404 | 368 | 36 | 7 | 1 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 113..506 | 394 | 394 | 353 | 41 | 12 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79105 |
| 18 | 117..543 | 427 | 427 | 388 | 39 | 10 | 2 | 28 | 79108, 79110, 79111, 79116, 79122, 79132 |
| 19 | 120..562 | 443 | 443 | 408 | 35 | 5 | 2 | 29 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 120..463 | 344 | 344 | 301 | 43 | 10 | 3 | 29 | 78969 |
| 21 | 127..529 | 403 | 403 | 363 | 40 | 9 | 2 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 22 | 127..474 | 348 | 348 | 303 | 45 | 11 | 2 | 29 | 78897, 79037, 79045 |
| 23 | 133..526 | 394 | 394 | 362 | 32 | 3 | 1 | 29 | 79108, 79110, 79111, 79115, 79116 |
| 24 | 138..556 | 419 | 419 | 387 | 32 | 6 | 9 | 18 | 79128, 79132, 79134, 79136, 79139 |
| 26 | 145..567 | 423 | 423 | 375 | 48 | 14 | 2 | 31 | 79136 |
| 27 | 172..560 | 389 | 389 | 356 | 33 | 4 | 1 | 29 | 79115, 79116 |
