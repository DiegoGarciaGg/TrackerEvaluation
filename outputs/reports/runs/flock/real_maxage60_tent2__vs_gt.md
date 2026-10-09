# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 60, "tentative_threshold": 2}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=d31516533e6d git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage60_tent2/tracks.csv sha256=3a536d0ab283cd96
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage60_tent2
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
| observations | none | 4 | 10142 | 4289 | 0.247 | 0.099 | 0.625 | 1.01 | 0.265 | -0.162 | 1.03 | 105 | 270.0 | 0.156 | 0.263 | 0.111 | 0.136 | 0.321 | 1378 | 8764 | 2911 | 1 | 0 | 24 |
| observations | none | 6 | 10142 | 4289 | 0.259 | 0.112 | 0.610 | 1.42 | 0.272 | -0.134 | 1.43 | 136 | 358.0 | 0.167 | 0.282 | 0.119 | 0.151 | 0.357 | 1533 | 8609 | 2756 | 1 | 1 | 23 |
| observations | none | 8 | 10142 | 4289 | 0.268 | 0.124 | 0.590 | 1.90 | 0.274 | -0.114 | 1.81 | 159 | 423.0 | 0.173 | 0.291 | 0.123 | 0.162 | 0.384 | 1647 | 8495 | 2642 | 1 | 1 | 23 |
| observations | none | 12 | 10142 | 4289 | 0.278 | 0.138 | 0.576 | 2.58 | 0.280 | -0.069 | 2.92 | 180 | 485.0 | 0.189 | 0.318 | 0.135 | 0.186 | 0.440 | 1887 | 8255 | 2402 | 1 | 2 | 22 |
| observations | ignore | 4 | 10142 | 3867 | 0.251 | 0.102 | 0.625 | 1.01 | 0.269 | -0.120 | 1.03 | 105 | 270.0 | 0.161 | 0.292 | 0.111 | 0.136 | 0.356 | 1378 | 8764 | 2489 | 1 | 0 | 24 |
| observations | ignore | 6 | 10142 | 3867 | 0.264 | 0.116 | 0.610 | 1.42 | 0.276 | -0.092 | 1.43 | 136 | 358.0 | 0.172 | 0.312 | 0.119 | 0.151 | 0.396 | 1533 | 8609 | 2334 | 1 | 1 | 23 |
| observations | ignore | 8 | 10142 | 3867 | 0.272 | 0.129 | 0.590 | 1.90 | 0.279 | -0.072 | 1.81 | 159 | 423.0 | 0.178 | 0.323 | 0.123 | 0.162 | 0.426 | 1647 | 8495 | 2220 | 1 | 1 | 23 |
| observations | ignore | 12 | 10142 | 3867 | 0.283 | 0.143 | 0.576 | 2.58 | 0.285 | -0.027 | 2.92 | 180 | 485.0 | 0.195 | 0.353 | 0.135 | 0.186 | 0.488 | 1887 | 8255 | 1980 | 1 | 2 | 22 |
| updates | none | 4 | 10142 | 10346 | 0.203 | 0.075 | 0.563 | 1.18 | 0.217 | -0.743 | 1.14 | 175 | 345.0 | 0.111 | 0.110 | 0.113 | 0.147 | 0.144 | 1493 | 8649 | 8853 | 1 | 0 | 24 |
| updates | none | 6 | 10142 | 10346 | 0.214 | 0.090 | 0.531 | 1.76 | 0.224 | -0.695 | 1.72 | 218 | 445.0 | 0.121 | 0.120 | 0.122 | 0.173 | 0.170 | 1759 | 8383 | 8587 | 1 | 1 | 23 |
| updates | none | 8 | 10142 | 10346 | 0.221 | 0.103 | 0.502 | 2.37 | 0.226 | -0.653 | 2.33 | 247 | 505.0 | 0.126 | 0.125 | 0.127 | 0.196 | 0.192 | 1987 | 8155 | 8359 | 1 | 3 | 21 |
| updates | none | 12 | 10142 | 10346 | 0.230 | 0.118 | 0.474 | 3.28 | 0.232 | -0.577 | 3.71 | 266 | 550.0 | 0.140 | 0.139 | 0.141 | 0.235 | 0.230 | 2380 | 7762 | 7966 | 1 | 5 | 19 |
| updates | ignore | 4 | 10142 | 7165 | 0.222 | 0.090 | 0.563 | 1.18 | 0.238 | -0.429 | 1.14 | 175 | 345.0 | 0.132 | 0.159 | 0.113 | 0.147 | 0.208 | 1493 | 8649 | 5672 | 1 | 0 | 24 |
| updates | ignore | 6 | 10142 | 7165 | 0.234 | 0.108 | 0.531 | 1.76 | 0.245 | -0.381 | 1.72 | 218 | 445.0 | 0.143 | 0.173 | 0.122 | 0.173 | 0.245 | 1759 | 8383 | 5406 | 1 | 1 | 23 |
| updates | ignore | 8 | 10142 | 7165 | 0.243 | 0.124 | 0.502 | 2.37 | 0.249 | -0.339 | 2.33 | 247 | 505.0 | 0.149 | 0.180 | 0.127 | 0.196 | 0.277 | 1987 | 8155 | 5178 | 1 | 3 | 21 |
| updates | ignore | 12 | 10142 | 7165 | 0.253 | 0.144 | 0.474 | 3.28 | 0.256 | -0.263 | 3.71 | 266 | 550.0 | 0.166 | 0.200 | 0.141 | 0.235 | 0.332 | 2380 | 7762 | 4785 | 1 | 5 | 19 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 83; matched pairs: 1647; unmatched reference entries: 8495; unmatched candidate entries: 2642
- identity switches: 159; fragmentation (coverage interruptions): 422; orphan candidate ids (never on a reference object): 65

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f166: ref 79139: 9 -> 12 at (1953.5, 3016), 5 frames after previous cover
- f173: ref 79135: 9 -> 12 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 9 -> 12 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 9 -> 12 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 12 -> 13 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 9 -> 12 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 12 -> 13 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 4 -> 9 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 12 -> 13 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 9 -> 12 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 13 -> 15 at (1797, 3013), 2 frames after previous cover
- f188: ref 78971: 9 -> 12 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 12 -> 13 at (1777.5, 3018.5), 7 frames after previous cover
- f192: ref 78899: 12 -> 4 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 4 -> 12 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 9 -> 4 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 13 -> 15 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 9 -> 4 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 12 -> 13 at (1646.5, 3013), 25 frames after previous cover
- f207: ref 79134: 13 -> 15 at (1655.5, 3014), 15 frames after previous cover
- f212: ref 79128: 13 -> 15 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 9 -> 13 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 13 -> 15 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 9 -> 13 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 12 -> 4 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 4 -> 13 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 13 -> 15 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 9 -> 15 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 13 -> 15 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 13 -> 15 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 13 -> 4 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 15 -> 13 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 15 -> 13 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 15 -> 13 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 15 -> 13 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 15 -> 13 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 13 -> 15 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 13 -> 15 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 13 -> 15 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 4 -> 13 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 13 -> 15 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 4 -> 13 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 13 -> 4 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 4 -> 12 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 78971: 12 -> 13 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 13 -> 15 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 15 -> 4 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 13 -> 4 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 13 -> 12 at (1119, 2986), 3 frames after previous cover
- f242: ref 79097: 4 -> 26 at (1225, 2985), 3 frames after previous cover
- f242: ref 79111: 13 -> 4 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 13 -> 26 at (1179, 2985.5), 5 frames after previous cover
- f255: ref 79037: 13 -> 26 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 4 -> 15 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 4 -> 26 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 4 -> 15 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 26 -> 4 at (1090, 2983.5), 4 frames after previous cover
- f272: ref 79045: 9 -> 26 at (945.5, 2991.5), 89 frames after previous cover
- f274: ref 78899: 26 -> 4 at (996, 2989.5), 5 frames after previous cover
- f282: ref 78897: 26 -> 4 at (913, 2990), 22 frames after previous cover
- ... 99 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 9 | 0 (976) |
| 78896 | 350 (76..429) | 11 | 9 | 4 (7), 12 (3), 36 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 12 (60), 4 (32) |
| 78971 | 352 (84..439) | 18 | 12 | 4 (8), 12 (8), 9 (1), 13 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 12 (11), 26 (2), 50 (2), 9 (1), 4 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 12 (5), 4 (3), 26 (3), 13 (2), 50 (2), 9 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 4 (11), 50 (7), 12 (5), 9 (2), 26 (1), 30 (1) |
| 78899 | 365 (91..455) | 51 | 41 | 4 (20), 26 (12), 12 (6), 50 (5), 38 (3), 13 (2), 30 (1), 47 (1), 49 (1) |
| 79097 | 366 (94..461) | 70 | 45 | 4 (37), 26 (8), 12 (6), 50 (6), 13 (5), 38 (4), 9 (1), 30 (1), 47 (1), 49 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 50 (16), 4 (4), 13 (1), 38 (1), 47 (1), 12 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 50 (15), 4 (6), 38 (1), 49 (1), 12 (1) |
| 79103 | 380 (99..481) | 19 | 12 | 4 (9), 41 (3), 12 (3), 13 (2), 9 (1), 38 (1) |
| 79105 | 379 (101..484) | 7 | 6 | 13 (2), 12 (2), 15 (1), 38 (1), 49 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 12 (4), 15 (3), 13 (2), 4 (2), 9 (1), 41 (1), 38 (1), 49 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 4 (7), 15 (4), 13 (2), 47 (1), 12 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 4 (6), 15 (2), 9 (1), 13 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 15 (4), 13 (2), 49 (1), 17 (1), 24 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 24 (37), 17 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 49 (10), 24 (9), 17 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 17 (55), 13 (3), 15 (2), 9 (1), 12 (1), 38 (1), 25 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 15 (5), 17 (4), 13 (3), 9 (2), 12 (1), 47 (1), 49 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 9 (5), 12 (4), 15 (4), 13 (2), 41 (2), 17 (2), 29 (2), 30 (1), 49 (1), 24 (1) |
| 79135 | 409 (129..542) | 49 | 41 | 15 (15), 29 (14), 9 (6), 17 (5), 13 (2), 41 (2), 25 (2), 12 (1), 49 (1), 24 (1) |
| 79139 | 406 (132..537) | 30 | 20 | 15 (9), 29 (8), 9 (3), 13 (3), 12 (2), 41 (2), 17 (1), 25 (1), 49 (1) |
| 79136 | 393 (136..538) | 4 | 3 | 12 (1), 25 (1), 29 (1), 24 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..24 | 3 | 0 | 3 |
| 2 | 24..30 | 7 | 0 | 3 |
| 3 | 31..31 | 1 | 0 | 1 |
| 5 | 87..89 | 3 | 0 | 3 |
| 6 | 92..99 | 8 | 0 | 3 |
| 10 | 149..209 | 61 | 0 | 15 |
| 11 | 150..155 | 6 | 0 | 4 |
| 20 | 216..222 | 7 | 0 | 6 |
| 22 | 224..233 | 10 | 0 | 10 |
| 27 | 249..258 | 10 | 0 | 10 |
| 31 | 274..290 | 17 | 0 | 16 |
| 33 | 275..614 | 340 | 0 | 263 |
| 34 | 277..455 | 179 | 0 | 132 |
| 35 | 278..284 | 7 | 0 | 6 |
| 39 | 297..601 | 305 | 0 | 227 |
| 40 | 299..311 | 13 | 0 | 11 |
| 43 | 324..335 | 12 | 0 | 12 |
| 45 | 340..346 | 7 | 0 | 6 |
| 48 | 349..360 | 12 | 0 | 11 |
| 52 | 374..384 | 11 | 0 | 11 |
| 54 | 388..486 | 99 | 0 | 50 |
| 56 | 399..433 | 35 | 0 | 14 |
| 57 | 402..408 | 7 | 0 | 6 |
| 59 | 409..603 | 195 | 0 | 153 |
| 61 | 449..470 | 22 | 0 | 8 |
| 62 | 450..456 | 7 | 0 | 6 |
| 64 | 466..476 | 11 | 0 | 5 |
| 65 | 472..495 | 24 | 0 | 4 |
| 66 | 474..483 | 10 | 0 | 10 |
| 67 | 499..508 | 10 | 0 | 10 |
| 69 | 524..535 | 12 | 0 | 10 |
| 70 | 526..532 | 7 | 0 | 6 |
| 72 | 529..537 | 9 | 0 | 6 |
| 73 | 529..546 | 18 | 0 | 13 |
| 78 | 549..561 | 13 | 0 | 11 |
| 80 | 574..610 | 37 | 0 | 14 |
| 83 | 588..594 | 7 | 0 | 6 |
| 84 | 592..596 | 5 | 0 | 5 |
| 88 | 624..634 | 11 | 0 | 11 |
| 89 | 649..685 | 37 | 0 | 14 |
| ... | 25 more | | | |

