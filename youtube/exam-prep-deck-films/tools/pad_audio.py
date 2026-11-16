#!/usr/bin/env python3
"""pad_audio.py - add the silences the pictures need, without re-voicing anything.

    python3 pad_audio.py <reel-folder>

Three pads, all by appending silence to the existing mp3 and writing the new length into
beat_sheet.json and mp3/timings.json (the audio stays the clock):
  1. BOUT ends on 1.0 s of silence (lecture skill).
  2. A deck beat is never shorter than its own animation plus 1.2 s, so the settled picture is seen.
  3. A deck beat ends on at least 0.45 s of silence, and the LAST step of a slide on 0.9 s, so the
     finished slide holds for a breath before the cut to the next one.
Idempotent: a beat that already has its tail is left alone.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def probe(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True, check=True).stdout.strip())


def speech_end(p, total):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "silencedetect=noise=-45dB:d=0.12", "-f", "null", "-"],
                       capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    if starts and (len(starts) > len(ends) or abs(ends[-1] - total) < 0.15):
        return max(0.0, starts[-1])
    return total


def main():
    reel = Path(sys.argv[1]).resolve()
    sp = reel / "beat_sheet.json"
    sheet = json.loads(sp.read_text())
    tp = reel / "mp3" / "timings.json"
    timings = json.loads(tp.read_text()) if tp.exists() else {}
    beats = sheet["beats"]
    last_step = {}
    for b in beats:
        if b.get("deck"):
            last_step[b["deck"]["slide"]] = max(last_step.get(b["deck"]["slide"], 0), b["deck"]["step"])
    changed = 0
    tmpdir = Path(tempfile.mkdtemp())
    for b in beats:
        bid = b["beat_id"]
        if not b.get("audio_file"):
            raise SystemExit(f"{bid} is not voiced")
        mp3 = reel / b["audio_file"]
        total = probe(mp3)
        end = speech_end(mp3, total)
        if bid == "BOUT":
            target = end + 1.0
        elif b.get("deck"):
            tail = 0.9 if b["deck"]["step"] == last_step[b["deck"]["slide"]] else 0.45
            target = max(end + tail, b["deck"].get("anim_ms", 0) / 1000 + 1.2)
        else:
            continue
        if total >= target - 0.04:
            if abs((b.get("actual_duration_s") or 0) - total) > 0.03:
                b["actual_duration_s"] = round(total, 2)
                timings[bid] = round(total, 2)
                changed += 1
            continue
        tmp = tmpdir / f"{bid}.mp3"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), "-af", f"apad=whole_dur={target:.3f}", "-c:a", "libmp3lame", "-q:a", "2", str(tmp)], check=True)
        dur = round(probe(tmp), 2)
        shutil.copy(tmp, mp3)
        b["actual_duration_s"] = dur
        timings[bid] = dur
        changed += 1
        for rel in (f"media/{bid}.mp4", f"clips/{bid}.mp4"):
            f = reel / rel
            if f.is_file():
                f.unlink()          # a clip cut to the old length is stale; it is re-made from the deck
    sp.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    tp.write_text(json.dumps(timings, indent=2) + "\n")
    print(f"pad_audio: {changed} beat(s) padded; total {sum(b['actual_duration_s'] for b in beats):.1f} s")


if __name__ == "__main__":
    main()
