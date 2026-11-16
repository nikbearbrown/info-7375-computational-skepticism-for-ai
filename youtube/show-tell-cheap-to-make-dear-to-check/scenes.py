"""
Manim scenes for show-tell-cheap-to-make-dear-to-check (show-tell skill; INFO 7375 course film, ordered by Bear on
2026-09-27 in SHOW-TELL-SOLVE-VERIFY.md: the solve-verify asymmetry from chapter 1).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py. The kit, pacing
helpers and midpoint guard are copied from the sibling course film show-tell-a-test-that-cant-fail
(itself from show-tell-induction-until-it-changes), with its larger end slack (_END = 0.15) for 24 fps frame rounding.

Cheap to make, dear to check. The COST METER, two grey bars ('solve' and 'verify') growing from an ink axis, is the
one object every beat shares. The folklore: a kraft NUMBER crate; the solve bar creeps long and two FACTOR tiles emerge;
multiplying back, the verify bar is a stub and a check lands. The dark MODEL block and its white OUTPUT slip: solve is a
sliver. The PATIENT peg on a chair, the CLINICIAN peg, a CLOCK filling: verify grows long. The agent's REPORT slip, the
SERVER stack (the system of record), a QUERY line and the RECORD page to compare: verify long again. Side by side, a
'proof' meter and a 'model' meter, flipped, labelled illustrative; the model's pair repeats along a time arrow. The model
streams slips into a GRID; a short BUDGET bar; two get a terracotta dot; every slip carries a check. One slip lifts and
turns over: a cross underneath. A CHECKER block of the same shape drops onto the model and gets a meter of the same
shape. The HUMAN peg's one check swings from the report (a cross) to the server (lights, a check); verify is short.
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



# ═════════════════════════════ the film: cheap to make, dear to check ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
AG_TOP, AG_L, AG_R = "#2E2A26", "#1B1815", "#141210"   # the model block (darker than DARK_*, so it never fuses with ink)


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


# ─── the COST METER: two grey bars, 'solve' and 'verify', growing from an ink axis ───
BH = 0.62         # bar height
ROW = 0.5         # rows sit at cy ± ROW


def m_axis(x0, cy, s=1.0):
    return Line([x0, cy - 1.05 * s, 0], [x0, cy + 1.05 * s, 0], color=INK, stroke_width=6)


def m_bar(x0, cy, which, L, s=1.0):
    """which: 'solve' (top row) or 'verify' (bottom row). Grows from the axis to the right."""
    y = cy + (ROW if which == "solve" else -ROW) * s
    return Rectangle(width=L, height=BH * s, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([x0 + L / 2, y, 0])


def m_labels(x0, cy, size=44):
    return VGroup(T("solve", size).move_to([x0 - 0.9, cy + ROW, 0]),
                  T("verify", size).move_to([x0 - 1.0, cy - ROW, 0]))


def m_check(x0, cy, L):
    return check(x0 + L + 0.5, cy - ROW + 0.05, 0.26)


# ─── the MODEL (dark block) and its OUTPUT slip (a white page, no spark) ───
def model(c, s=1.0, tones=(AG_TOP, AG_L, AG_R)):
    i = rig_at(c[0], c[1], s, 1.5, 1.5)
    body = i.box(0, 0, 0, 1.5, 1.5, 0.95, *tones)
    ports = VGroup(*[i.box(1.5 * f, -0.16, 0.3, 0.24, 0.16, 0.32, GHOST, BOX_IN1, BOX_IN2, sw=1) for f in (0.2, 0.6)])
    return VGroup(body, ports)


SW, SD = 1.0, 1.3       # slip footprint


def slip(c, s=1.0):
    i = rig_at(c[0], c[1], s, SW, SD)
    slab = i.box(0, 0, 0, SW, SD, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=2.5)
    zt = 0.06
    lines = VGroup(*[Line(i.p(0.18, SD * f, zt), i.p(SW - 0.18 - (0.3 if k == 2 else 0.0), SD * f, zt), color=BAR2, stroke_width=4)
                     for k, f in enumerate((0.3, 0.5, 0.7))])
    return VGroup(slab, lines)


def slip_top(c, s=1.0):
    """Screen point above the slip's face, where a check or a dot sits."""
    return (c[0], c[1] + 0.12 * s)


