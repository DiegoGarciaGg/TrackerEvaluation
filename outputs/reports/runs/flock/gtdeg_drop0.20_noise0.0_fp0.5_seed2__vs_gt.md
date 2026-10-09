# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=4acc6d78f88f
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise0.0_fp0.5_seed2/tracks.csv sha256=4a4911d43ac8192f
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise0.0_fp0.5_seed2.csv sha256=4acc6d78f88f8d56
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise0.0_fp0.5_seed2
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
| observations | none | 4 | 0.364 | 0.169 | 0.700 | 0.01 | 0.332 | 835 | 1607.0 |
| observations | none | 6 | 0.364 | 0.170 | 0.701 | 0.01 | 0.332 | 835 | 1604.0 |
| observations | none | 8 | 0.364 | 0.172 | 0.701 | 0.02 | 0.335 | 835 | 1601.0 |
| observations | none | 12 | 0.365 | 0.176 | 0.705 | 0.27 | 0.346 | 783 | 1571.0 |
| observations | ignore | 4 | 0.364 | 0.169 | 0.700 | 0.01 | 0.332 | 835 | 1607.0 |
| observations | ignore | 6 | 0.364 | 0.170 | 0.701 | 0.01 | 0.332 | 835 | 1604.0 |
| observations | ignore | 8 | 0.364 | 0.172 | 0.701 | 0.02 | 0.335 | 835 | 1601.0 |
| observations | ignore | 12 | 0.365 | 0.176 | 0.705 | 0.27 | 0.346 | 783 | 1571.0 |
| updates | none | 4 | 0.335 | 0.168 | 0.469 | 0.08 | 0.300 | 863 | 1516.0 |
| updates | none | 6 | 0.355 | 0.179 | 0.565 | 0.37 | 0.323 | 865 | 1132.0 |
| updates | none | 8 | 0.367 | 0.186 | 0.663 | 0.73 | 0.345 | 831 | 759.0 |
| updates | none | 12 | 0.382 | 0.197 | 0.696 | 1.15 | 0.363 | 764 | 624.0 |
| updates | ignore | 4 | 0.335 | 0.168 | 0.469 | 0.08 | 0.300 | 863 | 1516.0 |
| updates | ignore | 6 | 0.355 | 0.179 | 0.565 | 0.37 | 0.323 | 865 | 1132.0 |
| updates | ignore | 8 | 0.367 | 0.186 | 0.663 | 0.73 | 0.345 | 831 | 759.0 |
| updates | ignore | 12 | 0.382 | 0.197 | 0.696 | 1.15 | 0.363 | 764 | 624.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7992; unmatched reference entries: 2150; unmatched candidate entries: 51
- identity switches: 835; fragmentation (coverage interruptions): 1603; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 32 -> 41 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 42 -> 32 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 38 -> 42 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 38 -> 42 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 42 -> 32 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 32 -> 41 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 32 -> 50 at (2090.5, 3032.5), 4 frames after previous cover
- f95: ref 79037: 42 -> 32 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 41 -> 53 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 78897: 38 -> 42 at (2112.5, 3033), 1 frames after previous cover
- f97: ref 78971: 50 -> 32 at (2072, 3034.5), 2 frames after previous cover
- f97: ref 79045: 32 -> 50 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 49 -> 38 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 32 -> 50 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 50 -> 32 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 49 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 42 -> 38 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 32 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 38 -> 42 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 42 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 42 -> 62 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 49 -> 61 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 49 -> 63 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 42 -> 62 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 62 -> 32 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 49 -> 63 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 63 -> 61 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 32 -> 69 at (2014.5, 3034), 6 frames after previous cover
- f108: ref 79103: 63 -> 70 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 63 -> 67 at (2113.5, 3025), 2 frames after previous cover
- f108: ref 79110: 49 -> 68 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 61 -> 38 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79108: 49 -> 63 at (2125, 3025), 4 frames after previous cover
- f110: ref 79098: 38 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 61 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 67 -> 70 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 63 -> 67 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 68 -> 63 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 38 -> 61 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 70 -> 67 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 67 -> 63 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 61 -> 70 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 63 -> 68 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 70 -> 63 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 42 -> 69 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 69 -> 50 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 38 -> 62 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 70 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 67 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 63 -> 67 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 68 -> 70 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 62 -> 69 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 69 -> 61 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 32 -> 69 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 50 -> 32 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79116: 49 -> 77 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 79037: 69 -> 32 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 61 -> 62 at (2010.5, 3030), 3 frames after previous cover
- f118: ref 79098: 62 -> 38 at (2024.5, 3030.5), 1 frames after previous cover
- ... 775 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 171 | 0 (799) |
| 78896 | 350 (76..429) | 285 | 46 | 106 (92), 63 (70), 53 (66), 69 (30), 38 (14), 41 (8), 32 (5) |
| 78969 | 352 (80..434) | 276 | 55 | 61 (69), 106 (66), 41 (44), 62 (37), 53 (29), 38 (20), 69 (5), 32 (4), 63 (2) |
| 78971 | 352 (84..439) | 265 | 61 | 41 (79), 62 (41), 50 (35), 38 (32), 42 (28), 106 (27), 53 (7), 32 (5), 69 (4), 133 (4), 61 (3) |
| 79045 | 355 (84..443) | 281 | 51 | 38 (126), 41 (46), 50 (44), 32 (23), 53 (10), 69 (8), 133 (8), 42 (6), 61 (4), 62 (3), 106 (2), 63 (1) |
| 79037 | 355 (86..445) | 273 | 56 | 62 (54), 41 (43), 106 (42), 133 (33), 53 (23), 32 (22), 38 (14), 104 (12), 42 (10), 50 (9), 69 (7), 63 (2), +2 more |
| 78897 | 345 (89..450) | 271 | 57 | 42 (67), 41 (38), 123 (32), 38 (29), 53 (26), 62 (23), 69 (16), 50 (15), 104 (9), 106 (6), 79 (3), 61 (3), +2 more |
| 78899 | 365 (91..455) | 274 | 66 | 53 (91), 61 (55), 104 (34), 38 (25), 42 (22), 62 (12), 50 (10), 41 (7), 32 (6), 79 (5), 106 (3), 49 (1), +3 more |
| 79097 | 366 (94..461) | 290 | 58 | 104 (139), 61 (42), 42 (40), 38 (16), 62 (13), 79 (11), 53 (10), 83 (7), 123 (7), 49 (3), 106 (2) |
| 79098 | 360 (97..467) | 296 | 50 | 123 (85), 104 (57), 41 (41), 53 (38), 61 (16), 62 (16), 38 (9), 79 (9), 156 (9), 83 (8), 32 (5), 49 (3) |
| 79102 | 371 (98..477) | 295 | 59 | 156 (73), 123 (63), 83 (60), 62 (49), 32 (19), 79 (7), 104 (5), 61 (4), 49 (3), 38 (3), 53 (3), 70 (2), +3 more |
| 79103 | 380 (99..481) | 295 | 57 | 83 (94), 156 (63), 123 (32), 63 (20), 42 (20), 62 (18), 32 (18), 67 (14), 38 (10), 70 (3), 130 (3) |
| 79105 | 379 (101..484) | 290 | 70 | 67 (100), 83 (47), 32 (33), 156 (24), 63 (19), 42 (15), 41 (15), 38 (13), 62 (10), 84 (8), 70 (2), 68 (2), +2 more |
| 79108 | 385 (104..492) | 313 | 55 | 84 (95), 67 (58), 42 (49), 130 (29), 68 (28), 83 (18), 32 (18), 63 (10), 62 (4), 49 (2), 106 (1), 91 (1) |
| 79110 | 388 (106..497) | 308 | 60 | 32 (85), 67 (65), 84 (41), 130 (32), 68 (31), 42 (31), 83 (9), 63 (6), 70 (5), 91 (2), 49 (1) |
| 79111 | 386 (109..500) | 304 | 62 | 68 (115), 83 (47), 67 (36), 32 (33), 91 (22), 84 (15), 157 (12), 63 (11), 130 (7), 49 (2), 77 (2), 70 (1), +1 more |
| 79115 | 421 (111..531) | 316 | 75 | 91 (143), 68 (47), 63 (26), 130 (22), 157 (21), 84 (17), 67 (16), 32 (11), 77 (7), 70 (3), 49 (2), 83 (1) |
| 79116 | 411 (114..530) | 346 | 51 | 124 (73), 68 (71), 190 (52), 63 (41), 91 (30), 77 (26), 130 (17), 67 (13), 84 (10), 70 (4), 157 (4), 49 (3), +2 more |
| 79122 | 404 (118..532) | 326 | 65 | 92 (94), 91 (46), 84 (39), 63 (39), 68 (37), 130 (29), 77 (13), 157 (13), 32 (13), 49 (3) |
| 79132 | 391 (120..515) | 298 | 64 | 157 (73), 91 (57), 130 (43), 77 (31), 92 (31), 63 (26), 84 (15), 68 (13), 70 (3), 49 (2), 85 (2), 32 (1), +1 more |
| 79128 | 402 (124..527) | 319 | 64 | 130 (91), 157 (68), 84 (41), 77 (35), 91 (32), 124 (14), 49 (10), 92 (9), 32 (7), 85 (6), 70 (6) |
| 79134 | 407 (127..533) | 329 | 63 | 124 (104), 92 (41), 190 (41), 77 (38), 32 (35), 70 (32), 84 (16), 49 (10), 85 (5), 157 (5), 91 (2) |
| 79135 | 409 (129..542) | 320 | 61 | 124 (96), 49 (67), 77 (60), 214 (33), 92 (29), 85 (28), 84 (5), 190 (2) |
| 79139 | 406 (132..537) | 323 | 62 | 92 (114), 77 (95), 49 (92), 214 (12), 70 (8), 124 (1), 190 (1) |
| 79136 | 393 (136..538) | 300 | 64 | 49 (154), 190 (50), 214 (45), 77 (43), 92 (8) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 78 | 122..122 | 1 | 0 | 1 |
| 113 | 167..167 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/328/1007; tracks with internal gaps: 10; total internal gaps: 27; longest internal gap: 1; tracks ending in coasting: 10 (trailing rows total 24)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 811 | 799 | 12 | 12 | 1 | 0 | 78911 |
| 32 | 78..495 | 418 | 345 | 345 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 38 | 84..443 | 360 | 312 | 311 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 41 | 87..484 | 398 | 323 | 321 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79105 |
| 42 | 87..439 | 353 | 291 | 289 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 49 | 93..632 | 540 | 366 | 359 | 7 | 0 | 0 | 7 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 94..239 | 146 | 115 | 113 | 2 | 0 | 0 | 2 | 78897, 78899, 78971, 79037, 79045 |
| 53 | 96..455 | 360 | 303 | 303 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..333 | 231 | 198 | 197 | 1 | 0 | 0 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 62 | 103..434 | 332 | 280 | 280 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 63 | 103..429 | 327 | 276 | 274 | 2 | 2 | 1 | 0 | 78896, 78969, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 67 | 108..495 | 388 | 305 | 304 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 68 | 108..500 | 393 | 345 | 345 | 0 | 0 | 0 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 69 | 108..247 | 140 | 76 | 71 | 5 | 0 | 0 | 5 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 70 | 108..190 | 83 | 71 | 69 | 2 | 0 | 0 | 2 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79139 |
| 77 | 117..536 | 420 | 352 | 350 | 2 | 2 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 78 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 79 | 122..166 | 45 | 37 | 35 | 2 | 0 | 0 | 2 | 78897, 78899, 79097, 79098, 79102 |
| 83 | 126..477 | 352 | 292 | 292 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 84 | 126..491 | 366 | 302 | 302 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 85 | 126..175 | 50 | 42 | 41 | 1 | 0 | 0 | 1 | 79128, 79132, 79134, 79135 |
| 91 | 136..531 | 396 | 336 | 335 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 92 | 138..532 | 395 | 327 | 327 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 104 | 158..467 | 310 | 256 | 256 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 106 | 158..445 | 288 | 241 | 241 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79108 |
| 113 | 167..167 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 123 | 184..450 | 267 | 222 | 222 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 124 | 186..533 | 348 | 292 | 289 | 3 | 3 | 1 | 0 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 130 | 200..527 | 328 | 273 | 273 | 0 | 0 | 0 | 0 | 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 133 | 205..269 | 65 | 50 | 48 | 2 | 0 | 0 | 2 | 78897, 78971, 79037, 79045 |
| 156 | 274..481 | 208 | 170 | 169 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105 |
| 157 | 274..515 | 242 | 196 | 196 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 190 | 350..530 | 181 | 146 | 146 | 0 | 0 | 0 | 0 | 79116, 79134, 79135, 79136, 79139 |
| 214 | 427..538 | 112 | 90 | 90 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7992; unmatched reference entries: 2150; unmatched candidate entries: 51
- identity switches: 835; fragmentation (coverage interruptions): 1603; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 32 -> 41 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 42 -> 32 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 38 -> 42 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 38 -> 42 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 42 -> 32 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 32 -> 41 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 32 -> 50 at (2090.5, 3032.5), 4 frames after previous cover
- f95: ref 79037: 42 -> 32 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 41 -> 53 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 78897: 38 -> 42 at (2112.5, 3033), 1 frames after previous cover
- f97: ref 78971: 50 -> 32 at (2072, 3034.5), 2 frames after previous cover
- f97: ref 79045: 32 -> 50 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 49 -> 38 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 32 -> 50 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 50 -> 32 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 49 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 42 -> 38 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 32 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 38 -> 42 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 42 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 42 -> 62 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 49 -> 61 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 49 -> 63 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 42 -> 62 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 62 -> 32 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 49 -> 63 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 63 -> 61 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 32 -> 69 at (2014.5, 3034), 6 frames after previous cover
- f108: ref 79103: 63 -> 70 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 63 -> 67 at (2113.5, 3025), 2 frames after previous cover
- f108: ref 79110: 49 -> 68 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 61 -> 38 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79108: 49 -> 63 at (2125, 3025), 4 frames after previous cover
- f110: ref 79098: 38 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 61 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 67 -> 70 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 63 -> 67 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 68 -> 63 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 38 -> 61 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 70 -> 67 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 67 -> 63 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 61 -> 70 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 63 -> 68 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 70 -> 63 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 42 -> 69 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 69 -> 50 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 38 -> 62 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 70 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 67 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 63 -> 67 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 68 -> 70 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 62 -> 69 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 69 -> 61 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 32 -> 69 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 50 -> 32 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79116: 49 -> 77 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 79037: 69 -> 32 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 61 -> 62 at (2010.5, 3030), 3 frames after previous cover
- f118: ref 79098: 62 -> 38 at (2024.5, 3030.5), 1 frames after previous cover
- ... 775 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 171 | 0 (799) |
| 78896 | 350 (76..429) | 285 | 46 | 106 (92), 63 (70), 53 (66), 69 (30), 38 (14), 41 (8), 32 (5) |
| 78969 | 352 (80..434) | 276 | 55 | 61 (69), 106 (66), 41 (44), 62 (37), 53 (29), 38 (20), 69 (5), 32 (4), 63 (2) |
| 78971 | 352 (84..439) | 265 | 61 | 41 (79), 62 (41), 50 (35), 38 (32), 42 (28), 106 (27), 53 (7), 32 (5), 69 (4), 133 (4), 61 (3) |
| 79045 | 355 (84..443) | 281 | 51 | 38 (126), 41 (46), 50 (44), 32 (23), 53 (10), 69 (8), 133 (8), 42 (6), 61 (4), 62 (3), 106 (2), 63 (1) |
| 79037 | 355 (86..445) | 273 | 56 | 62 (54), 41 (43), 106 (42), 133 (33), 53 (23), 32 (22), 38 (14), 104 (12), 42 (10), 50 (9), 69 (7), 63 (2), +2 more |
| 78897 | 345 (89..450) | 271 | 57 | 42 (67), 41 (38), 123 (32), 38 (29), 53 (26), 62 (23), 69 (16), 50 (15), 104 (9), 106 (6), 79 (3), 61 (3), +2 more |
| 78899 | 365 (91..455) | 274 | 66 | 53 (91), 61 (55), 104 (34), 38 (25), 42 (22), 62 (12), 50 (10), 41 (7), 32 (6), 79 (5), 106 (3), 49 (1), +3 more |
| 79097 | 366 (94..461) | 290 | 58 | 104 (139), 61 (42), 42 (40), 38 (16), 62 (13), 79 (11), 53 (10), 83 (7), 123 (7), 49 (3), 106 (2) |
| 79098 | 360 (97..467) | 296 | 50 | 123 (85), 104 (57), 41 (41), 53 (38), 61 (16), 62 (16), 38 (9), 79 (9), 156 (9), 83 (8), 32 (5), 49 (3) |
| 79102 | 371 (98..477) | 295 | 59 | 156 (73), 123 (63), 83 (60), 62 (49), 32 (19), 79 (7), 104 (5), 61 (4), 49 (3), 38 (3), 53 (3), 70 (2), +3 more |
| 79103 | 380 (99..481) | 295 | 57 | 83 (94), 156 (63), 123 (32), 63 (20), 42 (20), 62 (18), 32 (18), 67 (14), 38 (10), 70 (3), 130 (3) |
| 79105 | 379 (101..484) | 290 | 70 | 67 (100), 83 (47), 32 (33), 156 (24), 63 (19), 42 (15), 41 (15), 38 (13), 62 (10), 84 (8), 70 (2), 68 (2), +2 more |
| 79108 | 385 (104..492) | 313 | 55 | 84 (95), 67 (58), 42 (49), 130 (29), 68 (28), 83 (18), 32 (18), 63 (10), 62 (4), 49 (2), 106 (1), 91 (1) |
| 79110 | 388 (106..497) | 308 | 60 | 32 (85), 67 (65), 84 (41), 130 (32), 68 (31), 42 (31), 83 (9), 63 (6), 70 (5), 91 (2), 49 (1) |
| 79111 | 386 (109..500) | 304 | 62 | 68 (115), 83 (47), 67 (36), 32 (33), 91 (22), 84 (15), 157 (12), 63 (11), 130 (7), 49 (2), 77 (2), 70 (1), +1 more |
| 79115 | 421 (111..531) | 316 | 75 | 91 (143), 68 (47), 63 (26), 130 (22), 157 (21), 84 (17), 67 (16), 32 (11), 77 (7), 70 (3), 49 (2), 83 (1) |
| 79116 | 411 (114..530) | 346 | 51 | 124 (73), 68 (71), 190 (52), 63 (41), 91 (30), 77 (26), 130 (17), 67 (13), 84 (10), 70 (4), 157 (4), 49 (3), +2 more |
| 79122 | 404 (118..532) | 326 | 65 | 92 (94), 91 (46), 84 (39), 63 (39), 68 (37), 130 (29), 77 (13), 157 (13), 32 (13), 49 (3) |
| 79132 | 391 (120..515) | 298 | 64 | 157 (73), 91 (57), 130 (43), 77 (31), 92 (31), 63 (26), 84 (15), 68 (13), 70 (3), 49 (2), 85 (2), 32 (1), +1 more |
| 79128 | 402 (124..527) | 319 | 64 | 130 (91), 157 (68), 84 (41), 77 (35), 91 (32), 124 (14), 49 (10), 92 (9), 32 (7), 85 (6), 70 (6) |
| 79134 | 407 (127..533) | 329 | 63 | 124 (104), 92 (41), 190 (41), 77 (38), 32 (35), 70 (32), 84 (16), 49 (10), 85 (5), 157 (5), 91 (2) |
| 79135 | 409 (129..542) | 320 | 61 | 124 (96), 49 (67), 77 (60), 214 (33), 92 (29), 85 (28), 84 (5), 190 (2) |
| 79139 | 406 (132..537) | 323 | 62 | 92 (114), 77 (95), 49 (92), 214 (12), 70 (8), 124 (1), 190 (1) |
| 79136 | 393 (136..538) | 300 | 64 | 49 (154), 190 (50), 214 (45), 77 (43), 92 (8) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 78 | 122..122 | 1 | 0 | 1 |
| 113 | 167..167 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/328/1007; tracks with internal gaps: 10; total internal gaps: 27; longest internal gap: 1; tracks ending in coasting: 10 (trailing rows total 24)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 811 | 799 | 12 | 12 | 1 | 0 | 78911 |
| 32 | 78..495 | 418 | 345 | 345 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 38 | 84..443 | 360 | 312 | 311 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 41 | 87..484 | 398 | 323 | 321 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79105 |
| 42 | 87..439 | 353 | 291 | 289 | 2 | 2 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 49 | 93..632 | 540 | 366 | 359 | 7 | 0 | 0 | 7 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 94..239 | 146 | 115 | 113 | 2 | 0 | 0 | 2 | 78897, 78899, 78971, 79037, 79045 |
| 53 | 96..455 | 360 | 303 | 303 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..333 | 231 | 198 | 197 | 1 | 0 | 0 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 62 | 103..434 | 332 | 280 | 280 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 63 | 103..429 | 327 | 276 | 274 | 2 | 2 | 1 | 0 | 78896, 78969, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 67 | 108..495 | 388 | 305 | 304 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 68 | 108..500 | 393 | 345 | 345 | 0 | 0 | 0 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 69 | 108..247 | 140 | 76 | 71 | 5 | 0 | 0 | 5 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 70 | 108..190 | 83 | 71 | 69 | 2 | 0 | 0 | 2 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79139 |
| 77 | 117..536 | 420 | 352 | 350 | 2 | 2 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 78 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 79 | 122..166 | 45 | 37 | 35 | 2 | 0 | 0 | 2 | 78897, 78899, 79097, 79098, 79102 |
| 83 | 126..477 | 352 | 292 | 292 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 84 | 126..491 | 366 | 302 | 302 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 85 | 126..175 | 50 | 42 | 41 | 1 | 0 | 0 | 1 | 79128, 79132, 79134, 79135 |
| 91 | 136..531 | 396 | 336 | 335 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 92 | 138..532 | 395 | 327 | 327 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 104 | 158..467 | 310 | 256 | 256 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 106 | 158..445 | 288 | 241 | 241 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79108 |
| 113 | 167..167 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 123 | 184..450 | 267 | 222 | 222 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 124 | 186..533 | 348 | 292 | 289 | 3 | 3 | 1 | 0 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 130 | 200..527 | 328 | 273 | 273 | 0 | 0 | 0 | 0 | 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 133 | 205..269 | 65 | 50 | 48 | 2 | 0 | 0 | 2 | 78897, 78971, 79037, 79045 |
| 156 | 274..481 | 208 | 170 | 169 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105 |
| 157 | 274..515 | 242 | 196 | 196 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 190 | 350..530 | 181 | 146 | 146 | 0 | 0 | 0 | 0 | 79116, 79134, 79135, 79136, 79139 |
| 214 | 427..538 | 112 | 90 | 90 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 9180; unmatched reference entries: 962; unmatched candidate entries: 1628
- identity switches: 831; fragmentation (coverage interruptions): 678; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 32 -> 41 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 42 -> 32 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 38 -> 42 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 38 -> 42 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 42 -> 32 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 32 -> 41 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 32 -> 50 at (2090.5, 3032.5), 4 frames after previous cover
- f96: ref 78896: 41 -> 53 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 79037: 42 -> 32 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 38 -> 42 at (2107, 3033), 1 frames after previous cover
- f97: ref 78971: 50 -> 32 at (2072, 3034.5), 1 frames after previous cover
- f97: ref 79045: 32 -> 50 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 49 -> 38 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 32 -> 50 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 50 -> 32 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 49 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 42 -> 38 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 32 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 38 -> 42 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 42 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 42 -> 62 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 49 -> 61 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 49 -> 63 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 42 -> 62 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 62 -> 32 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 49 -> 63 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 63 -> 61 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 32 -> 69 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79103: 63 -> 70 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 63 -> 67 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 49 -> 63 at (2131, 3027), 3 frames after previous cover
- f108: ref 79110: 49 -> 68 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79097: 38 -> 42 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 61 -> 38 at (2077.5, 3029.5), 3 frames after previous cover
- f110: ref 79097: 42 -> 38 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 38 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 61 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 67 -> 70 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 63 -> 67 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 68 -> 63 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 38 -> 61 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 70 -> 67 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 67 -> 63 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 61 -> 70 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 63 -> 68 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 70 -> 63 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 42 -> 69 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79045: 69 -> 50 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 38 -> 62 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 70 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 67 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 63 -> 67 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 68 -> 70 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 62 -> 69 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 69 -> 61 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 32 -> 69 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 50 -> 32 at (1956.5, 3034.5), 2 frames after previous cover
- f118: ref 79037: 69 -> 32 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 61 -> 62 at (2010.5, 3030), 2 frames after previous cover
- ... 771 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 981 | 22 | 0 (981) |
| 78896 | 350 (76..429) | 314 | 21 | 106 (104), 63 (77), 53 (71), 69 (34), 38 (14), 41 (8), 32 (6) |
| 78969 | 352 (80..434) | 318 | 22 | 61 (78), 106 (75), 41 (52), 62 (45), 53 (34), 38 (23), 69 (6), 32 (4), 63 (1) |
| 78971 | 352 (84..439) | 308 | 27 | 41 (93), 62 (48), 50 (39), 38 (36), 42 (33), 106 (31), 53 (8), 61 (6), 32 (5), 133 (5), 69 (4) |
| 79045 | 355 (84..443) | 309 | 32 | 38 (138), 41 (50), 50 (49), 32 (26), 53 (11), 133 (9), 69 (8), 42 (6), 61 (4), 62 (4), 63 (2), 106 (2) |
| 79037 | 355 (86..445) | 303 | 34 | 62 (62), 41 (50), 106 (50), 133 (36), 53 (26), 32 (21), 38 (14), 104 (12), 42 (11), 50 (9), 69 (7), 63 (2), +2 more |
| 78897 | 345 (89..450) | 305 | 31 | 42 (77), 41 (41), 123 (37), 38 (34), 53 (28), 62 (27), 69 (16), 50 (16), 104 (10), 106 (6), 79 (4), 133 (4), +2 more |
| 78899 | 365 (91..455) | 318 | 30 | 53 (107), 61 (63), 104 (39), 42 (29), 38 (26), 62 (13), 50 (12), 41 (9), 79 (6), 32 (6), 106 (4), 49 (1), +3 more |
| 79097 | 366 (94..461) | 332 | 24 | 104 (160), 42 (49), 61 (46), 38 (16), 62 (16), 79 (13), 53 (11), 123 (8), 83 (7), 49 (3), 106 (3) |
| 79098 | 360 (97..467) | 332 | 21 | 123 (97), 104 (63), 41 (50), 53 (44), 61 (17), 62 (16), 156 (11), 38 (9), 79 (9), 83 (8), 32 (5), 49 (3) |
| 79102 | 371 (98..477) | 333 | 26 | 156 (87), 83 (71), 123 (68), 62 (53), 32 (21), 79 (8), 104 (5), 61 (4), 38 (4), 49 (3), 53 (3), 70 (2), +3 more |
| 79103 | 380 (99..481) | 328 | 31 | 83 (113), 156 (67), 123 (35), 42 (22), 63 (21), 62 (20), 32 (19), 67 (15), 38 (10), 70 (3), 130 (3) |
| 79105 | 379 (101..484) | 343 | 30 | 67 (125), 83 (55), 32 (39), 156 (27), 63 (22), 41 (20), 42 (15), 38 (14), 62 (11), 84 (9), 70 (2), 68 (2), +2 more |
| 79108 | 385 (104..492) | 353 | 26 | 84 (105), 67 (66), 42 (55), 130 (32), 68 (29), 83 (21), 32 (21), 63 (11), 62 (5), 41 (3), 49 (2), 106 (2), +1 more |
| 79110 | 388 (106..497) | 354 | 24 | 32 (105), 67 (72), 84 (48), 130 (39), 42 (34), 68 (31), 83 (10), 63 (7), 70 (5), 91 (2), 49 (1) |
| 79111 | 386 (109..500) | 340 | 34 | 68 (136), 83 (48), 67 (38), 32 (38), 91 (24), 84 (15), 157 (14), 63 (13), 130 (8), 49 (2), 77 (2), 70 (1), +1 more |
| 79115 | 421 (111..531) | 361 | 40 | 91 (164), 68 (51), 63 (30), 157 (27), 130 (25), 84 (19), 67 (18), 32 (12), 77 (8), 49 (3), 70 (3), 83 (1) |
| 79116 | 411 (114..530) | 380 | 26 | 124 (87), 68 (78), 190 (59), 63 (41), 91 (31), 77 (26), 130 (18), 67 (16), 84 (10), 70 (5), 49 (4), 157 (3), +2 more |
| 79122 | 404 (118..532) | 371 | 28 | 92 (116), 91 (52), 84 (42), 63 (42), 68 (40), 130 (31), 157 (16), 32 (15), 77 (14), 49 (3) |
| 79132 | 391 (120..515) | 351 | 30 | 157 (87), 91 (66), 130 (50), 92 (38), 77 (35), 63 (29), 84 (23), 68 (13), 70 (4), 49 (3), 85 (2), 124 (1) |
| 79128 | 402 (124..527) | 372 | 20 | 130 (108), 157 (81), 84 (51), 77 (39), 91 (35), 124 (16), 49 (12), 92 (10), 32 (8), 85 (6), 70 (6) |
| 79134 | 407 (127..533) | 376 | 25 | 124 (117), 190 (49), 92 (45), 77 (41), 32 (39), 70 (37), 84 (22), 49 (12), 85 (6), 157 (5), 91 (3) |
| 79135 | 409 (129..542) | 366 | 26 | 124 (106), 49 (77), 77 (69), 214 (39), 85 (34), 92 (33), 84 (6), 190 (2) |
| 79139 | 406 (132..537) | 379 | 21 | 92 (134), 49 (117), 77 (103), 214 (13), 70 (10), 124 (1), 190 (1) |
| 79136 | 393 (136..538) | 353 | 27 | 49 (171), 190 (62), 77 (57), 214 (55), 92 (8) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 78 | 122..151 | 30 | 0 | 30 |
| 113 | 167..196 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/357/1007; tracks with internal gaps: 31; total internal gaps: 334; longest internal gap: 9; tracks ending in coasting: 33 (trailing rows total 1146)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 981 | 26 | 22 | 3 | 0 | 78911 |
| 32 | 78..524 | 447 | 447 | 393 | 54 | 16 | 4 | 27 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134 |
| 38 | 84..472 | 389 | 389 | 338 | 51 | 18 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 41 | 87..513 | 427 | 427 | 376 | 51 | 17 | 7 | 21 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79105, 79108 |
| 42 | 87..468 | 382 | 382 | 332 | 50 | 15 | 6 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 49 | 93..661 | 569 | 569 | 418 | 151 | 19 | 3 | 119 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 94..268 | 175 | 175 | 125 | 50 | 4 | 1 | 46 | 78897, 78899, 78971, 79037, 79045 |
| 53 | 96..484 | 389 | 389 | 343 | 46 | 11 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..362 | 260 | 260 | 222 | 38 | 7 | 2 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 62 | 103..463 | 361 | 361 | 320 | 41 | 11 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 63 | 103..458 | 356 | 356 | 299 | 57 | 15 | 9 | 29 | 78896, 78969, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 67 | 108..524 | 417 | 417 | 352 | 65 | 10 | 9 | 38 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 68 | 108..529 | 422 | 422 | 381 | 41 | 7 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 69 | 108..276 | 169 | 169 | 76 | 93 | 0 | 0 | 93 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 70 | 108..219 | 112 | 112 | 78 | 34 | 2 | 1 | 32 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79139 |
| 77 | 117..565 | 449 | 449 | 394 | 55 | 15 | 8 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 78 | 122..151 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 79 | 122..195 | 74 | 74 | 40 | 34 | 1 | 1 | 33 | 78897, 78899, 79097, 79098, 79102 |
| 83 | 126..506 | 381 | 381 | 335 | 46 | 15 | 4 | 25 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 84 | 126..520 | 395 | 395 | 350 | 45 | 10 | 3 | 31 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 85 | 126..204 | 79 | 79 | 48 | 31 | 1 | 1 | 30 | 79128, 79132, 79134, 79135 |
| 91 | 136..560 | 425 | 425 | 378 | 47 | 14 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 92 | 138..561 | 424 | 424 | 385 | 39 | 10 | 1 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 104 | 158..496 | 339 | 339 | 289 | 50 | 12 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 106 | 158..474 | 317 | 317 | 277 | 40 | 9 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79108 |
| 113 | 167..196 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 123 | 184..479 | 296 | 296 | 249 | 47 | 17 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 124 | 186..562 | 377 | 377 | 328 | 49 | 11 | 7 | 29 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 130 | 200..556 | 357 | 357 | 314 | 43 | 13 | 2 | 29 | 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 133 | 205..298 | 94 | 94 | 54 | 40 | 3 | 1 | 37 | 78897, 78971, 79037, 79045 |
| 156 | 274..510 | 237 | 237 | 192 | 45 | 9 | 3 | 32 | 79098, 79102, 79103, 79105 |
| 157 | 274..544 | 271 | 271 | 233 | 38 | 7 | 2 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 190 | 350..559 | 210 | 210 | 173 | 37 | 8 | 1 | 29 | 79116, 79134, 79135, 79136, 79139 |
| 214 | 427..567 | 141 | 141 | 107 | 34 | 5 | 1 | 29 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 9180; unmatched reference entries: 962; unmatched candidate entries: 1628
- identity switches: 831; fragmentation (coverage interruptions): 678; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 32 -> 41 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 42 -> 32 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 38 -> 42 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 38 -> 42 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 42 -> 32 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 32 -> 41 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 32 -> 50 at (2090.5, 3032.5), 4 frames after previous cover
- f96: ref 78896: 41 -> 53 at (2034.5, 3034), 4 frames after previous cover
- f96: ref 79037: 42 -> 32 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 38 -> 42 at (2107, 3033), 1 frames after previous cover
- f97: ref 78971: 50 -> 32 at (2072, 3034.5), 1 frames after previous cover
- f97: ref 79045: 32 -> 50 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 49 -> 38 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 32 -> 50 at (2066, 3034), 1 frames after previous cover
- f98: ref 79045: 50 -> 32 at (2075.5, 3033), 1 frames after previous cover
- f99: ref 78899: 49 -> 38 at (2109.5, 3030), 6 frames after previous cover
- f100: ref 78897: 42 -> 38 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79037: 32 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f101: ref 78897: 38 -> 42 at (2083, 3033.5), 1 frames after previous cover
- f103: ref 78899: 38 -> 42 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 42 -> 62 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 49 -> 61 at (2113.5, 3027), 3 frames after previous cover
- f103: ref 79102: 49 -> 63 at (2124.5, 3027.5), 1 frames after previous cover
- f104: ref 78897: 42 -> 62 at (2064, 3032), 2 frames after previous cover
- f104: ref 79037: 62 -> 32 at (2051, 3034), 1 frames after previous cover
- f105: ref 79105: 49 -> 63 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 79102: 63 -> 61 at (2101.5, 3029.5), 4 frames after previous cover
- f108: ref 79045: 32 -> 69 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79103: 63 -> 70 at (2104.5, 3023), 4 frames after previous cover
- f108: ref 79105: 63 -> 67 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 49 -> 63 at (2131, 3027), 3 frames after previous cover
- f108: ref 79110: 49 -> 68 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79097: 38 -> 42 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 61 -> 38 at (2077.5, 3029.5), 3 frames after previous cover
- f110: ref 79097: 42 -> 38 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 38 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 61 -> 38 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79105: 67 -> 70 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 63 -> 67 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 68 -> 63 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 38 -> 61 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 70 -> 67 at (2082, 3024), 2 frames after previous cover
- f112: ref 79108: 67 -> 63 at (2109, 3027), 1 frames after previous cover
- f113: ref 79102: 61 -> 70 at (2067, 3028.5), 2 frames after previous cover
- f113: ref 79110: 63 -> 68 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79105: 70 -> 63 at (2079, 3025), 2 frames after previous cover
- f115: ref 78899: 42 -> 69 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79045: 69 -> 50 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79098: 38 -> 62 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 70 -> 38 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 67 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 63 -> 67 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 68 -> 70 at (2105.5, 3026.5), 1 frames after previous cover
- f116: ref 78897: 62 -> 69 at (1990.5, 3033.5), 2 frames after previous cover
- f117: ref 78899: 69 -> 61 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 32 -> 69 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 50 -> 32 at (1956.5, 3034.5), 2 frames after previous cover
- f118: ref 79037: 69 -> 32 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 61 -> 62 at (2010.5, 3030), 2 frames after previous cover
- ... 771 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 981 | 22 | 0 (981) |
| 78896 | 350 (76..429) | 314 | 21 | 106 (104), 63 (77), 53 (71), 69 (34), 38 (14), 41 (8), 32 (6) |
| 78969 | 352 (80..434) | 318 | 22 | 61 (78), 106 (75), 41 (52), 62 (45), 53 (34), 38 (23), 69 (6), 32 (4), 63 (1) |
| 78971 | 352 (84..439) | 308 | 27 | 41 (93), 62 (48), 50 (39), 38 (36), 42 (33), 106 (31), 53 (8), 61 (6), 32 (5), 133 (5), 69 (4) |
| 79045 | 355 (84..443) | 309 | 32 | 38 (138), 41 (50), 50 (49), 32 (26), 53 (11), 133 (9), 69 (8), 42 (6), 61 (4), 62 (4), 63 (2), 106 (2) |
| 79037 | 355 (86..445) | 303 | 34 | 62 (62), 41 (50), 106 (50), 133 (36), 53 (26), 32 (21), 38 (14), 104 (12), 42 (11), 50 (9), 69 (7), 63 (2), +2 more |
| 78897 | 345 (89..450) | 305 | 31 | 42 (77), 41 (41), 123 (37), 38 (34), 53 (28), 62 (27), 69 (16), 50 (16), 104 (10), 106 (6), 79 (4), 133 (4), +2 more |
| 78899 | 365 (91..455) | 318 | 30 | 53 (107), 61 (63), 104 (39), 42 (29), 38 (26), 62 (13), 50 (12), 41 (9), 79 (6), 32 (6), 106 (4), 49 (1), +3 more |
| 79097 | 366 (94..461) | 332 | 24 | 104 (160), 42 (49), 61 (46), 38 (16), 62 (16), 79 (13), 53 (11), 123 (8), 83 (7), 49 (3), 106 (3) |
| 79098 | 360 (97..467) | 332 | 21 | 123 (97), 104 (63), 41 (50), 53 (44), 61 (17), 62 (16), 156 (11), 38 (9), 79 (9), 83 (8), 32 (5), 49 (3) |
| 79102 | 371 (98..477) | 333 | 26 | 156 (87), 83 (71), 123 (68), 62 (53), 32 (21), 79 (8), 104 (5), 61 (4), 38 (4), 49 (3), 53 (3), 70 (2), +3 more |
| 79103 | 380 (99..481) | 328 | 31 | 83 (113), 156 (67), 123 (35), 42 (22), 63 (21), 62 (20), 32 (19), 67 (15), 38 (10), 70 (3), 130 (3) |
| 79105 | 379 (101..484) | 343 | 30 | 67 (125), 83 (55), 32 (39), 156 (27), 63 (22), 41 (20), 42 (15), 38 (14), 62 (11), 84 (9), 70 (2), 68 (2), +2 more |
| 79108 | 385 (104..492) | 353 | 26 | 84 (105), 67 (66), 42 (55), 130 (32), 68 (29), 83 (21), 32 (21), 63 (11), 62 (5), 41 (3), 49 (2), 106 (2), +1 more |
| 79110 | 388 (106..497) | 354 | 24 | 32 (105), 67 (72), 84 (48), 130 (39), 42 (34), 68 (31), 83 (10), 63 (7), 70 (5), 91 (2), 49 (1) |
| 79111 | 386 (109..500) | 340 | 34 | 68 (136), 83 (48), 67 (38), 32 (38), 91 (24), 84 (15), 157 (14), 63 (13), 130 (8), 49 (2), 77 (2), 70 (1), +1 more |
| 79115 | 421 (111..531) | 361 | 40 | 91 (164), 68 (51), 63 (30), 157 (27), 130 (25), 84 (19), 67 (18), 32 (12), 77 (8), 49 (3), 70 (3), 83 (1) |
| 79116 | 411 (114..530) | 380 | 26 | 124 (87), 68 (78), 190 (59), 63 (41), 91 (31), 77 (26), 130 (18), 67 (16), 84 (10), 70 (5), 49 (4), 157 (3), +2 more |
| 79122 | 404 (118..532) | 371 | 28 | 92 (116), 91 (52), 84 (42), 63 (42), 68 (40), 130 (31), 157 (16), 32 (15), 77 (14), 49 (3) |
| 79132 | 391 (120..515) | 351 | 30 | 157 (87), 91 (66), 130 (50), 92 (38), 77 (35), 63 (29), 84 (23), 68 (13), 70 (4), 49 (3), 85 (2), 124 (1) |
| 79128 | 402 (124..527) | 372 | 20 | 130 (108), 157 (81), 84 (51), 77 (39), 91 (35), 124 (16), 49 (12), 92 (10), 32 (8), 85 (6), 70 (6) |
| 79134 | 407 (127..533) | 376 | 25 | 124 (117), 190 (49), 92 (45), 77 (41), 32 (39), 70 (37), 84 (22), 49 (12), 85 (6), 157 (5), 91 (3) |
| 79135 | 409 (129..542) | 366 | 26 | 124 (106), 49 (77), 77 (69), 214 (39), 85 (34), 92 (33), 84 (6), 190 (2) |
| 79139 | 406 (132..537) | 379 | 21 | 92 (134), 49 (117), 77 (103), 214 (13), 70 (10), 124 (1), 190 (1) |
| 79136 | 393 (136..538) | 353 | 27 | 49 (171), 190 (62), 77 (57), 214 (55), 92 (8) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 78 | 122..151 | 30 | 0 | 30 |
| 113 | 167..196 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/357/1007; tracks with internal gaps: 31; total internal gaps: 334; longest internal gap: 9; tracks ending in coasting: 33 (trailing rows total 1146)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 981 | 26 | 22 | 3 | 0 | 78911 |
| 32 | 78..524 | 447 | 447 | 393 | 54 | 16 | 4 | 27 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134 |
| 38 | 84..472 | 389 | 389 | 338 | 51 | 18 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 41 | 87..513 | 427 | 427 | 376 | 51 | 17 | 7 | 21 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79105, 79108 |
| 42 | 87..468 | 382 | 382 | 332 | 50 | 15 | 6 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 49 | 93..661 | 569 | 569 | 418 | 151 | 19 | 3 | 119 | 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 94..268 | 175 | 175 | 125 | 50 | 4 | 1 | 46 | 78897, 78899, 78971, 79037, 79045 |
| 53 | 96..484 | 389 | 389 | 343 | 46 | 11 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..362 | 260 | 260 | 222 | 38 | 7 | 2 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 62 | 103..463 | 361 | 361 | 320 | 41 | 11 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 63 | 103..458 | 356 | 356 | 299 | 57 | 15 | 9 | 29 | 78896, 78969, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 67 | 108..524 | 417 | 417 | 352 | 65 | 10 | 9 | 38 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 68 | 108..529 | 422 | 422 | 381 | 41 | 7 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 69 | 108..276 | 169 | 169 | 76 | 93 | 0 | 0 | 93 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 70 | 108..219 | 112 | 112 | 78 | 34 | 2 | 1 | 32 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79139 |
| 77 | 117..565 | 449 | 449 | 394 | 55 | 15 | 8 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 78 | 122..151 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 79 | 122..195 | 74 | 74 | 40 | 34 | 1 | 1 | 33 | 78897, 78899, 79097, 79098, 79102 |
| 83 | 126..506 | 381 | 381 | 335 | 46 | 15 | 4 | 25 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 84 | 126..520 | 395 | 395 | 350 | 45 | 10 | 3 | 31 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 85 | 126..204 | 79 | 79 | 48 | 31 | 1 | 1 | 30 | 79128, 79132, 79134, 79135 |
| 91 | 136..560 | 425 | 425 | 378 | 47 | 14 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 92 | 138..561 | 424 | 424 | 385 | 39 | 10 | 1 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 104 | 158..496 | 339 | 339 | 289 | 50 | 12 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102 |
| 106 | 158..474 | 317 | 317 | 277 | 40 | 9 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79108 |
| 113 | 167..196 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 123 | 184..479 | 296 | 296 | 249 | 47 | 17 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 124 | 186..562 | 377 | 377 | 328 | 49 | 11 | 7 | 29 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 130 | 200..556 | 357 | 357 | 314 | 43 | 13 | 2 | 29 | 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 133 | 205..298 | 94 | 94 | 54 | 40 | 3 | 1 | 37 | 78897, 78971, 79037, 79045 |
| 156 | 274..510 | 237 | 237 | 192 | 45 | 9 | 3 | 32 | 79098, 79102, 79103, 79105 |
| 157 | 274..544 | 271 | 271 | 233 | 38 | 7 | 2 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 190 | 350..559 | 210 | 210 | 173 | 37 | 8 | 1 | 29 | 79116, 79134, 79135, 79136, 79139 |
| 214 | 427..567 | 141 | 141 | 107 | 34 | 5 | 1 | 29 | 79135, 79136, 79139 |
