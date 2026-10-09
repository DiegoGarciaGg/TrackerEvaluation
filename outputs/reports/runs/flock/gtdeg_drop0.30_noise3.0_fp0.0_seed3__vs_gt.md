# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=416eae213bbe
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise3.0_fp0.0_seed3/tracks.csv sha256=4fdacd5ca1fdd37b
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise3.0_fp0.0_seed3.csv sha256=416eae213bbe255e
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise3.0_fp0.0_seed3
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
| observations | none | 4 | 10142 | 7081 | 0.176 | 0.324 | 0.096 | 2.18 | 0.178 | 0.043 | 2.39 | 842 | 2432.0 | 0.211 | 0.256 | 0.179 | 0.412 | 0.590 | 4179 | 5963 | 2902 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 7081 | 0.241 | 0.448 | 0.130 | 2.72 | 0.297 | 0.412 | 3.20 | 1066 | 2325.0 | 0.307 | 0.373 | 0.261 | 0.608 | 0.870 | 6163 | 3979 | 918 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 7081 | 0.276 | 0.508 | 0.150 | 3.03 | 0.346 | 0.544 | 3.59 | 1100 | 2077.0 | 0.346 | 0.421 | 0.294 | 0.675 | 0.967 | 6848 | 3294 | 233 | 0 | 25 | 0 |
| observations | none | 12 | 10142 | 7081 | 0.312 | 0.548 | 0.178 | 3.59 | 0.363 | 0.587 | 3.92 | 1022 | 1947.0 | 0.376 | 0.458 | 0.320 | 0.693 | 0.993 | 7030 | 3112 | 51 | 0 | 25 | 0 |
| observations | ignore | 4 | 10142 | 7081 | 0.176 | 0.324 | 0.096 | 2.18 | 0.178 | 0.043 | 2.39 | 842 | 2432.0 | 0.211 | 0.256 | 0.179 | 0.412 | 0.590 | 4179 | 5963 | 2902 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 7081 | 0.241 | 0.448 | 0.130 | 2.72 | 0.297 | 0.412 | 3.20 | 1066 | 2325.0 | 0.307 | 0.373 | 0.261 | 0.608 | 0.870 | 6163 | 3979 | 918 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 7081 | 0.276 | 0.508 | 0.150 | 3.03 | 0.346 | 0.544 | 3.59 | 1100 | 2077.0 | 0.346 | 0.421 | 0.294 | 0.675 | 0.967 | 6848 | 3294 | 233 | 0 | 25 | 0 |
| observations | ignore | 12 | 10142 | 7081 | 0.312 | 0.548 | 0.178 | 3.59 | 0.363 | 0.587 | 3.92 | 1022 | 1947.0 | 0.376 | 0.458 | 0.320 | 0.693 | 0.993 | 7030 | 3112 | 51 | 0 | 25 | 0 |
| updates | none | 4 | 10142 | 9828 | 0.179 | 0.313 | 0.102 | 2.23 | 0.172 | -0.155 | 2.42 | 944 | 2452.0 | 0.206 | 0.209 | 0.203 | 0.454 | 0.468 | 4600 | 5542 | 5228 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 9828 | 0.261 | 0.458 | 0.149 | 2.87 | 0.304 | 0.296 | 3.29 | 1164 | 1992.0 | 0.314 | 0.319 | 0.309 | 0.690 | 0.712 | 6996 | 3146 | 2832 | 0 | 25 | 0 |
| updates | none | 8 | 10142 | 9828 | 0.313 | 0.541 | 0.181 | 3.30 | 0.380 | 0.510 | 3.80 | 1169 | 1408.0 | 0.371 | 0.376 | 0.365 | 0.797 | 0.822 | 8083 | 2059 | 1745 | 8 | 17 | 0 |
| updates | none | 12 | 10142 | 9828 | 0.370 | 0.612 | 0.224 | 4.02 | 0.437 | 0.657 | 4.46 | 1010 | 912.0 | 0.428 | 0.435 | 0.422 | 0.863 | 0.890 | 8751 | 1391 | 1077 | 24 | 1 | 0 |
| updates | ignore | 4 | 10142 | 9828 | 0.179 | 0.313 | 0.102 | 2.23 | 0.172 | -0.155 | 2.42 | 944 | 2452.0 | 0.206 | 0.209 | 0.203 | 0.454 | 0.468 | 4600 | 5542 | 5228 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 9828 | 0.261 | 0.458 | 0.149 | 2.87 | 0.304 | 0.296 | 3.29 | 1164 | 1992.0 | 0.314 | 0.319 | 0.309 | 0.690 | 0.712 | 6996 | 3146 | 2832 | 0 | 25 | 0 |
| updates | ignore | 8 | 10142 | 9828 | 0.313 | 0.541 | 0.181 | 3.30 | 0.380 | 0.510 | 3.80 | 1169 | 1408.0 | 0.371 | 0.376 | 0.365 | 0.797 | 0.822 | 8083 | 2059 | 1745 | 8 | 17 | 0 |
| updates | ignore | 12 | 10142 | 9828 | 0.370 | 0.612 | 0.224 | 4.02 | 0.437 | 0.657 | 4.46 | 1010 | 912.0 | 0.428 | 0.435 | 0.422 | 0.863 | 0.890 | 8751 | 1391 | 1077 | 24 | 1 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 6848; unmatched reference entries: 3294; unmatched candidate entries: 233
- identity switches: 1100; fragmentation (coverage interruptions): 2131; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 4 -> 5 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 4 -> 6 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 6 -> 5 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 4 -> 6 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 5 -> 8 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 6 -> 5 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 5 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 8 -> 5 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 4 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 4 -> 9 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 5 -> 8 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 9 -> 4 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 8 -> 5 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 5 -> 8 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 8 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 8 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 6 -> 4 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 10 -> 8 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 8 -> 3 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 3 -> 10 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 6 -> 4 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 4 -> 6 at (2119, 3027), 3 frames after previous cover
- f106: ref 78897: 5 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 5 -> 12 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79037: 3 -> 10 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 10 -> 8 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79097: 4 -> 5 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 9 -> 6 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 8 -> 13 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 12 -> 5 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 10 -> 12 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 10 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 5 -> 4 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 5 -> 12 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 13 -> 2 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 4 -> 3 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 9 -> 5 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 6 -> 4 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 6 -> 9 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 8 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 12 -> 10 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 10 -> 8 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 9 -> 4 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 3 -> 10 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 10 -> 8 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 8 -> 10 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 9 -> 5 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 12 -> 8 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 3 -> 10 at (2034.5, 3030), 2 frames after previous cover
- ... 1040 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 675 | 219 | 0 (675) |
| 78896 | 350 (76..429) | 238 | 78 | 2 (215), 13 (23) |
| 78969 | 352 (80..434) | 238 | 71 | 8 (175), 2 (47), 3 (11), 13 (5) |
| 78971 | 352 (84..439) | 236 | 74 | 36 (52), 8 (45), 30 (39), 21 (36), 13 (31), 12 (19), 3 (6), 5 (3), 2 (3), 10 (2) |
| 79045 | 355 (84..443) | 233 | 76 | 12 (62), 21 (57), 36 (43), 13 (30), 8 (20), 30 (12), 10 (3), 5 (2), 3 (2), 4 (1), 2 (1) |
| 79037 | 355 (86..445) | 227 | 78 | 12 (63), 21 (59), 36 (32), 30 (31), 13 (16), 5 (6), 8 (6), 9 (5), 10 (4), 4 (2), 3 (2), 6 (1) |
| 78897 | 345 (89..450) | 234 | 70 | 12 (81), 30 (69), 21 (40), 36 (16), 8 (7), 9 (5), 6 (4), 3 (4), 5 (3), 4 (2), 10 (2), 13 (1) |
| 78899 | 365 (91..455) | 255 | 72 | 3 (81), 9 (50), 30 (49), 21 (36), 12 (27), 4 (5), 5 (3), 8 (3), 6 (1) |
| 79097 | 366 (94..461) | 245 | 81 | 3 (98), 4 (47), 9 (37), 13 (30), 30 (15), 21 (8), 12 (4), 10 (3), 5 (2), 6 (1) |
| 79098 | 360 (97..467) | 262 | 66 | 4 (117), 9 (76), 3 (19), 6 (13), 10 (9), 19 (9), 13 (9), 5 (6), 21 (3), 12 (1) |
| 79102 | 371 (98..477) | 260 | 72 | 6 (74), 4 (56), 3 (36), 9 (34), 13 (20), 19 (14), 5 (11), 10 (10), 30 (3), 21 (1), 34 (1) |
| 79103 | 380 (99..481) | 254 | 81 | 6 (94), 4 (60), 9 (28), 34 (27), 5 (17), 13 (14), 30 (6), 3 (4), 19 (3), 10 (1) |
| 79105 | 379 (101..484) | 263 | 84 | 6 (65), 5 (45), 34 (44), 35 (39), 13 (25), 9 (15), 4 (8), 30 (8), 3 (6), 19 (4), 10 (2), 24 (2) |
| 79108 | 385 (104..492) | 278 | 79 | 34 (76), 5 (74), 13 (33), 35 (27), 19 (23), 24 (17), 3 (10), 6 (8), 30 (6), 4 (2), 9 (2) |
| 79110 | 388 (106..497) | 253 | 74 | 35 (53), 9 (52), 19 (48), 24 (31), 13 (18), 34 (13), 10 (11), 5 (8), 3 (6), 28 (6), 6 (4), 30 (2), +1 more |
| 79111 | 386 (109..500) | 265 | 75 | 13 (56), 10 (48), 35 (38), 24 (37), 19 (33), 34 (29), 3 (10), 6 (8), 9 (2), 15 (1), 20 (1), 5 (1), +1 more |
| 79115 | 421 (111..531) | 272 | 90 | 10 (123), 19 (31), 34 (29), 5 (27), 35 (16), 24 (15), 28 (10), 3 (7), 20 (6), 15 (4), 6 (4) |
| 79116 | 411 (114..530) | 272 | 86 | 24 (68), 5 (63), 20 (39), 35 (18), 34 (18), 19 (16), 6 (14), 10 (14), 28 (11), 3 (7), 15 (4) |
| 79122 | 404 (118..532) | 266 | 89 | 20 (126), 5 (45), 35 (26), 24 (25), 28 (19), 6 (13), 10 (9), 15 (2), 19 (1) |
| 79132 | 391 (120..515) | 267 | 88 | 24 (66), 19 (62), 10 (58), 20 (29), 35 (27), 28 (19), 6 (4), 15 (2) |
| 79128 | 402 (124..527) | 280 | 86 | 19 (71), 28 (69), 24 (39), 20 (26), 5 (26), 10 (22), 27 (18), 15 (8), 6 (1) |
| 79134 | 407 (127..533) | 280 | 85 | 27 (123), 20 (55), 28 (52), 15 (45), 31 (4), 6 (1) |
| 79135 | 409 (129..542) | 269 | 85 | 28 (113), 27 (86), 20 (40), 15 (27), 31 (3) |
| 79139 | 406 (132..537) | 274 | 89 | 15 (145), 31 (103), 27 (26) |
| 79136 | 393 (136..538) | 252 | 83 | 31 (158), 15 (72), 27 (22) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 195/393/1004; tracks with internal gaps: 23; total internal gaps: 221; longest internal gap: 2; tracks ending in coasting: 2 (trailing rows total 2)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1007 | 1004 | 700 | 675 | 25 | 24 | 2 | 0 | 78911 |
| 2 | 80..429 | 350 | 271 | 266 | 5 | 5 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 3 | 82..476 | 395 | 319 | 309 | 10 | 10 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 4 | 86..467 | 382 | 308 | 300 | 8 | 7 | 1 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 5 | 88..531 | 444 | 354 | 342 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 6 | 89..481 | 393 | 326 | 310 | 16 | 14 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..439 | 343 | 265 | 256 | 9 | 8 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 9 | 100..496 | 397 | 314 | 306 | 8 | 7 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 10 | 102..530 | 429 | 335 | 321 | 14 | 11 | 2 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 12 | 106..454 | 349 | 261 | 257 | 4 | 4 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 13 | 106..500 | 395 | 323 | 311 | 12 | 11 | 2 | 0 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 108..533 | 426 | 318 | 311 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 116..526 | 411 | 322 | 315 | 7 | 7 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 20 | 116..529 | 414 | 327 | 322 | 5 | 5 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 21 | 117..444 | 328 | 250 | 240 | 10 | 10 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 24 | 125..515 | 391 | 310 | 300 | 10 | 10 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 27 | 137..537 | 401 | 285 | 275 | 10 | 10 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 28 | 137..542 | 406 | 313 | 300 | 13 | 13 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 30 | 137..460 | 324 | 252 | 240 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 31 | 151..538 | 388 | 275 | 268 | 7 | 7 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 34 | 177..492 | 316 | 247 | 237 | 10 | 10 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 35 | 177..484 | 308 | 257 | 244 | 13 | 12 | 1 | 1 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 36 | 256..450 | 195 | 149 | 143 | 6 | 5 | 2 | 0 | 78897, 78971, 79037, 79045 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 6848; unmatched reference entries: 3294; unmatched candidate entries: 233
- identity switches: 1100; fragmentation (coverage interruptions): 2131; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 4 -> 5 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 4 -> 6 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 6 -> 5 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 4 -> 6 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 5 -> 8 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 6 -> 5 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 5 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 8 -> 5 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 4 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 4 -> 9 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 5 -> 8 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 9 -> 4 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 8 -> 5 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 5 -> 8 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 8 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 8 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 6 -> 4 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 10 -> 8 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 8 -> 3 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 3 -> 10 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 6 -> 4 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 4 -> 6 at (2119, 3027), 3 frames after previous cover
- f106: ref 78897: 5 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 5 -> 12 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79037: 3 -> 10 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 10 -> 8 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79097: 4 -> 5 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 9 -> 6 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 8 -> 13 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 12 -> 5 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 10 -> 12 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 10 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 5 -> 4 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 5 -> 12 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 13 -> 2 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 4 -> 3 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 9 -> 5 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 6 -> 4 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 6 -> 9 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 8 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 12 -> 10 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 10 -> 8 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 9 -> 4 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 3 -> 10 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 10 -> 8 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 8 -> 10 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 9 -> 5 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 12 -> 8 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 3 -> 10 at (2034.5, 3030), 2 frames after previous cover
- ... 1040 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 675 | 219 | 0 (675) |
| 78896 | 350 (76..429) | 238 | 78 | 2 (215), 13 (23) |
| 78969 | 352 (80..434) | 238 | 71 | 8 (175), 2 (47), 3 (11), 13 (5) |
| 78971 | 352 (84..439) | 236 | 74 | 36 (52), 8 (45), 30 (39), 21 (36), 13 (31), 12 (19), 3 (6), 5 (3), 2 (3), 10 (2) |
| 79045 | 355 (84..443) | 233 | 76 | 12 (62), 21 (57), 36 (43), 13 (30), 8 (20), 30 (12), 10 (3), 5 (2), 3 (2), 4 (1), 2 (1) |
| 79037 | 355 (86..445) | 227 | 78 | 12 (63), 21 (59), 36 (32), 30 (31), 13 (16), 5 (6), 8 (6), 9 (5), 10 (4), 4 (2), 3 (2), 6 (1) |
| 78897 | 345 (89..450) | 234 | 70 | 12 (81), 30 (69), 21 (40), 36 (16), 8 (7), 9 (5), 6 (4), 3 (4), 5 (3), 4 (2), 10 (2), 13 (1) |
| 78899 | 365 (91..455) | 255 | 72 | 3 (81), 9 (50), 30 (49), 21 (36), 12 (27), 4 (5), 5 (3), 8 (3), 6 (1) |
| 79097 | 366 (94..461) | 245 | 81 | 3 (98), 4 (47), 9 (37), 13 (30), 30 (15), 21 (8), 12 (4), 10 (3), 5 (2), 6 (1) |
| 79098 | 360 (97..467) | 262 | 66 | 4 (117), 9 (76), 3 (19), 6 (13), 10 (9), 19 (9), 13 (9), 5 (6), 21 (3), 12 (1) |
| 79102 | 371 (98..477) | 260 | 72 | 6 (74), 4 (56), 3 (36), 9 (34), 13 (20), 19 (14), 5 (11), 10 (10), 30 (3), 21 (1), 34 (1) |
| 79103 | 380 (99..481) | 254 | 81 | 6 (94), 4 (60), 9 (28), 34 (27), 5 (17), 13 (14), 30 (6), 3 (4), 19 (3), 10 (1) |
| 79105 | 379 (101..484) | 263 | 84 | 6 (65), 5 (45), 34 (44), 35 (39), 13 (25), 9 (15), 4 (8), 30 (8), 3 (6), 19 (4), 10 (2), 24 (2) |
| 79108 | 385 (104..492) | 278 | 79 | 34 (76), 5 (74), 13 (33), 35 (27), 19 (23), 24 (17), 3 (10), 6 (8), 30 (6), 4 (2), 9 (2) |
| 79110 | 388 (106..497) | 253 | 74 | 35 (53), 9 (52), 19 (48), 24 (31), 13 (18), 34 (13), 10 (11), 5 (8), 3 (6), 28 (6), 6 (4), 30 (2), +1 more |
| 79111 | 386 (109..500) | 265 | 75 | 13 (56), 10 (48), 35 (38), 24 (37), 19 (33), 34 (29), 3 (10), 6 (8), 9 (2), 15 (1), 20 (1), 5 (1), +1 more |
| 79115 | 421 (111..531) | 272 | 90 | 10 (123), 19 (31), 34 (29), 5 (27), 35 (16), 24 (15), 28 (10), 3 (7), 20 (6), 15 (4), 6 (4) |
| 79116 | 411 (114..530) | 272 | 86 | 24 (68), 5 (63), 20 (39), 35 (18), 34 (18), 19 (16), 6 (14), 10 (14), 28 (11), 3 (7), 15 (4) |
| 79122 | 404 (118..532) | 266 | 89 | 20 (126), 5 (45), 35 (26), 24 (25), 28 (19), 6 (13), 10 (9), 15 (2), 19 (1) |
| 79132 | 391 (120..515) | 267 | 88 | 24 (66), 19 (62), 10 (58), 20 (29), 35 (27), 28 (19), 6 (4), 15 (2) |
| 79128 | 402 (124..527) | 280 | 86 | 19 (71), 28 (69), 24 (39), 20 (26), 5 (26), 10 (22), 27 (18), 15 (8), 6 (1) |
| 79134 | 407 (127..533) | 280 | 85 | 27 (123), 20 (55), 28 (52), 15 (45), 31 (4), 6 (1) |
| 79135 | 409 (129..542) | 269 | 85 | 28 (113), 27 (86), 20 (40), 15 (27), 31 (3) |
| 79139 | 406 (132..537) | 274 | 89 | 15 (145), 31 (103), 27 (26) |
| 79136 | 393 (136..538) | 252 | 83 | 31 (158), 15 (72), 27 (22) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 195/393/1004; tracks with internal gaps: 23; total internal gaps: 221; longest internal gap: 2; tracks ending in coasting: 2 (trailing rows total 2)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1007 | 1004 | 700 | 675 | 25 | 24 | 2 | 0 | 78911 |
| 2 | 80..429 | 350 | 271 | 266 | 5 | 5 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 3 | 82..476 | 395 | 319 | 309 | 10 | 10 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 4 | 86..467 | 382 | 308 | 300 | 8 | 7 | 1 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 5 | 88..531 | 444 | 354 | 342 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 6 | 89..481 | 393 | 326 | 310 | 16 | 14 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..439 | 343 | 265 | 256 | 9 | 8 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 9 | 100..496 | 397 | 314 | 306 | 8 | 7 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 10 | 102..530 | 429 | 335 | 321 | 14 | 11 | 2 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 12 | 106..454 | 349 | 261 | 257 | 4 | 4 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 13 | 106..500 | 395 | 323 | 311 | 12 | 11 | 2 | 0 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 108..533 | 426 | 318 | 311 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 116..526 | 411 | 322 | 315 | 7 | 7 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 20 | 116..529 | 414 | 327 | 322 | 5 | 5 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 21 | 117..444 | 328 | 250 | 240 | 10 | 10 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 24 | 125..515 | 391 | 310 | 300 | 10 | 10 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 27 | 137..537 | 401 | 285 | 275 | 10 | 10 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 28 | 137..542 | 406 | 313 | 300 | 13 | 13 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 30 | 137..460 | 324 | 252 | 240 | 12 | 12 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 31 | 151..538 | 388 | 275 | 268 | 7 | 7 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 34 | 177..492 | 316 | 247 | 237 | 10 | 10 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 35 | 177..484 | 308 | 257 | 244 | 13 | 12 | 1 | 1 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 36 | 256..450 | 195 | 149 | 143 | 6 | 5 | 2 | 0 | 78897, 78971, 79037, 79045 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 8083; unmatched reference entries: 2059; unmatched candidate entries: 1745
- identity switches: 1169; fragmentation (coverage interruptions): 1347; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 4 -> 5 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 4 -> 6 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 6 -> 5 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 4 -> 6 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 5 -> 8 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 6 -> 5 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 5 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 8 -> 5 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 4 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 4 -> 9 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 5 -> 8 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 9 -> 4 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 8 -> 5 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 5 -> 8 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 8 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 8 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 6 -> 4 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 10 -> 8 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 8 -> 3 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 3 -> 10 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 6 -> 4 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 4 -> 6 at (2119, 3027), 2 frames after previous cover
- f106: ref 78897: 5 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 5 -> 12 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79037: 3 -> 10 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 10 -> 8 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79097: 4 -> 5 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 9 -> 6 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 8 -> 13 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 12 -> 5 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 10 -> 12 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 10 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 5 -> 4 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 5 -> 12 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 13 -> 2 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 4 -> 3 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 9 -> 5 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 6 -> 4 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 6 -> 9 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 8 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 12 -> 10 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 10 -> 8 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 9 -> 4 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 3 -> 10 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 10 -> 8 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 8 -> 10 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 9 -> 5 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 12 -> 8 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 3 -> 10 at (2034.5, 3030), 1 frames after previous cover
- ... 1109 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 910 | 70 | 0 (910) |
| 78896 | 350 (76..429) | 282 | 48 | 2 (256), 13 (26) |
| 78969 | 352 (80..434) | 277 | 45 | 8 (210), 2 (50), 3 (12), 13 (5) |
| 78971 | 352 (84..439) | 265 | 55 | 36 (63), 30 (47), 8 (44), 21 (37), 13 (33), 12 (22), 3 (7), 2 (7), 5 (3), 10 (2) |
| 79045 | 355 (84..443) | 271 | 58 | 12 (71), 21 (67), 36 (52), 13 (35), 8 (23), 30 (13), 10 (4), 5 (2), 3 (2), 4 (1), 2 (1) |
| 79037 | 355 (86..445) | 259 | 64 | 12 (73), 21 (71), 36 (35), 30 (34), 13 (17), 5 (7), 8 (6), 9 (5), 10 (4), 4 (2), 3 (2), 2 (2), +1 more |
| 78897 | 345 (89..450) | 276 | 50 | 12 (94), 30 (84), 21 (53), 36 (17), 8 (7), 6 (5), 3 (4), 9 (4), 5 (3), 4 (2), 10 (2), 13 (1) |
| 78899 | 365 (91..455) | 295 | 43 | 3 (93), 9 (58), 30 (56), 21 (42), 12 (30), 4 (6), 8 (5), 5 (4), 6 (1) |
| 79097 | 366 (94..461) | 282 | 60 | 3 (115), 4 (51), 9 (44), 13 (33), 30 (14), 21 (13), 12 (5), 10 (4), 5 (2), 6 (1) |
| 79098 | 360 (97..467) | 290 | 45 | 4 (129), 9 (88), 3 (20), 6 (14), 10 (11), 19 (9), 13 (9), 5 (6), 21 (3), 12 (1) |
| 79102 | 371 (98..477) | 301 | 49 | 6 (89), 4 (68), 3 (42), 9 (39), 13 (22), 19 (14), 10 (11), 5 (11), 30 (3), 21 (1), 34 (1) |
| 79103 | 380 (99..481) | 280 | 66 | 6 (102), 4 (64), 9 (33), 34 (29), 5 (18), 13 (14), 3 (9), 30 (6), 19 (4), 10 (1) |
| 79105 | 379 (101..484) | 301 | 53 | 6 (69), 34 (53), 5 (51), 35 (49), 13 (27), 9 (16), 4 (12), 30 (8), 3 (7), 19 (5), 10 (2), 24 (2) |
| 79108 | 385 (104..492) | 313 | 51 | 34 (91), 5 (81), 13 (38), 35 (31), 19 (26), 24 (18), 3 (10), 6 (8), 30 (6), 4 (2), 9 (2) |
| 79110 | 388 (106..497) | 296 | 48 | 9 (64), 35 (62), 19 (52), 24 (36), 13 (19), 5 (15), 34 (14), 10 (11), 3 (7), 28 (7), 6 (5), 30 (3), +1 more |
| 79111 | 386 (109..500) | 303 | 50 | 13 (67), 10 (58), 24 (42), 35 (40), 19 (39), 34 (33), 6 (8), 3 (6), 28 (3), 15 (2), 5 (2), 9 (2), +1 more |
| 79115 | 421 (111..531) | 332 | 50 | 10 (164), 34 (34), 5 (33), 19 (30), 35 (19), 24 (16), 3 (12), 28 (12), 15 (4), 20 (4), 6 (4) |
| 79116 | 411 (114..530) | 318 | 58 | 24 (79), 5 (74), 20 (49), 19 (22), 34 (22), 35 (20), 10 (16), 6 (15), 28 (9), 3 (8), 15 (4) |
| 79122 | 404 (118..532) | 324 | 53 | 20 (157), 5 (55), 35 (33), 24 (29), 28 (23), 6 (13), 10 (7), 19 (4), 15 (2), 34 (1) |
| 79132 | 391 (120..515) | 312 | 57 | 24 (84), 19 (79), 10 (62), 20 (32), 35 (27), 28 (22), 6 (4), 15 (2) |
| 79128 | 402 (124..527) | 319 | 58 | 19 (88), 28 (74), 24 (45), 20 (29), 5 (29), 10 (25), 27 (20), 15 (8), 6 (1) |
| 79134 | 407 (127..533) | 326 | 52 | 27 (146), 20 (62), 28 (59), 15 (53), 31 (3), 10 (2), 6 (1) |
| 79135 | 409 (129..542) | 323 | 56 | 28 (135), 27 (106), 20 (49), 15 (28), 31 (4), 10 (1) |
| 79139 | 406 (132..537) | 322 | 62 | 15 (170), 31 (118), 27 (28), 20 (4), 19 (2) |
| 79136 | 393 (136..538) | 306 | 46 | 31 (192), 15 (86), 27 (28) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 224/422/1005; tracks with internal gaps: 23; total internal gaps: 847; longest internal gap: 15; tracks ending in coasting: 22 (trailing rows total 586)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1008 | 1005 | 1005 | 910 | 95 | 71 | 3 | 0 | 78911 |
| 2 | 80..458 | 379 | 379 | 316 | 63 | 36 | 6 | 13 | 78896, 78969, 78971, 79037, 79045 |
| 3 | 82..505 | 424 | 424 | 356 | 68 | 35 | 4 | 21 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 4 | 86..496 | 411 | 411 | 337 | 74 | 32 | 3 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 5 | 88..560 | 473 | 473 | 396 | 77 | 33 | 5 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 6 | 89..510 | 422 | 422 | 341 | 81 | 37 | 4 | 33 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..468 | 372 | 372 | 295 | 77 | 33 | 6 | 25 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 9 | 100..525 | 426 | 426 | 355 | 71 | 33 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 10 | 102..559 | 458 | 458 | 387 | 71 | 31 | 4 | 29 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 12 | 106..483 | 378 | 378 | 296 | 82 | 39 | 5 | 22 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 13 | 106..529 | 424 | 424 | 346 | 78 | 39 | 4 | 29 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 108..562 | 455 | 455 | 360 | 95 | 45 | 6 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 116..555 | 440 | 440 | 374 | 66 | 38 | 3 | 18 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 20 | 116..558 | 443 | 443 | 387 | 56 | 24 | 2 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 21 | 117..473 | 357 | 357 | 287 | 70 | 31 | 15 | 13 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 24 | 125..544 | 420 | 420 | 351 | 69 | 32 | 3 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 27 | 137..566 | 430 | 430 | 328 | 102 | 50 | 7 | 31 | 79128, 79134, 79135, 79136, 79139 |
| 28 | 137..571 | 435 | 435 | 344 | 91 | 45 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 30 | 137..489 | 353 | 353 | 274 | 79 | 36 | 4 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 31 | 151..567 | 417 | 417 | 317 | 100 | 49 | 5 | 29 | 79134, 79135, 79136, 79139 |
| 34 | 177..521 | 345 | 345 | 278 | 67 | 30 | 2 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 35 | 177..513 | 337 | 337 | 281 | 56 | 24 | 2 | 30 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 36 | 256..479 | 224 | 224 | 167 | 57 | 24 | 2 | 29 | 78897, 78971, 79037, 79045 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 23; matched pairs: 8083; unmatched reference entries: 2059; unmatched candidate entries: 1745
- identity switches: 1169; fragmentation (coverage interruptions): 1347; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 4 -> 6 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 4 -> 5 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 4 -> 6 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 3 -> 2 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 5 -> 3 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 6 -> 5 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 2 -> 3 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 4 -> 6 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 3 -> 2 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 5 -> 8 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 6 -> 5 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 5 -> 8 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 8 -> 5 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 4 -> 6 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 6 -> 4 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 4 -> 9 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 5 -> 8 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 6 -> 5 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 4 -> 6 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 9 -> 4 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 8 -> 5 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 3 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 5 -> 8 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 8 -> 3 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 2 -> 8 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 6 -> 4 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 10 -> 8 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 8 -> 3 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 3 -> 10 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 6 -> 4 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 4 -> 6 at (2119, 3027), 2 frames after previous cover
- f106: ref 78897: 5 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 5 -> 12 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79037: 3 -> 10 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 10 -> 8 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79097: 4 -> 5 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 9 -> 6 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 8 -> 13 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 12 -> 5 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 10 -> 12 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 10 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 5 -> 4 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 5 -> 12 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 13 -> 2 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 4 -> 3 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 9 -> 5 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 6 -> 4 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 6 -> 9 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 8 -> 13 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 12 -> 10 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 10 -> 8 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 4 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 9 -> 4 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 3 -> 10 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 10 -> 8 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 8 -> 10 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 9 -> 5 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 12 -> 8 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 3 -> 10 at (2034.5, 3030), 1 frames after previous cover
- ... 1109 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 910 | 70 | 0 (910) |
| 78896 | 350 (76..429) | 282 | 48 | 2 (256), 13 (26) |
| 78969 | 352 (80..434) | 277 | 45 | 8 (210), 2 (50), 3 (12), 13 (5) |
| 78971 | 352 (84..439) | 265 | 55 | 36 (63), 30 (47), 8 (44), 21 (37), 13 (33), 12 (22), 3 (7), 2 (7), 5 (3), 10 (2) |
| 79045 | 355 (84..443) | 271 | 58 | 12 (71), 21 (67), 36 (52), 13 (35), 8 (23), 30 (13), 10 (4), 5 (2), 3 (2), 4 (1), 2 (1) |
| 79037 | 355 (86..445) | 259 | 64 | 12 (73), 21 (71), 36 (35), 30 (34), 13 (17), 5 (7), 8 (6), 9 (5), 10 (4), 4 (2), 3 (2), 2 (2), +1 more |
| 78897 | 345 (89..450) | 276 | 50 | 12 (94), 30 (84), 21 (53), 36 (17), 8 (7), 6 (5), 3 (4), 9 (4), 5 (3), 4 (2), 10 (2), 13 (1) |
| 78899 | 365 (91..455) | 295 | 43 | 3 (93), 9 (58), 30 (56), 21 (42), 12 (30), 4 (6), 8 (5), 5 (4), 6 (1) |
| 79097 | 366 (94..461) | 282 | 60 | 3 (115), 4 (51), 9 (44), 13 (33), 30 (14), 21 (13), 12 (5), 10 (4), 5 (2), 6 (1) |
| 79098 | 360 (97..467) | 290 | 45 | 4 (129), 9 (88), 3 (20), 6 (14), 10 (11), 19 (9), 13 (9), 5 (6), 21 (3), 12 (1) |
| 79102 | 371 (98..477) | 301 | 49 | 6 (89), 4 (68), 3 (42), 9 (39), 13 (22), 19 (14), 10 (11), 5 (11), 30 (3), 21 (1), 34 (1) |
| 79103 | 380 (99..481) | 280 | 66 | 6 (102), 4 (64), 9 (33), 34 (29), 5 (18), 13 (14), 3 (9), 30 (6), 19 (4), 10 (1) |
| 79105 | 379 (101..484) | 301 | 53 | 6 (69), 34 (53), 5 (51), 35 (49), 13 (27), 9 (16), 4 (12), 30 (8), 3 (7), 19 (5), 10 (2), 24 (2) |
| 79108 | 385 (104..492) | 313 | 51 | 34 (91), 5 (81), 13 (38), 35 (31), 19 (26), 24 (18), 3 (10), 6 (8), 30 (6), 4 (2), 9 (2) |
| 79110 | 388 (106..497) | 296 | 48 | 9 (64), 35 (62), 19 (52), 24 (36), 13 (19), 5 (15), 34 (14), 10 (11), 3 (7), 28 (7), 6 (5), 30 (3), +1 more |
| 79111 | 386 (109..500) | 303 | 50 | 13 (67), 10 (58), 24 (42), 35 (40), 19 (39), 34 (33), 6 (8), 3 (6), 28 (3), 15 (2), 5 (2), 9 (2), +1 more |
| 79115 | 421 (111..531) | 332 | 50 | 10 (164), 34 (34), 5 (33), 19 (30), 35 (19), 24 (16), 3 (12), 28 (12), 15 (4), 20 (4), 6 (4) |
| 79116 | 411 (114..530) | 318 | 58 | 24 (79), 5 (74), 20 (49), 19 (22), 34 (22), 35 (20), 10 (16), 6 (15), 28 (9), 3 (8), 15 (4) |
| 79122 | 404 (118..532) | 324 | 53 | 20 (157), 5 (55), 35 (33), 24 (29), 28 (23), 6 (13), 10 (7), 19 (4), 15 (2), 34 (1) |
| 79132 | 391 (120..515) | 312 | 57 | 24 (84), 19 (79), 10 (62), 20 (32), 35 (27), 28 (22), 6 (4), 15 (2) |
| 79128 | 402 (124..527) | 319 | 58 | 19 (88), 28 (74), 24 (45), 20 (29), 5 (29), 10 (25), 27 (20), 15 (8), 6 (1) |
| 79134 | 407 (127..533) | 326 | 52 | 27 (146), 20 (62), 28 (59), 15 (53), 31 (3), 10 (2), 6 (1) |
| 79135 | 409 (129..542) | 323 | 56 | 28 (135), 27 (106), 20 (49), 15 (28), 31 (4), 10 (1) |
| 79139 | 406 (132..537) | 322 | 62 | 15 (170), 31 (118), 27 (28), 20 (4), 19 (2) |
| 79136 | 393 (136..538) | 306 | 46 | 31 (192), 15 (86), 27 (28) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 23; lifespan min/median/max: 224/422/1005; tracks with internal gaps: 23; total internal gaps: 847; longest internal gap: 15; tracks ending in coasting: 22 (trailing rows total 586)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1008 | 1005 | 1005 | 910 | 95 | 71 | 3 | 0 | 78911 |
| 2 | 80..458 | 379 | 379 | 316 | 63 | 36 | 6 | 13 | 78896, 78969, 78971, 79037, 79045 |
| 3 | 82..505 | 424 | 424 | 356 | 68 | 35 | 4 | 21 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 4 | 86..496 | 411 | 411 | 337 | 74 | 32 | 3 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 5 | 88..560 | 473 | 473 | 396 | 77 | 33 | 5 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128 |
| 6 | 89..510 | 422 | 422 | 341 | 81 | 37 | 4 | 33 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 8 | 97..468 | 372 | 372 | 295 | 77 | 33 | 6 | 25 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 9 | 100..525 | 426 | 426 | 355 | 71 | 33 | 4 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 10 | 102..559 | 458 | 458 | 387 | 71 | 31 | 4 | 29 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 12 | 106..483 | 378 | 378 | 296 | 82 | 39 | 5 | 22 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 13 | 106..529 | 424 | 424 | 346 | 78 | 39 | 4 | 29 | 78896, 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 15 | 108..562 | 455 | 455 | 360 | 95 | 45 | 6 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 116..555 | 440 | 440 | 374 | 66 | 38 | 3 | 18 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 20 | 116..558 | 443 | 443 | 387 | 56 | 24 | 2 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 21 | 117..473 | 357 | 357 | 287 | 70 | 31 | 15 | 13 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 24 | 125..544 | 420 | 420 | 351 | 69 | 32 | 3 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 27 | 137..566 | 430 | 430 | 328 | 102 | 50 | 7 | 31 | 79128, 79134, 79135, 79136, 79139 |
| 28 | 137..571 | 435 | 435 | 344 | 91 | 45 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 30 | 137..489 | 353 | 353 | 274 | 79 | 36 | 4 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 31 | 151..567 | 417 | 417 | 317 | 100 | 49 | 5 | 29 | 79134, 79135, 79136, 79139 |
| 34 | 177..521 | 345 | 345 | 278 | 67 | 30 | 2 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 35 | 177..513 | 337 | 337 | 281 | 56 | 24 | 2 | 30 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 36 | 256..479 | 224 | 224 | 167 | 57 | 24 | 2 | 29 | 78897, 78971, 79037, 79045 |
