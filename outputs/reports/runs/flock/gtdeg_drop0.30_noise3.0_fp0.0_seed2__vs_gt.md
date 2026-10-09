# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=708cc942b1e6
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise3.0_fp0.0_seed2/tracks.csv sha256=92f95e24f2602d21
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise3.0_fp0.0_seed2.csv sha256=708cc942b1e6a3ee
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise3.0_fp0.0_seed2
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
| observations | none | 4 | 0.174 | 0.096 | 0.047 | 2.40 | 0.224 | 670 | 2394.0 |
| observations | none | 6 | 0.240 | 0.131 | 0.419 | 3.21 | 0.337 | 871 | 2374.0 |
| observations | none | 8 | 0.275 | 0.153 | 0.555 | 3.61 | 0.379 | 912 | 2134.0 |
| observations | none | 12 | 0.313 | 0.182 | 0.599 | 3.94 | 0.410 | 807 | 2003.0 |
| observations | ignore | 4 | 0.174 | 0.096 | 0.047 | 2.40 | 0.224 | 670 | 2394.0 |
| observations | ignore | 6 | 0.240 | 0.131 | 0.419 | 3.21 | 0.337 | 871 | 2374.0 |
| observations | ignore | 8 | 0.275 | 0.153 | 0.555 | 3.61 | 0.379 | 912 | 2134.0 |
| observations | ignore | 12 | 0.313 | 0.182 | 0.599 | 3.94 | 0.410 | 807 | 2003.0 |
| updates | none | 4 | 0.174 | 0.100 | -0.175 | 2.43 | 0.215 | 806 | 2468.0 |
| updates | none | 6 | 0.258 | 0.148 | 0.282 | 3.30 | 0.337 | 1005 | 2028.0 |
| updates | none | 8 | 0.310 | 0.181 | 0.511 | 3.85 | 0.401 | 989 | 1378.0 |
| updates | none | 12 | 0.370 | 0.224 | 0.675 | 4.55 | 0.465 | 805 | 866.0 |
| updates | ignore | 4 | 0.174 | 0.100 | -0.175 | 2.43 | 0.215 | 806 | 2468.0 |
| updates | ignore | 6 | 0.258 | 0.148 | 0.282 | 3.30 | 0.337 | 1005 | 2028.0 |
| updates | ignore | 8 | 0.310 | 0.181 | 0.511 | 3.85 | 0.401 | 989 | 1378.0 |
| updates | ignore | 12 | 0.370 | 0.224 | 0.675 | 4.55 | 0.465 | 805 | 866.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 6765; unmatched reference entries: 3377; unmatched candidate entries: 224
- identity switches: 912; fragmentation (coverage interruptions): 2185; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 3 -> 9 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 9 -> 10 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 3 -> 9 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 7 -> 6 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 3 -> 10 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 6 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 9 -> 10 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 10 -> 12 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 10 -> 6 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 3 -> 9 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 10 -> 6 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 9 -> 10 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 6 -> 10 at (2088.5, 3033.5), 2 frames after previous cover
- f100: ref 79097: 9 -> 15 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 3 -> 9 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 12 -> 6 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 6 -> 12 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 9 -> 15 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 6 -> 16 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 9 -> 15 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 3 -> 9 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 10 -> 6 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 6 -> 12 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 78899: 10 -> 6 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 12 -> 7 at (2023.5, 3033.5), 3 frames after previous cover
- f106: ref 79097: 15 -> 10 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 6 -> 12 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 15 -> 10 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79105: 3 -> 9 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 78969: 7 -> 21 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 7 -> 20 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 15 -> 10 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 9 -> 15 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 12 -> 20 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 7 -> 21 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 20 -> 7 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 6 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 10 -> 12 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 9 -> 23 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 3 -> 9 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 3 -> 22 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 20 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 21 -> 7 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 7 -> 20 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 6 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 3 -> 22 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 6 -> 20 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 12 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 20 -> 7 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 10 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 12 -> 10 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 22 -> 9 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 9 -> 3 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 10 -> 6 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 23 -> 15 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 3 -> 23 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 9 -> 3 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 22 -> 9 at (2126, 3027), 1 frames after previous cover
- ... 852 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 667 | 207 | 1 (667) |
| 78896 | 350 (76..429) | 219 | 77 | 21 (187), 16 (25), 6 (7) |
| 78969 | 352 (80..434) | 225 | 79 | 16 (118), 24 (59), 21 (33), 7 (8), 3 (3), 20 (3), 6 (1) |
| 78971 | 352 (84..439) | 237 | 74 | 20 (140), 16 (36), 24 (34), 7 (12), 21 (5), 26 (5), 32 (4), 30 (1) |
| 79045 | 355 (84..443) | 223 | 80 | 32 (111), 20 (36), 24 (26), 16 (16), 30 (11), 26 (6), 7 (5), 3 (3), 6 (3), 12 (3), 10 (2), 9 (1) |
| 79037 | 355 (86..445) | 237 | 78 | 24 (68), 32 (45), 30 (43), 20 (31), 16 (20), 26 (10), 12 (8), 6 (4), 7 (4), 3 (2), 10 (2) |
| 78897 | 345 (89..450) | 245 | 68 | 30 (112), 24 (36), 26 (27), 20 (25), 16 (19), 32 (10), 10 (4), 6 (4), 3 (2), 9 (2), 12 (2), 7 (2) |
| 78899 | 365 (91..455) | 233 | 86 | 26 (124), 24 (32), 32 (29), 30 (25), 10 (5), 12 (5), 20 (4), 9 (3), 6 (3), 3 (2), 7 (1) |
| 79097 | 366 (94..461) | 241 | 87 | 7 (100), 26 (69), 30 (31), 12 (14), 32 (9), 27 (8), 10 (3), 6 (3), 3 (2), 9 (1), 15 (1) |
| 79098 | 360 (97..467) | 242 | 82 | 27 (76), 12 (74), 7 (44), 15 (20), 30 (13), 32 (6), 10 (3), 6 (3), 3 (2), 9 (1) |
| 79102 | 371 (98..477) | 245 | 78 | 27 (90), 9 (53), 7 (48), 15 (28), 12 (17), 6 (5), 10 (3), 32 (1) |
| 79103 | 380 (99..481) | 253 | 87 | 12 (71), 7 (64), 27 (38), 15 (37), 9 (35), 3 (4), 33 (2), 10 (1), 6 (1) |
| 79105 | 379 (101..484) | 259 | 78 | 15 (70), 27 (56), 12 (45), 6 (33), 9 (22), 7 (14), 33 (13), 23 (3), 3 (2), 10 (1) |
| 79108 | 385 (104..492) | 280 | 75 | 15 (122), 6 (58), 9 (48), 12 (21), 33 (19), 3 (5), 23 (4), 10 (3) |
| 79110 | 388 (106..497) | 257 | 80 | 6 (82), 23 (54), 33 (29), 9 (25), 10 (16), 3 (11), 12 (11), 35 (10), 15 (9), 38 (9), 22 (1) |
| 79111 | 386 (109..500) | 252 | 81 | 23 (68), 6 (59), 3 (30), 10 (25), 35 (19), 12 (14), 38 (14), 9 (12), 15 (6), 33 (3), 22 (2) |
| 79115 | 421 (111..531) | 281 | 88 | 10 (135), 3 (52), 38 (25), 6 (20), 9 (18), 23 (14), 35 (13), 15 (2), 33 (2) |
| 79116 | 411 (114..530) | 277 | 86 | 33 (115), 10 (50), 3 (46), 38 (23), 9 (20), 35 (9), 6 (7), 22 (3), 23 (2), 40 (2) |
| 79122 | 404 (118..532) | 268 | 91 | 3 (119), 10 (45), 38 (31), 33 (24), 9 (23), 22 (11), 35 (11), 23 (4) |
| 79132 | 391 (120..515) | 256 | 80 | 40 (76), 38 (55), 35 (35), 10 (30), 9 (20), 3 (13), 33 (12), 22 (10), 23 (4), 29 (1) |
| 79128 | 402 (124..527) | 255 | 93 | 38 (63), 22 (54), 40 (32), 3 (29), 35 (23), 33 (16), 23 (15), 9 (15), 31 (5), 29 (3) |
| 79134 | 407 (127..533) | 298 | 73 | 22 (141), 23 (53), 31 (51), 35 (36), 33 (14), 29 (3) |
| 79135 | 409 (129..542) | 284 | 88 | 35 (121), 23 (66), 22 (41), 33 (33), 29 (15), 31 (8) |
| 79139 | 406 (132..537) | 269 | 98 | 29 (137), 31 (118), 22 (10), 35 (3), 33 (1) |
| 79136 | 393 (136..538) | 262 | 91 | 31 (117), 29 (107), 22 (38) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 144/387/1002; tracks with internal gaps: 24; total internal gaps: 216; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 688 | 667 | 21 | 21 | 1 | 0 | 78911 |
| 3 | 80..532 | 453 | 341 | 327 | 14 | 14 | 1 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 87..500 | 414 | 306 | 293 | 13 | 12 | 2 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 87..480 | 394 | 317 | 302 | 15 | 13 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 91..477 | 387 | 304 | 299 | 5 | 5 | 1 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 10 | 92..530 | 439 | 338 | 328 | 10 | 8 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 96..465 | 370 | 294 | 285 | 9 | 9 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 100..492 | 393 | 304 | 295 | 9 | 9 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 102..439 | 338 | 241 | 234 | 7 | 7 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 109..442 | 334 | 247 | 239 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 109..434 | 326 | 228 | 225 | 3 | 3 | 1 | 0 | 78896, 78969, 78971 |
| 22 | 110..527 | 418 | 320 | 311 | 9 | 9 | 1 | 0 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 110..496 | 387 | 295 | 287 | 8 | 8 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 24 | 115..455 | 341 | 263 | 255 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 26 | 115..461 | 347 | 250 | 241 | 9 | 9 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 27 | 124..484 | 361 | 277 | 268 | 9 | 8 | 2 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 29 | 128..537 | 410 | 282 | 266 | 16 | 16 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 30 | 128..450 | 323 | 244 | 236 | 8 | 8 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 31 | 135..537 | 403 | 308 | 299 | 9 | 9 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 32 | 135..445 | 311 | 222 | 215 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 33 | 140..529 | 390 | 292 | 283 | 9 | 8 | 2 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 35 | 176..542 | 367 | 289 | 280 | 9 | 8 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 38 | 217..527 | 311 | 225 | 220 | 5 | 5 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 40 | 372..515 | 144 | 114 | 110 | 4 | 4 | 1 | 0 | 79116, 79128, 79132 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 6765; unmatched reference entries: 3377; unmatched candidate entries: 224
- identity switches: 912; fragmentation (coverage interruptions): 2185; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 3 -> 9 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 9 -> 10 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 3 -> 9 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 7 -> 6 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 3 -> 10 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 6 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 9 -> 10 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 10 -> 12 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 10 -> 6 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 3 -> 9 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 10 -> 6 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 9 -> 10 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 6 -> 10 at (2088.5, 3033.5), 2 frames after previous cover
- f100: ref 79097: 9 -> 15 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 3 -> 9 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 12 -> 6 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 6 -> 12 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 9 -> 15 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 6 -> 16 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 9 -> 15 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 3 -> 9 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 10 -> 6 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 6 -> 12 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 78899: 10 -> 6 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 12 -> 7 at (2023.5, 3033.5), 3 frames after previous cover
- f106: ref 79097: 15 -> 10 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 6 -> 12 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 15 -> 10 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79105: 3 -> 9 at (2113.5, 3025), 5 frames after previous cover
- f109: ref 78969: 7 -> 21 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 7 -> 20 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 15 -> 10 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 9 -> 15 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 12 -> 20 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 7 -> 21 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 20 -> 7 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 6 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 10 -> 12 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 9 -> 23 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 3 -> 9 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 3 -> 22 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 20 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 21 -> 7 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 7 -> 20 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 6 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 3 -> 22 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 6 -> 20 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 12 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 20 -> 7 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 10 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 12 -> 10 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 22 -> 9 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 9 -> 3 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 10 -> 6 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 23 -> 15 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 3 -> 23 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 9 -> 3 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 22 -> 9 at (2126, 3027), 1 frames after previous cover
- ... 852 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 667 | 207 | 1 (667) |
| 78896 | 350 (76..429) | 219 | 77 | 21 (187), 16 (25), 6 (7) |
| 78969 | 352 (80..434) | 225 | 79 | 16 (118), 24 (59), 21 (33), 7 (8), 3 (3), 20 (3), 6 (1) |
| 78971 | 352 (84..439) | 237 | 74 | 20 (140), 16 (36), 24 (34), 7 (12), 21 (5), 26 (5), 32 (4), 30 (1) |
| 79045 | 355 (84..443) | 223 | 80 | 32 (111), 20 (36), 24 (26), 16 (16), 30 (11), 26 (6), 7 (5), 3 (3), 6 (3), 12 (3), 10 (2), 9 (1) |
| 79037 | 355 (86..445) | 237 | 78 | 24 (68), 32 (45), 30 (43), 20 (31), 16 (20), 26 (10), 12 (8), 6 (4), 7 (4), 3 (2), 10 (2) |
| 78897 | 345 (89..450) | 245 | 68 | 30 (112), 24 (36), 26 (27), 20 (25), 16 (19), 32 (10), 10 (4), 6 (4), 3 (2), 9 (2), 12 (2), 7 (2) |
| 78899 | 365 (91..455) | 233 | 86 | 26 (124), 24 (32), 32 (29), 30 (25), 10 (5), 12 (5), 20 (4), 9 (3), 6 (3), 3 (2), 7 (1) |
| 79097 | 366 (94..461) | 241 | 87 | 7 (100), 26 (69), 30 (31), 12 (14), 32 (9), 27 (8), 10 (3), 6 (3), 3 (2), 9 (1), 15 (1) |
| 79098 | 360 (97..467) | 242 | 82 | 27 (76), 12 (74), 7 (44), 15 (20), 30 (13), 32 (6), 10 (3), 6 (3), 3 (2), 9 (1) |
| 79102 | 371 (98..477) | 245 | 78 | 27 (90), 9 (53), 7 (48), 15 (28), 12 (17), 6 (5), 10 (3), 32 (1) |
| 79103 | 380 (99..481) | 253 | 87 | 12 (71), 7 (64), 27 (38), 15 (37), 9 (35), 3 (4), 33 (2), 10 (1), 6 (1) |
| 79105 | 379 (101..484) | 259 | 78 | 15 (70), 27 (56), 12 (45), 6 (33), 9 (22), 7 (14), 33 (13), 23 (3), 3 (2), 10 (1) |
| 79108 | 385 (104..492) | 280 | 75 | 15 (122), 6 (58), 9 (48), 12 (21), 33 (19), 3 (5), 23 (4), 10 (3) |
| 79110 | 388 (106..497) | 257 | 80 | 6 (82), 23 (54), 33 (29), 9 (25), 10 (16), 3 (11), 12 (11), 35 (10), 15 (9), 38 (9), 22 (1) |
| 79111 | 386 (109..500) | 252 | 81 | 23 (68), 6 (59), 3 (30), 10 (25), 35 (19), 12 (14), 38 (14), 9 (12), 15 (6), 33 (3), 22 (2) |
| 79115 | 421 (111..531) | 281 | 88 | 10 (135), 3 (52), 38 (25), 6 (20), 9 (18), 23 (14), 35 (13), 15 (2), 33 (2) |
| 79116 | 411 (114..530) | 277 | 86 | 33 (115), 10 (50), 3 (46), 38 (23), 9 (20), 35 (9), 6 (7), 22 (3), 23 (2), 40 (2) |
| 79122 | 404 (118..532) | 268 | 91 | 3 (119), 10 (45), 38 (31), 33 (24), 9 (23), 22 (11), 35 (11), 23 (4) |
| 79132 | 391 (120..515) | 256 | 80 | 40 (76), 38 (55), 35 (35), 10 (30), 9 (20), 3 (13), 33 (12), 22 (10), 23 (4), 29 (1) |
| 79128 | 402 (124..527) | 255 | 93 | 38 (63), 22 (54), 40 (32), 3 (29), 35 (23), 33 (16), 23 (15), 9 (15), 31 (5), 29 (3) |
| 79134 | 407 (127..533) | 298 | 73 | 22 (141), 23 (53), 31 (51), 35 (36), 33 (14), 29 (3) |
| 79135 | 409 (129..542) | 284 | 88 | 35 (121), 23 (66), 22 (41), 33 (33), 29 (15), 31 (8) |
| 79139 | 406 (132..537) | 269 | 98 | 29 (137), 31 (118), 22 (10), 35 (3), 33 (1) |
| 79136 | 393 (136..538) | 262 | 91 | 31 (117), 29 (107), 22 (38) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 144/387/1002; tracks with internal gaps: 24; total internal gaps: 216; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 688 | 667 | 21 | 21 | 1 | 0 | 78911 |
| 3 | 80..532 | 453 | 341 | 327 | 14 | 14 | 1 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 87..500 | 414 | 306 | 293 | 13 | 12 | 2 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 87..480 | 394 | 317 | 302 | 15 | 13 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 91..477 | 387 | 304 | 299 | 5 | 5 | 1 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 10 | 92..530 | 439 | 338 | 328 | 10 | 8 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 96..465 | 370 | 294 | 285 | 9 | 9 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 100..492 | 393 | 304 | 295 | 9 | 9 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 102..439 | 338 | 241 | 234 | 7 | 7 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 109..442 | 334 | 247 | 239 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 109..434 | 326 | 228 | 225 | 3 | 3 | 1 | 0 | 78896, 78969, 78971 |
| 22 | 110..527 | 418 | 320 | 311 | 9 | 9 | 1 | 0 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 110..496 | 387 | 295 | 287 | 8 | 8 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 24 | 115..455 | 341 | 263 | 255 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 26 | 115..461 | 347 | 250 | 241 | 9 | 9 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 27 | 124..484 | 361 | 277 | 268 | 9 | 8 | 2 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 29 | 128..537 | 410 | 282 | 266 | 16 | 16 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 30 | 128..450 | 323 | 244 | 236 | 8 | 8 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 31 | 135..537 | 403 | 308 | 299 | 9 | 9 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 32 | 135..445 | 311 | 222 | 215 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 33 | 140..529 | 390 | 292 | 283 | 9 | 8 | 2 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 35 | 176..542 | 367 | 289 | 280 | 9 | 8 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 38 | 217..527 | 311 | 225 | 220 | 5 | 5 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 40 | 372..515 | 144 | 114 | 110 | 4 | 4 | 1 | 0 | 79116, 79128, 79132 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8102; unmatched reference entries: 2040; unmatched candidate entries: 1928
- identity switches: 989; fragmentation (coverage interruptions): 1320; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 3 -> 9 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 9 -> 10 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 3 -> 9 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 7 -> 6 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 3 -> 10 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 6 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 9 -> 10 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 10 -> 12 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 10 -> 6 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 3 -> 9 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 10 -> 6 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 9 -> 10 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 6 -> 10 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79097: 9 -> 15 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 3 -> 9 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 12 -> 6 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 6 -> 12 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 9 -> 15 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 6 -> 16 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 9 -> 15 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 3 -> 9 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 10 -> 6 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 6 -> 12 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 15 -> 10 at (2088, 3029), 5 frames after previous cover
- f105: ref 79103: 9 -> 15 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79105: 3 -> 9 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78899: 10 -> 6 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 12 -> 7 at (2023.5, 3033.5), 3 frames after previous cover
- f107: ref 79103: 15 -> 9 at (2110, 3022.5), 2 frames after previous cover
- f108: ref 78897: 6 -> 12 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 15 -> 10 at (2084.5, 3028.5), 6 frames after previous cover
- f109: ref 78969: 7 -> 21 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 7 -> 20 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 15 -> 10 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 9 -> 15 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 12 -> 20 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 7 -> 21 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 20 -> 7 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 6 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 10 -> 12 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 9 -> 23 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 3 -> 9 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 3 -> 22 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 20 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 21 -> 7 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 7 -> 20 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 6 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 3 -> 22 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 6 -> 20 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 12 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 20 -> 7 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 10 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 12 -> 10 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 22 -> 9 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 9 -> 3 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 10 -> 6 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 23 -> 15 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 3 -> 23 at (2097.5, 3025.5), 1 frames after previous cover
- ... 929 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 894 | 65 | 1 (894) |
| 78896 | 350 (76..429) | 258 | 50 | 21 (222), 16 (29), 6 (7) |
| 78969 | 352 (80..434) | 271 | 48 | 16 (149), 24 (66), 21 (40), 7 (8), 20 (4), 3 (3), 6 (1) |
| 78971 | 352 (84..439) | 273 | 49 | 20 (166), 24 (39), 16 (39), 7 (12), 32 (6), 21 (5), 26 (5), 30 (1) |
| 79045 | 355 (84..443) | 264 | 56 | 32 (130), 20 (48), 24 (31), 16 (19), 30 (11), 26 (7), 7 (5), 3 (4), 6 (3), 12 (3), 10 (2), 9 (1) |
| 79037 | 355 (86..445) | 279 | 54 | 24 (77), 32 (61), 30 (48), 20 (37), 16 (25), 26 (11), 12 (8), 6 (4), 7 (4), 3 (2), 10 (2) |
| 78897 | 345 (89..450) | 279 | 47 | 30 (127), 24 (44), 20 (28), 26 (26), 16 (23), 32 (14), 6 (5), 10 (4), 3 (2), 9 (2), 12 (2), 7 (2) |
| 78899 | 365 (91..455) | 274 | 59 | 26 (153), 24 (39), 32 (32), 30 (26), 10 (5), 12 (5), 20 (5), 9 (3), 6 (3), 3 (2), 7 (1) |
| 79097 | 366 (94..461) | 285 | 57 | 7 (113), 26 (87), 30 (36), 12 (16), 32 (10), 27 (10), 10 (4), 3 (3), 6 (3), 9 (1), 15 (1), 24 (1) |
| 79098 | 360 (97..467) | 276 | 60 | 12 (84), 27 (84), 7 (54), 15 (22), 30 (15), 32 (7), 10 (3), 6 (3), 3 (2), 9 (1), 26 (1) |
| 79102 | 371 (98..477) | 280 | 54 | 27 (104), 9 (65), 7 (53), 15 (30), 12 (18), 6 (5), 10 (3), 32 (2) |
| 79103 | 380 (99..481) | 299 | 55 | 7 (80), 12 (78), 27 (46), 9 (44), 15 (43), 3 (4), 33 (2), 10 (1), 6 (1) |
| 79105 | 379 (101..484) | 305 | 50 | 15 (81), 27 (72), 12 (53), 6 (37), 9 (28), 7 (14), 33 (13), 3 (3), 23 (3), 10 (1) |
| 79108 | 385 (104..492) | 317 | 50 | 15 (143), 6 (66), 9 (52), 33 (22), 12 (21), 3 (5), 23 (4), 10 (4) |
| 79110 | 388 (106..497) | 308 | 50 | 6 (100), 23 (67), 33 (35), 9 (30), 10 (17), 3 (12), 15 (12), 12 (12), 38 (12), 35 (10), 22 (1) |
| 79111 | 386 (109..500) | 306 | 52 | 23 (86), 6 (77), 10 (32), 3 (30), 35 (23), 9 (16), 12 (16), 38 (15), 15 (8), 22 (2), 33 (1) |
| 79115 | 421 (111..531) | 329 | 56 | 10 (166), 3 (61), 38 (25), 6 (23), 9 (18), 35 (17), 23 (13), 15 (3), 33 (3) |
| 79116 | 411 (114..530) | 335 | 52 | 33 (142), 3 (54), 10 (52), 38 (34), 9 (23), 6 (13), 35 (8), 22 (4), 40 (3), 23 (2) |
| 79122 | 404 (118..532) | 318 | 56 | 3 (147), 10 (57), 38 (31), 9 (25), 33 (25), 35 (14), 22 (13), 23 (6) |
| 79132 | 391 (120..515) | 303 | 52 | 40 (85), 38 (75), 10 (39), 35 (35), 9 (26), 3 (15), 33 (13), 22 (10), 23 (4), 29 (1) |
| 79128 | 402 (124..527) | 301 | 64 | 38 (75), 22 (62), 40 (42), 3 (38), 35 (23), 9 (18), 33 (18), 23 (17), 31 (5), 29 (3) |
| 79134 | 407 (127..533) | 347 | 43 | 22 (170), 23 (58), 31 (57), 35 (41), 33 (17), 29 (2), 38 (2) |
| 79135 | 409 (129..542) | 340 | 46 | 35 (150), 23 (76), 22 (47), 33 (40), 29 (15), 31 (9), 40 (3) |
| 79139 | 406 (132..537) | 336 | 49 | 31 (163), 29 (157), 22 (12), 33 (2), 10 (2) |
| 79136 | 393 (136..538) | 325 | 46 | 29 (152), 31 (122), 22 (48), 35 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 173/416/1002; tracks with internal gaps: 24; total internal gaps: 908; longest internal gap: 12; tracks ending in coasting: 23 (trailing rows total 620)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 1002 | 894 | 108 | 65 | 5 | 0 | 78911 |
| 3 | 80..561 | 482 | 482 | 387 | 95 | 47 | 6 | 30 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 87..529 | 443 | 443 | 351 | 92 | 45 | 7 | 29 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 87..509 | 423 | 423 | 346 | 77 | 41 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 91..506 | 416 | 416 | 353 | 63 | 25 | 4 | 29 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 10 | 92..559 | 468 | 468 | 394 | 74 | 37 | 3 | 22 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79139 |
| 12 | 96..494 | 399 | 399 | 316 | 83 | 39 | 5 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 100..521 | 422 | 422 | 343 | 79 | 34 | 4 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 102..468 | 367 | 367 | 284 | 83 | 39 | 5 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 109..471 | 363 | 363 | 288 | 75 | 35 | 4 | 28 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 109..463 | 355 | 355 | 267 | 88 | 42 | 4 | 29 | 78896, 78969, 78971 |
| 22 | 110..556 | 447 | 447 | 369 | 78 | 37 | 3 | 28 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 110..525 | 416 | 416 | 336 | 80 | 42 | 5 | 28 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 24 | 115..484 | 370 | 370 | 297 | 73 | 33 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 26 | 115..490 | 376 | 376 | 290 | 86 | 44 | 5 | 23 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 27 | 124..513 | 390 | 390 | 316 | 74 | 39 | 3 | 29 | 79097, 79098, 79102, 79103, 79105 |
| 29 | 128..566 | 439 | 439 | 330 | 109 | 47 | 4 | 31 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 30 | 128..479 | 352 | 352 | 264 | 88 | 35 | 5 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 31 | 135..566 | 432 | 432 | 356 | 76 | 39 | 2 | 28 | 79128, 79134, 79135, 79136, 79139 |
| 32 | 135..474 | 340 | 340 | 262 | 78 | 36 | 3 | 24 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 33 | 140..558 | 419 | 419 | 333 | 86 | 36 | 5 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 35 | 176..571 | 396 | 396 | 324 | 72 | 28 | 6 | 32 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 38 | 217..556 | 340 | 340 | 269 | 71 | 30 | 6 | 23 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 40 | 372..544 | 173 | 173 | 133 | 40 | 13 | 12 | 2 | 79116, 79128, 79132, 79135 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8102; unmatched reference entries: 2040; unmatched candidate entries: 1928
- identity switches: 989; fragmentation (coverage interruptions): 1320; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 3 -> 9 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 79045: 9 -> 10 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78899: 3 -> 9 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 7 -> 6 at (2071, 3031), 4 frames after previous cover
- f94: ref 79037: 3 -> 10 at (2112.5, 3034), 5 frames after previous cover
- f95: ref 78969: 6 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78897: 9 -> 10 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79037: 10 -> 12 at (2099, 3033.5), 1 frames after previous cover
- f96: ref 79045: 10 -> 6 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 79097: 3 -> 9 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 10 -> 6 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 9 -> 10 at (2116.5, 3029), 2 frames after previous cover
- f100: ref 78897: 6 -> 10 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 79097: 9 -> 15 at (2117.5, 3029.5), 3 frames after previous cover
- f100: ref 79098: 3 -> 9 at (2130, 3027), 2 frames after previous cover
- f101: ref 79037: 12 -> 6 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 6 -> 12 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79098: 9 -> 15 at (2124, 3028), 1 frames after previous cover
- f102: ref 78896: 6 -> 16 at (1997.5, 3032.5), 7 frames after previous cover
- f103: ref 79102: 9 -> 15 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 3 -> 9 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 10 -> 6 at (2058, 3033), 3 frames after previous cover
- f105: ref 79037: 6 -> 12 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 15 -> 10 at (2088, 3029), 5 frames after previous cover
- f105: ref 79103: 9 -> 15 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79105: 3 -> 9 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78899: 10 -> 6 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79045: 12 -> 7 at (2023.5, 3033.5), 3 frames after previous cover
- f107: ref 79103: 15 -> 9 at (2110, 3022.5), 2 frames after previous cover
- f108: ref 78897: 6 -> 12 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 15 -> 10 at (2084.5, 3028.5), 6 frames after previous cover
- f109: ref 78969: 7 -> 21 at (1978, 3034.5), 4 frames after previous cover
- f109: ref 79045: 7 -> 20 at (2007, 3034), 3 frames after previous cover
- f109: ref 79102: 15 -> 10 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 9 -> 15 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78897: 12 -> 20 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 7 -> 21 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 20 -> 7 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 6 at (2058.5, 3029.5), 3 frames after previous cover
- f110: ref 79098: 10 -> 12 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79105: 9 -> 23 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 3 -> 9 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 3 -> 22 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 20 -> 6 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 21 -> 7 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 7 -> 20 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 6 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 3 -> 22 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 6 -> 20 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 6 -> 12 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 20 -> 7 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 10 -> 6 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 12 -> 10 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79110: 22 -> 9 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 9 -> 3 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 10 -> 6 at (2048, 3030), 1 frames after previous cover
- f114: ref 79105: 23 -> 15 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 3 -> 23 at (2097.5, 3025.5), 1 frames after previous cover
- ... 929 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 894 | 65 | 1 (894) |
| 78896 | 350 (76..429) | 258 | 50 | 21 (222), 16 (29), 6 (7) |
| 78969 | 352 (80..434) | 271 | 48 | 16 (149), 24 (66), 21 (40), 7 (8), 20 (4), 3 (3), 6 (1) |
| 78971 | 352 (84..439) | 273 | 49 | 20 (166), 24 (39), 16 (39), 7 (12), 32 (6), 21 (5), 26 (5), 30 (1) |
| 79045 | 355 (84..443) | 264 | 56 | 32 (130), 20 (48), 24 (31), 16 (19), 30 (11), 26 (7), 7 (5), 3 (4), 6 (3), 12 (3), 10 (2), 9 (1) |
| 79037 | 355 (86..445) | 279 | 54 | 24 (77), 32 (61), 30 (48), 20 (37), 16 (25), 26 (11), 12 (8), 6 (4), 7 (4), 3 (2), 10 (2) |
| 78897 | 345 (89..450) | 279 | 47 | 30 (127), 24 (44), 20 (28), 26 (26), 16 (23), 32 (14), 6 (5), 10 (4), 3 (2), 9 (2), 12 (2), 7 (2) |
| 78899 | 365 (91..455) | 274 | 59 | 26 (153), 24 (39), 32 (32), 30 (26), 10 (5), 12 (5), 20 (5), 9 (3), 6 (3), 3 (2), 7 (1) |
| 79097 | 366 (94..461) | 285 | 57 | 7 (113), 26 (87), 30 (36), 12 (16), 32 (10), 27 (10), 10 (4), 3 (3), 6 (3), 9 (1), 15 (1), 24 (1) |
| 79098 | 360 (97..467) | 276 | 60 | 12 (84), 27 (84), 7 (54), 15 (22), 30 (15), 32 (7), 10 (3), 6 (3), 3 (2), 9 (1), 26 (1) |
| 79102 | 371 (98..477) | 280 | 54 | 27 (104), 9 (65), 7 (53), 15 (30), 12 (18), 6 (5), 10 (3), 32 (2) |
| 79103 | 380 (99..481) | 299 | 55 | 7 (80), 12 (78), 27 (46), 9 (44), 15 (43), 3 (4), 33 (2), 10 (1), 6 (1) |
| 79105 | 379 (101..484) | 305 | 50 | 15 (81), 27 (72), 12 (53), 6 (37), 9 (28), 7 (14), 33 (13), 3 (3), 23 (3), 10 (1) |
| 79108 | 385 (104..492) | 317 | 50 | 15 (143), 6 (66), 9 (52), 33 (22), 12 (21), 3 (5), 23 (4), 10 (4) |
| 79110 | 388 (106..497) | 308 | 50 | 6 (100), 23 (67), 33 (35), 9 (30), 10 (17), 3 (12), 15 (12), 12 (12), 38 (12), 35 (10), 22 (1) |
| 79111 | 386 (109..500) | 306 | 52 | 23 (86), 6 (77), 10 (32), 3 (30), 35 (23), 9 (16), 12 (16), 38 (15), 15 (8), 22 (2), 33 (1) |
| 79115 | 421 (111..531) | 329 | 56 | 10 (166), 3 (61), 38 (25), 6 (23), 9 (18), 35 (17), 23 (13), 15 (3), 33 (3) |
| 79116 | 411 (114..530) | 335 | 52 | 33 (142), 3 (54), 10 (52), 38 (34), 9 (23), 6 (13), 35 (8), 22 (4), 40 (3), 23 (2) |
| 79122 | 404 (118..532) | 318 | 56 | 3 (147), 10 (57), 38 (31), 9 (25), 33 (25), 35 (14), 22 (13), 23 (6) |
| 79132 | 391 (120..515) | 303 | 52 | 40 (85), 38 (75), 10 (39), 35 (35), 9 (26), 3 (15), 33 (13), 22 (10), 23 (4), 29 (1) |
| 79128 | 402 (124..527) | 301 | 64 | 38 (75), 22 (62), 40 (42), 3 (38), 35 (23), 9 (18), 33 (18), 23 (17), 31 (5), 29 (3) |
| 79134 | 407 (127..533) | 347 | 43 | 22 (170), 23 (58), 31 (57), 35 (41), 33 (17), 29 (2), 38 (2) |
| 79135 | 409 (129..542) | 340 | 46 | 35 (150), 23 (76), 22 (47), 33 (40), 29 (15), 31 (9), 40 (3) |
| 79139 | 406 (132..537) | 336 | 49 | 31 (163), 29 (157), 22 (12), 33 (2), 10 (2) |
| 79136 | 393 (136..538) | 325 | 46 | 29 (152), 31 (122), 22 (48), 35 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 173/416/1002; tracks with internal gaps: 24; total internal gaps: 908; longest internal gap: 12; tracks ending in coasting: 23 (trailing rows total 620)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 1002 | 894 | 108 | 65 | 5 | 0 | 78911 |
| 3 | 80..561 | 482 | 482 | 387 | 95 | 47 | 6 | 30 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 87..529 | 443 | 443 | 351 | 92 | 45 | 7 | 29 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 87..509 | 423 | 423 | 346 | 77 | 41 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 91..506 | 416 | 416 | 353 | 63 | 25 | 4 | 29 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 10 | 92..559 | 468 | 468 | 394 | 74 | 37 | 3 | 22 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79139 |
| 12 | 96..494 | 399 | 399 | 316 | 83 | 39 | 5 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 100..521 | 422 | 422 | 343 | 79 | 34 | 4 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 102..468 | 367 | 367 | 284 | 83 | 39 | 5 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 109..471 | 363 | 363 | 288 | 75 | 35 | 4 | 28 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 21 | 109..463 | 355 | 355 | 267 | 88 | 42 | 4 | 29 | 78896, 78969, 78971 |
| 22 | 110..556 | 447 | 447 | 369 | 78 | 37 | 3 | 28 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 110..525 | 416 | 416 | 336 | 80 | 42 | 5 | 28 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 24 | 115..484 | 370 | 370 | 297 | 73 | 33 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 26 | 115..490 | 376 | 376 | 290 | 86 | 44 | 5 | 23 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 27 | 124..513 | 390 | 390 | 316 | 74 | 39 | 3 | 29 | 79097, 79098, 79102, 79103, 79105 |
| 29 | 128..566 | 439 | 439 | 330 | 109 | 47 | 4 | 31 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 30 | 128..479 | 352 | 352 | 264 | 88 | 35 | 5 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 31 | 135..566 | 432 | 432 | 356 | 76 | 39 | 2 | 28 | 79128, 79134, 79135, 79136, 79139 |
| 32 | 135..474 | 340 | 340 | 262 | 78 | 36 | 3 | 24 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 33 | 140..558 | 419 | 419 | 333 | 86 | 36 | 5 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 35 | 176..571 | 396 | 396 | 324 | 72 | 28 | 6 | 32 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 38 | 217..556 | 340 | 340 | 269 | 71 | 30 | 6 | 23 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 40 | 372..544 | 173 | 173 | 133 | 40 | 13 | 12 | 2 | 79116, 79128, 79132, 79135 |
