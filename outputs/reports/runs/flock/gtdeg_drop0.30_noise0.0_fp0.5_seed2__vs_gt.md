# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=c241d5b334d6
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise0.0_fp0.5_seed2/tracks.csv sha256=aa7a5e469295d592
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise0.0_fp0.5_seed2.csv sha256=c241d5b334d66e87
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise0.0_fp0.5_seed2
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
| observations | none | 4 | 0.299 | 0.131 | 0.557 | 0.01 | 0.259 | 1251 | 2023.0 |
| observations | none | 6 | 0.299 | 0.132 | 0.557 | 0.01 | 0.260 | 1252 | 2020.0 |
| observations | none | 8 | 0.299 | 0.133 | 0.558 | 0.05 | 0.263 | 1247 | 2018.0 |
| observations | none | 12 | 0.300 | 0.137 | 0.565 | 0.36 | 0.284 | 1163 | 1972.0 |
| observations | ignore | 4 | 0.299 | 0.131 | 0.557 | 0.01 | 0.259 | 1251 | 2023.0 |
| observations | ignore | 6 | 0.299 | 0.132 | 0.557 | 0.01 | 0.260 | 1252 | 2020.0 |
| observations | ignore | 8 | 0.299 | 0.133 | 0.558 | 0.05 | 0.263 | 1247 | 2018.0 |
| observations | ignore | 12 | 0.300 | 0.137 | 0.565 | 0.36 | 0.284 | 1163 | 1972.0 |
| updates | none | 4 | 0.281 | 0.135 | 0.318 | 0.12 | 0.240 | 1285 | 1929.0 |
| updates | none | 6 | 0.305 | 0.148 | 0.430 | 0.51 | 0.263 | 1311 | 1527.0 |
| updates | none | 8 | 0.320 | 0.157 | 0.540 | 0.97 | 0.283 | 1270 | 1167.0 |
| updates | none | 12 | 0.339 | 0.170 | 0.587 | 1.50 | 0.312 | 1161 | 996.0 |
| updates | ignore | 4 | 0.281 | 0.135 | 0.318 | 0.12 | 0.240 | 1285 | 1929.0 |
| updates | ignore | 6 | 0.305 | 0.148 | 0.430 | 0.51 | 0.263 | 1311 | 1527.0 |
| updates | ignore | 8 | 0.320 | 0.157 | 0.540 | 0.97 | 0.283 | 1270 | 1167.0 |
| updates | ignore | 12 | 0.339 | 0.170 | 0.587 | 1.50 | 0.312 | 1161 | 996.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 6965; unmatched reference entries: 3177; unmatched candidate entries: 60
- identity switches: 1247; fragmentation (coverage interruptions): 2056; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 42 -> 49 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 79045: 49 -> 51 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78897: 42 -> 49 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 42 -> 48 at (2095, 3033.5), 6 frames after previous cover
- f95: ref 78897: 49 -> 42 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 49 -> 51 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 42 -> 48 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 48 -> 45 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 45 -> 48 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 51 -> 48 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 49 -> 51 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 48 -> 62 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 48 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 49 -> 51 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 42 -> 48 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 49 -> 51 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 78899: 51 -> 42 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 48 -> 62 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 51 -> 66 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 51 -> 66 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 62 -> 70 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 49 -> 51 at (2116.5, 3023), 5 frames after previous cover
- f106: ref 79105: 49 -> 69 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 48 -> 74 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 66 -> 75 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 51 -> 72 at (2096.5, 3027.5), 4 frames after previous cover
- f108: ref 79110: 49 -> 73 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 66 -> 75 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79103: 51 -> 66 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79108: 49 -> 69 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 42 -> 66 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 66 -> 72 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 69 -> 51 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 73 -> 69 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 73 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 75 -> 72 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 72 -> 51 at (2082, 3024), 2 frames after previous cover
- f112: ref 79105: 51 -> 69 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 69 -> 73 at (2109, 3027), 3 frames after previous cover
- f113: ref 79108: 73 -> 69 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 69 -> 73 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 72 -> 66 at (2034.5, 3030), 2 frames after previous cover
- f114: ref 79098: 75 -> 72 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 72 -> 75 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 66 -> 74 at (2012.5, 3030), 3 frames after previous cover
- f115: ref 79045: 74 -> 70 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 51 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 69 -> 75 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 73 -> 69 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 49 -> 51 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78897: 42 -> 74 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 75 -> 66 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 75 -> 42 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 69 -> 75 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 74 -> 72 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 48 -> 74 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 70 -> 48 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 72 -> 66 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 74 -> 48 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 66 -> 72 at (2010.5, 3030), 3 frames after previous cover
- ... 1187 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 701 | 208 | 8 (701) |
| 78896 | 350 (76..429) | 242 | 63 | 95 (68), 150 (56), 45 (37), 82 (37), 62 (18), 70 (10), 127 (9), 75 (4), 48 (3) |
| 78969 | 352 (80..434) | 237 | 74 | 150 (67), 95 (65), 62 (37), 70 (25), 45 (18), 82 (13), 75 (11), 48 (1) |
| 78971 | 352 (84..439) | 232 | 68 | 70 (94), 149 (39), 82 (35), 62 (20), 74 (13), 75 (10), 95 (6), 150 (5), 48 (3), 127 (3), 42 (2), 87 (1), +1 more |
| 79045 | 355 (84..443) | 251 | 63 | 75 (65), 70 (57), 127 (37), 62 (18), 74 (15), 45 (13), 95 (8), 149 (8), 51 (7), 82 (7), 150 (6), 48 (4), +3 more |
| 79037 | 355 (86..445) | 239 | 69 | 149 (63), 75 (40), 51 (32), 62 (29), 48 (22), 70 (18), 45 (13), 127 (9), 42 (7), 74 (3), 95 (2), 87 (1) |
| 78897 | 345 (89..450) | 241 | 73 | 127 (48), 75 (30), 149 (30), 62 (27), 70 (26), 95 (22), 42 (17), 74 (11), 51 (9), 87 (6), 45 (5), 133 (5), +2 more |
| 78899 | 365 (91..455) | 236 | 83 | 62 (76), 51 (40), 127 (37), 45 (21), 95 (16), 72 (12), 75 (7), 74 (5), 87 (4), 70 (4), 149 (4), 94 (3), +4 more |
| 79097 | 366 (94..461) | 253 | 75 | 51 (70), 127 (38), 95 (33), 62 (30), 75 (23), 72 (15), 133 (14), 74 (8), 66 (5), 48 (4), 49 (3), 70 (3), +4 more |
| 79098 | 360 (97..467) | 253 | 81 | 109 (67), 75 (46), 49 (22), 62 (22), 127 (20), 70 (14), 48 (12), 51 (10), 66 (10), 72 (9), 133 (8), 87 (5), +2 more |
| 79102 | 371 (98..477) | 246 | 82 | 133 (62), 49 (31), 109 (31), 51 (19), 75 (15), 66 (14), 48 (13), 62 (12), 127 (12), 70 (10), 72 (9), 91 (7), +3 more |
| 79103 | 380 (99..481) | 262 | 76 | 133 (61), 109 (60), 51 (22), 66 (22), 91 (17), 72 (16), 82 (12), 100 (12), 49 (10), 87 (9), 127 (9), 48 (7), +2 more |
| 79105 | 379 (101..484) | 252 | 80 | 109 (68), 133 (23), 51 (22), 66 (22), 49 (19), 100 (19), 72 (15), 207 (12), 73 (9), 42 (8), 87 (8), 91 (8), +5 more |
| 79108 | 385 (104..492) | 268 | 78 | 66 (88), 49 (37), 100 (23), 109 (21), 48 (15), 133 (13), 69 (12), 72 (10), 87 (10), 75 (9), 73 (6), 51 (6), +5 more |
| 79110 | 388 (106..497) | 259 | 79 | 100 (80), 66 (60), 48 (25), 69 (21), 49 (15), 87 (12), 73 (11), 51 (7), 91 (7), 133 (7), 42 (4), 82 (3), +4 more |
| 79111 | 386 (109..500) | 272 | 78 | 87 (44), 100 (43), 49 (39), 69 (32), 73 (28), 48 (26), 91 (14), 66 (12), 133 (8), 51 (7), 207 (5), 42 (4), +4 more |
| 79115 | 421 (111..531) | 284 | 89 | 69 (82), 73 (64), 48 (39), 45 (17), 42 (15), 66 (15), 87 (15), 91 (14), 49 (6), 51 (5), 75 (5), 100 (3), +2 more |
| 79116 | 411 (114..530) | 311 | 72 | 91 (65), 48 (38), 151 (35), 73 (33), 66 (33), 42 (30), 87 (24), 69 (23), 75 (7), 49 (6), 100 (5), 51 (4), +5 more |
| 79122 | 404 (118..532) | 281 | 73 | 69 (44), 42 (40), 87 (36), 91 (30), 48 (30), 151 (24), 73 (24), 94 (14), 49 (12), 66 (10), 51 (7), 75 (4), +3 more |
| 79132 | 391 (120..515) | 273 | 77 | 87 (89), 69 (58), 48 (39), 91 (20), 73 (17), 45 (17), 100 (7), 66 (7), 94 (6), 207 (5), 151 (3), 49 (2), +2 more |
| 79128 | 402 (124..527) | 276 | 82 | 151 (48), 91 (32), 87 (28), 49 (25), 73 (24), 75 (23), 69 (21), 45 (20), 100 (17), 42 (14), 207 (9), 94 (8), +3 more |
| 79134 | 407 (127..533) | 281 | 83 | 69 (56), 91 (48), 73 (39), 48 (31), 151 (27), 45 (22), 49 (19), 42 (16), 100 (14), 87 (6), 72 (2), 94 (1) |
| 79135 | 409 (129..542) | 275 | 86 | 198 (52), 151 (45), 73 (43), 48 (29), 45 (26), 49 (19), 207 (18), 91 (16), 87 (13), 100 (7), 133 (3), 94 (2), +1 more |
| 79139 | 406 (132..537) | 266 | 83 | 198 (65), 151 (45), 91 (37), 45 (33), 42 (26), 49 (19), 73 (18), 94 (12), 48 (9), 100 (2) |
| 79136 | 393 (136..538) | 274 | 81 | 42 (157), 49 (33), 73 (26), 100 (22), 91 (15), 48 (14), 198 (7) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 83 | 122..122 | 1 | 0 | 1 |
| 118 | 167..167 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 1/334/995; tracks with internal gaps: 12; total internal gaps: 34; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 23)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 14..1008 | 995 | 718 | 701 | 17 | 17 | 1 | 0 | 78911 |
| 42 | 84..532 | 449 | 352 | 351 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 45 | 87..419 | 333 | 254 | 251 | 3 | 1 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 48 | 89..533 | 445 | 376 | 375 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 89..500 | 412 | 322 | 322 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 91..467 | 377 | 273 | 269 | 4 | 2 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 62 | 100..455 | 356 | 289 | 289 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 66 | 103..495 | 393 | 302 | 302 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 106..531 | 426 | 354 | 354 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 70 | 106..443 | 338 | 261 | 261 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 72 | 108..225 | 118 | 101 | 100 | 1 | 0 | 0 | 1 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134 |
| 73 | 108..536 | 429 | 344 | 342 | 2 | 2 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 108..247 | 140 | 64 | 58 | 6 | 0 | 0 | 6 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 75 | 108..527 | 420 | 314 | 313 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 121..269 | 149 | 118 | 116 | 2 | 0 | 0 | 2 | 78896, 78969, 78971, 79045, 79102, 79103, 79105, 79108, 79110, 79116 |
| 83 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 87 | 126..515 | 390 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 91 | 126..538 | 413 | 334 | 333 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 94 | 134..217 | 84 | 64 | 61 | 3 | 0 | 0 | 3 | 78899, 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 95 | 134..429 | 296 | 225 | 225 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 100 | 142..477 | 336 | 263 | 261 | 2 | 2 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 109 | 158..491 | 334 | 251 | 249 | 2 | 2 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 118 | 167..167 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 127 | 182..481 | 300 | 223 | 222 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 133 | 199..444 | 246 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79132, 79135 |
| 149 | 248..439 | 192 | 144 | 144 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 150 | 248..434 | 187 | 138 | 134 | 4 | 3 | 2 | 0 | 78896, 78969, 78971, 79045 |
| 151 | 248..530 | 283 | 227 | 227 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 198 | 372..632 | 261 | 131 | 124 | 7 | 0 | 0 | 7 | 79135, 79136, 79139 |
| 207 | 397..484 | 88 | 56 | 56 | 0 | 0 | 0 | 0 | 79105, 79108, 79111, 79116, 79128, 79132, 79135 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 6965; unmatched reference entries: 3177; unmatched candidate entries: 60
- identity switches: 1247; fragmentation (coverage interruptions): 2056; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 42 -> 49 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 79045: 49 -> 51 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78897: 42 -> 49 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 42 -> 48 at (2095, 3033.5), 6 frames after previous cover
- f95: ref 78897: 49 -> 42 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 49 -> 51 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 42 -> 48 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 48 -> 45 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 45 -> 48 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 51 -> 48 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 49 -> 51 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 48 -> 62 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 48 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 49 -> 51 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 42 -> 48 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 49 -> 51 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 78899: 51 -> 42 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 48 -> 62 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 51 -> 66 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 51 -> 66 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 62 -> 70 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 49 -> 51 at (2116.5, 3023), 5 frames after previous cover
- f106: ref 79105: 49 -> 69 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 48 -> 74 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 66 -> 75 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 51 -> 72 at (2096.5, 3027.5), 4 frames after previous cover
- f108: ref 79110: 49 -> 73 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 66 -> 75 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79103: 51 -> 66 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79108: 49 -> 69 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 42 -> 66 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 66 -> 72 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 69 -> 51 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 73 -> 69 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 73 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 75 -> 72 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 72 -> 51 at (2082, 3024), 2 frames after previous cover
- f112: ref 79105: 51 -> 69 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 69 -> 73 at (2109, 3027), 3 frames after previous cover
- f113: ref 79108: 73 -> 69 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 69 -> 73 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 72 -> 66 at (2034.5, 3030), 2 frames after previous cover
- f114: ref 79098: 75 -> 72 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 72 -> 75 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 66 -> 74 at (2012.5, 3030), 3 frames after previous cover
- f115: ref 79045: 74 -> 70 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 51 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 69 -> 75 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 73 -> 69 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 49 -> 51 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78897: 42 -> 74 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 75 -> 66 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 75 -> 42 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 69 -> 75 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 74 -> 72 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 48 -> 74 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 70 -> 48 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 72 -> 66 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 74 -> 48 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 66 -> 72 at (2010.5, 3030), 3 frames after previous cover
- ... 1187 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 701 | 208 | 8 (701) |
| 78896 | 350 (76..429) | 242 | 63 | 95 (68), 150 (56), 45 (37), 82 (37), 62 (18), 70 (10), 127 (9), 75 (4), 48 (3) |
| 78969 | 352 (80..434) | 237 | 74 | 150 (67), 95 (65), 62 (37), 70 (25), 45 (18), 82 (13), 75 (11), 48 (1) |
| 78971 | 352 (84..439) | 232 | 68 | 70 (94), 149 (39), 82 (35), 62 (20), 74 (13), 75 (10), 95 (6), 150 (5), 48 (3), 127 (3), 42 (2), 87 (1), +1 more |
| 79045 | 355 (84..443) | 251 | 63 | 75 (65), 70 (57), 127 (37), 62 (18), 74 (15), 45 (13), 95 (8), 149 (8), 51 (7), 82 (7), 150 (6), 48 (4), +3 more |
| 79037 | 355 (86..445) | 239 | 69 | 149 (63), 75 (40), 51 (32), 62 (29), 48 (22), 70 (18), 45 (13), 127 (9), 42 (7), 74 (3), 95 (2), 87 (1) |
| 78897 | 345 (89..450) | 241 | 73 | 127 (48), 75 (30), 149 (30), 62 (27), 70 (26), 95 (22), 42 (17), 74 (11), 51 (9), 87 (6), 45 (5), 133 (5), +2 more |
| 78899 | 365 (91..455) | 236 | 83 | 62 (76), 51 (40), 127 (37), 45 (21), 95 (16), 72 (12), 75 (7), 74 (5), 87 (4), 70 (4), 149 (4), 94 (3), +4 more |
| 79097 | 366 (94..461) | 253 | 75 | 51 (70), 127 (38), 95 (33), 62 (30), 75 (23), 72 (15), 133 (14), 74 (8), 66 (5), 48 (4), 49 (3), 70 (3), +4 more |
| 79098 | 360 (97..467) | 253 | 81 | 109 (67), 75 (46), 49 (22), 62 (22), 127 (20), 70 (14), 48 (12), 51 (10), 66 (10), 72 (9), 133 (8), 87 (5), +2 more |
| 79102 | 371 (98..477) | 246 | 82 | 133 (62), 49 (31), 109 (31), 51 (19), 75 (15), 66 (14), 48 (13), 62 (12), 127 (12), 70 (10), 72 (9), 91 (7), +3 more |
| 79103 | 380 (99..481) | 262 | 76 | 133 (61), 109 (60), 51 (22), 66 (22), 91 (17), 72 (16), 82 (12), 100 (12), 49 (10), 87 (9), 127 (9), 48 (7), +2 more |
| 79105 | 379 (101..484) | 252 | 80 | 109 (68), 133 (23), 51 (22), 66 (22), 49 (19), 100 (19), 72 (15), 207 (12), 73 (9), 42 (8), 87 (8), 91 (8), +5 more |
| 79108 | 385 (104..492) | 268 | 78 | 66 (88), 49 (37), 100 (23), 109 (21), 48 (15), 133 (13), 69 (12), 72 (10), 87 (10), 75 (9), 73 (6), 51 (6), +5 more |
| 79110 | 388 (106..497) | 259 | 79 | 100 (80), 66 (60), 48 (25), 69 (21), 49 (15), 87 (12), 73 (11), 51 (7), 91 (7), 133 (7), 42 (4), 82 (3), +4 more |
| 79111 | 386 (109..500) | 272 | 78 | 87 (44), 100 (43), 49 (39), 69 (32), 73 (28), 48 (26), 91 (14), 66 (12), 133 (8), 51 (7), 207 (5), 42 (4), +4 more |
| 79115 | 421 (111..531) | 284 | 89 | 69 (82), 73 (64), 48 (39), 45 (17), 42 (15), 66 (15), 87 (15), 91 (14), 49 (6), 51 (5), 75 (5), 100 (3), +2 more |
| 79116 | 411 (114..530) | 311 | 72 | 91 (65), 48 (38), 151 (35), 73 (33), 66 (33), 42 (30), 87 (24), 69 (23), 75 (7), 49 (6), 100 (5), 51 (4), +5 more |
| 79122 | 404 (118..532) | 281 | 73 | 69 (44), 42 (40), 87 (36), 91 (30), 48 (30), 151 (24), 73 (24), 94 (14), 49 (12), 66 (10), 51 (7), 75 (4), +3 more |
| 79132 | 391 (120..515) | 273 | 77 | 87 (89), 69 (58), 48 (39), 91 (20), 73 (17), 45 (17), 100 (7), 66 (7), 94 (6), 207 (5), 151 (3), 49 (2), +2 more |
| 79128 | 402 (124..527) | 276 | 82 | 151 (48), 91 (32), 87 (28), 49 (25), 73 (24), 75 (23), 69 (21), 45 (20), 100 (17), 42 (14), 207 (9), 94 (8), +3 more |
| 79134 | 407 (127..533) | 281 | 83 | 69 (56), 91 (48), 73 (39), 48 (31), 151 (27), 45 (22), 49 (19), 42 (16), 100 (14), 87 (6), 72 (2), 94 (1) |
| 79135 | 409 (129..542) | 275 | 86 | 198 (52), 151 (45), 73 (43), 48 (29), 45 (26), 49 (19), 207 (18), 91 (16), 87 (13), 100 (7), 133 (3), 94 (2), +1 more |
| 79139 | 406 (132..537) | 266 | 83 | 198 (65), 151 (45), 91 (37), 45 (33), 42 (26), 49 (19), 73 (18), 94 (12), 48 (9), 100 (2) |
| 79136 | 393 (136..538) | 274 | 81 | 42 (157), 49 (33), 73 (26), 100 (22), 91 (15), 48 (14), 198 (7) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 83 | 122..122 | 1 | 0 | 1 |
| 118 | 167..167 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 1/334/995; tracks with internal gaps: 12; total internal gaps: 34; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 23)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 14..1008 | 995 | 718 | 701 | 17 | 17 | 1 | 0 | 78911 |
| 42 | 84..532 | 449 | 352 | 351 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 45 | 87..419 | 333 | 254 | 251 | 3 | 1 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 48 | 89..533 | 445 | 376 | 375 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 89..500 | 412 | 322 | 322 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 91..467 | 377 | 273 | 269 | 4 | 2 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 62 | 100..455 | 356 | 289 | 289 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 66 | 103..495 | 393 | 302 | 302 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 106..531 | 426 | 354 | 354 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 70 | 106..443 | 338 | 261 | 261 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 72 | 108..225 | 118 | 101 | 100 | 1 | 0 | 0 | 1 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134 |
| 73 | 108..536 | 429 | 344 | 342 | 2 | 2 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 108..247 | 140 | 64 | 58 | 6 | 0 | 0 | 6 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 75 | 108..527 | 420 | 314 | 313 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 121..269 | 149 | 118 | 116 | 2 | 0 | 0 | 2 | 78896, 78969, 78971, 79045, 79102, 79103, 79105, 79108, 79110, 79116 |
| 83 | 122..122 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 87 | 126..515 | 390 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 91 | 126..538 | 413 | 334 | 333 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 94 | 134..217 | 84 | 64 | 61 | 3 | 0 | 0 | 3 | 78899, 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 95 | 134..429 | 296 | 225 | 225 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 100 | 142..477 | 336 | 263 | 261 | 2 | 2 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 109 | 158..491 | 334 | 251 | 249 | 2 | 2 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 118 | 167..167 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 127 | 182..481 | 300 | 223 | 222 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 133 | 199..444 | 246 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79132, 79135 |
| 149 | 248..439 | 192 | 144 | 144 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 150 | 248..434 | 187 | 138 | 134 | 4 | 3 | 2 | 0 | 78896, 78969, 78971, 79045 |
| 151 | 248..530 | 283 | 227 | 227 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 198 | 372..632 | 261 | 131 | 124 | 7 | 0 | 0 | 7 | 79135, 79136, 79139 |
| 207 | 397..484 | 88 | 56 | 56 | 0 | 0 | 0 | 0 | 79105, 79108, 79111, 79116, 79128, 79132, 79135 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8388; unmatched reference entries: 1754; unmatched candidate entries: 1645
- identity switches: 1270; fragmentation (coverage interruptions): 1102; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 42 -> 49 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 78971: 42 -> 45 at (2108.5, 3033.5), 4 frames after previous cover
- f92: ref 79045: 49 -> 51 at (2110.5, 3033.5), 1 frames after previous cover
- f93: ref 78897: 42 -> 49 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 45 -> 48 at (2095, 3033.5), 2 frames after previous cover
- f95: ref 78897: 49 -> 42 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 49 -> 51 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 42 -> 48 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 48 -> 45 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 45 -> 48 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 51 -> 48 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 49 -> 51 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 48 -> 62 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 48 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 49 -> 51 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 42 -> 48 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 49 -> 51 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78899: 51 -> 42 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 48 -> 62 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 51 -> 66 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 51 -> 66 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 62 -> 70 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 49 -> 51 at (2116.5, 3023), 4 frames after previous cover
- f106: ref 79105: 49 -> 69 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 48 -> 74 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 66 -> 75 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 51 -> 72 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79110: 49 -> 73 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 66 -> 75 at (2077.5, 3029.5), 2 frames after previous cover
- f109: ref 79108: 49 -> 69 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 42 -> 66 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 51 -> 72 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 69 -> 51 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 79110: 73 -> 69 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 73 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 75 -> 72 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 72 -> 51 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 51 -> 69 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 69 -> 73 at (2109, 3027), 2 frames after previous cover
- f113: ref 79108: 73 -> 69 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 69 -> 73 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 72 -> 66 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 75 -> 72 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 72 -> 75 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 66 -> 74 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 74 -> 70 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 51 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 69 -> 75 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 73 -> 69 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 49 -> 51 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 78897: 42 -> 74 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 75 -> 66 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 75 -> 42 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 69 -> 75 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 74 -> 72 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 48 -> 74 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 70 -> 48 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 72 -> 66 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 74 -> 48 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 66 -> 72 at (2010.5, 3030), 3 frames after previous cover
- ... 1210 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 938 | 42 | 8 (938) |
| 78896 | 350 (76..429) | 289 | 34 | 95 (78), 150 (70), 82 (44), 45 (43), 62 (21), 127 (14), 70 (12), 48 (4), 75 (3) |
| 78969 | 352 (80..434) | 291 | 36 | 95 (83), 150 (83), 62 (44), 70 (30), 45 (21), 82 (17), 75 (12), 48 (1) |
| 78971 | 352 (84..439) | 278 | 41 | 70 (116), 149 (49), 82 (42), 62 (23), 74 (13), 75 (11), 95 (8), 150 (5), 48 (3), 127 (3), 42 (2), 45 (2), +1 more |
| 79045 | 355 (84..443) | 288 | 40 | 75 (71), 70 (68), 127 (43), 62 (21), 45 (16), 74 (15), 149 (10), 95 (9), 150 (9), 51 (8), 82 (7), 48 (4), +3 more |
| 79037 | 355 (86..445) | 278 | 47 | 149 (74), 75 (46), 51 (41), 62 (31), 48 (22), 70 (21), 45 (17), 127 (13), 42 (7), 74 (3), 95 (2), 87 (1) |
| 78897 | 345 (89..450) | 285 | 44 | 127 (59), 75 (38), 149 (33), 95 (31), 62 (30), 70 (29), 42 (18), 74 (12), 51 (11), 133 (7), 87 (6), 45 (5), +2 more |
| 78899 | 365 (91..455) | 285 | 50 | 62 (86), 51 (55), 127 (44), 45 (25), 95 (19), 72 (16), 75 (8), 74 (6), 66 (4), 87 (4), 70 (4), 149 (4), +5 more |
| 79097 | 366 (94..461) | 297 | 43 | 51 (83), 127 (44), 62 (39), 95 (38), 75 (27), 72 (17), 133 (16), 74 (8), 66 (5), 48 (5), 70 (4), 49 (3), +4 more |
| 79098 | 360 (97..467) | 301 | 46 | 109 (84), 75 (63), 62 (28), 49 (24), 127 (22), 70 (16), 48 (14), 66 (11), 51 (10), 72 (9), 133 (8), 95 (5), +2 more |
| 79102 | 371 (98..477) | 292 | 50 | 133 (70), 49 (36), 109 (36), 51 (23), 66 (19), 75 (17), 127 (16), 62 (15), 48 (14), 70 (14), 72 (10), 100 (10), +3 more |
| 79103 | 380 (99..481) | 306 | 46 | 133 (70), 109 (68), 66 (27), 51 (24), 72 (20), 91 (19), 100 (17), 49 (15), 82 (14), 87 (9), 127 (9), 48 (8), +2 more |
| 79105 | 379 (101..484) | 311 | 43 | 109 (86), 66 (31), 51 (27), 133 (27), 49 (26), 100 (24), 72 (16), 207 (15), 73 (10), 75 (9), 42 (9), 87 (9), +5 more |
| 79108 | 385 (104..492) | 313 | 47 | 66 (103), 49 (46), 109 (25), 100 (25), 69 (16), 48 (16), 133 (13), 72 (12), 87 (12), 207 (11), 75 (10), 51 (7), +5 more |
| 79110 | 388 (106..497) | 312 | 50 | 100 (95), 66 (76), 48 (29), 69 (24), 49 (20), 87 (15), 73 (12), 91 (10), 51 (9), 133 (7), 42 (4), 75 (3), +5 more |
| 79111 | 386 (109..500) | 324 | 43 | 87 (58), 100 (50), 49 (43), 69 (39), 73 (30), 48 (27), 66 (18), 91 (15), 51 (11), 133 (9), 207 (8), 42 (4), +4 more |
| 79115 | 421 (111..531) | 335 | 51 | 69 (95), 73 (81), 48 (47), 45 (20), 91 (17), 87 (17), 42 (15), 66 (14), 49 (8), 51 (6), 75 (6), 100 (4), +2 more |
| 79116 | 411 (114..530) | 353 | 39 | 91 (80), 151 (42), 48 (40), 73 (39), 66 (34), 42 (31), 87 (27), 69 (26), 51 (7), 75 (7), 49 (6), 100 (5), +5 more |
| 79122 | 404 (118..532) | 328 | 44 | 69 (51), 42 (49), 87 (42), 48 (36), 91 (33), 151 (33), 73 (25), 94 (16), 49 (13), 66 (11), 51 (8), 75 (5), +3 more |
| 79132 | 391 (120..515) | 322 | 44 | 87 (109), 69 (65), 48 (41), 45 (26), 91 (21), 73 (21), 66 (9), 100 (8), 94 (7), 207 (6), 133 (3), 151 (3), +2 more |
| 79128 | 402 (124..527) | 324 | 47 | 151 (58), 91 (37), 87 (31), 49 (30), 45 (29), 73 (26), 75 (26), 69 (24), 100 (21), 42 (15), 207 (10), 94 (9), +3 more |
| 79134 | 407 (127..533) | 333 | 50 | 69 (71), 91 (54), 73 (42), 48 (40), 151 (31), 49 (23), 45 (23), 42 (21), 100 (16), 87 (7), 72 (3), 94 (2) |
| 79135 | 409 (129..542) | 328 | 53 | 198 (65), 73 (55), 151 (49), 48 (37), 45 (29), 207 (24), 49 (21), 91 (16), 87 (15), 100 (7), 42 (4), 133 (4), +1 more |
| 79139 | 406 (132..537) | 343 | 39 | 198 (95), 91 (62), 151 (56), 45 (45), 42 (26), 49 (20), 73 (20), 94 (14), 48 (3), 100 (2) |
| 79136 | 393 (136..538) | 334 | 33 | 42 (206), 49 (40), 73 (38), 100 (26), 48 (23), 91 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 83 | 122..151 | 30 | 0 | 30 |
| 118 | 167..196 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 30/363/995; tracks with internal gaps: 28; total internal gaps: 398; longest internal gap: 21; tracks ending in coasting: 29 (trailing rows total 1018)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 14..1008 | 995 | 995 | 938 | 57 | 42 | 3 | 0 | 78911 |
| 42 | 84..561 | 478 | 478 | 421 | 57 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 45 | 87..448 | 362 | 362 | 309 | 53 | 12 | 5 | 35 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 48 | 89..562 | 474 | 474 | 428 | 46 | 12 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 89..529 | 441 | 441 | 382 | 59 | 17 | 6 | 29 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 91..496 | 406 | 406 | 332 | 74 | 21 | 9 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 62 | 100..484 | 385 | 385 | 338 | 47 | 12 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 66 | 103..524 | 422 | 422 | 364 | 58 | 17 | 4 | 27 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 106..560 | 455 | 455 | 416 | 39 | 10 | 1 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 70 | 106..472 | 367 | 367 | 314 | 53 | 21 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 72 | 108..254 | 147 | 147 | 116 | 31 | 1 | 1 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134 |
| 73 | 108..565 | 458 | 458 | 405 | 53 | 12 | 7 | 28 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 108..276 | 169 | 169 | 60 | 109 | 3 | 1 | 106 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 75 | 108..556 | 449 | 449 | 368 | 81 | 20 | 21 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 121..298 | 178 | 178 | 136 | 42 | 4 | 2 | 37 | 78896, 78969, 78971, 79045, 79102, 79103, 79105, 79108, 79110, 79116 |
| 83 | 122..151 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 87 | 126..544 | 419 | 419 | 374 | 45 | 14 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 91 | 126..567 | 442 | 442 | 385 | 57 | 16 | 9 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 94 | 134..246 | 113 | 113 | 68 | 45 | 5 | 2 | 39 | 78899, 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 95 | 134..458 | 325 | 325 | 273 | 52 | 16 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 100 | 142..506 | 365 | 365 | 310 | 55 | 16 | 6 | 25 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 109 | 158..520 | 363 | 363 | 302 | 61 | 24 | 3 | 30 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 118 | 167..196 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 127 | 182..510 | 329 | 329 | 267 | 62 | 19 | 9 | 32 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 133 | 199..473 | 275 | 275 | 237 | 38 | 11 | 3 | 23 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79132, 79135 |
| 149 | 248..468 | 221 | 221 | 170 | 51 | 16 | 2 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 150 | 248..463 | 216 | 216 | 167 | 49 | 13 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 151 | 248..559 | 312 | 312 | 272 | 40 | 10 | 2 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 198 | 372..661 | 290 | 290 | 160 | 130 | 7 | 3 | 119 | 79135, 79139 |
| 207 | 397..513 | 117 | 117 | 76 | 41 | 9 | 5 | 21 | 79105, 79108, 79111, 79116, 79128, 79132, 79135 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8388; unmatched reference entries: 1754; unmatched candidate entries: 1645
- identity switches: 1270; fragmentation (coverage interruptions): 1102; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 42 -> 49 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 78971: 42 -> 45 at (2108.5, 3033.5), 4 frames after previous cover
- f92: ref 79045: 49 -> 51 at (2110.5, 3033.5), 1 frames after previous cover
- f93: ref 78897: 42 -> 49 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 45 -> 48 at (2095, 3033.5), 2 frames after previous cover
- f95: ref 78897: 49 -> 42 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 49 -> 51 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 42 -> 48 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 48 -> 45 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 45 -> 48 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 51 -> 48 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 49 -> 51 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 48 -> 62 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 48 -> 42 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 49 -> 51 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 42 -> 48 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 49 -> 51 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78899: 51 -> 42 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 48 -> 62 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 51 -> 66 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 51 -> 66 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 62 -> 70 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 49 -> 51 at (2116.5, 3023), 4 frames after previous cover
- f106: ref 79105: 49 -> 69 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 48 -> 74 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 66 -> 75 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 51 -> 72 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79110: 49 -> 73 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 66 -> 75 at (2077.5, 3029.5), 2 frames after previous cover
- f109: ref 79108: 49 -> 69 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 42 -> 66 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 51 -> 72 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 69 -> 51 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 79110: 73 -> 69 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 49 -> 73 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 75 -> 72 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 72 -> 51 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 51 -> 69 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 69 -> 73 at (2109, 3027), 2 frames after previous cover
- f113: ref 79108: 73 -> 69 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 69 -> 73 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 72 -> 66 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 75 -> 72 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 72 -> 75 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 66 -> 74 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 74 -> 70 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 51 -> 42 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 69 -> 75 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 73 -> 69 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 49 -> 51 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 78897: 42 -> 74 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 75 -> 66 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 75 -> 42 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 69 -> 75 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 74 -> 72 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 48 -> 74 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 70 -> 48 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 72 -> 66 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 74 -> 48 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 66 -> 72 at (2010.5, 3030), 3 frames after previous cover
- ... 1210 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 938 | 42 | 8 (938) |
| 78896 | 350 (76..429) | 289 | 34 | 95 (78), 150 (70), 82 (44), 45 (43), 62 (21), 127 (14), 70 (12), 48 (4), 75 (3) |
| 78969 | 352 (80..434) | 291 | 36 | 95 (83), 150 (83), 62 (44), 70 (30), 45 (21), 82 (17), 75 (12), 48 (1) |
| 78971 | 352 (84..439) | 278 | 41 | 70 (116), 149 (49), 82 (42), 62 (23), 74 (13), 75 (11), 95 (8), 150 (5), 48 (3), 127 (3), 42 (2), 45 (2), +1 more |
| 79045 | 355 (84..443) | 288 | 40 | 75 (71), 70 (68), 127 (43), 62 (21), 45 (16), 74 (15), 149 (10), 95 (9), 150 (9), 51 (8), 82 (7), 48 (4), +3 more |
| 79037 | 355 (86..445) | 278 | 47 | 149 (74), 75 (46), 51 (41), 62 (31), 48 (22), 70 (21), 45 (17), 127 (13), 42 (7), 74 (3), 95 (2), 87 (1) |
| 78897 | 345 (89..450) | 285 | 44 | 127 (59), 75 (38), 149 (33), 95 (31), 62 (30), 70 (29), 42 (18), 74 (12), 51 (11), 133 (7), 87 (6), 45 (5), +2 more |
| 78899 | 365 (91..455) | 285 | 50 | 62 (86), 51 (55), 127 (44), 45 (25), 95 (19), 72 (16), 75 (8), 74 (6), 66 (4), 87 (4), 70 (4), 149 (4), +5 more |
| 79097 | 366 (94..461) | 297 | 43 | 51 (83), 127 (44), 62 (39), 95 (38), 75 (27), 72 (17), 133 (16), 74 (8), 66 (5), 48 (5), 70 (4), 49 (3), +4 more |
| 79098 | 360 (97..467) | 301 | 46 | 109 (84), 75 (63), 62 (28), 49 (24), 127 (22), 70 (16), 48 (14), 66 (11), 51 (10), 72 (9), 133 (8), 95 (5), +2 more |
| 79102 | 371 (98..477) | 292 | 50 | 133 (70), 49 (36), 109 (36), 51 (23), 66 (19), 75 (17), 127 (16), 62 (15), 48 (14), 70 (14), 72 (10), 100 (10), +3 more |
| 79103 | 380 (99..481) | 306 | 46 | 133 (70), 109 (68), 66 (27), 51 (24), 72 (20), 91 (19), 100 (17), 49 (15), 82 (14), 87 (9), 127 (9), 48 (8), +2 more |
| 79105 | 379 (101..484) | 311 | 43 | 109 (86), 66 (31), 51 (27), 133 (27), 49 (26), 100 (24), 72 (16), 207 (15), 73 (10), 75 (9), 42 (9), 87 (9), +5 more |
| 79108 | 385 (104..492) | 313 | 47 | 66 (103), 49 (46), 109 (25), 100 (25), 69 (16), 48 (16), 133 (13), 72 (12), 87 (12), 207 (11), 75 (10), 51 (7), +5 more |
| 79110 | 388 (106..497) | 312 | 50 | 100 (95), 66 (76), 48 (29), 69 (24), 49 (20), 87 (15), 73 (12), 91 (10), 51 (9), 133 (7), 42 (4), 75 (3), +5 more |
| 79111 | 386 (109..500) | 324 | 43 | 87 (58), 100 (50), 49 (43), 69 (39), 73 (30), 48 (27), 66 (18), 91 (15), 51 (11), 133 (9), 207 (8), 42 (4), +4 more |
| 79115 | 421 (111..531) | 335 | 51 | 69 (95), 73 (81), 48 (47), 45 (20), 91 (17), 87 (17), 42 (15), 66 (14), 49 (8), 51 (6), 75 (6), 100 (4), +2 more |
| 79116 | 411 (114..530) | 353 | 39 | 91 (80), 151 (42), 48 (40), 73 (39), 66 (34), 42 (31), 87 (27), 69 (26), 51 (7), 75 (7), 49 (6), 100 (5), +5 more |
| 79122 | 404 (118..532) | 328 | 44 | 69 (51), 42 (49), 87 (42), 48 (36), 91 (33), 151 (33), 73 (25), 94 (16), 49 (13), 66 (11), 51 (8), 75 (5), +3 more |
| 79132 | 391 (120..515) | 322 | 44 | 87 (109), 69 (65), 48 (41), 45 (26), 91 (21), 73 (21), 66 (9), 100 (8), 94 (7), 207 (6), 133 (3), 151 (3), +2 more |
| 79128 | 402 (124..527) | 324 | 47 | 151 (58), 91 (37), 87 (31), 49 (30), 45 (29), 73 (26), 75 (26), 69 (24), 100 (21), 42 (15), 207 (10), 94 (9), +3 more |
| 79134 | 407 (127..533) | 333 | 50 | 69 (71), 91 (54), 73 (42), 48 (40), 151 (31), 49 (23), 45 (23), 42 (21), 100 (16), 87 (7), 72 (3), 94 (2) |
| 79135 | 409 (129..542) | 328 | 53 | 198 (65), 73 (55), 151 (49), 48 (37), 45 (29), 207 (24), 49 (21), 91 (16), 87 (15), 100 (7), 42 (4), 133 (4), +1 more |
| 79139 | 406 (132..537) | 343 | 39 | 198 (95), 91 (62), 151 (56), 45 (45), 42 (26), 49 (20), 73 (20), 94 (14), 48 (3), 100 (2) |
| 79136 | 393 (136..538) | 334 | 33 | 42 (206), 49 (40), 73 (38), 100 (26), 48 (23), 91 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 83 | 122..151 | 30 | 0 | 30 |
| 118 | 167..196 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 30/363/995; tracks with internal gaps: 28; total internal gaps: 398; longest internal gap: 21; tracks ending in coasting: 29 (trailing rows total 1018)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 14..1008 | 995 | 995 | 938 | 57 | 42 | 3 | 0 | 78911 |
| 42 | 84..561 | 478 | 478 | 421 | 57 | 18 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 45 | 87..448 | 362 | 362 | 309 | 53 | 12 | 5 | 35 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 48 | 89..562 | 474 | 474 | 428 | 46 | 12 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 89..529 | 441 | 441 | 382 | 59 | 17 | 6 | 29 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 91..496 | 406 | 406 | 332 | 74 | 21 | 9 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 62 | 100..484 | 385 | 385 | 338 | 47 | 12 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 66 | 103..524 | 422 | 422 | 364 | 58 | 17 | 4 | 27 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 69 | 106..560 | 455 | 455 | 416 | 39 | 10 | 1 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 70 | 106..472 | 367 | 367 | 314 | 53 | 21 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 72 | 108..254 | 147 | 147 | 116 | 31 | 1 | 1 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134 |
| 73 | 108..565 | 458 | 458 | 405 | 53 | 12 | 7 | 28 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 108..276 | 169 | 169 | 60 | 109 | 3 | 1 | 106 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 75 | 108..556 | 449 | 449 | 368 | 81 | 20 | 21 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 121..298 | 178 | 178 | 136 | 42 | 4 | 2 | 37 | 78896, 78969, 78971, 79045, 79102, 79103, 79105, 79108, 79110, 79116 |
| 83 | 122..151 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 87 | 126..544 | 419 | 419 | 374 | 45 | 14 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 91 | 126..567 | 442 | 442 | 385 | 57 | 16 | 9 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 94 | 134..246 | 113 | 113 | 68 | 45 | 5 | 2 | 39 | 78899, 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 95 | 134..458 | 325 | 325 | 273 | 52 | 16 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 100 | 142..506 | 365 | 365 | 310 | 55 | 16 | 6 | 25 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135, 79136, 79139 |
| 109 | 158..520 | 363 | 363 | 302 | 61 | 24 | 3 | 30 | 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 118 | 167..196 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 127 | 182..510 | 329 | 329 | 267 | 62 | 19 | 9 | 32 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 133 | 199..473 | 275 | 275 | 237 | 38 | 11 | 3 | 23 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79132, 79135 |
| 149 | 248..468 | 221 | 221 | 170 | 51 | 16 | 2 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 150 | 248..463 | 216 | 216 | 167 | 49 | 13 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 151 | 248..559 | 312 | 312 | 272 | 40 | 10 | 2 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 198 | 372..661 | 290 | 290 | 160 | 130 | 7 | 3 | 119 | 79135, 79139 |
| 207 | 397..513 | 117 | 117 | 76 | 41 | 9 | 5 | 21 | 79105, 79108, 79111, 79116, 79128, 79132, 79135 |
