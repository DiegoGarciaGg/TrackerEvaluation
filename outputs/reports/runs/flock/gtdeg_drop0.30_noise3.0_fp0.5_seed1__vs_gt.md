# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=2d84a169ca37
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise3.0_fp0.5_seed1/tracks.csv sha256=973f1921d249186d
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise3.0_fp0.5_seed1.csv sha256=2d84a169ca3770a6
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise3.0_fp0.5_seed1
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
| observations | none | 4 | 0.120 | 0.046 | 0.000 | 2.41 | 0.118 | 1178 | 2398.0 |
| observations | none | 6 | 0.163 | 0.061 | 0.350 | 3.20 | 0.176 | 1479 | 2345.0 |
| observations | none | 8 | 0.186 | 0.069 | 0.485 | 3.60 | 0.200 | 1532 | 2140.0 |
| observations | none | 12 | 0.208 | 0.079 | 0.531 | 4.03 | 0.220 | 1401 | 2007.0 |
| observations | ignore | 4 | 0.120 | 0.046 | 0.000 | 2.41 | 0.118 | 1178 | 2398.0 |
| observations | ignore | 6 | 0.163 | 0.061 | 0.350 | 3.20 | 0.176 | 1479 | 2345.0 |
| observations | ignore | 8 | 0.186 | 0.069 | 0.485 | 3.60 | 0.200 | 1532 | 2140.0 |
| observations | ignore | 12 | 0.208 | 0.079 | 0.531 | 4.03 | 0.220 | 1401 | 2007.0 |
| updates | none | 4 | 0.119 | 0.049 | -0.235 | 2.41 | 0.111 | 1242 | 2408.0 |
| updates | none | 6 | 0.170 | 0.068 | 0.183 | 3.26 | 0.171 | 1534 | 2078.0 |
| updates | none | 8 | 0.200 | 0.081 | 0.392 | 3.79 | 0.203 | 1556 | 1558.0 |
| updates | none | 12 | 0.232 | 0.095 | 0.520 | 4.47 | 0.235 | 1382 | 1154.0 |
| updates | ignore | 4 | 0.119 | 0.049 | -0.235 | 2.41 | 0.111 | 1242 | 2408.0 |
| updates | ignore | 6 | 0.170 | 0.068 | 0.183 | 3.26 | 0.171 | 1534 | 2078.0 |
| updates | ignore | 8 | 0.200 | 0.081 | 0.392 | 3.79 | 0.203 | 1556 | 1558.0 |
| updates | ignore | 12 | 0.232 | 0.095 | 0.520 | 4.47 | 0.235 | 1382 | 1154.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 6756; unmatched reference entries: 3386; unmatched candidate entries: 310
- identity switches: 1532; fragmentation (coverage interruptions): 2193; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 42 -> 49 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 44 -> 42 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 42 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 42 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 42 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 42 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 44 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 42 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 42 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 42 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 44 -> 51 at (2111.5, 3028.5), 4 frames after previous cover
- f102: ref 79098: 44 -> 51 at (2118, 3027), 1 frames after previous cover
- f103: ref 78899: 42 -> 49 at (2086, 3030), 2 frames after previous cover
- f103: ref 79097: 51 -> 42 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 57 -> 44 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 49 -> 39 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 60 -> 59 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 39 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 49 -> 39 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 60 -> 63 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 51 -> 42 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79105: 57 -> 44 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 39 -> 60 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 42 -> 49 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 44 -> 51 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 57 -> 44 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79097: 49 -> 44 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 60 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78969: 56 -> 66 at (1984.5, 3035), 2 frames after previous cover
- f108: ref 79037: 49 -> 63 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 44 -> 39 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79102: 57 -> 44 at (2096.5, 3027.5), 7 frames after previous cover
- f108: ref 79105: 44 -> 64 at (2113.5, 3025), 3 frames after previous cover
- f108: ref 79108: 44 -> 57 at (2131, 3027), 2 frames after previous cover
- f109: ref 78899: 39 -> 60 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 78969: 66 -> 56 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 79105: 64 -> 51 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 44 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 64 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78896: 56 -> 66 at (1946, 3034.5), 2 frames after previous cover
- f110: ref 78971: 59 -> 56 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 63 -> 59 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79103: 51 -> 44 at (2092.5, 3023.5), 2 frames after previous cover
- f111: ref 79037: 59 -> 63 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 63 -> 59 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 44 -> 42 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 44 -> 39 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79111: 57 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79037: 63 -> 59 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79098: 42 -> 39 at (2059, 3029.5), 2 frames after previous cover
- ... 1472 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 675 | 226 | 102 (383), 0 (292) |
| 78896 | 350 (76..429) | 224 | 76 | 110 (108), 66 (78), 73 (10), 56 (9), 83 (9), 39 (5), 51 (5) |
| 78969 | 352 (80..434) | 223 | 84 | 51 (42), 110 (41), 56 (26), 73 (26), 66 (23), 131 (18), 82 (15), 60 (14), 83 (8), 39 (6), 59 (4) |
| 78971 | 352 (84..439) | 221 | 80 | 60 (56), 73 (40), 77 (25), 56 (22), 82 (17), 131 (16), 110 (12), 51 (8), 66 (6), 59 (4), 64 (4), 42 (3), +4 more |
| 79045 | 355 (84..443) | 242 | 72 | 64 (39), 51 (38), 131 (30), 73 (28), 56 (27), 110 (22), 83 (15), 60 (12), 59 (7), 82 (6), 63 (5), 39 (4), +4 more |
| 79037 | 355 (86..445) | 242 | 71 | 131 (72), 56 (51), 83 (20), 64 (17), 60 (15), 51 (13), 110 (10), 59 (9), 77 (8), 63 (5), 73 (5), 39 (4), +6 more |
| 78897 | 345 (89..450) | 229 | 77 | 56 (68), 60 (53), 63 (20), 51 (17), 131 (14), 110 (10), 73 (9), 49 (8), 149 (8), 77 (5), 83 (4), 64 (4), +6 more |
| 78899 | 365 (91..455) | 244 | 84 | 149 (68), 56 (38), 63 (35), 60 (27), 131 (23), 49 (18), 51 (6), 86 (6), 44 (4), 110 (4), 77 (4), 42 (3), +4 more |
| 79097 | 366 (94..461) | 238 | 78 | 149 (68), 49 (51), 56 (37), 60 (23), 63 (17), 77 (10), 85 (8), 44 (3), 39 (3), 86 (3), 111 (3), 64 (3), +6 more |
| 79098 | 360 (97..467) | 238 | 76 | 49 (64), 149 (21), 102 (19), 147 (15), 63 (14), 111 (14), 192 (13), 71 (11), 64 (10), 60 (9), 56 (9), 193 (9), +9 more |
| 79102 | 371 (98..477) | 242 | 78 | 192 (33), 49 (31), 147 (23), 64 (22), 85 (19), 111 (19), 193 (18), 71 (16), 96 (10), 77 (8), 102 (8), 149 (7), +9 more |
| 79103 | 380 (99..481) | 259 | 79 | 147 (41), 71 (39), 193 (29), 192 (28), 111 (23), 96 (16), 64 (15), 102 (14), 85 (12), 51 (9), 110 (6), 44 (5), +8 more |
| 79105 | 379 (101..484) | 247 | 89 | 147 (47), 71 (30), 193 (25), 77 (23), 111 (19), 64 (17), 44 (15), 96 (13), 192 (13), 51 (8), 85 (8), 102 (7), +7 more |
| 79108 | 385 (104..492) | 269 | 79 | 96 (45), 111 (44), 44 (31), 71 (27), 64 (25), 147 (21), 49 (18), 77 (13), 85 (11), 63 (8), 60 (5), 42 (4), +7 more |
| 79110 | 388 (106..497) | 264 | 81 | 111 (51), 44 (34), 64 (24), 96 (24), 194 (19), 85 (17), 193 (17), 148 (16), 77 (15), 147 (8), 60 (7), 39 (7), +9 more |
| 79111 | 386 (109..500) | 265 | 87 | 96 (58), 44 (43), 64 (30), 111 (23), 39 (18), 85 (17), 147 (17), 49 (10), 77 (10), 194 (10), 71 (8), 51 (4), +8 more |
| 79115 | 421 (111..531) | 285 | 93 | 85 (72), 44 (53), 39 (40), 96 (22), 148 (19), 42 (14), 111 (11), 49 (9), 102 (7), 64 (6), 51 (6), 60 (5), +7 more |
| 79116 | 411 (114..530) | 274 | 81 | 42 (50), 39 (42), 44 (38), 111 (29), 85 (21), 102 (18), 194 (17), 64 (11), 129 (10), 148 (9), 96 (8), 71 (7), +4 more |
| 79122 | 404 (118..532) | 262 | 87 | 148 (63), 39 (37), 85 (30), 44 (28), 42 (20), 102 (18), 111 (12), 71 (12), 60 (9), 49 (9), 64 (5), 96 (5), +5 more |
| 79132 | 391 (120..515) | 256 | 80 | 148 (89), 39 (43), 44 (22), 194 (20), 42 (18), 64 (17), 85 (14), 102 (11), 49 (9), 60 (6), 57 (3), 51 (2), +2 more |
| 79128 | 402 (124..527) | 269 | 86 | 39 (62), 44 (57), 42 (29), 71 (27), 129 (22), 49 (15), 64 (10), 51 (8), 85 (7), 194 (6), 96 (5), 63 (5), +5 more |
| 79134 | 407 (127..533) | 283 | 85 | 42 (79), 39 (55), 71 (52), 85 (25), 129 (22), 44 (10), 96 (9), 111 (9), 49 (6), 51 (4), 60 (3), 63 (3), +3 more |
| 79135 | 409 (129..542) | 267 | 96 | 42 (79), 129 (47), 71 (37), 96 (33), 57 (21), 194 (13), 39 (11), 63 (8), 111 (6), 85 (4), 102 (3), 148 (2), +3 more |
| 79139 | 406 (132..537) | 269 | 88 | 129 (66), 85 (41), 57 (39), 96 (35), 102 (28), 71 (13), 42 (12), 39 (9), 51 (6), 49 (6), 63 (4), 194 (4), +3 more |
| 79136 | 393 (136..538) | 269 | 80 | 102 (57), 129 (53), 51 (46), 63 (35), 49 (22), 111 (21), 42 (17), 85 (6), 57 (5), 44 (5), 71 (1), 39 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 184 | 338..338 | 1 | 0 | 1 |
| 327 | 734..734 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/299/849; tracks with internal gaps: 31; total internal gaps: 266; longest internal gap: 4; tracks ending in coasting: 16 (trailing rows total 26)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..456 | 455 | 315 | 292 | 23 | 21 | 1 | 2 | 78911 |
| 39 | 81..531 | 451 | 385 | 365 | 20 | 16 | 3 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 42 | 87..536 | 450 | 364 | 353 | 11 | 10 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..537 | 449 | 369 | 357 | 12 | 12 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..491 | 401 | 306 | 295 | 11 | 9 | 3 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..439 | 347 | 250 | 244 | 6 | 6 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 98..461 | 364 | 300 | 290 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 57 | 99..222 | 124 | 97 | 92 | 5 | 3 | 1 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 99..132 | 34 | 31 | 29 | 2 | 1 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 60 | 99..464 | 366 | 279 | 267 | 12 | 10 | 2 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 105..349 | 245 | 192 | 181 | 11 | 9 | 1 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 64 | 108..442 | 335 | 267 | 259 | 8 | 8 | 1 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 108..256 | 149 | 113 | 108 | 5 | 3 | 1 | 2 | 78896, 78969, 78971, 79037 |
| 71 | 113..493 | 381 | 308 | 298 | 10 | 9 | 1 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 73 | 117..256 | 140 | 124 | 119 | 5 | 4 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 77 | 125..342 | 218 | 149 | 138 | 11 | 8 | 1 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 82 | 132..192 | 61 | 45 | 41 | 4 | 2 | 1 | 2 | 78969, 78971, 79037, 79045 |
| 83 | 132..211 | 80 | 67 | 59 | 8 | 7 | 1 | 1 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 85 | 133..532 | 400 | 337 | 321 | 16 | 13 | 3 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 86 | 133..156 | 24 | 13 | 11 | 2 | 0 | 0 | 2 | 78899, 79097, 79098 |
| 96 | 147..542 | 396 | 299 | 284 | 15 | 14 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79139 |
| 102 | 160..1008 | 849 | 617 | 587 | 30 | 25 | 4 | 0 | 78911, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 110 | 176..482 | 307 | 221 | 214 | 7 | 7 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79105 |
| 111 | 179..528 | 350 | 299 | 289 | 10 | 10 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 129 | 205..537 | 333 | 236 | 228 | 8 | 7 | 2 | 0 | 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 131 | 210..452 | 243 | 184 | 176 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 147 | 243..462 | 220 | 177 | 174 | 3 | 1 | 1 | 2 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132 |
| 148 | 243..541 | 299 | 217 | 208 | 9 | 9 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79139 |
| 149 | 243..484 | 242 | 188 | 181 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 184 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 192 | 359..477 | 119 | 95 | 88 | 7 | 7 | 1 | 0 | 79098, 79102, 79103, 79105, 79110 |
| 193 | 359..500 | 142 | 107 | 104 | 3 | 3 | 1 | 0 | 78971, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 194 | 359..512 | 154 | 113 | 104 | 9 | 7 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 327 | 734..734 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 6756; unmatched reference entries: 3386; unmatched candidate entries: 310
- identity switches: 1532; fragmentation (coverage interruptions): 2193; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 42 -> 49 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 44 -> 42 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 42 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 42 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79045: 42 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 42 at (2112.5, 3033), 2 frames after previous cover
- f96: ref 78899: 44 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 42 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 42 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 42 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 3 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 44 -> 51 at (2111.5, 3028.5), 4 frames after previous cover
- f102: ref 79098: 44 -> 51 at (2118, 3027), 1 frames after previous cover
- f103: ref 78899: 42 -> 49 at (2086, 3030), 2 frames after previous cover
- f103: ref 79097: 51 -> 42 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 57 -> 44 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 49 -> 39 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 60 -> 59 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 39 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 49 -> 39 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 60 -> 63 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 51 -> 42 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79105: 57 -> 44 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 39 -> 60 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 42 -> 49 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 44 -> 51 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 57 -> 44 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 3 frames after previous cover
- f107: ref 79097: 49 -> 44 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 60 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78969: 56 -> 66 at (1984.5, 3035), 2 frames after previous cover
- f108: ref 79037: 49 -> 63 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 44 -> 39 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79102: 57 -> 44 at (2096.5, 3027.5), 7 frames after previous cover
- f108: ref 79105: 44 -> 64 at (2113.5, 3025), 3 frames after previous cover
- f108: ref 79108: 44 -> 57 at (2131, 3027), 2 frames after previous cover
- f109: ref 78899: 39 -> 60 at (2049.5, 3031), 2 frames after previous cover
- f109: ref 78969: 66 -> 56 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 79105: 64 -> 51 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 44 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 64 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78896: 56 -> 66 at (1946, 3034.5), 2 frames after previous cover
- f110: ref 78971: 59 -> 56 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 63 -> 59 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79103: 51 -> 44 at (2092.5, 3023.5), 2 frames after previous cover
- f111: ref 79037: 59 -> 63 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 63 -> 59 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 44 -> 42 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 44 -> 39 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79111: 57 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79037: 63 -> 59 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79098: 42 -> 39 at (2059, 3029.5), 2 frames after previous cover
- ... 1472 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 675 | 226 | 102 (383), 0 (292) |
| 78896 | 350 (76..429) | 224 | 76 | 110 (108), 66 (78), 73 (10), 56 (9), 83 (9), 39 (5), 51 (5) |
| 78969 | 352 (80..434) | 223 | 84 | 51 (42), 110 (41), 56 (26), 73 (26), 66 (23), 131 (18), 82 (15), 60 (14), 83 (8), 39 (6), 59 (4) |
| 78971 | 352 (84..439) | 221 | 80 | 60 (56), 73 (40), 77 (25), 56 (22), 82 (17), 131 (16), 110 (12), 51 (8), 66 (6), 59 (4), 64 (4), 42 (3), +4 more |
| 79045 | 355 (84..443) | 242 | 72 | 64 (39), 51 (38), 131 (30), 73 (28), 56 (27), 110 (22), 83 (15), 60 (12), 59 (7), 82 (6), 63 (5), 39 (4), +4 more |
| 79037 | 355 (86..445) | 242 | 71 | 131 (72), 56 (51), 83 (20), 64 (17), 60 (15), 51 (13), 110 (10), 59 (9), 77 (8), 63 (5), 73 (5), 39 (4), +6 more |
| 78897 | 345 (89..450) | 229 | 77 | 56 (68), 60 (53), 63 (20), 51 (17), 131 (14), 110 (10), 73 (9), 49 (8), 149 (8), 77 (5), 83 (4), 64 (4), +6 more |
| 78899 | 365 (91..455) | 244 | 84 | 149 (68), 56 (38), 63 (35), 60 (27), 131 (23), 49 (18), 51 (6), 86 (6), 44 (4), 110 (4), 77 (4), 42 (3), +4 more |
| 79097 | 366 (94..461) | 238 | 78 | 149 (68), 49 (51), 56 (37), 60 (23), 63 (17), 77 (10), 85 (8), 44 (3), 39 (3), 86 (3), 111 (3), 64 (3), +6 more |
| 79098 | 360 (97..467) | 238 | 76 | 49 (64), 149 (21), 102 (19), 147 (15), 63 (14), 111 (14), 192 (13), 71 (11), 64 (10), 60 (9), 56 (9), 193 (9), +9 more |
| 79102 | 371 (98..477) | 242 | 78 | 192 (33), 49 (31), 147 (23), 64 (22), 85 (19), 111 (19), 193 (18), 71 (16), 96 (10), 77 (8), 102 (8), 149 (7), +9 more |
| 79103 | 380 (99..481) | 259 | 79 | 147 (41), 71 (39), 193 (29), 192 (28), 111 (23), 96 (16), 64 (15), 102 (14), 85 (12), 51 (9), 110 (6), 44 (5), +8 more |
| 79105 | 379 (101..484) | 247 | 89 | 147 (47), 71 (30), 193 (25), 77 (23), 111 (19), 64 (17), 44 (15), 96 (13), 192 (13), 51 (8), 85 (8), 102 (7), +7 more |
| 79108 | 385 (104..492) | 269 | 79 | 96 (45), 111 (44), 44 (31), 71 (27), 64 (25), 147 (21), 49 (18), 77 (13), 85 (11), 63 (8), 60 (5), 42 (4), +7 more |
| 79110 | 388 (106..497) | 264 | 81 | 111 (51), 44 (34), 64 (24), 96 (24), 194 (19), 85 (17), 193 (17), 148 (16), 77 (15), 147 (8), 60 (7), 39 (7), +9 more |
| 79111 | 386 (109..500) | 265 | 87 | 96 (58), 44 (43), 64 (30), 111 (23), 39 (18), 85 (17), 147 (17), 49 (10), 77 (10), 194 (10), 71 (8), 51 (4), +8 more |
| 79115 | 421 (111..531) | 285 | 93 | 85 (72), 44 (53), 39 (40), 96 (22), 148 (19), 42 (14), 111 (11), 49 (9), 102 (7), 64 (6), 51 (6), 60 (5), +7 more |
| 79116 | 411 (114..530) | 274 | 81 | 42 (50), 39 (42), 44 (38), 111 (29), 85 (21), 102 (18), 194 (17), 64 (11), 129 (10), 148 (9), 96 (8), 71 (7), +4 more |
| 79122 | 404 (118..532) | 262 | 87 | 148 (63), 39 (37), 85 (30), 44 (28), 42 (20), 102 (18), 111 (12), 71 (12), 60 (9), 49 (9), 64 (5), 96 (5), +5 more |
| 79132 | 391 (120..515) | 256 | 80 | 148 (89), 39 (43), 44 (22), 194 (20), 42 (18), 64 (17), 85 (14), 102 (11), 49 (9), 60 (6), 57 (3), 51 (2), +2 more |
| 79128 | 402 (124..527) | 269 | 86 | 39 (62), 44 (57), 42 (29), 71 (27), 129 (22), 49 (15), 64 (10), 51 (8), 85 (7), 194 (6), 96 (5), 63 (5), +5 more |
| 79134 | 407 (127..533) | 283 | 85 | 42 (79), 39 (55), 71 (52), 85 (25), 129 (22), 44 (10), 96 (9), 111 (9), 49 (6), 51 (4), 60 (3), 63 (3), +3 more |
| 79135 | 409 (129..542) | 267 | 96 | 42 (79), 129 (47), 71 (37), 96 (33), 57 (21), 194 (13), 39 (11), 63 (8), 111 (6), 85 (4), 102 (3), 148 (2), +3 more |
| 79139 | 406 (132..537) | 269 | 88 | 129 (66), 85 (41), 57 (39), 96 (35), 102 (28), 71 (13), 42 (12), 39 (9), 51 (6), 49 (6), 63 (4), 194 (4), +3 more |
| 79136 | 393 (136..538) | 269 | 80 | 102 (57), 129 (53), 51 (46), 63 (35), 49 (22), 111 (21), 42 (17), 85 (6), 57 (5), 44 (5), 71 (1), 39 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 184 | 338..338 | 1 | 0 | 1 |
| 327 | 734..734 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/299/849; tracks with internal gaps: 31; total internal gaps: 266; longest internal gap: 4; tracks ending in coasting: 16 (trailing rows total 26)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..456 | 455 | 315 | 292 | 23 | 21 | 1 | 2 | 78911 |
| 39 | 81..531 | 451 | 385 | 365 | 20 | 16 | 3 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 42 | 87..536 | 450 | 364 | 353 | 11 | 10 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..537 | 449 | 369 | 357 | 12 | 12 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..491 | 401 | 306 | 295 | 11 | 9 | 3 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..439 | 347 | 250 | 244 | 6 | 6 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 98..461 | 364 | 300 | 290 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 57 | 99..222 | 124 | 97 | 92 | 5 | 3 | 1 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 99..132 | 34 | 31 | 29 | 2 | 1 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 60 | 99..464 | 366 | 279 | 267 | 12 | 10 | 2 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 105..349 | 245 | 192 | 181 | 11 | 9 | 1 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 64 | 108..442 | 335 | 267 | 259 | 8 | 8 | 1 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 108..256 | 149 | 113 | 108 | 5 | 3 | 1 | 2 | 78896, 78969, 78971, 79037 |
| 71 | 113..493 | 381 | 308 | 298 | 10 | 9 | 1 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 73 | 117..256 | 140 | 124 | 119 | 5 | 4 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 77 | 125..342 | 218 | 149 | 138 | 11 | 8 | 1 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 82 | 132..192 | 61 | 45 | 41 | 4 | 2 | 1 | 2 | 78969, 78971, 79037, 79045 |
| 83 | 132..211 | 80 | 67 | 59 | 8 | 7 | 1 | 1 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 85 | 133..532 | 400 | 337 | 321 | 16 | 13 | 3 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 86 | 133..156 | 24 | 13 | 11 | 2 | 0 | 0 | 2 | 78899, 79097, 79098 |
| 96 | 147..542 | 396 | 299 | 284 | 15 | 14 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79139 |
| 102 | 160..1008 | 849 | 617 | 587 | 30 | 25 | 4 | 0 | 78911, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 110 | 176..482 | 307 | 221 | 214 | 7 | 7 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79105 |
| 111 | 179..528 | 350 | 299 | 289 | 10 | 10 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 129 | 205..537 | 333 | 236 | 228 | 8 | 7 | 2 | 0 | 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 131 | 210..452 | 243 | 184 | 176 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 147 | 243..462 | 220 | 177 | 174 | 3 | 1 | 1 | 2 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132 |
| 148 | 243..541 | 299 | 217 | 208 | 9 | 9 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79139 |
| 149 | 243..484 | 242 | 188 | 181 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 184 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 192 | 359..477 | 119 | 95 | 88 | 7 | 7 | 1 | 0 | 79098, 79102, 79103, 79105, 79110 |
| 193 | 359..500 | 142 | 107 | 104 | 3 | 3 | 1 | 0 | 78971, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 194 | 359..512 | 154 | 113 | 104 | 9 | 7 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 327 | 734..734 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7810; unmatched reference entries: 2332; unmatched candidate entries: 2277
- identity switches: 1556; fragmentation (coverage interruptions): 1503; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 42 -> 49 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 44 -> 42 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 42 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 42 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 42 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 42 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 44 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 42 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 42 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 42 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 44 -> 51 at (2111.5, 3028.5), 3 frames after previous cover
- f102: ref 79098: 44 -> 51 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 57 -> 44 at (2130.5, 3027), 1 frames after previous cover
- f103: ref 78899: 42 -> 49 at (2086, 3030), 1 frames after previous cover
- f103: ref 79097: 51 -> 42 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 57 -> 44 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 49 -> 39 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 60 -> 59 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 39 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 49 -> 39 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 60 -> 63 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 51 -> 42 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 44 -> 51 at (2113.5, 3026.5), 3 frames after previous cover
- f105: ref 79105: 57 -> 44 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 39 -> 60 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 42 -> 49 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 44 -> 51 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 57 -> 44 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79097: 49 -> 44 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 60 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 39 -> 60 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 56 -> 66 at (1984.5, 3035), 2 frames after previous cover
- f108: ref 79037: 49 -> 63 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 44 -> 39 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79102: 51 -> 44 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 44 -> 64 at (2113.5, 3025), 3 frames after previous cover
- f108: ref 79108: 44 -> 57 at (2131, 3027), 2 frames after previous cover
- f109: ref 79105: 64 -> 51 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 44 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 64 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78896: 56 -> 66 at (1946, 3034.5), 2 frames after previous cover
- f110: ref 78971: 59 -> 56 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 63 -> 59 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79103: 51 -> 44 at (2092.5, 3023.5), 2 frames after previous cover
- f111: ref 79037: 59 -> 63 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 63 -> 59 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 44 -> 42 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 44 -> 39 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79111: 57 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79037: 63 -> 59 at (2000.5, 3035), 1 frames after previous cover
- ... 1496 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 899 | 77 | 102 (493), 0 (406) |
| 78896 | 350 (76..429) | 264 | 50 | 110 (127), 66 (90), 83 (11), 73 (11), 56 (10), 51 (9), 39 (6) |
| 78969 | 352 (80..434) | 257 | 58 | 51 (50), 110 (48), 56 (33), 73 (27), 66 (26), 131 (21), 82 (18), 60 (15), 83 (8), 39 (6), 59 (5) |
| 78971 | 352 (84..439) | 263 | 51 | 60 (71), 73 (45), 77 (29), 56 (27), 82 (18), 131 (17), 110 (16), 51 (11), 66 (6), 59 (5), 64 (5), 49 (4), +4 more |
| 79045 | 355 (84..443) | 269 | 55 | 64 (48), 51 (45), 131 (32), 56 (31), 73 (28), 110 (24), 83 (15), 60 (13), 59 (7), 82 (7), 63 (5), 77 (5), +4 more |
| 79037 | 355 (86..445) | 273 | 53 | 131 (85), 56 (54), 83 (24), 64 (19), 51 (18), 60 (16), 110 (10), 77 (10), 59 (9), 63 (5), 73 (5), 49 (4), +6 more |
| 78897 | 345 (89..450) | 263 | 54 | 56 (75), 60 (61), 51 (23), 63 (20), 131 (17), 110 (12), 73 (11), 149 (9), 49 (8), 83 (6), 64 (6), 77 (5), +6 more |
| 78899 | 365 (91..455) | 276 | 61 | 149 (75), 56 (40), 63 (35), 60 (32), 131 (30), 49 (23), 86 (8), 51 (7), 110 (6), 44 (4), 42 (4), 77 (4), +4 more |
| 79097 | 366 (94..461) | 262 | 63 | 149 (77), 49 (55), 56 (44), 60 (24), 63 (18), 77 (11), 85 (8), 44 (4), 39 (3), 86 (3), 111 (3), 64 (3), +6 more |
| 79098 | 360 (97..467) | 262 | 57 | 49 (75), 149 (24), 102 (21), 147 (16), 63 (15), 111 (15), 192 (14), 71 (11), 64 (10), 193 (10), 60 (9), 56 (9), +9 more |
| 79102 | 371 (98..477) | 276 | 60 | 49 (37), 192 (36), 64 (27), 85 (24), 193 (24), 111 (23), 147 (23), 71 (16), 96 (10), 77 (8), 102 (8), 149 (8), +9 more |
| 79103 | 380 (99..481) | 287 | 60 | 147 (50), 71 (42), 192 (34), 193 (31), 111 (23), 96 (18), 64 (17), 102 (16), 85 (12), 51 (9), 110 (7), 60 (6), +8 more |
| 79105 | 379 (101..484) | 281 | 65 | 147 (54), 71 (33), 193 (31), 77 (24), 111 (21), 64 (20), 44 (17), 192 (16), 96 (15), 51 (9), 149 (9), 85 (8), +6 more |
| 79108 | 385 (104..492) | 300 | 56 | 96 (53), 111 (46), 44 (34), 71 (31), 147 (26), 64 (25), 49 (22), 77 (14), 85 (11), 63 (8), 60 (5), 194 (5), +8 more |
| 79110 | 388 (106..497) | 301 | 63 | 111 (58), 44 (38), 96 (28), 64 (27), 194 (25), 193 (23), 85 (19), 77 (16), 148 (15), 147 (9), 60 (8), 71 (8), +9 more |
| 79111 | 386 (109..500) | 308 | 54 | 96 (67), 44 (51), 64 (34), 111 (25), 147 (21), 39 (20), 85 (18), 49 (11), 77 (11), 194 (11), 71 (8), 148 (7), +8 more |
| 79115 | 421 (111..531) | 323 | 68 | 85 (82), 44 (60), 39 (49), 96 (26), 42 (19), 148 (18), 111 (11), 49 (10), 102 (7), 194 (7), 64 (6), 51 (6), +7 more |
| 79116 | 411 (114..530) | 301 | 67 | 42 (54), 44 (46), 39 (38), 111 (37), 85 (23), 102 (19), 194 (17), 64 (15), 129 (13), 148 (9), 96 (8), 71 (7), +5 more |
| 79122 | 404 (118..532) | 304 | 61 | 148 (81), 39 (42), 85 (35), 44 (31), 42 (25), 102 (21), 71 (16), 111 (13), 60 (9), 49 (9), 64 (5), 51 (4), +5 more |
| 79132 | 391 (120..515) | 281 | 60 | 148 (101), 39 (46), 42 (22), 44 (22), 194 (22), 64 (21), 102 (12), 85 (12), 49 (9), 60 (7), 57 (3), 51 (2), +2 more |
| 79128 | 402 (124..527) | 307 | 68 | 39 (71), 44 (66), 42 (32), 71 (30), 129 (28), 49 (16), 64 (11), 51 (9), 85 (8), 194 (7), 63 (6), 96 (5), +6 more |
| 79134 | 407 (127..533) | 324 | 60 | 42 (87), 39 (65), 71 (61), 85 (28), 129 (26), 44 (12), 96 (10), 111 (10), 49 (6), 51 (5), 60 (4), 102 (4), +3 more |
| 79135 | 409 (129..542) | 313 | 72 | 42 (90), 129 (55), 71 (49), 96 (38), 57 (23), 39 (14), 194 (14), 63 (9), 85 (5), 111 (5), 102 (3), 44 (3), +3 more |
| 79139 | 406 (132..537) | 305 | 60 | 129 (73), 85 (44), 57 (41), 96 (41), 102 (34), 71 (15), 39 (12), 44 (11), 42 (10), 49 (7), 51 (6), 63 (5), +2 more |
| 79136 | 393 (136..538) | 311 | 50 | 102 (69), 129 (57), 51 (54), 63 (47), 42 (24), 49 (23), 111 (23), 85 (7), 57 (5), 71 (1), 44 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 184 | 338..367 | 30 | 0 | 30 |
| 327 | 734..763 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/328/849; tracks with internal gaps: 32; total internal gaps: 777; longest internal gap: 30; tracks ending in coasting: 33 (trailing rows total 1067)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..485 | 484 | 484 | 406 | 78 | 33 | 3 | 37 | 78911 |
| 39 | 81..560 | 480 | 480 | 404 | 76 | 37 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 42 | 87..565 | 479 | 479 | 400 | 79 | 39 | 4 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..566 | 478 | 478 | 413 | 65 | 35 | 3 | 24 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..520 | 430 | 430 | 334 | 96 | 38 | 20 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..468 | 376 | 376 | 293 | 83 | 28 | 13 | 18 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 98..490 | 393 | 393 | 326 | 67 | 34 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 57 | 99..251 | 153 | 153 | 98 | 55 | 10 | 5 | 40 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 99..161 | 63 | 63 | 31 | 32 | 2 | 1 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 60 | 99..493 | 395 | 395 | 303 | 92 | 31 | 20 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 105..378 | 274 | 274 | 200 | 74 | 27 | 3 | 41 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 64 | 108..471 | 364 | 364 | 299 | 65 | 30 | 4 | 28 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 108..285 | 178 | 178 | 124 | 54 | 9 | 2 | 44 | 78896, 78969, 78971, 79037 |
| 71 | 113..522 | 410 | 410 | 340 | 70 | 22 | 3 | 43 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 73 | 117..285 | 169 | 169 | 128 | 41 | 10 | 1 | 31 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 77 | 125..371 | 247 | 247 | 151 | 96 | 20 | 3 | 67 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 82 | 132..221 | 90 | 90 | 45 | 45 | 5 | 1 | 40 | 78969, 78971, 79037, 79045 |
| 83 | 132..240 | 109 | 109 | 67 | 42 | 11 | 2 | 30 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 85 | 133..561 | 429 | 429 | 353 | 76 | 31 | 5 | 28 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 86 | 133..185 | 53 | 53 | 13 | 40 | 1 | 1 | 39 | 78899, 79097, 79098 |
| 96 | 147..571 | 425 | 425 | 325 | 100 | 41 | 12 | 32 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79139 |
| 102 | 160..1008 | 849 | 849 | 726 | 123 | 65 | 30 | 0 | 78911, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 110 | 176..511 | 336 | 336 | 251 | 85 | 28 | 19 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79108 |
| 111 | 179..557 | 379 | 379 | 317 | 62 | 27 | 3 | 27 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 129 | 205..566 | 362 | 362 | 262 | 100 | 29 | 23 | 31 | 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 131 | 210..481 | 272 | 272 | 205 | 67 | 31 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 147 | 243..491 | 249 | 249 | 202 | 47 | 14 | 2 | 30 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132 |
| 148 | 243..570 | 328 | 328 | 241 | 87 | 28 | 9 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79139 |
| 149 | 243..513 | 271 | 271 | 206 | 65 | 23 | 4 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 184 | 338..367 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 192 | 359..506 | 148 | 148 | 101 | 47 | 12 | 3 | 29 | 79098, 79102, 79103, 79105, 79110 |
| 193 | 359..529 | 171 | 171 | 129 | 42 | 10 | 2 | 29 | 78971, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 194 | 359..541 | 183 | 183 | 117 | 66 | 16 | 3 | 40 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 327 | 734..763 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7810; unmatched reference entries: 2332; unmatched candidate entries: 2277
- identity switches: 1556; fragmentation (coverage interruptions): 1503; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78971: 42 -> 49 at (2108.5, 3033.5), 1 frames after previous cover
- f92: ref 79037: 44 -> 42 at (2124, 3034), 3 frames after previous cover
- f93: ref 79037: 42 -> 51 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 51 at (2125, 3030), 3 frames after previous cover
- f94: ref 79037: 51 -> 42 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78971: 49 -> 39 at (2084, 3033.5), 1 frames after previous cover
- f95: ref 79045: 42 -> 49 at (2092.5, 3034), 2 frames after previous cover
- f96: ref 78897: 51 -> 42 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 44 -> 51 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 42 -> 49 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 49 -> 39 at (2087.5, 3033.5), 1 frames after previous cover
- f98: ref 78896: 39 -> 56 at (2023, 3033), 9 frames after previous cover
- f99: ref 78897: 42 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 51 -> 42 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78969: 39 -> 59 at (2041.5, 3033.5), 5 frames after previous cover
- f99: ref 78971: 39 -> 60 at (2059.5, 3034), 4 frames after previous cover
- f100: ref 79037: 49 -> 39 at (2076, 3033.5), 2 frames after previous cover
- f101: ref 79045: 39 -> 60 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79097: 44 -> 51 at (2111.5, 3028.5), 3 frames after previous cover
- f102: ref 79098: 44 -> 51 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 57 -> 44 at (2130.5, 3027), 1 frames after previous cover
- f103: ref 78899: 42 -> 49 at (2086, 3030), 1 frames after previous cover
- f103: ref 79097: 51 -> 42 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79103: 57 -> 44 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 49 -> 39 at (2064, 3032), 2 frames after previous cover
- f104: ref 78971: 60 -> 59 at (2027.5, 3034.5), 4 frames after previous cover
- f104: ref 79037: 39 -> 60 at (2051, 3034), 1 frames after previous cover
- f105: ref 78899: 49 -> 39 at (2074, 3031), 1 frames after previous cover
- f105: ref 79045: 60 -> 63 at (2030.5, 3033.5), 2 frames after previous cover
- f105: ref 79098: 51 -> 42 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 44 -> 51 at (2113.5, 3026.5), 3 frames after previous cover
- f105: ref 79105: 57 -> 44 at (2130.5, 3023.5), 2 frames after previous cover
- f106: ref 78897: 39 -> 60 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 78969: 59 -> 56 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79097: 42 -> 49 at (2082.5, 3028.5), 2 frames after previous cover
- f106: ref 79103: 44 -> 51 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 57 -> 44 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 79037: 60 -> 49 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79097: 49 -> 44 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 60 -> 49 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 39 -> 60 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 56 -> 66 at (1984.5, 3035), 2 frames after previous cover
- f108: ref 79037: 49 -> 63 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 44 -> 39 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79102: 51 -> 44 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 44 -> 64 at (2113.5, 3025), 3 frames after previous cover
- f108: ref 79108: 44 -> 57 at (2131, 3027), 2 frames after previous cover
- f109: ref 79105: 64 -> 51 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 57 -> 44 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 57 -> 64 at (2139.5, 3026.5), 3 frames after previous cover
- f110: ref 78896: 56 -> 66 at (1946, 3034.5), 2 frames after previous cover
- f110: ref 78971: 59 -> 56 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 63 -> 59 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79103: 51 -> 44 at (2092.5, 3023.5), 2 frames after previous cover
- f111: ref 79037: 59 -> 63 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 63 -> 59 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79102: 44 -> 42 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79103: 44 -> 39 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79111: 57 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79037: 63 -> 59 at (2000.5, 3035), 1 frames after previous cover
- ... 1496 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 899 | 77 | 102 (493), 0 (406) |
| 78896 | 350 (76..429) | 264 | 50 | 110 (127), 66 (90), 83 (11), 73 (11), 56 (10), 51 (9), 39 (6) |
| 78969 | 352 (80..434) | 257 | 58 | 51 (50), 110 (48), 56 (33), 73 (27), 66 (26), 131 (21), 82 (18), 60 (15), 83 (8), 39 (6), 59 (5) |
| 78971 | 352 (84..439) | 263 | 51 | 60 (71), 73 (45), 77 (29), 56 (27), 82 (18), 131 (17), 110 (16), 51 (11), 66 (6), 59 (5), 64 (5), 49 (4), +4 more |
| 79045 | 355 (84..443) | 269 | 55 | 64 (48), 51 (45), 131 (32), 56 (31), 73 (28), 110 (24), 83 (15), 60 (13), 59 (7), 82 (7), 63 (5), 77 (5), +4 more |
| 79037 | 355 (86..445) | 273 | 53 | 131 (85), 56 (54), 83 (24), 64 (19), 51 (18), 60 (16), 110 (10), 77 (10), 59 (9), 63 (5), 73 (5), 49 (4), +6 more |
| 78897 | 345 (89..450) | 263 | 54 | 56 (75), 60 (61), 51 (23), 63 (20), 131 (17), 110 (12), 73 (11), 149 (9), 49 (8), 83 (6), 64 (6), 77 (5), +6 more |
| 78899 | 365 (91..455) | 276 | 61 | 149 (75), 56 (40), 63 (35), 60 (32), 131 (30), 49 (23), 86 (8), 51 (7), 110 (6), 44 (4), 42 (4), 77 (4), +4 more |
| 79097 | 366 (94..461) | 262 | 63 | 149 (77), 49 (55), 56 (44), 60 (24), 63 (18), 77 (11), 85 (8), 44 (4), 39 (3), 86 (3), 111 (3), 64 (3), +6 more |
| 79098 | 360 (97..467) | 262 | 57 | 49 (75), 149 (24), 102 (21), 147 (16), 63 (15), 111 (15), 192 (14), 71 (11), 64 (10), 193 (10), 60 (9), 56 (9), +9 more |
| 79102 | 371 (98..477) | 276 | 60 | 49 (37), 192 (36), 64 (27), 85 (24), 193 (24), 111 (23), 147 (23), 71 (16), 96 (10), 77 (8), 102 (8), 149 (8), +9 more |
| 79103 | 380 (99..481) | 287 | 60 | 147 (50), 71 (42), 192 (34), 193 (31), 111 (23), 96 (18), 64 (17), 102 (16), 85 (12), 51 (9), 110 (7), 60 (6), +8 more |
| 79105 | 379 (101..484) | 281 | 65 | 147 (54), 71 (33), 193 (31), 77 (24), 111 (21), 64 (20), 44 (17), 192 (16), 96 (15), 51 (9), 149 (9), 85 (8), +6 more |
| 79108 | 385 (104..492) | 300 | 56 | 96 (53), 111 (46), 44 (34), 71 (31), 147 (26), 64 (25), 49 (22), 77 (14), 85 (11), 63 (8), 60 (5), 194 (5), +8 more |
| 79110 | 388 (106..497) | 301 | 63 | 111 (58), 44 (38), 96 (28), 64 (27), 194 (25), 193 (23), 85 (19), 77 (16), 148 (15), 147 (9), 60 (8), 71 (8), +9 more |
| 79111 | 386 (109..500) | 308 | 54 | 96 (67), 44 (51), 64 (34), 111 (25), 147 (21), 39 (20), 85 (18), 49 (11), 77 (11), 194 (11), 71 (8), 148 (7), +8 more |
| 79115 | 421 (111..531) | 323 | 68 | 85 (82), 44 (60), 39 (49), 96 (26), 42 (19), 148 (18), 111 (11), 49 (10), 102 (7), 194 (7), 64 (6), 51 (6), +7 more |
| 79116 | 411 (114..530) | 301 | 67 | 42 (54), 44 (46), 39 (38), 111 (37), 85 (23), 102 (19), 194 (17), 64 (15), 129 (13), 148 (9), 96 (8), 71 (7), +5 more |
| 79122 | 404 (118..532) | 304 | 61 | 148 (81), 39 (42), 85 (35), 44 (31), 42 (25), 102 (21), 71 (16), 111 (13), 60 (9), 49 (9), 64 (5), 51 (4), +5 more |
| 79132 | 391 (120..515) | 281 | 60 | 148 (101), 39 (46), 42 (22), 44 (22), 194 (22), 64 (21), 102 (12), 85 (12), 49 (9), 60 (7), 57 (3), 51 (2), +2 more |
| 79128 | 402 (124..527) | 307 | 68 | 39 (71), 44 (66), 42 (32), 71 (30), 129 (28), 49 (16), 64 (11), 51 (9), 85 (8), 194 (7), 63 (6), 96 (5), +6 more |
| 79134 | 407 (127..533) | 324 | 60 | 42 (87), 39 (65), 71 (61), 85 (28), 129 (26), 44 (12), 96 (10), 111 (10), 49 (6), 51 (5), 60 (4), 102 (4), +3 more |
| 79135 | 409 (129..542) | 313 | 72 | 42 (90), 129 (55), 71 (49), 96 (38), 57 (23), 39 (14), 194 (14), 63 (9), 85 (5), 111 (5), 102 (3), 44 (3), +3 more |
| 79139 | 406 (132..537) | 305 | 60 | 129 (73), 85 (44), 57 (41), 96 (41), 102 (34), 71 (15), 39 (12), 44 (11), 42 (10), 49 (7), 51 (6), 63 (5), +2 more |
| 79136 | 393 (136..538) | 311 | 50 | 102 (69), 129 (57), 51 (54), 63 (47), 42 (24), 49 (23), 111 (23), 85 (7), 57 (5), 71 (1), 44 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 184 | 338..367 | 30 | 0 | 30 |
| 327 | 734..763 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/328/849; tracks with internal gaps: 32; total internal gaps: 777; longest internal gap: 30; tracks ending in coasting: 33 (trailing rows total 1067)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..485 | 484 | 484 | 406 | 78 | 33 | 3 | 37 | 78911 |
| 39 | 81..560 | 480 | 480 | 404 | 76 | 37 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 42 | 87..565 | 479 | 479 | 400 | 79 | 39 | 4 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 89..566 | 478 | 478 | 413 | 65 | 35 | 3 | 24 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 91..520 | 430 | 430 | 334 | 96 | 38 | 20 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 51 | 93..468 | 376 | 376 | 293 | 83 | 28 | 13 | 18 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 56 | 98..490 | 393 | 393 | 326 | 67 | 34 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 57 | 99..251 | 153 | 153 | 98 | 55 | 10 | 5 | 40 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 99..161 | 63 | 63 | 31 | 32 | 2 | 1 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 60 | 99..493 | 395 | 395 | 303 | 92 | 31 | 20 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 63 | 105..378 | 274 | 274 | 200 | 74 | 27 | 3 | 41 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 64 | 108..471 | 364 | 364 | 299 | 65 | 30 | 4 | 28 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 108..285 | 178 | 178 | 124 | 54 | 9 | 2 | 44 | 78896, 78969, 78971, 79037 |
| 71 | 113..522 | 410 | 410 | 340 | 70 | 22 | 3 | 43 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 73 | 117..285 | 169 | 169 | 128 | 41 | 10 | 1 | 31 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 77 | 125..371 | 247 | 247 | 151 | 96 | 20 | 3 | 67 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 82 | 132..221 | 90 | 90 | 45 | 45 | 5 | 1 | 40 | 78969, 78971, 79037, 79045 |
| 83 | 132..240 | 109 | 109 | 67 | 42 | 11 | 2 | 30 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 85 | 133..561 | 429 | 429 | 353 | 76 | 31 | 5 | 28 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 86 | 133..185 | 53 | 53 | 13 | 40 | 1 | 1 | 39 | 78899, 79097, 79098 |
| 96 | 147..571 | 425 | 425 | 325 | 100 | 41 | 12 | 32 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79139 |
| 102 | 160..1008 | 849 | 849 | 726 | 123 | 65 | 30 | 0 | 78911, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 110 | 176..511 | 336 | 336 | 251 | 85 | 28 | 19 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79108 |
| 111 | 179..557 | 379 | 379 | 317 | 62 | 27 | 3 | 27 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 129 | 205..566 | 362 | 362 | 262 | 100 | 29 | 23 | 31 | 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 131 | 210..481 | 272 | 272 | 205 | 67 | 31 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 147 | 243..491 | 249 | 249 | 202 | 47 | 14 | 2 | 30 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132 |
| 148 | 243..570 | 328 | 328 | 241 | 87 | 28 | 9 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79139 |
| 149 | 243..513 | 271 | 271 | 206 | 65 | 23 | 4 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 184 | 338..367 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 192 | 359..506 | 148 | 148 | 101 | 47 | 12 | 3 | 29 | 79098, 79102, 79103, 79105, 79110 |
| 193 | 359..529 | 171 | 171 | 129 | 42 | 10 | 2 | 29 | 78971, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 194 | 359..541 | 183 | 183 | 117 | 66 | 16 | 3 | 40 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 327 | 734..763 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
