"""
Manim scenes for tldr-hold-one-fair (tldr skill — LEARN section 1, B10–B19).

The one representation: each group is a unit square. Its POSITIVE column is as
wide as the group's base rate (0.6 for A, 0.3 for B); the model's flags fill each
column from the bottom — the positive column to the true-positive rate (ink), the
negative column to the false-positive rate (grey). Gather the flagged area into
one horizontal "pile" bar: its dark share is PPV. The pile's dark-to-grey ratio is
a width ratio (the world's base-rate odds) times a height ratio (the model's
TPR/FPR) — the odds identity, read straight off the squares.

Every number is recomputed from the chapter's inputs at import and asserted
(FACTCHECK.md). INK text on the cream stage; terracotta is one accent per scene —
a dot or an X beside a word — never text, never a thin line, never a ring (GATE T).
Gate A: every scene creates a new geometric object before its final play.
Explicit coordinates inside ±6.2 × ±3.3. Type floor 32 (titles 40). Captions
≤ 34 chars, centred at x ≈ 3.2. No slant=ITALIC on multi-word text.
"""
import json as _json, os as _os
import numpy as np
from manim import *

STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the chapter's numbers ═══════════
P = {"A": 0.6, "B": 0.3}
CAL = {"A": (0.60, 0.30), "B": (0.70, 0.10)}      # calibration-satisfying table
EO = {"A": (0.70, 0.15), "B": (0.70, 0.15)}       # equalized-odds-satisfying table
SAME = {"A": (0.60, 0.30), "B": (0.60, 0.30)}     # A's rates copied onto B (derived)
def ppv(g, cfg): p = P[g]; t, f = cfg[g]; return p * t / (p * t + (1 - p) * f)
def yes(g, cfg): p = P[g]; t, f = cfg[g]; return p * t + (1 - p) * f
def podds(g, cfg): p = P[g]; t, f = cfg[g]; return (p * t) / ((1 - p) * f)
assert abs(ppv("A", CAL) - 0.75) < 1e-12 and abs(ppv("B", CAL) - 0.75) < 1e-12
assert abs(ppv("A", EO) - 0.875) < 1e-12 and abs(ppv("B", EO) - 2 / 3) < 1e-12
assert abs(ppv("B", SAME) - 0.4615384615) < 1e-9
assert abs(yes("A", CAL) - 0.48) < 1e-12 and abs(yes("B", CAL) - 0.28) < 1e-12
assert abs(yes("A", EO) - 0.48) < 1e-12 and abs(yes("B", EO) - 0.315) < 1e-12
for cfg in (CAL, EO, SAME):
    for g in "AB":
        t, f = cfg[g]; assert abs(podds(g, cfg) - P[g] / (1 - P[g]) * t / f) < 1e-9     # the odds identity
assert abs(podds("A", CAL) - 3) < 1e-9 and abs(podds("B", CAL) - 3) < 1e-9
assert abs(podds("A", EO) - 7) < 1e-9 and abs(podds("B", EO) - 2) < 1e-9

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
def _title(txt, size=40): return Text(txt, font=SERIF, color=INK, font_size=size).move_to([0, 3.0, 0])
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _m(tex, size=44, color=INK): return MathTex(tex, font_size=size, color=color)
def _cap(txt, x=3.2, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -3.05, 0])
def _x(x, y, s=0.17, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _ok(x, y, w=7):
    return VGroup(Line([x - 0.17, y + 0.02, 0], [x - 0.05, y - 0.13, 0], color=INK, stroke_width=w),
                  Line([x - 0.05, y - 0.13, 0], [x + 0.19, y + 0.17, 0], color=INK, stroke_width=w))
def _q(x, y): return _t("?", 36).move_to([x, y, 0])
def _mark(kind, x, y): return {"x": _x, "ok": _ok}[kind](x, y) if kind in ("x", "ok") else _q(x, y)
def _dot(x, y, r=0.13): return Dot([x, y, 0], color=TERRA, radius=r)
def _target():
    tx = 2.2 + 0.75 * 2.8
    return Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.13).move_to([tx, -0.8, 0])

