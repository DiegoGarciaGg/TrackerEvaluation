# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=0613302d190b
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise0.0_fp0.5_seed3/tracks.csv sha256=2e4bdb0e900b7f32
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise0.0_fp0.5_seed3.csv sha256=0613302d190b6253
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise0.0_fp0.5_seed3
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
| observations | none | 4 | 0.298 | 0.130 | 0.549 | 0.01 | 0.268 | 1360 | 2122.0 |
| observations | none | 6 | 0.298 | 0.130 | 0.549 | 0.01 | 0.269 | 1362 | 2122.0 |
| observations | none | 8 | 0.298 | 0.131 | 0.551 | 0.04 | 0.269 | 1347 | 2116.0 |
| observations | none | 12 | 0.298 | 0.133 | 0.558 | 0.41 | 0.275 | 1257 | 2063.0 |
| observations | ignore | 4 | 0.298 | 0.130 | 0.549 | 0.01 | 0.268 | 1360 | 2122.0 |
| observations | ignore | 6 | 0.298 | 0.130 | 0.549 | 0.01 | 0.269 | 1362 | 2122.0 |
| observations | ignore | 8 | 0.298 | 0.131 | 0.551 | 0.04 | 0.269 | 1347 | 2116.0 |
| observations | ignore | 12 | 0.298 | 0.133 | 0.558 | 0.41 | 0.275 | 1257 | 2063.0 |
| updates | none | 4 | 0.287 | 0.139 | 0.321 | 0.13 | 0.254 | 1394 | 2014.0 |
| updates | none | 6 | 0.311 | 0.151 | 0.434 | 0.51 | 0.280 | 1402 | 1594.0 |
| updates | none | 8 | 0.325 | 0.159 | 0.549 | 0.98 | 0.299 | 1367 | 1195.0 |
| updates | none | 12 | 0.341 | 0.169 | 0.592 | 1.50 | 0.314 | 1258 | 1014.0 |
| updates | ignore | 4 | 0.287 | 0.139 | 0.321 | 0.13 | 0.254 | 1394 | 2014.0 |
| updates | ignore | 6 | 0.311 | 0.151 | 0.434 | 0.51 | 0.280 | 1402 | 1594.0 |
| updates | ignore | 8 | 0.325 | 0.159 | 0.549 | 0.98 | 0.299 | 1367 | 1195.0 |
| updates | ignore | 12 | 0.341 | 0.169 | 0.592 | 1.50 | 0.314 | 1258 | 1014.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 6983; unmatched reference entries: 3159; unmatched candidate entries: 50
- identity switches: 1347; fragmentation (coverage interruptions): 2157; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 47 -> 44 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 44 -> 47 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 47 -> 44 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 44 -> 49 at (2090.5, 3033), 4 frames after previous cover
- f87: ref 79037: 47 -> 44 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 78971: 44 -> 51 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79045: 44 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 44 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 47 -> 50 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 50 -> 47 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 51 -> 47 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 47 -> 50 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 50 -> 51 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 47 -> 51 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 44 -> 50 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 47 -> 49 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 51 -> 47 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 50 -> 54 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 50 -> 54 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 54 -> 49 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 44 -> 50 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 49 -> 57 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 50 -> 55 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 49 -> 47 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 47 -> 49 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 44 -> 50 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 47 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 49 -> 51 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 51 -> 49 at (2061, 3032.5), 2 frames after previous cover
- f101: ref 79097: 50 -> 55 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 44 -> 50 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 54 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 47 -> 54 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 50 -> 49 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 55 -> 51 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 51 -> 54 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 50 -> 55 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 44 -> 60 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 49 -> 51 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 51 -> 50 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 54 -> 49 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 50 -> 60 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 49 -> 51 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 55 -> 50 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 51 -> 49 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 55 -> 60 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 60 -> 55 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 51 -> 49 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 51 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 49 -> 54 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 60 -> 65 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 55 -> 60 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 44 -> 55 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 65 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 60 -> 65 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78969: 47 -> 57 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 78971: 54 -> 47 at (1996.5, 3034.5), 4 frames after previous cover
- f109: ref 79037: 49 -> 54 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 60 -> 50 at (2097, 3024.5), 1 frames after previous cover
- ... 1287 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 696 | 218 | 10 (696) |
| 78896 | 350 (76..429) | 252 | 70 | 57 (89), 51 (45), 44 (38), 85 (34), 54 (29), 49 (7), 76 (5), 113 (4), 47 (1) |
| 78969 | 352 (80..434) | 240 | 71 | 85 (76), 76 (66), 113 (26), 84 (19), 57 (14), 44 (13), 47 (10), 51 (6), 54 (3), 106 (3), 50 (2), 49 (2) |
| 78971 | 352 (84..439) | 247 | 67 | 85 (55), 44 (45), 106 (38), 113 (28), 51 (18), 54 (15), 84 (15), 47 (11), 90 (10), 76 (6), 57 (5), 49 (1) |
| 79045 | 355 (84..443) | 242 | 78 | 84 (50), 51 (31), 54 (31), 85 (27), 90 (24), 126 (15), 50 (13), 57 (11), 106 (11), 44 (8), 76 (8), 47 (7), +2 more |
| 79037 | 355 (86..445) | 245 | 75 | 126 (37), 51 (36), 57 (31), 84 (27), 85 (23), 182 (20), 50 (19), 106 (12), 54 (10), 90 (10), 44 (6), 49 (4), +4 more |
| 78897 | 345 (89..450) | 235 | 83 | 126 (74), 84 (46), 51 (20), 106 (15), 57 (12), 50 (9), 87 (9), 85 (8), 71 (7), 54 (6), 60 (6), 113 (6), +7 more |
| 78899 | 365 (91..455) | 238 | 81 | 84 (56), 126 (42), 50 (28), 113 (23), 49 (16), 71 (15), 106 (14), 57 (10), 51 (7), 54 (6), 44 (4), 60 (4), +7 more |
| 79097 | 366 (94..461) | 242 | 83 | 76 (40), 106 (39), 113 (29), 71 (27), 50 (24), 49 (16), 84 (16), 44 (12), 54 (11), 90 (4), 126 (4), 82 (3), +8 more |
| 79098 | 360 (97..467) | 237 | 83 | 50 (29), 76 (28), 44 (25), 71 (24), 106 (19), 51 (18), 113 (13), 57 (12), 54 (11), 84 (11), 126 (8), 142 (7), +10 more |
| 79102 | 371 (98..477) | 252 | 89 | 106 (39), 50 (30), 113 (25), 44 (24), 57 (19), 142 (17), 182 (14), 49 (13), 76 (10), 87 (8), 90 (8), 91 (7), +10 more |
| 79103 | 380 (99..481) | 257 | 82 | 44 (44), 142 (43), 87 (31), 54 (23), 113 (19), 60 (15), 65 (11), 49 (11), 71 (11), 50 (9), 76 (8), 68 (8), +10 more |
| 79105 | 379 (101..484) | 257 | 76 | 87 (47), 142 (34), 86 (21), 44 (20), 50 (19), 60 (18), 47 (18), 49 (12), 68 (8), 182 (8), 106 (8), 65 (7), +11 more |
| 79108 | 385 (104..492) | 269 | 73 | 44 (76), 142 (31), 87 (26), 60 (19), 50 (15), 86 (13), 76 (13), 91 (12), 113 (11), 49 (10), 47 (9), 51 (8), +10 more |
| 79110 | 388 (106..497) | 269 | 76 | 60 (74), 47 (29), 50 (22), 142 (22), 87 (13), 68 (12), 76 (12), 51 (12), 65 (11), 106 (11), 91 (9), 49 (9), +10 more |
| 79111 | 386 (109..500) | 274 | 80 | 193 (54), 49 (33), 60 (32), 142 (22), 47 (20), 68 (19), 54 (18), 50 (17), 65 (16), 87 (14), 51 (7), 72 (5), +6 more |
| 79115 | 421 (111..531) | 291 | 89 | 149 (76), 60 (31), 47 (29), 51 (26), 54 (23), 82 (21), 65 (16), 55 (15), 87 (15), 76 (14), 68 (10), 50 (8), +4 more |
| 79116 | 411 (114..530) | 278 | 91 | 82 (106), 60 (32), 47 (18), 76 (17), 149 (16), 54 (14), 68 (13), 87 (13), 55 (12), 86 (12), 50 (7), 90 (4), +7 more |
| 79122 | 404 (118..532) | 265 | 91 | 49 (84), 82 (43), 60 (34), 47 (19), 50 (18), 54 (13), 149 (13), 87 (10), 68 (6), 90 (5), 76 (5), 51 (5), +5 more |
| 79132 | 391 (120..515) | 275 | 81 | 51 (88), 60 (40), 68 (27), 54 (22), 76 (22), 82 (21), 149 (13), 50 (8), 87 (8), 49 (6), 55 (4), 65 (4), +3 more |
| 79128 | 402 (124..527) | 279 | 86 | 47 (76), 68 (44), 149 (35), 54 (28), 82 (25), 49 (17), 60 (16), 65 (10), 50 (9), 87 (8), 72 (4), 76 (4), +2 more |
| 79134 | 407 (127..533) | 291 | 86 | 55 (80), 49 (54), 87 (33), 47 (32), 68 (29), 82 (17), 54 (14), 149 (13), 65 (8), 50 (6), 72 (4), 201 (1) |
| 79135 | 409 (129..542) | 285 | 87 | 201 (76), 82 (55), 68 (37), 47 (33), 55 (27), 193 (15), 87 (13), 65 (12), 49 (11), 149 (5), 50 (1) |
| 79139 | 406 (132..537) | 286 | 88 | 68 (102), 55 (84), 82 (35), 65 (21), 47 (19), 49 (10), 179 (8), 201 (4), 72 (3) |
| 79136 | 393 (136..538) | 281 | 73 | 179 (134), 55 (74), 65 (54), 49 (16), 201 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 52/286/995; tracks with internal gaps: 12; total internal gaps: 27; longest internal gap: 2; tracks ending in coasting: 12 (trailing rows total 21)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 12..1006 | 995 | 711 | 696 | 15 | 15 | 1 | 0 | 78911 |
| 44 | 81..492 | 412 | 330 | 330 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 47 | 84..515 | 432 | 354 | 349 | 5 | 2 | 1 | 3 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 49 | 87..533 | 447 | 348 | 347 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 88..466 | 379 | 295 | 293 | 2 | 0 | 0 | 2 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 51 | 88..515 | 428 | 340 | 338 | 2 | 1 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 54 | 97..481 | 385 | 299 | 299 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 55 | 99..530 | 432 | 317 | 315 | 2 | 1 | 2 | 0 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 99..381 | 283 | 215 | 213 | 2 | 0 | 0 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 60 | 103..495 | 393 | 332 | 331 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..361 | 255 | 185 | 182 | 3 | 1 | 1 | 2 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 113..535 | 423 | 323 | 320 | 3 | 1 | 1 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 71 | 116..240 | 125 | 96 | 94 | 2 | 0 | 0 | 2 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 72 | 116..167 | 52 | 31 | 29 | 2 | 0 | 0 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 76 | 120..467 | 348 | 272 | 271 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 129..530 | 402 | 336 | 336 | 0 | 0 | 0 | 0 | 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 84 | 129..434 | 306 | 240 | 240 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 132..427 | 296 | 223 | 223 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 135..203 | 69 | 59 | 58 | 1 | 0 | 0 | 1 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 87 | 135..459 | 325 | 255 | 254 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 90 | 141..253 | 113 | 94 | 93 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132 |
| 91 | 141..198 | 58 | 44 | 42 | 2 | 0 | 0 | 2 | 79097, 79098, 79102, 79105, 79108, 79110 |
| 106 | 192..477 | 286 | 219 | 218 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 113 | 200..438 | 239 | 195 | 194 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 126 | 224..460 | 237 | 187 | 187 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 142 | 269..484 | 216 | 186 | 186 | 0 | 0 | 0 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 149 | 291..531 | 241 | 171 | 171 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 179 | 363..537 | 175 | 142 | 142 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 182 | 371..445 | 75 | 60 | 60 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108 |
| 193 | 404..544 | 141 | 86 | 84 | 2 | 1 | 1 | 1 | 78897, 79098, 79103, 79105, 79110, 79111, 79116, 79128, 79135 |
| 201 | 418..537 | 120 | 88 | 88 | 0 | 0 | 0 | 0 | 79122, 79134, 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 6983; unmatched reference entries: 3159; unmatched candidate entries: 50
- identity switches: 1347; fragmentation (coverage interruptions): 2157; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 47 -> 44 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 44 -> 47 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 47 -> 44 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 44 -> 49 at (2090.5, 3033), 4 frames after previous cover
- f87: ref 79037: 47 -> 44 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 78971: 44 -> 51 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79045: 44 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 44 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 47 -> 50 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 50 -> 47 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 51 -> 47 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 47 -> 50 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 50 -> 51 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 47 -> 51 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 44 -> 50 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 47 -> 49 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 51 -> 47 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 50 -> 54 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 50 -> 54 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 54 -> 49 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 44 -> 50 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 49 -> 57 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 50 -> 55 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 49 -> 47 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 47 -> 49 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 44 -> 50 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 47 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 49 -> 51 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 51 -> 49 at (2061, 3032.5), 2 frames after previous cover
- f101: ref 79097: 50 -> 55 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 44 -> 50 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 54 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 47 -> 54 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 50 -> 49 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 55 -> 51 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 51 -> 54 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 50 -> 55 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 44 -> 60 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 49 -> 51 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 51 -> 50 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 54 -> 49 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 50 -> 60 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 49 -> 51 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 55 -> 50 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 51 -> 49 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 55 -> 60 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 60 -> 55 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 51 -> 49 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 51 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 49 -> 54 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 60 -> 65 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 55 -> 60 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 44 -> 55 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 65 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 60 -> 65 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78969: 47 -> 57 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 78971: 54 -> 47 at (1996.5, 3034.5), 4 frames after previous cover
- f109: ref 79037: 49 -> 54 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 60 -> 50 at (2097, 3024.5), 1 frames after previous cover
- ... 1287 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 696 | 218 | 10 (696) |
| 78896 | 350 (76..429) | 252 | 70 | 57 (89), 51 (45), 44 (38), 85 (34), 54 (29), 49 (7), 76 (5), 113 (4), 47 (1) |
| 78969 | 352 (80..434) | 240 | 71 | 85 (76), 76 (66), 113 (26), 84 (19), 57 (14), 44 (13), 47 (10), 51 (6), 54 (3), 106 (3), 50 (2), 49 (2) |
| 78971 | 352 (84..439) | 247 | 67 | 85 (55), 44 (45), 106 (38), 113 (28), 51 (18), 54 (15), 84 (15), 47 (11), 90 (10), 76 (6), 57 (5), 49 (1) |
| 79045 | 355 (84..443) | 242 | 78 | 84 (50), 51 (31), 54 (31), 85 (27), 90 (24), 126 (15), 50 (13), 57 (11), 106 (11), 44 (8), 76 (8), 47 (7), +2 more |
| 79037 | 355 (86..445) | 245 | 75 | 126 (37), 51 (36), 57 (31), 84 (27), 85 (23), 182 (20), 50 (19), 106 (12), 54 (10), 90 (10), 44 (6), 49 (4), +4 more |
| 78897 | 345 (89..450) | 235 | 83 | 126 (74), 84 (46), 51 (20), 106 (15), 57 (12), 50 (9), 87 (9), 85 (8), 71 (7), 54 (6), 60 (6), 113 (6), +7 more |
| 78899 | 365 (91..455) | 238 | 81 | 84 (56), 126 (42), 50 (28), 113 (23), 49 (16), 71 (15), 106 (14), 57 (10), 51 (7), 54 (6), 44 (4), 60 (4), +7 more |
| 79097 | 366 (94..461) | 242 | 83 | 76 (40), 106 (39), 113 (29), 71 (27), 50 (24), 49 (16), 84 (16), 44 (12), 54 (11), 90 (4), 126 (4), 82 (3), +8 more |
| 79098 | 360 (97..467) | 237 | 83 | 50 (29), 76 (28), 44 (25), 71 (24), 106 (19), 51 (18), 113 (13), 57 (12), 54 (11), 84 (11), 126 (8), 142 (7), +10 more |
| 79102 | 371 (98..477) | 252 | 89 | 106 (39), 50 (30), 113 (25), 44 (24), 57 (19), 142 (17), 182 (14), 49 (13), 76 (10), 87 (8), 90 (8), 91 (7), +10 more |
| 79103 | 380 (99..481) | 257 | 82 | 44 (44), 142 (43), 87 (31), 54 (23), 113 (19), 60 (15), 65 (11), 49 (11), 71 (11), 50 (9), 76 (8), 68 (8), +10 more |
| 79105 | 379 (101..484) | 257 | 76 | 87 (47), 142 (34), 86 (21), 44 (20), 50 (19), 60 (18), 47 (18), 49 (12), 68 (8), 182 (8), 106 (8), 65 (7), +11 more |
| 79108 | 385 (104..492) | 269 | 73 | 44 (76), 142 (31), 87 (26), 60 (19), 50 (15), 86 (13), 76 (13), 91 (12), 113 (11), 49 (10), 47 (9), 51 (8), +10 more |
| 79110 | 388 (106..497) | 269 | 76 | 60 (74), 47 (29), 50 (22), 142 (22), 87 (13), 68 (12), 76 (12), 51 (12), 65 (11), 106 (11), 91 (9), 49 (9), +10 more |
| 79111 | 386 (109..500) | 274 | 80 | 193 (54), 49 (33), 60 (32), 142 (22), 47 (20), 68 (19), 54 (18), 50 (17), 65 (16), 87 (14), 51 (7), 72 (5), +6 more |
| 79115 | 421 (111..531) | 291 | 89 | 149 (76), 60 (31), 47 (29), 51 (26), 54 (23), 82 (21), 65 (16), 55 (15), 87 (15), 76 (14), 68 (10), 50 (8), +4 more |
| 79116 | 411 (114..530) | 278 | 91 | 82 (106), 60 (32), 47 (18), 76 (17), 149 (16), 54 (14), 68 (13), 87 (13), 55 (12), 86 (12), 50 (7), 90 (4), +7 more |
| 79122 | 404 (118..532) | 265 | 91 | 49 (84), 82 (43), 60 (34), 47 (19), 50 (18), 54 (13), 149 (13), 87 (10), 68 (6), 90 (5), 76 (5), 51 (5), +5 more |
| 79132 | 391 (120..515) | 275 | 81 | 51 (88), 60 (40), 68 (27), 54 (22), 76 (22), 82 (21), 149 (13), 50 (8), 87 (8), 49 (6), 55 (4), 65 (4), +3 more |
| 79128 | 402 (124..527) | 279 | 86 | 47 (76), 68 (44), 149 (35), 54 (28), 82 (25), 49 (17), 60 (16), 65 (10), 50 (9), 87 (8), 72 (4), 76 (4), +2 more |
| 79134 | 407 (127..533) | 291 | 86 | 55 (80), 49 (54), 87 (33), 47 (32), 68 (29), 82 (17), 54 (14), 149 (13), 65 (8), 50 (6), 72 (4), 201 (1) |
| 79135 | 409 (129..542) | 285 | 87 | 201 (76), 82 (55), 68 (37), 47 (33), 55 (27), 193 (15), 87 (13), 65 (12), 49 (11), 149 (5), 50 (1) |
| 79139 | 406 (132..537) | 286 | 88 | 68 (102), 55 (84), 82 (35), 65 (21), 47 (19), 49 (10), 179 (8), 201 (4), 72 (3) |
| 79136 | 393 (136..538) | 281 | 73 | 179 (134), 55 (74), 65 (54), 49 (16), 201 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 52/286/995; tracks with internal gaps: 12; total internal gaps: 27; longest internal gap: 2; tracks ending in coasting: 12 (trailing rows total 21)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 12..1006 | 995 | 711 | 696 | 15 | 15 | 1 | 0 | 78911 |
| 44 | 81..492 | 412 | 330 | 330 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 47 | 84..515 | 432 | 354 | 349 | 5 | 2 | 1 | 3 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 49 | 87..533 | 447 | 348 | 347 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 88..466 | 379 | 295 | 293 | 2 | 0 | 0 | 2 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 51 | 88..515 | 428 | 340 | 338 | 2 | 1 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 54 | 97..481 | 385 | 299 | 299 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 55 | 99..530 | 432 | 317 | 315 | 2 | 1 | 2 | 0 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 99..381 | 283 | 215 | 213 | 2 | 0 | 0 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 60 | 103..495 | 393 | 332 | 331 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..361 | 255 | 185 | 182 | 3 | 1 | 1 | 2 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 113..535 | 423 | 323 | 320 | 3 | 1 | 1 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 71 | 116..240 | 125 | 96 | 94 | 2 | 0 | 0 | 2 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 72 | 116..167 | 52 | 31 | 29 | 2 | 0 | 0 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 76 | 120..467 | 348 | 272 | 271 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 129..530 | 402 | 336 | 336 | 0 | 0 | 0 | 0 | 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 84 | 129..434 | 306 | 240 | 240 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 132..427 | 296 | 223 | 223 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 135..203 | 69 | 59 | 58 | 1 | 0 | 0 | 1 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 87 | 135..459 | 325 | 255 | 254 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 90 | 141..253 | 113 | 94 | 93 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132 |
| 91 | 141..198 | 58 | 44 | 42 | 2 | 0 | 0 | 2 | 79097, 79098, 79102, 79105, 79108, 79110 |
| 106 | 192..477 | 286 | 219 | 218 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 113 | 200..438 | 239 | 195 | 194 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 126 | 224..460 | 237 | 187 | 187 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 142 | 269..484 | 216 | 186 | 186 | 0 | 0 | 0 | 0 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 149 | 291..531 | 241 | 171 | 171 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 179 | 363..537 | 175 | 142 | 142 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 182 | 371..445 | 75 | 60 | 60 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108 |
| 193 | 404..544 | 141 | 86 | 84 | 2 | 1 | 1 | 1 | 78897, 79098, 79103, 79105, 79110, 79111, 79116, 79128, 79135 |
| 201 | 418..537 | 120 | 88 | 88 | 0 | 0 | 0 | 0 | 79122, 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 8447; unmatched reference entries: 1695; unmatched candidate entries: 1513
- identity switches: 1367; fragmentation (coverage interruptions): 1130; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 47 -> 44 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 44 -> 47 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 47 -> 44 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 44 -> 49 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 44 -> 51 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79037: 47 -> 44 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 44 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 44 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 47 -> 50 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 50 -> 47 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 51 -> 47 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 47 -> 50 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 50 -> 51 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 47 -> 51 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 44 -> 50 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 47 -> 49 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 51 -> 47 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 50 -> 54 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 50 -> 54 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 54 -> 49 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 44 -> 50 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 49 -> 57 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 50 -> 55 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 49 -> 47 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 47 -> 49 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 44 -> 50 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 47 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 49 -> 51 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 51 -> 49 at (2061, 3032.5), 1 frames after previous cover
- f101: ref 79097: 50 -> 55 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 44 -> 50 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 54 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 47 -> 54 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 50 -> 49 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 55 -> 51 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 51 -> 54 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 50 -> 55 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 44 -> 60 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 49 -> 51 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 51 -> 50 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 54 -> 49 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 50 -> 60 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 49 -> 51 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 55 -> 50 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 51 -> 49 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 55 -> 60 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 60 -> 55 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 51 -> 49 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 51 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 49 -> 54 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 60 -> 65 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 55 -> 60 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 44 -> 55 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 65 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 60 -> 65 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78969: 47 -> 57 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 78971: 54 -> 47 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79037: 49 -> 54 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 60 -> 50 at (2097, 3024.5), 1 frames after previous cover
- ... 1307 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 946 | 34 | 10 (946) |
| 78896 | 350 (76..429) | 304 | 31 | 57 (105), 51 (54), 44 (45), 85 (44), 54 (34), 49 (9), 76 (7), 113 (5), 47 (1) |
| 78969 | 352 (80..434) | 287 | 39 | 85 (98), 76 (76), 113 (33), 84 (23), 57 (15), 44 (14), 47 (11), 51 (6), 106 (4), 54 (3), 50 (2), 49 (2) |
| 78971 | 352 (84..439) | 290 | 40 | 85 (65), 44 (51), 106 (48), 113 (33), 51 (21), 54 (17), 84 (17), 90 (13), 47 (11), 76 (7), 57 (6), 49 (1) |
| 79045 | 355 (84..443) | 283 | 46 | 84 (58), 54 (37), 51 (35), 85 (33), 90 (26), 50 (18), 126 (16), 106 (14), 57 (12), 44 (11), 76 (9), 47 (7), +2 more |
| 79037 | 355 (86..445) | 281 | 54 | 51 (41), 126 (39), 57 (36), 84 (33), 182 (25), 85 (24), 50 (23), 54 (13), 106 (13), 90 (12), 44 (6), 47 (4), +4 more |
| 78897 | 345 (89..450) | 273 | 59 | 126 (88), 84 (54), 51 (22), 106 (16), 57 (14), 50 (10), 87 (9), 85 (9), 71 (8), 60 (7), 113 (7), 54 (6), +7 more |
| 78899 | 365 (91..455) | 284 | 50 | 84 (67), 126 (52), 50 (31), 113 (27), 49 (19), 71 (17), 106 (16), 57 (13), 54 (9), 51 (8), 44 (4), 60 (4), +8 more |
| 79097 | 366 (94..461) | 283 | 54 | 76 (52), 106 (42), 113 (34), 71 (29), 50 (28), 84 (20), 49 (18), 54 (14), 44 (12), 126 (7), 87 (4), 90 (4), +8 more |
| 79098 | 360 (97..467) | 276 | 55 | 50 (34), 76 (33), 71 (29), 44 (28), 106 (25), 51 (18), 54 (14), 113 (14), 84 (12), 57 (12), 126 (10), 142 (9), +10 more |
| 79102 | 371 (98..477) | 291 | 58 | 106 (54), 50 (36), 113 (27), 44 (25), 57 (21), 142 (19), 182 (15), 49 (13), 90 (11), 76 (11), 87 (9), 91 (8), +10 more |
| 79103 | 380 (99..481) | 301 | 54 | 44 (49), 142 (48), 87 (37), 113 (24), 54 (24), 60 (17), 71 (17), 106 (13), 49 (12), 65 (11), 76 (11), 50 (10), +10 more |
| 79105 | 379 (101..484) | 299 | 46 | 87 (61), 142 (38), 86 (26), 44 (25), 50 (22), 47 (21), 60 (19), 49 (14), 68 (10), 182 (8), 106 (8), 65 (7), +11 more |
| 79108 | 385 (104..492) | 313 | 48 | 44 (97), 142 (33), 87 (30), 60 (21), 50 (20), 76 (16), 86 (13), 91 (13), 113 (13), 49 (10), 47 (9), 51 (9), +10 more |
| 79110 | 388 (106..497) | 319 | 42 | 60 (93), 47 (31), 142 (26), 50 (23), 68 (15), 76 (15), 106 (15), 65 (13), 51 (13), 87 (12), 54 (11), 49 (11), +10 more |
| 79111 | 386 (109..500) | 326 | 40 | 193 (73), 49 (40), 60 (37), 142 (24), 50 (22), 54 (22), 68 (21), 65 (19), 47 (19), 87 (16), 51 (7), 72 (6), +6 more |
| 79115 | 421 (111..531) | 358 | 45 | 149 (117), 47 (34), 60 (33), 51 (32), 54 (26), 82 (23), 65 (17), 87 (17), 76 (15), 55 (14), 68 (12), 50 (9), +5 more |
| 79116 | 411 (114..530) | 342 | 46 | 82 (133), 60 (37), 47 (20), 76 (20), 54 (19), 149 (18), 87 (17), 68 (15), 55 (15), 86 (14), 50 (7), 44 (6), +7 more |
| 79122 | 404 (118..532) | 326 | 52 | 49 (117), 82 (50), 60 (37), 47 (22), 50 (20), 54 (18), 87 (12), 149 (10), 68 (7), 55 (7), 90 (7), 76 (5), +5 more |
| 79132 | 391 (120..515) | 328 | 43 | 51 (116), 60 (47), 68 (28), 54 (25), 82 (25), 76 (23), 149 (16), 50 (11), 87 (8), 49 (7), 55 (5), 47 (5), +3 more |
| 79128 | 402 (124..527) | 341 | 43 | 47 (99), 68 (53), 149 (42), 54 (32), 82 (29), 49 (19), 60 (19), 50 (12), 87 (12), 65 (11), 72 (5), 76 (5), +2 more |
| 79134 | 407 (127..533) | 351 | 41 | 55 (100), 49 (63), 87 (43), 47 (41), 68 (31), 54 (20), 82 (18), 149 (13), 65 (8), 50 (8), 72 (5), 201 (1) |
| 79135 | 409 (129..542) | 348 | 38 | 201 (99), 82 (61), 68 (48), 47 (37), 55 (35), 193 (18), 87 (17), 65 (13), 49 (12), 149 (6), 50 (2) |
| 79139 | 406 (132..537) | 357 | 35 | 68 (130), 55 (108), 82 (41), 65 (26), 47 (24), 49 (13), 201 (6), 72 (4), 179 (3), 149 (2) |
| 79136 | 393 (136..538) | 340 | 37 | 179 (163), 55 (92), 65 (68), 49 (17) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 81/315/997; tracks with internal gaps: 30; total internal gaps: 371; longest internal gap: 10; tracks ending in coasting: 31 (trailing rows total 973)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 12..1008 | 997 | 997 | 946 | 51 | 34 | 4 | 1 | 78911 |
| 44 | 81..521 | 441 | 441 | 387 | 54 | 17 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 47 | 84..544 | 461 | 461 | 407 | 54 | 13 | 5 | 37 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 49 | 87..562 | 476 | 476 | 418 | 58 | 21 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 88..495 | 408 | 408 | 348 | 60 | 16 | 2 | 43 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 51 | 88..544 | 457 | 457 | 400 | 57 | 17 | 6 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 54 | 97..510 | 414 | 414 | 359 | 55 | 17 | 3 | 32 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 55 | 99..559 | 461 | 461 | 395 | 66 | 25 | 5 | 28 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 99..410 | 312 | 312 | 246 | 66 | 10 | 3 | 52 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 60 | 103..524 | 422 | 422 | 382 | 40 | 8 | 5 | 27 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..390 | 284 | 284 | 214 | 70 | 9 | 7 | 46 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 113..564 | 452 | 452 | 384 | 68 | 18 | 2 | 47 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 71 | 116..269 | 154 | 154 | 112 | 42 | 1 | 1 | 41 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 72 | 116..196 | 81 | 81 | 33 | 48 | 2 | 5 | 42 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 76 | 120..496 | 377 | 377 | 321 | 56 | 18 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 129..559 | 431 | 431 | 393 | 38 | 10 | 2 | 27 | 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 84 | 129..463 | 335 | 335 | 284 | 51 | 19 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 132..456 | 325 | 325 | 273 | 52 | 16 | 4 | 27 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 135..232 | 98 | 98 | 66 | 32 | 2 | 1 | 30 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 87 | 135..488 | 354 | 354 | 309 | 45 | 14 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 90 | 141..282 | 142 | 142 | 109 | 33 | 3 | 1 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132 |
| 91 | 141..227 | 87 | 87 | 47 | 40 | 0 | 0 | 40 | 79097, 79098, 79102, 79105, 79108, 79110 |
| 106 | 192..506 | 315 | 315 | 269 | 46 | 16 | 3 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 113 | 200..467 | 268 | 268 | 230 | 38 | 8 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 126 | 224..489 | 266 | 266 | 222 | 44 | 14 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 142 | 269..513 | 245 | 245 | 208 | 37 | 5 | 4 | 29 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 149 | 291..560 | 270 | 270 | 224 | 46 | 15 | 4 | 23 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 179 | 363..566 | 204 | 204 | 166 | 38 | 7 | 3 | 28 | 79136, 79139 |
| 182 | 371..474 | 104 | 104 | 69 | 35 | 3 | 3 | 29 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108 |
| 193 | 404..573 | 170 | 170 | 115 | 55 | 7 | 10 | 34 | 78897, 78899, 79098, 79103, 79105, 79110, 79111, 79115, 79116, 79128, 79135 |
| 201 | 418..566 | 149 | 149 | 111 | 38 | 6 | 6 | 24 | 79122, 79134, 79135, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 31; matched pairs: 8447; unmatched reference entries: 1695; unmatched candidate entries: 1513
- identity switches: 1367; fragmentation (coverage interruptions): 1130; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 47 -> 44 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 44 -> 47 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 47 -> 44 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 44 -> 49 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 44 -> 51 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79037: 47 -> 44 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 44 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 44 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 47 -> 50 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 50 -> 47 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 51 -> 47 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 47 -> 50 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 50 -> 51 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 47 -> 51 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 44 -> 50 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 47 -> 49 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 51 -> 47 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 50 -> 54 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 50 -> 54 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 54 -> 49 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 44 -> 50 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 49 -> 57 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 50 -> 55 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 49 -> 47 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 47 -> 49 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 44 -> 50 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 47 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 49 -> 51 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 51 -> 49 at (2061, 3032.5), 1 frames after previous cover
- f101: ref 79097: 50 -> 55 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 44 -> 50 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 54 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 47 -> 54 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 50 -> 49 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 55 -> 51 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 51 -> 54 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 50 -> 55 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 44 -> 60 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 49 -> 51 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 51 -> 50 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 54 -> 49 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 50 -> 60 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 49 -> 51 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 55 -> 50 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 51 -> 49 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 55 -> 60 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 60 -> 55 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 51 -> 49 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 51 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 49 -> 54 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 60 -> 65 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 55 -> 60 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 44 -> 55 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 65 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 60 -> 65 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78969: 47 -> 57 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 78971: 54 -> 47 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79037: 49 -> 54 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 60 -> 50 at (2097, 3024.5), 1 frames after previous cover
- ... 1307 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 946 | 34 | 10 (946) |
| 78896 | 350 (76..429) | 304 | 31 | 57 (105), 51 (54), 44 (45), 85 (44), 54 (34), 49 (9), 76 (7), 113 (5), 47 (1) |
| 78969 | 352 (80..434) | 287 | 39 | 85 (98), 76 (76), 113 (33), 84 (23), 57 (15), 44 (14), 47 (11), 51 (6), 106 (4), 54 (3), 50 (2), 49 (2) |
| 78971 | 352 (84..439) | 290 | 40 | 85 (65), 44 (51), 106 (48), 113 (33), 51 (21), 54 (17), 84 (17), 90 (13), 47 (11), 76 (7), 57 (6), 49 (1) |
| 79045 | 355 (84..443) | 283 | 46 | 84 (58), 54 (37), 51 (35), 85 (33), 90 (26), 50 (18), 126 (16), 106 (14), 57 (12), 44 (11), 76 (9), 47 (7), +2 more |
| 79037 | 355 (86..445) | 281 | 54 | 51 (41), 126 (39), 57 (36), 84 (33), 182 (25), 85 (24), 50 (23), 54 (13), 106 (13), 90 (12), 44 (6), 47 (4), +4 more |
| 78897 | 345 (89..450) | 273 | 59 | 126 (88), 84 (54), 51 (22), 106 (16), 57 (14), 50 (10), 87 (9), 85 (9), 71 (8), 60 (7), 113 (7), 54 (6), +7 more |
| 78899 | 365 (91..455) | 284 | 50 | 84 (67), 126 (52), 50 (31), 113 (27), 49 (19), 71 (17), 106 (16), 57 (13), 54 (9), 51 (8), 44 (4), 60 (4), +8 more |
| 79097 | 366 (94..461) | 283 | 54 | 76 (52), 106 (42), 113 (34), 71 (29), 50 (28), 84 (20), 49 (18), 54 (14), 44 (12), 126 (7), 87 (4), 90 (4), +8 more |
| 79098 | 360 (97..467) | 276 | 55 | 50 (34), 76 (33), 71 (29), 44 (28), 106 (25), 51 (18), 54 (14), 113 (14), 84 (12), 57 (12), 126 (10), 142 (9), +10 more |
| 79102 | 371 (98..477) | 291 | 58 | 106 (54), 50 (36), 113 (27), 44 (25), 57 (21), 142 (19), 182 (15), 49 (13), 90 (11), 76 (11), 87 (9), 91 (8), +10 more |
| 79103 | 380 (99..481) | 301 | 54 | 44 (49), 142 (48), 87 (37), 113 (24), 54 (24), 60 (17), 71 (17), 106 (13), 49 (12), 65 (11), 76 (11), 50 (10), +10 more |
| 79105 | 379 (101..484) | 299 | 46 | 87 (61), 142 (38), 86 (26), 44 (25), 50 (22), 47 (21), 60 (19), 49 (14), 68 (10), 182 (8), 106 (8), 65 (7), +11 more |
| 79108 | 385 (104..492) | 313 | 48 | 44 (97), 142 (33), 87 (30), 60 (21), 50 (20), 76 (16), 86 (13), 91 (13), 113 (13), 49 (10), 47 (9), 51 (9), +10 more |
| 79110 | 388 (106..497) | 319 | 42 | 60 (93), 47 (31), 142 (26), 50 (23), 68 (15), 76 (15), 106 (15), 65 (13), 51 (13), 87 (12), 54 (11), 49 (11), +10 more |
| 79111 | 386 (109..500) | 326 | 40 | 193 (73), 49 (40), 60 (37), 142 (24), 50 (22), 54 (22), 68 (21), 65 (19), 47 (19), 87 (16), 51 (7), 72 (6), +6 more |
| 79115 | 421 (111..531) | 358 | 45 | 149 (117), 47 (34), 60 (33), 51 (32), 54 (26), 82 (23), 65 (17), 87 (17), 76 (15), 55 (14), 68 (12), 50 (9), +5 more |
| 79116 | 411 (114..530) | 342 | 46 | 82 (133), 60 (37), 47 (20), 76 (20), 54 (19), 149 (18), 87 (17), 68 (15), 55 (15), 86 (14), 50 (7), 44 (6), +7 more |
| 79122 | 404 (118..532) | 326 | 52 | 49 (117), 82 (50), 60 (37), 47 (22), 50 (20), 54 (18), 87 (12), 149 (10), 68 (7), 55 (7), 90 (7), 76 (5), +5 more |
| 79132 | 391 (120..515) | 328 | 43 | 51 (116), 60 (47), 68 (28), 54 (25), 82 (25), 76 (23), 149 (16), 50 (11), 87 (8), 49 (7), 55 (5), 47 (5), +3 more |
| 79128 | 402 (124..527) | 341 | 43 | 47 (99), 68 (53), 149 (42), 54 (32), 82 (29), 49 (19), 60 (19), 50 (12), 87 (12), 65 (11), 72 (5), 76 (5), +2 more |
| 79134 | 407 (127..533) | 351 | 41 | 55 (100), 49 (63), 87 (43), 47 (41), 68 (31), 54 (20), 82 (18), 149 (13), 65 (8), 50 (8), 72 (5), 201 (1) |
| 79135 | 409 (129..542) | 348 | 38 | 201 (99), 82 (61), 68 (48), 47 (37), 55 (35), 193 (18), 87 (17), 65 (13), 49 (12), 149 (6), 50 (2) |
| 79139 | 406 (132..537) | 357 | 35 | 68 (130), 55 (108), 82 (41), 65 (26), 47 (24), 49 (13), 201 (6), 72 (4), 179 (3), 149 (2) |
| 79136 | 393 (136..538) | 340 | 37 | 179 (163), 55 (92), 65 (68), 49 (17) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 31; lifespan min/median/max: 81/315/997; tracks with internal gaps: 30; total internal gaps: 371; longest internal gap: 10; tracks ending in coasting: 31 (trailing rows total 973)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 12..1008 | 997 | 997 | 946 | 51 | 34 | 4 | 1 | 78911 |
| 44 | 81..521 | 441 | 441 | 387 | 54 | 17 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 47 | 84..544 | 461 | 461 | 407 | 54 | 13 | 5 | 37 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 49 | 87..562 | 476 | 476 | 418 | 58 | 21 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 88..495 | 408 | 408 | 348 | 60 | 16 | 2 | 43 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 51 | 88..544 | 457 | 457 | 400 | 57 | 17 | 6 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 54 | 97..510 | 414 | 414 | 359 | 55 | 17 | 3 | 32 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 55 | 99..559 | 461 | 461 | 395 | 66 | 25 | 5 | 28 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 99..410 | 312 | 312 | 246 | 66 | 10 | 3 | 52 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110 |
| 60 | 103..524 | 422 | 422 | 382 | 40 | 8 | 5 | 27 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..390 | 284 | 284 | 214 | 70 | 9 | 7 | 46 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 68 | 113..564 | 452 | 452 | 384 | 68 | 18 | 2 | 47 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 71 | 116..269 | 154 | 154 | 112 | 42 | 1 | 1 | 41 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 72 | 116..196 | 81 | 81 | 33 | 48 | 2 | 5 | 42 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 76 | 120..496 | 377 | 377 | 321 | 56 | 18 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 82 | 129..559 | 431 | 431 | 393 | 38 | 10 | 2 | 27 | 79097, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 84 | 129..463 | 335 | 335 | 284 | 51 | 19 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 132..456 | 325 | 325 | 273 | 52 | 16 | 4 | 27 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 135..232 | 98 | 98 | 66 | 32 | 2 | 1 | 30 | 78899, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 87 | 135..488 | 354 | 354 | 309 | 45 | 14 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 90 | 141..282 | 142 | 142 | 109 | 33 | 3 | 1 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132 |
| 91 | 141..227 | 87 | 87 | 47 | 40 | 0 | 0 | 40 | 79097, 79098, 79102, 79105, 79108, 79110 |
| 106 | 192..506 | 315 | 315 | 269 | 46 | 16 | 3 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 113 | 200..467 | 268 | 268 | 230 | 38 | 8 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 126 | 224..489 | 266 | 266 | 222 | 44 | 14 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 142 | 269..513 | 245 | 245 | 208 | 37 | 5 | 4 | 29 | 78897, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 149 | 291..560 | 270 | 270 | 224 | 46 | 15 | 4 | 23 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 179 | 363..566 | 204 | 204 | 166 | 38 | 7 | 3 | 28 | 79136, 79139 |
| 182 | 371..474 | 104 | 104 | 69 | 35 | 3 | 3 | 29 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108 |
| 193 | 404..573 | 170 | 170 | 115 | 55 | 7 | 10 | 34 | 78897, 78899, 79098, 79103, 79105, 79110, 79111, 79115, 79116, 79128, 79135 |
| 201 | 418..566 | 149 | 149 | 111 | 38 | 6 | 6 | 24 | 79122, 79134, 79135, 79139 |
