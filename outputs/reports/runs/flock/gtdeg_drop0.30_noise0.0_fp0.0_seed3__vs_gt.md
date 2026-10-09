# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=9e1e5050a8bb
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise0.0_fp0.0_seed3/tracks.csv sha256=6ebed87e5e7db51f
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise0.0_fp0.0_seed3.csv sha256=9e1e5050a8bb5220
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise0.0_fp0.0_seed3
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
| observations | none | 4 | 10142 | 7001 | 0.337 | 0.689 | 0.165 | 0.01 | 0.338 | 0.595 | 0.01 | 969 | 2109.0 | 0.327 | 0.400 | 0.276 | 0.690 | 1.000 | 7001 | 3141 | 0 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 7001 | 0.338 | 0.687 | 0.166 | 0.02 | 0.338 | 0.595 | 0.01 | 967 | 2109.0 | 0.327 | 0.400 | 0.276 | 0.690 | 1.000 | 7001 | 3141 | 0 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 7001 | 0.337 | 0.678 | 0.168 | 0.06 | 0.336 | 0.595 | 0.03 | 963 | 2106.0 | 0.328 | 0.402 | 0.277 | 0.690 | 1.000 | 7001 | 3141 | 0 | 0 | 25 | 0 |
| observations | none | 12 | 10142 | 7001 | 0.338 | 0.661 | 0.173 | 0.28 | 0.338 | 0.598 | 0.29 | 924 | 2065.0 | 0.339 | 0.416 | 0.287 | 0.690 | 0.999 | 6995 | 3147 | 6 | 0 | 25 | 0 |
| observations | ignore | 4 | 10142 | 7001 | 0.337 | 0.689 | 0.165 | 0.01 | 0.338 | 0.595 | 0.01 | 969 | 2109.0 | 0.327 | 0.400 | 0.276 | 0.690 | 1.000 | 7001 | 3141 | 0 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 7001 | 0.338 | 0.687 | 0.166 | 0.02 | 0.338 | 0.595 | 0.01 | 967 | 2109.0 | 0.327 | 0.400 | 0.276 | 0.690 | 1.000 | 7001 | 3141 | 0 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 7001 | 0.337 | 0.678 | 0.168 | 0.06 | 0.336 | 0.595 | 0.03 | 963 | 2106.0 | 0.328 | 0.402 | 0.277 | 0.690 | 1.000 | 7001 | 3141 | 0 | 0 | 25 | 0 |
| observations | ignore | 12 | 10142 | 7001 | 0.338 | 0.661 | 0.173 | 0.28 | 0.338 | 0.598 | 0.29 | 924 | 2065.0 | 0.339 | 0.416 | 0.287 | 0.690 | 0.999 | 6995 | 3147 | 6 | 0 | 25 | 0 |
| updates | none | 4 | 10142 | 9982 | 0.319 | 0.602 | 0.169 | 0.30 | 0.310 | 0.365 | 0.14 | 1022 | 1995.0 | 0.304 | 0.306 | 0.301 | 0.725 | 0.737 | 7352 | 2790 | 2630 | 1 | 24 | 0 |
| updates | none | 6 | 10142 | 9982 | 0.349 | 0.658 | 0.185 | 0.61 | 0.355 | 0.492 | 0.56 | 1042 | 1528.0 | 0.337 | 0.340 | 0.334 | 0.790 | 0.802 | 8009 | 2133 | 1973 | 8 | 17 | 0 |
| updates | none | 8 | 10142 | 9982 | 0.368 | 0.686 | 0.198 | 0.87 | 0.394 | 0.628 | 1.08 | 999 | 1049.0 | 0.364 | 0.367 | 0.361 | 0.856 | 0.869 | 8677 | 1465 | 1305 | 23 | 2 | 0 |
| updates | none | 12 | 10142 | 9982 | 0.391 | 0.717 | 0.214 | 1.34 | 0.414 | 0.681 | 1.62 | 931 | 854.0 | 0.389 | 0.392 | 0.386 | 0.878 | 0.893 | 8909 | 1233 | 1073 | 24 | 1 | 0 |
| updates | ignore | 4 | 10142 | 9982 | 0.319 | 0.602 | 0.169 | 0.30 | 0.310 | 0.365 | 0.14 | 1022 | 1995.0 | 0.304 | 0.306 | 0.301 | 0.725 | 0.737 | 7352 | 2790 | 2630 | 1 | 24 | 0 |
| updates | ignore | 6 | 10142 | 9982 | 0.349 | 0.658 | 0.185 | 0.61 | 0.355 | 0.492 | 0.56 | 1042 | 1528.0 | 0.337 | 0.340 | 0.334 | 0.790 | 0.802 | 8009 | 2133 | 1973 | 8 | 17 | 0 |
| updates | ignore | 8 | 10142 | 9982 | 0.368 | 0.686 | 0.198 | 0.87 | 0.394 | 0.628 | 1.08 | 999 | 1049.0 | 0.364 | 0.367 | 0.361 | 0.856 | 0.869 | 8677 | 1465 | 1305 | 23 | 2 | 0 |
| updates | ignore | 12 | 10142 | 9982 | 0.391 | 0.717 | 0.214 | 1.34 | 0.414 | 0.681 | 1.62 | 931 | 854.0 | 0.389 | 0.392 | 0.386 | 0.878 | 0.893 | 8909 | 1233 | 1073 | 24 | 1 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7001; unmatched reference entries: 3141; unmatched candidate entries: 0
- identity switches: 963; fragmentation (coverage interruptions): 2157; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 6 -> 5 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 5 -> 6 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 6 -> 5 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 5 -> 7 at (2090.5, 3033), 4 frames after previous cover
- f87: ref 79037: 6 -> 5 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 78971: 5 -> 9 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 8 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 8 -> 6 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 9 -> 6 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 6 -> 8 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 8 -> 9 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 6 -> 9 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 6 -> 7 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 9 -> 6 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 8 -> 11 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 8 -> 11 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 11 -> 7 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 5 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 7 -> 14 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 8 -> 12 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 7 -> 6 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 6 -> 7 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 5 -> 8 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 7 -> 9 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 9 -> 7 at (2061, 3032.5), 2 frames after previous cover
- f101: ref 79097: 8 -> 12 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 5 -> 8 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 11 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 11 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 8 -> 7 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 12 -> 9 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 9 -> 11 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 8 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 5 -> 16 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 7 -> 9 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 11 -> 7 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 8 -> 16 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 7 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 12 -> 8 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 9 -> 7 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 12 -> 16 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 16 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 9 -> 7 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 7 -> 11 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 16 -> 18 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 12 -> 16 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 18 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 16 -> 18 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78971: 11 -> 14 at (1996.5, 3034.5), 4 frames after previous cover
- f109: ref 79037: 7 -> 11 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 16 -> 8 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 12 -> 16 at (2107.5, 3023.5), 1 frames after previous cover
- ... 903 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 696 | 218 | 3 (696) |
| 78896 | 350 (76..429) | 252 | 70 | 6 (160), 16 (72), 14 (10), 7 (7), 5 (3) |
| 78969 | 352 (80..434) | 240 | 71 | 22 (108), 6 (75), 16 (30), 28 (19), 32 (3), 8 (2), 7 (2), 11 (1) |
| 78971 | 352 (84..439) | 247 | 67 | 25 (58), 32 (42), 26 (41), 6 (35), 16 (34), 30 (11), 11 (9), 22 (8), 9 (5), 14 (2), 5 (1), 7 (1) |
| 79045 | 355 (84..443) | 247 | 79 | 25 (59), 22 (51), 16 (30), 30 (28), 26 (23), 28 (17), 9 (12), 6 (7), 14 (5), 7 (4), 32 (4), 11 (3), +2 more |
| 79037 | 355 (86..445) | 245 | 75 | 9 (85), 16 (50), 26 (34), 22 (20), 32 (12), 30 (10), 25 (9), 11 (8), 7 (4), 28 (4), 6 (3), 5 (2), +3 more |
| 78897 | 345 (89..450) | 236 | 82 | 11 (63), 9 (30), 25 (23), 27 (21), 26 (21), 22 (20), 16 (14), 8 (12), 5 (11), 28 (10), 20 (7), 7 (3), +1 more |
| 78899 | 365 (91..455) | 240 | 81 | 11 (62), 22 (43), 9 (31), 28 (27), 25 (26), 20 (9), 8 (7), 5 (6), 26 (6), 16 (5), 14 (4), 7 (4), +3 more |
| 79097 | 366 (94..461) | 243 | 85 | 11 (85), 28 (37), 25 (22), 20 (20), 5 (17), 31 (17), 9 (16), 27 (11), 8 (3), 7 (3), 24 (3), 30 (3), +4 more |
| 79098 | 360 (97..467) | 236 | 82 | 28 (56), 11 (48), 31 (37), 7 (24), 25 (13), 20 (12), 5 (9), 9 (9), 30 (8), 8 (7), 32 (5), 27 (3), +3 more |
| 79102 | 371 (98..477) | 252 | 89 | 31 (80), 7 (41), 28 (40), 8 (22), 27 (16), 32 (13), 26 (12), 5 (6), 30 (4), 11 (4), 12 (3), 18 (3), +5 more |
| 79103 | 380 (99..481) | 257 | 82 | 31 (86), 8 (76), 5 (18), 7 (16), 28 (16), 26 (11), 27 (8), 16 (6), 18 (5), 30 (4), 24 (3), 32 (3), +4 more |
| 79105 | 379 (101..484) | 259 | 76 | 26 (85), 31 (54), 8 (35), 27 (24), 5 (20), 7 (15), 28 (6), 30 (4), 12 (3), 18 (3), 20 (3), 14 (2), +3 more |
| 79108 | 385 (104..492) | 271 | 73 | 8 (80), 5 (66), 27 (41), 32 (23), 25 (11), 26 (10), 20 (8), 7 (8), 31 (7), 21 (5), 9 (4), 30 (4), +3 more |
| 79110 | 388 (106..497) | 269 | 76 | 32 (50), 7 (39), 27 (37), 21 (31), 5 (27), 26 (23), 25 (14), 8 (11), 24 (8), 9 (8), 19 (8), 30 (5), +3 more |
| 79111 | 386 (109..500) | 275 | 80 | 21 (106), 7 (31), 5 (28), 18 (24), 8 (23), 9 (20), 19 (14), 20 (13), 26 (11), 12 (2), 25 (1), 24 (1), +1 more |
| 79115 | 421 (111..531) | 291 | 88 | 18 (88), 21 (33), 7 (29), 8 (28), 27 (24), 12 (22), 5 (19), 20 (13), 24 (12), 19 (9), 9 (6), 25 (6), +1 more |
| 79116 | 411 (114..530) | 276 | 95 | 5 (108), 19 (32), 24 (28), 27 (23), 12 (14), 9 (14), 30 (13), 21 (12), 18 (9), 7 (8), 20 (6), 14 (4), +2 more |
| 79122 | 404 (118..532) | 269 | 88 | 19 (96), 12 (38), 7 (31), 27 (30), 21 (22), 24 (17), 18 (16), 5 (5), 25 (4), 20 (4), 9 (3), 14 (2), +1 more |
| 79132 | 391 (120..515) | 274 | 82 | 12 (78), 19 (66), 30 (44), 9 (38), 18 (16), 7 (14), 21 (8), 24 (5), 14 (3), 5 (2) |
| 79128 | 402 (124..527) | 279 | 86 | 30 (139), 19 (58), 12 (26), 14 (20), 21 (18), 7 (9), 18 (7), 8 (2) |
| 79134 | 407 (127..533) | 292 | 85 | 14 (160), 18 (82), 30 (20), 24 (12), 12 (7), 21 (6), 19 (5) |
| 79135 | 409 (129..542) | 286 | 87 | 14 (97), 20 (73), 18 (41), 33 (41), 19 (15), 21 (9), 12 (6), 24 (4) |
| 79139 | 406 (132..537) | 294 | 82 | 20 (141), 21 (46), 12 (34), 33 (27), 24 (26), 18 (8), 14 (7), 19 (5) |
| 79136 | 393 (136..538) | 275 | 78 | 24 (176), 12 (57), 33 (27), 20 (9), 18 (6) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 120/385/995; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 12..1006 | 995 | 696 | 696 | 0 | 0 | 0 | 0 | 78911 |
| 5 | 81..530 | 450 | 350 | 350 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 84..438 | 355 | 280 | 280 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 7 | 87..477 | 391 | 293 | 293 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 8 | 88..492 | 405 | 314 | 314 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128 |
| 9 | 88..445 | 358 | 284 | 284 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 11 | 97..467 | 371 | 283 | 283 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 12 | 99..515 | 417 | 298 | 298 | 0 | 0 | 0 | 0 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..533 | 435 | 326 | 326 | 0 | 0 | 0 | 0 | 78896, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 16 | 103..427 | 325 | 247 | 247 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 18 | 107..530 | 424 | 313 | 313 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 113..531 | 419 | 308 | 308 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 116..542 | 427 | 322 | 322 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79135, 79136, 79139 |
| 21 | 116..500 | 385 | 296 | 296 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 120..454 | 335 | 250 | 250 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 24 | 129..537 | 409 | 301 | 301 | 0 | 0 | 0 | 0 | 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 25 | 129..501 | 373 | 253 | 253 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122 |
| 26 | 132..484 | 353 | 277 | 277 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111 |
| 27 | 135..460 | 326 | 244 | 244 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 28 | 135..434 | 300 | 232 | 232 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 30 | 141..527 | 387 | 299 | 299 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79116, 79122, 79128, 79132, 79134 |
| 31 | 141..481 | 341 | 281 | 281 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 32 | 284..495 | 212 | 159 | 159 | 0 | 0 | 0 | 0 | 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110 |
| 33 | 418..537 | 120 | 95 | 95 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 7001; unmatched reference entries: 3141; unmatched candidate entries: 0
- identity switches: 963; fragmentation (coverage interruptions): 2157; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 6 -> 5 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 5 -> 6 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 6 -> 5 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 5 -> 7 at (2090.5, 3033), 4 frames after previous cover
- f87: ref 79037: 6 -> 5 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 78971: 5 -> 9 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 8 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 8 -> 6 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 9 -> 6 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 6 -> 8 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 8 -> 9 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 6 -> 9 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 6 -> 7 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 9 -> 6 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 8 -> 11 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 8 -> 11 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 11 -> 7 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 5 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 7 -> 14 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 8 -> 12 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 7 -> 6 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 6 -> 7 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 5 -> 8 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 7 -> 9 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 9 -> 7 at (2061, 3032.5), 2 frames after previous cover
- f101: ref 79097: 8 -> 12 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 5 -> 8 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 11 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 11 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 8 -> 7 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 12 -> 9 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 9 -> 11 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 8 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 5 -> 16 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 7 -> 9 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 11 -> 7 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 8 -> 16 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 7 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 12 -> 8 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 9 -> 7 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 12 -> 16 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 16 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 9 -> 7 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 7 -> 11 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 16 -> 18 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 12 -> 16 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 18 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 16 -> 18 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78971: 11 -> 14 at (1996.5, 3034.5), 4 frames after previous cover
- f109: ref 79037: 7 -> 11 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 16 -> 8 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 12 -> 16 at (2107.5, 3023.5), 1 frames after previous cover
- ... 903 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 696 | 218 | 3 (696) |
| 78896 | 350 (76..429) | 252 | 70 | 6 (160), 16 (72), 14 (10), 7 (7), 5 (3) |
| 78969 | 352 (80..434) | 240 | 71 | 22 (108), 6 (75), 16 (30), 28 (19), 32 (3), 8 (2), 7 (2), 11 (1) |
| 78971 | 352 (84..439) | 247 | 67 | 25 (58), 32 (42), 26 (41), 6 (35), 16 (34), 30 (11), 11 (9), 22 (8), 9 (5), 14 (2), 5 (1), 7 (1) |
| 79045 | 355 (84..443) | 247 | 79 | 25 (59), 22 (51), 16 (30), 30 (28), 26 (23), 28 (17), 9 (12), 6 (7), 14 (5), 7 (4), 32 (4), 11 (3), +2 more |
| 79037 | 355 (86..445) | 245 | 75 | 9 (85), 16 (50), 26 (34), 22 (20), 32 (12), 30 (10), 25 (9), 11 (8), 7 (4), 28 (4), 6 (3), 5 (2), +3 more |
| 78897 | 345 (89..450) | 236 | 82 | 11 (63), 9 (30), 25 (23), 27 (21), 26 (21), 22 (20), 16 (14), 8 (12), 5 (11), 28 (10), 20 (7), 7 (3), +1 more |
| 78899 | 365 (91..455) | 240 | 81 | 11 (62), 22 (43), 9 (31), 28 (27), 25 (26), 20 (9), 8 (7), 5 (6), 26 (6), 16 (5), 14 (4), 7 (4), +3 more |
| 79097 | 366 (94..461) | 243 | 85 | 11 (85), 28 (37), 25 (22), 20 (20), 5 (17), 31 (17), 9 (16), 27 (11), 8 (3), 7 (3), 24 (3), 30 (3), +4 more |
| 79098 | 360 (97..467) | 236 | 82 | 28 (56), 11 (48), 31 (37), 7 (24), 25 (13), 20 (12), 5 (9), 9 (9), 30 (8), 8 (7), 32 (5), 27 (3), +3 more |
| 79102 | 371 (98..477) | 252 | 89 | 31 (80), 7 (41), 28 (40), 8 (22), 27 (16), 32 (13), 26 (12), 5 (6), 30 (4), 11 (4), 12 (3), 18 (3), +5 more |
| 79103 | 380 (99..481) | 257 | 82 | 31 (86), 8 (76), 5 (18), 7 (16), 28 (16), 26 (11), 27 (8), 16 (6), 18 (5), 30 (4), 24 (3), 32 (3), +4 more |
| 79105 | 379 (101..484) | 259 | 76 | 26 (85), 31 (54), 8 (35), 27 (24), 5 (20), 7 (15), 28 (6), 30 (4), 12 (3), 18 (3), 20 (3), 14 (2), +3 more |
| 79108 | 385 (104..492) | 271 | 73 | 8 (80), 5 (66), 27 (41), 32 (23), 25 (11), 26 (10), 20 (8), 7 (8), 31 (7), 21 (5), 9 (4), 30 (4), +3 more |
| 79110 | 388 (106..497) | 269 | 76 | 32 (50), 7 (39), 27 (37), 21 (31), 5 (27), 26 (23), 25 (14), 8 (11), 24 (8), 9 (8), 19 (8), 30 (5), +3 more |
| 79111 | 386 (109..500) | 275 | 80 | 21 (106), 7 (31), 5 (28), 18 (24), 8 (23), 9 (20), 19 (14), 20 (13), 26 (11), 12 (2), 25 (1), 24 (1), +1 more |
| 79115 | 421 (111..531) | 291 | 88 | 18 (88), 21 (33), 7 (29), 8 (28), 27 (24), 12 (22), 5 (19), 20 (13), 24 (12), 19 (9), 9 (6), 25 (6), +1 more |
| 79116 | 411 (114..530) | 276 | 95 | 5 (108), 19 (32), 24 (28), 27 (23), 12 (14), 9 (14), 30 (13), 21 (12), 18 (9), 7 (8), 20 (6), 14 (4), +2 more |
| 79122 | 404 (118..532) | 269 | 88 | 19 (96), 12 (38), 7 (31), 27 (30), 21 (22), 24 (17), 18 (16), 5 (5), 25 (4), 20 (4), 9 (3), 14 (2), +1 more |
| 79132 | 391 (120..515) | 274 | 82 | 12 (78), 19 (66), 30 (44), 9 (38), 18 (16), 7 (14), 21 (8), 24 (5), 14 (3), 5 (2) |
| 79128 | 402 (124..527) | 279 | 86 | 30 (139), 19 (58), 12 (26), 14 (20), 21 (18), 7 (9), 18 (7), 8 (2) |
| 79134 | 407 (127..533) | 292 | 85 | 14 (160), 18 (82), 30 (20), 24 (12), 12 (7), 21 (6), 19 (5) |
| 79135 | 409 (129..542) | 286 | 87 | 14 (97), 20 (73), 18 (41), 33 (41), 19 (15), 21 (9), 12 (6), 24 (4) |
| 79139 | 406 (132..537) | 294 | 82 | 20 (141), 21 (46), 12 (34), 33 (27), 24 (26), 18 (8), 14 (7), 19 (5) |
| 79136 | 393 (136..538) | 275 | 78 | 24 (176), 12 (57), 33 (27), 20 (9), 18 (6) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 120/385/995; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 12..1006 | 995 | 696 | 696 | 0 | 0 | 0 | 0 | 78911 |
| 5 | 81..530 | 450 | 350 | 350 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 84..438 | 355 | 280 | 280 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 7 | 87..477 | 391 | 293 | 293 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 8 | 88..492 | 405 | 314 | 314 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128 |
| 9 | 88..445 | 358 | 284 | 284 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 11 | 97..467 | 371 | 283 | 283 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 12 | 99..515 | 417 | 298 | 298 | 0 | 0 | 0 | 0 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..533 | 435 | 326 | 326 | 0 | 0 | 0 | 0 | 78896, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 16 | 103..427 | 325 | 247 | 247 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 18 | 107..530 | 424 | 313 | 313 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 113..531 | 419 | 308 | 308 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 116..542 | 427 | 322 | 322 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79135, 79136, 79139 |
| 21 | 116..500 | 385 | 296 | 296 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 120..454 | 335 | 250 | 250 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 24 | 129..537 | 409 | 301 | 301 | 0 | 0 | 0 | 0 | 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 25 | 129..501 | 373 | 253 | 253 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122 |
| 26 | 132..484 | 353 | 277 | 277 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111 |
| 27 | 135..460 | 326 | 244 | 244 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 28 | 135..434 | 300 | 232 | 232 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 30 | 141..527 | 387 | 299 | 299 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79116, 79122, 79128, 79132, 79134 |
| 31 | 141..481 | 341 | 281 | 281 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 32 | 284..495 | 212 | 159 | 159 | 0 | 0 | 0 | 0 | 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110 |
| 33 | 418..537 | 120 | 95 | 95 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8677; unmatched reference entries: 1465; unmatched candidate entries: 1305
- identity switches: 999; fragmentation (coverage interruptions): 983; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 6 -> 5 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 5 -> 6 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 6 -> 5 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 5 -> 7 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 5 -> 9 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79037: 6 -> 5 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 8 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 8 -> 6 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 9 -> 6 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 6 -> 8 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 8 -> 9 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 6 -> 9 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 6 -> 7 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 9 -> 6 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 8 -> 11 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 8 -> 11 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 11 -> 7 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 5 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 7 -> 14 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 8 -> 12 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 7 -> 6 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 6 -> 7 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 5 -> 8 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 7 -> 9 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 9 -> 7 at (2061, 3032.5), 1 frames after previous cover
- f101: ref 79097: 8 -> 12 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 5 -> 8 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 11 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 11 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 8 -> 7 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 12 -> 9 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 9 -> 11 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 8 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 5 -> 16 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 7 -> 9 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 11 -> 7 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 8 -> 16 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 7 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 12 -> 8 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 9 -> 7 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 12 -> 16 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 16 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 9 -> 7 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 7 -> 11 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 16 -> 18 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 12 -> 16 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 18 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 16 -> 18 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78971: 11 -> 14 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79037: 7 -> 11 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 16 -> 8 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 12 -> 16 at (2107.5, 3023.5), 1 frames after previous cover
- ... 939 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 963 | 24 | 3 (963) |
| 78896 | 350 (76..429) | 311 | 26 | 6 (197), 16 (91), 14 (11), 7 (9), 5 (3) |
| 78969 | 352 (80..434) | 292 | 36 | 22 (131), 6 (90), 16 (39), 28 (23), 32 (4), 8 (2), 7 (2), 11 (1) |
| 78971 | 352 (84..439) | 293 | 39 | 25 (67), 32 (53), 26 (50), 16 (42), 6 (40), 30 (14), 11 (11), 22 (7), 9 (5), 14 (2), 5 (1), 7 (1) |
| 79045 | 355 (84..443) | 295 | 41 | 25 (69), 22 (65), 16 (37), 30 (30), 26 (25), 28 (25), 9 (15), 6 (8), 14 (5), 32 (5), 7 (4), 11 (3), +2 more |
| 79037 | 355 (86..445) | 290 | 45 | 9 (103), 16 (58), 26 (39), 22 (24), 32 (15), 25 (14), 30 (11), 11 (9), 6 (4), 7 (4), 28 (4), 8 (2), +3 more |
| 78897 | 345 (89..450) | 279 | 53 | 11 (74), 9 (36), 25 (28), 26 (25), 22 (24), 27 (23), 16 (16), 8 (15), 5 (14), 28 (11), 20 (8), 7 (4), +1 more |
| 78899 | 365 (91..455) | 292 | 45 | 11 (74), 22 (53), 9 (36), 25 (35), 28 (34), 20 (10), 26 (10), 5 (8), 8 (8), 16 (5), 27 (5), 14 (4), +3 more |
| 79097 | 366 (94..461) | 295 | 45 | 11 (109), 28 (44), 25 (26), 20 (22), 9 (20), 31 (19), 5 (17), 27 (15), 8 (4), 7 (4), 14 (3), 24 (3), +5 more |
| 79098 | 360 (97..467) | 276 | 55 | 28 (62), 11 (56), 31 (41), 7 (36), 25 (16), 20 (14), 9 (10), 5 (9), 30 (9), 8 (7), 27 (6), 32 (5), +3 more |
| 79102 | 371 (98..477) | 302 | 49 | 31 (93), 7 (55), 28 (47), 8 (24), 27 (19), 26 (16), 32 (15), 5 (7), 11 (7), 25 (4), 30 (4), 12 (3), +5 more |
| 79103 | 380 (99..481) | 305 | 50 | 8 (96), 31 (96), 5 (21), 7 (20), 28 (20), 26 (13), 27 (12), 16 (6), 18 (5), 30 (4), 32 (4), 24 (3), +4 more |
| 79105 | 379 (101..484) | 308 | 42 | 26 (102), 31 (62), 8 (44), 27 (33), 5 (21), 7 (16), 28 (9), 20 (4), 30 (4), 12 (3), 18 (3), 14 (2), +3 more |
| 79108 | 385 (104..492) | 322 | 40 | 8 (97), 5 (76), 27 (51), 32 (28), 25 (13), 26 (13), 20 (10), 7 (10), 31 (7), 30 (5), 21 (4), 9 (4), +3 more |
| 79110 | 388 (106..497) | 329 | 38 | 32 (66), 7 (48), 27 (46), 21 (35), 5 (32), 26 (28), 25 (16), 8 (11), 9 (10), 19 (10), 24 (9), 18 (5), +3 more |
| 79111 | 386 (109..500) | 335 | 30 | 21 (137), 7 (40), 5 (33), 18 (28), 8 (27), 9 (22), 19 (15), 20 (13), 26 (12), 12 (3), 27 (3), 25 (1), +1 more |
| 79115 | 421 (111..531) | 365 | 41 | 18 (128), 21 (37), 8 (34), 7 (34), 27 (28), 12 (27), 5 (24), 20 (16), 24 (13), 25 (7), 19 (6), 9 (6), +2 more |
| 79116 | 411 (114..530) | 356 | 39 | 5 (143), 19 (47), 24 (35), 27 (27), 12 (18), 21 (16), 9 (16), 30 (15), 18 (13), 7 (9), 20 (6), 14 (4), +2 more |
| 79122 | 404 (118..532) | 338 | 43 | 19 (127), 12 (46), 7 (39), 27 (33), 18 (26), 21 (25), 24 (18), 5 (6), 25 (5), 9 (5), 20 (4), 14 (2), +1 more |
| 79132 | 391 (120..515) | 340 | 36 | 12 (102), 19 (81), 30 (50), 9 (49), 18 (17), 7 (17), 21 (9), 24 (6), 14 (5), 5 (4) |
| 79128 | 402 (124..527) | 345 | 41 | 30 (181), 19 (72), 12 (30), 21 (21), 14 (21), 7 (10), 18 (7), 8 (3) |
| 79134 | 407 (127..533) | 361 | 33 | 14 (197), 18 (100), 30 (26), 24 (14), 12 (10), 19 (7), 21 (7) |
| 79135 | 409 (129..542) | 364 | 34 | 14 (129), 20 (94), 33 (50), 18 (48), 19 (21), 21 (9), 12 (7), 24 (6) |
| 79139 | 406 (132..537) | 375 | 25 | 20 (185), 21 (57), 12 (42), 24 (36), 33 (30), 18 (11), 14 (9), 19 (5) |
| 79136 | 393 (136..538) | 346 | 33 | 24 (214), 12 (74), 33 (36), 20 (12), 18 (6), 19 (3), 14 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 149/414/997; tracks with internal gaps: 24; total internal gaps: 445; longest internal gap: 25; tracks ending in coasting: 24 (trailing rows total 644)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 12..1008 | 997 | 997 | 963 | 34 | 24 | 3 | 1 | 78911 |
| 5 | 81..559 | 479 | 479 | 422 | 57 | 22 | 4 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 84..467 | 384 | 384 | 339 | 45 | 14 | 3 | 28 | 78896, 78969, 78971, 79037, 79045 |
| 7 | 87..506 | 420 | 420 | 366 | 54 | 21 | 5 | 25 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 8 | 88..521 | 434 | 434 | 379 | 55 | 18 | 4 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128 |
| 9 | 88..474 | 387 | 387 | 340 | 47 | 11 | 4 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 11 | 97..496 | 400 | 400 | 344 | 56 | 19 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 12 | 99..544 | 446 | 446 | 374 | 72 | 29 | 6 | 29 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..562 | 464 | 464 | 403 | 61 | 24 | 2 | 29 | 78896, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 103..456 | 354 | 354 | 300 | 54 | 20 | 4 | 27 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 18 | 107..559 | 453 | 453 | 402 | 51 | 17 | 6 | 28 | 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 113..560 | 448 | 448 | 394 | 54 | 21 | 3 | 22 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 116..571 | 456 | 456 | 404 | 52 | 15 | 3 | 32 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79135, 79136, 79139 |
| 21 | 116..529 | 414 | 414 | 357 | 57 | 17 | 5 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 120..483 | 364 | 364 | 306 | 58 | 24 | 4 | 23 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 24 | 129..566 | 438 | 438 | 364 | 74 | 33 | 5 | 24 | 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 25 | 129..530 | 402 | 402 | 306 | 96 | 23 | 25 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122 |
| 26 | 132..513 | 382 | 382 | 333 | 49 | 15 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111 |
| 27 | 135..489 | 355 | 355 | 302 | 53 | 17 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 28 | 135..463 | 329 | 329 | 279 | 50 | 17 | 2 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 30 | 141..556 | 416 | 416 | 367 | 49 | 15 | 3 | 29 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134 |
| 31 | 141..510 | 370 | 370 | 318 | 52 | 16 | 2 | 32 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 32 | 284..524 | 241 | 241 | 199 | 42 | 9 | 3 | 27 | 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110 |
| 33 | 418..566 | 149 | 149 | 116 | 33 | 4 | 1 | 29 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8677; unmatched reference entries: 1465; unmatched candidate entries: 1305
- identity switches: 999; fragmentation (coverage interruptions): 983; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 6 -> 5 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 5 -> 6 at (2153, 3032), 1 frames after previous cover
- f86: ref 79045: 6 -> 5 at (2147.5, 3033), 1 frames after previous cover
- f87: ref 78896: 5 -> 7 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 5 -> 9 at (2125.5, 3034), 3 frames after previous cover
- f88: ref 79037: 6 -> 5 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 5 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 6 -> 8 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78969: 8 -> 6 at (2089.5, 3031.5), 2 frames after previous cover
- f92: ref 78971: 9 -> 6 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79037: 6 -> 8 at (2124, 3034), 2 frames after previous cover
- f92: ref 79045: 8 -> 9 at (2110.5, 3033.5), 1 frames after previous cover
- f94: ref 78897: 5 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78971: 6 -> 9 at (2090.5, 3032.5), 1 frames after previous cover
- f96: ref 78899: 5 -> 8 at (2128, 3029), 2 frames after previous cover
- f96: ref 78969: 6 -> 7 at (2059.5, 3036), 1 frames after previous cover
- f96: ref 78971: 9 -> 6 at (2077, 3034.5), 2 frames after previous cover
- f97: ref 79037: 8 -> 11 at (2093, 3032.5), 4 frames after previous cover
- f98: ref 78897: 8 -> 11 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 11 -> 7 at (2087, 3034), 1 frames after previous cover
- f98: ref 79097: 5 -> 8 at (2129, 3028), 2 frames after previous cover
- f99: ref 78896: 7 -> 14 at (2016, 3034), 4 frames after previous cover
- f99: ref 78899: 8 -> 12 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 78969: 7 -> 6 at (2041.5, 3033.5), 2 frames after previous cover
- f99: ref 78971: 6 -> 7 at (2059.5, 3034), 1 frames after previous cover
- f99: ref 79098: 5 -> 8 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 7 -> 9 at (2076, 3033.5), 2 frames after previous cover
- f100: ref 79045: 9 -> 7 at (2061, 3032.5), 1 frames after previous cover
- f101: ref 79097: 8 -> 12 at (2111.5, 3028.5), 3 frames after previous cover
- f101: ref 79102: 5 -> 8 at (2136, 3025.5), 2 frames after previous cover
- f102: ref 78897: 11 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 11 at (2041, 3033), 2 frames after previous cover
- f103: ref 78897: 8 -> 7 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 12 -> 9 at (2086, 3030), 1 frames after previous cover
- f103: ref 79037: 9 -> 11 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79102: 8 -> 12 at (2124.5, 3027.5), 2 frames after previous cover
- f103: ref 79103: 5 -> 16 at (2133.5, 3022.5), 3 frames after previous cover
- f104: ref 78897: 7 -> 9 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 9 -> 8 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 11 -> 7 at (2051, 3034), 1 frames after previous cover
- f104: ref 79098: 8 -> 16 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79037: 7 -> 9 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79097: 12 -> 8 at (2088, 3029), 4 frames after previous cover
- f106: ref 79037: 9 -> 7 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79102: 12 -> 16 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 16 -> 12 at (2116.5, 3023), 1 frames after previous cover
- f107: ref 78897: 9 -> 7 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 3 frames after previous cover
- f107: ref 79045: 7 -> 11 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79098: 16 -> 18 at (2090, 3028), 3 frames after previous cover
- f107: ref 79103: 12 -> 16 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 5 -> 12 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79098: 18 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 16 -> 18 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78971: 11 -> 14 at (1996.5, 3034.5), 3 frames after previous cover
- f109: ref 79037: 7 -> 11 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 16 -> 8 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 12 -> 16 at (2107.5, 3023.5), 1 frames after previous cover
- ... 939 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 963 | 24 | 3 (963) |
| 78896 | 350 (76..429) | 311 | 26 | 6 (197), 16 (91), 14 (11), 7 (9), 5 (3) |
| 78969 | 352 (80..434) | 292 | 36 | 22 (131), 6 (90), 16 (39), 28 (23), 32 (4), 8 (2), 7 (2), 11 (1) |
| 78971 | 352 (84..439) | 293 | 39 | 25 (67), 32 (53), 26 (50), 16 (42), 6 (40), 30 (14), 11 (11), 22 (7), 9 (5), 14 (2), 5 (1), 7 (1) |
| 79045 | 355 (84..443) | 295 | 41 | 25 (69), 22 (65), 16 (37), 30 (30), 26 (25), 28 (25), 9 (15), 6 (8), 14 (5), 32 (5), 7 (4), 11 (3), +2 more |
| 79037 | 355 (86..445) | 290 | 45 | 9 (103), 16 (58), 26 (39), 22 (24), 32 (15), 25 (14), 30 (11), 11 (9), 6 (4), 7 (4), 28 (4), 8 (2), +3 more |
| 78897 | 345 (89..450) | 279 | 53 | 11 (74), 9 (36), 25 (28), 26 (25), 22 (24), 27 (23), 16 (16), 8 (15), 5 (14), 28 (11), 20 (8), 7 (4), +1 more |
| 78899 | 365 (91..455) | 292 | 45 | 11 (74), 22 (53), 9 (36), 25 (35), 28 (34), 20 (10), 26 (10), 5 (8), 8 (8), 16 (5), 27 (5), 14 (4), +3 more |
| 79097 | 366 (94..461) | 295 | 45 | 11 (109), 28 (44), 25 (26), 20 (22), 9 (20), 31 (19), 5 (17), 27 (15), 8 (4), 7 (4), 14 (3), 24 (3), +5 more |
| 79098 | 360 (97..467) | 276 | 55 | 28 (62), 11 (56), 31 (41), 7 (36), 25 (16), 20 (14), 9 (10), 5 (9), 30 (9), 8 (7), 27 (6), 32 (5), +3 more |
| 79102 | 371 (98..477) | 302 | 49 | 31 (93), 7 (55), 28 (47), 8 (24), 27 (19), 26 (16), 32 (15), 5 (7), 11 (7), 25 (4), 30 (4), 12 (3), +5 more |
| 79103 | 380 (99..481) | 305 | 50 | 8 (96), 31 (96), 5 (21), 7 (20), 28 (20), 26 (13), 27 (12), 16 (6), 18 (5), 30 (4), 32 (4), 24 (3), +4 more |
| 79105 | 379 (101..484) | 308 | 42 | 26 (102), 31 (62), 8 (44), 27 (33), 5 (21), 7 (16), 28 (9), 20 (4), 30 (4), 12 (3), 18 (3), 14 (2), +3 more |
| 79108 | 385 (104..492) | 322 | 40 | 8 (97), 5 (76), 27 (51), 32 (28), 25 (13), 26 (13), 20 (10), 7 (10), 31 (7), 30 (5), 21 (4), 9 (4), +3 more |
| 79110 | 388 (106..497) | 329 | 38 | 32 (66), 7 (48), 27 (46), 21 (35), 5 (32), 26 (28), 25 (16), 8 (11), 9 (10), 19 (10), 24 (9), 18 (5), +3 more |
| 79111 | 386 (109..500) | 335 | 30 | 21 (137), 7 (40), 5 (33), 18 (28), 8 (27), 9 (22), 19 (15), 20 (13), 26 (12), 12 (3), 27 (3), 25 (1), +1 more |
| 79115 | 421 (111..531) | 365 | 41 | 18 (128), 21 (37), 8 (34), 7 (34), 27 (28), 12 (27), 5 (24), 20 (16), 24 (13), 25 (7), 19 (6), 9 (6), +2 more |
| 79116 | 411 (114..530) | 356 | 39 | 5 (143), 19 (47), 24 (35), 27 (27), 12 (18), 21 (16), 9 (16), 30 (15), 18 (13), 7 (9), 20 (6), 14 (4), +2 more |
| 79122 | 404 (118..532) | 338 | 43 | 19 (127), 12 (46), 7 (39), 27 (33), 18 (26), 21 (25), 24 (18), 5 (6), 25 (5), 9 (5), 20 (4), 14 (2), +1 more |
| 79132 | 391 (120..515) | 340 | 36 | 12 (102), 19 (81), 30 (50), 9 (49), 18 (17), 7 (17), 21 (9), 24 (6), 14 (5), 5 (4) |
| 79128 | 402 (124..527) | 345 | 41 | 30 (181), 19 (72), 12 (30), 21 (21), 14 (21), 7 (10), 18 (7), 8 (3) |
| 79134 | 407 (127..533) | 361 | 33 | 14 (197), 18 (100), 30 (26), 24 (14), 12 (10), 19 (7), 21 (7) |
| 79135 | 409 (129..542) | 364 | 34 | 14 (129), 20 (94), 33 (50), 18 (48), 19 (21), 21 (9), 12 (7), 24 (6) |
| 79139 | 406 (132..537) | 375 | 25 | 20 (185), 21 (57), 12 (42), 24 (36), 33 (30), 18 (11), 14 (9), 19 (5) |
| 79136 | 393 (136..538) | 346 | 33 | 24 (214), 12 (74), 33 (36), 20 (12), 18 (6), 19 (3), 14 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 149/414/997; tracks with internal gaps: 24; total internal gaps: 445; longest internal gap: 25; tracks ending in coasting: 24 (trailing rows total 644)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 12..1008 | 997 | 997 | 963 | 34 | 24 | 3 | 1 | 78911 |
| 5 | 81..559 | 479 | 479 | 422 | 57 | 22 | 4 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 84..467 | 384 | 384 | 339 | 45 | 14 | 3 | 28 | 78896, 78969, 78971, 79037, 79045 |
| 7 | 87..506 | 420 | 420 | 366 | 54 | 21 | 5 | 25 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 8 | 88..521 | 434 | 434 | 379 | 55 | 18 | 4 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128 |
| 9 | 88..474 | 387 | 387 | 340 | 47 | 11 | 4 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 11 | 97..496 | 400 | 400 | 344 | 56 | 19 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 12 | 99..544 | 446 | 446 | 374 | 72 | 29 | 6 | 29 | 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 99..562 | 464 | 464 | 403 | 61 | 24 | 2 | 29 | 78896, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 16 | 103..456 | 354 | 354 | 300 | 54 | 20 | 4 | 27 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 18 | 107..559 | 453 | 453 | 402 | 51 | 17 | 6 | 28 | 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 113..560 | 448 | 448 | 394 | 54 | 21 | 3 | 22 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 116..571 | 456 | 456 | 404 | 52 | 15 | 3 | 32 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79135, 79136, 79139 |
| 21 | 116..529 | 414 | 414 | 357 | 57 | 17 | 5 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 120..483 | 364 | 364 | 306 | 58 | 24 | 4 | 23 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 24 | 129..566 | 438 | 438 | 364 | 74 | 33 | 5 | 24 | 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 25 | 129..530 | 402 | 402 | 306 | 96 | 23 | 25 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122 |
| 26 | 132..513 | 382 | 382 | 333 | 49 | 15 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110, 79111 |
| 27 | 135..489 | 355 | 355 | 302 | 53 | 17 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 28 | 135..463 | 329 | 329 | 279 | 50 | 17 | 2 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 30 | 141..556 | 416 | 416 | 367 | 49 | 15 | 3 | 29 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134 |
| 31 | 141..510 | 370 | 370 | 318 | 52 | 16 | 2 | 32 | 79097, 79098, 79102, 79103, 79105, 79108 |
| 32 | 284..524 | 241 | 241 | 199 | 42 | 9 | 3 | 27 | 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110 |
| 33 | 418..566 | 149 | 149 | 116 | 33 | 4 | 1 | 29 | 79135, 79136, 79139 |
