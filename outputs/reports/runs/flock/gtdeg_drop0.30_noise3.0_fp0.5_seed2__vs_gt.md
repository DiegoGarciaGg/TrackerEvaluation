# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=2e0e10dc4313
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise3.0_fp0.5_seed2/tracks.csv sha256=b9f91fe4bb1c2d9f
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise3.0_fp0.5_seed2.csv sha256=2e0e10dc431347b4
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise3.0_fp0.5_seed2
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
| observations | none | 4 | 0.140 | 0.062 | 0.002 | 2.41 | 0.136 | 1062 | 2387.0 |
| observations | none | 6 | 0.192 | 0.084 | 0.364 | 3.22 | 0.206 | 1347 | 2369.0 |
| observations | none | 8 | 0.220 | 0.097 | 0.495 | 3.62 | 0.234 | 1420 | 2134.0 |
| observations | none | 12 | 0.247 | 0.110 | 0.536 | 4.01 | 0.254 | 1336 | 2010.0 |
| observations | ignore | 4 | 0.140 | 0.062 | 0.002 | 2.41 | 0.136 | 1062 | 2387.0 |
| observations | ignore | 6 | 0.192 | 0.084 | 0.364 | 3.22 | 0.206 | 1347 | 2369.0 |
| observations | ignore | 8 | 0.220 | 0.097 | 0.495 | 3.62 | 0.234 | 1420 | 2134.0 |
| observations | ignore | 12 | 0.247 | 0.110 | 0.536 | 4.01 | 0.254 | 1336 | 2010.0 |
| updates | none | 4 | 0.141 | 0.067 | -0.222 | 2.42 | 0.131 | 1153 | 2457.0 |
| updates | none | 6 | 0.205 | 0.099 | 0.207 | 3.29 | 0.205 | 1449 | 2116.0 |
| updates | none | 8 | 0.244 | 0.118 | 0.410 | 3.82 | 0.244 | 1455 | 1585.0 |
| updates | none | 12 | 0.286 | 0.141 | 0.540 | 4.52 | 0.280 | 1337 | 1163.0 |
| updates | ignore | 4 | 0.141 | 0.067 | -0.222 | 2.42 | 0.131 | 1153 | 2457.0 |
| updates | ignore | 6 | 0.205 | 0.099 | 0.207 | 3.29 | 0.205 | 1449 | 2116.0 |
| updates | ignore | 8 | 0.244 | 0.118 | 0.410 | 3.82 | 0.244 | 1455 | 1585.0 |
| updates | ignore | 12 | 0.286 | 0.141 | 0.540 | 4.52 | 0.280 | 1337 | 1163.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 6726; unmatched reference entries: 3416; unmatched candidate entries: 289
- identity switches: 1420; fragmentation (coverage interruptions): 2181; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 41 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 31 -> 41 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 41 -> 43 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 31 -> 41 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 36 -> 38 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 31 -> 43 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 38 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 41 -> 43 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 43 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 43 -> 38 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 31 -> 41 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 43 -> 38 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 41 -> 43 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 38 -> 43 at (2088.5, 3033.5), 2 frames after previous cover
- f100: ref 79097: 41 -> 53 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 31 -> 41 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 49 -> 38 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 38 -> 49 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 41 -> 53 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 38 -> 56 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 41 -> 53 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 31 -> 41 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 38 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 38 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 78899: 43 -> 38 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 49 -> 36 at (2023.5, 3033.5), 3 frames after previous cover
- f106: ref 79097: 53 -> 43 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 38 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 53 -> 43 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79105: 31 -> 41 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 78969: 36 -> 63 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 36 -> 64 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 53 -> 43 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 41 -> 53 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 49 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 36 -> 63 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 64 -> 36 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 38 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 43 -> 49 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 41 -> 66 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 31 -> 41 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 31 -> 67 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 64 -> 38 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 63 -> 36 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 36 -> 64 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 38 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 31 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 38 -> 64 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 38 -> 49 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 64 -> 36 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 38 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 49 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 67 -> 41 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 41 -> 31 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 38 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 66 -> 53 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 31 -> 66 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 41 -> 31 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 67 -> 41 at (2126, 3027), 1 frames after previous cover
- ... 1360 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 670 | 208 | 1 (670) |
| 78896 | 350 (76..429) | 219 | 77 | 91 (64), 56 (60), 63 (34), 84 (26), 190 (18), 69 (9), 38 (7), 64 (1) |
| 78969 | 352 (80..434) | 223 | 77 | 69 (111), 64 (30), 84 (29), 63 (22), 36 (8), 56 (8), 91 (7), 190 (4), 31 (3), 38 (1) |
| 78971 | 352 (84..439) | 235 | 75 | 69 (84), 84 (46), 64 (40), 182 (16), 63 (15), 36 (12), 90 (10), 68 (7), 56 (4), 117 (1) |
| 79045 | 355 (84..443) | 220 | 81 | 90 (46), 64 (38), 84 (37), 69 (28), 68 (17), 117 (15), 182 (13), 56 (6), 36 (5), 31 (3), 38 (3), 49 (3), +4 more |
| 79037 | 355 (86..445) | 231 | 77 | 117 (33), 68 (31), 64 (29), 84 (27), 90 (23), 182 (19), 56 (18), 69 (17), 128 (9), 49 (8), 38 (4), 36 (4), +5 more |
| 78897 | 345 (89..450) | 242 | 68 | 64 (52), 117 (52), 128 (42), 68 (32), 90 (25), 84 (11), 56 (8), 43 (4), 38 (4), 49 (3), 31 (2), 41 (2), +3 more |
| 78899 | 365 (91..455) | 233 | 86 | 68 (42), 117 (41), 36 (33), 64 (26), 84 (22), 90 (22), 94 (12), 56 (9), 128 (7), 49 (6), 43 (5), 41 (3), +2 more |
| 79097 | 366 (94..461) | 241 | 87 | 117 (51), 90 (46), 68 (34), 84 (29), 94 (27), 64 (21), 36 (13), 49 (7), 43 (3), 38 (3), 128 (3), 31 (2), +2 more |
| 79098 | 360 (97..467) | 242 | 82 | 49 (59), 94 (49), 64 (43), 68 (16), 43 (12), 84 (12), 36 (10), 117 (9), 90 (8), 128 (8), 78 (7), 38 (3), +4 more |
| 79102 | 371 (98..477) | 243 | 79 | 49 (60), 43 (39), 94 (31), 78 (29), 90 (18), 128 (18), 117 (15), 64 (7), 53 (6), 36 (6), 38 (5), 68 (4), +2 more |
| 79103 | 380 (99..481) | 254 | 88 | 49 (53), 36 (40), 90 (37), 128 (31), 94 (23), 53 (19), 78 (14), 43 (12), 198 (8), 31 (4), 41 (4), 64 (4), +3 more |
| 79105 | 379 (101..484) | 253 | 79 | 128 (47), 49 (46), 36 (42), 43 (28), 198 (28), 53 (16), 94 (13), 78 (9), 163 (9), 66 (3), 90 (3), 31 (2), +4 more |
| 79108 | 385 (104..492) | 278 | 74 | 78 (47), 36 (40), 43 (39), 90 (31), 49 (24), 68 (23), 38 (21), 53 (19), 94 (13), 128 (7), 31 (5), 66 (3), +3 more |
| 79110 | 388 (106..497) | 254 | 79 | 38 (44), 94 (29), 68 (24), 43 (23), 49 (23), 53 (21), 163 (17), 78 (15), 91 (15), 36 (12), 66 (10), 31 (8), +4 more |
| 79111 | 386 (109..500) | 253 | 79 | 94 (39), 43 (37), 38 (30), 91 (26), 49 (25), 68 (19), 66 (18), 53 (17), 36 (15), 31 (9), 129 (6), 163 (4), +4 more |
| 79115 | 421 (111..531) | 280 | 87 | 106 (54), 38 (51), 66 (42), 43 (34), 129 (20), 68 (20), 178 (19), 53 (13), 36 (11), 91 (7), 31 (4), 41 (3), +2 more |
| 79116 | 411 (114..530) | 265 | 86 | 38 (57), 129 (47), 43 (39), 66 (25), 41 (23), 106 (17), 94 (16), 178 (14), 36 (12), 53 (6), 31 (4), 67 (2), +2 more |
| 79122 | 404 (118..532) | 273 | 90 | 38 (61), 129 (57), 66 (39), 41 (29), 43 (20), 78 (18), 178 (16), 106 (15), 91 (9), 53 (5), 67 (1), 31 (1), +2 more |
| 79132 | 391 (120..515) | 259 | 79 | 78 (46), 66 (37), 49 (25), 106 (24), 94 (23), 91 (22), 41 (21), 36 (21), 43 (11), 178 (11), 129 (6), 67 (5), +3 more |
| 79128 | 402 (124..527) | 255 | 93 | 178 (54), 106 (44), 41 (36), 91 (25), 78 (21), 94 (19), 66 (15), 129 (14), 53 (13), 81 (8), 67 (3), 38 (3) |
| 79134 | 407 (127..533) | 298 | 72 | 66 (49), 106 (47), 129 (45), 53 (34), 41 (29), 78 (25), 81 (22), 38 (17), 91 (13), 178 (9), 192 (5), 67 (3) |
| 79135 | 409 (129..542) | 283 | 89 | 41 (104), 129 (48), 81 (41), 66 (34), 106 (23), 53 (21), 99 (4), 192 (4), 67 (2), 91 (2) |
| 79139 | 406 (132..537) | 266 | 97 | 53 (86), 81 (66), 66 (30), 106 (29), 38 (17), 99 (14), 192 (12), 41 (6), 67 (4), 91 (2) |
| 79136 | 393 (136..538) | 256 | 92 | 53 (67), 41 (67), 81 (34), 66 (19), 99 (17), 38 (16), 67 (15), 106 (14), 192 (6), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 31/315/1006; tracks with internal gaps: 30; total internal gaps: 248; longest internal gap: 2; tracks ending in coasting: 10 (trailing rows total 21)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 706 | 671 | 35 | 33 | 2 | 0 | 78911, 79136 |
| 31 | 80..156 | 77 | 57 | 53 | 4 | 1 | 1 | 3 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 36 | 87..455 | 369 | 299 | 287 | 12 | 12 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 38 | 87..537 | 451 | 369 | 357 | 12 | 12 | 1 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 41 | 91..542 | 452 | 353 | 342 | 11 | 10 | 2 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 92..500 | 409 | 327 | 310 | 17 | 15 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 49 | 96..515 | 420 | 357 | 342 | 15 | 14 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 53 | 100..537 | 438 | 361 | 347 | 14 | 11 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 102..279 | 178 | 118 | 113 | 5 | 3 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 63 | 109..210 | 102 | 78 | 74 | 4 | 2 | 1 | 2 | 78896, 78969, 78971, 79037, 79045 |
| 64 | 109..465 | 357 | 301 | 291 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 66 | 110..523 | 414 | 337 | 324 | 13 | 10 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 67 | 110..165 | 56 | 44 | 38 | 6 | 5 | 1 | 1 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 115..489 | 375 | 288 | 273 | 15 | 12 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 69 | 115..439 | 325 | 263 | 251 | 12 | 11 | 2 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 78 | 124..415 | 292 | 244 | 235 | 9 | 8 | 1 | 1 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 81 | 128..370 | 243 | 181 | 172 | 9 | 7 | 1 | 2 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 128..442 | 315 | 245 | 241 | 4 | 4 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 90 | 135..496 | 362 | 286 | 277 | 9 | 8 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 135..398 | 264 | 205 | 195 | 10 | 8 | 2 | 1 | 78896, 78969, 79037, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79139 |
| 94 | 140..529 | 390 | 305 | 294 | 11 | 9 | 2 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79128, 79132 |
| 99 | 159..247 | 89 | 42 | 35 | 7 | 2 | 1 | 5 | 79135, 79136, 79139 |
| 106 | 176..527 | 352 | 280 | 269 | 11 | 11 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 192..477 | 286 | 227 | 219 | 8 | 8 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 128 | 217..450 | 234 | 186 | 175 | 11 | 11 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 129 | 217..532 | 316 | 248 | 243 | 5 | 5 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 163 | 313..356 | 44 | 36 | 33 | 3 | 2 | 1 | 1 | 79105, 79108, 79110, 79111 |
| 178 | 372..530 | 159 | 125 | 123 | 2 | 2 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 182 | 383..445 | 63 | 50 | 49 | 1 | 1 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 190 | 404..434 | 31 | 22 | 22 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 192 | 410..481 | 72 | 38 | 34 | 4 | 1 | 1 | 3 | 79037, 79098, 79103, 79105, 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 198 | 429..480 | 52 | 37 | 37 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 6726; unmatched reference entries: 3416; unmatched candidate entries: 289
- identity switches: 1420; fragmentation (coverage interruptions): 2181; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 41 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 31 -> 41 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 41 -> 43 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 31 -> 41 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 36 -> 38 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 31 -> 43 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 38 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 41 -> 43 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 43 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 43 -> 38 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 31 -> 41 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 43 -> 38 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 41 -> 43 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 38 -> 43 at (2088.5, 3033.5), 2 frames after previous cover
- f100: ref 79097: 41 -> 53 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 31 -> 41 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 49 -> 38 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 38 -> 49 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 41 -> 53 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 38 -> 56 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 41 -> 53 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 31 -> 41 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 38 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 38 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 78899: 43 -> 38 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 49 -> 36 at (2023.5, 3033.5), 3 frames after previous cover
- f106: ref 79097: 53 -> 43 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 38 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 53 -> 43 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79105: 31 -> 41 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 78969: 36 -> 63 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 36 -> 64 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 53 -> 43 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 41 -> 53 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 49 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 36 -> 63 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 64 -> 36 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 38 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 43 -> 49 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 41 -> 66 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 31 -> 41 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 31 -> 67 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 64 -> 38 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 63 -> 36 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 36 -> 64 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 38 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 31 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 38 -> 64 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 38 -> 49 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 64 -> 36 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 38 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 49 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 67 -> 41 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 41 -> 31 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 38 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 66 -> 53 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 31 -> 66 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 41 -> 31 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 67 -> 41 at (2126, 3027), 1 frames after previous cover
- ... 1360 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 670 | 208 | 1 (670) |
| 78896 | 350 (76..429) | 219 | 77 | 91 (64), 56 (60), 63 (34), 84 (26), 190 (18), 69 (9), 38 (7), 64 (1) |
| 78969 | 352 (80..434) | 223 | 77 | 69 (111), 64 (30), 84 (29), 63 (22), 36 (8), 56 (8), 91 (7), 190 (4), 31 (3), 38 (1) |
| 78971 | 352 (84..439) | 235 | 75 | 69 (84), 84 (46), 64 (40), 182 (16), 63 (15), 36 (12), 90 (10), 68 (7), 56 (4), 117 (1) |
| 79045 | 355 (84..443) | 220 | 81 | 90 (46), 64 (38), 84 (37), 69 (28), 68 (17), 117 (15), 182 (13), 56 (6), 36 (5), 31 (3), 38 (3), 49 (3), +4 more |
| 79037 | 355 (86..445) | 231 | 77 | 117 (33), 68 (31), 64 (29), 84 (27), 90 (23), 182 (19), 56 (18), 69 (17), 128 (9), 49 (8), 38 (4), 36 (4), +5 more |
| 78897 | 345 (89..450) | 242 | 68 | 64 (52), 117 (52), 128 (42), 68 (32), 90 (25), 84 (11), 56 (8), 43 (4), 38 (4), 49 (3), 31 (2), 41 (2), +3 more |
| 78899 | 365 (91..455) | 233 | 86 | 68 (42), 117 (41), 36 (33), 64 (26), 84 (22), 90 (22), 94 (12), 56 (9), 128 (7), 49 (6), 43 (5), 41 (3), +2 more |
| 79097 | 366 (94..461) | 241 | 87 | 117 (51), 90 (46), 68 (34), 84 (29), 94 (27), 64 (21), 36 (13), 49 (7), 43 (3), 38 (3), 128 (3), 31 (2), +2 more |
| 79098 | 360 (97..467) | 242 | 82 | 49 (59), 94 (49), 64 (43), 68 (16), 43 (12), 84 (12), 36 (10), 117 (9), 90 (8), 128 (8), 78 (7), 38 (3), +4 more |
| 79102 | 371 (98..477) | 243 | 79 | 49 (60), 43 (39), 94 (31), 78 (29), 90 (18), 128 (18), 117 (15), 64 (7), 53 (6), 36 (6), 38 (5), 68 (4), +2 more |
| 79103 | 380 (99..481) | 254 | 88 | 49 (53), 36 (40), 90 (37), 128 (31), 94 (23), 53 (19), 78 (14), 43 (12), 198 (8), 31 (4), 41 (4), 64 (4), +3 more |
| 79105 | 379 (101..484) | 253 | 79 | 128 (47), 49 (46), 36 (42), 43 (28), 198 (28), 53 (16), 94 (13), 78 (9), 163 (9), 66 (3), 90 (3), 31 (2), +4 more |
| 79108 | 385 (104..492) | 278 | 74 | 78 (47), 36 (40), 43 (39), 90 (31), 49 (24), 68 (23), 38 (21), 53 (19), 94 (13), 128 (7), 31 (5), 66 (3), +3 more |
| 79110 | 388 (106..497) | 254 | 79 | 38 (44), 94 (29), 68 (24), 43 (23), 49 (23), 53 (21), 163 (17), 78 (15), 91 (15), 36 (12), 66 (10), 31 (8), +4 more |
| 79111 | 386 (109..500) | 253 | 79 | 94 (39), 43 (37), 38 (30), 91 (26), 49 (25), 68 (19), 66 (18), 53 (17), 36 (15), 31 (9), 129 (6), 163 (4), +4 more |
| 79115 | 421 (111..531) | 280 | 87 | 106 (54), 38 (51), 66 (42), 43 (34), 129 (20), 68 (20), 178 (19), 53 (13), 36 (11), 91 (7), 31 (4), 41 (3), +2 more |
| 79116 | 411 (114..530) | 265 | 86 | 38 (57), 129 (47), 43 (39), 66 (25), 41 (23), 106 (17), 94 (16), 178 (14), 36 (12), 53 (6), 31 (4), 67 (2), +2 more |
| 79122 | 404 (118..532) | 273 | 90 | 38 (61), 129 (57), 66 (39), 41 (29), 43 (20), 78 (18), 178 (16), 106 (15), 91 (9), 53 (5), 67 (1), 31 (1), +2 more |
| 79132 | 391 (120..515) | 259 | 79 | 78 (46), 66 (37), 49 (25), 106 (24), 94 (23), 91 (22), 41 (21), 36 (21), 43 (11), 178 (11), 129 (6), 67 (5), +3 more |
| 79128 | 402 (124..527) | 255 | 93 | 178 (54), 106 (44), 41 (36), 91 (25), 78 (21), 94 (19), 66 (15), 129 (14), 53 (13), 81 (8), 67 (3), 38 (3) |
| 79134 | 407 (127..533) | 298 | 72 | 66 (49), 106 (47), 129 (45), 53 (34), 41 (29), 78 (25), 81 (22), 38 (17), 91 (13), 178 (9), 192 (5), 67 (3) |
| 79135 | 409 (129..542) | 283 | 89 | 41 (104), 129 (48), 81 (41), 66 (34), 106 (23), 53 (21), 99 (4), 192 (4), 67 (2), 91 (2) |
| 79139 | 406 (132..537) | 266 | 97 | 53 (86), 81 (66), 66 (30), 106 (29), 38 (17), 99 (14), 192 (12), 41 (6), 67 (4), 91 (2) |
| 79136 | 393 (136..538) | 256 | 92 | 53 (67), 41 (67), 81 (34), 66 (19), 99 (17), 38 (16), 67 (15), 106 (14), 192 (6), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 31/315/1006; tracks with internal gaps: 30; total internal gaps: 248; longest internal gap: 2; tracks ending in coasting: 10 (trailing rows total 21)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 706 | 671 | 35 | 33 | 2 | 0 | 78911, 79136 |
| 31 | 80..156 | 77 | 57 | 53 | 4 | 1 | 1 | 3 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 36 | 87..455 | 369 | 299 | 287 | 12 | 12 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 38 | 87..537 | 451 | 369 | 357 | 12 | 12 | 1 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 41 | 91..542 | 452 | 353 | 342 | 11 | 10 | 2 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 92..500 | 409 | 327 | 310 | 17 | 15 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 49 | 96..515 | 420 | 357 | 342 | 15 | 14 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 53 | 100..537 | 438 | 361 | 347 | 14 | 11 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 102..279 | 178 | 118 | 113 | 5 | 3 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 63 | 109..210 | 102 | 78 | 74 | 4 | 2 | 1 | 2 | 78896, 78969, 78971, 79037, 79045 |
| 64 | 109..465 | 357 | 301 | 291 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 66 | 110..523 | 414 | 337 | 324 | 13 | 10 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 67 | 110..165 | 56 | 44 | 38 | 6 | 5 | 1 | 1 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 115..489 | 375 | 288 | 273 | 15 | 12 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 69 | 115..439 | 325 | 263 | 251 | 12 | 11 | 2 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 78 | 124..415 | 292 | 244 | 235 | 9 | 8 | 1 | 1 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 81 | 128..370 | 243 | 181 | 172 | 9 | 7 | 1 | 2 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 128..442 | 315 | 245 | 241 | 4 | 4 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 90 | 135..496 | 362 | 286 | 277 | 9 | 8 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 135..398 | 264 | 205 | 195 | 10 | 8 | 2 | 1 | 78896, 78969, 79037, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79139 |
| 94 | 140..529 | 390 | 305 | 294 | 11 | 9 | 2 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79128, 79132 |
| 99 | 159..247 | 89 | 42 | 35 | 7 | 2 | 1 | 5 | 79135, 79136, 79139 |
| 106 | 176..527 | 352 | 280 | 269 | 11 | 11 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 192..477 | 286 | 227 | 219 | 8 | 8 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 128 | 217..450 | 234 | 186 | 175 | 11 | 11 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 129 | 217..532 | 316 | 248 | 243 | 5 | 5 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 163 | 313..356 | 44 | 36 | 33 | 3 | 2 | 1 | 1 | 79105, 79108, 79110, 79111 |
| 178 | 372..530 | 159 | 125 | 123 | 2 | 2 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 182 | 383..445 | 63 | 50 | 49 | 1 | 1 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 190 | 404..434 | 31 | 22 | 22 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 192 | 410..481 | 72 | 38 | 34 | 4 | 1 | 1 | 3 | 79037, 79098, 79103, 79105, 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 198 | 429..480 | 52 | 37 | 37 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7754; unmatched reference entries: 2388; unmatched candidate entries: 2138
- identity switches: 1455; fragmentation (coverage interruptions): 1530; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 41 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 31 -> 41 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 41 -> 43 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 31 -> 41 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 36 -> 38 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 31 -> 43 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 38 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 41 -> 43 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 43 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 43 -> 38 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 31 -> 41 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 43 -> 38 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 41 -> 43 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 38 -> 43 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79097: 41 -> 53 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 31 -> 41 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 49 -> 38 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 38 -> 49 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 41 -> 53 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 38 -> 56 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 41 -> 53 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 31 -> 41 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 38 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 38 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 53 -> 43 at (2088, 3029), 5 frames after previous cover
- f105: ref 79103: 41 -> 53 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79105: 31 -> 41 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78899: 43 -> 38 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 49 -> 36 at (2023.5, 3033.5), 3 frames after previous cover
- f107: ref 79103: 53 -> 41 at (2110, 3022.5), 2 frames after previous cover
- f108: ref 78897: 38 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 53 -> 43 at (2084.5, 3028.5), 6 frames after previous cover
- f109: ref 78969: 36 -> 63 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 36 -> 64 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 53 -> 43 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 41 -> 53 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 49 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 36 -> 63 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 64 -> 36 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 38 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 43 -> 49 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 41 -> 66 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 31 -> 41 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 31 -> 67 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 64 -> 38 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 63 -> 36 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 36 -> 64 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 38 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 31 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 38 -> 64 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 38 -> 49 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 64 -> 36 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 38 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 49 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 67 -> 41 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 41 -> 31 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 38 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 66 -> 53 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 31 -> 66 at (2097.5, 3025.5), 1 frames after previous cover
- ... 1395 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 880 | 76 | 1 (880) |
| 78896 | 350 (76..429) | 251 | 54 | 91 (76), 56 (68), 63 (36), 84 (32), 190 (22), 69 (9), 38 (7), 64 (1) |
| 78969 | 352 (80..434) | 256 | 55 | 69 (128), 64 (36), 84 (34), 63 (25), 56 (9), 36 (8), 91 (8), 190 (4), 31 (3), 38 (1) |
| 78971 | 352 (84..439) | 258 | 58 | 69 (89), 84 (54), 64 (44), 63 (16), 182 (16), 90 (15), 36 (12), 68 (7), 56 (4), 117 (1) |
| 79045 | 355 (84..443) | 244 | 64 | 90 (50), 64 (45), 84 (45), 69 (29), 68 (19), 182 (15), 117 (13), 56 (7), 36 (5), 31 (4), 38 (3), 49 (3), +4 more |
| 79037 | 355 (86..445) | 261 | 61 | 117 (40), 68 (34), 64 (34), 84 (30), 90 (26), 182 (25), 56 (20), 69 (18), 128 (9), 49 (8), 38 (4), 36 (4), +5 more |
| 78897 | 345 (89..450) | 265 | 58 | 117 (59), 64 (53), 128 (45), 68 (33), 90 (27), 84 (11), 56 (9), 38 (5), 43 (4), 69 (4), 182 (4), 49 (3), +4 more |
| 78899 | 365 (91..455) | 264 | 67 | 68 (52), 117 (45), 36 (41), 64 (30), 84 (23), 90 (22), 56 (12), 94 (12), 128 (7), 49 (6), 43 (5), 41 (3), +3 more |
| 79097 | 366 (94..461) | 271 | 65 | 117 (59), 90 (52), 68 (42), 84 (33), 94 (28), 64 (21), 36 (14), 49 (7), 43 (4), 31 (3), 38 (3), 128 (3), +2 more |
| 79098 | 360 (97..467) | 268 | 64 | 49 (64), 94 (55), 64 (46), 68 (18), 84 (15), 43 (12), 117 (12), 36 (11), 90 (11), 128 (9), 78 (6), 38 (3), +4 more |
| 79102 | 371 (98..477) | 270 | 61 | 49 (64), 43 (47), 94 (34), 78 (33), 90 (22), 128 (18), 117 (16), 36 (9), 64 (7), 53 (6), 38 (5), 68 (4), +2 more |
| 79103 | 380 (99..481) | 293 | 61 | 49 (59), 90 (47), 36 (44), 128 (35), 94 (24), 53 (22), 78 (19), 43 (15), 198 (11), 64 (5), 31 (4), 41 (3), +3 more |
| 79105 | 379 (101..484) | 289 | 59 | 128 (54), 49 (47), 36 (47), 198 (37), 43 (33), 53 (17), 94 (15), 78 (10), 163 (10), 41 (4), 31 (3), 66 (3), +4 more |
| 79108 | 385 (104..492) | 302 | 57 | 78 (52), 36 (46), 43 (44), 90 (33), 49 (27), 68 (25), 38 (22), 53 (19), 94 (13), 128 (7), 31 (5), 66 (3), +3 more |
| 79110 | 388 (106..497) | 284 | 63 | 38 (49), 94 (31), 68 (28), 49 (26), 43 (25), 53 (23), 163 (19), 78 (17), 91 (15), 36 (13), 66 (12), 90 (12), +5 more |
| 79111 | 386 (109..500) | 293 | 61 | 94 (49), 43 (40), 38 (35), 91 (32), 49 (30), 68 (23), 53 (21), 66 (19), 36 (16), 31 (9), 129 (6), 163 (5), +4 more |
| 79115 | 421 (111..531) | 323 | 61 | 106 (69), 38 (58), 66 (48), 43 (33), 68 (27), 129 (21), 178 (19), 53 (15), 36 (15), 91 (8), 31 (5), 41 (4), +1 more |
| 79116 | 411 (114..530) | 313 | 65 | 38 (61), 129 (60), 43 (42), 66 (31), 41 (25), 106 (24), 36 (19), 94 (17), 178 (13), 53 (8), 31 (4), 67 (3), +3 more |
| 79122 | 404 (118..532) | 305 | 67 | 38 (70), 129 (60), 66 (45), 41 (31), 43 (22), 178 (21), 78 (17), 106 (15), 91 (11), 53 (6), 192 (3), 36 (2), +2 more |
| 79132 | 391 (120..515) | 291 | 57 | 78 (53), 66 (43), 49 (29), 94 (27), 91 (24), 36 (24), 106 (23), 41 (21), 43 (13), 178 (12), 38 (8), 129 (7), +3 more |
| 79128 | 402 (124..527) | 292 | 69 | 178 (62), 106 (53), 41 (40), 78 (26), 91 (25), 94 (20), 66 (19), 129 (16), 53 (13), 81 (9), 67 (4), 38 (3), +1 more |
| 79134 | 407 (127..533) | 335 | 51 | 106 (52), 129 (51), 66 (47), 53 (38), 41 (32), 78 (31), 81 (25), 38 (25), 91 (13), 178 (10), 192 (5), 67 (4), +1 more |
| 79135 | 409 (129..542) | 327 | 57 | 41 (122), 129 (61), 81 (43), 66 (40), 53 (24), 106 (23), 99 (4), 192 (4), 49 (3), 67 (2), 91 (1) |
| 79139 | 406 (132..537) | 303 | 70 | 81 (76), 53 (76), 66 (38), 38 (34), 106 (32), 99 (16), 192 (12), 41 (11), 67 (4), 91 (2), 178 (2) |
| 79136 | 393 (136..538) | 316 | 49 | 53 (108), 41 (80), 81 (39), 66 (23), 99 (21), 106 (20), 67 (15), 192 (9), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 60/344/1006; tracks with internal gaps: 32; total internal gaps: 804; longest internal gap: 19; tracks ending in coasting: 31 (trailing rows total 993)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 1006 | 881 | 125 | 75 | 5 | 0 | 78911, 79136 |
| 31 | 80..185 | 106 | 106 | 57 | 49 | 4 | 2 | 44 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 36 | 87..484 | 398 | 398 | 332 | 66 | 27 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 38 | 87..566 | 480 | 480 | 402 | 78 | 37 | 6 | 31 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 41 | 91..571 | 481 | 481 | 391 | 90 | 44 | 4 | 32 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 92..529 | 438 | 438 | 343 | 95 | 34 | 19 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 49 | 96..544 | 449 | 449 | 380 | 69 | 42 | 10 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79128, 79132, 79134, 79135 |
| 53 | 100..566 | 467 | 467 | 400 | 67 | 25 | 4 | 28 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 102..308 | 207 | 207 | 129 | 78 | 18 | 6 | 54 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 63 | 109..239 | 131 | 131 | 80 | 51 | 8 | 2 | 42 | 78896, 78969, 78971, 79037, 79045 |
| 64 | 109..494 | 386 | 386 | 322 | 64 | 31 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 66 | 110..552 | 443 | 443 | 371 | 72 | 35 | 5 | 25 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 67 | 110..194 | 85 | 85 | 41 | 44 | 9 | 2 | 33 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 115..518 | 404 | 404 | 316 | 88 | 43 | 4 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 69 | 115..468 | 354 | 354 | 277 | 77 | 33 | 5 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 78 | 124..444 | 321 | 321 | 269 | 52 | 19 | 2 | 30 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 81 | 128..399 | 272 | 272 | 193 | 79 | 31 | 2 | 44 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 128..471 | 344 | 344 | 279 | 65 | 28 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 90 | 135..525 | 391 | 391 | 320 | 71 | 30 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 135..427 | 293 | 293 | 222 | 71 | 27 | 4 | 30 | 78896, 78897, 78899, 78969, 79037, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 94 | 140..558 | 419 | 419 | 325 | 94 | 41 | 4 | 28 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79128, 79132 |
| 99 | 159..276 | 118 | 118 | 41 | 77 | 7 | 2 | 69 | 79135, 79136, 79139 |
| 106 | 176..556 | 381 | 381 | 313 | 68 | 28 | 4 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 192..506 | 315 | 315 | 247 | 68 | 30 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 128 | 217..479 | 263 | 263 | 190 | 73 | 31 | 3 | 33 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 129 | 217..561 | 345 | 345 | 282 | 63 | 25 | 6 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 163 | 313..385 | 73 | 73 | 37 | 36 | 4 | 2 | 31 | 79105, 79108, 79110, 79111 |
| 178 | 372..559 | 188 | 188 | 139 | 49 | 20 | 4 | 22 | 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 182 | 383..474 | 92 | 92 | 60 | 32 | 6 | 2 | 24 | 78897, 78971, 79037, 79045 |
| 190 | 404..463 | 60 | 60 | 26 | 34 | 3 | 3 | 29 | 78896, 78969 |
| 192 | 410..510 | 101 | 101 | 40 | 61 | 6 | 4 | 47 | 79037, 79098, 79103, 79105, 79110, 79116, 79122, 79134, 79135, 79136, 79139 |
| 198 | 429..509 | 81 | 81 | 49 | 32 | 3 | 2 | 28 | 79103, 79105, 79108 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7754; unmatched reference entries: 2388; unmatched candidate entries: 2138
- identity switches: 1455; fragmentation (coverage interruptions): 1530; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 41 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 31 -> 41 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 41 -> 43 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 31 -> 41 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 36 -> 38 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 31 -> 43 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 38 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 41 -> 43 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 43 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 43 -> 38 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 31 -> 41 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 43 -> 38 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 41 -> 43 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 38 -> 43 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79097: 41 -> 53 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 31 -> 41 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 49 -> 38 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 38 -> 49 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 41 -> 53 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 38 -> 56 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 41 -> 53 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 31 -> 41 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 38 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 38 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 53 -> 43 at (2088, 3029), 5 frames after previous cover
- f105: ref 79103: 41 -> 53 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79105: 31 -> 41 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78899: 43 -> 38 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 49 -> 36 at (2023.5, 3033.5), 3 frames after previous cover
- f107: ref 79103: 53 -> 41 at (2110, 3022.5), 2 frames after previous cover
- f108: ref 78897: 38 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 53 -> 43 at (2084.5, 3028.5), 6 frames after previous cover
- f109: ref 78969: 36 -> 63 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 36 -> 64 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 53 -> 43 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 41 -> 53 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 49 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 36 -> 63 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 64 -> 36 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 38 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 43 -> 49 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 41 -> 66 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 31 -> 41 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 31 -> 67 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 64 -> 38 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 63 -> 36 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 36 -> 64 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 38 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 31 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 38 -> 64 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 38 -> 49 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 64 -> 36 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 38 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 49 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 67 -> 41 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 41 -> 31 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 38 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 66 -> 53 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 31 -> 66 at (2097.5, 3025.5), 1 frames after previous cover
- ... 1395 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 880 | 76 | 1 (880) |
| 78896 | 350 (76..429) | 251 | 54 | 91 (76), 56 (68), 63 (36), 84 (32), 190 (22), 69 (9), 38 (7), 64 (1) |
| 78969 | 352 (80..434) | 256 | 55 | 69 (128), 64 (36), 84 (34), 63 (25), 56 (9), 36 (8), 91 (8), 190 (4), 31 (3), 38 (1) |
| 78971 | 352 (84..439) | 258 | 58 | 69 (89), 84 (54), 64 (44), 63 (16), 182 (16), 90 (15), 36 (12), 68 (7), 56 (4), 117 (1) |
| 79045 | 355 (84..443) | 244 | 64 | 90 (50), 64 (45), 84 (45), 69 (29), 68 (19), 182 (15), 117 (13), 56 (7), 36 (5), 31 (4), 38 (3), 49 (3), +4 more |
| 79037 | 355 (86..445) | 261 | 61 | 117 (40), 68 (34), 64 (34), 84 (30), 90 (26), 182 (25), 56 (20), 69 (18), 128 (9), 49 (8), 38 (4), 36 (4), +5 more |
| 78897 | 345 (89..450) | 265 | 58 | 117 (59), 64 (53), 128 (45), 68 (33), 90 (27), 84 (11), 56 (9), 38 (5), 43 (4), 69 (4), 182 (4), 49 (3), +4 more |
| 78899 | 365 (91..455) | 264 | 67 | 68 (52), 117 (45), 36 (41), 64 (30), 84 (23), 90 (22), 56 (12), 94 (12), 128 (7), 49 (6), 43 (5), 41 (3), +3 more |
| 79097 | 366 (94..461) | 271 | 65 | 117 (59), 90 (52), 68 (42), 84 (33), 94 (28), 64 (21), 36 (14), 49 (7), 43 (4), 31 (3), 38 (3), 128 (3), +2 more |
| 79098 | 360 (97..467) | 268 | 64 | 49 (64), 94 (55), 64 (46), 68 (18), 84 (15), 43 (12), 117 (12), 36 (11), 90 (11), 128 (9), 78 (6), 38 (3), +4 more |
| 79102 | 371 (98..477) | 270 | 61 | 49 (64), 43 (47), 94 (34), 78 (33), 90 (22), 128 (18), 117 (16), 36 (9), 64 (7), 53 (6), 38 (5), 68 (4), +2 more |
| 79103 | 380 (99..481) | 293 | 61 | 49 (59), 90 (47), 36 (44), 128 (35), 94 (24), 53 (22), 78 (19), 43 (15), 198 (11), 64 (5), 31 (4), 41 (3), +3 more |
| 79105 | 379 (101..484) | 289 | 59 | 128 (54), 49 (47), 36 (47), 198 (37), 43 (33), 53 (17), 94 (15), 78 (10), 163 (10), 41 (4), 31 (3), 66 (3), +4 more |
| 79108 | 385 (104..492) | 302 | 57 | 78 (52), 36 (46), 43 (44), 90 (33), 49 (27), 68 (25), 38 (22), 53 (19), 94 (13), 128 (7), 31 (5), 66 (3), +3 more |
| 79110 | 388 (106..497) | 284 | 63 | 38 (49), 94 (31), 68 (28), 49 (26), 43 (25), 53 (23), 163 (19), 78 (17), 91 (15), 36 (13), 66 (12), 90 (12), +5 more |
| 79111 | 386 (109..500) | 293 | 61 | 94 (49), 43 (40), 38 (35), 91 (32), 49 (30), 68 (23), 53 (21), 66 (19), 36 (16), 31 (9), 129 (6), 163 (5), +4 more |
| 79115 | 421 (111..531) | 323 | 61 | 106 (69), 38 (58), 66 (48), 43 (33), 68 (27), 129 (21), 178 (19), 53 (15), 36 (15), 91 (8), 31 (5), 41 (4), +1 more |
| 79116 | 411 (114..530) | 313 | 65 | 38 (61), 129 (60), 43 (42), 66 (31), 41 (25), 106 (24), 36 (19), 94 (17), 178 (13), 53 (8), 31 (4), 67 (3), +3 more |
| 79122 | 404 (118..532) | 305 | 67 | 38 (70), 129 (60), 66 (45), 41 (31), 43 (22), 178 (21), 78 (17), 106 (15), 91 (11), 53 (6), 192 (3), 36 (2), +2 more |
| 79132 | 391 (120..515) | 291 | 57 | 78 (53), 66 (43), 49 (29), 94 (27), 91 (24), 36 (24), 106 (23), 41 (21), 43 (13), 178 (12), 38 (8), 129 (7), +3 more |
| 79128 | 402 (124..527) | 292 | 69 | 178 (62), 106 (53), 41 (40), 78 (26), 91 (25), 94 (20), 66 (19), 129 (16), 53 (13), 81 (9), 67 (4), 38 (3), +1 more |
| 79134 | 407 (127..533) | 335 | 51 | 106 (52), 129 (51), 66 (47), 53 (38), 41 (32), 78 (31), 81 (25), 38 (25), 91 (13), 178 (10), 192 (5), 67 (4), +1 more |
| 79135 | 409 (129..542) | 327 | 57 | 41 (122), 129 (61), 81 (43), 66 (40), 53 (24), 106 (23), 99 (4), 192 (4), 49 (3), 67 (2), 91 (1) |
| 79139 | 406 (132..537) | 303 | 70 | 81 (76), 53 (76), 66 (38), 38 (34), 106 (32), 99 (16), 192 (12), 41 (11), 67 (4), 91 (2), 178 (2) |
| 79136 | 393 (136..538) | 316 | 49 | 53 (108), 41 (80), 81 (39), 66 (23), 99 (21), 106 (20), 67 (15), 192 (9), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 60/344/1006; tracks with internal gaps: 32; total internal gaps: 804; longest internal gap: 19; tracks ending in coasting: 31 (trailing rows total 993)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 1006 | 881 | 125 | 75 | 5 | 0 | 78911, 79136 |
| 31 | 80..185 | 106 | 106 | 57 | 49 | 4 | 2 | 44 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 36 | 87..484 | 398 | 398 | 332 | 66 | 27 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 38 | 87..566 | 480 | 480 | 402 | 78 | 37 | 6 | 31 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 41 | 91..571 | 481 | 481 | 391 | 90 | 44 | 4 | 32 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 92..529 | 438 | 438 | 343 | 95 | 34 | 19 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 49 | 96..544 | 449 | 449 | 380 | 69 | 42 | 10 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79128, 79132, 79134, 79135 |
| 53 | 100..566 | 467 | 467 | 400 | 67 | 25 | 4 | 28 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 102..308 | 207 | 207 | 129 | 78 | 18 | 6 | 54 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 63 | 109..239 | 131 | 131 | 80 | 51 | 8 | 2 | 42 | 78896, 78969, 78971, 79037, 79045 |
| 64 | 109..494 | 386 | 386 | 322 | 64 | 31 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 66 | 110..552 | 443 | 443 | 371 | 72 | 35 | 5 | 25 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 67 | 110..194 | 85 | 85 | 41 | 44 | 9 | 2 | 33 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 115..518 | 404 | 404 | 316 | 88 | 43 | 4 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 69 | 115..468 | 354 | 354 | 277 | 77 | 33 | 5 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 78 | 124..444 | 321 | 321 | 269 | 52 | 19 | 2 | 30 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 81 | 128..399 | 272 | 272 | 193 | 79 | 31 | 2 | 44 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 128..471 | 344 | 344 | 279 | 65 | 28 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 90 | 135..525 | 391 | 391 | 320 | 71 | 30 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 135..427 | 293 | 293 | 222 | 71 | 27 | 4 | 30 | 78896, 78897, 78899, 78969, 79037, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 94 | 140..558 | 419 | 419 | 325 | 94 | 41 | 4 | 28 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79128, 79132 |
| 99 | 159..276 | 118 | 118 | 41 | 77 | 7 | 2 | 69 | 79135, 79136, 79139 |
| 106 | 176..556 | 381 | 381 | 313 | 68 | 28 | 4 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 192..506 | 315 | 315 | 247 | 68 | 30 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 128 | 217..479 | 263 | 263 | 190 | 73 | 31 | 3 | 33 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 129 | 217..561 | 345 | 345 | 282 | 63 | 25 | 6 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 163 | 313..385 | 73 | 73 | 37 | 36 | 4 | 2 | 31 | 79105, 79108, 79110, 79111 |
| 178 | 372..559 | 188 | 188 | 139 | 49 | 20 | 4 | 22 | 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 182 | 383..474 | 92 | 92 | 60 | 32 | 6 | 2 | 24 | 78897, 78971, 79037, 79045 |
| 190 | 404..463 | 60 | 60 | 26 | 34 | 3 | 3 | 29 | 78896, 78969 |
| 192 | 410..510 | 101 | 101 | 40 | 61 | 6 | 4 | 47 | 79037, 79098, 79103, 79105, 79110, 79116, 79122, 79134, 79135, 79136, 79139 |
| 198 | 429..509 | 81 | 81 | 49 | 32 | 3 | 2 | 28 | 79103, 79105, 79108 |
