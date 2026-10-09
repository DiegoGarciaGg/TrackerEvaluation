# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=a988b19baffb
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise1.0_fp0.5_seed3/tracks.csv sha256=112c29ff5aeeaa64
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise1.0_fp0.5_seed3.csv sha256=a988b19baffbcb47
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise1.0_fp0.5_seed3
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
| observations | none | 4 | 10142 | 7118 | 0.210 | 0.576 | 0.076 | 1.07 | 0.248 | 0.525 | 1.26 | 1665 | 2016.0 | 0.200 | 0.242 | 0.170 | 0.696 | 0.991 | 7054 | 3088 | 64 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 7118 | 0.225 | 0.616 | 0.082 | 1.16 | 0.249 | 0.526 | 1.27 | 1660 | 2011.0 | 0.200 | 0.243 | 0.171 | 0.696 | 0.992 | 7058 | 3084 | 60 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 7118 | 0.233 | 0.634 | 0.085 | 1.23 | 0.249 | 0.529 | 1.31 | 1628 | 2006.0 | 0.204 | 0.248 | 0.174 | 0.696 | 0.991 | 7054 | 3088 | 64 | 0 | 25 | 0 |
| observations | none | 12 | 10142 | 7118 | 0.242 | 0.650 | 0.090 | 1.42 | 0.252 | 0.537 | 1.67 | 1513 | 1958.0 | 0.223 | 0.270 | 0.190 | 0.694 | 0.989 | 7039 | 3103 | 79 | 0 | 25 | 0 |
| observations | ignore | 4 | 10142 | 7118 | 0.210 | 0.576 | 0.076 | 1.07 | 0.248 | 0.525 | 1.26 | 1665 | 2016.0 | 0.200 | 0.242 | 0.170 | 0.696 | 0.991 | 7054 | 3088 | 64 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 7118 | 0.225 | 0.616 | 0.082 | 1.16 | 0.249 | 0.526 | 1.27 | 1660 | 2011.0 | 0.200 | 0.243 | 0.171 | 0.696 | 0.992 | 7058 | 3084 | 60 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 7118 | 0.233 | 0.634 | 0.085 | 1.23 | 0.249 | 0.529 | 1.31 | 1628 | 2006.0 | 0.204 | 0.248 | 0.174 | 0.696 | 0.991 | 7054 | 3088 | 64 | 0 | 25 | 0 |
| observations | ignore | 12 | 10142 | 7118 | 0.242 | 0.650 | 0.090 | 1.42 | 0.252 | 0.537 | 1.67 | 1513 | 1958.0 | 0.223 | 0.270 | 0.190 | 0.694 | 0.989 | 7039 | 3103 | 79 | 0 | 25 | 0 |
| updates | none | 4 | 10142 | 9689 | 0.204 | 0.514 | 0.081 | 1.21 | 0.232 | 0.327 | 1.32 | 1695 | 1940.0 | 0.184 | 0.189 | 0.180 | 0.725 | 0.758 | 7349 | 2793 | 2340 | 1 | 24 | 0 |
| updates | none | 6 | 10142 | 9689 | 0.233 | 0.585 | 0.093 | 1.47 | 0.255 | 0.414 | 1.54 | 1700 | 1633.0 | 0.199 | 0.204 | 0.195 | 0.769 | 0.805 | 7795 | 2347 | 1894 | 1 | 24 | 0 |
| updates | none | 8 | 10142 | 9689 | 0.250 | 0.622 | 0.101 | 1.67 | 0.278 | 0.502 | 1.87 | 1631 | 1348.0 | 0.218 | 0.223 | 0.213 | 0.809 | 0.847 | 8204 | 1938 | 1485 | 11 | 14 | 0 |
| updates | none | 12 | 10142 | 9689 | 0.270 | 0.659 | 0.110 | 2.03 | 0.292 | 0.547 | 2.39 | 1481 | 1178.0 | 0.241 | 0.246 | 0.235 | 0.824 | 0.863 | 8360 | 1782 | 1329 | 14 | 11 | 0 |
| updates | ignore | 4 | 10142 | 9689 | 0.204 | 0.514 | 0.081 | 1.21 | 0.232 | 0.327 | 1.32 | 1695 | 1940.0 | 0.184 | 0.189 | 0.180 | 0.725 | 0.758 | 7349 | 2793 | 2340 | 1 | 24 | 0 |
| updates | ignore | 6 | 10142 | 9689 | 0.233 | 0.585 | 0.093 | 1.47 | 0.255 | 0.414 | 1.54 | 1700 | 1633.0 | 0.199 | 0.204 | 0.195 | 0.769 | 0.805 | 7795 | 2347 | 1894 | 1 | 24 | 0 |
| updates | ignore | 8 | 10142 | 9689 | 0.250 | 0.622 | 0.101 | 1.67 | 0.278 | 0.502 | 1.87 | 1631 | 1348.0 | 0.218 | 0.223 | 0.213 | 0.809 | 0.847 | 8204 | 1938 | 1485 | 11 | 14 | 0 |
| updates | ignore | 12 | 10142 | 9689 | 0.270 | 0.659 | 0.110 | 2.03 | 0.292 | 0.547 | 2.39 | 1481 | 1178.0 | 0.241 | 0.246 | 0.235 | 0.824 | 0.863 | 8360 | 1782 | 1329 | 14 | 11 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7054; unmatched reference entries: 3088; unmatched candidate entries: 64
- identity switches: 1628; fragmentation (coverage interruptions): 2054; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 48 -> 49 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 48 -> 49 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 49 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 48 -> 49 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 50 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 49 -> 50 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 48 -> 49 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 49 -> 50 at (2107, 3033), 2 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79045: 50 -> 57 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 50 -> 57 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 48 -> 49 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 50 -> 57 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 48 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 57 -> 61 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 49 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 57 -> 45 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 49 -> 61 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 50 -> 57 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 45 -> 57 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 57 -> 61 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 61 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 45 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 62 -> 61 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 45 -> 62 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 57 -> 50 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 50 -> 48 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 61 -> 57 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 61 -> 62 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 62 -> 61 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 48 -> 50 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 57 -> 62 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 62 -> 61 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 61 -> 64 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 49 -> 48 at (2110, 3022.5), 6 frames after previous cover
- f108: ref 78899: 57 -> 70 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 61 -> 57 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 61 -> 64 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 64 -> 61 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79098: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 48 -> 72 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 70 -> 62 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 57 -> 61 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 61 -> 57 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 50 -> 70 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 48 -> 50 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 49 -> 48 at (2101.5, 3024.5), 4 frames after previous cover
- f111: ref 78897: 62 -> 64 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 62 -> 57 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 45 -> 41 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 64 -> 45 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 70 -> 62 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 50 -> 70 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 48 -> 50 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 49 -> 72 at (2113.5, 3026), 1 frames after previous cover
- ... 1568 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 697 | 210 | 215 (391), 1 (306) |
| 78896 | 350 (76..429) | 242 | 75 | 82 (120), 77 (84), 41 (29), 155 (9) |
| 78969 | 352 (80..434) | 248 | 66 | 130 (45), 82 (42), 41 (34), 72 (24), 57 (22), 76 (20), 45 (19), 155 (19), 77 (10), 61 (7), 186 (5), 154 (1) |
| 78971 | 352 (84..439) | 236 | 72 | 155 (49), 57 (30), 134 (26), 72 (21), 41 (18), 76 (16), 77 (14), 45 (12), 61 (12), 82 (12), 62 (11), 95 (8), +2 more |
| 79045 | 355 (84..443) | 235 | 79 | 61 (43), 134 (34), 57 (33), 72 (33), 41 (26), 155 (23), 45 (10), 76 (10), 77 (7), 49 (3), 62 (3), 82 (3), +4 more |
| 79037 | 355 (86..445) | 238 | 76 | 57 (65), 61 (33), 134 (25), 49 (23), 72 (18), 95 (14), 76 (9), 155 (7), 45 (6), 41 (6), 82 (6), 97 (6), +7 more |
| 78897 | 345 (89..450) | 244 | 68 | 57 (34), 72 (32), 154 (32), 49 (28), 134 (28), 61 (24), 45 (21), 97 (17), 95 (7), 62 (6), 130 (4), 48 (2), +6 more |
| 78899 | 365 (91..455) | 263 | 67 | 57 (51), 72 (41), 49 (35), 61 (30), 154 (30), 134 (20), 97 (16), 45 (10), 82 (8), 62 (7), 70 (6), 95 (5), +3 more |
| 79097 | 366 (94..461) | 246 | 77 | 62 (39), 49 (34), 57 (32), 154 (19), 70 (18), 45 (16), 134 (14), 97 (13), 72 (10), 95 (8), 130 (8), 82 (7), +7 more |
| 79098 | 360 (97..467) | 273 | 60 | 62 (68), 70 (35), 49 (35), 110 (33), 45 (24), 61 (15), 57 (13), 154 (11), 50 (9), 64 (6), 134 (6), 82 (5), +4 more |
| 79102 | 371 (98..477) | 270 | 71 | 49 (74), 70 (48), 154 (33), 110 (17), 62 (14), 72 (13), 45 (12), 61 (12), 97 (11), 134 (10), 57 (8), 50 (6), +4 more |
| 79103 | 380 (99..481) | 262 | 80 | 97 (65), 70 (50), 49 (42), 134 (35), 62 (12), 64 (9), 50 (7), 72 (7), 154 (7), 110 (7), 45 (6), 57 (5), +4 more |
| 79105 | 379 (101..484) | 272 | 81 | 97 (57), 45 (46), 70 (42), 64 (29), 49 (22), 110 (17), 62 (15), 154 (10), 134 (9), 74 (6), 50 (5), 48 (4), +5 more |
| 79108 | 385 (104..492) | 283 | 73 | 70 (83), 64 (36), 74 (34), 45 (30), 97 (24), 62 (19), 50 (15), 110 (13), 49 (10), 95 (6), 72 (4), 84 (4), +3 more |
| 79110 | 388 (106..497) | 266 | 76 | 45 (54), 70 (34), 74 (30), 86 (30), 48 (24), 50 (23), 97 (20), 64 (15), 84 (10), 80 (8), 95 (6), 71 (3), +4 more |
| 79111 | 386 (109..500) | 272 | 75 | 62 (63), 48 (35), 86 (33), 50 (32), 74 (25), 45 (17), 64 (15), 80 (14), 72 (8), 71 (7), 84 (7), 70 (6), +5 more |
| 79115 | 421 (111..531) | 284 | 89 | 48 (42), 74 (39), 86 (37), 152 (30), 50 (28), 80 (26), 61 (18), 199 (12), 72 (11), 45 (9), 110 (9), 71 (7), +4 more |
| 79116 | 411 (114..530) | 285 | 85 | 80 (60), 86 (39), 48 (36), 50 (35), 152 (27), 62 (16), 61 (15), 199 (11), 74 (9), 72 (9), 64 (7), 84 (5), +5 more |
| 79122 | 404 (118..532) | 283 | 82 | 48 (70), 50 (45), 80 (33), 110 (29), 86 (20), 45 (20), 62 (18), 152 (18), 74 (10), 72 (10), 71 (3), 95 (2), +3 more |
| 79132 | 391 (120..515) | 267 | 88 | 199 (46), 74 (35), 80 (35), 86 (26), 48 (24), 72 (21), 71 (14), 64 (14), 152 (14), 62 (12), 45 (10), 50 (5), +3 more |
| 79128 | 402 (124..527) | 286 | 79 | 80 (64), 152 (41), 74 (26), 45 (24), 48 (23), 61 (23), 71 (20), 199 (20), 64 (10), 110 (9), 72 (7), 50 (7), +3 more |
| 79134 | 407 (127..533) | 287 | 80 | 80 (63), 74 (58), 61 (34), 152 (32), 48 (29), 50 (14), 86 (11), 71 (9), 62 (9), 190 (9), 110 (8), 45 (5), +3 more |
| 79135 | 409 (129..542) | 272 | 84 | 61 (65), 71 (43), 80 (40), 86 (26), 110 (17), 74 (16), 50 (16), 152 (16), 64 (12), 48 (8), 95 (5), 190 (5), +1 more |
| 79139 | 406 (132..537) | 276 | 84 | 190 (73), 48 (47), 110 (37), 74 (28), 86 (27), 71 (17), 50 (16), 62 (13), 61 (12), 95 (5), 80 (1) |
| 79136 | 393 (136..538) | 267 | 77 | 71 (62), 50 (61), 86 (39), 190 (30), 74 (19), 110 (19), 61 (18), 80 (10), 48 (7), 199 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 6/275/567; tracks with internal gaps: 16; total internal gaps: 38; longest internal gap: 1; tracks ending in coasting: 13 (trailing rows total 26)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..433 | 430 | 314 | 306 | 8 | 7 | 1 | 1 | 78911 |
| 41 | 80..241 | 162 | 118 | 114 | 4 | 0 | 0 | 4 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 82..496 | 415 | 357 | 356 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 48 | 86..529 | 444 | 375 | 373 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 88..460 | 373 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 50 | 89..485 | 397 | 340 | 336 | 4 | 4 | 1 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 97..454 | 358 | 296 | 296 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 100..542 | 443 | 373 | 372 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 62 | 102..542 | 441 | 348 | 345 | 3 | 2 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 106..297 | 192 | 177 | 174 | 3 | 2 | 1 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 70 | 108..492 | 385 | 326 | 323 | 3 | 3 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 71 | 108..347 | 240 | 190 | 187 | 3 | 2 | 1 | 1 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 108..439 | 332 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 74 | 116..536 | 421 | 336 | 335 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 117..190 | 74 | 60 | 58 | 2 | 0 | 0 | 2 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 77 | 117..264 | 148 | 119 | 116 | 3 | 0 | 0 | 3 | 78896, 78969, 78971, 79037, 79045 |
| 80 | 125..533 | 409 | 354 | 354 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 82 | 137..429 | 293 | 216 | 215 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79116, 79134 |
| 84 | 137..210 | 74 | 49 | 44 | 5 | 0 | 0 | 5 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 86 | 144..523 | 380 | 295 | 292 | 3 | 1 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 95 | 177..287 | 111 | 96 | 92 | 4 | 2 | 1 | 2 | 78897, 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 97 | 177..450 | 274 | 233 | 233 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 110 | 207..481 | 275 | 232 | 232 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 130 | 250..352 | 103 | 71 | 69 | 2 | 0 | 0 | 2 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 134 | 256..484 | 229 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 152 | 306..531 | 226 | 178 | 178 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 154 | 309..479 | 171 | 149 | 147 | 2 | 1 | 1 | 1 | 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103, 79105 |
| 155 | 309..444 | 136 | 107 | 107 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 186 | 390..395 | 6 | 6 | 5 | 1 | 0 | 0 | 1 | 78969 |
| 190 | 393..537 | 145 | 118 | 118 | 0 | 0 | 0 | 0 | 79122, 79134, 79135, 79136, 79139 |
| 199 | 404..538 | 135 | 92 | 91 | 1 | 1 | 1 | 0 | 79115, 79116, 79128, 79132, 79136 |
| 215 | 441..1007 | 567 | 398 | 391 | 7 | 7 | 1 | 0 | 78911 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7054; unmatched reference entries: 3088; unmatched candidate entries: 64
- identity switches: 1628; fragmentation (coverage interruptions): 2054; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 48 -> 49 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 48 -> 49 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 49 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 48 -> 49 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 50 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 49 -> 50 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 48 -> 49 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 49 -> 50 at (2107, 3033), 2 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 2 frames after previous cover
- f97: ref 79045: 50 -> 57 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 50 -> 57 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 48 -> 49 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 50 -> 57 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 48 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 57 -> 61 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 49 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 57 -> 45 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 49 -> 61 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 50 -> 57 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 45 -> 57 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 57 -> 61 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 61 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 45 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 62 -> 61 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 45 -> 62 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 57 -> 50 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 50 -> 48 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 61 -> 57 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 61 -> 62 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 62 -> 61 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 48 -> 50 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 57 -> 62 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 62 -> 61 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 61 -> 64 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 49 -> 48 at (2110, 3022.5), 6 frames after previous cover
- f108: ref 78899: 57 -> 70 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 61 -> 57 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 61 -> 64 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 64 -> 61 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79098: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 48 -> 72 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 70 -> 62 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 57 -> 61 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 61 -> 57 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 50 -> 70 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 48 -> 50 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 49 -> 48 at (2101.5, 3024.5), 4 frames after previous cover
- f111: ref 78897: 62 -> 64 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 62 -> 57 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 45 -> 41 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 64 -> 45 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 70 -> 62 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 50 -> 70 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 48 -> 50 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 49 -> 72 at (2113.5, 3026), 1 frames after previous cover
- ... 1568 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 697 | 210 | 215 (391), 1 (306) |
| 78896 | 350 (76..429) | 242 | 75 | 82 (120), 77 (84), 41 (29), 155 (9) |
| 78969 | 352 (80..434) | 248 | 66 | 130 (45), 82 (42), 41 (34), 72 (24), 57 (22), 76 (20), 45 (19), 155 (19), 77 (10), 61 (7), 186 (5), 154 (1) |
| 78971 | 352 (84..439) | 236 | 72 | 155 (49), 57 (30), 134 (26), 72 (21), 41 (18), 76 (16), 77 (14), 45 (12), 61 (12), 82 (12), 62 (11), 95 (8), +2 more |
| 79045 | 355 (84..443) | 235 | 79 | 61 (43), 134 (34), 57 (33), 72 (33), 41 (26), 155 (23), 45 (10), 76 (10), 77 (7), 49 (3), 62 (3), 82 (3), +4 more |
| 79037 | 355 (86..445) | 238 | 76 | 57 (65), 61 (33), 134 (25), 49 (23), 72 (18), 95 (14), 76 (9), 155 (7), 45 (6), 41 (6), 82 (6), 97 (6), +7 more |
| 78897 | 345 (89..450) | 244 | 68 | 57 (34), 72 (32), 154 (32), 49 (28), 134 (28), 61 (24), 45 (21), 97 (17), 95 (7), 62 (6), 130 (4), 48 (2), +6 more |
| 78899 | 365 (91..455) | 263 | 67 | 57 (51), 72 (41), 49 (35), 61 (30), 154 (30), 134 (20), 97 (16), 45 (10), 82 (8), 62 (7), 70 (6), 95 (5), +3 more |
| 79097 | 366 (94..461) | 246 | 77 | 62 (39), 49 (34), 57 (32), 154 (19), 70 (18), 45 (16), 134 (14), 97 (13), 72 (10), 95 (8), 130 (8), 82 (7), +7 more |
| 79098 | 360 (97..467) | 273 | 60 | 62 (68), 70 (35), 49 (35), 110 (33), 45 (24), 61 (15), 57 (13), 154 (11), 50 (9), 64 (6), 134 (6), 82 (5), +4 more |
| 79102 | 371 (98..477) | 270 | 71 | 49 (74), 70 (48), 154 (33), 110 (17), 62 (14), 72 (13), 45 (12), 61 (12), 97 (11), 134 (10), 57 (8), 50 (6), +4 more |
| 79103 | 380 (99..481) | 262 | 80 | 97 (65), 70 (50), 49 (42), 134 (35), 62 (12), 64 (9), 50 (7), 72 (7), 154 (7), 110 (7), 45 (6), 57 (5), +4 more |
| 79105 | 379 (101..484) | 272 | 81 | 97 (57), 45 (46), 70 (42), 64 (29), 49 (22), 110 (17), 62 (15), 154 (10), 134 (9), 74 (6), 50 (5), 48 (4), +5 more |
| 79108 | 385 (104..492) | 283 | 73 | 70 (83), 64 (36), 74 (34), 45 (30), 97 (24), 62 (19), 50 (15), 110 (13), 49 (10), 95 (6), 72 (4), 84 (4), +3 more |
| 79110 | 388 (106..497) | 266 | 76 | 45 (54), 70 (34), 74 (30), 86 (30), 48 (24), 50 (23), 97 (20), 64 (15), 84 (10), 80 (8), 95 (6), 71 (3), +4 more |
| 79111 | 386 (109..500) | 272 | 75 | 62 (63), 48 (35), 86 (33), 50 (32), 74 (25), 45 (17), 64 (15), 80 (14), 72 (8), 71 (7), 84 (7), 70 (6), +5 more |
| 79115 | 421 (111..531) | 284 | 89 | 48 (42), 74 (39), 86 (37), 152 (30), 50 (28), 80 (26), 61 (18), 199 (12), 72 (11), 45 (9), 110 (9), 71 (7), +4 more |
| 79116 | 411 (114..530) | 285 | 85 | 80 (60), 86 (39), 48 (36), 50 (35), 152 (27), 62 (16), 61 (15), 199 (11), 74 (9), 72 (9), 64 (7), 84 (5), +5 more |
| 79122 | 404 (118..532) | 283 | 82 | 48 (70), 50 (45), 80 (33), 110 (29), 86 (20), 45 (20), 62 (18), 152 (18), 74 (10), 72 (10), 71 (3), 95 (2), +3 more |
| 79132 | 391 (120..515) | 267 | 88 | 199 (46), 74 (35), 80 (35), 86 (26), 48 (24), 72 (21), 71 (14), 64 (14), 152 (14), 62 (12), 45 (10), 50 (5), +3 more |
| 79128 | 402 (124..527) | 286 | 79 | 80 (64), 152 (41), 74 (26), 45 (24), 48 (23), 61 (23), 71 (20), 199 (20), 64 (10), 110 (9), 72 (7), 50 (7), +3 more |
| 79134 | 407 (127..533) | 287 | 80 | 80 (63), 74 (58), 61 (34), 152 (32), 48 (29), 50 (14), 86 (11), 71 (9), 62 (9), 190 (9), 110 (8), 45 (5), +3 more |
| 79135 | 409 (129..542) | 272 | 84 | 61 (65), 71 (43), 80 (40), 86 (26), 110 (17), 74 (16), 50 (16), 152 (16), 64 (12), 48 (8), 95 (5), 190 (5), +1 more |
| 79139 | 406 (132..537) | 276 | 84 | 190 (73), 48 (47), 110 (37), 74 (28), 86 (27), 71 (17), 50 (16), 62 (13), 61 (12), 95 (5), 80 (1) |
| 79136 | 393 (136..538) | 267 | 77 | 71 (62), 50 (61), 86 (39), 190 (30), 74 (19), 110 (19), 61 (18), 80 (10), 48 (7), 199 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 6/275/567; tracks with internal gaps: 16; total internal gaps: 38; longest internal gap: 1; tracks ending in coasting: 13 (trailing rows total 26)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..433 | 430 | 314 | 306 | 8 | 7 | 1 | 1 | 78911 |
| 41 | 80..241 | 162 | 118 | 114 | 4 | 0 | 0 | 4 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 82..496 | 415 | 357 | 356 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 48 | 86..529 | 444 | 375 | 373 | 2 | 2 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 88..460 | 373 | 310 | 310 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 50 | 89..485 | 397 | 340 | 336 | 4 | 4 | 1 | 0 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 97..454 | 358 | 296 | 296 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 100..542 | 443 | 373 | 372 | 1 | 1 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 62 | 102..542 | 441 | 348 | 345 | 3 | 2 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 106..297 | 192 | 177 | 174 | 3 | 2 | 1 | 1 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 70 | 108..492 | 385 | 326 | 323 | 3 | 3 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 71 | 108..347 | 240 | 190 | 187 | 3 | 2 | 1 | 1 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 108..439 | 332 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 74 | 116..536 | 421 | 336 | 335 | 1 | 1 | 1 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 117..190 | 74 | 60 | 58 | 2 | 0 | 0 | 2 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 77 | 117..264 | 148 | 119 | 116 | 3 | 0 | 0 | 3 | 78896, 78969, 78971, 79037, 79045 |
| 80 | 125..533 | 409 | 354 | 354 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 82 | 137..429 | 293 | 216 | 215 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79116, 79134 |
| 84 | 137..210 | 74 | 49 | 44 | 5 | 0 | 0 | 5 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 86 | 144..523 | 380 | 295 | 292 | 3 | 1 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 95 | 177..287 | 111 | 96 | 92 | 4 | 2 | 1 | 2 | 78897, 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 97 | 177..450 | 274 | 233 | 233 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 110 | 207..481 | 275 | 232 | 232 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 130 | 250..352 | 103 | 71 | 69 | 2 | 0 | 0 | 2 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 134 | 256..484 | 229 | 207 | 207 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 152 | 306..531 | 226 | 178 | 178 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 154 | 309..479 | 171 | 149 | 147 | 2 | 1 | 1 | 1 | 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103, 79105 |
| 155 | 309..444 | 136 | 107 | 107 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 186 | 390..395 | 6 | 6 | 5 | 1 | 0 | 0 | 1 | 78969 |
| 190 | 393..537 | 145 | 118 | 118 | 0 | 0 | 0 | 0 | 79122, 79134, 79135, 79136, 79139 |
| 199 | 404..538 | 135 | 92 | 91 | 1 | 1 | 1 | 0 | 79115, 79116, 79128, 79132, 79136 |
| 215 | 441..1007 | 567 | 398 | 391 | 7 | 7 | 1 | 0 | 78911 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8204; unmatched reference entries: 1938; unmatched candidate entries: 1485
- identity switches: 1631; fragmentation (coverage interruptions): 1281; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 48 -> 49 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 48 -> 49 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 49 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 48 -> 49 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 50 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 49 -> 50 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 48 -> 49 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 49 -> 50 at (2107, 3033), 1 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 1 frames after previous cover
- f97: ref 79045: 50 -> 57 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 50 -> 57 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 48 -> 49 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 50 -> 57 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 48 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 57 -> 61 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 49 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 57 -> 45 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 49 -> 61 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 50 -> 57 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 45 -> 57 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 57 -> 61 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 61 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 45 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 62 -> 61 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 45 -> 62 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 57 -> 50 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 50 -> 48 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 61 -> 57 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 61 -> 62 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 62 -> 61 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 48 -> 50 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 57 -> 62 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 62 -> 61 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 61 -> 64 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 49 -> 48 at (2110, 3022.5), 5 frames after previous cover
- f108: ref 78899: 57 -> 70 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 61 -> 57 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 61 -> 64 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 64 -> 61 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79098: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 48 -> 72 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 70 -> 62 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 57 -> 61 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 61 -> 57 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 50 -> 70 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 48 -> 50 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 49 -> 48 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 62 -> 64 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 62 -> 57 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 45 -> 41 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 64 -> 45 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 70 -> 62 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 50 -> 70 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 48 -> 50 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 49 -> 72 at (2113.5, 3026), 1 frames after previous cover
- ... 1571 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 946 | 41 | 215 (531), 1 (415) |
| 78896 | 350 (76..429) | 291 | 41 | 82 (148), 77 (100), 41 (34), 155 (9) |
| 78969 | 352 (80..434) | 285 | 39 | 130 (54), 82 (48), 41 (37), 57 (29), 72 (27), 76 (25), 155 (22), 45 (21), 77 (9), 61 (7), 186 (5), 154 (1) |
| 78971 | 352 (84..439) | 263 | 56 | 155 (54), 57 (35), 134 (27), 72 (23), 41 (20), 77 (17), 76 (17), 82 (16), 62 (13), 45 (12), 61 (12), 95 (9), +2 more |
| 79045 | 355 (84..443) | 270 | 59 | 61 (47), 72 (45), 57 (37), 134 (36), 41 (31), 155 (28), 45 (10), 76 (10), 77 (8), 49 (4), 62 (3), 130 (3), +5 more |
| 79037 | 355 (86..445) | 273 | 58 | 57 (80), 61 (36), 134 (27), 49 (25), 72 (19), 95 (15), 76 (10), 155 (9), 41 (8), 45 (7), 82 (7), 97 (7), +7 more |
| 78897 | 345 (89..450) | 274 | 47 | 57 (38), 72 (36), 49 (35), 154 (35), 134 (29), 61 (26), 45 (23), 97 (18), 95 (8), 62 (6), 130 (6), 48 (3), +7 more |
| 78899 | 365 (91..455) | 291 | 45 | 57 (59), 72 (47), 49 (37), 154 (34), 61 (32), 134 (22), 97 (18), 45 (11), 82 (8), 70 (7), 62 (7), 95 (5), +3 more |
| 79097 | 366 (94..461) | 280 | 58 | 62 (43), 49 (41), 57 (38), 154 (22), 70 (20), 45 (18), 97 (16), 134 (15), 72 (11), 130 (10), 95 (9), 82 (8), +7 more |
| 79098 | 360 (97..467) | 295 | 43 | 62 (74), 70 (39), 49 (38), 110 (37), 45 (26), 61 (18), 57 (13), 154 (11), 50 (9), 64 (6), 134 (6), 82 (5), +4 more |
| 79102 | 371 (98..477) | 296 | 56 | 49 (81), 70 (53), 154 (35), 110 (22), 62 (15), 72 (14), 45 (13), 61 (13), 97 (11), 134 (10), 57 (9), 48 (6), +4 more |
| 79103 | 380 (99..481) | 297 | 58 | 97 (77), 70 (56), 49 (46), 134 (42), 62 (14), 64 (9), 110 (8), 50 (7), 57 (7), 72 (7), 154 (7), 45 (6), +4 more |
| 79105 | 379 (101..484) | 304 | 56 | 97 (62), 45 (53), 70 (47), 64 (33), 49 (23), 62 (18), 110 (18), 134 (11), 154 (10), 50 (7), 74 (7), 48 (4), +5 more |
| 79108 | 385 (104..492) | 316 | 46 | 70 (100), 74 (37), 64 (36), 45 (32), 97 (24), 62 (21), 50 (17), 110 (16), 49 (12), 95 (7), 72 (5), 84 (4), +3 more |
| 79110 | 388 (106..497) | 305 | 50 | 45 (61), 70 (41), 86 (35), 74 (34), 50 (29), 97 (23), 48 (22), 64 (17), 84 (13), 80 (10), 95 (6), 49 (4), +4 more |
| 79111 | 386 (109..500) | 310 | 46 | 62 (79), 48 (42), 86 (37), 50 (35), 74 (26), 45 (17), 64 (16), 80 (14), 71 (9), 72 (9), 84 (7), 97 (6), +5 more |
| 79115 | 421 (111..531) | 326 | 58 | 74 (49), 48 (47), 86 (45), 152 (32), 50 (29), 80 (29), 61 (21), 199 (14), 72 (13), 45 (13), 110 (9), 71 (7), +4 more |
| 79116 | 411 (114..530) | 328 | 50 | 80 (65), 86 (44), 48 (42), 50 (41), 152 (34), 62 (21), 61 (18), 199 (14), 72 (10), 74 (9), 64 (7), 45 (6), +5 more |
| 79122 | 404 (118..532) | 326 | 56 | 48 (87), 50 (48), 110 (34), 80 (33), 86 (27), 152 (24), 45 (21), 62 (20), 74 (11), 72 (11), 71 (3), 95 (2), +3 more |
| 79132 | 391 (120..515) | 312 | 58 | 199 (55), 74 (46), 80 (44), 86 (28), 48 (25), 72 (22), 152 (19), 64 (17), 71 (15), 62 (12), 45 (12), 95 (5), +3 more |
| 79128 | 402 (124..527) | 320 | 56 | 80 (72), 152 (46), 45 (29), 74 (28), 61 (26), 48 (24), 199 (23), 71 (21), 64 (11), 72 (10), 110 (9), 50 (7), +3 more |
| 79134 | 407 (127..533) | 326 | 53 | 80 (73), 74 (65), 152 (42), 61 (37), 48 (31), 50 (15), 86 (12), 71 (10), 62 (10), 190 (10), 110 (8), 45 (7), +3 more |
| 79135 | 409 (129..542) | 323 | 52 | 61 (78), 71 (47), 80 (46), 86 (36), 74 (23), 50 (20), 152 (19), 110 (18), 64 (12), 48 (10), 190 (6), 95 (5), +1 more |
| 79139 | 406 (132..537) | 325 | 57 | 190 (86), 48 (55), 110 (43), 74 (35), 86 (30), 71 (20), 61 (18), 50 (16), 62 (13), 95 (8), 199 (1) |
| 79136 | 393 (136..538) | 322 | 42 | 71 (77), 50 (74), 86 (46), 190 (35), 74 (25), 61 (23), 110 (21), 80 (12), 48 (9) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 35/304/568; tracks with internal gaps: 31; total internal gaps: 343; longest internal gap: 25; tracks ending in coasting: 31 (trailing rows total 969)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..462 | 459 | 459 | 415 | 44 | 11 | 2 | 30 | 78911 |
| 41 | 80..270 | 191 | 191 | 131 | 60 | 8 | 2 | 51 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 82..525 | 444 | 444 | 398 | 46 | 14 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 48 | 86..558 | 473 | 473 | 425 | 48 | 16 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 88..489 | 402 | 402 | 348 | 54 | 19 | 2 | 32 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 50 | 89..514 | 426 | 426 | 378 | 48 | 13 | 4 | 28 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 97..483 | 387 | 387 | 348 | 39 | 13 | 3 | 22 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 100..571 | 472 | 472 | 425 | 47 | 14 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 62 | 102..571 | 470 | 470 | 390 | 80 | 11 | 25 | 39 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 106..326 | 221 | 221 | 186 | 35 | 5 | 1 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 70 | 108..521 | 414 | 414 | 370 | 44 | 11 | 3 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 71 | 108..376 | 269 | 269 | 214 | 55 | 12 | 5 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 108..468 | 361 | 361 | 318 | 43 | 13 | 6 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 74 | 116..565 | 450 | 450 | 395 | 55 | 19 | 4 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 117..219 | 103 | 103 | 64 | 39 | 2 | 1 | 37 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 77 | 117..293 | 177 | 177 | 135 | 42 | 6 | 2 | 35 | 78896, 78969, 78971, 79037, 79045 |
| 80 | 125..562 | 438 | 438 | 398 | 40 | 10 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 82 | 137..458 | 322 | 322 | 256 | 66 | 20 | 16 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79116, 79134 |
| 84 | 137..239 | 103 | 103 | 51 | 52 | 2 | 2 | 49 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 86 | 144..552 | 409 | 409 | 345 | 64 | 15 | 8 | 37 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 95 | 177..316 | 140 | 140 | 102 | 38 | 5 | 1 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 97 | 177..479 | 303 | 303 | 262 | 41 | 12 | 1 | 29 | 78897, 78899, 79037, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 110 | 207..510 | 304 | 304 | 261 | 43 | 14 | 1 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 130 | 250..381 | 132 | 132 | 84 | 48 | 7 | 2 | 38 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 134 | 256..513 | 258 | 258 | 225 | 33 | 4 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 152 | 306..560 | 255 | 255 | 216 | 39 | 8 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 154 | 309..508 | 200 | 200 | 160 | 40 | 9 | 2 | 30 | 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103, 79105 |
| 155 | 309..473 | 165 | 165 | 123 | 42 | 10 | 3 | 28 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 186 | 390..424 | 35 | 35 | 5 | 30 | 0 | 0 | 30 | 78969 |
| 190 | 393..566 | 174 | 174 | 138 | 36 | 7 | 2 | 28 | 79122, 79134, 79135, 79136, 79139 |
| 199 | 404..567 | 164 | 164 | 107 | 57 | 4 | 13 | 30 | 79115, 79116, 79128, 79132, 79139 |
| 215 | 441..1008 | 568 | 568 | 531 | 37 | 29 | 3 | 0 | 78911 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8204; unmatched reference entries: 1938; unmatched candidate entries: 1485
- identity switches: 1631; fragmentation (coverage interruptions): 1281; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79045: 48 -> 49 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 48 -> 49 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 79045: 49 -> 50 at (2116.5, 3034), 3 frames after previous cover
- f92: ref 78897: 48 -> 49 at (2136.5, 3032), 1 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 50 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 49 -> 50 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f94: ref 78899: 48 -> 49 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 78897: 49 -> 50 at (2107, 3033), 1 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 1 frames after previous cover
- f97: ref 79045: 50 -> 57 at (2081.5, 3032), 3 frames after previous cover
- f98: ref 79037: 50 -> 57 at (2087, 3034), 2 frames after previous cover
- f98: ref 79097: 48 -> 49 at (2129, 3028), 1 frames after previous cover
- f99: ref 78897: 50 -> 57 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79098: 48 -> 50 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79045: 57 -> 61 at (2061, 3032.5), 3 frames after previous cover
- f100: ref 79097: 49 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f101: ref 78897: 57 -> 45 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 49 -> 61 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79097: 50 -> 57 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 45 -> 57 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 57 -> 61 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 61 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 45 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 78971: 62 -> 61 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79045: 45 -> 62 at (2042.5, 3033.5), 1 frames after previous cover
- f103: ref 79097: 57 -> 50 at (2100, 3028.5), 2 frames after previous cover
- f103: ref 79098: 50 -> 48 at (2113.5, 3027), 1 frames after previous cover
- f104: ref 78899: 61 -> 57 at (2079.5, 3030.5), 3 frames after previous cover
- f104: ref 79037: 61 -> 62 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 62 -> 61 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 48 -> 50 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 78897: 57 -> 62 at (2058, 3033), 2 frames after previous cover
- f105: ref 79037: 62 -> 61 at (2044.5, 3034), 1 frames after previous cover
- f106: ref 79045: 61 -> 64 at (2023.5, 3033.5), 2 frames after previous cover
- f107: ref 79103: 49 -> 48 at (2110, 3022.5), 5 frames after previous cover
- f108: ref 78899: 57 -> 70 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 61 -> 57 at (2003.5, 3034.5), 5 frames after previous cover
- f108: ref 79037: 61 -> 64 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 64 -> 61 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79098: 50 -> 48 at (2084.5, 3028.5), 1 frames after previous cover
- f108: ref 79102: 48 -> 72 at (2096.5, 3027.5), 2 frames after previous cover
- f109: ref 78899: 70 -> 62 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 57 -> 61 at (1996.5, 3034.5), 1 frames after previous cover
- f109: ref 79045: 61 -> 57 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 50 -> 70 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 48 -> 50 at (2077.5, 3029.5), 1 frames after previous cover
- f110: ref 79105: 49 -> 48 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 62 -> 64 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 78899: 62 -> 57 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 45 -> 41 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 79037: 64 -> 45 at (2007.5, 3035), 1 frames after previous cover
- f111: ref 79097: 70 -> 62 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 50 -> 70 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79103: 48 -> 50 at (2087.5, 3023.5), 2 frames after previous cover
- f111: ref 79108: 49 -> 72 at (2113.5, 3026), 1 frames after previous cover
- ... 1571 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 946 | 41 | 215 (531), 1 (415) |
| 78896 | 350 (76..429) | 291 | 41 | 82 (148), 77 (100), 41 (34), 155 (9) |
| 78969 | 352 (80..434) | 285 | 39 | 130 (54), 82 (48), 41 (37), 57 (29), 72 (27), 76 (25), 155 (22), 45 (21), 77 (9), 61 (7), 186 (5), 154 (1) |
| 78971 | 352 (84..439) | 263 | 56 | 155 (54), 57 (35), 134 (27), 72 (23), 41 (20), 77 (17), 76 (17), 82 (16), 62 (13), 45 (12), 61 (12), 95 (9), +2 more |
| 79045 | 355 (84..443) | 270 | 59 | 61 (47), 72 (45), 57 (37), 134 (36), 41 (31), 155 (28), 45 (10), 76 (10), 77 (8), 49 (4), 62 (3), 130 (3), +5 more |
| 79037 | 355 (86..445) | 273 | 58 | 57 (80), 61 (36), 134 (27), 49 (25), 72 (19), 95 (15), 76 (10), 155 (9), 41 (8), 45 (7), 82 (7), 97 (7), +7 more |
| 78897 | 345 (89..450) | 274 | 47 | 57 (38), 72 (36), 49 (35), 154 (35), 134 (29), 61 (26), 45 (23), 97 (18), 95 (8), 62 (6), 130 (6), 48 (3), +7 more |
| 78899 | 365 (91..455) | 291 | 45 | 57 (59), 72 (47), 49 (37), 154 (34), 61 (32), 134 (22), 97 (18), 45 (11), 82 (8), 70 (7), 62 (7), 95 (5), +3 more |
| 79097 | 366 (94..461) | 280 | 58 | 62 (43), 49 (41), 57 (38), 154 (22), 70 (20), 45 (18), 97 (16), 134 (15), 72 (11), 130 (10), 95 (9), 82 (8), +7 more |
| 79098 | 360 (97..467) | 295 | 43 | 62 (74), 70 (39), 49 (38), 110 (37), 45 (26), 61 (18), 57 (13), 154 (11), 50 (9), 64 (6), 134 (6), 82 (5), +4 more |
| 79102 | 371 (98..477) | 296 | 56 | 49 (81), 70 (53), 154 (35), 110 (22), 62 (15), 72 (14), 45 (13), 61 (13), 97 (11), 134 (10), 57 (9), 48 (6), +4 more |
| 79103 | 380 (99..481) | 297 | 58 | 97 (77), 70 (56), 49 (46), 134 (42), 62 (14), 64 (9), 110 (8), 50 (7), 57 (7), 72 (7), 154 (7), 45 (6), +4 more |
| 79105 | 379 (101..484) | 304 | 56 | 97 (62), 45 (53), 70 (47), 64 (33), 49 (23), 62 (18), 110 (18), 134 (11), 154 (10), 50 (7), 74 (7), 48 (4), +5 more |
| 79108 | 385 (104..492) | 316 | 46 | 70 (100), 74 (37), 64 (36), 45 (32), 97 (24), 62 (21), 50 (17), 110 (16), 49 (12), 95 (7), 72 (5), 84 (4), +3 more |
| 79110 | 388 (106..497) | 305 | 50 | 45 (61), 70 (41), 86 (35), 74 (34), 50 (29), 97 (23), 48 (22), 64 (17), 84 (13), 80 (10), 95 (6), 49 (4), +4 more |
| 79111 | 386 (109..500) | 310 | 46 | 62 (79), 48 (42), 86 (37), 50 (35), 74 (26), 45 (17), 64 (16), 80 (14), 71 (9), 72 (9), 84 (7), 97 (6), +5 more |
| 79115 | 421 (111..531) | 326 | 58 | 74 (49), 48 (47), 86 (45), 152 (32), 50 (29), 80 (29), 61 (21), 199 (14), 72 (13), 45 (13), 110 (9), 71 (7), +4 more |
| 79116 | 411 (114..530) | 328 | 50 | 80 (65), 86 (44), 48 (42), 50 (41), 152 (34), 62 (21), 61 (18), 199 (14), 72 (10), 74 (9), 64 (7), 45 (6), +5 more |
| 79122 | 404 (118..532) | 326 | 56 | 48 (87), 50 (48), 110 (34), 80 (33), 86 (27), 152 (24), 45 (21), 62 (20), 74 (11), 72 (11), 71 (3), 95 (2), +3 more |
| 79132 | 391 (120..515) | 312 | 58 | 199 (55), 74 (46), 80 (44), 86 (28), 48 (25), 72 (22), 152 (19), 64 (17), 71 (15), 62 (12), 45 (12), 95 (5), +3 more |
| 79128 | 402 (124..527) | 320 | 56 | 80 (72), 152 (46), 45 (29), 74 (28), 61 (26), 48 (24), 199 (23), 71 (21), 64 (11), 72 (10), 110 (9), 50 (7), +3 more |
| 79134 | 407 (127..533) | 326 | 53 | 80 (73), 74 (65), 152 (42), 61 (37), 48 (31), 50 (15), 86 (12), 71 (10), 62 (10), 190 (10), 110 (8), 45 (7), +3 more |
| 79135 | 409 (129..542) | 323 | 52 | 61 (78), 71 (47), 80 (46), 86 (36), 74 (23), 50 (20), 152 (19), 110 (18), 64 (12), 48 (10), 190 (6), 95 (5), +1 more |
| 79139 | 406 (132..537) | 325 | 57 | 190 (86), 48 (55), 110 (43), 74 (35), 86 (30), 71 (20), 61 (18), 50 (16), 62 (13), 95 (8), 199 (1) |
| 79136 | 393 (136..538) | 322 | 42 | 71 (77), 50 (74), 86 (46), 190 (35), 74 (25), 61 (23), 110 (21), 80 (12), 48 (9) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 35/304/568; tracks with internal gaps: 31; total internal gaps: 343; longest internal gap: 25; tracks ending in coasting: 31 (trailing rows total 969)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..462 | 459 | 459 | 415 | 44 | 11 | 2 | 30 | 78911 |
| 41 | 80..270 | 191 | 191 | 131 | 60 | 8 | 2 | 51 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 45 | 82..525 | 444 | 444 | 398 | 46 | 14 | 3 | 28 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 48 | 86..558 | 473 | 473 | 425 | 48 | 16 | 3 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 49 | 88..489 | 402 | 402 | 348 | 54 | 19 | 2 | 32 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 50 | 89..514 | 426 | 426 | 378 | 48 | 13 | 4 | 28 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 57 | 97..483 | 387 | 387 | 348 | 39 | 13 | 3 | 22 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 100..571 | 472 | 472 | 425 | 47 | 14 | 4 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 62 | 102..571 | 470 | 470 | 390 | 80 | 11 | 25 | 39 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 64 | 106..326 | 221 | 221 | 186 | 35 | 5 | 1 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 70 | 108..521 | 414 | 414 | 370 | 44 | 11 | 3 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 71 | 108..376 | 269 | 269 | 214 | 55 | 12 | 5 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 72 | 108..468 | 361 | 361 | 318 | 43 | 13 | 6 | 25 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 74 | 116..565 | 450 | 450 | 395 | 55 | 19 | 4 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 76 | 117..219 | 103 | 103 | 64 | 39 | 2 | 1 | 37 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 77 | 117..293 | 177 | 177 | 135 | 42 | 6 | 2 | 35 | 78896, 78969, 78971, 79037, 79045 |
| 80 | 125..562 | 438 | 438 | 398 | 40 | 10 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136 |
| 82 | 137..458 | 322 | 322 | 256 | 66 | 20 | 16 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79111, 79116, 79134 |
| 84 | 137..239 | 103 | 103 | 51 | 52 | 2 | 2 | 49 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 86 | 144..552 | 409 | 409 | 345 | 64 | 15 | 8 | 37 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 95 | 177..316 | 140 | 140 | 102 | 38 | 5 | 1 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 97 | 177..479 | 303 | 303 | 262 | 41 | 12 | 1 | 29 | 78897, 78899, 79037, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 110 | 207..510 | 304 | 304 | 261 | 43 | 14 | 1 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 130 | 250..381 | 132 | 132 | 84 | 48 | 7 | 2 | 38 | 78897, 78969, 78971, 79037, 79045, 79097 |
| 134 | 256..513 | 258 | 258 | 225 | 33 | 4 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 152 | 306..560 | 255 | 255 | 216 | 39 | 8 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 154 | 309..508 | 200 | 200 | 160 | 40 | 9 | 2 | 30 | 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79103, 79105 |
| 155 | 309..473 | 165 | 165 | 123 | 42 | 10 | 3 | 28 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 186 | 390..424 | 35 | 35 | 5 | 30 | 0 | 0 | 30 | 78969 |
| 190 | 393..566 | 174 | 174 | 138 | 36 | 7 | 2 | 28 | 79122, 79134, 79135, 79136, 79139 |
| 199 | 404..567 | 164 | 164 | 107 | 57 | 4 | 13 | 30 | 79115, 79116, 79128, 79132, 79139 |
| 215 | 441..1008 | 568 | 568 | 531 | 37 | 29 | 3 | 0 | 78911 |
