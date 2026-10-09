# Tracker evaluation: claim = ACCURACY

Candidate: predictor=kit dataset=flock video=20251012_164031_1DAC detections=real config={"euclidean_matching_threshold": 250.0, "max_age": 60, "tentative_threshold": 5}
Reference: predictor=gt claim=accuracy curation=independent manual annotation (not traced from the cloud tracker output)

## Provenance
- candidate: config_hash=0f330bc195fc git=none model=53d7ab0c6f99
  - tracker_csv: /Users/diegogarciagonzalez/tracker-kit-Eval/outputs/runs/flock/real_maxage60_tent5/tracks.csv sha256=a74ed8196da83f50
  - detections_csv: data/20251012_164031_1DAC_detections.csv sha256=53d7ab0c6f992c27
  - video: data/20251012_164031_1DAC.mp4 sha256=fbc117d9da3fce2e
  - tracker/ hash=7b65976a888fbd3c coasting_known=True
  - note: matched rows carry confidence 1.0: the kit's detections have no confidence
  - note: coasting rows are track updates only (confidence 0.0), never observations
  - note: real_maxage60_tent5
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
| observations | none | 4 | 10142 | 3961 | 0.250 | 0.099 | 0.635 | 0.98 | 0.268 | -0.132 | 1.01 | 91 | 252.0 | 0.162 | 0.288 | 0.112 | 0.134 | 0.342 | 1355 | 8787 | 2606 | 1 | 0 | 24 |
| observations | none | 6 | 10142 | 3961 | 0.263 | 0.112 | 0.624 | 1.37 | 0.275 | -0.108 | 1.38 | 118 | 325.0 | 0.173 | 0.307 | 0.120 | 0.147 | 0.377 | 1494 | 8648 | 2467 | 1 | 1 | 23 |
| observations | none | 8 | 10142 | 3961 | 0.272 | 0.123 | 0.614 | 1.83 | 0.278 | -0.089 | 1.74 | 138 | 382.0 | 0.178 | 0.318 | 0.124 | 0.158 | 0.404 | 1599 | 8543 | 2362 | 1 | 1 | 23 |
| observations | none | 12 | 10142 | 3961 | 0.286 | 0.136 | 0.611 | 2.51 | 0.286 | -0.047 | 2.81 | 154 | 431.0 | 0.195 | 0.347 | 0.136 | 0.180 | 0.460 | 1821 | 8321 | 2140 | 1 | 2 | 22 |
| observations | ignore | 4 | 10142 | 3695 | 0.253 | 0.101 | 0.635 | 0.98 | 0.271 | -0.106 | 1.01 | 91 | 252.0 | 0.165 | 0.308 | 0.112 | 0.134 | 0.367 | 1355 | 8787 | 2340 | 1 | 0 | 24 |
| observations | ignore | 6 | 10142 | 3695 | 0.265 | 0.115 | 0.624 | 1.37 | 0.278 | -0.081 | 1.38 | 118 | 325.0 | 0.176 | 0.329 | 0.120 | 0.147 | 0.404 | 1494 | 8648 | 2201 | 1 | 1 | 23 |
| observations | ignore | 8 | 10142 | 3695 | 0.275 | 0.126 | 0.614 | 1.83 | 0.281 | -0.063 | 1.74 | 138 | 382.0 | 0.182 | 0.340 | 0.124 | 0.158 | 0.433 | 1599 | 8543 | 2096 | 1 | 1 | 23 |
| observations | ignore | 12 | 10142 | 3695 | 0.289 | 0.139 | 0.611 | 2.51 | 0.289 | -0.020 | 2.81 | 154 | 431.0 | 0.199 | 0.372 | 0.136 | 0.180 | 0.493 | 1821 | 8321 | 1874 | 1 | 2 | 22 |
| updates | none | 4 | 10142 | 9013 | 0.210 | 0.078 | 0.580 | 1.13 | 0.224 | -0.617 | 1.11 | 139 | 307.0 | 0.120 | 0.128 | 0.113 | 0.143 | 0.161 | 1447 | 8695 | 7566 | 1 | 0 | 24 |
| updates | none | 6 | 10142 | 9013 | 0.221 | 0.092 | 0.553 | 1.68 | 0.231 | -0.577 | 1.62 | 182 | 387.0 | 0.129 | 0.137 | 0.122 | 0.165 | 0.186 | 1672 | 8470 | 7341 | 1 | 1 | 23 |
| updates | none | 8 | 10142 | 9013 | 0.230 | 0.104 | 0.532 | 2.25 | 0.234 | -0.541 | 2.18 | 206 | 440.0 | 0.135 | 0.143 | 0.127 | 0.184 | 0.207 | 1864 | 8278 | 7149 | 1 | 2 | 22 |
| updates | none | 12 | 10142 | 9013 | 0.242 | 0.119 | 0.511 | 3.16 | 0.242 | -0.472 | 3.54 | 224 | 474.0 | 0.150 | 0.159 | 0.142 | 0.220 | 0.247 | 2227 | 7915 | 6786 | 1 | 4 | 20 |
| updates | ignore | 4 | 10142 | 6298 | 0.228 | 0.092 | 0.580 | 1.13 | 0.244 | -0.349 | 1.11 | 139 | 307.0 | 0.140 | 0.183 | 0.113 | 0.143 | 0.230 | 1447 | 8695 | 4851 | 1 | 0 | 24 |
| updates | ignore | 6 | 10142 | 6298 | 0.241 | 0.109 | 0.553 | 1.68 | 0.252 | -0.309 | 1.62 | 182 | 387.0 | 0.151 | 0.197 | 0.122 | 0.165 | 0.265 | 1672 | 8470 | 4626 | 1 | 1 | 23 |
| updates | ignore | 8 | 10142 | 6298 | 0.250 | 0.123 | 0.532 | 2.25 | 0.255 | -0.274 | 2.18 | 206 | 440.0 | 0.157 | 0.205 | 0.127 | 0.184 | 0.296 | 1864 | 8278 | 4434 | 1 | 2 | 22 |
| updates | ignore | 12 | 10142 | 6298 | 0.264 | 0.142 | 0.511 | 3.16 | 0.264 | -0.204 | 3.54 | 224 | 474.0 | 0.175 | 0.228 | 0.142 | 0.220 | 0.354 | 2227 | 7915 | 4071 | 1 | 4 | 20 |

HOTA/DetA/AssA are TrackEval's mean over 19 alphas (distances 0.05 T .. 0.95 T); HOTA@a.5 is the value at the configured px. LocA px and MOTP px are mean center distance over matches. Matched-rows-only (`observations`) excludes coasting rows; `updates` scores every row as written. CLEAR's Frag counts every resumption of tracking after an interruption, including frames where the reference object itself is absent, so a reference with gaps gives Frag > 0 even to a perfect candidate (the flock GT has 111 such gaps), while an interruption that falls on frames with no candidate entry at all is not counted by CLEAR; the diagnostics' fragmentation below counts only interruptions within the object's labelled frames, whatever the rest of the frame holds.

