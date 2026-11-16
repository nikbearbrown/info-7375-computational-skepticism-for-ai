"""
Manim scenes for tldr-missing-is-not-one-thing (tldr skill — LEARN section 1, B10–B19).

The one representation: a missingness matrix (rows as thin lines, columns as
stripes, dark where the income value is absent) whose ROWS RE-SORT by a column —
a block of dark cells means the blanks depend on that column. Three constructed
worlds from world.py, each with exactly 9 of 50 income cells blank (18%):
random (MCAR), table A (under-25s skipped — MAR), table B (the nine highest
earners — MNAR). A right-hand income axis shows DIRECTION only (no numbers):
where an average fill lands relative to the (constructed, known) truth.

State factory: `_Matrix` rebuilds a table at any sort order; `sort_to(order)`
glides every row (transform, don't cut). `_Axis` holds the truth tick and the
fill dot. Every relation shown is asserted in world.py at import.

INK text on the cream stage; terracotta is ONE accent per scene — a dot or an X
beside a shape — never text, never a thin horizontal bar, never an outline near
text (GATE T). Gate A: every scene adds a new geometric object before its final
play. Explicit coords inside ±6.2 / ±3.3. Type floor 32 (titles 40). Captions
≤ 34 chars centred at x ≈ 3.2. No slant on multi-word text.
"""
import json as _json, os as _os, sys as _sys
from manim import *

_HERE = _os.path.dirname(_os.path.abspath(__file__))
# run.sh renders from the reel folder, but its Gate A copies ONLY scenes.py into a temp dir —
# so fall back to the reel's own world.py (the constructed table) when it is not beside this file.
_REEL = "/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/tldr-missing-is-not-one-thing"
for _d in (_HERE, _os.getcwd(), _REEL):
    if _os.path.exists(_os.path.join(_d, "world.py")):
        _sys.path.insert(0, _d); break
import world as W
if not _os.path.exists(_os.path.join(_HERE, "beat_sheet.json")) and _os.path.exists(_os.path.join(_REEL, "beat_sheet.json")):
    _HERE = _REEL

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
PRESENT = "#BFB7A5"      # a recorded cell (Gate V: mean ink must sit ≥ 0.30 luminance below the stage)
IMPUTED = "#7E8895"      # a filled-in (imputed) blank — cool grey, apart from the warm recorded cells
YOUNG_C = "#8C846F"      # an age cell of someone under 25
BAR_C = "#ADA590"        # the never-recorded true-income bars
SERIF = "EB Garamond"
config.background_color = STAGE

