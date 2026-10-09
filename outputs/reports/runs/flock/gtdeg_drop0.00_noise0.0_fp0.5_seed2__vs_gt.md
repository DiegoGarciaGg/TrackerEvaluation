# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=bfa89569f923
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise0.0_fp0.5_seed2/tracks.csv sha256=68df83bee1adefc3
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise0.0_fp0.5_seed2.csv sha256=bfa89569f923f994
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise0.0_fp0.5_seed2
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
| observations | none | 4 | 0.801 | 0.647 | 0.988 | 0.01 | 0.773 | 52 | 116.0 |
| observations | none | 6 | 0.801 | 0.648 | 0.988 | 0.01 | 0.773 | 48 | 116.0 |
| observations | none | 8 | 0.801 | 0.650 | 0.988 | 0.01 | 0.774 | 48 | 116.0 |
| observations | none | 12 | 0.796 | 0.667 | 0.988 | 0.05 | 0.783 | 49 | 115.0 |
| observations | ignore | 4 | 0.801 | 0.647 | 0.988 | 0.01 | 0.773 | 52 | 116.0 |
| observations | ignore | 6 | 0.801 | 0.648 | 0.988 | 0.01 | 0.773 | 48 | 116.0 |
| observations | ignore | 8 | 0.801 | 0.650 | 0.988 | 0.01 | 0.774 | 48 | 116.0 |
| observations | ignore | 12 | 0.796 | 0.667 | 0.988 | 0.05 | 0.783 | 49 | 115.0 |
| updates | none | 4 | 0.741 | 0.606 | 0.894 | 0.01 | 0.739 | 50 | 116.0 |
| updates | none | 6 | 0.742 | 0.607 | 0.894 | 0.01 | 0.739 | 48 | 116.0 |
| updates | none | 8 | 0.741 | 0.609 | 0.894 | 0.01 | 0.740 | 48 | 116.0 |
| updates | none | 12 | 0.737 | 0.624 | 0.894 | 0.06 | 0.749 | 49 | 115.0 |
| updates | ignore | 4 | 0.741 | 0.606 | 0.894 | 0.01 | 0.739 | 50 | 116.0 |
| updates | ignore | 6 | 0.742 | 0.607 | 0.894 | 0.01 | 0.739 | 48 | 116.0 |
| updates | ignore | 8 | 0.741 | 0.609 | 0.894 | 0.01 | 0.740 | 48 | 116.0 |
| updates | ignore | 12 | 0.737 | 0.624 | 0.894 | 0.06 | 0.749 | 49 | 115.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 17
- identity switches: 48; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 39 -> 47 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 39 -> 50 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 39 -> 52 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 39 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 39 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 55 -> 39 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 39 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 75 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 79 -> 77 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 77 -> 75 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 84 at (1952.5, 3031), 4 frames after previous cover
- f165: ref 78899: 52 -> 50 at (1693.5, 3029.5), 1 frames after previous cover
- f165: ref 79098: 56 -> 52 at (1733.5, 3026), 1 frames after previous cover
- f165: ref 79102: 84 -> 56 at (1747, 3026), 1 frames after previous cover
- f166: ref 78899: 50 -> 53 at (1687, 3029.5), 1 frames after previous cover
- f166: ref 79097: 53 -> 52 at (1709.5, 3029), 1 frames after previous cover
- f166: ref 79098: 52 -> 56 at (1727, 3027), 1 frames after previous cover
- f166: ref 79102: 56 -> 84 at (1740.5, 3026), 1 frames after previous cover
- f295: ref 78896: 33 -> 35 at (725, 2984.5), 4 frames after previous cover
- f295: ref 78899: 53 -> 52 at (858.5, 2986), 1 frames after previous cover
- f295: ref 78969: 35 -> 47 at (749.5, 2983.5), 1 frames after previous cover
- f295: ref 79037: 47 -> 53 at (814.5, 2984), 1 frames after previous cover
- f295: ref 79097: 52 -> 84 at (884, 2987.5), 1 frames after previous cover
- f296: ref 79102: 84 -> 58 at (938, 2986), 2 frames after previous cover
- f297: ref 78971: 43 -> 47 at (777.5, 2989.5), 1 frames after previous cover
- f297: ref 79097: 84 -> 43 at (873.5, 2983), 1 frames after previous cover
- f297: ref 79098: 56 -> 84 at (906.5, 2987), 1 frames after previous cover
- f297: ref 79102: 58 -> 56 at (933, 2985.5), 1 frames after previous cover
- f297: ref 79103: 39 -> 58 at (953.5, 2983), 1 frames after previous cover
- f297: ref 79105: 58 -> 39 at (968.5, 2981.5), 2 frames after previous cover
- f298: ref 78899: 52 -> 43 at (840, 2985.5), 1 frames after previous cover
- f298: ref 79097: 43 -> 52 at (866.5, 2984), 1 frames after previous cover
- f301: ref 78969: 47 -> 176 at (710.5, 2981.5), 5 frames after previous cover
- f375: ref 79103: 58 -> 39 at (498.5, 2963), 1 frames after previous cover
- f375: ref 79105: 39 -> 64 at (516, 2963), 1 frames after previous cover
- f375: ref 79108: 64 -> 55 at (540, 2967.5), 1 frames after previous cover
- f375: ref 79110: 55 -> 67 at (557.5, 2968), 1 frames after previous cover
- f375: ref 79122: 67 -> 72 at (641, 2966.5), 1 frames after previous cover
- f377: ref 79103: 39 -> 58 at (489, 2964), 1 frames after previous cover
- f377: ref 79105: 64 -> 39 at (507.5, 2964.5), 1 frames after previous cover
- f377: ref 79108: 55 -> 64 at (530.5, 2963.5), 1 frames after previous cover
- f377: ref 79110: 67 -> 55 at (547.5, 2965), 1 frames after previous cover
- f377: ref 79111: 68 -> 67 at (568.5, 2964.5), 1 frames after previous cover
- f377: ref 79116: 72 -> 68 at (675, 2953), 3 frames after previous cover
- f467: ref 79139: 85 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 85 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (214), 35 (134) |
| 78969 | 352 (80..434) | 348 | 1 | 35 (213), 176 (133), 47 (2) |
| 78971 | 352 (84..439) | 348 | 0 | 43 (205), 47 (143) |
| 79045 | 355 (84..443) | 353 | 0 | 38 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 47 (204), 53 (146), 39 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 50 (341), 39 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 43 (158), 53 (129), 52 (72), 39 (3), 50 (1) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (291), 53 (67), 39 (3), 84 (2), 43 (1) |
| 79098 | 360 (97..467) | 358 | 1 | 56 (191), 84 (164), 39 (2), 52 (1) |
| 79102 | 371 (98..477) | 366 | 2 | 56 (178), 84 (159), 58 (27), 39 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 39 (198), 58 (180), 55 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 39 (184), 58 (166), 55 (27), 64 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 64 (381), 55 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (365), 67 (20) |
| 79111 | 386 (109..500) | 384 | 0 | 68 (260), 67 (124) |
| 79115 | 421 (111..531) | 419 | 0 | 71 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 72 (255), 68 (154) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (236), 72 (157), 75 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 75 (382), 77 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 77 (397), 79 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 79 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 85 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 85 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 88 (391) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 271 | 508..508 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 1/396/1007; tracks with internal gaps: 5; total internal gaps: 5; longest internal gap: 1; tracks ending in coasting: 5 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..299 | 222 | 216 | 214 | 2 | 0 | 0 | 2 | 78896 |
| 35 | 82..429 | 348 | 347 | 347 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 38 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 39 | 86..484 | 399 | 397 | 397 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 43 | 88..455 | 368 | 364 | 364 | 0 | 0 | 0 | 0 | 78899, 78971, 79097 |
| 47 | 91..439 | 349 | 349 | 349 | 0 | 0 | 0 | 0 | 78969, 78971, 79037 |
| 50 | 93..450 | 358 | 342 | 342 | 0 | 0 | 0 | 0 | 78897, 78899 |
| 52 | 96..461 | 366 | 364 | 364 | 0 | 0 | 0 | 0 | 78899, 79097, 79098 |
| 53 | 99..445 | 347 | 343 | 342 | 1 | 1 | 1 | 0 | 78899, 79037, 79097 |
| 55 | 100..497 | 398 | 395 | 395 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110 |
| 56 | 101..522 | 422 | 375 | 369 | 6 | 1 | 1 | 5 | 79098, 79102 |
| 58 | 103..481 | 379 | 374 | 373 | 1 | 1 | 1 | 0 | 79102, 79103, 79105 |
| 64 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 67 | 110..510 | 401 | 382 | 380 | 2 | 1 | 1 | 1 | 79110, 79111, 79122 |
| 68 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 71 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115 |
| 72 | 116..571 | 456 | 415 | 412 | 3 | 0 | 0 | 3 | 79116, 79122 |
| 75 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 77 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 79 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 82 | 129..537 | 409 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 84 | 132..467 | 336 | 326 | 325 | 1 | 1 | 1 | 0 | 79097, 79098, 79102 |
| 85 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 88 | 138..538 | 401 | 391 | 391 | 0 | 0 | 0 | 0 | 79136 |
| 176 | 301..434 | 134 | 133 | 133 | 0 | 0 | 0 | 0 | 78969 |
| 271 | 508..508 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 17
- identity switches: 48; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 39 -> 47 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 39 -> 50 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 39 -> 52 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 39 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 39 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 55 -> 39 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 39 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 75 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 79 -> 77 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 77 -> 75 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 84 at (1952.5, 3031), 4 frames after previous cover
- f165: ref 78899: 52 -> 50 at (1693.5, 3029.5), 1 frames after previous cover
- f165: ref 79098: 56 -> 52 at (1733.5, 3026), 1 frames after previous cover
- f165: ref 79102: 84 -> 56 at (1747, 3026), 1 frames after previous cover
- f166: ref 78899: 50 -> 53 at (1687, 3029.5), 1 frames after previous cover
- f166: ref 79097: 53 -> 52 at (1709.5, 3029), 1 frames after previous cover
- f166: ref 79098: 52 -> 56 at (1727, 3027), 1 frames after previous cover
- f166: ref 79102: 56 -> 84 at (1740.5, 3026), 1 frames after previous cover
- f295: ref 78896: 33 -> 35 at (725, 2984.5), 4 frames after previous cover
- f295: ref 78899: 53 -> 52 at (858.5, 2986), 1 frames after previous cover
- f295: ref 78969: 35 -> 47 at (749.5, 2983.5), 1 frames after previous cover
- f295: ref 79037: 47 -> 53 at (814.5, 2984), 1 frames after previous cover
- f295: ref 79097: 52 -> 84 at (884, 2987.5), 1 frames after previous cover
- f296: ref 79102: 84 -> 58 at (938, 2986), 2 frames after previous cover
- f297: ref 78971: 43 -> 47 at (777.5, 2989.5), 1 frames after previous cover
- f297: ref 79097: 84 -> 43 at (873.5, 2983), 1 frames after previous cover
- f297: ref 79098: 56 -> 84 at (906.5, 2987), 1 frames after previous cover
- f297: ref 79102: 58 -> 56 at (933, 2985.5), 1 frames after previous cover
- f297: ref 79103: 39 -> 58 at (953.5, 2983), 1 frames after previous cover
- f297: ref 79105: 58 -> 39 at (968.5, 2981.5), 2 frames after previous cover
- f298: ref 78899: 52 -> 43 at (840, 2985.5), 1 frames after previous cover
- f298: ref 79097: 43 -> 52 at (866.5, 2984), 1 frames after previous cover
- f301: ref 78969: 47 -> 176 at (710.5, 2981.5), 5 frames after previous cover
- f375: ref 79103: 58 -> 39 at (498.5, 2963), 1 frames after previous cover
- f375: ref 79105: 39 -> 64 at (516, 2963), 1 frames after previous cover
- f375: ref 79108: 64 -> 55 at (540, 2967.5), 1 frames after previous cover
- f375: ref 79110: 55 -> 67 at (557.5, 2968), 1 frames after previous cover
- f375: ref 79122: 67 -> 72 at (641, 2966.5), 1 frames after previous cover
- f377: ref 79103: 39 -> 58 at (489, 2964), 1 frames after previous cover
- f377: ref 79105: 64 -> 39 at (507.5, 2964.5), 1 frames after previous cover
- f377: ref 79108: 55 -> 64 at (530.5, 2963.5), 1 frames after previous cover
- f377: ref 79110: 67 -> 55 at (547.5, 2965), 1 frames after previous cover
- f377: ref 79111: 68 -> 67 at (568.5, 2964.5), 1 frames after previous cover
- f377: ref 79116: 72 -> 68 at (675, 2953), 3 frames after previous cover
- f467: ref 79139: 85 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 85 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (214), 35 (134) |
| 78969 | 352 (80..434) | 348 | 1 | 35 (213), 176 (133), 47 (2) |
| 78971 | 352 (84..439) | 348 | 0 | 43 (205), 47 (143) |
| 79045 | 355 (84..443) | 353 | 0 | 38 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 47 (204), 53 (146), 39 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 50 (341), 39 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 43 (158), 53 (129), 52 (72), 39 (3), 50 (1) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (291), 53 (67), 39 (3), 84 (2), 43 (1) |
| 79098 | 360 (97..467) | 358 | 1 | 56 (191), 84 (164), 39 (2), 52 (1) |
| 79102 | 371 (98..477) | 366 | 2 | 56 (178), 84 (159), 58 (27), 39 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 39 (198), 58 (180), 55 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 39 (184), 58 (166), 55 (27), 64 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 64 (381), 55 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (365), 67 (20) |
| 79111 | 386 (109..500) | 384 | 0 | 68 (260), 67 (124) |
| 79115 | 421 (111..531) | 419 | 0 | 71 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 72 (255), 68 (154) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (236), 72 (157), 75 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 75 (382), 77 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 77 (397), 79 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 79 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 85 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 85 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 88 (391) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 271 | 508..508 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 1/396/1007; tracks with internal gaps: 5; total internal gaps: 5; longest internal gap: 1; tracks ending in coasting: 5 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..299 | 222 | 216 | 214 | 2 | 0 | 0 | 2 | 78896 |
| 35 | 82..429 | 348 | 347 | 347 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 38 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 39 | 86..484 | 399 | 397 | 397 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 43 | 88..455 | 368 | 364 | 364 | 0 | 0 | 0 | 0 | 78899, 78971, 79097 |
| 47 | 91..439 | 349 | 349 | 349 | 0 | 0 | 0 | 0 | 78969, 78971, 79037 |
| 50 | 93..450 | 358 | 342 | 342 | 0 | 0 | 0 | 0 | 78897, 78899 |
| 52 | 96..461 | 366 | 364 | 364 | 0 | 0 | 0 | 0 | 78899, 79097, 79098 |
| 53 | 99..445 | 347 | 343 | 342 | 1 | 1 | 1 | 0 | 78899, 79037, 79097 |
| 55 | 100..497 | 398 | 395 | 395 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110 |
| 56 | 101..522 | 422 | 375 | 369 | 6 | 1 | 1 | 5 | 79098, 79102 |
| 58 | 103..481 | 379 | 374 | 373 | 1 | 1 | 1 | 0 | 79102, 79103, 79105 |
| 64 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 67 | 110..510 | 401 | 382 | 380 | 2 | 1 | 1 | 1 | 79110, 79111, 79122 |
| 68 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 71 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115 |
| 72 | 116..571 | 456 | 415 | 412 | 3 | 0 | 0 | 3 | 79116, 79122 |
| 75 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 77 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 79 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 82 | 129..537 | 409 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 84 | 132..467 | 336 | 326 | 325 | 1 | 1 | 1 | 0 | 79097, 79098, 79102 |
| 85 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 88 | 138..538 | 401 | 391 | 391 | 0 | 0 | 0 | 0 | 79136 |
| 176 | 301..434 | 134 | 133 | 133 | 0 | 0 | 0 | 0 | 78969 |
| 271 | 508..508 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 969
- identity switches: 48; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 39 -> 47 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 39 -> 50 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 39 -> 52 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 39 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 39 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 55 -> 39 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 39 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 75 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 79 -> 77 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 77 -> 75 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 84 at (1952.5, 3031), 4 frames after previous cover
- f165: ref 78899: 52 -> 50 at (1693.5, 3029.5), 1 frames after previous cover
- f165: ref 79098: 56 -> 52 at (1733.5, 3026), 1 frames after previous cover
- f165: ref 79102: 84 -> 56 at (1747, 3026), 1 frames after previous cover
- f166: ref 78899: 50 -> 53 at (1687, 3029.5), 1 frames after previous cover
- f166: ref 79097: 53 -> 52 at (1709.5, 3029), 1 frames after previous cover
- f166: ref 79098: 52 -> 56 at (1727, 3027), 1 frames after previous cover
- f166: ref 79102: 56 -> 84 at (1740.5, 3026), 1 frames after previous cover
- f295: ref 78896: 33 -> 35 at (725, 2984.5), 4 frames after previous cover
- f295: ref 78899: 53 -> 52 at (858.5, 2986), 1 frames after previous cover
- f295: ref 78969: 35 -> 47 at (749.5, 2983.5), 1 frames after previous cover
- f295: ref 79037: 47 -> 53 at (814.5, 2984), 1 frames after previous cover
- f295: ref 79097: 52 -> 84 at (884, 2987.5), 1 frames after previous cover
- f296: ref 79102: 84 -> 58 at (938, 2986), 2 frames after previous cover
- f297: ref 78971: 43 -> 47 at (777.5, 2989.5), 1 frames after previous cover
- f297: ref 79097: 84 -> 43 at (873.5, 2983), 1 frames after previous cover
- f297: ref 79098: 56 -> 84 at (906.5, 2987), 1 frames after previous cover
- f297: ref 79102: 58 -> 56 at (933, 2985.5), 1 frames after previous cover
- f297: ref 79103: 39 -> 58 at (953.5, 2983), 1 frames after previous cover
- f297: ref 79105: 58 -> 39 at (968.5, 2981.5), 2 frames after previous cover
- f298: ref 78899: 52 -> 43 at (840, 2985.5), 1 frames after previous cover
- f298: ref 79097: 43 -> 52 at (866.5, 2984), 1 frames after previous cover
- f301: ref 78969: 47 -> 176 at (710.5, 2981.5), 5 frames after previous cover
- f375: ref 79103: 58 -> 39 at (498.5, 2963), 1 frames after previous cover
- f375: ref 79105: 39 -> 64 at (516, 2963), 1 frames after previous cover
- f375: ref 79108: 64 -> 55 at (540, 2967.5), 1 frames after previous cover
- f375: ref 79110: 55 -> 67 at (557.5, 2968), 1 frames after previous cover
- f375: ref 79122: 67 -> 72 at (641, 2966.5), 1 frames after previous cover
- f377: ref 79103: 39 -> 58 at (489, 2964), 1 frames after previous cover
- f377: ref 79105: 64 -> 39 at (507.5, 2964.5), 1 frames after previous cover
- f377: ref 79108: 55 -> 64 at (530.5, 2963.5), 1 frames after previous cover
- f377: ref 79110: 67 -> 55 at (547.5, 2965), 1 frames after previous cover
- f377: ref 79111: 68 -> 67 at (568.5, 2964.5), 1 frames after previous cover
- f377: ref 79116: 72 -> 68 at (675, 2953), 3 frames after previous cover
- f467: ref 79139: 85 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 85 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (214), 35 (134) |
| 78969 | 352 (80..434) | 348 | 1 | 35 (213), 176 (133), 47 (2) |
| 78971 | 352 (84..439) | 348 | 0 | 43 (205), 47 (143) |
| 79045 | 355 (84..443) | 353 | 0 | 38 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 47 (204), 53 (146), 39 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 50 (341), 39 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 43 (158), 53 (129), 52 (72), 39 (3), 50 (1) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (291), 53 (67), 39 (3), 84 (2), 43 (1) |
| 79098 | 360 (97..467) | 358 | 1 | 56 (191), 84 (164), 39 (2), 52 (1) |
| 79102 | 371 (98..477) | 366 | 2 | 56 (178), 84 (159), 58 (27), 39 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 39 (198), 58 (180), 55 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 39 (184), 58 (166), 55 (27), 64 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 64 (381), 55 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (365), 67 (20) |
| 79111 | 386 (109..500) | 384 | 0 | 68 (260), 67 (124) |
| 79115 | 421 (111..531) | 419 | 0 | 71 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 72 (255), 68 (154) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (236), 72 (157), 75 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 75 (382), 77 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 77 (397), 79 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 79 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 85 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 85 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 88 (391) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 271 | 508..537 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 30/425/1007; tracks with internal gaps: 21; total internal gaps: 105; longest internal gap: 2; tracks ending in coasting: 26 (trailing rows total 857)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..328 | 251 | 251 | 214 | 37 | 0 | 0 | 37 | 78896 |
| 35 | 82..458 | 377 | 377 | 347 | 30 | 1 | 1 | 29 | 78896, 78969 |
| 38 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 39 | 86..513 | 428 | 428 | 397 | 31 | 2 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 43 | 88..484 | 397 | 397 | 364 | 33 | 4 | 1 | 29 | 78899, 78971, 79097 |
| 47 | 91..468 | 378 | 378 | 349 | 29 | 0 | 0 | 29 | 78969, 78971, 79037 |
| 50 | 93..479 | 387 | 387 | 342 | 45 | 16 | 1 | 29 | 78897, 78899 |
| 52 | 96..490 | 395 | 395 | 364 | 31 | 2 | 1 | 29 | 78899, 79097, 79098 |
| 53 | 99..474 | 376 | 376 | 342 | 34 | 3 | 2 | 29 | 78899, 79037, 79097 |
| 55 | 100..526 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79103, 79105, 79108, 79110 |
| 56 | 101..551 | 451 | 451 | 369 | 82 | 8 | 1 | 74 | 79098, 79102 |
| 58 | 103..510 | 408 | 408 | 373 | 35 | 4 | 2 | 29 | 79102, 79103, 79105 |
| 64 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79105, 79108 |
| 67 | 110..539 | 430 | 430 | 380 | 50 | 11 | 1 | 39 | 79110, 79111, 79122 |
| 68 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 71 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115 |
| 72 | 116..600 | 485 | 485 | 412 | 73 | 5 | 1 | 68 | 79116, 79122 |
| 75 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 77 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 79 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 82 | 129..566 | 438 | 438 | 405 | 33 | 4 | 1 | 29 | 79135, 79139 |
| 84 | 132..496 | 365 | 365 | 325 | 40 | 10 | 2 | 29 | 79097, 79098, 79102 |
| 85 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 88 | 138..567 | 430 | 430 | 391 | 39 | 9 | 2 | 29 | 79136 |
| 176 | 301..463 | 163 | 163 | 133 | 30 | 1 | 1 | 29 | 78969 |
| 271 | 508..537 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10089; unmatched reference entries: 53; unmatched candidate entries: 969
- identity switches: 48; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 39 -> 47 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 39 -> 50 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 39 -> 52 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 39 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 39 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 55 -> 39 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 39 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 75 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 79 -> 77 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 77 -> 75 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 84 at (1952.5, 3031), 4 frames after previous cover
- f165: ref 78899: 52 -> 50 at (1693.5, 3029.5), 1 frames after previous cover
- f165: ref 79098: 56 -> 52 at (1733.5, 3026), 1 frames after previous cover
- f165: ref 79102: 84 -> 56 at (1747, 3026), 1 frames after previous cover
- f166: ref 78899: 50 -> 53 at (1687, 3029.5), 1 frames after previous cover
- f166: ref 79097: 53 -> 52 at (1709.5, 3029), 1 frames after previous cover
- f166: ref 79098: 52 -> 56 at (1727, 3027), 1 frames after previous cover
- f166: ref 79102: 56 -> 84 at (1740.5, 3026), 1 frames after previous cover
- f295: ref 78896: 33 -> 35 at (725, 2984.5), 4 frames after previous cover
- f295: ref 78899: 53 -> 52 at (858.5, 2986), 1 frames after previous cover
- f295: ref 78969: 35 -> 47 at (749.5, 2983.5), 1 frames after previous cover
- f295: ref 79037: 47 -> 53 at (814.5, 2984), 1 frames after previous cover
- f295: ref 79097: 52 -> 84 at (884, 2987.5), 1 frames after previous cover
- f296: ref 79102: 84 -> 58 at (938, 2986), 2 frames after previous cover
- f297: ref 78971: 43 -> 47 at (777.5, 2989.5), 1 frames after previous cover
- f297: ref 79097: 84 -> 43 at (873.5, 2983), 1 frames after previous cover
- f297: ref 79098: 56 -> 84 at (906.5, 2987), 1 frames after previous cover
- f297: ref 79102: 58 -> 56 at (933, 2985.5), 1 frames after previous cover
- f297: ref 79103: 39 -> 58 at (953.5, 2983), 1 frames after previous cover
- f297: ref 79105: 58 -> 39 at (968.5, 2981.5), 2 frames after previous cover
- f298: ref 78899: 52 -> 43 at (840, 2985.5), 1 frames after previous cover
- f298: ref 79097: 43 -> 52 at (866.5, 2984), 1 frames after previous cover
- f301: ref 78969: 47 -> 176 at (710.5, 2981.5), 5 frames after previous cover
- f375: ref 79103: 58 -> 39 at (498.5, 2963), 1 frames after previous cover
- f375: ref 79105: 39 -> 64 at (516, 2963), 1 frames after previous cover
- f375: ref 79108: 64 -> 55 at (540, 2967.5), 1 frames after previous cover
- f375: ref 79110: 55 -> 67 at (557.5, 2968), 1 frames after previous cover
- f375: ref 79122: 67 -> 72 at (641, 2966.5), 1 frames after previous cover
- f377: ref 79103: 39 -> 58 at (489, 2964), 1 frames after previous cover
- f377: ref 79105: 64 -> 39 at (507.5, 2964.5), 1 frames after previous cover
- f377: ref 79108: 55 -> 64 at (530.5, 2963.5), 1 frames after previous cover
- f377: ref 79110: 67 -> 55 at (547.5, 2965), 1 frames after previous cover
- f377: ref 79111: 68 -> 67 at (568.5, 2964.5), 1 frames after previous cover
- f377: ref 79116: 72 -> 68 at (675, 2953), 3 frames after previous cover
- f467: ref 79139: 85 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 85 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (214), 35 (134) |
| 78969 | 352 (80..434) | 348 | 1 | 35 (213), 176 (133), 47 (2) |
| 78971 | 352 (84..439) | 348 | 0 | 43 (205), 47 (143) |
| 79045 | 355 (84..443) | 353 | 0 | 38 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 47 (204), 53 (146), 39 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 50 (341), 39 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 43 (158), 53 (129), 52 (72), 39 (3), 50 (1) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (291), 53 (67), 39 (3), 84 (2), 43 (1) |
| 79098 | 360 (97..467) | 358 | 1 | 56 (191), 84 (164), 39 (2), 52 (1) |
| 79102 | 371 (98..477) | 366 | 2 | 56 (178), 84 (159), 58 (27), 39 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 39 (198), 58 (180), 55 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 39 (184), 58 (166), 55 (27), 64 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 64 (381), 55 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (365), 67 (20) |
| 79111 | 386 (109..500) | 384 | 0 | 68 (260), 67 (124) |
| 79115 | 421 (111..531) | 419 | 0 | 71 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 72 (255), 68 (154) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (236), 72 (157), 75 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 75 (382), 77 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 77 (397), 79 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 79 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 85 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 85 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 88 (391) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 271 | 508..537 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 30/425/1007; tracks with internal gaps: 21; total internal gaps: 105; longest internal gap: 2; tracks ending in coasting: 26 (trailing rows total 857)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..328 | 251 | 251 | 214 | 37 | 0 | 0 | 37 | 78896 |
| 35 | 82..458 | 377 | 377 | 347 | 30 | 1 | 1 | 29 | 78896, 78969 |
| 38 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 39 | 86..513 | 428 | 428 | 397 | 31 | 2 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105 |
| 43 | 88..484 | 397 | 397 | 364 | 33 | 4 | 1 | 29 | 78899, 78971, 79097 |
| 47 | 91..468 | 378 | 378 | 349 | 29 | 0 | 0 | 29 | 78969, 78971, 79037 |
| 50 | 93..479 | 387 | 387 | 342 | 45 | 16 | 1 | 29 | 78897, 78899 |
| 52 | 96..490 | 395 | 395 | 364 | 31 | 2 | 1 | 29 | 78899, 79097, 79098 |
| 53 | 99..474 | 376 | 376 | 342 | 34 | 3 | 2 | 29 | 78899, 79037, 79097 |
| 55 | 100..526 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79103, 79105, 79108, 79110 |
| 56 | 101..551 | 451 | 451 | 369 | 82 | 8 | 1 | 74 | 79098, 79102 |
| 58 | 103..510 | 408 | 408 | 373 | 35 | 4 | 2 | 29 | 79102, 79103, 79105 |
| 64 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79105, 79108 |
| 67 | 110..539 | 430 | 430 | 380 | 50 | 11 | 1 | 39 | 79110, 79111, 79122 |
| 68 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 71 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115 |
| 72 | 116..600 | 485 | 485 | 412 | 73 | 5 | 1 | 68 | 79116, 79122 |
| 75 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 77 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 79 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 82 | 129..566 | 438 | 438 | 405 | 33 | 4 | 1 | 29 | 79135, 79139 |
| 84 | 132..496 | 365 | 365 | 325 | 40 | 10 | 2 | 29 | 79097, 79098, 79102 |
| 85 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 88 | 138..567 | 430 | 430 | 391 | 39 | 9 | 2 | 29 | 79136 |
| 176 | 301..463 | 163 | 163 | 133 | 30 | 1 | 1 | 29 | 78969 |
| 271 | 508..537 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