## Diagnostics: view=observations, region=none, match 8 px
- reference objects: 25; candidate ids: 68; matched pairs: 1599; unmatched reference entries: 8543; unmatched candidate entries: 2362
- identity switches: 138; fragmentation (coverage interruptions): 382; orphan candidate ids (never on a reference object): 52

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f176: ref 79132: 23 -> 25 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 23 -> 25 at (1843, 3015), 10 frames after previous cover
- f181: ref 79134: 25 -> 23 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 5 -> 23 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 23 -> 5 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78971: 23 -> 5 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 79134: 23 -> 25 at (1753.5, 3017.5), 11 frames after previous cover
- f196: ref 79139: 25 -> 32 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 25 -> 32 at (1718, 3008.5), 8 frames after previous cover
- f207: ref 79134: 25 -> 32 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 23 -> 25 at (1625.5, 3010), 36 frames after previous cover
- f212: ref 79128: 25 -> 32 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 23 -> 25 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 25 -> 32 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 23 -> 25 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 5 -> 23 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 23 -> 25 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 25 -> 32 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 23 -> 32 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 25 -> 32 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 25 -> 32 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 25 -> 23 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 32 -> 25 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 32 -> 25 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 32 -> 25 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 32 -> 25 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 32 -> 25 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 25 -> 32 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 25 -> 32 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 25 -> 32 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 23 -> 25 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 25 -> 32 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 23 -> 25 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 25 -> 23 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78971: 5 -> 25 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 25 -> 32 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 32 -> 23 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 25 -> 23 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 25 -> 5 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 25 -> 23 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 25 -> 45 at (1179, 2985.5), 5 frames after previous cover
- f246: ref 79097: 23 -> 45 at (1199.5, 2985), 7 frames after previous cover
- f255: ref 79037: 25 -> 45 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 23 -> 32 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 23 -> 45 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 23 -> 32 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 45 -> 23 at (1090, 2983.5), 4 frames after previous cover
- f274: ref 78899: 45 -> 23 at (996, 2989.5), 5 frames after previous cover
- f282: ref 78897: 45 -> 23 at (913, 2990), 22 frames after previous cover
- f287: ref 78896: 5 -> 58 at (775, 2987), 14 frames after previous cover
- f304: ref 79108: 32 -> 68 at (954, 2978), 44 frames after previous cover
- f317: ref 79134: 32 -> 68 at (990.5, 2965.5), 74 frames after previous cover
- f327: ref 79132: 32 -> 68 at (895, 2966.5), 88 frames after previous cover
- f331: ref 79102: 23 -> 68 at (723.5, 2979.5), 82 frames after previous cover
- f333: ref 79097: 23 -> 68 at (654.5, 2972.5), 33 frames after previous cover
- f334: ref 78899: 23 -> 68 at (619, 2977.5), 39 frames after previous cover
- f338: ref 79105: 32 -> 23 at (719.5, 2978), 103 frames after previous cover
- f344: ref 79097: 68 -> 23 at (590, 2968.5), 2 frames after previous cover
- f345: ref 78899: 68 -> 23 at (554.5, 2973.5), 5 frames after previous cover
- f351: ref 78899: 23 -> 77 at (519, 2967.5), 6 frames after previous cover
- ... 78 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 974 | 8 | 0 (974) |
| 78896 | 350 (76..429) | 10 | 8 | 5 (7), 80 (2), 58 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 5 (82), 80 (8), 23 (2) |
| 78971 | 352 (84..439) | 18 | 12 | 80 (7), 5 (5), 23 (5), 25 (1) |
| 79045 | 355 (84..443) | 16 | 11 | 23 (11), 80 (3), 45 (2) |
| 79037 | 355 (86..445) | 16 | 15 | 23 (6), 5 (3), 45 (3), 25 (2), 80 (2) |
| 78897 | 345 (89..450) | 27 | 21 | 23 (15), 80 (8), 5 (2), 45 (1), 79 (1) |
| 78899 | 365 (91..455) | 50 | 40 | 23 (23), 45 (12), 80 (5), 68 (3), 5 (3), 25 (2), 77 (1), 79 (1) |
| 79097 | 366 (94..461) | 66 | 43 | 23 (45), 25 (5), 45 (5), 68 (4), 5 (4), 80 (3) |
| 79098 | 360 (97..467) | 24 | 19 | 23 (11), 5 (10), 25 (1), 44 (1), 80 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 5 (15), 80 (4), 23 (2), 68 (1), 79 (1), 44 (1) |
| 79103 | 380 (99..481) | 15 | 10 | 23 (5), 80 (5), 25 (2), 5 (2), 44 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 25 (2), 32 (1), 23 (1), 79 (1), 44 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 23 (3), 32 (3), 44 (3), 25 (2), 68 (2), 79 (1), 80 (1) |
| 79110 | 388 (106..497) | 14 | 7 | 80 (7), 32 (4), 25 (2), 44 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 80 (5), 23 (2), 32 (2), 25 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 32 (4), 25 (2), 79 (1), 35 (1), 55 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 55 (37), 35 (1) |
| 79122 | 404 (118..532) | 19 | 10 | 79 (9), 55 (9), 35 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 35 (56), 25 (4), 32 (2), 23 (1), 68 (1) |
| 79128 | 402 (124..527) | 13 | 10 | 32 (5), 35 (4), 25 (2), 23 (1), 79 (1) |
| 79134 | 407 (127..533) | 15 | 13 | 32 (4), 25 (3), 55 (3), 35 (2), 23 (1), 68 (1), 79 (1) |
| 79135 | 409 (129..542) | 40 | 32 | 32 (10), 43 (10), 25 (5), 35 (5), 89 (4), 55 (3), 23 (2), 79 (1) |
| 79139 | 406 (132..537) | 21 | 14 | 32 (9), 55 (7), 43 (2), 25 (1), 35 (1), 79 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 89 (1), 43 (1), 55 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 34 | 202..209 | 8 | 0 | 6 |
| 39 | 219..222 | 4 | 0 | 3 |
| 41 | 227..233 | 7 | 0 | 7 |
| 46 | 252..258 | 7 | 0 | 7 |
| 49 | 271..614 | 344 | 0 | 232 |
| 51 | 277..290 | 14 | 0 | 13 |
| 56 | 281..284 | 4 | 0 | 3 |
| 60 | 286..568 | 283 | 0 | 181 |
| 63 | 292..534 | 243 | 0 | 128 |
| 65 | 300..606 | 307 | 0 | 205 |
| 66 | 302..311 | 10 | 0 | 8 |
| 69 | 327..335 | 9 | 0 | 9 |
| 71 | 338..338 | 1 | 0 | 1 |
| 73 | 343..346 | 4 | 0 | 3 |
| 78 | 352..360 | 9 | 0 | 8 |
| 82 | 377..384 | 8 | 0 | 8 |
| 85 | 405..408 | 4 | 0 | 3 |
| 87 | 412..607 | 196 | 0 | 132 |
| 88 | 427..433 | 7 | 0 | 7 |
| 91 | 453..456 | 4 | 0 | 3 |
| 93 | 467..470 | 4 | 0 | 3 |
| 98 | 477..483 | 7 | 0 | 7 |
| 103 | 502..508 | 7 | 0 | 7 |
| 105 | 529..532 | 4 | 0 | 3 |
| 106 | 531..535 | 5 | 0 | 4 |
| 107 | 532..537 | 6 | 0 | 3 |
| 110 | 552..561 | 10 | 0 | 8 |
| 116 | 591..594 | 4 | 0 | 3 |
| 117 | 595..596 | 2 | 0 | 2 |
| 120 | 602..610 | 9 | 0 | 8 |
| 122 | 627..634 | 8 | 0 | 8 |
| 124 | 653..656 | 4 | 0 | 3 |
| 126 | 659..665 | 7 | 0 | 7 |
| 128 | 677..685 | 9 | 0 | 9 |
| 129 | 703..708 | 6 | 0 | 5 |
| 130 | 715..718 | 4 | 0 | 3 |
| 134 | 727..733 | 7 | 0 | 7 |
| 136 | 752..758 | 7 | 0 | 7 |
| 137 | 777..782 | 6 | 0 | 6 |
| 144 | 802..811 | 10 | 0 | 8 |
| ... | 12 more | | | |

