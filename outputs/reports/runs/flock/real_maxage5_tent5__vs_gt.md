# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 5, "tentative_threshold": 5}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=679e182e4d04 git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage5_tent5/tracks.csv sha256=8150441636d6cfe1
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage5_tent5
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
| observations | none | 4 | 10142 | 3838 | 0.249 | 0.098 | 0.641 | 0.97 | 0.267 | -0.126 | 0.99 | 76 | 225.0 | 0.162 | 0.295 | 0.112 | 0.130 | 0.344 | 1319 | 8823 | 2519 | 1 | 0 | 24 |
| observations | none | 6 | 10142 | 3838 | 0.261 | 0.110 | 0.630 | 1.35 | 0.274 | -0.102 | 1.36 | 102 | 294.0 | 0.170 | 0.310 | 0.117 | 0.143 | 0.379 | 1454 | 8688 | 2384 | 1 | 1 | 23 |
| observations | none | 8 | 10142 | 3838 | 0.270 | 0.121 | 0.616 | 1.82 | 0.276 | -0.085 | 1.71 | 125 | 347.0 | 0.175 | 0.318 | 0.120 | 0.153 | 0.404 | 1551 | 8591 | 2287 | 1 | 1 | 23 |
| observations | none | 12 | 10142 | 3838 | 0.281 | 0.134 | 0.604 | 2.49 | 0.283 | -0.043 | 2.80 | 139 | 396.0 | 0.191 | 0.347 | 0.131 | 0.175 | 0.461 | 1770 | 8372 | 2068 | 1 | 2 | 22 |
| observations | ignore | 4 | 10142 | 3572 | 0.252 | 0.100 | 0.641 | 0.97 | 0.269 | -0.100 | 0.99 | 76 | 225.0 | 0.165 | 0.317 | 0.112 | 0.130 | 0.369 | 1319 | 8823 | 2253 | 1 | 0 | 24 |
| observations | ignore | 6 | 10142 | 3572 | 0.264 | 0.112 | 0.630 | 1.35 | 0.277 | -0.076 | 1.36 | 102 | 294.0 | 0.174 | 0.333 | 0.117 | 0.143 | 0.407 | 1454 | 8688 | 2118 | 1 | 1 | 23 |
| observations | ignore | 8 | 10142 | 3572 | 0.273 | 0.123 | 0.616 | 1.82 | 0.279 | -0.059 | 1.71 | 125 | 347.0 | 0.178 | 0.342 | 0.120 | 0.153 | 0.434 | 1551 | 8591 | 2021 | 1 | 1 | 23 |
| observations | ignore | 12 | 10142 | 3572 | 0.284 | 0.137 | 0.604 | 2.49 | 0.286 | -0.017 | 2.80 | 139 | 396.0 | 0.194 | 0.373 | 0.131 | 0.175 | 0.496 | 1770 | 8372 | 1802 | 1 | 2 | 22 |
| updates | none | 4 | 10142 | 4562 | 0.243 | 0.096 | 0.623 | 1.04 | 0.260 | -0.191 | 1.03 | 87 | 244.0 | 0.155 | 0.250 | 0.112 | 0.134 | 0.297 | 1356 | 8786 | 3206 | 1 | 0 | 24 |
| updates | none | 6 | 10142 | 4562 | 0.255 | 0.110 | 0.605 | 1.49 | 0.267 | -0.160 | 1.47 | 117 | 312.0 | 0.164 | 0.265 | 0.119 | 0.151 | 0.335 | 1527 | 8615 | 3035 | 1 | 1 | 23 |
| updates | none | 8 | 10142 | 4562 | 0.264 | 0.123 | 0.586 | 1.99 | 0.270 | -0.136 | 1.91 | 137 | 358.0 | 0.169 | 0.273 | 0.123 | 0.164 | 0.364 | 1662 | 8480 | 2900 | 1 | 1 | 23 |
| updates | none | 12 | 10142 | 4562 | 0.275 | 0.137 | 0.569 | 2.75 | 0.278 | -0.085 | 3.09 | 148 | 395.0 | 0.186 | 0.300 | 0.135 | 0.190 | 0.422 | 1925 | 8217 | 2637 | 1 | 2 | 22 |
| updates | ignore | 4 | 10142 | 4099 | 0.247 | 0.099 | 0.623 | 1.04 | 0.264 | -0.145 | 1.03 | 87 | 244.0 | 0.160 | 0.278 | 0.112 | 0.134 | 0.331 | 1356 | 8786 | 2743 | 1 | 0 | 24 |
| updates | ignore | 6 | 10142 | 4099 | 0.260 | 0.114 | 0.605 | 1.49 | 0.272 | -0.115 | 1.47 | 117 | 312.0 | 0.170 | 0.295 | 0.119 | 0.151 | 0.373 | 1527 | 8615 | 2572 | 1 | 1 | 23 |
| updates | ignore | 8 | 10142 | 4099 | 0.269 | 0.127 | 0.586 | 1.99 | 0.275 | -0.090 | 1.91 | 137 | 358.0 | 0.175 | 0.304 | 0.123 | 0.164 | 0.405 | 1662 | 8480 | 2437 | 1 | 1 | 23 |
| updates | ignore | 12 | 10142 | 4099 | 0.280 | 0.142 | 0.569 | 2.75 | 0.283 | -0.039 | 3.09 | 148 | 395.0 | 0.192 | 0.333 | 0.135 | 0.190 | 0.470 | 1925 | 8217 | 2174 | 1 | 2 | 22 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 84; matched pairs: 1551; unmatched reference entries: 8591; unmatched candidate entries: 2287
- identity switches: 125; fragmentation (coverage interruptions): 348; orphan candidate ids (never on a reference object): 62

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f34: ref 78911: 0 -> 5 at (1812.5, 3363), 27 frames after previous cover
- f176: ref 79132: 24 -> 26 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 24 -> 26 at (1843, 3015), 10 frames after previous cover
- f181: ref 79134: 26 -> 24 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 6 -> 24 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 24 -> 6 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78971: 24 -> 6 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 79134: 24 -> 26 at (1753.5, 3017.5), 11 frames after previous cover
- f196: ref 79139: 26 -> 33 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 26 -> 33 at (1718, 3008.5), 8 frames after previous cover
- f201: ref 79132: 26 -> 24 at (1646.5, 3013), 25 frames after previous cover
- f205: ref 79097: 24 -> 36 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 78897: 24 -> 36 at (1401.5, 3004.5), 12 frames after previous cover
- f206: ref 79135: 33 -> 24 at (1673, 3006), 2 frames after previous cover
- f207: ref 79134: 26 -> 24 at (1655.5, 3014), 15 frames after previous cover
- f210: ref 78899: 24 -> 36 at (1400, 3003.5), 11 frames after previous cover
- f211: ref 79135: 24 -> 33 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 24 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f214: ref 79132: 24 -> 33 at (1561, 3005), 4 frames after previous cover
- f216: ref 79037: 6 -> 36 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 36 -> 24 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 24 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 24 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 24 -> 33 at (1465, 3003), 7 frames after previous cover
- f225: ref 78899: 36 -> 24 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 36 -> 24 at (1272, 2992), 12 frames after previous cover
- f227: ref 79105: 24 -> 33 at (1392, 2996), 13 frames after previous cover
- f228: ref 79103: 24 -> 33 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 6 -> 24 at (1202, 2988), 41 frames after previous cover
- f230: ref 79134: 24 -> 33 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79097: 24 -> 45 at (1295, 2989.5), 7 frames after previous cover
- f235: ref 78899: 24 -> 45 at (1242.5, 2989), 10 frames after previous cover
- f237: ref 79037: 36 -> 45 at (1184.5, 2988), 21 frames after previous cover
- f240: ref 79108: 33 -> 45 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 33 -> 45 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 24 -> 6 at (1119, 2986), 13 frames after previous cover
- f242: ref 79111: 33 -> 45 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 45 -> 49 at (1179, 2985.5), 10 frames after previous cover
- f246: ref 79097: 45 -> 49 at (1199.5, 2985), 7 frames after previous cover
- f255: ref 79037: 45 -> 49 at (1069.5, 2987.5), 18 frames after previous cover
- f260: ref 78897: 24 -> 49 at (1057.5, 2987.5), 34 frames after previous cover
- f271: ref 79037: 49 -> 6 at (965, 2987), 8 frames after previous cover
- f272: ref 79045: 24 -> 6 at (945.5, 2991.5), 45 frames after previous cover
- f281: ref 79098: 33 -> 49 at (1009.5, 2985), 44 frames after previous cover
- f287: ref 78896: 6 -> 60 at (775, 2987), 48 frames after previous cover
- f290: ref 79103: 45 -> 49 at (995.5, 2980.5), 42 frames after previous cover
- f304: ref 78969: 6 -> 49 at (689.5, 2980), 34 frames after previous cover
- f304: ref 79108: 45 -> 76 at (954, 2978), 64 frames after previous cover
- f317: ref 79134: 33 -> 76 at (990.5, 2965.5), 74 frames after previous cover
- f327: ref 79132: 33 -> 76 at (895, 2966.5), 88 frames after previous cover
- f331: ref 79102: 45 -> 76 at (723.5, 2979.5), 82 frames after previous cover
- f332: ref 79098: 49 -> 76 at (692, 2975.5), 51 frames after previous cover
- f333: ref 79097: 49 -> 76 at (654.5, 2972.5), 39 frames after previous cover
- f334: ref 78899: 49 -> 76 at (619, 2977.5), 39 frames after previous cover
- f335: ref 78969: 49 -> 83 at (508, 2966.5), 28 frames after previous cover
- f345: ref 79135: 33 -> 85 at (875.5, 2962), 103 frames after previous cover
- f346: ref 78897: 49 -> 76 at (523, 2971.5), 63 frames after previous cover
- f346: ref 79128: 33 -> 85 at (828, 2962), 102 frames after previous cover
- f348: ref 79110: 33 -> 85 at (701.5, 2979.5), 102 frames after previous cover
- ... 65 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 970 | 8 | 5 (968), 0 (2) |
| 78896 | 350 (76..429) | 8 | 6 | 6 (4), 96 (2), 60 (1), 83 (1) |
| 78969 | 352 (80..434) | 88 | 43 | 6 (64), 83 (12), 96 (8), 49 (3), 105 (1) |
| 78971 | 352 (84..439) | 15 | 10 | 96 (7), 6 (4), 24 (2), 76 (1), 83 (1) |
| 79045 | 355 (84..443) | 16 | 11 | 76 (5), 83 (5), 96 (3), 6 (2), 24 (1) |
| 79037 | 355 (86..445) | 15 | 14 | 83 (5), 6 (2), 49 (2), 96 (2), 24 (1), 36 (1), 45 (1), 76 (1) |
| 78897 | 345 (89..450) | 26 | 20 | 96 (9), 83 (5), 24 (4), 49 (3), 76 (3), 36 (2) |
| 78899 | 365 (91..455) | 45 | 36 | 49 (15), 24 (8), 83 (7), 76 (6), 96 (5), 36 (3), 45 (1) |
| 79097 | 366 (94..461) | 62 | 39 | 49 (18), 76 (12), 24 (10), 45 (7), 36 (6), 96 (4), 83 (4), 108 (1) |
| 79098 | 360 (97..467) | 21 | 17 | 108 (11), 76 (3), 83 (3), 96 (2), 33 (1), 49 (1) |
| 79102 | 371 (98..477) | 22 | 12 | 108 (14), 96 (4), 45 (2), 76 (1), 83 (1) |
| 79103 | 380 (99..481) | 15 | 10 | 96 (5), 45 (3), 83 (3), 24 (2), 33 (1), 49 (1) |
| 79105 | 379 (101..484) | 4 | 3 | 33 (2), 24 (1), 83 (1) |
| 79108 | 385 (104..492) | 12 | 10 | 33 (3), 24 (2), 76 (2), 83 (2), 45 (1), 85 (1), 96 (1) |
| 79110 | 388 (106..497) | 13 | 6 | 96 (7), 33 (4), 24 (1), 85 (1) |
| 79111 | 386 (109..500) | 9 | 4 | 96 (5), 33 (2), 24 (1), 45 (1) |
| 79115 | 421 (111..531) | 8 | 7 | 33 (4), 24 (1), 93 (1), 37 (1), 123 (1) |
| 79116 | 411 (114..530) | 37 | 8 | 123 (36), 37 (1) |
| 79122 | 404 (118..532) | 18 | 9 | 93 (9), 123 (8), 37 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 37 (56), 24 (3), 33 (3), 26 (1), 76 (1) |
| 79128 | 402 (124..527) | 14 | 11 | 33 (5), 37 (4), 24 (3), 85 (1), 93 (1) |
| 79134 | 407 (127..533) | 15 | 13 | 26 (3), 33 (3), 24 (2), 37 (2), 65 (2), 76 (1), 93 (1), 107 (1) |
| 79135 | 409 (129..542) | 35 | 29 | 96 (9), 33 (6), 26 (5), 37 (5), 65 (4), 24 (3), 85 (1), 93 (1), 95 (1) |
| 79139 | 406 (132..537) | 16 | 11 | 65 (7), 33 (5), 26 (1), 37 (1), 93 (1), 96 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 107 (1), 96 (1), 123 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 35 | 202..209 | 8 | 0 | 6 |
| 41 | 219..222 | 4 | 0 | 3 |
| 44 | 227..233 | 7 | 0 | 7 |
| 46 | 236..412 | 177 | 0 | 164 |
| 47 | 242..412 | 171 | 0 | 150 |
| 51 | 252..258 | 7 | 0 | 7 |
| 56 | 271..387 | 117 | 0 | 109 |
| 62 | 277..290 | 14 | 0 | 13 |
| 66 | 281..284 | 4 | 0 | 3 |
| 69 | 286..297 | 12 | 0 | 12 |
| 72 | 292..471 | 180 | 0 | 161 |
| 73 | 300..338 | 39 | 0 | 25 |
| 75 | 302..311 | 10 | 0 | 8 |
| 79 | 327..335 | 9 | 0 | 9 |
| 82 | 332..332 | 1 | 0 | 1 |
| 84 | 338..338 | 1 | 0 | 1 |
| 87 | 343..346 | 4 | 0 | 3 |
| 89 | 345..614 | 270 | 0 | 229 |
| 90 | 346..347 | 2 | 0 | 2 |
| 91 | 352..360 | 9 | 0 | 8 |
| 98 | 377..384 | 8 | 0 | 8 |
| 101 | 394..421 | 28 | 0 | 26 |
| 104 | 405..408 | 4 | 0 | 3 |
| 110 | 427..433 | 7 | 0 | 7 |
| 118 | 453..456 | 4 | 0 | 3 |
| 121 | 467..470 | 4 | 0 | 3 |
| 128 | 477..483 | 7 | 0 | 7 |
| 131 | 486..605 | 120 | 0 | 107 |
| 137 | 502..508 | 7 | 0 | 7 |
| 143 | 525..565 | 41 | 0 | 38 |
| 145 | 529..532 | 4 | 0 | 3 |
| 147 | 531..535 | 5 | 0 | 4 |
| 148 | 532..537 | 6 | 0 | 3 |
| 149 | 532..546 | 15 | 0 | 10 |
| 154 | 552..561 | 10 | 0 | 8 |
| 155 | 560..585 | 26 | 0 | 26 |
| 159 | 580..607 | 28 | 0 | 23 |
| 163 | 591..594 | 4 | 0 | 3 |
| 164 | 595..596 | 2 | 0 | 2 |
| 167 | 602..610 | 9 | 0 | 8 |
| ... | 22 more | | | |

