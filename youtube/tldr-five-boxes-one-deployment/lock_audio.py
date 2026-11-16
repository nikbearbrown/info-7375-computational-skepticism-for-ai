#!/usr/bin/env python3
"""lock_audio.py — re-apply the audio lock to beat_sheet.json (run after make_sheet.py, once mp3s exist
and BOUT is padded). actual_duration_s from mp3/timings.json (BOUT from ffprobe of the 1.0 s-padded mp3);
B00/B01/B03 durationSeconds = measured audio; B00/B01 cues on the spoken clauses (character position of each
clause's anchor in the narration × the measured duration, minus a small lead)."""
import json, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
p = HERE / "beat_sheet.json"; d = json.load(open(p))
T = json.load(open(HERE / "mp3" / "timings.json"))
def probe(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).decode())
bout = probe(HERE / "mp3" / "beat-BOUT.mp3")
assert bout > float(T["BOUT"]) + 0.9, "pad BOUT by 1.0 s first (ffmpeg apad)"
ANCH = {"B00": ["This film is about", "A requirement counts", "You'll watch", "The trap"],
        "B01": ["Why should you care", "Take the words", "Run the tests", "And it unlocks"]}
for b in d["beats"]:
    bid = b["beat_id"]
    b["audio_file"] = f"mp3/beat-{bid}.mp3"
    b["actual_duration_s"] = round(bout, 3) if bid == "BOUT" else float(T[bid])
    dur = b["actual_duration_s"]
    if bid in ("B00", "B01", "B03"):
        props = b["shot"]["remotion"]["props"]; props["durationSeconds"] = round(dur, 2)
        if bid in ANCH:
            n = b["narration_text"]; L = len(n); cues = []
            for i, a in enumerate(ANCH[bid]):
                k = n.index(a); c = max(0.6, dur * k / L - 0.3)
                cues.append(round(c if i else (1.5 if bid == "B00" else 0.8), 2))
            props["cues"] = cues
        print(bid, dur, props.get("cues"))
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print("audio lock applied:", round(sum(b["actual_duration_s"] for b in d["beats"]), 2), "s; BOUT", round(bout, 3))
