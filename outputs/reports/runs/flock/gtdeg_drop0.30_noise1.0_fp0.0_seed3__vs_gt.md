# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=d06ac3e7cac8
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise1.0_fp0.0_seed3/tracks.csv sha256=77ddf5de7e637c8b
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise1.0_fp0.0_seed3.csv sha256=d06ac3e7cac836c5
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise1.0_fp0.0_seed3
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
| observations | none | 4 | 0.299 | 0.153 | 0.610 | 1.26 | 0.392 | 889 | 2019.0 |
| observations | none | 6 | 0.320 | 0.165 | 0.611 | 1.26 | 0.392 | 883 | 2013.0 |
| observations | none | 8 | 0.331 | 0.174 | 0.612 | 1.29 | 0.394 | 877 | 2004.0 |
| observations | none | 12 | 0.347 | 0.188 | 0.618 | 1.59 | 0.411 | 791 | 1957.0 |
| observations | ignore | 4 | 0.299 | 0.153 | 0.610 | 1.26 | 0.392 | 889 | 2019.0 |
| observations | ignore | 6 | 0.320 | 0.165 | 0.611 | 1.26 | 0.392 | 883 | 2013.0 |
| observations | ignore | 8 | 0.331 | 0.174 | 0.612 | 1.29 | 0.394 | 877 | 2004.0 |
| observations | ignore | 12 | 0.347 | 0.188 | 0.618 | 1.59 | 0.411 | 791 | 1957.0 |
| updates | none | 4 | 0.284 | 0.154 | 0.392 | 1.33 | 0.361 | 942 | 1900.0 |
| updates | none | 6 | 0.332 | 0.181 | 0.517 | 1.63 | 0.397 | 957 | 1440.0 |
| updates | none | 8 | 0.362 | 0.201 | 0.634 | 2.02 | 0.432 | 916 | 1042.0 |
| updates | none | 12 | 0.399 | 0.229 | 0.701 | 2.59 | 0.468 | 818 | 785.0 |
| updates | ignore | 4 | 0.284 | 0.154 | 0.392 | 1.33 | 0.361 | 942 | 1900.0 |
| updates | ignore | 6 | 0.332 | 0.181 | 0.517 | 1.63 | 0.397 | 957 | 1440.0 |
| updates | ignore | 8 | 0.362 | 0.201 | 0.634 | 2.02 | 0.432 | 916 | 1042.0 |
| updates | ignore | 12 | 0.399 | 0.229 | 0.701 | 2.59 | 0.468 | 818 | 785.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7082; unmatched reference entries: 3060; unmatched candidate entries: 2
- identity switches: 877; fragmentation (coverage interruptions): 2058; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 5 -> 6 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 4 -> 5 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 5 -> 6 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 5 -> 6 at (2107, 3033), 2 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79045: 6 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 6 -> 8 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 4 -> 5 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 6 -> 8 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 8 -> 9 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 5 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 8 -> 3 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 5 -> 9 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 6 -> 8 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 3 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 8 -> 9 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 9 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 3 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 10 -> 9 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 3 -> 10 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 8 -> 6 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 6 -> 4 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 9 -> 10 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 10 -> 9 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 4 -> 6 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 8 -> 10 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 10 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 9 -> 13 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 5 -> 4 at (2110, 3022.5), 6 frames after previous cover
- f108: ref 78899: 8 -> 17 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 9 -> 8 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 9 -> 13 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 13 -> 9 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79098: 6 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 4 -> 14 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 17 -> 10 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 9 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 9 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 6 -> 17 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 4 -> 6 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 5 -> 4 at (2101.5, 3024.5), 4 frames after previous cover
- f111: ref 78897: 10 -> 13 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 10 -> 8 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 3 -> 2 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 13 -> 3 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 6 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 4 -> 6 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 5 -> 14 at (2113.5, 3026), 1 frames after previous cover
- ... 817 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 698 | 211 | 29 (577), 0 (121) |
| 78896 | 350 (76..429) | 242 | 75 | 21 (213), 2 (29) |
| 78969 | 352 (80..434) | 251 | 67 | 23 (88), 9 (63), 3 (40), 2 (28), 21 (15), 33 (12), 20 (5) |
| 78971 | 352 (84..439) | 238 | 72 | 33 (94), 3 (52), 9 (36), 20 (24), 23 (24), 6 (2), 21 (2), 2 (2), 10 (1), 8 (1) |
| 79045 | 355 (84..443) | 237 | 78 | 8 (100), 23 (63), 3 (27), 9 (15), 20 (11), 2 (6), 33 (6), 6 (2), 21 (2), 4 (1), 5 (1), 10 (1), +2 more |
| 79037 | 355 (86..445) | 236 | 76 | 9 (93), 8 (32), 23 (30), 25 (22), 3 (20), 20 (12), 33 (12), 6 (3), 13 (3), 34 (3), 4 (2), 5 (2), +2 more |
| 78897 | 345 (89..450) | 246 | 67 | 34 (96), 20 (59), 3 (36), 8 (15), 33 (9), 2 (8), 9 (7), 10 (4), 5 (3), 23 (3), 4 (2), 6 (2), +1 more |
| 78899 | 365 (91..455) | 263 | 67 | 3 (92), 8 (61), 9 (36), 20 (22), 2 (15), 25 (12), 34 (6), 23 (4), 13 (3), 6 (3), 4 (2), 5 (2), +3 more |
| 79097 | 366 (94..461) | 250 | 77 | 20 (84), 2 (57), 8 (37), 25 (31), 13 (10), 9 (10), 5 (7), 6 (6), 4 (4), 17 (2), 10 (2) |
| 79098 | 360 (97..467) | 272 | 60 | 2 (135), 3 (42), 8 (16), 25 (16), 13 (14), 6 (12), 5 (12), 17 (10), 20 (5), 4 (4), 9 (3), 22 (3) |
| 79102 | 371 (98..477) | 269 | 71 | 25 (96), 13 (59), 20 (48), 6 (15), 17 (14), 2 (10), 8 (9), 22 (5), 4 (4), 14 (3), 9 (3), 23 (2), +1 more |
| 79103 | 380 (99..481) | 263 | 81 | 13 (118), 25 (55), 22 (51), 17 (11), 5 (9), 8 (4), 6 (3), 10 (3), 9 (3), 4 (2), 23 (2), 32 (1), +1 more |
| 79105 | 379 (101..484) | 272 | 81 | 22 (174), 17 (26), 32 (26), 13 (23), 5 (6), 10 (5), 4 (4), 6 (4), 23 (2), 25 (1), 9 (1) |
| 79108 | 385 (104..492) | 284 | 73 | 17 (145), 13 (70), 32 (17), 22 (11), 6 (10), 25 (9), 10 (7), 5 (5), 31 (4), 4 (3), 14 (2), 0 (1) |
| 79110 | 388 (106..497) | 268 | 75 | 32 (81), 5 (79), 31 (40), 17 (22), 4 (15), 25 (10), 6 (9), 10 (4), 0 (3), 14 (2), 15 (1), 13 (1), +1 more |
| 79111 | 386 (109..500) | 276 | 75 | 17 (77), 5 (49), 31 (46), 32 (40), 4 (20), 0 (16), 10 (8), 6 (7), 14 (6), 15 (2), 22 (2), 23 (1), +2 more |
| 79115 | 421 (111..531) | 279 | 90 | 5 (119), 31 (36), 32 (26), 0 (24), 10 (22), 6 (17), 4 (11), 19 (10), 15 (7), 25 (3), 14 (2), 17 (1), +1 more |
| 79116 | 411 (114..530) | 286 | 85 | 6 (137), 0 (50), 5 (29), 19 (26), 4 (11), 10 (8), 25 (6), 32 (6), 14 (4), 31 (4), 15 (2), 23 (2), +1 more |
| 79122 | 404 (118..532) | 284 | 82 | 4 (120), 32 (34), 10 (31), 19 (19), 31 (19), 5 (14), 6 (14), 0 (14), 22 (6), 14 (6), 25 (4), 15 (3) |
| 79132 | 391 (120..515) | 266 | 87 | 31 (96), 6 (47), 10 (32), 32 (29), 0 (25), 19 (11), 4 (10), 14 (6), 22 (5), 15 (3), 5 (2) |
| 79128 | 402 (124..527) | 289 | 80 | 0 (128), 4 (47), 6 (33), 10 (23), 19 (17), 22 (13), 14 (12), 31 (10), 15 (6) |
| 79134 | 407 (127..533) | 292 | 79 | 10 (150), 19 (53), 4 (24), 6 (21), 15 (16), 22 (16), 14 (11), 23 (1) |
| 79135 | 409 (129..542) | 277 | 85 | 14 (127), 19 (59), 4 (35), 10 (32), 15 (24) |
| 79139 | 406 (132..537) | 281 | 83 | 14 (94), 19 (93), 15 (70), 4 (22), 22 (2) |
| 79136 | 393 (136..538) | 263 | 81 | 15 (185), 19 (43), 14 (35) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 142/386/831; tracks with internal gaps: 2; total internal gaps: 2; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..526 | 523 | 385 | 384 | 1 | 1 | 1 | 0 | 78899, 78911, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 2 | 80..460 | 381 | 291 | 291 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 3 | 82..467 | 386 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 4 | 86..529 | 444 | 343 | 343 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 88..531 | 444 | 341 | 340 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 89..529 | 441 | 347 | 347 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..444 | 348 | 275 | 275 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 100..454 | 355 | 270 | 270 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 10 | 102..533 | 432 | 336 | 336 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 13 | 106..492 | 387 | 305 | 305 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 108..538 | 431 | 310 | 310 | 0 | 0 | 0 | 0 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 108..537 | 430 | 319 | 319 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..500 | 393 | 309 | 309 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 19 | 116..542 | 427 | 331 | 331 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 117..476 | 360 | 271 | 271 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 21 | 117..429 | 313 | 232 | 232 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 22 | 125..484 | 360 | 291 | 291 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 23 | 137..443 | 307 | 222 | 222 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79111, 79116, 79134 |
| 25 | 137..481 | 345 | 266 | 266 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 177..1007 | 831 | 577 | 577 | 0 | 0 | 0 | 0 | 78911 |
| 31 | 177..515 | 339 | 255 | 255 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 177..496 | 320 | 260 | 260 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 33 | 256..439 | 184 | 133 | 133 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 34 | 309..450 | 142 | 106 | 106 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7082; unmatched reference entries: 3060; unmatched candidate entries: 2
- identity switches: 877; fragmentation (coverage interruptions): 2058; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 5 -> 6 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 4 -> 5 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 5 -> 6 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 5 -> 6 at (2107, 3033), 2 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79045: 6 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 6 -> 8 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 4 -> 5 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 6 -> 8 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 8 -> 9 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 5 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 8 -> 3 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 5 -> 9 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 6 -> 8 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 3 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 8 -> 9 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 9 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 3 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 10 -> 9 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 3 -> 10 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 8 -> 6 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 6 -> 4 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 9 -> 10 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 10 -> 9 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 4 -> 6 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 8 -> 10 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 10 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 9 -> 13 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 5 -> 4 at (2110, 3022.5), 6 frames after previous cover
- f108: ref 78899: 8 -> 17 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 9 -> 8 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 9 -> 13 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 13 -> 9 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79098: 6 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 4 -> 14 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 17 -> 10 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 9 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 9 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 6 -> 17 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 4 -> 6 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 5 -> 4 at (2101.5, 3024.5), 4 frames after previous cover
- f111: ref 78897: 10 -> 13 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 10 -> 8 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 3 -> 2 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 13 -> 3 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 6 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 4 -> 6 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 5 -> 14 at (2113.5, 3026), 1 frames after previous cover
- ... 817 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 698 | 211 | 29 (577), 0 (121) |
| 78896 | 350 (76..429) | 242 | 75 | 21 (213), 2 (29) |
| 78969 | 352 (80..434) | 251 | 67 | 23 (88), 9 (63), 3 (40), 2 (28), 21 (15), 33 (12), 20 (5) |
| 78971 | 352 (84..439) | 238 | 72 | 33 (94), 3 (52), 9 (36), 20 (24), 23 (24), 6 (2), 21 (2), 2 (2), 10 (1), 8 (1) |
| 79045 | 355 (84..443) | 237 | 78 | 8 (100), 23 (63), 3 (27), 9 (15), 20 (11), 2 (6), 33 (6), 6 (2), 21 (2), 4 (1), 5 (1), 10 (1), +2 more |
| 79037 | 355 (86..445) | 236 | 76 | 9 (93), 8 (32), 23 (30), 25 (22), 3 (20), 20 (12), 33 (12), 6 (3), 13 (3), 34 (3), 4 (2), 5 (2), +2 more |
| 78897 | 345 (89..450) | 246 | 67 | 34 (96), 20 (59), 3 (36), 8 (15), 33 (9), 2 (8), 9 (7), 10 (4), 5 (3), 23 (3), 4 (2), 6 (2), +1 more |
| 78899 | 365 (91..455) | 263 | 67 | 3 (92), 8 (61), 9 (36), 20 (22), 2 (15), 25 (12), 34 (6), 23 (4), 13 (3), 6 (3), 4 (2), 5 (2), +3 more |
| 79097 | 366 (94..461) | 250 | 77 | 20 (84), 2 (57), 8 (37), 25 (31), 13 (10), 9 (10), 5 (7), 6 (6), 4 (4), 17 (2), 10 (2) |
| 79098 | 360 (97..467) | 272 | 60 | 2 (135), 3 (42), 8 (16), 25 (16), 13 (14), 6 (12), 5 (12), 17 (10), 20 (5), 4 (4), 9 (3), 22 (3) |
| 79102 | 371 (98..477) | 269 | 71 | 25 (96), 13 (59), 20 (48), 6 (15), 17 (14), 2 (10), 8 (9), 22 (5), 4 (4), 14 (3), 9 (3), 23 (2), +1 more |
| 79103 | 380 (99..481) | 263 | 81 | 13 (118), 25 (55), 22 (51), 17 (11), 5 (9), 8 (4), 6 (3), 10 (3), 9 (3), 4 (2), 23 (2), 32 (1), +1 more |
| 79105 | 379 (101..484) | 272 | 81 | 22 (174), 17 (26), 32 (26), 13 (23), 5 (6), 10 (5), 4 (4), 6 (4), 23 (2), 25 (1), 9 (1) |
| 79108 | 385 (104..492) | 284 | 73 | 17 (145), 13 (70), 32 (17), 22 (11), 6 (10), 25 (9), 10 (7), 5 (5), 31 (4), 4 (3), 14 (2), 0 (1) |
| 79110 | 388 (106..497) | 268 | 75 | 32 (81), 5 (79), 31 (40), 17 (22), 4 (15), 25 (10), 6 (9), 10 (4), 0 (3), 14 (2), 15 (1), 13 (1), +1 more |
| 79111 | 386 (109..500) | 276 | 75 | 17 (77), 5 (49), 31 (46), 32 (40), 4 (20), 0 (16), 10 (8), 6 (7), 14 (6), 15 (2), 22 (2), 23 (1), +2 more |
| 79115 | 421 (111..531) | 279 | 90 | 5 (119), 31 (36), 32 (26), 0 (24), 10 (22), 6 (17), 4 (11), 19 (10), 15 (7), 25 (3), 14 (2), 17 (1), +1 more |
| 79116 | 411 (114..530) | 286 | 85 | 6 (137), 0 (50), 5 (29), 19 (26), 4 (11), 10 (8), 25 (6), 32 (6), 14 (4), 31 (4), 15 (2), 23 (2), +1 more |
| 79122 | 404 (118..532) | 284 | 82 | 4 (120), 32 (34), 10 (31), 19 (19), 31 (19), 5 (14), 6 (14), 0 (14), 22 (6), 14 (6), 25 (4), 15 (3) |
| 79132 | 391 (120..515) | 266 | 87 | 31 (96), 6 (47), 10 (32), 32 (29), 0 (25), 19 (11), 4 (10), 14 (6), 22 (5), 15 (3), 5 (2) |
| 79128 | 402 (124..527) | 289 | 80 | 0 (128), 4 (47), 6 (33), 10 (23), 19 (17), 22 (13), 14 (12), 31 (10), 15 (6) |
| 79134 | 407 (127..533) | 292 | 79 | 10 (150), 19 (53), 4 (24), 6 (21), 15 (16), 22 (16), 14 (11), 23 (1) |
| 79135 | 409 (129..542) | 277 | 85 | 14 (127), 19 (59), 4 (35), 10 (32), 15 (24) |
| 79139 | 406 (132..537) | 281 | 83 | 14 (94), 19 (93), 15 (70), 4 (22), 22 (2) |
| 79136 | 393 (136..538) | 263 | 81 | 15 (185), 19 (43), 14 (35) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 142/386/831; tracks with internal gaps: 2; total internal gaps: 2; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..526 | 523 | 385 | 384 | 1 | 1 | 1 | 0 | 78899, 78911, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 2 | 80..460 | 381 | 291 | 291 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 3 | 82..467 | 386 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 4 | 86..529 | 444 | 343 | 343 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 88..531 | 444 | 341 | 340 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 89..529 | 441 | 347 | 347 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..444 | 348 | 275 | 275 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 100..454 | 355 | 270 | 270 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 10 | 102..533 | 432 | 336 | 336 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 13 | 106..492 | 387 | 305 | 305 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 108..538 | 431 | 310 | 310 | 0 | 0 | 0 | 0 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 108..537 | 430 | 319 | 319 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..500 | 393 | 309 | 309 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 19 | 116..542 | 427 | 331 | 331 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 117..476 | 360 | 271 | 271 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 21 | 117..429 | 313 | 232 | 232 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 22 | 125..484 | 360 | 291 | 291 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 23 | 137..443 | 307 | 222 | 222 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79111, 79116, 79134 |
| 25 | 137..481 | 345 | 266 | 266 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 177..1007 | 831 | 577 | 577 | 0 | 0 | 0 | 0 | 78911 |
| 31 | 177..515 | 339 | 255 | 255 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 177..496 | 320 | 260 | 260 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 33 | 256..439 | 184 | 133 | 133 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 34 | 309..450 | 142 | 106 | 106 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8670; unmatched reference entries: 1472; unmatched candidate entries: 1321
- identity switches: 916; fragmentation (coverage interruptions): 972; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 5 -> 6 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 4 -> 5 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 5 -> 6 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 5 -> 6 at (2107, 3033), 1 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 1 frames after previous cover
- f97: ref 79045: 6 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 6 -> 8 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 4 -> 5 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 6 -> 8 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 8 -> 9 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 5 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 8 -> 3 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 5 -> 9 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 6 -> 8 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 3 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 8 -> 9 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 9 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 3 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 10 -> 9 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 3 -> 10 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 8 -> 6 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 6 -> 4 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 9 -> 10 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 10 -> 9 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 4 -> 6 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 8 -> 10 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 10 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 9 -> 13 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 5 -> 4 at (2110, 3022.5), 5 frames after previous cover
- f108: ref 78899: 8 -> 17 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 9 -> 8 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 9 -> 13 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 13 -> 9 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79098: 6 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 4 -> 14 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 17 -> 10 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 9 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 9 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 6 -> 17 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 4 -> 6 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 5 -> 4 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 10 -> 13 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 10 -> 8 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 3 -> 2 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 13 -> 3 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 6 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 4 -> 6 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 5 -> 14 at (2113.5, 3026), 1 frames after previous cover
- ... 856 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 965 | 29 | 29 (798), 0 (167) |
| 78896 | 350 (76..429) | 300 | 35 | 21 (266), 2 (34) |
| 78969 | 352 (80..434) | 301 | 33 | 23 (115), 9 (76), 3 (46), 2 (30), 21 (15), 33 (12), 20 (7) |
| 78971 | 352 (84..439) | 280 | 43 | 33 (116), 3 (62), 9 (40), 20 (26), 23 (24), 21 (6), 6 (2), 2 (2), 10 (1), 8 (1) |
| 79045 | 355 (84..443) | 285 | 47 | 8 (124), 23 (76), 3 (31), 9 (15), 20 (12), 33 (10), 2 (7), 6 (2), 13 (2), 21 (2), 4 (1), 5 (1), +2 more |
| 79037 | 355 (86..445) | 284 | 49 | 9 (113), 8 (39), 23 (35), 3 (24), 25 (24), 20 (16), 33 (15), 6 (4), 34 (4), 5 (3), 13 (3), 4 (2), +2 more |
| 78897 | 345 (89..450) | 291 | 38 | 34 (117), 20 (67), 3 (40), 8 (16), 9 (13), 33 (10), 2 (9), 5 (4), 10 (4), 23 (4), 4 (3), 6 (2), +1 more |
| 78899 | 365 (91..455) | 309 | 36 | 3 (113), 8 (71), 9 (42), 20 (26), 2 (16), 25 (14), 34 (6), 6 (4), 23 (4), 13 (3), 0 (3), 4 (2), +3 more |
| 79097 | 366 (94..461) | 303 | 44 | 20 (105), 2 (70), 8 (40), 25 (37), 9 (13), 13 (11), 6 (8), 5 (7), 4 (4), 10 (3), 0 (3), 17 (2) |
| 79098 | 360 (97..467) | 309 | 32 | 2 (161), 3 (49), 13 (16), 8 (16), 25 (16), 5 (13), 6 (12), 17 (11), 20 (6), 4 (4), 9 (3), 22 (2) |
| 79102 | 371 (98..477) | 322 | 35 | 25 (122), 13 (69), 20 (56), 17 (16), 6 (15), 2 (13), 8 (11), 4 (6), 22 (5), 14 (3), 9 (3), 23 (2), +1 more |
| 79103 | 380 (99..481) | 313 | 50 | 13 (140), 25 (66), 22 (59), 17 (12), 5 (10), 8 (6), 20 (5), 9 (4), 6 (3), 10 (3), 4 (2), 23 (2), +1 more |
| 79105 | 379 (101..484) | 328 | 38 | 22 (213), 17 (34), 32 (31), 13 (26), 10 (6), 5 (5), 6 (5), 4 (4), 23 (2), 25 (1), 9 (1) |
| 79108 | 385 (104..492) | 332 | 31 | 17 (173), 13 (86), 32 (17), 6 (11), 22 (11), 25 (9), 10 (8), 5 (6), 31 (4), 14 (3), 4 (3), 0 (1) |
| 79110 | 388 (106..497) | 325 | 33 | 5 (101), 32 (99), 31 (47), 17 (29), 4 (15), 25 (12), 6 (9), 10 (4), 0 (3), 14 (2), 22 (2), 15 (1), +1 more |
| 79111 | 386 (109..500) | 327 | 39 | 17 (95), 31 (54), 5 (53), 32 (47), 0 (24), 4 (22), 10 (9), 6 (7), 14 (6), 15 (4), 22 (3), 23 (1), +2 more |
| 79115 | 421 (111..531) | 355 | 38 | 5 (164), 31 (46), 32 (32), 0 (31), 10 (23), 6 (20), 4 (12), 19 (10), 15 (7), 25 (4), 14 (3), 22 (2), +1 more |
| 79116 | 411 (114..530) | 339 | 40 | 6 (172), 0 (56), 5 (32), 19 (27), 4 (14), 10 (12), 32 (7), 25 (6), 14 (4), 31 (4), 15 (2), 23 (2), +1 more |
| 79122 | 404 (118..532) | 345 | 44 | 4 (159), 32 (37), 10 (34), 31 (24), 19 (22), 0 (19), 6 (16), 5 (14), 14 (7), 22 (6), 25 (4), 15 (3) |
| 79132 | 391 (120..515) | 321 | 51 | 31 (128), 6 (61), 32 (34), 10 (32), 0 (27), 19 (11), 4 (10), 22 (6), 14 (6), 15 (4), 5 (2) |
| 79128 | 402 (124..527) | 343 | 40 | 0 (159), 4 (54), 6 (42), 10 (26), 19 (18), 22 (14), 14 (12), 31 (11), 15 (7) |
| 79134 | 407 (127..533) | 357 | 34 | 10 (185), 19 (66), 4 (31), 6 (25), 15 (18), 22 (18), 14 (13), 23 (1) |
| 79135 | 409 (129..542) | 351 | 37 | 14 (155), 19 (78), 4 (47), 10 (45), 15 (26) |
| 79139 | 406 (132..537) | 346 | 46 | 14 (134), 19 (113), 15 (70), 4 (25), 22 (3), 10 (1) |
| 79136 | 393 (136..538) | 339 | 30 | 15 (249), 19 (54), 14 (36) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 171/415/832; tracks with internal gaps: 24; total internal gaps: 490; longest internal gap: 7; tracks ending in coasting: 23 (trailing rows total 638)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..555 | 552 | 552 | 493 | 59 | 24 | 4 | 23 | 78899, 78911, 79097, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 2 | 80..489 | 410 | 410 | 343 | 67 | 24 | 4 | 32 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 3 | 82..496 | 415 | 415 | 365 | 50 | 17 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 4 | 86..558 | 473 | 473 | 420 | 53 | 19 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 88..560 | 473 | 473 | 418 | 55 | 20 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 89..558 | 470 | 470 | 420 | 50 | 16 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..473 | 377 | 377 | 324 | 53 | 18 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 100..483 | 384 | 384 | 323 | 61 | 24 | 5 | 22 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 10 | 102..562 | 461 | 461 | 400 | 61 | 23 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 106..521 | 416 | 416 | 360 | 56 | 21 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 108..567 | 460 | 460 | 384 | 76 | 29 | 5 | 29 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 108..566 | 459 | 459 | 391 | 68 | 26 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..529 | 422 | 422 | 374 | 48 | 15 | 3 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 19 | 116..571 | 456 | 456 | 399 | 57 | 23 | 4 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 117..505 | 389 | 389 | 326 | 63 | 29 | 4 | 24 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 21 | 117..458 | 342 | 342 | 289 | 53 | 22 | 7 | 19 | 78896, 78969, 78971, 79045 |
| 22 | 125..513 | 389 | 389 | 345 | 44 | 14 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 23 | 137..472 | 336 | 336 | 268 | 68 | 25 | 5 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79111, 79116, 79134 |
| 25 | 137..510 | 374 | 374 | 316 | 58 | 21 | 3 | 32 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 177..1008 | 832 | 832 | 798 | 34 | 26 | 3 | 0 | 78911 |
| 31 | 177..544 | 368 | 368 | 318 | 50 | 16 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 177..525 | 349 | 349 | 305 | 44 | 13 | 3 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 33 | 256..468 | 213 | 213 | 163 | 50 | 15 | 6 | 25 | 78897, 78969, 78971, 79037, 79045 |
| 34 | 309..479 | 171 | 171 | 128 | 43 | 10 | 4 | 29 | 78897, 78899, 79037, 79045 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8670; unmatched reference entries: 1472; unmatched candidate entries: 1321
- identity switches: 916; fragmentation (coverage interruptions): 972; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 5 -> 6 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 4 -> 5 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 6 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 5 -> 6 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 5 -> 6 at (2107, 3033), 1 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 1 frames after previous cover
- f97: ref 79045: 6 -> 8 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 6 -> 8 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 4 -> 5 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 6 -> 8 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 4 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 8 -> 9 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 5 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 8 -> 3 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 5 -> 9 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 6 -> 8 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 3 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 8 -> 9 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 9 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 3 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 10 -> 9 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 3 -> 10 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 8 -> 6 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 6 -> 4 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 9 -> 10 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 10 -> 9 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 4 -> 6 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 8 -> 10 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 10 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 9 -> 13 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 5 -> 4 at (2110, 3022.5), 5 frames after previous cover
- f108: ref 78899: 8 -> 17 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 9 -> 8 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 9 -> 13 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 13 -> 9 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79098: 6 -> 4 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 4 -> 14 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 17 -> 10 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 9 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 9 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 6 -> 17 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 4 -> 6 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 5 -> 4 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 10 -> 13 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 10 -> 8 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 3 -> 2 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 13 -> 3 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 6 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 4 -> 6 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 5 -> 14 at (2113.5, 3026), 1 frames after previous cover
- ... 856 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 965 | 29 | 29 (798), 0 (167) |
| 78896 | 350 (76..429) | 300 | 35 | 21 (266), 2 (34) |
| 78969 | 352 (80..434) | 301 | 33 | 23 (115), 9 (76), 3 (46), 2 (30), 21 (15), 33 (12), 20 (7) |
| 78971 | 352 (84..439) | 280 | 43 | 33 (116), 3 (62), 9 (40), 20 (26), 23 (24), 21 (6), 6 (2), 2 (2), 10 (1), 8 (1) |
| 79045 | 355 (84..443) | 285 | 47 | 8 (124), 23 (76), 3 (31), 9 (15), 20 (12), 33 (10), 2 (7), 6 (2), 13 (2), 21 (2), 4 (1), 5 (1), +2 more |
| 79037 | 355 (86..445) | 284 | 49 | 9 (113), 8 (39), 23 (35), 3 (24), 25 (24), 20 (16), 33 (15), 6 (4), 34 (4), 5 (3), 13 (3), 4 (2), +2 more |
| 78897 | 345 (89..450) | 291 | 38 | 34 (117), 20 (67), 3 (40), 8 (16), 9 (13), 33 (10), 2 (9), 5 (4), 10 (4), 23 (4), 4 (3), 6 (2), +1 more |
| 78899 | 365 (91..455) | 309 | 36 | 3 (113), 8 (71), 9 (42), 20 (26), 2 (16), 25 (14), 34 (6), 6 (4), 23 (4), 13 (3), 0 (3), 4 (2), +3 more |
| 79097 | 366 (94..461) | 303 | 44 | 20 (105), 2 (70), 8 (40), 25 (37), 9 (13), 13 (11), 6 (8), 5 (7), 4 (4), 10 (3), 0 (3), 17 (2) |
| 79098 | 360 (97..467) | 309 | 32 | 2 (161), 3 (49), 13 (16), 8 (16), 25 (16), 5 (13), 6 (12), 17 (11), 20 (6), 4 (4), 9 (3), 22 (2) |
| 79102 | 371 (98..477) | 322 | 35 | 25 (122), 13 (69), 20 (56), 17 (16), 6 (15), 2 (13), 8 (11), 4 (6), 22 (5), 14 (3), 9 (3), 23 (2), +1 more |
| 79103 | 380 (99..481) | 313 | 50 | 13 (140), 25 (66), 22 (59), 17 (12), 5 (10), 8 (6), 20 (5), 9 (4), 6 (3), 10 (3), 4 (2), 23 (2), +1 more |
| 79105 | 379 (101..484) | 328 | 38 | 22 (213), 17 (34), 32 (31), 13 (26), 10 (6), 5 (5), 6 (5), 4 (4), 23 (2), 25 (1), 9 (1) |
| 79108 | 385 (104..492) | 332 | 31 | 17 (173), 13 (86), 32 (17), 6 (11), 22 (11), 25 (9), 10 (8), 5 (6), 31 (4), 14 (3), 4 (3), 0 (1) |
| 79110 | 388 (106..497) | 325 | 33 | 5 (101), 32 (99), 31 (47), 17 (29), 4 (15), 25 (12), 6 (9), 10 (4), 0 (3), 14 (2), 22 (2), 15 (1), +1 more |
| 79111 | 386 (109..500) | 327 | 39 | 17 (95), 31 (54), 5 (53), 32 (47), 0 (24), 4 (22), 10 (9), 6 (7), 14 (6), 15 (4), 22 (3), 23 (1), +2 more |
| 79115 | 421 (111..531) | 355 | 38 | 5 (164), 31 (46), 32 (32), 0 (31), 10 (23), 6 (20), 4 (12), 19 (10), 15 (7), 25 (4), 14 (3), 22 (2), +1 more |
| 79116 | 411 (114..530) | 339 | 40 | 6 (172), 0 (56), 5 (32), 19 (27), 4 (14), 10 (12), 32 (7), 25 (6), 14 (4), 31 (4), 15 (2), 23 (2), +1 more |
| 79122 | 404 (118..532) | 345 | 44 | 4 (159), 32 (37), 10 (34), 31 (24), 19 (22), 0 (19), 6 (16), 5 (14), 14 (7), 22 (6), 25 (4), 15 (3) |
| 79132 | 391 (120..515) | 321 | 51 | 31 (128), 6 (61), 32 (34), 10 (32), 0 (27), 19 (11), 4 (10), 22 (6), 14 (6), 15 (4), 5 (2) |
| 79128 | 402 (124..527) | 343 | 40 | 0 (159), 4 (54), 6 (42), 10 (26), 19 (18), 22 (14), 14 (12), 31 (11), 15 (7) |
| 79134 | 407 (127..533) | 357 | 34 | 10 (185), 19 (66), 4 (31), 6 (25), 15 (18), 22 (18), 14 (13), 23 (1) |
| 79135 | 409 (129..542) | 351 | 37 | 14 (155), 19 (78), 4 (47), 10 (45), 15 (26) |
| 79139 | 406 (132..537) | 346 | 46 | 14 (134), 19 (113), 15 (70), 4 (25), 22 (3), 10 (1) |
| 79136 | 393 (136..538) | 339 | 30 | 15 (249), 19 (54), 14 (36) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 171/415/832; tracks with internal gaps: 24; total internal gaps: 490; longest internal gap: 7; tracks ending in coasting: 23 (trailing rows total 638)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..555 | 552 | 552 | 493 | 59 | 24 | 4 | 23 | 78899, 78911, 79097, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 2 | 80..489 | 410 | 410 | 343 | 67 | 24 | 4 | 32 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 3 | 82..496 | 415 | 415 | 365 | 50 | 17 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79098 |
| 4 | 86..558 | 473 | 473 | 420 | 53 | 19 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 88..560 | 473 | 473 | 418 | 55 | 20 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 89..558 | 470 | 470 | 420 | 50 | 16 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..473 | 377 | 377 | 324 | 53 | 18 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 100..483 | 384 | 384 | 323 | 61 | 24 | 5 | 22 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 10 | 102..562 | 461 | 461 | 400 | 61 | 23 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 106..521 | 416 | 416 | 360 | 56 | 21 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 14 | 108..567 | 460 | 460 | 384 | 76 | 29 | 5 | 29 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 108..566 | 459 | 459 | 391 | 68 | 26 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 108..529 | 422 | 422 | 374 | 48 | 15 | 3 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 19 | 116..571 | 456 | 456 | 399 | 57 | 23 | 4 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 117..505 | 389 | 389 | 326 | 63 | 29 | 4 | 24 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 21 | 117..458 | 342 | 342 | 289 | 53 | 22 | 7 | 19 | 78896, 78969, 78971, 79045 |
| 22 | 125..513 | 389 | 389 | 345 | 44 | 14 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 23 | 137..472 | 336 | 336 | 268 | 68 | 25 | 5 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79111, 79116, 79134 |
| 25 | 137..510 | 374 | 374 | 316 | 58 | 21 | 3 | 32 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 29 | 177..1008 | 832 | 832 | 798 | 34 | 26 | 3 | 0 | 78911 |
| 31 | 177..544 | 368 | 368 | 318 | 50 | 16 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 177..525 | 349 | 349 | 305 | 44 | 13 | 3 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 33 | 256..468 | 213 | 213 | 163 | 50 | 15 | 6 | 25 | 78897, 78969, 78971, 79037, 79045 |
| 34 | 309..479 | 171 | 171 | 128 | 43 | 10 | 4 | 29 | 78897, 78899, 79037, 79045 |
