# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=9c45431748e9
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise1.0_fp0.0_seed1/tracks.csv sha256=4fa9867161841dd2
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise1.0_fp0.0_seed1.csv sha256=9c45431748e921e8
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise1.0_fp0.0_seed1
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
| observations | none | 4 | 0.805 | 0.790 | 0.991 | 1.27 | 0.982 | 21 | 124.0 |
| observations | none | 6 | 0.869 | 0.853 | 0.993 | 1.27 | 0.984 | 14 | 117.0 |
| observations | none | 8 | 0.904 | 0.888 | 0.994 | 1.27 | 0.984 | 14 | 116.0 |
| observations | none | 12 | 0.937 | 0.929 | 0.993 | 1.31 | 0.984 | 15 | 116.0 |
| observations | ignore | 4 | 0.805 | 0.790 | 0.991 | 1.27 | 0.982 | 21 | 124.0 |
| observations | ignore | 6 | 0.869 | 0.853 | 0.993 | 1.27 | 0.984 | 14 | 117.0 |
| observations | ignore | 8 | 0.904 | 0.888 | 0.994 | 1.27 | 0.984 | 14 | 116.0 |
| observations | ignore | 12 | 0.937 | 0.929 | 0.993 | 1.31 | 0.984 | 15 | 116.0 |
| updates | none | 4 | 0.748 | 0.735 | 0.912 | 1.27 | 0.944 | 16 | 123.0 |
| updates | none | 6 | 0.806 | 0.793 | 0.913 | 1.27 | 0.946 | 14 | 117.0 |
| updates | none | 8 | 0.838 | 0.824 | 0.913 | 1.27 | 0.946 | 14 | 116.0 |
| updates | none | 12 | 0.869 | 0.862 | 0.913 | 1.31 | 0.946 | 15 | 116.0 |
| updates | ignore | 4 | 0.748 | 0.735 | 0.912 | 1.27 | 0.944 | 16 | 123.0 |
| updates | ignore | 6 | 0.806 | 0.793 | 0.913 | 1.27 | 0.946 | 14 | 117.0 |
| updates | ignore | 8 | 0.838 | 0.824 | 0.913 | 1.27 | 0.946 | 14 | 116.0 |
| updates | ignore | 12 | 0.869 | 0.862 | 0.913 | 1.31 | 0.946 | 15 | 116.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 0
- identity switches: 14; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 4 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 4 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 16 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 18 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 19 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 3 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 4 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 4 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 4 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 4 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 4 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 4 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 4 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 15 (385) |
| 79111 | 386 (109..500) | 384 | 0 | 13 (366), 16 (18) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 16 (396), 18 (13) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (389) |
| 79128 | 402 (124..527) | 400 | 0 | 19 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (409) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/393/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 4 | 86..481 | 396 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 5 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 6 | 91..445 | 355 | 350 | 350 | 0 | 0 | 0 | 0 | 79037 |
| 7 | 93..450 | 358 | 341 | 341 | 0 | 0 | 0 | 0 | 78897 |
| 8 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 9 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 10 | 100..492 | 393 | 388 | 388 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |
| 11 | 101..467 | 367 | 356 | 356 | 0 | 0 | 0 | 0 | 79098 |
| 12 | 103..484 | 382 | 378 | 378 | 0 | 0 | 0 | 0 | 79102, 79105 |
| 13 | 106..500 | 395 | 389 | 389 | 0 | 0 | 0 | 0 | 79108, 79111 |
| 15 | 110..497 | 388 | 385 | 385 | 0 | 0 | 0 | 0 | 79110 |
| 16 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 17 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115 |
| 18 | 116..532 | 417 | 406 | 406 | 0 | 0 | 0 | 0 | 79116, 79122 |
| 19 | 120..527 | 408 | 406 | 406 | 0 | 0 | 0 | 0 | 79122, 79128 |
| 20 | 122..515 | 394 | 389 | 389 | 0 | 0 | 0 | 0 | 79132 |
| 21 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 22 | 129..542 | 414 | 409 | 409 | 0 | 0 | 0 | 0 | 79135 |
| 23 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 24 | 134..537 | 404 | 404 | 404 | 0 | 0 | 0 | 0 | 79139 |
| 25 | 138..538 | 401 | 391 | 391 | 0 | 0 | 0 | 0 | 79136 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 0
- identity switches: 14; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 4 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 4 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 16 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 18 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 19 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 3 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 4 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 4 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 4 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 4 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 4 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 4 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 4 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 15 (385) |
| 79111 | 386 (109..500) | 384 | 0 | 13 (366), 16 (18) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 16 (396), 18 (13) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (389) |
| 79128 | 402 (124..527) | 400 | 0 | 19 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (409) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/393/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 4 | 86..481 | 396 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 5 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 6 | 91..445 | 355 | 350 | 350 | 0 | 0 | 0 | 0 | 79037 |
| 7 | 93..450 | 358 | 341 | 341 | 0 | 0 | 0 | 0 | 78897 |
| 8 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 9 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 10 | 100..492 | 393 | 388 | 388 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |
| 11 | 101..467 | 367 | 356 | 356 | 0 | 0 | 0 | 0 | 79098 |
| 12 | 103..484 | 382 | 378 | 378 | 0 | 0 | 0 | 0 | 79102, 79105 |
| 13 | 106..500 | 395 | 389 | 389 | 0 | 0 | 0 | 0 | 79108, 79111 |
| 15 | 110..497 | 388 | 385 | 385 | 0 | 0 | 0 | 0 | 79110 |
| 16 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 17 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115 |
| 18 | 116..532 | 417 | 406 | 406 | 0 | 0 | 0 | 0 | 79116, 79122 |
| 19 | 120..527 | 408 | 406 | 406 | 0 | 0 | 0 | 0 | 79122, 79128 |
| 20 | 122..515 | 394 | 389 | 389 | 0 | 0 | 0 | 0 | 79132 |
| 21 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 22 | 129..542 | 414 | 409 | 409 | 0 | 0 | 0 | 0 | 79135 |
| 23 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 24 | 134..537 | 404 | 404 | 404 | 0 | 0 | 0 | 0 | 79139 |
| 25 | 138..538 | 401 | 391 | 391 | 0 | 0 | 0 | 0 | 79136 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 815
- identity switches: 14; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 4 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 4 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 16 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 18 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 19 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 3 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 4 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 4 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 4 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 4 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 4 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 4 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 4 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 15 (385) |
| 79111 | 386 (109..500) | 384 | 0 | 13 (366), 16 (18) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 16 (396), 18 (13) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (389) |
| 79128 | 402 (124..527) | 400 | 0 | 19 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (409) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/422/1007; tracks with internal gaps: 20; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 4 | 86..510 | 425 | 425 | 393 | 32 | 2 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 5 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 6 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 7 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 8 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 9 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 10 | 100..521 | 422 | 422 | 388 | 34 | 5 | 1 | 29 | 79103, 79105, 79108 |
| 11 | 101..496 | 396 | 396 | 356 | 40 | 10 | 2 | 29 | 79098 |
| 12 | 103..513 | 411 | 411 | 378 | 33 | 4 | 1 | 29 | 79102, 79105 |
| 13 | 106..529 | 424 | 424 | 389 | 35 | 5 | 2 | 29 | 79108, 79111 |
| 15 | 110..526 | 417 | 417 | 385 | 32 | 3 | 1 | 29 | 79110 |
| 16 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 17 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115 |
| 18 | 116..561 | 446 | 446 | 406 | 40 | 11 | 1 | 29 | 79116, 79122 |
| 19 | 120..556 | 437 | 437 | 406 | 31 | 2 | 1 | 29 | 79122, 79128 |
| 20 | 122..544 | 423 | 423 | 389 | 34 | 5 | 1 | 29 | 79132 |
| 21 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 22 | 129..571 | 443 | 443 | 409 | 34 | 5 | 1 | 29 | 79135 |
| 23 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 24 | 134..566 | 433 | 433 | 404 | 29 | 0 | 0 | 29 | 79139 |
| 25 | 138..567 | 430 | 430 | 391 | 39 | 9 | 2 | 29 | 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 815
- identity switches: 14; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 4 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 4 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 4 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 4 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 4 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 4 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79111: 16 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 18 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 19 at (2125, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 3 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 4 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 4 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 4 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 4 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 4 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 4 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 4 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 15 (385) |
| 79111 | 386 (109..500) | 384 | 0 | 13 (366), 16 (18) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 16 (396), 18 (13) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (389) |
| 79128 | 402 (124..527) | 400 | 0 | 19 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (409) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/422/1007; tracks with internal gaps: 20; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 4 | 86..510 | 425 | 425 | 393 | 32 | 2 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 5 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 6 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 7 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 8 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 9 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 10 | 100..521 | 422 | 422 | 388 | 34 | 5 | 1 | 29 | 79103, 79105, 79108 |
| 11 | 101..496 | 396 | 396 | 356 | 40 | 10 | 2 | 29 | 79098 |
| 12 | 103..513 | 411 | 411 | 378 | 33 | 4 | 1 | 29 | 79102, 79105 |
| 13 | 106..529 | 424 | 424 | 389 | 35 | 5 | 2 | 29 | 79108, 79111 |
| 15 | 110..526 | 417 | 417 | 385 | 32 | 3 | 1 | 29 | 79110 |
| 16 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 17 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115 |
| 18 | 116..561 | 446 | 446 | 406 | 40 | 11 | 1 | 29 | 79116, 79122 |
| 19 | 120..556 | 437 | 437 | 406 | 31 | 2 | 1 | 29 | 79122, 79128 |
| 20 | 122..544 | 423 | 423 | 389 | 34 | 5 | 1 | 29 | 79132 |
| 21 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 22 | 129..571 | 443 | 443 | 409 | 34 | 5 | 1 | 29 | 79135 |
| 23 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 24 | 134..566 | 433 | 433 | 404 | 29 | 0 | 0 | 29 | 79139 |
| 25 | 138..567 | 430 | 430 | 391 | 39 | 9 | 2 | 29 | 79136 |
