#!/usr/bin/env python3
"""whisper_check.py — transcribe every narration mp3 (faster-whisper, local, free) and list what Liam
actually said next to what the sheet says, for the BOPEN order, numbers, acronyms and model names.
Writes WHISPER-CHECK.md. Usage: python3 whisper_check.py [BID ...]"""
import json, sys
from pathlib import Path
from faster_whisper import WhisperModel
HERE = Path(__file__).resolve().parent
sheet = json.loads((HERE / "beat_sheet.json").read_text())
only = set(sys.argv[1:])
model = WhisperModel("small.en", device="cpu", compute_type="int8")
rows = []
WATCH = ["Fable", "Opus", "Sonnet", "Haiku", "xhigh", "extra high", "Notebook", "five point", "four point",
         "dollar", "cents", "percent", "thousand", "point", "Cognition", "Devin", "Artificial Analysis", "API"]
for b in sheet["beats"]:
    bid = b["beat_id"]
    if only and bid not in only:
        continue
    segs, _ = model.transcribe(str(HERE / "mp3" / f"beat-{bid}.mp3"), beam_size=5, language="en")
    heard = " ".join(s.text.strip() for s in segs)
    rows.append((bid, b["narration_text"], heard))
    print(bid, "|", heard)
out = ["# WHISPER-CHECK — what Liam said (faster-whisper small.en, local)", "",
       "**What.** Every narration mp3 transcribed and set beside the sheet's text.",
       "**Why.** File existence proves nothing about speech: BOPEN order, numbers, acronyms and the model names must be heard right.",
       "**Found.** See the verdict lines at the end (written by hand after reading the table).", "",
       "| beat | sheet | heard |", "|---|---|---|"]
for bid, n, h in rows:
    out.append(f"| {bid} | {n} | {h} |")
(HERE / "WHISPER-CHECK.md").write_text("\n".join(out) + "\n")
