# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=3418d0610592
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise0.0_fp0.5_seed1/tracks.csv sha256=7931055f6aaaf5ef
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise0.0_fp0.5_seed1.csv sha256=3418d0610592677c
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise0.0_fp0.5_seed1
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
| observations | none | 4 | 10142 | 8081 | 0.360 | 0.785 | 0.165 | 0.01 | 0.360 | 0.688 | 0.01 | 1003 | 1589.0 | 0.314 | 0.354 | 0.282 | 0.792 | 0.994 | 8031 | 2111 | 50 | 8 | 17 | 0 |
| observations | none | 6 | 10142 | 8081 | 0.360 | 0.775 | 0.167 | 0.04 | 0.358 | 0.688 | 0.02 | 1000 | 1587.0 | 0.315 | 0.355 | 0.283 | 0.792 | 0.994 | 8031 | 2111 | 50 | 8 | 17 | 0 |
| observations | none | 8 | 10142 | 8081 | 0.360 | 0.765 | 0.170 | 0.12 | 0.358 | 0.689 | 0.06 | 991 | 1580.0 | 0.318 | 0.359 | 0.286 | 0.792 | 0.994 | 8031 | 2111 | 50 | 9 | 16 | 0 |
| observations | none | 12 | 10142 | 8081 | 0.363 | 0.759 | 0.173 | 0.27 | 0.366 | 0.694 | 0.38 | 916 | 1551.0 | 0.331 | 0.373 | 0.297 | 0.791 | 0.992 | 8020 | 2122 | 61 | 8 | 17 | 0 |
| observations | ignore | 4 | 10142 | 8081 | 0.360 | 0.785 | 0.165 | 0.01 | 0.360 | 0.688 | 0.01 | 1003 | 1589.0 | 0.314 | 0.354 | 0.282 | 0.792 | 0.994 | 8031 | 2111 | 50 | 8 | 17 | 0 |
| observations | ignore | 6 | 10142 | 8081 | 0.360 | 0.775 | 0.167 | 0.04 | 0.358 | 0.688 | 0.02 | 1000 | 1587.0 | 0.315 | 0.355 | 0.283 | 0.792 | 0.994 | 8031 | 2111 | 50 | 8 | 17 | 0 |
| observations | ignore | 8 | 10142 | 8081 | 0.360 | 0.765 | 0.170 | 0.12 | 0.358 | 0.689 | 0.06 | 991 | 1580.0 | 0.318 | 0.359 | 0.286 | 0.792 | 0.994 | 8031 | 2111 | 50 | 9 | 16 | 0 |
| observations | ignore | 12 | 10142 | 8081 | 0.363 | 0.759 | 0.173 | 0.27 | 0.366 | 0.694 | 0.38 | 916 | 1551.0 | 0.331 | 0.373 | 0.297 | 0.791 | 0.992 | 8020 | 2122 | 61 | 8 | 17 | 0 |
| updates | none | 4 | 10142 | 10548 | 0.336 | 0.683 | 0.165 | 0.19 | 0.332 | 0.490 | 0.09 | 1023 | 1495.0 | 0.295 | 0.289 | 0.300 | 0.815 | 0.784 | 8269 | 1873 | 2279 | 18 | 7 | 0 |
| updates | none | 6 | 10142 | 10548 | 0.355 | 0.714 | 0.177 | 0.41 | 0.359 | 0.577 | 0.35 | 1015 | 1159.0 | 0.315 | 0.309 | 0.322 | 0.858 | 0.825 | 8706 | 1436 | 1842 | 24 | 1 | 0 |
| updates | none | 8 | 10142 | 10548 | 0.367 | 0.729 | 0.185 | 0.61 | 0.385 | 0.669 | 0.72 | 988 | 790.0 | 0.333 | 0.327 | 0.340 | 0.903 | 0.868 | 9159 | 983 | 1389 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10548 | 0.382 | 0.750 | 0.195 | 0.92 | 0.401 | 0.698 | 1.16 | 898 | 662.0 | 0.352 | 0.345 | 0.359 | 0.913 | 0.878 | 9261 | 881 | 1287 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10548 | 0.336 | 0.683 | 0.165 | 0.19 | 0.332 | 0.490 | 0.09 | 1023 | 1495.0 | 0.295 | 0.289 | 0.300 | 0.815 | 0.784 | 8269 | 1873 | 2279 | 18 | 7 | 0 |
| updates | ignore | 6 | 10142 | 10548 | 0.355 | 0.714 | 0.177 | 0.41 | 0.359 | 0.577 | 0.35 | 1015 | 1159.0 | 0.315 | 0.309 | 0.322 | 0.858 | 0.825 | 8706 | 1436 | 1842 | 24 | 1 | 0 |
| updates | ignore | 8 | 10142 | 10548 | 0.367 | 0.729 | 0.185 | 0.61 | 0.385 | 0.669 | 0.72 | 988 | 790.0 | 0.333 | 0.327 | 0.340 | 0.903 | 0.868 | 9159 | 983 | 1389 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10548 | 0.382 | 0.750 | 0.195 | 0.92 | 0.401 | 0.698 | 1.16 | 898 | 662.0 | 0.352 | 0.345 | 0.359 | 0.913 | 0.878 | 9261 | 881 | 1287 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8031; unmatched reference entries: 2111; unmatched candidate entries: 50
- identity switches: 991; fragmentation (coverage interruptions): 1590; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 27 -> 32 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 33 -> 34 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 34 -> 27 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 33 -> 34 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 34 -> 38 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 33 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 34 -> 42 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78897: 34 -> 42 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 33 -> 44 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 27 -> 45 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 42 -> 38 at (2099, 3033.5), 2 frames after previous cover
- f98: ref 78899: 44 -> 34 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 33 -> 44 at (2129, 3028), 1 frames after previous cover
- f100: ref 79098: 33 -> 44 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 34 -> 42 at (2098.5, 3030.5), 3 frames after previous cover
- f101: ref 79098: 44 -> 34 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 33 -> 44 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 48 -> 33 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79097: 44 -> 34 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 34 -> 42 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 48 -> 33 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 27 -> 45 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 38 -> 27 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 44 -> 34 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 33 -> 44 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 42 -> 48 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 45 -> 27 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 34 -> 33 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 79045: 27 -> 38 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79102: 34 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 44 -> 34 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 33 -> 44 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 33 -> 42 at (2090, 3028), 2 frames after previous cover
- f108: ref 79037: 38 -> 55 at (2026, 3034), 4 frames after previous cover
- f108: ref 79105: 44 -> 34 at (2113.5, 3025), 2 frames after previous cover
- f110: ref 78899: 48 -> 55 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 55 -> 38 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 38 -> 32 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 42 -> 48 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79102: 33 -> 42 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 34 -> 60 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 34 -> 33 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 48 -> 34 at (2118, 3025), 6 frames after previous cover
- f111: ref 78897: 42 -> 48 at (2021.5, 3032.5), 9 frames after previous cover
- f111: ref 79098: 42 -> 61 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79110: 44 -> 34 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 44 -> 62 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 42 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 60 -> 42 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 34 -> 60 at (2109, 3027), 2 frames after previous cover
- f113: ref 79103: 42 -> 61 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 33 -> 42 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 60 -> 33 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 34 -> 60 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 78896: 32 -> 27 at (1921, 3035), 5 frames after previous cover
- f114: ref 79097: 48 -> 67 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79098: 61 -> 68 at (2048, 3030), 3 frames after previous cover
- f114: ref 79110: 60 -> 33 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 62 -> 34 at (2126, 3027), 1 frames after previous cover
- f115: ref 78971: 27 -> 32 at (1959, 3034), 2 frames after previous cover
- ... 931 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 153 | 2 (799) |
| 78896 | 350 (76..429) | 277 | 53 | 83 (89), 84 (76), 125 (50), 27 (38), 32 (24) |
| 78969 | 352 (80..434) | 287 | 48 | 27 (77), 84 (63), 90 (61), 38 (35), 45 (24), 83 (23), 77 (4) |
| 78971 | 352 (84..439) | 269 | 54 | 62 (92), 27 (76), 84 (59), 90 (25), 45 (6), 38 (4), 34 (2), 32 (2), 77 (2), 125 (1) |
| 79045 | 355 (84..443) | 286 | 53 | 90 (114), 154 (44), 62 (42), 38 (20), 27 (19), 42 (14), 32 (13), 45 (6), 77 (4), 84 (4), 48 (3), 33 (1), +2 more |
| 79037 | 355 (86..445) | 276 | 53 | 45 (52), 38 (50), 62 (41), 84 (41), 90 (20), 32 (19), 27 (16), 48 (13), 154 (8), 42 (7), 77 (3), 33 (2), +2 more |
| 78897 | 345 (89..450) | 272 | 48 | 48 (49), 38 (46), 42 (38), 77 (38), 32 (34), 62 (17), 84 (17), 27 (14), 34 (5), 154 (5), 45 (4), 155 (3), +1 more |
| 78899 | 365 (91..455) | 298 | 51 | 48 (82), 155 (73), 32 (43), 42 (34), 125 (26), 38 (10), 154 (7), 55 (5), 45 (4), 27 (4), 33 (3), 61 (3), +3 more |
| 79097 | 366 (94..461) | 291 | 57 | 48 (53), 32 (41), 38 (38), 42 (37), 125 (33), 154 (28), 155 (26), 61 (16), 27 (7), 33 (4), 55 (3), 44 (2), +3 more |
| 79098 | 360 (97..467) | 281 | 66 | 27 (74), 61 (43), 42 (39), 73 (35), 62 (18), 38 (13), 125 (13), 48 (12), 155 (9), 32 (4), 77 (4), 33 (3), +7 more |
| 79102 | 371 (98..477) | 278 | 67 | 48 (70), 42 (52), 62 (49), 32 (30), 73 (14), 38 (10), 68 (8), 45 (8), 154 (7), 125 (6), 75 (5), 33 (4), +7 more |
| 79103 | 380 (99..481) | 291 | 67 | 132 (68), 73 (52), 55 (32), 125 (30), 48 (24), 38 (23), 42 (15), 62 (13), 68 (8), 32 (7), 45 (6), 61 (3), +6 more |
| 79105 | 379 (101..484) | 309 | 59 | 73 (110), 45 (58), 32 (32), 42 (28), 55 (17), 68 (14), 155 (10), 38 (9), 33 (6), 132 (6), 48 (5), 75 (5), +5 more |
| 79108 | 385 (104..492) | 313 | 58 | 67 (93), 38 (41), 73 (41), 32 (28), 132 (26), 68 (23), 45 (22), 33 (17), 55 (9), 42 (4), 77 (3), 75 (2), +4 more |
| 79110 | 388 (106..497) | 305 | 62 | 180 (75), 132 (48), 75 (40), 32 (35), 68 (21), 67 (20), 42 (19), 33 (16), 55 (10), 45 (7), 73 (3), 38 (3), +4 more |
| 79111 | 386 (109..500) | 321 | 53 | 68 (137), 75 (48), 33 (42), 67 (19), 73 (17), 132 (15), 42 (9), 55 (8), 77 (7), 34 (5), 32 (5), 62 (4), +2 more |
| 79115 | 421 (111..531) | 339 | 62 | 182 (90), 75 (82), 68 (41), 33 (27), 77 (27), 67 (21), 73 (19), 44 (10), 42 (7), 55 (4), 87 (4), 34 (3), +2 more |
| 79116 | 411 (114..530) | 320 | 67 | 34 (77), 67 (44), 75 (36), 87 (27), 73 (22), 77 (19), 185 (19), 44 (17), 86 (13), 33 (11), 68 (10), 132 (9), +4 more |
| 79122 | 404 (118..532) | 311 | 72 | 75 (87), 67 (56), 68 (41), 86 (39), 87 (28), 44 (22), 182 (15), 55 (6), 185 (6), 77 (5), 34 (4), 60 (2) |
| 79132 | 391 (120..515) | 316 | 64 | 87 (146), 132 (33), 68 (31), 67 (30), 77 (25), 86 (20), 75 (12), 44 (11), 60 (4), 34 (4) |
| 79128 | 402 (124..527) | 329 | 62 | 44 (136), 77 (49), 67 (37), 87 (29), 75 (23), 34 (21), 86 (12), 68 (12), 33 (6), 60 (3), 55 (1) |
| 79134 | 407 (127..533) | 310 | 69 | 44 (116), 34 (79), 77 (70), 86 (17), 87 (10), 55 (6), 33 (6), 60 (3), 185 (2), 75 (1) |
| 79135 | 409 (129..542) | 324 | 68 | 34 (80), 162 (68), 185 (51), 44 (46), 55 (33), 86 (18), 77 (13), 33 (6), 60 (5), 87 (4) |
| 79139 | 406 (132..537) | 317 | 65 | 33 (87), 87 (67), 86 (43), 34 (43), 77 (40), 162 (26), 185 (6), 55 (4), 60 (1) |
| 79136 | 393 (136..538) | 312 | 59 | 33 (133), 162 (72), 60 (42), 86 (26), 77 (25), 55 (8), 34 (4), 185 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 100/329/1003; tracks with internal gaps: 19; total internal gaps: 36; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1007 | 1003 | 807 | 799 | 8 | 8 | 1 | 0 | 78911 |
| 27 | 78..467 | 390 | 327 | 325 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 32 | 85..461 | 377 | 319 | 317 | 2 | 1 | 2 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 33 | 86..538 | 453 | 381 | 378 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135, 79136, 79139 |
| 34 | 86..494 | 409 | 344 | 343 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 90..434 | 345 | 305 | 302 | 3 | 3 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 42 | 94..450 | 357 | 308 | 307 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 44 | 96..533 | 438 | 371 | 371 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 45 | 96..318 | 223 | 198 | 197 | 1 | 0 | 0 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110 |
| 48 | 100..477 | 378 | 312 | 312 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 108..293 | 186 | 162 | 159 | 3 | 1 | 1 | 2 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 60 | 110..212 | 103 | 68 | 66 | 2 | 0 | 0 | 2 | 79103, 79108, 79110, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 111..210 | 100 | 68 | 66 | 2 | 0 | 0 | 2 | 78899, 79097, 79098, 79102, 79103 |
| 62 | 111..439 | 329 | 285 | 282 | 3 | 3 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115 |
| 67 | 114..492 | 379 | 328 | 327 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 68 | 114..532 | 419 | 348 | 348 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 73 | 122..484 | 363 | 314 | 313 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 75 | 124..527 | 404 | 345 | 344 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 77 | 128..537 | 410 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 137..271 | 135 | 115 | 113 | 2 | 1 | 1 | 1 | 78896, 78969, 79045 |
| 84 | 137..445 | 309 | 261 | 260 | 1 | 1 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 139..384 | 246 | 192 | 188 | 4 | 2 | 1 | 2 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 87 | 139..515 | 377 | 315 | 315 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 90 | 144..392 | 249 | 221 | 220 | 1 | 0 | 0 | 1 | 78969, 78971, 79037, 79045 |
| 125 | 237..429 | 193 | 163 | 161 | 2 | 1 | 2 | 0 | 78896, 78899, 78971, 79097, 79098, 79102, 79103, 79105 |
| 132 | 243..481 | 239 | 205 | 205 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79116, 79132 |
| 154 | 312..443 | 132 | 103 | 101 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 155 | 312..455 | 144 | 126 | 126 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 162 | 345..542 | 198 | 168 | 166 | 2 | 2 | 1 | 0 | 79135, 79136, 79139 |
| 180 | 395..496 | 102 | 83 | 82 | 1 | 1 | 1 | 0 | 79110, 79111, 79116 |
| 182 | 400..531 | 132 | 105 | 105 | 0 | 0 | 0 | 0 | 79115, 79122 |
| 185 | 405..530 | 126 | 90 | 89 | 1 | 1 | 1 | 0 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8031; unmatched reference entries: 2111; unmatched candidate entries: 50
- identity switches: 991; fragmentation (coverage interruptions): 1590; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 27 -> 32 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 33 -> 34 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 34 -> 27 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 33 -> 34 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 34 -> 38 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 33 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 34 -> 42 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78897: 34 -> 42 at (2112.5, 3033), 1 frames after previous cover
- f96: ref 78899: 33 -> 44 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 27 -> 45 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 42 -> 38 at (2099, 3033.5), 2 frames after previous cover
- f98: ref 78899: 44 -> 34 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 33 -> 44 at (2129, 3028), 1 frames after previous cover
- f100: ref 79098: 33 -> 44 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 34 -> 42 at (2098.5, 3030.5), 3 frames after previous cover
- f101: ref 79098: 44 -> 34 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 33 -> 44 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 48 -> 33 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 79097: 44 -> 34 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 34 -> 42 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 48 -> 33 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 27 -> 45 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 38 -> 27 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 44 -> 34 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 33 -> 44 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 42 -> 48 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 45 -> 27 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 34 -> 33 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 79045: 27 -> 38 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79102: 34 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 44 -> 34 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 33 -> 44 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 33 -> 42 at (2090, 3028), 2 frames after previous cover
- f108: ref 79037: 38 -> 55 at (2026, 3034), 4 frames after previous cover
- f108: ref 79105: 44 -> 34 at (2113.5, 3025), 2 frames after previous cover
- f110: ref 78899: 48 -> 55 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 55 -> 38 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 38 -> 32 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 42 -> 48 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79102: 33 -> 42 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 34 -> 60 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 34 -> 33 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 48 -> 34 at (2118, 3025), 6 frames after previous cover
- f111: ref 78897: 42 -> 48 at (2021.5, 3032.5), 9 frames after previous cover
- f111: ref 79098: 42 -> 61 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79110: 44 -> 34 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 44 -> 62 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 42 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 60 -> 42 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 34 -> 60 at (2109, 3027), 2 frames after previous cover
- f113: ref 79103: 42 -> 61 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 33 -> 42 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 60 -> 33 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 34 -> 60 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 78896: 32 -> 27 at (1921, 3035), 5 frames after previous cover
- f114: ref 79097: 48 -> 67 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79098: 61 -> 68 at (2048, 3030), 3 frames after previous cover
- f114: ref 79110: 60 -> 33 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 62 -> 34 at (2126, 3027), 1 frames after previous cover
- f115: ref 78971: 27 -> 32 at (1959, 3034), 2 frames after previous cover
- ... 931 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 799 | 153 | 2 (799) |
| 78896 | 350 (76..429) | 277 | 53 | 83 (89), 84 (76), 125 (50), 27 (38), 32 (24) |
| 78969 | 352 (80..434) | 287 | 48 | 27 (77), 84 (63), 90 (61), 38 (35), 45 (24), 83 (23), 77 (4) |
| 78971 | 352 (84..439) | 269 | 54 | 62 (92), 27 (76), 84 (59), 90 (25), 45 (6), 38 (4), 34 (2), 32 (2), 77 (2), 125 (1) |
| 79045 | 355 (84..443) | 286 | 53 | 90 (114), 154 (44), 62 (42), 38 (20), 27 (19), 42 (14), 32 (13), 45 (6), 77 (4), 84 (4), 48 (3), 33 (1), +2 more |
| 79037 | 355 (86..445) | 276 | 53 | 45 (52), 38 (50), 62 (41), 84 (41), 90 (20), 32 (19), 27 (16), 48 (13), 154 (8), 42 (7), 77 (3), 33 (2), +2 more |
| 78897 | 345 (89..450) | 272 | 48 | 48 (49), 38 (46), 42 (38), 77 (38), 32 (34), 62 (17), 84 (17), 27 (14), 34 (5), 154 (5), 45 (4), 155 (3), +1 more |
| 78899 | 365 (91..455) | 298 | 51 | 48 (82), 155 (73), 32 (43), 42 (34), 125 (26), 38 (10), 154 (7), 55 (5), 45 (4), 27 (4), 33 (3), 61 (3), +3 more |
| 79097 | 366 (94..461) | 291 | 57 | 48 (53), 32 (41), 38 (38), 42 (37), 125 (33), 154 (28), 155 (26), 61 (16), 27 (7), 33 (4), 55 (3), 44 (2), +3 more |
| 79098 | 360 (97..467) | 281 | 66 | 27 (74), 61 (43), 42 (39), 73 (35), 62 (18), 38 (13), 125 (13), 48 (12), 155 (9), 32 (4), 77 (4), 33 (3), +7 more |
| 79102 | 371 (98..477) | 278 | 67 | 48 (70), 42 (52), 62 (49), 32 (30), 73 (14), 38 (10), 68 (8), 45 (8), 154 (7), 125 (6), 75 (5), 33 (4), +7 more |
| 79103 | 380 (99..481) | 291 | 67 | 132 (68), 73 (52), 55 (32), 125 (30), 48 (24), 38 (23), 42 (15), 62 (13), 68 (8), 32 (7), 45 (6), 61 (3), +6 more |
| 79105 | 379 (101..484) | 309 | 59 | 73 (110), 45 (58), 32 (32), 42 (28), 55 (17), 68 (14), 155 (10), 38 (9), 33 (6), 132 (6), 48 (5), 75 (5), +5 more |
| 79108 | 385 (104..492) | 313 | 58 | 67 (93), 38 (41), 73 (41), 32 (28), 132 (26), 68 (23), 45 (22), 33 (17), 55 (9), 42 (4), 77 (3), 75 (2), +4 more |
| 79110 | 388 (106..497) | 305 | 62 | 180 (75), 132 (48), 75 (40), 32 (35), 68 (21), 67 (20), 42 (19), 33 (16), 55 (10), 45 (7), 73 (3), 38 (3), +4 more |
| 79111 | 386 (109..500) | 321 | 53 | 68 (137), 75 (48), 33 (42), 67 (19), 73 (17), 132 (15), 42 (9), 55 (8), 77 (7), 34 (5), 32 (5), 62 (4), +2 more |
| 79115 | 421 (111..531) | 339 | 62 | 182 (90), 75 (82), 68 (41), 33 (27), 77 (27), 67 (21), 73 (19), 44 (10), 42 (7), 55 (4), 87 (4), 34 (3), +2 more |
| 79116 | 411 (114..530) | 320 | 67 | 34 (77), 67 (44), 75 (36), 87 (27), 73 (22), 77 (19), 185 (19), 44 (17), 86 (13), 33 (11), 68 (10), 132 (9), +4 more |
| 79122 | 404 (118..532) | 311 | 72 | 75 (87), 67 (56), 68 (41), 86 (39), 87 (28), 44 (22), 182 (15), 55 (6), 185 (6), 77 (5), 34 (4), 60 (2) |
| 79132 | 391 (120..515) | 316 | 64 | 87 (146), 132 (33), 68 (31), 67 (30), 77 (25), 86 (20), 75 (12), 44 (11), 60 (4), 34 (4) |
| 79128 | 402 (124..527) | 329 | 62 | 44 (136), 77 (49), 67 (37), 87 (29), 75 (23), 34 (21), 86 (12), 68 (12), 33 (6), 60 (3), 55 (1) |
| 79134 | 407 (127..533) | 310 | 69 | 44 (116), 34 (79), 77 (70), 86 (17), 87 (10), 55 (6), 33 (6), 60 (3), 185 (2), 75 (1) |
| 79135 | 409 (129..542) | 324 | 68 | 34 (80), 162 (68), 185 (51), 44 (46), 55 (33), 86 (18), 77 (13), 33 (6), 60 (5), 87 (4) |
| 79139 | 406 (132..537) | 317 | 65 | 33 (87), 87 (67), 86 (43), 34 (43), 77 (40), 162 (26), 185 (6), 55 (4), 60 (1) |
| 79136 | 393 (136..538) | 312 | 59 | 33 (133), 162 (72), 60 (42), 86 (26), 77 (25), 55 (8), 34 (4), 185 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 100/329/1003; tracks with internal gaps: 19; total internal gaps: 36; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1007 | 1003 | 807 | 799 | 8 | 8 | 1 | 0 | 78911 |
| 27 | 78..467 | 390 | 327 | 325 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 32 | 85..461 | 377 | 319 | 317 | 2 | 1 | 2 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 33 | 86..538 | 453 | 381 | 378 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135, 79136, 79139 |
| 34 | 86..494 | 409 | 344 | 343 | 1 | 0 | 0 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 90..434 | 345 | 305 | 302 | 3 | 3 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 42 | 94..450 | 357 | 308 | 307 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 44 | 96..533 | 438 | 371 | 371 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 45 | 96..318 | 223 | 198 | 197 | 1 | 0 | 0 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110 |
| 48 | 100..477 | 378 | 312 | 312 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 108..293 | 186 | 162 | 159 | 3 | 1 | 1 | 2 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 60 | 110..212 | 103 | 68 | 66 | 2 | 0 | 0 | 2 | 79103, 79108, 79110, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 111..210 | 100 | 68 | 66 | 2 | 0 | 0 | 2 | 78899, 79097, 79098, 79102, 79103 |
| 62 | 111..439 | 329 | 285 | 282 | 3 | 3 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115 |
| 67 | 114..492 | 379 | 328 | 327 | 1 | 1 | 1 | 0 | 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 68 | 114..532 | 419 | 348 | 348 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 73 | 122..484 | 363 | 314 | 313 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 75 | 124..527 | 404 | 345 | 344 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 77 | 128..537 | 410 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 78969, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 137..271 | 135 | 115 | 113 | 2 | 1 | 1 | 1 | 78896, 78969, 79045 |
| 84 | 137..445 | 309 | 261 | 260 | 1 | 1 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 139..384 | 246 | 192 | 188 | 4 | 2 | 1 | 2 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 87 | 139..515 | 377 | 315 | 315 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 90 | 144..392 | 249 | 221 | 220 | 1 | 0 | 0 | 1 | 78969, 78971, 79037, 79045 |
| 125 | 237..429 | 193 | 163 | 161 | 2 | 1 | 2 | 0 | 78896, 78899, 78971, 79097, 79098, 79102, 79103, 79105 |
| 132 | 243..481 | 239 | 205 | 205 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79116, 79132 |
| 154 | 312..443 | 132 | 103 | 101 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 155 | 312..455 | 144 | 126 | 126 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 162 | 345..542 | 198 | 168 | 166 | 2 | 2 | 1 | 0 | 79135, 79136, 79139 |
| 180 | 395..496 | 102 | 83 | 82 | 1 | 1 | 1 | 0 | 79110, 79111, 79116 |
| 182 | 400..531 | 132 | 105 | 105 | 0 | 0 | 0 | 0 | 79115, 79122 |
| 185 | 405..530 | 126 | 90 | 89 | 1 | 1 | 1 | 0 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9159; unmatched reference entries: 983; unmatched candidate entries: 1389
- identity switches: 988; fragmentation (coverage interruptions): 712; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 27 -> 32 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 33 -> 34 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 34 -> 27 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 33 -> 34 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 34 -> 38 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 33 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 34 -> 42 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78899: 33 -> 44 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 27 -> 45 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 42 -> 38 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 34 -> 42 at (2107, 3033), 1 frames after previous cover
- f98: ref 78899: 44 -> 34 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 33 -> 44 at (2129, 3028), 1 frames after previous cover
- f100: ref 78899: 34 -> 42 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 79097: 44 -> 34 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 33 -> 44 at (2130, 3027), 1 frames after previous cover
- f101: ref 79098: 44 -> 34 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 33 -> 44 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 48 -> 33 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 34 -> 42 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 48 -> 33 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 27 -> 45 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 38 -> 27 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 44 -> 34 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 33 -> 44 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 42 -> 48 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 45 -> 27 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 34 -> 33 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 79045: 27 -> 38 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79102: 34 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 44 -> 34 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 33 -> 44 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 79098: 33 -> 42 at (2090, 3028), 2 frames after previous cover
- f108: ref 79037: 38 -> 55 at (2026, 3034), 4 frames after previous cover
- f108: ref 79105: 44 -> 34 at (2113.5, 3025), 1 frames after previous cover
- f110: ref 78899: 48 -> 55 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 55 -> 38 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 38 -> 32 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 42 -> 48 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79102: 33 -> 42 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 34 -> 60 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 34 -> 33 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 48 -> 34 at (2118, 3025), 6 frames after previous cover
- f111: ref 78897: 42 -> 48 at (2021.5, 3032.5), 9 frames after previous cover
- f111: ref 79098: 42 -> 61 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79110: 44 -> 34 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 44 -> 62 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 42 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 60 -> 42 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 34 -> 60 at (2109, 3027), 2 frames after previous cover
- f113: ref 79103: 42 -> 61 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 33 -> 42 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 60 -> 33 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 32 -> 27 at (1921, 3035), 5 frames after previous cover
- f114: ref 79097: 48 -> 67 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79098: 61 -> 68 at (2048, 3030), 3 frames after previous cover
- f114: ref 79110: 34 -> 33 at (2111, 3026.5), 1 frames after previous cover
- f115: ref 78971: 27 -> 32 at (1959, 3034), 2 frames after previous cover
- f115: ref 79097: 67 -> 55 at (2028.5, 3030), 1 frames after previous cover
- f115: ref 79098: 68 -> 67 at (2042.5, 3029), 1 frames after previous cover
- ... 928 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 972 | 20 | 2 (972) |
| 78896 | 350 (76..429) | 318 | 20 | 83 (102), 84 (90), 125 (60), 27 (41), 32 (25) |
| 78969 | 352 (80..434) | 317 | 26 | 27 (88), 84 (69), 90 (65), 38 (39), 45 (27), 83 (25), 77 (4) |
| 78971 | 352 (84..439) | 300 | 32 | 62 (107), 27 (83), 84 (66), 90 (26), 45 (6), 38 (5), 34 (2), 32 (2), 77 (2), 125 (1) |
| 79045 | 355 (84..443) | 319 | 29 | 90 (128), 154 (50), 62 (43), 27 (23), 38 (21), 32 (17), 42 (17), 45 (6), 77 (4), 84 (4), 48 (3), 33 (1), +2 more |
| 79037 | 355 (86..445) | 314 | 26 | 45 (59), 38 (56), 62 (47), 84 (46), 32 (25), 90 (22), 48 (15), 27 (15), 42 (10), 154 (10), 77 (3), 33 (2), +2 more |
| 78897 | 345 (89..450) | 302 | 25 | 48 (54), 38 (51), 77 (46), 42 (42), 32 (37), 62 (19), 84 (19), 27 (13), 34 (6), 154 (6), 45 (4), 155 (3), +1 more |
| 78899 | 365 (91..455) | 333 | 21 | 48 (89), 155 (81), 32 (51), 42 (39), 125 (32), 38 (10), 154 (7), 55 (5), 45 (4), 27 (4), 33 (3), 61 (3), +3 more |
| 79097 | 366 (94..461) | 325 | 31 | 48 (59), 32 (46), 38 (44), 42 (41), 125 (35), 154 (32), 155 (31), 61 (17), 27 (7), 33 (4), 55 (3), 44 (2), +3 more |
| 79098 | 360 (97..467) | 322 | 34 | 27 (87), 61 (54), 42 (43), 73 (39), 62 (18), 48 (15), 38 (14), 125 (13), 155 (11), 32 (6), 77 (4), 33 (3), +7 more |
| 79102 | 371 (98..477) | 317 | 38 | 48 (83), 42 (58), 62 (55), 32 (37), 73 (15), 38 (10), 45 (9), 154 (9), 68 (8), 125 (6), 33 (5), 75 (5), +7 more |
| 79103 | 380 (99..481) | 330 | 36 | 132 (84), 73 (52), 55 (37), 125 (37), 48 (29), 38 (24), 42 (15), 62 (14), 68 (10), 32 (8), 45 (6), 61 (4), +6 more |
| 79105 | 379 (101..484) | 345 | 31 | 73 (130), 45 (61), 32 (34), 42 (33), 55 (18), 68 (15), 155 (11), 38 (9), 33 (7), 132 (6), 48 (5), 75 (5), +5 more |
| 79108 | 385 (104..492) | 350 | 28 | 67 (113), 73 (48), 38 (44), 132 (29), 32 (28), 68 (25), 45 (24), 33 (17), 55 (9), 42 (4), 77 (3), 75 (2), +4 more |
| 79110 | 388 (106..497) | 341 | 33 | 180 (91), 132 (51), 75 (47), 32 (38), 68 (24), 67 (20), 42 (20), 33 (17), 55 (10), 45 (9), 34 (3), 73 (3), +3 more |
| 79111 | 386 (109..500) | 350 | 30 | 68 (150), 75 (57), 33 (45), 73 (20), 67 (19), 132 (16), 42 (9), 55 (8), 77 (7), 62 (5), 32 (5), 34 (4), +2 more |
| 79115 | 421 (111..531) | 380 | 29 | 182 (117), 75 (91), 68 (40), 33 (30), 77 (27), 67 (23), 73 (19), 44 (10), 42 (7), 87 (5), 55 (4), 34 (3), +2 more |
| 79116 | 411 (114..530) | 364 | 35 | 34 (94), 67 (50), 75 (40), 87 (27), 73 (26), 77 (21), 44 (20), 185 (20), 86 (14), 68 (11), 33 (11), 55 (10), +4 more |
| 79122 | 404 (118..532) | 359 | 36 | 75 (109), 67 (63), 68 (54), 86 (41), 87 (35), 44 (24), 182 (9), 185 (7), 55 (6), 77 (5), 34 (4), 60 (2) |
| 79132 | 391 (120..515) | 363 | 26 | 87 (170), 68 (39), 132 (38), 67 (33), 77 (28), 86 (21), 44 (13), 75 (13), 60 (4), 34 (4) |
| 79128 | 402 (124..527) | 374 | 24 | 44 (159), 77 (54), 67 (40), 87 (35), 75 (24), 34 (23), 86 (14), 68 (13), 33 (7), 60 (3), 55 (2) |
| 79134 | 407 (127..533) | 357 | 31 | 44 (132), 34 (86), 77 (86), 86 (21), 87 (10), 33 (9), 55 (7), 60 (3), 185 (3) |
| 79135 | 409 (129..542) | 377 | 28 | 34 (94), 162 (77), 185 (61), 44 (54), 55 (38), 86 (22), 77 (15), 33 (7), 60 (5), 87 (4) |
| 79139 | 406 (132..537) | 365 | 26 | 33 (110), 87 (80), 86 (54), 34 (46), 77 (35), 162 (25), 185 (10), 55 (3), 60 (1), 75 (1) |
| 79136 | 393 (136..538) | 365 | 17 | 33 (145), 162 (89), 60 (50), 77 (35), 86 (31), 55 (10), 34 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 129/358/1004; tracks with internal gaps: 31; total internal gaps: 294; longest internal gap: 11; tracks ending in coasting: 31 (trailing rows total 964)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 972 | 32 | 20 | 4 | 0 | 78911 |
| 27 | 78..496 | 419 | 419 | 361 | 58 | 19 | 3 | 31 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 32 | 85..490 | 406 | 406 | 359 | 47 | 9 | 11 | 23 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 33 | 86..567 | 482 | 482 | 427 | 55 | 14 | 10 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135, 79136, 79139 |
| 34 | 86..523 | 438 | 438 | 390 | 48 | 14 | 3 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 90..463 | 374 | 374 | 330 | 44 | 14 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 42 | 94..479 | 386 | 386 | 342 | 44 | 13 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 44 | 96..562 | 467 | 467 | 427 | 40 | 11 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 45 | 96..347 | 252 | 252 | 215 | 37 | 6 | 2 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110 |
| 48 | 100..506 | 407 | 407 | 353 | 54 | 18 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 108..322 | 215 | 215 | 176 | 39 | 4 | 2 | 34 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 60 | 110..241 | 132 | 132 | 73 | 59 | 4 | 3 | 52 | 79103, 79108, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 111..239 | 129 | 129 | 80 | 49 | 0 | 0 | 49 | 78899, 79097, 79098, 79102, 79103 |
| 62 | 111..468 | 358 | 358 | 315 | 43 | 11 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115 |
| 67 | 114..521 | 408 | 408 | 368 | 40 | 8 | 2 | 29 | 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 68 | 114..561 | 448 | 448 | 391 | 57 | 18 | 8 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 73 | 122..513 | 392 | 392 | 352 | 40 | 10 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 75 | 124..556 | 433 | 433 | 397 | 36 | 8 | 3 | 26 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 77 | 128..566 | 439 | 439 | 385 | 54 | 16 | 3 | 29 | 78897, 78969, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 137..300 | 164 | 164 | 128 | 36 | 4 | 2 | 30 | 78896, 78969, 79045 |
| 84 | 137..474 | 338 | 338 | 294 | 44 | 10 | 3 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 139..413 | 275 | 275 | 218 | 57 | 8 | 2 | 47 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 87 | 139..544 | 406 | 406 | 366 | 40 | 10 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 90 | 144..421 | 278 | 278 | 241 | 37 | 7 | 1 | 30 | 78969, 78971, 79037, 79045 |
| 125 | 237..458 | 222 | 222 | 186 | 36 | 4 | 2 | 29 | 78896, 78899, 78971, 79097, 79098, 79102, 79103, 79105 |
| 132 | 243..510 | 268 | 268 | 233 | 35 | 5 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79116, 79132 |
| 154 | 312..472 | 161 | 161 | 117 | 44 | 8 | 4 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 155 | 312..484 | 173 | 173 | 142 | 31 | 2 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 162 | 345..571 | 227 | 227 | 191 | 36 | 5 | 2 | 29 | 79135, 79136, 79139 |
| 180 | 395..525 | 131 | 131 | 100 | 31 | 3 | 1 | 28 | 79110, 79111, 79116 |
| 182 | 400..560 | 161 | 161 | 126 | 35 | 6 | 1 | 29 | 79115, 79122 |
| 185 | 405..559 | 155 | 155 | 104 | 51 | 5 | 9 | 32 | 79115, 79116, 79122, 79134, 79135, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 9159; unmatched reference entries: 983; unmatched candidate entries: 1389
- identity switches: 988; fragmentation (coverage interruptions): 712; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78896: 27 -> 32 at (2102, 3033), 6 frames after previous cover
- f88: ref 79045: 33 -> 34 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 78971: 34 -> 27 at (2121, 3034), 2 frames after previous cover
- f89: ref 79037: 33 -> 34 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 79045: 34 -> 38 at (2124, 3033.5), 2 frames after previous cover
- f91: ref 78897: 33 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f94: ref 79037: 34 -> 42 at (2112.5, 3034), 4 frames after previous cover
- f96: ref 78899: 33 -> 44 at (2128, 3029), 3 frames after previous cover
- f96: ref 78969: 27 -> 45 at (2059.5, 3036), 3 frames after previous cover
- f96: ref 79037: 42 -> 38 at (2099, 3033.5), 1 frames after previous cover
- f97: ref 78897: 34 -> 42 at (2107, 3033), 1 frames after previous cover
- f98: ref 78899: 44 -> 34 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 33 -> 44 at (2129, 3028), 1 frames after previous cover
- f100: ref 78899: 34 -> 42 at (2104, 3030.5), 1 frames after previous cover
- f100: ref 79097: 44 -> 34 at (2117.5, 3029.5), 1 frames after previous cover
- f100: ref 79098: 33 -> 44 at (2130, 3027), 1 frames after previous cover
- f101: ref 79098: 44 -> 34 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 33 -> 44 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 48 -> 33 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79097: 34 -> 42 at (2100, 3028.5), 1 frames after previous cover
- f103: ref 79105: 48 -> 33 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78971: 27 -> 45 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 38 -> 27 at (2036.5, 3033.5), 3 frames after previous cover
- f104: ref 79102: 44 -> 34 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 33 -> 44 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78899: 42 -> 48 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 45 -> 27 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 34 -> 33 at (2100.5, 3028.5), 2 frames after previous cover
- f106: ref 79045: 27 -> 38 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79102: 34 -> 33 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 44 -> 34 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 33 -> 44 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 79098: 33 -> 42 at (2090, 3028), 2 frames after previous cover
- f108: ref 79037: 38 -> 55 at (2026, 3034), 4 frames after previous cover
- f108: ref 79105: 44 -> 34 at (2113.5, 3025), 1 frames after previous cover
- f110: ref 78899: 48 -> 55 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 79037: 55 -> 38 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 38 -> 32 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 42 -> 48 at (2058.5, 3029.5), 4 frames after previous cover
- f110: ref 79102: 33 -> 42 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 34 -> 60 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 34 -> 33 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 48 -> 34 at (2118, 3025), 6 frames after previous cover
- f111: ref 78897: 42 -> 48 at (2021.5, 3032.5), 9 frames after previous cover
- f111: ref 79098: 42 -> 61 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79110: 44 -> 34 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 44 -> 62 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79102: 42 -> 61 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 60 -> 42 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 34 -> 60 at (2109, 3027), 2 frames after previous cover
- f113: ref 79103: 42 -> 61 at (2074, 3024.5), 1 frames after previous cover
- f113: ref 79105: 33 -> 42 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 60 -> 33 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 32 -> 27 at (1921, 3035), 5 frames after previous cover
- f114: ref 79097: 48 -> 67 at (2034.5, 3030), 4 frames after previous cover
- f114: ref 79098: 61 -> 68 at (2048, 3030), 3 frames after previous cover
- f114: ref 79110: 34 -> 33 at (2111, 3026.5), 1 frames after previous cover
- f115: ref 78971: 27 -> 32 at (1959, 3034), 2 frames after previous cover
- f115: ref 79097: 67 -> 55 at (2028.5, 3030), 1 frames after previous cover
- f115: ref 79098: 68 -> 67 at (2042.5, 3029), 1 frames after previous cover
- ... 928 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 972 | 20 | 2 (972) |
| 78896 | 350 (76..429) | 318 | 20 | 83 (102), 84 (90), 125 (60), 27 (41), 32 (25) |
| 78969 | 352 (80..434) | 317 | 26 | 27 (88), 84 (69), 90 (65), 38 (39), 45 (27), 83 (25), 77 (4) |
| 78971 | 352 (84..439) | 300 | 32 | 62 (107), 27 (83), 84 (66), 90 (26), 45 (6), 38 (5), 34 (2), 32 (2), 77 (2), 125 (1) |
| 79045 | 355 (84..443) | 319 | 29 | 90 (128), 154 (50), 62 (43), 27 (23), 38 (21), 32 (17), 42 (17), 45 (6), 77 (4), 84 (4), 48 (3), 33 (1), +2 more |
| 79037 | 355 (86..445) | 314 | 26 | 45 (59), 38 (56), 62 (47), 84 (46), 32 (25), 90 (22), 48 (15), 27 (15), 42 (10), 154 (10), 77 (3), 33 (2), +2 more |
| 78897 | 345 (89..450) | 302 | 25 | 48 (54), 38 (51), 77 (46), 42 (42), 32 (37), 62 (19), 84 (19), 27 (13), 34 (6), 154 (6), 45 (4), 155 (3), +1 more |
| 78899 | 365 (91..455) | 333 | 21 | 48 (89), 155 (81), 32 (51), 42 (39), 125 (32), 38 (10), 154 (7), 55 (5), 45 (4), 27 (4), 33 (3), 61 (3), +3 more |
| 79097 | 366 (94..461) | 325 | 31 | 48 (59), 32 (46), 38 (44), 42 (41), 125 (35), 154 (32), 155 (31), 61 (17), 27 (7), 33 (4), 55 (3), 44 (2), +3 more |
| 79098 | 360 (97..467) | 322 | 34 | 27 (87), 61 (54), 42 (43), 73 (39), 62 (18), 48 (15), 38 (14), 125 (13), 155 (11), 32 (6), 77 (4), 33 (3), +7 more |
| 79102 | 371 (98..477) | 317 | 38 | 48 (83), 42 (58), 62 (55), 32 (37), 73 (15), 38 (10), 45 (9), 154 (9), 68 (8), 125 (6), 33 (5), 75 (5), +7 more |
| 79103 | 380 (99..481) | 330 | 36 | 132 (84), 73 (52), 55 (37), 125 (37), 48 (29), 38 (24), 42 (15), 62 (14), 68 (10), 32 (8), 45 (6), 61 (4), +6 more |
| 79105 | 379 (101..484) | 345 | 31 | 73 (130), 45 (61), 32 (34), 42 (33), 55 (18), 68 (15), 155 (11), 38 (9), 33 (7), 132 (6), 48 (5), 75 (5), +5 more |
| 79108 | 385 (104..492) | 350 | 28 | 67 (113), 73 (48), 38 (44), 132 (29), 32 (28), 68 (25), 45 (24), 33 (17), 55 (9), 42 (4), 77 (3), 75 (2), +4 more |
| 79110 | 388 (106..497) | 341 | 33 | 180 (91), 132 (51), 75 (47), 32 (38), 68 (24), 67 (20), 42 (20), 33 (17), 55 (10), 45 (9), 34 (3), 73 (3), +3 more |
| 79111 | 386 (109..500) | 350 | 30 | 68 (150), 75 (57), 33 (45), 73 (20), 67 (19), 132 (16), 42 (9), 55 (8), 77 (7), 62 (5), 32 (5), 34 (4), +2 more |
| 79115 | 421 (111..531) | 380 | 29 | 182 (117), 75 (91), 68 (40), 33 (30), 77 (27), 67 (23), 73 (19), 44 (10), 42 (7), 87 (5), 55 (4), 34 (3), +2 more |
| 79116 | 411 (114..530) | 364 | 35 | 34 (94), 67 (50), 75 (40), 87 (27), 73 (26), 77 (21), 44 (20), 185 (20), 86 (14), 68 (11), 33 (11), 55 (10), +4 more |
| 79122 | 404 (118..532) | 359 | 36 | 75 (109), 67 (63), 68 (54), 86 (41), 87 (35), 44 (24), 182 (9), 185 (7), 55 (6), 77 (5), 34 (4), 60 (2) |
| 79132 | 391 (120..515) | 363 | 26 | 87 (170), 68 (39), 132 (38), 67 (33), 77 (28), 86 (21), 44 (13), 75 (13), 60 (4), 34 (4) |
| 79128 | 402 (124..527) | 374 | 24 | 44 (159), 77 (54), 67 (40), 87 (35), 75 (24), 34 (23), 86 (14), 68 (13), 33 (7), 60 (3), 55 (2) |
| 79134 | 407 (127..533) | 357 | 31 | 44 (132), 34 (86), 77 (86), 86 (21), 87 (10), 33 (9), 55 (7), 60 (3), 185 (3) |
| 79135 | 409 (129..542) | 377 | 28 | 34 (94), 162 (77), 185 (61), 44 (54), 55 (38), 86 (22), 77 (15), 33 (7), 60 (5), 87 (4) |
| 79139 | 406 (132..537) | 365 | 26 | 33 (110), 87 (80), 86 (54), 34 (46), 77 (35), 162 (25), 185 (10), 55 (3), 60 (1), 75 (1) |
| 79136 | 393 (136..538) | 365 | 17 | 33 (145), 162 (89), 60 (50), 77 (35), 86 (31), 55 (10), 34 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 129/358/1004; tracks with internal gaps: 31; total internal gaps: 294; longest internal gap: 11; tracks ending in coasting: 31 (trailing rows total 964)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 972 | 32 | 20 | 4 | 0 | 78911 |
| 27 | 78..496 | 419 | 419 | 361 | 58 | 19 | 3 | 31 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 32 | 85..490 | 406 | 406 | 359 | 47 | 9 | 11 | 23 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 33 | 86..567 | 482 | 482 | 427 | 55 | 14 | 10 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79134, 79135, 79136, 79139 |
| 34 | 86..523 | 438 | 438 | 390 | 48 | 14 | 3 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 90..463 | 374 | 374 | 330 | 44 | 14 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 42 | 94..479 | 386 | 386 | 342 | 44 | 13 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 44 | 96..562 | 467 | 467 | 427 | 40 | 11 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 45 | 96..347 | 252 | 252 | 215 | 37 | 6 | 2 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79103, 79105, 79108, 79110 |
| 48 | 100..506 | 407 | 407 | 353 | 54 | 18 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 55 | 108..322 | 215 | 215 | 176 | 39 | 4 | 2 | 34 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79135, 79136, 79139 |
| 60 | 110..241 | 132 | 132 | 73 | 59 | 4 | 3 | 52 | 79103, 79108, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 111..239 | 129 | 129 | 80 | 49 | 0 | 0 | 49 | 78899, 79097, 79098, 79102, 79103 |
| 62 | 111..468 | 358 | 358 | 315 | 43 | 11 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115 |
| 67 | 114..521 | 408 | 408 | 368 | 40 | 8 | 2 | 29 | 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 68 | 114..561 | 448 | 448 | 391 | 57 | 18 | 8 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 73 | 122..513 | 392 | 392 | 352 | 40 | 10 | 2 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 75 | 124..556 | 433 | 433 | 397 | 36 | 8 | 3 | 26 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 77 | 128..566 | 439 | 439 | 385 | 54 | 16 | 3 | 29 | 78897, 78969, 78971, 79037, 79045, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 83 | 137..300 | 164 | 164 | 128 | 36 | 4 | 2 | 30 | 78896, 78969, 79045 |
| 84 | 137..474 | 338 | 338 | 294 | 44 | 10 | 3 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 86 | 139..413 | 275 | 275 | 218 | 57 | 8 | 2 | 47 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 87 | 139..544 | 406 | 406 | 366 | 40 | 10 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 90 | 144..421 | 278 | 278 | 241 | 37 | 7 | 1 | 30 | 78969, 78971, 79037, 79045 |
| 125 | 237..458 | 222 | 222 | 186 | 36 | 4 | 2 | 29 | 78896, 78899, 78971, 79097, 79098, 79102, 79103, 79105 |
| 132 | 243..510 | 268 | 268 | 233 | 35 | 5 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79116, 79132 |
| 154 | 312..472 | 161 | 161 | 117 | 44 | 8 | 4 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 155 | 312..484 | 173 | 173 | 142 | 31 | 2 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105 |
| 162 | 345..571 | 227 | 227 | 191 | 36 | 5 | 2 | 29 | 79135, 79136, 79139 |
| 180 | 395..525 | 131 | 131 | 100 | 31 | 3 | 1 | 28 | 79110, 79111, 79116 |
| 182 | 400..560 | 161 | 161 | 126 | 35 | 6 | 1 | 29 | 79115, 79122 |
| 185 | 405..559 | 155 | 155 | 104 | 51 | 5 | 9 | 32 | 79115, 79116, 79122, 79134, 79135, 79139 |
