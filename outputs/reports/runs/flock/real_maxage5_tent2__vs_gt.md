# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 5, "tentative_threshold": 2}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=2d7bd1d230eb git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage5_tent2/tracks.csv sha256=3e65f60d2fcc6cf8
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage5_tent2
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
| observations | none | 4 | 10142 | 4245 | 0.246 | 0.099 | 0.623 | 1.01 | 0.264 | -0.159 | 1.03 | 110 | 264.0 | 0.158 | 0.268 | 0.112 | 0.135 | 0.323 | 1370 | 8772 | 2875 | 1 | 0 | 24 |
| observations | none | 6 | 10142 | 4245 | 0.259 | 0.112 | 0.608 | 1.41 | 0.271 | -0.132 | 1.42 | 146 | 351.0 | 0.167 | 0.282 | 0.118 | 0.150 | 0.359 | 1524 | 8618 | 2721 | 1 | 1 | 23 |
| observations | none | 8 | 10142 | 4245 | 0.266 | 0.124 | 0.588 | 1.90 | 0.273 | -0.114 | 1.79 | 175 | 413.0 | 0.171 | 0.290 | 0.122 | 0.161 | 0.385 | 1634 | 8508 | 2611 | 1 | 1 | 23 |
| observations | none | 12 | 10142 | 4245 | 0.275 | 0.138 | 0.565 | 2.57 | 0.279 | -0.068 | 2.91 | 190 | 476.0 | 0.189 | 0.319 | 0.134 | 0.185 | 0.441 | 1873 | 8269 | 2372 | 1 | 2 | 22 |
| observations | ignore | 4 | 10142 | 3831 | 0.250 | 0.102 | 0.623 | 1.01 | 0.268 | -0.118 | 1.03 | 110 | 264.0 | 0.163 | 0.297 | 0.112 | 0.135 | 0.358 | 1370 | 8772 | 2461 | 1 | 0 | 24 |
| observations | ignore | 6 | 10142 | 3831 | 0.263 | 0.116 | 0.608 | 1.41 | 0.275 | -0.092 | 1.42 | 146 | 351.0 | 0.171 | 0.313 | 0.118 | 0.150 | 0.398 | 1524 | 8618 | 2307 | 1 | 1 | 23 |
| observations | ignore | 8 | 10142 | 3831 | 0.271 | 0.128 | 0.588 | 1.90 | 0.278 | -0.073 | 1.79 | 175 | 413.0 | 0.176 | 0.322 | 0.122 | 0.161 | 0.427 | 1634 | 8508 | 2197 | 1 | 1 | 23 |
| observations | ignore | 12 | 10142 | 3831 | 0.279 | 0.142 | 0.565 | 2.57 | 0.284 | -0.027 | 2.91 | 190 | 476.0 | 0.194 | 0.354 | 0.134 | 0.185 | 0.489 | 1873 | 8269 | 1958 | 1 | 2 | 22 |
| updates | none | 4 | 10142 | 5207 | 0.239 | 0.097 | 0.600 | 1.09 | 0.255 | -0.245 | 1.09 | 131 | 296.0 | 0.149 | 0.220 | 0.113 | 0.141 | 0.274 | 1425 | 8717 | 3782 | 1 | 0 | 24 |
| updates | none | 6 | 10142 | 5207 | 0.251 | 0.113 | 0.576 | 1.58 | 0.263 | -0.210 | 1.55 | 168 | 378.0 | 0.159 | 0.234 | 0.120 | 0.160 | 0.311 | 1621 | 8521 | 3586 | 1 | 1 | 23 |
| updates | none | 8 | 10142 | 5207 | 0.259 | 0.126 | 0.552 | 2.11 | 0.266 | -0.180 | 2.07 | 196 | 437.0 | 0.164 | 0.242 | 0.124 | 0.177 | 0.344 | 1791 | 8351 | 3416 | 1 | 1 | 23 |
| updates | none | 12 | 10142 | 5207 | 0.268 | 0.142 | 0.524 | 2.88 | 0.272 | -0.122 | 3.28 | 211 | 485.0 | 0.183 | 0.270 | 0.139 | 0.206 | 0.401 | 2088 | 8054 | 3119 | 1 | 3 | 21 |
| updates | ignore | 4 | 10142 | 4548 | 0.244 | 0.101 | 0.600 | 1.09 | 0.261 | -0.180 | 1.09 | 131 | 296.0 | 0.156 | 0.252 | 0.113 | 0.141 | 0.313 | 1425 | 8717 | 3123 | 1 | 0 | 24 |
| updates | ignore | 6 | 10142 | 4548 | 0.257 | 0.118 | 0.576 | 1.58 | 0.269 | -0.145 | 1.55 | 168 | 378.0 | 0.166 | 0.268 | 0.120 | 0.160 | 0.356 | 1621 | 8521 | 2927 | 1 | 1 | 23 |
| updates | ignore | 8 | 10142 | 4548 | 0.265 | 0.133 | 0.552 | 2.11 | 0.272 | -0.115 | 2.07 | 196 | 437.0 | 0.172 | 0.277 | 0.124 | 0.177 | 0.394 | 1791 | 8351 | 2757 | 1 | 1 | 23 |
| updates | ignore | 12 | 10142 | 4548 | 0.274 | 0.150 | 0.524 | 2.88 | 0.279 | -0.057 | 3.28 | 211 | 485.0 | 0.192 | 0.309 | 0.139 | 0.206 | 0.459 | 2088 | 8054 | 2460 | 1 | 3 | 21 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 118; matched pairs: 1634; unmatched reference entries: 8508; unmatched candidate entries: 2611
- identity switches: 175; fragmentation (coverage interruptions): 412; orphan candidate ids (never on a reference object): 86

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 3 at (1819, 3367), 24 frames after previous cover
- f166: ref 79139: 11 -> 14 at (1953.5, 3016), 5 frames after previous cover
- f173: ref 79135: 11 -> 14 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 11 -> 14 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 11 -> 14 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 14 -> 15 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 11 -> 14 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 14 -> 15 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 5 -> 11 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 14 -> 15 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 11 -> 14 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 15 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78971: 11 -> 14 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 14 -> 15 at (1777.5, 3018.5), 7 frames after previous cover
- f192: ref 78899: 14 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 5 -> 14 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 11 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 15 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 11 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 14 -> 5 at (1646.5, 3013), 25 frames after previous cover
- f202: ref 78899: 5 -> 21 at (1451.5, 3009.5), 3 frames after previous cover
- f203: ref 78897: 5 -> 21 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 79135: 17 -> 5 at (1685, 3007), 2 frames after previous cover
- f205: ref 79097: 5 -> 21 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 5 -> 17 at (1673, 3006), 2 frames after previous cover
- f207: ref 79134: 15 -> 17 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 15 -> 17 at (1625.5, 3010), 22 frames after previous cover
- f210: ref 79132: 5 -> 17 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 17 -> 5 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 17 -> 5 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 11 -> 17 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 17 -> 5 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 11 -> 17 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 14 -> 21 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 21 -> 17 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 17 -> 5 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 11 -> 5 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 17 -> 5 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 17 -> 5 at (1465, 3003), 7 frames after previous cover
- f221: ref 79139: 17 -> 5 at (1598, 2998.5), 24 frames after previous cover
- f223: ref 79135: 5 -> 27 at (1561.5, 2998), 12 frames after previous cover
- f224: ref 79139: 5 -> 27 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 21 -> 17 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 21 -> 17 at (1272, 2992), 12 frames after previous cover
- f227: ref 79045: 11 -> 17 at (1232, 2990.5), 44 frames after previous cover
- f227: ref 79105: 17 -> 5 at (1392, 2996), 13 frames after previous cover
- f228: ref 78899: 17 -> 29 at (1286.5, 2991.5), 3 frames after previous cover
- f228: ref 79103: 17 -> 5 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 14 -> 17 at (1202, 2988), 41 frames after previous cover
- f229: ref 79097: 17 -> 29 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 17 -> 27 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79128: 5 -> 27 at (1478, 2994), 16 frames after previous cover
- f232: ref 79115: 5 -> 27 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 5 -> 27 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 5 -> 27 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 79105: 5 -> 27 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 21 -> 29 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 29 -> 27 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 5 -> 14 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 79132: 5 -> 27 at (1404.5, 2987), 17 frames after previous cover
- ... 115 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 9 | 3 (971), 0 (4) |
| 78896 | 350 (76..429) | 11 | 9 | 5 (4), 14 (2), 40 (2), 68 (2), 56 (1) |
| 78969 | 352 (80..434) | 91 | 44 | 14 (54), 56 (12), 5 (11), 68 (8), 33 (3), 76 (2), 40 (1) |
| 78971 | 352 (84..439) | 17 | 11 | 68 (7), 14 (3), 76 (2), 5 (1), 11 (1), 17 (1), 48 (1), 56 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 48 (5), 56 (5), 68 (3), 14 (2), 11 (1), 17 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 56 (5), 14 (2), 33 (2), 68 (2), 11 (1), 21 (1), 29 (1), 32 (1), 48 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 68 (9), 56 (5), 21 (3), 33 (3), 48 (3), 11 (2), 5 (1), 17 (1) |
| 78899 | 365 (91..455) | 50 | 41 | 33 (15), 56 (7), 5 (6), 48 (6), 21 (5), 68 (5), 14 (2), 29 (2), 17 (1), 32 (1) |
| 79097 | 366 (94..461) | 69 | 44 | 33 (21), 48 (12), 17 (8), 29 (8), 21 (6), 68 (4), 56 (4), 79 (2), 11 (1), 5 (1), 35 (1), 50 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 79 (13), 48 (3), 56 (3), 37 (2), 29 (1), 27 (1), 33 (1) |
| 79102 | 371 (98..477) | 23 | 13 | 79 (15), 37 (5), 29 (2), 48 (1) |
| 79103 | 380 (99..481) | 19 | 12 | 37 (8), 48 (4), 29 (3), 11 (1), 17 (1), 5 (1), 33 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 17 (1), 5 (1), 27 (1), 48 (1), 82 (1), 37 (1) |
| 79108 | 385 (104..492) | 14 | 12 | 37 (4), 5 (2), 48 (2), 11 (1), 17 (1), 27 (1), 29 (1), 35 (1), 58 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 37 (8), 5 (2), 27 (2), 17 (1), 35 (1), 58 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 37 (5), 5 (2), 11 (1), 29 (1), 35 (1) |
| 79115 | 421 (111..531) | 8 | 7 | 5 (2), 27 (2), 17 (1), 66 (1), 22 (1), 91 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 91 (37), 22 (1) |
| 79122 | 404 (118..532) | 19 | 10 | 66 (10), 91 (8), 22 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 22 (56), 5 (3), 11 (1), 14 (1), 17 (1), 27 (1), 48 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 22 (4), 5 (3), 11 (2), 17 (2), 27 (2), 14 (1), 15 (1), 58 (1), 66 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 11 (5), 14 (4), 27 (3), 15 (2), 22 (2), 17 (1), 48 (1), 57 (1), 58 (1), 66 (1), 37 (1), 62 (1), +1 more |
| 79135 | 409 (129..542) | 50 | 42 | 37 (11), 17 (8), 11 (6), 22 (5), 27 (3), 15 (2), 5 (2), 35 (2), 66 (2), 88 (2), 14 (1), 54 (1), +5 more |
| 79139 | 406 (132..537) | 26 | 17 | 37 (7), 11 (3), 15 (3), 27 (3), 14 (2), 17 (2), 35 (2), 5 (1), 22 (1), 66 (1), 62 (1) |
| 79136 | 393 (136..538) | 4 | 3 | 14 (1), 43 (1), 37 (1), 91 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..24 | 3 | 0 | 3 |
| 2 | 24..30 | 7 | 0 | 3 |
| 4 | 31..31 | 1 | 0 | 1 |
| 6 | 87..89 | 3 | 0 | 3 |
| 7 | 92..92 | 1 | 0 | 1 |
| 8 | 99..99 | 1 | 0 | 1 |
| 12 | 149..154 | 6 | 0 | 3 |
| 13 | 150..155 | 6 | 0 | 4 |
| 16 | 175..175 | 1 | 0 | 1 |
| 20 | 199..209 | 11 | 0 | 9 |
| 25 | 213..216 | 4 | 0 | 3 |
| 26 | 216..222 | 7 | 0 | 6 |
| 28 | 224..233 | 10 | 0 | 10 |
| 30 | 233..412 | 180 | 0 | 167 |
| 31 | 239..412 | 174 | 0 | 153 |
| 34 | 249..258 | 10 | 0 | 10 |
| 38 | 268..301 | 34 | 0 | 21 |
| 41 | 274..290 | 17 | 0 | 16 |
| 44 | 277..387 | 111 | 0 | 103 |
| 45 | 278..284 | 7 | 0 | 6 |
| 47 | 297..338 | 42 | 0 | 28 |
| 49 | 299..311 | 13 | 0 | 11 |
| 52 | 324..335 | 12 | 0 | 12 |
| 55 | 329..332 | 4 | 0 | 4 |
| 60 | 340..346 | 7 | 0 | 6 |
| 63 | 343..347 | 5 | 0 | 5 |
| 64 | 349..360 | 12 | 0 | 11 |
| 67 | 364..438 | 75 | 0 | 62 |
| 70 | 374..384 | 11 | 0 | 11 |
| 72 | 388..421 | 34 | 0 | 31 |
| 74 | 399..401 | 3 | 0 | 3 |
| 75 | 402..408 | 7 | 0 | 6 |
| 78 | 409..614 | 206 | 0 | 183 |
| 81 | 424..433 | 10 | 0 | 10 |
| 84 | 449..449 | 1 | 0 | 1 |
| 85 | 450..456 | 7 | 0 | 6 |
| 86 | 450..474 | 25 | 0 | 17 |
| 89 | 464..470 | 7 | 0 | 6 |
| 90 | 466..476 | 11 | 0 | 5 |
| 92 | 472..472 | 1 | 0 | 1 |
| ... | 46 more | | | |

