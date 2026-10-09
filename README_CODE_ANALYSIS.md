# Spoor Tracker — Current Algorithm Analysis

This document explains how the current standalone **Spoor bird-watcher `SimpleSORTTracker`** works.

The goal is to describe the algorithm as it exists today, following the source code in the tracker kit. It does **not** propose improvements, discuss bugs, or compare against alternative trackers.

---

## 1. What the tracker does

The tracker receives two things:

```text
video
+
per-frame bird detections (bounding boxes)
```

The detector answers:

> “Is there a bird in this frame, and where is it?”

The tracker answers:

> “Which detections across different frames belong to the same real bird?”

That second problem is called **data association**.

The tracker assigns a persistent `track_id` to detections that it believes belong to the same bird.

Conceptually:

```text
Frame t detections
      ↓
Existing tracks
      ↓
Association
      ↓
Matched detection → update existing track
Unmatched detection → create new track
Unmatched track → keep alive or delete
      ↓
Predict next frame
```

The standalone kit operates in **2D image coordinates for one camera**. It does not perform stereo reconstruction or 3D tracking.

---

## 2. Source / provenance

According to `PROVENANCE.md`, the standalone tracker was copied from:

```text
libs/tracker/src/spoortracker/
```

at Spoor main commit:

```text
145fc6696241ec3ea1e1d3b930164bebf226538b
```

The kit isolates the bird-watcher tracker from the rest of the Spoor pipeline so it can run from a video and a detection CSV.

`tracker/shim.py` provides lightweight local replacements for internal Spoor bounding-box and detection classes.

This document describes the **bird-watcher `SimpleSORTTracker`** contained in this kit.

---

## 3. Important source files

| File | Responsibility |
|---|---|
| `run_tracker.py` | Loads the video and detections, calls the tracker once per frame, renders tracks, writes the output CSV |
| `tracker/simple_sort_tracker.py` | Main tracker lifecycle and per-frame orchestration |
| `tracker/matching.py` | Defines the two association stages |
| `tracker/nn_matching.py` | Nearest-neighbor feature-history metric used in Stage 1 |
| `tracker/distance_matching.py` | Predicted-position Euclidean matching used in Stage 2 |
| `tracker/linear_assignment.py` | Hungarian assignment, matching cascade and Kalman gating |
| `tracker/kalman_filter.py` | Constant-velocity Kalman filter |
| `tracker/kalman_tracker_state.py` | Stores Kalman state and feature history for a track |
| `tracker/tracked_object.py` | Stores track identity, detections, age and lifecycle state |
| `tracker/tracked_object_state.py` | Defines `TENTATIVE`, `CONFIRMED`, and `DELETED` |
| `tracker/shim.py` | Local bounding-box and detection classes |

---

# 4. High-level execution flow

The main tracking loop is:

```text
DETECTIONS FOR FRAME t
        │
        ▼
SimpleSORTTracker.match_and_track()
        │
        ▼
┌─────────────────────────────────────┐
│ Stage 1                             │
│ Confirmed-track association         │
│                                     │
│ historical feature distance         │
│ + Kalman/Mahalanobis gating         │
│ + Hungarian assignment              │
└─────────────────────────────────────┘
        │
        ▼
remaining tracks / detections
        │
        ▼
┌─────────────────────────────────────┐
│ Stage 2                             │
│ Remaining-track association         │
│                                     │
│ predicted position                  │
│ + Euclidean distance                │
│ + Hungarian assignment              │
└─────────────────────────────────────┘
        │
        ▼
Update matched tracks
Keep or delete unmatched tracks
Create tracks from unmatched detections
        │
        ▼
Predict every active track one frame forward
        │
        ▼
NEXT FRAME
```

`match_and_track()` must be called exactly once for every real video frame, including frames with no detections.

---

# 5. Input detections

`run_tracker.py` reads detections from a CSV.

The tracker works with a bounding box represented by:

```text
x
 y
 width
 height
```

where `x` and `y` are the top-left corner of the box.

For each detection, `run_tracker.py` also creates the tracking feature:

```python
feature = (int(box.x), int(box.y), float(box.area))
```

So the feature used by the current tracker is:

```text
(x, y, area)
```

where:

```text
x    = bounding-box top-left x
 y    = bounding-box top-left y
 area = width × height
```

The current tracker does not use a learned appearance/ReID embedding for association.

---

