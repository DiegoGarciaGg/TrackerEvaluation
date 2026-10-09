# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=e5a406457b71
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise3.0_fp0.0_seed2/tracks.csv sha256=4fda0d81c8113e47
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise3.0_fp0.0_seed2.csv sha256=e5a406457b719ce0
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise3.0_fp0.0_seed2
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
| observations | none | 4 | 0.195 | 0.107 | 0.058 | 2.42 | 0.230 | 708 | 2460.0 |
| observations | none | 6 | 0.272 | 0.150 | 0.488 | 3.22 | 0.347 | 885 | 2086.0 |
| observations | none | 8 | 0.313 | 0.174 | 0.649 | 3.63 | 0.396 | 913 | 1694.0 |
| observations | none | 12 | 0.357 | 0.206 | 0.697 | 3.98 | 0.425 | 841 | 1553.0 |
| observations | ignore | 4 | 0.195 | 0.107 | 0.058 | 2.42 | 0.230 | 708 | 2460.0 |
| observations | ignore | 6 | 0.272 | 0.150 | 0.488 | 3.22 | 0.347 | 885 | 2086.0 |
| observations | ignore | 8 | 0.313 | 0.174 | 0.649 | 3.63 | 0.396 | 913 | 1694.0 |
| observations | ignore | 12 | 0.357 | 0.206 | 0.697 | 3.98 | 0.425 | 841 | 1553.0 |
| updates | none | 4 | 0.191 | 0.109 | -0.124 | 2.43 | 0.220 | 800 | 2496.0 |
| updates | none | 6 | 0.279 | 0.160 | 0.371 | 3.29 | 0.343 | 956 | 1827.0 |
| updates | none | 8 | 0.332 | 0.193 | 0.595 | 3.78 | 0.405 | 955 | 1150.0 |
| updates | none | 12 | 0.390 | 0.235 | 0.732 | 4.38 | 0.457 | 805 | 644.0 |
| updates | ignore | 4 | 0.191 | 0.109 | -0.124 | 2.43 | 0.220 | 800 | 2496.0 |
| updates | ignore | 6 | 0.279 | 0.160 | 0.371 | 3.29 | 0.343 | 956 | 1827.0 |
| updates | ignore | 8 | 0.332 | 0.193 | 0.595 | 3.78 | 0.405 | 955 | 1150.0 |
| updates | ignore | 12 | 0.390 | 0.235 | 0.732 | 4.38 | 0.457 | 805 | 644.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7772; unmatched reference entries: 2370; unmatched candidate entries: 277
- identity switches: 913; fragmentation (coverage interruptions): 1721; orphan candidate ids (never on a reference object): 0

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
- f102: ref 78899: 9 -> 10 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 12 -> 9 at (2105, 3028.5), 2 frames after previous cover
- f103: ref 79102: 7 -> 8 at (2124.5, 3027.5), 4 frames after previous cover
- f104: ref 78899: 10 -> 9 at (2079.5, 3030.5), 2 frames after previous cover
- f104: ref 78971: 6 -> 5 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 5 -> 11 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 9 -> 12 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 5 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 11 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 11 -> 5 at (2030.5, 3033.5), 1 frames after previous cover
- f107: ref 78971: 6 -> 5 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 5 -> 11 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 9 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 13 -> 17 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 7 -> 16 at (2131, 3027), 4 frames after previous cover
- f109: ref 79110: 7 -> 16 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 9 -> 19 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 8 -> 20 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 17 -> 13 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 17 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 16 -> 18 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 7 -> 16 at (2142, 3026.5), 2 frames after previous cover
- f113: ref 79105: 13 -> 17 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 17 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 19 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 79098: 20 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 13 -> 20 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 17 -> 8 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 18 -> 13 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 16 -> 17 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 7 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 9 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 9 -> 11 at (1983, 3035), 1 frames after previous cover
- f115: ref 79045: 11 -> 5 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78969: 6 -> 4 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 5 -> 6 at (1953, 3036), 5 frames after previous cover
- f116: ref 79102: 8 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- f117: ref 79102: 19 -> 20 at (2043.5, 3029.5), 1 frames after previous cover
- f117: ref 79111: 17 -> 18 at (2109, 3027.5), 1 frames after previous cover
- f118: ref 79098: 19 -> 12 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79110: 18 -> 13 at (2090, 3026.5), 3 frames after previous cover
- f119: ref 79097: 12 -> 10 at (2004, 3029), 2 frames after previous cover
- f119: ref 79102: 20 -> 19 at (2030, 3030), 2 frames after previous cover
- f119: ref 79115: 16 -> 18 at (2114, 3021), 2 frames after previous cover
- ... 853 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 766 | 179 | 3 (766) |
| 78896 | 350 (76..429) | 270 | 60 | 4 (139), 6 (131) |
| 78969 | 352 (80..434) | 276 | 54 | 6 (123), 10 (113), 4 (26), 5 (14) |
| 78971 | 352 (84..439) | 271 | 56 | 12 (105), 10 (95), 6 (28), 11 (26), 4 (7), 5 (6), 9 (2), 20 (2) |
| 79045 | 355 (84..443) | 273 | 52 | 4 (78), 9 (66), 20 (60), 10 (30), 11 (20), 5 (13), 12 (5), 6 (1) |
| 79037 | 355 (86..445) | 273 | 63 | 20 (153), 9 (62), 4 (26), 10 (14), 11 (12), 7 (3), 8 (2), 12 (1) |
| 78897 | 345 (89..450) | 268 | 56 | 9 (133), 12 (76), 10 (20), 20 (20), 11 (8), 5 (4), 7 (2), 8 (2), 22 (2), 4 (1) |
| 78899 | 365 (91..455) | 281 | 62 | 26 (137), 11 (50), 9 (28), 5 (20), 12 (17), 20 (9), 10 (8), 19 (7), 7 (3), 8 (2) |
| 79097 | 366 (94..461) | 286 | 64 | 26 (100), 19 (90), 13 (35), 12 (25), 20 (9), 11 (9), 10 (5), 5 (5), 7 (3), 9 (2), 8 (1), 22 (1), +1 more |
| 79098 | 360 (97..467) | 270 | 68 | 19 (111), 11 (42), 12 (33), 13 (32), 26 (19), 29 (16), 8 (4), 20 (4), 5 (4), 18 (3), 7 (2) |
| 79102 | 371 (98..477) | 284 | 63 | 11 (92), 5 (56), 13 (40), 19 (38), 26 (23), 12 (12), 20 (10), 8 (8), 18 (3), 7 (1), 29 (1) |
| 79103 | 380 (99..481) | 296 | 66 | 13 (87), 5 (64), 29 (52), 11 (45), 18 (21), 19 (12), 20 (5), 12 (5), 28 (3), 22 (1), 26 (1) |
| 79105 | 379 (101..484) | 279 | 68 | 5 (88), 29 (77), 13 (41), 18 (35), 8 (13), 11 (11), 28 (5), 17 (4), 19 (3), 20 (1), 12 (1) |
| 79108 | 385 (104..492) | 290 | 70 | 29 (73), 5 (43), 22 (29), 8 (28), 27 (28), 28 (23), 24 (20), 19 (16), 18 (14), 13 (11), 16 (2), 17 (2), +1 more |
| 79110 | 388 (106..497) | 307 | 62 | 27 (76), 22 (62), 28 (58), 24 (51), 8 (33), 13 (9), 18 (7), 19 (6), 29 (3), 7 (1), 16 (1) |
| 79111 | 386 (109..500) | 288 | 69 | 24 (108), 27 (50), 29 (38), 22 (23), 28 (23), 8 (18), 18 (13), 13 (6), 16 (3), 17 (3), 19 (2), 7 (1) |
| 79115 | 421 (111..531) | 303 | 79 | 27 (101), 18 (68), 8 (32), 22 (30), 28 (25), 24 (15), 29 (13), 13 (11), 16 (5), 7 (3) |
| 79116 | 411 (114..530) | 319 | 64 | 17 (92), 28 (72), 27 (40), 24 (31), 18 (23), 13 (21), 8 (20), 22 (9), 7 (6), 29 (4), 16 (1) |
| 79122 | 404 (118..532) | 322 | 64 | 18 (162), 22 (48), 28 (29), 27 (27), 24 (26), 13 (16), 17 (7), 8 (3), 7 (2), 16 (2) |
| 79132 | 391 (120..515) | 302 | 58 | 8 (113), 31 (69), 22 (51), 24 (43), 17 (9), 13 (5), 25 (5), 16 (4), 7 (1), 27 (1), 28 (1) |
| 79128 | 402 (124..527) | 304 | 69 | 17 (120), 25 (71), 28 (71), 31 (20), 24 (8), 16 (4), 22 (4), 7 (3), 13 (2), 8 (1) |
| 79134 | 407 (127..533) | 322 | 70 | 25 (114), 8 (45), 31 (41), 7 (38), 17 (33), 22 (33), 16 (18) |
| 79135 | 409 (129..542) | 317 | 65 | 25 (136), 31 (113), 16 (54), 17 (9), 7 (5) |
| 79139 | 406 (132..537) | 304 | 67 | 16 (233), 17 (40), 7 (23), 8 (5), 25 (3) |
| 79136 | 393 (136..538) | 301 | 73 | 7 (252), 8 (33), 16 (15), 17 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 303/385/1001; tracks with internal gaps: 24; total internal gaps: 263; longest internal gap: 3; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 796 | 766 | 30 | 29 | 2 | 0 | 78911 |
| 4 | 78..439 | 362 | 290 | 277 | 13 | 13 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 5 | 82..492 | 411 | 332 | 317 | 15 | 15 | 1 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 6 | 86..429 | 344 | 288 | 283 | 5 | 5 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 7 | 86..533 | 448 | 362 | 350 | 12 | 10 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..537 | 449 | 386 | 363 | 23 | 22 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 9 | 91..455 | 365 | 302 | 293 | 9 | 8 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 10 | 93..434 | 342 | 293 | 285 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 11 | 97..481 | 385 | 327 | 315 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..443 | 344 | 287 | 280 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 13 | 100..484 | 385 | 323 | 316 | 7 | 7 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 108..537 | 430 | 352 | 342 | 10 | 10 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..521 | 414 | 330 | 320 | 10 | 10 | 1 | 0 | 79105, 79108, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 111..532 | 422 | 362 | 350 | 12 | 12 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 19 | 111..461 | 351 | 294 | 285 | 9 | 9 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 20 | 111..445 | 335 | 286 | 273 | 13 | 12 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 22 | 126..497 | 372 | 306 | 293 | 13 | 12 | 2 | 0 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 24 | 130..500 | 371 | 306 | 302 | 4 | 3 | 1 | 1 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 25 | 130..542 | 413 | 340 | 329 | 11 | 10 | 2 | 0 | 79128, 79132, 79134, 79135, 79139 |
| 26 | 133..477 | 345 | 293 | 280 | 13 | 10 | 3 | 0 | 78899, 79097, 79098, 79102, 79103 |
| 27 | 133..531 | 399 | 335 | 323 | 12 | 10 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 28 | 138..527 | 390 | 323 | 310 | 13 | 13 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 29 | 138..467 | 330 | 285 | 277 | 8 | 8 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 31 | 213..515 | 303 | 251 | 243 | 8 | 8 | 1 | 0 | 79128, 79132, 79134, 79135 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7772; unmatched reference entries: 2370; unmatched candidate entries: 277
- identity switches: 913; fragmentation (coverage interruptions): 1721; orphan candidate ids (never on a reference object): 0

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
- f102: ref 78899: 9 -> 10 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 12 -> 9 at (2105, 3028.5), 2 frames after previous cover
- f103: ref 79102: 7 -> 8 at (2124.5, 3027.5), 4 frames after previous cover
- f104: ref 78899: 10 -> 9 at (2079.5, 3030.5), 2 frames after previous cover
- f104: ref 78971: 6 -> 5 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 5 -> 11 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 9 -> 12 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 5 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 11 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 11 -> 5 at (2030.5, 3033.5), 1 frames after previous cover
- f107: ref 78971: 6 -> 5 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 5 -> 11 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 9 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 13 -> 17 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 7 -> 16 at (2131, 3027), 4 frames after previous cover
- f109: ref 79110: 7 -> 16 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 9 -> 19 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 8 -> 20 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 17 -> 13 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 17 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 16 -> 18 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 7 -> 16 at (2142, 3026.5), 2 frames after previous cover
- f113: ref 79105: 13 -> 17 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 17 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 19 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 79098: 20 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 13 -> 20 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 17 -> 8 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 18 -> 13 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 16 -> 17 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 7 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 9 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 9 -> 11 at (1983, 3035), 1 frames after previous cover
- f115: ref 79045: 11 -> 5 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78969: 6 -> 4 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 5 -> 6 at (1953, 3036), 5 frames after previous cover
- f116: ref 79102: 8 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- f117: ref 79102: 19 -> 20 at (2043.5, 3029.5), 1 frames after previous cover
- f117: ref 79111: 17 -> 18 at (2109, 3027.5), 1 frames after previous cover
- f118: ref 79098: 19 -> 12 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79110: 18 -> 13 at (2090, 3026.5), 3 frames after previous cover
- f119: ref 79097: 12 -> 10 at (2004, 3029), 2 frames after previous cover
- f119: ref 79102: 20 -> 19 at (2030, 3030), 2 frames after previous cover
- f119: ref 79115: 16 -> 18 at (2114, 3021), 2 frames after previous cover
- ... 853 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 766 | 179 | 3 (766) |
| 78896 | 350 (76..429) | 270 | 60 | 4 (139), 6 (131) |
| 78969 | 352 (80..434) | 276 | 54 | 6 (123), 10 (113), 4 (26), 5 (14) |
| 78971 | 352 (84..439) | 271 | 56 | 12 (105), 10 (95), 6 (28), 11 (26), 4 (7), 5 (6), 9 (2), 20 (2) |
| 79045 | 355 (84..443) | 273 | 52 | 4 (78), 9 (66), 20 (60), 10 (30), 11 (20), 5 (13), 12 (5), 6 (1) |
| 79037 | 355 (86..445) | 273 | 63 | 20 (153), 9 (62), 4 (26), 10 (14), 11 (12), 7 (3), 8 (2), 12 (1) |
| 78897 | 345 (89..450) | 268 | 56 | 9 (133), 12 (76), 10 (20), 20 (20), 11 (8), 5 (4), 7 (2), 8 (2), 22 (2), 4 (1) |
| 78899 | 365 (91..455) | 281 | 62 | 26 (137), 11 (50), 9 (28), 5 (20), 12 (17), 20 (9), 10 (8), 19 (7), 7 (3), 8 (2) |
| 79097 | 366 (94..461) | 286 | 64 | 26 (100), 19 (90), 13 (35), 12 (25), 20 (9), 11 (9), 10 (5), 5 (5), 7 (3), 9 (2), 8 (1), 22 (1), +1 more |
| 79098 | 360 (97..467) | 270 | 68 | 19 (111), 11 (42), 12 (33), 13 (32), 26 (19), 29 (16), 8 (4), 20 (4), 5 (4), 18 (3), 7 (2) |
| 79102 | 371 (98..477) | 284 | 63 | 11 (92), 5 (56), 13 (40), 19 (38), 26 (23), 12 (12), 20 (10), 8 (8), 18 (3), 7 (1), 29 (1) |
| 79103 | 380 (99..481) | 296 | 66 | 13 (87), 5 (64), 29 (52), 11 (45), 18 (21), 19 (12), 20 (5), 12 (5), 28 (3), 22 (1), 26 (1) |
| 79105 | 379 (101..484) | 279 | 68 | 5 (88), 29 (77), 13 (41), 18 (35), 8 (13), 11 (11), 28 (5), 17 (4), 19 (3), 20 (1), 12 (1) |
| 79108 | 385 (104..492) | 290 | 70 | 29 (73), 5 (43), 22 (29), 8 (28), 27 (28), 28 (23), 24 (20), 19 (16), 18 (14), 13 (11), 16 (2), 17 (2), +1 more |
| 79110 | 388 (106..497) | 307 | 62 | 27 (76), 22 (62), 28 (58), 24 (51), 8 (33), 13 (9), 18 (7), 19 (6), 29 (3), 7 (1), 16 (1) |
| 79111 | 386 (109..500) | 288 | 69 | 24 (108), 27 (50), 29 (38), 22 (23), 28 (23), 8 (18), 18 (13), 13 (6), 16 (3), 17 (3), 19 (2), 7 (1) |
| 79115 | 421 (111..531) | 303 | 79 | 27 (101), 18 (68), 8 (32), 22 (30), 28 (25), 24 (15), 29 (13), 13 (11), 16 (5), 7 (3) |
| 79116 | 411 (114..530) | 319 | 64 | 17 (92), 28 (72), 27 (40), 24 (31), 18 (23), 13 (21), 8 (20), 22 (9), 7 (6), 29 (4), 16 (1) |
| 79122 | 404 (118..532) | 322 | 64 | 18 (162), 22 (48), 28 (29), 27 (27), 24 (26), 13 (16), 17 (7), 8 (3), 7 (2), 16 (2) |
| 79132 | 391 (120..515) | 302 | 58 | 8 (113), 31 (69), 22 (51), 24 (43), 17 (9), 13 (5), 25 (5), 16 (4), 7 (1), 27 (1), 28 (1) |
| 79128 | 402 (124..527) | 304 | 69 | 17 (120), 25 (71), 28 (71), 31 (20), 24 (8), 16 (4), 22 (4), 7 (3), 13 (2), 8 (1) |
| 79134 | 407 (127..533) | 322 | 70 | 25 (114), 8 (45), 31 (41), 7 (38), 17 (33), 22 (33), 16 (18) |
| 79135 | 409 (129..542) | 317 | 65 | 25 (136), 31 (113), 16 (54), 17 (9), 7 (5) |
| 79139 | 406 (132..537) | 304 | 67 | 16 (233), 17 (40), 7 (23), 8 (5), 25 (3) |
| 79136 | 393 (136..538) | 301 | 73 | 7 (252), 8 (33), 16 (15), 17 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 303/385/1001; tracks with internal gaps: 24; total internal gaps: 263; longest internal gap: 3; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 796 | 766 | 30 | 29 | 2 | 0 | 78911 |
| 4 | 78..439 | 362 | 290 | 277 | 13 | 13 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 5 | 82..492 | 411 | 332 | 317 | 15 | 15 | 1 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 6 | 86..429 | 344 | 288 | 283 | 5 | 5 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 7 | 86..533 | 448 | 362 | 350 | 12 | 10 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..537 | 449 | 386 | 363 | 23 | 22 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 9 | 91..455 | 365 | 302 | 293 | 9 | 8 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 10 | 93..434 | 342 | 293 | 285 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 11 | 97..481 | 385 | 327 | 315 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..443 | 344 | 287 | 280 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 13 | 100..484 | 385 | 323 | 316 | 7 | 7 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 108..537 | 430 | 352 | 342 | 10 | 10 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..521 | 414 | 330 | 320 | 10 | 10 | 1 | 0 | 79105, 79108, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 111..532 | 422 | 362 | 350 | 12 | 12 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 19 | 111..461 | 351 | 294 | 285 | 9 | 9 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 20 | 111..445 | 335 | 286 | 273 | 13 | 12 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 22 | 126..497 | 372 | 306 | 293 | 13 | 12 | 2 | 0 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 24 | 130..500 | 371 | 306 | 302 | 4 | 3 | 1 | 1 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 25 | 130..542 | 413 | 340 | 329 | 11 | 10 | 2 | 0 | 79128, 79132, 79134, 79135, 79139 |
| 26 | 133..477 | 345 | 293 | 280 | 13 | 10 | 3 | 0 | 78899, 79097, 79098, 79102, 79103 |
| 27 | 133..531 | 399 | 335 | 323 | 12 | 10 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 28 | 138..527 | 390 | 323 | 310 | 13 | 13 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 29 | 138..467 | 330 | 285 | 277 | 8 | 8 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 31 | 213..515 | 303 | 251 | 243 | 8 | 8 | 1 | 0 | 79128, 79132, 79134, 79135 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8685; unmatched reference entries: 1457; unmatched candidate entries: 1693
- identity switches: 955; fragmentation (coverage interruptions): 1080; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 7 -> 8 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 7 -> 8 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 8 -> 9 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 8 -> 9 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 7 -> 8 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 9 -> 10 at (2105, 3034.5), 3 frames after previous cover
- f96: ref 79045: 10 -> 6 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 79045: 6 -> 11 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 79097: 7 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 9 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 8 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 10 -> 11 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 5 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 7 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 5 -> 6 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 8 -> 12 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 9 -> 10 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 12 -> 9 at (2105, 3028.5), 2 frames after previous cover
- f102: ref 79098: 8 -> 12 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 7 -> 8 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 79103: 7 -> 13 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 13 -> 7 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78899: 10 -> 9 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 78971: 6 -> 5 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 5 -> 11 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 9 -> 12 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 5 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 11 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 11 -> 5 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79098: 12 -> 8 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79105: 7 -> 13 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 78971: 6 -> 5 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 5 -> 11 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 9 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 13 -> 17 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 7 -> 16 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 7 -> 16 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 9 -> 19 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 8 -> 20 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 17 -> 13 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 17 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 16 -> 18 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 7 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f113: ref 79045: 11 -> 5 at (1982.5, 3034), 2 frames after previous cover
- f113: ref 79105: 13 -> 17 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 17 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 19 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 78971: 5 -> 11 at (1966, 3035), 2 frames after previous cover
- f114: ref 79098: 20 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 13 -> 20 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 17 -> 8 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 18 -> 13 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 16 -> 17 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 7 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 9 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 9 -> 11 at (1983, 3035), 1 frames after previous cover
- f116: ref 78969: 6 -> 4 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 11 -> 6 at (1953, 3036), 2 frames after previous cover
- f116: ref 79102: 8 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- ... 895 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 922 | 64 | 3 (922) |
| 78896 | 350 (76..429) | 295 | 38 | 4 (152), 6 (143) |
| 78969 | 352 (80..434) | 295 | 44 | 6 (131), 10 (118), 4 (31), 5 (15) |
| 78971 | 352 (84..439) | 305 | 34 | 12 (122), 10 (104), 11 (32), 6 (29), 5 (7), 4 (6), 9 (3), 20 (2) |
| 79045 | 355 (84..443) | 297 | 34 | 4 (84), 9 (75), 20 (63), 10 (33), 11 (19), 5 (15), 12 (6), 6 (2) |
| 79037 | 355 (86..445) | 300 | 45 | 20 (171), 9 (67), 4 (30), 10 (14), 11 (12), 7 (3), 8 (2), 12 (1) |
| 78897 | 345 (89..450) | 284 | 47 | 9 (143), 12 (79), 20 (23), 10 (20), 11 (8), 5 (4), 7 (2), 8 (2), 22 (2), 4 (1) |
| 78899 | 365 (91..455) | 306 | 44 | 26 (152), 11 (52), 9 (30), 5 (20), 12 (18), 20 (13), 10 (8), 19 (7), 7 (3), 8 (3) |
| 79097 | 366 (94..461) | 320 | 38 | 19 (109), 26 (107), 13 (41), 12 (24), 20 (11), 11 (9), 10 (5), 5 (5), 7 (3), 9 (2), 18 (2), 8 (1), +1 more |
| 79098 | 360 (97..467) | 297 | 47 | 19 (121), 11 (49), 12 (35), 13 (34), 29 (21), 26 (19), 5 (5), 8 (4), 20 (4), 18 (3), 7 (2) |
| 79102 | 371 (98..477) | 310 | 43 | 11 (104), 5 (56), 13 (45), 19 (43), 26 (26), 12 (12), 20 (10), 8 (9), 18 (3), 7 (1), 29 (1) |
| 79103 | 380 (99..481) | 322 | 45 | 13 (93), 5 (71), 29 (61), 11 (46), 18 (20), 19 (12), 20 (6), 12 (5), 7 (3), 28 (3), 22 (1), 26 (1) |
| 79105 | 379 (101..484) | 317 | 44 | 5 (105), 29 (81), 13 (49), 18 (38), 8 (14), 11 (14), 28 (5), 17 (4), 19 (4), 7 (1), 20 (1), 12 (1) |
| 79108 | 385 (104..492) | 320 | 51 | 29 (79), 5 (53), 22 (32), 27 (31), 8 (29), 28 (26), 24 (22), 19 (17), 18 (14), 13 (11), 7 (2), 16 (2), +1 more |
| 79110 | 388 (106..497) | 334 | 40 | 27 (81), 22 (70), 24 (61), 28 (59), 8 (32), 13 (9), 18 (7), 19 (6), 29 (6), 16 (2), 7 (1) |
| 79111 | 386 (109..500) | 323 | 43 | 24 (126), 27 (53), 29 (37), 28 (28), 22 (25), 8 (24), 18 (13), 13 (6), 16 (3), 17 (3), 7 (2), 19 (2), +1 more |
| 79115 | 421 (111..531) | 346 | 48 | 27 (122), 18 (74), 22 (34), 8 (31), 28 (29), 24 (18), 29 (14), 13 (12), 16 (8), 7 (3), 17 (1) |
| 79116 | 411 (114..530) | 357 | 41 | 17 (106), 28 (79), 27 (45), 24 (30), 8 (27), 18 (27), 13 (21), 22 (10), 7 (6), 29 (4), 16 (2) |
| 79122 | 404 (118..532) | 353 | 43 | 18 (177), 22 (54), 28 (33), 27 (32), 24 (26), 13 (18), 17 (7), 7 (2), 16 (2), 8 (2) |
| 79132 | 391 (120..515) | 330 | 41 | 8 (126), 31 (76), 22 (55), 24 (45), 17 (10), 13 (5), 25 (5), 16 (4), 27 (2), 7 (1), 28 (1) |
| 79128 | 402 (124..527) | 355 | 35 | 17 (144), 25 (82), 28 (82), 31 (23), 24 (8), 22 (6), 16 (4), 7 (3), 13 (2), 8 (1) |
| 79134 | 407 (127..533) | 354 | 46 | 25 (124), 8 (49), 31 (46), 7 (40), 17 (38), 22 (38), 16 (19) |
| 79135 | 409 (129..542) | 346 | 46 | 25 (149), 31 (124), 16 (57), 17 (11), 7 (5) |
| 79139 | 406 (132..537) | 353 | 40 | 16 (265), 17 (43), 7 (22), 8 (20), 18 (2), 25 (1) |
| 79136 | 393 (136..538) | 344 | 39 | 7 (293), 16 (26), 8 (23), 17 (1), 25 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 332/414/1001; tracks with internal gaps: 24; total internal gaps: 813; longest internal gap: 12; tracks ending in coasting: 23 (trailing rows total 617)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 1001 | 922 | 79 | 64 | 3 | 0 | 78911 |
| 4 | 78..468 | 391 | 391 | 304 | 87 | 38 | 4 | 30 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 5 | 82..521 | 440 | 440 | 357 | 83 | 42 | 7 | 21 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 6 | 86..458 | 373 | 373 | 305 | 68 | 32 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 7 | 86..562 | 477 | 477 | 398 | 79 | 39 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..566 | 478 | 478 | 399 | 79 | 39 | 3 | 32 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 9 | 91..484 | 394 | 394 | 320 | 74 | 32 | 3 | 35 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 10 | 93..463 | 371 | 371 | 302 | 69 | 31 | 4 | 24 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 11 | 97..510 | 414 | 414 | 345 | 69 | 36 | 3 | 26 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..472 | 373 | 373 | 303 | 70 | 31 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 13 | 100..513 | 414 | 414 | 346 | 68 | 31 | 3 | 32 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 108..566 | 459 | 459 | 394 | 65 | 33 | 2 | 28 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..550 | 443 | 443 | 370 | 73 | 34 | 12 | 16 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 111..561 | 451 | 451 | 380 | 71 | 37 | 3 | 24 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79139 |
| 19 | 111..490 | 380 | 380 | 321 | 59 | 27 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 20 | 111..474 | 364 | 364 | 304 | 60 | 29 | 4 | 19 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 22 | 126..526 | 401 | 401 | 328 | 73 | 33 | 3 | 29 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 24 | 130..529 | 400 | 400 | 336 | 64 | 27 | 3 | 30 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 25 | 130..571 | 442 | 442 | 362 | 80 | 38 | 4 | 34 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 26 | 133..506 | 374 | 374 | 305 | 69 | 27 | 5 | 29 | 78899, 79097, 79098, 79102, 79103 |
| 27 | 133..560 | 428 | 428 | 366 | 62 | 23 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 28 | 138..556 | 419 | 419 | 345 | 74 | 33 | 3 | 32 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 29 | 138..496 | 359 | 359 | 304 | 55 | 23 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 31 | 213..544 | 332 | 332 | 269 | 63 | 34 | 12 | 2 | 79128, 79132, 79134, 79135 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8685; unmatched reference entries: 1457; unmatched candidate entries: 1693
- identity switches: 955; fragmentation (coverage interruptions): 1080; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 7 -> 8 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 7 -> 8 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 8 -> 9 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 8 -> 9 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 7 -> 8 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 9 -> 10 at (2105, 3034.5), 3 frames after previous cover
- f96: ref 79045: 10 -> 6 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 79045: 6 -> 11 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 79097: 7 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 9 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 8 -> 9 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 10 -> 11 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 5 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 7 -> 8 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 5 -> 6 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 8 -> 12 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 9 -> 10 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 12 -> 9 at (2105, 3028.5), 2 frames after previous cover
- f102: ref 79098: 8 -> 12 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 7 -> 8 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 79103: 7 -> 13 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 13 -> 7 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78899: 10 -> 9 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 78971: 6 -> 5 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 11 -> 10 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 5 -> 11 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 9 -> 12 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 5 -> 6 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 10 -> 11 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 11 -> 5 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79098: 12 -> 8 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79105: 7 -> 13 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 78971: 6 -> 5 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 5 -> 11 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 9 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 13 -> 17 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 7 -> 16 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 7 -> 16 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 9 -> 19 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 8 -> 20 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 17 -> 13 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 16 -> 17 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 16 -> 18 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 7 -> 16 at (2142, 3026.5), 1 frames after previous cover
- f113: ref 79045: 11 -> 5 at (1982.5, 3034), 2 frames after previous cover
- f113: ref 79105: 13 -> 17 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 17 -> 18 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 19 -> 10 at (2018, 3031), 1 frames after previous cover
- f114: ref 78971: 5 -> 11 at (1966, 3035), 2 frames after previous cover
- f114: ref 79098: 20 -> 19 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 13 -> 20 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 17 -> 8 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 18 -> 13 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 16 -> 17 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 7 -> 16 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 10 -> 9 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 9 -> 11 at (1983, 3035), 1 frames after previous cover
- f116: ref 78969: 6 -> 4 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 11 -> 6 at (1953, 3036), 2 frames after previous cover
- f116: ref 79102: 8 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- ... 895 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 922 | 64 | 3 (922) |
| 78896 | 350 (76..429) | 295 | 38 | 4 (152), 6 (143) |
| 78969 | 352 (80..434) | 295 | 44 | 6 (131), 10 (118), 4 (31), 5 (15) |
| 78971 | 352 (84..439) | 305 | 34 | 12 (122), 10 (104), 11 (32), 6 (29), 5 (7), 4 (6), 9 (3), 20 (2) |
| 79045 | 355 (84..443) | 297 | 34 | 4 (84), 9 (75), 20 (63), 10 (33), 11 (19), 5 (15), 12 (6), 6 (2) |
| 79037 | 355 (86..445) | 300 | 45 | 20 (171), 9 (67), 4 (30), 10 (14), 11 (12), 7 (3), 8 (2), 12 (1) |
| 78897 | 345 (89..450) | 284 | 47 | 9 (143), 12 (79), 20 (23), 10 (20), 11 (8), 5 (4), 7 (2), 8 (2), 22 (2), 4 (1) |
| 78899 | 365 (91..455) | 306 | 44 | 26 (152), 11 (52), 9 (30), 5 (20), 12 (18), 20 (13), 10 (8), 19 (7), 7 (3), 8 (3) |
| 79097 | 366 (94..461) | 320 | 38 | 19 (109), 26 (107), 13 (41), 12 (24), 20 (11), 11 (9), 10 (5), 5 (5), 7 (3), 9 (2), 18 (2), 8 (1), +1 more |
| 79098 | 360 (97..467) | 297 | 47 | 19 (121), 11 (49), 12 (35), 13 (34), 29 (21), 26 (19), 5 (5), 8 (4), 20 (4), 18 (3), 7 (2) |
| 79102 | 371 (98..477) | 310 | 43 | 11 (104), 5 (56), 13 (45), 19 (43), 26 (26), 12 (12), 20 (10), 8 (9), 18 (3), 7 (1), 29 (1) |
| 79103 | 380 (99..481) | 322 | 45 | 13 (93), 5 (71), 29 (61), 11 (46), 18 (20), 19 (12), 20 (6), 12 (5), 7 (3), 28 (3), 22 (1), 26 (1) |
| 79105 | 379 (101..484) | 317 | 44 | 5 (105), 29 (81), 13 (49), 18 (38), 8 (14), 11 (14), 28 (5), 17 (4), 19 (4), 7 (1), 20 (1), 12 (1) |
| 79108 | 385 (104..492) | 320 | 51 | 29 (79), 5 (53), 22 (32), 27 (31), 8 (29), 28 (26), 24 (22), 19 (17), 18 (14), 13 (11), 7 (2), 16 (2), +1 more |
| 79110 | 388 (106..497) | 334 | 40 | 27 (81), 22 (70), 24 (61), 28 (59), 8 (32), 13 (9), 18 (7), 19 (6), 29 (6), 16 (2), 7 (1) |
| 79111 | 386 (109..500) | 323 | 43 | 24 (126), 27 (53), 29 (37), 28 (28), 22 (25), 8 (24), 18 (13), 13 (6), 16 (3), 17 (3), 7 (2), 19 (2), +1 more |
| 79115 | 421 (111..531) | 346 | 48 | 27 (122), 18 (74), 22 (34), 8 (31), 28 (29), 24 (18), 29 (14), 13 (12), 16 (8), 7 (3), 17 (1) |
| 79116 | 411 (114..530) | 357 | 41 | 17 (106), 28 (79), 27 (45), 24 (30), 8 (27), 18 (27), 13 (21), 22 (10), 7 (6), 29 (4), 16 (2) |
| 79122 | 404 (118..532) | 353 | 43 | 18 (177), 22 (54), 28 (33), 27 (32), 24 (26), 13 (18), 17 (7), 7 (2), 16 (2), 8 (2) |
| 79132 | 391 (120..515) | 330 | 41 | 8 (126), 31 (76), 22 (55), 24 (45), 17 (10), 13 (5), 25 (5), 16 (4), 27 (2), 7 (1), 28 (1) |
| 79128 | 402 (124..527) | 355 | 35 | 17 (144), 25 (82), 28 (82), 31 (23), 24 (8), 22 (6), 16 (4), 7 (3), 13 (2), 8 (1) |
| 79134 | 407 (127..533) | 354 | 46 | 25 (124), 8 (49), 31 (46), 7 (40), 17 (38), 22 (38), 16 (19) |
| 79135 | 409 (129..542) | 346 | 46 | 25 (149), 31 (124), 16 (57), 17 (11), 7 (5) |
| 79139 | 406 (132..537) | 353 | 40 | 16 (265), 17 (43), 7 (22), 8 (20), 18 (2), 25 (1) |
| 79136 | 393 (136..538) | 344 | 39 | 7 (293), 16 (26), 8 (23), 17 (1), 25 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 332/414/1001; tracks with internal gaps: 24; total internal gaps: 813; longest internal gap: 12; tracks ending in coasting: 23 (trailing rows total 617)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8..1008 | 1001 | 1001 | 922 | 79 | 64 | 3 | 0 | 78911 |
| 4 | 78..468 | 391 | 391 | 304 | 87 | 38 | 4 | 30 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 5 | 82..521 | 440 | 440 | 357 | 83 | 42 | 7 | 21 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 6 | 86..458 | 373 | 373 | 305 | 68 | 32 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 7 | 86..562 | 477 | 477 | 398 | 79 | 39 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..566 | 478 | 478 | 399 | 79 | 39 | 3 | 32 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 9 | 91..484 | 394 | 394 | 320 | 74 | 32 | 3 | 35 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 10 | 93..463 | 371 | 371 | 302 | 69 | 31 | 4 | 24 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 11 | 97..510 | 414 | 414 | 345 | 69 | 36 | 3 | 26 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..472 | 373 | 373 | 303 | 70 | 31 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 13 | 100..513 | 414 | 414 | 346 | 68 | 31 | 3 | 32 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 108..566 | 459 | 459 | 394 | 65 | 33 | 2 | 28 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..550 | 443 | 443 | 370 | 73 | 34 | 12 | 16 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 111..561 | 451 | 451 | 380 | 71 | 37 | 3 | 24 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79139 |
| 19 | 111..490 | 380 | 380 | 321 | 59 | 27 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 20 | 111..474 | 364 | 364 | 304 | 60 | 29 | 4 | 19 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 22 | 126..526 | 401 | 401 | 328 | 73 | 33 | 3 | 29 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 24 | 130..529 | 400 | 400 | 336 | 64 | 27 | 3 | 30 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 25 | 130..571 | 442 | 442 | 362 | 80 | 38 | 4 | 34 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 26 | 133..506 | 374 | 374 | 305 | 69 | 27 | 5 | 29 | 78899, 79097, 79098, 79102, 79103 |
| 27 | 133..560 | 428 | 428 | 366 | 62 | 23 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 28 | 138..556 | 419 | 419 | 345 | 74 | 33 | 3 | 32 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 29 | 138..496 | 359 | 359 | 304 | 55 | 23 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 31 | 213..544 | 332 | 332 | 269 | 63 | 34 | 12 | 2 | 79128, 79132, 79134, 79135 |
