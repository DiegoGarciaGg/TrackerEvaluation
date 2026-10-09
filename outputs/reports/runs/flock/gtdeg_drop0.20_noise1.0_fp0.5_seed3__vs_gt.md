# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=66d3aa4b9bc5
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise1.0_fp0.5_seed3/tracks.csv sha256=f690abe55fc44851
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise1.0_fp0.5_seed3.csv sha256=66d3aa4b9bc5df33
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise1.0_fp0.5_seed3
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
| observations | none | 4 | 0.291 | 0.128 | 0.666 | 1.26 | 0.290 | 1259 | 1630.0 |
| observations | none | 6 | 0.312 | 0.138 | 0.667 | 1.26 | 0.291 | 1254 | 1621.0 |
| observations | none | 8 | 0.323 | 0.144 | 0.668 | 1.30 | 0.295 | 1238 | 1613.0 |
| observations | none | 12 | 0.335 | 0.151 | 0.668 | 1.57 | 0.316 | 1187 | 1589.0 |
| observations | ignore | 4 | 0.291 | 0.128 | 0.666 | 1.26 | 0.290 | 1259 | 1630.0 |
| observations | ignore | 6 | 0.312 | 0.138 | 0.667 | 1.26 | 0.291 | 1254 | 1621.0 |
| observations | ignore | 8 | 0.323 | 0.144 | 0.668 | 1.30 | 0.295 | 1238 | 1613.0 |
| observations | ignore | 12 | 0.335 | 0.151 | 0.668 | 1.57 | 0.316 | 1187 | 1589.0 |
| updates | none | 4 | 0.280 | 0.134 | 0.483 | 1.30 | 0.272 | 1273 | 1509.0 |
| updates | none | 6 | 0.315 | 0.151 | 0.562 | 1.48 | 0.286 | 1265 | 1187.0 |
| updates | none | 8 | 0.334 | 0.161 | 0.633 | 1.73 | 0.303 | 1231 | 902.0 |
| updates | none | 12 | 0.356 | 0.173 | 0.663 | 2.16 | 0.331 | 1152 | 772.0 |
| updates | ignore | 4 | 0.280 | 0.134 | 0.483 | 1.30 | 0.272 | 1273 | 1509.0 |
| updates | ignore | 6 | 0.315 | 0.151 | 0.562 | 1.48 | 0.286 | 1265 | 1187.0 |
| updates | ignore | 8 | 0.334 | 0.161 | 0.633 | 1.73 | 0.303 | 1231 | 902.0 |
| updates | ignore | 12 | 0.356 | 0.173 | 0.663 | 2.16 | 0.331 | 1152 | 772.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 8068; unmatched reference entries: 2074; unmatched candidate entries: 56
- identity switches: 1238; fragmentation (coverage interruptions): 1619; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 42 -> 54 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 49 -> 56 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 53 -> 56 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 56 -> 49 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 53 -> 49 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 52 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 56 -> 42 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 49 -> 54 at (2066, 3034), 4 frames after previous cover
- f98: ref 79037: 52 -> 59 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 56 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 52 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 42 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 42 -> 49 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 49 -> 61 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 49 -> 59 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 59 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 56 -> 49 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 56 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 52 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 61 -> 54 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 54 -> 42 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 53 -> 56 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 61 -> 59 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 54 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 61 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 42 -> 54 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 59 -> 61 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 61 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 60 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 56 -> 49 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 56 -> 66 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 79097: 49 -> 59 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 49 -> 61 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 53 -> 49 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 52 -> 56 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 64 -> 52 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 64 -> 53 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 61 -> 42 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 42 -> 60 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 59 -> 61 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 61 -> 49 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 61 -> 59 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 49 -> 61 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 66 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 49 -> 66 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 52 -> 56 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 53 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 64 -> 53 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 60 -> 74 at (1959.5, 3036), 7 frames after previous cover
- ... 1178 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 809 | 159 | 5 (809) |
| 78896 | 350 (76..429) | 271 | 60 | 65 (126), 93 (36), 86 (35), 120 (28), 193 (18), 102 (9), 42 (7), 54 (7), 60 (3), 88 (2) |
| 78969 | 352 (80..434) | 258 | 67 | 93 (76), 77 (54), 88 (30), 120 (30), 65 (21), 102 (13), 86 (12), 42 (11), 74 (5), 54 (2), 60 (2), 49 (1), +1 more |
| 78971 | 352 (84..439) | 277 | 60 | 120 (113), 77 (46), 88 (37), 54 (35), 86 (22), 49 (8), 65 (8), 93 (4), 42 (3), 102 (1) |
| 79045 | 355 (84..443) | 277 | 56 | 88 (79), 86 (38), 84 (37), 102 (28), 65 (26), 54 (22), 76 (10), 74 (6), 77 (6), 120 (5), 42 (4), 60 (4), +4 more |
| 79037 | 355 (86..445) | 273 | 61 | 88 (98), 86 (39), 102 (26), 93 (26), 84 (20), 76 (15), 54 (12), 60 (7), 74 (6), 52 (4), 59 (4), 42 (4), +5 more |
| 78897 | 345 (89..450) | 266 | 60 | 86 (65), 76 (44), 102 (37), 42 (34), 49 (18), 88 (12), 84 (11), 77 (9), 93 (8), 60 (7), 74 (7), 61 (5), +4 more |
| 78899 | 365 (91..455) | 288 | 61 | 84 (52), 54 (47), 77 (36), 42 (35), 102 (29), 76 (23), 86 (17), 49 (13), 93 (12), 56 (8), 59 (6), 60 (6), +3 more |
| 79097 | 366 (94..461) | 294 | 63 | 54 (84), 76 (40), 42 (37), 86 (33), 77 (30), 84 (18), 49 (11), 56 (10), 60 (6), 102 (6), 105 (6), 74 (5), +5 more |
| 79098 | 360 (97..467) | 291 | 54 | 105 (61), 84 (47), 102 (38), 42 (36), 77 (36), 76 (27), 56 (8), 49 (8), 74 (8), 86 (7), 53 (4), 54 (4), +5 more |
| 79102 | 371 (98..477) | 290 | 66 | 76 (67), 102 (59), 105 (35), 77 (24), 42 (19), 84 (13), 49 (12), 74 (12), 59 (10), 60 (10), 56 (8), 66 (6), +5 more |
| 79103 | 380 (99..481) | 306 | 56 | 170 (69), 76 (44), 105 (35), 77 (26), 74 (25), 84 (21), 54 (18), 42 (13), 93 (12), 56 (11), 53 (6), 66 (6), +6 more |
| 79105 | 379 (101..484) | 298 | 64 | 74 (56), 54 (39), 93 (34), 66 (26), 105 (21), 170 (20), 77 (18), 76 (16), 42 (13), 60 (11), 84 (10), 52 (6), +7 more |
| 79108 | 385 (104..492) | 321 | 59 | 74 (39), 42 (32), 66 (30), 105 (30), 56 (29), 93 (25), 146 (23), 54 (22), 84 (18), 170 (17), 83 (14), 61 (12), +8 more |
| 79110 | 388 (106..497) | 328 | 49 | 74 (81), 56 (44), 49 (36), 54 (29), 146 (26), 83 (22), 93 (19), 88 (17), 84 (14), 59 (11), 66 (7), 105 (6), +8 more |
| 79111 | 386 (109..500) | 306 | 64 | 74 (62), 83 (61), 49 (47), 105 (30), 146 (27), 60 (12), 59 (10), 56 (10), 42 (10), 93 (10), 53 (6), 66 (6), +6 more |
| 79115 | 421 (111..531) | 333 | 71 | 52 (74), 42 (65), 105 (36), 74 (31), 60 (24), 66 (20), 49 (16), 146 (16), 64 (12), 83 (12), 56 (11), 80 (8), +4 more |
| 79116 | 411 (114..530) | 328 | 66 | 80 (71), 83 (60), 60 (50), 64 (46), 61 (43), 52 (17), 49 (12), 66 (10), 42 (5), 74 (4), 146 (4), 59 (3), +2 more |
| 79122 | 404 (118..532) | 305 | 69 | 66 (83), 52 (42), 83 (37), 146 (31), 64 (28), 59 (25), 42 (20), 61 (16), 80 (10), 60 (7), 49 (4), 53 (1), +1 more |
| 79132 | 391 (120..515) | 315 | 60 | 66 (94), 52 (61), 83 (56), 80 (52), 60 (34), 170 (7), 61 (5), 64 (3), 53 (2), 59 (1) |
| 79128 | 402 (124..527) | 334 | 59 | 52 (102), 64 (70), 61 (54), 80 (42), 59 (24), 66 (15), 83 (11), 60 (11), 42 (2), 74 (2), 53 (1) |
| 79134 | 407 (127..533) | 314 | 67 | 61 (103), 59 (54), 60 (50), 52 (42), 66 (24), 202 (16), 64 (10), 83 (6), 80 (6), 53 (2), 42 (1) |
| 79135 | 409 (129..542) | 329 | 58 | 80 (105), 42 (52), 59 (45), 61 (42), 202 (29), 60 (24), 52 (12), 64 (9), 66 (8), 53 (3) |
| 79139 | 406 (132..537) | 339 | 54 | 59 (106), 61 (61), 80 (58), 60 (41), 64 (28), 74 (17), 66 (9), 178 (7), 52 (6), 53 (3), 83 (3) |
| 79136 | 393 (136..538) | 318 | 56 | 64 (143), 178 (64), 202 (43), 60 (30), 53 (21), 61 (5), 66 (3), 59 (3), 74 (3), 42 (2), 80 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 305 | 718..718 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 1/320/1004; tracks with internal gaps: 16; total internal gaps: 34; longest internal gap: 2; tracks ending in coasting: 12 (trailing rows total 20)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 817 | 809 | 8 | 7 | 2 | 0 | 78911 |
| 42 | 78..542 | 465 | 407 | 406 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 49 | 84..321 | 238 | 211 | 207 | 4 | 1 | 1 | 3 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 88..531 | 444 | 383 | 383 | 0 | 0 | 0 | 0 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..162 | 75 | 65 | 64 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..461 | 373 | 331 | 330 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 56 | 91..251 | 161 | 149 | 148 | 1 | 0 | 0 | 1 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 59 | 98..467 | 370 | 320 | 319 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 101..533 | 433 | 355 | 348 | 7 | 6 | 2 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 101..531 | 431 | 369 | 368 | 1 | 1 | 1 | 0 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..530 | 425 | 357 | 354 | 3 | 3 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 107..327 | 221 | 184 | 182 | 2 | 1 | 1 | 1 | 78896, 78969, 78971, 79037, 79045 |
| 66 | 108..515 | 408 | 350 | 348 | 2 | 2 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..538 | 427 | 371 | 371 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79136, 79139 |
| 76 | 115..455 | 341 | 288 | 288 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 77 | 115..434 | 320 | 289 | 288 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 80 | 123..527 | 405 | 359 | 356 | 3 | 3 | 1 | 0 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..479 | 350 | 295 | 294 | 1 | 0 | 0 | 1 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 84 | 131..455 | 325 | 271 | 267 | 4 | 0 | 0 | 4 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 86 | 133..449 | 317 | 269 | 268 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 136..497 | 362 | 290 | 289 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110 |
| 93 | 146..463 | 318 | 270 | 267 | 3 | 2 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 102 | 171..481 | 311 | 251 | 251 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 105 | 178..484 | 307 | 262 | 262 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 120 | 216..450 | 235 | 181 | 179 | 2 | 0 | 0 | 2 | 78896, 78969, 78971, 79037, 79045 |
| 146 | 271..436 | 166 | 130 | 127 | 3 | 1 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 170 | 354..492 | 139 | 118 | 118 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79116, 79132 |
| 178 | 370..457 | 88 | 75 | 71 | 4 | 2 | 1 | 2 | 79136, 79139 |
| 193 | 409..429 | 21 | 18 | 18 | 0 | 0 | 0 | 0 | 78896 |
| 202 | 440..537 | 98 | 88 | 88 | 0 | 0 | 0 | 0 | 79134, 79135, 79136 |
| 305 | 718..718 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 8068; unmatched reference entries: 2074; unmatched candidate entries: 56
- identity switches: 1238; fragmentation (coverage interruptions): 1619; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 42 -> 54 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 49 -> 56 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 53 -> 56 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 56 -> 49 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 53 -> 49 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 52 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 56 -> 42 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 49 -> 54 at (2066, 3034), 4 frames after previous cover
- f98: ref 79037: 52 -> 59 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 56 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 52 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 42 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 42 -> 49 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 49 -> 61 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 49 -> 59 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 59 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 56 -> 49 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 56 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 52 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 61 -> 54 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 54 -> 42 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 53 -> 56 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 61 -> 59 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 54 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 61 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 42 -> 54 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 59 -> 61 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 61 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 60 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 56 -> 49 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 56 -> 66 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 79097: 49 -> 59 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 49 -> 61 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 53 -> 49 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 52 -> 56 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 64 -> 52 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 64 -> 53 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 61 -> 42 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 42 -> 60 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 59 -> 61 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 61 -> 49 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 61 -> 59 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 49 -> 61 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 66 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 49 -> 66 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 52 -> 56 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 53 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 64 -> 53 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 60 -> 74 at (1959.5, 3036), 7 frames after previous cover
- ... 1178 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 809 | 159 | 5 (809) |
| 78896 | 350 (76..429) | 271 | 60 | 65 (126), 93 (36), 86 (35), 120 (28), 193 (18), 102 (9), 42 (7), 54 (7), 60 (3), 88 (2) |
| 78969 | 352 (80..434) | 258 | 67 | 93 (76), 77 (54), 88 (30), 120 (30), 65 (21), 102 (13), 86 (12), 42 (11), 74 (5), 54 (2), 60 (2), 49 (1), +1 more |
| 78971 | 352 (84..439) | 277 | 60 | 120 (113), 77 (46), 88 (37), 54 (35), 86 (22), 49 (8), 65 (8), 93 (4), 42 (3), 102 (1) |
| 79045 | 355 (84..443) | 277 | 56 | 88 (79), 86 (38), 84 (37), 102 (28), 65 (26), 54 (22), 76 (10), 74 (6), 77 (6), 120 (5), 42 (4), 60 (4), +4 more |
| 79037 | 355 (86..445) | 273 | 61 | 88 (98), 86 (39), 102 (26), 93 (26), 84 (20), 76 (15), 54 (12), 60 (7), 74 (6), 52 (4), 59 (4), 42 (4), +5 more |
| 78897 | 345 (89..450) | 266 | 60 | 86 (65), 76 (44), 102 (37), 42 (34), 49 (18), 88 (12), 84 (11), 77 (9), 93 (8), 60 (7), 74 (7), 61 (5), +4 more |
| 78899 | 365 (91..455) | 288 | 61 | 84 (52), 54 (47), 77 (36), 42 (35), 102 (29), 76 (23), 86 (17), 49 (13), 93 (12), 56 (8), 59 (6), 60 (6), +3 more |
| 79097 | 366 (94..461) | 294 | 63 | 54 (84), 76 (40), 42 (37), 86 (33), 77 (30), 84 (18), 49 (11), 56 (10), 60 (6), 102 (6), 105 (6), 74 (5), +5 more |
| 79098 | 360 (97..467) | 291 | 54 | 105 (61), 84 (47), 102 (38), 42 (36), 77 (36), 76 (27), 56 (8), 49 (8), 74 (8), 86 (7), 53 (4), 54 (4), +5 more |
| 79102 | 371 (98..477) | 290 | 66 | 76 (67), 102 (59), 105 (35), 77 (24), 42 (19), 84 (13), 49 (12), 74 (12), 59 (10), 60 (10), 56 (8), 66 (6), +5 more |
| 79103 | 380 (99..481) | 306 | 56 | 170 (69), 76 (44), 105 (35), 77 (26), 74 (25), 84 (21), 54 (18), 42 (13), 93 (12), 56 (11), 53 (6), 66 (6), +6 more |
| 79105 | 379 (101..484) | 298 | 64 | 74 (56), 54 (39), 93 (34), 66 (26), 105 (21), 170 (20), 77 (18), 76 (16), 42 (13), 60 (11), 84 (10), 52 (6), +7 more |
| 79108 | 385 (104..492) | 321 | 59 | 74 (39), 42 (32), 66 (30), 105 (30), 56 (29), 93 (25), 146 (23), 54 (22), 84 (18), 170 (17), 83 (14), 61 (12), +8 more |
| 79110 | 388 (106..497) | 328 | 49 | 74 (81), 56 (44), 49 (36), 54 (29), 146 (26), 83 (22), 93 (19), 88 (17), 84 (14), 59 (11), 66 (7), 105 (6), +8 more |
| 79111 | 386 (109..500) | 306 | 64 | 74 (62), 83 (61), 49 (47), 105 (30), 146 (27), 60 (12), 59 (10), 56 (10), 42 (10), 93 (10), 53 (6), 66 (6), +6 more |
| 79115 | 421 (111..531) | 333 | 71 | 52 (74), 42 (65), 105 (36), 74 (31), 60 (24), 66 (20), 49 (16), 146 (16), 64 (12), 83 (12), 56 (11), 80 (8), +4 more |
| 79116 | 411 (114..530) | 328 | 66 | 80 (71), 83 (60), 60 (50), 64 (46), 61 (43), 52 (17), 49 (12), 66 (10), 42 (5), 74 (4), 146 (4), 59 (3), +2 more |
| 79122 | 404 (118..532) | 305 | 69 | 66 (83), 52 (42), 83 (37), 146 (31), 64 (28), 59 (25), 42 (20), 61 (16), 80 (10), 60 (7), 49 (4), 53 (1), +1 more |
| 79132 | 391 (120..515) | 315 | 60 | 66 (94), 52 (61), 83 (56), 80 (52), 60 (34), 170 (7), 61 (5), 64 (3), 53 (2), 59 (1) |
| 79128 | 402 (124..527) | 334 | 59 | 52 (102), 64 (70), 61 (54), 80 (42), 59 (24), 66 (15), 83 (11), 60 (11), 42 (2), 74 (2), 53 (1) |
| 79134 | 407 (127..533) | 314 | 67 | 61 (103), 59 (54), 60 (50), 52 (42), 66 (24), 202 (16), 64 (10), 83 (6), 80 (6), 53 (2), 42 (1) |
| 79135 | 409 (129..542) | 329 | 58 | 80 (105), 42 (52), 59 (45), 61 (42), 202 (29), 60 (24), 52 (12), 64 (9), 66 (8), 53 (3) |
| 79139 | 406 (132..537) | 339 | 54 | 59 (106), 61 (61), 80 (58), 60 (41), 64 (28), 74 (17), 66 (9), 178 (7), 52 (6), 53 (3), 83 (3) |
| 79136 | 393 (136..538) | 318 | 56 | 64 (143), 178 (64), 202 (43), 60 (30), 53 (21), 61 (5), 66 (3), 59 (3), 74 (3), 42 (2), 80 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 305 | 718..718 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 1/320/1004; tracks with internal gaps: 16; total internal gaps: 34; longest internal gap: 2; tracks ending in coasting: 12 (trailing rows total 20)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 817 | 809 | 8 | 7 | 2 | 0 | 78911 |
| 42 | 78..542 | 465 | 407 | 406 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 49 | 84..321 | 238 | 211 | 207 | 4 | 1 | 1 | 3 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 88..531 | 444 | 383 | 383 | 0 | 0 | 0 | 0 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..162 | 75 | 65 | 64 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..461 | 373 | 331 | 330 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 56 | 91..251 | 161 | 149 | 148 | 1 | 0 | 0 | 1 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 59 | 98..467 | 370 | 320 | 319 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 101..533 | 433 | 355 | 348 | 7 | 6 | 2 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 101..531 | 431 | 369 | 368 | 1 | 1 | 1 | 0 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..530 | 425 | 357 | 354 | 3 | 3 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 107..327 | 221 | 184 | 182 | 2 | 1 | 1 | 1 | 78896, 78969, 78971, 79037, 79045 |
| 66 | 108..515 | 408 | 350 | 348 | 2 | 2 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..538 | 427 | 371 | 371 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79136, 79139 |
| 76 | 115..455 | 341 | 288 | 288 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 77 | 115..434 | 320 | 289 | 288 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 80 | 123..527 | 405 | 359 | 356 | 3 | 3 | 1 | 0 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..479 | 350 | 295 | 294 | 1 | 0 | 0 | 1 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 84 | 131..455 | 325 | 271 | 267 | 4 | 0 | 0 | 4 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 86 | 133..449 | 317 | 269 | 268 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 136..497 | 362 | 290 | 289 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110 |
| 93 | 146..463 | 318 | 270 | 267 | 3 | 2 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 102 | 171..481 | 311 | 251 | 251 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 105 | 178..484 | 307 | 262 | 262 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 120 | 216..450 | 235 | 181 | 179 | 2 | 0 | 0 | 2 | 78896, 78969, 78971, 79037, 79045 |
| 146 | 271..436 | 166 | 130 | 127 | 3 | 1 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 170 | 354..492 | 139 | 118 | 118 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79116, 79132 |
| 178 | 370..457 | 88 | 75 | 71 | 4 | 2 | 1 | 2 | 79136, 79139 |
| 193 | 409..429 | 21 | 18 | 18 | 0 | 0 | 0 | 0 | 78896 |
| 202 | 440..537 | 98 | 88 | 88 | 0 | 0 | 0 | 0 | 79134, 79135, 79136 |
| 305 | 718..718 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 9049; unmatched reference entries: 1093; unmatched candidate entries: 1400
- identity switches: 1231; fragmentation (coverage interruptions): 821; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 42 -> 54 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 49 -> 56 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 53 -> 56 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 56 -> 49 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 53 -> 49 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 52 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 56 -> 42 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 49 -> 54 at (2066, 3034), 3 frames after previous cover
- f98: ref 79037: 52 -> 59 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 56 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 52 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 42 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 42 -> 49 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 49 -> 61 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 49 -> 59 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 59 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 56 -> 49 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 56 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 52 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 61 -> 54 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 54 -> 42 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 53 -> 56 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 61 -> 59 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 54 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 61 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 42 -> 54 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 59 -> 61 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 61 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 60 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 56 -> 49 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 56 -> 66 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79097: 49 -> 59 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 49 -> 61 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 53 -> 49 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 52 -> 56 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 64 -> 52 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 64 -> 53 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 61 -> 42 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 42 -> 60 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 59 -> 61 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 61 -> 49 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 61 -> 59 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 49 -> 61 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 66 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 49 -> 66 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 52 -> 56 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 53 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 64 -> 53 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 60 -> 74 at (1959.5, 3036), 7 frames after previous cover
- ... 1171 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 980 | 17 | 5 (980) |
| 78896 | 350 (76..429) | 307 | 29 | 65 (142), 93 (39), 86 (39), 120 (34), 193 (21), 102 (11), 54 (9), 42 (7), 60 (3), 88 (2) |
| 78969 | 352 (80..434) | 301 | 31 | 93 (86), 77 (60), 120 (38), 88 (35), 65 (23), 102 (19), 86 (17), 42 (11), 74 (6), 54 (2), 60 (2), 49 (1), +1 more |
| 78971 | 352 (84..439) | 307 | 36 | 120 (127), 77 (50), 88 (44), 54 (37), 86 (22), 49 (9), 65 (9), 42 (4), 93 (4), 102 (1) |
| 79045 | 355 (84..443) | 304 | 37 | 88 (87), 86 (41), 84 (40), 102 (31), 65 (28), 54 (23), 76 (12), 77 (10), 74 (6), 120 (6), 42 (4), 60 (4), +4 more |
| 79037 | 355 (86..445) | 312 | 32 | 88 (113), 86 (46), 102 (30), 93 (29), 84 (23), 76 (19), 54 (13), 60 (7), 74 (7), 42 (5), 52 (4), 59 (4), +5 more |
| 78897 | 345 (89..450) | 293 | 41 | 86 (71), 76 (49), 102 (41), 42 (35), 49 (23), 88 (12), 84 (12), 93 (10), 77 (9), 60 (8), 74 (8), 61 (5), +4 more |
| 78899 | 365 (91..455) | 310 | 44 | 84 (59), 54 (49), 77 (39), 42 (36), 102 (32), 76 (27), 86 (17), 49 (13), 93 (12), 56 (9), 59 (7), 60 (6), +3 more |
| 79097 | 366 (94..461) | 324 | 36 | 54 (97), 76 (44), 42 (41), 86 (38), 77 (31), 84 (19), 49 (11), 56 (10), 60 (6), 74 (6), 102 (6), 105 (6), +5 more |
| 79098 | 360 (97..467) | 316 | 35 | 105 (71), 84 (53), 102 (42), 77 (39), 42 (36), 76 (27), 49 (9), 56 (8), 74 (8), 86 (7), 53 (4), 54 (4), +5 more |
| 79102 | 371 (98..477) | 322 | 39 | 76 (74), 102 (68), 105 (38), 77 (29), 42 (19), 84 (15), 49 (14), 74 (13), 60 (10), 56 (9), 59 (9), 66 (7), +5 more |
| 79103 | 380 (99..481) | 334 | 38 | 170 (78), 76 (49), 105 (41), 77 (27), 74 (25), 84 (22), 54 (19), 42 (15), 93 (12), 56 (11), 53 (6), 66 (6), +6 more |
| 79105 | 379 (101..484) | 331 | 36 | 74 (61), 54 (43), 93 (41), 66 (28), 105 (23), 170 (23), 77 (20), 76 (19), 42 (14), 60 (11), 84 (11), 49 (7), +7 more |
| 79108 | 385 (104..492) | 352 | 29 | 42 (42), 74 (40), 105 (34), 66 (33), 56 (29), 54 (26), 146 (26), 93 (25), 84 (19), 170 (18), 83 (15), 61 (12), +8 more |
| 79110 | 388 (106..497) | 354 | 28 | 74 (84), 56 (46), 49 (40), 54 (32), 146 (27), 83 (25), 93 (20), 88 (20), 84 (14), 59 (12), 66 (8), 105 (7), +8 more |
| 79111 | 386 (109..500) | 345 | 31 | 74 (73), 83 (67), 49 (52), 105 (32), 146 (29), 60 (15), 42 (14), 93 (13), 59 (11), 56 (11), 53 (8), 66 (5), +6 more |
| 79115 | 421 (111..531) | 368 | 38 | 52 (80), 42 (72), 105 (41), 74 (36), 60 (23), 66 (21), 49 (17), 83 (17), 146 (17), 64 (11), 56 (11), 80 (8), +4 more |
| 79116 | 411 (114..530) | 361 | 42 | 80 (74), 83 (64), 60 (59), 64 (52), 61 (50), 52 (18), 49 (12), 66 (10), 74 (6), 42 (6), 146 (4), 59 (3), +2 more |
| 79122 | 404 (118..532) | 348 | 37 | 66 (97), 52 (57), 83 (41), 146 (32), 59 (31), 64 (29), 42 (23), 61 (12), 80 (10), 60 (9), 49 (4), 74 (2), +1 more |
| 79132 | 391 (120..515) | 356 | 29 | 66 (111), 52 (70), 83 (59), 80 (55), 60 (40), 170 (10), 61 (5), 64 (3), 53 (2), 59 (1) |
| 79128 | 402 (124..527) | 374 | 25 | 52 (112), 64 (83), 61 (60), 80 (48), 59 (24), 66 (15), 83 (13), 60 (12), 74 (4), 42 (2), 53 (1) |
| 79134 | 407 (127..533) | 353 | 33 | 61 (116), 59 (63), 60 (58), 52 (47), 66 (25), 202 (17), 64 (11), 83 (7), 80 (6), 53 (2), 42 (1) |
| 79135 | 409 (129..542) | 369 | 26 | 80 (120), 42 (56), 61 (49), 59 (48), 202 (34), 60 (26), 52 (13), 64 (11), 66 (9), 53 (3) |
| 79139 | 406 (132..537) | 372 | 26 | 59 (125), 61 (67), 80 (59), 60 (42), 64 (30), 74 (19), 66 (10), 178 (7), 52 (6), 83 (4), 53 (3) |
| 79136 | 393 (136..538) | 356 | 26 | 64 (158), 178 (73), 202 (47), 60 (32), 53 (26), 61 (6), 42 (4), 66 (3), 59 (3), 74 (3), 80 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 305 | 718..747 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 30/349/1004; tracks with internal gaps: 29; total internal gaps: 329; longest internal gap: 20; tracks ending in coasting: 30 (trailing rows total 931)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 1004 | 980 | 24 | 17 | 3 | 0 | 78911 |
| 42 | 78..571 | 494 | 494 | 450 | 44 | 12 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 49 | 84..350 | 267 | 267 | 229 | 38 | 4 | 1 | 34 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 88..560 | 473 | 473 | 431 | 42 | 10 | 2 | 29 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..191 | 104 | 104 | 73 | 31 | 1 | 1 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..490 | 402 | 402 | 363 | 39 | 9 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 56 | 91..280 | 190 | 190 | 154 | 36 | 6 | 1 | 30 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 59 | 98..496 | 399 | 399 | 359 | 40 | 9 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 101..562 | 462 | 462 | 384 | 78 | 18 | 14 | 29 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 101..560 | 460 | 460 | 410 | 50 | 15 | 3 | 28 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..559 | 454 | 454 | 393 | 61 | 20 | 6 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 107..356 | 250 | 250 | 203 | 47 | 11 | 4 | 30 | 78896, 78969, 78971, 79037, 79045 |
| 66 | 108..544 | 437 | 437 | 389 | 48 | 17 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..567 | 456 | 456 | 408 | 48 | 13 | 2 | 30 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79136, 79139 |
| 76 | 115..484 | 370 | 370 | 322 | 48 | 17 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 77 | 115..463 | 349 | 349 | 317 | 32 | 7 | 6 | 20 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 80 | 123..556 | 434 | 434 | 383 | 51 | 14 | 5 | 29 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..508 | 379 | 379 | 325 | 54 | 18 | 3 | 31 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 84 | 131..484 | 354 | 354 | 293 | 61 | 11 | 2 | 48 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 86 | 133..478 | 346 | 346 | 298 | 48 | 19 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 136..526 | 391 | 391 | 328 | 63 | 10 | 20 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110 |
| 93 | 146..492 | 347 | 347 | 296 | 51 | 15 | 4 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 102 | 171..510 | 340 | 340 | 288 | 52 | 18 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 105 | 178..513 | 336 | 336 | 295 | 41 | 12 | 1 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 120 | 216..479 | 264 | 264 | 208 | 56 | 13 | 2 | 40 | 78896, 78969, 78971, 79037, 79045 |
| 146 | 271..465 | 195 | 195 | 135 | 60 | 5 | 2 | 54 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 170 | 354..521 | 168 | 168 | 136 | 32 | 3 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79116, 79132 |
| 178 | 370..486 | 117 | 117 | 80 | 37 | 4 | 1 | 33 | 79136, 79139 |
| 193 | 409..458 | 50 | 50 | 21 | 29 | 0 | 0 | 29 | 78896 |
| 202 | 440..566 | 127 | 127 | 98 | 29 | 1 | 1 | 28 | 79134, 79135, 79136 |
| 305 | 718..747 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 9049; unmatched reference entries: 1093; unmatched candidate entries: 1400
- identity switches: 1231; fragmentation (coverage interruptions): 821; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 42 -> 54 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 49 -> 56 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 53 -> 56 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 56 -> 49 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 53 -> 49 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 52 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 56 -> 42 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 49 -> 54 at (2066, 3034), 3 frames after previous cover
- f98: ref 79037: 52 -> 59 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 56 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 52 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 42 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 42 -> 49 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 49 -> 61 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 49 -> 59 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 59 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 56 -> 49 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 56 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 52 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 61 -> 54 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 54 -> 42 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 53 -> 56 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 52 -> 53 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 61 -> 59 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 54 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 61 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 42 -> 54 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 59 -> 61 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 61 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 60 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 56 -> 49 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 56 -> 66 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79097: 49 -> 59 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 49 -> 61 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 53 -> 49 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 52 -> 56 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 64 -> 52 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 64 -> 53 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 61 -> 42 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 42 -> 60 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 59 -> 61 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 61 -> 49 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 61 -> 59 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 49 -> 61 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 66 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 49 -> 66 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 52 -> 56 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 53 -> 52 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 64 -> 53 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 60 -> 74 at (1959.5, 3036), 7 frames after previous cover
- ... 1171 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 980 | 17 | 5 (980) |
| 78896 | 350 (76..429) | 307 | 29 | 65 (142), 93 (39), 86 (39), 120 (34), 193 (21), 102 (11), 54 (9), 42 (7), 60 (3), 88 (2) |
| 78969 | 352 (80..434) | 301 | 31 | 93 (86), 77 (60), 120 (38), 88 (35), 65 (23), 102 (19), 86 (17), 42 (11), 74 (6), 54 (2), 60 (2), 49 (1), +1 more |
| 78971 | 352 (84..439) | 307 | 36 | 120 (127), 77 (50), 88 (44), 54 (37), 86 (22), 49 (9), 65 (9), 42 (4), 93 (4), 102 (1) |
| 79045 | 355 (84..443) | 304 | 37 | 88 (87), 86 (41), 84 (40), 102 (31), 65 (28), 54 (23), 76 (12), 77 (10), 74 (6), 120 (6), 42 (4), 60 (4), +4 more |
| 79037 | 355 (86..445) | 312 | 32 | 88 (113), 86 (46), 102 (30), 93 (29), 84 (23), 76 (19), 54 (13), 60 (7), 74 (7), 42 (5), 52 (4), 59 (4), +5 more |
| 78897 | 345 (89..450) | 293 | 41 | 86 (71), 76 (49), 102 (41), 42 (35), 49 (23), 88 (12), 84 (12), 93 (10), 77 (9), 60 (8), 74 (8), 61 (5), +4 more |
| 78899 | 365 (91..455) | 310 | 44 | 84 (59), 54 (49), 77 (39), 42 (36), 102 (32), 76 (27), 86 (17), 49 (13), 93 (12), 56 (9), 59 (7), 60 (6), +3 more |
| 79097 | 366 (94..461) | 324 | 36 | 54 (97), 76 (44), 42 (41), 86 (38), 77 (31), 84 (19), 49 (11), 56 (10), 60 (6), 74 (6), 102 (6), 105 (6), +5 more |
| 79098 | 360 (97..467) | 316 | 35 | 105 (71), 84 (53), 102 (42), 77 (39), 42 (36), 76 (27), 49 (9), 56 (8), 74 (8), 86 (7), 53 (4), 54 (4), +5 more |
| 79102 | 371 (98..477) | 322 | 39 | 76 (74), 102 (68), 105 (38), 77 (29), 42 (19), 84 (15), 49 (14), 74 (13), 60 (10), 56 (9), 59 (9), 66 (7), +5 more |
| 79103 | 380 (99..481) | 334 | 38 | 170 (78), 76 (49), 105 (41), 77 (27), 74 (25), 84 (22), 54 (19), 42 (15), 93 (12), 56 (11), 53 (6), 66 (6), +6 more |
| 79105 | 379 (101..484) | 331 | 36 | 74 (61), 54 (43), 93 (41), 66 (28), 105 (23), 170 (23), 77 (20), 76 (19), 42 (14), 60 (11), 84 (11), 49 (7), +7 more |
| 79108 | 385 (104..492) | 352 | 29 | 42 (42), 74 (40), 105 (34), 66 (33), 56 (29), 54 (26), 146 (26), 93 (25), 84 (19), 170 (18), 83 (15), 61 (12), +8 more |
| 79110 | 388 (106..497) | 354 | 28 | 74 (84), 56 (46), 49 (40), 54 (32), 146 (27), 83 (25), 93 (20), 88 (20), 84 (14), 59 (12), 66 (8), 105 (7), +8 more |
| 79111 | 386 (109..500) | 345 | 31 | 74 (73), 83 (67), 49 (52), 105 (32), 146 (29), 60 (15), 42 (14), 93 (13), 59 (11), 56 (11), 53 (8), 66 (5), +6 more |
| 79115 | 421 (111..531) | 368 | 38 | 52 (80), 42 (72), 105 (41), 74 (36), 60 (23), 66 (21), 49 (17), 83 (17), 146 (17), 64 (11), 56 (11), 80 (8), +4 more |
| 79116 | 411 (114..530) | 361 | 42 | 80 (74), 83 (64), 60 (59), 64 (52), 61 (50), 52 (18), 49 (12), 66 (10), 74 (6), 42 (6), 146 (4), 59 (3), +2 more |
| 79122 | 404 (118..532) | 348 | 37 | 66 (97), 52 (57), 83 (41), 146 (32), 59 (31), 64 (29), 42 (23), 61 (12), 80 (10), 60 (9), 49 (4), 74 (2), +1 more |
| 79132 | 391 (120..515) | 356 | 29 | 66 (111), 52 (70), 83 (59), 80 (55), 60 (40), 170 (10), 61 (5), 64 (3), 53 (2), 59 (1) |
| 79128 | 402 (124..527) | 374 | 25 | 52 (112), 64 (83), 61 (60), 80 (48), 59 (24), 66 (15), 83 (13), 60 (12), 74 (4), 42 (2), 53 (1) |
| 79134 | 407 (127..533) | 353 | 33 | 61 (116), 59 (63), 60 (58), 52 (47), 66 (25), 202 (17), 64 (11), 83 (7), 80 (6), 53 (2), 42 (1) |
| 79135 | 409 (129..542) | 369 | 26 | 80 (120), 42 (56), 61 (49), 59 (48), 202 (34), 60 (26), 52 (13), 64 (11), 66 (9), 53 (3) |
| 79139 | 406 (132..537) | 372 | 26 | 59 (125), 61 (67), 80 (59), 60 (42), 64 (30), 74 (19), 66 (10), 178 (7), 52 (6), 83 (4), 53 (3) |
| 79136 | 393 (136..538) | 356 | 26 | 64 (158), 178 (73), 202 (47), 60 (32), 53 (26), 61 (6), 42 (4), 66 (3), 59 (3), 74 (3), 80 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 305 | 718..747 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 30/349/1004; tracks with internal gaps: 29; total internal gaps: 329; longest internal gap: 20; tracks ending in coasting: 30 (trailing rows total 931)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 1004 | 980 | 24 | 17 | 3 | 0 | 78911 |
| 42 | 78..571 | 494 | 494 | 450 | 44 | 12 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 49 | 84..350 | 267 | 267 | 229 | 38 | 4 | 1 | 34 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 52 | 88..560 | 473 | 473 | 431 | 42 | 10 | 2 | 29 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..191 | 104 | 104 | 73 | 31 | 1 | 1 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..490 | 402 | 402 | 363 | 39 | 9 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 56 | 91..280 | 190 | 190 | 154 | 36 | 6 | 1 | 30 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 59 | 98..496 | 399 | 399 | 359 | 40 | 9 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 101..562 | 462 | 462 | 384 | 78 | 18 | 14 | 29 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 101..560 | 460 | 460 | 410 | 50 | 15 | 3 | 28 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..559 | 454 | 454 | 393 | 61 | 20 | 6 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 107..356 | 250 | 250 | 203 | 47 | 11 | 4 | 30 | 78896, 78969, 78971, 79037, 79045 |
| 66 | 108..544 | 437 | 437 | 389 | 48 | 17 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..567 | 456 | 456 | 408 | 48 | 13 | 2 | 30 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79136, 79139 |
| 76 | 115..484 | 370 | 370 | 322 | 48 | 17 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 77 | 115..463 | 349 | 349 | 317 | 32 | 7 | 6 | 20 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 80 | 123..556 | 434 | 434 | 383 | 51 | 14 | 5 | 29 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..508 | 379 | 379 | 325 | 54 | 18 | 3 | 31 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 84 | 131..484 | 354 | 354 | 293 | 61 | 11 | 2 | 48 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 86 | 133..478 | 346 | 346 | 298 | 48 | 19 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 136..526 | 391 | 391 | 328 | 63 | 10 | 20 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79105, 79108, 79110 |
| 93 | 146..492 | 347 | 347 | 296 | 51 | 15 | 4 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111 |
| 102 | 171..510 | 340 | 340 | 288 | 52 | 18 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 105 | 178..513 | 336 | 336 | 295 | 41 | 12 | 1 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 120 | 216..479 | 264 | 264 | 208 | 56 | 13 | 2 | 40 | 78896, 78969, 78971, 79037, 79045 |
| 146 | 271..465 | 195 | 195 | 135 | 60 | 5 | 2 | 54 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 170 | 354..521 | 168 | 168 | 136 | 32 | 3 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79116, 79132 |
| 178 | 370..486 | 117 | 117 | 80 | 37 | 4 | 1 | 33 | 79136, 79139 |
| 193 | 409..458 | 50 | 50 | 21 | 29 | 0 | 0 | 29 | 78896 |
| 202 | 440..566 | 127 | 127 | 98 | 29 | 1 | 1 | 28 | 79134, 79135, 79136 |
| 305 | 718..747 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
