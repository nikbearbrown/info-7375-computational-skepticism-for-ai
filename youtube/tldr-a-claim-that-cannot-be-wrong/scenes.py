"""
Manim scenes for tldr-a-claim-that-cannot-be-wrong (tldr skill — LEARN section 1, B10–B19).

ONE stage, persistent across the section via the `_Stage` factory:
  · a claim tile (the claim's words, top left) that morphs rhetorical → Popperian;
  · an outcome axis (error rate on unfamiliar inputs → recall) with results as dots;
  · the FORBIDDEN REGION — the claim drawn as the outcomes it rules out (dim fill);
  · a confidence bar at right (schematic) that the favorable checks push up.
The representation: a claim is the region of outcomes it forbids.

Numbers: only the chapter's (table thresholds; 27,697; missed ≈ 2 of 3) and the one
recomputation (caught ≈ 1/3), asserted below. INK text on the cream stage; terracotta
is ONE accent per scene — a dot, never text, never a stroke near text (GATE T).
Gate A/B: a new geometric object before each final play; no line crosses a label;
explicit coords inside ±6.2 / ±3.3. Type floor 32 (titles 40). Captions ≤ 34 chars,
centred at x ≈ 3.2. No slant=ITALIC on multi-word text.
"""
import json as _json, os as _os
from fractions import Fraction
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ── the chapter's numbers ──────────────────────────────────────────────────
CAUGHT = 1 - Fraction(2, 3)                  # missed roughly two of every three → caught roughly one in three
RECALL_FLOOR = 0.88                          # table row 2
PRECISION_FLOOR = 0.91
assert CAUGHT == Fraction(1, 3) and float(CAUGHT) < RECALL_FLOOR
N_MICHIGAN = 27697

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
except Exception:
    _TARGET = {}
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

def _finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    rt = getattr(getattr(self, "renderer", None), "time", None)
    elapsed = float(rt) if isinstance(rt, (int, float)) else 0.0
    self.wait(max(1.0, target - elapsed) if target else 2.0)

# ═══════════ text helpers ═══════════
def _title(txt, size=40): return Text(txt, font=SERIF, color=INK, font_size=size).move_to([0, 2.95, 0])
def _t(s, size=36, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _L(s, x, y, size=32, color=INK, bold=False): return _t(s, size, color, bold).move_to([x, y, 0], aligned_edge=LEFT)
def _cap(txt, x=3.2, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -3.05, 0])

# ═══════════ stage geometry ═══════════
TX = -5.9                                    # claim tile left edge
TY1, TY2 = 1.95, 1.4                         # claim tile lines
TALLY_Y = 0.75
AY = -1.3                                    # the outcome axis
AX0, AX1 = -5.6, 3.6
RTOP = 0.0                                   # forbidden region top
E2 = -3.2                                    # the 2% mark on the (schematic) error axis
DOTS_E = [-4.4, -0.8, 2.8]                   # three constructed results: low · middling · terrible
def XR(r): return AX0 + float(r) * (AX1 - AX0)   # recall axis 0 … 1
XC = XR(CAUGHT)                              # ≈ −2.53
BAR_X, BAR_W, BAR_Y0, BAR_Y1 = 5.3, 0.5, -2.2, 1.0
BAR_LEVELS = [0, 0.4, 0.64, 0.78, 0.87, 0.92]    # schematic: climbs, never reaches the top
COL_X = 4.4; COL_Y = [0.6, 0.2, -0.2, -0.6, -1.0]
ROWS_Y = [1.2, 0.7, 0.2, -0.3, -0.8]
CHECKS = ["strong internal validation", "a respectable reported AUC", "a risk number on every patient",
          "published", "cleared through procurement"]

