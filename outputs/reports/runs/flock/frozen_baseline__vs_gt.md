# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=unknown config={}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=44136fa355b3 git=none model=unknown
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/results/flock/baseline_tracks.csv sha256=903c5ff6f9e4b42b
  - tracker/ hash=7b65976a888fbd3c coasting_known=False
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: 6-column format: coasting rows unknown, every row counted as an observation
  - note: frozen_baseline
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- reference: config_hash=44136fa355b3 git=none model=gt
  - gt_tracks_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv sha256=a89c6bc9f4e8148d
  - gt_detections_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/ground_truth/20251012_164031_1DAC_detections_corrected.csv sha256=503255dd69b114a5
  - note: confidence 1.0 on every box: labels carry no score
  - note: track_id is the annotator's obj_id as text
  - note: companion detections CSV holds the same boxes without ids (0 row mismatches)
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}
- candidate is in the 6-column baseline format: coasting rows are indistinguishable, so only the 'updates' view (every row as written) is scored; matched-rows-only needs the 10-column format
- ignore region 'burnt-in timestamp overlay, top-left': entries with center inside it are dropped on both sides before scoring

## Metrics (center-distance matching)
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| updates | none | 4 | 0.219 | 0.574 | -0.472 | 1.13 | 0.130 | 154 | 325.0 |
| updates | none | 6 | 0.231 | 0.545 | -0.430 | 1.66 | 0.140 | 194 | 414.0 |
| updates | none | 8 | 0.239 | 0.519 | -0.393 | 2.23 | 0.146 | 227 | 472.0 |
| updates | none | 12 | 0.249 | 0.493 | -0.323 | 3.58 | 0.159 | 240 | 515.0 |
| updates | ignore | 4 | 0.231 | 0.574 | -0.312 | 1.13 | 0.143 | 154 | 325.0 |
| updates | ignore | 6 | 0.244 | 0.545 | -0.270 | 1.66 | 0.154 | 194 | 414.0 |
| updates | ignore | 8 | 0.252 | 0.519 | -0.233 | 2.23 | 0.160 | 227 | 472.0 |
| updates | ignore | 12 | 0.263 | 0.493 | -0.163 | 3.58 | 0.175 | 240 | 515.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 78; matched pairs: 1906; unmatched reference entries: 8236; unmatched candidate entries: 5665
- identity switches: 227; fragmentation (coverage interruptions): 469; orphan candidate ids (never on a reference object): 60

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f167: ref 79139: 11 -> 16 at (1946.5, 3016), 5 frames after previous cover
- f169: ref 79136: 11 -> 16 at (1961, 3015.5), 28 frames after previous cover
- f173: ref 79135: 11 -> 16 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 11 -> 16 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 11 -> 16 at (1843, 3021), 3 frames after previous cover
- f176: ref 79132: 11 -> 16 at (1812, 3020), 3 frames after previous cover
- f176: ref 79139: 16 -> 18 at (1889.5, 3014.5), 9 frames after previous cover
- f178: ref 79136: 16 -> 18 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 16 -> 18 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 5 -> 11 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 16 -> 18 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 11 -> 16 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 5 -> 11 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 11 -> 16 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 16 -> 18 at (1777.5, 3018.5), 6 frames after previous cover
- f189: ref 79135: 18 -> 19 at (1782.5, 3013.5), 4 frames after previous cover
- f190: ref 79045: 11 -> 16 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 19 -> 18 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 16 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 11 -> 16 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 78971: 16 -> 11 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 18 -> 19 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 11 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 16 -> 11 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 18 -> 19 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 16 -> 11 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 11 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 5 -> 11 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 16 -> 18 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 11 -> 5 at (1419.5, 3003), 2 frames after previous cover
- f205: ref 78899: 5 -> 11 at (1433, 3006), 1 frames after previous cover
- f207: ref 79134: 18 -> 19 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 18 -> 19 at (1698.5, 3013.5), 27 frames after previous cover
- f210: ref 78899: 11 -> 5 at (1400, 3003.5), 5 frames after previous cover
- f212: ref 79128: 18 -> 19 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 11 -> 18 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 18 -> 19 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 11 -> 18 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 11 -> 5 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 5 -> 18 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 18 -> 19 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 11 -> 19 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 18 -> 19 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 18 -> 19 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 18 -> 5 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 19 -> 18 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 19 -> 18 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 19 -> 18 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 19 -> 18 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 19 -> 18 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 11 -> 16 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 18 -> 19 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 18 -> 19 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 18 -> 19 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 5 -> 18 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 18 -> 19 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 5 -> 18 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 18 -> 5 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 5 -> 16 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 16 -> 18 at (1139, 2987), 10 frames after previous cover
- ... 167 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 7 | 0 (978) |
| 78896 | 350 (76..429) | 12 | 8 | 5 (4), 16 (4), 42 (2), 59 (2) |
| 78969 | 352 (80..434) | 105 | 46 | 16 (71), 5 (19), 59 (11), 11 (2), 42 (2) |
| 78971 | 352 (84..439) | 29 | 16 | 59 (8), 5 (7), 16 (5), 18 (4), 11 (3), 32 (1), 42 (1) |
| 79045 | 355 (84..443) | 36 | 16 | 5 (16), 59 (5), 11 (4), 18 (3), 32 (3), 42 (3), 16 (2) |
| 79037 | 355 (86..445) | 31 | 19 | 5 (11), 18 (5), 16 (4), 11 (3), 32 (3), 59 (3), 42 (2) |
| 78897 | 345 (89..450) | 46 | 25 | 5 (20), 59 (9), 16 (6), 11 (4), 42 (3), 18 (2), 32 (1), 56 (1) |
| 78899 | 365 (91..455) | 67 | 40 | 5 (26), 32 (14), 16 (6), 59 (6), 18 (5), 47 (3), 56 (3), 42 (2), 11 (1), 57 (1) |
| 79097 | 366 (94..461) | 80 | 44 | 5 (44), 18 (7), 32 (7), 47 (5), 59 (5), 16 (4), 42 (3), 57 (3), 11 (1), 56 (1) |
| 79098 | 360 (97..467) | 43 | 23 | 16 (20), 5 (6), 59 (5), 18 (4), 57 (4), 42 (2), 47 (2) |
| 79102 | 371 (98..477) | 34 | 16 | 16 (15), 5 (4), 59 (4), 18 (3), 47 (3), 57 (3), 56 (2) |
| 79103 | 380 (99..481) | 29 | 13 | 5 (14), 59 (5), 47 (4), 57 (3), 18 (2), 11 (1) |
| 79105 | 379 (101..484) | 16 | 8 | 5 (6), 57 (3), 18 (2), 19 (2), 47 (2), 56 (1) |
| 79108 | 385 (104..492) | 24 | 15 | 5 (9), 47 (4), 19 (3), 11 (2), 18 (2), 57 (2), 56 (1), 59 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 59 (7), 19 (5), 5 (3), 47 (3), 18 (2), 57 (1) |
| 79111 | 386 (109..500) | 14 | 7 | 59 (6), 19 (4), 11 (1), 18 (1), 5 (1), 47 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 19 (6), 18 (2), 47 (2), 56 (1), 23 (1), 30 (1) |
| 79116 | 411 (114..530) | 42 | 9 | 30 (37), 23 (3), 31 (2) |
| 79122 | 404 (118..532) | 29 | 14 | 30 (12), 56 (10), 31 (3), 19 (2), 11 (1), 23 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 23 (57), 18 (3), 19 (2), 11 (1), 16 (1), 47 (1) |
| 79128 | 402 (124..527) | 25 | 16 | 18 (7), 19 (5), 23 (4), 11 (3), 31 (3), 56 (2), 16 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 11 (7), 18 (6), 16 (5), 19 (4), 56 (3), 23 (2), 39 (2), 30 (2), 47 (1), 37 (1), 53 (1) |
| 79135 | 409 (129..542) | 68 | 39 | 39 (20), 19 (13), 31 (10), 11 (9), 23 (6), 16 (3), 18 (2), 37 (2), 30 (2), 56 (1) |
| 79139 | 406 (132..537) | 42 | 22 | 19 (13), 39 (9), 37 (5), 11 (4), 31 (4), 23 (3), 18 (2), 16 (1), 56 (1) |
| 79136 | 393 (136..538) | 23 | 12 | 19 (7), 39 (3), 23 (3), 16 (2), 18 (2), 31 (2), 30 (2), 11 (1), 37 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..53 | 31 | 0 | 31 |
| 6 | 88..118 | 31 | 0 | 31 |
| 13 | 151..184 | 34 | 0 | 34 |
| 22 | 200..238 | 39 | 0 | 39 |
| 26 | 217..251 | 35 | 0 | 35 |
| 28 | 225..262 | 38 | 0 | 38 |
| 33 | 250..287 | 38 | 0 | 38 |
| 36 | 269..484 | 216 | 0 | 216 |
| 38 | 275..319 | 45 | 0 | 45 |
| 40 | 276..643 | 368 | 0 | 368 |
| 41 | 279..313 | 35 | 0 | 35 |
| 45 | 298..630 | 333 | 0 | 333 |
| 46 | 300..340 | 41 | 0 | 41 |
| 50 | 325..364 | 40 | 0 | 40 |
| 54 | 341..375 | 35 | 0 | 35 |
| 58 | 350..389 | 40 | 0 | 40 |
| 61 | 375..413 | 39 | 0 | 39 |
| 64 | 392..515 | 124 | 0 | 124 |
| 66 | 400..462 | 63 | 0 | 63 |
| 67 | 403..437 | 35 | 0 | 35 |
| 69 | 410..632 | 223 | 0 | 223 |
| 72 | 451..485 | 35 | 0 | 35 |
| 74 | 465..499 | 35 | 0 | 35 |
| 79 | 475..512 | 38 | 0 | 38 |
| 84 | 500..537 | 38 | 0 | 38 |
| 86 | 525..564 | 40 | 0 | 40 |
| 87 | 527..561 | 35 | 0 | 35 |
| 89 | 530..566 | 37 | 0 | 37 |
| 91 | 530..575 | 46 | 0 | 46 |
| 95 | 550..590 | 41 | 0 | 41 |
| 101 | 589..623 | 35 | 0 | 35 |
| 102 | 593..625 | 33 | 0 | 33 |
| 105 | 600..639 | 40 | 0 | 40 |
| 107 | 625..663 | 39 | 0 | 39 |
| 109 | 651..685 | 35 | 0 | 35 |
| 111 | 657..694 | 38 | 0 | 38 |
| 113 | 675..714 | 40 | 0 | 40 |
| 114 | 701..737 | 37 | 0 | 37 |
| 115 | 713..747 | 35 | 0 | 35 |
| 117 | 721..757 | 37 | 0 | 37 |
| ... | 20 more | | | |