### Gaps and durations of candidate tracks
- tracks: 84; lifespan min/median/max: 1/9/975; tracks with internal gaps: 18; total internal gaps: 128; longest internal gap: 195; tracks ending in coasting: 73 (trailing rows total 1428)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..7 | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 78911 |
| 5 | 34..1008 | 975 | 973 | 968 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..283 | 202 | 194 | 76 | 118 | 24 | 53 | 5 | 78896, 78969, 78971, 79037, 79045 |
| 24 | 169..229 | 61 | 49 | 45 | 4 | 4 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135 |
| 26 | 176..193 | 18 | 17 | 10 | 7 | 5 | 2 | 1 | 79132, 79134, 79135, 79139 |
| 33 | 196..246 | 51 | 46 | 39 | 7 | 5 | 2 | 0 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 35 | 202..209 | 8 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 36 | 205..216 | 12 | 12 | 12 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 37 | 206..514 | 309 | 298 | 71 | 227 | 8 | 195 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 41 | 219..222 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 44 | 227..233 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 45 | 231..249 | 19 | 16 | 16 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79102, 79103, 79108, 79111 |
| 46 | 236..412 | 177 | 164 | 0 | 164 | 0 | 0 | 164 | - |
| 47 | 242..412 | 171 | 150 | 0 | 150 | 0 | 0 | 150 | - |
| 49 | 245..321 | 77 | 67 | 43 | 24 | 6 | 4 | 14 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 51 | 252..258 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 56 | 271..387 | 117 | 109 | 0 | 109 | 0 | 0 | 109 | - |
| 60 | 276..292 | 17 | 13 | 1 | 12 | 1 | 11 | 1 | 78896 |
| 62 | 277..290 | 14 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 65 | 280..453 | 174 | 157 | 13 | 144 | 2 | 138 | 3 | 79134, 79135, 79139 |
| 66 | 281..284 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 69 | 286..297 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 72 | 292..471 | 180 | 161 | 0 | 161 | 0 | 0 | 161 | - |
| 73 | 300..338 | 39 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 75 | 302..311 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 76 | 303..378 | 76 | 56 | 36 | 20 | 9 | 5 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79108, 79132, 79134 |
| 79 | 327..335 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 82 | 332..332 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 83 | 335..466 | 132 | 106 | 50 | 56 | 13 | 15 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 84 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 85 | 342..351 | 10 | 8 | 4 | 4 | 3 | 2 | 0 | 79108, 79110, 79128, 79135 |
| 87 | 343..346 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 89 | 345..614 | 270 | 229 | 0 | 229 | 0 | 0 | 229 | - |
| 90 | 346..347 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 91 | 352..360 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 93 | 366..438 | 73 | 60 | 14 | 46 | 9 | 17 | 7 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 95 | 370..493 | 124 | 105 | 1 | 104 | 1 | 89 | 15 | 79135 |
| 96 | 373..551 | 179 | 146 | 75 | 71 | 22 | 13 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 98 | 377..384 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 101 | 394..421 | 28 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 104 | 405..408 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 105 | 407..407 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 78969 |
| 107 | 412..486 | 75 | 55 | 2 | 53 | 2 | 50 | 0 | 79134, 79136 |
| 108 | 422..458 | 37 | 32 | 26 | 6 | 4 | 2 | 1 | 79097, 79098, 79102 |
| 110 | 427..433 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 118 | 453..456 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 121 | 467..470 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 123 | 470..539 | 70 | 63 | 46 | 17 | 6 | 5 | 4 | 79115, 79116, 79122, 79136 |
| 128 | 477..483 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 131 | 486..605 | 120 | 107 | 0 | 107 | 0 | 0 | 107 | - |
| 137 | 502..508 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 143 | 525..565 | 41 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 145 | 529..532 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 147 | 531..535 | 5 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 148 | 532..537 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 149 | 532..546 | 15 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 154 | 552..561 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 155 | 560..585 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 159 | 580..607 | 28 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 163 | 591..594 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 164 | 595..596 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 167 | 602..610 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 169 | 627..634 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 171 | 653..656 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 173 | 659..665 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 175 | 677..685 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 176 | 703..708 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 177 | 715..718 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 181 | 727..733 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 183 | 752..758 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 184 | 777..782 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 191 | 802..811 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 193 | 827..834 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 194 | 839..842 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 199 | 852..860 | 9 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 202 | 877..885 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 203 | 901..906 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 204 | 903..911 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 212 | 927..935 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 213 | 933..940 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| ... | 4 more in JSON | | | | | | | | |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 41; matched pairs: 1551; unmatched reference entries: 8591; unmatched candidate entries: 2021
- identity switches: 125; fragmentation (coverage interruptions): 348; orphan candidate ids (never on a reference object): 19

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f34: ref 78911: 0 -> 5 at (1812.5, 3363), 27 frames after previous cover
- f176: ref 79132: 24 -> 26 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 24 -> 26 at (1843, 3015), 10 frames after previous cover
- f181: ref 79134: 26 -> 24 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 6 -> 24 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 24 -> 6 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78971: 24 -> 6 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 79134: 24 -> 26 at (1753.5, 3017.5), 11 frames after previous cover
- f196: ref 79139: 26 -> 33 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 26 -> 33 at (1718, 3008.5), 8 frames after previous cover
- f201: ref 79132: 26 -> 24 at (1646.5, 3013), 25 frames after previous cover
- f205: ref 79097: 24 -> 36 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 78897: 24 -> 36 at (1401.5, 3004.5), 12 frames after previous cover
- f206: ref 79135: 33 -> 24 at (1673, 3006), 2 frames after previous cover
- f207: ref 79134: 26 -> 24 at (1655.5, 3014), 15 frames after previous cover
- f210: ref 78899: 24 -> 36 at (1400, 3003.5), 11 frames after previous cover
- f211: ref 79135: 24 -> 33 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 24 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f214: ref 79132: 24 -> 33 at (1561, 3005), 4 frames after previous cover
- f216: ref 79037: 6 -> 36 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 36 -> 24 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 24 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 24 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 24 -> 33 at (1465, 3003), 7 frames after previous cover
- f225: ref 78899: 36 -> 24 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 36 -> 24 at (1272, 2992), 12 frames after previous cover
- f227: ref 79105: 24 -> 33 at (1392, 2996), 13 frames after previous cover
- f228: ref 79103: 24 -> 33 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 6 -> 24 at (1202, 2988), 41 frames after previous cover
- f230: ref 79134: 24 -> 33 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79097: 24 -> 45 at (1295, 2989.5), 7 frames after previous cover
- f235: ref 78899: 24 -> 45 at (1242.5, 2989), 10 frames after previous cover
- f237: ref 79037: 36 -> 45 at (1184.5, 2988), 21 frames after previous cover
- f240: ref 79108: 33 -> 45 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 33 -> 45 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 24 -> 6 at (1119, 2986), 13 frames after previous cover
- f242: ref 79111: 33 -> 45 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 45 -> 49 at (1179, 2985.5), 10 frames after previous cover
- f246: ref 79097: 45 -> 49 at (1199.5, 2985), 7 frames after previous cover
- f255: ref 79037: 45 -> 49 at (1069.5, 2987.5), 18 frames after previous cover
- f260: ref 78897: 24 -> 49 at (1057.5, 2987.5), 34 frames after previous cover
- f271: ref 79037: 49 -> 6 at (965, 2987), 8 frames after previous cover
- f272: ref 79045: 24 -> 6 at (945.5, 2991.5), 45 frames after previous cover
- f281: ref 79098: 33 -> 49 at (1009.5, 2985), 44 frames after previous cover
- f287: ref 78896: 6 -> 60 at (775, 2987), 48 frames after previous cover
- f290: ref 79103: 45 -> 49 at (995.5, 2980.5), 42 frames after previous cover
- f304: ref 78969: 6 -> 49 at (689.5, 2980), 34 frames after previous cover
- f304: ref 79108: 45 -> 76 at (954, 2978), 64 frames after previous cover
- f317: ref 79134: 33 -> 76 at (990.5, 2965.5), 74 frames after previous cover
- f327: ref 79132: 33 -> 76 at (895, 2966.5), 88 frames after previous cover
- f331: ref 79102: 45 -> 76 at (723.5, 2979.5), 82 frames after previous cover
- f332: ref 79098: 49 -> 76 at (692, 2975.5), 51 frames after previous cover
- f333: ref 79097: 49 -> 76 at (654.5, 2972.5), 39 frames after previous cover
- f334: ref 78899: 49 -> 76 at (619, 2977.5), 39 frames after previous cover
- f335: ref 78969: 49 -> 83 at (508, 2966.5), 28 frames after previous cover
- f345: ref 79135: 33 -> 85 at (875.5, 2962), 103 frames after previous cover
- f346: ref 78897: 49 -> 76 at (523, 2971.5), 63 frames after previous cover
- f346: ref 79128: 33 -> 85 at (828, 2962), 102 frames after previous cover
- f348: ref 79110: 33 -> 85 at (701.5, 2979.5), 102 frames after previous cover
- ... 65 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 970 | 8 | 5 (968), 0 (2) |
| 78896 | 350 (76..429) | 8 | 6 | 6 (4), 96 (2), 60 (1), 83 (1) |
| 78969 | 352 (80..434) | 88 | 43 | 6 (64), 83 (12), 96 (8), 49 (3), 105 (1) |
| 78971 | 352 (84..439) | 15 | 10 | 96 (7), 6 (4), 24 (2), 76 (1), 83 (1) |
| 79045 | 355 (84..443) | 16 | 11 | 76 (5), 83 (5), 96 (3), 6 (2), 24 (1) |
| 79037 | 355 (86..445) | 15 | 14 | 83 (5), 6 (2), 49 (2), 96 (2), 24 (1), 36 (1), 45 (1), 76 (1) |
| 78897 | 345 (89..450) | 26 | 20 | 96 (9), 83 (5), 24 (4), 49 (3), 76 (3), 36 (2) |
| 78899 | 365 (91..455) | 45 | 36 | 49 (15), 24 (8), 83 (7), 76 (6), 96 (5), 36 (3), 45 (1) |
| 79097 | 366 (94..461) | 62 | 39 | 49 (18), 76 (12), 24 (10), 45 (7), 36 (6), 96 (4), 83 (4), 108 (1) |
| 79098 | 360 (97..467) | 21 | 17 | 108 (11), 76 (3), 83 (3), 96 (2), 33 (1), 49 (1) |
| 79102 | 371 (98..477) | 22 | 12 | 108 (14), 96 (4), 45 (2), 76 (1), 83 (1) |
| 79103 | 380 (99..481) | 15 | 10 | 96 (5), 45 (3), 83 (3), 24 (2), 33 (1), 49 (1) |
| 79105 | 379 (101..484) | 4 | 3 | 33 (2), 24 (1), 83 (1) |
| 79108 | 385 (104..492) | 12 | 10 | 33 (3), 24 (2), 76 (2), 83 (2), 45 (1), 85 (1), 96 (1) |
| 79110 | 388 (106..497) | 13 | 6 | 96 (7), 33 (4), 24 (1), 85 (1) |
| 79111 | 386 (109..500) | 9 | 4 | 96 (5), 33 (2), 24 (1), 45 (1) |
| 79115 | 421 (111..531) | 8 | 7 | 33 (4), 24 (1), 93 (1), 37 (1), 123 (1) |
| 79116 | 411 (114..530) | 37 | 8 | 123 (36), 37 (1) |
| 79122 | 404 (118..532) | 18 | 9 | 93 (9), 123 (8), 37 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 37 (56), 24 (3), 33 (3), 26 (1), 76 (1) |
| 79128 | 402 (124..527) | 14 | 11 | 33 (5), 37 (4), 24 (3), 85 (1), 93 (1) |
| 79134 | 407 (127..533) | 15 | 13 | 26 (3), 33 (3), 24 (2), 37 (2), 65 (2), 76 (1), 93 (1), 107 (1) |
| 79135 | 409 (129..542) | 35 | 29 | 96 (9), 33 (6), 26 (5), 37 (5), 65 (4), 24 (3), 85 (1), 93 (1), 95 (1) |
| 79139 | 406 (132..537) | 16 | 11 | 65 (7), 33 (5), 26 (1), 37 (1), 93 (1), 96 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 107 (1), 96 (1), 123 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 46 | 236..412 | 177 | 0 | 164 |
| 47 | 242..412 | 171 | 0 | 150 |
| 56 | 271..387 | 117 | 0 | 109 |
| 69 | 286..297 | 12 | 0 | 12 |
| 72 | 292..471 | 180 | 0 | 161 |
| 73 | 300..338 | 39 | 0 | 25 |
| 82 | 332..332 | 1 | 0 | 1 |
| 84 | 338..338 | 1 | 0 | 1 |
| 89 | 345..614 | 270 | 0 | 229 |
| 90 | 346..347 | 2 | 0 | 2 |
| 101 | 394..421 | 28 | 0 | 26 |
| 131 | 486..605 | 120 | 0 | 107 |
| 143 | 525..565 | 41 | 0 | 38 |
| 148 | 532..537 | 6 | 0 | 3 |
| 149 | 532..546 | 15 | 0 | 10 |
| 155 | 560..585 | 26 | 0 | 26 |
| 159 | 580..607 | 28 | 0 | 23 |
| 164 | 595..596 | 2 | 0 | 2 |
| 173 | 659..665 | 7 | 0 | 7 |