### Gaps and durations of candidate tracks
- tracks: 68; lifespan min/median/max: 1/8/1005; tracks with internal gaps: 16; total internal gaps: 141; longest internal gap: 194; tracks ending in coasting: 59 (trailing rows total 1238)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1008 | 1005 | 979 | 974 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 82..453 | 372 | 318 | 133 | 185 | 42 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103 |
| 23 | 169..461 | 293 | 165 | 136 | 29 | 15 | 4 | 4 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79128, 79132, 79134, 79135 |
| 25 | 176..274 | 99 | 49 | 37 | 12 | 7 | 2 | 3 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 32 | 196..412 | 217 | 77 | 44 | 33 | 6 | 2 | 26 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 34 | 202..209 | 8 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 35 | 206..514 | 309 | 297 | 71 | 226 | 8 | 194 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 39 | 219..222 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 41 | 227..233 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 43 | 236..551 | 316 | 258 | 13 | 245 | 5 | 163 | 12 | 79135, 79136, 79139 |
| 44 | 242..464 | 223 | 161 | 8 | 153 | 2 | 148 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 45 | 245..280 | 36 | 29 | 23 | 6 | 2 | 1 | 4 | 78897, 78899, 79037, 79045, 79097 |
| 46 | 252..258 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 49 | 271..614 | 344 | 232 | 0 | 232 | 0 | 0 | 232 | - |
| 51 | 277..290 | 14 | 13 | 0 | 13 | 0 | 0 | 13 | - |
| 55 | 280..592 | 313 | 249 | 61 | 188 | 8 | 137 | 31 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 56 | 281..284 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 58 | 284..292 | 9 | 5 | 1 | 4 | 1 | 3 | 1 | 78896 |
| 60 | 286..568 | 283 | 181 | 0 | 181 | 0 | 0 | 181 | - |
| 63 | 292..534 | 243 | 128 | 0 | 128 | 0 | 0 | 128 | - |
| 65 | 300..606 | 307 | 205 | 0 | 205 | 0 | 0 | 205 | - |
| 66 | 302..311 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 68 | 303..342 | 40 | 26 | 12 | 14 | 6 | 5 | 0 | 78899, 79097, 79102, 79108, 79132, 79134 |
| 69 | 327..335 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 71 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 73 | 343..346 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 77 | 349..351 | 3 | 3 | 1 | 2 | 1 | 2 | 0 | 78899 |
| 78 | 352..360 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 79 | 366..443 | 78 | 63 | 19 | 44 | 10 | 17 | 0 | 78897, 78899, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 80 | 373..499 | 127 | 98 | 61 | 37 | 19 | 5 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 82 | 377..384 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 85 | 405..408 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 87 | 412..607 | 196 | 132 | 0 | 132 | 0 | 0 | 132 | - |
| 88 | 427..433 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 89 | 434..486 | 53 | 27 | 5 | 22 | 5 | 10 | 0 | 79135, 79136 |
| 91 | 453..456 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 93 | 467..470 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 98 | 477..483 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 103 | 502..508 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 105 | 529..532 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 106 | 531..535 | 5 | 4 | 0 | 4 | 0 | 0 | 4 | - |
| 107 | 532..537 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 110 | 552..561 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 116 | 591..594 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 117 | 595..596 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 120 | 602..610 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 122 | 627..634 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 124 | 653..656 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 126 | 659..665 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 128 | 677..685 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 129 | 703..708 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 130 | 715..718 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 134 | 727..733 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 136 | 752..758 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 137 | 777..782 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 144 | 802..811 | 10 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 146 | 827..834 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 147 | 839..842 | 4 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 152 | 852..860 | 9 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 155 | 877..885 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 156 | 901..906 | 6 | 6 | 0 | 6 | 0 | 0 | 6 | - |
| 157 | 903..911 | 9 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 165 | 927..935 | 9 | 9 | 0 | 9 | 0 | 0 | 9 | - |
| 166 | 933..940 | 8 | 8 | 0 | 8 | 0 | 0 | 8 | - |
| 167 | 952..957 | 6 | 5 | 0 | 5 | 0 | 0 | 5 | - |
| 169 | 963..965 | 3 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 171 | 977..983 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |
| 175 | 1002..1008 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |

