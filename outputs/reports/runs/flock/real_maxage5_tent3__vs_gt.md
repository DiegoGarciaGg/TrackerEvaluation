# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 5, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=b658b17d67e5 git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage5_tent3/tracks.csv sha256=d06494b1f4827b64
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage5_tent3
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
| observations | none | 4 | 10142 | 4104 | 0.247 | 0.098 | 0.631 | 1.00 | 0.265 | -0.149 | 1.02 | 101 | 248.0 | 0.159 | 0.275 | 0.111 | 0.133 | 0.328 | 1348 | 8794 | 2756 | 1 | 0 | 24 |
| observations | none | 6 | 10142 | 4104 | 0.259 | 0.111 | 0.617 | 1.40 | 0.272 | -0.123 | 1.41 | 137 | 332.0 | 0.167 | 0.290 | 0.117 | 0.148 | 0.365 | 1498 | 8644 | 2606 | 1 | 1 | 23 |
| observations | none | 8 | 10142 | 4104 | 0.267 | 0.123 | 0.595 | 1.89 | 0.274 | -0.105 | 1.78 | 164 | 392.0 | 0.171 | 0.298 | 0.120 | 0.158 | 0.391 | 1604 | 8538 | 2500 | 1 | 1 | 23 |
| observations | none | 12 | 10142 | 4104 | 0.276 | 0.136 | 0.573 | 2.57 | 0.280 | -0.060 | 2.90 | 181 | 455.0 | 0.188 | 0.327 | 0.132 | 0.181 | 0.448 | 1839 | 8303 | 2265 | 1 | 2 | 22 |
| observations | ignore | 4 | 10142 | 3747 | 0.251 | 0.101 | 0.631 | 1.00 | 0.268 | -0.114 | 1.02 | 101 | 248.0 | 0.163 | 0.302 | 0.111 | 0.133 | 0.360 | 1348 | 8794 | 2399 | 1 | 0 | 24 |
| observations | ignore | 6 | 10142 | 3747 | 0.263 | 0.114 | 0.617 | 1.40 | 0.276 | -0.088 | 1.41 | 137 | 332.0 | 0.171 | 0.318 | 0.117 | 0.148 | 0.400 | 1498 | 8644 | 2249 | 1 | 1 | 23 |
| observations | ignore | 8 | 10142 | 3747 | 0.271 | 0.126 | 0.595 | 1.89 | 0.278 | -0.069 | 1.78 | 164 | 392.0 | 0.176 | 0.326 | 0.120 | 0.158 | 0.428 | 1604 | 8538 | 2143 | 1 | 1 | 23 |
| observations | ignore | 12 | 10142 | 3747 | 0.280 | 0.140 | 0.573 | 2.57 | 0.284 | -0.025 | 2.90 | 181 | 455.0 | 0.193 | 0.358 | 0.132 | 0.181 | 0.491 | 1839 | 8303 | 1908 | 1 | 2 | 22 |
| updates | none | 4 | 10142 | 4976 | 0.240 | 0.097 | 0.607 | 1.08 | 0.257 | -0.226 | 1.07 | 121 | 279.0 | 0.151 | 0.229 | 0.113 | 0.138 | 0.282 | 1402 | 8740 | 3574 | 1 | 0 | 24 |
| updates | none | 6 | 10142 | 4976 | 0.252 | 0.112 | 0.585 | 1.55 | 0.264 | -0.192 | 1.53 | 154 | 356.0 | 0.160 | 0.244 | 0.120 | 0.157 | 0.320 | 1591 | 8551 | 3385 | 1 | 1 | 23 |
| updates | none | 8 | 10142 | 4976 | 0.260 | 0.126 | 0.560 | 2.09 | 0.267 | -0.164 | 2.03 | 183 | 412.0 | 0.166 | 0.252 | 0.123 | 0.173 | 0.352 | 1750 | 8392 | 3226 | 1 | 1 | 23 |
| updates | none | 12 | 10142 | 4976 | 0.269 | 0.142 | 0.532 | 2.86 | 0.273 | -0.108 | 3.24 | 200 | 464.0 | 0.184 | 0.279 | 0.137 | 0.201 | 0.410 | 2039 | 8103 | 2937 | 1 | 3 | 21 |
| updates | ignore | 4 | 10142 | 4417 | 0.245 | 0.101 | 0.607 | 1.08 | 0.262 | -0.171 | 1.07 | 121 | 279.0 | 0.157 | 0.258 | 0.113 | 0.138 | 0.317 | 1402 | 8740 | 3015 | 1 | 0 | 24 |
| updates | ignore | 6 | 10142 | 4417 | 0.258 | 0.117 | 0.585 | 1.55 | 0.270 | -0.137 | 1.53 | 154 | 356.0 | 0.167 | 0.275 | 0.120 | 0.157 | 0.360 | 1591 | 8551 | 2826 | 1 | 1 | 23 |
| updates | ignore | 8 | 10142 | 4417 | 0.266 | 0.131 | 0.560 | 2.09 | 0.273 | -0.108 | 2.03 | 183 | 412.0 | 0.172 | 0.283 | 0.123 | 0.173 | 0.396 | 1750 | 8392 | 2667 | 1 | 1 | 23 |
| updates | ignore | 12 | 10142 | 4417 | 0.275 | 0.148 | 0.532 | 2.86 | 0.279 | -0.053 | 3.24 | 200 | 464.0 | 0.191 | 0.314 | 0.137 | 0.201 | 0.462 | 2039 | 8103 | 2378 | 1 | 3 | 21 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 102; matched pairs: 1604; unmatched reference entries: 8538; unmatched candidate entries: 2500
- identity switches: 164; fragmentation (coverage interruptions): 391; orphan candidate ids (never on a reference object): 75

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f32: ref 78911: 0 -> 5 at (1816.5, 3365.5), 25 frames after previous cover
- f167: ref 79139: 12 -> 17 at (1946.5, 3016), 6 frames after previous cover
- f173: ref 79135: 12 -> 17 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 12 -> 17 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 12 -> 17 at (1843, 3021), 3 frames after previous cover
- f176: ref 79132: 12 -> 17 at (1812, 3020), 3 frames after previous cover
- f176: ref 79139: 17 -> 18 at (1889.5, 3014.5), 9 frames after previous cover
- f180: ref 79135: 17 -> 18 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 6 -> 12 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 17 -> 18 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 12 -> 17 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78971: 12 -> 17 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 17 -> 18 at (1777.5, 3018.5), 7 frames after previous cover
- f189: ref 79135: 18 -> 20 at (1782.5, 3013.5), 4 frames after previous cover
- f192: ref 78899: 17 -> 6 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 6 -> 17 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 12 -> 6 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 18 -> 20 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 12 -> 6 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 17 -> 6 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 6 -> 24 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 78899: 6 -> 24 at (1439, 3007.5), 5 frames after previous cover
- f204: ref 79135: 20 -> 6 at (1685, 3007), 2 frames after previous cover
- f205: ref 79097: 6 -> 24 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 6 -> 20 at (1673, 3006), 2 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 18 -> 20 at (1625.5, 3010), 22 frames after previous cover
- f210: ref 79132: 6 -> 20 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 20 -> 6 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 20 -> 6 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 20 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 20 -> 6 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 20 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 17 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 20 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 20 -> 6 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 6 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 20 -> 6 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 20 -> 6 at (1465, 3003), 7 frames after previous cover
- f221: ref 79139: 20 -> 6 at (1598, 2998.5), 24 frames after previous cover
- f224: ref 79139: 6 -> 30 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 24 -> 20 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 24 -> 20 at (1272, 2992), 12 frames after previous cover
- f227: ref 79045: 12 -> 20 at (1232, 2990.5), 44 frames after previous cover
- f227: ref 79105: 20 -> 6 at (1392, 2996), 13 frames after previous cover
- f228: ref 79103: 20 -> 6 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 17 -> 20 at (1202, 2988), 41 frames after previous cover
- f229: ref 79097: 20 -> 32 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 20 -> 30 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79128: 6 -> 30 at (1478, 2994), 16 frames after previous cover
- f232: ref 79115: 6 -> 30 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 6 -> 30 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 6 -> 30 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 20 -> 32 at (1242.5, 2989), 10 frames after previous cover
- f235: ref 79105: 6 -> 30 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 24 -> 32 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 32 -> 30 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 6 -> 17 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 79132: 6 -> 30 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 30 -> 32 at (1344.5, 2992), 6 frames after previous cover
- ... 104 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 9 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 9 | 7 | 6 (3), 17 (2), 73 (2), 44 (1), 60 (1) |
| 78969 | 352 (80..434) | 91 | 44 | 17 (54), 60 (12), 6 (11), 73 (8), 36 (3), 82 (2), 44 (1) |
| 78971 | 352 (84..439) | 16 | 11 | 73 (7), 17 (3), 6 (1), 12 (1), 20 (1), 54 (1), 82 (1), 60 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 54 (5), 60 (5), 73 (3), 17 (2), 12 (1), 20 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 60 (5), 17 (2), 36 (2), 73 (2), 12 (1), 24 (1), 32 (1), 35 (1), 54 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 73 (9), 60 (5), 24 (3), 36 (3), 54 (3), 12 (2), 6 (1), 20 (1) |
| 78899 | 365 (91..455) | 47 | 38 | 36 (15), 60 (7), 6 (6), 54 (6), 73 (5), 24 (4), 17 (2), 20 (1), 32 (1) |
| 79097 | 366 (94..461) | 66 | 42 | 36 (20), 54 (12), 20 (8), 32 (8), 24 (6), 73 (4), 60 (4), 12 (1), 6 (1), 38 (1), 85 (1) |
| 79098 | 360 (97..467) | 23 | 18 | 85 (12), 54 (3), 60 (3), 73 (2), 32 (1), 30 (1), 36 (1) |
| 79102 | 371 (98..477) | 23 | 13 | 85 (15), 73 (4), 32 (2), 54 (1), 60 (1) |
| 79103 | 380 (99..481) | 17 | 11 | 73 (5), 32 (3), 60 (3), 54 (2), 12 (1), 20 (1), 6 (1), 36 (1) |
| 79105 | 379 (101..484) | 4 | 3 | 20 (1), 6 (1), 30 (1), 60 (1) |
| 79108 | 385 (104..492) | 13 | 11 | 6 (2), 54 (2), 60 (2), 12 (1), 20 (1), 30 (1), 32 (1), 38 (1), 62 (1), 73 (1) |
| 79110 | 388 (106..497) | 13 | 6 | 73 (7), 6 (2), 30 (2), 20 (1), 62 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 73 (5), 6 (2), 12 (1), 32 (1), 38 (1) |
| 79115 | 421 (111..531) | 8 | 7 | 6 (2), 30 (2), 20 (1), 70 (1), 25 (1), 100 (1) |
| 79116 | 411 (114..530) | 37 | 8 | 100 (36), 25 (1) |
| 79122 | 404 (118..532) | 18 | 9 | 70 (9), 100 (8), 25 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 25 (56), 6 (3), 12 (1), 17 (1), 20 (1), 30 (1), 54 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 25 (4), 6 (3), 12 (2), 20 (2), 30 (2), 17 (1), 18 (1), 62 (1), 70 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 12 (5), 17 (4), 30 (3), 18 (2), 25 (2), 46 (2), 20 (1), 54 (1), 61 (1), 62 (1), 70 (1), 100 (1) |
| 79135 | 409 (129..542) | 45 | 37 | 73 (9), 20 (7), 12 (6), 25 (5), 46 (4), 18 (2), 6 (2), 30 (2), 38 (2), 96 (2), 17 (1), 62 (1), +2 more |
| 79139 | 406 (132..537) | 23 | 17 | 46 (7), 30 (3), 12 (2), 18 (2), 20 (2), 38 (2), 17 (1), 6 (1), 25 (1), 70 (1), 73 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 72 (1), 73 (1), 100 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..24 | 2 | 0 | 2 |
| 7 | 88..89 | 2 | 0 | 2 |
| 14 | 151..155 | 5 | 0 | 3 |
| 23 | 200..209 | 10 | 0 | 8 |
| 28 | 214..216 | 3 | 0 | 2 |
| 29 | 217..222 | 6 | 0 | 5 |
| 31 | 225..233 | 9 | 0 | 9 |
| 33 | 234..412 | 179 | 0 | 166 |
| 34 | 240..412 | 173 | 0 | 152 |
| 37 | 250..258 | 9 | 0 | 9 |
| 41 | 269..387 | 119 | 0 | 108 |
| 42 | 269..301 | 33 | 0 | 21 |
| 45 | 275..290 | 16 | 0 | 15 |
| 47 | 276..438 | 163 | 0 | 142 |
| 48 | 279..284 | 6 | 0 | 5 |
| 50 | 298..338 | 41 | 0 | 27 |
| 52 | 300..311 | 12 | 0 | 10 |
| 53 | 301..302 | 2 | 0 | 2 |
| 56 | 325..335 | 11 | 0 | 11 |
| 59 | 330..332 | 3 | 0 | 3 |
| 64 | 341..346 | 6 | 0 | 5 |
| 66 | 343..614 | 272 | 0 | 231 |
| 67 | 344..347 | 4 | 0 | 4 |
| 68 | 350..360 | 11 | 0 | 10 |
| 75 | 375..384 | 10 | 0 | 10 |
| 78 | 392..421 | 30 | 0 | 28 |
| 80 | 400..401 | 2 | 0 | 2 |
| 81 | 403..408 | 6 | 0 | 5 |
| 84 | 410..474 | 65 | 0 | 47 |
| 87 | 425..433 | 9 | 0 | 9 |
| 89 | 432..471 | 40 | 0 | 39 |
| 94 | 451..456 | 6 | 0 | 5 |
| 97 | 465..470 | 6 | 0 | 5 |
| 103 | 475..483 | 9 | 0 | 9 |
| 106 | 485..486 | 2 | 0 | 2 |
| 113 | 500..508 | 9 | 0 | 9 |
| 117 | 519..565 | 47 | 0 | 43 |
| 119 | 525..535 | 11 | 0 | 9 |
| 120 | 527..532 | 6 | 0 | 5 |
| 122 | 530..546 | 17 | 0 | 12 |
| ... | 35 more | | | |

### Gaps and durations of candidate tracks
- tracks: 102; lifespan min/median/max: 1/10/977; tracks with internal gaps: 21; total internal gaps: 141; longest internal gap: 197; tracks ending in coasting: 90 (trailing rows total 1659)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..7 | 6 | 4 | 3 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 23..24 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 5 | 32..1008 | 977 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..228 | 149 | 139 | 42 | 97 | 12 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79139 |
| 7 | 88..89 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 12 | 139..187 | 49 | 33 | 25 | 8 | 7 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 14 | 151..155 | 5 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 17 | 167..283 | 117 | 100 | 73 | 27 | 15 | 3 | 5 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79139 |
| 18 | 176..193 | 18 | 13 | 7 | 6 | 3 | 2 | 1 | 79128, 79134, 79135, 79139 |
| 20 | 188..229 | 42 | 40 | 30 | 10 | 8 | 2 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 23 | 200..209 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 24 | 203..216 | 14 | 14 | 14 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 25 | 204..514 | 311 | 300 | 71 | 229 | 8 | 197 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 214..216 | 3 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 29 | 217..222 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 30 | 224..246 | 23 | 18 | 18 | 0 | 0 | 0 | 0 | 79098, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 31 | 225..233 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 32 | 229..249 | 21 | 18 | 18 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 33 | 234..412 | 179 | 166 | 0 | 166 | 0 | 0 | 166 | - |
| 34 | 240..412 | 173 | 152 | 0 | 152 | 0 | 0 | 152 | - |
| 35 | 241..243 | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 79037 |
| 36 | 243..321 | 79 | 69 | 45 | 24 | 6 | 4 | 14 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 37 | 250..258 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 38 | 259..269 | 11 | 7 | 7 | 0 | 0 | 0 | 0 | 79097, 79108, 79111, 79135, 79139 |
| 41 | 269..387 | 119 | 108 | 0 | 108 | 0 | 0 | 108 | - |
| 42 | 269..301 | 33 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 44 | 274..292 | 19 | 15 | 2 | 13 | 1 | 12 | 1 | 78896, 78969 |
| 45 | 275..290 | 16 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 46 | 275..453 | 179 | 158 | 13 | 145 | 2 | 139 | 3 | 79134, 79135, 79139 |
| 47 | 276..438 | 163 | 142 | 0 | 142 | 0 | 0 | 142 | - |
| 48 | 279..284 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 50 | 298..338 | 41 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 52 | 300..311 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 53 | 301..302 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 54 | 301..378 | 78 | 58 | 38 | 20 | 9 | 5 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79132, 79134 |
| 56 | 325..335 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 59 | 330..332 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 60 | 333..466 | 134 | 108 | 50 | 58 | 14 | 15 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 336..338 | 3 | 3 | 1 | 2 | 1 | 1 | 1 | 79134 |
| 62 | 340..351 | 12 | 10 | 5 | 5 | 4 | 2 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 64 | 341..346 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 66 | 343..614 | 272 | 231 | 0 | 231 | 0 | 0 | 231 | - |
| 67 | 344..347 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 68 | 350..360 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 70 | 364..436 | 73 | 61 | 14 | 47 | 9 | 19 | 6 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 72 | 368..493 | 126 | 107 | 2 | 105 | 2 | 90 | 7 | 79135, 79136 |
| 73 | 371..551 | 181 | 148 | 75 | 73 | 23 | 13 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 75 | 375..384 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 78 | 392..421 | 30 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 80 | 400..401 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 81 | 403..408 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 82 | 405..407 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 84 | 410..474 | 65 | 47 | 0 | 47 | 0 | 0 | 47 | - |
| 85 | 420..458 | 39 | 34 | 28 | 6 | 4 | 2 | 1 | 79097, 79098, 79102 |
| 87 | 425..433 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 89 | 432..471 | 40 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 94 | 451..456 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 96 | 464..605 | 142 | 124 | 2 | 122 | 2 | 1 | 120 | 79135 |
| 97 | 465..470 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 100 | 470..539 | 70 | 64 | 47 | 17 | 6 | 5 | 4 | 79115, 79116, 79122, 79134, 79136 |
| 103 | 475..483 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 106 | 485..486 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 113 | 500..508 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 117 | 519..565 | 47 | 43 | 0 | 43 | 0 | 0 | 43 | - |
| 119 | 525..535 | 11 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 120 | 527..532 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 122 | 530..546 | 17 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 124 | 530..537 | 8 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 128 | 550..561 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 129 | 558..585 | 28 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 131 | 574..607 | 34 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 136 | 589..594 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 137 | 593..596 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 140 | 600..610 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 142 | 625..634 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 144 | 651..656 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 146 | 657..665 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 148 | 675..685 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 149 | 701..708 | 8 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 150 | 713..718 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| ... | 22 more in JSON | | | | | | | | |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 58; matched pairs: 1604; unmatched reference entries: 8538; unmatched candidate entries: 2143
- identity switches: 164; fragmentation (coverage interruptions): 391; orphan candidate ids (never on a reference object): 31

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f32: ref 78911: 0 -> 5 at (1816.5, 3365.5), 25 frames after previous cover
- f167: ref 79139: 12 -> 17 at (1946.5, 3016), 6 frames after previous cover
- f173: ref 79135: 12 -> 17 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 12 -> 17 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 12 -> 17 at (1843, 3021), 3 frames after previous cover
- f176: ref 79132: 12 -> 17 at (1812, 3020), 3 frames after previous cover
- f176: ref 79139: 17 -> 18 at (1889.5, 3014.5), 9 frames after previous cover
- f180: ref 79135: 17 -> 18 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 6 -> 12 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 17 -> 18 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 12 -> 17 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78971: 12 -> 17 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 17 -> 18 at (1777.5, 3018.5), 7 frames after previous cover
- f189: ref 79135: 18 -> 20 at (1782.5, 3013.5), 4 frames after previous cover
- f192: ref 78899: 17 -> 6 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 6 -> 17 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 12 -> 6 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 18 -> 20 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 12 -> 6 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 17 -> 6 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 6 -> 24 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 78899: 6 -> 24 at (1439, 3007.5), 5 frames after previous cover
- f204: ref 79135: 20 -> 6 at (1685, 3007), 2 frames after previous cover
- f205: ref 79097: 6 -> 24 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 6 -> 20 at (1673, 3006), 2 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 18 -> 20 at (1625.5, 3010), 22 frames after previous cover
- f210: ref 79132: 6 -> 20 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 20 -> 6 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 20 -> 6 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 20 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 20 -> 6 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 20 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 17 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 20 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 20 -> 6 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 6 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 20 -> 6 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 20 -> 6 at (1465, 3003), 7 frames after previous cover
- f221: ref 79139: 20 -> 6 at (1598, 2998.5), 24 frames after previous cover
- f224: ref 79139: 6 -> 30 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 24 -> 20 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 24 -> 20 at (1272, 2992), 12 frames after previous cover
- f227: ref 79045: 12 -> 20 at (1232, 2990.5), 44 frames after previous cover
- f227: ref 79105: 20 -> 6 at (1392, 2996), 13 frames after previous cover
- f228: ref 79103: 20 -> 6 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 17 -> 20 at (1202, 2988), 41 frames after previous cover
- f229: ref 79097: 20 -> 32 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 20 -> 30 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79128: 6 -> 30 at (1478, 2994), 16 frames after previous cover
- f232: ref 79115: 6 -> 30 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 6 -> 30 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 6 -> 30 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 20 -> 32 at (1242.5, 2989), 10 frames after previous cover
- f235: ref 79105: 6 -> 30 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 24 -> 32 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 32 -> 30 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 6 -> 17 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 79132: 6 -> 30 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 30 -> 32 at (1344.5, 2992), 6 frames after previous cover
- ... 104 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 9 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 9 | 7 | 6 (3), 17 (2), 73 (2), 44 (1), 60 (1) |
| 78969 | 352 (80..434) | 91 | 44 | 17 (54), 60 (12), 6 (11), 73 (8), 36 (3), 82 (2), 44 (1) |
| 78971 | 352 (84..439) | 16 | 11 | 73 (7), 17 (3), 6 (1), 12 (1), 20 (1), 54 (1), 82 (1), 60 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 54 (5), 60 (5), 73 (3), 17 (2), 12 (1), 20 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 60 (5), 17 (2), 36 (2), 73 (2), 12 (1), 24 (1), 32 (1), 35 (1), 54 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 73 (9), 60 (5), 24 (3), 36 (3), 54 (3), 12 (2), 6 (1), 20 (1) |
| 78899 | 365 (91..455) | 47 | 38 | 36 (15), 60 (7), 6 (6), 54 (6), 73 (5), 24 (4), 17 (2), 20 (1), 32 (1) |
| 79097 | 366 (94..461) | 66 | 42 | 36 (20), 54 (12), 20 (8), 32 (8), 24 (6), 73 (4), 60 (4), 12 (1), 6 (1), 38 (1), 85 (1) |
| 79098 | 360 (97..467) | 23 | 18 | 85 (12), 54 (3), 60 (3), 73 (2), 32 (1), 30 (1), 36 (1) |
| 79102 | 371 (98..477) | 23 | 13 | 85 (15), 73 (4), 32 (2), 54 (1), 60 (1) |
| 79103 | 380 (99..481) | 17 | 11 | 73 (5), 32 (3), 60 (3), 54 (2), 12 (1), 20 (1), 6 (1), 36 (1) |
| 79105 | 379 (101..484) | 4 | 3 | 20 (1), 6 (1), 30 (1), 60 (1) |
| 79108 | 385 (104..492) | 13 | 11 | 6 (2), 54 (2), 60 (2), 12 (1), 20 (1), 30 (1), 32 (1), 38 (1), 62 (1), 73 (1) |
| 79110 | 388 (106..497) | 13 | 6 | 73 (7), 6 (2), 30 (2), 20 (1), 62 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 73 (5), 6 (2), 12 (1), 32 (1), 38 (1) |
| 79115 | 421 (111..531) | 8 | 7 | 6 (2), 30 (2), 20 (1), 70 (1), 25 (1), 100 (1) |
| 79116 | 411 (114..530) | 37 | 8 | 100 (36), 25 (1) |
| 79122 | 404 (118..532) | 18 | 9 | 70 (9), 100 (8), 25 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 25 (56), 6 (3), 12 (1), 17 (1), 20 (1), 30 (1), 54 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 25 (4), 6 (3), 12 (2), 20 (2), 30 (2), 17 (1), 18 (1), 62 (1), 70 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 12 (5), 17 (4), 30 (3), 18 (2), 25 (2), 46 (2), 20 (1), 54 (1), 61 (1), 62 (1), 70 (1), 100 (1) |
| 79135 | 409 (129..542) | 45 | 37 | 73 (9), 20 (7), 12 (6), 25 (5), 46 (4), 18 (2), 6 (2), 30 (2), 38 (2), 96 (2), 17 (1), 62 (1), +2 more |
| 79139 | 406 (132..537) | 23 | 17 | 46 (7), 30 (3), 12 (2), 18 (2), 20 (2), 38 (2), 17 (1), 6 (1), 25 (1), 70 (1), 73 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 72 (1), 73 (1), 100 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..24 | 2 | 0 | 2 |
| 7 | 88..89 | 2 | 0 | 2 |
| 14 | 151..155 | 5 | 0 | 3 |
| 28 | 214..216 | 3 | 0 | 2 |
| 33 | 234..412 | 179 | 0 | 166 |
| 34 | 240..412 | 173 | 0 | 152 |
| 41 | 269..387 | 119 | 0 | 108 |
| 42 | 269..301 | 33 | 0 | 21 |
| 47 | 276..438 | 163 | 0 | 142 |
| 50 | 298..338 | 41 | 0 | 27 |
| 53 | 301..302 | 2 | 0 | 2 |
| 59 | 330..332 | 3 | 0 | 3 |
| 66 | 343..614 | 272 | 0 | 231 |
| 67 | 344..347 | 4 | 0 | 4 |
| 78 | 392..421 | 30 | 0 | 28 |
| 84 | 410..474 | 65 | 0 | 47 |
| 89 | 432..471 | 40 | 0 | 39 |
| 106 | 485..486 | 2 | 0 | 2 |
| 117 | 519..565 | 47 | 0 | 43 |
| 122 | 530..546 | 17 | 0 | 12 |
| 124 | 530..537 | 8 | 0 | 5 |
| 129 | 558..585 | 28 | 0 | 28 |
| 131 | 574..607 | 34 | 0 | 26 |
| 137 | 593..596 | 4 | 0 | 4 |
| 146 | 657..665 | 9 | 0 | 9 |
| 152 | 721..721 | 1 | 0 | 1 |
| 159 | 786..794 | 9 | 0 | 4 |
| 167 | 848..848 | 1 | 0 | 1 |
| 171 | 856..856 | 1 | 0 | 1 |
| 178 | 913..919 | 7 | 0 | 3 |
| 187 | 976..981 | 6 | 0 | 4 |

