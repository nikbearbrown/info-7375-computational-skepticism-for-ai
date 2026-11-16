#!/usr/bin/env python3
"""assemble_scenes.py — kit.py + scenes_act*.py (+ the guard attach loop) -> scenes.py.
  python3 assemble_scenes.py [--out DIR] [--acts 1 2 3]     (default: write ./scenes.py from every scenes_act*.py)
Each act file contains ONLY beat classes `class B##_Name(Scene):` and act-prefixed helpers (a1_, a2_ ...); the kit is pasted once.
"""
import argparse, glob, re
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("--out", default="."); ap.add_argument("--acts", nargs="*")
a = ap.parse_args()
here = Path(__file__).resolve().parent
parts = [(here / "kit.py").read_text()]
files = sorted(glob.glob(str(here / "scenes_act*.py")))
if a.acts:
    files = [f for f in files if re.search(r"scenes_act(\d+)", f).group(1) in a.acts]
for f in files:
    parts.append(f"\n\n# {'═'*30} {Path(f).name} {'═'*30}\n" + Path(f).read_text())
parts.append("""

# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
import re as _re
for _n, _c in list(globals().items()):
    if isinstance(_c, type) and issubclass(_c, Scene) and _c is not Scene and _re.match(r"^B[A-Z0-9]+_", _n):
        _c.play = ST.play
""")
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
(out / "scenes.py").write_text("".join(parts))
print("wrote", out / "scenes.py", "from", [Path(f).name for f in files])