## Diagnostics: view=observations, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 1599; unmatched reference entries: 8543; unmatched candidate entries: 2096
- identity switches: 138; fragmentation (coverage interruptions): 382; orphan candidate ids (never on a reference object): 9

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f176: ref 79132: 23 -> 25 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 23 -> 25 at (1843, 3015), 10 frames after previous cover
- f181: ref 79134: 25 -> 23 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 5 -> 23 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 23 -> 5 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78971: 23 -> 5 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 79134: 23 -> 25 at (1753.5, 3017.5), 11 frames after previous cover
- f196: ref 79139: 25 -> 32 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 25 -> 32 at (1718, 3008.5), 8 frames after previous cover
- f207: ref 79134: 25 -> 32 at (1655.5, 3014), 15 frames after previous cover
- f208: ref 79128: 23 -> 25 at (1625.5, 3010), 36 frames after previous cover
- f212: ref 79128: 25 -> 32 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 23 -> 25 at (1509.5, 3005), 36 frames after previous cover
- f214: ref 79132: 25 -> 32 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 23 -> 25 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 5 -> 23 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 23 -> 25 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 25 -> 32 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 23 -> 32 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 25 -> 32 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 25 -> 32 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 25 -> 23 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 32 -> 25 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 32 -> 25 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 32 -> 25 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 32 -> 25 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 32 -> 25 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 25 -> 32 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 25 -> 32 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 25 -> 32 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 23 -> 25 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 25 -> 32 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 23 -> 25 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 25 -> 23 at (1285.5, 2989.5), 7 frames after previous cover
- f239: ref 78971: 5 -> 25 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 25 -> 32 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 32 -> 23 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 25 -> 23 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 25 -> 5 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 25 -> 23 at (1359, 2995.5), 18 frames after previous cover
- f245: ref 78899: 25 -> 45 at (1179, 2985.5), 5 frames after previous cover
- f246: ref 79097: 23 -> 45 at (1199.5, 2985), 7 frames after previous cover
- f255: ref 79037: 25 -> 45 at (1069.5, 2987.5), 14 frames after previous cover
- f259: ref 79111: 23 -> 32 at (1256.5, 2986), 17 frames after previous cover
- f260: ref 78897: 23 -> 45 at (1057.5, 2987.5), 34 frames after previous cover
- f260: ref 79108: 23 -> 32 at (1226, 2983), 20 frames after previous cover
- f263: ref 79097: 45 -> 23 at (1090, 2983.5), 4 frames after previous cover
- f274: ref 78899: 45 -> 23 at (996, 2989.5), 5 frames after previous cover
- f282: ref 78897: 45 -> 23 at (913, 2990), 22 frames after previous cover
- f287: ref 78896: 5 -> 58 at (775, 2987), 14 frames after previous cover
- f304: ref 79108: 32 -> 68 at (954, 2978), 44 frames after previous cover
- f317: ref 79134: 32 -> 68 at (990.5, 2965.5), 74 frames after previous cover
- f327: ref 79132: 32 -> 68 at (895, 2966.5), 88 frames after previous cover
- f331: ref 79102: 23 -> 68 at (723.5, 2979.5), 82 frames after previous cover
- f333: ref 79097: 23 -> 68 at (654.5, 2972.5), 33 frames after previous cover
- f334: ref 78899: 23 -> 68 at (619, 2977.5), 39 frames after previous cover
- f338: ref 79105: 32 -> 23 at (719.5, 2978), 103 frames after previous cover
- f344: ref 79097: 68 -> 23 at (590, 2968.5), 2 frames after previous cover
- f345: ref 78899: 68 -> 23 at (554.5, 2973.5), 5 frames after previous cover
- f351: ref 78899: 23 -> 77 at (519, 2967.5), 6 frames after previous cover
- ... 78 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 974 | 8 | 0 (974) |
| 78896 | 350 (76..429) | 10 | 8 | 5 (7), 80 (2), 58 (1) |
| 78969 | 352 (80..434) | 92 | 45 | 5 (82), 80 (8), 23 (2) |
| 78971 | 352 (84..439) | 18 | 12 | 80 (7), 5 (5), 23 (5), 25 (1) |
| 79045 | 355 (84..443) | 16 | 11 | 23 (11), 80 (3), 45 (2) |
| 79037 | 355 (86..445) | 16 | 15 | 23 (6), 5 (3), 45 (3), 25 (2), 80 (2) |
| 78897 | 345 (89..450) | 27 | 21 | 23 (15), 80 (8), 5 (2), 45 (1), 79 (1) |
| 78899 | 365 (91..455) | 50 | 40 | 23 (23), 45 (12), 80 (5), 68 (3), 5 (3), 25 (2), 77 (1), 79 (1) |
| 79097 | 366 (94..461) | 66 | 43 | 23 (45), 25 (5), 45 (5), 68 (4), 5 (4), 80 (3) |
| 79098 | 360 (97..467) | 24 | 19 | 23 (11), 5 (10), 25 (1), 44 (1), 80 (1) |
| 79102 | 371 (98..477) | 24 | 14 | 5 (15), 80 (4), 23 (2), 68 (1), 79 (1), 44 (1) |
| 79103 | 380 (99..481) | 15 | 10 | 23 (5), 80 (5), 25 (2), 5 (2), 44 (1) |
| 79105 | 379 (101..484) | 6 | 5 | 25 (2), 32 (1), 23 (1), 79 (1), 44 (1) |
| 79108 | 385 (104..492) | 15 | 13 | 23 (3), 32 (3), 44 (3), 25 (2), 68 (2), 79 (1), 80 (1) |
| 79110 | 388 (106..497) | 14 | 7 | 80 (7), 32 (4), 25 (2), 44 (1) |
| 79111 | 386 (109..500) | 10 | 5 | 80 (5), 23 (2), 32 (2), 25 (1) |
| 79115 | 421 (111..531) | 9 | 8 | 32 (4), 25 (2), 79 (1), 35 (1), 55 (1) |
| 79116 | 411 (114..530) | 38 | 8 | 55 (37), 35 (1) |
| 79122 | 404 (118..532) | 19 | 10 | 79 (9), 55 (9), 35 (1) |
| 79132 | 391 (120..515) | 64 | 9 | 35 (56), 25 (4), 32 (2), 23 (1), 68 (1) |
| 79128 | 402 (124..527) | 13 | 10 | 32 (5), 35 (4), 25 (2), 23 (1), 79 (1) |
| 79134 | 407 (127..533) | 15 | 13 | 32 (4), 25 (3), 55 (3), 35 (2), 23 (1), 68 (1), 79 (1) |
| 79135 | 409 (129..542) | 40 | 32 | 32 (10), 43 (10), 25 (5), 35 (5), 89 (4), 55 (3), 23 (2), 79 (1) |
| 79139 | 406 (132..537) | 21 | 14 | 32 (9), 55 (7), 43 (2), 25 (1), 35 (1), 79 (1) |
| 79136 | 393 (136..538) | 3 | 2 | 89 (1), 43 (1), 55 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 49 | 271..614 | 344 | 0 | 232 |
| 60 | 286..568 | 283 | 0 | 181 |
| 63 | 292..534 | 243 | 0 | 128 |
| 65 | 300..606 | 307 | 0 | 205 |
| 71 | 338..338 | 1 | 0 | 1 |
| 87 | 412..607 | 196 | 0 | 132 |
| 107 | 532..537 | 6 | 0 | 3 |
| 117 | 595..596 | 2 | 0 | 2 |
| 126 | 659..665 | 7 | 0 | 7 |

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 1/196/1005; tracks with internal gaps: 16; total internal gaps: 141; longest internal gap: 194; tracks ending in coasting: 16 (trailing rows total 972)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1008 | 1005 | 979 | 974 | 5 | 4 | 2 | 0 | 78911 |
| 5 | 82..453 | 372 | 318 | 133 | 185 | 42 | 53 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103 |
| 23 | 169..461 | 293 | 165 | 136 | 29 | 15 | 4 | 4 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79111, 79128, 79132, 79134, 79135 |
| 25 | 176..274 | 99 | 49 | 37 | 12 | 7 | 2 | 3 | 78899, 78971, 79037, 79097, 79098, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 32 | 196..412 | 217 | 77 | 44 | 33 | 6 | 2 | 26 | 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79139 |
| 35 | 206..514 | 309 | 297 | 71 | 226 | 8 | 194 | 0 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79139 |
| 43 | 236..551 | 316 | 258 | 13 | 245 | 5 | 163 | 12 | 79135, 79136, 79139 |
| 44 | 242..464 | 223 | 161 | 8 | 153 | 2 | 148 | 0 | 79098, 79102, 79103, 79105, 79108, 79110 |
| 45 | 245..280 | 36 | 29 | 23 | 6 | 2 | 1 | 4 | 78897, 78899, 79037, 79045, 79097 |
| 49 | 271..614 | 344 | 232 | 0 | 232 | 0 | 0 | 232 | - |
| 55 | 280..592 | 313 | 249 | 61 | 188 | 8 | 137 | 31 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 58 | 284..292 | 9 | 5 | 1 | 4 | 1 | 3 | 1 | 78896 |
| 60 | 286..568 | 283 | 181 | 0 | 181 | 0 | 0 | 181 | - |
| 63 | 292..534 | 243 | 128 | 0 | 128 | 0 | 0 | 128 | - |
| 65 | 300..606 | 307 | 205 | 0 | 205 | 0 | 0 | 205 | - |
| 68 | 303..342 | 40 | 26 | 12 | 14 | 6 | 5 | 0 | 78899, 79097, 79102, 79108, 79132, 79134 |
| 71 | 338..338 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | - |
| 77 | 349..351 | 3 | 3 | 1 | 2 | 1 | 2 | 0 | 78899 |
| 79 | 366..443 | 78 | 63 | 19 | 44 | 10 | 17 | 0 | 78897, 78899, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 80 | 373..499 | 127 | 98 | 61 | 37 | 19 | 5 | 0 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 87 | 412..607 | 196 | 132 | 0 | 132 | 0 | 0 | 132 | - |
| 89 | 434..486 | 53 | 27 | 5 | 22 | 5 | 10 | 0 | 79135, 79136 |
| 107 | 532..537 | 6 | 3 | 0 | 3 | 0 | 0 | 3 | - |
| 117 | 595..596 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | - |
| 126 | 659..665 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |

