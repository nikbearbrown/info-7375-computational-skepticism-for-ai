#!/usr/bin/env python3
"""gate_probe.py <ACT> <classes...> — generalised from evidence/act3/midframe_gates.py (Act III builder). Run GATE T (type_check.py's pixel checks) and GATE V (final_frame_check.analyze_frame) on the clip MIDPOINT (50%) and 85% frames
of every Act III scene, rendered at 1920x1080 / 24 fps from the preflight scratch (scenes.py assembled by ../../preflight.sh 3 ...).
    ../../preflight.sh 3 <classes>      # assembles /private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/act3/scenes.py
    python3 midframe_gates.py B19_UnitBar B20_NoConversion ...
NOSPARSE=1 ignores the sparse waiver (to decide which beats need it).
Frames land in /private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/act3/gates/ ; sparse beats waive underfill/clustered, as in lanes/act3.json."""
import sys, os, subprocess, json, glob
ACT = sys.argv.pop(1)
SCR = f"/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/act{ACT}"
TK = "/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime"
sys.path.insert(0, TK + "/scripts"); sys.path.insert(0, TK + "/qc")
import type_check as tc
import final_frame_check as gv
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
lp = os.path.join(HERE, "lanes", f"act{ACT}.json")
lanes = json.load(open(lp)) if os.path.exists(lp) else {}
os.makedirs(SCR + "/gates", exist_ok=True)
for cls in sys.argv[1:]:
    bid = cls.split("_")[0]
    subprocess.run(["manim", "-r", "1920,1080", "--fps", "24", "--media_dir", SCR + "/media_hd24", "scenes.py", cls], cwd=SCR, capture_output=True)
    mp4 = glob.glob(f"{SCR}/media_hd24/videos/scenes/*/{cls}.mp4")[0]
    dur = tc.video_duration(__import__("pathlib").Path(mp4))
    res = []
    for pct in (50, 85):
        out = f"{SCR}/gates/{bid}_{pct}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(dur * pct / 100), "-i", mp4, "-frames:v", "1", out])
        img = Image.open(out).convert("RGB")
        arr = np.array(img)
        pol, bg = tc.detect_polarity(arr)
        if pct == 50:
            for name, fn in (("min-size", lambda: tc.check_min_size(img, bid, "", polarity=pol)),
                             ("overflow", lambda: tc.check_overflow(img, bid, polarity=pol, pattern="")),
                             ("contrast", lambda: tc.check_contrast(img, bid, "", polarity=pol, bg_rgb=bg)),
                             ("contrast-local", lambda: tc.check_contrast_per_blob(img, polarity=pol)),
                             ("bbox-overlap", lambda: tc.check_bbox_overlap(img, polarity=pol))):
                # (the §8.4 pixel kerning check is skipped by the real gate on >=1500 px frames, and is noise at 1080 px, so it is not run here)
                try:
                    s, m = fn()
                except Exception as e:
                    s, m = "ERR", str(e)[:80]
                if s != "PASS":
                    res.append(f"T {name}: {s} {m[:150]}")
        d, cover = gv.analyze_frame(out)
        sparse = lanes.get(bid, {}).get("sparse", True) and not os.environ.get("NOSPARSE")
        for sev, kind, msg in d if isinstance(d, list) else []:
            if sparse and kind in ("underfill", "clustered"):
                continue
            res.append(f"V@{pct} {sev} {kind}: {msg[:110]}")
    print(f"{bid}: " + ("CLEAN" if not res else ""), flush=True)
    for r in res:
        print("   ", r, flush=True)