### Gaps and durations of candidate tracks
- tracks: 58; lifespan min/median/max: 1/28/977; tracks with internal gaps: 21; total internal gaps: 141; longest internal gap: 197; tracks ending in coasting: 46 (trailing rows total 1302)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..7 | 6 | 4 | 3 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 23..24 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 5 | 32..1008 | 977 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..228 | 149 | 139 | 42 | 97 | 12 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79139 |
| 7 | 88..89 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 12 | 139..187 | 49 | 33 | 25 | 8 | 7 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 14 | 151..155 | 5 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 17 | 167..283 | 117 | 100 | 73 | 27 | 15 | 3 | 5 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79139 |
| 18 | 176..193 | 18 | 13 | 7 | 6 | 3 | 2 | 1 | 79128, 79134, 79135, 79139 |
| 20 | 188..229 | 42 | 40 | 30 | 10 | 8 | 2 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 24 | 203..216 | 14 | 14 | 14 | 0 | 0 | 0 | 0 | 78897, 78899, 79037, 79097 |
| 25 | 204..514 | 311 | 300 | 71 | 229 | 8 | 197 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 214..216 | 3 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 30 | 224..246 | 23 | 18 | 18 | 0 | 0 | 0 | 0 | 79098, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79139 |
| 32 | 229..249 | 21 | 18 | 18 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 33 | 234..412 | 179 | 166 | 0 | 166 | 0 | 0 | 166 | - |
| 34 | 240..412 | 173 | 152 | 0 | 152 | 0 | 0 | 152 | - |
| 35 | 241..243 | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 79037 |
| 36 | 243..321 | 79 | 69 | 45 | 24 | 6 | 4 | 14 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 38 | 259..269 | 11 | 7 | 7 | 0 | 0 | 0 | 0 | 79097, 79108, 79111, 79135, 79139 |
| 41 | 269..387 | 119 | 108 | 0 | 108 | 0 | 0 | 108 | - |
| 42 | 269..301 | 33 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 44 | 274..292 | 19 | 15 | 2 | 13 | 1 | 12 | 1 | 78896, 78969 |
| 46 | 275..453 | 179 | 158 | 13 | 145 | 2 | 139 | 3 | 79134, 79135, 79139 |
| 47 | 276..438 | 163 | 142 | 0 | 142 | 0 | 0 | 142 | - |
| 50 | 298..338 | 41 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 53 | 301..302 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 54 | 301..378 | 78 | 58 | 38 | 20 | 9 | 5 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79132, 79134 |
| 59 | 330..332 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 60 | 333..466 | 134 | 108 | 50 | 58 | 14 | 15 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 336..338 | 3 | 3 | 1 | 2 | 1 | 1 | 1 | 79134 |
| 62 | 340..351 | 12 | 10 | 5 | 5 | 4 | 2 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 66 | 343..614 | 272 | 231 | 0 | 231 | 0 | 0 | 231 | - |
| 67 | 344..347 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 70 | 364..436 | 73 | 61 | 14 | 47 | 9 | 19 | 6 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 72 | 368..493 | 126 | 107 | 2 | 105 | 2 | 90 | 7 | 79135, 79136 |
| 73 | 371..551 | 181 | 148 | 75 | 73 | 23 | 13 | 12 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 78 | 392..421 | 30 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 82 | 405..407 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 78969, 78971 |
| 84 | 410..474 | 65 | 47 | 0 | 47 | 0 | 0 | 47 | - |
| 85 | 420..458 | 39 | 34 | 28 | 6 | 4 | 2 | 1 | 79097, 79098, 79102 |
| 89 | 432..471 | 40 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 96 | 464..605 | 142 | 124 | 2 | 122 | 2 | 1 | 120 | 79135 |
| 100 | 470..539 | 70 | 64 | 47 | 17 | 6 | 5 | 4 | 79115, 79116, 79122, 79134, 79136 |
| 106 | 485..486 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 117 | 519..565 | 47 | 43 | 0 | 43 | 0 | 0 | 43 | - |
| 122 | 530..546 | 17 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 124 | 530..537 | 8 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 129 | 558..585 | 28 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 131 | 574..607 | 34 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 137 | 593..596 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 146 | 657..665 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 152 | 721..721 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 159 | 786..794 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 167 | 848..848 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 171 | 856..856 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 178 | 913..919 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 187 | 976..981 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 102; matched pairs: 1750; unmatched reference entries: 8392; unmatched candidate entries: 3226
- identity switches: 183; fragmentation (coverage interruptions): 409; orphan candidate ids (never on a reference object): 75

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f32: ref 78911: 0 -> 5 at (1816.5, 3365.5), 24 frames after previous cover
- f167: ref 79139: 12 -> 17 at (1946.5, 3016), 5 frames after previous cover
- f169: ref 79136: 12 -> 17 at (1961, 3015.5), 28 frames after previous cover
- f173: ref 79135: 12 -> 17 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 12 -> 17 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 12 -> 17 at (1843, 3021), 3 frames after previous cover
- f176: ref 79132: 12 -> 17 at (1812, 3020), 3 frames after previous cover
- f176: ref 79139: 17 -> 18 at (1889.5, 3014.5), 9 frames after previous cover
- f178: ref 79136: 17 -> 18 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 17 -> 18 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 6 -> 12 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 17 -> 18 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 12 -> 17 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 6 -> 12 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 12 -> 17 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 17 -> 18 at (1777.5, 3018.5), 6 frames after previous cover
- f189: ref 79135: 18 -> 20 at (1782.5, 3013.5), 4 frames after previous cover
- f190: ref 79045: 12 -> 17 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 20 -> 18 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 17 -> 6 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 12 -> 17 at (1414, 3008.5), 3 frames after previous cover
- f193: ref 79135: 18 -> 20 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 12 -> 6 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 18 -> 20 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 12 -> 6 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 17 -> 6 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 6 -> 24 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 78899: 6 -> 24 at (1439, 3007.5), 5 frames after previous cover
- f204: ref 79135: 20 -> 6 at (1685, 3007), 2 frames after previous cover
- f204: ref 79136: 18 -> 20 at (1731, 3016), 22 frames after previous cover
- f205: ref 79097: 6 -> 24 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 6 -> 20 at (1673, 3006), 2 frames after previous cover
- f206: ref 79139: 20 -> 6 at (1693.5, 3007.5), 9 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 18 -> 20 at (1625.5, 3010), 12 frames after previous cover
- f209: ref 79136: 20 -> 6 at (1698.5, 3013.5), 5 frames after previous cover
- f210: ref 79132: 6 -> 20 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 20 -> 6 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 20 -> 6 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 20 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 20 -> 6 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 20 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 17 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 20 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 20 -> 6 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 6 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 20 -> 6 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 20 -> 6 at (1465, 3003), 7 frames after previous cover
- f224: ref 79139: 6 -> 30 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 24 -> 20 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 24 -> 20 at (1272, 2992), 7 frames after previous cover
- f227: ref 79045: 17 -> 20 at (1232, 2990.5), 36 frames after previous cover
- f227: ref 79105: 20 -> 6 at (1392, 2996), 13 frames after previous cover
- f227: ref 79136: 6 -> 30 at (1580, 3002), 17 frames after previous cover
- f228: ref 79103: 20 -> 6 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 17 -> 20 at (1202, 2988), 40 frames after previous cover
- f229: ref 79097: 20 -> 32 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 20 -> 30 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79128: 6 -> 30 at (1478, 2994), 16 frames after previous cover
- f232: ref 79115: 6 -> 30 at (1429.5, 3001), 9 frames after previous cover
- ... 123 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 7 | 5 (972), 0 (4) |
| 78896 | 350 (76..429) | 11 | 7 | 6 (4), 17 (2), 44 (2), 73 (2), 60 (1) |
| 78969 | 352 (80..434) | 103 | 45 | 17 (54), 73 (13), 6 (12), 60 (12), 82 (4), 44 (3), 36 (3), 12 (2) |
| 78971 | 352 (84..439) | 23 | 12 | 73 (8), 17 (4), 35 (3), 20 (2), 60 (2), 6 (1), 12 (1), 54 (1), 82 (1) |
| 79045 | 355 (84..443) | 29 | 13 | 54 (8), 60 (6), 20 (5), 17 (4), 73 (4), 12 (1), 35 (1) |
| 79037 | 355 (86..445) | 21 | 16 | 60 (6), 54 (4), 17 (2), 35 (2), 36 (2), 73 (2), 12 (1), 24 (1), 32 (1) |
| 78897 | 345 (89..450) | 35 | 22 | 73 (11), 60 (7), 24 (5), 54 (5), 36 (3), 12 (2), 6 (1), 20 (1) |
| 78899 | 365 (91..455) | 54 | 37 | 36 (17), 60 (10), 6 (6), 54 (6), 73 (6), 24 (4), 17 (3), 20 (1), 32 (1) |
| 79097 | 366 (94..461) | 69 | 41 | 36 (20), 54 (13), 20 (8), 32 (8), 24 (6), 73 (5), 60 (5), 12 (1), 6 (1), 38 (1), 85 (1) |
| 79098 | 360 (97..467) | 29 | 18 | 85 (15), 60 (4), 73 (4), 54 (3), 32 (1), 30 (1), 36 (1) |
| 79102 | 371 (98..477) | 25 | 12 | 85 (16), 73 (4), 32 (3), 54 (1), 60 (1) |
| 79103 | 380 (99..481) | 24 | 11 | 32 (8), 60 (5), 73 (5), 54 (2), 12 (1), 20 (1), 6 (1), 36 (1) |
| 79105 | 379 (101..484) | 8 | 5 | 6 (3), 30 (2), 20 (1), 32 (1), 60 (1) |
| 79108 | 385 (104..492) | 17 | 11 | 62 (3), 12 (2), 6 (2), 38 (2), 54 (2), 60 (2), 20 (1), 30 (1), 32 (1), 73 (1) |
| 79110 | 388 (106..497) | 16 | 8 | 73 (7), 62 (3), 6 (2), 30 (2), 20 (1), 38 (1) |
| 79111 | 386 (109..500) | 13 | 6 | 73 (6), 6 (2), 30 (2), 12 (1), 32 (1), 38 (1) |
| 79115 | 421 (111..531) | 12 | 10 | 30 (4), 6 (2), 54 (2), 20 (1), 70 (1), 25 (1), 100 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 100 (36), 25 (2) |
| 79122 | 404 (118..532) | 21 | 11 | 100 (10), 70 (9), 12 (1), 25 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 25 (57), 6 (3), 12 (1), 17 (1), 20 (1), 30 (1), 54 (1) |
| 79128 | 402 (124..527) | 21 | 15 | 25 (4), 12 (3), 18 (3), 6 (3), 20 (2), 30 (2), 70 (2), 17 (1), 62 (1) |
| 79134 | 407 (127..533) | 31 | 22 | 12 (7), 17 (5), 18 (4), 30 (3), 70 (3), 25 (2), 46 (2), 20 (1), 54 (1), 61 (1), 62 (1), 100 (1) |
| 79135 | 409 (129..542) | 58 | 35 | 73 (12), 12 (9), 20 (6), 25 (6), 46 (6), 96 (4), 17 (3), 18 (2), 6 (2), 30 (2), 38 (2), 72 (2), +2 more |
| 79139 | 406 (132..537) | 34 | 18 | 46 (8), 38 (5), 12 (4), 30 (4), 6 (3), 25 (3), 18 (2), 20 (2), 17 (1), 70 (1), 73 (1) |
| 79136 | 393 (136..538) | 17 | 10 | 38 (3), 17 (2), 18 (2), 6 (2), 30 (2), 100 (2), 12 (1), 20 (1), 72 (1), 73 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..28 | 6 | 0 | 6 |
| 7 | 88..93 | 6 | 0 | 6 |
| 14 | 151..159 | 9 | 0 | 9 |
| 23 | 200..213 | 14 | 0 | 14 |
| 28 | 214..220 | 7 | 0 | 7 |
| 29 | 217..226 | 10 | 0 | 10 |
| 31 | 225..237 | 13 | 0 | 13 |
| 33 | 234..416 | 183 | 0 | 183 |
| 34 | 240..416 | 177 | 0 | 177 |
| 37 | 250..262 | 13 | 0 | 13 |
| 41 | 269..391 | 123 | 0 | 123 |
| 42 | 269..305 | 37 | 0 | 37 |
| 45 | 275..294 | 20 | 0 | 20 |
| 47 | 276..442 | 167 | 0 | 167 |
| 48 | 279..288 | 10 | 0 | 10 |
| 50 | 298..342 | 45 | 0 | 45 |
| 52 | 300..315 | 16 | 0 | 16 |
| 53 | 301..306 | 6 | 0 | 6 |
| 56 | 325..339 | 15 | 0 | 15 |
| 59 | 330..336 | 7 | 0 | 7 |
| 64 | 341..350 | 10 | 0 | 10 |
| 66 | 343..618 | 276 | 0 | 276 |
| 67 | 344..351 | 8 | 0 | 8 |
| 68 | 350..364 | 15 | 0 | 15 |
| 75 | 375..388 | 14 | 0 | 14 |
| 78 | 392..425 | 34 | 0 | 34 |
| 80 | 400..405 | 6 | 0 | 6 |
| 81 | 403..412 | 10 | 0 | 10 |
| 84 | 410..478 | 69 | 0 | 69 |
| 87 | 425..437 | 13 | 0 | 13 |
| 89 | 432..475 | 44 | 0 | 44 |
| 94 | 451..460 | 10 | 0 | 10 |
| 97 | 465..474 | 10 | 0 | 10 |
| 103 | 475..487 | 13 | 0 | 13 |
| 106 | 485..490 | 6 | 0 | 6 |
| 113 | 500..512 | 13 | 0 | 13 |
| 117 | 519..569 | 51 | 0 | 51 |
| 119 | 525..539 | 15 | 0 | 15 |
| 120 | 527..536 | 10 | 0 | 10 |
| 122 | 530..550 | 21 | 0 | 21 |
| ... | 35 more | | | |

