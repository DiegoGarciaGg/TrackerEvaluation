# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=bbbe28a08fe0
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise3.0_fp0.5_seed1/tracks.csv sha256=af312fee778e980b
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise3.0_fp0.5_seed1.csv sha256=bbbe28a08fe0a095
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise3.0_fp0.5_seed1
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
| observations | none | 4 | 10142 | 9078 | 0.219 | 0.398 | 0.121 | 2.18 | 0.214 | 0.108 | 2.41 | 534 | 2511.0 | 0.240 | 0.254 | 0.228 | 0.528 | 0.590 | 5356 | 4786 | 3722 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 9078 | 0.304 | 0.557 | 0.166 | 2.72 | 0.370 | 0.586 | 3.19 | 650 | 1757.0 | 0.356 | 0.376 | 0.337 | 0.773 | 0.863 | 7836 | 2306 | 1242 | 3 | 22 | 0 |
| observations | none | 8 | 10142 | 9078 | 0.350 | 0.631 | 0.194 | 3.05 | 0.441 | 0.765 | 3.58 | 638 | 1179.0 | 0.403 | 0.426 | 0.381 | 0.862 | 0.963 | 8739 | 1403 | 339 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 9078 | 0.398 | 0.690 | 0.230 | 3.57 | 0.469 | 0.814 | 3.90 | 585 | 989.0 | 0.436 | 0.462 | 0.414 | 0.884 | 0.987 | 8961 | 1181 | 117 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 9078 | 0.219 | 0.398 | 0.121 | 2.18 | 0.214 | 0.108 | 2.41 | 534 | 2511.0 | 0.240 | 0.254 | 0.228 | 0.528 | 0.590 | 5356 | 4786 | 3722 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 9078 | 0.304 | 0.557 | 0.166 | 2.72 | 0.370 | 0.586 | 3.19 | 650 | 1757.0 | 0.356 | 0.376 | 0.337 | 0.773 | 0.863 | 7836 | 2306 | 1242 | 3 | 22 | 0 |
| observations | ignore | 8 | 10142 | 9078 | 0.350 | 0.631 | 0.194 | 3.05 | 0.441 | 0.765 | 3.58 | 638 | 1179.0 | 0.403 | 0.426 | 0.381 | 0.862 | 0.963 | 8739 | 1403 | 339 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 9078 | 0.398 | 0.690 | 0.230 | 3.57 | 0.469 | 0.814 | 3.90 | 585 | 989.0 | 0.436 | 0.462 | 0.414 | 0.884 | 0.987 | 8961 | 1181 | 117 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 11228 | 0.206 | 0.361 | 0.118 | 2.20 | 0.199 | -0.071 | 2.42 | 560 | 2503.0 | 0.224 | 0.213 | 0.236 | 0.545 | 0.493 | 5532 | 4610 | 5696 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 11228 | 0.293 | 0.514 | 0.168 | 2.79 | 0.349 | 0.444 | 3.22 | 650 | 1544.0 | 0.337 | 0.321 | 0.355 | 0.808 | 0.730 | 8192 | 1950 | 3036 | 13 | 12 | 0 |
| updates | none | 8 | 10142 | 11228 | 0.342 | 0.591 | 0.198 | 3.16 | 0.426 | 0.663 | 3.67 | 622 | 756.0 | 0.390 | 0.371 | 0.410 | 0.916 | 0.827 | 9288 | 854 | 1940 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 11228 | 0.394 | 0.657 | 0.237 | 3.73 | 0.469 | 0.753 | 4.12 | 552 | 384.0 | 0.431 | 0.410 | 0.454 | 0.957 | 0.865 | 9710 | 432 | 1518 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 11228 | 0.206 | 0.361 | 0.118 | 2.20 | 0.199 | -0.071 | 2.42 | 560 | 2503.0 | 0.224 | 0.213 | 0.236 | 0.545 | 0.493 | 5532 | 4610 | 5696 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 11228 | 0.293 | 0.514 | 0.168 | 2.79 | 0.349 | 0.444 | 3.22 | 650 | 1544.0 | 0.337 | 0.321 | 0.355 | 0.808 | 0.730 | 8192 | 1950 | 3036 | 13 | 12 | 0 |
| updates | ignore | 8 | 10142 | 11228 | 0.342 | 0.591 | 0.198 | 3.16 | 0.426 | 0.663 | 3.67 | 622 | 756.0 | 0.390 | 0.371 | 0.410 | 0.916 | 0.827 | 9288 | 854 | 1940 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 11228 | 0.394 | 0.657 | 0.237 | 3.73 | 0.469 | 0.753 | 4.12 | 552 | 384.0 | 0.431 | 0.410 | 0.454 | 0.957 | 0.865 | 9710 | 432 | 1518 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 36; matched pairs: 8739; unmatched reference entries: 1403; unmatched candidate entries: 339
- identity switches: 638; fragmentation (coverage interruptions): 1143; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 43 -> 45 at (2112.5, 3034), 1 frames after previous cover
- f94: ref 79045: 45 -> 50 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78971: 50 -> 51 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79097: 46 -> 48 at (2146.5, 3029), 1 frames after previous cover
- f96: ref 79097: 48 -> 46 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 51 -> 41 at (2072, 3034.5), 1 frames after previous cover
- f98: ref 78969: 41 -> 51 at (2047.5, 3033), 2 frames after previous cover
- f98: ref 79097: 46 -> 48 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 46 -> 48 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 48 -> 43 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79097: 48 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78897: 43 -> 57 at (2077, 3031.5), 3 frames after previous cover
- f102: ref 79103: 55 -> 46 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 46 -> 58 at (2124.5, 3027.5), 2 frames after previous cover
- f104: ref 78899: 43 -> 57 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79098: 48 -> 54 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79097: 54 -> 43 at (2088, 3029), 2 frames after previous cover
- f105: ref 79102: 58 -> 48 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 46 -> 58 at (2120.5, 3023), 2 frames after previous cover
- f105: ref 79105: 55 -> 46 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78897: 57 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 43 -> 57 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 54 -> 43 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 58 -> 54 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 46 -> 58 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78897: 45 -> 57 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 57 -> 62 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 57 -> 45 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 45 -> 50 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 50 -> 41 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 62 -> 43 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78969: 51 -> 38 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 79098: 43 -> 62 at (2077.5, 3029.5), 2 frames after previous cover
- f110: ref 78969: 38 -> 51 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 58 -> 54 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 55 -> 58 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 46 -> 55 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 62 -> 48 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 48 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 41 -> 66 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 54 -> 65 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 54 -> 62 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 65 -> 54 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 58 -> 65 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 55 -> 58 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 46 -> 55 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 48 -> 43 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 48 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 65 -> 58 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 58 -> 65 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 43 -> 45 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 79097: 45 -> 43 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 55 -> 65 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 46 -> 55 at (2118, 3022), 1 frames after previous cover
- ... 578 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 878 | 113 | 0 (878) |
| 78896 | 350 (76..429) | 304 | 36 | 38 (304) |
| 78969 | 352 (80..434) | 299 | 40 | 66 (127), 45 (121), 51 (32), 41 (13), 38 (6) |
| 78971 | 352 (84..439) | 303 | 39 | 41 (236), 51 (42), 50 (12), 66 (7), 45 (4), 43 (1), 57 (1) |
| 79045 | 355 (84..443) | 298 | 43 | 66 (87), 41 (64), 45 (53), 57 (33), 106 (27), 210 (17), 50 (14), 43 (3) |
| 79037 | 355 (86..445) | 304 | 35 | 106 (155), 45 (42), 66 (41), 57 (31), 50 (29), 43 (3), 210 (2), 41 (1) |
| 78897 | 345 (89..450) | 290 | 41 | 50 (95), 57 (78), 106 (49), 45 (32), 66 (25), 43 (7), 48 (3), 46 (1) |
| 78899 | 365 (91..455) | 305 | 47 | 133 (168), 57 (55), 45 (45), 50 (21), 106 (7), 43 (4), 46 (3), 48 (2) |
| 79097 | 366 (94..461) | 313 | 47 | 50 (113), 43 (75), 161 (62), 133 (23), 48 (21), 57 (6), 45 (6), 54 (4), 46 (2), 62 (1) |
| 79098 | 360 (97..467) | 315 | 35 | 83 (141), 48 (72), 161 (72), 50 (13), 43 (11), 54 (2), 62 (2), 46 (1), 78 (1) |
| 79102 | 371 (98..477) | 304 | 46 | 83 (98), 78 (69), 48 (51), 87 (45), 43 (32), 62 (4), 46 (3), 58 (2) |
| 79103 | 380 (99..481) | 315 | 46 | 78 (101), 43 (69), 87 (59), 83 (53), 124 (12), 62 (10), 54 (5), 46 (2), 48 (2), 55 (1), 58 (1) |
| 79105 | 379 (101..484) | 328 | 43 | 78 (129), 87 (80), 43 (50), 195 (24), 124 (15), 54 (13), 58 (4), 83 (4), 55 (3), 65 (2), 84 (2), 46 (1), +1 more |
| 79108 | 385 (104..492) | 329 | 48 | 43 (102), 124 (93), 54 (76), 87 (22), 78 (13), 58 (12), 55 (4), 84 (3), 65 (2), 62 (2) |
| 79110 | 388 (106..497) | 341 | 39 | 54 (72), 195 (72), 87 (52), 58 (48), 91 (36), 124 (32), 70 (11), 62 (5), 55 (4), 74 (4), 46 (3), 65 (2) |
| 79111 | 386 (109..500) | 335 | 44 | 54 (102), 58 (61), 87 (43), 84 (41), 124 (28), 91 (23), 70 (15), 65 (7), 46 (4), 55 (4), 62 (4), 74 (3) |
| 79115 | 421 (111..531) | 374 | 39 | 124 (111), 84 (99), 70 (43), 54 (41), 58 (21), 65 (19), 55 (14), 87 (9), 91 (8), 62 (5), 46 (4) |
| 79116 | 411 (114..530) | 358 | 39 | 65 (138), 84 (48), 91 (43), 62 (40), 70 (30), 58 (28), 152 (12), 54 (7), 55 (6), 87 (4), 74 (2) |
| 79122 | 404 (118..532) | 336 | 61 | 84 (101), 70 (36), 55 (36), 62 (36), 65 (31), 58 (30), 91 (28), 54 (25), 46 (7), 74 (6) |
| 79132 | 391 (120..515) | 344 | 41 | 58 (112), 70 (50), 84 (48), 74 (46), 152 (37), 55 (20), 65 (17), 54 (4), 46 (3), 91 (3), 72 (2), 62 (2) |
| 79128 | 402 (124..527) | 349 | 47 | 74 (97), 70 (90), 65 (65), 58 (48), 177 (26), 84 (10), 72 (4), 46 (4), 91 (3), 152 (2) |
| 79134 | 407 (127..533) | 360 | 42 | 177 (105), 70 (81), 74 (64), 91 (61), 65 (25), 72 (13), 152 (6), 46 (5) |
| 79135 | 409 (129..542) | 362 | 39 | 72 (137), 74 (75), 65 (62), 46 (47), 91 (29), 152 (9), 177 (2), 70 (1) |
| 79139 | 406 (132..537) | 355 | 45 | 72 (108), 74 (79), 46 (60), 152 (44), 177 (36), 91 (27), 82 (1) |
| 79136 | 393 (136..538) | 340 | 48 | 72 (95), 91 (95), 46 (66), 82 (42), 181 (20), 177 (12), 62 (10) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 301 | 633..633 | 1 | 0 | 1 |
| 306 | 647..671 | 25 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 36; lifespan min/median/max: 1/339/1007; tracks with internal gaps: 33; total internal gaps: 291; longest internal gap: 3; tracks ending in coasting: 14 (trailing rows total 34)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 912 | 878 | 34 | 34 | 1 | 0 | 78911 |
| 38 | 78..429 | 352 | 315 | 310 | 5 | 5 | 1 | 0 | 78896, 78969 |
| 41 | 83..439 | 357 | 326 | 314 | 12 | 11 | 2 | 0 | 78969, 78971, 79037, 79045 |
| 43 | 86..492 | 407 | 369 | 357 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 45 | 90..434 | 345 | 308 | 303 | 5 | 5 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 46 | 90..368 | 279 | 227 | 216 | 11 | 7 | 1 | 4 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 48 | 91..272 | 182 | 161 | 151 | 10 | 9 | 1 | 1 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 50 | 93..482 | 390 | 320 | 297 | 23 | 19 | 2 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 95..186 | 92 | 81 | 74 | 7 | 5 | 1 | 2 | 78969, 78971 |
| 54 | 100..500 | 401 | 362 | 351 | 11 | 10 | 2 | 0 | 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 55 | 100..227 | 128 | 98 | 92 | 6 | 4 | 1 | 2 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 57 | 102..340 | 239 | 213 | 204 | 9 | 7 | 1 | 2 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 58 | 103..515 | 413 | 385 | 367 | 18 | 16 | 3 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 62 | 107..284 | 178 | 128 | 122 | 6 | 3 | 1 | 3 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..530 | 419 | 387 | 370 | 17 | 15 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..450 | 339 | 302 | 287 | 15 | 14 | 2 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 70 | 116..527 | 412 | 368 | 357 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 72 | 122..537 | 416 | 374 | 359 | 15 | 15 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 122..542 | 421 | 391 | 376 | 15 | 14 | 2 | 0 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 126..481 | 356 | 316 | 313 | 3 | 3 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 82 | 132..186 | 55 | 47 | 43 | 4 | 3 | 1 | 1 | 79136, 79139 |
| 83 | 132..481 | 350 | 305 | 296 | 9 | 7 | 2 | 1 | 79098, 79102, 79103, 79105 |
| 84 | 132..532 | 401 | 363 | 352 | 11 | 11 | 1 | 0 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 139..484 | 346 | 324 | 314 | 10 | 10 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 91 | 145..533 | 389 | 363 | 356 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 106 | 177..445 | 269 | 248 | 238 | 10 | 8 | 2 | 0 | 78897, 78899, 79037, 79045 |
| 124 | 207..531 | 325 | 297 | 291 | 6 | 6 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 133 | 230..455 | 226 | 202 | 191 | 11 | 10 | 2 | 0 | 78899, 79097 |
| 152 | 281..431 | 151 | 117 | 110 | 7 | 2 | 1 | 5 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 161 | 314..467 | 154 | 137 | 134 | 3 | 3 | 1 | 0 | 79097, 79098 |
| 177 | 344..538 | 195 | 182 | 181 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 181 | 353..408 | 56 | 26 | 20 | 6 | 1 | 1 | 5 | 79136 |
| 195 | 384..497 | 114 | 100 | 96 | 4 | 4 | 1 | 0 | 79105, 79110 |
| 210 | 421..443 | 23 | 20 | 19 | 1 | 0 | 0 | 1 | 79037, 79045 |
| 301 | 633..633 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 306 | 647..671 | 25 | 3 | 0 | 3 | 0 | 0 | 3 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 36; matched pairs: 8739; unmatched reference entries: 1403; unmatched candidate entries: 339
- identity switches: 638; fragmentation (coverage interruptions): 1143; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 43 -> 45 at (2112.5, 3034), 1 frames after previous cover
- f94: ref 79045: 45 -> 50 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78971: 50 -> 51 at (2084, 3033.5), 2 frames after previous cover
- f95: ref 79097: 46 -> 48 at (2146.5, 3029), 1 frames after previous cover
- f96: ref 79097: 48 -> 46 at (2141, 3029), 1 frames after previous cover
- f97: ref 78971: 51 -> 41 at (2072, 3034.5), 1 frames after previous cover
- f98: ref 78969: 41 -> 51 at (2047.5, 3033), 2 frames after previous cover
- f98: ref 79097: 46 -> 48 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 46 -> 48 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 48 -> 43 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79097: 48 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78897: 43 -> 57 at (2077, 3031.5), 3 frames after previous cover
- f102: ref 79103: 55 -> 46 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 46 -> 58 at (2124.5, 3027.5), 2 frames after previous cover
- f104: ref 78899: 43 -> 57 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79098: 48 -> 54 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79097: 54 -> 43 at (2088, 3029), 2 frames after previous cover
- f105: ref 79102: 58 -> 48 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 46 -> 58 at (2120.5, 3023), 2 frames after previous cover
- f105: ref 79105: 55 -> 46 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78897: 57 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 43 -> 57 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 54 -> 43 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 58 -> 54 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 46 -> 58 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78897: 45 -> 57 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 57 -> 62 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 57 -> 45 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 45 -> 50 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 50 -> 41 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 62 -> 43 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78969: 51 -> 38 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 79098: 43 -> 62 at (2077.5, 3029.5), 2 frames after previous cover
- f110: ref 78969: 38 -> 51 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 58 -> 54 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 55 -> 58 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 46 -> 55 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 62 -> 48 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 48 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 41 -> 66 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 54 -> 65 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 54 -> 62 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 65 -> 54 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 58 -> 65 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 55 -> 58 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 46 -> 55 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 48 -> 43 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 48 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 65 -> 58 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 58 -> 65 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 43 -> 45 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 79097: 45 -> 43 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 55 -> 65 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 46 -> 55 at (2118, 3022), 1 frames after previous cover
- ... 578 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 878 | 113 | 0 (878) |
| 78896 | 350 (76..429) | 304 | 36 | 38 (304) |
| 78969 | 352 (80..434) | 299 | 40 | 66 (127), 45 (121), 51 (32), 41 (13), 38 (6) |
| 78971 | 352 (84..439) | 303 | 39 | 41 (236), 51 (42), 50 (12), 66 (7), 45 (4), 43 (1), 57 (1) |
| 79045 | 355 (84..443) | 298 | 43 | 66 (87), 41 (64), 45 (53), 57 (33), 106 (27), 210 (17), 50 (14), 43 (3) |
| 79037 | 355 (86..445) | 304 | 35 | 106 (155), 45 (42), 66 (41), 57 (31), 50 (29), 43 (3), 210 (2), 41 (1) |
| 78897 | 345 (89..450) | 290 | 41 | 50 (95), 57 (78), 106 (49), 45 (32), 66 (25), 43 (7), 48 (3), 46 (1) |
| 78899 | 365 (91..455) | 305 | 47 | 133 (168), 57 (55), 45 (45), 50 (21), 106 (7), 43 (4), 46 (3), 48 (2) |
| 79097 | 366 (94..461) | 313 | 47 | 50 (113), 43 (75), 161 (62), 133 (23), 48 (21), 57 (6), 45 (6), 54 (4), 46 (2), 62 (1) |
| 79098 | 360 (97..467) | 315 | 35 | 83 (141), 48 (72), 161 (72), 50 (13), 43 (11), 54 (2), 62 (2), 46 (1), 78 (1) |
| 79102 | 371 (98..477) | 304 | 46 | 83 (98), 78 (69), 48 (51), 87 (45), 43 (32), 62 (4), 46 (3), 58 (2) |
| 79103 | 380 (99..481) | 315 | 46 | 78 (101), 43 (69), 87 (59), 83 (53), 124 (12), 62 (10), 54 (5), 46 (2), 48 (2), 55 (1), 58 (1) |
| 79105 | 379 (101..484) | 328 | 43 | 78 (129), 87 (80), 43 (50), 195 (24), 124 (15), 54 (13), 58 (4), 83 (4), 55 (3), 65 (2), 84 (2), 46 (1), +1 more |
| 79108 | 385 (104..492) | 329 | 48 | 43 (102), 124 (93), 54 (76), 87 (22), 78 (13), 58 (12), 55 (4), 84 (3), 65 (2), 62 (2) |
| 79110 | 388 (106..497) | 341 | 39 | 54 (72), 195 (72), 87 (52), 58 (48), 91 (36), 124 (32), 70 (11), 62 (5), 55 (4), 74 (4), 46 (3), 65 (2) |
| 79111 | 386 (109..500) | 335 | 44 | 54 (102), 58 (61), 87 (43), 84 (41), 124 (28), 91 (23), 70 (15), 65 (7), 46 (4), 55 (4), 62 (4), 74 (3) |
| 79115 | 421 (111..531) | 374 | 39 | 124 (111), 84 (99), 70 (43), 54 (41), 58 (21), 65 (19), 55 (14), 87 (9), 91 (8), 62 (5), 46 (4) |
| 79116 | 411 (114..530) | 358 | 39 | 65 (138), 84 (48), 91 (43), 62 (40), 70 (30), 58 (28), 152 (12), 54 (7), 55 (6), 87 (4), 74 (2) |
| 79122 | 404 (118..532) | 336 | 61 | 84 (101), 70 (36), 55 (36), 62 (36), 65 (31), 58 (30), 91 (28), 54 (25), 46 (7), 74 (6) |
| 79132 | 391 (120..515) | 344 | 41 | 58 (112), 70 (50), 84 (48), 74 (46), 152 (37), 55 (20), 65 (17), 54 (4), 46 (3), 91 (3), 72 (2), 62 (2) |
| 79128 | 402 (124..527) | 349 | 47 | 74 (97), 70 (90), 65 (65), 58 (48), 177 (26), 84 (10), 72 (4), 46 (4), 91 (3), 152 (2) |
| 79134 | 407 (127..533) | 360 | 42 | 177 (105), 70 (81), 74 (64), 91 (61), 65 (25), 72 (13), 152 (6), 46 (5) |
| 79135 | 409 (129..542) | 362 | 39 | 72 (137), 74 (75), 65 (62), 46 (47), 91 (29), 152 (9), 177 (2), 70 (1) |
| 79139 | 406 (132..537) | 355 | 45 | 72 (108), 74 (79), 46 (60), 152 (44), 177 (36), 91 (27), 82 (1) |
| 79136 | 393 (136..538) | 340 | 48 | 72 (95), 91 (95), 46 (66), 82 (42), 181 (20), 177 (12), 62 (10) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 301 | 633..633 | 1 | 0 | 1 |
| 306 | 647..671 | 25 | 0 | 3 |

