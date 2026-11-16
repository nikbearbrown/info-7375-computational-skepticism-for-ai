"""
Manim scenes for tldr-features-entering-a-room (tldr skill — LEARN section 1, B10–B19).

The chapter's constructed worked example: one applicant, f̂(x) = 0.72, E[f̂] = 0.55,
three features. Persistent objects: the PREDICTION LINE along the bottom (a dot at
the current score, the ghost SPAN 0.55 → 0.72 that the bars must fill), and the
ROOM LEDGER at the top — one row per arrival order of the three features, with the
bump income makes when it walks in. The six bumps merge into one bar (0.073); with
debt (0.062) and zip (0.035) the three bars fill the span exactly (Efficiency).

State factory: `_Stage(scene, "Bxx")` rebuilds the stage exactly as it stands at the
END of beat Bxx, so the last frame of Bk is the first frame of Bk+1 (transform,
don't cut). Numbers are asserted at import (FACTCHECK.md). INK text on the cream
stage; terracotta is ONE accent per scene — a dot or an X beside a word, never text,
never a line, never a bar, never a ring (GATE T). Explicit coords inside ±6.2 × ±3.3.
Type floor 32 (titles 40). Captions ≤ 34 chars, centred at x ≈ 3.2. Bars ≥ 0.85 and
labels ≥ 1.4 above the prediction line.
"""
import json as _json, os as _os
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the chapter's worked example ═══════════
F_X, E_F = 0.72, 0.55
ROWS = [(("income", "debt", "zip"), "nobody", 0.08),
        (("income", "zip", "debt"), "nobody", 0.08),
        (("debt", "income", "zip"), "debt", 0.07),
        (("zip", "income", "debt"), "zip", 0.09),
        (("debt", "zip", "income"), "debt, zip", 0.06),
        (("zip", "debt", "income"), "debt, zip", 0.06)]
PHI = [("income", 0.073), ("debt", 0.062), ("zip", 0.035)]
assert abs(sum(r[2] for r in ROWS) / 6 - 0.0733333) < 1e-6
assert abs(sum(p for _, p in PHI) - (F_X - E_F)) < 1e-9
assert abs((2 * 0.08 + 0.07 + 0.09 + 2 * 0.06) / 6 - sum(r[2] for r in ROWS) / 6) < 1e-12
assert round(E_F + 0.08, 2) == 0.63 and round(F_X - 0.06, 2) == 0.66

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
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _title(txt, size=40): return _t(txt, size).move_to([0, 3.0, 0])
def _m(tex, size=44, color=INK): return MathTex(tex, font_size=size, color=color)
def _cap(txt, x=3.2, size=32): return _t(txt, size, DIM).move_to([x, -3.0, 0])
def _constructed(): return _t("constructed example", 32, DIM).move_to([-4.35, -3.0, 0])
def _dot(x, y, r=0.13): return Dot([x, y, 0], color=TERRA, radius=r)
def _x(x, y, s=0.2, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))

# ═══════════ the prediction line ═══════════
LY = -2.1                                  # the line
BY = -1.25                                   # bars (0.85 above the line)
LBY = -0.7                                 # bar labels (1.4 above the line)
def PX(v): return -4.6 + (v - 0.50) * 36    # 0.55 → −2.8 · 0.72 → 3.32
U = 36                                      # units per 1.0 of prediction (bars everywhere use it)
BH = 0.24
def _line():
    ln = Line([PX(0.50), LY, 0], [PX(0.75), LY, 0], color=INK, stroke_width=3)
    ticks = VGroup(*[Line([PX(v), LY - 0.1, 0], [PX(v), LY + 0.1, 0], color=INK, stroke_width=3) for v in (E_F, F_X)])
    labs = VGroup(_t("0.55", 32).move_to([PX(E_F), LY - 0.4, 0]), _t("0.72", 32).move_to([PX(F_X), LY - 0.4, 0]),
                  _t("average", 32, DIM).move_to([PX(E_F) - 0.55, LY - 0.4, 0], aligned_edge=RIGHT),
                  _t("her score", 32, DIM).move_to([PX(F_X) + 0.55, LY - 0.4, 0], aligned_edge=LEFT))
    return VGroup(ln, ticks, labs)
