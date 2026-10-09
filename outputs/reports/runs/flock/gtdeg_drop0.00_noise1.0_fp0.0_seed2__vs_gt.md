# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=2064d3415e94
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise1.0_fp0.0_seed2/tracks.csv sha256=5f49f0fe70a41a8e
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise1.0_fp0.0_seed2.csv sha256=2064d3415e9473fe
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise1.0_fp0.0_seed2
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
| observations | none | 4 | 10142 | 10091 | 0.788 | 0.820 | 0.757 | 1.07 | 0.951 | 0.990 | 1.27 | 26 | 129.0 | 0.965 | 0.967 | 0.962 | 0.994 | 0.999 | 10078 | 64 | 13 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 10091 | 0.850 | 0.884 | 0.817 | 1.16 | 0.954 | 0.993 | 1.27 | 23 | 116.0 | 0.966 | 0.969 | 0.964 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10091 | 0.883 | 0.911 | 0.855 | 1.19 | 0.952 | 0.993 | 1.28 | 23 | 115.0 | 0.967 | 0.969 | 0.964 | 0.995 | 1.000 | 10090 | 52 | 1 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10091 | 0.918 | 0.938 | 0.899 | 1.30 | 0.949 | 0.992 | 1.30 | 26 | 116.0 | 0.967 | 0.970 | 0.965 | 0.995 | 1.000 | 10090 | 52 | 1 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10091 | 0.788 | 0.820 | 0.757 | 1.07 | 0.951 | 0.990 | 1.27 | 26 | 129.0 | 0.965 | 0.967 | 0.962 | 0.994 | 0.999 | 10078 | 64 | 13 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 10091 | 0.850 | 0.884 | 0.817 | 1.16 | 0.954 | 0.993 | 1.27 | 23 | 116.0 | 0.966 | 0.969 | 0.964 | 0.995 | 1.000 | 10091 | 51 | 0 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10091 | 0.883 | 0.911 | 0.855 | 1.19 | 0.952 | 0.993 | 1.28 | 23 | 115.0 | 0.967 | 0.969 | 0.964 | 0.995 | 1.000 | 10090 | 52 | 1 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10091 | 0.918 | 0.938 | 0.899 | 1.30 | 0.949 | 0.992 | 1.30 | 26 | 116.0 | 0.967 | 0.970 | 0.965 | 0.995 | 1.000 | 10090 | 52 | 1 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10906 | 0.732 | 0.760 | 0.705 | 1.07 | 0.882 | 0.910 | 1.27 | 25 | 129.0 | 0.928 | 0.895 | 0.963 | 0.994 | 0.924 | 10078 | 64 | 828 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 10906 | 0.789 | 0.820 | 0.760 | 1.16 | 0.884 | 0.912 | 1.27 | 23 | 116.0 | 0.929 | 0.896 | 0.964 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10906 | 0.819 | 0.844 | 0.795 | 1.20 | 0.883 | 0.913 | 1.28 | 19 | 115.0 | 0.930 | 0.897 | 0.965 | 0.995 | 0.925 | 10090 | 52 | 816 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10906 | 0.853 | 0.869 | 0.837 | 1.30 | 0.881 | 0.912 | 1.29 | 20 | 116.0 | 0.931 | 0.898 | 0.966 | 0.995 | 0.925 | 10090 | 52 | 816 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10906 | 0.732 | 0.760 | 0.705 | 1.07 | 0.882 | 0.910 | 1.27 | 25 | 129.0 | 0.928 | 0.895 | 0.963 | 0.994 | 0.924 | 10078 | 64 | 828 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 10906 | 0.789 | 0.820 | 0.760 | 1.16 | 0.884 | 0.912 | 1.27 | 23 | 116.0 | 0.929 | 0.896 | 0.964 | 0.995 | 0.925 | 10091 | 51 | 815 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10906 | 0.819 | 0.844 | 0.795 | 1.20 | 0.883 | 0.913 | 1.28 | 19 | 115.0 | 0.930 | 0.897 | 0.965 | 0.995 | 0.925 | 10090 | 52 | 816 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10906 | 0.853 | 0.869 | 0.837 | 1.30 | 0.881 | 0.912 | 1.29 | 20 | 116.0 | 0.931 | 0.898 | 0.966 | 0.995 | 0.925 | 10090 | 52 | 816 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 1
- identity switches: 23; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 5 -> 4 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 4 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 5 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 10 -> 11 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 5 -> 12 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 17 -> 18 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 10 -> 5 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 16 -> 15 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 17 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 17 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 5 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f210: ref 79132: 19 -> 17 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 17 -> 19 at (1579, 3004.5), 1 frames after previous cover
- f467: ref 79139: 24 -> 22 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 22 -> 24 at (399.5, 2892.5), 2 frames after previous cover
- f479: ref 79139: 22 -> 25 at (332.5, 2877.5), 1 frames after previous cover
- f480: ref 79136: 25 -> 22 at (324, 2876.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 350 | 0 | 3 (350) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 4 (5) |
| 79037 | 355 (86..445) | 351 | 1 | 4 (350), 5 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 6 (343), 5 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 5 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 5 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 12 (354), 5 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 23 (338), 5 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (377), 10 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 5 (352), 10 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 13 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 15 (366), 16 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 18 (416), 17 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 16 (396), 17 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 17 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (381), 20 (7), 17 (1) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 24 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (333), 25 (59), 22 (12) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (332), 22 (59) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/392/1007; tracks with internal gaps: 1; total internal gaps: 1; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..439 | 354 | 350 | 350 | 0 | 0 | 0 | 0 | 78971 |
| 4 | 86..445 | 360 | 355 | 355 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 5 | 88..484 | 397 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 6 | 91..450 | 360 | 343 | 343 | 0 | 0 | 0 | 0 | 78897 |
| 7 | 93..443 | 351 | 346 | 346 | 0 | 0 | 0 | 0 | 79045 |
| 8 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 9 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 10 | 100..492 | 393 | 388 | 388 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |
| 11 | 101..481 | 381 | 378 | 377 | 1 | 1 | 1 | 0 | 79103 |
| 12 | 103..467 | 365 | 354 | 354 | 0 | 0 | 0 | 0 | 79098 |
| 13 | 106..497 | 392 | 390 | 390 | 0 | 0 | 0 | 0 | 79108, 79110 |
| 15 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 16 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 17 | 113..532 | 420 | 410 | 410 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79132 |
| 18 | 116..531 | 416 | 416 | 416 | 0 | 0 | 0 | 0 | 79115 |
| 19 | 120..515 | 396 | 390 | 390 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 20 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 21 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 22 | 129..538 | 410 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 23 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 24 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 25 | 138..537 | 400 | 391 | 391 | 0 | 0 | 0 | 0 | 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 1
- identity switches: 23; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 5 -> 4 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 4 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 5 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 10 -> 11 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 5 -> 12 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 17 -> 18 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 10 -> 5 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 16 -> 15 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 17 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 17 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 5 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f210: ref 79132: 19 -> 17 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 17 -> 19 at (1579, 3004.5), 1 frames after previous cover
- f467: ref 79139: 24 -> 22 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 22 -> 24 at (399.5, 2892.5), 2 frames after previous cover
- f479: ref 79139: 22 -> 25 at (332.5, 2877.5), 1 frames after previous cover
- f480: ref 79136: 25 -> 22 at (324, 2876.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 350 | 0 | 3 (350) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 4 (5) |
| 79037 | 355 (86..445) | 351 | 1 | 4 (350), 5 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 6 (343), 5 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 5 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 5 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 12 (354), 5 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 23 (338), 5 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (377), 10 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 5 (352), 10 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 13 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 15 (366), 16 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 18 (416), 17 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 16 (396), 17 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 17 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (381), 20 (7), 17 (1) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 24 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (333), 25 (59), 22 (12) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (332), 22 (59) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/392/1007; tracks with internal gaps: 1; total internal gaps: 1; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 3 | 86..439 | 354 | 350 | 350 | 0 | 0 | 0 | 0 | 78971 |
| 4 | 86..445 | 360 | 355 | 355 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 5 | 88..484 | 397 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 6 | 91..450 | 360 | 343 | 343 | 0 | 0 | 0 | 0 | 78897 |
| 7 | 93..443 | 351 | 346 | 346 | 0 | 0 | 0 | 0 | 79045 |
| 8 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 9 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 10 | 100..492 | 393 | 388 | 388 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |
| 11 | 101..481 | 381 | 378 | 377 | 1 | 1 | 1 | 0 | 79103 |
| 12 | 103..467 | 365 | 354 | 354 | 0 | 0 | 0 | 0 | 79098 |
| 13 | 106..497 | 392 | 390 | 390 | 0 | 0 | 0 | 0 | 79108, 79110 |
| 15 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 16 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 17 | 113..532 | 420 | 410 | 410 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79132 |
| 18 | 116..531 | 416 | 416 | 416 | 0 | 0 | 0 | 0 | 79115 |
| 19 | 120..515 | 396 | 390 | 390 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 20 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 21 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134 |
| 22 | 129..538 | 410 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 23 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 24 | 134..542 | 409 | 408 | 408 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 25 | 138..537 | 400 | 391 | 391 | 0 | 0 | 0 | 0 | 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 816
- identity switches: 19; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 5 -> 4 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 4 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 5 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 10 -> 11 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 5 -> 12 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 17 -> 18 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 10 -> 5 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 16 -> 15 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 17 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 17 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 5 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79139: 24 -> 22 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 22 -> 24 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 350 | 0 | 3 (350) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 4 (5) |
| 79037 | 355 (86..445) | 351 | 1 | 4 (350), 5 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 6 (343), 5 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 5 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 5 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 12 (354), 5 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 23 (338), 5 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (377), 10 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 5 (352), 10 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 13 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 15 (366), 16 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 18 (416), 17 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 16 (396), 17 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 17 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (382), 20 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 24 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (333), 22 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/421/1007; tracks with internal gaps: 21; total internal gaps: 110; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..468 | 383 | 383 | 350 | 33 | 4 | 1 | 29 | 78971 |
| 4 | 86..474 | 389 | 389 | 355 | 34 | 3 | 2 | 29 | 79037, 79045 |
| 5 | 88..513 | 426 | 426 | 393 | 33 | 4 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 6 | 91..479 | 389 | 389 | 343 | 46 | 17 | 1 | 29 | 78897 |
| 7 | 93..472 | 380 | 380 | 346 | 34 | 5 | 1 | 29 | 79045 |
| 8 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 9 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 10 | 100..521 | 422 | 422 | 388 | 34 | 5 | 1 | 29 | 79103, 79105, 79108 |
| 11 | 101..510 | 410 | 410 | 377 | 33 | 3 | 2 | 29 | 79103 |
| 12 | 103..496 | 394 | 394 | 354 | 40 | 10 | 2 | 29 | 79098 |
| 13 | 106..526 | 421 | 421 | 390 | 31 | 2 | 1 | 29 | 79108, 79110 |
| 15 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 16 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 17 | 113..561 | 449 | 449 | 409 | 40 | 11 | 1 | 29 | 79115, 79116, 79122 |
| 18 | 116..560 | 445 | 445 | 416 | 29 | 0 | 0 | 29 | 79115 |
| 19 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 20 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 21 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 22 | 129..567 | 439 | 439 | 405 | 34 | 4 | 1 | 30 | 79135, 79139 |
| 23 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 24 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 25 | 138..566 | 429 | 429 | 391 | 38 | 9 | 2 | 28 | 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 816
- identity switches: 19; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 5 -> 4 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 4 -> 7 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 5 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 10 -> 11 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 5 -> 12 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 17 -> 18 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 10 -> 5 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 13 -> 10 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 15 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 16 -> 15 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 17 -> 16 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 17 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 21 -> 20 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 20 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 5 -> 23 at (1952.5, 3031), 4 frames after previous cover
- f467: ref 79139: 24 -> 22 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 22 -> 24 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 1 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 2 (350) |
| 78971 | 352 (84..439) | 350 | 0 | 3 (350) |
| 79045 | 355 (84..443) | 351 | 1 | 7 (346), 4 (5) |
| 79037 | 355 (86..445) | 351 | 1 | 4 (350), 5 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 6 (343), 5 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 8 (360), 5 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 9 (361), 5 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 12 (354), 5 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 23 (338), 5 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 11 (377), 10 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 5 (352), 10 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 10 (360), 13 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 13 (367), 15 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 15 (366), 16 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 18 (416), 17 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 16 (396), 17 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 17 (393), 19 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 19 (382), 20 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 20 (397), 21 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 21 (405) |
| 79135 | 409 (129..542) | 409 | 0 | 22 (334), 24 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 24 (333), 22 (71) |
| 79136 | 393 (136..538) | 391 | 0 | 25 (391) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/421/1007; tracks with internal gaps: 21; total internal gaps: 110; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 3 | 86..468 | 383 | 383 | 350 | 33 | 4 | 1 | 29 | 78971 |
| 4 | 86..474 | 389 | 389 | 355 | 34 | 3 | 2 | 29 | 79037, 79045 |
| 5 | 88..513 | 426 | 426 | 393 | 33 | 4 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 6 | 91..479 | 389 | 389 | 343 | 46 | 17 | 1 | 29 | 78897 |
| 7 | 93..472 | 380 | 380 | 346 | 34 | 5 | 1 | 29 | 79045 |
| 8 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 9 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 10 | 100..521 | 422 | 422 | 388 | 34 | 5 | 1 | 29 | 79103, 79105, 79108 |
| 11 | 101..510 | 410 | 410 | 377 | 33 | 3 | 2 | 29 | 79103 |
| 12 | 103..496 | 394 | 394 | 354 | 40 | 10 | 2 | 29 | 79098 |
| 13 | 106..526 | 421 | 421 | 390 | 31 | 2 | 1 | 29 | 79108, 79110 |
| 15 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 16 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 17 | 113..561 | 449 | 449 | 409 | 40 | 11 | 1 | 29 | 79115, 79116, 79122 |
| 18 | 116..560 | 445 | 445 | 416 | 29 | 0 | 0 | 29 | 79115 |
| 19 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 20 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 21 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134 |
| 22 | 129..567 | 439 | 439 | 405 | 34 | 4 | 1 | 30 | 79135, 79139 |
| 23 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 24 | 134..571 | 438 | 438 | 408 | 30 | 1 | 1 | 29 | 79135, 79139 |
| 25 | 138..566 | 429 | 429 | 391 | 38 | 9 | 2 | 28 | 79136 |