### Gaps and durations of candidate tracks
- tracks: 41; lifespan min/median/max: 1/41/975; tracks with internal gaps: 18; total internal gaps: 128; longest internal gap: 195; tracks ending in coasting: 30 (trailing rows total 1162)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..7 | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 78911 |
| 5 | 34..1008 | 975 | 973 | 968 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..283 | 202 | 194 | 76 | 118 | 24 | 53 | 5 | 78896, 78969, 78971, 79037, 79045 |
| 24 | 169..229 | 61 | 49 | 45 | 4 | 4 | 1 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135 |
| 26 | 176..193 | 18 | 17 | 10 | 7 | 5 | 2 | 1 | 79132, 79134, 79135, 79139 |
| 33 | 196..246 | 51 | 46 | 39 | 7 | 5 | 2 | 0 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 36 | 205..216 | 12 | 12 | 12 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 37 | 206..514 | 309 | 298 | 71 | 227 | 8 | 195 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 45 | 231..249 | 19 | 16 | 16 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79102, 79103, 79108, 79111 |
| 46 | 236..412 | 177 | 164 | 0 | 164 | 0 | 0 | 164 | - |
| 47 | 242..412 | 171 | 150 | 0 | 150 | 0 | 0 | 150 | - |
| 49 | 245..321 | 77 | 67 | 43 | 24 | 6 | 4 | 14 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 56 | 271..387 | 117 | 109 | 0 | 109 | 0 | 0 | 109 | - |
| 60 | 276..292 | 17 | 13 | 1 | 12 | 1 | 11 | 1 | 78896 |
| 65 | 280..453 | 174 | 157 | 13 | 144 | 2 | 138 | 3 | 79134, 79135, 79139 |
| 69 | 286..297 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 72 | 292..471 | 180 | 161 | 0 | 161 | 0 | 0 | 161 | - |
| 73 | 300..338 | 39 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 76 | 303..378 | 76 | 56 | 36 | 20 | 9 | 5 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79108, 79132, 79134 |
| 82 | 332..332 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 83 | 335..466 | 132 | 106 | 50 | 56 | 13 | 15 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 84 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 85 | 342..351 | 10 | 8 | 4 | 4 | 3 | 2 | 0 | 79108, 79110, 79128, 79135 |
| 89 | 345..614 | 270 | 229 | 0 | 229 | 0 | 0 | 229 | - |
| 90 | 346..347 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 93 | 366..438 | 73 | 60 | 14 | 46 | 9 | 17 | 7 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 95 | 370..493 | 124 | 105 | 1 | 104 | 1 | 89 | 15 | 79135 |
| 96 | 373..551 | 179 | 146 | 75 | 71 | 22 | 13 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 101 | 394..421 | 28 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 105 | 407..407 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 78969 |
| 107 | 412..486 | 75 | 55 | 2 | 53 | 2 | 50 | 0 | 79134, 79136 |
| 108 | 422..458 | 37 | 32 | 26 | 6 | 4 | 2 | 1 | 79097, 79098, 79102 |
| 123 | 470..539 | 70 | 63 | 46 | 17 | 6 | 5 | 4 | 79115, 79116, 79122, 79136 |
| 131 | 486..605 | 120 | 107 | 0 | 107 | 0 | 0 | 107 | - |
| 143 | 525..565 | 41 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 148 | 532..537 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 149 | 532..546 | 15 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 155 | 560..585 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 159 | 580..607 | 28 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 164 | 595..596 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 173 | 659..665 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 84; matched pairs: 1662; unmatched reference entries: 8480; unmatched candidate entries: 2900
- identity switches: 137; fragmentation (coverage interruptions): 356; orphan candidate ids (never on a reference object): 62

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f34: ref 78911: 0 -> 5 at (1812.5, 3363), 26 frames after previous cover
- f176: ref 79132: 24 -> 26 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 24 -> 26 at (1843, 3015), 9 frames after previous cover
- f181: ref 79134: 26 -> 24 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 6 -> 24 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 24 -> 6 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 6 -> 24 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 24 -> 6 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 78969: 24 -> 6 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 79134: 24 -> 26 at (1753.5, 3017.5), 11 frames after previous cover
- f195: ref 79128: 24 -> 26 at (1712.5, 3015), 23 frames after previous cover
- f196: ref 79139: 26 -> 33 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 26 -> 33 at (1718, 3008.5), 8 frames after previous cover
- f201: ref 79132: 26 -> 24 at (1646.5, 3013), 25 frames after previous cover
- f204: ref 79128: 26 -> 24 at (1651, 3011.5), 8 frames after previous cover
- f205: ref 79097: 24 -> 36 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 78897: 24 -> 36 at (1401.5, 3004.5), 12 frames after previous cover
- f206: ref 79135: 33 -> 24 at (1673, 3006), 2 frames after previous cover
- f206: ref 79136: 26 -> 33 at (1718.5, 3013), 24 frames after previous cover
- f207: ref 79134: 26 -> 24 at (1655.5, 3014), 15 frames after previous cover
- f210: ref 78899: 24 -> 36 at (1400, 3003.5), 11 frames after previous cover
- f211: ref 79135: 24 -> 33 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 24 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f214: ref 79132: 24 -> 33 at (1561, 3005), 4 frames after previous cover
- f216: ref 79037: 6 -> 36 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 36 -> 24 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 24 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 24 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 24 -> 33 at (1465, 3003), 7 frames after previous cover
- f225: ref 78899: 36 -> 24 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 36 -> 24 at (1272, 2992), 7 frames after previous cover
- f227: ref 79105: 24 -> 33 at (1392, 2996), 13 frames after previous cover
- f228: ref 79103: 24 -> 33 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 6 -> 24 at (1202, 2988), 41 frames after previous cover
- f230: ref 79134: 24 -> 33 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79097: 24 -> 45 at (1295, 2989.5), 7 frames after previous cover
- f235: ref 78899: 24 -> 45 at (1242.5, 2989), 10 frames after previous cover
- f237: ref 79037: 36 -> 45 at (1184.5, 2988), 21 frames after previous cover
- f240: ref 79108: 33 -> 45 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 33 -> 45 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 24 -> 6 at (1119, 2986), 12 frames after previous cover
- f242: ref 79111: 33 -> 45 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 45 -> 49 at (1179, 2985.5), 10 frames after previous cover
- f246: ref 79097: 45 -> 49 at (1199.5, 2985), 7 frames after previous cover
- f247: ref 79111: 45 -> 33 at (1328.5, 2993.5), 5 frames after previous cover
- f253: ref 79105: 33 -> 45 at (1236, 2985.5), 17 frames after previous cover
- f255: ref 79037: 45 -> 49 at (1069.5, 2987.5), 18 frames after previous cover
- f260: ref 78897: 24 -> 49 at (1057.5, 2987.5), 34 frames after previous cover
- f271: ref 79037: 49 -> 6 at (965, 2987), 8 frames after previous cover
- f272: ref 79045: 24 -> 6 at (945.5, 2991.5), 39 frames after previous cover
- f281: ref 79098: 33 -> 49 at (1009.5, 2985), 44 frames after previous cover
- f287: ref 78896: 6 -> 60 at (775, 2987), 48 frames after previous cover
- f290: ref 78969: 6 -> 60 at (780, 2986.5), 20 frames after previous cover
- f290: ref 79103: 45 -> 49 at (995.5, 2980.5), 38 frames after previous cover
- f304: ref 78969: 60 -> 49 at (689.5, 2980), 13 frames after previous cover
- f304: ref 79108: 45 -> 76 at (954, 2978), 64 frames after previous cover
- f317: ref 79134: 33 -> 76 at (990.5, 2965.5), 74 frames after previous cover
- f326: ref 79115: 33 -> 76 at (867.5, 2979.5), 76 frames after previous cover
- f327: ref 79132: 33 -> 76 at (895, 2966.5), 88 frames after previous cover
- ... 77 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 6 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 9 | 6 | 6 (4), 60 (2), 96 (2), 83 (1) |
| 78969 | 352 (80..434) | 101 | 44 | 6 (65), 96 (13), 83 (12), 105 (4), 49 (3), 24 (2), 60 (2) |
| 78971 | 352 (84..439) | 19 | 11 | 96 (8), 6 (5), 24 (3), 83 (2), 76 (1) |
| 79045 | 355 (84..443) | 25 | 10 | 76 (8), 83 (6), 24 (5), 96 (4), 6 (2) |
| 79037 | 355 (86..445) | 19 | 15 | 83 (6), 76 (4), 6 (2), 49 (2), 96 (2), 24 (1), 36 (1), 45 (1) |
| 78897 | 345 (89..450) | 34 | 21 | 96 (11), 83 (7), 76 (5), 24 (4), 36 (4), 49 (3) |
| 78899 | 365 (91..455) | 51 | 35 | 49 (17), 83 (10), 24 (8), 76 (6), 96 (6), 36 (3), 45 (1) |
| 79097 | 366 (94..461) | 65 | 38 | 49 (18), 76 (13), 24 (10), 45 (7), 36 (6), 96 (5), 83 (5), 108 (1) |
| 79098 | 360 (97..467) | 27 | 17 | 108 (14), 83 (4), 96 (4), 76 (3), 33 (1), 49 (1) |
| 79102 | 371 (98..477) | 24 | 11 | 108 (15), 96 (4), 45 (3), 76 (1), 83 (1) |
| 79103 | 380 (99..481) | 22 | 10 | 45 (8), 83 (5), 96 (5), 24 (2), 33 (1), 49 (1) |
| 79105 | 379 (101..484) | 6 | 4 | 33 (3), 24 (1), 45 (1), 83 (1) |
| 79108 | 385 (104..492) | 15 | 10 | 24 (3), 33 (3), 85 (3), 76 (2), 83 (2), 45 (1), 96 (1) |
| 79110 | 388 (106..497) | 15 | 7 | 96 (7), 33 (4), 85 (3), 24 (1) |
| 79111 | 386 (109..500) | 12 | 5 | 96 (6), 33 (4), 24 (1), 45 (1) |
| 79115 | 421 (111..531) | 12 | 10 | 33 (6), 76 (2), 24 (1), 93 (1), 37 (1), 123 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 123 (36), 37 (2) |
| 79122 | 404 (118..532) | 22 | 11 | 123 (11), 93 (9), 24 (1), 37 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 37 (57), 24 (3), 33 (3), 26 (1), 76 (1) |
| 79128 | 402 (124..527) | 19 | 13 | 24 (5), 33 (5), 37 (4), 26 (2), 93 (2), 85 (1) |
| 79134 | 407 (127..533) | 17 | 13 | 26 (3), 33 (3), 93 (3), 24 (2), 37 (2), 65 (2), 76 (1), 107 (1) |
| 79135 | 409 (129..542) | 44 | 27 | 96 (12), 33 (6), 37 (6), 65 (6), 26 (5), 24 (4), 95 (2), 85 (1), 93 (1), 107 (1) |
| 79139 | 406 (132..537) | 19 | 10 | 65 (8), 33 (5), 37 (3), 26 (1), 93 (1), 96 (1) |
| 79136 | 393 (136..538) | 9 | 5 | 33 (3), 107 (2), 123 (2), 26 (1), 96 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 35 | 202..213 | 12 | 0 | 12 |
| 41 | 219..226 | 8 | 0 | 8 |
| 44 | 227..237 | 11 | 0 | 11 |
| 46 | 236..416 | 181 | 0 | 181 |
| 47 | 242..416 | 175 | 0 | 175 |
| 51 | 252..262 | 11 | 0 | 11 |
| 56 | 271..391 | 121 | 0 | 121 |
| 62 | 277..294 | 18 | 0 | 18 |
| 66 | 281..288 | 8 | 0 | 8 |
| 69 | 286..301 | 16 | 0 | 16 |
| 72 | 292..475 | 184 | 0 | 184 |
| 73 | 300..342 | 43 | 0 | 43 |
| 75 | 302..315 | 14 | 0 | 14 |
| 79 | 327..339 | 13 | 0 | 13 |
| 82 | 332..336 | 5 | 0 | 5 |
| 84 | 338..342 | 5 | 0 | 5 |
| 87 | 343..350 | 8 | 0 | 8 |
| 89 | 345..618 | 274 | 0 | 274 |
| 90 | 346..351 | 6 | 0 | 6 |
| 91 | 352..364 | 13 | 0 | 13 |
| 98 | 377..388 | 12 | 0 | 12 |
| 101 | 394..425 | 32 | 0 | 32 |
| 104 | 405..412 | 8 | 0 | 8 |
| 110 | 427..437 | 11 | 0 | 11 |
| 118 | 453..460 | 8 | 0 | 8 |
| 121 | 467..474 | 8 | 0 | 8 |
| 128 | 477..487 | 11 | 0 | 11 |
| 131 | 486..609 | 124 | 0 | 124 |
| 137 | 502..512 | 11 | 0 | 11 |
| 143 | 525..569 | 45 | 0 | 45 |
| 145 | 529..536 | 8 | 0 | 8 |
| 147 | 531..539 | 9 | 0 | 9 |
| 148 | 532..541 | 10 | 0 | 10 |
| 149 | 532..550 | 19 | 0 | 19 |
| 154 | 552..565 | 14 | 0 | 14 |
| 155 | 560..589 | 30 | 0 | 30 |
| 159 | 580..611 | 32 | 0 | 32 |
| 163 | 591..598 | 8 | 0 | 8 |
| 164 | 595..600 | 6 | 0 | 6 |
| 167 | 602..614 | 13 | 0 | 13 |
| ... | 22 more | | | |