### Gaps and durations of candidate tracks
- tracks: 78; lifespan min/median/max: 9/39/1007; tracks with internal gaps: 17; total internal gaps: 253; longest internal gap: 215; tracks ending in coasting: 75 (trailing rows total 3952)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 978 | 29 | 7 | 21 | 0 | 78911 |
| 1 | 23..53 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 5 | 80..495 | 416 | 416 | 190 | 226 | 44 | 53 | 34 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 6 | 88..118 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 11 | 139..243 | 105 | 105 | 48 | 57 | 13 | 3 | 38 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 151..184 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 16 | 167..490 | 324 | 324 | 150 | 174 | 43 | 29 | 26 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 176..303 | 128 | 128 | 66 | 62 | 17 | 3 | 36 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 188..435 | 248 | 248 | 66 | 182 | 14 | 4 | 162 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 22 | 200..238 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 23 | 204..543 | 340 | 340 | 80 | 260 | 12 | 199 | 5 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 26 | 217..251 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 28 | 225..262 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 30 | 234..619 | 386 | 386 | 56 | 330 | 10 | 215 | 86 | 79115, 79116, 79122, 79134, 79135, 79136 |
| 31 | 240..542 | 303 | 303 | 24 | 279 | 7 | 179 | 0 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 32 | 243..309 | 67 | 67 | 29 | 38 | 5 | 2 | 32 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 33 | 250..287 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 36 | 269..484 | 216 | 216 | 0 | 216 | 0 | 0 | 216 | - |
| 37 | 269..367 | 99 | 99 | 9 | 90 | 3 | 58 | 30 | 79134, 79135, 79136, 79139 |
| 38 | 275..319 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 39 | 275..641 | 367 | 367 | 34 | 333 | 10 | 153 | 102 | 79134, 79135, 79136, 79139 |
| 40 | 276..643 | 368 | 368 | 0 | 368 | 0 | 0 | 368 | - |
| 41 | 279..313 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 42 | 282..321 | 40 | 40 | 20 | 20 | 6 | 5 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 45 | 298..630 | 333 | 333 | 0 | 333 | 0 | 0 | 333 | - |
| 46 | 300..340 | 41 | 41 | 0 | 41 | 0 | 0 | 41 | - |
| 47 | 301..371 | 71 | 71 | 31 | 40 | 15 | 11 | 2 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132, 79134 |
| 50 | 325..364 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 53 | 341..371 | 31 | 31 | 1 | 30 | 0 | 0 | 30 | 79134 |
| 54 | 341..375 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 56 | 346..472 | 127 | 127 | 27 | 100 | 15 | 22 | 19 | 78897, 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 57 | 347..380 | 34 | 34 | 20 | 14 | 8 | 3 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 58 | 350..389 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 59 | 371..528 | 158 | 158 | 77 | 81 | 24 | 5 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 61 | 375..413 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 64 | 392..515 | 124 | 124 | 0 | 124 | 0 | 0 | 124 | - |
| 66 | 400..462 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 67 | 403..437 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 69 | 410..632 | 223 | 223 | 0 | 223 | 0 | 0 | 223 | - |
| 72 | 451..485 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 74 | 465..499 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 79 | 475..512 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 84 | 500..537 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 86 | 525..564 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 87 | 527..561 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 89 | 530..566 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 91 | 530..575 | 46 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 95 | 550..590 | 41 | 41 | 0 | 41 | 0 | 0 | 41 | - |
| 101 | 589..623 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 102 | 593..625 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 105 | 600..639 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 107 | 625..663 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 109 | 651..685 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 111 | 657..694 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 113 | 675..714 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 114 | 701..737 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 115 | 713..747 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 117 | 721..757 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 119 | 725..762 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 120 | 750..787 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 121 | 775..811 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 123 | 786..823 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 125 | 800..840 | 41 | 41 | 0 | 41 | 0 | 0 | 41 | - |
| 127 | 825..863 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 128 | 837..871 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 131 | 848..885 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 133 | 850..889 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 135 | 875..914 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 136 | 899..935 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 137 | 901..940 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 141 | 913..948 | 36 | 36 | 0 | 36 | 0 | 0 | 36 | - |
| 143 | 925..964 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 144 | 931..969 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 145 | 950..986 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 147 | 961..994 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 149 | 975..1008 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 150 | 976..1008 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 152 | 1000..1008 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 35; matched pairs: 1906; unmatched reference entries: 8236; unmatched candidate entries: 4041
- identity switches: 227; fragmentation (coverage interruptions): 469; orphan candidate ids (never on a reference object): 17

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f167: ref 79139: 11 -> 16 at (1946.5, 3016), 5 frames after previous cover
- f169: ref 79136: 11 -> 16 at (1961, 3015.5), 28 frames after previous cover
- f173: ref 79135: 11 -> 16 at (1888, 3016.5), 2 frames after previous cover
- f174: ref 79134: 11 -> 16 at (1870.5, 3021), 6 frames after previous cover
- f175: ref 79128: 11 -> 16 at (1843, 3021), 3 frames after previous cover
- f176: ref 79132: 11 -> 16 at (1812, 3020), 3 frames after previous cover
- f176: ref 79139: 16 -> 18 at (1889.5, 3014.5), 9 frames after previous cover
- f178: ref 79136: 16 -> 18 at (1901.5, 3015.5), 8 frames after previous cover
- f185: ref 79135: 16 -> 18 at (1810, 3015), 5 frames after previous cover
- f186: ref 78971: 5 -> 11 at (1481, 3016), 97 frames after previous cover
- f186: ref 79128: 16 -> 18 at (1771, 3019), 11 frames after previous cover
- f187: ref 79037: 11 -> 16 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 5 -> 11 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 11 -> 16 at (1467.5, 3014), 2 frames after previous cover
- f188: ref 79134: 16 -> 18 at (1777.5, 3018.5), 6 frames after previous cover
- f189: ref 79135: 18 -> 19 at (1782.5, 3013.5), 4 frames after previous cover
- f190: ref 79045: 11 -> 16 at (1469.5, 3012.5), 7 frames after previous cover
- f191: ref 79135: 19 -> 18 at (1769.5, 3011), 2 frames after previous cover
- f192: ref 78899: 16 -> 5 at (1516.5, 3017.5), 6 frames after previous cover
- f192: ref 78969: 11 -> 16 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 78971: 16 -> 11 at (1439.5, 3010.5), 3 frames after previous cover
- f193: ref 79135: 18 -> 19 at (1757, 3013), 2 frames after previous cover
- f194: ref 78897: 11 -> 5 at (1477, 3013.5), 10 frames after previous cover
- f194: ref 79045: 16 -> 11 at (1443.5, 3009.5), 3 frames after previous cover
- f196: ref 79139: 18 -> 19 at (1760, 3010.5), 12 frames after previous cover
- f197: ref 79037: 16 -> 11 at (1440, 3009.5), 10 frames after previous cover
- f197: ref 79097: 11 -> 5 at (1510.5, 3013.5), 17 frames after previous cover
- f200: ref 78897: 5 -> 11 at (1440, 3009), 6 frames after previous cover
- f201: ref 79132: 16 -> 18 at (1646.5, 3013), 25 frames after previous cover
- f203: ref 78897: 11 -> 5 at (1419.5, 3003), 2 frames after previous cover
- f205: ref 78899: 5 -> 11 at (1433, 3006), 1 frames after previous cover
- f207: ref 79134: 18 -> 19 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 18 -> 19 at (1698.5, 3013.5), 27 frames after previous cover
- f210: ref 78899: 11 -> 5 at (1400, 3003.5), 5 frames after previous cover
- f212: ref 79128: 18 -> 19 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 11 -> 18 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 18 -> 19 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 11 -> 18 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 11 -> 5 at (1318.5, 2997), 18 frames after previous cover
- f216: ref 79097: 5 -> 18 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 18 -> 19 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 11 -> 19 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 18 -> 19 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 18 -> 19 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 18 -> 5 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 19 -> 18 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 19 -> 18 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 19 -> 18 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 19 -> 18 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 19 -> 18 at (1429.5, 2998), 6 frames after previous cover
- f229: ref 78971: 11 -> 16 at (1202, 2988), 36 frames after previous cover
- f232: ref 79115: 18 -> 19 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 18 -> 19 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 18 -> 19 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 5 -> 18 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 18 -> 19 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 5 -> 18 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 18 -> 5 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78896: 5 -> 16 at (1090, 2990.5), 52 frames after previous cover
- f239: ref 78971: 16 -> 18 at (1139, 2987), 10 frames after previous cover
- ... 167 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 978 | 7 | 0 (978) |
| 78896 | 350 (76..429) | 12 | 8 | 5 (4), 16 (4), 42 (2), 59 (2) |
| 78969 | 352 (80..434) | 105 | 46 | 16 (71), 5 (19), 59 (11), 11 (2), 42 (2) |
| 78971 | 352 (84..439) | 29 | 16 | 59 (8), 5 (7), 16 (5), 18 (4), 11 (3), 32 (1), 42 (1) |
| 79045 | 355 (84..443) | 36 | 16 | 5 (16), 59 (5), 11 (4), 18 (3), 32 (3), 42 (3), 16 (2) |
| 79037 | 355 (86..445) | 31 | 19 | 5 (11), 18 (5), 16 (4), 11 (3), 32 (3), 59 (3), 42 (2) |
| 78897 | 345 (89..450) | 46 | 25 | 5 (20), 59 (9), 16 (6), 11 (4), 42 (3), 18 (2), 32 (1), 56 (1) |
| 78899 | 365 (91..455) | 67 | 40 | 5 (26), 32 (14), 16 (6), 59 (6), 18 (5), 47 (3), 56 (3), 42 (2), 11 (1), 57 (1) |
| 79097 | 366 (94..461) | 80 | 44 | 5 (44), 18 (7), 32 (7), 47 (5), 59 (5), 16 (4), 42 (3), 57 (3), 11 (1), 56 (1) |
| 79098 | 360 (97..467) | 43 | 23 | 16 (20), 5 (6), 59 (5), 18 (4), 57 (4), 42 (2), 47 (2) |
| 79102 | 371 (98..477) | 34 | 16 | 16 (15), 5 (4), 59 (4), 18 (3), 47 (3), 57 (3), 56 (2) |
| 79103 | 380 (99..481) | 29 | 13 | 5 (14), 59 (5), 47 (4), 57 (3), 18 (2), 11 (1) |
| 79105 | 379 (101..484) | 16 | 8 | 5 (6), 57 (3), 18 (2), 19 (2), 47 (2), 56 (1) |
| 79108 | 385 (104..492) | 24 | 15 | 5 (9), 47 (4), 19 (3), 11 (2), 18 (2), 57 (2), 56 (1), 59 (1) |
| 79110 | 388 (106..497) | 21 | 10 | 59 (7), 19 (5), 5 (3), 47 (3), 18 (2), 57 (1) |
| 79111 | 386 (109..500) | 14 | 7 | 59 (6), 19 (4), 11 (1), 18 (1), 5 (1), 47 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 19 (6), 18 (2), 47 (2), 56 (1), 23 (1), 30 (1) |
| 79116 | 411 (114..530) | 42 | 9 | 30 (37), 23 (3), 31 (2) |
| 79122 | 404 (118..532) | 29 | 14 | 30 (12), 56 (10), 31 (3), 19 (2), 11 (1), 23 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 23 (57), 18 (3), 19 (2), 11 (1), 16 (1), 47 (1) |
| 79128 | 402 (124..527) | 25 | 16 | 18 (7), 19 (5), 23 (4), 11 (3), 31 (3), 56 (2), 16 (1) |
| 79134 | 407 (127..533) | 34 | 24 | 11 (7), 18 (6), 16 (5), 19 (4), 56 (3), 23 (2), 39 (2), 30 (2), 47 (1), 37 (1), 53 (1) |
| 79135 | 409 (129..542) | 68 | 39 | 39 (20), 19 (13), 31 (10), 11 (9), 23 (6), 16 (3), 18 (2), 37 (2), 30 (2), 56 (1) |
| 79139 | 406 (132..537) | 42 | 22 | 19 (13), 39 (9), 37 (5), 11 (4), 31 (4), 23 (3), 18 (2), 16 (1), 56 (1) |
| 79136 | 393 (136..538) | 23 | 12 | 19 (7), 39 (3), 23 (3), 16 (2), 18 (2), 31 (2), 30 (2), 11 (1), 37 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..53 | 31 | 0 | 31 |
| 6 | 88..118 | 31 | 0 | 31 |
| 13 | 151..184 | 34 | 0 | 34 |
| 36 | 269..484 | 216 | 0 | 216 |
| 40 | 276..643 | 368 | 0 | 368 |
| 45 | 298..630 | 333 | 0 | 333 |
| 64 | 392..515 | 124 | 0 | 124 |
| 69 | 410..632 | 223 | 0 | 223 |
| 89 | 530..566 | 37 | 0 | 37 |
| 91 | 530..575 | 46 | 0 | 46 |
| 102 | 593..625 | 33 | 0 | 33 |
| 111 | 657..694 | 38 | 0 | 38 |
| 117 | 721..757 | 37 | 0 | 37 |
| 123 | 786..823 | 38 | 0 | 38 |
| 131 | 848..885 | 38 | 0 | 38 |
| 141 | 913..948 | 36 | 0 | 36 |
| 150 | 976..1008 | 33 | 0 | 33 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 31/99/1007; tracks with internal gaps: 17; total internal gaps: 253; longest internal gap: 215; tracks ending in coasting: 32 (trailing rows total 2328)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 978 | 29 | 7 | 21 | 0 | 78911 |
| 1 | 23..53 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 5 | 80..495 | 416 | 416 | 190 | 226 | 44 | 53 | 34 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 6 | 88..118 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 11 | 139..243 | 105 | 105 | 48 | 57 | 13 | 3 | 38 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79103, 79108, 79111, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 13 | 151..184 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 16 | 167..490 | 324 | 324 | 150 | 174 | 43 | 29 | 26 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79128, 79132, 79134, 79135, 79136, 79139 |
| 18 | 176..303 | 128 | 128 | 66 | 62 | 17 | 3 | 36 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 19 | 188..435 | 248 | 248 | 66 | 182 | 14 | 4 | 162 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 23 | 204..543 | 340 | 340 | 80 | 260 | 12 | 199 | 5 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 30 | 234..619 | 386 | 386 | 56 | 330 | 10 | 215 | 86 | 79115, 79116, 79122, 79134, 79135, 79136 |
| 31 | 240..542 | 303 | 303 | 24 | 279 | 7 | 179 | 0 | 79116, 79122, 79128, 79135, 79136, 79139 |
| 32 | 243..309 | 67 | 67 | 29 | 38 | 5 | 2 | 32 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 36 | 269..484 | 216 | 216 | 0 | 216 | 0 | 0 | 216 | - |
| 37 | 269..367 | 99 | 99 | 9 | 90 | 3 | 58 | 30 | 79134, 79135, 79136, 79139 |
| 39 | 275..641 | 367 | 367 | 34 | 333 | 10 | 153 | 102 | 79134, 79135, 79136, 79139 |
| 40 | 276..643 | 368 | 368 | 0 | 368 | 0 | 0 | 368 | - |
| 42 | 282..321 | 40 | 40 | 20 | 20 | 6 | 5 | 2 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098 |
| 45 | 298..630 | 333 | 333 | 0 | 333 | 0 | 0 | 333 | - |
| 47 | 301..371 | 71 | 71 | 31 | 40 | 15 | 11 | 2 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132, 79134 |
| 53 | 341..371 | 31 | 31 | 1 | 30 | 0 | 0 | 30 | 79134 |
| 56 | 346..472 | 127 | 127 | 27 | 100 | 15 | 22 | 19 | 78897, 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 57 | 347..380 | 34 | 34 | 20 | 14 | 8 | 3 | 0 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 59 | 371..528 | 158 | 158 | 77 | 81 | 24 | 5 | 28 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 64 | 392..515 | 124 | 124 | 0 | 124 | 0 | 0 | 124 | - |
| 69 | 410..632 | 223 | 223 | 0 | 223 | 0 | 0 | 223 | - |
| 89 | 530..566 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 91 | 530..575 | 46 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 102 | 593..625 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 111 | 657..694 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 117 | 721..757 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 123 | 786..823 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 131 | 848..885 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 141 | 913..948 | 36 | 36 | 0 | 36 | 0 | 0 | 36 | - |
| 150 | 976..1008 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
