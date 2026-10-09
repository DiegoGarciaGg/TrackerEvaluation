# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=038506d1435a
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise1.0_fp0.0_seed2/tracks.csv sha256=0be03ee947a16ede
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise1.0_fp0.0_seed2.csv sha256=038506d1435a9fb1
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise1.0_fp0.0_seed2
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
| observations | none | 4 | 10142 | 6992 | 0.296 | 0.572 | 0.153 | 1.08 | 0.353 | 0.591 | 1.27 | 981 | 2071.0 | 0.367 | 0.450 | 0.310 | 0.689 | 0.999 | 6985 | 3157 | 7 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 6992 | 0.318 | 0.612 | 0.165 | 1.17 | 0.353 | 0.593 | 1.28 | 979 | 2062.0 | 0.369 | 0.452 | 0.311 | 0.689 | 1.000 | 6991 | 3151 | 1 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 6992 | 0.330 | 0.628 | 0.173 | 1.25 | 0.353 | 0.593 | 1.31 | 960 | 2060.0 | 0.371 | 0.455 | 0.313 | 0.689 | 0.999 | 6984 | 3158 | 8 | 0 | 25 | 0 |
| observations | none | 12 | 10142 | 6992 | 0.345 | 0.623 | 0.191 | 1.58 | 0.352 | 0.597 | 1.57 | 893 | 2016.0 | 0.387 | 0.474 | 0.327 | 0.687 | 0.997 | 6972 | 3170 | 20 | 0 | 25 | 0 |
| observations | ignore | 4 | 10142 | 6992 | 0.296 | 0.572 | 0.153 | 1.08 | 0.353 | 0.591 | 1.27 | 981 | 2071.0 | 0.367 | 0.450 | 0.310 | 0.689 | 0.999 | 6985 | 3157 | 7 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 6992 | 0.318 | 0.612 | 0.165 | 1.17 | 0.353 | 0.593 | 1.28 | 979 | 2062.0 | 0.369 | 0.452 | 0.311 | 0.689 | 1.000 | 6991 | 3151 | 1 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 6992 | 0.330 | 0.628 | 0.173 | 1.25 | 0.353 | 0.593 | 1.31 | 960 | 2060.0 | 0.371 | 0.455 | 0.313 | 0.689 | 0.999 | 6984 | 3158 | 8 | 0 | 25 | 0 |
| observations | ignore | 12 | 10142 | 6992 | 0.345 | 0.623 | 0.191 | 1.58 | 0.352 | 0.597 | 1.57 | 893 | 2016.0 | 0.387 | 0.474 | 0.327 | 0.687 | 0.997 | 6972 | 3170 | 20 | 0 | 25 | 0 |
| updates | none | 4 | 10142 | 9859 | 0.286 | 0.516 | 0.159 | 1.26 | 0.321 | 0.376 | 1.34 | 1044 | 1952.0 | 0.343 | 0.348 | 0.338 | 0.726 | 0.747 | 7360 | 2782 | 2499 | 1 | 24 | 0 |
| updates | none | 6 | 10142 | 9859 | 0.335 | 0.602 | 0.186 | 1.59 | 0.367 | 0.495 | 1.64 | 1044 | 1530.0 | 0.379 | 0.384 | 0.374 | 0.785 | 0.808 | 7963 | 2179 | 1896 | 8 | 17 | 0 |
| updates | none | 8 | 10142 | 9859 | 0.365 | 0.649 | 0.205 | 1.84 | 0.405 | 0.612 | 2.03 | 997 | 1139.0 | 0.411 | 0.417 | 0.405 | 0.841 | 0.865 | 8530 | 1612 | 1329 | 20 | 5 | 0 |
| updates | none | 12 | 10142 | 9859 | 0.402 | 0.680 | 0.237 | 2.41 | 0.433 | 0.683 | 2.59 | 896 | 874.0 | 0.447 | 0.454 | 0.441 | 0.872 | 0.897 | 8841 | 1301 | 1018 | 24 | 1 | 0 |
| updates | ignore | 4 | 10142 | 9859 | 0.286 | 0.516 | 0.159 | 1.26 | 0.321 | 0.376 | 1.34 | 1044 | 1952.0 | 0.343 | 0.348 | 0.338 | 0.726 | 0.747 | 7360 | 2782 | 2499 | 1 | 24 | 0 |
| updates | ignore | 6 | 10142 | 9859 | 0.335 | 0.602 | 0.186 | 1.59 | 0.367 | 0.495 | 1.64 | 1044 | 1530.0 | 0.379 | 0.384 | 0.374 | 0.785 | 0.808 | 7963 | 2179 | 1896 | 8 | 17 | 0 |
| updates | ignore | 8 | 10142 | 9859 | 0.365 | 0.649 | 0.205 | 1.84 | 0.405 | 0.612 | 2.03 | 997 | 1139.0 | 0.411 | 0.417 | 0.405 | 0.841 | 0.865 | 8530 | 1612 | 1329 | 20 | 5 | 0 |
| updates | ignore | 12 | 10142 | 9859 | 0.402 | 0.680 | 0.237 | 2.41 | 0.433 | 0.683 | 2.59 | 896 | 874.0 | 0.447 | 0.454 | 0.441 | 0.872 | 0.897 | 8841 | 1301 | 1018 | 24 | 1 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 6984; unmatched reference entries: 3158; unmatched candidate entries: 8
- identity switches: 960; fragmentation (coverage interruptions): 2113; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 10 -> 3 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 7 -> 11 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 79037: 3 -> 9 at (2118, 3034.5), 3 frames after previous cover
- f93: ref 79045: 9 -> 11 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 7 -> 8 at (2071, 3031), 4 frames after previous cover
- f94: ref 78971: 11 -> 7 at (2090.5, 3032.5), 2 frames after previous cover
- f95: ref 78969: 8 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 10 -> 12 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 7 -> 8 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 10 -> 12 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 3 -> 9 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 12 -> 3 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 9 -> 11 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 10 -> 12 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 11 -> 3 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 12 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 3 -> 9 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 8 -> 7 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 10 -> 12 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 10 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 14 -> 10 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 9 -> 16 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 6 frames after previous cover
- f106: ref 79105: 14 -> 10 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 78897: 16 -> 11 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 9 -> 16 at (2055.5, 3031), 4 frames after previous cover
- f109: ref 78971: 7 -> 18 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 12 -> 9 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 11 -> 3 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 18 -> 7 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 3 -> 18 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 9 -> 11 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 12 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 12 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 10 -> 20 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 14 -> 10 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 14 -> 19 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 3 -> 16 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 7 -> 18 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 18 -> 3 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 16 -> 9 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 14 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 16 -> 3 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 16 -> 11 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 3 -> 18 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 9 -> 16 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 11 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 9 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 19 -> 10 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 10 -> 14 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 9 -> 16 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 20 -> 9 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 20 -> 12 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 14 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 10 -> 14 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 19 -> 10 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 11 -> 21 at (2012.5, 3030), 1 frames after previous cover
- ... 900 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 688 | 202 | 1 (688) |
| 78896 | 350 (76..429) | 223 | 75 | 18 (145), 8 (78) |
| 78969 | 352 (80..434) | 235 | 79 | 7 (166), 8 (28), 18 (24), 23 (14), 3 (3) |
| 78971 | 352 (84..439) | 244 | 71 | 8 (138), 7 (47), 23 (41), 39 (12), 18 (5), 11 (1) |
| 79045 | 355 (84..443) | 230 | 75 | 23 (72), 7 (39), 18 (35), 3 (27), 8 (23), 29 (14), 39 (13), 11 (5), 9 (2) |
| 79037 | 355 (86..445) | 248 | 75 | 23 (79), 29 (48), 3 (26), 18 (24), 22 (23), 7 (19), 8 (12), 11 (11), 9 (5), 16 (1) |
| 78897 | 345 (89..450) | 254 | 64 | 29 (80), 3 (63), 28 (52), 23 (22), 22 (17), 21 (7), 16 (4), 9 (3), 18 (3), 11 (2), 10 (1) |
| 78899 | 365 (91..455) | 241 | 82 | 28 (70), 16 (36), 29 (35), 23 (32), 21 (19), 3 (18), 22 (10), 14 (10), 11 (5), 9 (3), 10 (2), 12 (1) |
| 79097 | 366 (94..461) | 256 | 82 | 3 (81), 28 (72), 16 (50), 21 (13), 22 (11), 14 (10), 11 (7), 9 (4), 12 (3), 29 (3), 10 (2) |
| 79098 | 360 (97..467) | 253 | 76 | 16 (57), 22 (50), 29 (50), 11 (43), 28 (18), 14 (10), 3 (9), 19 (7), 10 (3), 12 (3), 9 (3) |
| 79102 | 371 (98..477) | 251 | 80 | 11 (91), 16 (58), 14 (24), 22 (15), 19 (13), 21 (11), 29 (9), 9 (7), 3 (7), 12 (6), 28 (6), 10 (3), +1 more |
| 79103 | 380 (99..481) | 259 | 82 | 11 (97), 3 (40), 22 (32), 19 (23), 14 (22), 16 (14), 28 (11), 9 (9), 12 (4), 10 (3), 21 (3), 29 (1) |
| 79105 | 379 (101..484) | 266 | 76 | 14 (76), 11 (32), 21 (31), 22 (28), 9 (24), 16 (20), 19 (16), 28 (15), 3 (15), 10 (3), 20 (3), 12 (3) |
| 79108 | 385 (104..492) | 288 | 71 | 22 (83), 14 (48), 9 (42), 19 (32), 21 (30), 16 (27), 11 (8), 12 (7), 20 (5), 10 (2), 28 (2), 3 (2) |
| 79110 | 388 (106..497) | 267 | 82 | 9 (101), 14 (43), 12 (39), 19 (26), 21 (24), 22 (18), 10 (8), 16 (4), 11 (4) |
| 79111 | 386 (109..500) | 258 | 83 | 12 (97), 19 (69), 14 (32), 10 (14), 9 (13), 27 (12), 25 (11), 21 (5), 20 (3), 16 (1), 22 (1) |
| 79115 | 421 (111..531) | 293 | 85 | 12 (126), 25 (44), 27 (39), 9 (26), 10 (19), 16 (16), 14 (10), 19 (5), 20 (5), 21 (2), 22 (1) |
| 79116 | 411 (114..530) | 286 | 84 | 27 (112), 25 (44), 12 (33), 21 (24), 9 (19), 19 (15), 10 (15), 20 (13), 16 (4), 38 (4), 14 (3) |
| 79122 | 404 (118..532) | 278 | 85 | 10 (113), 20 (44), 9 (38), 27 (28), 25 (15), 21 (15), 12 (10), 19 (9), 14 (5), 31 (1) |
| 79132 | 391 (120..515) | 264 | 77 | 38 (77), 10 (43), 21 (36), 19 (22), 20 (20), 31 (20), 12 (14), 9 (11), 14 (9), 27 (8), 25 (3), 26 (1) |
| 79128 | 402 (124..527) | 257 | 94 | 21 (86), 20 (47), 38 (32), 31 (29), 19 (19), 10 (16), 27 (16), 25 (7), 26 (4), 12 (1) |
| 79134 | 407 (127..533) | 306 | 68 | 20 (173), 19 (40), 27 (36), 25 (19), 21 (12), 31 (11), 10 (8), 26 (7) |
| 79135 | 409 (129..542) | 290 | 85 | 25 (146), 26 (41), 27 (35), 20 (33), 10 (26), 31 (6), 19 (3) |
| 79139 | 406 (132..537) | 280 | 94 | 26 (165), 31 (62), 25 (22), 27 (21), 10 (10) |
| 79136 | 393 (136..538) | 269 | 86 | 31 (146), 26 (83), 10 (40) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 33/385/1002; tracks with internal gaps: 4; total internal gaps: 6; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 688 | 688 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 80..450 | 371 | 291 | 291 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 87..445 | 359 | 271 | 271 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 8 | 89..439 | 351 | 279 | 279 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..496 | 406 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 91..530 | 440 | 331 | 331 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 92..480 | 389 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 96..532 | 437 | 348 | 347 | 1 | 1 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 100..484 | 385 | 302 | 302 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 105..477 | 373 | 292 | 292 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 18 | 109..434 | 326 | 236 | 236 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 19 | 110..500 | 391 | 299 | 299 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 20 | 110..527 | 418 | 350 | 347 | 3 | 1 | 3 | 0 | 79102, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 21 | 115..527 | 413 | 319 | 318 | 1 | 1 | 1 | 0 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 115..492 | 378 | 289 | 289 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 115..455 | 341 | 260 | 260 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 25 | 128..542 | 415 | 314 | 311 | 3 | 3 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 128..537 | 410 | 301 | 301 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 27 | 135..529 | 395 | 307 | 307 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 135..461 | 327 | 246 | 246 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 29 | 140..465 | 326 | 240 | 240 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 31 | 176..537 | 362 | 275 | 275 | 0 | 0 | 0 | 0 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 372..515 | 144 | 113 | 113 | 0 | 0 | 0 | 0 | 79116, 79128, 79132 |
| 39 | 410..442 | 33 | 25 | 25 | 0 | 0 | 0 | 0 | 78971, 79045 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 6984; unmatched reference entries: 3158; unmatched candidate entries: 8
- identity switches: 960; fragmentation (coverage interruptions): 2113; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 10 -> 3 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 7 -> 11 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 79037: 3 -> 9 at (2118, 3034.5), 3 frames after previous cover
- f93: ref 79045: 9 -> 11 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 7 -> 8 at (2071, 3031), 4 frames after previous cover
- f94: ref 78971: 11 -> 7 at (2090.5, 3032.5), 2 frames after previous cover
- f95: ref 78969: 8 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 10 -> 12 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 7 -> 8 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 10 -> 12 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 3 -> 9 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 12 -> 3 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 9 -> 11 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 10 -> 12 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 11 -> 3 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 12 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 3 -> 9 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 8 -> 7 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 10 -> 12 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 10 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 14 -> 10 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 9 -> 16 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 6 frames after previous cover
- f106: ref 79105: 14 -> 10 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 78897: 16 -> 11 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 9 -> 16 at (2055.5, 3031), 4 frames after previous cover
- f109: ref 78971: 7 -> 18 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 12 -> 9 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 11 -> 3 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 18 -> 7 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 3 -> 18 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 9 -> 11 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 12 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 12 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 10 -> 20 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 14 -> 10 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 14 -> 19 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 3 -> 16 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 7 -> 18 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 18 -> 3 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 16 -> 9 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 14 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 16 -> 3 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 16 -> 11 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 3 -> 18 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 9 -> 16 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 11 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 9 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 19 -> 10 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 10 -> 14 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 9 -> 16 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 20 -> 9 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 20 -> 12 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 14 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 10 -> 14 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 19 -> 10 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 11 -> 21 at (2012.5, 3030), 1 frames after previous cover
- ... 900 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 688 | 202 | 1 (688) |
| 78896 | 350 (76..429) | 223 | 75 | 18 (145), 8 (78) |
| 78969 | 352 (80..434) | 235 | 79 | 7 (166), 8 (28), 18 (24), 23 (14), 3 (3) |
| 78971 | 352 (84..439) | 244 | 71 | 8 (138), 7 (47), 23 (41), 39 (12), 18 (5), 11 (1) |
| 79045 | 355 (84..443) | 230 | 75 | 23 (72), 7 (39), 18 (35), 3 (27), 8 (23), 29 (14), 39 (13), 11 (5), 9 (2) |
| 79037 | 355 (86..445) | 248 | 75 | 23 (79), 29 (48), 3 (26), 18 (24), 22 (23), 7 (19), 8 (12), 11 (11), 9 (5), 16 (1) |
| 78897 | 345 (89..450) | 254 | 64 | 29 (80), 3 (63), 28 (52), 23 (22), 22 (17), 21 (7), 16 (4), 9 (3), 18 (3), 11 (2), 10 (1) |
| 78899 | 365 (91..455) | 241 | 82 | 28 (70), 16 (36), 29 (35), 23 (32), 21 (19), 3 (18), 22 (10), 14 (10), 11 (5), 9 (3), 10 (2), 12 (1) |
| 79097 | 366 (94..461) | 256 | 82 | 3 (81), 28 (72), 16 (50), 21 (13), 22 (11), 14 (10), 11 (7), 9 (4), 12 (3), 29 (3), 10 (2) |
| 79098 | 360 (97..467) | 253 | 76 | 16 (57), 22 (50), 29 (50), 11 (43), 28 (18), 14 (10), 3 (9), 19 (7), 10 (3), 12 (3), 9 (3) |
| 79102 | 371 (98..477) | 251 | 80 | 11 (91), 16 (58), 14 (24), 22 (15), 19 (13), 21 (11), 29 (9), 9 (7), 3 (7), 12 (6), 28 (6), 10 (3), +1 more |
| 79103 | 380 (99..481) | 259 | 82 | 11 (97), 3 (40), 22 (32), 19 (23), 14 (22), 16 (14), 28 (11), 9 (9), 12 (4), 10 (3), 21 (3), 29 (1) |
| 79105 | 379 (101..484) | 266 | 76 | 14 (76), 11 (32), 21 (31), 22 (28), 9 (24), 16 (20), 19 (16), 28 (15), 3 (15), 10 (3), 20 (3), 12 (3) |
| 79108 | 385 (104..492) | 288 | 71 | 22 (83), 14 (48), 9 (42), 19 (32), 21 (30), 16 (27), 11 (8), 12 (7), 20 (5), 10 (2), 28 (2), 3 (2) |
| 79110 | 388 (106..497) | 267 | 82 | 9 (101), 14 (43), 12 (39), 19 (26), 21 (24), 22 (18), 10 (8), 16 (4), 11 (4) |
| 79111 | 386 (109..500) | 258 | 83 | 12 (97), 19 (69), 14 (32), 10 (14), 9 (13), 27 (12), 25 (11), 21 (5), 20 (3), 16 (1), 22 (1) |
| 79115 | 421 (111..531) | 293 | 85 | 12 (126), 25 (44), 27 (39), 9 (26), 10 (19), 16 (16), 14 (10), 19 (5), 20 (5), 21 (2), 22 (1) |
| 79116 | 411 (114..530) | 286 | 84 | 27 (112), 25 (44), 12 (33), 21 (24), 9 (19), 19 (15), 10 (15), 20 (13), 16 (4), 38 (4), 14 (3) |
| 79122 | 404 (118..532) | 278 | 85 | 10 (113), 20 (44), 9 (38), 27 (28), 25 (15), 21 (15), 12 (10), 19 (9), 14 (5), 31 (1) |
| 79132 | 391 (120..515) | 264 | 77 | 38 (77), 10 (43), 21 (36), 19 (22), 20 (20), 31 (20), 12 (14), 9 (11), 14 (9), 27 (8), 25 (3), 26 (1) |
| 79128 | 402 (124..527) | 257 | 94 | 21 (86), 20 (47), 38 (32), 31 (29), 19 (19), 10 (16), 27 (16), 25 (7), 26 (4), 12 (1) |
| 79134 | 407 (127..533) | 306 | 68 | 20 (173), 19 (40), 27 (36), 25 (19), 21 (12), 31 (11), 10 (8), 26 (7) |
| 79135 | 409 (129..542) | 290 | 85 | 25 (146), 26 (41), 27 (35), 20 (33), 10 (26), 31 (6), 19 (3) |
| 79139 | 406 (132..537) | 280 | 94 | 26 (165), 31 (62), 25 (22), 27 (21), 10 (10) |
| 79136 | 393 (136..538) | 269 | 86 | 31 (146), 26 (83), 10 (40) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 33/385/1002; tracks with internal gaps: 4; total internal gaps: 6; longest internal gap: 3; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 688 | 688 | 0 | 0 | 0 | 0 | 78911 |
| 3 | 80..450 | 371 | 291 | 291 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 87..445 | 359 | 271 | 271 | 0 | 0 | 0 | 0 | 78969, 78971, 79037, 79045 |
| 8 | 89..439 | 351 | 279 | 279 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..496 | 406 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 91..530 | 440 | 331 | 331 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 92..480 | 389 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 96..532 | 437 | 348 | 347 | 1 | 1 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 100..484 | 385 | 302 | 302 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 105..477 | 373 | 292 | 292 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 18 | 109..434 | 326 | 236 | 236 | 0 | 0 | 0 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 19 | 110..500 | 391 | 299 | 299 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 20 | 110..527 | 418 | 350 | 347 | 3 | 1 | 3 | 0 | 79102, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 21 | 115..527 | 413 | 319 | 318 | 1 | 1 | 1 | 0 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 115..492 | 378 | 289 | 289 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 115..455 | 341 | 260 | 260 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045 |
| 25 | 128..542 | 415 | 314 | 311 | 3 | 3 | 1 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 128..537 | 410 | 301 | 301 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 27 | 135..529 | 395 | 307 | 307 | 0 | 0 | 0 | 0 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 135..461 | 327 | 246 | 246 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 29 | 140..465 | 326 | 240 | 240 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 31 | 176..537 | 362 | 275 | 275 | 0 | 0 | 0 | 0 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 372..515 | 144 | 113 | 113 | 0 | 0 | 0 | 0 | 79116, 79128, 79132 |
| 39 | 410..442 | 33 | 25 | 25 | 0 | 0 | 0 | 0 | 78971, 79045 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8530; unmatched reference entries: 1612; unmatched candidate entries: 1329
- identity switches: 997; fragmentation (coverage interruptions): 1076; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 10 -> 3 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 7 -> 11 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 78971: 11 -> 7 at (2095, 3033.5), 1 frames after previous cover
- f93: ref 79037: 3 -> 9 at (2118, 3034.5), 2 frames after previous cover
- f93: ref 79045: 9 -> 11 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 7 -> 8 at (2071, 3031), 4 frames after previous cover
- f95: ref 78969: 8 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 10 -> 12 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 7 -> 8 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 10 -> 12 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 3 -> 9 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 12 -> 3 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 9 -> 11 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 10 -> 12 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 11 -> 3 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 12 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 3 -> 9 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 8 -> 7 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 10 -> 12 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 10 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 14 -> 10 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 9 -> 16 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 16 -> 11 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 9 -> 16 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79105: 14 -> 10 at (2113.5, 3025), 4 frames after previous cover
- f109: ref 78971: 7 -> 18 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 12 -> 9 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 11 -> 3 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 18 -> 7 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 3 -> 18 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 9 -> 11 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 12 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 12 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 10 -> 20 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 14 -> 10 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 14 -> 19 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 3 -> 16 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 7 -> 18 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 18 -> 3 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 16 -> 9 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 14 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 16 -> 3 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 16 -> 11 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 3 -> 18 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 9 -> 16 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 11 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 9 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 19 -> 10 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 10 -> 14 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 9 -> 16 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 20 -> 9 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 20 -> 12 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 14 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 10 -> 14 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 19 -> 10 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 11 -> 21 at (2012.5, 3030), 1 frames after previous cover
- ... 937 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 945 | 40 | 1 (945) |
| 78896 | 350 (76..429) | 275 | 36 | 18 (182), 8 (93) |
| 78969 | 352 (80..434) | 285 | 44 | 7 (203), 8 (31), 18 (30), 23 (17), 3 (4) |
| 78971 | 352 (84..439) | 284 | 39 | 8 (162), 7 (51), 23 (48), 39 (16), 18 (6), 11 (1) |
| 79045 | 355 (84..443) | 281 | 45 | 23 (91), 7 (44), 18 (42), 3 (34), 8 (28), 29 (19), 39 (16), 11 (5), 9 (2) |
| 79037 | 355 (86..445) | 298 | 40 | 23 (98), 29 (58), 3 (31), 18 (29), 22 (27), 7 (26), 8 (12), 11 (11), 9 (5), 16 (1) |
| 78897 | 345 (89..450) | 292 | 39 | 29 (85), 3 (69), 28 (64), 23 (25), 22 (24), 21 (8), 9 (4), 16 (4), 18 (3), 39 (3), 11 (2), 10 (1) |
| 78899 | 365 (91..455) | 294 | 48 | 28 (87), 16 (47), 29 (44), 23 (40), 3 (21), 21 (21), 22 (11), 14 (11), 11 (5), 9 (4), 10 (2), 12 (1) |
| 79097 | 366 (94..461) | 308 | 43 | 3 (97), 28 (89), 16 (61), 21 (14), 22 (13), 14 (12), 11 (8), 9 (4), 10 (3), 12 (3), 29 (3), 23 (1) |
| 79098 | 360 (97..467) | 295 | 46 | 16 (65), 22 (63), 29 (62), 11 (46), 28 (21), 14 (11), 3 (10), 19 (8), 10 (3), 12 (3), 9 (3) |
| 79102 | 371 (98..477) | 293 | 52 | 11 (107), 16 (71), 14 (31), 22 (18), 19 (14), 21 (12), 29 (10), 12 (7), 9 (7), 3 (7), 28 (5), 10 (3), +1 more |
| 79103 | 380 (99..481) | 321 | 39 | 11 (124), 3 (51), 22 (38), 14 (27), 19 (26), 16 (16), 9 (13), 28 (12), 10 (5), 12 (4), 21 (3), 29 (2) |
| 79105 | 379 (101..484) | 321 | 38 | 14 (101), 21 (37), 11 (35), 9 (33), 22 (30), 19 (22), 16 (21), 28 (16), 3 (16), 12 (5), 20 (3), 10 (2) |
| 79108 | 385 (104..492) | 332 | 39 | 22 (99), 14 (53), 9 (49), 21 (36), 19 (34), 16 (31), 11 (9), 12 (8), 20 (6), 3 (3), 10 (2), 28 (2) |
| 79110 | 388 (106..497) | 316 | 52 | 9 (132), 14 (49), 12 (41), 19 (27), 21 (25), 22 (23), 10 (8), 16 (6), 11 (5) |
| 79111 | 386 (109..500) | 309 | 56 | 12 (110), 19 (95), 14 (35), 9 (18), 10 (16), 25 (14), 27 (12), 21 (5), 20 (3), 22 (1) |
| 79115 | 421 (111..531) | 354 | 49 | 12 (165), 25 (45), 27 (45), 9 (28), 10 (22), 14 (17), 16 (16), 20 (8), 19 (5), 21 (2), 22 (1) |
| 79116 | 411 (114..530) | 342 | 44 | 27 (145), 25 (58), 12 (37), 21 (26), 9 (25), 19 (18), 10 (16), 20 (8), 16 (4), 38 (3), 14 (2) |
| 79122 | 404 (118..532) | 334 | 50 | 10 (152), 20 (47), 9 (42), 27 (30), 25 (20), 21 (17), 12 (10), 19 (9), 14 (6), 31 (1) |
| 79132 | 391 (120..515) | 309 | 50 | 38 (91), 21 (50), 10 (48), 19 (24), 20 (23), 31 (21), 12 (15), 9 (14), 14 (9), 27 (9), 25 (4), 26 (1) |
| 79128 | 402 (124..527) | 318 | 53 | 21 (110), 20 (51), 38 (44), 31 (36), 19 (25), 10 (22), 27 (16), 25 (7), 26 (5), 12 (2) |
| 79134 | 407 (127..533) | 359 | 33 | 20 (210), 19 (45), 27 (40), 25 (22), 21 (17), 10 (9), 26 (7), 31 (7), 38 (2) |
| 79135 | 409 (129..542) | 359 | 34 | 25 (189), 26 (45), 27 (42), 20 (38), 10 (34), 31 (6), 19 (5) |
| 79139 | 406 (132..537) | 359 | 36 | 26 (247), 31 (40), 27 (31), 25 (28), 10 (13) |
| 79136 | 393 (136..538) | 347 | 31 | 31 (228), 26 (66), 10 (53) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 62/414/1002; tracks with internal gaps: 24; total internal gaps: 500; longest internal gap: 16; tracks ending in coasting: 23 (trailing rows total 633)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 1002 | 945 | 57 | 40 | 5 | 0 | 78911 |
| 3 | 80..479 | 400 | 400 | 343 | 57 | 17 | 4 | 34 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 87..474 | 388 | 388 | 324 | 64 | 24 | 5 | 29 | 78969, 78971, 79037, 79045 |
| 8 | 89..468 | 380 | 380 | 326 | 54 | 18 | 3 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..525 | 435 | 435 | 383 | 52 | 20 | 2 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 91..559 | 469 | 469 | 414 | 55 | 21 | 4 | 27 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 92..509 | 418 | 418 | 358 | 60 | 24 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 96..561 | 466 | 466 | 411 | 55 | 22 | 2 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 100..513 | 414 | 414 | 364 | 50 | 15 | 4 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 105..506 | 402 | 402 | 343 | 59 | 19 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116 |
| 18 | 109..463 | 355 | 355 | 292 | 63 | 23 | 4 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 19 | 110..529 | 420 | 420 | 357 | 63 | 22 | 5 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 20 | 110..556 | 447 | 447 | 398 | 49 | 16 | 3 | 28 | 79102, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 21 | 115..556 | 442 | 442 | 383 | 59 | 23 | 3 | 29 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 115..521 | 407 | 407 | 348 | 59 | 25 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 115..484 | 370 | 370 | 320 | 50 | 17 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 25 | 128..571 | 444 | 444 | 387 | 57 | 22 | 3 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 128..566 | 439 | 439 | 371 | 68 | 30 | 3 | 29 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 27 | 135..558 | 424 | 424 | 370 | 54 | 22 | 4 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 135..490 | 356 | 356 | 296 | 60 | 26 | 5 | 23 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 29 | 140..494 | 355 | 355 | 283 | 72 | 29 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 31 | 176..566 | 391 | 391 | 339 | 52 | 15 | 3 | 28 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 372..544 | 173 | 173 | 140 | 33 | 7 | 16 | 11 | 79116, 79128, 79132, 79134 |
| 39 | 410..471 | 62 | 62 | 35 | 27 | 3 | 4 | 21 | 78897, 78971, 79045 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8530; unmatched reference entries: 1612; unmatched candidate entries: 1329
- identity switches: 997; fragmentation (coverage interruptions): 1076; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 78969: 3 -> 7 at (2108, 3033.5), 5 frames after previous cover
- f91: ref 79045: 3 -> 9 at (2116.5, 3034), 4 frames after previous cover
- f92: ref 78897: 10 -> 3 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78971: 7 -> 11 at (2101.5, 3036), 5 frames after previous cover
- f93: ref 78971: 11 -> 7 at (2095, 3033.5), 1 frames after previous cover
- f93: ref 79037: 3 -> 9 at (2118, 3034.5), 2 frames after previous cover
- f93: ref 79045: 9 -> 11 at (2106.5, 3031.5), 1 frames after previous cover
- f94: ref 78969: 7 -> 8 at (2071, 3031), 4 frames after previous cover
- f95: ref 78969: 8 -> 7 at (2065.5, 3033), 1 frames after previous cover
- f96: ref 78899: 10 -> 12 at (2128, 3029), 3 frames after previous cover
- f97: ref 78969: 7 -> 8 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79097: 10 -> 12 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 3 -> 9 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 12 -> 3 at (2116.5, 3029), 2 frames after previous cover
- f98: ref 79037: 9 -> 11 at (2087, 3034), 1 frames after previous cover
- f99: ref 79098: 10 -> 12 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 11 -> 3 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79098: 12 -> 10 at (2130, 3027), 1 frames after previous cover
- f101: ref 78899: 3 -> 9 at (2098.5, 3030.5), 2 frames after previous cover
- f101: ref 78969: 8 -> 7 at (2028, 3033.5), 1 frames after previous cover
- f101: ref 79098: 10 -> 12 at (2124, 3028), 1 frames after previous cover
- f103: ref 79102: 10 -> 12 at (2124.5, 3027.5), 1 frames after previous cover
- f103: ref 79103: 14 -> 10 at (2133.5, 3022.5), 1 frames after previous cover
- f105: ref 78897: 9 -> 16 at (2058, 3033), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 6 frames after previous cover
- f108: ref 78897: 16 -> 11 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 78899: 9 -> 16 at (2055.5, 3031), 3 frames after previous cover
- f108: ref 79105: 14 -> 10 at (2113.5, 3025), 4 frames after previous cover
- f109: ref 78971: 7 -> 18 at (1996.5, 3034.5), 9 frames after previous cover
- f109: ref 79098: 12 -> 9 at (2077.5, 3029.5), 7 frames after previous cover
- f110: ref 78897: 11 -> 3 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78971: 18 -> 7 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79045: 3 -> 18 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79097: 9 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79098: 9 -> 11 at (2072.5, 3029.5), 1 frames after previous cover
- f110: ref 79102: 12 -> 9 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 12 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79105: 10 -> 20 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 14 -> 10 at (2118, 3025), 3 frames after previous cover
- f110: ref 79110: 14 -> 19 at (2134, 3026), 2 frames after previous cover
- f111: ref 78897: 3 -> 16 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78971: 7 -> 18 at (1984, 3033.5), 1 frames after previous cover
- f111: ref 79045: 18 -> 3 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 16 -> 9 at (2052, 3030), 1 frames after previous cover
- f111: ref 79111: 14 -> 19 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 16 -> 3 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 16 -> 11 at (2032, 3032), 3 frames after previous cover
- f112: ref 79045: 3 -> 18 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 9 -> 16 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 11 -> 9 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 9 -> 20 at (2072.5, 3029.5), 2 frames after previous cover
- f112: ref 79110: 19 -> 10 at (2124.5, 3027.5), 2 frames after previous cover
- f113: ref 79108: 10 -> 14 at (2101.5, 3026), 2 frames after previous cover
- f114: ref 79098: 9 -> 16 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 20 -> 9 at (2061.5, 3029), 2 frames after previous cover
- f114: ref 79105: 20 -> 12 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 14 -> 20 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 10 -> 14 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 19 -> 10 at (2126, 3027), 1 frames after previous cover
- f115: ref 78899: 11 -> 21 at (2012.5, 3030), 1 frames after previous cover
- ... 937 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 945 | 40 | 1 (945) |
| 78896 | 350 (76..429) | 275 | 36 | 18 (182), 8 (93) |
| 78969 | 352 (80..434) | 285 | 44 | 7 (203), 8 (31), 18 (30), 23 (17), 3 (4) |
| 78971 | 352 (84..439) | 284 | 39 | 8 (162), 7 (51), 23 (48), 39 (16), 18 (6), 11 (1) |
| 79045 | 355 (84..443) | 281 | 45 | 23 (91), 7 (44), 18 (42), 3 (34), 8 (28), 29 (19), 39 (16), 11 (5), 9 (2) |
| 79037 | 355 (86..445) | 298 | 40 | 23 (98), 29 (58), 3 (31), 18 (29), 22 (27), 7 (26), 8 (12), 11 (11), 9 (5), 16 (1) |
| 78897 | 345 (89..450) | 292 | 39 | 29 (85), 3 (69), 28 (64), 23 (25), 22 (24), 21 (8), 9 (4), 16 (4), 18 (3), 39 (3), 11 (2), 10 (1) |
| 78899 | 365 (91..455) | 294 | 48 | 28 (87), 16 (47), 29 (44), 23 (40), 3 (21), 21 (21), 22 (11), 14 (11), 11 (5), 9 (4), 10 (2), 12 (1) |
| 79097 | 366 (94..461) | 308 | 43 | 3 (97), 28 (89), 16 (61), 21 (14), 22 (13), 14 (12), 11 (8), 9 (4), 10 (3), 12 (3), 29 (3), 23 (1) |
| 79098 | 360 (97..467) | 295 | 46 | 16 (65), 22 (63), 29 (62), 11 (46), 28 (21), 14 (11), 3 (10), 19 (8), 10 (3), 12 (3), 9 (3) |
| 79102 | 371 (98..477) | 293 | 52 | 11 (107), 16 (71), 14 (31), 22 (18), 19 (14), 21 (12), 29 (10), 12 (7), 9 (7), 3 (7), 28 (5), 10 (3), +1 more |
| 79103 | 380 (99..481) | 321 | 39 | 11 (124), 3 (51), 22 (38), 14 (27), 19 (26), 16 (16), 9 (13), 28 (12), 10 (5), 12 (4), 21 (3), 29 (2) |
| 79105 | 379 (101..484) | 321 | 38 | 14 (101), 21 (37), 11 (35), 9 (33), 22 (30), 19 (22), 16 (21), 28 (16), 3 (16), 12 (5), 20 (3), 10 (2) |
| 79108 | 385 (104..492) | 332 | 39 | 22 (99), 14 (53), 9 (49), 21 (36), 19 (34), 16 (31), 11 (9), 12 (8), 20 (6), 3 (3), 10 (2), 28 (2) |
| 79110 | 388 (106..497) | 316 | 52 | 9 (132), 14 (49), 12 (41), 19 (27), 21 (25), 22 (23), 10 (8), 16 (6), 11 (5) |
| 79111 | 386 (109..500) | 309 | 56 | 12 (110), 19 (95), 14 (35), 9 (18), 10 (16), 25 (14), 27 (12), 21 (5), 20 (3), 22 (1) |
| 79115 | 421 (111..531) | 354 | 49 | 12 (165), 25 (45), 27 (45), 9 (28), 10 (22), 14 (17), 16 (16), 20 (8), 19 (5), 21 (2), 22 (1) |
| 79116 | 411 (114..530) | 342 | 44 | 27 (145), 25 (58), 12 (37), 21 (26), 9 (25), 19 (18), 10 (16), 20 (8), 16 (4), 38 (3), 14 (2) |
| 79122 | 404 (118..532) | 334 | 50 | 10 (152), 20 (47), 9 (42), 27 (30), 25 (20), 21 (17), 12 (10), 19 (9), 14 (6), 31 (1) |
| 79132 | 391 (120..515) | 309 | 50 | 38 (91), 21 (50), 10 (48), 19 (24), 20 (23), 31 (21), 12 (15), 9 (14), 14 (9), 27 (9), 25 (4), 26 (1) |
| 79128 | 402 (124..527) | 318 | 53 | 21 (110), 20 (51), 38 (44), 31 (36), 19 (25), 10 (22), 27 (16), 25 (7), 26 (5), 12 (2) |
| 79134 | 407 (127..533) | 359 | 33 | 20 (210), 19 (45), 27 (40), 25 (22), 21 (17), 10 (9), 26 (7), 31 (7), 38 (2) |
| 79135 | 409 (129..542) | 359 | 34 | 25 (189), 26 (45), 27 (42), 20 (38), 10 (34), 31 (6), 19 (5) |
| 79139 | 406 (132..537) | 359 | 36 | 26 (247), 31 (40), 27 (31), 25 (28), 10 (13) |
| 79136 | 393 (136..538) | 347 | 31 | 31 (228), 26 (66), 10 (53) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 62/414/1002; tracks with internal gaps: 24; total internal gaps: 500; longest internal gap: 16; tracks ending in coasting: 23 (trailing rows total 633)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7..1008 | 1002 | 1002 | 945 | 57 | 40 | 5 | 0 | 78911 |
| 3 | 80..479 | 400 | 400 | 343 | 57 | 17 | 4 | 34 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 7 | 87..474 | 388 | 388 | 324 | 64 | 24 | 5 | 29 | 78969, 78971, 79037, 79045 |
| 8 | 89..468 | 380 | 380 | 326 | 54 | 18 | 3 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 9 | 91..525 | 435 | 435 | 383 | 52 | 20 | 2 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 10 | 91..559 | 469 | 469 | 414 | 55 | 21 | 4 | 27 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 92..509 | 418 | 418 | 358 | 60 | 24 | 3 | 28 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 12 | 96..561 | 466 | 466 | 411 | 55 | 22 | 2 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 14 | 100..513 | 414 | 414 | 364 | 50 | 15 | 4 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 16 | 105..506 | 402 | 402 | 343 | 59 | 19 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79115, 79116 |
| 18 | 109..463 | 355 | 355 | 292 | 63 | 23 | 4 | 29 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 19 | 110..529 | 420 | 420 | 357 | 63 | 22 | 5 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 20 | 110..556 | 447 | 447 | 398 | 49 | 16 | 3 | 28 | 79102, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 21 | 115..556 | 442 | 442 | 383 | 59 | 23 | 3 | 29 | 78897, 78899, 79097, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 22 | 115..521 | 407 | 407 | 348 | 59 | 25 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 23 | 115..484 | 370 | 370 | 320 | 50 | 17 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 25 | 128..571 | 444 | 444 | 387 | 57 | 22 | 3 | 29 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 26 | 128..566 | 439 | 439 | 371 | 68 | 30 | 3 | 29 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 27 | 135..558 | 424 | 424 | 370 | 54 | 22 | 4 | 28 | 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 135..490 | 356 | 356 | 296 | 60 | 26 | 5 | 23 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 29 | 140..494 | 355 | 355 | 283 | 72 | 29 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 31 | 176..566 | 391 | 391 | 339 | 52 | 15 | 3 | 28 | 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 38 | 372..544 | 173 | 173 | 140 | 33 | 7 | 16 | 11 | 79116, 79128, 79132, 79134 |
| 39 | 410..471 | 62 | 62 | 35 | 27 | 3 | 4 | 21 | 78897, 78971, 79045 |
