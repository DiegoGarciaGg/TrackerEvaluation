# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=90f9fd0fef71
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise3.0_fp0.5_seed3/tracks.csv sha256=88aa1bdc4f547375
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise3.0_fp0.5_seed3.csv sha256=90f9fd0fef714888
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise3.0_fp0.5_seed3
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
| observations | none | 4 | 10142 | 10095 | 0.340 | 0.433 | 0.267 | 2.19 | 0.322 | 0.153 | 2.41 | 142 | 2461.0 | 0.419 | 0.420 | 0.418 | 0.581 | 0.584 | 5892 | 4250 | 4203 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 10095 | 0.484 | 0.608 | 0.385 | 2.75 | 0.583 | 0.714 | 3.21 | 123 | 1256.0 | 0.627 | 0.629 | 0.626 | 0.861 | 0.865 | 8732 | 1410 | 1363 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10095 | 0.561 | 0.690 | 0.456 | 3.09 | 0.711 | 0.923 | 3.60 | 97 | 410.0 | 0.715 | 0.716 | 0.713 | 0.964 | 0.969 | 9779 | 363 | 316 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10095 | 0.643 | 0.769 | 0.537 | 3.62 | 0.764 | 0.975 | 3.85 | 93 | 145.0 | 0.777 | 0.779 | 0.775 | 0.990 | 0.995 | 10040 | 102 | 55 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10095 | 0.340 | 0.433 | 0.267 | 2.19 | 0.322 | 0.153 | 2.41 | 142 | 2461.0 | 0.419 | 0.420 | 0.418 | 0.581 | 0.584 | 5892 | 4250 | 4203 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 10095 | 0.484 | 0.608 | 0.385 | 2.75 | 0.583 | 0.714 | 3.21 | 123 | 1256.0 | 0.627 | 0.629 | 0.626 | 0.861 | 0.865 | 8732 | 1410 | 1363 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10095 | 0.561 | 0.690 | 0.456 | 3.09 | 0.711 | 0.923 | 3.60 | 97 | 410.0 | 0.715 | 0.716 | 0.713 | 0.964 | 0.969 | 9779 | 363 | 316 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10095 | 0.643 | 0.769 | 0.537 | 3.62 | 0.764 | 0.975 | 3.85 | 93 | 145.0 | 0.777 | 0.779 | 0.775 | 0.990 | 0.995 | 10040 | 102 | 55 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10904 | 0.321 | 0.407 | 0.253 | 2.19 | 0.306 | 0.074 | 2.41 | 151 | 2459.0 | 0.403 | 0.389 | 0.418 | 0.582 | 0.542 | 5905 | 4237 | 4999 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10904 | 0.454 | 0.567 | 0.363 | 2.75 | 0.548 | 0.636 | 3.21 | 125 | 1248.0 | 0.604 | 0.583 | 0.627 | 0.862 | 0.802 | 8741 | 1401 | 2163 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10904 | 0.525 | 0.642 | 0.430 | 3.10 | 0.665 | 0.844 | 3.60 | 100 | 405.0 | 0.688 | 0.664 | 0.714 | 0.965 | 0.897 | 9783 | 359 | 1121 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10904 | 0.601 | 0.715 | 0.506 | 3.62 | 0.713 | 0.898 | 3.84 | 76 | 144.0 | 0.750 | 0.723 | 0.778 | 0.990 | 0.921 | 10045 | 97 | 859 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10904 | 0.321 | 0.407 | 0.253 | 2.19 | 0.306 | 0.074 | 2.41 | 151 | 2459.0 | 0.403 | 0.389 | 0.418 | 0.582 | 0.542 | 5905 | 4237 | 4999 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10904 | 0.454 | 0.567 | 0.363 | 2.75 | 0.548 | 0.636 | 3.21 | 125 | 1248.0 | 0.604 | 0.583 | 0.627 | 0.862 | 0.802 | 8741 | 1401 | 2163 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10904 | 0.525 | 0.642 | 0.430 | 3.10 | 0.665 | 0.844 | 3.60 | 100 | 405.0 | 0.688 | 0.664 | 0.714 | 0.965 | 0.897 | 9783 | 359 | 1121 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10904 | 0.601 | 0.715 | 0.506 | 3.62 | 0.713 | 0.898 | 3.84 | 76 | 144.0 | 0.750 | 0.723 | 0.778 | 0.990 | 0.921 | 10045 | 97 | 859 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9779; unmatched reference entries: 363; unmatched candidate entries: 316
- identity switches: 97; fragmentation (coverage interruptions): 304; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 44 -> 49 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 51 -> 54 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 54 -> 51 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 67 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 67 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 62 -> 55 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 69 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 69 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 67 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 69 -> 68 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 68 -> 69 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 68 -> 69 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 69 -> 68 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 69 -> 68 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 68 -> 69 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 62 -> 68 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 68 -> 62 at (1675.5, 3017), 1 frames after previous cover
- f210: ref 79132: 76 -> 67 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 67 -> 76 at (1579, 3004.5), 1 frames after previous cover
- f216: ref 79103: 56 -> 87 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79102: 87 -> 56 at (1421, 3005), 3 frames after previous cover
- f225: ref 79037: 49 -> 45 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 45 -> 49 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 69 -> 62 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 67 -> 69 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 76 -> 67 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 45 -> 49 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 49 -> 45 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 62 -> 72 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 72 -> 69 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 69 -> 76 at (1483, 3006.5), 1 frames after previous cover
- f227: ref 79103: 87 -> 56 at (1374, 2997.5), 1 frames after previous cover
- f228: ref 79103: 56 -> 87 at (1365.5, 2995), 1 frames after previous cover
- f243: ref 79116: 69 -> 67 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 67 -> 69 at (1379, 2985.5), 2 frames after previous cover
- f244: ref 79115: 72 -> 67 at (1358, 2997), 1 frames after previous cover
- f245: ref 79115: 67 -> 72 at (1351, 2998), 1 frames after previous cover
- f245: ref 79116: 67 -> 76 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 76 -> 67 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 56 -> 87 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 87 -> 56 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 72 -> 76 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 76 -> 72 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 49 -> 45 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 45 -> 49 at (1021.5, 2989), 2 frames after previous cover
- f271: ref 79037: 45 -> 49 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 49 -> 45 at (951.5, 2989.5), 2 frames after previous cover
- f273: ref 79045: 45 -> 49 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 76 -> 72 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 49 -> 45 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 72 -> 76 at (1184.5, 2981), 2 frames after previous cover
- f278: ref 79037: 45 -> 49 at (918.5, 2989.5), 1 frames after previous cover
- f278: ref 79045: 49 -> 43 at (906.5, 2986.5), 1 frames after previous cover
- f280: ref 79045: 43 -> 45 at (892.5, 2989.5), 2 frames after previous cover
- ... 37 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 38 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 41 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 43 (192), 45 (148) |
| 79045 | 355 (84..443) | 338 | 12 | 45 (174), 43 (147), 49 (16), 44 (1) |
| 79037 | 355 (86..445) | 338 | 16 | 49 (319), 45 (14), 44 (5) |
| 78897 | 345 (89..450) | 333 | 9 | 44 (333) |
| 78899 | 365 (91..455) | 359 | 6 | 47 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 51 (350), 54 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 54 (344) |
| 79102 | 371 (98..477) | 349 | 17 | 87 (290), 56 (59) |
| 79103 | 380 (99..481) | 373 | 6 | 56 (164), 62 (149), 87 (31), 55 (29) |
| 79105 | 379 (101..484) | 364 | 12 | 55 (187), 56 (153), 62 (24) |
| 79108 | 385 (104..492) | 375 | 8 | 63 (214), 55 (161) |
| 79110 | 388 (106..497) | 367 | 14 | 63 (167), 68 (128), 62 (57), 69 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 72 (198), 62 (98), 68 (47), 69 (29), 67 (1) |
| 79115 | 421 (111..531) | 399 | 18 | 68 (197), 69 (73), 72 (52), 62 (33), 76 (21), 78 (19), 67 (4) |
| 79116 | 411 (114..530) | 396 | 15 | 72 (112), 78 (82), 67 (70), 69 (70), 76 (61), 68 (1) |
| 79122 | 404 (118..532) | 397 | 5 | 69 (178), 67 (161), 68 (31), 76 (26), 78 (1) |
| 79132 | 391 (120..515) | 373 | 16 | 76 (175), 67 (156), 69 (35), 78 (7) |
| 79128 | 402 (124..527) | 386 | 12 | 78 (284), 76 (99), 81 (3) |
| 79134 | 407 (127..533) | 397 | 8 | 81 (349), 92 (35), 82 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 82 (326), 90 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 90 (322), 82 (49), 92 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 92 (324), 81 (48), 82 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/385/1007; tracks with internal gaps: 25; total internal gaps: 306; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 38 | 78..429 | 352 | 348 | 342 | 6 | 6 | 1 | 0 | 78896 |
| 41 | 82..434 | 353 | 350 | 345 | 5 | 5 | 1 | 0 | 78969 |
| 43 | 86..443 | 358 | 352 | 339 | 13 | 13 | 1 | 0 | 78971, 79045 |
| 44 | 86..450 | 365 | 349 | 339 | 10 | 9 | 2 | 0 | 78897, 79037, 79045 |
| 45 | 88..439 | 352 | 351 | 336 | 15 | 14 | 2 | 0 | 78971, 79037, 79045 |
| 47 | 91..455 | 365 | 365 | 359 | 6 | 6 | 1 | 0 | 78899 |
| 49 | 93..445 | 353 | 348 | 335 | 13 | 13 | 1 | 0 | 79037, 79045 |
| 51 | 96..461 | 366 | 364 | 350 | 14 | 14 | 1 | 0 | 79097 |
| 54 | 99..467 | 369 | 358 | 345 | 13 | 13 | 1 | 0 | 79097, 79098 |
| 55 | 100..492 | 393 | 388 | 377 | 11 | 11 | 1 | 0 | 79103, 79105, 79108 |
| 56 | 101..484 | 384 | 383 | 376 | 7 | 7 | 1 | 0 | 79102, 79103, 79105 |
| 62 | 105..481 | 377 | 374 | 361 | 13 | 11 | 2 | 0 | 79103, 79105, 79110, 79111, 79115 |
| 63 | 106..497 | 392 | 390 | 381 | 9 | 9 | 1 | 0 | 79108, 79110 |
| 67 | 110..515 | 406 | 400 | 392 | 8 | 8 | 1 | 0 | 79111, 79115, 79116, 79122, 79132 |
| 68 | 111..531 | 421 | 418 | 404 | 14 | 14 | 1 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 69 | 113..530 | 418 | 411 | 400 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 116..500 | 385 | 377 | 362 | 15 | 14 | 2 | 0 | 79111, 79115, 79116 |
| 76 | 120..527 | 408 | 402 | 382 | 20 | 20 | 1 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 78 | 122..532 | 411 | 409 | 393 | 16 | 14 | 2 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 81 | 126..537 | 412 | 412 | 400 | 12 | 12 | 1 | 0 | 79128, 79134, 79136 |
| 82 | 129..538 | 410 | 405 | 393 | 12 | 12 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 87 | 132..477 | 346 | 339 | 321 | 18 | 17 | 2 | 0 | 79102, 79103 |
| 90 | 134..542 | 409 | 408 | 394 | 14 | 14 | 1 | 0 | 79135, 79139 |
| 92 | 138..533 | 396 | 387 | 378 | 9 | 9 | 1 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9779; unmatched reference entries: 363; unmatched candidate entries: 316
- identity switches: 97; fragmentation (coverage interruptions): 304; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 44 -> 49 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 51 -> 54 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 54 -> 51 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 67 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 67 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 62 -> 55 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 69 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 69 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 67 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 69 -> 68 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 68 -> 69 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 68 -> 69 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 69 -> 68 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 69 -> 68 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 68 -> 69 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 62 -> 68 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 68 -> 62 at (1675.5, 3017), 1 frames after previous cover
- f210: ref 79132: 76 -> 67 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 67 -> 76 at (1579, 3004.5), 1 frames after previous cover
- f216: ref 79103: 56 -> 87 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79102: 87 -> 56 at (1421, 3005), 3 frames after previous cover
- f225: ref 79037: 49 -> 45 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 45 -> 49 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 69 -> 62 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 67 -> 69 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 76 -> 67 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 45 -> 49 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 49 -> 45 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 62 -> 72 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 72 -> 69 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 69 -> 76 at (1483, 3006.5), 1 frames after previous cover
- f227: ref 79103: 87 -> 56 at (1374, 2997.5), 1 frames after previous cover
- f228: ref 79103: 56 -> 87 at (1365.5, 2995), 1 frames after previous cover
- f243: ref 79116: 69 -> 67 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 67 -> 69 at (1379, 2985.5), 2 frames after previous cover
- f244: ref 79115: 72 -> 67 at (1358, 2997), 1 frames after previous cover
- f245: ref 79115: 67 -> 72 at (1351, 2998), 1 frames after previous cover
- f245: ref 79116: 67 -> 76 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 76 -> 67 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 56 -> 87 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 87 -> 56 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 72 -> 76 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 76 -> 72 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 49 -> 45 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 45 -> 49 at (1021.5, 2989), 2 frames after previous cover
- f271: ref 79037: 45 -> 49 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 49 -> 45 at (951.5, 2989.5), 2 frames after previous cover
- f273: ref 79045: 45 -> 49 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 76 -> 72 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 49 -> 45 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 72 -> 76 at (1184.5, 2981), 2 frames after previous cover
- f278: ref 79037: 45 -> 49 at (918.5, 2989.5), 1 frames after previous cover
- f278: ref 79045: 49 -> 43 at (906.5, 2986.5), 1 frames after previous cover
- f280: ref 79045: 43 -> 45 at (892.5, 2989.5), 2 frames after previous cover
- ... 37 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 38 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 41 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 43 (192), 45 (148) |
| 79045 | 355 (84..443) | 338 | 12 | 45 (174), 43 (147), 49 (16), 44 (1) |
| 79037 | 355 (86..445) | 338 | 16 | 49 (319), 45 (14), 44 (5) |
| 78897 | 345 (89..450) | 333 | 9 | 44 (333) |
| 78899 | 365 (91..455) | 359 | 6 | 47 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 51 (350), 54 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 54 (344) |
| 79102 | 371 (98..477) | 349 | 17 | 87 (290), 56 (59) |
| 79103 | 380 (99..481) | 373 | 6 | 56 (164), 62 (149), 87 (31), 55 (29) |
| 79105 | 379 (101..484) | 364 | 12 | 55 (187), 56 (153), 62 (24) |
| 79108 | 385 (104..492) | 375 | 8 | 63 (214), 55 (161) |
| 79110 | 388 (106..497) | 367 | 14 | 63 (167), 68 (128), 62 (57), 69 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 72 (198), 62 (98), 68 (47), 69 (29), 67 (1) |
| 79115 | 421 (111..531) | 399 | 18 | 68 (197), 69 (73), 72 (52), 62 (33), 76 (21), 78 (19), 67 (4) |
| 79116 | 411 (114..530) | 396 | 15 | 72 (112), 78 (82), 67 (70), 69 (70), 76 (61), 68 (1) |
| 79122 | 404 (118..532) | 397 | 5 | 69 (178), 67 (161), 68 (31), 76 (26), 78 (1) |
| 79132 | 391 (120..515) | 373 | 16 | 76 (175), 67 (156), 69 (35), 78 (7) |
| 79128 | 402 (124..527) | 386 | 12 | 78 (284), 76 (99), 81 (3) |
| 79134 | 407 (127..533) | 397 | 8 | 81 (349), 92 (35), 82 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 82 (326), 90 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 90 (322), 82 (49), 92 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 92 (324), 81 (48), 82 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/385/1007; tracks with internal gaps: 25; total internal gaps: 306; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 38 | 78..429 | 352 | 348 | 342 | 6 | 6 | 1 | 0 | 78896 |
| 41 | 82..434 | 353 | 350 | 345 | 5 | 5 | 1 | 0 | 78969 |
| 43 | 86..443 | 358 | 352 | 339 | 13 | 13 | 1 | 0 | 78971, 79045 |
| 44 | 86..450 | 365 | 349 | 339 | 10 | 9 | 2 | 0 | 78897, 79037, 79045 |
| 45 | 88..439 | 352 | 351 | 336 | 15 | 14 | 2 | 0 | 78971, 79037, 79045 |
| 47 | 91..455 | 365 | 365 | 359 | 6 | 6 | 1 | 0 | 78899 |
| 49 | 93..445 | 353 | 348 | 335 | 13 | 13 | 1 | 0 | 79037, 79045 |
| 51 | 96..461 | 366 | 364 | 350 | 14 | 14 | 1 | 0 | 79097 |
| 54 | 99..467 | 369 | 358 | 345 | 13 | 13 | 1 | 0 | 79097, 79098 |
| 55 | 100..492 | 393 | 388 | 377 | 11 | 11 | 1 | 0 | 79103, 79105, 79108 |
| 56 | 101..484 | 384 | 383 | 376 | 7 | 7 | 1 | 0 | 79102, 79103, 79105 |
| 62 | 105..481 | 377 | 374 | 361 | 13 | 11 | 2 | 0 | 79103, 79105, 79110, 79111, 79115 |
| 63 | 106..497 | 392 | 390 | 381 | 9 | 9 | 1 | 0 | 79108, 79110 |
| 67 | 110..515 | 406 | 400 | 392 | 8 | 8 | 1 | 0 | 79111, 79115, 79116, 79122, 79132 |
| 68 | 111..531 | 421 | 418 | 404 | 14 | 14 | 1 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 69 | 113..530 | 418 | 411 | 400 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 116..500 | 385 | 377 | 362 | 15 | 14 | 2 | 0 | 79111, 79115, 79116 |
| 76 | 120..527 | 408 | 402 | 382 | 20 | 20 | 1 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 78 | 122..532 | 411 | 409 | 393 | 16 | 14 | 2 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 81 | 126..537 | 412 | 412 | 400 | 12 | 12 | 1 | 0 | 79128, 79134, 79136 |
| 82 | 129..538 | 410 | 405 | 393 | 12 | 12 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 87 | 132..477 | 346 | 339 | 321 | 18 | 17 | 2 | 0 | 79102, 79103 |
| 90 | 134..542 | 409 | 408 | 394 | 14 | 14 | 1 | 0 | 79135, 79139 |
| 92 | 138..533 | 396 | 387 | 378 | 9 | 9 | 1 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9783; unmatched reference entries: 359; unmatched candidate entries: 1121
- identity switches: 100; fragmentation (coverage interruptions): 299; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 44 -> 49 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 51 -> 54 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 54 -> 51 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 67 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 67 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 62 -> 55 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 69 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 69 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 67 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 69 -> 68 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 68 -> 69 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 68 -> 69 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 69 -> 68 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 69 -> 68 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 68 -> 69 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 62 -> 68 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 68 -> 62 at (1675.5, 3017), 1 frames after previous cover
- f194: ref 79132: 76 -> 67 at (1692.5, 3016), 1 frames after previous cover
- f195: ref 79122: 67 -> 76 at (1681, 3019), 2 frames after previous cover
- f201: ref 79122: 76 -> 67 at (1641, 3015), 1 frames after previous cover
- f201: ref 79132: 67 -> 76 at (1646.5, 3013), 1 frames after previous cover
- f210: ref 79132: 76 -> 67 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 67 -> 76 at (1579, 3004.5), 1 frames after previous cover
- f218: ref 79102: 87 -> 56 at (1415.5, 3002), 4 frames after previous cover
- f218: ref 79103: 56 -> 87 at (1425.5, 3002), 1 frames after previous cover
- f225: ref 79037: 49 -> 45 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 45 -> 49 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 69 -> 62 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 67 -> 69 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 76 -> 67 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 45 -> 49 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 49 -> 45 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 62 -> 72 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 72 -> 69 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 69 -> 76 at (1483, 3006.5), 1 frames after previous cover
- f243: ref 79116: 69 -> 67 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 67 -> 69 at (1379, 2985.5), 2 frames after previous cover
- f245: ref 79116: 67 -> 76 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 76 -> 67 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 56 -> 87 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 87 -> 56 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 72 -> 76 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 76 -> 72 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 49 -> 45 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 45 -> 49 at (1021.5, 2989), 2 frames after previous cover
- f270: ref 79045: 49 -> 43 at (957.5, 2987.5), 1 frames after previous cover
- f271: ref 79037: 45 -> 49 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 43 -> 45 at (951.5, 2989.5), 1 frames after previous cover
- f273: ref 79045: 45 -> 49 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 76 -> 72 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 49 -> 45 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 72 -> 76 at (1184.5, 2981), 2 frames after previous cover
- f278: ref 79037: 45 -> 49 at (918.5, 2989.5), 1 frames after previous cover
- f278: ref 79045: 49 -> 43 at (906.5, 2986.5), 1 frames after previous cover
- ... 40 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 38 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 41 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 43 (192), 45 (148) |
| 79045 | 355 (84..443) | 339 | 11 | 45 (174), 43 (148), 49 (16), 44 (1) |
| 79037 | 355 (86..445) | 338 | 16 | 49 (319), 45 (14), 44 (5) |
| 78897 | 345 (89..450) | 334 | 8 | 44 (332), 41 (2) |
| 78899 | 365 (91..455) | 359 | 6 | 47 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 51 (350), 54 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 54 (344) |
| 79102 | 371 (98..477) | 348 | 17 | 87 (290), 56 (58) |
| 79103 | 380 (99..481) | 373 | 6 | 56 (165), 62 (149), 87 (30), 55 (29) |
| 79105 | 379 (101..484) | 365 | 11 | 55 (187), 56 (152), 62 (26) |
| 79108 | 385 (104..492) | 375 | 8 | 63 (214), 55 (161) |
| 79110 | 388 (106..497) | 367 | 14 | 63 (167), 68 (128), 62 (57), 69 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 72 (198), 62 (98), 68 (47), 69 (29), 67 (1) |
| 79115 | 421 (111..531) | 402 | 16 | 68 (197), 69 (74), 72 (55), 62 (33), 76 (21), 78 (19), 67 (3) |
| 79116 | 411 (114..530) | 396 | 15 | 72 (112), 78 (82), 67 (70), 69 (70), 76 (61), 68 (1) |
| 79122 | 404 (118..532) | 394 | 7 | 69 (178), 67 (155), 68 (32), 76 (29) |
| 79132 | 391 (120..515) | 374 | 15 | 76 (169), 67 (163), 69 (35), 78 (7) |
| 79128 | 402 (124..527) | 387 | 11 | 78 (284), 76 (98), 81 (3), 67 (2) |
| 79134 | 407 (127..533) | 397 | 8 | 81 (349), 92 (35), 82 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 82 (326), 90 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 90 (322), 82 (49), 92 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 92 (324), 81 (49), 82 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/414/1007; tracks with internal gaps: 25; total internal gaps: 401; longest internal gap: 14; tracks ending in coasting: 24 (trailing rows total 671)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 342 | 39 | 8 | 3 | 29 | 78896 |
| 41 | 82..463 | 382 | 382 | 347 | 35 | 8 | 14 | 13 | 78897, 78969 |
| 43 | 86..472 | 387 | 387 | 340 | 47 | 18 | 1 | 29 | 78971, 79045 |
| 44 | 86..479 | 394 | 394 | 338 | 56 | 24 | 2 | 31 | 78897, 79037, 79045 |
| 45 | 88..468 | 381 | 381 | 336 | 45 | 14 | 2 | 29 | 78971, 79037, 79045 |
| 47 | 91..484 | 394 | 394 | 359 | 35 | 6 | 1 | 29 | 78899 |
| 49 | 93..474 | 382 | 382 | 335 | 47 | 16 | 2 | 29 | 79037, 79045 |
| 51 | 96..490 | 395 | 395 | 350 | 45 | 15 | 2 | 29 | 79097 |
| 54 | 99..496 | 398 | 398 | 345 | 53 | 23 | 2 | 29 | 79097, 79098 |
| 55 | 100..521 | 422 | 422 | 377 | 45 | 16 | 1 | 29 | 79103, 79105, 79108 |
| 56 | 101..513 | 413 | 413 | 375 | 38 | 7 | 1 | 31 | 79102, 79103, 79105 |
| 62 | 105..510 | 406 | 406 | 363 | 43 | 13 | 4 | 26 | 79103, 79105, 79110, 79111, 79115 |
| 63 | 106..526 | 421 | 421 | 381 | 40 | 11 | 1 | 29 | 79108, 79110 |
| 67 | 110..544 | 435 | 435 | 394 | 41 | 15 | 10 | 17 | 79111, 79115, 79116, 79122, 79128, 79132 |
| 68 | 111..560 | 450 | 450 | 405 | 45 | 17 | 1 | 28 | 79110, 79111, 79115, 79116, 79122 |
| 69 | 113..559 | 447 | 447 | 401 | 46 | 17 | 2 | 28 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 116..529 | 414 | 414 | 365 | 49 | 18 | 2 | 29 | 79111, 79115, 79116 |
| 76 | 120..556 | 437 | 437 | 378 | 59 | 25 | 2 | 31 | 79115, 79116, 79122, 79128, 79132 |
| 78 | 122..561 | 440 | 440 | 392 | 48 | 15 | 2 | 31 | 79115, 79116, 79128, 79132 |
| 81 | 126..566 | 441 | 441 | 401 | 40 | 12 | 1 | 28 | 79128, 79134, 79136 |
| 82 | 129..567 | 439 | 439 | 392 | 47 | 17 | 1 | 30 | 79134, 79135, 79136, 79139 |
| 87 | 132..506 | 375 | 375 | 320 | 55 | 23 | 3 | 29 | 79102, 79103 |
| 90 | 134..571 | 438 | 438 | 394 | 44 | 15 | 1 | 29 | 79135, 79139 |
| 92 | 138..562 | 425 | 425 | 378 | 47 | 17 | 2 | 29 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9783; unmatched reference entries: 359; unmatched candidate entries: 1121
- identity switches: 100; fragmentation (coverage interruptions): 299; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f93: ref 79037: 44 -> 49 at (2118, 3034.5), 3 frames after previous cover
- f104: ref 79097: 51 -> 54 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 79097: 54 -> 51 at (2088, 3029), 1 frames after previous cover
- f111: ref 79111: 67 -> 68 at (2142, 3026.5), 1 frames after previous cover
- f116: ref 79115: 67 -> 72 at (2130, 3021), 3 frames after previous cover
- f129: ref 79103: 55 -> 56 at (1980.5, 3025), 1 frames after previous cover
- f129: ref 79105: 62 -> 55 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 69 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 68 -> 69 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 72 -> 68 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 67 -> 72 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 76 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 81 -> 78 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 78 -> 76 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 56 -> 87 at (1952.5, 3031), 4 frames after previous cover
- f157: ref 79111: 69 -> 68 at (1878.5, 3024.5), 2 frames after previous cover
- f157: ref 79115: 68 -> 69 at (1888.5, 3023.5), 1 frames after previous cover
- f160: ref 79111: 68 -> 69 at (1859.5, 3023.5), 1 frames after previous cover
- f160: ref 79115: 69 -> 68 at (1870.5, 3023), 3 frames after previous cover
- f162: ref 79111: 69 -> 68 at (1849.5, 3023), 1 frames after previous cover
- f162: ref 79115: 68 -> 69 at (1859, 3022), 2 frames after previous cover
- f190: ref 79110: 62 -> 68 at (1665.5, 3016), 3 frames after previous cover
- f190: ref 79111: 68 -> 62 at (1675.5, 3017), 1 frames after previous cover
- f194: ref 79132: 76 -> 67 at (1692.5, 3016), 1 frames after previous cover
- f195: ref 79122: 67 -> 76 at (1681, 3019), 2 frames after previous cover
- f201: ref 79122: 76 -> 67 at (1641, 3015), 1 frames after previous cover
- f201: ref 79132: 67 -> 76 at (1646.5, 3013), 1 frames after previous cover
- f210: ref 79132: 76 -> 67 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 67 -> 76 at (1579, 3004.5), 1 frames after previous cover
- f218: ref 79102: 87 -> 56 at (1415.5, 3002), 4 frames after previous cover
- f218: ref 79103: 56 -> 87 at (1425.5, 3002), 1 frames after previous cover
- f225: ref 79037: 49 -> 45 at (1257.5, 2993.5), 1 frames after previous cover
- f225: ref 79045: 45 -> 49 at (1245, 2992), 1 frames after previous cover
- f225: ref 79115: 69 -> 62 at (1470.5, 3004), 2 frames after previous cover
- f225: ref 79122: 67 -> 69 at (1489, 3005.5), 1 frames after previous cover
- f225: ref 79132: 76 -> 67 at (1489, 2997), 2 frames after previous cover
- f226: ref 79037: 45 -> 49 at (1253.5, 2991.5), 1 frames after previous cover
- f226: ref 79045: 49 -> 45 at (1238, 2990), 1 frames after previous cover
- f226: ref 79115: 62 -> 72 at (1465.5, 3005), 1 frames after previous cover
- f226: ref 79116: 72 -> 69 at (1473, 3001.5), 1 frames after previous cover
- f226: ref 79122: 69 -> 76 at (1483, 3006.5), 1 frames after previous cover
- f243: ref 79116: 69 -> 67 at (1369.5, 2994.5), 1 frames after previous cover
- f243: ref 79132: 67 -> 69 at (1379, 2985.5), 2 frames after previous cover
- f245: ref 79116: 67 -> 76 at (1358, 2997), 2 frames after previous cover
- f245: ref 79122: 76 -> 67 at (1366, 2994.5), 1 frames after previous cover
- f249: ref 79102: 56 -> 87 at (1230, 2984), 1 frames after previous cover
- f249: ref 79103: 87 -> 56 at (1243, 2988), 2 frames after previous cover
- f252: ref 79115: 72 -> 76 at (1309.5, 2993), 1 frames after previous cover
- f252: ref 79116: 76 -> 72 at (1316.5, 2991.5), 2 frames after previous cover
- f260: ref 79037: 49 -> 45 at (1036, 2986), 1 frames after previous cover
- f260: ref 79045: 45 -> 49 at (1021.5, 2989), 2 frames after previous cover
- f270: ref 79045: 49 -> 43 at (957.5, 2987.5), 1 frames after previous cover
- f271: ref 79037: 45 -> 49 at (965, 2987), 1 frames after previous cover
- f271: ref 79045: 43 -> 45 at (951.5, 2989.5), 1 frames after previous cover
- f273: ref 79045: 45 -> 49 at (938.5, 2989), 2 frames after previous cover
- f273: ref 79115: 76 -> 72 at (1183.5, 2984), 1 frames after previous cover
- f274: ref 79037: 49 -> 45 at (945, 2987.5), 2 frames after previous cover
- f274: ref 79116: 72 -> 76 at (1184.5, 2981), 2 frames after previous cover
- f278: ref 79037: 45 -> 49 at (918.5, 2989.5), 1 frames after previous cover
- f278: ref 79045: 49 -> 43 at (906.5, 2986.5), 1 frames after previous cover
- ... 40 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 31 | 0 (975) |
| 78896 | 350 (76..429) | 342 | 6 | 38 (342) |
| 78969 | 352 (80..434) | 345 | 5 | 41 (345) |
| 78971 | 352 (84..439) | 340 | 10 | 43 (192), 45 (148) |
| 79045 | 355 (84..443) | 339 | 11 | 45 (174), 43 (148), 49 (16), 44 (1) |
| 79037 | 355 (86..445) | 338 | 16 | 49 (319), 45 (14), 44 (5) |
| 78897 | 345 (89..450) | 334 | 8 | 44 (332), 41 (2) |
| 78899 | 365 (91..455) | 359 | 6 | 47 (359) |
| 79097 | 366 (94..461) | 351 | 13 | 51 (350), 54 (1) |
| 79098 | 360 (97..467) | 344 | 14 | 54 (344) |
| 79102 | 371 (98..477) | 348 | 17 | 87 (290), 56 (58) |
| 79103 | 380 (99..481) | 373 | 6 | 56 (165), 62 (149), 87 (30), 55 (29) |
| 79105 | 379 (101..484) | 365 | 11 | 55 (187), 56 (152), 62 (26) |
| 79108 | 385 (104..492) | 375 | 8 | 63 (214), 55 (161) |
| 79110 | 388 (106..497) | 367 | 14 | 63 (167), 68 (128), 62 (57), 69 (15) |
| 79111 | 386 (109..500) | 373 | 12 | 72 (198), 62 (98), 68 (47), 69 (29), 67 (1) |
| 79115 | 421 (111..531) | 402 | 16 | 68 (197), 69 (74), 72 (55), 62 (33), 76 (21), 78 (19), 67 (3) |
| 79116 | 411 (114..530) | 396 | 15 | 72 (112), 78 (82), 67 (70), 69 (70), 76 (61), 68 (1) |
| 79122 | 404 (118..532) | 394 | 7 | 69 (178), 67 (155), 68 (32), 76 (29) |
| 79132 | 391 (120..515) | 374 | 15 | 76 (169), 67 (163), 69 (35), 78 (7) |
| 79128 | 402 (124..527) | 387 | 11 | 78 (284), 76 (98), 81 (3), 67 (2) |
| 79134 | 407 (127..533) | 397 | 8 | 81 (349), 92 (35), 82 (13) |
| 79135 | 409 (129..542) | 398 | 11 | 82 (326), 90 (72) |
| 79139 | 406 (132..537) | 390 | 14 | 90 (322), 82 (49), 92 (19) |
| 79136 | 393 (136..538) | 377 | 14 | 92 (324), 81 (49), 82 (4) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 375/414/1007; tracks with internal gaps: 25; total internal gaps: 401; longest internal gap: 14; tracks ending in coasting: 24 (trailing rows total 671)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 975 | 32 | 31 | 2 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 342 | 39 | 8 | 3 | 29 | 78896 |
| 41 | 82..463 | 382 | 382 | 347 | 35 | 8 | 14 | 13 | 78897, 78969 |
| 43 | 86..472 | 387 | 387 | 340 | 47 | 18 | 1 | 29 | 78971, 79045 |
| 44 | 86..479 | 394 | 394 | 338 | 56 | 24 | 2 | 31 | 78897, 79037, 79045 |
| 45 | 88..468 | 381 | 381 | 336 | 45 | 14 | 2 | 29 | 78971, 79037, 79045 |
| 47 | 91..484 | 394 | 394 | 359 | 35 | 6 | 1 | 29 | 78899 |
| 49 | 93..474 | 382 | 382 | 335 | 47 | 16 | 2 | 29 | 79037, 79045 |
| 51 | 96..490 | 395 | 395 | 350 | 45 | 15 | 2 | 29 | 79097 |
| 54 | 99..496 | 398 | 398 | 345 | 53 | 23 | 2 | 29 | 79097, 79098 |
| 55 | 100..521 | 422 | 422 | 377 | 45 | 16 | 1 | 29 | 79103, 79105, 79108 |
| 56 | 101..513 | 413 | 413 | 375 | 38 | 7 | 1 | 31 | 79102, 79103, 79105 |
| 62 | 105..510 | 406 | 406 | 363 | 43 | 13 | 4 | 26 | 79103, 79105, 79110, 79111, 79115 |
| 63 | 106..526 | 421 | 421 | 381 | 40 | 11 | 1 | 29 | 79108, 79110 |
| 67 | 110..544 | 435 | 435 | 394 | 41 | 15 | 10 | 17 | 79111, 79115, 79116, 79122, 79128, 79132 |
| 68 | 111..560 | 450 | 450 | 405 | 45 | 17 | 1 | 28 | 79110, 79111, 79115, 79116, 79122 |
| 69 | 113..559 | 447 | 447 | 401 | 46 | 17 | 2 | 28 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 116..529 | 414 | 414 | 365 | 49 | 18 | 2 | 29 | 79111, 79115, 79116 |
| 76 | 120..556 | 437 | 437 | 378 | 59 | 25 | 2 | 31 | 79115, 79116, 79122, 79128, 79132 |
| 78 | 122..561 | 440 | 440 | 392 | 48 | 15 | 2 | 31 | 79115, 79116, 79128, 79132 |
| 81 | 126..566 | 441 | 441 | 401 | 40 | 12 | 1 | 28 | 79128, 79134, 79136 |
| 82 | 129..567 | 439 | 439 | 392 | 47 | 17 | 1 | 30 | 79134, 79135, 79136, 79139 |
| 87 | 132..506 | 375 | 375 | 320 | 55 | 23 | 3 | 29 | 79102, 79103 |
| 90 | 134..571 | 438 | 438 | 394 | 44 | 15 | 1 | 29 | 79135, 79139 |
| 92 | 138..562 | 425 | 425 | 378 | 47 | 17 | 2 | 29 | 79134, 79136, 79139 |