### Gaps and durations of candidate tracks
- tracks: 118; lifespan min/median/max: 1/10/978; tracks with internal gaps: 22; total internal gaps: 142; longest internal gap: 198; tracks ending in coasting: 103 (trailing rows total 1591)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..7 | 7 | 5 | 4 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 22..24 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 2 | 24..30 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 3 | 31..1008 | 978 | 976 | 971 | 5 | 4 | 2 | 0 | 78911 |
| 4 | 31..31 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 5 | 79..228 | 150 | 140 | 43 | 97 | 12 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79139 |
| 6 | 87..89 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 7 | 92..92 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 8 | 99..99 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 11 | 138..187 | 50 | 33 | 26 | 7 | 6 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 12 | 149..154 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 13 | 150..155 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 14 | 160..283 | 124 | 104 | 75 | 29 | 16 | 3 | 5 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 175..193 | 19 | 14 | 8 | 6 | 3 | 2 | 1 | 79128, 79134, 79135, 79139 |
| 16 | 175..175 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 17 | 187..229 | 43 | 41 | 31 | 10 | 8 | 2 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 20 | 199..209 | 11 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 21 | 202..216 | 15 | 15 | 15 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 22 | 203..514 | 312 | 301 | 71 | 230 | 8 | 198 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 25 | 213..216 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 26 | 216..222 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 27 | 223..246 | 24 | 19 | 19 | 0 | 0 | 0 | 0 | 79098, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 28 | 224..233 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 29 | 228..249 | 22 | 19 | 19 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 30 | 233..412 | 180 | 167 | 0 | 167 | 0 | 0 | 167 | - |
| 31 | 239..412 | 174 | 153 | 0 | 153 | 0 | 0 | 153 | - |
| 32 | 240..243 | 4 | 3 | 2 | 1 | 0 | 0 | 1 | 78899, 79037 |
| 33 | 242..321 | 80 | 70 | 46 | 24 | 6 | 4 | 14 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 34 | 249..258 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 35 | 258..269 | 12 | 8 | 8 | 0 | 0 | 0 | 0 | 79097, 79108, 79110, 79111, 79135, 79139 |
| 37 | 265..551 | 287 | 251 | 53 | 198 | 12 | 148 | 12 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79134, 79135, 79136, 79139 |
| 38 | 268..301 | 34 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 40 | 273..292 | 20 | 16 | 3 | 13 | 1 | 12 | 1 | 78896, 78969 |
| 41 | 274..290 | 17 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 43 | 275..493 | 219 | 185 | 2 | 183 | 2 | 168 | 7 | 79135, 79136 |
| 44 | 277..387 | 111 | 103 | 0 | 103 | 0 | 0 | 103 | - |
| 45 | 278..284 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 47 | 297..338 | 42 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 48 | 297..378 | 82 | 61 | 41 | 20 | 9 | 5 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79132, 79134 |
| 49 | 299..311 | 13 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 50 | 300..302 | 3 | 3 | 1 | 2 | 0 | 0 | 2 | 79097 |
| 52 | 324..335 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 54 | 328..328 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 79135 |
| 55 | 329..332 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 56 | 332..442 | 111 | 94 | 43 | 51 | 13 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 57 | 335..338 | 4 | 4 | 2 | 2 | 1 | 1 | 1 | 79134, 79135 |
| 58 | 339..351 | 13 | 11 | 5 | 6 | 4 | 2 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 60 | 340..346 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 62 | 342..444 | 103 | 76 | 3 | 73 | 1 | 72 | 1 | 79134, 79135, 79139 |
| 63 | 343..347 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 64 | 349..360 | 12 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 66 | 363..453 | 91 | 79 | 16 | 63 | 10 | 19 | 3 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 67 | 364..438 | 75 | 62 | 0 | 62 | 0 | 0 | 62 | - |
| 68 | 370..458 | 89 | 70 | 40 | 30 | 14 | 5 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 70 | 374..384 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 72 | 388..421 | 34 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 74 | 399..401 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 75 | 402..408 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 76 | 404..407 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 78 | 409..614 | 206 | 183 | 0 | 183 | 0 | 0 | 183 | - |
| 79 | 419..461 | 43 | 37 | 30 | 7 | 3 | 2 | 3 | 79097, 79098, 79102 |
| 80 | 420..471 | 52 | 45 | 1 | 44 | 0 | 0 | 44 | 79135 |
| 81 | 424..433 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 82 | 436..436 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 79105 |
| 84 | 449..449 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 85 | 450..456 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 86 | 450..474 | 25 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 88 | 463..605 | 143 | 125 | 2 | 123 | 2 | 2 | 120 | 79135 |
| 89 | 464..470 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 90 | 466..476 | 11 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 91 | 469..539 | 71 | 65 | 48 | 17 | 6 | 5 | 4 | 79115, 79116, 79122, 79134, 79136 |
| 92 | 472..472 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 93 | 474..483 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 95 | 484..486 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 102 | 499..508 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 103 | 502..505 | 4 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 104 | 514..565 | 52 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 106 | 524..535 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 107 | 526..532 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 109 | 529..546 | 18 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| ... | 38 more in JSON | | | | | | | | |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 65; matched pairs: 1634; unmatched reference entries: 8508; unmatched candidate entries: 2197
- identity switches: 175; fragmentation (coverage interruptions): 412; orphan candidate ids (never on a reference object): 33

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 3 at (1819, 3367), 24 frames after previous cover
- f166: ref 79139: 11 -> 14 at (1953.5, 3016), 5 frames after previous cover
- f173: ref 79135: 11 -> 14 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 11 -> 14 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 11 -> 14 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 14 -> 15 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 11 -> 14 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 14 -> 15 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 5 -> 11 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 14 -> 15 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 11 -> 14 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 15 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78971: 11 -> 14 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 14 -> 15 at (1777.5, 3018.5), 7 frames after previous cover
- f192: ref 78899: 14 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 5 -> 14 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 11 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 15 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 11 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 14 -> 5 at (1646.5, 3013), 25 frames after previous cover
- f202: ref 78899: 5 -> 21 at (1451.5, 3009.5), 3 frames after previous cover
- f203: ref 78897: 5 -> 21 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 79135: 17 -> 5 at (1685, 3007), 2 frames after previous cover
- f205: ref 79097: 5 -> 21 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 5 -> 17 at (1673, 3006), 2 frames after previous cover
- f207: ref 79134: 15 -> 17 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 15 -> 17 at (1625.5, 3010), 22 frames after previous cover
- f210: ref 79132: 5 -> 17 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 17 -> 5 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 17 -> 5 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 11 -> 17 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 17 -> 5 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 11 -> 17 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 14 -> 21 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 21 -> 17 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 17 -> 5 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 11 -> 5 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 17 -> 5 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 17 -> 5 at (1465, 3003), 7 frames after previous cover
- f221: ref 79139: 17 -> 5 at (1598, 2998.5), 24 frames after previous cover
- f223: ref 79135: 5 -> 27 at (1561.5, 2998), 12 frames after previous cover
- f224: ref 79139: 5 -> 27 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 21 -> 17 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 21 -> 17 at (1272, 2992), 12 frames after previous cover
- f227: ref 79045: 11 -> 17 at (1232, 2990.5), 44 frames after previous cover
- f227: ref 79105: 17 -> 5 at (1392, 2996), 13 frames after previous cover
- f228: ref 78899: 17 -> 29 at (1286.5, 2991.5), 3 frames after previous cover
- f228: ref 79103: 17 -> 5 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 14 -> 17 at (1202, 2988), 41 frames after previous cover
- f229: ref 79097: 17 -> 29 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 17 -> 27 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79128: 5 -> 27 at (1478, 2994), 16 frames after previous cover
- f232: ref 79115: 5 -> 27 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 5 -> 27 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 5 -> 27 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 79105: 5 -> 27 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 21 -> 29 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 29 -> 27 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 5 -> 14 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 79132: 5 -> 27 at (1404.5, 2987), 17 frames after previous cover
- ... 115 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 9 | 3 (971), 0 (4) |
| 78896 | 350 (76..429) | 11 | 9 | 5 (4), 14 (2), 40 (2), 68 (2), 56 (1) |
| 78969 | 352 (80..434) | 91 | 44 | 14 (54), 56 (12), 5 (11), 68 (8), 33 (3), 76 (2), 40 (1) |
| 78971 | 352 (84..439) | 17 | 11 | 68 (7), 14 (3), 76 (2), 5 (1), 11 (1), 17 (1), 48 (1), 56 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 48 (5), 56 (5), 68 (3), 14 (2), 11 (1), 17 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 56 (5), 14 (2), 33 (2), 68 (2), 11 (1), 21 (1), 29 (1), 32 (1), 48 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 68 (9), 56 (5), 21 (3), 33 (3), 48 (3), 11 (2), 5 (1), 17 (1) |
| 78899 | 365 (91..455) | 50 | 41 | 33 (15), 56 (7), 5 (6), 48 (6), 21 (5), 68 (5), 14 (2), 29 (2), 17 (1), 32 (1) |
| 79097 | 366 (94..461) | 69 | 44 | 33 (21), 48 (12), 17 (8), 29 (8), 21 (6), 68 (4), 56 (4), 79 (2), 11 (1), 5 (1), 35 (1), 50 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 79 (13), 48 (3), 56 (3), 37 (2), 29 (1), 27 (1), 33 (1) |
| 79102 | 371 (98..477) | 23 | 13 | 79 (15), 37 (5), 29 (2), 48 (1) |
| 79103 | 380 (99..481) | 19 | 12 | 37 (8), 48 (4), 29 (3), 11 (1), 17 (1), 5 (1), 33 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 17 (1), 5 (1), 27 (1), 48 (1), 82 (1), 37 (1) |
| 79108 | 385 (104..492) | 14 | 12 | 37 (4), 5 (2), 48 (2), 11 (1), 17 (1), 27 (1), 29 (1), 35 (1), 58 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 37 (8), 5 (2), 27 (2), 17 (1), 35 (1), 58 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 37 (5), 5 (2), 11 (1), 29 (1), 35 (1) |
| 79115 | 421 (111..531) | 8 | 7 | 5 (2), 27 (2), 17 (1), 66 (1), 22 (1), 91 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 91 (37), 22 (1) |
| 79122 | 404 (118..532) | 19 | 10 | 66 (10), 91 (8), 22 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 22 (56), 5 (3), 11 (1), 14 (1), 17 (1), 27 (1), 48 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 22 (4), 5 (3), 11 (2), 17 (2), 27 (2), 14 (1), 15 (1), 58 (1), 66 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 11 (5), 14 (4), 27 (3), 15 (2), 22 (2), 17 (1), 48 (1), 57 (1), 58 (1), 66 (1), 37 (1), 62 (1), +1 more |
| 79135 | 409 (129..542) | 50 | 42 | 37 (11), 17 (8), 11 (6), 22 (5), 27 (3), 15 (2), 5 (2), 35 (2), 66 (2), 88 (2), 14 (1), 54 (1), +5 more |
| 79139 | 406 (132..537) | 26 | 17 | 37 (7), 11 (3), 15 (3), 27 (3), 14 (2), 17 (2), 35 (2), 5 (1), 22 (1), 66 (1), 62 (1) |
| 79136 | 393 (136..538) | 4 | 3 | 14 (1), 43 (1), 37 (1), 91 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..24 | 3 | 0 | 3 |
| 6 | 87..89 | 3 | 0 | 3 |
| 13 | 150..155 | 6 | 0 | 4 |
| 25 | 213..216 | 4 | 0 | 3 |
| 30 | 233..412 | 180 | 0 | 167 |
| 31 | 239..412 | 174 | 0 | 153 |
| 38 | 268..301 | 34 | 0 | 21 |
| 44 | 277..387 | 111 | 0 | 103 |
| 47 | 297..338 | 42 | 0 | 28 |
| 55 | 329..332 | 4 | 0 | 4 |
| 63 | 343..347 | 5 | 0 | 5 |
| 67 | 364..438 | 75 | 0 | 62 |
| 72 | 388..421 | 34 | 0 | 31 |
| 78 | 409..614 | 206 | 0 | 183 |
| 86 | 450..474 | 25 | 0 | 17 |
| 90 | 466..476 | 11 | 0 | 5 |
| 92 | 472..472 | 1 | 0 | 1 |
| 95 | 484..486 | 3 | 0 | 3 |
| 103 | 502..505 | 4 | 0 | 2 |
| 104 | 514..565 | 52 | 0 | 46 |
| 109 | 529..546 | 18 | 0 | 13 |
| 111 | 529..537 | 9 | 0 | 6 |
| 116 | 557..585 | 29 | 0 | 29 |
| 118 | 573..607 | 35 | 0 | 27 |
| 124 | 592..596 | 5 | 0 | 5 |
| 133 | 656..665 | 10 | 0 | 10 |
| 139 | 720..721 | 2 | 0 | 2 |
| 142 | 728..728 | 1 | 0 | 1 |
| 146 | 785..794 | 10 | 0 | 5 |
| 154 | 847..848 | 2 | 0 | 2 |
| 158 | 855..856 | 2 | 0 | 2 |
| 165 | 912..919 | 8 | 0 | 4 |
| 174 | 975..981 | 7 | 0 | 5 |