# ═══════════ stage geometry ═══════════
S = 3.0                                   # square side
SQ_X0 = {"A": -5.8, "B": -2.2}            # left edges
Y0 = -1.35                                # square bottom (top = 1.65)
def CX(g): return SQ_X0[g] + S / 2
def SPLIT(g): return SQ_X0[g] + P[g] * S  # the base-rate divider
def POSC(g): return (SQ_X0[g] + SPLIT(g)) / 2
def NEGC(g): return (SPLIT(g) + SQ_X0[g] + S) / 2
GL_Y, PM_Y, RD_Y = 2.45, 1.95, -1.72     # group label, +/− marks, TPR·FPR readout

# right panel
ASK_Y = [2.0, 1.45, 0.9]; ASK_X = 2.05; MARK_X = 1.65
PILE_X0, PILE_L, PILE_H = 2.2, 2.8, 0.4
PILE_Y = {"A": 0.3, "B": -0.35}; PILE_LAB_X = 1.85; PILE_VAL_X = 5.55; LLAB_X = 1.7
PHEAD_Y = 0.85
LINE_Y = {"A": -1.2, "B": -1.85}; LINE_CX = 4.05

def _fill(g, cfg, which):
    t, f = cfg[g]
    if which == "pos":
        w, h, cx, col = P[g] * S, max(t * S, 0.02), POSC(g), INK
    else:
        w, h, cx, col = (1 - P[g]) * S, max(f * S, 0.02), NEGC(g), DIM
    return Rectangle(width=w, height=h, fill_color=col, fill_opacity=1, stroke_color=STAGE, stroke_width=2).move_to([cx, Y0 + h / 2, 0])

def _readout(g, cfg):
    t, f = cfg[g]
    return VGroup(_t(f"TPR {t:.2f}", 32).move_to([CX(g), RD_Y, 0]), _t(f"FPR {f:.2f}", 32).move_to([CX(g), RD_Y - 0.48, 0]))

def _pile(g, cfg, dy=0.0):
    v = ppv(g, cfg); y = PILE_Y[g] + dy
    wd = v * PILE_L; wg = PILE_L - wd
    dark = Rectangle(width=wd, height=PILE_H, fill_color=INK, fill_opacity=1, stroke_color=STAGE, stroke_width=2).move_to([PILE_X0 + wd / 2, y, 0])
    grey = Rectangle(width=wg, height=PILE_H, fill_color=DIM, fill_opacity=1, stroke_color=STAGE, stroke_width=2).move_to([PILE_X0 + wd + wg / 2, y, 0])
    return VGroup(dark, grey)
def _pile_val(g, cfg, dy=0.0): return _t(f"{ppv(g, cfg):.2f}", 36).move_to([PILE_VAL_X, PILE_Y[g] + dy, 0])
def _boundary_x(g, cfg): return PILE_X0 + ppv(g, cfg) * PILE_L

def _num(x):
    s = f"{x:.3f}".rstrip("0").rstrip(".")
    return s
def _odds_line(g, cfg):
    p = P[g]; t, f = cfg[g]
    a, b = p * t, (1 - p) * f; k = a / b
    tex = rf"{_num(a)} : {_num(b)}"
    if abs(k - round(k)) < 1e-9: tex += rf" \;=\; {int(round(k))} : 1"
    return _m(tex, 40).move_to([LINE_CX, LINE_Y[g], 0])

FX = [3.0, None, 3.95, None, 5.33]         # factor-line piece centres: lhs, =, world, ×, model
def _factor_line(g, cfg):
    p = P[g]; t, f = cfg[g]
    k = podds(g, cfg); w = p / (1 - p); h = t / f
    lhs = f"{int(round(k))}" if abs(k - round(k)) < 1e-9 else f"{k:.2f}"
    wt = f"{w:.2f}".rstrip("0").rstrip("."); ht = f"{int(round(h))}" if abs(h - round(h)) < 1e-9 else f"{h:.2f}"
    parts = [(lhs + r" \;=", 3.0), (wt + r" \;\times", 4.12), (ht, 5.33)]     # "=" and "×" ride with a number: a lone glyph reads as a sub-floor text run (GATE T)
    return VGroup(*[_m(t, 44).move_to([x, LINE_Y[g], 0]) for t, x in parts])


