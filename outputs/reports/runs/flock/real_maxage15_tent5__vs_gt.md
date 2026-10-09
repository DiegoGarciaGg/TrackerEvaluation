# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 15, "tentative_threshold": 5}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=8ba9d6b50d24 git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage15_tent5/tracks.csv sha256=9512c5d0eeb1a011
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage15_tent5
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
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 0.249 | 0.628 | -0.129 | 1.01 | 0.161 | 82 | 253.0 |
| observations | none | 6 | 0.261 | 0.616 | -0.104 | 1.39 | 0.172 | 108 | 328.0 |
| observations | none | 8 | 0.270 | 0.602 | -0.084 | 1.76 | 0.177 | 126 | 387.0 |
| observations | none | 12 | 0.281 | 0.590 | -0.041 | 2.84 | 0.192 | 143 | 438.0 |
| observations | ignore | 4 | 0.251 | 0.628 | -0.103 | 1.01 | 0.164 | 82 | 253.0 |
| observations | ignore | 6 | 0.264 | 0.616 | -0.077 | 1.39 | 0.175 | 108 | 328.0 |
| observations | ignore | 8 | 0.273 | 0.602 | -0.058 | 1.76 | 0.180 | 126 | 387.0 |
| observations | ignore | 12 | 0.284 | 0.590 | -0.015 | 2.84 | 0.196 | 143 | 438.0 |
| updates | none | 4 | 0.234 | 0.597 | -0.293 | 1.08 | 0.145 | 102 | 289.0 |
| updates | none | 6 | 0.246 | 0.576 | -0.257 | 1.56 | 0.156 | 130 | 362.0 |
| updates | none | 8 | 0.255 | 0.555 | -0.225 | 2.06 | 0.162 | 147 | 411.0 |
| updates | none | 12 | 0.267 | 0.534 | -0.167 | 3.31 | 0.178 | 162 | 448.0 |
| updates | ignore | 4 | 0.241 | 0.597 | -0.206 | 1.08 | 0.153 | 102 | 289.0 |
| updates | ignore | 6 | 0.254 | 0.576 | -0.169 | 1.56 | 0.165 | 130 | 362.0 |
| updates | ignore | 8 | 0.264 | 0.555 | -0.138 | 2.06 | 0.171 | 147 | 411.0 |
| updates | ignore | 12 | 0.276 | 0.534 | -0.080 | 3.31 | 0.189 | 162 | 448.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 72; matched pairs: 1601; unmatched reference entries: 8541; unmatched candidate entries: 2331
- identity switches: 126; fragmentation (coverage interruptions): 387; orphan candidate ids (never on a reference object): 58

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
- f207: ref 79134: 26 -> 33 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 24 -> 26 at (1625.5, 3010), 36 frames after previous cover
- f212: ref 79128: 26 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 24 -> 26 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 26 -> 33 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 24 -> 26 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 6 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 26 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 26 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 26 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 26 -> 33 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 26 -> 24 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 33 -> 26 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 33 -> 26 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 33 -> 26 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 33 -> 26 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 33 -> 26 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 26 -> 33 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 26 -> 33 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 26 -> 33 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 24 -> 26 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 26 -> 33 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 24 -> 26 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 26 -> 24 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78971: 6 -> 26 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 26 -> 33 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 33 -> 24 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 26 -> 24 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 26 -> 6 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 26 -> 24 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 26 -> 46 at (1179, 2985.5), 5 frames after previous cover
- f246: ref 79097: 24 -> 46 at (1199.5, 2985), 7 frames after previous cover
- f255: ref 79037: 26 -> 46 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 24 -> 33 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 24 -> 46 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 24 -> 33 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 46 -> 24 at (1090, 2983.5), 4 frames after previous cover
- f274: ref 78899: 46 -> 24 at (996, 2989.5), 5 frames after previous cover
- f274: ref 78969: 6 -> 46 at (883.5, 2989), 4 frames after previous cover
- f282: ref 78897: 46 -> 24 at (913, 2990), 22 frames after previous cover
- f287: ref 78896: 6 -> 46 at (775, 2987), 14 frames after previous cover
- f304: ref 79108: 33 -> 71 at (954, 2978), 44 frames after previous cover
- f317: ref 79134: 33 -> 71 at (990.5, 2965.5), 74 frames after previous cover
- f327: ref 79132: 33 -> 71 at (895, 2966.5), 88 frames after previous cover
- f331: ref 79102: 24 -> 71 at (723.5, 2979.5), 82 frames after previous cover
- f332: ref 79098: 24 -> 71 at (692, 2975.5), 51 frames after previous cover
- f333: ref 79097: 24 -> 71 at (654.5, 2972.5), 33 frames after previous cover
- f334: ref 78899: 24 -> 71 at (619, 2977.5), 39 frames after previous cover
- f345: ref 79135: 33 -> 75 at (875.5, 2962), 80 frames after previous cover
- ... 66 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 970 | 8 | 5 (968), 0 (2) |
| 78896 | 350 (76..429) | 10 | 8 | 6 (6), 75 (3), 46 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 6 (65), 46 (15), 75 (12) |
| 78971 | 352 (84..439) | 18 | 12 | 75 (10), 6 (5), 24 (1), 26 (1), 46 (1) |
| 79045 | 355 (84..443) | 16 | 11 | 46 (14), 71 (1), 75 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 46 (7), 24 (2), 26 (2), 71 (2), 75 (2), 6 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 24 (9), 46 (9), 71 (5), 75 (4) |
| 78899 | 365 (91..455) | 50 | 40 | 24 (18), 46 (15), 71 (11), 75 (3), 26 (2), 79 (1) |
| 79097 | 366 (94..461) | 68 | 44 | 24 (35), 71 (19), 26 (5), 46 (5), 75 (3), 79 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 71 (19), 24 (2), 75 (2), 26 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 71 (16), 75 (4), 24 (2), 79 (1), 46 (1) |
| 79103 | 380 (99..481) | 15 | 10 | 24 (5), 75 (5), 46 (3), 26 (2) |
| 79105 | 379 (101..484) | 5 | 4 | 26 (2), 33 (1), 79 (1), 46 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 33 (3), 46 (3), 24 (2), 26 (2), 71 (2), 75 (2), 79 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 75 (8), 33 (4), 26 (2), 46 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 75 (5), 24 (2), 33 (2), 26 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 33 (4), 26 (2), 79 (1), 36 (1), 57 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 57 (37), 36 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 79 (10), 57 (9), 36 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 36 (56), 26 (4), 33 (2), 24 (1), 71 (1) |
| 79128 | 402 (124..527) | 14 | 11 | 33 (5), 36 (4), 26 (2), 24 (1), 75 (1), 79 (1) |
| 79134 | 407 (127..533) | 15 | 13 | 33 (4), 26 (3), 57 (3), 36 (2), 24 (1), 71 (1), 79 (1) |
| 79135 | 409 (129..542) | 41 | 33 | 33 (10), 45 (10), 26 (5), 36 (5), 93 (4), 57 (3), 24 (2), 75 (1), 79 (1) |
| 79139 | 406 (132..537) | 22 | 15 | 33 (9), 57 (7), 36 (2), 45 (2), 26 (1), 79 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 93 (1), 45 (1), 57 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 35 | 202..209 | 8 | 0 | 6 |
| 40 | 219..222 | 4 | 0 | 3 |
| 42 | 227..233 | 7 | 0 | 7 |
| 44 | 236..412 | 177 | 0 | 162 |
| 47 | 252..258 | 7 | 0 | 7 |
| 50 | 271..492 | 222 | 0 | 164 |
| 53 | 277..290 | 14 | 0 | 13 |
| 58 | 281..284 | 4 | 0 | 3 |
| 62 | 286..371 | 86 | 0 | 35 |
| 66 | 292..406 | 115 | 0 | 93 |
| 68 | 300..455 | 156 | 0 | 109 |
| 69 | 302..311 | 10 | 0 | 8 |
| 72 | 327..335 | 9 | 0 | 9 |
| 74 | 338..338 | 1 | 0 | 1 |
| 77 | 343..346 | 4 | 0 | 3 |
| 80 | 352..360 | 9 | 0 | 8 |
| 82 | 367..486 | 120 | 0 | 83 |
| 83 | 377..384 | 8 | 0 | 8 |
| 86 | 394..446 | 53 | 0 | 38 |
| 89 | 405..408 | 4 | 0 | 3 |
| 91 | 412..607 | 196 | 0 | 159 |
| 92 | 427..433 | 7 | 0 | 7 |
| 96 | 453..456 | 4 | 0 | 3 |
| 98 | 467..470 | 4 | 0 | 3 |
| 103 | 477..483 | 7 | 0 | 7 |
| 106 | 496..606 | 111 | 0 | 104 |
| 109 | 502..508 | 7 | 0 | 7 |
| 115 | 525..614 | 90 | 0 | 75 |
| 117 | 529..532 | 4 | 0 | 3 |
| 119 | 531..535 | 5 | 0 | 4 |
| 121 | 532..546 | 15 | 0 | 10 |
| 122 | 532..537 | 6 | 0 | 3 |
| 126 | 552..561 | 10 | 0 | 8 |
| 132 | 591..594 | 4 | 0 | 3 |
| 133 | 595..596 | 2 | 0 | 2 |
| 136 | 602..610 | 9 | 0 | 8 |
| 138 | 627..634 | 8 | 0 | 8 |
| 140 | 653..656 | 4 | 0 | 3 |
| 142 | 659..665 | 7 | 0 | 7 |
| 144 | 677..685 | 9 | 0 | 9 |
| ... | 18 more | | | |