CLAIMS = {
    "robust":   ["“The system is robust.”"],
    "robustP":  ["error rate on out-of-distribution inputs < 2%", "across a 30-day rolling window"],
    "perf":     ["“The model performs well.”"],
    "perfP":    ["precision ≥ 0.91 and recall ≥ 0.88", "on the held-out test set, monthly"],
    "sepsis":   ["“The sepsis model performs well.”"],
    "sepsisP":  ["“The sepsis model performs well.”", "recall ≥ 0.88"],
}
def _claim(key):
    lines = CLAIMS[key]
    if len(lines) == 1:
        return VGroup(_L(lines[0], TX, TY1, 36, INK, bold=True))
    first_bold = key == "sepsisP"
    return VGroup(_L(lines[0], TX, TY1, 36 if first_bold else 32, INK, bold=first_bold), _L(lines[1], TX, TY2, 32))

AXES = {
    "error":  {"name": "error rate on unfamiliar inputs", "ends": ("none", "a lot")},
    "recall": {"name": "recall: share of real cases caught", "ends": ("0", "1")},
}
def _axis(kind, color=INK):
    a = AXES[kind]
    line = Line([AX0, AY, 0], [AX1, AY, 0], color=color, stroke_width=3)
    ticks = VGroup(*[Line([x, AY - 0.1, 0], [x, AY + 0.1, 0], color=color, stroke_width=2) for x in (AX0, AX1)])
    ends = VGroup(_t(a["ends"][0], 32, DIM if color == INK else GHOST).move_to([AX0, AY - 0.5, 0]),
                  _t(a["ends"][1], 32, DIM if color == INK else GHOST).move_to([AX1, AY - 0.5, 0]))
    name = _t(a["name"], 32, DIM if color == INK else GHOST).move_to([-1.0, AY - 1.05, 0])
    return VGroup(line, ticks, ends, name)
def _mark(x, label, color=INK):
    return VGroup(Line([x, AY - 0.14, 0], [x, AY + 0.14, 0], color=color, stroke_width=4),
                  _t(label, 32, INK).move_to([x, AY - 0.5, 0]))
def _region(x0, x1, lx):
    r = Rectangle(width=x1 - x0, height=RTOP - AY, fill_color=DIM, fill_opacity=0.17, stroke_width=0).move_to([(x0 + x1) / 2, (AY + RTOP) / 2, 0])
    lab = _t("forbidden", 32, INK).move_to([lx, (AY + RTOP) / 2 + 0.2, 0])
    return VGroup(r, lab)
REGION = {"error": (E2, AX1, 0.8), "recall": (AX0, XR(RECALL_FLOOR), 0.6)}
def _dot(x, y=AY, color=INK, r=0.12): return Dot([x, y, 0], color=color, radius=r)
def _grow(scene, rect, edge):
    """grow a region along ONE axis from an edge (width from LEFT, height from DOWN) — the ban being drawn."""
    dim = 0 if edge is LEFT else 1
    seed = rect.copy().stretch(0.02, dim, about_edge=edge)
    scene.add(seed)
    return seed, Transform(seed, rect)
def _tally(s, bold=False): return _L(s, TX, TALLY_Y, 36, INK, bold)