class _Stage:
    """The persistent world: two squares (+ fills per cfg), asks with marks, piles, ratio lines."""
    def __init__(self, scene, title, cfg=None, asks=True, marks=("q", "q"), piles=(), lines=None, arrows=False, pile_dy=0.0, head=True):
        self.scene = scene; self.cfg = cfg; self.pdy = pile_dy
        self.t = _title(title)
        self.sq = {g: Rectangle(width=S, height=S, stroke_color=INK, stroke_width=3, fill_opacity=0).move_to([CX(g), Y0 + S / 2, 0]) for g in "AB"}
        self.div = {g: Line([SPLIT(g), Y0, 0], [SPLIT(g), Y0 + S, 0], color=INK, stroke_width=2) for g in "AB"}
        self.gl = {g: _t(f"{g} · {int(P[g] * 100)}% positive", 32).move_to([CX(g), GL_Y, 0]) for g in "AB"}
        self.pm = {g: VGroup(_t("+", 36, DIM).move_to([POSC(g), PM_Y, 0]), _t("−", 36, DIM).move_to([NEGC(g), PM_Y, 0])) for g in "AB"}
        scene.add(self.t, *self.sq.values(), *self.div.values(), *self.gl.values())
        if arrows:
            self.pm = {g: self._arrows(g) for g in "AB"}
        scene.add(*self.pm.values())
        self.fills = {}; self.rd = {}
        if cfg:
            for g in cfg:
                self.fills[g] = VGroup(_fill(g, cfg, "pos"), _fill(g, cfg, "neg")); self.rd[g] = _readout(g, cfg)
                scene.add(self.fills[g], self.rd[g])
        self.asks = []; self.marks = []
        if asks:
            self.asks = [_t("1 · flags mean the same", 32).move_to([ASK_X, ASK_Y[0], 0], aligned_edge=LEFT),
                         _t("2 · errors land evenly", 32).move_to([ASK_X, ASK_Y[1], 0], aligned_edge=LEFT)]
            self.marks = [_mark(m, MARK_X, y) for m, y in zip(marks, ASK_Y)]
            scene.add(*self.asks, *self.marks)
        self.piles = {}; self.pvals = {}; self.plabs = {}; self.phead = None
        if piles:
            if head:
                self.phead = _t("flagged pile · PPV", 32, DIM).move_to([3.6, PHEAD_Y, 0]); scene.add(self.phead)
            for g in piles:
                self.piles[g] = _pile(g, cfg, pile_dy); self.pvals[g] = _pile_val(g, cfg, pile_dy)
                self.plabs[g] = _t(g, 32).move_to([PILE_LAB_X, PILE_Y[g] + pile_dy, 0])
                scene.add(self.piles[g], self.pvals[g], self.plabs[g])
        self.lines = {}; self.llabs = {}; self.mode = lines
        if lines:
            for g in "AB":
                self.lines[g] = (_odds_line if lines == "odds" else _factor_line)(g, cfg)
                self.llabs[g] = _t(g + ":", 32, DIM).move_to([LLAB_X, LINE_Y[g], 0])
                scene.add(self.lines[g], self.llabs[g])

    def _arrows(self, g):
        y = PM_Y
        a1 = DoubleArrow([SQ_X0[g] + 0.06, y, 0], [SPLIT(g) - 0.06, y, 0], color=INK, stroke_width=3, buff=0, tip_length=0.14, max_tip_length_to_length_ratio=0.3)
        a2 = DoubleArrow([SPLIT(g) + 0.06, y, 0], [SQ_X0[g] + S - 0.06, y, 0], color=INK, stroke_width=3, buff=0, tip_length=0.14, max_tip_length_to_length_ratio=0.3)
        return VGroup(a1, a2)

    def fill_in(self, g, cfg):
        """grow group g's fills from the bottom (first appearance)."""
        self.cfg = dict(self.cfg or {}); self.cfg[g] = cfg[g]
        self.fills[g] = VGroup(_fill(g, cfg, "pos"), _fill(g, cfg, "neg")); self.rd[g] = _readout(g, cfg)
        return [GrowFromEdge(self.fills[g][0], DOWN), GrowFromEdge(self.fills[g][1], DOWN), FadeIn(self.rd[g])]

    def to(self, cfg, marks=None):
        """animations moving every present object to configuration cfg (transform, don't cut)."""
        self.cfg = cfg; an = []
        for g in self.fills:
            an += [Transform(self.fills[g][0], _fill(g, cfg, "pos")), Transform(self.fills[g][1], _fill(g, cfg, "neg")),
                   Transform(self.rd[g], _readout(g, cfg))]
        for g in self.piles:
            an += [Transform(self.piles[g], _pile(g, cfg, self.pdy)), Transform(self.pvals[g], _pile_val(g, cfg, self.pdy))]
        for g in self.lines:
            an.append(Transform(self.lines[g], (_odds_line if self.mode == "odds" else _factor_line)(g, cfg)))
        if marks:
            for i, m in enumerate(marks):
                new = _mark(m, MARK_X, ASK_Y[i]); an.append(ReplacementTransform(self.marks[i], new)); self.marks[i] = new
        return an


