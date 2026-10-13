# benchmark/tests/

`.venv/bin/python -m pytest -q` from the repo root (pytest.ini points here and puts
`benchmark/` and `tracker_kit/` on the path). About 15 s.

| file | checks |
|---|---|
| `conftest.py` | fixtures with the three roots: repo, tracker kit, benchmark |
| `test_experiments.py` | degraded ground truth is deterministic and keeps the detector schema; the runner reproduces `tracker_kit/results/synthetic` byte for byte and reuses finished runs |
| `test_library_trackers.py` | each Roboflow tracker returns the input boxes with stable ids; the runner records the algorithm in the manifest |
| `test_clips_and_renderers.py` | every clip in `clips.json` has its files; the track image renderer draws every track at the requested size |
| `test_run_birdeval.py` | the bridge maps run names to experiments and rows to birdeval row types without changing a box |

The team evaluator has its own tests: `pytest -q evaluationScripts/tests`.