# 6. What a track contains

A tracked bird is represented primarily by `TrackedObject`.

Conceptually:

```text
TrackedObject
├── id
├── state
├── age
├── detections
└── kalman_tracker_state
```

The `TrackedObject` stores the identity and observation history.

Its `KalmanTrackerState` stores:

```text
Kalman mean
Kalman covariance
feature history
```

A useful mental model is:

```text
TrackedObject
= identity and history

KalmanTrackerState
= motion state and uncertainty
```

---

# 7. Track lifecycle

Tracks have three states:

```text
TENTATIVE
CONFIRMED
DELETED
```

The lifecycle is:

```text
new unmatched detection
        │
        ▼
    TENTATIVE
        │
        │ enough matched detections
        ▼
    CONFIRMED
        │
        │ too many consecutive misses
        ▼
      DELETED
```

The default confirmation threshold is:

```text
tentative_threshold = 3
```

The initial detection that creates the track counts as the first detection.

Example:

```text
Frame 10
new detection
→ create Track 4
→ detections = 1
→ TENTATIVE

Frame 11
match Track 4
→ detections = 2
→ TENTATIVE

Frame 12
match Track 4
→ detections = 3
→ CONFIRMED
```

An unmatched tentative track is removed immediately.

A confirmed track is allowed to survive missing detections until it reaches `max_age`.

Default:

```text
max_age = 30
```

Only confirmed tracks are rendered and written to the standalone output CSV.

---

# 8. Kalman filter state

The Kalman filter models the bounding box with the state:

```text
[cx, cy, a, h, vx, vy, va, vh]
```

where:

```text
cx = bounding-box center x
cy = bounding-box center y
a  = aspect ratio
h  = bounding-box height

vx = center-x velocity
vy = center-y velocity
va = aspect-ratio velocity
vh = height velocity
```

The motion model is **constant velocity**.

The time step is fixed to:

```text
dt = 1 frame
```

There is no elapsed-time value passed into the filter.

Example:

```text
Frame 20: bird center x = 100
Frame 21: bird center x = 110
Frame 22: bird center x = 120
```

The Kalman filter can infer forward motion and predict something approximately like:

```text
Frame 23 prediction: x ≈ 130
```

If there is no detection in frame 23, the tracker can still continue predicting the track's motion.

---

# 9. Kalman predict and update

The Kalman filter is used in two main operations.

## Predict

`predict()` advances the track state one frame forward according to the motion model.

Conceptually:

```text
current estimated state
        ↓
constant-velocity model
        ↓
predicted next-frame state
```

## Update

When a detection is matched to a track, the Kalman filter is corrected toward the observed bounding box.

Conceptually:

```text
Kalman prediction
       X

Detector observation
          O

       ↓ update

corrected state between prediction and observation
```

The amount of correction depends on the filter's current uncertainty and measurement model.

---

# 10. Timing of prediction

An important implementation detail is that every surviving track is predicted at the **end** of `match_and_track()`.

So the order is:

```text
Frame t arrives
      ↓
associate detections
      ↓
correct matched tracks using frame-t observations
      ↓
predict every active track for frame t+1
      ↓
return
```

Therefore, after `match_and_track()` finishes processing frame `t`, the internal Kalman state is already predicted for the next frame.

This is why the method must be called once per frame and in chronological order.

---

# 11. Track age

Each track contains an `age` value.

A successful match resets age:

```text
age = 0
```

At the end of the frame, prediction increments the age.

Therefore, on the next frame a track that was just successfully observed normally appears with:

```text
age = 1
```

As detections are missed, the age increases:

```text
age 1
age 2
age 3
...
```

The age is used to prioritize recent tracks and determine when an unmatched track should be deleted.

---

# 12. Association overview

The current tracker uses **two matching stages**.

```text
existing tracks
      │
      ├── confirmed tracks
      │       ↓
      │     Stage 1
      │
      └── tentative tracks
              │
              └──────────────┐
                             ▼
                    remaining tracks
                             ↓
                           Stage 2
```

Stage 1 is attempted first for confirmed tracks.

Stage 2 handles the tracks and detections that remain unresolved.

---

# 13. Stage 1 — confirmed-track matching

Stage 1 is used for confirmed tracks.

The main ingredients are:

```text
historical tracking feature
+
Kalman/Mahalanobis gating
+
matching cascade
+
Hungarian assignment
```

