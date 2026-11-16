"""
Manim scenes for tldr-where-the-axis-starts (tldr skill — LEARN section 1, B10–B19).

One persistent object: the colleague's two-bar chart from the chapter's Exercise 1
(a CONSTRUCTED exercise — captioned "Exercise 1 · constructed" on the stage): Model A
92.1 %, Model B 94.3 %, the y-axis top fixed at 96 and ONE value that moves — the
axis floor. Every drawn height is H · (value − floor) / (96 − floor), so a bar's
height is its value minus the floor, stretched to fill the frame. B12 and B16 move
only the floor; the two printed values never change.

State factory: `_Chart(scene, title, f=…)` rebuilds the axis, the two bars, their
value labels, the right-column readouts (B looks ×· A · the values · the floor ·
the floor rail with its terracotta knob) at the previous beat's floor, so the last
frame of Bk is the first frame of Bk+1. Every label that changes is an
`always_redraw` Text (crisp at any sampled frame — GATE T samples the 50 % frame).

Numbers are asserted at import with exact fractions (FACTCHECK.md). INK text on the
cream stage; terracotta is the knob plus at most one dot or X per scene — never
text, never a line, never a bar, never a ring (GATE T). Explicit coords inside
±6.2 × ±3.3. Type floor 32 (titles 40). Captions ≤ 34 chars.

Pacing: the exemplar's `_TARGET` block plus `_until(self, phrase)` (from
tldr-both-audits-were-right): a reveal waits for the phrase's character share of the
measured narration, so motion lands on the word. BASE = 99 keeps the stretch at 1.
"""
import json as _json, os as _os
from fractions import Fraction as F
import numpy as np
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
DISCARD = "#A39E8E"                      # the part of a bar below the floor (thrown away) — dark enough for Gate V
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ Exercise 1 (exact) ═══════════
A_V, B_V, TOP_V, FLOOR_V = F("92.1"), F("94.3"), F(96), F(91)
def _looks(f): return (B_V - f) / (A_V - f)
assert (A_V - FLOOR_V, B_V - FLOOR_V) == (F("1.1"), F("3.3")) and _looks(FLOOR_V) == 3
assert B_V - A_V == F("2.2") and round(float(_looks(0)), 2) == 1.02
assert _looks(F("89.9")) == 2 and round(float(_looks(80)), 2) == 1.18 and _looks(92) == 23
A, B, TOP = float(A_V), float(B_V), float(TOP_V)

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}
_BASE_DEFAULT = 10.0

def _stretch_for(self):
    f = getattr(self, "_stretch", None)
    if f is None:
        target = _TARGET.get(type(self).__name__.split("_")[0], 0)
        base = getattr(self, "BASE", _BASE_DEFAULT) - 2.0
        f = 1.0 if not target or base <= 0 else max(1.0, min(1.8, (target - 2.0) / base))
        self._stretch = f
    return f

if not getattr(Scene.play, "_paced", False):
    _orig_play = Scene.play
    def _paced_play(self, *anims, **kw):
        if "run_time" in kw:
            kw["run_time"] = kw["run_time"] * _stretch_for(self)
        return _orig_play(self, *anims, **kw)
    _paced_play._paced = True
    Scene.play = _paced_play

def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0

def _until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured duration)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    t = target * n.index(phrase) / len(n) - lead
    gap = t - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)

def _finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(1.0, target - _elapsed(self)) if target else 2.0)

# ═══════════ text + mark helpers ═══════════
def _title(txt, size=40): return Text(txt, font=SERIF, color=INK, font_size=size).move_to([0, 3.0, 0])
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _cap(txt, x=3.3, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -3.05, 0])
def _m(tex, size=50, color=INK): return MathTex(tex, font_size=size, color=color)
def _x(x, y, s=0.18, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _dot(x, y, r=0.13): return Dot([x, y, 0], color=TERRA, radius=r)
def _check(x, y, s=0.16, color=INK):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.8, 0], color=color, stroke_width=6),
                  Line([x - s * 0.3, y - s * 0.8, 0], [x + s * 1.1, y + s * 0.9, 0], color=color, stroke_width=6))
