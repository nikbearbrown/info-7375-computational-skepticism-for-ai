"""
Manim scenes for show-tell-a-test-that-cant-fail (show-tell skill; INFO 7375 course film, Film 3 of
SHOW-TELL-THREE-MOVES.md: falsifiability, Popper).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py. The kit, pacing
helpers and midpoint guard are copied from the sibling course film show-tell-induction-until-it-changes
(itself from show-tell-skepticism-is-a-method), with a larger end slack (_END) for 24 fps frame rounding.

A test that can't fail isn't a test. The CLAIM (a white page on a dark plinth) and a row of kraft OUTCOME
tiles: one possible result would refute it (Popper, The Logic of Scientific Discovery, 1934). Cases of every
shape slide into a theory that fits them all, each adding a check, and the refuting slot stays empty.
The 1919 ECLIPSE: three answers marked on a RULER before the look (0, Newton, Einstein); the star's image
lands on Einstein's mark, and a cross at 0 is the result that would have refuted it. The TESTER, a kraft
machine on a belt: working and broken CODE crates both pass; rewritten with a FAIL-CONDITION card written
first (terracotta seal), the broken crate drops into the fail bin. "Robust" is rewritten as a daily error
chart with a 2% line over 30 days, which a bad month crosses. The dark AGENT grades its own REPORT: a check
whether it stacks the blocks, knocks them over or does nothing. The agent swaps the tester's card and a
broken crate passes (Claude 3.7 Sonnet system card). The close: the fail condition written first, checked
by an outside scan, with a fail slot that stays open.
A midpoint guard (ST / guard, 0.22 s margin) keeps every animation off the clip midpoint, where GATE T and
Gate V sample.
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if n and phrase not in n:
        print(f"[until] MISSING phrase in {bid}: {phrase!r}")
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ─────────────── midpoint guard: GATE T and Gate V sample each clip at its midpoint ───────────────
class ST:
    """No animation straddles the clip midpoint: one that would cross it is shortened to land before
    it, or starts just after it, so the midpoint frame is always a still. Attached to every beat class
    at the bottom of this file (run.sh finds scenes only by the literal `(Scene)`)."""
    def play(self, *anims, **kw):
        if not all(isinstance(a, Wait) for a in anims):
            kw["run_time"] = guard(self, float(kw.get("run_time", 1.0)))
        return Scene.play(self, *anims, **kw)


def guard(self, rt):
    """If an animation of length rt starting now would straddle the midpoint, shorten it to land before
    the midpoint or wait until just after it. Returns the run time to use. Call it BEFORE staging anything
    off-position, so nothing sits at the frame edge during the wait."""
    tgt = _TARGET.get(type(self).__name__.split("_")[0], 0)
    if not tgt:
        return rt
    mid, t0 = tgt / 2.0, _elapsed(self)
    M = 0.22                                     # margin: frame rounding drifts the real clip clock
    if t0 < mid + M and t0 + rt > mid - M:
        room = mid - M - t0
        if room >= 0.6 * rt and room > 0.25:
            return room
        Scene.wait(self, max(0.02, mid + M - t0))
    return rt


_SLACK = {}     # per-beat extra end slack, if a 4K clip still runs past its audio (BUILD-LOG)
_END = 0.15      # base end slack: every guarded wait/play rounds UP to whole frames at 24 fps (sibling induction film, BUILD-LOG)


def done(self):
    """finish() plus a pacing report (a clip must not outrun its audio: compile centre-cuts it)."""
    bid = type(self).__name__.split("_")[0]
    t = _elapsed(self)
    tgt = _TARGET.get(bid, 0)
    print(f"[pace] {bid} content={t:.2f}s target={tgt:.2f}s" + ("  OVER" if t > tgt - 0.1 else ""))
    if tgt:
        self.wait(max(0.05, tgt - t - _END - _SLACK.get(bid, 0.0)))     # end ~0.15 s under the audio (24 fps frame rounding)
    else:
        self.wait(2.0)


# ═════════════════════════════ the film: a test that can't fail isn't a test ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
PAD = "#E6E1D6"            # within Gate V's INK_DELTA of the stage
AG_TOP, AG_L, AG_R = "#2E2A26", "#1B1815", "#141210"   # the agent block (darker than DARK_*, so it never fuses with ink)


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=42):
    return T(s, size).move_to(P3(c))


def cross(x, y, s=0.24, w=9):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=INK, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=INK, stroke_width=w))


# ─── the CLAIM: a white page on a dark plinth ───
CLW, CLD, CLH = 2.0, 1.6, 0.5


def claim(c, s):
    i = rig_at(c[0], c[1], s, CLW, CLD)
    plinth = i.box(0, 0, 0, CLW, CLD, CLH, DARK_TOP, DARK_L, DARK_R)
    page = i.box(0.15, 0.15, CLH, CLW - 0.3, CLD - 0.3, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    return VGroup(plinth, page)


def claim_lines(c, s):
    i = rig_at(c[0], c[1], s, CLW, CLD)
    zt = CLH + 0.06
    return VGroup(*[Line(i.p(0.45, CLD * f, zt), i.p(CLW - 0.45 - (0.35 if k == 2 else 0.0), CLD * f, zt), color=BAR2, stroke_width=6)
                    for k, f in enumerate((0.7, 0.5, 0.3))])


def claim_dot(c, s):
    i = rig_at(c[0], c[1], s, CLW, CLD)
    return Dot(i.p(0.4, CLD * 0.84, CLH + 0.06), radius=0.1, color=TERRA).set_z_index(3)


# ─── OUTCOME tiles: the possible results ───
TW, TD, TH = 0.9, 0.9, 0.22


def tile(x, y, s=1.0, white=False):
    i = rig_at(x, y, s, TW, TD)
    if white:
        return i.box(0, 0, 0, TW, TD, TH, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    return i.box(0, 0, 0, TW, TD, TH)


def empty_tile(x, y, s=1.0):
    """An empty slot: the tile's top outline only, filled with the stage colour."""
    i = rig_at(x, y, s, TW, TD)
    return i.quad([(0, 0, 0), (TW, 0, 0), (TW, TD, 0), (0, TD, 0)], STAGE, sw=5)