## Diagnostics: view=updates, region=none, match 8 px
- reference objects: 25; candidate ids: 68; matched pairs: 1864; unmatched reference entries: 8278; unmatched candidate entries: 7149
- identity switches: 206; fragmentation (coverage interruptions): 436; orphan candidate ids (never on a reference object): 52

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f176: ref 79132: 23 -> 25 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 23 -> 25 at (1843, 3015), 9 frames after previous cover
- f181: ref 79134: 25 -> 23 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 5 -> 23 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 23 -> 5 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 5 -> 23 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 23 -> 5 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 78969: 23 -> 5 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 79134: 23 -> 25 at (1753.5, 3017.5), 11 frames after previous cover
- f195: ref 79128: 23 -> 25 at (1712.5, 3015), 23 frames after previous cover
- f196: ref 79139: 25 -> 32 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 25 -> 32 at (1718, 3008.5), 8 frames after previous cover
- f207: ref 79134: 25 -> 32 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 25 -> 32 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 25 -> 32 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 23 -> 25 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 25 -> 32 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 23 -> 25 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 5 -> 23 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 23 -> 25 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 25 -> 32 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 23 -> 32 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 25 -> 32 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 25 -> 32 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 25 -> 23 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 32 -> 25 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 32 -> 25 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 32 -> 25 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 32 -> 25 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 32 -> 25 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 25 -> 32 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 25 -> 32 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 25 -> 32 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 23 -> 25 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 25 -> 32 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 23 -> 25 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 25 -> 23 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78971: 5 -> 25 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 25 -> 32 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 32 -> 23 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 25 -> 23 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 25 -> 5 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 25 -> 23 at (1359, 2995.5), 18 frames after previous cover
- f244: ref 78971: 5 -> 25 at (1106.5, 2984.5), 2 frames after previous cover
- f245: ref 78899: 25 -> 45 at (1179, 2985.5), 5 frames after previous cover
- f245: ref 79102: 25 -> 23 at (1254.5, 2986), 11 frames after previous cover
- f246: ref 79097: 23 -> 45 at (1199.5, 2985), 7 frames after previous cover
- f247: ref 79111: 23 -> 32 at (1328.5, 2993.5), 5 frames after previous cover
- f251: ref 79122: 23 -> 32 at (1330.5, 2994), 76 frames after previous cover
- f253: ref 78897: 23 -> 25 at (1100.5, 2987.5), 27 frames after previous cover
- f253: ref 79105: 32 -> 23 at (1236, 2985.5), 17 frames after previous cover
- f255: ref 79037: 25 -> 45 at (1069.5, 2987.5), 4 frames after previous cover
- f257: ref 78899: 45 -> 25 at (1103, 2985), 3 frames after previous cover
- f258: ref 78971: 25 -> 5 at (1018, 2985.5), 12 frames after previous cover
- f260: ref 78897: 25 -> 45 at (1057.5, 2987.5), 6 frames after previous cover
- f261: ref 78899: 25 -> 45 at (1079.5, 2986), 3 frames after previous cover
- f261: ref 79097: 45 -> 25 at (1103.5, 2983), 2 frames after previous cover
- f261: ref 79108: 23 -> 32 at (1218.5, 2983.5), 1 frames after previous cover
- f261: ref 79110: 32 -> 23 at (1234.5, 2983), 3 frames after previous cover
- f263: ref 79097: 25 -> 23 at (1090, 2983.5), 1 frames after previous cover
- ... 146 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 977 | 6 | 0 (977) |
| 78896 | 350 (76..429) | 11 | 8 | 5 (7), 58 (2), 80 (2) |
| 78969 | 352 (80..434) | 105 | 46 | 5 (83), 80 (11), 23 (9), 58 (2) |
| 78971 | 352 (84..439) | 26 | 15 | 80 (8), 23 (7), 5 (5), 25 (4), 45 (1), 58 (1) |
| 79045 | 355 (84..443) | 30 | 13 | 23 (16), 80 (5), 25 (3), 45 (3), 58 (3) |
| 79037 | 355 (86..445) | 29 | 18 | 23 (12), 25 (5), 5 (4), 45 (3), 80 (3), 58 (2) |
| 78897 | 345 (89..450) | 44 | 24 | 23 (22), 80 (9), 5 (6), 58 (3), 25 (2), 45 (1), 79 (1) |
| 78899 | 365 (91..455) | 64 | 39 | 23 (27), 45 (14), 80 (6), 25 (5), 68 (3), 5 (3), 79 (3), 58 (2), 77 (1) |
| 79097 | 366 (94..461) | 78 | 43 | 23 (46), 25 (7), 45 (5), 68 (5), 80 (4), 5 (4), 58 (3), 77 (3), 79 (1) |
| 79098 | 360 (97..467) | 44 | 23 | 23 (16), 5 (12), 25 (4), 77 (4), 80 (4), 58 (2), 68 (2) |
| 79102 | 371 (98..477) | 39 | 16 | 5 (17), 80 (4), 25 (3), 23 (3), 68 (3), 77 (3), 58 (2), 79 (2), 44 (2) |
| 79103 | 380 (99..481) | 30 | 13 | 23 (10), 5 (5), 80 (5), 77 (3), 25 (2), 58 (2), 68 (2), 44 (1) |
| 79105 | 379 (101..484) | 22 | 10 | 23 (5), 58 (3), 77 (3), 5 (3), 25 (2), 32 (2), 68 (2), 79 (1), 44 (1) |
| 79108 | 385 (104..492) | 30 | 18 | 23 (7), 44 (5), 68 (4), 32 (3), 58 (3), 25 (2), 77 (2), 5 (2), 79 (1), 80 (1) |
| 79110 | 388 (106..497) | 26 | 12 | 80 (7), 32 (5), 68 (3), 77 (3), 25 (2), 23 (2), 58 (2), 44 (1), 5 (1) |
| 79111 | 386 (109..500) | 18 | 9 | 80 (6), 32 (4), 23 (2), 58 (2), 77 (2), 25 (1), 68 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 32 (6), 25 (2), 68 (2), 79 (1), 35 (1), 55 (1) |
| 79116 | 411 (114..530) | 42 | 9 | 55 (37), 35 (5) |
| 79122 | 404 (118..532) | 30 | 15 | 55 (12), 79 (9), 58 (3), 35 (3), 32 (2), 23 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 35 (57), 25 (4), 32 (2), 23 (1), 68 (1) |
| 79128 | 402 (124..527) | 21 | 13 | 35 (7), 25 (6), 32 (5), 79 (2), 23 (1) |
| 79134 | 407 (127..533) | 20 | 15 | 25 (5), 32 (4), 55 (4), 79 (3), 35 (2), 23 (1), 68 (1) |
| 79135 | 409 (129..542) | 56 | 31 | 43 (14), 89 (11), 32 (10), 35 (8), 25 (5), 55 (4), 23 (3), 79 (1) |
| 79139 | 406 (132..537) | 28 | 13 | 32 (13), 55 (8), 35 (3), 43 (2), 25 (1), 79 (1) |
| 79136 | 393 (136..538) | 16 | 7 | 32 (7), 35 (3), 89 (2), 55 (2), 25 (1), 43 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 34 | 202..268 | 67 | 0 | 67 |
| 39 | 219..281 | 63 | 0 | 63 |
| 41 | 227..292 | 66 | 0 | 66 |
| 46 | 252..317 | 66 | 0 | 66 |
| 49 | 271..673 | 403 | 0 | 403 |
| 51 | 277..349 | 73 | 0 | 73 |
| 56 | 281..343 | 63 | 0 | 63 |
| 60 | 286..627 | 342 | 0 | 342 |
| 63 | 292..593 | 302 | 0 | 302 |
| 65 | 300..665 | 366 | 0 | 366 |
| 66 | 302..370 | 69 | 0 | 69 |
| 69 | 327..394 | 68 | 0 | 68 |
| 71 | 338..397 | 60 | 0 | 60 |
| 73 | 343..405 | 63 | 0 | 63 |
| 78 | 352..419 | 68 | 0 | 68 |
| 82 | 377..443 | 67 | 0 | 67 |
| 85 | 405..467 | 63 | 0 | 63 |
| 87 | 412..666 | 255 | 0 | 255 |
| 88 | 427..492 | 66 | 0 | 66 |
| 91 | 453..515 | 63 | 0 | 63 |
| 93 | 467..529 | 63 | 0 | 63 |
| 98 | 477..542 | 66 | 0 | 66 |
| 103 | 502..567 | 66 | 0 | 66 |
| 105 | 529..591 | 63 | 0 | 63 |
| 106 | 531..594 | 64 | 0 | 64 |
| 107 | 532..596 | 65 | 0 | 65 |
| 110 | 552..620 | 69 | 0 | 69 |
| 116 | 591..653 | 63 | 0 | 63 |
| 117 | 595..655 | 61 | 0 | 61 |
| 120 | 602..669 | 68 | 0 | 68 |
| 122 | 627..693 | 67 | 0 | 67 |
| 124 | 653..715 | 63 | 0 | 63 |
| 126 | 659..724 | 66 | 0 | 66 |
| 128 | 677..744 | 68 | 0 | 68 |
| 129 | 703..767 | 65 | 0 | 65 |
| 130 | 715..777 | 63 | 0 | 63 |
| 134 | 727..792 | 66 | 0 | 66 |
| 136 | 752..817 | 66 | 0 | 66 |
| 137 | 777..841 | 65 | 0 | 65 |
| 144 | 802..870 | 69 | 0 | 69 |
| ... | 12 more | | | |