def _fmt(f):
    s = f"{f:.1f}"
    return s[:-2] if s.endswith(".0") else s
def _fmtr(r):
    if r >= 9.95: return f"{r:.0f}"
    s = f"{r:.2f}"
    return s[:-1] if s.endswith("0") else s

# ═══════════ chart geometry ═══════════
AX, BASE_Y, H = -5.3, -2.3, 4.4            # y-axis x; floor line y; height of the 96 mark above the floor
TOP_Y = BASE_Y + H                          # 2.1
BASE_R = -1.1                               # right end of the floor line
XA, XB, BW = -4.2, -2.0, 1.0                # bar centres, bar width
RX0, RX1, RAIL_Y = 1.2, 5.8, -0.6           # floor rail: 0 … 96
def RX(f): return RX0 + f / TOP * (RX1 - RX0)
COL = 3.5                                   # right-column centre
ROW1, ROW2 = -1.7, -2.3                     # commentary rows

def _h(v, f): return max(0.004, H * (v - f) / (TOP - f))
def _bar(x, v, f, color=INK):
    h = _h(v, f)
    return Rectangle(width=BW, height=h, fill_color=color, fill_opacity=1, stroke_width=0).move_to([x, BASE_Y + h / 2, 0])


class _Chart:
    """The colleague's chart at axis floor f. `ft` is the one value that moves."""
    def __init__(self, scene, title, f=91.0, right=True, add=True):
        self.scene = scene
        self.ft = ValueTracker(f)
        self.t = _title(title)
        self.axis = Line([AX, BASE_Y, 0], [AX, TOP_Y + 0.2, 0], color=INK, stroke_width=3)
        self.base = Line([AX, BASE_Y, 0], [BASE_R, BASE_Y, 0], color=INK, stroke_width=3)
        self.ttick = Line([AX - 0.1, TOP_Y, 0], [AX + 0.1, TOP_Y, 0], color=INK, stroke_width=2)
        self.tlab = _t("96", 32, DIM).move_to([AX - 0.18, TOP_Y, 0], aligned_edge=RIGHT)
        self.flab = always_redraw(lambda: _t(_fmt(self.f()), 32).move_to([AX - 0.18, BASE_Y, 0], aligned_edge=RIGHT))
        self.bars = VGroup(always_redraw(lambda: _bar(XA, A, self.f())), always_redraw(lambda: _bar(XB, B, self.f())))
        self.vlabs = VGroup(always_redraw(lambda: _t("92.1%", 36).move_to([XA, BASE_Y + _h(A, self.f()) + 0.32, 0])),
                            always_redraw(lambda: _t("94.3%", 36).move_to([XB, BASE_Y + _h(B, self.f()) + 0.32, 0])))
        self.names = VGroup(_t("Model A", 32).move_to([XA, BASE_Y - 0.42, 0]), _t("Model B", 32).move_to([XB, BASE_Y - 0.42, 0]))
        self.cons = _t("Exercise 1 · constructed", 32, DIM).move_to([COL, 2.35, 0])
        self.chart = VGroup(self.axis, self.base, self.ttick, self.tlab, self.flab, self.bars, self.vlabs, self.names)
        self.right = right
        self.looks = always_redraw(lambda: _t(f"B looks {_fmtr(self.r())} × A", 44, bold=True).move_to([COL, 1.5, 0]))
        self.vals = _t("values: 92.1% and 94.3%", 36).move_to([COL, 0.8, 0])
        self.flr = always_redraw(lambda: _t(f"axis floor: {_fmt(self.f())}", 36).move_to([COL, 0.15, 0]))
        rail = Line([RX0, RAIL_Y, 0], [RX1, RAIL_Y, 0], color=INK, stroke_width=3)
        rt = VGroup(*[Line([RX(v), RAIL_Y - 0.1, 0], [RX(v), RAIL_Y + 0.1, 0], color=INK, stroke_width=2) for v in (0, TOP)])
        rl = VGroup(_t("0", 32, DIM).move_to([RX0, RAIL_Y - 0.42, 0]), _t("96", 32, DIM).move_to([RX1, RAIL_Y - 0.42, 0]))
        self.rail = VGroup(rail, rt, rl)
        self.knob = always_redraw(lambda: Dot([RX(self.f()), RAIL_Y, 0], color=TERRA, radius=0.16))
        self.panel = VGroup(self.looks, self.vals, self.flr, self.rail, self.knob)
        if add:
            scene.add(self.t, self.cons, self.chart)
            if right:
                scene.add(self.panel)
    def f(self): return float(self.ft.get_value())
    def r(self): f = self.f(); return (B - f) / (A - f)
    def to(self, f): return self.ft.animate.set_value(f)
    def top(self, v): return BASE_Y + _h(v, self.f())