### Gaps and durations of candidate tracks
- tracks: 72; lifespan min/median/max: 1/9/975; tracks with internal gaps: 13; total internal gaps: 141; longest internal gap: 164; tracks ending in coasting: 65 (trailing rows total 1365)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..7 | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 78911 |
| 5 | 34..1008 | 975 | 973 | 968 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..274 | 193 | 191 | 77 | 114 | 24 | 53 | 1 | 78896, 78969, 78971, 79037 |
| 24 | 169..302 | 134 | 94 | 83 | 11 | 6 | 3 | 2 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79108, 79111, 79128, 79132, 79134, 79135 |
| 26 | 176..243 | 68 | 47 | 37 | 10 | 7 | 2 | 1 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 33 | 196..269 | 74 | 51 | 44 | 7 | 6 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 35 | 202..209 | 8 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 36 | 206..514 | 309 | 297 | 72 | 225 | 9 | 164 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 40 | 219..222 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 42 | 227..233 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 44 | 236..412 | 177 | 162 | 0 | 162 | 0 | 0 | 162 | - |
| 45 | 242..564 | 323 | 243 | 13 | 230 | 5 | 145 | 15 | 79135, 79136, 79139 |
| 46 | 245..466 | 222 | 143 | 76 | 67 | 17 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 47 | 252..258 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 50 | 271..492 | 222 | 164 | 0 | 164 | 0 | 0 | 164 | - |
| 53 | 277..290 | 14 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 57 | 280..592 | 313 | 248 | 61 | 187 | 8 | 138 | 29 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 58 | 281..284 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 62 | 286..371 | 86 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 66 | 292..406 | 115 | 93 | 0 | 93 | 0 | 0 | 93 | - |
| 68 | 300..455 | 156 | 109 | 0 | 109 | 0 | 0 | 109 | - |
| 69 | 302..311 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 71 | 303..461 | 159 | 108 | 77 | 31 | 15 | 5 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79108, 79132, 79134 |
| 72 | 327..335 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 74 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 75 | 342..499 | 158 | 128 | 66 | 62 | 24 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79135 |
| 77 | 343..346 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 79 | 346..442 | 97 | 69 | 20 | 49 | 11 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 80 | 352..360 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 82 | 367..486 | 120 | 83 | 0 | 83 | 0 | 0 | 83 | - |
| 83 | 377..384 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 86 | 394..446 | 53 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 89 | 405..408 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 91 | 412..607 | 196 | 159 | 0 | 159 | 0 | 0 | 159 | - |
| 92 | 427..433 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 93 | 434..486 | 53 | 27 | 5 | 22 | 5 | 10 | 0 | 79135, 79136 |
| 96 | 453..456 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 98 | 467..470 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 103 | 477..483 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 106 | 496..606 | 111 | 104 | 0 | 104 | 0 | 0 | 104 | - |
| 109 | 502..508 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 115 | 525..614 | 90 | 75 | 0 | 75 | 0 | 0 | 75 | - |
| 117 | 529..532 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 119 | 531..535 | 5 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 121 | 532..546 | 15 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 122 | 532..537 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 126 | 552..561 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 132 | 591..594 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 133 | 595..596 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 136 | 602..610 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 138 | 627..634 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 140 | 653..656 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 142 | 659..665 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 144 | 677..685 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 145 | 703..708 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 146 | 715..718 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 150 | 727..733 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 152 | 752..758 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 153 | 777..782 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 160 | 802..811 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 162 | 827..834 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 163 | 839..842 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 168 | 852..860 | 9 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 171 | 877..885 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 172 | 901..906 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 173 | 903..911 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 181 | 927..935 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 182 | 933..940 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 183 | 952..957 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 185 | 963..965 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 187 | 977..983 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 191 | 1002..1008 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 1601; unmatched reference entries: 8541; unmatched candidate entries: 2065
- identity switches: 126; fragmentation (coverage interruptions): 387; orphan candidate ids (never on a reference object): 15

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
- f207: ref 79134: 26 -> 33 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 24 -> 26 at (1625.5, 3010), 36 frames after previous cover
- f212: ref 79128: 26 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 24 -> 26 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 26 -> 33 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 24 -> 26 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 6 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 26 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 26 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 26 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 26 -> 33 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 26 -> 24 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 33 -> 26 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 33 -> 26 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 33 -> 26 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 33 -> 26 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 33 -> 26 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 26 -> 33 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 26 -> 33 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 26 -> 33 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 24 -> 26 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 26 -> 33 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 24 -> 26 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 26 -> 24 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78971: 6 -> 26 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 26 -> 33 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 33 -> 24 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 26 -> 24 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 26 -> 6 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 26 -> 24 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 26 -> 46 at (1179, 2985.5), 5 frames after previous cover
- f246: ref 79097: 24 -> 46 at (1199.5, 2985), 7 frames after previous cover
- f255: ref 79037: 26 -> 46 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 24 -> 33 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 24 -> 46 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 24 -> 33 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 46 -> 24 at (1090, 2983.5), 4 frames after previous cover
- f274: ref 78899: 46 -> 24 at (996, 2989.5), 5 frames after previous cover
- f274: ref 78969: 6 -> 46 at (883.5, 2989), 4 frames after previous cover
- f282: ref 78897: 46 -> 24 at (913, 2990), 22 frames after previous cover
- f287: ref 78896: 6 -> 46 at (775, 2987), 14 frames after previous cover
- f304: ref 79108: 33 -> 71 at (954, 2978), 44 frames after previous cover
- f317: ref 79134: 33 -> 71 at (990.5, 2965.5), 74 frames after previous cover
- f327: ref 79132: 33 -> 71 at (895, 2966.5), 88 frames after previous cover
- f331: ref 79102: 24 -> 71 at (723.5, 2979.5), 82 frames after previous cover
- f332: ref 79098: 24 -> 71 at (692, 2975.5), 51 frames after previous cover
- f333: ref 79097: 24 -> 71 at (654.5, 2972.5), 33 frames after previous cover
- f334: ref 78899: 24 -> 71 at (619, 2977.5), 39 frames after previous cover
- f345: ref 79135: 33 -> 75 at (875.5, 2962), 80 frames after previous cover
- ... 66 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 970 | 8 | 5 (968), 0 (2) |
| 78896 | 350 (76..429) | 10 | 8 | 6 (6), 75 (3), 46 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 6 (65), 46 (15), 75 (12) |
| 78971 | 352 (84..439) | 18 | 12 | 75 (10), 6 (5), 24 (1), 26 (1), 46 (1) |
| 79045 | 355 (84..443) | 16 | 11 | 46 (14), 71 (1), 75 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 46 (7), 24 (2), 26 (2), 71 (2), 75 (2), 6 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 24 (9), 46 (9), 71 (5), 75 (4) |
| 78899 | 365 (91..455) | 50 | 40 | 24 (18), 46 (15), 71 (11), 75 (3), 26 (2), 79 (1) |
| 79097 | 366 (94..461) | 68 | 44 | 24 (35), 71 (19), 26 (5), 46 (5), 75 (3), 79 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 71 (19), 24 (2), 75 (2), 26 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 71 (16), 75 (4), 24 (2), 79 (1), 46 (1) |
| 79103 | 380 (99..481) | 15 | 10 | 24 (5), 75 (5), 46 (3), 26 (2) |
| 79105 | 379 (101..484) | 5 | 4 | 26 (2), 33 (1), 79 (1), 46 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 33 (3), 46 (3), 24 (2), 26 (2), 71 (2), 75 (2), 79 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 75 (8), 33 (4), 26 (2), 46 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 75 (5), 24 (2), 33 (2), 26 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 33 (4), 26 (2), 79 (1), 36 (1), 57 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 57 (37), 36 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 79 (10), 57 (9), 36 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 36 (56), 26 (4), 33 (2), 24 (1), 71 (1) |
| 79128 | 402 (124..527) | 14 | 11 | 33 (5), 36 (4), 26 (2), 24 (1), 75 (1), 79 (1) |
| 79134 | 407 (127..533) | 15 | 13 | 33 (4), 26 (3), 57 (3), 36 (2), 24 (1), 71 (1), 79 (1) |
| 79135 | 409 (129..542) | 41 | 33 | 33 (10), 45 (10), 26 (5), 36 (5), 93 (4), 57 (3), 24 (2), 75 (1), 79 (1) |
| 79139 | 406 (132..537) | 22 | 15 | 33 (9), 57 (7), 36 (2), 45 (2), 26 (1), 79 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 93 (1), 45 (1), 57 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 44 | 236..412 | 177 | 0 | 162 |
| 50 | 271..492 | 222 | 0 | 164 |
| 62 | 286..371 | 86 | 0 | 35 |
| 66 | 292..406 | 115 | 0 | 93 |
| 68 | 300..455 | 156 | 0 | 109 |
| 74 | 338..338 | 1 | 0 | 1 |
| 82 | 367..486 | 120 | 0 | 83 |
| 86 | 394..446 | 53 | 0 | 38 |
| 91 | 412..607 | 196 | 0 | 159 |
| 106 | 496..606 | 111 | 0 | 104 |
| 115 | 525..614 | 90 | 0 | 75 |
| 121 | 532..546 | 15 | 0 | 10 |
| 122 | 532..537 | 6 | 0 | 3 |
| 133 | 595..596 | 2 | 0 | 2 |
| 142 | 659..665 | 7 | 0 | 7 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 1/115/975; tracks with internal gaps: 13; total internal gaps: 141; longest internal gap: 164; tracks ending in coasting: 22 (trailing rows total 1099)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..7 | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 78911 |
| 5 | 34..1008 | 975 | 973 | 968 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..274 | 193 | 191 | 77 | 114 | 24 | 53 | 1 | 78896, 78969, 78971, 79037 |
| 24 | 169..302 | 134 | 94 | 83 | 11 | 6 | 3 | 2 | 78897, 78899, 78971, 79037, 79097, 79098, 79102, 79103, 79108, 79111, 79128, 79132, 79134, 79135 |
| 26 | 176..243 | 68 | 47 | 37 | 10 | 7 | 2 | 1 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 33 | 196..269 | 74 | 51 | 44 | 7 | 6 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 36 | 206..514 | 309 | 297 | 72 | 225 | 9 | 164 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 44 | 236..412 | 177 | 162 | 0 | 162 | 0 | 0 | 162 | - |
| 45 | 242..564 | 323 | 243 | 13 | 230 | 5 | 145 | 15 | 79135, 79136, 79139 |
| 46 | 245..466 | 222 | 143 | 76 | 67 | 17 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 50 | 271..492 | 222 | 164 | 0 | 164 | 0 | 0 | 164 | - |
| 57 | 280..592 | 313 | 248 | 61 | 187 | 8 | 138 | 29 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 62 | 286..371 | 86 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 66 | 292..406 | 115 | 93 | 0 | 93 | 0 | 0 | 93 | - |
| 68 | 300..455 | 156 | 109 | 0 | 109 | 0 | 0 | 109 | - |
| 71 | 303..461 | 159 | 108 | 77 | 31 | 15 | 5 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79108, 79132, 79134 |
| 74 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 75 | 342..499 | 158 | 128 | 66 | 62 | 24 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79135 |
| 79 | 346..442 | 97 | 69 | 20 | 49 | 11 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 82 | 367..486 | 120 | 83 | 0 | 83 | 0 | 0 | 83 | - |
| 86 | 394..446 | 53 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 91 | 412..607 | 196 | 159 | 0 | 159 | 0 | 0 | 159 | - |
| 93 | 434..486 | 53 | 27 | 5 | 22 | 5 | 10 | 0 | 79135, 79136 |
| 106 | 496..606 | 111 | 104 | 0 | 104 | 0 | 0 | 104 | - |
| 115 | 525..614 | 90 | 75 | 0 | 75 | 0 | 0 | 75 | - |
| 121 | 532..546 | 15 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 122 | 532..537 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 133 | 595..596 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 142 | 659..665 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 72; matched pairs: 1787; unmatched reference entries: 8355; unmatched candidate entries: 3927
- identity switches: 147; fragmentation (coverage interruptions): 408; orphan candidate ids (never on a reference object): 58

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
- f207: ref 79134: 26 -> 33 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 26 -> 33 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 26 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 24 -> 26 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 26 -> 33 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 24 -> 26 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 6 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 26 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 26 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 26 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 26 -> 33 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 26 -> 24 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 33 -> 26 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 33 -> 26 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 33 -> 26 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 33 -> 26 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 33 -> 26 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 26 -> 33 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 26 -> 33 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 26 -> 33 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 24 -> 26 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 26 -> 33 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 24 -> 26 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 26 -> 24 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78971: 6 -> 26 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 26 -> 33 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 33 -> 24 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 26 -> 24 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 26 -> 6 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 26 -> 24 at (1359, 2995.5), 18 frames after previous cover
- f244: ref 78971: 6 -> 26 at (1106.5, 2984.5), 2 frames after previous cover
- f245: ref 78899: 26 -> 46 at (1179, 2985.5), 5 frames after previous cover
- f245: ref 79102: 26 -> 24 at (1254.5, 2986), 11 frames after previous cover
- f246: ref 79097: 24 -> 46 at (1199.5, 2985), 7 frames after previous cover
- f247: ref 79111: 24 -> 33 at (1328.5, 2993.5), 5 frames after previous cover
- f251: ref 79122: 24 -> 33 at (1330.5, 2994), 76 frames after previous cover
- f253: ref 78897: 24 -> 26 at (1100.5, 2987.5), 27 frames after previous cover
- f253: ref 79105: 33 -> 24 at (1236, 2985.5), 17 frames after previous cover
- f255: ref 79037: 26 -> 46 at (1069.5, 2987.5), 4 frames after previous cover
- f257: ref 78899: 46 -> 26 at (1103, 2985), 3 frames after previous cover
- f258: ref 78899: 26 -> 46 at (1098, 2986.5), 1 frames after previous cover
- f258: ref 78971: 26 -> 6 at (1018, 2985.5), 12 frames after previous cover
- f260: ref 78897: 26 -> 46 at (1057.5, 2987.5), 6 frames after previous cover
- f261: ref 79108: 24 -> 33 at (1218.5, 2983.5), 1 frames after previous cover
- f261: ref 79110: 33 -> 24 at (1234.5, 2983), 3 frames after previous cover
- f263: ref 79097: 46 -> 24 at (1090, 2983.5), 4 frames after previous cover
- ... 87 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 6 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 11 | 8 | 6 (6), 75 (3), 46 (2) |
| 78969 | 352 (80..434) | 103 | 45 | 6 (66), 46 (18), 75 (17), 24 (2) |
| 78971 | 352 (84..439) | 24 | 14 | 75 (11), 6 (5), 26 (4), 46 (3), 24 (1) |
| 79045 | 355 (84..443) | 31 | 11 | 46 (26), 26 (3), 71 (1), 75 (1) |
| 79037 | 355 (86..445) | 25 | 17 | 46 (12), 26 (5), 71 (3), 24 (2), 75 (2), 6 (1) |
| 78897 | 345 (89..450) | 43 | 24 | 46 (16), 24 (11), 71 (10), 75 (4), 26 (2) |
| 78899 | 365 (91..455) | 62 | 37 | 46 (21), 24 (19), 71 (13), 26 (4), 75 (3), 79 (2) |
| 79097 | 366 (94..461) | 78 | 43 | 24 (36), 71 (24), 26 (5), 46 (5), 79 (5), 75 (3) |
| 79098 | 360 (97..467) | 36 | 20 | 71 (27), 75 (5), 26 (2), 24 (2) |
| 79102 | 371 (98..477) | 28 | 15 | 71 (16), 75 (4), 26 (3), 24 (3), 79 (1), 46 (1) |
| 79103 | 380 (99..481) | 22 | 10 | 24 (10), 46 (5), 75 (5), 26 (2) |
| 79105 | 379 (101..484) | 9 | 5 | 24 (3), 26 (2), 33 (2), 79 (1), 46 (1) |
| 79108 | 385 (104..492) | 22 | 13 | 24 (6), 75 (4), 46 (4), 33 (3), 26 (2), 71 (2), 79 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 75 (11), 33 (5), 26 (2), 24 (2), 46 (1) |
| 79111 | 386 (109..500) | 15 | 7 | 75 (8), 33 (4), 24 (2), 26 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 33 (6), 26 (2), 71 (2), 79 (1), 36 (1), 57 (1) |
| 79116 | 411 (114..530) | 40 | 9 | 57 (37), 36 (3) |
| 79122 | 404 (118..532) | 26 | 14 | 57 (12), 79 (10), 33 (2), 24 (1), 36 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 36 (57), 26 (4), 33 (2), 24 (1), 71 (1) |
| 79128 | 402 (124..527) | 22 | 14 | 36 (7), 26 (6), 33 (5), 79 (2), 24 (1), 75 (1) |
| 79134 | 407 (127..533) | 20 | 15 | 26 (5), 33 (4), 57 (4), 79 (3), 36 (2), 24 (1), 71 (1) |
| 79135 | 409 (129..542) | 55 | 31 | 45 (14), 93 (11), 33 (10), 36 (6), 26 (5), 57 (4), 24 (3), 75 (1), 79 (1) |
| 79139 | 406 (132..537) | 30 | 14 | 33 (13), 57 (8), 36 (5), 45 (2), 26 (1), 79 (1) |
| 79136 | 393 (136..538) | 13 | 6 | 33 (7), 93 (2), 57 (2), 26 (1), 45 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 35 | 202..223 | 22 | 0 | 22 |
| 40 | 219..236 | 18 | 0 | 18 |
| 42 | 227..247 | 21 | 0 | 21 |
| 44 | 236..426 | 191 | 0 | 191 |
| 47 | 252..272 | 21 | 0 | 21 |
| 50 | 271..506 | 236 | 0 | 236 |
| 53 | 277..304 | 28 | 0 | 28 |
| 58 | 281..298 | 18 | 0 | 18 |
| 62 | 286..385 | 100 | 0 | 100 |
| 66 | 292..420 | 129 | 0 | 129 |
| 68 | 300..469 | 170 | 0 | 170 |
| 69 | 302..325 | 24 | 0 | 24 |
| 72 | 327..349 | 23 | 0 | 23 |
| 74 | 338..352 | 15 | 0 | 15 |
| 77 | 343..360 | 18 | 0 | 18 |
| 80 | 352..374 | 23 | 0 | 23 |
| 82 | 367..500 | 134 | 0 | 134 |
| 83 | 377..398 | 22 | 0 | 22 |
| 86 | 394..460 | 67 | 0 | 67 |
| 89 | 405..422 | 18 | 0 | 18 |
| 91 | 412..621 | 210 | 0 | 210 |
| 92 | 427..447 | 21 | 0 | 21 |
| 96 | 453..470 | 18 | 0 | 18 |
| 98 | 467..484 | 18 | 0 | 18 |
| 103 | 477..497 | 21 | 0 | 21 |
| 106 | 496..620 | 125 | 0 | 125 |
| 109 | 502..522 | 21 | 0 | 21 |
| 115 | 525..628 | 104 | 0 | 104 |
| 117 | 529..546 | 18 | 0 | 18 |
| 119 | 531..549 | 19 | 0 | 19 |
| 121 | 532..560 | 29 | 0 | 29 |
| 122 | 532..551 | 20 | 0 | 20 |
| 126 | 552..575 | 24 | 0 | 24 |
| 132 | 591..608 | 18 | 0 | 18 |
| 133 | 595..610 | 16 | 0 | 16 |
| 136 | 602..624 | 23 | 0 | 23 |
| 138 | 627..648 | 22 | 0 | 22 |
| 140 | 653..670 | 18 | 0 | 18 |
| 142 | 659..679 | 21 | 0 | 21 |
| 144 | 677..699 | 23 | 0 | 23 |
| ... | 18 more | | | |

