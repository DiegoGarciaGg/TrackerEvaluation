# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=be8e42d3376f
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise0.0_fp0.0_seed1/tracks.csv sha256=935a2b531cea6b2f
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise0.0_fp0.0_seed1.csv sha256=be8e42d3376fcfe5
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise0.0_fp0.0_seed1
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
| observations | none | 4 | 10142 | 8052 | 0.417 | 0.793 | 0.219 | 0.01 | 0.417 | 0.729 | 0.01 | 662 | 1590.0 | 0.383 | 0.433 | 0.344 | 0.794 | 1.000 | 8052 | 2090 | 0 | 8 | 17 | 0 |
| observations | none | 6 | 10142 | 8052 | 0.417 | 0.790 | 0.220 | 0.02 | 0.417 | 0.729 | 0.01 | 659 | 1590.0 | 0.383 | 0.433 | 0.344 | 0.794 | 1.000 | 8052 | 2090 | 0 | 8 | 17 | 0 |
| observations | none | 8 | 10142 | 8052 | 0.416 | 0.777 | 0.223 | 0.08 | 0.416 | 0.729 | 0.05 | 655 | 1585.0 | 0.385 | 0.435 | 0.345 | 0.794 | 1.000 | 8052 | 2090 | 0 | 8 | 17 | 0 |
| observations | none | 12 | 10142 | 8052 | 0.417 | 0.764 | 0.227 | 0.25 | 0.419 | 0.732 | 0.35 | 615 | 1562.0 | 0.403 | 0.455 | 0.362 | 0.793 | 0.999 | 8046 | 2096 | 6 | 9 | 16 | 0 |
| observations | ignore | 4 | 10142 | 8052 | 0.417 | 0.793 | 0.219 | 0.01 | 0.417 | 0.729 | 0.01 | 662 | 1590.0 | 0.383 | 0.433 | 0.344 | 0.794 | 1.000 | 8052 | 2090 | 0 | 8 | 17 | 0 |
| observations | ignore | 6 | 10142 | 8052 | 0.417 | 0.790 | 0.220 | 0.02 | 0.417 | 0.729 | 0.01 | 659 | 1590.0 | 0.383 | 0.433 | 0.344 | 0.794 | 1.000 | 8052 | 2090 | 0 | 8 | 17 | 0 |
| observations | ignore | 8 | 10142 | 8052 | 0.416 | 0.777 | 0.223 | 0.08 | 0.416 | 0.729 | 0.05 | 655 | 1585.0 | 0.385 | 0.435 | 0.345 | 0.794 | 1.000 | 8052 | 2090 | 0 | 8 | 17 | 0 |
| observations | ignore | 12 | 10142 | 8052 | 0.417 | 0.764 | 0.227 | 0.25 | 0.419 | 0.732 | 0.35 | 615 | 1562.0 | 0.403 | 0.455 | 0.362 | 0.793 | 0.999 | 8046 | 2096 | 6 | 9 | 16 | 0 |
| updates | none | 4 | 10142 | 10481 | 0.384 | 0.696 | 0.212 | 0.21 | 0.376 | 0.535 | 0.09 | 689 | 1493.0 | 0.355 | 0.349 | 0.361 | 0.818 | 0.792 | 8298 | 1844 | 2183 | 17 | 8 | 0 |
| updates | none | 6 | 10142 | 10481 | 0.409 | 0.744 | 0.225 | 0.44 | 0.411 | 0.634 | 0.39 | 686 | 1104.0 | 0.379 | 0.373 | 0.386 | 0.868 | 0.840 | 8800 | 1342 | 1681 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10481 | 0.424 | 0.764 | 0.235 | 0.64 | 0.449 | 0.747 | 0.81 | 671 | 652.0 | 0.403 | 0.396 | 0.410 | 0.923 | 0.893 | 9364 | 778 | 1117 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10481 | 0.442 | 0.789 | 0.248 | 0.98 | 0.464 | 0.780 | 1.24 | 613 | 520.0 | 0.431 | 0.424 | 0.438 | 0.937 | 0.906 | 9501 | 641 | 980 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10481 | 0.384 | 0.696 | 0.212 | 0.21 | 0.376 | 0.535 | 0.09 | 689 | 1493.0 | 0.355 | 0.349 | 0.361 | 0.818 | 0.792 | 8298 | 1844 | 2183 | 17 | 8 | 0 |
| updates | ignore | 6 | 10142 | 10481 | 0.409 | 0.744 | 0.225 | 0.44 | 0.411 | 0.634 | 0.39 | 686 | 1104.0 | 0.379 | 0.373 | 0.386 | 0.868 | 0.840 | 8800 | 1342 | 1681 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10481 | 0.424 | 0.764 | 0.235 | 0.64 | 0.449 | 0.747 | 0.81 | 671 | 652.0 | 0.403 | 0.396 | 0.410 | 0.923 | 0.893 | 9364 | 778 | 1117 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10481 | 0.442 | 0.789 | 0.248 | 0.98 | 0.464 | 0.780 | 1.24 | 613 | 520.0 | 0.431 | 0.424 | 0.438 | 0.937 | 0.906 | 9501 | 641 | 980 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8052; unmatched reference entries: 2090; unmatched candidate entries: 0
- identity switches: 655; fragmentation (coverage interruptions): 1599; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 2 -> 4 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 6 -> 2 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 7 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 6 -> 9 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78897: 6 -> 9 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 5 -> 10 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 2 -> 11 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 9 -> 7 at (2099, 3033.5), 2 frames after previous cover
- f98: ref 78899: 10 -> 6 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 5 -> 10 at (2129, 3028), 1 frames after previous cover
- f100: ref 79098: 5 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 6 -> 9 at (2098.5, 3030.5), 3 frames after previous cover
- f101: ref 79098: 10 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 10 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 12 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79097: 10 -> 6 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 6 -> 9 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 12 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 2 -> 11 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 7 -> 2 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 10 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 10 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 9 -> 7 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 11 -> 2 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 6 -> 5 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 78897: 9 -> 7 at (2052.5, 3032.5), 4 frames after previous cover
- f106: ref 79102: 6 -> 5 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 10 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 5 -> 10 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 5 -> 9 at (2090, 3028), 2 frames after previous cover
- f108: ref 78899: 7 -> 9 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79037: 7 -> 17 at (2026, 3034), 4 frames after previous cover
- f108: ref 79045: 2 -> 15 at (2014.5, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 6 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 15 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79045: 15 -> 4 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 7 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 6 -> 9 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 10 -> 5 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 12 -> 10 at (2118, 3025), 6 frames after previous cover
- f111: ref 78897: 7 -> 15 at (2021.5, 3032.5), 2 frames after previous cover
- f111: ref 78899: 15 -> 7 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79102: 5 -> 19 at (2079, 3029.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 10 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 12 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f113: ref 79037: 17 -> 4 at (1995, 3034.5), 1 frames after previous cover
- f114: ref 78896: 4 -> 2 at (1921, 3035), 5 frames after previous cover
- f114: ref 79045: 4 -> 17 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79097: 7 -> 22 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79110: 10 -> 21 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 18 -> 10 at (2126, 3027), 1 frames after previous cover
- f115: ref 78971: 2 -> 17 at (1959, 3034), 2 frames after previous cover
- f115: ref 79115: 12 -> 18 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 79108: 10 -> 21 at (2087, 3026.5), 6 frames after previous cover
- f117: ref 79110: 21 -> 12 at (2094.5, 3027), 3 frames after previous cover
- f118: ref 78899: 7 -> 15 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 79037: 4 -> 23 at (1964, 3035.5), 2 frames after previous cover
- ... 595 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 153 | 1 (799) |
| 78896 | 350 (76..429) | 276 | 53 | 29 (231), 4 (24), 2 (21) |
| 78969 | 352 (80..434) | 289 | 48 | 25 (145), 17 (104), 11 (24), 2 (13), 29 (3) |
| 78971 | 352 (84..439) | 275 | 55 | 2 (152), 17 (102), 25 (13), 11 (6), 6 (2) |
| 79045 | 355 (84..443) | 280 | 51 | 25 (102), 17 (64), 32 (48), 2 (42), 7 (11), 11 (4), 4 (3), 15 (2), 23 (2), 5 (1), 6 (1) |
| 79037 | 355 (86..445) | 276 | 53 | 23 (158), 32 (83), 2 (14), 17 (5), 7 (4), 4 (4), 25 (3), 5 (2), 6 (2), 9 (1) |
| 78897 | 345 (89..450) | 275 | 50 | 23 (96), 2 (48), 32 (38), 31 (37), 4 (26), 15 (6), 6 (5), 9 (4), 11 (4), 7 (3), 25 (3), 17 (3), +1 more |
| 78899 | 365 (91..455) | 297 | 54 | 4 (164), 32 (83), 11 (19), 23 (12), 7 (6), 15 (4), 5 (3), 10 (2), 9 (2), 6 (1), 31 (1) |
| 79097 | 366 (94..461) | 293 | 56 | 11 (152), 4 (88), 15 (13), 32 (12), 31 (7), 9 (5), 22 (5), 5 (4), 7 (4), 10 (2), 6 (1) |
| 79098 | 360 (97..467) | 285 | 64 | 15 (109), 7 (61), 22 (56), 11 (32), 4 (11), 9 (8), 6 (4), 5 (3), 10 (1) |
| 79102 | 371 (98..477) | 280 | 69 | 15 (116), 22 (80), 7 (45), 11 (11), 19 (6), 5 (5), 31 (5), 26 (4), 9 (3), 10 (2), 6 (2), 4 (1) |
| 79103 | 380 (99..481) | 293 | 68 | 22 (65), 7 (61), 11 (50), 15 (39), 26 (34), 31 (16), 5 (13), 6 (9), 21 (3), 10 (2), 12 (1) |
| 79105 | 379 (101..484) | 310 | 60 | 7 (106), 21 (65), 22 (55), 31 (25), 5 (16), 11 (16), 26 (12), 15 (11), 10 (3), 12 (1) |
| 79108 | 385 (104..492) | 311 | 57 | 21 (180), 6 (46), 31 (38), 7 (33), 5 (9), 22 (2), 12 (1), 10 (1), 9 (1) |
| 79110 | 388 (106..497) | 310 | 62 | 5 (91), 21 (67), 31 (43), 19 (35), 9 (29), 22 (20), 6 (17), 12 (4), 10 (3), 26 (1) |
| 79111 | 386 (109..500) | 324 | 51 | 5 (110), 19 (105), 6 (38), 9 (32), 21 (15), 31 (12), 10 (4), 18 (3), 22 (3), 12 (1), 26 (1) |
| 79115 | 421 (111..531) | 332 | 67 | 30 (72), 19 (63), 5 (60), 6 (58), 12 (47), 9 (14), 22 (6), 18 (5), 26 (3), 28 (3), 31 (1) |
| 79116 | 411 (114..530) | 325 | 65 | 18 (124), 12 (57), 6 (32), 5 (31), 9 (27), 31 (25), 28 (19), 19 (9), 26 (1) |
| 79122 | 404 (118..532) | 315 | 71 | 28 (107), 6 (75), 12 (50), 18 (37), 31 (27), 19 (6), 26 (5), 30 (4), 10 (2), 9 (2) |
| 79132 | 391 (120..515) | 313 | 67 | 18 (69), 6 (68), 19 (53), 30 (42), 12 (39), 28 (26), 9 (8), 10 (4), 31 (3), 26 (1) |
| 79128 | 402 (124..527) | 329 | 62 | 10 (125), 19 (63), 28 (57), 12 (25), 26 (23), 31 (20), 9 (8), 30 (5), 18 (3) |
| 79134 | 407 (127..533) | 311 | 69 | 12 (109), 28 (80), 30 (65), 9 (23), 18 (20), 10 (10), 33 (4) |
| 79135 | 409 (129..542) | 326 | 68 | 10 (107), 18 (73), 9 (65), 28 (37), 26 (36), 12 (6), 30 (2) |
| 79139 | 406 (132..537) | 319 | 66 | 30 (121), 9 (85), 26 (68), 33 (44), 10 (1) |
| 79136 | 393 (136..538) | 309 | 60 | 26 (130), 10 (87), 9 (62), 33 (27), 12 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 93/386/1003; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1007 | 1003 | 799 | 799 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 78..443 | 366 | 290 | 290 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 4 | 85..461 | 377 | 321 | 321 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..496 | 411 | 350 | 350 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 6 | 86..515 | 430 | 361 | 361 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 90..484 | 395 | 334 | 334 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 9 | 94..542 | 449 | 379 | 379 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 10 | 96..527 | 432 | 356 | 356 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 96..481 | 386 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..533 | 434 | 344 | 344 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 15 | 108..467 | 360 | 300 | 300 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 108..439 | 332 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 111..530 | 420 | 334 | 334 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..500 | 390 | 340 | 340 | 0 | 0 | 0 | 0 | 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 114..492 | 379 | 330 | 330 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111 |
| 22 | 114..477 | 364 | 292 | 292 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 118..445 | 328 | 268 | 268 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 25 | 124..434 | 311 | 266 | 266 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 26 | 128..538 | 411 | 319 | 319 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79136, 79139 |
| 28 | 129..532 | 404 | 329 | 329 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 138..429 | 292 | 234 | 234 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 30 | 139..531 | 393 | 311 | 311 | 0 | 0 | 0 | 0 | 79115, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 139..450 | 312 | 260 | 260 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 144..455 | 312 | 264 | 264 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097 |
| 33 | 445..537 | 93 | 75 | 75 | 0 | 0 | 0 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8052; unmatched reference entries: 2090; unmatched candidate entries: 0
- identity switches: 655; fragmentation (coverage interruptions): 1599; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 2 -> 4 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 6 -> 2 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 7 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 6 -> 9 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78897: 6 -> 9 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 5 -> 10 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 2 -> 11 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 9 -> 7 at (2099, 3033.5), 2 frames after previous cover
- f98: ref 78899: 10 -> 6 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 5 -> 10 at (2129, 3028), 1 frames after previous cover
- f100: ref 79098: 5 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 6 -> 9 at (2098.5, 3030.5), 3 frames after previous cover
- f101: ref 79098: 10 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 10 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 12 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79097: 10 -> 6 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 6 -> 9 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 12 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 2 -> 11 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 7 -> 2 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 10 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 10 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 9 -> 7 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 11 -> 2 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 6 -> 5 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 78897: 9 -> 7 at (2052.5, 3032.5), 4 frames after previous cover
- f106: ref 79102: 6 -> 5 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 10 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 5 -> 10 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 5 -> 9 at (2090, 3028), 2 frames after previous cover
- f108: ref 78899: 7 -> 9 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79037: 7 -> 17 at (2026, 3034), 4 frames after previous cover
- f108: ref 79045: 2 -> 15 at (2014.5, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 6 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 15 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79045: 15 -> 4 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 7 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 6 -> 9 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 10 -> 5 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 12 -> 10 at (2118, 3025), 6 frames after previous cover
- f111: ref 78897: 7 -> 15 at (2021.5, 3032.5), 2 frames after previous cover
- f111: ref 78899: 15 -> 7 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79102: 5 -> 19 at (2079, 3029.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 10 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 12 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f113: ref 79037: 17 -> 4 at (1995, 3034.5), 1 frames after previous cover
- f114: ref 78896: 4 -> 2 at (1921, 3035), 5 frames after previous cover
- f114: ref 79045: 4 -> 17 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79097: 7 -> 22 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79110: 10 -> 21 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 18 -> 10 at (2126, 3027), 1 frames after previous cover
- f115: ref 78971: 2 -> 17 at (1959, 3034), 2 frames after previous cover
- f115: ref 79115: 12 -> 18 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 79108: 10 -> 21 at (2087, 3026.5), 6 frames after previous cover
- f117: ref 79110: 21 -> 12 at (2094.5, 3027), 3 frames after previous cover
- f118: ref 78899: 7 -> 15 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 79037: 4 -> 23 at (1964, 3035.5), 2 frames after previous cover
- ... 595 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 153 | 1 (799) |
| 78896 | 350 (76..429) | 276 | 53 | 29 (231), 4 (24), 2 (21) |
| 78969 | 352 (80..434) | 289 | 48 | 25 (145), 17 (104), 11 (24), 2 (13), 29 (3) |
| 78971 | 352 (84..439) | 275 | 55 | 2 (152), 17 (102), 25 (13), 11 (6), 6 (2) |
| 79045 | 355 (84..443) | 280 | 51 | 25 (102), 17 (64), 32 (48), 2 (42), 7 (11), 11 (4), 4 (3), 15 (2), 23 (2), 5 (1), 6 (1) |
| 79037 | 355 (86..445) | 276 | 53 | 23 (158), 32 (83), 2 (14), 17 (5), 7 (4), 4 (4), 25 (3), 5 (2), 6 (2), 9 (1) |
| 78897 | 345 (89..450) | 275 | 50 | 23 (96), 2 (48), 32 (38), 31 (37), 4 (26), 15 (6), 6 (5), 9 (4), 11 (4), 7 (3), 25 (3), 17 (3), +1 more |
| 78899 | 365 (91..455) | 297 | 54 | 4 (164), 32 (83), 11 (19), 23 (12), 7 (6), 15 (4), 5 (3), 10 (2), 9 (2), 6 (1), 31 (1) |
| 79097 | 366 (94..461) | 293 | 56 | 11 (152), 4 (88), 15 (13), 32 (12), 31 (7), 9 (5), 22 (5), 5 (4), 7 (4), 10 (2), 6 (1) |
| 79098 | 360 (97..467) | 285 | 64 | 15 (109), 7 (61), 22 (56), 11 (32), 4 (11), 9 (8), 6 (4), 5 (3), 10 (1) |
| 79102 | 371 (98..477) | 280 | 69 | 15 (116), 22 (80), 7 (45), 11 (11), 19 (6), 5 (5), 31 (5), 26 (4), 9 (3), 10 (2), 6 (2), 4 (1) |
| 79103 | 380 (99..481) | 293 | 68 | 22 (65), 7 (61), 11 (50), 15 (39), 26 (34), 31 (16), 5 (13), 6 (9), 21 (3), 10 (2), 12 (1) |
| 79105 | 379 (101..484) | 310 | 60 | 7 (106), 21 (65), 22 (55), 31 (25), 5 (16), 11 (16), 26 (12), 15 (11), 10 (3), 12 (1) |
| 79108 | 385 (104..492) | 311 | 57 | 21 (180), 6 (46), 31 (38), 7 (33), 5 (9), 22 (2), 12 (1), 10 (1), 9 (1) |
| 79110 | 388 (106..497) | 310 | 62 | 5 (91), 21 (67), 31 (43), 19 (35), 9 (29), 22 (20), 6 (17), 12 (4), 10 (3), 26 (1) |
| 79111 | 386 (109..500) | 324 | 51 | 5 (110), 19 (105), 6 (38), 9 (32), 21 (15), 31 (12), 10 (4), 18 (3), 22 (3), 12 (1), 26 (1) |
| 79115 | 421 (111..531) | 332 | 67 | 30 (72), 19 (63), 5 (60), 6 (58), 12 (47), 9 (14), 22 (6), 18 (5), 26 (3), 28 (3), 31 (1) |
| 79116 | 411 (114..530) | 325 | 65 | 18 (124), 12 (57), 6 (32), 5 (31), 9 (27), 31 (25), 28 (19), 19 (9), 26 (1) |
| 79122 | 404 (118..532) | 315 | 71 | 28 (107), 6 (75), 12 (50), 18 (37), 31 (27), 19 (6), 26 (5), 30 (4), 10 (2), 9 (2) |
| 79132 | 391 (120..515) | 313 | 67 | 18 (69), 6 (68), 19 (53), 30 (42), 12 (39), 28 (26), 9 (8), 10 (4), 31 (3), 26 (1) |
| 79128 | 402 (124..527) | 329 | 62 | 10 (125), 19 (63), 28 (57), 12 (25), 26 (23), 31 (20), 9 (8), 30 (5), 18 (3) |
| 79134 | 407 (127..533) | 311 | 69 | 12 (109), 28 (80), 30 (65), 9 (23), 18 (20), 10 (10), 33 (4) |
| 79135 | 409 (129..542) | 326 | 68 | 10 (107), 18 (73), 9 (65), 28 (37), 26 (36), 12 (6), 30 (2) |
| 79139 | 406 (132..537) | 319 | 66 | 30 (121), 9 (85), 26 (68), 33 (44), 10 (1) |
| 79136 | 393 (136..538) | 309 | 60 | 26 (130), 10 (87), 9 (62), 33 (27), 12 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 93/386/1003; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1007 | 1003 | 799 | 799 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 78..443 | 366 | 290 | 290 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 4 | 85..461 | 377 | 321 | 321 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..496 | 411 | 350 | 350 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 6 | 86..515 | 430 | 361 | 361 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 90..484 | 395 | 334 | 334 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 9 | 94..542 | 449 | 379 | 379 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 10 | 96..527 | 432 | 356 | 356 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 96..481 | 386 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..533 | 434 | 344 | 344 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 15 | 108..467 | 360 | 300 | 300 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 108..439 | 332 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 111..530 | 420 | 334 | 334 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..500 | 390 | 340 | 340 | 0 | 0 | 0 | 0 | 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 114..492 | 379 | 330 | 330 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111 |
| 22 | 114..477 | 364 | 292 | 292 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 118..445 | 328 | 268 | 268 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 25 | 124..434 | 311 | 266 | 266 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 26 | 128..538 | 411 | 319 | 319 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79136, 79139 |
| 28 | 129..532 | 404 | 329 | 329 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 138..429 | 292 | 234 | 234 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 30 | 139..531 | 393 | 311 | 311 | 0 | 0 | 0 | 0 | 79115, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 139..450 | 312 | 260 | 260 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 144..455 | 312 | 264 | 264 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097 |
| 33 | 445..537 | 93 | 75 | 75 | 0 | 0 | 0 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9364; unmatched reference entries: 778; unmatched candidate entries: 1117
- identity switches: 671; fragmentation (coverage interruptions): 570; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 2 -> 4 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 6 -> 2 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 7 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 6 -> 9 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78899: 5 -> 10 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 2 -> 11 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 9 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 6 -> 9 at (2107, 3033), 1 frames after previous cover
- f98: ref 78899: 10 -> 6 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 5 -> 10 at (2129, 3028), 1 frames after previous cover
- f100: ref 78899: 6 -> 9 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 79097: 10 -> 6 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 5 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 79098: 10 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 10 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 12 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 6 -> 9 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 12 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 2 -> 11 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 7 -> 2 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 10 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 10 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 9 -> 7 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 11 -> 2 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 6 -> 5 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 78897: 9 -> 7 at (2052.5, 3032.5), 4 frames after previous cover
- f106: ref 79102: 6 -> 5 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 10 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 5 -> 10 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 79098: 5 -> 9 at (2090, 3028), 2 frames after previous cover
- f108: ref 78899: 7 -> 9 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79037: 7 -> 17 at (2026, 3034), 4 frames after previous cover
- f108: ref 79045: 2 -> 15 at (2014.5, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 6 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 15 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79045: 15 -> 4 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 7 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 6 -> 9 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 10 -> 5 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 12 -> 10 at (2118, 3025), 5 frames after previous cover
- f111: ref 78897: 7 -> 15 at (2021.5, 3032.5), 2 frames after previous cover
- f111: ref 78899: 15 -> 7 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79102: 5 -> 19 at (2079, 3029.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 10 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 12 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f114: ref 78896: 4 -> 2 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 17 -> 4 at (1988, 3035), 1 frames after previous cover
- f114: ref 79045: 4 -> 17 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79097: 7 -> 22 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79110: 10 -> 21 at (2111, 3026.5), 1 frames after previous cover
- f115: ref 78971: 2 -> 17 at (1959, 3034), 2 frames after previous cover
- f115: ref 79111: 18 -> 10 at (2120, 3028.5), 1 frames after previous cover
- f115: ref 79115: 12 -> 18 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 79108: 10 -> 21 at (2087, 3026.5), 6 frames after previous cover
- f117: ref 79110: 21 -> 12 at (2094.5, 3027), 2 frames after previous cover
- f118: ref 78897: 15 -> 4 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 78899: 7 -> 15 at (1995, 3032.5), 1 frames after previous cover
- ... 611 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 981 | 14 | 1 (981) |
| 78896 | 350 (76..429) | 323 | 14 | 29 (275), 4 (25), 2 (23) |
| 78969 | 352 (80..434) | 326 | 21 | 25 (162), 17 (121), 11 (27), 2 (13), 29 (3) |
| 78971 | 352 (84..439) | 316 | 26 | 2 (180), 17 (112), 25 (16), 11 (6), 6 (2) |
| 79045 | 355 (84..443) | 318 | 22 | 25 (116), 17 (73), 32 (57), 2 (48), 7 (11), 11 (4), 4 (3), 15 (2), 23 (2), 5 (1), 6 (1) |
| 79037 | 355 (86..445) | 318 | 23 | 23 (178), 32 (99), 2 (17), 17 (6), 7 (4), 4 (4), 25 (4), 5 (2), 6 (2), 9 (2) |
| 78897 | 345 (89..450) | 313 | 20 | 23 (111), 2 (56), 32 (41), 31 (41), 4 (31), 6 (6), 15 (6), 9 (4), 7 (4), 25 (4), 11 (4), 17 (3), +1 more |
| 78899 | 365 (91..455) | 339 | 19 | 4 (187), 32 (91), 11 (24), 23 (14), 7 (8), 15 (4), 5 (3), 9 (3), 10 (2), 6 (2), 31 (1) |
| 79097 | 366 (94..461) | 331 | 26 | 11 (175), 4 (99), 15 (14), 32 (13), 31 (8), 9 (5), 22 (5), 5 (4), 7 (4), 10 (2), 6 (2) |
| 79098 | 360 (97..467) | 335 | 22 | 15 (128), 7 (70), 22 (69), 11 (36), 4 (15), 9 (9), 6 (4), 5 (3), 10 (1) |
| 79102 | 371 (98..477) | 325 | 35 | 15 (134), 22 (95), 7 (51), 11 (13), 19 (7), 5 (6), 31 (6), 26 (4), 10 (3), 9 (3), 6 (2), 4 (1) |
| 79103 | 380 (99..481) | 334 | 36 | 22 (77), 7 (66), 11 (60), 26 (40), 15 (40), 31 (22), 5 (13), 6 (10), 21 (3), 10 (2), 12 (1) |
| 79105 | 379 (101..484) | 353 | 26 | 7 (123), 21 (71), 22 (68), 31 (26), 5 (17), 11 (17), 26 (14), 15 (12), 10 (4), 12 (1) |
| 79108 | 385 (104..492) | 356 | 20 | 21 (205), 6 (55), 31 (41), 7 (39), 5 (10), 12 (2), 22 (2), 10 (1), 9 (1) |
| 79110 | 388 (106..497) | 353 | 27 | 5 (111), 21 (74), 31 (51), 19 (38), 9 (32), 22 (21), 6 (18), 12 (4), 10 (3), 26 (1) |
| 79111 | 386 (109..500) | 363 | 19 | 5 (127), 19 (116), 6 (41), 9 (37), 21 (17), 31 (13), 18 (4), 10 (3), 22 (3), 12 (1), 26 (1) |
| 79115 | 421 (111..531) | 383 | 29 | 30 (92), 19 (73), 5 (68), 6 (61), 12 (51), 9 (18), 22 (6), 18 (5), 26 (3), 28 (3), 31 (2), 21 (1) |
| 79116 | 411 (114..530) | 377 | 27 | 18 (150), 12 (64), 6 (38), 5 (33), 9 (30), 31 (30), 28 (19), 19 (11), 10 (2) |
| 79122 | 404 (118..532) | 373 | 24 | 28 (129), 6 (92), 12 (64), 18 (41), 31 (29), 19 (5), 30 (5), 26 (4), 10 (2), 9 (2) |
| 79132 | 391 (120..515) | 368 | 20 | 18 (80), 6 (79), 19 (63), 30 (51), 12 (46), 28 (30), 9 (10), 10 (4), 31 (3), 5 (1), 26 (1) |
| 79128 | 402 (124..527) | 378 | 20 | 10 (144), 19 (69), 28 (66), 12 (31), 26 (29), 31 (22), 9 (8), 30 (6), 18 (3) |
| 79134 | 407 (127..533) | 366 | 29 | 12 (128), 28 (92), 30 (79), 9 (26), 18 (24), 10 (11), 33 (5), 26 (1) |
| 79135 | 409 (129..542) | 386 | 21 | 10 (127), 18 (90), 9 (76), 28 (43), 26 (42), 12 (6), 30 (2) |
| 79139 | 406 (132..537) | 380 | 13 | 30 (150), 9 (91), 26 (86), 33 (52), 10 (1) |
| 79136 | 393 (136..538) | 369 | 17 | 26 (152), 10 (103), 9 (78), 33 (28), 12 (8) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 122/415/1004; tracks with internal gaps: 25; total internal gaps: 324; longest internal gap: 6; tracks ending in coasting: 24 (trailing rows total 691)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 981 | 23 | 14 | 4 | 0 | 78911 |
| 2 | 78..472 | 395 | 395 | 337 | 58 | 20 | 4 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 4 | 85..490 | 406 | 406 | 365 | 41 | 12 | 4 | 23 | 78896, 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..525 | 440 | 440 | 401 | 39 | 9 | 2 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 6 | 86..544 | 459 | 459 | 415 | 44 | 12 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 90..513 | 424 | 424 | 380 | 44 | 12 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 9 | 94..571 | 478 | 478 | 435 | 43 | 11 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 10 | 96..556 | 461 | 461 | 415 | 46 | 16 | 3 | 26 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 96..510 | 415 | 415 | 366 | 49 | 15 | 3 | 29 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..562 | 463 | 463 | 407 | 56 | 20 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 15 | 108..496 | 389 | 389 | 340 | 49 | 14 | 3 | 31 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 108..468 | 361 | 361 | 315 | 46 | 13 | 3 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 111..559 | 449 | 449 | 397 | 52 | 16 | 2 | 32 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..529 | 419 | 419 | 382 | 37 | 8 | 1 | 29 | 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 114..521 | 408 | 408 | 371 | 37 | 7 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 22 | 114..506 | 393 | 393 | 346 | 47 | 15 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 118..474 | 357 | 357 | 305 | 52 | 17 | 3 | 29 | 78897, 78899, 79037, 79045 |
| 25 | 124..463 | 340 | 340 | 302 | 38 | 9 | 1 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 26 | 128..567 | 440 | 440 | 378 | 62 | 19 | 6 | 29 | 79102, 79103, 79105, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 28 | 129..561 | 433 | 433 | 382 | 51 | 19 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 138..458 | 321 | 321 | 278 | 43 | 10 | 3 | 29 | 78896, 78969 |
| 30 | 139..560 | 422 | 422 | 385 | 37 | 6 | 2 | 29 | 79115, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 139..479 | 341 | 341 | 295 | 46 | 14 | 2 | 29 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 144..484 | 341 | 341 | 301 | 40 | 10 | 2 | 29 | 78897, 78899, 79037, 79045, 79097 |
| 33 | 445..566 | 122 | 122 | 85 | 37 | 6 | 2 | 29 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9364; unmatched reference entries: 778; unmatched candidate entries: 1117
- identity switches: 671; fragmentation (coverage interruptions): 570; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 2 -> 4 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 6 -> 2 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 7 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 6 -> 9 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78899: 5 -> 10 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 2 -> 11 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 9 -> 7 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 6 -> 9 at (2107, 3033), 1 frames after previous cover
- f98: ref 78899: 10 -> 6 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 5 -> 10 at (2129, 3028), 1 frames after previous cover
- f100: ref 78899: 6 -> 9 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 79097: 10 -> 6 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 5 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 79098: 10 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 10 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 12 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 6 -> 9 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 12 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 2 -> 11 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 7 -> 2 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 10 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 10 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 9 -> 7 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 11 -> 2 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 6 -> 5 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 78897: 9 -> 7 at (2052.5, 3032.5), 4 frames after previous cover
- f106: ref 79102: 6 -> 5 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 10 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 5 -> 10 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 79098: 5 -> 9 at (2090, 3028), 2 frames after previous cover
- f108: ref 78899: 7 -> 9 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79037: 7 -> 17 at (2026, 3034), 4 frames after previous cover
- f108: ref 79045: 2 -> 15 at (2014.5, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 6 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 78899: 9 -> 15 at (2043, 3030.5), 2 frames after previous cover
- f110: ref 79045: 15 -> 4 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 7 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 6 -> 9 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 10 -> 5 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 12 -> 10 at (2118, 3025), 5 frames after previous cover
- f111: ref 78897: 7 -> 15 at (2021.5, 3032.5), 2 frames after previous cover
- f111: ref 78899: 15 -> 7 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79102: 5 -> 19 at (2079, 3029.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 10 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 12 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f114: ref 78896: 4 -> 2 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 17 -> 4 at (1988, 3035), 1 frames after previous cover
- f114: ref 79045: 4 -> 17 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79097: 7 -> 22 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79110: 10 -> 21 at (2111, 3026.5), 1 frames after previous cover
- f115: ref 78971: 2 -> 17 at (1959, 3034), 2 frames after previous cover
- f115: ref 79111: 18 -> 10 at (2120, 3028.5), 1 frames after previous cover
- f115: ref 79115: 12 -> 18 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 79108: 10 -> 21 at (2087, 3026.5), 6 frames after previous cover
- f117: ref 79110: 21 -> 12 at (2094.5, 3027), 2 frames after previous cover
- f118: ref 78897: 15 -> 4 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 78899: 7 -> 15 at (1995, 3032.5), 1 frames after previous cover
- ... 611 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 981 | 14 | 1 (981) |
| 78896 | 350 (76..429) | 323 | 14 | 29 (275), 4 (25), 2 (23) |
| 78969 | 352 (80..434) | 326 | 21 | 25 (162), 17 (121), 11 (27), 2 (13), 29 (3) |
| 78971 | 352 (84..439) | 316 | 26 | 2 (180), 17 (112), 25 (16), 11 (6), 6 (2) |
| 79045 | 355 (84..443) | 318 | 22 | 25 (116), 17 (73), 32 (57), 2 (48), 7 (11), 11 (4), 4 (3), 15 (2), 23 (2), 5 (1), 6 (1) |
| 79037 | 355 (86..445) | 318 | 23 | 23 (178), 32 (99), 2 (17), 17 (6), 7 (4), 4 (4), 25 (4), 5 (2), 6 (2), 9 (2) |
| 78897 | 345 (89..450) | 313 | 20 | 23 (111), 2 (56), 32 (41), 31 (41), 4 (31), 6 (6), 15 (6), 9 (4), 7 (4), 25 (4), 11 (4), 17 (3), +1 more |
| 78899 | 365 (91..455) | 339 | 19 | 4 (187), 32 (91), 11 (24), 23 (14), 7 (8), 15 (4), 5 (3), 9 (3), 10 (2), 6 (2), 31 (1) |
| 79097 | 366 (94..461) | 331 | 26 | 11 (175), 4 (99), 15 (14), 32 (13), 31 (8), 9 (5), 22 (5), 5 (4), 7 (4), 10 (2), 6 (2) |
| 79098 | 360 (97..467) | 335 | 22 | 15 (128), 7 (70), 22 (69), 11 (36), 4 (15), 9 (9), 6 (4), 5 (3), 10 (1) |
| 79102 | 371 (98..477) | 325 | 35 | 15 (134), 22 (95), 7 (51), 11 (13), 19 (7), 5 (6), 31 (6), 26 (4), 10 (3), 9 (3), 6 (2), 4 (1) |
| 79103 | 380 (99..481) | 334 | 36 | 22 (77), 7 (66), 11 (60), 26 (40), 15 (40), 31 (22), 5 (13), 6 (10), 21 (3), 10 (2), 12 (1) |
| 79105 | 379 (101..484) | 353 | 26 | 7 (123), 21 (71), 22 (68), 31 (26), 5 (17), 11 (17), 26 (14), 15 (12), 10 (4), 12 (1) |
| 79108 | 385 (104..492) | 356 | 20 | 21 (205), 6 (55), 31 (41), 7 (39), 5 (10), 12 (2), 22 (2), 10 (1), 9 (1) |
| 79110 | 388 (106..497) | 353 | 27 | 5 (111), 21 (74), 31 (51), 19 (38), 9 (32), 22 (21), 6 (18), 12 (4), 10 (3), 26 (1) |
| 79111 | 386 (109..500) | 363 | 19 | 5 (127), 19 (116), 6 (41), 9 (37), 21 (17), 31 (13), 18 (4), 10 (3), 22 (3), 12 (1), 26 (1) |
| 79115 | 421 (111..531) | 383 | 29 | 30 (92), 19 (73), 5 (68), 6 (61), 12 (51), 9 (18), 22 (6), 18 (5), 26 (3), 28 (3), 31 (2), 21 (1) |
| 79116 | 411 (114..530) | 377 | 27 | 18 (150), 12 (64), 6 (38), 5 (33), 9 (30), 31 (30), 28 (19), 19 (11), 10 (2) |
| 79122 | 404 (118..532) | 373 | 24 | 28 (129), 6 (92), 12 (64), 18 (41), 31 (29), 19 (5), 30 (5), 26 (4), 10 (2), 9 (2) |
| 79132 | 391 (120..515) | 368 | 20 | 18 (80), 6 (79), 19 (63), 30 (51), 12 (46), 28 (30), 9 (10), 10 (4), 31 (3), 5 (1), 26 (1) |
| 79128 | 402 (124..527) | 378 | 20 | 10 (144), 19 (69), 28 (66), 12 (31), 26 (29), 31 (22), 9 (8), 30 (6), 18 (3) |
| 79134 | 407 (127..533) | 366 | 29 | 12 (128), 28 (92), 30 (79), 9 (26), 18 (24), 10 (11), 33 (5), 26 (1) |
| 79135 | 409 (129..542) | 386 | 21 | 10 (127), 18 (90), 9 (76), 28 (43), 26 (42), 12 (6), 30 (2) |
| 79139 | 406 (132..537) | 380 | 13 | 30 (150), 9 (91), 26 (86), 33 (52), 10 (1) |
| 79136 | 393 (136..538) | 369 | 17 | 26 (152), 10 (103), 9 (78), 33 (28), 12 (8) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 122/415/1004; tracks with internal gaps: 25; total internal gaps: 324; longest internal gap: 6; tracks ending in coasting: 24 (trailing rows total 691)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 981 | 23 | 14 | 4 | 0 | 78911 |
| 2 | 78..472 | 395 | 395 | 337 | 58 | 20 | 4 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 4 | 85..490 | 406 | 406 | 365 | 41 | 12 | 4 | 23 | 78896, 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 5 | 86..525 | 440 | 440 | 401 | 39 | 9 | 2 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 6 | 86..544 | 459 | 459 | 415 | 44 | 12 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 90..513 | 424 | 424 | 380 | 44 | 12 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 9 | 94..571 | 478 | 478 | 435 | 43 | 11 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 10 | 96..556 | 461 | 461 | 415 | 46 | 16 | 3 | 26 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 96..510 | 415 | 415 | 366 | 49 | 15 | 3 | 29 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..562 | 463 | 463 | 407 | 56 | 20 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 15 | 108..496 | 389 | 389 | 340 | 49 | 14 | 3 | 31 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105 |
| 17 | 108..468 | 361 | 361 | 315 | 46 | 13 | 3 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 18 | 111..559 | 449 | 449 | 397 | 52 | 16 | 2 | 32 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..529 | 419 | 419 | 382 | 37 | 8 | 1 | 29 | 79102, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 114..521 | 408 | 408 | 371 | 37 | 7 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 22 | 114..506 | 393 | 393 | 346 | 47 | 15 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 118..474 | 357 | 357 | 305 | 52 | 17 | 3 | 29 | 78897, 78899, 79037, 79045 |
| 25 | 124..463 | 340 | 340 | 302 | 38 | 9 | 1 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 26 | 128..567 | 440 | 440 | 378 | 62 | 19 | 6 | 29 | 79102, 79103, 79105, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 28 | 129..561 | 433 | 433 | 382 | 51 | 19 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 29 | 138..458 | 321 | 321 | 278 | 43 | 10 | 3 | 29 | 78896, 78969 |
| 30 | 139..560 | 422 | 422 | 385 | 37 | 6 | 2 | 29 | 79115, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 139..479 | 341 | 341 | 295 | 46 | 14 | 2 | 29 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 32 | 144..484 | 341 | 341 | 301 | 40 | 10 | 2 | 29 | 78897, 78899, 79037, 79045, 79097 |
| 33 | 445..566 | 122 | 122 | 85 | 37 | 6 | 2 | 29 | 79134, 79136, 79139 |
