# Tracker evaluation: claim = PARITY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=unknown config={}
Reference: predictor=cloud claim=parity curation=n/a

## Provenance
- candidate: config_hash=44136fa355b3 git=none model=unknown
  - tracker_csv: results/flock/baseline_tracks.csv sha256=903c5ff6f9e4b42b
  - tracker/ hash=7b65976a888fbd3c coasting_known=False
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: 6-column format: coasting rows unknown, every row counted as an observation
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- reference: config_hash=44136fa355b3 git=none model=cloud-tracke
  - cloud_tracks_csv: data/20251012_164031_1DAC_cloud_reference_tracks.csv sha256=d9840f855f6cc35c
  - note: stored output of the cloud tracking pipeline for the same frame window; a reference for parity only
  - note: confidence 1.0 on every row: the export carries no score
  - note: clip = frames 4001..5009 of the original recording 20251012_164031_1DAC (1009 frames, renumbered 0..1008; 2160x3840 portrait, 25 fps)
- metrics engine: TrackEval 12c8791b303e (https://github.com/JonathonLuiten/TrackEval); np.float and np.int restored as float/int before import; sources unmodified
- similarity: s = max(0, 1 - d / T), T = match_px / (1 - threshold), threshold 0.5; T per px: {'4.0': 8.0, '6.0': 12.0, '8.0': 16.0, '12.0': 24.0}
- candidate is in the 6-column baseline format: coasting rows are indistinguishable, so only the 'updates' view (every row as written) is scored; matched-rows-only needs the 10-column format
- ignore region 'burnt-in timestamp overlay, top-left': entries with center inside it are dropped on both sides before scoring

## Metrics (center-distance matching)
| view | region | px | ref | cand | HOTA | DetA | AssA | LocA px | HOTA@a.5 | MOTA | MOTP px | IDSW | Frag | IDF1 | IDP | IDR | Re | Pr | TP | FN | FP | MT | PT | ML |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| updates | none | 4 | 3542 | 7571 | 0.351 | 0.339 | 0.363 | 0.14 | 0.353 | -0.583 | 0.13 | 164 | 441.0 | 0.327 | 0.240 | 0.513 | 0.800 | 0.374 | 2835 | 707 | 4736 | 7 | 10 | 0 |
| updates | none | 6 | 3542 | 7571 | 0.355 | 0.346 | 0.364 | 0.24 | 0.355 | -0.562 | 0.20 | 170 | 451.0 | 0.330 | 0.242 | 0.517 | 0.812 | 0.380 | 2875 | 667 | 4696 | 7 | 10 | 0 |
| updates | none | 8 | 3542 | 7571 | 0.357 | 0.353 | 0.362 | 0.37 | 0.357 | -0.540 | 0.31 | 177 | 462.0 | 0.332 | 0.244 | 0.521 | 0.824 | 0.385 | 2918 | 624 | 4653 | 7 | 10 | 0 |
| updates | none | 12 | 3542 | 7571 | 0.362 | 0.366 | 0.359 | 0.68 | 0.363 | -0.496 | 0.61 | 189 | 453.0 | 0.337 | 0.248 | 0.529 | 0.847 | 0.396 | 3001 | 541 | 4570 | 8 | 9 | 0 |
| updates | ignore | 4 | 3542 | 5947 | 0.391 | 0.421 | 0.363 | 0.14 | 0.394 | -0.125 | 0.13 | 164 | 441.0 | 0.383 | 0.305 | 0.513 | 0.800 | 0.477 | 2835 | 707 | 3112 | 7 | 10 | 0 |
| updates | ignore | 6 | 3542 | 5947 | 0.396 | 0.431 | 0.364 | 0.24 | 0.396 | -0.104 | 0.20 | 170 | 451.0 | 0.386 | 0.308 | 0.517 | 0.812 | 0.483 | 2875 | 667 | 3072 | 7 | 10 | 0 |
| updates | ignore | 8 | 3542 | 5947 | 0.399 | 0.440 | 0.362 | 0.37 | 0.399 | -0.081 | 0.31 | 177 | 462.0 | 0.389 | 0.310 | 0.521 | 0.824 | 0.491 | 2918 | 624 | 3029 | 7 | 10 | 0 |
| updates | ignore | 12 | 3542 | 5947 | 0.405 | 0.457 | 0.359 | 0.68 | 0.406 | -0.038 | 0.61 | 189 | 453.0 | 0.395 | 0.315 | 0.529 | 0.847 | 0.505 | 3001 | 541 | 2946 | 8 | 9 | 0 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

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