# ─── HUMAN pegs, a chair, a clock ───
def peg(x, y, s=1.0, badge=False):
    body = RoundedRectangle(width=0.62 * s, height=0.95 * s, corner_radius=0.2 * s, fill_color=BOX_L, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    head = Circle(radius=0.27 * s, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4) \
        .move_to([x, y + 0.475 * s + 0.27 * s + 0.06, 0])
    g = VGroup(body, head)
    if badge:
        g.add(Dot([x, y + 0.2 * s, 0], radius=0.09, color=TERRA))
    return g


def chair(x, y):
    i = rig_at(x, y, 1.0, 0.9, 0.9)
    return i.box(0, 0, 0, 0.9, 0.9, 0.5)


CLR = 0.95


def clock_face(c):
    return Circle(radius=CLR, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to(P3(c))


def clock_wedges(c, n=8):
    """n pie wedges (polygons along the arc), clockwise from twelve, DIM grey."""
    out = []
    for k in range(n):
        a0, a1 = PI / 2 - 2 * PI * k / n, PI / 2 - 2 * PI * (k + 1) / n
        pts = [P3(c)] + [P3((c[0] + (CLR - 0.09) * np.cos(a), c[1] + (CLR - 0.09) * np.sin(a)))
                         for a in np.linspace(a0, a1, 8)]
        out.append(Polygon(*pts, fill_color=DIM, fill_opacity=1, stroke_width=0))
    return VGroup(*out)


# ─── the SERVER (system of record) ───
SVS = 1.15


def server_at(c, s=SVS):
    i = rig_at(c[0], c[1], s, 1.4, 1.4)
    return i.server(0, 0, 0)          # (stack, lights)


def server_on(c, s=SVS):
    i = rig_at(c[0], c[1], s, 1.4, 1.4)
    return VGroup(*[Dot(i.p(0.25, 0, k * 0.46 + 0.21), radius=0.07, color=TERRA) for k in range(3)]).set_z_index(3)


# ══════════════ B00: the folklore — factor hard, multiply easy ══════════════
CR0 = (-4.2, -0.6)
M0 = (0.4, 1.5)          # meter axis x0, cy
SOLVE0, VER0 = 3.6, 0.45
FT = [(1.6, -1.5), (3.5, -1.5)]
FT_SHIFT = 0.5


def crate():
    i = rig_at(CR0[0], CR0[1], 1.55, 1.4, 1.4)
    return VGroup(i.box(0, 0, 0, 1.4, 1.4, 1.1), i.tape(0, 0, 1.1, 1.4, 1.4))


def factor_tile(c):
    i = rig_at(c[0], c[1], 1.25, 0.8, 0.8)
    return i.box(0, 0, 0, 0.8, 0.8, 0.8)


def l_bignum():
    return lbl("big number", (CR0[0], -2.85))


def l_factors():
    return lbl("factors", (2.55 - FT_SHIFT, -2.85))


def b00_state():
    return VGroup(crate(), l_bignum(), m_axis(*M0), m_labels(*M0), m_bar(M0[0], M0[1], "solve", SOLVE0),
                  VGroup(*[factor_tile((x - FT_SHIFT, y)) for x, y in FT]), l_factors(),
                  m_bar(M0[0], M0[1], "verify", VER0), m_check(M0[0], M0[1], VER0))


class B00_Folklore(Scene):
    def construct(self):
        cr = crate()
        self.play(FadeIn(cr, shift=UP * 0.4), run_time=0.6)
        until(self, "very large number", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_bignum()), FadeIn(m_axis(*M0)), FadeIn(m_labels(*M0)), run_time=rt)
        until(self, "ask for its factors", lead=0.2)
        sb = m_bar(M0[0], M0[1], "solve", SOLVE0)
        rt = guard(self, 2.2)
        self.play(GrowFromEdge(sb, LEFT), run_time=rt, rate_func=linear)
        tl = VGroup(*[factor_tile(c) for c in FT])
        rt = guard(self, 0.5)
        self.play(FadeIn(tl, shift=DOWN * 0.4), FadeIn(l_factors()), run_time=rt, rate_func=ease_in)
        until(self, "ask them to multiply", lead=0.2)
        vb = m_bar(M0[0], M0[1], "verify", VER0)
        rt = guard(self, 0.4)
        self.play(tl.animate.shift(LEFT * FT_SHIFT), GrowFromEdge(vb, LEFT), run_time=rt)
        ck = m_check(M0[0], M0[1], VER0)
        rt = guard(self, 0.3)
        self.play(Create(ck), run_time=rt)
        until(self, "Solving is dear", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(sb, color=None, scale_factor=1.06), run_time=rt)
        until(self, "Verifying is cheap", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(vb, ck), color=None, scale_factor=1.15), run_time=rt)
        done(self)