### Gaps and durations of candidate tracks
- tracks: 72; lifespan min/median/max: 7/23/975; tracks with internal gaps: 14; total internal gaps: 210; longest internal gap: 177; tracks ending in coasting: 69 (trailing rows total 2675)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..21 | 18 | 18 | 3 | 15 | 1 | 2 | 13 | 78911 |
| 5 | 34..1008 | 975 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..288 | 207 | 207 | 78 | 129 | 24 | 53 | 15 | 78896, 78969, 78971, 79037 |
| 24 | 169..316 | 148 | 148 | 106 | 42 | 17 | 4 | 16 | 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79128, 79132, 79134, 79135 |
| 26 | 176..257 | 82 | 82 | 61 | 21 | 17 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 33 | 196..283 | 88 | 88 | 63 | 25 | 11 | 4 | 10 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 35 | 202..223 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 36 | 206..528 | 323 | 323 | 82 | 241 | 12 | 164 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 40 | 219..236 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 42 | 227..247 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 44 | 236..426 | 191 | 191 | 0 | 191 | 0 | 0 | 191 | - |
| 45 | 242..578 | 337 | 337 | 17 | 320 | 6 | 177 | 39 | 79135, 79136, 79139 |
| 46 | 245..480 | 236 | 236 | 115 | 121 | 33 | 23 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 47 | 252..272 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 50 | 271..506 | 236 | 236 | 0 | 236 | 0 | 0 | 236 | - |
| 53 | 277..304 | 28 | 28 | 0 | 28 | 0 | 0 | 28 | - |
| 57 | 280..606 | 327 | 327 | 68 | 259 | 11 | 148 | 73 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 58 | 281..298 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 62 | 286..385 | 100 | 100 | 0 | 100 | 0 | 0 | 100 | - |
| 66 | 292..420 | 129 | 129 | 0 | 129 | 0 | 0 | 129 | - |
| 68 | 300..469 | 170 | 170 | 0 | 170 | 0 | 0 | 170 | - |
| 69 | 302..325 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 71 | 303..475 | 173 | 173 | 100 | 73 | 26 | 11 | 11 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79108, 79115, 79132, 79134 |
| 72 | 327..349 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 74 | 338..352 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 75 | 342..513 | 172 | 172 | 83 | 89 | 29 | 15 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79135 |
| 77 | 343..360 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 79 | 346..456 | 111 | 111 | 28 | 83 | 13 | 22 | 8 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 80 | 352..374 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 82 | 367..500 | 134 | 134 | 0 | 134 | 0 | 0 | 134 | - |
| 83 | 377..398 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 86 | 394..460 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 89 | 405..422 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 91 | 412..621 | 210 | 210 | 0 | 210 | 0 | 0 | 210 | - |
| 92 | 427..447 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 93 | 434..500 | 67 | 67 | 13 | 54 | 6 | 15 | 8 | 79135, 79136 |
| 96 | 453..470 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 98 | 467..484 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 103 | 477..497 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 106 | 496..620 | 125 | 125 | 0 | 125 | 0 | 0 | 125 | - |
| 109 | 502..522 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 115 | 525..628 | 104 | 104 | 0 | 104 | 0 | 0 | 104 | - |
| 117 | 529..546 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 119 | 531..549 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 121 | 532..560 | 29 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 122 | 532..551 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 126 | 552..575 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 132 | 591..608 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 133 | 595..610 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 136 | 602..624 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 138 | 627..648 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 140 | 653..670 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 142 | 659..679 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 144 | 677..699 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 145 | 703..722 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 146 | 715..732 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 150 | 727..747 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 152 | 752..772 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 153 | 777..796 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 160 | 802..825 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 162 | 827..848 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 163 | 839..856 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 168 | 852..874 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 171 | 877..899 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 172 | 901..920 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 173 | 903..925 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 181 | 927..949 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 182 | 933..954 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 183 | 952..971 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 185 | 963..979 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 187 | 977..997 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 191 | 1002..1008 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 29; matched pairs: 1787; unmatched reference entries: 8355; unmatched candidate entries: 3044
- identity switches: 147; fragmentation (coverage interruptions): 408; orphan candidate ids (never on a reference object): 15

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
- f207: ref 79134: 26 -> 33 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 26 -> 33 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 26 -> 33 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 24 -> 26 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 26 -> 33 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 24 -> 26 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 6 -> 24 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 24 -> 26 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 26 -> 33 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 24 -> 33 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 26 -> 33 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 26 -> 33 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 26 -> 24 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 33 -> 26 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 33 -> 26 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 33 -> 26 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 33 -> 26 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 33 -> 26 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 26 -> 33 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 26 -> 33 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 26 -> 33 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 24 -> 26 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 26 -> 33 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 24 -> 26 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 26 -> 24 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78971: 6 -> 26 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 26 -> 33 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 33 -> 24 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 26 -> 24 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 26 -> 6 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 26 -> 24 at (1359, 2995.5), 18 frames after previous cover
- f244: ref 78971: 6 -> 26 at (1106.5, 2984.5), 2 frames after previous cover
- f245: ref 78899: 26 -> 46 at (1179, 2985.5), 5 frames after previous cover
- f245: ref 79102: 26 -> 24 at (1254.5, 2986), 11 frames after previous cover
- f246: ref 79097: 24 -> 46 at (1199.5, 2985), 7 frames after previous cover
- f247: ref 79111: 24 -> 33 at (1328.5, 2993.5), 5 frames after previous cover
- f251: ref 79122: 24 -> 33 at (1330.5, 2994), 76 frames after previous cover
- f253: ref 78897: 24 -> 26 at (1100.5, 2987.5), 27 frames after previous cover
- f253: ref 79105: 33 -> 24 at (1236, 2985.5), 17 frames after previous cover
- f255: ref 79037: 26 -> 46 at (1069.5, 2987.5), 4 frames after previous cover
- f257: ref 78899: 46 -> 26 at (1103, 2985), 3 frames after previous cover
- f258: ref 78899: 26 -> 46 at (1098, 2986.5), 1 frames after previous cover
- f258: ref 78971: 26 -> 6 at (1018, 2985.5), 12 frames after previous cover
- f260: ref 78897: 26 -> 46 at (1057.5, 2987.5), 6 frames after previous cover
- f261: ref 79108: 24 -> 33 at (1218.5, 2983.5), 1 frames after previous cover
- f261: ref 79110: 33 -> 24 at (1234.5, 2983), 3 frames after previous cover
- f263: ref 79097: 46 -> 24 at (1090, 2983.5), 4 frames after previous cover
- ... 87 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 6 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 11 | 8 | 6 (6), 75 (3), 46 (2) |
| 78969 | 352 (80..434) | 103 | 45 | 6 (66), 46 (18), 75 (17), 24 (2) |
| 78971 | 352 (84..439) | 24 | 14 | 75 (11), 6 (5), 26 (4), 46 (3), 24 (1) |
| 79045 | 355 (84..443) | 31 | 11 | 46 (26), 26 (3), 71 (1), 75 (1) |
| 79037 | 355 (86..445) | 25 | 17 | 46 (12), 26 (5), 71 (3), 24 (2), 75 (2), 6 (1) |
| 78897 | 345 (89..450) | 43 | 24 | 46 (16), 24 (11), 71 (10), 75 (4), 26 (2) |
| 78899 | 365 (91..455) | 62 | 37 | 46 (21), 24 (19), 71 (13), 26 (4), 75 (3), 79 (2) |
| 79097 | 366 (94..461) | 78 | 43 | 24 (36), 71 (24), 26 (5), 46 (5), 79 (5), 75 (3) |
| 79098 | 360 (97..467) | 36 | 20 | 71 (27), 75 (5), 26 (2), 24 (2) |
| 79102 | 371 (98..477) | 28 | 15 | 71 (16), 75 (4), 26 (3), 24 (3), 79 (1), 46 (1) |
| 79103 | 380 (99..481) | 22 | 10 | 24 (10), 46 (5), 75 (5), 26 (2) |
| 79105 | 379 (101..484) | 9 | 5 | 24 (3), 26 (2), 33 (2), 79 (1), 46 (1) |
| 79108 | 385 (104..492) | 22 | 13 | 24 (6), 75 (4), 46 (4), 33 (3), 26 (2), 71 (2), 79 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 75 (11), 33 (5), 26 (2), 24 (2), 46 (1) |
| 79111 | 386 (109..500) | 15 | 7 | 75 (8), 33 (4), 24 (2), 26 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 33 (6), 26 (2), 71 (2), 79 (1), 36 (1), 57 (1) |
| 79116 | 411 (114..530) | 40 | 9 | 57 (37), 36 (3) |
| 79122 | 404 (118..532) | 26 | 14 | 57 (12), 79 (10), 33 (2), 24 (1), 36 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 36 (57), 26 (4), 33 (2), 24 (1), 71 (1) |
| 79128 | 402 (124..527) | 22 | 14 | 36 (7), 26 (6), 33 (5), 79 (2), 24 (1), 75 (1) |
| 79134 | 407 (127..533) | 20 | 15 | 26 (5), 33 (4), 57 (4), 79 (3), 36 (2), 24 (1), 71 (1) |
| 79135 | 409 (129..542) | 55 | 31 | 45 (14), 93 (11), 33 (10), 36 (6), 26 (5), 57 (4), 24 (3), 75 (1), 79 (1) |
| 79139 | 406 (132..537) | 30 | 14 | 33 (13), 57 (8), 36 (5), 45 (2), 26 (1), 79 (1) |
| 79136 | 393 (136..538) | 13 | 6 | 33 (7), 93 (2), 57 (2), 26 (1), 45 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 44 | 236..426 | 191 | 0 | 191 |
| 50 | 271..506 | 236 | 0 | 236 |
| 62 | 286..385 | 100 | 0 | 100 |
| 66 | 292..420 | 129 | 0 | 129 |
| 68 | 300..469 | 170 | 0 | 170 |
| 74 | 338..352 | 15 | 0 | 15 |
| 82 | 367..500 | 134 | 0 | 134 |
| 86 | 394..460 | 67 | 0 | 67 |
| 91 | 412..621 | 210 | 0 | 210 |
| 106 | 496..620 | 125 | 0 | 125 |
| 115 | 525..628 | 104 | 0 | 104 |
| 121 | 532..560 | 29 | 0 | 29 |
| 122 | 532..551 | 20 | 0 | 20 |
| 133 | 595..610 | 16 | 0 | 16 |
| 142 | 659..679 | 21 | 0 | 21 |