# ══════════════ B00: Popper — some possible result must be able to refute it ══════════════
CL0, CLS0 = (-4.0, -0.9), 1.45
TX = [-0.2, 1.6, 3.4, 5.2]
TY = -1.35
TS0 = 1.05
RF = 2                         # the refuting tile


def l_popper():
    return lbl("Popper, 1934", (CL0[0], 2.6), 48)


def l_results():
    return lbl("possible results", (2.5, -2.85))


def l_refutes():
    return lbl("refutes it", (TX[RF], 1.0))


def rf_cross():
    return cross(TX[RF], 0.05, 0.26)


def b00_state():
    return VGroup(claim(CL0, CLS0), claim_lines(CL0, CLS0), claim_dot(CL0, CLS0), l_popper(),
                  VGroup(*[tile(x, TY, TS0, white=(k == RF)) for k, x in enumerate(TX)]), l_results(), rf_cross(), l_refutes())


class B00_Criterion(Scene):
    def construct(self):
        cl, ln = claim(CL0, CLS0), claim_lines(CL0, CLS0)
        self.play(FadeIn(cl, shift=RIGHT * 0.5), run_time=0.6)
        self.play(LaggedStart(*[Create(x) for x in ln], lag_ratio=0.3), run_time=0.6)
        until(self, "Karl Popper", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_popper()), run_time=rt)
        until(self, "A claim is scientific", lead=0.3)
        tl = [tile(x, TY, TS0) for x in TX]
        rt = guard(self, 1.5)
        self.play(LaggedStart(*[FadeIn(t_, shift=DOWN * 0.5) for t_ in tl], lag_ratio=0.3), FadeIn(l_results()), run_time=rt, rate_func=ease_in)
        until(self, "prove it wrong", lead=0.3)
        wt = tile(TX[RF], TY, TS0, white=True)
        rt = guard(self, 0.6)
        self.play(FadeOut(tl[RF]), FadeIn(wt), Create(rf_cross()), FadeIn(l_refutes()), run_time=rt)
        until(self, "In his words", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(claim_dot(CL0, CLS0), scale=1.6), run_time=rt)
        until(self, "refuted by experience", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(wt), color=None, scale_factor=1.12), run_time=rt)
        done(self)


# ══════════════ B01: a theory that fits every case ══════════════
CK_Y = 1.65
CK_X = [-5.6, -4.8, -4.0, -3.2, -2.4]
EMP = (TX[RF], TY)


def shape(k, x, y):
    """Cases of opposite shapes: a slab, a tall bar, a cube, a long block, a small cube."""
    dims = [(1.3, 0.9, 0.22), (0.5, 0.5, 1.3), (0.8, 0.8, 0.8), (1.5, 0.55, 0.4), (0.55, 0.55, 0.55)][k]
    i = rig_at(x, y, 1.25, dims[0], dims[1])
    return i.box(0, 0, 0, *dims)


def ck(k):
    return check(CK_X[k], CK_Y, 0.3)


def l_fits():
    return lbl("fits all", (-4.0, 2.65), 46)


def l_cantfail():
    return lbl("can't fail", (EMP[0], 0.25))


def b01_state():
    return VGroup(claim(CL0, CLS0), claim_lines(CL0, CLS0), VGroup(*[ck(k) for k in range(5)]), l_fits(),
                  empty_tile(EMP[0], EMP[1], 1.3), l_cantfail())


