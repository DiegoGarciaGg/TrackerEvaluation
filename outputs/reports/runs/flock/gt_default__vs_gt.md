# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=503255dd69b1
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gt_default/tracks.csv sha256=78661ae864bcaab2
  - detections_csv: ground_truth/20251012_164031_1DAC_detections_corrected.csv sha256=503255dd69b114a5
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gt_default
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
| view | region | px | ref | cand | HOTA | DetA | AssA | LocA px | HOTA@a.5 | MOTA | MOTP px | IDSW | Frag | IDF1 | IDP | IDR | Re | Pr | TP | FN | FP | MT | PT | ML |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 10142 | 10091 | 0.961 | 0.991 | 0.932 | 0.01 | 0.963 | 0.993 | 0.01 | 17 | 116.0 | 0.972 | 0.975 | 0.970 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 10091 | 0.962 | 0.992 | 0.933 | 0.01 | 0.963 | 0.993 | 0.01 | 17 | 116.0 | 0.972 | 0.975 | 0.970 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10091 | 0.962 | 0.992 | 0.934 | 0.02 | 0.963 | 0.993 | 0.01 | 17 | 116.0 | 0.973 | 0.975 | 0.971 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10091 | 0.962 | 0.982 | 0.942 | 0.05 | 0.960 | 0.993 | 0.05 | 18 | 115.0 | 0.974 | 0.976 | 0.971 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10091 | 0.961 | 0.991 | 0.932 | 0.01 | 0.963 | 0.993 | 0.01 | 17 | 116.0 | 0.972 | 0.975 | 0.970 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 10091 | 0.962 | 0.992 | 0.933 | 0.01 | 0.963 | 0.993 | 0.01 | 17 | 116.0 | 0.972 | 0.975 | 0.970 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10091 | 0.962 | 0.992 | 0.934 | 0.02 | 0.963 | 0.993 | 0.01 | 17 | 116.0 | 0.973 | 0.975 | 0.971 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10091 | 0.962 | 0.982 | 0.942 | 0.05 | 0.960 | 0.993 | 0.05 | 18 | 115.0 | 0.974 | 0.976 | 0.971 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10906 | 0.891 | 0.918 | 0.866 | 0.01 | 0.893 | 0.913 | 0.01 | 15 | 116.0 | 0.935 | 0.902 | 0.970 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 10906 | 0.892 | 0.918 | 0.867 | 0.01 | 0.893 | 0.913 | 0.01 | 15 | 116.0 | 0.935 | 0.902 | 0.970 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10906 | 0.892 | 0.918 | 0.868 | 0.02 | 0.893 | 0.913 | 0.01 | 15 | 116.0 | 0.936 | 0.903 | 0.971 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10906 | 0.892 | 0.909 | 0.875 | 0.05 | 0.891 | 0.913 | 0.06 | 16 | 116.0 | 0.936 | 0.904 | 0.972 | 0.995 | 0.925 | 10090 | 52 | 816 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10906 | 0.891 | 0.918 | 0.866 | 0.01 | 0.893 | 0.913 | 0.01 | 15 | 116.0 | 0.935 | 0.902 | 0.970 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 10906 | 0.892 | 0.918 | 0.867 | 0.01 | 0.893 | 0.913 | 0.01 | 15 | 116.0 | 0.935 | 0.902 | 0.970 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10906 | 0.892 | 0.918 | 0.868 | 0.02 | 0.893 | 0.913 | 0.01 | 15 | 116.0 | 0.936 | 0.903 | 0.971 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10906 | 0.892 | 0.909 | 0.875 | 0.05 | 0.891 | 0.913 | 0.06 | 16 | 116.0 | 0.936 | 0.904 | 0.972 | 0.995 | 0.925 | 10090 | 52 | 816 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 0
- identity switches: 17; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 3 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 3 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 3 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 3 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 3 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 3 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 19 -> 15 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79136: 25 -> 22 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 22 -> 25 at (399.5, 2892.5), 2 frames after previous cover
- f479: ref 79139: 24 -> 22 at (332.5, 2877.5), 1 frames after previous cover
- f480: ref 79136: 22 -> 24 at (324, 2876.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 4 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 3 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 3 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 3 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 3 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 3 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 3 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 3 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 13 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (384) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 18 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 15 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (382), 20 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (345), 22 (59) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (320), 24 (59), 22 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/390/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..481 | 396 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 4 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 5 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 6 | 91..445 | 355 | 350 | 350 | 0 | 0 | 0 | 0 | 79037 |
| 7 | 93..450 | 358 | 341 | 341 | 0 | 0 | 0 | 0 | 78897 |
| 8 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 9 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 10 | 100..497 | 398 | 395 | 395 | 0 | 0 | 0 | 0 | 79103, 79105, 79110 |
| 11 | 101..467 | 367 | 356 | 356 | 0 | 0 | 0 | 0 | 79098 |
| 12 | 103..484 | 382 | 378 | 378 | 0 | 0 | 0 | 0 | 79102, 79105 |
| 13 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79108 |
| 15 | 110..532 | 423 | 411 | 411 | 0 | 0 | 0 | 0 | 79110, 79122 |
| 16 | 111..500 | 390 | 384 | 384 | 0 | 0 | 0 | 0 | 79111 |
| 17 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115 |
| 18 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79116 |
| 19 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 20 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 21 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 22 | 129..537 | 409 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 23 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 24 | 134..538 | 405 | 404 | 404 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 25 | 138..542 | 405 | 395 | 395 | 0 | 0 | 0 | 0 | 79135, 79136 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 0
- identity switches: 17; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 3 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 3 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 3 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 3 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 3 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 3 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 19 -> 15 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79136: 25 -> 22 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 22 -> 25 at (399.5, 2892.5), 2 frames after previous cover
- f479: ref 79139: 24 -> 22 at (332.5, 2877.5), 1 frames after previous cover
- f480: ref 79136: 22 -> 24 at (324, 2876.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 4 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 3 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 3 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 3 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 3 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 3 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 3 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 3 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 13 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (384) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 18 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 15 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (382), 20 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (345), 22 (59) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (320), 24 (59), 22 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/390/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..481 | 396 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 4 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 5 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 6 | 91..445 | 355 | 350 | 350 | 0 | 0 | 0 | 0 | 79037 |
| 7 | 93..450 | 358 | 341 | 341 | 0 | 0 | 0 | 0 | 78897 |
| 8 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 9 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 10 | 100..497 | 398 | 395 | 395 | 0 | 0 | 0 | 0 | 79103, 79105, 79110 |
| 11 | 101..467 | 367 | 356 | 356 | 0 | 0 | 0 | 0 | 79098 |
| 12 | 103..484 | 382 | 378 | 378 | 0 | 0 | 0 | 0 | 79102, 79105 |
| 13 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79108 |
| 15 | 110..532 | 423 | 411 | 411 | 0 | 0 | 0 | 0 | 79110, 79122 |
| 16 | 111..500 | 390 | 384 | 384 | 0 | 0 | 0 | 0 | 79111 |
| 17 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115 |
| 18 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79116 |
| 19 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 20 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 21 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 22 | 129..537 | 409 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 23 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 24 | 134..538 | 405 | 404 | 404 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 25 | 138..542 | 405 | 395 | 395 | 0 | 0 | 0 | 0 | 79135, 79136 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 815
- identity switches: 15; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 3 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 3 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 3 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 3 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 3 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 3 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 19 -> 15 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79136: 25 -> 22 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 22 -> 25 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 4 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 3 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 3 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 3 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 3 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 3 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 3 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 3 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 13 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (384) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 18 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 15 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (382), 20 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (320), 22 (71) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/419/1007; tracks with internal gaps: 20; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..510 | 425 | 425 | 393 | 32 | 2 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 4 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 5 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 6 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 7 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 8 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 9 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 10 | 100..526 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79103, 79105, 79110 |
| 11 | 101..496 | 396 | 396 | 356 | 40 | 10 | 2 | 29 | 79098 |
| 12 | 103..513 | 411 | 411 | 378 | 33 | 4 | 1 | 29 | 79102, 79105 |
| 13 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79108 |
| 15 | 110..561 | 452 | 452 | 411 | 41 | 12 | 1 | 29 | 79110, 79122 |
| 16 | 111..529 | 419 | 419 | 384 | 35 | 5 | 2 | 29 | 79111 |
| 17 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115 |
| 18 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79116 |
| 19 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 20 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 21 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 22 | 129..566 | 438 | 438 | 405 | 33 | 5 | 1 | 28 | 79135, 79136 |
| 23 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 24 | 134..567 | 434 | 434 | 404 | 30 | 0 | 0 | 30 | 79139 |
| 25 | 138..571 | 434 | 434 | 395 | 39 | 9 | 2 | 29 | 79135, 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10091; unmatched reference entries: 51; unmatched candidate entries: 815
- identity switches: 15; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 3 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 3 -> 7 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 3 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 3 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 10 -> 3 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 3 -> 12 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 10 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 19 -> 15 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 12 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79136: 25 -> 22 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 22 -> 25 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 4 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 6 (350), 3 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 7 (341), 3 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 3 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 3 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 11 (356), 3 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 23 (338), 12 (26), 3 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 3 (378), 10 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 12 (352), 10 (27) |
| 79108 | 385 (104..492) | 383 | 0 | 13 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (384) |
| 79115 | 421 (111..531) | 419 | 0 | 17 (419) |
| 79116 | 411 (114..530) | 409 | 0 | 18 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 15 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (382), 20 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (320), 22 (71) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/419/1007; tracks with internal gaps: 20; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..510 | 425 | 425 | 393 | 32 | 2 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 4 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 5 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 6 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 7 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 8 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 9 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 10 | 100..526 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79103, 79105, 79110 |
| 11 | 101..496 | 396 | 396 | 356 | 40 | 10 | 2 | 29 | 79098 |
| 12 | 103..513 | 411 | 411 | 378 | 33 | 4 | 1 | 29 | 79102, 79105 |
| 13 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79108 |
| 15 | 110..561 | 452 | 452 | 411 | 41 | 12 | 1 | 29 | 79110, 79122 |
| 16 | 111..529 | 419 | 419 | 384 | 35 | 5 | 2 | 29 | 79111 |
| 17 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115 |
| 18 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79116 |
| 19 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 20 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 21 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 22 | 129..566 | 438 | 438 | 405 | 33 | 5 | 1 | 28 | 79135, 79136 |
| 23 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 24 | 134..567 | 434 | 434 | 404 | 30 | 0 | 0 | 30 | 79139 |
| 25 | 138..571 | 434 | 434 | 395 | 39 | 9 | 2 | 29 | 79135, 79136 |