def _b10_extras():
    return VGroup(_dot(POSC("B"), 1.15),
                  _t("1 → calibration", 32, DIM).move_to([ASK_X, 0.6, 0], aligned_edge=LEFT),
                  _t("2 → equalized odds", 32, DIM).move_to([ASK_X, 0.05, 0], aligned_edge=LEFT),
                  _t("tune our way to both?", 36).move_to([3.9, -1.0, 0]),
                  _cap("the chapter's constructed numbers"))


class B10_TwoAsks(Scene):
    BASE = 13.0
    def construct(self):
        t = _title("Two Groups, Two Asks"); self.add(t)
        sq = {g: Rectangle(width=S, height=S, stroke_color=INK, stroke_width=3, fill_opacity=0).move_to([CX(g), Y0 + S / 2, 0]) for g in "AB"}
        self.play(Create(sq["A"]), Create(sq["B"]), run_time=0.9)
        for g in "AB":
            mid = SQ_X0[g] + S / 2
            d = Line([mid, Y0, 0], [mid, Y0 + S, 0], color=INK, stroke_width=2)
            self.play(Create(d), run_time=0.3)
            gl = _t(f"{g} · {int(P[g] * 100)}% positive", 32).move_to([CX(g), GL_Y, 0])
            pm = VGroup(_t("+", 36, DIM).move_to([POSC(g), PM_Y, 0]), _t("−", 36, DIM).move_to([NEGC(g), PM_Y, 0]))
            self.play(d.animate.move_to([SPLIT(g), Y0 + S / 2, 0]), FadeIn(gl), FadeIn(pm), run_time=1.0)
        ex = _b10_extras()
        self.play(GrowFromCenter(ex[0]), run_time=0.4)
        a1 = _t("1 · flags mean the same", 32).move_to([ASK_X, ASK_Y[0], 0], aligned_edge=LEFT)
        self.play(FadeIn(a1, shift=RIGHT * 0.15), run_time=0.6)
        self.play(FadeIn(ex[1]), run_time=0.4)
        a2 = _t("2 · errors land evenly", 32).move_to([ASK_X, ASK_Y[1], 0], aligned_edge=LEFT)
        self.play(FadeIn(a2, shift=RIGHT * 0.15), run_time=0.6)
        self.play(FadeIn(ex[2]), run_time=0.4)
        self.play(FadeIn(_q(MARK_X, ASK_Y[0])), FadeIn(_q(MARK_X, ASK_Y[1])), run_time=0.4)
        self.play(FadeIn(ex[3]), run_time=0.5)
        self.play(FadeIn(ex[4]), run_time=0.5)
        _finish(self)