class B01_FitsAll(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[2], st[3], st[4], st[5], st[6], st[7])), run_time=0.45)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_fits()), run_time=rt)
        until(self, "any case at all", lead=0.4)
        cks = []
        for k in range(5):
            sh = shape(k, 4.3, -1.5)
            rt = guard(self, 0.25)
            self.play(FadeIn(sh, shift=LEFT * 0.6), run_time=rt)
            rt = guard(self, 0.35)
            self.play(sh.animate.move_to([-2.0, -1.0, 0]).scale(0.45), run_time=rt, rate_func=ease_in)
            self.remove(sh)
            c_ = ck(k)
            cks.append(c_)
            rt = guard(self, 0.2)
            self.play(Create(c_), run_time=rt)
        until(self, "called that strength", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(*cks), color=None, scale_factor=1.12), run_time=rt)
        until(self, "no possible event", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Create(empty_tile(EMP[0], EMP[1], 1.3)), FadeIn(l_cantfail()), run_time=rt)
        done(self)


# ══════════════ B02: the risky prediction — the 1919 eclipse ══════════════
DISC = (-1.9, 1.95)
DR = 0.8
STAR = (5.2, 1.25)
CAM = (-5.5, 1.1)
RU_Y = -2.0
TK_X = [-2.6, 0.0, 2.65]          # 0, 0.87", 1.75" of arc (Dyson, Eddington & Davidson 1920), at 3.0 units per second of arc
TK_N = ["0", "Newton", "Einstein"]
PT_Y = -1.3


