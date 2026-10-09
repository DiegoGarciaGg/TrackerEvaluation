# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=a6694b519554
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise0.0_fp0.0_seed3/tracks.csv sha256=7bf8b83aa262aebe
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise0.0_fp0.0_seed3.csv sha256=a6694b5195545beb
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise0.0_fp0.0_seed3
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
| observations | none | 4 | 10142 | 8984 | 0.805 | 0.884 | 0.733 | 0.01 | 0.806 | 0.867 | 0.01 | 188 | 1042.0 | 0.874 | 0.930 | 0.824 | 0.886 | 1.000 | 8984 | 1158 | 0 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 8984 | 0.805 | 0.882 | 0.735 | 0.01 | 0.805 | 0.868 | 0.01 | 184 | 1042.0 | 0.874 | 0.930 | 0.824 | 0.886 | 1.000 | 8984 | 1158 | 0 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 8984 | 0.804 | 0.871 | 0.742 | 0.03 | 0.802 | 0.868 | 0.02 | 185 | 1042.0 | 0.874 | 0.931 | 0.824 | 0.886 | 1.000 | 8984 | 1158 | 0 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 8984 | 0.805 | 0.858 | 0.755 | 0.14 | 0.800 | 0.867 | 0.07 | 174 | 1039.0 | 0.875 | 0.932 | 0.825 | 0.885 | 0.999 | 8978 | 1164 | 6 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 8984 | 0.805 | 0.884 | 0.733 | 0.01 | 0.806 | 0.867 | 0.01 | 188 | 1042.0 | 0.874 | 0.930 | 0.824 | 0.886 | 1.000 | 8984 | 1158 | 0 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 8984 | 0.805 | 0.882 | 0.735 | 0.01 | 0.805 | 0.868 | 0.01 | 184 | 1042.0 | 0.874 | 0.930 | 0.824 | 0.886 | 1.000 | 8984 | 1158 | 0 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 8984 | 0.804 | 0.871 | 0.742 | 0.03 | 0.802 | 0.868 | 0.02 | 185 | 1042.0 | 0.874 | 0.931 | 0.824 | 0.886 | 1.000 | 8984 | 1158 | 0 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 8984 | 0.805 | 0.858 | 0.755 | 0.14 | 0.800 | 0.867 | 0.07 | 174 | 1039.0 | 0.875 | 0.932 | 0.825 | 0.885 | 0.999 | 8978 | 1164 | 6 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10840 | 0.725 | 0.790 | 0.666 | 0.14 | 0.706 | 0.712 | 0.05 | 194 | 957.0 | 0.810 | 0.784 | 0.838 | 0.900 | 0.842 | 9130 | 1012 | 1710 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 10840 | 0.759 | 0.825 | 0.698 | 0.28 | 0.757 | 0.784 | 0.25 | 192 | 629.0 | 0.843 | 0.816 | 0.873 | 0.936 | 0.875 | 9490 | 652 | 1350 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10840 | 0.778 | 0.836 | 0.723 | 0.39 | 0.815 | 0.865 | 0.52 | 179 | 272.0 | 0.882 | 0.853 | 0.912 | 0.976 | 0.913 | 9897 | 245 | 943 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10840 | 0.800 | 0.848 | 0.754 | 0.59 | 0.822 | 0.877 | 0.62 | 167 | 218.0 | 0.888 | 0.860 | 0.919 | 0.981 | 0.918 | 9949 | 193 | 891 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10840 | 0.725 | 0.790 | 0.666 | 0.14 | 0.706 | 0.712 | 0.05 | 194 | 957.0 | 0.810 | 0.784 | 0.838 | 0.900 | 0.842 | 9130 | 1012 | 1710 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 10840 | 0.759 | 0.825 | 0.698 | 0.28 | 0.757 | 0.784 | 0.25 | 192 | 629.0 | 0.843 | 0.816 | 0.873 | 0.936 | 0.875 | 9490 | 652 | 1350 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10840 | 0.778 | 0.836 | 0.723 | 0.39 | 0.815 | 0.865 | 0.52 | 179 | 272.0 | 0.882 | 0.853 | 0.912 | 0.976 | 0.913 | 9897 | 245 | 943 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10840 | 0.800 | 0.848 | 0.754 | 0.59 | 0.822 | 0.877 | 0.62 | 167 | 218.0 | 0.888 | 0.860 | 0.919 | 0.981 | 0.918 | 9949 | 193 | 891 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8984; unmatched reference entries: 1158; unmatched candidate entries: 0
- identity switches: 185; fragmentation (coverage interruptions): 990; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 79037: 5 -> 4 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 5 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79037: 5 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 5 -> 8 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 5 -> 7 at (2125, 3030), 2 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 7 -> 8 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 7 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 4 -> 5 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 7 -> 8 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 8 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 3 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 4 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 7 -> 10 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 5 -> 7 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 5 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 3 -> 13 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 7 -> 14 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 7 -> 14 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 5 -> 7 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 4 -> 5 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 12 -> 4 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 10 -> 8 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 14 -> 10 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 8 -> 9 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 9 -> 3 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 14 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 14 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 5 -> 7 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 4 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 12 -> 4 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 9 -> 3 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 3 -> 6 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 9 -> 8 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 3 -> 9 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 7 -> 10 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 5 -> 7 at (2107.5, 3023.5), 1 frames after previous cover
- f110: ref 78897: 3 -> 9 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 8 -> 3 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 6 -> 15 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 14 -> 10 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 14 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79108: 4 -> 5 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 12 -> 4 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 14 -> 10 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 14 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 7 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 4 -> 5 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 12 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 15 -> 1 at (1977.5, 3034.5), 2 frames after previous cover
- f112: ref 79037: 9 -> 6 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 6 -> 15 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 10 -> 16 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 10 -> 17 at (2072.5, 3029.5), 2 frames after previous cover
- ... 125 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 914 | 82 | 0 (914) |
| 78896 | 350 (76..429) | 326 | 21 | 1 (326) |
| 78969 | 352 (80..434) | 307 | 31 | 13 (294), 3 (13) |
| 78971 | 352 (84..439) | 316 | 26 | 17 (273), 9 (21), 6 (19), 15 (1), 1 (1), 13 (1) |
| 79045 | 355 (84..443) | 311 | 37 | 23 (275), 15 (11), 3 (8), 17 (7), 6 (4), 9 (2), 4 (1), 5 (1), 8 (1), 13 (1) |
| 79037 | 355 (86..445) | 316 | 36 | 9 (283), 6 (15), 5 (3), 7 (3), 8 (3), 4 (2), 15 (2), 17 (2), 23 (2), 3 (1) |
| 78897 | 345 (89..450) | 303 | 39 | 3 (267), 17 (10), 6 (8), 8 (7), 9 (5), 5 (2), 7 (2), 4 (1), 23 (1) |
| 78899 | 365 (91..455) | 321 | 37 | 6 (282), 3 (16), 10 (6), 8 (4), 15 (4), 4 (3), 5 (2), 7 (2), 9 (2) |
| 79097 | 366 (94..461) | 312 | 46 | 14 (286), 8 (15), 7 (3), 3 (3), 4 (2), 5 (2), 10 (1) |
| 79098 | 360 (97..467) | 311 | 42 | 15 (280), 14 (14), 3 (4), 5 (3), 7 (3), 10 (3), 4 (1), 16 (1), 17 (1), 8 (1) |
| 79102 | 371 (98..477) | 324 | 38 | 8 (302), 17 (5), 14 (4), 4 (3), 5 (3), 7 (3), 19 (2), 10 (1), 16 (1) |
| 79103 | 380 (99..481) | 325 | 45 | 25 (292), 10 (15), 15 (6), 7 (3), 19 (3), 4 (2), 5 (2), 14 (1), 8 (1) |
| 79105 | 379 (101..484) | 334 | 40 | 19 (313), 7 (4), 5 (3), 18 (3), 12 (2), 4 (2), 14 (2), 16 (2), 21 (2), 10 (1) |
| 79108 | 385 (104..492) | 336 | 39 | 26 (310), 21 (6), 7 (4), 16 (4), 4 (3), 12 (2), 20 (2), 10 (2), 19 (2), 5 (1) |
| 79110 | 388 (106..497) | 336 | 42 | 21 (311), 10 (9), 7 (6), 12 (3), 16 (3), 5 (2), 4 (1), 18 (1) |
| 79111 | 386 (109..500) | 340 | 40 | 10 (317), 7 (10), 4 (3), 18 (3), 20 (3), 5 (2), 12 (1), 16 (1) |
| 79115 | 421 (111..531) | 380 | 40 | 7 (359), 20 (6), 5 (4), 12 (3), 4 (3), 16 (3), 18 (2) |
| 79116 | 411 (114..530) | 363 | 45 | 20 (346), 5 (5), 4 (4), 16 (4), 12 (2), 18 (2) |
| 79122 | 404 (118..532) | 357 | 38 | 5 (342), 18 (5), 16 (4), 12 (3), 4 (3) |
| 79132 | 391 (120..515) | 343 | 43 | 16 (328), 5 (5), 12 (4), 18 (4), 4 (2) |
| 79128 | 402 (124..527) | 350 | 42 | 18 (343), 4 (3), 12 (2), 5 (2) |
| 79134 | 407 (127..533) | 365 | 41 | 22 (360), 12 (3), 4 (2) |
| 79135 | 409 (129..542) | 373 | 33 | 4 (302), 12 (71) |
| 79139 | 406 (132..537) | 365 | 37 | 12 (301), 4 (32), 24 (32) |
| 79136 | 393 (136..538) | 356 | 30 | 24 (320), 4 (36) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 310/367/1005; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 914 | 914 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..428 | 351 | 327 | 327 | 0 | 0 | 0 | 0 | 78896, 78971 |
| 3 | 84..450 | 367 | 312 | 312 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 4 | 86..538 | 453 | 411 | 411 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 5 | 86..532 | 447 | 384 | 384 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 88..454 | 367 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 91..531 | 441 | 402 | 402 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 8 | 93..477 | 385 | 334 | 334 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 97..445 | 349 | 313 | 313 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 10 | 99..500 | 402 | 355 | 355 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..542 | 442 | 397 | 397 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 103..434 | 332 | 296 | 296 | 0 | 0 | 0 | 0 | 78969, 78971, 79045 |
| 14 | 103..461 | 359 | 307 | 307 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 15 | 110..467 | 358 | 304 | 304 | 0 | 0 | 0 | 0 | 78899, 78971, 79037, 79045, 79098, 79103 |
| 16 | 112..515 | 404 | 351 | 351 | 0 | 0 | 0 | 0 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 112..439 | 328 | 298 | 298 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79098, 79102 |
| 18 | 116..527 | 412 | 363 | 363 | 0 | 0 | 0 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 123..484 | 362 | 320 | 320 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108 |
| 20 | 123..530 | 408 | 357 | 357 | 0 | 0 | 0 | 0 | 79108, 79111, 79115, 79116 |
| 21 | 129..495 | 367 | 319 | 319 | 0 | 0 | 0 | 0 | 79105, 79108, 79110 |
| 22 | 133..533 | 401 | 360 | 360 | 0 | 0 | 0 | 0 | 79134 |
| 23 | 134..443 | 310 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 24 | 138..537 | 400 | 352 | 352 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 25 | 141..481 | 341 | 292 | 292 | 0 | 0 | 0 | 0 | 79103 |
| 26 | 141..492 | 352 | 310 | 310 | 0 | 0 | 0 | 0 | 79108 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 8984; unmatched reference entries: 1158; unmatched candidate entries: 0
- identity switches: 185; fragmentation (coverage interruptions): 990; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 79037: 5 -> 4 at (2152.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 5 at (2142, 3030.5), 2 frames after previous cover
- f91: ref 79037: 5 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 5 -> 8 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 5 -> 7 at (2125, 3030), 2 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 7 -> 8 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 7 at (2128, 3029), 1 frames after previous cover
- f96: ref 79097: 4 -> 5 at (2141, 3029), 1 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 4 frames after previous cover
- f98: ref 78897: 7 -> 8 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 8 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 3 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 4 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 7 -> 10 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 5 -> 7 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 5 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 3 -> 13 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 7 -> 14 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 7 -> 14 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 5 -> 7 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 4 -> 5 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 12 -> 4 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 10 -> 8 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 14 -> 10 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 8 -> 9 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 9 -> 3 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 14 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 14 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 5 -> 7 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 4 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 12 -> 4 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 9 -> 3 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 3 -> 6 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 9 -> 8 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 3 -> 9 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 7 -> 10 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 5 -> 7 at (2107.5, 3023.5), 1 frames after previous cover
- f110: ref 78897: 3 -> 9 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 8 -> 3 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 6 -> 15 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 14 -> 10 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 14 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79108: 4 -> 5 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 12 -> 4 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 14 -> 10 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 14 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 7 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 4 -> 5 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 12 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 15 -> 1 at (1977.5, 3034.5), 2 frames after previous cover
- f112: ref 79037: 9 -> 6 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 6 -> 15 at (1988, 3034.5), 2 frames after previous cover
- f112: ref 79098: 10 -> 16 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 10 -> 17 at (2072.5, 3029.5), 2 frames after previous cover
- ... 125 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 914 | 82 | 0 (914) |
| 78896 | 350 (76..429) | 326 | 21 | 1 (326) |
| 78969 | 352 (80..434) | 307 | 31 | 13 (294), 3 (13) |
| 78971 | 352 (84..439) | 316 | 26 | 17 (273), 9 (21), 6 (19), 15 (1), 1 (1), 13 (1) |
| 79045 | 355 (84..443) | 311 | 37 | 23 (275), 15 (11), 3 (8), 17 (7), 6 (4), 9 (2), 4 (1), 5 (1), 8 (1), 13 (1) |
| 79037 | 355 (86..445) | 316 | 36 | 9 (283), 6 (15), 5 (3), 7 (3), 8 (3), 4 (2), 15 (2), 17 (2), 23 (2), 3 (1) |
| 78897 | 345 (89..450) | 303 | 39 | 3 (267), 17 (10), 6 (8), 8 (7), 9 (5), 5 (2), 7 (2), 4 (1), 23 (1) |
| 78899 | 365 (91..455) | 321 | 37 | 6 (282), 3 (16), 10 (6), 8 (4), 15 (4), 4 (3), 5 (2), 7 (2), 9 (2) |
| 79097 | 366 (94..461) | 312 | 46 | 14 (286), 8 (15), 7 (3), 3 (3), 4 (2), 5 (2), 10 (1) |
| 79098 | 360 (97..467) | 311 | 42 | 15 (280), 14 (14), 3 (4), 5 (3), 7 (3), 10 (3), 4 (1), 16 (1), 17 (1), 8 (1) |
| 79102 | 371 (98..477) | 324 | 38 | 8 (302), 17 (5), 14 (4), 4 (3), 5 (3), 7 (3), 19 (2), 10 (1), 16 (1) |
| 79103 | 380 (99..481) | 325 | 45 | 25 (292), 10 (15), 15 (6), 7 (3), 19 (3), 4 (2), 5 (2), 14 (1), 8 (1) |
| 79105 | 379 (101..484) | 334 | 40 | 19 (313), 7 (4), 5 (3), 18 (3), 12 (2), 4 (2), 14 (2), 16 (2), 21 (2), 10 (1) |
| 79108 | 385 (104..492) | 336 | 39 | 26 (310), 21 (6), 7 (4), 16 (4), 4 (3), 12 (2), 20 (2), 10 (2), 19 (2), 5 (1) |
| 79110 | 388 (106..497) | 336 | 42 | 21 (311), 10 (9), 7 (6), 12 (3), 16 (3), 5 (2), 4 (1), 18 (1) |
| 79111 | 386 (109..500) | 340 | 40 | 10 (317), 7 (10), 4 (3), 18 (3), 20 (3), 5 (2), 12 (1), 16 (1) |
| 79115 | 421 (111..531) | 380 | 40 | 7 (359), 20 (6), 5 (4), 12 (3), 4 (3), 16 (3), 18 (2) |
| 79116 | 411 (114..530) | 363 | 45 | 20 (346), 5 (5), 4 (4), 16 (4), 12 (2), 18 (2) |
| 79122 | 404 (118..532) | 357 | 38 | 5 (342), 18 (5), 16 (4), 12 (3), 4 (3) |
| 79132 | 391 (120..515) | 343 | 43 | 16 (328), 5 (5), 12 (4), 18 (4), 4 (2) |
| 79128 | 402 (124..527) | 350 | 42 | 18 (343), 4 (3), 12 (2), 5 (2) |
| 79134 | 407 (127..533) | 365 | 41 | 22 (360), 12 (3), 4 (2) |
| 79135 | 409 (129..542) | 373 | 33 | 4 (302), 12 (71) |
| 79139 | 406 (132..537) | 365 | 37 | 12 (301), 4 (32), 24 (32) |
| 79136 | 393 (136..538) | 356 | 30 | 24 (320), 4 (36) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 310/367/1005; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1007 | 1005 | 914 | 914 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..428 | 351 | 327 | 327 | 0 | 0 | 0 | 0 | 78896, 78971 |
| 3 | 84..450 | 367 | 312 | 312 | 0 | 0 | 0 | 0 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 4 | 86..538 | 453 | 411 | 411 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 5 | 86..532 | 447 | 384 | 384 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 88..454 | 367 | 328 | 328 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 91..531 | 441 | 402 | 402 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 8 | 93..477 | 385 | 334 | 334 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 97..445 | 349 | 313 | 313 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045 |
| 10 | 99..500 | 402 | 355 | 355 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..542 | 442 | 397 | 397 | 0 | 0 | 0 | 0 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 103..434 | 332 | 296 | 296 | 0 | 0 | 0 | 0 | 78969, 78971, 79045 |
| 14 | 103..461 | 359 | 307 | 307 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105 |
| 15 | 110..467 | 358 | 304 | 304 | 0 | 0 | 0 | 0 | 78899, 78971, 79037, 79045, 79098, 79103 |
| 16 | 112..515 | 404 | 351 | 351 | 0 | 0 | 0 | 0 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 112..439 | 328 | 298 | 298 | 0 | 0 | 0 | 0 | 78897, 78971, 79037, 79045, 79098, 79102 |
| 18 | 116..527 | 412 | 363 | 363 | 0 | 0 | 0 | 0 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 123..484 | 362 | 320 | 320 | 0 | 0 | 0 | 0 | 79102, 79103, 79105, 79108 |
| 20 | 123..530 | 408 | 357 | 357 | 0 | 0 | 0 | 0 | 79108, 79111, 79115, 79116 |
| 21 | 129..495 | 367 | 319 | 319 | 0 | 0 | 0 | 0 | 79105, 79108, 79110 |
| 22 | 133..533 | 401 | 360 | 360 | 0 | 0 | 0 | 0 | 79134 |
| 23 | 134..443 | 310 | 278 | 278 | 0 | 0 | 0 | 0 | 78897, 79037, 79045 |
| 24 | 138..537 | 400 | 352 | 352 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 25 | 141..481 | 341 | 292 | 292 | 0 | 0 | 0 | 0 | 79103 |
| 26 | 141..492 | 352 | 310 | 310 | 0 | 0 | 0 | 0 | 79108 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9897; unmatched reference entries: 245; unmatched candidate entries: 943
- identity switches: 179; fragmentation (coverage interruptions): 171; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79037: 5 -> 4 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 5 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 5 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 5 -> 8 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 5 -> 7 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 7 -> 8 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 7 at (2128, 3029), 1 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 4 -> 5 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 7 -> 8 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 8 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 3 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 4 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 7 -> 10 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 5 -> 7 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 5 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 3 -> 13 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 7 -> 14 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 7 -> 14 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 5 -> 7 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 4 -> 5 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 12 -> 4 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 10 -> 8 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 14 -> 10 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 8 -> 9 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 9 -> 3 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 14 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 14 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 5 -> 7 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 4 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 12 -> 4 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 9 -> 3 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 3 -> 6 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 9 -> 8 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 3 -> 9 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 7 -> 10 at (2097, 3024.5), 1 frames after previous cover
- f110: ref 78897: 3 -> 9 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 8 -> 3 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 6 -> 15 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 14 -> 10 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 14 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 5 -> 7 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 4 -> 5 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 12 -> 4 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 14 -> 10 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 14 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 7 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 4 -> 5 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 12 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 15 -> 1 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 9 -> 6 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 6 -> 15 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79098: 10 -> 16 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 10 -> 17 at (2072.5, 3029.5), 2 frames after previous cover
- ... 119 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1003 | 3 | 0 (1003) |
| 78896 | 350 (76..429) | 347 | 1 | 1 (347) |
| 78969 | 352 (80..434) | 333 | 10 | 13 (319), 3 (14) |
| 78971 | 352 (84..439) | 339 | 6 | 17 (294), 9 (22), 6 (19), 15 (2), 1 (1), 13 (1) |
| 79045 | 355 (84..443) | 341 | 8 | 23 (302), 15 (12), 3 (8), 17 (7), 6 (5), 8 (2), 9 (2), 4 (1), 5 (1), 13 (1) |
| 79037 | 355 (86..445) | 342 | 10 | 9 (309), 6 (15), 5 (4), 7 (3), 8 (3), 15 (2), 17 (2), 23 (2), 4 (1), 3 (1) |
| 78897 | 345 (89..450) | 335 | 9 | 3 (297), 17 (10), 6 (8), 8 (7), 9 (5), 5 (3), 4 (2), 7 (2), 23 (1) |
| 78899 | 365 (91..455) | 356 | 7 | 6 (317), 3 (16), 10 (6), 8 (4), 15 (4), 4 (3), 5 (2), 7 (2), 9 (2) |
| 79097 | 366 (94..461) | 350 | 14 | 14 (323), 8 (16), 4 (3), 7 (3), 3 (3), 5 (1), 10 (1) |
| 79098 | 360 (97..467) | 348 | 8 | 15 (315), 14 (15), 3 (5), 5 (3), 7 (3), 10 (3), 4 (1), 16 (1), 17 (1), 8 (1) |
| 79102 | 371 (98..477) | 357 | 10 | 8 (335), 17 (5), 14 (4), 4 (3), 5 (3), 7 (3), 19 (2), 10 (1), 16 (1) |
| 79103 | 380 (99..481) | 367 | 6 | 25 (330), 10 (15), 15 (6), 8 (4), 4 (3), 7 (3), 19 (3), 5 (2), 14 (1) |
| 79105 | 379 (101..484) | 368 | 9 | 19 (347), 5 (4), 7 (3), 18 (3), 12 (2), 4 (2), 14 (2), 16 (2), 21 (2), 10 (1) |
| 79108 | 385 (104..492) | 369 | 10 | 26 (341), 21 (6), 7 (5), 4 (4), 16 (4), 12 (2), 20 (2), 10 (2), 19 (2), 5 (1) |
| 79110 | 388 (106..497) | 379 | 7 | 21 (352), 10 (9), 7 (6), 16 (4), 12 (3), 5 (3), 4 (1), 18 (1) |
| 79111 | 386 (109..500) | 379 | 4 | 10 (356), 7 (9), 4 (3), 5 (3), 18 (3), 20 (3), 12 (1), 16 (1) |
| 79115 | 421 (111..531) | 417 | 3 | 7 (396), 20 (6), 5 (4), 12 (3), 4 (3), 16 (3), 18 (2) |
| 79116 | 411 (114..530) | 405 | 5 | 20 (387), 12 (4), 4 (4), 5 (4), 16 (4), 18 (2) |
| 79122 | 404 (118..532) | 394 | 9 | 5 (379), 18 (5), 16 (4), 12 (3), 4 (3) |
| 79132 | 391 (120..515) | 382 | 9 | 16 (367), 5 (5), 12 (4), 18 (4), 4 (2) |
| 79128 | 402 (124..527) | 390 | 8 | 18 (382), 4 (3), 5 (3), 12 (2) |
| 79134 | 407 (127..533) | 404 | 3 | 22 (399), 12 (3), 4 (2) |
| 79135 | 409 (129..542) | 404 | 3 | 4 (328), 12 (76) |
| 79139 | 406 (132..537) | 402 | 4 | 12 (332), 4 (70) |
| 79136 | 393 (136..538) | 386 | 5 | 24 (386) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 339/396/1006; tracks with internal gaps: 25; total internal gaps: 217; longest internal gap: 4; tracks ending in coasting: 24 (trailing rows total 691)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 1003 | 3 | 3 | 1 | 0 | 78911 |
| 1 | 78..457 | 380 | 380 | 348 | 32 | 2 | 3 | 28 | 78896, 78971 |
| 3 | 84..479 | 396 | 396 | 344 | 52 | 21 | 2 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 4 | 86..567 | 482 | 482 | 442 | 40 | 9 | 2 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 86..561 | 476 | 476 | 425 | 51 | 20 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 88..483 | 396 | 396 | 364 | 32 | 4 | 1 | 28 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 91..560 | 470 | 470 | 438 | 32 | 3 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 8 | 93..506 | 414 | 414 | 372 | 42 | 15 | 2 | 25 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 97..474 | 378 | 378 | 340 | 38 | 6 | 3 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 10 | 99..529 | 431 | 431 | 394 | 37 | 7 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..571 | 471 | 471 | 435 | 36 | 6 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 103..463 | 361 | 361 | 321 | 40 | 9 | 2 | 29 | 78969, 78971, 79045 |
| 14 | 103..490 | 388 | 388 | 345 | 43 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105 |
| 15 | 110..496 | 387 | 387 | 341 | 46 | 12 | 4 | 29 | 78899, 78971, 79037, 79045, 79098, 79103 |
| 16 | 112..544 | 433 | 433 | 391 | 42 | 13 | 1 | 29 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 112..468 | 357 | 357 | 319 | 38 | 8 | 2 | 29 | 78897, 78971, 79037, 79045, 79098, 79102 |
| 18 | 116..556 | 441 | 441 | 402 | 39 | 8 | 2 | 29 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 123..513 | 391 | 391 | 354 | 37 | 7 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 20 | 123..559 | 437 | 437 | 398 | 39 | 8 | 2 | 29 | 79108, 79111, 79115, 79116 |
| 21 | 129..524 | 396 | 396 | 360 | 36 | 7 | 3 | 27 | 79105, 79108, 79110 |
| 22 | 133..562 | 430 | 430 | 399 | 31 | 2 | 1 | 29 | 79134 |
| 23 | 134..472 | 339 | 339 | 305 | 34 | 5 | 1 | 29 | 78897, 79037, 79045 |
| 24 | 138..566 | 429 | 429 | 386 | 43 | 14 | 2 | 28 | 79136 |
| 25 | 141..510 | 370 | 370 | 330 | 40 | 6 | 2 | 32 | 79103 |
| 26 | 141..521 | 381 | 381 | 341 | 40 | 9 | 2 | 29 | 79108 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9897; unmatched reference entries: 245; unmatched candidate entries: 943
- identity switches: 179; fragmentation (coverage interruptions): 171; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f88: ref 79037: 5 -> 4 at (2147.5, 3033.5), 1 frames after previous cover
- f88: ref 79045: 4 -> 5 at (2135.5, 3033), 2 frames after previous cover
- f89: ref 79037: 4 -> 5 at (2141, 3034.5), 1 frames after previous cover
- f91: ref 78897: 4 -> 5 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 5 -> 7 at (2129, 3033.5), 1 frames after previous cover
- f93: ref 79045: 5 -> 8 at (2106.5, 3031.5), 5 frames after previous cover
- f94: ref 78897: 5 -> 7 at (2125, 3030), 1 frames after previous cover
- f94: ref 78899: 4 -> 5 at (2140.5, 3029), 1 frames after previous cover
- f95: ref 79037: 7 -> 8 at (2105, 3034.5), 2 frames after previous cover
- f96: ref 78899: 5 -> 7 at (2128, 3029), 1 frames after previous cover
- f97: ref 79045: 8 -> 9 at (2081.5, 3032), 3 frames after previous cover
- f97: ref 79097: 4 -> 5 at (2135, 3028), 1 frames after previous cover
- f98: ref 78897: 7 -> 8 at (2100, 3031), 3 frames after previous cover
- f98: ref 79037: 8 -> 9 at (2087, 3034), 1 frames after previous cover
- f98: ref 79045: 9 -> 3 at (2075.5, 3033), 1 frames after previous cover
- f98: ref 79097: 5 -> 7 at (2129, 3028), 1 frames after previous cover
- f98: ref 79098: 4 -> 5 at (2141.5, 3026.5), 1 frames after previous cover
- f99: ref 78899: 7 -> 10 at (2109.5, 3030), 2 frames after previous cover
- f101: ref 79098: 5 -> 7 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 4 -> 5 at (2136, 3025.5), 1 frames after previous cover
- f103: ref 78969: 3 -> 13 at (2014.5, 3033.5), 6 frames after previous cover
- f103: ref 79097: 7 -> 14 at (2100, 3028.5), 3 frames after previous cover
- f104: ref 79098: 7 -> 14 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 5 -> 7 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 4 -> 5 at (2126, 3022.5), 1 frames after previous cover
- f104: ref 79105: 12 -> 4 at (2137, 3025), 1 frames after previous cover
- f105: ref 78899: 10 -> 8 at (2074, 3031), 1 frames after previous cover
- f105: ref 79097: 14 -> 10 at (2088, 3029), 2 frames after previous cover
- f106: ref 78897: 8 -> 9 at (2052.5, 3032.5), 2 frames after previous cover
- f106: ref 79037: 9 -> 3 at (2038, 3034.5), 1 frames after previous cover
- f106: ref 79098: 14 -> 10 at (2096, 3028.5), 1 frames after previous cover
- f106: ref 79102: 7 -> 14 at (2107.5, 3028.5), 1 frames after previous cover
- f106: ref 79103: 5 -> 7 at (2116.5, 3023), 1 frames after previous cover
- f106: ref 79105: 4 -> 5 at (2125, 3025.5), 1 frames after previous cover
- f106: ref 79108: 12 -> 4 at (2141.5, 3026), 1 frames after previous cover
- f107: ref 78897: 9 -> 3 at (2046.5, 3031.5), 1 frames after previous cover
- f107: ref 78899: 8 -> 9 at (2062.5, 3030.5), 1 frames after previous cover
- f107: ref 79045: 3 -> 6 at (2019, 3033.5), 2 frames after previous cover
- f107: ref 79097: 10 -> 8 at (2076.5, 3029), 2 frames after previous cover
- f109: ref 78899: 9 -> 8 at (2049.5, 3031), 1 frames after previous cover
- f109: ref 79037: 3 -> 9 at (2019.5, 3034), 3 frames after previous cover
- f109: ref 79103: 7 -> 10 at (2097, 3024.5), 1 frames after previous cover
- f110: ref 78897: 3 -> 9 at (2028, 3032.5), 1 frames after previous cover
- f110: ref 78899: 8 -> 3 at (2043, 3030.5), 1 frames after previous cover
- f110: ref 78971: 6 -> 15 at (1990.5, 3034), 4 frames after previous cover
- f110: ref 79102: 14 -> 10 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 10 -> 14 at (2092.5, 3023.5), 1 frames after previous cover
- f110: ref 79105: 5 -> 7 at (2101.5, 3024.5), 1 frames after previous cover
- f110: ref 79108: 4 -> 5 at (2118, 3025), 1 frames after previous cover
- f110: ref 79110: 12 -> 4 at (2134, 3026), 1 frames after previous cover
- f111: ref 79103: 14 -> 10 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 7 -> 14 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 7 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 4 -> 5 at (2129, 3027), 1 frames after previous cover
- f111: ref 79111: 12 -> 4 at (2142, 3026.5), 1 frames after previous cover
- f112: ref 78971: 15 -> 1 at (1977.5, 3034.5), 1 frames after previous cover
- f112: ref 79037: 9 -> 6 at (2000.5, 3035), 3 frames after previous cover
- f112: ref 79045: 6 -> 15 at (1988, 3034.5), 1 frames after previous cover
- f112: ref 79098: 10 -> 16 at (2059, 3029.5), 4 frames after previous cover
- f112: ref 79102: 10 -> 17 at (2072.5, 3029.5), 2 frames after previous cover
- ... 119 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1003 | 3 | 0 (1003) |
| 78896 | 350 (76..429) | 347 | 1 | 1 (347) |
| 78969 | 352 (80..434) | 333 | 10 | 13 (319), 3 (14) |
| 78971 | 352 (84..439) | 339 | 6 | 17 (294), 9 (22), 6 (19), 15 (2), 1 (1), 13 (1) |
| 79045 | 355 (84..443) | 341 | 8 | 23 (302), 15 (12), 3 (8), 17 (7), 6 (5), 8 (2), 9 (2), 4 (1), 5 (1), 13 (1) |
| 79037 | 355 (86..445) | 342 | 10 | 9 (309), 6 (15), 5 (4), 7 (3), 8 (3), 15 (2), 17 (2), 23 (2), 4 (1), 3 (1) |
| 78897 | 345 (89..450) | 335 | 9 | 3 (297), 17 (10), 6 (8), 8 (7), 9 (5), 5 (3), 4 (2), 7 (2), 23 (1) |
| 78899 | 365 (91..455) | 356 | 7 | 6 (317), 3 (16), 10 (6), 8 (4), 15 (4), 4 (3), 5 (2), 7 (2), 9 (2) |
| 79097 | 366 (94..461) | 350 | 14 | 14 (323), 8 (16), 4 (3), 7 (3), 3 (3), 5 (1), 10 (1) |
| 79098 | 360 (97..467) | 348 | 8 | 15 (315), 14 (15), 3 (5), 5 (3), 7 (3), 10 (3), 4 (1), 16 (1), 17 (1), 8 (1) |
| 79102 | 371 (98..477) | 357 | 10 | 8 (335), 17 (5), 14 (4), 4 (3), 5 (3), 7 (3), 19 (2), 10 (1), 16 (1) |
| 79103 | 380 (99..481) | 367 | 6 | 25 (330), 10 (15), 15 (6), 8 (4), 4 (3), 7 (3), 19 (3), 5 (2), 14 (1) |
| 79105 | 379 (101..484) | 368 | 9 | 19 (347), 5 (4), 7 (3), 18 (3), 12 (2), 4 (2), 14 (2), 16 (2), 21 (2), 10 (1) |
| 79108 | 385 (104..492) | 369 | 10 | 26 (341), 21 (6), 7 (5), 4 (4), 16 (4), 12 (2), 20 (2), 10 (2), 19 (2), 5 (1) |
| 79110 | 388 (106..497) | 379 | 7 | 21 (352), 10 (9), 7 (6), 16 (4), 12 (3), 5 (3), 4 (1), 18 (1) |
| 79111 | 386 (109..500) | 379 | 4 | 10 (356), 7 (9), 4 (3), 5 (3), 18 (3), 20 (3), 12 (1), 16 (1) |
| 79115 | 421 (111..531) | 417 | 3 | 7 (396), 20 (6), 5 (4), 12 (3), 4 (3), 16 (3), 18 (2) |
| 79116 | 411 (114..530) | 405 | 5 | 20 (387), 12 (4), 4 (4), 5 (4), 16 (4), 18 (2) |
| 79122 | 404 (118..532) | 394 | 9 | 5 (379), 18 (5), 16 (4), 12 (3), 4 (3) |
| 79132 | 391 (120..515) | 382 | 9 | 16 (367), 5 (5), 12 (4), 18 (4), 4 (2) |
| 79128 | 402 (124..527) | 390 | 8 | 18 (382), 4 (3), 5 (3), 12 (2) |
| 79134 | 407 (127..533) | 404 | 3 | 22 (399), 12 (3), 4 (2) |
| 79135 | 409 (129..542) | 404 | 3 | 4 (328), 12 (76) |
| 79139 | 406 (132..537) | 402 | 4 | 12 (332), 4 (70) |
| 79136 | 393 (136..538) | 386 | 5 | 24 (386) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 339/396/1006; tracks with internal gaps: 25; total internal gaps: 217; longest internal gap: 4; tracks ending in coasting: 24 (trailing rows total 691)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3..1008 | 1006 | 1006 | 1003 | 3 | 3 | 1 | 0 | 78911 |
| 1 | 78..457 | 380 | 380 | 348 | 32 | 2 | 3 | 28 | 78896, 78971 |
| 3 | 84..479 | 396 | 396 | 344 | 52 | 21 | 2 | 29 | 78897, 78899, 78969, 79037, 79045, 79097, 79098 |
| 4 | 86..567 | 482 | 482 | 442 | 40 | 9 | 2 | 30 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 5 | 86..561 | 476 | 476 | 425 | 51 | 20 | 2 | 29 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 6 | 88..483 | 396 | 396 | 364 | 32 | 4 | 1 | 28 | 78897, 78899, 78971, 79037, 79045 |
| 7 | 91..560 | 470 | 470 | 438 | 32 | 3 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 8 | 93..506 | 414 | 414 | 372 | 42 | 15 | 2 | 25 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103 |
| 9 | 97..474 | 378 | 378 | 340 | 38 | 6 | 3 | 29 | 78897, 78899, 78971, 79037, 79045 |
| 10 | 99..529 | 431 | 431 | 394 | 37 | 7 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 12 | 101..571 | 471 | 471 | 435 | 36 | 6 | 2 | 29 | 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 13 | 103..463 | 361 | 361 | 321 | 40 | 9 | 2 | 29 | 78969, 78971, 79045 |
| 14 | 103..490 | 388 | 388 | 345 | 43 | 13 | 2 | 29 | 79097, 79098, 79102, 79103, 79105 |
| 15 | 110..496 | 387 | 387 | 341 | 46 | 12 | 4 | 29 | 78899, 78971, 79037, 79045, 79098, 79103 |
| 16 | 112..544 | 433 | 433 | 391 | 42 | 13 | 1 | 29 | 79098, 79102, 79105, 79108, 79110, 79111, 79115, 79116, 79122, 79132 |
| 17 | 112..468 | 357 | 357 | 319 | 38 | 8 | 2 | 29 | 78897, 78971, 79037, 79045, 79098, 79102 |
| 18 | 116..556 | 441 | 441 | 402 | 39 | 8 | 2 | 29 | 79105, 79110, 79111, 79115, 79116, 79122, 79128, 79132 |
| 19 | 123..513 | 391 | 391 | 354 | 37 | 7 | 2 | 29 | 79102, 79103, 79105, 79108 |
| 20 | 123..559 | 437 | 437 | 398 | 39 | 8 | 2 | 29 | 79108, 79111, 79115, 79116 |
| 21 | 129..524 | 396 | 396 | 360 | 36 | 7 | 3 | 27 | 79105, 79108, 79110 |
| 22 | 133..562 | 430 | 430 | 399 | 31 | 2 | 1 | 29 | 79134 |
| 23 | 134..472 | 339 | 339 | 305 | 34 | 5 | 1 | 29 | 78897, 79037, 79045 |
| 24 | 138..566 | 429 | 429 | 386 | 43 | 14 | 2 | 28 | 79136 |
| 25 | 141..510 | 370 | 370 | 330 | 40 | 6 | 2 | 32 | 79103 |
| 26 | 141..521 | 381 | 381 | 341 | 40 | 9 | 2 | 29 | 79108 |