# ══════════════ B01: the model — the asymmetry inverts ══════════════
MD1 = (-3.8, -1.0)
MDS1 = 1.5
SL1 = (-0.3, -1.6)
M1 = (1.4, 1.5)
SLIVER = 0.28


def l_model1():
    return lbl("model", (MD1[0], -2.9))


def l_output():
    return lbl("output", (SL1[0], -2.75))


def b01_state():
    return VGroup(model(MD1, MDS1), l_model1(), slip(SL1), l_output(), m_axis(*M1), m_labels(*M1),
                  m_bar(M1[0], M1[1], "solve", SLIVER))


class B01_Inverts(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        md = model(MD1, MDS1)
        rt = guard(self, 0.6)
        self.play(FadeIn(md, shift=UP * 0.3), FadeIn(l_model1()), run_time=rt)
        until(self, "The asymmetry inverts", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(m_axis(*M1)), FadeIn(m_labels(*M1)), run_time=rt)
        until(self, "the result appears", lead=0.2)
        sl = slip(SL1)
        rt = guard(self, 0.3)
        self.play(FadeIn(sl, shift=DOWN * 0.5), FadeIn(l_output()), run_time=rt, rate_func=ease_in)
        until(self, "milliseconds", lead=0.2)
        sb = m_bar(M1[0], M1[1], "solve", SLIVER)
        rt = guard(self, 0.25)
        self.play(GrowFromEdge(sb, LEFT), run_time=rt)
        until(self, "barely moves", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(sb, color=None, scale_factor=1.3), run_time=rt)
        done(self)


# ══════════════ B02: the clinician — verifying is expensive ══════════════
CH2 = (-5.0, -1.6)
SL2 = (-2.9, -1.9)
CL2 = (-1.2, -1.1)
CK2 = (-3.6, 1.7)
VER2 = 3.6


def l_patient():
    return lbl("patient", (CH2[0], -2.95))


def l_clinician():
    return lbl("clinician", (CL2[0], -2.95))


def b02_state():
    return VGroup(m_axis(*M1), m_labels(*M1), m_bar(M1[0], M1[1], "solve", SLIVER), chair(*CH2), peg(CH2[0], CH2[1] + 1.05, 1.0),
                  l_patient(), slip(SL2), peg(CL2[0], CL2[1], 1.15, badge=True), l_clinician(), clock_face(CK2), clock_wedges(CK2),
                  m_bar(M1[0], M1[1], "verify", VER2), m_check(M1[0], M1[1], VER2))


class B02_Clinician(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[0], st[1], st[2], st[3])), run_time=0.45)
        until(self, "triage score", lead=0.5)
        ch, pt = chair(*CH2), peg(CH2[0], CH2[1] + 1.05, 1.0)
        rt = guard(self, 0.5)
        self.play(FadeIn(VGroup(ch, pt), shift=UP * 0.3), FadeIn(l_patient()), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(slip(SL2), shift=DOWN * 0.4), run_time=rt, rate_func=ease_in)
        until(self, "you need a clinician", lead=0.2)
        cl = peg(CL2[0] - 3.0, CL2[1], 1.15, badge=True)
        rt = guard(self, 0.7)
        self.play(cl.animate.shift(RIGHT * 3.0), FadeIn(l_clinician()), run_time=rt)
        until(self, "twenty minutes", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(clock_face(CK2)), run_time=rt)
        wd, vb = clock_wedges(CK2), m_bar(M1[0], M1[1], "verify", VER2)
        rt = guard(self, 2.6)
        self.play(LaggedStart(*[FadeIn(w) for w in wd], lag_ratio=0.12), GrowFromEdge(vb, LEFT), run_time=rt, rate_func=linear)
        until(self, "keeps growing", lead=0.1)
        rt = guard(self, 0.3)
        self.play(Create(m_check(M1[0], M1[1], VER2)), run_time=rt)
        done(self)


