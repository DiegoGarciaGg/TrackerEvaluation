# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=b1706121b6ca
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise1.0_fp0.0_seed1/tracks.csv sha256=70fcc5052aac42fa
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise1.0_fp0.0_seed1.csv sha256=b1706121b6ca3278
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise1.0_fp0.0_seed1
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
| observations | none | 4 | 0.282 | 0.138 | 0.587 | 1.27 | 0.316 | 1053 | 2089.0 |
| observations | none | 6 | 0.302 | 0.149 | 0.589 | 1.27 | 0.318 | 1048 | 2088.0 |
| observations | none | 8 | 0.313 | 0.156 | 0.589 | 1.31 | 0.320 | 1028 | 2083.0 |
| observations | none | 12 | 0.326 | 0.165 | 0.595 | 1.60 | 0.333 | 948 | 2025.0 |
| observations | ignore | 4 | 0.282 | 0.138 | 0.587 | 1.27 | 0.316 | 1053 | 2089.0 |
| observations | ignore | 6 | 0.302 | 0.149 | 0.589 | 1.27 | 0.318 | 1048 | 2088.0 |
| observations | ignore | 8 | 0.313 | 0.156 | 0.589 | 1.31 | 0.320 | 1028 | 2083.0 |
| observations | ignore | 12 | 0.326 | 0.165 | 0.595 | 1.60 | 0.333 | 948 | 2025.0 |
| updates | none | 4 | 0.272 | 0.144 | 0.364 | 1.34 | 0.292 | 1117 | 1948.0 |
| updates | none | 6 | 0.318 | 0.169 | 0.482 | 1.63 | 0.321 | 1117 | 1544.0 |
| updates | none | 8 | 0.347 | 0.185 | 0.602 | 2.03 | 0.352 | 1063 | 1127.0 |
| updates | none | 12 | 0.380 | 0.207 | 0.672 | 2.62 | 0.382 | 953 | 861.0 |
| updates | ignore | 4 | 0.272 | 0.144 | 0.364 | 1.34 | 0.292 | 1117 | 1948.0 |
| updates | ignore | 6 | 0.318 | 0.169 | 0.482 | 1.63 | 0.321 | 1117 | 1544.0 |
| updates | ignore | 8 | 0.347 | 0.185 | 0.602 | 2.03 | 0.352 | 1063 | 1127.0 |
| updates | ignore | 12 | 0.380 | 0.207 | 0.672 | 2.62 | 0.382 | 953 | 861.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 7013; unmatched reference entries: 3129; unmatched candidate entries: 10
- identity switches: 1028; fragmentation (coverage interruptions): 2148; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 5 -> 7 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 4 -> 5 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 5 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 4 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 5 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 5 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 5 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 4 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 5 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 5 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 5 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 4 -> 9 at (2124, 3028), 2 frames after previous cover
- f101: ref 79102: 12 -> 4 at (2136, 3025.5), 2 frames after previous cover
- f103: ref 78971: 14 -> 2 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 2 -> 7 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 9 -> 15 at (2100, 3028.5), 4 frames after previous cover
- f104: ref 79037: 7 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 2 -> 13 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 14 -> 2 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 12 -> 4 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78899: 5 -> 14 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 15 -> 5 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 9 -> 15 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 78897: 7 -> 5 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 2 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 15 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79045: 2 -> 7 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 5 -> 9 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 15 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79103: 9 -> 12 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78897: 5 -> 15 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 15 -> 7 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 9 -> 5 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 12 -> 9 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 4 -> 16 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 14 -> 15 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79105: 16 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79110: 12 -> 4 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78971: 2 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 7 -> 2 at (2013, 3034.5), 2 frames after previous cover
- f111: ref 79102: 4 -> 14 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 9 -> 5 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 16 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 15 -> 17 at (2015.5, 3032.5), 4 frames after previous cover
- f112: ref 79097: 5 -> 15 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 14 -> 5 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 5 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 4 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- ... 968 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 695 | 222 | 0 (695) |
| 78896 | 350 (76..429) | 233 | 74 | 17 (185), 11 (43), 2 (5) |
| 78969 | 352 (80..434) | 232 | 83 | 19 (100), 23 (73), 17 (25), 11 (16), 2 (11), 13 (7) |
| 78971 | 352 (84..439) | 228 | 81 | 23 (60), 26 (54), 11 (52), 19 (21), 21 (16), 2 (7), 17 (7), 13 (5), 7 (3), 14 (2), 5 (1) |
| 79045 | 355 (84..443) | 247 | 68 | 19 (66), 21 (64), 11 (59), 26 (25), 2 (10), 7 (5), 17 (5), 5 (4), 23 (4), 14 (3), 13 (2) |
| 79037 | 355 (86..445) | 249 | 68 | 26 (118), 5 (65), 2 (22), 19 (14), 21 (13), 7 (4), 17 (3), 4 (2), 13 (2), 11 (2), 9 (1), 14 (1), +2 more |
| 78897 | 345 (89..450) | 239 | 72 | 5 (66), 2 (60), 11 (41), 23 (24), 26 (12), 19 (11), 21 (10), 7 (6), 15 (3), 4 (2), 9 (1), 17 (1), +2 more |
| 78899 | 365 (91..455) | 254 | 79 | 2 (141), 5 (29), 11 (29), 23 (19), 15 (10), 14 (8), 22 (7), 4 (4), 9 (2), 17 (2), 26 (2), 19 (1) |
| 79097 | 366 (94..461) | 247 | 77 | 14 (115), 5 (29), 2 (27), 30 (16), 22 (13), 25 (12), 23 (10), 15 (7), 11 (6), 19 (4), 4 (2), 9 (2), +2 more |
| 79098 | 360 (97..467) | 249 | 77 | 30 (54), 21 (49), 5 (46), 14 (35), 29 (14), 11 (13), 19 (10), 22 (5), 9 (4), 23 (4), 7 (3), 13 (3), +4 more |
| 79102 | 371 (98..477) | 255 | 74 | 29 (52), 30 (52), 21 (37), 22 (36), 14 (23), 5 (15), 15 (14), 20 (9), 23 (8), 7 (3), 19 (3), 4 (2), +1 more |
| 79103 | 380 (99..481) | 274 | 76 | 30 (77), 22 (62), 29 (61), 14 (17), 7 (12), 19 (12), 5 (6), 15 (5), 20 (5), 4 (3), 9 (3), 21 (3), +5 more |
| 79105 | 379 (101..484) | 257 | 88 | 29 (75), 22 (60), 7 (40), 25 (26), 30 (12), 14 (10), 15 (7), 5 (7), 23 (5), 9 (4), 12 (2), 4 (2), +5 more |
| 79108 | 385 (104..492) | 283 | 75 | 22 (82), 18 (50), 7 (49), 14 (29), 20 (21), 15 (14), 25 (10), 23 (9), 9 (7), 12 (5), 13 (3), 5 (3), +1 more |
| 79110 | 388 (106..497) | 264 | 84 | 7 (93), 20 (33), 18 (29), 9 (23), 30 (20), 15 (18), 25 (14), 16 (10), 23 (7), 12 (5), 13 (5), 14 (4), +2 more |
| 79111 | 386 (109..500) | 271 | 87 | 20 (77), 9 (59), 15 (46), 18 (27), 7 (14), 14 (11), 25 (10), 16 (8), 12 (7), 4 (4), 13 (3), 29 (3), +1 more |
| 79115 | 421 (111..531) | 307 | 84 | 25 (103), 9 (58), 18 (50), 14 (25), 15 (22), 20 (13), 16 (11), 7 (8), 12 (6), 4 (5), 21 (5), 13 (1) |
| 79116 | 411 (114..530) | 278 | 86 | 16 (90), 9 (45), 12 (27), 20 (25), 7 (17), 21 (16), 14 (15), 25 (15), 13 (13), 18 (7), 29 (4), 15 (3), +1 more |
| 79122 | 404 (118..532) | 273 | 87 | 29 (40), 25 (37), 9 (36), 20 (34), 16 (32), 21 (29), 12 (17), 13 (17), 7 (15), 15 (8), 4 (3), 14 (3), +1 more |
| 79132 | 391 (120..515) | 274 | 80 | 12 (112), 16 (68), 9 (29), 25 (22), 7 (11), 15 (8), 21 (6), 20 (5), 4 (4), 13 (4), 18 (3), 14 (2) |
| 79128 | 402 (124..527) | 280 | 83 | 12 (78), 21 (55), 16 (34), 15 (25), 25 (25), 4 (22), 7 (21), 13 (8), 9 (4), 18 (3), 20 (3), 29 (2) |
| 79134 | 407 (127..533) | 290 | 87 | 4 (63), 9 (59), 12 (53), 13 (35), 16 (28), 15 (20), 25 (15), 7 (9), 18 (4), 20 (3), 21 (1) |
| 79135 | 409 (129..542) | 277 | 92 | 4 (118), 15 (37), 13 (33), 16 (30), 25 (20), 12 (18), 18 (11), 20 (9), 14 (1) |
| 79139 | 406 (132..537) | 273 | 88 | 15 (76), 4 (75), 13 (74), 18 (27), 20 (13), 25 (7), 16 (1) |
| 79136 | 393 (136..538) | 284 | 76 | 13 (110), 18 (71), 20 (61), 4 (39), 16 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 297/394/1007; tracks with internal gaps: 6; total internal gaps: 9; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 695 | 695 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 81..450 | 370 | 286 | 286 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 4 | 87..542 | 456 | 355 | 355 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 5 | 89..445 | 357 | 271 | 271 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 91..484 | 394 | 315 | 315 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 93..532 | 440 | 340 | 337 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..461 | 364 | 261 | 261 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 12 | 99..514 | 416 | 333 | 332 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 13 | 99..537 | 439 | 331 | 330 | 1 | 1 | 1 | 0 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..518 | 420 | 305 | 304 | 1 | 1 | 1 | 0 | 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79135 |
| 15 | 103..500 | 398 | 326 | 326 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 16 | 108..528 | 421 | 318 | 316 | 2 | 2 | 1 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 112..428 | 317 | 228 | 228 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 18 | 113..491 | 379 | 288 | 288 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 117..441 | 325 | 242 | 242 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 20 | 125..537 | 413 | 317 | 315 | 2 | 1 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 132..527 | 396 | 305 | 305 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 132..481 | 350 | 268 | 268 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 23 | 133..433 | 301 | 227 | 227 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 25 | 133..531 | 399 | 318 | 318 | 0 | 0 | 0 | 0 | 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 143..439 | 297 | 211 | 211 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 29 | 179..531 | 353 | 252 | 252 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79111, 79116, 79122, 79128 |
| 30 | 189..495 | 307 | 231 | 231 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79110 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 7013; unmatched reference entries: 3129; unmatched candidate entries: 10
- identity switches: 1028; fragmentation (coverage interruptions): 2148; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 5 -> 7 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 4 -> 5 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 5 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 4 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 5 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 5 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 5 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 4 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 5 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 5 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 5 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 4 -> 9 at (2124, 3028), 2 frames after previous cover
- f101: ref 79102: 12 -> 4 at (2136, 3025.5), 2 frames after previous cover
- f103: ref 78971: 14 -> 2 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 2 -> 7 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 9 -> 15 at (2100, 3028.5), 4 frames after previous cover
- f104: ref 79037: 7 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 2 -> 13 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 14 -> 2 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 12 -> 4 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78899: 5 -> 14 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 15 -> 5 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 9 -> 15 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 78897: 7 -> 5 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 2 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 15 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79045: 2 -> 7 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 5 -> 9 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 15 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79103: 9 -> 12 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78897: 5 -> 15 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 15 -> 7 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 9 -> 5 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 12 -> 9 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 4 -> 16 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 14 -> 15 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79105: 16 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79110: 12 -> 4 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78971: 2 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 7 -> 2 at (2013, 3034.5), 2 frames after previous cover
- f111: ref 79102: 4 -> 14 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 9 -> 5 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 16 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 15 -> 17 at (2015.5, 3032.5), 4 frames after previous cover
- f112: ref 79097: 5 -> 15 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 14 -> 5 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 5 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 4 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- ... 968 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 695 | 222 | 0 (695) |
| 78896 | 350 (76..429) | 233 | 74 | 17 (185), 11 (43), 2 (5) |
| 78969 | 352 (80..434) | 232 | 83 | 19 (100), 23 (73), 17 (25), 11 (16), 2 (11), 13 (7) |
| 78971 | 352 (84..439) | 228 | 81 | 23 (60), 26 (54), 11 (52), 19 (21), 21 (16), 2 (7), 17 (7), 13 (5), 7 (3), 14 (2), 5 (1) |
| 79045 | 355 (84..443) | 247 | 68 | 19 (66), 21 (64), 11 (59), 26 (25), 2 (10), 7 (5), 17 (5), 5 (4), 23 (4), 14 (3), 13 (2) |
| 79037 | 355 (86..445) | 249 | 68 | 26 (118), 5 (65), 2 (22), 19 (14), 21 (13), 7 (4), 17 (3), 4 (2), 13 (2), 11 (2), 9 (1), 14 (1), +2 more |
| 78897 | 345 (89..450) | 239 | 72 | 5 (66), 2 (60), 11 (41), 23 (24), 26 (12), 19 (11), 21 (10), 7 (6), 15 (3), 4 (2), 9 (1), 17 (1), +2 more |
| 78899 | 365 (91..455) | 254 | 79 | 2 (141), 5 (29), 11 (29), 23 (19), 15 (10), 14 (8), 22 (7), 4 (4), 9 (2), 17 (2), 26 (2), 19 (1) |
| 79097 | 366 (94..461) | 247 | 77 | 14 (115), 5 (29), 2 (27), 30 (16), 22 (13), 25 (12), 23 (10), 15 (7), 11 (6), 19 (4), 4 (2), 9 (2), +2 more |
| 79098 | 360 (97..467) | 249 | 77 | 30 (54), 21 (49), 5 (46), 14 (35), 29 (14), 11 (13), 19 (10), 22 (5), 9 (4), 23 (4), 7 (3), 13 (3), +4 more |
| 79102 | 371 (98..477) | 255 | 74 | 29 (52), 30 (52), 21 (37), 22 (36), 14 (23), 5 (15), 15 (14), 20 (9), 23 (8), 7 (3), 19 (3), 4 (2), +1 more |
| 79103 | 380 (99..481) | 274 | 76 | 30 (77), 22 (62), 29 (61), 14 (17), 7 (12), 19 (12), 5 (6), 15 (5), 20 (5), 4 (3), 9 (3), 21 (3), +5 more |
| 79105 | 379 (101..484) | 257 | 88 | 29 (75), 22 (60), 7 (40), 25 (26), 30 (12), 14 (10), 15 (7), 5 (7), 23 (5), 9 (4), 12 (2), 4 (2), +5 more |
| 79108 | 385 (104..492) | 283 | 75 | 22 (82), 18 (50), 7 (49), 14 (29), 20 (21), 15 (14), 25 (10), 23 (9), 9 (7), 12 (5), 13 (3), 5 (3), +1 more |
| 79110 | 388 (106..497) | 264 | 84 | 7 (93), 20 (33), 18 (29), 9 (23), 30 (20), 15 (18), 25 (14), 16 (10), 23 (7), 12 (5), 13 (5), 14 (4), +2 more |
| 79111 | 386 (109..500) | 271 | 87 | 20 (77), 9 (59), 15 (46), 18 (27), 7 (14), 14 (11), 25 (10), 16 (8), 12 (7), 4 (4), 13 (3), 29 (3), +1 more |
| 79115 | 421 (111..531) | 307 | 84 | 25 (103), 9 (58), 18 (50), 14 (25), 15 (22), 20 (13), 16 (11), 7 (8), 12 (6), 4 (5), 21 (5), 13 (1) |
| 79116 | 411 (114..530) | 278 | 86 | 16 (90), 9 (45), 12 (27), 20 (25), 7 (17), 21 (16), 14 (15), 25 (15), 13 (13), 18 (7), 29 (4), 15 (3), +1 more |
| 79122 | 404 (118..532) | 273 | 87 | 29 (40), 25 (37), 9 (36), 20 (34), 16 (32), 21 (29), 12 (17), 13 (17), 7 (15), 15 (8), 4 (3), 14 (3), +1 more |
| 79132 | 391 (120..515) | 274 | 80 | 12 (112), 16 (68), 9 (29), 25 (22), 7 (11), 15 (8), 21 (6), 20 (5), 4 (4), 13 (4), 18 (3), 14 (2) |
| 79128 | 402 (124..527) | 280 | 83 | 12 (78), 21 (55), 16 (34), 15 (25), 25 (25), 4 (22), 7 (21), 13 (8), 9 (4), 18 (3), 20 (3), 29 (2) |
| 79134 | 407 (127..533) | 290 | 87 | 4 (63), 9 (59), 12 (53), 13 (35), 16 (28), 15 (20), 25 (15), 7 (9), 18 (4), 20 (3), 21 (1) |
| 79135 | 409 (129..542) | 277 | 92 | 4 (118), 15 (37), 13 (33), 16 (30), 25 (20), 12 (18), 18 (11), 20 (9), 14 (1) |
| 79139 | 406 (132..537) | 273 | 88 | 15 (76), 4 (75), 13 (74), 18 (27), 20 (13), 25 (7), 16 (1) |
| 79136 | 393 (136..538) | 284 | 76 | 13 (110), 18 (71), 20 (61), 4 (39), 16 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 297/394/1007; tracks with internal gaps: 6; total internal gaps: 9; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 695 | 695 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 81..450 | 370 | 286 | 286 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 4 | 87..542 | 456 | 355 | 355 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 5 | 89..445 | 357 | 271 | 271 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 91..484 | 394 | 315 | 315 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 93..532 | 440 | 340 | 337 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..461 | 364 | 261 | 261 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 12 | 99..514 | 416 | 333 | 332 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 13 | 99..537 | 439 | 331 | 330 | 1 | 1 | 1 | 0 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..518 | 420 | 305 | 304 | 1 | 1 | 1 | 0 | 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79135 |
| 15 | 103..500 | 398 | 326 | 326 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 16 | 108..528 | 421 | 318 | 316 | 2 | 2 | 1 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 112..428 | 317 | 228 | 228 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 18 | 113..491 | 379 | 288 | 288 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 117..441 | 325 | 242 | 242 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 20 | 125..537 | 413 | 317 | 315 | 2 | 1 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 132..527 | 396 | 305 | 305 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 132..481 | 350 | 268 | 268 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 23 | 133..433 | 301 | 227 | 227 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 25 | 133..531 | 399 | 318 | 318 | 0 | 0 | 0 | 0 | 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 143..439 | 297 | 211 | 211 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 29 | 179..531 | 353 | 252 | 252 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79111, 79116, 79122, 79128 |
| 30 | 189..495 | 307 | 231 | 231 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79110 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 8562; unmatched reference entries: 1580; unmatched candidate entries: 1395
- identity switches: 1063; fragmentation (coverage interruptions): 1065; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 5 -> 7 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 4 -> 5 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 5 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 4 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 5 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 5 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 5 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 4 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 5 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 5 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 5 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 1 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 4 -> 9 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 12 -> 4 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78971: 14 -> 2 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 2 -> 7 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 9 -> 15 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79037: 7 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 2 -> 13 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 14 -> 2 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 12 -> 4 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78899: 5 -> 14 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 15 -> 5 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 9 -> 15 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 78897: 7 -> 5 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 2 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 15 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79045: 2 -> 7 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 5 -> 9 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 15 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79103: 9 -> 12 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78897: 5 -> 15 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 15 -> 7 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 9 -> 5 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 12 -> 9 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 4 -> 16 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 14 -> 15 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79105: 16 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79110: 12 -> 4 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78971: 2 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 7 -> 2 at (2013, 3034.5), 2 frames after previous cover
- f111: ref 79102: 4 -> 14 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 9 -> 5 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 16 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 15 -> 17 at (2015.5, 3032.5), 4 frames after previous cover
- f112: ref 79097: 5 -> 15 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 14 -> 5 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 5 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 4 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- ... 1003 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 961 | 34 | 0 (961) |
| 78896 | 350 (76..429) | 289 | 34 | 17 (233), 11 (50), 2 (6) |
| 78969 | 352 (80..434) | 287 | 37 | 19 (131), 23 (90), 17 (27), 11 (20), 2 (11), 13 (8) |
| 78971 | 352 (84..439) | 285 | 38 | 26 (73), 23 (73), 11 (66), 19 (23), 21 (18), 17 (11), 2 (8), 13 (6), 7 (4), 14 (2), 5 (1) |
| 79045 | 355 (84..443) | 297 | 34 | 19 (87), 21 (73), 11 (71), 26 (29), 2 (10), 23 (8), 7 (6), 17 (5), 5 (3), 14 (3), 13 (2) |
| 79037 | 355 (86..445) | 297 | 38 | 26 (140), 5 (82), 2 (23), 19 (14), 21 (12), 17 (6), 7 (5), 11 (4), 4 (2), 14 (2), 13 (2), 22 (2), +3 more |
| 78897 | 345 (89..450) | 286 | 38 | 5 (79), 2 (71), 11 (53), 23 (25), 26 (16), 21 (12), 19 (11), 7 (7), 4 (3), 15 (3), 9 (2), 22 (2), +2 more |
| 78899 | 365 (91..455) | 311 | 38 | 2 (172), 11 (40), 5 (33), 23 (23), 15 (10), 22 (10), 14 (9), 4 (4), 9 (3), 17 (3), 26 (2), 19 (1), +1 more |
| 79097 | 366 (94..461) | 290 | 52 | 14 (141), 2 (34), 5 (31), 30 (19), 22 (14), 25 (12), 23 (11), 15 (8), 11 (6), 19 (4), 4 (3), 9 (3), +2 more |
| 79098 | 360 (97..467) | 302 | 38 | 30 (66), 21 (64), 5 (53), 14 (44), 29 (18), 11 (15), 19 (12), 9 (5), 22 (5), 2 (4), 4 (3), 7 (3), +4 more |
| 79102 | 371 (98..477) | 306 | 44 | 29 (65), 30 (58), 21 (48), 22 (43), 14 (26), 5 (20), 15 (17), 23 (10), 20 (9), 7 (3), 19 (3), 12 (2), +1 more |
| 79103 | 380 (99..481) | 317 | 43 | 30 (95), 29 (73), 22 (72), 14 (18), 7 (14), 19 (12), 5 (6), 15 (5), 20 (5), 4 (3), 9 (3), 21 (3), +5 more |
| 79105 | 379 (101..484) | 308 | 52 | 29 (89), 22 (78), 7 (46), 25 (30), 30 (15), 14 (13), 5 (9), 15 (7), 23 (5), 9 (4), 18 (3), 12 (2), +5 more |
| 79108 | 385 (104..492) | 326 | 43 | 22 (94), 18 (69), 7 (53), 14 (28), 20 (23), 15 (17), 25 (12), 23 (11), 9 (7), 12 (5), 13 (3), 5 (3), +1 more |
| 79110 | 388 (106..497) | 322 | 47 | 7 (116), 20 (40), 18 (32), 30 (30), 9 (29), 15 (23), 25 (16), 16 (11), 23 (7), 12 (6), 13 (5), 14 (4), +2 more |
| 79111 | 386 (109..500) | 321 | 50 | 20 (95), 9 (71), 15 (54), 18 (32), 7 (17), 14 (12), 16 (10), 25 (9), 12 (8), 4 (4), 29 (4), 13 (3), +1 more |
| 79115 | 421 (111..531) | 361 | 46 | 25 (126), 9 (67), 18 (59), 14 (28), 15 (22), 20 (16), 16 (15), 7 (9), 4 (6), 12 (6), 21 (6), 13 (1) |
| 79116 | 411 (114..530) | 344 | 45 | 16 (106), 9 (59), 20 (33), 12 (30), 25 (21), 7 (20), 21 (19), 14 (18), 13 (17), 18 (9), 29 (6), 15 (5), +1 more |
| 79122 | 404 (118..532) | 334 | 48 | 29 (53), 9 (46), 25 (45), 20 (42), 16 (41), 21 (35), 13 (20), 12 (18), 7 (17), 15 (8), 4 (3), 14 (3), +1 more |
| 79132 | 391 (120..515) | 313 | 52 | 12 (130), 16 (78), 9 (32), 25 (26), 7 (11), 15 (9), 20 (6), 21 (6), 4 (5), 18 (4), 13 (4), 14 (2) |
| 79128 | 402 (124..527) | 332 | 48 | 12 (96), 21 (62), 16 (45), 15 (30), 25 (29), 4 (24), 7 (23), 13 (7), 29 (5), 18 (4), 9 (4), 20 (3) |
| 79134 | 407 (127..533) | 343 | 48 | 4 (75), 9 (75), 12 (62), 13 (42), 16 (31), 15 (21), 25 (19), 7 (9), 18 (5), 20 (3), 21 (1) |
| 79135 | 409 (129..542) | 341 | 49 | 4 (143), 15 (44), 13 (41), 16 (36), 25 (29), 12 (23), 18 (13), 20 (11), 14 (1) |
| 79139 | 406 (132..537) | 342 | 38 | 13 (102), 15 (96), 4 (88), 18 (39), 25 (10), 20 (6), 16 (1) |
| 79136 | 393 (136..538) | 347 | 31 | 13 (127), 18 (86), 20 (83), 4 (46), 16 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 326/423/1007; tracks with internal gaps: 23; total internal gaps: 533; longest internal gap: 33; tracks ending in coasting: 22 (trailing rows total 603)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 961 | 46 | 34 | 4 | 0 | 78911 |
| 2 | 81..479 | 399 | 399 | 339 | 60 | 22 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 4 | 87..571 | 485 | 485 | 419 | 66 | 27 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 5 | 89..474 | 386 | 386 | 320 | 66 | 23 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 91..513 | 423 | 423 | 365 | 58 | 20 | 4 | 29 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 93..561 | 469 | 469 | 411 | 58 | 21 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..490 | 393 | 393 | 325 | 68 | 28 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 12 | 99..543 | 445 | 445 | 389 | 56 | 23 | 9 | 16 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 13 | 99..566 | 468 | 468 | 398 | 70 | 27 | 4 | 29 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..547 | 449 | 449 | 354 | 95 | 21 | 33 | 29 | 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79135 |
| 15 | 103..529 | 427 | 427 | 382 | 45 | 13 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 16 | 108..557 | 450 | 450 | 380 | 70 | 34 | 3 | 26 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 112..457 | 346 | 346 | 286 | 60 | 29 | 7 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 18 | 113..520 | 408 | 408 | 360 | 48 | 15 | 3 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 117..470 | 354 | 354 | 298 | 56 | 21 | 4 | 27 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 20 | 125..566 | 442 | 442 | 379 | 63 | 23 | 5 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 132..556 | 425 | 425 | 361 | 64 | 26 | 5 | 26 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 132..510 | 379 | 379 | 321 | 58 | 24 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 23 | 133..462 | 330 | 330 | 271 | 59 | 21 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 25 | 133..560 | 428 | 428 | 386 | 42 | 13 | 2 | 28 | 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 143..468 | 326 | 326 | 260 | 66 | 25 | 4 | 32 | 78897, 78899, 78971, 79037, 79045 |
| 29 | 179..560 | 382 | 382 | 314 | 68 | 23 | 4 | 33 | 79098, 79102, 79103, 79105, 79108, 79111, 79116, 79122, 79128 |
| 30 | 189..524 | 336 | 336 | 283 | 53 | 20 | 4 | 27 | 79097, 79098, 79102, 79103, 79105, 79110 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 8562; unmatched reference entries: 1580; unmatched candidate entries: 1395
- identity switches: 1063; fragmentation (coverage interruptions): 1065; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 5 -> 7 at (2108.5, 3033.5), 2 frames after previous cover
- f92: ref 79037: 4 -> 5 at (2124, 3034), 4 frames after previous cover
- f93: ref 79037: 5 -> 9 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 4 -> 9 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 9 -> 5 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 7 -> 2 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 5 -> 7 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 9 -> 5 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 4 -> 9 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 5 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 7 -> 2 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 2 -> 11 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 5 -> 7 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 9 -> 5 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 2 -> 13 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 2 -> 14 at (2059.5, 3034), 4 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 1 frames after previous cover
- f100: ref 79037: 7 -> 2 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 2 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 4 -> 9 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 12 -> 4 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78971: 14 -> 2 at (2033, 3032.5), 3 frames after previous cover
- f103: ref 79037: 2 -> 7 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 9 -> 15 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79037: 7 -> 14 at (2051, 3034), 1 frames after previous cover
- f105: ref 78971: 2 -> 13 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 14 -> 2 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79105: 12 -> 4 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78899: 5 -> 14 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 78969: 13 -> 11 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 15 -> 5 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 9 -> 15 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 4 -> 9 at (2116.5, 3023), 2 frames after previous cover
- f107: ref 78897: 7 -> 5 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78969: 11 -> 13 at (1989, 3034.5), 1 frames after previous cover
- f107: ref 78971: 13 -> 2 at (2009.5, 3033), 1 frames after previous cover
- f107: ref 79037: 14 -> 15 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79045: 2 -> 7 at (2019, 3033.5), 1 frames after previous cover
- f107: ref 79097: 5 -> 9 at (2076.5, 3029), 1 frames after previous cover
- f107: ref 79098: 15 -> 4 at (2090, 3028), 1 frames after previous cover
- f107: ref 79103: 9 -> 12 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78897: 5 -> 15 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 15 -> 7 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 9 -> 5 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79103: 12 -> 9 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 4 -> 16 at (2113.5, 3025), 2 frames after previous cover
- f109: ref 78899: 14 -> 15 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 79105: 16 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79110: 12 -> 4 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78971: 2 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 7 -> 2 at (2013, 3034.5), 2 frames after previous cover
- f111: ref 79102: 4 -> 14 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 9 -> 5 at (2087.5, 3023.5), 3 frames after previous cover
- f111: ref 79111: 16 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 15 -> 17 at (2015.5, 3032.5), 4 frames after previous cover
- f112: ref 79097: 5 -> 15 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79098: 14 -> 5 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79103: 5 -> 9 at (2082, 3024), 1 frames after previous cover
- f112: ref 79110: 4 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- ... 1003 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 961 | 34 | 0 (961) |
| 78896 | 350 (76..429) | 289 | 34 | 17 (233), 11 (50), 2 (6) |
| 78969 | 352 (80..434) | 287 | 37 | 19 (131), 23 (90), 17 (27), 11 (20), 2 (11), 13 (8) |
| 78971 | 352 (84..439) | 285 | 38 | 26 (73), 23 (73), 11 (66), 19 (23), 21 (18), 17 (11), 2 (8), 13 (6), 7 (4), 14 (2), 5 (1) |
| 79045 | 355 (84..443) | 297 | 34 | 19 (87), 21 (73), 11 (71), 26 (29), 2 (10), 23 (8), 7 (6), 17 (5), 5 (3), 14 (3), 13 (2) |
| 79037 | 355 (86..445) | 297 | 38 | 26 (140), 5 (82), 2 (23), 19 (14), 21 (12), 17 (6), 7 (5), 11 (4), 4 (2), 14 (2), 13 (2), 22 (2), +3 more |
| 78897 | 345 (89..450) | 286 | 38 | 5 (79), 2 (71), 11 (53), 23 (25), 26 (16), 21 (12), 19 (11), 7 (7), 4 (3), 15 (3), 9 (2), 22 (2), +2 more |
| 78899 | 365 (91..455) | 311 | 38 | 2 (172), 11 (40), 5 (33), 23 (23), 15 (10), 22 (10), 14 (9), 4 (4), 9 (3), 17 (3), 26 (2), 19 (1), +1 more |
| 79097 | 366 (94..461) | 290 | 52 | 14 (141), 2 (34), 5 (31), 30 (19), 22 (14), 25 (12), 23 (11), 15 (8), 11 (6), 19 (4), 4 (3), 9 (3), +2 more |
| 79098 | 360 (97..467) | 302 | 38 | 30 (66), 21 (64), 5 (53), 14 (44), 29 (18), 11 (15), 19 (12), 9 (5), 22 (5), 2 (4), 4 (3), 7 (3), +4 more |
| 79102 | 371 (98..477) | 306 | 44 | 29 (65), 30 (58), 21 (48), 22 (43), 14 (26), 5 (20), 15 (17), 23 (10), 20 (9), 7 (3), 19 (3), 12 (2), +1 more |
| 79103 | 380 (99..481) | 317 | 43 | 30 (95), 29 (73), 22 (72), 14 (18), 7 (14), 19 (12), 5 (6), 15 (5), 20 (5), 4 (3), 9 (3), 21 (3), +5 more |
| 79105 | 379 (101..484) | 308 | 52 | 29 (89), 22 (78), 7 (46), 25 (30), 30 (15), 14 (13), 5 (9), 15 (7), 23 (5), 9 (4), 18 (3), 12 (2), +5 more |
| 79108 | 385 (104..492) | 326 | 43 | 22 (94), 18 (69), 7 (53), 14 (28), 20 (23), 15 (17), 25 (12), 23 (11), 9 (7), 12 (5), 13 (3), 5 (3), +1 more |
| 79110 | 388 (106..497) | 322 | 47 | 7 (116), 20 (40), 18 (32), 30 (30), 9 (29), 15 (23), 25 (16), 16 (11), 23 (7), 12 (6), 13 (5), 14 (4), +2 more |
| 79111 | 386 (109..500) | 321 | 50 | 20 (95), 9 (71), 15 (54), 18 (32), 7 (17), 14 (12), 16 (10), 25 (9), 12 (8), 4 (4), 29 (4), 13 (3), +1 more |
| 79115 | 421 (111..531) | 361 | 46 | 25 (126), 9 (67), 18 (59), 14 (28), 15 (22), 20 (16), 16 (15), 7 (9), 4 (6), 12 (6), 21 (6), 13 (1) |
| 79116 | 411 (114..530) | 344 | 45 | 16 (106), 9 (59), 20 (33), 12 (30), 25 (21), 7 (20), 21 (19), 14 (18), 13 (17), 18 (9), 29 (6), 15 (5), +1 more |
| 79122 | 404 (118..532) | 334 | 48 | 29 (53), 9 (46), 25 (45), 20 (42), 16 (41), 21 (35), 13 (20), 12 (18), 7 (17), 15 (8), 4 (3), 14 (3), +1 more |
| 79132 | 391 (120..515) | 313 | 52 | 12 (130), 16 (78), 9 (32), 25 (26), 7 (11), 15 (9), 20 (6), 21 (6), 4 (5), 18 (4), 13 (4), 14 (2) |
| 79128 | 402 (124..527) | 332 | 48 | 12 (96), 21 (62), 16 (45), 15 (30), 25 (29), 4 (24), 7 (23), 13 (7), 29 (5), 18 (4), 9 (4), 20 (3) |
| 79134 | 407 (127..533) | 343 | 48 | 4 (75), 9 (75), 12 (62), 13 (42), 16 (31), 15 (21), 25 (19), 7 (9), 18 (5), 20 (3), 21 (1) |
| 79135 | 409 (129..542) | 341 | 49 | 4 (143), 15 (44), 13 (41), 16 (36), 25 (29), 12 (23), 18 (13), 20 (11), 14 (1) |
| 79139 | 406 (132..537) | 342 | 38 | 13 (102), 15 (96), 4 (88), 18 (39), 25 (10), 20 (6), 16 (1) |
| 79136 | 393 (136..538) | 347 | 31 | 13 (127), 18 (86), 20 (83), 4 (46), 16 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 326/423/1007; tracks with internal gaps: 23; total internal gaps: 533; longest internal gap: 33; tracks ending in coasting: 22 (trailing rows total 603)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 961 | 46 | 34 | 4 | 0 | 78911 |
| 2 | 81..479 | 399 | 399 | 339 | 60 | 22 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 4 | 87..571 | 485 | 485 | 419 | 66 | 27 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 5 | 89..474 | 386 | 386 | 320 | 66 | 23 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 91..513 | 423 | 423 | 365 | 58 | 20 | 4 | 29 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 9 | 93..561 | 469 | 469 | 411 | 58 | 21 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 11 | 98..490 | 393 | 393 | 325 | 68 | 28 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 12 | 99..543 | 445 | 445 | 389 | 56 | 23 | 9 | 16 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 13 | 99..566 | 468 | 468 | 398 | 70 | 27 | 4 | 29 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..547 | 449 | 449 | 354 | 95 | 21 | 33 | 29 | 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79135 |
| 15 | 103..529 | 427 | 427 | 382 | 45 | 13 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 16 | 108..557 | 450 | 450 | 380 | 70 | 34 | 3 | 26 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 112..457 | 346 | 346 | 286 | 60 | 29 | 7 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 18 | 113..520 | 408 | 408 | 360 | 48 | 15 | 3 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 117..470 | 354 | 354 | 298 | 56 | 21 | 4 | 27 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 20 | 125..566 | 442 | 442 | 379 | 63 | 23 | 5 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 132..556 | 425 | 425 | 361 | 64 | 26 | 5 | 26 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 132..510 | 379 | 379 | 321 | 58 | 24 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 23 | 133..462 | 330 | 330 | 271 | 59 | 21 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 25 | 133..560 | 428 | 428 | 386 | 42 | 13 | 2 | 28 | 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 143..468 | 326 | 326 | 260 | 66 | 25 | 4 | 32 | 78897, 78899, 78971, 79037, 79045 |
| 29 | 179..560 | 382 | 382 | 314 | 68 | 23 | 4 | 33 | 79098, 79102, 79103, 79105, 79108, 79111, 79116, 79122, 79128 |
| 30 | 189..524 | 336 | 336 | 283 | 53 | 20 | 4 | 27 | 79097, 79098, 79102, 79103, 79105, 79110 |