def disc():
    halo = Circle(radius=DR + 0.3, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(P3(DISC))
    body = Circle(radius=DR, fill_color=AG_TOP, fill_opacity=1, stroke_width=0).move_to(P3(DISC))
    return VGroup(halo, body)


def star():
    return Dot(P3(STAR), radius=0.16, color=TERRA).set_z_index(3)


def camera():
    i = rig_at(CAM[0], CAM[1] - 0.5, 1.0, 0.9, 0.9)
    body = i.box(0, 0, 0, 0.9, 0.9, 0.75)
    lens = Circle(radius=0.17, fill_color=AG_TOP, fill_opacity=1, stroke_width=0).move_to(i.p(0.45, 0, 0.38))
    return VGroup(body, lens)


def ray():
    low = (DISC[0], DISC[1] - DR - 0.62)
    return VMobject(color=INK, stroke_width=6).set_points_smoothly(
        [P3(STAR), P3((1.6, low[1] - 0.18)), P3(low), P3((-3.9, low[1] + 0.2)), P3((CAM[0] + 0.55, CAM[1] + 0.05))])


def ruler():
    return Polygon([-3.3, RU_Y - 0.3, 0], [3.4, RU_Y - 0.3, 0], [3.4, RU_Y, 0], [-3.3, RU_Y, 0],
                   fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4)


def ticks():
    return VGroup(*[Line([x, RU_Y, 0], [x, RU_Y + 0.36, 0], color=INK, stroke_width=8) for x in TK_X])


def tick_lbls():
    return VGroup(*[T(n, 42).move_to([x, RU_Y - 0.72, 0]) for x, n in zip(TK_X, TK_N)])


def pointer(x):
    return Polygon([x, PT_Y - 0.28, 0], [x - 0.24, PT_Y + 0.14, 0], [x + 0.24, PT_Y + 0.14, 0],
                   fill_color=INK, fill_opacity=1, stroke_width=0).set_z_index(3)


def ghost_pointer(x):
    return Polygon([x, PT_Y - 0.28, 0], [x - 0.24, PT_Y + 0.14, 0], [x + 0.24, PT_Y + 0.14, 0],
                   fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=4).set_z_index(3)


def e_dot():
    return Dot([TK_X[2], PT_Y + 0.55, 0], radius=0.12, color=TERRA)


def e_cross():
    return cross(TK_X[0], PT_Y + 0.75, 0.22)


def l_1919():
    return lbl("1919", (DISC[0] + 1.75, DISC[1] + 0.35), 48)


def b02_state():
    return VGroup(disc(), star(), camera(), ray(), ruler(), ticks(), tick_lbls(), pointer(TK_X[2]),
                  e_dot(), ghost_pointer(TK_X[0]), e_cross(), l_1919())


class B02_Eclipse(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        dk = disc()
        self.play(FadeIn(dk), run_time=0.5)
        until(self, "starlight", lead=0.3)
        sr, cm = star(), camera()
        rt = guard(self, 0.5)
        self.play(FadeIn(sr, scale=1.5), FadeIn(cm, shift=RIGHT * 0.3), run_time=rt)
        until(self, "would bend", lead=0.3)
        ry = ray()
        rt = guard(self, 1.0)
        self.play(Create(ry), run_time=rt)
        until(self, "eclipse expeditions", lead=0.3)
        ru = ruler()
        rt = guard(self, 0.5)
        self.play(FadeIn(l_1919()), FadeIn(ru, shift=UP * 0.3), run_time=rt)
        tk, tl = ticks(), tick_lbls()
        for k, ph in enumerate(("no shift", "a small shift", "Einstein's larger one")):
            until(self, ph, lead=0.25)
            rt = guard(self, 0.4)
            self.play(Create(tk[k]), FadeIn(tl[k]), run_time=rt)
        until(self, "They reported his", lead=0.3)
        pt = pointer(TK_X[0])
        rt = guard(self, 0.25)
        self.play(FadeIn(pt), run_time=rt)
        rt = guard(self, 0.7)
        self.play(pt.animate.shift(RIGHT * (TK_X[2] - TK_X[0])), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(e_dot(), scale=1.6), run_time=rt)
        until(self, "clearly absent", lead=0.3)
        rt = guard(self, 0.6)
        self.play(FadeIn(ghost_pointer(TK_X[0])), Create(e_cross()), run_time=rt)
        until(self, "simply refuted", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(tk[0], color=None, scale_factor=1.3), run_time=rt)
        done(self)


# ══════════════ the TESTER: a kraft machine on a belt ══════════════
MC = (0.7, -1.25)
MW, MD, MH = 2.0, 1.6, 1.45
BELT_Y = -1.95
IN_X = -1.1                     # where a crate enters the machine
CR = 0.62                       # crate size


def m_rig():
    return rig_at(MC[0], MC[1], 1.0, MW, MD)


def machine():
    i = m_rig()
    body = i.box(0, 0, 0, MW, MD, MH)
    slot = i.quad([(0, 0.55, 0.12), (0, 1.05, 0.12), (0, 1.05, 0.72), (0, 0.55, 0.72)], BOX_FLOOR, stroke=DEV_EDGE, sw=3)
    chute = i.quad([(1.25, 0, 0.12), (1.75, 0, 0.12), (1.75, 0, 0.62), (1.25, 0, 0.62)], BOX_FLOOR, stroke=DEV_EDGE, sw=3)
    return VGroup(body, slot, chute)


def lamp(on=False):
    i = m_rig()
    return Circle(radius=0.2, fill_color=TERRA if on else GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4) \
        .move_to(i.p(0.6, 0, 1.0)).set_z_index(2)


def belt():
    return VGroup(Polygon([-5.9, BELT_Y - 0.3, 0], [IN_X + 0.2, BELT_Y - 0.3, 0], [IN_X + 0.2, BELT_Y + 0.05, 0], [-5.9, BELT_Y + 0.05, 0],
                          fill_color=PAD, fill_opacity=1, stroke_width=0),
                  Line([-5.9, BELT_Y - 0.3, 0], [IN_X + 0.2, BELT_Y - 0.3, 0], color=DEV_EDGE, stroke_width=4))


def crate(x, y, s=1.0, broken=False):
    """A kraft code crate; a broken one is split in two halves with a gap."""
    c = CR * s
    i = rig_at(x, y + c * 0.5, 1.0, c, c)
    if not broken:
        return i.box(0, 0, 0, c, c, c, sw=4).set_z_index(2)
    a = i.box(0, 0, 0, c * 0.44, c, c, sw=4)
    b = i.box(c * 0.56, 0, -0.12 * s, c * 0.44, c, c, sw=4)
    return VGroup(a, b).set_z_index(2)


def l_test():
    return lbl("test", (0.7, 1.95))


# results on the right
PASS_Y = 0.75
R_X = 4.2


def result_crate(row_y, broken=False):
    return crate(R_X - 0.35, row_y - 0.35, 0.9, broken)


def result_check(row_y):
    return check(R_X + 0.95, row_y + 0.1, 0.26)


ROW2_Y = -1.15


def l_always():
    return lbl("always passes", (R_X + 0.35, 2.3))


def b03_state():
    return VGroup(belt(), machine(), lamp(), l_test(), result_crate(PASS_Y), result_check(PASS_Y),
                  result_crate(ROW2_Y, True), result_check(ROW2_Y), l_always())


def feed(self, broken, rt_in=1.0):
    """A crate rides the belt into the machine; the lamp blinks. Returns nothing (the crate is removed)."""
    cr = crate(-5.1, BELT_Y, 1.0, broken)
    rt = guard(self, 0.3)
    self.play(FadeIn(cr, shift=RIGHT * 0.3), run_time=rt)
    rt = guard(self, rt_in)
    self.play(cr.animate.shift(RIGHT * (IN_X - 0.3 + 5.1)), run_time=rt, rate_func=linear)
    self.remove(cr)


class B03_AlwaysPasses(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        mc, bl, lp = machine(), belt(), lamp()
        self.play(FadeIn(VGroup(bl, mc, lp), shift=UP * 0.3), run_time=0.6)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_test()), run_time=rt)
        until(self, "Feed it working code", lead=0.3)
        feed(self, False, 0.9)
        on = lamp(True)
        rt = guard(self, 0.3)
        self.play(FadeIn(on), FadeIn(result_crate(PASS_Y), shift=RIGHT * 0.4), run_time=rt)
        k1 = result_check(PASS_Y)
        rt = guard(self, 0.3)
        self.play(Create(k1), FadeOut(on), run_time=rt)
        until(self, "Feed it broken code", lead=0.3)
        feed(self, True, 0.9)
        on2 = lamp(True)
        rt = guard(self, 0.3)
        self.play(FadeIn(on2), FadeIn(result_crate(ROW2_Y, True), shift=RIGHT * 0.4), run_time=rt)
        k2 = result_check(ROW2_Y)
        rt = guard(self, 0.3)
        self.play(Create(k2), FadeOut(on2), run_time=rt)
        until(self, "always passes", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_always()), run_time=rt)
        until(self, "which one you had", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(k1, k2), color=None, scale_factor=1.15), run_time=rt)
        done(self)


