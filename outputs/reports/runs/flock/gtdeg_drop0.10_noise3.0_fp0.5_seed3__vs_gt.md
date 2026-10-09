# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=cfa6c4ec5bce
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise3.0_fp0.5_seed3/tracks.csv sha256=f180040af0caea52
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise3.0_fp0.5_seed3.csv sha256=cfa6c4ec5bce7459
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise3.0_fp0.5_seed3
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
| observations | none | 4 | 0.230 | 0.133 | 0.077 | 2.40 | 0.281 | 681 | 2499.0 |
| observations | none | 6 | 0.320 | 0.184 | 0.573 | 3.22 | 0.415 | 846 | 1735.0 |
| observations | none | 8 | 0.368 | 0.213 | 0.749 | 3.61 | 0.469 | 864 | 1159.0 |
| observations | none | 12 | 0.417 | 0.254 | 0.801 | 3.95 | 0.507 | 754 | 977.0 |
| observations | ignore | 4 | 0.230 | 0.133 | 0.077 | 2.40 | 0.281 | 681 | 2499.0 |
| observations | ignore | 6 | 0.320 | 0.184 | 0.573 | 3.22 | 0.415 | 846 | 1735.0 |
| observations | ignore | 8 | 0.368 | 0.213 | 0.749 | 3.61 | 0.469 | 864 | 1159.0 |
| observations | ignore | 12 | 0.417 | 0.254 | 0.801 | 3.95 | 0.507 | 754 | 977.0 |
| updates | none | 4 | 0.217 | 0.129 | -0.074 | 2.41 | 0.264 | 719 | 2505.0 |
| updates | none | 6 | 0.308 | 0.182 | 0.455 | 3.25 | 0.398 | 869 | 1533.0 |
| updates | none | 8 | 0.359 | 0.214 | 0.663 | 3.68 | 0.456 | 865 | 778.0 |
| updates | none | 12 | 0.411 | 0.258 | 0.749 | 4.12 | 0.503 | 721 | 452.0 |
| updates | ignore | 4 | 0.217 | 0.129 | -0.074 | 2.41 | 0.264 | 719 | 2505.0 |
| updates | ignore | 6 | 0.308 | 0.182 | 0.455 | 3.25 | 0.398 | 869 | 1533.0 |
| updates | ignore | 8 | 0.359 | 0.214 | 0.663 | 3.68 | 0.456 | 865 | 778.0 |
| updates | ignore | 12 | 0.411 | 0.258 | 0.749 | 4.12 | 0.503 | 721 | 452.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8803; unmatched reference entries: 1339; unmatched candidate entries: 342
- identity switches: 864; fragmentation (coverage interruptions): 1108; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 46 -> 45 at (2129.5, 3032), 1 frames after previous cover
- f90: ref 78971: 47 -> 46 at (2115, 3033.5), 2 frames after previous cover
- f92: ref 78897: 47 -> 45 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 46 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 45 -> 46 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78899: 47 -> 53 at (2146.5, 3030.5), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 53 -> 45 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 45 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 47 -> 53 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79098: 47 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 45 -> 54 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 53 -> 45 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 53 -> 58 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 53 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 58 -> 53 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 53 -> 58 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 45 -> 56 at (2083, 3033.5), 6 frames after previous cover
- f101: ref 79097: 45 -> 54 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 45 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 58 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 58 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 54 -> 60 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 56 -> 61 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 45 -> 54 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79105: 47 -> 58 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 54 -> 45 at (2093.5, 3029.5), 2 frames after previous cover
- f105: ref 78897: 56 -> 61 at (2058, 3033), 1 frames after previous cover
- f105: ref 78899: 60 -> 56 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 45 -> 60 at (2088, 3029), 1 frames after previous cover
- f105: ref 79098: 54 -> 45 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 53 -> 54 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 58 -> 53 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79108: 47 -> 58 at (2148.5, 3025), 1 frames after previous cover
- f106: ref 79037: 61 -> 46 at (2038, 3034.5), 2 frames after previous cover
- f107: ref 79045: 46 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79108: 58 -> 47 at (2136, 3026.5), 2 frames after previous cover
- f109: ref 79037: 46 -> 64 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 44 -> 46 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 47 -> 58 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 61 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 56 -> 61 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 64 -> 46 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 46 -> 44 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 56 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 45 -> 60 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 54 -> 45 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 79102: 45 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 53 -> 45 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 58 -> 54 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 58 -> 53 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 47 -> 58 at (2129, 3027), 1 frames after previous cover
- f112: ref 78899: 61 -> 64 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 56 -> 61 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 60 -> 56 at (2059, 3029.5), 2 frames after previous cover
- ... 804 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 886 | 106 | 2 (886) |
| 78896 | 350 (76..429) | 309 | 36 | 41 (308), 59 (1) |
| 78969 | 352 (80..434) | 305 | 35 | 59 (155), 72 (130), 44 (15), 41 (4), 60 (1) |
| 78971 | 352 (84..439) | 299 | 37 | 60 (142), 44 (121), 59 (27), 46 (2), 56 (2), 69 (2), 47 (1), 72 (1), 61 (1) |
| 79045 | 355 (84..443) | 300 | 40 | 44 (102), 59 (68), 61 (43), 69 (35), 60 (23), 46 (18), 78 (10), 45 (1) |
| 79037 | 355 (86..445) | 295 | 45 | 61 (101), 60 (53), 78 (46), 44 (39), 59 (33), 46 (12), 45 (5), 54 (2), 56 (2), 64 (1), 69 (1) |
| 78897 | 345 (89..450) | 297 | 37 | 78 (171), 44 (45), 60 (34), 69 (13), 61 (12), 45 (4), 56 (4), 46 (4), 59 (4), 47 (3), 64 (3) |
| 78899 | 365 (91..455) | 307 | 52 | 53 (110), 61 (78), 78 (56), 69 (21), 60 (15), 46 (10), 45 (6), 56 (4), 54 (2), 64 (2), 59 (2), 47 (1) |
| 79097 | 366 (94..461) | 329 | 33 | 69 (136), 53 (81), 45 (49), 61 (36), 60 (15), 64 (4), 56 (3), 47 (2), 54 (2), 46 (1) |
| 79098 | 360 (97..467) | 323 | 33 | 45 (94), 53 (53), 69 (53), 46 (38), 143 (34), 131 (19), 61 (10), 60 (9), 56 (7), 54 (2), 64 (2), 47 (1), +1 more |
| 79102 | 371 (98..477) | 331 | 36 | 131 (130), 45 (66), 53 (50), 143 (23), 69 (21), 46 (14), 60 (11), 54 (6), 64 (4), 61 (2), 73 (2), 47 (1), +1 more |
| 79103 | 380 (99..481) | 336 | 38 | 143 (100), 45 (68), 73 (56), 61 (22), 54 (20), 46 (17), 53 (15), 56 (14), 131 (12), 81 (7), 58 (3), 47 (2) |
| 79105 | 379 (101..484) | 323 | 50 | 81 (116), 73 (57), 143 (45), 45 (41), 54 (22), 56 (12), 53 (11), 131 (8), 184 (5), 58 (3), 61 (2), 47 (1) |
| 79108 | 385 (104..492) | 329 | 45 | 184 (110), 56 (74), 131 (33), 73 (27), 45 (23), 46 (19), 54 (17), 53 (11), 71 (6), 47 (3), 58 (3), 64 (3) |
| 79110 | 388 (106..497) | 339 | 44 | 73 (153), 56 (59), 54 (30), 81 (20), 66 (19), 64 (13), 105 (12), 184 (10), 46 (9), 45 (5), 58 (4), 47 (3), +1 more |
| 79111 | 386 (109..500) | 332 | 43 | 56 (151), 46 (39), 81 (28), 64 (25), 54 (24), 73 (19), 66 (14), 105 (10), 58 (9), 71 (9), 157 (4) |
| 79115 | 421 (111..531) | 373 | 39 | 157 (172), 66 (41), 64 (33), 58 (32), 46 (30), 71 (15), 54 (12), 105 (12), 56 (9), 73 (8), 81 (6), 47 (3) |
| 79116 | 411 (114..530) | 353 | 45 | 58 (98), 46 (83), 64 (58), 81 (24), 66 (23), 56 (23), 105 (13), 54 (8), 73 (8), 71 (5), 157 (5), 47 (4), +1 more |
| 79122 | 404 (118..532) | 359 | 39 | 58 (148), 46 (66), 64 (43), 66 (35), 81 (18), 73 (14), 157 (14), 54 (10), 71 (8), 47 (2), 105 (1) |
| 79132 | 391 (120..515) | 333 | 48 | 66 (175), 64 (60), 54 (30), 58 (29), 81 (23), 71 (6), 85 (4), 47 (3), 105 (3) |
| 79128 | 402 (124..527) | 363 | 33 | 64 (119), 81 (77), 58 (49), 66 (41), 157 (29), 46 (20), 77 (14), 85 (10), 47 (3), 56 (1) |
| 79134 | 407 (127..533) | 356 | 46 | 77 (196), 85 (90), 90 (46), 66 (15), 47 (8), 64 (1) |
| 79135 | 409 (129..542) | 341 | 54 | 77 (122), 85 (118), 47 (77), 90 (21), 56 (3) |
| 79139 | 406 (132..537) | 348 | 49 | 47 (203), 90 (113), 85 (20), 77 (12) |
| 79136 | 393 (136..538) | 337 | 45 | 90 (158), 85 (110), 47 (63), 77 (6) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 438 | 910..910 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 1/352/1004; tracks with internal gaps: 29; total internal gaps: 309; longest internal gap: 3; tracks ending in coasting: 11 (trailing rows total 17)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 926 | 886 | 40 | 40 | 1 | 0 | 78911 |
| 41 | 78..429 | 352 | 324 | 312 | 12 | 11 | 2 | 0 | 78896, 78969 |
| 44 | 82..449 | 368 | 335 | 322 | 13 | 13 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 45 | 86..481 | 396 | 372 | 362 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 46 | 86..528 | 443 | 402 | 382 | 20 | 19 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 47 | 87..535 | 449 | 404 | 384 | 20 | 18 | 2 | 0 | 78897, 78899, 78971, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 53 | 93..461 | 369 | 341 | 331 | 10 | 9 | 2 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 96..337 | 242 | 197 | 187 | 10 | 7 | 2 | 2 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 97..577 | 481 | 388 | 368 | 20 | 17 | 2 | 2 | 78897, 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79135 |
| 58 | 99..525 | 427 | 395 | 380 | 15 | 12 | 3 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 59 | 102..434 | 333 | 299 | 290 | 9 | 9 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 60 | 102..439 | 338 | 318 | 303 | 15 | 15 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..448 | 346 | 318 | 307 | 11 | 8 | 2 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 64 | 109..531 | 423 | 387 | 371 | 16 | 16 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 110..514 | 405 | 373 | 363 | 10 | 9 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 113..443 | 331 | 287 | 282 | 5 | 5 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 71 | 117..177 | 61 | 55 | 51 | 4 | 2 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 120..289 | 170 | 138 | 131 | 7 | 5 | 1 | 2 | 78969, 78971 |
| 73 | 120..500 | 381 | 356 | 344 | 12 | 12 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 77 | 127..533 | 407 | 362 | 350 | 12 | 12 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 127..455 | 329 | 293 | 283 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79045 |
| 81 | 133..484 | 352 | 328 | 319 | 9 | 9 | 1 | 0 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 85 | 138..539 | 402 | 361 | 352 | 9 | 7 | 2 | 1 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 145..538 | 394 | 350 | 339 | 11 | 11 | 1 | 0 | 79116, 79134, 79135, 79136, 79139 |
| 105 | 172..242 | 71 | 56 | 51 | 5 | 3 | 1 | 2 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 131 | 231..478 | 248 | 210 | 202 | 8 | 7 | 1 | 1 | 79098, 79102, 79103, 79105, 79108 |
| 143 | 243..467 | 225 | 208 | 202 | 6 | 5 | 2 | 0 | 79098, 79102, 79103, 79105 |
| 157 | 283..532 | 250 | 229 | 224 | 5 | 4 | 2 | 0 | 79111, 79115, 79116, 79122, 79128 |
| 184 | 350..499 | 150 | 132 | 125 | 7 | 4 | 2 | 2 | 79105, 79108, 79110 |
| 438 | 910..910 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8803; unmatched reference entries: 1339; unmatched candidate entries: 342
- identity switches: 864; fragmentation (coverage interruptions): 1108; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 46 -> 45 at (2129.5, 3032), 1 frames after previous cover
- f90: ref 78971: 47 -> 46 at (2115, 3033.5), 2 frames after previous cover
- f92: ref 78897: 47 -> 45 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 46 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 45 -> 46 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78899: 47 -> 53 at (2146.5, 3030.5), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 53 -> 45 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 45 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f96: ref 79097: 47 -> 53 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f98: ref 79098: 47 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 45 -> 54 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 53 -> 45 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 53 -> 58 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 53 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 58 -> 53 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 53 -> 58 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 45 -> 56 at (2083, 3033.5), 6 frames after previous cover
- f101: ref 79097: 45 -> 54 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 45 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 58 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 58 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 54 -> 60 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 56 -> 61 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 45 -> 54 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79105: 47 -> 58 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 54 -> 45 at (2093.5, 3029.5), 2 frames after previous cover
- f105: ref 78897: 56 -> 61 at (2058, 3033), 1 frames after previous cover
- f105: ref 78899: 60 -> 56 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 45 -> 60 at (2088, 3029), 1 frames after previous cover
- f105: ref 79098: 54 -> 45 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 53 -> 54 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 58 -> 53 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79108: 47 -> 58 at (2148.5, 3025), 1 frames after previous cover
- f106: ref 79037: 61 -> 46 at (2038, 3034.5), 2 frames after previous cover
- f107: ref 79045: 46 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79108: 58 -> 47 at (2136, 3026.5), 2 frames after previous cover
- f109: ref 79037: 46 -> 64 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 44 -> 46 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 47 -> 58 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 61 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 56 -> 61 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 64 -> 46 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 46 -> 44 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 56 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 45 -> 60 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 54 -> 45 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 79102: 45 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 53 -> 45 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 58 -> 54 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 58 -> 53 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 47 -> 58 at (2129, 3027), 1 frames after previous cover
- f112: ref 78899: 61 -> 64 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 56 -> 61 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 60 -> 56 at (2059, 3029.5), 2 frames after previous cover
- ... 804 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 886 | 106 | 2 (886) |
| 78896 | 350 (76..429) | 309 | 36 | 41 (308), 59 (1) |
| 78969 | 352 (80..434) | 305 | 35 | 59 (155), 72 (130), 44 (15), 41 (4), 60 (1) |
| 78971 | 352 (84..439) | 299 | 37 | 60 (142), 44 (121), 59 (27), 46 (2), 56 (2), 69 (2), 47 (1), 72 (1), 61 (1) |
| 79045 | 355 (84..443) | 300 | 40 | 44 (102), 59 (68), 61 (43), 69 (35), 60 (23), 46 (18), 78 (10), 45 (1) |
| 79037 | 355 (86..445) | 295 | 45 | 61 (101), 60 (53), 78 (46), 44 (39), 59 (33), 46 (12), 45 (5), 54 (2), 56 (2), 64 (1), 69 (1) |
| 78897 | 345 (89..450) | 297 | 37 | 78 (171), 44 (45), 60 (34), 69 (13), 61 (12), 45 (4), 56 (4), 46 (4), 59 (4), 47 (3), 64 (3) |
| 78899 | 365 (91..455) | 307 | 52 | 53 (110), 61 (78), 78 (56), 69 (21), 60 (15), 46 (10), 45 (6), 56 (4), 54 (2), 64 (2), 59 (2), 47 (1) |
| 79097 | 366 (94..461) | 329 | 33 | 69 (136), 53 (81), 45 (49), 61 (36), 60 (15), 64 (4), 56 (3), 47 (2), 54 (2), 46 (1) |
| 79098 | 360 (97..467) | 323 | 33 | 45 (94), 53 (53), 69 (53), 46 (38), 143 (34), 131 (19), 61 (10), 60 (9), 56 (7), 54 (2), 64 (2), 47 (1), +1 more |
| 79102 | 371 (98..477) | 331 | 36 | 131 (130), 45 (66), 53 (50), 143 (23), 69 (21), 46 (14), 60 (11), 54 (6), 64 (4), 61 (2), 73 (2), 47 (1), +1 more |
| 79103 | 380 (99..481) | 336 | 38 | 143 (100), 45 (68), 73 (56), 61 (22), 54 (20), 46 (17), 53 (15), 56 (14), 131 (12), 81 (7), 58 (3), 47 (2) |
| 79105 | 379 (101..484) | 323 | 50 | 81 (116), 73 (57), 143 (45), 45 (41), 54 (22), 56 (12), 53 (11), 131 (8), 184 (5), 58 (3), 61 (2), 47 (1) |
| 79108 | 385 (104..492) | 329 | 45 | 184 (110), 56 (74), 131 (33), 73 (27), 45 (23), 46 (19), 54 (17), 53 (11), 71 (6), 47 (3), 58 (3), 64 (3) |
| 79110 | 388 (106..497) | 339 | 44 | 73 (153), 56 (59), 54 (30), 81 (20), 66 (19), 64 (13), 105 (12), 184 (10), 46 (9), 45 (5), 58 (4), 47 (3), +1 more |
| 79111 | 386 (109..500) | 332 | 43 | 56 (151), 46 (39), 81 (28), 64 (25), 54 (24), 73 (19), 66 (14), 105 (10), 58 (9), 71 (9), 157 (4) |
| 79115 | 421 (111..531) | 373 | 39 | 157 (172), 66 (41), 64 (33), 58 (32), 46 (30), 71 (15), 54 (12), 105 (12), 56 (9), 73 (8), 81 (6), 47 (3) |
| 79116 | 411 (114..530) | 353 | 45 | 58 (98), 46 (83), 64 (58), 81 (24), 66 (23), 56 (23), 105 (13), 54 (8), 73 (8), 71 (5), 157 (5), 47 (4), +1 more |
| 79122 | 404 (118..532) | 359 | 39 | 58 (148), 46 (66), 64 (43), 66 (35), 81 (18), 73 (14), 157 (14), 54 (10), 71 (8), 47 (2), 105 (1) |
| 79132 | 391 (120..515) | 333 | 48 | 66 (175), 64 (60), 54 (30), 58 (29), 81 (23), 71 (6), 85 (4), 47 (3), 105 (3) |
| 79128 | 402 (124..527) | 363 | 33 | 64 (119), 81 (77), 58 (49), 66 (41), 157 (29), 46 (20), 77 (14), 85 (10), 47 (3), 56 (1) |
| 79134 | 407 (127..533) | 356 | 46 | 77 (196), 85 (90), 90 (46), 66 (15), 47 (8), 64 (1) |
| 79135 | 409 (129..542) | 341 | 54 | 77 (122), 85 (118), 47 (77), 90 (21), 56 (3) |
| 79139 | 406 (132..537) | 348 | 49 | 47 (203), 90 (113), 85 (20), 77 (12) |
| 79136 | 393 (136..538) | 337 | 45 | 90 (158), 85 (110), 47 (63), 77 (6) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 438 | 910..910 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 1/352/1004; tracks with internal gaps: 29; total internal gaps: 309; longest internal gap: 3; tracks ending in coasting: 11 (trailing rows total 17)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 926 | 886 | 40 | 40 | 1 | 0 | 78911 |
| 41 | 78..429 | 352 | 324 | 312 | 12 | 11 | 2 | 0 | 78896, 78969 |
| 44 | 82..449 | 368 | 335 | 322 | 13 | 13 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 45 | 86..481 | 396 | 372 | 362 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 46 | 86..528 | 443 | 402 | 382 | 20 | 19 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 47 | 87..535 | 449 | 404 | 384 | 20 | 18 | 2 | 0 | 78897, 78899, 78971, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 53 | 93..461 | 369 | 341 | 331 | 10 | 9 | 2 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 96..337 | 242 | 197 | 187 | 10 | 7 | 2 | 2 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 97..577 | 481 | 388 | 368 | 20 | 17 | 2 | 2 | 78897, 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79135 |
| 58 | 99..525 | 427 | 395 | 380 | 15 | 12 | 3 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 59 | 102..434 | 333 | 299 | 290 | 9 | 9 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 60 | 102..439 | 338 | 318 | 303 | 15 | 15 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..448 | 346 | 318 | 307 | 11 | 8 | 2 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 64 | 109..531 | 423 | 387 | 371 | 16 | 16 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 110..514 | 405 | 373 | 363 | 10 | 9 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 113..443 | 331 | 287 | 282 | 5 | 5 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 71 | 117..177 | 61 | 55 | 51 | 4 | 2 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 120..289 | 170 | 138 | 131 | 7 | 5 | 1 | 2 | 78969, 78971 |
| 73 | 120..500 | 381 | 356 | 344 | 12 | 12 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 77 | 127..533 | 407 | 362 | 350 | 12 | 12 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 127..455 | 329 | 293 | 283 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79045 |
| 81 | 133..484 | 352 | 328 | 319 | 9 | 9 | 1 | 0 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 85 | 138..539 | 402 | 361 | 352 | 9 | 7 | 2 | 1 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 145..538 | 394 | 350 | 339 | 11 | 11 | 1 | 0 | 79116, 79134, 79135, 79136, 79139 |
| 105 | 172..242 | 71 | 56 | 51 | 5 | 3 | 1 | 2 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 131 | 231..478 | 248 | 210 | 202 | 8 | 7 | 1 | 1 | 79098, 79102, 79103, 79105, 79108 |
| 143 | 243..467 | 225 | 208 | 202 | 6 | 5 | 2 | 0 | 79098, 79102, 79103, 79105 |
| 157 | 283..532 | 250 | 229 | 224 | 5 | 4 | 2 | 0 | 79111, 79115, 79116, 79122, 79128 |
| 184 | 350..499 | 150 | 132 | 125 | 7 | 4 | 2 | 2 | 79105, 79108, 79110 |
| 438 | 910..910 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 9287; unmatched reference entries: 855; unmatched candidate entries: 1702
- identity switches: 865; fragmentation (coverage interruptions): 686; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 46 -> 45 at (2129.5, 3032), 1 frames after previous cover
- f90: ref 78971: 47 -> 46 at (2115, 3033.5), 2 frames after previous cover
- f92: ref 78897: 47 -> 45 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 46 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 45 -> 46 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78899: 47 -> 53 at (2146.5, 3030.5), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 53 -> 45 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 45 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 47 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 45 -> 54 at (2100, 3031), 3 frames after previous cover
- f98: ref 79098: 47 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 45 -> 54 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 53 -> 45 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 53 -> 58 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 53 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 58 -> 53 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 53 -> 58 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 54 -> 56 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79097: 45 -> 54 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 45 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 58 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 58 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 54 -> 60 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 56 -> 61 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 45 -> 54 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79105: 47 -> 58 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 54 -> 45 at (2093.5, 3029.5), 2 frames after previous cover
- f105: ref 78897: 56 -> 61 at (2058, 3033), 1 frames after previous cover
- f105: ref 78899: 60 -> 56 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 45 -> 60 at (2088, 3029), 1 frames after previous cover
- f105: ref 79098: 54 -> 45 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 53 -> 54 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 58 -> 53 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79108: 47 -> 58 at (2148.5, 3025), 1 frames after previous cover
- f106: ref 79037: 61 -> 46 at (2038, 3034.5), 2 frames after previous cover
- f107: ref 79045: 46 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79108: 58 -> 47 at (2136, 3026.5), 2 frames after previous cover
- f109: ref 79037: 46 -> 64 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 44 -> 46 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 47 -> 58 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 61 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 56 -> 61 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 64 -> 46 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 46 -> 44 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 56 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 45 -> 60 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 54 -> 45 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 79102: 45 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 53 -> 45 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 58 -> 54 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 58 -> 53 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 47 -> 58 at (2129, 3027), 1 frames after previous cover
- f112: ref 78899: 61 -> 64 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 56 -> 61 at (2046, 3030.5), 1 frames after previous cover
- ... 805 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 945 | 52 | 2 (945) |
| 78896 | 350 (76..429) | 320 | 26 | 41 (319), 59 (1) |
| 78969 | 352 (80..434) | 321 | 22 | 59 (164), 72 (137), 44 (15), 41 (4), 60 (1) |
| 78971 | 352 (84..439) | 314 | 24 | 60 (147), 44 (129), 59 (29), 46 (2), 56 (2), 69 (2), 47 (1), 72 (1), 61 (1) |
| 79045 | 355 (84..443) | 315 | 26 | 44 (107), 59 (71), 61 (43), 69 (40), 60 (25), 46 (18), 78 (10), 45 (1) |
| 79037 | 355 (86..445) | 313 | 32 | 61 (109), 60 (56), 78 (49), 44 (41), 59 (35), 46 (12), 45 (5), 54 (2), 56 (2), 64 (1), 69 (1) |
| 78897 | 345 (89..450) | 311 | 29 | 78 (180), 44 (48), 60 (34), 69 (14), 61 (12), 45 (4), 56 (4), 46 (4), 59 (4), 47 (3), 64 (3), 54 (1) |
| 78899 | 365 (91..455) | 327 | 34 | 53 (116), 61 (84), 78 (63), 69 (20), 60 (15), 46 (12), 45 (6), 56 (4), 54 (2), 64 (2), 59 (2), 47 (1) |
| 79097 | 366 (94..461) | 337 | 25 | 69 (140), 53 (82), 45 (49), 61 (36), 60 (17), 64 (4), 47 (3), 56 (3), 54 (2), 46 (1) |
| 79098 | 360 (97..467) | 340 | 18 | 45 (99), 53 (57), 69 (56), 46 (40), 143 (36), 131 (20), 61 (10), 60 (9), 56 (7), 54 (2), 64 (2), 47 (1), +1 more |
| 79102 | 371 (98..477) | 341 | 26 | 131 (135), 45 (66), 53 (51), 143 (23), 69 (22), 46 (15), 60 (11), 54 (7), 64 (5), 61 (2), 73 (2), 47 (1), +1 more |
| 79103 | 380 (99..481) | 344 | 31 | 143 (103), 45 (72), 73 (56), 61 (22), 54 (21), 46 (17), 53 (15), 56 (14), 131 (12), 81 (7), 58 (3), 47 (2) |
| 79105 | 379 (101..484) | 351 | 24 | 81 (129), 73 (62), 143 (50), 45 (41), 54 (25), 56 (13), 53 (11), 131 (9), 184 (5), 58 (3), 61 (2), 47 (1) |
| 79108 | 385 (104..492) | 349 | 28 | 184 (118), 56 (75), 131 (39), 73 (28), 45 (23), 46 (21), 54 (18), 53 (12), 71 (6), 47 (3), 58 (3), 64 (3) |
| 79110 | 388 (106..497) | 353 | 30 | 73 (161), 56 (60), 54 (33), 81 (21), 66 (18), 64 (13), 105 (12), 184 (11), 46 (9), 45 (5), 58 (4), 47 (3), +2 more |
| 79111 | 386 (109..500) | 349 | 30 | 56 (158), 46 (40), 81 (31), 54 (28), 64 (26), 73 (19), 66 (15), 105 (10), 58 (9), 71 (9), 157 (4) |
| 79115 | 421 (111..531) | 387 | 26 | 157 (183), 66 (41), 64 (34), 46 (33), 58 (32), 71 (15), 54 (12), 105 (12), 73 (8), 81 (7), 56 (7), 47 (3) |
| 79116 | 411 (114..530) | 377 | 24 | 58 (103), 46 (91), 64 (61), 56 (29), 81 (25), 66 (23), 105 (15), 54 (8), 73 (8), 71 (5), 47 (4), 157 (4), +1 more |
| 79122 | 404 (118..532) | 373 | 25 | 58 (153), 46 (70), 64 (43), 66 (37), 81 (19), 73 (15), 157 (14), 54 (11), 71 (8), 47 (2), 105 (1) |
| 79132 | 391 (120..515) | 351 | 34 | 66 (188), 64 (62), 58 (33), 54 (30), 81 (22), 71 (6), 85 (4), 47 (3), 105 (3) |
| 79128 | 402 (124..527) | 376 | 20 | 64 (127), 81 (77), 58 (50), 66 (45), 157 (30), 46 (20), 77 (14), 85 (10), 47 (3) |
| 79134 | 407 (127..533) | 383 | 23 | 77 (207), 85 (94), 90 (50), 66 (16), 47 (12), 64 (3), 184 (1) |
| 79135 | 409 (129..542) | 374 | 25 | 77 (136), 85 (133), 47 (80), 90 (23), 46 (2) |
| 79139 | 406 (132..537) | 373 | 28 | 47 (217), 90 (123), 85 (21), 77 (12) |
| 79136 | 393 (136..538) | 363 | 24 | 90 (168), 85 (116), 47 (69), 77 (10) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 438 | 910..939 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 30/381/1004; tracks with internal gaps: 29; total internal gaps: 599; longest internal gap: 30; tracks ending in coasting: 29 (trailing rows total 892)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 945 | 59 | 52 | 3 | 0 | 78911 |
| 41 | 78..458 | 381 | 381 | 323 | 58 | 24 | 4 | 29 | 78896, 78969 |
| 44 | 82..478 | 397 | 397 | 340 | 57 | 27 | 2 | 28 | 78897, 78969, 78971, 79037, 79045 |
| 45 | 86..510 | 425 | 425 | 371 | 54 | 20 | 5 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 46 | 86..557 | 472 | 472 | 407 | 65 | 34 | 11 | 17 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79135 |
| 47 | 87..564 | 478 | 478 | 412 | 66 | 34 | 3 | 23 | 78897, 78899, 78971, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 53 | 93..490 | 398 | 398 | 344 | 54 | 23 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 96..366 | 271 | 271 | 202 | 69 | 10 | 2 | 57 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 97..606 | 510 | 510 | 378 | 132 | 24 | 30 | 76 | 78897, 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 58 | 99..554 | 456 | 456 | 395 | 61 | 29 | 3 | 26 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 59 | 102..463 | 362 | 362 | 306 | 56 | 21 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 60 | 102..468 | 367 | 367 | 315 | 52 | 21 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..477 | 375 | 375 | 321 | 54 | 16 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 64 | 109..560 | 452 | 452 | 389 | 63 | 27 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 110..543 | 434 | 434 | 383 | 51 | 23 | 10 | 16 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 113..472 | 360 | 360 | 295 | 65 | 17 | 18 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 71 | 117..206 | 90 | 90 | 51 | 39 | 3 | 2 | 34 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 120..318 | 199 | 199 | 138 | 61 | 12 | 3 | 47 | 78969, 78971 |
| 73 | 120..529 | 410 | 410 | 359 | 51 | 21 | 2 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 77 | 127..562 | 436 | 436 | 379 | 57 | 28 | 8 | 20 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 127..484 | 358 | 358 | 302 | 56 | 26 | 2 | 29 | 78897, 78899, 79037, 79045 |
| 81 | 133..513 | 381 | 381 | 338 | 43 | 12 | 2 | 29 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 85 | 138..568 | 431 | 431 | 378 | 53 | 18 | 2 | 30 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 145..567 | 423 | 423 | 365 | 58 | 25 | 2 | 29 | 79116, 79134, 79135, 79136, 79139 |
| 105 | 172..271 | 100 | 100 | 53 | 47 | 4 | 2 | 42 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 131 | 231..507 | 277 | 277 | 216 | 61 | 19 | 9 | 30 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 143 | 243..496 | 254 | 254 | 212 | 42 | 10 | 2 | 29 | 79098, 79102, 79103, 79105 |
| 157 | 283..561 | 279 | 279 | 235 | 44 | 11 | 3 | 29 | 79111, 79115, 79116, 79122, 79128 |
| 184 | 350..528 | 179 | 179 | 135 | 44 | 8 | 28 | 7 | 79105, 79108, 79110, 79134 |
| 438 | 910..939 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 9287; unmatched reference entries: 855; unmatched candidate entries: 1702
- identity switches: 865; fragmentation (coverage interruptions): 686; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 46 -> 45 at (2129.5, 3032), 1 frames after previous cover
- f90: ref 78971: 47 -> 46 at (2115, 3033.5), 2 frames after previous cover
- f92: ref 78897: 47 -> 45 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 46 -> 44 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 45 -> 46 at (2110.5, 3033.5), 3 frames after previous cover
- f93: ref 78899: 47 -> 53 at (2146.5, 3030.5), 1 frames after previous cover
- f93: ref 78969: 44 -> 41 at (2077.5, 3034), 2 frames after previous cover
- f94: ref 78969: 41 -> 44 at (2071, 3031), 1 frames after previous cover
- f96: ref 78899: 53 -> 45 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 45 -> 54 at (2099, 3033.5), 5 frames after previous cover
- f97: ref 78971: 44 -> 56 at (2072, 3034.5), 4 frames after previous cover
- f97: ref 79097: 47 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 45 -> 54 at (2100, 3031), 3 frames after previous cover
- f98: ref 79098: 47 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 45 -> 54 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 78971: 56 -> 44 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79037: 54 -> 56 at (2080, 3034.5), 2 frames after previous cover
- f99: ref 79097: 53 -> 45 at (2122.5, 3028.5), 2 frames after previous cover
- f99: ref 79098: 53 -> 58 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 47 -> 53 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 79098: 58 -> 53 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 53 -> 58 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 54 -> 56 at (2083, 3033.5), 3 frames after previous cover
- f101: ref 79097: 45 -> 54 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 53 -> 45 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 58 -> 53 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 47 -> 58 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78969: 44 -> 59 at (2021, 3032), 4 frames after previous cover
- f103: ref 78899: 54 -> 60 at (2086, 3030), 3 frames after previous cover
- f103: ref 79037: 56 -> 61 at (2056.5, 3034.5), 3 frames after previous cover
- f103: ref 79098: 45 -> 54 at (2113.5, 3027), 1 frames after previous cover
- f103: ref 79105: 47 -> 58 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 79097: 54 -> 45 at (2093.5, 3029.5), 2 frames after previous cover
- f105: ref 78897: 56 -> 61 at (2058, 3033), 1 frames after previous cover
- f105: ref 78899: 60 -> 56 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 45 -> 60 at (2088, 3029), 1 frames after previous cover
- f105: ref 79098: 54 -> 45 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 53 -> 54 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 58 -> 53 at (2120.5, 3023), 1 frames after previous cover
- f105: ref 79108: 47 -> 58 at (2148.5, 3025), 1 frames after previous cover
- f106: ref 79037: 61 -> 46 at (2038, 3034.5), 2 frames after previous cover
- f107: ref 79045: 46 -> 44 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79108: 58 -> 47 at (2136, 3026.5), 2 frames after previous cover
- f109: ref 79037: 46 -> 64 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79045: 44 -> 46 at (2007, 3034), 2 frames after previous cover
- f109: ref 79108: 47 -> 58 at (2125, 3025), 1 frames after previous cover
- f110: ref 78897: 61 -> 64 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 56 -> 61 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79037: 64 -> 46 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 46 -> 44 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 60 -> 56 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 45 -> 60 at (2072.5, 3029.5), 2 frames after previous cover
- f110: ref 79102: 54 -> 45 at (2084.5, 3028.5), 1 frames after previous cover
- f111: ref 79102: 45 -> 60 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 53 -> 45 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 58 -> 54 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79108: 58 -> 53 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 47 -> 58 at (2129, 3027), 1 frames after previous cover
- f112: ref 78899: 61 -> 64 at (2032, 3032), 1 frames after previous cover
- f112: ref 79097: 56 -> 61 at (2046, 3030.5), 1 frames after previous cover
- ... 805 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 945 | 52 | 2 (945) |
| 78896 | 350 (76..429) | 320 | 26 | 41 (319), 59 (1) |
| 78969 | 352 (80..434) | 321 | 22 | 59 (164), 72 (137), 44 (15), 41 (4), 60 (1) |
| 78971 | 352 (84..439) | 314 | 24 | 60 (147), 44 (129), 59 (29), 46 (2), 56 (2), 69 (2), 47 (1), 72 (1), 61 (1) |
| 79045 | 355 (84..443) | 315 | 26 | 44 (107), 59 (71), 61 (43), 69 (40), 60 (25), 46 (18), 78 (10), 45 (1) |
| 79037 | 355 (86..445) | 313 | 32 | 61 (109), 60 (56), 78 (49), 44 (41), 59 (35), 46 (12), 45 (5), 54 (2), 56 (2), 64 (1), 69 (1) |
| 78897 | 345 (89..450) | 311 | 29 | 78 (180), 44 (48), 60 (34), 69 (14), 61 (12), 45 (4), 56 (4), 46 (4), 59 (4), 47 (3), 64 (3), 54 (1) |
| 78899 | 365 (91..455) | 327 | 34 | 53 (116), 61 (84), 78 (63), 69 (20), 60 (15), 46 (12), 45 (6), 56 (4), 54 (2), 64 (2), 59 (2), 47 (1) |
| 79097 | 366 (94..461) | 337 | 25 | 69 (140), 53 (82), 45 (49), 61 (36), 60 (17), 64 (4), 47 (3), 56 (3), 54 (2), 46 (1) |
| 79098 | 360 (97..467) | 340 | 18 | 45 (99), 53 (57), 69 (56), 46 (40), 143 (36), 131 (20), 61 (10), 60 (9), 56 (7), 54 (2), 64 (2), 47 (1), +1 more |
| 79102 | 371 (98..477) | 341 | 26 | 131 (135), 45 (66), 53 (51), 143 (23), 69 (22), 46 (15), 60 (11), 54 (7), 64 (5), 61 (2), 73 (2), 47 (1), +1 more |
| 79103 | 380 (99..481) | 344 | 31 | 143 (103), 45 (72), 73 (56), 61 (22), 54 (21), 46 (17), 53 (15), 56 (14), 131 (12), 81 (7), 58 (3), 47 (2) |
| 79105 | 379 (101..484) | 351 | 24 | 81 (129), 73 (62), 143 (50), 45 (41), 54 (25), 56 (13), 53 (11), 131 (9), 184 (5), 58 (3), 61 (2), 47 (1) |
| 79108 | 385 (104..492) | 349 | 28 | 184 (118), 56 (75), 131 (39), 73 (28), 45 (23), 46 (21), 54 (18), 53 (12), 71 (6), 47 (3), 58 (3), 64 (3) |
| 79110 | 388 (106..497) | 353 | 30 | 73 (161), 56 (60), 54 (33), 81 (21), 66 (18), 64 (13), 105 (12), 184 (11), 46 (9), 45 (5), 58 (4), 47 (3), +2 more |
| 79111 | 386 (109..500) | 349 | 30 | 56 (158), 46 (40), 81 (31), 54 (28), 64 (26), 73 (19), 66 (15), 105 (10), 58 (9), 71 (9), 157 (4) |
| 79115 | 421 (111..531) | 387 | 26 | 157 (183), 66 (41), 64 (34), 46 (33), 58 (32), 71 (15), 54 (12), 105 (12), 73 (8), 81 (7), 56 (7), 47 (3) |
| 79116 | 411 (114..530) | 377 | 24 | 58 (103), 46 (91), 64 (61), 56 (29), 81 (25), 66 (23), 105 (15), 54 (8), 73 (8), 71 (5), 47 (4), 157 (4), +1 more |
| 79122 | 404 (118..532) | 373 | 25 | 58 (153), 46 (70), 64 (43), 66 (37), 81 (19), 73 (15), 157 (14), 54 (11), 71 (8), 47 (2), 105 (1) |
| 79132 | 391 (120..515) | 351 | 34 | 66 (188), 64 (62), 58 (33), 54 (30), 81 (22), 71 (6), 85 (4), 47 (3), 105 (3) |
| 79128 | 402 (124..527) | 376 | 20 | 64 (127), 81 (77), 58 (50), 66 (45), 157 (30), 46 (20), 77 (14), 85 (10), 47 (3) |
| 79134 | 407 (127..533) | 383 | 23 | 77 (207), 85 (94), 90 (50), 66 (16), 47 (12), 64 (3), 184 (1) |
| 79135 | 409 (129..542) | 374 | 25 | 77 (136), 85 (133), 47 (80), 90 (23), 46 (2) |
| 79139 | 406 (132..537) | 373 | 28 | 47 (217), 90 (123), 85 (21), 77 (12) |
| 79136 | 393 (136..538) | 363 | 24 | 90 (168), 85 (116), 47 (69), 77 (10) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 438 | 910..939 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 30/381/1004; tracks with internal gaps: 29; total internal gaps: 599; longest internal gap: 30; tracks ending in coasting: 29 (trailing rows total 892)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 945 | 59 | 52 | 3 | 0 | 78911 |
| 41 | 78..458 | 381 | 381 | 323 | 58 | 24 | 4 | 29 | 78896, 78969 |
| 44 | 82..478 | 397 | 397 | 340 | 57 | 27 | 2 | 28 | 78897, 78969, 78971, 79037, 79045 |
| 45 | 86..510 | 425 | 425 | 371 | 54 | 20 | 5 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 46 | 86..557 | 472 | 472 | 407 | 65 | 34 | 11 | 17 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79135 |
| 47 | 87..564 | 478 | 478 | 412 | 66 | 34 | 3 | 23 | 78897, 78899, 78971, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 53 | 93..490 | 398 | 398 | 344 | 54 | 23 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 96..366 | 271 | 271 | 202 | 69 | 10 | 2 | 57 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 56 | 97..606 | 510 | 510 | 378 | 132 | 24 | 30 | 76 | 78897, 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 58 | 99..554 | 456 | 456 | 395 | 61 | 29 | 3 | 26 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 59 | 102..463 | 362 | 362 | 306 | 56 | 21 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 60 | 102..468 | 367 | 367 | 315 | 52 | 21 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 61 | 103..477 | 375 | 375 | 321 | 54 | 16 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 64 | 109..560 | 452 | 452 | 389 | 63 | 27 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 66 | 110..543 | 434 | 434 | 383 | 51 | 23 | 10 | 16 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 113..472 | 360 | 360 | 295 | 65 | 17 | 18 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 71 | 117..206 | 90 | 90 | 51 | 39 | 3 | 2 | 34 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 120..318 | 199 | 199 | 138 | 61 | 12 | 3 | 47 | 78969, 78971 |
| 73 | 120..529 | 410 | 410 | 359 | 51 | 21 | 2 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 77 | 127..562 | 436 | 436 | 379 | 57 | 28 | 8 | 20 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 127..484 | 358 | 358 | 302 | 56 | 26 | 2 | 29 | 78897, 78899, 79037, 79045 |
| 81 | 133..513 | 381 | 381 | 338 | 43 | 12 | 2 | 29 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 85 | 138..568 | 431 | 431 | 378 | 53 | 18 | 2 | 30 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 145..567 | 423 | 423 | 365 | 58 | 25 | 2 | 29 | 79116, 79134, 79135, 79136, 79139 |
| 105 | 172..271 | 100 | 100 | 53 | 47 | 4 | 2 | 42 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 131 | 231..507 | 277 | 277 | 216 | 61 | 19 | 9 | 30 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 143 | 243..496 | 254 | 254 | 212 | 42 | 10 | 2 | 29 | 79098, 79102, 79103, 79105 |
| 157 | 283..561 | 279 | 279 | 235 | 44 | 11 | 3 | 29 | 79111, 79115, 79116, 79122, 79128 |
| 184 | 350..528 | 179 | 179 | 135 | 44 | 8 | 28 | 7 | 79105, 79108, 79110, 79134 |
| 438 | 910..939 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
