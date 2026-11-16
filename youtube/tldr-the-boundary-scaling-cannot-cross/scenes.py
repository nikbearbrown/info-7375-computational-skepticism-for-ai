"""
Manim scenes for tldr-the-boundary-scaling-cannot-cross (tldr skill — LEARN section 1, B10–B19).

Two persistent objects, one per panel:
  LEFT  — the turkey's confidence curve: day 0 … 1,000, no scale (schematic),
          22 "mornings" riding it, an ink rider at day 1,000, a dashed day-1,001
          marker just past the axis.
  RIGHT — Figure 13.1 rebuilt from its caption: the WORLD (dim outline) and a
          SAMPLE inside it (ink edge, faint fill, dim case-dots). The sample grows;
          the edge moves; the part outside is the excluded region.
B16 is the collision: the curve's mornings fly into the world and become a flat
sample; day 1,001 lands outside it; more mornings stretch the sample along the
routine and the event never comes in.

State factory: `_Stage(scene, title, left=…, right=…, **state)` rebuilds the world
at the previous beat's end state, so the last frame of Bk is the first frame of Bk+1.

Numbers are the chapter's (asserted below; FACTCHECK.md). INK text on the cream
stage; terracotta is ONE accent per scene — a dot or an X beside a word, never
text, never a line, never a ring (GATE T). Case-dots and containers are DIM (outside
the ink masks). Explicit coords inside ±6.2 × ±3.3 (never get_right()). Type floor
32 (titles 40). Captions ≤ 34 chars at x ≈ 3.2. Text is faded, never morphed.

Pacing: the exemplar's `_TARGET` block plus `_until(self, phrase)` — each reveal
waits for the spoken phrase (character share of the narration × measured audio).
"""
import math, json as _json, os as _os
import numpy as np
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the chapter's numbers (asserted — FACTCHECK rows 6–13, 20) ═══════════
FED_DAYS, EVENT_DAY = 1000, 1001
CASES, ACC_PCT = 10_000, 99.7
assert EVENT_DAY == FED_DAYS + 1 and 1 / EVENT_DAY < 0.001
assert round(CASES * (100 - ACC_PCT) / 100) == 30
CLINIC_PCT, HARMED = 94, 3

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}
_BASE_DEFAULT = 40.0

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
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)

# ═══════════ text + mark helpers ═══════════
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _title(txt, size=40): return _t(txt, size).move_to([0, 3.02, 0])
def _cap(txt, x=3.2, y=-3.05): return _t(txt, 32, DIM).move_to([x, y, 0])
def _at(txt, x, y, size=32, color=INK, bold=False): return _t(txt, size, color, bold).move_to([x, y, 0])
def _dot(x, y, r=0.14, color=TERRA): return Dot([x, y, 0], color=color, radius=r)
def _x(x, y, s=0.18, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))

# ═══════════ LEFT: the turkey's confidence curve (schematic) ═══════════
AX_X0, AX_X1, AX_Y0, AX_TOP = -5.7, -1.7, -1.75, 1.95
EX = -0.95                                                   # the day-1,001 marker, just past the axis
LX = -3.3                                                    # left-column centre for commentary
BAND_Y = -2.62
def DX(d): return AX_X0 + d / FED_DAYS * (AX_X1 - AX_X0)
def CY(d): return AX_Y0 + 0.2 + 3.2 * (1 - math.exp(-d / 260)) / (1 - math.exp(-FED_DAYS / 260))
assert all(CY(d + 1) > CY(d) for d in range(FED_DAYS))     # monotone: it never once dips
MORNINGS = [FED_DAYS * i / 21 for i in range(22)]           # 22 mornings on the curve, day 0 … 1,000