def _bar_track():
    track = Rectangle(width=BAR_W, height=BAR_Y1 - BAR_Y0, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([BAR_X, (BAR_Y0 + BAR_Y1) / 2, 0])
    top = DashedLine([BAR_X - 0.45, BAR_Y1 + 0.06, 0], [BAR_X + 0.45, BAR_Y1 + 0.06, 0], color=INK, stroke_width=3, dash_length=0.08)
    lab = _t("confidence", 32, DIM).move_to([BAR_X, BAR_Y1 + 0.5, 0])
    return VGroup(track, top, lab)
def _bar_fill(level):
    h = max(level * (BAR_Y1 - BAR_Y0), 0.02)
    return Rectangle(width=BAR_W, height=h, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([BAR_X, BAR_Y0 + h / 2, 0])


class _Stage:
    """The persistent world. Rebuilt at the previous beat's END state (transform, don't cut)."""
    def __init__(self, scene, title, claim="robust", axis="error", dots=0, region=None, bar=None, col=False, ghost_col=False,
                 swan=False, mark=None, tally=None):
        self.scene = scene
        self.t = _title(title); scene.add(self.t)
        self.claim = _claim(claim); scene.add(self.claim)
        self.axis = _axis(axis); scene.add(self.axis)
        self.mark = None
        if mark == "2%":
            self.mark = _mark(E2, "2%"); scene.add(self.mark)
        elif mark == "0.88":
            self.mark = _mark(XR(RECALL_FLOOR), "0.88"); scene.add(self.mark)
        self.region = None
        if region:
            x0, x1, lx = REGION[region]; self.region = _region(x0, x1, lx); scene.add(self.region)
        self.dots = VGroup(*[_dot(x) for x in DOTS_E[:dots]]); scene.add(self.dots)
        self.tally = _tally(tally) if tally else None
        if self.tally: scene.add(self.tally)
        self.bar = self.fill = None
        if bar is not None:
            self.bar = _bar_track(); self.fill = _bar_fill(BAR_LEVELS[bar]); scene.add(self.bar, self.fill)
        self.col = VGroup()
        if col:
            self.col = VGroup(*[_dot(COL_X, y, GHOST if ghost_col else INK, 0.1) for y in COL_Y]); scene.add(self.col)
        self.swan = None
        if swan:
            self.swan = _dot(XC, AY, TERRA, 0.16); scene.add(self.swan)


# ═══════════ B10 HOOK ═══════════
class B10_TheTile(Scene):
    BASE = 11.0
    def construct(self):
        t = _title("What Would Non-Robust Look Like?")
        self.add(t)
        claim = _claim("robust")
        self.play(FadeIn(claim, shift=DOWN * 0.1), run_time=0.6)
        axis = _axis("error")
        self.play(Create(axis[0]), FadeIn(axis[1]), FadeIn(axis[2]), FadeIn(axis[3]), run_time=1.0)
        self.play(FadeIn(_cap("constructed observations")), run_time=0.4)
        tally = None
        for i, x in enumerate(DOTS_E):
            d = _dot(x, 0.35)
            self.play(FadeIn(d, scale=0.5), run_time=0.3)
            self.play(d.animate.move_to([x, AY, 0]), run_time=0.6)
            nt = _tally(f"compatible: {i + 1} of {i + 1}")
            self.play(FadeIn(nt) if tally is None else Transform(tally, nt), run_time=0.4)
            tally = tally or nt
        q = _t("so what would non-robust look like?", 36, INK, bold=True).move_to([-1.0, -0.15, 0])
        self.play(FadeIn(q), run_time=0.6)
        _finish(self)


# ═══════════ B11 INSTANCE — draw what it forbids ═══════════
class B11_DrawTheBan(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "Draw What It Forbids", claim="robust", axis="error", dots=3, tally="compatible: 3 of 3")
        self.wait(0.4)
        self.play(Transform(st.claim, _claim("robustP")), FadeOut(st.tally), run_time=1.0)
        mark = _mark(E2, "2%")
        self.play(Create(mark[0]), FadeIn(mark[1]), run_time=0.6)
        x0, x1, lx = REGION["error"]; reg = _region(x0, x1, lx)
        seed, grow = _grow(self, reg[0], LEFT)
        self.play(grow, run_time=1.2)
        self.play(FadeIn(reg[1]), run_time=0.4)
        # replay the same three results
        self.play(*[d.animate.move_to([d.get_center()[0], 0.35, 0]) for d in st.dots], run_time=0.6)
        for i, d in enumerate(st.dots):
            self.play(d.animate.move_to([DOTS_E[i], AY, 0]), run_time=0.6)
        verdict = _tally("refuted: 2 of 3", bold=True)
        self.play(FadeIn(verdict), run_time=0.4)
        self.play(GrowFromCenter(Dot([-2.45, TALLY_Y, 0], color=TERRA, radius=0.14)), run_time=0.4)
        self.play(FadeIn(_cap("now it can be wrong")), run_time=0.5)
        _finish(self)


# ═══════════ B12 INSTANCE — the other side ═══════════
class B12_OtherSide(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "Same Move, Other Side", claim="robustP", axis="error", dots=3, region="error", mark="2%")
        self.wait(0.4)
        new = _claim("perf")
        self.play(FadeOut(st.dots), FadeOut(st.claim), FadeIn(new), run_time=0.8)
        st.claim = new
        self.play(Transform(st.claim, _claim("perfP")), run_time=1.0)
        self.play(Transform(st.axis, _axis("recall")), Transform(st.mark, _mark(XR(RECALL_FLOOR), "0.88")), run_time=1.0)
        x0, x1, lx = REGION["recall"]
        self.play(Transform(st.region, _region(x0, x1, lx)), run_time=1.6)
        probe = _dot(XR(0.95), AY)                    # a result above the floor: allowed
        self.play(GrowFromCenter(probe), run_time=0.4)
        self.play(FadeIn(_cap("different claim, different side")), run_time=0.5)
        _finish(self)


# ═══════════ B13 NAIVE — count the swans ═══════════
class B13_CountTheSwans(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "Count The Evidence", claim="perfP", axis="recall", region="recall", mark="0.88")
        self.wait(0.3)
        ghost_axis = _axis("recall", GHOST)
        new = _claim("sepsis")
        self.play(FadeOut(st.region), FadeOut(st.mark), Transform(st.axis, ghost_axis), FadeOut(st.claim), FadeIn(new), run_time=0.9)
        st.claim = new
        bar = _bar_track(); fill = _bar_fill(0)
        self.play(FadeIn(bar[0]), Create(bar[1]), FadeIn(bar[2]), run_time=0.6)
        self.add(fill)
        for i, (txt, y) in enumerate(zip(CHECKS, ROWS_Y)):
            self.play(GrowFromCenter(_dot(-5.75, y, INK, 0.1)), FadeIn(_L(txt, -5.45, y, 32)),
                      Transform(fill, _bar_fill(BAR_LEVELS[i + 1])), run_time=0.7)
        self.play(FadeIn(_cap("confidence here is schematic")), run_time=0.5)
        _finish(self)


# ═══════════ B14 SHIFT — what it forbids ═══════════
class B14_WhatItForbids(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "Ask What It Forbids", claim="sepsis", axis="recall", bar=5)
        st.axis.become(_axis("recall", GHOST))
        rows = VGroup(*[_L(txt, -5.45, y, 32) for txt, y in zip(CHECKS, ROWS_Y)])
        rdots = VGroup(*[_dot(-5.75, y, INK, 0.1) for y in ROWS_Y])
        self.add(rows, rdots)
        self.wait(0.3)
        self.play(FadeOut(rows), *[d.animate.move_to([COL_X, y, 0]) for d, y in zip(rdots, COL_Y)], run_time=1.0)
        self.play(Transform(st.axis, _axis("recall")), run_time=0.6)
        nothing = _t("forbidden: nothing", 36, INK).move_to([-1.0, 0.45, 0])
        self.play(FadeIn(nothing), run_time=0.5)
        self.wait(0.6)
        mark = _mark(XR(RECALL_FLOOR), "0.88")
        self.play(FadeOut(nothing), Transform(st.claim, _claim("sepsisP")), Create(mark[0]), FadeIn(mark[1]), run_time=0.8)
        x0, x1, lx = REGION["recall"]; reg = _region(x0, x1, lx)
        seed, grow = _grow(self, reg[0], DOWN)
        self.play(grow, run_time=1.3)
        self.play(FadeIn(reg[1]), run_time=0.4)
        self.play(FadeIn(_cap("the table's recall floor, applied")), run_time=0.5)
        _finish(self)


# ═══════════ B15 PREDICT ═══════════
class B15_Predict(Scene):
    BASE = 9.0
    def construct(self):
        st = _Stage(self, "Before It Lands", claim="sepsisP", axis="recall", region="recall", mark="0.88", bar=5, col=True)
        self.wait(0.4)
        swan = _dot(XC, 0.75, TERRA, 0.16)
        self.play(GrowFromCenter(swan), run_time=0.5)
        lab = _L(f"Michigan: {N_MICHIGAN:,} patients", XC + 0.4, 0.75, 32)
        self.play(FadeIn(lab), run_time=0.5)
        guide = DashedLine([XC, 0.5, 0], [XC, AY + 0.2, 0], color=DIM, stroke_width=3, dash_length=0.1)
        self.play(Create(guide), run_time=0.6)
        self.play(FadeIn(_cap("commit before it lands")), run_time=0.5)
        _finish(self)


# ═══════════ B16 TRANSFORM — the black swan ═══════════
class B16_BlackSwan(Scene):
    BASE = 8.0
    def construct(self):
        st = _Stage(self, "One Black Swan", claim="sepsisP", axis="recall", region="recall", mark="0.88", bar=5, col=True)
        swan = _dot(XC, 0.75, TERRA, 0.16)
        lab = _L(f"Michigan: {N_MICHIGAN:,} patients", XC + 0.4, 0.75, 32)
        guide = DashedLine([XC, 0.5, 0], [XC, AY + 0.2, 0], color=DIM, stroke_width=3, dash_length=0.1)
        self.add(swan, lab, guide)
        self.wait(0.3)
        self.play(swan.animate.move_to([XC, AY, 0]), FadeOut(guide), run_time=1.2)
        tick = Line([XC, AY - 0.16, 0], [XC, AY + 0.16, 0], color=INK, stroke_width=4)
        self.play(Create(tick), Transform(lab, _t("caught ≈ 1 in 3", 32, INK).move_to([XC, 0.45, 0])), run_time=0.7)
        self.play(Transform(st.fill, _bar_fill(0)), run_time=1.6)
        self.play(*[d.animate.set_color(GHOST) for d in st.col], run_time=0.8)
        self.play(FadeIn(_L("refuted", -3.2, TY2, 36, INK, bold=True)), run_time=0.5)
        self.play(FadeIn(_cap("missed roughly 2 of every 3")), run_time=0.5)
        _finish(self)


# ═══════════ B17 INSTANCE — four rows ═══════════
TAB_Y = [1.35, 0.25, -0.85, -1.95]
LEFT_CELLS = [("“The system", "is robust.”"), ("“The model", "performs well.”"), ("“The migration", "was a success.”"), ("“We have", "mitigated drift.”")]
RIGHT_CELLS = [("OOD error < 2%", "over a 30-day rolling window"), ("precision ≥ 0.91, recall ≥ 0.88", "held-out set, monthly"),
               ("zero data-loss events;", "p95 ≤ 120 ms at 48 h post-cutover"), ("PSI < 0.10 on the top 3 features", "week over week")]
class B17_FourRows(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "Four Claims, Two Columns", claim="sepsisP", axis="recall", region="recall", mark="0.88", bar=0, col=True, ghost_col=True, swan=True)
        self.wait(0.3)
        keep = [st.t]
        self.play(*[FadeOut(m) for m in self.mobjects if m not in keep], Transform(st.t, _title("Four Claims, Two Columns")), run_time=0.8)
        h1 = _t("forbids nothing", 32, DIM).move_to([-3.9, 2.1, 0]); h2 = _t("forbids a region", 32, DIM).move_to([2.4, 2.1, 0])
        rule = Line([-1.4, 2.4, 0], [-1.4, -2.45, 0], color=GHOST, stroke_width=3)
        self.play(FadeIn(h1), FadeIn(h2), Create(rule), run_time=0.7)
        for y, (la, lb), (ra, rb) in zip(TAB_Y, LEFT_CELLS, RIGHT_CELLS):
            left = VGroup(_L(la, -6.0, y + 0.23, 32), _L(lb, -6.0, y - 0.23, 32))
            right = VGroup(_L(ra, -0.4, y + 0.23, 32), _L(rb, -0.4, y - 0.23, 32))
            block = Rectangle(width=0.45, height=0.5, fill_color=DIM, fill_opacity=0.35, stroke_width=0).move_to([-0.85, y, 0])
            self.play(FadeIn(left), run_time=0.5)
            self.play(GrowFromEdge(block, DOWN), FadeIn(right), run_time=0.8)
        self.play(FadeIn(_cap("PSI is named here, not taught")), run_time=0.5)
        _finish(self)


# ═══════════ B18 ABSTRACTION — name it ═══════════
class B18_NameIt(Scene):
    BASE = 11.0
    def construct(self):
        t = _title("Falsifiable")
        self.add(t)
        name = _t("falsifiable", 44, INK, bold=True).move_to([0, -1.95, 0])
        defn = _t("names the observation that would make it false", 32, INK).move_to([0, -2.6, 0])
        self.play(FadeIn(name, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(defn), run_time=0.6)
        dots = VGroup(*[_dot(-4.6, y, INK, 0.1) for y in (0.9, 0.5, 0.1, -0.3, -0.7)])
        certain = DashedLine([-5.3, 1.5, 0], [-3.5, 1.5, 0], color=INK, stroke_width=3, dash_length=0.1)
        clab = _t("certain", 32, DIM).move_to([-2.7, 1.5, 0])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.2), Create(certain), FadeIn(clab), run_time=1.2)
        arrow = Arrow([-3.95, -0.8, 0], [-3.95, 1.15, 0], color=INK, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.12)
        self.play(GrowArrow(arrow), run_time=1.0)
        self.play(FadeIn(_t("confirmations pile up", 32, DIM).move_to([-4.1, -1.2, 0])), run_time=0.5)
        div = Line([-1.2, 1.9, 0], [-1.2, -1.35, 0], color=GHOST, stroke_width=3)
        self.play(Create(div), run_time=0.4)
        base = Line([0.6, -0.35, 0], [3.4, -0.35, 0], color=INK, stroke_width=3)
        swan = _dot(2.0, 0.25, TERRA, 0.16)
        self.play(Create(base), run_time=0.4)
        self.play(GrowFromCenter(swan), run_time=0.4)
        self.play(swan.animate.move_to([2.0, -0.35, 0]), run_time=0.6)
        self.play(FadeIn(_t("one refutation settles it", 32, DIM).move_to([2.1, -1.2, 0])), run_time=0.5)
        _finish(self)


# ═══════════ B19 PAYOFF ═══════════
class B19_Payoff(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "Back To The Dashboard", claim="robust", axis="error", dots=3, tally="compatible: 3 of 3")
        self.wait(3.6)                               # "…it survived every result because it forbade none."
        tiles = VGroup()
        for x, sub in ((1.0, "never at risk"), (4.2, "survived a test")):
            box = Rectangle(width=2.6, height=0.75, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([x, 1.15, 0])
            tiles.add(VGroup(box, _t("PASS", 32, INK, bold=True).move_to([x, 1.15, 0]), _t(sub, 32, DIM).move_to([x, 0.45, 0])))
        self.play(GrowFromEdge(tiles[0][0], DOWN), FadeIn(tiles[0][1]), FadeIn(tiles[0][2]), run_time=0.7)
        self.play(GrowFromEdge(tiles[1][0], DOWN), FadeIn(tiles[1][1]), FadeIn(tiles[1][2]), run_time=0.7)
        self.wait(2.6)                               # hold: the two tiles are indistinguishable
        self.play(FadeOut(tiles), run_time=0.5)
        mark = _mark(E2, "2%")
        self.play(Create(mark[0]), FadeIn(mark[1]), run_time=0.5)
        x0, x1, lx = REGION["error"]; reg = _region(x0, x1, lx)
        seed, grow = _grow(self, reg[0], LEFT)
        self.play(grow, FadeIn(reg[1]), run_time=1.2)
        self.play(Transform(st.tally, _tally("refuted: 2 of 3", bold=True)), run_time=0.5)
        self.play(GrowFromCenter(Dot([-2.45, TALLY_Y, 0], color=TERRA, radius=0.14)), run_time=0.4)
        self.play(FadeIn(_cap("not taught here: the line first")), run_time=0.5)
        _finish(self)
