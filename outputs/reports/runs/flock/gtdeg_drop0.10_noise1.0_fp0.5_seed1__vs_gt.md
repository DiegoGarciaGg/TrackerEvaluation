# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=23d5b795033e
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise1.0_fp0.5_seed1/tracks.csv sha256=9e3cc4dac8e80047
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise1.0_fp0.5_seed1.csv sha256=23d5b795033e2f5f
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise1.0_fp0.5_seed1
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
| observations | none | 4 | 0.408 | 0.227 | 0.835 | 1.26 | 0.432 | 492 | 981.0 |
| observations | none | 6 | 0.437 | 0.246 | 0.838 | 1.26 | 0.434 | 492 | 973.0 |
| observations | none | 8 | 0.456 | 0.267 | 0.837 | 1.28 | 0.440 | 484 | 975.0 |
| observations | none | 12 | 0.482 | 0.289 | 0.838 | 1.44 | 0.470 | 445 | 967.0 |
| observations | ignore | 4 | 0.408 | 0.227 | 0.835 | 1.26 | 0.432 | 492 | 981.0 |
| observations | ignore | 6 | 0.437 | 0.246 | 0.838 | 1.26 | 0.434 | 492 | 973.0 |
| observations | ignore | 8 | 0.456 | 0.267 | 0.837 | 1.28 | 0.440 | 484 | 975.0 |
| observations | ignore | 12 | 0.482 | 0.289 | 0.838 | 1.44 | 0.470 | 445 | 967.0 |
| updates | none | 4 | 0.376 | 0.218 | 0.661 | 1.28 | 0.401 | 502 | 910.0 |
| updates | none | 6 | 0.417 | 0.245 | 0.723 | 1.41 | 0.419 | 500 | 633.0 |
| updates | none | 8 | 0.443 | 0.270 | 0.776 | 1.58 | 0.436 | 483 | 401.0 |
| updates | none | 12 | 0.476 | 0.298 | 0.799 | 1.84 | 0.469 | 429 | 310.0 |
| updates | ignore | 4 | 0.376 | 0.218 | 0.661 | 1.28 | 0.401 | 502 | 910.0 |
| updates | ignore | 6 | 0.417 | 0.245 | 0.723 | 1.41 | 0.419 | 500 | 633.0 |
| updates | ignore | 8 | 0.443 | 0.270 | 0.776 | 1.58 | 0.436 | 483 | 401.0 |
| updates | ignore | 12 | 0.476 | 0.298 | 0.799 | 1.84 | 0.469 | 429 | 310.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9024; unmatched reference entries: 1118; unmatched candidate entries: 51
- identity switches: 484; fragmentation (coverage interruptions): 934; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 51 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 48 -> 46 at (2128, 3029), 2 frames after previous cover
- f96: ref 79097: 46 -> 48 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 48 -> 46 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 48 -> 46 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 46 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 55 -> 48 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 46 -> 57 at (2093, 3030.5), 6 frames after previous cover
- f103: ref 79102: 48 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 43 -> 51 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 57 -> 43 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 46 -> 57 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 58 -> 46 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 48 -> 58 at (2116.5, 3023), 3 frames after previous cover
- f106: ref 79108: 48 -> 55 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 51 -> 43 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 55 -> 62 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 43 -> 51 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 51 -> 50 at (2026, 3034), 1 frames after previous cover
- f109: ref 78971: 50 -> 38 at (1996.5, 3034.5), 2 frames after previous cover
- f112: ref 78896: 38 -> 65 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 48 -> 66 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 62 -> 46 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 55 -> 62 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 66 -> 55 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 48 -> 66 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 57 -> 54 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 46 -> 57 at (2055, 3030), 2 frames after previous cover
- f117: ref 79097: 54 -> 51 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 51 -> 50 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 66 -> 55 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 48 -> 66 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 70 -> 48 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 43 -> 51 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 51 -> 58 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 55 -> 62 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 62 -> 74 at (2053.5, 3026), 5 frames after previous cover
- f124: ref 79122: 70 -> 48 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 72 -> 70 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 48 -> 70 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 58 -> 78 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 62 -> 74 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 55 -> 62 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 66 -> 55 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 70 -> 66 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 48 -> 70 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 70 -> 48 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 78 -> 57 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 46 -> 78 at (2007, 3026), 1 frames after previous cover
- f127: ref 79108: 74 -> 46 at (2025.5, 3026), 2 frames after previous cover
- f127: ref 79128: 72 -> 48 at (2137, 3022.5), 1 frames after previous cover
- f127: ref 79132: 48 -> 70 at (2117, 3025), 1 frames after previous cover
- f128: ref 79132: 70 -> 72 at (2111, 3024), 1 frames after previous cover
- ... 424 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 908 | 88 | 0 (908) |
| 78896 | 350 (76..429) | 307 | 32 | 65 (279), 38 (28) |
| 78969 | 352 (80..434) | 315 | 28 | 41 (310), 65 (5) |
| 78971 | 352 (84..439) | 313 | 32 | 107 (131), 45 (81), 38 (69), 50 (15), 97 (11), 41 (5), 43 (1) |
| 79045 | 355 (84..443) | 312 | 34 | 45 (207), 107 (81), 213 (19), 43 (3), 41 (1), 184 (1) |
| 79037 | 355 (86..445) | 311 | 35 | 184 (83), 97 (78), 50 (74), 51 (39), 107 (26), 45 (4), 43 (3), 41 (3), 213 (1) |
| 78897 | 345 (89..450) | 304 | 36 | 50 (120), 43 (55), 97 (50), 51 (42), 45 (31), 48 (3), 107 (2), 46 (1) |
| 78899 | 365 (91..455) | 317 | 37 | 43 (83), 50 (82), 97 (63), 134 (54), 51 (26), 46 (4), 57 (4), 48 (1) |
| 79097 | 366 (94..461) | 327 | 38 | 134 (141), 43 (83), 58 (48), 50 (25), 54 (14), 51 (11), 46 (3), 48 (1), 97 (1) |
| 79098 | 360 (97..467) | 320 | 29 | 97 (71), 43 (63), 51 (61), 58 (43), 163 (26), 54 (25), 134 (12), 57 (8), 46 (7), 50 (3), 48 (1) |
| 79102 | 371 (98..477) | 315 | 40 | 163 (55), 43 (53), 58 (51), 51 (48), 83 (45), 54 (28), 57 (18), 46 (8), 87 (7), 48 (2) |
| 79103 | 380 (99..481) | 323 | 38 | 54 (98), 51 (62), 163 (61), 83 (54), 87 (27), 58 (14), 48 (3), 57 (2), 55 (1), 78 (1) |
| 79105 | 379 (101..484) | 339 | 35 | 83 (195), 87 (60), 54 (50), 46 (12), 62 (7), 57 (6), 55 (4), 78 (2), 84 (2), 72 (1) |
| 79108 | 385 (104..492) | 336 | 41 | 51 (73), 87 (62), 54 (59), 57 (50), 72 (37), 83 (24), 46 (8), 55 (7), 84 (7), 62 (4), 74 (4), 48 (1) |
| 79110 | 388 (106..497) | 352 | 32 | 72 (96), 54 (76), 57 (64), 74 (53), 87 (35), 62 (6), 84 (6), 55 (4), 48 (3), 78 (3), 46 (3), 66 (2), +1 more |
| 79111 | 386 (109..500) | 344 | 35 | 84 (91), 72 (88), 57 (64), 87 (61), 55 (12), 46 (9), 74 (6), 48 (4), 66 (4), 62 (3), 78 (2) |
| 79115 | 421 (111..531) | 383 | 32 | 84 (193), 46 (102), 55 (50), 62 (9), 66 (8), 74 (6), 48 (4), 72 (4), 57 (4), 78 (3) |
| 79116 | 411 (114..530) | 367 | 33 | 46 (183), 84 (57), 62 (49), 74 (47), 72 (12), 48 (5), 70 (3), 66 (3), 55 (3), 78 (2), 57 (2), 154 (1) |
| 79122 | 404 (118..532) | 347 | 55 | 57 (162), 46 (44), 78 (39), 62 (36), 74 (32), 55 (13), 70 (8), 84 (5), 66 (3), 72 (3), 48 (2) |
| 79132 | 391 (120..515) | 351 | 36 | 87 (99), 74 (87), 78 (59), 55 (54), 154 (25), 46 (9), 66 (6), 70 (5), 72 (3), 84 (2), 48 (1), 62 (1) |
| 79128 | 402 (124..527) | 362 | 37 | 74 (112), 55 (94), 154 (86), 66 (47), 72 (12), 82 (6), 46 (3), 48 (2) |
| 79134 | 407 (127..533) | 368 | 36 | 55 (106), 72 (87), 70 (65), 82 (63), 74 (28), 78 (11), 154 (5), 48 (3) |
| 79135 | 409 (129..542) | 376 | 29 | 82 (175), 78 (99), 70 (97), 48 (3), 55 (2) |
| 79139 | 406 (132..537) | 368 | 34 | 70 (110), 48 (107), 78 (74), 82 (46), 55 (31) |
| 79136 | 393 (136..538) | 359 | 32 | 70 (104), 82 (93), 78 (70), 48 (68), 55 (13), 62 (11) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 304 | 633..633 | 1 | 0 | 1 |
| 309 | 647..671 | 25 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 1/353/1007; tracks with internal gaps: 16; total internal gaps: 26; longest internal gap: 2; tracks ending in coasting: 10 (trailing rows total 24)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 912 | 908 | 4 | 4 | 1 | 0 | 78911 |
| 38 | 78..186 | 109 | 99 | 97 | 2 | 0 | 0 | 2 | 78896, 78971 |
| 41 | 83..434 | 352 | 319 | 319 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 43 | 86..481 | 396 | 345 | 344 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 45 | 90..450 | 361 | 324 | 323 | 1 | 1 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 46 | 90..530 | 441 | 400 | 396 | 4 | 3 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 91..368 | 278 | 218 | 214 | 4 | 0 | 0 | 4 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 93..455 | 363 | 320 | 319 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 51 | 95..492 | 398 | 362 | 362 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79108 |
| 54 | 100..497 | 398 | 350 | 350 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 55 | 100..537 | 438 | 394 | 394 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 102..532 | 431 | 385 | 384 | 1 | 1 | 1 | 0 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 58 | 103..272 | 170 | 157 | 156 | 1 | 0 | 0 | 1 | 79097, 79098, 79102, 79103 |
| 62 | 107..284 | 178 | 130 | 126 | 4 | 1 | 1 | 3 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..429 | 318 | 284 | 284 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 66 | 112..186 | 75 | 74 | 73 | 1 | 0 | 0 | 1 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 70 | 116..533 | 418 | 393 | 392 | 1 | 1 | 1 | 0 | 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 72 | 122..500 | 379 | 345 | 343 | 2 | 2 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 74 | 122..527 | 406 | 375 | 375 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 78 | 126..538 | 413 | 368 | 365 | 3 | 3 | 1 | 0 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 82 | 132..542 | 411 | 384 | 383 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 83 | 132..484 | 353 | 320 | 319 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110 |
| 84 | 132..531 | 400 | 364 | 363 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 139..515 | 377 | 352 | 351 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 97 | 151..467 | 317 | 277 | 274 | 3 | 3 | 1 | 0 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 107 | 177..439 | 263 | 240 | 240 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045 |
| 134 | 230..482 | 253 | 210 | 207 | 3 | 0 | 0 | 3 | 78899, 79097, 79098 |
| 154 | 281..431 | 151 | 122 | 117 | 5 | 0 | 0 | 5 | 79116, 79128, 79132, 79134 |
| 163 | 314..481 | 168 | 143 | 142 | 1 | 1 | 1 | 0 | 79098, 79102, 79103 |
| 184 | 354..445 | 92 | 85 | 84 | 1 | 1 | 1 | 0 | 79037, 79045 |
| 213 | 421..443 | 23 | 20 | 20 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 304 | 633..633 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 309 | 647..671 | 25 | 3 | 0 | 3 | 0 | 0 | 3 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9024; unmatched reference entries: 1118; unmatched candidate entries: 51
- identity switches: 484; fragmentation (coverage interruptions): 934; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 51 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 48 -> 46 at (2128, 3029), 2 frames after previous cover
- f96: ref 79097: 46 -> 48 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 48 -> 46 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 48 -> 46 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 46 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 55 -> 48 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 46 -> 57 at (2093, 3030.5), 6 frames after previous cover
- f103: ref 79102: 48 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 43 -> 51 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 57 -> 43 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 46 -> 57 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 58 -> 46 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 48 -> 58 at (2116.5, 3023), 3 frames after previous cover
- f106: ref 79108: 48 -> 55 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 51 -> 43 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 55 -> 62 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 43 -> 51 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 51 -> 50 at (2026, 3034), 1 frames after previous cover
- f109: ref 78971: 50 -> 38 at (1996.5, 3034.5), 2 frames after previous cover
- f112: ref 78896: 38 -> 65 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 48 -> 66 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 62 -> 46 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 55 -> 62 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 66 -> 55 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 48 -> 66 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 57 -> 54 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 46 -> 57 at (2055, 3030), 2 frames after previous cover
- f117: ref 79097: 54 -> 51 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 51 -> 50 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 66 -> 55 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 48 -> 66 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 70 -> 48 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 43 -> 51 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 51 -> 58 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 55 -> 62 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 62 -> 74 at (2053.5, 3026), 5 frames after previous cover
- f124: ref 79122: 70 -> 48 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 72 -> 70 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 48 -> 70 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 58 -> 78 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 62 -> 74 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 55 -> 62 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 66 -> 55 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 70 -> 66 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 48 -> 70 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 70 -> 48 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 78 -> 57 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 46 -> 78 at (2007, 3026), 1 frames after previous cover
- f127: ref 79108: 74 -> 46 at (2025.5, 3026), 2 frames after previous cover
- f127: ref 79128: 72 -> 48 at (2137, 3022.5), 1 frames after previous cover
- f127: ref 79132: 48 -> 70 at (2117, 3025), 1 frames after previous cover
- f128: ref 79132: 70 -> 72 at (2111, 3024), 1 frames after previous cover
- ... 424 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 908 | 88 | 0 (908) |
| 78896 | 350 (76..429) | 307 | 32 | 65 (279), 38 (28) |
| 78969 | 352 (80..434) | 315 | 28 | 41 (310), 65 (5) |
| 78971 | 352 (84..439) | 313 | 32 | 107 (131), 45 (81), 38 (69), 50 (15), 97 (11), 41 (5), 43 (1) |
| 79045 | 355 (84..443) | 312 | 34 | 45 (207), 107 (81), 213 (19), 43 (3), 41 (1), 184 (1) |
| 79037 | 355 (86..445) | 311 | 35 | 184 (83), 97 (78), 50 (74), 51 (39), 107 (26), 45 (4), 43 (3), 41 (3), 213 (1) |
| 78897 | 345 (89..450) | 304 | 36 | 50 (120), 43 (55), 97 (50), 51 (42), 45 (31), 48 (3), 107 (2), 46 (1) |
| 78899 | 365 (91..455) | 317 | 37 | 43 (83), 50 (82), 97 (63), 134 (54), 51 (26), 46 (4), 57 (4), 48 (1) |
| 79097 | 366 (94..461) | 327 | 38 | 134 (141), 43 (83), 58 (48), 50 (25), 54 (14), 51 (11), 46 (3), 48 (1), 97 (1) |
| 79098 | 360 (97..467) | 320 | 29 | 97 (71), 43 (63), 51 (61), 58 (43), 163 (26), 54 (25), 134 (12), 57 (8), 46 (7), 50 (3), 48 (1) |
| 79102 | 371 (98..477) | 315 | 40 | 163 (55), 43 (53), 58 (51), 51 (48), 83 (45), 54 (28), 57 (18), 46 (8), 87 (7), 48 (2) |
| 79103 | 380 (99..481) | 323 | 38 | 54 (98), 51 (62), 163 (61), 83 (54), 87 (27), 58 (14), 48 (3), 57 (2), 55 (1), 78 (1) |
| 79105 | 379 (101..484) | 339 | 35 | 83 (195), 87 (60), 54 (50), 46 (12), 62 (7), 57 (6), 55 (4), 78 (2), 84 (2), 72 (1) |
| 79108 | 385 (104..492) | 336 | 41 | 51 (73), 87 (62), 54 (59), 57 (50), 72 (37), 83 (24), 46 (8), 55 (7), 84 (7), 62 (4), 74 (4), 48 (1) |
| 79110 | 388 (106..497) | 352 | 32 | 72 (96), 54 (76), 57 (64), 74 (53), 87 (35), 62 (6), 84 (6), 55 (4), 48 (3), 78 (3), 46 (3), 66 (2), +1 more |
| 79111 | 386 (109..500) | 344 | 35 | 84 (91), 72 (88), 57 (64), 87 (61), 55 (12), 46 (9), 74 (6), 48 (4), 66 (4), 62 (3), 78 (2) |
| 79115 | 421 (111..531) | 383 | 32 | 84 (193), 46 (102), 55 (50), 62 (9), 66 (8), 74 (6), 48 (4), 72 (4), 57 (4), 78 (3) |
| 79116 | 411 (114..530) | 367 | 33 | 46 (183), 84 (57), 62 (49), 74 (47), 72 (12), 48 (5), 70 (3), 66 (3), 55 (3), 78 (2), 57 (2), 154 (1) |
| 79122 | 404 (118..532) | 347 | 55 | 57 (162), 46 (44), 78 (39), 62 (36), 74 (32), 55 (13), 70 (8), 84 (5), 66 (3), 72 (3), 48 (2) |
| 79132 | 391 (120..515) | 351 | 36 | 87 (99), 74 (87), 78 (59), 55 (54), 154 (25), 46 (9), 66 (6), 70 (5), 72 (3), 84 (2), 48 (1), 62 (1) |
| 79128 | 402 (124..527) | 362 | 37 | 74 (112), 55 (94), 154 (86), 66 (47), 72 (12), 82 (6), 46 (3), 48 (2) |
| 79134 | 407 (127..533) | 368 | 36 | 55 (106), 72 (87), 70 (65), 82 (63), 74 (28), 78 (11), 154 (5), 48 (3) |
| 79135 | 409 (129..542) | 376 | 29 | 82 (175), 78 (99), 70 (97), 48 (3), 55 (2) |
| 79139 | 406 (132..537) | 368 | 34 | 70 (110), 48 (107), 78 (74), 82 (46), 55 (31) |
| 79136 | 393 (136..538) | 359 | 32 | 70 (104), 82 (93), 78 (70), 48 (68), 55 (13), 62 (11) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 304 | 633..633 | 1 | 0 | 1 |
| 309 | 647..671 | 25 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 1/353/1007; tracks with internal gaps: 16; total internal gaps: 26; longest internal gap: 2; tracks ending in coasting: 10 (trailing rows total 24)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 912 | 908 | 4 | 4 | 1 | 0 | 78911 |
| 38 | 78..186 | 109 | 99 | 97 | 2 | 0 | 0 | 2 | 78896, 78971 |
| 41 | 83..434 | 352 | 319 | 319 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 43 | 86..481 | 396 | 345 | 344 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 45 | 90..450 | 361 | 324 | 323 | 1 | 1 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 46 | 90..530 | 441 | 400 | 396 | 4 | 3 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 91..368 | 278 | 218 | 214 | 4 | 0 | 0 | 4 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 93..455 | 363 | 320 | 319 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 51 | 95..492 | 398 | 362 | 362 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79108 |
| 54 | 100..497 | 398 | 350 | 350 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 55 | 100..537 | 438 | 394 | 394 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 102..532 | 431 | 385 | 384 | 1 | 1 | 1 | 0 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 58 | 103..272 | 170 | 157 | 156 | 1 | 0 | 0 | 1 | 79097, 79098, 79102, 79103 |
| 62 | 107..284 | 178 | 130 | 126 | 4 | 1 | 1 | 3 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..429 | 318 | 284 | 284 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 66 | 112..186 | 75 | 74 | 73 | 1 | 0 | 0 | 1 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 70 | 116..533 | 418 | 393 | 392 | 1 | 1 | 1 | 0 | 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 72 | 122..500 | 379 | 345 | 343 | 2 | 2 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 74 | 122..527 | 406 | 375 | 375 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 78 | 126..538 | 413 | 368 | 365 | 3 | 3 | 1 | 0 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 82 | 132..542 | 411 | 384 | 383 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 83 | 132..484 | 353 | 320 | 319 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110 |
| 84 | 132..531 | 400 | 364 | 363 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 139..515 | 377 | 352 | 351 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 97 | 151..467 | 317 | 277 | 274 | 3 | 3 | 1 | 0 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 107 | 177..439 | 263 | 240 | 240 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045 |
| 134 | 230..482 | 253 | 210 | 207 | 3 | 0 | 0 | 3 | 78899, 79097, 79098 |
| 154 | 281..431 | 151 | 122 | 117 | 5 | 0 | 0 | 5 | 79116, 79128, 79132, 79134 |
| 163 | 314..481 | 168 | 143 | 142 | 1 | 1 | 1 | 0 | 79098, 79102, 79103 |
| 184 | 354..445 | 92 | 85 | 84 | 1 | 1 | 1 | 0 | 79037, 79045 |
| 213 | 421..443 | 23 | 20 | 20 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 304 | 633..633 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 309 | 647..671 | 25 | 3 | 0 | 3 | 0 | 0 | 3 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9724; unmatched reference entries: 418; unmatched candidate entries: 1367
- identity switches: 483; fragmentation (coverage interruptions): 308; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 51 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 48 -> 46 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 46 -> 48 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 48 -> 46 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 48 -> 46 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 46 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 55 -> 48 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 46 -> 57 at (2093, 3030.5), 5 frames after previous cover
- f103: ref 79102: 48 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 43 -> 51 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 57 -> 43 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 46 -> 57 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 58 -> 46 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 48 -> 58 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 48 -> 55 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 51 -> 43 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 55 -> 62 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 43 -> 51 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 51 -> 50 at (2026, 3034), 1 frames after previous cover
- f109: ref 78971: 50 -> 38 at (1996.5, 3034.5), 2 frames after previous cover
- f112: ref 78896: 38 -> 65 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 48 -> 66 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 62 -> 46 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 55 -> 62 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 66 -> 55 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 48 -> 66 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 57 -> 54 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 46 -> 57 at (2055, 3030), 2 frames after previous cover
- f117: ref 79097: 54 -> 51 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 51 -> 50 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 66 -> 55 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 48 -> 66 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 70 -> 48 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 43 -> 51 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 51 -> 58 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 55 -> 62 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 62 -> 74 at (2053.5, 3026), 4 frames after previous cover
- f124: ref 79122: 70 -> 48 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 72 -> 70 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 48 -> 70 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 58 -> 78 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 62 -> 74 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 55 -> 62 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 66 -> 55 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 70 -> 66 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 48 -> 70 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 70 -> 48 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 78 -> 57 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 46 -> 78 at (2007, 3026), 1 frames after previous cover
- f127: ref 79108: 74 -> 46 at (2025.5, 3026), 2 frames after previous cover
- f127: ref 79128: 72 -> 48 at (2137, 3022.5), 1 frames after previous cover
- f127: ref 79132: 48 -> 70 at (2117, 3025), 1 frames after previous cover
- f128: ref 79132: 70 -> 72 at (2111, 3024), 1 frames after previous cover
- ... 423 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 10 | 0 (996) |
| 78896 | 350 (76..429) | 334 | 10 | 65 (304), 38 (30) |
| 78969 | 352 (80..434) | 339 | 10 | 41 (333), 65 (6) |
| 78971 | 352 (84..439) | 336 | 12 | 107 (141), 45 (89), 38 (73), 50 (15), 97 (11), 41 (5), 43 (2) |
| 79045 | 355 (84..443) | 338 | 11 | 45 (222), 107 (90), 213 (21), 43 (3), 41 (1), 184 (1) |
| 79037 | 355 (86..445) | 329 | 17 | 184 (90), 97 (84), 50 (75), 51 (42), 107 (28), 45 (4), 43 (3), 41 (3) |
| 78897 | 345 (89..450) | 329 | 14 | 50 (132), 43 (62), 97 (53), 51 (44), 45 (32), 48 (3), 107 (2), 46 (1) |
| 78899 | 365 (91..455) | 346 | 14 | 50 (91), 43 (89), 97 (70), 134 (58), 51 (27), 46 (5), 57 (4), 48 (2) |
| 79097 | 366 (94..461) | 353 | 12 | 134 (160), 43 (87), 58 (49), 50 (25), 54 (15), 51 (11), 46 (3), 48 (2), 97 (1) |
| 79098 | 360 (97..467) | 337 | 13 | 97 (71), 43 (68), 51 (65), 58 (45), 54 (28), 163 (28), 134 (12), 57 (9), 46 (7), 50 (3), 48 (1) |
| 79102 | 371 (98..477) | 343 | 17 | 163 (62), 43 (60), 58 (56), 51 (51), 83 (48), 54 (30), 57 (19), 46 (8), 87 (7), 48 (2) |
| 79103 | 380 (99..481) | 349 | 17 | 54 (108), 163 (66), 51 (65), 83 (57), 87 (28), 58 (15), 48 (4), 57 (2), 43 (2), 55 (1), 78 (1) |
| 79105 | 379 (101..484) | 365 | 10 | 83 (212), 87 (61), 54 (56), 46 (13), 62 (7), 57 (6), 55 (4), 84 (3), 78 (2), 72 (1) |
| 79108 | 385 (104..492) | 366 | 15 | 51 (80), 87 (66), 54 (65), 57 (54), 72 (40), 83 (27), 55 (8), 46 (8), 84 (8), 62 (5), 74 (4), 48 (1) |
| 79110 | 388 (106..497) | 376 | 9 | 72 (105), 54 (85), 57 (67), 74 (54), 87 (37), 62 (6), 84 (6), 55 (4), 48 (3), 78 (3), 46 (3), 66 (2), +1 more |
| 79111 | 386 (109..500) | 369 | 12 | 84 (100), 72 (93), 57 (68), 87 (66), 55 (13), 46 (10), 74 (6), 48 (4), 66 (4), 62 (3), 78 (2) |
| 79115 | 421 (111..531) | 408 | 9 | 84 (206), 46 (109), 55 (54), 62 (9), 66 (8), 74 (6), 72 (5), 48 (4), 57 (4), 78 (3) |
| 79116 | 411 (114..530) | 392 | 13 | 46 (200), 84 (61), 62 (49), 74 (49), 72 (12), 48 (6), 55 (4), 70 (3), 66 (3), 78 (2), 57 (2), 154 (1) |
| 79122 | 404 (118..532) | 392 | 12 | 57 (185), 46 (49), 78 (48), 62 (40), 74 (35), 55 (14), 70 (8), 84 (5), 66 (3), 72 (3), 48 (2) |
| 79132 | 391 (120..515) | 375 | 13 | 87 (105), 74 (96), 78 (62), 55 (57), 154 (28), 46 (9), 66 (6), 70 (5), 72 (3), 84 (2), 48 (1), 62 (1) |
| 79128 | 402 (124..527) | 388 | 11 | 74 (121), 55 (106), 154 (90), 66 (48), 72 (12), 82 (6), 46 (3), 48 (2) |
| 79134 | 407 (127..533) | 392 | 14 | 55 (119), 72 (94), 82 (66), 70 (61), 74 (30), 78 (14), 154 (5), 48 (3) |
| 79135 | 409 (129..542) | 396 | 10 | 82 (185), 78 (106), 70 (100), 48 (3), 55 (2) |
| 79139 | 406 (132..537) | 396 | 10 | 48 (114), 70 (108), 78 (82), 82 (47), 55 (45) |
| 79136 | 393 (136..538) | 380 | 13 | 70 (125), 82 (97), 48 (77), 78 (69), 62 (12) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 304 | 633..662 | 30 | 0 | 30 |
| 309 | 647..700 | 54 | 0 | 54 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 30/382/1007; tracks with internal gaps: 30; total internal gaps: 241; longest internal gap: 7; tracks ending in coasting: 32 (trailing rows total 1072)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 996 | 11 | 10 | 2 | 0 | 78911 |
| 38 | 78..215 | 138 | 138 | 103 | 35 | 3 | 1 | 32 | 78896, 78971 |
| 41 | 83..463 | 381 | 381 | 342 | 39 | 10 | 1 | 29 | 78969, 78971, 79037, 79045 |
| 43 | 86..510 | 425 | 425 | 376 | 49 | 18 | 2 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 45 | 90..479 | 390 | 390 | 347 | 43 | 13 | 2 | 29 | 78897, 78971, 79037, 79045 |
| 46 | 90..559 | 470 | 470 | 428 | 42 | 10 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 91..397 | 307 | 307 | 234 | 73 | 8 | 2 | 63 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 93..484 | 392 | 392 | 341 | 51 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 51 | 95..521 | 427 | 427 | 385 | 42 | 12 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79108 |
| 54 | 100..526 | 427 | 427 | 387 | 40 | 9 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 55 | 100..566 | 467 | 467 | 431 | 36 | 7 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 57 | 102..561 | 460 | 460 | 420 | 40 | 11 | 1 | 29 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 58 | 103..301 | 199 | 199 | 165 | 34 | 3 | 2 | 30 | 79097, 79098, 79102, 79103 |
| 62 | 107..313 | 207 | 207 | 132 | 75 | 7 | 4 | 61 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..458 | 347 | 347 | 310 | 37 | 8 | 1 | 29 | 78896, 78969 |
| 66 | 112..215 | 104 | 104 | 74 | 30 | 0 | 0 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 70 | 116..562 | 447 | 447 | 410 | 37 | 6 | 3 | 29 | 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 72 | 122..529 | 408 | 408 | 368 | 40 | 10 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 74 | 122..556 | 435 | 435 | 401 | 34 | 4 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 78 | 126..567 | 442 | 442 | 394 | 48 | 18 | 2 | 29 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 82 | 132..571 | 440 | 440 | 401 | 39 | 8 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 83 | 132..513 | 382 | 382 | 345 | 37 | 6 | 3 | 29 | 79102, 79103, 79105, 79108, 79110 |
| 84 | 132..560 | 429 | 429 | 391 | 38 | 7 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 139..544 | 406 | 406 | 370 | 36 | 7 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 97 | 151..496 | 346 | 346 | 290 | 56 | 12 | 7 | 29 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 107 | 177..468 | 292 | 292 | 261 | 31 | 2 | 1 | 29 | 78897, 78971, 79037, 79045 |
| 134 | 230..511 | 282 | 282 | 230 | 52 | 2 | 1 | 50 | 78899, 79097, 79098 |
| 154 | 281..460 | 180 | 180 | 124 | 56 | 2 | 1 | 54 | 79116, 79128, 79132, 79134 |
| 163 | 314..510 | 197 | 197 | 156 | 41 | 7 | 4 | 29 | 79098, 79102, 79103 |
| 184 | 354..474 | 121 | 121 | 91 | 30 | 1 | 1 | 29 | 79037, 79045 |
| 213 | 421..472 | 52 | 52 | 21 | 31 | 2 | 1 | 29 | 79045 |
| 304 | 633..662 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 309 | 647..700 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9724; unmatched reference entries: 418; unmatched candidate entries: 1367
- identity switches: 483; fragmentation (coverage interruptions): 308; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 43 -> 51 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 48 -> 46 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 46 -> 48 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 48 -> 46 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 48 -> 46 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 46 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 55 -> 48 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 46 -> 57 at (2093, 3030.5), 5 frames after previous cover
- f103: ref 79102: 48 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 43 -> 51 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 57 -> 43 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 46 -> 57 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 58 -> 46 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 48 -> 58 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 48 -> 55 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 51 -> 43 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 55 -> 62 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 43 -> 51 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 51 -> 50 at (2026, 3034), 1 frames after previous cover
- f109: ref 78971: 50 -> 38 at (1996.5, 3034.5), 2 frames after previous cover
- f112: ref 78896: 38 -> 65 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 48 -> 66 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 62 -> 46 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 55 -> 62 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 66 -> 55 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 48 -> 66 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 57 -> 54 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 46 -> 57 at (2055, 3030), 2 frames after previous cover
- f117: ref 79097: 54 -> 51 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 51 -> 50 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 66 -> 55 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 48 -> 66 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 70 -> 48 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 50 -> 43 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 43 -> 51 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 51 -> 58 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 55 -> 62 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 62 -> 74 at (2053.5, 3026), 4 frames after previous cover
- f124: ref 79122: 70 -> 48 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 72 -> 70 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 48 -> 70 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 58 -> 78 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 62 -> 74 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 55 -> 62 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 66 -> 55 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 70 -> 66 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 48 -> 70 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 70 -> 48 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 78 -> 57 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 46 -> 78 at (2007, 3026), 1 frames after previous cover
- f127: ref 79108: 74 -> 46 at (2025.5, 3026), 2 frames after previous cover
- f127: ref 79128: 72 -> 48 at (2137, 3022.5), 1 frames after previous cover
- f127: ref 79132: 48 -> 70 at (2117, 3025), 1 frames after previous cover
- f128: ref 79132: 70 -> 72 at (2111, 3024), 1 frames after previous cover
- ... 423 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 10 | 0 (996) |
| 78896 | 350 (76..429) | 334 | 10 | 65 (304), 38 (30) |
| 78969 | 352 (80..434) | 339 | 10 | 41 (333), 65 (6) |
| 78971 | 352 (84..439) | 336 | 12 | 107 (141), 45 (89), 38 (73), 50 (15), 97 (11), 41 (5), 43 (2) |
| 79045 | 355 (84..443) | 338 | 11 | 45 (222), 107 (90), 213 (21), 43 (3), 41 (1), 184 (1) |
| 79037 | 355 (86..445) | 329 | 17 | 184 (90), 97 (84), 50 (75), 51 (42), 107 (28), 45 (4), 43 (3), 41 (3) |
| 78897 | 345 (89..450) | 329 | 14 | 50 (132), 43 (62), 97 (53), 51 (44), 45 (32), 48 (3), 107 (2), 46 (1) |
| 78899 | 365 (91..455) | 346 | 14 | 50 (91), 43 (89), 97 (70), 134 (58), 51 (27), 46 (5), 57 (4), 48 (2) |
| 79097 | 366 (94..461) | 353 | 12 | 134 (160), 43 (87), 58 (49), 50 (25), 54 (15), 51 (11), 46 (3), 48 (2), 97 (1) |
| 79098 | 360 (97..467) | 337 | 13 | 97 (71), 43 (68), 51 (65), 58 (45), 54 (28), 163 (28), 134 (12), 57 (9), 46 (7), 50 (3), 48 (1) |
| 79102 | 371 (98..477) | 343 | 17 | 163 (62), 43 (60), 58 (56), 51 (51), 83 (48), 54 (30), 57 (19), 46 (8), 87 (7), 48 (2) |
| 79103 | 380 (99..481) | 349 | 17 | 54 (108), 163 (66), 51 (65), 83 (57), 87 (28), 58 (15), 48 (4), 57 (2), 43 (2), 55 (1), 78 (1) |
| 79105 | 379 (101..484) | 365 | 10 | 83 (212), 87 (61), 54 (56), 46 (13), 62 (7), 57 (6), 55 (4), 84 (3), 78 (2), 72 (1) |
| 79108 | 385 (104..492) | 366 | 15 | 51 (80), 87 (66), 54 (65), 57 (54), 72 (40), 83 (27), 55 (8), 46 (8), 84 (8), 62 (5), 74 (4), 48 (1) |
| 79110 | 388 (106..497) | 376 | 9 | 72 (105), 54 (85), 57 (67), 74 (54), 87 (37), 62 (6), 84 (6), 55 (4), 48 (3), 78 (3), 46 (3), 66 (2), +1 more |
| 79111 | 386 (109..500) | 369 | 12 | 84 (100), 72 (93), 57 (68), 87 (66), 55 (13), 46 (10), 74 (6), 48 (4), 66 (4), 62 (3), 78 (2) |
| 79115 | 421 (111..531) | 408 | 9 | 84 (206), 46 (109), 55 (54), 62 (9), 66 (8), 74 (6), 72 (5), 48 (4), 57 (4), 78 (3) |
| 79116 | 411 (114..530) | 392 | 13 | 46 (200), 84 (61), 62 (49), 74 (49), 72 (12), 48 (6), 55 (4), 70 (3), 66 (3), 78 (2), 57 (2), 154 (1) |
| 79122 | 404 (118..532) | 392 | 12 | 57 (185), 46 (49), 78 (48), 62 (40), 74 (35), 55 (14), 70 (8), 84 (5), 66 (3), 72 (3), 48 (2) |
| 79132 | 391 (120..515) | 375 | 13 | 87 (105), 74 (96), 78 (62), 55 (57), 154 (28), 46 (9), 66 (6), 70 (5), 72 (3), 84 (2), 48 (1), 62 (1) |
| 79128 | 402 (124..527) | 388 | 11 | 74 (121), 55 (106), 154 (90), 66 (48), 72 (12), 82 (6), 46 (3), 48 (2) |
| 79134 | 407 (127..533) | 392 | 14 | 55 (119), 72 (94), 82 (66), 70 (61), 74 (30), 78 (14), 154 (5), 48 (3) |
| 79135 | 409 (129..542) | 396 | 10 | 82 (185), 78 (106), 70 (100), 48 (3), 55 (2) |
| 79139 | 406 (132..537) | 396 | 10 | 48 (114), 70 (108), 78 (82), 82 (47), 55 (45) |
| 79136 | 393 (136..538) | 380 | 13 | 70 (125), 82 (97), 48 (77), 78 (69), 62 (12) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 304 | 633..662 | 30 | 0 | 30 |
| 309 | 647..700 | 54 | 0 | 54 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 30/382/1007; tracks with internal gaps: 30; total internal gaps: 241; longest internal gap: 7; tracks ending in coasting: 32 (trailing rows total 1072)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 996 | 11 | 10 | 2 | 0 | 78911 |
| 38 | 78..215 | 138 | 138 | 103 | 35 | 3 | 1 | 32 | 78896, 78971 |
| 41 | 83..463 | 381 | 381 | 342 | 39 | 10 | 1 | 29 | 78969, 78971, 79037, 79045 |
| 43 | 86..510 | 425 | 425 | 376 | 49 | 18 | 2 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 45 | 90..479 | 390 | 390 | 347 | 43 | 13 | 2 | 29 | 78897, 78971, 79037, 79045 |
| 46 | 90..559 | 470 | 470 | 428 | 42 | 10 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 91..397 | 307 | 307 | 234 | 73 | 8 | 2 | 63 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 93..484 | 392 | 392 | 341 | 51 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 51 | 95..521 | 427 | 427 | 385 | 42 | 12 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79108 |
| 54 | 100..526 | 427 | 427 | 387 | 40 | 9 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 55 | 100..566 | 467 | 467 | 431 | 36 | 7 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 57 | 102..561 | 460 | 460 | 420 | 40 | 11 | 1 | 29 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 58 | 103..301 | 199 | 199 | 165 | 34 | 3 | 2 | 30 | 79097, 79098, 79102, 79103 |
| 62 | 107..313 | 207 | 207 | 132 | 75 | 7 | 4 | 61 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..458 | 347 | 347 | 310 | 37 | 8 | 1 | 29 | 78896, 78969 |
| 66 | 112..215 | 104 | 104 | 74 | 30 | 0 | 0 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 70 | 116..562 | 447 | 447 | 410 | 37 | 6 | 3 | 29 | 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 72 | 122..529 | 408 | 408 | 368 | 40 | 10 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 74 | 122..556 | 435 | 435 | 401 | 34 | 4 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 78 | 126..567 | 442 | 442 | 394 | 48 | 18 | 2 | 29 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 82 | 132..571 | 440 | 440 | 401 | 39 | 8 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 83 | 132..513 | 382 | 382 | 345 | 37 | 6 | 3 | 29 | 79102, 79103, 79105, 79108, 79110 |
| 84 | 132..560 | 429 | 429 | 391 | 38 | 7 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 139..544 | 406 | 406 | 370 | 36 | 7 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 97 | 151..496 | 346 | 346 | 290 | 56 | 12 | 7 | 29 | 78897, 78899, 78971, 79037, 79097, 79098 |
| 107 | 177..468 | 292 | 292 | 261 | 31 | 2 | 1 | 29 | 78897, 78971, 79037, 79045 |
| 134 | 230..511 | 282 | 282 | 230 | 52 | 2 | 1 | 50 | 78899, 79097, 79098 |
| 154 | 281..460 | 180 | 180 | 124 | 56 | 2 | 1 | 54 | 79116, 79128, 79132, 79134 |
| 163 | 314..510 | 197 | 197 | 156 | 41 | 7 | 4 | 29 | 79098, 79102, 79103 |
| 184 | 354..474 | 121 | 121 | 91 | 30 | 1 | 1 | 29 | 79037, 79045 |
| 213 | 421..472 | 52 | 52 | 21 | 31 | 2 | 1 | 29 | 79045 |
| 304 | 633..662 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 309 | 647..700 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |
