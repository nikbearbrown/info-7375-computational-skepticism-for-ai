#!/usr/bin/env python3
"""build_film.py - one deck film, from script to verified 4K master. Free and local; never publishes.

    python3 build_film.py NN [--from STAGE] [--to STAGE]

Stages, in order:  sheet  voice  pad  whisper  resheet  card  capture  review  final  checks
Every stage is safe to repeat. Results are appended to <reel>/BUILD-LOG.md.
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from films import BOOKS, TOOLKIT, film  # noqa: E402

TOOLS = Path(__file__).resolve().parent
STAGES = ["sheet", "voice", "pad", "whisper", "resheet", "card", "capture", "review", "final", "checks"]
SCRIPTS = TOOLKIT / "runtime" / "scripts"


def chrome():
    c = sorted(glob.glob(str(Path.home() / "Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))
    if not c:
        raise SystemExit("no Playwright headless shell found; not downloading a browser")
    return c[-1]


def run(cmd, log, cwd=BOOKS, env=None, ok=(0,)):
    t = time.time()
    e = dict(os.environ)
    e.update(env or {})
    p = subprocess.run([str(c) for c in cmd], cwd=cwd, env=e, capture_output=True, text=True)
    out = (p.stdout + p.stderr)
    tail = "\n".join(out.strip().splitlines()[-14:])
    log(f"`{' '.join(Path(str(c)).name if str(c).startswith('/') else str(c) for c in cmd[:4])} ...` exit {p.returncode}, {time.time() - t:.0f} s")
    if p.returncode not in ok:
        log("```\n" + "\n".join(out.strip().splitlines()[-40:]) + "\n```")
        raise SystemExit(f"FAILED: {' '.join(map(str, cmd))}\n{tail}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("nn")
    ap.add_argument("--from", dest="frm", default="sheet")
    ap.add_argument("--to", default="checks")
    a = ap.parse_args()
    F = film(a.nn)
    reel = F["reel"]
    reel.mkdir(parents=True, exist_ok=True)
    logp = reel / "BUILD-LOG.md"
    if not logp.exists():
        logp.write_text(f"# BUILD-LOG - {F['title']}\n\nBuilt end to end by Claude Code with `exam-prep-deck-films/tools/build_film.py` (Bear asked for the films, 2026-11-11).\n")

    def log(s):
        with logp.open("a") as f:
            f.write(s + "\n")
        print(s, flush=True)

    todo = STAGES[STAGES.index(a.frm):STAGES.index(a.to) + 1]
    log(f"\n## {datetime.now():%Y-%m-%d %H:%M} - stages: {', '.join(todo)}\n")
    sheet_path = reel / "beat_sheet.json"

    def sheet():
        return json.loads(sheet_path.read_text())

    for st in todo:
        if st in ("sheet", "resheet"):
            out = run(["python3", TOOLS / "make_film.py", a.nn], log)
            log("- " + out.strip().splitlines()[-1])
            run(["python3", "-c", "import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2])))",
                 sheet_path, TOOLKIT / "runtime/schema/beat_sheet.schema.json"], log)
            if st == "sheet":
                r = subprocess.run(["python3", TOOLKIT / "runtime/qc/factcheck_check.py", reel, "--quiet"], capture_output=True, text=True)
                log(f"- factcheck_check.py exit {r.returncode} (0 clean, 1 advisories, 2 blocker)")
                if r.returncode >= 2:
                    raise SystemExit(r.stdout + r.stderr)
        elif st == "voice":
            need = [b["beat_id"] for b in sheet()["beats"] if not b.get("audio_file") or not (reel / b["audio_file"]).is_file()]
            if need:
                run(["python3", SCRIPTS / "generate_audio_kokoro.py", reel, "--only", *need], log)
            s = sheet()
            missing = [b["beat_id"] for b in s["beats"] if not b.get("audio_file")]
            if missing:
                raise SystemExit(f"unvoiced beats: {missing}")
            log(f"- voiced {len(need)} beat(s); all {len(s['beats'])} beats have audio, {sum(b['actual_duration_s'] for b in s['beats']):.1f} s")
        elif st == "pad":
            log("- " + run(["python3", TOOLS / "pad_audio.py", reel], log).strip().splitlines()[-1])
        elif st == "whisper":
            out = run(["python3", TOOLS / "whisper_check.py", reel], log)
            log("- " + [l for l in out.splitlines() if l.startswith("whisper:")][-1])
        elif st == "card":
            # the six Northeastern bookends, drawn to the measured audio (Bear, 2026-11-12)
            out = run(["python3", TOOLS / "bookends.py", reel], log)
            log("- bookends: " + "; ".join(l for l in out.splitlines() if l.startswith("B") or l.startswith("portrait")))
        elif st == "capture":
            # a clip cut for an older take of the audio is stale: remove it so it is re-made at the measured length
            stale = []
            for b in sheet()["beats"]:
                bid = b["beat_id"]
                m = reel / "media" / f"{bid}.mp4"
                if m.exists():
                    pr = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(m)], capture_output=True, text=True)
                    try:
                        d = float(pr.stdout.strip())
                    except ValueError:
                        d = -1
                    if abs(d - b["actual_duration_s"]) > 0.07:
                        stale.append(bid)
                        m.unlink()
                        for extra in (reel / "clips" / f"{bid}.mp4", reel / "opening-title-card" / ".duration" if bid == "BOPEN" else None):
                            if extra and extra.exists():
                                extra.unlink()
            if stale:
                log(f"- removed {len(stale)} stale clip(s): {', '.join(stale[:12])}{' ...' if len(stale) > 12 else ''}")
                if any(x in stale for x in ("BOPEN", "BIDEA", "BDEFS", "BVDT", "BHTF", "BOUT")):
                    raise SystemExit("a bookend clip was stale; re-run from the card stage")
            out = run(["python3", TOOLS / "deck_capture.py", reel], log)
            for l in out.splitlines():
                if l.startswith("NOTE") or l.startswith("captured"):
                    log("- " + l)
        elif st == "review":
            out = run([TOOLKIT / "art", "run", reel, "--height", "2160"], log, env={"ART_CHROME": chrome()})
            for l in out.splitlines():
                if "GATE" in l or "BLOCKER" in l or "MAJOR" in l or "[run] done" in l:
                    log("- " + l.strip()[:300])
        elif st == "final":
            out = run([TOOLKIT / "art", "final", reel, "--local", "--height", "2160", "--out", reel / "exports" / "landscape"], log, env={"ART_CHROME": chrome()})
            for l in out.splitlines()[-12:]:
                log("- " + l.strip()[:300])
        elif st == "checks":
            # The toolkit's bookend_check looks for the Claude-palette Remotion bookends, which these films replaced
            # with Northeastern ones at Bear's request. Check the same structure here instead.
            sh = sheet()
            ids = [b["beat_id"] for b in sh["beats"]]
            want_first, want_last = ["BOPEN", "BIDEA", "BDEFS"], ["BVDT", "BHTF", "BOUT"]
            probs = []
            if ids[:3] != want_first or ids[-3:] != want_last:
                probs.append(f"bookend order {ids[:3]} ... {ids[-3:]}")
            bm = {b["beat_id"]: b for b in sh["beats"]}
            if not bm["BOPEN"]["narration_text"].startswith(f"{sh['metadata']['playlist']}. {sh['metadata']['title']}. "):
                probs.append("BOPEN does not say playlist then title")
            if not bm["BIDEA"]["narration_text"].startswith("Hallo. This is Liam, in for Bear."):
                probs.append("BIDEA greeting")
            if bm["BOUT"]["narration_text"] != f"{sh['metadata']['title']}. At Nik Bear Brown.":
                probs.append("BOUT narration")
            if len(sh["metadata"]["bookends"]["recap_lines"]) != 6:
                probs.append("recap is not six lines")
            if not all((reel / "media" / f"{x}.mp4").exists() for x in want_first + want_last):
                probs.append("a bookend clip is missing")
            class R: pass
            r = R(); r.returncode = 2 if probs else 0
            log(f"- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): {'PASS' if not probs else 'FAIL ' + '; '.join(probs)}")
            master = reel / "exports" / "landscape" / f"{F['slug']}.mp4"
            lr = subprocess.run(["python3", SCRIPTS / "loudness_check.py", reel, "--mp4", master], capture_output=True, text=True)
            log(f"- loudness_check exit {lr.returncode}: " + " | ".join(l.strip() for l in (lr.stdout + lr.stderr).strip().splitlines()[-3:])[:300])
            if not master.exists():
                raise SystemExit(f"no master at {master}")
            pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate:format=duration",
                                 "-of", "json", str(master)], capture_output=True, text=True)
            j = json.loads(pr.stdout)
            dur = float(j["format"]["duration"])
            audio = sum(b["actual_duration_s"] for b in sheet()["beats"])
            v = j["streams"][0]
            log(f"- master {master}: {v['width']}x{v['height']} at {v['r_frame_rate']}, {dur:.2f} s ({dur / 60:.1f} min); sum of audio {audio:.2f} s; "
                f"difference {dur - audio:+.2f} s; {master.stat().st_size / 1e6:.0f} MB")
            if (v["width"], v["height"]) != (3840, 2160) or abs(dur - audio) > 1.5 or r.returncode != 0 or lr.returncode not in (0, 3):
                raise SystemExit("final checks did not pass; see BUILD-LOG.md")
    log(f"- stages done: {', '.join(todo)}")


if __name__ == "__main__":
    main()
