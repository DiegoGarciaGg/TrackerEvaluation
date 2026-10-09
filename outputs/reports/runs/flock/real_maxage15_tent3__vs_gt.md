# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 15, "tentative_threshold": 3}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=0da8d97d2ca0 git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage15_tent3/tracks.csv sha256=a14aec5d8f08ae72
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage15_tent3
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
| observations | none | 4 | 0.247 | 0.622 | -0.149 | 1.03 | 0.158 | 97 | 266.0 |
| observations | none | 6 | 0.259 | 0.608 | -0.122 | 1.42 | 0.168 | 129 | 352.0 |
| observations | none | 8 | 0.267 | 0.587 | -0.102 | 1.80 | 0.173 | 147 | 416.0 |
| observations | none | 12 | 0.276 | 0.566 | -0.057 | 2.91 | 0.186 | 166 | 477.0 |
| observations | ignore | 4 | 0.251 | 0.622 | -0.114 | 1.03 | 0.162 | 97 | 266.0 |
| observations | ignore | 6 | 0.263 | 0.608 | -0.087 | 1.42 | 0.173 | 129 | 352.0 |
| observations | ignore | 8 | 0.271 | 0.587 | -0.067 | 1.80 | 0.178 | 147 | 416.0 |
| observations | ignore | 12 | 0.280 | 0.566 | -0.021 | 2.91 | 0.191 | 166 | 477.0 |
| updates | none | 4 | 0.231 | 0.586 | -0.333 | 1.11 | 0.140 | 127 | 318.0 |
| updates | none | 6 | 0.243 | 0.561 | -0.294 | 1.60 | 0.151 | 159 | 398.0 |
| updates | none | 8 | 0.251 | 0.534 | -0.259 | 2.14 | 0.157 | 180 | 454.0 |
| updates | none | 12 | 0.261 | 0.506 | -0.196 | 3.43 | 0.172 | 199 | 504.0 |
| updates | ignore | 4 | 0.239 | 0.586 | -0.236 | 1.11 | 0.149 | 127 | 318.0 |
| updates | ignore | 6 | 0.252 | 0.561 | -0.197 | 1.60 | 0.161 | 159 | 398.0 |
| updates | ignore | 8 | 0.260 | 0.534 | -0.162 | 2.14 | 0.167 | 180 | 454.0 |
| updates | ignore | 12 | 0.270 | 0.506 | -0.099 | 3.43 | 0.183 | 199 | 504.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 85; matched pairs: 1635; unmatched reference entries: 8507; unmatched candidate entries: 2520
- identity switches: 147; fragmentation (coverage interruptions): 415; orphan candidate ids (never on a reference object): 69

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
- f201: ref 79132: 17 -> 18 at (1646.5, 3013), 25 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 15 frames after previous cover
- f212: ref 79128: 18 -> 20 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 18 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 18 -> 20 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 18 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 17 -> 6 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 6 -> 18 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 18 -> 20 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 20 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 18 -> 20 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 18 -> 20 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 18 -> 6 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 20 -> 18 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 20 -> 18 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 20 -> 18 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 20 -> 18 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 20 -> 18 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 18 -> 20 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 18 -> 20 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 18 -> 20 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 6 -> 18 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 18 -> 20 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 6 -> 18 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 18 -> 6 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 6 -> 17 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 78971: 17 -> 18 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 18 -> 20 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 20 -> 6 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 18 -> 6 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 18 -> 17 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 18 -> 6 at (1359, 2995.5), 18 frames after previous cover
- f243: ref 79097: 6 -> 33 at (1219, 2986), 4 frames after previous cover
- f245: ref 78899: 18 -> 33 at (1179, 2985.5), 5 frames after previous cover
- f255: ref 79037: 18 -> 33 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 6 -> 20 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 6 -> 33 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 6 -> 20 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 33 -> 6 at (1090, 2983.5), 4 frames after previous cover
- f272: ref 79045: 12 -> 33 at (945.5, 2991.5), 89 frames after previous cover
- f274: ref 78899: 33 -> 6 at (996, 2989.5), 5 frames after previous cover
- ... 87 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 9 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 10 | 8 | 6 (3), 17 (3), 54 (3), 33 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 17 (54), 6 (13), 33 (13), 54 (12) |
| 78971 | 352 (84..439) | 18 | 12 | 54 (10), 17 (4), 6 (1), 12 (1), 18 (1), 33 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 33 (14), 12 (1), 44 (1), 54 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 33 (7), 18 (2), 44 (2), 54 (2), 12 (1), 17 (1), 6 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 33 (9), 6 (7), 44 (5), 54 (4), 12 (2) |
| 78899 | 365 (91..455) | 51 | 41 | 6 (16), 33 (15), 44 (12), 54 (3), 17 (2), 18 (2), 58 (1) |
| 79097 | 366 (94..461) | 69 | 44 | 6 (32), 44 (20), 33 (7), 18 (5), 54 (3), 12 (1), 58 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 44 (19), 6 (2), 54 (2), 18 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 44 (16), 54 (4), 6 (2), 58 (1), 33 (1) |
| 79103 | 380 (99..481) | 21 | 13 | 6 (5), 44 (5), 54 (5), 33 (3), 18 (2), 12 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 18 (2), 20 (1), 44 (1), 58 (1), 33 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 20 (3), 33 (3), 18 (2), 44 (2), 54 (2), 12 (1), 6 (1), 58 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 54 (8), 20 (4), 18 (2), 33 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 54 (5), 20 (2), 12 (1), 18 (1), 6 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 20 (4), 18 (2), 58 (1), 24 (1), 40 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 40 (37), 24 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 58 (10), 40 (9), 24 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 24 (56), 18 (3), 20 (2), 12 (1), 17 (1), 44 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 20 (5), 24 (4), 18 (3), 12 (2), 17 (1), 54 (1), 58 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 12 (5), 17 (4), 20 (4), 40 (3), 18 (2), 24 (2), 44 (1), 53 (1), 54 (1), 58 (1) |
| 79135 | 409 (129..542) | 47 | 39 | 20 (14), 32 (10), 12 (6), 24 (5), 73 (4), 40 (3), 18 (2), 17 (1), 54 (1), 58 (1) |
| 79139 | 406 (132..537) | 25 | 18 | 20 (9), 40 (7), 12 (2), 18 (2), 32 (2), 17 (1), 24 (1), 58 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 73 (1), 32 (1), 40 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..24 | 2 | 0 | 2 |
| 7 | 88..89 | 2 | 0 | 2 |
| 14 | 151..155 | 5 | 0 | 3 |
| 23 | 200..209 | 10 | 0 | 8 |
| 27 | 214..216 | 3 | 0 | 2 |
| 28 | 217..222 | 6 | 0 | 5 |
| 29 | 225..233 | 9 | 0 | 9 |
| 31 | 234..412 | 179 | 0 | 162 |
| 34 | 250..258 | 9 | 0 | 9 |
| 37 | 269..406 | 138 | 0 | 113 |
| 38 | 269..308 | 40 | 0 | 22 |
| 41 | 275..290 | 16 | 0 | 15 |
| 42 | 276..455 | 180 | 0 | 134 |
| 43 | 279..284 | 6 | 0 | 5 |
| 45 | 298..352 | 55 | 0 | 30 |
| 46 | 300..311 | 12 | 0 | 10 |
| 47 | 301..302 | 2 | 0 | 2 |
| 50 | 325..335 | 11 | 0 | 11 |
| 52 | 330..492 | 163 | 0 | 123 |
| 57 | 341..346 | 6 | 0 | 5 |
| 59 | 350..360 | 11 | 0 | 10 |
| 61 | 365..486 | 122 | 0 | 85 |
| 63 | 375..384 | 10 | 0 | 10 |
| 66 | 392..446 | 55 | 0 | 40 |
| 68 | 400..401 | 2 | 0 | 2 |
| 69 | 403..408 | 6 | 0 | 5 |
| 71 | 410..607 | 198 | 0 | 161 |
| 72 | 425..433 | 9 | 0 | 9 |
| 76 | 451..456 | 6 | 0 | 5 |
| 78 | 465..470 | 6 | 0 | 5 |
| 83 | 475..483 | 9 | 0 | 9 |
| 86 | 494..606 | 113 | 0 | 106 |
| 89 | 500..508 | 9 | 0 | 9 |
| 93 | 519..614 | 96 | 0 | 80 |
| 95 | 525..535 | 11 | 0 | 9 |
| 96 | 527..532 | 6 | 0 | 5 |
| 99 | 530..537 | 8 | 0 | 5 |
| 100 | 530..546 | 17 | 0 | 12 |
| 104 | 550..561 | 12 | 0 | 10 |
| 110 | 589..594 | 6 | 0 | 5 |
| ... | 29 more | | | |

