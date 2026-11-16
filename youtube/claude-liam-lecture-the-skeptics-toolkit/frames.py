#!/usr/bin/env python3
"""frames.py <BID[@pct]> ... — extracts frames of the review cut at a beat's 50% (default) or given % into /private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/frames/"""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
OUT = Path("/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/frames"); OUT.mkdir(parents=True, exist_ok=True)
d = json.loads((HERE / "beat_sheet.json").read_text())
t0, start = 0.0, {}
for b in d["beats"]:
    dur = float(b.get("render_duration_s") or b["actual_duration_s"]); start[b["beat_id"]] = (t0, dur); t0 += dur
mp4 = next(HERE.glob("*-slate.mp4"))
for a in sys.argv[1:]:
    bid, _, pct = a.partition("@"); pct = float(pct or 50)
    s, dur = start[bid]
    out = OUT / f"{bid}_{int(pct)}.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{s + dur * pct / 100:.3f}", "-i", str(mp4), "-frames:v", "1", "-vf", "scale=1920:-1", str(out)], check=True)
    print(out)