# ══════════════ B03: the agent's report — check the system of record ══════════════
MD3 = (-4.5, -1.2)
MDS3 = 1.2
SL3 = (-2.2, -2.0)
PG3 = (-0.8, 0.55)
SV3 = (3.0, -1.7)
RC3 = (0.2, -2.0)
M3 = (1.6, 2.1)
VER3 = 3.4
Q_A, Q_B = (-0.45, 0.3), (1.3, 0.02)


def l_report():
    return lbl("report", (SL3[0], -3.0))


def l_sor(c=SV3):
    return lbl("system of record", (c[0], -3.05), 40)


def l_compare():
    return lbl("compare", (-1.0, -0.75))


def query():
    return Line(P3(Q_A), P3(Q_B), color=BAR1, stroke_width=7)


def b03_state():
    stack, lights = server_at(SV3)
    return VGroup(model(MD3, MDS3), slip(SL3), l_report(), peg(PG3[0], PG3[1], 1.15), stack, lights, l_sor(), m_axis(*M3), m_labels(*M3),
                  query(), server_on(SV3), slip(RC3), l_compare(), m_bar(M3[0], M3[1], "solve", SLIVER), m_bar(M3[0], M3[1], "verify", VER3))


class B03_Report(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        md, sl = model(MD3, MDS3), slip(SL3)
        rt = guard(self, 0.6)
        self.play(FadeIn(md, shift=UP * 0.3), FadeIn(sl, shift=RIGHT * 0.4), FadeIn(l_report()), run_time=rt)
        until(self, "To verify it", lead=0.2)
        stack, lights = server_at(SV3)
        pg = peg(PG3[0], PG3[1], 1.15)
        rt = guard(self, 0.6)
        self.play(FadeIn(VGroup(stack, lights), shift=UP * 0.3), FadeIn(l_sor()), FadeIn(pg, shift=DOWN * 0.3),
                  FadeIn(m_axis(*M3)), FadeIn(m_labels(*M3)), run_time=rt)
        until(self, "query the provider", lead=0.2)
        q = query()
        rt = guard(self, 0.7)
        self.play(Create(q), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(server_on(SV3), scale=1.5), run_time=rt)
        until(self, "examine the actual", lead=0.2)
        rc = slip(RC3)
        rt = guard(self, 0.6)
        self.play(FadeIn(rc, shift=LEFT * 0.8), run_time=rt)
        until(self, "compare it", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(l_compare()), Indicate(VGroup(sl, rc), color=None, scale_factor=1.08), run_time=rt)
        until(self, "fraction of a cent", lead=0.3)
        rt = guard(self, 0.25)
        self.play(GrowFromEdge(m_bar(M3[0], M3[1], "solve", SLIVER), LEFT), run_time=rt)
        until(self, "an hour of senior labor", lead=0.4)
        rt = guard(self, 1.4)
        self.play(GrowFromEdge(m_bar(M3[0], M3[1], "verify", VER3), LEFT), run_time=rt, rate_func=linear)
        done(self)


# ══════════════ B04: where the costs sit — and will sit ══════════════
MP = (-4.5, 1.4)      # the proof meter
MM = (1.6, 1.4)       # the model meter
PS, PV = 3.4, 0.45
MS, MV = 0.28, 3.4
AR_Y = -1.15
MINI = [(1.5, -0.05), (3.6, -0.05)]
MINI_S = 0.45


def l_proof():
    return lbl("proof", (-2.6, 2.95))


def l_model4():
    return lbl("model", (3.4, 2.95))


def l_illus():
    return lbl("illustrative", (-3.0, -1.5), 44)


def arrow4():
    return Arrow([0.9, AR_Y, 0], [5.9, AR_Y, 0], color=INK, stroke_width=6, buff=0, max_tip_length_to_length_ratio=0.06)


def mini(k):
    x0, cy = MINI[k]
    return VGroup(m_axis(x0, cy, MINI_S), m_bar(x0, cy, "solve", MS * MINI_S, MINI_S), m_bar(x0, cy, "verify", MV * MINI_S, MINI_S))


def b04_state():
    return VGroup(m_axis(*MP), m_labels(*MP), m_bar(MP[0], MP[1], "solve", PS), m_bar(MP[0], MP[1], "verify", PV), l_proof(),
                  m_axis(*MM), m_labels(*MM), m_bar(MM[0], MM[1], "solve", MS), m_bar(MM[0], MM[1], "verify", MV), l_model4(),
                  arrow4(), mini(0), mini(1), l_illus())


class B04_WhereCostsSit(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        until(self, "where the costs sit", lead=0.4)
        ps, pv = m_bar(MP[0], MP[1], "solve", PS), m_bar(MP[0], MP[1], "verify", PV)
        rt = guard(self, 0.5)
        self.play(FadeIn(m_axis(*MP)), FadeIn(m_labels(*MP)), FadeIn(l_proof()), run_time=rt)
        rt = guard(self, 0.6)
        self.play(GrowFromEdge(ps, LEFT), GrowFromEdge(pv, LEFT), run_time=rt)
        ms, mv = m_bar(MM[0], MM[1], "solve", MS), m_bar(MM[0], MM[1], "verify", MV)
        rt = guard(self, 0.5)
        self.play(FadeIn(m_axis(*MM)), FadeIn(m_labels(*MM)), FadeIn(l_model4()), run_time=rt)
        rt = guard(self, 0.6)
        self.play(GrowFromEdge(ms, LEFT), GrowFromEdge(mv, LEFT), run_time=rt)
        until(self, "keep sitting", lead=0.2)
        rt = guard(self, 0.6)
        self.play(GrowArrow(arrow4()), run_time=rt)
        rt = guard(self, 0.7)
        self.play(LaggedStart(FadeIn(mini(0), shift=UP * 0.2), FadeIn(mini(1), shift=UP * 0.2), lag_ratio=0.5), run_time=rt)
        until(self, "the short bar", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(pv, color=None, scale_factor=1.2), run_time=rt)
        until(self, "the long one", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(mv, color=None, scale_factor=1.06), run_time=rt)
        until(self, "kinds of work", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_illus()), run_time=rt)
        done(self)


# ══════════════ B05: outputs at scale, verification not ══════════════
MD5 = (-4.7, 0.6)
MDS5 = 1.1
GX = [-2.3, -0.55, 1.2, 2.95]
GY = [1.9, 0.35, -1.2]
GS = 0.72
BG_X, BG_Y, BG_L = -5.6, -2.15, 0.7
PG5 = (-3.7, -1.7)
VERIFIED = [(0, 2), (1, 2)]


def gpos(i, j):
    return (GX[i], GY[j])


def grid_slips():
    return VGroup(*[slip(gpos(i, j), GS) for j in range(3) for i in range(4)])


def grid_checks():
    return VGroup(*[check(gpos(i, j)[0], slip_top(gpos(i, j), GS)[1] + 0.05, 0.2, w=6) for j in range(3) for i in range(4)])


def verified_dots():
    return VGroup(*[Dot([gpos(i, j)[0] - 0.42, gpos(i, j)[1] + 0.02, 0], radius=0.11, color=TERRA).set_z_index(3) for i, j in VERIFIED])


def budget_axis():
    return Line([BG_X, BG_Y - 0.5, 0], [BG_X, BG_Y + 0.5, 0], color=INK, stroke_width=6)


def budget_bar():
    return Rectangle(width=BG_L, height=BH, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([BG_X + BG_L / 2, BG_Y, 0])


def l_budget():
    return lbl("budget", (BG_X + 0.55, -3.0))


def l_looks():
    return lbl("looks right", (5.0, GY[0]))


def b05_state():
    return VGroup(model(MD5, MDS5), grid_slips(), budget_axis(), budget_bar(), l_budget(), peg(PG5[0], PG5[1]),
                  verified_dots(), grid_checks(), l_looks())


class B05_AtScale(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        md = model(MD5, MDS5)
        rt = guard(self, 0.5)
        self.play(FadeIn(md, shift=UP * 0.3), run_time=rt)
        until(self, "outputs at scale", lead=0.6)
        gs = grid_slips()
        rt = guard(self, 2.2)
        self.play(LaggedStart(*[FadeIn(s_, shift=RIGHT * 1.2) for s_ in gs], lag_ratio=0.1), run_time=rt)
        until(self, "does not happen at scale", lead=0.3)
        pg = peg(PG5[0], PG5[1])
        rt = guard(self, 0.5)
        self.play(FadeIn(budget_axis()), FadeIn(l_budget()), FadeIn(pg, shift=UP * 0.3), run_time=rt)
        rt = guard(self, 0.3)
        self.play(GrowFromEdge(budget_bar(), LEFT), run_time=rt)
        until(self, "checks a few", lead=0.2)
        vd = verified_dots()
        rt = guard(self, 0.5)
        self.play(LaggedStart(*[FadeIn(d, scale=1.6) for d in vd], lag_ratio=0.4), run_time=rt)
        until(self, "looks like a success", lead=0.5)
        gc = grid_checks()
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[Create(c_) for c_ in gc], lag_ratio=0.08), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_looks()), run_time=rt)
        done(self)


