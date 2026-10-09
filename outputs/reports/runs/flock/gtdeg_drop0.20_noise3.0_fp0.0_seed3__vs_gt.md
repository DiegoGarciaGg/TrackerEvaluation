# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=dcc9cc165454
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise3.0_fp0.0_seed3/tracks.csv sha256=c4016e10ecae7705
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise3.0_fp0.0_seed3.csv sha256=dcc9cc1654543757
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise3.0_fp0.0_seed3
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
| observations | none | 4 | 10142 | 8084 | 0.199 | 0.362 | 0.110 | 2.18 | 0.198 | 0.060 | 2.39 | 812 | 2529.0 | 0.262 | 0.296 | 0.236 | 0.469 | 0.588 | 4753 | 5389 | 3331 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 8084 | 0.275 | 0.501 | 0.151 | 2.73 | 0.334 | 0.489 | 3.20 | 1027 | 2134.0 | 0.384 | 0.432 | 0.345 | 0.694 | 0.870 | 7037 | 3105 | 1047 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 8084 | 0.316 | 0.567 | 0.176 | 3.06 | 0.395 | 0.640 | 3.60 | 1076 | 1771.0 | 0.434 | 0.489 | 0.390 | 0.772 | 0.968 | 7826 | 2316 | 258 | 4 | 21 | 0 |
| observations | none | 12 | 10142 | 8084 | 0.359 | 0.614 | 0.210 | 3.62 | 0.418 | 0.689 | 3.94 | 936 | 1614.0 | 0.464 | 0.523 | 0.417 | 0.789 | 0.990 | 8004 | 2138 | 80 | 12 | 13 | 0 |
| observations | ignore | 4 | 10142 | 8084 | 0.199 | 0.362 | 0.110 | 2.18 | 0.198 | 0.060 | 2.39 | 812 | 2529.0 | 0.262 | 0.296 | 0.236 | 0.469 | 0.588 | 4753 | 5389 | 3331 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 8084 | 0.275 | 0.501 | 0.151 | 2.73 | 0.334 | 0.489 | 3.20 | 1027 | 2134.0 | 0.384 | 0.432 | 0.345 | 0.694 | 0.870 | 7037 | 3105 | 1047 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 8084 | 0.316 | 0.567 | 0.176 | 3.06 | 0.395 | 0.640 | 3.60 | 1076 | 1771.0 | 0.434 | 0.489 | 0.390 | 0.772 | 0.968 | 7826 | 2316 | 258 | 4 | 21 | 0 |
| observations | ignore | 12 | 10142 | 8084 | 0.359 | 0.614 | 0.210 | 3.62 | 0.418 | 0.689 | 3.94 | 936 | 1614.0 | 0.464 | 0.523 | 0.417 | 0.789 | 0.990 | 8004 | 2138 | 80 | 12 | 13 | 0 |
| updates | none | 4 | 10142 | 10372 | 0.198 | 0.345 | 0.114 | 2.21 | 0.192 | -0.105 | 2.41 | 876 | 2483.0 | 0.255 | 0.252 | 0.257 | 0.502 | 0.491 | 5093 | 5049 | 5279 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10372 | 0.285 | 0.495 | 0.164 | 2.84 | 0.333 | 0.386 | 3.25 | 1098 | 1777.0 | 0.382 | 0.378 | 0.387 | 0.759 | 0.742 | 7693 | 2449 | 2679 | 1 | 24 | 0 |
| updates | none | 8 | 10142 | 10372 | 0.336 | 0.575 | 0.196 | 3.24 | 0.412 | 0.601 | 3.75 | 1098 | 1090.0 | 0.447 | 0.442 | 0.452 | 0.866 | 0.847 | 8783 | 1359 | 1589 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10372 | 0.392 | 0.646 | 0.239 | 3.90 | 0.461 | 0.718 | 4.30 | 926 | 664.0 | 0.495 | 0.489 | 0.500 | 0.916 | 0.896 | 9291 | 851 | 1081 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10372 | 0.198 | 0.345 | 0.114 | 2.21 | 0.192 | -0.105 | 2.41 | 876 | 2483.0 | 0.255 | 0.252 | 0.257 | 0.502 | 0.491 | 5093 | 5049 | 5279 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10372 | 0.285 | 0.495 | 0.164 | 2.84 | 0.333 | 0.386 | 3.25 | 1098 | 1777.0 | 0.382 | 0.378 | 0.387 | 0.759 | 0.742 | 7693 | 2449 | 2679 | 1 | 24 | 0 |
| updates | ignore | 8 | 10142 | 10372 | 0.336 | 0.575 | 0.196 | 3.24 | 0.412 | 0.601 | 3.75 | 1098 | 1090.0 | 0.447 | 0.442 | 0.452 | 0.866 | 0.847 | 8783 | 1359 | 1589 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10372 | 0.392 | 0.646 | 0.239 | 3.90 | 0.461 | 0.718 | 4.30 | 926 | 664.0 | 0.495 | 0.489 | 0.500 | 0.916 | 0.896 | 9291 | 851 | 1081 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 7826; unmatched reference entries: 2316; unmatched candidate entries: 258
- identity switches: 1076; fragmentation (coverage interruptions): 1777; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 4 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 2 -> 8 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78897: 7 -> 9 at (2125, 3030), 2 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 4 -> 7 at (2100.5, 3033), 2 frames after previous cover
- f95: ref 78897: 9 -> 6 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 7 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 7 -> 4 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 9 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 6 -> 8 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 6 -> 10 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 4 -> 2 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 6 -> 4 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 9 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 8 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 8 -> 10 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 10 -> 4 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 10 -> 8 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 4 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 8 -> 12 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 6 -> 10 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 6 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 9 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 12 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 4 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 7 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 9 -> 7 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 2 -> 12 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 12 -> 2 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 9 -> 7 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 12 -> 11 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 4 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 12 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79103: 7 -> 6 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 4 -> 2 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 10 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 6 -> 10 at (2096.5, 3027.5), 2 frames after previous cover
- f108: ref 79105: 7 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 8 -> 4 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 13 -> 7 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 8 -> 4 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 2 -> 12 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 4 -> 8 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 8 -> 6 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 6 -> 8 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 6 -> 10 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 7 -> 9 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 13 -> 7 at (2129, 3027), 3 frames after previous cover
- ... 1016 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 779 | 180 | 1 (779) |
| 78896 | 350 (76..429) | 268 | 61 | 27 (181), 19 (46), 22 (14), 14 (11), 2 (7), 8 (6), 11 (3) |
| 78969 | 352 (80..434) | 245 | 73 | 19 (175), 27 (39), 2 (11), 14 (8), 25 (4), 12 (2), 11 (2), 4 (1), 22 (1), 26 (1), 21 (1) |
| 78971 | 352 (84..439) | 273 | 64 | 22 (99), 21 (78), 12 (47), 19 (15), 4 (8), 2 (7), 14 (6), 11 (5), 27 (4), 25 (3), 26 (1) |
| 79045 | 355 (84..443) | 270 | 61 | 21 (77), 12 (72), 25 (50), 14 (26), 22 (20), 19 (8), 11 (5), 4 (3), 8 (3), 6 (2), 26 (2), 7 (1), +1 more |
| 79037 | 355 (86..445) | 267 | 65 | 22 (112), 25 (35), 14 (34), 26 (33), 21 (11), 12 (10), 4 (6), 11 (6), 19 (5), 6 (4), 2 (4), 28 (4), +1 more |
| 78897 | 345 (89..450) | 257 | 65 | 28 (110), 14 (54), 25 (33), 12 (19), 2 (9), 26 (9), 21 (5), 4 (4), 11 (4), 7 (2), 6 (2), 22 (2), +4 more |
| 78899 | 365 (91..455) | 278 | 68 | 2 (111), 12 (80), 14 (37), 26 (16), 28 (14), 8 (4), 9 (3), 21 (3), 7 (2), 10 (2), 11 (2), 6 (1), +3 more |
| 79097 | 366 (94..461) | 284 | 70 | 26 (154), 2 (46), 12 (34), 21 (8), 14 (7), 11 (6), 20 (5), 25 (5), 6 (4), 10 (4), 28 (4), 9 (2), +3 more |
| 79098 | 360 (97..467) | 289 | 55 | 11 (111), 21 (37), 26 (33), 2 (27), 14 (26), 28 (19), 20 (7), 12 (7), 25 (7), 7 (4), 8 (4), 6 (2), +3 more |
| 79102 | 371 (98..477) | 279 | 69 | 14 (82), 11 (62), 28 (31), 25 (27), 8 (18), 2 (13), 26 (10), 4 (6), 21 (6), 6 (5), 20 (5), 9 (4), +5 more |
| 79103 | 380 (99..481) | 304 | 60 | 4 (119), 8 (53), 2 (31), 11 (24), 28 (22), 21 (21), 25 (10), 6 (7), 12 (4), 9 (3), 26 (3), 20 (2), +4 more |
| 79105 | 379 (101..484) | 288 | 71 | 25 (113), 2 (49), 11 (34), 8 (18), 28 (17), 13 (12), 21 (11), 4 (10), 9 (7), 6 (6), 7 (3), 20 (3), +3 more |
| 79108 | 385 (104..492) | 309 | 65 | 20 (127), 4 (45), 13 (36), 8 (27), 11 (23), 9 (14), 28 (12), 2 (8), 23 (4), 25 (4), 7 (3), 10 (2), +3 more |
| 79110 | 388 (106..497) | 318 | 56 | 8 (137), 4 (53), 24 (36), 13 (23), 11 (22), 23 (18), 9 (10), 20 (8), 6 (4), 10 (3), 7 (2), 17 (2) |
| 79111 | 386 (109..500) | 291 | 73 | 17 (118), 13 (45), 20 (30), 8 (25), 23 (21), 24 (21), 4 (12), 9 (11), 10 (3), 6 (3), 28 (1), 11 (1) |
| 79115 | 421 (111..531) | 323 | 78 | 9 (175), 13 (38), 20 (24), 17 (20), 23 (18), 4 (14), 24 (12), 8 (11), 7 (5), 10 (4), 6 (2) |
| 79116 | 411 (114..530) | 312 | 71 | 13 (150), 23 (47), 17 (35), 20 (29), 9 (16), 4 (14), 24 (10), 7 (3), 10 (3), 8 (3), 6 (1), 29 (1) |
| 79122 | 404 (118..532) | 296 | 75 | 23 (161), 9 (26), 17 (23), 4 (23), 13 (19), 20 (16), 8 (9), 6 (6), 24 (6), 29 (3), 10 (2), 7 (1), +1 more |
| 79132 | 391 (120..515) | 307 | 68 | 29 (117), 23 (43), 20 (35), 17 (29), 6 (24), 9 (24), 13 (15), 4 (11), 7 (3), 8 (3), 24 (3) |
| 79128 | 402 (124..527) | 326 | 67 | 7 (133), 29 (68), 9 (43), 24 (20), 6 (17), 17 (14), 8 (13), 20 (13), 13 (3), 10 (2) |
| 79134 | 407 (127..533) | 310 | 74 | 24 (137), 17 (57), 7 (38), 30 (31), 6 (30), 8 (8), 9 (6), 10 (3) |
| 79135 | 409 (129..542) | 324 | 61 | 6 (171), 7 (60), 17 (33), 24 (33), 9 (19), 30 (6), 8 (2) |
| 79139 | 406 (132..537) | 322 | 63 | 10 (118), 6 (91), 7 (71), 24 (27), 30 (9), 17 (6) |
| 79136 | 393 (136..538) | 307 | 64 | 10 (205), 30 (74), 24 (15), 7 (11), 6 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 164/378/1004; tracks with internal gaps: 25; total internal gaps: 248; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 809 | 779 | 30 | 29 | 2 | 0 | 78911 |
| 2 | 78..455 | 378 | 332 | 324 | 8 | 8 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 4 | 84..481 | 398 | 347 | 334 | 13 | 13 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 88..542 | 455 | 396 | 385 | 11 | 11 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 88..527 | 440 | 357 | 349 | 8 | 8 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..497 | 409 | 359 | 347 | 12 | 11 | 2 | 0 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 9 | 91..531 | 441 | 380 | 365 | 15 | 13 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 10 | 98..538 | 441 | 374 | 360 | 14 | 14 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 11 | 101..466 | 366 | 319 | 310 | 9 | 9 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..444 | 344 | 286 | 278 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 106..530 | 425 | 352 | 342 | 10 | 10 | 1 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 107..477 | 371 | 303 | 292 | 11 | 10 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 17 | 111..500 | 390 | 344 | 337 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 112..439 | 328 | 261 | 250 | 11 | 11 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 115..492 | 378 | 319 | 305 | 14 | 10 | 3 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 115..434 | 320 | 264 | 259 | 5 | 5 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 22 | 123..442 | 320 | 258 | 248 | 10 | 10 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 23 | 130..531 | 402 | 329 | 314 | 15 | 14 | 2 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 24 | 131..537 | 407 | 333 | 326 | 7 | 7 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 25 | 133..484 | 352 | 297 | 292 | 5 | 5 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 140..461 | 322 | 269 | 262 | 7 | 7 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 27 | 146..429 | 284 | 228 | 224 | 4 | 4 | 1 | 0 | 78896, 78969, 78971 |
| 28 | 158..449 | 292 | 239 | 235 | 4 | 4 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79122 |
| 29 | 271..515 | 245 | 201 | 189 | 12 | 12 | 1 | 0 | 79116, 79122, 79128, 79132 |
| 30 | 370..533 | 164 | 128 | 120 | 8 | 8 | 1 | 0 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 7826; unmatched reference entries: 2316; unmatched candidate entries: 258
- identity switches: 1076; fragmentation (coverage interruptions): 1777; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 4 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 2 -> 8 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78897: 7 -> 9 at (2125, 3030), 2 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 4 -> 7 at (2100.5, 3033), 2 frames after previous cover
- f95: ref 78897: 9 -> 6 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 7 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 7 -> 4 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 9 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 6 -> 8 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 6 -> 10 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 4 -> 2 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 6 -> 4 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 9 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 8 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 8 -> 10 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 10 -> 4 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 10 -> 8 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 4 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 8 -> 12 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 6 -> 10 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 6 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 9 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 12 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 4 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 7 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 9 -> 7 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 2 -> 12 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 12 -> 2 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 9 -> 7 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 12 -> 11 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 4 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 12 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79103: 7 -> 6 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 4 -> 2 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 10 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 6 -> 10 at (2096.5, 3027.5), 2 frames after previous cover
- f108: ref 79105: 7 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 8 -> 4 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 13 -> 7 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 8 -> 4 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 2 -> 12 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 4 -> 8 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 8 -> 6 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 6 -> 8 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 6 -> 10 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 7 -> 9 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 13 -> 7 at (2129, 3027), 3 frames after previous cover
- ... 1016 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 779 | 180 | 1 (779) |
| 78896 | 350 (76..429) | 268 | 61 | 27 (181), 19 (46), 22 (14), 14 (11), 2 (7), 8 (6), 11 (3) |
| 78969 | 352 (80..434) | 245 | 73 | 19 (175), 27 (39), 2 (11), 14 (8), 25 (4), 12 (2), 11 (2), 4 (1), 22 (1), 26 (1), 21 (1) |
| 78971 | 352 (84..439) | 273 | 64 | 22 (99), 21 (78), 12 (47), 19 (15), 4 (8), 2 (7), 14 (6), 11 (5), 27 (4), 25 (3), 26 (1) |
| 79045 | 355 (84..443) | 270 | 61 | 21 (77), 12 (72), 25 (50), 14 (26), 22 (20), 19 (8), 11 (5), 4 (3), 8 (3), 6 (2), 26 (2), 7 (1), +1 more |
| 79037 | 355 (86..445) | 267 | 65 | 22 (112), 25 (35), 14 (34), 26 (33), 21 (11), 12 (10), 4 (6), 11 (6), 19 (5), 6 (4), 2 (4), 28 (4), +1 more |
| 78897 | 345 (89..450) | 257 | 65 | 28 (110), 14 (54), 25 (33), 12 (19), 2 (9), 26 (9), 21 (5), 4 (4), 11 (4), 7 (2), 6 (2), 22 (2), +4 more |
| 78899 | 365 (91..455) | 278 | 68 | 2 (111), 12 (80), 14 (37), 26 (16), 28 (14), 8 (4), 9 (3), 21 (3), 7 (2), 10 (2), 11 (2), 6 (1), +3 more |
| 79097 | 366 (94..461) | 284 | 70 | 26 (154), 2 (46), 12 (34), 21 (8), 14 (7), 11 (6), 20 (5), 25 (5), 6 (4), 10 (4), 28 (4), 9 (2), +3 more |
| 79098 | 360 (97..467) | 289 | 55 | 11 (111), 21 (37), 26 (33), 2 (27), 14 (26), 28 (19), 20 (7), 12 (7), 25 (7), 7 (4), 8 (4), 6 (2), +3 more |
| 79102 | 371 (98..477) | 279 | 69 | 14 (82), 11 (62), 28 (31), 25 (27), 8 (18), 2 (13), 26 (10), 4 (6), 21 (6), 6 (5), 20 (5), 9 (4), +5 more |
| 79103 | 380 (99..481) | 304 | 60 | 4 (119), 8 (53), 2 (31), 11 (24), 28 (22), 21 (21), 25 (10), 6 (7), 12 (4), 9 (3), 26 (3), 20 (2), +4 more |
| 79105 | 379 (101..484) | 288 | 71 | 25 (113), 2 (49), 11 (34), 8 (18), 28 (17), 13 (12), 21 (11), 4 (10), 9 (7), 6 (6), 7 (3), 20 (3), +3 more |
| 79108 | 385 (104..492) | 309 | 65 | 20 (127), 4 (45), 13 (36), 8 (27), 11 (23), 9 (14), 28 (12), 2 (8), 23 (4), 25 (4), 7 (3), 10 (2), +3 more |
| 79110 | 388 (106..497) | 318 | 56 | 8 (137), 4 (53), 24 (36), 13 (23), 11 (22), 23 (18), 9 (10), 20 (8), 6 (4), 10 (3), 7 (2), 17 (2) |
| 79111 | 386 (109..500) | 291 | 73 | 17 (118), 13 (45), 20 (30), 8 (25), 23 (21), 24 (21), 4 (12), 9 (11), 10 (3), 6 (3), 28 (1), 11 (1) |
| 79115 | 421 (111..531) | 323 | 78 | 9 (175), 13 (38), 20 (24), 17 (20), 23 (18), 4 (14), 24 (12), 8 (11), 7 (5), 10 (4), 6 (2) |
| 79116 | 411 (114..530) | 312 | 71 | 13 (150), 23 (47), 17 (35), 20 (29), 9 (16), 4 (14), 24 (10), 7 (3), 10 (3), 8 (3), 6 (1), 29 (1) |
| 79122 | 404 (118..532) | 296 | 75 | 23 (161), 9 (26), 17 (23), 4 (23), 13 (19), 20 (16), 8 (9), 6 (6), 24 (6), 29 (3), 10 (2), 7 (1), +1 more |
| 79132 | 391 (120..515) | 307 | 68 | 29 (117), 23 (43), 20 (35), 17 (29), 6 (24), 9 (24), 13 (15), 4 (11), 7 (3), 8 (3), 24 (3) |
| 79128 | 402 (124..527) | 326 | 67 | 7 (133), 29 (68), 9 (43), 24 (20), 6 (17), 17 (14), 8 (13), 20 (13), 13 (3), 10 (2) |
| 79134 | 407 (127..533) | 310 | 74 | 24 (137), 17 (57), 7 (38), 30 (31), 6 (30), 8 (8), 9 (6), 10 (3) |
| 79135 | 409 (129..542) | 324 | 61 | 6 (171), 7 (60), 17 (33), 24 (33), 9 (19), 30 (6), 8 (2) |
| 79139 | 406 (132..537) | 322 | 63 | 10 (118), 6 (91), 7 (71), 24 (27), 30 (9), 17 (6) |
| 79136 | 393 (136..538) | 307 | 64 | 10 (205), 30 (74), 24 (15), 7 (11), 6 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 164/378/1004; tracks with internal gaps: 25; total internal gaps: 248; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 809 | 779 | 30 | 29 | 2 | 0 | 78911 |
| 2 | 78..455 | 378 | 332 | 324 | 8 | 8 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 4 | 84..481 | 398 | 347 | 334 | 13 | 13 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 88..542 | 455 | 396 | 385 | 11 | 11 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 7 | 88..527 | 440 | 357 | 349 | 8 | 8 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..497 | 409 | 359 | 347 | 12 | 11 | 2 | 0 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 9 | 91..531 | 441 | 380 | 365 | 15 | 13 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 10 | 98..538 | 441 | 374 | 360 | 14 | 14 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 11 | 101..466 | 366 | 319 | 310 | 9 | 9 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..444 | 344 | 286 | 278 | 8 | 8 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 106..530 | 425 | 352 | 342 | 10 | 10 | 1 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 107..477 | 371 | 303 | 292 | 11 | 10 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 17 | 111..500 | 390 | 344 | 337 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 112..439 | 328 | 261 | 250 | 11 | 11 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 115..492 | 378 | 319 | 305 | 14 | 10 | 3 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 115..434 | 320 | 264 | 259 | 5 | 5 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 22 | 123..442 | 320 | 258 | 248 | 10 | 10 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 23 | 130..531 | 402 | 329 | 314 | 15 | 14 | 2 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 24 | 131..537 | 407 | 333 | 326 | 7 | 7 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 25 | 133..484 | 352 | 297 | 292 | 5 | 5 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 140..461 | 322 | 269 | 262 | 7 | 7 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 27 | 146..429 | 284 | 228 | 224 | 4 | 4 | 1 | 0 | 78896, 78969, 78971 |
| 28 | 158..449 | 292 | 239 | 235 | 4 | 4 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79122 |
| 29 | 271..515 | 245 | 201 | 189 | 12 | 12 | 1 | 0 | 79116, 79122, 79128, 79132 |
| 30 | 370..533 | 164 | 128 | 120 | 8 | 8 | 1 | 0 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8783; unmatched reference entries: 1359; unmatched candidate entries: 1589
- identity switches: 1098; fragmentation (coverage interruptions): 1017; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 4 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 2 -> 8 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79045: 4 -> 2 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78897: 7 -> 9 at (2125, 3030), 1 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 2 -> 7 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 9 -> 6 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 7 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 7 -> 4 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 9 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 6 -> 8 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 6 -> 10 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 4 -> 2 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 6 -> 4 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 9 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 8 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 8 -> 10 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 10 -> 4 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 10 -> 8 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 4 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 8 -> 12 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 6 -> 10 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 6 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 9 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 12 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 4 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 7 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 9 -> 7 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 2 -> 12 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 12 -> 2 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 9 -> 7 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 12 -> 11 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 4 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 12 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79102: 6 -> 9 at (2101.5, 3029.5), 1 frames after previous cover
- f107: ref 79103: 7 -> 6 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 4 -> 2 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 10 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 9 -> 10 at (2096.5, 3027.5), 1 frames after previous cover
- f108: ref 79105: 7 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 8 -> 4 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 13 -> 7 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 8 -> 4 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 2 -> 12 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 4 -> 8 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 8 -> 6 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 6 -> 8 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 6 -> 10 at (2087.5, 3023.5), 2 frames after previous cover
- ... 1038 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 935 | 55 | 1 (935) |
| 78896 | 350 (76..429) | 303 | 34 | 27 (206), 19 (52), 22 (15), 14 (13), 2 (7), 8 (7), 11 (3) |
| 78969 | 352 (80..434) | 285 | 41 | 19 (206), 27 (48), 2 (11), 14 (9), 25 (4), 12 (2), 11 (2), 4 (1), 22 (1), 26 (1) |
| 78971 | 352 (84..439) | 302 | 41 | 22 (109), 21 (85), 12 (56), 19 (15), 4 (9), 2 (7), 11 (6), 14 (6), 25 (4), 27 (4), 26 (1) |
| 79045 | 355 (84..443) | 301 | 40 | 21 (87), 12 (83), 25 (53), 14 (26), 22 (24), 19 (9), 11 (5), 4 (3), 8 (3), 6 (2), 2 (2), 26 (2), +2 more |
| 79037 | 355 (86..445) | 304 | 36 | 22 (132), 26 (40), 14 (39), 25 (37), 21 (14), 12 (8), 4 (6), 11 (6), 19 (6), 28 (5), 6 (4), 2 (4), +1 more |
| 78897 | 345 (89..450) | 284 | 47 | 28 (128), 14 (55), 25 (34), 12 (21), 26 (10), 2 (9), 21 (6), 4 (4), 11 (4), 7 (3), 22 (3), 6 (2), +4 more |
| 78899 | 365 (91..455) | 303 | 47 | 2 (127), 12 (85), 14 (39), 26 (16), 28 (16), 8 (4), 9 (3), 21 (3), 7 (2), 10 (2), 11 (2), 6 (1), +3 more |
| 79097 | 366 (94..461) | 311 | 45 | 26 (175), 2 (51), 12 (34), 21 (8), 14 (7), 11 (6), 25 (6), 20 (5), 6 (4), 10 (4), 28 (4), 9 (2), +3 more |
| 79098 | 360 (97..467) | 315 | 39 | 11 (125), 21 (43), 26 (35), 14 (30), 2 (29), 28 (19), 20 (7), 25 (7), 12 (5), 7 (4), 8 (4), 6 (2), +3 more |
| 79102 | 371 (98..477) | 313 | 43 | 14 (100), 11 (65), 28 (38), 25 (30), 8 (19), 2 (13), 26 (10), 21 (8), 9 (5), 6 (5), 4 (5), 20 (5), +5 more |
| 79103 | 380 (99..481) | 334 | 38 | 4 (134), 8 (56), 2 (33), 28 (27), 11 (24), 21 (22), 25 (11), 6 (7), 12 (4), 14 (4), 9 (3), 26 (3), +4 more |
| 79105 | 379 (101..484) | 324 | 41 | 25 (134), 2 (51), 11 (36), 8 (23), 28 (18), 21 (13), 13 (13), 4 (11), 9 (7), 6 (6), 20 (4), 7 (3), +3 more |
| 79108 | 385 (104..492) | 340 | 36 | 20 (149), 4 (47), 13 (41), 8 (29), 11 (25), 9 (13), 28 (11), 2 (8), 23 (4), 25 (4), 7 (3), 10 (2), +3 more |
| 79110 | 388 (106..497) | 346 | 34 | 8 (150), 4 (55), 24 (42), 11 (25), 13 (23), 23 (18), 9 (10), 20 (9), 10 (4), 6 (4), 17 (3), 7 (2), +1 more |
| 79111 | 386 (109..500) | 322 | 48 | 17 (134), 13 (54), 20 (31), 8 (26), 23 (23), 24 (20), 4 (13), 9 (12), 6 (3), 11 (3), 10 (2), 28 (1) |
| 79115 | 421 (111..531) | 357 | 47 | 9 (198), 13 (45), 20 (24), 17 (22), 23 (20), 4 (15), 8 (12), 24 (10), 7 (5), 10 (4), 6 (2) |
| 79116 | 411 (114..530) | 351 | 45 | 13 (175), 23 (47), 17 (36), 20 (34), 9 (18), 4 (16), 24 (13), 8 (5), 7 (3), 10 (3), 6 (1) |
| 79122 | 404 (118..532) | 326 | 48 | 23 (181), 9 (32), 17 (24), 4 (24), 13 (20), 20 (15), 8 (10), 24 (7), 6 (6), 29 (3), 10 (2), 7 (1), +1 more |
| 79132 | 391 (120..515) | 347 | 35 | 29 (134), 23 (56), 20 (38), 17 (32), 6 (25), 9 (23), 13 (15), 4 (12), 8 (6), 7 (3), 24 (3) |
| 79128 | 402 (124..527) | 361 | 37 | 7 (156), 29 (78), 9 (45), 24 (20), 6 (17), 17 (14), 8 (13), 20 (13), 13 (3), 10 (2) |
| 79134 | 407 (127..533) | 359 | 38 | 24 (159), 17 (62), 7 (45), 30 (41), 6 (34), 8 (8), 9 (7), 10 (3) |
| 79135 | 409 (129..542) | 361 | 35 | 6 (186), 7 (70), 24 (41), 17 (34), 9 (21), 30 (7), 8 (2) |
| 79139 | 406 (132..537) | 353 | 33 | 6 (109), 10 (104), 7 (80), 24 (45), 30 (8), 17 (6), 9 (1) |
| 79136 | 393 (136..538) | 346 | 34 | 10 (244), 30 (84), 7 (18) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 193/407/1004; tracks with internal gaps: 25; total internal gaps: 696; longest internal gap: 8; tracks ending in coasting: 24 (trailing rows total 670)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 935 | 69 | 55 | 3 | 0 | 78911 |
| 2 | 78..484 | 407 | 407 | 353 | 54 | 24 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 84..510 | 427 | 427 | 360 | 67 | 27 | 4 | 32 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 88..571 | 484 | 484 | 421 | 63 | 21 | 7 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 7 | 88..556 | 469 | 469 | 406 | 63 | 32 | 8 | 18 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..526 | 438 | 438 | 380 | 58 | 26 | 2 | 29 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 9 | 91..560 | 470 | 470 | 402 | 68 | 27 | 4 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 10 | 98..567 | 470 | 470 | 386 | 84 | 37 | 5 | 32 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 11 | 101..495 | 395 | 395 | 337 | 58 | 24 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..473 | 373 | 373 | 301 | 72 | 33 | 4 | 31 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 106..559 | 454 | 454 | 390 | 64 | 27 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 107..506 | 400 | 400 | 328 | 72 | 39 | 2 | 25 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 17 | 111..529 | 419 | 419 | 367 | 52 | 17 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 112..468 | 357 | 357 | 289 | 68 | 31 | 3 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 115..521 | 407 | 407 | 337 | 70 | 26 | 5 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 115..463 | 349 | 349 | 290 | 59 | 21 | 4 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 22 | 123..471 | 349 | 349 | 284 | 65 | 32 | 4 | 26 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 23 | 130..560 | 431 | 431 | 351 | 80 | 36 | 5 | 28 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 24 | 131..566 | 436 | 436 | 366 | 70 | 29 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 25 | 133..513 | 381 | 381 | 325 | 56 | 25 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 140..490 | 351 | 351 | 293 | 58 | 22 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 27 | 146..458 | 313 | 313 | 259 | 54 | 25 | 8 | 15 | 78896, 78969, 78971, 79045 |
| 28 | 158..478 | 321 | 321 | 268 | 53 | 20 | 3 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79122 |
| 29 | 271..544 | 274 | 274 | 215 | 59 | 24 | 2 | 29 | 79122, 79128, 79132 |
| 30 | 370..562 | 193 | 193 | 140 | 53 | 16 | 3 | 29 | 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8783; unmatched reference entries: 1359; unmatched candidate entries: 1589
- identity switches: 1098; fragmentation (coverage interruptions): 1017; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 4 -> 6 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 2 -> 8 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79045: 4 -> 2 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78897: 7 -> 9 at (2125, 3030), 1 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 2 -> 7 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 9 -> 6 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 7 -> 6 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 7 -> 4 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 9 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 6 -> 8 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 6 -> 10 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 4 -> 2 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 6 -> 4 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 9 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 8 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 8 -> 10 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 10 -> 4 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 10 -> 8 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 4 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 8 -> 12 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 6 -> 10 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 6 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 9 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 12 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 4 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 7 -> 6 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 9 -> 7 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 2 -> 12 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 12 -> 2 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 9 -> 7 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 12 -> 11 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 4 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 12 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79102: 6 -> 9 at (2101.5, 3029.5), 1 frames after previous cover
- f107: ref 79103: 7 -> 6 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 4 -> 2 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 10 -> 8 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 9 -> 10 at (2096.5, 3027.5), 1 frames after previous cover
- f108: ref 79105: 7 -> 9 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 8 -> 4 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 13 -> 7 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 8 -> 4 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 2 -> 12 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 4 -> 8 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 8 -> 6 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 6 -> 8 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 6 -> 10 at (2087.5, 3023.5), 2 frames after previous cover
- ... 1038 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 935 | 55 | 1 (935) |
| 78896 | 350 (76..429) | 303 | 34 | 27 (206), 19 (52), 22 (15), 14 (13), 2 (7), 8 (7), 11 (3) |
| 78969 | 352 (80..434) | 285 | 41 | 19 (206), 27 (48), 2 (11), 14 (9), 25 (4), 12 (2), 11 (2), 4 (1), 22 (1), 26 (1) |
| 78971 | 352 (84..439) | 302 | 41 | 22 (109), 21 (85), 12 (56), 19 (15), 4 (9), 2 (7), 11 (6), 14 (6), 25 (4), 27 (4), 26 (1) |
| 79045 | 355 (84..443) | 301 | 40 | 21 (87), 12 (83), 25 (53), 14 (26), 22 (24), 19 (9), 11 (5), 4 (3), 8 (3), 6 (2), 2 (2), 26 (2), +2 more |
| 79037 | 355 (86..445) | 304 | 36 | 22 (132), 26 (40), 14 (39), 25 (37), 21 (14), 12 (8), 4 (6), 11 (6), 19 (6), 28 (5), 6 (4), 2 (4), +1 more |
| 78897 | 345 (89..450) | 284 | 47 | 28 (128), 14 (55), 25 (34), 12 (21), 26 (10), 2 (9), 21 (6), 4 (4), 11 (4), 7 (3), 22 (3), 6 (2), +4 more |
| 78899 | 365 (91..455) | 303 | 47 | 2 (127), 12 (85), 14 (39), 26 (16), 28 (16), 8 (4), 9 (3), 21 (3), 7 (2), 10 (2), 11 (2), 6 (1), +3 more |
| 79097 | 366 (94..461) | 311 | 45 | 26 (175), 2 (51), 12 (34), 21 (8), 14 (7), 11 (6), 25 (6), 20 (5), 6 (4), 10 (4), 28 (4), 9 (2), +3 more |
| 79098 | 360 (97..467) | 315 | 39 | 11 (125), 21 (43), 26 (35), 14 (30), 2 (29), 28 (19), 20 (7), 25 (7), 12 (5), 7 (4), 8 (4), 6 (2), +3 more |
| 79102 | 371 (98..477) | 313 | 43 | 14 (100), 11 (65), 28 (38), 25 (30), 8 (19), 2 (13), 26 (10), 21 (8), 9 (5), 6 (5), 4 (5), 20 (5), +5 more |
| 79103 | 380 (99..481) | 334 | 38 | 4 (134), 8 (56), 2 (33), 28 (27), 11 (24), 21 (22), 25 (11), 6 (7), 12 (4), 14 (4), 9 (3), 26 (3), +4 more |
| 79105 | 379 (101..484) | 324 | 41 | 25 (134), 2 (51), 11 (36), 8 (23), 28 (18), 21 (13), 13 (13), 4 (11), 9 (7), 6 (6), 20 (4), 7 (3), +3 more |
| 79108 | 385 (104..492) | 340 | 36 | 20 (149), 4 (47), 13 (41), 8 (29), 11 (25), 9 (13), 28 (11), 2 (8), 23 (4), 25 (4), 7 (3), 10 (2), +3 more |
| 79110 | 388 (106..497) | 346 | 34 | 8 (150), 4 (55), 24 (42), 11 (25), 13 (23), 23 (18), 9 (10), 20 (9), 10 (4), 6 (4), 17 (3), 7 (2), +1 more |
| 79111 | 386 (109..500) | 322 | 48 | 17 (134), 13 (54), 20 (31), 8 (26), 23 (23), 24 (20), 4 (13), 9 (12), 6 (3), 11 (3), 10 (2), 28 (1) |
| 79115 | 421 (111..531) | 357 | 47 | 9 (198), 13 (45), 20 (24), 17 (22), 23 (20), 4 (15), 8 (12), 24 (10), 7 (5), 10 (4), 6 (2) |
| 79116 | 411 (114..530) | 351 | 45 | 13 (175), 23 (47), 17 (36), 20 (34), 9 (18), 4 (16), 24 (13), 8 (5), 7 (3), 10 (3), 6 (1) |
| 79122 | 404 (118..532) | 326 | 48 | 23 (181), 9 (32), 17 (24), 4 (24), 13 (20), 20 (15), 8 (10), 24 (7), 6 (6), 29 (3), 10 (2), 7 (1), +1 more |
| 79132 | 391 (120..515) | 347 | 35 | 29 (134), 23 (56), 20 (38), 17 (32), 6 (25), 9 (23), 13 (15), 4 (12), 8 (6), 7 (3), 24 (3) |
| 79128 | 402 (124..527) | 361 | 37 | 7 (156), 29 (78), 9 (45), 24 (20), 6 (17), 17 (14), 8 (13), 20 (13), 13 (3), 10 (2) |
| 79134 | 407 (127..533) | 359 | 38 | 24 (159), 17 (62), 7 (45), 30 (41), 6 (34), 8 (8), 9 (7), 10 (3) |
| 79135 | 409 (129..542) | 361 | 35 | 6 (186), 7 (70), 24 (41), 17 (34), 9 (21), 30 (7), 8 (2) |
| 79139 | 406 (132..537) | 353 | 33 | 6 (109), 10 (104), 7 (80), 24 (45), 30 (8), 17 (6), 9 (1) |
| 79136 | 393 (136..538) | 346 | 34 | 10 (244), 30 (84), 7 (18) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 193/407/1004; tracks with internal gaps: 25; total internal gaps: 696; longest internal gap: 8; tracks ending in coasting: 24 (trailing rows total 670)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 935 | 69 | 55 | 3 | 0 | 78911 |
| 2 | 78..484 | 407 | 407 | 353 | 54 | 24 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 84..510 | 427 | 427 | 360 | 67 | 27 | 4 | 32 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 6 | 88..571 | 484 | 484 | 421 | 63 | 21 | 7 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 7 | 88..556 | 469 | 469 | 406 | 63 | 32 | 8 | 18 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..526 | 438 | 438 | 380 | 58 | 26 | 2 | 29 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 9 | 91..560 | 470 | 470 | 402 | 68 | 27 | 4 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 10 | 98..567 | 470 | 470 | 386 | 84 | 37 | 5 | 32 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 11 | 101..495 | 395 | 395 | 337 | 58 | 24 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..473 | 373 | 373 | 301 | 72 | 33 | 4 | 31 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 13 | 106..559 | 454 | 454 | 390 | 64 | 27 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 107..506 | 400 | 400 | 328 | 72 | 39 | 2 | 25 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 17 | 111..529 | 419 | 419 | 367 | 52 | 17 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 19 | 112..468 | 357 | 357 | 289 | 68 | 31 | 3 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 20 | 115..521 | 407 | 407 | 337 | 70 | 26 | 5 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 115..463 | 349 | 349 | 290 | 59 | 21 | 4 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 22 | 123..471 | 349 | 349 | 284 | 65 | 32 | 4 | 26 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 23 | 130..560 | 431 | 431 | 351 | 80 | 36 | 5 | 28 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 24 | 131..566 | 436 | 436 | 366 | 70 | 29 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 25 | 133..513 | 381 | 381 | 325 | 56 | 25 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 26 | 140..490 | 351 | 351 | 293 | 58 | 22 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 27 | 146..458 | 313 | 313 | 259 | 54 | 25 | 8 | 15 | 78896, 78969, 78971, 79045 |
| 28 | 158..478 | 321 | 321 | 268 | 53 | 20 | 3 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79122 |
| 29 | 271..544 | 274 | 274 | 215 | 59 | 24 | 2 | 29 | 79122, 79128, 79132 |
| 30 | 370..562 | 193 | 193 | 140 | 53 | 16 | 3 | 29 | 79134, 79135, 79136, 79139 |
