# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=92dda0ce148a
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise0.0_fp0.5_seed1/tracks.csv sha256=afb48144ca1c05cf
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise0.0_fp0.5_seed1.csv sha256=92dda0ce148a6cc2
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise0.0_fp0.5_seed1
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
| observations | none | 4 | 0.494 | 0.275 | 0.848 | 0.01 | 0.452 | 412 | 963.0 |
| observations | none | 6 | 0.494 | 0.278 | 0.849 | 0.01 | 0.452 | 407 | 962.0 |
| observations | none | 8 | 0.494 | 0.282 | 0.849 | 0.02 | 0.455 | 404 | 962.0 |
| observations | none | 12 | 0.495 | 0.290 | 0.848 | 0.17 | 0.476 | 391 | 956.0 |
| observations | ignore | 4 | 0.494 | 0.275 | 0.848 | 0.01 | 0.452 | 412 | 963.0 |
| observations | ignore | 6 | 0.494 | 0.278 | 0.849 | 0.01 | 0.452 | 407 | 962.0 |
| observations | ignore | 8 | 0.494 | 0.282 | 0.849 | 0.02 | 0.455 | 404 | 962.0 |
| observations | ignore | 12 | 0.495 | 0.290 | 0.848 | 0.17 | 0.476 | 391 | 956.0 |
| updates | none | 4 | 0.454 | 0.264 | 0.685 | 0.05 | 0.422 | 424 | 907.0 |
| updates | none | 6 | 0.470 | 0.275 | 0.742 | 0.21 | 0.436 | 416 | 651.0 |
| updates | none | 8 | 0.479 | 0.284 | 0.810 | 0.44 | 0.454 | 400 | 345.0 |
| updates | none | 12 | 0.490 | 0.297 | 0.819 | 0.69 | 0.478 | 387 | 286.0 |
| updates | ignore | 4 | 0.454 | 0.264 | 0.685 | 0.05 | 0.422 | 424 | 907.0 |
| updates | ignore | 6 | 0.470 | 0.275 | 0.742 | 0.21 | 0.436 | 416 | 651.0 |
| updates | ignore | 8 | 0.479 | 0.284 | 0.810 | 0.44 | 0.454 | 400 | 345.0 |
| updates | ignore | 12 | 0.490 | 0.297 | 0.819 | 0.69 | 0.478 | 387 | 286.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9048; unmatched reference entries: 1094; unmatched candidate entries: 32
- identity switches: 404; fragmentation (coverage interruptions): 931; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 26 -> 28 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 32 -> 31 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 31 -> 35 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 32 -> 38 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 26 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 32 -> 31 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 31 -> 35 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 26 -> 40 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 32 -> 42 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 31 -> 35 at (2099, 3033.5), 2 frames after previous cover
- f97: ref 78897: 38 -> 31 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 42 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 32 -> 42 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 38 -> 31 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 42 -> 38 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 32 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 35 -> 46 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 31 -> 35 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 42 -> 38 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 32 -> 42 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 45 -> 32 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 35 -> 46 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 38 -> 31 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 26 -> 40 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 46 -> 26 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 31 -> 38 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 31 -> 35 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 40 -> 26 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 26 -> 46 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 38 -> 31 at (2088, 3029), 1 frames after previous cover
- f106: ref 79045: 46 -> 40 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 38 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 32 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 45 -> 32 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 38 -> 31 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 35 -> 52 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 52 -> 46 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 35 -> 52 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78969: 40 -> 28 at (1971.5, 3034.5), 5 frames after previous cover
- f110: ref 79037: 46 -> 40 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 40 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 31 -> 35 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 31 -> 56 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 38 -> 31 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 38 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 32 -> 42 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 45 -> 32 at (2118, 3025), 4 frames after previous cover
- f110: ref 79110: 45 -> 58 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 28 -> 62 at (1928, 3035), 4 frames after previous cover
- f113: ref 79037: 40 -> 57 at (1995, 3034.5), 1 frames after previous cover
- f114: ref 79045: 57 -> 40 at (1976.5, 3034.5), 2 frames after previous cover
- f118: ref 79105: 42 -> 38 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 32 -> 42 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 58 -> 32 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 45 -> 58 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 63 -> 45 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 64 -> 63 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 38 -> 42 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 42 -> 32 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 46 -> 57 at (1966, 3033.5), 1 frames after previous cover
- ... 344 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 898 | 97 | 0 (898) |
| 78896 | 350 (76..429) | 310 | 29 | 40 (171), 62 (82), 183 (28), 28 (27), 26 (2) |
| 78969 | 352 (80..434) | 313 | 27 | 71 (235), 40 (54), 26 (12), 28 (12) |
| 78971 | 352 (84..439) | 313 | 32 | 26 (141), 40 (81), 68 (53), 62 (28), 71 (5), 31 (2), 35 (2), 82 (1) |
| 79045 | 355 (84..443) | 312 | 32 | 28 (129), 68 (74), 62 (58), 82 (24), 40 (10), 35 (6), 31 (3), 46 (3), 57 (3), 32 (1), 26 (1) |
| 79037 | 355 (86..445) | 313 | 38 | 69 (93), 82 (72), 26 (64), 31 (39), 28 (12), 68 (8), 46 (7), 57 (6), 35 (4), 40 (4), 32 (2), 62 (2) |
| 78897 | 345 (89..450) | 307 | 33 | 28 (144), 31 (61), 82 (51), 26 (27), 46 (8), 38 (6), 35 (3), 32 (2), 52 (2), 57 (2), 68 (1) |
| 78899 | 365 (91..455) | 332 | 27 | 125 (139), 31 (85), 26 (73), 52 (10), 69 (10), 35 (5), 32 (3), 38 (2), 28 (2), 42 (1), 46 (1), 82 (1) |
| 79097 | 366 (94..461) | 330 | 33 | 69 (174), 31 (69), 82 (51), 26 (12), 35 (10), 38 (4), 32 (3), 46 (3), 42 (2), 52 (1), 57 (1) |
| 79098 | 360 (97..467) | 319 | 36 | 160 (78), 151 (57), 31 (50), 57 (47), 82 (20), 125 (19), 46 (15), 69 (13), 56 (9), 35 (4), 38 (3), 32 (2), +1 more |
| 79102 | 371 (98..477) | 331 | 36 | 46 (274), 31 (26), 125 (9), 57 (6), 42 (4), 38 (3), 52 (3), 32 (2), 56 (2), 82 (1), 151 (1) |
| 79103 | 380 (99..481) | 327 | 40 | 38 (138), 82 (42), 160 (42), 125 (29), 46 (25), 52 (21), 57 (8), 35 (7), 32 (5), 42 (4), 31 (2), 56 (2), +2 more |
| 79105 | 379 (101..484) | 340 | 37 | 77 (140), 35 (61), 38 (59), 42 (46), 52 (26), 32 (3), 45 (2), 31 (2), 46 (1) |
| 79108 | 385 (104..492) | 347 | 32 | 42 (145), 52 (92), 38 (50), 35 (34), 56 (9), 32 (8), 77 (6), 45 (3) |
| 79110 | 388 (106..497) | 343 | 42 | 56 (183), 42 (96), 52 (42), 58 (7), 38 (7), 77 (3), 45 (2), 35 (2), 32 (1) |
| 79111 | 386 (109..500) | 363 | 21 | 56 (111), 32 (109), 38 (87), 77 (25), 45 (8), 58 (7), 42 (7), 35 (6), 63 (3) |
| 79115 | 421 (111..531) | 374 | 42 | 58 (131), 63 (101), 42 (57), 45 (33), 56 (27), 32 (21), 77 (3), 35 (1) |
| 79116 | 411 (114..530) | 363 | 41 | 32 (193), 181 (89), 58 (58), 35 (13), 64 (4), 45 (4), 63 (2) |
| 79122 | 404 (118..532) | 364 | 36 | 58 (178), 63 (99), 35 (61), 45 (9), 114 (8), 32 (7), 64 (2) |
| 79132 | 391 (120..515) | 351 | 37 | 45 (166), 35 (159), 63 (10), 32 (9), 64 (5), 58 (2) |
| 79128 | 402 (124..527) | 357 | 43 | 63 (117), 45 (101), 77 (47), 114 (43), 181 (26), 64 (17), 35 (5), 58 (1) |
| 79134 | 407 (127..533) | 353 | 42 | 64 (130), 77 (86), 114 (53), 63 (44), 45 (39), 78 (1) |
| 79135 | 409 (129..542) | 376 | 31 | 78 (210), 64 (85), 146 (72), 72 (5), 77 (3), 114 (1) |
| 79139 | 406 (132..537) | 360 | 36 | 114 (110), 72 (92), 146 (69), 78 (64), 45 (19), 64 (6) |
| 79136 | 393 (136..538) | 352 | 31 | 64 (116), 78 (88), 146 (86), 114 (62) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 33/348/1007; tracks with internal gaps: 11; total internal gaps: 22; longest internal gap: 1; tracks ending in coasting: 8 (trailing rows total 10)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 903 | 898 | 5 | 5 | 1 | 0 | 78911 |
| 26 | 78..439 | 362 | 332 | 332 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 28 | 83..450 | 368 | 326 | 326 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 79037, 79045 |
| 31 | 86..461 | 376 | 340 | 339 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 32 | 86..500 | 415 | 372 | 371 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 35 | 89..515 | 427 | 383 | 383 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 38 | 91..481 | 391 | 359 | 359 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 40 | 94..434 | 341 | 320 | 320 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 42 | 96..492 | 397 | 366 | 364 | 2 | 2 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 45 | 100..531 | 432 | 387 | 387 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 46 | 100..477 | 378 | 337 | 337 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 52 | 108..318 | 211 | 198 | 197 | 1 | 0 | 0 | 1 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110 |
| 56 | 110..497 | 388 | 344 | 343 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79108, 79110, 79111, 79115 |
| 57 | 110..210 | 101 | 75 | 73 | 2 | 0 | 0 | 2 | 78897, 79037, 79045, 79097, 79098, 79102, 79103 |
| 58 | 110..530 | 421 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 62 | 113..303 | 191 | 172 | 170 | 2 | 1 | 1 | 1 | 78896, 78971, 79037, 79045 |
| 63 | 113..532 | 420 | 376 | 376 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 64 | 116..533 | 418 | 368 | 365 | 3 | 3 | 1 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 124..271 | 148 | 137 | 136 | 1 | 0 | 0 | 1 | 78897, 78971, 79037, 79045 |
| 69 | 124..445 | 322 | 293 | 290 | 3 | 3 | 1 | 0 | 78899, 79037, 79097, 79098 |
| 71 | 128..392 | 265 | 241 | 240 | 1 | 0 | 0 | 1 | 78969, 78971 |
| 72 | 129..239 | 111 | 99 | 97 | 2 | 0 | 0 | 2 | 79135, 79139 |
| 77 | 137..484 | 348 | 314 | 314 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79134, 79135 |
| 78 | 138..537 | 400 | 363 | 363 | 0 | 0 | 0 | 0 | 79134, 79135, 79136, 79139 |
| 82 | 144..443 | 300 | 265 | 263 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 114 | 225..538 | 314 | 277 | 277 | 0 | 0 | 0 | 0 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 125 | 243..455 | 213 | 196 | 196 | 0 | 0 | 0 | 0 | 78899, 79098, 79102, 79103 |
| 146 | 294..542 | 249 | 227 | 227 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 151 | 312..384 | 73 | 60 | 58 | 2 | 1 | 1 | 1 | 79098, 79102 |
| 160 | 337..467 | 131 | 120 | 120 | 0 | 0 | 0 | 0 | 79098, 79103 |
| 181 | 395..527 | 133 | 117 | 115 | 2 | 2 | 1 | 0 | 79116, 79128 |
| 183 | 398..430 | 33 | 29 | 28 | 1 | 0 | 0 | 1 | 78896 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9048; unmatched reference entries: 1094; unmatched candidate entries: 32
- identity switches: 404; fragmentation (coverage interruptions): 931; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 26 -> 28 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 32 -> 31 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 31 -> 35 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 32 -> 38 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 26 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 32 -> 31 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 31 -> 35 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 26 -> 40 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 32 -> 42 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 31 -> 35 at (2099, 3033.5), 2 frames after previous cover
- f97: ref 78897: 38 -> 31 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 42 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 32 -> 42 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 38 -> 31 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 42 -> 38 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 32 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 35 -> 46 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 31 -> 35 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 42 -> 38 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 32 -> 42 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 45 -> 32 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 35 -> 46 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 38 -> 31 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 26 -> 40 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 46 -> 26 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 31 -> 38 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 31 -> 35 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 40 -> 26 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 26 -> 46 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 38 -> 31 at (2088, 3029), 1 frames after previous cover
- f106: ref 79045: 46 -> 40 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 38 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 32 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 45 -> 32 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 38 -> 31 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 35 -> 52 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 52 -> 46 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 35 -> 52 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78969: 40 -> 28 at (1971.5, 3034.5), 5 frames after previous cover
- f110: ref 79037: 46 -> 40 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 40 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 31 -> 35 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 31 -> 56 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 38 -> 31 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 38 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 32 -> 42 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 45 -> 32 at (2118, 3025), 4 frames after previous cover
- f110: ref 79110: 45 -> 58 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 28 -> 62 at (1928, 3035), 4 frames after previous cover
- f113: ref 79037: 40 -> 57 at (1995, 3034.5), 1 frames after previous cover
- f114: ref 79045: 57 -> 40 at (1976.5, 3034.5), 2 frames after previous cover
- f118: ref 79105: 42 -> 38 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 32 -> 42 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 58 -> 32 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 45 -> 58 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 63 -> 45 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 64 -> 63 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 38 -> 42 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 42 -> 32 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 46 -> 57 at (1966, 3033.5), 1 frames after previous cover
- ... 344 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 898 | 97 | 0 (898) |
| 78896 | 350 (76..429) | 310 | 29 | 40 (171), 62 (82), 183 (28), 28 (27), 26 (2) |
| 78969 | 352 (80..434) | 313 | 27 | 71 (235), 40 (54), 26 (12), 28 (12) |
| 78971 | 352 (84..439) | 313 | 32 | 26 (141), 40 (81), 68 (53), 62 (28), 71 (5), 31 (2), 35 (2), 82 (1) |
| 79045 | 355 (84..443) | 312 | 32 | 28 (129), 68 (74), 62 (58), 82 (24), 40 (10), 35 (6), 31 (3), 46 (3), 57 (3), 32 (1), 26 (1) |
| 79037 | 355 (86..445) | 313 | 38 | 69 (93), 82 (72), 26 (64), 31 (39), 28 (12), 68 (8), 46 (7), 57 (6), 35 (4), 40 (4), 32 (2), 62 (2) |
| 78897 | 345 (89..450) | 307 | 33 | 28 (144), 31 (61), 82 (51), 26 (27), 46 (8), 38 (6), 35 (3), 32 (2), 52 (2), 57 (2), 68 (1) |
| 78899 | 365 (91..455) | 332 | 27 | 125 (139), 31 (85), 26 (73), 52 (10), 69 (10), 35 (5), 32 (3), 38 (2), 28 (2), 42 (1), 46 (1), 82 (1) |
| 79097 | 366 (94..461) | 330 | 33 | 69 (174), 31 (69), 82 (51), 26 (12), 35 (10), 38 (4), 32 (3), 46 (3), 42 (2), 52 (1), 57 (1) |
| 79098 | 360 (97..467) | 319 | 36 | 160 (78), 151 (57), 31 (50), 57 (47), 82 (20), 125 (19), 46 (15), 69 (13), 56 (9), 35 (4), 38 (3), 32 (2), +1 more |
| 79102 | 371 (98..477) | 331 | 36 | 46 (274), 31 (26), 125 (9), 57 (6), 42 (4), 38 (3), 52 (3), 32 (2), 56 (2), 82 (1), 151 (1) |
| 79103 | 380 (99..481) | 327 | 40 | 38 (138), 82 (42), 160 (42), 125 (29), 46 (25), 52 (21), 57 (8), 35 (7), 32 (5), 42 (4), 31 (2), 56 (2), +2 more |
| 79105 | 379 (101..484) | 340 | 37 | 77 (140), 35 (61), 38 (59), 42 (46), 52 (26), 32 (3), 45 (2), 31 (2), 46 (1) |
| 79108 | 385 (104..492) | 347 | 32 | 42 (145), 52 (92), 38 (50), 35 (34), 56 (9), 32 (8), 77 (6), 45 (3) |
| 79110 | 388 (106..497) | 343 | 42 | 56 (183), 42 (96), 52 (42), 58 (7), 38 (7), 77 (3), 45 (2), 35 (2), 32 (1) |
| 79111 | 386 (109..500) | 363 | 21 | 56 (111), 32 (109), 38 (87), 77 (25), 45 (8), 58 (7), 42 (7), 35 (6), 63 (3) |
| 79115 | 421 (111..531) | 374 | 42 | 58 (131), 63 (101), 42 (57), 45 (33), 56 (27), 32 (21), 77 (3), 35 (1) |
| 79116 | 411 (114..530) | 363 | 41 | 32 (193), 181 (89), 58 (58), 35 (13), 64 (4), 45 (4), 63 (2) |
| 79122 | 404 (118..532) | 364 | 36 | 58 (178), 63 (99), 35 (61), 45 (9), 114 (8), 32 (7), 64 (2) |
| 79132 | 391 (120..515) | 351 | 37 | 45 (166), 35 (159), 63 (10), 32 (9), 64 (5), 58 (2) |
| 79128 | 402 (124..527) | 357 | 43 | 63 (117), 45 (101), 77 (47), 114 (43), 181 (26), 64 (17), 35 (5), 58 (1) |
| 79134 | 407 (127..533) | 353 | 42 | 64 (130), 77 (86), 114 (53), 63 (44), 45 (39), 78 (1) |
| 79135 | 409 (129..542) | 376 | 31 | 78 (210), 64 (85), 146 (72), 72 (5), 77 (3), 114 (1) |
| 79139 | 406 (132..537) | 360 | 36 | 114 (110), 72 (92), 146 (69), 78 (64), 45 (19), 64 (6) |
| 79136 | 393 (136..538) | 352 | 31 | 64 (116), 78 (88), 146 (86), 114 (62) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 33/348/1007; tracks with internal gaps: 11; total internal gaps: 22; longest internal gap: 1; tracks ending in coasting: 8 (trailing rows total 10)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 903 | 898 | 5 | 5 | 1 | 0 | 78911 |
| 26 | 78..439 | 362 | 332 | 332 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 28 | 83..450 | 368 | 326 | 326 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 79037, 79045 |
| 31 | 86..461 | 376 | 340 | 339 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 32 | 86..500 | 415 | 372 | 371 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 35 | 89..515 | 427 | 383 | 383 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 38 | 91..481 | 391 | 359 | 359 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 40 | 94..434 | 341 | 320 | 320 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 42 | 96..492 | 397 | 366 | 364 | 2 | 2 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 45 | 100..531 | 432 | 387 | 387 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 46 | 100..477 | 378 | 337 | 337 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 52 | 108..318 | 211 | 198 | 197 | 1 | 0 | 0 | 1 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110 |
| 56 | 110..497 | 388 | 344 | 343 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79108, 79110, 79111, 79115 |
| 57 | 110..210 | 101 | 75 | 73 | 2 | 0 | 0 | 2 | 78897, 79037, 79045, 79097, 79098, 79102, 79103 |
| 58 | 110..530 | 421 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 62 | 113..303 | 191 | 172 | 170 | 2 | 1 | 1 | 1 | 78896, 78971, 79037, 79045 |
| 63 | 113..532 | 420 | 376 | 376 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 64 | 116..533 | 418 | 368 | 365 | 3 | 3 | 1 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 124..271 | 148 | 137 | 136 | 1 | 0 | 0 | 1 | 78897, 78971, 79037, 79045 |
| 69 | 124..445 | 322 | 293 | 290 | 3 | 3 | 1 | 0 | 78899, 79037, 79097, 79098 |
| 71 | 128..392 | 265 | 241 | 240 | 1 | 0 | 0 | 1 | 78969, 78971 |
| 72 | 129..239 | 111 | 99 | 97 | 2 | 0 | 0 | 2 | 79135, 79139 |
| 77 | 137..484 | 348 | 314 | 314 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79134, 79135 |
| 78 | 138..537 | 400 | 363 | 363 | 0 | 0 | 0 | 0 | 79134, 79135, 79136, 79139 |
| 82 | 144..443 | 300 | 265 | 263 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 114 | 225..538 | 314 | 277 | 277 | 0 | 0 | 0 | 0 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 125 | 243..455 | 213 | 196 | 196 | 0 | 0 | 0 | 0 | 78899, 79098, 79102, 79103 |
| 146 | 294..542 | 249 | 227 | 227 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 151 | 312..384 | 73 | 60 | 58 | 2 | 1 | 1 | 1 | 79098, 79102 |
| 160 | 337..467 | 131 | 120 | 120 | 0 | 0 | 0 | 0 | 79098, 79103 |
| 181 | 395..527 | 133 | 117 | 115 | 2 | 2 | 1 | 0 | 79116, 79128 |
| 183 | 398..430 | 33 | 29 | 28 | 1 | 0 | 0 | 1 | 78896 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9801; unmatched reference entries: 341; unmatched candidate entries: 1182
- identity switches: 400; fragmentation (coverage interruptions): 253; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 26 -> 28 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 32 -> 31 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 31 -> 35 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 32 -> 38 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 26 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 32 -> 31 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 31 -> 35 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 26 -> 40 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 32 -> 42 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 31 -> 35 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 38 -> 31 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 42 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 32 -> 42 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 38 -> 31 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 42 -> 38 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 32 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 35 -> 46 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 31 -> 35 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 42 -> 38 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 32 -> 42 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 45 -> 32 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 35 -> 46 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 38 -> 31 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 26 -> 40 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 46 -> 26 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 31 -> 38 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 31 -> 35 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 40 -> 26 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 26 -> 46 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 38 -> 31 at (2088, 3029), 1 frames after previous cover
- f106: ref 79045: 46 -> 40 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 38 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 32 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 45 -> 32 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 38 -> 31 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 35 -> 52 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 52 -> 46 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 35 -> 52 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78969: 40 -> 28 at (1971.5, 3034.5), 5 frames after previous cover
- f110: ref 79037: 46 -> 40 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 40 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 31 -> 35 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 31 -> 56 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 38 -> 31 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 38 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 32 -> 42 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 45 -> 32 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 45 -> 58 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 28 -> 62 at (1928, 3035), 4 frames after previous cover
- f114: ref 79037: 40 -> 57 at (1988, 3035), 1 frames after previous cover
- f114: ref 79045: 57 -> 40 at (1976.5, 3034.5), 2 frames after previous cover
- f118: ref 79105: 42 -> 38 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 32 -> 42 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 58 -> 32 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 45 -> 58 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 63 -> 45 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 64 -> 63 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 38 -> 42 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 42 -> 32 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 46 -> 57 at (1966, 3033.5), 1 frames after previous cover
- ... 340 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 10 | 0 (996) |
| 78896 | 350 (76..429) | 331 | 10 | 40 (180), 62 (90), 183 (32), 28 (27), 26 (2) |
| 78969 | 352 (80..434) | 329 | 15 | 71 (249), 40 (54), 28 (14), 26 (12) |
| 78971 | 352 (84..439) | 334 | 14 | 26 (158), 40 (82), 68 (56), 62 (28), 71 (5), 31 (2), 35 (2), 82 (1) |
| 79045 | 355 (84..443) | 335 | 13 | 28 (140), 68 (79), 62 (62), 82 (26), 40 (11), 35 (6), 31 (3), 46 (3), 57 (3), 32 (1), 26 (1) |
| 79037 | 355 (86..445) | 336 | 16 | 69 (100), 82 (77), 26 (67), 31 (43), 28 (13), 68 (9), 46 (7), 57 (6), 40 (5), 35 (4), 62 (3), 32 (2) |
| 78897 | 345 (89..450) | 329 | 13 | 28 (154), 31 (64), 82 (54), 26 (31), 46 (8), 38 (6), 35 (4), 57 (3), 32 (2), 52 (2), 68 (1) |
| 78899 | 365 (91..455) | 352 | 9 | 125 (148), 31 (93), 26 (75), 69 (11), 52 (10), 35 (5), 32 (3), 38 (2), 28 (2), 42 (1), 46 (1), 82 (1) |
| 79097 | 366 (94..461) | 353 | 10 | 69 (189), 31 (73), 82 (54), 26 (13), 35 (10), 38 (4), 32 (3), 46 (3), 42 (2), 52 (1), 57 (1) |
| 79098 | 360 (97..467) | 340 | 19 | 160 (82), 151 (64), 31 (53), 57 (50), 82 (21), 125 (21), 46 (15), 69 (13), 56 (10), 35 (4), 38 (3), 32 (2), +1 more |
| 79102 | 371 (98..477) | 362 | 8 | 46 (302), 31 (26), 125 (10), 57 (6), 42 (5), 38 (4), 52 (3), 32 (2), 56 (2), 82 (1), 151 (1) |
| 79103 | 380 (99..481) | 361 | 12 | 38 (151), 82 (50), 160 (48), 125 (32), 46 (26), 52 (22), 35 (8), 57 (8), 32 (5), 42 (4), 31 (2), 56 (2), +2 more |
| 79105 | 379 (101..484) | 369 | 9 | 77 (152), 35 (68), 38 (65), 42 (47), 52 (28), 32 (4), 45 (2), 31 (2), 46 (1) |
| 79108 | 385 (104..492) | 373 | 9 | 42 (158), 52 (97), 38 (53), 35 (37), 32 (9), 56 (9), 77 (6), 45 (4) |
| 79110 | 388 (106..497) | 377 | 10 | 56 (205), 42 (103), 52 (46), 58 (8), 38 (7), 77 (3), 45 (2), 35 (2), 32 (1) |
| 79111 | 386 (109..500) | 381 | 4 | 56 (119), 32 (114), 38 (91), 77 (25), 45 (8), 58 (8), 42 (7), 35 (6), 63 (3) |
| 79115 | 421 (111..531) | 413 | 6 | 58 (142), 63 (114), 42 (61), 45 (36), 56 (31), 32 (24), 77 (4), 35 (1) |
| 79116 | 411 (114..530) | 395 | 10 | 32 (210), 181 (98), 58 (64), 35 (13), 64 (4), 45 (4), 63 (2) |
| 79122 | 404 (118..532) | 393 | 10 | 58 (191), 63 (104), 35 (70), 45 (9), 114 (9), 32 (8), 64 (2) |
| 79132 | 391 (120..515) | 384 | 6 | 45 (187), 35 (170), 63 (10), 32 (9), 64 (6), 58 (2) |
| 79128 | 402 (124..527) | 394 | 7 | 63 (132), 45 (109), 77 (51), 114 (49), 181 (30), 64 (17), 35 (6) |
| 79134 | 407 (127..533) | 385 | 13 | 64 (142), 77 (93), 114 (57), 63 (48), 45 (44), 78 (1) |
| 79135 | 409 (129..542) | 404 | 5 | 78 (224), 64 (96), 146 (75), 72 (5), 77 (3), 114 (1) |
| 79139 | 406 (132..537) | 393 | 7 | 114 (124), 72 (99), 146 (76), 78 (68), 45 (20), 64 (6) |
| 79136 | 393 (136..538) | 382 | 8 | 64 (122), 78 (95), 146 (95), 114 (70) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 62/377/1007; tracks with internal gaps: 30; total internal gaps: 209; longest internal gap: 4; tracks ending in coasting: 31 (trailing rows total 933)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 996 | 11 | 10 | 2 | 0 | 78911 |
| 26 | 78..468 | 391 | 391 | 359 | 32 | 3 | 1 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 28 | 83..479 | 397 | 397 | 350 | 47 | 17 | 2 | 29 | 78896, 78897, 78899, 78969, 79037, 79045 |
| 31 | 86..490 | 405 | 405 | 361 | 44 | 13 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 32 | 86..529 | 444 | 444 | 399 | 45 | 11 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 35 | 89..544 | 456 | 456 | 416 | 40 | 10 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 38 | 91..510 | 420 | 420 | 386 | 34 | 5 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 40 | 94..463 | 370 | 370 | 332 | 38 | 7 | 3 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 42 | 96..521 | 426 | 426 | 390 | 36 | 6 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 45 | 100..560 | 461 | 461 | 426 | 35 | 6 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 46 | 100..506 | 407 | 407 | 366 | 41 | 11 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 52 | 108..347 | 240 | 240 | 209 | 31 | 1 | 1 | 30 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110 |
| 56 | 110..526 | 417 | 417 | 378 | 39 | 8 | 2 | 29 | 79098, 79102, 79103, 79108, 79110, 79111, 79115 |
| 57 | 110..239 | 130 | 130 | 77 | 53 | 4 | 1 | 49 | 78897, 79037, 79045, 79097, 79098, 79102, 79103 |
| 58 | 110..559 | 450 | 450 | 415 | 35 | 6 | 1 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 62 | 113..332 | 220 | 220 | 183 | 37 | 6 | 2 | 30 | 78896, 78971, 79037, 79045 |
| 63 | 113..561 | 449 | 449 | 413 | 36 | 5 | 3 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 64 | 116..562 | 447 | 447 | 395 | 52 | 17 | 4 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 124..300 | 177 | 177 | 145 | 32 | 1 | 1 | 31 | 78897, 78971, 79037, 79045 |
| 69 | 124..474 | 351 | 351 | 313 | 38 | 6 | 3 | 29 | 78899, 79037, 79097, 79098 |
| 71 | 128..421 | 294 | 294 | 254 | 40 | 8 | 3 | 30 | 78969, 78971 |
| 72 | 129..268 | 140 | 140 | 104 | 36 | 0 | 0 | 36 | 79135, 79139 |
| 77 | 137..513 | 377 | 377 | 339 | 38 | 8 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79134, 79135 |
| 78 | 138..566 | 429 | 429 | 388 | 41 | 10 | 3 | 29 | 79134, 79135, 79136, 79139 |
| 82 | 144..472 | 329 | 329 | 285 | 44 | 12 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 114 | 225..567 | 343 | 343 | 310 | 33 | 4 | 1 | 29 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 125 | 243..484 | 242 | 242 | 211 | 31 | 2 | 1 | 29 | 78899, 79098, 79102, 79103 |
| 146 | 294..571 | 278 | 278 | 246 | 32 | 3 | 1 | 29 | 79135, 79136, 79139 |
| 151 | 312..413 | 102 | 102 | 65 | 37 | 6 | 2 | 30 | 79098, 79102 |
| 160 | 337..496 | 160 | 160 | 130 | 30 | 1 | 1 | 29 | 79098, 79103 |
| 181 | 395..556 | 162 | 162 | 128 | 34 | 2 | 4 | 29 | 79116, 79128 |
| 183 | 398..459 | 62 | 62 | 32 | 30 | 0 | 0 | 30 | 78896 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9801; unmatched reference entries: 341; unmatched candidate entries: 1182
- identity switches: 400; fragmentation (coverage interruptions): 253; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f83: ref 78896: 26 -> 28 at (2114.5, 3033), 4 frames after previous cover
- f88: ref 79045: 32 -> 31 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 31 -> 35 at (2121, 3034), 2 frames after previous cover
- f91: ref 78897: 32 -> 38 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 78971: 35 -> 26 at (2108.5, 3033.5), 1 frames after previous cover
- f91: ref 79037: 32 -> 31 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 31 -> 35 at (2116.5, 3034), 1 frames after previous cover
- f94: ref 78969: 26 -> 40 at (2071, 3031), 4 frames after previous cover
- f96: ref 78899: 32 -> 42 at (2128, 3029), 3 frames after previous cover
- f96: ref 79037: 31 -> 35 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 38 -> 31 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 42 -> 38 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 32 -> 42 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 38 -> 31 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79097: 42 -> 38 at (2122.5, 3028.5), 1 frames after previous cover
- f99: ref 79098: 32 -> 42 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 35 -> 46 at (2061, 3032.5), 3 frames after previous cover
- f101: ref 78897: 31 -> 35 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79098: 42 -> 38 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 32 -> 42 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 45 -> 32 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79037: 35 -> 46 at (2062, 3034.5), 2 frames after previous cover
- f103: ref 79097: 38 -> 31 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 26 -> 40 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 46 -> 26 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79097: 31 -> 38 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78899: 31 -> 35 at (2074, 3031), 1 frames after previous cover
- f105: ref 78971: 40 -> 26 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 26 -> 46 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79097: 38 -> 31 at (2088, 3029), 1 frames after previous cover
- f106: ref 79045: 46 -> 40 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 38 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 32 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 45 -> 32 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 38 -> 31 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 35 -> 52 at (2040.5, 3033), 4 frames after previous cover
- f110: ref 78897: 52 -> 46 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 35 -> 52 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78969: 40 -> 28 at (1971.5, 3034.5), 5 frames after previous cover
- f110: ref 79037: 46 -> 40 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 40 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 31 -> 35 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79098: 31 -> 56 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 38 -> 31 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 38 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 32 -> 42 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 45 -> 32 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 45 -> 58 at (2134, 3026), 1 frames after previous cover
- f113: ref 78896: 28 -> 62 at (1928, 3035), 4 frames after previous cover
- f114: ref 79037: 40 -> 57 at (1988, 3035), 1 frames after previous cover
- f114: ref 79045: 57 -> 40 at (1976.5, 3034.5), 2 frames after previous cover
- f118: ref 79105: 42 -> 38 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 32 -> 42 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 58 -> 32 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 45 -> 58 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 63 -> 45 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 64 -> 63 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 79105: 38 -> 42 at (2050.5, 3026), 1 frames after previous cover
- f119: ref 79108: 42 -> 32 at (2070.5, 3026.5), 1 frames after previous cover
- f120: ref 78897: 46 -> 57 at (1966, 3033.5), 1 frames after previous cover
- ... 340 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 10 | 0 (996) |
| 78896 | 350 (76..429) | 331 | 10 | 40 (180), 62 (90), 183 (32), 28 (27), 26 (2) |
| 78969 | 352 (80..434) | 329 | 15 | 71 (249), 40 (54), 28 (14), 26 (12) |
| 78971 | 352 (84..439) | 334 | 14 | 26 (158), 40 (82), 68 (56), 62 (28), 71 (5), 31 (2), 35 (2), 82 (1) |
| 79045 | 355 (84..443) | 335 | 13 | 28 (140), 68 (79), 62 (62), 82 (26), 40 (11), 35 (6), 31 (3), 46 (3), 57 (3), 32 (1), 26 (1) |
| 79037 | 355 (86..445) | 336 | 16 | 69 (100), 82 (77), 26 (67), 31 (43), 28 (13), 68 (9), 46 (7), 57 (6), 40 (5), 35 (4), 62 (3), 32 (2) |
| 78897 | 345 (89..450) | 329 | 13 | 28 (154), 31 (64), 82 (54), 26 (31), 46 (8), 38 (6), 35 (4), 57 (3), 32 (2), 52 (2), 68 (1) |
| 78899 | 365 (91..455) | 352 | 9 | 125 (148), 31 (93), 26 (75), 69 (11), 52 (10), 35 (5), 32 (3), 38 (2), 28 (2), 42 (1), 46 (1), 82 (1) |
| 79097 | 366 (94..461) | 353 | 10 | 69 (189), 31 (73), 82 (54), 26 (13), 35 (10), 38 (4), 32 (3), 46 (3), 42 (2), 52 (1), 57 (1) |
| 79098 | 360 (97..467) | 340 | 19 | 160 (82), 151 (64), 31 (53), 57 (50), 82 (21), 125 (21), 46 (15), 69 (13), 56 (10), 35 (4), 38 (3), 32 (2), +1 more |
| 79102 | 371 (98..477) | 362 | 8 | 46 (302), 31 (26), 125 (10), 57 (6), 42 (5), 38 (4), 52 (3), 32 (2), 56 (2), 82 (1), 151 (1) |
| 79103 | 380 (99..481) | 361 | 12 | 38 (151), 82 (50), 160 (48), 125 (32), 46 (26), 52 (22), 35 (8), 57 (8), 32 (5), 42 (4), 31 (2), 56 (2), +2 more |
| 79105 | 379 (101..484) | 369 | 9 | 77 (152), 35 (68), 38 (65), 42 (47), 52 (28), 32 (4), 45 (2), 31 (2), 46 (1) |
| 79108 | 385 (104..492) | 373 | 9 | 42 (158), 52 (97), 38 (53), 35 (37), 32 (9), 56 (9), 77 (6), 45 (4) |
| 79110 | 388 (106..497) | 377 | 10 | 56 (205), 42 (103), 52 (46), 58 (8), 38 (7), 77 (3), 45 (2), 35 (2), 32 (1) |
| 79111 | 386 (109..500) | 381 | 4 | 56 (119), 32 (114), 38 (91), 77 (25), 45 (8), 58 (8), 42 (7), 35 (6), 63 (3) |
| 79115 | 421 (111..531) | 413 | 6 | 58 (142), 63 (114), 42 (61), 45 (36), 56 (31), 32 (24), 77 (4), 35 (1) |
| 79116 | 411 (114..530) | 395 | 10 | 32 (210), 181 (98), 58 (64), 35 (13), 64 (4), 45 (4), 63 (2) |
| 79122 | 404 (118..532) | 393 | 10 | 58 (191), 63 (104), 35 (70), 45 (9), 114 (9), 32 (8), 64 (2) |
| 79132 | 391 (120..515) | 384 | 6 | 45 (187), 35 (170), 63 (10), 32 (9), 64 (6), 58 (2) |
| 79128 | 402 (124..527) | 394 | 7 | 63 (132), 45 (109), 77 (51), 114 (49), 181 (30), 64 (17), 35 (6) |
| 79134 | 407 (127..533) | 385 | 13 | 64 (142), 77 (93), 114 (57), 63 (48), 45 (44), 78 (1) |
| 79135 | 409 (129..542) | 404 | 5 | 78 (224), 64 (96), 146 (75), 72 (5), 77 (3), 114 (1) |
| 79139 | 406 (132..537) | 393 | 7 | 114 (124), 72 (99), 146 (76), 78 (68), 45 (20), 64 (6) |
| 79136 | 393 (136..538) | 382 | 8 | 64 (122), 78 (95), 146 (95), 114 (70) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 62/377/1007; tracks with internal gaps: 30; total internal gaps: 209; longest internal gap: 4; tracks ending in coasting: 31 (trailing rows total 933)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 996 | 11 | 10 | 2 | 0 | 78911 |
| 26 | 78..468 | 391 | 391 | 359 | 32 | 3 | 1 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 28 | 83..479 | 397 | 397 | 350 | 47 | 17 | 2 | 29 | 78896, 78897, 78899, 78969, 79037, 79045 |
| 31 | 86..490 | 405 | 405 | 361 | 44 | 13 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 32 | 86..529 | 444 | 444 | 399 | 45 | 11 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 35 | 89..544 | 456 | 456 | 416 | 40 | 10 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 38 | 91..510 | 420 | 420 | 386 | 34 | 5 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 40 | 94..463 | 370 | 370 | 332 | 38 | 7 | 3 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 42 | 96..521 | 426 | 426 | 390 | 36 | 6 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 45 | 100..560 | 461 | 461 | 426 | 35 | 6 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 46 | 100..506 | 407 | 407 | 366 | 41 | 11 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 52 | 108..347 | 240 | 240 | 209 | 31 | 1 | 1 | 30 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110 |
| 56 | 110..526 | 417 | 417 | 378 | 39 | 8 | 2 | 29 | 79098, 79102, 79103, 79108, 79110, 79111, 79115 |
| 57 | 110..239 | 130 | 130 | 77 | 53 | 4 | 1 | 49 | 78897, 79037, 79045, 79097, 79098, 79102, 79103 |
| 58 | 110..559 | 450 | 450 | 415 | 35 | 6 | 1 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 62 | 113..332 | 220 | 220 | 183 | 37 | 6 | 2 | 30 | 78896, 78971, 79037, 79045 |
| 63 | 113..561 | 449 | 449 | 413 | 36 | 5 | 3 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 64 | 116..562 | 447 | 447 | 395 | 52 | 17 | 4 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 124..300 | 177 | 177 | 145 | 32 | 1 | 1 | 31 | 78897, 78971, 79037, 79045 |
| 69 | 124..474 | 351 | 351 | 313 | 38 | 6 | 3 | 29 | 78899, 79037, 79097, 79098 |
| 71 | 128..421 | 294 | 294 | 254 | 40 | 8 | 3 | 30 | 78969, 78971 |
| 72 | 129..268 | 140 | 140 | 104 | 36 | 0 | 0 | 36 | 79135, 79139 |
| 77 | 137..513 | 377 | 377 | 339 | 38 | 8 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79134, 79135 |
| 78 | 138..566 | 429 | 429 | 388 | 41 | 10 | 3 | 29 | 79134, 79135, 79136, 79139 |
| 82 | 144..472 | 329 | 329 | 285 | 44 | 12 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 114 | 225..567 | 343 | 343 | 310 | 33 | 4 | 1 | 29 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 125 | 243..484 | 242 | 242 | 211 | 31 | 2 | 1 | 29 | 78899, 79098, 79102, 79103 |
| 146 | 294..571 | 278 | 278 | 246 | 32 | 3 | 1 | 29 | 79135, 79136, 79139 |
| 151 | 312..413 | 102 | 102 | 65 | 37 | 6 | 2 | 30 | 79098, 79102 |
| 160 | 337..496 | 160 | 160 | 130 | 30 | 1 | 1 | 29 | 79098, 79103 |
| 181 | 395..556 | 162 | 162 | 128 | 34 | 2 | 4 | 29 | 79116, 79128 |
| 183 | 398..459 | 62 | 62 | 32 | 30 | 0 | 0 | 30 | 78896 |
