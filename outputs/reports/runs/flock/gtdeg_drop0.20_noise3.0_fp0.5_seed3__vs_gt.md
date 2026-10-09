# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=dd3e2a7dd43f
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise3.0_fp0.5_seed3/tracks.csv sha256=02bd6a27f1d0e0a4
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise3.0_fp0.5_seed3.csv sha256=dd3e2a7dd43f4bcd
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise3.0_fp0.5_seed3
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
| observations | none | 4 | 10142 | 8128 | 0.163 | 0.362 | 0.074 | 2.18 | 0.162 | 0.022 | 2.39 | 1137 | 2524.0 | 0.171 | 0.192 | 0.154 | 0.468 | 0.584 | 4746 | 5396 | 3382 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 8128 | 0.225 | 0.502 | 0.101 | 2.72 | 0.275 | 0.439 | 3.21 | 1469 | 2138.0 | 0.255 | 0.287 | 0.230 | 0.692 | 0.864 | 7023 | 3119 | 1105 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 8128 | 0.258 | 0.573 | 0.116 | 3.03 | 0.325 | 0.588 | 3.61 | 1528 | 1786.0 | 0.288 | 0.323 | 0.259 | 0.770 | 0.961 | 7810 | 2332 | 318 | 4 | 21 | 0 |
| observations | none | 12 | 10142 | 8128 | 0.291 | 0.630 | 0.134 | 3.50 | 0.344 | 0.636 | 3.99 | 1394 | 1612.0 | 0.314 | 0.353 | 0.283 | 0.788 | 0.983 | 7987 | 2155 | 141 | 8 | 17 | 0 |
| observations | ignore | 4 | 10142 | 8128 | 0.163 | 0.362 | 0.074 | 2.18 | 0.162 | 0.022 | 2.39 | 1137 | 2524.0 | 0.171 | 0.192 | 0.154 | 0.468 | 0.584 | 4746 | 5396 | 3382 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 8128 | 0.225 | 0.502 | 0.101 | 2.72 | 0.275 | 0.439 | 3.21 | 1469 | 2138.0 | 0.255 | 0.287 | 0.230 | 0.692 | 0.864 | 7023 | 3119 | 1105 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 8128 | 0.258 | 0.573 | 0.116 | 3.03 | 0.325 | 0.588 | 3.61 | 1528 | 1786.0 | 0.288 | 0.323 | 0.259 | 0.770 | 0.961 | 7810 | 2332 | 318 | 4 | 21 | 0 |
| observations | ignore | 12 | 10142 | 8128 | 0.291 | 0.630 | 0.134 | 3.50 | 0.344 | 0.636 | 3.99 | 1394 | 1612.0 | 0.314 | 0.353 | 0.283 | 0.788 | 0.983 | 7987 | 2155 | 141 | 8 | 17 | 0 |
| updates | none | 4 | 10142 | 10365 | 0.164 | 0.340 | 0.079 | 2.21 | 0.158 | -0.143 | 2.40 | 1190 | 2496.0 | 0.164 | 0.162 | 0.166 | 0.498 | 0.487 | 5052 | 5090 | 5313 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10365 | 0.234 | 0.486 | 0.112 | 2.81 | 0.277 | 0.324 | 3.25 | 1510 | 1851.0 | 0.250 | 0.247 | 0.253 | 0.748 | 0.732 | 7582 | 2560 | 2783 | 1 | 24 | 0 |
| updates | none | 8 | 10142 | 10365 | 0.273 | 0.565 | 0.132 | 3.18 | 0.340 | 0.526 | 3.73 | 1540 | 1240.0 | 0.291 | 0.288 | 0.294 | 0.850 | 0.832 | 8620 | 1522 | 1745 | 22 | 3 | 0 |
| updates | none | 12 | 10142 | 10365 | 0.315 | 0.637 | 0.155 | 3.73 | 0.375 | 0.627 | 4.25 | 1361 | 861.0 | 0.328 | 0.325 | 0.332 | 0.892 | 0.872 | 9043 | 1099 | 1322 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10365 | 0.164 | 0.340 | 0.079 | 2.21 | 0.158 | -0.143 | 2.40 | 1190 | 2496.0 | 0.164 | 0.162 | 0.166 | 0.498 | 0.487 | 5052 | 5090 | 5313 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10365 | 0.234 | 0.486 | 0.112 | 2.81 | 0.277 | 0.324 | 3.25 | 1510 | 1851.0 | 0.250 | 0.247 | 0.253 | 0.748 | 0.732 | 7582 | 2560 | 2783 | 1 | 24 | 0 |
| updates | ignore | 8 | 10142 | 10365 | 0.273 | 0.565 | 0.132 | 3.18 | 0.340 | 0.526 | 3.73 | 1540 | 1240.0 | 0.291 | 0.288 | 0.294 | 0.850 | 0.832 | 8620 | 1522 | 1745 | 22 | 3 | 0 |
| updates | ignore | 12 | 10142 | 10365 | 0.315 | 0.637 | 0.155 | 3.73 | 0.375 | 0.627 | 4.25 | 1361 | 861.0 | 0.328 | 0.325 | 0.332 | 0.892 | 0.872 | 9043 | 1099 | 1322 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 7810; unmatched reference entries: 2332; unmatched candidate entries: 318
- identity switches: 1528; fragmentation (coverage interruptions): 1788; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 49 -> 52 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 42 -> 54 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78897: 53 -> 56 at (2125, 3030), 2 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 49 -> 53 at (2100.5, 3033), 2 frames after previous cover
- f95: ref 78897: 56 -> 52 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 53 -> 52 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 53 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 56 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 52 -> 54 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 52 -> 59 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 49 -> 42 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 52 -> 49 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 52 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 56 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 54 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 54 -> 59 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 59 -> 49 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 59 -> 54 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 49 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 54 -> 61 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 52 -> 59 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 52 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 56 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 61 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 49 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 53 -> 52 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 56 -> 53 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 42 -> 61 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 61 -> 42 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 56 -> 53 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 61 -> 60 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 49 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 61 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 52 -> 59 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 59 -> 54 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79103: 53 -> 52 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 49 -> 42 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 59 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 52 -> 59 at (2096.5, 3027.5), 2 frames after previous cover
- f108: ref 79105: 53 -> 56 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 54 -> 49 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 64 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 54 -> 49 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 42 -> 61 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 49 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 54 -> 52 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 52 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 52 -> 59 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 53 -> 56 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 64 -> 53 at (2129, 3027), 3 frames after previous cover
- ... 1468 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 779 | 180 | 5 (779) |
| 78896 | 350 (76..429) | 266 | 61 | 81 (102), 101 (63), 94 (46), 191 (18), 65 (11), 74 (10), 42 (7), 54 (6), 60 (3) |
| 78969 | 352 (80..434) | 243 | 73 | 94 (94), 60 (39), 81 (39), 101 (26), 74 (14), 42 (11), 65 (8), 87 (4), 166 (3), 61 (2), 49 (1), 91 (1), +1 more |
| 78971 | 352 (84..439) | 274 | 63 | 87 (87), 64 (49), 60 (33), 65 (24), 81 (21), 166 (21), 49 (8), 42 (7), 101 (7), 74 (6), 94 (5), 78 (4), +2 more |
| 79045 | 355 (84..443) | 270 | 61 | 65 (108), 74 (50), 64 (28), 87 (27), 81 (20), 60 (10), 78 (7), 61 (5), 49 (3), 54 (3), 91 (3), 52 (2), +4 more |
| 79037 | 355 (86..445) | 267 | 65 | 74 (72), 81 (51), 91 (38), 65 (27), 87 (16), 64 (14), 60 (9), 166 (9), 61 (7), 49 (6), 78 (5), 52 (4), +3 more |
| 78897 | 345 (89..450) | 257 | 65 | 65 (91), 166 (35), 61 (26), 64 (26), 74 (18), 81 (16), 60 (9), 42 (8), 101 (6), 91 (5), 49 (4), 87 (4), +6 more |
| 78899 | 365 (91..455) | 278 | 68 | 61 (90), 74 (47), 54 (23), 91 (23), 65 (17), 101 (15), 64 (14), 81 (12), 42 (9), 60 (7), 166 (5), 87 (4), +7 more |
| 79097 | 366 (94..461) | 284 | 70 | 91 (56), 64 (55), 61 (46), 77 (24), 78 (21), 87 (16), 74 (16), 54 (15), 42 (7), 60 (7), 101 (5), 52 (4), +6 more |
| 79098 | 360 (97..467) | 289 | 55 | 91 (42), 60 (28), 71 (28), 54 (25), 77 (25), 101 (24), 64 (21), 78 (20), 87 (16), 166 (16), 74 (15), 42 (11), +6 more |
| 79102 | 371 (98..477) | 280 | 68 | 60 (60), 77 (41), 54 (36), 71 (29), 78 (21), 101 (20), 91 (16), 74 (11), 42 (9), 87 (7), 52 (5), 49 (5), +7 more |
| 79103 | 380 (99..481) | 301 | 60 | 78 (78), 60 (61), 101 (34), 54 (29), 77 (23), 87 (20), 71 (13), 42 (10), 52 (8), 49 (6), 166 (5), 64 (4), +6 more |
| 79105 | 379 (101..484) | 288 | 71 | 87 (61), 101 (40), 54 (32), 78 (30), 42 (29), 60 (21), 52 (19), 71 (16), 56 (7), 64 (7), 77 (5), 91 (5), +8 more |
| 79108 | 385 (104..492) | 309 | 65 | 54 (52), 97 (35), 78 (30), 52 (29), 91 (22), 101 (20), 77 (18), 144 (17), 56 (14), 85 (14), 87 (14), 176 (11), +8 more |
| 79110 | 388 (106..497) | 316 | 57 | 52 (51), 144 (42), 97 (41), 54 (36), 64 (29), 85 (26), 176 (23), 84 (11), 56 (10), 78 (9), 49 (8), 91 (8), +6 more |
| 79111 | 386 (109..500) | 289 | 74 | 52 (60), 85 (56), 176 (46), 78 (25), 97 (19), 56 (18), 64 (17), 77 (11), 54 (10), 71 (7), 144 (6), 84 (4), +3 more |
| 79115 | 421 (111..531) | 320 | 79 | 97 (65), 56 (60), 84 (36), 85 (32), 144 (26), 42 (19), 54 (18), 176 (16), 77 (11), 78 (11), 52 (6), 53 (5), +4 more |
| 79116 | 411 (114..530) | 313 | 73 | 85 (84), 56 (70), 84 (50), 77 (31), 144 (14), 176 (11), 54 (10), 78 (10), 97 (7), 49 (6), 42 (6), 64 (4), +4 more |
| 79122 | 404 (118..532) | 294 | 77 | 84 (116), 77 (43), 85 (30), 78 (23), 144 (15), 52 (12), 54 (11), 56 (8), 176 (8), 71 (6), 49 (6), 97 (6), +4 more |
| 79132 | 391 (120..515) | 303 | 70 | 52 (67), 56 (37), 144 (36), 84 (33), 85 (31), 78 (31), 77 (17), 54 (16), 42 (16), 49 (6), 64 (4), 97 (4), +2 more |
| 79128 | 402 (124..527) | 325 | 68 | 56 (52), 42 (50), 84 (46), 85 (38), 97 (33), 52 (31), 176 (18), 49 (15), 71 (13), 54 (13), 77 (10), 64 (3), +2 more |
| 79134 | 407 (127..533) | 312 | 73 | 71 (62), 49 (59), 97 (57), 56 (52), 84 (16), 52 (14), 144 (13), 77 (11), 54 (8), 42 (8), 53 (7), 59 (3), +1 more |
| 79135 | 409 (129..542) | 323 | 62 | 71 (84), 49 (67), 97 (57), 53 (33), 42 (32), 52 (26), 56 (20), 54 (2), 77 (2) |
| 79139 | 406 (132..537) | 323 | 65 | 49 (119), 53 (61), 144 (43), 42 (36), 52 (24), 71 (17), 56 (9), 84 (8), 59 (6) |
| 79136 | 393 (136..538) | 307 | 65 | 53 (152), 42 (47), 49 (37), 85 (34), 71 (11), 59 (10), 77 (7), 56 (3), 84 (3), 97 (2), 144 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 303 | 718..718 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 1/344/1004; tracks with internal gaps: 26; total internal gaps: 283; longest internal gap: 3; tracks ending in coasting: 11 (trailing rows total 19)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 817 | 779 | 38 | 35 | 3 | 0 | 78911 |
| 42 | 78..479 | 402 | 359 | 345 | 14 | 12 | 2 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 84..533 | 450 | 393 | 377 | 16 | 16 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 88..527 | 440 | 386 | 370 | 16 | 16 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..457 | 370 | 308 | 289 | 19 | 17 | 1 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..497 | 409 | 361 | 346 | 15 | 15 | 1 | 0 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 91..530 | 440 | 389 | 374 | 15 | 13 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 98..162 | 65 | 54 | 53 | 1 | 0 | 0 | 1 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 60 | 101..434 | 334 | 296 | 290 | 6 | 6 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 101..321 | 221 | 198 | 187 | 11 | 8 | 1 | 3 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 64 | 106..459 | 354 | 299 | 293 | 6 | 6 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..450 | 344 | 295 | 288 | 7 | 5 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 71 | 111..484 | 374 | 311 | 300 | 11 | 10 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..455 | 344 | 275 | 260 | 15 | 11 | 1 | 4 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 77 | 115..467 | 353 | 300 | 286 | 14 | 11 | 2 | 1 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 78 | 115..515 | 401 | 344 | 329 | 15 | 14 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 81 | 123..455 | 333 | 272 | 262 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 84 | 130..531 | 402 | 346 | 329 | 17 | 13 | 3 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 85 | 131..537 | 407 | 363 | 351 | 12 | 12 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 87 | 133..463 | 331 | 284 | 277 | 7 | 6 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 140..436 | 297 | 232 | 222 | 10 | 8 | 1 | 2 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 94 | 146..327 | 182 | 150 | 145 | 5 | 4 | 1 | 1 | 78896, 78969, 78971 |
| 97 | 158..542 | 385 | 337 | 327 | 10 | 9 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 101 | 171..492 | 322 | 266 | 263 | 3 | 3 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 144 | 271..538 | 268 | 227 | 215 | 12 | 11 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79136, 79139 |
| 166 | 345..481 | 137 | 105 | 99 | 6 | 6 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103 |
| 176 | 370..531 | 162 | 142 | 136 | 6 | 6 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 191 | 409..429 | 21 | 18 | 18 | 0 | 0 | 0 | 0 | 78896 |
| 303 | 718..718 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 7810; unmatched reference entries: 2332; unmatched candidate entries: 318
- identity switches: 1528; fragmentation (coverage interruptions): 1788; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 49 -> 52 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 42 -> 54 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f94: ref 78897: 53 -> 56 at (2125, 3030), 2 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 49 -> 53 at (2100.5, 3033), 2 frames after previous cover
- f95: ref 78897: 56 -> 52 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 53 -> 52 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 53 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 56 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 52 -> 54 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 52 -> 59 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 49 -> 42 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 52 -> 49 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 52 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 56 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 54 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 54 -> 59 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 59 -> 49 at (2077, 3031.5), 2 frames after previous cover
- f102: ref 78899: 59 -> 54 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 49 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 54 -> 61 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 52 -> 59 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 52 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 56 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 61 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 49 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 53 -> 52 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 56 -> 53 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 42 -> 61 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 61 -> 42 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 56 -> 53 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 61 -> 60 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 49 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 61 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 52 -> 59 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 59 -> 54 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79103: 53 -> 52 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 49 -> 42 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 59 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 52 -> 59 at (2096.5, 3027.5), 2 frames after previous cover
- f108: ref 79105: 53 -> 56 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 54 -> 49 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 64 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 54 -> 49 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 42 -> 61 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 49 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 54 -> 52 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 52 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 52 -> 59 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 53 -> 56 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 64 -> 53 at (2129, 3027), 3 frames after previous cover
- ... 1468 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 779 | 180 | 5 (779) |
| 78896 | 350 (76..429) | 266 | 61 | 81 (102), 101 (63), 94 (46), 191 (18), 65 (11), 74 (10), 42 (7), 54 (6), 60 (3) |
| 78969 | 352 (80..434) | 243 | 73 | 94 (94), 60 (39), 81 (39), 101 (26), 74 (14), 42 (11), 65 (8), 87 (4), 166 (3), 61 (2), 49 (1), 91 (1), +1 more |
| 78971 | 352 (84..439) | 274 | 63 | 87 (87), 64 (49), 60 (33), 65 (24), 81 (21), 166 (21), 49 (8), 42 (7), 101 (7), 74 (6), 94 (5), 78 (4), +2 more |
| 79045 | 355 (84..443) | 270 | 61 | 65 (108), 74 (50), 64 (28), 87 (27), 81 (20), 60 (10), 78 (7), 61 (5), 49 (3), 54 (3), 91 (3), 52 (2), +4 more |
| 79037 | 355 (86..445) | 267 | 65 | 74 (72), 81 (51), 91 (38), 65 (27), 87 (16), 64 (14), 60 (9), 166 (9), 61 (7), 49 (6), 78 (5), 52 (4), +3 more |
| 78897 | 345 (89..450) | 257 | 65 | 65 (91), 166 (35), 61 (26), 64 (26), 74 (18), 81 (16), 60 (9), 42 (8), 101 (6), 91 (5), 49 (4), 87 (4), +6 more |
| 78899 | 365 (91..455) | 278 | 68 | 61 (90), 74 (47), 54 (23), 91 (23), 65 (17), 101 (15), 64 (14), 81 (12), 42 (9), 60 (7), 166 (5), 87 (4), +7 more |
| 79097 | 366 (94..461) | 284 | 70 | 91 (56), 64 (55), 61 (46), 77 (24), 78 (21), 87 (16), 74 (16), 54 (15), 42 (7), 60 (7), 101 (5), 52 (4), +6 more |
| 79098 | 360 (97..467) | 289 | 55 | 91 (42), 60 (28), 71 (28), 54 (25), 77 (25), 101 (24), 64 (21), 78 (20), 87 (16), 166 (16), 74 (15), 42 (11), +6 more |
| 79102 | 371 (98..477) | 280 | 68 | 60 (60), 77 (41), 54 (36), 71 (29), 78 (21), 101 (20), 91 (16), 74 (11), 42 (9), 87 (7), 52 (5), 49 (5), +7 more |
| 79103 | 380 (99..481) | 301 | 60 | 78 (78), 60 (61), 101 (34), 54 (29), 77 (23), 87 (20), 71 (13), 42 (10), 52 (8), 49 (6), 166 (5), 64 (4), +6 more |
| 79105 | 379 (101..484) | 288 | 71 | 87 (61), 101 (40), 54 (32), 78 (30), 42 (29), 60 (21), 52 (19), 71 (16), 56 (7), 64 (7), 77 (5), 91 (5), +8 more |
| 79108 | 385 (104..492) | 309 | 65 | 54 (52), 97 (35), 78 (30), 52 (29), 91 (22), 101 (20), 77 (18), 144 (17), 56 (14), 85 (14), 87 (14), 176 (11), +8 more |
| 79110 | 388 (106..497) | 316 | 57 | 52 (51), 144 (42), 97 (41), 54 (36), 64 (29), 85 (26), 176 (23), 84 (11), 56 (10), 78 (9), 49 (8), 91 (8), +6 more |
| 79111 | 386 (109..500) | 289 | 74 | 52 (60), 85 (56), 176 (46), 78 (25), 97 (19), 56 (18), 64 (17), 77 (11), 54 (10), 71 (7), 144 (6), 84 (4), +3 more |
| 79115 | 421 (111..531) | 320 | 79 | 97 (65), 56 (60), 84 (36), 85 (32), 144 (26), 42 (19), 54 (18), 176 (16), 77 (11), 78 (11), 52 (6), 53 (5), +4 more |
| 79116 | 411 (114..530) | 313 | 73 | 85 (84), 56 (70), 84 (50), 77 (31), 144 (14), 176 (11), 54 (10), 78 (10), 97 (7), 49 (6), 42 (6), 64 (4), +4 more |
| 79122 | 404 (118..532) | 294 | 77 | 84 (116), 77 (43), 85 (30), 78 (23), 144 (15), 52 (12), 54 (11), 56 (8), 176 (8), 71 (6), 49 (6), 97 (6), +4 more |
| 79132 | 391 (120..515) | 303 | 70 | 52 (67), 56 (37), 144 (36), 84 (33), 85 (31), 78 (31), 77 (17), 54 (16), 42 (16), 49 (6), 64 (4), 97 (4), +2 more |
| 79128 | 402 (124..527) | 325 | 68 | 56 (52), 42 (50), 84 (46), 85 (38), 97 (33), 52 (31), 176 (18), 49 (15), 71 (13), 54 (13), 77 (10), 64 (3), +2 more |
| 79134 | 407 (127..533) | 312 | 73 | 71 (62), 49 (59), 97 (57), 56 (52), 84 (16), 52 (14), 144 (13), 77 (11), 54 (8), 42 (8), 53 (7), 59 (3), +1 more |
| 79135 | 409 (129..542) | 323 | 62 | 71 (84), 49 (67), 97 (57), 53 (33), 42 (32), 52 (26), 56 (20), 54 (2), 77 (2) |
| 79139 | 406 (132..537) | 323 | 65 | 49 (119), 53 (61), 144 (43), 42 (36), 52 (24), 71 (17), 56 (9), 84 (8), 59 (6) |
| 79136 | 393 (136..538) | 307 | 65 | 53 (152), 42 (47), 49 (37), 85 (34), 71 (11), 59 (10), 77 (7), 56 (3), 84 (3), 97 (2), 144 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 303 | 718..718 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 1/344/1004; tracks with internal gaps: 26; total internal gaps: 283; longest internal gap: 3; tracks ending in coasting: 11 (trailing rows total 19)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 817 | 779 | 38 | 35 | 3 | 0 | 78911 |
| 42 | 78..479 | 402 | 359 | 345 | 14 | 12 | 2 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 84..533 | 450 | 393 | 377 | 16 | 16 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 88..527 | 440 | 386 | 370 | 16 | 16 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..457 | 370 | 308 | 289 | 19 | 17 | 1 | 2 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..497 | 409 | 361 | 346 | 15 | 15 | 1 | 0 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 91..530 | 440 | 389 | 374 | 15 | 13 | 2 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 98..162 | 65 | 54 | 53 | 1 | 0 | 0 | 1 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 60 | 101..434 | 334 | 296 | 290 | 6 | 6 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 101..321 | 221 | 198 | 187 | 11 | 8 | 1 | 3 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 64 | 106..459 | 354 | 299 | 293 | 6 | 6 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..450 | 344 | 295 | 288 | 7 | 5 | 1 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 71 | 111..484 | 374 | 311 | 300 | 11 | 10 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..455 | 344 | 275 | 260 | 15 | 11 | 1 | 4 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 77 | 115..467 | 353 | 300 | 286 | 14 | 11 | 2 | 1 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 78 | 115..515 | 401 | 344 | 329 | 15 | 14 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 81 | 123..455 | 333 | 272 | 262 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 84 | 130..531 | 402 | 346 | 329 | 17 | 13 | 3 | 0 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 85 | 131..537 | 407 | 363 | 351 | 12 | 12 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 87 | 133..463 | 331 | 284 | 277 | 7 | 6 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 140..436 | 297 | 232 | 222 | 10 | 8 | 1 | 2 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 94 | 146..327 | 182 | 150 | 145 | 5 | 4 | 1 | 1 | 78896, 78969, 78971 |
| 97 | 158..542 | 385 | 337 | 327 | 10 | 9 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 101 | 171..492 | 322 | 266 | 263 | 3 | 3 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 144 | 271..538 | 268 | 227 | 215 | 12 | 11 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79136, 79139 |
| 166 | 345..481 | 137 | 105 | 99 | 6 | 6 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103 |
| 176 | 370..531 | 162 | 142 | 136 | 6 | 6 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 191 | 409..429 | 21 | 18 | 18 | 0 | 0 | 0 | 0 | 78896 |
| 303 | 718..718 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 8620; unmatched reference entries: 1522; unmatched candidate entries: 1745
- identity switches: 1540; fragmentation (coverage interruptions): 1166; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 49 -> 52 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 42 -> 54 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79045: 49 -> 42 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78897: 53 -> 56 at (2125, 3030), 1 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 42 -> 53 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 56 -> 52 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 53 -> 52 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 53 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 56 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 52 -> 54 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 52 -> 59 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 49 -> 42 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 52 -> 49 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 52 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 56 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 54 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 54 -> 59 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 59 -> 49 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 59 -> 54 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 49 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 54 -> 61 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 52 -> 59 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 52 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 56 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 61 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 49 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 53 -> 52 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 56 -> 53 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 42 -> 61 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 61 -> 42 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 56 -> 53 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 61 -> 60 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 49 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 61 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 52 -> 59 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 59 -> 54 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79102: 52 -> 56 at (2101.5, 3029.5), 1 frames after previous cover
- f107: ref 79103: 53 -> 52 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 49 -> 42 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 59 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 56 -> 59 at (2096.5, 3027.5), 1 frames after previous cover
- f108: ref 79105: 53 -> 56 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 54 -> 49 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 64 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 54 -> 49 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 42 -> 61 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 49 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 54 -> 52 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 52 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 52 -> 59 at (2087.5, 3023.5), 2 frames after previous cover
- ... 1480 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 932 | 58 | 5 (932) |
| 78896 | 350 (76..429) | 296 | 37 | 81 (114), 101 (70), 94 (50), 191 (21), 65 (13), 74 (11), 42 (7), 54 (7), 60 (3) |
| 78969 | 352 (80..434) | 281 | 43 | 94 (109), 81 (49), 60 (48), 101 (27), 74 (15), 42 (11), 65 (9), 87 (4), 166 (3), 61 (2), 49 (1), 91 (1), +2 more |
| 78971 | 352 (84..439) | 299 | 42 | 87 (95), 64 (56), 60 (39), 65 (24), 166 (23), 81 (22), 49 (9), 42 (7), 101 (7), 74 (6), 94 (5), 78 (4), +2 more |
| 79045 | 355 (84..443) | 296 | 46 | 65 (113), 74 (53), 64 (35), 87 (31), 81 (22), 60 (15), 78 (7), 61 (5), 49 (3), 54 (3), 91 (3), 52 (2), +3 more |
| 79037 | 355 (86..445) | 300 | 41 | 74 (81), 81 (60), 91 (45), 65 (31), 64 (18), 87 (16), 166 (10), 60 (9), 61 (7), 49 (6), 78 (6), 52 (4), +2 more |
| 78897 | 345 (89..450) | 283 | 47 | 65 (96), 166 (39), 64 (30), 61 (28), 74 (22), 81 (16), 60 (9), 42 (8), 101 (8), 91 (6), 87 (6), 49 (4), +6 more |
| 78899 | 365 (91..455) | 292 | 58 | 61 (94), 74 (49), 54 (24), 91 (24), 65 (17), 81 (16), 64 (15), 101 (15), 42 (9), 60 (7), 166 (6), 87 (4), +7 more |
| 79097 | 366 (94..461) | 307 | 49 | 64 (64), 91 (63), 61 (48), 77 (25), 78 (22), 87 (18), 74 (17), 54 (15), 42 (7), 60 (7), 101 (5), 52 (4), +6 more |
| 79098 | 360 (97..467) | 309 | 42 | 91 (45), 71 (33), 54 (27), 60 (27), 101 (27), 77 (26), 78 (23), 64 (23), 166 (18), 87 (16), 74 (16), 42 (11), +6 more |
| 79102 | 371 (98..477) | 304 | 51 | 60 (61), 77 (43), 54 (39), 71 (32), 78 (25), 101 (25), 91 (17), 74 (12), 42 (9), 87 (8), 166 (6), 56 (5), +7 more |
| 79103 | 380 (99..481) | 326 | 43 | 78 (81), 60 (65), 101 (36), 54 (33), 77 (26), 87 (21), 71 (16), 42 (11), 52 (8), 166 (8), 49 (6), 64 (5), +6 more |
| 79105 | 379 (101..484) | 316 | 48 | 87 (72), 101 (42), 54 (35), 78 (34), 42 (31), 60 (23), 52 (19), 71 (19), 56 (7), 64 (7), 77 (6), 91 (5), +8 more |
| 79108 | 385 (104..492) | 331 | 45 | 54 (55), 97 (39), 78 (35), 52 (30), 91 (23), 77 (21), 101 (21), 144 (19), 85 (15), 87 (14), 56 (13), 176 (12), +8 more |
| 79110 | 388 (106..497) | 339 | 39 | 52 (53), 97 (46), 144 (46), 54 (41), 64 (33), 85 (27), 176 (20), 84 (11), 56 (10), 49 (9), 91 (9), 78 (9), +6 more |
| 79111 | 386 (109..500) | 315 | 53 | 52 (67), 85 (59), 176 (51), 78 (31), 97 (20), 64 (17), 56 (17), 54 (12), 77 (11), 144 (9), 71 (8), 84 (4), +3 more |
| 79115 | 421 (111..531) | 353 | 54 | 97 (72), 56 (62), 84 (37), 144 (35), 85 (33), 42 (20), 176 (18), 54 (17), 77 (16), 78 (14), 52 (8), 53 (5), +4 more |
| 79116 | 411 (114..530) | 341 | 56 | 85 (96), 56 (81), 84 (54), 77 (33), 144 (12), 176 (12), 54 (11), 97 (8), 78 (8), 49 (6), 42 (6), 64 (4), +4 more |
| 79122 | 404 (118..532) | 322 | 54 | 84 (129), 77 (53), 85 (27), 78 (27), 144 (17), 52 (12), 54 (11), 56 (8), 97 (8), 71 (7), 176 (7), 49 (6), +4 more |
| 79132 | 391 (120..515) | 335 | 46 | 52 (75), 144 (41), 56 (39), 84 (36), 78 (36), 85 (35), 54 (21), 77 (17), 42 (16), 49 (6), 64 (4), 97 (4), +2 more |
| 79128 | 402 (124..527) | 354 | 44 | 84 (57), 42 (54), 56 (53), 85 (41), 52 (35), 97 (35), 176 (21), 49 (15), 71 (13), 54 (13), 77 (11), 64 (3), +2 more |
| 79134 | 407 (127..533) | 349 | 45 | 71 (70), 49 (64), 56 (62), 97 (61), 84 (17), 52 (16), 77 (15), 144 (15), 42 (9), 54 (8), 53 (7), 59 (3), +1 more |
| 79135 | 409 (129..542) | 356 | 40 | 71 (95), 49 (74), 97 (61), 53 (37), 42 (35), 52 (28), 56 (22), 54 (2), 77 (2) |
| 79139 | 406 (132..537) | 348 | 44 | 49 (133), 53 (61), 144 (44), 42 (37), 52 (29), 71 (18), 56 (10), 84 (9), 59 (7) |
| 79136 | 393 (136..538) | 336 | 41 | 53 (168), 42 (50), 49 (41), 85 (37), 71 (12), 59 (10), 77 (7), 84 (4), 97 (4), 56 (3) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 303 | 718..747 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 30/373/1004; tracks with internal gaps: 28; total internal gaps: 664; longest internal gap: 13; tracks ending in coasting: 28 (trailing rows total 849)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 1004 | 932 | 72 | 58 | 3 | 0 | 78911 |
| 42 | 78..508 | 431 | 431 | 362 | 69 | 28 | 6 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 84..562 | 479 | 479 | 409 | 70 | 32 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 88..556 | 469 | 469 | 403 | 66 | 35 | 9 | 19 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..486 | 399 | 399 | 310 | 89 | 31 | 10 | 33 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..526 | 438 | 438 | 375 | 63 | 26 | 6 | 29 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 91..559 | 469 | 469 | 402 | 67 | 30 | 3 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 98..191 | 94 | 94 | 55 | 39 | 4 | 5 | 31 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 60 | 101..463 | 363 | 363 | 316 | 47 | 19 | 7 | 20 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 101..350 | 250 | 250 | 194 | 56 | 18 | 2 | 35 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 64 | 106..488 | 383 | 383 | 333 | 50 | 18 | 4 | 27 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..479 | 373 | 373 | 305 | 68 | 29 | 3 | 34 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 71 | 111..513 | 403 | 403 | 338 | 65 | 28 | 5 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..484 | 373 | 373 | 283 | 90 | 31 | 8 | 48 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 77 | 115..496 | 382 | 382 | 321 | 61 | 22 | 5 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 78 | 115..544 | 430 | 430 | 366 | 64 | 23 | 7 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 81 | 123..484 | 362 | 362 | 300 | 62 | 27 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 84 | 130..560 | 431 | 431 | 364 | 67 | 32 | 3 | 24 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 85 | 131..566 | 436 | 436 | 376 | 60 | 27 | 2 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 87 | 133..492 | 360 | 360 | 306 | 54 | 20 | 3 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 140..465 | 326 | 326 | 244 | 82 | 21 | 3 | 54 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 94 | 146..356 | 211 | 211 | 164 | 47 | 13 | 3 | 30 | 78896, 78969, 78971 |
| 97 | 158..571 | 414 | 414 | 359 | 55 | 24 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 101 | 171..521 | 351 | 351 | 283 | 68 | 21 | 13 | 29 | 78896, 78897, 78899, 78969, 78971, 79097, 79098, 79102, 79103, 79105, 79108 |
| 144 | 271..567 | 297 | 297 | 240 | 57 | 17 | 3 | 32 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79139 |
| 166 | 345..510 | 166 | 166 | 114 | 52 | 15 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103 |
| 176 | 370..560 | 191 | 191 | 144 | 47 | 14 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 191 | 409..458 | 50 | 50 | 22 | 28 | 1 | 4 | 24 | 78896, 78969 |
| 303 | 718..747 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 8620; unmatched reference entries: 1522; unmatched candidate entries: 1745
- identity switches: 1540; fragmentation (coverage interruptions): 1166; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78969: 42 -> 49 at (2126.5, 3033), 1 frames after previous cover
- f86: ref 78969: 49 -> 42 at (2121.5, 3033), 1 frames after previous cover
- f88: ref 79045: 49 -> 52 at (2135.5, 3033), 2 frames after previous cover
- f90: ref 78896: 42 -> 54 at (2071.5, 3033), 5 frames after previous cover
- f91: ref 79037: 53 -> 52 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78971: 49 -> 42 at (2101.5, 3036), 1 frames after previous cover
- f92: ref 79045: 52 -> 49 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79045: 49 -> 42 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78897: 53 -> 56 at (2125, 3030), 1 frames after previous cover
- f94: ref 78971: 42 -> 49 at (2090.5, 3032.5), 2 frames after previous cover
- f94: ref 79045: 42 -> 53 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78897: 56 -> 52 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 56 -> 53 at (2134.5, 3029), 2 frames after previous cover
- f97: ref 78899: 53 -> 52 at (2123, 3030), 1 frames after previous cover
- f97: ref 79045: 53 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 56 -> 53 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 52 -> 54 at (2100, 3031), 2 frames after previous cover
- f98: ref 78899: 52 -> 59 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 78971: 49 -> 42 at (2066, 3034), 2 frames after previous cover
- f98: ref 79037: 52 -> 49 at (2087, 3034), 4 frames after previous cover
- f98: ref 79097: 53 -> 52 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 56 -> 53 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 54 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 54 -> 59 at (2088.5, 3033.5), 2 frames after previous cover
- f101: ref 78896: 54 -> 60 at (2003.5, 3033.5), 4 frames after previous cover
- f101: ref 78969: 42 -> 61 at (2028, 3033.5), 4 frames after previous cover
- f102: ref 78897: 59 -> 49 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 59 -> 54 at (2093, 3030.5), 3 frames after previous cover
- f102: ref 79037: 49 -> 42 at (2062, 3034.5), 1 frames after previous cover
- f102: ref 79045: 54 -> 61 at (2049, 3033), 1 frames after previous cover
- f102: ref 79097: 52 -> 59 at (2105, 3028.5), 1 frames after previous cover
- f102: ref 79098: 53 -> 52 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 56 -> 53 at (2130.5, 3027), 2 frames after previous cover
- f104: ref 78969: 61 -> 60 at (2009, 3033.5), 1 frames after previous cover
- f104: ref 79037: 42 -> 49 at (2051, 3034), 2 frames after previous cover
- f104: ref 79102: 53 -> 52 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 56 -> 53 at (2126, 3022.5), 2 frames after previous cover
- f105: ref 78971: 42 -> 61 at (2022, 3034), 1 frames after previous cover
- f105: ref 79045: 61 -> 42 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79105: 56 -> 53 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78971: 61 -> 60 at (2016.5, 3034), 1 frames after previous cover
- f106: ref 79037: 49 -> 42 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 42 -> 61 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79098: 52 -> 59 at (2096, 3028.5), 4 frames after previous cover
- f107: ref 78896: 60 -> 65 at (1965, 3034), 4 frames after previous cover
- f107: ref 79097: 59 -> 54 at (2076.5, 3029), 2 frames after previous cover
- f107: ref 79102: 52 -> 56 at (2101.5, 3029.5), 1 frames after previous cover
- f107: ref 79103: 53 -> 52 at (2110, 3022.5), 3 frames after previous cover
- f108: ref 78897: 49 -> 42 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79098: 59 -> 54 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 56 -> 59 at (2096.5, 3027.5), 1 frames after previous cover
- f108: ref 79105: 53 -> 56 at (2113.5, 3025), 1 frames after previous cover
- f109: ref 79097: 54 -> 49 at (2064.5, 3030), 2 frames after previous cover
- f109: ref 79108: 64 -> 53 at (2125, 3025), 2 frames after previous cover
- f110: ref 78899: 54 -> 49 at (2043, 3030.5), 4 frames after previous cover
- f110: ref 79037: 42 -> 61 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79097: 49 -> 54 at (2058.5, 3029.5), 1 frames after previous cover
- f110: ref 79098: 54 -> 52 at (2072.5, 3029.5), 1 frames after previous cover
- f111: ref 79098: 52 -> 54 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 52 -> 59 at (2087.5, 3023.5), 2 frames after previous cover
- ... 1480 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 932 | 58 | 5 (932) |
| 78896 | 350 (76..429) | 296 | 37 | 81 (114), 101 (70), 94 (50), 191 (21), 65 (13), 74 (11), 42 (7), 54 (7), 60 (3) |
| 78969 | 352 (80..434) | 281 | 43 | 94 (109), 81 (49), 60 (48), 101 (27), 74 (15), 42 (11), 65 (9), 87 (4), 166 (3), 61 (2), 49 (1), 91 (1), +2 more |
| 78971 | 352 (84..439) | 299 | 42 | 87 (95), 64 (56), 60 (39), 65 (24), 166 (23), 81 (22), 49 (9), 42 (7), 101 (7), 74 (6), 94 (5), 78 (4), +2 more |
| 79045 | 355 (84..443) | 296 | 46 | 65 (113), 74 (53), 64 (35), 87 (31), 81 (22), 60 (15), 78 (7), 61 (5), 49 (3), 54 (3), 91 (3), 52 (2), +3 more |
| 79037 | 355 (86..445) | 300 | 41 | 74 (81), 81 (60), 91 (45), 65 (31), 64 (18), 87 (16), 166 (10), 60 (9), 61 (7), 49 (6), 78 (6), 52 (4), +2 more |
| 78897 | 345 (89..450) | 283 | 47 | 65 (96), 166 (39), 64 (30), 61 (28), 74 (22), 81 (16), 60 (9), 42 (8), 101 (8), 91 (6), 87 (6), 49 (4), +6 more |
| 78899 | 365 (91..455) | 292 | 58 | 61 (94), 74 (49), 54 (24), 91 (24), 65 (17), 81 (16), 64 (15), 101 (15), 42 (9), 60 (7), 166 (6), 87 (4), +7 more |
| 79097 | 366 (94..461) | 307 | 49 | 64 (64), 91 (63), 61 (48), 77 (25), 78 (22), 87 (18), 74 (17), 54 (15), 42 (7), 60 (7), 101 (5), 52 (4), +6 more |
| 79098 | 360 (97..467) | 309 | 42 | 91 (45), 71 (33), 54 (27), 60 (27), 101 (27), 77 (26), 78 (23), 64 (23), 166 (18), 87 (16), 74 (16), 42 (11), +6 more |
| 79102 | 371 (98..477) | 304 | 51 | 60 (61), 77 (43), 54 (39), 71 (32), 78 (25), 101 (25), 91 (17), 74 (12), 42 (9), 87 (8), 166 (6), 56 (5), +7 more |
| 79103 | 380 (99..481) | 326 | 43 | 78 (81), 60 (65), 101 (36), 54 (33), 77 (26), 87 (21), 71 (16), 42 (11), 52 (8), 166 (8), 49 (6), 64 (5), +6 more |
| 79105 | 379 (101..484) | 316 | 48 | 87 (72), 101 (42), 54 (35), 78 (34), 42 (31), 60 (23), 52 (19), 71 (19), 56 (7), 64 (7), 77 (6), 91 (5), +8 more |
| 79108 | 385 (104..492) | 331 | 45 | 54 (55), 97 (39), 78 (35), 52 (30), 91 (23), 77 (21), 101 (21), 144 (19), 85 (15), 87 (14), 56 (13), 176 (12), +8 more |
| 79110 | 388 (106..497) | 339 | 39 | 52 (53), 97 (46), 144 (46), 54 (41), 64 (33), 85 (27), 176 (20), 84 (11), 56 (10), 49 (9), 91 (9), 78 (9), +6 more |
| 79111 | 386 (109..500) | 315 | 53 | 52 (67), 85 (59), 176 (51), 78 (31), 97 (20), 64 (17), 56 (17), 54 (12), 77 (11), 144 (9), 71 (8), 84 (4), +3 more |
| 79115 | 421 (111..531) | 353 | 54 | 97 (72), 56 (62), 84 (37), 144 (35), 85 (33), 42 (20), 176 (18), 54 (17), 77 (16), 78 (14), 52 (8), 53 (5), +4 more |
| 79116 | 411 (114..530) | 341 | 56 | 85 (96), 56 (81), 84 (54), 77 (33), 144 (12), 176 (12), 54 (11), 97 (8), 78 (8), 49 (6), 42 (6), 64 (4), +4 more |
| 79122 | 404 (118..532) | 322 | 54 | 84 (129), 77 (53), 85 (27), 78 (27), 144 (17), 52 (12), 54 (11), 56 (8), 97 (8), 71 (7), 176 (7), 49 (6), +4 more |
| 79132 | 391 (120..515) | 335 | 46 | 52 (75), 144 (41), 56 (39), 84 (36), 78 (36), 85 (35), 54 (21), 77 (17), 42 (16), 49 (6), 64 (4), 97 (4), +2 more |
| 79128 | 402 (124..527) | 354 | 44 | 84 (57), 42 (54), 56 (53), 85 (41), 52 (35), 97 (35), 176 (21), 49 (15), 71 (13), 54 (13), 77 (11), 64 (3), +2 more |
| 79134 | 407 (127..533) | 349 | 45 | 71 (70), 49 (64), 56 (62), 97 (61), 84 (17), 52 (16), 77 (15), 144 (15), 42 (9), 54 (8), 53 (7), 59 (3), +1 more |
| 79135 | 409 (129..542) | 356 | 40 | 71 (95), 49 (74), 97 (61), 53 (37), 42 (35), 52 (28), 56 (22), 54 (2), 77 (2) |
| 79139 | 406 (132..537) | 348 | 44 | 49 (133), 53 (61), 144 (44), 42 (37), 52 (29), 71 (18), 56 (10), 84 (9), 59 (7) |
| 79136 | 393 (136..538) | 336 | 41 | 53 (168), 42 (50), 49 (41), 85 (37), 71 (12), 59 (10), 77 (7), 84 (4), 97 (4), 56 (3) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 303 | 718..747 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 30/373/1004; tracks with internal gaps: 28; total internal gaps: 664; longest internal gap: 13; tracks ending in coasting: 28 (trailing rows total 849)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 5..1008 | 1004 | 1004 | 932 | 72 | 58 | 3 | 0 | 78911 |
| 42 | 78..508 | 431 | 431 | 362 | 69 | 28 | 6 | 30 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 84..562 | 479 | 479 | 409 | 70 | 32 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 52 | 88..556 | 469 | 469 | 403 | 66 | 35 | 9 | 19 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 53 | 88..486 | 399 | 399 | 310 | 89 | 31 | 10 | 33 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 54 | 89..526 | 438 | 438 | 375 | 63 | 26 | 6 | 29 | 78896, 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 56 | 91..559 | 469 | 469 | 402 | 67 | 30 | 3 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 59 | 98..191 | 94 | 94 | 55 | 39 | 4 | 5 | 31 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79134, 79136, 79139 |
| 60 | 101..463 | 363 | 363 | 316 | 47 | 19 | 7 | 20 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 101..350 | 250 | 250 | 194 | 56 | 18 | 2 | 35 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 64 | 106..488 | 383 | 383 | 333 | 50 | 18 | 4 | 27 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 107..479 | 373 | 373 | 305 | 68 | 29 | 3 | 34 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 71 | 111..513 | 403 | 403 | 338 | 65 | 28 | 5 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 112..484 | 373 | 373 | 283 | 90 | 31 | 8 | 48 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 77 | 115..496 | 382 | 382 | 321 | 61 | 22 | 5 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 78 | 115..544 | 430 | 430 | 366 | 64 | 23 | 7 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 81 | 123..484 | 362 | 362 | 300 | 62 | 27 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 84 | 130..560 | 431 | 431 | 364 | 67 | 32 | 3 | 24 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 85 | 131..566 | 436 | 436 | 376 | 60 | 27 | 2 | 28 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79136 |
| 87 | 133..492 | 360 | 360 | 306 | 54 | 20 | 3 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 91 | 140..465 | 326 | 326 | 244 | 82 | 21 | 3 | 54 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 94 | 146..356 | 211 | 211 | 164 | 47 | 13 | 3 | 30 | 78896, 78969, 78971 |
| 97 | 158..571 | 414 | 414 | 359 | 55 | 24 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 101 | 171..521 | 351 | 351 | 283 | 68 | 21 | 13 | 29 | 78896, 78897, 78899, 78969, 78971, 79097, 79098, 79102, 79103, 79105, 79108 |
| 144 | 271..567 | 297 | 297 | 240 | 57 | 17 | 3 | 32 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79139 |
| 166 | 345..510 | 166 | 166 | 114 | 52 | 15 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103 |
| 176 | 370..560 | 191 | 191 | 144 | 47 | 14 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 191 | 409..458 | 50 | 50 | 22 | 28 | 1 | 4 | 24 | 78896, 78969 |
| 303 | 718..747 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
