# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=265c7e84f159
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.00_noise0.0_fp0.5_seed1/tracks.csv sha256=5870c19f017517aa
  - detections_csv: outputs/detections/flock/gt_drop0.00_noise0.0_fp0.5_seed1.csv sha256=265c7e84f159ffb1
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.00_noise0.0_fp0.5_seed1
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
| observations | none | 4 | 10142 | 10106 | 0.856 | 0.990 | 0.740 | 0.01 | 0.857 | 0.987 | 0.01 | 58 | 118.0 | 0.857 | 0.858 | 0.855 | 0.995 | 0.998 | 10087 | 55 | 19 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 10106 | 0.856 | 0.986 | 0.743 | 0.02 | 0.856 | 0.987 | 0.01 | 54 | 118.0 | 0.857 | 0.859 | 0.856 | 0.995 | 0.998 | 10087 | 55 | 19 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 10106 | 0.856 | 0.984 | 0.745 | 0.03 | 0.855 | 0.988 | 0.01 | 54 | 117.0 | 0.858 | 0.859 | 0.856 | 0.995 | 0.998 | 10088 | 54 | 18 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 10106 | 0.857 | 0.981 | 0.749 | 0.07 | 0.857 | 0.988 | 0.08 | 53 | 116.0 | 0.861 | 0.862 | 0.859 | 0.995 | 0.998 | 10088 | 54 | 18 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 10106 | 0.856 | 0.990 | 0.740 | 0.01 | 0.857 | 0.987 | 0.01 | 58 | 118.0 | 0.857 | 0.858 | 0.855 | 0.995 | 0.998 | 10087 | 55 | 19 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 10106 | 0.856 | 0.986 | 0.743 | 0.02 | 0.856 | 0.987 | 0.01 | 54 | 118.0 | 0.857 | 0.859 | 0.856 | 0.995 | 0.998 | 10087 | 55 | 19 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 10106 | 0.856 | 0.984 | 0.745 | 0.03 | 0.855 | 0.988 | 0.01 | 54 | 117.0 | 0.858 | 0.859 | 0.856 | 0.995 | 0.998 | 10088 | 54 | 18 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 10106 | 0.857 | 0.981 | 0.749 | 0.07 | 0.857 | 0.988 | 0.08 | 53 | 116.0 | 0.861 | 0.862 | 0.859 | 0.995 | 0.998 | 10088 | 54 | 18 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 11042 | 0.789 | 0.907 | 0.687 | 0.01 | 0.790 | 0.895 | 0.01 | 55 | 118.0 | 0.819 | 0.786 | 0.856 | 0.995 | 0.914 | 10087 | 55 | 955 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 11042 | 0.789 | 0.903 | 0.690 | 0.02 | 0.789 | 0.895 | 0.01 | 53 | 118.0 | 0.819 | 0.786 | 0.856 | 0.995 | 0.914 | 10087 | 55 | 955 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 11042 | 0.790 | 0.902 | 0.691 | 0.03 | 0.789 | 0.895 | 0.01 | 53 | 117.0 | 0.820 | 0.787 | 0.857 | 0.995 | 0.914 | 10088 | 54 | 954 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 11042 | 0.790 | 0.899 | 0.695 | 0.07 | 0.790 | 0.895 | 0.09 | 52 | 116.0 | 0.823 | 0.789 | 0.859 | 0.995 | 0.914 | 10088 | 54 | 954 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 11042 | 0.789 | 0.907 | 0.687 | 0.01 | 0.790 | 0.895 | 0.01 | 55 | 118.0 | 0.819 | 0.786 | 0.856 | 0.995 | 0.914 | 10087 | 55 | 955 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 11042 | 0.789 | 0.903 | 0.690 | 0.02 | 0.789 | 0.895 | 0.01 | 53 | 118.0 | 0.819 | 0.786 | 0.856 | 0.995 | 0.914 | 10087 | 55 | 955 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 11042 | 0.790 | 0.902 | 0.691 | 0.03 | 0.789 | 0.895 | 0.01 | 53 | 117.0 | 0.820 | 0.787 | 0.857 | 0.995 | 0.914 | 10088 | 54 | 954 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 11042 | 0.790 | 0.899 | 0.695 | 0.07 | 0.790 | 0.895 | 0.09 | 52 | 116.0 | 0.823 | 0.789 | 0.859 | 0.995 | 0.914 | 10088 | 54 | 954 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10088; unmatched reference entries: 54; unmatched candidate entries: 18
- identity switches: 54; fragmentation (coverage interruptions): 9; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 43 -> 46 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 43 -> 49 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 43 -> 51 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 43 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 43 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 43 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 43 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 64 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 70 -> 64 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 71 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 71 -> 70 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 81 at (1952.5, 3031), 4 frames after previous cover
- f206: ref 79097: 53 -> 58 at (1453, 3004), 1 frames after previous cover
- f206: ref 79105: 58 -> 59 at (1519, 3010), 1 frames after previous cover
- f206: ref 79108: 59 -> 54 at (1551, 3007.5), 1 frames after previous cover
- f206: ref 79110: 54 -> 64 at (1567, 3011.5), 1 frames after previous cover
- f207: ref 79122: 64 -> 71 at (1603, 3014.5), 2 frames after previous cover
- f207: ref 79128: 71 -> 73 at (1632, 3009.5), 1 frames after previous cover
- f207: ref 79134: 73 -> 78 at (1655.5, 3014), 1 frames after previous cover
- f207: ref 79135: 78 -> 86 at (1666, 3004.5), 1 frames after previous cover
- f208: ref 79097: 58 -> 53 at (1440, 3006.5), 1 frames after previous cover
- f208: ref 79098: 56 -> 58 at (1464, 3007), 1 frames after previous cover
- f208: ref 79105: 59 -> 56 at (1507, 3005.5), 1 frames after previous cover
- f208: ref 79108: 54 -> 59 at (1539, 3010), 1 frames after previous cover
- f208: ref 79110: 64 -> 54 at (1556, 3008.5), 1 frames after previous cover
- f208: ref 79115: 66 -> 64 at (1573.5, 3007.5), 1 frames after previous cover
- f208: ref 79122: 71 -> 66 at (1597, 3013.5), 1 frames after previous cover
- f208: ref 79128: 73 -> 71 at (1625.5, 3010), 1 frames after previous cover
- f208: ref 79134: 78 -> 73 at (1648, 3010.5), 1 frames after previous cover
- f208: ref 79135: 86 -> 78 at (1658.5, 3005), 1 frames after previous cover
- f209: ref 79111: 65 -> 64 at (1559.5, 3007), 1 frames after previous cover
- f209: ref 79115: 64 -> 65 at (1568.5, 3009), 1 frames after previous cover
- f225: ref 79115: 65 -> 64 at (1470.5, 3004), 1 frames after previous cover
- f225: ref 79132: 70 -> 65 at (1489, 2997), 1 frames after previous cover
- f225: ref 79134: 73 -> 70 at (1537.5, 3005.5), 1 frames after previous cover
- f225: ref 79135: 78 -> 73 at (1549, 2998.5), 1 frames after previous cover
- f225: ref 79136: 86 -> 78 at (1593, 3006), 2 frames after previous cover
- f228: ref 79111: 64 -> 129 at (1444.5, 3000.5), 4 frames after previous cover
- f290: ref 79134: 70 -> 71 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 73 -> 70 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79136: 78 -> 83 at (1195, 2969), 1 frames after previous cover
- f290: ref 79139: 83 -> 73 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 71 -> 70 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 70 -> 73 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 73 -> 83 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 83 -> 78 at (1184, 2971.5), 2 frames after previous cover
- f331: ref 79135: 73 -> 83 at (939, 2963.5), 1 frames after previous cover
- f331: ref 79139: 83 -> 78 at (959, 2959), 1 frames after previous cover
- f333: ref 79136: 78 -> 73 at (965.5, 2962), 3 frames after previous cover
- f467: ref 79139: 78 -> 83 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 83 -> 78 at (399.5, 2892.5), 2 frames after previous cover
- f477: ref 79128: 71 -> 260 at (278.5, 2878), 2 frames after previous cover
- f538: ref 79136: 73 -> 83 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 44 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 46 (350), 43 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 49 (341), 43 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 51 (360), 43 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (359), 43 (3), 58 (2) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (249), 56 (107), 43 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 81 (338), 58 (26), 43 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 43 (378), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 56 (273), 58 (77), 54 (27), 59 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 59 (381), 54 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (365), 64 (20) |
| 79111 | 386 (109..500) | 382 | 1 | 129 (268), 65 (98), 64 (16) |
| 79115 | 421 (111..531) | 419 | 0 | 64 (308), 66 (95), 65 (16) |
| 79116 | 411 (114..530) | 409 | 0 | 68 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 66 (316), 64 (76), 70 (9), 71 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 65 (286), 70 (96), 71 (7) |
| 79128 | 402 (124..527) | 399 | 1 | 71 (344), 260 (51), 73 (4) |
| 79134 | 407 (127..533) | 405 | 0 | 70 (308), 73 (95), 78 (1), 71 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 78 (170), 83 (136), 73 (101), 86 (1), 70 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 83 (267), 78 (136), 73 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (203), 78 (102), 86 (84), 83 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 51/381/1007; tracks with internal gaps: 6; total internal gaps: 6; longest internal gap: 1; tracks ending in coasting: 6 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..429 | 352 | 349 | 348 | 1 | 1 | 1 | 0 | 78896 |
| 40 | 82..462 | 381 | 353 | 350 | 3 | 1 | 1 | 2 | 78969 |
| 43 | 86..481 | 396 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 44 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 45 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 46 | 91..445 | 355 | 351 | 350 | 1 | 1 | 1 | 0 | 79037 |
| 49 | 93..450 | 358 | 341 | 341 | 0 | 0 | 0 | 0 | 78897 |
| 51 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 53 | 99..461 | 363 | 360 | 359 | 1 | 1 | 1 | 0 | 79097 |
| 54 | 100..512 | 413 | 399 | 395 | 4 | 0 | 0 | 4 | 79103, 79105, 79108, 79110 |
| 56 | 101..484 | 384 | 380 | 380 | 0 | 0 | 0 | 0 | 79098, 79105 |
| 58 | 103..467 | 365 | 354 | 354 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79105 |
| 59 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 64 | 110..531 | 422 | 420 | 420 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79122 |
| 65 | 111..515 | 405 | 400 | 400 | 0 | 0 | 0 | 0 | 79111, 79115, 79132 |
| 66 | 113..556 | 444 | 413 | 411 | 2 | 0 | 0 | 2 | 79115, 79122 |
| 68 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79116 |
| 70 | 120..533 | 414 | 414 | 414 | 0 | 0 | 0 | 0 | 79122, 79132, 79134, 79135 |
| 71 | 122..476 | 355 | 354 | 353 | 1 | 0 | 0 | 1 | 79122, 79128, 79132, 79134 |
| 73 | 126..537 | 412 | 405 | 404 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 129..555 | 427 | 411 | 409 | 2 | 1 | 1 | 1 | 79134, 79135, 79136, 79139 |
| 81 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 83 | 134..538 | 405 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 86 | 138..225 | 88 | 87 | 85 | 2 | 0 | 0 | 2 | 79135, 79136 |
| 129 | 228..500 | 273 | 268 | 268 | 0 | 0 | 0 | 0 | 79111 |
| 260 | 477..527 | 51 | 51 | 51 | 0 | 0 | 0 | 0 | 79128 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10088; unmatched reference entries: 54; unmatched candidate entries: 18
- identity switches: 54; fragmentation (coverage interruptions): 9; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 43 -> 46 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 43 -> 49 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 43 -> 51 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 43 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 43 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 43 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 43 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 64 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 70 -> 64 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 71 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 71 -> 70 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 81 at (1952.5, 3031), 4 frames after previous cover
- f206: ref 79097: 53 -> 58 at (1453, 3004), 1 frames after previous cover
- f206: ref 79105: 58 -> 59 at (1519, 3010), 1 frames after previous cover
- f206: ref 79108: 59 -> 54 at (1551, 3007.5), 1 frames after previous cover
- f206: ref 79110: 54 -> 64 at (1567, 3011.5), 1 frames after previous cover
- f207: ref 79122: 64 -> 71 at (1603, 3014.5), 2 frames after previous cover
- f207: ref 79128: 71 -> 73 at (1632, 3009.5), 1 frames after previous cover
- f207: ref 79134: 73 -> 78 at (1655.5, 3014), 1 frames after previous cover
- f207: ref 79135: 78 -> 86 at (1666, 3004.5), 1 frames after previous cover
- f208: ref 79097: 58 -> 53 at (1440, 3006.5), 1 frames after previous cover
- f208: ref 79098: 56 -> 58 at (1464, 3007), 1 frames after previous cover
- f208: ref 79105: 59 -> 56 at (1507, 3005.5), 1 frames after previous cover
- f208: ref 79108: 54 -> 59 at (1539, 3010), 1 frames after previous cover
- f208: ref 79110: 64 -> 54 at (1556, 3008.5), 1 frames after previous cover
- f208: ref 79115: 66 -> 64 at (1573.5, 3007.5), 1 frames after previous cover
- f208: ref 79122: 71 -> 66 at (1597, 3013.5), 1 frames after previous cover
- f208: ref 79128: 73 -> 71 at (1625.5, 3010), 1 frames after previous cover
- f208: ref 79134: 78 -> 73 at (1648, 3010.5), 1 frames after previous cover
- f208: ref 79135: 86 -> 78 at (1658.5, 3005), 1 frames after previous cover
- f209: ref 79111: 65 -> 64 at (1559.5, 3007), 1 frames after previous cover
- f209: ref 79115: 64 -> 65 at (1568.5, 3009), 1 frames after previous cover
- f225: ref 79115: 65 -> 64 at (1470.5, 3004), 1 frames after previous cover
- f225: ref 79132: 70 -> 65 at (1489, 2997), 1 frames after previous cover
- f225: ref 79134: 73 -> 70 at (1537.5, 3005.5), 1 frames after previous cover
- f225: ref 79135: 78 -> 73 at (1549, 2998.5), 1 frames after previous cover
- f225: ref 79136: 86 -> 78 at (1593, 3006), 2 frames after previous cover
- f228: ref 79111: 64 -> 129 at (1444.5, 3000.5), 4 frames after previous cover
- f290: ref 79134: 70 -> 71 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 73 -> 70 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79136: 78 -> 83 at (1195, 2969), 1 frames after previous cover
- f290: ref 79139: 83 -> 73 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 71 -> 70 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 70 -> 73 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 73 -> 83 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 83 -> 78 at (1184, 2971.5), 2 frames after previous cover
- f331: ref 79135: 73 -> 83 at (939, 2963.5), 1 frames after previous cover
- f331: ref 79139: 83 -> 78 at (959, 2959), 1 frames after previous cover
- f333: ref 79136: 78 -> 73 at (965.5, 2962), 3 frames after previous cover
- f467: ref 79139: 78 -> 83 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 83 -> 78 at (399.5, 2892.5), 2 frames after previous cover
- f477: ref 79128: 71 -> 260 at (278.5, 2878), 2 frames after previous cover
- f538: ref 79136: 73 -> 83 at (1.5, 2853.5), 1 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 44 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 46 (350), 43 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 49 (341), 43 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 51 (360), 43 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (359), 43 (3), 58 (2) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (249), 56 (107), 43 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 81 (338), 58 (26), 43 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 43 (378), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 56 (273), 58 (77), 54 (27), 59 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 59 (381), 54 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (365), 64 (20) |
| 79111 | 386 (109..500) | 382 | 1 | 129 (268), 65 (98), 64 (16) |
| 79115 | 421 (111..531) | 419 | 0 | 64 (308), 66 (95), 65 (16) |
| 79116 | 411 (114..530) | 409 | 0 | 68 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 66 (316), 64 (76), 70 (9), 71 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 65 (286), 70 (96), 71 (7) |
| 79128 | 402 (124..527) | 399 | 1 | 71 (344), 260 (51), 73 (4) |
| 79134 | 407 (127..533) | 405 | 0 | 70 (308), 73 (95), 78 (1), 71 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 78 (170), 83 (136), 73 (101), 86 (1), 70 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 83 (267), 78 (136), 73 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (203), 78 (102), 86 (84), 83 (2) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 51/381/1007; tracks with internal gaps: 6; total internal gaps: 6; longest internal gap: 1; tracks ending in coasting: 6 (trailing rows total 12)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..429 | 352 | 349 | 348 | 1 | 1 | 1 | 0 | 78896 |
| 40 | 82..462 | 381 | 353 | 350 | 3 | 1 | 1 | 2 | 78969 |
| 43 | 86..481 | 396 | 393 | 393 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 44 | 86..443 | 358 | 353 | 353 | 0 | 0 | 0 | 0 | 79045 |
| 45 | 88..439 | 352 | 348 | 348 | 0 | 0 | 0 | 0 | 78971 |
| 46 | 91..445 | 355 | 351 | 350 | 1 | 1 | 1 | 0 | 79037 |
| 49 | 93..450 | 358 | 341 | 341 | 0 | 0 | 0 | 0 | 78897 |
| 51 | 96..455 | 360 | 360 | 360 | 0 | 0 | 0 | 0 | 78899 |
| 53 | 99..461 | 363 | 360 | 359 | 1 | 1 | 1 | 0 | 79097 |
| 54 | 100..512 | 413 | 399 | 395 | 4 | 0 | 0 | 4 | 79103, 79105, 79108, 79110 |
| 56 | 101..484 | 384 | 380 | 380 | 0 | 0 | 0 | 0 | 79098, 79105 |
| 58 | 103..467 | 365 | 354 | 354 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79105 |
| 59 | 106..492 | 387 | 383 | 383 | 0 | 0 | 0 | 0 | 79105, 79108 |
| 64 | 110..531 | 422 | 420 | 420 | 0 | 0 | 0 | 0 | 79110, 79111, 79115, 79122 |
| 65 | 111..515 | 405 | 400 | 400 | 0 | 0 | 0 | 0 | 79111, 79115, 79132 |
| 66 | 113..556 | 444 | 413 | 411 | 2 | 0 | 0 | 2 | 79115, 79122 |
| 68 | 116..530 | 415 | 409 | 409 | 0 | 0 | 0 | 0 | 79116 |
| 70 | 120..533 | 414 | 414 | 414 | 0 | 0 | 0 | 0 | 79122, 79132, 79134, 79135 |
| 71 | 122..476 | 355 | 354 | 353 | 1 | 0 | 0 | 1 | 79122, 79128, 79132, 79134 |
| 73 | 126..537 | 412 | 405 | 404 | 1 | 1 | 1 | 0 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 129..555 | 427 | 411 | 409 | 2 | 1 | 1 | 1 | 79134, 79135, 79136, 79139 |
| 81 | 132..477 | 346 | 338 | 338 | 0 | 0 | 0 | 0 | 79102 |
| 83 | 134..538 | 405 | 405 | 405 | 0 | 0 | 0 | 0 | 79135, 79136, 79139 |
| 86 | 138..225 | 88 | 87 | 85 | 2 | 0 | 0 | 2 | 79135, 79136 |
| 129 | 228..500 | 273 | 268 | 268 | 0 | 0 | 0 | 0 | 79111 |
| 260 | 477..527 | 51 | 51 | 51 | 0 | 0 | 0 | 0 | 79128 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10088; unmatched reference entries: 54; unmatched candidate entries: 954
- identity switches: 53; fragmentation (coverage interruptions): 9; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 43 -> 46 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 43 -> 49 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 43 -> 51 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 43 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 43 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 43 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 43 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 64 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 70 -> 64 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 71 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 71 -> 70 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 81 at (1952.5, 3031), 4 frames after previous cover
- f206: ref 79097: 53 -> 58 at (1453, 3004), 1 frames after previous cover
- f206: ref 79105: 58 -> 59 at (1519, 3010), 1 frames after previous cover
- f206: ref 79108: 59 -> 54 at (1551, 3007.5), 1 frames after previous cover
- f206: ref 79110: 54 -> 64 at (1567, 3011.5), 1 frames after previous cover
- f207: ref 79122: 64 -> 71 at (1603, 3014.5), 2 frames after previous cover
- f207: ref 79128: 71 -> 73 at (1632, 3009.5), 1 frames after previous cover
- f207: ref 79134: 73 -> 78 at (1655.5, 3014), 1 frames after previous cover
- f207: ref 79135: 78 -> 86 at (1666, 3004.5), 1 frames after previous cover
- f208: ref 79097: 58 -> 53 at (1440, 3006.5), 1 frames after previous cover
- f208: ref 79098: 56 -> 58 at (1464, 3007), 1 frames after previous cover
- f208: ref 79105: 59 -> 56 at (1507, 3005.5), 1 frames after previous cover
- f208: ref 79108: 54 -> 59 at (1539, 3010), 1 frames after previous cover
- f208: ref 79110: 64 -> 54 at (1556, 3008.5), 1 frames after previous cover
- f208: ref 79115: 66 -> 64 at (1573.5, 3007.5), 1 frames after previous cover
- f208: ref 79122: 71 -> 66 at (1597, 3013.5), 1 frames after previous cover
- f208: ref 79128: 73 -> 71 at (1625.5, 3010), 1 frames after previous cover
- f208: ref 79134: 78 -> 73 at (1648, 3010.5), 1 frames after previous cover
- f208: ref 79135: 86 -> 78 at (1658.5, 3005), 1 frames after previous cover
- f209: ref 79111: 65 -> 64 at (1559.5, 3007), 1 frames after previous cover
- f209: ref 79115: 64 -> 65 at (1568.5, 3009), 1 frames after previous cover
- f225: ref 79115: 65 -> 64 at (1470.5, 3004), 1 frames after previous cover
- f225: ref 79132: 70 -> 65 at (1489, 2997), 1 frames after previous cover
- f225: ref 79134: 73 -> 70 at (1537.5, 3005.5), 1 frames after previous cover
- f225: ref 79135: 78 -> 73 at (1549, 2998.5), 1 frames after previous cover
- f225: ref 79136: 86 -> 78 at (1593, 3006), 2 frames after previous cover
- f228: ref 79111: 64 -> 129 at (1444.5, 3000.5), 4 frames after previous cover
- f290: ref 79134: 70 -> 71 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 73 -> 70 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79136: 78 -> 83 at (1195, 2969), 1 frames after previous cover
- f290: ref 79139: 83 -> 73 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 71 -> 70 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 70 -> 73 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 73 -> 83 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 83 -> 78 at (1184, 2971.5), 2 frames after previous cover
- f331: ref 79139: 83 -> 78 at (959, 2959), 1 frames after previous cover
- f332: ref 79135: 73 -> 83 at (934.5, 2963.5), 1 frames after previous cover
- f333: ref 79136: 78 -> 73 at (965.5, 2962), 3 frames after previous cover
- f467: ref 79139: 78 -> 83 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 83 -> 78 at (399.5, 2892.5), 2 frames after previous cover
- f477: ref 79128: 71 -> 260 at (278.5, 2878), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 44 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 46 (350), 43 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 49 (341), 43 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 51 (360), 43 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (359), 43 (3), 58 (2) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (249), 56 (107), 43 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 81 (338), 58 (26), 43 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 43 (378), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 56 (273), 58 (77), 54 (27), 59 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 59 (381), 54 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (365), 64 (20) |
| 79111 | 386 (109..500) | 382 | 1 | 129 (268), 65 (98), 64 (16) |
| 79115 | 421 (111..531) | 419 | 0 | 64 (308), 66 (95), 65 (16) |
| 79116 | 411 (114..530) | 409 | 0 | 68 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 66 (316), 64 (76), 70 (9), 71 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 65 (286), 70 (96), 71 (7) |
| 79128 | 402 (124..527) | 399 | 1 | 71 (344), 260 (51), 73 (4) |
| 79134 | 407 (127..533) | 405 | 0 | 70 (308), 73 (95), 78 (1), 71 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 78 (170), 83 (135), 73 (102), 86 (1), 70 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 83 (267), 78 (136), 73 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (204), 78 (102), 86 (84), 83 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 80/410/1007; tracks with internal gaps: 23; total internal gaps: 106; longest internal gap: 3; tracks ending in coasting: 26 (trailing rows total 837)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 40 | 82..491 | 410 | 410 | 350 | 60 | 2 | 2 | 57 | 78969 |
| 43 | 86..510 | 425 | 425 | 393 | 32 | 2 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 44 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 45 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 46 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 49 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 51 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 53 | 99..490 | 392 | 392 | 359 | 33 | 3 | 2 | 29 | 79097 |
| 54 | 100..541 | 442 | 442 | 395 | 47 | 3 | 1 | 44 | 79103, 79105, 79108, 79110 |
| 56 | 101..513 | 413 | 413 | 380 | 33 | 4 | 1 | 29 | 79098, 79105 |
| 58 | 103..496 | 394 | 394 | 354 | 40 | 10 | 2 | 29 | 79097, 79098, 79102, 79105 |
| 59 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79105, 79108 |
| 64 | 110..560 | 451 | 451 | 420 | 31 | 2 | 1 | 29 | 79110, 79111, 79115, 79122 |
| 65 | 111..544 | 434 | 434 | 400 | 34 | 5 | 1 | 29 | 79111, 79115, 79132 |
| 66 | 113..585 | 473 | 473 | 411 | 62 | 9 | 1 | 53 | 79115, 79122 |
| 68 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79116 |
| 70 | 120..562 | 443 | 443 | 414 | 29 | 0 | 0 | 29 | 79122, 79132, 79134, 79135 |
| 71 | 122..505 | 384 | 384 | 353 | 31 | 1 | 1 | 30 | 79122, 79128, 79132, 79134 |
| 73 | 126..566 | 441 | 441 | 406 | 35 | 7 | 1 | 28 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 129..584 | 456 | 456 | 409 | 47 | 4 | 2 | 42 | 79134, 79135, 79136, 79139 |
| 81 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 83 | 134..567 | 434 | 434 | 403 | 31 | 1 | 1 | 30 | 79135, 79136, 79139 |
| 86 | 138..254 | 117 | 117 | 85 | 32 | 1 | 1 | 31 | 79135, 79136 |
| 129 | 228..529 | 302 | 302 | 268 | 34 | 4 | 2 | 29 | 79111 |
| 260 | 477..556 | 80 | 80 | 51 | 29 | 0 | 0 | 29 | 79128 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 27; matched pairs: 10088; unmatched reference entries: 54; unmatched candidate entries: 954
- identity switches: 53; fragmentation (coverage interruptions): 9; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f91: ref 79037: 43 -> 46 at (2129, 3033.5), 3 frames after previous cover
- f93: ref 78897: 43 -> 49 at (2132, 3032), 3 frames after previous cover
- f96: ref 78899: 43 -> 51 at (2128, 3029), 3 frames after previous cover
- f99: ref 79097: 43 -> 53 at (2122.5, 3028.5), 3 frames after previous cover
- f101: ref 79098: 43 -> 56 at (2124, 3028), 3 frames after previous cover
- f101: ref 79103: 54 -> 43 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 79102: 43 -> 58 at (2124.5, 3027.5), 3 frames after previous cover
- f129: ref 79105: 54 -> 58 at (1993.5, 3026), 1 frames after previous cover
- f129: ref 79110: 64 -> 54 at (2027.5, 3027.5), 1 frames after previous cover
- f129: ref 79122: 70 -> 64 at (2088, 3027.5), 1 frames after previous cover
- f129: ref 79128: 73 -> 71 at (2125, 3023), 1 frames after previous cover
- f129: ref 79132: 71 -> 70 at (2107.5, 3023), 1 frames after previous cover
- f132: ref 79102: 58 -> 81 at (1952.5, 3031), 4 frames after previous cover
- f206: ref 79097: 53 -> 58 at (1453, 3004), 1 frames after previous cover
- f206: ref 79105: 58 -> 59 at (1519, 3010), 1 frames after previous cover
- f206: ref 79108: 59 -> 54 at (1551, 3007.5), 1 frames after previous cover
- f206: ref 79110: 54 -> 64 at (1567, 3011.5), 1 frames after previous cover
- f207: ref 79122: 64 -> 71 at (1603, 3014.5), 2 frames after previous cover
- f207: ref 79128: 71 -> 73 at (1632, 3009.5), 1 frames after previous cover
- f207: ref 79134: 73 -> 78 at (1655.5, 3014), 1 frames after previous cover
- f207: ref 79135: 78 -> 86 at (1666, 3004.5), 1 frames after previous cover
- f208: ref 79097: 58 -> 53 at (1440, 3006.5), 1 frames after previous cover
- f208: ref 79098: 56 -> 58 at (1464, 3007), 1 frames after previous cover
- f208: ref 79105: 59 -> 56 at (1507, 3005.5), 1 frames after previous cover
- f208: ref 79108: 54 -> 59 at (1539, 3010), 1 frames after previous cover
- f208: ref 79110: 64 -> 54 at (1556, 3008.5), 1 frames after previous cover
- f208: ref 79115: 66 -> 64 at (1573.5, 3007.5), 1 frames after previous cover
- f208: ref 79122: 71 -> 66 at (1597, 3013.5), 1 frames after previous cover
- f208: ref 79128: 73 -> 71 at (1625.5, 3010), 1 frames after previous cover
- f208: ref 79134: 78 -> 73 at (1648, 3010.5), 1 frames after previous cover
- f208: ref 79135: 86 -> 78 at (1658.5, 3005), 1 frames after previous cover
- f209: ref 79111: 65 -> 64 at (1559.5, 3007), 1 frames after previous cover
- f209: ref 79115: 64 -> 65 at (1568.5, 3009), 1 frames after previous cover
- f225: ref 79115: 65 -> 64 at (1470.5, 3004), 1 frames after previous cover
- f225: ref 79132: 70 -> 65 at (1489, 2997), 1 frames after previous cover
- f225: ref 79134: 73 -> 70 at (1537.5, 3005.5), 1 frames after previous cover
- f225: ref 79135: 78 -> 73 at (1549, 2998.5), 1 frames after previous cover
- f225: ref 79136: 86 -> 78 at (1593, 3006), 2 frames after previous cover
- f228: ref 79111: 64 -> 129 at (1444.5, 3000.5), 4 frames after previous cover
- f290: ref 79134: 70 -> 71 at (1142.5, 2970.5), 1 frames after previous cover
- f290: ref 79135: 73 -> 70 at (1161, 2970.5), 1 frames after previous cover
- f290: ref 79136: 78 -> 83 at (1195, 2969), 1 frames after previous cover
- f290: ref 79139: 83 -> 73 at (1177.5, 2968), 1 frames after previous cover
- f291: ref 79134: 71 -> 70 at (1136.5, 2970), 1 frames after previous cover
- f291: ref 79135: 70 -> 73 at (1154, 2970), 1 frames after previous cover
- f291: ref 79139: 73 -> 83 at (1171, 2968), 1 frames after previous cover
- f292: ref 79136: 83 -> 78 at (1184, 2971.5), 2 frames after previous cover
- f331: ref 79139: 83 -> 78 at (959, 2959), 1 frames after previous cover
- f332: ref 79135: 73 -> 83 at (934.5, 2963.5), 1 frames after previous cover
- f333: ref 79136: 78 -> 73 at (965.5, 2962), 3 frames after previous cover
- f467: ref 79139: 78 -> 83 at (402.5, 2886), 1 frames after previous cover
- f468: ref 79135: 83 -> 78 at (399.5, 2892.5), 2 frames after previous cover
- f477: ref 79128: 71 -> 260 at (278.5, 2878), 2 frames after previous cover

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1007 | 0 | 0 (1007) |
| 78896 | 350 (76..429) | 348 | 0 | 38 (348) |
| 78969 | 352 (80..434) | 350 | 0 | 40 (350) |
| 78971 | 352 (84..439) | 348 | 0 | 45 (348) |
| 79045 | 355 (84..443) | 353 | 0 | 44 (353) |
| 79037 | 355 (86..445) | 353 | 1 | 46 (350), 43 (3) |
| 78897 | 345 (89..450) | 343 | 1 | 49 (341), 43 (2) |
| 78899 | 365 (91..455) | 363 | 1 | 51 (360), 43 (3) |
| 79097 | 366 (94..461) | 364 | 1 | 53 (359), 43 (3), 58 (2) |
| 79098 | 360 (97..467) | 358 | 1 | 58 (249), 56 (107), 43 (2) |
| 79102 | 371 (98..477) | 366 | 2 | 81 (338), 58 (26), 43 (2) |
| 79103 | 380 (99..481) | 379 | 0 | 43 (378), 54 (1) |
| 79105 | 379 (101..484) | 379 | 0 | 56 (273), 58 (77), 54 (27), 59 (2) |
| 79108 | 385 (104..492) | 383 | 0 | 59 (381), 54 (2) |
| 79110 | 388 (106..497) | 385 | 0 | 54 (365), 64 (20) |
| 79111 | 386 (109..500) | 382 | 1 | 129 (268), 65 (98), 64 (16) |
| 79115 | 421 (111..531) | 419 | 0 | 64 (308), 66 (95), 65 (16) |
| 79116 | 411 (114..530) | 409 | 0 | 68 (409) |
| 79122 | 404 (118..532) | 402 | 0 | 66 (316), 64 (76), 70 (9), 71 (1) |
| 79132 | 391 (120..515) | 389 | 0 | 65 (286), 70 (96), 71 (7) |
| 79128 | 402 (124..527) | 399 | 1 | 71 (344), 260 (51), 73 (4) |
| 79134 | 407 (127..533) | 405 | 0 | 70 (308), 73 (95), 78 (1), 71 (1) |
| 79135 | 409 (129..542) | 409 | 0 | 78 (170), 83 (135), 73 (102), 86 (1), 70 (1) |
| 79139 | 406 (132..537) | 404 | 0 | 83 (267), 78 (136), 73 (1) |
| 79136 | 393 (136..538) | 391 | 0 | 73 (204), 78 (102), 86 (84), 83 (1) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 27; lifespan min/median/max: 80/410/1007; tracks with internal gaps: 23; total internal gaps: 106; longest internal gap: 3; tracks ending in coasting: 26 (trailing rows total 837)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1007 | 0 | 0 | 0 | 0 | 78911 |
| 38 | 78..458 | 381 | 381 | 348 | 33 | 2 | 3 | 29 | 78896 |
| 40 | 82..491 | 410 | 410 | 350 | 60 | 2 | 2 | 57 | 78969 |
| 43 | 86..510 | 425 | 425 | 393 | 32 | 2 | 2 | 29 | 78897, 78899, 79037, 79097, 79098, 79102, 79103 |
| 44 | 86..472 | 387 | 387 | 353 | 34 | 5 | 1 | 29 | 79045 |
| 45 | 88..468 | 381 | 381 | 348 | 33 | 4 | 1 | 29 | 78971 |
| 46 | 91..474 | 384 | 384 | 350 | 34 | 3 | 2 | 29 | 79037 |
| 49 | 93..479 | 387 | 387 | 341 | 46 | 17 | 1 | 29 | 78897 |
| 51 | 96..484 | 389 | 389 | 360 | 29 | 0 | 0 | 29 | 78899 |
| 53 | 99..490 | 392 | 392 | 359 | 33 | 3 | 2 | 29 | 79097 |
| 54 | 100..541 | 442 | 442 | 395 | 47 | 3 | 1 | 44 | 79103, 79105, 79108, 79110 |
| 56 | 101..513 | 413 | 413 | 380 | 33 | 4 | 1 | 29 | 79098, 79105 |
| 58 | 103..496 | 394 | 394 | 354 | 40 | 10 | 2 | 29 | 79097, 79098, 79102, 79105 |
| 59 | 106..521 | 416 | 416 | 383 | 33 | 4 | 1 | 29 | 79105, 79108 |
| 64 | 110..560 | 451 | 451 | 420 | 31 | 2 | 1 | 29 | 79110, 79111, 79115, 79122 |
| 65 | 111..544 | 434 | 434 | 400 | 34 | 5 | 1 | 29 | 79111, 79115, 79132 |
| 66 | 113..585 | 473 | 473 | 411 | 62 | 9 | 1 | 53 | 79115, 79122 |
| 68 | 116..559 | 444 | 444 | 409 | 35 | 5 | 2 | 29 | 79116 |
| 70 | 120..562 | 443 | 443 | 414 | 29 | 0 | 0 | 29 | 79122, 79132, 79134, 79135 |
| 71 | 122..505 | 384 | 384 | 353 | 31 | 1 | 1 | 30 | 79122, 79128, 79132, 79134 |
| 73 | 126..566 | 441 | 441 | 406 | 35 | 7 | 1 | 28 | 79128, 79134, 79135, 79136, 79139 |
| 78 | 129..584 | 456 | 456 | 409 | 47 | 4 | 2 | 42 | 79134, 79135, 79136, 79139 |
| 81 | 132..506 | 375 | 375 | 338 | 37 | 8 | 1 | 29 | 79102 |
| 83 | 134..567 | 434 | 434 | 403 | 31 | 1 | 1 | 30 | 79135, 79136, 79139 |
| 86 | 138..254 | 117 | 117 | 85 | 32 | 1 | 1 | 31 | 79135, 79136 |
| 129 | 228..529 | 302 | 302 | 268 | 34 | 4 | 2 | 29 | 79111 |
| 260 | 477..556 | 80 | 80 | 51 | 29 | 0 | 0 | 29 | 79128 |