### Gaps and durations of candidate tracks
- tracks: 36; lifespan min/median/max: 1/339/1007; tracks with internal gaps: 33; total internal gaps: 291; longest internal gap: 3; tracks ending in coasting: 14 (trailing rows total 34)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 912 | 878 | 34 | 34 | 1 | 0 | 78911 |
| 38 | 78..429 | 352 | 315 | 310 | 5 | 5 | 1 | 0 | 78896, 78969 |
| 41 | 83..439 | 357 | 326 | 314 | 12 | 11 | 2 | 0 | 78969, 78971, 79037, 79045 |
| 43 | 86..492 | 407 | 369 | 357 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 45 | 90..434 | 345 | 308 | 303 | 5 | 5 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 46 | 90..368 | 279 | 227 | 216 | 11 | 7 | 1 | 4 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 48 | 91..272 | 182 | 161 | 151 | 10 | 9 | 1 | 1 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 50 | 93..482 | 390 | 320 | 297 | 23 | 19 | 2 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 95..186 | 92 | 81 | 74 | 7 | 5 | 1 | 2 | 78969, 78971 |
| 54 | 100..500 | 401 | 362 | 351 | 11 | 10 | 2 | 0 | 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 55 | 100..227 | 128 | 98 | 92 | 6 | 4 | 1 | 2 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 57 | 102..340 | 239 | 213 | 204 | 9 | 7 | 1 | 2 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 58 | 103..515 | 413 | 385 | 367 | 18 | 16 | 3 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 62 | 107..284 | 178 | 128 | 122 | 6 | 3 | 1 | 3 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..530 | 419 | 387 | 370 | 17 | 15 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..450 | 339 | 302 | 287 | 15 | 14 | 2 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 70 | 116..527 | 412 | 368 | 357 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 72 | 122..537 | 416 | 374 | 359 | 15 | 15 | 1 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 122..542 | 421 | 391 | 376 | 15 | 14 | 2 | 0 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 126..481 | 356 | 316 | 313 | 3 | 3 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 82 | 132..186 | 55 | 47 | 43 | 4 | 3 | 1 | 1 | 79136, 79139 |
| 83 | 132..481 | 350 | 305 | 296 | 9 | 7 | 2 | 1 | 79098, 79102, 79103, 79105 |
| 84 | 132..532 | 401 | 363 | 352 | 11 | 11 | 1 | 0 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 139..484 | 346 | 324 | 314 | 10 | 10 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 91 | 145..533 | 389 | 363 | 356 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 106 | 177..445 | 269 | 248 | 238 | 10 | 8 | 2 | 0 | 78897, 78899, 79037, 79045 |
| 124 | 207..531 | 325 | 297 | 291 | 6 | 6 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 133 | 230..455 | 226 | 202 | 191 | 11 | 10 | 2 | 0 | 78899, 79097 |
| 152 | 281..431 | 151 | 117 | 110 | 7 | 2 | 1 | 5 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 161 | 314..467 | 154 | 137 | 134 | 3 | 3 | 1 | 0 | 79097, 79098 |
| 177 | 344..538 | 195 | 182 | 181 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 181 | 353..408 | 56 | 26 | 20 | 6 | 1 | 1 | 5 | 79136 |
| 195 | 384..497 | 114 | 100 | 96 | 4 | 4 | 1 | 0 | 79105, 79110 |
| 210 | 421..443 | 23 | 20 | 19 | 1 | 0 | 0 | 1 | 79037, 79045 |
| 301 | 633..633 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 306 | 647..671 | 25 | 3 | 0 | 3 | 0 | 0 | 3 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 36; matched pairs: 9288; unmatched reference entries: 854; unmatched candidate entries: 1940
- identity switches: 622; fragmentation (coverage interruptions): 670; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 1 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 43 -> 45 at (2112.5, 3034), 1 frames after previous cover
- f94: ref 79045: 45 -> 50 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78971: 50 -> 51 at (2084, 3033.5), 2 frames after previous cover
- f98: ref 78969: 41 -> 51 at (2047.5, 3033), 2 frames after previous cover
- f98: ref 78971: 51 -> 41 at (2066, 3034), 1 frames after previous cover
- f98: ref 79097: 46 -> 48 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 46 -> 48 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 48 -> 43 at (2104, 3030.5), 3 frames after previous cover
- f100: ref 79097: 48 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78897: 43 -> 57 at (2077, 3031.5), 3 frames after previous cover
- f102: ref 79103: 55 -> 46 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 46 -> 58 at (2124.5, 3027.5), 2 frames after previous cover
- f105: ref 78899: 43 -> 57 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 54 -> 43 at (2088, 3029), 2 frames after previous cover
- f105: ref 79098: 48 -> 54 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 58 -> 48 at (2113.5, 3026.5), 1 frames after previous cover
- f106: ref 78897: 57 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 43 -> 57 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 54 -> 43 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 46 -> 54 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 55 -> 58 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 78897: 45 -> 57 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 57 -> 62 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 57 -> 45 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 45 -> 50 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 50 -> 41 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 62 -> 43 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 43 -> 62 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78969: 51 -> 38 at (1978, 3034.5), 1 frames after previous cover
- f110: ref 78969: 38 -> 51 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 58 -> 54 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 55 -> 58 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 46 -> 55 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 62 -> 48 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 48 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 41 -> 66 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 54 -> 65 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 54 -> 62 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 65 -> 54 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 58 -> 65 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 55 -> 58 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 46 -> 55 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 48 -> 43 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 48 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 65 -> 58 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 58 -> 65 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 43 -> 45 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 45 -> 50 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79097: 45 -> 43 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 55 -> 65 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 46 -> 55 at (2118, 3022), 1 frames after previous cover
- f119: ref 78897: 50 -> 45 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 79098: 43 -> 48 at (2019, 3029.5), 2 frames after previous cover
- f121: ref 78899: 57 -> 45 at (1976, 3033), 1 frames after previous cover
- ... 562 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 955 | 49 | 0 (955) |
| 78896 | 350 (76..429) | 322 | 23 | 38 (322) |
| 78969 | 352 (80..434) | 319 | 27 | 66 (135), 45 (129), 51 (35), 41 (13), 38 (7) |
| 78971 | 352 (84..439) | 318 | 28 | 41 (247), 51 (44), 50 (12), 66 (7), 43 (4), 45 (4) |
| 79045 | 355 (84..443) | 322 | 22 | 66 (96), 41 (69), 45 (61), 57 (36), 106 (26), 210 (19), 50 (14), 43 (1) |
| 79037 | 355 (86..445) | 315 | 24 | 106 (162), 45 (44), 66 (41), 57 (33), 50 (29), 43 (3), 210 (2), 41 (1) |
| 78897 | 345 (89..450) | 309 | 27 | 50 (103), 57 (83), 106 (53), 45 (34), 66 (25), 43 (7), 48 (3), 46 (1) |
| 78899 | 365 (91..455) | 330 | 29 | 133 (183), 57 (55), 45 (52), 50 (22), 106 (7), 43 (5), 46 (3), 48 (3) |
| 79097 | 366 (94..461) | 332 | 30 | 50 (122), 43 (76), 161 (68), 133 (23), 48 (21), 57 (7), 45 (6), 46 (4), 54 (4), 62 (1) |
| 79098 | 360 (97..467) | 329 | 23 | 83 (147), 48 (78), 161 (74), 50 (13), 43 (11), 62 (3), 46 (1), 54 (1), 78 (1) |
| 79102 | 371 (98..477) | 325 | 29 | 83 (108), 78 (74), 48 (53), 87 (48), 43 (33), 62 (4), 46 (3), 58 (2) |
| 79103 | 380 (99..481) | 336 | 28 | 78 (109), 43 (72), 87 (62), 83 (58), 124 (12), 62 (10), 54 (6), 46 (4), 48 (2), 55 (1) |
| 79105 | 379 (101..484) | 347 | 24 | 78 (136), 87 (83), 43 (54), 195 (26), 54 (15), 124 (15), 83 (6), 58 (4), 55 (3), 84 (3), 65 (2) |
| 79108 | 385 (104..492) | 353 | 26 | 43 (110), 124 (95), 54 (84), 87 (25), 58 (14), 78 (13), 55 (5), 84 (3), 65 (2), 62 (2) |
| 79110 | 388 (106..497) | 365 | 17 | 195 (82), 54 (77), 87 (55), 58 (50), 91 (37), 124 (34), 70 (12), 62 (5), 55 (4), 74 (4), 46 (3), 65 (2) |
| 79111 | 386 (109..500) | 357 | 23 | 54 (109), 58 (61), 87 (45), 84 (43), 124 (31), 91 (27), 70 (18), 65 (8), 46 (4), 55 (4), 62 (4), 74 (3) |
| 79115 | 421 (111..531) | 392 | 22 | 124 (117), 84 (104), 54 (46), 70 (45), 58 (21), 65 (19), 55 (14), 87 (9), 91 (8), 62 (5), 46 (4) |
| 79116 | 411 (114..530) | 378 | 23 | 65 (151), 84 (49), 91 (44), 62 (42), 70 (32), 58 (22), 152 (18), 54 (7), 55 (6), 87 (5), 74 (2) |
| 79122 | 404 (118..532) | 367 | 35 | 84 (114), 55 (43), 70 (39), 62 (37), 58 (34), 65 (32), 91 (28), 54 (27), 46 (7), 74 (6) |
| 79132 | 391 (120..515) | 359 | 24 | 58 (117), 70 (52), 84 (50), 74 (49), 152 (39), 55 (20), 65 (18), 54 (4), 46 (3), 91 (3), 72 (2), 62 (2) |
| 79128 | 402 (124..527) | 367 | 30 | 74 (100), 70 (97), 65 (66), 58 (52), 177 (27), 84 (12), 72 (4), 46 (4), 91 (3), 152 (2) |
| 79134 | 407 (127..533) | 380 | 25 | 177 (112), 70 (86), 74 (68), 91 (63), 65 (25), 72 (15), 152 (6), 46 (5) |
| 79135 | 409 (129..542) | 379 | 22 | 72 (148), 74 (77), 65 (64), 46 (49), 91 (29), 152 (9), 177 (2), 70 (1) |
| 79139 | 406 (132..537) | 373 | 31 | 72 (98), 74 (83), 46 (60), 177 (48), 152 (47), 91 (35), 82 (2) |
| 79136 | 393 (136..538) | 359 | 29 | 72 (116), 91 (94), 46 (71), 82 (45), 181 (23), 62 (10) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 301 | 633..662 | 30 | 0 | 30 |
| 306 | 647..700 | 54 | 0 | 54 |