### Gaps and durations of candidate tracks
- tracks: 85; lifespan min/median/max: 2/10/977; tracks with internal gaps: 16; total internal gaps: 152; longest internal gap: 197; tracks ending in coasting: 77 (trailing rows total 1526)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..7 | 6 | 4 | 3 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 23..24 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 5 | 32..1008 | 977 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..305 | 226 | 186 | 84 | 102 | 13 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 7 | 88..89 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 12 | 139..187 | 49 | 33 | 25 | 8 | 7 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 14 | 151..155 | 5 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 17 | 167..274 | 108 | 96 | 72 | 24 | 16 | 3 | 1 | 78896, 78899, 78969, 78971, 79037, 79128, 79132, 79134, 79135, 79139 |
| 18 | 176..243 | 68 | 43 | 34 | 9 | 5 | 2 | 1 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 20 | 188..269 | 82 | 59 | 48 | 11 | 10 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 23 | 200..209 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 24 | 204..514 | 311 | 300 | 71 | 229 | 8 | 197 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 214..216 | 3 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 28 | 217..222 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 29 | 225..233 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 31 | 234..412 | 179 | 162 | 0 | 162 | 0 | 0 | 162 | - |
| 32 | 240..564 | 325 | 245 | 13 | 232 | 5 | 147 | 15 | 79135, 79136, 79139 |
| 33 | 243..466 | 224 | 141 | 76 | 65 | 17 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 34 | 250..258 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 37 | 269..406 | 138 | 113 | 0 | 113 | 0 | 0 | 113 | - |
| 38 | 269..308 | 40 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 40 | 275..592 | 318 | 249 | 61 | 188 | 8 | 139 | 29 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 41 | 275..290 | 16 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 42 | 276..455 | 180 | 134 | 0 | 134 | 0 | 0 | 134 | - |
| 43 | 279..284 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 44 | 281..461 | 181 | 119 | 85 | 34 | 16 | 5 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79132, 79134 |
| 45 | 298..352 | 55 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 46 | 300..311 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 47 | 301..302 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 50 | 325..335 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 52 | 330..492 | 163 | 123 | 0 | 123 | 0 | 0 | 123 | - |
| 53 | 336..338 | 3 | 3 | 1 | 2 | 1 | 1 | 1 | 79134 |
| 54 | 340..499 | 160 | 130 | 67 | 63 | 25 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 57 | 341..346 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 58 | 344..442 | 99 | 71 | 20 | 51 | 11 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 59 | 350..360 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 61 | 365..486 | 122 | 85 | 0 | 85 | 0 | 0 | 85 | - |
| 63 | 375..384 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 66 | 392..446 | 55 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 68 | 400..401 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 69 | 403..408 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 71 | 410..607 | 198 | 161 | 0 | 161 | 0 | 0 | 161 | - |
| 72 | 425..433 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 73 | 432..486 | 55 | 29 | 5 | 24 | 5 | 12 | 0 | 79135, 79136 |
| 76 | 451..456 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 78 | 465..470 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 83 | 475..483 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 86 | 494..606 | 113 | 106 | 0 | 106 | 0 | 0 | 106 | - |
| 89 | 500..508 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 93 | 519..614 | 96 | 80 | 0 | 80 | 0 | 0 | 80 | - |
| 95 | 525..535 | 11 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 96 | 527..532 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 99 | 530..537 | 8 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 100 | 530..546 | 17 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 104 | 550..561 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 110 | 589..594 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 111 | 593..596 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 114 | 600..610 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 116 | 625..634 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 118 | 651..656 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 120 | 657..665 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 122 | 675..685 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 123 | 701..708 | 8 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 124 | 713..718 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 126 | 721..728 | 8 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 128 | 725..733 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 129 | 750..758 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 130 | 775..782 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 132 | 786..794 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 134 | 800..811 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 136 | 825..834 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 137 | 837..842 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 140 | 848..856 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 142 | 850..860 | 11 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 144 | 875..885 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 145 | 899..906 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 146 | 901..911 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 150 | 913..919 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 152 | 925..935 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 153 | 931..940 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| ... | 5 more in JSON | | | | | | | | |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 41; matched pairs: 1635; unmatched reference entries: 8507; unmatched candidate entries: 2163
- identity switches: 147; fragmentation (coverage interruptions): 415; orphan candidate ids (never on a reference object): 25

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
- f201: ref 79132: 17 -> 18 at (1646.5, 3013), 25 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 15 frames after previous cover
- f212: ref 79128: 18 -> 20 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 18 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 18 -> 20 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 18 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 17 -> 6 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 6 -> 18 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 18 -> 20 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 20 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 18 -> 20 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 18 -> 20 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 18 -> 6 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 20 -> 18 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 20 -> 18 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 20 -> 18 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 20 -> 18 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 20 -> 18 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 18 -> 20 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 18 -> 20 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 18 -> 20 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 6 -> 18 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 18 -> 20 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 6 -> 18 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 18 -> 6 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78896: 6 -> 17 at (1090, 2990.5), 53 frames after previous cover
- f239: ref 78971: 17 -> 18 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 18 -> 20 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 20 -> 6 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 18 -> 6 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 18 -> 17 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 18 -> 6 at (1359, 2995.5), 18 frames after previous cover
- f243: ref 79097: 6 -> 33 at (1219, 2986), 4 frames after previous cover
- f245: ref 78899: 18 -> 33 at (1179, 2985.5), 5 frames after previous cover
- f255: ref 79037: 18 -> 33 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 6 -> 20 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 6 -> 33 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 6 -> 20 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 33 -> 6 at (1090, 2983.5), 4 frames after previous cover
- f272: ref 79045: 12 -> 33 at (945.5, 2991.5), 89 frames after previous cover
- f274: ref 78899: 33 -> 6 at (996, 2989.5), 5 frames after previous cover
- ... 87 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 973 | 9 | 5 (970), 0 (3) |
| 78896 | 350 (76..429) | 10 | 8 | 6 (3), 17 (3), 54 (3), 33 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 17 (54), 6 (13), 33 (13), 54 (12) |
| 78971 | 352 (84..439) | 18 | 12 | 54 (10), 17 (4), 6 (1), 12 (1), 18 (1), 33 (1) |
| 79045 | 355 (84..443) | 17 | 12 | 33 (14), 12 (1), 44 (1), 54 (1) |
| 79037 | 355 (86..445) | 16 | 15 | 33 (7), 18 (2), 44 (2), 54 (2), 12 (1), 17 (1), 6 (1) |
| 78897 | 345 (89..450) | 27 | 21 | 33 (9), 6 (7), 44 (5), 54 (4), 12 (2) |
| 78899 | 365 (91..455) | 51 | 41 | 6 (16), 33 (15), 44 (12), 54 (3), 17 (2), 18 (2), 58 (1) |
| 79097 | 366 (94..461) | 69 | 44 | 6 (32), 44 (20), 33 (7), 18 (5), 54 (3), 12 (1), 58 (1) |
| 79098 | 360 (97..467) | 24 | 19 | 44 (19), 6 (2), 54 (2), 18 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 44 (16), 54 (4), 6 (2), 58 (1), 33 (1) |
| 79103 | 380 (99..481) | 21 | 13 | 6 (5), 44 (5), 54 (5), 33 (3), 18 (2), 12 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 18 (2), 20 (1), 44 (1), 58 (1), 33 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 20 (3), 33 (3), 18 (2), 44 (2), 54 (2), 12 (1), 6 (1), 58 (1) |
| 79110 | 388 (106..497) | 15 | 8 | 54 (8), 20 (4), 18 (2), 33 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 54 (5), 20 (2), 12 (1), 18 (1), 6 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 20 (4), 18 (2), 58 (1), 24 (1), 40 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 40 (37), 24 (1) |
| 79122 | 404 (118..532) | 20 | 11 | 58 (10), 40 (9), 24 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 24 (56), 18 (3), 20 (2), 12 (1), 17 (1), 44 (1) |
| 79128 | 402 (124..527) | 17 | 14 | 20 (5), 24 (4), 18 (3), 12 (2), 17 (1), 54 (1), 58 (1) |
| 79134 | 407 (127..533) | 24 | 22 | 12 (5), 17 (4), 20 (4), 40 (3), 18 (2), 24 (2), 44 (1), 53 (1), 54 (1), 58 (1) |
| 79135 | 409 (129..542) | 47 | 39 | 20 (14), 32 (10), 12 (6), 24 (5), 73 (4), 40 (3), 18 (2), 17 (1), 54 (1), 58 (1) |
| 79139 | 406 (132..537) | 25 | 18 | 20 (9), 40 (7), 12 (2), 18 (2), 32 (2), 17 (1), 24 (1), 58 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 73 (1), 32 (1), 40 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..24 | 2 | 0 | 2 |
| 7 | 88..89 | 2 | 0 | 2 |
| 14 | 151..155 | 5 | 0 | 3 |
| 27 | 214..216 | 3 | 0 | 2 |
| 31 | 234..412 | 179 | 0 | 162 |
| 37 | 269..406 | 138 | 0 | 113 |
| 38 | 269..308 | 40 | 0 | 22 |
| 42 | 276..455 | 180 | 0 | 134 |
| 45 | 298..352 | 55 | 0 | 30 |
| 47 | 301..302 | 2 | 0 | 2 |
| 52 | 330..492 | 163 | 0 | 123 |
| 61 | 365..486 | 122 | 0 | 85 |
| 66 | 392..446 | 55 | 0 | 40 |
| 71 | 410..607 | 198 | 0 | 161 |
| 86 | 494..606 | 113 | 0 | 106 |
| 93 | 519..614 | 96 | 0 | 80 |
| 99 | 530..537 | 8 | 0 | 5 |
| 100 | 530..546 | 17 | 0 | 12 |
| 111 | 593..596 | 4 | 0 | 4 |
| 120 | 657..665 | 9 | 0 | 9 |
| 126 | 721..728 | 8 | 0 | 3 |
| 132 | 786..794 | 9 | 0 | 4 |
| 140 | 848..856 | 9 | 0 | 4 |
| 150 | 913..919 | 7 | 0 | 3 |
| 159 | 976..981 | 6 | 0 | 4 |

