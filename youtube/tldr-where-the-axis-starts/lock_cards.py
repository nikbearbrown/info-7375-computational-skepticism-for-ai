#!/usr/bin/env python3
"""lock_cards.py — after audio lock (and safe to re-run after make_sheet.py):
restores actual_duration_s from mp3/timings.json (BOUT from ffprobe of the padded
mp3), sets B00/B01/B03 durationSeconds = measured audio, and places the B00/B01
cues ON the spoken clauses (character position of each clause's anchor in the
narration × the measured duration, minus a small lead)."""
import json, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
p = HERE / "beat_sheet.json"; d = json.load(open(p))
T = json.load(open(HERE / "mp3" / "timings.json"))
def probe(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).decode())
ANCH = {"B00": ["This film is about", "A bar measures", "You'll watch", "The trap"],
        "B01": ["Why should you care", "Miss the floor", "Check it", "And it unlocks"]}
for b in d["beats"]:
    bid = b["beat_id"]
    b["audio_file"] = f"mp3/beat-{bid}.mp3"
    b["actual_duration_s"] = round(probe(HERE / b["audio_file"]), 2) if bid == "BOUT" else T[bid]
    dur = b["actual_duration_s"]
    if bid in ("B00", "B01", "B03"):
        props = b["shot"]["remotion"]["props"]; props["durationSeconds"] = round(dur, 2)
        if bid in ANCH:
            n = b["narration_text"]; L = len(n)
            cues = []
            for i, a in enumerate(ANCH[bid]):
                k = n.index(a); c = max(0.6, dur * k / L - 0.3)
                cues.append(round(c if i else (1.5 if bid == "B00" else 0.8), 2))   # the question / stake writes on from the start
            props["cues"] = cues
        print(bid, dur, props.get("cues"))
json.dump(d, open(p, "w"), indent=2, ensure_ascii=False); open(p, "a").write("\n")
print("BOUT", [b for b in d["beats"] if b["beat_id"] == "BOUT"][0]["actual_duration_s"])