### Gaps and durations of candidate tracks
- tracks: 36; lifespan min/median/max: 30/368/1007; tracks with internal gaps: 34; total internal gaps: 607; longest internal gap: 12; tracks ending in coasting: 35 (trailing rows total 1204)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 955 | 52 | 49 | 2 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 329 | 52 | 22 | 2 | 29 | 78896, 78969 |
| 41 | 83..468 | 386 | 386 | 330 | 56 | 24 | 3 | 29 | 78969, 78971, 79037, 79045 |
| 43 | 86..521 | 436 | 436 | 376 | 60 | 26 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 45 | 90..463 | 374 | 374 | 330 | 44 | 17 | 8 | 20 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 46 | 90..397 | 308 | 308 | 226 | 82 | 15 | 3 | 63 | 78897, 78899, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 48 | 91..301 | 211 | 211 | 160 | 51 | 17 | 2 | 30 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 50 | 93..511 | 419 | 419 | 315 | 104 | 34 | 12 | 50 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 95..215 | 121 | 121 | 79 | 42 | 9 | 2 | 32 | 78969, 78971 |
| 54 | 100..529 | 430 | 430 | 380 | 50 | 18 | 2 | 29 | 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 55 | 100..256 | 157 | 157 | 100 | 57 | 10 | 1 | 47 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 57 | 102..369 | 268 | 268 | 214 | 54 | 20 | 2 | 31 | 78897, 78899, 79037, 79045, 79097 |
| 58 | 103..544 | 442 | 442 | 377 | 65 | 27 | 5 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 62 | 107..313 | 207 | 207 | 125 | 82 | 11 | 4 | 62 | 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..559 | 448 | 448 | 389 | 59 | 26 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..479 | 368 | 368 | 304 | 64 | 24 | 6 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 70 | 116..556 | 441 | 441 | 382 | 59 | 28 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 72 | 122..566 | 445 | 445 | 383 | 62 | 31 | 2 | 28 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 122..571 | 450 | 450 | 392 | 58 | 25 | 3 | 29 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 126..510 | 385 | 385 | 333 | 52 | 15 | 3 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 82 | 132..215 | 84 | 84 | 47 | 37 | 6 | 2 | 30 | 79136, 79139 |
| 83 | 132..510 | 379 | 379 | 319 | 60 | 27 | 3 | 30 | 79098, 79102, 79103, 79105 |
| 84 | 132..561 | 430 | 430 | 378 | 52 | 22 | 2 | 29 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 139..513 | 375 | 375 | 332 | 43 | 14 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 91 | 145..562 | 418 | 418 | 371 | 47 | 15 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 106 | 177..474 | 298 | 298 | 248 | 50 | 15 | 3 | 29 | 78897, 78899, 79037, 79045 |
| 124 | 207..560 | 354 | 354 | 304 | 50 | 18 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 133 | 230..484 | 255 | 255 | 206 | 49 | 18 | 2 | 29 | 78899, 79097 |
| 152 | 281..460 | 180 | 180 | 121 | 59 | 3 | 2 | 54 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 161 | 314..496 | 183 | 183 | 142 | 41 | 9 | 4 | 29 | 79097, 79098 |
| 177 | 344..567 | 224 | 224 | 189 | 35 | 5 | 1 | 30 | 79128, 79134, 79135, 79139 |
| 181 | 353..437 | 85 | 85 | 23 | 62 | 1 | 1 | 61 | 79136 |
| 195 | 384..526 | 143 | 143 | 108 | 35 | 5 | 2 | 29 | 79105, 79110 |
| 210 | 421..472 | 52 | 52 | 21 | 31 | 1 | 1 | 30 | 79037, 79045 |
| 301 | 633..662 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 306 | 647..700 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 36; matched pairs: 9288; unmatched reference entries: 854; unmatched candidate entries: 1940
- identity switches: 622; fragmentation (coverage interruptions): 670; orphan candidate ids (never on a reference object): 2

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 43 -> 45 at (2115, 3033.5), 1 frames after previous cover
- f91: ref 78897: 46 -> 48 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 43 -> 45 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 45 -> 50 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78897: 48 -> 43 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 46 -> 48 at (2140.5, 3029), 1 frames after previous cover
- f94: ref 79037: 43 -> 45 at (2112.5, 3034), 1 frames after previous cover
- f94: ref 79045: 45 -> 50 at (2100.5, 3033), 1 frames after previous cover
- f95: ref 78971: 50 -> 51 at (2084, 3033.5), 2 frames after previous cover
- f98: ref 78969: 41 -> 51 at (2047.5, 3033), 2 frames after previous cover
- f98: ref 78971: 51 -> 41 at (2066, 3034), 1 frames after previous cover
- f98: ref 79097: 46 -> 48 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 46 -> 48 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78899: 48 -> 43 at (2104, 3030.5), 3 frames after previous cover
- f100: ref 79097: 48 -> 54 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78897: 43 -> 57 at (2077, 3031.5), 3 frames after previous cover
- f102: ref 79103: 55 -> 46 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 46 -> 58 at (2124.5, 3027.5), 2 frames after previous cover
- f105: ref 78899: 43 -> 57 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 54 -> 43 at (2088, 3029), 2 frames after previous cover
- f105: ref 79098: 48 -> 54 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 58 -> 48 at (2113.5, 3026.5), 1 frames after previous cover
- f106: ref 78897: 57 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 43 -> 57 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 54 -> 43 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 46 -> 54 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 55 -> 58 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 78897: 45 -> 57 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 57 -> 62 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 57 -> 45 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 45 -> 50 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 50 -> 41 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 62 -> 43 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 43 -> 62 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78969: 51 -> 38 at (1978, 3034.5), 1 frames after previous cover
- f110: ref 78969: 38 -> 51 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 58 -> 54 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 55 -> 58 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 46 -> 55 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 62 -> 48 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 48 -> 62 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 41 -> 66 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 54 -> 65 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 54 -> 62 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 65 -> 54 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 58 -> 65 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 55 -> 58 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 46 -> 55 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 48 -> 43 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 62 -> 48 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 65 -> 58 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 58 -> 65 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 43 -> 45 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 45 -> 50 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79097: 45 -> 43 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 55 -> 65 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 46 -> 55 at (2118, 3022), 1 frames after previous cover
- f119: ref 78897: 50 -> 45 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 79098: 43 -> 48 at (2019, 3029.5), 2 frames after previous cover
- f121: ref 78899: 57 -> 45 at (1976, 3033), 1 frames after previous cover
- ... 562 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 955 | 49 | 0 (955) |
| 78896 | 350 (76..429) | 322 | 23 | 38 (322) |
| 78969 | 352 (80..434) | 319 | 27 | 66 (135), 45 (129), 51 (35), 41 (13), 38 (7) |
| 78971 | 352 (84..439) | 318 | 28 | 41 (247), 51 (44), 50 (12), 66 (7), 43 (4), 45 (4) |
| 79045 | 355 (84..443) | 322 | 22 | 66 (96), 41 (69), 45 (61), 57 (36), 106 (26), 210 (19), 50 (14), 43 (1) |
| 79037 | 355 (86..445) | 315 | 24 | 106 (162), 45 (44), 66 (41), 57 (33), 50 (29), 43 (3), 210 (2), 41 (1) |
| 78897 | 345 (89..450) | 309 | 27 | 50 (103), 57 (83), 106 (53), 45 (34), 66 (25), 43 (7), 48 (3), 46 (1) |
| 78899 | 365 (91..455) | 330 | 29 | 133 (183), 57 (55), 45 (52), 50 (22), 106 (7), 43 (5), 46 (3), 48 (3) |
| 79097 | 366 (94..461) | 332 | 30 | 50 (122), 43 (76), 161 (68), 133 (23), 48 (21), 57 (7), 45 (6), 46 (4), 54 (4), 62 (1) |
| 79098 | 360 (97..467) | 329 | 23 | 83 (147), 48 (78), 161 (74), 50 (13), 43 (11), 62 (3), 46 (1), 54 (1), 78 (1) |
| 79102 | 371 (98..477) | 325 | 29 | 83 (108), 78 (74), 48 (53), 87 (48), 43 (33), 62 (4), 46 (3), 58 (2) |
| 79103 | 380 (99..481) | 336 | 28 | 78 (109), 43 (72), 87 (62), 83 (58), 124 (12), 62 (10), 54 (6), 46 (4), 48 (2), 55 (1) |
| 79105 | 379 (101..484) | 347 | 24 | 78 (136), 87 (83), 43 (54), 195 (26), 54 (15), 124 (15), 83 (6), 58 (4), 55 (3), 84 (3), 65 (2) |
| 79108 | 385 (104..492) | 353 | 26 | 43 (110), 124 (95), 54 (84), 87 (25), 58 (14), 78 (13), 55 (5), 84 (3), 65 (2), 62 (2) |
| 79110 | 388 (106..497) | 365 | 17 | 195 (82), 54 (77), 87 (55), 58 (50), 91 (37), 124 (34), 70 (12), 62 (5), 55 (4), 74 (4), 46 (3), 65 (2) |
| 79111 | 386 (109..500) | 357 | 23 | 54 (109), 58 (61), 87 (45), 84 (43), 124 (31), 91 (27), 70 (18), 65 (8), 46 (4), 55 (4), 62 (4), 74 (3) |
| 79115 | 421 (111..531) | 392 | 22 | 124 (117), 84 (104), 54 (46), 70 (45), 58 (21), 65 (19), 55 (14), 87 (9), 91 (8), 62 (5), 46 (4) |
| 79116 | 411 (114..530) | 378 | 23 | 65 (151), 84 (49), 91 (44), 62 (42), 70 (32), 58 (22), 152 (18), 54 (7), 55 (6), 87 (5), 74 (2) |
| 79122 | 404 (118..532) | 367 | 35 | 84 (114), 55 (43), 70 (39), 62 (37), 58 (34), 65 (32), 91 (28), 54 (27), 46 (7), 74 (6) |
| 79132 | 391 (120..515) | 359 | 24 | 58 (117), 70 (52), 84 (50), 74 (49), 152 (39), 55 (20), 65 (18), 54 (4), 46 (3), 91 (3), 72 (2), 62 (2) |
| 79128 | 402 (124..527) | 367 | 30 | 74 (100), 70 (97), 65 (66), 58 (52), 177 (27), 84 (12), 72 (4), 46 (4), 91 (3), 152 (2) |
| 79134 | 407 (127..533) | 380 | 25 | 177 (112), 70 (86), 74 (68), 91 (63), 65 (25), 72 (15), 152 (6), 46 (5) |
| 79135 | 409 (129..542) | 379 | 22 | 72 (148), 74 (77), 65 (64), 46 (49), 91 (29), 152 (9), 177 (2), 70 (1) |
| 79139 | 406 (132..537) | 373 | 31 | 72 (98), 74 (83), 46 (60), 177 (48), 152 (47), 91 (35), 82 (2) |
| 79136 | 393 (136..538) | 359 | 29 | 72 (116), 91 (94), 46 (71), 82 (45), 181 (23), 62 (10) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 301 | 633..662 | 30 | 0 | 30 |
| 306 | 647..700 | 54 | 0 | 54 |