The tracking feature is:

```text
(x, y, area)
```

Each confirmed track maintains a history of features from detections that were previously assigned to it.

For a new frame, the nearest-neighbor metric compares the current detection feature against stored samples for each existing track.

Conceptually:

```text
Track 7 historical features

(500, 800, 400)
(508, 804, 420)
(516, 808, 405)

           vs

Current detection
(525, 812, 410)
```

The resulting cost is used as the association cost for Stage 1.

---

# 14. Matching cascade

Stage 1 uses a **matching cascade**.

The cascade processes confirmed tracks according to how recently they were observed.

Example:

```text
Track A age 1
Track B age 1
Track C age 3
Track D age 5
```

The tracker first attempts to associate the most recent tracks:

```text
age 1
```

Then, using only remaining unmatched detections, it proceeds to older tracks:

```text
age 2
age 3
age 4
...
```

This gives recently observed tracks priority in association.

---

# 15. Mahalanobis gating

Before accepting Stage-1 candidates, the tracker applies Kalman-based gating.

This answers:

> “Given the track's predicted position and uncertainty, is this detection a plausible observation of the same object?”

The detection bounding box is converted into Kalman measurement space.

For the current Stage-1 gating call, only position is used:

```text
cx
cy
```

The code computes the squared Mahalanobis distance from the predicted Kalman state to the detection.

For two position dimensions, the 95% chi-square gating threshold used by the code is:

```text
5.9915
```

A detection outside the valid region receives an invalid/high cost and is not considered a valid association candidate.

Conceptually:

```text
        plausible region
      ...................
    ...                 ...
   ..        Track         ..
    ...                 ...
      ...................

inside → candidate
outside → gated out
```

---

# 16. Hungarian assignment

Once the Stage-1 cost matrix is built, the tracker performs one-to-one assignment with SciPy's Hungarian algorithm:

```python
scipy.optimize.linear_sum_assignment
```

Conceptually the tracker has a matrix like:

```text
            Detection 1   Detection 2   Detection 3
Track 1         cost          cost          cost
Track 2         cost          cost          cost
Track 3         cost          cost          cost
```

The Hungarian algorithm selects the set of track-detection pairs with the lowest total cost while preserving one-to-one matching.

This means:

```text
one detection → at most one track
one track     → at most one detection
```

within the assignment.

---

# 17. Stage 2 — predicted-position matching

After Stage 1, some tracks and detections may remain unmatched.

Stage 2 receives:

```text
unconfirmed tracks
+
confirmed tracks still unmatched after Stage 1
```

The current implementation in `distance_matching.py` uses Euclidean distance between:

```text
the Kalman-predicted bounding-box top-left position
```

and:

```text
the current detection bounding-box top-left position
```

The distance is:

```text
d = sqrt((x_track - x_detection)^2 +
         (y_track - y_detection)^2)
```

The resulting distance matrix is again solved with one-to-one assignment.

So Stage 2 can be summarized as:

```text
Where did Kalman predict this track would be now?

            vs

Where is the new detection now?
```

---

# 18. Why prediction helps bridge missing detections

Stage 2 compares the detection with the **current predicted position**, not simply with the last observed position.

Example:

```text
bird velocity ≈ 40 px/frame
last observed x = 100
```

If detections are missed:

```text
next prediction     x ≈ 140
next prediction     x ≈ 180
next prediction     x ≈ 220
```

When the bird is detected again near:

```text
x ≈ 222
```

the association distance is based on:

```text
220 ↔ 222
```

rather than:

```text
100 ↔ 222
```

This allows the tracker to maintain an identity across short gaps when the motion remains reasonably consistent with the Kalman model.

---

# 19. What happens to a matched track

When a detection is matched to an existing track, `TrackedObject.update()` performs the main update operations.

Conceptually:

```text
matched detection
      ↓
append detection to track history
      ↓
Kalman correction/update
      ↓
store detection feature
      ↓
reset track age
      ↓
possibly confirm tentative track
```

If the number of detections accumulated by a tentative track reaches `tentative_threshold`, its state becomes:

```text
CONFIRMED
```

---

# 20. Feature history

When a track receives a successful update, the detection feature is appended to the track's feature history:

```text
(x1, y1, area1)
(x2, y2, area2)
(x3, y3, area3)
...
```

For confirmed tracks, this feature history is supplied to the nearest-neighbor metric used by Stage 1.