def _ptick(v): return VGroup(Line([PX(v), LY - 0.1, 0], [PX(v), LY + 0.1, 0], color=DIM, stroke_width=3),
                             _t(f"{v:.2f}", 32, DIM).move_to([PX(v), LY - 0.4, 0]))
def _pdot(v): return Dot([PX(v), LY, 0], color=INK, radius=0.12)
def _hbar(a, b, y=BY, color=INK, opacity=1.0):
    w = max((b - a) * U, 0.02)
    return Rectangle(width=w, height=BH, fill_color=color, fill_opacity=opacity, stroke_color=STAGE, stroke_width=2).move_to([PX(a) + w / 2, y, 0])
def _span(): return Rectangle(width=(F_X - E_F) * U, height=BH, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([(PX(E_F) + PX(F_X)) / 2, BY, 0])
def _span_label(q=False): return _t("0.17 to split" + ("  ?" if q else ""), 32).move_to([(PX(E_F) + PX(F_X)) / 2, LBY, 0])
def _bump_label(a, b, s, color=INK): return _t(s, 32, color).move_to([(PX(a) + PX(b)) / 2, LBY, 0])
PHI_ALPHA = [1.0, 0.62, 0.34]
def _force_bars():
    g = VGroup(); a = E_F
    for (name, p), al in zip(PHI, PHI_ALPHA):
        g.add(_hbar(a, a + p, opacity=al)); a += p
    return g
def _force_labels():
    g = VGroup(); a = E_F
    for name, p in PHI:
        lab = _t(f"{name} {p:.3f}", 32)
        if name == "zip": lab.move_to([PX(F_X) + 0.2, LBY, 0], aligned_edge=LEFT)      # the short bar: label past its end
        else: lab.move_to([(PX(a) + PX(a + p)) / 2, LBY, 0])
        g.add(lab); a += p
    return g

# ═══════════ the room ledger ═══════════
HY = 2.5
RY = [2.1, 1.64, 1.18, 0.72, 0.26, -0.2]
SEAT = [-5.9, -4.45, -3.0]                  # left edges of the three arrival seats
COLX, VALX, TBX = -1.45, 0.4, 1.6            # already-in column, bump value, bar origin
TBH = 0.2
TOP = 0.13                                 # row words are TOP-aligned (descenders in 'zip', 'nobody' would lift a centred word)
def _header():
    return VGroup(_t("arrival order", 32, DIM).move_to([SEAT[0], HY, 0], aligned_edge=LEFT),
                  _t("already in", 32, DIM).move_to([COLX, HY, 0], aligned_edge=LEFT),
                  _t("income adds", 32, DIM).move_to([VALX, HY, 0], aligned_edge=LEFT))
def _seat(i, k):
    name = ROWS[i][0][k]
    return _t(name, 32, INK, bold=(name == "income")).move_to([SEAT[k], RY[i] + TOP, 0], aligned_edge=UL)
def _seats(i): return VGroup(*[_seat(i, k) for k in range(3)])
def _coal(i): return _t(ROWS[i][1], 32).move_to([COLX, RY[i] + TOP, 0], aligned_edge=UL)
def _val(i): return _t(f"+{ROWS[i][2]:.2f}", 32).move_to([VALX, RY[i] + TOP, 0], aligned_edge=UL)
def _tbar(i):
    w = ROWS[i][2] * U
    return Rectangle(width=w, height=TBH, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([TBX + w / 2, RY[i], 0])
def _row_dot(i): return _dot(TBX + ROWS[i][2] * U + 0.3, RY[i])

# ═══════════ equations ═══════════
WSUM = r"\tfrac{2}{6}(0.08)+\tfrac{1}{6}(0.07)+\tfrac{1}{6}(0.09)+\tfrac{2}{6}(0.06)", r"=0.073"
SHAPLEY = r"\phi_i=\sum_{S\subseteq F\setminus\{i\}}\frac{|S|!\,(|F|-|S|-1)!}{|F|!}\,\bigl[v(S\cup\{i\})-v(S)\bigr]"
EFFIC = r"\phi_{\mathrm{inc}}+\phi_{\mathrm{debt}}+\phi_{\mathrm{zip}}=\hat f(\mathbf{x})-\mathbb{E}[\hat f]"
WORKED_W = r"|S|=1:\ \frac{1!\,1!}{3!}=\frac{1}{6}\qquad |S|=0:\ \frac{0!\,2!}{3!}=\frac{2}{6}"
PLUG = r"0.073+0.062+0.035=0.17=0.72-0.55"
WS_DOT_X = 5.0
def _wsum(): return _m("".join(WSUM), 44).move_to([0, 1.95, 0])
def _shapley(y=0.75, size=44): return _m(SHAPLEY, size).move_to([0, y, 0])
def _effic(y=LBY, size=40): return _m(EFFIC, size).move_to([(PX(E_F) + PX(F_X)) / 2, y, 0])
def _plug(): return _m(PLUG, 40).move_to([(PX(E_F) + PX(F_X)) / 2, LBY, 0])

# tangent layout
TL_X = -5.9; SEP_X = 0.35; GS_X, GM_X = 0.65, 1.95
TROWS = [1.0, 0.45, -0.1, -0.65]
def _sep(y0=1.35, y1=-0.95): return Line([SEP_X, y0, 0], [SEP_X, y1, 0], color=GHOST, stroke_width=3)
T1_SENT = ["left:  income's fair share", "right:  each bump, weighted", "=  exactly that average"]
T1_GLOSS = [(r"\phi_i", "income's fair share"), (r"S", "who's already in"), (r"F", "all three features"), (r"v(S)", "score knowing only S")]
T2_SENT = ["left:  the three shares, added", "right:  her score minus the average", "=  nothing left, nothing twice"]
T2_GLOSS = [(r"\hat f(\mathbf{x})", "her score, 0.72"), (r"\mathbb{E}[\hat f]", "the average, 0.55")]
def _sent(lines): return VGroup(*[_t(s, 32).move_to([TL_X, TROWS[i], 0], aligned_edge=LEFT) for i, s in enumerate(lines)])
def _gloss(rows):
    return VGroup(*[VGroup(_m(sym, 40).move_to([GS_X, TROWS[i], 0], aligned_edge=LEFT),
                           _t(mean, 32).move_to([GM_X + (0.5 if len(sym) > 8 else 0), TROWS[i], 0], aligned_edge=LEFT))
                    for i, (sym, mean) in enumerate(rows)])


TITLES = {"B10": "One Applicant", "B11": "Income Walks In First", "B12": "Drop It And See", "B13": "The Seats In Between",
          "B14": "Every Order", "B15": "Average Them", "B16": "The Shapley Value", "B17": "Read The Line",
          "B18": "Read The Sum", "B19": "Back To Her Score"}
FILLED = {"B11": [0], "B12": [0, 5], "B13": [0, 5, 2, 3], "B14": [0, 1, 2, 3, 4, 5], "B15": [0, 1, 2, 3, 4, 5]}
CAPS = {"B10": "three features, one gap", "B11": "first into an empty room", "B12": "it depends who's already in",
        "B13": "one bump per room", "B14": "exactly, over, or short? commit", "B15": "nothing left over",
        "B16": "the average over every order", "B17": "back to the bars", "B18": "efficiency, drawn",
        "B19": "not taught: what 0.035 means"}
DOTV = {"B10": F_X, "B11": 0.63, "B12": F_X, "B13": F_X, "B14": E_F, "B15": F_X, "B16": F_X, "B18": F_X, "B19": F_X}


class _Stage:
    """The stage exactly as it stands at the END of beat `b` (without that beat's
    terracotta accent, which each scene adds and the next removes)."""
    def __init__(self, scene, b):
        n = int(b[1:])
        self.t = _title(TITLES[b]); self.cons = _constructed(); self.cap = _cap(CAPS[b])
        scene.add(self.t, self.cons, self.cap)
        self.line = self.pdot = None
        if b != "B17":
            self.line = _line(); self.span = _span(); self.pdot = _pdot(DOTV[b])
            scene.add(self.span, self.line, self.pdot)
        if b == "B10":
            self.names = _names(); self.q = _question(); self.slab = _span_label(); scene.add(self.names, self.q, self.slab)
        if b == "B14": self.slab = _span_label(True); scene.add(self.slab)
        # the room ledger
        self.rows = {}
        if b in FILLED:
            self.header = _header(); scene.add(self.header)
            for i in FILLED[b]:
                r = VGroup(_seats(i), _coal(i), _val(i)); self.rows[i] = r; scene.add(r)
            self.tbars = VGroup(*[_tbar(i) for i in FILLED[b]]) if b != "B15" else VGroup()
            scene.add(self.tbars)
        # the bumps on the line (B11–B13)
        if b in ("B11", "B12", "B13"):
            self.tick63 = _ptick(0.63); scene.add(self.tick63)
            dimmed = b != "B11"
            self.b08 = _hbar(E_F, 0.63, color=DIM if dimmed else INK); self.l08 = _bump_label(E_F, 0.63, "+0.08", DIM if dimmed else INK)
            scene.add(self.b08, self.l08)
            if b != "B11":
                self.tick66 = _ptick(0.66); self.b06 = _hbar(0.66, F_X); self.l06 = _bump_label(0.66, F_X, "+0.06")
                scene.add(self.tick66, self.b06, self.l06)
        # the force plot
        if n >= 15 and b != "B17":
            self.fbars = _force_bars(); scene.add(self.fbars)
            if b in ("B15", "B19"): self.flabs = _force_labels(); scene.add(self.flabs)
            if b == "B16": self.eff = _effic(); scene.add(self.eff)
            if b == "B18": self.plug = _plug(); scene.add(self.plug)
        if b == "B16":
            self.wsum = _wsum(); self.shap = _shapley(); self.rail = _rail(); scene.add(self.wsum, self.shap, self.rail)
        if b == "B17":
            self.shap = _shapley(2.0, 42); self.sent = _sent(T1_SENT); self.sep = _sep(); self.gloss = _gloss(T1_GLOSS)
            self.worked = _m(WORKED_W, 40).move_to([0, -1.75, 0])
            scene.add(self.shap, self.sent, self.sep, self.gloss, self.worked)
        if b == "B18":
            self.eff = _effic(2.0, 44); self.sent = _sent(T2_SENT[:3]); self.sep = _sep(1.35, -0.35); self.gloss = _gloss(T2_GLOSS)
            scene.add(self.eff, self.sent, self.sep, self.gloss)
        if b == "B19":
            self.ans = _t("income's share: 0.073, the average", 36).move_to([0, 1.6, 0])
            self.zipnote = _t("zip 0.035: about the model, not the world", 32).move_to([0.3, 0.75, 0])
            scene.add(self.ans, self.zipnote)


def _names():
    return VGroup(_t("income", 36).move_to([-3.4, 1.6, 0]), _t("debt-to-income", 36).move_to([0.0, 1.6, 0]),
                  _t("zip code", 36).move_to([3.4, 1.6, 0]))
def _question(): return _t("how much of the 0.17 is income's?", 36).move_to([0, 0.55, 0])
def _rail(): return Line([-5.6, 1.95, 0], [-5.6, 0.75, 0], color=INK, stroke_width=3)


# ═══════════ B10 — HOOK ═══════════
class B10_OneApplicant(Scene):
    BASE = 11.0
    def construct(self):
        t = _title(TITLES["B10"]); self.add(t, _constructed())
        line = _line(); d = _pdot(E_F)
        self.play(Create(line[0]), FadeIn(line[1]), FadeIn(line[2][0]), FadeIn(line[2][2]), run_time=1.0)
        self.play(GrowFromCenter(d), run_time=0.4)
        self.play(FadeIn(line[2][1]), FadeIn(line[2][3]), d.animate.move_to([PX(F_X), LY, 0]), run_time=1.4)
        span = _span()
        self.play(GrowFromEdge(span, LEFT), run_time=0.9)
        self.play(FadeIn(_span_label()), run_time=0.5)
        names = _names()
        self.play(LaggedStart(*[FadeIn(n, shift=DOWN * 0.15) for n in names], lag_ratio=0.35), run_time=1.3)
        self.play(FadeIn(_question()), run_time=0.7)
        self.play(GrowFromCenter(_dot(-4.1, 1.6)), run_time=0.4)
        self.play(FadeIn(_cap(CAPS["B10"])), run_time=0.5)
        _finish(self)


# ═══════════ B11 — INSTANCE 1: income walks into an empty room ═══════════
class B11_IncomeFirst(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "B10"); dd = _dot(-4.1, 1.6); self.add(dd)
        self.play(FadeOut(st.q), FadeOut(dd), FadeOut(st.cap), FadeOut(st.names), FadeOut(st.slab),
                  Transform(st.t, _title(TITLES["B11"])), run_time=0.8)
        self.play(FadeIn(_header()), st.pdot.animate.move_to([PX(E_F), LY, 0]), run_time=0.9)
        self.wait(0.5)
        self.play(FadeIn(_seat(0, 0), shift=RIGHT * 0.5), run_time=0.8)
        b08 = _hbar(E_F, 0.63)
        self.play(st.pdot.animate.move_to([PX(0.63), LY, 0]), GrowFromEdge(b08, LEFT), FadeIn(_ptick(0.63)), run_time=1.3)
        self.play(FadeIn(_bump_label(E_F, 0.63, "+0.08")), run_time=0.4)
        tb = _tbar(0)
        self.play(FadeIn(_coal(0)), FadeIn(_val(0)), GrowFromEdge(tb, LEFT), run_time=0.8)
        self.play(FadeIn(_seat(0, 1), shift=RIGHT * 0.5), FadeIn(_seat(0, 2), shift=RIGHT * 0.5), run_time=0.8)
        self.play(GrowFromCenter(_row_dot(0)), run_time=0.4)
        self.play(FadeIn(_cap(CAPS["B11"])), run_time=0.5)
        _finish(self)


# ═══════════ B12 — NAIVE: drop it and see ═══════════
class B12_DropItAndSee(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "B11"); dd = _row_dot(0); self.add(dd)
        self.play(FadeOut(dd), FadeOut(st.cap), Transform(st.t, _title(TITLES["B12"])),
                  st.b08.animate.set_fill(DIM), st.l08.animate.set_color(DIM), run_time=0.7)
        self.play(FadeIn(_seat(5, 0), shift=RIGHT * 0.5), FadeIn(_seat(5, 1), shift=RIGHT * 0.5), run_time=0.8)
        self.play(st.pdot.animate.move_to([PX(F_X), LY, 0]), run_time=0.9)
        self.wait(0.6)
        t66 = _ptick(0.66)
        self.play(st.pdot.animate.move_to([PX(0.66), LY, 0]), FadeIn(t66), run_time=1.0)
        b06 = _hbar(0.66, F_X)
        self.play(GrowFromEdge(b06, RIGHT), FadeIn(_bump_label(0.66, F_X, "+0.06")), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(_seat(5, 2), shift=RIGHT * 0.5), st.pdot.animate.move_to([PX(F_X), LY, 0]), run_time=0.9)
        tb = _tbar(5)
        self.play(FadeIn(_coal(5)), FadeIn(_val(5)), GrowFromEdge(tb, LEFT), run_time=0.8)
        self.play(FadeIn(_t("+0.08 or +0.06?", 36).move_to([3.1, 1.1, 0])), run_time=0.6)
        self.play(Create(_x(5.05, 1.1)), run_time=0.5)
        self.play(FadeIn(_cap(CAPS["B12"])), run_time=0.5)
        _finish(self)


# ═══════════ B13 — INSTANCE 2: the seats in between ═══════════
class B13_MiddleSeats(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "B12")
        q = _t("+0.08 or +0.06?", 36).move_to([3.1, 1.1, 0]); xx = _x(5.05, 1.1); self.add(q, xx)
        self.play(FadeOut(q), FadeOut(xx), FadeOut(st.cap), Transform(st.t, _title(TITLES["B13"])), run_time=0.7)
        for i in (2, 3):
            self.play(FadeIn(_seat(i, 0), shift=RIGHT * 0.5), run_time=0.6)
            self.play(FadeIn(_seat(i, 1), shift=RIGHT * 0.5), run_time=0.6)
            tb = _tbar(i)
            self.play(FadeIn(_coal(i)), FadeIn(_val(i)), GrowFromEdge(tb, LEFT), FadeIn(_seat(i, 2), shift=RIGHT * 0.5), run_time=0.9)
            self.wait(0.4)
        self.play(GrowFromCenter(_row_dot(3)), run_time=0.4)
        self.play(FadeIn(_cap(CAPS["B13"])), run_time=0.5)
        _finish(self)


# ═══════════ B14 — SHIFT (predict): every order ═══════════
class B14_EveryOrder(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "B13"); dd = _row_dot(3); self.add(dd)
        self.play(FadeOut(dd), FadeOut(st.cap), Transform(st.t, _title(TITLES["B14"])), run_time=0.7)
        for i in (1, 4):
            tb = _tbar(i)
            self.play(FadeIn(_seats(i), shift=RIGHT * 0.4), FadeIn(_coal(i)), FadeIn(_val(i)), GrowFromEdge(tb, LEFT), run_time=1.0)
        c1 = _cap("six orders, each equally likely")
        self.play(FadeIn(c1), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(st.b08), FadeOut(st.l08), FadeOut(st.b06), FadeOut(st.l06), FadeOut(st.tick63), FadeOut(st.tick66),
                  st.pdot.animate.move_to([PX(E_F), LY, 0]), run_time=1.0)
        self.play(FadeIn(_span_label(True)), run_time=0.5)
        self.play(GrowFromCenter(_dot((PX(E_F) + PX(F_X)) / 2 + 1.35, LBY)), run_time=0.4)
        self.play(Transform(c1, _cap(CAPS["B14"])), run_time=0.5)
        _finish(self)


# ═══════════ B15 — TRANSFORM: average them; the bars fill the gap ═══════════
class B15_AverageThem(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "B14"); dd = _dot((PX(E_F) + PX(F_X)) / 2 + 1.35, LBY); self.add(dd)
        fb = _force_bars(); fl = _force_labels()
        self.play(FadeOut(dd), FadeOut(st.slab), FadeOut(st.cap), Transform(st.t, _title(TITLES["B15"])), run_time=0.6)
        self.play(ReplacementTransform(st.tbars, fb[0]), run_time=2.2)
        self.play(FadeIn(fl[0]), st.pdot.animate.move_to([PX(E_F + 0.073), LY, 0]), run_time=0.6)
        self.wait(0.6)
        self.play(GrowFromEdge(fb[1], LEFT), FadeIn(fl[1]), st.pdot.animate.move_to([PX(E_F + 0.135), LY, 0]), run_time=1.1)
        self.play(GrowFromEdge(fb[2], LEFT), FadeIn(fl[2]), st.pdot.animate.move_to([PX(F_X), LY, 0]), run_time=1.1)
        self.wait(0.5)
        self.play(GrowFromCenter(_dot(PX(F_X), LY + 0.45)), run_time=0.4)
        self.play(FadeIn(_cap(CAPS["B15"])), run_time=0.5)
        _finish(self)


# ═══════════ B16 — ABSTRACTION: name it ═══════════
class B16_NameIt(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "B15"); dd = _dot(PX(F_X), LY + 0.45); self.add(dd)
        self.play(FadeOut(dd), FadeOut(st.cap), Transform(st.t, _title("Six Orders, Grouped")), run_time=0.6)
        ws = _wsum()
        cols = VGroup(*[VGroup(st.rows[i][1], st.rows[i][2]) for i in range(6)])
        self.play(FadeOut(st.header), *[FadeOut(st.rows[i][0]) for i in range(6)], run_time=0.6)
        self.play(ReplacementTransform(cols, ws), run_time=2.0)
        self.wait(0.5)
        sh = _shapley()
        self.play(Write(sh), run_time=2.0)
        self.play(Create(_rail()), run_time=0.6)
        self.play(Transform(st.t, _title(TITLES["B16"])), run_time=0.6)
        self.play(GrowFromCenter(_dot(WS_DOT_X, 1.95)), run_time=0.4)
        self.play(ReplacementTransform(st.flabs, _effic()), run_time=1.4)
        self.play(FadeIn(_cap(CAPS["B16"])), run_time=0.5)
        _finish(self)


# ═══════════ B17 — TANGENT 1: read the Shapley formula ═══════════
class B17_ReadTheFormula(Scene):
    BASE = 18.0
    def construct(self):
        st = _Stage(self, "B16"); dd = _dot(WS_DOT_X, 1.95); self.add(dd)
        self.play(FadeOut(dd), FadeOut(st.cap), FadeOut(st.wsum), FadeOut(st.rail), FadeOut(st.eff), FadeOut(st.fbars),
                  FadeOut(st.line), FadeOut(st.span), FadeOut(st.pdot), Transform(st.t, _title(TITLES["B17"])), run_time=0.8)
        self.play(Transform(st.shap, _shapley(2.0, 42)), run_time=0.9)
        self.play(Create(_sep()), run_time=0.5)
        sent = _sent(T1_SENT); gloss = _gloss(T1_GLOSS)
        spot = _dot(-6.1, TROWS[0], 0.11)
        self.play(FadeIn(sent[0], shift=RIGHT * 0.15), GrowFromCenter(spot), run_time=0.7)
        self.play(FadeIn(sent[1], shift=RIGHT * 0.15), spot.animate.move_to([-6.1, TROWS[1], 0]), run_time=0.7)
        self.play(FadeIn(sent[2], shift=RIGHT * 0.15), spot.animate.move_to([-6.1, TROWS[2], 0]), run_time=0.7)
        for i, g in enumerate(gloss):
            self.play(FadeIn(g, shift=RIGHT * 0.1), spot.animate.move_to([GS_X - 0.25, TROWS[i], 0]), run_time=0.6)
        worked = _m(WORKED_W, 40).move_to([0, -1.75, 0])
        self.play(Write(worked), spot.animate.move_to([-4.7, -1.75, 0]), run_time=1.4)
        self.play(FadeIn(_cap(CAPS["B17"])), run_time=0.5)
        _finish(self)


# ═══════════ B18 — TANGENT 2: read the efficiency sum ═══════════
class B18_ReadTheSum(Scene):
    BASE = 18.0
    def construct(self):
        st = _Stage(self, "B17")
        self.play(FadeOut(st.cap), FadeOut(st.sent), FadeOut(st.gloss), FadeOut(st.sep), FadeOut(st.worked), FadeOut(st.shap),
                  Transform(st.t, _title(TITLES["B18"])), run_time=0.8)
        line = _line(); span = _span(); fb = _force_bars(); d = _pdot(F_X)
        self.play(FadeIn(line), FadeIn(span), FadeIn(fb), FadeIn(d), run_time=0.8)
        eff = _effic(2.0, 44)
        self.play(Write(eff), run_time=1.2)
        self.play(Create(_sep(1.35, -0.35)), run_time=0.5)
        sent = _sent(T2_SENT); gloss = _gloss(T2_GLOSS)
        for s in sent:
            self.play(FadeIn(s, shift=RIGHT * 0.15), run_time=0.7)
        for g in gloss:
            self.play(FadeIn(g, shift=RIGHT * 0.1), run_time=0.6)
        self.wait(0.4)
        self.play(Write(_plug()), run_time=1.6)
        self.play(GrowFromCenter(_dot(4.55, LBY)), run_time=0.4)
        self.play(FadeIn(_cap(CAPS["B18"])), run_time=0.5)
        _finish(self)


# ═══════════ B19 — PAYOFF ═══════════
class B19_Payoff(Scene):
    BASE = 15.0
    def construct(self):
        st = _Stage(self, "B18"); dd = _dot(4.55, LBY); self.add(dd)
        self.play(FadeOut(dd), FadeOut(st.cap), FadeOut(st.eff), FadeOut(st.sent), FadeOut(st.gloss), FadeOut(st.sep),
                  Transform(st.t, _title(TITLES["B19"])), ReplacementTransform(st.plug, _force_labels()), run_time=1.0)
        q = _question().move_to([0, 1.6, 0])
        self.play(FadeIn(q), run_time=0.6)
        g08 = _hbar(E_F, 0.63, y=0.75, color=DIM); g06 = _hbar(E_F, 0.61, y=0.15, color=DIM)
        l08 = _t("first in, +0.08", 32, DIM).move_to([PX(0.63) + 0.3, 0.75, 0], aligned_edge=LEFT)
        l06 = _t("last in, +0.06", 32, DIM).move_to([PX(0.61) + 0.3, 0.15, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(g08, LEFT), FadeIn(l08), run_time=0.7)
        self.play(GrowFromEdge(g06, LEFT), FadeIn(l06), run_time=0.7)
        inc = st.fbars[0].copy()
        self.play(FadeOut(l08), FadeOut(l06), ReplacementTransform(VGroup(g08, g06), inc), run_time=1.4)
        self.play(Transform(q, _t("income's share: 0.073, the average", 36).move_to([0, 1.6, 0])), run_time=0.8)
        self.wait(0.6)
        dz = _dot(PX(E_F + 0.135 + 0.0175), LY + 0.45)
        self.play(GrowFromCenter(dz), run_time=0.4)
        self.play(FadeIn(_t("zip 0.035: about the model, not the world", 32).move_to([0.3, 0.75, 0])), run_time=0.7)
        self.play(FadeIn(_cap(CAPS["B19"])), run_time=0.5)
        _finish(self)