# ══════════════ B04: rewritten with a fail condition, written first ══════════════
FAIL_Y = -1.55


def card():
    """The fail-condition card: a white page lying on the machine's top, with lines and a terracotta seal."""
    i = m_rig()
    z = MH
    slab = i.box(0.3, 0.25, z, MW - 0.6, MD - 0.5, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    return slab.set_z_index(2)


def card_lines():
    i = m_rig()
    z = MH + 0.06
    return VGroup(*[Line(i.p(0.55, MD * f, z), i.p(MW - 0.55 - (0.3 if k == 1 else 0.0), MD * f, z), color=BAR1, stroke_width=6)
                    for k, f in enumerate((0.62, 0.42))]).set_z_index(3)


def seal():
    i = m_rig()
    return Dot(i.p(MW - 0.55, MD * 0.3, MH + 0.06), radius=0.11, color=TERRA).set_z_index(3)


def l_first():
    return lbl("written first", (0.7, 2.25))


def fail_bin():
    i = rig_at(R_X - 0.2, FAIL_Y - 0.6, 1.0, 1.3, 1.0)
    back, front = i.open_box(0, 0, 0, 1.3, 1.0, 0.55)
    return back, front


def l_fail():
    return lbl("fail", (R_X - 0.2, -3.05))


def fail_cross():
    return cross(R_X + 1.25, FAIL_Y + 0.3, 0.24)


def b04_state():
    back, front = fail_bin()
    return VGroup(belt(), machine(), lamp(), card(), card_lines(), seal(), l_first(), back, crate(R_X - 0.25, FAIL_Y - 0.45, 0.9, True).set_z_index(1),
                  front, l_fail(), fail_cross(), result_crate(PASS_Y), result_check(PASS_Y))


class B04_FailCondition(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[3], st[4], st[5], st[6], st[7], st[8])), run_time=0.45)
        until(self, "fail condition", lead=0.4)
        cd = card()
        rt = guard(self, 0.5)
        self.play(FadeIn(cd, shift=DOWN * 0.6), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[Create(x) for x in card_lines()], lag_ratio=0.4), FadeIn(l_first()), run_time=rt)
        until(self, "or the test fails", lead=0.3)
        back, front = fail_bin()
        rt = guard(self, 0.5)
        self.play(FadeIn(VGroup(back, front), shift=UP * 0.3), FadeIn(l_fail()), run_time=rt)
        until(self, "laid down beforehand", lead=0.4)
        sl = seal()
        rt = guard(self, 0.4)
        self.play(FadeIn(sl, scale=1.8), run_time=rt)
        until(self, "Now broken code fails", lead=0.9)
        feed(self, True, 0.5)
        bc = crate(R_X - 0.25, FAIL_Y - 0.45, 0.9, True).set_z_index(1)
        self.add(bc)
        self.bring_to_front(front)
        bc.shift(UP * 0.8)
        rt = guard(self, 0.3)
        self.play(bc.animate.shift(DOWN * 0.8), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.25)
        self.play(Create(fail_cross()), run_time=rt)
        feed(self, False, 0.45)
        on = lamp(True)
        rt = guard(self, 0.25)
        self.play(FadeIn(on), FadeIn(result_crate(PASS_Y), shift=RIGHT * 0.4), run_time=rt)
        rt = guard(self, 0.25)
        self.play(Create(result_check(PASS_Y)), FadeOut(on), run_time=rt)
        done(self)


