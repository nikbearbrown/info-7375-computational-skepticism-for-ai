"""
Manim scenes for tldr-robust-against-what (tldr skill — LEARN section 1, B10–B19).

One persistent object: the chapter's disclosure TABLE, filled one row at a time.
Every row keeps a dim CLEAN bar fixed at 94 and grows an ink ROBUST bar to its own
height (71 white-box ε = 0.03 · 58 transfer · 87 natural shift). The values are the
chapter's TEMPLATE values (a form with blanks, not a measured model) — a small dim
caption "template values — illustrative" stays on the stage from B11 on.

State factory: `_Table(scene, **state)` rebuilds the table at the previous beat's end
state, so the last frame of Bk is the first frame of Bk+1 (transform, don't cut).
Numbers are asserted at import (FACTCHECK.md). INK text on the cream stage;
terracotta is ONE accent per scene — a dot or an X beside a word, never text, never
a line, never a bar, never a ring (GATE T). Explicit coords inside ±6.2 × ±3.3.
Type floor 32 (titles 40). Captions ≤ 34 chars, centred at x ≈ 3.3.
"""
import json as _json, os as _os
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the chapter's template (Section 1 — Robustness profile) ═══════════
CLEAN = 94
ROWS = [("white-box attack", "ε = 0.03", 71),
        ("transfer attack", "surrogate model", 58),
        ("natural shift", "time shift only", 87)]
