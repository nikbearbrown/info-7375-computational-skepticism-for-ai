"""
Manim scenes for tldr-the-99-percent-test (tldr skill — LEARN section 1, B10–B19).

Key case (chapter 2, INFO 7375 Computational Skepticism): a disease 1 in 10,000
people have, a test that is "99% accurate", one positive result. Persistent objects
across the section: the PATIENT (an ink square), the CHANCE RAIL (0% · 50% · 100%)
with its terracotta KNOB, the two FACTS; then the 10×10 block (100 sick / 100
healthy), the 100×100 GRID of 10,000 people, the PEN, and the PILE of 101.

Every number is recomputed at import from the chapter's inputs (FACTCHECK.md).
INK text on the cream stage; terracotta is the knob, a dot, an X beside a word —
never text, never a thin horizontal line, never an outline around text (GATE T).
Gate A/B: a NEW geometric object appears before each scene's final play; no line
crosses a label; explicit coords inside ±6.2 / ±3.3. Type floor 32 (titles 40).
Captions ≤ 34 chars, centred at x ≈ 3.2. No slant=ITALIC on multi-word text.
"""
import json as _json, os as _os, random as _random
from fractions import Fraction as _F
from manim import *
import numpy as np

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
PALE = "#A39E8E"                                            # an unlit person
SERIF = "EB Garamond"
config.background_color = STAGE
SLUG = "tldr-the-99-percent-test"

# ═══════════ the chapter's numbers, re-asserted ═══════════
PRIOR = _F(1, 10_000); SENS = _F(99, 100); FPR = _F(1, 100)
FALSE_POS = round(FPR * 9_999); assert FALSE_POS == 100                  # 0.01 × 9,999 = 99.99 ≈ 100
COUNT = _F(1, 1 + FALSE_POS); assert abs(float(COUNT) - 0.0099) < 1e-4   # 1/101
POST = PRIOR * SENS / (PRIOR * SENS + (1 - PRIOR) * FPR)
assert PRIOR * SENS == _F(99, 1_000_000) and PRIOR * SENS + (1 - PRIOR) * FPR == _F(10_098, 1_000_000)
assert abs(float(POST) - 0.0098039) < 1e-6 and 98 < float(POST / PRIOR) < 98.1