# ═══════════ B10 — HOOK: the colleague's chart ═══════════
class B10_TheChart(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "The Colleague's Chart", add=False)
        self.add(c.t)
        self.wait(0.4)
        self.play(Create(c.axis), Create(c.base), Create(c.ttick), FadeIn(c.tlab), FadeIn(c.flab), FadeIn(c.cons), run_time=1.0)
        self.play(FadeIn(c.vals), FadeIn(c.flr), Create(c.rail[0]), FadeIn(c.rail[1]), FadeIn(c.rail[2]), GrowFromCenter(c.knob), run_time=0.8)
        _until(self, "Two models")
        self.play(FadeIn(c.names), run_time=0.5)
        _until(self, "Model A: ninety-two")
        self.play(GrowFromEdge(c.bars[0], DOWN), FadeIn(c.vlabs[0]), run_time=0.8)
        _until(self, "Model B: ninety-four")
        self.play(GrowFromEdge(c.bars[1], DOWN), FadeIn(c.vlabs[1]), run_time=0.8)
        _until(self, "three times as tall")
        self.play(FadeIn(c.looks), run_time=0.6)
        _until(self, "So is B three times better")
        q = _t("three times better?", 40).move_to([COL + 0.25, ROW1, 0])
        self.play(FadeIn(q), GrowFromCenter(_dot(COL - 2.2, ROW1)), run_time=0.6)
        _until(self, "Nothing on this chart")
        self.play(FadeIn(_cap("every label on it is correct")), run_time=0.5)
        _finish(self)


# ═══════════ B11 — INSTANCE: measure from the floor ═══════════
class B11_MeasureIt(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "Measure From The Floor")
        _until(self, "they start at ninety-one")
        self.play(GrowFromCenter(_dot(AX + 0.02, BASE_Y - 0.42)), run_time=0.5)
        _until(self, "So A's bar")
        ba = BraceBetweenPoints([XA + BW / 2 + 0.06, BASE_Y, 0], [XA + BW / 2 + 0.06, c.top(A), 0], direction=RIGHT, color=INK)
        self.play(GrowFromCenter(ba), FadeIn(_t("1.1", 32).move_to([XA + BW / 2 + 0.7, (BASE_Y + c.top(A)) / 2, 0])), run_time=0.7)
        self.play(FadeIn(_t("A: 92.1 minus 91 = 1.1", 32).move_to([COL, ROW1, 0])), run_time=0.5)
        _until(self, "B's is ninety-four")
        bb = BraceBetweenPoints([XB + BW / 2 + 0.06, BASE_Y, 0], [XB + BW / 2 + 0.06, c.top(B), 0], direction=RIGHT, color=INK)
        self.play(GrowFromCenter(bb), FadeIn(_t("3.3", 32).move_to([XB + BW / 2 + 0.7, (BASE_Y + c.top(B)) / 2, 0])), run_time=0.7)
        self.play(FadeIn(_t("B: 94.3 minus 91 = 3.3", 32).move_to([COL, ROW2, 0])), run_time=0.5)
        _until(self, "The eye isn't wrong")
        self.play(FadeIn(_cap("3.3 ÷ 1.1 = 3, from the floor")), run_time=0.5)
        _finish(self)


