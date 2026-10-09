# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=2070bb34f73e
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise0.0_fp0.0_seed3/tracks.csv sha256=0a1b4df8d9dd7441
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise0.0_fp0.0_seed3.csv sha256=2070bb34f73e2627
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise0.0_fp0.0_seed3
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
| observations | none | 4 | 0.681 | 0.589 | 0.765 | 0.01 | 0.787 | 255 | 1640.0 |
| observations | none | 6 | 0.681 | 0.592 | 0.765 | 0.01 | 0.787 | 255 | 1640.0 |
| observations | none | 8 | 0.680 | 0.602 | 0.765 | 0.02 | 0.787 | 255 | 1641.0 |
| observations | none | 12 | 0.683 | 0.623 | 0.766 | 0.10 | 0.790 | 244 | 1638.0 |
| observations | ignore | 4 | 0.681 | 0.589 | 0.765 | 0.01 | 0.787 | 255 | 1640.0 |
| observations | ignore | 6 | 0.681 | 0.592 | 0.765 | 0.01 | 0.787 | 255 | 1640.0 |
| observations | ignore | 8 | 0.680 | 0.602 | 0.765 | 0.02 | 0.787 | 255 | 1641.0 |
| observations | ignore | 12 | 0.683 | 0.623 | 0.766 | 0.10 | 0.790 | 244 | 1638.0 |
| updates | none | 4 | 0.603 | 0.530 | 0.547 | 0.11 | 0.708 | 303 | 1519.0 |
| updates | none | 6 | 0.653 | 0.577 | 0.665 | 0.45 | 0.763 | 315 | 1042.0 |
| updates | none | 8 | 0.685 | 0.616 | 0.797 | 0.89 | 0.824 | 272 | 530.0 |
| updates | none | 12 | 0.725 | 0.668 | 0.830 | 1.22 | 0.843 | 264 | 391.0 |
| updates | ignore | 4 | 0.603 | 0.530 | 0.547 | 0.11 | 0.708 | 303 | 1519.0 |
| updates | ignore | 6 | 0.653 | 0.577 | 0.665 | 0.45 | 0.763 | 315 | 1042.0 |
| updates | ignore | 8 | 0.685 | 0.616 | 0.797 | 0.89 | 0.824 | 272 | 530.0 |
| updates | ignore | 12 | 0.725 | 0.668 | 0.830 | 1.22 | 0.843 | 264 | 391.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8009; unmatched reference entries: 2133; unmatched candidate entries: 0
- identity switches: 255; fragmentation (coverage interruptions): 1648; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 3 -> 1 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 1 -> 3 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 3 -> 1 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 3 -> 1 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 1 -> 7 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 3 -> 1 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79045: 1 -> 8 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 1 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 3 -> 1 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 1 -> 10 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 8 -> 10 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 1 -> 8 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 10 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 6 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 3 -> 1 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 3 -> 11 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 6 -> 7 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 10 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 8 -> 1 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 1 -> 11 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 8 -> 9 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 1 -> 8 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 10 -> 7 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 9 -> 10 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 11 -> 1 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 7 -> 9 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 3 -> 15 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 9 -> 7 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 3 -> 16 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 3 -> 17 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 7 -> 10 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 9 -> 1 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 10 -> 9 at (2019.5, 3034), 3 frames after previous cover
- f110: ref 79097: 1 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 3 -> 18 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 1 -> 9 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 8 -> 10 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 16 -> 8 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 15 -> 1 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 17 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 3 -> 15 at (2113.5, 3026), 5 frames after previous cover
- f111: ref 79110: 18 -> 17 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 3 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 10 -> 4 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 11 -> 1 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 1 -> 16 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 16 -> 11 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 4 -> 6 at (1928, 3035), 3 frames after previous cover
- f114: ref 78897: 9 -> 19 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 10 -> 9 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 6 -> 4 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 8 -> 10 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 1 -> 8 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 11 -> 1 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 17 -> 15 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 18 -> 17 at (2126, 3027), 2 frames after previous cover
- ... 195 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 812 | 156 | 0 (812) |
| 78896 | 350 (76..429) | 287 | 50 | 6 (259), 4 (23), 1 (5) |
| 78969 | 352 (80..434) | 282 | 47 | 4 (259), 6 (22), 22 (1) |
| 78971 | 352 (84..439) | 279 | 50 | 28 (234), 7 (28), 22 (9), 1 (3), 4 (2), 3 (1), 6 (1), 10 (1) |
| 79045 | 355 (84..443) | 276 | 62 | 22 (239), 7 (9), 9 (5), 4 (5), 26 (5), 8 (3), 10 (3), 1 (2), 3 (2), 21 (2), 6 (1) |
| 79037 | 355 (86..445) | 279 | 57 | 26 (244), 9 (8), 7 (8), 10 (5), 1 (4), 19 (4), 21 (3), 3 (2), 4 (1) |
| 78897 | 345 (89..450) | 271 | 62 | 7 (227), 9 (16), 21 (11), 8 (4), 10 (4), 1 (3), 19 (3), 3 (1), 16 (1), 24 (1) |
| 78899 | 365 (91..455) | 288 | 60 | 24 (248), 8 (12), 16 (11), 10 (6), 1 (5), 3 (3), 9 (2), 21 (1) |
| 79097 | 366 (94..461) | 276 | 74 | 16 (250), 1 (8), 10 (6), 3 (3), 8 (3), 9 (3), 19 (2), 11 (1) |
| 79098 | 360 (97..467) | 277 | 61 | 27 (243), 11 (10), 10 (7), 8 (5), 19 (4), 21 (4), 1 (2), 3 (1), 9 (1) |
| 79102 | 371 (98..477) | 292 | 62 | 21 (257), 27 (6), 15 (5), 16 (5), 10 (5), 9 (5), 8 (4), 3 (2), 11 (2), 1 (1) |
| 79103 | 380 (99..481) | 292 | 65 | 10 (269), 11 (10), 16 (4), 1 (4), 19 (3), 3 (1), 9 (1) |
| 79105 | 379 (101..484) | 297 | 66 | 11 (275), 19 (6), 17 (4), 1 (4), 9 (3), 3 (2), 8 (2), 10 (1) |
| 79108 | 385 (104..492) | 300 | 58 | 18 (270), 11 (15), 20 (4), 1 (4), 3 (3), 15 (2), 8 (2) |
| 79110 | 388 (106..497) | 301 | 61 | 19 (253), 9 (19), 18 (10), 8 (6), 15 (4), 1 (3), 3 (2), 17 (2), 20 (2) |
| 79111 | 386 (109..500) | 304 | 62 | 29 (255), 19 (20), 9 (7), 18 (6), 20 (6), 1 (3), 17 (2), 8 (2), 3 (1), 15 (1), 11 (1) |
| 79115 | 421 (111..531) | 328 | 73 | 9 (278), 8 (15), 18 (13), 19 (10), 15 (6), 3 (3), 17 (2), 1 (1) |
| 79116 | 411 (114..530) | 323 | 71 | 8 (284), 1 (24), 18 (4), 25 (4), 3 (2), 17 (2), 20 (2), 15 (1) |
| 79122 | 404 (118..532) | 309 | 68 | 1 (274), 25 (13), 8 (10), 20 (5), 3 (2), 18 (2), 17 (2), 15 (1) |
| 79132 | 391 (120..515) | 308 | 66 | 25 (283), 20 (8), 3 (6), 1 (5), 17 (4), 15 (2) |
| 79128 | 402 (124..527) | 320 | 65 | 3 (298), 20 (16), 17 (5), 1 (1) |
| 79134 | 407 (127..533) | 330 | 64 | 20 (300), 17 (22), 3 (5), 15 (3) |
| 79135 | 409 (129..542) | 326 | 63 | 17 (247), 15 (65), 3 (14) |
| 79139 | 406 (132..537) | 334 | 63 | 15 (263), 17 (59), 23 (7), 3 (5) |
| 79136 | 393 (136..538) | 318 | 62 | 23 (317), 17 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 293/382/1005; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 812 | 812 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 79..532 | 454 | 356 | 356 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 3 | 84..527 | 444 | 359 | 359 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 4 | 87..434 | 348 | 290 | 290 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 6 | 88..428 | 341 | 283 | 283 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 7 | 90..450 | 361 | 272 | 272 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045 |
| 8 | 91..530 | 440 | 352 | 352 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 9 | 97..531 | 435 | 348 | 348 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115 |
| 10 | 97..481 | 385 | 307 | 307 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 11 | 99..484 | 386 | 314 | 314 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 15 | 105..542 | 438 | 353 | 353 | 0 | 0 | 0 | 0 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 16 | 107..460 | 354 | 271 | 271 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103 |
| 17 | 107..537 | 431 | 352 | 352 | 0 | 0 | 0 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 110..492 | 383 | 305 | 305 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 19 | 114..495 | 382 | 305 | 305 | 0 | 0 | 0 | 0 | 78897, 79037, 79097, 79098, 79103, 79105, 79110, 79111, 79115 |
| 20 | 116..533 | 418 | 343 | 343 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134 |
| 21 | 123..477 | 355 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102 |
| 22 | 130..443 | 314 | 249 | 249 | 0 | 0 | 0 | 0 | 78969, 78971, 79045 |
| 23 | 132..537 | 406 | 324 | 324 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 24 | 135..454 | 320 | 249 | 249 | 0 | 0 | 0 | 0 | 78897, 78899 |
| 25 | 135..515 | 381 | 300 | 300 | 0 | 0 | 0 | 0 | 79116, 79122, 79132 |
| 26 | 137..445 | 309 | 249 | 249 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 27 | 141..467 | 327 | 249 | 249 | 0 | 0 | 0 | 0 | 79098, 79102 |
| 28 | 146..438 | 293 | 234 | 234 | 0 | 0 | 0 | 0 | 78971 |
| 29 | 177..500 | 324 | 255 | 255 | 0 | 0 | 0 | 0 | 79111 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8009; unmatched reference entries: 2133; unmatched candidate entries: 0
- identity switches: 255; fragmentation (coverage interruptions): 1648; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 3 -> 1 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 1 -> 3 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 3 -> 1 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 3 -> 1 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 1 -> 7 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 3 -> 1 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79045: 1 -> 8 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 1 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 3 -> 1 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 1 -> 10 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 8 -> 10 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 1 -> 8 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 10 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 6 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 3 -> 1 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 3 -> 11 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 6 -> 7 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 10 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 8 -> 1 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 1 -> 11 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 8 -> 9 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 1 -> 8 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 10 -> 7 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 9 -> 10 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 11 -> 1 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 7 -> 9 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 3 -> 15 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 9 -> 7 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 3 -> 16 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 3 -> 17 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 7 -> 10 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 9 -> 1 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 10 -> 9 at (2019.5, 3034), 3 frames after previous cover
- f110: ref 79097: 1 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 3 -> 18 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 1 -> 9 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 8 -> 10 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 16 -> 8 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 15 -> 1 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 17 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 3 -> 15 at (2113.5, 3026), 5 frames after previous cover
- f111: ref 79110: 18 -> 17 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 3 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 10 -> 4 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 11 -> 1 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 1 -> 16 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 16 -> 11 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 4 -> 6 at (1928, 3035), 3 frames after previous cover
- f114: ref 78897: 9 -> 19 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 10 -> 9 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 6 -> 4 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 8 -> 10 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 1 -> 8 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 11 -> 1 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 17 -> 15 at (2111, 3026.5), 2 frames after previous cover
- f114: ref 79111: 18 -> 17 at (2126, 3027), 2 frames after previous cover
- ... 195 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 812 | 156 | 0 (812) |
| 78896 | 350 (76..429) | 287 | 50 | 6 (259), 4 (23), 1 (5) |
| 78969 | 352 (80..434) | 282 | 47 | 4 (259), 6 (22), 22 (1) |
| 78971 | 352 (84..439) | 279 | 50 | 28 (234), 7 (28), 22 (9), 1 (3), 4 (2), 3 (1), 6 (1), 10 (1) |
| 79045 | 355 (84..443) | 276 | 62 | 22 (239), 7 (9), 9 (5), 4 (5), 26 (5), 8 (3), 10 (3), 1 (2), 3 (2), 21 (2), 6 (1) |
| 79037 | 355 (86..445) | 279 | 57 | 26 (244), 9 (8), 7 (8), 10 (5), 1 (4), 19 (4), 21 (3), 3 (2), 4 (1) |
| 78897 | 345 (89..450) | 271 | 62 | 7 (227), 9 (16), 21 (11), 8 (4), 10 (4), 1 (3), 19 (3), 3 (1), 16 (1), 24 (1) |
| 78899 | 365 (91..455) | 288 | 60 | 24 (248), 8 (12), 16 (11), 10 (6), 1 (5), 3 (3), 9 (2), 21 (1) |
| 79097 | 366 (94..461) | 276 | 74 | 16 (250), 1 (8), 10 (6), 3 (3), 8 (3), 9 (3), 19 (2), 11 (1) |
| 79098 | 360 (97..467) | 277 | 61 | 27 (243), 11 (10), 10 (7), 8 (5), 19 (4), 21 (4), 1 (2), 3 (1), 9 (1) |
| 79102 | 371 (98..477) | 292 | 62 | 21 (257), 27 (6), 15 (5), 16 (5), 10 (5), 9 (5), 8 (4), 3 (2), 11 (2), 1 (1) |
| 79103 | 380 (99..481) | 292 | 65 | 10 (269), 11 (10), 16 (4), 1 (4), 19 (3), 3 (1), 9 (1) |
| 79105 | 379 (101..484) | 297 | 66 | 11 (275), 19 (6), 17 (4), 1 (4), 9 (3), 3 (2), 8 (2), 10 (1) |
| 79108 | 385 (104..492) | 300 | 58 | 18 (270), 11 (15), 20 (4), 1 (4), 3 (3), 15 (2), 8 (2) |
| 79110 | 388 (106..497) | 301 | 61 | 19 (253), 9 (19), 18 (10), 8 (6), 15 (4), 1 (3), 3 (2), 17 (2), 20 (2) |
| 79111 | 386 (109..500) | 304 | 62 | 29 (255), 19 (20), 9 (7), 18 (6), 20 (6), 1 (3), 17 (2), 8 (2), 3 (1), 15 (1), 11 (1) |
| 79115 | 421 (111..531) | 328 | 73 | 9 (278), 8 (15), 18 (13), 19 (10), 15 (6), 3 (3), 17 (2), 1 (1) |
| 79116 | 411 (114..530) | 323 | 71 | 8 (284), 1 (24), 18 (4), 25 (4), 3 (2), 17 (2), 20 (2), 15 (1) |
| 79122 | 404 (118..532) | 309 | 68 | 1 (274), 25 (13), 8 (10), 20 (5), 3 (2), 18 (2), 17 (2), 15 (1) |
| 79132 | 391 (120..515) | 308 | 66 | 25 (283), 20 (8), 3 (6), 1 (5), 17 (4), 15 (2) |
| 79128 | 402 (124..527) | 320 | 65 | 3 (298), 20 (16), 17 (5), 1 (1) |
| 79134 | 407 (127..533) | 330 | 64 | 20 (300), 17 (22), 3 (5), 15 (3) |
| 79135 | 409 (129..542) | 326 | 63 | 17 (247), 15 (65), 3 (14) |
| 79139 | 406 (132..537) | 334 | 63 | 15 (263), 17 (59), 23 (7), 3 (5) |
| 79136 | 393 (136..538) | 318 | 62 | 23 (317), 17 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 293/382/1005; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 812 | 812 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 79..532 | 454 | 356 | 356 | 0 | 0 | 0 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 3 | 84..527 | 444 | 359 | 359 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 4 | 87..434 | 348 | 290 | 290 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045 |
| 6 | 88..428 | 341 | 283 | 283 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79045 |
| 7 | 90..450 | 361 | 272 | 272 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045 |
| 8 | 91..530 | 440 | 352 | 352 | 0 | 0 | 0 | 0 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 9 | 97..531 | 435 | 348 | 348 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115 |
| 10 | 97..481 | 385 | 307 | 307 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 11 | 99..484 | 386 | 314 | 314 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 15 | 105..542 | 438 | 353 | 353 | 0 | 0 | 0 | 0 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 16 | 107..460 | 354 | 271 | 271 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79102, 79103 |
| 17 | 107..537 | 431 | 352 | 352 | 0 | 0 | 0 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 110..492 | 383 | 305 | 305 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 19 | 114..495 | 382 | 305 | 305 | 0 | 0 | 0 | 0 | 78897, 79037, 79097, 79098, 79103, 79105, 79110, 79111, 79115 |
| 20 | 116..533 | 418 | 343 | 343 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134 |
| 21 | 123..477 | 355 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79098, 79102 |
| 22 | 130..443 | 314 | 249 | 249 | 0 | 0 | 0 | 0 | 78969, 78971, 79045 |
| 23 | 132..537 | 406 | 324 | 324 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 24 | 135..454 | 320 | 249 | 249 | 0 | 0 | 0 | 0 | 78897, 78899 |
| 25 | 135..515 | 381 | 300 | 300 | 0 | 0 | 0 | 0 | 79116, 79122, 79132 |
| 26 | 137..445 | 309 | 249 | 249 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 27 | 141..467 | 327 | 249 | 249 | 0 | 0 | 0 | 0 | 79098, 79102 |
| 28 | 146..438 | 293 | 234 | 234 | 0 | 0 | 0 | 0 | 78971 |
| 29 | 177..500 | 324 | 255 | 255 | 0 | 0 | 0 | 0 | 79111 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9543; unmatched reference entries: 599; unmatched candidate entries: 1188
- identity switches: 272; fragmentation (coverage interruptions): 444; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 3 -> 1 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 1 -> 3 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 3 -> 1 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 3 -> 1 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 1 -> 7 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 3 -> 1 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 1 -> 8 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 1 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 3 -> 1 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 1 -> 10 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 8 -> 10 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 1 -> 8 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 10 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 6 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 3 -> 1 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 3 -> 11 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 6 -> 7 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 10 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 8 -> 1 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 1 -> 11 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 8 -> 9 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 1 -> 8 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 10 -> 7 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 9 -> 10 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 11 -> 1 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 7 -> 9 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 3 -> 15 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 9 -> 7 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 3 -> 16 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 3 -> 17 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 7 -> 10 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 9 -> 1 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 10 -> 9 at (2019.5, 3034), 2 frames after previous cover
- f110: ref 79097: 1 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 3 -> 18 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 1 -> 9 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 8 -> 10 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 16 -> 8 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 15 -> 1 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 17 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 3 -> 15 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 18 -> 17 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 3 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 10 -> 4 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 11 -> 1 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 1 -> 16 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 16 -> 11 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 4 -> 6 at (1928, 3035), 2 frames after previous cover
- f114: ref 78897: 9 -> 19 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 10 -> 9 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 6 -> 4 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 8 -> 10 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 1 -> 8 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 11 -> 1 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 17 -> 15 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 18 -> 17 at (2126, 3027), 1 frames after previous cover
- ... 212 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 993 | 12 | 0 (993) |
| 78896 | 350 (76..429) | 335 | 9 | 6 (305), 4 (25), 1 (5) |
| 78969 | 352 (80..434) | 321 | 19 | 4 (296), 6 (24), 22 (1) |
| 78971 | 352 (84..439) | 323 | 21 | 28 (273), 7 (32), 22 (10), 1 (3), 4 (2), 3 (1), 6 (1), 10 (1) |
| 79045 | 355 (84..443) | 328 | 19 | 22 (288), 7 (11), 9 (5), 4 (5), 26 (5), 8 (3), 10 (3), 21 (3), 1 (2), 3 (2), 6 (1) |
| 79037 | 355 (86..445) | 324 | 22 | 26 (284), 7 (10), 9 (9), 10 (6), 19 (5), 1 (4), 21 (3), 3 (2), 4 (1) |
| 78897 | 345 (89..450) | 319 | 23 | 7 (273), 9 (16), 21 (11), 8 (5), 10 (4), 1 (3), 19 (3), 3 (2), 16 (1), 24 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 24 (305), 8 (12), 16 (12), 10 (6), 1 (5), 3 (3), 9 (2), 21 (1), 7 (1) |
| 79097 | 366 (94..461) | 340 | 23 | 16 (312), 1 (10), 10 (6), 3 (3), 8 (3), 9 (3), 19 (2), 11 (1) |
| 79098 | 360 (97..467) | 326 | 27 | 27 (287), 11 (11), 10 (7), 8 (6), 21 (6), 19 (4), 1 (2), 3 (1), 9 (1), 16 (1) |
| 79102 | 371 (98..477) | 345 | 18 | 21 (309), 15 (6), 27 (6), 16 (5), 10 (5), 9 (5), 8 (4), 3 (2), 11 (2), 1 (1) |
| 79103 | 380 (99..481) | 351 | 19 | 10 (324), 11 (10), 16 (4), 1 (4), 21 (4), 19 (3), 3 (1), 9 (1) |
| 79105 | 379 (101..484) | 359 | 15 | 11 (330), 19 (7), 10 (5), 17 (4), 1 (4), 9 (4), 8 (3), 3 (2) |
| 79108 | 385 (104..492) | 352 | 18 | 18 (319), 11 (15), 20 (5), 3 (4), 1 (4), 15 (3), 8 (2) |
| 79110 | 388 (106..497) | 357 | 23 | 19 (304), 9 (22), 18 (10), 8 (6), 15 (5), 17 (3), 1 (3), 3 (2), 20 (2) |
| 79111 | 386 (109..500) | 360 | 14 | 29 (306), 19 (22), 18 (7), 9 (7), 20 (6), 17 (4), 1 (3), 8 (2), 3 (1), 15 (1), 11 (1) |
| 79115 | 421 (111..531) | 407 | 11 | 9 (351), 8 (18), 18 (13), 19 (12), 15 (7), 3 (3), 17 (2), 1 (1) |
| 79116 | 411 (114..530) | 389 | 17 | 8 (343), 1 (27), 18 (5), 3 (4), 25 (4), 17 (3), 20 (2), 15 (1) |
| 79122 | 404 (118..532) | 370 | 25 | 1 (330), 25 (14), 8 (13), 20 (5), 3 (3), 18 (2), 17 (2), 15 (1) |
| 79132 | 391 (120..515) | 364 | 21 | 25 (338), 20 (9), 3 (6), 1 (5), 17 (4), 15 (2) |
| 79128 | 402 (124..527) | 382 | 15 | 3 (358), 20 (17), 17 (6), 1 (1) |
| 79134 | 407 (127..533) | 388 | 17 | 20 (356), 17 (23), 3 (5), 15 (4) |
| 79135 | 409 (129..542) | 387 | 18 | 17 (294), 15 (75), 3 (16), 23 (2) |
| 79139 | 406 (132..537) | 395 | 10 | 15 (317), 23 (56), 17 (12), 3 (7), 1 (2), 20 (1) |
| 79136 | 393 (136..538) | 381 | 12 | 23 (325), 17 (56) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 322/411/1006; tracks with internal gaps: 25; total internal gaps: 408; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 681)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 993 | 13 | 12 | 2 | 0 | 78911 |
| 1 | 79..561 | 483 | 483 | 419 | 64 | 29 | 4 | 24 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 3 | 84..556 | 473 | 473 | 428 | 45 | 13 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 4 | 87..463 | 377 | 377 | 329 | 48 | 15 | 3 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 6 | 88..457 | 370 | 370 | 331 | 39 | 7 | 3 | 28 | 78896, 78969, 78971, 79045 |
| 7 | 90..479 | 390 | 390 | 327 | 63 | 31 | 2 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 8 | 91..559 | 469 | 469 | 420 | 49 | 18 | 2 | 29 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 9 | 97..560 | 464 | 464 | 426 | 38 | 8 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115 |
| 10 | 97..510 | 414 | 414 | 367 | 47 | 13 | 2 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 11 | 99..513 | 415 | 415 | 370 | 45 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 15 | 105..571 | 467 | 467 | 422 | 45 | 11 | 2 | 32 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 16 | 107..489 | 383 | 383 | 335 | 48 | 18 | 2 | 28 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 17 | 107..566 | 460 | 460 | 413 | 47 | 19 | 1 | 28 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 110..521 | 412 | 412 | 356 | 56 | 17 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 19 | 114..524 | 411 | 411 | 362 | 49 | 17 | 3 | 27 | 78897, 79037, 79097, 79098, 79103, 79105, 79110, 79111, 79115 |
| 20 | 116..562 | 447 | 447 | 403 | 44 | 14 | 2 | 29 | 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79139 |
| 21 | 123..506 | 384 | 384 | 337 | 47 | 19 | 2 | 25 | 78897, 78899, 79037, 79045, 79098, 79102, 79103 |
| 22 | 130..472 | 343 | 343 | 299 | 44 | 12 | 2 | 29 | 78969, 78971, 79045 |
| 23 | 132..566 | 435 | 435 | 383 | 52 | 22 | 5 | 24 | 79135, 79136, 79139 |
| 24 | 135..483 | 349 | 349 | 306 | 43 | 13 | 2 | 28 | 78897, 78899 |
| 25 | 135..544 | 410 | 410 | 356 | 54 | 20 | 3 | 29 | 79116, 79122, 79132 |
| 26 | 137..474 | 338 | 338 | 289 | 49 | 15 | 4 | 29 | 79037, 79045 |
| 27 | 141..496 | 356 | 356 | 293 | 63 | 24 | 4 | 29 | 79098, 79102 |
| 28 | 146..467 | 322 | 322 | 273 | 49 | 16 | 3 | 28 | 78971 |
| 29 | 177..529 | 353 | 353 | 306 | 47 | 12 | 3 | 29 | 79111 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9543; unmatched reference entries: 599; unmatched candidate entries: 1188
- identity switches: 272; fragmentation (coverage interruptions): 444; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f85: ref 78971: 3 -> 1 at (2145, 3033.5), 1 frames after previous cover
- f85: ref 79045: 1 -> 3 at (2153, 3032), 1 frames after previous cover
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 79045: 3 -> 1 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 3 -> 1 at (2141, 3034.5), 1 frames after previous cover
- f90: ref 78971: 1 -> 7 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 3 -> 1 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 1 -> 8 at (2116.5, 3034), 3 frames after previous cover
- f94: ref 78897: 1 -> 8 at (2125, 3030), 3 frames after previous cover
- f94: ref 78899: 3 -> 1 at (2140.5, 3029), 1 frames after previous cover
- f97: ref 79037: 1 -> 10 at (2093, 3032.5), 4 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 8 -> 10 at (2100, 3031), 1 frames after previous cover
- f98: ref 78899: 1 -> 8 at (2116.5, 3029), 1 frames after previous cover
- f98: ref 79037: 10 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 6 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 3 -> 1 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 3 -> 11 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78971: 7 -> 6 at (2052.5, 3034.5), 1 frames after previous cover
- f100: ref 79045: 6 -> 7 at (2061, 3032.5), 2 frames after previous cover
- f102: ref 78897: 10 -> 8 at (2077, 3031.5), 1 frames after previous cover
- f102: ref 78899: 8 -> 1 at (2093, 3030.5), 1 frames after previous cover
- f102: ref 78971: 6 -> 10 at (2041, 3033), 2 frames after previous cover
- f102: ref 79097: 1 -> 11 at (2105, 3028.5), 1 frames after previous cover
- f103: ref 78897: 8 -> 9 at (2070.5, 3031.5), 1 frames after previous cover
- f103: ref 78899: 1 -> 8 at (2086, 3030), 1 frames after previous cover
- f103: ref 78971: 10 -> 7 at (2033, 3032.5), 1 frames after previous cover
- f103: ref 79037: 9 -> 10 at (2056.5, 3034.5), 1 frames after previous cover
- f103: ref 79097: 11 -> 1 at (2100, 3028.5), 1 frames after previous cover
- f105: ref 79045: 7 -> 9 at (2030.5, 3033.5), 3 frames after previous cover
- f105: ref 79102: 3 -> 15 at (2113.5, 3026.5), 6 frames after previous cover
- f107: ref 79045: 9 -> 7 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79103: 3 -> 16 at (2110, 3022.5), 7 frames after previous cover
- f107: ref 79105: 3 -> 17 at (2118.5, 3025), 4 frames after previous cover
- f108: ref 79045: 7 -> 10 at (2014.5, 3034), 1 frames after previous cover
- f109: ref 78897: 9 -> 1 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 79037: 10 -> 9 at (2019.5, 3034), 2 frames after previous cover
- f110: ref 79097: 1 -> 16 at (2058.5, 3029.5), 2 frames after previous cover
- f110: ref 79110: 3 -> 18 at (2134, 3026), 1 frames after previous cover
- f111: ref 78897: 1 -> 9 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 8 -> 10 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 79097: 16 -> 8 at (2052, 3030), 1 frames after previous cover
- f111: ref 79102: 15 -> 1 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79105: 17 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 3 -> 15 at (2113.5, 3026), 4 frames after previous cover
- f111: ref 79110: 18 -> 17 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 3 -> 18 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 79045: 10 -> 4 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 11 -> 1 at (2059, 3029.5), 2 frames after previous cover
- f112: ref 79102: 1 -> 16 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79103: 16 -> 11 at (2082, 3024), 1 frames after previous cover
- f113: ref 78896: 4 -> 6 at (1928, 3035), 2 frames after previous cover
- f114: ref 78897: 9 -> 19 at (2002.5, 3034), 1 frames after previous cover
- f114: ref 78899: 10 -> 9 at (2018, 3031), 1 frames after previous cover
- f114: ref 78969: 6 -> 4 at (1946.5, 3035), 2 frames after previous cover
- f114: ref 79097: 8 -> 10 at (2034.5, 3030), 1 frames after previous cover
- f114: ref 79098: 1 -> 8 at (2048, 3030), 1 frames after previous cover
- f114: ref 79103: 11 -> 1 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79110: 17 -> 15 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 18 -> 17 at (2126, 3027), 1 frames after previous cover
- ... 212 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 993 | 12 | 0 (993) |
| 78896 | 350 (76..429) | 335 | 9 | 6 (305), 4 (25), 1 (5) |
| 78969 | 352 (80..434) | 321 | 19 | 4 (296), 6 (24), 22 (1) |
| 78971 | 352 (84..439) | 323 | 21 | 28 (273), 7 (32), 22 (10), 1 (3), 4 (2), 3 (1), 6 (1), 10 (1) |
| 79045 | 355 (84..443) | 328 | 19 | 22 (288), 7 (11), 9 (5), 4 (5), 26 (5), 8 (3), 10 (3), 21 (3), 1 (2), 3 (2), 6 (1) |
| 79037 | 355 (86..445) | 324 | 22 | 26 (284), 7 (10), 9 (9), 10 (6), 19 (5), 1 (4), 21 (3), 3 (2), 4 (1) |
| 78897 | 345 (89..450) | 319 | 23 | 7 (273), 9 (16), 21 (11), 8 (5), 10 (4), 1 (3), 19 (3), 3 (2), 16 (1), 24 (1) |
| 78899 | 365 (91..455) | 347 | 16 | 24 (305), 8 (12), 16 (12), 10 (6), 1 (5), 3 (3), 9 (2), 21 (1), 7 (1) |
| 79097 | 366 (94..461) | 340 | 23 | 16 (312), 1 (10), 10 (6), 3 (3), 8 (3), 9 (3), 19 (2), 11 (1) |
| 79098 | 360 (97..467) | 326 | 27 | 27 (287), 11 (11), 10 (7), 8 (6), 21 (6), 19 (4), 1 (2), 3 (1), 9 (1), 16 (1) |
| 79102 | 371 (98..477) | 345 | 18 | 21 (309), 15 (6), 27 (6), 16 (5), 10 (5), 9 (5), 8 (4), 3 (2), 11 (2), 1 (1) |
| 79103 | 380 (99..481) | 351 | 19 | 10 (324), 11 (10), 16 (4), 1 (4), 21 (4), 19 (3), 3 (1), 9 (1) |
| 79105 | 379 (101..484) | 359 | 15 | 11 (330), 19 (7), 10 (5), 17 (4), 1 (4), 9 (4), 8 (3), 3 (2) |
| 79108 | 385 (104..492) | 352 | 18 | 18 (319), 11 (15), 20 (5), 3 (4), 1 (4), 15 (3), 8 (2) |
| 79110 | 388 (106..497) | 357 | 23 | 19 (304), 9 (22), 18 (10), 8 (6), 15 (5), 17 (3), 1 (3), 3 (2), 20 (2) |
| 79111 | 386 (109..500) | 360 | 14 | 29 (306), 19 (22), 18 (7), 9 (7), 20 (6), 17 (4), 1 (3), 8 (2), 3 (1), 15 (1), 11 (1) |
| 79115 | 421 (111..531) | 407 | 11 | 9 (351), 8 (18), 18 (13), 19 (12), 15 (7), 3 (3), 17 (2), 1 (1) |
| 79116 | 411 (114..530) | 389 | 17 | 8 (343), 1 (27), 18 (5), 3 (4), 25 (4), 17 (3), 20 (2), 15 (1) |
| 79122 | 404 (118..532) | 370 | 25 | 1 (330), 25 (14), 8 (13), 20 (5), 3 (3), 18 (2), 17 (2), 15 (1) |
| 79132 | 391 (120..515) | 364 | 21 | 25 (338), 20 (9), 3 (6), 1 (5), 17 (4), 15 (2) |
| 79128 | 402 (124..527) | 382 | 15 | 3 (358), 20 (17), 17 (6), 1 (1) |
| 79134 | 407 (127..533) | 388 | 17 | 20 (356), 17 (23), 3 (5), 15 (4) |
| 79135 | 409 (129..542) | 387 | 18 | 17 (294), 15 (75), 3 (16), 23 (2) |
| 79139 | 406 (132..537) | 395 | 10 | 15 (317), 23 (56), 17 (12), 3 (7), 1 (2), 20 (1) |
| 79136 | 393 (136..538) | 381 | 12 | 23 (325), 17 (56) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 322/411/1006; tracks with internal gaps: 25; total internal gaps: 408; longest internal gap: 5; tracks ending in coasting: 24 (trailing rows total 681)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 993 | 13 | 12 | 2 | 0 | 78911 |
| 1 | 79..561 | 483 | 483 | 419 | 64 | 29 | 4 | 24 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 3 | 84..556 | 473 | 473 | 428 | 45 | 13 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 4 | 87..463 | 377 | 377 | 329 | 48 | 15 | 3 | 29 | 78896, 78969, 78971, 79037, 79045 |
| 6 | 88..457 | 370 | 370 | 331 | 39 | 7 | 3 | 28 | 78896, 78969, 78971, 79045 |
| 7 | 90..479 | 390 | 390 | 327 | 63 | 31 | 2 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 8 | 91..559 | 469 | 469 | 420 | 49 | 18 | 2 | 29 | 78897, 78899, 79045, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 9 | 97..560 | 464 | 464 | 426 | 38 | 8 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115 |
| 10 | 97..510 | 414 | 414 | 367 | 47 | 13 | 2 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 11 | 99..513 | 415 | 415 | 370 | 45 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 15 | 105..571 | 467 | 467 | 422 | 45 | 11 | 2 | 32 | 79102, 79108, 79110, 79111, 79115, 79116, 79122, 79132, 79134, 79135, 79139 |
| 16 | 107..489 | 383 | 383 | 335 | 48 | 18 | 2 | 28 | 78897, 78899, 79097, 79098, 79102, 79103 |
| 17 | 107..566 | 460 | 460 | 413 | 47 | 19 | 1 | 28 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 110..521 | 412 | 412 | 356 | 56 | 17 | 4 | 29 | 79108, 79110, 79111, 79115, 79116, 79122 |
| 19 | 114..524 | 411 | 411 | 362 | 49 | 17 | 3 | 27 | 78897, 79037, 79097, 79098, 79103, 79105, 79110, 79111, 79115 |
| 20 | 116..562 | 447 | 447 | 403 | 44 | 14 | 2 | 29 | 79108, 79110, 79111, 79116, 79122, 79128, 79132, 79134, 79139 |
| 21 | 123..506 | 384 | 384 | 337 | 47 | 19 | 2 | 25 | 78897, 78899, 79037, 79045, 79098, 79102, 79103 |
| 22 | 130..472 | 343 | 343 | 299 | 44 | 12 | 2 | 29 | 78969, 78971, 79045 |
| 23 | 132..566 | 435 | 435 | 383 | 52 | 22 | 5 | 24 | 79135, 79136, 79139 |
| 24 | 135..483 | 349 | 349 | 306 | 43 | 13 | 2 | 28 | 78897, 78899 |
| 25 | 135..544 | 410 | 410 | 356 | 54 | 20 | 3 | 29 | 79116, 79122, 79132 |
| 26 | 137..474 | 338 | 338 | 289 | 49 | 15 | 4 | 29 | 79037, 79045 |
| 27 | 141..496 | 356 | 356 | 293 | 63 | 24 | 4 | 29 | 79098, 79102 |
| 28 | 146..467 | 322 | 322 | 273 | 49 | 16 | 3 | 28 | 78971 |
| 29 | 177..529 | 353 | 353 | 306 | 47 | 12 | 3 | 29 | 79111 |
