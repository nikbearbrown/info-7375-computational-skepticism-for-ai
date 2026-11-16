#!/usr/bin/env python3
"""build_srt.py: full-text caption track (SRT) from beat_sheet.json, on the narration clock (cumulative measured
durations, which the compiler also uses), with voice-only respellings mapped back to the true spelling.
Writes <slug>.srt beside this file. Does not stage or publish anything."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
sheet = json.loads((HERE / "beat_sheet.json").read_text())
MAP = [("INFO seventy-three seventy-five", "INFO 7375"), ("Koshee", "Cauchy"), ("I C M L", "ICML")]
def fix(t):
    for a, b in MAP: t = t.replace(a, b)
    return t
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
MAXC = 84; out = []; n = 0; t = 0.0
for b in sheet["beats"]:
    d = float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0)
    txt = fix(b.get("narration_text", "")).strip()
    lead = float(b.get("lead_silence_s") or 0)
    if txt:
        words = txt.split(); chunks = []; cur = []
        for w in words:
            if cur and len(" ".join(cur + [w])) > MAXC and (cur[-1][-1] in ".,;:?!" or len(" ".join(cur)) > MAXC * 0.7):
                chunks.append(" ".join(cur)); cur = [w]
            else: cur.append(w)
        if cur: chunks.append(" ".join(cur))
        total = sum(len(c.split()) for c in chunks); tt = t + lead; span = max(d - lead, 0.1)
        for c in chunks:
            dd = span * len(c.split()) / total; n += 1
            out.append(f"{n}\n{ts(tt)} --> {ts(min(tt + dd, t + d) - 0.02)}\n{c}\n"); tt += dd
    t += d
(HERE / f"{HERE.name}.srt").write_text("\n".join(out))
print(n, "cues,", round(t, 1), "s")
