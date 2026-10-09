# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=5aea4c67a497
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise1.0_fp0.0_seed3/tracks.csv sha256=bae70a70eb67b66c
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise1.0_fp0.0_seed3.csv sha256=5aea4c67a497d96a
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise1.0_fp0.0_seed3
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
| observations | none | 4 | 10142 | 10090 | 0.789 | 0.819 | 0.761 | 1.07 | 0.953 | 0.990 | 1.27 | 20 | 126.0 | 0.966 | 0.969 | 0.964 | 0.993 | 0.999 | 10075 | 67 | 15 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 10090 | 0.851 | 0.877 | 0.825 | 1.16 | 0.954 | 0.993 | 1.27 | 15 | 112.0 | 0.968 | 0.971 | 0.966 | 0.995 | 1.000 | 10089 | 53 | 1 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10090 | 0.885 | 0.908 | 0.863 | 1.21 | 0.952 | 0.993 | 1.27 | 15 | 111.0 | 0.969 | 0.971 | 0.966 | 0.995 | 1.000 | 10090 | 52 | 0 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10090 | 0.923 | 0.939 | 0.906 | 1.31 | 0.958 | 0.993 | 1.27 | 15 | 111.0 | 0.972 | 0.975 | 0.970 | 0.995 | 1.000 | 10090 | 52 | 0 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10090 | 0.789 | 0.819 | 0.761 | 1.07 | 0.953 | 0.990 | 1.27 | 20 | 126.0 | 0.966 | 0.969 | 0.964 | 0.993 | 0.999 | 10075 | 67 | 15 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 10090 | 0.851 | 0.877 | 0.825 | 1.16 | 0.954 | 0.993 | 1.27 | 15 | 112.0 | 0.968 | 0.971 | 0.966 | 0.995 | 1.000 | 10089 | 53 | 1 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10090 | 0.885 | 0.908 | 0.863 | 1.21 | 0.952 | 0.993 | 1.27 | 15 | 111.0 | 0.969 | 0.971 | 0.966 | 0.995 | 1.000 | 10090 | 52 | 0 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10090 | 0.923 | 0.939 | 0.906 | 1.31 | 0.958 | 0.993 | 1.27 | 15 | 111.0 | 0.972 | 0.975 | 0.970 | 0.995 | 1.000 | 10090 | 52 | 0 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10904 | 0.733 | 0.760 | 0.708 | 1.07 | 0.884 | 0.910 | 1.27 | 16 | 124.0 | 0.929 | 0.897 | 0.964 | 0.994 | 0.924 | 10077 | 65 | 827 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 10904 | 0.790 | 0.813 | 0.768 | 1.16 | 0.884 | 0.913 | 1.27 | 14 | 112.0 | 0.931 | 0.898 | 0.966 | 0.995 | 0.925 | 10089 | 53 | 815 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10904 | 0.822 | 0.841 | 0.802 | 1.21 | 0.883 | 0.913 | 1.27 | 14 | 111.0 | 0.931 | 0.899 | 0.966 | 0.995 | 0.925 | 10090 | 52 | 814 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10904 | 0.856 | 0.871 | 0.842 | 1.32 | 0.888 | 0.913 | 1.28 | 14 | 112.0 | 0.935 | 0.902 | 0.970 | 0.995 | 0.925 | 10087 | 55 | 817 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10904 | 0.733 | 0.760 | 0.708 | 1.07 | 0.884 | 0.910 | 1.27 | 16 | 124.0 | 0.929 | 0.897 | 0.964 | 0.994 | 0.924 | 10077 | 65 | 827 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 10904 | 0.790 | 0.813 | 0.768 | 1.16 | 0.884 | 0.913 | 1.27 | 14 | 112.0 | 0.931 | 0.898 | 0.966 | 0.995 | 0.925 | 10089 | 53 | 815 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10904 | 0.822 | 0.841 | 0.802 | 1.21 | 0.883 | 0.913 | 1.27 | 14 | 111.0 | 0.931 | 0.899 | 0.966 | 0.995 | 0.925 | 10090 | 52 | 814 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10904 | 0.856 | 0.871 | 0.842 | 1.32 | 0.888 | 0.913 | 1.28 | 14 | 112.0 | 0.935 | 0.902 | 0.970 | 0.995 | 0.925 | 10087 | 55 | 817 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 0
- identity switches: 15; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 3 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 18 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 16 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 16 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 18 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79139: 25 -> 23 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 23 -> 25 at (399.5, 2892.5), 2 frames after previous cover
- f538: ref 79136: 26 -> 23 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 3 (5) |
| 79037 | 355 (86..445) | 355 | 0 | 3 (350), 4 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 4 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 6 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 8 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 9 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 24 (338), 11 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (350), 10 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 13 (376) |
| 79108 | 385 (104..492) | 383 | 0 | 14 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 16 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (366), 17 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 17 (403), 19 (13), 18 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 19 (396), 18 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 20 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (382), 21 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 21 (397), 22 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 22 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 23 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 25 (333), 23 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 26 (390), 23 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/387/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..445 | 360 | 355 | 355 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 4 | 86..450 | 365 | 348 | 348 | 0 | 0 | 0 | 0 | 78897, 79037 |
| 5 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 6 | 91..455 | 365 | 365 | 365 | 0 | 0 | 0 | 0 | 78899 |
| 7 | 93..443 | 351 | 346 | 346 | 0 | 0 | 0 | 0 | 79045 |
| 8 | 96..461 | 366 | 364 | 364 | 0 | 0 | 0 | 0 | 79097 |
| 9 | 99..467 | 369 | 358 | 358 | 0 | 0 | 0 | 0 | 79098 |
| 10 | 100..497 | 398 | 396 | 396 | 0 | 0 | 0 | 0 | 79103, 79110 |
| 11 | 101..481 | 381 | 378 | 378 | 0 | 0 | 0 | 0 | 79102, 79103 |
| 13 | 105..484 | 380 | 376 | 376 | 0 | 0 | 0 | 0 | 79105 |
| 14 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79108 |
| 16 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 17 | 111..531 | 421 | 421 | 421 | 0 | 0 | 0 | 0 | 79111, 79115 |
| 18 | 113..532 | 420 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116, 79122 |
| 19 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116 |
| 20 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 21 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 22 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 23 | 129..538 | 410 | 406 | 406 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 24 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 25 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 26 | 138..537 | 400 | 390 | 390 | 0 | 0 | 0 | 0 | 79136 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 0
- identity switches: 15; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 3 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 18 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 16 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 16 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 18 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79139: 25 -> 23 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 23 -> 25 at (399.5, 2892.5), 2 frames after previous cover
- f538: ref 79136: 26 -> 23 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 3 (5) |
| 79037 | 355 (86..445) | 355 | 0 | 3 (350), 4 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 4 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 6 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 8 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 9 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 24 (338), 11 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (350), 10 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 13 (376) |
| 79108 | 385 (104..492) | 383 | 0 | 14 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 16 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (366), 17 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 17 (403), 19 (13), 18 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 19 (396), 18 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 20 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (382), 21 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 21 (397), 22 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 22 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 23 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 25 (333), 23 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 26 (390), 23 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/387/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..445 | 360 | 355 | 355 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 4 | 86..450 | 365 | 348 | 348 | 0 | 0 | 0 | 0 | 78897, 79037 |
| 5 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 6 | 91..455 | 365 | 365 | 365 | 0 | 0 | 0 | 0 | 78899 |
| 7 | 93..443 | 351 | 346 | 346 | 0 | 0 | 0 | 0 | 79045 |
| 8 | 96..461 | 366 | 364 | 364 | 0 | 0 | 0 | 0 | 79097 |
| 9 | 99..467 | 369 | 358 | 358 | 0 | 0 | 0 | 0 | 79098 |
| 10 | 100..497 | 398 | 396 | 396 | 0 | 0 | 0 | 0 | 79103, 79110 |
| 11 | 101..481 | 381 | 378 | 378 | 0 | 0 | 0 | 0 | 79102, 79103 |
| 13 | 105..484 | 380 | 376 | 376 | 0 | 0 | 0 | 0 | 79105 |
| 14 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79108 |
| 16 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 17 | 111..531 | 421 | 421 | 421 | 0 | 0 | 0 | 0 | 79111, 79115 |
| 18 | 113..532 | 420 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116, 79122 |
| 19 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79115, 79116 |
| 20 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 21 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 22 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 23 | 129..538 | 410 | 406 | 406 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 24 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 25 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 26 | 138..537 | 400 | 390 | 390 | 0 | 0 | 0 | 0 | 79136 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 814
- identity switches: 14; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 3 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 18 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 16 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 16 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 18 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79139: 25 -> 23 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 23 -> 25 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 3 (5) |
| 79037 | 355 (86..445) | 355 | 0 | 3 (350), 4 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 4 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 6 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 8 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 9 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 24 (338), 11 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (350), 10 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 13 (376) |
| 79108 | 385 (104..492) | 383 | 0 | 14 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 16 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (366), 17 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 17 (403), 19 (13), 18 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 19 (396), 18 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 20 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (382), 21 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 21 (397), 22 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 22 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 23 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 25 (333), 23 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 26 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/416/1007; tracks with internal gaps: 21; total internal gaps: 108; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..474 | 389 | 389 | 355 | 34 | 3 | 2 | 29 | 79037, 79045 |
| 4 | 86..479 | 394 | 394 | 348 | 46 | 17 | 1 | 29 | 78897, 79037 |
| 5 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 6 | 91..484 | 394 | 394 | 365 | 29 | 0 | 0 | 29 | 78899 |
| 7 | 93..472 | 380 | 380 | 346 | 34 | 5 | 1 | 29 | 79045 |
| 8 | 96..490 | 395 | 395 | 364 | 31 | 2 | 1 | 29 | 79097 |
| 9 | 99..496 | 398 | 398 | 358 | 40 | 10 | 2 | 29 | 79098 |
| 10 | 100..526 | 427 | 427 | 396 | 31 | 2 | 1 | 29 | 79103, 79110 |
| 11 | 101..510 | 410 | 410 | 378 | 32 | 2 | 2 | 29 | 79102, 79103 |
| 13 | 105..513 | 409 | 409 | 376 | 33 | 4 | 1 | 29 | 79105 |
| 14 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79108 |
| 16 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 17 | 111..560 | 450 | 450 | 421 | 29 | 0 | 0 | 29 | 79111, 79115 |
| 18 | 113..561 | 449 | 449 | 409 | 40 | 11 | 1 | 29 | 79115, 79116, 79122 |
| 19 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79115, 79116 |
| 20 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 21 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 22 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 23 | 129..567 | 439 | 439 | 405 | 34 | 4 | 1 | 30 | 79135, 79139 |
| 24 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 25 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 26 | 138..566 | 429 | 429 | 391 | 38 | 9 | 2 | 28 | 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 814
- identity switches: 14; fragmentation (coverage interruptions): 3; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 3 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 3 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f116: ref 79115: 18 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79110: 16 -> 10 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 16 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 18 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 18 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79139: 25 -> 23 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 23 -> 25 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 5 (348) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 3 (5) |
| 79037 | 355 (86..445) | 355 | 0 | 3 (350), 4 (5) |
| 78897 | 345 (89..450) | 343 | 0 | 4 (343) |
| 78899 | 365 (91..455) | 365 | 0 | 6 (365) |
| 79097 | 366 (94..461) | 364 | 0 | 8 (364) |
| 79098 | 360 (97..467) | 358 | 0 | 9 (358) |
| 79102 | 371 (98..477) | 366 | 1 | 24 (338), 11 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (350), 10 (29) |
| 79105 | 379 (101..484) | 376 | 0 | 13 (376) |
| 79108 | 385 (104..492) | 383 | 0 | 14 (383) |
| 79110 | 388 (106..497) | 385 | 0 | 10 (367), 16 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 16 (366), 17 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 17 (403), 19 (13), 18 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 19 (396), 18 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 18 (393), 20 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 20 (382), 21 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 21 (397), 22 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 22 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 23 (334), 25 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 25 (333), 23 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 26 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/416/1007; tracks with internal gaps: 21; total internal gaps: 108; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..474 | 389 | 389 | 355 | 34 | 3 | 2 | 29 | 79037, 79045 |
| 4 | 86..479 | 394 | 394 | 348 | 46 | 17 | 1 | 29 | 78897, 79037 |
| 5 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 6 | 91..484 | 394 | 394 | 365 | 29 | 0 | 0 | 29 | 78899 |
| 7 | 93..472 | 380 | 380 | 346 | 34 | 5 | 1 | 29 | 79045 |
| 8 | 96..490 | 395 | 395 | 364 | 31 | 2 | 1 | 29 | 79097 |
| 9 | 99..496 | 398 | 398 | 358 | 40 | 10 | 2 | 29 | 79098 |
| 10 | 100..526 | 427 | 427 | 396 | 31 | 2 | 1 | 29 | 79103, 79110 |
| 11 | 101..510 | 410 | 410 | 378 | 32 | 2 | 2 | 29 | 79102, 79103 |
| 13 | 105..513 | 409 | 409 | 376 | 33 | 4 | 1 | 29 | 79105 |
| 14 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79108 |
| 16 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 17 | 111..560 | 450 | 450 | 421 | 29 | 0 | 0 | 29 | 79111, 79115 |
| 18 | 113..561 | 449 | 449 | 409 | 40 | 11 | 1 | 29 | 79115, 79116, 79122 |
| 19 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79115, 79116 |
| 20 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 21 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 22 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 23 | 129..567 | 439 | 439 | 405 | 34 | 4 | 1 | 30 | 79135, 79139 |
| 24 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 25 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 26 | 138..566 | 429 | 429 | 391 | 38 | 9 | 2 | 28 | 79136 |
