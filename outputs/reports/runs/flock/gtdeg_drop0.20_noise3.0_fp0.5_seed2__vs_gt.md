# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=b9477ad2ea1d
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise3.0_fp0.5_seed2/tracks.csv sha256=b51973ffb167c3c9
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise3.0_fp0.5_seed2.csv sha256=b9477ad2ea1dbaee
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise3.0_fp0.5_seed2
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
| observations | none | 4 | 10142 | 8084 | 0.153 | 0.353 | 0.066 | 2.19 | 0.153 | 0.032 | 2.42 | 926 | 2458.0 | 0.159 | 0.179 | 0.143 | 0.460 | 0.577 | 4665 | 5477 | 3419 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 8084 | 0.211 | 0.496 | 0.090 | 2.75 | 0.257 | 0.458 | 3.22 | 1139 | 2083.0 | 0.239 | 0.269 | 0.214 | 0.683 | 0.857 | 6932 | 3210 | 1152 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 8084 | 0.242 | 0.567 | 0.103 | 3.07 | 0.304 | 0.613 | 3.63 | 1203 | 1699.0 | 0.274 | 0.309 | 0.246 | 0.765 | 0.959 | 7754 | 2388 | 330 | 0 | 25 | 0 |
| observations | none | 12 | 10142 | 8084 | 0.273 | 0.627 | 0.119 | 3.56 | 0.323 | 0.665 | 3.98 | 1099 | 1553.0 | 0.305 | 0.344 | 0.275 | 0.785 | 0.985 | 7965 | 2177 | 119 | 5 | 20 | 0 |
| observations | ignore | 4 | 10142 | 8084 | 0.153 | 0.353 | 0.066 | 2.19 | 0.153 | 0.032 | 2.42 | 926 | 2458.0 | 0.159 | 0.179 | 0.143 | 0.460 | 0.577 | 4665 | 5477 | 3419 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 8084 | 0.211 | 0.496 | 0.090 | 2.75 | 0.257 | 0.458 | 3.22 | 1139 | 2083.0 | 0.239 | 0.269 | 0.214 | 0.683 | 0.857 | 6932 | 3210 | 1152 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 8084 | 0.242 | 0.567 | 0.103 | 3.07 | 0.304 | 0.613 | 3.63 | 1203 | 1699.0 | 0.274 | 0.309 | 0.246 | 0.765 | 0.959 | 7754 | 2388 | 330 | 0 | 25 | 0 |
| observations | ignore | 12 | 10142 | 8084 | 0.273 | 0.627 | 0.119 | 3.56 | 0.323 | 0.665 | 3.98 | 1099 | 1553.0 | 0.305 | 0.344 | 0.275 | 0.785 | 0.985 | 7965 | 2177 | 119 | 5 | 20 | 0 |
| updates | none | 4 | 10142 | 10529 | 0.147 | 0.324 | 0.067 | 2.22 | 0.144 | -0.168 | 2.42 | 994 | 2500.0 | 0.150 | 0.147 | 0.152 | 0.484 | 0.466 | 4911 | 5231 | 5618 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10529 | 0.211 | 0.471 | 0.095 | 2.85 | 0.247 | 0.314 | 3.28 | 1179 | 1885.0 | 0.230 | 0.226 | 0.234 | 0.734 | 0.707 | 7445 | 2697 | 3084 | 0 | 25 | 0 |
| updates | none | 8 | 10142 | 10529 | 0.249 | 0.554 | 0.112 | 3.26 | 0.305 | 0.526 | 3.77 | 1225 | 1258.0 | 0.272 | 0.267 | 0.277 | 0.842 | 0.811 | 8544 | 1598 | 1985 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10529 | 0.290 | 0.631 | 0.133 | 3.86 | 0.346 | 0.653 | 4.37 | 1071 | 782.0 | 0.316 | 0.310 | 0.322 | 0.898 | 0.865 | 9112 | 1030 | 1417 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10529 | 0.147 | 0.324 | 0.067 | 2.22 | 0.144 | -0.168 | 2.42 | 994 | 2500.0 | 0.150 | 0.147 | 0.152 | 0.484 | 0.466 | 4911 | 5231 | 5618 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10529 | 0.211 | 0.471 | 0.095 | 2.85 | 0.247 | 0.314 | 3.28 | 1179 | 1885.0 | 0.230 | 0.226 | 0.234 | 0.734 | 0.707 | 7445 | 2697 | 3084 | 0 | 25 | 0 |
| updates | ignore | 8 | 10142 | 10529 | 0.249 | 0.554 | 0.112 | 3.26 | 0.305 | 0.526 | 3.77 | 1225 | 1258.0 | 0.272 | 0.267 | 0.277 | 0.842 | 0.811 | 8544 | 1598 | 1985 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10529 | 0.290 | 0.631 | 0.133 | 3.86 | 0.346 | 0.653 | 4.37 | 1071 | 782.0 | 0.316 | 0.310 | 0.322 | 0.898 | 0.865 | 9112 | 1030 | 1417 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7754; unmatched reference entries: 2388; unmatched candidate entries: 330
- identity switches: 1203; fragmentation (coverage interruptions): 1722; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 44 -> 46 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 42 -> 44 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 47 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 3 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 46 -> 47 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 53 -> 46 at (2105, 3028.5), 2 frames after previous cover
- f103: ref 79102: 42 -> 44 at (2124.5, 3027.5), 4 frames after previous cover
- f104: ref 78899: 47 -> 46 at (2079.5, 3030.5), 2 frames after previous cover
- f104: ref 78971: 43 -> 38 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 38 -> 49 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 46 -> 53 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 38 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 49 -> 38 at (2030.5, 3033.5), 1 frames after previous cover
- f107: ref 78971: 43 -> 38 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 38 -> 49 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 54 -> 61 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 42 -> 60 at (2131, 3027), 4 frames after previous cover
- f109: ref 79110: 42 -> 60 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 46 -> 65 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 44 -> 66 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 61 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 61 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 60 -> 67 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 42 -> 60 at (2142, 3026.5), 2 frames after previous cover
- f113: ref 79105: 54 -> 61 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 61 -> 67 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 65 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 79098: 66 -> 65 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 66 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 61 -> 44 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 67 -> 54 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 60 -> 61 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 42 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 46 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 46 -> 49 at (1983, 3035), 1 frames after previous cover
- f115: ref 79045: 49 -> 38 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78969: 43 -> 34 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 38 -> 43 at (1953, 3036), 5 frames after previous cover
- f116: ref 79102: 44 -> 65 at (2049.5, 3030.5), 3 frames after previous cover
- f117: ref 79102: 65 -> 66 at (2043.5, 3029.5), 1 frames after previous cover
- f117: ref 79111: 61 -> 67 at (2109, 3027.5), 1 frames after previous cover
- f118: ref 79098: 65 -> 53 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79110: 67 -> 54 at (2090, 3026.5), 3 frames after previous cover
- f119: ref 79097: 53 -> 47 at (2004, 3029), 2 frames after previous cover
- f119: ref 79102: 66 -> 65 at (2030, 3030), 2 frames after previous cover
- f119: ref 79115: 60 -> 67 at (2114, 3021), 2 frames after previous cover
- ... 1143 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 768 | 182 | 147 (518), 0 (250) |
| 78896 | 350 (76..429) | 270 | 60 | 34 (139), 91 (49), 66 (46), 49 (27), 82 (9) |
| 78969 | 352 (80..434) | 276 | 54 | 43 (75), 91 (52), 82 (48), 49 (27), 34 (22), 66 (21), 67 (17), 38 (14) |
| 78971 | 352 (84..439) | 271 | 56 | 43 (88), 49 (78), 91 (27), 66 (22), 82 (21), 47 (14), 67 (14), 38 (6), 53 (1) |
| 79045 | 355 (84..443) | 274 | 52 | 49 (78), 43 (75), 67 (45), 47 (43), 53 (14), 38 (13), 46 (4), 66 (2) |
| 79037 | 355 (86..445) | 269 | 63 | 43 (56), 47 (45), 67 (34), 65 (25), 46 (22), 189 (19), 91 (18), 49 (13), 82 (13), 34 (10), 66 (5), 53 (4), +2 more |
| 78897 | 345 (89..450) | 268 | 56 | 66 (81), 46 (37), 67 (37), 47 (35), 34 (33), 65 (24), 82 (7), 38 (4), 42 (2), 44 (2), 76 (2), 43 (2), +2 more |
| 78899 | 365 (91..455) | 281 | 62 | 53 (51), 67 (42), 34 (42), 66 (36), 82 (30), 46 (22), 38 (22), 65 (19), 47 (8), 97 (4), 42 (3), 44 (2) |
| 79097 | 366 (94..461) | 287 | 63 | 97 (57), 53 (56), 82 (47), 66 (41), 67 (21), 65 (20), 34 (15), 87 (14), 47 (5), 42 (3), 46 (3), 38 (3), +2 more |
| 79098 | 360 (97..467) | 270 | 68 | 97 (97), 82 (48), 34 (38), 53 (36), 87 (16), 66 (7), 65 (7), 83 (6), 44 (4), 38 (3), 46 (3), 42 (2), +2 more |
| 79102 | 371 (98..477) | 282 | 64 | 97 (56), 131 (49), 53 (48), 65 (29), 83 (18), 54 (15), 81 (13), 66 (11), 82 (11), 46 (10), 44 (8), 34 (5), +4 more |
| 79103 | 380 (99..481) | 294 | 65 | 131 (69), 53 (46), 87 (27), 54 (25), 65 (24), 46 (19), 83 (19), 67 (17), 97 (14), 38 (12), 82 (9), 81 (7), +2 more |
| 79105 | 379 (101..484) | 279 | 68 | 54 (58), 65 (32), 87 (30), 131 (29), 44 (28), 53 (23), 81 (23), 67 (22), 83 (16), 38 (5), 61 (4), 82 (4), +3 more |
| 79108 | 385 (104..492) | 287 | 70 | 44 (55), 83 (40), 81 (40), 65 (35), 87 (34), 131 (23), 54 (17), 79 (10), 38 (8), 53 (8), 88 (5), 67 (4), +5 more |
| 79110 | 388 (106..497) | 306 | 61 | 83 (71), 44 (54), 87 (53), 38 (25), 46 (25), 65 (22), 81 (18), 88 (14), 79 (9), 67 (5), 54 (5), 60 (2), +2 more |
| 79111 | 386 (109..500) | 288 | 69 | 46 (62), 38 (45), 44 (43), 83 (39), 81 (30), 65 (20), 79 (16), 54 (12), 88 (8), 60 (6), 61 (3), 42 (1), +3 more |
| 79115 | 421 (111..531) | 303 | 76 | 38 (68), 83 (54), 60 (39), 44 (30), 81 (28), 65 (27), 79 (14), 88 (10), 202 (10), 46 (6), 87 (5), 169 (5), +4 more |
| 79116 | 411 (114..530) | 318 | 66 | 60 (70), 88 (40), 38 (35), 81 (32), 44 (21), 65 (16), 76 (15), 61 (13), 79 (13), 87 (12), 54 (11), 83 (10), +6 more |
| 79122 | 404 (118..532) | 319 | 64 | 38 (76), 81 (59), 202 (47), 88 (31), 76 (20), 54 (19), 79 (19), 169 (16), 44 (8), 60 (7), 65 (5), 46 (4), +4 more |
| 79132 | 391 (120..515) | 299 | 60 | 171 (69), 76 (64), 88 (64), 169 (23), 38 (19), 87 (16), 79 (10), 81 (7), 54 (6), 83 (6), 158 (6), 60 (4), +3 more |
| 79128 | 402 (124..527) | 301 | 70 | 79 (87), 169 (62), 76 (39), 171 (30), 81 (16), 87 (15), 88 (15), 38 (9), 60 (7), 46 (6), 61 (5), 158 (5), +2 more |
| 79134 | 407 (127..533) | 322 | 66 | 88 (108), 158 (44), 76 (40), 79 (34), 87 (32), 61 (21), 46 (16), 60 (14), 169 (5), 81 (3), 42 (2), 171 (2), +1 more |
| 79135 | 409 (129..542) | 318 | 67 | 79 (117), 46 (78), 61 (35), 87 (23), 60 (17), 158 (16), 81 (15), 88 (9), 76 (5), 42 (3) |
| 79139 | 406 (132..537) | 304 | 67 | 60 (163), 61 (75), 158 (42), 76 (7), 46 (6), 88 (5), 42 (4), 79 (2) |
| 79136 | 393 (136..538) | 300 | 73 | 61 (175), 76 (52), 88 (33), 158 (25), 42 (10), 60 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 21/340/682; tracks with internal gaps: 31; total internal gaps: 296; longest internal gap: 3; tracks ending in coasting: 11 (trailing rows total 17)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..341 | 340 | 270 | 250 | 20 | 17 | 2 | 2 | 78911 |
| 34 | 78..467 | 390 | 318 | 304 | 14 | 11 | 2 | 0 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102 |
| 38 | 82..531 | 450 | 383 | 372 | 11 | 11 | 1 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 86..149 | 64 | 55 | 51 | 4 | 2 | 1 | 2 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 86..443 | 358 | 307 | 296 | 11 | 11 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 44 | 89..394 | 306 | 274 | 258 | 16 | 15 | 1 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 46 | 91..497 | 407 | 345 | 333 | 12 | 12 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 93..267 | 175 | 156 | 150 | 6 | 5 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 49 | 97..364 | 268 | 232 | 223 | 9 | 7 | 1 | 2 | 78896, 78969, 78971, 79037, 79045 |
| 53 | 100..439 | 340 | 297 | 288 | 9 | 9 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 100..307 | 208 | 180 | 172 | 8 | 7 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 60 | 108..521 | 414 | 349 | 336 | 13 | 13 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 108..537 | 430 | 351 | 339 | 12 | 10 | 2 | 0 | 79105, 79108, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 111..500 | 390 | 317 | 305 | 12 | 11 | 1 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 66 | 111..455 | 345 | 288 | 278 | 10 | 9 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 67 | 111..433 | 323 | 274 | 264 | 10 | 10 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 76 | 126..439 | 314 | 264 | 251 | 13 | 12 | 1 | 1 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 79 | 130..542 | 413 | 347 | 331 | 16 | 15 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 81 | 130..496 | 367 | 308 | 291 | 17 | 14 | 2 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 82 | 133..429 | 297 | 259 | 249 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 83 | 133..477 | 345 | 295 | 280 | 15 | 13 | 3 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 138..484 | 347 | 293 | 279 | 14 | 10 | 2 | 2 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 88 | 138..537 | 400 | 355 | 342 | 13 | 13 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 146..369 | 224 | 153 | 147 | 6 | 3 | 1 | 3 | 78896, 78897, 78969, 78971, 79037 |
| 97 | 184..461 | 278 | 235 | 229 | 6 | 6 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 131 | 290..484 | 195 | 177 | 172 | 5 | 5 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 147 | 327..1008 | 682 | 540 | 518 | 22 | 21 | 2 | 0 | 78911 |
| 158 | 349..533 | 185 | 146 | 143 | 3 | 2 | 2 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 169 | 383..527 | 145 | 121 | 113 | 8 | 7 | 2 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 171 | 383..515 | 133 | 113 | 111 | 2 | 2 | 1 | 0 | 79116, 79128, 79132, 79134 |
| 189 | 425..445 | 21 | 19 | 19 | 0 | 0 | 0 | 0 | 79037 |
| 202 | 457..532 | 76 | 63 | 60 | 3 | 3 | 1 | 0 | 79115, 79116, 79122 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7754; unmatched reference entries: 2388; unmatched candidate entries: 330
- identity switches: 1203; fragmentation (coverage interruptions): 1722; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 44 -> 46 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 42 -> 44 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f97: ref 79045: 47 -> 49 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 3 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 46 -> 47 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 53 -> 46 at (2105, 3028.5), 2 frames after previous cover
- f103: ref 79102: 42 -> 44 at (2124.5, 3027.5), 4 frames after previous cover
- f104: ref 78899: 47 -> 46 at (2079.5, 3030.5), 2 frames after previous cover
- f104: ref 78971: 43 -> 38 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 38 -> 49 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 46 -> 53 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 38 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 49 -> 38 at (2030.5, 3033.5), 1 frames after previous cover
- f107: ref 78971: 43 -> 38 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 38 -> 49 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 54 -> 61 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 42 -> 60 at (2131, 3027), 4 frames after previous cover
- f109: ref 79110: 42 -> 60 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 46 -> 65 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 44 -> 66 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 61 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 61 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 60 -> 67 at (2129, 3027), 2 frames after previous cover
- f111: ref 79111: 42 -> 60 at (2142, 3026.5), 2 frames after previous cover
- f113: ref 79105: 54 -> 61 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 61 -> 67 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 65 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 79098: 66 -> 65 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 66 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 61 -> 44 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 67 -> 54 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 60 -> 61 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 42 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 46 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 46 -> 49 at (1983, 3035), 1 frames after previous cover
- f115: ref 79045: 49 -> 38 at (1968.5, 3035.5), 1 frames after previous cover
- f116: ref 78969: 43 -> 34 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 38 -> 43 at (1953, 3036), 5 frames after previous cover
- f116: ref 79102: 44 -> 65 at (2049.5, 3030.5), 3 frames after previous cover
- f117: ref 79102: 65 -> 66 at (2043.5, 3029.5), 1 frames after previous cover
- f117: ref 79111: 61 -> 67 at (2109, 3027.5), 1 frames after previous cover
- f118: ref 79098: 65 -> 53 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79110: 67 -> 54 at (2090, 3026.5), 3 frames after previous cover
- f119: ref 79097: 53 -> 47 at (2004, 3029), 2 frames after previous cover
- f119: ref 79102: 66 -> 65 at (2030, 3030), 2 frames after previous cover
- f119: ref 79115: 60 -> 67 at (2114, 3021), 2 frames after previous cover
- ... 1143 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 768 | 182 | 147 (518), 0 (250) |
| 78896 | 350 (76..429) | 270 | 60 | 34 (139), 91 (49), 66 (46), 49 (27), 82 (9) |
| 78969 | 352 (80..434) | 276 | 54 | 43 (75), 91 (52), 82 (48), 49 (27), 34 (22), 66 (21), 67 (17), 38 (14) |
| 78971 | 352 (84..439) | 271 | 56 | 43 (88), 49 (78), 91 (27), 66 (22), 82 (21), 47 (14), 67 (14), 38 (6), 53 (1) |
| 79045 | 355 (84..443) | 274 | 52 | 49 (78), 43 (75), 67 (45), 47 (43), 53 (14), 38 (13), 46 (4), 66 (2) |
| 79037 | 355 (86..445) | 269 | 63 | 43 (56), 47 (45), 67 (34), 65 (25), 46 (22), 189 (19), 91 (18), 49 (13), 82 (13), 34 (10), 66 (5), 53 (4), +2 more |
| 78897 | 345 (89..450) | 268 | 56 | 66 (81), 46 (37), 67 (37), 47 (35), 34 (33), 65 (24), 82 (7), 38 (4), 42 (2), 44 (2), 76 (2), 43 (2), +2 more |
| 78899 | 365 (91..455) | 281 | 62 | 53 (51), 67 (42), 34 (42), 66 (36), 82 (30), 46 (22), 38 (22), 65 (19), 47 (8), 97 (4), 42 (3), 44 (2) |
| 79097 | 366 (94..461) | 287 | 63 | 97 (57), 53 (56), 82 (47), 66 (41), 67 (21), 65 (20), 34 (15), 87 (14), 47 (5), 42 (3), 46 (3), 38 (3), +2 more |
| 79098 | 360 (97..467) | 270 | 68 | 97 (97), 82 (48), 34 (38), 53 (36), 87 (16), 66 (7), 65 (7), 83 (6), 44 (4), 38 (3), 46 (3), 42 (2), +2 more |
| 79102 | 371 (98..477) | 282 | 64 | 97 (56), 131 (49), 53 (48), 65 (29), 83 (18), 54 (15), 81 (13), 66 (11), 82 (11), 46 (10), 44 (8), 34 (5), +4 more |
| 79103 | 380 (99..481) | 294 | 65 | 131 (69), 53 (46), 87 (27), 54 (25), 65 (24), 46 (19), 83 (19), 67 (17), 97 (14), 38 (12), 82 (9), 81 (7), +2 more |
| 79105 | 379 (101..484) | 279 | 68 | 54 (58), 65 (32), 87 (30), 131 (29), 44 (28), 53 (23), 81 (23), 67 (22), 83 (16), 38 (5), 61 (4), 82 (4), +3 more |
| 79108 | 385 (104..492) | 287 | 70 | 44 (55), 83 (40), 81 (40), 65 (35), 87 (34), 131 (23), 54 (17), 79 (10), 38 (8), 53 (8), 88 (5), 67 (4), +5 more |
| 79110 | 388 (106..497) | 306 | 61 | 83 (71), 44 (54), 87 (53), 38 (25), 46 (25), 65 (22), 81 (18), 88 (14), 79 (9), 67 (5), 54 (5), 60 (2), +2 more |
| 79111 | 386 (109..500) | 288 | 69 | 46 (62), 38 (45), 44 (43), 83 (39), 81 (30), 65 (20), 79 (16), 54 (12), 88 (8), 60 (6), 61 (3), 42 (1), +3 more |
| 79115 | 421 (111..531) | 303 | 76 | 38 (68), 83 (54), 60 (39), 44 (30), 81 (28), 65 (27), 79 (14), 88 (10), 202 (10), 46 (6), 87 (5), 169 (5), +4 more |
| 79116 | 411 (114..530) | 318 | 66 | 60 (70), 88 (40), 38 (35), 81 (32), 44 (21), 65 (16), 76 (15), 61 (13), 79 (13), 87 (12), 54 (11), 83 (10), +6 more |
| 79122 | 404 (118..532) | 319 | 64 | 38 (76), 81 (59), 202 (47), 88 (31), 76 (20), 54 (19), 79 (19), 169 (16), 44 (8), 60 (7), 65 (5), 46 (4), +4 more |
| 79132 | 391 (120..515) | 299 | 60 | 171 (69), 76 (64), 88 (64), 169 (23), 38 (19), 87 (16), 79 (10), 81 (7), 54 (6), 83 (6), 158 (6), 60 (4), +3 more |
| 79128 | 402 (124..527) | 301 | 70 | 79 (87), 169 (62), 76 (39), 171 (30), 81 (16), 87 (15), 88 (15), 38 (9), 60 (7), 46 (6), 61 (5), 158 (5), +2 more |
| 79134 | 407 (127..533) | 322 | 66 | 88 (108), 158 (44), 76 (40), 79 (34), 87 (32), 61 (21), 46 (16), 60 (14), 169 (5), 81 (3), 42 (2), 171 (2), +1 more |
| 79135 | 409 (129..542) | 318 | 67 | 79 (117), 46 (78), 61 (35), 87 (23), 60 (17), 158 (16), 81 (15), 88 (9), 76 (5), 42 (3) |
| 79139 | 406 (132..537) | 304 | 67 | 60 (163), 61 (75), 158 (42), 76 (7), 46 (6), 88 (5), 42 (4), 79 (2) |
| 79136 | 393 (136..538) | 300 | 73 | 61 (175), 76 (52), 88 (33), 158 (25), 42 (10), 60 (5) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 21/340/682; tracks with internal gaps: 31; total internal gaps: 296; longest internal gap: 3; tracks ending in coasting: 11 (trailing rows total 17)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..341 | 340 | 270 | 250 | 20 | 17 | 2 | 2 | 78911 |
| 34 | 78..467 | 390 | 318 | 304 | 14 | 11 | 2 | 0 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102 |
| 38 | 82..531 | 450 | 383 | 372 | 11 | 11 | 1 | 0 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 86..149 | 64 | 55 | 51 | 4 | 2 | 1 | 2 | 78897, 78899, 79037, 79097, 79098, 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 86..443 | 358 | 307 | 296 | 11 | 11 | 1 | 0 | 78897, 78969, 78971, 79037, 79045 |
| 44 | 89..394 | 306 | 274 | 258 | 16 | 15 | 1 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 46 | 91..497 | 407 | 345 | 333 | 12 | 12 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 93..267 | 175 | 156 | 150 | 6 | 5 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 49 | 97..364 | 268 | 232 | 223 | 9 | 7 | 1 | 2 | 78896, 78969, 78971, 79037, 79045 |
| 53 | 100..439 | 340 | 297 | 288 | 9 | 9 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 100..307 | 208 | 180 | 172 | 8 | 7 | 1 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 60 | 108..521 | 414 | 349 | 336 | 13 | 13 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 108..537 | 430 | 351 | 339 | 12 | 10 | 2 | 0 | 79105, 79108, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 111..500 | 390 | 317 | 305 | 12 | 11 | 1 | 1 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 66 | 111..455 | 345 | 288 | 278 | 10 | 9 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 67 | 111..433 | 323 | 274 | 264 | 10 | 10 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 76 | 126..439 | 314 | 264 | 251 | 13 | 12 | 1 | 1 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 79 | 130..542 | 413 | 347 | 331 | 16 | 15 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 81 | 130..496 | 367 | 308 | 291 | 17 | 14 | 2 | 1 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 82 | 133..429 | 297 | 259 | 249 | 10 | 10 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108 |
| 83 | 133..477 | 345 | 295 | 280 | 15 | 13 | 3 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 138..484 | 347 | 293 | 279 | 14 | 10 | 2 | 2 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 88 | 138..537 | 400 | 355 | 342 | 13 | 13 | 1 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 146..369 | 224 | 153 | 147 | 6 | 3 | 1 | 3 | 78896, 78897, 78969, 78971, 79037 |
| 97 | 184..461 | 278 | 235 | 229 | 6 | 6 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 131 | 290..484 | 195 | 177 | 172 | 5 | 5 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 147 | 327..1008 | 682 | 540 | 518 | 22 | 21 | 2 | 0 | 78911 |
| 158 | 349..533 | 185 | 146 | 143 | 3 | 2 | 2 | 0 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 169 | 383..527 | 145 | 121 | 113 | 8 | 7 | 2 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 171 | 383..515 | 133 | 113 | 111 | 2 | 2 | 1 | 0 | 79116, 79128, 79132, 79134 |
| 189 | 425..445 | 21 | 19 | 19 | 0 | 0 | 0 | 0 | 79037 |
| 202 | 457..532 | 76 | 63 | 60 | 3 | 3 | 1 | 0 | 79115, 79116, 79122 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8544; unmatched reference entries: 1598; unmatched candidate entries: 1985
- identity switches: 1225; fragmentation (coverage interruptions): 1187; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 44 -> 46 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 42 -> 44 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f96: ref 79045: 47 -> 43 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 79045: 43 -> 49 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 46 -> 47 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 53 -> 46 at (2105, 3028.5), 2 frames after previous cover
- f102: ref 79098: 44 -> 53 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 42 -> 44 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 79103: 42 -> 54 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 54 -> 42 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78899: 47 -> 46 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 78971: 43 -> 38 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 38 -> 49 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 46 -> 53 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 38 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 49 -> 38 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79098: 53 -> 44 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79105: 42 -> 54 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 78971: 43 -> 38 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 38 -> 49 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 54 -> 61 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 42 -> 60 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 42 -> 60 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 46 -> 65 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 44 -> 66 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 61 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 61 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 60 -> 67 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 42 -> 60 at (2142, 3026.5), 1 frames after previous cover
- f113: ref 79045: 49 -> 38 at (1982.5, 3034), 2 frames after previous cover
- f113: ref 79105: 54 -> 61 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 61 -> 67 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 65 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 78971: 38 -> 49 at (1966, 3035), 2 frames after previous cover
- f114: ref 79098: 66 -> 65 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 66 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 61 -> 44 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 67 -> 54 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 60 -> 61 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 42 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 46 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 46 -> 49 at (1983, 3035), 1 frames after previous cover
- f116: ref 78969: 43 -> 34 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 49 -> 43 at (1953, 3036), 2 frames after previous cover
- f116: ref 79102: 44 -> 65 at (2049.5, 3030.5), 3 frames after previous cover
- ... 1165 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 916 | 73 | 147 (620), 0 (296) |
| 78896 | 350 (76..429) | 295 | 38 | 34 (153), 91 (53), 66 (51), 49 (29), 82 (9) |
| 78969 | 352 (80..434) | 293 | 45 | 43 (78), 91 (57), 82 (48), 49 (28), 34 (25), 66 (24), 67 (18), 38 (15) |
| 78971 | 352 (84..439) | 301 | 38 | 43 (98), 49 (87), 91 (30), 66 (24), 82 (24), 47 (16), 67 (15), 38 (7) |
| 79045 | 355 (84..443) | 296 | 34 | 49 (83), 43 (78), 67 (49), 47 (48), 53 (16), 38 (15), 46 (4), 66 (2), 82 (1) |
| 79037 | 355 (86..445) | 292 | 48 | 43 (62), 47 (47), 67 (40), 65 (29), 46 (23), 189 (21), 91 (20), 49 (13), 82 (12), 34 (11), 66 (5), 53 (4), +2 more |
| 78897 | 345 (89..450) | 282 | 48 | 66 (85), 67 (40), 46 (37), 47 (34), 34 (34), 65 (29), 82 (8), 38 (4), 42 (2), 44 (2), 76 (2), 43 (2), +3 more |
| 78899 | 365 (91..455) | 305 | 47 | 53 (52), 34 (50), 67 (45), 66 (35), 82 (35), 46 (25), 38 (23), 65 (19), 47 (8), 97 (4), 42 (3), 44 (3), +1 more |
| 79097 | 366 (94..461) | 314 | 41 | 97 (66), 53 (62), 82 (48), 66 (46), 67 (23), 65 (22), 34 (16), 87 (15), 47 (5), 42 (3), 46 (3), 38 (3), +2 more |
| 79098 | 360 (97..467) | 294 | 51 | 97 (105), 82 (49), 34 (46), 53 (38), 87 (18), 66 (7), 65 (7), 83 (7), 44 (4), 38 (4), 46 (3), 131 (3), +2 more |
| 79102 | 371 (98..477) | 303 | 49 | 97 (67), 131 (52), 53 (48), 65 (32), 83 (20), 54 (16), 81 (13), 66 (11), 82 (11), 46 (10), 44 (9), 34 (5), +4 more |
| 79103 | 380 (99..481) | 311 | 51 | 131 (71), 53 (50), 87 (29), 65 (26), 54 (23), 46 (21), 83 (20), 67 (17), 97 (15), 38 (12), 82 (10), 81 (7), +3 more |
| 79105 | 379 (101..484) | 307 | 51 | 54 (67), 65 (38), 87 (31), 131 (31), 44 (29), 67 (25), 53 (25), 81 (24), 83 (17), 38 (5), 61 (4), 82 (4), +4 more |
| 79108 | 385 (104..492) | 310 | 56 | 44 (58), 81 (47), 83 (42), 65 (40), 87 (37), 131 (23), 54 (17), 79 (10), 53 (9), 38 (8), 88 (6), 67 (4), +5 more |
| 79110 | 388 (106..497) | 331 | 41 | 83 (80), 87 (57), 44 (55), 46 (30), 38 (26), 65 (23), 81 (19), 88 (14), 79 (9), 54 (6), 67 (5), 60 (3), +3 more |
| 79111 | 386 (109..500) | 322 | 47 | 46 (68), 38 (50), 44 (46), 83 (44), 81 (34), 65 (26), 79 (18), 54 (12), 88 (8), 60 (6), 61 (3), 42 (2), +4 more |
| 79115 | 421 (111..531) | 343 | 48 | 38 (84), 83 (59), 60 (45), 44 (33), 81 (32), 65 (26), 79 (16), 202 (12), 88 (10), 169 (7), 46 (6), 87 (5), +5 more |
| 79116 | 411 (114..530) | 349 | 47 | 60 (82), 88 (42), 38 (38), 81 (34), 44 (24), 65 (18), 76 (15), 79 (15), 61 (14), 83 (13), 87 (13), 54 (11), +6 more |
| 79122 | 404 (118..532) | 345 | 49 | 38 (84), 81 (65), 202 (52), 88 (31), 54 (21), 76 (20), 79 (20), 169 (17), 44 (9), 60 (7), 65 (6), 46 (4), +4 more |
| 79132 | 391 (120..515) | 322 | 46 | 171 (76), 76 (71), 88 (66), 169 (24), 38 (20), 87 (18), 79 (10), 81 (7), 83 (7), 158 (7), 54 (6), 60 (4), +3 more |
| 79128 | 402 (124..527) | 337 | 49 | 79 (98), 169 (70), 76 (47), 171 (36), 81 (17), 88 (17), 87 (15), 38 (10), 60 (6), 46 (6), 61 (5), 158 (5), +2 more |
| 79134 | 407 (127..533) | 351 | 45 | 88 (117), 76 (47), 158 (47), 87 (37), 79 (35), 61 (21), 46 (18), 60 (14), 169 (7), 81 (3), 42 (2), 171 (2), +1 more |
| 79135 | 409 (129..542) | 341 | 57 | 79 (126), 46 (80), 61 (35), 87 (25), 60 (18), 158 (18), 81 (17), 88 (11), 76 (5), 42 (3), 171 (3) |
| 79139 | 406 (132..537) | 343 | 47 | 60 (179), 61 (77), 158 (48), 88 (20), 76 (7), 46 (6), 42 (4), 202 (2) |
| 79136 | 393 (136..538) | 341 | 41 | 61 (206), 76 (58), 158 (36), 88 (23), 42 (11), 60 (6), 79 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 50/369/682; tracks with internal gaps: 32; total internal gaps: 787; longest internal gap: 15; tracks ending in coasting: 31 (trailing rows total 916)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..370 | 369 | 369 | 296 | 73 | 22 | 3 | 46 | 78911 |
| 34 | 78..496 | 419 | 419 | 340 | 79 | 36 | 5 | 29 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102 |
| 38 | 82..560 | 479 | 479 | 413 | 66 | 32 | 2 | 29 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 86..178 | 93 | 93 | 58 | 35 | 3 | 2 | 31 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 86..472 | 387 | 387 | 318 | 69 | 29 | 7 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 44 | 89..423 | 335 | 335 | 275 | 60 | 26 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 46 | 91..526 | 436 | 436 | 356 | 80 | 43 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 93..296 | 204 | 204 | 158 | 46 | 13 | 2 | 30 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 49 | 97..393 | 297 | 297 | 240 | 57 | 16 | 3 | 34 | 78896, 78969, 78971, 79037, 79045 |
| 53 | 100..468 | 369 | 369 | 305 | 64 | 31 | 2 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 100..336 | 237 | 237 | 183 | 54 | 21 | 2 | 31 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 60 | 108..550 | 443 | 443 | 372 | 71 | 33 | 12 | 16 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 108..566 | 459 | 459 | 374 | 85 | 41 | 8 | 28 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 111..529 | 419 | 419 | 341 | 78 | 33 | 6 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 66 | 111..484 | 374 | 374 | 297 | 77 | 31 | 3 | 35 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 67 | 111..462 | 352 | 352 | 288 | 64 | 26 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 76 | 126..468 | 343 | 343 | 279 | 64 | 26 | 4 | 30 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 79 | 130..571 | 442 | 442 | 358 | 84 | 36 | 6 | 34 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 81 | 130..525 | 396 | 396 | 319 | 77 | 35 | 4 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 82 | 133..458 | 326 | 326 | 261 | 65 | 28 | 9 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 83 | 133..506 | 374 | 374 | 310 | 64 | 25 | 5 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 138..513 | 376 | 376 | 302 | 74 | 27 | 4 | 36 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 88 | 138..566 | 429 | 429 | 365 | 64 | 28 | 2 | 32 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 146..398 | 253 | 253 | 161 | 92 | 16 | 3 | 72 | 78896, 78897, 78969, 78971, 79037 |
| 97 | 184..490 | 307 | 307 | 258 | 49 | 19 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 131 | 290..513 | 224 | 224 | 182 | 42 | 14 | 15 | 13 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 147 | 327..1008 | 682 | 682 | 620 | 62 | 50 | 3 | 0 | 78911 |
| 158 | 349..562 | 214 | 214 | 167 | 47 | 16 | 2 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 169 | 383..556 | 174 | 174 | 127 | 47 | 10 | 3 | 32 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 171 | 383..544 | 162 | 162 | 127 | 35 | 10 | 12 | 2 | 79116, 79128, 79132, 79134, 79135 |
| 189 | 425..474 | 50 | 50 | 25 | 25 | 2 | 4 | 19 | 78897, 78899, 79037 |
| 202 | 457..561 | 105 | 105 | 69 | 36 | 9 | 3 | 24 | 79115, 79116, 79122, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8544; unmatched reference entries: 1598; unmatched candidate entries: 1985
- identity switches: 1225; fragmentation (coverage interruptions): 1187; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 42 -> 44 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 42 -> 44 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 44 -> 46 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 78897: 44 -> 46 at (2132, 3032), 1 frames after previous cover
- f95: ref 78899: 42 -> 44 at (2134.5, 3029), 2 frames after previous cover
- f95: ref 79037: 46 -> 47 at (2105, 3034.5), 3 frames after previous cover
- f96: ref 79045: 47 -> 43 at (2087.5, 3033.5), 2 frames after previous cover
- f97: ref 79045: 43 -> 49 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 79097: 42 -> 44 at (2129, 3028), 2 frames after previous cover
- f99: ref 78897: 46 -> 47 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 78899: 44 -> 46 at (2109.5, 3030), 2 frames after previous cover
- f99: ref 79037: 47 -> 49 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 49 -> 38 at (2068, 3033.5), 1 frames after previous cover
- f99: ref 79098: 42 -> 44 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 78969: 38 -> 43 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79097: 44 -> 53 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 46 -> 47 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 79097: 53 -> 46 at (2105, 3028.5), 2 frames after previous cover
- f102: ref 79098: 44 -> 53 at (2118, 3027), 1 frames after previous cover
- f102: ref 79102: 42 -> 44 at (2130.5, 3027), 3 frames after previous cover
- f103: ref 79103: 42 -> 54 at (2133.5, 3022.5), 1 frames after previous cover
- f103: ref 79105: 54 -> 42 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78899: 47 -> 46 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 78971: 43 -> 38 at (2027.5, 3034.5), 5 frames after previous cover
- f104: ref 79037: 49 -> 47 at (2051, 3034), 1 frames after previous cover
- f104: ref 79045: 38 -> 49 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79097: 46 -> 53 at (2093.5, 3029.5), 1 frames after previous cover
- f105: ref 78971: 38 -> 43 at (2022, 3034), 1 frames after previous cover
- f105: ref 79037: 47 -> 49 at (2044.5, 3034), 1 frames after previous cover
- f105: ref 79045: 49 -> 38 at (2030.5, 3033.5), 1 frames after previous cover
- f105: ref 79098: 53 -> 44 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79105: 42 -> 54 at (2130.5, 3023.5), 2 frames after previous cover
- f107: ref 78971: 43 -> 38 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79045: 38 -> 49 at (2019, 3033.5), 1 frames after previous cover
- f108: ref 79037: 49 -> 46 at (2026, 3034), 2 frames after previous cover
- f108: ref 79105: 54 -> 61 at (2113.5, 3025), 1 frames after previous cover
- f108: ref 79108: 42 -> 60 at (2131, 3027), 3 frames after previous cover
- f109: ref 79110: 42 -> 60 at (2139.5, 3026.5), 3 frames after previous cover
- f111: ref 78899: 46 -> 65 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 44 -> 66 at (2065.5, 3029), 6 frames after previous cover
- f111: ref 79105: 61 -> 54 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 60 -> 61 at (2113.5, 3026), 3 frames after previous cover
- f111: ref 79110: 60 -> 67 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 42 -> 60 at (2142, 3026.5), 1 frames after previous cover
- f113: ref 79045: 49 -> 38 at (1982.5, 3034), 2 frames after previous cover
- f113: ref 79105: 54 -> 61 at (2085, 3025), 1 frames after previous cover
- f113: ref 79108: 61 -> 67 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78899: 65 -> 47 at (2018, 3031), 1 frames after previous cover
- f114: ref 78971: 38 -> 49 at (1966, 3035), 2 frames after previous cover
- f114: ref 79098: 66 -> 65 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 54 -> 66 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 61 -> 44 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 67 -> 54 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79111: 60 -> 61 at (2126, 3027), 1 frames after previous cover
- f114: ref 79115: 42 -> 60 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 78897: 47 -> 46 at (1996, 3033.5), 2 frames after previous cover
- f115: ref 79037: 46 -> 49 at (1983, 3035), 1 frames after previous cover
- f116: ref 78969: 43 -> 34 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 49 -> 43 at (1953, 3036), 2 frames after previous cover
- f116: ref 79102: 44 -> 65 at (2049.5, 3030.5), 3 frames after previous cover
- ... 1165 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 916 | 73 | 147 (620), 0 (296) |
| 78896 | 350 (76..429) | 295 | 38 | 34 (153), 91 (53), 66 (51), 49 (29), 82 (9) |
| 78969 | 352 (80..434) | 293 | 45 | 43 (78), 91 (57), 82 (48), 49 (28), 34 (25), 66 (24), 67 (18), 38 (15) |
| 78971 | 352 (84..439) | 301 | 38 | 43 (98), 49 (87), 91 (30), 66 (24), 82 (24), 47 (16), 67 (15), 38 (7) |
| 79045 | 355 (84..443) | 296 | 34 | 49 (83), 43 (78), 67 (49), 47 (48), 53 (16), 38 (15), 46 (4), 66 (2), 82 (1) |
| 79037 | 355 (86..445) | 292 | 48 | 43 (62), 47 (47), 67 (40), 65 (29), 46 (23), 189 (21), 91 (20), 49 (13), 82 (12), 34 (11), 66 (5), 53 (4), +2 more |
| 78897 | 345 (89..450) | 282 | 48 | 66 (85), 67 (40), 46 (37), 47 (34), 34 (34), 65 (29), 82 (8), 38 (4), 42 (2), 44 (2), 76 (2), 43 (2), +3 more |
| 78899 | 365 (91..455) | 305 | 47 | 53 (52), 34 (50), 67 (45), 66 (35), 82 (35), 46 (25), 38 (23), 65 (19), 47 (8), 97 (4), 42 (3), 44 (3), +1 more |
| 79097 | 366 (94..461) | 314 | 41 | 97 (66), 53 (62), 82 (48), 66 (46), 67 (23), 65 (22), 34 (16), 87 (15), 47 (5), 42 (3), 46 (3), 38 (3), +2 more |
| 79098 | 360 (97..467) | 294 | 51 | 97 (105), 82 (49), 34 (46), 53 (38), 87 (18), 66 (7), 65 (7), 83 (7), 44 (4), 38 (4), 46 (3), 131 (3), +2 more |
| 79102 | 371 (98..477) | 303 | 49 | 97 (67), 131 (52), 53 (48), 65 (32), 83 (20), 54 (16), 81 (13), 66 (11), 82 (11), 46 (10), 44 (9), 34 (5), +4 more |
| 79103 | 380 (99..481) | 311 | 51 | 131 (71), 53 (50), 87 (29), 65 (26), 54 (23), 46 (21), 83 (20), 67 (17), 97 (15), 38 (12), 82 (10), 81 (7), +3 more |
| 79105 | 379 (101..484) | 307 | 51 | 54 (67), 65 (38), 87 (31), 131 (31), 44 (29), 67 (25), 53 (25), 81 (24), 83 (17), 38 (5), 61 (4), 82 (4), +4 more |
| 79108 | 385 (104..492) | 310 | 56 | 44 (58), 81 (47), 83 (42), 65 (40), 87 (37), 131 (23), 54 (17), 79 (10), 53 (9), 38 (8), 88 (6), 67 (4), +5 more |
| 79110 | 388 (106..497) | 331 | 41 | 83 (80), 87 (57), 44 (55), 46 (30), 38 (26), 65 (23), 81 (19), 88 (14), 79 (9), 54 (6), 67 (5), 60 (3), +3 more |
| 79111 | 386 (109..500) | 322 | 47 | 46 (68), 38 (50), 44 (46), 83 (44), 81 (34), 65 (26), 79 (18), 54 (12), 88 (8), 60 (6), 61 (3), 42 (2), +4 more |
| 79115 | 421 (111..531) | 343 | 48 | 38 (84), 83 (59), 60 (45), 44 (33), 81 (32), 65 (26), 79 (16), 202 (12), 88 (10), 169 (7), 46 (6), 87 (5), +5 more |
| 79116 | 411 (114..530) | 349 | 47 | 60 (82), 88 (42), 38 (38), 81 (34), 44 (24), 65 (18), 76 (15), 79 (15), 61 (14), 83 (13), 87 (13), 54 (11), +6 more |
| 79122 | 404 (118..532) | 345 | 49 | 38 (84), 81 (65), 202 (52), 88 (31), 54 (21), 76 (20), 79 (20), 169 (17), 44 (9), 60 (7), 65 (6), 46 (4), +4 more |
| 79132 | 391 (120..515) | 322 | 46 | 171 (76), 76 (71), 88 (66), 169 (24), 38 (20), 87 (18), 79 (10), 81 (7), 83 (7), 158 (7), 54 (6), 60 (4), +3 more |
| 79128 | 402 (124..527) | 337 | 49 | 79 (98), 169 (70), 76 (47), 171 (36), 81 (17), 88 (17), 87 (15), 38 (10), 60 (6), 46 (6), 61 (5), 158 (5), +2 more |
| 79134 | 407 (127..533) | 351 | 45 | 88 (117), 76 (47), 158 (47), 87 (37), 79 (35), 61 (21), 46 (18), 60 (14), 169 (7), 81 (3), 42 (2), 171 (2), +1 more |
| 79135 | 409 (129..542) | 341 | 57 | 79 (126), 46 (80), 61 (35), 87 (25), 60 (18), 158 (18), 81 (17), 88 (11), 76 (5), 42 (3), 171 (3) |
| 79139 | 406 (132..537) | 343 | 47 | 60 (179), 61 (77), 158 (48), 88 (20), 76 (7), 46 (6), 42 (4), 202 (2) |
| 79136 | 393 (136..538) | 341 | 41 | 61 (206), 76 (58), 158 (36), 88 (23), 42 (11), 60 (6), 79 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 50/369/682; tracks with internal gaps: 32; total internal gaps: 787; longest internal gap: 15; tracks ending in coasting: 31 (trailing rows total 916)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..370 | 369 | 369 | 296 | 73 | 22 | 3 | 46 | 78911 |
| 34 | 78..496 | 419 | 419 | 340 | 79 | 36 | 5 | 29 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102 |
| 38 | 82..560 | 479 | 479 | 413 | 66 | 32 | 2 | 29 | 78897, 78899, 78969, 78971, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 42 | 86..178 | 93 | 93 | 58 | 35 | 3 | 2 | 31 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 86..472 | 387 | 387 | 318 | 69 | 29 | 7 | 29 | 78897, 78969, 78971, 79037, 79045 |
| 44 | 89..423 | 335 | 335 | 275 | 60 | 26 | 2 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 46 | 91..526 | 436 | 436 | 356 | 80 | 43 | 3 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 47 | 93..296 | 204 | 204 | 158 | 46 | 13 | 2 | 30 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 49 | 97..393 | 297 | 297 | 240 | 57 | 16 | 3 | 34 | 78896, 78969, 78971, 79037, 79045 |
| 53 | 100..468 | 369 | 369 | 305 | 64 | 31 | 2 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 54 | 100..336 | 237 | 237 | 183 | 54 | 21 | 2 | 31 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 60 | 108..550 | 443 | 443 | 372 | 71 | 33 | 12 | 16 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 108..566 | 459 | 459 | 374 | 85 | 41 | 8 | 28 | 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 65 | 111..529 | 419 | 419 | 341 | 78 | 33 | 6 | 30 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 66 | 111..484 | 374 | 374 | 297 | 77 | 31 | 3 | 35 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 67 | 111..462 | 352 | 352 | 288 | 64 | 26 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 76 | 126..468 | 343 | 343 | 279 | 64 | 26 | 4 | 30 | 78897, 79097, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 79 | 130..571 | 442 | 442 | 358 | 84 | 36 | 6 | 34 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 81 | 130..525 | 396 | 396 | 319 | 77 | 35 | 4 | 30 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 82 | 133..458 | 326 | 326 | 261 | 65 | 28 | 9 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 83 | 133..506 | 374 | 374 | 310 | 64 | 25 | 5 | 29 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 87 | 138..513 | 376 | 376 | 302 | 74 | 27 | 4 | 36 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 88 | 138..566 | 429 | 429 | 365 | 64 | 28 | 2 | 32 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 91 | 146..398 | 253 | 253 | 161 | 92 | 16 | 3 | 72 | 78896, 78897, 78969, 78971, 79037 |
| 97 | 184..490 | 307 | 307 | 258 | 49 | 19 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 131 | 290..513 | 224 | 224 | 182 | 42 | 14 | 15 | 13 | 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 147 | 327..1008 | 682 | 682 | 620 | 62 | 50 | 3 | 0 | 78911 |
| 158 | 349..562 | 214 | 214 | 167 | 47 | 16 | 2 | 29 | 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 169 | 383..556 | 174 | 174 | 127 | 47 | 10 | 3 | 32 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 171 | 383..544 | 162 | 162 | 127 | 35 | 10 | 12 | 2 | 79116, 79128, 79132, 79134, 79135 |
| 189 | 425..474 | 50 | 50 | 25 | 25 | 2 | 4 | 19 | 78897, 78899, 79037 |
| 202 | 457..561 | 105 | 105 | 69 | 36 | 9 | 3 | 24 | 79115, 79116, 79122, 79139 |
