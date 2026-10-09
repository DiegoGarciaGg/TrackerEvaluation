# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=d8db04f3ed35
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise1.0_fp0.5_seed2/tracks.csv sha256=16de79309676bcca
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise1.0_fp0.5_seed2.csv sha256=d8db04f3ed358ab1
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise1.0_fp0.5_seed2
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
| observations | none | 4 | 0.273 | 0.115 | 0.683 | 1.28 | 0.283 | 1054 | 1564.0 |
| observations | none | 6 | 0.294 | 0.123 | 0.683 | 1.29 | 0.285 | 1046 | 1560.0 |
| observations | none | 8 | 0.304 | 0.128 | 0.685 | 1.31 | 0.286 | 1034 | 1561.0 |
| observations | none | 12 | 0.317 | 0.137 | 0.687 | 1.60 | 0.306 | 968 | 1533.0 |
| observations | ignore | 4 | 0.273 | 0.115 | 0.683 | 1.28 | 0.283 | 1054 | 1564.0 |
| observations | ignore | 6 | 0.294 | 0.123 | 0.683 | 1.29 | 0.285 | 1046 | 1560.0 |
| observations | ignore | 8 | 0.304 | 0.128 | 0.685 | 1.31 | 0.286 | 1034 | 1561.0 |
| observations | ignore | 12 | 0.317 | 0.137 | 0.687 | 1.60 | 0.306 | 968 | 1533.0 |
| updates | none | 4 | 0.256 | 0.114 | 0.487 | 1.33 | 0.262 | 1095 | 1486.0 |
| updates | none | 6 | 0.291 | 0.129 | 0.565 | 1.51 | 0.278 | 1077 | 1185.0 |
| updates | none | 8 | 0.310 | 0.139 | 0.651 | 1.78 | 0.295 | 1030 | 864.0 |
| updates | none | 12 | 0.333 | 0.152 | 0.689 | 2.25 | 0.325 | 948 | 697.0 |
| updates | ignore | 4 | 0.256 | 0.114 | 0.487 | 1.33 | 0.262 | 1095 | 1486.0 |
| updates | ignore | 6 | 0.291 | 0.129 | 0.565 | 1.51 | 0.278 | 1077 | 1185.0 |
| updates | ignore | 8 | 0.310 | 0.139 | 0.651 | 1.78 | 0.295 | 1030 | 864.0 |
| updates | ignore | 12 | 0.333 | 0.152 | 0.689 | 2.25 | 0.325 | 948 | 697.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8028; unmatched reference entries: 2114; unmatched candidate entries: 49
- identity switches: 1034; fragmentation (coverage interruptions): 1586; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 44 -> 46 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 42 -> 44 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 47 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 3 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 54 -> 42 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 42 -> 44 at (2124.5, 3027.5), 4 frames after previous cover
- f103: ref 79105: 54 -> 42 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 43 -> 49 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 44 -> 42 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 49 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 38 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 38 -> 49 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 44 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 43 -> 49 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 49 -> 38 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 47 -> 46 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 38 -> 47 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 54 -> 60 at (2131, 3027), 4 frames after previous cover
- f111: ref 78897: 46 -> 47 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 38 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 38 -> 43 at (1994.5, 3035), 2 frames after previous cover
- f111: ref 79097: 53 -> 66 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 44 -> 53 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 42 -> 67 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 42 -> 68 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 44 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 54 -> 42 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 54 -> 60 at (2142, 3026.5), 2 frames after previous cover
- f112: ref 79102: 44 -> 67 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 43 -> 49 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 67 -> 68 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 68 -> 42 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 46 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 66 -> 46 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 53 -> 66 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 68 -> 53 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 42 -> 68 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 44 -> 67 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 44 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 60 -> 42 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 54 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 43 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 49 -> 34 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 43 -> 49 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 43 -> 47 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 47 -> 46 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 38 -> 43 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 49 -> 38 at (1963.5, 3035.5), 1 frames after previous cover
- ... 974 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 798 | 166 | 153 (534), 0 (264) |
| 78896 | 350 (76..429) | 276 | 54 | 34 (152), 95 (69), 49 (30), 68 (25) |
| 78969 | 352 (80..434) | 279 | 51 | 79 (102), 38 (78), 34 (25), 95 (25), 49 (21), 68 (18), 43 (10) |
| 78971 | 352 (84..439) | 281 | 49 | 95 (82), 43 (77), 38 (58), 49 (33), 68 (17), 79 (13), 34 (1) |
| 79045 | 355 (84..443) | 286 | 44 | 38 (123), 47 (64), 49 (43), 95 (32), 68 (11), 43 (10), 79 (2), 34 (1) |
| 79037 | 355 (86..445) | 279 | 61 | 49 (86), 34 (42), 38 (37), 47 (32), 43 (21), 193 (19), 46 (15), 95 (9), 68 (5), 79 (4), 87 (4), 42 (3), +1 more |
| 78897 | 345 (89..450) | 279 | 49 | 46 (76), 47 (46), 95 (33), 68 (27), 43 (26), 66 (26), 87 (21), 49 (11), 38 (5), 34 (4), 42 (2), 44 (2) |
| 78899 | 365 (91..455) | 290 | 57 | 68 (70), 87 (62), 47 (43), 46 (41), 66 (22), 43 (21), 34 (16), 95 (9), 42 (3), 44 (2), 53 (1) |
| 79097 | 366 (94..461) | 295 | 60 | 87 (54), 68 (54), 46 (43), 43 (41), 66 (38), 34 (20), 85 (18), 47 (12), 53 (11), 42 (3), 44 (1) |
| 79098 | 360 (97..467) | 279 | 60 | 87 (66), 43 (64), 46 (61), 66 (23), 34 (22), 47 (12), 85 (11), 53 (7), 44 (5), 68 (5), 42 (2), 83 (1) |
| 79102 | 371 (98..477) | 299 | 61 | 46 (48), 47 (46), 113 (46), 83 (42), 68 (27), 43 (22), 42 (17), 87 (14), 92 (11), 53 (7), 44 (6), 91 (4), +4 more |
| 79103 | 380 (99..481) | 297 | 58 | 68 (42), 83 (42), 47 (37), 113 (35), 46 (32), 85 (30), 91 (27), 53 (14), 42 (11), 87 (9), 66 (5), 43 (5), +3 more |
| 79105 | 379 (101..484) | 293 | 65 | 83 (69), 42 (32), 53 (29), 85 (28), 91 (25), 68 (24), 137 (20), 87 (16), 92 (16), 47 (15), 46 (9), 66 (6), +3 more |
| 79108 | 385 (104..492) | 293 | 64 | 137 (39), 83 (35), 87 (34), 42 (34), 162 (29), 91 (24), 67 (20), 92 (20), 53 (15), 85 (10), 86 (8), 66 (7), +6 more |
| 79110 | 388 (106..497) | 312 | 57 | 85 (46), 86 (45), 42 (43), 53 (40), 162 (27), 137 (21), 44 (20), 67 (19), 66 (14), 83 (13), 174 (10), 91 (5), +4 more |
| 79111 | 386 (109..500) | 306 | 65 | 85 (67), 53 (48), 67 (42), 42 (40), 86 (34), 174 (20), 137 (14), 66 (13), 44 (11), 92 (8), 60 (3), 83 (2), +3 more |
| 79115 | 421 (111..531) | 319 | 68 | 204 (53), 53 (40), 85 (38), 86 (35), 92 (34), 42 (27), 137 (23), 66 (17), 174 (17), 162 (13), 67 (7), 60 (5), +5 more |
| 79116 | 411 (114..530) | 331 | 59 | 86 (116), 44 (56), 42 (36), 67 (28), 92 (24), 85 (17), 173 (16), 53 (11), 162 (7), 54 (6), 113 (6), 66 (5), +2 more |
| 79122 | 404 (118..532) | 321 | 66 | 86 (64), 66 (64), 44 (62), 67 (40), 85 (22), 137 (22), 42 (15), 53 (12), 83 (8), 204 (4), 54 (2), 60 (2), +3 more |
| 79132 | 391 (120..515) | 309 | 53 | 173 (71), 44 (63), 86 (38), 85 (28), 162 (24), 92 (23), 53 (18), 67 (17), 113 (12), 82 (4), 60 (3), 42 (3), +3 more |
| 79128 | 402 (124..527) | 316 | 65 | 113 (60), 174 (60), 67 (53), 162 (23), 82 (22), 44 (22), 173 (21), 42 (16), 66 (16), 83 (13), 54 (3), 60 (3), +3 more |
| 79134 | 407 (127..533) | 332 | 64 | 53 (112), 82 (90), 83 (65), 66 (16), 113 (12), 42 (10), 60 (8), 173 (6), 174 (5), 91 (3), 54 (2), 67 (1), +2 more |
| 79135 | 409 (129..542) | 333 | 58 | 137 (72), 82 (71), 60 (57), 42 (35), 66 (32), 113 (24), 83 (13), 44 (11), 91 (8), 53 (7), 54 (3) |
| 79139 | 406 (132..537) | 312 | 66 | 82 (130), 91 (93), 60 (44), 44 (29), 113 (8), 54 (4), 137 (3), 66 (1) |
| 79136 | 393 (136..538) | 313 | 66 | 60 (222), 66 (52), 82 (27), 54 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 21/351/682; tracks with internal gaps: 19; total internal gaps: 37; longest internal gap: 1; tracks ending in coasting: 9 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..341 | 340 | 270 | 264 | 6 | 4 | 1 | 2 | 78911 |
| 34 | 78..429 | 352 | 286 | 284 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 38 | 82..434 | 353 | 302 | 301 | 1 | 1 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 42 | 86..484 | 399 | 335 | 332 | 3 | 1 | 1 | 2 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 43 | 86..439 | 354 | 297 | 297 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 44 | 89..439 | 351 | 299 | 298 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 91..467 | 377 | 327 | 327 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..443 | 351 | 308 | 307 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 49 | 97..364 | 268 | 227 | 224 | 3 | 1 | 1 | 2 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 53 | 100..533 | 434 | 374 | 373 | 1 | 1 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 54 | 100..149 | 50 | 43 | 42 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 108..537 | 430 | 353 | 352 | 1 | 1 | 1 | 0 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 111..531 | 421 | 359 | 359 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 67 | 111..394 | 284 | 237 | 233 | 4 | 3 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 68 | 111..484 | 374 | 331 | 329 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 79 | 126..267 | 142 | 122 | 121 | 1 | 0 | 0 | 1 | 78969, 78971, 79037, 79045 |
| 82 | 129..537 | 409 | 344 | 344 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..496 | 367 | 307 | 305 | 2 | 1 | 1 | 1 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135 |
| 85 | 130..500 | 371 | 324 | 321 | 3 | 3 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 86 | 133..530 | 398 | 341 | 341 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 133..461 | 329 | 285 | 283 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 91 | 138..363 | 226 | 195 | 192 | 3 | 2 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79132, 79134, 79135, 79139 |
| 92 | 138..307 | 170 | 146 | 145 | 1 | 0 | 0 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 95 | 146..455 | 310 | 261 | 259 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 113 | 213..477 | 265 | 218 | 217 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 137 | 290..542 | 253 | 215 | 215 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79122, 79132, 79135, 79139 |
| 153 | 327..1008 | 682 | 540 | 534 | 6 | 6 | 1 | 0 | 78911 |
| 162 | 349..497 | 149 | 126 | 126 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 173 | 383..515 | 133 | 114 | 114 | 0 | 0 | 0 | 0 | 79116, 79128, 79132, 79134 |
| 174 | 383..527 | 145 | 115 | 113 | 2 | 2 | 1 | 0 | 79110, 79111, 79115, 79122, 79128, 79134 |
| 193 | 425..445 | 21 | 19 | 19 | 0 | 0 | 0 | 0 | 79037 |
| 204 | 454..532 | 79 | 57 | 57 | 0 | 0 | 0 | 0 | 79115, 79122 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8028; unmatched reference entries: 2114; unmatched candidate entries: 49
- identity switches: 1034; fragmentation (coverage interruptions): 1586; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 44 -> 46 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 42 -> 44 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 47 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 3 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 54 -> 42 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 42 -> 44 at (2124.5, 3027.5), 4 frames after previous cover
- f103: ref 79105: 54 -> 42 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 43 -> 49 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 44 -> 42 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 49 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 38 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 38 -> 49 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 44 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 43 -> 49 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 49 -> 38 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 47 -> 46 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 38 -> 47 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 54 -> 60 at (2131, 3027), 4 frames after previous cover
- f111: ref 78897: 46 -> 47 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 38 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 38 -> 43 at (1994.5, 3035), 2 frames after previous cover
- f111: ref 79097: 53 -> 66 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 44 -> 53 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 42 -> 67 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 42 -> 68 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 44 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 54 -> 42 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 54 -> 60 at (2142, 3026.5), 2 frames after previous cover
- f112: ref 79102: 44 -> 67 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 43 -> 49 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 67 -> 68 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 68 -> 42 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 46 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 66 -> 46 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 53 -> 66 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 68 -> 53 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 42 -> 68 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 44 -> 67 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 44 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 60 -> 42 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 54 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 43 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 49 -> 34 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 43 -> 49 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 43 -> 47 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 47 -> 46 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 38 -> 43 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 49 -> 38 at (1963.5, 3035.5), 1 frames after previous cover
- ... 974 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 798 | 166 | 153 (534), 0 (264) |
| 78896 | 350 (76..429) | 276 | 54 | 34 (152), 95 (69), 49 (30), 68 (25) |
| 78969 | 352 (80..434) | 279 | 51 | 79 (102), 38 (78), 34 (25), 95 (25), 49 (21), 68 (18), 43 (10) |
| 78971 | 352 (84..439) | 281 | 49 | 95 (82), 43 (77), 38 (58), 49 (33), 68 (17), 79 (13), 34 (1) |
| 79045 | 355 (84..443) | 286 | 44 | 38 (123), 47 (64), 49 (43), 95 (32), 68 (11), 43 (10), 79 (2), 34 (1) |
| 79037 | 355 (86..445) | 279 | 61 | 49 (86), 34 (42), 38 (37), 47 (32), 43 (21), 193 (19), 46 (15), 95 (9), 68 (5), 79 (4), 87 (4), 42 (3), +1 more |
| 78897 | 345 (89..450) | 279 | 49 | 46 (76), 47 (46), 95 (33), 68 (27), 43 (26), 66 (26), 87 (21), 49 (11), 38 (5), 34 (4), 42 (2), 44 (2) |
| 78899 | 365 (91..455) | 290 | 57 | 68 (70), 87 (62), 47 (43), 46 (41), 66 (22), 43 (21), 34 (16), 95 (9), 42 (3), 44 (2), 53 (1) |
| 79097 | 366 (94..461) | 295 | 60 | 87 (54), 68 (54), 46 (43), 43 (41), 66 (38), 34 (20), 85 (18), 47 (12), 53 (11), 42 (3), 44 (1) |
| 79098 | 360 (97..467) | 279 | 60 | 87 (66), 43 (64), 46 (61), 66 (23), 34 (22), 47 (12), 85 (11), 53 (7), 44 (5), 68 (5), 42 (2), 83 (1) |
| 79102 | 371 (98..477) | 299 | 61 | 46 (48), 47 (46), 113 (46), 83 (42), 68 (27), 43 (22), 42 (17), 87 (14), 92 (11), 53 (7), 44 (6), 91 (4), +4 more |
| 79103 | 380 (99..481) | 297 | 58 | 68 (42), 83 (42), 47 (37), 113 (35), 46 (32), 85 (30), 91 (27), 53 (14), 42 (11), 87 (9), 66 (5), 43 (5), +3 more |
| 79105 | 379 (101..484) | 293 | 65 | 83 (69), 42 (32), 53 (29), 85 (28), 91 (25), 68 (24), 137 (20), 87 (16), 92 (16), 47 (15), 46 (9), 66 (6), +3 more |
| 79108 | 385 (104..492) | 293 | 64 | 137 (39), 83 (35), 87 (34), 42 (34), 162 (29), 91 (24), 67 (20), 92 (20), 53 (15), 85 (10), 86 (8), 66 (7), +6 more |
| 79110 | 388 (106..497) | 312 | 57 | 85 (46), 86 (45), 42 (43), 53 (40), 162 (27), 137 (21), 44 (20), 67 (19), 66 (14), 83 (13), 174 (10), 91 (5), +4 more |
| 79111 | 386 (109..500) | 306 | 65 | 85 (67), 53 (48), 67 (42), 42 (40), 86 (34), 174 (20), 137 (14), 66 (13), 44 (11), 92 (8), 60 (3), 83 (2), +3 more |
| 79115 | 421 (111..531) | 319 | 68 | 204 (53), 53 (40), 85 (38), 86 (35), 92 (34), 42 (27), 137 (23), 66 (17), 174 (17), 162 (13), 67 (7), 60 (5), +5 more |
| 79116 | 411 (114..530) | 331 | 59 | 86 (116), 44 (56), 42 (36), 67 (28), 92 (24), 85 (17), 173 (16), 53 (11), 162 (7), 54 (6), 113 (6), 66 (5), +2 more |
| 79122 | 404 (118..532) | 321 | 66 | 86 (64), 66 (64), 44 (62), 67 (40), 85 (22), 137 (22), 42 (15), 53 (12), 83 (8), 204 (4), 54 (2), 60 (2), +3 more |
| 79132 | 391 (120..515) | 309 | 53 | 173 (71), 44 (63), 86 (38), 85 (28), 162 (24), 92 (23), 53 (18), 67 (17), 113 (12), 82 (4), 60 (3), 42 (3), +3 more |
| 79128 | 402 (124..527) | 316 | 65 | 113 (60), 174 (60), 67 (53), 162 (23), 82 (22), 44 (22), 173 (21), 42 (16), 66 (16), 83 (13), 54 (3), 60 (3), +3 more |
| 79134 | 407 (127..533) | 332 | 64 | 53 (112), 82 (90), 83 (65), 66 (16), 113 (12), 42 (10), 60 (8), 173 (6), 174 (5), 91 (3), 54 (2), 67 (1), +2 more |
| 79135 | 409 (129..542) | 333 | 58 | 137 (72), 82 (71), 60 (57), 42 (35), 66 (32), 113 (24), 83 (13), 44 (11), 91 (8), 53 (7), 54 (3) |
| 79139 | 406 (132..537) | 312 | 66 | 82 (130), 91 (93), 60 (44), 44 (29), 113 (8), 54 (4), 137 (3), 66 (1) |
| 79136 | 393 (136..538) | 313 | 66 | 60 (222), 66 (52), 82 (27), 54 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 21/351/682; tracks with internal gaps: 19; total internal gaps: 37; longest internal gap: 1; tracks ending in coasting: 9 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..341 | 340 | 270 | 264 | 6 | 4 | 1 | 2 | 78911 |
| 34 | 78..429 | 352 | 286 | 284 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 38 | 82..434 | 353 | 302 | 301 | 1 | 1 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 42 | 86..484 | 399 | 335 | 332 | 3 | 1 | 1 | 2 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 43 | 86..439 | 354 | 297 | 297 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 44 | 89..439 | 351 | 299 | 298 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 91..467 | 377 | 327 | 327 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..443 | 351 | 308 | 307 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 49 | 97..364 | 268 | 227 | 224 | 3 | 1 | 1 | 2 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 53 | 100..533 | 434 | 374 | 373 | 1 | 1 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 54 | 100..149 | 50 | 43 | 42 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 108..537 | 430 | 353 | 352 | 1 | 1 | 1 | 0 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 111..531 | 421 | 359 | 359 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 67 | 111..394 | 284 | 237 | 233 | 4 | 3 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 68 | 111..484 | 374 | 331 | 329 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 79 | 126..267 | 142 | 122 | 121 | 1 | 0 | 0 | 1 | 78969, 78971, 79037, 79045 |
| 82 | 129..537 | 409 | 344 | 344 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..496 | 367 | 307 | 305 | 2 | 1 | 1 | 1 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135 |
| 85 | 130..500 | 371 | 324 | 321 | 3 | 3 | 1 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 86 | 133..530 | 398 | 341 | 341 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 133..461 | 329 | 285 | 283 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 91 | 138..363 | 226 | 195 | 192 | 3 | 2 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79132, 79134, 79135, 79139 |
| 92 | 138..307 | 170 | 146 | 145 | 1 | 0 | 0 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 95 | 146..455 | 310 | 261 | 259 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 113 | 213..477 | 265 | 218 | 217 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 137 | 290..542 | 253 | 215 | 215 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79122, 79132, 79135, 79139 |
| 153 | 327..1008 | 682 | 540 | 534 | 6 | 6 | 1 | 0 | 78911 |
| 162 | 349..497 | 149 | 126 | 126 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 173 | 383..515 | 133 | 114 | 114 | 0 | 0 | 0 | 0 | 79116, 79128, 79132, 79134 |
| 174 | 383..527 | 145 | 115 | 113 | 2 | 2 | 1 | 0 | 79110, 79111, 79115, 79122, 79128, 79134 |
| 193 | 425..445 | 21 | 19 | 19 | 0 | 0 | 0 | 0 | 79037 |
| 204 | 454..532 | 79 | 57 | 57 | 0 | 0 | 0 | 0 | 79115, 79122 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9061; unmatched reference entries: 1081; unmatched candidate entries: 1425
- identity switches: 1030; fragmentation (coverage interruptions): 789; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 46 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 42 -> 44 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 47 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 54 -> 42 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 42 -> 44 at (2124.5, 3027.5), 3 frames after previous cover
- f103: ref 79105: 54 -> 42 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 43 -> 49 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 44 -> 42 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 49 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 38 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 38 -> 49 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 44 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 43 -> 49 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 49 -> 38 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 47 -> 46 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 38 -> 47 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 54 -> 60 at (2131, 3027), 3 frames after previous cover
- f111: ref 78897: 46 -> 47 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 38 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 38 -> 43 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 53 -> 66 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 44 -> 53 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 42 -> 67 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 42 -> 68 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 44 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 54 -> 42 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 54 -> 60 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 44 -> 67 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 43 -> 49 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 67 -> 68 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 68 -> 42 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 46 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 66 -> 46 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 53 -> 66 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 68 -> 53 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 42 -> 68 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 44 -> 67 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 44 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 60 -> 42 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 54 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 43 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 49 -> 34 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 43 -> 49 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 43 -> 47 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 47 -> 46 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 38 -> 43 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 49 -> 38 at (1963.5, 3035.5), 1 frames after previous cover
- ... 970 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 972 | 29 | 153 (656), 0 (316) |
| 78896 | 350 (76..429) | 309 | 26 | 34 (169), 95 (81), 49 (34), 68 (25) |
| 78969 | 352 (80..434) | 307 | 32 | 79 (112), 38 (82), 34 (31), 49 (26), 95 (26), 68 (20), 43 (10) |
| 78971 | 352 (84..439) | 315 | 24 | 95 (94), 43 (89), 38 (65), 49 (35), 68 (18), 79 (13), 34 (1) |
| 79045 | 355 (84..443) | 310 | 24 | 38 (131), 47 (70), 49 (47), 95 (38), 68 (12), 43 (9), 79 (2), 34 (1) |
| 79037 | 355 (86..445) | 312 | 34 | 49 (93), 34 (51), 38 (43), 47 (35), 43 (24), 193 (21), 46 (15), 95 (10), 79 (5), 87 (5), 68 (5), 42 (3), +1 more |
| 78897 | 345 (89..450) | 299 | 36 | 46 (82), 47 (51), 95 (35), 66 (29), 43 (28), 68 (28), 87 (21), 49 (11), 38 (5), 34 (4), 44 (3), 42 (2) |
| 78899 | 365 (91..455) | 321 | 37 | 68 (79), 87 (70), 47 (48), 46 (43), 43 (22), 66 (21), 34 (19), 95 (11), 44 (4), 42 (3), 53 (1) |
| 79097 | 366 (94..461) | 329 | 29 | 87 (59), 68 (57), 46 (50), 43 (50), 66 (39), 34 (24), 85 (22), 47 (13), 53 (11), 42 (3), 44 (1) |
| 79098 | 360 (97..467) | 314 | 34 | 87 (73), 43 (72), 46 (70), 66 (25), 34 (25), 85 (13), 47 (12), 53 (8), 44 (6), 68 (6), 42 (2), 83 (2) |
| 79102 | 371 (98..477) | 331 | 33 | 46 (55), 113 (53), 47 (50), 83 (48), 68 (27), 43 (27), 42 (19), 87 (15), 92 (11), 53 (7), 44 (6), 91 (4), +4 more |
| 79103 | 380 (99..481) | 323 | 37 | 83 (48), 68 (44), 47 (39), 46 (38), 113 (36), 85 (34), 91 (29), 53 (15), 42 (12), 87 (10), 66 (5), 43 (5), +3 more |
| 79105 | 379 (101..484) | 327 | 37 | 83 (78), 53 (36), 42 (33), 91 (29), 85 (29), 68 (26), 137 (22), 92 (20), 87 (19), 47 (16), 46 (9), 66 (6), +3 more |
| 79108 | 385 (104..492) | 324 | 44 | 137 (42), 83 (39), 42 (39), 87 (37), 162 (35), 91 (24), 92 (23), 67 (22), 53 (18), 85 (10), 86 (8), 66 (7), +6 more |
| 79110 | 388 (106..497) | 342 | 33 | 86 (50), 42 (48), 85 (48), 53 (43), 162 (30), 67 (22), 137 (21), 44 (20), 66 (15), 83 (15), 174 (14), 91 (6), +4 more |
| 79111 | 386 (109..500) | 345 | 32 | 85 (78), 53 (56), 67 (47), 42 (45), 86 (39), 174 (21), 137 (14), 66 (14), 44 (12), 92 (8), 60 (3), 54 (2), +3 more |
| 79115 | 421 (111..531) | 364 | 38 | 204 (74), 53 (43), 85 (41), 86 (40), 92 (36), 42 (31), 137 (25), 174 (20), 66 (17), 162 (14), 67 (8), 60 (6), +4 more |
| 79116 | 411 (114..530) | 372 | 31 | 86 (132), 44 (60), 42 (44), 67 (33), 92 (26), 85 (19), 173 (18), 53 (11), 162 (7), 54 (6), 66 (6), 113 (6), +2 more |
| 79122 | 404 (118..532) | 364 | 28 | 66 (83), 86 (71), 44 (67), 67 (44), 85 (25), 137 (24), 42 (18), 53 (15), 83 (8), 54 (2), 60 (2), 113 (2), +3 more |
| 79132 | 391 (120..515) | 341 | 32 | 173 (78), 44 (76), 86 (42), 85 (28), 92 (26), 162 (25), 53 (20), 67 (18), 113 (12), 82 (4), 91 (4), 60 (3), +3 more |
| 79128 | 402 (124..527) | 363 | 30 | 113 (73), 174 (72), 67 (64), 44 (26), 162 (26), 82 (25), 173 (21), 42 (18), 66 (16), 83 (13), 54 (3), 60 (2), +3 more |
| 79134 | 407 (127..533) | 381 | 20 | 53 (124), 82 (104), 83 (79), 66 (18), 113 (14), 42 (11), 60 (9), 174 (7), 173 (6), 91 (4), 54 (2), 67 (1), +2 more |
| 79135 | 409 (129..542) | 369 | 31 | 137 (83), 82 (75), 60 (63), 42 (39), 66 (35), 113 (27), 83 (14), 44 (13), 53 (9), 91 (8), 54 (3) |
| 79139 | 406 (132..537) | 364 | 33 | 82 (181), 91 (105), 44 (39), 60 (24), 113 (9), 54 (4), 204 (2) |
| 79136 | 393 (136..538) | 363 | 25 | 60 (287), 66 (61), 54 (13), 82 (1), 137 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 50/380/682; tracks with internal gaps: 31; total internal gaps: 369; longest internal gap: 8; tracks ending in coasting: 31 (trailing rows total 933)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..370 | 369 | 369 | 316 | 53 | 6 | 2 | 46 | 78911 |
| 34 | 78..458 | 381 | 381 | 326 | 55 | 18 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 38 | 82..463 | 382 | 382 | 326 | 56 | 17 | 6 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 42 | 86..513 | 428 | 428 | 373 | 55 | 15 | 2 | 36 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 43 | 86..468 | 383 | 383 | 336 | 47 | 15 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 44 | 89..468 | 380 | 380 | 342 | 38 | 7 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 91..496 | 406 | 406 | 365 | 41 | 12 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..472 | 380 | 380 | 334 | 46 | 13 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 49 | 97..393 | 297 | 297 | 246 | 51 | 10 | 7 | 34 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 53 | 100..562 | 463 | 463 | 418 | 45 | 12 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 54 | 100..178 | 79 | 79 | 45 | 34 | 4 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 108..566 | 459 | 459 | 404 | 55 | 22 | 2 | 28 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 111..560 | 450 | 450 | 399 | 51 | 16 | 3 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 67 | 111..423 | 313 | 313 | 265 | 48 | 13 | 3 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 68 | 111..513 | 403 | 403 | 351 | 52 | 15 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 79 | 126..296 | 171 | 171 | 132 | 39 | 8 | 2 | 30 | 78969, 78971, 79037, 79045 |
| 82 | 129..566 | 438 | 438 | 390 | 48 | 14 | 2 | 31 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..525 | 396 | 396 | 348 | 48 | 14 | 2 | 33 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79134, 79135 |
| 85 | 130..529 | 400 | 400 | 353 | 47 | 16 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 86 | 133..559 | 427 | 427 | 383 | 44 | 13 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 133..490 | 358 | 358 | 313 | 45 | 13 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 91 | 138..392 | 255 | 255 | 213 | 42 | 9 | 3 | 30 | 79102, 79103, 79105, 79108, 79110, 79132, 79134, 79135, 79139 |
| 92 | 138..336 | 199 | 199 | 159 | 40 | 7 | 2 | 31 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 95 | 146..484 | 339 | 339 | 295 | 44 | 11 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 113 | 213..506 | 294 | 294 | 243 | 51 | 13 | 8 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 137 | 290..571 | 282 | 282 | 233 | 49 | 14 | 4 | 29 | 79105, 79108, 79110, 79111, 79115, 79122, 79132, 79135, 79136 |
| 153 | 327..1008 | 682 | 682 | 656 | 26 | 22 | 2 | 0 | 78911 |
| 162 | 349..526 | 178 | 178 | 141 | 37 | 3 | 5 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 173 | 383..544 | 162 | 162 | 123 | 39 | 7 | 3 | 29 | 79116, 79128, 79132, 79134 |
| 174 | 383..556 | 174 | 174 | 135 | 39 | 7 | 3 | 29 | 79110, 79111, 79115, 79122, 79128, 79134 |
| 193 | 425..474 | 50 | 50 | 21 | 29 | 0 | 0 | 29 | 79037 |
| 204 | 454..561 | 108 | 108 | 77 | 31 | 3 | 4 | 24 | 79115, 79122, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9061; unmatched reference entries: 1081; unmatched candidate entries: 1425
- identity switches: 1030; fragmentation (coverage interruptions): 789; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 44 -> 46 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 42 -> 44 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 47 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 54 -> 42 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 42 -> 44 at (2124.5, 3027.5), 3 frames after previous cover
- f103: ref 79105: 54 -> 42 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 43 -> 49 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79102: 44 -> 42 at (2119, 3027), 1 frames after previous cover
- f105: ref 78971: 49 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 38 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 38 -> 49 at (2030.5, 3033.5), 1 frames after previous cover
- f106: ref 79102: 42 -> 44 at (2107.5, 3028.5), 2 frames after previous cover
- f107: ref 78971: 43 -> 49 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 49 -> 38 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 78897: 47 -> 46 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 38 -> 47 at (2026, 3034), 2 frames after previous cover
- f108: ref 79108: 54 -> 60 at (2131, 3027), 3 frames after previous cover
- f111: ref 78897: 46 -> 47 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 38 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79045: 38 -> 43 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 53 -> 66 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 44 -> 53 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79103: 42 -> 67 at (2087.5, 3023.5), 9 frames after previous cover
- f111: ref 79105: 42 -> 68 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 44 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 54 -> 42 at (2129, 3027), 3 frames after previous cover
- f111: ref 79111: 54 -> 60 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 44 -> 67 at (2072.5, 3029.5), 2 frames after previous cover
- f113: ref 78969: 43 -> 49 at (1953.5, 3035.5), 3 frames after previous cover
- f113: ref 79103: 67 -> 68 at (2074, 3024.5), 2 frames after previous cover
- f113: ref 79105: 68 -> 42 at (2085, 3025), 1 frames after previous cover
- f114: ref 78899: 46 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 79097: 66 -> 46 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 53 -> 66 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 68 -> 53 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 42 -> 68 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 44 -> 67 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 42 -> 44 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 60 -> 42 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 54 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 43 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 78969: 49 -> 34 at (1939.5, 3036), 1 frames after previous cover
- f115: ref 79045: 43 -> 49 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78897: 43 -> 47 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 47 -> 46 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79037: 38 -> 43 at (1976, 3034.5), 1 frames after previous cover
- f116: ref 79045: 49 -> 38 at (1963.5, 3035.5), 1 frames after previous cover
- ... 970 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 972 | 29 | 153 (656), 0 (316) |
| 78896 | 350 (76..429) | 309 | 26 | 34 (169), 95 (81), 49 (34), 68 (25) |
| 78969 | 352 (80..434) | 307 | 32 | 79 (112), 38 (82), 34 (31), 49 (26), 95 (26), 68 (20), 43 (10) |
| 78971 | 352 (84..439) | 315 | 24 | 95 (94), 43 (89), 38 (65), 49 (35), 68 (18), 79 (13), 34 (1) |
| 79045 | 355 (84..443) | 310 | 24 | 38 (131), 47 (70), 49 (47), 95 (38), 68 (12), 43 (9), 79 (2), 34 (1) |
| 79037 | 355 (86..445) | 312 | 34 | 49 (93), 34 (51), 38 (43), 47 (35), 43 (24), 193 (21), 46 (15), 95 (10), 79 (5), 87 (5), 68 (5), 42 (3), +1 more |
| 78897 | 345 (89..450) | 299 | 36 | 46 (82), 47 (51), 95 (35), 66 (29), 43 (28), 68 (28), 87 (21), 49 (11), 38 (5), 34 (4), 44 (3), 42 (2) |
| 78899 | 365 (91..455) | 321 | 37 | 68 (79), 87 (70), 47 (48), 46 (43), 43 (22), 66 (21), 34 (19), 95 (11), 44 (4), 42 (3), 53 (1) |
| 79097 | 366 (94..461) | 329 | 29 | 87 (59), 68 (57), 46 (50), 43 (50), 66 (39), 34 (24), 85 (22), 47 (13), 53 (11), 42 (3), 44 (1) |
| 79098 | 360 (97..467) | 314 | 34 | 87 (73), 43 (72), 46 (70), 66 (25), 34 (25), 85 (13), 47 (12), 53 (8), 44 (6), 68 (6), 42 (2), 83 (2) |
| 79102 | 371 (98..477) | 331 | 33 | 46 (55), 113 (53), 47 (50), 83 (48), 68 (27), 43 (27), 42 (19), 87 (15), 92 (11), 53 (7), 44 (6), 91 (4), +4 more |
| 79103 | 380 (99..481) | 323 | 37 | 83 (48), 68 (44), 47 (39), 46 (38), 113 (36), 85 (34), 91 (29), 53 (15), 42 (12), 87 (10), 66 (5), 43 (5), +3 more |
| 79105 | 379 (101..484) | 327 | 37 | 83 (78), 53 (36), 42 (33), 91 (29), 85 (29), 68 (26), 137 (22), 92 (20), 87 (19), 47 (16), 46 (9), 66 (6), +3 more |
| 79108 | 385 (104..492) | 324 | 44 | 137 (42), 83 (39), 42 (39), 87 (37), 162 (35), 91 (24), 92 (23), 67 (22), 53 (18), 85 (10), 86 (8), 66 (7), +6 more |
| 79110 | 388 (106..497) | 342 | 33 | 86 (50), 42 (48), 85 (48), 53 (43), 162 (30), 67 (22), 137 (21), 44 (20), 66 (15), 83 (15), 174 (14), 91 (6), +4 more |
| 79111 | 386 (109..500) | 345 | 32 | 85 (78), 53 (56), 67 (47), 42 (45), 86 (39), 174 (21), 137 (14), 66 (14), 44 (12), 92 (8), 60 (3), 54 (2), +3 more |
| 79115 | 421 (111..531) | 364 | 38 | 204 (74), 53 (43), 85 (41), 86 (40), 92 (36), 42 (31), 137 (25), 174 (20), 66 (17), 162 (14), 67 (8), 60 (6), +4 more |
| 79116 | 411 (114..530) | 372 | 31 | 86 (132), 44 (60), 42 (44), 67 (33), 92 (26), 85 (19), 173 (18), 53 (11), 162 (7), 54 (6), 66 (6), 113 (6), +2 more |
| 79122 | 404 (118..532) | 364 | 28 | 66 (83), 86 (71), 44 (67), 67 (44), 85 (25), 137 (24), 42 (18), 53 (15), 83 (8), 54 (2), 60 (2), 113 (2), +3 more |
| 79132 | 391 (120..515) | 341 | 32 | 173 (78), 44 (76), 86 (42), 85 (28), 92 (26), 162 (25), 53 (20), 67 (18), 113 (12), 82 (4), 91 (4), 60 (3), +3 more |
| 79128 | 402 (124..527) | 363 | 30 | 113 (73), 174 (72), 67 (64), 44 (26), 162 (26), 82 (25), 173 (21), 42 (18), 66 (16), 83 (13), 54 (3), 60 (2), +3 more |
| 79134 | 407 (127..533) | 381 | 20 | 53 (124), 82 (104), 83 (79), 66 (18), 113 (14), 42 (11), 60 (9), 174 (7), 173 (6), 91 (4), 54 (2), 67 (1), +2 more |
| 79135 | 409 (129..542) | 369 | 31 | 137 (83), 82 (75), 60 (63), 42 (39), 66 (35), 113 (27), 83 (14), 44 (13), 53 (9), 91 (8), 54 (3) |
| 79139 | 406 (132..537) | 364 | 33 | 82 (181), 91 (105), 44 (39), 60 (24), 113 (9), 54 (4), 204 (2) |
| 79136 | 393 (136..538) | 363 | 25 | 60 (287), 66 (61), 54 (13), 82 (1), 137 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 50/380/682; tracks with internal gaps: 31; total internal gaps: 369; longest internal gap: 8; tracks ending in coasting: 31 (trailing rows total 933)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..370 | 369 | 369 | 316 | 53 | 6 | 2 | 46 | 78911 |
| 34 | 78..458 | 381 | 381 | 326 | 55 | 18 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 38 | 82..463 | 382 | 382 | 326 | 56 | 17 | 6 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 42 | 86..513 | 428 | 428 | 373 | 55 | 15 | 2 | 36 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 43 | 86..468 | 383 | 383 | 336 | 47 | 15 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 44 | 89..468 | 380 | 380 | 342 | 38 | 7 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 91..496 | 406 | 406 | 365 | 41 | 12 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..472 | 380 | 380 | 334 | 46 | 13 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 49 | 97..393 | 297 | 297 | 246 | 51 | 10 | 7 | 34 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 53 | 100..562 | 463 | 463 | 418 | 45 | 12 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 54 | 100..178 | 79 | 79 | 45 | 34 | 4 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 60 | 108..566 | 459 | 459 | 404 | 55 | 22 | 2 | 28 | 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 66 | 111..560 | 450 | 450 | 399 | 51 | 16 | 3 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136 |
| 67 | 111..423 | 313 | 313 | 265 | 48 | 13 | 3 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 68 | 111..513 | 403 | 403 | 351 | 52 | 15 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 79 | 126..296 | 171 | 171 | 132 | 39 | 8 | 2 | 30 | 78969, 78971, 79037, 79045 |
| 82 | 129..566 | 438 | 438 | 390 | 48 | 14 | 2 | 31 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 130..525 | 396 | 396 | 348 | 48 | 14 | 2 | 33 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79134, 79135 |
| 85 | 130..529 | 400 | 400 | 353 | 47 | 16 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 86 | 133..559 | 427 | 427 | 383 | 44 | 13 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 133..490 | 358 | 358 | 313 | 45 | 13 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115 |
| 91 | 138..392 | 255 | 255 | 213 | 42 | 9 | 3 | 30 | 79102, 79103, 79105, 79108, 79110, 79132, 79134, 79135, 79139 |
| 92 | 138..336 | 199 | 199 | 159 | 40 | 7 | 2 | 31 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 95 | 146..484 | 339 | 339 | 295 | 44 | 11 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 113 | 213..506 | 294 | 294 | 243 | 51 | 13 | 8 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 137 | 290..571 | 282 | 282 | 233 | 49 | 14 | 4 | 29 | 79105, 79108, 79110, 79111, 79115, 79122, 79132, 79135, 79136 |
| 153 | 327..1008 | 682 | 682 | 656 | 26 | 22 | 2 | 0 | 78911 |
| 162 | 349..526 | 178 | 178 | 141 | 37 | 3 | 5 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 173 | 383..544 | 162 | 162 | 123 | 39 | 7 | 3 | 29 | 79116, 79128, 79132, 79134 |
| 174 | 383..556 | 174 | 174 | 135 | 39 | 7 | 3 | 29 | 79110, 79111, 79115, 79122, 79128, 79134 |
| 193 | 425..474 | 50 | 50 | 21 | 29 | 0 | 0 | 29 | 79037 |
| 204 | 454..561 | 108 | 108 | 77 | 31 | 3 | 4 | 24 | 79115, 79122, 79139 |