# ═══════════ facts the scenes draw (asserted) ═══════════
N, K = W.N, W.K
assert N == 50 and K == 9
YOUNG = {i for i in range(N) if W.AGES[i] < W.YOUNG}
assert len(YOUNG) == 12 and set(W.MAR) <= YOUNG
assert W.GAP[("mar", "column")] > 0 > W.GAP[("mnar", "band")]
assert W.is_block("truth", W.MNAR) and not W.is_block("truth", W.MCAR)

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
def _cap(txt, x=3.2, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -3.05, 0])
def _x(x, y, s=0.18, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _spot(x, y, r=0.13): return Dot([x, y, 0], color=TERRA, radius=r)

# ═══════════ the matrix (state factory) ═══════════
M_TOP, ROW_H, SW, PITCH = 1.95, 0.08, 0.70, 1.05         # 50 rows → 4.0 tall (1.95 … −2.05)
HEAD_Y, LABEL_Y = 2.3, -2.45
X_A, X_B = -4.0, -0.6                                     # the two-table stage
HEADS = ("age", "city", "income")
BAR_K = 1.45 / 160.0                                      # true-income bars: the constructed max (160) → 1.45 units

class _Matrix:
    """A missingness matrix of one constructed world, at a given sort order.
    Rows keep their identity; sort_to() glides them (the join between beats is continuous)."""
    def __init__(self, blank, cx, order="file", heads=HEADS, label=None, young=False,
                 top=M_TOP, rh=ROW_H, sw=SW, pitch=PITCH, filled=False):
        self.blank = set(blank); self.cx = cx; self.order = order
        self.top, self.rh, self.sw, self.pitch = top, rh, sw, pitch
        xs = [cx - pitch, cx, cx + pitch]; self.xs = xs
        self.rows = VGroup()
        for i in range(N):
            y = self._y(order, i)
            age_c = YOUNG_C if (young and i in YOUNG) else PRESENT
            inc_c = (IMPUTED if filled else INK) if i in self.blank else PRESENT
            cells = VGroup(*[Rectangle(width=sw, height=rh * 0.72, fill_color=c, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
                             for x, c in zip(xs, (age_c, PRESENT, inc_c))])
            self.rows.add(cells)
        self.heads = VGroup(*[_t(h, 32, DIM).move_to([x, HEAD_Y, 0]) for x, h in zip(xs, heads)]) if heads else VGroup()
        self.label = _t(label, 32).move_to([cx, LABEL_Y, 0]) if label else None
        self.bars = None
    def _y(self, order, i): return self.top - (W.rank_of(order, i) + 0.5) * self.rh
    def mobs(self):
        g = VGroup(self.heads, self.rows)
        if self.label is not None: g.add(self.label)
        if self.bars is not None: g.add(self.bars)
        return g
    def add_to(self, scene): scene.add(self.mobs()); return self
    def inc(self, i): return self.rows[i][2]
    def sort_to(self, order):
        self.order = order
        an = [self.rows[i].animate.set_y(self._y(order, i)) for i in range(N)]
        if self.bars is not None:
            an += [self.bars[i].animate.set_y(self._y(order, i)) for i in range(N)]
        return an
    def fill(self, color=IMPUTED): return [self.inc(i).animate.set_fill(color) for i in sorted(self.blank)]
    def shade_young(self): return [self.rows[i][0].animate.set_fill(YOUNG_C) for i in sorted(YOUNG)]
    def reblank(self, new, color=INK):
        new = set(new); an = []
        for i in range(N):
            if i in self.blank and i not in new: an.append(self.inc(i).animate.set_fill(PRESENT))
            if i in new and i not in self.blank: an.append(self.inc(i).animate.set_fill(color))
            if i in new and i in self.blank: an.append(self.inc(i).animate.set_fill(color))
        self.blank = new; return an
    def make_bars(self, x0, k=BAR_K):
        """the never-recorded column: one bar per row, length ∝ the constructed true income."""
        self.bars = VGroup(*[Rectangle(width=max(W.INCOME[i] * k, 0.04), height=self.rh * 0.72, fill_color=BAR_C, fill_opacity=1,
                                       stroke_width=0).move_to([x0 + W.INCOME[i] * k / 2, self._y(self.order, i), 0]) for i in range(N)])
        return self.bars
    def rank_top(self, n):  # y of the centre of the top-n block
        return self.top - n * self.rh / 2
    def set_label(self, s):
        """cross-fade the label (a letter-morph between two strings reads as garbled text mid-way — GATE T)."""
        new = _t(s, 32).move_to([self.cx, LABEL_Y, 0]); an = FadeTransform(self.label, new); self.label = new; return an

# ═══════════ the income axis: direction only, no numbers ═══════════
AX_X0, AX_X1 = 1.4, 5.6
def AXX(v): return AX_X0 + (v - W.AX_LO) / (W.AX_HI - W.AX_LO) * (AX_X1 - AX_X0)
TRUTH_X = AXX(W.TRUE_MEAN)
def FX(world, how="column"): return AXX(W.FILL[(world, how)])
assert AX_X0 + 0.9 < FX("mnar") < TRUTH_X < FX("mar") < AX_X1 - 0.9

class _Axis:
    def __init__(self, y, name="average income", ends=True):
        self.y = y
        self.line = Line([AX_X0, y, 0], [AX_X1, y, 0], color=INK, stroke_width=3)
        self.name = _t(name, 32, DIM).move_to([AX_X0, y + 0.95, 0], aligned_edge=LEFT) if name else VGroup()
        self.ends = VGroup(_t("lower", 32, DIM).move_to([AX_X0, y - 0.45, 0]), _t("higher", 32, DIM).move_to([AX_X1 - 0.1, y - 0.45, 0])) if ends else VGroup()
        self.tick = Line([TRUTH_X, y - 0.25, 0], [TRUTH_X, y + 0.25, 0], color=INK, stroke_width=5)
        self.tlab = _t("truth", 32).move_to([TRUTH_X, y + 0.55, 0])
        self.dot = Dot([AX_X0, y, 0], color=INK, radius=0.13)
    def base(self): return VGroup(self.line, self.name, self.ends)
    def truth(self): return VGroup(self.tick, self.tlab)
    def dot_at(self, x): self.dot.move_to([x, self.y, 0]); return self.dot


class B10_TwoTables(Scene):
    BASE = 11.0
    def construct(self):
        self.add(_title("Same Count, Same Look"))
        A = _Matrix(W.MAR, X_A, label="table A · 9 blank")
        B = _Matrix(W.MNAR, X_B, label="table B · 9 blank")
        for m in (A, B):                              # the blanks arrive after the rows
            for i in m.blank: m.inc(i).set_fill(PRESENT)
        self.play(FadeIn(A.heads), LaggedStart(*[GrowFromEdge(r, LEFT) for r in A.rows], lag_ratio=0.03), run_time=1.4)
        self.play(FadeIn(B.heads), LaggedStart(*[GrowFromEdge(r, LEFT) for r in B.rows], lag_ratio=0.03), run_time=1.2)
        self.play(*[m.inc(i).animate.set_fill(INK) for m in (A, B) for i in m.blank], FadeIn(A.label), FadeIn(B.label), run_time=0.9)
        self.wait(1.2)
        q1 = _t("fill both with the average:", 32).move_to([3.7, 1.0, 0])
        q2 = _t("which fill is safe?", 40, INK, bold=True).move_to([3.7, 0.3, 0])
        self.play(FadeIn(q1), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(q2), GrowFromCenter(_spot(1.15, 0.3)), run_time=0.6)
        self.play(FadeIn(_cap("constructed: 50 rows, 18% blank")), run_time=0.5)
        _finish(self)


class B11_RandomWipe(Scene):
    BASE = 13.0
    def construct(self):
        self.add(_title("A Random Wipe"))
        M = _Matrix(W.MCAR, X_A, label="random · 9 blank").add_to(self)
        ax = _Axis(-0.9); self.add(ax.base())
        self.play(FadeIn(_t("nine cells, wiped at random", 32).move_to([3.5, 1.7, 0])), run_time=0.6)
        self.wait(0.6)
        dot = ax.dot_at(AX_X0)
        self.play(*M.fill(), GrowFromCenter(dot), run_time=0.8)
        self.play(dot.animate.move_to([FX("mcar"), ax.y, 0]), run_time=1.0)
        self.wait(0.8)
        self.play(Create(ax.tick), FadeIn(ax.tlab), run_time=0.7)
        self.wait(1.0)
        self.play(*M.reblank(W.MCAR2, INK), run_time=0.9)
        self.play(*M.fill(), dot.animate.move_to([FX("mcar2"), ax.y, 0]), run_time=1.0)
        on = _t("on the truth, twice", 36).move_to([3.9, 0.9, 0])
        self.play(FadeIn(on), GrowFromCenter(_spot(1.7, 0.9)), run_time=0.6)
        self.play(FadeIn(_cap("random loss: fewer rows, no tilt")), run_time=0.5)
        _finish(self)


class B12_TableA(Scene):
    BASE = 12.0
    def construct(self):
        self.add(_title("Table A"))
        M = _Matrix(W.MAR, X_A, label="table A · 9 blank").add_to(self)
        ax = _Axis(-0.9); self.add(ax.base(), ax.truth())
        dot = ax.dot_at(AX_X0)
        self.play(*M.fill(), GrowFromCenter(dot), run_time=0.8)
        self.play(dot.animate.move_to([FX("mar"), ax.y, 0]), run_time=1.0)
        self.play(FadeIn(_t("too high", 36).move_to([3.5, 0.9, 0])), run_time=0.7)
        self.wait(1.4)
        self.play(*M.shade_young(), GrowFromCenter(_spot(X_A - PITCH - 0.62, HEAD_Y)), run_time=1.0)
        self.play(FadeIn(_t("every blank: under 25", 36).move_to([3.5, 1.7, 0])), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(_cap("here, the young earn less")), run_time=0.5)
        _finish(self)


class B13_AgeGroupFill(Scene):
    BASE = 12.0
    def construct(self):
        self.add(_title("Fill By Age Group"))
        A = _Matrix(W.MAR, X_A, label="table A", young=True, filled=True).add_to(self)
        B = _Matrix(W.MNAR, X_B, label="table B", young=True).add_to(self)
        axA = _Axis(1.0, name="table A", ends=False); axB = _Axis(-1.2, name="table B")
        dA = axA.dot_at(FX("mar"))
        self.add(axA.base(), axA.truth(), dA)
        self.wait(0.4)
        self.play(dA.animate.move_to([FX("mar", "band"), axA.y, 0]), run_time=1.2)
        self.wait(1.2)
        self.play(FadeIn(axB.base()), Create(axB.tick), FadeIn(axB.tlab), run_time=0.7)
        dB = axB.dot_at(AX_X0)
        self.play(*B.fill(), GrowFromCenter(dB), run_time=0.7)
        self.play(dB.animate.move_to([FX("mnar"), axB.y, 0]), run_time=0.9)
        self.play(dB.animate.move_to([FX("mnar", "band"), axB.y, 0]), run_time=1.0)
        self.play(Create(_x(FX("mnar", "band"), axB.y - 0.62)), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(_cap("nothing in table B says why")), run_time=0.5)
        _finish(self)


class B14_SortTheRows(Scene):
    BASE = 12.5
    def construct(self):
        self.add(_title("Sort The Rows"))
        A = _Matrix(W.MAR, X_A, label="table A, file order", young=True).add_to(self)
        B = _Matrix(W.MNAR, X_B, label="table B, file order", young=True).add_to(self)
        self.wait(1.4)
        self.play(*A.sort_to("age"), A.set_label("table A, by age"), run_time=1.8)
        top12 = M_TOP - 12 * ROW_H
        br = Line([X_A - PITCH - SW / 2 - 0.14, M_TOP - 0.02, 0], [X_A - PITCH - SW / 2 - 0.14, top12 + 0.02, 0], color=INK, stroke_width=4)
        self.play(Create(br), FadeIn(_t("A: one block, under 25", 36).move_to([3.9, 1.3, 0])), run_time=0.7)
        self.wait(0.8)
        self.play(*B.sort_to("age"), B.set_label("table B, by age"), run_time=1.6)
        self.play(*B.sort_to("city"), B.set_label("table B, by city"), run_time=1.6)
        self.play(FadeIn(_t("B: scattered, twice", 36).move_to([3.9, 0.6, 0])), GrowFromCenter(_spot(1.7, 0.6)), run_time=0.6)
        self.play(FadeIn(_cap("a block: depends on what you see")), run_time=0.5)
        _finish(self)


# the hidden-column stage (B15–B16): table B left, the random table right, each with its unrecorded bars
XB2, XR2 = -4.7, 0.75
BARS_B, BARS_R = XB2 + PITCH + SW / 2 + 0.2, XR2 + PITCH + SW / 2 + 0.2
def _hidden_stage(scene, order_b="city", order_r="city", bars=True):
    B = _Matrix(W.MNAR, XB2, order=order_b, label="table B", young=True)
    R = _Matrix(W.MCAR, XR2, order=order_r, label="random")
    if bars:
        B.make_bars(BARS_B); R.make_bars(BARS_R)
    B.add_to(scene); R.add_to(scene)
    hb = _t("true income", 32, DIM).move_to([BARS_B + 0.95, LABEL_Y, 0])
    hr = _t("true income", 32, DIM).move_to([BARS_R + 0.95, LABEL_Y, 0])
    return B, R, VGroup(hb, hr)


class B15_Predict(Scene):
    BASE = 10.0
    def construct(self):
        self.add(_title("The Column Nobody Wrote Down"))
        B, R, heads = _hidden_stage(self, bars=False)
        self.wait(1.2)
        B.make_bars(BARS_B); R.make_bars(BARS_R)
        self.play(FadeIn(heads), LaggedStart(*[GrowFromEdge(b, LEFT) for b in B.bars], lag_ratio=0.02),
                  LaggedStart(*[GrowFromEdge(b, LEFT) for b in R.bars], lag_ratio=0.02), run_time=2.2)
        self.wait(1.0)
        self.play(FadeIn(_t("commit", 40, INK, bold=True).move_to([5.2, 0.4, 0])), GrowFromCenter(_spot(5.2, -0.25)), run_time=0.6)
        self.play(FadeIn(_cap("true income: never recorded")), run_time=0.5)
        _finish(self)


class B16_TheHiddenSort(Scene):
    BASE = 8.5
    def construct(self):
        self.add(_title("The Column Nobody Wrote Down"))
        B, R, heads = _hidden_stage(self)
        self.add(heads)
        self.wait(0.3)
        self.play(*B.sort_to("truth"), *R.sort_to("truth"), run_time=2.6)
        top9 = M_TOP - K * ROW_H
        self.play(GrowFromCenter(_spot(XB2 + PITCH + SW / 2 + 0.1, (M_TOP + top9) / 2, 0.08)),
                  FadeIn(_t("B: the top nine", 32).move_to([4.6, -1.2, 0])), run_time=0.7)
        self.play(FadeIn(_t("random: scattered", 32).move_to([4.6, -1.85, 0])), run_time=0.6)
        self.play(FadeIn(_cap("from inside, they looked the same")), run_time=0.5)
        _finish(self)


class B17_ThreeNames(Scene):
    BASE = 12.5
    def construct(self):
        self.add(_title("Three Kinds Of Missing"))
        s = 0.62; top = 1.95; rh = ROW_H * s; sw = SW * s; p = PITCH * s
        xs = (-4.4, -0.2, 3.9)
        R = _Matrix(W.MCAR, xs[0], order="file", heads=None, top=top, rh=rh, sw=sw, pitch=p)
        A = _Matrix(W.MAR, xs[1], order="age", heads=None, young=True, top=top, rh=rh, sw=sw, pitch=p)
        B = _Matrix(W.MNAR, xs[2], order="truth", heads=None, young=True, top=top, rh=rh, sw=sw, pitch=p)
        B.make_bars(xs[2] + p + 0.35, k=BAR_K * 0.62)
        self.play(FadeIn(R.mobs()), FadeIn(A.mobs()), FadeIn(B.mobs()), run_time=0.9)
        names = [("MCAR", "depends on nothing", None), ("MAR", "on what you can see", None), ("MNAR", "on the missing value", "itself")]
        for x, (nm, m1, m2) in zip(xs, names):
            g = VGroup(_t(nm, 40, INK, bold=True).move_to([x, -1.1, 0]), _t(m1, 32).move_to([x, -1.75, 0]))
            if m2: g.add(_t(m2, 32).move_to([x, -2.2, 0]))
            self.play(FadeIn(g), run_time=0.7)
            self.wait(1.3)
        self.play(B.bars.animate.set_fill(GHOST), GrowFromCenter(_spot(xs[2] + 1.2, -1.1)), run_time=0.8)
        self.play(FadeIn(_cap("after Rubin (1976)")), run_time=0.5)
        _finish(self)


class B18_WhoWouldNotReport(Scene):
    BASE = 12.0
    def construct(self):
        self.add(_title("A Study With Dropouts"))
        M = _Matrix(W.MNAR, X_A, heads=("start", "mid", "final"), label="sorted by: file").add_to(self)
        self.play(FadeIn(_t("final: blank for the nine", 32).move_to([3.6, 1.7, 0])),
                  FadeIn(_t("who left before the end", 32).move_to([3.6, 1.2, 0])), run_time=0.8)
        self.wait(0.4)
        self.play(*M.sort_to("city"), M.set_label("sorted by: start"), run_time=1.2)
        self.wait(0.8)
        bx0 = X_A + PITCH + SW / 2 + 0.25
        M.make_bars(bx0)
        self.play(FadeIn(_t("got sicker", 32, DIM).move_to([bx0 + 0.95, HEAD_Y, 0])),
                  LaggedStart(*[GrowFromEdge(b, LEFT) for b in M.bars], lag_ratio=0.02), run_time=1.0)
        self.play(*M.sort_to("truth"), M.set_label("sorted by: got sicker"), run_time=1.4)
        self.wait(1.4)                                  # settled before the clip midpoint (GATE T samples it)
        q = VGroup(_t("who would not", 36, INK, bold=True).move_to([3.6, -0.1, 0]),
                   _t("report this, and why?", 36, INK, bold=True).move_to([3.6, -0.7, 0]))
        self.play(FadeIn(q), GrowFromCenter(_spot(1.15, -0.1)), run_time=0.7)
        self.play(FadeIn(_cap("constructed: same shape, new table")), run_time=0.5)
        _finish(self)


class B19_Payoff(Scene):
    BASE = 14.0
    def construct(self):
        self.add(_title("Which Fill Is Safe?"))
        A = _Matrix(W.MAR, X_A, label="table A · 9 blank").add_to(self)
        B = _Matrix(W.MNAR, X_B, label="table B · 9 blank").add_to(self)
        self.wait(1.0)
        self.play(*A.shade_young(), *B.shade_young(), run_time=0.6)
        self.play(*A.sort_to("age"), *B.sort_to("age"), A.set_label("table A, by age"), B.set_label("table B, by age"), run_time=1.8)
        axA = _Axis(1.0, name="A · MAR", ends=False); axB = _Axis(-1.2, name="B · MNAR")
        dA = axA.dot_at(AX_X0); dB = axB.dot_at(AX_X0)
        self.play(FadeIn(axA.base()), FadeIn(axA.truth()), *A.fill(), GrowFromCenter(dA), run_time=0.8)
        self.play(dA.animate.move_to([FX("mar", "band"), axA.y, 0]), run_time=1.0)
        self.wait(0.6)
        self.play(FadeIn(axB.base()), FadeIn(axB.truth()), *B.fill(), GrowFromCenter(dB), run_time=0.8)
        self.play(dB.animate.move_to([FX("mnar", "band"), axB.y, 0]), run_time=1.0)
        self.play(Create(_x(FX("mnar", "band"), axB.y - 0.62)), run_time=0.5)
        self.wait(1.2)
        self.play(FadeIn(_cap("not taught here: choosing a fill")), run_time=0.5)
        _finish(self)
