"""Where things are: the repo root, the Spoor tracker kit and this benchmark folder.

Every script in ``benchmark/`` imports this first; it puts ``benchmark/`` (for ``evaluation`` and
``experiments``) and ``tracker_kit/`` (for ``tracker`` and ``run_tracker``) on ``sys.path``.
"""

from __future__ import annotations

import sys
from pathlib import Path

BENCH_ROOT = Path(__file__).resolve().parent
REPO_ROOT = BENCH_ROOT.parent
KIT_ROOT = REPO_ROOT / "tracker_kit"
OUTPUTS = BENCH_ROOT / "outputs"
RUNS = OUTPUTS / "runs"
REPORTS = OUTPUTS / "reports"

for path in (BENCH_ROOT, KIT_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