def _axes():
    xa = Line([AX_X0, AX_Y0, 0], [AX_X1 + 0.1, AX_Y0, 0], color=INK, stroke_width=3)
    ya = Line([AX_X0, AX_Y0, 0], [AX_X0, AX_TOP, 0], color=INK, stroke_width=3)
    ticks = VGroup(*[Line([DX(d), AX_Y0 - 0.08, 0], [DX(d), AX_Y0 + 0.08, 0], color=INK, stroke_width=2) for d in (0, 500, 1000)])
    labels = VGroup(_at("day 0", DX(0) + 0.1, AX_Y0 - 0.38, 32, DIM), _at("500", DX(500), AX_Y0 - 0.38, 32, DIM),
                    _at("1,000", DX(1000), AX_Y0 - 0.38, 32, DIM))
    name = _t("confidence", 32, DIM).move_to([AX_X0 - 0.05, AX_TOP + 0.33, 0], aligned_edge=LEFT)
    return VGroup(xa, ya, ticks, labels, name)
def _curve(color=INK): return ParametricFunction(lambda t: np.array([DX(t), CY(t), 0]), t_range=[0, FED_DAYS], color=color, stroke_width=5)
def _morning_on_curve(d): return Dot([DX(d), CY(d), 0], color=INK, radius=0.06)
def _rider(): return Dot([DX(FED_DAYS), CY(FED_DAYS), 0], color=INK, radius=0.11)
def _marker():
    line = DashedLine([EX, AX_Y0, 0], [EX, AX_TOP, 0], color=DIM, stroke_width=3, dash_length=0.12)
    lab = _at("day 1,001", EX, AX_TOP + 0.33, 32)
    return VGroup(line, lab)
def _event_left(): return _dot(EX, CY(FED_DAYS), 0.15)

# ═══════════ RIGHT: the world and the sample (Figure 13.1, rebuilt) ═══════════
WX0, WX1, WY0, WY1 = 0.25, 6.0, -2.45, 2.35
W_AREA = (WX1 - WX0) * (WY1 - WY0)
SC = (3.12, -0.1)                                            # the generic sample's centre
K = {1: (1.55, 1.05), 2: (2.2, 1.5), 3: (2.5, 1.85), 4: (2.62, 1.95)}   # semi-axes per enlargement
UNCOVERED = {k: 1 - math.pi * a * b / W_AREA for k, (a, b) in K.items()}
assert UNCOVERED[1] > UNCOVERED[2] > UNCOVERED[3] > UNCOVERED[4] > 0      # shrinks, never reaches zero
for a, b in K.values():
    assert SC[0] - a > WX0 + 0.2 and SC[0] + a < WX1 - 0.2 and SC[1] - b > WY0 + 0.3 and SC[1] + b < WY1 - 0.3
TC = (3.12, -0.8)                                           # the turkey's sample: long and flat, along the routine
TB = 0.8
TA = {"start": 1.5, "more": 2.45, "most": 2.65}
EVENT_R = (4.6, 1.15)                                        # day 1,001 in the world — off the routine axis
FLAB = (1.9, 0.45)                                           # "fed mornings" sits ABOVE the sample (GATE T §8.6b: an ink label inside the flat ink edge reads as nested text)
assert TC[1] + TB < EVENT_R[1] - 0.5                          # the event sits outside every turkey sample
assert TC[0] - TA["most"] > WX0 + 0.15 and TC[0] + TA["most"] < WX1 - 0.15
CL = (2.7, -0.15, 1.8, 1.3)                                  # the clinic's sample (cx, cy, a, b)
HARM = [(4.95, -1.95), (5.35, -1.7), (5.62, -2.08)]
for hx, hy in HARM:
    assert ((hx - CL[0]) / CL[2]) ** 2 + ((hy - CL[1]) / CL[3]) ** 2 > 1.2   # the three harms: past the edge

def _world():
    rect = Rectangle(width=WX1 - WX0, height=WY1 - WY0, stroke_color=DIM, stroke_width=3, fill_opacity=0).move_to([(WX0 + WX1) / 2, (WY0 + WY1) / 2, 0])
    lab = _t("the world", 32, DIM).move_to([WX0 + 0.25, WY1 - 0.33, 0], aligned_edge=LEFT)
    return VGroup(rect, lab)
def _ellipse(cx, cy, a, b, w=5):
    return Ellipse(width=2 * a, height=2 * b, stroke_color=INK, stroke_width=w, fill_color=INK, fill_opacity=0.08).move_to([cx, cy, 0])