### Gaps and durations of candidate tracks
- tracks: 36; lifespan min/median/max: 30/368/1007; tracks with internal gaps: 34; total internal gaps: 607; longest internal gap: 12; tracks ending in coasting: 35 (trailing rows total 1204)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 955 | 52 | 49 | 2 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 329 | 52 | 22 | 2 | 29 | 78896, 78969 |
| 41 | 83..468 | 386 | 386 | 330 | 56 | 24 | 3 | 29 | 78969, 78971, 79037, 79045 |
| 43 | 86..521 | 436 | 436 | 376 | 60 | 26 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 45 | 90..463 | 374 | 374 | 330 | 44 | 17 | 8 | 20 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 46 | 90..397 | 308 | 308 | 226 | 82 | 15 | 3 | 63 | 78897, 78899, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 48 | 91..301 | 211 | 211 | 160 | 51 | 17 | 2 | 30 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 50 | 93..511 | 419 | 419 | 315 | 104 | 34 | 12 | 50 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 51 | 95..215 | 121 | 121 | 79 | 42 | 9 | 2 | 32 | 78969, 78971 |
| 54 | 100..529 | 430 | 430 | 380 | 50 | 18 | 2 | 29 | 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 55 | 100..256 | 157 | 157 | 100 | 57 | 10 | 1 | 47 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 57 | 102..369 | 268 | 268 | 214 | 54 | 20 | 2 | 31 | 78897, 78899, 79037, 79045, 79097 |
| 58 | 103..544 | 442 | 442 | 377 | 65 | 27 | 5 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 62 | 107..313 | 207 | 207 | 125 | 82 | 11 | 4 | 62 | 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79136 |
| 65 | 112..559 | 448 | 448 | 389 | 59 | 26 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..479 | 368 | 368 | 304 | 64 | 24 | 6 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 70 | 116..556 | 441 | 441 | 382 | 59 | 28 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 72 | 122..566 | 445 | 445 | 383 | 62 | 31 | 2 | 28 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 122..571 | 450 | 450 | 392 | 58 | 25 | 3 | 29 | 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 126..510 | 385 | 385 | 333 | 52 | 15 | 3 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 82 | 132..215 | 84 | 84 | 47 | 37 | 6 | 2 | 30 | 79136, 79139 |
| 83 | 132..510 | 379 | 379 | 319 | 60 | 27 | 3 | 30 | 79098, 79102, 79103, 79105 |
| 84 | 132..561 | 430 | 430 | 378 | 52 | 22 | 2 | 29 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132 |
| 87 | 139..513 | 375 | 375 | 332 | 43 | 14 | 1 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 91 | 145..562 | 418 | 418 | 371 | 47 | 15 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 106 | 177..474 | 298 | 298 | 248 | 50 | 15 | 3 | 29 | 78897, 78899, 79037, 79045 |
| 124 | 207..560 | 354 | 354 | 304 | 50 | 18 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115 |
| 133 | 230..484 | 255 | 255 | 206 | 49 | 18 | 2 | 29 | 78899, 79097 |
| 152 | 281..460 | 180 | 180 | 121 | 59 | 3 | 2 | 54 | 79116, 79128, 79132, 79134, 79135, 79139 |
| 161 | 314..496 | 183 | 183 | 142 | 41 | 9 | 4 | 29 | 79097, 79098 |
| 177 | 344..567 | 224 | 224 | 189 | 35 | 5 | 1 | 30 | 79128, 79134, 79135, 79139 |
| 181 | 353..437 | 85 | 85 | 23 | 62 | 1 | 1 | 61 | 79136 |
| 195 | 384..526 | 143 | 143 | 108 | 35 | 5 | 2 | 29 | 79105, 79110 |
| 210 | 421..472 | 52 | 52 | 21 | 31 | 1 | 1 | 30 | 79037, 79045 |
| 301 | 633..662 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 306 | 647..700 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |
