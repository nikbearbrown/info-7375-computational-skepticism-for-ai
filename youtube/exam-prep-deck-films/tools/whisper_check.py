#!/usr/bin/env python3
"""whisper_check.py - listen to every voiced beat with faster-whisper and flag the ones that do not match their script.

    python3 whisper_check.py <reel-folder> [--threshold 0.86]

A hearing aid, not a verdict: it catches a truncated or garbled take and badly said terms. Numbers are
dropped from both sides before comparing, because Whisper writes spoken numbers as digits.
Writes <reel>/WHISPER-CHECK.md and prints the flagged beats. Exit 0 always.
"""
import argparse
import difflib
import json
import re
from pathlib import Path

NUMW = set("""zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
thirty forty fifty sixty seventy eighty ninety hundred thousand million billion point percent dollars dollar first second third""".split())


def norm(s):
    s = s.lower().replace("’", "'").replace("-", " ")
    toks = re.findall(r"[a-z']+|\d[\d,.]*", s)
    return [t.strip("'") for t in toks if t not in NUMW and not t[0].isdigit() and t.strip("'")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel")
    ap.add_argument("--threshold", type=float, default=0.86)
    a = ap.parse_args()
    from faster_whisper import WhisperModel
    reel = Path(a.reel).resolve()
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    rows, flagged = [], []
    for b in sheet["beats"]:
        if not b.get("audio_file"):
            continue
        segs, _ = model.transcribe(str(reel / b["audio_file"]), beam_size=1, language="en")
        heard = " ".join(s.text.strip() for s in segs)
        r = difflib.SequenceMatcher(None, norm(b["narration_text"]), norm(heard)).ratio()
        rows.append((b["beat_id"], r, heard))
        if r < a.threshold:
            flagged.append((b["beat_id"], r, b["narration_text"], heard))
    out = [f"# WHISPER-CHECK - {sheet['metadata']['title']}", "",
           f"{len(rows)} beats transcribed with faster-whisper base.en; {len(flagged)} below {a.threshold} similarity (numbers ignored). "
           "A flag means: listen to that beat. It is not proof of an error.", ""]
    for bid, r, want, heard in flagged:
        out += [f"## {bid} ({r:.2f})", "", f"- script: {want}", f"- heard:  {heard}", ""]
    (reel / "WHISPER-CHECK.md").write_text("\n".join(out) + "\n")
    (reel / "_whisper.json").write_text(json.dumps({bid: {"ratio": round(r, 3), "heard": h} for bid, r, h in rows}, indent=1))
    print(f"whisper: {len(rows)} beats, {len(flagged)} flagged, lowest {min(r for _, r, _ in rows):.2f}")
    for bid, r, want, heard in flagged:
        print(f"  {bid} {r:.2f}\n    script: {want}\n    heard:  {heard}")


if __name__ == "__main__":
    main()