class B11_GroupA(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "Group A's Flags")
        ex = _b10_extras(); self.add(ex)
        self.wait(0.3)
        self.play(FadeOut(ex), run_time=0.5)
        an = st.fill_in("A", CAL)
        self.play(an[0], run_time=1.0)
        self.play(an[1], an[2], run_time=1.0)
        head = _t("flagged pile · PPV", 32, DIM).move_to([3.6, PHEAD_Y, 0])
        pile = _pile("A", CAL)
        self.play(FadeIn(head), FadeIn(_t("A", 32).move_to([PILE_LAB_X, PILE_Y["A"], 0])), run_time=0.4)
        self.play(ReplacementTransform(st.fills["A"][0].copy(), pile[0]), ReplacementTransform(st.fills["A"][1].copy(), pile[1]), run_time=1.6)
        self.play(Write(_odds_line("A", CAL)), FadeIn(_t("A:", 32, DIM).move_to([LLAB_X, LINE_Y["A"], 0])), run_time=0.9)
        self.play(FadeIn(_pile_val("A", CAL)), GrowFromCenter(_dot(PILE_VAL_X, PILE_Y["A"] + 0.5)), run_time=0.5)
        self.play(FadeIn(_cap("a flag in A: right 3 times in 4")), run_time=0.5)
        _finish(self)


class B12_GroupB(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "Same Rates in Group B", cfg={"A": SAME["A"]}, piles=("A",), lines=None)
        self.add(_odds_line("A", SAME), _t("A:", 32, DIM).move_to([LLAB_X, LINE_Y["A"], 0]))
        self.wait(0.4)
        an = st.fill_in("B", SAME)
        self.play(*an, run_time=1.6)
        pile = _pile("B", SAME)
        self.play(FadeIn(_t("B", 32).move_to([PILE_LAB_X, PILE_Y["B"], 0])), run_time=0.3)
        self.play(ReplacementTransform(st.fills["B"][0].copy(), pile[0]), ReplacementTransform(st.fills["B"][1].copy(), pile[1]), run_time=1.6)
        self.play(Write(_odds_line("B", SAME)), FadeIn(_t("B:", 32, DIM).move_to([LLAB_X, LINE_Y["B"], 0])), run_time=0.8)
        self.play(FadeIn(_pile_val("B", SAME)), run_time=0.5)
        self.play(ReplacementTransform(st.marks[1], _ok(MARK_X, ASK_Y[1])), run_time=0.5)
        self.play(ReplacementTransform(st.marks[0], _x(MARK_X, ASK_Y[0])), run_time=0.5)
        self.play(FadeIn(_cap("same rates, different meaning")), run_time=0.5)
        _finish(self)


class B13_BetterModel(Scene):
    BASE = 11.0
    def construct(self):
        st = _Stage(self, "A Better Model", cfg=SAME, marks=("x", "ok"), piles=("A", "B"), lines="odds")
        self.wait(0.4)
        self.play(*st.to(EO), run_time=2.4)
        gA = DashedLine([_boundary_x("A", EO), PILE_Y["A"] + 0.35, 0], [_boundary_x("A", EO), PILE_Y["B"] - 0.35, 0], color=INK, stroke_width=3, dash_length=0.08)
        gB = DashedLine([_boundary_x("B", EO), PILE_Y["A"] + 0.35, 0], [_boundary_x("B", EO), PILE_Y["B"] - 0.35, 0], color=INK, stroke_width=3, dash_length=0.08)
        self.play(Create(gA), run_time=0.6)
        self.play(Create(gB), run_time=0.6)
        self.play(FadeIn(_cap("better model, same gap")), run_time=0.5)
        _finish(self)