# ═══════════ pacing ═══════════
_HERE = _os.path.dirname(_os.path.abspath(__file__))
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
def _t(s, size=36, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _m(tex, size=48, color=INK): return MathTex(tex, font_size=size, color=color)
def _cap(txt, x=3.2, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -3.05, 0])
def _x(x, y, s=0.22, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _sq(x, y, side, color=INK):
    return Square(side_length=side, fill_color=color, fill_opacity=1, stroke_width=0).move_to([x, y, 0])

# ═══════════ stage geometry ═══════════
PAT = (-3.5, 0.4)                                            # the patient
RAIL_Y = -1.95; RAIL_X0, RAIL_X1 = 0.8, 5.8
def RX(v): return RAIL_X0 + float(v) * (RAIL_X1 - RAIL_X0)
R1, R2, R3 = 0.8, 0.2, -0.4                                  # right-column commentary rows

def _facts():
    return (_t("disease: 1 in 10,000", 36).move_to([3.3, 2.25, 0]), _t("test: 99% accurate", 36).move_to([3.3, 1.65, 0]))

def _rail():
    line = Line([RAIL_X0, RAIL_Y, 0], [RAIL_X1, RAIL_Y, 0], color=INK, stroke_width=3)
    ticks = VGroup(*[Line([RX(v), RAIL_Y - 0.1, 0], [RX(v), RAIL_Y + 0.1, 0], color=INK, stroke_width=2) for v in (0, 0.5, 1)])
    labels = VGroup(_t("0%", 32, DIM).move_to([RX(0), RAIL_Y - 0.42, 0]), _t("50%", 32, DIM).move_to([RX(0.5), RAIL_Y - 0.42, 0]),
                    _t("100%", 32, DIM).move_to([RX(1), RAIL_Y - 0.42, 0]))
    name = _t("chance of disease", 32, DIM).move_to([RAIL_X0, RAIL_Y + 0.5, 0], aligned_edge=LEFT)
    return VGroup(line, ticks, labels, name)
def _readout(s): return _t(s, 40).move_to([RAIL_X1, RAIL_Y + 0.5, 0], aligned_edge=RIGHT)
def _knob(v): return Dot([RX(v), RAIL_Y, 0], color=TERRA, radius=0.15)

# the 10×10 block (B11–B12)
BP, BS = 0.42, 0.32
def _bxy(r, c): return (PAT[0] + (c - 4.5) * BP, -0.1 + (4.5 - r) * BP)
MISSED = (6, 7)                                              # the one sick person the test misses (B11)
FALSEP = (3, 2)                                              # the one healthy person it flags (B12)
def _block(lit=()):
    return VGroup(*[_sq(*_bxy(r, c), BS, INK if (r, c) in lit else PALE) for r in range(10) for c in range(10)])
ALL = {(r, c) for r in range(10) for c in range(10)}

# the 100×100 grid of 10,000 (B14–B16)
GP, GS = 0.05, 0.038
GRID_C = (-3.5, -0.1)
def _gxy(r, c): return (GRID_C[0] + (c - 49.5) * GP, GRID_C[1] + (49.5 - r) * GP)
SICK = (37, 62)
_rng = _random.Random(SLUG)
_pool = [i for i in range(10_000) if i != SICK[0] * 100 + SICK[1]]
FP_CELLS = [divmod(i, 100) for i in sorted(_rng.sample(_pool, FALSE_POS))]
assert len(FP_CELLS) == 100 and SICK not in FP_CELLS

def _cells_vm(cells, side, color):
    """Many squares as ONE VMobject (one Cairo path, many subpaths) — 10,000 Mobjects would crawl."""
    vm = VMobject(fill_color=color, fill_opacity=1, stroke_width=0)
    h = side / 2; pts = []
    for (x, y) in cells:
        c = [np.array([x - h, y - h, 0.0]), np.array([x + h, y - h, 0.0]), np.array([x + h, y + h, 0.0]), np.array([x - h, y + h, 0.0])]
        for i in range(4):
            a, b = c[i], c[(i + 1) % 4]
            pts += [a, a + (b - a) / 3, a + 2 * (b - a) / 3, b]
    vm.set_points(np.array(pts))
    return vm
def _grid_bands():
    """ten bands of ten rows each, so the crowd can build band by band."""
    return VGroup(*[_cells_vm([_gxy(r, c) for r in range(b * 10, b * 10 + 10) for c in range(100)], GS, PALE) for b in range(10)])
def _sick_dot(x=None, y=None):
    if x is None: x, y = _gxy(*SICK)
    return Dot([x, y, 0], color=TERRA, radius=0.09)

# the pen and the pile (B15–B17)
PEN_C = (2.1, 0.1)
SP = 0.2; SS = 0.16
def _slot(k): return (PEN_C[0] + (k % 11 - 5) * SP, PEN_C[1] + (4.5 - k // 11) * SP)
def _pen(dx=0.0, dy=0.0):
    return DashedVMobject(Rectangle(width=2.5, height=2.3, stroke_color=DIM, stroke_width=3).move_to([PEN_C[0] + dx, PEN_C[1] + dy, 0]), num_dashes=40)
def _pile(dx=0.0, dy=0.0):
    return VGroup(*[_sq(_slot(k)[0] + dx, _slot(k)[1] + dy, SS) for k in range(101)])


class _Stage:
    """The resting state: title, facts, and the chance rail (knob at v, or '?' with no knob)."""
    def __init__(self, scene, title, facts=True, rail=True, v=None, read="?"):
        self.t = _title(title); scene.add(self.t)
        self.f1, self.f2 = _facts()
        if facts: scene.add(self.f1, self.f2)
        self.rail = _rail(); self.read = _readout(read); self.knob = _knob(v if v is not None else 0)
        if rail:
            scene.add(self.rail, self.read)
            if v is not None: scene.add(self.knob)


class B10_OnePositive(Scene):
    BASE = 8.5
    def construct(self):
        st = _Stage(self, "One Positive Result", facts=False, rail=False)
        self.wait(0.4)
        patient = _sq(*PAT, 0.6)
        self.play(GrowFromCenter(patient), run_time=0.6)
        self.play(FadeIn(st.f1), run_time=0.5)
        self.play(FadeIn(st.f2), run_time=0.5)
        tag = _t("positive", 36).move_to([PAT[0], -0.45, 0])
        self.play(FadeIn(tag), GrowFromCenter(Dot([PAT[0] - 0.95, -0.45, 0], color=TERRA, radius=0.12)), run_time=0.5)
        q1 = _t("how likely is it", 36).move_to([3.3, 0.7, 0]); q2 = _t("this patient is sick?", 36).move_to([3.3, 0.15, 0])
        self.play(FadeIn(q1), FadeIn(q2), run_time=0.6)
        self.play(Create(st.rail[0]), FadeIn(st.rail[1]), FadeIn(st.rail[2]), FadeIn(st.rail[3]), run_time=0.9)
        self.play(FadeIn(st.read), run_time=0.4)
        self.play(FadeIn(_cap("the answer goes on the rail")), run_time=0.5)
        _finish(self)


class B11_TheSick(Scene):
    BASE = 9.0
    def construct(self):
        st = _Stage(self, "What 99% Promises")
        patient = _sq(*PAT, 0.6); self.add(patient)
        self.wait(0.3)
        block = _block()
        self.play(ReplacementTransform(patient, block), run_time=1.0)
        self.play(FadeIn(_t("100 sick people", 36).move_to([PAT[0], 2.3, 0])), run_time=0.5)
        scan = Line([-5.65, 2.0, 0], [-5.65, -2.2, 0], color=DIM, stroke_width=4)
        self.play(Create(scan), run_time=0.4)
        order = sorted([(r, c) for (r, c) in ALL if (r, c) != MISSED], key=lambda rc: (rc[1], rc[0]))
        fills = [block[r * 10 + c].animate.set_fill(INK) for (r, c) in order]
        self.play(scan.animate.move_to([-1.35, -0.1, 0]), LaggedStart(*fills, lag_ratio=0.02), run_time=2.4)
        self.play(FadeOut(scan), GrowFromCenter(Dot([*_bxy(*MISSED), 0], color=TERRA, radius=0.1)), run_time=0.5)
        self.play(FadeIn(_t("sick → positive: 99 of 100", 34).move_to([3.3, R1, 0])), run_time=0.5)
        self.play(FadeIn(_t("missed: 1", 34).move_to([3.3, R2, 0])), run_time=0.4)
        self.play(FadeIn(_cap("the rate printed on the box")), run_time=0.5)
        _finish(self)


class B12_TheHealthy(Scene):
    BASE = 10.0
    def construct(self):
        st = _Stage(self, "What 99% Promises, Part Two")
        block = _block(lit=ALL - {MISSED}); self.add(block)
        lab = _t("100 sick people", 36).move_to([PAT[0], 2.3, 0]); md = Dot([*_bxy(*MISSED), 0], color=TERRA, radius=0.1)
        r1 = _t("sick → positive: 99 of 100", 34).move_to([3.3, R1, 0]); r2 = _t("missed: 1", 34).move_to([3.3, R2, 0])
        self.add(lab, md, r1, r2)
        self.wait(0.3)
        self.play(*[sq.animate.set_fill(PALE) for sq in block], FadeOut(md), FadeOut(r1), FadeOut(r2),
                  Transform(lab, _t("100 healthy people", 36).move_to([PAT[0], 2.3, 0])), run_time=1.0)
        scan = Line([-5.65, 2.0, 0], [-5.65, -2.2, 0], color=DIM, stroke_width=4)
        self.play(Create(scan), run_time=0.4)
        fx, fy = _bxy(*FALSEP)
        self.play(scan.animate.move_to([fx, -0.1, 0]), run_time=0.9)
        self.play(block[FALSEP[0] * 10 + FALSEP[1]].animate.set_fill(INK), run_time=0.4)
        self.play(scan.animate.move_to([-1.35, -0.1, 0]), run_time=1.3)
        self.play(FadeOut(scan), GrowFromCenter(Dot([fx, fy, 0], color=TERRA, radius=0.1)), run_time=0.5)
        self.play(FadeIn(_t("healthy → positive: 1 of 100", 34).move_to([3.3, R1, 0])), run_time=0.5)
        self.play(FadeIn(_t("a false positive", 34).move_to([3.3, R2, 0])), run_time=0.4)
        self.play(FadeIn(_cap("one number, two jobs — simplified")), run_time=0.5)
        _finish(self)


class B13_TheObviousAnswer(Scene):
    BASE = 11.0
    def construct(self):
        st = _Stage(self, "The Obvious Answer")
        block = _block(lit={FALSEP}); lab = _t("100 healthy people", 36).move_to([PAT[0], 2.3, 0])
        fd = Dot([*_bxy(*FALSEP), 0], color=TERRA, radius=0.1)
        r1 = _t("healthy → positive: 1 of 100", 34).move_to([3.3, R1, 0]); r2 = _t("a false positive", 34).move_to([3.3, R2, 0])
        self.add(block, lab, fd, r1, r2)
        self.wait(0.3)
        self.play(FadeOut(block), FadeOut(lab), FadeOut(fd), FadeOut(r1), FadeOut(r2), run_time=0.6)
        knob = _knob(0)
        self.play(GrowFromCenter(knob), run_time=0.4)
        self.play(knob.animate.move_to([RX(0.99), RAIL_Y, 0]), Transform(st.read, _readout("≈ 99%")),
                  FadeIn(_t("the obvious answer: 99%", 34).move_to([3.3, R1, 0])), run_time=1.2)
        band = Rectangle(width=RX(1.0) - RX(0.9), height=0.36, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([(RX(0.9) + RX(1.0)) / 2, RAIL_Y, 0])
        band.set_z_index(-1)
        self.play(FadeIn(band), FadeIn(_t("most answers: above 90%", 34).move_to([3.3, R2, 0])), run_time=0.6)
        self.play(FadeIn(_t("1978 study: most said about 95%", 32).move_to([3.3, R3, 0])), run_time=0.6)
        row1 = _m(r"P(+ \mid \text{sick}) = 0.99", 52).move_to([-3.4, 1.5, 0])
        self.play(FadeIn(_t("what 99% measured", 32, DIM).move_to([-3.4, 2.25, 0])), Write(row1), run_time=0.9)
        ghost = row1.copy()
        self.play(ghost.animate.move_to([-3.4, -0.9, 0]), run_time=0.7)
        row2 = _m(r"P(\text{sick} \mid +) = \;?", 52).move_to([-3.4, -0.9, 0])
        self.play(Transform(ghost, row2), FadeIn(_t("what we were asked", 32, DIM).move_to([-3.4, -0.15, 0])), run_time=0.9)
        self.play(Create(_x(-3.4, 0.55)), run_time=0.4)
        self.play(FadeIn(_cap("same words, the bar flipped")), run_time=0.5)
        _finish(self)


class B14_TenThousand(Scene):
    BASE = 8.5
    def construct(self):
        st = _Stage(self, "Ten Thousand People", v=0.99, read="≈ 99%")
        self.wait(0.3)
        self.play(FadeOut(st.knob), Transform(st.read, _readout("?")), run_time=0.5)
        bands = _grid_bands()
        self.play(LaggedStart(*[FadeIn(b) for b in bands], lag_ratio=0.25), run_time=2.4)
        self.play(FadeIn(_t("10,000 people", 36).move_to([3.3, R1, 0])), run_time=0.5)
        self.play(GrowFromCenter(_sick_dot()), FadeIn(_t("1 sick", 36).move_to([3.3, R2, 0])), run_time=0.6)
        self.play(FadeIn(_t("9,999 healthy", 36).move_to([3.3, R3, 0])), run_time=0.5)
        self.play(FadeIn(_cap("one square per person")), run_time=0.5)
        _finish(self)


class B15_Commit(Scene):
    BASE = 7.0
    def construct(self):
        st = _Stage(self, "Commit")
        self.add(_grid_bands(), _sick_dot())
        rr = VGroup(_t("10,000 people", 36).move_to([3.3, R1, 0]), _t("1 sick", 36).move_to([3.3, R2, 0]), _t("9,999 healthy", 36).move_to([3.3, R3, 0]))
        self.add(rr)
        self.wait(0.3)
        self.play(FadeOut(rr), FadeOut(st.f1), FadeOut(st.f2), run_time=0.5)
        self.play(Create(_pen()), FadeIn(_t("positives", 32, DIM).move_to([PEN_C[0], 1.55, 0])), run_time=0.9)
        self.play(FadeIn(_t("?", 72).move_to([PEN_C[0], PEN_C[1], 0])), run_time=0.4)
        self.play(FadeIn(_t("what share", 32).move_to([4.85, 0.3, 0])), FadeIn(_t("is the sick one?", 32).move_to([4.85, -0.3, 0])), run_time=0.6)
        self.play(FadeIn(_cap("pick a number. lock it in.")), run_time=0.5)
        _finish(self)


class B16_ThePile(Scene):
    BASE = 10.5
    def construct(self):
        st = _Stage(self, "Run It", facts=False)
        self.add(_grid_bands())
        sd = _sick_dot(); self.add(sd)
        pen = _pen(); plab = _t("positives", 32, DIM).move_to([PEN_C[0], 1.55, 0]); qm = _t("?", 72).move_to([PEN_C[0], PEN_C[1], 0])
        a1 = _t("what share", 32).move_to([4.85, 0.3, 0]); a2 = _t("is the sick one?", 32).move_to([4.85, -0.3, 0])
        self.add(pen, plab, qm, a1, a2)
        self.wait(0.3)
        sick = _sq(*_gxy(*SICK), GS); sick.set_z_index(-0.5)
        self.play(FadeIn(sick), sd.animate.scale(1.3), run_time=0.5)
        fps = [_sq(*_gxy(r, c), GS) for (r, c) in FP_CELLS]
        self.play(LaggedStart(*[FadeIn(s) for s in fps], lag_ratio=0.02), run_time=1.6)
        self.play(FadeOut(qm), run_time=0.3)
        moves = [Transform(sick, _sq(*_slot(0), SS)), sd.animate.scale(1 / 1.3).move_to([_slot(0)[0], _slot(0)[1], 0])]
        moves += [Transform(s, _sq(*_slot(k + 1), SS)) for k, s in enumerate(fps)]
        self.play(LaggedStart(*moves, lag_ratio=0.01), run_time=2.4)
        self.play(Transform(a1, _t("1 of 101", 44, INK, bold=True).move_to([4.85, 0.35, 0])), FadeOut(a2), run_time=0.6)
        knob = _knob(0.5)
        self.play(GrowFromCenter(knob), run_time=0.4)
        self.play(knob.animate.move_to([RX(COUNT), RAIL_Y, 0]), Transform(st.read, _readout("≈ 1%")), run_time=1.4)
        self.play(FadeIn(_cap("the healthy crowd fills the pile")), run_time=0.5)
        _finish(self)


# Bayes, staged: lhs, a bar, the numerator, the denominator — each lands on its clause
EQ_Y = 1.6
def _bayes_parts():
    lhs = _m(r"P(D \mid +) \;=", 40).move_to([-3.2, EQ_Y, 0])
    num = _m(r"P(D)\,P(+ \mid D)", 40).move_to([1.3, EQ_Y + 0.45, 0])
    den = _m(r"P(D)\,P(+ \mid D) + P(H)\,P(+ \mid H)", 40).move_to([1.3, EQ_Y - 0.45, 0])
    bar = Line([-1.95, EQ_Y, 0], [4.55, EQ_Y, 0], color=INK, stroke_width=3)
    return lhs, bar, num, den


class B17_NameIt(Scene):
    BASE = 11.0
    def construct(self):
        st = _Stage(self, "A Name For The Pile", facts=False, v=COUNT, read="≈ 1%")
        grid = _grid_bands(); pen = _pen(); plab = _t("positives", 32, DIM).move_to([PEN_C[0], 1.55, 0])
        pile = _pile(); sd = _sick_dot(*_slot(0))
        a1 = _t("1 of 101", 44, INK, bold=True).move_to([4.85, 0.35, 0])
        self.add(grid, pen, plab, pile, sd, a1)
        self.wait(0.3)
        DX, DY = -6.4, -1.2
        self.play(FadeOut(grid), FadeOut(st.rail), FadeOut(st.read), FadeOut(st.knob), FadeOut(plab), FadeOut(a1),
                  VGroup(pen, pile, sd).animate.shift([DX, DY, 0]), run_time=1.0)
        self.play(FadeIn(_t("101 positives", 32, DIM).move_to([PEN_C[0] + DX, 0.35, 0])), run_time=0.4)
        lhs, bar, num, den = _bayes_parts()
        self.play(FadeIn(lhs), Create(bar), run_time=0.7)
        self.play(Write(num), FadeIn(_t("top: the one sick square", 32).move_to([1.9, -0.3, 0])), run_time=0.9)
        self.play(Write(den), FadeIn(_t("bottom: the whole pile of 101", 32).move_to([1.9, -0.85, 0])), run_time=1.1)
        self.play(FadeIn(_t("Bayes' theorem", 40, INK, bold=True).move_to([1.9, 0.35, 0])), run_time=0.6)
        self.play(FadeIn(_t("the base rate sits on top", 32).move_to([2.05, -1.4, 0])),
                  GrowFromCenter(Dot([-0.45, -1.4, 0], color=TERRA, radius=0.12)), run_time=0.6)
        self.play(FadeIn(_cap("D disease · H healthy · + positive")), run_time=0.5)
        _finish(self)


class B18_ReadTheLine(Scene):
    BASE = 13.0
    def construct(self):
        self.add(_title("Read The Line"))
        eq = _m(r"P(D \mid +) = \frac{P(D)\,P(+ \mid D)}{P(+)}", 48).move_to([-3.35, 1.75, 0])
        self.play(FadeIn(eq), run_time=0.7)
        self.play(Create(Line([0.2, 2.3, 0], [0.2, -2.6, 0], color=GHOST, stroke_width=2)), run_time=0.5)
        rows = [(r"P(D)", "prior: 0.0001"), (r"P(+ \mid D)", "hit rate: 0.99"), (r"P(+ \mid H)", "false alarms: 0.01"),
                (r"P(H)", "healthy share: 0.9999"), (r"P(+)", "whole pile: ≈ 0.0101")]
        for i, (sym, mean) in enumerate(rows):
            y = 1.95 - i * 0.62
            self.play(FadeIn(_m(sym, 38).move_to([0.55, y, 0], aligned_edge=LEFT)),
                      FadeIn(_t(mean, 30).move_to([2.55, y, 0], aligned_edge=LEFT), shift=RIGHT * 0.1), run_time=0.55)
        work = _m(r"\frac{0.0001 \times 0.99}{0.0001 \times 0.99 + 0.9999 \times 0.01}", 38).move_to([-3.3, 0.15, 0])
        self.play(Write(work), run_time=1.4)
        res = _m(r"= \frac{0.000099}{0.010098} \approx 0.0098", 42).move_to([-3.45, -1.35, 0])
        self.play(Write(res), run_time=1.1)
        self.play(GrowFromCenter(Dot([-0.55, -1.35, 0], color=TERRA, radius=0.13)), run_time=0.4)
        self.play(FadeIn(_cap("the count said 1 in 101 ≈ 0.0099")), run_time=0.5)
        _finish(self)


class B19_BackToThePatient(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "Back To The Patient", v=COUNT, read="≈ 1%")
        patient = _sq(*PAT, 0.6); tag = _t("positive", 36).move_to([PAT[0], -0.45, 0])
        self.add(patient, tag)
        self.wait(0.4)
        NP = (-4.9, 1.55)
        self.play(patient.animate.scale(0.75).move_to([NP[0], NP[1], 0]), tag.animate.move_to([NP[0], 0.95, 0]), run_time=0.9)
        base = Line([-4.3, -1.0, 0], [-1.3, -1.0, 0], color=INK, stroke_width=3)
        b_before = Rectangle(width=0.8, height=0.02, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-3.4, -0.99, 0])
        after_h = 0.02 * float(POST / PRIOR)                     # 98× taller — the lift, to scale
        b_after = Rectangle(width=0.8, height=after_h, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-2.2, -1.0 + after_h / 2, 0])
        self.play(Create(base), FadeIn(b_before), FadeIn(_t("before", 32, DIM).move_to([-3.4, -1.38, 0])),
                  FadeIn(_t("0.01%", 32).move_to([-3.4, -0.62, 0])), run_time=0.8)
        self.play(GrowFromEdge(b_after, DOWN), FadeIn(_t("after", 32, DIM).move_to([-2.2, -1.38, 0])), run_time=1.2)
        self.play(FadeIn(_t("≈ 1%", 32).move_to([-2.2, -1.0 + after_h + 0.32, 0])), run_time=0.4)
        self.play(FadeIn(_t("the test did real work: ×98", 34).move_to([3.3, R1, 0])), run_time=0.6)
        self.play(FadeIn(_t("and it is still about 1%", 34, INK, bold=True).move_to([3.3, R2, 0])),
                  GrowFromCenter(Dot([0.6, R2, 0], color=TERRA, radius=0.12)), run_time=0.6)
        self.play(FadeIn(_t("hospital scale:", 32, DIM).move_to([-3.5, -2.0, 0])),
                  FadeIn(_t("alerts on 18% of all patients", 32, DIM).move_to([-3.5, -2.45, 0])), run_time=0.7)
        self.play(FadeIn(_cap("not found: the coin-flip base rate")), run_time=0.5)
        _finish(self)
