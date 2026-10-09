# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=680aa00ab859
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise1.0_fp0.5_seed1/tracks.csv sha256=c396e9cdca261ebd
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise1.0_fp0.5_seed1.csv sha256=680aa00ab859213e
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise1.0_fp0.5_seed1
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
| observations | none | 4 | 0.676 | 0.559 | 0.984 | 1.27 | 0.804 | 88 | 129.0 |
| observations | none | 6 | 0.729 | 0.606 | 0.986 | 1.27 | 0.807 | 81 | 122.0 |
| observations | none | 8 | 0.757 | 0.634 | 0.985 | 1.28 | 0.810 | 81 | 125.0 |
| observations | none | 12 | 0.787 | 0.679 | 0.986 | 1.30 | 0.820 | 68 | 122.0 |
| observations | ignore | 4 | 0.676 | 0.559 | 0.984 | 1.27 | 0.804 | 88 | 129.0 |
| observations | ignore | 6 | 0.729 | 0.606 | 0.986 | 1.27 | 0.807 | 81 | 122.0 |
| observations | ignore | 8 | 0.757 | 0.634 | 0.985 | 1.28 | 0.810 | 81 | 125.0 |
| observations | ignore | 12 | 0.787 | 0.679 | 0.986 | 1.30 | 0.820 | 68 | 122.0 |
| updates | none | 4 | 0.630 | 0.524 | 0.902 | 1.26 | 0.772 | 83 | 128.0 |
| updates | none | 6 | 0.679 | 0.568 | 0.903 | 1.27 | 0.775 | 81 | 122.0 |
| updates | none | 8 | 0.705 | 0.594 | 0.902 | 1.28 | 0.778 | 79 | 125.0 |
| updates | none | 12 | 0.733 | 0.635 | 0.902 | 1.33 | 0.788 | 68 | 125.0 |
| updates | ignore | 4 | 0.630 | 0.524 | 0.902 | 1.26 | 0.772 | 83 | 128.0 |
| updates | ignore | 6 | 0.679 | 0.568 | 0.903 | 1.27 | 0.775 | 81 | 122.0 |
| updates | ignore | 8 | 0.705 | 0.594 | 0.902 | 1.28 | 0.778 | 79 | 125.0 |
| updates | ignore | 12 | 0.733 | 0.635 | 0.902 | 1.33 | 0.788 | 68 | 125.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 16
- identity switches: 81; fragmentation (coverage interruptions): 15; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 78971: 35 -> 32 at (2121, 3034), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 33 -> 37 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f92: ref 78971: 32 -> 29 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78896: 38 -> 30 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 30 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78897: 33 -> 37 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 37 -> 38 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78897: 37 -> 38 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 79037: 38 -> 37 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78897: 38 -> 35 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78969: 38 -> 42 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79097: 35 -> 38 at (2141, 3029), 1 frames after previous cover
- f97: ref 78897: 35 -> 37 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 33 -> 35 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 38 -> 33 at (2135, 3028), 1 frames after previous cover
- f99: ref 79037: 37 -> 44 at (2080, 3034.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 46 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79098: 38 -> 33 at (2124, 3028), 4 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 38 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 33 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79105: 38 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 79103: 46 -> 33 at (2120.5, 3023), 2 frames after previous cover
- f106: ref 79098: 33 -> 50 at (2096, 3028.5), 3 frames after previous cover
- f106: ref 79102: 47 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 33 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 37 -> 44 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 35 -> 37 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 44 -> 32 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79097: 48 -> 35 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 50 -> 48 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79105: 46 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 46 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 79037: 32 -> 53 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79102: 33 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 33 at (2092.5, 3023.5), 2 frames after previous cover
- f129: ref 79105: 47 -> 50 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 46 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 38 -> 46 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 57 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 57 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 61 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 50 -> 70 at (1952.5, 3031), 4 frames after previous cover
- f220: ref 79097: 35 -> 44 at (1365.5, 2995), 1 frames after previous cover
- f220: ref 79102: 70 -> 35 at (1404, 3001.5), 1 frames after previous cover
- f220: ref 79103: 33 -> 70 at (1415, 3000.5), 1 frames after previous cover
- f220: ref 79108: 47 -> 33 at (1465, 3003), 2 frames after previous cover
- f221: ref 79097: 44 -> 48 at (1358, 2994), 1 frames after previous cover
- f221: ref 79098: 48 -> 35 at (1384, 2999.5), 1 frames after previous cover
- f221: ref 79102: 35 -> 70 at (1398, 3001), 1 frames after previous cover
- f221: ref 79103: 70 -> 50 at (1408, 2999.5), 1 frames after previous cover
- f221: ref 79105: 50 -> 33 at (1428.5, 2999.5), 1 frames after previous cover
- f221: ref 79108: 33 -> 46 at (1460, 3001), 1 frames after previous cover
- f221: ref 79111: 46 -> 56 at (1485.5, 3002), 1 frames after previous cover
- f221: ref 79115: 56 -> 38 at (1495.5, 3003.5), 1 frames after previous cover
- ... 21 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 347 | 1 | 30 (333), 29 (13), 38 (1) |
| 78969 | 352 (80..434) | 348 | 1 | 42 (336), 30 (11), 38 (1) |
| 78971 | 352 (84..439) | 349 | 0 | 29 (344), 32 (3), 35 (2) |
| 79045 | 355 (84..443) | 348 | 2 | 32 (348) |
| 79037 | 355 (86..445) | 353 | 1 | 53 (331), 44 (10), 33 (5), 37 (5), 38 (1), 32 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 44 (325), 37 (13), 35 (3), 33 (3), 38 (1) |
| 78899 | 365 (91..455) | 365 | 0 | 37 (347), 35 (15), 33 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 48 (247), 35 (111), 33 (4), 38 (1), 44 (1) |
| 79098 | 360 (97..467) | 355 | 2 | 35 (236), 48 (112), 33 (3), 50 (3), 38 (1) |
| 79102 | 371 (98..477) | 368 | 2 | 70 (337), 50 (19), 47 (5), 33 (4), 38 (1), 46 (1), 35 (1) |
| 79103 | 380 (99..481) | 378 | 2 | 51 (139), 50 (119), 33 (111), 46 (3), 47 (3), 38 (2), 70 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 50 (233), 33 (119), 47 (20), 46 (5), 38 (2) |
| 79108 | 385 (104..492) | 383 | 1 | 46 (289), 47 (90), 38 (2), 51 (1), 33 (1) |
| 79110 | 388 (106..497) | 388 | 0 | 51 (230), 56 (155), 38 (2), 33 (1) |
| 79111 | 386 (109..500) | 386 | 0 | 33 (157), 56 (117), 46 (92), 38 (20) |
| 79115 | 421 (111..531) | 417 | 2 | 62 (303), 56 (108), 38 (6) |
| 79116 | 411 (114..530) | 409 | 0 | 38 (234), 65 (154), 57 (13), 62 (8) |
| 79122 | 404 (118..532) | 402 | 0 | 47 (303), 57 (90), 61 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 57 (289), 62 (99), 47 (1) |
| 79128 | 402 (124..527) | 400 | 0 | 61 (397), 65 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 65 (251), 38 (154) |
| 79135 | 409 (129..542) | 409 | 0 | 69 (408), 38 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 71 (403), 69 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (390), 71 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 225 | 469..469 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 1/385/1007; tracks with internal gaps: 10; total internal gaps: 12; longest internal gap: 1; tracks ending in coasting: 3 (trailing rows total 4)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 29 | 78..439 | 362 | 358 | 357 | 1 | 1 | 1 | 0 | 78896, 78971 |
| 30 | 82..429 | 348 | 344 | 344 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 32 | 86..443 | 358 | 353 | 352 | 1 | 1 | 1 | 0 | 78971, 79037, 79045 |
| 33 | 86..500 | 415 | 412 | 411 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 35 | 87..469 | 383 | 369 | 368 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79097, 79098, 79102 |
| 37 | 91..455 | 365 | 365 | 365 | 0 | 0 | 0 | 0 | 78897, 78899, 79037 |
| 38 | 92..535 | 444 | 434 | 430 | 4 | 2 | 1 | 2 | 78896, 78897, 78969, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79134, 79135 |
| 42 | 96..434 | 339 | 336 | 336 | 0 | 0 | 0 | 0 | 78969 |
| 44 | 99..450 | 352 | 337 | 336 | 1 | 1 | 1 | 0 | 78897, 79037, 79097 |
| 46 | 100..492 | 393 | 390 | 390 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79111 |
| 47 | 101..532 | 432 | 423 | 422 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79122, 79132 |
| 48 | 103..461 | 359 | 359 | 359 | 0 | 0 | 0 | 0 | 79097, 79098 |
| 50 | 106..484 | 379 | 376 | 374 | 2 | 2 | 1 | 0 | 79098, 79102, 79103, 79105 |
| 51 | 108..481 | 374 | 371 | 370 | 1 | 1 | 1 | 0 | 79103, 79108, 79110 |
| 53 | 110..445 | 336 | 331 | 331 | 0 | 0 | 0 | 0 | 79037 |
| 56 | 113..497 | 385 | 381 | 380 | 1 | 1 | 1 | 0 | 79110, 79111, 79115 |
| 57 | 116..515 | 400 | 392 | 392 | 0 | 0 | 0 | 0 | 79116, 79122, 79132 |
| 61 | 120..527 | 408 | 406 | 406 | 0 | 0 | 0 | 0 | 79122, 79128 |
| 62 | 122..531 | 410 | 410 | 410 | 0 | 0 | 0 | 0 | 79115, 79116, 79132 |
| 65 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79116, 79128, 79134 |
| 69 | 129..542 | 414 | 409 | 409 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 70 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102, 79103 |
| 71 | 134..537 | 404 | 404 | 404 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 73 | 138..538 | 401 | 391 | 390 | 1 | 1 | 1 | 0 | 79136 |
| 225 | 469..469 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 16
- identity switches: 81; fragmentation (coverage interruptions): 15; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 78971: 35 -> 32 at (2121, 3034), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 33 -> 37 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f92: ref 78971: 32 -> 29 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78896: 38 -> 30 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 30 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78897: 33 -> 37 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 37 -> 38 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78897: 37 -> 38 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 79037: 38 -> 37 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78897: 38 -> 35 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78969: 38 -> 42 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79097: 35 -> 38 at (2141, 3029), 1 frames after previous cover
- f97: ref 78897: 35 -> 37 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 33 -> 35 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 38 -> 33 at (2135, 3028), 1 frames after previous cover
- f99: ref 79037: 37 -> 44 at (2080, 3034.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 46 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79098: 38 -> 33 at (2124, 3028), 4 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 38 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 33 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79105: 38 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 79103: 46 -> 33 at (2120.5, 3023), 2 frames after previous cover
- f106: ref 79098: 33 -> 50 at (2096, 3028.5), 3 frames after previous cover
- f106: ref 79102: 47 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 33 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 37 -> 44 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 35 -> 37 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 44 -> 32 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79097: 48 -> 35 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 50 -> 48 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79105: 46 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 46 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 79037: 32 -> 53 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79102: 33 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 33 at (2092.5, 3023.5), 2 frames after previous cover
- f129: ref 79105: 47 -> 50 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 46 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 38 -> 46 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 57 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 57 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 61 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 50 -> 70 at (1952.5, 3031), 4 frames after previous cover
- f220: ref 79097: 35 -> 44 at (1365.5, 2995), 1 frames after previous cover
- f220: ref 79102: 70 -> 35 at (1404, 3001.5), 1 frames after previous cover
- f220: ref 79103: 33 -> 70 at (1415, 3000.5), 1 frames after previous cover
- f220: ref 79108: 47 -> 33 at (1465, 3003), 2 frames after previous cover
- f221: ref 79097: 44 -> 48 at (1358, 2994), 1 frames after previous cover
- f221: ref 79098: 48 -> 35 at (1384, 2999.5), 1 frames after previous cover
- f221: ref 79102: 35 -> 70 at (1398, 3001), 1 frames after previous cover
- f221: ref 79103: 70 -> 50 at (1408, 2999.5), 1 frames after previous cover
- f221: ref 79105: 50 -> 33 at (1428.5, 2999.5), 1 frames after previous cover
- f221: ref 79108: 33 -> 46 at (1460, 3001), 1 frames after previous cover
- f221: ref 79111: 46 -> 56 at (1485.5, 3002), 1 frames after previous cover
- f221: ref 79115: 56 -> 38 at (1495.5, 3003.5), 1 frames after previous cover
- ... 21 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 347 | 1 | 30 (333), 29 (13), 38 (1) |
| 78969 | 352 (80..434) | 348 | 1 | 42 (336), 30 (11), 38 (1) |
| 78971 | 352 (84..439) | 349 | 0 | 29 (344), 32 (3), 35 (2) |
| 79045 | 355 (84..443) | 348 | 2 | 32 (348) |
| 79037 | 355 (86..445) | 353 | 1 | 53 (331), 44 (10), 33 (5), 37 (5), 38 (1), 32 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 44 (325), 37 (13), 35 (3), 33 (3), 38 (1) |
| 78899 | 365 (91..455) | 365 | 0 | 37 (347), 35 (15), 33 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 48 (247), 35 (111), 33 (4), 38 (1), 44 (1) |
| 79098 | 360 (97..467) | 355 | 2 | 35 (236), 48 (112), 33 (3), 50 (3), 38 (1) |
| 79102 | 371 (98..477) | 368 | 2 | 70 (337), 50 (19), 47 (5), 33 (4), 38 (1), 46 (1), 35 (1) |
| 79103 | 380 (99..481) | 378 | 2 | 51 (139), 50 (119), 33 (111), 46 (3), 47 (3), 38 (2), 70 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 50 (233), 33 (119), 47 (20), 46 (5), 38 (2) |
| 79108 | 385 (104..492) | 383 | 1 | 46 (289), 47 (90), 38 (2), 51 (1), 33 (1) |
| 79110 | 388 (106..497) | 388 | 0 | 51 (230), 56 (155), 38 (2), 33 (1) |
| 79111 | 386 (109..500) | 386 | 0 | 33 (157), 56 (117), 46 (92), 38 (20) |
| 79115 | 421 (111..531) | 417 | 2 | 62 (303), 56 (108), 38 (6) |
| 79116 | 411 (114..530) | 409 | 0 | 38 (234), 65 (154), 57 (13), 62 (8) |
| 79122 | 404 (118..532) | 402 | 0 | 47 (303), 57 (90), 61 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 57 (289), 62 (99), 47 (1) |
| 79128 | 402 (124..527) | 400 | 0 | 61 (397), 65 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 65 (251), 38 (154) |
| 79135 | 409 (129..542) | 409 | 0 | 69 (408), 38 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 71 (403), 69 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (390), 71 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 225 | 469..469 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 1/385/1007; tracks with internal gaps: 10; total internal gaps: 12; longest internal gap: 1; tracks ending in coasting: 3 (trailing rows total 4)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 29 | 78..439 | 362 | 358 | 357 | 1 | 1 | 1 | 0 | 78896, 78971 |
| 30 | 82..429 | 348 | 344 | 344 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 32 | 86..443 | 358 | 353 | 352 | 1 | 1 | 1 | 0 | 78971, 79037, 79045 |
| 33 | 86..500 | 415 | 412 | 411 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 35 | 87..469 | 383 | 369 | 368 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79097, 79098, 79102 |
| 37 | 91..455 | 365 | 365 | 365 | 0 | 0 | 0 | 0 | 78897, 78899, 79037 |
| 38 | 92..535 | 444 | 434 | 430 | 4 | 2 | 1 | 2 | 78896, 78897, 78969, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79134, 79135 |
| 42 | 96..434 | 339 | 336 | 336 | 0 | 0 | 0 | 0 | 78969 |
| 44 | 99..450 | 352 | 337 | 336 | 1 | 1 | 1 | 0 | 78897, 79037, 79097 |
| 46 | 100..492 | 393 | 390 | 390 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108, 79111 |
| 47 | 101..532 | 432 | 423 | 422 | 1 | 1 | 1 | 0 | 79102, 79103, 79105, 79108, 79122, 79132 |
| 48 | 103..461 | 359 | 359 | 359 | 0 | 0 | 0 | 0 | 79097, 79098 |
| 50 | 106..484 | 379 | 376 | 374 | 2 | 2 | 1 | 0 | 79098, 79102, 79103, 79105 |
| 51 | 108..481 | 374 | 371 | 370 | 1 | 1 | 1 | 0 | 79103, 79108, 79110 |
| 53 | 110..445 | 336 | 331 | 331 | 0 | 0 | 0 | 0 | 79037 |
| 56 | 113..497 | 385 | 381 | 380 | 1 | 1 | 1 | 0 | 79110, 79111, 79115 |
| 57 | 116..515 | 400 | 392 | 392 | 0 | 0 | 0 | 0 | 79116, 79122, 79132 |
| 61 | 120..527 | 408 | 406 | 406 | 0 | 0 | 0 | 0 | 79122, 79128 |
| 62 | 122..531 | 410 | 410 | 410 | 0 | 0 | 0 | 0 | 79115, 79116, 79132 |
| 65 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79116, 79128, 79134 |
| 69 | 129..542 | 414 | 409 | 409 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 70 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102, 79103 |
| 71 | 134..537 | 404 | 404 | 404 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 73 | 138..538 | 401 | 391 | 390 | 1 | 1 | 1 | 0 | 79136 |
| 225 | 469..469 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 859
- identity switches: 79; fragmentation (coverage interruptions): 15; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 78971: 35 -> 32 at (2121, 3034), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 33 -> 37 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f92: ref 78971: 32 -> 29 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78896: 38 -> 30 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 30 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78897: 33 -> 37 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 37 -> 38 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78897: 37 -> 38 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 79037: 38 -> 37 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78897: 38 -> 35 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78969: 38 -> 42 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79097: 35 -> 38 at (2141, 3029), 1 frames after previous cover
- f97: ref 78897: 35 -> 37 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 33 -> 35 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 38 -> 33 at (2135, 3028), 1 frames after previous cover
- f99: ref 79037: 37 -> 44 at (2080, 3034.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 46 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79098: 38 -> 33 at (2124, 3028), 4 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 38 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 33 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79105: 38 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 79103: 46 -> 33 at (2120.5, 3023), 2 frames after previous cover
- f106: ref 79098: 33 -> 50 at (2096, 3028.5), 3 frames after previous cover
- f106: ref 79102: 47 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 33 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 37 -> 44 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 35 -> 37 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 44 -> 32 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79097: 48 -> 35 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 50 -> 48 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79105: 46 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 46 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 79037: 32 -> 53 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79102: 33 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 33 at (2092.5, 3023.5), 2 frames after previous cover
- f129: ref 79105: 47 -> 50 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 46 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 38 -> 46 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 57 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 57 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 61 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 50 -> 70 at (1952.5, 3031), 4 frames after previous cover
- f220: ref 79097: 35 -> 44 at (1365.5, 2995), 1 frames after previous cover
- f220: ref 79102: 70 -> 35 at (1404, 3001.5), 1 frames after previous cover
- f220: ref 79103: 33 -> 70 at (1415, 3000.5), 1 frames after previous cover
- f220: ref 79108: 47 -> 33 at (1465, 3003), 2 frames after previous cover
- f221: ref 79097: 44 -> 48 at (1358, 2994), 1 frames after previous cover
- f221: ref 79098: 48 -> 35 at (1384, 2999.5), 1 frames after previous cover
- f221: ref 79102: 35 -> 70 at (1398, 3001), 1 frames after previous cover
- f221: ref 79103: 70 -> 50 at (1408, 2999.5), 1 frames after previous cover
- f221: ref 79105: 50 -> 33 at (1428.5, 2999.5), 1 frames after previous cover
- f221: ref 79108: 33 -> 46 at (1460, 3001), 1 frames after previous cover
- f221: ref 79111: 46 -> 56 at (1485.5, 3002), 1 frames after previous cover
- f221: ref 79115: 56 -> 38 at (1495.5, 3003.5), 1 frames after previous cover
- ... 19 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 347 | 1 | 30 (333), 29 (13), 38 (1) |
| 78969 | 352 (80..434) | 348 | 1 | 42 (336), 30 (11), 38 (1) |
| 78971 | 352 (84..439) | 349 | 0 | 29 (344), 32 (3), 35 (2) |
| 79045 | 355 (84..443) | 348 | 2 | 32 (348) |
| 79037 | 355 (86..445) | 353 | 1 | 53 (331), 44 (10), 33 (5), 37 (5), 38 (1), 32 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 44 (325), 37 (13), 35 (3), 33 (3), 38 (1) |
| 78899 | 365 (91..455) | 365 | 0 | 37 (347), 35 (15), 33 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 48 (247), 35 (111), 33 (4), 38 (1), 44 (1) |
| 79098 | 360 (97..467) | 355 | 2 | 35 (236), 48 (112), 33 (3), 50 (3), 38 (1) |
| 79102 | 371 (98..477) | 368 | 2 | 70 (337), 50 (19), 47 (5), 33 (4), 38 (1), 46 (1), 35 (1) |
| 79103 | 380 (99..481) | 378 | 2 | 51 (139), 50 (119), 33 (111), 46 (3), 47 (3), 38 (2), 70 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 50 (233), 33 (119), 47 (20), 46 (5), 38 (2) |
| 79108 | 385 (104..492) | 383 | 1 | 46 (289), 47 (90), 38 (2), 51 (1), 33 (1) |
| 79110 | 388 (106..497) | 388 | 0 | 51 (230), 56 (156), 38 (2) |
| 79111 | 386 (109..500) | 386 | 0 | 33 (157), 56 (117), 46 (92), 38 (20) |
| 79115 | 421 (111..531) | 417 | 2 | 62 (303), 56 (108), 38 (6) |
| 79116 | 411 (114..530) | 409 | 0 | 38 (234), 65 (154), 57 (13), 62 (8) |
| 79122 | 404 (118..532) | 402 | 0 | 47 (303), 57 (90), 61 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 57 (288), 62 (99), 47 (2) |
| 79128 | 402 (124..527) | 400 | 0 | 61 (397), 65 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 65 (251), 38 (154) |
| 79135 | 409 (129..542) | 409 | 0 | 69 (408), 38 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 71 (403), 69 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (390), 71 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 225 | 469..498 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 30/414/1007; tracks with internal gaps: 19; total internal gaps: 117; longest internal gap: 3; tracks ending in coasting: 25 (trailing rows total 733)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 29 | 78..468 | 391 | 391 | 357 | 34 | 5 | 1 | 29 | 78896, 78971 |
| 30 | 82..458 | 377 | 377 | 344 | 33 | 2 | 3 | 29 | 78896, 78969 |
| 32 | 86..472 | 387 | 387 | 352 | 35 | 6 | 1 | 29 | 78971, 79037, 79045 |
| 33 | 86..529 | 444 | 444 | 410 | 34 | 5 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 35 | 87..498 | 412 | 412 | 368 | 44 | 12 | 2 | 31 | 78897, 78899, 78971, 79097, 79098, 79102 |
| 37 | 91..484 | 394 | 394 | 365 | 29 | 0 | 0 | 29 | 78897, 78899, 79037 |
| 38 | 92..564 | 473 | 473 | 430 | 43 | 9 | 1 | 34 | 78896, 78897, 78969, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79134, 79135 |
| 42 | 96..463 | 368 | 368 | 336 | 32 | 2 | 2 | 29 | 78969 |
| 44 | 99..479 | 381 | 381 | 336 | 45 | 16 | 1 | 29 | 78897, 79037, 79097 |
| 46 | 100..521 | 422 | 422 | 390 | 32 | 3 | 1 | 29 | 79102, 79103, 79105, 79108, 79111 |
| 47 | 101..561 | 461 | 461 | 423 | 38 | 8 | 2 | 29 | 79102, 79103, 79105, 79108, 79122, 79132 |
| 48 | 103..490 | 388 | 388 | 359 | 29 | 0 | 0 | 29 | 79097, 79098 |
| 50 | 106..513 | 408 | 408 | 374 | 34 | 4 | 2 | 29 | 79098, 79102, 79103, 79105 |
| 51 | 108..510 | 403 | 403 | 370 | 33 | 4 | 1 | 29 | 79103, 79108, 79110 |
| 53 | 110..474 | 365 | 365 | 331 | 34 | 3 | 2 | 29 | 79037 |
| 56 | 113..526 | 414 | 414 | 381 | 33 | 4 | 1 | 29 | 79110, 79111, 79115 |
| 57 | 116..544 | 429 | 429 | 391 | 38 | 9 | 1 | 29 | 79116, 79122, 79132 |
| 61 | 120..556 | 437 | 437 | 406 | 31 | 2 | 1 | 29 | 79122, 79128 |
| 62 | 122..560 | 439 | 439 | 410 | 29 | 0 | 0 | 29 | 79115, 79116, 79132 |
| 65 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79116, 79128, 79134 |
| 69 | 129..571 | 443 | 443 | 409 | 34 | 5 | 1 | 29 | 79135, 79139 |
| 70 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102, 79103 |
| 71 | 134..566 | 433 | 433 | 404 | 29 | 0 | 0 | 29 | 79136, 79139 |
| 73 | 138..567 | 430 | 430 | 390 | 40 | 10 | 2 | 29 | 79136 |
| 225 | 469..498 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 859
- identity switches: 79; fragmentation (coverage interruptions): 15; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 78971: 35 -> 32 at (2121, 3034), 1 frames after previous cover
- f91: ref 78897: 35 -> 33 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 33 -> 37 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 29 -> 38 at (2059, 3033.5), 2 frames after previous cover
- f92: ref 78971: 32 -> 29 at (2101.5, 3036), 1 frames after previous cover
- f93: ref 78896: 38 -> 30 at (2052, 3033.5), 1 frames after previous cover
- f93: ref 78969: 30 -> 38 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78897: 33 -> 37 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 35 -> 33 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 37 -> 38 at (2112.5, 3034), 1 frames after previous cover
- f95: ref 78897: 37 -> 38 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 79037: 38 -> 37 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78897: 38 -> 35 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78969: 38 -> 42 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79097: 35 -> 38 at (2141, 3029), 1 frames after previous cover
- f97: ref 78897: 35 -> 37 at (2107, 3033), 1 frames after previous cover
- f97: ref 78899: 33 -> 35 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 38 -> 33 at (2135, 3028), 1 frames after previous cover
- f99: ref 79037: 37 -> 44 at (2080, 3034.5), 3 frames after previous cover
- f100: ref 79102: 38 -> 46 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79098: 38 -> 33 at (2124, 3028), 4 frames after previous cover
- f101: ref 79102: 46 -> 47 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 38 -> 46 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 33 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79105: 38 -> 46 at (2137, 3025), 1 frames after previous cover
- f105: ref 79103: 46 -> 33 at (2120.5, 3023), 2 frames after previous cover
- f106: ref 79098: 33 -> 50 at (2096, 3028.5), 3 frames after previous cover
- f106: ref 79102: 47 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 33 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f108: ref 79108: 38 -> 51 at (2131, 3027), 3 frames after previous cover
- f109: ref 78897: 37 -> 44 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 35 -> 37 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 44 -> 32 at (2019.5, 3034), 1 frames after previous cover
- f109: ref 79097: 48 -> 35 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 50 -> 48 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79105: 46 -> 47 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 51 -> 46 at (2125, 3025), 1 frames after previous cover
- f109: ref 79110: 38 -> 51 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 79037: 32 -> 53 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79102: 33 -> 50 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 47 -> 33 at (2092.5, 3023.5), 2 frames after previous cover
- f129: ref 79105: 47 -> 50 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 46 -> 47 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 38 -> 46 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 57 -> 38 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 61 -> 57 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 65 -> 61 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 50 -> 70 at (1952.5, 3031), 4 frames after previous cover
- f220: ref 79097: 35 -> 44 at (1365.5, 2995), 1 frames after previous cover
- f220: ref 79102: 70 -> 35 at (1404, 3001.5), 1 frames after previous cover
- f220: ref 79103: 33 -> 70 at (1415, 3000.5), 1 frames after previous cover
- f220: ref 79108: 47 -> 33 at (1465, 3003), 2 frames after previous cover
- f221: ref 79097: 44 -> 48 at (1358, 2994), 1 frames after previous cover
- f221: ref 79098: 48 -> 35 at (1384, 2999.5), 1 frames after previous cover
- f221: ref 79102: 35 -> 70 at (1398, 3001), 1 frames after previous cover
- f221: ref 79103: 70 -> 50 at (1408, 2999.5), 1 frames after previous cover
- f221: ref 79105: 50 -> 33 at (1428.5, 2999.5), 1 frames after previous cover
- f221: ref 79108: 33 -> 46 at (1460, 3001), 1 frames after previous cover
- f221: ref 79111: 46 -> 56 at (1485.5, 3002), 1 frames after previous cover
- f221: ref 79115: 56 -> 38 at (1495.5, 3003.5), 1 frames after previous cover
- ... 19 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 347 | 1 | 30 (333), 29 (13), 38 (1) |
| 78969 | 352 (80..434) | 348 | 1 | 42 (336), 30 (11), 38 (1) |
| 78971 | 352 (84..439) | 349 | 0 | 29 (344), 32 (3), 35 (2) |
| 79045 | 355 (84..443) | 348 | 2 | 32 (348) |
| 79037 | 355 (86..445) | 353 | 1 | 53 (331), 44 (10), 33 (5), 37 (5), 38 (1), 32 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 44 (325), 37 (13), 35 (3), 33 (3), 38 (1) |
| 78899 | 365 (91..455) | 365 | 0 | 37 (347), 35 (15), 33 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 48 (247), 35 (111), 33 (4), 38 (1), 44 (1) |
| 79098 | 360 (97..467) | 355 | 2 | 35 (236), 48 (112), 33 (3), 50 (3), 38 (1) |
| 79102 | 371 (98..477) | 368 | 2 | 70 (337), 50 (19), 47 (5), 33 (4), 38 (1), 46 (1), 35 (1) |
| 79103 | 380 (99..481) | 378 | 2 | 51 (139), 50 (119), 33 (111), 46 (3), 47 (3), 38 (2), 70 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 50 (233), 33 (119), 47 (20), 46 (5), 38 (2) |
| 79108 | 385 (104..492) | 383 | 1 | 46 (289), 47 (90), 38 (2), 51 (1), 33 (1) |
| 79110 | 388 (106..497) | 388 | 0 | 51 (230), 56 (156), 38 (2) |
| 79111 | 386 (109..500) | 386 | 0 | 33 (157), 56 (117), 46 (92), 38 (20) |
| 79115 | 421 (111..531) | 417 | 2 | 62 (303), 56 (108), 38 (6) |
| 79116 | 411 (114..530) | 409 | 0 | 38 (234), 65 (154), 57 (13), 62 (8) |
| 79122 | 404 (118..532) | 402 | 0 | 47 (303), 57 (90), 61 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 57 (288), 62 (99), 47 (2) |
| 79128 | 402 (124..527) | 400 | 0 | 61 (397), 65 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 65 (251), 38 (154) |
| 79135 | 409 (129..542) | 409 | 0 | 69 (408), 38 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 71 (403), 69 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (390), 71 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 225 | 469..498 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 30/414/1007; tracks with internal gaps: 19; total internal gaps: 117; longest internal gap: 3; tracks ending in coasting: 25 (trailing rows total 733)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 29 | 78..468 | 391 | 391 | 357 | 34 | 5 | 1 | 29 | 78896, 78971 |
| 30 | 82..458 | 377 | 377 | 344 | 33 | 2 | 3 | 29 | 78896, 78969 |
| 32 | 86..472 | 387 | 387 | 352 | 35 | 6 | 1 | 29 | 78971, 79037, 79045 |
| 33 | 86..529 | 444 | 444 | 410 | 34 | 5 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 35 | 87..498 | 412 | 412 | 368 | 44 | 12 | 2 | 31 | 78897, 78899, 78971, 79097, 79098, 79102 |
| 37 | 91..484 | 394 | 394 | 365 | 29 | 0 | 0 | 29 | 78897, 78899, 79037 |
| 38 | 92..564 | 473 | 473 | 430 | 43 | 9 | 1 | 34 | 78896, 78897, 78969, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79134, 79135 |
| 42 | 96..463 | 368 | 368 | 336 | 32 | 2 | 2 | 29 | 78969 |
| 44 | 99..479 | 381 | 381 | 336 | 45 | 16 | 1 | 29 | 78897, 79037, 79097 |
| 46 | 100..521 | 422 | 422 | 390 | 32 | 3 | 1 | 29 | 79102, 79103, 79105, 79108, 79111 |
| 47 | 101..561 | 461 | 461 | 423 | 38 | 8 | 2 | 29 | 79102, 79103, 79105, 79108, 79122, 79132 |
| 48 | 103..490 | 388 | 388 | 359 | 29 | 0 | 0 | 29 | 79097, 79098 |
| 50 | 106..513 | 408 | 408 | 374 | 34 | 4 | 2 | 29 | 79098, 79102, 79103, 79105 |
| 51 | 108..510 | 403 | 403 | 370 | 33 | 4 | 1 | 29 | 79103, 79108, 79110 |
| 53 | 110..474 | 365 | 365 | 331 | 34 | 3 | 2 | 29 | 79037 |
| 56 | 113..526 | 414 | 414 | 381 | 33 | 4 | 1 | 29 | 79110, 79111, 79115 |
| 57 | 116..544 | 429 | 429 | 391 | 38 | 9 | 1 | 29 | 79116, 79122, 79132 |
| 61 | 120..556 | 437 | 437 | 406 | 31 | 2 | 1 | 29 | 79122, 79128 |
| 62 | 122..560 | 439 | 439 | 410 | 29 | 0 | 0 | 29 | 79115, 79116, 79132 |
| 65 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79116, 79128, 79134 |
| 69 | 129..571 | 443 | 443 | 409 | 34 | 5 | 1 | 29 | 79135, 79139 |
| 70 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102, 79103 |
| 71 | 134..566 | 433 | 433 | 404 | 29 | 0 | 0 | 29 | 79136, 79139 |
| 73 | 138..567 | 430 | 430 | 390 | 40 | 10 | 2 | 29 | 79136 |
| 225 | 469..498 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
