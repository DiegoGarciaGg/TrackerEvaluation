# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=988552e4bd33
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise3.0_fp0.0_seed1/tracks.csv sha256=f840062fc86287ab
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise3.0_fp0.0_seed1.csv sha256=988552e4bd33e9e2
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise3.0_fp0.0_seed1
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
| observations | none | 4 | 0.172 | 0.093 | 0.034 | 2.41 | 0.204 | 901 | 2401.0 |
| observations | none | 6 | 0.236 | 0.127 | 0.390 | 3.20 | 0.297 | 1155 | 2355.0 |
| observations | none | 8 | 0.272 | 0.148 | 0.529 | 3.60 | 0.339 | 1181 | 2148.0 |
| observations | none | 12 | 0.307 | 0.173 | 0.571 | 4.02 | 0.369 | 1094 | 2035.0 |
| observations | ignore | 4 | 0.172 | 0.093 | 0.034 | 2.41 | 0.204 | 901 | 2401.0 |
| observations | ignore | 6 | 0.236 | 0.127 | 0.390 | 3.20 | 0.297 | 1155 | 2355.0 |
| observations | ignore | 8 | 0.272 | 0.148 | 0.529 | 3.60 | 0.339 | 1181 | 2148.0 |
| observations | ignore | 12 | 0.307 | 0.173 | 0.571 | 4.02 | 0.369 | 1094 | 2035.0 |
| updates | none | 4 | 0.173 | 0.098 | -0.174 | 2.41 | 0.196 | 997 | 2417.0 |
| updates | none | 6 | 0.255 | 0.146 | 0.264 | 3.27 | 0.298 | 1249 | 2027.0 |
| updates | none | 8 | 0.307 | 0.178 | 0.490 | 3.82 | 0.362 | 1257 | 1442.0 |
| updates | none | 12 | 0.365 | 0.218 | 0.632 | 4.53 | 0.420 | 1090 | 996.0 |
| updates | ignore | 4 | 0.173 | 0.098 | -0.174 | 2.41 | 0.196 | 997 | 2417.0 |
| updates | ignore | 6 | 0.255 | 0.146 | 0.264 | 3.27 | 0.298 | 1249 | 2027.0 |
| updates | ignore | 8 | 0.307 | 0.178 | 0.490 | 3.82 | 0.362 | 1257 | 1442.0 |
| updates | ignore | 12 | 0.365 | 0.218 | 0.632 | 4.53 | 0.420 | 1090 | 996.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 6784; unmatched reference entries: 3358; unmatched candidate entries: 234
- identity switches: 1181; fragmentation (coverage interruptions): 2207; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 4 -> 7 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 5 -> 4 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 4 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 4 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 4 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 4 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 5 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 4 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 4 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 4 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 5 -> 9 at (2111.5, 3028.5), 4 frames after previous cover
- f102: ref 79098: 5 -> 9 at (2118, 3027), 1 frames after previous cover
- f103: ref 78899: 4 -> 7 at (2086, 3030), 2 frames after previous cover
- f103: ref 79097: 9 -> 4 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 12 -> 5 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 7 -> 2 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 14 -> 13 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 2 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 7 -> 2 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 14 -> 16 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 9 -> 4 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79105: 12 -> 5 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 2 -> 14 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 4 -> 7 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 5 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 12 -> 5 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 16 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 7 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79045: 16 -> 14 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 7 -> 5 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 14 -> 17 at (2040.5, 3033), 2 frames after previous cover
- f108: ref 79037: 7 -> 14 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 7 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 2 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 12 -> 4 at (2096.5, 3027.5), 7 frames after previous cover
- f108: ref 79103: 9 -> 5 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 12 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 5 -> 12 at (2131, 3027), 2 frames after previous cover
- f109: ref 78899: 2 -> 7 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79097: 7 -> 2 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 9 -> 5 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 12 -> 4 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 12 -> 9 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 17 -> 14 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 16 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 14 -> 17 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 14 -> 16 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79103: 5 -> 4 at (2092.5, 3023.5), 2 frames after previous cover
- f111: ref 78971: 13 -> 16 at (1984, 3033.5), 1 frames after previous cover
- ... 1121 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 675 | 226 | 0 (675) |
| 78896 | 350 (76..429) | 226 | 77 | 16 (201), 11 (20), 2 (5) |
| 78969 | 352 (80..434) | 229 | 85 | 17 (204), 13 (9), 16 (8), 2 (6), 11 (2) |
| 78971 | 352 (84..439) | 219 | 82 | 7 (94), 22 (72), 17 (21), 28 (11), 16 (8), 23 (4), 4 (3), 13 (3), 14 (2), 2 (1) |
| 79045 | 355 (84..443) | 241 | 72 | 28 (135), 22 (50), 7 (18), 23 (11), 14 (5), 16 (5), 13 (5), 2 (4), 17 (4), 4 (3), 11 (1) |
| 79037 | 355 (86..445) | 240 | 71 | 22 (68), 28 (68), 7 (64), 23 (18), 2 (4), 4 (3), 13 (3), 11 (3), 14 (2), 17 (2), 16 (2), 5 (1), +2 more |
| 78897 | 345 (89..450) | 228 | 78 | 23 (120), 19 (42), 7 (25), 22 (23), 14 (4), 4 (3), 11 (3), 5 (1), 9 (1), 2 (1), 17 (1), 16 (1), +3 more |
| 78899 | 365 (91..455) | 245 | 84 | 19 (81), 23 (61), 26 (44), 7 (22), 11 (16), 31 (5), 5 (4), 4 (3), 2 (3), 22 (3), 9 (2), 13 (1) |
| 79097 | 366 (94..461) | 238 | 78 | 26 (85), 19 (84), 7 (20), 31 (19), 11 (13), 23 (5), 5 (3), 13 (3), 4 (2), 9 (1), 2 (1), 20 (1), +1 more |
| 79098 | 360 (97..467) | 239 | 79 | 11 (67), 31 (63), 26 (56), 33 (11), 18 (7), 19 (7), 7 (6), 9 (5), 4 (3), 20 (3), 5 (2), 2 (2), +4 more |
| 79102 | 371 (98..477) | 244 | 78 | 31 (84), 9 (45), 11 (44), 18 (25), 26 (20), 19 (5), 13 (4), 33 (4), 14 (3), 12 (2), 2 (2), 21 (2), +3 more |
| 79103 | 380 (99..481) | 264 | 83 | 11 (66), 9 (65), 33 (38), 31 (25), 26 (24), 4 (15), 18 (12), 5 (8), 21 (4), 19 (3), 12 (1), 7 (1), +2 more |
| 79105 | 379 (101..484) | 250 | 89 | 9 (51), 33 (45), 11 (35), 31 (21), 5 (20), 4 (20), 21 (15), 12 (11), 18 (9), 26 (8), 2 (4), 13 (4), +3 more |
| 79108 | 385 (104..492) | 271 | 79 | 12 (69), 18 (52), 33 (33), 5 (28), 9 (19), 19 (13), 11 (11), 26 (10), 4 (9), 21 (8), 31 (7), 2 (3), +3 more |
| 79110 | 388 (106..497) | 264 | 82 | 12 (61), 33 (58), 18 (33), 5 (26), 2 (25), 19 (19), 9 (13), 4 (11), 21 (6), 13 (4), 11 (4), 20 (2), +1 more |
| 79111 | 386 (109..500) | 261 | 87 | 18 (60), 2 (49), 33 (42), 4 (22), 9 (20), 5 (15), 13 (15), 12 (14), 19 (11), 21 (6), 14 (5), 20 (1), +1 more |
| 79115 | 421 (111..531) | 296 | 86 | 2 (92), 21 (62), 4 (35), 13 (34), 9 (25), 14 (17), 18 (14), 5 (9), 12 (4), 33 (3), 19 (1) |
| 79116 | 411 (114..530) | 270 | 83 | 13 (112), 2 (29), 4 (28), 5 (26), 14 (25), 21 (15), 9 (14), 18 (8), 12 (7), 33 (4), 20 (2) |
| 79122 | 404 (118..532) | 267 | 88 | 14 (101), 13 (64), 9 (40), 4 (23), 21 (20), 5 (10), 12 (5), 2 (4) |
| 79132 | 391 (120..515) | 257 | 80 | 4 (57), 14 (49), 13 (45), 5 (36), 21 (26), 9 (21), 2 (13), 20 (5), 12 (3), 33 (2) |
| 79128 | 402 (124..527) | 267 | 87 | 14 (82), 21 (74), 4 (21), 5 (20), 2 (19), 12 (12), 13 (12), 20 (10), 18 (9), 9 (8) |
| 79134 | 407 (127..533) | 283 | 86 | 21 (40), 2 (39), 4 (37), 12 (35), 20 (31), 14 (25), 5 (22), 13 (18), 35 (17), 18 (16), 9 (3) |
| 79135 | 409 (129..542) | 268 | 96 | 18 (69), 12 (48), 20 (32), 21 (32), 35 (30), 4 (28), 5 (20), 2 (9) |
| 79139 | 406 (132..537) | 279 | 88 | 35 (160), 20 (63), 12 (29), 2 (12), 5 (9), 4 (6) |
| 79136 | 393 (136..538) | 263 | 83 | 20 (148), 5 (46), 35 (43), 2 (25), 12 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 299/380/1007; tracks with internal gaps: 23; total internal gaps: 226; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 695 | 675 | 20 | 19 | 2 | 0 | 78911 |
| 2 | 81..537 | 457 | 368 | 352 | 16 | 14 | 3 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 4 | 87..514 | 428 | 347 | 333 | 14 | 13 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 89..491 | 403 | 310 | 306 | 4 | 4 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 91..439 | 349 | 260 | 252 | 8 | 8 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 93..531 | 439 | 342 | 334 | 8 | 8 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..477 | 380 | 296 | 286 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 99..495 | 397 | 312 | 302 | 10 | 9 | 2 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 99..528 | 430 | 353 | 343 | 10 | 9 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 14 | 99..527 | 429 | 348 | 330 | 18 | 18 | 1 | 0 | 78897, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 16 | 105..428 | 324 | 233 | 225 | 8 | 8 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 17 | 108..433 | 326 | 237 | 232 | 5 | 5 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 112..542 | 431 | 324 | 315 | 9 | 9 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135 |
| 19 | 113..461 | 349 | 276 | 269 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 117..532 | 416 | 319 | 306 | 13 | 12 | 2 | 0 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 125..531 | 407 | 326 | 311 | 15 | 14 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 22 | 132..445 | 314 | 225 | 216 | 9 | 9 | 1 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 23 | 132..450 | 319 | 235 | 221 | 14 | 14 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 133..484 | 352 | 252 | 247 | 5 | 5 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 28 | 143..441 | 299 | 222 | 214 | 8 | 8 | 1 | 0 | 78971, 79037, 79045 |
| 31 | 176..481 | 306 | 238 | 225 | 13 | 13 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 33 | 179..500 | 322 | 247 | 240 | 7 | 7 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 35 | 210..537 | 328 | 253 | 250 | 3 | 3 | 1 | 0 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 6784; unmatched reference entries: 3358; unmatched candidate entries: 234
- identity switches: 1181; fragmentation (coverage interruptions): 2207; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 4 -> 7 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 5 -> 4 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 4 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 4 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 4 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 4 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 5 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 4 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 4 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 4 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 5 -> 9 at (2111.5, 3028.5), 4 frames after previous cover
- f102: ref 79098: 5 -> 9 at (2118, 3027), 1 frames after previous cover
- f103: ref 78899: 4 -> 7 at (2086, 3030), 2 frames after previous cover
- f103: ref 79097: 9 -> 4 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 12 -> 5 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 7 -> 2 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 14 -> 13 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 2 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 7 -> 2 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 14 -> 16 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 9 -> 4 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79105: 12 -> 5 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 2 -> 14 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 4 -> 7 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 5 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 12 -> 5 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 16 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 7 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79045: 16 -> 14 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 7 -> 5 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 14 -> 17 at (2040.5, 3033), 2 frames after previous cover
- f108: ref 79037: 7 -> 14 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 7 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 2 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 12 -> 4 at (2096.5, 3027.5), 7 frames after previous cover
- f108: ref 79103: 9 -> 5 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 12 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 5 -> 12 at (2131, 3027), 2 frames after previous cover
- f109: ref 78899: 2 -> 7 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79097: 7 -> 2 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 9 -> 5 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 12 -> 4 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 12 -> 9 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 17 -> 14 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 16 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 14 -> 17 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 14 -> 16 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79103: 5 -> 4 at (2092.5, 3023.5), 2 frames after previous cover
- f111: ref 78971: 13 -> 16 at (1984, 3033.5), 1 frames after previous cover
- ... 1121 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 675 | 226 | 0 (675) |
| 78896 | 350 (76..429) | 226 | 77 | 16 (201), 11 (20), 2 (5) |
| 78969 | 352 (80..434) | 229 | 85 | 17 (204), 13 (9), 16 (8), 2 (6), 11 (2) |
| 78971 | 352 (84..439) | 219 | 82 | 7 (94), 22 (72), 17 (21), 28 (11), 16 (8), 23 (4), 4 (3), 13 (3), 14 (2), 2 (1) |
| 79045 | 355 (84..443) | 241 | 72 | 28 (135), 22 (50), 7 (18), 23 (11), 14 (5), 16 (5), 13 (5), 2 (4), 17 (4), 4 (3), 11 (1) |
| 79037 | 355 (86..445) | 240 | 71 | 22 (68), 28 (68), 7 (64), 23 (18), 2 (4), 4 (3), 13 (3), 11 (3), 14 (2), 17 (2), 16 (2), 5 (1), +2 more |
| 78897 | 345 (89..450) | 228 | 78 | 23 (120), 19 (42), 7 (25), 22 (23), 14 (4), 4 (3), 11 (3), 5 (1), 9 (1), 2 (1), 17 (1), 16 (1), +3 more |
| 78899 | 365 (91..455) | 245 | 84 | 19 (81), 23 (61), 26 (44), 7 (22), 11 (16), 31 (5), 5 (4), 4 (3), 2 (3), 22 (3), 9 (2), 13 (1) |
| 79097 | 366 (94..461) | 238 | 78 | 26 (85), 19 (84), 7 (20), 31 (19), 11 (13), 23 (5), 5 (3), 13 (3), 4 (2), 9 (1), 2 (1), 20 (1), +1 more |
| 79098 | 360 (97..467) | 239 | 79 | 11 (67), 31 (63), 26 (56), 33 (11), 18 (7), 19 (7), 7 (6), 9 (5), 4 (3), 20 (3), 5 (2), 2 (2), +4 more |
| 79102 | 371 (98..477) | 244 | 78 | 31 (84), 9 (45), 11 (44), 18 (25), 26 (20), 19 (5), 13 (4), 33 (4), 14 (3), 12 (2), 2 (2), 21 (2), +3 more |
| 79103 | 380 (99..481) | 264 | 83 | 11 (66), 9 (65), 33 (38), 31 (25), 26 (24), 4 (15), 18 (12), 5 (8), 21 (4), 19 (3), 12 (1), 7 (1), +2 more |
| 79105 | 379 (101..484) | 250 | 89 | 9 (51), 33 (45), 11 (35), 31 (21), 5 (20), 4 (20), 21 (15), 12 (11), 18 (9), 26 (8), 2 (4), 13 (4), +3 more |
| 79108 | 385 (104..492) | 271 | 79 | 12 (69), 18 (52), 33 (33), 5 (28), 9 (19), 19 (13), 11 (11), 26 (10), 4 (9), 21 (8), 31 (7), 2 (3), +3 more |
| 79110 | 388 (106..497) | 264 | 82 | 12 (61), 33 (58), 18 (33), 5 (26), 2 (25), 19 (19), 9 (13), 4 (11), 21 (6), 13 (4), 11 (4), 20 (2), +1 more |
| 79111 | 386 (109..500) | 261 | 87 | 18 (60), 2 (49), 33 (42), 4 (22), 9 (20), 5 (15), 13 (15), 12 (14), 19 (11), 21 (6), 14 (5), 20 (1), +1 more |
| 79115 | 421 (111..531) | 296 | 86 | 2 (92), 21 (62), 4 (35), 13 (34), 9 (25), 14 (17), 18 (14), 5 (9), 12 (4), 33 (3), 19 (1) |
| 79116 | 411 (114..530) | 270 | 83 | 13 (112), 2 (29), 4 (28), 5 (26), 14 (25), 21 (15), 9 (14), 18 (8), 12 (7), 33 (4), 20 (2) |
| 79122 | 404 (118..532) | 267 | 88 | 14 (101), 13 (64), 9 (40), 4 (23), 21 (20), 5 (10), 12 (5), 2 (4) |
| 79132 | 391 (120..515) | 257 | 80 | 4 (57), 14 (49), 13 (45), 5 (36), 21 (26), 9 (21), 2 (13), 20 (5), 12 (3), 33 (2) |
| 79128 | 402 (124..527) | 267 | 87 | 14 (82), 21 (74), 4 (21), 5 (20), 2 (19), 12 (12), 13 (12), 20 (10), 18 (9), 9 (8) |
| 79134 | 407 (127..533) | 283 | 86 | 21 (40), 2 (39), 4 (37), 12 (35), 20 (31), 14 (25), 5 (22), 13 (18), 35 (17), 18 (16), 9 (3) |
| 79135 | 409 (129..542) | 268 | 96 | 18 (69), 12 (48), 20 (32), 21 (32), 35 (30), 4 (28), 5 (20), 2 (9) |
| 79139 | 406 (132..537) | 279 | 88 | 35 (160), 20 (63), 12 (29), 2 (12), 5 (9), 4 (6) |
| 79136 | 393 (136..538) | 263 | 83 | 20 (148), 5 (46), 35 (43), 2 (25), 12 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 299/380/1007; tracks with internal gaps: 23; total internal gaps: 226; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 695 | 675 | 20 | 19 | 2 | 0 | 78911 |
| 2 | 81..537 | 457 | 368 | 352 | 16 | 14 | 3 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 4 | 87..514 | 428 | 347 | 333 | 14 | 13 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 89..491 | 403 | 310 | 306 | 4 | 4 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 91..439 | 349 | 260 | 252 | 8 | 8 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 93..531 | 439 | 342 | 334 | 8 | 8 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..477 | 380 | 296 | 286 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 99..495 | 397 | 312 | 302 | 10 | 9 | 2 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 99..528 | 430 | 353 | 343 | 10 | 9 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 14 | 99..527 | 429 | 348 | 330 | 18 | 18 | 1 | 0 | 78897, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 16 | 105..428 | 324 | 233 | 225 | 8 | 8 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 17 | 108..433 | 326 | 237 | 232 | 5 | 5 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 112..542 | 431 | 324 | 315 | 9 | 9 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135 |
| 19 | 113..461 | 349 | 276 | 269 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 117..532 | 416 | 319 | 306 | 13 | 12 | 2 | 0 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 125..531 | 407 | 326 | 311 | 15 | 14 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 22 | 132..445 | 314 | 225 | 216 | 9 | 9 | 1 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 23 | 132..450 | 319 | 235 | 221 | 14 | 14 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 133..484 | 352 | 252 | 247 | 5 | 5 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 28 | 143..441 | 299 | 222 | 214 | 8 | 8 | 1 | 0 | 78971, 79037, 79045 |
| 31 | 176..481 | 306 | 238 | 225 | 13 | 13 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 33 | 179..500 | 322 | 247 | 240 | 7 | 7 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 35 | 210..537 | 328 | 253 | 250 | 3 | 3 | 1 | 0 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 8038; unmatched reference entries: 2104; unmatched candidate entries: 1812
- identity switches: 1257; fragmentation (coverage interruptions): 1385; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 4 -> 7 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 5 -> 4 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 4 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 4 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 4 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 4 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 5 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 4 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 4 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 4 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 5 -> 9 at (2111.5, 3028.5), 3 frames after previous cover
- f102: ref 79098: 5 -> 9 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 12 -> 5 at (2130.5, 3027), 1 frames after previous cover
- f103: ref 78899: 4 -> 7 at (2086, 3030), 1 frames after previous cover
- f103: ref 79097: 9 -> 4 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 12 -> 5 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 7 -> 2 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 14 -> 13 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 2 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 7 -> 2 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 14 -> 16 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 9 -> 4 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 5 -> 9 at (2113.5, 3026.5), 3 frames after previous cover
- f105: ref 79105: 12 -> 5 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 2 -> 14 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 4 -> 7 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 5 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 12 -> 5 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 16 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 7 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79045: 16 -> 14 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 7 -> 5 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 14 -> 17 at (2040.5, 3033), 2 frames after previous cover
- f108: ref 79037: 7 -> 14 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 7 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 2 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 9 -> 4 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79103: 9 -> 5 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 12 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 5 -> 12 at (2131, 3027), 2 frames after previous cover
- f109: ref 78899: 2 -> 7 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79097: 7 -> 2 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 9 -> 5 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 12 -> 4 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 12 -> 9 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 17 -> 14 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 16 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 14 -> 17 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 14 -> 16 at (2000.5, 3033.5), 1 frames after previous cover
- ... 1197 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 912 | 67 | 0 (912) |
| 78896 | 350 (76..429) | 273 | 45 | 16 (245), 11 (22), 2 (6) |
| 78969 | 352 (80..434) | 275 | 49 | 17 (247), 13 (10), 16 (10), 2 (6), 11 (2) |
| 78971 | 352 (84..439) | 265 | 49 | 7 (116), 22 (86), 17 (24), 16 (13), 28 (13), 23 (4), 4 (3), 13 (3), 14 (2), 2 (1) |
| 79045 | 355 (84..443) | 282 | 48 | 28 (156), 22 (66), 7 (21), 23 (11), 16 (6), 14 (5), 13 (5), 2 (4), 17 (4), 4 (3), 11 (1) |
| 79037 | 355 (86..445) | 280 | 48 | 22 (87), 28 (76), 7 (71), 23 (20), 16 (5), 2 (4), 4 (3), 14 (3), 13 (3), 11 (3), 17 (2), 5 (1), +2 more |
| 78897 | 345 (89..450) | 266 | 53 | 23 (139), 19 (46), 7 (32), 22 (28), 14 (4), 4 (3), 11 (3), 5 (2), 9 (2), 28 (2), 2 (1), 17 (1), +3 more |
| 78899 | 365 (91..455) | 286 | 56 | 19 (96), 23 (68), 26 (59), 7 (24), 11 (17), 5 (4), 4 (4), 31 (4), 9 (3), 2 (3), 22 (3), 13 (1) |
| 79097 | 366 (94..461) | 270 | 60 | 19 (98), 26 (96), 31 (22), 7 (20), 11 (15), 23 (6), 5 (4), 13 (3), 4 (2), 9 (1), 2 (1), 20 (1), +1 more |
| 79098 | 360 (97..467) | 275 | 51 | 11 (80), 31 (77), 26 (64), 33 (12), 18 (8), 19 (7), 7 (6), 5 (3), 9 (3), 4 (3), 20 (3), 2 (2), +4 more |
| 79102 | 371 (98..477) | 287 | 56 | 31 (101), 11 (52), 9 (50), 18 (28), 26 (22), 33 (9), 19 (5), 14 (4), 13 (4), 12 (3), 2 (2), 21 (2), +4 more |
| 79103 | 380 (99..481) | 302 | 56 | 9 (83), 11 (74), 33 (39), 26 (29), 31 (28), 4 (16), 18 (11), 5 (9), 21 (5), 19 (3), 7 (2), 12 (1), +2 more |
| 79105 | 379 (101..484) | 296 | 57 | 9 (59), 33 (58), 11 (41), 31 (30), 5 (25), 4 (22), 21 (17), 18 (11), 12 (10), 26 (7), 2 (5), 13 (4), +3 more |
| 79108 | 385 (104..492) | 305 | 56 | 12 (83), 18 (56), 5 (36), 33 (35), 9 (22), 19 (14), 26 (12), 11 (11), 4 (9), 21 (8), 31 (7), 2 (3), +3 more |
| 79110 | 388 (106..497) | 309 | 55 | 12 (73), 33 (71), 18 (46), 5 (30), 2 (25), 19 (18), 9 (15), 4 (11), 21 (6), 13 (5), 11 (5), 20 (2), +1 more |
| 79111 | 386 (109..500) | 308 | 53 | 18 (71), 2 (60), 33 (48), 9 (23), 4 (23), 5 (19), 13 (19), 12 (18), 19 (12), 21 (6), 14 (5), 20 (2), +1 more |
| 79115 | 421 (111..531) | 344 | 54 | 2 (113), 21 (71), 4 (39), 13 (39), 9 (29), 14 (18), 18 (15), 5 (11), 12 (4), 33 (3), 20 (1), 19 (1) |
| 79116 | 411 (114..530) | 303 | 66 | 13 (125), 2 (30), 4 (29), 14 (29), 5 (28), 21 (17), 9 (16), 18 (13), 12 (9), 33 (6), 20 (1) |
| 79122 | 404 (118..532) | 316 | 61 | 14 (120), 13 (78), 9 (45), 4 (24), 21 (23), 5 (10), 2 (7), 12 (6), 33 (3) |
| 79132 | 391 (120..515) | 291 | 59 | 4 (67), 14 (55), 13 (53), 5 (39), 21 (28), 9 (23), 2 (13), 20 (6), 33 (4), 12 (3) |
| 79128 | 402 (124..527) | 311 | 62 | 14 (91), 21 (84), 4 (30), 5 (28), 2 (20), 12 (13), 20 (12), 9 (11), 13 (11), 18 (11) |
| 79134 | 407 (127..533) | 333 | 52 | 2 (48), 4 (48), 21 (42), 20 (40), 12 (38), 14 (30), 5 (23), 13 (21), 18 (21), 35 (18), 9 (4) |
| 79135 | 409 (129..542) | 317 | 68 | 18 (84), 12 (53), 21 (39), 20 (36), 4 (36), 35 (35), 5 (23), 2 (9), 14 (2) |
| 79139 | 406 (132..537) | 318 | 56 | 35 (199), 20 (67), 12 (34), 5 (10), 4 (7), 21 (1) |
| 79136 | 393 (136..538) | 314 | 48 | 20 (175), 5 (54), 2 (42), 35 (41), 12 (1), 14 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 328/409/1007; tracks with internal gaps: 23; total internal gaps: 852; longest internal gap: 13; tracks ending in coasting: 22 (trailing rows total 579)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 912 | 95 | 67 | 5 | 0 | 78911 |
| 2 | 81..566 | 486 | 486 | 405 | 81 | 35 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 4 | 87..543 | 457 | 457 | 383 | 74 | 31 | 10 | 16 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 89..520 | 432 | 432 | 360 | 72 | 28 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 91..468 | 378 | 378 | 294 | 84 | 37 | 5 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 93..560 | 468 | 468 | 390 | 78 | 32 | 5 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..506 | 409 | 409 | 328 | 81 | 37 | 4 | 29 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 99..524 | 426 | 426 | 349 | 77 | 40 | 4 | 27 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 99..557 | 459 | 459 | 391 | 68 | 30 | 4 | 27 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 14 | 99..556 | 458 | 458 | 379 | 79 | 39 | 13 | 18 | 78897, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 16 | 105..457 | 353 | 353 | 280 | 73 | 40 | 5 | 12 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 17 | 108..462 | 355 | 355 | 278 | 77 | 36 | 4 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 112..571 | 460 | 460 | 376 | 84 | 38 | 4 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135 |
| 19 | 113..490 | 378 | 378 | 303 | 75 | 31 | 4 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 117..561 | 445 | 445 | 354 | 91 | 41 | 5 | 28 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 125..560 | 436 | 436 | 350 | 86 | 38 | 5 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 132..474 | 343 | 343 | 270 | 73 | 31 | 6 | 24 | 78897, 78899, 78971, 79037, 79045 |
| 23 | 132..479 | 348 | 348 | 250 | 98 | 47 | 4 | 31 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 133..513 | 381 | 381 | 289 | 92 | 46 | 7 | 21 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 28 | 143..470 | 328 | 328 | 247 | 81 | 39 | 3 | 27 | 78897, 78971, 79037, 79045 |
| 31 | 176..510 | 335 | 335 | 269 | 66 | 32 | 3 | 27 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 33 | 179..529 | 351 | 351 | 288 | 63 | 29 | 3 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 35 | 210..566 | 357 | 357 | 293 | 64 | 28 | 3 | 29 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 8038; unmatched reference entries: 2104; unmatched candidate entries: 1812
- identity switches: 1257; fragmentation (coverage interruptions): 1385; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 4 -> 7 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 5 -> 4 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 4 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 4 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 4 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 4 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 5 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 4 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 4 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 4 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 5 -> 9 at (2111.5, 3028.5), 3 frames after previous cover
- f102: ref 79098: 5 -> 9 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 12 -> 5 at (2130.5, 3027), 1 frames after previous cover
- f103: ref 78899: 4 -> 7 at (2086, 3030), 1 frames after previous cover
- f103: ref 79097: 9 -> 4 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 12 -> 5 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 7 -> 2 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 14 -> 13 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 2 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 7 -> 2 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 14 -> 16 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 9 -> 4 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 5 -> 9 at (2113.5, 3026.5), 3 frames after previous cover
- f105: ref 79105: 12 -> 5 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 2 -> 14 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 4 -> 7 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 5 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 12 -> 5 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 16 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 7 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79045: 16 -> 14 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 7 -> 5 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78897: 14 -> 17 at (2040.5, 3033), 2 frames after previous cover
- f108: ref 79037: 7 -> 14 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 7 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 2 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 9 -> 4 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79103: 9 -> 5 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 12 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 5 -> 12 at (2131, 3027), 2 frames after previous cover
- f109: ref 78899: 2 -> 7 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79097: 7 -> 2 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79105: 9 -> 5 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 12 -> 4 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 12 -> 9 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78897: 17 -> 14 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 78971: 16 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 14 -> 17 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 14 -> 16 at (2000.5, 3033.5), 1 frames after previous cover
- ... 1197 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 912 | 67 | 0 (912) |
| 78896 | 350 (76..429) | 273 | 45 | 16 (245), 11 (22), 2 (6) |
| 78969 | 352 (80..434) | 275 | 49 | 17 (247), 13 (10), 16 (10), 2 (6), 11 (2) |
| 78971 | 352 (84..439) | 265 | 49 | 7 (116), 22 (86), 17 (24), 16 (13), 28 (13), 23 (4), 4 (3), 13 (3), 14 (2), 2 (1) |
| 79045 | 355 (84..443) | 282 | 48 | 28 (156), 22 (66), 7 (21), 23 (11), 16 (6), 14 (5), 13 (5), 2 (4), 17 (4), 4 (3), 11 (1) |
| 79037 | 355 (86..445) | 280 | 48 | 22 (87), 28 (76), 7 (71), 23 (20), 16 (5), 2 (4), 4 (3), 14 (3), 13 (3), 11 (3), 17 (2), 5 (1), +2 more |
| 78897 | 345 (89..450) | 266 | 53 | 23 (139), 19 (46), 7 (32), 22 (28), 14 (4), 4 (3), 11 (3), 5 (2), 9 (2), 28 (2), 2 (1), 17 (1), +3 more |
| 78899 | 365 (91..455) | 286 | 56 | 19 (96), 23 (68), 26 (59), 7 (24), 11 (17), 5 (4), 4 (4), 31 (4), 9 (3), 2 (3), 22 (3), 13 (1) |
| 79097 | 366 (94..461) | 270 | 60 | 19 (98), 26 (96), 31 (22), 7 (20), 11 (15), 23 (6), 5 (4), 13 (3), 4 (2), 9 (1), 2 (1), 20 (1), +1 more |
| 79098 | 360 (97..467) | 275 | 51 | 11 (80), 31 (77), 26 (64), 33 (12), 18 (8), 19 (7), 7 (6), 5 (3), 9 (3), 4 (3), 20 (3), 2 (2), +4 more |
| 79102 | 371 (98..477) | 287 | 56 | 31 (101), 11 (52), 9 (50), 18 (28), 26 (22), 33 (9), 19 (5), 14 (4), 13 (4), 12 (3), 2 (2), 21 (2), +4 more |
| 79103 | 380 (99..481) | 302 | 56 | 9 (83), 11 (74), 33 (39), 26 (29), 31 (28), 4 (16), 18 (11), 5 (9), 21 (5), 19 (3), 7 (2), 12 (1), +2 more |
| 79105 | 379 (101..484) | 296 | 57 | 9 (59), 33 (58), 11 (41), 31 (30), 5 (25), 4 (22), 21 (17), 18 (11), 12 (10), 26 (7), 2 (5), 13 (4), +3 more |
| 79108 | 385 (104..492) | 305 | 56 | 12 (83), 18 (56), 5 (36), 33 (35), 9 (22), 19 (14), 26 (12), 11 (11), 4 (9), 21 (8), 31 (7), 2 (3), +3 more |
| 79110 | 388 (106..497) | 309 | 55 | 12 (73), 33 (71), 18 (46), 5 (30), 2 (25), 19 (18), 9 (15), 4 (11), 21 (6), 13 (5), 11 (5), 20 (2), +1 more |
| 79111 | 386 (109..500) | 308 | 53 | 18 (71), 2 (60), 33 (48), 9 (23), 4 (23), 5 (19), 13 (19), 12 (18), 19 (12), 21 (6), 14 (5), 20 (2), +1 more |
| 79115 | 421 (111..531) | 344 | 54 | 2 (113), 21 (71), 4 (39), 13 (39), 9 (29), 14 (18), 18 (15), 5 (11), 12 (4), 33 (3), 20 (1), 19 (1) |
| 79116 | 411 (114..530) | 303 | 66 | 13 (125), 2 (30), 4 (29), 14 (29), 5 (28), 21 (17), 9 (16), 18 (13), 12 (9), 33 (6), 20 (1) |
| 79122 | 404 (118..532) | 316 | 61 | 14 (120), 13 (78), 9 (45), 4 (24), 21 (23), 5 (10), 2 (7), 12 (6), 33 (3) |
| 79132 | 391 (120..515) | 291 | 59 | 4 (67), 14 (55), 13 (53), 5 (39), 21 (28), 9 (23), 2 (13), 20 (6), 33 (4), 12 (3) |
| 79128 | 402 (124..527) | 311 | 62 | 14 (91), 21 (84), 4 (30), 5 (28), 2 (20), 12 (13), 20 (12), 9 (11), 13 (11), 18 (11) |
| 79134 | 407 (127..533) | 333 | 52 | 2 (48), 4 (48), 21 (42), 20 (40), 12 (38), 14 (30), 5 (23), 13 (21), 18 (21), 35 (18), 9 (4) |
| 79135 | 409 (129..542) | 317 | 68 | 18 (84), 12 (53), 21 (39), 20 (36), 4 (36), 35 (35), 5 (23), 2 (9), 14 (2) |
| 79139 | 406 (132..537) | 318 | 56 | 35 (199), 20 (67), 12 (34), 5 (10), 4 (7), 21 (1) |
| 79136 | 393 (136..538) | 314 | 48 | 20 (175), 5 (54), 2 (42), 35 (41), 12 (1), 14 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 328/409/1007; tracks with internal gaps: 23; total internal gaps: 852; longest internal gap: 13; tracks ending in coasting: 22 (trailing rows total 579)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 912 | 95 | 67 | 5 | 0 | 78911 |
| 2 | 81..566 | 486 | 486 | 405 | 81 | 35 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 4 | 87..543 | 457 | 457 | 383 | 74 | 31 | 10 | 16 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 89..520 | 432 | 432 | 360 | 72 | 28 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 91..468 | 378 | 378 | 294 | 84 | 37 | 5 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 93..560 | 468 | 468 | 390 | 78 | 32 | 5 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..506 | 409 | 409 | 328 | 81 | 37 | 4 | 29 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 99..524 | 426 | 426 | 349 | 77 | 40 | 4 | 27 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 99..557 | 459 | 459 | 391 | 68 | 30 | 4 | 27 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 14 | 99..556 | 458 | 458 | 379 | 79 | 39 | 13 | 18 | 78897, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 16 | 105..457 | 353 | 353 | 280 | 73 | 40 | 5 | 12 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 17 | 108..462 | 355 | 355 | 278 | 77 | 36 | 4 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 112..571 | 460 | 460 | 376 | 84 | 38 | 4 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135 |
| 19 | 113..490 | 378 | 378 | 303 | 75 | 31 | 4 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 20 | 117..561 | 445 | 445 | 354 | 91 | 41 | 5 | 28 | 78897, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 125..560 | 436 | 436 | 350 | 86 | 38 | 5 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 132..474 | 343 | 343 | 270 | 73 | 31 | 6 | 24 | 78897, 78899, 78971, 79037, 79045 |
| 23 | 132..479 | 348 | 348 | 250 | 98 | 47 | 4 | 31 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 133..513 | 381 | 381 | 289 | 92 | 46 | 7 | 21 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 28 | 143..470 | 328 | 328 | 247 | 81 | 39 | 3 | 27 | 78897, 78971, 79037, 79045 |
| 31 | 176..510 | 335 | 335 | 269 | 66 | 32 | 3 | 27 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 33 | 179..529 | 351 | 351 | 288 | 63 | 29 | 3 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 35 | 210..566 | 357 | 357 | 293 | 64 | 28 | 3 | 29 | 79134, 79135, 79136, 79139 |