assert [r[2] for r in ROWS] == [71, 58, 87] and all(r[2] < CLEAN for r in ROWS)

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
def _cap(txt, x=3.3, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -2.85, 0])
def _illus(): return _t("template values — illustrative", 32, DIM).move_to([-3.4, -2.85, 0])
def _x(x, y, s=0.2, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _dot(x, y, r=0.13): return Dot([x, y, 0], color=TERRA, radius=r)

# ═══════════ table geometry ═══════════
LX = -5.8                         # left edge of row labels
BX0, BW = -1.2, 5.0               # bar origin; 100 % = 5.0 units
ROW_Y = [1.25, 0.15, -0.95]
HEAD_Y = 2.2
BLANK_Y = -1.95
BH = 0.26
def CY(i): return ROW_Y[i] + 0.2          # clean bar centre-line
def RY(i): return ROW_Y[i] - 0.2          # robust bar centre-line
def BEND(v): return BX0 + v / 100 * BW    # where a bar of value v ends
def LABX(v): return BEND(v) + 0.2         # left edge of its value label

def _bar(v, y, color=INK):
    w = max(v / 100 * BW, 0.02)
    return Rectangle(width=w, height=BH, fill_color=color, fill_opacity=1, stroke_width=0).move_to([BX0 + w / 2, y, 0])
def _val(v, y, color=INK):
    return _t(f"{v}%", 32, color).move_to([LABX(v), y, 0], aligned_edge=LEFT)
def _qmark(y): return _t("?", 36, INK).move_to([BX0 + 0.3, y, 0])
def _rowlabels(i):
    name, budget, _ = ROWS[i]
    return VGroup(_t(name, 32, INK).move_to([LX, ROW_Y[i] + 0.2, 0], aligned_edge=LEFT),
                  _t(budget, 32, DIM).move_to([LX, ROW_Y[i] - 0.22, 0], aligned_edge=LEFT))
def _claim(size=32, color=DIM):
    return _t("“94% accurate, and robust.”", size, color).move_to([LX, HEAD_Y, 0], aligned_edge=LEFT)
ROBUST_GLYPHS = slice(16, 22)             # 'robust' inside the claim (spaces are not glyphs)
def _legend():
    return VGroup(Rectangle(width=0.32, height=0.22, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to([1.35, HEAD_Y, 0]),
                  _t("clean", 32, DIM).move_to([1.65, HEAD_Y, 0], aligned_edge=LEFT),
                  Rectangle(width=0.32, height=0.22, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([2.95, HEAD_Y, 0]),
                  _t("robust at budget", 32, INK).move_to([3.25, HEAD_Y, 0], aligned_edge=LEFT))
def _blanks():
    return VGroup(_t("2 · residual risk", 32, INK).move_to([LX, BLANK_Y, 0], aligned_edge=LEFT),
                  Line([-2.6, BLANK_Y - 0.14, 0], [-0.4, BLANK_Y - 0.14, 0], color=DIM, stroke_width=3),
                  _t("3 · monitoring trigger", 32, INK).move_to([0.1, BLANK_Y, 0], aligned_edge=LEFT),
                  Line([4.1, BLANK_Y - 0.14, 0], [5.9, BLANK_Y - 0.14, 0], color=DIM, stroke_width=3))
def _ticks():
    g = VGroup()
    for v in (58, 71):
        g.add(Line([BEND(v), RY(2) - 0.26, 0], [BEND(v), RY(2) + 0.26, 0], color=DIM, stroke_width=4))
    return g
def _tick_labels():
    return VGroup(*[_t(str(v), 32, DIM).move_to([BEND(v), RY(2) - 0.52, 0]) for v in (58, 71)])


class _Table:
    """The disclosure table at a given state. rows = how many rows are fully filled
    (0–3); row3 = 'clean' shows row three's labels + clean bar + '?'; merged = the
    robust bars of rows 1–2 folded into the word; ticks = the B15 guides; blanks =
    Sections 2 and 3; header = 'claim' | 'section'; rail = the B18 rail."""
    def __init__(self, scene, title, rows=0, row3=False, merged=False, ticks=False, blanks=False,
                 header="claim", rail=False, illus=True):
        self.t = _title(title); scene.add(self.t)
        self.head = _claim() if header == "claim" else _t("1 · the profile", 32, INK).move_to([LX, HEAD_Y, 0], aligned_edge=LEFT)
        self.legend = _legend(); scene.add(self.head, self.legend)
        self.labels, self.clean, self.cval, self.rob, self.rval = VGroup(), VGroup(), VGroup(), VGroup(), VGroup()
        n = max(rows, 3 if row3 else 0)
        for i in range(n):
            self.labels.add(_rowlabels(i))
            self.clean.add(_bar(CLEAN, CY(i), DIM)); self.cval.add(_val(CLEAN, CY(i), DIM))
            if i < rows:
                self.rob.add(_bar(ROWS[i][2], RY(i))); self.rval.add(_val(ROWS[i][2], RY(i)))
        scene.add(self.labels, self.clean, self.cval)
        self.q = None
        if row3 and rows < 3:
            self.q = _qmark(RY(2)); scene.add(self.q)
        self.word = None
        if merged:
            self.word = _t("robust", 40, INK, bold=True).move_to([0.8, -1.0, 0]); scene.add(self.word)
            self.rob3 = VGroup(*self.rob[2:]); self.rval3 = VGroup(*self.rval[2:]); scene.add(self.rob3, self.rval3)
        else:
            scene.add(self.rob, self.rval)
        self.ticks = _ticks() if ticks else None
        if ticks: scene.add(self.ticks)
        self.blanks = _blanks() if blanks else None
        if blanks: scene.add(self.blanks)
        self.rail = Line([-6.1, 2.4, 0], [-6.1, -2.1, 0], color=INK, stroke_width=3) if rail else None
        if rail: scene.add(self.rail)
        self.illus = _illus() if illus else None
        if illus: scene.add(self.illus)


# ═══════════ B10 — HOOK ═══════════
def _hook_objects():
    sent = _t("“94% accurate, and robust.”", 48, INK).move_to([0, 1.25, 0])
    bar = _bar(CLEAN, 0.2); lab = _val(CLEAN, 0.2)
    track = DashedLine([BX0, -0.55, 0], [BEND(CLEAN), -0.55, 0], color=DIM, stroke_width=3, dash_length=0.12)
    tlab = _t("robust", 32, DIM).move_to([BX0 - 0.3, -0.55, 0], aligned_edge=RIGHT)
    tq = _t("?", 36, INK).move_to([LABX(CLEAN) + 0.1, -0.55, 0])
    return sent, bar, lab, track, tlab, tq


class B10_TheSlide(Scene):
    BASE = 10.0
    def construct(self):
        t = _title("One Slide")
        sent, bar, lab, track, tlab, tq = _hook_objects()
        self.add(t)
        self.play(FadeIn(sent), run_time=0.8)
        self.play(GrowFromEdge(bar, LEFT), FadeIn(lab), run_time=1.0)
        self.play(GrowFromCenter(_dot(3.95, 1.25)), run_time=0.4)
        self.play(Create(track), FadeIn(tlab), run_time=0.9)
        self.play(FadeIn(tq), run_time=0.4)
        self.play(FadeIn(_t("robust — against what?", 40).move_to([0, -1.7, 0])), run_time=0.7)
        self.play(FadeIn(_cap("the number has a bar; the word?")), run_time=0.5)
        _finish(self)


# ═══════════ B11 — INSTANCE 1: row one ═══════════
class B11_WhiteBox(Scene):
    BASE = 12.0
    def construct(self):
        t = _title("One Slide")
        sent, bar, lab, track, tlab, tq = _hook_objects()
        q = _t("robust — against what?", 40).move_to([0, -1.7, 0]); cap0 = _cap("the number has a bar; the word?")
        dot0 = _dot(3.95, 1.25)
        self.add(t, sent, bar, lab, track, tlab, tq, q, cap0, dot0)
        self.wait(0.4)
        self.play(FadeOut(track), FadeOut(tlab), FadeOut(tq), FadeOut(q), FadeOut(cap0), FadeOut(dot0),
                  Transform(t, _title("Row One: White-Box")),
                  Transform(sent, _claim()), bar.animate.move_to([BX0 + CLEAN / 200 * BW, CY(0), 0]).set_fill(DIM),
                  Transform(lab, _val(CLEAN, CY(0), DIM)), run_time=1.4)
        self.play(FadeIn(_legend()), FadeIn(_rowlabels(0)), run_time=0.8)
        rb = _bar(ROWS[0][2], RY(0))
        self.play(GrowFromEdge(rb, LEFT), run_time=1.2)
        self.play(FadeIn(_val(71, RY(0))), GrowFromCenter(_dot(LABX(71) + 1.0, RY(0))), run_time=0.5)
        self.play(FadeIn(_illus()), run_time=0.5)
        self.play(FadeIn(_cap("one attack, one budget")), run_time=0.5)
        _finish(self)


# ═══════════ B12 — INSTANCE 2: row two ═══════════
class B12_Transfer(Scene):
    BASE = 10.0
    def construct(self):
        st = _Table(self, "Row One: White-Box", rows=1)
        d = _dot(LABX(71) + 1.0, RY(0)); self.add(d)
        self.play(Transform(st.t, _title("Row Two: Transfer")), FadeIn(_rowlabels(1)), run_time=0.8)
        cb = _bar(CLEAN, CY(1), DIM)
        self.play(GrowFromEdge(cb, LEFT), FadeIn(_val(CLEAN, CY(1), DIM)), run_time=1.0)
        rb = _bar(ROWS[1][2], RY(1))
        self.play(GrowFromEdge(rb, LEFT), run_time=1.1)
        self.play(FadeIn(_val(58, RY(1))), d.animate.move_to([LABX(58) + 1.0, RY(1), 0]), run_time=0.6)
        self.play(FadeIn(_cap("the attacker never saw the model")), run_time=0.5)
        _finish(self)


# ═══════════ B13 — NAIVE: fold the rows into one word ═══════════
class B13_OneWord(Scene):
    BASE = 11.0
    def construct(self):
        st = _Table(self, "Row Two: Transfer", rows=2)
        d = _dot(LABX(58) + 1.0, RY(1)); self.add(d)
        self.play(Transform(st.t, _title("The Vendor's Move")), FadeOut(d), run_time=0.7)
        self.wait(0.4)
        word = _t("robust", 40, INK, bold=True).move_to([0.8, -1.0, 0])
        self.play(ReplacementTransform(VGroup(st.rob, st.rval), word), run_time=2.0)
        self.wait(0.5)
        self.play(Create(_x(2.05, -1.0)), run_time=0.5)
        self.play(FadeIn(_t("which number?", 32, DIM).move_to([3.9, -1.0, 0])), run_time=0.5)
        self.play(FadeIn(_cap("the fluency trap in a lab coat")), run_time=0.5)
        _finish(self)


# ═══════════ B14 — SHIFT: unfold; each row its own axis ═══════════
class B14_UnfoldRows(Scene):
    BASE = 12.0
    def construct(self):
        st = _Table(self, "The Vendor's Move", rows=2, merged=True)
        xx = _x(2.05, -1.0); wn = _t("which number?", 32, DIM).move_to([3.9, -1.0, 0]); c0 = _cap("the fluency trap in a lab coat")
        self.add(xx, wn, c0)
        self.wait(0.3)
        back = VGroup(_bar(71, RY(0)), _val(71, RY(0)), _bar(58, RY(1)), _val(58, RY(1)))
        self.play(FadeOut(xx), FadeOut(wn), FadeOut(c0), Transform(st.t, _title("Unfold It")), run_time=0.6)
        self.play(ReplacementTransform(st.word, back), run_time=1.8)
        self.play(FadeIn(_t("each row, its own axis", 32, DIM).move_to([3.3, -2.85, 0])), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(_rowlabels(2)), run_time=0.7)
        cb = _bar(CLEAN, CY(2), DIM)
        self.play(GrowFromEdge(cb, LEFT), FadeIn(_val(CLEAN, CY(2), DIM)), run_time=1.0)
        self.play(FadeIn(_qmark(RY(2))), GrowFromCenter(_dot(BX0 + 0.75, RY(2))), run_time=0.5)
        _finish(self)


# ═══════════ B15 — predict ═══════════
class B15_Commit(Scene):
    BASE = 9.0
    def construct(self):
        st = _Table(self, "Unfold It", rows=2, row3=True)
        c0 = _t("each row, its own axis", 32, DIM).move_to([3.3, -2.85, 0]); d = _dot(BX0 + 0.75, RY(2))
        self.add(c0, d)
        self.play(Transform(st.t, _title("Commit")), FadeOut(c0), run_time=0.6)
        ticks = _ticks()
        self.play(Create(ticks), FadeIn(_tick_labels()), run_time=0.9)
        self.play(FadeIn(_t("above 71, between, or below 58?", 36).move_to([0, -2.2, 0])), run_time=0.7)
        self.play(FadeIn(_cap("could rows one and two tell you?")), run_time=0.5)
        _finish(self)


# ═══════════ B16 — TRANSFORM: row three lands; the word meets the form ═══════════
class B16_RowThreeLands(Scene):
    BASE = 12.0
    def construct(self):
        st = _Table(self, "Commit", rows=2, row3=True, ticks=True)
        tl = _tick_labels(); qq = _t("above 71, between, or below 58?", 36).move_to([0, -2.2, 0])
        c0 = _cap("could rows one and two tell you?"); d = _dot(BX0 + 0.75, RY(2))
        self.add(tl, qq, c0, d)
        self.wait(0.3)
        rb = _bar(ROWS[2][2], RY(2))
        self.play(Transform(st.t, _title("Row Three Lands")), FadeOut(qq), FadeOut(c0), FadeOut(tl), run_time=0.6)
        self.play(GrowFromEdge(rb, LEFT), Transform(st.q, _val(87, RY(2))),
                  d.animate.move_to([LABX(87) + 1.0, RY(2), 0]), run_time=1.8)
        self.bring_to_front(st.ticks)
        self.play(FadeIn(_t("past both", 32, DIM).move_to([3.3, -2.85, 0])), run_time=0.5)
        self.wait(0.8)
        word = st.head[ROBUST_GLYPHS].copy().set_color(INK)
        self.add(word)
        self.play(ReplacementTransform(word, _blanks()), run_time=2.2)
        _finish(self)


# ═══════════ B17 — INSTANCE (post-shift): move the budget ═══════════
class B17_MoveTheBudget(Scene):
    BASE = 12.0
    def construct(self):
        st = _Table(self, "Row Three Lands", rows=3, ticks=True, blanks=True)
        c0 = _t("past both", 32, DIM).move_to([3.3, -2.85, 0]); d0 = _dot(LABX(87) + 1.0, RY(2))
        self.add(c0, d0)
        self.play(Transform(st.t, _title("Move The Budget")), FadeOut(c0), FadeOut(d0), FadeOut(st.ticks), run_time=0.6)
        bud = st.labels[0][1]
        self.play(Transform(bud, _t("ε = 0.06", 32, INK).move_to([LX, ROW_Y[0] - 0.22, 0], aligned_edge=LEFT)),
                  GrowFromCenter(_dot(LX + 1.75, ROW_Y[0] - 0.22)), run_time=0.8)
        self.play(Transform(st.rob[0], _bar(0, RY(0))), Transform(st.rval[0], _t("?", 36).move_to([BX0 + 0.3, RY(0), 0])), run_time=1.2)
        self.wait(1.2)
        self.play(Transform(bud, _t("ε = 0.03", 32, DIM).move_to([LX, ROW_Y[0] - 0.22, 0], aligned_edge=LEFT)),
                  Transform(st.rob[0], _bar(71, RY(0))), Transform(st.rval[0], _val(71, RY(0))), run_time=1.4)
        self.play(FadeIn(_cap("a number at a budget")), run_time=0.5)
        _finish(self)


# ═══════════ B18 — ABSTRACTION: name the structure ═══════════
class B18_NameIt(Scene):
    BASE = 12.0
    def construct(self):
        st = _Table(self, "Move The Budget", rows=3, blanks=True)
        c0 = _cap("a number at a budget"); d0 = _dot(LX + 1.75, ROW_Y[0] - 0.22)
        self.add(c0, d0)
        self.play(Transform(st.t, _title("Name It")), FadeOut(c0), FadeOut(d0), run_time=0.6)
        name = _t("a profile, not a number", 36, INK, bold=True).move_to([3.3, -2.85, 0])
        self.play(FadeIn(name), run_time=0.7)
        self.play(Transform(st.head, _t("1 · the profile", 32, INK).move_to([LX, HEAD_Y, 0], aligned_edge=LEFT)), run_time=0.8)
        rail = Line([-6.1, 2.4, 0], [-6.1, -2.1, 0], color=INK, stroke_width=3)
        self.play(Create(rail), run_time=1.0)
        d = _dot(-6.1, HEAD_Y, 0.12)
        self.play(GrowFromCenter(d), run_time=0.4)
        self.play(d.animate.move_to([-6.1, BLANK_Y, 0]), run_time=1.6)
        _finish(self)


# ═══════════ B19 — PAYOFF ═══════════
class B19_Payoff(Scene):
    BASE = 13.0
    def construct(self):
        st = _Table(self, "Name It", rows=3, blanks=True, header="section", rail=True)
        name = _t("a profile, not a number", 36, INK, bold=True).move_to([3.3, -2.85, 0]); d = _dot(-6.1, BLANK_Y, 0.12)
        self.add(name, d)
        self.play(Transform(st.t, _title("Back To The Slide")), FadeOut(name), FadeOut(st.rail),
                  Transform(st.head, _claim(32, INK)), d.animate.move_to([LABX(CLEAN) + 1.0, CY(0), 0]), run_time=1.2)
        self.wait(0.6)
        for i in range(3):
            self.play(d.animate.move_to([LABX(ROWS[i][2]) + 1.0, RY(i), 0]), run_time=0.7)
            self.wait(0.3)
        self.play(d.animate.move_to([-1.5, BLANK_Y - 0.14, 0]), run_time=0.7)
        self.play(Create(_x(-0.55, HEAD_Y, 0.18)), run_time=0.5)
        self.play(FadeIn(_cap("not taught: what defenses cost")), run_time=0.5)
        _finish(self)
