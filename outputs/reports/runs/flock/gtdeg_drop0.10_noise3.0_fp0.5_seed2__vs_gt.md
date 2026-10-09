# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=f4b8a5e0a2a7
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise3.0_fp0.5_seed2/tracks.csv sha256=db8aa425beb6dbeb
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise3.0_fp0.5_seed2.csv sha256=f4b8a5e0a2a706da
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise3.0_fp0.5_seed2
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
| observations | none | 4 | 0.216 | 0.120 | 0.089 | 2.42 | 0.256 | 500 | 2505.0 |
| observations | none | 6 | 0.301 | 0.165 | 0.582 | 3.23 | 0.380 | 588 | 1814.0 |
| observations | none | 8 | 0.347 | 0.192 | 0.766 | 3.64 | 0.430 | 604 | 1196.0 |
| observations | none | 12 | 0.390 | 0.220 | 0.820 | 3.94 | 0.465 | 534 | 999.0 |
| observations | ignore | 4 | 0.216 | 0.120 | 0.089 | 2.42 | 0.256 | 500 | 2505.0 |
| observations | ignore | 6 | 0.301 | 0.165 | 0.582 | 3.23 | 0.380 | 588 | 1814.0 |
| observations | ignore | 8 | 0.347 | 0.192 | 0.766 | 3.64 | 0.430 | 604 | 1196.0 |
| observations | ignore | 12 | 0.390 | 0.220 | 0.820 | 3.94 | 0.465 | 534 | 999.0 |
| updates | none | 4 | 0.206 | 0.118 | -0.070 | 2.43 | 0.242 | 548 | 2481.0 |
| updates | none | 6 | 0.293 | 0.166 | 0.461 | 3.26 | 0.365 | 618 | 1581.0 |
| updates | none | 8 | 0.342 | 0.196 | 0.683 | 3.73 | 0.421 | 608 | 768.0 |
| updates | none | 12 | 0.390 | 0.227 | 0.786 | 4.16 | 0.465 | 503 | 374.0 |
| updates | ignore | 4 | 0.206 | 0.118 | -0.070 | 2.43 | 0.242 | 548 | 2481.0 |
| updates | ignore | 6 | 0.293 | 0.166 | 0.461 | 3.26 | 0.365 | 618 | 1581.0 |
| updates | ignore | 8 | 0.342 | 0.196 | 0.683 | 3.73 | 0.421 | 608 | 768.0 |
| updates | ignore | 12 | 0.390 | 0.227 | 0.786 | 4.16 | 0.465 | 503 | 374.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8712; unmatched reference entries: 1430; unmatched candidate entries: 338
- identity switches: 604; fragmentation (coverage interruptions): 1152; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 36 -> 47 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 47 -> 50 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 36 -> 52 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 35 -> 47 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 47 -> 35 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 52 -> 42 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 42 -> 56 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 55 -> 57 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 52 -> 42 at (2107.5, 3023.5), 2 frames after previous cover
- f109: ref 79108: 55 -> 52 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 50 -> 35 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 35 -> 50 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 43 -> 50 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78969: 39 -> 31 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 47 -> 39 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 50 -> 47 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 56 -> 54 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 42 -> 56 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 42 -> 60 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 52 -> 42 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 57 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 55 -> 57 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 50 -> 43 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 43 -> 51 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 31 -> 39 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 39 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 35 -> 50 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 47 -> 35 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 56 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 56 -> 42 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 42 -> 52 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 52 -> 57 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 52 -> 60 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 57 -> 52 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79115: 55 -> 57 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 36 -> 63 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 60 -> 42 at (2073, 3025), 3 frames after previous cover
- f115: ref 79108: 60 -> 36 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 52 -> 60 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 57 -> 52 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 43 -> 50 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 78899: 51 -> 43 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 54 -> 51 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 56 -> 54 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 42 -> 56 at (2049.5, 3030.5), 3 frames after previous cover
- f118: ref 78971: 47 -> 35 at (1940.5, 3036), 1 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 3 frames after previous cover
- ... 544 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 887 | 102 | 3 (887) |
| 78896 | 350 (76..429) | 302 | 38 | 70 (145), 76 (108), 31 (49) |
| 78969 | 352 (80..434) | 289 | 48 | 76 (134), 31 (121), 39 (32), 79 (2) |
| 78971 | 352 (84..439) | 308 | 34 | 39 (86), 139 (77), 35 (48), 79 (39), 31 (33), 47 (13), 50 (10), 76 (2) |
| 79045 | 355 (84..443) | 294 | 43 | 79 (79), 50 (71), 139 (57), 39 (36), 35 (31), 31 (9), 47 (8), 36 (2), 76 (1) |
| 79037 | 355 (86..445) | 297 | 48 | 31 (97), 72 (71), 79 (52), 50 (43), 139 (17), 39 (7), 43 (3), 35 (3), 47 (2), 36 (1), 42 (1) |
| 78897 | 345 (89..450) | 304 | 33 | 50 (80), 79 (74), 72 (59), 35 (55), 43 (22), 47 (4), 39 (4), 42 (3), 36 (2), 31 (1) |
| 78899 | 365 (91..455) | 315 | 43 | 39 (139), 50 (102), 72 (32), 51 (16), 43 (13), 36 (3), 42 (3), 35 (3), 79 (2), 47 (1), 31 (1) |
| 79097 | 366 (94..461) | 314 | 42 | 123 (133), 43 (107), 39 (26), 54 (18), 47 (11), 51 (6), 72 (6), 36 (3), 42 (2), 50 (1), 79 (1) |
| 79098 | 360 (97..467) | 303 | 49 | 43 (170), 47 (75), 72 (28), 56 (9), 54 (8), 42 (5), 51 (3), 123 (3), 36 (1), 50 (1) |
| 79102 | 371 (98..477) | 310 | 46 | 155 (123), 72 (77), 123 (38), 47 (36), 54 (14), 42 (6), 56 (6), 43 (5), 52 (4), 36 (1) |
| 79103 | 380 (99..481) | 334 | 43 | 54 (229), 47 (32), 155 (24), 36 (14), 123 (12), 63 (8), 72 (8), 56 (4), 51 (3) |
| 79105 | 379 (101..484) | 320 | 46 | 47 (150), 51 (82), 54 (28), 123 (25), 42 (10), 81 (6), 155 (6), 52 (4), 56 (4), 60 (2), 36 (1), 63 (1), +1 more |
| 79108 | 385 (104..492) | 344 | 35 | 81 (134), 56 (69), 51 (53), 54 (29), 42 (18), 47 (17), 36 (11), 60 (4), 52 (3), 63 (2), 55 (1), 68 (1), +2 more |
| 79110 | 388 (106..497) | 325 | 47 | 42 (204), 68 (37), 56 (29), 81 (24), 51 (9), 60 (7), 57 (5), 52 (4), 36 (4), 55 (1), 123 (1) |
| 79111 | 386 (109..500) | 328 | 43 | 60 (152), 81 (87), 42 (39), 68 (19), 63 (11), 51 (5), 52 (4), 56 (4), 55 (3), 57 (3), 36 (1) |
| 79115 | 421 (111..531) | 349 | 53 | 138 (116), 57 (84), 63 (46), 81 (30), 42 (28), 60 (16), 51 (10), 68 (6), 56 (6), 36 (4), 55 (3) |
| 79116 | 411 (114..530) | 362 | 44 | 57 (103), 51 (85), 56 (51), 42 (32), 36 (20), 63 (17), 68 (17), 60 (16), 81 (12), 52 (5), 55 (4) |
| 79122 | 404 (118..532) | 339 | 51 | 51 (97), 138 (80), 57 (62), 36 (26), 56 (25), 63 (14), 68 (13), 60 (11), 55 (7), 52 (3), 66 (1) |
| 79132 | 391 (120..515) | 337 | 44 | 57 (109), 60 (79), 56 (63), 68 (33), 81 (24), 36 (13), 52 (7), 66 (4), 55 (3), 63 (1), 72 (1) |
| 79128 | 402 (124..527) | 349 | 44 | 68 (114), 56 (93), 60 (33), 63 (30), 36 (25), 138 (20), 52 (19), 55 (6), 57 (6), 66 (3) |
| 79134 | 407 (127..533) | 353 | 43 | 63 (157), 55 (52), 36 (51), 68 (48), 60 (20), 57 (14), 66 (7), 52 (4) |
| 79135 | 409 (129..542) | 350 | 50 | 36 (155), 63 (76), 75 (61), 66 (26), 55 (8), 138 (8), 52 (8), 68 (7), 57 (1) |
| 79139 | 406 (132..537) | 363 | 35 | 52 (172), 66 (91), 68 (58), 36 (34), 63 (7), 75 (1) |
| 79136 | 393 (136..538) | 336 | 48 | 52 (147), 159 (93), 66 (46), 75 (29), 36 (17), 63 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 105/368/1003; tracks with internal gaps: 29; total internal gaps: 305; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 14)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 914 | 887 | 27 | 25 | 2 | 0 | 78911 |
| 31 | 78..434 | 357 | 317 | 311 | 6 | 6 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 35 | 86..252 | 167 | 145 | 140 | 5 | 3 | 1 | 2 | 78897, 78899, 78971, 79037, 79045 |
| 36 | 86..533 | 448 | 406 | 389 | 17 | 16 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 39 | 88..455 | 368 | 341 | 330 | 11 | 11 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 42 | 90..493 | 404 | 364 | 351 | 13 | 13 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116 |
| 43 | 91..467 | 377 | 334 | 320 | 14 | 13 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 47 | 95..489 | 395 | 363 | 349 | 14 | 14 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 50 | 98..449 | 352 | 321 | 308 | 13 | 13 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 100..530 | 431 | 384 | 369 | 15 | 14 | 2 | 0 | 78899, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 100..538 | 439 | 398 | 384 | 14 | 13 | 2 | 0 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 101..472 | 372 | 339 | 326 | 13 | 12 | 1 | 1 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 105..209 | 105 | 90 | 88 | 2 | 0 | 0 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 106..527 | 422 | 377 | 363 | 14 | 13 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 57 | 108..532 | 425 | 394 | 387 | 7 | 6 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 60 | 111..513 | 403 | 355 | 340 | 15 | 13 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 115..542 | 428 | 390 | 374 | 16 | 14 | 2 | 0 | 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 122..320 | 199 | 183 | 178 | 5 | 3 | 1 | 2 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 126..537 | 412 | 368 | 353 | 15 | 14 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 127..299 | 173 | 151 | 145 | 6 | 4 | 1 | 2 | 78896 |
| 72 | 132..515 | 384 | 298 | 284 | 14 | 14 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79132 |
| 75 | 135..246 | 112 | 98 | 91 | 7 | 4 | 2 | 2 | 79135, 79136, 79139 |
| 76 | 136..429 | 294 | 258 | 245 | 13 | 12 | 2 | 0 | 78896, 78969, 78971, 79045 |
| 79 | 142..439 | 298 | 263 | 249 | 14 | 14 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 81 | 144..500 | 357 | 325 | 317 | 8 | 7 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 123 | 235..497 | 263 | 224 | 213 | 11 | 10 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 138 | 267..528 | 262 | 231 | 224 | 7 | 6 | 1 | 1 | 79115, 79122, 79128, 79135 |
| 139 | 267..443 | 177 | 155 | 151 | 4 | 3 | 2 | 0 | 78971, 79037, 79045 |
| 155 | 306..484 | 179 | 161 | 153 | 8 | 7 | 2 | 0 | 79102, 79103, 79105 |
| 159 | 322..452 | 131 | 103 | 93 | 10 | 8 | 1 | 2 | 79136 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8712; unmatched reference entries: 1430; unmatched candidate entries: 338
- identity switches: 604; fragmentation (coverage interruptions): 1152; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 36 -> 47 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 47 -> 50 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 36 -> 52 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 35 -> 47 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 47 -> 35 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 52 -> 42 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 42 -> 56 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 55 -> 57 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 52 -> 42 at (2107.5, 3023.5), 2 frames after previous cover
- f109: ref 79108: 55 -> 52 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 50 -> 35 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 35 -> 50 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 43 -> 50 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78969: 39 -> 31 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 47 -> 39 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 50 -> 47 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 56 -> 54 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 42 -> 56 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 42 -> 60 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 52 -> 42 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 57 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 55 -> 57 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 50 -> 43 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 43 -> 51 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 31 -> 39 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 39 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 35 -> 50 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 47 -> 35 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 56 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 56 -> 42 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 42 -> 52 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 52 -> 57 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 52 -> 60 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 57 -> 52 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79115: 55 -> 57 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 36 -> 63 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 60 -> 42 at (2073, 3025), 3 frames after previous cover
- f115: ref 79108: 60 -> 36 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 52 -> 60 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 57 -> 52 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 43 -> 50 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 78899: 51 -> 43 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 54 -> 51 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 56 -> 54 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 42 -> 56 at (2049.5, 3030.5), 3 frames after previous cover
- f118: ref 78971: 47 -> 35 at (1940.5, 3036), 1 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 3 frames after previous cover
- ... 544 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 887 | 102 | 3 (887) |
| 78896 | 350 (76..429) | 302 | 38 | 70 (145), 76 (108), 31 (49) |
| 78969 | 352 (80..434) | 289 | 48 | 76 (134), 31 (121), 39 (32), 79 (2) |
| 78971 | 352 (84..439) | 308 | 34 | 39 (86), 139 (77), 35 (48), 79 (39), 31 (33), 47 (13), 50 (10), 76 (2) |
| 79045 | 355 (84..443) | 294 | 43 | 79 (79), 50 (71), 139 (57), 39 (36), 35 (31), 31 (9), 47 (8), 36 (2), 76 (1) |
| 79037 | 355 (86..445) | 297 | 48 | 31 (97), 72 (71), 79 (52), 50 (43), 139 (17), 39 (7), 43 (3), 35 (3), 47 (2), 36 (1), 42 (1) |
| 78897 | 345 (89..450) | 304 | 33 | 50 (80), 79 (74), 72 (59), 35 (55), 43 (22), 47 (4), 39 (4), 42 (3), 36 (2), 31 (1) |
| 78899 | 365 (91..455) | 315 | 43 | 39 (139), 50 (102), 72 (32), 51 (16), 43 (13), 36 (3), 42 (3), 35 (3), 79 (2), 47 (1), 31 (1) |
| 79097 | 366 (94..461) | 314 | 42 | 123 (133), 43 (107), 39 (26), 54 (18), 47 (11), 51 (6), 72 (6), 36 (3), 42 (2), 50 (1), 79 (1) |
| 79098 | 360 (97..467) | 303 | 49 | 43 (170), 47 (75), 72 (28), 56 (9), 54 (8), 42 (5), 51 (3), 123 (3), 36 (1), 50 (1) |
| 79102 | 371 (98..477) | 310 | 46 | 155 (123), 72 (77), 123 (38), 47 (36), 54 (14), 42 (6), 56 (6), 43 (5), 52 (4), 36 (1) |
| 79103 | 380 (99..481) | 334 | 43 | 54 (229), 47 (32), 155 (24), 36 (14), 123 (12), 63 (8), 72 (8), 56 (4), 51 (3) |
| 79105 | 379 (101..484) | 320 | 46 | 47 (150), 51 (82), 54 (28), 123 (25), 42 (10), 81 (6), 155 (6), 52 (4), 56 (4), 60 (2), 36 (1), 63 (1), +1 more |
| 79108 | 385 (104..492) | 344 | 35 | 81 (134), 56 (69), 51 (53), 54 (29), 42 (18), 47 (17), 36 (11), 60 (4), 52 (3), 63 (2), 55 (1), 68 (1), +2 more |
| 79110 | 388 (106..497) | 325 | 47 | 42 (204), 68 (37), 56 (29), 81 (24), 51 (9), 60 (7), 57 (5), 52 (4), 36 (4), 55 (1), 123 (1) |
| 79111 | 386 (109..500) | 328 | 43 | 60 (152), 81 (87), 42 (39), 68 (19), 63 (11), 51 (5), 52 (4), 56 (4), 55 (3), 57 (3), 36 (1) |
| 79115 | 421 (111..531) | 349 | 53 | 138 (116), 57 (84), 63 (46), 81 (30), 42 (28), 60 (16), 51 (10), 68 (6), 56 (6), 36 (4), 55 (3) |
| 79116 | 411 (114..530) | 362 | 44 | 57 (103), 51 (85), 56 (51), 42 (32), 36 (20), 63 (17), 68 (17), 60 (16), 81 (12), 52 (5), 55 (4) |
| 79122 | 404 (118..532) | 339 | 51 | 51 (97), 138 (80), 57 (62), 36 (26), 56 (25), 63 (14), 68 (13), 60 (11), 55 (7), 52 (3), 66 (1) |
| 79132 | 391 (120..515) | 337 | 44 | 57 (109), 60 (79), 56 (63), 68 (33), 81 (24), 36 (13), 52 (7), 66 (4), 55 (3), 63 (1), 72 (1) |
| 79128 | 402 (124..527) | 349 | 44 | 68 (114), 56 (93), 60 (33), 63 (30), 36 (25), 138 (20), 52 (19), 55 (6), 57 (6), 66 (3) |
| 79134 | 407 (127..533) | 353 | 43 | 63 (157), 55 (52), 36 (51), 68 (48), 60 (20), 57 (14), 66 (7), 52 (4) |
| 79135 | 409 (129..542) | 350 | 50 | 36 (155), 63 (76), 75 (61), 66 (26), 55 (8), 138 (8), 52 (8), 68 (7), 57 (1) |
| 79139 | 406 (132..537) | 363 | 35 | 52 (172), 66 (91), 68 (58), 36 (34), 63 (7), 75 (1) |
| 79136 | 393 (136..538) | 336 | 48 | 52 (147), 159 (93), 66 (46), 75 (29), 36 (17), 63 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 105/368/1003; tracks with internal gaps: 29; total internal gaps: 305; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 14)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 914 | 887 | 27 | 25 | 2 | 0 | 78911 |
| 31 | 78..434 | 357 | 317 | 311 | 6 | 6 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 35 | 86..252 | 167 | 145 | 140 | 5 | 3 | 1 | 2 | 78897, 78899, 78971, 79037, 79045 |
| 36 | 86..533 | 448 | 406 | 389 | 17 | 16 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 39 | 88..455 | 368 | 341 | 330 | 11 | 11 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 42 | 90..493 | 404 | 364 | 351 | 13 | 13 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116 |
| 43 | 91..467 | 377 | 334 | 320 | 14 | 13 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 47 | 95..489 | 395 | 363 | 349 | 14 | 14 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 50 | 98..449 | 352 | 321 | 308 | 13 | 13 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 100..530 | 431 | 384 | 369 | 15 | 14 | 2 | 0 | 78899, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 100..538 | 439 | 398 | 384 | 14 | 13 | 2 | 0 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 101..472 | 372 | 339 | 326 | 13 | 12 | 1 | 1 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 105..209 | 105 | 90 | 88 | 2 | 0 | 0 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 106..527 | 422 | 377 | 363 | 14 | 13 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 57 | 108..532 | 425 | 394 | 387 | 7 | 6 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 60 | 111..513 | 403 | 355 | 340 | 15 | 13 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 115..542 | 428 | 390 | 374 | 16 | 14 | 2 | 0 | 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 122..320 | 199 | 183 | 178 | 5 | 3 | 1 | 2 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 126..537 | 412 | 368 | 353 | 15 | 14 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 127..299 | 173 | 151 | 145 | 6 | 4 | 1 | 2 | 78896 |
| 72 | 132..515 | 384 | 298 | 284 | 14 | 14 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79132 |
| 75 | 135..246 | 112 | 98 | 91 | 7 | 4 | 2 | 2 | 79135, 79136, 79139 |
| 76 | 136..429 | 294 | 258 | 245 | 13 | 12 | 2 | 0 | 78896, 78969, 78971, 79045 |
| 79 | 142..439 | 298 | 263 | 249 | 14 | 14 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 81 | 144..500 | 357 | 325 | 317 | 8 | 7 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 123 | 235..497 | 263 | 224 | 213 | 11 | 10 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 138 | 267..528 | 262 | 231 | 224 | 7 | 6 | 1 | 1 | 79115, 79122, 79128, 79135 |
| 139 | 267..443 | 177 | 155 | 151 | 4 | 3 | 2 | 0 | 78971, 79037, 79045 |
| 155 | 306..484 | 179 | 161 | 153 | 8 | 7 | 2 | 0 | 79102, 79103, 79105 |
| 159 | 322..452 | 131 | 103 | 93 | 10 | 8 | 1 | 2 | 79136 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 9259; unmatched reference entries: 883; unmatched candidate entries: 1719
- identity switches: 608; fragmentation (coverage interruptions): 681; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 36 -> 47 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 47 -> 50 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 36 -> 52 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 35 -> 47 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 47 -> 35 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 52 -> 42 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 42 -> 56 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 55 -> 57 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 52 -> 42 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 55 -> 52 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 50 -> 35 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 35 -> 50 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 43 -> 50 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 39 -> 31 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 47 -> 39 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 50 -> 47 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 56 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 42 -> 56 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 42 -> 60 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 52 -> 42 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 57 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 55 -> 57 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 50 -> 43 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 43 -> 51 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 31 -> 39 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 39 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 35 -> 50 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 47 -> 35 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 56 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 56 -> 42 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 42 -> 52 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 52 -> 57 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 52 -> 60 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 57 -> 52 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79105: 60 -> 42 at (2079, 3025), 2 frames after previous cover
- f114: ref 79115: 55 -> 57 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 36 -> 63 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79108: 60 -> 36 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 52 -> 60 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 57 -> 52 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 43 -> 50 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 51 -> 43 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 54 -> 51 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 56 -> 54 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 42 -> 56 at (2049.5, 3030.5), 3 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 43 -> 51 at (1988.5, 3032), 1 frames after previous cover
- ... 548 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 960 | 37 | 3 (960) |
| 78896 | 350 (76..429) | 317 | 26 | 70 (151), 76 (116), 31 (50) |
| 78969 | 352 (80..434) | 309 | 31 | 76 (143), 31 (132), 39 (32), 79 (2) |
| 78971 | 352 (84..439) | 322 | 23 | 39 (87), 139 (79), 35 (50), 79 (42), 31 (36), 47 (15), 50 (11), 76 (2) |
| 79045 | 355 (84..443) | 309 | 31 | 79 (83), 50 (77), 139 (60), 39 (37), 35 (31), 31 (10), 47 (8), 36 (2), 76 (1) |
| 79037 | 355 (86..445) | 314 | 35 | 31 (101), 72 (75), 79 (54), 50 (45), 139 (22), 39 (7), 43 (3), 35 (3), 47 (2), 36 (1), 42 (1) |
| 78897 | 345 (89..450) | 312 | 28 | 50 (82), 79 (75), 72 (60), 35 (55), 43 (23), 47 (4), 31 (4), 39 (4), 42 (3), 36 (2) |
| 78899 | 365 (91..455) | 334 | 26 | 39 (148), 50 (107), 72 (33), 51 (17), 43 (14), 36 (3), 42 (3), 35 (3), 31 (3), 79 (2), 47 (1) |
| 79097 | 366 (94..461) | 332 | 25 | 123 (139), 43 (112), 39 (30), 54 (18), 47 (11), 72 (9), 51 (6), 36 (3), 42 (2), 50 (1), 79 (1) |
| 79098 | 360 (97..467) | 327 | 27 | 43 (183), 47 (80), 72 (33), 56 (10), 54 (8), 42 (5), 51 (3), 123 (3), 36 (1), 50 (1) |
| 79102 | 371 (98..477) | 325 | 33 | 155 (129), 72 (82), 123 (41), 47 (37), 54 (14), 42 (6), 56 (6), 43 (5), 52 (4), 36 (1) |
| 79103 | 380 (99..481) | 360 | 19 | 54 (246), 47 (34), 155 (25), 36 (15), 123 (13), 72 (10), 63 (9), 56 (5), 51 (3) |
| 79105 | 379 (101..484) | 345 | 26 | 47 (160), 51 (89), 54 (29), 123 (27), 42 (11), 81 (6), 155 (6), 52 (5), 56 (5), 72 (3), 60 (2), 36 (1), +1 more |
| 79108 | 385 (104..492) | 362 | 18 | 81 (142), 56 (73), 51 (56), 54 (31), 47 (19), 42 (18), 36 (11), 60 (4), 52 (3), 63 (2), 55 (1), 68 (1), +1 more |
| 79110 | 388 (106..497) | 354 | 26 | 42 (221), 68 (42), 56 (33), 81 (24), 51 (9), 60 (8), 57 (5), 52 (4), 36 (4), 47 (2), 55 (1), 123 (1) |
| 79111 | 386 (109..500) | 346 | 32 | 60 (158), 81 (93), 42 (42), 68 (20), 63 (12), 51 (6), 52 (5), 55 (3), 57 (3), 56 (3), 36 (1) |
| 79115 | 421 (111..531) | 377 | 28 | 138 (129), 57 (88), 63 (48), 81 (31), 42 (29), 60 (25), 51 (10), 68 (8), 36 (5), 55 (3), 56 (1) |
| 79116 | 411 (114..530) | 379 | 27 | 57 (107), 51 (90), 56 (58), 42 (35), 36 (20), 63 (18), 68 (17), 81 (13), 60 (11), 55 (5), 52 (5) |
| 79122 | 404 (118..532) | 364 | 28 | 51 (109), 138 (85), 57 (63), 36 (27), 56 (27), 63 (14), 68 (14), 60 (13), 55 (7), 52 (3), 66 (1), 42 (1) |
| 79132 | 391 (120..515) | 356 | 26 | 57 (114), 60 (85), 56 (65), 68 (34), 81 (26), 36 (17), 52 (7), 66 (4), 55 (3), 63 (1) |
| 79128 | 402 (124..527) | 372 | 23 | 68 (123), 56 (97), 60 (37), 63 (31), 36 (25), 52 (22), 138 (21), 55 (7), 57 (6), 66 (3) |
| 79134 | 407 (127..533) | 380 | 22 | 63 (168), 55 (56), 36 (56), 68 (53), 60 (21), 57 (14), 66 (7), 52 (5) |
| 79135 | 409 (129..542) | 372 | 30 | 36 (163), 63 (85), 75 (65), 66 (27), 55 (8), 138 (8), 52 (8), 68 (7), 57 (1) |
| 79139 | 406 (132..537) | 376 | 22 | 52 (182), 66 (93), 68 (59), 36 (34), 63 (7), 75 (1) |
| 79136 | 393 (136..538) | 355 | 32 | 52 (155), 159 (99), 66 (49), 75 (30), 36 (19), 63 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 134/397/1003; tracks with internal gaps: 30; total internal gaps: 634; longest internal gap: 14; tracks ending in coasting: 29 (trailing rows total 892)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 1003 | 960 | 43 | 37 | 3 | 0 | 78911 |
| 31 | 78..463 | 386 | 386 | 336 | 50 | 25 | 13 | 8 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 35 | 86..281 | 196 | 196 | 142 | 54 | 14 | 2 | 38 | 78897, 78899, 78971, 79037, 79045 |
| 36 | 86..562 | 477 | 477 | 411 | 66 | 29 | 4 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 39 | 88..484 | 397 | 397 | 345 | 52 | 20 | 2 | 31 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 42 | 90..522 | 433 | 433 | 377 | 56 | 20 | 6 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 43 | 91..496 | 406 | 406 | 340 | 66 | 27 | 2 | 32 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 47 | 95..518 | 424 | 424 | 373 | 51 | 25 | 3 | 22 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 50 | 98..478 | 381 | 381 | 324 | 57 | 24 | 2 | 31 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 100..559 | 460 | 460 | 398 | 62 | 25 | 3 | 29 | 78899, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 100..567 | 468 | 468 | 408 | 60 | 26 | 4 | 29 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 101..501 | 401 | 401 | 346 | 55 | 22 | 2 | 30 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 105..238 | 134 | 134 | 94 | 40 | 4 | 2 | 34 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 106..556 | 451 | 451 | 383 | 68 | 32 | 3 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 57 | 108..561 | 454 | 454 | 401 | 53 | 15 | 6 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 60 | 111..542 | 432 | 432 | 364 | 68 | 29 | 6 | 27 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 115..571 | 457 | 457 | 399 | 58 | 22 | 2 | 29 | 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 122..349 | 228 | 228 | 184 | 44 | 13 | 1 | 31 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 126..566 | 441 | 441 | 378 | 63 | 23 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 127..328 | 202 | 202 | 151 | 51 | 11 | 2 | 37 | 78896 |
| 72 | 132..544 | 413 | 413 | 306 | 107 | 33 | 7 | 52 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 75 | 135..275 | 141 | 141 | 96 | 45 | 9 | 3 | 33 | 79135, 79136, 79139 |
| 76 | 136..458 | 323 | 323 | 262 | 61 | 26 | 7 | 29 | 78896, 78969, 78971, 79045 |
| 79 | 142..468 | 327 | 327 | 259 | 68 | 31 | 5 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 81 | 144..529 | 386 | 386 | 335 | 51 | 20 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 123 | 235..526 | 292 | 292 | 224 | 68 | 19 | 14 | 29 | 79097, 79098, 79102, 79103, 79105, 79110 |
| 138 | 267..557 | 291 | 291 | 243 | 48 | 16 | 2 | 30 | 79115, 79122, 79128, 79135 |
| 139 | 267..472 | 206 | 206 | 161 | 45 | 12 | 3 | 29 | 78971, 79037, 79045 |
| 155 | 306..513 | 208 | 208 | 160 | 48 | 12 | 2 | 34 | 79102, 79103, 79105 |
| 159 | 322..481 | 160 | 160 | 99 | 61 | 13 | 2 | 46 | 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 9259; unmatched reference entries: 883; unmatched candidate entries: 1719
- identity switches: 608; fragmentation (coverage interruptions): 681; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 36 -> 42 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 36 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 36 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 47 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 36 -> 47 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 36 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 47 -> 50 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 36 -> 42 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 42 -> 51 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 36 -> 52 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 42 -> 54 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 35 -> 47 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 47 -> 35 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 52 -> 42 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 42 -> 56 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 55 -> 57 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 52 -> 42 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 55 -> 52 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 50 -> 35 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 35 -> 50 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 43 -> 50 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 51 -> 43 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 39 -> 31 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 47 -> 39 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 50 -> 47 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 54 -> 51 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 56 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 42 -> 56 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 42 -> 60 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 52 -> 42 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 57 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 55 -> 57 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 50 -> 43 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 43 -> 51 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 31 -> 39 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 39 -> 47 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 35 -> 50 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 47 -> 35 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 51 -> 54 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 56 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 56 -> 42 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 42 -> 52 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 52 -> 57 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 52 -> 60 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 57 -> 52 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79105: 60 -> 42 at (2079, 3025), 2 frames after previous cover
- f114: ref 79115: 55 -> 57 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 36 -> 63 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79108: 60 -> 36 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 52 -> 60 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 57 -> 52 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 43 -> 50 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 51 -> 43 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 54 -> 51 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 56 -> 54 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 42 -> 56 at (2049.5, 3030.5), 3 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 43 -> 51 at (1988.5, 3032), 1 frames after previous cover
- ... 548 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 960 | 37 | 3 (960) |
| 78896 | 350 (76..429) | 317 | 26 | 70 (151), 76 (116), 31 (50) |
| 78969 | 352 (80..434) | 309 | 31 | 76 (143), 31 (132), 39 (32), 79 (2) |
| 78971 | 352 (84..439) | 322 | 23 | 39 (87), 139 (79), 35 (50), 79 (42), 31 (36), 47 (15), 50 (11), 76 (2) |
| 79045 | 355 (84..443) | 309 | 31 | 79 (83), 50 (77), 139 (60), 39 (37), 35 (31), 31 (10), 47 (8), 36 (2), 76 (1) |
| 79037 | 355 (86..445) | 314 | 35 | 31 (101), 72 (75), 79 (54), 50 (45), 139 (22), 39 (7), 43 (3), 35 (3), 47 (2), 36 (1), 42 (1) |
| 78897 | 345 (89..450) | 312 | 28 | 50 (82), 79 (75), 72 (60), 35 (55), 43 (23), 47 (4), 31 (4), 39 (4), 42 (3), 36 (2) |
| 78899 | 365 (91..455) | 334 | 26 | 39 (148), 50 (107), 72 (33), 51 (17), 43 (14), 36 (3), 42 (3), 35 (3), 31 (3), 79 (2), 47 (1) |
| 79097 | 366 (94..461) | 332 | 25 | 123 (139), 43 (112), 39 (30), 54 (18), 47 (11), 72 (9), 51 (6), 36 (3), 42 (2), 50 (1), 79 (1) |
| 79098 | 360 (97..467) | 327 | 27 | 43 (183), 47 (80), 72 (33), 56 (10), 54 (8), 42 (5), 51 (3), 123 (3), 36 (1), 50 (1) |
| 79102 | 371 (98..477) | 325 | 33 | 155 (129), 72 (82), 123 (41), 47 (37), 54 (14), 42 (6), 56 (6), 43 (5), 52 (4), 36 (1) |
| 79103 | 380 (99..481) | 360 | 19 | 54 (246), 47 (34), 155 (25), 36 (15), 123 (13), 72 (10), 63 (9), 56 (5), 51 (3) |
| 79105 | 379 (101..484) | 345 | 26 | 47 (160), 51 (89), 54 (29), 123 (27), 42 (11), 81 (6), 155 (6), 52 (5), 56 (5), 72 (3), 60 (2), 36 (1), +1 more |
| 79108 | 385 (104..492) | 362 | 18 | 81 (142), 56 (73), 51 (56), 54 (31), 47 (19), 42 (18), 36 (11), 60 (4), 52 (3), 63 (2), 55 (1), 68 (1), +1 more |
| 79110 | 388 (106..497) | 354 | 26 | 42 (221), 68 (42), 56 (33), 81 (24), 51 (9), 60 (8), 57 (5), 52 (4), 36 (4), 47 (2), 55 (1), 123 (1) |
| 79111 | 386 (109..500) | 346 | 32 | 60 (158), 81 (93), 42 (42), 68 (20), 63 (12), 51 (6), 52 (5), 55 (3), 57 (3), 56 (3), 36 (1) |
| 79115 | 421 (111..531) | 377 | 28 | 138 (129), 57 (88), 63 (48), 81 (31), 42 (29), 60 (25), 51 (10), 68 (8), 36 (5), 55 (3), 56 (1) |
| 79116 | 411 (114..530) | 379 | 27 | 57 (107), 51 (90), 56 (58), 42 (35), 36 (20), 63 (18), 68 (17), 81 (13), 60 (11), 55 (5), 52 (5) |
| 79122 | 404 (118..532) | 364 | 28 | 51 (109), 138 (85), 57 (63), 36 (27), 56 (27), 63 (14), 68 (14), 60 (13), 55 (7), 52 (3), 66 (1), 42 (1) |
| 79132 | 391 (120..515) | 356 | 26 | 57 (114), 60 (85), 56 (65), 68 (34), 81 (26), 36 (17), 52 (7), 66 (4), 55 (3), 63 (1) |
| 79128 | 402 (124..527) | 372 | 23 | 68 (123), 56 (97), 60 (37), 63 (31), 36 (25), 52 (22), 138 (21), 55 (7), 57 (6), 66 (3) |
| 79134 | 407 (127..533) | 380 | 22 | 63 (168), 55 (56), 36 (56), 68 (53), 60 (21), 57 (14), 66 (7), 52 (5) |
| 79135 | 409 (129..542) | 372 | 30 | 36 (163), 63 (85), 75 (65), 66 (27), 55 (8), 138 (8), 52 (8), 68 (7), 57 (1) |
| 79139 | 406 (132..537) | 376 | 22 | 52 (182), 66 (93), 68 (59), 36 (34), 63 (7), 75 (1) |
| 79136 | 393 (136..538) | 355 | 32 | 52 (155), 159 (99), 66 (49), 75 (30), 36 (19), 63 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 134/397/1003; tracks with internal gaps: 30; total internal gaps: 634; longest internal gap: 14; tracks ending in coasting: 29 (trailing rows total 892)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 6..1008 | 1003 | 1003 | 960 | 43 | 37 | 3 | 0 | 78911 |
| 31 | 78..463 | 386 | 386 | 336 | 50 | 25 | 13 | 8 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 35 | 86..281 | 196 | 196 | 142 | 54 | 14 | 2 | 38 | 78897, 78899, 78971, 79037, 79045 |
| 36 | 86..562 | 477 | 477 | 411 | 66 | 29 | 4 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 39 | 88..484 | 397 | 397 | 345 | 52 | 20 | 2 | 31 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 42 | 90..522 | 433 | 433 | 377 | 56 | 20 | 6 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 43 | 91..496 | 406 | 406 | 340 | 66 | 27 | 2 | 32 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 47 | 95..518 | 424 | 424 | 373 | 51 | 25 | 3 | 22 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 50 | 98..478 | 381 | 381 | 324 | 57 | 24 | 2 | 31 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 100..559 | 460 | 460 | 398 | 62 | 25 | 3 | 29 | 78899, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 100..567 | 468 | 468 | 408 | 60 | 26 | 4 | 29 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 101..501 | 401 | 401 | 346 | 55 | 22 | 2 | 30 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 105..238 | 134 | 134 | 94 | 40 | 4 | 2 | 34 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 106..556 | 451 | 451 | 383 | 68 | 32 | 3 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 57 | 108..561 | 454 | 454 | 401 | 53 | 15 | 6 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 60 | 111..542 | 432 | 432 | 364 | 68 | 29 | 6 | 27 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 115..571 | 457 | 457 | 399 | 58 | 22 | 2 | 29 | 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 122..349 | 228 | 228 | 184 | 44 | 13 | 1 | 31 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 126..566 | 441 | 441 | 378 | 63 | 23 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 127..328 | 202 | 202 | 151 | 51 | 11 | 2 | 37 | 78896 |
| 72 | 132..544 | 413 | 413 | 306 | 107 | 33 | 7 | 52 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 75 | 135..275 | 141 | 141 | 96 | 45 | 9 | 3 | 33 | 79135, 79136, 79139 |
| 76 | 136..458 | 323 | 323 | 262 | 61 | 26 | 7 | 29 | 78896, 78969, 78971, 79045 |
| 79 | 142..468 | 327 | 327 | 259 | 68 | 31 | 5 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 81 | 144..529 | 386 | 386 | 335 | 51 | 20 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 123 | 235..526 | 292 | 292 | 224 | 68 | 19 | 14 | 29 | 79097, 79098, 79102, 79103, 79105, 79110 |
| 138 | 267..557 | 291 | 291 | 243 | 48 | 16 | 2 | 30 | 79115, 79122, 79128, 79135 |
| 139 | 267..472 | 206 | 206 | 161 | 45 | 12 | 3 | 29 | 78971, 79037, 79045 |
| 155 | 306..513 | 208 | 208 | 160 | 48 | 12 | 2 | 34 | 79102, 79103, 79105 |
| 159 | 322..481 | 160 | 160 | 99 | 61 | 13 | 2 | 46 | 79136 |
