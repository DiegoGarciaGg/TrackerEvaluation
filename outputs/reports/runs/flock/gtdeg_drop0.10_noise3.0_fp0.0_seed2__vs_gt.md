# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=d53e856b6f0c
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise3.0_fp0.0_seed2/tracks.csv sha256=ea2d62a934f9d1e0
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise3.0_fp0.0_seed2.csv sha256=d53e856b6f0ce853
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise3.0_fp0.0_seed2
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
| observations | none | 4 | 10142 | 9024 | 0.323 | 0.389 | 0.268 | 2.20 | 0.310 | 0.113 | 2.43 | 290 | 2504.0 | 0.440 | 0.468 | 0.416 | 0.516 | 0.580 | 5232 | 4910 | 3792 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 9024 | 0.458 | 0.544 | 0.386 | 2.77 | 0.553 | 0.614 | 3.23 | 317 | 1813.0 | 0.660 | 0.701 | 0.624 | 0.767 | 0.862 | 7783 | 2359 | 1241 | 2 | 23 | 0 |
| observations | none | 8 | 10142 | 9024 | 0.534 | 0.615 | 0.463 | 3.13 | 0.671 | 0.800 | 3.64 | 327 | 1194.0 | 0.749 | 0.796 | 0.708 | 0.861 | 0.968 | 8731 | 1411 | 293 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 9024 | 0.614 | 0.686 | 0.550 | 3.65 | 0.730 | 0.855 | 3.88 | 264 | 997.0 | 0.803 | 0.853 | 0.759 | 0.886 | 0.995 | 8981 | 1161 | 43 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 9024 | 0.323 | 0.389 | 0.268 | 2.20 | 0.310 | 0.113 | 2.43 | 290 | 2504.0 | 0.440 | 0.468 | 0.416 | 0.516 | 0.580 | 5232 | 4910 | 3792 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 9024 | 0.458 | 0.544 | 0.386 | 2.77 | 0.553 | 0.614 | 3.23 | 317 | 1813.0 | 0.660 | 0.701 | 0.624 | 0.767 | 0.862 | 7783 | 2359 | 1241 | 2 | 23 | 0 |
| observations | ignore | 8 | 10142 | 9024 | 0.534 | 0.615 | 0.463 | 3.13 | 0.671 | 0.800 | 3.64 | 327 | 1194.0 | 0.749 | 0.796 | 0.708 | 0.861 | 0.968 | 8731 | 1411 | 293 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 9024 | 0.614 | 0.686 | 0.550 | 3.65 | 0.730 | 0.855 | 3.88 | 264 | 997.0 | 0.803 | 0.853 | 0.759 | 0.886 | 0.995 | 8981 | 1161 | 43 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10836 | 0.306 | 0.365 | 0.256 | 2.22 | 0.289 | -0.030 | 2.44 | 343 | 2484.0 | 0.417 | 0.403 | 0.431 | 0.536 | 0.502 | 5438 | 4704 | 5398 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10836 | 0.446 | 0.523 | 0.380 | 2.84 | 0.522 | 0.513 | 3.27 | 356 | 1548.0 | 0.637 | 0.616 | 0.659 | 0.808 | 0.756 | 8196 | 1946 | 2640 | 15 | 10 | 0 |
| updates | none | 8 | 10142 | 10836 | 0.529 | 0.604 | 0.464 | 3.25 | 0.653 | 0.743 | 3.74 | 336 | 707.0 | 0.738 | 0.714 | 0.763 | 0.922 | 0.863 | 9355 | 787 | 1481 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10836 | 0.620 | 0.689 | 0.559 | 3.83 | 0.743 | 0.852 | 4.14 | 248 | 287.0 | 0.812 | 0.786 | 0.840 | 0.972 | 0.910 | 9860 | 282 | 976 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10836 | 0.306 | 0.365 | 0.256 | 2.22 | 0.289 | -0.030 | 2.44 | 343 | 2484.0 | 0.417 | 0.403 | 0.431 | 0.536 | 0.502 | 5438 | 4704 | 5398 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10836 | 0.446 | 0.523 | 0.380 | 2.84 | 0.522 | 0.513 | 3.27 | 356 | 1548.0 | 0.637 | 0.616 | 0.659 | 0.808 | 0.756 | 8196 | 1946 | 2640 | 15 | 10 | 0 |
| updates | ignore | 8 | 10142 | 10836 | 0.529 | 0.604 | 0.464 | 3.25 | 0.653 | 0.743 | 3.74 | 336 | 707.0 | 0.738 | 0.714 | 0.763 | 0.922 | 0.863 | 9355 | 787 | 1481 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10836 | 0.620 | 0.689 | 0.559 | 3.83 | 0.743 | 0.852 | 4.14 | 248 | 287.0 | 0.812 | 0.786 | 0.840 | 0.972 | 0.910 | 9860 | 282 | 976 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8731; unmatched reference entries: 1411; unmatched candidate entries: 293
- identity switches: 327; fragmentation (coverage interruptions): 1152; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 7 -> 13 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 13 -> 14 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 7 -> 15 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 6 -> 13 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 13 -> 6 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 15 -> 10 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 10 -> 19 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 18 -> 20 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 15 -> 10 at (2107.5, 3023.5), 2 frames after previous cover
- f109: ref 79108: 18 -> 15 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 14 -> 6 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 6 -> 14 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 11 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78969: 8 -> 3 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 13 -> 8 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 14 -> 13 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 19 -> 17 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 10 -> 19 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 10 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 15 -> 10 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 20 -> 15 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 18 -> 20 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 14 -> 11 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 11 -> 16 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 3 -> 8 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 8 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 6 -> 14 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 13 -> 6 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 19 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 19 -> 10 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 10 -> 15 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 15 -> 20 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 15 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 20 -> 15 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79115: 18 -> 20 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 7 -> 22 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 21 -> 10 at (2073, 3025), 3 frames after previous cover
- f115: ref 79108: 21 -> 7 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 15 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 20 -> 15 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 11 -> 14 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 78899: 16 -> 11 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 17 -> 16 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 19 -> 17 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 10 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- f118: ref 78971: 13 -> 6 at (1940.5, 3036), 1 frames after previous cover
- f119: ref 78897: 14 -> 11 at (1972.5, 3034.5), 3 frames after previous cover
- ... 267 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 887 | 102 | 2 (887) |
| 78896 | 350 (76..429) | 302 | 38 | 25 (259), 3 (43) |
| 78969 | 352 (80..434) | 289 | 48 | 28 (247), 8 (32), 3 (10) |
| 78971 | 352 (84..439) | 309 | 33 | 8 (275), 6 (20), 13 (13), 3 (1) |
| 79045 | 355 (84..443) | 296 | 43 | 29 (183), 3 (76), 6 (23), 13 (8), 7 (2), 14 (2), 8 (2) |
| 79037 | 355 (86..445) | 297 | 48 | 3 (118), 6 (76), 29 (66), 14 (30), 11 (3), 13 (2), 7 (1), 10 (1) |
| 78897 | 345 (89..450) | 304 | 33 | 6 (192), 3 (76), 11 (22), 14 (4), 13 (4), 10 (3), 7 (2), 26 (1) |
| 78899 | 365 (91..455) | 315 | 43 | 14 (277), 16 (16), 11 (12), 7 (3), 10 (3), 6 (3), 13 (1) |
| 79097 | 366 (94..461) | 314 | 42 | 11 (277), 17 (18), 13 (8), 16 (6), 7 (3), 10 (2) |
| 79098 | 360 (97..467) | 303 | 49 | 13 (273), 19 (9), 17 (8), 10 (5), 16 (3), 11 (2), 7 (1), 26 (1), 14 (1) |
| 79102 | 371 (98..477) | 314 | 46 | 26 (290), 10 (6), 19 (6), 17 (5), 15 (4), 13 (2), 7 (1) |
| 79103 | 380 (99..481) | 334 | 43 | 17 (303), 7 (14), 22 (8), 19 (4), 16 (3), 26 (2) |
| 79105 | 379 (101..484) | 320 | 46 | 16 (297), 10 (10), 15 (4), 19 (4), 21 (2), 7 (1), 22 (1), 17 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 19 (312), 7 (11), 30 (7), 21 (4), 15 (3), 10 (3), 22 (2), 18 (1), 16 (1) |
| 79110 | 388 (106..497) | 326 | 51 | 30 (278), 10 (14), 19 (10), 22 (6), 20 (5), 15 (4), 21 (4), 7 (4), 18 (1) |
| 79111 | 386 (109..500) | 331 | 43 | 22 (227), 10 (81), 30 (8), 15 (4), 21 (4), 18 (3), 20 (3), 7 (1) |
| 79115 | 421 (111..531) | 355 | 51 | 10 (180), 7 (87), 22 (55), 20 (26), 18 (3), 21 (3), 30 (1) |
| 79116 | 411 (114..530) | 361 | 43 | 7 (109), 21 (84), 10 (60), 20 (51), 22 (34), 15 (19), 18 (4) |
| 79122 | 404 (118..532) | 338 | 51 | 21 (218), 20 (85), 10 (19), 18 (7), 15 (3), 22 (3), 7 (2), 23 (1) |
| 79132 | 391 (120..515) | 338 | 43 | 20 (172), 7 (120), 21 (32), 15 (7), 23 (4), 18 (3) |
| 79128 | 402 (124..527) | 349 | 44 | 15 (321), 20 (18), 18 (6), 23 (3), 24 (1) |
| 79134 | 407 (127..533) | 351 | 45 | 18 (326), 27 (10), 24 (8), 23 (7) |
| 79135 | 409 (129..542) | 352 | 49 | 23 (341), 24 (10), 18 (1) |
| 79139 | 406 (132..537) | 364 | 36 | 24 (322), 27 (27), 18 (12), 23 (3) |
| 79136 | 393 (136..538) | 338 | 47 | 27 (297), 24 (39), 18 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 299/385/1003; tracks with internal gaps: 25; total internal gaps: 278; longest internal gap: 2; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 910 | 887 | 23 | 21 | 2 | 0 | 78911 |
| 3 | 78..449 | 372 | 330 | 324 | 6 | 6 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 6 | 86..445 | 360 | 319 | 314 | 5 | 5 | 1 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 86..515 | 430 | 380 | 362 | 18 | 18 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 8 | 88..439 | 352 | 317 | 309 | 8 | 8 | 1 | 0 | 78969, 78971, 79045 |
| 10 | 90..532 | 443 | 398 | 387 | 11 | 10 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 91..461 | 371 | 332 | 316 | 16 | 15 | 2 | 0 | 78897, 78899, 79037, 79097, 79098 |
| 13 | 95..467 | 373 | 324 | 311 | 13 | 13 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 14 | 98..455 | 358 | 332 | 314 | 18 | 18 | 1 | 0 | 78897, 78899, 79037, 79045, 79098 |
| 15 | 100..527 | 428 | 379 | 369 | 10 | 9 | 2 | 0 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 16 | 100..484 | 385 | 342 | 326 | 16 | 16 | 1 | 0 | 78899, 79097, 79098, 79103, 79105, 79108 |
| 17 | 101..481 | 381 | 345 | 335 | 10 | 10 | 1 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 18 | 105..533 | 429 | 379 | 369 | 10 | 9 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 106..492 | 387 | 346 | 345 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 20 | 108..528 | 421 | 375 | 360 | 15 | 13 | 2 | 1 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..530 | 420 | 362 | 351 | 11 | 9 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 115..500 | 386 | 346 | 336 | 10 | 9 | 2 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 23 | 122..542 | 421 | 373 | 359 | 14 | 12 | 2 | 0 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 126..538 | 413 | 388 | 380 | 8 | 8 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 25 | 127..429 | 303 | 269 | 259 | 10 | 10 | 1 | 0 | 78896 |
| 26 | 132..477 | 346 | 308 | 294 | 14 | 13 | 2 | 0 | 78897, 79098, 79102, 79103 |
| 27 | 135..537 | 403 | 351 | 334 | 17 | 17 | 1 | 0 | 79134, 79136, 79139 |
| 28 | 136..434 | 299 | 252 | 247 | 5 | 5 | 1 | 0 | 78969 |
| 29 | 142..443 | 302 | 262 | 249 | 13 | 12 | 2 | 0 | 79037, 79045 |
| 30 | 144..497 | 354 | 305 | 294 | 11 | 11 | 1 | 0 | 79108, 79110, 79111, 79115 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8731; unmatched reference entries: 1411; unmatched candidate entries: 293
- identity switches: 327; fragmentation (coverage interruptions): 1152; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 7 -> 13 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 13 -> 14 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 7 -> 15 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 6 -> 13 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 13 -> 6 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 15 -> 10 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 10 -> 19 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 18 -> 20 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 15 -> 10 at (2107.5, 3023.5), 2 frames after previous cover
- f109: ref 79108: 18 -> 15 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 14 -> 6 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 6 -> 14 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 11 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 2 frames after previous cover
- f111: ref 78969: 8 -> 3 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 13 -> 8 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 14 -> 13 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 19 -> 17 at (2065.5, 3029), 2 frames after previous cover
- f111: ref 79102: 10 -> 19 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 10 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 15 -> 10 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 20 -> 15 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 18 -> 20 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 14 -> 11 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 11 -> 16 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 3 -> 8 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 8 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 6 -> 14 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 13 -> 6 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 19 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 19 -> 10 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 10 -> 15 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 15 -> 20 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 15 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 20 -> 15 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79115: 18 -> 20 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 7 -> 22 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 21 -> 10 at (2073, 3025), 3 frames after previous cover
- f115: ref 79108: 21 -> 7 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 15 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 20 -> 15 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 11 -> 14 at (1990.5, 3033.5), 2 frames after previous cover
- f116: ref 78899: 16 -> 11 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 17 -> 16 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 19 -> 17 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 10 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- f118: ref 78971: 13 -> 6 at (1940.5, 3036), 1 frames after previous cover
- f119: ref 78897: 14 -> 11 at (1972.5, 3034.5), 3 frames after previous cover
- ... 267 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 887 | 102 | 2 (887) |
| 78896 | 350 (76..429) | 302 | 38 | 25 (259), 3 (43) |
| 78969 | 352 (80..434) | 289 | 48 | 28 (247), 8 (32), 3 (10) |
| 78971 | 352 (84..439) | 309 | 33 | 8 (275), 6 (20), 13 (13), 3 (1) |
| 79045 | 355 (84..443) | 296 | 43 | 29 (183), 3 (76), 6 (23), 13 (8), 7 (2), 14 (2), 8 (2) |
| 79037 | 355 (86..445) | 297 | 48 | 3 (118), 6 (76), 29 (66), 14 (30), 11 (3), 13 (2), 7 (1), 10 (1) |
| 78897 | 345 (89..450) | 304 | 33 | 6 (192), 3 (76), 11 (22), 14 (4), 13 (4), 10 (3), 7 (2), 26 (1) |
| 78899 | 365 (91..455) | 315 | 43 | 14 (277), 16 (16), 11 (12), 7 (3), 10 (3), 6 (3), 13 (1) |
| 79097 | 366 (94..461) | 314 | 42 | 11 (277), 17 (18), 13 (8), 16 (6), 7 (3), 10 (2) |
| 79098 | 360 (97..467) | 303 | 49 | 13 (273), 19 (9), 17 (8), 10 (5), 16 (3), 11 (2), 7 (1), 26 (1), 14 (1) |
| 79102 | 371 (98..477) | 314 | 46 | 26 (290), 10 (6), 19 (6), 17 (5), 15 (4), 13 (2), 7 (1) |
| 79103 | 380 (99..481) | 334 | 43 | 17 (303), 7 (14), 22 (8), 19 (4), 16 (3), 26 (2) |
| 79105 | 379 (101..484) | 320 | 46 | 16 (297), 10 (10), 15 (4), 19 (4), 21 (2), 7 (1), 22 (1), 17 (1) |
| 79108 | 385 (104..492) | 344 | 35 | 19 (312), 7 (11), 30 (7), 21 (4), 15 (3), 10 (3), 22 (2), 18 (1), 16 (1) |
| 79110 | 388 (106..497) | 326 | 51 | 30 (278), 10 (14), 19 (10), 22 (6), 20 (5), 15 (4), 21 (4), 7 (4), 18 (1) |
| 79111 | 386 (109..500) | 331 | 43 | 22 (227), 10 (81), 30 (8), 15 (4), 21 (4), 18 (3), 20 (3), 7 (1) |
| 79115 | 421 (111..531) | 355 | 51 | 10 (180), 7 (87), 22 (55), 20 (26), 18 (3), 21 (3), 30 (1) |
| 79116 | 411 (114..530) | 361 | 43 | 7 (109), 21 (84), 10 (60), 20 (51), 22 (34), 15 (19), 18 (4) |
| 79122 | 404 (118..532) | 338 | 51 | 21 (218), 20 (85), 10 (19), 18 (7), 15 (3), 22 (3), 7 (2), 23 (1) |
| 79132 | 391 (120..515) | 338 | 43 | 20 (172), 7 (120), 21 (32), 15 (7), 23 (4), 18 (3) |
| 79128 | 402 (124..527) | 349 | 44 | 15 (321), 20 (18), 18 (6), 23 (3), 24 (1) |
| 79134 | 407 (127..533) | 351 | 45 | 18 (326), 27 (10), 24 (8), 23 (7) |
| 79135 | 409 (129..542) | 352 | 49 | 23 (341), 24 (10), 18 (1) |
| 79139 | 406 (132..537) | 364 | 36 | 24 (322), 27 (27), 18 (12), 23 (3) |
| 79136 | 393 (136..538) | 338 | 47 | 27 (297), 24 (39), 18 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 299/385/1003; tracks with internal gaps: 25; total internal gaps: 278; longest internal gap: 2; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 910 | 887 | 23 | 21 | 2 | 0 | 78911 |
| 3 | 78..449 | 372 | 330 | 324 | 6 | 6 | 1 | 0 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 6 | 86..445 | 360 | 319 | 314 | 5 | 5 | 1 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 86..515 | 430 | 380 | 362 | 18 | 18 | 1 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 8 | 88..439 | 352 | 317 | 309 | 8 | 8 | 1 | 0 | 78969, 78971, 79045 |
| 10 | 90..532 | 443 | 398 | 387 | 11 | 10 | 2 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 91..461 | 371 | 332 | 316 | 16 | 15 | 2 | 0 | 78897, 78899, 79037, 79097, 79098 |
| 13 | 95..467 | 373 | 324 | 311 | 13 | 13 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 14 | 98..455 | 358 | 332 | 314 | 18 | 18 | 1 | 0 | 78897, 78899, 79037, 79045, 79098 |
| 15 | 100..527 | 428 | 379 | 369 | 10 | 9 | 2 | 0 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 16 | 100..484 | 385 | 342 | 326 | 16 | 16 | 1 | 0 | 78899, 79097, 79098, 79103, 79105, 79108 |
| 17 | 101..481 | 381 | 345 | 335 | 10 | 10 | 1 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 18 | 105..533 | 429 | 379 | 369 | 10 | 9 | 2 | 0 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 106..492 | 387 | 346 | 345 | 1 | 1 | 1 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 20 | 108..528 | 421 | 375 | 360 | 15 | 13 | 2 | 1 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..530 | 420 | 362 | 351 | 11 | 9 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 115..500 | 386 | 346 | 336 | 10 | 9 | 2 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 23 | 122..542 | 421 | 373 | 359 | 14 | 12 | 2 | 0 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 126..538 | 413 | 388 | 380 | 8 | 8 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 25 | 127..429 | 303 | 269 | 259 | 10 | 10 | 1 | 0 | 78896 |
| 26 | 132..477 | 346 | 308 | 294 | 14 | 13 | 2 | 0 | 78897, 79098, 79102, 79103 |
| 27 | 135..537 | 403 | 351 | 334 | 17 | 17 | 1 | 0 | 79134, 79136, 79139 |
| 28 | 136..434 | 299 | 252 | 247 | 5 | 5 | 1 | 0 | 78969 |
| 29 | 142..443 | 302 | 262 | 249 | 13 | 12 | 2 | 0 | 79037, 79045 |
| 30 | 144..497 | 354 | 305 | 294 | 11 | 11 | 1 | 0 | 79108, 79110, 79111, 79115 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9355; unmatched reference entries: 787; unmatched candidate entries: 1481
- identity switches: 336; fragmentation (coverage interruptions): 619; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 7 -> 13 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 13 -> 14 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 7 -> 15 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 6 -> 13 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 13 -> 6 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 15 -> 10 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 10 -> 19 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 18 -> 20 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 15 -> 10 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 18 -> 15 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 14 -> 6 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 6 -> 14 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 11 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 8 -> 3 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 13 -> 8 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 14 -> 13 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 19 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 10 -> 19 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 10 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 15 -> 10 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 20 -> 15 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 18 -> 20 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 14 -> 11 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 11 -> 16 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 3 -> 8 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 8 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 6 -> 14 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 13 -> 6 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 19 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 19 -> 10 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 10 -> 15 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 15 -> 20 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 15 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 20 -> 15 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79105: 21 -> 10 at (2079, 3025), 2 frames after previous cover
- f114: ref 79115: 18 -> 20 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 7 -> 22 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79108: 21 -> 7 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 15 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 20 -> 15 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 11 -> 14 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 16 -> 11 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 17 -> 16 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 19 -> 17 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 10 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- f119: ref 78897: 14 -> 11 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 11 -> 16 at (1988.5, 3032), 1 frames after previous cover
- ... 276 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 964 | 33 | 2 (964) |
| 78896 | 350 (76..429) | 318 | 25 | 25 (274), 3 (44) |
| 78969 | 352 (80..434) | 313 | 29 | 28 (271), 8 (32), 3 (10) |
| 78971 | 352 (84..439) | 328 | 18 | 8 (293), 6 (19), 13 (15), 3 (1) |
| 79045 | 355 (84..443) | 313 | 28 | 29 (194), 3 (80), 6 (23), 13 (8), 8 (4), 7 (2), 14 (2) |
| 79037 | 355 (86..445) | 318 | 31 | 3 (127), 6 (80), 29 (74), 14 (30), 11 (3), 13 (2), 7 (1), 10 (1) |
| 78897 | 345 (89..450) | 313 | 27 | 6 (194), 3 (79), 11 (23), 14 (4), 13 (4), 10 (3), 28 (3), 7 (2), 26 (1) |
| 78899 | 365 (91..455) | 336 | 25 | 14 (294), 16 (17), 11 (13), 7 (3), 10 (3), 6 (3), 28 (2), 13 (1) |
| 79097 | 366 (94..461) | 337 | 22 | 11 (300), 17 (18), 13 (8), 16 (6), 7 (3), 10 (2) |
| 79098 | 360 (97..467) | 329 | 26 | 13 (295), 19 (10), 17 (8), 10 (5), 11 (5), 16 (3), 7 (1), 26 (1), 14 (1) |
| 79102 | 371 (98..477) | 331 | 31 | 26 (307), 10 (6), 19 (6), 17 (5), 15 (4), 13 (2), 7 (1) |
| 79103 | 380 (99..481) | 361 | 18 | 17 (325), 7 (15), 22 (9), 19 (5), 26 (4), 16 (3) |
| 79105 | 379 (101..484) | 348 | 25 | 16 (322), 10 (11), 15 (5), 19 (5), 21 (2), 7 (1), 22 (1), 17 (1) |
| 79108 | 385 (104..492) | 366 | 14 | 19 (334), 7 (11), 30 (7), 21 (4), 15 (3), 10 (3), 22 (2), 18 (1), 16 (1) |
| 79110 | 388 (106..497) | 361 | 23 | 30 (305), 10 (14), 19 (13), 22 (8), 20 (5), 21 (5), 15 (4), 7 (4), 16 (2), 18 (1) |
| 79111 | 386 (109..500) | 354 | 26 | 22 (241), 10 (89), 30 (9), 15 (5), 18 (3), 20 (3), 21 (3), 7 (1) |
| 79115 | 421 (111..531) | 383 | 26 | 10 (199), 7 (94), 22 (56), 20 (27), 18 (3), 21 (3), 30 (1) |
| 79116 | 411 (114..530) | 386 | 24 | 7 (112), 21 (87), 10 (67), 20 (55), 22 (38), 15 (22), 18 (5) |
| 79122 | 404 (118..532) | 366 | 27 | 21 (238), 20 (92), 10 (19), 18 (7), 15 (3), 22 (3), 7 (3), 23 (1) |
| 79132 | 391 (120..515) | 361 | 21 | 20 (177), 7 (131), 21 (39), 15 (7), 23 (4), 18 (3) |
| 79128 | 402 (124..527) | 375 | 20 | 15 (344), 20 (20), 18 (7), 23 (3), 24 (1) |
| 79134 | 407 (127..533) | 381 | 22 | 18 (355), 27 (11), 24 (8), 23 (7) |
| 79135 | 409 (129..542) | 378 | 25 | 23 (366), 24 (11), 18 (1) |
| 79139 | 406 (132..537) | 378 | 22 | 24 (343), 27 (28), 23 (4), 18 (3) |
| 79136 | 393 (136..538) | 357 | 31 | 27 (315), 24 (32), 18 (10) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 328/414/1003; tracks with internal gaps: 25; total internal gaps: 649; longest internal gap: 13; tracks ending in coasting: 24 (trailing rows total 663)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 1003 | 964 | 39 | 33 | 3 | 0 | 78911 |
| 3 | 78..478 | 401 | 401 | 341 | 60 | 26 | 2 | 31 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 6 | 86..474 | 389 | 389 | 319 | 70 | 33 | 5 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 86..544 | 459 | 459 | 385 | 74 | 32 | 6 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 8 | 88..468 | 381 | 381 | 329 | 52 | 19 | 3 | 29 | 78969, 78971, 79045 |
| 10 | 90..561 | 472 | 472 | 422 | 50 | 19 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 91..490 | 400 | 400 | 344 | 56 | 25 | 4 | 23 | 78897, 78899, 79037, 79097, 79098 |
| 13 | 95..496 | 402 | 402 | 335 | 67 | 29 | 2 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 14 | 98..484 | 387 | 387 | 331 | 56 | 23 | 2 | 31 | 78897, 78899, 79037, 79045, 79098 |
| 15 | 100..556 | 457 | 457 | 397 | 60 | 24 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 16 | 100..513 | 414 | 414 | 354 | 60 | 30 | 10 | 17 | 78899, 79097, 79098, 79103, 79105, 79108, 79110 |
| 17 | 101..510 | 410 | 410 | 357 | 53 | 21 | 2 | 29 | 79097, 79098, 79102, 79103, 79105 |
| 18 | 105..562 | 458 | 458 | 399 | 59 | 24 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 106..521 | 416 | 416 | 373 | 43 | 16 | 4 | 24 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 20 | 108..557 | 450 | 450 | 379 | 71 | 28 | 6 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..559 | 449 | 449 | 381 | 68 | 27 | 7 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 115..529 | 415 | 415 | 358 | 57 | 23 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 23 | 122..571 | 450 | 450 | 385 | 65 | 28 | 3 | 29 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 126..567 | 442 | 442 | 395 | 47 | 17 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 25 | 127..458 | 332 | 332 | 274 | 58 | 24 | 3 | 29 | 78896 |
| 26 | 132..506 | 375 | 375 | 313 | 62 | 28 | 2 | 29 | 78897, 79098, 79102, 79103 |
| 27 | 135..566 | 432 | 432 | 354 | 78 | 41 | 4 | 29 | 79134, 79136, 79139 |
| 28 | 136..463 | 328 | 328 | 276 | 52 | 28 | 13 | 8 | 78897, 78899, 78969 |
| 29 | 142..472 | 331 | 331 | 268 | 63 | 26 | 3 | 29 | 79037, 79045 |
| 30 | 144..526 | 383 | 383 | 322 | 61 | 25 | 2 | 32 | 79108, 79110, 79111, 79115 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9355; unmatched reference entries: 787; unmatched candidate entries: 1481
- identity switches: 336; fragmentation (coverage interruptions): 619; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 79037: 7 -> 10 at (2135, 3035.5), 2 frames after previous cover
- f91: ref 78897: 7 -> 10 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 10 -> 11 at (2129, 3033.5), 1 frames after previous cover
- f94: ref 78897: 10 -> 11 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 7 -> 10 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 11 -> 13 at (2105, 3034.5), 2 frames after previous cover
- f97: ref 79045: 7 -> 13 at (2081.5, 3032), 10 frames after previous cover
- f97: ref 79097: 7 -> 10 at (2135, 3028), 1 frames after previous cover
- f98: ref 79037: 13 -> 14 at (2087, 3034), 2 frames after previous cover
- f99: ref 79098: 7 -> 10 at (2135.5, 3025.5), 2 frames after previous cover
- f100: ref 78899: 10 -> 16 at (2104, 3030.5), 4 frames after previous cover
- f100: ref 79102: 7 -> 15 at (2142.5, 3026), 2 frames after previous cover
- f101: ref 79097: 10 -> 17 at (2111.5, 3028.5), 3 frames after previous cover
- f104: ref 78971: 6 -> 13 at (2027.5, 3034.5), 1 frames after previous cover
- f104: ref 79045: 13 -> 6 at (2036.5, 3033.5), 2 frames after previous cover
- f104: ref 79102: 15 -> 10 at (2119, 3027), 1 frames after previous cover
- f106: ref 79098: 10 -> 19 at (2096, 3028.5), 3 frames after previous cover
- f108: ref 79110: 18 -> 20 at (2145, 3026.5), 2 frames after previous cover
- f109: ref 79105: 15 -> 10 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 18 -> 15 at (2125, 3025), 4 frames after previous cover
- f110: ref 79037: 14 -> 6 at (2013, 3034.5), 1 frames after previous cover
- f110: ref 79045: 6 -> 14 at (2000.5, 3033.5), 1 frames after previous cover
- f111: ref 78897: 11 -> 14 at (2021.5, 3032.5), 1 frames after previous cover
- f111: ref 78899: 16 -> 11 at (2037, 3030.5), 1 frames after previous cover
- f111: ref 78969: 8 -> 3 at (1965.5, 3036), 1 frames after previous cover
- f111: ref 78971: 13 -> 8 at (1984, 3033.5), 2 frames after previous cover
- f111: ref 79045: 14 -> 13 at (1994.5, 3035), 1 frames after previous cover
- f111: ref 79097: 17 -> 16 at (2052, 3030), 1 frames after previous cover
- f111: ref 79098: 19 -> 17 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 10 -> 19 at (2079, 3029.5), 3 frames after previous cover
- f111: ref 79105: 10 -> 21 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 15 -> 10 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 20 -> 15 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 18 -> 20 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78897: 14 -> 11 at (2015.5, 3032.5), 1 frames after previous cover
- f112: ref 78899: 11 -> 16 at (2032, 3032), 1 frames after previous cover
- f112: ref 78969: 3 -> 8 at (1959.5, 3036), 1 frames after previous cover
- f112: ref 78971: 8 -> 13 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 6 -> 14 at (2000.5, 3035), 1 frames after previous cover
- f112: ref 79045: 13 -> 6 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79097: 16 -> 17 at (2046, 3030.5), 1 frames after previous cover
- f112: ref 79098: 17 -> 19 at (2059, 3029.5), 1 frames after previous cover
- f112: ref 79102: 19 -> 10 at (2072.5, 3029.5), 1 frames after previous cover
- f112: ref 79108: 10 -> 15 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 15 -> 20 at (2124.5, 3027.5), 1 frames after previous cover
- f113: ref 79108: 15 -> 21 at (2101.5, 3026), 1 frames after previous cover
- f113: ref 79110: 20 -> 15 at (2117, 3027.5), 1 frames after previous cover
- f114: ref 79105: 21 -> 10 at (2079, 3025), 2 frames after previous cover
- f114: ref 79115: 18 -> 20 at (2141.5, 3021.5), 1 frames after previous cover
- f115: ref 79103: 7 -> 22 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79108: 21 -> 7 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 15 -> 21 at (2105.5, 3026.5), 1 frames after previous cover
- f115: ref 79111: 20 -> 15 at (2120, 3028.5), 2 frames after previous cover
- f116: ref 78897: 11 -> 14 at (1990.5, 3033.5), 1 frames after previous cover
- f116: ref 78899: 16 -> 11 at (2006.5, 3032), 1 frames after previous cover
- f116: ref 79097: 17 -> 16 at (2022.5, 3030.5), 1 frames after previous cover
- f116: ref 79098: 19 -> 17 at (2035.5, 3029), 1 frames after previous cover
- f116: ref 79102: 10 -> 19 at (2049.5, 3030.5), 3 frames after previous cover
- f119: ref 78897: 14 -> 11 at (1972.5, 3034.5), 3 frames after previous cover
- f119: ref 78899: 11 -> 16 at (1988.5, 3032), 1 frames after previous cover
- ... 276 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 964 | 33 | 2 (964) |
| 78896 | 350 (76..429) | 318 | 25 | 25 (274), 3 (44) |
| 78969 | 352 (80..434) | 313 | 29 | 28 (271), 8 (32), 3 (10) |
| 78971 | 352 (84..439) | 328 | 18 | 8 (293), 6 (19), 13 (15), 3 (1) |
| 79045 | 355 (84..443) | 313 | 28 | 29 (194), 3 (80), 6 (23), 13 (8), 8 (4), 7 (2), 14 (2) |
| 79037 | 355 (86..445) | 318 | 31 | 3 (127), 6 (80), 29 (74), 14 (30), 11 (3), 13 (2), 7 (1), 10 (1) |
| 78897 | 345 (89..450) | 313 | 27 | 6 (194), 3 (79), 11 (23), 14 (4), 13 (4), 10 (3), 28 (3), 7 (2), 26 (1) |
| 78899 | 365 (91..455) | 336 | 25 | 14 (294), 16 (17), 11 (13), 7 (3), 10 (3), 6 (3), 28 (2), 13 (1) |
| 79097 | 366 (94..461) | 337 | 22 | 11 (300), 17 (18), 13 (8), 16 (6), 7 (3), 10 (2) |
| 79098 | 360 (97..467) | 329 | 26 | 13 (295), 19 (10), 17 (8), 10 (5), 11 (5), 16 (3), 7 (1), 26 (1), 14 (1) |
| 79102 | 371 (98..477) | 331 | 31 | 26 (307), 10 (6), 19 (6), 17 (5), 15 (4), 13 (2), 7 (1) |
| 79103 | 380 (99..481) | 361 | 18 | 17 (325), 7 (15), 22 (9), 19 (5), 26 (4), 16 (3) |
| 79105 | 379 (101..484) | 348 | 25 | 16 (322), 10 (11), 15 (5), 19 (5), 21 (2), 7 (1), 22 (1), 17 (1) |
| 79108 | 385 (104..492) | 366 | 14 | 19 (334), 7 (11), 30 (7), 21 (4), 15 (3), 10 (3), 22 (2), 18 (1), 16 (1) |
| 79110 | 388 (106..497) | 361 | 23 | 30 (305), 10 (14), 19 (13), 22 (8), 20 (5), 21 (5), 15 (4), 7 (4), 16 (2), 18 (1) |
| 79111 | 386 (109..500) | 354 | 26 | 22 (241), 10 (89), 30 (9), 15 (5), 18 (3), 20 (3), 21 (3), 7 (1) |
| 79115 | 421 (111..531) | 383 | 26 | 10 (199), 7 (94), 22 (56), 20 (27), 18 (3), 21 (3), 30 (1) |
| 79116 | 411 (114..530) | 386 | 24 | 7 (112), 21 (87), 10 (67), 20 (55), 22 (38), 15 (22), 18 (5) |
| 79122 | 404 (118..532) | 366 | 27 | 21 (238), 20 (92), 10 (19), 18 (7), 15 (3), 22 (3), 7 (3), 23 (1) |
| 79132 | 391 (120..515) | 361 | 21 | 20 (177), 7 (131), 21 (39), 15 (7), 23 (4), 18 (3) |
| 79128 | 402 (124..527) | 375 | 20 | 15 (344), 20 (20), 18 (7), 23 (3), 24 (1) |
| 79134 | 407 (127..533) | 381 | 22 | 18 (355), 27 (11), 24 (8), 23 (7) |
| 79135 | 409 (129..542) | 378 | 25 | 23 (366), 24 (11), 18 (1) |
| 79139 | 406 (132..537) | 378 | 22 | 24 (343), 27 (28), 23 (4), 18 (3) |
| 79136 | 393 (136..538) | 357 | 31 | 27 (315), 24 (32), 18 (10) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 328/414/1003; tracks with internal gaps: 25; total internal gaps: 649; longest internal gap: 13; tracks ending in coasting: 24 (trailing rows total 663)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 6..1008 | 1003 | 1003 | 964 | 39 | 33 | 3 | 0 | 78911 |
| 3 | 78..478 | 401 | 401 | 341 | 60 | 26 | 2 | 31 | 78896, 78897, 78969, 78971, 79037, 79045 |
| 6 | 86..474 | 389 | 389 | 319 | 70 | 33 | 5 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 86..544 | 459 | 459 | 385 | 74 | 32 | 6 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 8 | 88..468 | 381 | 381 | 329 | 52 | 19 | 3 | 29 | 78969, 78971, 79045 |
| 10 | 90..561 | 472 | 472 | 422 | 50 | 19 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 91..490 | 400 | 400 | 344 | 56 | 25 | 4 | 23 | 78897, 78899, 79037, 79097, 79098 |
| 13 | 95..496 | 402 | 402 | 335 | 67 | 29 | 2 | 32 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102 |
| 14 | 98..484 | 387 | 387 | 331 | 56 | 23 | 2 | 31 | 78897, 78899, 79037, 79045, 79098 |
| 15 | 100..556 | 457 | 457 | 397 | 60 | 24 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 16 | 100..513 | 414 | 414 | 354 | 60 | 30 | 10 | 17 | 78899, 79097, 79098, 79103, 79105, 79108, 79110 |
| 17 | 101..510 | 410 | 410 | 357 | 53 | 21 | 2 | 29 | 79097, 79098, 79102, 79103, 79105 |
| 18 | 105..562 | 458 | 458 | 399 | 59 | 24 | 3 | 29 | 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 106..521 | 416 | 416 | 373 | 43 | 16 | 4 | 24 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 20 | 108..557 | 450 | 450 | 379 | 71 | 28 | 6 | 30 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 21 | 111..559 | 449 | 449 | 381 | 68 | 27 | 7 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 22 | 115..529 | 415 | 415 | 358 | 57 | 23 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 23 | 122..571 | 450 | 450 | 385 | 65 | 28 | 3 | 29 | 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 126..567 | 442 | 442 | 395 | 47 | 17 | 2 | 29 | 79128, 79134, 79135, 79136, 79139 |
| 25 | 127..458 | 332 | 332 | 274 | 58 | 24 | 3 | 29 | 78896 |
| 26 | 132..506 | 375 | 375 | 313 | 62 | 28 | 2 | 29 | 78897, 79098, 79102, 79103 |
| 27 | 135..566 | 432 | 432 | 354 | 78 | 41 | 4 | 29 | 79134, 79136, 79139 |
| 28 | 136..463 | 328 | 328 | 276 | 52 | 28 | 13 | 8 | 78897, 78899, 78969 |
| 29 | 142..472 | 331 | 331 | 268 | 63 | 26 | 3 | 29 | 79037, 79045 |
| 30 | 144..526 | 383 | 383 | 322 | 61 | 25 | 2 | 32 | 79108, 79110, 79111, 79115 |