# ══════════════ B05: "the system is robust" rewritten with a metric, a threshold and a window ══════════════
CL5, CLS5 = (-4.75, -0.9), 1.0
AX_Y = -2.3
BX0, BW, BG = -1.75, 0.21, 0.04
TH_Y = AX_Y + 2.3                # the 2% line
HS = [1.0, 1.4, 0.9, 1.3, 1.6, 1.1, 0.8, 1.4, 1.5, 1.0, 1.3, 1.7, 1.1, 0.9, 1.4, 1.6, 1.3, 1.0, 1.5, 1.2,
      1.4, 1.0, 1.5, 1.8, 1.4, 1.2, 1.6, 1.3, 1.0, 1.4]
BAD = [(19, 2.7), (20, 3.0), (21, 3.35), (22, 2.9), (23, 3.2), (24, 2.8)]


def bx(k):
    return BX0 + k * (BW + BG) + BW / 2


def day_bar(k, h):
    return Rectangle(width=BW, height=h, fill_color=(BAR1, BAR2)[k % 2], fill_opacity=1, stroke_width=0) \
        .move_to([bx(k), AX_Y + h / 2, 0])


def days():
    return VGroup(*[day_bar(k, h) for k, h in enumerate(HS)])


def axis5():
    return Line([BX0 - 0.15, AX_Y, 0], [bx(29) + 0.25, AX_Y, 0], color=DEV_EDGE, stroke_width=5)


def thr():
    return Line([BX0 - 0.15, TH_Y, 0], [bx(29) + 0.25, TH_Y, 0], color=INK, stroke_width=6).set_z_index(2)


def l_2pct():
    return lbl("2%", (BX0 - 0.6, TH_Y + 0.02), 46)


def l_30():
    return lbl("30 days", ((BX0 + bx(29)) / 2, AX_Y - 0.6), 44)


def l_robust():
    return lbl("robust", (CL5[0], 1.55), 50)


def bad_dot():
    return Dot([bx(21), AX_Y + 3.35 + 0.22, 0], radius=0.13, color=TERRA).set_z_index(3)


def bad_cross():
    return cross(bx(21), AX_Y + 3.35 + 0.82, 0.24)


def b05_state():
    d = days()
    for k, h in BAD:
        d[k].stretch_to_fit_height(h).move_to([bx(k), AX_Y + h / 2, 0])
    return VGroup(claim(CL5, CLS5), claim_lines(CL5, CLS5), l_robust(), axis5(), d, thr(), l_2pct(), l_30(), bad_dot(), bad_cross())


class B05_Robust(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        cl, ln = claim(CL5, CLS5), claim_lines(CL5, CLS5)
        rt = guard(self, 0.6)
        self.play(FadeIn(cl, shift=RIGHT * 0.4), run_time=rt)
        until(self, "The system is robust", lead=0.3)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[Create(x) for x in ln], lag_ratio=0.3), FadeIn(l_robust()), run_time=rt)
        until(self, "None is named", lead=0.3)
        et = empty_tile(-1.2, -1.2, 1.3)
        rt = guard(self, 0.5)
        self.play(Create(et), run_time=rt)
        until(self, "soothsayer", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(et, color=None, scale_factor=1.15), run_time=rt)
        until(self, "Rewrite it", lead=0.3)
        rt = guard(self, 0.3)
        self.play(FadeOut(et), run_time=rt)
        ax, d = axis5(), days()
        rt = guard(self, 1.2)
        self.play(Create(ax), LaggedStart(*[GrowFromEdge(b_, DOWN) for b_ in d], lag_ratio=0.08), FadeIn(l_30()), run_time=rt)
        until(self, "two percent", lead=0.4)
        rt = guard(self, 0.5)
        self.play(Create(thr()), FadeIn(l_2pct()), run_time=rt)
        until(self, "a bad month", lead=0.3)
        rt = guard(self, 0.8)
        self.play(*[d[k].animate.stretch_to_fit_height(h).move_to([bx(k), AX_Y + h / 2, 0]) for k, h in BAD], run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(bad_dot(), scale=1.6), Create(bad_cross()), run_time=rt)
        done(self)


# ══════════════ B06: the agent that grades its own work ══════════════
AG = (-4.4, -1.2)
AGS = 1.35
RP = (-4.4, 1.75)
FL_Y = -2.1
TWX = 1.9


def agent(c=AG, s=AGS):
    i = rig_at(c[0], c[1], s, 1.5, 1.5)
    body = i.box(0, 0, 0, 1.5, 1.5, 0.95, AG_TOP, AG_L, AG_R)
    ports = VGroup(*[i.box(1.5 * f, -0.16, 0.3, 0.24, 0.16, 0.32, GHOST, BOX_IN1, BOX_IN2, sw=1) for f in (0.2, 0.6)])
    return VGroup(body, ports)


