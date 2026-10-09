# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=f1b982f4e484
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise1.0_fp0.5_seed1/tracks.csv sha256=40eac7d09e8e3ef7
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise1.0_fp0.5_seed1.csv sha256=f1b982f4e48407ec
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise1.0_fp0.5_seed1
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
| observations | none | 4 | 10142 | 8046 | 0.291 | 0.647 | 0.131 | 1.07 | 0.347 | 0.671 | 1.26 | 1092 | 1634.0 | 0.294 | 0.332 | 0.263 | 0.786 | 0.991 | 7972 | 2170 | 74 | 5 | 20 | 0 |
| observations | none | 6 | 10142 | 8046 | 0.313 | 0.693 | 0.141 | 1.16 | 0.348 | 0.674 | 1.27 | 1080 | 1625.0 | 0.295 | 0.333 | 0.264 | 0.787 | 0.992 | 7980 | 2162 | 66 | 5 | 20 | 0 |
| observations | none | 8 | 10142 | 8046 | 0.324 | 0.714 | 0.147 | 1.23 | 0.348 | 0.674 | 1.31 | 1070 | 1620.0 | 0.298 | 0.337 | 0.267 | 0.786 | 0.991 | 7974 | 2168 | 72 | 5 | 20 | 0 |
| observations | none | 12 | 10142 | 8046 | 0.337 | 0.724 | 0.157 | 1.46 | 0.350 | 0.678 | 1.59 | 970 | 1588.0 | 0.314 | 0.355 | 0.282 | 0.783 | 0.987 | 7945 | 2197 | 101 | 4 | 21 | 0 |
| observations | ignore | 4 | 10142 | 8046 | 0.291 | 0.647 | 0.131 | 1.07 | 0.347 | 0.671 | 1.26 | 1092 | 1634.0 | 0.294 | 0.332 | 0.263 | 0.786 | 0.991 | 7972 | 2170 | 74 | 5 | 20 | 0 |
| observations | ignore | 6 | 10142 | 8046 | 0.313 | 0.693 | 0.141 | 1.16 | 0.348 | 0.674 | 1.27 | 1080 | 1625.0 | 0.295 | 0.333 | 0.264 | 0.787 | 0.992 | 7980 | 2162 | 66 | 5 | 20 | 0 |
| observations | ignore | 8 | 10142 | 8046 | 0.324 | 0.714 | 0.147 | 1.23 | 0.348 | 0.674 | 1.31 | 1070 | 1620.0 | 0.298 | 0.337 | 0.267 | 0.786 | 0.991 | 7974 | 2168 | 72 | 5 | 20 | 0 |
| observations | ignore | 12 | 10142 | 8046 | 0.337 | 0.724 | 0.157 | 1.46 | 0.350 | 0.678 | 1.59 | 970 | 1588.0 | 0.314 | 0.355 | 0.282 | 0.783 | 0.987 | 7945 | 2197 | 101 | 4 | 21 | 0 |
| updates | none | 4 | 10142 | 10774 | 0.275 | 0.560 | 0.136 | 1.19 | 0.316 | 0.444 | 1.30 | 1120 | 1556.0 | 0.270 | 0.262 | 0.279 | 0.808 | 0.761 | 8196 | 1946 | 2578 | 13 | 12 | 0 |
| updates | none | 6 | 10142 | 10774 | 0.313 | 0.635 | 0.155 | 1.45 | 0.344 | 0.529 | 1.50 | 1111 | 1212.0 | 0.289 | 0.280 | 0.298 | 0.851 | 0.801 | 8626 | 1516 | 2148 | 24 | 1 | 0 |
| updates | none | 8 | 10142 | 10774 | 0.334 | 0.674 | 0.166 | 1.62 | 0.370 | 0.616 | 1.79 | 1080 | 859.0 | 0.306 | 0.297 | 0.315 | 0.892 | 0.840 | 9050 | 1092 | 1724 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10774 | 0.358 | 0.707 | 0.181 | 1.99 | 0.386 | 0.658 | 2.26 | 969 | 687.0 | 0.329 | 0.319 | 0.339 | 0.908 | 0.855 | 9207 | 935 | 1567 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10774 | 0.275 | 0.560 | 0.136 | 1.19 | 0.316 | 0.444 | 1.30 | 1120 | 1556.0 | 0.270 | 0.262 | 0.279 | 0.808 | 0.761 | 8196 | 1946 | 2578 | 13 | 12 | 0 |
| updates | ignore | 6 | 10142 | 10774 | 0.313 | 0.635 | 0.155 | 1.45 | 0.344 | 0.529 | 1.50 | 1111 | 1212.0 | 0.289 | 0.280 | 0.298 | 0.851 | 0.801 | 8626 | 1516 | 2148 | 24 | 1 | 0 |
| updates | ignore | 8 | 10142 | 10774 | 0.334 | 0.674 | 0.166 | 1.62 | 0.370 | 0.616 | 1.79 | 1080 | 859.0 | 0.306 | 0.297 | 0.315 | 0.892 | 0.840 | 9050 | 1092 | 1724 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10774 | 0.358 | 0.707 | 0.181 | 1.99 | 0.386 | 0.658 | 2.26 | 969 | 687.0 | 0.329 | 0.319 | 0.339 | 0.908 | 0.855 | 9207 | 935 | 1567 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 35; matched pairs: 7974; unmatched reference entries: 2168; unmatched candidate entries: 72
- identity switches: 1070; fragmentation (coverage interruptions): 1637; orphan candidate ids (never on a reference object): 1

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
- f96: ref 78899: 42 -> 47 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f97: ref 78897: 47 -> 37 at (2107, 3033), 2 frames after previous cover
- f97: ref 78971: 45 -> 46 at (2072, 3034.5), 2 frames after previous cover
- f97: ref 79045: 37 -> 45 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 78971: 46 -> 45 at (2066, 3034), 1 frames after previous cover
- f98: ref 79097: 41 -> 47 at (2129, 3028), 3 frames after previous cover
- f98: ref 79098: 41 -> 42 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 37 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 47 -> 37 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 49 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 45 -> 46 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79098: 42 -> 47 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 41 -> 42 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78897: 49 -> 47 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 47 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 47 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 47 -> 49 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 79037: 49 -> 46 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 46 -> 45 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79097: 53 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 53 at (2124, 3028), 1 frames after previous cover
- f104: ref 79097: 47 -> 37 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 53 -> 47 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 42 -> 53 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 41 -> 42 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 43 -> 45 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 45 -> 64 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79098: 47 -> 37 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 42 -> 53 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 41 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 37 -> 66 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 45 -> 46 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 46 -> 49 at (2031, 3033.5), 2 frames after previous cover
- f108: ref 78899: 66 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 45 -> 43 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 46 -> 45 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 37 -> 66 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 53 -> 41 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 41 -> 47 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 47 -> 53 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 43 -> 70 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 49 -> 71 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 37 -> 66 at (2065.5, 3029), 1 frames after previous cover
- ... 1010 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 785 | 175 | 0 (785) |
| 78896 | 350 (76..429) | 267 | 46 | 43 (95), 77 (76), 46 (42), 109 (30), 70 (21), 93 (3) |
| 78969 | 352 (80..434) | 274 | 58 | 109 (75), 43 (69), 41 (52), 77 (23), 93 (22), 45 (21), 46 (5), 37 (4), 70 (3) |
| 78971 | 352 (84..439) | 269 | 65 | 45 (59), 186 (52), 93 (37), 109 (29), 70 (24), 46 (21), 41 (18), 77 (8), 82 (7), 37 (6), 43 (6), 88 (2) |
| 79045 | 355 (84..443) | 282 | 55 | 45 (91), 119 (39), 64 (23), 41 (20), 49 (19), 82 (17), 88 (17), 46 (15), 109 (14), 77 (10), 70 (7), 37 (5), +3 more |
| 79037 | 355 (86..445) | 280 | 57 | 49 (76), 45 (68), 42 (38), 46 (26), 82 (23), 88 (16), 119 (15), 41 (11), 109 (4), 43 (1), 47 (1), 64 (1) |
| 78897 | 345 (89..450) | 266 | 55 | 49 (56), 37 (42), 88 (30), 119 (28), 41 (24), 82 (14), 71 (11), 77 (11), 42 (10), 45 (10), 46 (8), 109 (8), +4 more |
| 78899 | 365 (91..455) | 280 | 67 | 41 (68), 37 (64), 88 (39), 49 (25), 72 (23), 45 (10), 77 (10), 119 (9), 53 (8), 82 (7), 42 (5), 64 (4), +5 more |
| 79097 | 366 (94..461) | 279 | 60 | 45 (49), 37 (40), 82 (33), 53 (31), 64 (30), 49 (17), 88 (15), 41 (14), 77 (12), 46 (10), 42 (10), 47 (5), +4 more |
| 79098 | 360 (97..467) | 296 | 51 | 64 (63), 198 (54), 119 (24), 41 (23), 47 (23), 37 (23), 46 (22), 53 (19), 88 (12), 189 (9), 66 (7), 42 (5), +4 more |
| 79102 | 371 (98..477) | 298 | 49 | 64 (86), 37 (42), 49 (37), 53 (28), 46 (16), 45 (13), 41 (12), 88 (11), 104 (11), 189 (11), 77 (7), 119 (7), +5 more |
| 79103 | 380 (99..481) | 298 | 67 | 41 (50), 64 (40), 72 (37), 189 (35), 46 (30), 53 (29), 49 (18), 119 (17), 37 (15), 104 (13), 88 (5), 47 (5), +3 more |
| 79105 | 379 (101..484) | 296 | 63 | 53 (56), 119 (49), 104 (35), 64 (35), 37 (31), 49 (21), 72 (19), 41 (12), 122 (9), 46 (8), 47 (7), 88 (4), +5 more |
| 79108 | 385 (104..492) | 304 | 67 | 49 (41), 72 (32), 53 (27), 37 (26), 64 (26), 122 (25), 189 (25), 160 (21), 119 (19), 46 (17), 77 (14), 102 (13), +5 more |
| 79110 | 388 (106..497) | 303 | 67 | 122 (55), 53 (49), 77 (39), 49 (30), 37 (24), 72 (23), 144 (19), 47 (12), 64 (12), 42 (11), 160 (10), 104 (6), +5 more |
| 79111 | 386 (109..500) | 303 | 66 | 122 (62), 160 (62), 144 (47), 72 (20), 66 (19), 77 (18), 53 (16), 102 (16), 47 (11), 71 (11), 42 (8), 69 (5), +3 more |
| 79115 | 421 (111..531) | 339 | 57 | 104 (71), 144 (48), 47 (47), 122 (36), 53 (32), 71 (29), 66 (23), 42 (14), 77 (13), 160 (11), 102 (9), 83 (3), +2 more |
| 79116 | 411 (114..530) | 328 | 60 | 144 (77), 66 (52), 71 (39), 47 (32), 102 (23), 168 (23), 83 (19), 104 (15), 42 (13), 122 (9), 160 (6), 69 (5), +4 more |
| 79122 | 404 (118..532) | 336 | 55 | 47 (60), 42 (57), 66 (57), 71 (51), 144 (30), 122 (24), 53 (16), 83 (16), 104 (15), 72 (4), 69 (4), 160 (1), +1 more |
| 79132 | 391 (120..515) | 296 | 75 | 66 (119), 160 (57), 42 (33), 71 (31), 122 (17), 83 (13), 104 (9), 72 (5), 144 (5), 47 (4), 69 (3) |
| 79128 | 402 (124..527) | 312 | 67 | 71 (135), 66 (64), 47 (40), 42 (21), 122 (16), 69 (14), 104 (14), 83 (5), 72 (3) |
| 79134 | 407 (127..533) | 324 | 62 | 179 (113), 69 (61), 104 (36), 83 (35), 42 (30), 71 (27), 168 (8), 72 (6), 66 (4), 47 (2), 122 (1), 160 (1) |
| 79135 | 409 (129..542) | 320 | 71 | 69 (115), 168 (74), 83 (48), 42 (40), 179 (38), 72 (4), 47 (1) |
| 79139 | 406 (132..537) | 327 | 60 | 83 (156), 69 (65), 47 (45), 168 (25), 100 (21), 42 (7), 104 (5), 72 (3) |
| 79136 | 393 (136..538) | 312 | 62 | 69 (84), 72 (78), 47 (55), 83 (47), 168 (26), 104 (15), 179 (4), 71 (3) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 129 | 217..217 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 1/272/1007; tracks with internal gaps: 18; total internal gaps: 41; longest internal gap: 1; tracks ending in coasting: 14 (trailing rows total 31)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 796 | 785 | 11 | 11 | 1 | 0 | 78911 |
| 37 | 82..454 | 373 | 325 | 325 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 41 | 86..443 | 358 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 88..445 | 358 | 311 | 309 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 43 | 88..348 | 261 | 179 | 174 | 5 | 1 | 1 | 4 | 78896, 78969, 78971, 79037, 79045 |
| 45 | 92..484 | 393 | 328 | 325 | 3 | 3 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79105 |
| 46 | 92..345 | 254 | 223 | 221 | 2 | 1 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..531 | 439 | 370 | 367 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 96..497 | 402 | 343 | 343 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 100..480 | 381 | 324 | 319 | 5 | 4 | 1 | 1 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 64 | 106..481 | 376 | 322 | 321 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 66 | 107..527 | 421 | 351 | 351 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 111..536 | 426 | 360 | 360 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 111..181 | 71 | 57 | 55 | 2 | 0 | 0 | 2 | 78896, 78969, 78971, 79045 |
| 71 | 111..533 | 423 | 352 | 351 | 1 | 1 | 1 | 0 | 78897, 78899, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 72 | 113..452 | 340 | 267 | 263 | 4 | 2 | 1 | 2 | 78899, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 119..429 | 311 | 254 | 251 | 3 | 3 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 82 | 129..270 | 142 | 110 | 106 | 4 | 2 | 1 | 2 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 130..537 | 408 | 346 | 345 | 1 | 1 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 88 | 137..392 | 256 | 163 | 155 | 8 | 0 | 0 | 8 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 93 | 144..224 | 81 | 64 | 62 | 2 | 0 | 0 | 2 | 78896, 78969, 78971 |
| 100 | 151..176 | 26 | 22 | 21 | 1 | 0 | 0 | 1 | 79139 |
| 102 | 155..225 | 71 | 66 | 65 | 1 | 0 | 0 | 1 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 104 | 159..453 | 295 | 255 | 253 | 2 | 1 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 109 | 181..373 | 193 | 162 | 161 | 1 | 0 | 0 | 1 | 78896, 78897, 78969, 78971, 79037, 79045, 79097 |
| 119 | 201..450 | 250 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108 |
| 122 | 201..569 | 369 | 263 | 257 | 6 | 2 | 1 | 4 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 129 | 217..217 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 144 | 261..532 | 272 | 229 | 228 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 160 | 312..515 | 204 | 172 | 171 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134 |
| 168 | 335..529 | 195 | 157 | 157 | 0 | 0 | 0 | 0 | 79116, 79122, 79134, 79135, 79136, 79139 |
| 179 | 354..542 | 189 | 157 | 156 | 1 | 1 | 1 | 0 | 79116, 79134, 79135, 79136 |
| 186 | 374..439 | 66 | 53 | 53 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 189 | 383..492 | 110 | 92 | 92 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79108 |
| 198 | 402..467 | 66 | 59 | 59 | 0 | 0 | 0 | 0 | 79097, 79098 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 35; matched pairs: 7974; unmatched reference entries: 2168; unmatched candidate entries: 72
- identity switches: 1070; fragmentation (coverage interruptions): 1637; orphan candidate ids (never on a reference object): 1

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
- f96: ref 78899: 42 -> 47 at (2128, 3029), 1 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f97: ref 78897: 47 -> 37 at (2107, 3033), 2 frames after previous cover
- f97: ref 78971: 45 -> 46 at (2072, 3034.5), 2 frames after previous cover
- f97: ref 79045: 37 -> 45 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 78971: 46 -> 45 at (2066, 3034), 1 frames after previous cover
- f98: ref 79097: 41 -> 47 at (2129, 3028), 3 frames after previous cover
- f98: ref 79098: 41 -> 42 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 37 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 47 -> 37 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 49 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 45 -> 46 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79098: 42 -> 47 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 41 -> 42 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78897: 49 -> 47 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 47 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 47 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 47 -> 49 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 79037: 49 -> 46 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 46 -> 45 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79097: 53 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 53 at (2124, 3028), 1 frames after previous cover
- f104: ref 79097: 47 -> 37 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 53 -> 47 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 42 -> 53 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 41 -> 42 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 43 -> 45 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 45 -> 64 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79098: 47 -> 37 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 42 -> 53 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 41 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 37 -> 66 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 45 -> 46 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 46 -> 49 at (2031, 3033.5), 2 frames after previous cover
- f108: ref 78899: 66 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 45 -> 43 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 46 -> 45 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 37 -> 66 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 53 -> 41 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 41 -> 47 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 47 -> 53 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 43 -> 70 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 49 -> 71 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 37 -> 66 at (2065.5, 3029), 1 frames after previous cover
- ... 1010 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 785 | 175 | 0 (785) |
| 78896 | 350 (76..429) | 267 | 46 | 43 (95), 77 (76), 46 (42), 109 (30), 70 (21), 93 (3) |
| 78969 | 352 (80..434) | 274 | 58 | 109 (75), 43 (69), 41 (52), 77 (23), 93 (22), 45 (21), 46 (5), 37 (4), 70 (3) |
| 78971 | 352 (84..439) | 269 | 65 | 45 (59), 186 (52), 93 (37), 109 (29), 70 (24), 46 (21), 41 (18), 77 (8), 82 (7), 37 (6), 43 (6), 88 (2) |
| 79045 | 355 (84..443) | 282 | 55 | 45 (91), 119 (39), 64 (23), 41 (20), 49 (19), 82 (17), 88 (17), 46 (15), 109 (14), 77 (10), 70 (7), 37 (5), +3 more |
| 79037 | 355 (86..445) | 280 | 57 | 49 (76), 45 (68), 42 (38), 46 (26), 82 (23), 88 (16), 119 (15), 41 (11), 109 (4), 43 (1), 47 (1), 64 (1) |
| 78897 | 345 (89..450) | 266 | 55 | 49 (56), 37 (42), 88 (30), 119 (28), 41 (24), 82 (14), 71 (11), 77 (11), 42 (10), 45 (10), 46 (8), 109 (8), +4 more |
| 78899 | 365 (91..455) | 280 | 67 | 41 (68), 37 (64), 88 (39), 49 (25), 72 (23), 45 (10), 77 (10), 119 (9), 53 (8), 82 (7), 42 (5), 64 (4), +5 more |
| 79097 | 366 (94..461) | 279 | 60 | 45 (49), 37 (40), 82 (33), 53 (31), 64 (30), 49 (17), 88 (15), 41 (14), 77 (12), 46 (10), 42 (10), 47 (5), +4 more |
| 79098 | 360 (97..467) | 296 | 51 | 64 (63), 198 (54), 119 (24), 41 (23), 47 (23), 37 (23), 46 (22), 53 (19), 88 (12), 189 (9), 66 (7), 42 (5), +4 more |
| 79102 | 371 (98..477) | 298 | 49 | 64 (86), 37 (42), 49 (37), 53 (28), 46 (16), 45 (13), 41 (12), 88 (11), 104 (11), 189 (11), 77 (7), 119 (7), +5 more |
| 79103 | 380 (99..481) | 298 | 67 | 41 (50), 64 (40), 72 (37), 189 (35), 46 (30), 53 (29), 49 (18), 119 (17), 37 (15), 104 (13), 88 (5), 47 (5), +3 more |
| 79105 | 379 (101..484) | 296 | 63 | 53 (56), 119 (49), 104 (35), 64 (35), 37 (31), 49 (21), 72 (19), 41 (12), 122 (9), 46 (8), 47 (7), 88 (4), +5 more |
| 79108 | 385 (104..492) | 304 | 67 | 49 (41), 72 (32), 53 (27), 37 (26), 64 (26), 122 (25), 189 (25), 160 (21), 119 (19), 46 (17), 77 (14), 102 (13), +5 more |
| 79110 | 388 (106..497) | 303 | 67 | 122 (55), 53 (49), 77 (39), 49 (30), 37 (24), 72 (23), 144 (19), 47 (12), 64 (12), 42 (11), 160 (10), 104 (6), +5 more |
| 79111 | 386 (109..500) | 303 | 66 | 122 (62), 160 (62), 144 (47), 72 (20), 66 (19), 77 (18), 53 (16), 102 (16), 47 (11), 71 (11), 42 (8), 69 (5), +3 more |
| 79115 | 421 (111..531) | 339 | 57 | 104 (71), 144 (48), 47 (47), 122 (36), 53 (32), 71 (29), 66 (23), 42 (14), 77 (13), 160 (11), 102 (9), 83 (3), +2 more |
| 79116 | 411 (114..530) | 328 | 60 | 144 (77), 66 (52), 71 (39), 47 (32), 102 (23), 168 (23), 83 (19), 104 (15), 42 (13), 122 (9), 160 (6), 69 (5), +4 more |
| 79122 | 404 (118..532) | 336 | 55 | 47 (60), 42 (57), 66 (57), 71 (51), 144 (30), 122 (24), 53 (16), 83 (16), 104 (15), 72 (4), 69 (4), 160 (1), +1 more |
| 79132 | 391 (120..515) | 296 | 75 | 66 (119), 160 (57), 42 (33), 71 (31), 122 (17), 83 (13), 104 (9), 72 (5), 144 (5), 47 (4), 69 (3) |
| 79128 | 402 (124..527) | 312 | 67 | 71 (135), 66 (64), 47 (40), 42 (21), 122 (16), 69 (14), 104 (14), 83 (5), 72 (3) |
| 79134 | 407 (127..533) | 324 | 62 | 179 (113), 69 (61), 104 (36), 83 (35), 42 (30), 71 (27), 168 (8), 72 (6), 66 (4), 47 (2), 122 (1), 160 (1) |
| 79135 | 409 (129..542) | 320 | 71 | 69 (115), 168 (74), 83 (48), 42 (40), 179 (38), 72 (4), 47 (1) |
| 79139 | 406 (132..537) | 327 | 60 | 83 (156), 69 (65), 47 (45), 168 (25), 100 (21), 42 (7), 104 (5), 72 (3) |
| 79136 | 393 (136..538) | 312 | 62 | 69 (84), 72 (78), 47 (55), 83 (47), 168 (26), 104 (15), 179 (4), 71 (3) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 129 | 217..217 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 1/272/1007; tracks with internal gaps: 18; total internal gaps: 41; longest internal gap: 1; tracks ending in coasting: 14 (trailing rows total 31)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 796 | 785 | 11 | 11 | 1 | 0 | 78911 |
| 37 | 82..454 | 373 | 325 | 325 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 41 | 86..443 | 358 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 88..445 | 358 | 311 | 309 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 43 | 88..348 | 261 | 179 | 174 | 5 | 1 | 1 | 4 | 78896, 78969, 78971, 79037, 79045 |
| 45 | 92..484 | 393 | 328 | 325 | 3 | 3 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79105 |
| 46 | 92..345 | 254 | 223 | 221 | 2 | 1 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..531 | 439 | 370 | 367 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 96..497 | 402 | 343 | 343 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 100..480 | 381 | 324 | 319 | 5 | 4 | 1 | 1 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 64 | 106..481 | 376 | 322 | 321 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 66 | 107..527 | 421 | 351 | 351 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 111..536 | 426 | 360 | 360 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 111..181 | 71 | 57 | 55 | 2 | 0 | 0 | 2 | 78896, 78969, 78971, 79045 |
| 71 | 111..533 | 423 | 352 | 351 | 1 | 1 | 1 | 0 | 78897, 78899, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 72 | 113..452 | 340 | 267 | 263 | 4 | 2 | 1 | 2 | 78899, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 119..429 | 311 | 254 | 251 | 3 | 3 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 82 | 129..270 | 142 | 110 | 106 | 4 | 2 | 1 | 2 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 130..537 | 408 | 346 | 345 | 1 | 1 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 88 | 137..392 | 256 | 163 | 155 | 8 | 0 | 0 | 8 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 93 | 144..224 | 81 | 64 | 62 | 2 | 0 | 0 | 2 | 78896, 78969, 78971 |
| 100 | 151..176 | 26 | 22 | 21 | 1 | 0 | 0 | 1 | 79139 |
| 102 | 155..225 | 71 | 66 | 65 | 1 | 0 | 0 | 1 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 104 | 159..453 | 295 | 255 | 253 | 2 | 1 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 109 | 181..373 | 193 | 162 | 161 | 1 | 0 | 0 | 1 | 78896, 78897, 78969, 78971, 79037, 79045, 79097 |
| 119 | 201..450 | 250 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108 |
| 122 | 201..569 | 369 | 263 | 257 | 6 | 2 | 1 | 4 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 129 | 217..217 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 144 | 261..532 | 272 | 229 | 228 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 160 | 312..515 | 204 | 172 | 171 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134 |
| 168 | 335..529 | 195 | 157 | 157 | 0 | 0 | 0 | 0 | 79116, 79122, 79134, 79135, 79136, 79139 |
| 179 | 354..542 | 189 | 157 | 156 | 1 | 1 | 1 | 0 | 79116, 79134, 79135, 79136 |
| 186 | 374..439 | 66 | 53 | 53 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 189 | 383..492 | 110 | 92 | 92 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79108 |
| 198 | 402..467 | 66 | 59 | 59 | 0 | 0 | 0 | 0 | 79097, 79098 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 35; matched pairs: 9050; unmatched reference entries: 1092; unmatched candidate entries: 1724
- identity switches: 1080; fragmentation (coverage interruptions): 787; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 41 -> 42 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 42 -> 43 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 41 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 43 -> 46 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 37 -> 45 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 43 -> 37 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 43 -> 47 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78896: 46 -> 43 at (2047.5, 3031), 1 frames after previous cover
- f94: ref 78897: 42 -> 47 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 41 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 45 -> 46 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 37 -> 45 at (2090.5, 3032.5), 3 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f97: ref 78897: 47 -> 37 at (2107, 3033), 2 frames after previous cover
- f97: ref 78899: 42 -> 47 at (2123, 3030), 1 frames after previous cover
- f97: ref 78971: 45 -> 46 at (2072, 3034.5), 1 frames after previous cover
- f97: ref 79045: 37 -> 45 at (2081.5, 3032), 1 frames after previous cover
- f97: ref 79097: 41 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 46 -> 45 at (2066, 3034), 1 frames after previous cover
- f98: ref 79097: 42 -> 47 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 41 -> 42 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 37 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 47 -> 37 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 49 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 45 -> 46 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79098: 42 -> 47 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 41 -> 42 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78897: 49 -> 47 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 47 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 47 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 47 -> 49 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 79037: 49 -> 46 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 46 -> 45 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79097: 53 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 53 at (2124, 3028), 1 frames after previous cover
- f104: ref 79097: 47 -> 37 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 53 -> 47 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 42 -> 53 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 41 -> 42 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 43 -> 45 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 45 -> 64 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79098: 47 -> 37 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 42 -> 53 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 41 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 37 -> 66 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 45 -> 46 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 46 -> 49 at (2031, 3033.5), 1 frames after previous cover
- f108: ref 78899: 66 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 45 -> 43 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 46 -> 45 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 37 -> 66 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 53 -> 41 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 41 -> 47 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 47 -> 53 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 43 -> 70 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 49 -> 71 at (2021.5, 3032.5), 5 frames after previous cover
- ... 1020 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 972 | 29 | 0 (972) |
| 78896 | 350 (76..429) | 293 | 26 | 43 (104), 77 (82), 46 (46), 109 (34), 70 (24), 93 (3) |
| 78969 | 352 (80..434) | 310 | 31 | 109 (87), 43 (79), 41 (58), 45 (26), 77 (25), 93 (23), 46 (5), 37 (4), 70 (3) |
| 78971 | 352 (84..439) | 307 | 34 | 45 (65), 186 (61), 93 (42), 109 (34), 70 (27), 41 (25), 46 (23), 82 (8), 77 (8), 37 (6), 43 (6), 88 (2) |
| 79045 | 355 (84..443) | 305 | 37 | 45 (96), 119 (48), 64 (23), 49 (21), 41 (21), 88 (19), 82 (18), 46 (17), 109 (14), 77 (10), 70 (8), 37 (5), +3 more |
| 79037 | 355 (86..445) | 315 | 28 | 49 (83), 45 (77), 42 (45), 46 (27), 82 (26), 88 (19), 119 (18), 41 (12), 109 (4), 43 (2), 47 (1), 64 (1) |
| 78897 | 345 (89..450) | 289 | 37 | 49 (60), 37 (46), 88 (35), 119 (29), 41 (25), 82 (16), 77 (13), 71 (12), 42 (10), 45 (10), 46 (9), 189 (9), +4 more |
| 78899 | 365 (91..455) | 320 | 36 | 37 (76), 41 (75), 88 (45), 49 (30), 72 (29), 45 (11), 77 (11), 119 (11), 53 (8), 82 (7), 42 (6), 64 (4), +5 more |
| 79097 | 366 (94..461) | 307 | 40 | 45 (57), 37 (41), 82 (38), 64 (34), 53 (32), 49 (20), 88 (17), 41 (15), 77 (14), 42 (11), 46 (10), 47 (5), +4 more |
| 79098 | 360 (97..467) | 320 | 31 | 64 (69), 198 (60), 41 (25), 46 (25), 119 (25), 47 (24), 37 (23), 53 (20), 88 (13), 66 (9), 189 (9), 42 (6), +4 more |
| 79102 | 371 (98..477) | 325 | 29 | 64 (93), 37 (47), 49 (39), 53 (31), 46 (17), 45 (16), 189 (15), 41 (13), 104 (12), 88 (11), 77 (8), 119 (7), +5 more |
| 79103 | 380 (99..481) | 332 | 36 | 41 (53), 64 (49), 72 (41), 189 (39), 46 (32), 53 (31), 49 (20), 119 (19), 104 (17), 37 (16), 47 (6), 88 (5), +3 more |
| 79105 | 379 (101..484) | 324 | 39 | 53 (64), 119 (53), 64 (39), 104 (37), 37 (34), 49 (24), 72 (20), 41 (13), 122 (10), 47 (8), 46 (8), 88 (4), +5 more |
| 79108 | 385 (104..492) | 345 | 32 | 49 (51), 72 (35), 53 (31), 189 (30), 64 (29), 122 (29), 37 (28), 160 (21), 119 (20), 46 (19), 77 (17), 102 (15), +5 more |
| 79110 | 388 (106..497) | 343 | 34 | 122 (67), 53 (55), 77 (42), 49 (37), 37 (26), 72 (25), 144 (22), 64 (15), 42 (12), 47 (12), 160 (12), 104 (6), +5 more |
| 79111 | 386 (109..500) | 342 | 36 | 160 (71), 122 (70), 144 (52), 66 (22), 53 (22), 72 (21), 102 (19), 77 (17), 47 (12), 71 (11), 42 (10), 69 (6), +3 more |
| 79115 | 421 (111..531) | 376 | 31 | 104 (81), 144 (55), 47 (51), 122 (40), 53 (38), 71 (28), 66 (21), 77 (20), 160 (15), 42 (14), 102 (7), 83 (3), +2 more |
| 79116 | 411 (114..530) | 377 | 25 | 144 (88), 66 (61), 71 (49), 47 (41), 168 (29), 102 (25), 83 (19), 104 (16), 42 (13), 53 (7), 122 (7), 77 (6), +4 more |
| 79122 | 404 (118..532) | 371 | 26 | 47 (69), 66 (63), 42 (61), 71 (56), 144 (36), 122 (26), 53 (18), 83 (17), 104 (15), 72 (4), 69 (4), 160 (1), +1 more |
| 79132 | 391 (120..515) | 347 | 35 | 66 (144), 160 (68), 71 (41), 42 (35), 122 (19), 83 (13), 104 (10), 72 (5), 144 (5), 47 (4), 69 (3) |
| 79128 | 402 (124..527) | 361 | 28 | 71 (160), 66 (76), 47 (45), 42 (23), 122 (16), 69 (15), 104 (15), 83 (6), 72 (3), 160 (2) |
| 79134 | 407 (127..533) | 366 | 29 | 179 (128), 69 (68), 104 (40), 83 (39), 42 (34), 71 (30), 168 (10), 72 (7), 66 (4), 160 (3), 47 (2), 122 (1) |
| 79135 | 409 (129..542) | 370 | 26 | 69 (129), 168 (86), 83 (55), 42 (48), 179 (47), 72 (4), 47 (1) |
| 79139 | 406 (132..537) | 369 | 27 | 83 (215), 47 (47), 168 (39), 100 (25), 69 (16), 42 (9), 104 (6), 179 (5), 71 (4), 72 (3) |
| 79136 | 393 (136..538) | 364 | 25 | 69 (154), 72 (85), 47 (65), 168 (23), 104 (20), 83 (17) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 129 | 217..246 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 30/301/1007; tracks with internal gaps: 33; total internal gaps: 354; longest internal gap: 16; tracks ending in coasting: 34 (trailing rows total 1210)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 972 | 35 | 29 | 2 | 0 | 78911 |
| 37 | 82..483 | 402 | 402 | 355 | 47 | 13 | 3 | 28 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 41 | 86..472 | 387 | 387 | 337 | 50 | 14 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 88..474 | 387 | 387 | 344 | 43 | 13 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 43 | 88..377 | 290 | 290 | 194 | 96 | 8 | 2 | 87 | 78896, 78969, 78971, 79037, 79045 |
| 45 | 92..513 | 422 | 422 | 362 | 60 | 18 | 6 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79105 |
| 46 | 92..374 | 283 | 283 | 239 | 44 | 14 | 1 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..560 | 468 | 468 | 410 | 58 | 21 | 5 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 96..526 | 431 | 431 | 388 | 43 | 12 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 100..509 | 410 | 410 | 360 | 50 | 19 | 2 | 30 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 64 | 106..510 | 405 | 405 | 357 | 48 | 13 | 7 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 66 | 107..556 | 450 | 450 | 406 | 44 | 12 | 1 | 32 | 78899, 79097, 79098, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 111..565 | 455 | 455 | 404 | 51 | 19 | 3 | 28 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 111..210 | 100 | 100 | 62 | 38 | 1 | 1 | 37 | 78896, 78969, 78971, 79045 |
| 71 | 111..562 | 452 | 452 | 405 | 47 | 12 | 2 | 31 | 78897, 78899, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 72 | 113..481 | 369 | 369 | 288 | 81 | 19 | 4 | 51 | 78899, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 119..458 | 340 | 340 | 278 | 62 | 16 | 10 | 24 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 82 | 129..299 | 171 | 171 | 118 | 53 | 3 | 16 | 35 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 130..566 | 437 | 437 | 387 | 50 | 12 | 6 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 88 | 137..421 | 285 | 285 | 174 | 111 | 7 | 2 | 102 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 93 | 144..253 | 110 | 110 | 68 | 42 | 3 | 1 | 39 | 78896, 78969, 78971 |
| 100 | 151..205 | 55 | 55 | 25 | 30 | 0 | 0 | 30 | 79139 |
| 102 | 155..254 | 100 | 100 | 69 | 31 | 1 | 1 | 30 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 104 | 159..482 | 324 | 324 | 286 | 38 | 4 | 5 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 109 | 181..402 | 222 | 222 | 182 | 40 | 8 | 2 | 30 | 78896, 78897, 78969, 78971, 79037, 79045, 79097 |
| 119 | 201..479 | 279 | 279 | 230 | 49 | 15 | 3 | 29 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108 |
| 122 | 201..598 | 398 | 398 | 286 | 112 | 12 | 3 | 98 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 129 | 217..246 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 144 | 261..561 | 301 | 301 | 260 | 41 | 7 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 160 | 312..544 | 233 | 233 | 201 | 32 | 8 | 10 | 11 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 168 | 335..558 | 224 | 224 | 188 | 36 | 10 | 4 | 21 | 79116, 79122, 79134, 79135, 79136, 79139 |
| 179 | 354..571 | 218 | 218 | 181 | 37 | 4 | 5 | 29 | 79116, 79134, 79135, 79139 |
| 186 | 374..468 | 95 | 95 | 62 | 33 | 3 | 2 | 29 | 78971, 79045 |
| 189 | 383..521 | 139 | 139 | 107 | 32 | 3 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79108 |
| 198 | 402..496 | 95 | 95 | 65 | 30 | 1 | 1 | 29 | 79097, 79098 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 35; matched pairs: 9050; unmatched reference entries: 1092; unmatched candidate entries: 1724
- identity switches: 1080; fragmentation (coverage interruptions): 787; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 41 -> 42 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 42 -> 43 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 41 -> 42 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 42 -> 43 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 43 -> 46 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 37 -> 45 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 43 -> 37 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 43 -> 47 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78896: 46 -> 43 at (2047.5, 3031), 1 frames after previous cover
- f94: ref 78897: 42 -> 47 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 41 -> 42 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 78969: 45 -> 46 at (2071, 3031), 1 frames after previous cover
- f94: ref 78971: 37 -> 45 at (2090.5, 3032.5), 3 frames after previous cover
- f96: ref 79037: 47 -> 49 at (2099, 3033.5), 3 frames after previous cover
- f97: ref 78897: 47 -> 37 at (2107, 3033), 2 frames after previous cover
- f97: ref 78899: 42 -> 47 at (2123, 3030), 1 frames after previous cover
- f97: ref 78971: 45 -> 46 at (2072, 3034.5), 1 frames after previous cover
- f97: ref 79045: 37 -> 45 at (2081.5, 3032), 1 frames after previous cover
- f97: ref 79097: 41 -> 42 at (2135, 3028), 1 frames after previous cover
- f98: ref 78971: 46 -> 45 at (2066, 3034), 1 frames after previous cover
- f98: ref 79097: 42 -> 47 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 41 -> 42 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 37 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 47 -> 37 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 49 -> 45 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 45 -> 46 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79098: 42 -> 47 at (2135.5, 3025.5), 1 frames after previous cover
- f99: ref 79102: 41 -> 42 at (2147.5, 3026.5), 1 frames after previous cover
- f100: ref 78897: 49 -> 47 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 46 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 45 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 47 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 47 -> 42 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 47 -> 49 at (2083, 3033.5), 1 frames after previous cover
- f101: ref 79037: 49 -> 46 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79045: 46 -> 45 at (2054.5, 3031.5), 1 frames after previous cover
- f101: ref 79097: 53 -> 47 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 42 -> 53 at (2124, 3028), 1 frames after previous cover
- f104: ref 79097: 47 -> 37 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 53 -> 47 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 42 -> 53 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 41 -> 42 at (2126, 3022.5), 4 frames after previous cover
- f106: ref 78969: 43 -> 45 at (1997.5, 3033), 3 frames after previous cover
- f106: ref 79045: 45 -> 64 at (2023.5, 3033.5), 4 frames after previous cover
- f106: ref 79098: 47 -> 37 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 42 -> 53 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 41 -> 47 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 37 -> 66 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 45 -> 46 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 46 -> 49 at (2031, 3033.5), 1 frames after previous cover
- f108: ref 78899: 66 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78969: 45 -> 43 at (1984.5, 3035), 1 frames after previous cover
- f108: ref 78971: 46 -> 45 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 1 frames after previous cover
- f108: ref 79097: 37 -> 66 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 53 -> 41 at (2096.5, 3027.5), 3 frames after previous cover
- f109: ref 79108: 41 -> 47 at (2125, 3025), 2 frames after previous cover
- f110: ref 79105: 47 -> 53 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 78896: 43 -> 70 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 49 -> 71 at (2021.5, 3032.5), 5 frames after previous cover
- ... 1020 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 972 | 29 | 0 (972) |
| 78896 | 350 (76..429) | 293 | 26 | 43 (104), 77 (82), 46 (46), 109 (34), 70 (24), 93 (3) |
| 78969 | 352 (80..434) | 310 | 31 | 109 (87), 43 (79), 41 (58), 45 (26), 77 (25), 93 (23), 46 (5), 37 (4), 70 (3) |
| 78971 | 352 (84..439) | 307 | 34 | 45 (65), 186 (61), 93 (42), 109 (34), 70 (27), 41 (25), 46 (23), 82 (8), 77 (8), 37 (6), 43 (6), 88 (2) |
| 79045 | 355 (84..443) | 305 | 37 | 45 (96), 119 (48), 64 (23), 49 (21), 41 (21), 88 (19), 82 (18), 46 (17), 109 (14), 77 (10), 70 (8), 37 (5), +3 more |
| 79037 | 355 (86..445) | 315 | 28 | 49 (83), 45 (77), 42 (45), 46 (27), 82 (26), 88 (19), 119 (18), 41 (12), 109 (4), 43 (2), 47 (1), 64 (1) |
| 78897 | 345 (89..450) | 289 | 37 | 49 (60), 37 (46), 88 (35), 119 (29), 41 (25), 82 (16), 77 (13), 71 (12), 42 (10), 45 (10), 46 (9), 189 (9), +4 more |
| 78899 | 365 (91..455) | 320 | 36 | 37 (76), 41 (75), 88 (45), 49 (30), 72 (29), 45 (11), 77 (11), 119 (11), 53 (8), 82 (7), 42 (6), 64 (4), +5 more |
| 79097 | 366 (94..461) | 307 | 40 | 45 (57), 37 (41), 82 (38), 64 (34), 53 (32), 49 (20), 88 (17), 41 (15), 77 (14), 42 (11), 46 (10), 47 (5), +4 more |
| 79098 | 360 (97..467) | 320 | 31 | 64 (69), 198 (60), 41 (25), 46 (25), 119 (25), 47 (24), 37 (23), 53 (20), 88 (13), 66 (9), 189 (9), 42 (6), +4 more |
| 79102 | 371 (98..477) | 325 | 29 | 64 (93), 37 (47), 49 (39), 53 (31), 46 (17), 45 (16), 189 (15), 41 (13), 104 (12), 88 (11), 77 (8), 119 (7), +5 more |
| 79103 | 380 (99..481) | 332 | 36 | 41 (53), 64 (49), 72 (41), 189 (39), 46 (32), 53 (31), 49 (20), 119 (19), 104 (17), 37 (16), 47 (6), 88 (5), +3 more |
| 79105 | 379 (101..484) | 324 | 39 | 53 (64), 119 (53), 64 (39), 104 (37), 37 (34), 49 (24), 72 (20), 41 (13), 122 (10), 47 (8), 46 (8), 88 (4), +5 more |
| 79108 | 385 (104..492) | 345 | 32 | 49 (51), 72 (35), 53 (31), 189 (30), 64 (29), 122 (29), 37 (28), 160 (21), 119 (20), 46 (19), 77 (17), 102 (15), +5 more |
| 79110 | 388 (106..497) | 343 | 34 | 122 (67), 53 (55), 77 (42), 49 (37), 37 (26), 72 (25), 144 (22), 64 (15), 42 (12), 47 (12), 160 (12), 104 (6), +5 more |
| 79111 | 386 (109..500) | 342 | 36 | 160 (71), 122 (70), 144 (52), 66 (22), 53 (22), 72 (21), 102 (19), 77 (17), 47 (12), 71 (11), 42 (10), 69 (6), +3 more |
| 79115 | 421 (111..531) | 376 | 31 | 104 (81), 144 (55), 47 (51), 122 (40), 53 (38), 71 (28), 66 (21), 77 (20), 160 (15), 42 (14), 102 (7), 83 (3), +2 more |
| 79116 | 411 (114..530) | 377 | 25 | 144 (88), 66 (61), 71 (49), 47 (41), 168 (29), 102 (25), 83 (19), 104 (16), 42 (13), 53 (7), 122 (7), 77 (6), +4 more |
| 79122 | 404 (118..532) | 371 | 26 | 47 (69), 66 (63), 42 (61), 71 (56), 144 (36), 122 (26), 53 (18), 83 (17), 104 (15), 72 (4), 69 (4), 160 (1), +1 more |
| 79132 | 391 (120..515) | 347 | 35 | 66 (144), 160 (68), 71 (41), 42 (35), 122 (19), 83 (13), 104 (10), 72 (5), 144 (5), 47 (4), 69 (3) |
| 79128 | 402 (124..527) | 361 | 28 | 71 (160), 66 (76), 47 (45), 42 (23), 122 (16), 69 (15), 104 (15), 83 (6), 72 (3), 160 (2) |
| 79134 | 407 (127..533) | 366 | 29 | 179 (128), 69 (68), 104 (40), 83 (39), 42 (34), 71 (30), 168 (10), 72 (7), 66 (4), 160 (3), 47 (2), 122 (1) |
| 79135 | 409 (129..542) | 370 | 26 | 69 (129), 168 (86), 83 (55), 42 (48), 179 (47), 72 (4), 47 (1) |
| 79139 | 406 (132..537) | 369 | 27 | 83 (215), 47 (47), 168 (39), 100 (25), 69 (16), 42 (9), 104 (6), 179 (5), 71 (4), 72 (3) |
| 79136 | 393 (136..538) | 364 | 25 | 69 (154), 72 (85), 47 (65), 168 (23), 104 (20), 83 (17) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 129 | 217..246 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 30/301/1007; tracks with internal gaps: 33; total internal gaps: 354; longest internal gap: 16; tracks ending in coasting: 34 (trailing rows total 1210)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 972 | 35 | 29 | 2 | 0 | 78911 |
| 37 | 82..483 | 402 | 402 | 355 | 47 | 13 | 3 | 28 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 41 | 86..472 | 387 | 387 | 337 | 50 | 14 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 42 | 88..474 | 387 | 387 | 344 | 43 | 13 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 43 | 88..377 | 290 | 290 | 194 | 96 | 8 | 2 | 87 | 78896, 78969, 78971, 79037, 79045 |
| 45 | 92..513 | 422 | 422 | 362 | 60 | 18 | 6 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79105 |
| 46 | 92..374 | 283 | 283 | 239 | 44 | 14 | 1 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 47 | 93..560 | 468 | 468 | 410 | 58 | 21 | 5 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 96..526 | 431 | 431 | 388 | 43 | 12 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 100..509 | 410 | 410 | 360 | 50 | 19 | 2 | 30 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 64 | 106..510 | 405 | 405 | 357 | 48 | 13 | 7 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 66 | 107..556 | 450 | 450 | 406 | 44 | 12 | 1 | 32 | 78899, 79097, 79098, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 69 | 111..565 | 455 | 455 | 404 | 51 | 19 | 3 | 28 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 111..210 | 100 | 100 | 62 | 38 | 1 | 1 | 37 | 78896, 78969, 78971, 79045 |
| 71 | 111..562 | 452 | 452 | 405 | 47 | 12 | 2 | 31 | 78897, 78899, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 72 | 113..481 | 369 | 369 | 288 | 81 | 19 | 4 | 51 | 78899, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 77 | 119..458 | 340 | 340 | 278 | 62 | 16 | 10 | 24 | 78896, 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 82 | 129..299 | 171 | 171 | 118 | 53 | 3 | 16 | 35 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 83 | 130..566 | 437 | 437 | 387 | 50 | 12 | 6 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 88 | 137..421 | 285 | 285 | 174 | 111 | 7 | 2 | 102 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 93 | 144..253 | 110 | 110 | 68 | 42 | 3 | 1 | 39 | 78896, 78969, 78971 |
| 100 | 151..205 | 55 | 55 | 25 | 30 | 0 | 0 | 30 | 79139 |
| 102 | 155..254 | 100 | 100 | 69 | 31 | 1 | 1 | 30 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 104 | 159..482 | 324 | 324 | 286 | 38 | 4 | 5 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 109 | 181..402 | 222 | 222 | 182 | 40 | 8 | 2 | 30 | 78896, 78897, 78969, 78971, 79037, 79045, 79097 |
| 119 | 201..479 | 279 | 279 | 230 | 49 | 15 | 3 | 29 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108 |
| 122 | 201..598 | 398 | 398 | 286 | 112 | 12 | 3 | 98 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 129 | 217..246 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 144 | 261..561 | 301 | 301 | 260 | 41 | 7 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 160 | 312..544 | 233 | 233 | 201 | 32 | 8 | 10 | 11 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 168 | 335..558 | 224 | 224 | 188 | 36 | 10 | 4 | 21 | 79116, 79122, 79134, 79135, 79136, 79139 |
| 179 | 354..571 | 218 | 218 | 181 | 37 | 4 | 5 | 29 | 79116, 79134, 79135, 79139 |
| 186 | 374..468 | 95 | 95 | 62 | 33 | 3 | 2 | 29 | 78971, 79045 |
| 189 | 383..521 | 139 | 139 | 107 | 32 | 3 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79108 |
| 198 | 402..496 | 95 | 95 | 65 | 30 | 1 | 1 | 29 | 79097, 79098 |
