# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=71ed1c0ad2c7
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise3.0_fp0.5_seed2/tracks.csv sha256=ea43165ec7772c1a
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise3.0_fp0.5_seed2.csv sha256=71ed1c0ad2c74c56
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise3.0_fp0.5_seed2
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
| observations | none | 4 | 10142 | 10105 | 0.372 | 0.429 | 0.324 | 2.19 | 0.354 | 0.153 | 2.41 | 140 | 2483.0 | 0.482 | 0.483 | 0.481 | 0.581 | 0.583 | 5896 | 4246 | 4209 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 10105 | 0.533 | 0.605 | 0.469 | 2.76 | 0.643 | 0.712 | 3.21 | 131 | 1276.0 | 0.719 | 0.721 | 0.718 | 0.860 | 0.864 | 8727 | 1415 | 1378 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10105 | 0.620 | 0.694 | 0.555 | 3.09 | 0.787 | 0.917 | 3.60 | 125 | 427.0 | 0.813 | 0.815 | 0.812 | 0.963 | 0.966 | 9765 | 377 | 340 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10105 | 0.711 | 0.783 | 0.646 | 3.50 | 0.851 | 0.973 | 3.91 | 103 | 161.0 | 0.862 | 0.864 | 0.861 | 0.990 | 0.993 | 10037 | 105 | 68 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10105 | 0.372 | 0.429 | 0.324 | 2.19 | 0.354 | 0.153 | 2.41 | 140 | 2483.0 | 0.482 | 0.483 | 0.481 | 0.581 | 0.583 | 5896 | 4246 | 4209 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 10105 | 0.533 | 0.605 | 0.469 | 2.76 | 0.643 | 0.712 | 3.21 | 131 | 1276.0 | 0.719 | 0.721 | 0.718 | 0.860 | 0.864 | 8727 | 1415 | 1378 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10105 | 0.620 | 0.694 | 0.555 | 3.09 | 0.787 | 0.917 | 3.60 | 125 | 427.0 | 0.813 | 0.815 | 0.812 | 0.963 | 0.966 | 9765 | 377 | 340 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10105 | 0.711 | 0.783 | 0.646 | 3.50 | 0.851 | 0.973 | 3.91 | 103 | 161.0 | 0.862 | 0.864 | 0.861 | 0.990 | 0.993 | 10037 | 105 | 68 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 11044 | 0.348 | 0.398 | 0.305 | 2.19 | 0.334 | 0.061 | 2.41 | 150 | 2476.0 | 0.461 | 0.442 | 0.482 | 0.582 | 0.535 | 5907 | 4235 | 5137 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 11044 | 0.495 | 0.558 | 0.439 | 2.76 | 0.600 | 0.620 | 3.22 | 135 | 1272.0 | 0.688 | 0.660 | 0.718 | 0.861 | 0.791 | 8732 | 1410 | 2312 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 11044 | 0.576 | 0.639 | 0.519 | 3.09 | 0.729 | 0.827 | 3.60 | 111 | 424.0 | 0.778 | 0.746 | 0.813 | 0.963 | 0.885 | 9770 | 372 | 1274 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 11044 | 0.659 | 0.719 | 0.604 | 3.50 | 0.787 | 0.884 | 3.90 | 82 | 152.0 | 0.826 | 0.792 | 0.863 | 0.991 | 0.910 | 10046 | 96 | 998 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 11044 | 0.348 | 0.398 | 0.305 | 2.19 | 0.334 | 0.061 | 2.41 | 150 | 2476.0 | 0.461 | 0.442 | 0.482 | 0.582 | 0.535 | 5907 | 4235 | 5137 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 11044 | 0.495 | 0.558 | 0.439 | 2.76 | 0.600 | 0.620 | 3.22 | 135 | 1272.0 | 0.688 | 0.660 | 0.718 | 0.861 | 0.791 | 8732 | 1410 | 2312 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 11044 | 0.576 | 0.639 | 0.519 | 3.09 | 0.729 | 0.827 | 3.60 | 111 | 424.0 | 0.778 | 0.746 | 0.813 | 0.963 | 0.885 | 9770 | 372 | 1274 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 11044 | 0.659 | 0.719 | 0.604 | 3.50 | 0.787 | 0.884 | 3.90 | 82 | 152.0 | 0.826 | 0.792 | 0.863 | 0.991 | 0.910 | 10046 | 96 | 998 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 9765; unmatched reference entries: 377; unmatched candidate entries: 340
- identity switches: 125; fragmentation (coverage interruptions): 321; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 43 -> 45 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 43 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 45 -> 47 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 50 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 42 -> 45 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 45 -> 42 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 55 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 54 -> 55 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 55 -> 54 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 55 -> 54 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 54 -> 55 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 55 -> 54 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 54 -> 55 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 66 -> 67 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 47 -> 42 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 42 -> 47 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 42 -> 47 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 47 -> 42 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 62 -> 55 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 59 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 64 -> 59 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 67 -> 64 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 66 -> 67 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 71 -> 66 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 72 -> 68 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 68 -> 71 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 58 -> 77 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 64 -> 67 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 67 -> 64 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 67 -> 64 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 64 -> 67 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 59 -> 64 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 64 -> 59 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 66 -> 71 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 71 -> 66 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 62 -> 64 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 64 -> 62 at (1559.5, 3007), 1 frames after previous cover
- f210: ref 79132: 66 -> 71 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79115: 59 -> 67 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 67 -> 59 at (1564, 3007.5), 1 frames after previous cover
- f211: ref 79132: 71 -> 66 at (1579, 3004.5), 1 frames after previous cover
- f220: ref 79116: 59 -> 71 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 71 -> 59 at (1521, 3009), 1 frames after previous cover
- f225: ref 79108: 55 -> 64 at (1436, 3000), 1 frames after previous cover
- f225: ref 79110: 64 -> 62 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79108: 64 -> 55 at (1429.5, 2998), 1 frames after previous cover
- f226: ref 79110: 62 -> 64 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 47 -> 42 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 42 -> 47 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 67 -> 71 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 71 -> 67 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 64 -> 62 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 62 -> 64 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 64 -> 71 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 71 -> 64 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 67 -> 64 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 64 -> 67 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 64 -> 59 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 59 -> 64 at (1307, 2993), 1 frames after previous cover
- ... 65 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 1 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 38 (334), 40 (1) |
| 78969 | 352 (80..434) | 342 | 8 | 40 (341), 47 (1) |
| 78971 | 352 (84..439) | 335 | 15 | 47 (162), 45 (160), 42 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 45 (174), 42 (130), 47 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 42 (194), 47 (140), 43 (3), 45 (2), 46 (1) |
| 78897 | 345 (89..450) | 338 | 7 | 46 (336), 43 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 43 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 52 (350), 50 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 50 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 58 (356), 55 (1) |
| 79103 | 380 (99..481) | 359 | 20 | 54 (354), 55 (5) |
| 79105 | 379 (101..484) | 362 | 16 | 77 (336), 55 (20), 54 (5), 58 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 55 (348), 62 (22), 64 (1) |
| 79110 | 388 (106..497) | 374 | 13 | 62 (322), 64 (30), 59 (20), 71 (1), 218 (1) |
| 79111 | 386 (109..500) | 376 | 8 | 71 (238), 64 (62), 59 (39), 62 (35), 218 (2) |
| 79115 | 421 (111..531) | 390 | 23 | 67 (286), 59 (44), 64 (41), 66 (13), 71 (6) |
| 79116 | 411 (114..530) | 402 | 9 | 59 (173), 64 (97), 67 (96), 71 (20), 66 (16) |
| 79122 | 404 (118..532) | 386 | 14 | 66 (292), 59 (45), 71 (24), 67 (14), 64 (11) |
| 79132 | 391 (120..515) | 380 | 11 | 68 (89), 59 (79), 66 (76), 71 (71), 64 (65) |
| 79128 | 402 (124..527) | 391 | 9 | 68 (297), 64 (91), 72 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 72 (348), 83 (44), 68 (1) |
| 79135 | 409 (129..542) | 397 | 12 | 75 (395), 72 (1), 83 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 83 (333), 72 (50), 86 (12), 75 (1) |
| 79136 | 393 (136..538) | 380 | 10 | 86 (366), 83 (12), 75 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 324 | 651..651 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 1/379/1007; tracks with internal gaps: 25; total internal gaps: 318; longest internal gap: 2; tracks ending in coasting: 3 (trailing rows total 9)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 38 | 78..429 | 352 | 348 | 334 | 14 | 14 | 1 | 0 | 78896 |
| 40 | 82..434 | 353 | 350 | 342 | 8 | 8 | 1 | 0 | 78896, 78969 |
| 42 | 86..445 | 360 | 354 | 337 | 17 | 16 | 2 | 0 | 78971, 79037, 79045 |
| 43 | 86..455 | 370 | 370 | 359 | 11 | 10 | 2 | 0 | 78897, 78899, 79037 |
| 45 | 88..443 | 356 | 349 | 336 | 13 | 13 | 1 | 0 | 78971, 79037, 79045 |
| 46 | 91..450 | 360 | 344 | 337 | 7 | 7 | 1 | 0 | 78897, 79037 |
| 47 | 93..439 | 347 | 346 | 331 | 15 | 14 | 2 | 0 | 78969, 78971, 79037, 79045 |
| 50 | 96..467 | 372 | 362 | 349 | 13 | 13 | 1 | 0 | 79097, 79098 |
| 52 | 99..461 | 363 | 361 | 350 | 11 | 10 | 2 | 0 | 79097 |
| 54 | 100..481 | 382 | 378 | 359 | 19 | 19 | 1 | 0 | 79103, 79105 |
| 55 | 101..492 | 392 | 387 | 374 | 13 | 12 | 2 | 0 | 79102, 79103, 79105, 79108 |
| 58 | 103..477 | 375 | 367 | 357 | 10 | 10 | 1 | 0 | 79102, 79105 |
| 59 | 106..530 | 425 | 417 | 400 | 17 | 16 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 62 | 108..497 | 390 | 386 | 379 | 7 | 7 | 1 | 0 | 79108, 79110, 79111 |
| 64 | 111..527 | 417 | 412 | 398 | 14 | 11 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 113..598 | 486 | 419 | 397 | 22 | 15 | 1 | 7 | 79115, 79116, 79122, 79132 |
| 67 | 116..531 | 416 | 413 | 396 | 17 | 16 | 2 | 0 | 79115, 79116, 79122 |
| 68 | 120..515 | 396 | 395 | 387 | 8 | 8 | 1 | 0 | 79128, 79132, 79134 |
| 71 | 122..500 | 379 | 373 | 360 | 13 | 13 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 126..537 | 412 | 412 | 402 | 10 | 9 | 2 | 0 | 79128, 79134, 79135, 79139 |
| 75 | 129..542 | 414 | 409 | 398 | 11 | 11 | 1 | 0 | 79135, 79136, 79139 |
| 77 | 132..484 | 353 | 349 | 336 | 13 | 13 | 1 | 0 | 79105 |
| 83 | 134..533 | 400 | 400 | 390 | 10 | 9 | 2 | 0 | 79134, 79135, 79136, 79139 |
| 86 | 138..538 | 401 | 392 | 378 | 14 | 13 | 2 | 0 | 79136, 79139 |
| 218 | 421..431 | 11 | 4 | 3 | 1 | 0 | 0 | 1 | 79110, 79111 |
| 324 | 651..651 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 9765; unmatched reference entries: 377; unmatched candidate entries: 340
- identity switches: 125; fragmentation (coverage interruptions): 321; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 43 -> 45 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 43 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 45 -> 47 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 50 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 42 -> 45 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 45 -> 42 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 55 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 54 -> 55 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 55 -> 54 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 55 -> 54 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 54 -> 55 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 55 -> 54 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 54 -> 55 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 66 -> 67 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 47 -> 42 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 42 -> 47 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 42 -> 47 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 47 -> 42 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 62 -> 55 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 59 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 64 -> 59 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 67 -> 64 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 66 -> 67 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 71 -> 66 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 72 -> 68 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 68 -> 71 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 58 -> 77 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 64 -> 67 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 67 -> 64 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 67 -> 64 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 64 -> 67 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 59 -> 64 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 64 -> 59 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 66 -> 71 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 71 -> 66 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 62 -> 64 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 64 -> 62 at (1559.5, 3007), 1 frames after previous cover
- f210: ref 79132: 66 -> 71 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79115: 59 -> 67 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 67 -> 59 at (1564, 3007.5), 1 frames after previous cover
- f211: ref 79132: 71 -> 66 at (1579, 3004.5), 1 frames after previous cover
- f220: ref 79116: 59 -> 71 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 71 -> 59 at (1521, 3009), 1 frames after previous cover
- f225: ref 79108: 55 -> 64 at (1436, 3000), 1 frames after previous cover
- f225: ref 79110: 64 -> 62 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79108: 64 -> 55 at (1429.5, 2998), 1 frames after previous cover
- f226: ref 79110: 62 -> 64 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 47 -> 42 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 42 -> 47 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 67 -> 71 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 71 -> 67 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 64 -> 62 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 62 -> 64 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 64 -> 71 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 71 -> 64 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 67 -> 64 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 64 -> 67 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 64 -> 59 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 59 -> 64 at (1307, 2993), 1 frames after previous cover
- ... 65 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 1 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 38 (334), 40 (1) |
| 78969 | 352 (80..434) | 342 | 8 | 40 (341), 47 (1) |
| 78971 | 352 (84..439) | 335 | 15 | 47 (162), 45 (160), 42 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 45 (174), 42 (130), 47 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 42 (194), 47 (140), 43 (3), 45 (2), 46 (1) |
| 78897 | 345 (89..450) | 338 | 7 | 46 (336), 43 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 43 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 52 (350), 50 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 50 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 58 (356), 55 (1) |
| 79103 | 380 (99..481) | 359 | 20 | 54 (354), 55 (5) |
| 79105 | 379 (101..484) | 362 | 16 | 77 (336), 55 (20), 54 (5), 58 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 55 (348), 62 (22), 64 (1) |
| 79110 | 388 (106..497) | 374 | 13 | 62 (322), 64 (30), 59 (20), 71 (1), 218 (1) |
| 79111 | 386 (109..500) | 376 | 8 | 71 (238), 64 (62), 59 (39), 62 (35), 218 (2) |
| 79115 | 421 (111..531) | 390 | 23 | 67 (286), 59 (44), 64 (41), 66 (13), 71 (6) |
| 79116 | 411 (114..530) | 402 | 9 | 59 (173), 64 (97), 67 (96), 71 (20), 66 (16) |
| 79122 | 404 (118..532) | 386 | 14 | 66 (292), 59 (45), 71 (24), 67 (14), 64 (11) |
| 79132 | 391 (120..515) | 380 | 11 | 68 (89), 59 (79), 66 (76), 71 (71), 64 (65) |
| 79128 | 402 (124..527) | 391 | 9 | 68 (297), 64 (91), 72 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 72 (348), 83 (44), 68 (1) |
| 79135 | 409 (129..542) | 397 | 12 | 75 (395), 72 (1), 83 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 83 (333), 72 (50), 86 (12), 75 (1) |
| 79136 | 393 (136..538) | 380 | 10 | 86 (366), 83 (12), 75 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 324 | 651..651 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 1/379/1007; tracks with internal gaps: 25; total internal gaps: 318; longest internal gap: 2; tracks ending in coasting: 3 (trailing rows total 9)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 38 | 78..429 | 352 | 348 | 334 | 14 | 14 | 1 | 0 | 78896 |
| 40 | 82..434 | 353 | 350 | 342 | 8 | 8 | 1 | 0 | 78896, 78969 |
| 42 | 86..445 | 360 | 354 | 337 | 17 | 16 | 2 | 0 | 78971, 79037, 79045 |
| 43 | 86..455 | 370 | 370 | 359 | 11 | 10 | 2 | 0 | 78897, 78899, 79037 |
| 45 | 88..443 | 356 | 349 | 336 | 13 | 13 | 1 | 0 | 78971, 79037, 79045 |
| 46 | 91..450 | 360 | 344 | 337 | 7 | 7 | 1 | 0 | 78897, 79037 |
| 47 | 93..439 | 347 | 346 | 331 | 15 | 14 | 2 | 0 | 78969, 78971, 79037, 79045 |
| 50 | 96..467 | 372 | 362 | 349 | 13 | 13 | 1 | 0 | 79097, 79098 |
| 52 | 99..461 | 363 | 361 | 350 | 11 | 10 | 2 | 0 | 79097 |
| 54 | 100..481 | 382 | 378 | 359 | 19 | 19 | 1 | 0 | 79103, 79105 |
| 55 | 101..492 | 392 | 387 | 374 | 13 | 12 | 2 | 0 | 79102, 79103, 79105, 79108 |
| 58 | 103..477 | 375 | 367 | 357 | 10 | 10 | 1 | 0 | 79102, 79105 |
| 59 | 106..530 | 425 | 417 | 400 | 17 | 16 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 62 | 108..497 | 390 | 386 | 379 | 7 | 7 | 1 | 0 | 79108, 79110, 79111 |
| 64 | 111..527 | 417 | 412 | 398 | 14 | 11 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 113..598 | 486 | 419 | 397 | 22 | 15 | 1 | 7 | 79115, 79116, 79122, 79132 |
| 67 | 116..531 | 416 | 413 | 396 | 17 | 16 | 2 | 0 | 79115, 79116, 79122 |
| 68 | 120..515 | 396 | 395 | 387 | 8 | 8 | 1 | 0 | 79128, 79132, 79134 |
| 71 | 122..500 | 379 | 373 | 360 | 13 | 13 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 126..537 | 412 | 412 | 402 | 10 | 9 | 2 | 0 | 79128, 79134, 79135, 79139 |
| 75 | 129..542 | 414 | 409 | 398 | 11 | 11 | 1 | 0 | 79135, 79136, 79139 |
| 77 | 132..484 | 353 | 349 | 336 | 13 | 13 | 1 | 0 | 79105 |
| 83 | 134..533 | 400 | 400 | 390 | 10 | 9 | 2 | 0 | 79134, 79135, 79136, 79139 |
| 86 | 138..538 | 401 | 392 | 378 | 14 | 13 | 2 | 0 | 79136, 79139 |
| 218 | 421..431 | 11 | 4 | 3 | 1 | 0 | 0 | 1 | 79110, 79111 |
| 324 | 651..651 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 9770; unmatched reference entries: 372; unmatched candidate entries: 1274
- identity switches: 111; fragmentation (coverage interruptions): 318; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 43 -> 45 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 43 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 45 -> 47 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 50 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 42 -> 45 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 45 -> 42 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 55 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 54 -> 55 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 55 -> 54 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 55 -> 54 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 54 -> 55 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 55 -> 54 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 54 -> 55 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 66 -> 67 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 47 -> 42 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 42 -> 47 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 42 -> 47 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 47 -> 42 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 62 -> 55 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 59 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 64 -> 59 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 67 -> 64 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 66 -> 67 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 71 -> 66 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 72 -> 68 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 68 -> 71 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 58 -> 77 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 64 -> 67 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 67 -> 64 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 67 -> 64 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 64 -> 67 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 59 -> 64 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 64 -> 59 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 66 -> 71 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 71 -> 66 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 62 -> 64 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 64 -> 62 at (1559.5, 3007), 1 frames after previous cover
- f211: ref 79115: 59 -> 67 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 67 -> 59 at (1564, 3007.5), 1 frames after previous cover
- f216: ref 79103: 54 -> 58 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79103: 58 -> 54 at (1432.5, 3002), 1 frames after previous cover
- f220: ref 79116: 59 -> 71 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 71 -> 59 at (1521, 3009), 1 frames after previous cover
- f225: ref 79110: 64 -> 62 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79110: 62 -> 64 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 47 -> 42 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 42 -> 47 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 67 -> 71 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 71 -> 67 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 64 -> 62 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 62 -> 64 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 64 -> 71 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 71 -> 64 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 67 -> 64 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 64 -> 67 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 64 -> 59 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 59 -> 64 at (1307, 2993), 1 frames after previous cover
- f264: ref 79122: 64 -> 66 at (1253.5, 2987), 1 frames after previous cover
- f264: ref 79132: 66 -> 64 at (1251, 2979.5), 2 frames after previous cover
- ... 51 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 1 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 38 (334), 40 (1) |
| 78969 | 352 (80..434) | 342 | 8 | 40 (341), 47 (1) |
| 78971 | 352 (84..439) | 335 | 15 | 47 (162), 45 (160), 42 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 45 (174), 42 (130), 47 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 42 (194), 47 (140), 43 (3), 45 (2), 46 (1) |
| 78897 | 345 (89..450) | 338 | 7 | 46 (336), 43 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 43 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 52 (350), 50 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 50 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 58 (356), 55 (1) |
| 79103 | 380 (99..481) | 360 | 19 | 54 (354), 55 (5), 58 (1) |
| 79105 | 379 (101..484) | 362 | 16 | 77 (336), 55 (20), 54 (5), 58 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 55 (349), 62 (22) |
| 79110 | 388 (106..497) | 375 | 12 | 62 (324), 64 (30), 59 (20), 71 (1) |
| 79111 | 386 (109..500) | 376 | 8 | 71 (240), 64 (62), 59 (39), 62 (35) |
| 79115 | 421 (111..531) | 393 | 22 | 67 (293), 64 (41), 59 (40), 66 (13), 71 (6) |
| 79116 | 411 (114..530) | 402 | 9 | 59 (179), 64 (98), 67 (90), 71 (20), 66 (15) |
| 79122 | 404 (118..532) | 386 | 14 | 66 (292), 59 (45), 71 (24), 67 (14), 64 (11) |
| 79132 | 391 (120..515) | 380 | 11 | 68 (89), 59 (79), 66 (77), 71 (70), 64 (65) |
| 79128 | 402 (124..527) | 391 | 9 | 68 (297), 64 (91), 72 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 72 (348), 83 (44), 68 (1) |
| 79135 | 409 (129..542) | 397 | 12 | 75 (395), 72 (1), 83 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 83 (333), 72 (50), 86 (12), 75 (1) |
| 79136 | 393 (136..538) | 380 | 10 | 86 (366), 83 (12), 75 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 218 | 421..460 | 40 | 0 | 40 |
| 324 | 651..680 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 30/408/1007; tracks with internal gaps: 25; total internal gaps: 412; longest internal gap: 3; tracks ending in coasting: 26 (trailing rows total 832)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 334 | 47 | 16 | 3 | 29 | 78896 |
| 40 | 82..463 | 382 | 382 | 342 | 40 | 10 | 2 | 29 | 78896, 78969 |
| 42 | 86..474 | 389 | 389 | 337 | 52 | 20 | 2 | 29 | 78971, 79037, 79045 |
| 43 | 86..484 | 399 | 399 | 359 | 40 | 10 | 2 | 29 | 78897, 78899, 79037 |
| 45 | 88..472 | 385 | 385 | 336 | 49 | 20 | 1 | 29 | 78971, 79037, 79045 |
| 46 | 91..479 | 389 | 389 | 337 | 52 | 23 | 1 | 29 | 78897, 79037 |
| 47 | 93..468 | 376 | 376 | 331 | 45 | 15 | 2 | 29 | 78969, 78971, 79037, 79045 |
| 50 | 96..496 | 401 | 401 | 349 | 52 | 22 | 2 | 29 | 79097, 79098 |
| 52 | 99..490 | 392 | 392 | 350 | 42 | 12 | 2 | 29 | 79097 |
| 54 | 100..510 | 411 | 411 | 359 | 52 | 22 | 2 | 29 | 79103, 79105 |
| 55 | 101..521 | 421 | 421 | 375 | 46 | 16 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 58 | 103..506 | 404 | 404 | 358 | 46 | 16 | 2 | 29 | 79102, 79103, 79105 |
| 59 | 106..559 | 454 | 454 | 402 | 52 | 21 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 62 | 108..526 | 419 | 419 | 381 | 38 | 9 | 1 | 29 | 79108, 79110, 79111 |
| 64 | 111..556 | 446 | 446 | 398 | 48 | 13 | 3 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 113..627 | 515 | 515 | 397 | 118 | 23 | 1 | 95 | 79115, 79116, 79122, 79132 |
| 67 | 116..560 | 445 | 445 | 397 | 48 | 18 | 2 | 29 | 79115, 79116, 79122 |
| 68 | 120..544 | 425 | 425 | 387 | 38 | 9 | 1 | 29 | 79128, 79132, 79134 |
| 71 | 122..529 | 408 | 408 | 361 | 47 | 16 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 126..566 | 441 | 441 | 402 | 39 | 9 | 2 | 29 | 79128, 79134, 79135, 79139 |
| 75 | 129..571 | 443 | 443 | 398 | 45 | 16 | 1 | 29 | 79135, 79136, 79139 |
| 77 | 132..513 | 382 | 382 | 336 | 46 | 16 | 2 | 29 | 79105 |
| 83 | 134..562 | 429 | 429 | 390 | 39 | 9 | 2 | 29 | 79134, 79135, 79136, 79139 |
| 86 | 138..567 | 430 | 430 | 378 | 52 | 20 | 2 | 29 | 79136, 79139 |
| 218 | 421..460 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 324 | 651..680 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 9770; unmatched reference entries: 372; unmatched candidate entries: 1274
- identity switches: 111; fragmentation (coverage interruptions): 318; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 43 -> 45 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 43 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f93: ref 79037: 45 -> 47 at (2118, 3034.5), 1 frames after previous cover
- f99: ref 79097: 50 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 78971: 42 -> 45 at (2041, 3033), 2 frames after previous cover
- f102: ref 79045: 45 -> 42 at (2049, 3033), 1 frames after previous cover
- f103: ref 79102: 55 -> 58 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 54 -> 55 at (2133.5, 3022.5), 2 frames after previous cover
- f103: ref 79105: 55 -> 54 at (2143, 3025.5), 2 frames after previous cover
- f108: ref 79103: 55 -> 54 at (2104.5, 3023), 1 frames after previous cover
- f108: ref 79105: 54 -> 55 at (2113.5, 3025), 1 frames after previous cover
- f115: ref 79105: 55 -> 54 at (2073, 3025), 2 frames after previous cover
- f116: ref 79105: 54 -> 55 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79115: 66 -> 67 at (2130, 3021), 3 frames after previous cover
- f126: ref 79037: 47 -> 42 at (1914, 3036), 1 frames after previous cover
- f126: ref 79045: 42 -> 47 at (1899, 3035.5), 1 frames after previous cover
- f127: ref 79037: 42 -> 47 at (1907, 3034.5), 1 frames after previous cover
- f129: ref 79045: 47 -> 42 at (1879.5, 3034), 1 frames after previous cover
- f129: ref 79105: 55 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 62 -> 55 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 59 -> 62 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 64 -> 59 at (2042, 3029), 1 frames after previous cover
- f129: ref 79115: 67 -> 64 at (2056, 3022), 1 frames after previous cover
- f129: ref 79116: 66 -> 67 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 71 -> 66 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 72 -> 68 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 68 -> 71 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79105: 58 -> 77 at (1975.5, 3025.5), 3 frames after previous cover
- f142: ref 79115: 64 -> 67 at (1978, 3023.5), 1 frames after previous cover
- f142: ref 79116: 67 -> 64 at (1992, 3025.5), 1 frames after previous cover
- f143: ref 79115: 67 -> 64 at (1973.5, 3024.5), 1 frames after previous cover
- f143: ref 79116: 64 -> 67 at (1987.5, 3025), 1 frames after previous cover
- f168: ref 79111: 59 -> 64 at (1812, 3022.5), 1 frames after previous cover
- f168: ref 79115: 64 -> 59 at (1819, 3023.5), 3 frames after previous cover
- f200: ref 79122: 66 -> 71 at (1648, 3017), 2 frames after previous cover
- f200: ref 79132: 71 -> 66 at (1652, 3011.5), 1 frames after previous cover
- f209: ref 79110: 62 -> 64 at (1549, 3009.5), 1 frames after previous cover
- f209: ref 79111: 64 -> 62 at (1559.5, 3007), 1 frames after previous cover
- f211: ref 79115: 59 -> 67 at (1555.5, 3008), 3 frames after previous cover
- f211: ref 79116: 67 -> 59 at (1564, 3007.5), 1 frames after previous cover
- f216: ref 79103: 54 -> 58 at (1438, 3003.5), 1 frames after previous cover
- f217: ref 79103: 58 -> 54 at (1432.5, 3002), 1 frames after previous cover
- f220: ref 79116: 59 -> 71 at (1509, 3006), 2 frames after previous cover
- f220: ref 79122: 71 -> 59 at (1521, 3009), 1 frames after previous cover
- f225: ref 79110: 64 -> 62 at (1453, 3001.5), 3 frames after previous cover
- f226: ref 79110: 62 -> 64 at (1446.5, 2999.5), 1 frames after previous cover
- f239: ref 79037: 47 -> 42 at (1170.5, 2988), 1 frames after previous cover
- f241: ref 79045: 42 -> 47 at (1143.5, 2989), 3 frames after previous cover
- f241: ref 79115: 67 -> 71 at (1373.5, 2998.5), 3 frames after previous cover
- f241: ref 79116: 71 -> 67 at (1381, 2998), 1 frames after previous cover
- f245: ref 79110: 64 -> 62 at (1332, 2991.5), 3 frames after previous cover
- f245: ref 79111: 62 -> 64 at (1340, 2995.5), 1 frames after previous cover
- f248: ref 79111: 64 -> 71 at (1322, 2992), 1 frames after previous cover
- f248: ref 79115: 71 -> 64 at (1333.5, 2995), 2 frames after previous cover
- f253: ref 79116: 67 -> 64 at (1309, 2992), 1 frames after previous cover
- f254: ref 79115: 64 -> 67 at (1296.5, 2992.5), 2 frames after previous cover
- f255: ref 79116: 64 -> 59 at (1298, 2989.5), 1 frames after previous cover
- f255: ref 79122: 59 -> 64 at (1307, 2993), 1 frames after previous cover
- f264: ref 79122: 64 -> 66 at (1253.5, 2987), 1 frames after previous cover
- f264: ref 79132: 66 -> 64 at (1251, 2979.5), 2 frames after previous cover
- ... 51 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 31 | 1 (976) |
| 78896 | 350 (76..429) | 335 | 13 | 38 (334), 40 (1) |
| 78969 | 352 (80..434) | 342 | 8 | 40 (341), 47 (1) |
| 78971 | 352 (84..439) | 335 | 15 | 47 (162), 45 (160), 42 (13) |
| 79045 | 355 (84..443) | 332 | 18 | 45 (174), 42 (130), 47 (28) |
| 79037 | 355 (86..445) | 340 | 14 | 42 (194), 47 (140), 43 (3), 45 (2), 46 (1) |
| 78897 | 345 (89..450) | 338 | 7 | 46 (336), 43 (2) |
| 78899 | 365 (91..455) | 354 | 9 | 43 (354) |
| 79097 | 366 (94..461) | 351 | 11 | 52 (350), 50 (1) |
| 79098 | 360 (97..467) | 348 | 12 | 50 (348) |
| 79102 | 371 (98..477) | 357 | 10 | 58 (356), 55 (1) |
| 79103 | 380 (99..481) | 360 | 19 | 54 (354), 55 (5), 58 (1) |
| 79105 | 379 (101..484) | 362 | 16 | 77 (336), 55 (20), 54 (5), 58 (1) |
| 79108 | 385 (104..492) | 371 | 10 | 55 (349), 62 (22) |
| 79110 | 388 (106..497) | 375 | 12 | 62 (324), 64 (30), 59 (20), 71 (1) |
| 79111 | 386 (109..500) | 376 | 8 | 71 (240), 64 (62), 59 (39), 62 (35) |
| 79115 | 421 (111..531) | 393 | 22 | 67 (293), 64 (41), 59 (40), 66 (13), 71 (6) |
| 79116 | 411 (114..530) | 402 | 9 | 59 (179), 64 (98), 67 (90), 71 (20), 66 (15) |
| 79122 | 404 (118..532) | 386 | 14 | 66 (292), 59 (45), 71 (24), 67 (14), 64 (11) |
| 79132 | 391 (120..515) | 380 | 11 | 68 (89), 59 (79), 66 (77), 71 (70), 64 (65) |
| 79128 | 402 (124..527) | 391 | 9 | 68 (297), 64 (91), 72 (3) |
| 79134 | 407 (127..533) | 393 | 11 | 72 (348), 83 (44), 68 (1) |
| 79135 | 409 (129..542) | 397 | 12 | 75 (395), 72 (1), 83 (1) |
| 79139 | 406 (132..537) | 396 | 7 | 83 (333), 72 (50), 86 (12), 75 (1) |
| 79136 | 393 (136..538) | 380 | 10 | 86 (366), 83 (12), 75 (2) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 218 | 421..460 | 40 | 0 | 40 |
| 324 | 651..680 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 30/408/1007; tracks with internal gaps: 25; total internal gaps: 412; longest internal gap: 3; tracks ending in coasting: 26 (trailing rows total 832)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 976 | 31 | 31 | 1 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 334 | 47 | 16 | 3 | 29 | 78896 |
| 40 | 82..463 | 382 | 382 | 342 | 40 | 10 | 2 | 29 | 78896, 78969 |
| 42 | 86..474 | 389 | 389 | 337 | 52 | 20 | 2 | 29 | 78971, 79037, 79045 |
| 43 | 86..484 | 399 | 399 | 359 | 40 | 10 | 2 | 29 | 78897, 78899, 79037 |
| 45 | 88..472 | 385 | 385 | 336 | 49 | 20 | 1 | 29 | 78971, 79037, 79045 |
| 46 | 91..479 | 389 | 389 | 337 | 52 | 23 | 1 | 29 | 78897, 79037 |
| 47 | 93..468 | 376 | 376 | 331 | 45 | 15 | 2 | 29 | 78969, 78971, 79037, 79045 |
| 50 | 96..496 | 401 | 401 | 349 | 52 | 22 | 2 | 29 | 79097, 79098 |
| 52 | 99..490 | 392 | 392 | 350 | 42 | 12 | 2 | 29 | 79097 |
| 54 | 100..510 | 411 | 411 | 359 | 52 | 22 | 2 | 29 | 79103, 79105 |
| 55 | 101..521 | 421 | 421 | 375 | 46 | 16 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 58 | 103..506 | 404 | 404 | 358 | 46 | 16 | 2 | 29 | 79102, 79103, 79105 |
| 59 | 106..559 | 454 | 454 | 402 | 52 | 21 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 62 | 108..526 | 419 | 419 | 381 | 38 | 9 | 1 | 29 | 79108, 79110, 79111 |
| 64 | 111..556 | 446 | 446 | 398 | 48 | 13 | 3 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 66 | 113..627 | 515 | 515 | 397 | 118 | 23 | 1 | 95 | 79115, 79116, 79122, 79132 |
| 67 | 116..560 | 445 | 445 | 397 | 48 | 18 | 2 | 29 | 79115, 79116, 79122 |
| 68 | 120..544 | 425 | 425 | 387 | 38 | 9 | 1 | 29 | 79128, 79132, 79134 |
| 71 | 122..529 | 408 | 408 | 361 | 47 | 16 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79132 |
| 72 | 126..566 | 441 | 441 | 402 | 39 | 9 | 2 | 29 | 79128, 79134, 79135, 79139 |
| 75 | 129..571 | 443 | 443 | 398 | 45 | 16 | 1 | 29 | 79135, 79136, 79139 |
| 77 | 132..513 | 382 | 382 | 336 | 46 | 16 | 2 | 29 | 79105 |
| 83 | 134..562 | 429 | 429 | 390 | 39 | 9 | 2 | 29 | 79134, 79135, 79136, 79139 |
| 86 | 138..567 | 430 | 430 | 378 | 52 | 20 | 2 | 29 | 79136, 79139 |
| 218 | 421..460 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 324 | 651..680 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
