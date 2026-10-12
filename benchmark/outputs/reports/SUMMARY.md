# Experiment summary

Match distance 8 px (T = 16). Clips: flock: frames 4001..5009 of the original; 25 labelled birds (first flock only); portrait 2160x3840; turbine: frames 2000..2670 of the original; one labelled bird over frames 53..293; portrait 2160x3840; semrev: landscape 3840x2160, 500 frames; two labelled birds (one over frames 32..457, one over 359..409); no detector output, so only ground-truth boxes can be fed to the trackers. Ignore regions and labelled frame ranges from clips.json. `obs` = matched rows only, `all` = every row as written (coasting included). Per-run reports (provenance, 4/6/8/12 px, both views, with/without region, identity-switch lists) are in runs/<clip>/.

HOTA = sqrt(DetA * AssA), the overall score. AssA = association accuracy (one bird keeps one id, one id keeps one bird). MOTA = 1 - (FN + FP + IDSW) / labelled boxes, can be negative. MOTP px = mean center distance over matched pairs. IDF1 = identity F1. IDSW = identity switches. Frag = fragmentations (CLEAR definition; the flock GT's own 111 gaps give a floor of about 111 even to a perfect tracker). Other TrackEval fields stay in the per-run JSON reports.

## Trackers compared (flock, real detections, matched rows, default parameters)

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| botsort (roboflow trackers 2.6.0) | 0.145 | 0.194 | -0.032 | 1.80 | 0.088 | 131 | 316 |
| bytetrack (roboflow trackers 2.6.0) | 0.276 | 0.617 | -0.044 | 1.70 | 0.181 | 186 | 338 |
| cbiou (roboflow trackers 2.6.0) | 0.276 | 0.614 | -0.040 | 1.77 | 0.184 | 153 | 374 |
| ocsort (roboflow trackers 2.6.0) | 0.069 | 0.067 | 0.008 | 1.37 | 0.041 | 44 | 92 |
| simplesort (spoor tracker-kit (tracker/)) | 0.273 | 0.594 | -0.069 | 1.80 | 0.180 | 156 | 416 |
| sort (roboflow trackers 2.6.0) | 0.071 | 0.064 | -0.042 | 1.70 | 0.044 | 94 | 190 |

## Trackers compared (flock, ground-truth boxes as detections, matched rows, default parameters)

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| botsort (roboflow trackers 2.6.0) | 0.566 | 0.482 | 0.587 | 0.03 | 0.618 | 811 | 555 |
| bytetrack (roboflow trackers 2.6.0) | 0.971 | 0.951 | 0.989 | 0.01 | 0.969 | 41 | 132 |
| cbiou (roboflow trackers 2.6.0) | 0.990 | 0.987 | 0.993 | 0.01 | 0.995 | 15 | 122 |
| ocsort (roboflow trackers 2.6.0) | 0.353 | 0.300 | 0.410 | 0.03 | 0.450 | 50 | 125 |
| simplesort (spoor tracker-kit (tracker/)) | 0.962 | 0.934 | 0.993 | 0.01 | 0.973 | 17 | 116 |
| sort (roboflow trackers 2.6.0) | 0.411 | 0.323 | 0.510 | 0.02 | 0.471 | 152 | 220 |

## Trackers compared (turbine, real detections, matched rows, default parameters)

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| botsort (roboflow trackers 2.6.0) | 0.162 | 0.133 | -0.162 | 0.32 | 0.183 | 3 | 2 |
| bytetrack (roboflow trackers 2.6.0) | 0.468 | 0.401 | 0.299 | 0.49 | 0.453 | 2 | 3 |
| cbiou (roboflow trackers 2.6.0) | 0.565 | 0.586 | 0.299 | 0.49 | 0.574 | 1 | 3 |
| ocsort (roboflow trackers 2.6.0) | 0.189 | 0.197 | -0.029 | 0.20 | 0.286 | 1 | 0 |
| simplesort (spoor tracker-kit (tracker/)) | 0.682 | 0.821 | 0.361 | 0.48 | 0.734 | 0 | 3 |
| sort (roboflow trackers 2.6.0) | 0.075 | 0.041 | -0.133 | 0.32 | 0.067 | 4 | 3 |

## Trackers compared (turbine, ground-truth boxes as detections, matched rows, default parameters)

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| botsort (roboflow trackers 2.6.0) | 0.905 | 0.900 | 0.905 | 0.00 | 0.948 | 1 | 0 |
| bytetrack (roboflow trackers 2.6.0) | 0.996 | 0.996 | 0.996 | 0.00 | 0.998 | 0 | 0 |
| cbiou (roboflow trackers 2.6.0) | 0.996 | 0.996 | 0.996 | 0.00 | 0.998 | 0 | 0 |
| ocsort (roboflow trackers 2.6.0) | 0.423 | 0.408 | 0.432 | 0.00 | 0.588 | 2 | 0 |
| simplesort (spoor tracker-kit (tracker/)) | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |
| sort (roboflow trackers 2.6.0) | 0.232 | 0.175 | 0.290 | 0.00 | 0.349 | 4 | 0 |

## Trackers compared (semrev, ground-truth boxes as detections, matched rows, default parameters)

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| botsort (roboflow trackers 2.6.0) | 0.790 | 0.791 | 0.788 | 0.00 | 0.882 | 0 | 0 |
| bytetrack (roboflow trackers 2.6.0) | 0.969 | 0.969 | 0.969 | 0.00 | 0.984 | 0 | 0 |
| cbiou (roboflow trackers 2.6.0) | 0.969 | 0.969 | 0.969 | 0.00 | 0.984 | 0 | 0 |
| ocsort (roboflow trackers 2.6.0) | 0.698 | 0.640 | 0.755 | 0.00 | 0.786 | 3 | 0 |
| simplesort (spoor tracker-kit (tracker/)) | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |
| sort (roboflow trackers 2.6.0) | 0.724 | 0.722 | 0.723 | 0.00 | 0.836 | 1 | 0 |

## E1 accuracy: baseline (real detections, default parameters) against ground truth

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| flock (obs) | 0.273 | 0.594 | -0.069 | 1.80 | 0.180 | 156 | 416 |
| flock (all) | 0.252 | 0.519 | -0.233 | 2.23 | 0.160 | 227 | 472 |
| turbine (obs) | 0.682 | 0.821 | 0.361 | 0.48 | 0.734 | 0 | 3 |
| turbine (all) | 0.477 | 0.793 | -1.178 | 0.52 | 0.450 | 0 | 4 |

## E2 parity: baseline against the cloud export

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| flock (obs) | 0.504 | 0.397 | 0.500 | 0.23 | 0.497 | 170 | 449 |
| flock (all) | 0.399 | 0.362 | -0.081 | 0.31 | 0.389 | 177 | 462 |
| turbine (obs) | 0.732 | 0.931 | 0.358 | 0.10 | 0.732 | 0 | 7 |
| turbine (all) | 0.357 | 0.684 | -2.831 | 0.10 | 0.315 | 0 | 8 |

## E3 association ceiling: ground truth as detections

| run | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|
| flock (obs) | 0.962 | 0.934 | 0.993 | 0.01 | 0.973 | 17 | 116 |
| flock (all) | 0.892 | 0.868 | 0.913 | 0.01 | 0.936 | 15 | 116 |
| turbine (obs) | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |
| turbine (all) | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |

## E4 robustness: degraded ground truth (flock, matched rows), mean +- half-range over seeds

| drop | noise px | FP/frame | seeds | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.0 | 0.0 | 0.0 | 1 | 0.963 +- 0.000 | 0.934 +- 0.000 | 0.993 +- 0.000 | 0.01 +- 0.00 | 0.973 +- 0.000 | 18.0 +- 0.0 | 116.0 +- 0.0 |
| 0.0 | 0.0 | 0.5 | 3 | 0.850 +- 0.046 | 0.742 +- 0.091 | 0.989 +- 0.001 | 0.01 +- 0.00 | 0.841 +- 0.058 | 43.7 +- 12.5 | 116.7 +- 0.5 |
| 0.0 | 1.0 | 0.0 | 3 | 0.891 +- 0.011 | 0.868 +- 0.016 | 0.993 +- 0.001 | 1.27 +- 0.00 | 0.973 +- 0.009 | 17.3 +- 4.5 | 114.0 +- 2.5 |
| 0.0 | 1.0 | 0.5 | 3 | 0.807 +- 0.044 | 0.718 +- 0.075 | 0.989 +- 0.003 | 1.28 +- 0.00 | 0.868 +- 0.054 | 48.0 +- 29.0 | 117.0 +- 7.0 |
| 0.0 | 3.0 | 0.0 | 3 | 0.605 +- 0.012 | 0.534 +- 0.013 | 0.922 +- 0.002 | 3.60 +- 0.01 | 0.803 +- 0.019 | 96.3 +- 5.0 | 422.0 +- 10.5 |
| 0.0 | 3.0 | 0.5 | 3 | 0.581 +- 0.030 | 0.491 +- 0.049 | 0.918 +- 0.006 | 3.60 +- 0.01 | 0.761 +- 0.049 | 128.7 +- 33.5 | 424.3 +- 13.0 |
| 0.1 | 0.0 | 0.0 | 3 | 0.812 +- 0.014 | 0.760 +- 0.028 | 0.875 +- 0.006 | 0.01 +- 0.00 | 0.882 +- 0.012 | 153.3 +- 27.5 | 990.3 +- 41.5 |
| 0.1 | 0.0 | 0.5 | 3 | 0.492 +- 0.031 | 0.281 +- 0.035 | 0.841 +- 0.019 | 0.02 +- 0.00 | 0.471 +- 0.059 | 452.7 +- 163.0 | 993.0 +- 40.0 |
| 0.1 | 1.0 | 0.0 | 3 | 0.726 +- 0.021 | 0.661 +- 0.028 | 0.871 +- 0.005 | 1.28 +- 0.02 | 0.856 +- 0.018 | 224.0 +- 75.5 | 959.0 +- 20.0 |
| 0.1 | 1.0 | 0.5 | 3 | 0.471 +- 0.023 | 0.281 +- 0.031 | 0.840 +- 0.004 | 1.29 +- 0.01 | 0.481 +- 0.056 | 475.3 +- 67.0 | 964.3 +- 18.0 |
| 0.1 | 3.0 | 0.0 | 3 | 0.526 +- 0.017 | 0.450 +- 0.025 | 0.804 +- 0.009 | 3.60 +- 0.03 | 0.743 +- 0.023 | 327.3 +- 105.5 | 1172.7 +- 21.0 |
| 0.1 | 3.0 | 0.5 | 3 | 0.355 +- 0.011 | 0.200 +- 0.011 | 0.760 +- 0.009 | 3.61 +- 0.03 | 0.434 +- 0.033 | 702.0 +- 130.0 | 1178.0 +- 18.5 |
| 0.2 | 0.0 | 0.0 | 3 | 0.508 +- 0.132 | 0.354 +- 0.189 | 0.742 +- 0.018 | 0.03 +- 0.02 | 0.530 +- 0.201 | 495.7 +- 200.0 | 1608.3 +- 28.0 |
| 0.2 | 0.0 | 0.5 | 3 | 0.359 +- 0.006 | 0.167 +- 0.006 | 0.686 +- 0.016 | 0.05 +- 0.02 | 0.317 +- 0.018 | 998.0 +- 166.5 | 1605.7 +- 28.0 |
| 0.2 | 1.0 | 0.0 | 3 | 0.466 +- 0.110 | 0.319 +- 0.154 | 0.730 +- 0.025 | 1.30 +- 0.01 | 0.549 +- 0.167 | 631.0 +- 291.5 | 1591.3 +- 30.0 |
| 0.2 | 1.0 | 0.5 | 3 | 0.317 +- 0.010 | 0.140 +- 0.009 | 0.675 +- 0.008 | 1.30 +- 0.01 | 0.293 +- 0.006 | 1114.0 +- 102.0 | 1598.0 +- 29.5 |
| 0.2 | 3.0 | 0.0 | 3 | 0.352 +- 0.057 | 0.227 +- 0.078 | 0.659 +- 0.024 | 3.60 +- 0.02 | 0.492 +- 0.125 | 830.7 +- 286.5 | 1740.7 +- 38.5 |
| 0.2 | 3.0 | 0.5 | 3 | 0.254 +- 0.010 | 0.114 +- 0.009 | 0.602 +- 0.013 | 3.61 +- 0.02 | 0.286 +- 0.011 | 1324.7 +- 162.5 | 1749.7 +- 43.5 |
| 0.3 | 0.0 | 0.0 | 3 | 0.349 +- 0.014 | 0.180 +- 0.014 | 0.600 +- 0.007 | 0.04 +- 0.01 | 0.343 +- 0.011 | 913.7 +- 58.5 | 2042.3 +- 48.0 |
| 0.3 | 0.0 | 0.5 | 3 | 0.296 +- 0.004 | 0.130 +- 0.004 | 0.551 +- 0.007 | 0.05 +- 0.01 | 0.260 +- 0.010 | 1342.0 +- 92.5 | 2050.0 +- 50.0 |
| 0.3 | 1.0 | 0.0 | 3 | 0.325 +- 0.009 | 0.168 +- 0.009 | 0.598 +- 0.011 | 1.30 +- 0.01 | 0.362 +- 0.037 | 955.0 +- 75.5 | 2049.0 +- 39.5 |
| 0.3 | 1.0 | 0.5 | 3 | 0.245 +- 0.021 | 0.096 +- 0.017 | 0.535 +- 0.008 | 1.31 +- 0.01 | 0.223 +- 0.021 | 1502.0 +- 127.0 | 2047.3 +- 34.0 |
| 0.3 | 3.0 | 0.0 | 3 | 0.274 +- 0.002 | 0.150 +- 0.002 | 0.543 +- 0.013 | 3.60 +- 0.01 | 0.355 +- 0.020 | 1064.3 +- 134.5 | 2119.7 +- 35.5 |
| 0.3 | 3.0 | 0.5 | 3 | 0.195 +- 0.019 | 0.077 +- 0.016 | 0.482 +- 0.013 | 3.61 +- 0.02 | 0.207 +- 0.023 | 1570.0 +- 169.0 | 2117.0 +- 31.5 |

## E5 parameters (flock, real detections, matched rows)

| max_age | tentative_threshold | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|
| 5 | 2 | 0.271 | 0.588 | -0.073 | 1.79 | 0.176 | 175 | 413 |
| 5 | 3 | 0.271 | 0.595 | -0.069 | 1.78 | 0.176 | 164 | 392 |
| 5 | 5 | 0.273 | 0.616 | -0.059 | 1.71 | 0.178 | 125 | 347 |
| 15 | 2 | 0.271 | 0.584 | -0.070 | 1.81 | 0.177 | 151 | 423 |
| 15 | 3 | 0.271 | 0.587 | -0.067 | 1.80 | 0.178 | 147 | 416 |
| 15 | 5 | 0.273 | 0.602 | -0.058 | 1.76 | 0.180 | 126 | 387 |
| 30 | 2 | 0.272 | 0.590 | -0.072 | 1.81 | 0.178 | 159 | 423 |
| 30 | 3 | 0.273 | 0.594 | -0.069 | 1.80 | 0.180 | 156 | 416 |
| 30 | 5 | 0.275 | 0.614 | -0.063 | 1.74 | 0.182 | 138 | 382 |
| 60 | 2 | 0.272 | 0.590 | -0.072 | 1.81 | 0.178 | 159 | 423 |
| 60 | 3 | 0.273 | 0.594 | -0.069 | 1.80 | 0.180 | 156 | 416 |
| 60 | 5 | 0.275 | 0.614 | -0.063 | 1.74 | 0.182 | 138 | 382 |

## E5 parameters (turbine, real detections, matched rows)

| max_age | tentative_threshold | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|
| 5 | 2 | 0.494 | 0.451 | 0.278 | 0.49 | 0.449 | 1 | 3 |
| 5 | 3 | 0.515 | 0.452 | 0.407 | 0.48 | 0.475 | 1 | 3 |
| 5 | 5 | 0.530 | 0.453 | 0.485 | 0.46 | 0.495 | 1 | 3 |
| 15 | 2 | 0.661 | 0.824 | 0.249 | 0.49 | 0.703 | 0 | 3 |
| 15 | 3 | 0.685 | 0.821 | 0.373 | 0.48 | 0.738 | 0 | 3 |
| 15 | 5 | 0.711 | 0.824 | 0.477 | 0.46 | 0.770 | 0 | 3 |
| 30 | 2 | 0.656 | 0.824 | 0.228 | 0.49 | 0.697 | 0 | 3 |
| 30 | 3 | 0.682 | 0.821 | 0.361 | 0.48 | 0.734 | 0 | 3 |
| 30 | 5 | 0.710 | 0.824 | 0.473 | 0.46 | 0.769 | 0 | 3 |
| 60 | 2 | 0.656 | 0.824 | 0.228 | 0.49 | 0.697 | 0 | 3 |
| 60 | 3 | 0.682 | 0.821 | 0.361 | 0.48 | 0.734 | 0 | 3 |
| 60 | 5 | 0.710 | 0.824 | 0.473 | 0.46 | 0.769 | 0 | 3 |

## Sensitivity to the match distance (matched rows)

| run | px | HOTA | AssA | MOTA | MOTP px | IDF1 | IDSW | Frag |
|---|---|---|---|---|---|---|---|---|
| flock/real_default | 4 | 0.251 | 0.628 | -0.116 | 1.02 | 0.163 | 104 | 265 |
| flock/real_default | 6 | 0.264 | 0.614 | -0.089 | 1.42 | 0.174 | 135 | 352 |
| flock/real_default | 8 | 0.273 | 0.594 | -0.069 | 1.80 | 0.180 | 156 | 416 |
| flock/real_default | 12 | 0.283 | 0.577 | -0.024 | 2.91 | 0.193 | 173 | 474 |
| flock/gt_default | 4 | 0.961 | 0.932 | 0.993 | 0.01 | 0.972 | 17 | 116 |
| flock/gt_default | 6 | 0.962 | 0.933 | 0.993 | 0.01 | 0.972 | 17 | 116 |
| flock/gt_default | 8 | 0.962 | 0.934 | 0.993 | 0.01 | 0.973 | 17 | 116 |
| flock/gt_default | 12 | 0.962 | 0.942 | 0.993 | 0.05 | 0.974 | 18 | 115 |
| turbine/real_default | 4 | 0.652 | 0.782 | 0.353 | 0.46 | 0.731 | 0 | 3 |
| turbine/real_default | 6 | 0.675 | 0.811 | 0.361 | 0.48 | 0.734 | 0 | 3 |
| turbine/real_default | 8 | 0.682 | 0.821 | 0.361 | 0.48 | 0.734 | 0 | 3 |
| turbine/real_default | 12 | 0.707 | 0.850 | 0.361 | 0.48 | 0.734 | 0 | 3 |
| turbine/gt_default | 4 | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |
| turbine/gt_default | 6 | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |
| turbine/gt_default | 8 | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |
| turbine/gt_default | 12 | 0.992 | 0.992 | 0.992 | 0.00 | 0.996 | 0 | 0 |
