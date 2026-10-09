# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=6688a351e89d
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise0.0_fp0.5_seed3/tracks.csv sha256=d7573ab9ab038a4a
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise0.0_fp0.5_seed3.csv sha256=6688a351e89d702f
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise0.0_fp0.5_seed3
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
| observations | none | 4 | 0.461 | 0.241 | 0.817 | 0.01 | 0.418 | 647 | 1043.0 |
| observations | none | 6 | 0.460 | 0.243 | 0.818 | 0.02 | 0.419 | 642 | 1042.0 |
| observations | none | 8 | 0.460 | 0.246 | 0.818 | 0.02 | 0.420 | 640 | 1042.0 |
| observations | none | 12 | 0.461 | 0.253 | 0.819 | 0.28 | 0.434 | 590 | 1030.0 |
| observations | ignore | 4 | 0.461 | 0.241 | 0.817 | 0.01 | 0.418 | 647 | 1043.0 |
| observations | ignore | 6 | 0.460 | 0.243 | 0.818 | 0.02 | 0.419 | 642 | 1042.0 |
| observations | ignore | 8 | 0.460 | 0.246 | 0.818 | 0.02 | 0.420 | 640 | 1042.0 |
| observations | ignore | 12 | 0.461 | 0.253 | 0.819 | 0.28 | 0.434 | 590 | 1030.0 |
| updates | none | 4 | 0.423 | 0.233 | 0.647 | 0.05 | 0.387 | 650 | 976.0 |
| updates | none | 6 | 0.436 | 0.240 | 0.707 | 0.23 | 0.403 | 642 | 702.0 |
| updates | none | 8 | 0.444 | 0.246 | 0.774 | 0.46 | 0.415 | 616 | 418.0 |
| updates | none | 12 | 0.453 | 0.257 | 0.782 | 0.72 | 0.432 | 572 | 377.0 |
| updates | ignore | 4 | 0.423 | 0.233 | 0.647 | 0.05 | 0.387 | 650 | 976.0 |
| updates | ignore | 6 | 0.436 | 0.240 | 0.707 | 0.23 | 0.403 | 642 | 702.0 |
| updates | ignore | 8 | 0.444 | 0.246 | 0.774 | 0.46 | 0.415 | 616 | 418.0 |
| updates | ignore | 12 | 0.453 | 0.257 | 0.782 | 0.72 | 0.432 | 572 | 377.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8972; unmatched reference entries: 1170; unmatched candidate entries: 37
- identity switches: 640; fragmentation (coverage interruptions): 991; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 79037: 47 -> 46 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 46 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 46 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 46 -> 47 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79037: 47 -> 49 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 47 -> 50 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 47 -> 49 at (2125, 3030), 2 frames after previous cover
- f94: ref 78899: 46 -> 47 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 49 -> 50 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 47 -> 49 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 46 -> 47 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 50 -> 53 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 49 -> 50 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 50 -> 53 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 53 -> 45 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 47 -> 49 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 46 -> 47 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 49 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 47 -> 49 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 45 -> 60 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 49 -> 57 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 49 -> 57 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 47 -> 49 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 46 -> 47 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 56 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 54 -> 50 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 57 -> 54 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 50 -> 53 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 53 -> 45 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 57 -> 54 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 49 -> 57 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 47 -> 49 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 46 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 56 -> 46 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 53 -> 45 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 53 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 45 -> 48 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 54 -> 50 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 53 -> 50 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 45 -> 53 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 49 -> 54 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 47 -> 49 at (2107.5, 3023.5), 1 frames after previous cover
- f110: ref 78897: 45 -> 53 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 50 -> 45 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 48 -> 66 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 57 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 54 -> 57 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79108: 46 -> 47 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 56 -> 46 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 57 -> 54 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 49 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 47 -> 49 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 46 -> 47 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 56 -> 46 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 66 -> 40 at (1977.5, 3034.5), 2 frames after previous cover
- f112: ref 79037: 53 -> 48 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 48 -> 66 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 54 -> 67 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 54 -> 68 at (2072.5, 3029.5), 2 frames after previous cover
- ... 580 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 914 | 82 | 0 (914) |
| 78896 | 350 (76..429) | 326 | 21 | 40 (263), 53 (63) |
| 78969 | 352 (80..434) | 307 | 31 | 60 (97), 68 (87), 136 (69), 53 (40), 45 (13), 40 (1) |
| 78971 | 352 (84..439) | 314 | 27 | 68 (185), 136 (80), 53 (27), 48 (19), 66 (1), 40 (1), 60 (1) |
| 79045 | 355 (84..443) | 311 | 37 | 84 (112), 53 (85), 48 (82), 66 (11), 68 (9), 45 (8), 46 (1), 47 (1), 50 (1), 60 (1) |
| 79037 | 355 (86..445) | 316 | 36 | 48 (130), 40 (78), 53 (76), 84 (9), 87 (5), 68 (4), 47 (3), 49 (3), 50 (3), 46 (2), 66 (2), 45 (1) |
| 78897 | 345 (89..450) | 303 | 39 | 84 (122), 45 (71), 88 (46), 87 (16), 48 (14), 68 (10), 53 (8), 50 (7), 40 (4), 47 (2), 49 (2), 46 (1) |
| 78899 | 365 (91..455) | 321 | 37 | 45 (222), 48 (73), 54 (6), 50 (4), 66 (4), 46 (3), 84 (3), 47 (2), 49 (2), 53 (2) |
| 79097 | 366 (94..461) | 312 | 46 | 88 (159), 87 (85), 57 (34), 50 (15), 45 (10), 49 (3), 46 (2), 47 (2), 54 (1), 66 (1) |
| 79098 | 360 (97..467) | 311 | 42 | 87 (127), 47 (45), 66 (44), 57 (39), 88 (30), 50 (10), 45 (7), 49 (3), 54 (3), 46 (1), 67 (1), 68 (1) |
| 79102 | 371 (98..477) | 324 | 38 | 57 (211), 50 (56), 87 (18), 88 (17), 49 (5), 68 (5), 47 (4), 46 (3), 54 (2), 76 (2), 67 (1) |
| 79103 | 380 (99..481) | 325 | 45 | 50 (70), 112 (59), 57 (46), 49 (26), 87 (26), 71 (25), 96 (25), 47 (16), 54 (15), 66 (6), 82 (6), 76 (3), +1 more |
| 79105 | 379 (101..484) | 333 | 39 | 49 (94), 96 (65), 50 (41), 47 (30), 54 (28), 76 (27), 112 (19), 71 (14), 82 (6), 57 (3), 56 (2), 46 (2), +1 more |
| 79108 | 385 (104..492) | 336 | 39 | 82 (112), 50 (55), 112 (41), 88 (30), 49 (26), 54 (22), 71 (19), 96 (9), 47 (5), 76 (5), 67 (4), 46 (3), +3 more |
| 79110 | 388 (106..497) | 336 | 42 | 71 (63), 82 (58), 85 (46), 96 (44), 76 (41), 50 (28), 54 (18), 112 (13), 49 (8), 47 (6), 56 (3), 67 (3), +3 more |
| 79111 | 386 (109..500) | 336 | 41 | 201 (55), 112 (48), 174 (47), 82 (45), 77 (33), 54 (26), 49 (18), 85 (12), 96 (12), 76 (11), 47 (8), 67 (7), +4 more |
| 79115 | 421 (111..531) | 378 | 40 | 50 (94), 54 (73), 71 (49), 49 (30), 77 (29), 82 (28), 47 (21), 112 (18), 76 (12), 85 (9), 96 (5), 56 (3), +3 more |
| 79116 | 411 (114..530) | 363 | 45 | 174 (80), 77 (74), 49 (62), 76 (54), 67 (19), 54 (19), 47 (15), 82 (14), 112 (13), 46 (6), 71 (3), 56 (2), +2 more |
| 79122 | 404 (118..532) | 356 | 39 | 77 (136), 82 (55), 67 (33), 112 (28), 47 (22), 96 (19), 85 (18), 174 (18), 49 (8), 71 (6), 76 (6), 46 (4), +1 more |
| 79132 | 391 (120..515) | 341 | 42 | 49 (82), 77 (82), 71 (59), 67 (31), 54 (28), 96 (25), 85 (15), 112 (8), 47 (5), 56 (4), 46 (2) |
| 79128 | 402 (124..527) | 350 | 42 | 54 (151), 96 (80), 71 (41), 46 (27), 85 (20), 47 (17), 49 (12), 56 (2) |
| 79134 | 407 (127..533) | 365 | 41 | 46 (154), 47 (102), 67 (44), 83 (23), 76 (21), 71 (15), 56 (3), 54 (2), 85 (1) |
| 79135 | 409 (129..542) | 373 | 33 | 67 (173), 76 (103), 46 (65), 47 (29), 56 (2), 71 (1) |
| 79139 | 406 (132..537) | 361 | 40 | 46 (118), 76 (75), 56 (60), 67 (43), 85 (28), 71 (23), 77 (14) |
| 79136 | 393 (136..538) | 360 | 27 | 85 (188), 56 (127), 71 (23), 67 (21), 77 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 35/364/1005; tracks with internal gaps: 13; total internal gaps: 19; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 17)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 918 | 914 | 4 | 4 | 1 | 0 | 78911 |
| 40 | 78..445 | 368 | 347 | 347 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037 |
| 45 | 84..454 | 371 | 333 | 332 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 46 | 86..533 | 448 | 405 | 403 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 86..467 | 382 | 335 | 335 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 48 | 88..443 | 356 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 49 | 91..527 | 437 | 384 | 384 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 50 | 93..531 | 439 | 390 | 388 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 53 | 97..428 | 332 | 302 | 301 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 54 | 99..530 | 432 | 394 | 394 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134 |
| 56 | 101..361 | 261 | 216 | 214 | 2 | 0 | 0 | 2 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 103..477 | 375 | 334 | 333 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 60 | 103..262 | 160 | 102 | 99 | 3 | 0 | 0 | 3 | 78969, 78971, 79045 |
| 66 | 110..195 | 86 | 71 | 69 | 2 | 0 | 0 | 2 | 78899, 78971, 79037, 79045, 79097, 79098, 79103 |
| 67 | 112..537 | 426 | 386 | 385 | 1 | 1 | 1 | 0 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 68 | 112..439 | 328 | 301 | 301 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045, 79098, 79102 |
| 71 | 116..495 | 380 | 349 | 347 | 2 | 2 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 123..568 | 446 | 364 | 360 | 4 | 1 | 2 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 77 | 123..538 | 416 | 375 | 374 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136, 79139 |
| 82 | 129..492 | 364 | 324 | 324 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 83 | 133..167 | 35 | 25 | 23 | 2 | 0 | 0 | 2 | 79134 |
| 84 | 134..410 | 277 | 247 | 246 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79045 |
| 85 | 138..535 | 398 | 343 | 339 | 4 | 1 | 1 | 3 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 87 | 141..461 | 321 | 278 | 277 | 1 | 1 | 1 | 0 | 78897, 79037, 79097, 79098, 79102, 79103 |
| 88 | 141..466 | 326 | 285 | 283 | 2 | 0 | 0 | 2 | 78897, 79097, 79098, 79102, 79108, 79110 |
| 96 | 177..484 | 308 | 286 | 285 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 112 | 205..481 | 277 | 247 | 247 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 136 | 273..434 | 162 | 149 | 149 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 174 | 371..532 | 162 | 146 | 146 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122 |
| 201 | 434..500 | 67 | 55 | 55 | 0 | 0 | 0 | 0 | 79111 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 8972; unmatched reference entries: 1170; unmatched candidate entries: 37
- identity switches: 640; fragmentation (coverage interruptions): 991; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 79037: 47 -> 46 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 46 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 46 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 46 -> 47 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79037: 47 -> 49 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 47 -> 50 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 47 -> 49 at (2125, 3030), 2 frames after previous cover
- f94: ref 78899: 46 -> 47 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 49 -> 50 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 47 -> 49 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 46 -> 47 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 50 -> 53 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 49 -> 50 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 50 -> 53 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 53 -> 45 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 47 -> 49 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 46 -> 47 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 49 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 47 -> 49 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 45 -> 60 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 49 -> 57 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 49 -> 57 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 47 -> 49 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 46 -> 47 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 56 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 54 -> 50 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 57 -> 54 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 50 -> 53 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 53 -> 45 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 57 -> 54 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 49 -> 57 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 47 -> 49 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 46 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 56 -> 46 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 53 -> 45 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 53 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 45 -> 48 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 54 -> 50 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 53 -> 50 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 45 -> 53 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 49 -> 54 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 47 -> 49 at (2107.5, 3023.5), 1 frames after previous cover
- f110: ref 78897: 45 -> 53 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 50 -> 45 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 48 -> 66 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 57 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 54 -> 57 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79108: 46 -> 47 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 56 -> 46 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 57 -> 54 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 49 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 47 -> 49 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 46 -> 47 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 56 -> 46 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 66 -> 40 at (1977.5, 3034.5), 2 frames after previous cover
- f112: ref 79037: 53 -> 48 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 48 -> 66 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 54 -> 67 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 54 -> 68 at (2072.5, 3029.5), 2 frames after previous cover
- ... 580 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 914 | 82 | 0 (914) |
| 78896 | 350 (76..429) | 326 | 21 | 40 (263), 53 (63) |
| 78969 | 352 (80..434) | 307 | 31 | 60 (97), 68 (87), 136 (69), 53 (40), 45 (13), 40 (1) |
| 78971 | 352 (84..439) | 314 | 27 | 68 (185), 136 (80), 53 (27), 48 (19), 66 (1), 40 (1), 60 (1) |
| 79045 | 355 (84..443) | 311 | 37 | 84 (112), 53 (85), 48 (82), 66 (11), 68 (9), 45 (8), 46 (1), 47 (1), 50 (1), 60 (1) |
| 79037 | 355 (86..445) | 316 | 36 | 48 (130), 40 (78), 53 (76), 84 (9), 87 (5), 68 (4), 47 (3), 49 (3), 50 (3), 46 (2), 66 (2), 45 (1) |
| 78897 | 345 (89..450) | 303 | 39 | 84 (122), 45 (71), 88 (46), 87 (16), 48 (14), 68 (10), 53 (8), 50 (7), 40 (4), 47 (2), 49 (2), 46 (1) |
| 78899 | 365 (91..455) | 321 | 37 | 45 (222), 48 (73), 54 (6), 50 (4), 66 (4), 46 (3), 84 (3), 47 (2), 49 (2), 53 (2) |
| 79097 | 366 (94..461) | 312 | 46 | 88 (159), 87 (85), 57 (34), 50 (15), 45 (10), 49 (3), 46 (2), 47 (2), 54 (1), 66 (1) |
| 79098 | 360 (97..467) | 311 | 42 | 87 (127), 47 (45), 66 (44), 57 (39), 88 (30), 50 (10), 45 (7), 49 (3), 54 (3), 46 (1), 67 (1), 68 (1) |
| 79102 | 371 (98..477) | 324 | 38 | 57 (211), 50 (56), 87 (18), 88 (17), 49 (5), 68 (5), 47 (4), 46 (3), 54 (2), 76 (2), 67 (1) |
| 79103 | 380 (99..481) | 325 | 45 | 50 (70), 112 (59), 57 (46), 49 (26), 87 (26), 71 (25), 96 (25), 47 (16), 54 (15), 66 (6), 82 (6), 76 (3), +1 more |
| 79105 | 379 (101..484) | 333 | 39 | 49 (94), 96 (65), 50 (41), 47 (30), 54 (28), 76 (27), 112 (19), 71 (14), 82 (6), 57 (3), 56 (2), 46 (2), +1 more |
| 79108 | 385 (104..492) | 336 | 39 | 82 (112), 50 (55), 112 (41), 88 (30), 49 (26), 54 (22), 71 (19), 96 (9), 47 (5), 76 (5), 67 (4), 46 (3), +3 more |
| 79110 | 388 (106..497) | 336 | 42 | 71 (63), 82 (58), 85 (46), 96 (44), 76 (41), 50 (28), 54 (18), 112 (13), 49 (8), 47 (6), 56 (3), 67 (3), +3 more |
| 79111 | 386 (109..500) | 336 | 41 | 201 (55), 112 (48), 174 (47), 82 (45), 77 (33), 54 (26), 49 (18), 85 (12), 96 (12), 76 (11), 47 (8), 67 (7), +4 more |
| 79115 | 421 (111..531) | 378 | 40 | 50 (94), 54 (73), 71 (49), 49 (30), 77 (29), 82 (28), 47 (21), 112 (18), 76 (12), 85 (9), 96 (5), 56 (3), +3 more |
| 79116 | 411 (114..530) | 363 | 45 | 174 (80), 77 (74), 49 (62), 76 (54), 67 (19), 54 (19), 47 (15), 82 (14), 112 (13), 46 (6), 71 (3), 56 (2), +2 more |
| 79122 | 404 (118..532) | 356 | 39 | 77 (136), 82 (55), 67 (33), 112 (28), 47 (22), 96 (19), 85 (18), 174 (18), 49 (8), 71 (6), 76 (6), 46 (4), +1 more |
| 79132 | 391 (120..515) | 341 | 42 | 49 (82), 77 (82), 71 (59), 67 (31), 54 (28), 96 (25), 85 (15), 112 (8), 47 (5), 56 (4), 46 (2) |
| 79128 | 402 (124..527) | 350 | 42 | 54 (151), 96 (80), 71 (41), 46 (27), 85 (20), 47 (17), 49 (12), 56 (2) |
| 79134 | 407 (127..533) | 365 | 41 | 46 (154), 47 (102), 67 (44), 83 (23), 76 (21), 71 (15), 56 (3), 54 (2), 85 (1) |
| 79135 | 409 (129..542) | 373 | 33 | 67 (173), 76 (103), 46 (65), 47 (29), 56 (2), 71 (1) |
| 79139 | 406 (132..537) | 361 | 40 | 46 (118), 76 (75), 56 (60), 67 (43), 85 (28), 71 (23), 77 (14) |
| 79136 | 393 (136..538) | 360 | 27 | 85 (188), 56 (127), 71 (23), 67 (21), 77 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 35/364/1005; tracks with internal gaps: 13; total internal gaps: 19; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 17)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 918 | 914 | 4 | 4 | 1 | 0 | 78911 |
| 40 | 78..445 | 368 | 347 | 347 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037 |
| 45 | 84..454 | 371 | 333 | 332 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 46 | 86..533 | 448 | 405 | 403 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 86..467 | 382 | 335 | 335 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 48 | 88..443 | 356 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 49 | 91..527 | 437 | 384 | 384 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 50 | 93..531 | 439 | 390 | 388 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 53 | 97..428 | 332 | 302 | 301 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 54 | 99..530 | 432 | 394 | 394 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134 |
| 56 | 101..361 | 261 | 216 | 214 | 2 | 0 | 0 | 2 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 103..477 | 375 | 334 | 333 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 60 | 103..262 | 160 | 102 | 99 | 3 | 0 | 0 | 3 | 78969, 78971, 79045 |
| 66 | 110..195 | 86 | 71 | 69 | 2 | 0 | 0 | 2 | 78899, 78971, 79037, 79045, 79097, 79098, 79103 |
| 67 | 112..537 | 426 | 386 | 385 | 1 | 1 | 1 | 0 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 68 | 112..439 | 328 | 301 | 301 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045, 79098, 79102 |
| 71 | 116..495 | 380 | 349 | 347 | 2 | 2 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 123..568 | 446 | 364 | 360 | 4 | 1 | 2 | 2 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 77 | 123..538 | 416 | 375 | 374 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136, 79139 |
| 82 | 129..492 | 364 | 324 | 324 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 83 | 133..167 | 35 | 25 | 23 | 2 | 0 | 0 | 2 | 79134 |
| 84 | 134..410 | 277 | 247 | 246 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79045 |
| 85 | 138..535 | 398 | 343 | 339 | 4 | 1 | 1 | 3 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 87 | 141..461 | 321 | 278 | 277 | 1 | 1 | 1 | 0 | 78897, 79037, 79097, 79098, 79102, 79103 |
| 88 | 141..466 | 326 | 285 | 283 | 2 | 0 | 0 | 2 | 78897, 79097, 79098, 79102, 79108, 79110 |
| 96 | 177..484 | 308 | 286 | 285 | 1 | 1 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 112 | 205..481 | 277 | 247 | 247 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 136 | 273..434 | 162 | 149 | 149 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 174 | 371..532 | 162 | 146 | 146 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122 |
| 201 | 434..500 | 67 | 55 | 55 | 0 | 0 | 0 | 0 | 79111 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 9727; unmatched reference entries: 415; unmatched candidate entries: 1260
- identity switches: 616; fragmentation (coverage interruptions): 321; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79037: 47 -> 46 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 46 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 46 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 46 -> 47 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 47 -> 49 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 47 -> 50 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 47 -> 49 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 47 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 49 -> 50 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 47 -> 49 at (2128, 3029), 1 frames after previous cover
- f97: ref 79045: 50 -> 53 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 46 -> 47 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 49 -> 50 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 50 -> 53 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 53 -> 45 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 47 -> 49 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 46 -> 47 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 49 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 47 -> 49 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 45 -> 60 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 49 -> 57 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 49 -> 57 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 47 -> 49 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 46 -> 47 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 56 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 54 -> 50 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 57 -> 54 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 50 -> 53 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 53 -> 45 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 57 -> 54 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 49 -> 57 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 47 -> 49 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 46 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 56 -> 46 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 53 -> 45 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 53 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 45 -> 48 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 54 -> 50 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 53 -> 50 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 45 -> 53 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 49 -> 54 at (2097, 3024.5), 1 frames after previous cover
- f110: ref 78897: 45 -> 53 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 50 -> 45 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 48 -> 66 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 57 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 54 -> 57 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 47 -> 49 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 46 -> 47 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 56 -> 46 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 57 -> 54 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 49 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 47 -> 49 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 46 -> 47 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 56 -> 46 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 66 -> 40 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 53 -> 48 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 48 -> 66 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 67 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 54 -> 68 at (2072.5, 3029.5), 2 frames after previous cover
- ... 556 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 999 | 7 | 0 (999) |
| 78896 | 350 (76..429) | 345 | 3 | 40 (277), 53 (68) |
| 78969 | 352 (80..434) | 331 | 11 | 60 (104), 68 (94), 136 (73), 53 (45), 45 (14), 40 (1) |
| 78971 | 352 (84..439) | 335 | 9 | 68 (199), 136 (85), 53 (28), 48 (19), 66 (2), 40 (1), 60 (1) |
| 79045 | 355 (84..443) | 338 | 11 | 84 (123), 53 (91), 48 (90), 66 (12), 68 (9), 45 (8), 50 (2), 46 (1), 47 (1), 60 (1) |
| 79037 | 355 (86..445) | 335 | 17 | 48 (138), 53 (84), 40 (81), 84 (9), 87 (5), 47 (4), 68 (4), 49 (3), 50 (3), 66 (2), 46 (1), 45 (1) |
| 78897 | 345 (89..450) | 331 | 13 | 84 (135), 45 (78), 88 (49), 87 (18), 48 (15), 68 (10), 53 (8), 50 (7), 40 (4), 47 (3), 46 (2), 49 (2) |
| 78899 | 365 (91..455) | 352 | 11 | 45 (243), 48 (83), 54 (6), 50 (4), 66 (4), 46 (3), 84 (3), 47 (2), 49 (2), 53 (2) |
| 79097 | 366 (94..461) | 342 | 19 | 88 (173), 87 (95), 57 (38), 50 (16), 45 (11), 46 (3), 49 (3), 47 (1), 54 (1), 66 (1) |
| 79098 | 360 (97..467) | 342 | 14 | 87 (137), 47 (54), 66 (51), 57 (42), 88 (31), 50 (10), 45 (8), 49 (3), 54 (3), 46 (1), 67 (1), 68 (1) |
| 79102 | 371 (98..477) | 347 | 18 | 57 (230), 50 (60), 87 (18), 88 (17), 49 (5), 68 (5), 47 (4), 46 (3), 54 (2), 76 (2), 67 (1) |
| 79103 | 380 (99..481) | 354 | 19 | 50 (81), 112 (60), 57 (54), 49 (29), 87 (29), 96 (26), 71 (25), 47 (17), 54 (15), 66 (6), 82 (6), 46 (3), +1 more |
| 79105 | 379 (101..484) | 359 | 16 | 49 (102), 96 (69), 50 (43), 47 (35), 54 (31), 76 (29), 112 (21), 71 (14), 82 (6), 57 (3), 56 (2), 46 (2), +1 more |
| 79108 | 385 (104..492) | 361 | 18 | 82 (121), 50 (59), 112 (44), 88 (32), 49 (29), 54 (24), 71 (20), 96 (9), 47 (5), 76 (5), 46 (4), 67 (4), +3 more |
| 79110 | 388 (106..497) | 367 | 18 | 71 (70), 82 (66), 76 (47), 85 (47), 96 (46), 50 (30), 54 (20), 112 (14), 49 (8), 47 (7), 67 (4), 56 (3), +3 more |
| 79111 | 386 (109..500) | 366 | 13 | 201 (66), 112 (52), 174 (52), 82 (48), 77 (35), 54 (27), 49 (17), 85 (15), 96 (13), 47 (10), 76 (10), 67 (8), +4 more |
| 79115 | 421 (111..531) | 408 | 10 | 50 (101), 54 (77), 71 (54), 77 (32), 49 (31), 82 (30), 47 (24), 112 (20), 76 (14), 85 (10), 96 (5), 56 (3), +3 more |
| 79116 | 411 (114..530) | 396 | 14 | 174 (89), 77 (75), 49 (70), 76 (60), 67 (22), 54 (20), 82 (16), 47 (15), 112 (14), 46 (6), 56 (4), 71 (3), +2 more |
| 79122 | 404 (118..532) | 389 | 14 | 77 (149), 82 (63), 67 (34), 112 (30), 47 (24), 85 (21), 96 (20), 174 (20), 49 (9), 71 (6), 76 (6), 46 (4), +1 more |
| 79132 | 391 (120..515) | 367 | 20 | 49 (91), 77 (89), 71 (59), 67 (35), 54 (32), 96 (26), 85 (16), 112 (8), 47 (5), 56 (4), 46 (2) |
| 79128 | 402 (124..527) | 380 | 18 | 54 (167), 96 (85), 71 (43), 46 (27), 85 (23), 47 (20), 49 (13), 56 (2) |
| 79134 | 407 (127..533) | 399 | 8 | 46 (169), 47 (114), 67 (48), 83 (24), 76 (22), 71 (17), 56 (3), 54 (2) |
| 79135 | 409 (129..542) | 401 | 6 | 67 (183), 76 (111), 46 (72), 47 (32), 56 (2), 71 (1) |
| 79139 | 406 (132..537) | 398 | 8 | 46 (129), 76 (82), 67 (69), 56 (65), 85 (29), 71 (24) |
| 79136 | 393 (136..538) | 385 | 6 | 85 (203), 56 (138), 71 (25), 77 (19) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 64/393/1006; tracks with internal gaps: 27; total internal gaps: 208; longest internal gap: 20; tracks ending in coasting: 29 (trailing rows total 983)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 999 | 7 | 7 | 1 | 0 | 78911 |
| 40 | 78..474 | 397 | 397 | 364 | 33 | 2 | 3 | 29 | 78896, 78897, 78969, 78971, 79037 |
| 45 | 84..483 | 400 | 400 | 363 | 37 | 9 | 1 | 28 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 46 | 86..562 | 477 | 477 | 439 | 38 | 7 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 86..496 | 411 | 411 | 377 | 34 | 5 | 1 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 48 | 88..472 | 385 | 385 | 345 | 40 | 8 | 3 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 49 | 91..556 | 466 | 466 | 417 | 49 | 15 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 50 | 93..560 | 468 | 468 | 420 | 48 | 8 | 10 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 53 | 97..457 | 361 | 361 | 326 | 35 | 6 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 54 | 99..559 | 461 | 461 | 427 | 34 | 5 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134 |
| 56 | 101..390 | 290 | 290 | 232 | 58 | 11 | 2 | 46 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 103..506 | 404 | 404 | 367 | 37 | 12 | 1 | 25 | 79097, 79098, 79102, 79103, 79105 |
| 60 | 103..291 | 189 | 189 | 106 | 83 | 3 | 2 | 79 | 78969, 78971, 79045 |
| 66 | 110..224 | 115 | 115 | 78 | 37 | 0 | 0 | 37 | 78899, 78971, 79037, 79045, 79097, 79098, 79103 |
| 67 | 112..566 | 455 | 455 | 414 | 41 | 10 | 3 | 29 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 68 | 112..468 | 357 | 357 | 322 | 35 | 5 | 2 | 29 | 78897, 78969, 78971, 79037, 79045, 79098, 79102 |
| 71 | 116..524 | 409 | 409 | 366 | 43 | 11 | 4 | 27 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 123..597 | 475 | 475 | 391 | 84 | 9 | 20 | 55 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 77 | 123..567 | 445 | 445 | 404 | 41 | 11 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 82 | 129..521 | 393 | 393 | 356 | 37 | 6 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 83 | 133..196 | 64 | 64 | 24 | 40 | 0 | 0 | 40 | 79134 |
| 84 | 134..439 | 306 | 306 | 270 | 36 | 6 | 1 | 30 | 78897, 78899, 79037, 79045 |
| 85 | 138..564 | 427 | 427 | 366 | 61 | 7 | 8 | 47 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136, 79139 |
| 87 | 141..490 | 350 | 350 | 302 | 48 | 16 | 3 | 29 | 78897, 79037, 79097, 79098, 79102, 79103 |
| 88 | 141..495 | 355 | 355 | 303 | 52 | 7 | 1 | 45 | 78897, 79097, 79098, 79102, 79108, 79110 |
| 96 | 177..513 | 337 | 337 | 300 | 37 | 8 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 112 | 205..510 | 306 | 306 | 263 | 43 | 10 | 2 | 32 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 136 | 273..463 | 191 | 191 | 158 | 33 | 3 | 2 | 29 | 78969, 78971 |
| 174 | 371..561 | 191 | 191 | 162 | 29 | 0 | 0 | 29 | 79111, 79115, 79116, 79122 |
| 201 | 434..529 | 96 | 96 | 66 | 30 | 1 | 1 | 29 | 79111 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 30; matched pairs: 9727; unmatched reference entries: 415; unmatched candidate entries: 1260
- identity switches: 616; fragmentation (coverage interruptions): 321; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79037: 47 -> 46 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 46 -> 47 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 46 -> 47 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 46 -> 47 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 47 -> 49 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 47 -> 50 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 47 -> 49 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 47 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 49 -> 50 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 47 -> 49 at (2128, 3029), 1 frames after previous cover
- f97: ref 79045: 50 -> 53 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 46 -> 47 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 49 -> 50 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 50 -> 53 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 53 -> 45 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 47 -> 49 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 46 -> 47 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 49 -> 54 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 47 -> 49 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 45 -> 60 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 49 -> 57 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 49 -> 57 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 47 -> 49 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 46 -> 47 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 56 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 54 -> 50 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 57 -> 54 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 50 -> 53 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 53 -> 45 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 57 -> 54 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 49 -> 57 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 47 -> 49 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 46 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 56 -> 46 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 53 -> 45 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 50 -> 53 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 45 -> 48 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 54 -> 50 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 53 -> 50 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 45 -> 53 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 49 -> 54 at (2097, 3024.5), 1 frames after previous cover
- f110: ref 78897: 45 -> 53 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 50 -> 45 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 48 -> 66 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 57 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 54 -> 57 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 47 -> 49 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 46 -> 47 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 56 -> 46 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 57 -> 54 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 49 -> 57 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 47 -> 49 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 46 -> 47 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 56 -> 46 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 66 -> 40 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 53 -> 48 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 48 -> 66 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79098: 54 -> 67 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 54 -> 68 at (2072.5, 3029.5), 2 frames after previous cover
- ... 556 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 999 | 7 | 0 (999) |
| 78896 | 350 (76..429) | 345 | 3 | 40 (277), 53 (68) |
| 78969 | 352 (80..434) | 331 | 11 | 60 (104), 68 (94), 136 (73), 53 (45), 45 (14), 40 (1) |
| 78971 | 352 (84..439) | 335 | 9 | 68 (199), 136 (85), 53 (28), 48 (19), 66 (2), 40 (1), 60 (1) |
| 79045 | 355 (84..443) | 338 | 11 | 84 (123), 53 (91), 48 (90), 66 (12), 68 (9), 45 (8), 50 (2), 46 (1), 47 (1), 60 (1) |
| 79037 | 355 (86..445) | 335 | 17 | 48 (138), 53 (84), 40 (81), 84 (9), 87 (5), 47 (4), 68 (4), 49 (3), 50 (3), 66 (2), 46 (1), 45 (1) |
| 78897 | 345 (89..450) | 331 | 13 | 84 (135), 45 (78), 88 (49), 87 (18), 48 (15), 68 (10), 53 (8), 50 (7), 40 (4), 47 (3), 46 (2), 49 (2) |
| 78899 | 365 (91..455) | 352 | 11 | 45 (243), 48 (83), 54 (6), 50 (4), 66 (4), 46 (3), 84 (3), 47 (2), 49 (2), 53 (2) |
| 79097 | 366 (94..461) | 342 | 19 | 88 (173), 87 (95), 57 (38), 50 (16), 45 (11), 46 (3), 49 (3), 47 (1), 54 (1), 66 (1) |
| 79098 | 360 (97..467) | 342 | 14 | 87 (137), 47 (54), 66 (51), 57 (42), 88 (31), 50 (10), 45 (8), 49 (3), 54 (3), 46 (1), 67 (1), 68 (1) |
| 79102 | 371 (98..477) | 347 | 18 | 57 (230), 50 (60), 87 (18), 88 (17), 49 (5), 68 (5), 47 (4), 46 (3), 54 (2), 76 (2), 67 (1) |
| 79103 | 380 (99..481) | 354 | 19 | 50 (81), 112 (60), 57 (54), 49 (29), 87 (29), 96 (26), 71 (25), 47 (17), 54 (15), 66 (6), 82 (6), 46 (3), +1 more |
| 79105 | 379 (101..484) | 359 | 16 | 49 (102), 96 (69), 50 (43), 47 (35), 54 (31), 76 (29), 112 (21), 71 (14), 82 (6), 57 (3), 56 (2), 46 (2), +1 more |
| 79108 | 385 (104..492) | 361 | 18 | 82 (121), 50 (59), 112 (44), 88 (32), 49 (29), 54 (24), 71 (20), 96 (9), 47 (5), 76 (5), 46 (4), 67 (4), +3 more |
| 79110 | 388 (106..497) | 367 | 18 | 71 (70), 82 (66), 76 (47), 85 (47), 96 (46), 50 (30), 54 (20), 112 (14), 49 (8), 47 (7), 67 (4), 56 (3), +3 more |
| 79111 | 386 (109..500) | 366 | 13 | 201 (66), 112 (52), 174 (52), 82 (48), 77 (35), 54 (27), 49 (17), 85 (15), 96 (13), 47 (10), 76 (10), 67 (8), +4 more |
| 79115 | 421 (111..531) | 408 | 10 | 50 (101), 54 (77), 71 (54), 77 (32), 49 (31), 82 (30), 47 (24), 112 (20), 76 (14), 85 (10), 96 (5), 56 (3), +3 more |
| 79116 | 411 (114..530) | 396 | 14 | 174 (89), 77 (75), 49 (70), 76 (60), 67 (22), 54 (20), 82 (16), 47 (15), 112 (14), 46 (6), 56 (4), 71 (3), +2 more |
| 79122 | 404 (118..532) | 389 | 14 | 77 (149), 82 (63), 67 (34), 112 (30), 47 (24), 85 (21), 96 (20), 174 (20), 49 (9), 71 (6), 76 (6), 46 (4), +1 more |
| 79132 | 391 (120..515) | 367 | 20 | 49 (91), 77 (89), 71 (59), 67 (35), 54 (32), 96 (26), 85 (16), 112 (8), 47 (5), 56 (4), 46 (2) |
| 79128 | 402 (124..527) | 380 | 18 | 54 (167), 96 (85), 71 (43), 46 (27), 85 (23), 47 (20), 49 (13), 56 (2) |
| 79134 | 407 (127..533) | 399 | 8 | 46 (169), 47 (114), 67 (48), 83 (24), 76 (22), 71 (17), 56 (3), 54 (2) |
| 79135 | 409 (129..542) | 401 | 6 | 67 (183), 76 (111), 46 (72), 47 (32), 56 (2), 71 (1) |
| 79139 | 406 (132..537) | 398 | 8 | 46 (129), 76 (82), 67 (69), 56 (65), 85 (29), 71 (24) |
| 79136 | 393 (136..538) | 385 | 6 | 85 (203), 56 (138), 71 (25), 77 (19) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 30; lifespan min/median/max: 64/393/1006; tracks with internal gaps: 27; total internal gaps: 208; longest internal gap: 20; tracks ending in coasting: 29 (trailing rows total 983)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 999 | 7 | 7 | 1 | 0 | 78911 |
| 40 | 78..474 | 397 | 397 | 364 | 33 | 2 | 3 | 29 | 78896, 78897, 78969, 78971, 79037 |
| 45 | 84..483 | 400 | 400 | 363 | 37 | 9 | 1 | 28 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 46 | 86..562 | 477 | 477 | 439 | 38 | 7 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 86..496 | 411 | 411 | 377 | 34 | 5 | 1 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 48 | 88..472 | 385 | 385 | 345 | 40 | 8 | 3 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 49 | 91..556 | 466 | 466 | 417 | 49 | 15 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 50 | 93..560 | 468 | 468 | 420 | 48 | 8 | 10 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 53 | 97..457 | 361 | 361 | 326 | 35 | 6 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 54 | 99..559 | 461 | 461 | 427 | 34 | 5 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134 |
| 56 | 101..390 | 290 | 290 | 232 | 58 | 11 | 2 | 46 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 103..506 | 404 | 404 | 367 | 37 | 12 | 1 | 25 | 79097, 79098, 79102, 79103, 79105 |
| 60 | 103..291 | 189 | 189 | 106 | 83 | 3 | 2 | 79 | 78969, 78971, 79045 |
| 66 | 110..224 | 115 | 115 | 78 | 37 | 0 | 0 | 37 | 78899, 78971, 79037, 79045, 79097, 79098, 79103 |
| 67 | 112..566 | 455 | 455 | 414 | 41 | 10 | 3 | 29 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 68 | 112..468 | 357 | 357 | 322 | 35 | 5 | 2 | 29 | 78897, 78969, 78971, 79037, 79045, 79098, 79102 |
| 71 | 116..524 | 409 | 409 | 366 | 43 | 11 | 4 | 27 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 123..597 | 475 | 475 | 391 | 84 | 9 | 20 | 55 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79139 |
| 77 | 123..567 | 445 | 445 | 404 | 41 | 11 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 82 | 129..521 | 393 | 393 | 356 | 37 | 6 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 83 | 133..196 | 64 | 64 | 24 | 40 | 0 | 0 | 40 | 79134 |
| 84 | 134..439 | 306 | 306 | 270 | 36 | 6 | 1 | 30 | 78897, 78899, 79037, 79045 |
| 85 | 138..564 | 427 | 427 | 366 | 61 | 7 | 8 | 47 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136, 79139 |
| 87 | 141..490 | 350 | 350 | 302 | 48 | 16 | 3 | 29 | 78897, 79037, 79097, 79098, 79102, 79103 |
| 88 | 141..495 | 355 | 355 | 303 | 52 | 7 | 1 | 45 | 78897, 79097, 79098, 79102, 79108, 79110 |
| 96 | 177..513 | 337 | 337 | 300 | 37 | 8 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 112 | 205..510 | 306 | 306 | 263 | 43 | 10 | 2 | 32 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 136 | 273..463 | 191 | 191 | 158 | 33 | 3 | 2 | 29 | 78969, 78971 |
| 174 | 371..561 | 191 | 191 | 162 | 29 | 0 | 0 | 29 | 79111, 79115, 79116, 79122 |
| 201 | 434..529 | 96 | 96 | 66 | 30 | 1 | 1 | 29 | 79111 |