### Gaps and durations of candidate tracks
- tracks: 65; lifespan min/median/max: 1/20/978; tracks with internal gaps: 22; total internal gaps: 142; longest internal gap: 198; tracks ending in coasting: 50 (trailing rows total 1177)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..7 | 7 | 5 | 4 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 22..24 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 3 | 31..1008 | 978 | 976 | 971 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 79..228 | 150 | 140 | 43 | 97 | 12 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79139 |
| 6 | 87..89 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 11 | 138..187 | 50 | 33 | 26 | 7 | 6 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 13 | 150..155 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 14 | 160..283 | 124 | 104 | 75 | 29 | 16 | 3 | 5 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 175..193 | 19 | 14 | 8 | 6 | 3 | 2 | 1 | 79128, 79134, 79135, 79139 |
| 17 | 187..229 | 43 | 41 | 31 | 10 | 8 | 2 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 21 | 202..216 | 15 | 15 | 15 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 22 | 203..514 | 312 | 301 | 71 | 230 | 8 | 198 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 25 | 213..216 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 27 | 223..246 | 24 | 19 | 19 | 0 | 0 | 0 | 0 | 79098, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 29 | 228..249 | 22 | 19 | 19 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 30 | 233..412 | 180 | 167 | 0 | 167 | 0 | 0 | 167 | - |
| 31 | 239..412 | 174 | 153 | 0 | 153 | 0 | 0 | 153 | - |
| 32 | 240..243 | 4 | 3 | 2 | 1 | 0 | 0 | 1 | 78899, 79037 |
| 33 | 242..321 | 80 | 70 | 46 | 24 | 6 | 4 | 14 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 35 | 258..269 | 12 | 8 | 8 | 0 | 0 | 0 | 0 | 79097, 79108, 79110, 79111, 79135, 79139 |
| 37 | 265..551 | 287 | 251 | 53 | 198 | 12 | 148 | 12 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79134, 79135, 79136, 79139 |
| 38 | 268..301 | 34 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 40 | 273..292 | 20 | 16 | 3 | 13 | 1 | 12 | 1 | 78896, 78969 |
| 43 | 275..493 | 219 | 185 | 2 | 183 | 2 | 168 | 7 | 79135, 79136 |
| 44 | 277..387 | 111 | 103 | 0 | 103 | 0 | 0 | 103 | - |
| 47 | 297..338 | 42 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 48 | 297..378 | 82 | 61 | 41 | 20 | 9 | 5 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79132, 79134 |
| 50 | 300..302 | 3 | 3 | 1 | 2 | 0 | 0 | 2 | 79097 |
| 54 | 328..328 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 79135 |
| 55 | 329..332 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 56 | 332..442 | 111 | 94 | 43 | 51 | 13 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 57 | 335..338 | 4 | 4 | 2 | 2 | 1 | 1 | 1 | 79134, 79135 |
| 58 | 339..351 | 13 | 11 | 5 | 6 | 4 | 2 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 62 | 342..444 | 103 | 76 | 3 | 73 | 1 | 72 | 1 | 79134, 79135, 79139 |
| 63 | 343..347 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 66 | 363..453 | 91 | 79 | 16 | 63 | 10 | 19 | 3 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 67 | 364..438 | 75 | 62 | 0 | 62 | 0 | 0 | 62 | - |
| 68 | 370..458 | 89 | 70 | 40 | 30 | 14 | 5 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097 |
| 72 | 388..421 | 34 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 76 | 404..407 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 78 | 409..614 | 206 | 183 | 0 | 183 | 0 | 0 | 183 | - |
| 79 | 419..461 | 43 | 37 | 30 | 7 | 3 | 2 | 3 | 79097, 79098, 79102 |
| 80 | 420..471 | 52 | 45 | 1 | 44 | 0 | 0 | 44 | 79135 |
| 82 | 436..436 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 79105 |
| 86 | 450..474 | 25 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 88 | 463..605 | 143 | 125 | 2 | 123 | 2 | 2 | 120 | 79135 |
| 90 | 466..476 | 11 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 91 | 469..539 | 71 | 65 | 48 | 17 | 6 | 5 | 4 | 79115, 79116, 79122, 79134, 79136 |
| 92 | 472..472 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 95 | 484..486 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 103 | 502..505 | 4 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 104 | 514..565 | 52 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 109 | 529..546 | 18 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 111 | 529..537 | 9 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 116 | 557..585 | 29 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 118 | 573..607 | 35 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 124 | 592..596 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 133 | 656..665 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 139 | 720..721 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 142 | 728..728 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 146 | 785..794 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 154 | 847..848 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 158 | 855..856 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 165 | 912..919 | 8 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 174 | 975..981 | 7 | 5 | 0 | 5 | 0 | 0 | 5 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 118; matched pairs: 1791; unmatched reference entries: 8351; unmatched candidate entries: 3416
- identity switches: 196; fragmentation (coverage interruptions): 434; orphan candidate ids (never on a reference object): 86

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 3 at (1819, 3367), 23 frames after previous cover
- f161: ref 79136: 11 -> 14 at (2010, 3014.5), 20 frames after previous cover
- f166: ref 79139: 11 -> 14 at (1953.5, 3016), 4 frames after previous cover
- f173: ref 79135: 11 -> 14 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 11 -> 14 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 11 -> 14 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 14 -> 15 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 11 -> 14 at (1812, 3020), 3 frames after previous cover
- f178: ref 79136: 14 -> 15 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 14 -> 15 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 5 -> 11 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 14 -> 15 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 11 -> 14 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 15 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78969: 5 -> 11 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 11 -> 14 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 14 -> 15 at (1777.5, 3018.5), 6 frames after previous cover
- f190: ref 79045: 11 -> 14 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 17 -> 15 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 14 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 11 -> 14 at (1414, 3008.5), 3 frames after previous cover
- f193: ref 79135: 15 -> 17 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 11 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 15 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 11 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 14 -> 5 at (1646.5, 3013), 25 frames after previous cover
- f202: ref 78899: 5 -> 21 at (1451.5, 3009.5), 3 frames after previous cover
- f203: ref 78897: 5 -> 21 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 79135: 17 -> 5 at (1685, 3007), 2 frames after previous cover
- f204: ref 79136: 15 -> 17 at (1731, 3016), 22 frames after previous cover
- f205: ref 79097: 5 -> 21 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 5 -> 17 at (1673, 3006), 2 frames after previous cover
- f206: ref 79139: 17 -> 5 at (1693.5, 3007.5), 9 frames after previous cover
- f207: ref 79134: 15 -> 17 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 15 -> 17 at (1625.5, 3010), 12 frames after previous cover
- f209: ref 79136: 17 -> 5 at (1698.5, 3013.5), 5 frames after previous cover
- f210: ref 79132: 5 -> 17 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 17 -> 5 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 17 -> 5 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 11 -> 17 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 17 -> 5 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 11 -> 17 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 14 -> 21 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 21 -> 17 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 17 -> 5 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 11 -> 5 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 17 -> 5 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 17 -> 5 at (1465, 3003), 7 frames after previous cover
- f223: ref 79135: 5 -> 27 at (1561.5, 2998), 12 frames after previous cover
- f224: ref 79139: 5 -> 27 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 21 -> 17 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 21 -> 17 at (1272, 2992), 7 frames after previous cover
- f227: ref 79045: 14 -> 17 at (1232, 2990.5), 36 frames after previous cover
- f227: ref 79105: 17 -> 5 at (1392, 2996), 13 frames after previous cover
- f227: ref 79136: 5 -> 27 at (1580, 3002), 17 frames after previous cover
- f228: ref 78899: 17 -> 29 at (1286.5, 2991.5), 3 frames after previous cover
- f228: ref 79103: 17 -> 5 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 14 -> 17 at (1202, 2988), 40 frames after previous cover
- f229: ref 79097: 17 -> 29 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 17 -> 27 at (1505.5, 3001), 23 frames after previous cover
- ... 136 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 7 | 3 (973), 0 (5) |
| 78896 | 350 (76..429) | 13 | 9 | 5 (5), 40 (3), 14 (2), 68 (2), 56 (1) |
| 78969 | 352 (80..434) | 103 | 45 | 14 (54), 68 (13), 5 (12), 56 (12), 76 (4), 40 (3), 33 (3), 11 (2) |
| 78971 | 352 (84..439) | 24 | 12 | 68 (8), 14 (4), 32 (3), 17 (2), 76 (2), 56 (2), 5 (1), 11 (1), 48 (1) |
| 79045 | 355 (84..443) | 29 | 13 | 48 (8), 56 (6), 17 (5), 14 (4), 68 (4), 11 (1), 32 (1) |
| 79037 | 355 (86..445) | 21 | 16 | 56 (6), 48 (4), 14 (2), 32 (2), 33 (2), 68 (2), 11 (1), 21 (1), 29 (1) |
| 78897 | 345 (89..450) | 35 | 22 | 68 (11), 56 (7), 21 (5), 48 (5), 33 (3), 11 (2), 5 (1), 17 (1) |
| 78899 | 365 (91..455) | 57 | 40 | 33 (17), 56 (10), 5 (6), 48 (6), 68 (6), 21 (5), 14 (3), 29 (2), 17 (1), 32 (1) |
| 79097 | 366 (94..461) | 73 | 44 | 33 (21), 48 (13), 17 (8), 29 (8), 21 (6), 56 (6), 68 (5), 79 (2), 11 (1), 5 (1), 35 (1), 50 (1) |
| 79098 | 360 (97..467) | 29 | 19 | 79 (15), 56 (4), 48 (3), 68 (3), 29 (1), 27 (1), 33 (1), 37 (1) |
| 79102 | 371 (98..477) | 25 | 12 | 79 (16), 37 (5), 29 (3), 48 (1) |
| 79103 | 380 (99..481) | 27 | 12 | 37 (10), 29 (8), 48 (5), 11 (1), 17 (1), 5 (1), 33 (1) |
| 79105 | 379 (101..484) | 10 | 7 | 5 (3), 27 (2), 17 (1), 29 (1), 48 (1), 82 (1), 37 (1) |
| 79108 | 385 (104..492) | 21 | 13 | 37 (5), 58 (3), 11 (2), 5 (2), 35 (2), 48 (2), 82 (2), 17 (1), 27 (1), 29 (1) |
| 79110 | 388 (106..497) | 18 | 10 | 37 (8), 58 (3), 5 (2), 27 (2), 35 (2), 17 (1) |
| 79111 | 386 (109..500) | 13 | 6 | 37 (6), 5 (2), 27 (2), 11 (1), 29 (1), 35 (1) |
| 79115 | 421 (111..531) | 12 | 10 | 27 (4), 5 (2), 48 (2), 17 (1), 66 (1), 22 (1), 91 (1) |
| 79116 | 411 (114..530) | 39 | 8 | 91 (37), 22 (2) |
| 79122 | 404 (118..532) | 22 | 12 | 66 (10), 91 (10), 11 (1), 22 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 22 (57), 5 (3), 11 (1), 14 (1), 17 (1), 27 (1), 48 (1) |
| 79128 | 402 (124..527) | 21 | 15 | 22 (4), 11 (3), 15 (3), 5 (3), 17 (2), 27 (2), 66 (2), 14 (1), 58 (1) |
| 79134 | 407 (127..533) | 31 | 22 | 11 (7), 14 (5), 15 (4), 27 (3), 66 (3), 22 (2), 17 (1), 48 (1), 57 (1), 58 (1), 37 (1), 62 (1), +1 more |
| 79135 | 409 (129..542) | 64 | 40 | 37 (15), 11 (9), 17 (7), 22 (6), 88 (4), 14 (3), 27 (3), 66 (3), 15 (2), 5 (2), 35 (2), 80 (2), +5 more |
| 79139 | 406 (132..537) | 40 | 19 | 37 (8), 11 (5), 35 (5), 27 (4), 15 (3), 5 (3), 54 (3), 22 (3), 14 (2), 17 (2), 66 (1), 62 (1) |
| 79136 | 393 (136..538) | 21 | 12 | 14 (6), 35 (3), 15 (2), 5 (2), 27 (2), 91 (2), 11 (1), 17 (1), 43 (1), 37 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..28 | 7 | 0 | 7 |
| 2 | 24..34 | 11 | 0 | 11 |
| 4 | 31..35 | 5 | 0 | 5 |
| 6 | 87..93 | 7 | 0 | 7 |
| 7 | 92..96 | 5 | 0 | 5 |
| 8 | 99..103 | 5 | 0 | 5 |
| 12 | 149..158 | 10 | 0 | 10 |
| 13 | 150..159 | 10 | 0 | 10 |
| 16 | 175..179 | 5 | 0 | 5 |
| 20 | 199..213 | 15 | 0 | 15 |
| 25 | 213..220 | 8 | 0 | 8 |
| 26 | 216..226 | 11 | 0 | 11 |
| 28 | 224..237 | 14 | 0 | 14 |
| 30 | 233..416 | 184 | 0 | 184 |
| 31 | 239..416 | 178 | 0 | 178 |
| 34 | 249..262 | 14 | 0 | 14 |
| 38 | 268..305 | 38 | 0 | 38 |
| 41 | 274..294 | 21 | 0 | 21 |
| 44 | 277..391 | 115 | 0 | 115 |
| 45 | 278..288 | 11 | 0 | 11 |
| 47 | 297..342 | 46 | 0 | 46 |
| 49 | 299..315 | 17 | 0 | 17 |
| 52 | 324..339 | 16 | 0 | 16 |
| 55 | 329..336 | 8 | 0 | 8 |
| 60 | 340..350 | 11 | 0 | 11 |
| 63 | 343..351 | 9 | 0 | 9 |
| 64 | 349..364 | 16 | 0 | 16 |
| 67 | 364..442 | 79 | 0 | 79 |
| 70 | 374..388 | 15 | 0 | 15 |
| 72 | 388..425 | 38 | 0 | 38 |
| 74 | 399..405 | 7 | 0 | 7 |
| 75 | 402..412 | 11 | 0 | 11 |
| 78 | 409..618 | 210 | 0 | 210 |
| 81 | 424..437 | 14 | 0 | 14 |
| 84 | 449..453 | 5 | 0 | 5 |
| 85 | 450..460 | 11 | 0 | 11 |
| 86 | 450..478 | 29 | 0 | 29 |
| 89 | 464..474 | 11 | 0 | 11 |
| 90 | 466..480 | 15 | 0 | 15 |
| 92 | 472..476 | 5 | 0 | 5 |
| ... | 46 more | | | |

