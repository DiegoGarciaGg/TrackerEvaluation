# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=96306abb137e
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise1.0_fp0.5_seed1/tracks.csv sha256=884a15773895ef3b
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise1.0_fp0.5_seed1.csv sha256=96306abb137e6ef7
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise1.0_fp0.5_seed1
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
| observations | none | 4 | 0.208 | 0.076 | 0.529 | 1.27 | 0.214 | 1534 | 2088.0 |
| observations | none | 6 | 0.222 | 0.081 | 0.530 | 1.27 | 0.215 | 1530 | 2086.0 |
| observations | none | 8 | 0.230 | 0.084 | 0.531 | 1.31 | 0.217 | 1504 | 2074.0 |
| observations | none | 12 | 0.239 | 0.090 | 0.540 | 1.67 | 0.231 | 1392 | 2016.0 |
| observations | ignore | 4 | 0.208 | 0.076 | 0.529 | 1.27 | 0.214 | 1534 | 2088.0 |
| observations | ignore | 6 | 0.222 | 0.081 | 0.530 | 1.27 | 0.215 | 1530 | 2086.0 |
| observations | ignore | 8 | 0.230 | 0.084 | 0.531 | 1.31 | 0.217 | 1504 | 2074.0 |
| observations | ignore | 12 | 0.239 | 0.090 | 0.540 | 1.67 | 0.231 | 1392 | 2016.0 |
| updates | none | 4 | 0.197 | 0.078 | 0.286 | 1.34 | 0.193 | 1560 | 1963.0 |
| updates | none | 6 | 0.224 | 0.089 | 0.381 | 1.58 | 0.212 | 1570 | 1635.0 |
| updates | none | 8 | 0.241 | 0.096 | 0.474 | 1.92 | 0.228 | 1529 | 1313.0 |
| updates | none | 12 | 0.260 | 0.106 | 0.535 | 2.50 | 0.253 | 1379 | 1097.0 |
| updates | ignore | 4 | 0.197 | 0.078 | 0.286 | 1.34 | 0.193 | 1560 | 1963.0 |
| updates | ignore | 6 | 0.224 | 0.089 | 0.381 | 1.58 | 0.212 | 1570 | 1635.0 |
| updates | ignore | 8 | 0.241 | 0.096 | 0.474 | 1.92 | 0.228 | 1529 | 1313.0 |
| updates | ignore | 12 | 0.260 | 0.106 | 0.535 | 2.50 | 0.253 | 1379 | 1097.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 6985; unmatched reference entries: 3157; unmatched candidate entries: 95
- identity switches: 1504; fragmentation (coverage interruptions): 2133; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 44 -> 49 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 42 -> 44 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 44 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 44 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 44 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 44 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 42 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 44 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 44 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 44 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 42 -> 51 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 42 -> 51 at (2124, 3028), 2 frames after previous cover
- f101: ref 79102: 57 -> 42 at (2136, 3025.5), 2 frames after previous cover
- f103: ref 78971: 60 -> 39 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 39 -> 49 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 51 -> 61 at (2100, 3028.5), 4 frames after previous cover
- f104: ref 79037: 49 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 39 -> 59 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 60 -> 39 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 57 -> 42 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f107: ref 78897: 49 -> 44 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 44 -> 61 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 78969: 56 -> 60 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79097: 61 -> 51 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 51 -> 42 at (2090, 3028), 1 frames after previous cover
- f108: ref 78969: 60 -> 59 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 79097: 51 -> 61 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 42 -> 51 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 42 -> 63 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 42 -> 64 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 61 -> 44 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 78971: 59 -> 60 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79105: 64 -> 63 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 64 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 42 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 44 -> 49 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 60 -> 59 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 49 -> 60 at (2013, 3034.5), 2 frames after previous cover
- f111: ref 79037: 60 -> 39 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 39 -> 60 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 42 -> 51 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 63 -> 61 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 57 -> 42 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 61 -> 44 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 51 -> 61 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 61 -> 63 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 42 -> 64 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 78897: 49 -> 39 at (2008.5, 3033.5), 1 frames after previous cover
- f113: ref 78899: 44 -> 60 at (2025, 3032), 2 frames after previous cover
- f113: ref 78969: 59 -> 56 at (1953.5, 3035.5), 4 frames after previous cover
- ... 1444 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 695 | 222 | 42 (392), 0 (303) |
| 78896 | 350 (76..429) | 231 | 73 | 56 (73), 108 (73), 128 (47), 39 (21), 81 (10), 72 (5), 125 (1), 82 (1) |
| 78969 | 352 (80..434) | 232 | 83 | 72 (90), 82 (33), 56 (29), 39 (22), 191 (16), 81 (12), 61 (8), 128 (7), 108 (7), 59 (6), 60 (1), 125 (1) |
| 78971 | 352 (84..439) | 227 | 80 | 56 (44), 82 (40), 72 (32), 39 (30), 59 (23), 108 (15), 81 (13), 83 (11), 191 (5), 61 (4), 49 (3), 60 (3), +2 more |
| 79045 | 355 (84..443) | 251 | 68 | 83 (57), 72 (46), 39 (27), 59 (25), 108 (23), 82 (21), 81 (20), 56 (16), 60 (10), 44 (3), 61 (2), 49 (1) |
| 79037 | 355 (86..445) | 249 | 68 | 82 (81), 39 (34), 72 (32), 56 (26), 83 (26), 59 (13), 81 (13), 60 (9), 49 (5), 44 (3), 108 (3), 42 (2), +1 more |
| 78897 | 345 (89..450) | 241 | 72 | 59 (49), 82 (33), 56 (30), 72 (24), 108 (23), 83 (17), 107 (15), 60 (11), 49 (9), 61 (9), 44 (6), 39 (6), +4 more |
| 78899 | 365 (91..455) | 253 | 79 | 107 (49), 82 (39), 56 (34), 108 (24), 59 (23), 51 (20), 83 (19), 44 (14), 128 (10), 72 (5), 85 (5), 42 (4), +3 more |
| 79097 | 366 (94..461) | 248 | 73 | 107 (98), 51 (32), 44 (24), 56 (23), 108 (21), 83 (20), 61 (13), 59 (6), 82 (4), 42 (2), 49 (2), 60 (2), +1 more |
| 79098 | 360 (97..467) | 247 | 76 | 107 (55), 59 (52), 83 (42), 51 (35), 191 (14), 44 (9), 128 (8), 82 (5), 61 (4), 76 (4), 85 (4), 108 (4), +7 more |
| 79102 | 371 (98..477) | 250 | 74 | 51 (83), 83 (40), 191 (24), 76 (20), 144 (18), 107 (12), 192 (12), 59 (11), 60 (8), 61 (7), 44 (3), 56 (3), +5 more |
| 79103 | 380 (99..481) | 267 | 75 | 76 (77), 144 (68), 51 (27), 83 (20), 192 (15), 59 (14), 42 (13), 61 (12), 128 (4), 191 (3), 56 (3), 63 (2), +5 more |
| 79105 | 379 (101..484) | 257 | 88 | 144 (79), 76 (60), 63 (27), 57 (23), 44 (17), 51 (15), 42 (11), 59 (9), 61 (5), 49 (3), 83 (3), 107 (2), +3 more |
| 79108 | 385 (104..492) | 279 | 74 | 57 (66), 63 (42), 76 (40), 59 (32), 144 (26), 42 (16), 51 (15), 69 (10), 44 (9), 61 (6), 107 (6), 64 (4), +4 more |
| 79110 | 388 (106..497) | 265 | 83 | 63 (80), 57 (70), 64 (18), 59 (17), 42 (15), 51 (11), 69 (11), 107 (11), 76 (9), 44 (6), 144 (5), 61 (3), +6 more |
| 79111 | 386 (109..500) | 267 | 87 | 63 (68), 69 (60), 57 (34), 64 (25), 60 (18), 42 (16), 51 (13), 59 (11), 44 (10), 100 (9), 49 (1), 146 (1), +1 more |
| 79115 | 421 (111..531) | 306 | 86 | 44 (52), 64 (52), 57 (36), 51 (36), 190 (25), 63 (24), 69 (19), 42 (16), 192 (16), 60 (15), 76 (6), 59 (4), +2 more |
| 79116 | 411 (114..530) | 273 | 86 | 100 (47), 44 (34), 60 (26), 42 (24), 63 (24), 51 (23), 192 (22), 190 (19), 57 (15), 69 (11), 64 (10), 59 (5), +5 more |
| 79122 | 404 (118..532) | 276 | 83 | 63 (35), 192 (34), 69 (32), 44 (32), 64 (26), 42 (24), 190 (21), 57 (20), 60 (19), 100 (10), 51 (9), 216 (7), +5 more |
| 79132 | 391 (120..515) | 271 | 79 | 190 (64), 42 (48), 44 (31), 100 (29), 69 (15), 64 (15), 57 (14), 107 (12), 63 (10), 60 (10), 49 (6), 192 (6), +4 more |
| 79128 | 402 (124..527) | 279 | 84 | 100 (66), 60 (34), 192 (31), 69 (21), 44 (20), 57 (17), 42 (16), 167 (15), 49 (13), 190 (11), 64 (9), 146 (6), +6 more |
| 79134 | 407 (127..533) | 292 | 85 | 167 (73), 60 (36), 100 (35), 64 (34), 44 (33), 69 (22), 76 (19), 57 (17), 63 (7), 49 (6), 192 (5), 42 (3), +1 more |
| 79135 | 409 (129..542) | 276 | 92 | 64 (56), 167 (49), 60 (43), 100 (29), 49 (22), 76 (18), 44 (16), 69 (12), 216 (9), 146 (8), 57 (7), 42 (3), +3 more |
| 79139 | 406 (132..537) | 268 | 91 | 60 (65), 64 (50), 167 (46), 100 (32), 44 (29), 49 (11), 76 (11), 69 (8), 42 (5), 216 (5), 125 (2), 63 (2), +2 more |
| 79136 | 393 (136..538) | 285 | 72 | 42 (54), 69 (46), 60 (45), 100 (39), 146 (39), 167 (18), 44 (15), 216 (12), 125 (6), 64 (5), 49 (4), 76 (1), +1 more |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 182 | 338..338 | 1 | 0 | 1 |
| 315 | 734..734 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/312/922; tracks with internal gaps: 21; total internal gaps: 54; longest internal gap: 4; tracks ending in coasting: 17 (trailing rows total 37)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..456 | 455 | 315 | 303 | 12 | 10 | 1 | 2 | 78911 |
| 39 | 81..256 | 176 | 146 | 143 | 3 | 1 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 42 | 87..1008 | 922 | 683 | 670 | 13 | 10 | 4 | 0 | 78897, 78899, 78911, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..537 | 449 | 371 | 369 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..222 | 132 | 103 | 100 | 3 | 1 | 1 | 2 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..484 | 392 | 327 | 327 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 98..578 | 481 | 297 | 292 | 5 | 0 | 0 | 5 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79108, 79110, 79116, 79128, 79132, 79135, 79136 |
| 57 | 99..501 | 403 | 326 | 324 | 2 | 0 | 0 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 59 | 99..464 | 366 | 302 | 300 | 2 | 1 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 60 | 99..532 | 434 | 373 | 368 | 5 | 4 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 103..192 | 90 | 77 | 75 | 2 | 0 | 0 | 2 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 63 | 108..532 | 425 | 326 | 325 | 1 | 1 | 1 | 0 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 108..563 | 456 | 314 | 305 | 9 | 3 | 1 | 6 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 113..462 | 350 | 273 | 270 | 3 | 2 | 1 | 1 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 117..428 | 312 | 240 | 236 | 4 | 4 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 76 | 125..481 | 357 | 283 | 281 | 2 | 2 | 1 | 0 | 78897, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 81 | 132..211 | 80 | 72 | 70 | 2 | 1 | 1 | 1 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 82 | 132..454 | 323 | 258 | 258 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 133..445 | 313 | 257 | 256 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 85 | 133..156 | 24 | 13 | 11 | 2 | 0 | 0 | 2 | 78899, 79098, 79102 |
| 100 | 160..537 | 378 | 302 | 300 | 2 | 2 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 107 | 176..531 | 356 | 264 | 264 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79122, 79128, 79132 |
| 108 | 179..441 | 263 | 194 | 193 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 125 | 205..292 | 88 | 20 | 15 | 5 | 1 | 1 | 4 | 78896, 78969, 79110, 79128, 79132, 79135, 79136, 79139 |
| 128 | 210..314 | 105 | 83 | 79 | 4 | 2 | 1 | 2 | 78896, 78899, 78969, 78971, 79098, 79103 |
| 144 | 243..488 | 246 | 197 | 197 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 146 | 243..349 | 107 | 65 | 63 | 2 | 0 | 0 | 2 | 79111, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 167 | 290..542 | 253 | 205 | 203 | 2 | 2 | 1 | 0 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 182 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 190 | 359..531 | 173 | 144 | 142 | 2 | 2 | 1 | 0 | 79110, 79115, 79116, 79122, 79128, 79132 |
| 191 | 359..439 | 81 | 63 | 62 | 1 | 1 | 1 | 0 | 78969, 78971, 79098, 79102, 79103 |
| 192 | 359..528 | 170 | 141 | 141 | 0 | 0 | 0 | 0 | 79102, 79103, 79115, 79116, 79122, 79128, 79132, 79134 |
| 216 | 437..493 | 57 | 44 | 43 | 1 | 0 | 0 | 1 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 315 | 734..734 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 6985; unmatched reference entries: 3157; unmatched candidate entries: 95
- identity switches: 1504; fragmentation (coverage interruptions): 2133; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 44 -> 49 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 42 -> 44 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 44 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 44 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 44 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 44 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 42 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 44 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 44 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 44 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 42 -> 51 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 42 -> 51 at (2124, 3028), 2 frames after previous cover
- f101: ref 79102: 57 -> 42 at (2136, 3025.5), 2 frames after previous cover
- f103: ref 78971: 60 -> 39 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 39 -> 49 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 51 -> 61 at (2100, 3028.5), 4 frames after previous cover
- f104: ref 79037: 49 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 39 -> 59 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 60 -> 39 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 57 -> 42 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f107: ref 78897: 49 -> 44 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 44 -> 61 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 78969: 56 -> 60 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79097: 61 -> 51 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 51 -> 42 at (2090, 3028), 1 frames after previous cover
- f108: ref 78969: 60 -> 59 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 79097: 51 -> 61 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 42 -> 51 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 42 -> 63 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 42 -> 64 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 61 -> 44 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 78971: 59 -> 60 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79105: 64 -> 63 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 64 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 42 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 44 -> 49 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 60 -> 59 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 49 -> 60 at (2013, 3034.5), 2 frames after previous cover
- f111: ref 79037: 60 -> 39 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 39 -> 60 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 42 -> 51 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 63 -> 61 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 57 -> 42 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 61 -> 44 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 51 -> 61 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 61 -> 63 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 42 -> 64 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 78897: 49 -> 39 at (2008.5, 3033.5), 1 frames after previous cover
- f113: ref 78899: 44 -> 60 at (2025, 3032), 2 frames after previous cover
- f113: ref 78969: 59 -> 56 at (1953.5, 3035.5), 4 frames after previous cover
- ... 1444 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 695 | 222 | 42 (392), 0 (303) |
| 78896 | 350 (76..429) | 231 | 73 | 56 (73), 108 (73), 128 (47), 39 (21), 81 (10), 72 (5), 125 (1), 82 (1) |
| 78969 | 352 (80..434) | 232 | 83 | 72 (90), 82 (33), 56 (29), 39 (22), 191 (16), 81 (12), 61 (8), 128 (7), 108 (7), 59 (6), 60 (1), 125 (1) |
| 78971 | 352 (84..439) | 227 | 80 | 56 (44), 82 (40), 72 (32), 39 (30), 59 (23), 108 (15), 81 (13), 83 (11), 191 (5), 61 (4), 49 (3), 60 (3), +2 more |
| 79045 | 355 (84..443) | 251 | 68 | 83 (57), 72 (46), 39 (27), 59 (25), 108 (23), 82 (21), 81 (20), 56 (16), 60 (10), 44 (3), 61 (2), 49 (1) |
| 79037 | 355 (86..445) | 249 | 68 | 82 (81), 39 (34), 72 (32), 56 (26), 83 (26), 59 (13), 81 (13), 60 (9), 49 (5), 44 (3), 108 (3), 42 (2), +1 more |
| 78897 | 345 (89..450) | 241 | 72 | 59 (49), 82 (33), 56 (30), 72 (24), 108 (23), 83 (17), 107 (15), 60 (11), 49 (9), 61 (9), 44 (6), 39 (6), +4 more |
| 78899 | 365 (91..455) | 253 | 79 | 107 (49), 82 (39), 56 (34), 108 (24), 59 (23), 51 (20), 83 (19), 44 (14), 128 (10), 72 (5), 85 (5), 42 (4), +3 more |
| 79097 | 366 (94..461) | 248 | 73 | 107 (98), 51 (32), 44 (24), 56 (23), 108 (21), 83 (20), 61 (13), 59 (6), 82 (4), 42 (2), 49 (2), 60 (2), +1 more |
| 79098 | 360 (97..467) | 247 | 76 | 107 (55), 59 (52), 83 (42), 51 (35), 191 (14), 44 (9), 128 (8), 82 (5), 61 (4), 76 (4), 85 (4), 108 (4), +7 more |
| 79102 | 371 (98..477) | 250 | 74 | 51 (83), 83 (40), 191 (24), 76 (20), 144 (18), 107 (12), 192 (12), 59 (11), 60 (8), 61 (7), 44 (3), 56 (3), +5 more |
| 79103 | 380 (99..481) | 267 | 75 | 76 (77), 144 (68), 51 (27), 83 (20), 192 (15), 59 (14), 42 (13), 61 (12), 128 (4), 191 (3), 56 (3), 63 (2), +5 more |
| 79105 | 379 (101..484) | 257 | 88 | 144 (79), 76 (60), 63 (27), 57 (23), 44 (17), 51 (15), 42 (11), 59 (9), 61 (5), 49 (3), 83 (3), 107 (2), +3 more |
| 79108 | 385 (104..492) | 279 | 74 | 57 (66), 63 (42), 76 (40), 59 (32), 144 (26), 42 (16), 51 (15), 69 (10), 44 (9), 61 (6), 107 (6), 64 (4), +4 more |
| 79110 | 388 (106..497) | 265 | 83 | 63 (80), 57 (70), 64 (18), 59 (17), 42 (15), 51 (11), 69 (11), 107 (11), 76 (9), 44 (6), 144 (5), 61 (3), +6 more |
| 79111 | 386 (109..500) | 267 | 87 | 63 (68), 69 (60), 57 (34), 64 (25), 60 (18), 42 (16), 51 (13), 59 (11), 44 (10), 100 (9), 49 (1), 146 (1), +1 more |
| 79115 | 421 (111..531) | 306 | 86 | 44 (52), 64 (52), 57 (36), 51 (36), 190 (25), 63 (24), 69 (19), 42 (16), 192 (16), 60 (15), 76 (6), 59 (4), +2 more |
| 79116 | 411 (114..530) | 273 | 86 | 100 (47), 44 (34), 60 (26), 42 (24), 63 (24), 51 (23), 192 (22), 190 (19), 57 (15), 69 (11), 64 (10), 59 (5), +5 more |
| 79122 | 404 (118..532) | 276 | 83 | 63 (35), 192 (34), 69 (32), 44 (32), 64 (26), 42 (24), 190 (21), 57 (20), 60 (19), 100 (10), 51 (9), 216 (7), +5 more |
| 79132 | 391 (120..515) | 271 | 79 | 190 (64), 42 (48), 44 (31), 100 (29), 69 (15), 64 (15), 57 (14), 107 (12), 63 (10), 60 (10), 49 (6), 192 (6), +4 more |
| 79128 | 402 (124..527) | 279 | 84 | 100 (66), 60 (34), 192 (31), 69 (21), 44 (20), 57 (17), 42 (16), 167 (15), 49 (13), 190 (11), 64 (9), 146 (6), +6 more |
| 79134 | 407 (127..533) | 292 | 85 | 167 (73), 60 (36), 100 (35), 64 (34), 44 (33), 69 (22), 76 (19), 57 (17), 63 (7), 49 (6), 192 (5), 42 (3), +1 more |
| 79135 | 409 (129..542) | 276 | 92 | 64 (56), 167 (49), 60 (43), 100 (29), 49 (22), 76 (18), 44 (16), 69 (12), 216 (9), 146 (8), 57 (7), 42 (3), +3 more |
| 79139 | 406 (132..537) | 268 | 91 | 60 (65), 64 (50), 167 (46), 100 (32), 44 (29), 49 (11), 76 (11), 69 (8), 42 (5), 216 (5), 125 (2), 63 (2), +2 more |
| 79136 | 393 (136..538) | 285 | 72 | 42 (54), 69 (46), 60 (45), 100 (39), 146 (39), 167 (18), 44 (15), 216 (12), 125 (6), 64 (5), 49 (4), 76 (1), +1 more |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 182 | 338..338 | 1 | 0 | 1 |
| 315 | 734..734 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/312/922; tracks with internal gaps: 21; total internal gaps: 54; longest internal gap: 4; tracks ending in coasting: 17 (trailing rows total 37)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..456 | 455 | 315 | 303 | 12 | 10 | 1 | 2 | 78911 |
| 39 | 81..256 | 176 | 146 | 143 | 3 | 1 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 42 | 87..1008 | 922 | 683 | 670 | 13 | 10 | 4 | 0 | 78897, 78899, 78911, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..537 | 449 | 371 | 369 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..222 | 132 | 103 | 100 | 3 | 1 | 1 | 2 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..484 | 392 | 327 | 327 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 98..578 | 481 | 297 | 292 | 5 | 0 | 0 | 5 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79108, 79110, 79116, 79128, 79132, 79135, 79136 |
| 57 | 99..501 | 403 | 326 | 324 | 2 | 0 | 0 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 59 | 99..464 | 366 | 302 | 300 | 2 | 1 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 60 | 99..532 | 434 | 373 | 368 | 5 | 4 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 103..192 | 90 | 77 | 75 | 2 | 0 | 0 | 2 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 63 | 108..532 | 425 | 326 | 325 | 1 | 1 | 1 | 0 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 108..563 | 456 | 314 | 305 | 9 | 3 | 1 | 6 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 113..462 | 350 | 273 | 270 | 3 | 2 | 1 | 1 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 117..428 | 312 | 240 | 236 | 4 | 4 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 76 | 125..481 | 357 | 283 | 281 | 2 | 2 | 1 | 0 | 78897, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 81 | 132..211 | 80 | 72 | 70 | 2 | 1 | 1 | 1 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 82 | 132..454 | 323 | 258 | 258 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 133..445 | 313 | 257 | 256 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 85 | 133..156 | 24 | 13 | 11 | 2 | 0 | 0 | 2 | 78899, 79098, 79102 |
| 100 | 160..537 | 378 | 302 | 300 | 2 | 2 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 107 | 176..531 | 356 | 264 | 264 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79122, 79128, 79132 |
| 108 | 179..441 | 263 | 194 | 193 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 125 | 205..292 | 88 | 20 | 15 | 5 | 1 | 1 | 4 | 78896, 78969, 79110, 79128, 79132, 79135, 79136, 79139 |
| 128 | 210..314 | 105 | 83 | 79 | 4 | 2 | 1 | 2 | 78896, 78899, 78969, 78971, 79098, 79103 |
| 144 | 243..488 | 246 | 197 | 197 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 146 | 243..349 | 107 | 65 | 63 | 2 | 0 | 0 | 2 | 79111, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 167 | 290..542 | 253 | 205 | 203 | 2 | 2 | 1 | 0 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 182 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 190 | 359..531 | 173 | 144 | 142 | 2 | 2 | 1 | 0 | 79110, 79115, 79116, 79122, 79128, 79132 |
| 191 | 359..439 | 81 | 63 | 62 | 1 | 1 | 1 | 0 | 78969, 78971, 79098, 79102, 79103 |
| 192 | 359..528 | 170 | 141 | 141 | 0 | 0 | 0 | 0 | 79102, 79103, 79115, 79116, 79122, 79128, 79132, 79134 |
| 216 | 437..493 | 57 | 44 | 43 | 1 | 0 | 0 | 1 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 315 | 734..734 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 8258; unmatched reference entries: 1884; unmatched candidate entries: 1918
- identity switches: 1529; fragmentation (coverage interruptions): 1258; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 44 -> 49 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 42 -> 44 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 44 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 44 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 44 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 44 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 42 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 44 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 44 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 44 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 42 -> 51 at (2122.5, 3028.5), 1 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 42 -> 51 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 57 -> 42 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78971: 60 -> 39 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 39 -> 49 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 51 -> 61 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79037: 49 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 39 -> 59 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 60 -> 39 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 57 -> 42 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f107: ref 78897: 49 -> 44 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 44 -> 61 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 78969: 56 -> 60 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79097: 61 -> 51 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 51 -> 42 at (2090, 3028), 1 frames after previous cover
- f108: ref 79097: 51 -> 61 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 42 -> 51 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 42 -> 63 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 42 -> 64 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 61 -> 44 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 78969: 60 -> 59 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 78971: 59 -> 60 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79105: 64 -> 63 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 64 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 42 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 44 -> 49 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 60 -> 59 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 49 -> 60 at (2013, 3034.5), 1 frames after previous cover
- f111: ref 79037: 60 -> 39 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 39 -> 60 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 42 -> 51 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 63 -> 61 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 57 -> 42 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 61 -> 44 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 51 -> 61 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 61 -> 63 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 42 -> 64 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 78897: 49 -> 39 at (2008.5, 3033.5), 1 frames after previous cover
- f113: ref 78899: 44 -> 60 at (2025, 3032), 2 frames after previous cover
- f113: ref 78969: 59 -> 56 at (1953.5, 3035.5), 4 frames after previous cover
- ... 1469 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 944 | 48 | 42 (514), 0 (430) |
| 78896 | 350 (76..429) | 279 | 41 | 108 (94), 56 (85), 128 (54), 39 (23), 81 (12), 72 (8), 125 (2), 82 (1) |
| 78969 | 352 (80..434) | 273 | 50 | 72 (111), 82 (39), 56 (32), 39 (22), 191 (17), 81 (13), 108 (12), 61 (9), 128 (8), 59 (6), 60 (2), 125 (2) |
| 78971 | 352 (84..439) | 270 | 49 | 56 (58), 82 (50), 72 (40), 39 (30), 59 (25), 108 (19), 81 (13), 83 (13), 191 (5), 49 (4), 61 (4), 128 (4), +3 more |
| 79045 | 355 (84..443) | 288 | 43 | 83 (71), 72 (48), 39 (30), 59 (29), 108 (29), 82 (24), 81 (21), 56 (18), 60 (11), 44 (3), 61 (3), 49 (1) |
| 79037 | 355 (86..445) | 289 | 45 | 82 (96), 72 (38), 39 (35), 56 (33), 83 (30), 59 (17), 81 (12), 60 (11), 49 (7), 44 (3), 108 (3), 42 (2), +1 more |
| 78897 | 345 (89..450) | 273 | 46 | 59 (59), 82 (36), 56 (32), 72 (27), 108 (27), 83 (20), 107 (16), 60 (13), 49 (10), 61 (9), 44 (6), 39 (6), +4 more |
| 78899 | 365 (91..455) | 297 | 48 | 107 (57), 82 (49), 56 (39), 108 (29), 59 (26), 51 (23), 83 (21), 44 (15), 128 (13), 85 (8), 72 (5), 42 (4), +3 more |
| 79097 | 366 (94..461) | 287 | 49 | 107 (118), 51 (38), 56 (29), 44 (25), 83 (23), 108 (22), 61 (13), 59 (6), 82 (4), 42 (3), 60 (3), 49 (2), +1 more |
| 79098 | 360 (97..467) | 285 | 49 | 107 (61), 59 (59), 83 (48), 51 (43), 191 (18), 44 (11), 128 (9), 76 (5), 82 (5), 61 (4), 85 (4), 108 (4), +7 more |
| 79102 | 371 (98..477) | 291 | 51 | 51 (98), 83 (44), 191 (29), 76 (23), 144 (20), 192 (17), 107 (14), 59 (12), 60 (10), 61 (8), 57 (3), 44 (3), +5 more |
| 79103 | 380 (99..481) | 305 | 46 | 76 (95), 144 (82), 51 (29), 83 (20), 192 (16), 42 (15), 59 (14), 61 (13), 128 (4), 191 (3), 56 (3), 63 (2), +5 more |
| 79105 | 379 (101..484) | 300 | 57 | 144 (93), 76 (75), 63 (29), 57 (28), 44 (18), 51 (15), 42 (11), 59 (9), 61 (5), 107 (5), 49 (3), 83 (3), +4 more |
| 79108 | 385 (104..492) | 312 | 49 | 57 (74), 63 (49), 76 (46), 59 (34), 144 (29), 42 (19), 51 (15), 69 (11), 44 (10), 107 (7), 61 (6), 64 (4), +4 more |
| 79110 | 388 (106..497) | 311 | 55 | 63 (97), 57 (78), 64 (22), 59 (21), 42 (17), 107 (14), 51 (13), 69 (13), 76 (9), 44 (8), 144 (7), 49 (3), +5 more |
| 79111 | 386 (109..500) | 317 | 47 | 63 (89), 69 (75), 57 (40), 64 (26), 60 (19), 42 (17), 51 (13), 59 (12), 44 (12), 100 (10), 76 (2), 49 (1), +1 more |
| 79115 | 421 (111..531) | 343 | 58 | 64 (64), 44 (61), 51 (38), 57 (37), 63 (27), 190 (26), 69 (19), 42 (18), 192 (18), 60 (16), 76 (7), 59 (6), +2 more |
| 79116 | 411 (114..530) | 320 | 60 | 100 (57), 44 (43), 192 (31), 42 (27), 60 (27), 63 (25), 51 (24), 57 (21), 190 (21), 69 (13), 64 (10), 59 (5), +6 more |
| 79122 | 404 (118..532) | 323 | 54 | 63 (46), 192 (41), 69 (39), 44 (37), 64 (32), 190 (25), 42 (23), 57 (22), 60 (20), 100 (12), 51 (10), 216 (10), +4 more |
| 79132 | 391 (120..515) | 305 | 58 | 190 (71), 42 (59), 44 (35), 100 (33), 69 (17), 64 (17), 107 (17), 57 (15), 60 (11), 63 (7), 49 (6), 192 (6), +4 more |
| 79128 | 402 (124..527) | 325 | 52 | 100 (81), 60 (39), 192 (34), 69 (25), 44 (24), 42 (20), 57 (18), 167 (17), 49 (15), 190 (12), 64 (11), 146 (7), +6 more |
| 79134 | 407 (127..533) | 335 | 54 | 167 (84), 60 (43), 100 (42), 44 (39), 64 (36), 69 (25), 76 (21), 57 (18), 49 (7), 63 (7), 192 (6), 42 (4), +1 more |
| 79135 | 409 (129..542) | 324 | 65 | 64 (68), 167 (57), 60 (49), 100 (34), 49 (25), 76 (22), 44 (19), 69 (14), 216 (11), 146 (9), 57 (8), 42 (3), +3 more |
| 79139 | 406 (132..537) | 324 | 48 | 60 (76), 64 (62), 167 (56), 44 (38), 100 (35), 76 (16), 49 (11), 69 (10), 42 (6), 216 (6), 63 (4), 125 (2), +2 more |
| 79136 | 393 (136..538) | 338 | 36 | 42 (68), 69 (56), 146 (54), 60 (47), 100 (43), 167 (20), 44 (17), 216 (12), 125 (8), 64 (6), 49 (4), 56 (2), +1 more |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 182 | 338..367 | 30 | 0 | 30 |
| 315 | 734..763 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/341/922; tracks with internal gaps: 30; total internal gaps: 441; longest internal gap: 29; tracks ending in coasting: 33 (trailing rows total 1205)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..485 | 484 | 484 | 430 | 54 | 15 | 2 | 37 | 78911 |
| 39 | 81..285 | 205 | 205 | 149 | 56 | 12 | 1 | 44 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 42 | 87..1008 | 922 | 922 | 838 | 84 | 42 | 29 | 0 | 78897, 78899, 78911, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..566 | 478 | 478 | 430 | 48 | 15 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..251 | 161 | 161 | 113 | 48 | 4 | 5 | 40 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..513 | 421 | 421 | 368 | 53 | 19 | 17 | 16 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 98..607 | 510 | 510 | 349 | 161 | 26 | 24 | 96 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110, 79116, 79128, 79132, 79135, 79136 |
| 57 | 99..530 | 432 | 432 | 365 | 67 | 13 | 3 | 49 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 59 | 99..493 | 395 | 395 | 340 | 55 | 18 | 3 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 60 | 99..561 | 463 | 463 | 415 | 48 | 17 | 2 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 103..221 | 119 | 119 | 79 | 40 | 0 | 0 | 40 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 63 | 108..561 | 454 | 454 | 387 | 67 | 20 | 13 | 28 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 108..592 | 485 | 485 | 359 | 126 | 19 | 12 | 91 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 113..491 | 379 | 379 | 321 | 58 | 20 | 2 | 30 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 117..457 | 341 | 341 | 279 | 62 | 21 | 13 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 76 | 125..510 | 386 | 386 | 335 | 51 | 16 | 5 | 28 | 78897, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 81 | 132..240 | 109 | 109 | 74 | 35 | 5 | 1 | 30 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 82 | 132..483 | 352 | 352 | 305 | 47 | 15 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 133..474 | 342 | 342 | 294 | 48 | 14 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 85 | 133..185 | 53 | 53 | 14 | 39 | 0 | 0 | 39 | 78899, 79098, 79102 |
| 100 | 160..566 | 407 | 407 | 350 | 57 | 20 | 3 | 29 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 107 | 176..560 | 385 | 385 | 313 | 72 | 26 | 8 | 30 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79116, 79128, 79132 |
| 108 | 179..470 | 292 | 292 | 239 | 53 | 20 | 3 | 27 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 125 | 205..321 | 117 | 117 | 21 | 96 | 3 | 11 | 82 | 78896, 78969, 78971, 79110, 79128, 79132, 79135, 79136, 79139 |
| 128 | 210..343 | 134 | 134 | 92 | 42 | 4 | 2 | 37 | 78896, 78899, 78969, 78971, 79098, 79103 |
| 144 | 243..517 | 275 | 275 | 233 | 42 | 12 | 3 | 28 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 146 | 243..378 | 136 | 136 | 82 | 54 | 11 | 2 | 41 | 79111, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 167 | 290..571 | 282 | 282 | 236 | 46 | 14 | 2 | 29 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 182 | 338..367 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 190 | 359..560 | 202 | 202 | 157 | 45 | 10 | 3 | 28 | 79110, 79115, 79116, 79122, 79128, 79132 |
| 191 | 359..468 | 110 | 110 | 72 | 38 | 4 | 3 | 32 | 78969, 78971, 79098, 79102, 79103 |
| 192 | 359..557 | 199 | 199 | 169 | 30 | 4 | 1 | 26 | 79102, 79103, 79115, 79116, 79122, 79128, 79132, 79134 |
| 216 | 437..522 | 86 | 86 | 50 | 36 | 2 | 5 | 30 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 315 | 734..763 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 8258; unmatched reference entries: 1884; unmatched candidate entries: 1918
- identity switches: 1529; fragmentation (coverage interruptions): 1258; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 44 -> 49 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 42 -> 44 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 44 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 42 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 44 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 44 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 44 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 42 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 44 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 44 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 44 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 42 -> 51 at (2122.5, 3028.5), 1 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 42 -> 51 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 57 -> 42 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78971: 60 -> 39 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 39 -> 49 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 51 -> 61 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79037: 49 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 39 -> 59 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 60 -> 39 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 57 -> 42 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f107: ref 78897: 49 -> 44 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 44 -> 61 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 78969: 56 -> 60 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79097: 61 -> 51 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 51 -> 42 at (2090, 3028), 1 frames after previous cover
- f108: ref 79097: 51 -> 61 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 42 -> 51 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 42 -> 63 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 42 -> 64 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 61 -> 44 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 78969: 60 -> 59 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 78971: 59 -> 60 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79105: 64 -> 63 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 64 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 42 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 44 -> 49 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 60 -> 59 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 49 -> 60 at (2013, 3034.5), 1 frames after previous cover
- f111: ref 79037: 60 -> 39 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 39 -> 60 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 42 -> 51 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 63 -> 61 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 57 -> 42 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 61 -> 44 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 51 -> 61 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 61 -> 63 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 42 -> 64 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 78897: 49 -> 39 at (2008.5, 3033.5), 1 frames after previous cover
- f113: ref 78899: 44 -> 60 at (2025, 3032), 2 frames after previous cover
- f113: ref 78969: 59 -> 56 at (1953.5, 3035.5), 4 frames after previous cover
- ... 1469 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 944 | 48 | 42 (514), 0 (430) |
| 78896 | 350 (76..429) | 279 | 41 | 108 (94), 56 (85), 128 (54), 39 (23), 81 (12), 72 (8), 125 (2), 82 (1) |
| 78969 | 352 (80..434) | 273 | 50 | 72 (111), 82 (39), 56 (32), 39 (22), 191 (17), 81 (13), 108 (12), 61 (9), 128 (8), 59 (6), 60 (2), 125 (2) |
| 78971 | 352 (84..439) | 270 | 49 | 56 (58), 82 (50), 72 (40), 39 (30), 59 (25), 108 (19), 81 (13), 83 (13), 191 (5), 49 (4), 61 (4), 128 (4), +3 more |
| 79045 | 355 (84..443) | 288 | 43 | 83 (71), 72 (48), 39 (30), 59 (29), 108 (29), 82 (24), 81 (21), 56 (18), 60 (11), 44 (3), 61 (3), 49 (1) |
| 79037 | 355 (86..445) | 289 | 45 | 82 (96), 72 (38), 39 (35), 56 (33), 83 (30), 59 (17), 81 (12), 60 (11), 49 (7), 44 (3), 108 (3), 42 (2), +1 more |
| 78897 | 345 (89..450) | 273 | 46 | 59 (59), 82 (36), 56 (32), 72 (27), 108 (27), 83 (20), 107 (16), 60 (13), 49 (10), 61 (9), 44 (6), 39 (6), +4 more |
| 78899 | 365 (91..455) | 297 | 48 | 107 (57), 82 (49), 56 (39), 108 (29), 59 (26), 51 (23), 83 (21), 44 (15), 128 (13), 85 (8), 72 (5), 42 (4), +3 more |
| 79097 | 366 (94..461) | 287 | 49 | 107 (118), 51 (38), 56 (29), 44 (25), 83 (23), 108 (22), 61 (13), 59 (6), 82 (4), 42 (3), 60 (3), 49 (2), +1 more |
| 79098 | 360 (97..467) | 285 | 49 | 107 (61), 59 (59), 83 (48), 51 (43), 191 (18), 44 (11), 128 (9), 76 (5), 82 (5), 61 (4), 85 (4), 108 (4), +7 more |
| 79102 | 371 (98..477) | 291 | 51 | 51 (98), 83 (44), 191 (29), 76 (23), 144 (20), 192 (17), 107 (14), 59 (12), 60 (10), 61 (8), 57 (3), 44 (3), +5 more |
| 79103 | 380 (99..481) | 305 | 46 | 76 (95), 144 (82), 51 (29), 83 (20), 192 (16), 42 (15), 59 (14), 61 (13), 128 (4), 191 (3), 56 (3), 63 (2), +5 more |
| 79105 | 379 (101..484) | 300 | 57 | 144 (93), 76 (75), 63 (29), 57 (28), 44 (18), 51 (15), 42 (11), 59 (9), 61 (5), 107 (5), 49 (3), 83 (3), +4 more |
| 79108 | 385 (104..492) | 312 | 49 | 57 (74), 63 (49), 76 (46), 59 (34), 144 (29), 42 (19), 51 (15), 69 (11), 44 (10), 107 (7), 61 (6), 64 (4), +4 more |
| 79110 | 388 (106..497) | 311 | 55 | 63 (97), 57 (78), 64 (22), 59 (21), 42 (17), 107 (14), 51 (13), 69 (13), 76 (9), 44 (8), 144 (7), 49 (3), +5 more |
| 79111 | 386 (109..500) | 317 | 47 | 63 (89), 69 (75), 57 (40), 64 (26), 60 (19), 42 (17), 51 (13), 59 (12), 44 (12), 100 (10), 76 (2), 49 (1), +1 more |
| 79115 | 421 (111..531) | 343 | 58 | 64 (64), 44 (61), 51 (38), 57 (37), 63 (27), 190 (26), 69 (19), 42 (18), 192 (18), 60 (16), 76 (7), 59 (6), +2 more |
| 79116 | 411 (114..530) | 320 | 60 | 100 (57), 44 (43), 192 (31), 42 (27), 60 (27), 63 (25), 51 (24), 57 (21), 190 (21), 69 (13), 64 (10), 59 (5), +6 more |
| 79122 | 404 (118..532) | 323 | 54 | 63 (46), 192 (41), 69 (39), 44 (37), 64 (32), 190 (25), 42 (23), 57 (22), 60 (20), 100 (12), 51 (10), 216 (10), +4 more |
| 79132 | 391 (120..515) | 305 | 58 | 190 (71), 42 (59), 44 (35), 100 (33), 69 (17), 64 (17), 107 (17), 57 (15), 60 (11), 63 (7), 49 (6), 192 (6), +4 more |
| 79128 | 402 (124..527) | 325 | 52 | 100 (81), 60 (39), 192 (34), 69 (25), 44 (24), 42 (20), 57 (18), 167 (17), 49 (15), 190 (12), 64 (11), 146 (7), +6 more |
| 79134 | 407 (127..533) | 335 | 54 | 167 (84), 60 (43), 100 (42), 44 (39), 64 (36), 69 (25), 76 (21), 57 (18), 49 (7), 63 (7), 192 (6), 42 (4), +1 more |
| 79135 | 409 (129..542) | 324 | 65 | 64 (68), 167 (57), 60 (49), 100 (34), 49 (25), 76 (22), 44 (19), 69 (14), 216 (11), 146 (9), 57 (8), 42 (3), +3 more |
| 79139 | 406 (132..537) | 324 | 48 | 60 (76), 64 (62), 167 (56), 44 (38), 100 (35), 76 (16), 49 (11), 69 (10), 42 (6), 216 (6), 63 (4), 125 (2), +2 more |
| 79136 | 393 (136..538) | 338 | 36 | 42 (68), 69 (56), 146 (54), 60 (47), 100 (43), 167 (20), 44 (17), 216 (12), 125 (8), 64 (6), 49 (4), 56 (2), +1 more |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 182 | 338..367 | 30 | 0 | 30 |
| 315 | 734..763 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/341/922; tracks with internal gaps: 30; total internal gaps: 441; longest internal gap: 29; tracks ending in coasting: 33 (trailing rows total 1205)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..485 | 484 | 484 | 430 | 54 | 15 | 2 | 37 | 78911 |
| 39 | 81..285 | 205 | 205 | 149 | 56 | 12 | 1 | 44 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 42 | 87..1008 | 922 | 922 | 838 | 84 | 42 | 29 | 0 | 78897, 78899, 78911, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..566 | 478 | 478 | 430 | 48 | 15 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..251 | 161 | 161 | 113 | 48 | 4 | 5 | 40 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..513 | 421 | 421 | 368 | 53 | 19 | 17 | 16 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 98..607 | 510 | 510 | 349 | 161 | 26 | 24 | 96 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110, 79116, 79128, 79132, 79135, 79136 |
| 57 | 99..530 | 432 | 432 | 365 | 67 | 13 | 3 | 49 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 59 | 99..493 | 395 | 395 | 340 | 55 | 18 | 3 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 60 | 99..561 | 463 | 463 | 415 | 48 | 17 | 2 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 103..221 | 119 | 119 | 79 | 40 | 0 | 0 | 40 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 63 | 108..561 | 454 | 454 | 387 | 67 | 20 | 13 | 28 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 108..592 | 485 | 485 | 359 | 126 | 19 | 12 | 91 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 113..491 | 379 | 379 | 321 | 58 | 20 | 2 | 30 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 117..457 | 341 | 341 | 279 | 62 | 21 | 13 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 76 | 125..510 | 386 | 386 | 335 | 51 | 16 | 5 | 28 | 78897, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 81 | 132..240 | 109 | 109 | 74 | 35 | 5 | 1 | 30 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 82 | 132..483 | 352 | 352 | 305 | 47 | 15 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 133..474 | 342 | 342 | 294 | 48 | 14 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 85 | 133..185 | 53 | 53 | 14 | 39 | 0 | 0 | 39 | 78899, 79098, 79102 |
| 100 | 160..566 | 407 | 407 | 350 | 57 | 20 | 3 | 29 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 107 | 176..560 | 385 | 385 | 313 | 72 | 26 | 8 | 30 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79116, 79128, 79132 |
| 108 | 179..470 | 292 | 292 | 239 | 53 | 20 | 3 | 27 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 125 | 205..321 | 117 | 117 | 21 | 96 | 3 | 11 | 82 | 78896, 78969, 78971, 79110, 79128, 79132, 79135, 79136, 79139 |
| 128 | 210..343 | 134 | 134 | 92 | 42 | 4 | 2 | 37 | 78896, 78899, 78969, 78971, 79098, 79103 |
| 144 | 243..517 | 275 | 275 | 233 | 42 | 12 | 3 | 28 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 146 | 243..378 | 136 | 136 | 82 | 54 | 11 | 2 | 41 | 79111, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 167 | 290..571 | 282 | 282 | 236 | 46 | 14 | 2 | 29 | 79122, 79128, 79134, 79135, 79136, 79139 |
| 182 | 338..367 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 190 | 359..560 | 202 | 202 | 157 | 45 | 10 | 3 | 28 | 79110, 79115, 79116, 79122, 79128, 79132 |
| 191 | 359..468 | 110 | 110 | 72 | 38 | 4 | 3 | 32 | 78969, 78971, 79098, 79102, 79103 |
| 192 | 359..557 | 199 | 199 | 169 | 30 | 4 | 1 | 26 | 79102, 79103, 79115, 79116, 79122, 79128, 79132, 79134 |
| 216 | 437..522 | 86 | 86 | 50 | 36 | 2 | 5 | 30 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 315 | 734..763 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