def _sample(k): a, b = K[k]; return _ellipse(SC[0], SC[1], a, b)
def _on_edge(cx, cy, a, b, deg=-38): r = math.radians(deg); return (cx + a * math.cos(r), cy + b * math.sin(r))

_rs = np.random.RandomState(13)
_CAND = [(SC[0] + (u * 2 - 1) * K[4][0], SC[1] + (v * 2 - 1) * K[4][1]) for u, v in _rs.rand(210, 2)]
def _inside(p, cx, cy, a, b, f=0.86): return ((p[0] - cx) / (a * f)) ** 2 + ((p[1] - cy) / (b * f)) ** 2 < 1
def _clear_of_label(p, cx, cy, hw=0.72, hh=0.3): return not (abs(p[0] - cx) < hw and abs(p[1] - cy) < hh)
def _case_pts(k):
    a, b = K[k]; return [p for p in _CAND if _inside(p, SC[0], SC[1], a, b) and _clear_of_label(p, *SC)]
def _case_dots(pts): return VGroup(*[Dot([x, y, 0], color=DIM, radius=0.05) for x, y in pts])
def _new_pts(k_from, k_to): old = set(_case_pts(k_from)); return [p for p in _case_pts(k_to) if p not in old]
_CL_CAND = [(CL[0] + (u * 2 - 1) * CL[2], CL[1] + (v * 2 - 1) * CL[3]) for u, v in np.random.RandomState(94).rand(110, 2)]
def _clinic_pts(): return [p for p in _CL_CAND if _inside(p, CL[0], CL[1], CL[2], CL[3]) and _clear_of_label(p, CL[0], CL[1], 0.7, 0.4)]

# the turkey's mornings in the world: two rows along the routine, a label between them
MORN_POS = [(TC[0] + dx, TC[1] + dy) for dy in (0.36, -0.36) for dx in np.linspace(-1.1, 1.1, 11)]   # 11 per row = 22 mornings
MORE_POS = [(TC[0] + s * dx, TC[1] + dy) for dy in (0.36, -0.36) for s in (-1, 1) for dx in (1.34, 1.56, 1.78)]   # 12 more (B16)
MOST_POS = [(TC[0] + s * 1.98, TC[1] + dy) for dy in (0.36, -0.36) for s in (-1, 1)]                            # 4 more (B19)
for (px, py) in MORN_POS: assert _inside((px, py), TC[0], TC[1], TA["start"], TB, 1.0)
for (px, py) in MORE_POS: assert _inside((px, py), TC[0], TC[1], TA["more"], TB, 1.0)
for (px, py) in MOST_POS: assert _inside((px, py), TC[0], TC[1], TA["most"], TB, 1.0)
assert len(MORN_POS) == len(MORNINGS) == 22
def _tdots(pts, color=DIM): return VGroup(*[Dot([x, y, 0], color=color, radius=0.07) for x, y in pts])   # in the sample, mornings are cases: DIM (GATE T §8.6b)
def _tsample(which): return _ellipse(TC[0], TC[1], TA[which], TB)