def report(c=RP):
    r = RoundedRectangle(width=1.8, height=1.25, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3(c))
    lines = VGroup(*[Line([c[0] - 0.6, c[1] + dy, 0], [c[0] + 0.6 - (0.35 if k == 2 else 0.0), c[1] + dy, 0], color=BAR1, stroke_width=7)
                     for k, dy in enumerate((0.3, 0.0, -0.3))])
    return VGroup(r, lines)


RCK_X = [-2.75, -1.85, -0.95, -0.05, 0.85]


def rck(k):
    return check(RCK_X[k], RP[1], 0.3)


def l_agent():
    return lbl("agent", (AG[0], -3.0))


def l_report():
    return lbl("report", (RP[0], 2.85))


def blk(x, z_level, s=0.85):
    i = rig_at(x, FL_Y + s * 0.5 + z_level * s, 1.0, s, s)
    return i.box(0, 0, 0, s, s, s, sw=4).set_z_index(2)


def tower():
    return VGroup(*[blk(TWX, k) for k in range(3)])


FALLEN = [(0.9, -2.05, 0.0), (2.55, -2.35, 0.35), (4.1, -1.95, -0.3)]


def fallen(k):
    x, y, a = FALLEN[k]
    return blk(TWX, 0).move_to([x, y, 0]).rotate(a)


def b06_state():
    return VGroup(agent(), l_agent(), report(), l_report(), VGroup(*[rck(k) for k in range(5)]),
                  VGroup(*[fallen(k) for k in range(3)]))