### Gaps and durations of candidate tracks
- tracks: 83; lifespan min/median/max: 1/11/1008; tracks with internal gaps: 18; total internal gaps: 148; longest internal gap: 196; tracks ending in coasting: 76 (trailing rows total 1447)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..1008 | 1008 | 982 | 976 | 6 | 5 | 2 | 0 | 78911 |
| 1 | 22..24 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 2 | 24..30 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 3 | 31..31 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 4 | 79..499 | 421 | 339 | 153 | 186 | 41 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 5 | 87..89 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 6 | 92..99 | 8 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 9 | 138..214 | 77 | 36 | 26 | 10 | 6 | 1 | 4 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 10 | 149..209 | 61 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 11 | 150..155 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 12 | 160..466 | 307 | 193 | 126 | 67 | 25 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 175..274 | 100 | 46 | 35 | 11 | 5 | 2 | 3 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 15 | 187..406 | 220 | 104 | 49 | 55 | 10 | 2 | 44 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 17 | 203..514 | 312 | 298 | 70 | 228 | 8 | 196 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 20 | 216..222 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 22 | 224..233 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 24 | 233..590 | 358 | 274 | 50 | 224 | 8 | 180 | 25 | 79115, 79116, 79122, 79134, 79135, 79136 |
| 25 | 239..513 | 275 | 193 | 5 | 188 | 3 | 148 | 0 | 79132, 79135, 79136, 79139 |
| 26 | 242..280 | 39 | 32 | 26 | 6 | 2 | 1 | 4 | 78897, 78899, 79037, 79045, 79097 |
| 27 | 249..258 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 29 | 265..612 | 348 | 251 | 25 | 226 | 7 | 150 | 33 | 79134, 79135, 79136, 79139 |
| 30 | 268..346 | 79 | 30 | 4 | 26 | 2 | 25 | 0 | 78897, 78899, 79097, 79134 |
| 31 | 274..290 | 17 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 33 | 275..614 | 340 | 263 | 0 | 263 | 0 | 0 | 263 | - |
| 34 | 277..455 | 179 | 132 | 0 | 132 | 0 | 0 | 132 | - |
| 35 | 278..284 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 36 | 281..292 | 12 | 8 | 1 | 7 | 1 | 6 | 1 | 78896 |
| 38 | 297..342 | 46 | 28 | 13 | 15 | 6 | 9 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79132 |
| 39 | 297..601 | 305 | 227 | 0 | 227 | 0 | 0 | 227 | - |
| 40 | 299..311 | 13 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 41 | 300..338 | 39 | 12 | 10 | 2 | 1 | 1 | 1 | 79103, 79108, 79134, 79135, 79139 |
| 43 | 324..335 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 45 | 340..346 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 47 | 346..354 | 9 | 9 | 5 | 4 | 1 | 1 | 3 | 78899, 79097, 79098, 79110, 79128 |
| 48 | 349..360 | 12 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 49 | 363..442 | 80 | 66 | 20 | 46 | 10 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 50 | 370..461 | 92 | 65 | 53 | 12 | 7 | 2 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 52 | 374..384 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 54 | 388..486 | 99 | 50 | 0 | 50 | 0 | 0 | 50 | - |
| 56 | 399..433 | 35 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 57 | 402..408 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 59 | 409..603 | 195 | 153 | 0 | 153 | 0 | 0 | 153 | - |
| 61 | 449..470 | 22 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 62 | 450..456 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 64 | 466..476 | 11 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 65 | 472..495 | 24 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 66 | 474..483 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 67 | 499..508 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 69 | 524..535 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 70 | 526..532 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 72 | 529..537 | 9 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 73 | 529..546 | 18 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 78 | 549..561 | 13 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 80 | 574..610 | 37 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 83 | 588..594 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 84 | 592..596 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 88 | 624..634 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 89 | 649..685 | 37 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 90 | 650..656 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 92 | 656..665 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 94 | 700..708 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 95 | 712..718 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 97 | 720..728 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 99 | 724..733 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 100 | 749..758 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 101 | 774..782 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 103 | 785..794 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 105 | 799..811 | 13 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 107 | 824..834 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 108 | 836..842 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 111 | 847..856 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 113 | 849..860 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 115 | 874..885 | 12 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 116 | 898..906 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 117 | 900..911 | 12 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 121 | 912..919 | 8 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 123 | 924..935 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 124 | 930..940 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 125 | 949..957 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 127 | 960..965 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| ... | 3 more in JSON | | | | | | | | |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 37; matched pairs: 1647; unmatched reference entries: 8495; unmatched candidate entries: 2220
- identity switches: 159; fragmentation (coverage interruptions): 422; orphan candidate ids (never on a reference object): 19

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f166: ref 79139: 9 -> 12 at (1953.5, 3016), 5 frames after previous cover
- f173: ref 79135: 9 -> 12 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 9 -> 12 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 9 -> 12 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 12 -> 13 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 9 -> 12 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 12 -> 13 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 4 -> 9 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 12 -> 13 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 9 -> 12 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 13 -> 15 at (1797, 3013), 2 frames after previous cover
- f188: ref 78971: 9 -> 12 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 12 -> 13 at (1777.5, 3018.5), 7 frames after previous cover
- f192: ref 78899: 12 -> 4 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 4 -> 12 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 9 -> 4 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 13 -> 15 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 9 -> 4 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 12 -> 13 at (1646.5, 3013), 25 frames after previous cover
- f207: ref 79134: 13 -> 15 at (1655.5, 3014), 15 frames after previous cover
- f212: ref 79128: 13 -> 15 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 9 -> 13 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 13 -> 15 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 9 -> 13 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 12 -> 4 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 4 -> 13 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 13 -> 15 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 9 -> 15 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 13 -> 15 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 13 -> 15 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 13 -> 4 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 15 -> 13 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 15 -> 13 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 15 -> 13 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 15 -> 13 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 15 -> 13 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 13 -> 15 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 13 -> 15 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 13 -> 15 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 4 -> 13 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 13 -> 15 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 4 -> 13 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 13 -> 4 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 4 -> 12 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 78971: 12 -> 13 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 13 -> 15 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 15 -> 4 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 13 -> 4 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 13 -> 12 at (1119, 2986), 3 frames after previous cover
- f242: ref 79097: 4 -> 26 at (1225, 2985), 3 frames after previous cover
- f242: ref 79111: 13 -> 4 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 13 -> 26 at (1179, 2985.5), 5 frames after previous cover
- f255: ref 79037: 13 -> 26 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 4 -> 15 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 4 -> 26 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 4 -> 15 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 26 -> 4 at (1090, 2983.5), 4 frames after previous cover
- f272: ref 79045: 9 -> 26 at (945.5, 2991.5), 89 frames after previous cover
- f274: ref 78899: 26 -> 4 at (996, 2989.5), 5 frames after previous cover
- f282: ref 78897: 26 -> 4 at (913, 2990), 22 frames after previous cover
- ... 99 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 9 | 0 (976) |
| 78896 | 350 (76..429) | 11 | 9 | 4 (7), 12 (3), 36 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 12 (60), 4 (32) |
| 78971 | 352 (84..439) | 18 | 12 | 4 (8), 12 (8), 9 (1), 13 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 12 (11), 26 (2), 50 (2), 9 (1), 4 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 12 (5), 4 (3), 26 (3), 13 (2), 50 (2), 9 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 4 (11), 50 (7), 12 (5), 9 (2), 26 (1), 30 (1) |
| 78899 | 365 (91..455) | 51 | 41 | 4 (20), 26 (12), 12 (6), 50 (5), 38 (3), 13 (2), 30 (1), 47 (1), 49 (1) |
| 79097 | 366 (94..461) | 70 | 45 | 4 (37), 26 (8), 12 (6), 50 (6), 13 (5), 38 (4), 9 (1), 30 (1), 47 (1), 49 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 50 (16), 4 (4), 13 (1), 38 (1), 47 (1), 12 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 50 (15), 4 (6), 38 (1), 49 (1), 12 (1) |
| 79103 | 380 (99..481) | 19 | 12 | 4 (9), 41 (3), 12 (3), 13 (2), 9 (1), 38 (1) |
| 79105 | 379 (101..484) | 7 | 6 | 13 (2), 12 (2), 15 (1), 38 (1), 49 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 12 (4), 15 (3), 13 (2), 4 (2), 9 (1), 41 (1), 38 (1), 49 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 4 (7), 15 (4), 13 (2), 47 (1), 12 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 4 (6), 15 (2), 9 (1), 13 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 15 (4), 13 (2), 49 (1), 17 (1), 24 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 24 (37), 17 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 49 (10), 24 (9), 17 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 17 (55), 13 (3), 15 (2), 9 (1), 12 (1), 38 (1), 25 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 15 (5), 17 (4), 13 (3), 9 (2), 12 (1), 47 (1), 49 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 9 (5), 12 (4), 15 (4), 13 (2), 41 (2), 17 (2), 29 (2), 30 (1), 49 (1), 24 (1) |
| 79135 | 409 (129..542) | 49 | 41 | 15 (15), 29 (14), 9 (6), 17 (5), 13 (2), 41 (2), 25 (2), 12 (1), 49 (1), 24 (1) |
| 79139 | 406 (132..537) | 30 | 20 | 15 (9), 29 (8), 9 (3), 13 (3), 12 (2), 41 (2), 17 (1), 25 (1), 49 (1) |
| 79136 | 393 (136..538) | 4 | 3 | 12 (1), 25 (1), 29 (1), 24 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..24 | 3 | 0 | 3 |
| 5 | 87..89 | 3 | 0 | 3 |
| 11 | 150..155 | 6 | 0 | 4 |
| 33 | 275..614 | 340 | 0 | 263 |
| 34 | 277..455 | 179 | 0 | 132 |
| 39 | 297..601 | 305 | 0 | 227 |
| 54 | 388..486 | 99 | 0 | 50 |
| 59 | 409..603 | 195 | 0 | 153 |
| 64 | 466..476 | 11 | 0 | 5 |
| 65 | 472..495 | 24 | 0 | 4 |
| 72 | 529..537 | 9 | 0 | 6 |
| 73 | 529..546 | 18 | 0 | 13 |
| 84 | 592..596 | 5 | 0 | 5 |
| 92 | 656..665 | 10 | 0 | 10 |
| 97 | 720..728 | 9 | 0 | 4 |
| 103 | 785..794 | 10 | 0 | 5 |
| 111 | 847..856 | 10 | 0 | 5 |
| 121 | 912..919 | 8 | 0 | 4 |
| 130 | 975..981 | 7 | 0 | 5 |