### Gaps and durations of candidate tracks
- tracks: 118; lifespan min/median/max: 5/14/978; tracks with internal gaps: 27; total internal gaps: 187; longest internal gap: 201; tracks ending in coasting: 107 (trailing rows total 2210)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..11 | 11 | 11 | 5 | 6 | 2 | 2 | 3 | 78911 |
| 1 | 22..28 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 2 | 24..34 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 3 | 31..1008 | 978 | 978 | 973 | 5 | 4 | 2 | 0 | 78911 |
| 4 | 31..35 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 5 | 79..232 | 154 | 154 | 51 | 103 | 15 | 53 | 1 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79136, 79139 |
| 6 | 87..93 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 7 | 92..96 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 8 | 99..103 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 11 | 138..191 | 54 | 54 | 39 | 15 | 10 | 2 | 2 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 12 | 149..158 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 13 | 150..159 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 14 | 160..287 | 128 | 128 | 87 | 41 | 20 | 3 | 14 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 175..197 | 23 | 23 | 14 | 9 | 5 | 3 | 1 | 79128, 79134, 79135, 79136, 79139 |
| 16 | 175..179 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 17 | 187..233 | 47 | 47 | 36 | 11 | 8 | 3 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 199..213 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 21 | 202..220 | 19 | 19 | 17 | 2 | 1 | 1 | 1 | 78897, 78899, 79037, 79097 |
| 22 | 203..518 | 316 | 316 | 76 | 240 | 10 | 200 | 3 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 25 | 213..220 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 26 | 216..226 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 27 | 223..250 | 28 | 28 | 27 | 1 | 1 | 1 | 0 | 79098, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 28 | 224..237 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 29 | 228..253 | 26 | 26 | 26 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 30 | 233..416 | 184 | 184 | 0 | 184 | 0 | 0 | 184 | - |
| 31 | 239..416 | 178 | 178 | 0 | 178 | 0 | 0 | 178 | - |
| 32 | 240..247 | 8 | 8 | 7 | 1 | 1 | 1 | 0 | 78899, 78971, 79037, 79045 |
| 33 | 242..325 | 84 | 84 | 48 | 36 | 10 | 8 | 18 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 34 | 249..262 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 35 | 258..273 | 16 | 16 | 16 | 0 | 0 | 0 | 0 | 79097, 79108, 79110, 79111, 79135, 79136, 79139 |
| 37 | 265..555 | 291 | 291 | 61 | 230 | 16 | 163 | 16 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79134, 79135, 79136, 79139 |
| 38 | 268..305 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 40 | 273..296 | 24 | 24 | 6 | 18 | 2 | 12 | 5 | 78896, 78969 |
| 41 | 274..294 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 43 | 275..497 | 223 | 223 | 3 | 220 | 2 | 201 | 11 | 79135, 79136 |
| 44 | 277..391 | 115 | 115 | 0 | 115 | 0 | 0 | 115 | - |
| 45 | 278..288 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 47 | 297..342 | 46 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 48 | 297..382 | 86 | 86 | 53 | 33 | 11 | 11 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79132, 79134 |
| 49 | 299..315 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 50 | 300..306 | 7 | 7 | 1 | 6 | 0 | 0 | 6 | 79097 |
| 52 | 324..339 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 54 | 328..332 | 5 | 5 | 4 | 1 | 0 | 0 | 1 | 79135, 79139 |
| 55 | 329..336 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 56 | 332..446 | 115 | 115 | 54 | 61 | 18 | 16 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 57 | 335..342 | 8 | 8 | 2 | 6 | 1 | 1 | 5 | 79134, 79135 |
| 58 | 339..355 | 17 | 17 | 9 | 8 | 4 | 3 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 60 | 340..350 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 62 | 342..448 | 107 | 107 | 3 | 104 | 1 | 99 | 5 | 79134, 79135, 79139 |
| 63 | 343..351 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 64 | 349..364 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 66 | 363..457 | 95 | 95 | 20 | 75 | 10 | 23 | 7 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 67 | 364..442 | 79 | 79 | 0 | 79 | 0 | 0 | 79 | - |
| 68 | 370..462 | 93 | 93 | 54 | 39 | 19 | 5 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 70 | 374..388 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 72 | 388..425 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 74 | 399..405 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 75 | 402..412 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 76 | 404..411 | 8 | 8 | 6 | 2 | 1 | 1 | 1 | 78969, 78971 |
| 78 | 409..618 | 210 | 210 | 0 | 210 | 0 | 0 | 210 | - |
| 79 | 419..465 | 47 | 47 | 33 | 14 | 5 | 8 | 1 | 79097, 79098, 79102 |
| 80 | 420..475 | 56 | 56 | 2 | 54 | 0 | 0 | 54 | 79135 |
| 81 | 424..437 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 82 | 436..440 | 5 | 5 | 3 | 2 | 1 | 2 | 0 | 79105, 79108 |
| 84 | 449..453 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 85 | 450..460 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 86 | 450..478 | 29 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 88 | 463..609 | 147 | 147 | 4 | 143 | 2 | 3 | 139 | 79135 |
| 89 | 464..474 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 90 | 466..480 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 91 | 469..543 | 75 | 75 | 51 | 24 | 7 | 5 | 10 | 79115, 79116, 79122, 79134, 79136 |
| 92 | 472..476 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 93 | 474..487 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 95 | 484..490 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 102 | 499..512 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 103 | 502..509 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 104 | 514..569 | 56 | 56 | 0 | 56 | 0 | 0 | 56 | - |
| 106 | 524..539 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 107 | 526..536 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 109 | 529..550 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| ... | 38 more in JSON | | | | | | | | |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 65; matched pairs: 1791; unmatched reference entries: 8351; unmatched candidate entries: 2757
- identity switches: 196; fragmentation (coverage interruptions): 434; orphan candidate ids (never on a reference object): 33

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 3 at (1819, 3367), 23 frames after previous cover
- f161: ref 79136: 11 -> 14 at (2010, 3014.5), 20 frames after previous cover
- f166: ref 79139: 11 -> 14 at (1953.5, 3016), 4 frames after previous cover
- f173: ref 79135: 11 -> 14 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 11 -> 14 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 11 -> 14 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 14 -> 15 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 11 -> 14 at (1812, 3020), 3 frames after previous cover
- f178: ref 79136: 14 -> 15 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 14 -> 15 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 5 -> 11 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 14 -> 15 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 11 -> 14 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 15 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78969: 5 -> 11 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 11 -> 14 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 14 -> 15 at (1777.5, 3018.5), 6 frames after previous cover
- f190: ref 79045: 11 -> 14 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 17 -> 15 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 14 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 11 -> 14 at (1414, 3008.5), 3 frames after previous cover
- f193: ref 79135: 15 -> 17 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 11 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 15 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 11 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 14 -> 5 at (1646.5, 3013), 25 frames after previous cover
- f202: ref 78899: 5 -> 21 at (1451.5, 3009.5), 3 frames after previous cover
- f203: ref 78897: 5 -> 21 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 79135: 17 -> 5 at (1685, 3007), 2 frames after previous cover
- f204: ref 79136: 15 -> 17 at (1731, 3016), 22 frames after previous cover
- f205: ref 79097: 5 -> 21 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 5 -> 17 at (1673, 3006), 2 frames after previous cover
- f206: ref 79139: 17 -> 5 at (1693.5, 3007.5), 9 frames after previous cover
- f207: ref 79134: 15 -> 17 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 15 -> 17 at (1625.5, 3010), 12 frames after previous cover
- f209: ref 79136: 17 -> 5 at (1698.5, 3013.5), 5 frames after previous cover
- f210: ref 79132: 5 -> 17 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 17 -> 5 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 17 -> 5 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 11 -> 17 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 17 -> 5 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 11 -> 17 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 14 -> 21 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 21 -> 17 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 17 -> 5 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 11 -> 5 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 17 -> 5 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 17 -> 5 at (1465, 3003), 7 frames after previous cover
- f223: ref 79135: 5 -> 27 at (1561.5, 2998), 12 frames after previous cover
- f224: ref 79139: 5 -> 27 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 21 -> 17 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 21 -> 17 at (1272, 2992), 7 frames after previous cover
- f227: ref 79045: 14 -> 17 at (1232, 2990.5), 36 frames after previous cover
- f227: ref 79105: 17 -> 5 at (1392, 2996), 13 frames after previous cover
- f227: ref 79136: 5 -> 27 at (1580, 3002), 17 frames after previous cover
- f228: ref 78899: 17 -> 29 at (1286.5, 2991.5), 3 frames after previous cover
- f228: ref 79103: 17 -> 5 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 14 -> 17 at (1202, 2988), 40 frames after previous cover
- f229: ref 79097: 17 -> 29 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 17 -> 27 at (1505.5, 3001), 23 frames after previous cover
- ... 136 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 7 | 3 (973), 0 (5) |
| 78896 | 350 (76..429) | 13 | 9 | 5 (5), 40 (3), 14 (2), 68 (2), 56 (1) |
| 78969 | 352 (80..434) | 103 | 45 | 14 (54), 68 (13), 5 (12), 56 (12), 76 (4), 40 (3), 33 (3), 11 (2) |
| 78971 | 352 (84..439) | 24 | 12 | 68 (8), 14 (4), 32 (3), 17 (2), 76 (2), 56 (2), 5 (1), 11 (1), 48 (1) |
| 79045 | 355 (84..443) | 29 | 13 | 48 (8), 56 (6), 17 (5), 14 (4), 68 (4), 11 (1), 32 (1) |
| 79037 | 355 (86..445) | 21 | 16 | 56 (6), 48 (4), 14 (2), 32 (2), 33 (2), 68 (2), 11 (1), 21 (1), 29 (1) |
| 78897 | 345 (89..450) | 35 | 22 | 68 (11), 56 (7), 21 (5), 48 (5), 33 (3), 11 (2), 5 (1), 17 (1) |
| 78899 | 365 (91..455) | 57 | 40 | 33 (17), 56 (10), 5 (6), 48 (6), 68 (6), 21 (5), 14 (3), 29 (2), 17 (1), 32 (1) |
| 79097 | 366 (94..461) | 73 | 44 | 33 (21), 48 (13), 17 (8), 29 (8), 21 (6), 56 (6), 68 (5), 79 (2), 11 (1), 5 (1), 35 (1), 50 (1) |
| 79098 | 360 (97..467) | 29 | 19 | 79 (15), 56 (4), 48 (3), 68 (3), 29 (1), 27 (1), 33 (1), 37 (1) |
| 79102 | 371 (98..477) | 25 | 12 | 79 (16), 37 (5), 29 (3), 48 (1) |
| 79103 | 380 (99..481) | 27 | 12 | 37 (10), 29 (8), 48 (5), 11 (1), 17 (1), 5 (1), 33 (1) |
| 79105 | 379 (101..484) | 10 | 7 | 5 (3), 27 (2), 17 (1), 29 (1), 48 (1), 82 (1), 37 (1) |
| 79108 | 385 (104..492) | 21 | 13 | 37 (5), 58 (3), 11 (2), 5 (2), 35 (2), 48 (2), 82 (2), 17 (1), 27 (1), 29 (1) |
| 79110 | 388 (106..497) | 18 | 10 | 37 (8), 58 (3), 5 (2), 27 (2), 35 (2), 17 (1) |
| 79111 | 386 (109..500) | 13 | 6 | 37 (6), 5 (2), 27 (2), 11 (1), 29 (1), 35 (1) |
| 79115 | 421 (111..531) | 12 | 10 | 27 (4), 5 (2), 48 (2), 17 (1), 66 (1), 22 (1), 91 (1) |
| 79116 | 411 (114..530) | 39 | 8 | 91 (37), 22 (2) |
| 79122 | 404 (118..532) | 22 | 12 | 66 (10), 91 (10), 11 (1), 22 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 22 (57), 5 (3), 11 (1), 14 (1), 17 (1), 27 (1), 48 (1) |
| 79128 | 402 (124..527) | 21 | 15 | 22 (4), 11 (3), 15 (3), 5 (3), 17 (2), 27 (2), 66 (2), 14 (1), 58 (1) |
| 79134 | 407 (127..533) | 31 | 22 | 11 (7), 14 (5), 15 (4), 27 (3), 66 (3), 22 (2), 17 (1), 48 (1), 57 (1), 58 (1), 37 (1), 62 (1), +1 more |
| 79135 | 409 (129..542) | 64 | 40 | 37 (15), 11 (9), 17 (7), 22 (6), 88 (4), 14 (3), 27 (3), 66 (3), 15 (2), 5 (2), 35 (2), 80 (2), +5 more |
| 79139 | 406 (132..537) | 40 | 19 | 37 (8), 11 (5), 35 (5), 27 (4), 15 (3), 5 (3), 54 (3), 22 (3), 14 (2), 17 (2), 66 (1), 62 (1) |
| 79136 | 393 (136..538) | 21 | 12 | 14 (6), 35 (3), 15 (2), 5 (2), 27 (2), 91 (2), 11 (1), 17 (1), 43 (1), 37 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..28 | 7 | 0 | 7 |
| 6 | 87..93 | 7 | 0 | 7 |
| 13 | 150..159 | 10 | 0 | 10 |
| 25 | 213..220 | 8 | 0 | 8 |
| 30 | 233..416 | 184 | 0 | 184 |
| 31 | 239..416 | 178 | 0 | 178 |
| 38 | 268..305 | 38 | 0 | 38 |
| 44 | 277..391 | 115 | 0 | 115 |
| 47 | 297..342 | 46 | 0 | 46 |
| 55 | 329..336 | 8 | 0 | 8 |
| 63 | 343..351 | 9 | 0 | 9 |
| 67 | 364..442 | 79 | 0 | 79 |
| 72 | 388..425 | 38 | 0 | 38 |
| 78 | 409..618 | 210 | 0 | 210 |
| 86 | 450..478 | 29 | 0 | 29 |
| 90 | 466..480 | 15 | 0 | 15 |
| 92 | 472..476 | 5 | 0 | 5 |
| 95 | 484..490 | 7 | 0 | 7 |
| 103 | 502..509 | 8 | 0 | 8 |
| 104 | 514..569 | 56 | 0 | 56 |
| 109 | 529..550 | 22 | 0 | 22 |
| 111 | 529..541 | 13 | 0 | 13 |
| 116 | 557..589 | 33 | 0 | 33 |
| 118 | 573..611 | 39 | 0 | 39 |
| 124 | 592..600 | 9 | 0 | 9 |
| 133 | 656..669 | 14 | 0 | 14 |
| 139 | 720..725 | 6 | 0 | 6 |
| 142 | 728..732 | 5 | 0 | 5 |
| 146 | 785..798 | 14 | 0 | 14 |
| 154 | 847..852 | 6 | 0 | 6 |
| 158 | 855..860 | 6 | 0 | 6 |
| 165 | 912..923 | 12 | 0 | 12 |
| 174 | 975..985 | 11 | 0 | 11 |

