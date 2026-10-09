# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=501e42365141
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise0.0_fp0.5_seed3/tracks.csv sha256=d20b86f688ff5c3d
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise0.0_fp0.5_seed3.csv sha256=501e4236514176e7
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise0.0_fp0.5_seed3
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
| observations | none | 4 | 10142 | 8041 | 0.353 | 0.782 | 0.159 | 0.01 | 0.353 | 0.667 | 0.01 | 1183 | 1640.0 | 0.298 | 0.337 | 0.267 | 0.788 | 0.994 | 7994 | 2148 | 47 | 6 | 19 | 0 |
| observations | none | 6 | 10142 | 8041 | 0.353 | 0.781 | 0.159 | 0.02 | 0.353 | 0.667 | 0.02 | 1184 | 1639.0 | 0.298 | 0.337 | 0.267 | 0.788 | 0.994 | 7994 | 2148 | 47 | 6 | 19 | 0 |
| observations | none | 8 | 10142 | 8041 | 0.353 | 0.777 | 0.160 | 0.04 | 0.352 | 0.668 | 0.06 | 1168 | 1636.0 | 0.299 | 0.338 | 0.268 | 0.788 | 0.994 | 7994 | 2148 | 47 | 6 | 19 | 0 |
| observations | none | 12 | 10142 | 8041 | 0.353 | 0.762 | 0.163 | 0.19 | 0.352 | 0.673 | 0.45 | 1094 | 1601.0 | 0.311 | 0.352 | 0.279 | 0.787 | 0.993 | 7981 | 2161 | 60 | 7 | 18 | 0 |
| observations | ignore | 4 | 10142 | 8041 | 0.353 | 0.782 | 0.159 | 0.01 | 0.353 | 0.667 | 0.01 | 1183 | 1640.0 | 0.298 | 0.337 | 0.267 | 0.788 | 0.994 | 7994 | 2148 | 47 | 6 | 19 | 0 |
| observations | ignore | 6 | 10142 | 8041 | 0.353 | 0.781 | 0.159 | 0.02 | 0.353 | 0.667 | 0.02 | 1184 | 1639.0 | 0.298 | 0.337 | 0.267 | 0.788 | 0.994 | 7994 | 2148 | 47 | 6 | 19 | 0 |
| observations | ignore | 8 | 10142 | 8041 | 0.353 | 0.777 | 0.160 | 0.04 | 0.352 | 0.668 | 0.06 | 1168 | 1636.0 | 0.299 | 0.338 | 0.268 | 0.788 | 0.994 | 7994 | 2148 | 47 | 6 | 19 | 0 |
| observations | ignore | 12 | 10142 | 8041 | 0.353 | 0.762 | 0.163 | 0.19 | 0.352 | 0.673 | 0.45 | 1094 | 1601.0 | 0.311 | 0.352 | 0.279 | 0.787 | 0.993 | 7981 | 2161 | 60 | 7 | 18 | 0 |
| updates | none | 4 | 10142 | 10388 | 0.332 | 0.684 | 0.161 | 0.19 | 0.329 | 0.478 | 0.09 | 1198 | 1558.0 | 0.280 | 0.277 | 0.283 | 0.810 | 0.791 | 8218 | 1924 | 2170 | 11 | 14 | 0 |
| updates | none | 6 | 10142 | 10388 | 0.351 | 0.723 | 0.170 | 0.38 | 0.357 | 0.564 | 0.36 | 1201 | 1210.0 | 0.298 | 0.295 | 0.302 | 0.853 | 0.833 | 8656 | 1486 | 1732 | 24 | 1 | 0 |
| updates | none | 8 | 10142 | 10388 | 0.361 | 0.742 | 0.176 | 0.53 | 0.380 | 0.654 | 0.72 | 1162 | 869.0 | 0.315 | 0.312 | 0.319 | 0.896 | 0.875 | 9090 | 1052 | 1298 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10388 | 0.372 | 0.755 | 0.184 | 0.82 | 0.387 | 0.680 | 1.19 | 1075 | 758.0 | 0.331 | 0.327 | 0.335 | 0.905 | 0.884 | 9179 | 963 | 1209 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10388 | 0.332 | 0.684 | 0.161 | 0.19 | 0.329 | 0.478 | 0.09 | 1198 | 1558.0 | 0.280 | 0.277 | 0.283 | 0.810 | 0.791 | 8218 | 1924 | 2170 | 11 | 14 | 0 |
| updates | ignore | 6 | 10142 | 10388 | 0.351 | 0.723 | 0.170 | 0.38 | 0.357 | 0.564 | 0.36 | 1201 | 1210.0 | 0.298 | 0.295 | 0.302 | 0.853 | 0.833 | 8656 | 1486 | 1732 | 24 | 1 | 0 |
| updates | ignore | 8 | 10142 | 10388 | 0.361 | 0.742 | 0.176 | 0.53 | 0.380 | 0.654 | 0.72 | 1162 | 869.0 | 0.315 | 0.312 | 0.319 | 0.896 | 0.875 | 9090 | 1052 | 1298 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10388 | 0.372 | 0.755 | 0.184 | 0.82 | 0.387 | 0.680 | 1.19 | 1075 | 758.0 | 0.331 | 0.327 | 0.335 | 0.905 | 0.884 | 9179 | 963 | 1209 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 28; matched pairs: 7994; unmatched reference entries: 2148; unmatched candidate entries: 47
- identity switches: 1168; fragmentation (coverage interruptions): 1634; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 45 -> 40 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 40 -> 45 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 40 -> 46 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 45 -> 40 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 45 -> 40 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 40 -> 49 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 45 -> 40 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79045: 40 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 40 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 45 -> 40 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 40 -> 53 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 50 -> 52 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 50 -> 53 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 40 -> 50 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 53 -> 52 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 52 -> 48 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 45 -> 40 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 45 -> 54 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 48 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 48 -> 49 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 53 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 50 -> 40 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 48 -> 53 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 40 -> 54 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 50 -> 52 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 40 -> 50 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 53 -> 49 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 52 -> 53 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 54 -> 40 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 49 -> 52 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 45 -> 60 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 52 -> 49 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 45 -> 63 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 45 -> 64 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 49 -> 53 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 52 -> 40 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 53 -> 52 at (2019.5, 3034), 3 frames after previous cover
- f110: ref 79097: 40 -> 63 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 45 -> 67 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 40 -> 52 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 50 -> 53 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 63 -> 50 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 60 -> 40 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 64 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 60 at (2113.5, 3026), 5 frames after previous cover
- f111: ref 79110: 67 -> 64 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 45 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 53 -> 46 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 54 -> 40 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 40 -> 63 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 63 -> 54 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 46 -> 48 at (1928, 3035), 3 frames after previous cover
- f114: ref 78897: 52 -> 71 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 53 -> 52 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 48 -> 46 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 50 -> 53 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 40 -> 50 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 40 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 64 -> 60 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 67 -> 64 at (2126, 3027), 2 frames after previous cover
- ... 1108 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 812 | 156 | 0 (812) |
| 78896 | 350 (76..429) | 285 | 49 | 48 (137), 82 (79), 84 (36), 46 (23), 40 (5), 54 (5) |
| 78969 | 352 (80..434) | 282 | 47 | 82 (88), 46 (79), 54 (51), 84 (33), 48 (25), 86 (6) |
| 78971 | 352 (84..439) | 279 | 50 | 54 (77), 84 (62), 92 (39), 49 (28), 82 (25), 53 (22), 48 (10), 46 (8), 86 (4), 40 (3), 45 (1) |
| 79045 | 355 (84..443) | 275 | 61 | 86 (59), 82 (53), 98 (53), 53 (22), 84 (18), 54 (18), 92 (17), 49 (9), 48 (7), 52 (5), 46 (5), 50 (3), +3 more |
| 79037 | 355 (86..445) | 279 | 57 | 86 (79), 98 (68), 84 (21), 53 (15), 49 (15), 82 (13), 77 (12), 92 (12), 48 (11), 88 (9), 52 (8), 54 (5), +4 more |
| 78897 | 345 (89..450) | 269 | 60 | 49 (76), 86 (52), 48 (33), 77 (19), 52 (16), 88 (14), 53 (13), 92 (12), 84 (11), 54 (7), 50 (4), 98 (4), +4 more |
| 78899 | 365 (91..455) | 288 | 60 | 84 (60), 86 (55), 88 (42), 49 (28), 92 (28), 77 (16), 50 (12), 63 (11), 48 (11), 53 (8), 40 (5), 45 (3), +4 more |
| 79097 | 366 (94..461) | 274 | 74 | 148 (51), 49 (45), 88 (36), 63 (31), 77 (16), 84 (15), 98 (14), 86 (14), 53 (12), 82 (9), 40 (8), 92 (8), +6 more |
| 79098 | 360 (97..467) | 273 | 61 | 148 (79), 77 (44), 53 (33), 88 (30), 98 (19), 92 (16), 54 (11), 49 (9), 48 (8), 50 (5), 71 (4), 67 (4), +6 more |
| 79102 | 371 (98..477) | 292 | 62 | 53 (97), 77 (50), 49 (22), 92 (18), 63 (16), 88 (14), 54 (13), 98 (13), 132 (11), 148 (10), 52 (6), 60 (5), +5 more |
| 79103 | 380 (99..481) | 291 | 64 | 52 (61), 132 (50), 53 (48), 49 (25), 63 (21), 54 (18), 77 (15), 98 (14), 92 (14), 88 (10), 40 (4), 67 (4), +4 more |
| 79105 | 379 (101..484) | 297 | 66 | 53 (51), 67 (37), 49 (34), 54 (31), 88 (30), 52 (29), 92 (20), 132 (16), 71 (8), 77 (8), 98 (7), 40 (6), +6 more |
| 79108 | 385 (104..492) | 300 | 58 | 40 (64), 132 (45), 71 (39), 54 (28), 52 (28), 67 (25), 77 (18), 88 (11), 49 (10), 48 (7), 85 (6), 72 (5), +6 more |
| 79110 | 388 (106..497) | 301 | 61 | 132 (61), 71 (37), 52 (35), 92 (35), 67 (31), 88 (24), 49 (16), 54 (14), 48 (14), 40 (11), 50 (6), 85 (5), +5 more |
| 79111 | 386 (109..500) | 306 | 62 | 48 (65), 71 (49), 72 (42), 40 (30), 52 (28), 67 (25), 132 (19), 64 (14), 49 (10), 92 (6), 85 (5), 54 (4), +5 more |
| 79115 | 421 (111..531) | 329 | 70 | 67 (87), 71 (45), 52 (43), 40 (38), 85 (31), 64 (26), 72 (25), 50 (12), 92 (10), 60 (6), 45 (3), 54 (2), +1 more |
| 79116 | 411 (114..530) | 322 | 68 | 92 (78), 72 (45), 40 (45), 52 (43), 50 (35), 71 (22), 85 (18), 67 (12), 64 (10), 54 (4), 98 (3), 45 (2), +4 more |
| 79122 | 404 (118..532) | 308 | 68 | 50 (100), 67 (70), 52 (28), 85 (25), 64 (22), 72 (18), 40 (12), 92 (12), 63 (8), 88 (4), 98 (3), 45 (2), +3 more |
| 79132 | 391 (120..515) | 308 | 64 | 83 (83), 40 (60), 72 (33), 88 (28), 85 (19), 71 (19), 50 (18), 67 (14), 52 (13), 64 (11), 45 (5), 60 (2), +2 more |
| 79128 | 402 (124..527) | 317 | 66 | 72 (114), 85 (65), 50 (31), 83 (28), 45 (15), 64 (14), 88 (12), 174 (11), 98 (10), 40 (9), 67 (4), 52 (3), +1 more |
| 79134 | 407 (127..533) | 329 | 63 | 85 (94), 50 (55), 83 (53), 64 (37), 98 (24), 63 (23), 67 (20), 45 (10), 72 (5), 60 (3), 40 (3), 174 (1), +1 more |
| 79135 | 409 (129..542) | 326 | 63 | 50 (86), 63 (65), 174 (56), 85 (51), 45 (22), 64 (19), 72 (18), 60 (6), 98 (1), 40 (1), 83 (1) |
| 79139 | 406 (132..537) | 329 | 65 | 63 (140), 174 (71), 72 (49), 40 (26), 71 (14), 60 (11), 64 (7), 83 (6), 45 (5) |
| 79136 | 393 (136..538) | 323 | 59 | 83 (151), 71 (119), 63 (41), 40 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 28; lifespan min/median/max: 63/381/1005; tracks with internal gaps: 11; total internal gaps: 30; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 16)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 826 | 812 | 14 | 14 | 1 | 0 | 78911 |
| 40 | 79..492 | 414 | 356 | 354 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 45 | 84..203 | 120 | 91 | 88 | 3 | 0 | 0 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 87..262 | 176 | 119 | 116 | 3 | 0 | 0 | 3 | 78896, 78969, 78971, 79037, 79045 |
| 48 | 88..500 | 413 | 346 | 342 | 4 | 3 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 49 | 90..484 | 395 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 50 | 91..544 | 454 | 382 | 380 | 2 | 1 | 1 | 1 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 52 | 97..481 | 385 | 353 | 353 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 53 | 97..477 | 381 | 326 | 325 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 99..428 | 330 | 293 | 293 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 60 | 105..167 | 63 | 44 | 42 | 2 | 0 | 0 | 2 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 63 | 107..533 | 427 | 363 | 363 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79122, 79134, 79135, 79136, 79139 |
| 64 | 107..334 | 228 | 170 | 166 | 4 | 2 | 1 | 2 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 67 | 110..535 | 426 | 341 | 338 | 3 | 1 | 1 | 2 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 71 | 114..537 | 424 | 371 | 368 | 3 | 3 | 1 | 0 | 78897, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132, 79136, 79139 |
| 72 | 116..530 | 415 | 356 | 356 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 77 | 123..360 | 238 | 203 | 202 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 82 | 130..460 | 331 | 269 | 269 | 0 | 0 | 0 | 0 | 78896, 78899, 78969, 78971, 79037, 79045, 79097 |
| 83 | 132..527 | 396 | 324 | 324 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 135..438 | 304 | 258 | 257 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 135..531 | 397 | 323 | 323 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 86 | 137..466 | 330 | 275 | 272 | 3 | 1 | 1 | 2 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 141..454 | 314 | 270 | 270 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 92 | 146..532 | 387 | 330 | 329 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134 |
| 98 | 177..445 | 269 | 237 | 237 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79116, 79122, 79128, 79132, 79134, 79135 |
| 132 | 255..495 | 241 | 204 | 204 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 148 | 302..467 | 166 | 143 | 143 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102 |
| 174 | 363..537 | 175 | 140 | 140 | 0 | 0 | 0 | 0 | 79116, 79128, 79134, 79135, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 28; matched pairs: 7994; unmatched reference entries: 2148; unmatched candidate entries: 47
- identity switches: 1168; fragmentation (coverage interruptions): 1634; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 45 -> 40 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 40 -> 45 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 40 -> 46 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 45 -> 40 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 45 -> 40 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 40 -> 49 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 45 -> 40 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79045: 40 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 40 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 45 -> 40 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 40 -> 53 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 50 -> 52 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 50 -> 53 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 40 -> 50 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 53 -> 52 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 52 -> 48 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 45 -> 40 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 45 -> 54 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 48 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 48 -> 49 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 53 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 50 -> 40 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 48 -> 53 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 40 -> 54 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 50 -> 52 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 40 -> 50 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 53 -> 49 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 52 -> 53 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 54 -> 40 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 49 -> 52 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 45 -> 60 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 52 -> 49 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 45 -> 63 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 45 -> 64 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 49 -> 53 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 52 -> 40 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 53 -> 52 at (2019.5, 3034), 3 frames after previous cover
- f110: ref 79097: 40 -> 63 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 45 -> 67 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 40 -> 52 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 50 -> 53 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 63 -> 50 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 60 -> 40 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 64 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 60 at (2113.5, 3026), 5 frames after previous cover
- f111: ref 79110: 67 -> 64 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 45 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 53 -> 46 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 54 -> 40 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 40 -> 63 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 63 -> 54 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 46 -> 48 at (1928, 3035), 3 frames after previous cover
- f114: ref 78897: 52 -> 71 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 53 -> 52 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 48 -> 46 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 50 -> 53 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 40 -> 50 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 40 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 64 -> 60 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 67 -> 64 at (2126, 3027), 2 frames after previous cover
- ... 1108 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 812 | 156 | 0 (812) |
| 78896 | 350 (76..429) | 285 | 49 | 48 (137), 82 (79), 84 (36), 46 (23), 40 (5), 54 (5) |
| 78969 | 352 (80..434) | 282 | 47 | 82 (88), 46 (79), 54 (51), 84 (33), 48 (25), 86 (6) |
| 78971 | 352 (84..439) | 279 | 50 | 54 (77), 84 (62), 92 (39), 49 (28), 82 (25), 53 (22), 48 (10), 46 (8), 86 (4), 40 (3), 45 (1) |
| 79045 | 355 (84..443) | 275 | 61 | 86 (59), 82 (53), 98 (53), 53 (22), 84 (18), 54 (18), 92 (17), 49 (9), 48 (7), 52 (5), 46 (5), 50 (3), +3 more |
| 79037 | 355 (86..445) | 279 | 57 | 86 (79), 98 (68), 84 (21), 53 (15), 49 (15), 82 (13), 77 (12), 92 (12), 48 (11), 88 (9), 52 (8), 54 (5), +4 more |
| 78897 | 345 (89..450) | 269 | 60 | 49 (76), 86 (52), 48 (33), 77 (19), 52 (16), 88 (14), 53 (13), 92 (12), 84 (11), 54 (7), 50 (4), 98 (4), +4 more |
| 78899 | 365 (91..455) | 288 | 60 | 84 (60), 86 (55), 88 (42), 49 (28), 92 (28), 77 (16), 50 (12), 63 (11), 48 (11), 53 (8), 40 (5), 45 (3), +4 more |
| 79097 | 366 (94..461) | 274 | 74 | 148 (51), 49 (45), 88 (36), 63 (31), 77 (16), 84 (15), 98 (14), 86 (14), 53 (12), 82 (9), 40 (8), 92 (8), +6 more |
| 79098 | 360 (97..467) | 273 | 61 | 148 (79), 77 (44), 53 (33), 88 (30), 98 (19), 92 (16), 54 (11), 49 (9), 48 (8), 50 (5), 71 (4), 67 (4), +6 more |
| 79102 | 371 (98..477) | 292 | 62 | 53 (97), 77 (50), 49 (22), 92 (18), 63 (16), 88 (14), 54 (13), 98 (13), 132 (11), 148 (10), 52 (6), 60 (5), +5 more |
| 79103 | 380 (99..481) | 291 | 64 | 52 (61), 132 (50), 53 (48), 49 (25), 63 (21), 54 (18), 77 (15), 98 (14), 92 (14), 88 (10), 40 (4), 67 (4), +4 more |
| 79105 | 379 (101..484) | 297 | 66 | 53 (51), 67 (37), 49 (34), 54 (31), 88 (30), 52 (29), 92 (20), 132 (16), 71 (8), 77 (8), 98 (7), 40 (6), +6 more |
| 79108 | 385 (104..492) | 300 | 58 | 40 (64), 132 (45), 71 (39), 54 (28), 52 (28), 67 (25), 77 (18), 88 (11), 49 (10), 48 (7), 85 (6), 72 (5), +6 more |
| 79110 | 388 (106..497) | 301 | 61 | 132 (61), 71 (37), 52 (35), 92 (35), 67 (31), 88 (24), 49 (16), 54 (14), 48 (14), 40 (11), 50 (6), 85 (5), +5 more |
| 79111 | 386 (109..500) | 306 | 62 | 48 (65), 71 (49), 72 (42), 40 (30), 52 (28), 67 (25), 132 (19), 64 (14), 49 (10), 92 (6), 85 (5), 54 (4), +5 more |
| 79115 | 421 (111..531) | 329 | 70 | 67 (87), 71 (45), 52 (43), 40 (38), 85 (31), 64 (26), 72 (25), 50 (12), 92 (10), 60 (6), 45 (3), 54 (2), +1 more |
| 79116 | 411 (114..530) | 322 | 68 | 92 (78), 72 (45), 40 (45), 52 (43), 50 (35), 71 (22), 85 (18), 67 (12), 64 (10), 54 (4), 98 (3), 45 (2), +4 more |
| 79122 | 404 (118..532) | 308 | 68 | 50 (100), 67 (70), 52 (28), 85 (25), 64 (22), 72 (18), 40 (12), 92 (12), 63 (8), 88 (4), 98 (3), 45 (2), +3 more |
| 79132 | 391 (120..515) | 308 | 64 | 83 (83), 40 (60), 72 (33), 88 (28), 85 (19), 71 (19), 50 (18), 67 (14), 52 (13), 64 (11), 45 (5), 60 (2), +2 more |
| 79128 | 402 (124..527) | 317 | 66 | 72 (114), 85 (65), 50 (31), 83 (28), 45 (15), 64 (14), 88 (12), 174 (11), 98 (10), 40 (9), 67 (4), 52 (3), +1 more |
| 79134 | 407 (127..533) | 329 | 63 | 85 (94), 50 (55), 83 (53), 64 (37), 98 (24), 63 (23), 67 (20), 45 (10), 72 (5), 60 (3), 40 (3), 174 (1), +1 more |
| 79135 | 409 (129..542) | 326 | 63 | 50 (86), 63 (65), 174 (56), 85 (51), 45 (22), 64 (19), 72 (18), 60 (6), 98 (1), 40 (1), 83 (1) |
| 79139 | 406 (132..537) | 329 | 65 | 63 (140), 174 (71), 72 (49), 40 (26), 71 (14), 60 (11), 64 (7), 83 (6), 45 (5) |
| 79136 | 393 (136..538) | 323 | 59 | 83 (151), 71 (119), 63 (41), 40 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 28; lifespan min/median/max: 63/381/1005; tracks with internal gaps: 11; total internal gaps: 30; longest internal gap: 2; tracks ending in coasting: 8 (trailing rows total 16)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 826 | 812 | 14 | 14 | 1 | 0 | 78911 |
| 40 | 79..492 | 414 | 356 | 354 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 45 | 84..203 | 120 | 91 | 88 | 3 | 0 | 0 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 87..262 | 176 | 119 | 116 | 3 | 0 | 0 | 3 | 78896, 78969, 78971, 79037, 79045 |
| 48 | 88..500 | 413 | 346 | 342 | 4 | 3 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 49 | 90..484 | 395 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 50 | 91..544 | 454 | 382 | 380 | 2 | 1 | 1 | 1 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 52 | 97..481 | 385 | 353 | 353 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 53 | 97..477 | 381 | 326 | 325 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 99..428 | 330 | 293 | 293 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 60 | 105..167 | 63 | 44 | 42 | 2 | 0 | 0 | 2 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 63 | 107..533 | 427 | 363 | 363 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79122, 79134, 79135, 79136, 79139 |
| 64 | 107..334 | 228 | 170 | 166 | 4 | 2 | 1 | 2 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 67 | 110..535 | 426 | 341 | 338 | 3 | 1 | 1 | 2 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 71 | 114..537 | 424 | 371 | 368 | 3 | 3 | 1 | 0 | 78897, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132, 79136, 79139 |
| 72 | 116..530 | 415 | 356 | 356 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 77 | 123..360 | 238 | 203 | 202 | 1 | 0 | 0 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 82 | 130..460 | 331 | 269 | 269 | 0 | 0 | 0 | 0 | 78896, 78899, 78969, 78971, 79037, 79045, 79097 |
| 83 | 132..527 | 396 | 324 | 324 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 135..438 | 304 | 258 | 257 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 135..531 | 397 | 323 | 323 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 86 | 137..466 | 330 | 275 | 272 | 3 | 1 | 1 | 2 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 141..454 | 314 | 270 | 270 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 92 | 146..532 | 387 | 330 | 329 | 1 | 1 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134 |
| 98 | 177..445 | 269 | 237 | 237 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79116, 79122, 79128, 79132, 79134, 79135 |
| 132 | 255..495 | 241 | 204 | 204 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 148 | 302..467 | 166 | 143 | 143 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102 |
| 174 | 363..537 | 175 | 140 | 140 | 0 | 0 | 0 | 0 | 79116, 79128, 79134, 79135, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 28; matched pairs: 9090; unmatched reference entries: 1052; unmatched candidate entries: 1298
- identity switches: 1162; fragmentation (coverage interruptions): 788; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 45 -> 40 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 40 -> 45 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 40 -> 46 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 45 -> 40 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 45 -> 40 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 40 -> 49 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 45 -> 40 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 40 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 40 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 45 -> 40 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 40 -> 53 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 50 -> 52 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 50 -> 53 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 40 -> 50 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 53 -> 52 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 52 -> 48 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 45 -> 40 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 45 -> 54 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 48 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 48 -> 49 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 53 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 50 -> 40 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 48 -> 53 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 40 -> 54 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 50 -> 52 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 40 -> 50 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 53 -> 49 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 52 -> 53 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 54 -> 40 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 49 -> 52 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 45 -> 60 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 52 -> 49 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 45 -> 63 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 45 -> 64 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 49 -> 53 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 52 -> 40 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 53 -> 52 at (2019.5, 3034), 2 frames after previous cover
- f110: ref 79097: 40 -> 63 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 45 -> 67 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 40 -> 52 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 50 -> 53 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 63 -> 50 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 60 -> 40 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 64 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 60 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 67 -> 64 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 45 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 53 -> 46 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 54 -> 40 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 40 -> 63 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 63 -> 54 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 46 -> 48 at (1928, 3035), 2 frames after previous cover
- f114: ref 78897: 52 -> 71 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 53 -> 52 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 48 -> 46 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 50 -> 53 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 40 -> 50 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 40 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 64 -> 60 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 67 -> 64 at (2126, 3027), 1 frames after previous cover
- ... 1102 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 24 | 0 (978) |
| 78896 | 350 (76..429) | 322 | 18 | 48 (158), 82 (87), 84 (40), 46 (25), 54 (7), 40 (5) |
| 78969 | 352 (80..434) | 315 | 24 | 82 (104), 46 (84), 54 (56), 84 (38), 48 (27), 86 (6) |
| 78971 | 352 (84..439) | 312 | 28 | 54 (84), 84 (70), 92 (48), 49 (32), 82 (28), 53 (23), 48 (10), 46 (9), 86 (4), 40 (3), 45 (1) |
| 79045 | 355 (84..443) | 312 | 30 | 98 (66), 82 (63), 86 (63), 53 (23), 54 (20), 84 (19), 92 (18), 49 (11), 48 (9), 52 (5), 46 (5), 50 (3), +3 more |
| 79037 | 355 (86..445) | 306 | 36 | 86 (87), 98 (73), 84 (24), 53 (17), 49 (17), 82 (14), 77 (13), 92 (13), 48 (13), 52 (9), 88 (9), 71 (5), +4 more |
| 78897 | 345 (89..450) | 301 | 32 | 49 (87), 86 (60), 48 (34), 77 (20), 52 (16), 53 (15), 88 (15), 92 (13), 84 (12), 54 (9), 98 (6), 50 (5), +4 more |
| 78899 | 365 (91..455) | 328 | 30 | 84 (72), 86 (63), 88 (47), 49 (33), 92 (31), 77 (19), 48 (13), 50 (12), 63 (12), 53 (9), 40 (5), 45 (3), +4 more |
| 79097 | 366 (94..461) | 309 | 44 | 148 (58), 49 (51), 88 (44), 63 (36), 86 (17), 77 (17), 84 (16), 98 (15), 53 (11), 82 (11), 40 (10), 92 (8), +6 more |
| 79098 | 360 (97..467) | 301 | 41 | 148 (88), 77 (47), 53 (37), 88 (34), 98 (21), 92 (17), 54 (13), 49 (9), 48 (9), 50 (6), 71 (4), 67 (4), +6 more |
| 79102 | 371 (98..477) | 322 | 38 | 53 (109), 77 (61), 49 (25), 92 (18), 63 (17), 88 (14), 54 (13), 98 (13), 148 (12), 132 (11), 60 (6), 52 (6), +5 more |
| 79103 | 380 (99..481) | 323 | 41 | 52 (63), 132 (59), 53 (55), 49 (28), 63 (23), 54 (19), 77 (18), 98 (15), 92 (15), 88 (12), 40 (4), 67 (4), +4 more |
| 79105 | 379 (101..484) | 337 | 36 | 53 (61), 67 (41), 49 (38), 88 (37), 54 (34), 52 (32), 92 (20), 132 (18), 71 (9), 77 (9), 63 (8), 40 (7), +6 more |
| 79108 | 385 (104..492) | 328 | 38 | 40 (75), 132 (48), 71 (42), 54 (30), 52 (28), 67 (26), 77 (18), 49 (12), 88 (11), 48 (9), 85 (7), 72 (6), +6 more |
| 79110 | 388 (106..497) | 342 | 35 | 132 (74), 71 (41), 92 (41), 52 (39), 67 (34), 88 (27), 49 (18), 54 (17), 48 (14), 40 (12), 50 (6), 60 (5), +5 more |
| 79111 | 386 (109..500) | 348 | 27 | 48 (83), 71 (52), 72 (47), 40 (32), 52 (31), 67 (27), 132 (21), 64 (17), 49 (12), 85 (6), 92 (6), 54 (5), +4 more |
| 79115 | 421 (111..531) | 380 | 32 | 67 (112), 71 (52), 52 (46), 40 (42), 85 (31), 72 (30), 64 (27), 92 (16), 50 (11), 60 (7), 45 (3), 54 (2), +1 more |
| 79116 | 411 (114..530) | 358 | 39 | 92 (95), 72 (49), 40 (48), 52 (45), 50 (38), 71 (23), 85 (18), 67 (14), 64 (12), 45 (4), 54 (4), 98 (3), +4 more |
| 79122 | 404 (118..532) | 350 | 39 | 50 (119), 67 (81), 85 (33), 52 (32), 64 (23), 72 (19), 40 (10), 63 (10), 92 (8), 88 (5), 45 (3), 98 (3), +3 more |
| 79132 | 391 (120..515) | 346 | 35 | 83 (97), 40 (70), 72 (35), 88 (31), 85 (24), 71 (20), 50 (18), 67 (15), 52 (13), 64 (12), 45 (5), 54 (3), +2 more |
| 79128 | 402 (124..527) | 362 | 31 | 72 (137), 85 (74), 50 (35), 83 (28), 45 (18), 64 (15), 88 (14), 174 (12), 98 (10), 40 (9), 67 (6), 52 (3), +1 more |
| 79134 | 407 (127..533) | 370 | 31 | 85 (112), 50 (62), 83 (59), 64 (38), 98 (26), 63 (25), 67 (21), 45 (12), 72 (6), 60 (4), 40 (3), 174 (1), +1 more |
| 79135 | 409 (129..542) | 378 | 23 | 50 (100), 63 (75), 174 (68), 85 (58), 45 (24), 64 (23), 72 (19), 60 (7), 71 (2), 98 (1), 83 (1) |
| 79139 | 406 (132..537) | 385 | 20 | 63 (144), 174 (70), 72 (54), 71 (51), 40 (29), 60 (13), 64 (8), 45 (7), 83 (6), 92 (2), 85 (1) |
| 79136 | 393 (136..538) | 377 | 16 | 83 (178), 71 (96), 63 (69), 174 (18), 40 (16) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 28; lifespan min/median/max: 92/410/1006; tracks with internal gaps: 28; total internal gaps: 285; longest internal gap: 11; tracks ending in coasting: 27 (trailing rows total 911)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 978 | 28 | 24 | 2 | 0 | 78911 |
| 40 | 79..521 | 443 | 443 | 392 | 51 | 11 | 7 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 45 | 84..232 | 149 | 149 | 102 | 47 | 2 | 1 | 45 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 87..291 | 205 | 205 | 124 | 81 | 1 | 1 | 80 | 78896, 78969, 78971, 79037, 79045 |
| 48 | 88..529 | 442 | 442 | 393 | 49 | 11 | 6 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 49 | 90..513 | 424 | 424 | 374 | 50 | 17 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 50 | 91..573 | 483 | 483 | 429 | 54 | 16 | 3 | 34 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 52 | 97..510 | 414 | 414 | 375 | 39 | 7 | 1 | 32 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 53 | 97..506 | 410 | 410 | 364 | 46 | 18 | 2 | 25 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 99..457 | 359 | 359 | 324 | 35 | 7 | 1 | 28 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 60 | 105..196 | 92 | 92 | 50 | 42 | 2 | 1 | 40 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 63 | 107..562 | 456 | 456 | 421 | 35 | 6 | 1 | 29 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79122, 79134, 79135, 79136, 79139 |
| 64 | 107..363 | 257 | 257 | 182 | 75 | 10 | 9 | 55 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 67 | 110..564 | 455 | 455 | 390 | 65 | 12 | 2 | 50 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 71 | 114..566 | 453 | 453 | 405 | 48 | 17 | 6 | 24 | 78897, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132, 79135, 79136, 79139 |
| 72 | 116..559 | 444 | 444 | 404 | 40 | 9 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 77 | 123..389 | 267 | 267 | 227 | 40 | 6 | 3 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 82 | 130..489 | 360 | 360 | 310 | 50 | 15 | 3 | 28 | 78896, 78899, 78969, 78971, 79037, 79045, 79097 |
| 83 | 132..556 | 425 | 425 | 371 | 54 | 17 | 6 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 135..467 | 333 | 333 | 292 | 41 | 9 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 135..560 | 426 | 426 | 374 | 52 | 13 | 11 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 86 | 137..495 | 359 | 359 | 303 | 56 | 9 | 3 | 45 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 141..483 | 343 | 343 | 307 | 36 | 7 | 2 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 92 | 146..561 | 416 | 416 | 373 | 43 | 14 | 4 | 24 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79139 |
| 98 | 177..474 | 298 | 298 | 261 | 37 | 8 | 1 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79116, 79122, 79128, 79132, 79134, 79135 |
| 132 | 255..524 | 270 | 270 | 234 | 36 | 7 | 3 | 27 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 148 | 302..496 | 195 | 195 | 161 | 34 | 5 | 1 | 29 | 78899, 79097, 79098, 79102 |
| 174 | 363..566 | 204 | 204 | 170 | 34 | 5 | 2 | 28 | 79116, 79128, 79134, 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 28; matched pairs: 9090; unmatched reference entries: 1052; unmatched candidate entries: 1298
- identity switches: 1162; fragmentation (coverage interruptions): 788; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 45 -> 40 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 40 -> 45 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 40 -> 46 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 45 -> 40 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 45 -> 40 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 40 -> 49 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 45 -> 40 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 40 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 40 -> 50 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 45 -> 40 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 40 -> 53 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 50 -> 52 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 50 -> 53 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 40 -> 50 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 53 -> 52 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 52 -> 48 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 45 -> 40 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 45 -> 54 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 49 -> 48 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 48 -> 49 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 53 -> 50 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 50 -> 40 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 48 -> 53 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 40 -> 54 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 50 -> 52 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 40 -> 50 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 53 -> 49 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 52 -> 53 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 54 -> 40 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 49 -> 52 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 45 -> 60 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 52 -> 49 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 45 -> 63 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 45 -> 64 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 49 -> 53 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 52 -> 40 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 53 -> 52 at (2019.5, 3034), 2 frames after previous cover
- f110: ref 79097: 40 -> 63 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 45 -> 67 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 40 -> 52 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 50 -> 53 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 63 -> 50 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 60 -> 40 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 64 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 45 -> 60 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 67 -> 64 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 45 -> 67 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 53 -> 46 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 54 -> 40 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 40 -> 63 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 63 -> 54 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 46 -> 48 at (1928, 3035), 2 frames after previous cover
- f114: ref 78897: 52 -> 71 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 53 -> 52 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 48 -> 46 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 50 -> 53 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 40 -> 50 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 40 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 64 -> 60 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 67 -> 64 at (2126, 3027), 1 frames after previous cover
- ... 1102 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 24 | 0 (978) |
| 78896 | 350 (76..429) | 322 | 18 | 48 (158), 82 (87), 84 (40), 46 (25), 54 (7), 40 (5) |
| 78969 | 352 (80..434) | 315 | 24 | 82 (104), 46 (84), 54 (56), 84 (38), 48 (27), 86 (6) |
| 78971 | 352 (84..439) | 312 | 28 | 54 (84), 84 (70), 92 (48), 49 (32), 82 (28), 53 (23), 48 (10), 46 (9), 86 (4), 40 (3), 45 (1) |
| 79045 | 355 (84..443) | 312 | 30 | 98 (66), 82 (63), 86 (63), 53 (23), 54 (20), 84 (19), 92 (18), 49 (11), 48 (9), 52 (5), 46 (5), 50 (3), +3 more |
| 79037 | 355 (86..445) | 306 | 36 | 86 (87), 98 (73), 84 (24), 53 (17), 49 (17), 82 (14), 77 (13), 92 (13), 48 (13), 52 (9), 88 (9), 71 (5), +4 more |
| 78897 | 345 (89..450) | 301 | 32 | 49 (87), 86 (60), 48 (34), 77 (20), 52 (16), 53 (15), 88 (15), 92 (13), 84 (12), 54 (9), 98 (6), 50 (5), +4 more |
| 78899 | 365 (91..455) | 328 | 30 | 84 (72), 86 (63), 88 (47), 49 (33), 92 (31), 77 (19), 48 (13), 50 (12), 63 (12), 53 (9), 40 (5), 45 (3), +4 more |
| 79097 | 366 (94..461) | 309 | 44 | 148 (58), 49 (51), 88 (44), 63 (36), 86 (17), 77 (17), 84 (16), 98 (15), 53 (11), 82 (11), 40 (10), 92 (8), +6 more |
| 79098 | 360 (97..467) | 301 | 41 | 148 (88), 77 (47), 53 (37), 88 (34), 98 (21), 92 (17), 54 (13), 49 (9), 48 (9), 50 (6), 71 (4), 67 (4), +6 more |
| 79102 | 371 (98..477) | 322 | 38 | 53 (109), 77 (61), 49 (25), 92 (18), 63 (17), 88 (14), 54 (13), 98 (13), 148 (12), 132 (11), 60 (6), 52 (6), +5 more |
| 79103 | 380 (99..481) | 323 | 41 | 52 (63), 132 (59), 53 (55), 49 (28), 63 (23), 54 (19), 77 (18), 98 (15), 92 (15), 88 (12), 40 (4), 67 (4), +4 more |
| 79105 | 379 (101..484) | 337 | 36 | 53 (61), 67 (41), 49 (38), 88 (37), 54 (34), 52 (32), 92 (20), 132 (18), 71 (9), 77 (9), 63 (8), 40 (7), +6 more |
| 79108 | 385 (104..492) | 328 | 38 | 40 (75), 132 (48), 71 (42), 54 (30), 52 (28), 67 (26), 77 (18), 49 (12), 88 (11), 48 (9), 85 (7), 72 (6), +6 more |
| 79110 | 388 (106..497) | 342 | 35 | 132 (74), 71 (41), 92 (41), 52 (39), 67 (34), 88 (27), 49 (18), 54 (17), 48 (14), 40 (12), 50 (6), 60 (5), +5 more |
| 79111 | 386 (109..500) | 348 | 27 | 48 (83), 71 (52), 72 (47), 40 (32), 52 (31), 67 (27), 132 (21), 64 (17), 49 (12), 85 (6), 92 (6), 54 (5), +4 more |
| 79115 | 421 (111..531) | 380 | 32 | 67 (112), 71 (52), 52 (46), 40 (42), 85 (31), 72 (30), 64 (27), 92 (16), 50 (11), 60 (7), 45 (3), 54 (2), +1 more |
| 79116 | 411 (114..530) | 358 | 39 | 92 (95), 72 (49), 40 (48), 52 (45), 50 (38), 71 (23), 85 (18), 67 (14), 64 (12), 45 (4), 54 (4), 98 (3), +4 more |
| 79122 | 404 (118..532) | 350 | 39 | 50 (119), 67 (81), 85 (33), 52 (32), 64 (23), 72 (19), 40 (10), 63 (10), 92 (8), 88 (5), 45 (3), 98 (3), +3 more |
| 79132 | 391 (120..515) | 346 | 35 | 83 (97), 40 (70), 72 (35), 88 (31), 85 (24), 71 (20), 50 (18), 67 (15), 52 (13), 64 (12), 45 (5), 54 (3), +2 more |
| 79128 | 402 (124..527) | 362 | 31 | 72 (137), 85 (74), 50 (35), 83 (28), 45 (18), 64 (15), 88 (14), 174 (12), 98 (10), 40 (9), 67 (6), 52 (3), +1 more |
| 79134 | 407 (127..533) | 370 | 31 | 85 (112), 50 (62), 83 (59), 64 (38), 98 (26), 63 (25), 67 (21), 45 (12), 72 (6), 60 (4), 40 (3), 174 (1), +1 more |
| 79135 | 409 (129..542) | 378 | 23 | 50 (100), 63 (75), 174 (68), 85 (58), 45 (24), 64 (23), 72 (19), 60 (7), 71 (2), 98 (1), 83 (1) |
| 79139 | 406 (132..537) | 385 | 20 | 63 (144), 174 (70), 72 (54), 71 (51), 40 (29), 60 (13), 64 (8), 45 (7), 83 (6), 92 (2), 85 (1) |
| 79136 | 393 (136..538) | 377 | 16 | 83 (178), 71 (96), 63 (69), 174 (18), 40 (16) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 28; lifespan min/median/max: 92/410/1006; tracks with internal gaps: 28; total internal gaps: 285; longest internal gap: 11; tracks ending in coasting: 27 (trailing rows total 911)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 978 | 28 | 24 | 2 | 0 | 78911 |
| 40 | 79..521 | 443 | 443 | 392 | 51 | 11 | 7 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 45 | 84..232 | 149 | 149 | 102 | 47 | 2 | 1 | 45 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 46 | 87..291 | 205 | 205 | 124 | 81 | 1 | 1 | 80 | 78896, 78969, 78971, 79037, 79045 |
| 48 | 88..529 | 442 | 442 | 393 | 49 | 11 | 6 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 49 | 90..513 | 424 | 424 | 374 | 50 | 17 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 50 | 91..573 | 483 | 483 | 429 | 54 | 16 | 3 | 34 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 52 | 97..510 | 414 | 414 | 375 | 39 | 7 | 1 | 32 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 53 | 97..506 | 410 | 410 | 364 | 46 | 18 | 2 | 25 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 99..457 | 359 | 359 | 324 | 35 | 7 | 1 | 28 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 60 | 105..196 | 92 | 92 | 50 | 42 | 2 | 1 | 40 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 63 | 107..562 | 456 | 456 | 421 | 35 | 6 | 1 | 29 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79122, 79134, 79135, 79136, 79139 |
| 64 | 107..363 | 257 | 257 | 182 | 75 | 10 | 9 | 55 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 67 | 110..564 | 455 | 455 | 390 | 65 | 12 | 2 | 50 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 71 | 114..566 | 453 | 453 | 405 | 48 | 17 | 6 | 24 | 78897, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132, 79135, 79136, 79139 |
| 72 | 116..559 | 444 | 444 | 404 | 40 | 9 | 2 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 77 | 123..389 | 267 | 267 | 227 | 40 | 6 | 3 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 82 | 130..489 | 360 | 360 | 310 | 50 | 15 | 3 | 28 | 78896, 78899, 78969, 78971, 79037, 79045, 79097 |
| 83 | 132..556 | 425 | 425 | 371 | 54 | 17 | 6 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 84 | 135..467 | 333 | 333 | 292 | 41 | 9 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 85 | 135..560 | 426 | 426 | 374 | 52 | 13 | 11 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 86 | 137..495 | 359 | 359 | 303 | 56 | 9 | 3 | 45 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 88 | 141..483 | 343 | 343 | 307 | 36 | 7 | 2 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 92 | 146..561 | 416 | 416 | 373 | 43 | 14 | 4 | 24 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79139 |
| 98 | 177..474 | 298 | 298 | 261 | 37 | 8 | 1 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79116, 79122, 79128, 79132, 79134, 79135 |
| 132 | 255..524 | 270 | 270 | 234 | 36 | 7 | 3 | 27 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 148 | 302..496 | 195 | 195 | 161 | 34 | 5 | 1 | 29 | 78899, 79097, 79098, 79102 |
| 174 | 363..566 | 204 | 204 | 170 | 34 | 5 | 2 | 28 | 79116, 79128, 79134, 79135, 79136, 79139 |