class B06_SelfGrader(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        ag, rp = agent(), report()
        self.play(FadeIn(ag, shift=UP * 0.3), FadeIn(l_agent()), run_time=0.6)
        until(self, "grades its own work", lead=0.4)
        rt = guard(self, 0.5)
        self.play(FadeIn(rp, shift=DOWN * 0.3), FadeIn(l_report()), run_time=rt)
        until(self, "It stacks the blocks", lead=0.2)
        tw = tower()
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(b_, shift=DOWN * 0.6) for b_ in tw], lag_ratio=0.4), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.25)
        self.play(Create(rck(0)), run_time=rt)
        until(self, "It knocks them over", lead=0.2)
        rt = guard(self, 0.6)
        self.play(*[Transform(tw[k], fallen(k)) for k in range(3)], run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.25)
        self.play(Create(rck(1)), run_time=rt)
        until(self, "It does nothing at all", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(ag, color=None, scale_factor=1.04), run_time=rt)
        rt = guard(self, 0.25)
        self.play(Create(rck(2)), run_time=rt)
        until(self, "no matter what it does", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Create(rck(3)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Create(rck(4)), run_time=rt)
        until(self, "just doing stuff", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(rp, color=None, scale_factor=1.08), run_time=rt)
        done(self)


# ══════════════ B07: the real case — tests special-cased and edited ══════════════
AG7 = (-5.2, 0.9)
AGS7 = 0.85


def l_anthropic():
    return lbl("per Anthropic, 2025", (-3.3, 2.8), 40)


def l_edited():
    return lbl("test edited", (0.7, 2.25))


def card2_lines():
    i = m_rig()
    z = MH + 0.06
    return VGroup(*[Line(i.p(0.55, MD * f, z), i.p(MW - 0.55 - (0.6 if k == 0 else 0.1), MD * f, z), color=BAR1, stroke_width=6)
                    for k, f in enumerate((0.62, 0.42))]).set_z_index(3)


def b07_state():
    back, front = fail_bin()
    return VGroup(belt(), machine(), lamp(), card(), card2_lines(), back, crate(R_X - 0.25, FAIL_Y - 0.45, 0.9, True).set_z_index(1), front,
                  fail_cross(), agent(AG7, AGS7), l_anthropic(), l_edited(), result_crate(PASS_Y, True), result_check(PASS_Y))


class B07_SpecialCase(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        bl, mc, lp, cd, cl, sl = belt(), machine(), lamp(), card(), card_lines(), seal()
        back, front = fail_bin()
        ag = agent(AG7, AGS7)
        self.play(FadeIn(VGroup(bl, mc, lp, cd, cl, sl, back, front), shift=UP * 0.3), FadeIn(ag, shift=RIGHT * 0.3), run_time=0.7)
        until(self, "Anthropic's system card", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_anthropic()), run_time=rt)
        until(self, "after repeated failures", lead=0.3)
        feed(self, True, 0.8)
        bc = crate(R_X - 0.25, FAIL_Y - 0.45, 0.9, True).set_z_index(1)
        bc.shift(UP * 0.8)
        self.add(bc)
        self.bring_to_front(front)
        rt = guard(self, 0.35)
        self.play(bc.animate.shift(DOWN * 0.8), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.3)
        self.play(Create(fail_cross()), run_time=rt)
        until(self, "edited the tests", lead=0.5)
        old = VGroup(cd, cl, sl)
        rt = guard(self, 0.5)
        self.play(old.animate.shift(UP * 1.2 + LEFT * 1.6).set_opacity(0), run_time=rt)
        self.remove(old)
        new = VGroup(card(), card2_lines())
        new.shift(UP * 1.2 + LEFT * 1.6)
        self.add(new)
        rt = guard(self, 0.5)
        self.play(new.animate.shift(DOWN * 1.2 + RIGHT * 1.6), FadeIn(l_edited()), run_time=rt)
        until(self, "The tests passed", lead=0.5)
        feed(self, True, 0.7)
        on, rc = lamp(True), result_crate(PASS_Y, True)
        rt = guard(self, 0.3)
        self.play(FadeIn(on), FadeIn(rc, shift=RIGHT * 0.4), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Create(result_check(PASS_Y)), FadeOut(on), run_time=rt)
        until(self, "never got written", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(rc, color=None, scale_factor=1.15), run_time=rt)
        done(self)


# ══════════════ B08: write the fail condition first, check from outside ══════════════
CD8 = (-4.3, 1.3)
SLOT_Y = 1.55
SLOT_X = [2.3, 4.5]
AG8 = (-4.4, -1.55)
AGS8 = 0.9
WK_X = [-1.3, -0.4, 0.5]
CHK8 = (5.35, -2.0)


def card8():
    i = rig_at(CD8[0], CD8[1], 1.15, 1.7, 1.3)
    slab = i.box(0, 0, 0, 1.7, 1.3, 0.08, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    lines = VGroup(*[Line(i.p(0.3, 1.3 * f, 0.08), i.p(1.4 - (0.3 if k == 1 else 0.0), 1.3 * f, 0.08), color=BAR1, stroke_width=6)
                     for k, f in enumerate((0.65, 0.4))])
    sl = Dot(i.p(1.35, 0.25, 0.08), radius=0.11, color=TERRA)
    return VGroup(slab, lines, sl).set_z_index(2)


def l_first8():
    return lbl("written first", (CD8[0], 2.65))


def slots():
    return VGroup(*[tile(x, SLOT_Y, 1.0) for x in SLOT_X])


def slot_lbls():
    return VGroup(*[T(n, 42).move_to([x, SLOT_Y - 0.95, 0]) for x, n in zip(SLOT_X, ("pass", "fail"))])


def verdict():
    return check(SLOT_X[0], SLOT_Y + 1.0, 0.28)


def work_blocks():
    return VGroup(*[blk(x, 0, 0.62) for x in WK_X])


def checker():
    i = rig_at(CHK8[0], CHK8[1], 1.0, 0.8, 0.8)
    body = i.box(0, 0, 0, 0.8, 0.8, 1.4)
    eye = Circle(radius=0.14, fill_color=TERRA, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(i.p(0.4, 0, 1.05))
    return VGroup(body, eye)


def l_outside():
    return lbl("outside", (CHK8[0] - 1.3, -3.0))


class B08_Outside(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        until(self, "before anything runs", lead=0.3)
        cd = card8()
        rt = guard(self, 0.5)
        self.play(FadeIn(cd, shift=DOWN * 0.5), FadeIn(l_first8()), run_time=rt, rate_func=ease_in)
        until(self, "count as failure", lead=0.4)
        sl, sll = slots(), slot_lbls()
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[FadeIn(x, shift=DOWN * 0.3) for x in sl], lag_ratio=0.4), FadeIn(sll), run_time=rt)
        until(self, "check it from outside", lead=0.4)
        ag, wb = agent(AG8, AGS8), work_blocks()
        rt = guard(self, 0.5)
        self.play(FadeIn(ag, shift=RIGHT * 0.3), run_time=rt)
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[FadeIn(b_, shift=DOWN * 0.5) for b_ in wb], lag_ratio=0.4), run_time=rt, rate_func=ease_in)
        ck8 = checker()
        rt = guard(self, 0.4)
        self.play(FadeIn(ck8, shift=LEFT * 0.3), FadeIn(l_outside()), run_time=rt)
        until(self, "not in its own report", lead=0.2)
        sc = Line([4.6, -2.6, 0], [4.6, -0.6, 0], color=TERRA, stroke_width=8).set_z_index(4)
        self.add(sc)
        rt = guard(self, 0.9)
        self.play(sc.animate.move_to([-1.8, -1.6, 0]), run_time=rt, rate_func=linear)
        self.remove(sc)
        rt = guard(self, 0.3)
        self.play(Create(verdict()), run_time=rt)
        until(self, "so they could be wrong", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(sl[1], color=None, scale_factor=1.2), run_time=rt)
        until(self, "no matter what", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(cd, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Criterion, B01_FitsAll, B02_Eclipse, B03_AlwaysPasses, B04_FailCondition, B05_Robust, B06_SelfGrader,
             B07_SpecialCase, B08_Outside):
    _cls.play = ST.play
