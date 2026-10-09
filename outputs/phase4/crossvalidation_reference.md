# Cross-validation against spoorpredictioneval.evaluate_track_quality (center_distance)

| case | px | IDF1 ref | IDF1 ours | IDTP ref/ours | switches ref/ours | only ref | only ours | frag ref/ours | frames with 2 cand near 1 obj | frames with 2 obj near 1 cand |
|---|---|---|---|---|---|---|---|---|---|---|
| flock E3 gt-as-detections, matched rows | 4 | 0.9673 | 0.9725 | 9786/9838 | 87/17 | 70 | 0 | 7/7 | 80 | 80 |
| flock E3 gt-as-detections, matched rows | 8 | 0.9673 | 0.9730 | 9786/9843 | 87/17 | 70 | 0 | 7/7 | 182 | 183 |
| flock real_default, matched rows, overlay ignored | 4 | 0.1627 | 0.1628 | 1135/1136 | 104/104 | 0 | 0 | 266/266 | 0 | 2 |
| flock real_default, matched rows, overlay ignored | 8 | 0.1790 | 0.1797 | 1249/1254 | 156/156 | 0 | 0 | 419/415 | 0 | 35 |
| flock baseline (6 col), all rows, overlay ignored | 4 | 0.1426 | 0.1426 | 1147/1147 | 154/154 | 1 | 1 | 324/324 | 6 | 3 |
| flock baseline (6 col), all rows, overlay ignored | 8 | 0.1596 | 0.1605 | 1284/1291 | 241/227 | 19 | 5 | 474/469 | 30 | 45 |
| turbine baseline, all rows, frames 53..293 | 4 | 0.4440 | 0.4440 | 212/212 | 0/0 | 0 | 0 | 3/3 | 0 | 0 |
| turbine baseline, all rows, frames 53..293 | 8 | 0.4503 | 0.4503 | 215/215 | 0/0 | 0 | 0 | 4/4 | 0 | 0 |

## Explanation of differences

- IDF1: the reference computes IDTP from its per-frame greedy one-to-one matches; TrackEval's Identity counts every pair within threshold as a potential match and solves one global assignment, so IDTP (and IDF1) can only be equal or higher on our side, and differs exactly when a frame has two candidates near one object or two objects near one candidate (last two columns).
- Identity switches: both count a change of the remembered candidate id per reference object across gaps. They differ only where the per-frame association differs: greedy nearest-first versus Hungarian with CLEAR's preference for the id that covered the object in the previous frame. The lists below give each such switch by (frame, reference id).
- Fragmentation: both count coverage interruptions that resume; differences come from the same association differences.

- flock E3 gt-as-detections, matched rows at 4 px: switches only in the reference (greedy): [(456, '79136'), (456, '79139'), (457, '79136'), (457, '79139'), (459, '79136'), (459, '79139'), (461, '79136'), (461, '79139'), (462, '79136'), (462, '79139'), (464, '79136'), (464, '79139'), (465, '79136'), (465, '79139'), (466, '79136')] ...; only in ours (Hungarian + continuation): []
- flock E3 gt-as-detections, matched rows at 8 px: switches only in the reference (greedy): [(456, '79136'), (456, '79139'), (457, '79136'), (457, '79139'), (459, '79136'), (459, '79139'), (461, '79136'), (461, '79139'), (462, '79136'), (462, '79139'), (464, '79136'), (464, '79139'), (465, '79136'), (465, '79139'), (466, '79136')] ...; only in ours (Hungarian + continuation): []
- flock baseline (6 col), all rows, overlay ignored at 4 px: switches only in the reference (greedy): [(526, '79128')]; only in ours (Hungarian + continuation): [(527, '79128')]
- flock baseline (6 col), all rows, overlay ignored at 8 px: switches only in the reference (greedy): [(180, '79135'), (190, '79135'), (258, '78899'), (356, '79097'), (357, '79097'), (361, '79098'), (362, '79098'), (388, '78897'), (422, '79116'), (464, '79098'), (513, '79132'), (514, '79132'), (526, '79128'), (529, '79116'), (532, '79122')] ...; only in ours (Hungarian + continuation): [(185, '79135'), (191, '79135'), (261, '78899'), (465, '79098'), (530, '79116')]

## Reading of the largest difference (E3, 87 reference switches versus 17 ours)

All 70 extra reference switches fall on frames 456..480 and on the two birds 79136 and 79139,
the pair that shares one identical box at frame 517: they fly within a few pixels of each other.
Greedy nearest-first matching re-decides each frame which candidate box is "nearest" to which
bird and flips the assignment back and forth, counting a switch on both birds every flip. The
Hungarian assignment with CLEAR's continuation bonus keeps each bird on the id that covered it
in the previous frame unless the distance gate forces otherwise, so it reports the tracker's own
swaps only (the 467..480 cluster). Both are faithful to their definitions; ours is the one that
measures the tracker rather than the scorer.
