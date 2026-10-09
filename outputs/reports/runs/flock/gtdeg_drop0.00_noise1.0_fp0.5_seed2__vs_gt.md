# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=677883ac3555
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise1.0_fp0.5_seed2/tracks.csv sha256=aad52eabf360f33e
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise1.0_fp0.5_seed2.csv sha256=677883ac3555c2f5
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise1.0_fp0.5_seed2
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
| observations | none | 4 | 10142 | 10103 | 0.755 | 0.820 | 0.696 | 1.07 | 0.912 | 0.987 | 1.27 | 40 | 128.0 | 0.917 | 0.919 | 0.915 | 0.994 | 0.998 | 10079 | 63 | 24 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 10103 | 0.815 | 0.884 | 0.750 | 1.15 | 0.913 | 0.990 | 1.27 | 40 | 116.0 | 0.919 | 0.920 | 0.917 | 0.995 | 0.999 | 10091 | 51 | 12 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10103 | 0.845 | 0.911 | 0.784 | 1.19 | 0.911 | 0.990 | 1.28 | 40 | 115.0 | 0.919 | 0.921 | 0.917 | 0.995 | 0.999 | 10090 | 52 | 13 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10103 | 0.879 | 0.936 | 0.826 | 1.30 | 0.908 | 0.989 | 1.30 | 43 | 116.0 | 0.920 | 0.922 | 0.918 | 0.995 | 0.999 | 10090 | 52 | 13 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10103 | 0.755 | 0.820 | 0.696 | 1.07 | 0.912 | 0.987 | 1.27 | 40 | 128.0 | 0.917 | 0.919 | 0.915 | 0.994 | 0.998 | 10079 | 63 | 24 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 10103 | 0.815 | 0.884 | 0.750 | 1.15 | 0.913 | 0.990 | 1.27 | 40 | 116.0 | 0.919 | 0.920 | 0.917 | 0.995 | 0.999 | 10091 | 51 | 12 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10103 | 0.845 | 0.911 | 0.784 | 1.19 | 0.911 | 0.990 | 1.28 | 40 | 115.0 | 0.919 | 0.921 | 0.917 | 0.995 | 0.999 | 10090 | 52 | 13 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10103 | 0.879 | 0.936 | 0.826 | 1.30 | 0.908 | 0.989 | 1.30 | 43 | 116.0 | 0.920 | 0.922 | 0.918 | 0.995 | 0.999 | 10090 | 52 | 13 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 11002 | 0.699 | 0.755 | 0.647 | 1.07 | 0.841 | 0.899 | 1.27 | 39 | 128.0 | 0.878 | 0.844 | 0.916 | 0.994 | 0.916 | 10079 | 63 | 923 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 11002 | 0.753 | 0.813 | 0.697 | 1.15 | 0.843 | 0.901 | 1.27 | 39 | 116.0 | 0.880 | 0.846 | 0.917 | 0.995 | 0.917 | 10091 | 51 | 911 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 11002 | 0.781 | 0.838 | 0.728 | 1.19 | 0.841 | 0.901 | 1.28 | 35 | 115.0 | 0.880 | 0.846 | 0.918 | 0.995 | 0.917 | 10090 | 52 | 912 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 11002 | 0.813 | 0.861 | 0.767 | 1.30 | 0.839 | 0.901 | 1.29 | 36 | 116.0 | 0.882 | 0.847 | 0.919 | 0.995 | 0.917 | 10090 | 52 | 912 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 11002 | 0.699 | 0.755 | 0.647 | 1.07 | 0.841 | 0.899 | 1.27 | 39 | 128.0 | 0.878 | 0.844 | 0.916 | 0.994 | 0.916 | 10079 | 63 | 923 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 11002 | 0.753 | 0.813 | 0.697 | 1.15 | 0.843 | 0.901 | 1.27 | 39 | 116.0 | 0.880 | 0.846 | 0.917 | 0.995 | 0.917 | 10091 | 51 | 911 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 11002 | 0.781 | 0.838 | 0.728 | 1.19 | 0.841 | 0.901 | 1.28 | 35 | 115.0 | 0.880 | 0.846 | 0.918 | 0.995 | 0.917 | 10090 | 52 | 912 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 11002 | 0.813 | 0.861 | 0.767 | 1.30 | 0.839 | 0.901 | 1.29 | 36 | 116.0 | 0.882 | 0.847 | 0.919 | 0.995 | 0.917 | 10090 | 52 | 912 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 13
- identity switches: 40; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 45 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 45 -> 43 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 43 -> 48 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 45 -> 50 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 45 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 54 -> 55 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 45 -> 58 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 67 -> 68 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 54 -> 45 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 59 -> 54 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 59 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 65 -> 63 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 67 -> 65 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 69 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 72 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 72 -> 69 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 45 -> 78 at (1952.5, 3031), 4 frames after previous cover
- f210: ref 79132: 69 -> 67 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 67 -> 69 at (1579, 3004.5), 1 frames after previous cover
- f290: ref 79134: 73 -> 72 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 76 -> 73 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79139: 84 -> 76 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 72 -> 73 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 73 -> 76 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 76 -> 87 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 87 -> 84 at (1184, 2971.5), 2 frames after previous cover
- f359: ref 78896: 38 -> 40 at (359, 2955), 1 frames after previous cover
- f359: ref 78969: 40 -> 42 at (383, 2957), 1 frames after previous cover
- f359: ref 78971: 42 -> 43 at (409.5, 2964), 1 frames after previous cover
- f359: ref 79037: 43 -> 46 at (441, 2964.5), 1 frames after previous cover
- f360: ref 78896: 40 -> 38 at (352, 2955), 1 frames after previous cover
- f360: ref 78969: 42 -> 40 at (377.5, 2956), 1 frames after previous cover
- f360: ref 78971: 43 -> 42 at (404, 2961.5), 1 frames after previous cover
- f360: ref 79037: 46 -> 48 at (436, 2965), 1 frames after previous cover
- f360: ref 79045: 48 -> 43 at (421, 2965.5), 1 frames after previous cover
- f467: ref 79139: 87 -> 76 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 76 -> 87 at (399.5, 2892.5), 2 frames after previous cover
- f479: ref 79139: 76 -> 84 at (332.5, 2877.5), 1 frames after previous cover
- f480: ref 79136: 84 -> 76 at (324, 2876.5), 2 frames after previous cover
- f538: ref 79136: 76 -> 84 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 1 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (347), 40 (1) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (349), 42 (1) |
| 78971 | 352 (84..439) | 350 | 0 | 42 (349), 43 (1) |
| 79045 | 355 (84..443) | 351 | 1 | 48 (266), 43 (85) |
| 79037 | 355 (86..445) | 351 | 1 | 43 (263), 48 (86), 45 (1), 46 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 46 (343), 45 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 50 (360), 45 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (361), 45 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (354), 45 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 78 (338), 45 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 55 (377), 54 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 45 (352), 54 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 54 (360), 59 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 59 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 63 (366), 65 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (416), 67 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 65 (396), 67 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (393), 69 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 69 (381), 72 (7), 67 (1) |
| 79128 | 402 (124..527) | 400 | 0 | 72 (397), 73 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 73 (404), 72 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 76 (333), 87 (75), 73 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 84 (215), 87 (176), 76 (13) |
| 79136 | 393 (136..538) | 391 | 0 | 84 (185), 87 (148), 76 (58) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 328 | 651..651 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 1/392/1007; tracks with internal gaps: 5; total internal gaps: 5; longest internal gap: 1; tracks ending in coasting: 2 (trailing rows total 8)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..429 | 352 | 348 | 347 | 1 | 1 | 1 | 0 | 78896 |
| 40 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 42 | 86..439 | 354 | 350 | 350 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 43 | 86..443 | 358 | 349 | 349 | 0 | 0 | 0 | 0 | 78971, 79037, 79045 |
| 45 | 88..484 | 397 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 46 | 91..450 | 360 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 79037 |
| 48 | 93..445 | 353 | 352 | 352 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 50 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 52 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 54 | 100..492 | 393 | 388 | 388 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |
| 55 | 101..481 | 381 | 378 | 377 | 1 | 1 | 1 | 0 | 79103 |
| 58 | 103..467 | 365 | 355 | 354 | 1 | 1 | 1 | 0 | 79098 |
| 59 | 106..497 | 392 | 390 | 390 | 0 | 0 | 0 | 0 | 79108, 79110 |
| 63 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 65 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 67 | 113..598 | 486 | 417 | 410 | 7 | 0 | 0 | 7 | 79115, 79116, 79122, 79132 |
| 68 | 116..531 | 416 | 416 | 416 | 0 | 0 | 0 | 0 | 79115 |
| 69 | 120..515 | 396 | 390 | 390 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 72 | 122..527 | 406 | 405 | 405 | 0 | 0 | 0 | 0 | 79128, 79132, 79134 |
| 73 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134, 79135 |
| 76 | 129..537 | 409 | 404 | 404 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 78 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 84 | 134..538 | 405 | 401 | 400 | 1 | 1 | 1 | 0 | 79136, 79139 |
| 87 | 138..542 | 405 | 400 | 399 | 1 | 1 | 1 | 0 | 79135, 79136, 79139 |
| 328 | 651..651 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 13
- identity switches: 40; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 45 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 45 -> 43 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 43 -> 48 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 45 -> 50 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 45 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 54 -> 55 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 45 -> 58 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 67 -> 68 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 54 -> 45 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 59 -> 54 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 59 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 65 -> 63 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 67 -> 65 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 69 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 72 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 72 -> 69 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 45 -> 78 at (1952.5, 3031), 4 frames after previous cover
- f210: ref 79132: 69 -> 67 at (1586.5, 3007.5), 1 frames after previous cover
- f211: ref 79132: 67 -> 69 at (1579, 3004.5), 1 frames after previous cover
- f290: ref 79134: 73 -> 72 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 76 -> 73 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79139: 84 -> 76 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 72 -> 73 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 73 -> 76 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 76 -> 87 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 87 -> 84 at (1184, 2971.5), 2 frames after previous cover
- f359: ref 78896: 38 -> 40 at (359, 2955), 1 frames after previous cover
- f359: ref 78969: 40 -> 42 at (383, 2957), 1 frames after previous cover
- f359: ref 78971: 42 -> 43 at (409.5, 2964), 1 frames after previous cover
- f359: ref 79037: 43 -> 46 at (441, 2964.5), 1 frames after previous cover
- f360: ref 78896: 40 -> 38 at (352, 2955), 1 frames after previous cover
- f360: ref 78969: 42 -> 40 at (377.5, 2956), 1 frames after previous cover
- f360: ref 78971: 43 -> 42 at (404, 2961.5), 1 frames after previous cover
- f360: ref 79037: 46 -> 48 at (436, 2965), 1 frames after previous cover
- f360: ref 79045: 48 -> 43 at (421, 2965.5), 1 frames after previous cover
- f467: ref 79139: 87 -> 76 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 76 -> 87 at (399.5, 2892.5), 2 frames after previous cover
- f479: ref 79139: 76 -> 84 at (332.5, 2877.5), 1 frames after previous cover
- f480: ref 79136: 84 -> 76 at (324, 2876.5), 2 frames after previous cover
- f538: ref 79136: 76 -> 84 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 1 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (347), 40 (1) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (349), 42 (1) |
| 78971 | 352 (84..439) | 350 | 0 | 42 (349), 43 (1) |
| 79045 | 355 (84..443) | 351 | 1 | 48 (266), 43 (85) |
| 79037 | 355 (86..445) | 351 | 1 | 43 (263), 48 (86), 45 (1), 46 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 46 (343), 45 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 50 (360), 45 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (361), 45 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (354), 45 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 78 (338), 45 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 55 (377), 54 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 45 (352), 54 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 54 (360), 59 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 59 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 63 (366), 65 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (416), 67 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 65 (396), 67 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (393), 69 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 69 (381), 72 (7), 67 (1) |
| 79128 | 402 (124..527) | 400 | 0 | 72 (397), 73 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 73 (404), 72 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 76 (333), 87 (75), 73 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 84 (215), 87 (176), 76 (13) |
| 79136 | 393 (136..538) | 391 | 0 | 84 (185), 87 (148), 76 (58) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 328 | 651..651 | 1 | 0 | 1 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 1/392/1007; tracks with internal gaps: 5; total internal gaps: 5; longest internal gap: 1; tracks ending in coasting: 2 (trailing rows total 8)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..429 | 352 | 348 | 347 | 1 | 1 | 1 | 0 | 78896 |
| 40 | 82..434 | 353 | 350 | 350 | 0 | 0 | 0 | 0 | 78896, 78969 |
| 42 | 86..439 | 354 | 350 | 350 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 43 | 86..443 | 358 | 349 | 349 | 0 | 0 | 0 | 0 | 78971, 79037, 79045 |
| 45 | 88..484 | 397 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 46 | 91..450 | 360 | 344 | 344 | 0 | 0 | 0 | 0 | 78897, 79037 |
| 48 | 93..445 | 353 | 352 | 352 | 0 | 0 | 0 | 0 | 79037, 79045 |
| 50 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 52 | 99..461 | 363 | 361 | 361 | 0 | 0 | 0 | 0 | 79097 |
| 54 | 100..492 | 393 | 388 | 388 | 0 | 0 | 0 | 0 | 79103, 79105, 79108 |
| 55 | 101..481 | 381 | 378 | 377 | 1 | 1 | 1 | 0 | 79103 |
| 58 | 103..467 | 365 | 355 | 354 | 1 | 1 | 1 | 0 | 79098 |
| 59 | 106..497 | 392 | 390 | 390 | 0 | 0 | 0 | 0 | 79108, 79110 |
| 63 | 110..500 | 391 | 384 | 384 | 0 | 0 | 0 | 0 | 79110, 79111 |
| 65 | 111..530 | 420 | 414 | 414 | 0 | 0 | 0 | 0 | 79111, 79116 |
| 67 | 113..598 | 486 | 417 | 410 | 7 | 0 | 0 | 7 | 79115, 79116, 79122, 79132 |
| 68 | 116..531 | 416 | 416 | 416 | 0 | 0 | 0 | 0 | 79115 |
| 69 | 120..515 | 396 | 390 | 390 | 0 | 0 | 0 | 0 | 79122, 79132 |
| 72 | 122..527 | 406 | 405 | 405 | 0 | 0 | 0 | 0 | 79128, 79132, 79134 |
| 73 | 126..533 | 408 | 408 | 408 | 0 | 0 | 0 | 0 | 79128, 79134, 79135 |
| 76 | 129..537 | 409 | 404 | 404 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 78 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 84 | 134..538 | 405 | 401 | 400 | 1 | 1 | 1 | 0 | 79136, 79139 |
| 87 | 138..542 | 405 | 400 | 399 | 1 | 1 | 1 | 0 | 79135, 79136, 79139 |
| 328 | 651..651 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 912
- identity switches: 35; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 45 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 45 -> 43 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 43 -> 48 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 45 -> 50 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 45 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 54 -> 55 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 45 -> 58 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 67 -> 68 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 54 -> 45 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 59 -> 54 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 59 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 65 -> 63 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 67 -> 65 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 69 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 72 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 72 -> 69 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 45 -> 78 at (1952.5, 3031), 4 frames after previous cover
- f290: ref 79134: 73 -> 72 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 76 -> 73 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79139: 84 -> 76 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 72 -> 73 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 73 -> 76 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 76 -> 87 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 87 -> 84 at (1184, 2971.5), 2 frames after previous cover
- f359: ref 78896: 38 -> 40 at (359, 2955), 1 frames after previous cover
- f359: ref 78969: 40 -> 42 at (383, 2957), 1 frames after previous cover
- f359: ref 78971: 42 -> 43 at (409.5, 2964), 1 frames after previous cover
- f359: ref 79037: 43 -> 46 at (441, 2964.5), 1 frames after previous cover
- f360: ref 78896: 40 -> 38 at (352, 2955), 1 frames after previous cover
- f360: ref 78969: 42 -> 40 at (377.5, 2956), 1 frames after previous cover
- f360: ref 78971: 43 -> 42 at (404, 2961.5), 1 frames after previous cover
- f360: ref 79037: 46 -> 48 at (436, 2965), 1 frames after previous cover
- f360: ref 79045: 48 -> 43 at (421, 2965.5), 1 frames after previous cover
- f467: ref 79139: 87 -> 76 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 76 -> 87 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 1 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (347), 40 (1) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (349), 42 (1) |
| 78971 | 352 (84..439) | 350 | 0 | 42 (349), 43 (1) |
| 79045 | 355 (84..443) | 351 | 1 | 48 (266), 43 (85) |
| 79037 | 355 (86..445) | 351 | 1 | 43 (263), 48 (86), 45 (1), 46 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 46 (343), 45 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 50 (360), 45 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (361), 45 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (354), 45 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 78 (338), 45 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 55 (377), 54 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 45 (352), 54 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 54 (360), 59 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 59 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 63 (366), 65 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (416), 67 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 65 (396), 67 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (393), 69 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 69 (382), 72 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 72 (397), 73 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 73 (404), 72 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 76 (333), 87 (75), 73 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 87 (176), 84 (156), 76 (72) |
| 79136 | 393 (136..538) | 391 | 0 | 84 (243), 87 (148) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 328 | 651..680 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 30/421/1007; tracks with internal gaps: 21; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 25 (trailing rows total 792)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 347 | 34 | 3 | 3 | 29 | 78896 |
| 40 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78896, 78969 |
| 42 | 86..468 | 383 | 383 | 350 | 33 | 4 | 1 | 29 | 78969, 78971 |
| 43 | 86..472 | 387 | 387 | 349 | 38 | 7 | 2 | 29 | 78971, 79037, 79045 |
| 45 | 88..513 | 426 | 426 | 393 | 33 | 4 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 46 | 91..479 | 389 | 389 | 344 | 45 | 16 | 1 | 29 | 78897, 79037 |
| 48 | 93..474 | 382 | 382 | 352 | 30 | 1 | 1 | 29 | 79037, 79045 |
| 50 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 52 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 54 | 100..521 | 422 | 422 | 388 | 34 | 5 | 1 | 29 | 79103, 79105, 79108 |
| 55 | 101..510 | 410 | 410 | 377 | 33 | 3 | 2 | 29 | 79103 |
| 58 | 103..496 | 394 | 394 | 354 | 40 | 10 | 2 | 29 | 79098 |
| 59 | 106..526 | 421 | 421 | 390 | 31 | 2 | 1 | 29 | 79108, 79110 |
| 63 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 65 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 67 | 113..627 | 515 | 515 | 409 | 106 | 11 | 1 | 95 | 79115, 79116, 79122 |
| 68 | 116..560 | 445 | 445 | 416 | 29 | 0 | 0 | 29 | 79115 |
| 69 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 72 | 122..556 | 435 | 435 | 405 | 30 | 1 | 1 | 29 | 79128, 79132, 79134 |
| 73 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134, 79135 |
| 76 | 129..566 | 438 | 438 | 405 | 33 | 4 | 1 | 29 | 79135, 79139 |
| 78 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 84 | 134..567 | 434 | 434 | 399 | 35 | 4 | 2 | 29 | 79136, 79139 |
| 87 | 138..571 | 434 | 434 | 399 | 35 | 6 | 1 | 29 | 79135, 79136, 79139 |
| 328 | 651..680 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 26; matched pairs: 10090; unmatched reference entries: 52; unmatched candidate entries: 912
- identity switches: 35; fragmentation (coverage interruptions): 7; orphan candidate ids (never on a reference object): 1

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 78897: 45 -> 46 at (2142, 3030.5), 1 frames after previous cover
- f91: ref 79037: 45 -> 43 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 79045: 43 -> 48 at (2106.5, 3031.5), 3 frames after previous cover
- f96: ref 78899: 45 -> 50 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 45 -> 52 at (2122.5, 3028.5), 3 frames after previous cover
- f102: ref 79103: 54 -> 55 at (2139, 3022), 1 frames after previous cover
- f103: ref 79098: 45 -> 58 at (2113.5, 3027), 3 frames after previous cover
- f116: ref 79115: 67 -> 68 at (2130, 3021), 3 frames after previous cover
- f129: ref 79105: 54 -> 45 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79108: 59 -> 54 at (2015, 3026), 1 frames after previous cover
- f129: ref 79110: 63 -> 59 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79111: 65 -> 63 at (2042, 3029), 1 frames after previous cover
- f129: ref 79116: 67 -> 65 at (2069, 3025), 1 frames after previous cover
- f129: ref 79122: 69 -> 67 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 72 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 72 -> 69 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 45 -> 78 at (1952.5, 3031), 4 frames after previous cover
- f290: ref 79134: 73 -> 72 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 76 -> 73 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79139: 84 -> 76 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 72 -> 73 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 73 -> 76 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 76 -> 87 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 87 -> 84 at (1184, 2971.5), 2 frames after previous cover
- f359: ref 78896: 38 -> 40 at (359, 2955), 1 frames after previous cover
- f359: ref 78969: 40 -> 42 at (383, 2957), 1 frames after previous cover
- f359: ref 78971: 42 -> 43 at (409.5, 2964), 1 frames after previous cover
- f359: ref 79037: 43 -> 46 at (441, 2964.5), 1 frames after previous cover
- f360: ref 78896: 40 -> 38 at (352, 2955), 1 frames after previous cover
- f360: ref 78969: 42 -> 40 at (377.5, 2956), 1 frames after previous cover
- f360: ref 78971: 43 -> 42 at (404, 2961.5), 1 frames after previous cover
- f360: ref 79037: 46 -> 48 at (436, 2965), 1 frames after previous cover
- f360: ref 79045: 48 -> 43 at (421, 2965.5), 1 frames after previous cover
- f467: ref 79139: 87 -> 76 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 76 -> 87 at (399.5, 2892.5), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 1 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (347), 40 (1) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (349), 42 (1) |
| 78971 | 352 (84..439) | 350 | 0 | 42 (349), 43 (1) |
| 79045 | 355 (84..443) | 351 | 1 | 48 (266), 43 (85) |
| 79037 | 355 (86..445) | 351 | 1 | 43 (263), 48 (86), 45 (1), 46 (1) |
| 78897 | 345 (89..450) | 345 | 0 | 46 (343), 45 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 50 (360), 45 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 52 (361), 45 (3) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (354), 45 (4) |
| 79102 | 371 (98..477) | 366 | 1 | 78 (338), 45 (28) |
| 79103 | 380 (99..481) | 379 | 0 | 55 (377), 54 (2) |
| 79105 | 379 (101..484) | 378 | 0 | 45 (352), 54 (26) |
| 79108 | 385 (104..492) | 383 | 0 | 54 (360), 59 (23) |
| 79110 | 388 (106..497) | 385 | 0 | 59 (367), 63 (18) |
| 79111 | 386 (109..500) | 384 | 0 | 63 (366), 65 (18) |
| 79115 | 421 (111..531) | 417 | 1 | 68 (416), 67 (1) |
| 79116 | 411 (114..530) | 411 | 0 | 65 (396), 67 (15) |
| 79122 | 404 (118..532) | 402 | 0 | 67 (393), 69 (9) |
| 79132 | 391 (120..515) | 389 | 0 | 69 (382), 72 (7) |
| 79128 | 402 (124..527) | 400 | 0 | 72 (397), 73 (3) |
| 79134 | 407 (127..533) | 405 | 0 | 73 (404), 72 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 76 (333), 87 (75), 73 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 87 (176), 84 (156), 76 (72) |
| 79136 | 393 (136..538) | 391 | 0 | 84 (243), 87 (148) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 328 | 651..680 | 30 | 0 | 30 |

