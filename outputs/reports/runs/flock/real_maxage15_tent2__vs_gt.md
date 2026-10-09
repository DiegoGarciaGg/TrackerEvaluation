# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 15, "tentative_threshold": 2}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=799d24d98a8c git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage15_tent2/tracks.csv sha256=dba9b74b0da456cf
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage15_tent2
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
| observations | none | 4 | 0.246 | 0.620 | -0.160 | 1.03 | 0.156 | 99 | 269.0 |
| observations | none | 6 | 0.258 | 0.605 | -0.132 | 1.43 | 0.167 | 132 | 358.0 |
| observations | none | 8 | 0.266 | 0.584 | -0.112 | 1.81 | 0.172 | 151 | 423.0 |
| observations | none | 12 | 0.275 | 0.563 | -0.066 | 2.92 | 0.185 | 169 | 484.0 |
| observations | ignore | 4 | 0.250 | 0.620 | -0.119 | 1.03 | 0.161 | 99 | 269.0 |
| observations | ignore | 6 | 0.263 | 0.605 | -0.091 | 1.43 | 0.172 | 132 | 358.0 |
| observations | ignore | 8 | 0.271 | 0.584 | -0.070 | 1.81 | 0.177 | 151 | 423.0 |
| observations | ignore | 12 | 0.280 | 0.563 | -0.025 | 2.92 | 0.191 | 169 | 484.0 |
| updates | none | 4 | 0.229 | 0.584 | -0.364 | 1.12 | 0.137 | 128 | 322.0 |
| updates | none | 6 | 0.241 | 0.558 | -0.324 | 1.61 | 0.148 | 165 | 407.0 |
| updates | none | 8 | 0.249 | 0.531 | -0.288 | 2.16 | 0.154 | 184 | 464.0 |
| updates | none | 12 | 0.258 | 0.502 | -0.224 | 3.45 | 0.169 | 202 | 513.0 |
| updates | ignore | 4 | 0.238 | 0.584 | -0.248 | 1.12 | 0.148 | 128 | 322.0 |
| updates | ignore | 6 | 0.251 | 0.558 | -0.208 | 1.61 | 0.160 | 165 | 407.0 |
| updates | ignore | 8 | 0.259 | 0.531 | -0.172 | 2.16 | 0.166 | 184 | 464.0 |
| updates | ignore | 12 | 0.269 | 0.502 | -0.107 | 3.45 | 0.182 | 202 | 513.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 93; matched pairs: 1648; unmatched reference entries: 8494; unmatched candidate entries: 2630
- identity switches: 151; fragmentation (coverage interruptions): 422; orphan candidate ids (never on a reference object): 76

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 4 at (1819, 3367), 24 frames after previous cover
- f166: ref 79139: 10 -> 13 at (1953.5, 3016), 5 frames after previous cover
- f173: ref 79135: 10 -> 13 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 10 -> 13 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 10 -> 13 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 13 -> 14 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 10 -> 13 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 13 -> 14 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 5 -> 10 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 13 -> 14 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 10 -> 13 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 14 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78971: 10 -> 13 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 13 -> 14 at (1777.5, 3018.5), 7 frames after previous cover
- f192: ref 78899: 13 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 5 -> 13 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 10 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 14 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 10 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 13 -> 14 at (1646.5, 3013), 25 frames after previous cover
- f207: ref 79134: 14 -> 17 at (1655.5, 3014), 15 frames after previous cover
- f212: ref 79128: 14 -> 17 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 10 -> 14 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 14 -> 17 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 10 -> 14 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 13 -> 5 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 5 -> 14 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 14 -> 17 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 10 -> 17 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 14 -> 17 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 14 -> 17 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 14 -> 5 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 17 -> 14 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 17 -> 14 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 17 -> 14 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 17 -> 14 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 17 -> 14 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 14 -> 17 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 14 -> 17 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 14 -> 17 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 5 -> 14 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 14 -> 17 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 5 -> 14 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 14 -> 5 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 5 -> 13 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 78971: 13 -> 14 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 14 -> 17 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 17 -> 5 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 14 -> 5 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 14 -> 13 at (1119, 2986), 3 frames after previous cover
- f242: ref 79097: 5 -> 29 at (1225, 2985), 3 frames after previous cover
- f242: ref 79111: 14 -> 5 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 14 -> 29 at (1179, 2985.5), 5 frames after previous cover
- f255: ref 79037: 14 -> 29 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 5 -> 17 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 5 -> 29 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 5 -> 17 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 29 -> 5 at (1090, 2983.5), 4 frames after previous cover
- f272: ref 79045: 10 -> 29 at (945.5, 2991.5), 89 frames after previous cover
- f274: ref 78899: 29 -> 5 at (996, 2989.5), 5 frames after previous cover
- ... 91 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 9 | 4 (971), 0 (4) |
| 78896 | 350 (76..429) | 11 | 9 | 5 (4), 13 (3), 49 (3), 29 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 13 (54), 5 (13), 29 (13), 49 (12) |
| 78971 | 352 (84..439) | 18 | 12 | 49 (10), 13 (4), 5 (1), 10 (1), 14 (1), 29 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 29 (14), 10 (1), 40 (1), 49 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 29 (7), 14 (2), 40 (2), 49 (2), 10 (1), 13 (1), 5 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 29 (9), 5 (7), 40 (5), 49 (4), 10 (2) |
| 78899 | 365 (91..455) | 51 | 41 | 5 (16), 29 (15), 40 (12), 49 (3), 13 (2), 14 (2), 53 (1) |
| 79097 | 366 (94..461) | 71 | 45 | 5 (32), 40 (20), 29 (8), 14 (5), 49 (3), 10 (1), 43 (1), 53 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 40 (19), 5 (2), 49 (2), 14 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 40 (16), 49 (4), 5 (2), 53 (1), 29 (1) |
| 79103 | 380 (99..481) | 21 | 13 | 5 (5), 40 (5), 49 (5), 29 (3), 14 (2), 10 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 14 (2), 17 (1), 40 (1), 53 (1), 29 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 17 (3), 29 (3), 14 (2), 40 (2), 49 (2), 10 (1), 5 (1), 53 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 49 (8), 17 (4), 14 (2), 29 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 49 (5), 17 (2), 10 (1), 14 (1), 5 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 17 (4), 14 (2), 53 (1), 20 (1), 32 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 32 (37), 20 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 53 (10), 32 (9), 20 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 20 (56), 14 (3), 17 (2), 10 (1), 13 (1), 40 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 17 (5), 20 (4), 14 (3), 10 (2), 13 (1), 49 (1), 53 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 10 (5), 13 (4), 17 (4), 32 (3), 14 (2), 20 (2), 40 (1), 47 (1), 49 (1), 53 (1) |
| 79135 | 409 (129..542) | 50 | 42 | 17 (15), 28 (10), 10 (6), 20 (5), 67 (4), 32 (3), 14 (2), 47 (2), 13 (1), 49 (1), 53 (1) |
| 79139 | 406 (132..537) | 29 | 19 | 17 (9), 32 (7), 10 (3), 14 (3), 13 (2), 28 (2), 47 (1), 20 (1), 53 (1) |
| 79136 | 393 (136..538) | 4 | 3 | 13 (1), 67 (1), 28 (1), 32 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..24 | 3 | 0 | 3 |
| 2 | 24..30 | 7 | 0 | 3 |
| 3 | 31..31 | 1 | 0 | 1 |
| 6 | 87..89 | 3 | 0 | 3 |
| 7 | 92..99 | 8 | 0 | 3 |
| 11 | 149..154 | 6 | 0 | 3 |
| 12 | 150..155 | 6 | 0 | 4 |
| 15 | 175..175 | 1 | 0 | 1 |
| 19 | 199..209 | 11 | 0 | 9 |
| 23 | 213..216 | 4 | 0 | 3 |
| 24 | 216..222 | 7 | 0 | 6 |
| 25 | 224..233 | 10 | 0 | 10 |
| 27 | 233..412 | 180 | 0 | 163 |
| 30 | 249..258 | 10 | 0 | 10 |
| 33 | 268..308 | 41 | 0 | 22 |
| 35 | 274..290 | 17 | 0 | 16 |
| 37 | 275..455 | 181 | 0 | 135 |
| 38 | 277..406 | 130 | 0 | 108 |
| 39 | 278..284 | 7 | 0 | 6 |
| 41 | 297..352 | 56 | 0 | 31 |
| 42 | 299..311 | 13 | 0 | 11 |
| 46 | 324..335 | 12 | 0 | 12 |
| 48 | 329..492 | 164 | 0 | 124 |
| 51 | 340..346 | 7 | 0 | 6 |
| 54 | 349..360 | 12 | 0 | 11 |
| 56 | 364..486 | 123 | 0 | 86 |
| 58 | 374..384 | 11 | 0 | 11 |
| 60 | 388..446 | 59 | 0 | 43 |
| 62 | 399..401 | 3 | 0 | 3 |
| 63 | 402..408 | 7 | 0 | 6 |
| 65 | 409..607 | 199 | 0 | 162 |
| 66 | 424..433 | 10 | 0 | 10 |
| 69 | 449..470 | 22 | 0 | 8 |
| 70 | 450..456 | 7 | 0 | 6 |
| 72 | 466..476 | 11 | 0 | 5 |
| 73 | 472..495 | 24 | 0 | 4 |
| 74 | 474..483 | 10 | 0 | 10 |
| 75 | 493..606 | 114 | 0 | 107 |
| 76 | 499..508 | 10 | 0 | 10 |
| 77 | 502..614 | 113 | 0 | 86 |
| ... | 36 more | | | |