### Gaps and durations of candidate tracks
- tracks: 65; lifespan min/median/max: 5/24/978; tracks with internal gaps: 27; total internal gaps: 187; longest internal gap: 201; tracks ending in coasting: 54 (trailing rows total 1551)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..11 | 11 | 11 | 5 | 6 | 2 | 2 | 3 | 78911 |
| 1 | 22..28 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 3 | 31..1008 | 978 | 978 | 973 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 79..232 | 154 | 154 | 51 | 103 | 15 | 53 | 1 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79136, 79139 |
| 6 | 87..93 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 11 | 138..191 | 54 | 54 | 39 | 15 | 10 | 2 | 2 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 150..159 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 14 | 160..287 | 128 | 128 | 87 | 41 | 20 | 3 | 14 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 175..197 | 23 | 23 | 14 | 9 | 5 | 3 | 1 | 79128, 79134, 79135, 79136, 79139 |
| 17 | 187..233 | 47 | 47 | 36 | 11 | 8 | 3 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 21 | 202..220 | 19 | 19 | 17 | 2 | 1 | 1 | 1 | 78897, 78899, 79037, 79097 |
| 22 | 203..518 | 316 | 316 | 76 | 240 | 10 | 200 | 3 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 25 | 213..220 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 27 | 223..250 | 28 | 28 | 27 | 1 | 1 | 1 | 0 | 79098, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 29 | 228..253 | 26 | 26 | 26 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 30 | 233..416 | 184 | 184 | 0 | 184 | 0 | 0 | 184 | - |
| 31 | 239..416 | 178 | 178 | 0 | 178 | 0 | 0 | 178 | - |
| 32 | 240..247 | 8 | 8 | 7 | 1 | 1 | 1 | 0 | 78899, 78971, 79037, 79045 |
| 33 | 242..325 | 84 | 84 | 48 | 36 | 10 | 8 | 18 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 35 | 258..273 | 16 | 16 | 16 | 0 | 0 | 0 | 0 | 79097, 79108, 79110, 79111, 79135, 79136, 79139 |
| 37 | 265..555 | 291 | 291 | 61 | 230 | 16 | 163 | 16 | 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79134, 79135, 79136, 79139 |
| 38 | 268..305 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 40 | 273..296 | 24 | 24 | 6 | 18 | 2 | 12 | 5 | 78896, 78969 |
| 43 | 275..497 | 223 | 223 | 3 | 220 | 2 | 201 | 11 | 79135, 79136 |
| 44 | 277..391 | 115 | 115 | 0 | 115 | 0 | 0 | 115 | - |
| 47 | 297..342 | 46 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 48 | 297..382 | 86 | 86 | 53 | 33 | 11 | 11 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79132, 79134 |
| 50 | 300..306 | 7 | 7 | 1 | 6 | 0 | 0 | 6 | 79097 |
| 54 | 328..332 | 5 | 5 | 4 | 1 | 0 | 0 | 1 | 79135, 79139 |
| 55 | 329..336 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 56 | 332..446 | 115 | 115 | 54 | 61 | 18 | 16 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 57 | 335..342 | 8 | 8 | 2 | 6 | 1 | 1 | 5 | 79134, 79135 |
| 58 | 339..355 | 17 | 17 | 9 | 8 | 4 | 3 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 62 | 342..448 | 107 | 107 | 3 | 104 | 1 | 99 | 5 | 79134, 79135, 79139 |
| 63 | 343..351 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 66 | 363..457 | 95 | 95 | 20 | 75 | 10 | 23 | 7 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 67 | 364..442 | 79 | 79 | 0 | 79 | 0 | 0 | 79 | - |
| 68 | 370..462 | 93 | 93 | 54 | 39 | 19 | 5 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 72 | 388..425 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 76 | 404..411 | 8 | 8 | 6 | 2 | 1 | 1 | 1 | 78969, 78971 |
| 78 | 409..618 | 210 | 210 | 0 | 210 | 0 | 0 | 210 | - |
| 79 | 419..465 | 47 | 47 | 33 | 14 | 5 | 8 | 1 | 79097, 79098, 79102 |
| 80 | 420..475 | 56 | 56 | 2 | 54 | 0 | 0 | 54 | 79135 |
| 82 | 436..440 | 5 | 5 | 3 | 2 | 1 | 2 | 0 | 79105, 79108 |
| 86 | 450..478 | 29 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 88 | 463..609 | 147 | 147 | 4 | 143 | 2 | 3 | 139 | 79135 |
| 90 | 466..480 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 91 | 469..543 | 75 | 75 | 51 | 24 | 7 | 5 | 10 | 79115, 79116, 79122, 79134, 79136 |
| 92 | 472..476 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 95 | 484..490 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 103 | 502..509 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 104 | 514..569 | 56 | 56 | 0 | 56 | 0 | 0 | 56 | - |
| 109 | 529..550 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 111 | 529..541 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 116 | 557..589 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 118 | 573..611 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 124 | 592..600 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 133 | 656..669 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 139 | 720..725 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 142 | 728..732 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 146 | 785..798 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 154 | 847..852 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 158 | 855..860 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 165 | 912..923 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 174 | 975..985 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
