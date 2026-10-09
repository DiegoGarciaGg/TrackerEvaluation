# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=90d8fdd45c9a
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise3.0_fp0.5_seed3/tracks.csv sha256=7666f6601d9d1c7b
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise3.0_fp0.5_seed3.csv sha256=90d8fdd45c9ae385
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise3.0_fp0.5_seed3
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
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 0.118 | 0.043 | -0.006 | 2.39 | 0.113 | 1275 | 2421.0 |
| observations | none | 6 | 0.159 | 0.057 | 0.344 | 3.20 | 0.167 | 1651 | 2320.0 |
| observations | none | 8 | 0.181 | 0.065 | 0.468 | 3.59 | 0.188 | 1758 | 2077.0 |
| observations | none | 12 | 0.203 | 0.074 | 0.517 | 3.96 | 0.208 | 1631 | 1940.0 |
| observations | ignore | 4 | 0.118 | 0.043 | -0.006 | 2.39 | 0.113 | 1275 | 2421.0 |
| observations | ignore | 6 | 0.159 | 0.057 | 0.344 | 3.20 | 0.167 | 1651 | 2320.0 |
| observations | ignore | 8 | 0.181 | 0.065 | 0.468 | 3.59 | 0.188 | 1758 | 2077.0 |
| observations | ignore | 12 | 0.203 | 0.074 | 0.517 | 3.96 | 0.208 | 1631 | 1940.0 |
| updates | none | 4 | 0.120 | 0.048 | -0.212 | 2.40 | 0.108 | 1316 | 2457.0 |
| updates | none | 6 | 0.169 | 0.067 | 0.204 | 3.26 | 0.165 | 1680 | 2102.0 |
| updates | none | 8 | 0.199 | 0.079 | 0.384 | 3.75 | 0.195 | 1760 | 1627.0 |
| updates | none | 12 | 0.230 | 0.092 | 0.497 | 4.36 | 0.224 | 1609 | 1238.0 |
| updates | ignore | 4 | 0.120 | 0.048 | -0.212 | 2.40 | 0.108 | 1316 | 2457.0 |
| updates | ignore | 6 | 0.169 | 0.067 | 0.204 | 3.26 | 0.165 | 1680 | 2102.0 |
| updates | ignore | 8 | 0.199 | 0.079 | 0.384 | 3.75 | 0.195 | 1760 | 1627.0 |
| updates | ignore | 12 | 0.230 | 0.092 | 0.497 | 4.36 | 0.224 | 1609 | 1238.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 6808; unmatched reference entries: 3334; unmatched candidate entries: 301
- identity switches: 1758; fragmentation (coverage interruptions): 2124; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 48 -> 50 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 48 -> 49 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 48 -> 50 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 49 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 50 -> 49 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 48 -> 50 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 49 -> 57 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 50 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 49 -> 57 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 57 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 48 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 48 -> 61 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 49 -> 57 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 50 -> 49 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 61 -> 48 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 57 -> 49 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 49 -> 57 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 57 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 57 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 50 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 62 -> 57 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 57 -> 45 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 45 -> 62 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 50 -> 48 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 48 -> 50 at (2119, 3027), 3 frames after previous cover
- f106: ref 78897: 49 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 49 -> 65 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79037: 45 -> 62 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 62 -> 57 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79097: 48 -> 49 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 61 -> 50 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 57 -> 64 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 65 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 62 -> 65 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 57 -> 62 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 49 -> 48 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 49 -> 65 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 64 -> 41 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 48 -> 45 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 61 -> 49 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 50 -> 48 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 50 -> 61 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 57 -> 64 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 65 -> 62 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 62 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 61 -> 48 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 45 -> 62 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 62 -> 57 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 57 -> 62 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 61 -> 49 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 65 -> 57 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 45 -> 62 at (2034.5, 3030), 2 frames after previous cover
- ... 1698 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 672 | 218 | 221 (378), 1 (294) |
| 78896 | 350 (76..429) | 236 | 78 | 48 (64), 41 (60), 77 (38), 64 (23), 149 (22), 57 (20), 160 (9) |
| 78969 | 352 (80..434) | 236 | 71 | 41 (44), 57 (37), 48 (37), 149 (28), 195 (28), 75 (22), 160 (18), 45 (11), 64 (5), 161 (5), 77 (1) |
| 78971 | 352 (84..439) | 234 | 74 | 160 (54), 77 (30), 65 (28), 57 (21), 75 (21), 41 (14), 49 (11), 64 (11), 61 (11), 195 (8), 45 (6), 161 (6), +5 more |
| 79045 | 355 (84..443) | 231 | 77 | 77 (47), 89 (34), 57 (30), 65 (28), 160 (21), 64 (19), 75 (13), 49 (12), 161 (7), 48 (4), 140 (4), 62 (3), +4 more |
| 79037 | 355 (86..445) | 228 | 77 | 77 (49), 64 (28), 61 (27), 161 (27), 89 (26), 65 (16), 57 (15), 75 (10), 49 (9), 160 (6), 140 (5), 62 (4), +3 more |
| 78897 | 345 (89..450) | 232 | 70 | 77 (34), 161 (33), 64 (32), 61 (24), 57 (19), 89 (18), 75 (16), 65 (15), 81 (15), 50 (8), 49 (8), 48 (5), +2 more |
| 78899 | 365 (91..455) | 255 | 72 | 161 (35), 81 (35), 61 (34), 77 (31), 75 (27), 49 (23), 64 (23), 65 (15), 89 (12), 48 (9), 50 (8), 57 (3) |
| 79097 | 366 (94..461) | 243 | 81 | 75 (68), 48 (30), 45 (23), 81 (22), 77 (20), 89 (19), 65 (18), 49 (13), 50 (9), 64 (9), 61 (8), 62 (3), +1 more |
| 79098 | 360 (97..467) | 263 | 65 | 45 (68), 89 (36), 75 (33), 50 (27), 65 (20), 64 (18), 48 (16), 49 (14), 61 (12), 86 (10), 77 (5), 81 (3), +1 more |
| 79102 | 371 (98..477) | 257 | 74 | 86 (55), 89 (36), 75 (35), 70 (24), 81 (23), 50 (22), 64 (16), 45 (14), 61 (8), 48 (6), 62 (5), 65 (5), +3 more |
| 79103 | 380 (99..481) | 254 | 80 | 81 (41), 86 (40), 89 (39), 45 (23), 70 (21), 50 (18), 74 (18), 75 (10), 64 (9), 48 (8), 49 (7), 87 (6), +4 more |
| 79105 | 379 (101..484) | 264 | 85 | 81 (44), 74 (38), 86 (30), 45 (27), 50 (19), 64 (19), 75 (15), 70 (14), 87 (10), 62 (10), 49 (9), 57 (9), +5 more |
| 79108 | 385 (104..492) | 278 | 79 | 74 (49), 81 (44), 131 (33), 49 (25), 64 (24), 45 (21), 50 (17), 57 (14), 103 (13), 75 (12), 62 (8), 70 (7), +4 more |
| 79110 | 388 (106..497) | 255 | 76 | 64 (48), 131 (34), 45 (32), 103 (23), 74 (22), 87 (19), 75 (14), 62 (11), 70 (10), 49 (9), 50 (8), 81 (6), +5 more |
| 79111 | 386 (109..500) | 260 | 76 | 131 (64), 103 (44), 87 (22), 70 (21), 45 (20), 62 (17), 89 (16), 64 (14), 50 (9), 74 (7), 49 (7), 75 (4), +5 more |
| 79115 | 421 (111..531) | 271 | 89 | 57 (50), 131 (38), 87 (30), 132 (24), 70 (17), 186 (16), 45 (15), 62 (14), 207 (14), 49 (12), 103 (10), 81 (7), +5 more |
| 79116 | 411 (114..530) | 272 | 86 | 87 (42), 132 (31), 186 (29), 45 (18), 131 (18), 199 (17), 57 (15), 70 (13), 49 (13), 65 (13), 103 (12), 64 (12), +6 more |
| 79122 | 404 (118..532) | 271 | 85 | 132 (54), 70 (28), 87 (27), 103 (22), 45 (22), 49 (18), 57 (18), 207 (17), 62 (11), 74 (10), 81 (8), 131 (5), +8 more |
| 79132 | 391 (120..515) | 264 | 89 | 87 (61), 74 (35), 186 (31), 62 (25), 207 (19), 45 (13), 49 (12), 65 (11), 70 (10), 132 (10), 131 (9), 81 (7), +4 more |
| 79128 | 402 (124..527) | 274 | 86 | 87 (51), 132 (45), 103 (41), 62 (20), 186 (20), 65 (15), 70 (14), 91 (14), 57 (11), 74 (9), 45 (9), 131 (6), +6 more |
| 79134 | 407 (127..533) | 282 | 84 | 103 (55), 70 (44), 207 (36), 87 (24), 65 (18), 86 (14), 81 (14), 57 (14), 132 (13), 74 (11), 91 (11), 199 (9), +5 more |
| 79135 | 409 (129..542) | 266 | 83 | 103 (58), 70 (54), 86 (34), 57 (29), 189 (26), 74 (12), 132 (11), 87 (10), 186 (9), 65 (7), 91 (6), 62 (5), +3 more |
| 79139 | 406 (132..537) | 269 | 87 | 199 (45), 74 (43), 189 (42), 132 (35), 86 (34), 62 (15), 70 (14), 57 (14), 65 (8), 117 (5), 103 (5), 49 (4), +3 more |
| 79136 | 393 (136..538) | 241 | 82 | 189 (49), 86 (44), 74 (42), 199 (26), 70 (16), 65 (15), 49 (13), 57 (11), 62 (10), 132 (7), 103 (5), 186 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 14/292/567; tracks with internal gaps: 31; total internal gaps: 252; longest internal gap: 4; tracks ending in coasting: 16 (trailing rows total 34)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..433 | 430 | 314 | 294 | 20 | 18 | 2 | 1 | 78911 |
| 41 | 80..241 | 162 | 125 | 120 | 5 | 1 | 1 | 4 | 78896, 78969, 78971, 79045 |
| 45 | 82..484 | 403 | 346 | 329 | 17 | 16 | 1 | 1 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 86..352 | 267 | 208 | 192 | 16 | 10 | 4 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 49 | 88..347 | 260 | 231 | 227 | 4 | 3 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 89..287 | 199 | 168 | 152 | 16 | 12 | 2 | 2 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 57 | 97..537 | 441 | 363 | 350 | 13 | 11 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 100..264 | 165 | 143 | 134 | 9 | 6 | 1 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 62 | 102..297 | 196 | 181 | 177 | 4 | 3 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..496 | 391 | 340 | 326 | 14 | 13 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 106..455 | 350 | 258 | 246 | 12 | 7 | 1 | 5 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 108..485 | 378 | 321 | 307 | 14 | 14 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 116..492 | 377 | 317 | 309 | 8 | 8 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 75 | 116..479 | 364 | 313 | 304 | 9 | 8 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 77 | 117..429 | 313 | 267 | 258 | 9 | 9 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 81 | 125..460 | 336 | 292 | 279 | 13 | 13 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 86 | 137..481 | 345 | 289 | 280 | 9 | 8 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79134, 79135, 79136, 79139 |
| 87 | 137..523 | 387 | 315 | 303 | 12 | 10 | 1 | 2 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 89 | 137..450 | 314 | 284 | 277 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 91 | 144..219 | 76 | 42 | 37 | 5 | 2 | 1 | 3 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 103 | 177..542 | 366 | 307 | 293 | 14 | 13 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 207..220 | 14 | 9 | 7 | 2 | 0 | 0 | 2 | 79135, 79139 |
| 131 | 240..542 | 303 | 226 | 215 | 11 | 10 | 1 | 1 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 132 | 240..531 | 292 | 249 | 237 | 12 | 12 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 140 | 256..286 | 31 | 11 | 9 | 2 | 0 | 0 | 2 | 79037, 79045 |
| 149 | 284..395 | 112 | 55 | 52 | 3 | 0 | 0 | 3 | 78896, 78969, 78971 |
| 160 | 309..444 | 136 | 110 | 108 | 2 | 2 | 1 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 161 | 309..454 | 146 | 116 | 114 | 2 | 2 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 186 | 363..541 | 179 | 123 | 121 | 2 | 2 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 189 | 367..538 | 172 | 136 | 130 | 6 | 5 | 2 | 0 | 79122, 79134, 79135, 79136, 79139 |
| 195 | 390..439 | 50 | 37 | 36 | 1 | 1 | 1 | 0 | 78969, 78971 |
| 199 | 393..529 | 137 | 109 | 106 | 3 | 3 | 1 | 0 | 79116, 79122, 79128, 79134, 79136, 79139 |
| 207 | 404..532 | 129 | 106 | 101 | 5 | 5 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 221 | 441..1007 | 567 | 398 | 378 | 20 | 18 | 2 | 0 | 78911 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 6808; unmatched reference entries: 3334; unmatched candidate entries: 301
- identity switches: 1758; fragmentation (coverage interruptions): 2124; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 48 -> 50 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 48 -> 49 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 48 -> 50 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 49 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 50 -> 49 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 48 -> 50 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 49 -> 57 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 50 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 49 -> 57 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 57 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 48 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 48 -> 61 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 49 -> 57 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 50 -> 49 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 61 -> 48 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 57 -> 49 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 49 -> 57 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 57 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 57 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 50 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 62 -> 57 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 57 -> 45 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 45 -> 62 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 50 -> 48 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 48 -> 50 at (2119, 3027), 3 frames after previous cover
- f106: ref 78897: 49 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 49 -> 65 at (2067.5, 3030), 2 frames after previous cover
- f106: ref 79037: 45 -> 62 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 62 -> 57 at (2023.5, 3033.5), 2 frames after previous cover
- f106: ref 79097: 48 -> 49 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 61 -> 50 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 57 -> 64 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 65 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 62 -> 65 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 57 -> 62 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 49 -> 48 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 49 -> 65 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 64 -> 41 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 48 -> 45 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 61 -> 49 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 50 -> 48 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 50 -> 61 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 57 -> 64 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 65 -> 62 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 62 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 61 -> 48 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 45 -> 62 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 62 -> 57 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 57 -> 62 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 61 -> 49 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 65 -> 57 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 45 -> 62 at (2034.5, 3030), 2 frames after previous cover
- ... 1698 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 672 | 218 | 221 (378), 1 (294) |
| 78896 | 350 (76..429) | 236 | 78 | 48 (64), 41 (60), 77 (38), 64 (23), 149 (22), 57 (20), 160 (9) |
| 78969 | 352 (80..434) | 236 | 71 | 41 (44), 57 (37), 48 (37), 149 (28), 195 (28), 75 (22), 160 (18), 45 (11), 64 (5), 161 (5), 77 (1) |
| 78971 | 352 (84..439) | 234 | 74 | 160 (54), 77 (30), 65 (28), 57 (21), 75 (21), 41 (14), 49 (11), 64 (11), 61 (11), 195 (8), 45 (6), 161 (6), +5 more |
| 79045 | 355 (84..443) | 231 | 77 | 77 (47), 89 (34), 57 (30), 65 (28), 160 (21), 64 (19), 75 (13), 49 (12), 161 (7), 48 (4), 140 (4), 62 (3), +4 more |
| 79037 | 355 (86..445) | 228 | 77 | 77 (49), 64 (28), 61 (27), 161 (27), 89 (26), 65 (16), 57 (15), 75 (10), 49 (9), 160 (6), 140 (5), 62 (4), +3 more |
| 78897 | 345 (89..450) | 232 | 70 | 77 (34), 161 (33), 64 (32), 61 (24), 57 (19), 89 (18), 75 (16), 65 (15), 81 (15), 50 (8), 49 (8), 48 (5), +2 more |
| 78899 | 365 (91..455) | 255 | 72 | 161 (35), 81 (35), 61 (34), 77 (31), 75 (27), 49 (23), 64 (23), 65 (15), 89 (12), 48 (9), 50 (8), 57 (3) |
| 79097 | 366 (94..461) | 243 | 81 | 75 (68), 48 (30), 45 (23), 81 (22), 77 (20), 89 (19), 65 (18), 49 (13), 50 (9), 64 (9), 61 (8), 62 (3), +1 more |
| 79098 | 360 (97..467) | 263 | 65 | 45 (68), 89 (36), 75 (33), 50 (27), 65 (20), 64 (18), 48 (16), 49 (14), 61 (12), 86 (10), 77 (5), 81 (3), +1 more |
| 79102 | 371 (98..477) | 257 | 74 | 86 (55), 89 (36), 75 (35), 70 (24), 81 (23), 50 (22), 64 (16), 45 (14), 61 (8), 48 (6), 62 (5), 65 (5), +3 more |
| 79103 | 380 (99..481) | 254 | 80 | 81 (41), 86 (40), 89 (39), 45 (23), 70 (21), 50 (18), 74 (18), 75 (10), 64 (9), 48 (8), 49 (7), 87 (6), +4 more |
| 79105 | 379 (101..484) | 264 | 85 | 81 (44), 74 (38), 86 (30), 45 (27), 50 (19), 64 (19), 75 (15), 70 (14), 87 (10), 62 (10), 49 (9), 57 (9), +5 more |
| 79108 | 385 (104..492) | 278 | 79 | 74 (49), 81 (44), 131 (33), 49 (25), 64 (24), 45 (21), 50 (17), 57 (14), 103 (13), 75 (12), 62 (8), 70 (7), +4 more |
| 79110 | 388 (106..497) | 255 | 76 | 64 (48), 131 (34), 45 (32), 103 (23), 74 (22), 87 (19), 75 (14), 62 (11), 70 (10), 49 (9), 50 (8), 81 (6), +5 more |
| 79111 | 386 (109..500) | 260 | 76 | 131 (64), 103 (44), 87 (22), 70 (21), 45 (20), 62 (17), 89 (16), 64 (14), 50 (9), 74 (7), 49 (7), 75 (4), +5 more |
| 79115 | 421 (111..531) | 271 | 89 | 57 (50), 131 (38), 87 (30), 132 (24), 70 (17), 186 (16), 45 (15), 62 (14), 207 (14), 49 (12), 103 (10), 81 (7), +5 more |
| 79116 | 411 (114..530) | 272 | 86 | 87 (42), 132 (31), 186 (29), 45 (18), 131 (18), 199 (17), 57 (15), 70 (13), 49 (13), 65 (13), 103 (12), 64 (12), +6 more |
| 79122 | 404 (118..532) | 271 | 85 | 132 (54), 70 (28), 87 (27), 103 (22), 45 (22), 49 (18), 57 (18), 207 (17), 62 (11), 74 (10), 81 (8), 131 (5), +8 more |
| 79132 | 391 (120..515) | 264 | 89 | 87 (61), 74 (35), 186 (31), 62 (25), 207 (19), 45 (13), 49 (12), 65 (11), 70 (10), 132 (10), 131 (9), 81 (7), +4 more |
| 79128 | 402 (124..527) | 274 | 86 | 87 (51), 132 (45), 103 (41), 62 (20), 186 (20), 65 (15), 70 (14), 91 (14), 57 (11), 74 (9), 45 (9), 131 (6), +6 more |
| 79134 | 407 (127..533) | 282 | 84 | 103 (55), 70 (44), 207 (36), 87 (24), 65 (18), 86 (14), 81 (14), 57 (14), 132 (13), 74 (11), 91 (11), 199 (9), +5 more |
| 79135 | 409 (129..542) | 266 | 83 | 103 (58), 70 (54), 86 (34), 57 (29), 189 (26), 74 (12), 132 (11), 87 (10), 186 (9), 65 (7), 91 (6), 62 (5), +3 more |
| 79139 | 406 (132..537) | 269 | 87 | 199 (45), 74 (43), 189 (42), 132 (35), 86 (34), 62 (15), 70 (14), 57 (14), 65 (8), 117 (5), 103 (5), 49 (4), +3 more |
| 79136 | 393 (136..538) | 241 | 82 | 189 (49), 86 (44), 74 (42), 199 (26), 70 (16), 65 (15), 49 (13), 57 (11), 62 (10), 132 (7), 103 (5), 186 (3) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 14/292/567; tracks with internal gaps: 31; total internal gaps: 252; longest internal gap: 4; tracks ending in coasting: 16 (trailing rows total 34)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..433 | 430 | 314 | 294 | 20 | 18 | 2 | 1 | 78911 |
| 41 | 80..241 | 162 | 125 | 120 | 5 | 1 | 1 | 4 | 78896, 78969, 78971, 79045 |
| 45 | 82..484 | 403 | 346 | 329 | 17 | 16 | 1 | 1 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 86..352 | 267 | 208 | 192 | 16 | 10 | 4 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 49 | 88..347 | 260 | 231 | 227 | 4 | 3 | 1 | 1 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 89..287 | 199 | 168 | 152 | 16 | 12 | 2 | 2 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 57 | 97..537 | 441 | 363 | 350 | 13 | 11 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 100..264 | 165 | 143 | 134 | 9 | 6 | 1 | 3 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 62 | 102..297 | 196 | 181 | 177 | 4 | 3 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..496 | 391 | 340 | 326 | 14 | 13 | 2 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 106..455 | 350 | 258 | 246 | 12 | 7 | 1 | 5 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 108..485 | 378 | 321 | 307 | 14 | 14 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 116..492 | 377 | 317 | 309 | 8 | 8 | 1 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 75 | 116..479 | 364 | 313 | 304 | 9 | 8 | 1 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 77 | 117..429 | 313 | 267 | 258 | 9 | 9 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 81 | 125..460 | 336 | 292 | 279 | 13 | 13 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 86 | 137..481 | 345 | 289 | 280 | 9 | 8 | 2 | 0 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79134, 79135, 79136, 79139 |
| 87 | 137..523 | 387 | 315 | 303 | 12 | 10 | 1 | 2 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 89 | 137..450 | 314 | 284 | 277 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 91 | 144..219 | 76 | 42 | 37 | 5 | 2 | 1 | 3 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 103 | 177..542 | 366 | 307 | 293 | 14 | 13 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 207..220 | 14 | 9 | 7 | 2 | 0 | 0 | 2 | 79135, 79139 |
| 131 | 240..542 | 303 | 226 | 215 | 11 | 10 | 1 | 1 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 132 | 240..531 | 292 | 249 | 237 | 12 | 12 | 1 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 140 | 256..286 | 31 | 11 | 9 | 2 | 0 | 0 | 2 | 79037, 79045 |
| 149 | 284..395 | 112 | 55 | 52 | 3 | 0 | 0 | 3 | 78896, 78969, 78971 |
| 160 | 309..444 | 136 | 110 | 108 | 2 | 2 | 1 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 161 | 309..454 | 146 | 116 | 114 | 2 | 2 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 186 | 363..541 | 179 | 123 | 121 | 2 | 2 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 189 | 367..538 | 172 | 136 | 130 | 6 | 5 | 2 | 0 | 79122, 79134, 79135, 79136, 79139 |
| 195 | 390..439 | 50 | 37 | 36 | 1 | 1 | 1 | 0 | 78969, 78971 |
| 199 | 393..529 | 137 | 109 | 106 | 3 | 3 | 1 | 0 | 79116, 79122, 79128, 79134, 79136, 79139 |
| 207 | 404..532 | 129 | 106 | 101 | 5 | 5 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 221 | 441..1007 | 567 | 398 | 378 | 20 | 18 | 2 | 0 | 78911 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7698; unmatched reference entries: 2444; unmatched candidate entries: 2048
- identity switches: 1760; fragmentation (coverage interruptions): 1573; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 48 -> 50 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 48 -> 49 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 48 -> 50 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 49 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 50 -> 49 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 48 -> 50 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 49 -> 57 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 50 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 49 -> 57 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 57 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 48 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 48 -> 61 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 49 -> 57 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 50 -> 49 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 61 -> 48 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 57 -> 49 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 49 -> 57 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 57 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 57 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 50 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 62 -> 57 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 57 -> 45 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 45 -> 62 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 50 -> 48 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 48 -> 50 at (2119, 3027), 2 frames after previous cover
- f106: ref 78897: 49 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 49 -> 65 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79037: 45 -> 62 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 62 -> 57 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79097: 48 -> 49 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 61 -> 50 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 57 -> 64 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 65 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 62 -> 65 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 57 -> 62 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 49 -> 48 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 49 -> 65 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 64 -> 41 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 48 -> 45 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 61 -> 49 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 50 -> 48 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 50 -> 61 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 57 -> 64 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 65 -> 62 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 62 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 61 -> 48 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 45 -> 62 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 62 -> 57 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 57 -> 62 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 61 -> 49 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 65 -> 57 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 45 -> 62 at (2034.5, 3030), 1 frames after previous cover
- ... 1700 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 891 | 80 | 221 (499), 1 (392) |
| 78896 | 350 (76..429) | 276 | 51 | 48 (76), 41 (68), 77 (46), 149 (28), 64 (26), 57 (22), 160 (10) |
| 78969 | 352 (80..434) | 265 | 52 | 41 (45), 57 (41), 48 (38), 195 (35), 149 (34), 75 (28), 160 (21), 45 (12), 64 (5), 161 (5), 77 (1) |
| 78971 | 352 (84..439) | 250 | 64 | 160 (56), 77 (33), 65 (31), 75 (22), 57 (21), 41 (15), 61 (13), 49 (12), 64 (11), 45 (7), 161 (7), 195 (6), +5 more |
| 79045 | 355 (84..443) | 255 | 66 | 77 (52), 89 (42), 57 (32), 65 (30), 160 (22), 64 (19), 75 (13), 49 (12), 161 (9), 48 (6), 62 (4), 61 (4), +4 more |
| 79037 | 355 (86..445) | 251 | 68 | 77 (58), 161 (32), 64 (30), 61 (26), 89 (26), 65 (18), 57 (15), 49 (10), 75 (10), 160 (8), 48 (6), 140 (5), +3 more |
| 78897 | 345 (89..450) | 258 | 57 | 161 (39), 77 (36), 64 (35), 61 (27), 57 (19), 65 (19), 89 (19), 75 (17), 81 (16), 50 (9), 49 (9), 48 (6), +3 more |
| 78899 | 365 (91..455) | 286 | 47 | 161 (41), 81 (40), 61 (37), 77 (33), 75 (29), 49 (27), 64 (27), 65 (16), 89 (12), 48 (10), 50 (9), 57 (5) |
| 79097 | 366 (94..461) | 270 | 66 | 75 (76), 48 (34), 45 (25), 77 (23), 81 (21), 89 (20), 65 (19), 49 (14), 50 (10), 64 (10), 61 (9), 62 (4), +2 more |
| 79098 | 360 (97..467) | 286 | 50 | 45 (76), 89 (39), 75 (36), 50 (27), 65 (24), 64 (20), 48 (16), 49 (14), 61 (12), 86 (10), 77 (7), 81 (3), +1 more |
| 79102 | 371 (98..477) | 279 | 64 | 86 (63), 75 (37), 89 (36), 50 (26), 81 (24), 70 (24), 64 (19), 45 (15), 61 (9), 48 (7), 62 (6), 65 (6), +3 more |
| 79103 | 380 (99..481) | 271 | 70 | 86 (45), 81 (42), 89 (39), 45 (28), 50 (21), 70 (21), 74 (20), 75 (11), 64 (9), 49 (7), 48 (7), 87 (6), +4 more |
| 79105 | 379 (101..484) | 288 | 66 | 81 (49), 74 (45), 86 (32), 45 (31), 64 (20), 50 (18), 75 (16), 70 (16), 87 (12), 62 (11), 49 (9), 57 (9), +5 more |
| 79108 | 385 (104..492) | 305 | 58 | 74 (60), 81 (48), 131 (38), 64 (27), 49 (25), 45 (22), 50 (17), 57 (15), 75 (13), 103 (13), 70 (8), 62 (8), +4 more |
| 79110 | 388 (106..497) | 282 | 59 | 64 (55), 131 (39), 45 (32), 103 (26), 74 (25), 87 (19), 75 (16), 50 (12), 62 (11), 70 (10), 49 (9), 81 (8), +5 more |
| 79111 | 386 (109..500) | 289 | 59 | 131 (70), 103 (50), 45 (27), 87 (23), 70 (22), 89 (18), 64 (17), 62 (17), 50 (11), 49 (9), 74 (7), 81 (4), +5 more |
| 79115 | 421 (111..531) | 313 | 61 | 57 (63), 131 (45), 87 (30), 132 (26), 70 (21), 186 (19), 45 (17), 207 (17), 49 (14), 62 (14), 103 (12), 75 (7), +6 more |
| 79116 | 411 (114..530) | 300 | 65 | 87 (49), 132 (36), 186 (36), 199 (21), 45 (20), 131 (17), 57 (16), 65 (15), 49 (13), 103 (13), 64 (13), 89 (11), +6 more |
| 79122 | 404 (118..532) | 306 | 66 | 132 (66), 70 (32), 87 (28), 103 (27), 45 (23), 57 (21), 49 (18), 207 (17), 62 (15), 74 (11), 81 (8), 131 (7), +8 more |
| 79132 | 391 (120..515) | 295 | 70 | 87 (70), 74 (37), 186 (36), 207 (28), 62 (23), 45 (16), 65 (13), 49 (12), 70 (11), 132 (9), 131 (9), 81 (8), +4 more |
| 79128 | 402 (124..527) | 302 | 67 | 87 (63), 132 (50), 103 (45), 186 (24), 62 (20), 70 (15), 65 (15), 91 (14), 57 (12), 74 (11), 45 (10), 131 (7), +6 more |
| 79134 | 407 (127..533) | 304 | 69 | 103 (60), 70 (49), 207 (40), 87 (25), 65 (19), 81 (16), 86 (15), 132 (14), 57 (14), 91 (13), 74 (11), 199 (9), +5 more |
| 79135 | 409 (129..542) | 298 | 65 | 103 (63), 70 (61), 86 (38), 57 (34), 189 (31), 74 (15), 87 (12), 132 (12), 186 (9), 65 (7), 91 (6), 62 (5), +3 more |
| 79139 | 406 (132..537) | 299 | 73 | 199 (51), 189 (48), 74 (46), 132 (41), 86 (37), 57 (17), 62 (16), 70 (14), 65 (8), 117 (5), 49 (4), 186 (4), +3 more |
| 79136 | 393 (136..538) | 279 | 60 | 189 (56), 86 (50), 74 (46), 199 (27), 65 (21), 70 (19), 57 (15), 49 (14), 62 (11), 103 (8), 132 (7), 186 (3), +1 more |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 43/321/568; tracks with internal gaps: 32; total internal gaps: 676; longest internal gap: 25; tracks ending in coasting: 33 (trailing rows total 1129)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..462 | 459 | 459 | 392 | 67 | 28 | 3 | 30 | 78911 |
| 41 | 80..270 | 191 | 191 | 130 | 61 | 10 | 1 | 51 | 78896, 78969, 78971, 79045 |
| 45 | 82..513 | 432 | 432 | 368 | 64 | 27 | 3 | 30 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 86..381 | 296 | 296 | 217 | 79 | 23 | 9 | 38 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 49 | 88..376 | 289 | 289 | 240 | 49 | 13 | 4 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 89..316 | 228 | 228 | 168 | 60 | 21 | 4 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 57 | 97..566 | 470 | 470 | 392 | 78 | 42 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 100..293 | 194 | 194 | 144 | 50 | 12 | 2 | 35 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 62 | 102..326 | 225 | 225 | 186 | 39 | 9 | 1 | 30 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..525 | 420 | 420 | 360 | 60 | 27 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 106..484 | 379 | 379 | 276 | 103 | 25 | 2 | 75 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 108..514 | 407 | 407 | 333 | 74 | 36 | 3 | 28 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 116..521 | 406 | 406 | 346 | 60 | 25 | 4 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 75 | 116..508 | 393 | 393 | 334 | 59 | 26 | 3 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 77 | 117..458 | 342 | 342 | 292 | 50 | 26 | 6 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 81 | 125..489 | 365 | 365 | 302 | 63 | 24 | 2 | 33 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 86 | 137..510 | 374 | 374 | 310 | 64 | 33 | 3 | 26 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79134, 79135, 79136, 79139 |
| 87 | 137..552 | 416 | 416 | 342 | 74 | 31 | 2 | 37 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 89 | 137..479 | 343 | 343 | 291 | 52 | 20 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 91 | 144..248 | 105 | 105 | 39 | 66 | 4 | 1 | 62 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 103 | 177..571 | 395 | 395 | 327 | 68 | 33 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 207..249 | 43 | 43 | 7 | 36 | 0 | 0 | 36 | 79135, 79139 |
| 131 | 240..571 | 332 | 332 | 240 | 92 | 22 | 25 | 39 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 132 | 240..560 | 321 | 321 | 268 | 53 | 24 | 4 | 23 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 140 | 256..315 | 60 | 60 | 9 | 51 | 0 | 0 | 51 | 79037, 79045 |
| 149 | 284..424 | 141 | 141 | 65 | 76 | 9 | 3 | 63 | 78896, 78969, 78971 |
| 160 | 309..473 | 165 | 165 | 122 | 43 | 13 | 15 | 13 | 78896, 78897, 78969, 78971, 79037, 79045, 79097 |
| 161 | 309..483 | 175 | 175 | 135 | 40 | 11 | 5 | 22 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 186 | 363..570 | 208 | 208 | 141 | 67 | 11 | 13 | 34 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 189 | 367..567 | 201 | 201 | 151 | 50 | 14 | 2 | 33 | 79122, 79134, 79135, 79136, 79139 |
| 195 | 390..468 | 79 | 79 | 41 | 38 | 3 | 2 | 34 | 78969, 78971 |
| 199 | 393..558 | 166 | 166 | 118 | 48 | 10 | 7 | 29 | 79116, 79122, 79128, 79134, 79136, 79139 |
| 207 | 404..561 | 158 | 158 | 113 | 45 | 12 | 2 | 28 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 221 | 441..1008 | 568 | 568 | 499 | 69 | 52 | 3 | 0 | 78911 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 34; matched pairs: 7698; unmatched reference entries: 2444; unmatched candidate entries: 2048
- identity switches: 1760; fragmentation (coverage interruptions): 1573; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 48 -> 50 at (2129, 3033.5), 3 frames after previous cover
- f91: ref 79045: 48 -> 49 at (2116.5, 3034), 5 frames after previous cover
- f92: ref 78897: 48 -> 50 at (2136.5, 3032), 2 frames after previous cover
- f92: ref 78969: 45 -> 41 at (2083, 3033), 1 frames after previous cover
- f92: ref 78971: 49 -> 45 at (2101.5, 3036), 2 frames after previous cover
- f92: ref 79037: 50 -> 49 at (2124, 3034), 1 frames after previous cover
- f93: ref 78969: 41 -> 45 at (2077.5, 3034), 1 frames after previous cover
- f97: ref 78899: 48 -> 50 at (2123, 3030), 4 frames after previous cover
- f97: ref 78969: 45 -> 41 at (2054, 3035.5), 2 frames after previous cover
- f98: ref 79045: 49 -> 57 at (2075.5, 3033), 4 frames after previous cover
- f99: ref 78897: 50 -> 49 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 49 -> 57 at (2080, 3034.5), 1 frames after previous cover
- f100: ref 79037: 57 -> 49 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 48 -> 50 at (2117.5, 3029.5), 2 frames after previous cover
- f100: ref 79098: 50 -> 48 at (2130, 3027), 1 frames after previous cover
- f100: ref 79102: 48 -> 61 at (2142.5, 3026), 1 frames after previous cover
- f101: ref 78897: 49 -> 57 at (2083, 3033.5), 2 frames after previous cover
- f101: ref 78899: 50 -> 49 at (2098.5, 3030.5), 4 frames after previous cover
- f101: ref 79098: 48 -> 50 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 61 -> 48 at (2136, 3025.5), 1 frames after previous cover
- f102: ref 78897: 57 -> 49 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78971: 45 -> 62 at (2041, 3033), 2 frames after previous cover
- f102: ref 79037: 49 -> 57 at (2062, 3034.5), 2 frames after previous cover
- f102: ref 79045: 57 -> 45 at (2049, 3033), 2 frames after previous cover
- f103: ref 78969: 41 -> 57 at (2014.5, 3033.5), 5 frames after previous cover
- f103: ref 79097: 50 -> 48 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 78971: 62 -> 57 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79037: 57 -> 45 at (2051, 3034), 2 frames after previous cover
- f104: ref 79045: 45 -> 62 at (2036.5, 3033.5), 1 frames after previous cover
- f104: ref 79098: 50 -> 48 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 48 -> 50 at (2119, 3027), 2 frames after previous cover
- f106: ref 78897: 49 -> 45 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 78899: 49 -> 65 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79037: 45 -> 62 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79045: 62 -> 57 at (2023.5, 3033.5), 1 frames after previous cover
- f106: ref 79097: 48 -> 49 at (2082.5, 3028.5), 3 frames after previous cover
- f106: ref 79103: 61 -> 50 at (2116.5, 3023), 5 frames after previous cover
- f107: ref 78969: 57 -> 64 at (1989, 3034.5), 4 frames after previous cover
- f108: ref 78899: 65 -> 49 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 79037: 62 -> 65 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 57 -> 62 at (2014.5, 3034), 2 frames after previous cover
- f108: ref 79097: 49 -> 48 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78899: 49 -> 65 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78969: 64 -> 41 at (1978, 3034.5), 2 frames after previous cover
- f109: ref 79097: 48 -> 45 at (2064.5, 3030), 1 frames after previous cover
- f109: ref 79098: 61 -> 49 at (2077.5, 3029.5), 1 frames after previous cover
- f109: ref 79102: 50 -> 48 at (2090, 3028), 1 frames after previous cover
- f109: ref 79103: 50 -> 61 at (2097, 3024.5), 2 frames after previous cover
- f110: ref 78971: 57 -> 64 at (1990.5, 3034), 1 frames after previous cover
- f110: ref 79037: 65 -> 62 at (2013, 3034.5), 2 frames after previous cover
- f110: ref 79045: 62 -> 57 at (2000.5, 3033.5), 1 frames after previous cover
- f110: ref 79102: 48 -> 61 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79105: 61 -> 48 at (2101.5, 3024.5), 3 frames after previous cover
- f111: ref 78897: 45 -> 62 at (2021.5, 3032.5), 3 frames after previous cover
- f111: ref 79037: 62 -> 57 at (2007.5, 3035), 1 frames after previous cover
- f112: ref 79037: 57 -> 62 at (2000.5, 3035), 1 frames after previous cover
- f113: ref 79103: 61 -> 49 at (2074, 3024.5), 4 frames after previous cover
- f114: ref 78899: 65 -> 57 at (2018, 3031), 2 frames after previous cover
- f114: ref 79097: 45 -> 62 at (2034.5, 3030), 1 frames after previous cover
- ... 1700 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 891 | 80 | 221 (499), 1 (392) |
| 78896 | 350 (76..429) | 276 | 51 | 48 (76), 41 (68), 77 (46), 149 (28), 64 (26), 57 (22), 160 (10) |
| 78969 | 352 (80..434) | 265 | 52 | 41 (45), 57 (41), 48 (38), 195 (35), 149 (34), 75 (28), 160 (21), 45 (12), 64 (5), 161 (5), 77 (1) |
| 78971 | 352 (84..439) | 250 | 64 | 160 (56), 77 (33), 65 (31), 75 (22), 57 (21), 41 (15), 61 (13), 49 (12), 64 (11), 45 (7), 161 (7), 195 (6), +5 more |
| 79045 | 355 (84..443) | 255 | 66 | 77 (52), 89 (42), 57 (32), 65 (30), 160 (22), 64 (19), 75 (13), 49 (12), 161 (9), 48 (6), 62 (4), 61 (4), +4 more |
| 79037 | 355 (86..445) | 251 | 68 | 77 (58), 161 (32), 64 (30), 61 (26), 89 (26), 65 (18), 57 (15), 49 (10), 75 (10), 160 (8), 48 (6), 140 (5), +3 more |
| 78897 | 345 (89..450) | 258 | 57 | 161 (39), 77 (36), 64 (35), 61 (27), 57 (19), 65 (19), 89 (19), 75 (17), 81 (16), 50 (9), 49 (9), 48 (6), +3 more |
| 78899 | 365 (91..455) | 286 | 47 | 161 (41), 81 (40), 61 (37), 77 (33), 75 (29), 49 (27), 64 (27), 65 (16), 89 (12), 48 (10), 50 (9), 57 (5) |
| 79097 | 366 (94..461) | 270 | 66 | 75 (76), 48 (34), 45 (25), 77 (23), 81 (21), 89 (20), 65 (19), 49 (14), 50 (10), 64 (10), 61 (9), 62 (4), +2 more |
| 79098 | 360 (97..467) | 286 | 50 | 45 (76), 89 (39), 75 (36), 50 (27), 65 (24), 64 (20), 48 (16), 49 (14), 61 (12), 86 (10), 77 (7), 81 (3), +1 more |
| 79102 | 371 (98..477) | 279 | 64 | 86 (63), 75 (37), 89 (36), 50 (26), 81 (24), 70 (24), 64 (19), 45 (15), 61 (9), 48 (7), 62 (6), 65 (6), +3 more |
| 79103 | 380 (99..481) | 271 | 70 | 86 (45), 81 (42), 89 (39), 45 (28), 50 (21), 70 (21), 74 (20), 75 (11), 64 (9), 49 (7), 48 (7), 87 (6), +4 more |
| 79105 | 379 (101..484) | 288 | 66 | 81 (49), 74 (45), 86 (32), 45 (31), 64 (20), 50 (18), 75 (16), 70 (16), 87 (12), 62 (11), 49 (9), 57 (9), +5 more |
| 79108 | 385 (104..492) | 305 | 58 | 74 (60), 81 (48), 131 (38), 64 (27), 49 (25), 45 (22), 50 (17), 57 (15), 75 (13), 103 (13), 70 (8), 62 (8), +4 more |
| 79110 | 388 (106..497) | 282 | 59 | 64 (55), 131 (39), 45 (32), 103 (26), 74 (25), 87 (19), 75 (16), 50 (12), 62 (11), 70 (10), 49 (9), 81 (8), +5 more |
| 79111 | 386 (109..500) | 289 | 59 | 131 (70), 103 (50), 45 (27), 87 (23), 70 (22), 89 (18), 64 (17), 62 (17), 50 (11), 49 (9), 74 (7), 81 (4), +5 more |
| 79115 | 421 (111..531) | 313 | 61 | 57 (63), 131 (45), 87 (30), 132 (26), 70 (21), 186 (19), 45 (17), 207 (17), 49 (14), 62 (14), 103 (12), 75 (7), +6 more |
| 79116 | 411 (114..530) | 300 | 65 | 87 (49), 132 (36), 186 (36), 199 (21), 45 (20), 131 (17), 57 (16), 65 (15), 49 (13), 103 (13), 64 (13), 89 (11), +6 more |
| 79122 | 404 (118..532) | 306 | 66 | 132 (66), 70 (32), 87 (28), 103 (27), 45 (23), 57 (21), 49 (18), 207 (17), 62 (15), 74 (11), 81 (8), 131 (7), +8 more |
| 79132 | 391 (120..515) | 295 | 70 | 87 (70), 74 (37), 186 (36), 207 (28), 62 (23), 45 (16), 65 (13), 49 (12), 70 (11), 132 (9), 131 (9), 81 (8), +4 more |
| 79128 | 402 (124..527) | 302 | 67 | 87 (63), 132 (50), 103 (45), 186 (24), 62 (20), 70 (15), 65 (15), 91 (14), 57 (12), 74 (11), 45 (10), 131 (7), +6 more |
| 79134 | 407 (127..533) | 304 | 69 | 103 (60), 70 (49), 207 (40), 87 (25), 65 (19), 81 (16), 86 (15), 132 (14), 57 (14), 91 (13), 74 (11), 199 (9), +5 more |
| 79135 | 409 (129..542) | 298 | 65 | 103 (63), 70 (61), 86 (38), 57 (34), 189 (31), 74 (15), 87 (12), 132 (12), 186 (9), 65 (7), 91 (6), 62 (5), +3 more |
| 79139 | 406 (132..537) | 299 | 73 | 199 (51), 189 (48), 74 (46), 132 (41), 86 (37), 57 (17), 62 (16), 70 (14), 65 (8), 117 (5), 49 (4), 186 (4), +3 more |
| 79136 | 393 (136..538) | 279 | 60 | 189 (56), 86 (50), 74 (46), 199 (27), 65 (21), 70 (19), 57 (15), 49 (14), 62 (11), 103 (8), 132 (7), 186 (3), +1 more |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 34; lifespan min/median/max: 43/321/568; tracks with internal gaps: 32; total internal gaps: 676; longest internal gap: 25; tracks ending in coasting: 33 (trailing rows total 1129)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4..462 | 459 | 459 | 392 | 67 | 28 | 3 | 30 | 78911 |
| 41 | 80..270 | 191 | 191 | 130 | 61 | 10 | 1 | 51 | 78896, 78969, 78971, 79045 |
| 45 | 82..513 | 432 | 432 | 368 | 64 | 27 | 3 | 30 | 78897, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 48 | 86..381 | 296 | 296 | 217 | 79 | 23 | 9 | 38 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 49 | 88..376 | 289 | 289 | 240 | 49 | 13 | 4 | 30 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 89..316 | 228 | 228 | 168 | 60 | 21 | 4 | 33 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116 |
| 57 | 97..566 | 470 | 470 | 392 | 78 | 42 | 2 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 61 | 100..293 | 194 | 194 | 144 | 50 | 12 | 2 | 35 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 62 | 102..326 | 225 | 225 | 186 | 39 | 9 | 1 | 30 | 78897, 78971, 79037, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 64 | 106..525 | 420 | 420 | 360 | 60 | 27 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 65 | 106..484 | 379 | 379 | 276 | 103 | 25 | 2 | 75 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 70 | 108..514 | 407 | 407 | 333 | 74 | 36 | 3 | 28 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 74 | 116..521 | 406 | 406 | 346 | 60 | 25 | 4 | 29 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 75 | 116..508 | 393 | 393 | 334 | 59 | 26 | 3 | 30 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 77 | 117..458 | 342 | 342 | 292 | 50 | 26 | 6 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103 |
| 81 | 125..489 | 365 | 365 | 302 | 63 | 24 | 2 | 33 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 86 | 137..510 | 374 | 374 | 310 | 64 | 33 | 3 | 26 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79134, 79135, 79136, 79139 |
| 87 | 137..552 | 416 | 416 | 342 | 74 | 31 | 2 | 37 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 89 | 137..479 | 343 | 343 | 291 | 52 | 20 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 91 | 144..248 | 105 | 105 | 39 | 66 | 4 | 1 | 62 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 103 | 177..571 | 395 | 395 | 327 | 68 | 33 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 117 | 207..249 | 43 | 43 | 7 | 36 | 0 | 0 | 36 | 79135, 79139 |
| 131 | 240..571 | 332 | 332 | 240 | 92 | 22 | 25 | 39 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 132 | 240..560 | 321 | 321 | 268 | 53 | 24 | 4 | 23 | 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 140 | 256..315 | 60 | 60 | 9 | 51 | 0 | 0 | 51 | 79037, 79045 |
| 149 | 284..424 | 141 | 141 | 65 | 76 | 9 | 3 | 63 | 78896, 78969, 78971 |
| 160 | 309..473 | 165 | 165 | 122 | 43 | 13 | 15 | 13 | 78896, 78897, 78969, 78971, 79037, 79045, 79097 |
| 161 | 309..483 | 175 | 175 | 135 | 40 | 11 | 5 | 22 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 186 | 363..570 | 208 | 208 | 141 | 67 | 11 | 13 | 34 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 189 | 367..567 | 201 | 201 | 151 | 50 | 14 | 2 | 33 | 79122, 79134, 79135, 79136, 79139 |
| 195 | 390..468 | 79 | 79 | 41 | 38 | 3 | 2 | 34 | 78969, 78971 |
| 199 | 393..558 | 166 | 166 | 118 | 48 | 10 | 7 | 29 | 79116, 79122, 79128, 79134, 79136, 79139 |
| 207 | 404..561 | 158 | 158 | 113 | 45 | 12 | 2 | 28 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 221 | 441..1008 | 568 | 568 | 499 | 69 | 52 | 3 | 0 | 78911 |
