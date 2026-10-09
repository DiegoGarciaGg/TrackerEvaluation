# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=d04b37c3392b
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.30_noise0.0_fp0.5_seed1/tracks.csv sha256=233ed463e780613b
  - detections_csv: outputs/detections/flock/gt_drop0.30_noise0.0_fp0.5_seed1.csv sha256=d04b37c3392ba547
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.30_noise0.0_fp0.5_seed1
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
| observations | none | 4 | 0.291 | 0.123 | 0.543 | 0.01 | 0.244 | 1440 | 2028.0 |
| observations | none | 6 | 0.291 | 0.124 | 0.544 | 0.01 | 0.245 | 1438 | 2027.0 |
| observations | none | 8 | 0.291 | 0.125 | 0.544 | 0.04 | 0.250 | 1432 | 2016.0 |
| observations | none | 12 | 0.292 | 0.128 | 0.552 | 0.42 | 0.266 | 1341 | 1966.0 |
| observations | ignore | 4 | 0.291 | 0.123 | 0.543 | 0.01 | 0.244 | 1440 | 2028.0 |
| observations | ignore | 6 | 0.291 | 0.124 | 0.544 | 0.01 | 0.245 | 1438 | 2027.0 |
| observations | ignore | 8 | 0.291 | 0.125 | 0.544 | 0.04 | 0.250 | 1432 | 2016.0 |
| observations | ignore | 12 | 0.292 | 0.128 | 0.552 | 0.42 | 0.266 | 1341 | 1966.0 |
| updates | none | 4 | 0.278 | 0.132 | 0.312 | 0.11 | 0.230 | 1466 | 1937.0 |
| updates | none | 6 | 0.299 | 0.143 | 0.408 | 0.45 | 0.250 | 1472 | 1622.0 |
| updates | none | 8 | 0.313 | 0.151 | 0.516 | 0.91 | 0.270 | 1431 | 1230.0 |
| updates | none | 12 | 0.330 | 0.162 | 0.559 | 1.47 | 0.294 | 1322 | 1072.0 |
| updates | ignore | 4 | 0.278 | 0.132 | 0.312 | 0.11 | 0.230 | 1466 | 1937.0 |
| updates | ignore | 6 | 0.299 | 0.143 | 0.408 | 0.45 | 0.250 | 1472 | 1622.0 |
| updates | ignore | 8 | 0.313 | 0.151 | 0.516 | 0.91 | 0.270 | 1431 | 1230.0 |
| updates | ignore | 12 | 0.330 | 0.162 | 0.559 | 1.47 | 0.294 | 1322 | 1072.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7008; unmatched reference entries: 3134; unmatched candidate entries: 57
- identity switches: 1432; fragmentation (coverage interruptions): 2066; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 37 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 34 -> 28 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 34 -> 42 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 34 -> 42 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 37 -> 34 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 34 -> 42 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 42 -> 47 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 37 -> 34 at (2141, 3029), 2 frames after previous cover
- f97: ref 79045: 42 -> 47 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 34 -> 37 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 47 -> 50 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 37 -> 34 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 37 -> 34 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 28 -> 50 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79045: 50 -> 47 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 34 -> 37 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 42 -> 34 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 34 -> 37 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 37 -> 34 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 50 -> 28 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 47 -> 50 at (2036.5, 3033.5), 3 frames after previous cover
- f105: ref 78899: 34 -> 47 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 28 -> 50 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 37 -> 42 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 42 -> 53 at (2120.5, 3023), 5 frames after previous cover
- f106: ref 79103: 53 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 42 -> 53 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 42 -> 34 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 34 -> 47 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 47 -> 42 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 42 -> 47 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 34 -> 42 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 50 -> 38 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 42 -> 37 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 42 -> 53 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 47 -> 42 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 64 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 42 -> 47 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 37 -> 66 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 53 -> 37 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 47 -> 64 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 37 -> 34 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 53 -> 37 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 37 -> 63 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 38 -> 28 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 64 -> 38 at (1988, 3035), 3 frames after previous cover
- f114: ref 79045: 38 -> 50 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79105: 37 -> 66 at (2079, 3025), 1 frames after previous cover
- f114: ref 79110: 53 -> 63 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 65 -> 53 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 28 -> 38 at (1939.5, 3036), 3 frames after previous cover
- f115: ref 79098: 34 -> 47 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79105: 66 -> 37 at (2073, 3025), 1 frames after previous cover
- f115: ref 79115: 63 -> 65 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 47 -> 42 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 38 -> 28 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 50 -> 38 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 63 -> 37 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 42 -> 64 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 28 -> 38 at (1921, 3034.5), 2 frames after previous cover
- ... 1372 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 698 | 209 | 2 (698) |
| 78896 | 350 (76..429) | 239 | 64 | 28 (88), 107 (53), 42 (52), 38 (20), 160 (15), 66 (8), 50 (2), 87 (1) |
| 78969 | 352 (80..434) | 254 | 71 | 28 (71), 42 (65), 81 (28), 83 (25), 160 (19), 107 (18), 174 (11), 50 (9), 38 (5), 66 (3) |
| 78971 | 352 (84..439) | 225 | 70 | 83 (65), 81 (58), 28 (28), 66 (27), 42 (17), 50 (15), 38 (7), 174 (3), 34 (2), 160 (2), 107 (1) |
| 79045 | 355 (84..443) | 243 | 75 | 83 (70), 81 (55), 50 (30), 63 (27), 66 (18), 141 (12), 42 (11), 38 (7), 107 (3), 28 (3), 174 (3), 47 (2), +2 more |
| 79037 | 355 (86..445) | 249 | 64 | 83 (91), 141 (45), 81 (19), 28 (16), 42 (15), 160 (10), 38 (8), 63 (8), 72 (8), 66 (7), 47 (6), 50 (6), +5 more |
| 78897 | 345 (89..450) | 228 | 73 | 141 (26), 50 (25), 42 (24), 81 (24), 92 (24), 28 (22), 72 (19), 38 (15), 107 (14), 83 (10), 66 (8), 87 (5), +5 more |
| 78899 | 365 (91..455) | 266 | 71 | 92 (74), 66 (67), 50 (26), 72 (11), 160 (10), 141 (10), 47 (8), 42 (7), 78 (7), 63 (7), 53 (7), 65 (6), +8 more |
| 79097 | 366 (94..461) | 248 | 77 | 92 (47), 66 (35), 42 (25), 63 (21), 28 (21), 72 (21), 141 (15), 88 (14), 65 (10), 53 (10), 78 (9), 34 (6), +5 more |
| 79098 | 360 (97..467) | 253 | 81 | 92 (73), 66 (21), 88 (18), 53 (17), 63 (16), 72 (14), 47 (12), 34 (11), 64 (11), 160 (8), 42 (7), 50 (7), +10 more |
| 79102 | 371 (98..477) | 237 | 82 | 92 (26), 88 (24), 63 (23), 53 (22), 64 (21), 185 (20), 47 (17), 160 (14), 42 (13), 78 (10), 66 (8), 34 (7), +8 more |
| 79103 | 380 (99..481) | 263 | 75 | 47 (64), 64 (31), 63 (26), 34 (25), 88 (24), 78 (20), 66 (9), 65 (8), 42 (7), 38 (7), 161 (7), 160 (7), +9 more |
| 79105 | 379 (101..484) | 267 | 78 | 78 (36), 185 (36), 34 (35), 63 (26), 47 (26), 141 (16), 64 (14), 65 (12), 28 (12), 160 (12), 42 (8), 37 (6), +8 more |
| 79108 | 385 (104..492) | 265 | 80 | 64 (62), 160 (40), 34 (37), 47 (22), 78 (17), 141 (14), 63 (12), 42 (8), 65 (8), 88 (7), 123 (6), 92 (5), +9 more |
| 79110 | 388 (106..497) | 271 | 79 | 34 (64), 64 (44), 63 (34), 65 (24), 141 (19), 90 (18), 47 (12), 187 (11), 38 (10), 42 (10), 66 (7), 123 (5), +8 more |
| 79111 | 386 (109..500) | 272 | 79 | 42 (63), 65 (30), 38 (24), 34 (21), 47 (17), 123 (16), 64 (15), 90 (13), 78 (12), 161 (12), 63 (11), 53 (10), +7 more |
| 79115 | 421 (111..531) | 293 | 76 | 189 (60), 72 (35), 53 (33), 78 (32), 90 (28), 34 (23), 65 (18), 63 (17), 136 (11), 64 (9), 42 (7), 37 (5), +5 more |
| 79116 | 411 (114..530) | 281 | 88 | 64 (47), 90 (40), 53 (39), 78 (26), 189 (22), 38 (18), 136 (17), 65 (15), 72 (15), 34 (11), 123 (9), 37 (4), +8 more |
| 79122 | 404 (118..532) | 276 | 88 | 136 (63), 53 (33), 64 (33), 38 (25), 63 (20), 34 (18), 72 (16), 90 (11), 65 (9), 87 (7), 161 (7), 66 (6), +7 more |
| 79132 | 391 (120..515) | 276 | 79 | 78 (92), 72 (30), 90 (29), 136 (26), 53 (20), 65 (14), 123 (12), 34 (8), 87 (7), 64 (6), 189 (6), 37 (5), +6 more |
| 79128 | 402 (124..527) | 284 | 82 | 90 (111), 136 (26), 64 (24), 123 (22), 88 (19), 72 (11), 53 (11), 37 (9), 34 (9), 47 (8), 78 (8), 65 (6), +6 more |
| 79134 | 407 (127..533) | 269 | 86 | 47 (65), 187 (44), 72 (28), 90 (23), 136 (22), 78 (21), 64 (16), 161 (10), 123 (9), 88 (8), 65 (6), 34 (6), +5 more |
| 79135 | 409 (129..542) | 290 | 84 | 65 (48), 205 (48), 72 (41), 90 (40), 123 (30), 47 (29), 161 (12), 53 (8), 64 (7), 63 (6), 34 (5), 88 (4), +5 more |
| 79139 | 406 (132..537) | 290 | 80 | 53 (73), 161 (59), 136 (28), 34 (27), 90 (17), 123 (15), 205 (15), 47 (14), 66 (6), 37 (6), 87 (6), 28 (6), +5 more |
| 79136 | 393 (136..538) | 271 | 75 | 161 (66), 123 (62), 136 (39), 37 (20), 87 (19), 88 (16), 38 (14), 187 (12), 53 (9), 205 (9), 28 (4), 47 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 25/277/1003; tracks with internal gaps: 14; total internal gaps: 37; longest internal gap: 1; tracks ending in coasting: 11 (trailing rows total 20)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1007 | 1003 | 711 | 698 | 13 | 13 | 1 | 0 | 78911 |
| 28 | 82..538 | 457 | 291 | 287 | 4 | 4 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79111, 79115, 79116, 79134, 79136, 79139 |
| 34 | 86..496 | 411 | 330 | 327 | 3 | 3 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 37 | 89..212 | 124 | 88 | 86 | 2 | 0 | 0 | 2 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79136, 79139 |
| 38 | 89..321 | 233 | 191 | 188 | 3 | 0 | 0 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136, 79139 |
| 42 | 92..499 | 408 | 341 | 339 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 47 | 96..478 | 383 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 99..271 | 173 | 140 | 137 | 3 | 2 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 105..477 | 373 | 304 | 304 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 63 | 111..443 | 333 | 275 | 274 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 111..532 | 422 | 349 | 348 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 65 | 111..384 | 274 | 228 | 227 | 1 | 0 | 0 | 1 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..429 | 318 | 255 | 254 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 72 | 118..461 | 344 | 280 | 277 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 124..515 | 392 | 316 | 315 | 1 | 1 | 1 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 81 | 124..368 | 245 | 198 | 195 | 3 | 1 | 1 | 2 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 83 | 129..494 | 366 | 265 | 264 | 1 | 0 | 0 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79103 |
| 87 | 137..256 | 120 | 65 | 60 | 5 | 0 | 0 | 5 | 78896, 78897, 78899, 79037, 79097, 79098, 79102, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 88 | 138..318 | 181 | 151 | 149 | 2 | 1 | 1 | 1 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 138..527 | 390 | 335 | 335 | 0 | 0 | 0 | 0 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 139..467 | 329 | 270 | 270 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79139 |
| 107 | 172..303 | 132 | 92 | 89 | 3 | 2 | 1 | 1 | 78896, 78897, 78969, 78971, 79045 |
| 123 | 201..477 | 277 | 199 | 195 | 4 | 2 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 136 | 243..531 | 289 | 234 | 234 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 141 | 256..454 | 199 | 169 | 169 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 160 | 316..490 | 175 | 142 | 142 | 0 | 0 | 0 | 0 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 161 | 316..537 | 222 | 180 | 180 | 0 | 0 | 0 | 0 | 79103, 79105, 79110, 79111, 79122, 79128, 79134, 79135, 79136, 79139 |
| 174 | 368..392 | 25 | 18 | 17 | 1 | 0 | 0 | 1 | 78969, 78971, 79045 |
| 185 | 395..481 | 87 | 71 | 71 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 187 | 398..533 | 136 | 92 | 92 | 0 | 0 | 0 | 0 | 79098, 79108, 79110, 79111, 79116, 79128, 79134, 79136, 79139 |
| 189 | 400..530 | 131 | 95 | 95 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 205 | 445..542 | 98 | 72 | 72 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 7008; unmatched reference entries: 3134; unmatched candidate entries: 57
- identity switches: 1432; fragmentation (coverage interruptions): 2066; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 37 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 34 -> 28 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 34 -> 42 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 34 -> 42 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 37 -> 34 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 34 -> 42 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 42 -> 47 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 37 -> 34 at (2141, 3029), 2 frames after previous cover
- f97: ref 79045: 42 -> 47 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 34 -> 37 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 47 -> 50 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 37 -> 34 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 37 -> 34 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 28 -> 50 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79045: 50 -> 47 at (2054.5, 3031.5), 2 frames after previous cover
- f101: ref 79098: 34 -> 37 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 42 -> 34 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 34 -> 37 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 79097: 37 -> 34 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 50 -> 28 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 47 -> 50 at (2036.5, 3033.5), 3 frames after previous cover
- f105: ref 78899: 34 -> 47 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 28 -> 50 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 37 -> 42 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 42 -> 53 at (2120.5, 3023), 5 frames after previous cover
- f106: ref 79103: 53 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 42 -> 53 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 42 -> 34 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 34 -> 47 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 47 -> 42 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 42 -> 47 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 34 -> 42 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 50 -> 38 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 42 -> 37 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 42 -> 53 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 47 -> 42 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 64 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 42 -> 47 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 37 -> 66 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 53 -> 37 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 47 -> 64 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 37 -> 34 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 53 -> 37 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 37 -> 63 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 38 -> 28 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 64 -> 38 at (1988, 3035), 3 frames after previous cover
- f114: ref 79045: 38 -> 50 at (1976.5, 3034.5), 2 frames after previous cover
- f114: ref 79105: 37 -> 66 at (2079, 3025), 1 frames after previous cover
- f114: ref 79110: 53 -> 63 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 65 -> 53 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 28 -> 38 at (1939.5, 3036), 3 frames after previous cover
- f115: ref 79098: 34 -> 47 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79105: 66 -> 37 at (2073, 3025), 1 frames after previous cover
- f115: ref 79115: 63 -> 65 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 47 -> 42 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 38 -> 28 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 50 -> 38 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 63 -> 37 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 42 -> 64 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 28 -> 38 at (1921, 3034.5), 2 frames after previous cover
- ... 1372 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 698 | 209 | 2 (698) |
| 78896 | 350 (76..429) | 239 | 64 | 28 (88), 107 (53), 42 (52), 38 (20), 160 (15), 66 (8), 50 (2), 87 (1) |
| 78969 | 352 (80..434) | 254 | 71 | 28 (71), 42 (65), 81 (28), 83 (25), 160 (19), 107 (18), 174 (11), 50 (9), 38 (5), 66 (3) |
| 78971 | 352 (84..439) | 225 | 70 | 83 (65), 81 (58), 28 (28), 66 (27), 42 (17), 50 (15), 38 (7), 174 (3), 34 (2), 160 (2), 107 (1) |
| 79045 | 355 (84..443) | 243 | 75 | 83 (70), 81 (55), 50 (30), 63 (27), 66 (18), 141 (12), 42 (11), 38 (7), 107 (3), 28 (3), 174 (3), 47 (2), +2 more |
| 79037 | 355 (86..445) | 249 | 64 | 83 (91), 141 (45), 81 (19), 28 (16), 42 (15), 160 (10), 38 (8), 63 (8), 72 (8), 66 (7), 47 (6), 50 (6), +5 more |
| 78897 | 345 (89..450) | 228 | 73 | 141 (26), 50 (25), 42 (24), 81 (24), 92 (24), 28 (22), 72 (19), 38 (15), 107 (14), 83 (10), 66 (8), 87 (5), +5 more |
| 78899 | 365 (91..455) | 266 | 71 | 92 (74), 66 (67), 50 (26), 72 (11), 160 (10), 141 (10), 47 (8), 42 (7), 78 (7), 63 (7), 53 (7), 65 (6), +8 more |
| 79097 | 366 (94..461) | 248 | 77 | 92 (47), 66 (35), 42 (25), 63 (21), 28 (21), 72 (21), 141 (15), 88 (14), 65 (10), 53 (10), 78 (9), 34 (6), +5 more |
| 79098 | 360 (97..467) | 253 | 81 | 92 (73), 66 (21), 88 (18), 53 (17), 63 (16), 72 (14), 47 (12), 34 (11), 64 (11), 160 (8), 42 (7), 50 (7), +10 more |
| 79102 | 371 (98..477) | 237 | 82 | 92 (26), 88 (24), 63 (23), 53 (22), 64 (21), 185 (20), 47 (17), 160 (14), 42 (13), 78 (10), 66 (8), 34 (7), +8 more |
| 79103 | 380 (99..481) | 263 | 75 | 47 (64), 64 (31), 63 (26), 34 (25), 88 (24), 78 (20), 66 (9), 65 (8), 42 (7), 38 (7), 161 (7), 160 (7), +9 more |
| 79105 | 379 (101..484) | 267 | 78 | 78 (36), 185 (36), 34 (35), 63 (26), 47 (26), 141 (16), 64 (14), 65 (12), 28 (12), 160 (12), 42 (8), 37 (6), +8 more |
| 79108 | 385 (104..492) | 265 | 80 | 64 (62), 160 (40), 34 (37), 47 (22), 78 (17), 141 (14), 63 (12), 42 (8), 65 (8), 88 (7), 123 (6), 92 (5), +9 more |
| 79110 | 388 (106..497) | 271 | 79 | 34 (64), 64 (44), 63 (34), 65 (24), 141 (19), 90 (18), 47 (12), 187 (11), 38 (10), 42 (10), 66 (7), 123 (5), +8 more |
| 79111 | 386 (109..500) | 272 | 79 | 42 (63), 65 (30), 38 (24), 34 (21), 47 (17), 123 (16), 64 (15), 90 (13), 78 (12), 161 (12), 63 (11), 53 (10), +7 more |
| 79115 | 421 (111..531) | 293 | 76 | 189 (60), 72 (35), 53 (33), 78 (32), 90 (28), 34 (23), 65 (18), 63 (17), 136 (11), 64 (9), 42 (7), 37 (5), +5 more |
| 79116 | 411 (114..530) | 281 | 88 | 64 (47), 90 (40), 53 (39), 78 (26), 189 (22), 38 (18), 136 (17), 65 (15), 72 (15), 34 (11), 123 (9), 37 (4), +8 more |
| 79122 | 404 (118..532) | 276 | 88 | 136 (63), 53 (33), 64 (33), 38 (25), 63 (20), 34 (18), 72 (16), 90 (11), 65 (9), 87 (7), 161 (7), 66 (6), +7 more |
| 79132 | 391 (120..515) | 276 | 79 | 78 (92), 72 (30), 90 (29), 136 (26), 53 (20), 65 (14), 123 (12), 34 (8), 87 (7), 64 (6), 189 (6), 37 (5), +6 more |
| 79128 | 402 (124..527) | 284 | 82 | 90 (111), 136 (26), 64 (24), 123 (22), 88 (19), 72 (11), 53 (11), 37 (9), 34 (9), 47 (8), 78 (8), 65 (6), +6 more |
| 79134 | 407 (127..533) | 269 | 86 | 47 (65), 187 (44), 72 (28), 90 (23), 136 (22), 78 (21), 64 (16), 161 (10), 123 (9), 88 (8), 65 (6), 34 (6), +5 more |
| 79135 | 409 (129..542) | 290 | 84 | 65 (48), 205 (48), 72 (41), 90 (40), 123 (30), 47 (29), 161 (12), 53 (8), 64 (7), 63 (6), 34 (5), 88 (4), +5 more |
| 79139 | 406 (132..537) | 290 | 80 | 53 (73), 161 (59), 136 (28), 34 (27), 90 (17), 123 (15), 205 (15), 47 (14), 66 (6), 37 (6), 87 (6), 28 (6), +5 more |
| 79136 | 393 (136..538) | 271 | 75 | 161 (66), 123 (62), 136 (39), 37 (20), 87 (19), 88 (16), 38 (14), 187 (12), 53 (9), 205 (9), 28 (4), 47 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 25/277/1003; tracks with internal gaps: 14; total internal gaps: 37; longest internal gap: 1; tracks ending in coasting: 11 (trailing rows total 20)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1007 | 1003 | 711 | 698 | 13 | 13 | 1 | 0 | 78911 |
| 28 | 82..538 | 457 | 291 | 287 | 4 | 4 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79103, 79105, 79108, 79111, 79115, 79116, 79134, 79136, 79139 |
| 34 | 86..496 | 411 | 330 | 327 | 3 | 3 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 37 | 89..212 | 124 | 88 | 86 | 2 | 0 | 0 | 2 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79136, 79139 |
| 38 | 89..321 | 233 | 191 | 188 | 3 | 0 | 0 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136, 79139 |
| 42 | 92..499 | 408 | 341 | 339 | 2 | 2 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 47 | 96..478 | 383 | 318 | 318 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 99..271 | 173 | 140 | 137 | 3 | 2 | 1 | 1 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 105..477 | 373 | 304 | 304 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 63 | 111..443 | 333 | 275 | 274 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 111..532 | 422 | 349 | 348 | 1 | 1 | 1 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 65 | 111..384 | 274 | 228 | 227 | 1 | 0 | 0 | 1 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..429 | 318 | 255 | 254 | 1 | 1 | 1 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 72 | 118..461 | 344 | 280 | 277 | 3 | 3 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 124..515 | 392 | 316 | 315 | 1 | 1 | 1 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 81 | 124..368 | 245 | 198 | 195 | 3 | 1 | 1 | 2 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 83 | 129..494 | 366 | 265 | 264 | 1 | 0 | 0 | 1 | 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79103 |
| 87 | 137..256 | 120 | 65 | 60 | 5 | 0 | 0 | 5 | 78896, 78897, 78899, 79037, 79097, 79098, 79102, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 88 | 138..318 | 181 | 151 | 149 | 2 | 1 | 1 | 1 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 138..527 | 390 | 335 | 335 | 0 | 0 | 0 | 0 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 139..467 | 329 | 270 | 270 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79139 |
| 107 | 172..303 | 132 | 92 | 89 | 3 | 2 | 1 | 1 | 78896, 78897, 78969, 78971, 79045 |
| 123 | 201..477 | 277 | 199 | 195 | 4 | 2 | 1 | 2 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 136 | 243..531 | 289 | 234 | 234 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 141 | 256..454 | 199 | 169 | 169 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 160 | 316..490 | 175 | 142 | 142 | 0 | 0 | 0 | 0 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 161 | 316..537 | 222 | 180 | 180 | 0 | 0 | 0 | 0 | 79103, 79105, 79110, 79111, 79122, 79128, 79134, 79135, 79136, 79139 |
| 174 | 368..392 | 25 | 18 | 17 | 1 | 0 | 0 | 1 | 78969, 78971, 79045 |
| 185 | 395..481 | 87 | 71 | 71 | 0 | 0 | 0 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 187 | 398..533 | 136 | 92 | 92 | 0 | 0 | 0 | 0 | 79098, 79108, 79110, 79111, 79116, 79128, 79134, 79136, 79139 |
| 189 | 400..530 | 131 | 95 | 95 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132 |
| 205 | 445..542 | 98 | 72 | 72 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8305; unmatched reference entries: 1837; unmatched candidate entries: 1645
- identity switches: 1431; fragmentation (coverage interruptions): 1171; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 37 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 34 -> 28 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 34 -> 42 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 34 -> 42 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 37 -> 34 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 34 -> 42 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 42 -> 47 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 37 -> 34 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 42 -> 47 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 34 -> 37 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 47 -> 50 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 37 -> 34 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 37 -> 34 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 28 -> 47 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79098: 34 -> 37 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 42 -> 34 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 34 -> 37 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 78971: 47 -> 50 at (2033, 3032.5), 2 frames after previous cover
- f103: ref 79097: 37 -> 34 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 50 -> 28 at (2027.5, 3034.5), 1 frames after previous cover
- f105: ref 78899: 34 -> 47 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 28 -> 50 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 37 -> 42 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 42 -> 53 at (2120.5, 3023), 4 frames after previous cover
- f106: ref 79103: 53 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 42 -> 53 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 42 -> 34 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 34 -> 47 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 47 -> 42 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 42 -> 47 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 34 -> 42 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 50 -> 38 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 42 -> 37 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 42 -> 53 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 47 -> 42 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 64 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 42 -> 47 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 37 -> 66 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 53 -> 37 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 47 -> 64 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 37 -> 34 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 53 -> 37 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 37 -> 63 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 38 -> 28 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 64 -> 38 at (1988, 3035), 2 frames after previous cover
- f114: ref 79045: 38 -> 50 at (1976.5, 3034.5), 1 frames after previous cover
- f114: ref 79110: 53 -> 63 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 65 -> 53 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 28 -> 38 at (1939.5, 3036), 2 frames after previous cover
- f115: ref 79098: 34 -> 47 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79115: 63 -> 65 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 47 -> 42 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 38 -> 28 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 50 -> 38 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 63 -> 37 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 42 -> 64 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 28 -> 38 at (1921, 3034.5), 1 frames after previous cover
- f118: ref 79037: 38 -> 50 at (1964, 3035.5), 4 frames after previous cover
- f118: ref 79098: 47 -> 42 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79102: 34 -> 47 at (2036.5, 3029.5), 1 frames after previous cover
- ... 1371 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 946 | 34 | 2 (946) |
| 78896 | 350 (76..429) | 286 | 30 | 28 (104), 107 (66), 42 (64), 38 (21), 160 (17), 66 (9), 50 (3), 87 (2) |
| 78969 | 352 (80..434) | 304 | 36 | 28 (79), 42 (74), 81 (33), 83 (31), 107 (26), 160 (24), 174 (14), 50 (10), 38 (7), 66 (4), 87 (2) |
| 78971 | 352 (84..439) | 262 | 48 | 83 (74), 81 (71), 66 (33), 28 (30), 42 (21), 50 (14), 38 (9), 174 (4), 34 (2), 160 (2), 47 (1), 107 (1) |
| 79045 | 355 (84..443) | 285 | 46 | 83 (83), 81 (59), 50 (39), 63 (34), 66 (21), 141 (13), 42 (12), 38 (8), 28 (5), 107 (4), 174 (4), 34 (1), +2 more |
| 79037 | 355 (86..445) | 287 | 40 | 83 (106), 141 (54), 81 (20), 28 (18), 42 (15), 160 (10), 63 (10), 38 (9), 66 (9), 72 (9), 47 (7), 50 (7), +5 more |
| 78897 | 345 (89..450) | 263 | 49 | 50 (30), 141 (30), 81 (27), 28 (27), 42 (26), 92 (26), 72 (21), 107 (18), 38 (17), 83 (12), 66 (10), 87 (7), +5 more |
| 78899 | 365 (91..455) | 306 | 40 | 92 (90), 66 (78), 50 (26), 141 (14), 72 (13), 160 (12), 78 (9), 47 (8), 63 (8), 53 (8), 42 (7), 65 (7), +7 more |
| 79097 | 366 (94..461) | 287 | 53 | 92 (51), 66 (40), 28 (30), 42 (28), 63 (24), 72 (24), 88 (17), 141 (17), 53 (13), 78 (11), 65 (10), 34 (6), +5 more |
| 79098 | 360 (97..467) | 288 | 56 | 92 (83), 66 (26), 88 (23), 72 (21), 53 (18), 63 (17), 34 (12), 47 (12), 64 (11), 42 (8), 65 (8), 160 (8), +10 more |
| 79102 | 371 (98..477) | 274 | 54 | 92 (32), 53 (32), 88 (27), 63 (25), 64 (22), 185 (21), 47 (19), 160 (17), 42 (15), 78 (11), 66 (10), 72 (8), +8 more |
| 79103 | 380 (99..481) | 287 | 57 | 47 (72), 64 (36), 34 (30), 63 (28), 88 (24), 78 (21), 42 (9), 66 (9), 38 (8), 65 (8), 161 (7), 92 (6), +8 more |
| 79105 | 379 (101..484) | 312 | 44 | 34 (48), 185 (47), 78 (38), 47 (29), 63 (28), 141 (20), 64 (16), 28 (16), 65 (12), 160 (11), 42 (10), 37 (7), +8 more |
| 79108 | 385 (104..492) | 309 | 47 | 64 (71), 160 (53), 34 (45), 47 (23), 78 (22), 63 (14), 141 (14), 65 (9), 42 (8), 123 (8), 88 (8), 92 (6), +8 more |
| 79110 | 388 (106..497) | 316 | 46 | 34 (81), 64 (49), 63 (41), 65 (27), 90 (20), 141 (20), 47 (13), 187 (13), 38 (11), 42 (11), 66 (8), 78 (5), +9 more |
| 79111 | 386 (109..500) | 309 | 55 | 42 (74), 65 (35), 38 (27), 34 (21), 47 (20), 123 (17), 64 (16), 78 (16), 63 (14), 90 (14), 161 (13), 53 (11), +6 more |
| 79115 | 421 (111..531) | 339 | 50 | 189 (81), 72 (38), 53 (35), 78 (31), 90 (30), 65 (26), 34 (25), 63 (19), 136 (12), 64 (9), 123 (8), 42 (7), +5 more |
| 79116 | 411 (114..530) | 319 | 60 | 64 (58), 90 (48), 53 (43), 78 (32), 189 (24), 38 (20), 136 (18), 72 (16), 65 (15), 34 (11), 187 (7), 37 (5), +8 more |
| 79122 | 404 (118..532) | 329 | 57 | 136 (73), 64 (40), 53 (37), 38 (30), 63 (24), 34 (22), 72 (18), 90 (14), 65 (11), 78 (10), 123 (9), 161 (9), +8 more |
| 79132 | 391 (120..515) | 315 | 52 | 78 (106), 72 (35), 90 (32), 136 (28), 53 (23), 65 (14), 123 (14), 34 (8), 66 (7), 87 (7), 64 (7), 47 (6), +7 more |
| 79128 | 402 (124..527) | 334 | 48 | 90 (129), 136 (30), 64 (27), 123 (25), 88 (23), 78 (16), 53 (13), 72 (12), 34 (11), 47 (11), 37 (9), 63 (8), +5 more |
| 79134 | 407 (127..533) | 331 | 45 | 47 (83), 187 (61), 72 (32), 90 (26), 136 (24), 78 (22), 64 (20), 161 (15), 123 (10), 34 (9), 88 (8), 63 (7), +5 more |
| 79135 | 409 (129..542) | 344 | 50 | 65 (61), 205 (58), 72 (49), 90 (43), 123 (40), 47 (32), 161 (13), 53 (8), 63 (7), 34 (7), 64 (7), 87 (5), +5 more |
| 79139 | 406 (132..537) | 348 | 37 | 53 (93), 161 (74), 34 (33), 205 (24), 90 (18), 123 (18), 136 (17), 187 (17), 47 (16), 37 (8), 66 (7), 72 (7), +4 more |
| 79136 | 393 (136..538) | 325 | 37 | 123 (74), 161 (72), 136 (61), 37 (25), 87 (25), 88 (20), 38 (15), 28 (15), 53 (11), 205 (5), 47 (1), 187 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 54/306/1004; tracks with internal gaps: 32; total internal gaps: 381; longest internal gap: 25; tracks ending in coasting: 31 (trailing rows total 979)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 946 | 58 | 34 | 4 | 0 | 78911 |
| 28 | 82..567 | 486 | 486 | 339 | 147 | 30 | 25 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79105, 79115, 79116, 79122, 79134, 79136 |
| 34 | 86..525 | 440 | 440 | 390 | 50 | 14 | 3 | 31 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 37 | 89..241 | 153 | 153 | 96 | 57 | 4 | 2 | 52 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79136, 79139 |
| 38 | 89..350 | 262 | 262 | 214 | 48 | 5 | 2 | 42 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136, 79139 |
| 42 | 92..528 | 437 | 437 | 389 | 48 | 16 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 47 | 96..507 | 412 | 412 | 363 | 49 | 17 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 99..300 | 202 | 202 | 153 | 49 | 7 | 8 | 34 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 105..506 | 402 | 402 | 358 | 44 | 12 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 63 | 111..472 | 362 | 362 | 319 | 43 | 14 | 2 | 27 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 111..561 | 451 | 451 | 398 | 53 | 18 | 4 | 29 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 65 | 111..413 | 303 | 303 | 262 | 41 | 11 | 1 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..458 | 347 | 347 | 299 | 48 | 13 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 72 | 118..490 | 373 | 373 | 321 | 52 | 17 | 7 | 23 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 124..544 | 421 | 421 | 365 | 56 | 18 | 6 | 29 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 81 | 124..397 | 274 | 274 | 221 | 53 | 13 | 4 | 31 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 83 | 129..523 | 395 | 395 | 311 | 84 | 12 | 16 | 42 | 78897, 78969, 78971, 79037, 79045, 79098, 79103 |
| 87 | 137..285 | 149 | 149 | 77 | 72 | 6 | 3 | 62 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 88 | 138..347 | 210 | 210 | 173 | 37 | 6 | 2 | 30 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 138..556 | 419 | 419 | 379 | 40 | 12 | 3 | 26 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 139..496 | 358 | 358 | 313 | 45 | 8 | 2 | 33 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79139 |
| 107 | 172..332 | 161 | 161 | 115 | 46 | 11 | 3 | 30 | 78896, 78897, 78969, 78971, 79045 |
| 123 | 201..506 | 306 | 306 | 233 | 73 | 16 | 20 | 31 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 136 | 243..560 | 318 | 318 | 265 | 53 | 16 | 5 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 141 | 256..483 | 228 | 228 | 196 | 32 | 4 | 1 | 28 | 78897, 78899, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 160 | 316..519 | 204 | 204 | 168 | 36 | 11 | 2 | 22 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 161 | 316..566 | 251 | 251 | 211 | 40 | 7 | 2 | 29 | 79103, 79105, 79110, 79111, 79122, 79128, 79134, 79135, 79136, 79139 |
| 174 | 368..421 | 54 | 54 | 22 | 32 | 1 | 2 | 30 | 78969, 78971, 79045 |
| 185 | 395..510 | 116 | 116 | 84 | 32 | 3 | 2 | 28 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 187 | 398..562 | 165 | 165 | 118 | 47 | 11 | 5 | 29 | 79098, 79108, 79110, 79111, 79116, 79132, 79134, 79136, 79139 |
| 189 | 400..559 | 160 | 160 | 120 | 40 | 7 | 2 | 30 | 79115, 79116, 79122, 79128, 79132 |
| 205 | 445..571 | 127 | 127 | 87 | 40 | 7 | 2 | 29 | 79135, 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 32; matched pairs: 8305; unmatched reference entries: 1837; unmatched candidate entries: 1645
- identity switches: 1431; fragmentation (coverage interruptions): 1171; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 37 -> 34 at (2142, 3030.5), 1 frames after previous cover
- f92: ref 78971: 34 -> 28 at (2101.5, 3036), 5 frames after previous cover
- f92: ref 79045: 34 -> 42 at (2110.5, 3033.5), 4 frames after previous cover
- f93: ref 79037: 34 -> 42 at (2118, 3034.5), 1 frames after previous cover
- f94: ref 78899: 37 -> 34 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 78897: 34 -> 42 at (2118.5, 3032), 2 frames after previous cover
- f96: ref 79037: 42 -> 47 at (2099, 3033.5), 2 frames after previous cover
- f96: ref 79097: 37 -> 34 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 42 -> 47 at (2081.5, 3032), 5 frames after previous cover
- f97: ref 79097: 34 -> 37 at (2135, 3028), 1 frames after previous cover
- f99: ref 79045: 47 -> 50 at (2068, 3033.5), 2 frames after previous cover
- f99: ref 79097: 37 -> 34 at (2122.5, 3028.5), 2 frames after previous cover
- f100: ref 79098: 37 -> 34 at (2130, 3027), 1 frames after previous cover
- f101: ref 78971: 28 -> 47 at (2047.5, 3034), 9 frames after previous cover
- f101: ref 79098: 34 -> 37 at (2124, 3028), 1 frames after previous cover
- f102: ref 78897: 42 -> 34 at (2077, 3031.5), 4 frames after previous cover
- f102: ref 79097: 34 -> 37 at (2105, 3028.5), 3 frames after previous cover
- f103: ref 78971: 47 -> 50 at (2033, 3032.5), 2 frames after previous cover
- f103: ref 79097: 37 -> 34 at (2100, 3028.5), 1 frames after previous cover
- f104: ref 78971: 50 -> 28 at (2027.5, 3034.5), 1 frames after previous cover
- f105: ref 78899: 34 -> 47 at (2074, 3031), 4 frames after previous cover
- f105: ref 78971: 28 -> 50 at (2022, 3034), 1 frames after previous cover
- f105: ref 79098: 37 -> 42 at (2100.5, 3028.5), 2 frames after previous cover
- f105: ref 79103: 42 -> 53 at (2120.5, 3023), 4 frames after previous cover
- f106: ref 79103: 53 -> 42 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 42 -> 53 at (2125, 3025.5), 3 frames after previous cover
- f107: ref 79098: 42 -> 34 at (2090, 3028), 2 frames after previous cover
- f108: ref 78897: 34 -> 47 at (2040.5, 3033), 6 frames after previous cover
- f108: ref 78899: 47 -> 42 at (2055.5, 3031), 1 frames after previous cover
- f109: ref 78899: 42 -> 47 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79097: 34 -> 42 at (2064.5, 3030), 3 frames after previous cover
- f110: ref 79045: 50 -> 38 at (2000.5, 3033.5), 6 frames after previous cover
- f110: ref 79103: 42 -> 37 at (2092.5, 3023.5), 3 frames after previous cover
- f110: ref 79108: 42 -> 53 at (2118, 3025), 6 frames after previous cover
- f111: ref 78899: 47 -> 42 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79037: 47 -> 64 at (2007.5, 3035), 7 frames after previous cover
- f112: ref 78899: 42 -> 47 at (2032, 3032), 1 frames after previous cover
- f112: ref 79103: 37 -> 66 at (2082, 3024), 1 frames after previous cover
- f112: ref 79108: 53 -> 37 at (2109, 3027), 2 frames after previous cover
- f113: ref 78897: 47 -> 64 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 79102: 37 -> 34 at (2067, 3028.5), 4 frames after previous cover
- f113: ref 79105: 53 -> 37 at (2085, 3025), 4 frames after previous cover
- f113: ref 79108: 37 -> 63 at (2101.5, 3026), 1 frames after previous cover
- f114: ref 78896: 38 -> 28 at (1921, 3035), 5 frames after previous cover
- f114: ref 79037: 64 -> 38 at (1988, 3035), 2 frames after previous cover
- f114: ref 79045: 38 -> 50 at (1976.5, 3034.5), 1 frames after previous cover
- f114: ref 79110: 53 -> 63 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 65 -> 53 at (2126, 3027), 1 frames after previous cover
- f115: ref 78969: 28 -> 38 at (1939.5, 3036), 2 frames after previous cover
- f115: ref 79098: 34 -> 47 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79115: 63 -> 65 at (2135.5, 3021), 3 frames after previous cover
- f116: ref 78899: 47 -> 42 at (2006.5, 3032), 2 frames after previous cover
- f116: ref 78969: 38 -> 28 at (1933.5, 3036), 1 frames after previous cover
- f116: ref 78971: 50 -> 38 at (1953, 3036), 1 frames after previous cover
- f117: ref 79108: 63 -> 37 at (2081.5, 3025.5), 1 frames after previous cover
- f118: ref 78899: 42 -> 64 at (1995, 3032.5), 2 frames after previous cover
- f118: ref 78969: 28 -> 38 at (1921, 3034.5), 1 frames after previous cover
- f118: ref 79037: 38 -> 50 at (1964, 3035.5), 4 frames after previous cover
- f118: ref 79098: 47 -> 42 at (2024.5, 3030.5), 1 frames after previous cover
- f118: ref 79102: 34 -> 47 at (2036.5, 3029.5), 1 frames after previous cover
- ... 1371 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 946 | 34 | 2 (946) |
| 78896 | 350 (76..429) | 286 | 30 | 28 (104), 107 (66), 42 (64), 38 (21), 160 (17), 66 (9), 50 (3), 87 (2) |
| 78969 | 352 (80..434) | 304 | 36 | 28 (79), 42 (74), 81 (33), 83 (31), 107 (26), 160 (24), 174 (14), 50 (10), 38 (7), 66 (4), 87 (2) |
| 78971 | 352 (84..439) | 262 | 48 | 83 (74), 81 (71), 66 (33), 28 (30), 42 (21), 50 (14), 38 (9), 174 (4), 34 (2), 160 (2), 47 (1), 107 (1) |
| 79045 | 355 (84..443) | 285 | 46 | 83 (83), 81 (59), 50 (39), 63 (34), 66 (21), 141 (13), 42 (12), 38 (8), 28 (5), 107 (4), 174 (4), 34 (1), +2 more |
| 79037 | 355 (86..445) | 287 | 40 | 83 (106), 141 (54), 81 (20), 28 (18), 42 (15), 160 (10), 63 (10), 38 (9), 66 (9), 72 (9), 47 (7), 50 (7), +5 more |
| 78897 | 345 (89..450) | 263 | 49 | 50 (30), 141 (30), 81 (27), 28 (27), 42 (26), 92 (26), 72 (21), 107 (18), 38 (17), 83 (12), 66 (10), 87 (7), +5 more |
| 78899 | 365 (91..455) | 306 | 40 | 92 (90), 66 (78), 50 (26), 141 (14), 72 (13), 160 (12), 78 (9), 47 (8), 63 (8), 53 (8), 42 (7), 65 (7), +7 more |
| 79097 | 366 (94..461) | 287 | 53 | 92 (51), 66 (40), 28 (30), 42 (28), 63 (24), 72 (24), 88 (17), 141 (17), 53 (13), 78 (11), 65 (10), 34 (6), +5 more |
| 79098 | 360 (97..467) | 288 | 56 | 92 (83), 66 (26), 88 (23), 72 (21), 53 (18), 63 (17), 34 (12), 47 (12), 64 (11), 42 (8), 65 (8), 160 (8), +10 more |
| 79102 | 371 (98..477) | 274 | 54 | 92 (32), 53 (32), 88 (27), 63 (25), 64 (22), 185 (21), 47 (19), 160 (17), 42 (15), 78 (11), 66 (10), 72 (8), +8 more |
| 79103 | 380 (99..481) | 287 | 57 | 47 (72), 64 (36), 34 (30), 63 (28), 88 (24), 78 (21), 42 (9), 66 (9), 38 (8), 65 (8), 161 (7), 92 (6), +8 more |
| 79105 | 379 (101..484) | 312 | 44 | 34 (48), 185 (47), 78 (38), 47 (29), 63 (28), 141 (20), 64 (16), 28 (16), 65 (12), 160 (11), 42 (10), 37 (7), +8 more |
| 79108 | 385 (104..492) | 309 | 47 | 64 (71), 160 (53), 34 (45), 47 (23), 78 (22), 63 (14), 141 (14), 65 (9), 42 (8), 123 (8), 88 (8), 92 (6), +8 more |
| 79110 | 388 (106..497) | 316 | 46 | 34 (81), 64 (49), 63 (41), 65 (27), 90 (20), 141 (20), 47 (13), 187 (13), 38 (11), 42 (11), 66 (8), 78 (5), +9 more |
| 79111 | 386 (109..500) | 309 | 55 | 42 (74), 65 (35), 38 (27), 34 (21), 47 (20), 123 (17), 64 (16), 78 (16), 63 (14), 90 (14), 161 (13), 53 (11), +6 more |
| 79115 | 421 (111..531) | 339 | 50 | 189 (81), 72 (38), 53 (35), 78 (31), 90 (30), 65 (26), 34 (25), 63 (19), 136 (12), 64 (9), 123 (8), 42 (7), +5 more |
| 79116 | 411 (114..530) | 319 | 60 | 64 (58), 90 (48), 53 (43), 78 (32), 189 (24), 38 (20), 136 (18), 72 (16), 65 (15), 34 (11), 187 (7), 37 (5), +8 more |
| 79122 | 404 (118..532) | 329 | 57 | 136 (73), 64 (40), 53 (37), 38 (30), 63 (24), 34 (22), 72 (18), 90 (14), 65 (11), 78 (10), 123 (9), 161 (9), +8 more |
| 79132 | 391 (120..515) | 315 | 52 | 78 (106), 72 (35), 90 (32), 136 (28), 53 (23), 65 (14), 123 (14), 34 (8), 66 (7), 87 (7), 64 (7), 47 (6), +7 more |
| 79128 | 402 (124..527) | 334 | 48 | 90 (129), 136 (30), 64 (27), 123 (25), 88 (23), 78 (16), 53 (13), 72 (12), 34 (11), 47 (11), 37 (9), 63 (8), +5 more |
| 79134 | 407 (127..533) | 331 | 45 | 47 (83), 187 (61), 72 (32), 90 (26), 136 (24), 78 (22), 64 (20), 161 (15), 123 (10), 34 (9), 88 (8), 63 (7), +5 more |
| 79135 | 409 (129..542) | 344 | 50 | 65 (61), 205 (58), 72 (49), 90 (43), 123 (40), 47 (32), 161 (13), 53 (8), 63 (7), 34 (7), 64 (7), 87 (5), +5 more |
| 79139 | 406 (132..537) | 348 | 37 | 53 (93), 161 (74), 34 (33), 205 (24), 90 (18), 123 (18), 136 (17), 187 (17), 47 (16), 37 (8), 66 (7), 72 (7), +4 more |
| 79136 | 393 (136..538) | 325 | 37 | 123 (74), 161 (72), 136 (61), 37 (25), 87 (25), 88 (20), 38 (15), 28 (15), 53 (11), 205 (5), 47 (1), 187 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 32; lifespan min/median/max: 54/306/1004; tracks with internal gaps: 32; total internal gaps: 381; longest internal gap: 25; tracks ending in coasting: 31 (trailing rows total 979)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 5..1008 | 1004 | 1004 | 946 | 58 | 34 | 4 | 0 | 78911 |
| 28 | 82..567 | 486 | 486 | 339 | 147 | 30 | 25 | 29 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79105, 79115, 79116, 79122, 79134, 79136 |
| 34 | 86..525 | 440 | 440 | 390 | 50 | 14 | 3 | 31 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 37 | 89..241 | 153 | 153 | 96 | 57 | 4 | 2 | 52 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79135, 79136, 79139 |
| 38 | 89..350 | 262 | 262 | 214 | 48 | 5 | 2 | 42 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79136, 79139 |
| 42 | 92..528 | 437 | 437 | 389 | 48 | 16 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 47 | 96..507 | 412 | 412 | 363 | 49 | 17 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 50 | 99..300 | 202 | 202 | 153 | 49 | 7 | 8 | 34 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 53 | 105..506 | 402 | 402 | 358 | 44 | 12 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 63 | 111..472 | 362 | 362 | 319 | 43 | 14 | 2 | 27 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 64 | 111..561 | 451 | 451 | 398 | 53 | 18 | 4 | 29 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 65 | 111..413 | 303 | 303 | 262 | 41 | 11 | 1 | 30 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 66 | 112..458 | 347 | 347 | 299 | 48 | 13 | 3 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 72 | 118..490 | 373 | 373 | 321 | 52 | 17 | 7 | 23 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 78 | 124..544 | 421 | 421 | 365 | 56 | 18 | 6 | 29 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135 |
| 81 | 124..397 | 274 | 274 | 221 | 53 | 13 | 4 | 31 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 83 | 129..523 | 395 | 395 | 311 | 84 | 12 | 16 | 42 | 78897, 78969, 78971, 79037, 79045, 79098, 79103 |
| 87 | 137..285 | 149 | 149 | 77 | 72 | 6 | 3 | 62 | 78896, 78897, 78899, 78969, 79037, 79097, 79098, 79102, 79116, 79122, 79132, 79134, 79135, 79136, 79139 |
| 88 | 138..347 | 210 | 210 | 173 | 37 | 6 | 2 | 30 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 90 | 138..556 | 419 | 419 | 379 | 40 | 12 | 3 | 26 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 92 | 139..496 | 358 | 358 | 313 | 45 | 8 | 2 | 33 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79139 |
| 107 | 172..332 | 161 | 161 | 115 | 46 | 11 | 3 | 30 | 78896, 78897, 78969, 78971, 79045 |
| 123 | 201..506 | 306 | 306 | 233 | 73 | 16 | 20 | 31 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 136 | 243..560 | 318 | 318 | 265 | 53 | 16 | 5 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 141 | 256..483 | 228 | 228 | 196 | 32 | 4 | 1 | 28 | 78897, 78899, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110, 79111 |
| 160 | 316..519 | 204 | 204 | 168 | 36 | 11 | 2 | 22 | 78896, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 161 | 316..566 | 251 | 251 | 211 | 40 | 7 | 2 | 29 | 79103, 79105, 79110, 79111, 79122, 79128, 79134, 79135, 79136, 79139 |
| 174 | 368..421 | 54 | 54 | 22 | 32 | 1 | 2 | 30 | 78969, 78971, 79045 |
| 185 | 395..510 | 116 | 116 | 84 | 32 | 3 | 2 | 28 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 187 | 398..562 | 165 | 165 | 118 | 47 | 11 | 5 | 29 | 79098, 79108, 79110, 79111, 79116, 79132, 79134, 79136, 79139 |
| 189 | 400..559 | 160 | 160 | 120 | 40 | 7 | 2 | 30 | 79115, 79116, 79122, 79128, 79132 |
| 205 | 445..571 | 127 | 127 | 87 | 40 | 7 | 2 | 29 | 79135, 79136, 79139 |