### Gaps and durations of candidate tracks
- tracks: 37; lifespan min/median/max: 3/46/1008; tracks with internal gaps: 18; total internal gaps: 148; longest internal gap: 196; tracks ending in coasting: 30 (trailing rows total 1025)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..1008 | 1008 | 982 | 976 | 6 | 5 | 2 | 0 | 78911 |
| 1 | 22..24 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 4 | 79..499 | 421 | 339 | 153 | 186 | 41 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 5 | 87..89 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 9 | 138..214 | 77 | 36 | 26 | 10 | 6 | 1 | 4 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 11 | 150..155 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 12 | 160..466 | 307 | 193 | 126 | 67 | 25 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 175..274 | 100 | 46 | 35 | 11 | 5 | 2 | 3 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 15 | 187..406 | 220 | 104 | 49 | 55 | 10 | 2 | 44 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 17 | 203..514 | 312 | 298 | 70 | 228 | 8 | 196 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 24 | 233..590 | 358 | 274 | 50 | 224 | 8 | 180 | 25 | 79115, 79116, 79122, 79134, 79135, 79136 |
| 25 | 239..513 | 275 | 193 | 5 | 188 | 3 | 148 | 0 | 79132, 79135, 79136, 79139 |
| 26 | 242..280 | 39 | 32 | 26 | 6 | 2 | 1 | 4 | 78897, 78899, 79037, 79045, 79097 |
| 29 | 265..612 | 348 | 251 | 25 | 226 | 7 | 150 | 33 | 79134, 79135, 79136, 79139 |
| 30 | 268..346 | 79 | 30 | 4 | 26 | 2 | 25 | 0 | 78897, 78899, 79097, 79134 |
| 33 | 275..614 | 340 | 263 | 0 | 263 | 0 | 0 | 263 | - |
| 34 | 277..455 | 179 | 132 | 0 | 132 | 0 | 0 | 132 | - |
| 36 | 281..292 | 12 | 8 | 1 | 7 | 1 | 6 | 1 | 78896 |
| 38 | 297..342 | 46 | 28 | 13 | 15 | 6 | 9 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79132 |
| 39 | 297..601 | 305 | 227 | 0 | 227 | 0 | 0 | 227 | - |
| 41 | 300..338 | 39 | 12 | 10 | 2 | 1 | 1 | 1 | 79103, 79108, 79134, 79135, 79139 |
| 47 | 346..354 | 9 | 9 | 5 | 4 | 1 | 1 | 3 | 78899, 79097, 79098, 79110, 79128 |
| 49 | 363..442 | 80 | 66 | 20 | 46 | 10 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 50 | 370..461 | 92 | 65 | 53 | 12 | 7 | 2 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 54 | 388..486 | 99 | 50 | 0 | 50 | 0 | 0 | 50 | - |
| 59 | 409..603 | 195 | 153 | 0 | 153 | 0 | 0 | 153 | - |
| 64 | 466..476 | 11 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 65 | 472..495 | 24 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 72 | 529..537 | 9 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 73 | 529..546 | 18 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 84 | 592..596 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 92 | 656..665 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 97 | 720..728 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 103 | 785..794 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 111 | 847..856 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 121 | 912..919 | 8 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 130 | 975..981 | 7 | 5 | 0 | 5 | 0 | 0 | 5 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 83; matched pairs: 1987; unmatched reference entries: 8155; unmatched candidate entries: 8359
- identity switches: 247; fragmentation (coverage interruptions): 500; orphan candidate ids (never on a reference object): 65

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f161: ref 79136: 9 -> 12 at (2010, 3014.5), 20 frames after previous cover
- f166: ref 79139: 9 -> 12 at (1953.5, 3016), 4 frames after previous cover
- f173: ref 79135: 9 -> 12 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 9 -> 12 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 9 -> 12 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 12 -> 13 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 9 -> 12 at (1812, 3020), 3 frames after previous cover
- f178: ref 79136: 12 -> 13 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 12 -> 13 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 4 -> 9 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 12 -> 13 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 9 -> 12 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 13 -> 15 at (1797, 3013), 2 frames after previous cover
- f188: ref 78969: 4 -> 9 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 9 -> 12 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 12 -> 13 at (1777.5, 3018.5), 6 frames after previous cover
- f190: ref 79045: 9 -> 12 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 15 -> 13 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 12 -> 4 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 9 -> 12 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 78971: 12 -> 9 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 13 -> 15 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 9 -> 4 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 12 -> 9 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 13 -> 15 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 12 -> 9 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 9 -> 4 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 4 -> 9 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 12 -> 13 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 9 -> 4 at (1419.5, 3003), 2 frames after previous cover
- f205: ref 78899: 4 -> 9 at (1433, 3006), 1 frames after previous cover
- f207: ref 79134: 13 -> 15 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 13 -> 15 at (1698.5, 3013.5), 27 frames after previous cover
- f210: ref 78899: 9 -> 4 at (1400, 3003.5), 5 frames after previous cover
- f212: ref 79128: 13 -> 15 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 9 -> 13 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 13 -> 15 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 9 -> 13 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 9 -> 4 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 4 -> 13 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 13 -> 15 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 9 -> 15 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 13 -> 15 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 13 -> 15 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 13 -> 4 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 15 -> 13 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 15 -> 13 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 15 -> 13 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 15 -> 13 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 15 -> 13 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 9 -> 12 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 13 -> 15 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 13 -> 15 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 13 -> 15 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 4 -> 13 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 13 -> 15 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 4 -> 13 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 13 -> 4 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 4 -> 12 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 12 -> 13 at (1139, 2987), 10 frames after previous cover
- ... 187 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 979 | 7 | 0 (979) |
| 78896 | 350 (76..429) | 13 | 9 | 4 (8), 12 (3), 36 (2) |
| 78969 | 352 (80..434) | 100 | 46 | 12 (59), 4 (37), 9 (2), 36 (2) |
| 78971 | 352 (84..439) | 29 | 17 | 12 (11), 4 (9), 13 (4), 9 (3), 26 (1), 36 (1) |
| 79045 | 355 (84..443) | 40 | 16 | 12 (22), 9 (4), 50 (4), 13 (3), 26 (3), 36 (3), 4 (1) |
| 79037 | 355 (86..445) | 30 | 19 | 12 (11), 13 (5), 9 (3), 4 (3), 26 (3), 50 (3), 36 (2) |
| 78897 | 345 (89..450) | 48 | 25 | 4 (13), 50 (12), 12 (7), 9 (4), 36 (3), 30 (3), 47 (3), 13 (2), 26 (1) |
| 78899 | 365 (91..455) | 74 | 41 | 4 (21), 26 (14), 12 (13), 50 (6), 13 (5), 30 (4), 38 (3), 47 (3), 36 (2), 49 (2), 9 (1) |
| 79097 | 366 (94..461) | 86 | 43 | 4 (38), 26 (8), 13 (7), 50 (7), 38 (5), 12 (5), 49 (5), 47 (4), 36 (3), 30 (3), 9 (1) |
| 79098 | 360 (97..467) | 43 | 23 | 50 (20), 4 (7), 13 (4), 47 (4), 38 (3), 36 (2), 30 (2), 12 (1) |
| 79102 | 371 (98..477) | 38 | 19 | 50 (15), 4 (7), 47 (4), 13 (3), 38 (3), 36 (2), 30 (2), 49 (1), 12 (1) |
| 79103 | 380 (99..481) | 37 | 16 | 4 (14), 12 (5), 38 (4), 41 (4), 47 (3), 13 (2), 36 (2), 30 (2), 9 (1) |
| 79105 | 379 (101..484) | 23 | 11 | 38 (4), 4 (3), 36 (3), 30 (3), 47 (3), 13 (2), 15 (2), 12 (2), 49 (1) |
| 79108 | 385 (104..492) | 32 | 17 | 12 (7), 4 (5), 15 (3), 36 (3), 47 (3), 9 (2), 13 (2), 41 (2), 38 (2), 30 (2), 49 (1) |
| 79110 | 388 (106..497) | 32 | 15 | 4 (9), 15 (5), 47 (4), 38 (3), 30 (3), 13 (2), 41 (2), 36 (2), 12 (2) |
| 79111 | 386 (109..500) | 18 | 9 | 4 (7), 15 (4), 41 (2), 36 (2), 9 (1), 13 (1), 38 (1) |
| 79115 | 421 (111..531) | 16 | 12 | 15 (6), 41 (3), 13 (2), 38 (2), 49 (1), 17 (1), 24 (1) |
| 79116 | 411 (114..530) | 43 | 10 | 24 (37), 17 (3), 25 (2), 41 (1) |
| 79122 | 404 (118..532) | 34 | 16 | 24 (12), 49 (10), 36 (3), 25 (3), 15 (2), 41 (2), 9 (1), 17 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 17 (57), 13 (3), 15 (2), 9 (1), 12 (1), 38 (1) |
| 79128 | 402 (124..527) | 26 | 17 | 13 (7), 15 (5), 17 (4), 9 (3), 25 (3), 49 (2), 12 (1), 47 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 9 (7), 13 (6), 12 (5), 15 (4), 49 (3), 41 (2), 17 (2), 29 (2), 24 (2), 30 (1) |
| 79135 | 409 (129..542) | 72 | 41 | 29 (20), 15 (14), 25 (10), 9 (9), 17 (6), 41 (5), 12 (3), 13 (2), 24 (2), 49 (1) |
| 79139 | 406 (132..537) | 47 | 23 | 15 (13), 29 (9), 41 (7), 9 (5), 25 (4), 13 (3), 17 (3), 12 (2), 49 (1) |
| 79136 | 393 (136..538) | 28 | 15 | 15 (7), 12 (6), 29 (3), 17 (3), 13 (2), 41 (2), 25 (2), 24 (2), 9 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..83 | 62 | 0 | 62 |
| 2 | 24..89 | 66 | 0 | 66 |
| 3 | 31..90 | 60 | 0 | 60 |
| 5 | 87..148 | 62 | 0 | 62 |
| 6 | 92..158 | 67 | 0 | 67 |
| 10 | 149..268 | 120 | 0 | 120 |
| 11 | 150..214 | 65 | 0 | 65 |
| 20 | 216..281 | 66 | 0 | 66 |
| 22 | 224..292 | 69 | 0 | 69 |
| 27 | 249..317 | 69 | 0 | 69 |
| 31 | 274..349 | 76 | 0 | 76 |
| 33 | 275..673 | 399 | 0 | 399 |
| 34 | 277..514 | 238 | 0 | 238 |
| 35 | 278..343 | 66 | 0 | 66 |
| 39 | 297..660 | 364 | 0 | 364 |
| 40 | 299..370 | 72 | 0 | 72 |
| 43 | 324..394 | 71 | 0 | 71 |
| 45 | 340..405 | 66 | 0 | 66 |
| 48 | 349..419 | 71 | 0 | 71 |
| 52 | 374..443 | 70 | 0 | 70 |
| 54 | 388..545 | 158 | 0 | 158 |
| 56 | 399..492 | 94 | 0 | 94 |
| 57 | 402..467 | 66 | 0 | 66 |
| 59 | 409..662 | 254 | 0 | 254 |
| 61 | 449..529 | 81 | 0 | 81 |
| 62 | 450..515 | 66 | 0 | 66 |
| 64 | 466..535 | 70 | 0 | 70 |
| 65 | 472..554 | 83 | 0 | 83 |
| 66 | 474..542 | 69 | 0 | 69 |
| 67 | 499..567 | 69 | 0 | 69 |
| 69 | 524..594 | 71 | 0 | 71 |
| 70 | 526..591 | 66 | 0 | 66 |
| 72 | 529..596 | 68 | 0 | 68 |
| 73 | 529..605 | 77 | 0 | 77 |
| 78 | 549..620 | 72 | 0 | 72 |
| 80 | 574..669 | 96 | 0 | 96 |
| 83 | 588..653 | 66 | 0 | 66 |
| 84 | 592..655 | 64 | 0 | 64 |
| 88 | 624..693 | 70 | 0 | 70 |
| 89 | 649..744 | 96 | 0 | 96 |
| ... | 25 more | | | |

