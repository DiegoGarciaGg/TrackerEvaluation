# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=2a1fb412c012
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise0.0_fp0.5_seed3/tracks.csv sha256=c406aeeb9b7fee4f
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise0.0_fp0.5_seed3.csv sha256=2a1fb412c012b3c4
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise0.0_fp0.5_seed3
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
| observations | none | 4 | 10142 | 10109 | 0.896 | 0.990 | 0.811 | 0.01 | 0.897 | 0.990 | 0.01 | 33 | 117.0 | 0.889 | 0.891 | 0.888 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 10109 | 0.897 | 0.990 | 0.812 | 0.01 | 0.897 | 0.990 | 0.01 | 29 | 117.0 | 0.889 | 0.891 | 0.888 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10109 | 0.894 | 0.961 | 0.831 | 0.08 | 0.886 | 0.990 | 0.01 | 29 | 117.0 | 0.890 | 0.891 | 0.889 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10109 | 0.901 | 0.963 | 0.844 | 0.18 | 0.902 | 0.990 | 0.07 | 28 | 116.0 | 0.904 | 0.905 | 0.902 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10109 | 0.896 | 0.990 | 0.811 | 0.01 | 0.897 | 0.990 | 0.01 | 33 | 117.0 | 0.889 | 0.891 | 0.888 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 10109 | 0.897 | 0.990 | 0.812 | 0.01 | 0.897 | 0.990 | 0.01 | 29 | 117.0 | 0.889 | 0.891 | 0.888 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10109 | 0.894 | 0.961 | 0.831 | 0.08 | 0.886 | 0.990 | 0.01 | 29 | 117.0 | 0.890 | 0.891 | 0.889 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10109 | 0.901 | 0.963 | 0.844 | 0.18 | 0.902 | 0.990 | 0.07 | 28 | 116.0 | 0.904 | 0.905 | 0.902 | 0.995 | 0.998 | 10090 | 52 | 19 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 11116 | 0.822 | 0.900 | 0.750 | 0.01 | 0.823 | 0.891 | 0.01 | 30 | 117.0 | 0.847 | 0.810 | 0.888 | 0.995 | 0.908 | 10090 | 52 | 1026 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 11116 | 0.822 | 0.900 | 0.751 | 0.01 | 0.823 | 0.891 | 0.01 | 28 | 117.0 | 0.847 | 0.810 | 0.888 | 0.995 | 0.908 | 10090 | 52 | 1026 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 11116 | 0.820 | 0.875 | 0.768 | 0.09 | 0.814 | 0.891 | 0.01 | 28 | 117.0 | 0.848 | 0.811 | 0.889 | 0.995 | 0.908 | 10090 | 52 | 1026 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 11116 | 0.827 | 0.877 | 0.780 | 0.18 | 0.828 | 0.891 | 0.08 | 27 | 117.0 | 0.861 | 0.824 | 0.903 | 0.995 | 0.908 | 10089 | 53 | 1027 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 11116 | 0.822 | 0.900 | 0.750 | 0.01 | 0.823 | 0.891 | 0.01 | 30 | 117.0 | 0.847 | 0.810 | 0.888 | 0.995 | 0.908 | 10090 | 52 | 1026 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 11116 | 0.822 | 0.900 | 0.751 | 0.01 | 0.823 | 0.891 | 0.01 | 28 | 117.0 | 0.847 | 0.810 | 0.888 | 0.995 | 0.908 | 10090 | 52 | 1026 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 11116 | 0.820 | 0.875 | 0.768 | 0.09 | 0.814 | 0.891 | 0.01 | 28 | 117.0 | 0.848 | 0.811 | 0.889 | 0.995 | 0.908 | 10090 | 52 | 1026 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 11116 | 0.827 | 0.877 | 0.780 | 0.18 | 0.828 | 0.891 | 0.08 | 27 | 117.0 | 0.861 | 0.824 | 0.903 | 0.995 | 0.908 | 10089 | 53 | 1027 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 19
- identity switches: 29; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 40 -> 44 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 40 -> 45 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 40 -> 48 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 40 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 40 -> 55 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 40 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 40 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 73 -> 63 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 80 -> 75 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 75 -> 73 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f227: ref 79105: 58 -> 87 at (1392, 2996), 1 frames after previous cover
- f227: ref 79111: 64 -> 58 at (1450, 3001.5), 1 frames after previous cover
- f227: ref 79115: 67 -> 64 at (1458.5, 3002), 1 frames after previous cover
- f227: ref 79122: 63 -> 67 at (1475.5, 3007), 1 frames after previous cover
- f228: ref 79102: 87 -> 40 at (1356, 2997.5), 2 frames after previous cover
- f228: ref 79103: 40 -> 87 at (1365.5, 2995), 1 frames after previous cover
- f228: ref 79105: 87 -> 59 at (1385, 2995.5), 1 frames after previous cover
- f228: ref 79108: 59 -> 58 at (1416, 2999.5), 1 frames after previous cover
- f228: ref 79111: 58 -> 64 at (1444.5, 3000.5), 1 frames after previous cover
- f228: ref 79115: 64 -> 67 at (1453, 3002), 1 frames after previous cover
- f228: ref 79122: 67 -> 63 at (1469, 3006), 1 frames after previous cover
- f335: ref 79134: 80 -> 63 at (898.5, 2961.5), 1 frames after previous cover
- f336: ref 79122: 63 -> 178 at (832, 2983), 2 frames after previous cover
- f467: ref 79136: 92 -> 84 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 84 -> 92 at (399.5, 2892.5), 2 frames after previous cover
- f538: ref 79136: 84 -> 90 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 37 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 42 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 39 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 44 (350), 40 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 45 (341), 40 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 48 (360), 40 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (361), 40 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 55 (356), 40 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 40 (247), 87 (93), 58 (26) |
| 79103 | 380 (99..481) | 379 | 0 | 87 (251), 40 (127), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 59 (254), 58 (97), 54 (27), 87 (1) |
| 79108 | 385 (104..492) | 383 | 0 | 58 (262), 59 (121) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 64 (383), 58 (1) |
| 79115 | 421 (111..531) | 419 | 0 | 67 (418), 64 (1) |
| 79116 | 411 (114..530) | 409 | 0 | 69 (409) |
| 79122 | 404 (118..532) | 401 | 1 | 63 (197), 178 (194), 73 (9), 67 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 73 (382), 75 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 75 (397), 80 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 80 (206), 63 (199) |
| 79135 | 409 (129..542) | 409 | 0 | 84 (334), 92 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (320), 84 (70), 90 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 246 | 490..502 | 13 | 0 | 2 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 13/388/1007; tracks with internal gaps: 3; total internal gaps: 3; longest internal gap: 1; tracks ending in coasting: 5 (trailing rows total 16)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 37 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 39 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 40 | 86..477 | 392 | 387 | 387 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 42 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 44 | 91..445 | 355 | 350 | 350 | 0 | 0 | 0 | 0 | 79037 |
| 45 | 93..450 | 358 | 342 | 341 | 1 | 1 | 1 | 0 | 78897 |
| 48 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 53 | 99..481 | 383 | 364 | 361 | 3 | 0 | 0 | 3 | 79097 |
| 54 | 100..497 | 398 | 395 | 395 | 0 | 0 | 0 | 0 | 79103, 79105, 79110 |
| 55 | 101..488 | 388 | 358 | 356 | 2 | 0 | 0 | 2 | 79098 |
| 58 | 103..492 | 390 | 386 | 386 | 0 | 0 | 0 | 0 | 79102, 79105, 79108, 79111 |
| 59 | 106..484 | 379 | 375 | 375 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 63 | 110..533 | 424 | 415 | 414 | 1 | 1 | 1 | 0 | 79110, 79122, 79134 |
| 64 | 111..500 | 390 | 384 | 384 | 0 | 0 | 0 | 0 | 79111, 79115 |
| 67 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115, 79122 |
| 69 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79116 |
| 73 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 75 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 80 | 126..335 | 210 | 210 | 209 | 1 | 0 | 0 | 1 | 79128, 79134 |
| 84 | 129..537 | 409 | 404 | 404 | 0 | 0 | 0 | 0 | 79135, 79136 |
| 87 | 132..481 | 350 | 345 | 345 | 0 | 0 | 0 | 0 | 79102, 79103, 79105 |
| 90 | 134..538 | 405 | 405 | 405 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 92 | 138..640 | 503 | 403 | 395 | 8 | 0 | 0 | 8 | 79135, 79136 |
| 178 | 336..532 | 197 | 195 | 194 | 1 | 1 | 1 | 0 | 79122 |
| 246 | 490..502 | 13 | 2 | 0 | 2 | 0 | 0 | 2 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 19
- identity switches: 29; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 40 -> 44 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 40 -> 45 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 40 -> 48 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 40 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 40 -> 55 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 40 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 40 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 73 -> 63 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 80 -> 75 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 75 -> 73 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f227: ref 79105: 58 -> 87 at (1392, 2996), 1 frames after previous cover
- f227: ref 79111: 64 -> 58 at (1450, 3001.5), 1 frames after previous cover
- f227: ref 79115: 67 -> 64 at (1458.5, 3002), 1 frames after previous cover
- f227: ref 79122: 63 -> 67 at (1475.5, 3007), 1 frames after previous cover
- f228: ref 79102: 87 -> 40 at (1356, 2997.5), 2 frames after previous cover
- f228: ref 79103: 40 -> 87 at (1365.5, 2995), 1 frames after previous cover
- f228: ref 79105: 87 -> 59 at (1385, 2995.5), 1 frames after previous cover
- f228: ref 79108: 59 -> 58 at (1416, 2999.5), 1 frames after previous cover
- f228: ref 79111: 58 -> 64 at (1444.5, 3000.5), 1 frames after previous cover
- f228: ref 79115: 64 -> 67 at (1453, 3002), 1 frames after previous cover
- f228: ref 79122: 67 -> 63 at (1469, 3006), 1 frames after previous cover
- f335: ref 79134: 80 -> 63 at (898.5, 2961.5), 1 frames after previous cover
- f336: ref 79122: 63 -> 178 at (832, 2983), 2 frames after previous cover
- f467: ref 79136: 92 -> 84 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 84 -> 92 at (399.5, 2892.5), 2 frames after previous cover
- f538: ref 79136: 84 -> 90 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 37 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 42 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 39 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 44 (350), 40 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 45 (341), 40 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 48 (360), 40 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (361), 40 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 55 (356), 40 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 40 (247), 87 (93), 58 (26) |
| 79103 | 380 (99..481) | 379 | 0 | 87 (251), 40 (127), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 59 (254), 58 (97), 54 (27), 87 (1) |
| 79108 | 385 (104..492) | 383 | 0 | 58 (262), 59 (121) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 64 (383), 58 (1) |
| 79115 | 421 (111..531) | 419 | 0 | 67 (418), 64 (1) |
| 79116 | 411 (114..530) | 409 | 0 | 69 (409) |
| 79122 | 404 (118..532) | 401 | 1 | 63 (197), 178 (194), 73 (9), 67 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 73 (382), 75 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 75 (397), 80 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 80 (206), 63 (199) |
| 79135 | 409 (129..542) | 409 | 0 | 84 (334), 92 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (320), 84 (70), 90 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 246 | 490..502 | 13 | 0 | 2 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 13/388/1007; tracks with internal gaps: 3; total internal gaps: 3; longest internal gap: 1; tracks ending in coasting: 5 (trailing rows total 16)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..429 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78896 |
| 37 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78969 |
| 39 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 40 | 86..477 | 392 | 387 | 387 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 42 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 44 | 91..445 | 355 | 350 | 350 | 0 | 0 | 0 | 0 | 79037 |
| 45 | 93..450 | 358 | 342 | 341 | 1 | 1 | 1 | 0 | 78897 |
| 48 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 53 | 99..481 | 383 | 364 | 361 | 3 | 0 | 0 | 3 | 79097 |
| 54 | 100..497 | 398 | 395 | 395 | 0 | 0 | 0 | 0 | 79103, 79105, 79110 |
| 55 | 101..488 | 388 | 358 | 356 | 2 | 0 | 0 | 2 | 79098 |
| 58 | 103..492 | 390 | 386 | 386 | 0 | 0 | 0 | 0 | 79102, 79105, 79108, 79111 |
| 59 | 106..484 | 379 | 375 | 375 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 63 | 110..533 | 424 | 415 | 414 | 1 | 1 | 1 | 0 | 79110, 79122, 79134 |
| 64 | 111..500 | 390 | 384 | 384 | 0 | 0 | 0 | 0 | 79111, 79115 |
| 67 | 113..531 | 419 | 419 | 419 | 0 | 0 | 0 | 0 | 79115, 79122 |
| 69 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79116 |
| 73 | 120..515 | 396 | 391 | 391 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 75 | 122..527 | 406 | 404 | 404 | 0 | 0 | 0 | 0 | 79128, 79132 |
| 80 | 126..335 | 210 | 210 | 209 | 1 | 0 | 0 | 1 | 79128, 79134 |
| 84 | 129..537 | 409 | 404 | 404 | 0 | 0 | 0 | 0 | 79135, 79136 |
| 87 | 132..481 | 350 | 345 | 345 | 0 | 0 | 0 | 0 | 79102, 79103, 79105 |
| 90 | 134..538 | 405 | 405 | 405 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 92 | 138..640 | 503 | 403 | 395 | 8 | 0 | 0 | 8 | 79135, 79136 |
| 178 | 336..532 | 197 | 195 | 194 | 1 | 1 | 1 | 0 | 79122 |
| 246 | 490..502 | 13 | 2 | 0 | 2 | 0 | 0 | 2 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 1026
- identity switches: 28; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 40 -> 44 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 40 -> 45 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 40 -> 48 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 40 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 40 -> 55 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 40 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 40 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 73 -> 63 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 80 -> 75 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 75 -> 73 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f227: ref 79105: 58 -> 87 at (1392, 2996), 1 frames after previous cover
- f227: ref 79111: 64 -> 58 at (1450, 3001.5), 1 frames after previous cover
- f227: ref 79115: 67 -> 64 at (1458.5, 3002), 1 frames after previous cover
- f227: ref 79122: 63 -> 67 at (1475.5, 3007), 1 frames after previous cover
- f228: ref 79102: 87 -> 40 at (1356, 2997.5), 2 frames after previous cover
- f228: ref 79103: 40 -> 87 at (1365.5, 2995), 1 frames after previous cover
- f228: ref 79105: 87 -> 59 at (1385, 2995.5), 1 frames after previous cover
- f228: ref 79108: 59 -> 58 at (1416, 2999.5), 1 frames after previous cover
- f228: ref 79111: 58 -> 64 at (1444.5, 3000.5), 1 frames after previous cover
- f228: ref 79115: 64 -> 67 at (1453, 3002), 1 frames after previous cover
- f228: ref 79122: 67 -> 63 at (1469, 3006), 1 frames after previous cover
- f335: ref 79134: 80 -> 63 at (898.5, 2961.5), 1 frames after previous cover
- f336: ref 79122: 63 -> 178 at (832, 2983), 2 frames after previous cover
- f467: ref 79136: 92 -> 84 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 84 -> 92 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 37 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 42 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 39 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 44 (350), 40 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 45 (341), 40 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 48 (360), 40 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (361), 40 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 55 (356), 40 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 40 (247), 87 (93), 58 (26) |
| 79103 | 380 (99..481) | 379 | 0 | 87 (251), 40 (127), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 59 (254), 58 (97), 54 (27), 87 (1) |
| 79108 | 385 (104..492) | 383 | 0 | 58 (262), 59 (121) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 64 (383), 58 (1) |
| 79115 | 421 (111..531) | 419 | 0 | 67 (418), 64 (1) |
| 79116 | 411 (114..530) | 409 | 0 | 69 (409) |
| 79122 | 404 (118..532) | 401 | 1 | 63 (197), 178 (194), 73 (9), 67 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 73 (382), 75 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 75 (397), 80 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 80 (206), 63 (199) |
| 79135 | 409 (129..542) | 409 | 0 | 84 (334), 92 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (320), 84 (71) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 246 | 490..531 | 42 | 0 | 42 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 42/417/1007; tracks with internal gaps: 21; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 26 (trailing rows total 907)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 37 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 39 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 40 | 86..506 | 421 | 421 | 387 | 34 | 5 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 42 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 44 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 45 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 48 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 53 | 99..510 | 412 | 412 | 361 | 51 | 2 | 1 | 49 | 79097 |
| 54 | 100..526 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79103, 79105, 79110 |
| 55 | 101..517 | 417 | 417 | 356 | 61 | 10 | 2 | 50 | 79098 |
| 58 | 103..521 | 419 | 419 | 386 | 33 | 4 | 1 | 29 | 79102, 79105, 79108, 79111 |
| 59 | 106..513 | 408 | 408 | 375 | 33 | 4 | 1 | 29 | 79105, 79108 |
| 63 | 110..562 | 453 | 453 | 414 | 39 | 10 | 1 | 29 | 79110, 79122, 79134 |
| 64 | 111..529 | 419 | 419 | 384 | 35 | 5 | 2 | 29 | 79111, 79115 |
| 67 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115, 79122 |
| 69 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79116 |
| 73 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 75 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 80 | 126..364 | 239 | 239 | 209 | 30 | 0 | 0 | 30 | 79128, 79134 |
| 84 | 129..566 | 438 | 438 | 405 | 33 | 5 | 1 | 28 | 79135, 79136 |
| 87 | 132..510 | 379 | 379 | 345 | 34 | 4 | 2 | 29 | 79102, 79103, 79105 |
| 90 | 134..567 | 434 | 434 | 404 | 30 | 0 | 0 | 30 | 79139 |
| 92 | 138..669 | 532 | 532 | 395 | 137 | 9 | 2 | 127 | 79135, 79136 |
| 178 | 336..561 | 226 | 226 | 194 | 32 | 3 | 1 | 29 | 79122 |
| 246 | 490..531 | 42 | 42 | 0 | 42 | 0 | 0 | 42 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 1026
- identity switches: 28; fragmentation (coverage interruptions): 8; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 40 -> 44 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 40 -> 45 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 40 -> 48 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 40 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 40 -> 55 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 40 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 40 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 73 -> 63 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 80 -> 75 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 75 -> 73 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f227: ref 79105: 58 -> 87 at (1392, 2996), 1 frames after previous cover
- f227: ref 79111: 64 -> 58 at (1450, 3001.5), 1 frames after previous cover
- f227: ref 79115: 67 -> 64 at (1458.5, 3002), 1 frames after previous cover
- f227: ref 79122: 63 -> 67 at (1475.5, 3007), 1 frames after previous cover
- f228: ref 79102: 87 -> 40 at (1356, 2997.5), 2 frames after previous cover
- f228: ref 79103: 40 -> 87 at (1365.5, 2995), 1 frames after previous cover
- f228: ref 79105: 87 -> 59 at (1385, 2995.5), 1 frames after previous cover
- f228: ref 79108: 59 -> 58 at (1416, 2999.5), 1 frames after previous cover
- f228: ref 79111: 58 -> 64 at (1444.5, 3000.5), 1 frames after previous cover
- f228: ref 79115: 64 -> 67 at (1453, 3002), 1 frames after previous cover
- f228: ref 79122: 67 -> 63 at (1469, 3006), 1 frames after previous cover
- f335: ref 79134: 80 -> 63 at (898.5, 2961.5), 1 frames after previous cover
- f336: ref 79122: 63 -> 178 at (832, 2983), 2 frames after previous cover
- f467: ref 79136: 92 -> 84 at (403.5, 2885.5), 1 frames after previous cover
- f468: ref 79135: 84 -> 92 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 33 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 37 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 42 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 39 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 44 (350), 40 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 45 (341), 40 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 48 (360), 40 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (361), 40 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 55 (356), 40 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 40 (247), 87 (93), 58 (26) |
| 79103 | 380 (99..481) | 379 | 0 | 87 (251), 40 (127), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 59 (254), 58 (97), 54 (27), 87 (1) |
| 79108 | 385 (104..492) | 383 | 0 | 58 (262), 59 (121) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 64 (383), 58 (1) |
| 79115 | 421 (111..531) | 419 | 0 | 67 (418), 64 (1) |
| 79116 | 411 (114..530) | 409 | 0 | 69 (409) |
| 79122 | 404 (118..532) | 401 | 1 | 63 (197), 178 (194), 73 (9), 67 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 73 (382), 75 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 75 (397), 80 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 80 (206), 63 (199) |
| 79135 | 409 (129..542) | 409 | 0 | 84 (334), 92 (75) |
| 79139 | 406 (132..537) | 404 | 0 | 90 (404) |
| 79136 | 393 (136..538) | 391 | 0 | 92 (320), 84 (71) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 246 | 490..531 | 42 | 0 | 42 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 42/417/1007; tracks with internal gaps: 21; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 26 (trailing rows total 907)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 33 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 37 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78969 |
| 39 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 40 | 86..506 | 421 | 421 | 387 | 34 | 5 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 42 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 44 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 45 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 48 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 53 | 99..510 | 412 | 412 | 361 | 51 | 2 | 1 | 49 | 79097 |
| 54 | 100..526 | 427 | 427 | 395 | 32 | 3 | 1 | 29 | 79103, 79105, 79110 |
| 55 | 101..517 | 417 | 417 | 356 | 61 | 10 | 2 | 50 | 79098 |
| 58 | 103..521 | 419 | 419 | 386 | 33 | 4 | 1 | 29 | 79102, 79105, 79108, 79111 |
| 59 | 106..513 | 408 | 408 | 375 | 33 | 4 | 1 | 29 | 79105, 79108 |
| 63 | 110..562 | 453 | 453 | 414 | 39 | 10 | 1 | 29 | 79110, 79122, 79134 |
| 64 | 111..529 | 419 | 419 | 384 | 35 | 5 | 2 | 29 | 79111, 79115 |
| 67 | 113..560 | 448 | 448 | 419 | 29 | 0 | 0 | 29 | 79115, 79122 |
| 69 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79116 |
| 73 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 75 | 122..556 | 435 | 435 | 404 | 31 | 2 | 1 | 29 | 79128, 79132 |
| 80 | 126..364 | 239 | 239 | 209 | 30 | 0 | 0 | 30 | 79128, 79134 |
| 84 | 129..566 | 438 | 438 | 405 | 33 | 5 | 1 | 28 | 79135, 79136 |
| 87 | 132..510 | 379 | 379 | 345 | 34 | 4 | 2 | 29 | 79102, 79103, 79105 |
| 90 | 134..567 | 434 | 434 | 404 | 30 | 0 | 0 | 30 | 79139 |
| 92 | 138..669 | 532 | 532 | 395 | 137 | 9 | 2 | 127 | 79135, 79136 |
| 178 | 336..561 | 226 | 226 | 194 | 32 | 3 | 1 | 29 | 79122 |
| 246 | 490..531 | 42 | 42 | 0 | 42 | 0 | 0 | 42 | - |
