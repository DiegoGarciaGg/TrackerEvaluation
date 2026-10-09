# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=aad2226a23e7
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise0.0_fp0.5_seed2/tracks.csv sha256=07989428fbf7d151
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise0.0_fp0.5_seed2.csv sha256=aad2226a23e764d1
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise0.0_fp0.5_seed2
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
| observations | none | 4 | 0.522 | 0.308 | 0.855 | 0.01 | 0.535 | 316 | 977.0 |
| observations | none | 6 | 0.521 | 0.311 | 0.855 | 0.01 | 0.536 | 314 | 976.0 |
| observations | none | 8 | 0.521 | 0.316 | 0.855 | 0.02 | 0.538 | 314 | 975.0 |
| observations | none | 12 | 0.525 | 0.332 | 0.856 | 0.18 | 0.546 | 288 | 963.0 |
| observations | ignore | 4 | 0.522 | 0.308 | 0.855 | 0.01 | 0.535 | 316 | 977.0 |
| observations | ignore | 6 | 0.521 | 0.311 | 0.855 | 0.01 | 0.536 | 314 | 976.0 |
| observations | ignore | 8 | 0.521 | 0.316 | 0.855 | 0.02 | 0.538 | 314 | 975.0 |
| observations | ignore | 12 | 0.525 | 0.332 | 0.856 | 0.18 | 0.546 | 288 | 963.0 |
| updates | none | 4 | 0.474 | 0.292 | 0.672 | 0.05 | 0.494 | 321 | 907.0 |
| updates | none | 6 | 0.490 | 0.305 | 0.738 | 0.23 | 0.517 | 318 | 613.0 |
| updates | none | 8 | 0.500 | 0.315 | 0.802 | 0.46 | 0.533 | 313 | 327.0 |
| updates | none | 12 | 0.514 | 0.335 | 0.817 | 0.70 | 0.548 | 270 | 258.0 |
| updates | ignore | 4 | 0.474 | 0.292 | 0.672 | 0.05 | 0.494 | 321 | 907.0 |
| updates | ignore | 6 | 0.490 | 0.305 | 0.738 | 0.23 | 0.517 | 318 | 613.0 |
| updates | ignore | 8 | 0.500 | 0.315 | 0.802 | 0.46 | 0.533 | 313 | 327.0 |
| updates | ignore | 12 | 0.514 | 0.335 | 0.817 | 0.70 | 0.548 | 270 | 258.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9033; unmatched reference entries: 1109; unmatched candidate entries: 47
- identity switches: 314; fragmentation (coverage interruptions): 924; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 33 -> 42 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 38 -> 33 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 40 -> 38 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 40 -> 38 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 38 -> 33 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 33 -> 50 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 33 -> 51 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 40 -> 38 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 45 -> 40 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 45 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 45 -> 40 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 38 -> 60 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 40 -> 57 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 40 -> 57 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 45 -> 40 at (2136, 3025.5), 2 frames after previous cover
- f101: ref 79103: 58 -> 45 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 62 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 57 -> 61 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 58 -> 45 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 38 -> 60 at (2064, 3032), 2 frames after previous cover
- f104: ref 78899: 62 -> 38 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 60 -> 33 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 61 -> 62 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 57 -> 61 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 40 -> 57 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 45 -> 40 at (2126, 3022.5), 3 frames after previous cover
- f108: ref 79045: 33 -> 66 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 62 -> 38 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 61 -> 62 at (2084.5, 3028.5), 2 frames after previous cover
- f108: ref 79102: 57 -> 61 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79103: 40 -> 57 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 45 -> 40 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 58 -> 45 at (2125, 3025), 2 frames after previous cover
- f111: ref 78899: 38 -> 70 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 62 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 61 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 57 -> 61 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 40 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 40 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 58 -> 45 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 38 -> 57 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 57 -> 40 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 40 -> 45 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 45 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 70 -> 60 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 38 -> 70 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 61 -> 62 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 40 -> 61 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 45 -> 40 at (2092.5, 3025.5), 2 frames after previous cover
- f115: ref 79110: 58 -> 45 at (2105.5, 3026.5), 1 frames after previous cover
- f117: ref 79116: 67 -> 75 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 78897: 60 -> 66 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 62 -> 38 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 61 -> 62 at (2057, 3025), 2 frames after previous cover
- f118: ref 79108: 40 -> 61 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 45 -> 40 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 58 -> 45 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 67 -> 58 at (2118, 3022), 5 frames after previous cover
- f119: ref 79103: 38 -> 62 at (2040, 3024.5), 1 frames after previous cover
- ... 254 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 901 | 99 | 0 (901) |
| 78896 | 350 (76..429) | 313 | 32 | 42 (175), 57 (102), 86 (30), 33 (6) |
| 78969 | 352 (80..434) | 306 | 30 | 57 (108), 42 (82), 86 (80), 50 (32), 33 (4) |
| 78971 | 352 (84..439) | 313 | 32 | 60 (153), 57 (62), 42 (52), 51 (32), 50 (7), 38 (4), 33 (3) |
| 79045 | 355 (84..443) | 313 | 34 | 66 (178), 50 (81), 60 (32), 33 (12), 77 (4), 38 (3), 42 (2), 40 (1) |
| 79037 | 355 (86..445) | 317 | 31 | 77 (157), 66 (118), 33 (23), 38 (6), 51 (5), 40 (4), 60 (4) |
| 78897 | 345 (89..450) | 306 | 30 | 38 (166), 77 (116), 60 (16), 40 (6), 66 (2) |
| 78899 | 365 (91..455) | 318 | 37 | 82 (205), 60 (64), 51 (28), 77 (7), 38 (5), 70 (4), 45 (3), 62 (1), 57 (1) |
| 79097 | 366 (94..461) | 333 | 28 | 70 (174), 82 (93), 38 (30), 57 (20), 60 (5), 62 (4), 45 (3), 40 (2), 61 (1), 33 (1) |
| 79098 | 360 (97..467) | 329 | 28 | 33 (197), 38 (68), 60 (31), 70 (16), 82 (4), 57 (3), 61 (3), 62 (3), 45 (2), 40 (2) |
| 79102 | 371 (98..477) | 326 | 37 | 122 (120), 33 (94), 152 (54), 70 (30), 38 (7), 61 (6), 57 (4), 62 (4), 40 (3), 81 (3), 45 (1) |
| 79103 | 380 (99..481) | 339 | 35 | 152 (128), 70 (93), 122 (86), 61 (8), 38 (8), 40 (5), 62 (4), 57 (2), 81 (2), 58 (1), 45 (1), 33 (1) |
| 79105 | 379 (101..484) | 327 | 43 | 61 (212), 38 (32), 122 (28), 81 (26), 40 (8), 62 (8), 45 (6), 70 (3), 58 (1), 57 (1), 112 (1), 33 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 112 (147), 81 (131), 61 (42), 40 (11), 62 (5), 58 (4), 45 (4) |
| 79110 | 388 (106..497) | 356 | 28 | 81 (176), 112 (86), 62 (62), 122 (8), 61 (7), 58 (6), 45 (4), 40 (3), 38 (2), 82 (1), 119 (1) |
| 79111 | 386 (109..500) | 341 | 30 | 119 (236), 112 (38), 91 (32), 62 (13), 45 (9), 58 (4), 61 (3), 40 (3), 82 (1), 81 (1), 33 (1) |
| 79115 | 421 (111..531) | 369 | 42 | 87 (233), 40 (83), 112 (13), 129 (13), 119 (10), 67 (3), 58 (3), 82 (3), 45 (2), 61 (2), 139 (2), 83 (1), +1 more |
| 79116 | 411 (114..530) | 373 | 28 | 40 (175), 83 (56), 62 (56), 61 (44), 139 (20), 58 (6), 82 (4), 87 (4), 67 (3), 75 (3), 45 (1), 129 (1) |
| 79122 | 404 (118..532) | 362 | 34 | 83 (260), 45 (47), 40 (19), 119 (11), 62 (10), 91 (5), 75 (4), 58 (4), 67 (2) |
| 79132 | 391 (120..515) | 342 | 44 | 129 (182), 92 (66), 83 (47), 119 (29), 91 (8), 67 (3), 75 (3), 40 (3), 58 (1) |
| 79128 | 402 (124..527) | 360 | 37 | 92 (89), 58 (66), 139 (57), 129 (50), 33 (30), 87 (28), 40 (18), 91 (17), 67 (3), 75 (2) |
| 79134 | 407 (127..533) | 363 | 37 | 62 (122), 58 (62), 40 (57), 92 (53), 87 (50), 45 (11), 75 (3), 91 (3), 67 (2) |
| 79135 | 409 (129..542) | 369 | 36 | 91 (295), 75 (39), 87 (29), 67 (4), 45 (1), 62 (1) |
| 79139 | 406 (132..537) | 359 | 42 | 139 (127), 58 (109), 67 (48), 92 (38), 87 (18), 45 (17), 91 (2) |
| 79136 | 393 (136..538) | 354 | 35 | 58 (126), 62 (91), 92 (82), 139 (55) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 76 | 122..122 | 1 | 0 | 1 |
| 107 | 167..167 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 1/332/1007; tracks with internal gaps: 12; total internal gaps: 25; longest internal gap: 1; tracks ending in coasting: 10 (trailing rows total 22)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 909 | 901 | 8 | 8 | 1 | 0 | 78911 |
| 33 | 78..527 | 450 | 373 | 373 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79128 |
| 38 | 84..450 | 367 | 331 | 331 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 40 | 86..533 | 448 | 404 | 403 | 1 | 1 | 1 | 0 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 87..434 | 348 | 313 | 311 | 2 | 2 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 45 | 91..217 | 127 | 115 | 112 | 3 | 0 | 0 | 3 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 50 | 93..239 | 147 | 122 | 120 | 2 | 0 | 0 | 2 | 78969, 78971, 79045 |
| 51 | 94..166 | 73 | 67 | 65 | 2 | 0 | 0 | 2 | 78899, 78971, 79037 |
| 57 | 100..429 | 330 | 305 | 303 | 2 | 2 | 1 | 0 | 78896, 78899, 78969, 78971, 79097, 79098, 79102, 79103, 79105 |
| 58 | 100..537 | 438 | 394 | 393 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 60 | 100..439 | 340 | 307 | 305 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 61 | 103..484 | 382 | 329 | 328 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 62 | 103..530 | 428 | 386 | 384 | 2 | 2 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79134, 79135, 79136 |
| 66 | 108..443 | 336 | 298 | 298 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 67 | 111..190 | 80 | 70 | 68 | 2 | 0 | 0 | 2 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 111..467 | 357 | 320 | 320 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 75 | 117..175 | 59 | 55 | 54 | 1 | 0 | 0 | 1 | 79116, 79122, 79128, 79132, 79134, 79135 |
| 76 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 77 | 122..445 | 324 | 284 | 284 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 81 | 124..495 | 372 | 339 | 339 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 82 | 124..455 | 332 | 311 | 311 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79110, 79111, 79115, 79116 |
| 83 | 126..532 | 407 | 364 | 364 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79132 |
| 86 | 131..269 | 139 | 112 | 110 | 2 | 0 | 0 | 2 | 78896, 78969 |
| 87 | 134..531 | 398 | 362 | 362 | 0 | 0 | 0 | 0 | 79115, 79116, 79128, 79134, 79135, 79139 |
| 91 | 137..632 | 496 | 369 | 362 | 7 | 0 | 0 | 7 | 79111, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 138..515 | 378 | 330 | 328 | 2 | 2 | 1 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 107 | 167..167 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 112 | 174..491 | 318 | 285 | 285 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115 |
| 119 | 186..500 | 315 | 287 | 287 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79122, 79132 |
| 122 | 200..477 | 278 | 245 | 243 | 2 | 2 | 1 | 0 | 79102, 79103, 79105, 79110, 79115 |
| 129 | 213..495 | 283 | 248 | 246 | 2 | 1 | 1 | 1 | 79115, 79116, 79128, 79132 |
| 139 | 248..538 | 291 | 261 | 261 | 0 | 0 | 0 | 0 | 79115, 79116, 79128, 79136, 79139 |
| 152 | 274..481 | 208 | 183 | 182 | 1 | 1 | 1 | 0 | 79102, 79103 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9033; unmatched reference entries: 1109; unmatched candidate entries: 47
- identity switches: 314; fragmentation (coverage interruptions): 924; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 33 -> 42 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 38 -> 33 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 40 -> 38 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 40 -> 38 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 38 -> 33 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 33 -> 50 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 33 -> 51 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 40 -> 38 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 45 -> 40 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 45 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 45 -> 40 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 38 -> 60 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 40 -> 57 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 40 -> 57 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 45 -> 40 at (2136, 3025.5), 2 frames after previous cover
- f101: ref 79103: 58 -> 45 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 62 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 57 -> 61 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 58 -> 45 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 38 -> 60 at (2064, 3032), 2 frames after previous cover
- f104: ref 78899: 62 -> 38 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 60 -> 33 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 61 -> 62 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 57 -> 61 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 40 -> 57 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 45 -> 40 at (2126, 3022.5), 3 frames after previous cover
- f108: ref 79045: 33 -> 66 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 62 -> 38 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 61 -> 62 at (2084.5, 3028.5), 2 frames after previous cover
- f108: ref 79102: 57 -> 61 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79103: 40 -> 57 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 45 -> 40 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 58 -> 45 at (2125, 3025), 2 frames after previous cover
- f111: ref 78899: 38 -> 70 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 62 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 61 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 57 -> 61 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 40 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 40 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 58 -> 45 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 38 -> 57 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 57 -> 40 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 40 -> 45 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 45 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 70 -> 60 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 38 -> 70 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 61 -> 62 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 40 -> 61 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 45 -> 40 at (2092.5, 3025.5), 2 frames after previous cover
- f115: ref 79110: 58 -> 45 at (2105.5, 3026.5), 1 frames after previous cover
- f117: ref 79116: 67 -> 75 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 78897: 60 -> 66 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 62 -> 38 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 61 -> 62 at (2057, 3025), 2 frames after previous cover
- f118: ref 79108: 40 -> 61 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 45 -> 40 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 58 -> 45 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 67 -> 58 at (2118, 3022), 5 frames after previous cover
- f119: ref 79103: 38 -> 62 at (2040, 3024.5), 1 frames after previous cover
- ... 254 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 901 | 99 | 0 (901) |
| 78896 | 350 (76..429) | 313 | 32 | 42 (175), 57 (102), 86 (30), 33 (6) |
| 78969 | 352 (80..434) | 306 | 30 | 57 (108), 42 (82), 86 (80), 50 (32), 33 (4) |
| 78971 | 352 (84..439) | 313 | 32 | 60 (153), 57 (62), 42 (52), 51 (32), 50 (7), 38 (4), 33 (3) |
| 79045 | 355 (84..443) | 313 | 34 | 66 (178), 50 (81), 60 (32), 33 (12), 77 (4), 38 (3), 42 (2), 40 (1) |
| 79037 | 355 (86..445) | 317 | 31 | 77 (157), 66 (118), 33 (23), 38 (6), 51 (5), 40 (4), 60 (4) |
| 78897 | 345 (89..450) | 306 | 30 | 38 (166), 77 (116), 60 (16), 40 (6), 66 (2) |
| 78899 | 365 (91..455) | 318 | 37 | 82 (205), 60 (64), 51 (28), 77 (7), 38 (5), 70 (4), 45 (3), 62 (1), 57 (1) |
| 79097 | 366 (94..461) | 333 | 28 | 70 (174), 82 (93), 38 (30), 57 (20), 60 (5), 62 (4), 45 (3), 40 (2), 61 (1), 33 (1) |
| 79098 | 360 (97..467) | 329 | 28 | 33 (197), 38 (68), 60 (31), 70 (16), 82 (4), 57 (3), 61 (3), 62 (3), 45 (2), 40 (2) |
| 79102 | 371 (98..477) | 326 | 37 | 122 (120), 33 (94), 152 (54), 70 (30), 38 (7), 61 (6), 57 (4), 62 (4), 40 (3), 81 (3), 45 (1) |
| 79103 | 380 (99..481) | 339 | 35 | 152 (128), 70 (93), 122 (86), 61 (8), 38 (8), 40 (5), 62 (4), 57 (2), 81 (2), 58 (1), 45 (1), 33 (1) |
| 79105 | 379 (101..484) | 327 | 43 | 61 (212), 38 (32), 122 (28), 81 (26), 40 (8), 62 (8), 45 (6), 70 (3), 58 (1), 57 (1), 112 (1), 33 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 112 (147), 81 (131), 61 (42), 40 (11), 62 (5), 58 (4), 45 (4) |
| 79110 | 388 (106..497) | 356 | 28 | 81 (176), 112 (86), 62 (62), 122 (8), 61 (7), 58 (6), 45 (4), 40 (3), 38 (2), 82 (1), 119 (1) |
| 79111 | 386 (109..500) | 341 | 30 | 119 (236), 112 (38), 91 (32), 62 (13), 45 (9), 58 (4), 61 (3), 40 (3), 82 (1), 81 (1), 33 (1) |
| 79115 | 421 (111..531) | 369 | 42 | 87 (233), 40 (83), 112 (13), 129 (13), 119 (10), 67 (3), 58 (3), 82 (3), 45 (2), 61 (2), 139 (2), 83 (1), +1 more |
| 79116 | 411 (114..530) | 373 | 28 | 40 (175), 83 (56), 62 (56), 61 (44), 139 (20), 58 (6), 82 (4), 87 (4), 67 (3), 75 (3), 45 (1), 129 (1) |
| 79122 | 404 (118..532) | 362 | 34 | 83 (260), 45 (47), 40 (19), 119 (11), 62 (10), 91 (5), 75 (4), 58 (4), 67 (2) |
| 79132 | 391 (120..515) | 342 | 44 | 129 (182), 92 (66), 83 (47), 119 (29), 91 (8), 67 (3), 75 (3), 40 (3), 58 (1) |
| 79128 | 402 (124..527) | 360 | 37 | 92 (89), 58 (66), 139 (57), 129 (50), 33 (30), 87 (28), 40 (18), 91 (17), 67 (3), 75 (2) |
| 79134 | 407 (127..533) | 363 | 37 | 62 (122), 58 (62), 40 (57), 92 (53), 87 (50), 45 (11), 75 (3), 91 (3), 67 (2) |
| 79135 | 409 (129..542) | 369 | 36 | 91 (295), 75 (39), 87 (29), 67 (4), 45 (1), 62 (1) |
| 79139 | 406 (132..537) | 359 | 42 | 139 (127), 58 (109), 67 (48), 92 (38), 87 (18), 45 (17), 91 (2) |
| 79136 | 393 (136..538) | 354 | 35 | 58 (126), 62 (91), 92 (82), 139 (55) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 76 | 122..122 | 1 | 0 | 1 |
| 107 | 167..167 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 1/332/1007; tracks with internal gaps: 12; total internal gaps: 25; longest internal gap: 1; tracks ending in coasting: 10 (trailing rows total 22)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 909 | 901 | 8 | 8 | 1 | 0 | 78911 |
| 33 | 78..527 | 450 | 373 | 373 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79128 |
| 38 | 84..450 | 367 | 331 | 331 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 40 | 86..533 | 448 | 404 | 403 | 1 | 1 | 1 | 0 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 87..434 | 348 | 313 | 311 | 2 | 2 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 45 | 91..217 | 127 | 115 | 112 | 3 | 0 | 0 | 3 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 50 | 93..239 | 147 | 122 | 120 | 2 | 0 | 0 | 2 | 78969, 78971, 79045 |
| 51 | 94..166 | 73 | 67 | 65 | 2 | 0 | 0 | 2 | 78899, 78971, 79037 |
| 57 | 100..429 | 330 | 305 | 303 | 2 | 2 | 1 | 0 | 78896, 78899, 78969, 78971, 79097, 79098, 79102, 79103, 79105 |
| 58 | 100..537 | 438 | 394 | 393 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 60 | 100..439 | 340 | 307 | 305 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 61 | 103..484 | 382 | 329 | 328 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 62 | 103..530 | 428 | 386 | 384 | 2 | 2 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79134, 79135, 79136 |
| 66 | 108..443 | 336 | 298 | 298 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 67 | 111..190 | 80 | 70 | 68 | 2 | 0 | 0 | 2 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 111..467 | 357 | 320 | 320 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 75 | 117..175 | 59 | 55 | 54 | 1 | 0 | 0 | 1 | 79116, 79122, 79128, 79132, 79134, 79135 |
| 76 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 77 | 122..445 | 324 | 284 | 284 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 81 | 124..495 | 372 | 339 | 339 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 82 | 124..455 | 332 | 311 | 311 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79110, 79111, 79115, 79116 |
| 83 | 126..532 | 407 | 364 | 364 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79132 |
| 86 | 131..269 | 139 | 112 | 110 | 2 | 0 | 0 | 2 | 78896, 78969 |
| 87 | 134..531 | 398 | 362 | 362 | 0 | 0 | 0 | 0 | 79115, 79116, 79128, 79134, 79135, 79139 |
| 91 | 137..632 | 496 | 369 | 362 | 7 | 0 | 0 | 7 | 79111, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 138..515 | 378 | 330 | 328 | 2 | 2 | 1 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 107 | 167..167 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 112 | 174..491 | 318 | 285 | 285 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115 |
| 119 | 186..500 | 315 | 287 | 287 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79122, 79132 |
| 122 | 200..477 | 278 | 245 | 243 | 2 | 2 | 1 | 0 | 79102, 79103, 79105, 79110, 79115 |
| 129 | 213..495 | 283 | 248 | 246 | 2 | 1 | 1 | 1 | 79115, 79116, 79128, 79132 |
| 139 | 248..538 | 291 | 261 | 261 | 0 | 0 | 0 | 0 | 79115, 79116, 79128, 79136, 79139 |
| 152 | 274..481 | 208 | 183 | 182 | 1 | 1 | 1 | 0 | 79102, 79103 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9816; unmatched reference entries: 326; unmatched candidate entries: 1370
- identity switches: 313; fragmentation (coverage interruptions): 231; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 33 -> 42 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 38 -> 33 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 40 -> 38 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 40 -> 38 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 38 -> 33 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 33 -> 50 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 33 -> 51 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 40 -> 38 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 45 -> 40 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 45 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 45 -> 40 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 38 -> 60 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 40 -> 57 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 40 -> 57 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 45 -> 40 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 58 -> 45 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 62 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 57 -> 61 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 58 -> 45 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 38 -> 60 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 62 -> 38 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 60 -> 33 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 61 -> 62 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 57 -> 61 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 40 -> 57 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 45 -> 40 at (2126, 3022.5), 2 frames after previous cover
- f108: ref 79045: 33 -> 66 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 62 -> 38 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 61 -> 62 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 79103: 40 -> 61 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 45 -> 40 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 58 -> 45 at (2125, 3025), 2 frames after previous cover
- f110: ref 79102: 57 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 61 -> 57 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 78899: 38 -> 70 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 62 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 61 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 57 -> 61 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 40 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 40 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 58 -> 45 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 38 -> 57 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 57 -> 40 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 40 -> 45 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 45 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 70 -> 60 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 38 -> 70 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 61 -> 62 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 40 -> 61 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 45 -> 40 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 58 -> 45 at (2105.5, 3026.5), 1 frames after previous cover
- f118: ref 78897: 60 -> 66 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 62 -> 38 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 61 -> 62 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 40 -> 61 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 45 -> 40 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 58 -> 45 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 67 -> 58 at (2118, 3022), 5 frames after previous cover
- f118: ref 79116: 67 -> 75 at (2131.5, 3022.5), 1 frames after previous cover
- ... 253 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 11 | 0 (996) |
| 78896 | 350 (76..429) | 335 | 11 | 42 (185), 57 (111), 86 (33), 33 (6) |
| 78969 | 352 (80..434) | 331 | 8 | 57 (112), 86 (92), 42 (89), 50 (34), 33 (4) |
| 78971 | 352 (84..439) | 337 | 12 | 60 (168), 57 (63), 42 (60), 51 (33), 50 (6), 38 (4), 33 (3) |
| 79045 | 355 (84..443) | 341 | 8 | 66 (196), 50 (88), 60 (34), 33 (13), 77 (4), 38 (3), 42 (2), 40 (1) |
| 79037 | 355 (86..445) | 342 | 9 | 77 (174), 66 (126), 33 (23), 38 (6), 51 (5), 40 (4), 60 (4) |
| 78897 | 345 (89..450) | 330 | 8 | 38 (183), 77 (122), 60 (17), 40 (6), 66 (2) |
| 78899 | 365 (91..455) | 344 | 12 | 82 (221), 60 (71), 51 (30), 77 (8), 38 (5), 70 (4), 45 (3), 62 (1), 57 (1) |
| 79097 | 366 (94..461) | 353 | 12 | 70 (190), 82 (94), 38 (32), 57 (21), 60 (5), 62 (4), 45 (3), 40 (2), 61 (1), 33 (1) |
| 79098 | 360 (97..467) | 355 | 5 | 33 (217), 38 (71), 60 (33), 70 (16), 61 (4), 82 (4), 57 (3), 62 (3), 45 (2), 40 (2) |
| 79102 | 371 (98..477) | 357 | 8 | 122 (135), 33 (101), 152 (60), 70 (32), 38 (7), 57 (6), 61 (4), 62 (4), 40 (3), 81 (3), 45 (2) |
| 79103 | 380 (99..481) | 366 | 11 | 152 (138), 70 (103), 122 (93), 61 (8), 38 (8), 40 (5), 62 (4), 45 (2), 81 (2), 58 (1), 57 (1), 33 (1) |
| 79105 | 379 (101..484) | 365 | 11 | 61 (241), 38 (37), 122 (29), 81 (28), 40 (8), 62 (8), 45 (6), 70 (3), 33 (2), 58 (1), 57 (1), 112 (1) |
| 79108 | 385 (104..492) | 376 | 7 | 112 (158), 81 (144), 61 (47), 40 (11), 45 (5), 62 (5), 58 (4), 33 (2) |
| 79110 | 388 (106..497) | 385 | 2 | 81 (191), 112 (96), 62 (64), 122 (9), 61 (8), 58 (6), 45 (4), 40 (3), 38 (2), 82 (1), 119 (1) |
| 79111 | 386 (109..500) | 366 | 12 | 119 (253), 112 (40), 91 (38), 62 (13), 45 (9), 58 (4), 61 (3), 40 (3), 82 (2), 81 (1) |
| 79115 | 421 (111..531) | 405 | 8 | 87 (254), 40 (93), 112 (16), 129 (14), 119 (10), 67 (3), 58 (3), 82 (3), 61 (3), 45 (2), 139 (2), 83 (1), +1 more |
| 79116 | 411 (114..530) | 398 | 10 | 40 (189), 62 (60), 83 (57), 61 (47), 139 (20), 87 (7), 58 (6), 67 (4), 82 (4), 75 (2), 45 (1), 129 (1) |
| 79122 | 404 (118..532) | 389 | 11 | 83 (285), 45 (47), 40 (19), 62 (12), 119 (11), 91 (5), 75 (4), 58 (4), 67 (2) |
| 79132 | 391 (120..515) | 381 | 9 | 129 (201), 92 (75), 83 (52), 119 (31), 91 (10), 67 (4), 75 (3), 40 (3), 58 (1), 139 (1) |
| 79128 | 402 (124..527) | 389 | 11 | 92 (100), 58 (69), 139 (61), 129 (56), 33 (33), 87 (30), 40 (18), 91 (17), 67 (3), 75 (2) |
| 79134 | 407 (127..533) | 397 | 8 | 62 (131), 58 (67), 92 (63), 40 (62), 87 (54), 45 (12), 75 (3), 91 (3), 67 (2) |
| 79135 | 409 (129..542) | 403 | 6 | 91 (323), 75 (43), 87 (31), 67 (4), 45 (1), 62 (1) |
| 79139 | 406 (132..537) | 393 | 12 | 139 (142), 58 (116), 67 (55), 92 (42), 87 (19), 45 (17), 91 (2) |
| 79136 | 393 (136..538) | 382 | 9 | 58 (141), 62 (96), 92 (87), 139 (58) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 76 | 122..151 | 30 | 0 | 30 |
| 107 | 167..196 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 30/361/1007; tracks with internal gaps: 30; total internal gaps: 231; longest internal gap: 21; tracks ending in coasting: 32 (trailing rows total 1060)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 996 | 11 | 11 | 1 | 0 | 78911 |
| 33 | 78..556 | 479 | 479 | 406 | 73 | 18 | 21 | 29 | 78896, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79128 |
| 38 | 84..479 | 396 | 396 | 358 | 38 | 9 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 40 | 86..562 | 477 | 477 | 432 | 45 | 11 | 3 | 29 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 87..463 | 377 | 377 | 336 | 41 | 8 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 45 | 91..246 | 156 | 156 | 116 | 40 | 1 | 1 | 39 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 50 | 93..268 | 176 | 176 | 128 | 48 | 2 | 1 | 46 | 78969, 78971, 79045 |
| 51 | 94..195 | 102 | 102 | 68 | 34 | 1 | 1 | 33 | 78899, 78971, 79037 |
| 57 | 100..458 | 359 | 359 | 319 | 40 | 9 | 2 | 29 | 78896, 78899, 78969, 78971, 79097, 79098, 79102, 79103, 79105 |
| 58 | 100..566 | 467 | 467 | 423 | 44 | 12 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 60 | 100..468 | 369 | 369 | 332 | 37 | 6 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 61 | 103..513 | 411 | 411 | 366 | 45 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 62 | 103..559 | 457 | 457 | 406 | 51 | 12 | 6 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79134, 79135, 79136 |
| 66 | 108..472 | 365 | 365 | 324 | 41 | 9 | 3 | 29 | 78897, 79037, 79045 |
| 67 | 111..219 | 109 | 109 | 77 | 32 | 0 | 0 | 32 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 111..496 | 386 | 386 | 348 | 38 | 7 | 3 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 75 | 117..204 | 88 | 88 | 57 | 31 | 1 | 1 | 30 | 79116, 79122, 79128, 79132, 79134, 79135 |
| 76 | 122..151 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 77 | 122..474 | 353 | 353 | 308 | 45 | 13 | 2 | 29 | 78897, 78899, 79037, 79045 |
| 81 | 124..524 | 401 | 401 | 369 | 32 | 5 | 1 | 27 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 82 | 124..484 | 361 | 361 | 329 | 32 | 3 | 1 | 29 | 78899, 79097, 79098, 79110, 79111, 79115, 79116 |
| 83 | 126..561 | 436 | 436 | 395 | 41 | 10 | 3 | 29 | 79115, 79116, 79122, 79132 |
| 86 | 131..298 | 168 | 168 | 125 | 43 | 4 | 2 | 37 | 78896, 78969 |
| 87 | 134..560 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79115, 79116, 79128, 79134, 79135, 79139 |
| 91 | 137..661 | 525 | 525 | 398 | 127 | 8 | 1 | 119 | 79111, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 138..544 | 407 | 407 | 367 | 40 | 10 | 2 | 29 | 79128, 79132, 79134, 79136, 79139 |
| 107 | 167..196 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 112 | 174..520 | 347 | 347 | 311 | 36 | 6 | 2 | 28 | 79105, 79108, 79110, 79111, 79115 |
| 119 | 186..529 | 344 | 344 | 306 | 38 | 7 | 2 | 29 | 79110, 79111, 79115, 79122, 79132 |
| 122 | 200..506 | 307 | 307 | 267 | 40 | 11 | 3 | 25 | 79102, 79103, 79105, 79110, 79115 |
| 129 | 213..524 | 312 | 312 | 272 | 40 | 9 | 2 | 30 | 79115, 79116, 79128, 79132 |
| 139 | 248..567 | 320 | 320 | 284 | 36 | 6 | 2 | 29 | 79115, 79116, 79128, 79132, 79136, 79139 |
| 152 | 274..510 | 237 | 237 | 198 | 39 | 6 | 2 | 32 | 79102, 79103 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 33; matched pairs: 9816; unmatched reference entries: 326; unmatched candidate entries: 1370
- identity switches: 313; fragmentation (coverage interruptions): 231; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 33 -> 42 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 38 -> 33 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 40 -> 38 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 40 -> 38 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 38 -> 33 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 33 -> 50 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 33 -> 51 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 40 -> 38 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 45 -> 40 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 45 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 45 -> 40 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 38 -> 60 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 40 -> 57 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 40 -> 57 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 45 -> 40 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 58 -> 45 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 62 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 57 -> 61 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 58 -> 45 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 38 -> 60 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 62 -> 38 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 60 -> 33 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 61 -> 62 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 57 -> 61 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 40 -> 57 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 45 -> 40 at (2126, 3022.5), 2 frames after previous cover
- f108: ref 79045: 33 -> 66 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 62 -> 38 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 61 -> 62 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 79103: 40 -> 61 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 45 -> 40 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 58 -> 45 at (2125, 3025), 2 frames after previous cover
- f110: ref 79102: 57 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 61 -> 57 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 78899: 38 -> 70 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 62 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 61 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 57 -> 61 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 40 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 40 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 58 -> 45 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 38 -> 57 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 57 -> 40 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 40 -> 45 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 45 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 70 -> 60 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 38 -> 70 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 61 -> 62 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 40 -> 61 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 45 -> 40 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 58 -> 45 at (2105.5, 3026.5), 1 frames after previous cover
- f118: ref 78897: 60 -> 66 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 62 -> 38 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 61 -> 62 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 40 -> 61 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 45 -> 40 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 58 -> 45 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 67 -> 58 at (2118, 3022), 5 frames after previous cover
- f118: ref 79116: 67 -> 75 at (2131.5, 3022.5), 1 frames after previous cover
- ... 253 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 996 | 11 | 0 (996) |
| 78896 | 350 (76..429) | 335 | 11 | 42 (185), 57 (111), 86 (33), 33 (6) |
| 78969 | 352 (80..434) | 331 | 8 | 57 (112), 86 (92), 42 (89), 50 (34), 33 (4) |
| 78971 | 352 (84..439) | 337 | 12 | 60 (168), 57 (63), 42 (60), 51 (33), 50 (6), 38 (4), 33 (3) |
| 79045 | 355 (84..443) | 341 | 8 | 66 (196), 50 (88), 60 (34), 33 (13), 77 (4), 38 (3), 42 (2), 40 (1) |
| 79037 | 355 (86..445) | 342 | 9 | 77 (174), 66 (126), 33 (23), 38 (6), 51 (5), 40 (4), 60 (4) |
| 78897 | 345 (89..450) | 330 | 8 | 38 (183), 77 (122), 60 (17), 40 (6), 66 (2) |
| 78899 | 365 (91..455) | 344 | 12 | 82 (221), 60 (71), 51 (30), 77 (8), 38 (5), 70 (4), 45 (3), 62 (1), 57 (1) |
| 79097 | 366 (94..461) | 353 | 12 | 70 (190), 82 (94), 38 (32), 57 (21), 60 (5), 62 (4), 45 (3), 40 (2), 61 (1), 33 (1) |
| 79098 | 360 (97..467) | 355 | 5 | 33 (217), 38 (71), 60 (33), 70 (16), 61 (4), 82 (4), 57 (3), 62 (3), 45 (2), 40 (2) |
| 79102 | 371 (98..477) | 357 | 8 | 122 (135), 33 (101), 152 (60), 70 (32), 38 (7), 57 (6), 61 (4), 62 (4), 40 (3), 81 (3), 45 (2) |
| 79103 | 380 (99..481) | 366 | 11 | 152 (138), 70 (103), 122 (93), 61 (8), 38 (8), 40 (5), 62 (4), 45 (2), 81 (2), 58 (1), 57 (1), 33 (1) |
| 79105 | 379 (101..484) | 365 | 11 | 61 (241), 38 (37), 122 (29), 81 (28), 40 (8), 62 (8), 45 (6), 70 (3), 33 (2), 58 (1), 57 (1), 112 (1) |
| 79108 | 385 (104..492) | 376 | 7 | 112 (158), 81 (144), 61 (47), 40 (11), 45 (5), 62 (5), 58 (4), 33 (2) |
| 79110 | 388 (106..497) | 385 | 2 | 81 (191), 112 (96), 62 (64), 122 (9), 61 (8), 58 (6), 45 (4), 40 (3), 38 (2), 82 (1), 119 (1) |
| 79111 | 386 (109..500) | 366 | 12 | 119 (253), 112 (40), 91 (38), 62 (13), 45 (9), 58 (4), 61 (3), 40 (3), 82 (2), 81 (1) |
| 79115 | 421 (111..531) | 405 | 8 | 87 (254), 40 (93), 112 (16), 129 (14), 119 (10), 67 (3), 58 (3), 82 (3), 61 (3), 45 (2), 139 (2), 83 (1), +1 more |
| 79116 | 411 (114..530) | 398 | 10 | 40 (189), 62 (60), 83 (57), 61 (47), 139 (20), 87 (7), 58 (6), 67 (4), 82 (4), 75 (2), 45 (1), 129 (1) |
| 79122 | 404 (118..532) | 389 | 11 | 83 (285), 45 (47), 40 (19), 62 (12), 119 (11), 91 (5), 75 (4), 58 (4), 67 (2) |
| 79132 | 391 (120..515) | 381 | 9 | 129 (201), 92 (75), 83 (52), 119 (31), 91 (10), 67 (4), 75 (3), 40 (3), 58 (1), 139 (1) |
| 79128 | 402 (124..527) | 389 | 11 | 92 (100), 58 (69), 139 (61), 129 (56), 33 (33), 87 (30), 40 (18), 91 (17), 67 (3), 75 (2) |
| 79134 | 407 (127..533) | 397 | 8 | 62 (131), 58 (67), 92 (63), 40 (62), 87 (54), 45 (12), 75 (3), 91 (3), 67 (2) |
| 79135 | 409 (129..542) | 403 | 6 | 91 (323), 75 (43), 87 (31), 67 (4), 45 (1), 62 (1) |
| 79139 | 406 (132..537) | 393 | 12 | 139 (142), 58 (116), 67 (55), 92 (42), 87 (19), 45 (17), 91 (2) |
| 79136 | 393 (136..538) | 382 | 9 | 58 (141), 62 (96), 92 (87), 139 (58) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 76 | 122..151 | 30 | 0 | 30 |
| 107 | 167..196 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 33; lifespan min/median/max: 30/361/1007; tracks with internal gaps: 30; total internal gaps: 231; longest internal gap: 21; tracks ending in coasting: 32 (trailing rows total 1060)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 996 | 11 | 11 | 1 | 0 | 78911 |
| 33 | 78..556 | 479 | 479 | 406 | 73 | 18 | 21 | 29 | 78896, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79128 |
| 38 | 84..479 | 396 | 396 | 358 | 38 | 9 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 40 | 86..562 | 477 | 477 | 432 | 45 | 11 | 3 | 29 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 87..463 | 377 | 377 | 336 | 41 | 8 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 45 | 91..246 | 156 | 156 | 116 | 40 | 1 | 1 | 39 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 50 | 93..268 | 176 | 176 | 128 | 48 | 2 | 1 | 46 | 78969, 78971, 79045 |
| 51 | 94..195 | 102 | 102 | 68 | 34 | 1 | 1 | 33 | 78899, 78971, 79037 |
| 57 | 100..458 | 359 | 359 | 319 | 40 | 9 | 2 | 29 | 78896, 78899, 78969, 78971, 79097, 79098, 79102, 79103, 79105 |
| 58 | 100..566 | 467 | 467 | 423 | 44 | 12 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 60 | 100..468 | 369 | 369 | 332 | 37 | 6 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 61 | 103..513 | 411 | 411 | 366 | 45 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 62 | 103..559 | 457 | 457 | 406 | 51 | 12 | 6 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79134, 79135, 79136 |
| 66 | 108..472 | 365 | 365 | 324 | 41 | 9 | 3 | 29 | 78897, 79037, 79045 |
| 67 | 111..219 | 109 | 109 | 77 | 32 | 0 | 0 | 32 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 70 | 111..496 | 386 | 386 | 348 | 38 | 7 | 3 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 75 | 117..204 | 88 | 88 | 57 | 31 | 1 | 1 | 30 | 79116, 79122, 79128, 79132, 79134, 79135 |
| 76 | 122..151 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 77 | 122..474 | 353 | 353 | 308 | 45 | 13 | 2 | 29 | 78897, 78899, 79037, 79045 |
| 81 | 124..524 | 401 | 401 | 369 | 32 | 5 | 1 | 27 | 79102, 79103, 79105, 79108, 79110, 79111 |
| 82 | 124..484 | 361 | 361 | 329 | 32 | 3 | 1 | 29 | 78899, 79097, 79098, 79110, 79111, 79115, 79116 |
| 83 | 126..561 | 436 | 436 | 395 | 41 | 10 | 3 | 29 | 79115, 79116, 79122, 79132 |
| 86 | 131..298 | 168 | 168 | 125 | 43 | 4 | 2 | 37 | 78896, 78969 |
| 87 | 134..560 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79115, 79116, 79128, 79134, 79135, 79139 |
| 91 | 137..661 | 525 | 525 | 398 | 127 | 8 | 1 | 119 | 79111, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 138..544 | 407 | 407 | 367 | 40 | 10 | 2 | 29 | 79128, 79132, 79134, 79136, 79139 |
| 107 | 167..196 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 112 | 174..520 | 347 | 347 | 311 | 36 | 6 | 2 | 28 | 79105, 79108, 79110, 79111, 79115 |
| 119 | 186..529 | 344 | 344 | 306 | 38 | 7 | 2 | 29 | 79110, 79111, 79115, 79122, 79132 |
| 122 | 200..506 | 307 | 307 | 267 | 40 | 11 | 3 | 25 | 79102, 79103, 79105, 79110, 79115 |
| 129 | 213..524 | 312 | 312 | 272 | 40 | 9 | 2 | 30 | 79115, 79116, 79128, 79132 |
| 139 | 248..567 | 320 | 320 | 284 | 36 | 6 | 2 | 29 | 79115, 79116, 79128, 79132, 79136, 79139 |
| 152 | 274..510 | 237 | 237 | 198 | 39 | 6 | 2 | 32 | 79102, 79103 |
