#!/usr/bin/env python3
"""deck_capture.py - film the deck's own animations, one clip per beat, timed to the measured narration.

    python3 deck_capture.py <reel-folder> [--only B0301 B0302 ...] [--force]

Reads <reel>/beat_sheet.json. Every beat that carries a `deck` block ({"slide": i, "step": k})
and a measured `actual_duration_s` gets <reel>/media/<beat_id>.mp4: 3840x2160, 24 fps, exactly as
long as the beat's audio. The clip starts on the frame the step is triggered, plays the step's D3
animation on a virtual clock (deck_driver.py), then holds the settled picture.

The deck is driven forward only, exactly as a presenter would press the arrow key. The first step
of a slide is triggered in the same instant the slide appears, so the "click to start" hint that
the deck shows at step 0 is never filmed. Free and local: Playwright + ffmpeg.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deck_driver import Deck  # noqa: E402

FPS = 24
DT = 1000.0 / FPS


def encode(frames: list[bytes], duration: float, out: Path):
    total = max(len(frames), round(duration * FPS))
    hold = max(0.0, (total - len(frames)) / FPS)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".part.mp4")
    vf = (f"tpad=stop_mode=clone:stop_duration={hold + 0.5:.3f},"
          "scale=3840:2160:flags=lanczos:in_range=full:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709,format=yuv420p")
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
           "-vf", vf, "-frames:v", str(total), "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "14",
           "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
           "-movflags", "+faststart", "-an", str(tmp)]
    p = subprocess.run(cmd, input=b"".join(frames), capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.decode()[-1500:])
    tmp.replace(out)
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    reel = Path(a.reel).resolve()
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    deck_file = Path(sheet["metadata"]["deck_file"])
    beats = [b for b in sheet["beats"] if b.get("deck")]
    beats.sort(key=lambda b: (b["deck"]["slide"], b["deck"]["step"]))
    log = []
    with sync_playwright() as pw, Deck(pw, deck_file, scale=2) as d:
        for b in beats:
            bid, slide, step = b["beat_id"], b["deck"]["slide"], b["deck"]["step"]
            dur = b.get("actual_duration_s")
            if not dur:
                raise SystemExit(f"{bid} has no measured audio; voice the film before capturing")
            out = reel / "media" / f"{bid}.mp4"
            # walk to the state just before this step (no screenshots, so nothing in between is filmed)
            st = d.state()
            if (st["slide"], st["step"]) != (slide, step - 1):
                d.goto_step(slide, step - 1)
            skip = out.exists() and not a.force and (not a.only or bid not in a.only)
            if a.only and bid not in a.only:
                skip = True
            d.next()                                   # trigger the step: animation at t = 0
            now = d.state()
            if (now["slide"], now["step"]) != (slide, step):
                raise SystemExit(f"{bid}: deck is at {now}, expected slide {slide} step {step}")
            if skip:
                d.settle()
                continue
            max_frames = round(dur * FPS)
            frames = [d.shot()]
            settled_for = 0
            while len(frames) < max_frames:
                d.advance(DT)
                frames.append(d.shot())
                if d.busy():
                    settled_for = 0
                else:
                    settled_for += 1
                    if settled_for >= 3:
                        break
            if d.busy():
                d.settle()                             # animation longer than the narration: finish it off-camera
                log.append(f"{bid}: animation outlasts its {dur:.2f} s narration (cut at the beat's end)")
            n = encode(frames, dur, out)
            print(f"{bid}  slide {slide} step {step}  {len(frames)} animated frames + hold = {n} frames ({n / FPS:.2f} s)", flush=True)
        if d.errors:
            raise SystemExit(f"page errors: {d.errors}")
    for line in log:
        print("NOTE", line)
    print(f"captured {len(beats)} deck beats into {reel / 'media'}")


if __name__ == "__main__":
    main()