class B14_WidthsTimesHeights(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "Widths Times Heights", cfg=EO, marks=("x", "ok"), piles=("A", "B"), lines="odds")
        self.wait(0.4)
        new = {g: _factor_line(g, EO) for g in "AB"}
        for g in "AB":
            self.play(FadeOut(st.lines[g]), FadeIn(new[g][0]), FadeIn(new[g][1]), run_time=0.8)
        self.play(FadeIn(_t("world", 32, DIM).move_to([FX[2], -2.45, 0])), run_time=0.5)
        self.play(*[FadeIn(new[g][2]) for g in "AB"], run_time=0.8)
        self.play(FadeIn(_t("model", 32, DIM).move_to([FX[4], -2.45, 0])), run_time=0.5)
        self.play(GrowFromCenter(_dot(POSC("B"), 1.2)), run_time=0.4)
        self.play(FadeIn(_cap("same heights, unequal piles")), run_time=0.5)
        _finish(self)


class B15_Commit(Scene):
    BASE = 10.0
    def construct(self):
        st = _Stage(self, "Commit", cfg=EO, marks=("x", "ok"), piles=("A", "B"), lines="factors")
        self.add(_t("world", 32, DIM).move_to([FX[2], -2.45, 0]), _t("model", 32, DIM).move_to([FX[4], -2.45, 0]))
        self.wait(0.4)
        self.play(GrowFromCenter(_target()), run_time=0.8)
        self.play(GrowFromCenter(_dot(NEGC("B"), Y0 + EO["B"][1] * S + 0.35)), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(_cap("B's false alarms: up or down?")), run_time=0.5)
        _finish(self)


class B16_PinOneBreakOther(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "Pin One, Break the Other", cfg=EO, marks=("x", "ok"), piles=("A", "B"), lines="factors")
        wl = _t("world", 32, DIM).move_to([FX[2], -2.45, 0]); ml = _t("model", 32, DIM).move_to([FX[4], -2.45, 0])
        self.add(wl, ml)
        self.wait(0.3)
        self.play(*st.to(CAL, marks=("ok", "x")), run_time=2.6)
        hit = _target()
        self.play(GrowFromCenter(hit), run_time=0.5)
        self.wait(0.6)
        self.play(*st.to(EO, marks=("x", "ok")), FadeOut(hit), run_time=1.8)
        self.wait(0.4)
        self.play(*st.to(CAL, marks=("ok", "x")), run_time=1.8)
        self.play(GrowFromCenter(_target()), run_time=0.4)
        _finish(self)


class B17_TheIdentity(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "One Line, Two Groups", cfg=CAL, marks=("ok", "x"), piles=("A", "B"), lines="factors")
        self.wait(0.3)
        gone = [*st.asks, *st.marks, st.phead, *st.piles.values(), *st.pvals.values(), *st.plabs.values(), *st.lines.values(), *st.llabs.values()]
        self.play(*[FadeOut(m) for m in gone], run_time=0.6)
        EQ_Y = 1.1; XS = [2.15, None, 4.05, None, 5.35]     # "=" and "·" ride with a fraction (GATE T: no lone glyph runs)
        parts = [(r"\frac{v}{1-v} \;=", 2.3), (r"\frac{p}{1-p}\,\cdot", 4.2), (r"\frac{t}{f}", 5.35)]
        eq = [_m(t, 52).move_to([x, EQ_Y, 0]) for t, x in parts]
        self.play(Write(eq[0]), run_time=0.8)
        self.play(Write(eq[1]), run_time=0.6)
        self.play(Write(eq[2]), run_time=0.6)
        words = [_t("pile", 32, DIM).move_to([XS[0], 0.15, 0]), _t("widths", 32, DIM).move_to([XS[2], 0.15, 0]), _t("heights", 32, DIM).move_to([5.5, 0.15, 0])]
        self.play(*[FadeIn(w) for w in words], run_time=0.6)
        self.play(GrowFromCenter(_dot(XS[2], 2.0)), run_time=0.4)
        self.play(FadeIn(_t("pin one, the other splits", 32).move_to([3.85, -0.75, 0])), run_time=0.6)
        ex = _t("the only exits:", 32, DIM).move_to([2.9, -1.55, 0])
        e1 = _m(r"p_A = p_B", 44).move_to([2.8, -2.25, 0]); e2 = _m(r"f = 0", 44).move_to([5.1, -2.25, 0])
        d1 = Dot([1.8, -2.25, 0], color=INK, radius=0.09); d2 = Dot([4.3, -2.25, 0], color=INK, radius=0.09)
        self.play(FadeIn(ex), run_time=0.4)
        self.play(GrowFromCenter(d1), Write(e1), run_time=0.6)
        self.play(GrowFromCenter(d2), Write(e2), run_time=0.6)
        _finish(self)