### Gaps and durations of candidate tracks
- tracks: 41; lifespan min/median/max: 2/55/977; tracks with internal gaps: 16; total internal gaps: 152; longest internal gap: 197; tracks ending in coasting: 33 (trailing rows total 1169)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..7 | 6 | 4 | 3 | 1 | 1 | 1 | 0 | 78911 |
| 1 | 23..24 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 5 | 32..1008 | 977 | 975 | 970 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..305 | 226 | 186 | 84 | 102 | 13 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79108, 79111 |
| 7 | 88..89 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 12 | 139..187 | 49 | 33 | 25 | 8 | 7 | 1 | 1 | 78897, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79128, 79132, 79134, 79135, 79139 |
| 14 | 151..155 | 5 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 17 | 167..274 | 108 | 96 | 72 | 24 | 16 | 3 | 1 | 78896, 78899, 78969, 78971, 79037, 79128, 79132, 79134, 79135, 79139 |
| 18 | 176..243 | 68 | 43 | 34 | 9 | 5 | 2 | 1 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 20 | 188..269 | 82 | 59 | 48 | 11 | 10 | 2 | 0 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 24 | 204..514 | 311 | 300 | 71 | 229 | 8 | 197 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 214..216 | 3 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 31 | 234..412 | 179 | 162 | 0 | 162 | 0 | 0 | 162 | - |
| 32 | 240..564 | 325 | 245 | 13 | 232 | 5 | 147 | 15 | 79135, 79136, 79139 |
| 33 | 243..466 | 224 | 141 | 76 | 65 | 17 | 14 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 37 | 269..406 | 138 | 113 | 0 | 113 | 0 | 0 | 113 | - |
| 38 | 269..308 | 40 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 40 | 275..592 | 318 | 249 | 61 | 188 | 8 | 139 | 29 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 42 | 276..455 | 180 | 134 | 0 | 134 | 0 | 0 | 134 | - |
| 44 | 281..461 | 181 | 119 | 85 | 34 | 16 | 5 | 3 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79132, 79134 |
| 45 | 298..352 | 55 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 47 | 301..302 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 52 | 330..492 | 163 | 123 | 0 | 123 | 0 | 0 | 123 | - |
| 53 | 336..338 | 3 | 3 | 1 | 2 | 1 | 1 | 1 | 79134 |
| 54 | 340..499 | 160 | 130 | 67 | 63 | 25 | 15 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 58 | 344..442 | 99 | 71 | 20 | 51 | 11 | 19 | 0 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 61 | 365..486 | 122 | 85 | 0 | 85 | 0 | 0 | 85 | - |
| 66 | 392..446 | 55 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 71 | 410..607 | 198 | 161 | 0 | 161 | 0 | 0 | 161 | - |
| 73 | 432..486 | 55 | 29 | 5 | 24 | 5 | 12 | 0 | 79135, 79136 |
| 86 | 494..606 | 113 | 106 | 0 | 106 | 0 | 0 | 106 | - |
| 93 | 519..614 | 96 | 80 | 0 | 80 | 0 | 0 | 80 | - |
| 99 | 530..537 | 8 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 100 | 530..546 | 17 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 111 | 593..596 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 120 | 657..665 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 126 | 721..728 | 8 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 132 | 786..794 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 140 | 848..856 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 150 | 913..919 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 159 | 976..981 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 85; matched pairs: 1861; unmatched reference entries: 8281; unmatched candidate entries: 4310
- identity switches: 180; fragmentation (coverage interruptions): 451; orphan candidate ids (never on a reference object): 69

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
- f192: ref 78971: 17 -> 12 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 18 -> 20 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 12 -> 6 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 17 -> 12 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 18 -> 20 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 17 -> 12 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 12 -> 6 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 6 -> 12 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 17 -> 18 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 12 -> 6 at (1419.5, 3003), 2 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 18 -> 20 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 18 -> 20 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 18 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 18 -> 20 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 18 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 12 -> 6 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 6 -> 18 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 18 -> 20 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 20 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 18 -> 20 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 18 -> 20 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 18 -> 6 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 20 -> 18 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 20 -> 18 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 20 -> 18 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 20 -> 18 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 20 -> 18 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 12 -> 17 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 18 -> 20 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 18 -> 20 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 18 -> 20 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 6 -> 18 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 18 -> 20 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 6 -> 18 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 18 -> 6 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 6 -> 17 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 17 -> 18 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 18 -> 20 at (1404.5, 2987), 17 frames after previous cover
- ... 120 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 7 | 5 (972), 0 (4) |
| 78896 | 350 (76..429) | 12 | 8 | 6 (4), 17 (3), 54 (3), 33 (2) |
| 78969 | 352 (80..434) | 103 | 45 | 17 (54), 54 (17), 33 (16), 6 (14), 12 (2) |
| 78971 | 352 (84..439) | 27 | 15 | 54 (11), 17 (5), 18 (4), 12 (3), 33 (3), 6 (1) |
| 79045 | 355 (84..443) | 39 | 15 | 33 (27), 12 (4), 18 (3), 17 (2), 6 (1), 44 (1), 54 (1) |
| 79037 | 355 (86..445) | 29 | 19 | 33 (14), 18 (5), 12 (3), 44 (3), 54 (2), 17 (1), 6 (1) |
| 78897 | 345 (89..450) | 48 | 26 | 33 (19), 44 (10), 6 (9), 12 (4), 54 (4), 18 (2) |
| 78899 | 365 (91..455) | 64 | 38 | 33 (21), 6 (17), 44 (14), 18 (4), 17 (3), 54 (3), 58 (2) |
| 79097 | 366 (94..461) | 79 | 43 | 6 (33), 44 (25), 33 (7), 18 (5), 58 (5), 54 (3), 12 (1) |
| 79098 | 360 (97..467) | 39 | 21 | 44 (30), 54 (5), 18 (2), 6 (2) |
| 79102 | 371 (98..477) | 28 | 15 | 44 (16), 54 (4), 18 (3), 6 (3), 58 (1), 33 (1) |
| 79103 | 380 (99..481) | 29 | 13 | 6 (10), 44 (6), 33 (5), 54 (5), 18 (2), 12 (1) |
| 79105 | 379 (101..484) | 11 | 7 | 6 (4), 18 (2), 20 (2), 44 (1), 58 (1), 33 (1) |
| 79108 | 385 (104..492) | 22 | 13 | 6 (4), 54 (4), 33 (4), 20 (3), 12 (2), 18 (2), 44 (2), 58 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 54 (11), 20 (5), 18 (2), 6 (2), 33 (1) |
| 79111 | 386 (109..500) | 15 | 7 | 54 (8), 20 (4), 12 (1), 18 (1), 6 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 20 (6), 18 (2), 44 (2), 58 (1), 24 (1), 40 (1) |
| 79116 | 411 (114..530) | 40 | 9 | 40 (37), 24 (3) |
| 79122 | 404 (118..532) | 26 | 14 | 40 (12), 58 (10), 20 (2), 12 (1), 24 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 24 (57), 18 (3), 20 (2), 12 (1), 17 (1), 44 (1) |
| 79128 | 402 (124..527) | 26 | 17 | 18 (7), 24 (7), 20 (5), 12 (3), 58 (2), 17 (1), 54 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 12 (7), 18 (6), 17 (5), 20 (4), 40 (4), 58 (3), 24 (2), 44 (1), 53 (1), 54 (1) |
| 79135 | 409 (129..542) | 64 | 38 | 32 (14), 20 (13), 73 (11), 12 (9), 24 (6), 40 (4), 17 (3), 18 (2), 54 (1), 58 (1) |
| 79139 | 406 (132..537) | 34 | 18 | 20 (13), 40 (8), 12 (4), 24 (3), 18 (2), 32 (2), 17 (1), 58 (1) |
| 79136 | 393 (136..538) | 17 | 9 | 20 (7), 17 (2), 18 (2), 73 (2), 40 (2), 12 (1), 32 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..38 | 16 | 0 | 16 |
| 7 | 88..103 | 16 | 0 | 16 |
| 14 | 151..169 | 19 | 0 | 19 |
| 23 | 200..223 | 24 | 0 | 24 |
| 27 | 214..230 | 17 | 0 | 17 |
| 28 | 217..236 | 20 | 0 | 20 |
| 29 | 225..247 | 23 | 0 | 23 |
| 31 | 234..426 | 193 | 0 | 193 |
| 34 | 250..272 | 23 | 0 | 23 |
| 37 | 269..420 | 152 | 0 | 152 |
| 38 | 269..322 | 54 | 0 | 54 |
| 41 | 275..304 | 30 | 0 | 30 |
| 42 | 276..469 | 194 | 0 | 194 |
| 43 | 279..298 | 20 | 0 | 20 |
| 45 | 298..366 | 69 | 0 | 69 |
| 46 | 300..325 | 26 | 0 | 26 |
| 47 | 301..316 | 16 | 0 | 16 |
| 50 | 325..349 | 25 | 0 | 25 |
| 52 | 330..506 | 177 | 0 | 177 |
| 57 | 341..360 | 20 | 0 | 20 |
| 59 | 350..374 | 25 | 0 | 25 |
| 61 | 365..500 | 136 | 0 | 136 |
| 63 | 375..398 | 24 | 0 | 24 |
| 66 | 392..460 | 69 | 0 | 69 |
| 68 | 400..415 | 16 | 0 | 16 |
| 69 | 403..422 | 20 | 0 | 20 |
| 71 | 410..621 | 212 | 0 | 212 |
| 72 | 425..447 | 23 | 0 | 23 |
| 76 | 451..470 | 20 | 0 | 20 |
| 78 | 465..484 | 20 | 0 | 20 |
| 83 | 475..497 | 23 | 0 | 23 |
| 86 | 494..620 | 127 | 0 | 127 |
| 89 | 500..522 | 23 | 0 | 23 |
| 93 | 519..628 | 110 | 0 | 110 |
| 95 | 525..549 | 25 | 0 | 25 |
| 96 | 527..546 | 20 | 0 | 20 |
| 99 | 530..551 | 22 | 0 | 22 |
| 100 | 530..560 | 31 | 0 | 31 |
| 104 | 550..575 | 26 | 0 | 26 |
| 110 | 589..608 | 20 | 0 | 20 |
| ... | 29 more | | | |

