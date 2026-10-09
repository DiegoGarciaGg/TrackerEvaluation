# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=5e35e883864c
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise3.0_fp0.0_seed1/tracks.csv sha256=4c4c4984fb914c2d
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise3.0_fp0.0_seed1.csv sha256=5e35e883864c50c2
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise3.0_fp0.0_seed1
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
| observations | none | 4 | 10142 | 9046 | 0.332 | 0.399 | 0.277 | 2.18 | 0.323 | 0.146 | 2.41 | 198 | 2516.0 | 0.461 | 0.489 | 0.437 | 0.529 | 0.593 | 5361 | 4781 | 3685 | 0 | 25 | 0 |
| observations | none | 6 | 10142 | 9046 | 0.466 | 0.551 | 0.394 | 2.73 | 0.563 | 0.633 | 3.19 | 242 | 1751.0 | 0.679 | 0.721 | 0.643 | 0.775 | 0.868 | 7855 | 2287 | 1191 | 3 | 22 | 0 |
| observations | none | 8 | 10142 | 9046 | 0.539 | 0.621 | 0.468 | 3.07 | 0.675 | 0.815 | 3.57 | 222 | 1172.0 | 0.763 | 0.809 | 0.722 | 0.864 | 0.969 | 8765 | 1377 | 281 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 9046 | 0.618 | 0.687 | 0.556 | 3.55 | 0.726 | 0.867 | 3.82 | 190 | 981.0 | 0.809 | 0.859 | 0.766 | 0.889 | 0.996 | 9013 | 1129 | 33 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 9046 | 0.332 | 0.399 | 0.277 | 2.18 | 0.323 | 0.146 | 2.41 | 198 | 2516.0 | 0.461 | 0.489 | 0.437 | 0.529 | 0.593 | 5361 | 4781 | 3685 | 0 | 25 | 0 |
| observations | ignore | 6 | 10142 | 9046 | 0.466 | 0.551 | 0.394 | 2.73 | 0.563 | 0.633 | 3.19 | 242 | 1751.0 | 0.679 | 0.721 | 0.643 | 0.775 | 0.868 | 7855 | 2287 | 1191 | 3 | 22 | 0 |
| observations | ignore | 8 | 10142 | 9046 | 0.539 | 0.621 | 0.468 | 3.07 | 0.675 | 0.815 | 3.57 | 222 | 1172.0 | 0.763 | 0.809 | 0.722 | 0.864 | 0.969 | 8765 | 1377 | 281 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 9046 | 0.618 | 0.687 | 0.556 | 3.55 | 0.726 | 0.867 | 3.82 | 190 | 981.0 | 0.809 | 0.859 | 0.766 | 0.889 | 0.996 | 9013 | 1129 | 33 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10857 | 0.314 | 0.374 | 0.264 | 2.20 | 0.301 | 0.003 | 2.42 | 242 | 2506.0 | 0.438 | 0.423 | 0.453 | 0.549 | 0.513 | 5565 | 4577 | 5292 | 0 | 25 | 0 |
| updates | none | 6 | 10142 | 10857 | 0.453 | 0.531 | 0.387 | 2.81 | 0.532 | 0.535 | 3.22 | 256 | 1505.0 | 0.656 | 0.634 | 0.679 | 0.815 | 0.761 | 8267 | 1875 | 2590 | 17 | 8 | 0 |
| updates | none | 8 | 10142 | 10857 | 0.534 | 0.609 | 0.469 | 3.19 | 0.658 | 0.763 | 3.68 | 208 | 682.0 | 0.753 | 0.728 | 0.779 | 0.927 | 0.866 | 9403 | 739 | 1454 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10857 | 0.623 | 0.686 | 0.566 | 3.73 | 0.739 | 0.868 | 4.05 | 148 | 253.0 | 0.818 | 0.791 | 0.847 | 0.976 | 0.912 | 9903 | 239 | 954 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10857 | 0.314 | 0.374 | 0.264 | 2.20 | 0.301 | 0.003 | 2.42 | 242 | 2506.0 | 0.438 | 0.423 | 0.453 | 0.549 | 0.513 | 5565 | 4577 | 5292 | 0 | 25 | 0 |
| updates | ignore | 6 | 10142 | 10857 | 0.453 | 0.531 | 0.387 | 2.81 | 0.532 | 0.535 | 3.22 | 256 | 1505.0 | 0.656 | 0.634 | 0.679 | 0.815 | 0.761 | 8267 | 1875 | 2590 | 17 | 8 | 0 |
| updates | ignore | 8 | 10142 | 10857 | 0.534 | 0.609 | 0.469 | 3.19 | 0.658 | 0.763 | 3.68 | 208 | 682.0 | 0.753 | 0.728 | 0.779 | 0.927 | 0.866 | 9403 | 739 | 1454 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10857 | 0.623 | 0.686 | 0.566 | 3.73 | 0.739 | 0.868 | 4.05 | 148 | 253.0 | 0.818 | 0.791 | 0.847 | 0.976 | 0.912 | 9903 | 239 | 954 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8765; unmatched reference entries: 1377; unmatched candidate entries: 281
- identity switches: 222; fragmentation (coverage interruptions): 1137; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 6 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 5 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 6 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 6 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 5 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79097: 5 -> 7 at (2146.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79097: 7 -> 5 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 5 -> 7 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 7 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 7 -> 12 at (2093, 3030.5), 6 frames after previous cover
- f102: ref 79103: 11 -> 5 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 5 -> 13 at (2124.5, 3027.5), 2 frames after previous cover
- f104: ref 78899: 12 -> 9 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79098: 7 -> 10 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79097: 10 -> 12 at (2088, 3029), 2 frames after previous cover
- f105: ref 79102: 13 -> 7 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 5 -> 13 at (2120.5, 3023), 2 frames after previous cover
- f105: ref 79105: 11 -> 5 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 10 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 13 -> 10 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 5 -> 13 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 9 -> 14 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 9 -> 3 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 3 -> 6 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 6 -> 8 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 14 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78969: 2 -> 1 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 79098: 12 -> 14 at (2077.5, 3029.5), 2 frames after previous cover
- f110: ref 78969: 1 -> 2 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 13 -> 10 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 11 -> 13 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 5 -> 11 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 14 -> 7 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 8 -> 15 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 10 -> 16 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 10 -> 14 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 16 -> 10 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 13 -> 16 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 11 -> 13 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 5 -> 11 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 7 -> 12 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 7 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 16 -> 13 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 13 -> 16 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 12 -> 3 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 79097: 3 -> 12 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 11 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 5 -> 11 at (2118, 3022), 1 frames after previous cover
- f119: ref 79098: 12 -> 7 at (2019, 3029.5), 2 frames after previous cover
- f121: ref 78899: 9 -> 3 at (1976, 3033), 1 frames after previous cover
- f122: ref 78899: 3 -> 9 at (1970, 3034), 1 frames after previous cover
- f122: ref 79105: 10 -> 14 at (2034.5, 3024.5), 1 frames after previous cover
- f122: ref 79110: 16 -> 21 at (2067, 3026), 5 frames after previous cover
- f123: ref 79102: 7 -> 14 at (2006, 3031), 2 frames after previous cover
- ... 162 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 878 | 113 | 0 (878) |
| 78896 | 350 (76..429) | 304 | 36 | 1 (304) |
| 78969 | 352 (80..434) | 299 | 40 | 15 (250), 2 (45), 1 (4) |
| 78971 | 352 (84..439) | 303 | 39 | 8 (164), 2 (135), 15 (2), 3 (1), 6 (1) |
| 79045 | 355 (84..443) | 303 | 41 | 8 (140), 2 (119), 15 (22), 6 (17), 3 (3), 9 (2) |
| 79037 | 355 (86..445) | 305 | 36 | 9 (256), 6 (29), 3 (16), 15 (3), 8 (1) |
| 78897 | 345 (89..450) | 291 | 40 | 6 (251), 3 (26), 9 (10), 7 (3), 5 (1) |
| 78899 | 365 (91..455) | 305 | 47 | 3 (266), 9 (32), 5 (3), 7 (2), 12 (2) |
| 79097 | 366 (94..461) | 313 | 47 | 12 (298), 10 (4), 3 (4), 7 (3), 5 (2), 9 (1), 14 (1) |
| 79098 | 360 (97..467) | 317 | 36 | 7 (302), 12 (9), 10 (2), 14 (2), 5 (1), 22 (1) |
| 79102 | 371 (98..477) | 306 | 47 | 26 (272), 7 (15), 22 (8), 14 (4), 5 (3), 13 (2), 24 (2) |
| 79103 | 380 (99..481) | 316 | 45 | 24 (293), 14 (10), 10 (5), 26 (3), 5 (2), 11 (1), 13 (1), 22 (1) |
| 79105 | 379 (101..484) | 330 | 43 | 22 (300), 10 (13), 13 (4), 24 (4), 11 (3), 16 (2), 25 (2), 5 (1), 14 (1) |
| 79108 | 385 (104..492) | 329 | 48 | 10 (303), 13 (11), 11 (4), 22 (4), 25 (3), 16 (2), 14 (2) |
| 79110 | 388 (106..497) | 343 | 37 | 27 (193), 25 (92), 13 (32), 10 (8), 14 (5), 11 (4), 21 (4), 5 (3), 16 (2) |
| 79111 | 386 (109..500) | 335 | 44 | 25 (178), 27 (70), 13 (65), 16 (7), 5 (4), 11 (4), 14 (4), 21 (3) |
| 79115 | 421 (111..531) | 370 | 39 | 13 (257), 25 (44), 27 (32), 14 (19), 11 (14), 5 (4) |
| 79116 | 411 (114..530) | 364 | 36 | 14 (317), 21 (14), 27 (9), 18 (8), 11 (6), 13 (5), 16 (3), 25 (2) |
| 79122 | 404 (118..532) | 336 | 63 | 11 (317), 5 (7), 21 (6), 18 (3), 16 (3) |
| 79132 | 391 (120..515) | 344 | 41 | 21 (242), 16 (79), 14 (11), 18 (4), 5 (3), 11 (3), 19 (2) |
| 79128 | 402 (124..527) | 352 | 47 | 16 (260), 21 (79), 18 (5), 19 (4), 5 (4) |
| 79134 | 407 (127..533) | 360 | 42 | 18 (310), 23 (40), 5 (6), 19 (4) |
| 79135 | 409 (129..542) | 365 | 39 | 5 (292), 19 (68), 23 (5) |
| 79139 | 406 (132..537) | 356 | 44 | 19 (295), 18 (36), 5 (15), 23 (10) |
| 79136 | 393 (136..538) | 341 | 47 | 23 (287), 5 (42), 18 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 323/370/1007; tracks with internal gaps: 25; total internal gaps: 266; longest internal gap: 4; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 908 | 878 | 30 | 30 | 1 | 0 | 78911 |
| 1 | 78..429 | 352 | 312 | 308 | 4 | 4 | 1 | 0 | 78896, 78969 |
| 2 | 83..443 | 361 | 311 | 299 | 12 | 11 | 1 | 1 | 78969, 78971, 79045 |
| 3 | 86..455 | 370 | 330 | 316 | 14 | 13 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 5 | 90..537 | 448 | 401 | 393 | 8 | 8 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 6 | 90..450 | 361 | 308 | 298 | 10 | 10 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 7 | 91..467 | 377 | 333 | 325 | 8 | 8 | 1 | 0 | 78897, 78899, 79097, 79098, 79102 |
| 8 | 93..439 | 347 | 314 | 305 | 9 | 8 | 2 | 0 | 78971, 79037, 79045 |
| 9 | 96..445 | 350 | 312 | 301 | 11 | 9 | 2 | 0 | 78897, 78899, 79037, 79045, 79097 |
| 10 | 100..492 | 393 | 345 | 335 | 10 | 10 | 1 | 0 | 79097, 79098, 79103, 79105, 79108, 79110 |
| 11 | 100..532 | 433 | 369 | 356 | 13 | 13 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..461 | 360 | 323 | 309 | 14 | 14 | 1 | 0 | 78899, 79097, 79098 |
| 13 | 103..531 | 429 | 394 | 377 | 17 | 16 | 2 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 14 | 107..530 | 424 | 383 | 376 | 7 | 5 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 15 | 112..434 | 323 | 291 | 277 | 14 | 13 | 2 | 0 | 78969, 78971, 79037, 79045 |
| 16 | 112..515 | 404 | 369 | 358 | 11 | 11 | 1 | 0 | 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 18 | 116..538 | 423 | 385 | 378 | 7 | 7 | 1 | 0 | 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 19 | 122..542 | 421 | 394 | 373 | 21 | 20 | 2 | 0 | 79128, 79132, 79134, 79135, 79139 |
| 21 | 122..527 | 406 | 356 | 348 | 8 | 8 | 1 | 0 | 79110, 79111, 79116, 79122, 79128, 79132 |
| 22 | 126..484 | 359 | 322 | 314 | 8 | 8 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 23 | 132..533 | 402 | 355 | 342 | 13 | 13 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 132..481 | 350 | 306 | 299 | 7 | 7 | 1 | 0 | 79102, 79103, 79105 |
| 25 | 132..500 | 369 | 327 | 321 | 6 | 5 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 26 | 139..477 | 339 | 283 | 275 | 8 | 7 | 2 | 0 | 79102, 79103 |
| 27 | 145..497 | 353 | 315 | 304 | 11 | 8 | 4 | 0 | 79110, 79111, 79115, 79116 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8765; unmatched reference entries: 1377; unmatched candidate entries: 281
- identity switches: 222; fragmentation (coverage interruptions): 1137; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 6 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 5 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 6 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 6 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 5 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79097: 5 -> 7 at (2146.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 79097: 7 -> 5 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 5 -> 7 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 7 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 7 -> 12 at (2093, 3030.5), 6 frames after previous cover
- f102: ref 79103: 11 -> 5 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 5 -> 13 at (2124.5, 3027.5), 2 frames after previous cover
- f104: ref 78899: 12 -> 9 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79098: 7 -> 10 at (2107, 3027.5), 1 frames after previous cover
- f105: ref 79097: 10 -> 12 at (2088, 3029), 2 frames after previous cover
- f105: ref 79102: 13 -> 7 at (2113.5, 3026.5), 1 frames after previous cover
- f105: ref 79103: 5 -> 13 at (2120.5, 3023), 2 frames after previous cover
- f105: ref 79105: 11 -> 5 at (2130.5, 3023.5), 1 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 10 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 13 -> 10 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 5 -> 13 at (2125, 3025.5), 1 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 9 -> 14 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 9 -> 3 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 3 -> 6 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 6 -> 8 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 14 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78969: 2 -> 1 at (1978, 3034.5), 1 frames after previous cover
- f109: ref 79098: 12 -> 14 at (2077.5, 3029.5), 2 frames after previous cover
- f110: ref 78969: 1 -> 2 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 13 -> 10 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 11 -> 13 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 5 -> 11 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 14 -> 7 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 8 -> 15 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 10 -> 16 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 10 -> 14 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 16 -> 10 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 13 -> 16 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 11 -> 13 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 5 -> 11 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 7 -> 12 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 7 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 16 -> 13 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 13 -> 16 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 12 -> 3 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 79097: 3 -> 12 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 11 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 5 -> 11 at (2118, 3022), 1 frames after previous cover
- f119: ref 79098: 12 -> 7 at (2019, 3029.5), 2 frames after previous cover
- f121: ref 78899: 9 -> 3 at (1976, 3033), 1 frames after previous cover
- f122: ref 78899: 3 -> 9 at (1970, 3034), 1 frames after previous cover
- f122: ref 79105: 10 -> 14 at (2034.5, 3024.5), 1 frames after previous cover
- f122: ref 79110: 16 -> 21 at (2067, 3026), 5 frames after previous cover
- f123: ref 79102: 7 -> 14 at (2006, 3031), 2 frames after previous cover
- ... 162 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 878 | 113 | 0 (878) |
| 78896 | 350 (76..429) | 304 | 36 | 1 (304) |
| 78969 | 352 (80..434) | 299 | 40 | 15 (250), 2 (45), 1 (4) |
| 78971 | 352 (84..439) | 303 | 39 | 8 (164), 2 (135), 15 (2), 3 (1), 6 (1) |
| 79045 | 355 (84..443) | 303 | 41 | 8 (140), 2 (119), 15 (22), 6 (17), 3 (3), 9 (2) |
| 79037 | 355 (86..445) | 305 | 36 | 9 (256), 6 (29), 3 (16), 15 (3), 8 (1) |
| 78897 | 345 (89..450) | 291 | 40 | 6 (251), 3 (26), 9 (10), 7 (3), 5 (1) |
| 78899 | 365 (91..455) | 305 | 47 | 3 (266), 9 (32), 5 (3), 7 (2), 12 (2) |
| 79097 | 366 (94..461) | 313 | 47 | 12 (298), 10 (4), 3 (4), 7 (3), 5 (2), 9 (1), 14 (1) |
| 79098 | 360 (97..467) | 317 | 36 | 7 (302), 12 (9), 10 (2), 14 (2), 5 (1), 22 (1) |
| 79102 | 371 (98..477) | 306 | 47 | 26 (272), 7 (15), 22 (8), 14 (4), 5 (3), 13 (2), 24 (2) |
| 79103 | 380 (99..481) | 316 | 45 | 24 (293), 14 (10), 10 (5), 26 (3), 5 (2), 11 (1), 13 (1), 22 (1) |
| 79105 | 379 (101..484) | 330 | 43 | 22 (300), 10 (13), 13 (4), 24 (4), 11 (3), 16 (2), 25 (2), 5 (1), 14 (1) |
| 79108 | 385 (104..492) | 329 | 48 | 10 (303), 13 (11), 11 (4), 22 (4), 25 (3), 16 (2), 14 (2) |
| 79110 | 388 (106..497) | 343 | 37 | 27 (193), 25 (92), 13 (32), 10 (8), 14 (5), 11 (4), 21 (4), 5 (3), 16 (2) |
| 79111 | 386 (109..500) | 335 | 44 | 25 (178), 27 (70), 13 (65), 16 (7), 5 (4), 11 (4), 14 (4), 21 (3) |
| 79115 | 421 (111..531) | 370 | 39 | 13 (257), 25 (44), 27 (32), 14 (19), 11 (14), 5 (4) |
| 79116 | 411 (114..530) | 364 | 36 | 14 (317), 21 (14), 27 (9), 18 (8), 11 (6), 13 (5), 16 (3), 25 (2) |
| 79122 | 404 (118..532) | 336 | 63 | 11 (317), 5 (7), 21 (6), 18 (3), 16 (3) |
| 79132 | 391 (120..515) | 344 | 41 | 21 (242), 16 (79), 14 (11), 18 (4), 5 (3), 11 (3), 19 (2) |
| 79128 | 402 (124..527) | 352 | 47 | 16 (260), 21 (79), 18 (5), 19 (4), 5 (4) |
| 79134 | 407 (127..533) | 360 | 42 | 18 (310), 23 (40), 5 (6), 19 (4) |
| 79135 | 409 (129..542) | 365 | 39 | 5 (292), 19 (68), 23 (5) |
| 79139 | 406 (132..537) | 356 | 44 | 19 (295), 18 (36), 5 (15), 23 (10) |
| 79136 | 393 (136..538) | 341 | 47 | 23 (287), 5 (42), 18 (12) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 323/370/1007; tracks with internal gaps: 25; total internal gaps: 266; longest internal gap: 4; tracks ending in coasting: 1 (trailing rows total 1)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 908 | 878 | 30 | 30 | 1 | 0 | 78911 |
| 1 | 78..429 | 352 | 312 | 308 | 4 | 4 | 1 | 0 | 78896, 78969 |
| 2 | 83..443 | 361 | 311 | 299 | 12 | 11 | 1 | 1 | 78969, 78971, 79045 |
| 3 | 86..455 | 370 | 330 | 316 | 14 | 13 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 5 | 90..537 | 448 | 401 | 393 | 8 | 8 | 1 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 6 | 90..450 | 361 | 308 | 298 | 10 | 10 | 1 | 0 | 78897, 78971, 79037, 79045 |
| 7 | 91..467 | 377 | 333 | 325 | 8 | 8 | 1 | 0 | 78897, 78899, 79097, 79098, 79102 |
| 8 | 93..439 | 347 | 314 | 305 | 9 | 8 | 2 | 0 | 78971, 79037, 79045 |
| 9 | 96..445 | 350 | 312 | 301 | 11 | 9 | 2 | 0 | 78897, 78899, 79037, 79045, 79097 |
| 10 | 100..492 | 393 | 345 | 335 | 10 | 10 | 1 | 0 | 79097, 79098, 79103, 79105, 79108, 79110 |
| 11 | 100..532 | 433 | 369 | 356 | 13 | 13 | 1 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..461 | 360 | 323 | 309 | 14 | 14 | 1 | 0 | 78899, 79097, 79098 |
| 13 | 103..531 | 429 | 394 | 377 | 17 | 16 | 2 | 0 | 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 14 | 107..530 | 424 | 383 | 376 | 7 | 5 | 2 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 15 | 112..434 | 323 | 291 | 277 | 14 | 13 | 2 | 0 | 78969, 78971, 79037, 79045 |
| 16 | 112..515 | 404 | 369 | 358 | 11 | 11 | 1 | 0 | 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 18 | 116..538 | 423 | 385 | 378 | 7 | 7 | 1 | 0 | 79116, 79122, 79128, 79132, 79134, 79136, 79139 |
| 19 | 122..542 | 421 | 394 | 373 | 21 | 20 | 2 | 0 | 79128, 79132, 79134, 79135, 79139 |
| 21 | 122..527 | 406 | 356 | 348 | 8 | 8 | 1 | 0 | 79110, 79111, 79116, 79122, 79128, 79132 |
| 22 | 126..484 | 359 | 322 | 314 | 8 | 8 | 1 | 0 | 79098, 79102, 79103, 79105, 79108 |
| 23 | 132..533 | 402 | 355 | 342 | 13 | 13 | 1 | 0 | 79134, 79135, 79136, 79139 |
| 24 | 132..481 | 350 | 306 | 299 | 7 | 7 | 1 | 0 | 79102, 79103, 79105 |
| 25 | 132..500 | 369 | 327 | 321 | 6 | 5 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 26 | 139..477 | 339 | 283 | 275 | 8 | 7 | 2 | 0 | 79102, 79103 |
| 27 | 145..497 | 353 | 315 | 304 | 11 | 8 | 4 | 0 | 79110, 79111, 79115, 79116 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9403; unmatched reference entries: 739; unmatched candidate entries: 1454
- identity switches: 208; fragmentation (coverage interruptions): 592; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 6 at (2115, 3033.5), 1 frames after previous cover
- f91: ref 78897: 5 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 6 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 6 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 5 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 5 -> 7 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 7 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 7 -> 12 at (2093, 3030.5), 5 frames after previous cover
- f102: ref 79103: 11 -> 5 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 5 -> 13 at (2124.5, 3027.5), 2 frames after previous cover
- f105: ref 78899: 12 -> 9 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 10 -> 12 at (2088, 3029), 2 frames after previous cover
- f105: ref 79098: 7 -> 10 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 13 -> 7 at (2113.5, 3026.5), 1 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 10 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 5 -> 10 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 11 -> 13 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 9 -> 14 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 9 -> 3 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 3 -> 6 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 6 -> 8 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 14 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 12 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78969: 2 -> 1 at (1978, 3034.5), 1 frames after previous cover
- f110: ref 78969: 1 -> 2 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 13 -> 10 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 11 -> 13 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 5 -> 11 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 14 -> 7 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 8 -> 15 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 10 -> 16 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 10 -> 14 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 16 -> 10 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 13 -> 16 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 11 -> 13 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 5 -> 11 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 7 -> 12 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 7 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 16 -> 13 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 13 -> 16 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 12 -> 3 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 3 -> 6 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79097: 3 -> 12 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 11 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 5 -> 11 at (2118, 3022), 1 frames after previous cover
- f119: ref 78897: 6 -> 3 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 79098: 12 -> 7 at (2019, 3029.5), 2 frames after previous cover
- f121: ref 78899: 9 -> 3 at (1976, 3033), 1 frames after previous cover
- f122: ref 78899: 3 -> 9 at (1970, 3034), 1 frames after previous cover
- f122: ref 79110: 16 -> 21 at (2067, 3026), 5 frames after previous cover
- f123: ref 79102: 7 -> 14 at (2006, 3031), 2 frames after previous cover
- f124: ref 79122: 5 -> 18 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 19 -> 5 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79122: 18 -> 5 at (2112.5, 3026.5), 1 frames after previous cover
- ... 148 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 958 | 47 | 0 (958) |
| 78896 | 350 (76..429) | 323 | 22 | 1 (323) |
| 78969 | 352 (80..434) | 320 | 26 | 15 (267), 2 (49), 1 (4) |
| 78971 | 352 (84..439) | 320 | 26 | 8 (171), 2 (142), 3 (4), 15 (2), 6 (1) |
| 79045 | 355 (84..443) | 332 | 16 | 8 (152), 2 (137), 15 (24), 6 (17), 3 (1), 9 (1) |
| 79037 | 355 (86..445) | 319 | 23 | 9 (270), 6 (29), 3 (16), 15 (3), 8 (1) |
| 78897 | 345 (89..450) | 311 | 25 | 6 (270), 3 (28), 9 (9), 7 (3), 5 (1) |
| 78899 | 365 (91..455) | 335 | 24 | 3 (294), 9 (32), 5 (3), 7 (3), 12 (3) |
| 79097 | 366 (94..461) | 337 | 26 | 12 (321), 5 (4), 10 (4), 3 (4), 9 (2), 7 (1), 14 (1) |
| 79098 | 360 (97..467) | 334 | 21 | 7 (319), 12 (9), 14 (3), 5 (1), 10 (1), 22 (1) |
| 79102 | 371 (98..477) | 334 | 25 | 26 (301), 7 (15), 22 (8), 14 (4), 5 (3), 13 (2), 24 (1) |
| 79103 | 380 (99..481) | 341 | 24 | 24 (314), 14 (10), 10 (6), 26 (6), 5 (4), 11 (1) |
| 79105 | 379 (101..484) | 354 | 22 | 22 (321), 10 (15), 24 (6), 13 (4), 11 (3), 25 (3), 16 (2) |
| 79108 | 385 (104..492) | 357 | 22 | 10 (328), 13 (13), 11 (5), 22 (4), 25 (3), 16 (2), 14 (2) |
| 79110 | 388 (106..497) | 368 | 13 | 27 (212), 25 (97), 13 (33), 10 (8), 14 (5), 11 (4), 21 (4), 5 (3), 16 (2) |
| 79111 | 386 (109..500) | 357 | 23 | 25 (195), 27 (74), 13 (63), 16 (8), 14 (6), 5 (4), 11 (4), 21 (3) |
| 79115 | 421 (111..531) | 392 | 22 | 13 (277), 25 (47), 27 (37), 11 (14), 14 (13), 5 (4) |
| 79116 | 411 (114..530) | 389 | 17 | 14 (343), 21 (12), 27 (10), 18 (9), 11 (6), 13 (4), 16 (3), 25 (2) |
| 79122 | 404 (118..532) | 373 | 30 | 11 (354), 5 (7), 21 (6), 18 (3), 16 (3) |
| 79132 | 391 (120..515) | 367 | 18 | 21 (262), 16 (82), 14 (12), 18 (4), 5 (3), 19 (2), 11 (2) |
| 79128 | 402 (124..527) | 375 | 25 | 16 (276), 21 (86), 18 (5), 19 (4), 5 (4) |
| 79134 | 407 (127..533) | 384 | 21 | 18 (331), 23 (41), 5 (8), 19 (4) |
| 79135 | 409 (129..542) | 386 | 19 | 5 (311), 19 (70), 23 (5) |
| 79139 | 406 (132..537) | 376 | 28 | 19 (310), 18 (48), 23 (18) |
| 79136 | 393 (136..538) | 361 | 27 | 23 (298), 5 (63) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 352/399/1007; tracks with internal gaps: 25; total internal gaps: 644; longest internal gap: 8; tracks ending in coasting: 24 (trailing rows total 687)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 958 | 49 | 47 | 2 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 327 | 54 | 22 | 3 | 29 | 78896, 78969 |
| 2 | 83..472 | 390 | 390 | 328 | 62 | 32 | 1 | 30 | 78969, 78971, 79045 |
| 3 | 86..484 | 399 | 399 | 347 | 52 | 21 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 5 | 90..566 | 477 | 477 | 423 | 54 | 24 | 2 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136 |
| 6 | 90..479 | 390 | 390 | 317 | 73 | 33 | 3 | 29 | 78897, 78971, 79037, 79045 |
| 7 | 91..496 | 406 | 406 | 341 | 65 | 28 | 4 | 29 | 78897, 78899, 79097, 79098, 79102 |
| 8 | 93..468 | 376 | 376 | 324 | 52 | 20 | 3 | 29 | 78971, 79037, 79045 |
| 9 | 96..474 | 379 | 379 | 314 | 65 | 25 | 3 | 29 | 78897, 78899, 79037, 79045, 79097 |
| 10 | 100..521 | 422 | 422 | 362 | 60 | 26 | 2 | 29 | 79097, 79098, 79103, 79105, 79108, 79110 |
| 11 | 100..561 | 462 | 462 | 393 | 69 | 37 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..490 | 389 | 389 | 333 | 56 | 25 | 2 | 29 | 78899, 79097, 79098 |
| 13 | 103..560 | 458 | 458 | 396 | 62 | 26 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116 |
| 14 | 107..559 | 453 | 453 | 399 | 54 | 19 | 2 | 29 | 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79132 |
| 15 | 112..463 | 352 | 352 | 296 | 56 | 26 | 8 | 20 | 78969, 78971, 79037, 79045 |
| 16 | 112..544 | 433 | 433 | 378 | 55 | 25 | 2 | 29 | 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 18 | 116..567 | 452 | 452 | 400 | 52 | 20 | 3 | 30 | 79116, 79122, 79128, 79132, 79134, 79139 |
| 19 | 122..571 | 450 | 450 | 390 | 60 | 29 | 2 | 29 | 79128, 79132, 79134, 79135, 79139 |
| 21 | 122..556 | 435 | 435 | 373 | 62 | 25 | 4 | 29 | 79110, 79111, 79116, 79122, 79128, 79132 |
| 22 | 126..513 | 388 | 388 | 334 | 54 | 23 | 2 | 29 | 79098, 79102, 79105, 79108 |
| 23 | 132..562 | 431 | 431 | 362 | 69 | 33 | 3 | 29 | 79134, 79135, 79136, 79139 |
| 24 | 132..510 | 379 | 379 | 321 | 58 | 20 | 3 | 32 | 79102, 79103, 79105 |
| 25 | 132..529 | 398 | 398 | 347 | 51 | 17 | 4 | 29 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 26 | 139..506 | 368 | 368 | 307 | 61 | 26 | 3 | 25 | 79102, 79103 |
| 27 | 145..526 | 382 | 382 | 333 | 49 | 15 | 4 | 29 | 79110, 79111, 79115, 79116 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9403; unmatched reference entries: 739; unmatched candidate entries: 1454
- identity switches: 208; fragmentation (coverage interruptions): 592; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 6 at (2115, 3033.5), 1 frames after previous cover
- f91: ref 78897: 5 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 6 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 6 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 5 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 5 -> 7 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 7 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f102: ref 78899: 7 -> 12 at (2093, 3030.5), 5 frames after previous cover
- f102: ref 79103: 11 -> 5 at (2139, 3022), 2 frames after previous cover
- f103: ref 79102: 5 -> 13 at (2124.5, 3027.5), 2 frames after previous cover
- f105: ref 78899: 12 -> 9 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 10 -> 12 at (2088, 3029), 2 frames after previous cover
- f105: ref 79098: 7 -> 10 at (2100.5, 3028.5), 1 frames after previous cover
- f105: ref 79102: 13 -> 7 at (2113.5, 3026.5), 1 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 3 frames after previous cover
- f106: ref 79097: 12 -> 9 at (2082.5, 3028.5), 1 frames after previous cover
- f106: ref 79098: 10 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79103: 5 -> 10 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 11 -> 13 at (2125, 3025.5), 2 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79097: 9 -> 14 at (2076.5, 3029), 1 frames after previous cover
- f108: ref 78897: 9 -> 3 at (2040.5, 3033), 1 frames after previous cover
- f108: ref 79037: 3 -> 6 at (2026, 3034), 1 frames after previous cover
- f108: ref 79045: 6 -> 8 at (2014.5, 3034), 1 frames after previous cover
- f108: ref 79097: 14 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 12 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 78969: 2 -> 1 at (1978, 3034.5), 1 frames after previous cover
- f110: ref 78969: 1 -> 2 at (1971.5, 3034.5), 1 frames after previous cover
- f110: ref 79105: 13 -> 10 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 11 -> 13 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 5 -> 11 at (2134, 3026), 1 frames after previous cover
- f111: ref 79098: 14 -> 7 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 7 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f112: ref 79045: 8 -> 15 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79105: 10 -> 16 at (2091.5, 3025.5), 2 frames after previous cover
- f114: ref 79103: 10 -> 14 at (2069, 3023.5), 1 frames after previous cover
- f114: ref 79105: 16 -> 10 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 13 -> 16 at (2097.5, 3025.5), 2 frames after previous cover
- f114: ref 79110: 11 -> 13 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 5 -> 11 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 7 -> 12 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 7 at (2055, 3030), 2 frames after previous cover
- f116: ref 79108: 16 -> 13 at (2087, 3026.5), 1 frames after previous cover
- f116: ref 79110: 13 -> 16 at (2101, 3028), 2 frames after previous cover
- f117: ref 79097: 12 -> 3 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 3 -> 6 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79097: 3 -> 12 at (2010.5, 3030), 1 frames after previous cover
- f118: ref 79111: 11 -> 16 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 5 -> 11 at (2118, 3022), 1 frames after previous cover
- f119: ref 78897: 6 -> 3 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 79098: 12 -> 7 at (2019, 3029.5), 2 frames after previous cover
- f121: ref 78899: 9 -> 3 at (1976, 3033), 1 frames after previous cover
- f122: ref 78899: 3 -> 9 at (1970, 3034), 1 frames after previous cover
- f122: ref 79110: 16 -> 21 at (2067, 3026), 5 frames after previous cover
- f123: ref 79102: 7 -> 14 at (2006, 3031), 2 frames after previous cover
- f124: ref 79122: 5 -> 18 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 19 -> 5 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79122: 18 -> 5 at (2112.5, 3026.5), 1 frames after previous cover
- ... 148 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 958 | 47 | 0 (958) |
| 78896 | 350 (76..429) | 323 | 22 | 1 (323) |
| 78969 | 352 (80..434) | 320 | 26 | 15 (267), 2 (49), 1 (4) |
| 78971 | 352 (84..439) | 320 | 26 | 8 (171), 2 (142), 3 (4), 15 (2), 6 (1) |
| 79045 | 355 (84..443) | 332 | 16 | 8 (152), 2 (137), 15 (24), 6 (17), 3 (1), 9 (1) |
| 79037 | 355 (86..445) | 319 | 23 | 9 (270), 6 (29), 3 (16), 15 (3), 8 (1) |
| 78897 | 345 (89..450) | 311 | 25 | 6 (270), 3 (28), 9 (9), 7 (3), 5 (1) |
| 78899 | 365 (91..455) | 335 | 24 | 3 (294), 9 (32), 5 (3), 7 (3), 12 (3) |
| 79097 | 366 (94..461) | 337 | 26 | 12 (321), 5 (4), 10 (4), 3 (4), 9 (2), 7 (1), 14 (1) |
| 79098 | 360 (97..467) | 334 | 21 | 7 (319), 12 (9), 14 (3), 5 (1), 10 (1), 22 (1) |
| 79102 | 371 (98..477) | 334 | 25 | 26 (301), 7 (15), 22 (8), 14 (4), 5 (3), 13 (2), 24 (1) |
| 79103 | 380 (99..481) | 341 | 24 | 24 (314), 14 (10), 10 (6), 26 (6), 5 (4), 11 (1) |
| 79105 | 379 (101..484) | 354 | 22 | 22 (321), 10 (15), 24 (6), 13 (4), 11 (3), 25 (3), 16 (2) |
| 79108 | 385 (104..492) | 357 | 22 | 10 (328), 13 (13), 11 (5), 22 (4), 25 (3), 16 (2), 14 (2) |
| 79110 | 388 (106..497) | 368 | 13 | 27 (212), 25 (97), 13 (33), 10 (8), 14 (5), 11 (4), 21 (4), 5 (3), 16 (2) |
| 79111 | 386 (109..500) | 357 | 23 | 25 (195), 27 (74), 13 (63), 16 (8), 14 (6), 5 (4), 11 (4), 21 (3) |
| 79115 | 421 (111..531) | 392 | 22 | 13 (277), 25 (47), 27 (37), 11 (14), 14 (13), 5 (4) |
| 79116 | 411 (114..530) | 389 | 17 | 14 (343), 21 (12), 27 (10), 18 (9), 11 (6), 13 (4), 16 (3), 25 (2) |
| 79122 | 404 (118..532) | 373 | 30 | 11 (354), 5 (7), 21 (6), 18 (3), 16 (3) |
| 79132 | 391 (120..515) | 367 | 18 | 21 (262), 16 (82), 14 (12), 18 (4), 5 (3), 19 (2), 11 (2) |
| 79128 | 402 (124..527) | 375 | 25 | 16 (276), 21 (86), 18 (5), 19 (4), 5 (4) |
| 79134 | 407 (127..533) | 384 | 21 | 18 (331), 23 (41), 5 (8), 19 (4) |
| 79135 | 409 (129..542) | 386 | 19 | 5 (311), 19 (70), 23 (5) |
| 79139 | 406 (132..537) | 376 | 28 | 19 (310), 18 (48), 23 (18) |
| 79136 | 393 (136..538) | 361 | 27 | 23 (298), 5 (63) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 352/399/1007; tracks with internal gaps: 25; total internal gaps: 644; longest internal gap: 8; tracks ending in coasting: 24 (trailing rows total 687)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 958 | 49 | 47 | 2 | 0 | 78911 |
| 1 | 78..458 | 381 | 381 | 327 | 54 | 22 | 3 | 29 | 78896, 78969 |
| 2 | 83..472 | 390 | 390 | 328 | 62 | 32 | 1 | 30 | 78969, 78971, 79045 |
| 3 | 86..484 | 399 | 399 | 347 | 52 | 21 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 5 | 90..566 | 477 | 477 | 423 | 54 | 24 | 2 | 28 | 78897, 78899, 79097, 79098, 79102, 79103, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136 |
| 6 | 90..479 | 390 | 390 | 317 | 73 | 33 | 3 | 29 | 78897, 78971, 79037, 79045 |
| 7 | 91..496 | 406 | 406 | 341 | 65 | 28 | 4 | 29 | 78897, 78899, 79097, 79098, 79102 |
| 8 | 93..468 | 376 | 376 | 324 | 52 | 20 | 3 | 29 | 78971, 79037, 79045 |
| 9 | 96..474 | 379 | 379 | 314 | 65 | 25 | 3 | 29 | 78897, 78899, 79037, 79045, 79097 |
| 10 | 100..521 | 422 | 422 | 362 | 60 | 26 | 2 | 29 | 79097, 79098, 79103, 79105, 79108, 79110 |
| 11 | 100..561 | 462 | 462 | 393 | 69 | 37 | 2 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..490 | 389 | 389 | 333 | 56 | 25 | 2 | 29 | 78899, 79097, 79098 |
| 13 | 103..560 | 458 | 458 | 396 | 62 | 26 | 3 | 29 | 79102, 79105, 79108, 79110, 79111, 79115, 79116 |
| 14 | 107..559 | 453 | 453 | 399 | 54 | 19 | 2 | 29 | 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79132 |
| 15 | 112..463 | 352 | 352 | 296 | 56 | 26 | 8 | 20 | 78969, 78971, 79037, 79045 |
| 16 | 112..544 | 433 | 433 | 378 | 55 | 25 | 2 | 29 | 79105, 79108, 79110, 79111, 79116, 79122, 79128, 79132 |
| 18 | 116..567 | 452 | 452 | 400 | 52 | 20 | 3 | 30 | 79116, 79122, 79128, 79132, 79134, 79139 |
| 19 | 122..571 | 450 | 450 | 390 | 60 | 29 | 2 | 29 | 79128, 79132, 79134, 79135, 79139 |
| 21 | 122..556 | 435 | 435 | 373 | 62 | 25 | 4 | 29 | 79110, 79111, 79116, 79122, 79128, 79132 |
| 22 | 126..513 | 388 | 388 | 334 | 54 | 23 | 2 | 29 | 79098, 79102, 79105, 79108 |
| 23 | 132..562 | 431 | 431 | 362 | 69 | 33 | 3 | 29 | 79134, 79135, 79136, 79139 |
| 24 | 132..510 | 379 | 379 | 321 | 58 | 20 | 3 | 32 | 79102, 79103, 79105 |
| 25 | 132..529 | 398 | 398 | 347 | 51 | 17 | 4 | 29 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 26 | 139..506 | 368 | 368 | 307 | 61 | 26 | 3 | 25 | 79102, 79103 |
| 27 | 145..526 | 382 | 382 | 333 | 49 | 15 | 4 | 29 | 79110, 79111, 79115, 79116 |
