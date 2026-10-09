# TrackEval bridge validation with IoU similarity

TrackEval commit 12c8791b303e0a0b50f753af204249e622d0281a; standard pipeline = Evaluator + MotChallenge2DBox on files from evaluation/adapters/motchallenge.py (DO_PREPROC off).

| case | HOTA std | HOTA ours | MOTA std | MOTA ours | IDF1 std | IDF1 ours | IDSW std/ours | fields compared | mismatches |
|---|---|---|---|---|---|---|---|---|---|
| turbine baseline (all rows) vs GT | 0.258301 | 0.258301 | -5.809129 | -5.809129 | 0.204556 | 0.204556 | 0/0 | 26 | 0 |
| flock baseline (all rows) vs GT | 0.197216 | 0.197216 | -0.547722 | -0.547722 | 0.112573 | 0.112573 | 4/4 | 26 | 0 |
| flock cloud vs GT | 0.205043 | 0.205043 | -0.152041 | -0.152041 | 0.126863 | 0.126863 | 10/10 | 26 | 0 |
| flock real_default matched rows vs GT | 0.222864 | 0.222864 | -0.213666 | -0.213666 | 0.139015 | 0.139015 | 2/2 | 26 | 0 |
| flock E3 gt-as-detections matched rows vs GT | 0.959052 | 0.959052 | 0.991816 | 0.991816 | 0.971482 | 0.971482 | 32/32 | 26 | 0 |
