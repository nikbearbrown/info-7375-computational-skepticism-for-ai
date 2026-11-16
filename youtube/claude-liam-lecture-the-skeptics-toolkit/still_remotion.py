#!/usr/bin/env python3
"""still_remotion.py <BEAT_ID> [<BEAT_ID> ...] — renders the 25% / 50% / 95% stills of Remotion beats from beat_sheet.json props
into /private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/remotion/<BID>_<pct>.png (look at them before any 4K render)."""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
RM = "/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion"
OUT = Path("/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/remotion"); OUT.mkdir(parents=True, exist_ok=True)
sheet = json.loads((HERE / "beat_sheet.json").read_text())
for bid in sys.argv[1:]:
    b = next(x for x in sheet["beats"] if x["beat_id"] == bid)
    r = b["shot"]["remotion"]; dur = float(b.get("actual_duration_s") or b["estimated_duration_s"])
    pf = OUT / f"{bid}_props.json"; pf.write_text(json.dumps(r["props"]))
    for pct in (25, 50, 95):
        frame = max(1, int(dur * 30 * pct / 100))
        png = OUT / f"{bid}_{pct}.png"
        p = subprocess.run(["npx", "remotion", "still", "src/index.ts", r["pattern"], str(png), f"--frame={frame}", f"--props={pf}", "--scale=1"],
                           cwd=RM, capture_output=True, text=True, timeout=300)
        print(bid, pct, "ok" if png.exists() else "FAILED\n" + p.stderr[-600:])
