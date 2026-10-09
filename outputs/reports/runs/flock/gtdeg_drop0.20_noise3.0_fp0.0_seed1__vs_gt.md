# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=7b23cf729381
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.20_noise3.0_fp0.0_seed1/tracks.csv sha256=89954d9b3da15293
  - detections_csv: outputs/detections/flock/gt_drop0.20_noise3.0_fp0.0_seed1.csv sha256=7b23cf729381d1df
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.20_noise3.0_fp0.0_seed1
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
| observations | none | 4 | 10142 | 8005 | 0.267 | 0.359 | 0.199 | 2.18 | 0.264 | 0.099 | 2.41 | 418 | 2469.0 | 0.391 | 0.443 | 0.350 | 0.465 | 0.589 | 4714 | 5428 | 3291 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 8005 | 0.370 | 0.493 | 0.278 | 2.74 | 0.451 | 0.530 | 3.20 | 510 | 2137.0 | 0.576 | 0.652 | 0.515 | 0.685 | 0.868 | 6946 | 3196 | 1059 | 0 | 25 | 0 |
| observations | none | 8 | 10142 | 8005 | 0.427 | 0.552 | 0.331 | 3.09 | 0.531 | 0.689 | 3.59 | 503 | 1757.0 | 0.646 | 0.732 | 0.577 | 0.764 | 0.968 | 7747 | 2395 | 258 | 1 | 24 | 0 |
| observations | none | 12 | 10142 | 8005 | 0.490 | 0.606 | 0.396 | 3.63 | 0.571 | 0.732 | 3.90 | 444 | 1622.0 | 0.687 | 0.778 | 0.614 | 0.783 | 0.992 | 7938 | 2204 | 67 | 5 | 20 | 0 |
| observations | ignore | 4 | 10142 | 8005 | 0.267 | 0.359 | 0.199 | 2.18 | 0.264 | 0.099 | 2.41 | 418 | 2469.0 | 0.391 | 0.443 | 0.350 | 0.465 | 0.589 | 4714 | 5428 | 3291 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 8005 | 0.370 | 0.493 | 0.278 | 2.74 | 0.451 | 0.530 | 3.20 | 510 | 2137.0 | 0.576 | 0.652 | 0.515 | 0.685 | 0.868 | 6946 | 3196 | 1059 | 0 | 25 | 0 |
| observations | ignore | 8 | 10142 | 8005 | 0.427 | 0.552 | 0.331 | 3.09 | 0.531 | 0.689 | 3.59 | 503 | 1757.0 | 0.646 | 0.732 | 0.577 | 0.764 | 0.968 | 7747 | 2395 | 258 | 1 | 24 | 0 |
| observations | ignore | 12 | 10142 | 8005 | 0.490 | 0.606 | 0.396 | 3.63 | 0.571 | 0.732 | 3.90 | 444 | 1622.0 | 0.687 | 0.778 | 0.614 | 0.783 | 0.992 | 7938 | 2204 | 67 | 5 | 20 | 0 |
| updates | none | 4 | 10142 | 10668 | 0.256 | 0.335 | 0.195 | 2.22 | 0.246 | -0.102 | 2.42 | 508 | 2479.0 | 0.369 | 0.359 | 0.378 | 0.500 | 0.475 | 5071 | 5071 | 5597 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10668 | 0.375 | 0.487 | 0.290 | 2.87 | 0.431 | 0.396 | 3.26 | 591 | 1802.0 | 0.557 | 0.544 | 0.572 | 0.753 | 0.716 | 7637 | 2505 | 3031 | 1 | 24 | 0 |
| updates | none | 8 | 10142 | 10668 | 0.450 | 0.569 | 0.357 | 3.32 | 0.543 | 0.640 | 3.78 | 550 | 1030.0 | 0.654 | 0.638 | 0.671 | 0.873 | 0.830 | 8852 | 1290 | 1816 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10668 | 0.537 | 0.652 | 0.442 | 3.99 | 0.636 | 0.782 | 4.39 | 440 | 491.0 | 0.731 | 0.713 | 0.750 | 0.938 | 0.892 | 9517 | 625 | 1151 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10668 | 0.256 | 0.335 | 0.195 | 2.22 | 0.246 | -0.102 | 2.42 | 508 | 2479.0 | 0.369 | 0.359 | 0.378 | 0.500 | 0.475 | 5071 | 5071 | 5597 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10668 | 0.375 | 0.487 | 0.290 | 2.87 | 0.431 | 0.396 | 3.26 | 591 | 1802.0 | 0.557 | 0.544 | 0.572 | 0.753 | 0.716 | 7637 | 2505 | 3031 | 1 | 24 | 0 |
| updates | ignore | 8 | 10142 | 10668 | 0.450 | 0.569 | 0.357 | 3.32 | 0.543 | 0.640 | 3.78 | 550 | 1030.0 | 0.654 | 0.638 | 0.671 | 0.873 | 0.830 | 8852 | 1290 | 1816 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10668 | 0.537 | 0.652 | 0.442 | 3.99 | 0.636 | 0.782 | 4.39 | 440 | 491.0 | 0.731 | 0.713 | 0.750 | 0.938 | 0.892 | 9517 | 625 | 1151 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 7747; unmatched reference entries: 2395; unmatched candidate entries: 258
- identity switches: 503; fragmentation (coverage interruptions): 1776; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 2 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 6 at (2128, 3029), 1 frames after previous cover
- f96: ref 79045: 3 -> 11 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 78897: 6 -> 10 at (2107, 3033), 2 frames after previous cover
- f97: ref 79037: 10 -> 11 at (2093, 3032.5), 1 frames after previous cover
- f97: ref 79045: 11 -> 3 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 79098: 7 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 10 -> 11 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 11 -> 3 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 3 -> 8 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 11 -> 10 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 3 -> 11 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 7 -> 12 at (2117.5, 3029.5), 6 frames after previous cover
- f101: ref 78899: 6 -> 10 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 11 -> 3 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 12 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 5 -> 12 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 5 at (2136, 3025.5), 3 frames after previous cover
- f102: ref 78897: 10 -> 11 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 3 -> 9 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 9 -> 14 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 6 -> 10 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 12 -> 6 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 12 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 10 -> 15 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 9 -> 3 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 3 -> 11 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79103: 6 -> 5 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78899: 15 -> 11 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 3 -> 14 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 3 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 10 -> 15 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 5 -> 6 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 5 -> 7 at (2113.5, 3025), 2 frames after previous cover
- f111: ref 78896: 14 -> 17 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 11 -> 18 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 10 -> 15 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 6 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 6 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 5 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 12 -> 16 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 18 -> 8 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 11 -> 18 at (2025, 3032), 2 frames after previous cover
- f113: ref 79037: 8 -> 3 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 3 -> 14 at (1982.5, 3034), 1 frames after previous cover
- f113: ref 79097: 15 -> 11 at (2040.5, 3031), 3 frames after previous cover
- f114: ref 79103: 6 -> 10 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 5 -> 6 at (2079, 3025), 1 frames after previous cover
- ... 443 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 760 | 190 | 0 (760) |
| 78896 | 350 (76..429) | 266 | 45 | 28 (233), 17 (21), 9 (7), 14 (4), 7 (1) |
| 78969 | 352 (80..434) | 258 | 68 | 9 (218), 17 (26), 8 (5), 28 (5), 3 (4) |
| 78971 | 352 (84..439) | 255 | 69 | 17 (195), 9 (17), 3 (15), 31 (11), 11 (7), 14 (5), 21 (5) |
| 79045 | 355 (84..443) | 277 | 56 | 11 (210), 3 (21), 9 (12), 8 (8), 14 (8), 17 (8), 21 (6), 7 (2), 6 (1), 31 (1) |
| 79037 | 355 (86..445) | 273 | 60 | 14 (198), 11 (24), 3 (19), 9 (7), 31 (7), 8 (5), 10 (4), 21 (4), 5 (2), 6 (2), 7 (1) |
| 78897 | 345 (89..450) | 259 | 62 | 31 (198), 11 (17), 3 (9), 8 (8), 14 (8), 6 (5), 21 (4), 9 (4), 10 (3), 5 (2), 18 (1) |
| 78899 | 365 (91..455) | 273 | 67 | 3 (213), 11 (14), 14 (12), 21 (10), 8 (7), 5 (5), 6 (5), 18 (3), 10 (2), 15 (1), 22 (1) |
| 79097 | 366 (94..461) | 271 | 63 | 22 (217), 3 (13), 8 (12), 11 (9), 21 (7), 15 (4), 6 (3), 10 (2), 7 (1), 12 (1), 18 (1), 14 (1) |
| 79098 | 360 (97..467) | 288 | 60 | 26 (221), 14 (16), 22 (11), 8 (10), 21 (8), 15 (7), 10 (5), 5 (3), 12 (2), 6 (2), 7 (1), 18 (1), +1 more |
| 79102 | 371 (98..477) | 288 | 57 | 8 (208), 21 (37), 22 (15), 14 (8), 5 (5), 26 (5), 6 (3), 10 (3), 15 (3), 7 (1) |
| 79103 | 380 (99..481) | 293 | 72 | 21 (204), 8 (31), 22 (14), 26 (14), 10 (11), 6 (4), 5 (4), 15 (4), 7 (3), 12 (2), 14 (1), 18 (1) |
| 79105 | 379 (101..484) | 292 | 65 | 18 (232), 26 (14), 8 (14), 10 (9), 22 (8), 5 (4), 6 (4), 15 (4), 7 (3) |
| 79108 | 385 (104..492) | 295 | 74 | 15 (258), 18 (12), 10 (8), 7 (7), 5 (5), 26 (5) |
| 79110 | 388 (106..497) | 294 | 70 | 32 (198), 10 (42), 18 (25), 15 (14), 7 (4), 16 (3), 6 (3), 12 (2), 23 (2), 5 (1) |
| 79111 | 386 (109..500) | 297 | 73 | 10 (231), 32 (27), 18 (11), 15 (9), 12 (5), 6 (5), 16 (4), 5 (3), 7 (1), 23 (1) |
| 79115 | 421 (111..531) | 318 | 66 | 23 (228), 5 (37), 32 (17), 6 (15), 18 (10), 12 (4), 7 (4), 19 (1), 16 (1), 15 (1) |
| 79116 | 411 (114..530) | 323 | 60 | 6 (171), 12 (68), 5 (51), 23 (25), 19 (3), 7 (3), 18 (2) |
| 79122 | 404 (118..532) | 330 | 60 | 12 (188), 6 (89), 5 (25), 23 (22), 16 (4), 19 (2) |
| 79132 | 391 (120..515) | 290 | 79 | 5 (119), 7 (67), 23 (47), 6 (30), 12 (22), 19 (3), 16 (2) |
| 79128 | 402 (124..527) | 302 | 73 | 7 (180), 5 (72), 12 (44), 16 (3), 19 (2), 23 (1) |
| 79134 | 407 (127..533) | 313 | 73 | 30 (223), 7 (45), 16 (40), 19 (2), 12 (2), 33 (1) |
| 79135 | 409 (129..542) | 311 | 78 | 16 (212), 19 (63), 30 (33), 7 (3) |
| 79139 | 406 (132..537) | 312 | 71 | 19 (219), 16 (50), 33 (42), 30 (1) |
| 79136 | 393 (136..538) | 309 | 65 | 33 (209), 19 (51), 30 (43), 16 (6) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 286/374/1007; tracks with internal gaps: 25; total internal gaps: 251; longest internal gap: 2; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 785 | 760 | 25 | 25 | 1 | 0 | 78911 |
| 3 | 82..454 | 373 | 305 | 294 | 11 | 11 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 5 | 86..527 | 442 | 348 | 338 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 88..531 | 444 | 354 | 342 | 12 | 10 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 88..515 | 428 | 335 | 327 | 8 | 8 | 1 | 0 | 78896, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 8 | 92..477 | 386 | 319 | 308 | 11 | 10 | 2 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 92..433 | 342 | 280 | 265 | 15 | 15 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 10 | 93..500 | 408 | 335 | 320 | 15 | 15 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 11 | 96..443 | 348 | 289 | 282 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 12 | 100..529 | 430 | 350 | 340 | 10 | 9 | 1 | 1 | 79097, 79098, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 14 | 103..445 | 343 | 273 | 261 | 12 | 12 | 1 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 15 | 107..492 | 386 | 313 | 305 | 8 | 8 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 111..533 | 423 | 332 | 325 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 111..439 | 329 | 256 | 250 | 6 | 6 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 18 | 111..484 | 374 | 306 | 299 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 19 | 113..542 | 430 | 358 | 346 | 12 | 12 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 119..481 | 363 | 295 | 285 | 10 | 10 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 22 | 124..461 | 338 | 276 | 266 | 10 | 9 | 2 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 23 | 130..532 | 403 | 337 | 326 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 26 | 137..467 | 331 | 264 | 259 | 5 | 5 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 28 | 144..429 | 286 | 240 | 238 | 2 | 2 | 1 | 0 | 78896, 78969 |
| 30 | 151..536 | 386 | 317 | 300 | 17 | 17 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 31 | 155..450 | 296 | 225 | 217 | 8 | 8 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 32 | 159..497 | 339 | 253 | 242 | 11 | 10 | 2 | 0 | 79110, 79111, 79115 |
| 33 | 201..537 | 337 | 260 | 252 | 8 | 8 | 1 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 7747; unmatched reference entries: 2395; unmatched candidate entries: 258
- identity switches: 503; fragmentation (coverage interruptions): 1776; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 2 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 6 at (2128, 3029), 1 frames after previous cover
- f96: ref 79045: 3 -> 11 at (2087.5, 3033.5), 3 frames after previous cover
- f97: ref 78897: 6 -> 10 at (2107, 3033), 2 frames after previous cover
- f97: ref 79037: 10 -> 11 at (2093, 3032.5), 1 frames after previous cover
- f97: ref 79045: 11 -> 3 at (2081.5, 3032), 1 frames after previous cover
- f98: ref 79098: 7 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 10 -> 11 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 11 -> 3 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 3 -> 8 at (2068, 3033.5), 2 frames after previous cover
- f100: ref 78897: 11 -> 10 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 3 -> 11 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 7 -> 12 at (2117.5, 3029.5), 6 frames after previous cover
- f101: ref 78899: 6 -> 10 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 11 -> 3 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 12 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 5 -> 12 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 5 at (2136, 3025.5), 3 frames after previous cover
- f102: ref 78897: 10 -> 11 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 3 -> 9 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 9 -> 14 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 6 -> 10 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 12 -> 6 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 12 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 10 -> 15 at (2062.5, 3030.5), 5 frames after previous cover
- f107: ref 78971: 9 -> 3 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 3 -> 11 at (2031, 3033.5), 2 frames after previous cover
- f107: ref 79103: 6 -> 5 at (2110, 3022.5), 1 frames after previous cover
- f108: ref 78899: 15 -> 11 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 3 -> 14 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 3 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 10 -> 15 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 5 -> 6 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 5 -> 7 at (2113.5, 3025), 2 frames after previous cover
- f111: ref 78896: 14 -> 17 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 11 -> 18 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 10 -> 15 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 6 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 6 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 5 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 12 -> 16 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 18 -> 8 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 11 -> 18 at (2025, 3032), 2 frames after previous cover
- f113: ref 79037: 8 -> 3 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 3 -> 14 at (1982.5, 3034), 1 frames after previous cover
- f113: ref 79097: 15 -> 11 at (2040.5, 3031), 3 frames after previous cover
- f114: ref 79103: 6 -> 10 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 5 -> 6 at (2079, 3025), 1 frames after previous cover
- ... 443 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 760 | 190 | 0 (760) |
| 78896 | 350 (76..429) | 266 | 45 | 28 (233), 17 (21), 9 (7), 14 (4), 7 (1) |
| 78969 | 352 (80..434) | 258 | 68 | 9 (218), 17 (26), 8 (5), 28 (5), 3 (4) |
| 78971 | 352 (84..439) | 255 | 69 | 17 (195), 9 (17), 3 (15), 31 (11), 11 (7), 14 (5), 21 (5) |
| 79045 | 355 (84..443) | 277 | 56 | 11 (210), 3 (21), 9 (12), 8 (8), 14 (8), 17 (8), 21 (6), 7 (2), 6 (1), 31 (1) |
| 79037 | 355 (86..445) | 273 | 60 | 14 (198), 11 (24), 3 (19), 9 (7), 31 (7), 8 (5), 10 (4), 21 (4), 5 (2), 6 (2), 7 (1) |
| 78897 | 345 (89..450) | 259 | 62 | 31 (198), 11 (17), 3 (9), 8 (8), 14 (8), 6 (5), 21 (4), 9 (4), 10 (3), 5 (2), 18 (1) |
| 78899 | 365 (91..455) | 273 | 67 | 3 (213), 11 (14), 14 (12), 21 (10), 8 (7), 5 (5), 6 (5), 18 (3), 10 (2), 15 (1), 22 (1) |
| 79097 | 366 (94..461) | 271 | 63 | 22 (217), 3 (13), 8 (12), 11 (9), 21 (7), 15 (4), 6 (3), 10 (2), 7 (1), 12 (1), 18 (1), 14 (1) |
| 79098 | 360 (97..467) | 288 | 60 | 26 (221), 14 (16), 22 (11), 8 (10), 21 (8), 15 (7), 10 (5), 5 (3), 12 (2), 6 (2), 7 (1), 18 (1), +1 more |
| 79102 | 371 (98..477) | 288 | 57 | 8 (208), 21 (37), 22 (15), 14 (8), 5 (5), 26 (5), 6 (3), 10 (3), 15 (3), 7 (1) |
| 79103 | 380 (99..481) | 293 | 72 | 21 (204), 8 (31), 22 (14), 26 (14), 10 (11), 6 (4), 5 (4), 15 (4), 7 (3), 12 (2), 14 (1), 18 (1) |
| 79105 | 379 (101..484) | 292 | 65 | 18 (232), 26 (14), 8 (14), 10 (9), 22 (8), 5 (4), 6 (4), 15 (4), 7 (3) |
| 79108 | 385 (104..492) | 295 | 74 | 15 (258), 18 (12), 10 (8), 7 (7), 5 (5), 26 (5) |
| 79110 | 388 (106..497) | 294 | 70 | 32 (198), 10 (42), 18 (25), 15 (14), 7 (4), 16 (3), 6 (3), 12 (2), 23 (2), 5 (1) |
| 79111 | 386 (109..500) | 297 | 73 | 10 (231), 32 (27), 18 (11), 15 (9), 12 (5), 6 (5), 16 (4), 5 (3), 7 (1), 23 (1) |
| 79115 | 421 (111..531) | 318 | 66 | 23 (228), 5 (37), 32 (17), 6 (15), 18 (10), 12 (4), 7 (4), 19 (1), 16 (1), 15 (1) |
| 79116 | 411 (114..530) | 323 | 60 | 6 (171), 12 (68), 5 (51), 23 (25), 19 (3), 7 (3), 18 (2) |
| 79122 | 404 (118..532) | 330 | 60 | 12 (188), 6 (89), 5 (25), 23 (22), 16 (4), 19 (2) |
| 79132 | 391 (120..515) | 290 | 79 | 5 (119), 7 (67), 23 (47), 6 (30), 12 (22), 19 (3), 16 (2) |
| 79128 | 402 (124..527) | 302 | 73 | 7 (180), 5 (72), 12 (44), 16 (3), 19 (2), 23 (1) |
| 79134 | 407 (127..533) | 313 | 73 | 30 (223), 7 (45), 16 (40), 19 (2), 12 (2), 33 (1) |
| 79135 | 409 (129..542) | 311 | 78 | 16 (212), 19 (63), 30 (33), 7 (3) |
| 79139 | 406 (132..537) | 312 | 71 | 19 (219), 16 (50), 33 (42), 30 (1) |
| 79136 | 393 (136..538) | 309 | 65 | 33 (209), 19 (51), 30 (43), 16 (6) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 286/374/1007; tracks with internal gaps: 25; total internal gaps: 251; longest internal gap: 2; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 785 | 760 | 25 | 25 | 1 | 0 | 78911 |
| 3 | 82..454 | 373 | 305 | 294 | 11 | 11 | 1 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 5 | 86..527 | 442 | 348 | 338 | 10 | 10 | 1 | 0 | 78897, 78899, 79037, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 88..531 | 444 | 354 | 342 | 12 | 10 | 2 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 88..515 | 428 | 335 | 327 | 8 | 8 | 1 | 0 | 78896, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 8 | 92..477 | 386 | 319 | 308 | 11 | 10 | 2 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 92..433 | 342 | 280 | 265 | 15 | 15 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 10 | 93..500 | 408 | 335 | 320 | 15 | 15 | 1 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 11 | 96..443 | 348 | 289 | 282 | 7 | 7 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 12 | 100..529 | 430 | 350 | 340 | 10 | 9 | 1 | 1 | 79097, 79098, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134 |
| 14 | 103..445 | 343 | 273 | 261 | 12 | 12 | 1 | 0 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 15 | 107..492 | 386 | 313 | 305 | 8 | 8 | 1 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 111..533 | 423 | 332 | 325 | 7 | 7 | 1 | 0 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 111..439 | 329 | 256 | 250 | 6 | 6 | 1 | 0 | 78896, 78969, 78971, 79045 |
| 18 | 111..484 | 374 | 306 | 299 | 7 | 7 | 1 | 0 | 78897, 78899, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 19 | 113..542 | 430 | 358 | 346 | 12 | 12 | 1 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 119..481 | 363 | 295 | 285 | 10 | 10 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 22 | 124..461 | 338 | 276 | 266 | 10 | 9 | 2 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 23 | 130..532 | 403 | 337 | 326 | 11 | 10 | 2 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 26 | 137..467 | 331 | 264 | 259 | 5 | 5 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 28 | 144..429 | 286 | 240 | 238 | 2 | 2 | 1 | 0 | 78896, 78969 |
| 30 | 151..536 | 386 | 317 | 300 | 17 | 17 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 31 | 155..450 | 296 | 225 | 217 | 8 | 8 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 32 | 159..497 | 339 | 253 | 242 | 11 | 10 | 2 | 0 | 79110, 79111, 79115 |
| 33 | 201..537 | 337 | 260 | 252 | 8 | 8 | 1 | 0 | 79134, 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8852; unmatched reference entries: 1290; unmatched candidate entries: 1816
- identity switches: 550; fragmentation (coverage interruptions): 955; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 6 at (2128, 3029), 1 frames after previous cover
- f96: ref 79045: 3 -> 11 at (2087.5, 3033.5), 3 frames after previous cover
- f96: ref 79097: 7 -> 5 at (2141, 3029), 2 frames after previous cover
- f97: ref 78897: 6 -> 10 at (2107, 3033), 2 frames after previous cover
- f97: ref 79037: 10 -> 11 at (2093, 3032.5), 1 frames after previous cover
- f98: ref 79098: 7 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 10 -> 11 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 11 -> 3 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 8 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 11 -> 10 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 3 -> 11 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 5 -> 12 at (2117.5, 3029.5), 3 frames after previous cover
- f101: ref 78899: 6 -> 10 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 11 -> 3 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 12 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 5 -> 12 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 5 at (2136, 3025.5), 3 frames after previous cover
- f102: ref 78897: 10 -> 11 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 3 -> 9 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 9 -> 14 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 6 -> 10 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 12 -> 6 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 12 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 10 -> 15 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 9 -> 3 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 3 -> 11 at (2031, 3033.5), 1 frames after previous cover
- f107: ref 79103: 6 -> 5 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 5 -> 6 at (2118.5, 3025), 1 frames after previous cover
- f108: ref 78899: 15 -> 11 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 3 -> 14 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 3 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 10 -> 15 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 5 -> 6 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 6 -> 7 at (2113.5, 3025), 1 frames after previous cover
- f111: ref 78896: 14 -> 17 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 11 -> 18 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 10 -> 15 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 6 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 6 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 5 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 12 -> 16 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 18 -> 8 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 11 -> 18 at (2025, 3032), 1 frames after previous cover
- f113: ref 79037: 8 -> 3 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 3 -> 14 at (1982.5, 3034), 1 frames after previous cover
- f113: ref 79097: 15 -> 11 at (2040.5, 3031), 3 frames after previous cover
- f114: ref 79103: 6 -> 10 at (2069, 3023.5), 1 frames after previous cover
- ... 490 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 934 | 63 | 0 (934) |
| 78896 | 350 (76..429) | 289 | 29 | 28 (254), 17 (24), 9 (6), 14 (4), 7 (1) |
| 78969 | 352 (80..434) | 290 | 46 | 9 (248), 17 (26), 28 (7), 8 (5), 3 (4) |
| 78971 | 352 (84..439) | 294 | 40 | 17 (229), 3 (19), 9 (17), 31 (12), 11 (7), 14 (5), 21 (5) |
| 79045 | 355 (84..443) | 303 | 37 | 11 (231), 3 (19), 9 (17), 17 (11), 8 (8), 14 (7), 21 (6), 7 (2), 6 (1), 31 (1) |
| 79037 | 355 (86..445) | 311 | 32 | 14 (228), 11 (26), 3 (22), 9 (8), 31 (8), 8 (5), 10 (4), 21 (4), 5 (3), 6 (2), 7 (1) |
| 78897 | 345 (89..450) | 290 | 38 | 31 (224), 11 (18), 14 (10), 8 (8), 3 (7), 21 (6), 6 (5), 9 (4), 10 (3), 5 (2), 17 (2), 18 (1) |
| 78899 | 365 (91..455) | 320 | 33 | 3 (251), 11 (18), 14 (12), 21 (11), 8 (7), 5 (5), 6 (5), 10 (3), 18 (3), 31 (3), 15 (1), 22 (1) |
| 79097 | 366 (94..461) | 298 | 44 | 22 (238), 3 (15), 8 (13), 11 (10), 21 (7), 15 (4), 6 (3), 5 (2), 10 (2), 7 (1), 12 (1), 18 (1), +1 more |
| 79098 | 360 (97..467) | 323 | 33 | 26 (250), 14 (18), 22 (12), 8 (11), 15 (8), 21 (8), 10 (5), 5 (3), 12 (2), 6 (2), 18 (2), 7 (1), +1 more |
| 79102 | 371 (98..477) | 320 | 35 | 8 (238), 21 (40), 22 (14), 14 (8), 5 (5), 26 (5), 6 (3), 10 (3), 15 (3), 7 (1) |
| 79103 | 380 (99..481) | 335 | 35 | 21 (240), 8 (37), 22 (14), 26 (14), 10 (12), 6 (4), 5 (4), 15 (4), 7 (3), 12 (2), 14 (1) |
| 79105 | 379 (101..484) | 333 | 34 | 18 (267), 26 (15), 8 (14), 10 (9), 22 (9), 6 (6), 5 (4), 15 (4), 7 (3), 21 (2) |
| 79108 | 385 (104..492) | 329 | 46 | 15 (290), 18 (13), 10 (8), 7 (7), 26 (6), 5 (5) |
| 79110 | 388 (106..497) | 336 | 41 | 32 (239), 10 (41), 18 (25), 15 (16), 7 (5), 16 (3), 6 (3), 12 (2), 23 (2) |
| 79111 | 386 (109..500) | 348 | 31 | 10 (269), 32 (37), 18 (12), 15 (9), 12 (5), 16 (5), 6 (5), 5 (4), 7 (1), 23 (1) |
| 79115 | 421 (111..531) | 356 | 42 | 23 (259), 5 (38), 32 (20), 6 (16), 18 (11), 12 (4), 7 (4), 19 (1), 16 (1), 15 (1), 10 (1) |
| 79116 | 411 (114..530) | 369 | 31 | 6 (192), 12 (77), 5 (61), 23 (27), 19 (4), 7 (3), 18 (3), 32 (2) |
| 79122 | 404 (118..532) | 366 | 30 | 12 (208), 6 (103), 5 (26), 23 (23), 16 (4), 19 (2) |
| 79132 | 391 (120..515) | 346 | 37 | 5 (151), 7 (79), 23 (53), 6 (34), 12 (24), 19 (3), 16 (2) |
| 79128 | 402 (124..527) | 349 | 39 | 7 (212), 5 (82), 12 (49), 16 (3), 19 (2), 23 (1) |
| 79134 | 407 (127..533) | 357 | 40 | 30 (259), 7 (48), 16 (46), 19 (2), 12 (2) |
| 79135 | 409 (129..542) | 360 | 37 | 16 (248), 19 (69), 30 (39), 7 (4) |
| 79139 | 406 (132..537) | 356 | 37 | 19 (245), 16 (61), 30 (46), 12 (2), 33 (1), 5 (1) |
| 79136 | 393 (136..538) | 340 | 45 | 33 (286), 19 (53), 16 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 315/403/1007; tracks with internal gaps: 25; total internal gaps: 896; longest internal gap: 10; tracks ending in coasting: 24 (trailing rows total 641)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 934 | 73 | 63 | 3 | 0 | 78911 |
| 3 | 82..483 | 402 | 402 | 337 | 65 | 28 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 5 | 86..556 | 471 | 471 | 396 | 75 | 39 | 6 | 19 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 6 | 88..560 | 473 | 473 | 384 | 89 | 37 | 5 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 88..544 | 457 | 457 | 376 | 81 | 42 | 10 | 11 | 78896, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 8 | 92..506 | 415 | 415 | 346 | 69 | 31 | 3 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 92..462 | 371 | 371 | 300 | 71 | 38 | 6 | 19 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 10 | 93..529 | 437 | 437 | 360 | 77 | 37 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 11 | 96..472 | 377 | 377 | 311 | 66 | 27 | 4 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 12 | 100..558 | 459 | 459 | 378 | 81 | 41 | 6 | 22 | 79097, 79098, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 14 | 103..474 | 372 | 372 | 294 | 78 | 37 | 4 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 15 | 107..521 | 415 | 415 | 340 | 75 | 39 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 111..562 | 452 | 452 | 374 | 78 | 38 | 3 | 31 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 111..468 | 358 | 358 | 292 | 66 | 34 | 9 | 18 | 78896, 78897, 78969, 78971, 79045 |
| 18 | 111..513 | 403 | 403 | 338 | 65 | 30 | 3 | 29 | 78897, 78899, 79097, 79098, 79105, 79108, 79110, 79111, 79115, 79116 |
| 19 | 113..571 | 459 | 459 | 381 | 78 | 40 | 3 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 119..510 | 392 | 392 | 329 | 63 | 27 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 22 | 124..490 | 367 | 367 | 288 | 79 | 33 | 4 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 23 | 130..561 | 432 | 432 | 366 | 66 | 29 | 3 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 26 | 137..496 | 360 | 360 | 290 | 70 | 34 | 4 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 28 | 144..458 | 315 | 315 | 261 | 54 | 24 | 2 | 29 | 78896, 78969 |
| 30 | 151..565 | 415 | 415 | 344 | 71 | 33 | 3 | 31 | 79134, 79135, 79139 |
| 31 | 155..479 | 325 | 325 | 248 | 77 | 39 | 6 | 24 | 78897, 78899, 78971, 79037, 79045 |
| 32 | 159..526 | 368 | 368 | 298 | 70 | 32 | 4 | 29 | 79110, 79111, 79115, 79116 |
| 33 | 201..566 | 366 | 366 | 287 | 79 | 44 | 3 | 28 | 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8852; unmatched reference entries: 1290; unmatched candidate entries: 1816
- identity switches: 550; fragmentation (coverage interruptions): 955; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f89: ref 79037: 5 -> 6 at (2141, 3034.5), 1 frames after previous cover
- f89: ref 79045: 6 -> 7 at (2129.5, 3032), 1 frames after previous cover
- f91: ref 78897: 5 -> 6 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 6 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f92: ref 78896: 7 -> 9 at (2059, 3033.5), 4 frames after previous cover
- f92: ref 78969: 3 -> 8 at (2083, 3033), 5 frames after previous cover
- f92: ref 79045: 7 -> 3 at (2110.5, 3033.5), 2 frames after previous cover
- f93: ref 79037: 7 -> 10 at (2118, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 6 at (2128, 3029), 1 frames after previous cover
- f96: ref 79045: 3 -> 11 at (2087.5, 3033.5), 3 frames after previous cover
- f96: ref 79097: 7 -> 5 at (2141, 3029), 2 frames after previous cover
- f97: ref 78897: 6 -> 10 at (2107, 3033), 2 frames after previous cover
- f97: ref 79037: 10 -> 11 at (2093, 3032.5), 1 frames after previous cover
- f98: ref 79098: 7 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78897: 10 -> 11 at (2094.5, 3030.5), 1 frames after previous cover
- f99: ref 79037: 11 -> 3 at (2080, 3034.5), 1 frames after previous cover
- f99: ref 79045: 11 -> 8 at (2068, 3033.5), 3 frames after previous cover
- f100: ref 78897: 11 -> 10 at (2088.5, 3033.5), 1 frames after previous cover
- f100: ref 78969: 8 -> 9 at (2033.5, 3034), 2 frames after previous cover
- f100: ref 79037: 3 -> 11 at (2076, 3033.5), 1 frames after previous cover
- f100: ref 79097: 5 -> 12 at (2117.5, 3029.5), 3 frames after previous cover
- f101: ref 78899: 6 -> 10 at (2098.5, 3030.5), 1 frames after previous cover
- f101: ref 79037: 11 -> 3 at (2068.5, 3034.5), 1 frames after previous cover
- f101: ref 79097: 12 -> 6 at (2111.5, 3028.5), 1 frames after previous cover
- f101: ref 79098: 5 -> 12 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 7 -> 5 at (2136, 3025.5), 3 frames after previous cover
- f102: ref 78897: 10 -> 11 at (2077, 3031.5), 2 frames after previous cover
- f103: ref 78971: 3 -> 9 at (2033, 3032.5), 5 frames after previous cover
- f104: ref 78896: 9 -> 14 at (1984, 3034.5), 7 frames after previous cover
- f104: ref 79097: 6 -> 10 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 12 -> 6 at (2107, 3027.5), 2 frames after previous cover
- f104: ref 79103: 7 -> 12 at (2126, 3022.5), 3 frames after previous cover
- f106: ref 79098: 6 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 12 -> 6 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 7 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78899: 10 -> 15 at (2062.5, 3030.5), 4 frames after previous cover
- f107: ref 78971: 9 -> 3 at (2009.5, 3033), 2 frames after previous cover
- f107: ref 79037: 3 -> 11 at (2031, 3033.5), 1 frames after previous cover
- f107: ref 79103: 6 -> 5 at (2110, 3022.5), 1 frames after previous cover
- f107: ref 79105: 5 -> 6 at (2118.5, 3025), 1 frames after previous cover
- f108: ref 78899: 15 -> 11 at (2055.5, 3031), 1 frames after previous cover
- f108: ref 78971: 3 -> 14 at (2003.5, 3034.5), 1 frames after previous cover
- f108: ref 79037: 11 -> 8 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 8 -> 3 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 10 -> 15 at (2070, 3029.5), 3 frames after previous cover
- f108: ref 79102: 5 -> 6 at (2096.5, 3027.5), 3 frames after previous cover
- f108: ref 79105: 6 -> 7 at (2113.5, 3025), 1 frames after previous cover
- f111: ref 78896: 14 -> 17 at (1939.5, 3034), 4 frames after previous cover
- f111: ref 78897: 11 -> 18 at (2021.5, 3032.5), 5 frames after previous cover
- f111: ref 79098: 10 -> 15 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 6 -> 10 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 5 -> 6 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 5 at (2096.5, 3025), 3 frames after previous cover
- f111: ref 79110: 12 -> 16 at (2129, 3027), 3 frames after previous cover
- f113: ref 78897: 18 -> 8 at (2008.5, 3033.5), 2 frames after previous cover
- f113: ref 78899: 11 -> 18 at (2025, 3032), 1 frames after previous cover
- f113: ref 79037: 8 -> 3 at (1995, 3034.5), 1 frames after previous cover
- f113: ref 79045: 3 -> 14 at (1982.5, 3034), 1 frames after previous cover
- f113: ref 79097: 15 -> 11 at (2040.5, 3031), 3 frames after previous cover
- f114: ref 79103: 6 -> 10 at (2069, 3023.5), 1 frames after previous cover
- ... 490 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 934 | 63 | 0 (934) |
| 78896 | 350 (76..429) | 289 | 29 | 28 (254), 17 (24), 9 (6), 14 (4), 7 (1) |
| 78969 | 352 (80..434) | 290 | 46 | 9 (248), 17 (26), 28 (7), 8 (5), 3 (4) |
| 78971 | 352 (84..439) | 294 | 40 | 17 (229), 3 (19), 9 (17), 31 (12), 11 (7), 14 (5), 21 (5) |
| 79045 | 355 (84..443) | 303 | 37 | 11 (231), 3 (19), 9 (17), 17 (11), 8 (8), 14 (7), 21 (6), 7 (2), 6 (1), 31 (1) |
| 79037 | 355 (86..445) | 311 | 32 | 14 (228), 11 (26), 3 (22), 9 (8), 31 (8), 8 (5), 10 (4), 21 (4), 5 (3), 6 (2), 7 (1) |
| 78897 | 345 (89..450) | 290 | 38 | 31 (224), 11 (18), 14 (10), 8 (8), 3 (7), 21 (6), 6 (5), 9 (4), 10 (3), 5 (2), 17 (2), 18 (1) |
| 78899 | 365 (91..455) | 320 | 33 | 3 (251), 11 (18), 14 (12), 21 (11), 8 (7), 5 (5), 6 (5), 10 (3), 18 (3), 31 (3), 15 (1), 22 (1) |
| 79097 | 366 (94..461) | 298 | 44 | 22 (238), 3 (15), 8 (13), 11 (10), 21 (7), 15 (4), 6 (3), 5 (2), 10 (2), 7 (1), 12 (1), 18 (1), +1 more |
| 79098 | 360 (97..467) | 323 | 33 | 26 (250), 14 (18), 22 (12), 8 (11), 15 (8), 21 (8), 10 (5), 5 (3), 12 (2), 6 (2), 18 (2), 7 (1), +1 more |
| 79102 | 371 (98..477) | 320 | 35 | 8 (238), 21 (40), 22 (14), 14 (8), 5 (5), 26 (5), 6 (3), 10 (3), 15 (3), 7 (1) |
| 79103 | 380 (99..481) | 335 | 35 | 21 (240), 8 (37), 22 (14), 26 (14), 10 (12), 6 (4), 5 (4), 15 (4), 7 (3), 12 (2), 14 (1) |
| 79105 | 379 (101..484) | 333 | 34 | 18 (267), 26 (15), 8 (14), 10 (9), 22 (9), 6 (6), 5 (4), 15 (4), 7 (3), 21 (2) |
| 79108 | 385 (104..492) | 329 | 46 | 15 (290), 18 (13), 10 (8), 7 (7), 26 (6), 5 (5) |
| 79110 | 388 (106..497) | 336 | 41 | 32 (239), 10 (41), 18 (25), 15 (16), 7 (5), 16 (3), 6 (3), 12 (2), 23 (2) |
| 79111 | 386 (109..500) | 348 | 31 | 10 (269), 32 (37), 18 (12), 15 (9), 12 (5), 16 (5), 6 (5), 5 (4), 7 (1), 23 (1) |
| 79115 | 421 (111..531) | 356 | 42 | 23 (259), 5 (38), 32 (20), 6 (16), 18 (11), 12 (4), 7 (4), 19 (1), 16 (1), 15 (1), 10 (1) |
| 79116 | 411 (114..530) | 369 | 31 | 6 (192), 12 (77), 5 (61), 23 (27), 19 (4), 7 (3), 18 (3), 32 (2) |
| 79122 | 404 (118..532) | 366 | 30 | 12 (208), 6 (103), 5 (26), 23 (23), 16 (4), 19 (2) |
| 79132 | 391 (120..515) | 346 | 37 | 5 (151), 7 (79), 23 (53), 6 (34), 12 (24), 19 (3), 16 (2) |
| 79128 | 402 (124..527) | 349 | 39 | 7 (212), 5 (82), 12 (49), 16 (3), 19 (2), 23 (1) |
| 79134 | 407 (127..533) | 357 | 40 | 30 (259), 7 (48), 16 (46), 19 (2), 12 (2) |
| 79135 | 409 (129..542) | 360 | 37 | 16 (248), 19 (69), 30 (39), 7 (4) |
| 79139 | 406 (132..537) | 356 | 37 | 19 (245), 16 (61), 30 (46), 12 (2), 33 (1), 5 (1) |
| 79136 | 393 (136..538) | 340 | 45 | 33 (286), 19 (53), 16 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 315/403/1007; tracks with internal gaps: 25; total internal gaps: 896; longest internal gap: 10; tracks ending in coasting: 24 (trailing rows total 641)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 934 | 73 | 63 | 3 | 0 | 78911 |
| 3 | 82..483 | 402 | 402 | 337 | 65 | 28 | 3 | 29 | 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 5 | 86..556 | 471 | 471 | 396 | 75 | 39 | 6 | 19 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79115, 79116, 79122, 79128, 79132, 79139 |
| 6 | 88..560 | 473 | 473 | 384 | 89 | 37 | 5 | 28 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132 |
| 7 | 88..544 | 457 | 457 | 376 | 81 | 42 | 10 | 11 | 78896, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79128, 79132, 79134, 79135 |
| 8 | 92..506 | 415 | 415 | 346 | 69 | 31 | 3 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 9 | 92..462 | 371 | 371 | 300 | 71 | 38 | 6 | 19 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 10 | 93..529 | 437 | 437 | 360 | 77 | 37 | 4 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 11 | 96..472 | 377 | 377 | 311 | 66 | 27 | 4 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 12 | 100..558 | 459 | 459 | 378 | 81 | 41 | 6 | 22 | 79097, 79098, 79103, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79139 |
| 14 | 103..474 | 372 | 372 | 294 | 78 | 37 | 4 | 29 | 78896, 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103 |
| 15 | 107..521 | 415 | 415 | 340 | 75 | 39 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 16 | 111..562 | 452 | 452 | 374 | 78 | 38 | 3 | 31 | 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 111..468 | 358 | 358 | 292 | 66 | 34 | 9 | 18 | 78896, 78897, 78969, 78971, 79045 |
| 18 | 111..513 | 403 | 403 | 338 | 65 | 30 | 3 | 29 | 78897, 78899, 79097, 79098, 79105, 79108, 79110, 79111, 79115, 79116 |
| 19 | 113..571 | 459 | 459 | 381 | 78 | 40 | 3 | 29 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 119..510 | 392 | 392 | 329 | 63 | 27 | 3 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105 |
| 22 | 124..490 | 367 | 367 | 288 | 79 | 33 | 4 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 23 | 130..561 | 432 | 432 | 366 | 66 | 29 | 3 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 26 | 137..496 | 360 | 360 | 290 | 70 | 34 | 4 | 29 | 79098, 79102, 79103, 79105, 79108 |
| 28 | 144..458 | 315 | 315 | 261 | 54 | 24 | 2 | 29 | 78896, 78969 |
| 30 | 151..565 | 415 | 415 | 344 | 71 | 33 | 3 | 31 | 79134, 79135, 79139 |
| 31 | 155..479 | 325 | 325 | 248 | 77 | 39 | 6 | 24 | 78897, 78899, 78971, 79037, 79045 |
| 32 | 159..526 | 368 | 368 | 298 | 70 | 32 | 4 | 29 | 79110, 79111, 79115, 79116 |
| 33 | 201..566 | 366 | 366 | 287 | 79 | 44 | 3 | 28 | 79136, 79139 |
