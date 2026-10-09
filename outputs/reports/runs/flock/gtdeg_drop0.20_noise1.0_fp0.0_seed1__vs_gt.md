# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=fce9fde60f32
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise1.0_fp0.0_seed1/tracks.csv sha256=7b74de0c522cde4f
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise1.0_fp0.0_seed1.csv sha256=fce9fde60f32e4d1
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise1.0_fp0.0_seed1
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
| observations | none | 4 | 10142 | 8000 | 0.545 | 0.653 | 0.455 | 1.07 | 0.652 | 0.755 | 1.26 | 331 | 1621.0 | 0.759 | 0.861 | 0.679 | 0.788 | 0.999 | 7992 | 2150 | 8 | 6 | 19 | 0 |
| observations | none | 6 | 10142 | 8000 | 0.586 | 0.700 | 0.490 | 1.16 | 0.653 | 0.757 | 1.27 | 320 | 1613.0 | 0.761 | 0.862 | 0.680 | 0.789 | 1.000 | 8000 | 2142 | 0 | 6 | 19 | 0 |
| observations | none | 8 | 10142 | 8000 | 0.607 | 0.710 | 0.518 | 1.22 | 0.650 | 0.758 | 1.28 | 314 | 1608.0 | 0.762 | 0.864 | 0.681 | 0.789 | 1.000 | 7999 | 2143 | 1 | 7 | 18 | 0 |
| observations | none | 12 | 10142 | 8000 | 0.633 | 0.718 | 0.559 | 1.47 | 0.647 | 0.756 | 1.38 | 300 | 1597.0 | 0.765 | 0.867 | 0.684 | 0.787 | 0.998 | 7983 | 2159 | 17 | 7 | 18 | 0 |
| observations | ignore | 4 | 10142 | 8000 | 0.545 | 0.653 | 0.455 | 1.07 | 0.652 | 0.755 | 1.26 | 331 | 1621.0 | 0.759 | 0.861 | 0.679 | 0.788 | 0.999 | 7992 | 2150 | 8 | 6 | 19 | 0 |
| observations | ignore | 6 | 10142 | 8000 | 0.586 | 0.700 | 0.490 | 1.16 | 0.653 | 0.757 | 1.27 | 320 | 1613.0 | 0.761 | 0.862 | 0.680 | 0.789 | 1.000 | 8000 | 2142 | 0 | 6 | 19 | 0 |
| observations | ignore | 8 | 10142 | 8000 | 0.607 | 0.710 | 0.518 | 1.22 | 0.650 | 0.758 | 1.28 | 314 | 1608.0 | 0.762 | 0.864 | 0.681 | 0.789 | 1.000 | 7999 | 2143 | 1 | 7 | 18 | 0 |
| observations | ignore | 12 | 10142 | 8000 | 0.633 | 0.718 | 0.559 | 1.47 | 0.647 | 0.756 | 1.38 | 300 | 1597.0 | 0.765 | 0.867 | 0.684 | 0.787 | 0.998 | 7983 | 2159 | 17 | 7 | 18 | 0 |
| updates | none | 4 | 10142 | 10681 | 0.492 | 0.579 | 0.418 | 1.22 | 0.554 | 0.539 | 1.31 | 383 | 1515.0 | 0.685 | 0.667 | 0.703 | 0.815 | 0.774 | 8264 | 1878 | 2417 | 18 | 7 | 0 |
| updates | none | 6 | 10142 | 10681 | 0.573 | 0.670 | 0.489 | 1.51 | 0.618 | 0.648 | 1.55 | 381 | 1069.0 | 0.734 | 0.716 | 0.754 | 0.870 | 0.826 | 8819 | 1323 | 1862 | 24 | 1 | 0 |
| updates | none | 8 | 10142 | 10681 | 0.620 | 0.712 | 0.540 | 1.72 | 0.688 | 0.765 | 1.89 | 343 | 605.0 | 0.787 | 0.767 | 0.808 | 0.926 | 0.879 | 9393 | 749 | 1288 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10681 | 0.678 | 0.756 | 0.608 | 2.14 | 0.728 | 0.823 | 2.27 | 311 | 374.0 | 0.820 | 0.799 | 0.841 | 0.954 | 0.905 | 9671 | 471 | 1010 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10681 | 0.492 | 0.579 | 0.418 | 1.22 | 0.554 | 0.539 | 1.31 | 383 | 1515.0 | 0.685 | 0.667 | 0.703 | 0.815 | 0.774 | 8264 | 1878 | 2417 | 18 | 7 | 0 |
| updates | ignore | 6 | 10142 | 10681 | 0.573 | 0.670 | 0.489 | 1.51 | 0.618 | 0.648 | 1.55 | 381 | 1069.0 | 0.734 | 0.716 | 0.754 | 0.870 | 0.826 | 8819 | 1323 | 1862 | 24 | 1 | 0 |
| updates | ignore | 8 | 10142 | 10681 | 0.620 | 0.712 | 0.540 | 1.72 | 0.688 | 0.765 | 1.89 | 343 | 605.0 | 0.787 | 0.767 | 0.808 | 0.926 | 0.879 | 9393 | 749 | 1288 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10681 | 0.678 | 0.756 | 0.608 | 2.14 | 0.728 | 0.823 | 2.27 | 311 | 374.0 | 0.820 | 0.799 | 0.841 | 0.954 | 0.905 | 9671 | 471 | 1010 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 7999; unmatched reference entries: 2143; unmatched candidate entries: 1
- identity switches: 314; fragmentation (coverage interruptions): 1633; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 2 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 78899: 5 -> 7 at (2146.5, 3030.5), 1 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 2 frames after previous cover
- f95: ref 78899: 7 -> 5 at (2134.5, 3029), 1 frames after previous cover
- f95: ref 79097: 5 -> 7 at (2146.5, 3029), 1 frames after previous cover
- f96: ref 78899: 5 -> 6 at (2128, 3029), 1 frames after previous cover
- f97: ref 78897: 6 -> 5 at (2107, 3033), 2 frames after previous cover
- f97: ref 78971: 3 -> 8 at (2072, 3034.5), 6 frames after previous cover
- f98: ref 78971: 8 -> 3 at (2066, 3034), 1 frames after previous cover
- f99: ref 78897: 5 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 6 -> 5 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79037: 10 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79097: 7 -> 6 at (2122.5, 3028.5), 4 frames after previous cover
- f100: ref 78897: 10 -> 5 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78899: 5 -> 6 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 8 -> 10 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 13 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 7 -> 12 at (2130, 3027), 3 frames after previous cover
- f101: ref 78897: 5 -> 10 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 10 -> 8 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 13 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 12 -> 13 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 12 at (2136, 3025.5), 3 frames after previous cover
- f104: ref 79097: 6 -> 5 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79102: 12 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 9 -> 3 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 3 -> 16 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79103: 12 -> 5 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 6 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 5 -> 17 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 3 -> 8 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 8 -> 10 at (2031, 3033.5), 2 frames after previous cover
- f108: ref 78899: 17 -> 10 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 3 -> 9 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 8 -> 3 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 10 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 17 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 6 -> 7 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 7 -> 6 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 6 -> 5 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 9 -> 19 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 10 -> 20 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 13 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 7 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 18 at (2129, 3027), 3 frames after previous cover
- f114: ref 79103: 7 -> 13 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 5 -> 7 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 6 -> 5 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 18 -> 6 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 12 -> 18 at (2126, 3027), 1 frames after previous cover
- ... 254 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 785 | 175 | 0 (785) |
| 78896 | 350 (76..429) | 267 | 46 | 36 (208), 9 (34), 19 (21), 32 (3), 7 (1) |
| 78969 | 352 (80..434) | 274 | 58 | 32 (224), 9 (35), 3 (6), 8 (6), 19 (3) |
| 78971 | 352 (84..439) | 266 | 63 | 9 (202), 3 (30), 19 (27), 32 (5), 8 (2) |
| 79045 | 355 (84..443) | 284 | 55 | 19 (221), 16 (23), 3 (20), 8 (16), 7 (2), 6 (1), 9 (1) |
| 79037 | 355 (86..445) | 281 | 55 | 8 (236), 3 (25), 10 (10), 16 (5), 5 (2), 6 (2), 7 (1) |
| 78897 | 345 (89..450) | 269 | 55 | 3 (214), 16 (19), 20 (11), 10 (6), 5 (5), 6 (5), 13 (5), 8 (4) |
| 78899 | 365 (91..455) | 282 | 65 | 13 (226), 10 (17), 8 (15), 5 (6), 16 (6), 6 (4), 20 (3), 7 (2), 25 (2), 17 (1) |
| 79097 | 366 (94..461) | 281 | 59 | 25 (235), 10 (28), 6 (4), 13 (4), 5 (3), 17 (3), 8 (2), 7 (1), 23 (1) |
| 79098 | 360 (97..467) | 294 | 52 | 10 (243), 13 (15), 25 (14), 17 (7), 16 (6), 20 (4), 23 (2), 7 (1), 12 (1), 26 (1) |
| 79102 | 371 (98..477) | 296 | 50 | 26 (244), 20 (22), 13 (8), 25 (6), 23 (5), 7 (4), 12 (3), 6 (2), 16 (2) |
| 79103 | 380 (99..481) | 300 | 66 | 16 (248), 13 (16), 20 (11), 25 (9), 7 (5), 5 (4), 26 (3), 12 (2), 23 (2) |
| 79105 | 379 (101..484) | 299 | 62 | 20 (256), 7 (13), 13 (8), 23 (7), 26 (5), 5 (4), 25 (3), 6 (2), 34 (1) |
| 79108 | 385 (104..492) | 302 | 67 | 34 (260), 7 (16), 23 (12), 6 (5), 5 (5), 13 (2), 30 (1), 25 (1) |
| 79110 | 388 (106..497) | 304 | 66 | 23 (258), 7 (16), 34 (8), 5 (7), 6 (5), 18 (3), 13 (3), 12 (2), 30 (1), 33 (1) |
| 79111 | 386 (109..500) | 305 | 66 | 33 (274), 12 (5), 18 (5), 17 (5), 23 (4), 7 (4), 26 (3), 13 (3), 6 (1), 5 (1) |
| 79115 | 421 (111..531) | 339 | 58 | 35 (300), 5 (7), 33 (7), 23 (6), 6 (5), 12 (4), 26 (3), 7 (3), 17 (2), 21 (1), 18 (1) |
| 79116 | 411 (114..530) | 329 | 60 | 7 (280), 5 (14), 26 (13), 17 (7), 18 (5), 21 (3), 35 (3), 12 (2), 6 (2) |
| 79122 | 404 (118..532) | 338 | 55 | 5 (300), 17 (19), 12 (6), 26 (5), 18 (4), 21 (2), 6 (1), 30 (1) |
| 79132 | 391 (120..515) | 298 | 75 | 17 (267), 5 (11), 26 (7), 21 (5), 6 (4), 18 (3), 12 (1) |
| 79128 | 402 (124..527) | 312 | 67 | 18 (297), 6 (8), 12 (3), 21 (2), 17 (1), 30 (1) |
| 79134 | 407 (127..533) | 327 | 64 | 6 (282), 12 (38), 18 (5), 21 (2) |
| 79135 | 409 (129..542) | 323 | 73 | 12 (254), 21 (65), 18 (3), 6 (1) |
| 79139 | 406 (132..537) | 328 | 61 | 21 (264), 30 (48), 12 (16) |
| 79136 | 393 (136..538) | 316 | 60 | 30 (256), 6 (43), 21 (12), 12 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 249/374/1007; tracks with internal gaps: 1; total internal gaps: 1; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 785 | 785 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 82..450 | 369 | 295 | 295 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 5 | 86..532 | 447 | 369 | 369 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 88..537 | 450 | 377 | 377 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 7 | 88..529 | 442 | 349 | 349 | 0 | 0 | 0 | 0 | 78896, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 8 | 92..445 | 354 | 282 | 281 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 9 | 92..439 | 348 | 272 | 272 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 10 | 93..467 | 375 | 304 | 304 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098 |
| 12 | 100..533 | 434 | 342 | 342 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 100..454 | 355 | 290 | 290 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 16 | 106..481 | 376 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103 |
| 17 | 107..515 | 409 | 312 | 312 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79111, 79115, 79116, 79122, 79128, 79132 |
| 18 | 111..527 | 417 | 326 | 326 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..443 | 333 | 272 | 272 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 20 | 111..484 | 374 | 307 | 307 | 0 | 0 | 0 | 0 | 78897, 78899, 79098, 79102, 79103, 79105 |
| 21 | 113..542 | 430 | 356 | 356 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 119..497 | 379 | 297 | 297 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 25 | 129..461 | 333 | 270 | 270 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 130..477 | 348 | 284 | 284 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79132 |
| 30 | 139..536 | 398 | 308 | 308 | 0 | 0 | 0 | 0 | 79108, 79110, 79122, 79128, 79136, 79139 |
| 32 | 144..433 | 290 | 232 | 232 | 0 | 0 | 0 | 0 | 78896, 78969, 78971 |
| 33 | 144..500 | 357 | 282 | 282 | 0 | 0 | 0 | 0 | 79110, 79111, 79115 |
| 34 | 155..492 | 338 | 269 | 269 | 0 | 0 | 0 | 0 | 79105, 79108, 79110 |
| 35 | 159..531 | 373 | 303 | 303 | 0 | 0 | 0 | 0 | 79115, 79116 |
| 36 | 181..429 | 249 | 208 | 208 | 0 | 0 | 0 | 0 | 78896 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 7999; unmatched reference entries: 2143; unmatched candidate entries: 1
- identity switches: 314; fragmentation (coverage interruptions): 1633; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 2 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 78899: 5 -> 7 at (2146.5, 3030.5), 1 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 2 frames after previous cover
- f95: ref 78899: 7 -> 5 at (2134.5, 3029), 1 frames after previous cover
- f95: ref 79097: 5 -> 7 at (2146.5, 3029), 1 frames after previous cover
- f96: ref 78899: 5 -> 6 at (2128, 3029), 1 frames after previous cover
- f97: ref 78897: 6 -> 5 at (2107, 3033), 2 frames after previous cover
- f97: ref 78971: 3 -> 8 at (2072, 3034.5), 6 frames after previous cover
- f98: ref 78971: 8 -> 3 at (2066, 3034), 1 frames after previous cover
- f99: ref 78897: 5 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 6 -> 5 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79037: 10 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79097: 7 -> 6 at (2122.5, 3028.5), 4 frames after previous cover
- f100: ref 78897: 10 -> 5 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78899: 5 -> 6 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 8 -> 10 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 13 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 7 -> 12 at (2130, 3027), 3 frames after previous cover
- f101: ref 78897: 5 -> 10 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 10 -> 8 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 13 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 12 -> 13 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 12 at (2136, 3025.5), 3 frames after previous cover
- f104: ref 79097: 6 -> 5 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79102: 12 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 9 -> 3 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 3 -> 16 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79103: 12 -> 5 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 6 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 5 -> 17 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 3 -> 8 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 8 -> 10 at (2031, 3033.5), 2 frames after previous cover
- f108: ref 78899: 17 -> 10 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 3 -> 9 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 8 -> 3 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 10 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 17 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 6 -> 7 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 7 -> 6 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 6 -> 5 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 9 -> 19 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 10 -> 20 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 13 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 7 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 18 at (2129, 3027), 3 frames after previous cover
- f114: ref 79103: 7 -> 13 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 5 -> 7 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 6 -> 5 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 18 -> 6 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 12 -> 18 at (2126, 3027), 1 frames after previous cover
- ... 254 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 785 | 175 | 0 (785) |
| 78896 | 350 (76..429) | 267 | 46 | 36 (208), 9 (34), 19 (21), 32 (3), 7 (1) |
| 78969 | 352 (80..434) | 274 | 58 | 32 (224), 9 (35), 3 (6), 8 (6), 19 (3) |
| 78971 | 352 (84..439) | 266 | 63 | 9 (202), 3 (30), 19 (27), 32 (5), 8 (2) |
| 79045 | 355 (84..443) | 284 | 55 | 19 (221), 16 (23), 3 (20), 8 (16), 7 (2), 6 (1), 9 (1) |
| 79037 | 355 (86..445) | 281 | 55 | 8 (236), 3 (25), 10 (10), 16 (5), 5 (2), 6 (2), 7 (1) |
| 78897 | 345 (89..450) | 269 | 55 | 3 (214), 16 (19), 20 (11), 10 (6), 5 (5), 6 (5), 13 (5), 8 (4) |
| 78899 | 365 (91..455) | 282 | 65 | 13 (226), 10 (17), 8 (15), 5 (6), 16 (6), 6 (4), 20 (3), 7 (2), 25 (2), 17 (1) |
| 79097 | 366 (94..461) | 281 | 59 | 25 (235), 10 (28), 6 (4), 13 (4), 5 (3), 17 (3), 8 (2), 7 (1), 23 (1) |
| 79098 | 360 (97..467) | 294 | 52 | 10 (243), 13 (15), 25 (14), 17 (7), 16 (6), 20 (4), 23 (2), 7 (1), 12 (1), 26 (1) |
| 79102 | 371 (98..477) | 296 | 50 | 26 (244), 20 (22), 13 (8), 25 (6), 23 (5), 7 (4), 12 (3), 6 (2), 16 (2) |
| 79103 | 380 (99..481) | 300 | 66 | 16 (248), 13 (16), 20 (11), 25 (9), 7 (5), 5 (4), 26 (3), 12 (2), 23 (2) |
| 79105 | 379 (101..484) | 299 | 62 | 20 (256), 7 (13), 13 (8), 23 (7), 26 (5), 5 (4), 25 (3), 6 (2), 34 (1) |
| 79108 | 385 (104..492) | 302 | 67 | 34 (260), 7 (16), 23 (12), 6 (5), 5 (5), 13 (2), 30 (1), 25 (1) |
| 79110 | 388 (106..497) | 304 | 66 | 23 (258), 7 (16), 34 (8), 5 (7), 6 (5), 18 (3), 13 (3), 12 (2), 30 (1), 33 (1) |
| 79111 | 386 (109..500) | 305 | 66 | 33 (274), 12 (5), 18 (5), 17 (5), 23 (4), 7 (4), 26 (3), 13 (3), 6 (1), 5 (1) |
| 79115 | 421 (111..531) | 339 | 58 | 35 (300), 5 (7), 33 (7), 23 (6), 6 (5), 12 (4), 26 (3), 7 (3), 17 (2), 21 (1), 18 (1) |
| 79116 | 411 (114..530) | 329 | 60 | 7 (280), 5 (14), 26 (13), 17 (7), 18 (5), 21 (3), 35 (3), 12 (2), 6 (2) |
| 79122 | 404 (118..532) | 338 | 55 | 5 (300), 17 (19), 12 (6), 26 (5), 18 (4), 21 (2), 6 (1), 30 (1) |
| 79132 | 391 (120..515) | 298 | 75 | 17 (267), 5 (11), 26 (7), 21 (5), 6 (4), 18 (3), 12 (1) |
| 79128 | 402 (124..527) | 312 | 67 | 18 (297), 6 (8), 12 (3), 21 (2), 17 (1), 30 (1) |
| 79134 | 407 (127..533) | 327 | 64 | 6 (282), 12 (38), 18 (5), 21 (2) |
| 79135 | 409 (129..542) | 323 | 73 | 12 (254), 21 (65), 18 (3), 6 (1) |
| 79139 | 406 (132..537) | 328 | 61 | 21 (264), 30 (48), 12 (16) |
| 79136 | 393 (136..538) | 316 | 60 | 30 (256), 6 (43), 21 (12), 12 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 249/374/1007; tracks with internal gaps: 1; total internal gaps: 1; longest internal gap: 1; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 785 | 785 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 82..450 | 369 | 295 | 295 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 5 | 86..532 | 447 | 369 | 369 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 88..537 | 450 | 377 | 377 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 7 | 88..529 | 442 | 349 | 349 | 0 | 0 | 0 | 0 | 78896, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 8 | 92..445 | 354 | 282 | 281 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 9 | 92..439 | 348 | 272 | 272 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 10 | 93..467 | 375 | 304 | 304 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098 |
| 12 | 100..533 | 434 | 342 | 342 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 100..454 | 355 | 290 | 290 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 16 | 106..481 | 376 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103 |
| 17 | 107..515 | 409 | 312 | 312 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79111, 79115, 79116, 79122, 79128, 79132 |
| 18 | 111..527 | 417 | 326 | 326 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..443 | 333 | 272 | 272 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 20 | 111..484 | 374 | 307 | 307 | 0 | 0 | 0 | 0 | 78897, 78899, 79098, 79102, 79103, 79105 |
| 21 | 113..542 | 430 | 356 | 356 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 119..497 | 379 | 297 | 297 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 25 | 129..461 | 333 | 270 | 270 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 130..477 | 348 | 284 | 284 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79132 |
| 30 | 139..536 | 398 | 308 | 308 | 0 | 0 | 0 | 0 | 79108, 79110, 79122, 79128, 79136, 79139 |
| 32 | 144..433 | 290 | 232 | 232 | 0 | 0 | 0 | 0 | 78896, 78969, 78971 |
| 33 | 144..500 | 357 | 282 | 282 | 0 | 0 | 0 | 0 | 79110, 79111, 79115 |
| 34 | 155..492 | 338 | 269 | 269 | 0 | 0 | 0 | 0 | 79105, 79108, 79110 |
| 35 | 159..531 | 373 | 303 | 303 | 0 | 0 | 0 | 0 | 79115, 79116 |
| 36 | 181..429 | 249 | 208 | 208 | 0 | 0 | 0 | 0 | 78896 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9393; unmatched reference entries: 749; unmatched candidate entries: 1288
- identity switches: 343; fragmentation (coverage interruptions): 527; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 5 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78899: 7 -> 5 at (2134.5, 3029), 1 frames after previous cover
- f95: ref 79097: 5 -> 7 at (2146.5, 3029), 1 frames after previous cover
- f97: ref 78897: 6 -> 5 at (2107, 3033), 2 frames after previous cover
- f97: ref 78899: 5 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 78971: 3 -> 8 at (2072, 3034.5), 6 frames after previous cover
- f98: ref 78971: 8 -> 3 at (2066, 3034), 1 frames after previous cover
- f99: ref 78897: 5 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 6 -> 5 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79037: 10 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79097: 7 -> 6 at (2122.5, 3028.5), 3 frames after previous cover
- f100: ref 78897: 10 -> 5 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78899: 5 -> 6 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 8 -> 10 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 13 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 7 -> 12 at (2130, 3027), 3 frames after previous cover
- f101: ref 78897: 5 -> 10 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 10 -> 8 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 13 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 12 -> 13 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 12 at (2136, 3025.5), 3 frames after previous cover
- f104: ref 79097: 6 -> 5 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79102: 12 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 9 -> 3 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 3 -> 16 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79103: 12 -> 5 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 6 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 5 -> 17 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 3 -> 8 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 8 -> 10 at (2031, 3033.5), 1 frames after previous cover
- f108: ref 78899: 17 -> 10 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 3 -> 9 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 8 -> 3 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 10 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 17 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 6 -> 7 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 7 -> 6 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 6 -> 5 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 9 -> 19 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 10 -> 20 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 13 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 7 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 18 at (2129, 3027), 3 frames after previous cover
- f114: ref 79103: 7 -> 13 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 5 -> 7 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 6 -> 5 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 18 -> 6 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 12 -> 18 at (2126, 3027), 1 frames after previous cover
- ... 283 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 982 | 20 | 0 (982) |
| 78896 | 350 (76..429) | 298 | 21 | 36 (232), 9 (38), 19 (24), 32 (3), 7 (1) |
| 78969 | 352 (80..434) | 316 | 25 | 32 (262), 9 (39), 3 (6), 8 (6), 19 (3) |
| 78971 | 352 (84..439) | 313 | 25 | 9 (242), 3 (34), 19 (30), 32 (5), 8 (2) |
| 79045 | 355 (84..443) | 319 | 27 | 19 (254), 16 (23), 3 (20), 8 (18), 7 (2), 6 (1), 9 (1) |
| 79037 | 355 (86..445) | 326 | 17 | 8 (275), 3 (28), 10 (10), 16 (5), 5 (3), 6 (2), 7 (2), 19 (1) |
| 78897 | 345 (89..450) | 310 | 24 | 3 (249), 16 (22), 20 (12), 10 (7), 13 (6), 5 (5), 6 (5), 8 (4) |
| 78899 | 365 (91..455) | 334 | 23 | 13 (271), 10 (20), 8 (17), 5 (9), 16 (6), 6 (3), 20 (3), 25 (2), 7 (1), 17 (1), 3 (1) |
| 79097 | 366 (94..461) | 323 | 28 | 25 (271), 10 (32), 6 (4), 13 (4), 5 (3), 17 (3), 8 (3), 7 (2), 23 (1) |
| 79098 | 360 (97..467) | 334 | 21 | 10 (278), 13 (16), 25 (15), 17 (9), 16 (7), 20 (4), 23 (2), 7 (1), 12 (1), 26 (1) |
| 79102 | 371 (98..477) | 333 | 24 | 26 (281), 20 (22), 13 (8), 25 (6), 23 (5), 7 (4), 12 (3), 6 (2), 16 (2) |
| 79103 | 380 (99..481) | 354 | 18 | 16 (297), 13 (17), 20 (12), 25 (11), 7 (5), 5 (4), 26 (4), 12 (2), 23 (2) |
| 79105 | 379 (101..484) | 347 | 26 | 20 (300), 7 (14), 13 (8), 23 (8), 26 (5), 5 (4), 6 (3), 25 (3), 34 (1), 16 (1) |
| 79108 | 385 (104..492) | 354 | 22 | 34 (308), 7 (16), 23 (14), 5 (6), 6 (5), 30 (2), 13 (2), 25 (1) |
| 79110 | 388 (106..497) | 361 | 19 | 23 (313), 7 (18), 34 (8), 5 (7), 6 (5), 18 (3), 13 (3), 12 (2), 30 (1), 33 (1) |
| 79111 | 386 (109..500) | 359 | 22 | 33 (325), 18 (6), 12 (5), 17 (5), 23 (5), 13 (4), 7 (4), 26 (3), 6 (1), 5 (1) |
| 79115 | 421 (111..531) | 389 | 21 | 35 (346), 33 (10), 5 (7), 23 (6), 6 (5), 12 (4), 7 (4), 26 (3), 17 (2), 21 (1), 18 (1) |
| 79116 | 411 (114..530) | 393 | 16 | 7 (336), 5 (14), 26 (13), 17 (9), 18 (6), 35 (6), 21 (4), 12 (2), 6 (2), 33 (1) |
| 79122 | 404 (118..532) | 388 | 13 | 5 (360), 17 (9), 12 (6), 26 (5), 18 (4), 21 (2), 6 (1), 30 (1) |
| 79132 | 391 (120..515) | 366 | 20 | 17 (344), 26 (7), 21 (5), 6 (4), 18 (3), 7 (2), 12 (1) |
| 79128 | 402 (124..527) | 370 | 22 | 18 (352), 6 (8), 12 (3), 17 (3), 21 (2), 30 (2) |
| 79134 | 407 (127..533) | 384 | 17 | 6 (326), 12 (45), 18 (6), 21 (3), 30 (2), 17 (2) |
| 79135 | 409 (129..542) | 386 | 18 | 12 (302), 21 (78), 18 (5), 6 (1) |
| 79139 | 406 (132..537) | 382 | 18 | 21 (307), 6 (44), 12 (27), 7 (3), 30 (1) |
| 79136 | 393 (136..538) | 372 | 20 | 30 (359), 21 (12), 6 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 278/403/1007; tracks with internal gaps: 25; total internal gaps: 473; longest internal gap: 10; tracks ending in coasting: 24 (trailing rows total 671)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 982 | 25 | 20 | 2 | 0 | 78911 |
| 3 | 82..479 | 398 | 398 | 338 | 60 | 25 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 5 | 86..561 | 476 | 476 | 423 | 53 | 18 | 4 | 29 | 78897, 78899, 79037, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 6 | 88..566 | 479 | 479 | 423 | 56 | 20 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 88..558 | 471 | 471 | 415 | 56 | 22 | 5 | 21 | 78896, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132, 79139 |
| 8 | 92..474 | 383 | 383 | 325 | 58 | 18 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 9 | 92..468 | 377 | 377 | 320 | 57 | 21 | 2 | 29 | 78896, 78969, 78971, 79045 |
| 10 | 93..496 | 404 | 404 | 347 | 57 | 23 | 3 | 29 | 78897, 78899, 79037, 79097, 79098 |
| 12 | 100..562 | 463 | 463 | 403 | 60 | 24 | 2 | 31 | 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 100..483 | 384 | 384 | 339 | 45 | 13 | 2 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 16 | 106..510 | 405 | 405 | 363 | 42 | 11 | 2 | 29 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105 |
| 17 | 107..544 | 438 | 438 | 387 | 51 | 22 | 10 | 11 | 78899, 79097, 79098, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 18 | 111..556 | 446 | 446 | 386 | 60 | 20 | 3 | 32 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..472 | 362 | 362 | 312 | 50 | 19 | 2 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 20 | 111..513 | 403 | 403 | 353 | 50 | 19 | 2 | 29 | 78897, 78899, 79098, 79102, 79103, 79105 |
| 21 | 113..571 | 459 | 459 | 414 | 45 | 14 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 119..526 | 408 | 408 | 356 | 52 | 17 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 25 | 129..490 | 362 | 362 | 309 | 53 | 20 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 130..506 | 377 | 377 | 322 | 55 | 21 | 4 | 29 | 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79132 |
| 30 | 139..565 | 427 | 427 | 368 | 59 | 27 | 2 | 28 | 79108, 79110, 79122, 79128, 79134, 79136, 79139 |
| 32 | 144..462 | 319 | 319 | 270 | 49 | 17 | 3 | 28 | 78896, 78969, 78971 |
| 33 | 144..529 | 386 | 386 | 337 | 49 | 16 | 4 | 29 | 79110, 79111, 79115, 79116 |
| 34 | 155..521 | 367 | 367 | 317 | 50 | 18 | 2 | 29 | 79105, 79108, 79110 |
| 35 | 159..560 | 402 | 402 | 352 | 50 | 15 | 3 | 29 | 79115, 79116 |
| 36 | 181..458 | 278 | 278 | 232 | 46 | 13 | 3 | 29 | 78896 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9393; unmatched reference entries: 749; unmatched candidate entries: 1288
- identity switches: 343; fragmentation (coverage interruptions): 527; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 5 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78899: 7 -> 5 at (2134.5, 3029), 1 frames after previous cover
- f95: ref 79097: 5 -> 7 at (2146.5, 3029), 1 frames after previous cover
- f97: ref 78897: 6 -> 5 at (2107, 3033), 2 frames after previous cover
- f97: ref 78899: 5 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 78971: 3 -> 8 at (2072, 3034.5), 6 frames after previous cover
- f98: ref 78971: 8 -> 3 at (2066, 3034), 1 frames after previous cover
- f99: ref 78897: 5 -> 10 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 6 -> 5 at (2109.5, 3030), 1 frames after previous cover
- f99: ref 79037: 10 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79097: 7 -> 6 at (2122.5, 3028.5), 3 frames after previous cover
- f100: ref 78897: 10 -> 5 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78899: 5 -> 6 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 8 -> 10 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 13 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 7 -> 12 at (2130, 3027), 3 frames after previous cover
- f101: ref 78897: 5 -> 10 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 10 -> 8 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 13 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 12 -> 13 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 12 at (2136, 3025.5), 3 frames after previous cover
- f104: ref 79097: 6 -> 5 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79102: 12 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 9 -> 3 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 3 -> 16 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79103: 12 -> 5 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 6 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 5 -> 17 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 3 -> 8 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 8 -> 10 at (2031, 3033.5), 1 frames after previous cover
- f108: ref 78899: 17 -> 10 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 3 -> 9 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 8 -> 3 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 10 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 5 -> 17 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 6 -> 7 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 7 -> 6 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 6 -> 5 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 9 -> 19 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 10 -> 20 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 13 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 13 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 7 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79110: 12 -> 18 at (2129, 3027), 3 frames after previous cover
- f114: ref 79103: 7 -> 13 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 5 -> 7 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 6 -> 5 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 18 -> 6 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 12 -> 18 at (2126, 3027), 1 frames after previous cover
- ... 283 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 982 | 20 | 0 (982) |
| 78896 | 350 (76..429) | 298 | 21 | 36 (232), 9 (38), 19 (24), 32 (3), 7 (1) |
| 78969 | 352 (80..434) | 316 | 25 | 32 (262), 9 (39), 3 (6), 8 (6), 19 (3) |
| 78971 | 352 (84..439) | 313 | 25 | 9 (242), 3 (34), 19 (30), 32 (5), 8 (2) |
| 79045 | 355 (84..443) | 319 | 27 | 19 (254), 16 (23), 3 (20), 8 (18), 7 (2), 6 (1), 9 (1) |
| 79037 | 355 (86..445) | 326 | 17 | 8 (275), 3 (28), 10 (10), 16 (5), 5 (3), 6 (2), 7 (2), 19 (1) |
| 78897 | 345 (89..450) | 310 | 24 | 3 (249), 16 (22), 20 (12), 10 (7), 13 (6), 5 (5), 6 (5), 8 (4) |
| 78899 | 365 (91..455) | 334 | 23 | 13 (271), 10 (20), 8 (17), 5 (9), 16 (6), 6 (3), 20 (3), 25 (2), 7 (1), 17 (1), 3 (1) |
| 79097 | 366 (94..461) | 323 | 28 | 25 (271), 10 (32), 6 (4), 13 (4), 5 (3), 17 (3), 8 (3), 7 (2), 23 (1) |
| 79098 | 360 (97..467) | 334 | 21 | 10 (278), 13 (16), 25 (15), 17 (9), 16 (7), 20 (4), 23 (2), 7 (1), 12 (1), 26 (1) |
| 79102 | 371 (98..477) | 333 | 24 | 26 (281), 20 (22), 13 (8), 25 (6), 23 (5), 7 (4), 12 (3), 6 (2), 16 (2) |
| 79103 | 380 (99..481) | 354 | 18 | 16 (297), 13 (17), 20 (12), 25 (11), 7 (5), 5 (4), 26 (4), 12 (2), 23 (2) |
| 79105 | 379 (101..484) | 347 | 26 | 20 (300), 7 (14), 13 (8), 23 (8), 26 (5), 5 (4), 6 (3), 25 (3), 34 (1), 16 (1) |
| 79108 | 385 (104..492) | 354 | 22 | 34 (308), 7 (16), 23 (14), 5 (6), 6 (5), 30 (2), 13 (2), 25 (1) |
| 79110 | 388 (106..497) | 361 | 19 | 23 (313), 7 (18), 34 (8), 5 (7), 6 (5), 18 (3), 13 (3), 12 (2), 30 (1), 33 (1) |
| 79111 | 386 (109..500) | 359 | 22 | 33 (325), 18 (6), 12 (5), 17 (5), 23 (5), 13 (4), 7 (4), 26 (3), 6 (1), 5 (1) |
| 79115 | 421 (111..531) | 389 | 21 | 35 (346), 33 (10), 5 (7), 23 (6), 6 (5), 12 (4), 7 (4), 26 (3), 17 (2), 21 (1), 18 (1) |
| 79116 | 411 (114..530) | 393 | 16 | 7 (336), 5 (14), 26 (13), 17 (9), 18 (6), 35 (6), 21 (4), 12 (2), 6 (2), 33 (1) |
| 79122 | 404 (118..532) | 388 | 13 | 5 (360), 17 (9), 12 (6), 26 (5), 18 (4), 21 (2), 6 (1), 30 (1) |
| 79132 | 391 (120..515) | 366 | 20 | 17 (344), 26 (7), 21 (5), 6 (4), 18 (3), 7 (2), 12 (1) |
| 79128 | 402 (124..527) | 370 | 22 | 18 (352), 6 (8), 12 (3), 17 (3), 21 (2), 30 (2) |
| 79134 | 407 (127..533) | 384 | 17 | 6 (326), 12 (45), 18 (6), 21 (3), 30 (2), 17 (2) |
| 79135 | 409 (129..542) | 386 | 18 | 12 (302), 21 (78), 18 (5), 6 (1) |
| 79139 | 406 (132..537) | 382 | 18 | 21 (307), 6 (44), 12 (27), 7 (3), 30 (1) |
| 79136 | 393 (136..538) | 372 | 20 | 30 (359), 21 (12), 6 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 278/403/1007; tracks with internal gaps: 25; total internal gaps: 473; longest internal gap: 10; tracks ending in coasting: 24 (trailing rows total 671)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 982 | 25 | 20 | 2 | 0 | 78911 |
| 3 | 82..479 | 398 | 398 | 338 | 60 | 25 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 5 | 86..561 | 476 | 476 | 423 | 53 | 18 | 4 | 29 | 78897, 78899, 79037, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 6 | 88..566 | 479 | 479 | 423 | 56 | 20 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 88..558 | 471 | 471 | 415 | 56 | 22 | 5 | 21 | 78896, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132, 79139 |
| 8 | 92..474 | 383 | 383 | 325 | 58 | 18 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 9 | 92..468 | 377 | 377 | 320 | 57 | 21 | 2 | 29 | 78896, 78969, 78971, 79045 |
| 10 | 93..496 | 404 | 404 | 347 | 57 | 23 | 3 | 29 | 78897, 78899, 79037, 79097, 79098 |
| 12 | 100..562 | 463 | 463 | 403 | 60 | 24 | 2 | 31 | 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 100..483 | 384 | 384 | 339 | 45 | 13 | 2 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 16 | 106..510 | 405 | 405 | 363 | 42 | 11 | 2 | 29 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105 |
| 17 | 107..544 | 438 | 438 | 387 | 51 | 22 | 10 | 11 | 78899, 79097, 79098, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 18 | 111..556 | 446 | 446 | 386 | 60 | 20 | 3 | 32 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 19 | 111..472 | 362 | 362 | 312 | 50 | 19 | 2 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 20 | 111..513 | 403 | 403 | 353 | 50 | 19 | 2 | 29 | 78897, 78899, 79098, 79102, 79103, 79105 |
| 21 | 113..571 | 459 | 459 | 414 | 45 | 14 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 119..526 | 408 | 408 | 356 | 52 | 17 | 3 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 25 | 129..490 | 362 | 362 | 309 | 53 | 20 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 130..506 | 377 | 377 | 322 | 55 | 21 | 4 | 29 | 79098, 79102, 79103, 79105, 79111, 79115, 79116, 79122, 79132 |
| 30 | 139..565 | 427 | 427 | 368 | 59 | 27 | 2 | 28 | 79108, 79110, 79122, 79128, 79134, 79136, 79139 |
| 32 | 144..462 | 319 | 319 | 270 | 49 | 17 | 3 | 28 | 78896, 78969, 78971 |
| 33 | 144..529 | 386 | 386 | 337 | 49 | 16 | 4 | 29 | 79110, 79111, 79115, 79116 |
| 34 | 155..521 | 367 | 367 | 317 | 50 | 18 | 2 | 29 | 79105, 79108, 79110 |
| 35 | 159..560 | 402 | 402 | 352 | 50 | 15 | 3 | 29 | 79115, 79116 |
| 36 | 181..458 | 278 | 278 | 232 | 46 | 13 | 3 | 29 | 78896 |
