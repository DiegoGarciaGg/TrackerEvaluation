# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=350400b86e26
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise1.0_fp0.0_seed1/tracks.csv sha256=95fee8b42f4b5063
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise1.0_fp0.0_seed1.csv sha256=350400b86e263c21
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise1.0_fp0.0_seed1
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
| observations | none | 4 | 10142 | 9044 | 0.671 | 0.737 | 0.612 | 1.06 | 0.807 | 0.875 | 1.25 | 147 | 979.0 | 0.876 | 0.929 | 0.829 | 0.891 | 0.999 | 9032 | 1110 | 12 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 9044 | 0.723 | 0.789 | 0.662 | 1.15 | 0.807 | 0.877 | 1.26 | 147 | 971.0 | 0.878 | 0.931 | 0.830 | 0.892 | 1.000 | 9044 | 1098 | 0 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 9044 | 0.750 | 0.808 | 0.696 | 1.21 | 0.805 | 0.877 | 1.26 | 147 | 971.0 | 0.878 | 0.932 | 0.831 | 0.892 | 1.000 | 9044 | 1098 | 0 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 9044 | 0.782 | 0.829 | 0.737 | 1.36 | 0.807 | 0.877 | 1.30 | 140 | 970.0 | 0.882 | 0.936 | 0.835 | 0.891 | 1.000 | 9041 | 1101 | 3 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 9044 | 0.671 | 0.737 | 0.612 | 1.06 | 0.807 | 0.875 | 1.25 | 147 | 979.0 | 0.876 | 0.929 | 0.829 | 0.891 | 0.999 | 9032 | 1110 | 12 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 9044 | 0.723 | 0.789 | 0.662 | 1.15 | 0.807 | 0.877 | 1.26 | 147 | 971.0 | 0.878 | 0.931 | 0.830 | 0.892 | 1.000 | 9044 | 1098 | 0 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 9044 | 0.750 | 0.808 | 0.696 | 1.21 | 0.805 | 0.877 | 1.26 | 147 | 971.0 | 0.878 | 0.932 | 0.831 | 0.892 | 1.000 | 9044 | 1098 | 0 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 9044 | 0.782 | 0.829 | 0.737 | 1.36 | 0.807 | 0.877 | 1.30 | 140 | 970.0 | 0.882 | 0.936 | 0.835 | 0.891 | 1.000 | 9041 | 1101 | 3 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10851 | 0.611 | 0.667 | 0.561 | 1.15 | 0.708 | 0.722 | 1.28 | 159 | 904.0 | 0.813 | 0.787 | 0.842 | 0.904 | 0.845 | 9168 | 974 | 1683 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 10851 | 0.686 | 0.744 | 0.634 | 1.34 | 0.755 | 0.791 | 1.42 | 164 | 594.0 | 0.845 | 0.817 | 0.874 | 0.938 | 0.877 | 9518 | 624 | 1333 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10851 | 0.728 | 0.779 | 0.680 | 1.47 | 0.802 | 0.858 | 1.61 | 146 | 304.0 | 0.877 | 0.848 | 0.907 | 0.971 | 0.908 | 9850 | 292 | 1001 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10851 | 0.776 | 0.819 | 0.735 | 1.70 | 0.824 | 0.884 | 1.75 | 129 | 195.0 | 0.893 | 0.863 | 0.924 | 0.983 | 0.919 | 9972 | 170 | 879 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10851 | 0.611 | 0.667 | 0.561 | 1.15 | 0.708 | 0.722 | 1.28 | 159 | 904.0 | 0.813 | 0.787 | 0.842 | 0.904 | 0.845 | 9168 | 974 | 1683 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 10851 | 0.686 | 0.744 | 0.634 | 1.34 | 0.755 | 0.791 | 1.42 | 164 | 594.0 | 0.845 | 0.817 | 0.874 | 0.938 | 0.877 | 9518 | 624 | 1333 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10851 | 0.728 | 0.779 | 0.680 | 1.47 | 0.802 | 0.858 | 1.61 | 146 | 304.0 | 0.877 | 0.848 | 0.907 | 0.971 | 0.908 | 9850 | 292 | 1001 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10851 | 0.776 | 0.819 | 0.735 | 1.70 | 0.824 | 0.884 | 1.75 | 129 | 195.0 | 0.893 | 0.863 | 0.924 | 0.983 | 0.919 | 9972 | 170 | 879 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9044; unmatched reference entries: 1098; unmatched candidate entries: 0
- identity switches: 147; fragmentation (coverage interruptions): 930; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 5 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 6 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 5 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 6 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78899: 7 -> 6 at (2128, 3029), 2 frames after previous cover
- f96: ref 79097: 6 -> 7 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 7 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 11 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 6 -> 12 at (2093, 3030.5), 6 frames after previous cover
- f103: ref 79102: 7 -> 13 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 12 -> 9 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 6 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 13 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 7 -> 13 at (2116.5, 3023), 3 frames after previous cover
- f106: ref 79108: 7 -> 11 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 11 -> 14 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78899: 9 -> 10 at (2055.5, 3031), 2 frames after previous cover
- f108: ref 79097: 10 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78897: 9 -> 5 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 10 -> 9 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 1 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79045: 5 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 12 -> 10 at (2064.5, 3030), 1 frames after previous cover
- f112: ref 78896: 1 -> 16 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 7 -> 15 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 14 -> 6 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 11 -> 14 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 15 -> 11 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 7 -> 15 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 12 -> 10 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 6 -> 12 at (2055, 3030), 2 frames after previous cover
- f117: ref 78899: 9 -> 5 at (2001.5, 3032.5), 1 frames after previous cover
- f117: ref 79097: 10 -> 9 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 5 -> 3 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 15 -> 11 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 7 -> 15 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 18 -> 7 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 3 -> 5 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 5 -> 9 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 9 -> 13 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 11 -> 14 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 14 -> 21 at (2053.5, 3026), 5 frames after previous cover
- f124: ref 79122: 18 -> 7 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 19 -> 18 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 7 -> 18 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 13 -> 22 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 14 -> 21 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 11 -> 14 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 15 -> 11 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 18 -> 15 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 7 -> 18 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 18 -> 7 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 22 -> 12 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 6 -> 22 at (2007, 3026), 1 frames after previous cover
- ... 87 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 908 | 88 | 0 (908) |
| 78896 | 350 (76..429) | 307 | 32 | 16 (279), 1 (28) |
| 78969 | 352 (80..434) | 315 | 28 | 2 (312), 16 (3) |
| 78971 | 352 (84..439) | 313 | 32 | 1 (296), 8 (15), 3 (1), 5 (1) |
| 79045 | 355 (84..443) | 314 | 33 | 8 (293), 5 (18), 3 (3) |
| 79037 | 355 (86..445) | 315 | 32 | 9 (267), 3 (45), 2 (3) |
| 78897 | 345 (89..450) | 302 | 37 | 5 (285), 9 (11), 7 (3), 3 (2), 6 (1) |
| 78899 | 365 (91..455) | 319 | 37 | 3 (278), 9 (29), 6 (4), 12 (4), 5 (2), 7 (1), 10 (1) |
| 79097 | 366 (94..461) | 327 | 38 | 13 (305), 10 (13), 6 (3), 9 (2), 3 (2), 7 (1), 12 (1) |
| 79098 | 360 (97..467) | 322 | 30 | 28 (277), 10 (25), 12 (8), 6 (7), 13 (3), 7 (1), 3 (1) |
| 79102 | 371 (98..477) | 317 | 41 | 24 (282), 12 (18), 6 (8), 10 (4), 13 (3), 7 (2) |
| 79103 | 380 (99..481) | 323 | 38 | 10 (292), 13 (12), 24 (9), 7 (3), 26 (3), 12 (2), 11 (1), 22 (1) |
| 79105 | 379 (101..484) | 339 | 35 | 26 (306), 6 (12), 14 (7), 12 (6), 11 (4), 22 (2), 25 (2) |
| 79108 | 385 (104..492) | 336 | 41 | 12 (305), 6 (8), 11 (7), 25 (7), 14 (4), 21 (4), 7 (1) |
| 79110 | 388 (106..497) | 351 | 33 | 21 (326), 14 (6), 11 (4), 25 (4), 7 (3), 22 (3), 6 (3), 15 (2) |
| 79111 | 386 (109..500) | 346 | 33 | 25 (311), 6 (9), 11 (7), 21 (6), 7 (4), 15 (4), 14 (3), 22 (2) |
| 79115 | 421 (111..531) | 385 | 31 | 6 (352), 14 (9), 15 (8), 21 (5), 7 (4), 11 (3), 22 (3), 25 (1) |
| 79116 | 411 (114..530) | 372 | 31 | 14 (357), 7 (5), 18 (3), 15 (3), 11 (2), 22 (2) |
| 79122 | 404 (118..532) | 346 | 56 | 22 (327), 18 (8), 11 (6), 15 (3), 7 (2) |
| 79132 | 391 (120..515) | 352 | 36 | 11 (336), 15 (6), 18 (5), 19 (3), 7 (1), 22 (1) |
| 79128 | 402 (124..527) | 364 | 37 | 15 (351), 19 (11), 7 (2) |
| 79134 | 407 (127..533) | 368 | 36 | 19 (319), 23 (41), 18 (5), 7 (3) |
| 79135 | 409 (129..542) | 376 | 29 | 18 (373), 7 (3) |
| 79139 | 406 (132..537) | 367 | 35 | 7 (326), 19 (30), 23 (10), 18 (1) |
| 79136 | 393 (136..538) | 360 | 31 | 23 (303), 7 (44), 19 (13) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 317/376/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 908 | 908 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..439 | 362 | 324 | 324 | 0 | 0 | 0 | 0 | 78896, 78971 |
| 2 | 83..434 | 352 | 315 | 315 | 0 | 0 | 0 | 0 | 78969, 79037 |
| 3 | 86..455 | 370 | 332 | 332 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 5 | 90..450 | 361 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79045 |
| 6 | 90..531 | 442 | 407 | 407 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115 |
| 7 | 91..538 | 448 | 409 | 409 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 93..443 | 351 | 308 | 308 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 9 | 96..445 | 350 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 10 | 100..481 | 382 | 335 | 335 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103 |
| 11 | 100..515 | 416 | 370 | 370 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..492 | 391 | 344 | 344 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 13 | 103..461 | 359 | 323 | 323 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103 |
| 14 | 107..530 | 424 | 386 | 386 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 15 | 112..527 | 416 | 377 | 377 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 112..429 | 318 | 282 | 282 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 18 | 116..542 | 427 | 395 | 395 | 0 | 0 | 0 | 0 | 79116, 79122, 79132, 79134, 79135, 79139 |
| 19 | 122..537 | 416 | 376 | 376 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 21 | 122..497 | 376 | 341 | 341 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115 |
| 22 | 126..532 | 407 | 341 | 341 | 0 | 0 | 0 | 0 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132 |
| 23 | 132..533 | 402 | 354 | 354 | 0 | 0 | 0 | 0 | 79134, 79136, 79139 |
| 24 | 132..477 | 346 | 291 | 291 | 0 | 0 | 0 | 0 | 79102, 79103 |
| 25 | 132..500 | 369 | 325 | 325 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115 |
| 26 | 139..484 | 346 | 309 | 309 | 0 | 0 | 0 | 0 | 79103, 79105 |
| 28 | 151..467 | 317 | 277 | 277 | 0 | 0 | 0 | 0 | 79098 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9044; unmatched reference entries: 1098; unmatched candidate entries: 0
- identity switches: 147; fragmentation (coverage interruptions): 930; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 5 at (2115, 3033.5), 4 frames after previous cover
- f91: ref 78897: 6 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 5 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 6 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78899: 7 -> 6 at (2128, 3029), 2 frames after previous cover
- f96: ref 79097: 6 -> 7 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 2 frames after previous cover
- f99: ref 79098: 7 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 11 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 6 -> 12 at (2093, 3030.5), 6 frames after previous cover
- f103: ref 79102: 7 -> 13 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 12 -> 9 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 6 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 13 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 7 -> 13 at (2116.5, 3023), 3 frames after previous cover
- f106: ref 79108: 7 -> 11 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 11 -> 14 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78899: 9 -> 10 at (2055.5, 3031), 2 frames after previous cover
- f108: ref 79097: 10 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78897: 9 -> 5 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 10 -> 9 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 1 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79045: 5 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 12 -> 10 at (2064.5, 3030), 1 frames after previous cover
- f112: ref 78896: 1 -> 16 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 7 -> 15 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 14 -> 6 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 11 -> 14 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 15 -> 11 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 7 -> 15 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 12 -> 10 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 6 -> 12 at (2055, 3030), 2 frames after previous cover
- f117: ref 78899: 9 -> 5 at (2001.5, 3032.5), 1 frames after previous cover
- f117: ref 79097: 10 -> 9 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 5 -> 3 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 15 -> 11 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 7 -> 15 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 18 -> 7 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 3 -> 5 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 5 -> 9 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 9 -> 13 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 11 -> 14 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 14 -> 21 at (2053.5, 3026), 5 frames after previous cover
- f124: ref 79122: 18 -> 7 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 19 -> 18 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 7 -> 18 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 13 -> 22 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 14 -> 21 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 11 -> 14 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 15 -> 11 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 18 -> 15 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 7 -> 18 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 18 -> 7 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 22 -> 12 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 6 -> 22 at (2007, 3026), 1 frames after previous cover
- ... 87 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 908 | 88 | 0 (908) |
| 78896 | 350 (76..429) | 307 | 32 | 16 (279), 1 (28) |
| 78969 | 352 (80..434) | 315 | 28 | 2 (312), 16 (3) |
| 78971 | 352 (84..439) | 313 | 32 | 1 (296), 8 (15), 3 (1), 5 (1) |
| 79045 | 355 (84..443) | 314 | 33 | 8 (293), 5 (18), 3 (3) |
| 79037 | 355 (86..445) | 315 | 32 | 9 (267), 3 (45), 2 (3) |
| 78897 | 345 (89..450) | 302 | 37 | 5 (285), 9 (11), 7 (3), 3 (2), 6 (1) |
| 78899 | 365 (91..455) | 319 | 37 | 3 (278), 9 (29), 6 (4), 12 (4), 5 (2), 7 (1), 10 (1) |
| 79097 | 366 (94..461) | 327 | 38 | 13 (305), 10 (13), 6 (3), 9 (2), 3 (2), 7 (1), 12 (1) |
| 79098 | 360 (97..467) | 322 | 30 | 28 (277), 10 (25), 12 (8), 6 (7), 13 (3), 7 (1), 3 (1) |
| 79102 | 371 (98..477) | 317 | 41 | 24 (282), 12 (18), 6 (8), 10 (4), 13 (3), 7 (2) |
| 79103 | 380 (99..481) | 323 | 38 | 10 (292), 13 (12), 24 (9), 7 (3), 26 (3), 12 (2), 11 (1), 22 (1) |
| 79105 | 379 (101..484) | 339 | 35 | 26 (306), 6 (12), 14 (7), 12 (6), 11 (4), 22 (2), 25 (2) |
| 79108 | 385 (104..492) | 336 | 41 | 12 (305), 6 (8), 11 (7), 25 (7), 14 (4), 21 (4), 7 (1) |
| 79110 | 388 (106..497) | 351 | 33 | 21 (326), 14 (6), 11 (4), 25 (4), 7 (3), 22 (3), 6 (3), 15 (2) |
| 79111 | 386 (109..500) | 346 | 33 | 25 (311), 6 (9), 11 (7), 21 (6), 7 (4), 15 (4), 14 (3), 22 (2) |
| 79115 | 421 (111..531) | 385 | 31 | 6 (352), 14 (9), 15 (8), 21 (5), 7 (4), 11 (3), 22 (3), 25 (1) |
| 79116 | 411 (114..530) | 372 | 31 | 14 (357), 7 (5), 18 (3), 15 (3), 11 (2), 22 (2) |
| 79122 | 404 (118..532) | 346 | 56 | 22 (327), 18 (8), 11 (6), 15 (3), 7 (2) |
| 79132 | 391 (120..515) | 352 | 36 | 11 (336), 15 (6), 18 (5), 19 (3), 7 (1), 22 (1) |
| 79128 | 402 (124..527) | 364 | 37 | 15 (351), 19 (11), 7 (2) |
| 79134 | 407 (127..533) | 368 | 36 | 19 (319), 23 (41), 18 (5), 7 (3) |
| 79135 | 409 (129..542) | 376 | 29 | 18 (373), 7 (3) |
| 79139 | 406 (132..537) | 367 | 35 | 7 (326), 19 (30), 23 (10), 18 (1) |
| 79136 | 393 (136..538) | 360 | 31 | 23 (303), 7 (44), 19 (13) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 317/376/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 908 | 908 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..439 | 362 | 324 | 324 | 0 | 0 | 0 | 0 | 78896, 78971 |
| 2 | 83..434 | 352 | 315 | 315 | 0 | 0 | 0 | 0 | 78969, 79037 |
| 3 | 86..455 | 370 | 332 | 332 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 5 | 90..450 | 361 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79045 |
| 6 | 90..531 | 442 | 407 | 407 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115 |
| 7 | 91..538 | 448 | 409 | 409 | 0 | 0 | 0 | 0 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 93..443 | 351 | 308 | 308 | 0 | 0 | 0 | 0 | 78971, 79045 |
| 9 | 96..445 | 350 | 309 | 309 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 10 | 100..481 | 382 | 335 | 335 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103 |
| 11 | 100..515 | 416 | 370 | 370 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..492 | 391 | 344 | 344 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 13 | 103..461 | 359 | 323 | 323 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103 |
| 14 | 107..530 | 424 | 386 | 386 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 15 | 112..527 | 416 | 377 | 377 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 112..429 | 318 | 282 | 282 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 18 | 116..542 | 427 | 395 | 395 | 0 | 0 | 0 | 0 | 79116, 79122, 79132, 79134, 79135, 79139 |
| 19 | 122..537 | 416 | 376 | 376 | 0 | 0 | 0 | 0 | 79128, 79132, 79134, 79136, 79139 |
| 21 | 122..497 | 376 | 341 | 341 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115 |
| 22 | 126..532 | 407 | 341 | 341 | 0 | 0 | 0 | 0 | 79103, 79105, 79110, 79111, 79115, 79116, 79122, 79132 |
| 23 | 132..533 | 402 | 354 | 354 | 0 | 0 | 0 | 0 | 79134, 79136, 79139 |
| 24 | 132..477 | 346 | 291 | 291 | 0 | 0 | 0 | 0 | 79102, 79103 |
| 25 | 132..500 | 369 | 325 | 325 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115 |
| 26 | 139..484 | 346 | 309 | 309 | 0 | 0 | 0 | 0 | 79103, 79105 |
| 28 | 151..467 | 317 | 277 | 277 | 0 | 0 | 0 | 0 | 79098 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9850; unmatched reference entries: 292; unmatched candidate entries: 1001
- identity switches: 146; fragmentation (coverage interruptions): 207; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 5 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 6 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 5 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 6 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78899: 7 -> 6 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 6 -> 7 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 7 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 11 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 6 -> 12 at (2093, 3030.5), 5 frames after previous cover
- f103: ref 79102: 7 -> 13 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 12 -> 9 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 6 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 13 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 7 -> 13 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 7 -> 11 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 11 -> 14 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78899: 9 -> 10 at (2055.5, 3031), 2 frames after previous cover
- f108: ref 79097: 10 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78897: 9 -> 5 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 10 -> 9 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 1 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79045: 5 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 12 -> 10 at (2064.5, 3030), 1 frames after previous cover
- f112: ref 78896: 1 -> 16 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 7 -> 15 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 14 -> 6 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 11 -> 14 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 15 -> 11 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 7 -> 15 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 12 -> 10 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 6 -> 12 at (2055, 3030), 2 frames after previous cover
- f117: ref 78899: 9 -> 5 at (2001.5, 3032.5), 1 frames after previous cover
- f117: ref 79097: 10 -> 9 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 5 -> 3 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 15 -> 11 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 7 -> 15 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 18 -> 7 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 3 -> 5 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 5 -> 9 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 9 -> 13 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 11 -> 14 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 14 -> 21 at (2053.5, 3026), 4 frames after previous cover
- f124: ref 79122: 18 -> 7 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 19 -> 18 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 7 -> 18 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 13 -> 22 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 14 -> 21 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 11 -> 14 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 15 -> 11 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 18 -> 15 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 7 -> 18 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 18 -> 7 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 22 -> 12 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 6 -> 22 at (2007, 3026), 1 frames after previous cover
- ... 86 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1001 | 6 | 0 (1001) |
| 78896 | 350 (76..429) | 334 | 10 | 16 (304), 1 (30) |
| 78969 | 352 (80..434) | 340 | 9 | 2 (337), 16 (3) |
| 78971 | 352 (84..439) | 339 | 9 | 1 (321), 8 (15), 3 (2), 5 (1) |
| 79045 | 355 (84..443) | 344 | 7 | 8 (323), 5 (18), 3 (3) |
| 79037 | 355 (86..445) | 340 | 9 | 9 (292), 3 (45), 2 (3) |
| 78897 | 345 (89..450) | 330 | 12 | 5 (312), 9 (12), 7 (3), 3 (2), 6 (1) |
| 78899 | 365 (91..455) | 352 | 10 | 3 (308), 9 (30), 6 (5), 12 (4), 7 (2), 5 (2), 10 (1) |
| 79097 | 366 (94..461) | 358 | 7 | 13 (334), 10 (14), 6 (3), 7 (2), 9 (2), 3 (2), 12 (1) |
| 79098 | 360 (97..467) | 343 | 10 | 28 (295), 10 (28), 12 (8), 6 (7), 13 (3), 7 (1), 3 (1) |
| 79102 | 371 (98..477) | 352 | 12 | 24 (316), 12 (19), 6 (8), 10 (4), 13 (3), 7 (2) |
| 79103 | 380 (99..481) | 357 | 10 | 10 (319), 13 (13), 24 (13), 7 (4), 26 (4), 12 (2), 11 (1), 22 (1) |
| 79105 | 379 (101..484) | 370 | 6 | 26 (335), 6 (13), 14 (7), 12 (6), 11 (4), 25 (3), 22 (2) |
| 79108 | 385 (104..492) | 371 | 11 | 12 (337), 11 (8), 6 (8), 25 (8), 14 (5), 21 (4), 7 (1) |
| 79110 | 388 (106..497) | 379 | 7 | 21 (354), 14 (6), 11 (4), 25 (4), 7 (3), 22 (3), 6 (3), 15 (2) |
| 79111 | 386 (109..500) | 373 | 9 | 25 (336), 6 (10), 11 (8), 21 (6), 7 (4), 15 (4), 14 (3), 22 (2) |
| 79115 | 421 (111..531) | 414 | 4 | 6 (380), 14 (9), 15 (8), 21 (5), 7 (4), 11 (3), 22 (3), 25 (2) |
| 79116 | 411 (114..530) | 400 | 7 | 14 (381), 7 (6), 18 (3), 15 (3), 11 (3), 22 (2), 6 (1), 25 (1) |
| 79122 | 404 (118..532) | 396 | 8 | 22 (377), 18 (8), 11 (6), 15 (3), 7 (2) |
| 79132 | 391 (120..515) | 383 | 6 | 11 (368), 15 (6), 18 (5), 19 (3), 7 (1) |
| 79128 | 402 (124..527) | 394 | 7 | 15 (381), 19 (11), 7 (2) |
| 79134 | 407 (127..533) | 396 | 10 | 19 (348), 23 (37), 7 (6), 18 (5) |
| 79135 | 409 (129..542) | 402 | 4 | 18 (399), 7 (3) |
| 79139 | 406 (132..537) | 399 | 7 | 7 (350), 19 (45), 23 (3), 18 (1) |
| 79136 | 393 (136..538) | 383 | 10 | 23 (343), 7 (40) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/405/1007; tracks with internal gaps: 25; total internal gaps: 265; longest internal gap: 4; tracks ending in coasting: 24 (trailing rows total 695)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1001 | 6 | 6 | 1 | 0 | 78911 |
| 1 | 78..468 | 391 | 391 | 351 | 40 | 11 | 1 | 29 | 78896, 78971 |
| 2 | 83..463 | 381 | 381 | 340 | 41 | 11 | 2 | 29 | 78969, 79037 |
| 3 | 86..484 | 399 | 399 | 363 | 36 | 7 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 5 | 90..479 | 390 | 390 | 333 | 57 | 23 | 2 | 29 | 78897, 78899, 78971, 79045 |
| 6 | 90..560 | 471 | 471 | 439 | 32 | 3 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 91..567 | 477 | 477 | 436 | 41 | 12 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 93..472 | 380 | 380 | 338 | 42 | 13 | 1 | 29 | 78971, 79045 |
| 9 | 96..474 | 379 | 379 | 336 | 43 | 10 | 3 | 29 | 78897, 78899, 79037, 79097 |
| 10 | 100..510 | 411 | 411 | 366 | 45 | 8 | 3 | 32 | 78899, 79097, 79098, 79102, 79103 |
| 11 | 100..544 | 445 | 445 | 405 | 40 | 11 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..521 | 420 | 420 | 377 | 43 | 14 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 13 | 103..490 | 388 | 388 | 353 | 35 | 6 | 1 | 29 | 79097, 79098, 79102, 79103 |
| 14 | 107..559 | 453 | 453 | 411 | 42 | 10 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 15 | 112..556 | 445 | 445 | 407 | 38 | 8 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 112..458 | 347 | 347 | 307 | 40 | 9 | 3 | 29 | 78896, 78969 |
| 18 | 116..571 | 456 | 456 | 421 | 35 | 6 | 1 | 29 | 79116, 79122, 79132, 79134, 79135, 79139 |
| 19 | 122..566 | 445 | 445 | 407 | 38 | 8 | 2 | 29 | 79128, 79132, 79134, 79139 |
| 21 | 122..526 | 405 | 405 | 369 | 36 | 5 | 3 | 29 | 79108, 79110, 79111, 79115 |
| 22 | 126..561 | 436 | 436 | 390 | 46 | 16 | 2 | 29 | 79103, 79105, 79110, 79111, 79115, 79116, 79122 |
| 23 | 132..562 | 431 | 431 | 383 | 48 | 17 | 2 | 29 | 79134, 79136, 79139 |
| 24 | 132..506 | 375 | 375 | 329 | 46 | 16 | 2 | 25 | 79102, 79103 |
| 25 | 132..529 | 398 | 398 | 354 | 44 | 12 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 26 | 139..513 | 375 | 375 | 339 | 36 | 7 | 1 | 29 | 79103, 79105 |
| 28 | 151..496 | 346 | 346 | 295 | 51 | 16 | 4 | 29 | 79098 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9850; unmatched reference entries: 292; unmatched candidate entries: 1001
- identity switches: 146; fragmentation (coverage interruptions): 207; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f90: ref 78971: 3 -> 5 at (2115, 3033.5), 3 frames after previous cover
- f91: ref 78897: 6 -> 7 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79045: 3 -> 5 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78971: 5 -> 8 at (2095, 3033.5), 3 frames after previous cover
- f94: ref 78899: 6 -> 7 at (2140.5, 3029), 1 frames after previous cover
- f96: ref 78897: 7 -> 9 at (2112.5, 3033), 3 frames after previous cover
- f96: ref 78899: 7 -> 6 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 6 -> 7 at (2141, 3029), 1 frames after previous cover
- f98: ref 79097: 7 -> 6 at (2129, 3028), 1 frames after previous cover
- f99: ref 79098: 7 -> 6 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79097: 6 -> 10 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79103: 11 -> 7 at (2145, 3023.5), 1 frames after previous cover
- f102: ref 78899: 6 -> 12 at (2093, 3030.5), 5 frames after previous cover
- f103: ref 79102: 7 -> 13 at (2124.5, 3027.5), 3 frames after previous cover
- f106: ref 78897: 9 -> 3 at (2052.5, 3032.5), 1 frames after previous cover
- f106: ref 78899: 12 -> 9 at (2067.5, 3030), 1 frames after previous cover
- f106: ref 79098: 6 -> 12 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 13 -> 6 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 7 -> 13 at (2116.5, 3023), 2 frames after previous cover
- f106: ref 79108: 7 -> 11 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 3 -> 9 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 79105: 11 -> 14 at (2118.5, 3025), 2 frames after previous cover
- f108: ref 78899: 9 -> 10 at (2055.5, 3031), 2 frames after previous cover
- f108: ref 79097: 10 -> 12 at (2070, 3029.5), 1 frames after previous cover
- f109: ref 78897: 9 -> 5 at (2033.5, 3033.5), 1 frames after previous cover
- f109: ref 78899: 10 -> 9 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 78971: 8 -> 1 at (1996.5, 3034.5), 2 frames after previous cover
- f109: ref 79045: 5 -> 8 at (2007, 3034), 1 frames after previous cover
- f109: ref 79097: 12 -> 10 at (2064.5, 3030), 1 frames after previous cover
- f112: ref 78896: 1 -> 16 at (1933.5, 3037), 4 frames after previous cover
- f112: ref 79110: 7 -> 15 at (2124.5, 3027.5), 3 frames after previous cover
- f114: ref 79105: 14 -> 6 at (2079, 3025), 1 frames after previous cover
- f114: ref 79108: 11 -> 14 at (2097.5, 3025.5), 1 frames after previous cover
- f114: ref 79110: 15 -> 11 at (2111, 3026.5), 1 frames after previous cover
- f114: ref 79111: 7 -> 15 at (2126, 3027), 1 frames after previous cover
- f115: ref 79098: 12 -> 10 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 6 -> 12 at (2055, 3030), 2 frames after previous cover
- f117: ref 78899: 9 -> 5 at (2001.5, 3032.5), 1 frames after previous cover
- f117: ref 79097: 10 -> 9 at (2017, 3030.5), 3 frames after previous cover
- f118: ref 78897: 5 -> 3 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79111: 15 -> 11 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 7 -> 15 at (2118, 3022), 1 frames after previous cover
- f118: ref 79116: 18 -> 7 at (2131.5, 3022.5), 1 frames after previous cover
- f119: ref 78897: 3 -> 5 at (1972.5, 3034.5), 1 frames after previous cover
- f119: ref 78899: 5 -> 9 at (1988.5, 3032), 1 frames after previous cover
- f119: ref 79097: 9 -> 13 at (2004, 3029), 1 frames after previous cover
- f120: ref 79110: 11 -> 14 at (2077, 3028), 3 frames after previous cover
- f122: ref 79108: 14 -> 21 at (2053.5, 3026), 4 frames after previous cover
- f124: ref 79122: 18 -> 7 at (2119, 3025.5), 1 frames after previous cover
- f124: ref 79132: 19 -> 18 at (2134.5, 3024), 1 frames after previous cover
- f125: ref 79116: 7 -> 18 at (2092, 3026), 2 frames after previous cover
- f126: ref 79103: 13 -> 22 at (1998.5, 3025), 8 frames after previous cover
- f126: ref 79110: 14 -> 21 at (2045, 3026), 1 frames after previous cover
- f126: ref 79111: 11 -> 14 at (2060, 3029), 1 frames after previous cover
- f126: ref 79115: 15 -> 11 at (2073, 3023.5), 1 frames after previous cover
- f126: ref 79116: 18 -> 15 at (2085, 3024.5), 1 frames after previous cover
- f126: ref 79122: 7 -> 18 at (2107, 3027), 1 frames after previous cover
- f126: ref 79132: 18 -> 7 at (2123.5, 3022.5), 2 frames after previous cover
- f127: ref 79103: 22 -> 12 at (1992.5, 3023.5), 1 frames after previous cover
- f127: ref 79105: 6 -> 22 at (2007, 3026), 1 frames after previous cover
- ... 86 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1001 | 6 | 0 (1001) |
| 78896 | 350 (76..429) | 334 | 10 | 16 (304), 1 (30) |
| 78969 | 352 (80..434) | 340 | 9 | 2 (337), 16 (3) |
| 78971 | 352 (84..439) | 339 | 9 | 1 (321), 8 (15), 3 (2), 5 (1) |
| 79045 | 355 (84..443) | 344 | 7 | 8 (323), 5 (18), 3 (3) |
| 79037 | 355 (86..445) | 340 | 9 | 9 (292), 3 (45), 2 (3) |
| 78897 | 345 (89..450) | 330 | 12 | 5 (312), 9 (12), 7 (3), 3 (2), 6 (1) |
| 78899 | 365 (91..455) | 352 | 10 | 3 (308), 9 (30), 6 (5), 12 (4), 7 (2), 5 (2), 10 (1) |
| 79097 | 366 (94..461) | 358 | 7 | 13 (334), 10 (14), 6 (3), 7 (2), 9 (2), 3 (2), 12 (1) |
| 79098 | 360 (97..467) | 343 | 10 | 28 (295), 10 (28), 12 (8), 6 (7), 13 (3), 7 (1), 3 (1) |
| 79102 | 371 (98..477) | 352 | 12 | 24 (316), 12 (19), 6 (8), 10 (4), 13 (3), 7 (2) |
| 79103 | 380 (99..481) | 357 | 10 | 10 (319), 13 (13), 24 (13), 7 (4), 26 (4), 12 (2), 11 (1), 22 (1) |
| 79105 | 379 (101..484) | 370 | 6 | 26 (335), 6 (13), 14 (7), 12 (6), 11 (4), 25 (3), 22 (2) |
| 79108 | 385 (104..492) | 371 | 11 | 12 (337), 11 (8), 6 (8), 25 (8), 14 (5), 21 (4), 7 (1) |
| 79110 | 388 (106..497) | 379 | 7 | 21 (354), 14 (6), 11 (4), 25 (4), 7 (3), 22 (3), 6 (3), 15 (2) |
| 79111 | 386 (109..500) | 373 | 9 | 25 (336), 6 (10), 11 (8), 21 (6), 7 (4), 15 (4), 14 (3), 22 (2) |
| 79115 | 421 (111..531) | 414 | 4 | 6 (380), 14 (9), 15 (8), 21 (5), 7 (4), 11 (3), 22 (3), 25 (2) |
| 79116 | 411 (114..530) | 400 | 7 | 14 (381), 7 (6), 18 (3), 15 (3), 11 (3), 22 (2), 6 (1), 25 (1) |
| 79122 | 404 (118..532) | 396 | 8 | 22 (377), 18 (8), 11 (6), 15 (3), 7 (2) |
| 79132 | 391 (120..515) | 383 | 6 | 11 (368), 15 (6), 18 (5), 19 (3), 7 (1) |
| 79128 | 402 (124..527) | 394 | 7 | 15 (381), 19 (11), 7 (2) |
| 79134 | 407 (127..533) | 396 | 10 | 19 (348), 23 (37), 7 (6), 18 (5) |
| 79135 | 409 (129..542) | 402 | 4 | 18 (399), 7 (3) |
| 79139 | 406 (132..537) | 399 | 7 | 7 (350), 19 (45), 23 (3), 18 (1) |
| 79136 | 393 (136..538) | 383 | 10 | 23 (343), 7 (40) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 346/405/1007; tracks with internal gaps: 25; total internal gaps: 265; longest internal gap: 4; tracks ending in coasting: 24 (trailing rows total 695)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1001 | 6 | 6 | 1 | 0 | 78911 |
| 1 | 78..468 | 391 | 391 | 351 | 40 | 11 | 1 | 29 | 78896, 78971 |
| 2 | 83..463 | 381 | 381 | 340 | 41 | 11 | 2 | 29 | 78969, 79037 |
| 3 | 86..484 | 399 | 399 | 363 | 36 | 7 | 1 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098 |
| 5 | 90..479 | 390 | 390 | 333 | 57 | 23 | 2 | 29 | 78897, 78899, 78971, 79045 |
| 6 | 90..560 | 471 | 471 | 439 | 32 | 3 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 91..567 | 477 | 477 | 436 | 41 | 12 | 1 | 29 | 78897, 78899, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 8 | 93..472 | 380 | 380 | 338 | 42 | 13 | 1 | 29 | 78971, 79045 |
| 9 | 96..474 | 379 | 379 | 336 | 43 | 10 | 3 | 29 | 78897, 78899, 79037, 79097 |
| 10 | 100..510 | 411 | 411 | 366 | 45 | 8 | 3 | 32 | 78899, 79097, 79098, 79102, 79103 |
| 11 | 100..544 | 445 | 445 | 405 | 40 | 11 | 1 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 12 | 102..521 | 420 | 420 | 377 | 43 | 14 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108 |
| 13 | 103..490 | 388 | 388 | 353 | 35 | 6 | 1 | 29 | 79097, 79098, 79102, 79103 |
| 14 | 107..559 | 453 | 453 | 411 | 42 | 10 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 15 | 112..556 | 445 | 445 | 407 | 38 | 8 | 2 | 29 | 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 16 | 112..458 | 347 | 347 | 307 | 40 | 9 | 3 | 29 | 78896, 78969 |
| 18 | 116..571 | 456 | 456 | 421 | 35 | 6 | 1 | 29 | 79116, 79122, 79132, 79134, 79135, 79139 |
| 19 | 122..566 | 445 | 445 | 407 | 38 | 8 | 2 | 29 | 79128, 79132, 79134, 79139 |
| 21 | 122..526 | 405 | 405 | 369 | 36 | 5 | 3 | 29 | 79108, 79110, 79111, 79115 |
| 22 | 126..561 | 436 | 436 | 390 | 46 | 16 | 2 | 29 | 79103, 79105, 79110, 79111, 79115, 79116, 79122 |
| 23 | 132..562 | 431 | 431 | 383 | 48 | 17 | 2 | 29 | 79134, 79136, 79139 |
| 24 | 132..506 | 375 | 375 | 329 | 46 | 16 | 2 | 25 | 79102, 79103 |
| 25 | 132..529 | 398 | 398 | 354 | 44 | 12 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116 |
| 26 | 139..513 | 375 | 375 | 339 | 36 | 7 | 1 | 29 | 79103, 79105 |
| 28 | 151..496 | 346 | 346 | 295 | 51 | 16 | 4 | 29 | 79098 |