# ═══════════ B12 — INSTANCE: slide the floor down ═══════════
class B12_SlideDown(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "Slide The Floor")
        before = VGroup(*[DashedLine([x - BW / 2 - 0.12, c.top(v), 0], [x + BW / 2 + 0.12, c.top(v), 0], color=DIM, stroke_width=3)
                          for x, v in ((XA, A), (XB, B))])
        self.wait(0.3)
        _until(self, "the floor.")
        self.play(Create(before), run_time=0.6)
        _until(self, "Ninety.")
        self.play(c.to(90), run_time=0.7)
        self.play(c.to(80), run_time=0.9)
        self.play(c.to(50), run_time=1.0)
        self.play(c.to(0), run_time=1.2)
        _until(self, "Watch the labels")
        self.play(FadeIn(_t("the values never move", 32).move_to([COL, ROW1, 0])), run_time=0.5)
        _until(self, "until, on a zero floor")
        self.play(FadeIn(_t("zero floor: 94.3 ÷ 92.1 = 1.02", 32).move_to([COL, ROW2, 0])), run_time=0.5)
        _until(self, "Same data")
        self.play(FadeIn(_cap("same numbers, new picture")), run_time=0.5)
        _finish(self)


# ═══════════ B13 — NAIVE: every number is true ═══════════
class B13_EveryNumberTrue(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "Every Number Is True", f=0.0)
        self.play(c.to(91), run_time=1.2)
        self.play(FadeOut(c.panel), run_time=0.5)
        rows = [("92.1%  ·  true", 1.5, "Ninety-two point one: true"), ("94.3%  ·  true", 0.8, "Ninety-four point three: true"),
                ("axis 91 to 96  ·  true", 0.1, "An axis from")]
        _until(self, "Check it")
        for s, y, cue in rows:
            _until(self, cue)
            self.play(Create(_check(1.25, y)), FadeIn(_t(s, 36).move_to([1.75, y, 0], aligned_edge=LEFT)), run_time=0.6)
        _until(self, "and the eye still reads")
        self.play(FadeIn(_t("the eye reads × 3", 40, bold=True).move_to([1.75, -0.9, 0], aligned_edge=LEFT)), Create(_x(1.25, -0.9)), run_time=0.6)
        _until(self, "nobody printed that ratio")
        self.play(FadeIn(_t("printed nowhere on the chart", 32).move_to([COL, ROW2, 0])), run_time=0.5)
        self.play(FadeIn(_cap("true labels, false ratio")), run_time=0.5)
        _finish(self)


