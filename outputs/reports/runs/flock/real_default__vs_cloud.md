# Tracker evaluation: claim = PARITY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 30, "tentative_threshold": 3}
Reference: predictor=cloud claim=parity curation=n/a

## Provenance
- candidate: config_hash=a78a73f6303f git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_default/tracks.csv sha256=4c462903461fa0e1
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_default
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- reference: config_hash=44136fa355b3 git=none model=cloud-tracke
  - cloud_tracks_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/data/20251012_164031_1DAC_cloud_reference_tracks.csv sha256=d9840f855f6cc35c
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - note: stored output of the cloud tracking pipeline for the same frame window; a reference for parity only
  - note: confidence 1.0 on every row: the export carries no score
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}
- ignore region 'burnt-in timestamp overlay, top-left': entries with center inside it are dropped on both sides before scoring

## Metrics (center-distance matching)
| view | region | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|
| observations | none | 4 | 0.476 | 0.399 | 0.370 | 0.12 | 0.469 | 160 | 435.0 |
| observations | none | 6 | 0.482 | 0.398 | 0.384 | 0.16 | 0.472 | 164 | 443.0 |
| observations | none | 8 | 0.485 | 0.397 | 0.398 | 0.23 | 0.474 | 170 | 449.0 |
| observations | none | 12 | 0.492 | 0.394 | 0.431 | 0.46 | 0.479 | 190 | 451.0 |
| observations | ignore | 4 | 0.495 | 0.399 | 0.471 | 0.12 | 0.492 | 160 | 435.0 |
| observations | ignore | 6 | 0.500 | 0.398 | 0.486 | 0.16 | 0.495 | 164 | 443.0 |
| observations | ignore | 8 | 0.504 | 0.397 | 0.500 | 0.23 | 0.497 | 170 | 449.0 |
| observations | ignore | 12 | 0.512 | 0.394 | 0.532 | 0.46 | 0.502 | 190 | 451.0 |
| updates | none | 4 | 0.351 | 0.363 | -0.583 | 0.13 | 0.327 | 164 | 441.0 |
| updates | none | 6 | 0.355 | 0.364 | -0.562 | 0.20 | 0.330 | 170 | 451.0 |
| updates | none | 8 | 0.357 | 0.362 | -0.540 | 0.31 | 0.332 | 177 | 462.0 |
| updates | none | 12 | 0.362 | 0.359 | -0.496 | 0.61 | 0.337 | 189 | 453.0 |
| updates | ignore | 4 | 0.391 | 0.363 | -0.125 | 0.13 | 0.383 | 164 | 441.0 |
| updates | ignore | 6 | 0.396 | 0.364 | -0.104 | 0.20 | 0.386 | 170 | 451.0 |
| updates | ignore | 8 | 0.399 | 0.362 | -0.081 | 0.31 | 0.389 | 177 | 462.0 |
| updates | ignore | 12 | 0.405 | 0.359 | -0.038 | 0.61 | 0.395 | 189 | 453.0 |