### Gaps and durations of candidate tracks
- tracks: 68; lifespan min/median/max: 7/67/1005; tracks with internal gaps: 16; total internal gaps: 243; longest internal gap: 200; tracks ending in coasting: 67 (trailing rows total 5558)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1008 | 1005 | 1005 | 977 | 28 | 6 | 21 | 0 | 78911 |
| 5 | 82..512 | 431 | 431 | 152 | 279 | 50 | 53 | 43 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 23 | 169..520 | 352 | 352 | 191 | 161 | 38 | 31 | 56 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79128, 79132, 79134, 79135 |
| 25 | 176..333 | 158 | 158 | 66 | 92 | 19 | 3 | 66 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 32 | 196..471 | 276 | 276 | 63 | 213 | 11 | 4 | 198 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 34 | 202..268 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 35 | 206..573 | 368 | 368 | 89 | 279 | 13 | 197 | 31 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 39 | 219..281 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 41 | 227..292 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 43 | 236..610 | 375 | 375 | 17 | 358 | 6 | 183 | 71 | 79135, 79136, 79139 |
| 44 | 242..523 | 282 | 282 | 10 | 272 | 6 | 200 | 61 | 79102, 79103, 79105, 79108, 79110 |
| 45 | 245..339 | 95 | 95 | 27 | 68 | 5 | 2 | 62 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 46 | 252..317 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 49 | 271..673 | 403 | 403 | 0 | 403 | 0 | 0 | 403 | - |
| 51 | 277..349 | 73 | 73 | 0 | 73 | 0 | 0 | 73 | - |
| 55 | 280..651 | 372 | 372 | 68 | 304 | 11 | 148 | 118 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 56 | 281..343 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 58 | 284..351 | 68 | 68 | 37 | 31 | 12 | 6 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122 |
| 60 | 286..627 | 342 | 342 | 0 | 342 | 0 | 0 | 342 | - |
| 63 | 292..593 | 302 | 302 | 0 | 302 | 0 | 0 | 302 | - |
| 65 | 300..665 | 366 | 366 | 0 | 366 | 0 | 0 | 366 | - |
| 66 | 302..370 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 68 | 303..401 | 99 | 99 | 29 | 70 | 15 | 11 | 32 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132, 79134 |
| 69 | 327..394 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 71 | 338..397 | 60 | 60 | 0 | 60 | 0 | 0 | 60 | - |
| 73 | 343..405 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 77 | 349..410 | 62 | 62 | 24 | 38 | 9 | 3 | 22 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 78 | 352..419 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 79 | 366..502 | 137 | 137 | 26 | 111 | 14 | 20 | 49 | 78897, 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 80 | 373..558 | 186 | 186 | 75 | 111 | 22 | 5 | 58 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 82 | 377..443 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 85 | 405..467 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 87 | 412..666 | 255 | 255 | 0 | 255 | 0 | 0 | 255 | - |
| 88 | 427..492 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 89 | 434..545 | 112 | 112 | 13 | 99 | 6 | 15 | 53 | 79135, 79136 |
| 91 | 453..515 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 93 | 467..529 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 98 | 477..542 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 103 | 502..567 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 105 | 529..591 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 106 | 531..594 | 64 | 64 | 0 | 64 | 0 | 0 | 64 | - |
| 107 | 532..596 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 110 | 552..620 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 116 | 591..653 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 117 | 595..655 | 61 | 61 | 0 | 61 | 0 | 0 | 61 | - |
| 120 | 602..669 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 122 | 627..693 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 124 | 653..715 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 126 | 659..724 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 128 | 677..744 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 129 | 703..767 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 130 | 715..777 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 134 | 727..792 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 136 | 752..817 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
| 137 | 777..841 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 144 | 802..870 | 69 | 69 | 0 | 69 | 0 | 0 | 69 | - |
| 146 | 827..893 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 147 | 839..901 | 63 | 63 | 0 | 63 | 0 | 0 | 63 | - |
| 152 | 852..919 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 155 | 877..944 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 156 | 901..965 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 157 | 903..970 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 165 | 927..994 | 68 | 68 | 0 | 68 | 0 | 0 | 68 | - |
| 166 | 933..999 | 67 | 67 | 0 | 67 | 0 | 0 | 67 | - |
| 167 | 952..1008 | 57 | 57 | 0 | 57 | 0 | 0 | 57 | - |
| 169 | 963..1008 | 46 | 46 | 0 | 46 | 0 | 0 | 46 | - |
| 171 | 977..1008 | 32 | 32 | 0 | 32 | 0 | 0 | 32 | - |
| 175 | 1002..1008 | 7 | 7 | 0 | 7 | 0 | 0 | 7 | - |

## Diagnostics: view=updates, region=ignored, match 8 px
- reference objects: 25; candidate ids: 25; matched pairs: 1864; unmatched reference entries: 8278; unmatched candidate entries: 4434
- identity switches: 206; fragmentation (coverage interruptions): 436; orphan candidate ids (never on a reference object): 9