# ═══════════ B14 — SHIFT: the cut ═══════════
class B14_TheCut(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "The Cut", right=False)
        self.play(FadeIn(c.panel), run_time=0.6)
        _until(self, "Go back to a zero floor")
        self.play(c.to(0), run_time=1.4)
        # swap the live bars for split bars at the same geometry: below 91 (shared) + the sliver above
        ycut = BASE_Y + H * 91 / TOP
        low = VGroup(*[Rectangle(width=BW, height=ycut - BASE_Y, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([x, (BASE_Y + ycut) / 2, 0]) for x in (XA, XB)])
        up = VGroup(*[Rectangle(width=BW, height=BASE_Y + H * v / TOP - ycut, fill_color=INK, fill_opacity=1, stroke_width=0)
                      .move_to([x, (ycut + BASE_Y + H * v / TOP) / 2, 0]) for x, v in ((XA, A), (XB, B))])
        self.remove(c.bars)
        self.add(low, up)
        cut = DashedLine([XA - BW / 2 - 0.25, ycut, 0], [XB + BW / 2 + 0.25, ycut, 0], color=INK, stroke_width=4)
        _until(self, "draw a line across")
        c91 = _t("91", 32).move_to([XB + BW / 2 + 0.62, ycut, 0])
        self.play(Create(cut), FadeIn(c91), run_time=0.8)
        _until(self, "Below the line")
        self.play(*[r.animate.set_fill(DISCARD) for r in low], run_time=0.7)
        self.play(FadeIn(_t("below: the same 91 in each bar", 32).move_to([COL, ROW1, 0])), run_time=0.5)
        _until(self, "Above it, slivers")
        self.play(FadeIn(_t("above: slivers of 1.1 and 3.3", 32).move_to([COL, ROW2, 0])), run_time=0.5)
        _until(self, "Now cut")
        new = VGroup(_bar(XA, A, 91), _bar(XB, B, 91))
        self.play(*[r.animate.shift(DOWN * 0.8).set_opacity(0) for r in low], FadeOut(cut), FadeOut(c91),
                  *[Transform(u, n) for u, n in zip(up, new)], c.to(91), run_time=2.0)
        self.remove(*low, up); self.add(c.bars)
        _until(self, "A truncated axis is a zoom")
        self.play(FadeIn(_cap("a zoom on the slivers")), run_time=0.5)
        _finish(self)


# ═══════════ B15 — predict ═══════════
class B15_Predict(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "Commit")
        y2 = BASE_Y + 2 * _h(A, 91)
        guide = DashedLine([XA - BW / 2 - 0.1, y2, 0], [XB + BW / 2 + 0.2, y2, 0], color=DIM, stroke_width=4)
        self.wait(0.3)
        _until(self, "B looks three times A")
        self.play(Create(guide), FadeIn(_t("2 × A", 32, DIM).move_to([XB + BW / 2 + 0.72, y2, 0])), run_time=0.7)
        _until(self, "Where does the floor have to go")
        self.play(FadeIn(_t("target: B looks 2 × A", 36).move_to([COL, ROW1, 0])), run_time=0.5)
        _until(self, "Up or down")
        self.play(FadeIn(_t("up or down? how far?", 36).move_to([COL, ROW2, 0])), run_time=0.5)
        self.play(FadeIn(_cap("commit before it moves")), run_time=0.5)
        _finish(self)


# ═══════════ B16 — TRANSFORM: sweep the floor ═══════════
class B16_Sweep(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "Sweep The Floor")
        def y2(): return min(2.2, c.top(A) + (c.top(A) - BASE_Y))
        guide = always_redraw(lambda: DashedLine([XA - BW / 2 - 0.1, y2(), 0], [XB + BW / 2 + 0.2, y2(), 0], color=DIM, stroke_width=4))
        glab = always_redraw(lambda: _t("2 × A", 32, DIM).move_to([XB + BW / 2 + 0.72, y2(), 0]))
        self.play(Create(guide), FadeIn(glab), run_time=0.5)
        _until(self, "Down to eighty-nine")
        self.play(c.to(89.9), run_time=1.4)
        self.play(FadeIn(_t("down just 1.1: exactly 2 ×", 32).move_to([COL, ROW1, 0])), run_time=0.5)
        _until(self, "Eighty:")
        self.play(FadeOut(guide), FadeOut(glab), run_time=0.3)
        self.play(c.to(80), run_time=1.0)
        _until(self, "Zero:")
        self.play(c.to(0), run_time=1.3)
        _until(self, "Now up, toward A")
        self.play(c.to(92), run_time=2.6)
        _until(self, "The two numbers never moved")
        self.play(FadeIn(_t("the numbers never moved", 36, bold=True).move_to([COL, ROW2, 0])), run_time=0.5)
        self.play(FadeIn(_cap("one setting did all of it")), run_time=0.5)
        _finish(self)


# ═══════════ B17 — ABSTRACTION: a truncated axis ═══════════
class B17_NameIt(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "A Truncated Axis", f=92.0)
        self.play(c.to(91), run_time=1.0)
        self.play(FadeOut(c.panel), run_time=0.5)
        _until(self, "a truncated axis")
        self.play(FadeIn(_t("truncated axis", 44, bold=True).move_to([COL, 1.55, 0])), run_time=0.6)
        _until(self, "The ratio your eye reads")
        eq = _m(r"\text{looks} = \frac{B - \text{floor}}{A - \text{floor}}", 50).move_to([COL, 0.35, 0])
        self.play(FadeIn(eq), run_time=1.0)
        self.play(FadeIn(_t("B's bar over A's bar", 32).move_to([COL, -0.95, 0])), run_time=0.5)
        _until(self, "The floor sits in both")
        self.play(FadeIn(_t("the same floor, twice", 32).move_to([COL, ROW1, 0])), run_time=0.5)
        _until(self, "Floor at zero")
        self.play(c.to(0), run_time=1.2)
        _until(self, "Raise it")
        self.play(c.to(91.5), run_time=1.6)
        self.play(FadeIn(_t("no limit as the floor nears A", 32).move_to([COL, ROW2, 0])), GrowFromCenter(_dot(5.95, 0.05)), run_time=0.5)
        _finish(self)


# ═══════════ B18 — TANGENT: read the line ═══════════
class B18_Tangent(Scene):
    BASE = 99
    def construct(self):
        t = _title("Read The Line")
        self.add(t)
        eq = _m(r"\text{looks} = \frac{B - \text{floor}}{A - \text{floor}}", 54).move_to([-3.2, 1.55, 0])
        self.play(FadeIn(eq), run_time=0.6)
        self.play(Create(Line([0.25, 2.35, 0], [0.25, -2.6, 0], color=GHOST, stroke_width=2)), run_time=0.4)
        rows = [("left: the ratio the eye reads", 1.95, "Left:"), ("top: B minus floor, B's bar", 1.3, "Top:"),
                ("bottom: A minus floor, A's bar", 0.65, "Bottom:")]
        for s, y, cue in rows:
            _until(self, cue)
            self.play(FadeIn(_t(s, 32).move_to([0.55, y, 0], aligned_edge=LEFT), shift=RIGHT * 0.1), run_time=0.5)
        _until(self, "The floor appears twice")
        self.play(FadeIn(_t("the same floor, twice", 34, bold=True).move_to([0.55, -0.1, 0], aligned_edge=LEFT)), run_time=0.5)
        self.play(FadeIn(_t("near A, the bottom goes to 0", 32).move_to([0.55, -0.75, 0], aligned_edge=LEFT)), run_time=0.5)
        worked = [("floor 91", r"\frac{3.3}{1.1} = 3", 0.1, "Floor ninety-one"), ("floor 0", r"\frac{94.3}{92.1} \approx 1.02", -1.1, "Floor zero"),
                  ("floor 89.9", r"\frac{4.4}{2.2} = 2", -2.3, "Floor eighty-nine")]
        for lab, tex, y, cue in worked:
            _until(self, cue)
            self.play(FadeIn(_t(lab, 32).move_to([-5.75, y, 0], aligned_edge=LEFT)), FadeIn(_m(tex, 44).move_to([-2.6, y, 0])), run_time=0.7)
        self.play(GrowFromCenter(_dot(-6.0, 0.1, 0.11)), run_time=0.4)
        _until(self, "The numbers the sweep")
        self.play(FadeIn(_cap("the numbers the sweep showed you", x=3.2)), run_time=0.5)
        _finish(self)


# ═══════════ B19 — PAYOFF: back to the colleague's chart ═══════════
class B19_Payoff(Scene):
    BASE = 99
    def construct(self):
        c = _Chart(self, "Back To The Colleague's Chart")
        self.wait(0.4)
        _until(self, "Now you can read it")
        ref = always_redraw(lambda: DashedLine([XA + BW / 2, c.top(A), 0], [XB + BW / 2 + 0.1, c.top(A), 0], color=DIM, stroke_width=3))
        br = always_redraw(lambda: BraceBetweenPoints([XB + BW / 2 + 0.1, c.top(A), 0], [XB + BW / 2 + 0.1, max(c.top(B), c.top(A) + 0.06), 0],
                                                      direction=RIGHT, color=INK))
        gl = always_redraw(lambda: _t("+2.2 points", 32).move_to([0.0, (c.top(A) + c.top(B)) / 2, 0]))
        self.play(Create(ref), GrowFromCenter(br), FadeIn(gl), run_time=0.8)
        _until(self, "drop the floor to zero")
        self.play(c.to(0), run_time=2.0)
        _until(self, "Truncation isn't banned")
        self.play(FadeIn(_t("honest if zero means nothing", 32).move_to([COL - 0.1, ROW1, 0])), run_time=0.5)
        _until(self, "The choice is the difference")
        self.play(FadeIn(_t("the choice is the difference", 32, bold=True).move_to([COL, ROW2, 0])), GrowFromCenter(_dot(COL - 2.75, ROW2)), run_time=0.6)
        _until(self, "Not taught here")
        self.play(FadeIn(_cap("not taught: mismatched panels")), run_time=0.5)
        _finish(self)