### Gaps and durations of candidate tracks
- tracks: 93; lifespan min/median/max: 1/11/978; tracks with internal gaps: 16; total internal gaps: 152; longest internal gap: 198; tracks ending in coasting: 85 (trailing rows total 1620)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..7 | 7 | 5 | 4 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 22..24 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 2 | 24..30 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 3 | 31..31 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 4 | 31..1008 | 978 | 976 | 971 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 79..305 | 227 | 187 | 85 | 102 | 13 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 6 | 87..89 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 7 | 92..99 | 8 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 10 | 138..187 | 50 | 33 | 26 | 7 | 6 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 11 | 149..154 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 12 | 150..155 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 13 | 160..274 | 115 | 100 | 74 | 26 | 17 | 3 | 1 | 78896, 78899, 78969, 78971, 79037, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 175..243 | 69 | 44 | 35 | 9 | 5 | 2 | 1 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 15 | 175..175 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 17 | 187..269 | 83 | 60 | 49 | 11 | 10 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 19 | 199..209 | 11 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 20 | 203..514 | 312 | 301 | 71 | 230 | 8 | 198 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 213..216 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 24 | 216..222 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 25 | 224..233 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 27 | 233..412 | 180 | 163 | 0 | 163 | 0 | 0 | 163 | - |
| 28 | 239..564 | 326 | 246 | 13 | 233 | 5 | 148 | 15 | 79135, 79136, 79139 |
| 29 | 242..466 | 225 | 142 | 77 | 65 | 17 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 30 | 249..258 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 32 | 265..592 | 328 | 258 | 61 | 197 | 8 | 148 | 29 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 33 | 268..308 | 41 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 35 | 274..290 | 17 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 37 | 275..455 | 181 | 135 | 0 | 135 | 0 | 0 | 135 | - |
| 38 | 277..406 | 130 | 108 | 0 | 108 | 0 | 0 | 108 | - |
| 39 | 278..284 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 40 | 280..461 | 182 | 120 | 85 | 35 | 16 | 5 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79132, 79134 |
| 41 | 297..352 | 56 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 42 | 299..311 | 13 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 43 | 300..302 | 3 | 3 | 1 | 2 | 0 | 0 | 2 | 79097 |
| 46 | 324..335 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 47 | 328..338 | 11 | 6 | 4 | 2 | 1 | 1 | 1 | 79134, 79135, 79139 |
| 48 | 329..492 | 164 | 124 | 0 | 124 | 0 | 0 | 124 | - |
| 49 | 339..499 | 161 | 131 | 67 | 64 | 25 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 51 | 340..346 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 53 | 343..442 | 100 | 72 | 20 | 52 | 11 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 54 | 349..360 | 12 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 56 | 364..486 | 123 | 86 | 0 | 86 | 0 | 0 | 86 | - |
| 58 | 374..384 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 60 | 388..446 | 59 | 43 | 0 | 43 | 0 | 0 | 43 | - |
| 62 | 399..401 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 63 | 402..408 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 65 | 409..607 | 199 | 162 | 0 | 162 | 0 | 0 | 162 | - |
| 66 | 424..433 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 67 | 431..486 | 56 | 30 | 5 | 25 | 5 | 13 | 0 | 79135, 79136 |
| 69 | 449..470 | 22 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 70 | 450..456 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 72 | 466..476 | 11 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 73 | 472..495 | 24 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 74 | 474..483 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 75 | 493..606 | 114 | 107 | 0 | 107 | 0 | 0 | 107 | - |
| 76 | 499..508 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 77 | 502..614 | 113 | 86 | 0 | 86 | 0 | 0 | 86 | - |
| 79 | 524..535 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 80 | 526..532 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 83 | 529..537 | 9 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 84 | 529..546 | 18 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 88 | 549..561 | 13 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 90 | 574..610 | 37 | 14 | 0 | 14 | 0 | 0 | 14 | - |
| 93 | 588..594 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 94 | 592..596 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 98 | 624..634 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 99 | 649..649 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 100 | 650..656 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 102 | 656..665 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 104 | 674..685 | 12 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 105 | 700..708 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 106 | 712..718 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 108 | 720..728 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 110 | 724..733 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 111 | 749..758 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 112 | 774..782 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 114 | 785..794 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 116 | 799..811 | 13 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 118 | 824..834 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 119 | 836..842 | 7 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| ... | 13 more in JSON | | | | | | | | |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 43; matched pairs: 1648; unmatched reference entries: 8494; unmatched candidate entries: 2212
- identity switches: 151; fragmentation (coverage interruptions): 422; orphan candidate ids (never on a reference object): 26

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 4 at (1819, 3367), 24 frames after previous cover
- f166: ref 79139: 10 -> 13 at (1953.5, 3016), 5 frames after previous cover
- f173: ref 79135: 10 -> 13 at (1888, 3016.5), 3 frames after previous cover
- f174: ref 79134: 10 -> 13 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 10 -> 13 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 13 -> 14 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 10 -> 13 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 13 -> 14 at (1843, 3015), 7 frames after previous cover
- f186: ref 78971: 5 -> 10 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 13 -> 14 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 10 -> 13 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 14 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78971: 10 -> 13 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 13 -> 14 at (1777.5, 3018.5), 7 frames after previous cover
- f192: ref 78899: 13 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 5 -> 13 at (1414, 3008.5), 8 frames after previous cover
- f194: ref 78897: 10 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f196: ref 79139: 14 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79097: 10 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f201: ref 79132: 13 -> 14 at (1646.5, 3013), 25 frames after previous cover
- f207: ref 79134: 14 -> 17 at (1655.5, 3014), 15 frames after previous cover
- f212: ref 79128: 14 -> 17 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 10 -> 14 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 14 -> 17 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 10 -> 14 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 13 -> 5 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 5 -> 14 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 14 -> 17 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 10 -> 17 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 14 -> 17 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 14 -> 17 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 14 -> 5 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 17 -> 14 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 17 -> 14 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 17 -> 14 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 17 -> 14 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 17 -> 14 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 14 -> 17 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 14 -> 17 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 14 -> 17 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 5 -> 14 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 14 -> 17 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 5 -> 14 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 14 -> 5 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 5 -> 13 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 78971: 13 -> 14 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 14 -> 17 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 17 -> 5 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 14 -> 5 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 14 -> 13 at (1119, 2986), 3 frames after previous cover
- f242: ref 79097: 5 -> 29 at (1225, 2985), 3 frames after previous cover
- f242: ref 79111: 14 -> 5 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 14 -> 29 at (1179, 2985.5), 5 frames after previous cover
- f255: ref 79037: 14 -> 29 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 5 -> 17 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 5 -> 29 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 5 -> 17 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 29 -> 5 at (1090, 2983.5), 4 frames after previous cover
- f272: ref 79045: 10 -> 29 at (945.5, 2991.5), 89 frames after previous cover
- f274: ref 78899: 29 -> 5 at (996, 2989.5), 5 frames after previous cover
- ... 91 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 975 | 9 | 4 (971), 0 (4) |
| 78896 | 350 (76..429) | 11 | 9 | 5 (4), 13 (3), 49 (3), 29 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 13 (54), 5 (13), 29 (13), 49 (12) |
| 78971 | 352 (84..439) | 18 | 12 | 49 (10), 13 (4), 5 (1), 10 (1), 14 (1), 29 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 29 (14), 10 (1), 40 (1), 49 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 29 (7), 14 (2), 40 (2), 49 (2), 10 (1), 13 (1), 5 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 29 (9), 5 (7), 40 (5), 49 (4), 10 (2) |
| 78899 | 365 (91..455) | 51 | 41 | 5 (16), 29 (15), 40 (12), 49 (3), 13 (2), 14 (2), 53 (1) |
| 79097 | 366 (94..461) | 71 | 45 | 5 (32), 40 (20), 29 (8), 14 (5), 49 (3), 10 (1), 43 (1), 53 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 40 (19), 5 (2), 49 (2), 14 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 40 (16), 49 (4), 5 (2), 53 (1), 29 (1) |
| 79103 | 380 (99..481) | 21 | 13 | 5 (5), 40 (5), 49 (5), 29 (3), 14 (2), 10 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 14 (2), 17 (1), 40 (1), 53 (1), 29 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 17 (3), 29 (3), 14 (2), 40 (2), 49 (2), 10 (1), 5 (1), 53 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 49 (8), 17 (4), 14 (2), 29 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 49 (5), 17 (2), 10 (1), 14 (1), 5 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 17 (4), 14 (2), 53 (1), 20 (1), 32 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 32 (37), 20 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 53 (10), 32 (9), 20 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 20 (56), 14 (3), 17 (2), 10 (1), 13 (1), 40 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 17 (5), 20 (4), 14 (3), 10 (2), 13 (1), 49 (1), 53 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 10 (5), 13 (4), 17 (4), 32 (3), 14 (2), 20 (2), 40 (1), 47 (1), 49 (1), 53 (1) |
| 79135 | 409 (129..542) | 50 | 42 | 17 (15), 28 (10), 10 (6), 20 (5), 67 (4), 32 (3), 14 (2), 47 (2), 13 (1), 49 (1), 53 (1) |
| 79139 | 406 (132..537) | 29 | 19 | 17 (9), 32 (7), 10 (3), 14 (3), 13 (2), 28 (2), 47 (1), 20 (1), 53 (1) |
| 79136 | 393 (136..538) | 4 | 3 | 13 (1), 67 (1), 28 (1), 32 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..24 | 3 | 0 | 3 |
| 6 | 87..89 | 3 | 0 | 3 |
| 12 | 150..155 | 6 | 0 | 4 |
| 23 | 213..216 | 4 | 0 | 3 |
| 27 | 233..412 | 180 | 0 | 163 |
| 33 | 268..308 | 41 | 0 | 22 |
| 37 | 275..455 | 181 | 0 | 135 |
| 38 | 277..406 | 130 | 0 | 108 |
| 41 | 297..352 | 56 | 0 | 31 |
| 48 | 329..492 | 164 | 0 | 124 |
| 56 | 364..486 | 123 | 0 | 86 |
| 60 | 388..446 | 59 | 0 | 43 |
| 65 | 409..607 | 199 | 0 | 162 |
| 72 | 466..476 | 11 | 0 | 5 |
| 73 | 472..495 | 24 | 0 | 4 |
| 75 | 493..606 | 114 | 0 | 107 |
| 77 | 502..614 | 113 | 0 | 86 |
| 83 | 529..537 | 9 | 0 | 6 |
| 84 | 529..546 | 18 | 0 | 13 |
| 94 | 592..596 | 5 | 0 | 5 |
| 102 | 656..665 | 10 | 0 | 10 |
| 108 | 720..728 | 9 | 0 | 4 |
| 114 | 785..794 | 10 | 0 | 5 |
| 122 | 847..856 | 10 | 0 | 5 |
| 132 | 912..919 | 8 | 0 | 4 |
| 141 | 975..981 | 7 | 0 | 5 |

