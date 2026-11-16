"""scenes.py — proxy; all 13 clips pre-rendered in manim/<BID>.mp4.
Satisfies run.sh's scenes.py presence check.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent / "manim"))
from scenes import *  # noqa: F401, F403