### Identity switches (frame, reference id, previous -> new candidate id, position, frames since previous)
- f176: ref 79132: 23 -> 25 at (1812, 3020), 3 frames after previous cover
- f180: ref 79135: 23 -> 25 at (1843, 3015), 9 frames after previous cover
- f181: ref 79134: 25 -> 23 at (1824.5, 3019.5), 3 frames after previous cover
- f186: ref 78971: 5 -> 23 at (1481, 3016), 97 frames after previous cover
- f187: ref 79037: 23 -> 5 at (1504.5, 3019), 2 frames after previous cover
- f188: ref 78969: 5 -> 23 at (1444, 3012.5), 4 frames after previous cover
- f188: ref 78971: 23 -> 5 at (1467.5, 3014), 2 frames after previous cover
- f192: ref 78969: 23 -> 5 at (1414, 3008.5), 3 frames after previous cover
- f192: ref 79134: 23 -> 25 at (1753.5, 3017.5), 11 frames after previous cover
- f195: ref 79128: 23 -> 25 at (1712.5, 3015), 23 frames after previous cover
- f196: ref 79139: 25 -> 32 at (1760, 3010.5), 12 frames after previous cover
- f199: ref 79135: 25 -> 32 at (1718, 3008.5), 8 frames after previous cover
- f207: ref 79134: 25 -> 32 at (1655.5, 3014), 8 frames after previous cover
- f209: ref 79136: 25 -> 32 at (1698.5, 3013.5), 27 frames after previous cover
- f212: ref 79128: 25 -> 32 at (1599.5, 3009), 3 frames after previous cover
- f213: ref 79108: 23 -> 25 at (1509.5, 3005), 35 frames after previous cover
- f214: ref 79132: 25 -> 32 at (1561, 3005), 4 frames after previous cover
- f215: ref 79103: 23 -> 25 at (1443.5, 3004.5), 36 frames after previous cover
- f216: ref 79037: 5 -> 23 at (1318.5, 2997), 29 frames after previous cover
- f216: ref 79097: 23 -> 25 at (1390.5, 2998), 3 frames after previous cover
- f216: ref 79115: 25 -> 32 at (1525.5, 3005), 5 frames after previous cover
- f217: ref 79111: 23 -> 32 at (1510.5, 3004), 41 frames after previous cover
- f218: ref 79110: 25 -> 32 at (1493.5, 3005.5), 6 frames after previous cover
- f220: ref 79108: 25 -> 32 at (1465, 3003), 7 frames after previous cover
- f222: ref 79097: 25 -> 23 at (1352, 2994.5), 1 frames after previous cover
- f222: ref 79132: 32 -> 25 at (1509.5, 2999), 8 frames after previous cover
- f223: ref 79115: 32 -> 25 at (1483.5, 3004), 7 frames after previous cover
- f224: ref 79111: 32 -> 25 at (1469, 3002), 7 frames after previous cover
- f225: ref 79110: 32 -> 25 at (1453, 3001.5), 7 frames after previous cover
- f226: ref 79108: 32 -> 25 at (1429.5, 2998), 6 frames after previous cover
- f232: ref 79115: 25 -> 32 at (1429.5, 3001), 9 frames after previous cover
- f233: ref 79110: 25 -> 32 at (1404, 2997), 8 frames after previous cover
- f234: ref 79108: 25 -> 32 at (1381.5, 2994), 8 frames after previous cover
- f235: ref 78899: 23 -> 25 at (1242.5, 2989), 7 frames after previous cover
- f235: ref 79105: 25 -> 32 at (1344, 2992), 8 frames after previous cover
- f237: ref 79037: 23 -> 25 at (1184.5, 2988), 21 frames after previous cover
- f237: ref 79098: 25 -> 23 at (1285.5, 2989.5), 6 frames after previous cover
- f239: ref 78971: 5 -> 25 at (1139, 2987), 10 frames after previous cover
- f239: ref 79132: 25 -> 32 at (1404.5, 2987), 17 frames after previous cover
- f240: ref 79108: 32 -> 23 at (1344.5, 2992), 6 frames after previous cover
- f241: ref 79103: 25 -> 23 at (1290, 2989.5), 13 frames after previous cover
- f242: ref 78971: 25 -> 5 at (1119, 2986), 3 frames after previous cover
- f242: ref 79111: 25 -> 23 at (1359, 2995.5), 18 frames after previous cover
- f244: ref 78971: 5 -> 25 at (1106.5, 2984.5), 2 frames after previous cover
- f245: ref 78899: 25 -> 45 at (1179, 2985.5), 5 frames after previous cover
- f245: ref 79102: 25 -> 23 at (1254.5, 2986), 11 frames after previous cover
- f246: ref 79097: 23 -> 45 at (1199.5, 2985), 7 frames after previous cover
- f247: ref 79111: 23 -> 32 at (1328.5, 2993.5), 5 frames after previous cover
- f251: ref 79122: 23 -> 32 at (1330.5, 2994), 76 frames after previous cover
- f253: ref 78897: 23 -> 25 at (1100.5, 2987.5), 27 frames after previous cover
- f253: ref 79105: 32 -> 23 at (1236, 2985.5), 17 frames after previous cover
- f255: ref 79037: 25 -> 45 at (1069.5, 2987.5), 4 frames after previous cover
- f257: ref 78899: 45 -> 25 at (1103, 2985), 3 frames after previous cover
- f258: ref 78971: 25 -> 5 at (1018, 2985.5), 12 frames after previous cover
- f260: ref 78897: 25 -> 45 at (1057.5, 2987.5), 6 frames after previous cover
- f261: ref 78899: 25 -> 45 at (1079.5, 2986), 3 frames after previous cover
- f261: ref 79097: 45 -> 25 at (1103.5, 2983), 2 frames after previous cover
- f261: ref 79108: 23 -> 32 at (1218.5, 2983.5), 1 frames after previous cover
- f261: ref 79110: 32 -> 23 at (1234.5, 2983), 3 frames after previous cover
- f263: ref 79097: 25 -> 23 at (1090, 2983.5), 1 frames after previous cover
- ... 146 more in the JSON report