The nearest-neighbor metric therefore represents each track using observations accumulated across previous matched frames.

---

# 21. What happens to unmatched tracks

After association, tracks that did not receive a detection are processed according to their lifecycle state.

### Tentative track

```text
TENTATIVE + unmatched
→ DELETED
```

Tentative tracks therefore require consistent early detections to survive.

### Confirmed track

```text
CONFIRMED + unmatched
```

may remain active while:

```text
age < max_age
```

During these missing frames, the Kalman filter continues predicting the track forward.

Once the age limit is reached, the track becomes:

```text
DELETED
```

---

# 22. What happens to unmatched detections

Every detection that remains unmatched after the association stages starts a new tentative track.

Conceptually:

```text
unmatched detection
      ↓
create new track ID
      ↓
initialize Kalman filter from detection bbox
      ↓
state = TENTATIVE
```

The track must then accumulate the required number of matched detections before becoming confirmed.

---

# 23. Track IDs

New track IDs are generated sequentially using `itertools.count()`.

Conceptually:

```text
0
1
2
3
4
...
```

Each `TrackedObject` keeps its assigned ID for its lifetime.

---

# 24. Complete per-frame order

The core `SimpleSORTTracker.match_and_track()` operation can be understood as:

```text
FRAME t detections arrive

        ↓

1. ASSOCIATION
   Stage 1
   Stage 2

        ↓

2. UPDATE MATCHED TRACKS
   append detection
   Kalman correction
   store feature
   reset age
   confirm when threshold reached

        ↓

3. PROCESS UNMATCHED TRACKS
   tentative → delete
   confirmed → keep or delete depending on age

        ↓

4. SPAWN NEW TRACKS
   every unmatched detection creates a tentative track

        ↓

5. UPDATE CONFIRMED-TRACK FEATURE MEMORY

        ↓

6. PREDICT EVERY ACTIVE TRACK
   Kalman moves state one frame forward
   age increases

        ↓

7. RETURN ACTIVE TRACKS
```

This order is central to understanding the implementation.

---

# 25. Full example: one bird

Consider a bird entering the image.

## Frame 0

Detector finds:

```text
Detection A
```

There are no tracks.

So:

```text
Detection A unmatched
→ create Track 0
→ TENTATIVE
→ detections = 1
```

Kalman is initialized and predicts the next frame.

---

## Frame 1

Detector finds:

```text
Detection B
```

Track 0 is still tentative, so it participates in Stage 2.

If Detection B is close enough to the Kalman-predicted position:

```text
Track 0 ↔ Detection B
```

The track now has:

```text
detections = 2
state = TENTATIVE
```

Kalman updates and predicts the next frame.

---

## Frame 2

Detector finds:

```text
Detection C
```

Track 0 matches again.

Now:

```text
detections = 3
```

With the default threshold:

```text
TENTATIVE → CONFIRMED
```

Track 0 can now be rendered and written to the standalone track output.

---

## Frame 3 — missed detection

No detection appears for the bird.

Track 0 remains alive because it is confirmed and has not exceeded `max_age`.

Kalman predicts its next position.

---

## Frame 4 — detection returns

The bird appears again.

Because Track 0 is confirmed, it first participates in Stage 1.

If it remains unmatched there, it can continue to Stage 2.

If the reappearing detection is associated with Track 0, the track keeps the same identity.

---

# 26. Rendering behavior

`run_tracker.py` renders only confirmed tracks.

For each confirmed track it draws:

```text
bounding box
track ID
trajectory dots
```

The trajectory dots come from the detections accumulated by that track.

Therefore the visible trail represents historical matched detector observations.

When a track is deleted, it is no longer rendered as an active track.

---

# 27. Bounding box used during missed detections

The standalone runner draws and writes:

```python
tracked_object.detections[-1].bounding_box
```

This is the **last matched detector bounding box** stored by the track.

The internal Kalman filter can continue predicting the track forward during missed detections, but the standalone visualization and CSV use the last real detection box for the active track.

Conceptually:

```text
internal tracker:
last observation → prediction → prediction → prediction

standalone rendered box:
last observation → same stored box → same stored box
```

The internal Kalman state and the rendered/output box should therefore be understood as related but distinct quantities during missing detections.

---

# 28. Standalone track CSV

The runner writes confirmed active tracks with:

```text
frame_number
track_id
x
y
w
h
```

Because only currently confirmed tracks are written, the first tentative observations of a new track are not retroactively inserted into the output CSV.

Example:

```text
Frame 50 → tentative
Frame 51 → tentative
Frame 52 → confirmed
```

The standalone CSV begins outputting that active track from the point at which it is confirmed.

---

# 29. Default tracker parameters

`SimpleSORTTracker` exposes three main constructor parameters.

| Parameter | Default | Meaning |
|---|---:|---|
| `euclidean_matching_threshold` | `250` | Distance threshold used by the association metric configuration |
| `max_age` | `30` | Number of missed-frame aging steps a confirmed track can tolerate before deletion |
| `tentative_threshold` | `3` | Number of accumulated detections needed for confirmation |

The Kalman process and measurement model are defined inside `kalman_filter.py` rather than exposed through the standalone CLI.

---

# 30. Synthetic sequence behavior

The included synthetic example contains three moving objects.

It tests behavior including:

```text
constant motion
crossing trajectories
short missing-detection gap
```

With the default parameters, the tracker keeps three track IDs in the supplied synthetic scenario.

This illustrates that the current motion prediction and association pipeline can maintain identities across clean constant-velocity motion, a short gap, and the generated crossing scenario.

---

# 31. Post-processing methods

`SimpleSORTTracker` also contains downstream methods including:

```text
filter_deleted_tracks()
concatenate_tracks()
```

The standalone `run_tracker.py` does not call these methods during the normal example runs.

It calls:

```text
match_and_track()
```

for every frame and finally:

```text
finalize_tracking()
```

Therefore the standalone annotated video and track CSV focus on the tracker's raw frame-by-frame behavior.

---

# 32. Track concatenation

The current `concatenate_tracks()` post-processing logic can join finished track fragments.

Conceptually it looks for another track that:

```text
starts after the current track ends
+
starts within a permitted time gap
+
starts within a permitted spatial distance
```

A nearby candidate can then be concatenated with the earlier trajectory.

Conceptually:

```text
Track A ends ●

       short gap

             ● Track B starts

       ↓

concatenate
```

This happens downstream of the frame-by-frame association logic.

---

# 33. Current tracker mental model

A compact way to remember the whole system is:

```text
DETECTOR
   │
   │ bounding boxes
   ▼
TRACKER
   │
   ├── existing confirmed tracks
   │       ↓
   │     Stage 1
   │     historical (x,y,area)
   │     + Mahalanobis gating
   │     + Hungarian assignment
   │
   └── remaining / tentative tracks
           ↓
         Stage 2
         predicted top-left position
         + Euclidean distance
         + one-to-one assignment

               ↓

          TRACK UPDATE

matched track
→ append observation
→ Kalman correction
→ reset age

unmatched confirmed track
→ remain alive temporarily
→ Kalman keeps predicting

unmatched tentative track
→ delete

unmatched detection
→ create new tentative track

               ↓

      PREDICT ALL ACTIVE TRACKS
        FOR THE NEXT FRAME
```

---

# 34. Five facts to remember

If only five implementation details are remembered, they should be these:

1. **The tracker is tracking-by-detection.** The detector provides independent boxes; the tracker links them through time.

2. **The current Stage-1 tracking feature is geometric:**

   ```text
   (top-left x, top-left y, bounding-box area)
   ```

3. **Stage 1 and Stage 2 are different:**

   ```text
   Stage 1 → confirmed tracks, feature history + Kalman gating
   Stage 2 → remaining tracks, Kalman-predicted position + Euclidean distance
   ```

4. **Tracks follow a lifecycle:**

   ```text
   TENTATIVE → CONFIRMED → DELETED
   ```

5. **Kalman is predicted one frame forward at the end of every tracker call.**

---

# 35. Short technical description

A concise technical description of the implementation is:

> **Spoor's current bird-watcher `SimpleSORTTracker` is an online tracking-by-detection system using a constant-velocity Kalman filter and two-stage geometric data association. Confirmed tracks are first associated using nearest-neighbor history over `(x, y, area)` features with position-only Mahalanobis gating and one-to-one assignment. Remaining and tentative tracks are then associated using Euclidean distance between Kalman-predicted and detected top-left positions. Tracks progress through tentative, confirmed, and deleted lifecycle states, while confirmed tracks can survive short detection gaps through continued Kalman prediction.**