### Gaps and durations of candidate tracks
- tracks: 85; lifespan min/median/max: 9/24/977; tracks with internal gaps: 16; total internal gaps: 228; longest internal gap: 199; tracks ending in coasting: 81 (trailing rows total 2999)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..21 | 20 | 20 | 4 | 16 | 2 | 2 | 13 | 78911 |
| 1 | 23..38 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 5 | 32..1008 | 977 | 977 | 972 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..319 | 240 | 240 | 106 | 134 | 24 | 53 | 6 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 7 | 88..103 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 12 | 139..201 | 63 | 63 | 47 | 16 | 12 | 2 | 0 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 151..169 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 17 | 167..288 | 122 | 122 | 81 | 41 | 18 | 3 | 15 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 176..257 | 82 | 82 | 61 | 21 | 15 | 3 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 188..283 | 96 | 96 | 66 | 30 | 14 | 4 | 10 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 200..223 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 24 | 204..528 | 325 | 325 | 80 | 245 | 11 | 199 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 214..230 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 28 | 217..236 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 29 | 225..247 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 31 | 234..426 | 193 | 193 | 0 | 193 | 0 | 0 | 193 | - |
| 32 | 240..578 | 339 | 339 | 17 | 322 | 6 | 179 | 39 | 79135, 79136, 79139 |
| 33 | 243..480 | 238 | 238 | 121 | 117 | 32 | 23 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 34 | 250..272 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 37 | 269..420 | 152 | 152 | 0 | 152 | 0 | 0 | 152 | - |
| 38 | 269..322 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |
| 40 | 275..606 | 332 | 332 | 68 | 264 | 11 | 153 | 73 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 41 | 275..304 | 30 | 30 | 0 | 30 | 0 | 0 | 30 | - |
| 42 | 276..469 | 194 | 194 | 0 | 194 | 0 | 0 | 194 | - |
| 43 | 279..298 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 44 | 281..475 | 195 | 195 | 112 | 83 | 29 | 11 | 11 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79132, 79134 |
| 45 | 298..366 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 46 | 300..325 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 47 | 301..316 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 50 | 325..349 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 52 | 330..506 | 177 | 177 | 0 | 177 | 0 | 0 | 177 | - |
| 53 | 336..352 | 17 | 17 | 1 | 16 | 1 | 1 | 15 | 79134 |
| 54 | 340..513 | 174 | 174 | 84 | 90 | 30 | 15 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 57 | 341..360 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 58 | 344..456 | 113 | 113 | 28 | 85 | 13 | 22 | 8 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 59 | 350..374 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 61 | 365..500 | 136 | 136 | 0 | 136 | 0 | 0 | 136 | - |
| 63 | 375..398 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 66 | 392..460 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 68 | 400..415 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 69 | 403..422 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 71 | 410..621 | 212 | 212 | 0 | 212 | 0 | 0 | 212 | - |
| 72 | 425..447 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 73 | 432..500 | 69 | 69 | 13 | 56 | 6 | 17 | 8 | 79135, 79136 |
| 76 | 451..470 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 78 | 465..484 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 83 | 475..497 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 86 | 494..620 | 127 | 127 | 0 | 127 | 0 | 0 | 127 | - |
| 89 | 500..522 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 93 | 519..628 | 110 | 110 | 0 | 110 | 0 | 0 | 110 | - |
| 95 | 525..549 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 96 | 527..546 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 99 | 530..551 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 100 | 530..560 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 104 | 550..575 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 110 | 589..608 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 111 | 593..610 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 114 | 600..624 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 116 | 625..648 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 118 | 651..670 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 120 | 657..679 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 122 | 675..699 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 123 | 701..722 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 124 | 713..732 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 126 | 721..742 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 128 | 725..747 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 129 | 750..772 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 130 | 775..796 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 132 | 786..808 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 134 | 800..825 | 26 | 26 | 0 | 26 | 0 | 0 | 26 | - |
| 136 | 825..848 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| 137 | 837..856 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
| 140 | 848..870 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 142 | 850..874 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 144 | 875..899 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 145 | 899..920 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 146 | 901..925 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 150 | 913..933 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 152 | 925..949 | 25 | 25 | 0 | 25 | 0 | 0 | 25 | - |
| 153 | 931..954 | 24 | 24 | 0 | 24 | 0 | 0 | 24 | - |
| ... | 5 more in JSON | | | | | | | | |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 41; matched pairs: 1861; unmatched reference entries: 8281; unmatched candidate entries: 3321
- identity switches: 180; fragmentation (coverage interruptions): 451; orphan candidate ids (never on a reference object): 25

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
- f192: ref 78971: 17 -> 12 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 18 -> 20 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 12 -> 6 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 17 -> 12 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 18 -> 20 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 17 -> 12 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 12 -> 6 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 6 -> 12 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 17 -> 18 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 12 -> 6 at (1419.5, 3003), 2 frames after previous cover
- f207: ref 79134: 18 -> 20 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 18 -> 20 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 18 -> 20 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 12 -> 18 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 18 -> 20 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 12 -> 18 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 12 -> 6 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 6 -> 18 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 18 -> 20 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 12 -> 20 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 18 -> 20 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 18 -> 20 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 18 -> 6 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 20 -> 18 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 20 -> 18 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 20 -> 18 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 20 -> 18 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 20 -> 18 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 12 -> 17 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 18 -> 20 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 18 -> 20 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 18 -> 20 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 6 -> 18 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 18 -> 20 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 6 -> 18 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 18 -> 6 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 6 -> 17 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 17 -> 18 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 18 -> 20 at (1404.5, 2987), 17 frames after previous cover
- ... 120 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 976 | 7 | 5 (972), 0 (4) |
| 78896 | 350 (76..429) | 12 | 8 | 6 (4), 17 (3), 54 (3), 33 (2) |
| 78969 | 352 (80..434) | 103 | 45 | 17 (54), 54 (17), 33 (16), 6 (14), 12 (2) |
| 78971 | 352 (84..439) | 27 | 15 | 54 (11), 17 (5), 18 (4), 12 (3), 33 (3), 6 (1) |
| 79045 | 355 (84..443) | 39 | 15 | 33 (27), 12 (4), 18 (3), 17 (2), 6 (1), 44 (1), 54 (1) |
| 79037 | 355 (86..445) | 29 | 19 | 33 (14), 18 (5), 12 (3), 44 (3), 54 (2), 17 (1), 6 (1) |
| 78897 | 345 (89..450) | 48 | 26 | 33 (19), 44 (10), 6 (9), 12 (4), 54 (4), 18 (2) |
| 78899 | 365 (91..455) | 64 | 38 | 33 (21), 6 (17), 44 (14), 18 (4), 17 (3), 54 (3), 58 (2) |
| 79097 | 366 (94..461) | 79 | 43 | 6 (33), 44 (25), 33 (7), 18 (5), 58 (5), 54 (3), 12 (1) |
| 79098 | 360 (97..467) | 39 | 21 | 44 (30), 54 (5), 18 (2), 6 (2) |
| 79102 | 371 (98..477) | 28 | 15 | 44 (16), 54 (4), 18 (3), 6 (3), 58 (1), 33 (1) |
| 79103 | 380 (99..481) | 29 | 13 | 6 (10), 44 (6), 33 (5), 54 (5), 18 (2), 12 (1) |
| 79105 | 379 (101..484) | 11 | 7 | 6 (4), 18 (2), 20 (2), 44 (1), 58 (1), 33 (1) |
| 79108 | 385 (104..492) | 22 | 13 | 6 (4), 54 (4), 33 (4), 20 (3), 12 (2), 18 (2), 44 (2), 58 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 54 (11), 20 (5), 18 (2), 6 (2), 33 (1) |
| 79111 | 386 (109..500) | 15 | 7 | 54 (8), 20 (4), 12 (1), 18 (1), 6 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 20 (6), 18 (2), 44 (2), 58 (1), 24 (1), 40 (1) |
| 79116 | 411 (114..530) | 40 | 9 | 40 (37), 24 (3) |
| 79122 | 404 (118..532) | 26 | 14 | 40 (12), 58 (10), 20 (2), 12 (1), 24 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 24 (57), 18 (3), 20 (2), 12 (1), 17 (1), 44 (1) |
| 79128 | 402 (124..527) | 26 | 17 | 18 (7), 24 (7), 20 (5), 12 (3), 58 (2), 17 (1), 54 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 12 (7), 18 (6), 17 (5), 20 (4), 40 (4), 58 (3), 24 (2), 44 (1), 53 (1), 54 (1) |
| 79135 | 409 (129..542) | 64 | 38 | 32 (14), 20 (13), 73 (11), 12 (9), 24 (6), 40 (4), 17 (3), 18 (2), 54 (1), 58 (1) |
| 79139 | 406 (132..537) | 34 | 18 | 20 (13), 40 (8), 12 (4), 24 (3), 18 (2), 32 (2), 17 (1), 58 (1) |
| 79136 | 393 (136..538) | 17 | 9 | 20 (7), 17 (2), 18 (2), 73 (2), 40 (2), 12 (1), 32 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..38 | 16 | 0 | 16 |
| 7 | 88..103 | 16 | 0 | 16 |
| 14 | 151..169 | 19 | 0 | 19 |
| 27 | 214..230 | 17 | 0 | 17 |
| 31 | 234..426 | 193 | 0 | 193 |
| 37 | 269..420 | 152 | 0 | 152 |
| 38 | 269..322 | 54 | 0 | 54 |
| 42 | 276..469 | 194 | 0 | 194 |
| 45 | 298..366 | 69 | 0 | 69 |
| 47 | 301..316 | 16 | 0 | 16 |
| 52 | 330..506 | 177 | 0 | 177 |
| 61 | 365..500 | 136 | 0 | 136 |
| 66 | 392..460 | 69 | 0 | 69 |
| 71 | 410..621 | 212 | 0 | 212 |
| 86 | 494..620 | 127 | 0 | 127 |
| 93 | 519..628 | 110 | 0 | 110 |
| 99 | 530..551 | 22 | 0 | 22 |
| 100 | 530..560 | 31 | 0 | 31 |
| 111 | 593..610 | 18 | 0 | 18 |
| 120 | 657..679 | 23 | 0 | 23 |
| 126 | 721..742 | 22 | 0 | 22 |
| 132 | 786..808 | 23 | 0 | 23 |
| 140 | 848..870 | 23 | 0 | 23 |
| 150 | 913..933 | 21 | 0 | 21 |
| 159 | 976..995 | 20 | 0 | 20 |

