# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=a5975141d922
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise1.0_fp0.0_seed2/tracks.csv sha256=a350344af2fed525
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise1.0_fp0.0_seed2.csv sha256=a5975141d922ac30
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise1.0_fp0.0_seed2
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
| observations | none | 4 | 0.362 | 0.201 | 0.724 | 1.28 | 0.454 | 694 | 1558.0 |
| observations | none | 6 | 0.390 | 0.217 | 0.725 | 1.29 | 0.456 | 685 | 1554.0 |
| observations | none | 8 | 0.404 | 0.229 | 0.725 | 1.30 | 0.457 | 682 | 1553.0 |
| observations | none | 12 | 0.421 | 0.247 | 0.727 | 1.54 | 0.469 | 603 | 1534.0 |
| observations | ignore | 4 | 0.362 | 0.201 | 0.724 | 1.28 | 0.454 | 694 | 1558.0 |
| observations | ignore | 6 | 0.390 | 0.217 | 0.725 | 1.29 | 0.456 | 685 | 1554.0 |
| observations | ignore | 8 | 0.404 | 0.229 | 0.725 | 1.30 | 0.457 | 682 | 1553.0 |
| observations | ignore | 12 | 0.421 | 0.247 | 0.727 | 1.54 | 0.469 | 603 | 1534.0 |
| updates | none | 4 | 0.342 | 0.199 | 0.536 | 1.33 | 0.424 | 735 | 1447.0 |
| updates | none | 6 | 0.391 | 0.228 | 0.630 | 1.55 | 0.455 | 721 | 1076.0 |
| updates | none | 8 | 0.420 | 0.248 | 0.728 | 1.84 | 0.481 | 689 | 703.0 |
| updates | none | 12 | 0.453 | 0.276 | 0.776 | 2.29 | 0.507 | 594 | 522.0 |
| updates | ignore | 4 | 0.342 | 0.199 | 0.536 | 1.33 | 0.424 | 735 | 1447.0 |
| updates | ignore | 6 | 0.391 | 0.228 | 0.630 | 1.55 | 0.455 | 721 | 1076.0 |
| updates | ignore | 8 | 0.420 | 0.248 | 0.728 | 1.84 | 0.481 | 689 | 703.0 |
| updates | ignore | 12 | 0.453 | 0.276 | 0.776 | 2.29 | 0.507 | 594 | 522.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8039; unmatched reference entries: 2103; unmatched candidate entries: 2
- identity switches: 682; fragmentation (coverage interruptions): 1579; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 7 -> 8 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 7 -> 8 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 8 -> 9 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 8 -> 9 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 7 -> 8 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 9 -> 10 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 10 -> 11 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 7 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 9 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 8 -> 9 at (2109.5, 3030), 3 frames after previous cover
- f99: ref 79037: 10 -> 11 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 5 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 7 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 5 -> 6 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 8 -> 12 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 13 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 8 at (2124.5, 3027.5), 4 frames after previous cover
- f103: ref 79105: 13 -> 7 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 6 -> 11 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 8 -> 7 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 11 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 5 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 5 -> 11 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 8 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 6 -> 11 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 11 -> 5 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 10 -> 9 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 5 -> 10 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 13 -> 16 at (2131, 3027), 4 frames after previous cover
- f111: ref 78897: 9 -> 10 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 10 -> 5 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 5 -> 6 at (1994.5, 3035), 2 frames after previous cover
- f111: ref 79097: 12 -> 19 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 8 -> 12 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 7 -> 20 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 7 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 8 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 13 -> 7 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 13 -> 16 at (2142, 3026.5), 2 frames after previous cover
- f112: ref 79102: 8 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 6 -> 11 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 20 -> 21 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 21 -> 7 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 9 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 19 -> 9 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 12 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 21 -> 12 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 7 -> 21 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 8 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 7 -> 8 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 16 -> 7 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 13 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 6 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 11 -> 4 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 6 -> 11 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 6 -> 10 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 10 -> 9 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 5 -> 6 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 11 -> 5 at (1963.5, 3035.5), 1 frames after previous cover
- ... 622 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 796 | 163 | 3 (796) |
| 78896 | 350 (76..429) | 276 | 54 | 4 (143), 32 (110), 11 (23) |
| 78969 | 352 (80..434) | 279 | 51 | 9 (108), 25 (102), 11 (20), 4 (15), 5 (14), 6 (10), 19 (9), 32 (1) |
| 78971 | 352 (84..439) | 281 | 49 | 11 (192), 5 (27), 6 (14), 25 (13), 9 (13), 19 (13), 32 (8), 4 (1) |
| 79045 | 355 (84..443) | 286 | 44 | 19 (191), 11 (36), 5 (23), 9 (13), 32 (10), 6 (4), 4 (4), 25 (3), 10 (2) |
| 79037 | 355 (86..445) | 283 | 61 | 4 (109), 9 (108), 11 (16), 25 (13), 10 (9), 19 (9), 5 (8), 6 (5), 7 (3), 8 (2), 32 (1) |
| 78897 | 345 (89..450) | 279 | 49 | 25 (129), 6 (33), 9 (28), 19 (24), 30 (21), 4 (14), 10 (12), 5 (9), 32 (3), 7 (2), 8 (2), 11 (2) |
| 78899 | 365 (91..455) | 290 | 57 | 30 (181), 10 (32), 6 (22), 4 (14), 9 (13), 19 (9), 5 (9), 7 (3), 8 (2), 32 (2), 25 (2), 12 (1) |
| 79097 | 366 (94..461) | 295 | 60 | 5 (119), 32 (88), 10 (21), 30 (18), 12 (11), 19 (11), 31 (10), 9 (8), 7 (3), 25 (3), 6 (2), 8 (1) |
| 79098 | 360 (97..467) | 279 | 60 | 21 (92), 31 (76), 5 (32), 32 (21), 6 (20), 10 (13), 12 (7), 19 (7), 8 (5), 9 (3), 7 (2), 30 (1) |
| 79102 | 371 (98..477) | 299 | 61 | 10 (124), 21 (61), 5 (47), 31 (27), 6 (15), 8 (6), 12 (6), 30 (6), 7 (2), 20 (2), 32 (2), 19 (1) |
| 79103 | 380 (99..481) | 299 | 59 | 12 (117), 21 (60), 10 (41), 31 (29), 6 (16), 5 (16), 30 (6), 19 (5), 32 (4), 7 (2), 20 (2), 13 (1) |
| 79105 | 379 (101..484) | 293 | 65 | 31 (116), 10 (56), 12 (38), 21 (29), 30 (22), 7 (9), 5 (9), 19 (6), 6 (5), 13 (1), 20 (1), 32 (1) |
| 79108 | 385 (104..492) | 295 | 64 | 27 (134), 12 (71), 21 (50), 31 (12), 20 (9), 6 (5), 8 (4), 16 (3), 30 (3), 10 (2), 13 (1), 33 (1) |
| 79110 | 388 (106..497) | 313 | 57 | 29 (130), 27 (75), 33 (45), 12 (26), 16 (12), 31 (6), 8 (5), 30 (5), 20 (4), 13 (2), 7 (2), 6 (1) |
| 79111 | 386 (109..500) | 306 | 65 | 28 (115), 16 (65), 12 (49), 29 (31), 27 (15), 33 (14), 8 (8), 7 (4), 30 (3), 13 (1), 6 (1) |
| 79115 | 421 (111..531) | 320 | 69 | 16 (145), 29 (110), 33 (17), 28 (17), 8 (13), 20 (5), 13 (3), 7 (3), 12 (3), 27 (2), 31 (1), 6 (1) |
| 79116 | 411 (114..530) | 334 | 58 | 7 (130), 28 (72), 20 (35), 27 (30), 29 (28), 8 (17), 33 (7), 13 (6), 6 (5), 16 (4) |
| 79122 | 404 (118..532) | 324 | 64 | 20 (157), 8 (48), 6 (48), 28 (38), 16 (15), 29 (6), 7 (4), 33 (4), 13 (2), 27 (2) |
| 79132 | 391 (120..515) | 308 | 53 | 6 (145), 8 (107), 27 (33), 20 (14), 16 (3), 7 (3), 28 (2), 13 (1) |
| 79128 | 402 (124..527) | 314 | 65 | 37 (115), 20 (113), 8 (26), 28 (25), 7 (11), 6 (8), 13 (7), 27 (5), 16 (4) |
| 79134 | 407 (127..533) | 334 | 64 | 8 (132), 13 (97), 16 (36), 28 (31), 7 (22), 27 (9), 33 (5), 36 (2) |
| 79135 | 409 (129..542) | 332 | 58 | 13 (156), 33 (65), 16 (45), 7 (30), 36 (23), 28 (11), 27 (2) |
| 79139 | 406 (132..537) | 312 | 65 | 36 (183), 13 (68), 33 (43), 7 (10), 16 (8) |
| 79136 | 393 (136..538) | 312 | 64 | 7 (133), 33 (123), 36 (42), 13 (14) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 145/368/1001; tracks with internal gaps: 2; total internal gaps: 2; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 796 | 796 | 0 | 0 | 0 | 0 | 78911 |
| 4 | 78..445 | 368 | 300 | 300 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 5 | 82..461 | 380 | 313 | 313 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 6 | 86..515 | 430 | 361 | 360 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 7 | 86..530 | 445 | 378 | 378 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..533 | 445 | 378 | 378 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 91..434 | 344 | 294 | 294 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 10 | 93..477 | 385 | 312 | 312 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 97..439 | 343 | 289 | 289 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 12 | 100..481 | 382 | 329 | 329 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 13 | 100..542 | 443 | 360 | 360 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 108..532 | 425 | 340 | 340 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 111..443 | 333 | 285 | 285 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 111..531 | 421 | 342 | 342 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..467 | 357 | 292 | 292 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 25 | 126..450 | 325 | 265 | 265 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 27 | 129..492 | 364 | 307 | 307 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 28 | 130..500 | 371 | 311 | 311 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 130..497 | 368 | 305 | 305 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 30 | 133..455 | 323 | 266 | 266 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 31 | 133..484 | 352 | 278 | 277 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 32 | 138..429 | 292 | 251 | 251 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 33 | 138..537 | 400 | 324 | 324 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 36 | 213..537 | 325 | 250 | 250 | 0 | 0 | 0 | 0 | 79134, 79135, 79136, 79139 |
| 37 | 383..527 | 145 | 115 | 115 | 0 | 0 | 0 | 0 | 79128 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8039; unmatched reference entries: 2103; unmatched candidate entries: 2
- identity switches: 682; fragmentation (coverage interruptions): 1579; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 7 -> 8 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 7 -> 8 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 8 -> 9 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 8 -> 9 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 7 -> 8 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 9 -> 10 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 10 -> 11 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 7 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 9 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 8 -> 9 at (2109.5, 3030), 3 frames after previous cover
- f99: ref 79037: 10 -> 11 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 5 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 7 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 5 -> 6 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 8 -> 12 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 13 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 8 at (2124.5, 3027.5), 4 frames after previous cover
- f103: ref 79105: 13 -> 7 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 6 -> 11 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 8 -> 7 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 11 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 5 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 5 -> 11 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 8 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 6 -> 11 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 11 -> 5 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 10 -> 9 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 5 -> 10 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 13 -> 16 at (2131, 3027), 4 frames after previous cover
- f111: ref 78897: 9 -> 10 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 10 -> 5 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 5 -> 6 at (1994.5, 3035), 2 frames after previous cover
- f111: ref 79097: 12 -> 19 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 8 -> 12 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 7 -> 20 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 7 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 8 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 13 -> 7 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 13 -> 16 at (2142, 3026.5), 2 frames after previous cover
- f112: ref 79102: 8 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 6 -> 11 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 20 -> 21 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 21 -> 7 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 9 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 19 -> 9 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 12 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 21 -> 12 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 7 -> 21 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 8 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 7 -> 8 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 16 -> 7 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 13 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 6 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 11 -> 4 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 6 -> 11 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 6 -> 10 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 10 -> 9 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 5 -> 6 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 11 -> 5 at (1963.5, 3035.5), 1 frames after previous cover
- ... 622 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 796 | 163 | 3 (796) |
| 78896 | 350 (76..429) | 276 | 54 | 4 (143), 32 (110), 11 (23) |
| 78969 | 352 (80..434) | 279 | 51 | 9 (108), 25 (102), 11 (20), 4 (15), 5 (14), 6 (10), 19 (9), 32 (1) |
| 78971 | 352 (84..439) | 281 | 49 | 11 (192), 5 (27), 6 (14), 25 (13), 9 (13), 19 (13), 32 (8), 4 (1) |
| 79045 | 355 (84..443) | 286 | 44 | 19 (191), 11 (36), 5 (23), 9 (13), 32 (10), 6 (4), 4 (4), 25 (3), 10 (2) |
| 79037 | 355 (86..445) | 283 | 61 | 4 (109), 9 (108), 11 (16), 25 (13), 10 (9), 19 (9), 5 (8), 6 (5), 7 (3), 8 (2), 32 (1) |
| 78897 | 345 (89..450) | 279 | 49 | 25 (129), 6 (33), 9 (28), 19 (24), 30 (21), 4 (14), 10 (12), 5 (9), 32 (3), 7 (2), 8 (2), 11 (2) |
| 78899 | 365 (91..455) | 290 | 57 | 30 (181), 10 (32), 6 (22), 4 (14), 9 (13), 19 (9), 5 (9), 7 (3), 8 (2), 32 (2), 25 (2), 12 (1) |
| 79097 | 366 (94..461) | 295 | 60 | 5 (119), 32 (88), 10 (21), 30 (18), 12 (11), 19 (11), 31 (10), 9 (8), 7 (3), 25 (3), 6 (2), 8 (1) |
| 79098 | 360 (97..467) | 279 | 60 | 21 (92), 31 (76), 5 (32), 32 (21), 6 (20), 10 (13), 12 (7), 19 (7), 8 (5), 9 (3), 7 (2), 30 (1) |
| 79102 | 371 (98..477) | 299 | 61 | 10 (124), 21 (61), 5 (47), 31 (27), 6 (15), 8 (6), 12 (6), 30 (6), 7 (2), 20 (2), 32 (2), 19 (1) |
| 79103 | 380 (99..481) | 299 | 59 | 12 (117), 21 (60), 10 (41), 31 (29), 6 (16), 5 (16), 30 (6), 19 (5), 32 (4), 7 (2), 20 (2), 13 (1) |
| 79105 | 379 (101..484) | 293 | 65 | 31 (116), 10 (56), 12 (38), 21 (29), 30 (22), 7 (9), 5 (9), 19 (6), 6 (5), 13 (1), 20 (1), 32 (1) |
| 79108 | 385 (104..492) | 295 | 64 | 27 (134), 12 (71), 21 (50), 31 (12), 20 (9), 6 (5), 8 (4), 16 (3), 30 (3), 10 (2), 13 (1), 33 (1) |
| 79110 | 388 (106..497) | 313 | 57 | 29 (130), 27 (75), 33 (45), 12 (26), 16 (12), 31 (6), 8 (5), 30 (5), 20 (4), 13 (2), 7 (2), 6 (1) |
| 79111 | 386 (109..500) | 306 | 65 | 28 (115), 16 (65), 12 (49), 29 (31), 27 (15), 33 (14), 8 (8), 7 (4), 30 (3), 13 (1), 6 (1) |
| 79115 | 421 (111..531) | 320 | 69 | 16 (145), 29 (110), 33 (17), 28 (17), 8 (13), 20 (5), 13 (3), 7 (3), 12 (3), 27 (2), 31 (1), 6 (1) |
| 79116 | 411 (114..530) | 334 | 58 | 7 (130), 28 (72), 20 (35), 27 (30), 29 (28), 8 (17), 33 (7), 13 (6), 6 (5), 16 (4) |
| 79122 | 404 (118..532) | 324 | 64 | 20 (157), 8 (48), 6 (48), 28 (38), 16 (15), 29 (6), 7 (4), 33 (4), 13 (2), 27 (2) |
| 79132 | 391 (120..515) | 308 | 53 | 6 (145), 8 (107), 27 (33), 20 (14), 16 (3), 7 (3), 28 (2), 13 (1) |
| 79128 | 402 (124..527) | 314 | 65 | 37 (115), 20 (113), 8 (26), 28 (25), 7 (11), 6 (8), 13 (7), 27 (5), 16 (4) |
| 79134 | 407 (127..533) | 334 | 64 | 8 (132), 13 (97), 16 (36), 28 (31), 7 (22), 27 (9), 33 (5), 36 (2) |
| 79135 | 409 (129..542) | 332 | 58 | 13 (156), 33 (65), 16 (45), 7 (30), 36 (23), 28 (11), 27 (2) |
| 79139 | 406 (132..537) | 312 | 65 | 36 (183), 13 (68), 33 (43), 7 (10), 16 (8) |
| 79136 | 393 (136..538) | 312 | 64 | 7 (133), 33 (123), 36 (42), 13 (14) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 145/368/1001; tracks with internal gaps: 2; total internal gaps: 2; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 796 | 796 | 0 | 0 | 0 | 0 | 78911 |
| 4 | 78..445 | 368 | 300 | 300 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 5 | 82..461 | 380 | 313 | 313 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 6 | 86..515 | 430 | 361 | 360 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 7 | 86..530 | 445 | 378 | 378 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..533 | 445 | 378 | 378 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 91..434 | 344 | 294 | 294 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 10 | 93..477 | 385 | 312 | 312 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 97..439 | 343 | 289 | 289 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 12 | 100..481 | 382 | 329 | 329 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 13 | 100..542 | 443 | 360 | 360 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 108..532 | 425 | 340 | 340 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 111..443 | 333 | 285 | 285 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 111..531 | 421 | 342 | 342 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..467 | 357 | 292 | 292 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 25 | 126..450 | 325 | 265 | 265 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 27 | 129..492 | 364 | 307 | 307 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 28 | 130..500 | 371 | 311 | 311 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 130..497 | 368 | 305 | 305 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 30 | 133..455 | 323 | 266 | 266 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 31 | 133..484 | 352 | 278 | 277 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 32 | 138..429 | 292 | 251 | 251 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 33 | 138..537 | 400 | 324 | 324 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 36 | 213..537 | 325 | 250 | 250 | 0 | 0 | 0 | 0 | 79134, 79135, 79136, 79139 |
| 37 | 383..527 | 145 | 115 | 115 | 0 | 0 | 0 | 0 | 79128 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9266; unmatched reference entries: 876; unmatched candidate entries: 1197
- identity switches: 689; fragmentation (coverage interruptions): 628; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 7 -> 8 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 7 -> 8 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 8 -> 9 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 8 -> 9 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 8 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 9 -> 10 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 10 -> 11 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 7 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 9 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 8 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 10 -> 11 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 5 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 7 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 5 -> 6 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 8 -> 12 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 13 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 8 at (2124.5, 3027.5), 3 frames after previous cover
- f103: ref 79105: 13 -> 7 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 6 -> 11 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 8 -> 7 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 11 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 5 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 5 -> 11 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 8 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 6 -> 11 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 11 -> 5 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 10 -> 9 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 5 -> 10 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 13 -> 16 at (2131, 3027), 3 frames after previous cover
- f111: ref 78897: 9 -> 10 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 10 -> 5 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 5 -> 6 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 12 -> 19 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 8 -> 12 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 7 -> 20 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 7 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 8 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 13 -> 7 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 13 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 8 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 6 -> 11 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 20 -> 21 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 21 -> 7 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 9 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 19 -> 9 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 12 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 21 -> 12 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 7 -> 21 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 8 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 7 -> 8 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 16 -> 7 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 13 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 6 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 11 -> 4 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 6 -> 11 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 6 -> 10 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 10 -> 9 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 5 -> 6 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 11 -> 5 at (1963.5, 3035.5), 1 frames after previous cover
- ... 629 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 979 | 19 | 3 (979) |
| 78896 | 350 (76..429) | 314 | 21 | 4 (159), 32 (128), 11 (27) |
| 78969 | 352 (80..434) | 308 | 31 | 9 (120), 25 (112), 11 (20), 4 (18), 5 (15), 19 (12), 6 (10), 32 (1) |
| 78971 | 352 (84..439) | 319 | 20 | 11 (224), 5 (31), 6 (15), 9 (14), 25 (13), 19 (13), 32 (8), 4 (1) |
| 79045 | 355 (84..443) | 313 | 23 | 19 (211), 11 (40), 5 (24), 9 (14), 32 (12), 6 (4), 4 (4), 10 (2), 25 (2) |
| 79037 | 355 (86..445) | 323 | 28 | 4 (132), 9 (119), 11 (18), 25 (15), 19 (10), 10 (9), 5 (8), 6 (6), 7 (3), 8 (2), 32 (1) |
| 78897 | 345 (89..450) | 305 | 32 | 25 (146), 6 (36), 9 (29), 19 (24), 30 (22), 4 (15), 10 (13), 5 (10), 8 (3), 32 (3), 7 (2), 11 (2) |
| 78899 | 365 (91..455) | 330 | 28 | 30 (207), 10 (36), 6 (22), 4 (16), 9 (14), 19 (11), 5 (10), 8 (4), 25 (4), 7 (3), 32 (2), 12 (1) |
| 79097 | 366 (94..461) | 340 | 21 | 5 (149), 32 (93), 10 (23), 30 (22), 31 (13), 12 (11), 19 (11), 9 (9), 7 (3), 25 (3), 6 (2), 8 (1) |
| 79098 | 360 (97..467) | 320 | 29 | 21 (110), 31 (91), 5 (34), 32 (24), 6 (21), 10 (13), 12 (8), 19 (7), 8 (6), 9 (3), 7 (2), 30 (1) |
| 79102 | 371 (98..477) | 341 | 25 | 10 (147), 21 (66), 5 (53), 31 (33), 6 (16), 8 (6), 12 (6), 30 (6), 7 (3), 20 (2), 32 (2), 19 (1) |
| 79103 | 380 (99..481) | 340 | 26 | 12 (137), 21 (69), 10 (49), 31 (30), 6 (17), 5 (17), 30 (6), 19 (5), 32 (5), 7 (2), 20 (2), 13 (1) |
| 79105 | 379 (101..484) | 343 | 25 | 31 (141), 10 (66), 12 (40), 21 (36), 30 (27), 5 (10), 7 (9), 19 (6), 6 (5), 13 (1), 20 (1), 32 (1) |
| 79108 | 385 (104..492) | 338 | 32 | 27 (163), 12 (78), 21 (54), 31 (12), 20 (9), 8 (5), 6 (5), 16 (3), 30 (3), 10 (3), 13 (2), 33 (1) |
| 79110 | 388 (106..497) | 353 | 25 | 29 (155), 27 (77), 33 (54), 12 (27), 16 (14), 31 (7), 8 (5), 30 (5), 20 (4), 13 (2), 7 (2), 6 (1) |
| 79111 | 386 (109..500) | 354 | 23 | 28 (135), 16 (75), 12 (56), 29 (35), 33 (17), 27 (17), 8 (8), 7 (5), 30 (3), 13 (2), 6 (1) |
| 79115 | 421 (111..531) | 375 | 30 | 16 (180), 29 (121), 33 (20), 28 (19), 8 (14), 7 (5), 20 (5), 13 (3), 12 (3), 27 (2), 6 (2), 31 (1) |
| 79116 | 411 (114..530) | 380 | 25 | 7 (152), 28 (83), 20 (38), 27 (31), 29 (30), 8 (18), 16 (9), 33 (7), 13 (6), 6 (6) |
| 79122 | 404 (118..532) | 371 | 22 | 20 (189), 6 (54), 8 (53), 28 (42), 16 (12), 29 (9), 7 (4), 33 (4), 13 (2), 27 (2) |
| 79132 | 391 (120..515) | 345 | 30 | 6 (163), 8 (120), 27 (38), 20 (14), 16 (3), 7 (3), 28 (3), 13 (1) |
| 79128 | 402 (124..527) | 373 | 22 | 20 (140), 37 (137), 8 (32), 28 (27), 7 (12), 6 (9), 13 (7), 27 (5), 16 (4) |
| 79134 | 407 (127..533) | 384 | 20 | 8 (152), 13 (115), 16 (43), 28 (34), 7 (23), 27 (9), 36 (4), 33 (4) |
| 79135 | 409 (129..542) | 381 | 22 | 13 (183), 33 (75), 16 (50), 7 (33), 36 (25), 28 (12), 27 (3) |
| 79139 | 406 (132..537) | 368 | 31 | 36 (271), 13 (75), 16 (12), 7 (10) |
| 79136 | 393 (136..538) | 369 | 18 | 33 (205), 7 (147), 13 (17) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 174/397/1001; tracks with internal gaps: 25; total internal gaps: 387; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 691)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 1001 | 979 | 22 | 19 | 2 | 0 | 78911 |
| 4 | 78..474 | 397 | 397 | 345 | 52 | 18 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 5 | 82..490 | 409 | 409 | 361 | 48 | 16 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 6 | 86..544 | 459 | 459 | 395 | 64 | 23 | 5 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 7 | 86..559 | 474 | 474 | 423 | 51 | 18 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..562 | 474 | 474 | 429 | 45 | 12 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 91..463 | 373 | 373 | 322 | 51 | 19 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 10 | 93..506 | 414 | 414 | 361 | 53 | 19 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 97..468 | 372 | 372 | 331 | 41 | 9 | 2 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 12 | 100..510 | 411 | 411 | 367 | 44 | 12 | 3 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 13 | 100..571 | 472 | 472 | 417 | 55 | 22 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 108..561 | 454 | 454 | 405 | 49 | 16 | 4 | 24 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 111..472 | 362 | 362 | 311 | 51 | 14 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 111..560 | 450 | 450 | 404 | 46 | 15 | 2 | 28 | 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..496 | 386 | 386 | 335 | 51 | 16 | 4 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 25 | 126..479 | 354 | 354 | 295 | 59 | 24 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 27 | 129..521 | 393 | 393 | 347 | 46 | 13 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 28 | 130..529 | 400 | 400 | 355 | 45 | 14 | 3 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 130..526 | 397 | 397 | 350 | 47 | 12 | 3 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 30 | 133..484 | 352 | 352 | 302 | 50 | 17 | 3 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 31 | 133..513 | 381 | 381 | 328 | 53 | 16 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 32 | 138..458 | 321 | 321 | 280 | 41 | 10 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 33 | 138..566 | 429 | 429 | 387 | 42 | 12 | 2 | 28 | 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79136 |
| 36 | 213..566 | 354 | 354 | 300 | 54 | 16 | 4 | 31 | 79134, 79135, 79139 |
| 37 | 383..556 | 174 | 174 | 137 | 37 | 5 | 3 | 29 | 79128 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9266; unmatched reference entries: 876; unmatched candidate entries: 1197
- identity switches: 689; fragmentation (coverage interruptions): 628; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 7 -> 8 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 7 -> 8 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 8 -> 9 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 8 -> 9 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 8 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 9 -> 10 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 10 -> 11 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 7 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 9 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 8 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 10 -> 11 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 5 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 7 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 5 -> 6 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 8 -> 12 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 13 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 8 at (2124.5, 3027.5), 3 frames after previous cover
- f103: ref 79105: 13 -> 7 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 6 -> 11 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 8 -> 7 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 11 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 5 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 5 -> 11 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 8 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 6 -> 11 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 11 -> 5 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 10 -> 9 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 5 -> 10 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 13 -> 16 at (2131, 3027), 3 frames after previous cover
- f111: ref 78897: 9 -> 10 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 10 -> 5 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 5 -> 6 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 12 -> 19 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 8 -> 12 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 7 -> 20 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 7 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 8 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 13 -> 7 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 13 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 8 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 6 -> 11 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 20 -> 21 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 21 -> 7 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 9 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 19 -> 9 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 12 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 21 -> 12 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 7 -> 21 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 8 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 7 -> 8 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 16 -> 7 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 13 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 6 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 11 -> 4 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 6 -> 11 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 6 -> 10 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 10 -> 9 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 5 -> 6 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 11 -> 5 at (1963.5, 3035.5), 1 frames after previous cover
- ... 629 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 979 | 19 | 3 (979) |
| 78896 | 350 (76..429) | 314 | 21 | 4 (159), 32 (128), 11 (27) |
| 78969 | 352 (80..434) | 308 | 31 | 9 (120), 25 (112), 11 (20), 4 (18), 5 (15), 19 (12), 6 (10), 32 (1) |
| 78971 | 352 (84..439) | 319 | 20 | 11 (224), 5 (31), 6 (15), 9 (14), 25 (13), 19 (13), 32 (8), 4 (1) |
| 79045 | 355 (84..443) | 313 | 23 | 19 (211), 11 (40), 5 (24), 9 (14), 32 (12), 6 (4), 4 (4), 10 (2), 25 (2) |
| 79037 | 355 (86..445) | 323 | 28 | 4 (132), 9 (119), 11 (18), 25 (15), 19 (10), 10 (9), 5 (8), 6 (6), 7 (3), 8 (2), 32 (1) |
| 78897 | 345 (89..450) | 305 | 32 | 25 (146), 6 (36), 9 (29), 19 (24), 30 (22), 4 (15), 10 (13), 5 (10), 8 (3), 32 (3), 7 (2), 11 (2) |
| 78899 | 365 (91..455) | 330 | 28 | 30 (207), 10 (36), 6 (22), 4 (16), 9 (14), 19 (11), 5 (10), 8 (4), 25 (4), 7 (3), 32 (2), 12 (1) |
| 79097 | 366 (94..461) | 340 | 21 | 5 (149), 32 (93), 10 (23), 30 (22), 31 (13), 12 (11), 19 (11), 9 (9), 7 (3), 25 (3), 6 (2), 8 (1) |
| 79098 | 360 (97..467) | 320 | 29 | 21 (110), 31 (91), 5 (34), 32 (24), 6 (21), 10 (13), 12 (8), 19 (7), 8 (6), 9 (3), 7 (2), 30 (1) |
| 79102 | 371 (98..477) | 341 | 25 | 10 (147), 21 (66), 5 (53), 31 (33), 6 (16), 8 (6), 12 (6), 30 (6), 7 (3), 20 (2), 32 (2), 19 (1) |
| 79103 | 380 (99..481) | 340 | 26 | 12 (137), 21 (69), 10 (49), 31 (30), 6 (17), 5 (17), 30 (6), 19 (5), 32 (5), 7 (2), 20 (2), 13 (1) |
| 79105 | 379 (101..484) | 343 | 25 | 31 (141), 10 (66), 12 (40), 21 (36), 30 (27), 5 (10), 7 (9), 19 (6), 6 (5), 13 (1), 20 (1), 32 (1) |
| 79108 | 385 (104..492) | 338 | 32 | 27 (163), 12 (78), 21 (54), 31 (12), 20 (9), 8 (5), 6 (5), 16 (3), 30 (3), 10 (3), 13 (2), 33 (1) |
| 79110 | 388 (106..497) | 353 | 25 | 29 (155), 27 (77), 33 (54), 12 (27), 16 (14), 31 (7), 8 (5), 30 (5), 20 (4), 13 (2), 7 (2), 6 (1) |
| 79111 | 386 (109..500) | 354 | 23 | 28 (135), 16 (75), 12 (56), 29 (35), 33 (17), 27 (17), 8 (8), 7 (5), 30 (3), 13 (2), 6 (1) |
| 79115 | 421 (111..531) | 375 | 30 | 16 (180), 29 (121), 33 (20), 28 (19), 8 (14), 7 (5), 20 (5), 13 (3), 12 (3), 27 (2), 6 (2), 31 (1) |
| 79116 | 411 (114..530) | 380 | 25 | 7 (152), 28 (83), 20 (38), 27 (31), 29 (30), 8 (18), 16 (9), 33 (7), 13 (6), 6 (6) |
| 79122 | 404 (118..532) | 371 | 22 | 20 (189), 6 (54), 8 (53), 28 (42), 16 (12), 29 (9), 7 (4), 33 (4), 13 (2), 27 (2) |
| 79132 | 391 (120..515) | 345 | 30 | 6 (163), 8 (120), 27 (38), 20 (14), 16 (3), 7 (3), 28 (3), 13 (1) |
| 79128 | 402 (124..527) | 373 | 22 | 20 (140), 37 (137), 8 (32), 28 (27), 7 (12), 6 (9), 13 (7), 27 (5), 16 (4) |
| 79134 | 407 (127..533) | 384 | 20 | 8 (152), 13 (115), 16 (43), 28 (34), 7 (23), 27 (9), 36 (4), 33 (4) |
| 79135 | 409 (129..542) | 381 | 22 | 13 (183), 33 (75), 16 (50), 7 (33), 36 (25), 28 (12), 27 (3) |
| 79139 | 406 (132..537) | 368 | 31 | 36 (271), 13 (75), 16 (12), 7 (10) |
| 79136 | 393 (136..538) | 369 | 18 | 33 (205), 7 (147), 13 (17) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 174/397/1001; tracks with internal gaps: 25; total internal gaps: 387; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 691)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 1001 | 979 | 22 | 19 | 2 | 0 | 78911 |
| 4 | 78..474 | 397 | 397 | 345 | 52 | 18 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 5 | 82..490 | 409 | 409 | 361 | 48 | 16 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 6 | 86..544 | 459 | 459 | 395 | 64 | 23 | 5 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 7 | 86..559 | 474 | 474 | 423 | 51 | 18 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..562 | 474 | 474 | 429 | 45 | 12 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 91..463 | 373 | 373 | 322 | 51 | 19 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 10 | 93..506 | 414 | 414 | 361 | 53 | 19 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 11 | 97..468 | 372 | 372 | 331 | 41 | 9 | 2 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 12 | 100..510 | 411 | 411 | 367 | 44 | 12 | 3 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 13 | 100..571 | 472 | 472 | 417 | 55 | 22 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 108..561 | 454 | 454 | 405 | 49 | 16 | 4 | 24 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 111..472 | 362 | 362 | 311 | 51 | 14 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 111..560 | 450 | 450 | 404 | 46 | 15 | 2 | 28 | 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..496 | 386 | 386 | 335 | 51 | 16 | 4 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 25 | 126..479 | 354 | 354 | 295 | 59 | 24 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 27 | 129..521 | 393 | 393 | 347 | 46 | 13 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 28 | 130..529 | 400 | 400 | 355 | 45 | 14 | 3 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 130..526 | 397 | 397 | 350 | 47 | 12 | 3 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 30 | 133..484 | 352 | 352 | 302 | 50 | 17 | 3 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 31 | 133..513 | 381 | 381 | 328 | 53 | 16 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 32 | 138..458 | 321 | 321 | 280 | 41 | 10 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 33 | 138..566 | 429 | 429 | 387 | 42 | 12 | 2 | 28 | 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79136 |
| 36 | 213..566 | 354 | 354 | 300 | 54 | 16 | 4 | 31 | 79134, 79135, 79139 |
| 37 | 383..556 | 174 | 174 | 137 | 37 | 5 | 3 | 29 | 79128 |
