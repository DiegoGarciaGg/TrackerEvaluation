# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=177b2ed2a976
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise3.0_fp0.0_seed2/tracks.csv sha256=bc63bbb9e663096c
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise3.0_fp0.0_seed2.csv sha256=177b2ed2a9762944
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise3.0_fp0.0_seed2
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
| observations | none | 4 | 10142 | 10092 | 0.373 | 0.430 | 0.324 | 2.19 | 0.354 | 0.155 | 2.41 | 126 | 2483.0 | 0.485 | 0.487 | 0.484 | 0.581 | 0.584 | 5896 | 4246 | 4196 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 10092 | 0.533 | 0.608 | 0.467 | 2.76 | 0.645 | 0.716 | 3.21 | 102 | 1275.0 | 0.725 | 0.726 | 0.723 | 0.861 | 0.865 | 8728 | 1414 | 1364 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10092 | 0.619 | 0.698 | 0.550 | 3.08 | 0.788 | 0.921 | 3.60 | 97 | 425.0 | 0.819 | 0.821 | 0.817 | 0.963 | 0.968 | 9767 | 375 | 325 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10092 | 0.709 | 0.789 | 0.636 | 3.46 | 0.848 | 0.976 | 3.92 | 78 | 164.0 | 0.866 | 0.869 | 0.864 | 0.989 | 0.994 | 10034 | 108 | 58 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10092 | 0.373 | 0.430 | 0.324 | 2.19 | 0.354 | 0.155 | 2.41 | 126 | 2483.0 | 0.485 | 0.487 | 0.484 | 0.581 | 0.584 | 5896 | 4246 | 4196 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 10092 | 0.533 | 0.608 | 0.467 | 2.76 | 0.645 | 0.716 | 3.21 | 102 | 1275.0 | 0.725 | 0.726 | 0.723 | 0.861 | 0.865 | 8728 | 1414 | 1364 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10092 | 0.619 | 0.698 | 0.550 | 3.08 | 0.788 | 0.921 | 3.60 | 97 | 425.0 | 0.819 | 0.821 | 0.817 | 0.963 | 0.968 | 9767 | 375 | 325 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10092 | 0.709 | 0.789 | 0.636 | 3.46 | 0.848 | 0.976 | 3.92 | 78 | 164.0 | 0.866 | 0.869 | 0.864 | 0.989 | 0.994 | 10034 | 108 | 58 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10908 | 0.351 | 0.403 | 0.305 | 2.19 | 0.336 | 0.076 | 2.41 | 136 | 2477.0 | 0.467 | 0.450 | 0.484 | 0.582 | 0.541 | 5905 | 4237 | 5003 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10908 | 0.498 | 0.567 | 0.438 | 2.76 | 0.605 | 0.636 | 3.22 | 107 | 1272.0 | 0.697 | 0.672 | 0.723 | 0.861 | 0.801 | 8732 | 1410 | 2176 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10908 | 0.578 | 0.649 | 0.515 | 3.08 | 0.735 | 0.843 | 3.60 | 87 | 423.0 | 0.788 | 0.760 | 0.817 | 0.963 | 0.896 | 9771 | 371 | 1137 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10908 | 0.661 | 0.732 | 0.596 | 3.46 | 0.789 | 0.898 | 3.90 | 62 | 157.0 | 0.834 | 0.805 | 0.866 | 0.990 | 0.921 | 10041 | 101 | 867 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10908 | 0.351 | 0.403 | 0.305 | 2.19 | 0.336 | 0.076 | 2.41 | 136 | 2477.0 | 0.467 | 0.450 | 0.484 | 0.582 | 0.541 | 5905 | 4237 | 5003 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10908 | 0.498 | 0.567 | 0.438 | 2.76 | 0.605 | 0.636 | 3.22 | 107 | 1272.0 | 0.697 | 0.672 | 0.723 | 0.861 | 0.801 | 8732 | 1410 | 2176 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10908 | 0.578 | 0.649 | 0.515 | 3.08 | 0.735 | 0.843 | 3.60 | 87 | 423.0 | 0.788 | 0.760 | 0.817 | 0.963 | 0.896 | 9771 | 371 | 1137 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10908 | 0.661 | 0.732 | 0.596 | 3.46 | 0.789 | 0.898 | 3.90 | 62 | 157.0 | 0.834 | 0.805 | 0.866 | 0.990 | 0.921 | 10041 | 101 | 867 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9767; unmatched reference entries: 375; unmatched candidate entries: 325
- identity switches: 97; fragmentation (coverage interruptions): 319; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 5 -> 7 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 8 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 3 -> 5 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 5 -> 3 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 11 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 10 -> 11 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 11 -> 10 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 11 -> 10 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 10 -> 11 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 11 -> 10 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 10 -> 11 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 7 -> 3 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 3 -> 7 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 3 -> 7 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 7 -> 3 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 11 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 14 -> 11 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 13 -> 14 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 15 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 17 -> 15 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 17 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 18 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 18 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 12 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 15 -> 17 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 17 -> 15 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 17 -> 15 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 15 -> 17 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 13 -> 15 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 15 -> 13 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 16 -> 19 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 19 -> 16 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 14 -> 15 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 15 -> 14 at (1559.5, 3007), 1 frames after previous cover
- f210: ref 79132: 16 -> 19 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79115: 13 -> 17 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 17 -> 13 at (1564, 3007.5), 1 frames after previous cover
- f211: ref 79132: 19 -> 16 at (1579, 3004.5), 1 frames after previous cover
- f220: ref 79116: 13 -> 19 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 19 -> 13 at (1521, 3009), 1 frames after previous cover
- f225: ref 79108: 11 -> 15 at (1436, 3000), 1 frames after previous cover
- f225: ref 79110: 15 -> 14 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79108: 15 -> 11 at (1429.5, 2998), 1 frames after previous cover
- f226: ref 79110: 14 -> 15 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 7 -> 3 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 3 -> 7 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 17 -> 19 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 19 -> 17 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 15 -> 14 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 14 -> 15 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 15 -> 19 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 19 -> 15 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 17 -> 15 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 15 -> 17 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 15 -> 13 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 13 -> 15 at (1307, 2993), 1 frames after previous cover
- ... 37 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 0 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 1 (335) |
| 78969 | 352 (80..434) | 342 | 8 | 2 (342) |
| 78971 | 352 (84..439) | 335 | 15 | 7 (163), 5 (159), 3 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 5 (175), 3 (129), 7 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 3 (195), 7 (140), 4 (3), 5 (2) |
| 78897 | 345 (89..450) | 338 | 7 | 6 (336), 4 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 4 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 9 (350), 8 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 8 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 12 (356), 11 (1) |
| 79103 | 380 (99..481) | 359 | 20 | 10 (354), 11 (5) |
| 79105 | 379 (101..484) | 362 | 16 | 22 (336), 11 (20), 10 (5), 12 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 11 (349), 14 (21), 15 (1) |
| 79110 | 388 (106..497) | 375 | 12 | 14 (325), 15 (30), 13 (20) |
| 79111 | 386 (109..500) | 377 | 7 | 19 (241), 15 (62), 13 (39), 14 (35) |
| 79115 | 421 (111..531) | 390 | 23 | 15 (264), 17 (63), 13 (56), 19 (6), 16 (1) |
| 79116 | 411 (114..530) | 401 | 10 | 16 (174), 17 (174), 15 (20), 19 (20), 13 (13) |
| 79122 | 404 (118..532) | 386 | 14 | 13 (268), 16 (69), 15 (25), 19 (24) |
| 79132 | 391 (120..515) | 381 | 10 | 16 (156), 18 (89), 19 (71), 17 (64), 15 (1) |
| 79128 | 402 (124..527) | 391 | 9 | 18 (297), 17 (91), 20 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 20 (349), 23 (44) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (396), 23 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 23 (334), 20 (50), 24 (12) |
| 79136 | 393 (136..538) | 380 | 10 | 24 (367), 23 (11), 21 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 347/382/1007; tracks with internal gaps: 25; total internal gaps: 313; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 335 | 13 | 13 | 1 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 342 | 8 | 8 | 1 | 0 | 78969 |
| 3 | 86..445 | 360 | 354 | 337 | 17 | 16 | 2 | 0 | 78971, 79037, 79045 |
| 4 | 86..455 | 370 | 370 | 359 | 11 | 10 | 2 | 0 | 78897, 78899, 79037 |
| 5 | 88..443 | 356 | 349 | 336 | 13 | 13 | 1 | 0 | 78971, 79037, 79045 |
| 6 | 91..450 | 360 | 343 | 336 | 7 | 7 | 1 | 0 | 78897 |
| 7 | 93..439 | 347 | 346 | 331 | 15 | 14 | 2 | 0 | 78971, 79037, 79045 |
| 8 | 96..467 | 372 | 361 | 349 | 12 | 12 | 1 | 0 | 79097, 79098 |
| 9 | 99..461 | 363 | 361 | 350 | 11 | 10 | 2 | 0 | 79097 |
| 10 | 100..481 | 382 | 378 | 359 | 19 | 19 | 1 | 0 | 79103, 79105 |
| 11 | 101..492 | 392 | 387 | 375 | 12 | 11 | 2 | 0 | 79102, 79103, 79105, 79108 |
| 12 | 103..477 | 375 | 367 | 357 | 10 | 10 | 1 | 0 | 79102, 79105 |
| 13 | 106..532 | 427 | 417 | 396 | 21 | 20 | 2 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 14 | 108..497 | 390 | 388 | 381 | 7 | 7 | 1 | 0 | 79108, 79110, 79111 |
| 15 | 111..531 | 421 | 420 | 403 | 17 | 15 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 113..530 | 418 | 411 | 400 | 11 | 11 | 1 | 0 | 79115, 79116, 79122, 79132 |
| 17 | 116..527 | 412 | 405 | 392 | 13 | 12 | 2 | 0 | 79115, 79116, 79128, 79132 |
| 18 | 120..515 | 396 | 394 | 386 | 8 | 8 | 1 | 0 | 79128, 79132 |
| 19 | 122..500 | 379 | 375 | 362 | 13 | 13 | 1 | 0 | 79111, 79115, 79116, 79122, 79132 |
| 20 | 126..537 | 412 | 412 | 402 | 10 | 9 | 2 | 0 | 79128, 79134, 79139 |
| 21 | 129..542 | 414 | 409 | 398 | 11 | 11 | 1 | 0 | 79135, 79136 |
| 22 | 132..484 | 353 | 349 | 336 | 13 | 13 | 1 | 0 | 79105 |
| 23 | 134..533 | 400 | 400 | 390 | 10 | 9 | 2 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 138..538 | 401 | 391 | 379 | 12 | 11 | 2 | 0 | 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9767; unmatched reference entries: 375; unmatched candidate entries: 325
- identity switches: 97; fragmentation (coverage interruptions): 319; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 5 -> 7 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 8 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 3 -> 5 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 5 -> 3 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 11 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 10 -> 11 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 11 -> 10 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 11 -> 10 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 10 -> 11 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 11 -> 10 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 10 -> 11 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 7 -> 3 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 3 -> 7 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 3 -> 7 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 7 -> 3 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 11 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 14 -> 11 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 13 -> 14 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 15 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 17 -> 15 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 17 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 18 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 18 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 12 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 15 -> 17 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 17 -> 15 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 17 -> 15 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 15 -> 17 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 13 -> 15 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 15 -> 13 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 16 -> 19 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 19 -> 16 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 14 -> 15 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 15 -> 14 at (1559.5, 3007), 1 frames after previous cover
- f210: ref 79132: 16 -> 19 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79115: 13 -> 17 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 17 -> 13 at (1564, 3007.5), 1 frames after previous cover
- f211: ref 79132: 19 -> 16 at (1579, 3004.5), 1 frames after previous cover
- f220: ref 79116: 13 -> 19 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 19 -> 13 at (1521, 3009), 1 frames after previous cover
- f225: ref 79108: 11 -> 15 at (1436, 3000), 1 frames after previous cover
- f225: ref 79110: 15 -> 14 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79108: 15 -> 11 at (1429.5, 2998), 1 frames after previous cover
- f226: ref 79110: 14 -> 15 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 7 -> 3 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 3 -> 7 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 17 -> 19 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 19 -> 17 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 15 -> 14 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 14 -> 15 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 15 -> 19 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 19 -> 15 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 17 -> 15 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 15 -> 17 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 15 -> 13 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 13 -> 15 at (1307, 2993), 1 frames after previous cover
- ... 37 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 0 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 1 (335) |
| 78969 | 352 (80..434) | 342 | 8 | 2 (342) |
| 78971 | 352 (84..439) | 335 | 15 | 7 (163), 5 (159), 3 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 5 (175), 3 (129), 7 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 3 (195), 7 (140), 4 (3), 5 (2) |
| 78897 | 345 (89..450) | 338 | 7 | 6 (336), 4 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 4 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 9 (350), 8 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 8 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 12 (356), 11 (1) |
| 79103 | 380 (99..481) | 359 | 20 | 10 (354), 11 (5) |
| 79105 | 379 (101..484) | 362 | 16 | 22 (336), 11 (20), 10 (5), 12 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 11 (349), 14 (21), 15 (1) |
| 79110 | 388 (106..497) | 375 | 12 | 14 (325), 15 (30), 13 (20) |
| 79111 | 386 (109..500) | 377 | 7 | 19 (241), 15 (62), 13 (39), 14 (35) |
| 79115 | 421 (111..531) | 390 | 23 | 15 (264), 17 (63), 13 (56), 19 (6), 16 (1) |
| 79116 | 411 (114..530) | 401 | 10 | 16 (174), 17 (174), 15 (20), 19 (20), 13 (13) |
| 79122 | 404 (118..532) | 386 | 14 | 13 (268), 16 (69), 15 (25), 19 (24) |
| 79132 | 391 (120..515) | 381 | 10 | 16 (156), 18 (89), 19 (71), 17 (64), 15 (1) |
| 79128 | 402 (124..527) | 391 | 9 | 18 (297), 17 (91), 20 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 20 (349), 23 (44) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (396), 23 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 23 (334), 20 (50), 24 (12) |
| 79136 | 393 (136..538) | 380 | 10 | 24 (367), 23 (11), 21 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 347/382/1007; tracks with internal gaps: 25; total internal gaps: 313; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 1 | 78..429 | 352 | 348 | 335 | 13 | 13 | 1 | 0 | 78896 |
| 2 | 82..434 | 353 | 350 | 342 | 8 | 8 | 1 | 0 | 78969 |
| 3 | 86..445 | 360 | 354 | 337 | 17 | 16 | 2 | 0 | 78971, 79037, 79045 |
| 4 | 86..455 | 370 | 370 | 359 | 11 | 10 | 2 | 0 | 78897, 78899, 79037 |
| 5 | 88..443 | 356 | 349 | 336 | 13 | 13 | 1 | 0 | 78971, 79037, 79045 |
| 6 | 91..450 | 360 | 343 | 336 | 7 | 7 | 1 | 0 | 78897 |
| 7 | 93..439 | 347 | 346 | 331 | 15 | 14 | 2 | 0 | 78971, 79037, 79045 |
| 8 | 96..467 | 372 | 361 | 349 | 12 | 12 | 1 | 0 | 79097, 79098 |
| 9 | 99..461 | 363 | 361 | 350 | 11 | 10 | 2 | 0 | 79097 |
| 10 | 100..481 | 382 | 378 | 359 | 19 | 19 | 1 | 0 | 79103, 79105 |
| 11 | 101..492 | 392 | 387 | 375 | 12 | 11 | 2 | 0 | 79102, 79103, 79105, 79108 |
| 12 | 103..477 | 375 | 367 | 357 | 10 | 10 | 1 | 0 | 79102, 79105 |
| 13 | 106..532 | 427 | 417 | 396 | 21 | 20 | 2 | 0 | 79110, 79111, 79115, 79116, 79122 |
| 14 | 108..497 | 390 | 388 | 381 | 7 | 7 | 1 | 0 | 79108, 79110, 79111 |
| 15 | 111..531 | 421 | 420 | 403 | 17 | 15 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 113..530 | 418 | 411 | 400 | 11 | 11 | 1 | 0 | 79115, 79116, 79122, 79132 |
| 17 | 116..527 | 412 | 405 | 392 | 13 | 12 | 2 | 0 | 79115, 79116, 79128, 79132 |
| 18 | 120..515 | 396 | 394 | 386 | 8 | 8 | 1 | 0 | 79128, 79132 |
| 19 | 122..500 | 379 | 375 | 362 | 13 | 13 | 1 | 0 | 79111, 79115, 79116, 79122, 79132 |
| 20 | 126..537 | 412 | 412 | 402 | 10 | 9 | 2 | 0 | 79128, 79134, 79139 |
| 21 | 129..542 | 414 | 409 | 398 | 11 | 11 | 1 | 0 | 79135, 79136 |
| 22 | 132..484 | 353 | 349 | 336 | 13 | 13 | 1 | 0 | 79105 |
| 23 | 134..533 | 400 | 400 | 390 | 10 | 9 | 2 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 138..538 | 401 | 391 | 379 | 12 | 11 | 2 | 0 | 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9771; unmatched reference entries: 371; unmatched candidate entries: 1137
- identity switches: 87; fragmentation (coverage interruptions): 317; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 5 -> 7 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 8 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 3 -> 5 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 5 -> 3 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 11 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 10 -> 11 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 11 -> 10 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 11 -> 10 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 10 -> 11 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 11 -> 10 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 10 -> 11 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 7 -> 3 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 3 -> 7 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 3 -> 7 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 7 -> 3 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 11 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 14 -> 11 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 13 -> 14 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 15 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 17 -> 15 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 17 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 18 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 18 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 12 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 15 -> 17 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 17 -> 15 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 17 -> 15 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 15 -> 17 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 13 -> 15 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 15 -> 13 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 16 -> 19 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 19 -> 16 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 14 -> 15 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 15 -> 14 at (1559.5, 3007), 1 frames after previous cover
- f211: ref 79115: 13 -> 17 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 17 -> 13 at (1564, 3007.5), 1 frames after previous cover
- f216: ref 79103: 10 -> 12 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79103: 12 -> 10 at (1432.5, 3002), 1 frames after previous cover
- f220: ref 79116: 13 -> 19 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 19 -> 13 at (1521, 3009), 1 frames after previous cover
- f225: ref 79110: 15 -> 14 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79110: 14 -> 15 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 7 -> 3 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 3 -> 7 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 17 -> 19 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 19 -> 17 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 15 -> 14 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 14 -> 15 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 15 -> 19 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 19 -> 15 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 17 -> 15 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 15 -> 17 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 15 -> 13 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 13 -> 15 at (1307, 2993), 1 frames after previous cover
- f264: ref 79122: 15 -> 16 at (1253.5, 2987), 1 frames after previous cover
- f264: ref 79132: 16 -> 15 at (1251, 2979.5), 2 frames after previous cover
- ... 27 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 0 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 1 (335) |
| 78969 | 352 (80..434) | 342 | 8 | 2 (342) |
| 78971 | 352 (84..439) | 335 | 15 | 7 (163), 5 (159), 3 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 5 (175), 3 (129), 7 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 3 (195), 7 (140), 4 (3), 5 (2) |
| 78897 | 345 (89..450) | 338 | 7 | 6 (336), 4 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 4 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 9 (350), 8 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 8 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 12 (356), 11 (1) |
| 79103 | 380 (99..481) | 360 | 19 | 10 (354), 11 (5), 12 (1) |
| 79105 | 379 (101..484) | 362 | 16 | 22 (336), 11 (20), 10 (5), 12 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 11 (350), 14 (21) |
| 79110 | 388 (106..497) | 375 | 12 | 14 (325), 15 (30), 13 (20) |
| 79111 | 386 (109..500) | 377 | 7 | 19 (241), 15 (62), 13 (39), 14 (35) |
| 79115 | 421 (111..531) | 393 | 22 | 15 (264), 17 (70), 13 (52), 19 (6), 16 (1) |
| 79116 | 411 (114..530) | 401 | 10 | 16 (174), 17 (169), 15 (20), 19 (20), 13 (18) |
| 79122 | 404 (118..532) | 386 | 14 | 13 (268), 16 (69), 15 (25), 19 (24) |
| 79132 | 391 (120..515) | 381 | 10 | 16 (157), 18 (89), 19 (70), 17 (64), 15 (1) |
| 79128 | 402 (124..527) | 391 | 9 | 18 (297), 17 (91), 20 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 20 (349), 23 (44) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (396), 23 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 23 (334), 20 (50), 24 (12) |
| 79136 | 393 (136..538) | 380 | 10 | 24 (367), 23 (11), 21 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 376/411/1007; tracks with internal gaps: 25; total internal gaps: 413; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 335 | 46 | 15 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 342 | 40 | 10 | 2 | 29 | 78969 |
| 3 | 86..474 | 389 | 389 | 337 | 52 | 20 | 2 | 29 | 78971, 79037, 79045 |
| 4 | 86..484 | 399 | 399 | 359 | 40 | 10 | 2 | 29 | 78897, 78899, 79037 |
| 5 | 88..472 | 385 | 385 | 336 | 49 | 20 | 1 | 29 | 78971, 79037, 79045 |
| 6 | 91..479 | 389 | 389 | 336 | 53 | 24 | 1 | 29 | 78897 |
| 7 | 93..468 | 376 | 376 | 331 | 45 | 15 | 2 | 29 | 78971, 79037, 79045 |
| 8 | 96..496 | 401 | 401 | 349 | 52 | 22 | 2 | 29 | 79097, 79098 |
| 9 | 99..490 | 392 | 392 | 350 | 42 | 12 | 2 | 29 | 79097 |
| 10 | 100..510 | 411 | 411 | 359 | 52 | 22 | 2 | 29 | 79103, 79105 |
| 11 | 101..521 | 421 | 421 | 376 | 45 | 15 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 12 | 103..506 | 404 | 404 | 358 | 46 | 16 | 2 | 29 | 79102, 79103, 79105 |
| 13 | 106..561 | 456 | 456 | 397 | 59 | 28 | 2 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 14 | 108..526 | 419 | 419 | 381 | 38 | 9 | 1 | 29 | 79108, 79110, 79111 |
| 15 | 111..560 | 450 | 450 | 402 | 48 | 15 | 3 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 113..559 | 447 | 447 | 401 | 46 | 17 | 1 | 29 | 79115, 79116, 79122, 79132 |
| 17 | 116..556 | 441 | 441 | 394 | 47 | 16 | 2 | 29 | 79115, 79116, 79128, 79132 |
| 18 | 120..544 | 425 | 425 | 386 | 39 | 10 | 1 | 29 | 79128, 79132 |
| 19 | 122..529 | 408 | 408 | 361 | 47 | 16 | 2 | 29 | 79111, 79115, 79116, 79122, 79132 |
| 20 | 126..566 | 441 | 441 | 402 | 39 | 9 | 2 | 29 | 79128, 79134, 79139 |
| 21 | 129..571 | 443 | 443 | 398 | 45 | 16 | 1 | 29 | 79135, 79136 |
| 22 | 132..513 | 382 | 382 | 336 | 46 | 16 | 2 | 29 | 79105 |
| 23 | 134..562 | 429 | 429 | 390 | 39 | 9 | 2 | 29 | 79134, 79135, 79136, 79139 |
| 24 | 138..567 | 430 | 430 | 379 | 51 | 20 | 2 | 29 | 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9771; unmatched reference entries: 371; unmatched candidate entries: 1137
- identity switches: 87; fragmentation (coverage interruptions): 317; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 5 -> 7 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 8 -> 9 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 3 -> 5 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 5 -> 3 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 11 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 10 -> 11 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 11 -> 10 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 11 -> 10 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 10 -> 11 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 11 -> 10 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 10 -> 11 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 16 -> 17 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 7 -> 3 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 3 -> 7 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 3 -> 7 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 7 -> 3 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 11 -> 12 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 14 -> 11 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 13 -> 14 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 15 -> 13 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 17 -> 15 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 16 -> 17 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 19 -> 16 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 20 -> 18 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 18 -> 19 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 12 -> 22 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 15 -> 17 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 17 -> 15 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 17 -> 15 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 15 -> 17 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 13 -> 15 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 15 -> 13 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 16 -> 19 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 19 -> 16 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 14 -> 15 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 15 -> 14 at (1559.5, 3007), 1 frames after previous cover
- f211: ref 79115: 13 -> 17 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 17 -> 13 at (1564, 3007.5), 1 frames after previous cover
- f216: ref 79103: 10 -> 12 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79103: 12 -> 10 at (1432.5, 3002), 1 frames after previous cover
- f220: ref 79116: 13 -> 19 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 19 -> 13 at (1521, 3009), 1 frames after previous cover
- f225: ref 79110: 15 -> 14 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79110: 14 -> 15 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 7 -> 3 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 3 -> 7 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 17 -> 19 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 19 -> 17 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 15 -> 14 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 14 -> 15 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 15 -> 19 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 19 -> 15 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 17 -> 15 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 15 -> 17 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 15 -> 13 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 13 -> 15 at (1307, 2993), 1 frames after previous cover
- f264: ref 79122: 15 -> 16 at (1253.5, 2987), 1 frames after previous cover
- f264: ref 79132: 16 -> 15 at (1251, 2979.5), 2 frames after previous cover
- ... 27 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 0 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 1 (335) |
| 78969 | 352 (80..434) | 342 | 8 | 2 (342) |
| 78971 | 352 (84..439) | 335 | 15 | 7 (163), 5 (159), 3 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 5 (175), 3 (129), 7 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 3 (195), 7 (140), 4 (3), 5 (2) |
| 78897 | 345 (89..450) | 338 | 7 | 6 (336), 4 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 4 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 9 (350), 8 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 8 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 12 (356), 11 (1) |
| 79103 | 380 (99..481) | 360 | 19 | 10 (354), 11 (5), 12 (1) |
| 79105 | 379 (101..484) | 362 | 16 | 22 (336), 11 (20), 10 (5), 12 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 11 (350), 14 (21) |
| 79110 | 388 (106..497) | 375 | 12 | 14 (325), 15 (30), 13 (20) |
| 79111 | 386 (109..500) | 377 | 7 | 19 (241), 15 (62), 13 (39), 14 (35) |
| 79115 | 421 (111..531) | 393 | 22 | 15 (264), 17 (70), 13 (52), 19 (6), 16 (1) |
| 79116 | 411 (114..530) | 401 | 10 | 16 (174), 17 (169), 15 (20), 19 (20), 13 (18) |
| 79122 | 404 (118..532) | 386 | 14 | 13 (268), 16 (69), 15 (25), 19 (24) |
| 79132 | 391 (120..515) | 381 | 10 | 16 (157), 18 (89), 19 (70), 17 (64), 15 (1) |
| 79128 | 402 (124..527) | 391 | 9 | 18 (297), 17 (91), 20 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 20 (349), 23 (44) |
| 79135 | 409 (129..542) | 397 | 12 | 21 (396), 23 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 23 (334), 20 (50), 24 (12) |
| 79136 | 393 (136..538) | 380 | 10 | 24 (367), 23 (11), 21 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 376/411/1007; tracks with internal gaps: 25; total internal gaps: 413; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 696)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 335 | 46 | 15 | 3 | 29 | 78896 |
| 2 | 82..463 | 382 | 382 | 342 | 40 | 10 | 2 | 29 | 78969 |
| 3 | 86..474 | 389 | 389 | 337 | 52 | 20 | 2 | 29 | 78971, 79037, 79045 |
| 4 | 86..484 | 399 | 399 | 359 | 40 | 10 | 2 | 29 | 78897, 78899, 79037 |
| 5 | 88..472 | 385 | 385 | 336 | 49 | 20 | 1 | 29 | 78971, 79037, 79045 |
| 6 | 91..479 | 389 | 389 | 336 | 53 | 24 | 1 | 29 | 78897 |
| 7 | 93..468 | 376 | 376 | 331 | 45 | 15 | 2 | 29 | 78971, 79037, 79045 |
| 8 | 96..496 | 401 | 401 | 349 | 52 | 22 | 2 | 29 | 79097, 79098 |
| 9 | 99..490 | 392 | 392 | 350 | 42 | 12 | 2 | 29 | 79097 |
| 10 | 100..510 | 411 | 411 | 359 | 52 | 22 | 2 | 29 | 79103, 79105 |
| 11 | 101..521 | 421 | 421 | 376 | 45 | 15 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 12 | 103..506 | 404 | 404 | 358 | 46 | 16 | 2 | 29 | 79102, 79103, 79105 |
| 13 | 106..561 | 456 | 456 | 397 | 59 | 28 | 2 | 29 | 79110, 79111, 79115, 79116, 79122 |
| 14 | 108..526 | 419 | 419 | 381 | 38 | 9 | 1 | 29 | 79108, 79110, 79111 |
| 15 | 111..560 | 450 | 450 | 402 | 48 | 15 | 3 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 113..559 | 447 | 447 | 401 | 46 | 17 | 1 | 29 | 79115, 79116, 79122, 79132 |
| 17 | 116..556 | 441 | 441 | 394 | 47 | 16 | 2 | 29 | 79115, 79116, 79128, 79132 |
| 18 | 120..544 | 425 | 425 | 386 | 39 | 10 | 1 | 29 | 79128, 79132 |
| 19 | 122..529 | 408 | 408 | 361 | 47 | 16 | 2 | 29 | 79111, 79115, 79116, 79122, 79132 |
| 20 | 126..566 | 441 | 441 | 402 | 39 | 9 | 2 | 29 | 79128, 79134, 79139 |
| 21 | 129..571 | 443 | 443 | 398 | 45 | 16 | 1 | 29 | 79135, 79136 |
| 22 | 132..513 | 382 | 382 | 336 | 46 | 16 | 2 | 29 | 79105 |
| 23 | 134..562 | 429 | 429 | 390 | 39 | 9 | 2 | 29 | 79134, 79135, 79136, 79139 |
| 24 | 138..567 | 430 | 430 | 379 | 51 | 20 | 2 | 29 | 79136, 79139 |