### Gaps and durations of candidate tracks
- tracks: 41; lifespan min/median/max: 16/69/977; tracks with internal gaps: 16; total internal gaps: 228; longest internal gap: 199; tracks ending in coasting: 37 (trailing rows total 2010)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..21 | 20 | 20 | 4 | 16 | 2 | 2 | 13 | 78911 |
| 1 | 23..38 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 5 | 32..1008 | 977 | 977 | 972 | 5 | 4 | 2 | 0 | 78911 |
| 6 | 80..319 | 240 | 240 | 106 | 134 | 24 | 53 | 6 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 7 | 88..103 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 12 | 139..201 | 63 | 63 | 47 | 16 | 12 | 2 | 0 | 78897, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 14 | 151..169 | 19 | 19 | 0 | 19 | 0 | 0 | 19 | - |
| 17 | 167..288 | 122 | 122 | 81 | 41 | 18 | 3 | 15 | 78896, 78899, 78969, 78971, 79037, 79045, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 176..257 | 82 | 82 | 61 | 21 | 15 | 3 | 0 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 20 | 188..283 | 96 | 96 | 66 | 30 | 14 | 4 | 10 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 24 | 204..528 | 325 | 325 | 80 | 245 | 11 | 199 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 27 | 214..230 | 17 | 17 | 0 | 17 | 0 | 0 | 17 | - |
| 31 | 234..426 | 193 | 193 | 0 | 193 | 0 | 0 | 193 | - |
| 32 | 240..578 | 339 | 339 | 17 | 322 | 6 | 179 | 39 | 79135, 79136, 79139 |
| 33 | 243..480 | 238 | 238 | 121 | 117 | 32 | 23 | 19 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79102, 79103, 79105, 79108, 79110 |
| 37 | 269..420 | 152 | 152 | 0 | 152 | 0 | 0 | 152 | - |
| 38 | 269..322 | 54 | 54 | 0 | 54 | 0 | 0 | 54 | - |
| 40 | 275..606 | 332 | 332 | 68 | 264 | 11 | 153 | 73 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 42 | 276..469 | 194 | 194 | 0 | 194 | 0 | 0 | 194 | - |
| 44 | 281..475 | 195 | 195 | 112 | 83 | 29 | 11 | 11 | 78897, 78899, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79115, 79132, 79134 |
| 45 | 298..366 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 47 | 301..316 | 16 | 16 | 0 | 16 | 0 | 0 | 16 | - |
| 52 | 330..506 | 177 | 177 | 0 | 177 | 0 | 0 | 177 | - |
| 53 | 336..352 | 17 | 17 | 1 | 16 | 1 | 1 | 15 | 79134 |
| 54 | 340..513 | 174 | 174 | 84 | 90 | 30 | 15 | 13 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111, 79128, 79134, 79135 |
| 58 | 344..456 | 113 | 113 | 28 | 85 | 13 | 22 | 8 | 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 61 | 365..500 | 136 | 136 | 0 | 136 | 0 | 0 | 136 | - |
| 66 | 392..460 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 71 | 410..621 | 212 | 212 | 0 | 212 | 0 | 0 | 212 | - |
| 73 | 432..500 | 69 | 69 | 13 | 56 | 6 | 17 | 8 | 79135, 79136 |
| 86 | 494..620 | 127 | 127 | 0 | 127 | 0 | 0 | 127 | - |
| 93 | 519..628 | 110 | 110 | 0 | 110 | 0 | 0 | 110 | - |
| 99 | 530..551 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 100 | 530..560 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 111 | 593..610 | 18 | 18 | 0 | 18 | 0 | 0 | 18 | - |
| 120 | 657..679 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 126 | 721..742 | 22 | 22 | 0 | 22 | 0 | 0 | 22 | - |
| 132 | 786..808 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 140 | 848..870 | 23 | 23 | 0 | 23 | 0 | 0 | 23 | - |
| 150 | 913..933 | 21 | 21 | 0 | 21 | 0 | 0 | 21 | - |
| 159 | 976..995 | 20 | 20 | 0 | 20 | 0 | 0 | 20 | - |