class B18_Tangent(Scene):
    BASE = 17.0
    def construct(self):
        t = _title("Read the Line"); self.add(t)
        eq = _m(r"\frac{v}{1-v} \;=\; \frac{p}{1-p}\cdot\frac{t}{f}", 64).move_to([-3.4, 1.35, 0])
        self.play(FadeIn(eq), run_time=0.7)
        div = Line([0.2, 2.3, 0], [0.2, -2.6, 0], color=GHOST, stroke_width=2)
        self.play(Create(div), run_time=0.4)
        rows = [("left: dark over grey in the pile", 2.0), ("right: widths times heights", 1.4), ("=  exactly, in every group", 0.8)]
        for s, y in rows:
            self.play(FadeIn(_t(s, 32).move_to([0.5, y, 0], aligned_edge=LEFT), shift=RIGHT * 0.15), run_time=0.7)
        gl = [("v", "PPV, the dark share"), ("p", "base rate, a width"), ("t, f", "TPR, FPR, the heights")]
        for i, (sym, mean) in enumerate(gl):
            y = -0.05 - i * 0.6
            self.play(FadeIn(_t(sym, 32, INK, bold=True).move_to([0.5, y, 0], aligned_edge=LEFT)),
                      FadeIn(_t(mean, 32).move_to([1.6, y, 0], aligned_edge=LEFT), shift=RIGHT * 0.1), run_time=0.6)
        wB = _m(r"\text{B: }\tfrac{3}{7}\cdot 7 = 3 \;\Rightarrow\; v = 0.75", 44).move_to([-3.2, -0.35, 0])
        wA = _m(r"\text{A: }1.5\cdot 2 = 3 \;\Rightarrow\; v = 0.75", 44).move_to([-3.2, -1.35, 0])
        self.play(Write(wB), run_time=0.9)
        self.play(Write(wA), run_time=0.7)
        self.play(GrowFromCenter(_dot(-3.2, -2.1)), run_time=0.4)
        self.play(FadeIn(_cap("both piles three to one", x=-3.0)), run_time=0.5)
        _finish(self)


class B19_Payoff(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "Tuning Picks Which Breaks", cfg=CAL, marks=("ok", "x"), piles=("A", "B"), pile_dy=-0.15, head=False)
        self.wait(1.2)
        self.play(*st.to(EO, marks=("x", "ok")), run_time=2.0)
        self.wait(0.6)
        a3 = _t("3 · equal yes-rates", 32).move_to([ASK_X, ASK_Y[2], 0], aligned_edge=LEFT)
        m3 = _x(MARK_X, ASK_Y[2])
        self.play(FadeIn(a3), Create(m3), run_time=0.7)
        ylab = _t("yes-rates", 32, DIM).move_to([2.55, -1.25, 0])
        y1 = _m(r"0.48 \;\text{vs}\; 0.28", 40).move_to([4.75, -1.25, 0])
        y2 = _m(r"0.48 \;\text{vs}\; 0.32", 40).move_to([4.75, -1.8, 0])
        self.play(FadeIn(ylab), Write(y1), run_time=0.6)
        self.play(Write(y2), run_time=0.6)
        give = _t("one must give: you choose", 32, INK, bold=True).move_to([3.55, -2.4, 0])
        self.play(FadeIn(give), run_time=0.7)
        self.play(FadeIn(_cap("not taught: the three-way proof")), run_time=0.5)
        _finish(self)
