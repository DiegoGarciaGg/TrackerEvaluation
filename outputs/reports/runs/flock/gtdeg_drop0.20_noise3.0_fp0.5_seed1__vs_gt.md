# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=8cdc138dbc49
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise3.0_fp0.5_seed1/tracks.csv sha256=092b4e0eda3f6ccc
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise3.0_fp0.5_seed1.csv sha256=8cdc138dbc4946e8
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise3.0_fp0.5_seed1
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
| observations | none | 4 | 10142 | 8055 | 0.167 | 0.357 | 0.078 | 2.18 | 0.166 | 0.038 | 2.41 | 953 | 2463.0 | 0.178 | 0.200 | 0.159 | 0.463 | 0.583 | 4699 | 5443 | 3356 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 8055 | 0.229 | 0.495 | 0.106 | 2.73 | 0.281 | 0.453 | 3.20 | 1196 | 2144.0 | 0.265 | 0.300 | 0.238 | 0.683 | 0.860 | 6924 | 3218 | 1131 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 8055 | 0.262 | 0.566 | 0.122 | 3.05 | 0.329 | 0.605 | 3.59 | 1243 | 1764.0 | 0.296 | 0.334 | 0.266 | 0.761 | 0.958 | 7718 | 2424 | 337 | 1 | 24 | 0 |
| observations | none | 12 | 10142 | 8055 | 0.295 | 0.624 | 0.139 | 3.51 | 0.348 | 0.651 | 3.94 | 1146 | 1626.0 | 0.321 | 0.363 | 0.288 | 0.779 | 0.981 | 7902 | 2240 | 153 | 3 | 22 | 0 |
| observations | ignore | 4 | 10142 | 8055 | 0.167 | 0.357 | 0.078 | 2.18 | 0.166 | 0.038 | 2.41 | 953 | 2463.0 | 0.178 | 0.200 | 0.159 | 0.463 | 0.583 | 4699 | 5443 | 3356 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 8055 | 0.229 | 0.495 | 0.106 | 2.73 | 0.281 | 0.453 | 3.20 | 1196 | 2144.0 | 0.265 | 0.300 | 0.238 | 0.683 | 0.860 | 6924 | 3218 | 1131 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 8055 | 0.262 | 0.566 | 0.122 | 3.05 | 0.329 | 0.605 | 3.59 | 1243 | 1764.0 | 0.296 | 0.334 | 0.266 | 0.761 | 0.958 | 7718 | 2424 | 337 | 1 | 24 | 0 |
| observations | ignore | 12 | 10142 | 8055 | 0.295 | 0.624 | 0.139 | 3.51 | 0.348 | 0.651 | 3.94 | 1146 | 1626.0 | 0.321 | 0.363 | 0.288 | 0.779 | 0.981 | 7902 | 2240 | 153 | 3 | 22 | 0 |
| updates | none | 4 | 10142 | 10748 | 0.164 | 0.324 | 0.083 | 2.21 | 0.159 | -0.177 | 2.42 | 998 | 2477.0 | 0.169 | 0.164 | 0.174 | 0.491 | 0.463 | 4975 | 5167 | 5773 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10748 | 0.235 | 0.466 | 0.118 | 2.84 | 0.276 | 0.294 | 3.25 | 1244 | 1890.0 | 0.259 | 0.251 | 0.266 | 0.738 | 0.696 | 7485 | 2657 | 3263 | 1 | 24 | 0 |
| updates | none | 8 | 10142 | 10748 | 0.276 | 0.546 | 0.140 | 3.24 | 0.340 | 0.507 | 3.74 | 1257 | 1215.0 | 0.298 | 0.290 | 0.307 | 0.845 | 0.798 | 8573 | 1569 | 2175 | 22 | 3 | 0 |
| updates | none | 12 | 10142 | 10748 | 0.319 | 0.621 | 0.164 | 3.81 | 0.383 | 0.627 | 4.34 | 1118 | 776.0 | 0.335 | 0.326 | 0.345 | 0.898 | 0.848 | 9110 | 1032 | 1638 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10748 | 0.164 | 0.324 | 0.083 | 2.21 | 0.159 | -0.177 | 2.42 | 998 | 2477.0 | 0.169 | 0.164 | 0.174 | 0.491 | 0.463 | 4975 | 5167 | 5773 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10748 | 0.235 | 0.466 | 0.118 | 2.84 | 0.276 | 0.294 | 3.25 | 1244 | 1890.0 | 0.259 | 0.251 | 0.266 | 0.738 | 0.696 | 7485 | 2657 | 3263 | 1 | 24 | 0 |
| updates | ignore | 8 | 10142 | 10748 | 0.276 | 0.546 | 0.140 | 3.24 | 0.340 | 0.507 | 3.74 | 1257 | 1215.0 | 0.298 | 0.290 | 0.307 | 0.845 | 0.798 | 8573 | 1569 | 2175 | 22 | 3 | 0 |
| updates | ignore | 12 | 10142 | 10748 | 0.319 | 0.621 | 0.164 | 3.81 | 0.383 | 0.627 | 4.34 | 1118 | 776.0 | 0.335 | 0.326 | 0.345 | 0.898 | 0.848 | 9110 | 1032 | 1638 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7718; unmatched reference entries: 2424; unmatched candidate entries: 337
- identity switches: 1243; fragmentation (coverage interruptions): 1780; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 41 -> 42 at (2141, 3034.5), 2 frames after previous cover
- f89: ref 79045: 42 -> 43 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 41 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 43 -> 46 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 37 -> 45 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 43 -> 37 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 43 -> 47 at (2118, 3034.5), 2 frames after previous cover
- f94: ref 78896: 46 -> 43 at (2047.5, 3031), 1 frames after previous cover
- f94: ref 78897: 42 -> 47 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 41 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 45 -> 46 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 37 -> 45 at (2090.5, 3032.5), 3 frames after previous cover
- f96: ref 78899: 42 -> 41 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f97: ref 78897: 47 -> 49 at (2107, 3033), 2 frames after previous cover
- f97: ref 78899: 41 -> 47 at (2123, 3030), 1 frames after previous cover
- f97: ref 79037: 49 -> 37 at (2093, 3032.5), 1 frames after previous cover
- f97: ref 79045: 37 -> 45 at (2081.5, 3032), 1 frames after previous cover
- f99: ref 78897: 49 -> 37 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 37 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 45 -> 46 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 37 -> 49 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 37 at (2076, 3033.5), 1 frames after previous cover
- f101: ref 78899: 47 -> 49 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 37 -> 45 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 41 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 41 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 49 -> 37 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 45 -> 43 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 43 -> 58 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 47 -> 49 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 41 -> 47 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 53 -> 41 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 78897: 37 -> 45 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79098: 47 -> 49 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 41 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 53 -> 42 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 49 -> 65 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 43 -> 45 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 45 -> 37 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79103: 47 -> 42 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78899: 65 -> 37 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 45 -> 58 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 37 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 46 -> 45 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 49 -> 65 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 42 -> 47 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 42 -> 53 at (2113.5, 3025), 2 frames after previous cover
- f111: ref 78896: 58 -> 69 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 45 -> 70 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 49 -> 65 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 47 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 42 -> 47 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 53 -> 42 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 41 -> 68 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 70 -> 46 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 37 -> 70 at (2025, 3032), 2 frames after previous cover
- f113: ref 79037: 46 -> 45 at (1995, 3034.5), 1 frames after previous cover
- ... 1183 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 760 | 190 | 0 (760) |
| 78896 | 350 (76..429) | 264 | 45 | 49 (77), 69 (74), 100 (39), 141 (26), 91 (24), 43 (10), 37 (8), 58 (4), 46 (2) |
| 78969 | 352 (80..434) | 258 | 68 | 43 (133), 37 (54), 100 (33), 69 (27), 91 (5), 45 (3), 46 (3) |
| 78971 | 352 (84..439) | 253 | 68 | 43 (60), 69 (41), 37 (38), 46 (33), 91 (30), 100 (14), 45 (10), 202 (7), 49 (6), 58 (5), 76 (5), 79 (4) |
| 79045 | 355 (84..443) | 279 | 55 | 37 (59), 102 (58), 43 (51), 100 (24), 69 (22), 45 (19), 46 (17), 49 (7), 76 (6), 79 (6), 58 (5), 202 (4), +1 more |
| 79037 | 355 (86..445) | 270 | 61 | 58 (43), 102 (41), 46 (35), 37 (30), 53 (27), 43 (21), 79 (21), 45 (19), 100 (11), 76 (8), 69 (5), 41 (2), +4 more |
| 78897 | 345 (89..450) | 257 | 62 | 102 (39), 53 (29), 46 (27), 58 (26), 76 (24), 100 (22), 184 (21), 37 (19), 49 (11), 45 (8), 43 (8), 79 (7), +5 more |
| 78899 | 365 (91..455) | 272 | 67 | 46 (65), 76 (36), 79 (34), 58 (28), 53 (21), 41 (19), 49 (19), 37 (14), 184 (14), 45 (6), 47 (4), 70 (3), +4 more |
| 79097 | 366 (94..461) | 271 | 64 | 41 (61), 46 (59), 58 (36), 76 (32), 102 (31), 45 (17), 49 (12), 37 (9), 79 (5), 65 (4), 47 (3), 70 (1), +1 more |
| 79098 | 360 (97..467) | 288 | 60 | 76 (108), 58 (70), 41 (30), 49 (28), 46 (22), 79 (9), 65 (7), 102 (5), 42 (4), 47 (2), 70 (1), 37 (1), +1 more |
| 79102 | 371 (98..477) | 287 | 56 | 58 (87), 76 (49), 42 (24), 102 (23), 46 (17), 79 (15), 45 (15), 53 (14), 49 (12), 65 (12), 41 (10), 86 (6), +1 more |
| 79103 | 380 (99..481) | 292 | 72 | 42 (66), 65 (46), 76 (36), 86 (24), 58 (22), 45 (22), 41 (19), 79 (14), 49 (11), 46 (10), 53 (8), 47 (4), +3 more |
| 79105 | 379 (101..484) | 292 | 65 | 65 (117), 86 (68), 42 (20), 81 (18), 53 (16), 49 (9), 79 (8), 46 (8), 41 (8), 76 (7), 156 (7), 47 (4), +2 more |
| 79108 | 385 (104..492) | 295 | 74 | 65 (80), 81 (61), 42 (41), 86 (33), 156 (29), 41 (18), 49 (11), 53 (10), 70 (6), 102 (6) |
| 79110 | 388 (106..497) | 289 | 70 | 156 (55), 70 (48), 81 (41), 86 (40), 42 (33), 49 (21), 65 (20), 102 (8), 41 (7), 53 (6), 68 (3), 47 (3), +3 more |
| 79111 | 386 (109..500) | 297 | 71 | 86 (85), 42 (36), 156 (36), 70 (32), 49 (22), 81 (18), 117 (18), 65 (16), 41 (10), 120 (6), 47 (5), 102 (5), +3 more |
| 79115 | 421 (111..531) | 320 | 69 | 70 (67), 45 (63), 81 (52), 117 (32), 42 (24), 49 (20), 120 (14), 47 (10), 98 (9), 102 (8), 41 (7), 53 (5), +5 more |
| 79116 | 411 (114..530) | 317 | 62 | 120 (52), 70 (45), 81 (40), 98 (31), 42 (30), 45 (29), 47 (26), 71 (24), 41 (13), 117 (13), 156 (6), 53 (4), +2 more |
| 79122 | 404 (118..532) | 329 | 61 | 117 (114), 70 (55), 81 (32), 41 (27), 42 (26), 98 (23), 120 (20), 47 (16), 45 (7), 68 (4), 71 (2), 53 (2), +1 more |
| 79132 | 391 (120..515) | 286 | 80 | 70 (54), 86 (44), 41 (34), 47 (29), 98 (24), 42 (22), 117 (19), 178 (19), 156 (13), 45 (8), 81 (6), 53 (5), +4 more |
| 79128 | 402 (124..527) | 302 | 73 | 178 (86), 117 (45), 41 (37), 98 (35), 81 (29), 45 (28), 70 (24), 53 (5), 175 (5), 68 (3), 71 (2), 42 (2), +1 more |
| 79134 | 407 (127..533) | 313 | 72 | 98 (84), 53 (72), 45 (40), 175 (35), 117 (33), 163 (15), 71 (14), 70 (7), 81 (5), 68 (4), 41 (2), 120 (1), +1 more |
| 79135 | 409 (129..542) | 310 | 77 | 71 (156), 98 (59), 163 (29), 45 (22), 53 (11), 70 (11), 41 (6), 175 (6), 68 (4), 120 (3), 117 (3) |
| 79139 | 406 (132..537) | 315 | 69 | 163 (72), 71 (69), 53 (43), 98 (41), 45 (33), 68 (29), 175 (15), 120 (10), 178 (3) |
| 79136 | 393 (136..538) | 302 | 69 | 175 (85), 120 (82), 71 (62), 163 (48), 98 (10), 53 (6), 178 (6), 45 (2), 68 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 127 | 217..217 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/332/1007; tracks with internal gaps: 29; total internal gaps: 293; longest internal gap: 3; tracks ending in coasting: 15 (trailing rows total 33)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 796 | 760 | 36 | 34 | 3 | 0 | 78911 |
| 37 | 82..373 | 292 | 242 | 232 | 10 | 9 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 41 | 86..467 | 382 | 328 | 314 | 14 | 14 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 42 | 88..492 | 405 | 346 | 336 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 43 | 88..443 | 356 | 302 | 283 | 19 | 18 | 2 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 92..537 | 446 | 370 | 355 | 15 | 15 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 46 | 92..445 | 354 | 310 | 298 | 12 | 11 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 47 | 93..225 | 133 | 117 | 113 | 4 | 3 | 1 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 49 | 96..429 | 334 | 284 | 270 | 14 | 13 | 2 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 53 | 100..454 | 355 | 300 | 287 | 13 | 13 | 1 | 0 | 78897, 78899, 79037, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 58 | 103..481 | 379 | 335 | 326 | 9 | 8 | 2 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 65 | 107..484 | 378 | 319 | 305 | 14 | 14 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 68 | 111..176 | 66 | 56 | 55 | 1 | 0 | 0 | 1 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 111..392 | 282 | 186 | 175 | 11 | 3 | 1 | 8 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 70 | 111..531 | 421 | 367 | 356 | 11 | 9 | 2 | 0 | 78897, 78899, 79097, 79098, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 71 | 113..529 | 417 | 346 | 334 | 12 | 11 | 1 | 1 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 119..491 | 373 | 320 | 311 | 9 | 7 | 1 | 2 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 79 | 124..270 | 147 | 129 | 123 | 6 | 5 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 81 | 130..497 | 368 | 316 | 304 | 12 | 11 | 2 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 86 | 137..515 | 379 | 316 | 302 | 14 | 14 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132 |
| 91 | 144..224 | 81 | 63 | 59 | 4 | 2 | 1 | 2 | 78896, 78969, 78971 |
| 98 | 151..542 | 392 | 332 | 317 | 15 | 14 | 2 | 0 | 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 100 | 155..345 | 191 | 154 | 146 | 8 | 6 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 102 | 159..450 | 292 | 244 | 232 | 12 | 11 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 117 | 201..532 | 332 | 289 | 278 | 11 | 11 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 120 | 201..453 | 253 | 202 | 191 | 11 | 10 | 1 | 1 | 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 127 | 217..217 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 141 | 263..348 | 86 | 30 | 26 | 4 | 0 | 0 | 4 | 78896 |
| 156 | 312..569 | 258 | 159 | 152 | 7 | 3 | 1 | 4 | 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132, 79134 |
| 163 | 335..536 | 202 | 170 | 164 | 6 | 6 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 175 | 354..533 | 180 | 150 | 147 | 3 | 3 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 178 | 364..527 | 164 | 123 | 118 | 5 | 5 | 1 | 0 | 79115, 79116, 79128, 79132, 79136, 79139 |
| 184 | 383..452 | 70 | 41 | 38 | 3 | 0 | 0 | 3 | 78897, 78899, 79037, 79097 |
| 202 | 425..439 | 15 | 12 | 11 | 1 | 0 | 0 | 1 | 78971, 79045 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7718; unmatched reference entries: 2424; unmatched candidate entries: 337
- identity switches: 1243; fragmentation (coverage interruptions): 1780; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 41 -> 42 at (2141, 3034.5), 2 frames after previous cover
- f89: ref 79045: 42 -> 43 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 41 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 43 -> 46 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 37 -> 45 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 43 -> 37 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 43 -> 47 at (2118, 3034.5), 2 frames after previous cover
- f94: ref 78896: 46 -> 43 at (2047.5, 3031), 1 frames after previous cover
- f94: ref 78897: 42 -> 47 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 41 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 45 -> 46 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 37 -> 45 at (2090.5, 3032.5), 3 frames after previous cover
- f96: ref 78899: 42 -> 41 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f97: ref 78897: 47 -> 49 at (2107, 3033), 2 frames after previous cover
- f97: ref 78899: 41 -> 47 at (2123, 3030), 1 frames after previous cover
- f97: ref 79037: 49 -> 37 at (2093, 3032.5), 1 frames after previous cover
- f97: ref 79045: 37 -> 45 at (2081.5, 3032), 1 frames after previous cover
- f99: ref 78897: 49 -> 37 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 37 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 45 -> 46 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 37 -> 49 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 37 at (2076, 3033.5), 1 frames after previous cover
- f101: ref 78899: 47 -> 49 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 37 -> 45 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 41 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 41 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 49 -> 37 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 45 -> 43 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 43 -> 58 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 47 -> 49 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 41 -> 47 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 53 -> 41 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 78897: 37 -> 45 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 79098: 47 -> 49 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 41 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 53 -> 42 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 49 -> 65 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 43 -> 45 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 45 -> 37 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79103: 47 -> 42 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78899: 65 -> 37 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 45 -> 58 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 37 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 46 -> 45 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 49 -> 65 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 42 -> 47 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 42 -> 53 at (2113.5, 3025), 2 frames after previous cover
- f111: ref 78896: 58 -> 69 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 45 -> 70 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 49 -> 65 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 47 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 42 -> 47 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 53 -> 42 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 41 -> 68 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 70 -> 46 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 37 -> 70 at (2025, 3032), 2 frames after previous cover
- f113: ref 79037: 46 -> 45 at (1995, 3034.5), 1 frames after previous cover
- ... 1183 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 760 | 190 | 0 (760) |
| 78896 | 350 (76..429) | 264 | 45 | 49 (77), 69 (74), 100 (39), 141 (26), 91 (24), 43 (10), 37 (8), 58 (4), 46 (2) |
| 78969 | 352 (80..434) | 258 | 68 | 43 (133), 37 (54), 100 (33), 69 (27), 91 (5), 45 (3), 46 (3) |
| 78971 | 352 (84..439) | 253 | 68 | 43 (60), 69 (41), 37 (38), 46 (33), 91 (30), 100 (14), 45 (10), 202 (7), 49 (6), 58 (5), 76 (5), 79 (4) |
| 79045 | 355 (84..443) | 279 | 55 | 37 (59), 102 (58), 43 (51), 100 (24), 69 (22), 45 (19), 46 (17), 49 (7), 76 (6), 79 (6), 58 (5), 202 (4), +1 more |
| 79037 | 355 (86..445) | 270 | 61 | 58 (43), 102 (41), 46 (35), 37 (30), 53 (27), 43 (21), 79 (21), 45 (19), 100 (11), 76 (8), 69 (5), 41 (2), +4 more |
| 78897 | 345 (89..450) | 257 | 62 | 102 (39), 53 (29), 46 (27), 58 (26), 76 (24), 100 (22), 184 (21), 37 (19), 49 (11), 45 (8), 43 (8), 79 (7), +5 more |
| 78899 | 365 (91..455) | 272 | 67 | 46 (65), 76 (36), 79 (34), 58 (28), 53 (21), 41 (19), 49 (19), 37 (14), 184 (14), 45 (6), 47 (4), 70 (3), +4 more |
| 79097 | 366 (94..461) | 271 | 64 | 41 (61), 46 (59), 58 (36), 76 (32), 102 (31), 45 (17), 49 (12), 37 (9), 79 (5), 65 (4), 47 (3), 70 (1), +1 more |
| 79098 | 360 (97..467) | 288 | 60 | 76 (108), 58 (70), 41 (30), 49 (28), 46 (22), 79 (9), 65 (7), 102 (5), 42 (4), 47 (2), 70 (1), 37 (1), +1 more |
| 79102 | 371 (98..477) | 287 | 56 | 58 (87), 76 (49), 42 (24), 102 (23), 46 (17), 79 (15), 45 (15), 53 (14), 49 (12), 65 (12), 41 (10), 86 (6), +1 more |
| 79103 | 380 (99..481) | 292 | 72 | 42 (66), 65 (46), 76 (36), 86 (24), 58 (22), 45 (22), 41 (19), 79 (14), 49 (11), 46 (10), 53 (8), 47 (4), +3 more |
| 79105 | 379 (101..484) | 292 | 65 | 65 (117), 86 (68), 42 (20), 81 (18), 53 (16), 49 (9), 79 (8), 46 (8), 41 (8), 76 (7), 156 (7), 47 (4), +2 more |
| 79108 | 385 (104..492) | 295 | 74 | 65 (80), 81 (61), 42 (41), 86 (33), 156 (29), 41 (18), 49 (11), 53 (10), 70 (6), 102 (6) |
| 79110 | 388 (106..497) | 289 | 70 | 156 (55), 70 (48), 81 (41), 86 (40), 42 (33), 49 (21), 65 (20), 102 (8), 41 (7), 53 (6), 68 (3), 47 (3), +3 more |
| 79111 | 386 (109..500) | 297 | 71 | 86 (85), 42 (36), 156 (36), 70 (32), 49 (22), 81 (18), 117 (18), 65 (16), 41 (10), 120 (6), 47 (5), 102 (5), +3 more |
| 79115 | 421 (111..531) | 320 | 69 | 70 (67), 45 (63), 81 (52), 117 (32), 42 (24), 49 (20), 120 (14), 47 (10), 98 (9), 102 (8), 41 (7), 53 (5), +5 more |
| 79116 | 411 (114..530) | 317 | 62 | 120 (52), 70 (45), 81 (40), 98 (31), 42 (30), 45 (29), 47 (26), 71 (24), 41 (13), 117 (13), 156 (6), 53 (4), +2 more |
| 79122 | 404 (118..532) | 329 | 61 | 117 (114), 70 (55), 81 (32), 41 (27), 42 (26), 98 (23), 120 (20), 47 (16), 45 (7), 68 (4), 71 (2), 53 (2), +1 more |
| 79132 | 391 (120..515) | 286 | 80 | 70 (54), 86 (44), 41 (34), 47 (29), 98 (24), 42 (22), 117 (19), 178 (19), 156 (13), 45 (8), 81 (6), 53 (5), +4 more |
| 79128 | 402 (124..527) | 302 | 73 | 178 (86), 117 (45), 41 (37), 98 (35), 81 (29), 45 (28), 70 (24), 53 (5), 175 (5), 68 (3), 71 (2), 42 (2), +1 more |
| 79134 | 407 (127..533) | 313 | 72 | 98 (84), 53 (72), 45 (40), 175 (35), 117 (33), 163 (15), 71 (14), 70 (7), 81 (5), 68 (4), 41 (2), 120 (1), +1 more |
| 79135 | 409 (129..542) | 310 | 77 | 71 (156), 98 (59), 163 (29), 45 (22), 53 (11), 70 (11), 41 (6), 175 (6), 68 (4), 120 (3), 117 (3) |
| 79139 | 406 (132..537) | 315 | 69 | 163 (72), 71 (69), 53 (43), 98 (41), 45 (33), 68 (29), 175 (15), 120 (10), 178 (3) |
| 79136 | 393 (136..538) | 302 | 69 | 175 (85), 120 (82), 71 (62), 163 (48), 98 (10), 53 (6), 178 (6), 45 (2), 68 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 127 | 217..217 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 1/332/1007; tracks with internal gaps: 29; total internal gaps: 293; longest internal gap: 3; tracks ending in coasting: 15 (trailing rows total 33)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 796 | 760 | 36 | 34 | 3 | 0 | 78911 |
| 37 | 82..373 | 292 | 242 | 232 | 10 | 9 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 41 | 86..467 | 382 | 328 | 314 | 14 | 14 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 42 | 88..492 | 405 | 346 | 336 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 43 | 88..443 | 356 | 302 | 283 | 19 | 18 | 2 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 92..537 | 446 | 370 | 355 | 15 | 15 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 46 | 92..445 | 354 | 310 | 298 | 12 | 11 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 47 | 93..225 | 133 | 117 | 113 | 4 | 3 | 1 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 49 | 96..429 | 334 | 284 | 270 | 14 | 13 | 2 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 53 | 100..454 | 355 | 300 | 287 | 13 | 13 | 1 | 0 | 78897, 78899, 79037, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 58 | 103..481 | 379 | 335 | 326 | 9 | 8 | 2 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 65 | 107..484 | 378 | 319 | 305 | 14 | 14 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 68 | 111..176 | 66 | 56 | 55 | 1 | 0 | 0 | 1 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 111..392 | 282 | 186 | 175 | 11 | 3 | 1 | 8 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 70 | 111..531 | 421 | 367 | 356 | 11 | 9 | 2 | 0 | 78897, 78899, 79097, 79098, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 71 | 113..529 | 417 | 346 | 334 | 12 | 11 | 1 | 1 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 119..491 | 373 | 320 | 311 | 9 | 7 | 1 | 2 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 79 | 124..270 | 147 | 129 | 123 | 6 | 5 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 81 | 130..497 | 368 | 316 | 304 | 12 | 11 | 2 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 86 | 137..515 | 379 | 316 | 302 | 14 | 14 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132 |
| 91 | 144..224 | 81 | 63 | 59 | 4 | 2 | 1 | 2 | 78896, 78969, 78971 |
| 98 | 151..542 | 392 | 332 | 317 | 15 | 14 | 2 | 0 | 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 100 | 155..345 | 191 | 154 | 146 | 8 | 6 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 102 | 159..450 | 292 | 244 | 232 | 12 | 11 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 117 | 201..532 | 332 | 289 | 278 | 11 | 11 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 120 | 201..453 | 253 | 202 | 191 | 11 | 10 | 1 | 1 | 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 127 | 217..217 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 141 | 263..348 | 86 | 30 | 26 | 4 | 0 | 0 | 4 | 78896 |
| 156 | 312..569 | 258 | 159 | 152 | 7 | 3 | 1 | 4 | 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132, 79134 |
| 163 | 335..536 | 202 | 170 | 164 | 6 | 6 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 175 | 354..533 | 180 | 150 | 147 | 3 | 3 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 178 | 364..527 | 164 | 123 | 118 | 5 | 5 | 1 | 0 | 79115, 79116, 79128, 79132, 79136, 79139 |
| 184 | 383..452 | 70 | 41 | 38 | 3 | 0 | 0 | 3 | 78897, 78899, 79037, 79097 |
| 202 | 425..439 | 15 | 12 | 11 | 1 | 0 | 0 | 1 | 78971, 79045 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 8573; unmatched reference entries: 1569; unmatched candidate entries: 2175
- identity switches: 1257; fragmentation (coverage interruptions): 1147; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 41 -> 42 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 42 -> 43 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 41 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 43 -> 46 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 37 -> 45 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 43 -> 37 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 43 -> 47 at (2118, 3034.5), 2 frames after previous cover
- f94: ref 78896: 46 -> 43 at (2047.5, 3031), 1 frames after previous cover
- f94: ref 78897: 42 -> 47 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 41 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 45 -> 46 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 37 -> 45 at (2090.5, 3032.5), 3 frames after previous cover
- f96: ref 78899: 42 -> 41 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f96: ref 79097: 41 -> 42 at (2141, 3029), 2 frames after previous cover
- f97: ref 78897: 47 -> 49 at (2107, 3033), 1 frames after previous cover
- f97: ref 79037: 49 -> 37 at (2093, 3032.5), 1 frames after previous cover
- f98: ref 78899: 41 -> 47 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 42 -> 41 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 49 -> 37 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 37 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 37 -> 46 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 37 -> 49 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 37 at (2076, 3033.5), 1 frames after previous cover
- f101: ref 78899: 47 -> 49 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 37 -> 45 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 41 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 41 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 49 -> 37 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 45 -> 43 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 43 -> 58 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 47 -> 49 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 41 -> 47 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 53 -> 41 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 79098: 47 -> 49 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 41 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 53 -> 42 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 49 -> 65 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 43 -> 45 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 45 -> 37 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79103: 47 -> 42 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 42 -> 47 at (2118.5, 3025), 1 frames after previous cover
- f108: ref 78899: 65 -> 37 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 45 -> 58 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 37 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 46 -> 45 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 49 -> 65 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 42 -> 47 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 47 -> 53 at (2113.5, 3025), 1 frames after previous cover
- f111: ref 78896: 58 -> 69 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 37 -> 70 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 49 -> 65 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 47 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 42 -> 47 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 53 -> 42 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 41 -> 68 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 70 -> 46 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 37 -> 70 at (2025, 3032), 1 frames after previous cover
- ... 1197 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 925 | 70 | 0 (925) |
| 78896 | 350 (76..429) | 284 | 32 | 69 (84), 49 (80), 100 (44), 141 (27), 91 (25), 43 (9), 37 (9), 58 (4), 46 (2) |
| 78969 | 352 (80..434) | 284 | 51 | 43 (150), 37 (59), 100 (36), 69 (27), 91 (5), 45 (3), 46 (3), 49 (1) |
| 78971 | 352 (84..439) | 281 | 49 | 43 (66), 69 (45), 37 (38), 46 (38), 91 (32), 100 (16), 45 (14), 202 (9), 49 (8), 58 (5), 76 (5), 79 (5) |
| 79045 | 355 (84..443) | 295 | 45 | 102 (65), 37 (62), 43 (51), 100 (26), 69 (24), 46 (19), 45 (17), 49 (10), 76 (6), 58 (5), 79 (5), 202 (4), +1 more |
| 79037 | 355 (86..445) | 297 | 45 | 102 (45), 58 (43), 46 (37), 37 (32), 53 (31), 79 (24), 43 (23), 45 (21), 100 (14), 76 (9), 69 (7), 41 (3), +4 more |
| 78897 | 345 (89..450) | 273 | 50 | 102 (39), 53 (31), 46 (30), 58 (26), 76 (26), 100 (25), 184 (24), 37 (22), 49 (11), 43 (8), 45 (7), 79 (7), +5 more |
| 78899 | 365 (91..455) | 305 | 45 | 46 (71), 76 (41), 79 (39), 58 (29), 53 (23), 41 (21), 49 (21), 184 (19), 37 (18), 45 (6), 100 (4), 102 (4), +4 more |
| 79097 | 366 (94..461) | 288 | 52 | 41 (64), 46 (64), 58 (39), 76 (33), 102 (32), 45 (19), 49 (12), 37 (10), 79 (5), 65 (4), 47 (3), 42 (1), +2 more |
| 79098 | 360 (97..467) | 310 | 41 | 76 (118), 58 (75), 41 (33), 49 (28), 46 (23), 79 (9), 65 (8), 102 (6), 42 (4), 47 (2), 70 (2), 37 (1), +1 more |
| 79102 | 371 (98..477) | 312 | 35 | 58 (94), 76 (55), 42 (28), 102 (27), 46 (18), 45 (15), 53 (15), 49 (14), 79 (14), 65 (12), 41 (11), 86 (6), +1 more |
| 79103 | 380 (99..481) | 322 | 46 | 42 (75), 65 (52), 76 (39), 58 (27), 86 (24), 45 (23), 41 (21), 79 (14), 49 (12), 46 (10), 53 (9), 102 (5), +3 more |
| 79105 | 379 (101..484) | 321 | 42 | 65 (135), 86 (72), 42 (20), 81 (20), 53 (16), 49 (9), 79 (9), 41 (9), 46 (8), 156 (8), 76 (7), 47 (6), +2 more |
| 79108 | 385 (104..492) | 325 | 48 | 65 (88), 81 (69), 42 (47), 86 (36), 156 (31), 41 (20), 53 (11), 49 (11), 70 (6), 102 (6) |
| 79110 | 388 (106..497) | 323 | 51 | 156 (64), 70 (49), 81 (49), 86 (48), 42 (37), 49 (23), 65 (21), 102 (9), 41 (7), 53 (7), 68 (3), 47 (3), +2 more |
| 79111 | 386 (109..500) | 334 | 39 | 86 (99), 156 (41), 42 (37), 70 (36), 49 (26), 117 (20), 65 (19), 81 (18), 41 (13), 120 (7), 68 (5), 47 (5), +3 more |
| 79115 | 421 (111..531) | 350 | 49 | 70 (72), 45 (72), 81 (57), 117 (33), 42 (26), 49 (24), 120 (14), 102 (10), 47 (9), 98 (9), 41 (7), 53 (5), +5 more |
| 79116 | 411 (114..530) | 346 | 40 | 120 (57), 70 (50), 81 (41), 45 (33), 47 (32), 98 (32), 42 (31), 71 (27), 41 (12), 117 (11), 156 (6), 178 (5), +4 more |
| 79122 | 404 (118..532) | 355 | 40 | 117 (126), 70 (63), 81 (34), 42 (28), 41 (27), 98 (23), 120 (20), 47 (17), 45 (7), 68 (4), 53 (3), 71 (2), +1 more |
| 79132 | 391 (120..515) | 331 | 46 | 70 (65), 86 (50), 41 (38), 47 (32), 98 (31), 42 (24), 117 (23), 178 (23), 156 (16), 45 (10), 81 (6), 53 (5), +3 more |
| 79128 | 402 (124..527) | 339 | 45 | 178 (99), 117 (46), 41 (41), 98 (40), 81 (33), 45 (32), 70 (28), 53 (5), 175 (5), 68 (3), 71 (2), 42 (2), +2 more |
| 79134 | 407 (127..533) | 345 | 49 | 98 (98), 53 (76), 45 (44), 175 (38), 117 (37), 71 (15), 163 (15), 70 (7), 81 (5), 68 (4), 41 (2), 86 (2), +2 more |
| 79135 | 409 (129..542) | 349 | 42 | 71 (179), 98 (68), 163 (32), 45 (22), 70 (13), 53 (10), 41 (7), 175 (6), 68 (5), 120 (4), 117 (3) |
| 79139 | 406 (132..537) | 343 | 48 | 71 (80), 163 (78), 98 (51), 53 (48), 68 (33), 45 (33), 120 (12), 178 (6), 175 (2) |
| 79136 | 393 (136..538) | 336 | 47 | 175 (112), 120 (88), 71 (60), 163 (54), 53 (7), 178 (7), 45 (4), 98 (3), 68 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 127 | 217..246 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/361/1007; tracks with internal gaps: 33; total internal gaps: 762; longest internal gap: 12; tracks ending in coasting: 33 (trailing rows total 1159)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 925 | 82 | 70 | 4 | 0 | 78911 |
| 37 | 82..402 | 321 | 321 | 251 | 70 | 26 | 9 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 41 | 86..496 | 411 | 411 | 340 | 71 | 34 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 42 | 88..521 | 434 | 434 | 368 | 66 | 28 | 7 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 43 | 88..472 | 385 | 385 | 307 | 78 | 32 | 6 | 32 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 92..566 | 475 | 475 | 387 | 88 | 40 | 12 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 46 | 92..474 | 383 | 383 | 323 | 60 | 29 | 3 | 24 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 47 | 93..254 | 162 | 162 | 124 | 38 | 7 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 49 | 96..458 | 363 | 363 | 295 | 68 | 30 | 10 | 15 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 53 | 100..483 | 384 | 384 | 308 | 76 | 35 | 3 | 29 | 78897, 78899, 79037, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 58 | 103..510 | 408 | 408 | 347 | 61 | 25 | 3 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 65 | 107..513 | 407 | 407 | 342 | 65 | 30 | 4 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 68 | 111..205 | 95 | 95 | 61 | 34 | 3 | 2 | 30 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 111..421 | 311 | 311 | 193 | 118 | 11 | 5 | 102 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 70 | 111..560 | 450 | 450 | 397 | 53 | 21 | 2 | 28 | 78897, 78899, 79097, 79098, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 71 | 113..558 | 446 | 446 | 372 | 74 | 39 | 6 | 22 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 119..520 | 402 | 402 | 339 | 63 | 17 | 3 | 43 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 79 | 124..299 | 176 | 176 | 131 | 45 | 13 | 2 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 81 | 130..526 | 397 | 397 | 334 | 63 | 30 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 86 | 137..544 | 408 | 408 | 342 | 66 | 38 | 10 | 11 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134 |
| 91 | 144..253 | 110 | 110 | 62 | 48 | 9 | 1 | 39 | 78896, 78969, 78971 |
| 98 | 151..571 | 421 | 421 | 356 | 65 | 29 | 3 | 29 | 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 100 | 155..374 | 220 | 220 | 165 | 55 | 19 | 3 | 32 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 102 | 159..479 | 321 | 321 | 255 | 66 | 26 | 6 | 24 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 117 | 201..561 | 361 | 361 | 299 | 62 | 26 | 2 | 30 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 120 | 201..482 | 282 | 282 | 206 | 76 | 31 | 5 | 30 | 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 127 | 217..246 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 141 | 263..377 | 115 | 115 | 27 | 88 | 1 | 1 | 87 | 78896 |
| 156 | 312..598 | 287 | 287 | 173 | 114 | 14 | 2 | 98 | 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132, 79134 |
| 163 | 335..565 | 231 | 231 | 179 | 52 | 16 | 3 | 31 | 79134, 79135, 79136, 79139 |
| 175 | 354..562 | 209 | 209 | 164 | 45 | 14 | 1 | 31 | 79116, 79128, 79134, 79135, 79136, 79139 |
| 178 | 364..556 | 193 | 193 | 142 | 51 | 16 | 6 | 19 | 79115, 79116, 79128, 79132, 79136, 79139 |
| 184 | 383..481 | 99 | 99 | 46 | 53 | 2 | 2 | 50 | 78897, 78899, 79037, 79097 |
| 202 | 425..468 | 44 | 44 | 13 | 31 | 1 | 1 | 30 | 78971, 79045 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 8573; unmatched reference entries: 1569; unmatched candidate entries: 2175
- identity switches: 1257; fragmentation (coverage interruptions): 1147; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 41 -> 42 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 42 -> 43 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 41 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 43 -> 46 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 37 -> 45 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 43 -> 37 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 43 -> 47 at (2118, 3034.5), 2 frames after previous cover
- f94: ref 78896: 46 -> 43 at (2047.5, 3031), 1 frames after previous cover
- f94: ref 78897: 42 -> 47 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 41 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 45 -> 46 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 37 -> 45 at (2090.5, 3032.5), 3 frames after previous cover
- f96: ref 78899: 42 -> 41 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f96: ref 79097: 41 -> 42 at (2141, 3029), 2 frames after previous cover
- f97: ref 78897: 47 -> 49 at (2107, 3033), 1 frames after previous cover
- f97: ref 79037: 49 -> 37 at (2093, 3032.5), 1 frames after previous cover
- f98: ref 78899: 41 -> 47 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79097: 42 -> 41 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 49 -> 37 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 37 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 37 -> 46 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 37 -> 49 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 37 at (2076, 3033.5), 1 frames after previous cover
- f101: ref 78899: 47 -> 49 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 37 -> 45 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 41 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 41 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 49 -> 37 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 45 -> 43 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 43 -> 58 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 47 -> 49 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 41 -> 47 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 53 -> 41 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 79098: 47 -> 49 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 41 -> 47 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 53 -> 42 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 49 -> 65 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 43 -> 45 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 45 -> 37 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79103: 47 -> 42 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 42 -> 47 at (2118.5, 3025), 1 frames after previous cover
- f108: ref 78899: 65 -> 37 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 45 -> 58 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 37 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 46 -> 45 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 49 -> 65 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 42 -> 47 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 47 -> 53 at (2113.5, 3025), 1 frames after previous cover
- f111: ref 78896: 58 -> 69 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 37 -> 70 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 49 -> 65 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 47 -> 49 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 42 -> 47 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 53 -> 42 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 41 -> 68 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 70 -> 46 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 37 -> 70 at (2025, 3032), 1 frames after previous cover
- ... 1197 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 925 | 70 | 0 (925) |
| 78896 | 350 (76..429) | 284 | 32 | 69 (84), 49 (80), 100 (44), 141 (27), 91 (25), 43 (9), 37 (9), 58 (4), 46 (2) |
| 78969 | 352 (80..434) | 284 | 51 | 43 (150), 37 (59), 100 (36), 69 (27), 91 (5), 45 (3), 46 (3), 49 (1) |
| 78971 | 352 (84..439) | 281 | 49 | 43 (66), 69 (45), 37 (38), 46 (38), 91 (32), 100 (16), 45 (14), 202 (9), 49 (8), 58 (5), 76 (5), 79 (5) |
| 79045 | 355 (84..443) | 295 | 45 | 102 (65), 37 (62), 43 (51), 100 (26), 69 (24), 46 (19), 45 (17), 49 (10), 76 (6), 58 (5), 79 (5), 202 (4), +1 more |
| 79037 | 355 (86..445) | 297 | 45 | 102 (45), 58 (43), 46 (37), 37 (32), 53 (31), 79 (24), 43 (23), 45 (21), 100 (14), 76 (9), 69 (7), 41 (3), +4 more |
| 78897 | 345 (89..450) | 273 | 50 | 102 (39), 53 (31), 46 (30), 58 (26), 76 (26), 100 (25), 184 (24), 37 (22), 49 (11), 43 (8), 45 (7), 79 (7), +5 more |
| 78899 | 365 (91..455) | 305 | 45 | 46 (71), 76 (41), 79 (39), 58 (29), 53 (23), 41 (21), 49 (21), 184 (19), 37 (18), 45 (6), 100 (4), 102 (4), +4 more |
| 79097 | 366 (94..461) | 288 | 52 | 41 (64), 46 (64), 58 (39), 76 (33), 102 (32), 45 (19), 49 (12), 37 (10), 79 (5), 65 (4), 47 (3), 42 (1), +2 more |
| 79098 | 360 (97..467) | 310 | 41 | 76 (118), 58 (75), 41 (33), 49 (28), 46 (23), 79 (9), 65 (8), 102 (6), 42 (4), 47 (2), 70 (2), 37 (1), +1 more |
| 79102 | 371 (98..477) | 312 | 35 | 58 (94), 76 (55), 42 (28), 102 (27), 46 (18), 45 (15), 53 (15), 49 (14), 79 (14), 65 (12), 41 (11), 86 (6), +1 more |
| 79103 | 380 (99..481) | 322 | 46 | 42 (75), 65 (52), 76 (39), 58 (27), 86 (24), 45 (23), 41 (21), 79 (14), 49 (12), 46 (10), 53 (9), 102 (5), +3 more |
| 79105 | 379 (101..484) | 321 | 42 | 65 (135), 86 (72), 42 (20), 81 (20), 53 (16), 49 (9), 79 (9), 41 (9), 46 (8), 156 (8), 76 (7), 47 (6), +2 more |
| 79108 | 385 (104..492) | 325 | 48 | 65 (88), 81 (69), 42 (47), 86 (36), 156 (31), 41 (20), 53 (11), 49 (11), 70 (6), 102 (6) |
| 79110 | 388 (106..497) | 323 | 51 | 156 (64), 70 (49), 81 (49), 86 (48), 42 (37), 49 (23), 65 (21), 102 (9), 41 (7), 53 (7), 68 (3), 47 (3), +2 more |
| 79111 | 386 (109..500) | 334 | 39 | 86 (99), 156 (41), 42 (37), 70 (36), 49 (26), 117 (20), 65 (19), 81 (18), 41 (13), 120 (7), 68 (5), 47 (5), +3 more |
| 79115 | 421 (111..531) | 350 | 49 | 70 (72), 45 (72), 81 (57), 117 (33), 42 (26), 49 (24), 120 (14), 102 (10), 47 (9), 98 (9), 41 (7), 53 (5), +5 more |
| 79116 | 411 (114..530) | 346 | 40 | 120 (57), 70 (50), 81 (41), 45 (33), 47 (32), 98 (32), 42 (31), 71 (27), 41 (12), 117 (11), 156 (6), 178 (5), +4 more |
| 79122 | 404 (118..532) | 355 | 40 | 117 (126), 70 (63), 81 (34), 42 (28), 41 (27), 98 (23), 120 (20), 47 (17), 45 (7), 68 (4), 53 (3), 71 (2), +1 more |
| 79132 | 391 (120..515) | 331 | 46 | 70 (65), 86 (50), 41 (38), 47 (32), 98 (31), 42 (24), 117 (23), 178 (23), 156 (16), 45 (10), 81 (6), 53 (5), +3 more |
| 79128 | 402 (124..527) | 339 | 45 | 178 (99), 117 (46), 41 (41), 98 (40), 81 (33), 45 (32), 70 (28), 53 (5), 175 (5), 68 (3), 71 (2), 42 (2), +2 more |
| 79134 | 407 (127..533) | 345 | 49 | 98 (98), 53 (76), 45 (44), 175 (38), 117 (37), 71 (15), 163 (15), 70 (7), 81 (5), 68 (4), 41 (2), 86 (2), +2 more |
| 79135 | 409 (129..542) | 349 | 42 | 71 (179), 98 (68), 163 (32), 45 (22), 70 (13), 53 (10), 41 (7), 175 (6), 68 (5), 120 (4), 117 (3) |
| 79139 | 406 (132..537) | 343 | 48 | 71 (80), 163 (78), 98 (51), 53 (48), 68 (33), 45 (33), 120 (12), 178 (6), 175 (2) |
| 79136 | 393 (136..538) | 336 | 47 | 175 (112), 120 (88), 71 (60), 163 (54), 53 (7), 178 (7), 45 (4), 98 (3), 68 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 127 | 217..246 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 30/361/1007; tracks with internal gaps: 33; total internal gaps: 762; longest internal gap: 12; tracks ending in coasting: 33 (trailing rows total 1159)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 925 | 82 | 70 | 4 | 0 | 78911 |
| 37 | 82..402 | 321 | 321 | 251 | 70 | 26 | 9 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 41 | 86..496 | 411 | 411 | 340 | 71 | 34 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 42 | 88..521 | 434 | 434 | 368 | 66 | 28 | 7 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 43 | 88..472 | 385 | 385 | 307 | 78 | 32 | 6 | 32 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 92..566 | 475 | 475 | 387 | 88 | 40 | 12 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 46 | 92..474 | 383 | 383 | 323 | 60 | 29 | 3 | 24 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 47 | 93..254 | 162 | 162 | 124 | 38 | 7 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 49 | 96..458 | 363 | 363 | 295 | 68 | 30 | 10 | 15 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 53 | 100..483 | 384 | 384 | 308 | 76 | 35 | 3 | 29 | 78897, 78899, 79037, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 58 | 103..510 | 408 | 408 | 347 | 61 | 25 | 3 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 65 | 107..513 | 407 | 407 | 342 | 65 | 30 | 4 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 68 | 111..205 | 95 | 95 | 61 | 34 | 3 | 2 | 30 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 69 | 111..421 | 311 | 311 | 193 | 118 | 11 | 5 | 102 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 70 | 111..560 | 450 | 450 | 397 | 53 | 21 | 2 | 28 | 78897, 78899, 79097, 79098, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 71 | 113..558 | 446 | 446 | 372 | 74 | 39 | 6 | 22 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 119..520 | 402 | 402 | 339 | 63 | 17 | 3 | 43 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 79 | 124..299 | 176 | 176 | 131 | 45 | 13 | 2 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 81 | 130..526 | 397 | 397 | 334 | 63 | 30 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 86 | 137..544 | 408 | 408 | 342 | 66 | 38 | 10 | 11 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134 |
| 91 | 144..253 | 110 | 110 | 62 | 48 | 9 | 1 | 39 | 78896, 78969, 78971 |
| 98 | 151..571 | 421 | 421 | 356 | 65 | 29 | 3 | 29 | 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 100 | 155..374 | 220 | 220 | 165 | 55 | 19 | 3 | 32 | 78896, 78897, 78899, 78969, 78971, 79037, 79045 |
| 102 | 159..479 | 321 | 321 | 255 | 66 | 26 | 6 | 24 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 117 | 201..561 | 361 | 361 | 299 | 62 | 26 | 2 | 30 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 120 | 201..482 | 282 | 282 | 206 | 76 | 31 | 5 | 30 | 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 127 | 217..246 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 141 | 263..377 | 115 | 115 | 27 | 88 | 1 | 1 | 87 | 78896 |
| 156 | 312..598 | 287 | 287 | 173 | 114 | 14 | 2 | 98 | 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79132, 79134 |
| 163 | 335..565 | 231 | 231 | 179 | 52 | 16 | 3 | 31 | 79134, 79135, 79136, 79139 |
| 175 | 354..562 | 209 | 209 | 164 | 45 | 14 | 1 | 31 | 79116, 79128, 79134, 79135, 79136, 79139 |
| 178 | 364..556 | 193 | 193 | 142 | 51 | 16 | 6 | 19 | 79115, 79116, 79128, 79132, 79136, 79139 |
| 184 | 383..481 | 99 | 99 | 46 | 53 | 2 | 2 | 50 | 78897, 78899, 79037, 79097 |
| 202 | 425..468 | 44 | 44 | 13 | 31 | 1 | 1 | 30 | 78971, 79045 |
