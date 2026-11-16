#!/usr/bin/env python3
"""build_srt.py — full-text caption track for this reel, on the measured clock (not staged, not published).
Windows come from the sheet's per-beat render_duration_s (falling back to actual_duration_s) in order; each beat's FULL
narration_text is split into cues of at most ~84 characters, proportional by word count. DISPLAY maps audio-only
respellings in narration_text back to their written form (the course number is spoken 'INFO seventy-three seventy-five')."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
slug = HERE.name
sheet = json.load(open(HERE / "beat_sheet.json"))
DISPLAY = {"INFO seventy-three seventy-five": "INFO 7375"}
MAX = 84
def s2t(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); mi, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{mi:02d}:{s:02d},{ms:03d}"
out, n, t0 = [], 0, 0.0
for beat in sheet["beats"]:
    d = float(beat.get("render_duration_s") or beat.get("actual_duration_s") or 0)
    text = beat.get("narration_text", "")
    for k, v in DISPLAY.items():
        text = text.replace(k, v)
    if text and d:
        lead = float(beat.get("lead_silence_s", 0) or 0) if beat["beat_id"] in ("BIDEA", "BVDT") else 0.0
        a = t0 + lead; z = t0 + d
        words = text.split(); chunks, cur = [], []
        for w in words:
            if cur and len(" ".join(cur + [w])) > MAX and (cur[-1][-1] in ".,;:?!" or len(" ".join(cur)) > MAX * 0.7):
                chunks.append(" ".join(cur)); cur = [w]
            else:
                cur.append(w)
        if cur: chunks.append(" ".join(cur))
        total = sum(len(c.split()) for c in chunks); t = a
        for c in chunks:
            dd = (z - a) * len(c.split()) / total; n += 1
            out.append(f"{n}\n{s2t(t)} --> {s2t(min(t + dd, z) - 0.02)}\n{c}\n"); t += dd
    t0 += d
(HERE / f"{slug}.srt").write_text("\n".join(out))
print(f"[srt] {n} cues -> {slug}.srt")