### Gaps and durations of candidate tracks
- tracks: 102; lifespan min/median/max: 5/14/977; tracks with internal gaps: 25; total internal gaps: 183; longest internal gap: 199; tracks ending in coasting: 93 (trailing rows total 2254)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..11 | 10 | 10 | 4 | 6 | 2 | 2 | 3 | 78911 |
| 1 | 23..28 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 5 | 32..1008 | 977 | 977 | 972 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..232 | 153 | 153 | 50 | 103 | 15 | 53 | 1 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79136, 79139 |
| 7 | 88..93 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 12 | 139..191 | 53 | 53 | 38 | 15 | 10 | 2 | 2 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 151..159 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 17 | 167..287 | 121 | 121 | 82 | 39 | 18 | 3 | 14 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 176..197 | 22 | 22 | 13 | 9 | 5 | 3 | 1 | 79128, 79134, 79135, 79136, 79139 |
| 20 | 188..233 | 46 | 46 | 35 | 11 | 8 | 3 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 200..213 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 24 | 203..220 | 18 | 18 | 16 | 2 | 1 | 1 | 1 | 78897, 78899, 79037, 79097 |
| 25 | 204..518 | 315 | 315 | 76 | 239 | 10 | 199 | 3 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 214..220 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 29 | 217..226 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 30 | 224..250 | 27 | 27 | 26 | 1 | 1 | 1 | 0 | 79098, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 31 | 225..237 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 32 | 229..253 | 25 | 25 | 25 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 33 | 234..416 | 183 | 183 | 0 | 183 | 0 | 0 | 183 | - |
| 34 | 240..416 | 177 | 177 | 0 | 177 | 0 | 0 | 177 | - |
| 35 | 241..247 | 7 | 7 | 6 | 1 | 1 | 1 | 0 | 78971, 79037, 79045 |
| 36 | 243..325 | 83 | 83 | 47 | 36 | 10 | 8 | 18 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 37 | 250..262 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 38 | 259..273 | 15 | 15 | 15 | 0 | 0 | 0 | 0 | 79097, 79108, 79110, 79111, 79135, 79136, 79139 |
| 41 | 269..391 | 123 | 123 | 0 | 123 | 0 | 0 | 123 | - |
| 42 | 269..305 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 44 | 274..296 | 23 | 23 | 5 | 18 | 2 | 12 | 5 | 78896, 78969 |
| 45 | 275..294 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 46 | 275..457 | 183 | 183 | 16 | 167 | 3 | 153 | 7 | 79134, 79135, 79139 |
| 47 | 276..442 | 167 | 167 | 0 | 167 | 0 | 0 | 167 | - |
| 48 | 279..288 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 50 | 298..342 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 52 | 300..315 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 53 | 301..306 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 54 | 301..382 | 82 | 82 | 49 | 33 | 11 | 11 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79115, 79132, 79134 |
| 56 | 325..339 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 59 | 330..336 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 60 | 333..470 | 138 | 138 | 62 | 76 | 21 | 16 | 9 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 336..342 | 7 | 7 | 1 | 6 | 1 | 1 | 5 | 79134 |
| 62 | 340..355 | 16 | 16 | 9 | 7 | 4 | 3 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 64 | 341..350 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 66 | 343..618 | 276 | 276 | 0 | 276 | 0 | 0 | 276 | - |
| 67 | 344..351 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 68 | 350..364 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 70 | 364..440 | 77 | 77 | 17 | 60 | 9 | 22 | 15 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 72 | 368..497 | 130 | 130 | 3 | 127 | 2 | 108 | 11 | 79135, 79136 |
| 73 | 371..555 | 185 | 185 | 92 | 93 | 29 | 17 | 16 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 75 | 375..388 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 78 | 392..425 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 80 | 400..405 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 81 | 403..412 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 82 | 405..411 | 7 | 7 | 5 | 2 | 1 | 1 | 1 | 78969, 78971 |
| 84 | 410..478 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 85 | 420..462 | 43 | 43 | 32 | 11 | 6 | 5 | 0 | 79097, 79098, 79102 |
| 87 | 425..437 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 89 | 432..475 | 44 | 44 | 0 | 44 | 0 | 0 | 44 | - |
| 94 | 451..460 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 96 | 464..609 | 146 | 146 | 4 | 142 | 2 | 2 | 139 | 79135 |
| 97 | 465..474 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 100 | 470..543 | 74 | 74 | 50 | 24 | 7 | 5 | 10 | 79115, 79116, 79122, 79134, 79136 |
| 103 | 475..487 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 106 | 485..490 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 113 | 500..512 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 117 | 519..569 | 51 | 51 | 0 | 51 | 0 | 0 | 51 | - |
| 119 | 525..539 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 120 | 527..536 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 122 | 530..550 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 124 | 530..541 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 128 | 550..565 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 129 | 558..589 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 131 | 574..611 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 136 | 589..598 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 137 | 593..600 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 140 | 600..614 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 142 | 625..638 | 14 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 144 | 651..660 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 146 | 657..669 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 148 | 675..689 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 149 | 701..712 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 150 | 713..722 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| ... | 22 more in JSON | | | | | | | | |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 58; matched pairs: 1750; unmatched reference entries: 8392; unmatched candidate entries: 2667
- identity switches: 183; fragmentation (coverage interruptions): 409; orphan candidate ids (never on a reference object): 31

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f32: ref 78911: 0 -> 5 at (1816.5, 3365.5), 24 frames after previous cover
- f167: ref 79139: 12 -> 17 at (1946.5, 3016), 5 frames after previous cover
- f169: ref 79136: 12 -> 17 at (1961, 3015.5), 28 frames after previous cover
- f173: ref 79135: 12 -> 17 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 12 -> 17 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 12 -> 17 at (1843, 3021), 3 frames after previous cover
- f176: ref 79132: 12 -> 17 at (1812, 3020), 3 frames after previous cover
- f176: ref 79139: 17 -> 18 at (1889.5, 3014.5), 9 frames after previous cover
- f178: ref 79136: 17 -> 18 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 17 -> 18 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 6 -> 12 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 17 -> 18 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 12 -> 17 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 6 -> 12 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 12 -> 17 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 17 -> 18 at (1777.5, 3018.5), 6 frames after previous cover
- f189: ref 79135: 18 -> 20 at (1782.5, 3013.5), 4 frames after previous cover
- f190: ref 79045: 12 -> 17 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 20 -> 18 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 17 -> 6 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 12 -> 17 at (1414, 3008.5), 3 frames after previous cover
- f193: ref 79135: 18 -> 20 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 12 -> 6 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 18 -> 20 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 12 -> 6 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 17 -> 6 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 6 -> 24 at (1419.5, 3003), 9 frames after previous cover
- f204: ref 78899: 6 -> 24 at (1439, 3007.5), 5 frames after previous cover
- f204: ref 79135: 20 -> 6 at (1685, 3007), 2 frames after previous cover
- f204: ref 79136: 18 -> 20 at (1731, 3016), 22 frames after previous cover
- f205: ref 79097: 6 -> 24 at (1459.5, 3008), 8 frames after previous cover
- f206: ref 79135: 6 -> 20 at (1673, 3006), 2 frames after previous cover
- f206: ref 79139: 20 -> 6 at (1693.5, 3007.5), 9 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 18 -> 20 at (1625.5, 3010), 12 frames after previous cover
- f209: ref 79136: 20 -> 6 at (1698.5, 3013.5), 5 frames after previous cover
- f210: ref 79132: 6 -> 20 at (1586.5, 3007.5), 9 frames after previous cover
- f211: ref 79135: 20 -> 6 at (1639, 3003), 5 frames after previous cover
- f212: ref 79128: 20 -> 6 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 20 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 20 -> 6 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 20 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 17 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 20 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 20 -> 6 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 6 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 20 -> 6 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 20 -> 6 at (1465, 3003), 7 frames after previous cover
- f224: ref 79139: 6 -> 30 at (1579.5, 2999.5), 3 frames after previous cover
- f225: ref 78899: 24 -> 20 at (1305.5, 2993), 10 frames after previous cover
- f226: ref 78897: 24 -> 20 at (1272, 2992), 7 frames after previous cover
- f227: ref 79045: 17 -> 20 at (1232, 2990.5), 36 frames after previous cover
- f227: ref 79105: 20 -> 6 at (1392, 2996), 13 frames after previous cover
- f227: ref 79136: 6 -> 30 at (1580, 3002), 17 frames after previous cover
- f228: ref 79103: 20 -> 6 at (1365.5, 2995), 13 frames after previous cover
- f229: ref 78971: 17 -> 20 at (1202, 2988), 40 frames after previous cover
- f229: ref 79097: 20 -> 32 at (1307.5, 2989.5), 5 frames after previous cover
- f230: ref 79134: 20 -> 30 at (1505.5, 3001), 23 frames after previous cover
- f231: ref 79128: 6 -> 30 at (1478, 2994), 16 frames after previous cover
- f232: ref 79115: 6 -> 30 at (1429.5, 3001), 9 frames after previous cover
- ... 123 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 7 | 5 (972), 0 (4) |
| 78896 | 350 (76..429) | 11 | 7 | 6 (4), 17 (2), 44 (2), 73 (2), 60 (1) |
| 78969 | 352 (80..434) | 103 | 45 | 17 (54), 73 (13), 6 (12), 60 (12), 82 (4), 44 (3), 36 (3), 12 (2) |
| 78971 | 352 (84..439) | 23 | 12 | 73 (8), 17 (4), 35 (3), 20 (2), 60 (2), 6 (1), 12 (1), 54 (1), 82 (1) |
| 79045 | 355 (84..443) | 29 | 13 | 54 (8), 60 (6), 20 (5), 17 (4), 73 (4), 12 (1), 35 (1) |
| 79037 | 355 (86..445) | 21 | 16 | 60 (6), 54 (4), 17 (2), 35 (2), 36 (2), 73 (2), 12 (1), 24 (1), 32 (1) |
| 78897 | 345 (89..450) | 35 | 22 | 73 (11), 60 (7), 24 (5), 54 (5), 36 (3), 12 (2), 6 (1), 20 (1) |
| 78899 | 365 (91..455) | 54 | 37 | 36 (17), 60 (10), 6 (6), 54 (6), 73 (6), 24 (4), 17 (3), 20 (1), 32 (1) |
| 79097 | 366 (94..461) | 69 | 41 | 36 (20), 54 (13), 20 (8), 32 (8), 24 (6), 73 (5), 60 (5), 12 (1), 6 (1), 38 (1), 85 (1) |
| 79098 | 360 (97..467) | 29 | 18 | 85 (15), 60 (4), 73 (4), 54 (3), 32 (1), 30 (1), 36 (1) |
| 79102 | 371 (98..477) | 25 | 12 | 85 (16), 73 (4), 32 (3), 54 (1), 60 (1) |
| 79103 | 380 (99..481) | 24 | 11 | 32 (8), 60 (5), 73 (5), 54 (2), 12 (1), 20 (1), 6 (1), 36 (1) |
| 79105 | 379 (101..484) | 8 | 5 | 6 (3), 30 (2), 20 (1), 32 (1), 60 (1) |
| 79108 | 385 (104..492) | 17 | 11 | 62 (3), 12 (2), 6 (2), 38 (2), 54 (2), 60 (2), 20 (1), 30 (1), 32 (1), 73 (1) |
| 79110 | 388 (106..497) | 16 | 8 | 73 (7), 62 (3), 6 (2), 30 (2), 20 (1), 38 (1) |
| 79111 | 386 (109..500) | 13 | 6 | 73 (6), 6 (2), 30 (2), 12 (1), 32 (1), 38 (1) |
| 79115 | 421 (111..531) | 12 | 10 | 30 (4), 6 (2), 54 (2), 20 (1), 70 (1), 25 (1), 100 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 100 (36), 25 (2) |
| 79122 | 404 (118..532) | 21 | 11 | 100 (10), 70 (9), 12 (1), 25 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 25 (57), 6 (3), 12 (1), 17 (1), 20 (1), 30 (1), 54 (1) |
| 79128 | 402 (124..527) | 21 | 15 | 25 (4), 12 (3), 18 (3), 6 (3), 20 (2), 30 (2), 70 (2), 17 (1), 62 (1) |
| 79134 | 407 (127..533) | 31 | 22 | 12 (7), 17 (5), 18 (4), 30 (3), 70 (3), 25 (2), 46 (2), 20 (1), 54 (1), 61 (1), 62 (1), 100 (1) |
| 79135 | 409 (129..542) | 58 | 35 | 73 (12), 12 (9), 20 (6), 25 (6), 46 (6), 96 (4), 17 (3), 18 (2), 6 (2), 30 (2), 38 (2), 72 (2), +2 more |
| 79139 | 406 (132..537) | 34 | 18 | 46 (8), 38 (5), 12 (4), 30 (4), 6 (3), 25 (3), 18 (2), 20 (2), 17 (1), 70 (1), 73 (1) |
| 79136 | 393 (136..538) | 17 | 10 | 38 (3), 17 (2), 18 (2), 6 (2), 30 (2), 100 (2), 12 (1), 20 (1), 72 (1), 73 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..28 | 6 | 0 | 6 |
| 7 | 88..93 | 6 | 0 | 6 |
| 14 | 151..159 | 9 | 0 | 9 |
| 28 | 214..220 | 7 | 0 | 7 |
| 33 | 234..416 | 183 | 0 | 183 |
| 34 | 240..416 | 177 | 0 | 177 |
| 41 | 269..391 | 123 | 0 | 123 |
| 42 | 269..305 | 37 | 0 | 37 |
| 47 | 276..442 | 167 | 0 | 167 |
| 50 | 298..342 | 45 | 0 | 45 |
| 53 | 301..306 | 6 | 0 | 6 |
| 59 | 330..336 | 7 | 0 | 7 |
| 66 | 343..618 | 276 | 0 | 276 |
| 67 | 344..351 | 8 | 0 | 8 |
| 78 | 392..425 | 34 | 0 | 34 |
| 84 | 410..478 | 69 | 0 | 69 |
| 89 | 432..475 | 44 | 0 | 44 |
| 106 | 485..490 | 6 | 0 | 6 |
| 117 | 519..569 | 51 | 0 | 51 |
| 122 | 530..550 | 21 | 0 | 21 |
| 124 | 530..541 | 12 | 0 | 12 |
| 129 | 558..589 | 32 | 0 | 32 |
| 131 | 574..611 | 38 | 0 | 38 |
| 137 | 593..600 | 8 | 0 | 8 |
| 146 | 657..669 | 13 | 0 | 13 |
| 152 | 721..725 | 5 | 0 | 5 |
| 159 | 786..798 | 13 | 0 | 13 |
| 167 | 848..852 | 5 | 0 | 5 |
| 171 | 856..860 | 5 | 0 | 5 |
| 178 | 913..923 | 11 | 0 | 11 |
| 187 | 976..985 | 10 | 0 | 10 |