### Gaps and durations of candidate tracks
- tracks: 84; lifespan min/median/max: 5/13/975; tracks with internal gaps: 20; total internal gaps: 163; longest internal gap: 197; tracks ending in coasting: 76 (trailing rows total 1907)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..11 | 8 | 8 | 3 | 5 | 1 | 2 | 3 | 78911 |
| 5 | 34..1008 | 975 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..287 | 206 | 206 | 78 | 128 | 25 | 53 | 14 | 78896, 78969, 78971, 79037, 79045 |
| 24 | 169..233 | 65 | 65 | 57 | 8 | 6 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135 |
| 26 | 176..197 | 22 | 22 | 13 | 9 | 7 | 2 | 1 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 33 | 196..250 | 55 | 55 | 47 | 8 | 6 | 2 | 0 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 35 | 202..213 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 36 | 205..220 | 16 | 16 | 14 | 2 | 1 | 1 | 1 | 78897, 78899, 79037, 79097 |
| 37 | 206..518 | 313 | 313 | 76 | 237 | 10 | 197 | 3 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 41 | 219..226 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 44 | 227..237 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 45 | 231..253 | 23 | 23 | 23 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79102, 79103, 79105, 79108, 79111 |
| 46 | 236..416 | 181 | 181 | 0 | 181 | 0 | 0 | 181 | - |
| 47 | 242..416 | 175 | 175 | 0 | 175 | 0 | 0 | 175 | - |
| 49 | 245..325 | 81 | 81 | 45 | 36 | 10 | 8 | 18 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 51 | 252..262 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 56 | 271..391 | 121 | 121 | 0 | 121 | 0 | 0 | 121 | - |
| 60 | 276..296 | 21 | 21 | 4 | 17 | 2 | 11 | 5 | 78896, 78969 |
| 62 | 277..294 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 65 | 280..457 | 178 | 178 | 16 | 162 | 3 | 148 | 7 | 79134, 79135, 79139 |
| 66 | 281..288 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 69 | 286..301 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 72 | 292..475 | 184 | 184 | 0 | 184 | 0 | 0 | 184 | - |
| 73 | 300..342 | 43 | 43 | 0 | 43 | 0 | 0 | 43 | - |
| 75 | 302..315 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 76 | 303..382 | 80 | 80 | 47 | 33 | 11 | 11 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79108, 79115, 79132, 79134 |
| 79 | 327..339 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 82 | 332..336 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 83 | 335..470 | 136 | 136 | 62 | 74 | 20 | 16 | 9 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 84 | 338..342 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 85 | 342..355 | 14 | 14 | 8 | 6 | 3 | 3 | 0 | 79108, 79110, 79128, 79135 |
| 87 | 343..350 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 89 | 345..618 | 274 | 274 | 0 | 274 | 0 | 0 | 274 | - |
| 90 | 346..351 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 91 | 352..364 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 93 | 366..442 | 77 | 77 | 17 | 60 | 9 | 20 | 17 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 95 | 370..497 | 128 | 128 | 2 | 126 | 1 | 106 | 20 | 79135 |
| 96 | 373..555 | 183 | 183 | 92 | 91 | 28 | 17 | 16 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 98 | 377..388 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 101 | 394..425 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 104 | 405..412 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 105 | 407..411 | 5 | 5 | 4 | 1 | 0 | 0 | 1 | 78969 |
| 107 | 412..490 | 79 | 79 | 4 | 75 | 3 | 69 | 0 | 79134, 79135, 79136 |
| 108 | 422..462 | 41 | 41 | 30 | 11 | 6 | 5 | 0 | 79097, 79098, 79102 |
| 110 | 427..437 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 118 | 453..460 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 121 | 467..474 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 123 | 470..543 | 74 | 74 | 50 | 24 | 7 | 5 | 10 | 79115, 79116, 79122, 79136 |
| 128 | 477..487 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 131 | 486..609 | 124 | 124 | 0 | 124 | 0 | 0 | 124 | - |
| 137 | 502..512 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 143 | 525..569 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 145 | 529..536 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 147 | 531..539 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 148 | 532..541 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 149 | 532..550 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 154 | 552..565 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 155 | 560..589 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 159 | 580..611 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 163 | 591..598 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 164 | 595..600 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 167 | 602..614 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 169 | 627..638 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 171 | 653..660 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 173 | 659..669 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 175 | 677..689 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 176 | 703..712 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 177 | 715..722 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 181 | 727..737 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 183 | 752..762 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 184 | 777..786 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 191 | 802..815 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 193 | 827..838 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 194 | 839..846 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 199 | 852..864 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 202 | 877..889 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 203 | 901..910 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 204 | 903..915 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 212 | 927..939 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 213 | 933..944 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| ... | 4 more in JSON | | | | | | | | |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 41; matched pairs: 1662; unmatched reference entries: 8480; unmatched candidate entries: 2437
- identity switches: 137; fragmentation (coverage interruptions): 356; orphan candidate ids (never on a reference object): 19

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f34: ref 78911: 0 -> 5 at (1812.5, 3363), 26 frames after previous cover
- f176: ref 79132: 24 -> 26 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 24 -> 26 at (1843, 3015), 9 frames after previous cover
- f181: ref 79134: 26 -> 24 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 6 -> 24 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 24 -> 6 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 6 -> 24 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 24 -> 6 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 78969: 24 -> 6 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 79134: 24 -> 26 at (1753.5, 3017.5), 11 frames after previous cover
- f195: ref 79128: 24 -> 26 at (1712.5, 3015), 23 frames after previous cover
- f196: ref 79139: 26 -> 33 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 26 -> 33 at (1718, 3008.5), 8 frames after previous cover
- f201: ref 79132: 26 -> 24 at (1646.5, 3013), 25 frames after previous cover
- f204: ref 79128: 26 -> 24 at (1651, 3011.5), 8 frames after previous cover
- f205: ref 79097: 24 -> 36 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 78897: 24 -> 36 at (1401.5, 3004.5), 12 frames after previous cover
- f206: ref 79135: 33 -> 24 at (1673, 3006), 2 frames after previous cover
- f206: ref 79136: 26 -> 33 at (1718.5, 3013), 24 frames after previous cover
- f207: ref 79134: 26 -> 24 at (1655.5, 3014), 15 frames after previous cover
- f210: ref 78899: 24 -> 36 at (1400, 3003.5), 11 frames after previous cover
- f211: ref 79135: 24 -> 33 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 24 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f214: ref 79132: 24 -> 33 at (1561, 3005), 4 frames after previous cover
- f216: ref 79037: 6 -> 36 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 36 -> 24 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 24 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 24 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 24 -> 33 at (1465, 3003), 7 frames after previous cover
- f225: ref 78899: 36 -> 24 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 36 -> 24 at (1272, 2992), 7 frames after previous cover
- f227: ref 79105: 24 -> 33 at (1392, 2996), 13 frames after previous cover
- f228: ref 79103: 24 -> 33 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 6 -> 24 at (1202, 2988), 41 frames after previous cover
- f230: ref 79134: 24 -> 33 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79097: 24 -> 45 at (1295, 2989.5), 7 frames after previous cover
- f235: ref 78899: 24 -> 45 at (1242.5, 2989), 10 frames after previous cover
- f237: ref 79037: 36 -> 45 at (1184.5, 2988), 21 frames after previous cover
- f240: ref 79108: 33 -> 45 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 33 -> 45 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 24 -> 6 at (1119, 2986), 12 frames after previous cover
- f242: ref 79111: 33 -> 45 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 45 -> 49 at (1179, 2985.5), 10 frames after previous cover
- f246: ref 79097: 45 -> 49 at (1199.5, 2985), 7 frames after previous cover
- f247: ref 79111: 45 -> 33 at (1328.5, 2993.5), 5 frames after previous cover
- f253: ref 79105: 33 -> 45 at (1236, 2985.5), 17 frames after previous cover
- f255: ref 79037: 45 -> 49 at (1069.5, 2987.5), 18 frames after previous cover
- f260: ref 78897: 24 -> 49 at (1057.5, 2987.5), 34 frames after previous cover
- f271: ref 79037: 49 -> 6 at (965, 2987), 8 frames after previous cover
- f272: ref 79045: 24 -> 6 at (945.5, 2991.5), 39 frames after previous cover
- f281: ref 79098: 33 -> 49 at (1009.5, 2985), 44 frames after previous cover
- f287: ref 78896: 6 -> 60 at (775, 2987), 48 frames after previous cover
- f290: ref 78969: 6 -> 60 at (780, 2986.5), 20 frames after previous cover
- f290: ref 79103: 45 -> 49 at (995.5, 2980.5), 38 frames after previous cover
- f304: ref 78969: 60 -> 49 at (689.5, 2980), 13 frames after previous cover
- f304: ref 79108: 45 -> 76 at (954, 2978), 64 frames after previous cover
- f317: ref 79134: 33 -> 76 at (990.5, 2965.5), 74 frames after previous cover
- f326: ref 79115: 33 -> 76 at (867.5, 2979.5), 76 frames after previous cover
- f327: ref 79132: 33 -> 76 at (895, 2966.5), 88 frames after previous cover
- ... 77 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 6 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 9 | 6 | 6 (4), 60 (2), 96 (2), 83 (1) |
| 78969 | 352 (80..434) | 101 | 44 | 6 (65), 96 (13), 83 (12), 105 (4), 49 (3), 24 (2), 60 (2) |
| 78971 | 352 (84..439) | 19 | 11 | 96 (8), 6 (5), 24 (3), 83 (2), 76 (1) |
| 79045 | 355 (84..443) | 25 | 10 | 76 (8), 83 (6), 24 (5), 96 (4), 6 (2) |
| 79037 | 355 (86..445) | 19 | 15 | 83 (6), 76 (4), 6 (2), 49 (2), 96 (2), 24 (1), 36 (1), 45 (1) |
| 78897 | 345 (89..450) | 34 | 21 | 96 (11), 83 (7), 76 (5), 24 (4), 36 (4), 49 (3) |
| 78899 | 365 (91..455) | 51 | 35 | 49 (17), 83 (10), 24 (8), 76 (6), 96 (6), 36 (3), 45 (1) |
| 79097 | 366 (94..461) | 65 | 38 | 49 (18), 76 (13), 24 (10), 45 (7), 36 (6), 96 (5), 83 (5), 108 (1) |
| 79098 | 360 (97..467) | 27 | 17 | 108 (14), 83 (4), 96 (4), 76 (3), 33 (1), 49 (1) |
| 79102 | 371 (98..477) | 24 | 11 | 108 (15), 96 (4), 45 (3), 76 (1), 83 (1) |
| 79103 | 380 (99..481) | 22 | 10 | 45 (8), 83 (5), 96 (5), 24 (2), 33 (1), 49 (1) |
| 79105 | 379 (101..484) | 6 | 4 | 33 (3), 24 (1), 45 (1), 83 (1) |
| 79108 | 385 (104..492) | 15 | 10 | 24 (3), 33 (3), 85 (3), 76 (2), 83 (2), 45 (1), 96 (1) |
| 79110 | 388 (106..497) | 15 | 7 | 96 (7), 33 (4), 85 (3), 24 (1) |
| 79111 | 386 (109..500) | 12 | 5 | 96 (6), 33 (4), 24 (1), 45 (1) |
| 79115 | 421 (111..531) | 12 | 10 | 33 (6), 76 (2), 24 (1), 93 (1), 37 (1), 123 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 123 (36), 37 (2) |
| 79122 | 404 (118..532) | 22 | 11 | 123 (11), 93 (9), 24 (1), 37 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 37 (57), 24 (3), 33 (3), 26 (1), 76 (1) |
| 79128 | 402 (124..527) | 19 | 13 | 24 (5), 33 (5), 37 (4), 26 (2), 93 (2), 85 (1) |
| 79134 | 407 (127..533) | 17 | 13 | 26 (3), 33 (3), 93 (3), 24 (2), 37 (2), 65 (2), 76 (1), 107 (1) |
| 79135 | 409 (129..542) | 44 | 27 | 96 (12), 33 (6), 37 (6), 65 (6), 26 (5), 24 (4), 95 (2), 85 (1), 93 (1), 107 (1) |
| 79139 | 406 (132..537) | 19 | 10 | 65 (8), 33 (5), 37 (3), 26 (1), 93 (1), 96 (1) |
| 79136 | 393 (136..538) | 9 | 5 | 33 (3), 107 (2), 123 (2), 26 (1), 96 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 46 | 236..416 | 181 | 0 | 181 |
| 47 | 242..416 | 175 | 0 | 175 |
| 56 | 271..391 | 121 | 0 | 121 |
| 69 | 286..301 | 16 | 0 | 16 |
| 72 | 292..475 | 184 | 0 | 184 |
| 73 | 300..342 | 43 | 0 | 43 |
| 82 | 332..336 | 5 | 0 | 5 |
| 84 | 338..342 | 5 | 0 | 5 |
| 89 | 345..618 | 274 | 0 | 274 |
| 90 | 346..351 | 6 | 0 | 6 |
| 101 | 394..425 | 32 | 0 | 32 |
| 131 | 486..609 | 124 | 0 | 124 |
| 143 | 525..569 | 45 | 0 | 45 |
| 148 | 532..541 | 10 | 0 | 10 |
| 149 | 532..550 | 19 | 0 | 19 |
| 155 | 560..589 | 30 | 0 | 30 |
| 159 | 580..611 | 32 | 0 | 32 |
| 164 | 595..600 | 6 | 0 | 6 |
| 173 | 659..669 | 11 | 0 | 11 |

