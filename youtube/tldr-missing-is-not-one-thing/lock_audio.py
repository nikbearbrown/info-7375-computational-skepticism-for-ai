#!/usr/bin/env python3
"""lock_audio.py — re-apply the audio lock to beat_sheet.json (run after make_sheet.py, once mp3s exist).
actual_duration_s from mp3/timings.json (BOUT from ffprobe of the 1.0 s-padded mp3); card durationSeconds
from the measured audio; B00/B01 cues on the spoken clauses (word positions in the measured narration)."""
import json, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
p = HERE / "beat_sheet.json"; d = json.load(open(p))
T = json.load(open(HERE / "mp3" / "timings.json"))
bout = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                      str(HERE / "mp3" / "beat-BOUT.mp3")]).decode().strip())
assert bout > T["BOUT"] + 0.9, "pad BOUT by 1.0 s first (ffmpeg apad)"
CUES = {"B00": [1.2, 7.7, 11.6, 16.5], "B01": [0.9, 5.4, 8.4, 13.0]}
for b in d["beats"]:
    i = b["beat_id"]
    b["actual_duration_s"] = round(bout, 3) if i == "BOUT" else T[i]
    b["audio_file"] = f"mp3/beat-{i}.mp3"
    if i in ("B00", "B01", "B03"):
        pr = b["shot"]["remotion"]["props"]; pr["durationSeconds"] = round(T[i], 2)
        if i in CUES: pr["cues"] = CUES[i]
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print("audio lock applied:", round(sum(b["actual_duration_s"] for b in d["beats"]), 2), "s")
