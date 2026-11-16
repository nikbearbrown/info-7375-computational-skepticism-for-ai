#!/usr/bin/env python3
"""deck_driver.py - drive one glossary terminology deck in headless Chromium on a VIRTUAL clock.

The decks animate with D3 transitions, which read performance.now() and wake on
requestAnimationFrame. An init script replaces both (and setTimeout / setInterval) with a
clock this driver advances by hand, so every frame of every animation is reproducible and
a screenshot can be taken at an exact time. Nothing in the deck file is changed.

The deck keeps its state inside a closure, so it is driven the way a person drives it:
ArrowRight adds one step, and at the last step moves to the next slide (step 0).
"""
from __future__ import annotations

import json
from pathlib import Path

SHIM = r"""
(() => {
  let now = 0, seq = 1, rafQ = [], timers = [];
  performance.now = () => now;
  const realDate = Date.now.bind(Date), t0 = realDate();
  Date.now = () => t0 + now;
  window.requestAnimationFrame = cb => { const i = seq++; rafQ.push([i, cb]); return i; };
  window.cancelAnimationFrame = i => { rafQ = rafQ.filter(r => r[0] !== i); };
  window.setTimeout = (cb, ms, ...a) => { const i = seq++; timers.push({ i, t: now + (+ms || 0), cb, a }); return i; };
  window.clearTimeout = i => { timers = timers.filter(t => t.i !== i); };
  window.setInterval = (cb, ms, ...a) => { const i = seq++; timers.push({ i, t: now + (+ms || 0), cb, a, every: Math.max(1, +ms || 0) }); return i; };
  window.clearInterval = window.clearTimeout;
  window.__vnow = () => now;
  window.__advance = dt => {
    const target = now + dt;
    for (;;) {
      const due = timers.filter(t => t.t <= target).sort((a, b) => a.t - b.t || a.i - b.i)[0];
      if (!due) break;
      now = Math.max(now, due.t);
      if (due.every) due.t += due.every; else timers = timers.filter(t => t.i !== due.i);
      try { if (typeof due.cb === "function") due.cb(...due.a); } catch (e) { console.error(e); }
    }
    now = target;
    const q = rafQ; rafQ = [];
    for (const r of q) { try { r[1](now); } catch (e) { console.error(e); } }
  };
  window.__key = k => document.dispatchEvent(new KeyboardEvent("keydown", { key: k, bubbles: true }));
  window.__busy = () => {
    const s = document.querySelector(".slide.is-active");
    if (!s) return false;
    for (const n of s.querySelectorAll("*")) if (n.__transition) return true;
    return false;
  };
  window.__state = () => {
    const s = document.querySelector(".slide.is-active");
    const all = Array.from(document.querySelectorAll("#deck .slide"));
    return { slide: all.indexOf(s), total: all.length,
             steps: document.querySelectorAll("#pips .pip").length,
             step: document.querySelectorAll("#pips .pip.on").length };
  };
})();
"""

# Hide the viewer chrome (prev / next buttons). The slide itself is untouched.
CHROME_CSS = "#controls,#notes,#thumbs{display:none !important} html,body{background:#FFFFFF !important}"

TEXTS_JS = r"""
() => {
  const s = document.querySelector(".slide.is-active");
  const clean = t => (t || "").replace(/\s+/g, " ").trim();
  const html = sel => { const n = s.querySelector(sel); return n ? clean(n.textContent) : ""; };
  const texts = [];
  for (const t of s.querySelectorAll("svg text")) {
    const ts = t.querySelectorAll("tspan");
    const v = ts.length ? clean(Array.from(ts).map(x => x.textContent).join(" ")) : clean(t.textContent);
    if (v) texts.push(v);
  }
  const svg = s.querySelector("svg");
  return { title: s.getAttribute("data-title") || "", eyebrow: html(".eyebrow"), evidence: html(".evidence"),
           source: html(".source"), notes: html(".speaker-notes"), texts,
           aria: svg ? (svg.getAttribute("aria-label") || "") : "",
           desc: svg && svg.querySelector("desc") ? clean(svg.querySelector("desc").textContent) : "" };
}
"""


class Deck:
    """One open deck. Use as a context manager."""

    def __init__(self, pw, html: Path, scale: int = 2):
        self.html = Path(html)
        self.browser = pw.chromium.launch(headless=True, args=["--force-color-profile=srgb", "--hide-scrollbars"])
        self.ctx = self.browser.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=scale,
                                            color_scheme="light", reduced_motion="no-preference")
        self.ctx.add_init_script(SHIM)
        self.page = self.ctx.new_page()
        self.errors: list[str] = []
        self.page.on("pageerror", lambda e: self.errors.append(str(e)))
        self.page.goto(self.html.resolve().as_uri(), wait_until="load", timeout=60_000)
        self.page.add_style_tag(content=CHROME_CSS)
        if not self.page.evaluate("typeof window.d3 !== 'undefined'"):
            raise RuntimeError("D3 did not load; the deck cannot draw")
        self.page.evaluate("document.fonts.ready.then(() => true)")
        fonts = self.page.evaluate("Array.from(document.fonts).filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight)")
        if not any("Lato" in f for f in fonts):
            raise RuntimeError(f"Lato did not load (loaded: {fonts}); the capture would use a fallback face")
        self.page.evaluate("window.dispatchEvent(new Event('resize'))")
        self.cdp = self.ctx.new_cdp_session(self.page)

    def close(self):
        self.ctx.close()
        self.browser.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    # -- driving ---------------------------------------------------------
    def state(self) -> dict:
        return self.page.evaluate("window.__state()")

    def next(self):
        """One ArrowRight: the next step, or the next slide at step 0."""
        self.page.evaluate("window.__key('ArrowRight')")

    def advance(self, ms: float):
        self.page.evaluate("dt => window.__advance(dt)", ms)

    def busy(self) -> bool:
        return self.page.evaluate("window.__busy()")

    def settle(self, limit_ms: float = 20000, dt: float = 1000 / 24) -> float:
        """Advance until no D3 transition is left on the slide. Returns the time it took (ms)."""
        t = 0.0
        while t < limit_ms:
            self.advance(dt)
            t += dt
            if not self.busy():
                return t
        raise RuntimeError(f"animation did not finish within {limit_ms} ms at {self.state()}")

    def texts(self) -> dict:
        return self.page.evaluate(TEXTS_JS)

    def shot(self, quality: int = 95) -> bytes:
        import base64
        r = self.cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": quality, "optimizeForSpeed": True})
        return base64.b64decode(r["data"])

    def goto_step(self, slide: int, step: int):
        """Walk forward from wherever the deck is to (slide, step). Forward only."""
        guard = 0
        while True:
            st = self.state()
            if (st["slide"], st["step"]) == (slide, step):
                return
            if (st["slide"], st["step"]) > (slide, step):
                raise RuntimeError(f"deck is past the requested position: at {st}, wanted {(slide, step)}")
            self.next()
            guard += 1
            if guard > 400:
                raise RuntimeError("could not reach the requested step")


def dump(obj, path: Path):
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")
