# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=f02f33d6fd21
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise0.0_fp0.0_seed1/tracks.csv sha256=d22b99c3cc17f7cc
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise0.0_fp0.0_seed1.csv sha256=f02f33d6fd21361c
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise0.0_fp0.0_seed1
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
| observations | none | 4 | 0.365 | 0.193 | 0.609 | 0.01 | 0.348 | 855 | 2020.0 |
| observations | none | 6 | 0.365 | 0.194 | 0.610 | 0.02 | 0.348 | 849 | 2020.0 |
| observations | none | 8 | 0.365 | 0.195 | 0.610 | 0.05 | 0.351 | 846 | 2011.0 |
| observations | none | 12 | 0.365 | 0.201 | 0.616 | 0.34 | 0.363 | 779 | 1963.0 |
| observations | ignore | 4 | 0.365 | 0.193 | 0.609 | 0.01 | 0.348 | 855 | 2020.0 |
| observations | ignore | 6 | 0.365 | 0.194 | 0.610 | 0.02 | 0.348 | 849 | 2020.0 |
| observations | ignore | 8 | 0.365 | 0.195 | 0.610 | 0.05 | 0.351 | 846 | 2011.0 |
| observations | ignore | 12 | 0.365 | 0.201 | 0.616 | 0.34 | 0.363 | 779 | 1963.0 |
| updates | none | 4 | 0.338 | 0.189 | 0.382 | 0.14 | 0.318 | 892 | 1894.0 |
| updates | none | 6 | 0.370 | 0.208 | 0.504 | 0.54 | 0.348 | 919 | 1486.0 |
| updates | none | 8 | 0.391 | 0.222 | 0.638 | 1.08 | 0.385 | 886 | 1003.0 |
| updates | none | 12 | 0.416 | 0.241 | 0.687 | 1.58 | 0.410 | 797 | 831.0 |
| updates | ignore | 4 | 0.338 | 0.189 | 0.382 | 0.14 | 0.318 | 892 | 1894.0 |
| updates | ignore | 6 | 0.370 | 0.208 | 0.504 | 0.54 | 0.348 | 919 | 1486.0 |
| updates | ignore | 8 | 0.391 | 0.222 | 0.638 | 1.08 | 0.385 | 886 | 1003.0 |
| updates | ignore | 12 | 0.416 | 0.241 | 0.687 | 1.58 | 0.410 | 797 | 831.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7031; unmatched reference entries: 3111; unmatched candidate entries: 0
- identity switches: 846; fragmentation (coverage interruptions): 2070; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 9 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 7 -> 3 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 7 -> 12 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 7 -> 12 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 9 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 7 -> 12 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 12 -> 14 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 9 -> 7 at (2141, 3029), 2 frames after previous cover
- f97: ref 79045: 12 -> 14 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 7 -> 9 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 14 -> 15 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 9 -> 7 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 9 -> 7 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 3 -> 15 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79045: 15 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 7 -> 9 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 12 -> 7 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 7 -> 9 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 9 -> 7 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 15 -> 3 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 14 -> 15 at (2036.5, 3033.5), 3 frames after previous cover
- f105: ref 78899: 7 -> 14 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 3 -> 15 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 9 -> 12 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 12 -> 17 at (2120.5, 3023), 5 frames after previous cover
- f106: ref 79103: 17 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 12 -> 17 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 12 -> 7 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 7 -> 14 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 14 -> 12 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 12 -> 14 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 7 -> 12 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 15 -> 8 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 12 -> 9 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 12 -> 17 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 14 -> 12 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 14 -> 24 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 12 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 9 -> 25 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 17 -> 9 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 14 -> 24 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 9 -> 7 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 17 -> 9 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 9 -> 23 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 8 -> 3 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 24 -> 8 at (1988, 3035), 3 frames after previous cover
- f114: ref 79045: 8 -> 15 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79105: 9 -> 25 at (2079, 3025), 1 frames after previous cover
- f114: ref 79110: 17 -> 23 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 22 -> 17 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 3 -> 8 at (1939.5, 3036), 3 frames after previous cover
- f115: ref 79098: 7 -> 14 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79105: 25 -> 9 at (2073, 3025), 1 frames after previous cover
- f115: ref 79115: 23 -> 22 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 14 -> 12 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 8 -> 3 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 15 -> 8 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 23 -> 9 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 12 -> 24 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 3 -> 8 at (1921, 3034.5), 2 frames after previous cover
- ... 786 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 698 | 209 | 1 (698) |
| 78896 | 350 (76..429) | 242 | 65 | 38 (160), 39 (47), 8 (20), 3 (15) |
| 78969 | 352 (80..434) | 254 | 71 | 3 (245), 8 (5), 35 (4) |
| 78971 | 352 (84..439) | 228 | 71 | 35 (154), 12 (37), 15 (12), 38 (10), 8 (7), 3 (3), 39 (3), 7 (2) |
| 79045 | 355 (84..443) | 245 | 73 | 39 (164), 15 (34), 12 (15), 38 (11), 35 (8), 8 (6), 34 (4), 14 (2), 7 (1) |
| 79037 | 355 (86..445) | 247 | 65 | 12 (179), 38 (29), 15 (16), 39 (7), 14 (6), 31 (5), 7 (3), 24 (1), 8 (1) |
| 78897 | 345 (89..450) | 228 | 73 | 44 (121), 15 (29), 22 (25), 38 (12), 12 (11), 34 (7), 35 (7), 24 (4), 31 (4), 7 (3), 9 (2), 14 (2), +1 more |
| 78899 | 365 (91..455) | 267 | 72 | 15 (133), 34 (37), 35 (26), 31 (22), 8 (19), 14 (8), 44 (6), 7 (5), 9 (3), 12 (3), 24 (3), 22 (2) |
| 79097 | 366 (94..461) | 247 | 78 | 8 (90), 35 (35), 15 (33), 34 (28), 31 (21), 12 (16), 44 (10), 7 (6), 9 (3), 43 (3), 22 (2) |
| 79098 | 360 (97..467) | 257 | 82 | 24 (71), 8 (70), 22 (45), 34 (34), 7 (8), 15 (6), 14 (5), 44 (5), 9 (4), 43 (3), 12 (2), 31 (2), +1 more |
| 79102 | 371 (98..477) | 238 | 81 | 34 (54), 22 (49), 8 (44), 44 (28), 24 (24), 43 (15), 9 (6), 7 (6), 14 (4), 23 (3), 15 (2), 31 (2), +1 more |
| 79103 | 380 (99..481) | 265 | 76 | 22 (54), 8 (39), 17 (36), 24 (35), 23 (35), 44 (20), 34 (13), 31 (11), 25 (7), 14 (5), 12 (4), 15 (3), +2 more |
| 79105 | 379 (101..484) | 268 | 78 | 31 (65), 24 (56), 17 (55), 44 (24), 23 (23), 22 (22), 34 (7), 9 (5), 25 (5), 8 (3), 12 (1), 15 (1), +1 more |
| 79108 | 385 (104..492) | 268 | 81 | 31 (58), 22 (37), 9 (35), 25 (30), 23 (29), 17 (25), 24 (24), 34 (10), 14 (7), 41 (7), 7 (5), 12 (1) |
| 79110 | 388 (106..497) | 271 | 78 | 34 (53), 25 (46), 17 (43), 31 (27), 41 (23), 24 (20), 27 (19), 14 (11), 43 (10), 23 (7), 22 (6), 7 (4), +1 more |
| 79111 | 386 (109..500) | 271 | 80 | 31 (72), 24 (31), 17 (25), 41 (22), 43 (20), 27 (20), 25 (19), 14 (19), 23 (14), 34 (12), 7 (11), 22 (4), +1 more |
| 79115 | 421 (111..531) | 296 | 74 | 25 (76), 14 (70), 7 (57), 17 (50), 41 (15), 23 (12), 43 (9), 27 (3), 22 (2), 9 (1), 34 (1) |
| 79116 | 411 (114..530) | 280 | 88 | 41 (70), 37 (53), 7 (40), 17 (35), 14 (27), 43 (18), 23 (14), 27 (8), 25 (6), 34 (4), 9 (3), 22 (2) |
| 79122 | 404 (118..532) | 280 | 88 | 14 (76), 41 (74), 17 (27), 37 (26), 23 (24), 43 (22), 25 (11), 22 (6), 9 (6), 27 (5), 7 (3) |
| 79132 | 391 (120..515) | 274 | 81 | 24 (45), 41 (41), 27 (40), 7 (39), 14 (38), 37 (23), 25 (12), 9 (11), 23 (9), 22 (8), 17 (6), 43 (2) |
| 79128 | 402 (124..527) | 284 | 82 | 14 (63), 37 (52), 25 (46), 41 (35), 43 (21), 27 (18), 23 (16), 9 (14), 7 (12), 17 (4), 22 (3) |
| 79134 | 407 (127..533) | 271 | 86 | 43 (110), 7 (58), 27 (54), 25 (20), 37 (12), 9 (9), 22 (4), 41 (2), 23 (1), 14 (1) |
| 79135 | 409 (129..542) | 290 | 84 | 27 (108), 23 (80), 7 (49), 9 (19), 43 (15), 22 (11), 25 (6), 37 (2) |
| 79139 | 406 (132..537) | 293 | 77 | 9 (116), 23 (70), 43 (41), 45 (21), 7 (16), 25 (13), 27 (10), 41 (3), 37 (2), 22 (1) |
| 79136 | 393 (136..538) | 269 | 77 | 37 (113), 9 (64), 45 (44), 27 (25), 7 (21), 43 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 94/384/1003; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1007 | 1003 | 698 | 698 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 82..434 | 353 | 263 | 263 | 0 | 0 | 0 | 0 | 78896, 78969, 78971 |
| 7 | 86..531 | 446 | 350 | 350 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..477 | 389 | 305 | 305 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 89..491 | 403 | 307 | 307 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 12 | 92..439 | 348 | 269 | 269 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 14 | 96..527 | 432 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 15 | 99..443 | 345 | 269 | 269 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 105..481 | 377 | 307 | 307 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 22 | 111..450 | 340 | 283 | 283 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 111..542 | 432 | 337 | 337 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 111..515 | 405 | 314 | 314 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 25 | 112..496 | 385 | 297 | 297 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 118..533 | 416 | 310 | 310 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 31 | 124..500 | 377 | 289 | 289 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 34 | 124..467 | 344 | 264 | 264 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 35 | 129..461 | 333 | 236 | 236 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098 |
| 37 | 138..530 | 393 | 283 | 283 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 138..445 | 308 | 222 | 222 | 0 | 0 | 0 | 0 | 78896, 78897, 78971, 79037, 79045 |
| 39 | 138..429 | 292 | 221 | 221 | 0 | 0 | 0 | 0 | 78896, 78971, 79037, 79045 |
| 41 | 139..532 | 394 | 293 | 293 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 43 | 154..537 | 384 | 291 | 291 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 172..484 | 313 | 214 | 214 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 45 | 445..538 | 94 | 65 | 65 | 0 | 0 | 0 | 0 | 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7031; unmatched reference entries: 3111; unmatched candidate entries: 0
- identity switches: 846; fragmentation (coverage interruptions): 2070; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 9 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 7 -> 3 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 7 -> 12 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 7 -> 12 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 9 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 7 -> 12 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 12 -> 14 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 9 -> 7 at (2141, 3029), 2 frames after previous cover
- f97: ref 79045: 12 -> 14 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 7 -> 9 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 14 -> 15 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 9 -> 7 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 9 -> 7 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 3 -> 15 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79045: 15 -> 14 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 7 -> 9 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 12 -> 7 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 7 -> 9 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 9 -> 7 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 15 -> 3 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 14 -> 15 at (2036.5, 3033.5), 3 frames after previous cover
- f105: ref 78899: 7 -> 14 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 3 -> 15 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 9 -> 12 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 12 -> 17 at (2120.5, 3023), 5 frames after previous cover
- f106: ref 79103: 17 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 12 -> 17 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 12 -> 7 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 7 -> 14 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 14 -> 12 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 12 -> 14 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 7 -> 12 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 15 -> 8 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 12 -> 9 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 12 -> 17 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 14 -> 12 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 14 -> 24 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 12 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 9 -> 25 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 17 -> 9 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 14 -> 24 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 9 -> 7 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 17 -> 9 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 9 -> 23 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 8 -> 3 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 24 -> 8 at (1988, 3035), 3 frames after previous cover
- f114: ref 79045: 8 -> 15 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79105: 9 -> 25 at (2079, 3025), 1 frames after previous cover
- f114: ref 79110: 17 -> 23 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 22 -> 17 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 3 -> 8 at (1939.5, 3036), 3 frames after previous cover
- f115: ref 79098: 7 -> 14 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79105: 25 -> 9 at (2073, 3025), 1 frames after previous cover
- f115: ref 79115: 23 -> 22 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 14 -> 12 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 8 -> 3 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 15 -> 8 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 23 -> 9 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 12 -> 24 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 3 -> 8 at (1921, 3034.5), 2 frames after previous cover
- ... 786 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 698 | 209 | 1 (698) |
| 78896 | 350 (76..429) | 242 | 65 | 38 (160), 39 (47), 8 (20), 3 (15) |
| 78969 | 352 (80..434) | 254 | 71 | 3 (245), 8 (5), 35 (4) |
| 78971 | 352 (84..439) | 228 | 71 | 35 (154), 12 (37), 15 (12), 38 (10), 8 (7), 3 (3), 39 (3), 7 (2) |
| 79045 | 355 (84..443) | 245 | 73 | 39 (164), 15 (34), 12 (15), 38 (11), 35 (8), 8 (6), 34 (4), 14 (2), 7 (1) |
| 79037 | 355 (86..445) | 247 | 65 | 12 (179), 38 (29), 15 (16), 39 (7), 14 (6), 31 (5), 7 (3), 24 (1), 8 (1) |
| 78897 | 345 (89..450) | 228 | 73 | 44 (121), 15 (29), 22 (25), 38 (12), 12 (11), 34 (7), 35 (7), 24 (4), 31 (4), 7 (3), 9 (2), 14 (2), +1 more |
| 78899 | 365 (91..455) | 267 | 72 | 15 (133), 34 (37), 35 (26), 31 (22), 8 (19), 14 (8), 44 (6), 7 (5), 9 (3), 12 (3), 24 (3), 22 (2) |
| 79097 | 366 (94..461) | 247 | 78 | 8 (90), 35 (35), 15 (33), 34 (28), 31 (21), 12 (16), 44 (10), 7 (6), 9 (3), 43 (3), 22 (2) |
| 79098 | 360 (97..467) | 257 | 82 | 24 (71), 8 (70), 22 (45), 34 (34), 7 (8), 15 (6), 14 (5), 44 (5), 9 (4), 43 (3), 12 (2), 31 (2), +1 more |
| 79102 | 371 (98..477) | 238 | 81 | 34 (54), 22 (49), 8 (44), 44 (28), 24 (24), 43 (15), 9 (6), 7 (6), 14 (4), 23 (3), 15 (2), 31 (2), +1 more |
| 79103 | 380 (99..481) | 265 | 76 | 22 (54), 8 (39), 17 (36), 24 (35), 23 (35), 44 (20), 34 (13), 31 (11), 25 (7), 14 (5), 12 (4), 15 (3), +2 more |
| 79105 | 379 (101..484) | 268 | 78 | 31 (65), 24 (56), 17 (55), 44 (24), 23 (23), 22 (22), 34 (7), 9 (5), 25 (5), 8 (3), 12 (1), 15 (1), +1 more |
| 79108 | 385 (104..492) | 268 | 81 | 31 (58), 22 (37), 9 (35), 25 (30), 23 (29), 17 (25), 24 (24), 34 (10), 14 (7), 41 (7), 7 (5), 12 (1) |
| 79110 | 388 (106..497) | 271 | 78 | 34 (53), 25 (46), 17 (43), 31 (27), 41 (23), 24 (20), 27 (19), 14 (11), 43 (10), 23 (7), 22 (6), 7 (4), +1 more |
| 79111 | 386 (109..500) | 271 | 80 | 31 (72), 24 (31), 17 (25), 41 (22), 43 (20), 27 (20), 25 (19), 14 (19), 23 (14), 34 (12), 7 (11), 22 (4), +1 more |
| 79115 | 421 (111..531) | 296 | 74 | 25 (76), 14 (70), 7 (57), 17 (50), 41 (15), 23 (12), 43 (9), 27 (3), 22 (2), 9 (1), 34 (1) |
| 79116 | 411 (114..530) | 280 | 88 | 41 (70), 37 (53), 7 (40), 17 (35), 14 (27), 43 (18), 23 (14), 27 (8), 25 (6), 34 (4), 9 (3), 22 (2) |
| 79122 | 404 (118..532) | 280 | 88 | 14 (76), 41 (74), 17 (27), 37 (26), 23 (24), 43 (22), 25 (11), 22 (6), 9 (6), 27 (5), 7 (3) |
| 79132 | 391 (120..515) | 274 | 81 | 24 (45), 41 (41), 27 (40), 7 (39), 14 (38), 37 (23), 25 (12), 9 (11), 23 (9), 22 (8), 17 (6), 43 (2) |
| 79128 | 402 (124..527) | 284 | 82 | 14 (63), 37 (52), 25 (46), 41 (35), 43 (21), 27 (18), 23 (16), 9 (14), 7 (12), 17 (4), 22 (3) |
| 79134 | 407 (127..533) | 271 | 86 | 43 (110), 7 (58), 27 (54), 25 (20), 37 (12), 9 (9), 22 (4), 41 (2), 23 (1), 14 (1) |
| 79135 | 409 (129..542) | 290 | 84 | 27 (108), 23 (80), 7 (49), 9 (19), 43 (15), 22 (11), 25 (6), 37 (2) |
| 79139 | 406 (132..537) | 293 | 77 | 9 (116), 23 (70), 43 (41), 45 (21), 7 (16), 25 (13), 27 (10), 41 (3), 37 (2), 22 (1) |
| 79136 | 393 (136..538) | 269 | 77 | 37 (113), 9 (64), 45 (44), 27 (25), 7 (21), 43 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 94/384/1003; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1007 | 1003 | 698 | 698 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 82..434 | 353 | 263 | 263 | 0 | 0 | 0 | 0 | 78896, 78969, 78971 |
| 7 | 86..531 | 446 | 350 | 350 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..477 | 389 | 305 | 305 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 89..491 | 403 | 307 | 307 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 12 | 92..439 | 348 | 269 | 269 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 14 | 96..527 | 432 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 15 | 99..443 | 345 | 269 | 269 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 105..481 | 377 | 307 | 307 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 22 | 111..450 | 340 | 283 | 283 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 111..542 | 432 | 337 | 337 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 111..515 | 405 | 314 | 314 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 25 | 112..496 | 385 | 297 | 297 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 118..533 | 416 | 310 | 310 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 31 | 124..500 | 377 | 289 | 289 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 34 | 124..467 | 344 | 264 | 264 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 35 | 129..461 | 333 | 236 | 236 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098 |
| 37 | 138..530 | 393 | 283 | 283 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 138..445 | 308 | 222 | 222 | 0 | 0 | 0 | 0 | 78896, 78897, 78971, 79037, 79045 |
| 39 | 138..429 | 292 | 221 | 221 | 0 | 0 | 0 | 0 | 78896, 78971, 79037, 79045 |
| 41 | 139..532 | 394 | 293 | 293 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 43 | 154..537 | 384 | 291 | 291 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 172..484 | 313 | 214 | 214 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 45 | 445..538 | 94 | 65 | 65 | 0 | 0 | 0 | 0 | 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8665; unmatched reference entries: 1477; unmatched candidate entries: 1309
- identity switches: 886; fragmentation (coverage interruptions): 941; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 9 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 7 -> 3 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 7 -> 12 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 7 -> 12 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 9 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 7 -> 12 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 12 -> 14 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 9 -> 7 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 12 -> 14 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 7 -> 9 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 14 -> 15 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 9 -> 7 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 9 -> 7 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 3 -> 14 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79098: 7 -> 9 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 12 -> 7 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 7 -> 9 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 78971: 14 -> 15 at (2033, 3032.5), 2 frames after previous cover
- f103: ref 79097: 9 -> 7 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 15 -> 3 at (2027.5, 3034.5), 1 frames after previous cover
- f105: ref 78899: 7 -> 14 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 3 -> 15 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 9 -> 12 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 12 -> 17 at (2120.5, 3023), 4 frames after previous cover
- f106: ref 79103: 17 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 12 -> 17 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 12 -> 7 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 7 -> 14 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 14 -> 12 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 12 -> 14 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 7 -> 12 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 15 -> 8 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 12 -> 9 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 12 -> 17 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 14 -> 12 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 14 -> 24 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 12 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 9 -> 25 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 17 -> 9 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 14 -> 24 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 9 -> 7 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 17 -> 9 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 9 -> 23 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 8 -> 3 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 24 -> 8 at (1988, 3035), 2 frames after previous cover
- f114: ref 79045: 8 -> 15 at (1976.5, 3034.5), 1 frames after previous cover
- f114: ref 79110: 17 -> 23 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 22 -> 17 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 3 -> 8 at (1939.5, 3036), 2 frames after previous cover
- f115: ref 79098: 7 -> 14 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79115: 23 -> 22 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 14 -> 12 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 8 -> 3 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 15 -> 8 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 23 -> 9 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 12 -> 24 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 3 -> 8 at (1921, 3034.5), 1 frames after previous cover
- f118: ref 79037: 8 -> 15 at (1964, 3035.5), 4 frames after previous cover
- f118: ref 79098: 14 -> 12 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79102: 7 -> 14 at (2036.5, 3029.5), 1 frames after previous cover
- ... 826 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 962 | 25 | 1 (962) |
| 78896 | 350 (76..429) | 302 | 19 | 38 (204), 39 (59), 8 (21), 3 (18) |
| 78969 | 352 (80..434) | 318 | 23 | 3 (301), 8 (7), 35 (5), 38 (5) |
| 78971 | 352 (84..439) | 280 | 37 | 35 (194), 12 (44), 38 (13), 15 (11), 8 (9), 3 (3), 39 (3), 7 (2), 14 (1) |
| 79045 | 355 (84..443) | 301 | 32 | 39 (208), 15 (41), 12 (15), 38 (13), 35 (10), 8 (7), 34 (5), 7 (1), 14 (1) |
| 79037 | 355 (86..445) | 295 | 34 | 12 (216), 38 (33), 15 (18), 39 (10), 14 (7), 31 (5), 7 (3), 24 (2), 8 (1) |
| 78897 | 345 (89..450) | 277 | 38 | 44 (151), 15 (37), 22 (28), 38 (15), 12 (14), 34 (8), 35 (7), 31 (5), 24 (4), 7 (3), 9 (2), 14 (2), +1 more |
| 78899 | 365 (91..455) | 319 | 31 | 15 (161), 34 (43), 35 (34), 31 (26), 8 (24), 14 (8), 44 (6), 7 (5), 9 (3), 12 (3), 24 (3), 22 (3) |
| 79097 | 366 (94..461) | 302 | 43 | 8 (111), 35 (41), 15 (40), 34 (38), 31 (26), 12 (18), 44 (11), 7 (6), 43 (5), 9 (4), 22 (2) |
| 79098 | 360 (97..467) | 304 | 45 | 24 (93), 8 (76), 22 (52), 34 (42), 7 (8), 15 (6), 44 (6), 14 (5), 9 (4), 43 (4), 35 (4), 12 (2), +1 more |
| 79102 | 371 (98..477) | 282 | 52 | 34 (68), 22 (54), 8 (50), 44 (37), 24 (26), 43 (20), 9 (7), 7 (6), 14 (4), 23 (4), 15 (3), 31 (2), +1 more |
| 79103 | 380 (99..481) | 314 | 45 | 22 (58), 8 (51), 17 (41), 24 (40), 23 (40), 44 (28), 34 (17), 31 (15), 25 (7), 14 (6), 12 (5), 15 (3), +2 more |
| 79105 | 379 (101..484) | 324 | 35 | 31 (77), 17 (70), 24 (67), 44 (31), 23 (28), 22 (25), 34 (9), 9 (6), 25 (4), 8 (4), 12 (1), 15 (1), +1 more |
| 79108 | 385 (104..492) | 322 | 40 | 31 (70), 22 (46), 9 (42), 25 (36), 23 (35), 24 (31), 17 (29), 34 (12), 41 (9), 14 (6), 7 (5), 12 (1) |
| 79110 | 388 (106..497) | 324 | 42 | 34 (60), 25 (59), 17 (51), 31 (34), 41 (26), 24 (23), 27 (21), 43 (13), 14 (12), 23 (8), 22 (7), 9 (6), +1 more |
| 79111 | 386 (109..500) | 323 | 48 | 31 (90), 24 (37), 17 (30), 41 (28), 43 (27), 25 (24), 27 (22), 14 (20), 23 (15), 34 (13), 7 (11), 22 (4), +1 more |
| 79115 | 421 (111..531) | 348 | 44 | 25 (89), 14 (85), 7 (70), 17 (53), 41 (21), 43 (12), 23 (11), 22 (2), 27 (2), 34 (2), 9 (1) |
| 79116 | 411 (114..530) | 340 | 53 | 41 (89), 37 (69), 7 (46), 17 (40), 14 (31), 43 (22), 23 (15), 27 (10), 25 (7), 34 (5), 22 (3), 9 (3) |
| 79122 | 404 (118..532) | 347 | 42 | 41 (99), 14 (91), 17 (36), 37 (34), 23 (27), 43 (24), 25 (14), 22 (7), 27 (6), 9 (6), 7 (3) |
| 79132 | 391 (120..515) | 330 | 41 | 24 (56), 27 (51), 41 (50), 14 (47), 7 (44), 37 (27), 9 (16), 25 (12), 23 (10), 22 (8), 17 (6), 43 (3) |
| 79128 | 402 (124..527) | 343 | 41 | 14 (75), 37 (63), 25 (58), 41 (44), 43 (24), 23 (20), 27 (18), 9 (17), 7 (16), 22 (4), 17 (4) |
| 79134 | 407 (127..533) | 346 | 39 | 43 (146), 7 (73), 27 (60), 25 (29), 37 (13), 9 (12), 23 (5), 22 (4), 41 (3), 14 (1) |
| 79135 | 409 (129..542) | 361 | 40 | 27 (134), 23 (102), 7 (61), 9 (22), 43 (18), 22 (14), 25 (7), 37 (3) |
| 79139 | 406 (132..537) | 358 | 25 | 9 (146), 23 (94), 45 (69), 25 (18), 7 (16), 27 (7), 41 (3), 37 (3), 22 (1), 43 (1) |
| 79136 | 393 (136..538) | 343 | 27 | 37 (141), 9 (80), 43 (47), 27 (42), 7 (24), 45 (9) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 123/413/1004; tracks with internal gaps: 24; total internal gaps: 445; longest internal gap: 7; tracks ending in coasting: 23 (trailing rows total 656)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 962 | 42 | 25 | 4 | 0 | 78911 |
| 3 | 82..463 | 382 | 382 | 322 | 60 | 20 | 3 | 29 | 78896, 78969, 78971 |
| 7 | 86..560 | 475 | 475 | 408 | 67 | 28 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..506 | 418 | 418 | 362 | 56 | 19 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 89..520 | 432 | 432 | 381 | 51 | 14 | 5 | 23 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 12 | 92..468 | 377 | 377 | 319 | 58 | 21 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 14 | 96..556 | 461 | 461 | 402 | 59 | 21 | 7 | 26 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 15 | 99..472 | 374 | 374 | 321 | 53 | 17 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 105..510 | 406 | 406 | 361 | 45 | 15 | 2 | 26 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 22 | 111..479 | 369 | 369 | 322 | 47 | 15 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 111..571 | 461 | 461 | 414 | 47 | 15 | 2 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 111..544 | 434 | 434 | 382 | 52 | 20 | 2 | 29 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 25 | 112..525 | 414 | 414 | 364 | 50 | 14 | 5 | 31 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 118..562 | 445 | 445 | 373 | 72 | 28 | 5 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 31 | 124..529 | 406 | 406 | 352 | 54 | 17 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 34 | 124..496 | 373 | 373 | 322 | 51 | 15 | 3 | 31 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 35 | 129..490 | 362 | 362 | 295 | 67 | 23 | 4 | 23 | 78897, 78899, 78969, 78971, 79045, 79097, 79098 |
| 37 | 138..559 | 422 | 422 | 353 | 69 | 25 | 3 | 30 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 138..474 | 337 | 337 | 283 | 54 | 16 | 5 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 39 | 138..458 | 321 | 321 | 280 | 41 | 10 | 2 | 29 | 78896, 78971, 79037, 79045 |
| 41 | 139..561 | 423 | 423 | 373 | 50 | 17 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 43 | 154..566 | 413 | 413 | 366 | 47 | 13 | 3 | 28 | 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 172..513 | 342 | 342 | 270 | 72 | 29 | 4 | 31 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 45 | 445..567 | 123 | 123 | 78 | 45 | 8 | 3 | 30 | 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8665; unmatched reference entries: 1477; unmatched candidate entries: 1309
- identity switches: 886; fragmentation (coverage interruptions): 941; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 9 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 7 -> 3 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 7 -> 12 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 7 -> 12 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 9 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 7 -> 12 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 12 -> 14 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 9 -> 7 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 12 -> 14 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 7 -> 9 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 14 -> 15 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 9 -> 7 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 9 -> 7 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 3 -> 14 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79098: 7 -> 9 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 12 -> 7 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 7 -> 9 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 78971: 14 -> 15 at (2033, 3032.5), 2 frames after previous cover
- f103: ref 79097: 9 -> 7 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 15 -> 3 at (2027.5, 3034.5), 1 frames after previous cover
- f105: ref 78899: 7 -> 14 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 3 -> 15 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 9 -> 12 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 12 -> 17 at (2120.5, 3023), 4 frames after previous cover
- f106: ref 79103: 17 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 12 -> 17 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 12 -> 7 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 7 -> 14 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 14 -> 12 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 12 -> 14 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 7 -> 12 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 15 -> 8 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 12 -> 9 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 12 -> 17 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 14 -> 12 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 14 -> 24 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 12 -> 14 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 9 -> 25 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 17 -> 9 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 14 -> 24 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 9 -> 7 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 17 -> 9 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 9 -> 23 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 8 -> 3 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 24 -> 8 at (1988, 3035), 2 frames after previous cover
- f114: ref 79045: 8 -> 15 at (1976.5, 3034.5), 1 frames after previous cover
- f114: ref 79110: 17 -> 23 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 22 -> 17 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 3 -> 8 at (1939.5, 3036), 2 frames after previous cover
- f115: ref 79098: 7 -> 14 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79115: 23 -> 22 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 14 -> 12 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 8 -> 3 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 15 -> 8 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 23 -> 9 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 12 -> 24 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 3 -> 8 at (1921, 3034.5), 1 frames after previous cover
- f118: ref 79037: 8 -> 15 at (1964, 3035.5), 4 frames after previous cover
- f118: ref 79098: 14 -> 12 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79102: 7 -> 14 at (2036.5, 3029.5), 1 frames after previous cover
- ... 826 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 962 | 25 | 1 (962) |
| 78896 | 350 (76..429) | 302 | 19 | 38 (204), 39 (59), 8 (21), 3 (18) |
| 78969 | 352 (80..434) | 318 | 23 | 3 (301), 8 (7), 35 (5), 38 (5) |
| 78971 | 352 (84..439) | 280 | 37 | 35 (194), 12 (44), 38 (13), 15 (11), 8 (9), 3 (3), 39 (3), 7 (2), 14 (1) |
| 79045 | 355 (84..443) | 301 | 32 | 39 (208), 15 (41), 12 (15), 38 (13), 35 (10), 8 (7), 34 (5), 7 (1), 14 (1) |
| 79037 | 355 (86..445) | 295 | 34 | 12 (216), 38 (33), 15 (18), 39 (10), 14 (7), 31 (5), 7 (3), 24 (2), 8 (1) |
| 78897 | 345 (89..450) | 277 | 38 | 44 (151), 15 (37), 22 (28), 38 (15), 12 (14), 34 (8), 35 (7), 31 (5), 24 (4), 7 (3), 9 (2), 14 (2), +1 more |
| 78899 | 365 (91..455) | 319 | 31 | 15 (161), 34 (43), 35 (34), 31 (26), 8 (24), 14 (8), 44 (6), 7 (5), 9 (3), 12 (3), 24 (3), 22 (3) |
| 79097 | 366 (94..461) | 302 | 43 | 8 (111), 35 (41), 15 (40), 34 (38), 31 (26), 12 (18), 44 (11), 7 (6), 43 (5), 9 (4), 22 (2) |
| 79098 | 360 (97..467) | 304 | 45 | 24 (93), 8 (76), 22 (52), 34 (42), 7 (8), 15 (6), 44 (6), 14 (5), 9 (4), 43 (4), 35 (4), 12 (2), +1 more |
| 79102 | 371 (98..477) | 282 | 52 | 34 (68), 22 (54), 8 (50), 44 (37), 24 (26), 43 (20), 9 (7), 7 (6), 14 (4), 23 (4), 15 (3), 31 (2), +1 more |
| 79103 | 380 (99..481) | 314 | 45 | 22 (58), 8 (51), 17 (41), 24 (40), 23 (40), 44 (28), 34 (17), 31 (15), 25 (7), 14 (6), 12 (5), 15 (3), +2 more |
| 79105 | 379 (101..484) | 324 | 35 | 31 (77), 17 (70), 24 (67), 44 (31), 23 (28), 22 (25), 34 (9), 9 (6), 25 (4), 8 (4), 12 (1), 15 (1), +1 more |
| 79108 | 385 (104..492) | 322 | 40 | 31 (70), 22 (46), 9 (42), 25 (36), 23 (35), 24 (31), 17 (29), 34 (12), 41 (9), 14 (6), 7 (5), 12 (1) |
| 79110 | 388 (106..497) | 324 | 42 | 34 (60), 25 (59), 17 (51), 31 (34), 41 (26), 24 (23), 27 (21), 43 (13), 14 (12), 23 (8), 22 (7), 9 (6), +1 more |
| 79111 | 386 (109..500) | 323 | 48 | 31 (90), 24 (37), 17 (30), 41 (28), 43 (27), 25 (24), 27 (22), 14 (20), 23 (15), 34 (13), 7 (11), 22 (4), +1 more |
| 79115 | 421 (111..531) | 348 | 44 | 25 (89), 14 (85), 7 (70), 17 (53), 41 (21), 43 (12), 23 (11), 22 (2), 27 (2), 34 (2), 9 (1) |
| 79116 | 411 (114..530) | 340 | 53 | 41 (89), 37 (69), 7 (46), 17 (40), 14 (31), 43 (22), 23 (15), 27 (10), 25 (7), 34 (5), 22 (3), 9 (3) |
| 79122 | 404 (118..532) | 347 | 42 | 41 (99), 14 (91), 17 (36), 37 (34), 23 (27), 43 (24), 25 (14), 22 (7), 27 (6), 9 (6), 7 (3) |
| 79132 | 391 (120..515) | 330 | 41 | 24 (56), 27 (51), 41 (50), 14 (47), 7 (44), 37 (27), 9 (16), 25 (12), 23 (10), 22 (8), 17 (6), 43 (3) |
| 79128 | 402 (124..527) | 343 | 41 | 14 (75), 37 (63), 25 (58), 41 (44), 43 (24), 23 (20), 27 (18), 9 (17), 7 (16), 22 (4), 17 (4) |
| 79134 | 407 (127..533) | 346 | 39 | 43 (146), 7 (73), 27 (60), 25 (29), 37 (13), 9 (12), 23 (5), 22 (4), 41 (3), 14 (1) |
| 79135 | 409 (129..542) | 361 | 40 | 27 (134), 23 (102), 7 (61), 9 (22), 43 (18), 22 (14), 25 (7), 37 (3) |
| 79139 | 406 (132..537) | 358 | 25 | 9 (146), 23 (94), 45 (69), 25 (18), 7 (16), 27 (7), 41 (3), 37 (3), 22 (1), 43 (1) |
| 79136 | 393 (136..538) | 343 | 27 | 37 (141), 9 (80), 43 (47), 27 (42), 7 (24), 45 (9) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 123/413/1004; tracks with internal gaps: 24; total internal gaps: 445; longest internal gap: 7; tracks ending in coasting: 23 (trailing rows total 656)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 962 | 42 | 25 | 4 | 0 | 78911 |
| 3 | 82..463 | 382 | 382 | 322 | 60 | 20 | 3 | 29 | 78896, 78969, 78971 |
| 7 | 86..560 | 475 | 475 | 408 | 67 | 28 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..506 | 418 | 418 | 362 | 56 | 19 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 89..520 | 432 | 432 | 381 | 51 | 14 | 5 | 23 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 12 | 92..468 | 377 | 377 | 319 | 58 | 21 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 14 | 96..556 | 461 | 461 | 402 | 59 | 21 | 7 | 26 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 15 | 99..472 | 374 | 374 | 321 | 53 | 17 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 105..510 | 406 | 406 | 361 | 45 | 15 | 2 | 26 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 22 | 111..479 | 369 | 369 | 322 | 47 | 15 | 2 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 111..571 | 461 | 461 | 414 | 47 | 15 | 2 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 111..544 | 434 | 434 | 382 | 52 | 20 | 2 | 29 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79132 |
| 25 | 112..525 | 414 | 414 | 364 | 50 | 14 | 5 | 31 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 118..562 | 445 | 445 | 373 | 72 | 28 | 5 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 31 | 124..529 | 406 | 406 | 352 | 54 | 17 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 34 | 124..496 | 373 | 373 | 322 | 51 | 15 | 3 | 31 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 35 | 129..490 | 362 | 362 | 295 | 67 | 23 | 4 | 23 | 78897, 78899, 78969, 78971, 79045, 79097, 79098 |
| 37 | 138..559 | 422 | 422 | 353 | 69 | 25 | 3 | 30 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 138..474 | 337 | 337 | 283 | 54 | 16 | 5 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 39 | 138..458 | 321 | 321 | 280 | 41 | 10 | 2 | 29 | 78896, 78971, 79037, 79045 |
| 41 | 139..561 | 423 | 423 | 373 | 50 | 17 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 43 | 154..566 | 413 | 413 | 366 | 47 | 13 | 3 | 28 | 79097, 79098, 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 44 | 172..513 | 342 | 342 | 270 | 72 | 29 | 4 | 31 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 45 | 445..567 | 123 | 123 | 78 | 45 | 8 | 3 | 30 | 79136, 79139 |