### Candidate ids per reference object (fragmentation)
| reference id | frames | covered | fragments | candidate ids (frames) |
|---|---|---|---|---|
| 78911 | 1009 (0..1008) | 977 | 6 | 0 (977) |
| 78896 | 350 (76..429) | 11 | 8 | 5 (7), 58 (2), 80 (2) |
| 78969 | 352 (80..434) | 105 | 46 | 5 (83), 80 (11), 23 (9), 58 (2) |
| 78971 | 352 (84..439) | 26 | 15 | 80 (8), 23 (7), 5 (5), 25 (4), 45 (1), 58 (1) |
| 79045 | 355 (84..443) | 30 | 13 | 23 (16), 80 (5), 25 (3), 45 (3), 58 (3) |
| 79037 | 355 (86..445) | 29 | 18 | 23 (12), 25 (5), 5 (4), 45 (3), 80 (3), 58 (2) |
| 78897 | 345 (89..450) | 44 | 24 | 23 (22), 80 (9), 5 (6), 58 (3), 25 (2), 45 (1), 79 (1) |
| 78899 | 365 (91..455) | 64 | 39 | 23 (27), 45 (14), 80 (6), 25 (5), 68 (3), 5 (3), 79 (3), 58 (2), 77 (1) |
| 79097 | 366 (94..461) | 78 | 43 | 23 (46), 25 (7), 45 (5), 68 (5), 80 (4), 5 (4), 58 (3), 77 (3), 79 (1) |
| 79098 | 360 (97..467) | 44 | 23 | 23 (16), 5 (12), 25 (4), 77 (4), 80 (4), 58 (2), 68 (2) |
| 79102 | 371 (98..477) | 39 | 16 | 5 (17), 80 (4), 25 (3), 23 (3), 68 (3), 77 (3), 58 (2), 79 (2), 44 (2) |
| 79103 | 380 (99..481) | 30 | 13 | 23 (10), 5 (5), 80 (5), 77 (3), 25 (2), 58 (2), 68 (2), 44 (1) |
| 79105 | 379 (101..484) | 22 | 10 | 23 (5), 58 (3), 77 (3), 5 (3), 25 (2), 32 (2), 68 (2), 79 (1), 44 (1) |
| 79108 | 385 (104..492) | 30 | 18 | 23 (7), 44 (5), 68 (4), 32 (3), 58 (3), 25 (2), 77 (2), 5 (2), 79 (1), 80 (1) |
| 79110 | 388 (106..497) | 26 | 12 | 80 (7), 32 (5), 68 (3), 77 (3), 25 (2), 23 (2), 58 (2), 44 (1), 5 (1) |
| 79111 | 386 (109..500) | 18 | 9 | 80 (6), 32 (4), 23 (2), 58 (2), 77 (2), 25 (1), 68 (1) |
| 79115 | 421 (111..531) | 13 | 11 | 32 (6), 25 (2), 68 (2), 79 (1), 35 (1), 55 (1) |
| 79116 | 411 (114..530) | 42 | 9 | 55 (37), 35 (5) |
| 79122 | 404 (118..532) | 30 | 15 | 55 (12), 79 (9), 58 (3), 35 (3), 32 (2), 23 (1) |
| 79132 | 391 (120..515) | 65 | 9 | 35 (57), 25 (4), 32 (2), 23 (1), 68 (1) |
| 79128 | 402 (124..527) | 21 | 13 | 35 (7), 25 (6), 32 (5), 79 (2), 23 (1) |
| 79134 | 407 (127..533) | 20 | 15 | 25 (5), 32 (4), 55 (4), 79 (3), 35 (2), 23 (1), 68 (1) |
| 79135 | 409 (129..542) | 56 | 31 | 43 (14), 89 (11), 32 (10), 35 (8), 25 (5), 55 (4), 23 (3), 79 (1) |
| 79139 | 406 (132..537) | 28 | 13 | 32 (13), 55 (8), 35 (3), 43 (2), 25 (1), 79 (1) |
| 79136 | 393 (136..538) | 16 | 7 | 32 (7), 35 (3), 89 (2), 55 (2), 25 (1), 43 (1) |

### Orphan candidate ids
| id | frames | lifespan | rows on a reference object | rows on none |
|---|---|---|---|---|
| 49 | 271..673 | 403 | 0 | 403 |
| 60 | 286..627 | 342 | 0 | 342 |
| 63 | 292..593 | 302 | 0 | 302 |
| 65 | 300..665 | 366 | 0 | 366 |
| 71 | 338..397 | 60 | 0 | 60 |
| 87 | 412..666 | 255 | 0 | 255 |
| 107 | 532..596 | 65 | 0 | 65 |
| 117 | 595..655 | 61 | 0 | 61 |
| 126 | 659..724 | 66 | 0 | 66 |

### Gaps and durations of candidate tracks
- tracks: 25; lifespan min/median/max: 60/255/1005; tracks with internal gaps: 16; total internal gaps: 243; longest internal gap: 200; tracks ending in coasting: 24 (trailing rows total 2843)
| id | frames | lifespan | rows | rows on a reference object | rows on none | internal uncovered runs | longest run | trailing uncovered | covers |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4..1008 | 1005 | 1005 | 977 | 28 | 6 | 21 | 0 | 78911 |
| 5 | 82..512 | 431 | 431 | 152 | 279 | 50 | 53 | 43 | 78896, 78897, 78899, 78969, 78971, 79037, 79097, 79098, 79102, 79103, 79105, 79108, 79110 |
| 23 | 169..520 | 352 | 352 | 191 | 161 | 38 | 31 | 56 | 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122, 79128, 79132, 79134, 79135 |
| 25 | 176..333 | 158 | 158 | 66 | 92 | 19 | 3 | 66 | 78897, 78899, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79128, 79132, 79134, 79135, 79136, 79139 |
| 32 | 196..471 | 276 | 276 | 63 | 213 | 11 | 4 | 198 | 79105, 79108, 79110, 79111, 79115, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 35 | 206..573 | 368 | 368 | 89 | 279 | 13 | 197 | 31 | 79115, 79116, 79122, 79128, 79132, 79134, 79135, 79136, 79139 |
| 43 | 236..610 | 375 | 375 | 17 | 358 | 6 | 183 | 71 | 79135, 79136, 79139 |
| 44 | 242..523 | 282 | 282 | 10 | 272 | 6 | 200 | 61 | 79102, 79103, 79105, 79108, 79110 |
| 45 | 245..339 | 95 | 95 | 27 | 68 | 5 | 2 | 62 | 78897, 78899, 78971, 79037, 79045, 79097 |
| 49 | 271..673 | 403 | 403 | 0 | 403 | 0 | 0 | 403 | - |
| 55 | 280..651 | 372 | 372 | 68 | 304 | 11 | 148 | 118 | 79115, 79116, 79122, 79134, 79135, 79136, 79139 |
| 58 | 284..351 | 68 | 68 | 37 | 31 | 12 | 6 | 3 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79122 |
| 60 | 286..627 | 342 | 342 | 0 | 342 | 0 | 0 | 342 | - |
| 63 | 292..593 | 302 | 302 | 0 | 302 | 0 | 0 | 302 | - |
| 65 | 300..665 | 366 | 366 | 0 | 366 | 0 | 0 | 366 | - |
| 68 | 303..401 | 99 | 99 | 29 | 70 | 15 | 11 | 32 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111, 79115, 79132, 79134 |
| 71 | 338..397 | 60 | 60 | 0 | 60 | 0 | 0 | 60 | - |
| 77 | 349..410 | 62 | 62 | 24 | 38 | 9 | 3 | 22 | 78899, 79097, 79098, 79102, 79103, 79105, 79108, 79110, 79111 |
| 79 | 366..502 | 137 | 137 | 26 | 111 | 14 | 20 | 49 | 78897, 78899, 79097, 79102, 79105, 79108, 79115, 79122, 79128, 79134, 79135, 79139 |
| 80 | 373..558 | 186 | 186 | 75 | 111 | 22 | 5 | 58 | 78896, 78897, 78899, 78969, 78971, 79037, 79045, 79097, 79098, 79102, 79103, 79108, 79110, 79111 |
| 87 | 412..666 | 255 | 255 | 0 | 255 | 0 | 0 | 255 | - |
| 89 | 434..545 | 112 | 112 | 13 | 99 | 6 | 15 | 53 | 79135, 79136 |
| 107 | 532..596 | 65 | 65 | 0 | 65 | 0 | 0 | 65 | - |
| 117 | 595..655 | 61 | 61 | 0 | 61 | 0 | 0 | 61 | - |
| 126 | 659..724 | 66 | 66 | 0 | 66 | 0 | 0 | 66 | - |