### Gaps and durations of candidate tracks
- tracks: 83; lifespan min/median/max: 10/70/1008; tracks with internal gaps: 18; total internal gaps: 273; longest internal gap: 216; tracks ending in coasting: 82 (trailing rows total 6586)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..1008 | 1008 | 1008 | 979 | 29 | 7 | 21 | 0 | 78911 |
| 1 | 22..83 | 62 | 62 | 0 | 62 | 0 | 0 | 62 | - |
| 2 | 24..89 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 3 | 31..90 | 60 | 60 | 0 | 60 | 0 | 0 | 60 | - |
| 4 | 79..558 | 480 | 480 | 182 | 298 | 54 | 53 | 58 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 5 | 87..148 | 62 | 62 | 0 | 62 | 0 | 0 | 62 | - |
| 6 | 92..158 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 9 | 138..273 | 136 | 136 | 49 | 87 | 13 | 3 | 68 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 10 | 149..268 | 120 | 120 | 0 | 120 | 0 | 0 | 120 | - |
| 11 | 150..214 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 12 | 160..525 | 366 | 366 | 167 | 199 | 46 | 29 | 64 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 175..333 | 159 | 159 | 67 | 92 | 17 | 3 | 66 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 187..465 | 279 | 279 | 67 | 212 | 14 | 4 | 192 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 203..573 | 371 | 371 | 80 | 291 | 12 | 200 | 35 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 216..281 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 22 | 224..292 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 24 | 233..649 | 417 | 417 | 56 | 361 | 10 | 216 | 116 | 79115, 79116, 79122, 79134, 79135, 79136 |
| 25 | 239..572 | 334 | 334 | 24 | 310 | 7 | 180 | 30 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 26 | 242..339 | 98 | 98 | 30 | 68 | 5 | 2 | 62 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 27 | 249..317 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 29 | 265..671 | 407 | 407 | 34 | 373 | 10 | 163 | 132 | 79134, 79135, 79136, 79139 |
| 30 | 268..405 | 138 | 138 | 25 | 113 | 10 | 73 | 20 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79134 |
| 31 | 274..349 | 76 | 76 | 0 | 76 | 0 | 0 | 76 | - |
| 33 | 275..673 | 399 | 399 | 0 | 399 | 0 | 0 | 399 | - |
| 34 | 277..514 | 238 | 238 | 0 | 238 | 0 | 0 | 238 | - |
| 35 | 278..343 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 36 | 281..351 | 71 | 71 | 37 | 34 | 12 | 6 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122 |
| 38 | 297..401 | 105 | 105 | 31 | 74 | 12 | 25 | 32 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132 |
| 39 | 297..660 | 364 | 364 | 0 | 364 | 0 | 0 | 364 | - |
| 40 | 299..370 | 72 | 72 | 0 | 72 | 0 | 0 | 72 | - |
| 41 | 300..397 | 98 | 98 | 32 | 66 | 6 | 1 | 60 | 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 43 | 324..394 | 71 | 71 | 0 | 71 | 0 | 0 | 71 | - |
| 45 | 340..405 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 47 | 346..413 | 68 | 68 | 32 | 36 | 11 | 4 | 18 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128 |
| 48 | 349..419 | 71 | 71 | 0 | 71 | 0 | 0 | 71 | - |
| 49 | 363..501 | 139 | 139 | 28 | 111 | 12 | 22 | 53 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 50 | 370..520 | 151 | 151 | 67 | 84 | 15 | 8 | 56 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 52 | 374..443 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 54 | 388..545 | 158 | 158 | 0 | 158 | 0 | 0 | 158 | - |
| 56 | 399..492 | 94 | 94 | 0 | 94 | 0 | 0 | 94 | - |
| 57 | 402..467 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 59 | 409..662 | 254 | 254 | 0 | 254 | 0 | 0 | 254 | - |
| 61 | 449..529 | 81 | 81 | 0 | 81 | 0 | 0 | 81 | - |
| 62 | 450..515 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 64 | 466..535 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 65 | 472..554 | 83 | 83 | 0 | 83 | 0 | 0 | 83 | - |
| 66 | 474..542 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 67 | 499..567 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 69 | 524..594 | 71 | 71 | 0 | 71 | 0 | 0 | 71 | - |
| 70 | 526..591 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 72 | 529..596 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 73 | 529..605 | 77 | 77 | 0 | 77 | 0 | 0 | 77 | - |
| 78 | 549..620 | 72 | 72 | 0 | 72 | 0 | 0 | 72 | - |
| 80 | 574..669 | 96 | 96 | 0 | 96 | 0 | 0 | 96 | - |
| 83 | 588..653 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 84 | 592..655 | 64 | 64 | 0 | 64 | 0 | 0 | 64 | - |
| 88 | 624..693 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 89 | 649..744 | 96 | 96 | 0 | 96 | 0 | 0 | 96 | - |
| 90 | 650..715 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 92 | 656..724 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 94 | 700..767 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 95 | 712..777 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 97 | 720..787 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 99 | 724..792 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 100 | 749..817 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 101 | 774..841 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 103 | 785..853 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 105 | 799..870 | 72 | 72 | 0 | 72 | 0 | 0 | 72 | - |
| 107 | 824..893 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 108 | 836..901 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 111 | 847..915 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 113 | 849..919 | 71 | 71 | 0 | 71 | 0 | 0 | 71 | - |
| 115 | 874..944 | 71 | 71 | 0 | 71 | 0 | 0 | 71 | - |
| 116 | 898..965 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 117 | 900..970 | 71 | 71 | 0 | 71 | 0 | 0 | 71 | - |
| 121 | 912..978 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 123 | 924..994 | 71 | 71 | 0 | 71 | 0 | 0 | 71 | - |
| 124 | 930..999 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 125 | 949..1008 | 60 | 60 | 0 | 60 | 0 | 0 | 60 | - |
| 127 | 960..1008 | 49 | 49 | 0 | 49 | 0 | 0 | 49 | - |
| ... | 3 more in JSON | | | | | | | | |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 37; matched pairs: 1987; unmatched reference entries: 8155; unmatched candidate entries: 5178
- identity switches: 247; fragmentation (coverage interruptions): 500; orphan candidate ids (never on a reference object): 19

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f161: ref 79136: 9 -> 12 at (2010, 3014.5), 20 frames after previous cover
- f166: ref 79139: 9 -> 12 at (1953.5, 3016), 4 frames after previous cover
- f173: ref 79135: 9 -> 12 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 9 -> 12 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 9 -> 12 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 12 -> 13 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 9 -> 12 at (1812, 3020), 3 frames after previous cover
- f178: ref 79136: 12 -> 13 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 12 -> 13 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 4 -> 9 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 12 -> 13 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 9 -> 12 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 13 -> 15 at (1797, 3013), 2 frames after previous cover
- f188: ref 78969: 4 -> 9 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 9 -> 12 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 12 -> 13 at (1777.5, 3018.5), 6 frames after previous cover
- f190: ref 79045: 9 -> 12 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 15 -> 13 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 12 -> 4 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 9 -> 12 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 78971: 12 -> 9 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 13 -> 15 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 9 -> 4 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 12 -> 9 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 13 -> 15 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 12 -> 9 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 9 -> 4 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 4 -> 9 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 12 -> 13 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 9 -> 4 at (1419.5, 3003), 2 frames after previous cover
- f205: ref 78899: 4 -> 9 at (1433, 3006), 1 frames after previous cover
- f207: ref 79134: 13 -> 15 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 13 -> 15 at (1698.5, 3013.5), 27 frames after previous cover
- f210: ref 78899: 9 -> 4 at (1400, 3003.5), 5 frames after previous cover
- f212: ref 79128: 13 -> 15 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 9 -> 13 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 13 -> 15 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 9 -> 13 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 9 -> 4 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 4 -> 13 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 13 -> 15 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 9 -> 15 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 13 -> 15 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 13 -> 15 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 13 -> 4 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 15 -> 13 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 15 -> 13 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 15 -> 13 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 15 -> 13 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 15 -> 13 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 9 -> 12 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 13 -> 15 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 13 -> 15 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 13 -> 15 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 4 -> 13 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 13 -> 15 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 4 -> 13 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 13 -> 4 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 4 -> 12 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 12 -> 13 at (1139, 2987), 10 frames after previous cover
- ... 187 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 979 | 7 | 0 (979) |
| 78896 | 350 (76..429) | 13 | 9 | 4 (8), 12 (3), 36 (2) |
| 78969 | 352 (80..434) | 100 | 46 | 12 (59), 4 (37), 9 (2), 36 (2) |
| 78971 | 352 (84..439) | 29 | 17 | 12 (11), 4 (9), 13 (4), 9 (3), 26 (1), 36 (1) |
| 79045 | 355 (84..443) | 40 | 16 | 12 (22), 9 (4), 50 (4), 13 (3), 26 (3), 36 (3), 4 (1) |
| 79037 | 355 (86..445) | 30 | 19 | 12 (11), 13 (5), 9 (3), 4 (3), 26 (3), 50 (3), 36 (2) |
| 78897 | 345 (89..450) | 48 | 25 | 4 (13), 50 (12), 12 (7), 9 (4), 36 (3), 30 (3), 47 (3), 13 (2), 26 (1) |
| 78899 | 365 (91..455) | 74 | 41 | 4 (21), 26 (14), 12 (13), 50 (6), 13 (5), 30 (4), 38 (3), 47 (3), 36 (2), 49 (2), 9 (1) |
| 79097 | 366 (94..461) | 86 | 43 | 4 (38), 26 (8), 13 (7), 50 (7), 38 (5), 12 (5), 49 (5), 47 (4), 36 (3), 30 (3), 9 (1) |
| 79098 | 360 (97..467) | 43 | 23 | 50 (20), 4 (7), 13 (4), 47 (4), 38 (3), 36 (2), 30 (2), 12 (1) |
| 79102 | 371 (98..477) | 38 | 19 | 50 (15), 4 (7), 47 (4), 13 (3), 38 (3), 36 (2), 30 (2), 49 (1), 12 (1) |
| 79103 | 380 (99..481) | 37 | 16 | 4 (14), 12 (5), 38 (4), 41 (4), 47 (3), 13 (2), 36 (2), 30 (2), 9 (1) |
| 79105 | 379 (101..484) | 23 | 11 | 38 (4), 4 (3), 36 (3), 30 (3), 47 (3), 13 (2), 15 (2), 12 (2), 49 (1) |
| 79108 | 385 (104..492) | 32 | 17 | 12 (7), 4 (5), 15 (3), 36 (3), 47 (3), 9 (2), 13 (2), 41 (2), 38 (2), 30 (2), 49 (1) |
| 79110 | 388 (106..497) | 32 | 15 | 4 (9), 15 (5), 47 (4), 38 (3), 30 (3), 13 (2), 41 (2), 36 (2), 12 (2) |
| 79111 | 386 (109..500) | 18 | 9 | 4 (7), 15 (4), 41 (2), 36 (2), 9 (1), 13 (1), 38 (1) |
| 79115 | 421 (111..531) | 16 | 12 | 15 (6), 41 (3), 13 (2), 38 (2), 49 (1), 17 (1), 24 (1) |
| 79116 | 411 (114..530) | 43 | 10 | 24 (37), 17 (3), 25 (2), 41 (1) |
| 79122 | 404 (118..532) | 34 | 16 | 24 (12), 49 (10), 36 (3), 25 (3), 15 (2), 41 (2), 9 (1), 17 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 17 (57), 13 (3), 15 (2), 9 (1), 12 (1), 38 (1) |
| 79128 | 402 (124..527) | 26 | 17 | 13 (7), 15 (5), 17 (4), 9 (3), 25 (3), 49 (2), 12 (1), 47 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 9 (7), 13 (6), 12 (5), 15 (4), 49 (3), 41 (2), 17 (2), 29 (2), 24 (2), 30 (1) |
| 79135 | 409 (129..542) | 72 | 41 | 29 (20), 15 (14), 25 (10), 9 (9), 17 (6), 41 (5), 12 (3), 13 (2), 24 (2), 49 (1) |
| 79139 | 406 (132..537) | 47 | 23 | 15 (13), 29 (9), 41 (7), 9 (5), 25 (4), 13 (3), 17 (3), 12 (2), 49 (1) |
| 79136 | 393 (136..538) | 28 | 15 | 15 (7), 12 (6), 29 (3), 17 (3), 13 (2), 41 (2), 25 (2), 24 (2), 9 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..83 | 62 | 0 | 62 |
| 5 | 87..148 | 62 | 0 | 62 |
| 11 | 150..214 | 65 | 0 | 65 |
| 33 | 275..673 | 399 | 0 | 399 |
| 34 | 277..514 | 238 | 0 | 238 |
| 39 | 297..660 | 364 | 0 | 364 |
| 54 | 388..545 | 158 | 0 | 158 |
| 59 | 409..662 | 254 | 0 | 254 |
| 64 | 466..535 | 70 | 0 | 70 |
| 65 | 472..554 | 83 | 0 | 83 |
| 72 | 529..596 | 68 | 0 | 68 |
| 73 | 529..605 | 77 | 0 | 77 |
| 84 | 592..655 | 64 | 0 | 64 |
| 92 | 656..724 | 69 | 0 | 69 |
| 97 | 720..787 | 68 | 0 | 68 |
| 103 | 785..853 | 69 | 0 | 69 |
| 111 | 847..915 | 69 | 0 | 69 |
| 121 | 912..978 | 67 | 0 | 67 |
| 130 | 975..1008 | 34 | 0 | 34 |

