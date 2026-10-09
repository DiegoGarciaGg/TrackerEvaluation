# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=gt-degraded config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=707ed12dd796
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/gtdeg_drop0.10_noise0.0_fp0.0_seed2/tracks.csv sha256=294b84e7d1ad844b
  - detections_csv: outputs/detections/flock/gt_drop0.10_noise0.0_fp0.0_seed2.csv sha256=707ed12dd796203f
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: gtdeg_drop0.10_noise0.0_fp0.0_seed2
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
| observations | none | 4 | 10142 | 9046 | 0.831 | 0.890 | 0.777 | 0.01 | 0.833 | 0.879 | 0.01 | 132 | 971.0 | 0.896 | 0.951 | 0.848 | 0.892 | 1.000 | 9046 | 1096 | 0 | 25 | 0 | 0 |
| observations | none | 6 | 10142 | 9046 | 0.830 | 0.878 | 0.785 | 0.02 | 0.830 | 0.879 | 0.01 | 130 | 971.0 | 0.897 | 0.951 | 0.848 | 0.892 | 1.000 | 9046 | 1096 | 0 | 25 | 0 | 0 |
| observations | none | 8 | 10142 | 9046 | 0.830 | 0.865 | 0.797 | 0.06 | 0.826 | 0.879 | 0.01 | 130 | 970.0 | 0.897 | 0.951 | 0.849 | 0.892 | 1.000 | 9046 | 1096 | 0 | 25 | 0 | 0 |
| observations | none | 12 | 10142 | 9046 | 0.835 | 0.861 | 0.810 | 0.16 | 0.833 | 0.880 | 0.07 | 118 | 967.0 | 0.903 | 0.958 | 0.854 | 0.892 | 1.000 | 9043 | 1099 | 3 | 25 | 0 | 0 |
| observations | ignore | 4 | 10142 | 9046 | 0.831 | 0.890 | 0.777 | 0.01 | 0.833 | 0.879 | 0.01 | 132 | 971.0 | 0.896 | 0.951 | 0.848 | 0.892 | 1.000 | 9046 | 1096 | 0 | 25 | 0 | 0 |
| observations | ignore | 6 | 10142 | 9046 | 0.830 | 0.878 | 0.785 | 0.02 | 0.830 | 0.879 | 0.01 | 130 | 971.0 | 0.897 | 0.951 | 0.848 | 0.892 | 1.000 | 9046 | 1096 | 0 | 25 | 0 | 0 |
| observations | ignore | 8 | 10142 | 9046 | 0.830 | 0.865 | 0.797 | 0.06 | 0.826 | 0.879 | 0.01 | 130 | 970.0 | 0.897 | 0.951 | 0.849 | 0.892 | 1.000 | 9046 | 1096 | 0 | 25 | 0 | 0 |
| observations | ignore | 12 | 10142 | 9046 | 0.835 | 0.861 | 0.810 | 0.16 | 0.833 | 0.880 | 0.07 | 118 | 967.0 | 0.903 | 0.958 | 0.854 | 0.892 | 1.000 | 9043 | 1099 | 3 | 25 | 0 | 0 |
| updates | none | 4 | 10142 | 10861 | 0.748 | 0.795 | 0.703 | 0.13 | 0.730 | 0.726 | 0.05 | 141 | 897.0 | 0.832 | 0.804 | 0.861 | 0.905 | 0.845 | 9182 | 960 | 1679 | 25 | 0 | 0 |
| updates | none | 6 | 10142 | 10861 | 0.781 | 0.821 | 0.742 | 0.28 | 0.778 | 0.795 | 0.24 | 141 | 590.0 | 0.865 | 0.836 | 0.895 | 0.940 | 0.878 | 9534 | 608 | 1327 | 25 | 0 | 0 |
| updates | none | 8 | 10142 | 10861 | 0.800 | 0.830 | 0.772 | 0.41 | 0.832 | 0.870 | 0.49 | 132 | 255.0 | 0.900 | 0.870 | 0.932 | 0.977 | 0.912 | 9908 | 234 | 953 | 25 | 0 | 0 |
| updates | none | 12 | 10142 | 10861 | 0.826 | 0.848 | 0.804 | 0.59 | 0.853 | 0.888 | 0.62 | 112 | 177.0 | 0.914 | 0.884 | 0.947 | 0.985 | 0.920 | 9990 | 152 | 871 | 25 | 0 | 0 |
| updates | ignore | 4 | 10142 | 10861 | 0.748 | 0.795 | 0.703 | 0.13 | 0.730 | 0.726 | 0.05 | 141 | 897.0 | 0.832 | 0.804 | 0.861 | 0.905 | 0.845 | 9182 | 960 | 1679 | 25 | 0 | 0 |
| updates | ignore | 6 | 10142 | 10861 | 0.781 | 0.821 | 0.742 | 0.28 | 0.778 | 0.795 | 0.24 | 141 | 590.0 | 0.865 | 0.836 | 0.895 | 0.940 | 0.878 | 9534 | 608 | 1327 | 25 | 0 | 0 |
| updates | ignore | 8 | 10142 | 10861 | 0.800 | 0.830 | 0.772 | 0.41 | 0.832 | 0.870 | 0.49 | 132 | 255.0 | 0.900 | 0.870 | 0.932 | 0.977 | 0.912 | 9908 | 234 | 953 | 25 | 0 | 0 |
| updates | ignore | 12 | 10142 | 10861 | 0.826 | 0.848 | 0.804 | 0.59 | 0.853 | 0.888 | 0.62 | 112 | 177.0 | 0.914 | 0.884 | 0.947 | 0.985 | 0.920 | 9990 | 152 | 871 | 25 | 0 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9046; unmatched reference entries: 1096; unmatched candidate entries: 0
- identity switches: 130; fragmentation (coverage interruptions): 924; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 2 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 3 -> 2 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 3 -> 2 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 2 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 7 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 3 -> 2 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 5 -> 3 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 5 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 5 -> 3 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 2 -> 12 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 3 -> 11 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 3 at (2136, 3025.5), 2 frames after previous cover
- f101: ref 79103: 10 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 14 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 11 -> 13 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 10 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 2 -> 12 at (2064, 3032), 2 frames after previous cover
- f104: ref 78899: 14 -> 2 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 12 -> 1 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 13 -> 14 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 11 -> 13 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 3 -> 11 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 3 at (2126, 3022.5), 3 frames after previous cover
- f108: ref 79045: 1 -> 16 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 14 -> 2 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 13 -> 14 at (2084.5, 3028.5), 2 frames after previous cover
- f108: ref 79102: 11 -> 13 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79103: 3 -> 11 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 5 -> 3 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 10 -> 5 at (2125, 3025), 2 frames after previous cover
- f111: ref 78899: 2 -> 18 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 13 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 13 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 3 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 3 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 10 -> 5 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 2 -> 11 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 11 -> 3 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 3 -> 5 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 5 -> 10 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 18 -> 12 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 2 -> 18 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 13 -> 14 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 3 -> 13 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 5 -> 3 at (2092.5, 3025.5), 2 frames after previous cover
- f115: ref 79110: 10 -> 5 at (2105.5, 3026.5), 1 frames after previous cover
- f117: ref 79116: 17 -> 19 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 78897: 12 -> 16 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 14 -> 2 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 13 -> 14 at (2057, 3025), 2 frames after previous cover
- f118: ref 79108: 3 -> 13 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 5 -> 3 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 10 -> 5 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 10 at (2118, 3022), 5 frames after previous cover
- f119: ref 79103: 2 -> 14 at (2040, 3024.5), 1 frames after previous cover
- ... 70 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 901 | 99 | 0 (901) |
| 78896 | 350 (76..429) | 313 | 32 | 4 (307), 1 (6) |
| 78969 | 352 (80..434) | 308 | 30 | 7 (304), 1 (4) |
| 78971 | 352 (84..439) | 313 | 32 | 16 (273), 8 (32), 2 (4), 1 (3), 7 (1) |
| 79045 | 355 (84..443) | 313 | 34 | 8 (275), 16 (20), 1 (12), 2 (3), 12 (2), 3 (1) |
| 79037 | 355 (86..445) | 317 | 31 | 12 (278), 1 (23), 2 (6), 8 (6), 3 (4) |
| 78897 | 345 (89..450) | 308 | 31 | 20 (285), 12 (11), 3 (6), 2 (5), 16 (1) |
| 78899 | 365 (91..455) | 318 | 37 | 11 (289), 12 (15), 2 (5), 18 (5), 5 (3), 14 (1) |
| 79097 | 366 (94..461) | 333 | 28 | 18 (300), 11 (20), 14 (4), 5 (3), 2 (3), 3 (2), 13 (1) |
| 79098 | 360 (97..467) | 329 | 28 | 23 (293), 18 (16), 2 (4), 11 (3), 13 (3), 14 (3), 1 (3), 5 (2), 3 (2) |
| 79102 | 371 (98..477) | 328 | 37 | 1 (304), 3 (4), 11 (4), 14 (4), 2 (4), 13 (3), 23 (3), 5 (1), 18 (1) |
| 79103 | 380 (99..481) | 339 | 35 | 3 (312), 2 (8), 23 (7), 13 (4), 14 (4), 11 (2), 10 (1), 5 (1) |
| 79105 | 379 (101..484) | 329 | 43 | 2 (303), 3 (8), 14 (8), 5 (6), 13 (2), 10 (1), 11 (1) |
| 79108 | 385 (104..492) | 346 | 35 | 22 (318), 3 (11), 14 (5), 10 (4), 5 (4), 13 (2), 2 (2) |
| 79110 | 388 (106..497) | 356 | 28 | 14 (334), 10 (6), 13 (6), 3 (5), 5 (4), 22 (1) |
| 79111 | 386 (109..500) | 341 | 30 | 27 (322), 5 (9), 13 (5), 10 (4), 22 (1) |
| 79115 | 421 (111..531) | 371 | 42 | 13 (358), 5 (4), 17 (3), 10 (3), 22 (3) |
| 79116 | 411 (114..530) | 374 | 29 | 5 (356), 10 (7), 22 (4), 17 (3), 19 (3), 24 (1) |
| 79122 | 404 (118..532) | 364 | 33 | 10 (357), 19 (4), 17 (2), 24 (1) |
| 79132 | 391 (120..515) | 342 | 44 | 24 (336), 17 (3), 19 (3) |
| 79128 | 402 (124..527) | 360 | 37 | 19 (357), 17 (3) |
| 79134 | 407 (127..533) | 365 | 36 | 17 (365) |
| 79135 | 409 (129..542) | 367 | 36 | 25 (367) |
| 79139 | 406 (132..537) | 358 | 43 | 26 (305), 28 (51), 25 (2) |
| 79136 | 393 (136..538) | 353 | 34 | 28 (299), 26 (54) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 329/393/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 901 | 901 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..477 | 400 | 355 | 355 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045, 79098, 79102 |
| 2 | 84..484 | 401 | 347 | 347 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 3 | 86..481 | 396 | 355 | 355 | 0 | 0 | 0 | 0 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 87..429 | 343 | 307 | 307 | 0 | 0 | 0 | 0 | 78896 |
| 5 | 91..530 | 440 | 393 | 393 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 93..434 | 342 | 305 | 305 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 8 | 94..443 | 350 | 313 | 313 | 0 | 0 | 0 | 0 | 78971, 79037, 79045 |
| 10 | 100..532 | 433 | 383 | 383 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 100..455 | 356 | 319 | 319 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..445 | 346 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 13 | 103..531 | 429 | 384 | 384 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 14 | 103..495 | 393 | 363 | 363 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 16 | 108..439 | 332 | 294 | 294 | 0 | 0 | 0 | 0 | 78897, 78971, 79045 |
| 17 | 111..533 | 423 | 379 | 379 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 18 | 111..461 | 351 | 322 | 322 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102 |
| 19 | 117..527 | 411 | 367 | 367 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132 |
| 20 | 122..450 | 329 | 285 | 285 | 0 | 0 | 0 | 0 | 78897 |
| 22 | 124..491 | 368 | 327 | 327 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116 |
| 23 | 124..467 | 344 | 303 | 303 | 0 | 0 | 0 | 0 | 79098, 79102, 79103 |
| 24 | 126..515 | 390 | 338 | 338 | 0 | 0 | 0 | 0 | 79116, 79122, 79132 |
| 25 | 131..542 | 412 | 369 | 369 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 26 | 134..538 | 405 | 359 | 359 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 27 | 137..500 | 364 | 322 | 322 | 0 | 0 | 0 | 0 | 79111 |
| 28 | 138..537 | 400 | 350 | 350 | 0 | 0 | 0 | 0 | 79136, 79139 |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9046; unmatched reference entries: 1096; unmatched candidate entries: 0
- identity switches: 130; fragmentation (coverage interruptions): 924; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 2 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 3 -> 2 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 3 -> 2 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 2 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 7 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 3 -> 2 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 5 -> 3 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 5 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 5 -> 3 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 2 -> 12 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 3 -> 11 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 3 at (2136, 3025.5), 2 frames after previous cover
- f101: ref 79103: 10 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 14 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 11 -> 13 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 10 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 2 -> 12 at (2064, 3032), 2 frames after previous cover
- f104: ref 78899: 14 -> 2 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 12 -> 1 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 13 -> 14 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 11 -> 13 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 3 -> 11 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 3 at (2126, 3022.5), 3 frames after previous cover
- f108: ref 79045: 1 -> 16 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 14 -> 2 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 13 -> 14 at (2084.5, 3028.5), 2 frames after previous cover
- f108: ref 79102: 11 -> 13 at (2096.5, 3027.5), 1 frames after previous cover
- f109: ref 79103: 3 -> 11 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 5 -> 3 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 10 -> 5 at (2125, 3025), 2 frames after previous cover
- f111: ref 78899: 2 -> 18 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 13 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 13 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 3 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 3 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 10 -> 5 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 2 -> 11 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 11 -> 3 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 3 -> 5 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 5 -> 10 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 18 -> 12 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 2 -> 18 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 13 -> 14 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 3 -> 13 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 5 -> 3 at (2092.5, 3025.5), 2 frames after previous cover
- f115: ref 79110: 10 -> 5 at (2105.5, 3026.5), 1 frames after previous cover
- f117: ref 79116: 17 -> 19 at (2137.5, 3024.5), 1 frames after previous cover
- f118: ref 78897: 12 -> 16 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 14 -> 2 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 13 -> 14 at (2057, 3025), 2 frames after previous cover
- f118: ref 79108: 3 -> 13 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 5 -> 3 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 10 -> 5 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 10 at (2118, 3022), 5 frames after previous cover
- f119: ref 79103: 2 -> 14 at (2040, 3024.5), 1 frames after previous cover
- ... 70 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 901 | 99 | 0 (901) |
| 78896 | 350 (76..429) | 313 | 32 | 4 (307), 1 (6) |
| 78969 | 352 (80..434) | 308 | 30 | 7 (304), 1 (4) |
| 78971 | 352 (84..439) | 313 | 32 | 16 (273), 8 (32), 2 (4), 1 (3), 7 (1) |
| 79045 | 355 (84..443) | 313 | 34 | 8 (275), 16 (20), 1 (12), 2 (3), 12 (2), 3 (1) |
| 79037 | 355 (86..445) | 317 | 31 | 12 (278), 1 (23), 2 (6), 8 (6), 3 (4) |
| 78897 | 345 (89..450) | 308 | 31 | 20 (285), 12 (11), 3 (6), 2 (5), 16 (1) |
| 78899 | 365 (91..455) | 318 | 37 | 11 (289), 12 (15), 2 (5), 18 (5), 5 (3), 14 (1) |
| 79097 | 366 (94..461) | 333 | 28 | 18 (300), 11 (20), 14 (4), 5 (3), 2 (3), 3 (2), 13 (1) |
| 79098 | 360 (97..467) | 329 | 28 | 23 (293), 18 (16), 2 (4), 11 (3), 13 (3), 14 (3), 1 (3), 5 (2), 3 (2) |
| 79102 | 371 (98..477) | 328 | 37 | 1 (304), 3 (4), 11 (4), 14 (4), 2 (4), 13 (3), 23 (3), 5 (1), 18 (1) |
| 79103 | 380 (99..481) | 339 | 35 | 3 (312), 2 (8), 23 (7), 13 (4), 14 (4), 11 (2), 10 (1), 5 (1) |
| 79105 | 379 (101..484) | 329 | 43 | 2 (303), 3 (8), 14 (8), 5 (6), 13 (2), 10 (1), 11 (1) |
| 79108 | 385 (104..492) | 346 | 35 | 22 (318), 3 (11), 14 (5), 10 (4), 5 (4), 13 (2), 2 (2) |
| 79110 | 388 (106..497) | 356 | 28 | 14 (334), 10 (6), 13 (6), 3 (5), 5 (4), 22 (1) |
| 79111 | 386 (109..500) | 341 | 30 | 27 (322), 5 (9), 13 (5), 10 (4), 22 (1) |
| 79115 | 421 (111..531) | 371 | 42 | 13 (358), 5 (4), 17 (3), 10 (3), 22 (3) |
| 79116 | 411 (114..530) | 374 | 29 | 5 (356), 10 (7), 22 (4), 17 (3), 19 (3), 24 (1) |
| 79122 | 404 (118..532) | 364 | 33 | 10 (357), 19 (4), 17 (2), 24 (1) |
| 79132 | 391 (120..515) | 342 | 44 | 24 (336), 17 (3), 19 (3) |
| 79128 | 402 (124..527) | 360 | 37 | 19 (357), 17 (3) |
| 79134 | 407 (127..533) | 365 | 36 | 17 (365) |
| 79135 | 409 (129..542) | 367 | 36 | 25 (367) |
| 79139 | 406 (132..537) | 358 | 43 | 26 (305), 28 (51), 25 (2) |
| 79136 | 393 (136..538) | 353 | 34 | 28 (299), 26 (54) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 329/393/1007; tracks with internal gaps: 0; total internal gaps: 0; longest internal gap: 0; tracks ending in coasting: 0 (trailing rows total 0)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 901 | 901 | 0 | 0 | 0 | 0 | 78911 |
| 1 | 78..477 | 400 | 355 | 355 | 0 | 0 | 0 | 0 | 78896, 78969, 78971, 79037, 79045, 79098, 79102 |
| 2 | 84..484 | 401 | 347 | 347 | 0 | 0 | 0 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 3 | 86..481 | 396 | 355 | 355 | 0 | 0 | 0 | 0 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 87..429 | 343 | 307 | 307 | 0 | 0 | 0 | 0 | 78896 |
| 5 | 91..530 | 440 | 393 | 393 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116 |
| 7 | 93..434 | 342 | 305 | 305 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 8 | 94..443 | 350 | 313 | 313 | 0 | 0 | 0 | 0 | 78971, 79037, 79045 |
| 10 | 100..532 | 433 | 383 | 383 | 0 | 0 | 0 | 0 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 100..455 | 356 | 319 | 319 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..445 | 346 | 306 | 306 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79045 |
| 13 | 103..531 | 429 | 384 | 384 | 0 | 0 | 0 | 0 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 14 | 103..495 | 393 | 363 | 363 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 16 | 108..439 | 332 | 294 | 294 | 0 | 0 | 0 | 0 | 78897, 78971, 79045 |
| 17 | 111..533 | 423 | 379 | 379 | 0 | 0 | 0 | 0 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 18 | 111..461 | 351 | 322 | 322 | 0 | 0 | 0 | 0 | 78899, 79097, 79098, 79102 |
| 19 | 117..527 | 411 | 367 | 367 | 0 | 0 | 0 | 0 | 79116, 79122, 79128, 79132 |
| 20 | 122..450 | 329 | 285 | 285 | 0 | 0 | 0 | 0 | 78897 |
| 22 | 124..491 | 368 | 327 | 327 | 0 | 0 | 0 | 0 | 79108, 79110, 79111, 79115, 79116 |
| 23 | 124..467 | 344 | 303 | 303 | 0 | 0 | 0 | 0 | 79098, 79102, 79103 |
| 24 | 126..515 | 390 | 338 | 338 | 0 | 0 | 0 | 0 | 79116, 79122, 79132 |
| 25 | 131..542 | 412 | 369 | 369 | 0 | 0 | 0 | 0 | 79135, 79139 |
| 26 | 134..538 | 405 | 359 | 359 | 0 | 0 | 0 | 0 | 79136, 79139 |
| 27 | 137..500 | 364 | 322 | 322 | 0 | 0 | 0 | 0 | 79111 |
| 28 | 138..537 | 400 | 350 | 350 | 0 | 0 | 0 | 0 | 79136, 79139 |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9908; unmatched reference entries: 234; unmatched candidate entries: 953
- identity switches: 132; fragmentation (coverage interruptions): 159; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 2 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 3 -> 2 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 3 -> 2 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 2 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 7 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 3 -> 2 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 5 -> 3 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 5 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 5 -> 3 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 2 -> 12 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 3 -> 11 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 3 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 10 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 14 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 11 -> 13 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 10 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 2 -> 12 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 14 -> 2 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 12 -> 1 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 13 -> 14 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 11 -> 13 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 3 -> 11 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 3 at (2126, 3022.5), 2 frames after previous cover
- f108: ref 79045: 1 -> 16 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 14 -> 2 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 13 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 79103: 3 -> 13 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 5 -> 3 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 10 -> 5 at (2125, 3025), 2 frames after previous cover
- f110: ref 79102: 11 -> 13 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 13 -> 11 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 78899: 2 -> 18 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 13 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 13 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 3 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 3 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 10 -> 5 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 2 -> 11 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 11 -> 3 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 3 -> 5 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 5 -> 10 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 18 -> 12 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 2 -> 18 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 13 -> 14 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 3 -> 13 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 5 -> 3 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 10 -> 5 at (2105.5, 3026.5), 1 frames after previous cover
- f118: ref 78897: 12 -> 16 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 14 -> 2 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 13 -> 14 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 3 -> 13 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 5 -> 3 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 10 -> 5 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 10 at (2118, 3022), 5 frames after previous cover
- f118: ref 79116: 17 -> 19 at (2131.5, 3022.5), 1 frames after previous cover
- ... 72 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1004 | 3 | 0 (1004) |
| 78896 | 350 (76..429) | 341 | 5 | 4 (335), 1 (6) |
| 78969 | 352 (80..434) | 333 | 8 | 7 (329), 1 (4) |
| 78971 | 352 (84..439) | 340 | 9 | 16 (299), 8 (33), 2 (4), 1 (3), 7 (1) |
| 79045 | 355 (84..443) | 342 | 7 | 8 (302), 16 (21), 1 (13), 2 (3), 12 (2), 3 (1) |
| 79037 | 355 (86..445) | 344 | 7 | 12 (305), 1 (23), 2 (6), 8 (6), 3 (4) |
| 78897 | 345 (89..450) | 335 | 6 | 20 (310), 12 (12), 3 (6), 2 (6), 16 (1) |
| 78899 | 365 (91..455) | 349 | 8 | 11 (320), 12 (15), 2 (5), 18 (5), 5 (3), 14 (1) |
| 79097 | 366 (94..461) | 356 | 9 | 18 (322), 11 (21), 14 (4), 5 (3), 2 (3), 3 (2), 13 (1) |
| 79098 | 360 (97..467) | 355 | 5 | 23 (318), 18 (16), 13 (4), 2 (4), 11 (3), 14 (3), 1 (3), 5 (2), 3 (2) |
| 79102 | 371 (98..477) | 362 | 5 | 1 (337), 11 (6), 3 (4), 14 (4), 2 (4), 23 (3), 5 (2), 13 (1), 18 (1) |
| 79103 | 380 (99..481) | 370 | 8 | 3 (339), 2 (8), 23 (7), 13 (5), 14 (4), 1 (3), 5 (2), 10 (1), 11 (1) |
| 79105 | 379 (101..484) | 371 | 7 | 2 (344), 3 (8), 14 (8), 5 (6), 13 (3), 10 (1), 11 (1) |
| 79108 | 385 (104..492) | 380 | 5 | 22 (351), 3 (11), 5 (5), 14 (5), 10 (4), 13 (2), 2 (2) |
| 79110 | 388 (106..497) | 386 | 1 | 14 (363), 13 (7), 10 (6), 3 (5), 5 (4), 22 (1) |
| 79111 | 386 (109..500) | 370 | 8 | 27 (350), 5 (9), 13 (5), 10 (4), 22 (2) |
| 79115 | 421 (111..531) | 411 | 5 | 13 (397), 5 (5), 17 (3), 10 (3), 22 (3) |
| 79116 | 411 (114..530) | 402 | 8 | 5 (384), 10 (7), 17 (4), 22 (4), 19 (2), 24 (1) |
| 79122 | 404 (118..532) | 393 | 8 | 10 (386), 19 (4), 17 (2), 24 (1) |
| 79132 | 391 (120..515) | 384 | 7 | 24 (376), 17 (4), 19 (3), 5 (1) |
| 79128 | 402 (124..527) | 396 | 6 | 19 (393), 17 (3) |
| 79134 | 407 (127..533) | 400 | 6 | 17 (400) |
| 79135 | 409 (129..542) | 404 | 3 | 25 (404) |
| 79139 | 406 (132..537) | 398 | 6 | 26 (340), 28 (56), 25 (2) |
| 79136 | 393 (136..538) | 382 | 9 | 28 (326), 26 (56) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 358/422/1007; tracks with internal gaps: 25; total internal gaps: 222; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 692)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1004 | 3 | 3 | 1 | 0 | 78911 |
| 1 | 78..506 | 429 | 429 | 392 | 37 | 11 | 2 | 25 | 78896, 78969, 78971, 79037, 79045, 79098, 79102, 79103 |
| 2 | 84..513 | 430 | 430 | 389 | 41 | 10 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 3 | 86..510 | 425 | 425 | 382 | 43 | 8 | 3 | 32 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 87..458 | 372 | 372 | 335 | 37 | 6 | 3 | 29 | 78896 |
| 5 | 91..559 | 469 | 469 | 426 | 43 | 11 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 7 | 93..463 | 371 | 371 | 330 | 41 | 9 | 2 | 29 | 78969, 78971 |
| 8 | 94..472 | 379 | 379 | 341 | 38 | 8 | 2 | 29 | 78971, 79037, 79045 |
| 10 | 100..561 | 462 | 462 | 412 | 50 | 15 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 100..484 | 385 | 385 | 352 | 33 | 4 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..474 | 375 | 375 | 334 | 41 | 8 | 3 | 29 | 78897, 78899, 79037, 79045 |
| 13 | 103..560 | 458 | 458 | 425 | 33 | 4 | 1 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 14 | 103..524 | 422 | 422 | 392 | 30 | 3 | 1 | 27 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 16 | 108..468 | 361 | 361 | 321 | 40 | 9 | 2 | 29 | 78897, 78971, 79045 |
| 17 | 111..562 | 452 | 452 | 416 | 36 | 6 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 18 | 111..490 | 380 | 380 | 344 | 36 | 7 | 1 | 29 | 78899, 79097, 79098, 79102 |
| 19 | 117..556 | 440 | 440 | 402 | 38 | 9 | 1 | 29 | 79116, 79122, 79128, 79132 |
| 20 | 122..479 | 358 | 358 | 310 | 48 | 18 | 2 | 29 | 78897 |
| 22 | 124..520 | 397 | 397 | 361 | 36 | 8 | 1 | 28 | 79108, 79110, 79111, 79115, 79116 |
| 23 | 124..496 | 373 | 373 | 328 | 45 | 14 | 2 | 29 | 79098, 79102, 79103 |
| 24 | 126..544 | 419 | 419 | 378 | 41 | 11 | 2 | 29 | 79116, 79122, 79132 |
| 25 | 131..571 | 441 | 441 | 406 | 35 | 6 | 1 | 29 | 79135, 79139 |
| 26 | 134..567 | 434 | 434 | 396 | 38 | 8 | 2 | 29 | 79136, 79139 |
| 27 | 137..529 | 393 | 393 | 350 | 43 | 11 | 2 | 29 | 79111 |
| 28 | 138..566 | 429 | 429 | 382 | 47 | 15 | 3 | 29 | 79136, 79139 |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 9908; unmatched reference entries: 234; unmatched candidate entries: 953
- identity switches: 132; fragmentation (coverage interruptions): 159; orphan candidate ids (never on a reference object): 0

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f87: ref 78896: 1 -> 4 at (2090.5, 3033), 4 frames after previous cover
- f88: ref 78971: 2 -> 1 at (2125.5, 3034), 1 frames after previous cover
- f88: ref 79045: 3 -> 2 at (2135.5, 3033), 1 frames after previous cover
- f91: ref 79037: 3 -> 2 at (2129, 3033.5), 1 frames after previous cover
- f91: ref 79045: 2 -> 1 at (2116.5, 3034), 1 frames after previous cover
- f93: ref 78969: 1 -> 7 at (2077.5, 3034), 6 frames after previous cover
- f94: ref 78971: 1 -> 8 at (2090.5, 3032.5), 4 frames after previous cover
- f97: ref 78897: 3 -> 2 at (2107, 3033), 1 frames after previous cover
- f97: ref 79097: 5 -> 3 at (2135, 3028), 1 frames after previous cover
- f99: ref 78899: 5 -> 2 at (2109.5, 3030), 6 frames after previous cover
- f99: ref 79098: 5 -> 3 at (2135.5, 3025.5), 1 frames after previous cover
- f100: ref 79037: 2 -> 12 at (2076, 3033.5), 4 frames after previous cover
- f100: ref 79097: 3 -> 11 at (2117.5, 3029.5), 2 frames after previous cover
- f101: ref 79098: 3 -> 11 at (2124, 3028), 1 frames after previous cover
- f101: ref 79102: 5 -> 3 at (2136, 3025.5), 1 frames after previous cover
- f101: ref 79103: 10 -> 5 at (2145, 3023.5), 1 frames after previous cover
- f103: ref 78899: 2 -> 14 at (2086, 3030), 4 frames after previous cover
- f103: ref 79097: 11 -> 13 at (2100, 3028.5), 3 frames after previous cover
- f103: ref 79105: 10 -> 5 at (2143, 3025.5), 2 frames after previous cover
- f104: ref 78897: 2 -> 12 at (2064, 3032), 1 frames after previous cover
- f104: ref 78899: 14 -> 2 at (2079.5, 3030.5), 1 frames after previous cover
- f104: ref 79037: 12 -> 1 at (2051, 3034), 1 frames after previous cover
- f104: ref 79097: 13 -> 14 at (2093.5, 3029.5), 1 frames after previous cover
- f104: ref 79098: 11 -> 13 at (2107, 3027.5), 1 frames after previous cover
- f104: ref 79102: 3 -> 11 at (2119, 3027), 1 frames after previous cover
- f104: ref 79103: 5 -> 3 at (2126, 3022.5), 2 frames after previous cover
- f108: ref 79045: 1 -> 16 at (2014.5, 3034), 5 frames after previous cover
- f108: ref 79097: 14 -> 2 at (2070, 3029.5), 1 frames after previous cover
- f108: ref 79098: 13 -> 14 at (2084.5, 3028.5), 1 frames after previous cover
- f109: ref 79103: 3 -> 13 at (2097, 3024.5), 1 frames after previous cover
- f109: ref 79105: 5 -> 3 at (2107.5, 3023.5), 1 frames after previous cover
- f109: ref 79108: 10 -> 5 at (2125, 3025), 2 frames after previous cover
- f110: ref 79102: 11 -> 13 at (2084.5, 3028.5), 1 frames after previous cover
- f110: ref 79103: 13 -> 11 at (2092.5, 3023.5), 1 frames after previous cover
- f111: ref 78899: 2 -> 18 at (2037, 3030.5), 4 frames after previous cover
- f111: ref 79098: 14 -> 2 at (2065.5, 3029), 1 frames after previous cover
- f111: ref 79102: 13 -> 14 at (2079, 3029.5), 1 frames after previous cover
- f111: ref 79103: 11 -> 13 at (2087.5, 3023.5), 1 frames after previous cover
- f111: ref 79105: 3 -> 11 at (2096.5, 3025), 1 frames after previous cover
- f111: ref 79108: 5 -> 3 at (2113.5, 3026), 1 frames after previous cover
- f111: ref 79110: 10 -> 5 at (2129, 3027), 1 frames after previous cover
- f112: ref 79097: 2 -> 11 at (2046, 3030.5), 2 frames after previous cover
- f112: ref 79105: 11 -> 3 at (2091.5, 3025.5), 1 frames after previous cover
- f112: ref 79108: 3 -> 5 at (2109, 3027), 1 frames after previous cover
- f112: ref 79110: 5 -> 10 at (2124.5, 3027.5), 1 frames after previous cover
- f115: ref 78899: 18 -> 12 at (2012.5, 3030), 1 frames after previous cover
- f115: ref 79098: 2 -> 18 at (2042.5, 3029), 1 frames after previous cover
- f115: ref 79102: 14 -> 2 at (2055, 3030), 1 frames after previous cover
- f115: ref 79103: 13 -> 14 at (2062.5, 3023), 1 frames after previous cover
- f115: ref 79105: 3 -> 13 at (2073, 3025), 1 frames after previous cover
- f115: ref 79108: 5 -> 3 at (2092.5, 3025.5), 1 frames after previous cover
- f115: ref 79110: 10 -> 5 at (2105.5, 3026.5), 1 frames after previous cover
- f118: ref 78897: 12 -> 16 at (1977.5, 3035), 2 frames after previous cover
- f118: ref 79103: 14 -> 2 at (2045, 3024.5), 1 frames after previous cover
- f118: ref 79105: 13 -> 14 at (2057, 3025), 1 frames after previous cover
- f118: ref 79108: 3 -> 13 at (2077, 3026), 1 frames after previous cover
- f118: ref 79110: 5 -> 3 at (2090, 3026.5), 1 frames after previous cover
- f118: ref 79111: 10 -> 5 at (2103.5, 3028), 1 frames after previous cover
- f118: ref 79115: 17 -> 10 at (2118, 3022), 5 frames after previous cover
- f118: ref 79116: 17 -> 19 at (2131.5, 3022.5), 1 frames after previous cover
- ... 72 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 1004 | 3 | 0 (1004) |
| 78896 | 350 (76..429) | 341 | 5 | 4 (335), 1 (6) |
| 78969 | 352 (80..434) | 333 | 8 | 7 (329), 1 (4) |
| 78971 | 352 (84..439) | 340 | 9 | 16 (299), 8 (33), 2 (4), 1 (3), 7 (1) |
| 79045 | 355 (84..443) | 342 | 7 | 8 (302), 16 (21), 1 (13), 2 (3), 12 (2), 3 (1) |
| 79037 | 355 (86..445) | 344 | 7 | 12 (305), 1 (23), 2 (6), 8 (6), 3 (4) |
| 78897 | 345 (89..450) | 335 | 6 | 20 (310), 12 (12), 3 (6), 2 (6), 16 (1) |
| 78899 | 365 (91..455) | 349 | 8 | 11 (320), 12 (15), 2 (5), 18 (5), 5 (3), 14 (1) |
| 79097 | 366 (94..461) | 356 | 9 | 18 (322), 11 (21), 14 (4), 5 (3), 2 (3), 3 (2), 13 (1) |
| 79098 | 360 (97..467) | 355 | 5 | 23 (318), 18 (16), 13 (4), 2 (4), 11 (3), 14 (3), 1 (3), 5 (2), 3 (2) |
| 79102 | 371 (98..477) | 362 | 5 | 1 (337), 11 (6), 3 (4), 14 (4), 2 (4), 23 (3), 5 (2), 13 (1), 18 (1) |
| 79103 | 380 (99..481) | 370 | 8 | 3 (339), 2 (8), 23 (7), 13 (5), 14 (4), 1 (3), 5 (2), 10 (1), 11 (1) |
| 79105 | 379 (101..484) | 371 | 7 | 2 (344), 3 (8), 14 (8), 5 (6), 13 (3), 10 (1), 11 (1) |
| 79108 | 385 (104..492) | 380 | 5 | 22 (351), 3 (11), 5 (5), 14 (5), 10 (4), 13 (2), 2 (2) |
| 79110 | 388 (106..497) | 386 | 1 | 14 (363), 13 (7), 10 (6), 3 (5), 5 (4), 22 (1) |
| 79111 | 386 (109..500) | 370 | 8 | 27 (350), 5 (9), 13 (5), 10 (4), 22 (2) |
| 79115 | 421 (111..531) | 411 | 5 | 13 (397), 5 (5), 17 (3), 10 (3), 22 (3) |
| 79116 | 411 (114..530) | 402 | 8 | 5 (384), 10 (7), 17 (4), 22 (4), 19 (2), 24 (1) |
| 79122 | 404 (118..532) | 393 | 8 | 10 (386), 19 (4), 17 (2), 24 (1) |
| 79132 | 391 (120..515) | 384 | 7 | 24 (376), 17 (4), 19 (3), 5 (1) |
| 79128 | 402 (124..527) | 396 | 6 | 19 (393), 17 (3) |
| 79134 | 407 (127..533) | 400 | 6 | 17 (400) |
| 79135 | 409 (129..542) | 404 | 3 | 25 (404) |
| 79139 | 406 (132..537) | 398 | 6 | 26 (340), 28 (56), 25 (2) |
| 79136 | 393 (136..538) | 382 | 9 | 28 (326), 26 (56) |