### Gaps and durations of candidate tracks
- tracks: 43; lifespan min/median/max: 3/56/978; tracks with internal gaps: 16; total internal gaps: 152; longest internal gap: 198; tracks ending in coasting: 35 (trailing rows total 1202)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..7 | 7 | 5 | 4 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 22..24 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 4 | 31..1008 | 978 | 976 | 971 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 79..305 | 227 | 187 | 85 | 102 | 13 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 6 | 87..89 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 10 | 138..187 | 50 | 33 | 26 | 7 | 6 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 12 | 150..155 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 13 | 160..274 | 115 | 100 | 74 | 26 | 17 | 3 | 1 | 78896, 78899, 78969, 78971, 79037, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 175..243 | 69 | 44 | 35 | 9 | 5 | 2 | 1 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 17 | 187..269 | 83 | 60 | 49 | 11 | 10 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 20 | 203..514 | 312 | 301 | 71 | 230 | 8 | 198 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 213..216 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 27 | 233..412 | 180 | 163 | 0 | 163 | 0 | 0 | 163 | - |
| 28 | 239..564 | 326 | 246 | 13 | 233 | 5 | 148 | 15 | 79135, 79136, 79139 |
| 29 | 242..466 | 225 | 142 | 77 | 65 | 17 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 32 | 265..592 | 328 | 258 | 61 | 197 | 8 | 148 | 29 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 33 | 268..308 | 41 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 37 | 275..455 | 181 | 135 | 0 | 135 | 0 | 0 | 135 | - |
| 38 | 277..406 | 130 | 108 | 0 | 108 | 0 | 0 | 108 | - |
| 40 | 280..461 | 182 | 120 | 85 | 35 | 16 | 5 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79132, 79134 |
| 41 | 297..352 | 56 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 43 | 300..302 | 3 | 3 | 1 | 2 | 0 | 0 | 2 | 79097 |
| 47 | 328..338 | 11 | 6 | 4 | 2 | 1 | 1 | 1 | 79134, 79135, 79139 |
| 48 | 329..492 | 164 | 124 | 0 | 124 | 0 | 0 | 124 | - |
| 49 | 339..499 | 161 | 131 | 67 | 64 | 25 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 53 | 343..442 | 100 | 72 | 20 | 52 | 11 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 56 | 364..486 | 123 | 86 | 0 | 86 | 0 | 0 | 86 | - |
| 60 | 388..446 | 59 | 43 | 0 | 43 | 0 | 0 | 43 | - |
| 65 | 409..607 | 199 | 162 | 0 | 162 | 0 | 0 | 162 | - |
| 67 | 431..486 | 56 | 30 | 5 | 25 | 5 | 13 | 0 | 79135, 79136 |
| 72 | 466..476 | 11 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 73 | 472..495 | 24 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 75 | 493..606 | 114 | 107 | 0 | 107 | 0 | 0 | 107 | - |
| 77 | 502..614 | 113 | 86 | 0 | 86 | 0 | 0 | 86 | - |
| 83 | 529..537 | 9 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 84 | 529..546 | 18 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 94 | 592..596 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 102 | 656..665 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 108 | 720..728 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 114 | 785..794 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 122 | 847..856 | 10 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 132 | 912..919 | 8 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 141 | 975..981 | 7 | 5 | 0 | 5 | 0 | 0 | 5 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 93; matched pairs: 1881; unmatched reference entries: 8261; unmatched candidate entries: 4618
- identity switches: 184; fragmentation (coverage interruptions): 461; orphan candidate ids (never on a reference object): 76

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 4 at (1819, 3367), 23 frames after previous cover
- f161: ref 79136: 10 -> 13 at (2010, 3014.5), 20 frames after previous cover
- f166: ref 79139: 10 -> 13 at (1953.5, 3016), 4 frames after previous cover
- f173: ref 79135: 10 -> 13 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 10 -> 13 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 10 -> 13 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 13 -> 14 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 10 -> 13 at (1812, 3020), 3 frames after previous cover
- f178: ref 79136: 13 -> 14 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 13 -> 14 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 5 -> 10 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 13 -> 14 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 10 -> 13 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 14 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78969: 5 -> 10 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 10 -> 13 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 13 -> 14 at (1777.5, 3018.5), 6 frames after previous cover
- f190: ref 79045: 10 -> 13 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 17 -> 14 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 13 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 10 -> 13 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 78971: 13 -> 10 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 14 -> 17 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 10 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 13 -> 10 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 14 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 13 -> 10 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 10 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 5 -> 10 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 13 -> 14 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 10 -> 5 at (1419.5, 3003), 2 frames after previous cover
- f207: ref 79134: 14 -> 17 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 14 -> 17 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 14 -> 17 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 10 -> 14 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 14 -> 17 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 10 -> 14 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 10 -> 5 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 5 -> 14 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 14 -> 17 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 10 -> 17 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 14 -> 17 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 14 -> 17 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 14 -> 5 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 17 -> 14 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 17 -> 14 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 17 -> 14 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 17 -> 14 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 17 -> 14 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 10 -> 13 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 14 -> 17 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 14 -> 17 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 14 -> 17 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 5 -> 14 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 14 -> 17 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 5 -> 14 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 14 -> 5 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 5 -> 13 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 13 -> 14 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 14 -> 17 at (1404.5, 2987), 17 frames after previous cover
- ... 124 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 7 | 4 (973), 0 (5) |
| 78896 | 350 (76..429) | 13 | 9 | 5 (5), 13 (3), 49 (3), 29 (2) |
| 78969 | 352 (80..434) | 103 | 45 | 13 (54), 49 (17), 29 (16), 5 (14), 10 (2) |
| 78971 | 352 (84..439) | 27 | 15 | 49 (11), 13 (5), 14 (4), 10 (3), 29 (3), 5 (1) |
| 79045 | 355 (84..443) | 39 | 15 | 29 (27), 10 (4), 14 (3), 13 (2), 5 (1), 40 (1), 49 (1) |
| 79037 | 355 (86..445) | 29 | 19 | 29 (14), 14 (5), 10 (3), 40 (3), 49 (2), 13 (1), 5 (1) |
| 78897 | 345 (89..450) | 48 | 26 | 29 (19), 40 (10), 5 (9), 10 (4), 49 (4), 14 (2) |
| 78899 | 365 (91..455) | 64 | 38 | 29 (21), 5 (17), 40 (14), 14 (4), 13 (3), 49 (3), 53 (2) |
| 79097 | 366 (94..461) | 81 | 44 | 5 (33), 40 (25), 29 (8), 14 (5), 53 (5), 49 (3), 10 (1), 43 (1) |
| 79098 | 360 (97..467) | 39 | 21 | 40 (30), 49 (5), 14 (2), 5 (2) |
| 79102 | 371 (98..477) | 28 | 15 | 40 (16), 49 (4), 14 (3), 5 (3), 53 (1), 29 (1) |
| 79103 | 380 (99..481) | 29 | 13 | 5 (10), 40 (6), 29 (5), 49 (5), 14 (2), 10 (1) |
| 79105 | 379 (101..484) | 11 | 7 | 5 (4), 14 (2), 17 (2), 40 (1), 53 (1), 29 (1) |
| 79108 | 385 (104..492) | 22 | 13 | 5 (4), 49 (4), 29 (4), 17 (3), 10 (2), 14 (2), 40 (2), 53 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 49 (11), 17 (5), 14 (2), 5 (2), 29 (1) |
| 79111 | 386 (109..500) | 15 | 7 | 49 (8), 17 (4), 10 (1), 14 (1), 5 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 17 (6), 14 (2), 40 (2), 53 (1), 20 (1), 32 (1) |
| 79116 | 411 (114..530) | 40 | 9 | 32 (37), 20 (3) |
| 79122 | 404 (118..532) | 26 | 14 | 32 (12), 53 (10), 17 (2), 10 (1), 20 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 20 (57), 14 (3), 17 (2), 10 (1), 13 (1), 40 (1) |
| 79128 | 402 (124..527) | 26 | 17 | 14 (7), 20 (7), 17 (5), 10 (3), 53 (2), 13 (1), 49 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 10 (7), 14 (6), 13 (5), 17 (4), 32 (4), 53 (3), 20 (2), 40 (1), 47 (1), 49 (1) |
| 79135 | 409 (129..542) | 67 | 41 | 17 (14), 28 (14), 67 (11), 10 (9), 20 (6), 32 (4), 13 (3), 14 (2), 47 (2), 49 (1), 53 (1) |
| 79139 | 406 (132..537) | 41 | 20 | 17 (13), 32 (8), 10 (5), 47 (4), 14 (3), 20 (3), 13 (2), 28 (2), 53 (1) |
| 79136 | 393 (136..538) | 22 | 12 | 17 (7), 13 (6), 14 (2), 67 (2), 32 (2), 10 (1), 47 (1), 28 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..38 | 17 | 0 | 17 |
| 2 | 24..44 | 21 | 0 | 21 |
| 3 | 31..45 | 15 | 0 | 15 |
| 6 | 87..103 | 17 | 0 | 17 |
| 7 | 92..113 | 22 | 0 | 22 |
| 11 | 149..168 | 20 | 0 | 20 |
| 12 | 150..169 | 20 | 0 | 20 |
| 15 | 175..189 | 15 | 0 | 15 |
| 19 | 199..223 | 25 | 0 | 25 |
| 23 | 213..230 | 18 | 0 | 18 |
| 24 | 216..236 | 21 | 0 | 21 |
| 25 | 224..247 | 24 | 0 | 24 |
| 27 | 233..426 | 194 | 0 | 194 |
| 30 | 249..272 | 24 | 0 | 24 |
| 33 | 268..322 | 55 | 0 | 55 |
| 35 | 274..304 | 31 | 0 | 31 |
| 37 | 275..469 | 195 | 0 | 195 |
| 38 | 277..420 | 144 | 0 | 144 |
| 39 | 278..298 | 21 | 0 | 21 |
| 41 | 297..366 | 70 | 0 | 70 |
| 42 | 299..325 | 27 | 0 | 27 |
| 46 | 324..349 | 26 | 0 | 26 |
| 48 | 329..506 | 178 | 0 | 178 |
| 51 | 340..360 | 21 | 0 | 21 |
| 54 | 349..374 | 26 | 0 | 26 |
| 56 | 364..500 | 137 | 0 | 137 |
| 58 | 374..398 | 25 | 0 | 25 |
| 60 | 388..460 | 73 | 0 | 73 |
| 62 | 399..415 | 17 | 0 | 17 |
| 63 | 402..422 | 21 | 0 | 21 |
| 65 | 409..621 | 213 | 0 | 213 |
| 66 | 424..447 | 24 | 0 | 24 |
| 69 | 449..484 | 36 | 0 | 36 |
| 70 | 450..470 | 21 | 0 | 21 |
| 72 | 466..490 | 25 | 0 | 25 |
| 73 | 472..509 | 38 | 0 | 38 |
| 74 | 474..497 | 24 | 0 | 24 |
| 75 | 493..620 | 128 | 0 | 128 |
| 76 | 499..522 | 24 | 0 | 24 |
| 77 | 502..628 | 127 | 0 | 127 |
| ... | 36 more | | | |