### Gaps and durations of candidate tracks
- tracks: 37; lifespan min/median/max: 34/105/1008; tracks with internal gaps: 18; total internal gaps: 273; longest internal gap: 216; tracks ending in coasting: 36 (trailing rows total 3405)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..1008 | 1008 | 1008 | 979 | 29 | 7 | 21 | 0 | 78911 |
| 1 | 22..83 | 62 | 62 | 0 | 62 | 0 | 0 | 62 | - |
| 4 | 79..558 | 480 | 480 | 182 | 298 | 54 | 53 | 58 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 5 | 87..148 | 62 | 62 | 0 | 62 | 0 | 0 | 62 | - |
| 9 | 138..273 | 136 | 136 | 49 | 87 | 13 | 3 | 68 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 150..214 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 12 | 160..525 | 366 | 366 | 167 | 199 | 46 | 29 | 64 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 175..333 | 159 | 159 | 67 | 92 | 17 | 3 | 66 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 187..465 | 279 | 279 | 67 | 212 | 14 | 4 | 192 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 203..573 | 371 | 371 | 80 | 291 | 12 | 200 | 35 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 24 | 233..649 | 417 | 417 | 56 | 361 | 10 | 216 | 116 | 79115, 79116, 79122, 79134, 79135, 79136 |
| 25 | 239..572 | 334 | 334 | 24 | 310 | 7 | 180 | 30 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 26 | 242..339 | 98 | 98 | 30 | 68 | 5 | 2 | 62 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 29 | 265..671 | 407 | 407 | 34 | 373 | 10 | 163 | 132 | 79134, 79135, 79136, 79139 |
| 30 | 268..405 | 138 | 138 | 25 | 113 | 10 | 73 | 20 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79134 |
| 33 | 275..673 | 399 | 399 | 0 | 399 | 0 | 0 | 399 | - |
| 34 | 277..514 | 238 | 238 | 0 | 238 | 0 | 0 | 238 | - |
| 36 | 281..351 | 71 | 71 | 37 | 34 | 12 | 6 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122 |
| 38 | 297..401 | 105 | 105 | 31 | 74 | 12 | 25 | 32 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132 |
| 39 | 297..660 | 364 | 364 | 0 | 364 | 0 | 0 | 364 | - |
| 41 | 300..397 | 98 | 98 | 32 | 66 | 6 | 1 | 60 | 79103, 79108, 79110, 79111, 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 47 | 346..413 | 68 | 68 | 32 | 36 | 11 | 4 | 18 | 78897, 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79128 |
| 49 | 363..501 | 139 | 139 | 28 | 111 | 12 | 22 | 53 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 50 | 370..520 | 151 | 151 | 67 | 84 | 15 | 8 | 56 | 78897, 78899, 79037, 79045, 79097, 79098, 79102 |
| 54 | 388..545 | 158 | 158 | 0 | 158 | 0 | 0 | 158 | - |
| 59 | 409..662 | 254 | 254 | 0 | 254 | 0 | 0 | 254 | - |
| 64 | 466..535 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 65 | 472..554 | 83 | 83 | 0 | 83 | 0 | 0 | 83 | - |
| 72 | 529..596 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 73 | 529..605 | 77 | 77 | 0 | 77 | 0 | 0 | 77 | - |
| 84 | 592..655 | 64 | 64 | 0 | 64 | 0 | 0 | 64 | - |
| 92 | 656..724 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 97 | 720..787 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 103 | 785..853 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 111 | 847..915 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 121 | 912..978 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 130 | 975..1008 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