### Orphan candidate ids
- none

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 358/422/1007; tracks with internal gaps: 25; total internal gaps: 222; longest internal gap: 3; tracks ending in coasting: 24 (trailing rows total 692)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 1004 | 3 | 3 | 1 | 0 | 78911 |
| 1 | 78..506 | 429 | 429 | 392 | 37 | 11 | 2 | 25 | 78896, 78969, 78971, 79037, 79045, 79098, 79102, 79103 |
| 2 | 84..513 | 430 | 430 | 389 | 41 | 10 | 2 | 29 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 3 | 86..510 | 425 | 425 | 382 | 43 | 8 | 3 | 32 | 78897, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 4 | 87..458 | 372 | 372 | 335 | 37 | 6 | 3 | 29 | 78896 |
| 5 | 91..559 | 469 | 469 | 426 | 43 | 11 | 2 | 29 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79132 |
| 7 | 93..463 | 371 | 371 | 330 | 41 | 9 | 2 | 29 | 78969, 78971 |
| 8 | 94..472 | 379 | 379 | 341 | 38 | 8 | 2 | 29 | 78971, 79037, 79045 |
| 10 | 100..561 | 462 | 462 | 412 | 50 | 15 | 3 | 29 | 79103, 79105, 79108, 79110, 79111, 79115, 79116, 79122 |
| 11 | 100..484 | 385 | 385 | 352 | 33 | 4 | 1 | 29 | 78899, 79097, 79098, 79102, 79103, 79105 |
| 12 | 100..474 | 375 | 375 | 334 | 41 | 8 | 3 | 29 | 78897, 78899, 79037, 79045 |
| 13 | 103..560 | 458 | 458 | 425 | 33 | 4 | 1 | 29 | 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115 |
| 14 | 103..524 | 422 | 422 | 392 | 30 | 3 | 1 | 27 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 16 | 108..468 | 361 | 361 | 321 | 40 | 9 | 2 | 29 | 78897, 78971, 79045 |
| 17 | 111..562 | 452 | 452 | 416 | 36 | 6 | 2 | 29 | 79115, 79116, 79122, 79128, 79132, 79134 |
| 18 | 111..490 | 380 | 380 | 344 | 36 | 7 | 1 | 29 | 78899, 79097, 79098, 79102 |
| 19 | 117..556 | 440 | 440 | 402 | 38 | 9 | 1 | 29 | 79116, 79122, 79128, 79132 |
| 20 | 122..479 | 358 | 358 | 310 | 48 | 18 | 2 | 29 | 78897 |
| 22 | 124..520 | 397 | 397 | 361 | 36 | 8 | 1 | 28 | 79108, 79110, 79111, 79115, 79116 |
| 23 | 124..496 | 373 | 373 | 328 | 45 | 14 | 2 | 29 | 79098, 79102, 79103 |
| 24 | 126..544 | 419 | 419 | 378 | 41 | 11 | 2 | 29 | 79116, 79122, 79132 |
| 25 | 131..571 | 441 | 441 | 406 | 35 | 6 | 1 | 29 | 79135, 79139 |
| 26 | 134..567 | 434 | 434 | 396 | 38 | 8 | 2 | 29 | 79136, 79139 |
| 27 | 137..529 | 393 | 393 | 350 | 43 | 11 | 2 | 29 | 79111 |
| 28 | 138..566 | 429 | 429 | 382 | 47 | 15 | 3 | 29 | 79136, 79139 |