### Gaps and durations of candidate tracks
- tracks: 93; lifespan min/median/max: 10/25/978; tracks with internal gaps: 16; total internal gaps: 231; longest internal gap: 200; tracks ending in coasting: 89 (trailing rows total 3288)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..21 | 21 | 21 | 5 | 16 | 2 | 2 | 13 | 78911 |
| 1 | 22..38 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 2 | 24..44 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 3 | 31..45 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 4 | 31..1008 | 978 | 978 | 973 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 79..319 | 241 | 241 | 107 | 134 | 24 | 53 | 6 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 6 | 87..103 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 7 | 92..113 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 10 | 138..201 | 64 | 64 | 48 | 16 | 12 | 2 | 0 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 11 | 149..168 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 12 | 150..169 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 13 | 160..288 | 129 | 129 | 86 | 43 | 20 | 3 | 15 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 175..257 | 83 | 83 | 62 | 21 | 15 | 3 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 15 | 175..189 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 17 | 187..283 | 97 | 97 | 67 | 30 | 14 | 4 | 10 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 199..223 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 20 | 203..528 | 326 | 326 | 80 | 246 | 11 | 200 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 213..230 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 24 | 216..236 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 25 | 224..247 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 27 | 233..426 | 194 | 194 | 0 | 194 | 0 | 0 | 194 | - |
| 28 | 239..578 | 340 | 340 | 17 | 323 | 6 | 180 | 39 | 79135, 79136, 79139 |
| 29 | 242..480 | 239 | 239 | 122 | 117 | 32 | 23 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 30 | 249..272 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 32 | 265..606 | 342 | 342 | 68 | 274 | 11 | 163 | 73 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 33 | 268..322 | 55 | 55 | 0 | 55 | 0 | 0 | 55 | - |
| 35 | 274..304 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 37 | 275..469 | 195 | 195 | 0 | 195 | 0 | 0 | 195 | - |
| 38 | 277..420 | 144 | 144 | 0 | 144 | 0 | 0 | 144 | - |
| 39 | 278..298 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 40 | 280..475 | 196 | 196 | 112 | 84 | 29 | 11 | 11 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79132, 79134 |
| 41 | 297..366 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 42 | 299..325 | 27 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 43 | 300..316 | 17 | 17 | 1 | 16 | 0 | 0 | 16 | 79097 |
| 46 | 324..349 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 47 | 328..352 | 25 | 25 | 8 | 17 | 2 | 1 | 15 | 79134, 79135, 79136, 79139 |
| 48 | 329..506 | 178 | 178 | 0 | 178 | 0 | 0 | 178 | - |
| 49 | 339..513 | 175 | 175 | 84 | 91 | 30 | 15 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 51 | 340..360 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 53 | 343..456 | 114 | 114 | 28 | 86 | 13 | 22 | 8 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 54 | 349..374 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 56 | 364..500 | 137 | 137 | 0 | 137 | 0 | 0 | 137 | - |
| 58 | 374..398 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 60 | 388..460 | 73 | 73 | 0 | 73 | 0 | 0 | 73 | - |
| 62 | 399..415 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 63 | 402..422 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 65 | 409..621 | 213 | 213 | 0 | 213 | 0 | 0 | 213 | - |
| 66 | 424..447 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 67 | 431..500 | 70 | 70 | 13 | 57 | 6 | 18 | 8 | 79135, 79136 |
| 69 | 449..484 | 36 | 36 | 0 | 36 | 0 | 0 | 36 | - |
| 70 | 450..470 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 72 | 466..490 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 73 | 472..509 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 74 | 474..497 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 75 | 493..620 | 128 | 128 | 0 | 128 | 0 | 0 | 128 | - |
| 76 | 499..522 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 77 | 502..628 | 127 | 127 | 0 | 127 | 0 | 0 | 127 | - |
| 79 | 524..549 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 80 | 526..546 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 83 | 529..551 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 84 | 529..560 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 88 | 549..575 | 27 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 90 | 574..624 | 51 | 51 | 0 | 51 | 0 | 0 | 51 | - |
| 93 | 588..608 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 94 | 592..610 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 98 | 624..648 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 99 | 649..663 | 15 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 100 | 650..670 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 102 | 656..679 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 104 | 674..699 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 105 | 700..722 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 106 | 712..732 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 108 | 720..742 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 110 | 724..747 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 111 | 749..772 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 112 | 774..796 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 114 | 785..808 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 116 | 799..825 | 27 | 27 | 0 | 27 | 0 | 0 | 27 | - |
| 118 | 824..848 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 119 | 836..856 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| ... | 13 more in JSON | | | | | | | | |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 43; matched pairs: 1881; unmatched reference entries: 8261; unmatched candidate entries: 3437
- identity switches: 184; fragmentation (coverage interruptions): 461; orphan candidate ids (never on a reference object): 26

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f31: ref 78911: 0 -> 4 at (1819, 3367), 23 frames after previous cover
- f161: ref 79136: 10 -> 13 at (2010, 3014.5), 20 frames after previous cover
- f166: ref 79139: 10 -> 13 at (1953.5, 3016), 4 frames after previous cover
- f173: ref 79135: 10 -> 13 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 10 -> 13 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 10 -> 13 at (1843, 3021), 3 frames after previous cover
- f175: ref 79139: 13 -> 14 at (1895.5, 3016.5), 8 frames after previous cover
- f176: ref 79132: 10 -> 13 at (1812, 3020), 3 frames after previous cover
- f178: ref 79136: 13 -> 14 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 13 -> 14 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 5 -> 10 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 13 -> 14 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 10 -> 13 at (1504.5, 3019), 2 frames after previous cover
- f187: ref 79135: 14 -> 17 at (1797, 3013), 2 frames after previous cover
- f188: ref 78969: 5 -> 10 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 10 -> 13 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 13 -> 14 at (1777.5, 3018.5), 6 frames after previous cover
- f190: ref 79045: 10 -> 13 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 17 -> 14 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 13 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 10 -> 13 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 78971: 13 -> 10 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 14 -> 17 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 10 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 13 -> 10 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 14 -> 17 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 13 -> 10 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 10 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 5 -> 10 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 13 -> 14 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 10 -> 5 at (1419.5, 3003), 2 frames after previous cover
- f207: ref 79134: 14 -> 17 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 14 -> 17 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 14 -> 17 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 10 -> 14 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 14 -> 17 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 10 -> 14 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 10 -> 5 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 5 -> 14 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 14 -> 17 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 10 -> 17 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 14 -> 17 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 14 -> 17 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 14 -> 5 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 17 -> 14 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 17 -> 14 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 17 -> 14 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 17 -> 14 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 17 -> 14 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 10 -> 13 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 14 -> 17 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 14 -> 17 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 14 -> 17 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 5 -> 14 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 14 -> 17 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 5 -> 14 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 14 -> 5 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 5 -> 13 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 13 -> 14 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 14 -> 17 at (1404.5, 2987), 17 frames after previous cover
- ... 124 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 7 | 4 (973), 0 (5) |
| 78896 | 350 (76..429) | 13 | 9 | 5 (5), 13 (3), 49 (3), 29 (2) |
| 78969 | 352 (80..434) | 103 | 45 | 13 (54), 49 (17), 29 (16), 5 (14), 10 (2) |
| 78971 | 352 (84..439) | 27 | 15 | 49 (11), 13 (5), 14 (4), 10 (3), 29 (3), 5 (1) |
| 79045 | 355 (84..443) | 39 | 15 | 29 (27), 10 (4), 14 (3), 13 (2), 5 (1), 40 (1), 49 (1) |
| 79037 | 355 (86..445) | 29 | 19 | 29 (14), 14 (5), 10 (3), 40 (3), 49 (2), 13 (1), 5 (1) |
| 78897 | 345 (89..450) | 48 | 26 | 29 (19), 40 (10), 5 (9), 10 (4), 49 (4), 14 (2) |
| 78899 | 365 (91..455) | 64 | 38 | 29 (21), 5 (17), 40 (14), 14 (4), 13 (3), 49 (3), 53 (2) |
| 79097 | 366 (94..461) | 81 | 44 | 5 (33), 40 (25), 29 (8), 14 (5), 53 (5), 49 (3), 10 (1), 43 (1) |
| 79098 | 360 (97..467) | 39 | 21 | 40 (30), 49 (5), 14 (2), 5 (2) |
| 79102 | 371 (98..477) | 28 | 15 | 40 (16), 49 (4), 14 (3), 5 (3), 53 (1), 29 (1) |
| 79103 | 380 (99..481) | 29 | 13 | 5 (10), 40 (6), 29 (5), 49 (5), 14 (2), 10 (1) |
| 79105 | 379 (101..484) | 11 | 7 | 5 (4), 14 (2), 17 (2), 40 (1), 53 (1), 29 (1) |
| 79108 | 385 (104..492) | 22 | 13 | 5 (4), 49 (4), 29 (4), 17 (3), 10 (2), 14 (2), 40 (2), 53 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 49 (11), 17 (5), 14 (2), 5 (2), 29 (1) |
| 79111 | 386 (109..500) | 15 | 7 | 49 (8), 17 (4), 10 (1), 14 (1), 5 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 17 (6), 14 (2), 40 (2), 53 (1), 20 (1), 32 (1) |
| 79116 | 411 (114..530) | 40 | 9 | 32 (37), 20 (3) |
| 79122 | 404 (118..532) | 26 | 14 | 32 (12), 53 (10), 17 (2), 10 (1), 20 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 20 (57), 14 (3), 17 (2), 10 (1), 13 (1), 40 (1) |
| 79128 | 402 (124..527) | 26 | 17 | 14 (7), 20 (7), 17 (5), 10 (3), 53 (2), 13 (1), 49 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 10 (7), 14 (6), 13 (5), 17 (4), 32 (4), 53 (3), 20 (2), 40 (1), 47 (1), 49 (1) |
| 79135 | 409 (129..542) | 67 | 41 | 17 (14), 28 (14), 67 (11), 10 (9), 20 (6), 32 (4), 13 (3), 14 (2), 47 (2), 49 (1), 53 (1) |
| 79139 | 406 (132..537) | 41 | 20 | 17 (13), 32 (8), 10 (5), 47 (4), 14 (3), 20 (3), 13 (2), 28 (2), 53 (1) |
| 79136 | 393 (136..538) | 22 | 12 | 17 (7), 13 (6), 14 (2), 67 (2), 32 (2), 10 (1), 47 (1), 28 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 22..38 | 17 | 0 | 17 |
| 6 | 87..103 | 17 | 0 | 17 |
| 12 | 150..169 | 20 | 0 | 20 |
| 23 | 213..230 | 18 | 0 | 18 |
| 27 | 233..426 | 194 | 0 | 194 |
| 33 | 268..322 | 55 | 0 | 55 |
| 37 | 275..469 | 195 | 0 | 195 |
| 38 | 277..420 | 144 | 0 | 144 |
| 41 | 297..366 | 70 | 0 | 70 |
| 48 | 329..506 | 178 | 0 | 178 |
| 56 | 364..500 | 137 | 0 | 137 |
| 60 | 388..460 | 73 | 0 | 73 |
| 65 | 409..621 | 213 | 0 | 213 |
| 72 | 466..490 | 25 | 0 | 25 |
| 73 | 472..509 | 38 | 0 | 38 |
| 75 | 493..620 | 128 | 0 | 128 |
| 77 | 502..628 | 127 | 0 | 127 |
| 83 | 529..551 | 23 | 0 | 23 |
| 84 | 529..560 | 32 | 0 | 32 |
| 94 | 592..610 | 19 | 0 | 19 |
| 102 | 656..679 | 24 | 0 | 24 |
| 108 | 720..742 | 23 | 0 | 23 |
| 114 | 785..808 | 24 | 0 | 24 |
| 122 | 847..870 | 24 | 0 | 24 |
| 132 | 912..933 | 22 | 0 | 22 |
| 141 | 975..995 | 21 | 0 | 21 |