### Gaps and durations of candidate tracks
- tracks: 41; lifespan min/median/max: 5/45/975; tracks with internal gaps: 20; total internal gaps: 163; longest internal gap: 197; tracks ending in coasting: 33 (trailing rows total 1444)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..11 | 8 | 8 | 3 | 5 | 1 | 2 | 3 | 78911 |
| 5 | 34..1008 | 975 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..287 | 206 | 206 | 78 | 128 | 25 | 53 | 14 | 78896, 78969, 78971, 79037, 79045 |
| 24 | 169..233 | 65 | 65 | 57 | 8 | 6 | 2 | 0 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135 |
| 26 | 176..197 | 22 | 22 | 13 | 9 | 7 | 2 | 1 | 79128, 79132, 79134, 79135, 79136, 79139 |
| 33 | 196..250 | 55 | 55 | 47 | 8 | 6 | 2 | 0 | 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 36 | 205..220 | 16 | 16 | 14 | 2 | 1 | 1 | 1 | 78897, 78899, 79037, 79097 |
| 37 | 206..518 | 313 | 313 | 76 | 237 | 10 | 197 | 3 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 45 | 231..253 | 23 | 23 | 23 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79102, 79103, 79105, 79108, 79111 |
| 46 | 236..416 | 181 | 181 | 0 | 181 | 0 | 0 | 181 | - |
| 47 | 242..416 | 175 | 175 | 0 | 175 | 0 | 0 | 175 | - |
| 49 | 245..325 | 81 | 81 | 45 | 36 | 10 | 8 | 18 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 56 | 271..391 | 121 | 121 | 0 | 121 | 0 | 0 | 121 | - |
| 60 | 276..296 | 21 | 21 | 4 | 17 | 2 | 11 | 5 | 78896, 78969 |
| 65 | 280..457 | 178 | 178 | 16 | 162 | 3 | 148 | 7 | 79134, 79135, 79139 |
| 69 | 286..301 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 72 | 292..475 | 184 | 184 | 0 | 184 | 0 | 0 | 184 | - |
| 73 | 300..342 | 43 | 43 | 0 | 43 | 0 | 0 | 43 | - |
| 76 | 303..382 | 80 | 80 | 47 | 33 | 11 | 11 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79108, 79115, 79132, 79134 |
| 82 | 332..336 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 83 | 335..470 | 136 | 136 | 62 | 74 | 20 | 16 | 9 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 84 | 338..342 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 85 | 342..355 | 14 | 14 | 8 | 6 | 3 | 3 | 0 | 79108, 79110, 79128, 79135 |
| 89 | 345..618 | 274 | 274 | 0 | 274 | 0 | 0 | 274 | - |
| 90 | 346..351 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 93 | 366..442 | 77 | 77 | 17 | 60 | 9 | 20 | 17 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 95 | 370..497 | 128 | 128 | 2 | 126 | 1 | 106 | 20 | 79135 |
| 96 | 373..555 | 183 | 183 | 92 | 91 | 28 | 17 | 16 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 101 | 394..425 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 105 | 407..411 | 5 | 5 | 4 | 1 | 0 | 0 | 1 | 78969 |
| 107 | 412..490 | 79 | 79 | 4 | 75 | 3 | 69 | 0 | 79134, 79135, 79136 |
| 108 | 422..462 | 41 | 41 | 30 | 11 | 6 | 5 | 0 | 79097, 79098, 79102 |
| 123 | 470..543 | 74 | 74 | 50 | 24 | 7 | 5 | 10 | 79115, 79116, 79122, 79136 |
| 131 | 486..609 | 124 | 124 | 0 | 124 | 0 | 0 | 124 | - |
| 143 | 525..569 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 148 | 532..541 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 149 | 532..550 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 155 | 560..589 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 159 | 580..611 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 164 | 595..600 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 173 | 659..669 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
