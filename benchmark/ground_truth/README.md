# benchmark/ground_truth/

Hand-labelled boxes and identities, the reference every tracker is scored against.

| file | what |
|---|---|
| `<clip>_reference_tracks_corrected.csv` | `frame_number, obj_id, x1, y1, x2, y2, bbox_size`: one labelled bird box per row, `obj_id` is the bird's identity, corners in pixels, frames 0-based |
| `<clip>_detections_corrected.csv` | the same boxes without identities, in the detector's schema (`frame_number, frame_timestamp, x, y, w, h, area, classifier_name`), so they can be fed to a tracker as "perfect detections" |
| `semrev_collision_..._176-196.mp4` | the semrev clip itself (the other two clips live in `tracker_kit/data/`); gitignored |
| `SHA256SUMS` | hashes of every file here; `shasum -a 256 -c SHA256SUMS` verifies them |

Clips: flock `20251012_164031_1DAC` (25 birds, first flock only), turbine `20250920_063942_6C42`
(one bird, frames 53..293), semrev (two birds). Flock and turbine came from
`tracker-kit-Changing/GT`; semrev was converted from Supervisely with `~/convert/supervisely_json_to_csv.py`.
