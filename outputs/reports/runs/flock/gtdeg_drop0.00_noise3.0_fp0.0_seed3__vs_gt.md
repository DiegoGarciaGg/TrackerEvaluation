# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=7ba1c32d78d1
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise3.0_fp0.0_seed3/tracks.csv sha256=ee5386145246c6bc
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise3.0_fp0.0_seed3.csv sha256=7ba1c32d78d13a02
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise3.0_fp0.0_seed3
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
| observations | none | 4 | 10142 | 10090 | 0.361 | 0.433 | 0.301 | 2.19 | 0.343 | 0.153 | 2.41 | 138 | 2461.0 | 0.461 | 0.462 | 0.460 | 0.581 | 0.584 | 5892 | 4250 | 4198 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 10090 | 0.512 | 0.602 | 0.436 | 2.75 | 0.616 | 0.715 | 3.21 | 119 | 1256.0 | 0.687 | 0.689 | 0.685 | 0.861 | 0.865 | 8732 | 1410 | 1358 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10090 | 0.595 | 0.677 | 0.524 | 3.12 | 0.750 | 0.925 | 3.60 | 91 | 410.0 | 0.781 | 0.783 | 0.779 | 0.964 | 0.969 | 9779 | 363 | 311 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10090 | 0.687 | 0.758 | 0.623 | 3.68 | 0.813 | 0.976 | 3.85 | 87 | 145.0 | 0.844 | 0.846 | 0.842 | 0.990 | 0.995 | 10039 | 103 | 51 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10090 | 0.361 | 0.433 | 0.301 | 2.19 | 0.343 | 0.153 | 2.41 | 138 | 2461.0 | 0.461 | 0.462 | 0.460 | 0.581 | 0.584 | 5892 | 4250 | 4198 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 10090 | 0.512 | 0.602 | 0.436 | 2.75 | 0.616 | 0.715 | 3.21 | 119 | 1256.0 | 0.687 | 0.689 | 0.685 | 0.861 | 0.865 | 8732 | 1410 | 1358 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10090 | 0.595 | 0.677 | 0.524 | 3.12 | 0.750 | 0.925 | 3.60 | 91 | 410.0 | 0.781 | 0.783 | 0.779 | 0.964 | 0.969 | 9779 | 363 | 311 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10090 | 0.687 | 0.758 | 0.623 | 3.68 | 0.813 | 0.976 | 3.85 | 87 | 145.0 | 0.844 | 0.846 | 0.842 | 0.990 | 0.995 | 10039 | 103 | 51 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10904 | 0.340 | 0.406 | 0.284 | 2.19 | 0.325 | 0.075 | 2.41 | 147 | 2459.0 | 0.444 | 0.428 | 0.460 | 0.582 | 0.542 | 5905 | 4237 | 4999 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10904 | 0.480 | 0.562 | 0.410 | 2.75 | 0.578 | 0.637 | 3.21 | 121 | 1248.0 | 0.661 | 0.638 | 0.686 | 0.862 | 0.802 | 8741 | 1401 | 2163 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10904 | 0.557 | 0.630 | 0.492 | 3.13 | 0.700 | 0.845 | 3.60 | 94 | 405.0 | 0.752 | 0.725 | 0.780 | 0.965 | 0.897 | 9783 | 359 | 1121 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10904 | 0.642 | 0.705 | 0.585 | 3.69 | 0.759 | 0.899 | 3.84 | 70 | 144.0 | 0.814 | 0.785 | 0.844 | 0.990 | 0.921 | 10044 | 98 | 860 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10904 | 0.340 | 0.406 | 0.284 | 2.19 | 0.325 | 0.075 | 2.41 | 147 | 2459.0 | 0.444 | 0.428 | 0.460 | 0.582 | 0.542 | 5905 | 4237 | 4999 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10904 | 0.480 | 0.562 | 0.410 | 2.75 | 0.578 | 0.637 | 3.21 | 121 | 1248.0 | 0.661 | 0.638 | 0.686 | 0.862 | 0.802 | 8741 | 1401 | 2163 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10904 | 0.557 | 0.630 | 0.492 | 3.13 | 0.700 | 0.845 | 3.60 | 94 | 405.0 | 0.752 | 0.725 | 0.780 | 0.965 | 0.897 | 9783 | 359 | 1121 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10904 | 0.642 | 0.705 | 0.585 | 3.69 | 0.759 | 0.899 | 3.84 | 70 | 144.0 | 0.814 | 0.785 | 0.844 | 0.990 | 0.921 | 10044 | 98 | 860 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9779; unmatched reference entries: 363; unmatched candidate entries: 311
- identity switches: 91; fragmentation (coverage interruptions): 304; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 4 -> 7 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 8 -> 9 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 9 -> 8 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 16 -> 17 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 13 -> 10 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 18 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 18 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 18 -> 17 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 17 -> 18 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 17 -> 18 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 18 -> 17 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 18 -> 17 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 17 -> 18 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 13 -> 17 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 17 -> 13 at (1675.5, 3017), 1 frames after previous cover
- f210: ref 79132: 20 -> 16 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 16 -> 20 at (1579, 3004.5), 1 frames after previous cover
- f216: ref 79103: 11 -> 24 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79102: 24 -> 11 at (1421, 3005), 3 frames after previous cover
- f225: ref 79037: 7 -> 5 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 5 -> 7 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 18 -> 13 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 16 -> 18 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 20 -> 16 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 5 -> 7 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 7 -> 5 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 13 -> 19 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 19 -> 18 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 18 -> 20 at (1483, 3006.5), 1 frames after previous cover
- f227: ref 79103: 24 -> 11 at (1374, 2997.5), 1 frames after previous cover
- f228: ref 79103: 11 -> 24 at (1365.5, 2995), 1 frames after previous cover
- f243: ref 79116: 18 -> 16 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 16 -> 18 at (1379, 2985.5), 2 frames after previous cover
- f244: ref 79115: 19 -> 16 at (1358, 2997), 1 frames after previous cover
- f245: ref 79115: 16 -> 19 at (1351, 2998), 1 frames after previous cover
- f245: ref 79116: 16 -> 20 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 20 -> 16 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 11 -> 24 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 24 -> 11 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 19 -> 20 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 20 -> 19 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 7 -> 5 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 5 -> 7 at (1021.5, 2989), 2 frames after previous cover
- f271: ref 79037: 5 -> 7 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 7 -> 5 at (951.5, 2989.5), 2 frames after previous cover
- f273: ref 79045: 5 -> 7 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 20 -> 19 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 7 -> 5 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 19 -> 20 at (1184.5, 2981), 2 frames after previous cover
- f279: ref 78971: 3 -> 7 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 78971: 7 -> 3 at (883, 2985.5), 1 frames after previous cover
- f281: ref 79116: 20 -> 18 at (1143, 2980.5), 2 frames after previous cover
- ... 31 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 1 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 2 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 3 (321), 7 (19) |
| 79045 | 355 (84..443) | 338 | 12 | 5 (166), 7 (155), 3 (17) |
| 79037 | 355 (86..445) | 338 | 16 | 5 (171), 7 (162), 4 (5) |
| 78897 | 345 (89..450) | 333 | 9 | 4 (333) |
| 78899 | 365 (91..455) | 359 | 6 | 6 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 8 (350), 9 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 9 (344) |
| 79102 | 371 (98..477) | 349 | 17 | 24 (290), 11 (59) |
| 79103 | 380 (99..481) | 373 | 6 | 11 (313), 24 (31), 10 (29) |
| 79105 | 379 (101..484) | 364 | 12 | 10 (339), 13 (24), 11 (1) |
| 79108 | 385 (104..492) | 375 | 8 | 14 (375) |
| 79110 | 388 (106..497) | 367 | 14 | 17 (295), 13 (57), 18 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 19 (198), 13 (98), 17 (47), 18 (29), 16 (1) |
| 79115 | 421 (111..531) | 399 | 18 | 13 (201), 18 (73), 19 (52), 17 (29), 20 (21), 21 (19), 16 (4) |
| 79116 | 411 (114..530) | 396 | 15 | 19 (112), 21 (82), 16 (70), 18 (70), 20 (61), 13 (1) |
| 79122 | 404 (118..532) | 397 | 5 | 18 (178), 16 (161), 13 (31), 20 (26), 21 (1) |
| 79132 | 391 (120..515) | 373 | 16 | 20 (175), 16 (156), 18 (35), 21 (7) |
| 79128 | 402 (124..527) | 386 | 12 | 21 (284), 20 (99), 22 (3) |
| 79134 | 407 (127..533) | 397 | 8 | 22 (349), 26 (35), 23 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 23 (326), 25 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 25 (322), 23 (49), 26 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 26 (324), 22 (48), 23 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/385/1007; tracks with internal gaps: 25; total internal gaps: 302; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 342 | 6 | 6 | 1 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 345 | 5 | 5 | 1 | 0 | 78969 |
| 3 | 86..439 | 354 | 349 | 338 | 11 | 11 | 1 | 0 | 78971, 79045 |
| 4 | 86..450 | 365 | 348 | 338 | 10 | 9 | 2 | 0 | 78897, 79037 |
| 5 | 88..445 | 358 | 353 | 337 | 16 | 15 | 2 | 0 | 79037, 79045 |
| 6 | 91..455 | 365 | 365 | 359 | 6 | 6 | 1 | 0 | 78899 |
| 7 | 93..443 | 351 | 347 | 336 | 11 | 11 | 1 | 0 | 78971, 79037, 79045 |
| 8 | 96..461 | 366 | 364 | 350 | 14 | 14 | 1 | 0 | 79097 |
| 9 | 99..467 | 369 | 358 | 345 | 13 | 13 | 1 | 0 | 79097, 79098 |
| 10 | 100..484 | 385 | 380 | 368 | 12 | 12 | 1 | 0 | 79103, 79105 |
| 11 | 101..481 | 381 | 378 | 373 | 5 | 5 | 1 | 0 | 79102, 79103, 79105 |
| 13 | 105..531 | 427 | 426 | 412 | 14 | 13 | 2 | 0 | 79105, 79110, 79111, 79115, 79116, 79122 |
| 14 | 106..492 | 387 | 383 | 375 | 8 | 8 | 1 | 0 | 79108 |
| 16 | 110..515 | 406 | 400 | 392 | 8 | 8 | 1 | 0 | 79111, 79115, 79116, 79122, 79132 |
| 17 | 111..497 | 387 | 384 | 371 | 13 | 13 | 1 | 0 | 79110, 79111, 79115 |
| 18 | 113..530 | 418 | 411 | 400 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 116..500 | 385 | 377 | 362 | 15 | 14 | 2 | 0 | 79111, 79115, 79116 |
| 20 | 120..527 | 408 | 402 | 382 | 20 | 20 | 1 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 21 | 122..532 | 411 | 409 | 393 | 16 | 14 | 2 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 22 | 126..537 | 412 | 412 | 400 | 12 | 12 | 1 | 0 | 79128, 79134, 79136 |
| 23 | 129..538 | 410 | 405 | 393 | 12 | 12 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 132..477 | 346 | 339 | 321 | 18 | 17 | 2 | 0 | 79102, 79103 |
| 25 | 134..542 | 409 | 408 | 394 | 14 | 14 | 1 | 0 | 79135, 79139 |
| 26 | 138..533 | 396 | 387 | 378 | 9 | 9 | 1 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9779; unmatched reference entries: 363; unmatched candidate entries: 311
- identity switches: 91; fragmentation (coverage interruptions): 304; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 4 -> 7 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 8 -> 9 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 9 -> 8 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 16 -> 17 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 13 -> 10 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 18 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 18 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 18 -> 17 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 17 -> 18 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 17 -> 18 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 18 -> 17 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 18 -> 17 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 17 -> 18 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 13 -> 17 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 17 -> 13 at (1675.5, 3017), 1 frames after previous cover
- f210: ref 79132: 20 -> 16 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 16 -> 20 at (1579, 3004.5), 1 frames after previous cover
- f216: ref 79103: 11 -> 24 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79102: 24 -> 11 at (1421, 3005), 3 frames after previous cover
- f225: ref 79037: 7 -> 5 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 5 -> 7 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 18 -> 13 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 16 -> 18 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 20 -> 16 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 5 -> 7 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 7 -> 5 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 13 -> 19 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 19 -> 18 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 18 -> 20 at (1483, 3006.5), 1 frames after previous cover
- f227: ref 79103: 24 -> 11 at (1374, 2997.5), 1 frames after previous cover
- f228: ref 79103: 11 -> 24 at (1365.5, 2995), 1 frames after previous cover
- f243: ref 79116: 18 -> 16 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 16 -> 18 at (1379, 2985.5), 2 frames after previous cover
- f244: ref 79115: 19 -> 16 at (1358, 2997), 1 frames after previous cover
- f245: ref 79115: 16 -> 19 at (1351, 2998), 1 frames after previous cover
- f245: ref 79116: 16 -> 20 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 20 -> 16 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 11 -> 24 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 24 -> 11 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 19 -> 20 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 20 -> 19 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 7 -> 5 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 5 -> 7 at (1021.5, 2989), 2 frames after previous cover
- f271: ref 79037: 5 -> 7 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 7 -> 5 at (951.5, 2989.5), 2 frames after previous cover
- f273: ref 79045: 5 -> 7 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 20 -> 19 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 7 -> 5 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 19 -> 20 at (1184.5, 2981), 2 frames after previous cover
- f279: ref 78971: 3 -> 7 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 78971: 7 -> 3 at (883, 2985.5), 1 frames after previous cover
- f281: ref 79116: 20 -> 18 at (1143, 2980.5), 2 frames after previous cover
- ... 31 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 1 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 2 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 3 (321), 7 (19) |
| 79045 | 355 (84..443) | 338 | 12 | 5 (166), 7 (155), 3 (17) |
| 79037 | 355 (86..445) | 338 | 16 | 5 (171), 7 (162), 4 (5) |
| 78897 | 345 (89..450) | 333 | 9 | 4 (333) |
| 78899 | 365 (91..455) | 359 | 6 | 6 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 8 (350), 9 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 9 (344) |
| 79102 | 371 (98..477) | 349 | 17 | 24 (290), 11 (59) |
| 79103 | 380 (99..481) | 373 | 6 | 11 (313), 24 (31), 10 (29) |
| 79105 | 379 (101..484) | 364 | 12 | 10 (339), 13 (24), 11 (1) |
| 79108 | 385 (104..492) | 375 | 8 | 14 (375) |
| 79110 | 388 (106..497) | 367 | 14 | 17 (295), 13 (57), 18 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 19 (198), 13 (98), 17 (47), 18 (29), 16 (1) |
| 79115 | 421 (111..531) | 399 | 18 | 13 (201), 18 (73), 19 (52), 17 (29), 20 (21), 21 (19), 16 (4) |
| 79116 | 411 (114..530) | 396 | 15 | 19 (112), 21 (82), 16 (70), 18 (70), 20 (61), 13 (1) |
| 79122 | 404 (118..532) | 397 | 5 | 18 (178), 16 (161), 13 (31), 20 (26), 21 (1) |
| 79132 | 391 (120..515) | 373 | 16 | 20 (175), 16 (156), 18 (35), 21 (7) |
| 79128 | 402 (124..527) | 386 | 12 | 21 (284), 20 (99), 22 (3) |
| 79134 | 407 (127..533) | 397 | 8 | 22 (349), 26 (35), 23 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 23 (326), 25 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 25 (322), 23 (49), 26 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 26 (324), 22 (48), 23 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/385/1007; tracks with internal gaps: 25; total internal gaps: 302; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 342 | 6 | 6 | 1 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 345 | 5 | 5 | 1 | 0 | 78969 |
| 3 | 86..439 | 354 | 349 | 338 | 11 | 11 | 1 | 0 | 78971, 79045 |
| 4 | 86..450 | 365 | 348 | 338 | 10 | 9 | 2 | 0 | 78897, 79037 |
| 5 | 88..445 | 358 | 353 | 337 | 16 | 15 | 2 | 0 | 79037, 79045 |
| 6 | 91..455 | 365 | 365 | 359 | 6 | 6 | 1 | 0 | 78899 |
| 7 | 93..443 | 351 | 347 | 336 | 11 | 11 | 1 | 0 | 78971, 79037, 79045 |
| 8 | 96..461 | 366 | 364 | 350 | 14 | 14 | 1 | 0 | 79097 |
| 9 | 99..467 | 369 | 358 | 345 | 13 | 13 | 1 | 0 | 79097, 79098 |
| 10 | 100..484 | 385 | 380 | 368 | 12 | 12 | 1 | 0 | 79103, 79105 |
| 11 | 101..481 | 381 | 378 | 373 | 5 | 5 | 1 | 0 | 79102, 79103, 79105 |
| 13 | 105..531 | 427 | 426 | 412 | 14 | 13 | 2 | 0 | 79105, 79110, 79111, 79115, 79116, 79122 |
| 14 | 106..492 | 387 | 383 | 375 | 8 | 8 | 1 | 0 | 79108 |
| 16 | 110..515 | 406 | 400 | 392 | 8 | 8 | 1 | 0 | 79111, 79115, 79116, 79122, 79132 |
| 17 | 111..497 | 387 | 384 | 371 | 13 | 13 | 1 | 0 | 79110, 79111, 79115 |
| 18 | 113..530 | 418 | 411 | 400 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 116..500 | 385 | 377 | 362 | 15 | 14 | 2 | 0 | 79111, 79115, 79116 |
| 20 | 120..527 | 408 | 402 | 382 | 20 | 20 | 1 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 21 | 122..532 | 411 | 409 | 393 | 16 | 14 | 2 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 22 | 126..537 | 412 | 412 | 400 | 12 | 12 | 1 | 0 | 79128, 79134, 79136 |
| 23 | 129..538 | 410 | 405 | 393 | 12 | 12 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 132..477 | 346 | 339 | 321 | 18 | 17 | 2 | 0 | 79102, 79103 |
| 25 | 134..542 | 409 | 408 | 394 | 14 | 14 | 1 | 0 | 79135, 79139 |
| 26 | 138..533 | 396 | 387 | 378 | 9 | 9 | 1 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9783; unmatched reference entries: 359; unmatched candidate entries: 1121
- identity switches: 94; fragmentation (coverage interruptions): 299; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 4 -> 7 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 8 -> 9 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 9 -> 8 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 16 -> 17 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 13 -> 10 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 18 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 18 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 18 -> 17 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 17 -> 18 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 17 -> 18 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 18 -> 17 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 18 -> 17 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 17 -> 18 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 13 -> 17 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 17 -> 13 at (1675.5, 3017), 1 frames after previous cover
- f194: ref 79132: 20 -> 16 at (1692.5, 3016), 1 frames after previous cover
- f195: ref 79122: 16 -> 20 at (1681, 3019), 2 frames after previous cover
- f201: ref 79122: 20 -> 16 at (1641, 3015), 1 frames after previous cover
- f201: ref 79132: 16 -> 20 at (1646.5, 3013), 1 frames after previous cover
- f210: ref 79132: 20 -> 16 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 16 -> 20 at (1579, 3004.5), 1 frames after previous cover
- f218: ref 79102: 24 -> 11 at (1415.5, 3002), 4 frames after previous cover
- f218: ref 79103: 11 -> 24 at (1425.5, 3002), 1 frames after previous cover
- f225: ref 79037: 7 -> 5 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 5 -> 7 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 18 -> 13 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 16 -> 18 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 20 -> 16 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 5 -> 7 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 7 -> 5 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 13 -> 19 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 19 -> 18 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 18 -> 20 at (1483, 3006.5), 1 frames after previous cover
- f243: ref 79116: 18 -> 16 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 16 -> 18 at (1379, 2985.5), 2 frames after previous cover
- f245: ref 79116: 16 -> 20 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 20 -> 16 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 11 -> 24 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 24 -> 11 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 19 -> 20 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 20 -> 19 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 7 -> 5 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 5 -> 7 at (1021.5, 2989), 2 frames after previous cover
- f270: ref 79045: 7 -> 3 at (957.5, 2987.5), 1 frames after previous cover
- f271: ref 79037: 5 -> 7 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 3 -> 5 at (951.5, 2989.5), 1 frames after previous cover
- f273: ref 79045: 5 -> 7 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 20 -> 19 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 7 -> 5 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 19 -> 20 at (1184.5, 2981), 2 frames after previous cover
- f279: ref 78971: 3 -> 7 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 78971: 7 -> 3 at (883, 2985.5), 1 frames after previous cover
- ... 34 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 1 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 2 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 3 (321), 7 (19) |
| 79045 | 355 (84..443) | 339 | 11 | 5 (166), 7 (155), 3 (18) |
| 79037 | 355 (86..445) | 338 | 16 | 5 (171), 7 (162), 4 (5) |
| 78897 | 345 (89..450) | 334 | 8 | 4 (332), 2 (2) |
| 78899 | 365 (91..455) | 359 | 6 | 6 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 8 (350), 9 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 9 (344) |
| 79102 | 371 (98..477) | 348 | 17 | 24 (290), 11 (58) |
| 79103 | 380 (99..481) | 373 | 6 | 11 (314), 24 (30), 10 (29) |
| 79105 | 379 (101..484) | 365 | 11 | 10 (338), 13 (24), 11 (3) |
| 79108 | 385 (104..492) | 375 | 8 | 14 (375) |
| 79110 | 388 (106..497) | 367 | 14 | 17 (295), 13 (57), 18 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 19 (198), 13 (98), 17 (47), 18 (29), 16 (1) |
| 79115 | 421 (111..531) | 402 | 16 | 13 (201), 18 (74), 19 (55), 17 (29), 20 (21), 21 (19), 16 (3) |
| 79116 | 411 (114..530) | 396 | 15 | 19 (112), 21 (82), 16 (70), 18 (70), 20 (61), 13 (1) |
| 79122 | 404 (118..532) | 394 | 7 | 18 (178), 16 (155), 13 (32), 20 (29) |
| 79132 | 391 (120..515) | 374 | 15 | 20 (169), 16 (163), 18 (35), 21 (7) |
| 79128 | 402 (124..527) | 387 | 11 | 21 (284), 20 (98), 22 (3), 16 (2) |
| 79134 | 407 (127..533) | 397 | 8 | 22 (349), 26 (35), 23 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 23 (326), 25 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 25 (322), 23 (49), 26 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 26 (324), 22 (49), 23 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/414/1007; tracks with internal gaps: 25; total internal gaps: 401; longest internal gap: 14; tracks ending in coasting: 24 (trailing rows total 671)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 342 | 39 | 8 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 347 | 35 | 8 | 14 | 13 | 78897, 78969 |
| 3 | 86..468 | 383 | 383 | 339 | 44 | 14 | 2 | 29 | 78971, 79045 |
| 4 | 86..479 | 394 | 394 | 337 | 57 | 25 | 2 | 31 | 78897, 79037 |
| 5 | 88..474 | 387 | 387 | 337 | 50 | 18 | 2 | 29 | 79037, 79045 |
| 6 | 91..484 | 394 | 394 | 359 | 35 | 6 | 1 | 29 | 78899 |
| 7 | 93..472 | 380 | 380 | 336 | 44 | 15 | 1 | 29 | 78971, 79037, 79045 |
| 8 | 96..490 | 395 | 395 | 350 | 45 | 15 | 2 | 29 | 79097 |
| 9 | 99..496 | 398 | 398 | 345 | 53 | 23 | 2 | 29 | 79097, 79098 |
| 10 | 100..513 | 414 | 414 | 367 | 47 | 14 | 3 | 31 | 79103, 79105 |
| 11 | 101..510 | 410 | 410 | 375 | 35 | 8 | 2 | 26 | 79102, 79103, 79105 |
| 13 | 105..560 | 456 | 456 | 413 | 43 | 14 | 2 | 28 | 79105, 79110, 79111, 79115, 79116, 79122 |
| 14 | 106..521 | 416 | 416 | 375 | 41 | 12 | 1 | 29 | 79108 |
| 16 | 110..544 | 435 | 435 | 394 | 41 | 15 | 10 | 17 | 79111, 79115, 79116, 79122, 79128, 79132 |
| 17 | 111..526 | 416 | 416 | 371 | 45 | 16 | 1 | 29 | 79110, 79111, 79115 |
| 18 | 113..559 | 447 | 447 | 401 | 46 | 17 | 2 | 28 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 116..529 | 414 | 414 | 365 | 49 | 18 | 2 | 29 | 79111, 79115, 79116 |
| 20 | 120..556 | 437 | 437 | 378 | 59 | 25 | 2 | 31 | 79115, 79116, 79122, 79128, 79132 |
| 21 | 122..561 | 440 | 440 | 392 | 48 | 15 | 2 | 31 | 79115, 79116, 79128, 79132 |
| 22 | 126..566 | 441 | 441 | 401 | 40 | 12 | 1 | 28 | 79128, 79134, 79136 |
| 23 | 129..567 | 439 | 439 | 392 | 47 | 17 | 1 | 30 | 79134, 79135, 79136, 79139 |
| 24 | 132..506 | 375 | 375 | 320 | 55 | 23 | 3 | 29 | 79102, 79103 |
| 25 | 134..571 | 438 | 438 | 394 | 44 | 15 | 1 | 29 | 79135, 79139 |
| 26 | 138..562 | 425 | 425 | 378 | 47 | 17 | 2 | 29 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9783; unmatched reference entries: 359; unmatched candidate entries: 1121
- identity switches: 94; fragmentation (coverage interruptions): 299; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 4 -> 7 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 8 -> 9 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 9 -> 8 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 16 -> 17 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 19 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 10 -> 11 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 13 -> 10 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 18 -> 13 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 17 -> 18 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 19 -> 17 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 19 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 20 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 22 -> 21 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 21 -> 20 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 11 -> 24 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 18 -> 17 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 17 -> 18 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 17 -> 18 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 18 -> 17 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 18 -> 17 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 17 -> 18 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 13 -> 17 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 17 -> 13 at (1675.5, 3017), 1 frames after previous cover
- f194: ref 79132: 20 -> 16 at (1692.5, 3016), 1 frames after previous cover
- f195: ref 79122: 16 -> 20 at (1681, 3019), 2 frames after previous cover
- f201: ref 79122: 20 -> 16 at (1641, 3015), 1 frames after previous cover
- f201: ref 79132: 16 -> 20 at (1646.5, 3013), 1 frames after previous cover
- f210: ref 79132: 20 -> 16 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 16 -> 20 at (1579, 3004.5), 1 frames after previous cover
- f218: ref 79102: 24 -> 11 at (1415.5, 3002), 4 frames after previous cover
- f218: ref 79103: 11 -> 24 at (1425.5, 3002), 1 frames after previous cover
- f225: ref 79037: 7 -> 5 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 5 -> 7 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 18 -> 13 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 16 -> 18 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 20 -> 16 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 5 -> 7 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 7 -> 5 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 13 -> 19 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 19 -> 18 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 18 -> 20 at (1483, 3006.5), 1 frames after previous cover
- f243: ref 79116: 18 -> 16 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 16 -> 18 at (1379, 2985.5), 2 frames after previous cover
- f245: ref 79116: 16 -> 20 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 20 -> 16 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 11 -> 24 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 24 -> 11 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 19 -> 20 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 20 -> 19 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 7 -> 5 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 5 -> 7 at (1021.5, 2989), 2 frames after previous cover
- f270: ref 79045: 7 -> 3 at (957.5, 2987.5), 1 frames after previous cover
- f271: ref 79037: 5 -> 7 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 3 -> 5 at (951.5, 2989.5), 1 frames after previous cover
- f273: ref 79045: 5 -> 7 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 20 -> 19 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 7 -> 5 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 19 -> 20 at (1184.5, 2981), 2 frames after previous cover
- f279: ref 78971: 3 -> 7 at (887.5, 2987.5), 2 frames after previous cover
- f280: ref 78971: 7 -> 3 at (883, 2985.5), 1 frames after previous cover
- ... 34 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 1 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 2 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 3 (321), 7 (19) |
| 79045 | 355 (84..443) | 339 | 11 | 5 (166), 7 (155), 3 (18) |
| 79037 | 355 (86..445) | 338 | 16 | 5 (171), 7 (162), 4 (5) |
| 78897 | 345 (89..450) | 334 | 8 | 4 (332), 2 (2) |
| 78899 | 365 (91..455) | 359 | 6 | 6 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 8 (350), 9 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 9 (344) |
| 79102 | 371 (98..477) | 348 | 17 | 24 (290), 11 (58) |
| 79103 | 380 (99..481) | 373 | 6 | 11 (314), 24 (30), 10 (29) |
| 79105 | 379 (101..484) | 365 | 11 | 10 (338), 13 (24), 11 (3) |
| 79108 | 385 (104..492) | 375 | 8 | 14 (375) |
| 79110 | 388 (106..497) | 367 | 14 | 17 (295), 13 (57), 18 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 19 (198), 13 (98), 17 (47), 18 (29), 16 (1) |
| 79115 | 421 (111..531) | 402 | 16 | 13 (201), 18 (74), 19 (55), 17 (29), 20 (21), 21 (19), 16 (3) |
| 79116 | 411 (114..530) | 396 | 15 | 19 (112), 21 (82), 16 (70), 18 (70), 20 (61), 13 (1) |
| 79122 | 404 (118..532) | 394 | 7 | 18 (178), 16 (155), 13 (32), 20 (29) |
| 79132 | 391 (120..515) | 374 | 15 | 20 (169), 16 (163), 18 (35), 21 (7) |
| 79128 | 402 (124..527) | 387 | 11 | 21 (284), 20 (98), 22 (3), 16 (2) |
| 79134 | 407 (127..533) | 397 | 8 | 22 (349), 26 (35), 23 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 23 (326), 25 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 25 (322), 23 (49), 26 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 26 (324), 22 (49), 23 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/414/1007; tracks with internal gaps: 25; total internal gaps: 401; longest internal gap: 14; tracks ending in coasting: 24 (trailing rows total 671)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 342 | 39 | 8 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 347 | 35 | 8 | 14 | 13 | 78897, 78969 |
| 3 | 86..468 | 383 | 383 | 339 | 44 | 14 | 2 | 29 | 78971, 79045 |
| 4 | 86..479 | 394 | 394 | 337 | 57 | 25 | 2 | 31 | 78897, 79037 |
| 5 | 88..474 | 387 | 387 | 337 | 50 | 18 | 2 | 29 | 79037, 79045 |
| 6 | 91..484 | 394 | 394 | 359 | 35 | 6 | 1 | 29 | 78899 |
| 7 | 93..472 | 380 | 380 | 336 | 44 | 15 | 1 | 29 | 78971, 79037, 79045 |
| 8 | 96..490 | 395 | 395 | 350 | 45 | 15 | 2 | 29 | 79097 |
| 9 | 99..496 | 398 | 398 | 345 | 53 | 23 | 2 | 29 | 79097, 79098 |
| 10 | 100..513 | 414 | 414 | 367 | 47 | 14 | 3 | 31 | 79103, 79105 |
| 11 | 101..510 | 410 | 410 | 375 | 35 | 8 | 2 | 26 | 79102, 79103, 79105 |
| 13 | 105..560 | 456 | 456 | 413 | 43 | 14 | 2 | 28 | 79105, 79110, 79111, 79115, 79116, 79122 |
| 14 | 106..521 | 416 | 416 | 375 | 41 | 12 | 1 | 29 | 79108 |
| 16 | 110..544 | 435 | 435 | 394 | 41 | 15 | 10 | 17 | 79111, 79115, 79116, 79122, 79128, 79132 |
| 17 | 111..526 | 416 | 416 | 371 | 45 | 16 | 1 | 29 | 79110, 79111, 79115 |
| 18 | 113..559 | 447 | 447 | 401 | 46 | 17 | 2 | 28 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 19 | 116..529 | 414 | 414 | 365 | 49 | 18 | 2 | 29 | 79111, 79115, 79116 |
| 20 | 120..556 | 437 | 437 | 378 | 59 | 25 | 2 | 31 | 79115, 79116, 79122, 79128, 79132 |
| 21 | 122..561 | 440 | 440 | 392 | 48 | 15 | 2 | 31 | 79115, 79116, 79128, 79132 |
| 22 | 126..566 | 441 | 441 | 401 | 40 | 12 | 1 | 28 | 79128, 79134, 79136 |
| 23 | 129..567 | 439 | 439 | 392 | 47 | 17 | 1 | 30 | 79134, 79135, 79136, 79139 |
| 24 | 132..506 | 375 | 375 | 320 | 55 | 23 | 3 | 29 | 79102, 79103 |
| 25 | 134..571 | 438 | 438 | 394 | 44 | 15 | 1 | 29 | 79135, 79139 |
| 26 | 138..562 | 425 | 425 | 378 | 47 | 17 | 2 | 29 | 79134, 79136, 79139 |
