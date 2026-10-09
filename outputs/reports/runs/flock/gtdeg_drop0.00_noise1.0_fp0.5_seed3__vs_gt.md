# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=10a75a029a0f
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise1.0_fp0.5_seed3/tracks.csv sha256=5ac067bb611010d9
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise1.0_fp0.5_seed3.csv sha256=10a75a029a0f8558
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise1.0_fp0.5_seed3
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
| observations | none | 4 | 0.729 | 0.650 | 0.989 | 1.27 | 0.872 | 28 | 126.0 |
| observations | none | 6 | 0.786 | 0.703 | 0.992 | 1.27 | 0.873 | 23 | 112.0 |
| observations | none | 8 | 0.817 | 0.735 | 0.992 | 1.27 | 0.874 | 23 | 111.0 |
| observations | none | 12 | 0.851 | 0.772 | 0.992 | 1.27 | 0.881 | 23 | 111.0 |
| observations | ignore | 4 | 0.729 | 0.650 | 0.989 | 1.27 | 0.872 | 28 | 126.0 |
| observations | ignore | 6 | 0.786 | 0.703 | 0.992 | 1.27 | 0.873 | 23 | 112.0 |
| observations | ignore | 8 | 0.817 | 0.735 | 0.992 | 1.27 | 0.874 | 23 | 111.0 |
| observations | ignore | 12 | 0.851 | 0.772 | 0.992 | 1.27 | 0.881 | 23 | 111.0 |
| updates | none | 4 | 0.679 | 0.607 | 0.910 | 1.27 | 0.839 | 24 | 124.0 |
| updates | none | 6 | 0.732 | 0.657 | 0.912 | 1.27 | 0.840 | 22 | 112.0 |
| updates | none | 8 | 0.760 | 0.686 | 0.912 | 1.27 | 0.841 | 22 | 111.0 |
| updates | none | 12 | 0.792 | 0.721 | 0.912 | 1.28 | 0.848 | 22 | 112.0 |
| updates | ignore | 4 | 0.679 | 0.607 | 0.910 | 1.27 | 0.839 | 24 | 124.0 |
| updates | ignore | 6 | 0.732 | 0.657 | 0.912 | 1.27 | 0.840 | 22 | 112.0 |
| updates | ignore | 8 | 0.760 | 0.686 | 0.912 | 1.27 | 0.841 | 22 | 111.0 |
| updates | ignore | 12 | 0.792 | 0.721 | 0.912 | 1.28 | 0.848 | 22 | 112.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 5
- identity switches: 23; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 44 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 43 -> 49 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 69 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 67 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 69 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 69 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f279: ref 78971: 45 -> 49 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 79037: 43 -> 45 at (906, 2986), 1 frames after previous cover
- f280: ref 79045: 49 -> 43 at (892.5, 2989.5), 2 frames after previous cover
- f325: ref 79045: 43 -> 44 at (614, 2978), 1 frames after previous cover
- f326: ref 79045: 44 -> 43 at (606, 2977.5), 1 frames after previous cover
- f326: ref 79105: 62 -> 56 at (791.5, 2980.5), 1 frames after previous cover
- f326: ref 79108: 63 -> 62 at (817.5, 2982.5), 1 frames after previous cover
- f330: ref 79103: 56 -> 63 at (753, 2979), 3 frames after previous cover
- f467: ref 79139: 90 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 90 at (399.5, 2892.5), 2 frames after previous cover
- f538: ref 79136: 92 -> 82 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 37 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 41 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (187), 49 (161) |
| 79045 | 355 (84..443) | 351 | 1 | 49 (186), 43 (164), 44 (1) |
| 79037 | 355 (86..445) | 355 | 0 | 43 (189), 45 (161), 44 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 44 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 47 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 51 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 54 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 87 (338), 56 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 56 (198), 63 (152), 55 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 62 (218), 56 (158) |
| 79108 | 385 (104..492) | 383 | 0 | 63 (218), 62 (165) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (367), 67 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 67 (366), 68 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (403), 72 (13), 69 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 72 (396), 69 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 69 (393), 76 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 76 (382), 78 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 78 (397), 81 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 81 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 90 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (390), 82 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/388/1007; tracks with internal gaps: 3; total internal gaps: 4; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 37 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 41 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 43 | 86..443 | 358 | 355 | 353 | 2 | 2 | 1 | 0 | 79037, 79045 |
| 44 | 86..450 | 365 | 349 | 349 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 45 | 88..445 | 358 | 349 | 348 | 1 | 1 | 1 | 0 | 78971, 79037 |
| 47 | 91..455 | 365 | 365 | 365 | 0 | 0 | 0 | 0 | 78899 |
| 49 | 93..439 | 347 | 347 | 347 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 51 | 96..461 | 366 | 364 | 364 | 0 | 0 | 0 | 0 | 79097 |
| 54 | 99..467 | 369 | 358 | 358 | 0 | 0 | 0 | 0 | 79098 |
| 55 | 100..497 | 398 | 396 | 396 | 0 | 0 | 0 | 0 | 79103, 79110 |
| 56 | 101..484 | 384 | 384 | 384 | 0 | 0 | 0 | 0 | 79102, 79103, 79105 |
| 62 | 105..492 | 388 | 383 | 383 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 63 | 106..481 | 376 | 372 | 370 | 2 | 1 | 2 | 0 | 79103, 79108 |
| 67 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 68 | 111..531 | 421 | 421 | 421 | 0 | 0 | 0 | 0 | 79111, 79115 |
| 69 | 113..532 | 420 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116, 79122 |
| 72 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116 |
| 76 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 78 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 81 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 82 | 129..538 | 410 | 406 | 406 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 87 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 90 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 92 | 138..537 | 400 | 390 | 390 | 0 | 0 | 0 | 0 | 79136 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 5
- identity switches: 23; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 44 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 43 -> 49 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 69 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 67 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 69 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 69 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f279: ref 78971: 45 -> 49 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 79037: 43 -> 45 at (906, 2986), 1 frames after previous cover
- f280: ref 79045: 49 -> 43 at (892.5, 2989.5), 2 frames after previous cover
- f325: ref 79045: 43 -> 44 at (614, 2978), 1 frames after previous cover
- f326: ref 79045: 44 -> 43 at (606, 2977.5), 1 frames after previous cover
- f326: ref 79105: 62 -> 56 at (791.5, 2980.5), 1 frames after previous cover
- f326: ref 79108: 63 -> 62 at (817.5, 2982.5), 1 frames after previous cover
- f330: ref 79103: 56 -> 63 at (753, 2979), 3 frames after previous cover
- f467: ref 79139: 90 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 90 at (399.5, 2892.5), 2 frames after previous cover
- f538: ref 79136: 92 -> 82 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 37 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 41 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (187), 49 (161) |
| 79045 | 355 (84..443) | 351 | 1 | 49 (186), 43 (164), 44 (1) |
| 79037 | 355 (86..445) | 355 | 0 | 43 (189), 45 (161), 44 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 44 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 47 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 51 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 54 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 87 (338), 56 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 56 (198), 63 (152), 55 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 62 (218), 56 (158) |
| 79108 | 385 (104..492) | 383 | 0 | 63 (218), 62 (165) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (367), 67 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 67 (366), 68 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (403), 72 (13), 69 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 72 (396), 69 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 69 (393), 76 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 76 (382), 78 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 78 (397), 81 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 81 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 90 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (390), 82 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/388/1007; tracks with internal gaps: 3; total internal gaps: 4; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 37 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 41 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 43 | 86..443 | 358 | 355 | 353 | 2 | 2 | 1 | 0 | 79037, 79045 |
| 44 | 86..450 | 365 | 349 | 349 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 45 | 88..445 | 358 | 349 | 348 | 1 | 1 | 1 | 0 | 78971, 79037 |
| 47 | 91..455 | 365 | 365 | 365 | 0 | 0 | 0 | 0 | 78899 |
| 49 | 93..439 | 347 | 347 | 347 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 51 | 96..461 | 366 | 364 | 364 | 0 | 0 | 0 | 0 | 79097 |
| 54 | 99..467 | 369 | 358 | 358 | 0 | 0 | 0 | 0 | 79098 |
| 55 | 100..497 | 398 | 396 | 396 | 0 | 0 | 0 | 0 | 79103, 79110 |
| 56 | 101..484 | 384 | 384 | 384 | 0 | 0 | 0 | 0 | 79102, 79103, 79105 |
| 62 | 105..492 | 388 | 383 | 383 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 63 | 106..481 | 376 | 372 | 370 | 2 | 1 | 2 | 0 | 79103, 79108 |
| 67 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 68 | 111..531 | 421 | 421 | 421 | 0 | 0 | 0 | 0 | 79111, 79115 |
| 69 | 113..532 | 420 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116, 79122 |
| 72 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116 |
| 76 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 78 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 81 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 82 | 129..538 | 410 | 406 | 406 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 87 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 90 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 92 | 138..537 | 400 | 390 | 390 | 0 | 0 | 0 | 0 | 79136 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 814
- identity switches: 22; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 44 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 43 -> 49 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 69 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 67 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 69 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 69 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f279: ref 78971: 45 -> 49 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 79037: 43 -> 45 at (906, 2986), 1 frames after previous cover
- f280: ref 79045: 49 -> 43 at (892.5, 2989.5), 2 frames after previous cover
- f325: ref 79045: 43 -> 44 at (614, 2978), 1 frames after previous cover
- f326: ref 79045: 44 -> 43 at (606, 2977.5), 1 frames after previous cover
- f326: ref 79105: 62 -> 56 at (791.5, 2980.5), 1 frames after previous cover
- f326: ref 79108: 63 -> 62 at (817.5, 2982.5), 1 frames after previous cover
- f330: ref 79103: 56 -> 63 at (753, 2979), 3 frames after previous cover
- f467: ref 79139: 90 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 90 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 37 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 41 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (187), 49 (161) |
| 79045 | 355 (84..443) | 351 | 1 | 49 (186), 43 (164), 44 (1) |
| 79037 | 355 (86..445) | 355 | 0 | 43 (189), 45 (161), 44 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 44 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 47 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 51 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 54 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 87 (338), 56 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 56 (198), 63 (152), 55 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 62 (218), 56 (158) |
| 79108 | 385 (104..492) | 383 | 0 | 63 (218), 62 (165) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (367), 67 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 67 (366), 68 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (403), 72 (13), 69 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 72 (396), 69 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 69 (393), 76 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 76 (382), 78 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 78 (397), 81 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 81 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 90 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/417/1007; tracks with internal gaps: 19; total internal gaps: 105; longest internal gap: 4; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 37 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 41 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 43 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79037, 79045 |
| 44 | 86..479 | 394 | 394 | 349 | 45 | 16 | 1 | 29 | 78897, 79037, 79045 |
| 45 | 88..474 | 387 | 387 | 348 | 39 | 7 | 2 | 29 | 78971, 79037 |
| 47 | 91..484 | 394 | 394 | 365 | 29 | 0 | 0 | 29 | 78899 |
| 49 | 93..468 | 376 | 376 | 347 | 29 | 0 | 0 | 29 | 78971, 79045 |
| 51 | 96..490 | 395 | 395 | 364 | 31 | 2 | 1 | 29 | 79097 |
| 54 | 99..496 | 398 | 398 | 358 | 40 | 10 | 2 | 29 | 79098 |
| 55 | 100..526 | 427 | 427 | 396 | 31 | 2 | 1 | 29 | 79103, 79110 |
| 56 | 101..513 | 413 | 413 | 384 | 29 | 0 | 0 | 29 | 79102, 79103, 79105 |
| 62 | 105..521 | 417 | 417 | 383 | 34 | 5 | 1 | 29 | 79105, 79108 |
| 63 | 106..510 | 405 | 405 | 370 | 35 | 3 | 4 | 29 | 79103, 79108 |
| 67 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 68 | 111..560 | 450 | 450 | 421 | 29 | 0 | 0 | 29 | 79111, 79115 |
| 69 | 113..561 | 449 | 449 | 409 | 40 | 11 | 1 | 29 | 79115, 79116, 79122 |
| 72 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79115, 79116 |
| 76 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 78 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 81 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 82 | 129..567 | 439 | 439 | 405 | 34 | 4 | 1 | 30 | 79135, 79139 |
| 87 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 90 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 92 | 138..566 | 429 | 429 | 391 | 38 | 9 | 2 | 28 | 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 814
- identity switches: 22; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 44 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 43 -> 49 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 69 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 67 -> 55 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 67 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 69 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 69 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f279: ref 78971: 45 -> 49 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 79037: 43 -> 45 at (906, 2986), 1 frames after previous cover
- f280: ref 79045: 49 -> 43 at (892.5, 2989.5), 2 frames after previous cover
- f325: ref 79045: 43 -> 44 at (614, 2978), 1 frames after previous cover
- f326: ref 79045: 44 -> 43 at (606, 2977.5), 1 frames after previous cover
- f326: ref 79105: 62 -> 56 at (791.5, 2980.5), 1 frames after previous cover
- f326: ref 79108: 63 -> 62 at (817.5, 2982.5), 1 frames after previous cover
- f330: ref 79103: 56 -> 63 at (753, 2979), 3 frames after previous cover
- f467: ref 79139: 90 -> 82 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 82 -> 90 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 37 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 41 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (187), 49 (161) |
| 79045 | 355 (84..443) | 351 | 1 | 49 (186), 43 (164), 44 (1) |
| 79037 | 355 (86..445) | 355 | 0 | 43 (189), 45 (161), 44 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 44 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 47 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 51 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 54 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 87 (338), 56 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 56 (198), 63 (152), 55 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 62 (218), 56 (158) |
| 79108 | 385 (104..492) | 383 | 0 | 63 (218), 62 (165) |
| 79110 | 388 (106..497) | 385 | 0 | 55 (367), 67 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 67 (366), 68 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (403), 72 (13), 69 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 72 (396), 69 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 69 (393), 76 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 76 (382), 78 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 78 (397), 81 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 81 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 82 (334), 90 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (333), 82 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/417/1007; tracks with internal gaps: 19; total internal gaps: 105; longest internal gap: 4; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 37 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 41 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 43 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79037, 79045 |
| 44 | 86..479 | 394 | 394 | 349 | 45 | 16 | 1 | 29 | 78897, 79037, 79045 |
| 45 | 88..474 | 387 | 387 | 348 | 39 | 7 | 2 | 29 | 78971, 79037 |
| 47 | 91..484 | 394 | 394 | 365 | 29 | 0 | 0 | 29 | 78899 |
| 49 | 93..468 | 376 | 376 | 347 | 29 | 0 | 0 | 29 | 78971, 79045 |
| 51 | 96..490 | 395 | 395 | 364 | 31 | 2 | 1 | 29 | 79097 |
| 54 | 99..496 | 398 | 398 | 358 | 40 | 10 | 2 | 29 | 79098 |
| 55 | 100..526 | 427 | 427 | 396 | 31 | 2 | 1 | 29 | 79103, 79110 |
| 56 | 101..513 | 413 | 413 | 384 | 29 | 0 | 0 | 29 | 79102, 79103, 79105 |
| 62 | 105..521 | 417 | 417 | 383 | 34 | 5 | 1 | 29 | 79105, 79108 |
| 63 | 106..510 | 405 | 405 | 370 | 35 | 3 | 4 | 29 | 79103, 79108 |
| 67 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 68 | 111..560 | 450 | 450 | 421 | 29 | 0 | 0 | 29 | 79111, 79115 |
| 69 | 113..561 | 449 | 449 | 409 | 40 | 11 | 1 | 29 | 79115, 79116, 79122 |
| 72 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79115, 79116 |
| 76 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 78 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 81 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 82 | 129..567 | 439 | 439 | 405 | 34 | 4 | 1 | 30 | 79135, 79139 |
| 87 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 90 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 92 | 138..566 | 429 | 429 | 391 | 38 | 9 | 2 | 28 | 79136 |