# bars: the uncovered share after each enlargement (schematic)
BAR_X = {1: -5.4, 2: -4.5, 3: -3.6}; BAR_BASE = -2.2; BAR_S = 1.8; BAR_W = 0.55
def _bar(k):
    h = UNCOVERED[k] * BAR_S
    return Rectangle(width=BAR_W, height=h, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([BAR_X[k], BAR_BASE + h / 2, 0])
def _bar_base(): return Line([-5.9, BAR_BASE, 0], [-2.9, BAR_BASE, 0], color=INK, stroke_width=3)
ZERO_X = BAR_X[3] + (UNCOVERED[3] * BAR_S) / ((UNCOVERED[1] - UNCOVERED[3]) * BAR_S / (BAR_X[3] - BAR_X[1]))
assert -2.2 < ZERO_X < -0.6                                   # the extrapolated zero lands inside the left column


class _Stage:
    """Rebuild the world at a beat boundary. left: None | 'turkey' | 'facts' | 'bars' | 'naive' | 'defs' | 'name' | 'clinicq'.
    right: None | 'puzzle' | ('generic', k) | 'ask' | ('turkey', which) | 'clinic'."""
    def __init__(self, scene, title, left=None, right=None, edge_dot=False, ev_left=True, ev_right_terra=True, curve_dim=False,
                 mornings_on_curve=True, excluded=False, marker=True):
        self.s = scene; self.t = _title(title); scene.add(self.t)
        self.L = VGroup(); self.R = VGroup()
        if left == "turkey":
            self.axes = _axes(); self.curve = _curve(DIM if curve_dim else INK); self.rider = _rider()
            self.mornings = VGroup(*[_morning_on_curve(d) for d in MORNINGS]) if mornings_on_curve else VGroup()
            self.L.add(self.axes, self.curve, self.mornings, self.rider)
            if marker:
                self.marker = _marker(); self.L.add(self.marker)
                if ev_left: self.ev = _event_left(); self.L.add(self.ev)
        elif left == "facts":
            self.facts = _facts(); self.L.add(self.facts)
        elif left in ("bars", "naive"):
            self.bars = VGroup(_bar_base(), _bar(1), _bar(2), _bar(3)); self.bband = _at("not yet reached", -4.5, BAND_Y, 32, DIM)
            self.L.add(self.bars, self.bband)
            if left == "bars":
                self.head = _more_head(); self.L.add(self.head)
            else:
                self.naive = _naive_group(); self.L.add(self.naive)
        elif left == "defs":
            self.defs = _defs(); self.L.add(self.defs)
        if right == "puzzle":
            self.R.add(_puzzle(), _facts_right())
        elif isinstance(right, tuple) and right[0] == "generic":
            k = right[1]; self.world = _world(); self.sample = _sample(k); self.cases = _case_dots(_case_pts(k))
            self.slab = _at("sample", SC[0], SC[1], 36)
            self.R.add(self.world, self.sample, self.cases, self.slab)
            if excluded: self.exl = _at("excluded", 5.15, 1.98, 32, DIM); self.R.add(self.exl)
            if edge_dot:
                a, b = K[k]; self.edot = _dot(*_on_edge(SC[0], SC[1], a, b)); self.R.add(self.edot)
        elif right == "ask":
            self.world = _world(); self.R.add(self.world, *_ask())
        elif isinstance(right, tuple) and right[0] == "turkey":
            which = right[1]; self.world = _world(); self.ts = _tsample(which)
            pts = MORN_POS + (MORE_POS if which in ("more", "most") else []) + (MOST_POS if which == "most" else [])
            self.tdots = _tdots(pts); self.flab = _at("fed mornings", FLAB[0], FLAB[1], 32)
            self.evr = _dot(*EVENT_R, 0.16, TERRA if ev_right_terra else INK); self.evlab = _at("day 1,001", EVENT_R[0], EVENT_R[1] + 0.47, 32)
            self.R.add(self.world, self.ts, self.tdots, self.flab, self.evr, self.evlab)
            if excluded: self.exl = _at("excluded", 1.35, 1.35, 32, DIM); self.R.add(self.exl)
        elif right == "clinic":
            self.world = _world(); self.cs = _ellipse(*CL); self.cdots = _case_dots(_clinic_pts())
            self.pct = _at(f"{CLINIC_PCT}%", CL[0], CL[1], 56)
            self.R.add(self.world, self.cs, self.cdots, self.pct)
        scene.add(self.L, self.R)


def _facts():
    return VGroup(_at("tested on", LX, 1.85, 34, DIM), _at("10,000", LX, 1.1, 64), _at("routine cases", LX, 0.35, 40),
                  _at("99.7%", LX, -0.75, 64), _at("right", LX, -1.5, 40))
def _more_head(): return VGroup(_at("more data:", LX, 1.85, 40), _at("the edge moves out", LX, 1.2, 40))
def _still(): return _at("still an edge", LX, 0.4, 40, INK, True)
def _naive_lines(): return VGroup(_at("scale it enough, and", LX, 1.85, 34), _at("the gap shrinks to nothing?", LX, 1.2, 34))
def _turkey_lines(): return VGroup(_at("turkey: 1 morning in 1,001", LX, 0.35, 36), _at("under 0.1%, and it mattered", LX, -0.25, 36, INK, True))
def _trend():
    return DashedLine([BAR_X[1], BAR_BASE + UNCOVERED[1] * BAR_S, 0], [ZERO_X, BAR_BASE, 0], color=DIM, stroke_width=4, dash_length=0.14)
def _enough(): return _at("enough?", ZERO_X, BAND_Y, 32, DIM)
def _naive_group(): return VGroup(_naive_lines(), _turkey_lines(), _trend(), _enough(), _x(-0.3, 1.2))
def _defs():
    rows = VGroup(*[_t(s, 34).move_to([-5.9, y, 0], aligned_edge=LEFT) for s, y in
                    (("sample: what the data reached", 1.85), ("excluded: what it did not", 1.15), ("edge: where the data stopped", 0.45))])
    return VGroup(rows, _at("the gap lives at the edge", LX, -0.75, 36, INK, True))
def _puzzle(): return VGroup(_at("Would more days", 3.2, 1.55, 40, INK, True), _at("of data have saved it?", 3.2, 0.9, 40, INK, True))
def _facts_right():
    return VGroup(_at("days 1 to 1,000: fed", 3.2, -0.35, 34), _at("confidence: rising", 3.2, -0.95, 34),
                  _at("day 1,001: Thanksgiving", 3.2, -1.55, 34))
def _ask(): return [_at("inside or outside?", SC[0], 0.45, 40, INK, True), _at("more mornings: in?", SC[0], -0.35, 36)]


class B10_BestDay(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "The Turkey's Best Day")
        axes = _axes(); curve = _curve(); rider = Dot([DX(0), CY(0), 0], color=INK, radius=0.11)
        mornings = VGroup(*[_morning_on_curve(d) for d in MORNINGS])
        facts = _facts_right()
        self.play(Create(axes), FadeIn(_cap("confidence: schematic, no scale")), run_time=0.8)
        self.play(FadeIn(facts[0]), run_time=0.4)
        self.play(Create(curve), MoveAlongPath(rider, curve), LaggedStart(*[FadeIn(m) for m in mornings], lag_ratio=0.12), run_time=4.4, rate_func=linear)
        _until(self, "It never once dips")
        self.play(FadeIn(facts[1]), run_time=0.4)
        _until(self, "Day one thousand and one")
        marker = _marker(); ev = _event_left()
        self.play(Create(marker[0]), FadeIn(marker[1]), run_time=0.6)
        self.play(GrowFromCenter(ev), FadeIn(facts[2]), run_time=0.5)
        _until(self, "So here's the puzzle")
        self.play(FadeIn(_puzzle()), run_time=0.5)
        _finish(self)


class B11_TheSample(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "Ten Thousand Routine Cases", left="turkey", right="puzzle")
        self.play(FadeOut(st.L), FadeOut(st.R), run_time=0.5)
        f = _facts(); cap = _cap("regions: schematic")
        _until(self, "It's tested on")
        self.play(FadeIn(f[0]), FadeIn(f[1]), FadeIn(f[2]), FadeIn(cap), run_time=0.5)
        _until(self, "ninety-nine point seven")
        self.play(FadeIn(f[3]), FadeIn(f[4]), run_time=0.5)
        _until(self, "Draw those cases")
        s = _sample(1); cases = _case_dots(_case_pts(1)); lab = _at("sample", SC[0], SC[1], 36)
        self.play(GrowFromCenter(s), LaggedStart(*[FadeIn(c) for c in cases], lag_ratio=0.02), run_time=1.2)
        self.play(FadeIn(lab), run_time=0.3)
        _until(self, "Draw everything")
        w = _world()
        self.play(Create(w[0]), FadeIn(w[1]), run_time=0.9)
        _until(self, "the sample has an edge")
        a, b = K[1]
        self.play(GrowFromCenter(_dot(*_on_edge(SC[0], SC[1], a, b))), run_time=0.4)
        _finish(self)


class B12_MoreData(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "Add More Data", left="facts", right=("generic", 1), edge_dot=True)
        self.add(_cap("regions: schematic"))
        base = _bar_base(); b1 = _bar(1); band = _at("not yet reached", -4.5, BAND_Y, 32, DIM); head = _more_head()
        self.play(FadeOut(st.L), run_time=0.4)
        self.play(Create(base), GrowFromEdge(b1, DOWN), FadeIn(band), FadeIn(head[0]), run_time=0.6)
        for k, phrase in ((2, "The sample grows"), (3, "Add more again")):
            _until(self, phrase)
            a, b = K[k]
            self.play(Transform(st.sample, _sample(k)), FadeIn(_case_dots(_new_pts(k - 1, k))),
                      st.edot.animate.move_to([*_on_edge(SC[0], SC[1], a, b), 0]), GrowFromEdge(_bar(k), DOWN),
                      *([FadeIn(head[1])] if k == 2 else []), run_time=1.3)
        _until(self, "look where the edge is")
        self.play(FadeIn(_still()), run_time=0.4)
        _finish(self)


class B13_ScaleItEnough(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "Scale It Enough?", left="bars", right=("generic", 3), edge_dot=True)
        still = _still(); self.add(still, _cap("regions: schematic"))
        self.play(FadeOut(st.head), FadeOut(still), FadeOut(st.edot), run_time=0.4)
        nl = _naive_lines(); tl = _turkey_lines()
        _until(self, "The gap is shrinking")
        self.play(FadeIn(nl[0]), FadeIn(nl[1]), run_time=0.5)
        _until(self, "Keep scaling")
        self.play(Create(_trend()), run_time=1.1)
        self.play(FadeIn(_enough()), run_time=0.3)
        _until(self, "But the turkey's gap")
        self.play(FadeIn(tl[0]), run_time=0.4)
        _until(self, "under a tenth")
        self.play(FadeIn(tl[1]), run_time=0.4)
        _until(self, "Measuring how much")
        self.play(Create(_x(-0.3, 1.2)), run_time=0.4)
        _finish(self)


class B14_WatchTheEdge(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "Watch the Edge", left="naive", right=("generic", 3))
        cap0 = _cap("regions: schematic"); self.add(cap0)
        self.play(FadeOut(st.L), FadeOut(cap0), run_time=0.5)
        d = _defs(); rows, bold = d[0], d[1]
        _until(self, "The sample is everything")
        self.play(FadeIn(rows[0]), run_time=0.4)
        _until(self, "The excluded part")
        exl = _at("excluded", 5.15, 1.98, 32, DIM)
        self.play(FadeIn(rows[1]), FadeIn(exl), run_time=0.4)
        _until(self, "Grow one")
        self.play(Transform(st.sample, _sample(4)), FadeIn(_case_dots(_new_pts(3, 4))), FadeIn(_cap("complementary by construction")), run_time=1.3)
        _until(self, "And that line, the edge")
        a, b = K[4]
        self.play(FadeIn(rows[2]), GrowFromCenter(_dot(*_on_edge(SC[0], SC[1], a, b))), run_time=0.5)
        _until(self, "It lives at the edge")
        self.play(FadeIn(bold), run_time=0.4)
        _finish(self)


class B15_Commit(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "Commit", left="defs", right=("generic", 4), edge_dot=True, excluded=True)
        cap0 = _cap("complementary by construction"); self.add(cap0)
        self.play(FadeOut(st.L), FadeOut(VGroup(st.sample, st.cases, st.slab, st.exl, st.edot)), FadeOut(cap0), run_time=0.6)
        axes = _axes(); curve = _curve(); mornings = VGroup(*[_morning_on_curve(d) for d in MORNINGS]); marker = _marker()
        rider = _rider()
        self.play(FadeIn(axes), FadeIn(curve), FadeIn(mornings), FadeIn(marker), run_time=0.7)
        ask = _ask()
        _until(self, "Put the turkey's")
        self.play(GrowFromCenter(rider), FadeIn(ask[0]), FadeIn(_cap("commit before it moves")), run_time=0.4)
        _until(self, "Where does day")
        self.play(GrowFromCenter(_event_left()), run_time=0.4)
        _until(self, "And if we added")
        self.play(FadeIn(ask[1]), run_time=0.4)
        _finish(self)


class B16_MorningsMoveIn(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "The Mornings Move In", left="turkey", right="ask")
        cap0 = _cap("commit before it moves"); self.add(cap0)
        self.play(*[FadeOut(m) for m in st.R[1:]], FadeOut(cap0), run_time=0.4)
        order = sorted(range(22), key=lambda i: MORNINGS[i])
        targets = sorted(MORN_POS, key=lambda p: (p[0], p[1]))
        _until(self, "Every fed morning")
        self.play(LaggedStart(*[st.mornings[i].animate.move_to([*targets[j], 0]).set_color(DIM).scale(0.07 / 0.06) for j, i in enumerate(order)], lag_ratio=0.06),
                  st.curve.animate.set_color(DIM), run_time=2.2)
        _until(self, "The last one is the edge")
        ts = _tsample("start"); flab = _at("fed mornings", FLAB[0], FLAB[1], 32)
        self.play(Create(ts), FadeIn(flab), run_time=0.8)
        _until(self, "Day one thousand and one lands")
        evlab = _at("day 1,001", EVENT_R[0], EVENT_R[1] + 0.47, 32)
        self.play(st.ev.animate.move_to([*EVENT_R, 0]).scale(0.16 / 0.15), FadeIn(evlab), run_time=1.0)
        _until(self, "Now add more")
        self.play(Transform(ts, _tsample("more")), LaggedStart(*[FadeIn(d) for d in _tdots(MORE_POS)], lag_ratio=0.05),
                  FadeIn(_at("more fed mornings", TC[0], -1.98, 32)), run_time=1.6)
        _until(self, "The event doesn't come in")
        self.play(FadeIn(_at("still outside", EVENT_R[0], EVENT_R[1] - 0.53, 32, INK, True)), FadeIn(_cap("more of the same mornings")), run_time=0.4)
        _finish(self)


class B17_NameIt(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "The Data-World Gap", left="turkey", right=("turkey", "more"), curve_dim=True, mornings_on_curve=False, ev_left=False)
        # B16's end: the left curve (dim), the rider, the marker; the right sample with its captions
        extras = VGroup(_at("more fed mornings", TC[0], -1.98, 32), _at("still outside", EVENT_R[0], EVENT_R[1] - 0.53, 32, INK, True),
                        _cap("more of the same mornings"))
        self.add(extras)
        self.play(FadeOut(st.L), FadeOut(extras), st.evr.animate.set_color(INK), run_time=0.6)
        _until(self, "the data-world gap")
        name = _at("the data-world gap", LX, 1.85, 44, INK, True)
        self.play(FadeIn(name), GrowFromCenter(_dot(-5.95, 1.85)), run_time=0.5)
        _until(self, "The parts of the world")
        self.play(FadeIn(_at("what is not in the data", LX, 0.95, 32)), FadeIn(_at("is not learnable from the data", LX, 0.4, 32)), run_time=0.5)
        _until(self, "complementary by construction", lead=1.4)
        self.play(FadeIn(_at("complementary by construction", LX, -0.5, 32)), FadeIn(_at("excluded", 1.35, 1.35, 32, DIM)),
                  Create(_ellipse(TC[0], TC[1], TA["more"], TB, 9).set_fill(opacity=0)), run_time=0.9)
        _until(self, "Scaling moves the edge")
        self.play(FadeIn(_at("the edge moves, never vanishes", LX, -1.15, 32, INK, True)), run_time=0.4)
        _until(self, "David Hume")
        self.play(FadeIn(_at("after Hume (1748), Enquiry §IV", LX, BAND_Y, 32, DIM)), run_time=0.4)
        _finish(self)


class B18_NinetyFour(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "Ninety-Four Percent, Three Patients", right=("turkey", "more"), ev_right_terra=False, excluded=True)
        left = VGroup(_at("the data-world gap", LX, 1.85, 44, INK, True), _dot(-5.95, 1.85),
                      _at("what is not in the data", LX, 0.95, 32), _at("is not learnable from the data", LX, 0.4, 32),
                      _at("complementary by construction", LX, -0.5, 32), _at("the edge moves, never vanishes", LX, -1.15, 32, INK, True),
                      _at("after Hume (1748), Enquiry §IV", LX, BAND_Y, 32, DIM))
        retrace = _ellipse(TC[0], TC[1], TA["more"], TB, 9).set_fill(opacity=0)
        self.add(left, retrace)
        self.play(FadeOut(left), FadeOut(retrace), FadeOut(VGroup(st.tdots, st.flab, st.evr, st.evlab, st.exl)), run_time=0.6)
        _until(self, "composite case")
        self.play(Transform(st.ts, _ellipse(*CL)), FadeIn(_cap("a composite, not one incident")), run_time=1.0)
        self.play(FadeIn(_at("tested:", LX, 1.85, 32, DIM)), FadeIn(_at("does this match the data?", LX, 1.3, 36)), run_time=0.4)
        _until(self, "ninety-four percent accuracy")
        self.play(FadeIn(_case_dots(_clinic_pts())), FadeIn(_at(f"{CLINIC_PCT}%", CL[0], CL[1], 56)), run_time=0.6)
        _until(self, "three patients harmed")
        self.play(*[GrowFromCenter(Dot([x, y, 0], color=INK, radius=0.11)) for x, y in HARM],
                  FadeIn(_at(f"{HARMED} harmed", 5.2, -1.15, 34)), GrowFromCenter(_dot(5.2, -0.72, 0.12)), run_time=0.6)
        self.play(FadeIn(_at("harmed:", LX, 0.2, 32, DIM)), FadeIn(_at("what is going on", LX, -0.35, 36)),
                  FadeIn(_at("with this patient?", LX, -0.9, 36)), run_time=0.4)
        _until(self, "In distribution")
        self.play(FadeIn(_at("inside the edge: it holds", LX, BAND_Y + 0.55, 32, INK, True)), run_time=0.4)
        _finish(self)


class B19_Tomorrow(Scene):
    BASE = 40.0
    def construct(self):
        st = _Stage(self, "Is Tomorrow Inside?", right="clinic")
        prev = VGroup(_at("tested:", LX, 1.85, 32, DIM), _at("does this match the data?", LX, 1.3, 36),
                      *[Dot([x, y, 0], color=INK, radius=0.11) for x, y in HARM], _at(f"{HARMED} harmed", 5.2, -1.15, 34), _dot(5.2, -0.72, 0.12),
                      _at("harmed:", LX, 0.2, 32, DIM), _at("what is going on", LX, -0.35, 36), _at("with this patient?", LX, -0.9, 36),
                      _at("inside the edge: it holds", LX, BAND_Y + 0.55, 32, INK, True), _cap("a composite, not one incident"))
        self.add(prev)
        self.play(FadeOut(prev), FadeOut(st.cdots), FadeOut(st.pct), run_time=0.6)
        axes = _axes(); curve = _curve(); rider = _rider(); marker = _marker()
        tdots = _tdots(MORN_POS + MORE_POS); flab = _at("fed mornings", FLAB[0], FLAB[1], 32)
        evr = _dot(*EVENT_R, 0.16, INK); evlab = _at("day 1,001", EVENT_R[0], EVENT_R[1] + 0.47, 32)
        self.play(Transform(st.cs, _tsample("more")), FadeIn(tdots), FadeIn(flab), FadeIn(evr), FadeIn(evlab),
                  FadeIn(axes), FadeIn(curve), FadeIn(rider), FadeIn(marker), run_time=1.0)
        _until(self, "More fed mornings raise")
        self.play(Transform(st.cs, _tsample("most")), LaggedStart(*[GrowFromCenter(d) for d in _tdots(MOST_POS)], lag_ratio=0.1), run_time=1.2)
        _until(self, "They never carry it across")
        self.play(FadeIn(_at("the edge moves, never across", LX, BAND_Y, 32, INK, True)), run_time=0.4)
        _until(self, "It's whether tomorrow is inside")
        self.play(FadeIn(_at("is tomorrow inside?", TC[0], -1.98, 36, INK, True)), evr.animate.set_color(TERRA), run_time=0.5)
        _until(self, "Not taught here")
        self.play(FadeIn(_cap("not taught here: meaning, intent")), run_time=0.4)
        _finish(self)