### Gaps and durations of candidate tracks
- tracks: 26; lifespan min/median/max: 30/421/1007; tracks with internal gaps: 21; total internal gaps: 109; longest internal gap: 3; tracks ending in coasting: 25 (trailing rows total 792)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 347 | 34 | 3 | 3 | 29 | 78896 |
| 40 | 82..463 | 382 | 382 | 350 | 32 | 2 | 2 | 29 | 78896, 78969 |
| 42 | 86..468 | 383 | 383 | 350 | 33 | 4 | 1 | 29 | 78969, 78971 |
| 43 | 86..472 | 387 | 387 | 349 | 38 | 7 | 2 | 29 | 78971, 79037, 79045 |
| 45 | 88..513 | 426 | 426 | 393 | 33 | 4 | 1 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79105 |
| 46 | 91..479 | 389 | 389 | 344 | 45 | 16 | 1 | 29 | 78897, 79037 |
| 48 | 93..474 | 382 | 382 | 352 | 30 | 1 | 1 | 29 | 79037, 79045 |
| 50 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 52 | 99..490 | 392 | 392 | 361 | 31 | 2 | 1 | 29 | 79097 |
| 54 | 100..521 | 422 | 422 | 388 | 34 | 5 | 1 | 29 | 79103, 79105, 79108 |
| 55 | 101..510 | 410 | 410 | 377 | 33 | 3 | 2 | 29 | 79103 |
| 58 | 103..496 | 394 | 394 | 354 | 40 | 10 | 2 | 29 | 79098 |
| 59 | 106..526 | 421 | 421 | 390 | 31 | 2 | 1 | 29 | 79108, 79110 |
| 63 | 110..529 | 420 | 420 | 384 | 36 | 6 | 2 | 29 | 79110, 79111 |
| 65 | 111..559 | 449 | 449 | 414 | 35 | 5 | 2 | 29 | 79111, 79116 |
| 67 | 113..627 | 515 | 515 | 409 | 106 | 11 | 1 | 95 | 79115, 79116, 79122 |
| 68 | 116..560 | 445 | 445 | 416 | 29 | 0 | 0 | 29 | 79115 |
| 69 | 120..544 | 425 | 425 | 391 | 34 | 5 | 1 | 29 | 79122, 79132 |
| 72 | 122..556 | 435 | 435 | 405 | 30 | 1 | 1 | 29 | 79128, 79132, 79134 |
| 73 | 126..562 | 437 | 437 | 408 | 29 | 0 | 0 | 29 | 79128, 79134, 79135 |
| 76 | 129..566 | 438 | 438 | 405 | 33 | 4 | 1 | 29 | 79135, 79139 |
| 78 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 84 | 134..567 | 434 | 434 | 399 | 35 | 4 | 2 | 29 | 79136, 79139 |
| 87 | 138..571 | 434 | 434 | 399 | 35 | 6 | 1 | 29 | 79135, 79136, 79139 |
| 328 | 651..680 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