### Gaps and durations of candidate tracks
- tracks: 29; lifespan min/median/max: 15/129/975; tracks with internal gaps: 14; total internal gaps: 210; longest internal gap: 177; tracks ending in coasting: 26 (trailing rows total 1792)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..21 | 18 | 18 | 3 | 15 | 1 | 2 | 13 | 78911 |
| 5 | 34..1008 | 975 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 82..288 | 207 | 207 | 78 | 129 | 24 | 53 | 15 | 78896, 78969, 78971, 79037 |
| 24 | 169..316 | 148 | 148 | 106 | 42 | 17 | 4 | 16 | 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79128, 79132, 79134, 79135 |
| 26 | 176..257 | 82 | 82 | 61 | 21 | 17 | 2 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 33 | 196..283 | 88 | 88 | 63 | 25 | 11 | 4 | 10 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 36 | 206..528 | 323 | 323 | 82 | 241 | 12 | 164 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 44 | 236..426 | 191 | 191 | 0 | 191 | 0 | 0 | 191 | - |
| 45 | 242..578 | 337 | 337 | 17 | 320 | 6 | 177 | 39 | 79135, 79136, 79139 |
| 46 | 245..480 | 236 | 236 | 115 | 121 | 33 | 23 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 50 | 271..506 | 236 | 236 | 0 | 236 | 0 | 0 | 236 | - |
| 57 | 280..606 | 327 | 327 | 68 | 259 | 11 | 148 | 73 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 62 | 286..385 | 100 | 100 | 0 | 100 | 0 | 0 | 100 | - |
| 66 | 292..420 | 129 | 129 | 0 | 129 | 0 | 0 | 129 | - |
| 68 | 300..469 | 170 | 170 | 0 | 170 | 0 | 0 | 170 | - |
| 71 | 303..475 | 173 | 173 | 100 | 73 | 26 | 11 | 11 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79108, 79115, 79132, 79134 |
| 74 | 338..352 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 75 | 342..513 | 172 | 172 | 83 | 89 | 29 | 15 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79135 |
| 79 | 346..456 | 111 | 111 | 28 | 83 | 13 | 22 | 8 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 82 | 367..500 | 134 | 134 | 0 | 134 | 0 | 0 | 134 | - |
| 86 | 394..460 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 91 | 412..621 | 210 | 210 | 0 | 210 | 0 | 0 | 210 | - |
| 93 | 434..500 | 67 | 67 | 13 | 54 | 6 | 15 | 8 | 79135, 79136 |
| 106 | 496..620 | 125 | 125 | 0 | 125 | 0 | 0 | 125 | - |
| 115 | 525..628 | 104 | 104 | 0 | 104 | 0 | 0 | 104 | - |
| 121 | 532..560 | 29 | 29 | 0 | 29 | 0 | 0 | 29 | - |
| 122 | 532..551 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 133 | 595..610 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 142 | 659..679 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