# ══════════════ B06: the one that is wrong looked the same ══════════════
ONE = (3, 2)
ONE_TO = (5.1, -1.2)


def l_wrong():
    return lbl("wrong", (ONE_TO[0], -2.6))


class B06_TheOne(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        gs, gc = st[1], st[7]
        k = ONE[1] * 4 + ONE[0]
        one, ck = gs[k], gc[k]
        until(self, "Until one of them", lead=0.2)
        dx = ONE_TO[0] - GX[ONE[0]]
        rt = guard(self, 0.7)
        self.play(VGroup(one, ck).animate.shift(RIGHT * dx), run_time=rt)
        rt = guard(self, 0.4)
        self.play(VGroup(one, ck).animate.shift(UP * 0.35), run_time=rt, rate_func=ease_in)
        until(self, "Under the check", lead=0.2)
        rt = guard(self, 0.35)
        self.play(FadeOut(ck), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Create(cross(ONE_TO[0], ONE_TO[1] + 0.45, 0.24)), FadeIn(l_wrong()), run_time=rt)
        until(self, "the whole time", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(one, color=None, scale_factor=1.1), run_time=rt)
        done(self)


def b06_state():
    st = b05_state()
    k = ONE[1] * 4 + ONE[0]
    st[1][k].shift(RIGHT * (ONE_TO[0] - GX[ONE[0]]) + UP * 0.35)
    st[7].remove(st[7][k])
    return VGroup(st, cross(ONE_TO[0], ONE_TO[1] + 0.45, 0.24), l_wrong())


# ══════════════ B07: the wrong fix — a checker of the same shape ══════════════
MD7 = (-1.9, -2.0)
MDS7 = 1.3
CK7 = (-1.9, MD7[1] + 0.95 * MDS7)
VS7 = (0.0, 2.5)
M7A = (2.4, -1.6)
M7B = (2.4, 1.3)
VER7 = 3.4


def l_model7():
    return lbl("model", (-4.7, -1.6))


def l_checker():
    return lbl("checker", (-4.7, 0.3))


def l_same():
    return lbl("same shape", (4.2, 2.85))


def b07_state():
    return VGroup(model(MD7, MDS7), l_model7(), m_axis(*M7A), m_labels(*M7A), m_bar(M7A[0], M7A[1], "solve", SLIVER),
                  m_bar(M7A[0], M7A[1], "verify", VER7), model(CK7, MDS7, (DARK_TOP, DARK_L, DARK_R)), l_checker(), slip(VS7, 0.9),
                  m_axis(*M7B), m_labels(*M7B), m_bar(M7B[0], M7B[1], "solve", SLIVER), m_bar(M7B[0], M7B[1], "verify", VER7), l_same())


class B07_Checker(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        md = model(MD7, MDS7)
        rt = guard(self, 0.6)
        self.play(FadeIn(md, shift=UP * 0.3), FadeIn(l_model7()), FadeIn(m_axis(*M7A)), FadeIn(m_labels(*M7A)), run_time=rt)
        va = m_bar(M7A[0], M7A[1], "verify", VER7)
        rt = guard(self, 0.5)
        self.play(GrowFromEdge(m_bar(M7A[0], M7A[1], "solve", SLIVER), LEFT), GrowFromEdge(va, LEFT), run_time=rt)
        until(self, "the wrong fix", lead=0.2)
        ck = model(CK7, MDS7, (DARK_TOP, DARK_L, DARK_R))
        rt = guard(self, 0.6)
        self.play(FadeIn(ck, shift=DOWN * 0.8), FadeIn(l_checker()), run_time=rt, rate_func=ease_in)
        until(self, "one layer up", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(slip(VS7, 0.9), shift=DOWN * 0.4), run_time=rt, rate_func=ease_in)
        until(self, "cheap to produce", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(m_axis(*M7B)), FadeIn(m_labels(*M7B)), run_time=rt)
        rt = guard(self, 0.25)
        self.play(GrowFromEdge(m_bar(M7B[0], M7B[1], "solve", SLIVER), LEFT), run_time=rt)
        until(self, "expensive to verify", lead=0.3)
        vb = m_bar(M7B[0], M7B[1], "verify", VER7)
        rt = guard(self, 1.0)
        self.play(GrowFromEdge(vb, LEFT), run_time=rt, rate_func=linear)
        until(self, "Same shape", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(l_same()), Indicate(VGroup(va, vb), color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B08: the right fix — one human check at the system of record ══════════════
MD8 = (-4.6, -1.4)
MDS8 = 1.1
SL8 = (-2.3, -2.05)
PG8 = (-1.0, 0.5)
SV8 = (3.0, -1.7)
M8 = (1.6, 2.3)
VER8 = 1.0
L1_A, L1_B = (-1.25, 0.05), (-1.9, -1.1)
L2_A, L2_B = (-0.65, 0.35), (1.3, 0.02)
CK8 = (5.2, 0.25)


def l_notreport():
    return lbl("not the report", (SL8[0], -3.05), 40)


def l_onecheck():
    return lbl("one check", (5.2, 1.05), 40)


def line1():
    return Line(P3(L1_A), P3(L1_B), color=BAR1, stroke_width=7)


def line2():
    return Line(P3(L2_A), P3(L2_B), color=BAR1, stroke_width=7)


class B08_OneCheck(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        md, sl, pg = model(MD8, MDS8), slip(SL8), peg(PG8[0], PG8[1], 1.15)
        stack, lights = server_at(SV8)
        rt = guard(self, 0.6)
        self.play(FadeIn(md, shift=UP * 0.3), FadeIn(sl, shift=RIGHT * 0.3), FadeIn(pg, shift=DOWN * 0.3),
                  FadeIn(VGroup(stack, lights), shift=UP * 0.3), FadeIn(l_sor(SV8)), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(m_axis(*M8)), FadeIn(m_labels(*M8)), GrowFromEdge(m_bar(M8[0], M8[1], "solve", SLIVER), LEFT), run_time=rt)
        until(self, "One human check", lead=0.2)
        l1, cx = line1(), cross(SL8[0], SL8[1] + 0.1, 0.28)
        rt = guard(self, 0.5)
        self.play(Create(l1), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Create(cx), run_time=rt)
        until(self, "at the system of record", lead=0.2)
        l2 = line2()
        rt = guard(self, 0.4)
        self.play(FadeOut(l1), FadeOut(cx), run_time=rt)
        rt = guard(self, 0.6)
        self.play(Create(l2), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(server_on(SV8), scale=1.5), Create(check(CK8[0], CK8[1], 0.3)), FadeIn(l_onecheck()), run_time=rt)
        until(self, "not at the report", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_notreport()), run_time=rt)
        until(self, "cheap enough to scale", lead=0.3)
        vb = m_bar(M8[0], M8[1], "verify", VER8)
        rt = guard(self, 0.4)
        self.play(GrowFromEdge(vb, LEFT), run_time=rt)
        rt = guard(self, 0.5)
        self.play(Indicate(vb, color=None, scale_factor=1.15), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Folklore, B01_Inverts, B02_Clinician, B03_Report, B04_WhereCostsSit, B05_AtScale, B06_TheOne,
             B07_Checker, B08_OneCheck):
    _cls.play = ST.play
