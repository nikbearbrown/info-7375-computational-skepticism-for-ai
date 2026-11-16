#!/usr/bin/env python3
"""deck_extract.py - read one terminology deck: every slide, every click-step.

For each step it records the words on the slide, the words that step ADDED, how long the
step's animation runs, and a 1920x1080 still of the settled picture. This is what the
narration is written from and what FACTCHECK compares the narration against.

    python3 deck_extract.py "<deck>.html" <out-dir>

Writes <out-dir>/deck.json and <out-dir>/stills/sNN-kK.jpg. Changes nothing in the deck.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deck_driver import Deck, dump  # noqa: E402


def main():
    html, out = Path(sys.argv[1]), Path(sys.argv[2])
    stills = out / "stills"
    stills.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw, Deck(pw, html, scale=1) as d:
        total = d.state()["total"]
        slides = []
        for i in range(total):
            d.goto_step(i, 0)
            d.advance(2000)
            st = d.state()
            base = d.texts()
            slide = {"index": i, "title": base["title"], "eyebrow": base["eyebrow"], "evidence": base["evidence"],
                     "source": base["source"], "notes": base["notes"], "picture": base["desc"] or base["aria"],
                     "n_steps": st["steps"], "steps": []}
            prev = []
            if st["steps"] == 0:
                (stills / f"s{i:02d}-k0.jpg").write_bytes(d.shot(90))
            for k in range(1, st["steps"] + 1):
                d.next()
                anim_ms = d.settle()
                d.advance(500)
                t = d.texts()["texts"]
                seen = list(prev)
                new = []
                for x in t:
                    if x in seen:
                        seen.remove(x)
                    else:
                        new.append(x)
                name = f"s{i:02d}-k{k}.jpg"
                (stills / name).write_bytes(d.shot(90))
                slide["steps"].append({"k": k, "anim_ms": round(anim_ms), "new_texts": new, "all_texts": t, "still": f"stills/{name}"})
                prev = t
            slides.append(slide)
        if d.errors:
            raise SystemExit(f"page errors: {d.errors}")
    dump({"deck_file": str(html.resolve()), "n_slides": len(slides), "slides": slides}, out / "deck.json")
    n = sum(s["n_steps"] for s in slides)
    print(f"{html.name}: {len(slides)} slides, {n} steps, longest animation {max((st['anim_ms'] for s in slides for st in s['steps']), default=0)} ms")


if __name__ == "__main__":
    main()
