# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=464181ec5d29
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise1.0_fp0.5_seed2/tracks.csv sha256=ddefb7bea5c8feb4
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise1.0_fp0.5_seed2.csv sha256=464181ec5d29c7e4
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise1.0_fp0.5_seed2
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
| observations | none | 4 | 0.245 | 0.105 | 0.543 | 1.27 | 0.242 | 1403 | 2072.0 |
| observations | none | 6 | 0.263 | 0.113 | 0.545 | 1.28 | 0.243 | 1392 | 2065.0 |
| observations | none | 8 | 0.272 | 0.118 | 0.545 | 1.30 | 0.247 | 1374 | 2062.0 |
| observations | none | 12 | 0.282 | 0.125 | 0.552 | 1.65 | 0.261 | 1282 | 2007.0 |
| observations | ignore | 4 | 0.245 | 0.105 | 0.543 | 1.27 | 0.242 | 1403 | 2072.0 |
| observations | ignore | 6 | 0.263 | 0.113 | 0.545 | 1.28 | 0.243 | 1392 | 2065.0 |
| observations | ignore | 8 | 0.272 | 0.118 | 0.545 | 1.30 | 0.247 | 1374 | 2062.0 |
| observations | ignore | 12 | 0.282 | 0.125 | 0.552 | 1.65 | 0.261 | 1282 | 2007.0 |
| updates | none | 4 | 0.240 | 0.113 | 0.329 | 1.34 | 0.226 | 1439 | 1980.0 |
| updates | none | 6 | 0.277 | 0.132 | 0.428 | 1.59 | 0.246 | 1437 | 1630.0 |
| updates | none | 8 | 0.299 | 0.144 | 0.522 | 1.93 | 0.265 | 1380 | 1319.0 |
| updates | none | 12 | 0.324 | 0.159 | 0.581 | 2.52 | 0.291 | 1268 | 1110.0 |
| updates | ignore | 4 | 0.240 | 0.113 | 0.329 | 1.34 | 0.226 | 1439 | 1980.0 |
| updates | ignore | 6 | 0.277 | 0.132 | 0.428 | 1.59 | 0.246 | 1437 | 1630.0 |
| updates | ignore | 8 | 0.299 | 0.144 | 0.522 | 1.93 | 0.265 | 1380 | 1319.0 |
| updates | ignore | 12 | 0.324 | 0.159 | 0.581 | 2.52 | 0.291 | 1268 | 1110.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 6965; unmatched reference entries: 3177; unmatched candidate entries: 60
- identity switches: 1374; fragmentation (coverage interruptions): 2109; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 43 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 42 -> 31 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 36 -> 44 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 79037: 31 -> 43 at (2118, 3034.5), 3 frames after previous cover
- f93: ref 79045: 43 -> 44 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 36 -> 40 at (2071, 3031), 4 frames after previous cover
- f94: ref 78971: 44 -> 36 at (2090.5, 3032.5), 2 frames after previous cover
- f95: ref 78969: 40 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 42 -> 50 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 36 -> 40 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 42 -> 50 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 31 -> 43 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 50 -> 31 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 43 -> 44 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 42 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 44 -> 31 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 50 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 31 -> 43 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 40 -> 36 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 50 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 42 -> 50 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 42 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 59 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 50 -> 43 at (2082.5, 3028.5), 6 frames after previous cover
- f106: ref 79105: 52 -> 42 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 78897: 59 -> 44 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 43 -> 59 at (2055.5, 3031), 4 frames after previous cover
- f109: ref 78971: 36 -> 61 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 50 -> 43 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 44 -> 31 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 61 -> 36 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 31 -> 61 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 59 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 43 -> 44 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 43 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 50 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 42 -> 63 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 52 -> 42 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 52 -> 64 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 31 -> 59 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 36 -> 61 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 61 -> 31 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 59 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 52 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 59 -> 31 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 59 -> 44 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 31 -> 61 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 59 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 44 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 43 -> 63 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 64 -> 42 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 42 -> 52 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 59 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 63 -> 43 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 63 -> 50 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 52 -> 63 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 52 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 64 -> 42 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 44 -> 66 at (2012.5, 3030), 1 frames after previous cover
- ... 1314 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 691 | 203 | 1 (691) |
| 78896 | 350 (76..429) | 223 | 75 | 91 (104), 40 (42), 87 (40), 36 (37) |
| 78969 | 352 (80..434) | 235 | 79 | 36 (104), 40 (35), 87 (31), 113 (20), 104 (19), 65 (13), 91 (5), 31 (4), 61 (4) |
| 78971 | 352 (84..439) | 245 | 70 | 36 (98), 31 (51), 113 (35), 40 (22), 65 (16), 188 (12), 61 (5), 87 (4), 44 (1), 104 (1) |
| 79045 | 355 (84..443) | 227 | 75 | 113 (62), 31 (42), 61 (35), 36 (29), 104 (19), 40 (14), 188 (12), 44 (5), 65 (5), 43 (2), 87 (2) |
| 79037 | 355 (86..445) | 245 | 73 | 104 (58), 113 (34), 31 (32), 40 (29), 61 (25), 91 (17), 44 (11), 177 (10), 66 (9), 87 (8), 36 (6), 43 (5), +1 more |
| 78897 | 345 (89..450) | 251 | 64 | 31 (47), 113 (40), 91 (30), 40 (30), 87 (20), 66 (19), 36 (17), 104 (16), 188 (7), 64 (5), 59 (4), 61 (4), +5 more |
| 78899 | 365 (91..455) | 241 | 82 | 31 (60), 91 (39), 87 (36), 66 (30), 64 (16), 40 (14), 177 (11), 67 (9), 113 (7), 44 (5), 104 (5), 43 (3), +4 more |
| 79097 | 366 (94..461) | 256 | 82 | 66 (68), 87 (41), 40 (24), 64 (22), 67 (19), 36 (19), 31 (15), 91 (11), 177 (8), 44 (7), 52 (7), 43 (4), +4 more |
| 79098 | 360 (97..467) | 253 | 76 | 66 (79), 40 (45), 31 (27), 87 (20), 52 (13), 67 (12), 44 (11), 177 (10), 59 (8), 91 (7), 65 (6), 64 (5), +4 more |
| 79102 | 371 (98..477) | 251 | 80 | 64 (36), 65 (31), 40 (27), 126 (26), 66 (22), 63 (17), 87 (17), 31 (16), 52 (11), 91 (9), 42 (8), 177 (8), +5 more |
| 79103 | 380 (99..481) | 260 | 83 | 66 (47), 63 (35), 65 (30), 126 (29), 52 (24), 64 (16), 44 (13), 42 (11), 40 (11), 87 (9), 31 (9), 67 (7), +6 more |
| 79105 | 379 (101..484) | 264 | 77 | 126 (45), 65 (38), 63 (32), 64 (32), 160 (21), 87 (15), 66 (14), 59 (10), 96 (9), 52 (8), 40 (8), 80 (7), +7 more |
| 79108 | 385 (104..492) | 286 | 70 | 160 (72), 126 (50), 52 (27), 96 (25), 80 (19), 63 (12), 104 (12), 59 (11), 66 (11), 42 (10), 88 (10), 40 (8), +6 more |
| 79110 | 388 (106..497) | 265 | 81 | 64 (47), 160 (44), 52 (35), 88 (25), 44 (17), 80 (17), 63 (14), 126 (11), 50 (10), 66 (10), 96 (9), 104 (8), +6 more |
| 79111 | 386 (109..500) | 258 | 83 | 64 (55), 52 (42), 44 (33), 80 (24), 50 (17), 160 (17), 88 (16), 96 (15), 63 (8), 42 (7), 126 (7), 65 (7), +3 more |
| 79115 | 421 (111..531) | 294 | 85 | 175 (45), 52 (38), 80 (35), 44 (32), 96 (25), 65 (23), 88 (21), 50 (19), 64 (17), 126 (16), 177 (7), 42 (5), +4 more |
| 79116 | 411 (114..530) | 286 | 84 | 96 (73), 44 (46), 80 (33), 88 (25), 52 (21), 64 (16), 59 (12), 175 (12), 126 (10), 177 (10), 63 (7), 50 (7), +4 more |
| 79122 | 404 (118..532) | 275 | 87 | 96 (88), 52 (30), 88 (30), 65 (23), 64 (17), 80 (17), 175 (14), 63 (10), 59 (9), 44 (9), 50 (8), 42 (7), +4 more |
| 79132 | 391 (120..515) | 266 | 77 | 64 (43), 80 (38), 44 (36), 65 (29), 96 (20), 42 (17), 88 (15), 52 (15), 67 (13), 104 (11), 126 (11), 175 (8), +4 more |
| 79128 | 402 (124..527) | 255 | 94 | 88 (47), 44 (35), 42 (34), 65 (26), 80 (22), 175 (22), 52 (14), 104 (12), 67 (11), 96 (10), 63 (7), 50 (5), +4 more |
| 79134 | 407 (127..533) | 306 | 68 | 42 (98), 104 (31), 88 (30), 44 (29), 80 (24), 65 (21), 175 (19), 52 (11), 177 (9), 67 (8), 63 (7), 50 (7), +4 more |
| 79135 | 409 (129..542) | 290 | 85 | 67 (85), 44 (61), 88 (49), 42 (35), 96 (12), 63 (11), 59 (10), 77 (9), 50 (7), 104 (6), 175 (4), 52 (1) |
| 79139 | 406 (132..537) | 278 | 94 | 67 (75), 42 (74), 177 (31), 88 (27), 50 (25), 52 (21), 77 (8), 63 (7), 59 (7), 96 (3) |
| 79136 | 393 (136..538) | 264 | 82 | 50 (78), 67 (64), 52 (47), 42 (31), 63 (21), 88 (13), 177 (9), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 38/300/1006; tracks with internal gaps: 16; total internal gaps: 40; longest internal gap: 3; tracks ending in coasting: 8 (trailing rows total 18)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 706 | 692 | 14 | 14 | 1 | 0 | 78911, 79136 |
| 31 | 80..477 | 398 | 304 | 303 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 36 | 87..461 | 375 | 311 | 311 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 40 | 89..492 | 404 | 314 | 309 | 5 | 5 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 91..527 | 437 | 365 | 361 | 4 | 2 | 3 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 91..156 | 66 | 45 | 43 | 2 | 0 | 0 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79116, 79122 |
| 44 | 92..527 | 436 | 364 | 364 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 50 | 96..370 | 275 | 212 | 209 | 3 | 1 | 1 | 2 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 100..537 | 438 | 366 | 365 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 105..247 | 143 | 96 | 91 | 5 | 0 | 0 | 5 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 61 | 109..241 | 133 | 78 | 73 | 5 | 0 | 0 | 5 | 78897, 78969, 78971, 79037, 79045 |
| 63 | 110..356 | 247 | 201 | 197 | 4 | 3 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 110..515 | 406 | 334 | 334 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 115..465 | 351 | 281 | 279 | 2 | 1 | 1 | 1 | 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 115..496 | 382 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 67 | 115..542 | 428 | 326 | 325 | 1 | 1 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 128..165 | 38 | 27 | 25 | 2 | 1 | 1 | 1 | 79128, 79132, 79134, 79135, 79139 |
| 80 | 128..415 | 288 | 239 | 236 | 3 | 2 | 1 | 1 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 87 | 135..434 | 300 | 245 | 245 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 88 | 135..530 | 396 | 311 | 310 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 140..455 | 316 | 224 | 223 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103 |
| 96 | 159..529 | 371 | 301 | 299 | 2 | 2 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 104 | 176..445 | 270 | 211 | 208 | 3 | 3 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135 |
| 113 | 192..442 | 251 | 202 | 201 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 126 | 217..480 | 264 | 215 | 215 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 160 | 313..500 | 188 | 155 | 155 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111 |
| 175 | 372..532 | 161 | 124 | 124 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 177 | 372..537 | 166 | 128 | 128 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79136, 79139 |
| 188 | 410..450 | 41 | 31 | 31 | 0 | 0 | 0 | 0 | 78897, 78971, 79045 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 6965; unmatched reference entries: 3177; unmatched candidate entries: 60
- identity switches: 1374; fragmentation (coverage interruptions): 2109; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 43 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 42 -> 31 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 36 -> 44 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 79037: 31 -> 43 at (2118, 3034.5), 3 frames after previous cover
- f93: ref 79045: 43 -> 44 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 36 -> 40 at (2071, 3031), 4 frames after previous cover
- f94: ref 78971: 44 -> 36 at (2090.5, 3032.5), 2 frames after previous cover
- f95: ref 78969: 40 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 42 -> 50 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 36 -> 40 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 42 -> 50 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 31 -> 43 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 50 -> 31 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 43 -> 44 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 42 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 44 -> 31 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 50 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 31 -> 43 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 40 -> 36 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 50 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 42 -> 50 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 42 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 59 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 50 -> 43 at (2082.5, 3028.5), 6 frames after previous cover
- f106: ref 79105: 52 -> 42 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 78897: 59 -> 44 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 43 -> 59 at (2055.5, 3031), 4 frames after previous cover
- f109: ref 78971: 36 -> 61 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 50 -> 43 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 44 -> 31 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 61 -> 36 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 31 -> 61 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 59 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 43 -> 44 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 43 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 50 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 42 -> 63 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 52 -> 42 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 52 -> 64 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 31 -> 59 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 36 -> 61 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 61 -> 31 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 59 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 52 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 59 -> 31 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 59 -> 44 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 31 -> 61 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 59 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 44 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 43 -> 63 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 64 -> 42 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 42 -> 52 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 59 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 63 -> 43 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 63 -> 50 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 52 -> 63 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 52 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 64 -> 42 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 44 -> 66 at (2012.5, 3030), 1 frames after previous cover
- ... 1314 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 691 | 203 | 1 (691) |
| 78896 | 350 (76..429) | 223 | 75 | 91 (104), 40 (42), 87 (40), 36 (37) |
| 78969 | 352 (80..434) | 235 | 79 | 36 (104), 40 (35), 87 (31), 113 (20), 104 (19), 65 (13), 91 (5), 31 (4), 61 (4) |
| 78971 | 352 (84..439) | 245 | 70 | 36 (98), 31 (51), 113 (35), 40 (22), 65 (16), 188 (12), 61 (5), 87 (4), 44 (1), 104 (1) |
| 79045 | 355 (84..443) | 227 | 75 | 113 (62), 31 (42), 61 (35), 36 (29), 104 (19), 40 (14), 188 (12), 44 (5), 65 (5), 43 (2), 87 (2) |
| 79037 | 355 (86..445) | 245 | 73 | 104 (58), 113 (34), 31 (32), 40 (29), 61 (25), 91 (17), 44 (11), 177 (10), 66 (9), 87 (8), 36 (6), 43 (5), +1 more |
| 78897 | 345 (89..450) | 251 | 64 | 31 (47), 113 (40), 91 (30), 40 (30), 87 (20), 66 (19), 36 (17), 104 (16), 188 (7), 64 (5), 59 (4), 61 (4), +5 more |
| 78899 | 365 (91..455) | 241 | 82 | 31 (60), 91 (39), 87 (36), 66 (30), 64 (16), 40 (14), 177 (11), 67 (9), 113 (7), 44 (5), 104 (5), 43 (3), +4 more |
| 79097 | 366 (94..461) | 256 | 82 | 66 (68), 87 (41), 40 (24), 64 (22), 67 (19), 36 (19), 31 (15), 91 (11), 177 (8), 44 (7), 52 (7), 43 (4), +4 more |
| 79098 | 360 (97..467) | 253 | 76 | 66 (79), 40 (45), 31 (27), 87 (20), 52 (13), 67 (12), 44 (11), 177 (10), 59 (8), 91 (7), 65 (6), 64 (5), +4 more |
| 79102 | 371 (98..477) | 251 | 80 | 64 (36), 65 (31), 40 (27), 126 (26), 66 (22), 63 (17), 87 (17), 31 (16), 52 (11), 91 (9), 42 (8), 177 (8), +5 more |
| 79103 | 380 (99..481) | 260 | 83 | 66 (47), 63 (35), 65 (30), 126 (29), 52 (24), 64 (16), 44 (13), 42 (11), 40 (11), 87 (9), 31 (9), 67 (7), +6 more |
| 79105 | 379 (101..484) | 264 | 77 | 126 (45), 65 (38), 63 (32), 64 (32), 160 (21), 87 (15), 66 (14), 59 (10), 96 (9), 52 (8), 40 (8), 80 (7), +7 more |
| 79108 | 385 (104..492) | 286 | 70 | 160 (72), 126 (50), 52 (27), 96 (25), 80 (19), 63 (12), 104 (12), 59 (11), 66 (11), 42 (10), 88 (10), 40 (8), +6 more |
| 79110 | 388 (106..497) | 265 | 81 | 64 (47), 160 (44), 52 (35), 88 (25), 44 (17), 80 (17), 63 (14), 126 (11), 50 (10), 66 (10), 96 (9), 104 (8), +6 more |
| 79111 | 386 (109..500) | 258 | 83 | 64 (55), 52 (42), 44 (33), 80 (24), 50 (17), 160 (17), 88 (16), 96 (15), 63 (8), 42 (7), 126 (7), 65 (7), +3 more |
| 79115 | 421 (111..531) | 294 | 85 | 175 (45), 52 (38), 80 (35), 44 (32), 96 (25), 65 (23), 88 (21), 50 (19), 64 (17), 126 (16), 177 (7), 42 (5), +4 more |
| 79116 | 411 (114..530) | 286 | 84 | 96 (73), 44 (46), 80 (33), 88 (25), 52 (21), 64 (16), 59 (12), 175 (12), 126 (10), 177 (10), 63 (7), 50 (7), +4 more |
| 79122 | 404 (118..532) | 275 | 87 | 96 (88), 52 (30), 88 (30), 65 (23), 64 (17), 80 (17), 175 (14), 63 (10), 59 (9), 44 (9), 50 (8), 42 (7), +4 more |
| 79132 | 391 (120..515) | 266 | 77 | 64 (43), 80 (38), 44 (36), 65 (29), 96 (20), 42 (17), 88 (15), 52 (15), 67 (13), 104 (11), 126 (11), 175 (8), +4 more |
| 79128 | 402 (124..527) | 255 | 94 | 88 (47), 44 (35), 42 (34), 65 (26), 80 (22), 175 (22), 52 (14), 104 (12), 67 (11), 96 (10), 63 (7), 50 (5), +4 more |
| 79134 | 407 (127..533) | 306 | 68 | 42 (98), 104 (31), 88 (30), 44 (29), 80 (24), 65 (21), 175 (19), 52 (11), 177 (9), 67 (8), 63 (7), 50 (7), +4 more |
| 79135 | 409 (129..542) | 290 | 85 | 67 (85), 44 (61), 88 (49), 42 (35), 96 (12), 63 (11), 59 (10), 77 (9), 50 (7), 104 (6), 175 (4), 52 (1) |
| 79139 | 406 (132..537) | 278 | 94 | 67 (75), 42 (74), 177 (31), 88 (27), 50 (25), 52 (21), 77 (8), 63 (7), 59 (7), 96 (3) |
| 79136 | 393 (136..538) | 264 | 82 | 50 (78), 67 (64), 52 (47), 42 (31), 63 (21), 88 (13), 177 (9), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 38/300/1006; tracks with internal gaps: 16; total internal gaps: 40; longest internal gap: 3; tracks ending in coasting: 8 (trailing rows total 18)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 706 | 692 | 14 | 14 | 1 | 0 | 78911, 79136 |
| 31 | 80..477 | 398 | 304 | 303 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 36 | 87..461 | 375 | 311 | 311 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 40 | 89..492 | 404 | 314 | 309 | 5 | 5 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 91..527 | 437 | 365 | 361 | 4 | 2 | 3 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 91..156 | 66 | 45 | 43 | 2 | 0 | 0 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79116, 79122 |
| 44 | 92..527 | 436 | 364 | 364 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 50 | 96..370 | 275 | 212 | 209 | 3 | 1 | 1 | 2 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 100..537 | 438 | 366 | 365 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 105..247 | 143 | 96 | 91 | 5 | 0 | 0 | 5 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 61 | 109..241 | 133 | 78 | 73 | 5 | 0 | 0 | 5 | 78897, 78969, 78971, 79037, 79045 |
| 63 | 110..356 | 247 | 201 | 197 | 4 | 3 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 110..515 | 406 | 334 | 334 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 115..465 | 351 | 281 | 279 | 2 | 1 | 1 | 1 | 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 115..496 | 382 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 67 | 115..542 | 428 | 326 | 325 | 1 | 1 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 128..165 | 38 | 27 | 25 | 2 | 1 | 1 | 1 | 79128, 79132, 79134, 79135, 79139 |
| 80 | 128..415 | 288 | 239 | 236 | 3 | 2 | 1 | 1 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 87 | 135..434 | 300 | 245 | 245 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 88 | 135..530 | 396 | 311 | 310 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 140..455 | 316 | 224 | 223 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103 |
| 96 | 159..529 | 371 | 301 | 299 | 2 | 2 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 104 | 176..445 | 270 | 211 | 208 | 3 | 3 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135 |
| 113 | 192..442 | 251 | 202 | 201 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 126 | 217..480 | 264 | 215 | 215 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 160 | 313..500 | 188 | 155 | 155 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111 |
| 175 | 372..532 | 161 | 124 | 124 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 177 | 372..537 | 166 | 128 | 128 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79136, 79139 |
| 188 | 410..450 | 41 | 31 | 31 | 0 | 0 | 0 | 0 | 78897, 78971, 79045 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 8231; unmatched reference entries: 1911; unmatched candidate entries: 1556
- identity switches: 1380; fragmentation (coverage interruptions): 1258; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 43 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 42 -> 31 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 36 -> 44 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 78971: 44 -> 36 at (2095, 3033.5), 1 frames after previous cover
- f93: ref 79037: 31 -> 43 at (2118, 3034.5), 2 frames after previous cover
- f93: ref 79045: 43 -> 44 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 36 -> 40 at (2071, 3031), 4 frames after previous cover
- f95: ref 78969: 40 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 42 -> 50 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 36 -> 40 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 42 -> 50 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 31 -> 43 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 50 -> 31 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 43 -> 44 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 42 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 44 -> 31 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 50 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 31 -> 43 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 40 -> 36 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 50 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 42 -> 50 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 42 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 59 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 50 -> 43 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 59 -> 44 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 43 -> 59 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79105: 52 -> 42 at (2113.5, 3025), 4 frames after previous cover
- f109: ref 78971: 36 -> 61 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 50 -> 43 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 44 -> 31 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 61 -> 36 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 31 -> 61 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 59 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 43 -> 44 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 43 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 50 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 42 -> 63 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 52 -> 42 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 52 -> 64 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 31 -> 59 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 36 -> 61 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 61 -> 31 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 59 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 52 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 59 -> 31 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 59 -> 44 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 31 -> 61 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 59 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 44 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 43 -> 63 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 64 -> 42 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 42 -> 52 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 59 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 63 -> 43 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 63 -> 50 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 52 -> 63 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 52 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 64 -> 42 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 44 -> 66 at (2012.5, 3030), 1 frames after previous cover
- ... 1320 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 931 | 52 | 1 (931) |
| 78896 | 350 (76..429) | 271 | 40 | 91 (130), 40 (50), 87 (48), 36 (43) |
| 78969 | 352 (80..434) | 278 | 50 | 36 (124), 40 (37), 87 (37), 104 (25), 113 (22), 65 (16), 91 (7), 31 (5), 61 (5) |
| 78971 | 352 (84..439) | 280 | 41 | 36 (107), 31 (62), 113 (40), 40 (26), 65 (18), 188 (15), 61 (5), 87 (4), 104 (2), 44 (1) |
| 79045 | 355 (84..443) | 266 | 51 | 113 (74), 31 (51), 61 (42), 36 (32), 104 (22), 40 (16), 188 (13), 65 (6), 44 (5), 87 (3), 43 (2) |
| 79037 | 355 (86..445) | 282 | 48 | 104 (68), 31 (40), 113 (40), 40 (31), 61 (29), 91 (20), 177 (12), 44 (11), 66 (10), 87 (9), 36 (6), 43 (5), +1 more |
| 78897 | 345 (89..450) | 278 | 45 | 31 (52), 113 (49), 91 (34), 40 (31), 66 (22), 87 (22), 36 (19), 104 (18), 64 (5), 188 (5), 43 (4), 59 (4), +5 more |
| 78899 | 365 (91..455) | 284 | 54 | 31 (69), 91 (51), 87 (41), 66 (34), 64 (20), 40 (19), 177 (13), 67 (9), 113 (8), 44 (5), 104 (5), 43 (4), +4 more |
| 79097 | 366 (94..461) | 294 | 52 | 66 (77), 87 (44), 64 (28), 40 (26), 67 (23), 36 (23), 31 (17), 91 (15), 177 (9), 44 (8), 52 (8), 43 (4), +4 more |
| 79098 | 360 (97..467) | 290 | 50 | 66 (95), 40 (53), 31 (31), 87 (22), 67 (14), 52 (13), 177 (13), 44 (11), 59 (8), 91 (7), 65 (7), 64 (5), +5 more |
| 79102 | 371 (98..477) | 294 | 51 | 64 (44), 40 (36), 65 (35), 126 (31), 66 (25), 63 (19), 31 (19), 87 (17), 52 (12), 91 (10), 177 (10), 42 (8), +5 more |
| 79103 | 380 (99..481) | 309 | 48 | 66 (56), 63 (39), 65 (35), 126 (35), 52 (28), 40 (17), 64 (16), 44 (15), 42 (14), 87 (10), 31 (10), 67 (9), +6 more |
| 79105 | 379 (101..484) | 309 | 47 | 126 (56), 65 (45), 64 (40), 63 (36), 160 (25), 66 (18), 87 (16), 59 (10), 40 (10), 52 (9), 96 (9), 80 (7), +7 more |
| 79108 | 385 (104..492) | 317 | 48 | 160 (80), 126 (57), 52 (28), 96 (26), 80 (22), 63 (14), 104 (14), 66 (14), 59 (12), 42 (11), 88 (10), 40 (9), +5 more |
| 79110 | 388 (106..497) | 300 | 61 | 160 (55), 64 (49), 52 (37), 88 (28), 44 (19), 80 (19), 63 (18), 126 (14), 66 (12), 50 (10), 96 (10), 104 (8), +6 more |
| 79111 | 386 (109..500) | 290 | 69 | 64 (65), 52 (46), 44 (36), 80 (28), 160 (22), 88 (18), 50 (17), 96 (15), 63 (9), 42 (7), 126 (7), 65 (7), +4 more |
| 79115 | 421 (111..531) | 347 | 54 | 175 (66), 44 (43), 52 (42), 80 (42), 65 (31), 96 (25), 50 (22), 126 (21), 64 (18), 88 (14), 177 (8), 42 (5), +4 more |
| 79116 | 411 (114..530) | 325 | 57 | 96 (89), 44 (47), 80 (34), 88 (28), 52 (27), 64 (17), 175 (16), 59 (14), 177 (13), 63 (8), 50 (8), 126 (8), +4 more |
| 79122 | 404 (118..532) | 320 | 60 | 96 (110), 88 (46), 52 (39), 65 (27), 80 (18), 64 (17), 63 (12), 44 (10), 59 (9), 50 (8), 126 (8), 42 (7), +4 more |
| 79132 | 391 (120..515) | 302 | 52 | 64 (50), 80 (44), 44 (41), 65 (35), 96 (22), 42 (17), 52 (17), 88 (16), 104 (14), 67 (13), 126 (13), 175 (9), +4 more |
| 79128 | 402 (124..527) | 304 | 61 | 88 (57), 44 (42), 42 (39), 65 (34), 175 (30), 80 (27), 52 (14), 104 (13), 67 (13), 96 (11), 63 (8), 50 (6), +4 more |
| 79134 | 407 (127..533) | 344 | 41 | 42 (107), 88 (37), 104 (34), 44 (30), 80 (30), 65 (24), 175 (20), 177 (14), 67 (9), 52 (9), 96 (8), 50 (7), +5 more |
| 79135 | 409 (129..542) | 350 | 44 | 67 (107), 44 (70), 88 (62), 42 (40), 96 (14), 63 (13), 59 (12), 77 (9), 104 (9), 50 (7), 175 (6), 52 (1) |
| 79139 | 406 (132..537) | 342 | 44 | 42 (91), 67 (91), 52 (69), 88 (31), 50 (29), 77 (10), 59 (10), 63 (8), 96 (3) |
| 79136 | 393 (136..538) | 324 | 38 | 50 (95), 67 (82), 42 (47), 177 (41), 63 (28), 88 (16), 52 (14), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 67/329/1006; tracks with internal gaps: 29; total internal gaps: 450; longest internal gap: 16; tracks ending in coasting: 28 (trailing rows total 902)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 1006 | 932 | 74 | 51 | 5 | 0 | 78911, 79136 |
| 31 | 80..506 | 427 | 427 | 356 | 71 | 23 | 9 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 36 | 87..490 | 404 | 404 | 356 | 48 | 18 | 5 | 23 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 40 | 89..521 | 433 | 433 | 361 | 72 | 28 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 91..556 | 466 | 466 | 417 | 49 | 19 | 3 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 91..185 | 95 | 95 | 51 | 44 | 1 | 1 | 43 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79116, 79122 |
| 44 | 92..556 | 465 | 465 | 408 | 57 | 19 | 6 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 50 | 96..399 | 304 | 304 | 240 | 64 | 15 | 3 | 44 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 100..566 | 467 | 467 | 413 | 54 | 19 | 4 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 105..276 | 172 | 172 | 101 | 71 | 2 | 1 | 69 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 61 | 109..270 | 162 | 162 | 85 | 77 | 2 | 2 | 73 | 78897, 78969, 78971, 79037, 79045 |
| 63 | 110..385 | 276 | 276 | 226 | 50 | 17 | 2 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 110..544 | 435 | 435 | 384 | 51 | 17 | 16 | 11 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 65 | 115..494 | 380 | 380 | 332 | 48 | 15 | 3 | 30 | 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 115..525 | 411 | 411 | 363 | 48 | 15 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 67 | 115..571 | 457 | 457 | 394 | 63 | 23 | 5 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 128..194 | 67 | 67 | 29 | 38 | 1 | 2 | 36 | 79128, 79132, 79134, 79135, 79139 |
| 80 | 128..444 | 317 | 317 | 271 | 46 | 12 | 3 | 30 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 87 | 135..463 | 329 | 329 | 275 | 54 | 19 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 88 | 135..559 | 425 | 425 | 367 | 58 | 19 | 8 | 27 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 140..484 | 345 | 345 | 276 | 69 | 27 | 6 | 29 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103 |
| 96 | 159..558 | 400 | 400 | 348 | 52 | 18 | 3 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 104 | 176..474 | 299 | 299 | 242 | 57 | 15 | 6 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135 |
| 113 | 192..471 | 280 | 280 | 236 | 44 | 17 | 4 | 21 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 126 | 217..509 | 293 | 293 | 253 | 40 | 10 | 2 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 160 | 313..529 | 217 | 217 | 183 | 34 | 5 | 1 | 29 | 79103, 79105, 79108, 79110, 79111 |
| 175 | 372..561 | 190 | 190 | 150 | 40 | 9 | 2 | 30 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 177 | 372..566 | 195 | 195 | 149 | 46 | 11 | 3 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79128, 79134, 79136 |
| 188 | 410..479 | 70 | 70 | 33 | 37 | 3 | 1 | 34 | 78897, 78971, 79045 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 8231; unmatched reference entries: 1911; unmatched candidate entries: 1556
- identity switches: 1380; fragmentation (coverage interruptions): 1258; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 31 -> 36 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 31 -> 43 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 42 -> 31 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 36 -> 44 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 78971: 44 -> 36 at (2095, 3033.5), 1 frames after previous cover
- f93: ref 79037: 31 -> 43 at (2118, 3034.5), 2 frames after previous cover
- f93: ref 79045: 43 -> 44 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 36 -> 40 at (2071, 3031), 4 frames after previous cover
- f95: ref 78969: 40 -> 36 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 42 -> 50 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 36 -> 40 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 42 -> 50 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 31 -> 43 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 50 -> 31 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 43 -> 44 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 42 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 44 -> 31 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 50 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 31 -> 43 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 40 -> 36 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 50 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 42 -> 50 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 42 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 43 -> 59 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 50 -> 43 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 59 -> 44 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 43 -> 59 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79105: 52 -> 42 at (2113.5, 3025), 4 frames after previous cover
- f109: ref 78971: 36 -> 61 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 50 -> 43 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 44 -> 31 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 61 -> 36 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 31 -> 61 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 43 -> 59 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 43 -> 44 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 50 -> 43 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 42 -> 50 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 42 -> 63 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 52 -> 42 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 52 -> 64 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 31 -> 59 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 36 -> 61 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 61 -> 31 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 59 -> 43 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 52 -> 64 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 59 -> 31 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 59 -> 44 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 31 -> 61 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 43 -> 59 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 44 -> 43 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 43 -> 63 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 64 -> 42 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 42 -> 52 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 43 -> 59 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 63 -> 43 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 63 -> 50 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 52 -> 63 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 52 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 64 -> 42 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 44 -> 66 at (2012.5, 3030), 1 frames after previous cover
- ... 1320 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 931 | 52 | 1 (931) |
| 78896 | 350 (76..429) | 271 | 40 | 91 (130), 40 (50), 87 (48), 36 (43) |
| 78969 | 352 (80..434) | 278 | 50 | 36 (124), 40 (37), 87 (37), 104 (25), 113 (22), 65 (16), 91 (7), 31 (5), 61 (5) |
| 78971 | 352 (84..439) | 280 | 41 | 36 (107), 31 (62), 113 (40), 40 (26), 65 (18), 188 (15), 61 (5), 87 (4), 104 (2), 44 (1) |
| 79045 | 355 (84..443) | 266 | 51 | 113 (74), 31 (51), 61 (42), 36 (32), 104 (22), 40 (16), 188 (13), 65 (6), 44 (5), 87 (3), 43 (2) |
| 79037 | 355 (86..445) | 282 | 48 | 104 (68), 31 (40), 113 (40), 40 (31), 61 (29), 91 (20), 177 (12), 44 (11), 66 (10), 87 (9), 36 (6), 43 (5), +1 more |
| 78897 | 345 (89..450) | 278 | 45 | 31 (52), 113 (49), 91 (34), 40 (31), 66 (22), 87 (22), 36 (19), 104 (18), 64 (5), 188 (5), 43 (4), 59 (4), +5 more |
| 78899 | 365 (91..455) | 284 | 54 | 31 (69), 91 (51), 87 (41), 66 (34), 64 (20), 40 (19), 177 (13), 67 (9), 113 (8), 44 (5), 104 (5), 43 (4), +4 more |
| 79097 | 366 (94..461) | 294 | 52 | 66 (77), 87 (44), 64 (28), 40 (26), 67 (23), 36 (23), 31 (17), 91 (15), 177 (9), 44 (8), 52 (8), 43 (4), +4 more |
| 79098 | 360 (97..467) | 290 | 50 | 66 (95), 40 (53), 31 (31), 87 (22), 67 (14), 52 (13), 177 (13), 44 (11), 59 (8), 91 (7), 65 (7), 64 (5), +5 more |
| 79102 | 371 (98..477) | 294 | 51 | 64 (44), 40 (36), 65 (35), 126 (31), 66 (25), 63 (19), 31 (19), 87 (17), 52 (12), 91 (10), 177 (10), 42 (8), +5 more |
| 79103 | 380 (99..481) | 309 | 48 | 66 (56), 63 (39), 65 (35), 126 (35), 52 (28), 40 (17), 64 (16), 44 (15), 42 (14), 87 (10), 31 (10), 67 (9), +6 more |
| 79105 | 379 (101..484) | 309 | 47 | 126 (56), 65 (45), 64 (40), 63 (36), 160 (25), 66 (18), 87 (16), 59 (10), 40 (10), 52 (9), 96 (9), 80 (7), +7 more |
| 79108 | 385 (104..492) | 317 | 48 | 160 (80), 126 (57), 52 (28), 96 (26), 80 (22), 63 (14), 104 (14), 66 (14), 59 (12), 42 (11), 88 (10), 40 (9), +5 more |
| 79110 | 388 (106..497) | 300 | 61 | 160 (55), 64 (49), 52 (37), 88 (28), 44 (19), 80 (19), 63 (18), 126 (14), 66 (12), 50 (10), 96 (10), 104 (8), +6 more |
| 79111 | 386 (109..500) | 290 | 69 | 64 (65), 52 (46), 44 (36), 80 (28), 160 (22), 88 (18), 50 (17), 96 (15), 63 (9), 42 (7), 126 (7), 65 (7), +4 more |
| 79115 | 421 (111..531) | 347 | 54 | 175 (66), 44 (43), 52 (42), 80 (42), 65 (31), 96 (25), 50 (22), 126 (21), 64 (18), 88 (14), 177 (8), 42 (5), +4 more |
| 79116 | 411 (114..530) | 325 | 57 | 96 (89), 44 (47), 80 (34), 88 (28), 52 (27), 64 (17), 175 (16), 59 (14), 177 (13), 63 (8), 50 (8), 126 (8), +4 more |
| 79122 | 404 (118..532) | 320 | 60 | 96 (110), 88 (46), 52 (39), 65 (27), 80 (18), 64 (17), 63 (12), 44 (10), 59 (9), 50 (8), 126 (8), 42 (7), +4 more |
| 79132 | 391 (120..515) | 302 | 52 | 64 (50), 80 (44), 44 (41), 65 (35), 96 (22), 42 (17), 52 (17), 88 (16), 104 (14), 67 (13), 126 (13), 175 (9), +4 more |
| 79128 | 402 (124..527) | 304 | 61 | 88 (57), 44 (42), 42 (39), 65 (34), 175 (30), 80 (27), 52 (14), 104 (13), 67 (13), 96 (11), 63 (8), 50 (6), +4 more |
| 79134 | 407 (127..533) | 344 | 41 | 42 (107), 88 (37), 104 (34), 44 (30), 80 (30), 65 (24), 175 (20), 177 (14), 67 (9), 52 (9), 96 (8), 50 (7), +5 more |
| 79135 | 409 (129..542) | 350 | 44 | 67 (107), 44 (70), 88 (62), 42 (40), 96 (14), 63 (13), 59 (12), 77 (9), 104 (9), 50 (7), 175 (6), 52 (1) |
| 79139 | 406 (132..537) | 342 | 44 | 42 (91), 67 (91), 52 (69), 88 (31), 50 (29), 77 (10), 59 (10), 63 (8), 96 (3) |
| 79136 | 393 (136..538) | 324 | 38 | 50 (95), 67 (82), 42 (47), 177 (41), 63 (28), 88 (16), 52 (14), 1 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 67/329/1006; tracks with internal gaps: 29; total internal gaps: 450; longest internal gap: 16; tracks ending in coasting: 28 (trailing rows total 902)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3..1008 | 1006 | 1006 | 932 | 74 | 51 | 5 | 0 | 78911, 79136 |
| 31 | 80..506 | 427 | 427 | 356 | 71 | 23 | 9 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 36 | 87..490 | 404 | 404 | 356 | 48 | 18 | 5 | 23 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 40 | 89..521 | 433 | 433 | 361 | 72 | 28 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 91..556 | 466 | 466 | 417 | 49 | 19 | 3 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 91..185 | 95 | 95 | 51 | 44 | 1 | 1 | 43 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79116, 79122 |
| 44 | 92..556 | 465 | 465 | 408 | 57 | 19 | 6 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 50 | 96..399 | 304 | 304 | 240 | 64 | 15 | 3 | 44 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 100..566 | 467 | 467 | 413 | 54 | 19 | 4 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 105..276 | 172 | 172 | 101 | 71 | 2 | 1 | 69 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 61 | 109..270 | 162 | 162 | 85 | 77 | 2 | 2 | 73 | 78897, 78969, 78971, 79037, 79045 |
| 63 | 110..385 | 276 | 276 | 226 | 50 | 17 | 2 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 110..544 | 435 | 435 | 384 | 51 | 17 | 16 | 11 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 65 | 115..494 | 380 | 380 | 332 | 48 | 15 | 3 | 30 | 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 115..525 | 411 | 411 | 363 | 48 | 15 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 67 | 115..571 | 457 | 457 | 394 | 63 | 23 | 5 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 128..194 | 67 | 67 | 29 | 38 | 1 | 2 | 36 | 79128, 79132, 79134, 79135, 79139 |
| 80 | 128..444 | 317 | 317 | 271 | 46 | 12 | 3 | 30 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 87 | 135..463 | 329 | 329 | 275 | 54 | 19 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 88 | 135..559 | 425 | 425 | 367 | 58 | 19 | 8 | 27 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 140..484 | 345 | 345 | 276 | 69 | 27 | 6 | 29 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103 |
| 96 | 159..558 | 400 | 400 | 348 | 52 | 18 | 3 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 104 | 176..474 | 299 | 299 | 242 | 57 | 15 | 6 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135 |
| 113 | 192..471 | 280 | 280 | 236 | 44 | 17 | 4 | 21 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 126 | 217..509 | 293 | 293 | 253 | 40 | 10 | 2 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 160 | 313..529 | 217 | 217 | 183 | 34 | 5 | 1 | 29 | 79103, 79105, 79108, 79110, 79111 |
| 175 | 372..561 | 190 | 190 | 150 | 40 | 9 | 2 | 30 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 177 | 372..566 | 195 | 195 | 149 | 46 | 11 | 3 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79128, 79134, 79136 |
| 188 | 410..479 | 70 | 70 | 33 | 37 | 3 | 1 | 34 | 78897, 78971, 79045 |
