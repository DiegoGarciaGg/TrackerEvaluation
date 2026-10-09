# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=57e71f06d552
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise1.0_fp0.0_seed3/tracks.csv sha256=da04be3ed97e8cb3
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise1.0_fp0.0_seed3.csv sha256=57e71f06d5529264
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise1.0_fp0.0_seed3
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
| observations | none | 4 | 10142 | 8082 | 0.348 | 0.661 | 0.183 | 1.06 | 0.414 | 0.705 | 1.26 | 919 | 1626.0 | 0.422 | 0.476 | 0.379 | 0.796 | 1.000 | 8078 | 2064 | 4 | 11 | 14 | 0 |
| observations | none | 6 | 10142 | 8082 | 0.373 | 0.701 | 0.198 | 1.17 | 0.412 | 0.706 | 1.26 | 914 | 1617.0 | 0.423 | 0.477 | 0.380 | 0.796 | 1.000 | 8078 | 2064 | 4 | 11 | 14 | 0 |
| observations | none | 8 | 10142 | 8082 | 0.386 | 0.711 | 0.210 | 1.27 | 0.411 | 0.707 | 1.30 | 897 | 1613.0 | 0.427 | 0.482 | 0.384 | 0.796 | 0.999 | 8073 | 2069 | 9 | 11 | 14 | 0 |
| observations | none | 12 | 10142 | 8082 | 0.404 | 0.707 | 0.231 | 1.66 | 0.415 | 0.710 | 1.60 | 833 | 1590.0 | 0.445 | 0.502 | 0.400 | 0.794 | 0.997 | 8057 | 2085 | 25 | 10 | 15 | 0 |
| observations | ignore | 4 | 10142 | 8082 | 0.348 | 0.661 | 0.183 | 1.06 | 0.414 | 0.705 | 1.26 | 919 | 1626.0 | 0.422 | 0.476 | 0.379 | 0.796 | 1.000 | 8078 | 2064 | 4 | 11 | 14 | 0 |
| observations | ignore | 6 | 10142 | 8082 | 0.373 | 0.701 | 0.198 | 1.17 | 0.412 | 0.706 | 1.26 | 914 | 1617.0 | 0.423 | 0.477 | 0.380 | 0.796 | 1.000 | 8078 | 2064 | 4 | 11 | 14 | 0 |
| observations | ignore | 8 | 10142 | 8082 | 0.386 | 0.711 | 0.210 | 1.27 | 0.411 | 0.707 | 1.30 | 897 | 1613.0 | 0.427 | 0.482 | 0.384 | 0.796 | 0.999 | 8073 | 2069 | 9 | 11 | 14 | 0 |
| observations | ignore | 12 | 10142 | 8082 | 0.404 | 0.707 | 0.231 | 1.66 | 0.415 | 0.710 | 1.60 | 833 | 1590.0 | 0.445 | 0.502 | 0.400 | 0.794 | 0.997 | 8057 | 2085 | 25 | 10 | 15 | 0 |
| updates | none | 4 | 10142 | 10359 | 0.332 | 0.598 | 0.185 | 1.20 | 0.381 | 0.532 | 1.31 | 954 | 1483.0 | 0.397 | 0.393 | 0.401 | 0.824 | 0.807 | 8355 | 1787 | 2004 | 18 | 7 | 0 |
| updates | none | 6 | 10142 | 10359 | 0.377 | 0.674 | 0.211 | 1.46 | 0.416 | 0.627 | 1.52 | 939 | 1091.0 | 0.427 | 0.423 | 0.432 | 0.870 | 0.852 | 8826 | 1316 | 1533 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10359 | 0.402 | 0.703 | 0.230 | 1.68 | 0.441 | 0.712 | 1.80 | 892 | 752.0 | 0.449 | 0.444 | 0.453 | 0.910 | 0.891 | 9234 | 908 | 1125 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10359 | 0.434 | 0.731 | 0.258 | 2.16 | 0.460 | 0.752 | 2.22 | 812 | 596.0 | 0.477 | 0.472 | 0.482 | 0.927 | 0.907 | 9398 | 744 | 961 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10359 | 0.332 | 0.598 | 0.185 | 1.20 | 0.381 | 0.532 | 1.31 | 954 | 1483.0 | 0.397 | 0.393 | 0.401 | 0.824 | 0.807 | 8355 | 1787 | 2004 | 18 | 7 | 0 |
| updates | ignore | 6 | 10142 | 10359 | 0.377 | 0.674 | 0.211 | 1.46 | 0.416 | 0.627 | 1.52 | 939 | 1091.0 | 0.427 | 0.423 | 0.432 | 0.870 | 0.852 | 8826 | 1316 | 1533 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10359 | 0.402 | 0.703 | 0.230 | 1.68 | 0.441 | 0.712 | 1.80 | 892 | 752.0 | 0.449 | 0.444 | 0.453 | 0.910 | 0.891 | 9234 | 908 | 1125 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10359 | 0.434 | 0.731 | 0.258 | 2.16 | 0.460 | 0.752 | 2.22 | 812 | 596.0 | 0.477 | 0.472 | 0.482 | 0.927 | 0.907 | 9398 | 744 | 961 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8073; unmatched reference entries: 2069; unmatched candidate entries: 9
- identity switches: 897; fragmentation (coverage interruptions): 1624; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 2 -> 8 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 4 -> 9 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 7 -> 9 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 9 -> 4 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 7 -> 4 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 6 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 9 -> 2 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 4 -> 8 at (2066, 3034), 4 frames after previous cover
- f98: ref 79037: 6 -> 10 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 9 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 6 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 2 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 2 -> 4 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 4 -> 12 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 4 -> 10 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 10 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 9 -> 4 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 9 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 6 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 12 -> 8 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 8 -> 2 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 9 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 6 -> 7 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 12 -> 10 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 8 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 12 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 2 -> 8 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 10 -> 12 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 12 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 11 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 4 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 9 -> 16 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 79097: 4 -> 10 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 4 -> 12 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 7 -> 4 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 6 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 13 -> 6 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 13 -> 7 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 12 -> 2 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 2 -> 11 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 12 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 12 -> 4 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 12 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 4 -> 12 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 16 -> 4 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 4 -> 16 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 6 -> 9 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 7 -> 6 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 13 -> 7 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 11 -> 18 at (1959.5, 3036), 7 frames after previous cover
- ... 837 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 809 | 159 | 1 (809) |
| 78896 | 350 (76..429) | 273 | 60 | 14 (210), 26 (46), 2 (7), 8 (7), 11 (3) |
| 78969 | 352 (80..434) | 258 | 67 | 26 (89), 4 (59), 14 (47), 23 (27), 2 (11), 20 (9), 24 (6), 18 (5), 8 (2), 11 (2), 12 (1) |
| 78971 | 352 (84..439) | 278 | 60 | 8 (149), 26 (71), 23 (29), 4 (10), 20 (9), 25 (4), 2 (3), 24 (2), 14 (1) |
| 79045 | 355 (84..443) | 277 | 56 | 8 (115), 4 (39), 19 (31), 23 (29), 20 (20), 25 (13), 18 (6), 24 (6), 2 (4), 11 (4), 26 (4), 6 (3), +2 more |
| 79037 | 355 (86..445) | 273 | 61 | 20 (79), 23 (42), 25 (39), 26 (25), 19 (22), 8 (14), 4 (13), 24 (9), 11 (7), 18 (6), 6 (4), 10 (4), +3 more |
| 78897 | 345 (89..450) | 266 | 60 | 23 (85), 24 (60), 25 (51), 19 (13), 2 (12), 20 (11), 11 (7), 18 (7), 4 (5), 12 (5), 7 (3), 9 (3), +2 more |
| 78899 | 365 (91..455) | 288 | 61 | 25 (95), 24 (67), 2 (47), 19 (23), 4 (17), 20 (12), 9 (8), 11 (8), 10 (6), 7 (2), 23 (2), 18 (1) |
| 79097 | 366 (94..461) | 294 | 63 | 19 (114), 25 (64), 24 (43), 4 (19), 2 (16), 9 (10), 11 (8), 20 (8), 18 (5), 10 (3), 6 (2), 7 (1), +1 more |
| 79098 | 360 (97..467) | 291 | 54 | 21 (85), 11 (58), 19 (45), 20 (33), 4 (13), 2 (13), 9 (8), 18 (8), 24 (8), 7 (7), 25 (7), 12 (2), +3 more |
| 79102 | 371 (98..477) | 292 | 65 | 24 (89), 11 (52), 20 (47), 21 (33), 19 (22), 7 (13), 10 (10), 9 (8), 18 (5), 6 (3), 16 (3), 12 (3), +2 more |
| 79103 | 380 (99..481) | 308 | 56 | 11 (132), 20 (56), 7 (38), 21 (24), 18 (19), 9 (11), 19 (11), 23 (5), 4 (4), 10 (3), 6 (2), 2 (2), +1 more |
| 79105 | 379 (101..484) | 298 | 64 | 30 (88), 11 (44), 7 (44), 21 (43), 2 (23), 4 (15), 19 (11), 6 (6), 20 (6), 9 (4), 12 (4), 18 (4), +2 more |
| 79108 | 385 (104..492) | 321 | 59 | 7 (122), 21 (47), 29 (27), 18 (24), 4 (19), 23 (16), 2 (13), 12 (12), 9 (11), 11 (10), 22 (8), 6 (3), +4 more |
| 79110 | 388 (106..497) | 328 | 49 | 29 (165), 18 (55), 22 (26), 9 (18), 23 (13), 10 (11), 21 (9), 4 (8), 16 (6), 7 (3), 12 (3), 2 (3), +4 more |
| 79111 | 386 (109..500) | 302 | 67 | 18 (172), 29 (39), 4 (33), 2 (15), 10 (10), 7 (7), 9 (6), 23 (5), 21 (4), 16 (3), 12 (3), 13 (2), +2 more |
| 79115 | 421 (111..531) | 334 | 66 | 9 (142), 2 (80), 29 (17), 18 (17), 16 (15), 4 (15), 30 (12), 21 (11), 6 (7), 22 (6), 13 (3), 7 (3), +3 more |
| 79116 | 411 (114..530) | 325 | 68 | 6 (158), 9 (52), 30 (30), 12 (13), 22 (13), 29 (13), 2 (11), 21 (10), 16 (7), 4 (6), 10 (6), 13 (3), +1 more |
| 79122 | 404 (118..532) | 305 | 72 | 2 (122), 9 (61), 16 (36), 30 (31), 6 (14), 22 (13), 21 (8), 4 (4), 10 (4), 13 (3), 7 (3), 12 (3), +1 more |
| 79132 | 391 (120..515) | 316 | 61 | 22 (131), 6 (57), 16 (40), 9 (26), 29 (16), 10 (15), 21 (14), 12 (6), 30 (5), 13 (3), 7 (2), 2 (1) |
| 79128 | 402 (124..527) | 334 | 59 | 16 (159), 6 (82), 22 (71), 10 (11), 7 (7), 13 (3), 12 (1) |
| 79134 | 407 (127..533) | 319 | 65 | 10 (125), 16 (62), 22 (57), 7 (29), 6 (24), 12 (15), 13 (4), 31 (3) |
| 79135 | 409 (129..542) | 332 | 57 | 12 (164), 10 (128), 16 (15), 7 (9), 13 (9), 6 (7) |
| 79139 | 406 (132..537) | 335 | 54 | 13 (172), 12 (134), 7 (14), 31 (8), 6 (6), 10 (1) |
| 79136 | 393 (136..538) | 317 | 61 | 13 (161), 31 (121), 7 (32), 12 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 169/354/1004; tracks with internal gaps: 7; total internal gaps: 8; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 809 | 809 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 78..531 | 454 | 389 | 389 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 4 | 84..434 | 351 | 281 | 281 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 6 | 88..530 | 443 | 383 | 382 | 1 | 1 | 1 | 0 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 7 | 88..492 | 405 | 345 | 345 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..442 | 354 | 288 | 287 | 1 | 1 | 1 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..531 | 441 | 371 | 370 | 1 | 1 | 1 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 98..533 | 436 | 348 | 348 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 11 | 101..481 | 381 | 337 | 337 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 101..542 | 442 | 378 | 378 | 0 | 0 | 0 | 0 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 106..537 | 432 | 366 | 366 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 107..429 | 323 | 259 | 259 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 16 | 108..527 | 420 | 355 | 354 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 18 | 112..500 | 389 | 335 | 334 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 19 | 115..461 | 347 | 292 | 292 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 115..444 | 330 | 290 | 290 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 21 | 123..466 | 344 | 288 | 288 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 130..515 | 386 | 328 | 327 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 23 | 131..449 | 319 | 254 | 254 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79108, 79110, 79111, 79115 |
| 24 | 133..477 | 345 | 291 | 291 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79108 |
| 25 | 136..455 | 320 | 273 | 273 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 146..439 | 294 | 238 | 238 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 29 | 178..497 | 320 | 283 | 280 | 3 | 2 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 30 | 271..484 | 214 | 169 | 169 | 0 | 0 | 0 | 0 | 79105, 79110, 79115, 79116, 79122, 79132 |
| 31 | 370..538 | 169 | 132 | 132 | 0 | 0 | 0 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8073; unmatched reference entries: 2069; unmatched candidate entries: 9
- identity switches: 897; fragmentation (coverage interruptions): 1624; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 2 -> 8 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 4 -> 9 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 7 -> 9 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 9 -> 4 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 7 -> 4 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 6 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 9 -> 2 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 4 -> 8 at (2066, 3034), 4 frames after previous cover
- f98: ref 79037: 6 -> 10 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 9 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 6 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 2 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 2 -> 4 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 4 -> 12 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 4 -> 10 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 10 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 9 -> 4 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 9 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 6 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 12 -> 8 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 8 -> 2 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 9 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 6 -> 7 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 12 -> 10 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 8 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 12 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 2 -> 8 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 10 -> 12 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 12 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 11 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 4 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 9 -> 16 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 79097: 4 -> 10 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 4 -> 12 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 7 -> 4 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 6 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 13 -> 6 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 13 -> 7 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 12 -> 2 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 2 -> 11 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 12 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 12 -> 4 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 12 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 4 -> 12 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 16 -> 4 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 4 -> 16 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 6 -> 9 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 7 -> 6 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 13 -> 7 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 11 -> 18 at (1959.5, 3036), 7 frames after previous cover
- ... 837 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 809 | 159 | 1 (809) |
| 78896 | 350 (76..429) | 273 | 60 | 14 (210), 26 (46), 2 (7), 8 (7), 11 (3) |
| 78969 | 352 (80..434) | 258 | 67 | 26 (89), 4 (59), 14 (47), 23 (27), 2 (11), 20 (9), 24 (6), 18 (5), 8 (2), 11 (2), 12 (1) |
| 78971 | 352 (84..439) | 278 | 60 | 8 (149), 26 (71), 23 (29), 4 (10), 20 (9), 25 (4), 2 (3), 24 (2), 14 (1) |
| 79045 | 355 (84..443) | 277 | 56 | 8 (115), 4 (39), 19 (31), 23 (29), 20 (20), 25 (13), 18 (6), 24 (6), 2 (4), 11 (4), 26 (4), 6 (3), +2 more |
| 79037 | 355 (86..445) | 273 | 61 | 20 (79), 23 (42), 25 (39), 26 (25), 19 (22), 8 (14), 4 (13), 24 (9), 11 (7), 18 (6), 6 (4), 10 (4), +3 more |
| 78897 | 345 (89..450) | 266 | 60 | 23 (85), 24 (60), 25 (51), 19 (13), 2 (12), 20 (11), 11 (7), 18 (7), 4 (5), 12 (5), 7 (3), 9 (3), +2 more |
| 78899 | 365 (91..455) | 288 | 61 | 25 (95), 24 (67), 2 (47), 19 (23), 4 (17), 20 (12), 9 (8), 11 (8), 10 (6), 7 (2), 23 (2), 18 (1) |
| 79097 | 366 (94..461) | 294 | 63 | 19 (114), 25 (64), 24 (43), 4 (19), 2 (16), 9 (10), 11 (8), 20 (8), 18 (5), 10 (3), 6 (2), 7 (1), +1 more |
| 79098 | 360 (97..467) | 291 | 54 | 21 (85), 11 (58), 19 (45), 20 (33), 4 (13), 2 (13), 9 (8), 18 (8), 24 (8), 7 (7), 25 (7), 12 (2), +3 more |
| 79102 | 371 (98..477) | 292 | 65 | 24 (89), 11 (52), 20 (47), 21 (33), 19 (22), 7 (13), 10 (10), 9 (8), 18 (5), 6 (3), 16 (3), 12 (3), +2 more |
| 79103 | 380 (99..481) | 308 | 56 | 11 (132), 20 (56), 7 (38), 21 (24), 18 (19), 9 (11), 19 (11), 23 (5), 4 (4), 10 (3), 6 (2), 2 (2), +1 more |
| 79105 | 379 (101..484) | 298 | 64 | 30 (88), 11 (44), 7 (44), 21 (43), 2 (23), 4 (15), 19 (11), 6 (6), 20 (6), 9 (4), 12 (4), 18 (4), +2 more |
| 79108 | 385 (104..492) | 321 | 59 | 7 (122), 21 (47), 29 (27), 18 (24), 4 (19), 23 (16), 2 (13), 12 (12), 9 (11), 11 (10), 22 (8), 6 (3), +4 more |
| 79110 | 388 (106..497) | 328 | 49 | 29 (165), 18 (55), 22 (26), 9 (18), 23 (13), 10 (11), 21 (9), 4 (8), 16 (6), 7 (3), 12 (3), 2 (3), +4 more |
| 79111 | 386 (109..500) | 302 | 67 | 18 (172), 29 (39), 4 (33), 2 (15), 10 (10), 7 (7), 9 (6), 23 (5), 21 (4), 16 (3), 12 (3), 13 (2), +2 more |
| 79115 | 421 (111..531) | 334 | 66 | 9 (142), 2 (80), 29 (17), 18 (17), 16 (15), 4 (15), 30 (12), 21 (11), 6 (7), 22 (6), 13 (3), 7 (3), +3 more |
| 79116 | 411 (114..530) | 325 | 68 | 6 (158), 9 (52), 30 (30), 12 (13), 22 (13), 29 (13), 2 (11), 21 (10), 16 (7), 4 (6), 10 (6), 13 (3), +1 more |
| 79122 | 404 (118..532) | 305 | 72 | 2 (122), 9 (61), 16 (36), 30 (31), 6 (14), 22 (13), 21 (8), 4 (4), 10 (4), 13 (3), 7 (3), 12 (3), +1 more |
| 79132 | 391 (120..515) | 316 | 61 | 22 (131), 6 (57), 16 (40), 9 (26), 29 (16), 10 (15), 21 (14), 12 (6), 30 (5), 13 (3), 7 (2), 2 (1) |
| 79128 | 402 (124..527) | 334 | 59 | 16 (159), 6 (82), 22 (71), 10 (11), 7 (7), 13 (3), 12 (1) |
| 79134 | 407 (127..533) | 319 | 65 | 10 (125), 16 (62), 22 (57), 7 (29), 6 (24), 12 (15), 13 (4), 31 (3) |
| 79135 | 409 (129..542) | 332 | 57 | 12 (164), 10 (128), 16 (15), 7 (9), 13 (9), 6 (7) |
| 79139 | 406 (132..537) | 335 | 54 | 13 (172), 12 (134), 7 (14), 31 (8), 6 (6), 10 (1) |
| 79136 | 393 (136..538) | 317 | 61 | 13 (161), 31 (121), 7 (32), 12 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 169/354/1004; tracks with internal gaps: 7; total internal gaps: 8; longest internal gap: 2; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 809 | 809 | 0 | 0 | 0 | 0 | 78911 |
| 2 | 78..531 | 454 | 389 | 389 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 4 | 84..434 | 351 | 281 | 281 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 6 | 88..530 | 443 | 383 | 382 | 1 | 1 | 1 | 0 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 7 | 88..492 | 405 | 345 | 345 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..442 | 354 | 288 | 287 | 1 | 1 | 1 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..531 | 441 | 371 | 370 | 1 | 1 | 1 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 98..533 | 436 | 348 | 348 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 11 | 101..481 | 381 | 337 | 337 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 101..542 | 442 | 378 | 378 | 0 | 0 | 0 | 0 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 106..537 | 432 | 366 | 366 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 107..429 | 323 | 259 | 259 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 16 | 108..527 | 420 | 355 | 354 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 18 | 112..500 | 389 | 335 | 334 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 19 | 115..461 | 347 | 292 | 292 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 115..444 | 330 | 290 | 290 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 21 | 123..466 | 344 | 288 | 288 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 130..515 | 386 | 328 | 327 | 1 | 1 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 23 | 131..449 | 319 | 254 | 254 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79108, 79110, 79111, 79115 |
| 24 | 133..477 | 345 | 291 | 291 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79108 |
| 25 | 136..455 | 320 | 273 | 273 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 146..439 | 294 | 238 | 238 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 29 | 178..497 | 320 | 283 | 280 | 3 | 2 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 30 | 271..484 | 214 | 169 | 169 | 0 | 0 | 0 | 0 | 79105, 79110, 79115, 79116, 79122, 79132 |
| 31 | 370..538 | 169 | 132 | 132 | 0 | 0 | 0 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9234; unmatched reference entries: 908; unmatched candidate entries: 1125
- identity switches: 892; fragmentation (coverage interruptions): 671; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 2 -> 8 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 4 -> 9 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 7 -> 9 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 9 -> 4 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 7 -> 4 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 6 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 9 -> 2 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 4 -> 8 at (2066, 3034), 3 frames after previous cover
- f98: ref 79037: 6 -> 10 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 9 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 6 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 2 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 2 -> 4 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 4 -> 12 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 4 -> 10 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 10 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 9 -> 4 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 9 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 6 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 12 -> 8 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 8 -> 2 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 9 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 6 -> 7 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 12 -> 10 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 8 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 12 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 2 -> 8 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 10 -> 12 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 12 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 11 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 4 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 9 -> 16 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79097: 4 -> 10 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 4 -> 12 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 7 -> 4 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 6 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 13 -> 6 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 13 -> 7 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 12 -> 2 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 2 -> 11 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 12 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 12 -> 4 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 12 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 4 -> 12 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 16 -> 4 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 4 -> 16 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 6 -> 9 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 7 -> 6 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 13 -> 7 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 11 -> 18 at (1959.5, 3036), 7 frames after previous cover
- ... 832 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 986 | 11 | 1 (986) |
| 78896 | 350 (76..429) | 313 | 26 | 14 (243), 26 (51), 8 (9), 2 (7), 11 (3) |
| 78969 | 352 (80..434) | 306 | 27 | 26 (108), 4 (70), 14 (57), 23 (33), 2 (11), 20 (9), 24 (7), 18 (6), 8 (2), 11 (2), 12 (1) |
| 78971 | 352 (84..439) | 316 | 28 | 8 (172), 26 (78), 23 (33), 4 (11), 20 (9), 25 (6), 2 (4), 24 (2), 14 (1) |
| 79045 | 355 (84..443) | 309 | 32 | 8 (135), 4 (47), 23 (33), 19 (33), 20 (18), 25 (13), 18 (6), 24 (6), 2 (4), 11 (4), 26 (4), 6 (3), +2 more |
| 79037 | 355 (86..445) | 321 | 26 | 20 (92), 23 (52), 25 (46), 26 (28), 19 (26), 4 (20), 8 (15), 24 (10), 11 (7), 18 (7), 2 (5), 6 (4), +3 more |
| 78897 | 345 (89..450) | 298 | 39 | 23 (98), 24 (66), 25 (53), 19 (15), 2 (12), 20 (12), 4 (9), 11 (8), 18 (8), 12 (5), 7 (4), 26 (4), +2 more |
| 78899 | 365 (91..455) | 316 | 38 | 25 (108), 24 (71), 2 (48), 19 (27), 4 (21), 20 (12), 9 (9), 11 (8), 10 (7), 7 (2), 23 (2), 18 (1) |
| 79097 | 366 (94..461) | 330 | 30 | 19 (131), 25 (75), 24 (45), 4 (23), 2 (16), 9 (10), 11 (8), 20 (8), 18 (6), 10 (4), 6 (2), 7 (1), +1 more |
| 79098 | 360 (97..467) | 322 | 30 | 21 (101), 11 (63), 19 (50), 20 (36), 4 (15), 2 (12), 24 (9), 9 (8), 18 (8), 7 (7), 25 (7), 12 (2), +3 more |
| 79102 | 371 (98..477) | 330 | 32 | 24 (109), 11 (55), 20 (52), 21 (40), 19 (22), 7 (15), 9 (9), 10 (9), 18 (5), 12 (4), 6 (3), 16 (3), +2 more |
| 79103 | 380 (99..481) | 342 | 32 | 11 (148), 20 (63), 7 (41), 21 (27), 18 (20), 19 (12), 9 (11), 23 (5), 4 (4), 10 (3), 24 (3), 6 (2), +2 more |
| 79105 | 379 (101..484) | 338 | 28 | 30 (109), 7 (49), 11 (47), 21 (47), 2 (24), 4 (17), 19 (13), 20 (7), 6 (6), 9 (5), 12 (4), 18 (4), +2 more |
| 79108 | 385 (104..492) | 361 | 20 | 7 (142), 21 (54), 29 (30), 18 (29), 4 (22), 23 (17), 2 (14), 12 (12), 9 (11), 11 (9), 22 (8), 6 (3), +4 more |
| 79110 | 388 (106..497) | 360 | 24 | 29 (184), 18 (61), 22 (27), 9 (19), 23 (13), 10 (12), 4 (9), 21 (9), 16 (7), 30 (5), 7 (3), 12 (3), +4 more |
| 79111 | 386 (109..500) | 342 | 32 | 18 (199), 29 (41), 4 (38), 2 (16), 10 (11), 7 (10), 9 (9), 23 (5), 21 (3), 12 (3), 13 (2), 22 (2), +2 more |
| 79115 | 421 (111..531) | 376 | 29 | 9 (171), 2 (88), 18 (18), 29 (17), 16 (16), 4 (16), 30 (13), 21 (11), 6 (7), 22 (6), 7 (4), 13 (3), +3 more |
| 79116 | 411 (114..530) | 373 | 30 | 6 (185), 9 (52), 30 (36), 22 (16), 12 (15), 29 (15), 2 (15), 21 (10), 4 (7), 10 (7), 16 (6), 13 (5), +2 more |
| 79122 | 404 (118..532) | 355 | 32 | 2 (153), 9 (72), 16 (39), 30 (32), 6 (15), 22 (15), 21 (8), 4 (4), 12 (4), 10 (4), 13 (3), 7 (3), +1 more |
| 79132 | 391 (120..515) | 361 | 25 | 22 (152), 6 (64), 16 (45), 9 (28), 21 (17), 29 (17), 10 (15), 30 (8), 12 (7), 13 (3), 2 (3), 7 (2) |
| 79128 | 402 (124..527) | 381 | 18 | 16 (188), 6 (89), 22 (81), 10 (12), 7 (7), 13 (3), 12 (1) |
| 79134 | 407 (127..533) | 373 | 22 | 10 (159), 16 (71), 22 (62), 7 (33), 6 (28), 12 (16), 13 (4) |
| 79135 | 409 (129..542) | 379 | 20 | 12 (183), 10 (149), 16 (18), 13 (11), 7 (10), 6 (8) |
| 79139 | 406 (132..537) | 381 | 19 | 13 (200), 12 (159), 7 (16), 6 (6) |
| 79136 | 393 (136..538) | 365 | 21 | 13 (169), 31 (156), 7 (37), 12 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 198/383/1004; tracks with internal gaps: 25; total internal gaps: 343; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 690)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 986 | 18 | 11 | 3 | 0 | 78911 |
| 2 | 78..560 | 483 | 483 | 439 | 44 | 11 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 4 | 84..463 | 380 | 380 | 335 | 45 | 14 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 6 | 88..559 | 472 | 472 | 430 | 42 | 10 | 2 | 29 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 7 | 88..521 | 434 | 434 | 392 | 42 | 9 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..471 | 383 | 383 | 333 | 50 | 19 | 2 | 28 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..560 | 470 | 470 | 419 | 51 | 17 | 3 | 28 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 98..562 | 465 | 465 | 407 | 58 | 19 | 5 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 11 | 101..510 | 410 | 410 | 364 | 46 | 11 | 3 | 32 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 101..571 | 471 | 471 | 428 | 43 | 10 | 3 | 29 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 106..566 | 461 | 461 | 406 | 55 | 20 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 107..458 | 352 | 352 | 302 | 50 | 18 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 16 | 108..556 | 449 | 449 | 402 | 47 | 15 | 4 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 18 | 112..529 | 418 | 418 | 379 | 39 | 9 | 2 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 19 | 115..490 | 376 | 376 | 329 | 47 | 13 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 115..473 | 359 | 359 | 318 | 41 | 9 | 4 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 21 | 123..495 | 373 | 373 | 327 | 46 | 17 | 2 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 130..544 | 415 | 415 | 369 | 46 | 14 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 23 | 131..478 | 348 | 348 | 292 | 56 | 20 | 4 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79108, 79110, 79111, 79115 |
| 24 | 133..506 | 374 | 374 | 330 | 44 | 17 | 2 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108 |
| 25 | 136..484 | 349 | 349 | 308 | 41 | 12 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 146..468 | 323 | 323 | 273 | 50 | 17 | 2 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 29 | 178..526 | 349 | 349 | 307 | 42 | 12 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 30 | 271..513 | 243 | 243 | 203 | 40 | 9 | 2 | 29 | 79105, 79110, 79115, 79116, 79122, 79132 |
| 31 | 370..567 | 198 | 198 | 156 | 42 | 10 | 3 | 29 | 79136 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9234; unmatched reference entries: 908; unmatched candidate entries: 1125
- identity switches: 892; fragmentation (coverage interruptions): 671; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 2 -> 4 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 4 -> 2 at (2121.5, 3033), 1 frames after previous cover
- f89: ref 78896: 2 -> 8 at (2078, 3034), 4 frames after previous cover
- f91: ref 79037: 7 -> 6 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 4 -> 2 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 6 -> 4 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78971: 2 -> 4 at (2090.5, 3032.5), 1 frames after previous cover
- f94: ref 79045: 4 -> 9 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 7 -> 9 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 9 -> 7 at (2134.5, 3029), 2 frames after previous cover
- f96: ref 79045: 9 -> 4 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 78899: 7 -> 4 at (2123, 3030), 1 frames after previous cover
- f97: ref 79097: 6 -> 7 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 9 -> 2 at (2100, 3031), 1 frames after previous cover
- f98: ref 78971: 4 -> 8 at (2066, 3034), 3 frames after previous cover
- f98: ref 79037: 6 -> 10 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 7 -> 9 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 6 -> 7 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 4 -> 2 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 2 -> 4 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 8 -> 11 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 2 -> 12 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 4 -> 12 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 4 -> 10 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 10 -> 2 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79097: 9 -> 4 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 7 -> 9 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 6 -> 7 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78969: 12 -> 8 at (2014.5, 3033.5), 2 frames after previous cover
- f103: ref 78971: 8 -> 2 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79102: 7 -> 9 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 6 -> 7 at (2133.5, 3022.5), 1 frames after previous cover
- f104: ref 78897: 12 -> 10 at (2064, 3032), 1 frames after previous cover
- f104: ref 78969: 8 -> 11 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 2 -> 12 at (2051, 3034), 2 frames after previous cover
- f105: ref 78971: 2 -> 8 at (2022, 3034), 1 frames after previous cover
- f106: ref 78897: 10 -> 12 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 12 -> 2 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 2 -> 11 at (2023.5, 3033.5), 1 frames after previous cover
- f107: ref 78896: 11 -> 14 at (1965, 3034), 4 frames after previous cover
- f108: ref 79098: 9 -> 4 at (2084.5, 3028.5), 6 frames after previous cover
- f108: ref 79102: 9 -> 16 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79097: 4 -> 10 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79098: 4 -> 12 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79103: 7 -> 4 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 6 -> 9 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 13 -> 6 at (2125, 3025), 2 frames after previous cover
- f109: ref 79110: 13 -> 7 at (2139.5, 3026.5), 1 frames after previous cover
- f110: ref 78897: 12 -> 2 at (2028, 3032.5), 2 frames after previous cover
- f110: ref 79037: 2 -> 11 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 10 -> 12 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 12 -> 4 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79097: 12 -> 10 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 4 -> 12 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 16 -> 4 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 4 -> 16 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 6 -> 9 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 7 -> 6 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 13 -> 7 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78969: 11 -> 18 at (1959.5, 3036), 7 frames after previous cover
- ... 832 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 986 | 11 | 1 (986) |
| 78896 | 350 (76..429) | 313 | 26 | 14 (243), 26 (51), 8 (9), 2 (7), 11 (3) |
| 78969 | 352 (80..434) | 306 | 27 | 26 (108), 4 (70), 14 (57), 23 (33), 2 (11), 20 (9), 24 (7), 18 (6), 8 (2), 11 (2), 12 (1) |
| 78971 | 352 (84..439) | 316 | 28 | 8 (172), 26 (78), 23 (33), 4 (11), 20 (9), 25 (6), 2 (4), 24 (2), 14 (1) |
| 79045 | 355 (84..443) | 309 | 32 | 8 (135), 4 (47), 23 (33), 19 (33), 20 (18), 25 (13), 18 (6), 24 (6), 2 (4), 11 (4), 26 (4), 6 (3), +2 more |
| 79037 | 355 (86..445) | 321 | 26 | 20 (92), 23 (52), 25 (46), 26 (28), 19 (26), 4 (20), 8 (15), 24 (10), 11 (7), 18 (7), 2 (5), 6 (4), +3 more |
| 78897 | 345 (89..450) | 298 | 39 | 23 (98), 24 (66), 25 (53), 19 (15), 2 (12), 20 (12), 4 (9), 11 (8), 18 (8), 12 (5), 7 (4), 26 (4), +2 more |
| 78899 | 365 (91..455) | 316 | 38 | 25 (108), 24 (71), 2 (48), 19 (27), 4 (21), 20 (12), 9 (9), 11 (8), 10 (7), 7 (2), 23 (2), 18 (1) |
| 79097 | 366 (94..461) | 330 | 30 | 19 (131), 25 (75), 24 (45), 4 (23), 2 (16), 9 (10), 11 (8), 20 (8), 18 (6), 10 (4), 6 (2), 7 (1), +1 more |
| 79098 | 360 (97..467) | 322 | 30 | 21 (101), 11 (63), 19 (50), 20 (36), 4 (15), 2 (12), 24 (9), 9 (8), 18 (8), 7 (7), 25 (7), 12 (2), +3 more |
| 79102 | 371 (98..477) | 330 | 32 | 24 (109), 11 (55), 20 (52), 21 (40), 19 (22), 7 (15), 9 (9), 10 (9), 18 (5), 12 (4), 6 (3), 16 (3), +2 more |
| 79103 | 380 (99..481) | 342 | 32 | 11 (148), 20 (63), 7 (41), 21 (27), 18 (20), 19 (12), 9 (11), 23 (5), 4 (4), 10 (3), 24 (3), 6 (2), +2 more |
| 79105 | 379 (101..484) | 338 | 28 | 30 (109), 7 (49), 11 (47), 21 (47), 2 (24), 4 (17), 19 (13), 20 (7), 6 (6), 9 (5), 12 (4), 18 (4), +2 more |
| 79108 | 385 (104..492) | 361 | 20 | 7 (142), 21 (54), 29 (30), 18 (29), 4 (22), 23 (17), 2 (14), 12 (12), 9 (11), 11 (9), 22 (8), 6 (3), +4 more |
| 79110 | 388 (106..497) | 360 | 24 | 29 (184), 18 (61), 22 (27), 9 (19), 23 (13), 10 (12), 4 (9), 21 (9), 16 (7), 30 (5), 7 (3), 12 (3), +4 more |
| 79111 | 386 (109..500) | 342 | 32 | 18 (199), 29 (41), 4 (38), 2 (16), 10 (11), 7 (10), 9 (9), 23 (5), 21 (3), 12 (3), 13 (2), 22 (2), +2 more |
| 79115 | 421 (111..531) | 376 | 29 | 9 (171), 2 (88), 18 (18), 29 (17), 16 (16), 4 (16), 30 (13), 21 (11), 6 (7), 22 (6), 7 (4), 13 (3), +3 more |
| 79116 | 411 (114..530) | 373 | 30 | 6 (185), 9 (52), 30 (36), 22 (16), 12 (15), 29 (15), 2 (15), 21 (10), 4 (7), 10 (7), 16 (6), 13 (5), +2 more |
| 79122 | 404 (118..532) | 355 | 32 | 2 (153), 9 (72), 16 (39), 30 (32), 6 (15), 22 (15), 21 (8), 4 (4), 12 (4), 10 (4), 13 (3), 7 (3), +1 more |
| 79132 | 391 (120..515) | 361 | 25 | 22 (152), 6 (64), 16 (45), 9 (28), 21 (17), 29 (17), 10 (15), 30 (8), 12 (7), 13 (3), 2 (3), 7 (2) |
| 79128 | 402 (124..527) | 381 | 18 | 16 (188), 6 (89), 22 (81), 10 (12), 7 (7), 13 (3), 12 (1) |
| 79134 | 407 (127..533) | 373 | 22 | 10 (159), 16 (71), 22 (62), 7 (33), 6 (28), 12 (16), 13 (4) |
| 79135 | 409 (129..542) | 379 | 20 | 12 (183), 10 (149), 16 (18), 13 (11), 7 (10), 6 (8) |
| 79139 | 406 (132..537) | 381 | 19 | 13 (200), 12 (159), 7 (16), 6 (6) |
| 79136 | 393 (136..538) | 365 | 21 | 13 (169), 31 (156), 7 (37), 12 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 198/383/1004; tracks with internal gaps: 25; total internal gaps: 343; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 690)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5..1008 | 1004 | 1004 | 986 | 18 | 11 | 3 | 0 | 78911 |
| 2 | 78..560 | 483 | 483 | 439 | 44 | 11 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 4 | 84..463 | 380 | 380 | 335 | 45 | 14 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 6 | 88..559 | 472 | 472 | 430 | 42 | 10 | 2 | 29 | 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 7 | 88..521 | 434 | 434 | 392 | 42 | 9 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 89..471 | 383 | 383 | 333 | 50 | 19 | 2 | 28 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..560 | 470 | 470 | 419 | 51 | 17 | 3 | 28 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 98..562 | 465 | 465 | 407 | 58 | 19 | 5 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 11 | 101..510 | 410 | 410 | 364 | 46 | 11 | 3 | 32 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 101..571 | 471 | 471 | 428 | 43 | 10 | 3 | 29 | 78897, 78969, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 106..566 | 461 | 461 | 406 | 55 | 20 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 107..458 | 352 | 352 | 302 | 50 | 18 | 3 | 29 | 78896, 78969, 78971, 79045 |
| 16 | 108..556 | 449 | 449 | 402 | 47 | 15 | 4 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 18 | 112..529 | 418 | 418 | 379 | 39 | 9 | 2 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 19 | 115..490 | 376 | 376 | 329 | 47 | 13 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 20 | 115..473 | 359 | 359 | 318 | 41 | 9 | 4 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 21 | 123..495 | 373 | 373 | 327 | 46 | 17 | 2 | 28 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 130..544 | 415 | 415 | 369 | 46 | 14 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 23 | 131..478 | 348 | 348 | 292 | 56 | 20 | 4 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79103, 79108, 79110, 79111, 79115 |
| 24 | 133..506 | 374 | 374 | 330 | 44 | 17 | 2 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108 |
| 25 | 136..484 | 349 | 349 | 308 | 41 | 12 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 26 | 146..468 | 323 | 323 | 273 | 50 | 17 | 2 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 29 | 178..526 | 349 | 349 | 307 | 42 | 12 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 30 | 271..513 | 243 | 243 | 203 | 40 | 9 | 2 | 29 | 79105, 79110, 79115, 79116, 79122, 79132 |
| 31 | 370..567 | 198 | 198 | 156 | 42 | 10 | 3 | 29 | 79136 |