### Gaps and durations of candidate tracks
- tracks: 58; lifespan min/median/max: 5/32/977; tracks with internal gaps: 25; total internal gaps: 183; longest internal gap: 199; tracks ending in coasting: 49 (trailing rows total 1695)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..11 | 10 | 10 | 4 | 6 | 2 | 2 | 3 | 78911 |
| 1 | 23..28 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 5 | 32..1008 | 977 | 977 | 972 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..232 | 153 | 153 | 50 | 103 | 15 | 53 | 1 | 78896, 78897, 78899, 78969, 78971, 79097, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79135, 79136, 79139 |
| 7 | 88..93 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 12 | 139..191 | 53 | 53 | 38 | 15 | 10 | 2 | 2 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 151..159 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 17 | 167..287 | 121 | 121 | 82 | 39 | 18 | 3 | 14 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 176..197 | 22 | 22 | 13 | 9 | 5 | 3 | 1 | 79128, 79134, 79135, 79136, 79139 |
| 20 | 188..233 | 46 | 46 | 35 | 11 | 8 | 3 | 0 | 78897, 78899, 78971, 79045, 79097, 79103, 79105, 79108, 79110, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 24 | 203..220 | 18 | 18 | 16 | 2 | 1 | 1 | 1 | 78897, 78899, 79037, 79097 |
| 25 | 204..518 | 315 | 315 | 76 | 239 | 10 | 199 | 3 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 28 | 214..220 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 30 | 224..250 | 27 | 27 | 26 | 1 | 1 | 1 | 0 | 79098, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 32 | 229..253 | 25 | 25 | 25 | 0 | 0 | 0 | 0 | 78899, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79111 |
| 33 | 234..416 | 183 | 183 | 0 | 183 | 0 | 0 | 183 | - |
| 34 | 240..416 | 177 | 177 | 0 | 177 | 0 | 0 | 177 | - |
| 35 | 241..247 | 7 | 7 | 6 | 1 | 1 | 1 | 0 | 78971, 79037, 79045 |
| 36 | 243..325 | 83 | 83 | 47 | 36 | 10 | 8 | 18 | 78897, 78899, 78969, 79037, 79097, 79098, 79103 |
| 38 | 259..273 | 15 | 15 | 15 | 0 | 0 | 0 | 0 | 79097, 79108, 79110, 79111, 79135, 79136, 79139 |
| 41 | 269..391 | 123 | 123 | 0 | 123 | 0 | 0 | 123 | - |
| 42 | 269..305 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 44 | 274..296 | 23 | 23 | 5 | 18 | 2 | 12 | 5 | 78896, 78969 |
| 46 | 275..457 | 183 | 183 | 16 | 167 | 3 | 153 | 7 | 79134, 79135, 79139 |
| 47 | 276..442 | 167 | 167 | 0 | 167 | 0 | 0 | 167 | - |
| 50 | 298..342 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 53 | 301..306 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 54 | 301..382 | 82 | 82 | 49 | 33 | 11 | 11 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79115, 79132, 79134 |
| 59 | 330..336 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 60 | 333..470 | 138 | 138 | 62 | 76 | 21 | 16 | 9 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108 |
| 61 | 336..342 | 7 | 7 | 1 | 6 | 1 | 1 | 5 | 79134 |
| 62 | 340..355 | 16 | 16 | 9 | 7 | 4 | 3 | 0 | 79108, 79110, 79128, 79134, 79135 |
| 66 | 343..618 | 276 | 276 | 0 | 276 | 0 | 0 | 276 | - |
| 67 | 344..351 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 70 | 364..440 | 77 | 77 | 17 | 60 | 9 | 22 | 15 | 79115, 79122, 79128, 79134, 79135, 79139 |
| 72 | 368..497 | 130 | 130 | 3 | 127 | 2 | 108 | 11 | 79135, 79136 |
| 73 | 371..555 | 185 | 185 | 92 | 93 | 29 | 17 | 16 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79135, 79136, 79139 |
| 78 | 392..425 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 82 | 405..411 | 7 | 7 | 5 | 2 | 1 | 1 | 1 | 78969, 78971 |
| 84 | 410..478 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 85 | 420..462 | 43 | 43 | 32 | 11 | 6 | 5 | 0 | 79097, 79098, 79102 |
| 89 | 432..475 | 44 | 44 | 0 | 44 | 0 | 0 | 44 | - |
| 96 | 464..609 | 146 | 146 | 4 | 142 | 2 | 2 | 139 | 79135 |
| 100 | 470..543 | 74 | 74 | 50 | 24 | 7 | 5 | 10 | 79115, 79116, 79122, 79134, 79136 |
| 106 | 485..490 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 117 | 519..569 | 51 | 51 | 0 | 51 | 0 | 0 | 51 | - |
| 122 | 530..550 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 124 | 530..541 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 129 | 558..589 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 131 | 574..611 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 137 | 593..600 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 146 | 657..669 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 152 | 721..725 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 159 | 786..798 | 13 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 167 | 848..852 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 171 | 856..860 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 178 | 913..923 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 187 | 976..985 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
