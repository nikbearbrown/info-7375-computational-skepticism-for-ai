#!/usr/bin/env python3
"""
make_srt.py — caption track from the beat sheet's MEASURED windows.

Why this exists: the SRT beside the dignity reel emits ONE cue per beat, capped
at three wrapped lines, so a 17-second beat's narration is cut off mid-sentence
("...and it opens with") and the rest never reaches the caption track. A caption
that drops most of the sentence is worse than no caption — a deaf viewer gets a
fragment and no signal that anything is missing.

This splits each beat's narration into readable cues and distributes the beat's
measured duration across them in proportion to their length, so every spoken
word is captioned and the cues stay inside their own beat window. Source text
on measured windows — never an auto-transcription guess.
"""
import json, os, sys

MAX_LINE = 42      # characters per caption line
MAX_LINES = 2      # lines per cue
MIN_CUE = 1.2      # seconds — never flash a cue shorter than this


def wrap(text, width):
    lines, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def chunk(text):
    """Group wrapped lines into cues of at most MAX_LINES, breaking preferentially
    after sentence-final punctuation so a cue rarely straddles two sentences."""
    lines = wrap(text, MAX_LINE)
    cues, cur = [], []
    for ln in lines:
        cur.append(ln)
        ends_sentence = ln.rstrip().endswith(('.', '?', '!', '—', ':'))
        if len(cur) == MAX_LINES or (ends_sentence and len(cur) >= 1 and len(lines) > 1):
            cues.append("\n".join(cur)); cur = []
    if cur:
        cues.append("\n".join(cur))
    return cues or [text]


def ts(sec):
    if sec < 0:
        sec = 0
    h = int(sec // 3600); m = int((sec % 3600) // 60)
    s = int(sec % 60); ms = int(round((sec - int(sec)) * 1000))
    if ms == 1000:
        ms = 0; s += 1
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    sheet = json.load(open(os.path.join(here, "beat_sheet.json")))
    slug = sheet["metadata"]["slug"]

    out, idx, t = [], 1, 0.0
    for b in sheet["beats"]:
        dur = b.get("actual_duration_s")
        if not dur:
            sys.exit(f"{b['beat_id']}: no measured duration — run the audio step first")
        text = (b.get("narration_text") or "").strip()
        if not text:
            t += dur
            continue

        cues = chunk(text)
        weights = [max(1, len(c.replace("\n", " "))) for c in cues]
        total_w = sum(weights)
        # Leave a 50ms gap at the beat boundary so cues never bleed across a cut.
        span = max(0.1, dur - 0.05)

        start = t
        for c, w in zip(cues, weights):
            length = span * (w / total_w)
            end = min(start + length, t + span)
            if end - start < MIN_CUE and len(cues) == 1:
                end = t + span
            out.append(f"{idx}\n{ts(start)} --> {ts(end)}\n{c}\n")
            idx += 1
            start = end
        t += dur

    path = os.path.join(here, f"{slug}.srt")
    with open(path, "w") as f:
        f.write("\n".join(out))

    words_in = sum(len((b.get("narration_text") or "").split()) for b in sheet["beats"])
    words_out = sum(len(c.split()) for c in
                    [ln for blk in out for ln in blk.split("\n")[2:]])
    print(f"{path}")
    print(f"  {idx - 1} cues · {t:.1f}s · {words_in} narration words -> {words_out} captioned")
    if words_out < words_in:
        sys.exit("REFUSED: caption track dropped words — every spoken word must be captioned")


if __name__ == "__main__":
    main()
