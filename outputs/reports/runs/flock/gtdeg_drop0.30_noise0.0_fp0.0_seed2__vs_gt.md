# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=f39a2576d134
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise0.0_fp0.0_seed2/tracks.csv sha256=bdbe68c827319cd7
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise0.0_fp0.0_seed2.csv sha256=f39a2576d1348c66
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise0.0_fp0.0_seed2
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
| observations | none | 4 | 10142 | 6978 | 0.345 | 0.686 | 0.174 | 0.01 | 0.346 | 0.596 | 0.01 | 933 | 2011.0 | 0.348 | 0.427 | 0.294 | 0.688 | 1.000 | 6978 | 3164 | 0 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 6978 | 0.346 | 0.684 | 0.175 | 0.02 | 0.346 | 0.596 | 0.01 | 933 | 2011.0 | 0.349 | 0.428 | 0.295 | 0.688 | 1.000 | 6978 | 3164 | 0 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 6978 | 0.346 | 0.679 | 0.176 | 0.05 | 0.345 | 0.596 | 0.04 | 932 | 2010.0 | 0.350 | 0.429 | 0.295 | 0.688 | 1.000 | 6978 | 3164 | 0 | 0 | 25 | 0 |
| observations | none | 12 | 10142 | 6978 | 0.346 | 0.659 | 0.182 | 0.25 | 0.344 | 0.600 | 0.31 | 882 | 1967.0 | 0.363 | 0.445 | 0.306 | 0.688 | 0.999 | 6974 | 3168 | 4 | 0 | 25 | 0 |
| observations | ignore | 4 | 10142 | 6978 | 0.345 | 0.686 | 0.174 | 0.01 | 0.346 | 0.596 | 0.01 | 933 | 2011.0 | 0.348 | 0.427 | 0.294 | 0.688 | 1.000 | 6978 | 3164 | 0 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 6978 | 0.346 | 0.684 | 0.175 | 0.02 | 0.346 | 0.596 | 0.01 | 933 | 2011.0 | 0.349 | 0.428 | 0.295 | 0.688 | 1.000 | 6978 | 3164 | 0 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 6978 | 0.346 | 0.679 | 0.176 | 0.05 | 0.345 | 0.596 | 0.04 | 932 | 2010.0 | 0.350 | 0.429 | 0.295 | 0.688 | 1.000 | 6978 | 3164 | 0 | 0 | 25 | 0 |
| observations | ignore | 12 | 10142 | 6978 | 0.346 | 0.659 | 0.182 | 0.25 | 0.344 | 0.600 | 0.31 | 882 | 1967.0 | 0.363 | 0.445 | 0.306 | 0.688 | 0.999 | 6974 | 3168 | 4 | 0 | 25 | 0 |
| updates | none | 4 | 10142 | 9888 | 0.322 | 0.601 | 0.173 | 0.29 | 0.313 | 0.370 | 0.13 | 985 | 1917.0 | 0.321 | 0.325 | 0.317 | 0.721 | 0.739 | 7311 | 2831 | 2577 | 2 | 23 | 0 |
| updates | none | 6 | 10142 | 9888 | 0.353 | 0.655 | 0.191 | 0.59 | 0.355 | 0.494 | 0.55 | 1008 | 1478.0 | 0.356 | 0.360 | 0.351 | 0.784 | 0.805 | 7955 | 2187 | 1933 | 5 | 20 | 0 |
| updates | none | 8 | 10142 | 9888 | 0.374 | 0.687 | 0.203 | 0.85 | 0.399 | 0.624 | 1.06 | 964 | 1066.0 | 0.387 | 0.392 | 0.382 | 0.847 | 0.869 | 8588 | 1554 | 1300 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 9888 | 0.398 | 0.713 | 0.222 | 1.33 | 0.420 | 0.679 | 1.61 | 898 | 859.0 | 0.417 | 0.422 | 0.412 | 0.871 | 0.894 | 8837 | 1305 | 1051 | 24 | 1 | 0 |
| updates | ignore | 4 | 10142 | 9888 | 0.322 | 0.601 | 0.173 | 0.29 | 0.313 | 0.370 | 0.13 | 985 | 1917.0 | 0.321 | 0.325 | 0.317 | 0.721 | 0.739 | 7311 | 2831 | 2577 | 2 | 23 | 0 |
| updates | ignore | 6 | 10142 | 9888 | 0.353 | 0.655 | 0.191 | 0.59 | 0.355 | 0.494 | 0.55 | 1008 | 1478.0 | 0.356 | 0.360 | 0.351 | 0.784 | 0.805 | 7955 | 2187 | 1933 | 5 | 20 | 0 |
| updates | ignore | 8 | 10142 | 9888 | 0.374 | 0.687 | 0.203 | 0.85 | 0.399 | 0.624 | 1.06 | 964 | 1066.0 | 0.387 | 0.392 | 0.382 | 0.847 | 0.869 | 8588 | 1554 | 1300 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 9888 | 0.398 | 0.713 | 0.222 | 1.33 | 0.420 | 0.679 | 1.61 | 898 | 859.0 | 0.417 | 0.422 | 0.412 | 0.871 | 0.894 | 8837 | 1305 | 1051 | 24 | 1 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 6978; unmatched reference entries: 3164; unmatched candidate entries: 0
- identity switches: 932; fragmentation (coverage interruptions): 2057; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 7 -> 10 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 79045: 10 -> 12 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78897: 7 -> 10 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 7 -> 11 at (2095, 3033.5), 6 frames after previous cover
- f95: ref 78897: 10 -> 7 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 10 -> 12 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 7 -> 11 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 11 -> 8 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 8 -> 11 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 12 -> 11 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 10 -> 12 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 11 -> 15 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 11 -> 7 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 10 -> 12 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 7 -> 11 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 10 -> 12 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 78899: 12 -> 7 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 11 -> 15 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 12 -> 19 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 12 -> 19 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 15 -> 22 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 10 -> 12 at (2116.5, 3023), 5 frames after previous cover
- f106: ref 79105: 10 -> 21 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 11 -> 26 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 19 -> 27 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 12 -> 24 at (2096.5, 3027.5), 4 frames after previous cover
- f108: ref 79110: 10 -> 25 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 19 -> 27 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79103: 12 -> 19 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79108: 10 -> 21 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 7 -> 19 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 19 -> 24 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 21 -> 12 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 25 -> 21 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 10 -> 25 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 27 -> 24 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 24 -> 12 at (2082, 3024), 2 frames after previous cover
- f112: ref 79105: 12 -> 21 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 21 -> 25 at (2109, 3027), 3 frames after previous cover
- f113: ref 79108: 25 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 21 -> 25 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 24 -> 19 at (2034.5, 3030), 2 frames after previous cover
- f114: ref 79098: 27 -> 24 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 24 -> 27 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 19 -> 26 at (2012.5, 3030), 3 frames after previous cover
- f115: ref 79045: 26 -> 22 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 12 -> 7 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 21 -> 27 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 25 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 10 -> 12 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78897: 7 -> 26 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 27 -> 19 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 27 -> 7 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 21 -> 27 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 26 -> 24 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 11 -> 26 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 22 -> 11 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 24 -> 19 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 26 -> 11 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 19 -> 24 at (2010.5, 3030), 3 frames after previous cover
- ... 872 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 701 | 208 | 3 (701) |
| 78896 | 350 (76..429) | 242 | 63 | 26 (164), 8 (37), 22 (29), 11 (12) |
| 78969 | 352 (80..434) | 236 | 75 | 11 (142), 26 (21), 8 (18), 22 (18), 40 (18), 15 (14), 42 (5) |
| 78971 | 352 (84..439) | 232 | 68 | 22 (93), 40 (81), 26 (24), 11 (17), 15 (6), 31 (4), 7 (3), 42 (3), 35 (1) |
| 79045 | 355 (84..443) | 253 | 62 | 42 (94), 22 (64), 31 (37), 11 (26), 26 (13), 40 (5), 12 (4), 15 (3), 7 (2), 10 (2), 35 (2), 8 (1) |
| 79037 | 355 (86..445) | 241 | 69 | 40 (77), 22 (32), 11 (31), 36 (30), 31 (26), 7 (15), 42 (11), 27 (8), 8 (5), 15 (3), 35 (2), 26 (1) |
| 78897 | 345 (89..450) | 243 | 72 | 31 (80), 42 (45), 15 (26), 7 (25), 27 (16), 11 (13), 22 (9), 40 (8), 8 (7), 36 (6), 26 (5), 10 (2), +1 more |
| 78899 | 365 (91..455) | 238 | 82 | 27 (66), 31 (48), 36 (37), 42 (16), 11 (15), 22 (14), 7 (12), 15 (12), 26 (4), 35 (3), 8 (3), 12 (2), +4 more |
| 79097 | 366 (94..461) | 253 | 75 | 36 (111), 27 (45), 15 (16), 40 (11), 8 (11), 26 (10), 7 (10), 24 (7), 31 (7), 11 (6), 42 (6), 19 (5), +4 more |
| 79098 | 360 (97..467) | 253 | 81 | 8 (58), 27 (37), 7 (32), 31 (29), 36 (27), 24 (18), 42 (12), 19 (10), 35 (8), 28 (7), 40 (5), 15 (4), +4 more |
| 79102 | 371 (98..477) | 246 | 82 | 15 (83), 8 (76), 7 (18), 42 (18), 36 (12), 28 (11), 24 (9), 12 (5), 35 (5), 27 (3), 19 (3), 31 (2), +1 more |
| 79103 | 380 (99..481) | 262 | 76 | 15 (74), 7 (54), 8 (36), 31 (33), 28 (21), 12 (12), 24 (12), 38 (12), 26 (4), 19 (2), 10 (1), 11 (1) |
| 79105 | 379 (101..484) | 252 | 80 | 7 (123), 24 (41), 12 (29), 38 (13), 8 (12), 28 (10), 27 (8), 21 (5), 35 (5), 15 (4), 10 (1), 26 (1) |
| 79108 | 385 (104..492) | 268 | 78 | 24 (84), 28 (65), 27 (37), 12 (37), 7 (12), 36 (6), 15 (6), 8 (6), 35 (5), 21 (3), 10 (2), 25 (1), +4 more |
| 79110 | 388 (106..497) | 259 | 79 | 24 (57), 12 (51), 28 (43), 15 (25), 35 (18), 8 (13), 36 (11), 27 (10), 21 (9), 29 (6), 25 (5), 38 (5), +3 more |
| 79111 | 386 (109..500) | 272 | 77 | 24 (67), 35 (62), 29 (42), 28 (37), 12 (26), 21 (10), 27 (8), 19 (5), 25 (4), 36 (3), 38 (3), 15 (3), +1 more |
| 79115 | 421 (111..531) | 284 | 89 | 28 (75), 44 (67), 19 (39), 35 (39), 21 (18), 12 (15), 27 (7), 24 (6), 36 (5), 38 (4), 29 (4), 10 (3), +2 more |
| 79116 | 411 (114..530) | 310 | 73 | 25 (111), 21 (49), 35 (32), 28 (28), 43 (25), 19 (17), 12 (16), 29 (16), 27 (9), 10 (4), 24 (3) |
| 79122 | 404 (118..532) | 281 | 72 | 29 (77), 21 (41), 44 (30), 19 (26), 43 (25), 12 (20), 38 (18), 25 (15), 35 (14), 27 (8), 10 (6), 36 (1) |
| 79132 | 391 (120..515) | 272 | 77 | 29 (65), 19 (63), 21 (38), 25 (23), 12 (22), 38 (18), 27 (15), 35 (14), 28 (9), 10 (2), 43 (2), 24 (1) |
| 79128 | 402 (124..527) | 277 | 83 | 35 (96), 43 (43), 38 (32), 19 (27), 21 (23), 29 (20), 12 (17), 25 (15), 27 (3), 10 (1) |
| 79134 | 407 (127..533) | 284 | 83 | 21 (113), 38 (55), 19 (46), 29 (45), 25 (8), 43 (8), 10 (5), 12 (4) |
| 79135 | 409 (129..542) | 279 | 86 | 43 (115), 25 (41), 19 (30), 29 (24), 12 (23), 38 (18), 21 (18), 10 (10) |
| 79139 | 406 (132..537) | 276 | 81 | 38 (89), 10 (68), 25 (63), 19 (42), 29 (10), 21 (3), 43 (1) |
| 79136 | 393 (136..538) | 264 | 86 | 10 (207), 38 (31), 25 (26) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 135/381/995; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 14..1008 | 995 | 701 | 701 | 0 | 0 | 0 | 0 | 78911 |
| 7 | 84..484 | 401 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 8 | 87..467 | 381 | 283 | 283 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 89..536 | 448 | 323 | 323 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 89..434 | 346 | 264 | 264 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 12 | 91..495 | 405 | 287 | 287 | 0 | 0 | 0 | 0 | 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 15 | 100..444 | 345 | 279 | 279 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 19 | 103..515 | 413 | 320 | 320 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 21 | 106..533 | 428 | 330 | 330 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 106..443 | 338 | 260 | 260 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 24 | 108..500 | 393 | 307 | 307 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 108..530 | 423 | 313 | 313 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 26 | 108..429 | 322 | 249 | 249 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 27 | 108..455 | 348 | 280 | 280 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 28 | 121..491 | 371 | 306 | 306 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 29 | 126..532 | 407 | 309 | 309 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 126..481 | 356 | 266 | 266 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 35 | 134..527 | 394 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 36 | 136..460 | 325 | 249 | 249 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79122 |
| 38 | 142..538 | 397 | 299 | 299 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 40 | 158..439 | 282 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79108 |
| 42 | 205..477 | 273 | 210 | 210 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 43 | 248..542 | 295 | 220 | 220 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 44 | 397..531 | 135 | 97 | 97 | 0 | 0 | 0 | 0 | 79115, 79122 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 6978; unmatched reference entries: 3164; unmatched candidate entries: 0
- identity switches: 932; fragmentation (coverage interruptions): 2057; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 7 -> 10 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 79045: 10 -> 12 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78897: 7 -> 10 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 7 -> 11 at (2095, 3033.5), 6 frames after previous cover
- f95: ref 78897: 10 -> 7 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 10 -> 12 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 7 -> 11 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 11 -> 8 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 8 -> 11 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 12 -> 11 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 10 -> 12 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 11 -> 15 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 11 -> 7 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 10 -> 12 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 7 -> 11 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 10 -> 12 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 78899: 12 -> 7 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 11 -> 15 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 12 -> 19 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 12 -> 19 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 15 -> 22 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 10 -> 12 at (2116.5, 3023), 5 frames after previous cover
- f106: ref 79105: 10 -> 21 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 11 -> 26 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 19 -> 27 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 12 -> 24 at (2096.5, 3027.5), 4 frames after previous cover
- f108: ref 79110: 10 -> 25 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 19 -> 27 at (2077.5, 3029.5), 3 frames after previous cover
- f109: ref 79103: 12 -> 19 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79108: 10 -> 21 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 7 -> 19 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 19 -> 24 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 21 -> 12 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 25 -> 21 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 10 -> 25 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 27 -> 24 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 24 -> 12 at (2082, 3024), 2 frames after previous cover
- f112: ref 79105: 12 -> 21 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 21 -> 25 at (2109, 3027), 3 frames after previous cover
- f113: ref 79108: 25 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 21 -> 25 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 24 -> 19 at (2034.5, 3030), 2 frames after previous cover
- f114: ref 79098: 27 -> 24 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 24 -> 27 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 19 -> 26 at (2012.5, 3030), 3 frames after previous cover
- f115: ref 79045: 26 -> 22 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 12 -> 7 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 21 -> 27 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 25 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 10 -> 12 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78897: 7 -> 26 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 27 -> 19 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 27 -> 7 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 21 -> 27 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 26 -> 24 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 11 -> 26 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 22 -> 11 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 24 -> 19 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 26 -> 11 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 19 -> 24 at (2010.5, 3030), 3 frames after previous cover
- ... 872 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 701 | 208 | 3 (701) |
| 78896 | 350 (76..429) | 242 | 63 | 26 (164), 8 (37), 22 (29), 11 (12) |
| 78969 | 352 (80..434) | 236 | 75 | 11 (142), 26 (21), 8 (18), 22 (18), 40 (18), 15 (14), 42 (5) |
| 78971 | 352 (84..439) | 232 | 68 | 22 (93), 40 (81), 26 (24), 11 (17), 15 (6), 31 (4), 7 (3), 42 (3), 35 (1) |
| 79045 | 355 (84..443) | 253 | 62 | 42 (94), 22 (64), 31 (37), 11 (26), 26 (13), 40 (5), 12 (4), 15 (3), 7 (2), 10 (2), 35 (2), 8 (1) |
| 79037 | 355 (86..445) | 241 | 69 | 40 (77), 22 (32), 11 (31), 36 (30), 31 (26), 7 (15), 42 (11), 27 (8), 8 (5), 15 (3), 35 (2), 26 (1) |
| 78897 | 345 (89..450) | 243 | 72 | 31 (80), 42 (45), 15 (26), 7 (25), 27 (16), 11 (13), 22 (9), 40 (8), 8 (7), 36 (6), 26 (5), 10 (2), +1 more |
| 78899 | 365 (91..455) | 238 | 82 | 27 (66), 31 (48), 36 (37), 42 (16), 11 (15), 22 (14), 7 (12), 15 (12), 26 (4), 35 (3), 8 (3), 12 (2), +4 more |
| 79097 | 366 (94..461) | 253 | 75 | 36 (111), 27 (45), 15 (16), 40 (11), 8 (11), 26 (10), 7 (10), 24 (7), 31 (7), 11 (6), 42 (6), 19 (5), +4 more |
| 79098 | 360 (97..467) | 253 | 81 | 8 (58), 27 (37), 7 (32), 31 (29), 36 (27), 24 (18), 42 (12), 19 (10), 35 (8), 28 (7), 40 (5), 15 (4), +4 more |
| 79102 | 371 (98..477) | 246 | 82 | 15 (83), 8 (76), 7 (18), 42 (18), 36 (12), 28 (11), 24 (9), 12 (5), 35 (5), 27 (3), 19 (3), 31 (2), +1 more |
| 79103 | 380 (99..481) | 262 | 76 | 15 (74), 7 (54), 8 (36), 31 (33), 28 (21), 12 (12), 24 (12), 38 (12), 26 (4), 19 (2), 10 (1), 11 (1) |
| 79105 | 379 (101..484) | 252 | 80 | 7 (123), 24 (41), 12 (29), 38 (13), 8 (12), 28 (10), 27 (8), 21 (5), 35 (5), 15 (4), 10 (1), 26 (1) |
| 79108 | 385 (104..492) | 268 | 78 | 24 (84), 28 (65), 27 (37), 12 (37), 7 (12), 36 (6), 15 (6), 8 (6), 35 (5), 21 (3), 10 (2), 25 (1), +4 more |
| 79110 | 388 (106..497) | 259 | 79 | 24 (57), 12 (51), 28 (43), 15 (25), 35 (18), 8 (13), 36 (11), 27 (10), 21 (9), 29 (6), 25 (5), 38 (5), +3 more |
| 79111 | 386 (109..500) | 272 | 77 | 24 (67), 35 (62), 29 (42), 28 (37), 12 (26), 21 (10), 27 (8), 19 (5), 25 (4), 36 (3), 38 (3), 15 (3), +1 more |
| 79115 | 421 (111..531) | 284 | 89 | 28 (75), 44 (67), 19 (39), 35 (39), 21 (18), 12 (15), 27 (7), 24 (6), 36 (5), 38 (4), 29 (4), 10 (3), +2 more |
| 79116 | 411 (114..530) | 310 | 73 | 25 (111), 21 (49), 35 (32), 28 (28), 43 (25), 19 (17), 12 (16), 29 (16), 27 (9), 10 (4), 24 (3) |
| 79122 | 404 (118..532) | 281 | 72 | 29 (77), 21 (41), 44 (30), 19 (26), 43 (25), 12 (20), 38 (18), 25 (15), 35 (14), 27 (8), 10 (6), 36 (1) |
| 79132 | 391 (120..515) | 272 | 77 | 29 (65), 19 (63), 21 (38), 25 (23), 12 (22), 38 (18), 27 (15), 35 (14), 28 (9), 10 (2), 43 (2), 24 (1) |
| 79128 | 402 (124..527) | 277 | 83 | 35 (96), 43 (43), 38 (32), 19 (27), 21 (23), 29 (20), 12 (17), 25 (15), 27 (3), 10 (1) |
| 79134 | 407 (127..533) | 284 | 83 | 21 (113), 38 (55), 19 (46), 29 (45), 25 (8), 43 (8), 10 (5), 12 (4) |
| 79135 | 409 (129..542) | 279 | 86 | 43 (115), 25 (41), 19 (30), 29 (24), 12 (23), 38 (18), 21 (18), 10 (10) |
| 79139 | 406 (132..537) | 276 | 81 | 38 (89), 10 (68), 25 (63), 19 (42), 29 (10), 21 (3), 43 (1) |
| 79136 | 393 (136..538) | 264 | 86 | 10 (207), 38 (31), 25 (26) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 135/381/995; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 14..1008 | 995 | 701 | 701 | 0 | 0 | 0 | 0 | 78911 |
| 7 | 84..484 | 401 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 8 | 87..467 | 381 | 283 | 283 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 89..536 | 448 | 323 | 323 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 89..434 | 346 | 264 | 264 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 12 | 91..495 | 405 | 287 | 287 | 0 | 0 | 0 | 0 | 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 15 | 100..444 | 345 | 279 | 279 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 19 | 103..515 | 413 | 320 | 320 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 21 | 106..533 | 428 | 330 | 330 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 22 | 106..443 | 338 | 260 | 260 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 24 | 108..500 | 393 | 307 | 307 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 108..530 | 423 | 313 | 313 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 26 | 108..429 | 322 | 249 | 249 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 27 | 108..455 | 348 | 280 | 280 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 28 | 121..491 | 371 | 306 | 306 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 29 | 126..532 | 407 | 309 | 309 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 126..481 | 356 | 266 | 266 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 35 | 134..527 | 394 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 36 | 136..460 | 325 | 249 | 249 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79122 |
| 38 | 142..538 | 397 | 299 | 299 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 40 | 158..439 | 282 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79108 |
| 42 | 205..477 | 273 | 210 | 210 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102 |
| 43 | 248..542 | 295 | 220 | 220 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 44 | 397..531 | 135 | 97 | 97 | 0 | 0 | 0 | 0 | 79115, 79122 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8588; unmatched reference entries: 1554; unmatched candidate entries: 1300
- identity switches: 964; fragmentation (coverage interruptions): 996; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 7 -> 10 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 78971: 7 -> 8 at (2108.5, 3033.5), 4 frames after previous cover
- f92: ref 79045: 10 -> 12 at (2110.5, 3033.5), 1 frames after previous cover
- f93: ref 78897: 7 -> 10 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 8 -> 11 at (2095, 3033.5), 2 frames after previous cover
- f95: ref 78897: 10 -> 7 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 10 -> 12 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 7 -> 11 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 11 -> 8 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 8 -> 11 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 12 -> 11 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 10 -> 12 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 11 -> 15 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 11 -> 7 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 10 -> 12 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 7 -> 11 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 10 -> 12 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78899: 12 -> 7 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 11 -> 15 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 12 -> 19 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 12 -> 19 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 15 -> 22 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 10 -> 12 at (2116.5, 3023), 4 frames after previous cover
- f106: ref 79105: 10 -> 21 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 11 -> 26 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 19 -> 27 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 12 -> 24 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79110: 10 -> 25 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 19 -> 27 at (2077.5, 3029.5), 2 frames after previous cover
- f109: ref 79108: 10 -> 21 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 7 -> 19 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 12 -> 24 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 21 -> 12 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 79110: 25 -> 21 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 10 -> 25 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 27 -> 24 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 24 -> 12 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 12 -> 21 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 21 -> 25 at (2109, 3027), 2 frames after previous cover
- f113: ref 79108: 25 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 21 -> 25 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 24 -> 19 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 27 -> 24 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 24 -> 27 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 19 -> 26 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 26 -> 22 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 12 -> 7 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 21 -> 27 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 25 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 10 -> 12 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 78897: 7 -> 26 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 27 -> 19 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 27 -> 7 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 21 -> 27 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 26 -> 24 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 11 -> 26 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 22 -> 11 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 24 -> 19 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 26 -> 11 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 19 -> 24 at (2010.5, 3030), 3 frames after previous cover
- ... 904 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 954 | 31 | 3 (954) |
| 78896 | 350 (76..429) | 294 | 29 | 26 (199), 8 (43), 22 (34), 11 (18) |
| 78969 | 352 (80..434) | 294 | 34 | 11 (179), 26 (26), 22 (23), 40 (23), 8 (21), 15 (16), 42 (6) |
| 78971 | 352 (84..439) | 284 | 37 | 22 (115), 40 (99), 26 (28), 11 (22), 15 (7), 31 (4), 42 (4), 7 (3), 8 (1), 35 (1) |
| 79045 | 355 (84..443) | 289 | 40 | 42 (108), 22 (75), 31 (42), 11 (30), 26 (13), 40 (5), 15 (4), 10 (3), 12 (3), 7 (2), 35 (2), 8 (2) |
| 79037 | 355 (86..445) | 288 | 44 | 40 (96), 22 (40), 36 (37), 11 (32), 31 (28), 7 (19), 42 (16), 27 (8), 8 (6), 15 (3), 35 (2), 26 (1) |
| 78897 | 345 (89..450) | 291 | 41 | 31 (103), 42 (53), 15 (32), 7 (28), 27 (19), 11 (14), 8 (10), 40 (8), 22 (8), 36 (8), 26 (5), 10 (2), +1 more |
| 78899 | 365 (91..455) | 294 | 46 | 27 (80), 31 (58), 36 (45), 42 (22), 15 (18), 11 (17), 22 (16), 7 (14), 26 (5), 19 (4), 35 (4), 8 (4), +4 more |
| 79097 | 366 (94..461) | 299 | 42 | 36 (136), 27 (51), 15 (18), 40 (14), 8 (12), 26 (11), 7 (11), 24 (9), 31 (9), 11 (7), 42 (7), 19 (5), +4 more |
| 79098 | 360 (97..467) | 307 | 42 | 8 (71), 27 (45), 7 (43), 31 (42), 36 (32), 24 (18), 42 (13), 19 (11), 35 (10), 28 (7), 40 (5), 15 (4), +4 more |
| 79102 | 371 (98..477) | 299 | 44 | 15 (98), 8 (97), 42 (26), 7 (19), 36 (16), 28 (12), 24 (9), 12 (6), 35 (5), 19 (4), 27 (3), 10 (2), +1 more |
| 79103 | 380 (99..481) | 308 | 47 | 15 (86), 7 (60), 8 (46), 31 (36), 28 (23), 24 (15), 38 (15), 12 (14), 26 (6), 42 (3), 10 (2), 19 (1), +1 more |
| 79105 | 379 (101..484) | 314 | 41 | 7 (155), 24 (50), 12 (39), 38 (16), 8 (16), 28 (11), 27 (9), 35 (6), 21 (5), 15 (5), 10 (1), 26 (1) |
| 79108 | 385 (104..492) | 319 | 45 | 24 (103), 28 (76), 12 (46), 27 (41), 7 (15), 36 (7), 8 (7), 15 (6), 35 (5), 21 (4), 10 (2), 26 (2), +4 more |
| 79110 | 388 (106..497) | 316 | 47 | 12 (71), 24 (70), 28 (53), 15 (30), 35 (20), 36 (13), 8 (13), 27 (11), 21 (9), 29 (8), 38 (7), 25 (5), +3 more |
| 79111 | 386 (109..500) | 331 | 39 | 24 (83), 35 (72), 29 (53), 28 (41), 12 (36), 21 (12), 27 (9), 25 (5), 19 (5), 36 (5), 38 (4), 15 (4), +1 more |
| 79115 | 421 (111..531) | 344 | 44 | 44 (87), 28 (78), 35 (53), 19 (47), 12 (19), 21 (18), 27 (9), 24 (8), 29 (7), 36 (5), 38 (5), 10 (4), +2 more |
| 79116 | 411 (114..530) | 358 | 37 | 25 (142), 21 (52), 28 (41), 35 (26), 43 (26), 12 (19), 29 (19), 19 (18), 27 (10), 10 (4), 24 (1) |
| 79122 | 404 (118..532) | 347 | 38 | 29 (99), 21 (49), 44 (41), 19 (30), 43 (29), 35 (22), 12 (21), 25 (21), 38 (20), 10 (7), 27 (7), 36 (1) |
| 79132 | 391 (120..515) | 325 | 41 | 29 (79), 19 (78), 21 (43), 12 (33), 25 (25), 38 (20), 27 (16), 35 (16), 28 (9), 10 (2), 43 (2), 24 (2) |
| 79128 | 402 (124..527) | 341 | 39 | 35 (123), 43 (56), 38 (39), 19 (32), 21 (27), 29 (21), 12 (20), 25 (19), 27 (3), 10 (1) |
| 79134 | 407 (127..533) | 350 | 38 | 21 (152), 38 (69), 19 (52), 29 (51), 43 (11), 25 (8), 12 (5), 10 (2) |
| 79135 | 409 (129..542) | 347 | 44 | 43 (145), 25 (48), 19 (39), 12 (28), 29 (27), 38 (25), 21 (24), 10 (11) |
| 79139 | 406 (132..537) | 354 | 35 | 38 (153), 25 (82), 19 (56), 10 (50), 29 (11), 43 (2) |
| 79136 | 393 (136..538) | 341 | 31 | 10 (305), 25 (34), 21 (1), 38 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 164/410/995; tracks with internal gaps: 24; total internal gaps: 467; longest internal gap: 7; tracks ending in coasting: 23 (trailing rows total 649)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 14..1008 | 995 | 995 | 954 | 41 | 31 | 3 | 0 | 78911 |
| 7 | 84..513 | 430 | 430 | 372 | 58 | 26 | 5 | 21 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 8 | 87..496 | 410 | 410 | 349 | 61 | 22 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 89..565 | 477 | 477 | 406 | 71 | 26 | 6 | 28 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 89..463 | 375 | 375 | 321 | 54 | 20 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 12 | 91..524 | 434 | 434 | 367 | 67 | 25 | 4 | 27 | 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 15 | 100..473 | 374 | 374 | 331 | 43 | 12 | 3 | 23 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 19 | 103..544 | 442 | 442 | 385 | 57 | 18 | 7 | 29 | 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 21 | 106..562 | 457 | 457 | 396 | 61 | 23 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 22 | 106..472 | 367 | 367 | 312 | 55 | 23 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 24 | 108..529 | 422 | 422 | 370 | 52 | 16 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 108..559 | 452 | 452 | 392 | 60 | 22 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 26 | 108..458 | 351 | 351 | 298 | 53 | 17 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 27 | 108..484 | 377 | 377 | 321 | 56 | 18 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 28 | 121..520 | 400 | 400 | 351 | 49 | 14 | 3 | 30 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 29 | 126..561 | 436 | 436 | 375 | 61 | 21 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 126..510 | 385 | 385 | 324 | 61 | 22 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 35 | 134..556 | 423 | 423 | 372 | 51 | 17 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 36 | 136..489 | 354 | 354 | 305 | 49 | 17 | 2 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79122 |
| 38 | 142..567 | 426 | 426 | 375 | 51 | 17 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 40 | 158..468 | 311 | 311 | 253 | 58 | 22 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79108 |
| 42 | 205..506 | 302 | 302 | 258 | 44 | 16 | 2 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 43 | 248..571 | 324 | 324 | 273 | 51 | 15 | 4 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 44 | 397..560 | 164 | 164 | 128 | 36 | 7 | 1 | 29 | 79115, 79122 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 24; matched pairs: 8588; unmatched reference entries: 1554; unmatched candidate entries: 1300
- identity switches: 964; fragmentation (coverage interruptions): 996; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79045: 7 -> 10 at (2129.5, 3032), 4 frames after previous cover
- f91: ref 78971: 7 -> 8 at (2108.5, 3033.5), 4 frames after previous cover
- f92: ref 79045: 10 -> 12 at (2110.5, 3033.5), 1 frames after previous cover
- f93: ref 78897: 7 -> 10 at (2132, 3032), 1 frames after previous cover
- f93: ref 78971: 8 -> 11 at (2095, 3033.5), 2 frames after previous cover
- f95: ref 78897: 10 -> 7 at (2118.5, 3032), 1 frames after previous cover
- f95: ref 78899: 10 -> 12 at (2134.5, 3029), 3 frames after previous cover
- f95: ref 79037: 7 -> 11 at (2105, 3034.5), 1 frames after previous cover
- f96: ref 78896: 11 -> 8 at (2034.5, 3034), 4 frames after previous cover
- f97: ref 78969: 8 -> 11 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 12 -> 11 at (2075.5, 3033), 4 frames after previous cover
- f98: ref 79097: 10 -> 12 at (2129, 3028), 1 frames after previous cover
- f100: ref 78971: 11 -> 15 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79037: 11 -> 7 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79098: 10 -> 12 at (2130, 3027), 2 frames after previous cover
- f102: ref 79037: 7 -> 11 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79102: 10 -> 12 at (2130.5, 3027), 2 frames after previous cover
- f103: ref 78899: 12 -> 7 at (2086, 3030), 4 frames after previous cover
- f103: ref 78969: 11 -> 15 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 12 -> 19 at (2100, 3028.5), 5 frames after previous cover
- f104: ref 79098: 12 -> 19 at (2107, 3027.5), 1 frames after previous cover
- f106: ref 78971: 15 -> 22 at (2016.5, 3034), 4 frames after previous cover
- f106: ref 79103: 10 -> 12 at (2116.5, 3023), 4 frames after previous cover
- f106: ref 79105: 10 -> 21 at (2125, 3025.5), 3 frames after previous cover
- f108: ref 79045: 11 -> 26 at (2014.5, 3034), 7 frames after previous cover
- f108: ref 79097: 19 -> 27 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 12 -> 24 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79110: 10 -> 25 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79098: 19 -> 27 at (2077.5, 3029.5), 2 frames after previous cover
- f109: ref 79108: 10 -> 21 at (2125, 3025), 4 frames after previous cover
- f110: ref 78899: 7 -> 19 at (2043, 3030.5), 6 frames after previous cover
- f110: ref 79103: 12 -> 24 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 21 -> 12 at (2101.5, 3024.5), 2 frames after previous cover
- f111: ref 79110: 25 -> 21 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 10 -> 25 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79097: 27 -> 24 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79103: 24 -> 12 at (2082, 3024), 1 frames after previous cover
- f112: ref 79105: 12 -> 21 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 21 -> 25 at (2109, 3027), 2 frames after previous cover
- f113: ref 79108: 25 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 21 -> 25 at (2117, 3027.5), 2 frames after previous cover
- f114: ref 79097: 24 -> 19 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 27 -> 24 at (2048, 3030), 1 frames after previous cover
- f114: ref 79102: 24 -> 27 at (2061.5, 3029), 5 frames after previous cover
- f115: ref 78899: 19 -> 26 at (2012.5, 3030), 2 frames after previous cover
- f115: ref 79045: 26 -> 22 at (1968.5, 3035.5), 1 frames after previous cover
- f115: ref 79103: 12 -> 7 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 21 -> 27 at (2073, 3025), 1 frames after previous cover
- f115: ref 79110: 25 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79115: 10 -> 12 at (2135.5, 3021), 2 frames after previous cover
- f116: ref 78897: 7 -> 26 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 79102: 27 -> 19 at (2049.5, 3030.5), 2 frames after previous cover
- f116: ref 79105: 27 -> 7 at (2067.5, 3026.5), 1 frames after previous cover
- f116: ref 79108: 21 -> 27 at (2087, 3026.5), 3 frames after previous cover
- f117: ref 78899: 26 -> 24 at (2001.5, 3032.5), 2 frames after previous cover
- f117: ref 79037: 11 -> 26 at (1968.5, 3034.5), 1 frames after previous cover
- f117: ref 79045: 22 -> 11 at (1956.5, 3034.5), 2 frames after previous cover
- f117: ref 79098: 24 -> 19 at (2031, 3030.5), 1 frames after previous cover
- f118: ref 79037: 26 -> 11 at (1964, 3035.5), 1 frames after previous cover
- f118: ref 79097: 19 -> 24 at (2010.5, 3030), 3 frames after previous cover
- ... 904 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 954 | 31 | 3 (954) |
| 78896 | 350 (76..429) | 294 | 29 | 26 (199), 8 (43), 22 (34), 11 (18) |
| 78969 | 352 (80..434) | 294 | 34 | 11 (179), 26 (26), 22 (23), 40 (23), 8 (21), 15 (16), 42 (6) |
| 78971 | 352 (84..439) | 284 | 37 | 22 (115), 40 (99), 26 (28), 11 (22), 15 (7), 31 (4), 42 (4), 7 (3), 8 (1), 35 (1) |
| 79045 | 355 (84..443) | 289 | 40 | 42 (108), 22 (75), 31 (42), 11 (30), 26 (13), 40 (5), 15 (4), 10 (3), 12 (3), 7 (2), 35 (2), 8 (2) |
| 79037 | 355 (86..445) | 288 | 44 | 40 (96), 22 (40), 36 (37), 11 (32), 31 (28), 7 (19), 42 (16), 27 (8), 8 (6), 15 (3), 35 (2), 26 (1) |
| 78897 | 345 (89..450) | 291 | 41 | 31 (103), 42 (53), 15 (32), 7 (28), 27 (19), 11 (14), 8 (10), 40 (8), 22 (8), 36 (8), 26 (5), 10 (2), +1 more |
| 78899 | 365 (91..455) | 294 | 46 | 27 (80), 31 (58), 36 (45), 42 (22), 15 (18), 11 (17), 22 (16), 7 (14), 26 (5), 19 (4), 35 (4), 8 (4), +4 more |
| 79097 | 366 (94..461) | 299 | 42 | 36 (136), 27 (51), 15 (18), 40 (14), 8 (12), 26 (11), 7 (11), 24 (9), 31 (9), 11 (7), 42 (7), 19 (5), +4 more |
| 79098 | 360 (97..467) | 307 | 42 | 8 (71), 27 (45), 7 (43), 31 (42), 36 (32), 24 (18), 42 (13), 19 (11), 35 (10), 28 (7), 40 (5), 15 (4), +4 more |
| 79102 | 371 (98..477) | 299 | 44 | 15 (98), 8 (97), 42 (26), 7 (19), 36 (16), 28 (12), 24 (9), 12 (6), 35 (5), 19 (4), 27 (3), 10 (2), +1 more |
| 79103 | 380 (99..481) | 308 | 47 | 15 (86), 7 (60), 8 (46), 31 (36), 28 (23), 24 (15), 38 (15), 12 (14), 26 (6), 42 (3), 10 (2), 19 (1), +1 more |
| 79105 | 379 (101..484) | 314 | 41 | 7 (155), 24 (50), 12 (39), 38 (16), 8 (16), 28 (11), 27 (9), 35 (6), 21 (5), 15 (5), 10 (1), 26 (1) |
| 79108 | 385 (104..492) | 319 | 45 | 24 (103), 28 (76), 12 (46), 27 (41), 7 (15), 36 (7), 8 (7), 15 (6), 35 (5), 21 (4), 10 (2), 26 (2), +4 more |
| 79110 | 388 (106..497) | 316 | 47 | 12 (71), 24 (70), 28 (53), 15 (30), 35 (20), 36 (13), 8 (13), 27 (11), 21 (9), 29 (8), 38 (7), 25 (5), +3 more |
| 79111 | 386 (109..500) | 331 | 39 | 24 (83), 35 (72), 29 (53), 28 (41), 12 (36), 21 (12), 27 (9), 25 (5), 19 (5), 36 (5), 38 (4), 15 (4), +1 more |
| 79115 | 421 (111..531) | 344 | 44 | 44 (87), 28 (78), 35 (53), 19 (47), 12 (19), 21 (18), 27 (9), 24 (8), 29 (7), 36 (5), 38 (5), 10 (4), +2 more |
| 79116 | 411 (114..530) | 358 | 37 | 25 (142), 21 (52), 28 (41), 35 (26), 43 (26), 12 (19), 29 (19), 19 (18), 27 (10), 10 (4), 24 (1) |
| 79122 | 404 (118..532) | 347 | 38 | 29 (99), 21 (49), 44 (41), 19 (30), 43 (29), 35 (22), 12 (21), 25 (21), 38 (20), 10 (7), 27 (7), 36 (1) |
| 79132 | 391 (120..515) | 325 | 41 | 29 (79), 19 (78), 21 (43), 12 (33), 25 (25), 38 (20), 27 (16), 35 (16), 28 (9), 10 (2), 43 (2), 24 (2) |
| 79128 | 402 (124..527) | 341 | 39 | 35 (123), 43 (56), 38 (39), 19 (32), 21 (27), 29 (21), 12 (20), 25 (19), 27 (3), 10 (1) |
| 79134 | 407 (127..533) | 350 | 38 | 21 (152), 38 (69), 19 (52), 29 (51), 43 (11), 25 (8), 12 (5), 10 (2) |
| 79135 | 409 (129..542) | 347 | 44 | 43 (145), 25 (48), 19 (39), 12 (28), 29 (27), 38 (25), 21 (24), 10 (11) |
| 79139 | 406 (132..537) | 354 | 35 | 38 (153), 25 (82), 19 (56), 10 (50), 29 (11), 43 (2) |
| 79136 | 393 (136..538) | 341 | 31 | 10 (305), 25 (34), 21 (1), 38 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 24; lifespan min/median/max: 164/410/995; tracks with internal gaps: 24; total internal gaps: 467; longest internal gap: 7; tracks ending in coasting: 23 (trailing rows total 649)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 14..1008 | 995 | 995 | 954 | 41 | 31 | 3 | 0 | 78911 |
| 7 | 84..513 | 430 | 430 | 372 | 58 | 26 | 5 | 21 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 8 | 87..496 | 410 | 410 | 349 | 61 | 22 | 4 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 10 | 89..565 | 477 | 477 | 406 | 71 | 26 | 6 | 28 | 78897, 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 89..463 | 375 | 375 | 321 | 54 | 20 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 12 | 91..524 | 434 | 434 | 367 | 67 | 25 | 4 | 27 | 78899, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 15 | 100..473 | 374 | 374 | 331 | 43 | 12 | 3 | 23 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 19 | 103..544 | 442 | 442 | 385 | 57 | 18 | 7 | 29 | 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 21 | 106..562 | 457 | 457 | 396 | 61 | 23 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 22 | 106..472 | 367 | 367 | 312 | 55 | 23 | 2 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 24 | 108..529 | 422 | 422 | 370 | 52 | 16 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 25 | 108..559 | 452 | 452 | 392 | 60 | 22 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 26 | 108..458 | 351 | 351 | 298 | 53 | 17 | 3 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108 |
| 27 | 108..484 | 377 | 377 | 321 | 56 | 18 | 3 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 28 | 121..520 | 400 | 400 | 351 | 49 | 14 | 3 | 30 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 29 | 126..561 | 436 | 436 | 375 | 61 | 21 | 4 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 31 | 126..510 | 385 | 385 | 324 | 61 | 22 | 3 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 35 | 134..556 | 423 | 423 | 372 | 51 | 17 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 36 | 136..489 | 354 | 354 | 305 | 49 | 17 | 2 | 28 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79122 |
| 38 | 142..567 | 426 | 426 | 375 | 51 | 17 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 40 | 158..468 | 311 | 311 | 253 | 58 | 22 | 2 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79108 |
| 42 | 205..506 | 302 | 302 | 258 | 44 | 16 | 2 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 43 | 248..571 | 324 | 324 | 273 | 51 | 15 | 4 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 44 | 397..560 | 164 | 164 | 128 | 36 | 7 | 1 | 29 | 79115, 79122 |