HOTA = sqrt(DetA * AssA), TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T). AssA = association accuracy (one bird, one id). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches, Frag = fragmentations (CLEAR definition; counts resumptions after any interruption, including frames where the reference object itself is absent, so the flock GT's 111 gaps give Frag > 0 even to a perfect candidate). Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. All other TrackEval fields (DetA, DetRe, DetPr, AssRe, AssPr, OWTA, LocA, IDP, IDR, MT/PT/ML, TP/FP/FN) are in the JSON report.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 17; candidate ids: 78; matched pairs: 2877; unmatched reference entries: 665; unmatched candidate entries: 1296
- identity switches: 170; fragmentation (coverage interruptions): 285; orphan candidate ids (never on a reference object): 57

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f181: ref 508: 16 -> 18 at (1870, 3016.5), 8 frames after previous cover
- f184: ref 511: 16 -> 11 at (1545.5, 3020), 1 frames after previous cover
- f186: ref 496: 5 -> 11 at (1475, 3014), 1 frames after previous cover
- f186: ref 511: 11 -> 16 at (1554.5, 3019), 1 frames after previous cover
- f188: ref 496: 11 -> 16 at (1462, 3014), 1 frames after previous cover
- f188: ref 508: 18 -> 19 at (1824.5, 3016), 7 frames after previous cover
- f189: ref 496: 16 -> 5 at (1443, 3011), 1 frames after previous cover
- f192: ref 496: 5 -> 16 at (1417, 3009.5), 1 frames after previous cover
- f192: ref 511: 16 -> 5 at (1515, 3017), 5 frames after previous cover
- f200: ref 503: 11 -> 18 at (1694.5, 3009.5), 34 frames after previous cover
- f213: ref 503: 18 -> 19 at (1595, 3007.5), 5 frames after previous cover
- f218: ref 511: 5 -> 18 at (1382, 2999.5), 2 frames after previous cover
- f222: ref 511: 18 -> 5 at (1358, 2995.5), 2 frames after previous cover
- f235: ref 511: 5 -> 18 at (1243, 2987.5), 1 frames after previous cover
- f237: ref 503: 19 -> 5 at (1286, 2990.5), 2 frames after previous cover
- f238: ref 511: 18 -> 5 at (1252, 2988), 3 frames after previous cover
- f243: ref 511: 5 -> 32 at (1219.5, 2988), 4 frames after previous cover
- f246: ref 503: 5 -> 32 at (1200, 2987), 9 frames after previous cover
- f257: ref 508: 19 -> 32 at (1132, 2984), 11 frames after previous cover
- f263: ref 508: 32 -> 5 at (1094, 2985.5), 4 frames after previous cover
- f264: ref 503: 32 -> 16 at (953.5, 2988), 9 frames after previous cover
- f264: ref 508: 5 -> 32 at (1056.5, 2986), 1 frames after previous cover
- f267: ref 508: 32 -> 5 at (1069, 2985), 1 frames after previous cover
- f268: ref 508: 5 -> 32 at (1031.5, 2986), 1 frames after previous cover
- f270: ref 496: 16 -> 18 at (786.5, 3257), 8 frames after previous cover
- f271: ref 508: 32 -> 5 at (1042.5, 2986), 2 frames after previous cover
- f274: ref 511: 32 -> 16 at (890.5, 2986.5), 3 frames after previous cover
- f274: ref 528: 37 -> 36 at (2147, 2974.5), 2 frames after previous cover
- f277: ref 527: 36 -> 37 at (1944.5, 2980), 8 frames after previous cover
- f279: ref 503: 16 -> 32 at (813.5, 3004.5), 2 frames after previous cover
- f282: ref 528: 36 -> 40 at (2024, 2972.5), 8 frames after previous cover
- f283: ref 503: 32 -> 16 at (808.5, 3164.5), 3 frames after previous cover
- f285: ref 508: 5 -> 42 at (871.5, 3003.5), 2 frames after previous cover
- f285: ref 527: 37 -> 40 at (1945, 2976), 8 frames after previous cover
- f289: ref 527: 40 -> 37 at (1863, 2975), 4 frames after previous cover
- f293: ref 532: 36 -> 40 at (2049.5, 2969.5), 3 frames after previous cover
- f294: ref 528: 40 -> 37 at (1927.5, 2967.5), 6 frames after previous cover
- f298: ref 514: 23 -> 19 at (1378.5, 2947.5), 1 frames after previous cover
- f298: ref 528: 37 -> 45 at (1894, 2966.5), 4 frames after previous cover
- f299: ref 514: 19 -> 23 at (1370, 2949.5), 1 frames after previous cover
- f301: ref 496: 18 -> 47 at (929, 2985.5), 31 frames after previous cover
- f301: ref 530: 39 -> 37 at (1688.5, 2969), 1 frames after previous cover
- f302: ref 530: 37 -> 39 at (1686.5, 2968), 1 frames after previous cover
- f305: ref 527: 37 -> 45 at (1784, 2967.5), 16 frames after previous cover
- f305: ref 528: 45 -> 36 at (1839.5, 2968), 2 frames after previous cover
- f306: ref 527: 45 -> 36 at (1797.5, 2967), 1 frames after previous cover
- f307: ref 527: 36 -> 45 at (1766, 2967.5), 1 frames after previous cover
- f308: ref 522: 31 -> 37 at (1554.5, 2962), 1 frames after previous cover
- f309: ref 522: 37 -> 31 at (1545.5, 2963), 1 frames after previous cover
- f314: ref 542: 36 -> 40 at (1881.5, 2963), 11 frames after previous cover
- f319: ref 542: 40 -> 36 at (1814, 2962.5), 1 frames after previous cover
- f320: ref 528: 36 -> 45 at (1720, 2963.5), 2 frames after previous cover
- f327: ref 527: 45 -> 19 at (1608.5, 2960.5), 12 frames after previous cover
- f327: ref 532: 40 -> 45 at (1662.5, 2962), 15 frames after previous cover
- f332: ref 496: 47 -> 5 at (688, 2974.5), 1 frames after previous cover
- f333: ref 496: 5 -> 47 at (654, 2975), 1 frames after previous cover
- f342: ref 496: 47 -> 16 at (459, 2963), 1 frames after previous cover
- f348: ref 528: 45 -> 39 at (1304, 2951.5), 23 frames after previous cover
- f359: ref 532: 45 -> 19 at (1410.5, 2952.5), 8 frames after previous cover
- f363: ref 530: 39 -> 19 at (1324, 2946.5), 16 frames after previous cover
- ... 110 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 491 | 856 (0..896) | 839 | 5 | 0 (839) |
| 496 | 241 (78..446) | 210 | 22 | 5 (106), 16 (83), 47 (16), 11 (2), 18 (1), 56 (1), 59 (1) |
| 503 | 229 (137..499) | 158 | 32 | 16 (67), 59 (48), 11 (17), 5 (9), 32 (8), 19 (5), 18 (3), 56 (1) |
| 508 | 81 (165..286) | 49 | 10 | 19 (28), 5 (9), 32 (6), 16 (3), 42 (2), 18 (1) |
| 511 | 71 (183..279) | 55 | 11 | 5 (33), 32 (11), 16 (5), 18 (4), 11 (2) |
| 514 | 296 (202..614) | 282 | 10 | 23 (206), 30 (52), 39 (10), 40 (10), 69 (2), 19 (1), 45 (1) |
| 521 | 244 (232..601) | 231 | 9 | 30 (158), 45 (35), 31 (28), 39 (4), 23 (3), 56 (2), 69 (1) |
| 522 | 216 (238..498) | 185 | 21 | 31 (114), 39 (38), 59 (18), 16 (10), 5 (3), 37 (1), 23 (1) |
| 527 | 119 (264..496) | 61 | 15 | 31 (22), 30 (15), 39 (7), 45 (5), 19 (4), 36 (2), 37 (2), 23 (2), 40 (1), 56 (1) |
| 528 | 141 (267..534) | 77 | 24 | 39 (33), 36 (13), 45 (9), 30 (9), 19 (5), 40 (4), 37 (3), 31 (1) |
| 530 | 177 (273..520) | 100 | 21 | 39 (55), 40 (31), 19 (7), 36 (3), 45 (2), 37 (1), 69 (1) |
| 532 | 120 (275..455) | 74 | 26 | 36 (31), 40 (20), 45 (20), 19 (3) |
| 542 | 185 (293..557) | 116 | 25 | 40 (67), 36 (35), 45 (14) |
| 549 | 107 (323..545) | 52 | 20 | 39 (27), 64 (10), 40 (8), 69 (3), 45 (2), 31 (1), 30 (1) |
| 559 | 183 (354..612) | 128 | 24 | 69 (74), 45 (26), 39 (13), 64 (12), 40 (3) |
| 561 | 139 (363..513) | 126 | 9 | 23 (74), 56 (51), 31 (1) |
| 647 | 137 (840..1008) | 134 | 1 | 0 (134) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..24 | 2 | 0 | 2 |
| 6 | 88..89 | 2 | 0 | 2 |
| 13 | 151..155 | 5 | 0 | 3 |
| 22 | 200..209 | 10 | 0 | 8 |
| 26 | 217..222 | 6 | 0 | 5 |
| 28 | 225..233 | 9 | 0 | 9 |
| 33 | 250..258 | 9 | 0 | 9 |
| 38 | 275..290 | 16 | 0 | 15 |
| 41 | 279..284 | 6 | 0 | 5 |
| 46 | 300..311 | 12 | 0 | 10 |
| 50 | 325..335 | 11 | 0 | 11 |
| 53 | 341..342 | 2 | 0 | 2 |
| 54 | 341..346 | 6 | 0 | 5 |
| 57 | 347..351 | 5 | 0 | 5 |
| 58 | 350..360 | 11 | 0 | 10 |
| 61 | 375..384 | 10 | 0 | 10 |
| 66 | 400..433 | 34 | 0 | 13 |
| 67 | 403..408 | 6 | 0 | 5 |
| 72 | 451..456 | 6 | 0 | 5 |
| 74 | 465..470 | 6 | 0 | 5 |
| 79 | 475..483 | 9 | 0 | 9 |
| 84 | 500..508 | 9 | 0 | 9 |
| 86 | 525..535 | 11 | 0 | 9 |
| 87 | 527..532 | 6 | 0 | 5 |
| 89 | 530..537 | 8 | 0 | 5 |
| 91 | 530..546 | 17 | 0 | 12 |
| 95 | 550..561 | 12 | 0 | 10 |
| 101 | 589..594 | 6 | 0 | 5 |
| 102 | 593..596 | 4 | 0 | 4 |
| 105 | 600..610 | 11 | 0 | 10 |
| 107 | 625..634 | 10 | 0 | 10 |
| 109 | 651..656 | 6 | 0 | 5 |
| 111 | 657..665 | 9 | 0 | 9 |
| 113 | 675..685 | 11 | 0 | 11 |
| 114 | 701..708 | 8 | 0 | 7 |
| 115 | 713..718 | 6 | 0 | 5 |
| 117 | 721..728 | 8 | 0 | 3 |
| 119 | 725..733 | 9 | 0 | 9 |
| 120 | 750..758 | 9 | 0 | 9 |
| 121 | 775..782 | 8 | 0 | 8 |
| ... | 17 more | | | |

### Gaps and durations of candidate tracks
- tracks: 78; lifespan min/median/max: 2/10/1007; tracks with internal gaps: 21; total internal gaps: 303; longest internal gap: 43; tracks ending in coasting: 65 (trailing rows total 446)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 981 | 973 | 8 | 6 | 3 | 0 | 491, 647 |
| 1 | 23..24 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 5 | 80..466 | 387 | 264 | 160 | 104 | 25 | 32 | 0 | 496, 503, 508, 511, 522 |
| 6 | 88..89 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 11 | 139..214 | 76 | 36 | 21 | 15 | 1 | 12 | 3 | 496, 503, 511 |
| 13 | 151..155 | 5 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 16 | 167..461 | 295 | 230 | 168 | 62 | 34 | 10 | 2 | 496, 503, 508, 511, 522 |
| 18 | 176..274 | 99 | 45 | 9 | 36 | 5 | 9 | 1 | 496, 503, 508, 511 |
| 19 | 188..406 | 219 | 103 | 53 | 50 | 16 | 8 | 4 | 503, 508, 514, 527, 528, 530, 532 |
| 22 | 200..209 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 23 | 204..514 | 311 | 298 | 286 | 12 | 8 | 5 | 0 | 514, 521, 522, 527, 561 |
| 26 | 217..222 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 28 | 225..233 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 30 | 234..590 | 357 | 273 | 235 | 38 | 18 | 9 | 0 | 514, 521, 527, 528, 549 |
| 31 | 240..513 | 274 | 192 | 167 | 25 | 14 | 5 | 0 | 521, 522, 527, 528, 549, 561 |
| 32 | 243..280 | 38 | 31 | 25 | 6 | 3 | 4 | 0 | 503, 508, 511 |
| 33 | 250..258 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 36 | 269..455 | 187 | 137 | 84 | 53 | 28 | 8 | 0 | 527, 528, 530, 532, 542 |
| 37 | 269..338 | 70 | 29 | 7 | 22 | 4 | 7 | 7 | 522, 527, 528, 530 |
| 38 | 275..290 | 16 | 15 | 0 | 15 | 0 | 0 | 15 | - |
| 39 | 275..612 | 338 | 242 | 187 | 55 | 29 | 6 | 0 | 514, 521, 522, 527, 528, 530, 549, 559 |
| 40 | 276..614 | 339 | 262 | 144 | 118 | 27 | 15 | 0 | 514, 527, 528, 530, 532, 542, 549, 559 |
| 41 | 279..284 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 42 | 282..292 | 11 | 7 | 2 | 5 | 1 | 3 | 2 | 508 |
| 45 | 298..601 | 304 | 226 | 114 | 112 | 40 | 43 | 0 | 514, 521, 527, 528, 530, 532, 542, 549, 559 |
| 46 | 300..311 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 47 | 301..342 | 42 | 28 | 16 | 12 | 5 | 5 | 1 | 496 |
| 50 | 325..335 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 53 | 341..342 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 54 | 341..346 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 56 | 346..443 | 98 | 69 | 56 | 13 | 7 | 4 | 0 | 496, 503, 521, 527, 561 |
| 57 | 347..351 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 58 | 350..360 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 59 | 371..499 | 129 | 100 | 67 | 33 | 12 | 15 | 0 | 496, 503, 522 |
| 61 | 375..384 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 64 | 392..486 | 95 | 47 | 22 | 25 | 10 | 5 | 5 | 549, 559 |
| 66 | 400..433 | 34 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 67 | 403..408 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 69 | 410..603 | 194 | 152 | 81 | 71 | 10 | 32 | 0 | 514, 521, 530, 549, 559 |
| 72 | 451..456 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 74 | 465..470 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 79 | 475..483 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 84 | 500..508 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 86 | 525..535 | 11 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 87 | 527..532 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 89 | 530..537 | 8 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 91 | 530..546 | 17 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 95 | 550..561 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 101 | 589..594 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 102 | 593..596 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 105 | 600..610 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 107 | 625..634 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 109 | 651..656 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 111 | 657..665 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 113 | 675..685 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 114 | 701..708 | 8 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 115 | 713..718 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 117 | 721..728 | 8 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 119 | 725..733 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 120 | 750..758 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 121 | 775..782 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 123 | 786..794 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 125 | 800..811 | 12 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 127 | 825..834 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 128 | 837..842 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 131 | 848..856 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 133 | 850..860 | 11 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 135 | 875..885 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 136 | 899..906 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 137 | 901..911 | 11 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 141 | 913..919 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 143 | 925..935 | 11 | 11 | 0 | 11 | 0 | 0 | 11 | - |
| 144 | 931..940 | 10 | 10 | 0 | 10 | 0 | 0 | 10 | - |
| 145 | 950..957 | 8 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 147 | 961..965 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 149 | 975..983 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 150 | 976..981 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 152 | 1000..1008 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 17; candidate ids: 35; matched pairs: 2877; unmatched reference entries: 665; unmatched candidate entries: 937
- identity switches: 170; fragmentation (coverage interruptions): 285; orphan candidate ids (never on a reference object): 14

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f181: ref 508: 16 -> 18 at (1870, 3016.5), 8 frames after previous cover
- f184: ref 511: 16 -> 11 at (1545.5, 3020), 1 frames after previous cover
- f186: ref 496: 5 -> 11 at (1475, 3014), 1 frames after previous cover
- f186: ref 511: 11 -> 16 at (1554.5, 3019), 1 frames after previous cover
- f188: ref 496: 11 -> 16 at (1462, 3014), 1 frames after previous cover
- f188: ref 508: 18 -> 19 at (1824.5, 3016), 7 frames after previous cover
- f189: ref 496: 16 -> 5 at (1443, 3011), 1 frames after previous cover
- f192: ref 496: 5 -> 16 at (1417, 3009.5), 1 frames after previous cover
- f192: ref 511: 16 -> 5 at (1515, 3017), 5 frames after previous cover
- f200: ref 503: 11 -> 18 at (1694.5, 3009.5), 34 frames after previous cover
- f213: ref 503: 18 -> 19 at (1595, 3007.5), 5 frames after previous cover
- f218: ref 511: 5 -> 18 at (1382, 2999.5), 2 frames after previous cover
- f222: ref 511: 18 -> 5 at (1358, 2995.5), 2 frames after previous cover
- f235: ref 511: 5 -> 18 at (1243, 2987.5), 1 frames after previous cover
- f237: ref 503: 19 -> 5 at (1286, 2990.5), 2 frames after previous cover
- f238: ref 511: 18 -> 5 at (1252, 2988), 3 frames after previous cover
- f243: ref 511: 5 -> 32 at (1219.5, 2988), 4 frames after previous cover
- f246: ref 503: 5 -> 32 at (1200, 2987), 9 frames after previous cover
- f257: ref 508: 19 -> 32 at (1132, 2984), 11 frames after previous cover
- f263: ref 508: 32 -> 5 at (1094, 2985.5), 4 frames after previous cover
- f264: ref 503: 32 -> 16 at (953.5, 2988), 9 frames after previous cover
- f264: ref 508: 5 -> 32 at (1056.5, 2986), 1 frames after previous cover
- f267: ref 508: 32 -> 5 at (1069, 2985), 1 frames after previous cover
- f268: ref 508: 5 -> 32 at (1031.5, 2986), 1 frames after previous cover
- f270: ref 496: 16 -> 18 at (786.5, 3257), 8 frames after previous cover
- f271: ref 508: 32 -> 5 at (1042.5, 2986), 2 frames after previous cover
- f274: ref 511: 32 -> 16 at (890.5, 2986.5), 3 frames after previous cover
- f274: ref 528: 37 -> 36 at (2147, 2974.5), 2 frames after previous cover
- f277: ref 527: 36 -> 37 at (1944.5, 2980), 8 frames after previous cover
- f279: ref 503: 16 -> 32 at (813.5, 3004.5), 2 frames after previous cover
- f282: ref 528: 36 -> 40 at (2024, 2972.5), 8 frames after previous cover
- f283: ref 503: 32 -> 16 at (808.5, 3164.5), 3 frames after previous cover
- f285: ref 508: 5 -> 42 at (871.5, 3003.5), 2 frames after previous cover
- f285: ref 527: 37 -> 40 at (1945, 2976), 8 frames after previous cover
- f289: ref 527: 40 -> 37 at (1863, 2975), 4 frames after previous cover
- f293: ref 532: 36 -> 40 at (2049.5, 2969.5), 3 frames after previous cover
- f294: ref 528: 40 -> 37 at (1927.5, 2967.5), 6 frames after previous cover
- f298: ref 514: 23 -> 19 at (1378.5, 2947.5), 1 frames after previous cover
- f298: ref 528: 37 -> 45 at (1894, 2966.5), 4 frames after previous cover
- f299: ref 514: 19 -> 23 at (1370, 2949.5), 1 frames after previous cover
- f301: ref 496: 18 -> 47 at (929, 2985.5), 31 frames after previous cover
- f301: ref 530: 39 -> 37 at (1688.5, 2969), 1 frames after previous cover
- f302: ref 530: 37 -> 39 at (1686.5, 2968), 1 frames after previous cover
- f305: ref 527: 37 -> 45 at (1784, 2967.5), 16 frames after previous cover
- f305: ref 528: 45 -> 36 at (1839.5, 2968), 2 frames after previous cover
- f306: ref 527: 45 -> 36 at (1797.5, 2967), 1 frames after previous cover
- f307: ref 527: 36 -> 45 at (1766, 2967.5), 1 frames after previous cover
- f308: ref 522: 31 -> 37 at (1554.5, 2962), 1 frames after previous cover
- f309: ref 522: 37 -> 31 at (1545.5, 2963), 1 frames after previous cover
- f314: ref 542: 36 -> 40 at (1881.5, 2963), 11 frames after previous cover
- f319: ref 542: 40 -> 36 at (1814, 2962.5), 1 frames after previous cover
- f320: ref 528: 36 -> 45 at (1720, 2963.5), 2 frames after previous cover
- f327: ref 527: 45 -> 19 at (1608.5, 2960.5), 12 frames after previous cover
- f327: ref 532: 40 -> 45 at (1662.5, 2962), 15 frames after previous cover
- f332: ref 496: 47 -> 5 at (688, 2974.5), 1 frames after previous cover
- f333: ref 496: 5 -> 47 at (654, 2975), 1 frames after previous cover
- f342: ref 496: 47 -> 16 at (459, 2963), 1 frames after previous cover
- f348: ref 528: 45 -> 39 at (1304, 2951.5), 23 frames after previous cover
- f359: ref 532: 45 -> 19 at (1410.5, 2952.5), 8 frames after previous cover
- f363: ref 530: 39 -> 19 at (1324, 2946.5), 16 frames after previous cover
- ... 110 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 491 | 856 (0..896) | 839 | 5 | 0 (839) |
| 496 | 241 (78..446) | 210 | 22 | 5 (106), 16 (83), 47 (16), 11 (2), 18 (1), 56 (1), 59 (1) |
| 503 | 229 (137..499) | 158 | 32 | 16 (67), 59 (48), 11 (17), 5 (9), 32 (8), 19 (5), 18 (3), 56 (1) |
| 508 | 81 (165..286) | 49 | 10 | 19 (28), 5 (9), 32 (6), 16 (3), 42 (2), 18 (1) |
| 511 | 71 (183..279) | 55 | 11 | 5 (33), 32 (11), 16 (5), 18 (4), 11 (2) |
| 514 | 296 (202..614) | 282 | 10 | 23 (206), 30 (52), 39 (10), 40 (10), 69 (2), 19 (1), 45 (1) |
| 521 | 244 (232..601) | 231 | 9 | 30 (158), 45 (35), 31 (28), 39 (4), 23 (3), 56 (2), 69 (1) |
| 522 | 216 (238..498) | 185 | 21 | 31 (114), 39 (38), 59 (18), 16 (10), 5 (3), 37 (1), 23 (1) |
| 527 | 119 (264..496) | 61 | 15 | 31 (22), 30 (15), 39 (7), 45 (5), 19 (4), 36 (2), 37 (2), 23 (2), 40 (1), 56 (1) |
| 528 | 141 (267..534) | 77 | 24 | 39 (33), 36 (13), 45 (9), 30 (9), 19 (5), 40 (4), 37 (3), 31 (1) |
| 530 | 177 (273..520) | 100 | 21 | 39 (55), 40 (31), 19 (7), 36 (3), 45 (2), 37 (1), 69 (1) |
| 532 | 120 (275..455) | 74 | 26 | 36 (31), 40 (20), 45 (20), 19 (3) |
| 542 | 185 (293..557) | 116 | 25 | 40 (67), 36 (35), 45 (14) |
| 549 | 107 (323..545) | 52 | 20 | 39 (27), 64 (10), 40 (8), 69 (3), 45 (2), 31 (1), 30 (1) |
| 559 | 183 (354..612) | 128 | 24 | 69 (74), 45 (26), 39 (13), 64 (12), 40 (3) |
| 561 | 139 (363..513) | 126 | 9 | 23 (74), 56 (51), 31 (1) |
| 647 | 137 (840..1008) | 134 | 1 | 0 (134) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..24 | 2 | 0 | 2 |
| 6 | 88..89 | 2 | 0 | 2 |
| 13 | 151..155 | 5 | 0 | 3 |
| 53 | 341..342 | 2 | 0 | 2 |
| 57 | 347..351 | 5 | 0 | 5 |
| 89 | 530..537 | 8 | 0 | 5 |
| 91 | 530..546 | 17 | 0 | 12 |
| 102 | 593..596 | 4 | 0 | 4 |
| 111 | 657..665 | 9 | 0 | 9 |
| 117 | 721..728 | 8 | 0 | 3 |
| 123 | 786..794 | 9 | 0 | 4 |
| 131 | 848..856 | 9 | 0 | 4 |
| 141 | 913..919 | 7 | 0 | 3 |
| 150 | 976..981 | 6 | 0 | 4 |

### Gaps and durations of candidate tracks
- tracks: 35; lifespan min/median/max: 2/70/1007; tracks with internal gaps: 21; total internal gaps: 303; longest internal gap: 43; tracks ending in coasting: 22 (trailing rows total 87)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 981 | 973 | 8 | 6 | 3 | 0 | 491, 647 |
| 1 | 23..24 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 5 | 80..466 | 387 | 264 | 160 | 104 | 25 | 32 | 0 | 496, 503, 508, 511, 522 |
| 6 | 88..89 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 11 | 139..214 | 76 | 36 | 21 | 15 | 1 | 12 | 3 | 496, 503, 511 |
| 13 | 151..155 | 5 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 16 | 167..461 | 295 | 230 | 168 | 62 | 34 | 10 | 2 | 496, 503, 508, 511, 522 |
| 18 | 176..274 | 99 | 45 | 9 | 36 | 5 | 9 | 1 | 496, 503, 508, 511 |
| 19 | 188..406 | 219 | 103 | 53 | 50 | 16 | 8 | 4 | 503, 508, 514, 527, 528, 530, 532 |
| 23 | 204..514 | 311 | 298 | 286 | 12 | 8 | 5 | 0 | 514, 521, 522, 527, 561 |
| 30 | 234..590 | 357 | 273 | 235 | 38 | 18 | 9 | 0 | 514, 521, 527, 528, 549 |
| 31 | 240..513 | 274 | 192 | 167 | 25 | 14 | 5 | 0 | 521, 522, 527, 528, 549, 561 |
| 32 | 243..280 | 38 | 31 | 25 | 6 | 3 | 4 | 0 | 503, 508, 511 |
| 36 | 269..455 | 187 | 137 | 84 | 53 | 28 | 8 | 0 | 527, 528, 530, 532, 542 |
| 37 | 269..338 | 70 | 29 | 7 | 22 | 4 | 7 | 7 | 522, 527, 528, 530 |
| 39 | 275..612 | 338 | 242 | 187 | 55 | 29 | 6 | 0 | 514, 521, 522, 527, 528, 530, 549, 559 |
| 40 | 276..614 | 339 | 262 | 144 | 118 | 27 | 15 | 0 | 514, 527, 528, 530, 532, 542, 549, 559 |
| 42 | 282..292 | 11 | 7 | 2 | 5 | 1 | 3 | 2 | 508 |
| 45 | 298..601 | 304 | 226 | 114 | 112 | 40 | 43 | 0 | 514, 521, 527, 528, 530, 532, 542, 549, 559 |
| 47 | 301..342 | 42 | 28 | 16 | 12 | 5 | 5 | 1 | 496 |
| 53 | 341..342 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 56 | 346..443 | 98 | 69 | 56 | 13 | 7 | 4 | 0 | 496, 503, 521, 527, 561 |
| 57 | 347..351 | 5 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 59 | 371..499 | 129 | 100 | 67 | 33 | 12 | 15 | 0 | 496, 503, 522 |
| 64 | 392..486 | 95 | 47 | 22 | 25 | 10 | 5 | 5 | 549, 559 |
| 69 | 410..603 | 194 | 152 | 81 | 71 | 10 | 32 | 0 | 514, 521, 530, 549, 559 |
| 89 | 530..537 | 8 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 91 | 530..546 | 17 | 12 | 0 | 12 | 0 | 0 | 12 | - |
| 102 | 593..596 | 4 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 111 | 657..665 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 117 | 721..728 | 8 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 123 | 786..794 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 131 | 848..856 | 9 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 141 | 913..919 | 7 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 150 | 976..981 | 6 | 4 | 0 | 4 | 0 | 0 | 4 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 17; candidate ids: 78; matched pairs: 2918; unmatched reference entries: 624; unmatched candidate entries: 4653
- identity switches: 177; fragmentation (coverage interruptions): 284; orphan candidate ids (never on a reference object): 57

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f178: ref 508: 16 -> 18 at (1889.5, 3015.5), 5 frames after previous cover
- f179: ref 503: 11 -> 16 at (1846, 3017), 13 frames after previous cover
- f184: ref 511: 16 -> 11 at (1545.5, 3020), 1 frames after previous cover
- f186: ref 496: 5 -> 11 at (1475, 3014), 1 frames after previous cover
- f186: ref 511: 11 -> 16 at (1554.5, 3019), 1 frames after previous cover
- f188: ref 496: 11 -> 16 at (1462, 3014), 1 frames after previous cover
- f188: ref 508: 18 -> 19 at (1824.5, 3016), 7 frames after previous cover
- f189: ref 496: 16 -> 5 at (1443, 3011), 1 frames after previous cover
- f192: ref 496: 5 -> 16 at (1417, 3009.5), 1 frames after previous cover
- f192: ref 511: 16 -> 5 at (1515, 3017), 5 frames after previous cover
- f200: ref 503: 16 -> 18 at (1694.5, 3009.5), 21 frames after previous cover
- f213: ref 503: 18 -> 19 at (1595, 3007.5), 5 frames after previous cover
- f218: ref 511: 5 -> 18 at (1382, 2999.5), 2 frames after previous cover
- f222: ref 511: 18 -> 5 at (1358, 2995.5), 2 frames after previous cover
- f235: ref 511: 5 -> 18 at (1243, 2987.5), 1 frames after previous cover
- f237: ref 503: 19 -> 5 at (1286, 2990.5), 2 frames after previous cover
- f238: ref 511: 18 -> 5 at (1252, 2988), 2 frames after previous cover
- f243: ref 511: 5 -> 32 at (1219.5, 2988), 4 frames after previous cover
- f246: ref 503: 5 -> 32 at (1200, 2987), 9 frames after previous cover
- f251: ref 503: 32 -> 18 at (1097.5, 2988), 1 frames after previous cover
- f255: ref 503: 18 -> 32 at (1072.5, 2988), 2 frames after previous cover
- f257: ref 508: 19 -> 32 at (1132, 2984), 11 frames after previous cover
- f263: ref 508: 32 -> 5 at (1094, 2985.5), 4 frames after previous cover
- f264: ref 503: 32 -> 16 at (953.5, 2988), 8 frames after previous cover
- f264: ref 508: 5 -> 32 at (1056.5, 2986), 1 frames after previous cover
- f267: ref 508: 32 -> 5 at (1069, 2985), 1 frames after previous cover
- f268: ref 508: 5 -> 32 at (1031.5, 2986), 1 frames after previous cover
- f270: ref 496: 16 -> 18 at (786.5, 3257), 8 frames after previous cover
- f271: ref 508: 32 -> 5 at (1042.5, 2986), 2 frames after previous cover
- f274: ref 511: 32 -> 16 at (890.5, 2986.5), 3 frames after previous cover
- f274: ref 528: 37 -> 36 at (2147, 2974.5), 2 frames after previous cover
- f277: ref 527: 36 -> 37 at (1944.5, 2980), 8 frames after previous cover
- f279: ref 503: 16 -> 32 at (813.5, 3004.5), 2 frames after previous cover
- f282: ref 528: 36 -> 40 at (2024, 2972.5), 8 frames after previous cover
- f283: ref 503: 32 -> 16 at (808.5, 3164.5), 3 frames after previous cover
- f285: ref 508: 5 -> 42 at (871.5, 3003.5), 2 frames after previous cover
- f285: ref 527: 37 -> 40 at (1945, 2976), 8 frames after previous cover
- f289: ref 527: 40 -> 37 at (1863, 2975), 4 frames after previous cover
- f293: ref 532: 36 -> 40 at (2049.5, 2969.5), 3 frames after previous cover
- f294: ref 528: 40 -> 37 at (1927.5, 2967.5), 6 frames after previous cover
- f298: ref 514: 23 -> 19 at (1378.5, 2947.5), 1 frames after previous cover
- f298: ref 528: 37 -> 45 at (1894, 2966.5), 4 frames after previous cover
- f299: ref 514: 19 -> 23 at (1370, 2949.5), 1 frames after previous cover
- f301: ref 496: 18 -> 47 at (929, 2985.5), 31 frames after previous cover
- f305: ref 527: 37 -> 45 at (1784, 2967.5), 13 frames after previous cover
- f305: ref 528: 45 -> 36 at (1839.5, 2968), 2 frames after previous cover
- f306: ref 527: 45 -> 36 at (1797.5, 2967), 1 frames after previous cover
- f307: ref 527: 36 -> 45 at (1766, 2967.5), 1 frames after previous cover
- f308: ref 522: 31 -> 37 at (1554.5, 2962), 1 frames after previous cover
- f309: ref 522: 37 -> 31 at (1545.5, 2963), 1 frames after previous cover
- f314: ref 542: 36 -> 40 at (1881.5, 2963), 11 frames after previous cover
- f319: ref 542: 40 -> 36 at (1814, 2962.5), 1 frames after previous cover
- f320: ref 528: 36 -> 45 at (1720, 2963.5), 2 frames after previous cover
- f327: ref 527: 45 -> 19 at (1608.5, 2960.5), 12 frames after previous cover
- f327: ref 532: 40 -> 45 at (1662.5, 2962), 15 frames after previous cover
- f332: ref 496: 47 -> 5 at (688, 2974.5), 1 frames after previous cover
- f333: ref 496: 5 -> 47 at (654, 2975), 1 frames after previous cover
- f340: ref 528: 45 -> 19 at (1494, 2958), 15 frames after previous cover
- f342: ref 496: 47 -> 16 at (459, 2963), 1 frames after previous cover
- f348: ref 528: 19 -> 39 at (1304, 2951.5), 8 frames after previous cover
- ... 117 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 491 | 856 (0..896) | 840 | 4 | 0 (840) |
| 496 | 241 (78..446) | 210 | 22 | 5 (106), 16 (83), 47 (16), 11 (2), 18 (1), 56 (1), 59 (1) |
| 503 | 229 (137..499) | 166 | 30 | 16 (72), 59 (47), 11 (17), 5 (10), 32 (8), 18 (5), 19 (5), 56 (2) |
| 508 | 81 (165..286) | 50 | 10 | 19 (28), 5 (9), 32 (6), 16 (3), 18 (2), 42 (2) |
| 511 | 71 (183..279) | 56 | 10 | 5 (33), 32 (11), 16 (5), 18 (5), 11 (2) |
| 514 | 296 (202..614) | 285 | 7 | 23 (207), 30 (55), 39 (10), 40 (9), 69 (2), 19 (1), 45 (1) |
| 521 | 244 (232..601) | 231 | 9 | 30 (158), 45 (35), 31 (28), 39 (4), 23 (3), 56 (2), 69 (1) |
| 522 | 216 (238..498) | 187 | 19 | 31 (114), 39 (39), 59 (18), 16 (11), 5 (3), 37 (1), 23 (1) |
| 527 | 119 (264..496) | 64 | 15 | 31 (22), 30 (14), 39 (9), 45 (6), 19 (4), 37 (3), 36 (2), 23 (2), 40 (1), 56 (1) |
| 528 | 141 (267..534) | 80 | 26 | 39 (35), 36 (13), 45 (9), 30 (9), 19 (6), 40 (4), 37 (3), 31 (1) |
| 530 | 177 (273..520) | 107 | 22 | 39 (58), 40 (35), 19 (8), 36 (3), 45 (2), 69 (1) |
| 532 | 120 (275..455) | 77 | 26 | 36 (34), 40 (20), 45 (20), 19 (3) |
| 542 | 185 (293..557) | 119 | 27 | 40 (67), 36 (35), 45 (17) |
| 549 | 107 (323..545) | 55 | 23 | 39 (28), 64 (11), 40 (8), 45 (3), 69 (3), 31 (1), 30 (1) |
| 559 | 183 (354..612) | 131 | 24 | 69 (74), 45 (28), 39 (13), 64 (12), 40 (4) |
| 561 | 139 (363..513) | 126 | 9 | 23 (75), 56 (51) |
| 647 | 137 (840..1008) | 134 | 1 | 0 (134) |

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
| 38 | 275..319 | 45 | 0 | 45 |
| 41 | 279..313 | 35 | 0 | 35 |
| 46 | 300..340 | 41 | 0 | 41 |
| 50 | 325..364 | 40 | 0 | 40 |
| 53 | 341..371 | 31 | 0 | 31 |
| 54 | 341..375 | 35 | 0 | 35 |
| 57 | 347..380 | 34 | 0 | 34 |
| 58 | 350..389 | 40 | 0 | 40 |
| 61 | 375..413 | 39 | 0 | 39 |
| 66 | 400..462 | 63 | 0 | 63 |
| 67 | 403..437 | 35 | 0 | 35 |
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
| 119 | 725..762 | 38 | 0 | 38 |
| 120 | 750..787 | 38 | 0 | 38 |
| 121 | 775..811 | 37 | 0 | 37 |
| ... | 17 more | | | |

### Gaps and durations of candidate tracks
- tracks: 78; lifespan min/median/max: 9/39/1007; tracks with internal gaps: 21; total internal gaps: 445; longest internal gap: 51; tracks ending in coasting: 77 (trailing rows total 2809)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 974 | 33 | 7 | 25 | 0 | 491, 647 |
| 1 | 23..53 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 5 | 80..495 | 416 | 416 | 161 | 255 | 31 | 48 | 29 | 496, 503, 508, 511, 522 |
| 6 | 88..118 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 11 | 139..243 | 105 | 105 | 21 | 84 | 8 | 17 | 56 | 496, 503, 511 |
| 13 | 151..184 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 16 | 167..490 | 324 | 324 | 174 | 150 | 45 | 23 | 26 | 496, 503, 508, 511, 522 |
| 18 | 176..303 | 128 | 128 | 13 | 115 | 9 | 18 | 33 | 496, 503, 508, 511 |
| 19 | 188..435 | 248 | 248 | 55 | 193 | 21 | 51 | 34 | 503, 508, 514, 527, 528, 530, 532 |
| 22 | 200..238 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 23 | 204..543 | 340 | 340 | 288 | 52 | 14 | 5 | 29 | 514, 521, 522, 527, 561 |
| 26 | 217..251 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 28 | 225..262 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 30 | 234..619 | 386 | 386 | 237 | 149 | 31 | 33 | 28 | 514, 521, 527, 528, 549 |
| 31 | 240..542 | 303 | 303 | 166 | 137 | 30 | 21 | 57 | 521, 522, 527, 528, 549 |
| 32 | 243..309 | 67 | 67 | 25 | 42 | 7 | 7 | 29 | 503, 508, 511 |
| 33 | 250..287 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 36 | 269..484 | 216 | 216 | 87 | 129 | 38 | 14 | 29 | 527, 528, 530, 532, 542 |
| 37 | 269..367 | 99 | 99 | 7 | 92 | 6 | 13 | 59 | 522, 527, 528 |
| 38 | 275..319 | 45 | 45 | 0 | 45 | 0 | 0 | 45 | - |
| 39 | 275..641 | 367 | 367 | 196 | 171 | 41 | 46 | 29 | 514, 521, 522, 527, 528, 530, 549, 559 |
| 40 | 276..643 | 368 | 368 | 148 | 220 | 40 | 23 | 29 | 514, 527, 528, 530, 532, 542, 549, 559 |
| 41 | 279..313 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 42 | 282..321 | 40 | 40 | 2 | 38 | 1 | 3 | 35 | 508 |
| 45 | 298..630 | 333 | 333 | 121 | 212 | 53 | 47 | 29 | 514, 521, 527, 528, 530, 532, 542, 549, 559 |
| 46 | 300..340 | 41 | 41 | 0 | 41 | 0 | 0 | 41 | - |
| 47 | 301..371 | 71 | 71 | 16 | 55 | 10 | 9 | 30 | 496 |
| 50 | 325..364 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 53 | 341..371 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 54 | 341..375 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 56 | 346..472 | 127 | 127 | 57 | 70 | 12 | 17 | 28 | 496, 503, 521, 527, 561 |
| 57 | 347..380 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 58 | 350..389 | 40 | 40 | 0 | 40 | 0 | 0 | 40 | - |
| 59 | 371..528 | 158 | 158 | 66 | 92 | 17 | 29 | 29 | 496, 503, 522 |
| 61 | 375..413 | 39 | 39 | 0 | 39 | 0 | 0 | 39 | - |
| 64 | 392..515 | 124 | 124 | 23 | 101 | 11 | 26 | 41 | 549, 559 |
| 66 | 400..462 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 67 | 403..437 | 35 | 35 | 0 | 35 | 0 | 0 | 35 | - |
| 69 | 410..632 | 223 | 223 | 81 | 142 | 13 | 45 | 29 | 514, 521, 530, 549, 559 |
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
- reference objects: 17; candidate ids: 35; matched pairs: 2918; unmatched reference entries: 624; unmatched candidate entries: 3029
- identity switches: 177; fragmentation (coverage interruptions): 284; orphan candidate ids (never on a reference object): 14

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f178: ref 508: 16 -> 18 at (1889.5, 3015.5), 5 frames after previous cover
- f179: ref 503: 11 -> 16 at (1846, 3017), 13 frames after previous cover
- f184: ref 511: 16 -> 11 at (1545.5, 3020), 1 frames after previous cover
- f186: ref 496: 5 -> 11 at (1475, 3014), 1 frames after previous cover
- f186: ref 511: 11 -> 16 at (1554.5, 3019), 1 frames after previous cover
- f188: ref 496: 11 -> 16 at (1462, 3014), 1 frames after previous cover
- f188: ref 508: 18 -> 19 at (1824.5, 3016), 7 frames after previous cover
- f189: ref 496: 16 -> 5 at (1443, 3011), 1 frames after previous cover
- f192: ref 496: 5 -> 16 at (1417, 3009.5), 1 frames after previous cover
- f192: ref 511: 16 -> 5 at (1515, 3017), 5 frames after previous cover
- f200: ref 503: 16 -> 18 at (1694.5, 3009.5), 21 frames after previous cover
- f213: ref 503: 18 -> 19 at (1595, 3007.5), 5 frames after previous cover
- f218: ref 511: 5 -> 18 at (1382, 2999.5), 2 frames after previous cover
- f222: ref 511: 18 -> 5 at (1358, 2995.5), 2 frames after previous cover
- f235: ref 511: 5 -> 18 at (1243, 2987.5), 1 frames after previous cover
- f237: ref 503: 19 -> 5 at (1286, 2990.5), 2 frames after previous cover
- f238: ref 511: 18 -> 5 at (1252, 2988), 2 frames after previous cover
- f243: ref 511: 5 -> 32 at (1219.5, 2988), 4 frames after previous cover
- f246: ref 503: 5 -> 32 at (1200, 2987), 9 frames after previous cover
- f251: ref 503: 32 -> 18 at (1097.5, 2988), 1 frames after previous cover
- f255: ref 503: 18 -> 32 at (1072.5, 2988), 2 frames after previous cover
- f257: ref 508: 19 -> 32 at (1132, 2984), 11 frames after previous cover
- f263: ref 508: 32 -> 5 at (1094, 2985.5), 4 frames after previous cover
- f264: ref 503: 32 -> 16 at (953.5, 2988), 8 frames after previous cover
- f264: ref 508: 5 -> 32 at (1056.5, 2986), 1 frames after previous cover
- f267: ref 508: 32 -> 5 at (1069, 2985), 1 frames after previous cover
- f268: ref 508: 5 -> 32 at (1031.5, 2986), 1 frames after previous cover
- f270: ref 496: 16 -> 18 at (786.5, 3257), 8 frames after previous cover
- f271: ref 508: 32 -> 5 at (1042.5, 2986), 2 frames after previous cover
- f274: ref 511: 32 -> 16 at (890.5, 2986.5), 3 frames after previous cover
- f274: ref 528: 37 -> 36 at (2147, 2974.5), 2 frames after previous cover
- f277: ref 527: 36 -> 37 at (1944.5, 2980), 8 frames after previous cover
- f279: ref 503: 16 -> 32 at (813.5, 3004.5), 2 frames after previous cover
- f282: ref 528: 36 -> 40 at (2024, 2972.5), 8 frames after previous cover
- f283: ref 503: 32 -> 16 at (808.5, 3164.5), 3 frames after previous cover
- f285: ref 508: 5 -> 42 at (871.5, 3003.5), 2 frames after previous cover
- f285: ref 527: 37 -> 40 at (1945, 2976), 8 frames after previous cover
- f289: ref 527: 40 -> 37 at (1863, 2975), 4 frames after previous cover
- f293: ref 532: 36 -> 40 at (2049.5, 2969.5), 3 frames after previous cover
- f294: ref 528: 40 -> 37 at (1927.5, 2967.5), 6 frames after previous cover
- f298: ref 514: 23 -> 19 at (1378.5, 2947.5), 1 frames after previous cover
- f298: ref 528: 37 -> 45 at (1894, 2966.5), 4 frames after previous cover
- f299: ref 514: 19 -> 23 at (1370, 2949.5), 1 frames after previous cover
- f301: ref 496: 18 -> 47 at (929, 2985.5), 31 frames after previous cover
- f305: ref 527: 37 -> 45 at (1784, 2967.5), 13 frames after previous cover
- f305: ref 528: 45 -> 36 at (1839.5, 2968), 2 frames after previous cover
- f306: ref 527: 45 -> 36 at (1797.5, 2967), 1 frames after previous cover
- f307: ref 527: 36 -> 45 at (1766, 2967.5), 1 frames after previous cover
- f308: ref 522: 31 -> 37 at (1554.5, 2962), 1 frames after previous cover
- f309: ref 522: 37 -> 31 at (1545.5, 2963), 1 frames after previous cover
- f314: ref 542: 36 -> 40 at (1881.5, 2963), 11 frames after previous cover
- f319: ref 542: 40 -> 36 at (1814, 2962.5), 1 frames after previous cover
- f320: ref 528: 36 -> 45 at (1720, 2963.5), 2 frames after previous cover
- f327: ref 527: 45 -> 19 at (1608.5, 2960.5), 12 frames after previous cover
- f327: ref 532: 40 -> 45 at (1662.5, 2962), 15 frames after previous cover
- f332: ref 496: 47 -> 5 at (688, 2974.5), 1 frames after previous cover
- f333: ref 496: 5 -> 47 at (654, 2975), 1 frames after previous cover
- f340: ref 528: 45 -> 19 at (1494, 2958), 15 frames after previous cover
- f342: ref 496: 47 -> 16 at (459, 2963), 1 frames after previous cover
- f348: ref 528: 19 -> 39 at (1304, 2951.5), 8 frames after previous cover
- ... 117 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 491 | 856 (0..896) | 840 | 4 | 0 (840) |
| 496 | 241 (78..446) | 210 | 22 | 5 (106), 16 (83), 47 (16), 11 (2), 18 (1), 56 (1), 59 (1) |
| 503 | 229 (137..499) | 166 | 30 | 16 (72), 59 (47), 11 (17), 5 (10), 32 (8), 18 (5), 19 (5), 56 (2) |
| 508 | 81 (165..286) | 50 | 10 | 19 (28), 5 (9), 32 (6), 16 (3), 18 (2), 42 (2) |
| 511 | 71 (183..279) | 56 | 10 | 5 (33), 32 (11), 16 (5), 18 (5), 11 (2) |
| 514 | 296 (202..614) | 285 | 7 | 23 (207), 30 (55), 39 (10), 40 (9), 69 (2), 19 (1), 45 (1) |
| 521 | 244 (232..601) | 231 | 9 | 30 (158), 45 (35), 31 (28), 39 (4), 23 (3), 56 (2), 69 (1) |
| 522 | 216 (238..498) | 187 | 19 | 31 (114), 39 (39), 59 (18), 16 (11), 5 (3), 37 (1), 23 (1) |
| 527 | 119 (264..496) | 64 | 15 | 31 (22), 30 (14), 39 (9), 45 (6), 19 (4), 37 (3), 36 (2), 23 (2), 40 (1), 56 (1) |
| 528 | 141 (267..534) | 80 | 26 | 39 (35), 36 (13), 45 (9), 30 (9), 19 (6), 40 (4), 37 (3), 31 (1) |
| 530 | 177 (273..520) | 107 | 22 | 39 (58), 40 (35), 19 (8), 36 (3), 45 (2), 69 (1) |
| 532 | 120 (275..455) | 77 | 26 | 36 (34), 40 (20), 45 (20), 19 (3) |
| 542 | 185 (293..557) | 119 | 27 | 40 (67), 36 (35), 45 (17) |
| 549 | 107 (323..545) | 55 | 23 | 39 (28), 64 (11), 40 (8), 45 (3), 69 (3), 31 (1), 30 (1) |
| 559 | 183 (354..612) | 131 | 24 | 69 (74), 45 (28), 39 (13), 64 (12), 40 (4) |
| 561 | 139 (363..513) | 126 | 9 | 23 (75), 56 (51) |
| 647 | 137 (840..1008) | 134 | 1 | 0 (134) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 1 | 23..53 | 31 | 0 | 31 |
| 6 | 88..118 | 31 | 0 | 31 |
| 13 | 151..184 | 34 | 0 | 34 |
| 53 | 341..371 | 31 | 0 | 31 |
| 57 | 347..380 | 34 | 0 | 34 |
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
- tracks: 35; lifespan min/median/max: 31/99/1007; tracks with internal gaps: 21; total internal gaps: 445; longest internal gap: 51; tracks ending in coasting: 34 (trailing rows total 1185)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2..1008 | 1007 | 1007 | 974 | 33 | 7 | 25 | 0 | 491, 647 |
| 1 | 23..53 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 5 | 80..495 | 416 | 416 | 161 | 255 | 31 | 48 | 29 | 496, 503, 508, 511, 522 |
| 6 | 88..118 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 11 | 139..243 | 105 | 105 | 21 | 84 | 8 | 17 | 56 | 496, 503, 511 |
| 13 | 151..184 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 16 | 167..490 | 324 | 324 | 174 | 150 | 45 | 23 | 26 | 496, 503, 508, 511, 522 |
| 18 | 176..303 | 128 | 128 | 13 | 115 | 9 | 18 | 33 | 496, 503, 508, 511 |
| 19 | 188..435 | 248 | 248 | 55 | 193 | 21 | 51 | 34 | 503, 508, 514, 527, 528, 530, 532 |
| 23 | 204..543 | 340 | 340 | 288 | 52 | 14 | 5 | 29 | 514, 521, 522, 527, 561 |
| 30 | 234..619 | 386 | 386 | 237 | 149 | 31 | 33 | 28 | 514, 521, 527, 528, 549 |
| 31 | 240..542 | 303 | 303 | 166 | 137 | 30 | 21 | 57 | 521, 522, 527, 528, 549 |
| 32 | 243..309 | 67 | 67 | 25 | 42 | 7 | 7 | 29 | 503, 508, 511 |
| 36 | 269..484 | 216 | 216 | 87 | 129 | 38 | 14 | 29 | 527, 528, 530, 532, 542 |
| 37 | 269..367 | 99 | 99 | 7 | 92 | 6 | 13 | 59 | 522, 527, 528 |
| 39 | 275..641 | 367 | 367 | 196 | 171 | 41 | 46 | 29 | 514, 521, 522, 527, 528, 530, 549, 559 |
| 40 | 276..643 | 368 | 368 | 148 | 220 | 40 | 23 | 29 | 514, 527, 528, 530, 532, 542, 549, 559 |
| 42 | 282..321 | 40 | 40 | 2 | 38 | 1 | 3 | 35 | 508 |
| 45 | 298..630 | 333 | 333 | 121 | 212 | 53 | 47 | 29 | 514, 521, 527, 528, 530, 532, 542, 549, 559 |
| 47 | 301..371 | 71 | 71 | 16 | 55 | 10 | 9 | 30 | 496 |
| 53 | 341..371 | 31 | 31 | 0 | 31 | 0 | 0 | 31 | - |
| 56 | 346..472 | 127 | 127 | 57 | 70 | 12 | 17 | 28 | 496, 503, 521, 527, 561 |
| 57 | 347..380 | 34 | 34 | 0 | 34 | 0 | 0 | 34 | - |
| 59 | 371..528 | 158 | 158 | 66 | 92 | 17 | 29 | 29 | 496, 503, 522 |
| 64 | 392..515 | 124 | 124 | 23 | 101 | 11 | 26 | 41 | 549, 559 |
| 69 | 410..632 | 223 | 223 | 81 | 142 | 13 | 45 | 29 | 514, 521, 530, 549, 559 |
| 89 | 530..566 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 91 | 530..575 | 46 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 102 | 593..625 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
| 111 | 657..694 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 117 | 721..757 | 37 | 37 | 0 | 37 | 0 | 0 | 37 | - |
| 123 | 786..823 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 131 | 848..885 | 38 | 38 | 0 | 38 | 0 | 0 | 38 | - |
| 141 | 913..948 | 36 | 36 | 0 | 36 | 0 | 0 | 36 | - |
| 150 | 976..1008 | 33 | 33 | 0 | 33 | 0 | 0 | 33 | - |