### Gaps and durations of candidate tracks
- tracks: 43; lifespan min/median/max: 17/70/978; tracks with internal gaps: 16; total internal gaps: 231; longest internal gap: 200; tracks ending in coasting: 39 (trailing rows total 2107)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1..21 | 21 | 21 | 5 | 16 | 2 | 2 | 13 | 78911 |
| 1 | 22..38 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 4 | 31..1008 | 978 | 978 | 973 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 79..319 | 241 | 241 | 107 | 134 | 24 | 53 | 6 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 6 | 87..103 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 10 | 138..201 | 64 | 64 | 48 | 16 | 12 | 2 | 0 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 12 | 150..169 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 13 | 160..288 | 129 | 129 | 86 | 43 | 20 | 3 | 15 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 175..257 | 83 | 83 | 62 | 21 | 15 | 3 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 17 | 187..283 | 97 | 97 | 67 | 30 | 14 | 4 | 10 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 203..528 | 326 | 326 | 80 | 246 | 11 | 200 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 23 | 213..230 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 27 | 233..426 | 194 | 194 | 0 | 194 | 0 | 0 | 194 | - |
| 28 | 239..578 | 340 | 340 | 17 | 323 | 6 | 180 | 39 | 79135, 79136, 79139 |
| 29 | 242..480 | 239 | 239 | 122 | 117 | 32 | 23 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 32 | 265..606 | 342 | 342 | 68 | 274 | 11 | 163 | 73 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 33 | 268..322 | 55 | 55 | 0 | 55 | 0 | 0 | 55 | - |
| 37 | 275..469 | 195 | 195 | 0 | 195 | 0 | 0 | 195 | - |
| 38 | 277..420 | 144 | 144 | 0 | 144 | 0 | 0 | 144 | - |
| 40 | 280..475 | 196 | 196 | 112 | 84 | 29 | 11 | 11 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79132, 79134 |
| 41 | 297..366 | 70 | 70 | 0 | 70 | 0 | 0 | 70 | - |
| 43 | 300..316 | 17 | 17 | 1 | 16 | 0 | 0 | 16 | 79097 |
| 47 | 328..352 | 25 | 25 | 8 | 17 | 2 | 1 | 15 | 79134, 79135, 79136, 79139 |
| 48 | 329..506 | 178 | 178 | 0 | 178 | 0 | 0 | 178 | - |
| 49 | 339..513 | 175 | 175 | 84 | 91 | 30 | 15 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 53 | 343..456 | 114 | 114 | 28 | 86 | 13 | 22 | 8 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 56 | 364..500 | 137 | 137 | 0 | 137 | 0 | 0 | 137 | - |
| 60 | 388..460 | 73 | 73 | 0 | 73 | 0 | 0 | 73 | - |
| 65 | 409..621 | 213 | 213 | 0 | 213 | 0 | 0 | 213 | - |
| 67 | 431..500 | 70 | 70 | 13 | 57 | 6 | 18 | 8 | 79135, 79136 |
| 72 | 466..490 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 73 | 472..509 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 75 | 493..620 | 128 | 128 | 0 | 128 | 0 | 0 | 128 | - |
| 77 | 502..628 | 127 | 127 | 0 | 127 | 0 | 0 | 127 | - |
| 83 | 529..551 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 84 | 529..560 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 94 | 592..610 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 102 | 656..679 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 108 | 720..742 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 114 | 785..808 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 122 | 847..870 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 132 | 912..933 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 141 | 975..995 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
