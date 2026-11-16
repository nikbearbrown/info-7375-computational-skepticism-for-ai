"""
Manim scenes for show-tell-five-things-the-model-cant-do (show-tell skill; INFO 7375 course film, ordered by Bear on
2026-09-27 in SHOW-TELL-FIVE-CAPACITIES.md: the Five Supervisory Capacities from chapter 1).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py. The kit, pacing
helpers and midpoint guard are copied from the sibling course film show-tell-cheap-to-make-dear-to-check
(itself from show-tell-a-test-that-cant-fail), with its larger end slack (_END = 0.15) for 24 fps frame rounding.

Five things the model can't do for itself. One cast, whole film: the dark MODEL block and its white OUTPUT slip; the
SUPERVISOR peg (terracotta badge) standing between the model and the world; the WORLD, drawn as the PATIENT peg on a kraft
chair; five kraft TILES that rise over the supervisor in the opening and come back as five PLINTHS in the close. Each
capacity is the supervisor doing one distinct thing with those objects: the twitch (a low-score slip stops at the
supervisor, a PRIOR stack of pages behind him, a question mark); training data versus the world (a crate by the model,
a line to the patient, then the slip sailing straight through with a check); two question slips, one into the model and
answered, one stopped short and never asked; four plinths and a cursor that lands on the empty one, no tool yet; a cross
on the path that the supervisor draws, then the AI block sliding in by itself when nobody draws it; one hero number, 5%,
sent to a spam crate (check) and to the patient (cross); three sources whose slips converge on the supervisor's plinth
and become one sealed decision; the same three with no plinth, a pile with no owner that slides back apart; and the five
plinths with a peg on four of them, a gap over the fifth, and the patient beneath the gap.
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



# ═════════════════════════════ the film: five things the model can't do for itself ═════════════════════════════
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
    """Screen point above the slip's face, where a check, a cross or a seal sits."""
    return (c[0], c[1] + 0.12 * s)


# ─── HUMAN pegs, a chair, kraft crates, tiles and plinths ───
def peg(x, y, s=1.0, badge=False):
    body = RoundedRectangle(width=0.62 * s, height=0.95 * s, corner_radius=0.2 * s, fill_color=BOX_L, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    head = Circle(radius=0.27 * s, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4) \
        .move_to([x, y + 0.475 * s + 0.27 * s + 0.06, 0])
    g = VGroup(body, head)
    if badge:
        g.add(Dot([x, y + 0.2 * s, 0], radius=0.09 * s, color=TERRA))
    return g


def chair(x, y, s=1.15):
    i = rig_at(x, y, s, 0.9, 0.9)
    return i.box(0, 0, 0, 0.9, 0.9, 0.5)


def crate(c, s=1.3):
    i = rig_at(c[0], c[1], s, 1.4, 1.4)
    return VGroup(i.box(0, 0, 0, 1.4, 1.4, 1.1), i.tape(0, 0, 1.1, 1.4, 1.4))


def tile(c, s=0.7):
    """A small kraft tile (one capacity); the same box, larger, is a plinth."""
    i = rig_at(c[0], c[1], s, 1.2, 1.2)
    return i.box(0, 0, 0, 1.2, 1.2, 0.45)


PLH = 0.45     # plinth height (box units)


def plinth_top(c, s):
    """Screen point of the plinth's top-face centre: where an object on it is centred."""
    return (c[0], c[1] + PLH * s)


# ─── the cast's home positions (B00, B01, B02, B06 share them) ───
ML = (-4.1, -1.2)       # model
MLS = 1.35
SP = (0.0, -1.3)        # supervisor
SPS = 1.35
PC = (4.3, -1.75)       # patient's chair; the patient peg sits on it
PT = (PC[0], PC[1] + 1.2)
SLS = 1.1               # slip scale in the home layout
SL_A = (-2.6, -1.95)    # slip: just out of the model
SL_B = (-1.7, -2.2)     # slip: at the supervisor's feet


def patient(dot=False):
    g = VGroup(chair(*PC), peg(PT[0], PT[1], 1.1))
    if dot:
        g.add(Dot([PT[0] - 0.1, PT[1] - 0.3, 0], radius=0.11, color=TERRA).set_z_index(3))
    return g


def supervisor(c=SP, s=SPS):
    return peg(c[0], c[1], s, badge=True)


TX = [-3.5, -1.75, 0.0, 1.75, 3.5]
TY = 1.55
TS = 0.7


def tiles():
    return VGroup(*[tile((x, TY), TS) for x in TX])


def numerals(xs, y, size=40):
    return VGroup(*[T(str(k + 1), size).move_to([x, y, 0]) for k, x in enumerate(xs)])


def l_model():
    return lbl("model", (ML[0], -3.05))


def l_super():
    return lbl("supervisor", (SP[0], -3.05))


def l_world():
    return lbl("the world", (PC[0], -3.05))


# ══════════════ B00: the supervisor stands between the model and the world ══════════════
def b00_state():
    return VGroup(model(ML, MLS), l_model(), slip(SL_B, SLS), patient(), l_world(), supervisor(), l_super(), tiles(), numerals(TX, 2.8))


class B00_Between(Scene):
    def construct(self):
        md = model(ML, MLS)
        self.play(FadeIn(md, shift=UP * 0.4), FadeIn(l_model()), run_time=0.6)
        until(self, "makes an output", lead=0.2)
        sl = slip(SL_A, SLS)
        rt = guard(self, 0.35)
        self.play(FadeIn(sl, shift=DOWN * 0.5), run_time=rt, rate_func=ease_in)
        until(self, "against the world", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(patient(), shift=UP * 0.3), FadeIn(l_world()), run_time=rt)
        until(self, "That someone", lead=0.2)
        rt = guard(self, 0.6)
        self.play(FadeIn(supervisor(), shift=UP * 0.4), FadeIn(l_super()), run_time=rt)
        until(self, "between the model", lead=0.2)
        rt = guard(self, 0.6)
        self.play(sl.animate.move_to(P3(SL_B)), run_time=rt)
        until(self, "five things", lead=0.3)
        tl = tiles()
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.3) for t in tl], lag_ratio=0.18), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(numerals(TX, 2.8)), run_time=rt)
        done(self)


# ══════════════ B01: plausibility auditing — the twitch ══════════════
PRX = [(2.0, -1.95 + k * 0.13) for k in range(5)]     # the prior: a stack of pages behind the supervisor
QM = (SP[0], 0.85)


def l_lowscore():
    return lbl("low score", (SL_B[0], -3.05))


def l_prior():
    return lbl("prior", (2.0, -3.05))


def prior_stack():
    return VGroup(*[slip(c, 0.9) for c in PRX])


def qmark():
    return T("?", 64).move_to(P3(QM))


def b01_state():
    return VGroup(model(ML, MLS), patient(dot=True), l_world(), supervisor(), slip(SL_B, SLS), l_lowscore(), prior_stack(), l_prior(), qmark())


class B01_Twitch(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        # st: 0 model, 1 l_model, 2 slip, 3 patient, 4 l_world, 5 supervisor, 6 l_super, 7 tiles, 8 numerals
        self.play(FadeOut(st[7]), FadeOut(st[8]), FadeOut(st[1]), FadeOut(st[6]), FadeOut(st[2]), run_time=0.45)
        until(self, "a low triage score", lead=0.2)
        sl = slip(SL_A, SLS)
        rt = guard(self, 0.3)
        self.play(FadeIn(sl, shift=DOWN * 0.5), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.6)
        self.play(sl.animate.move_to(P3(SL_B)), FadeIn(l_lowscore()), run_time=rt)
        until(self, "swollen leg", lead=0.2)
        rt = guard(self, 0.3)
        self.play(FadeIn(Dot([PT[0] - 0.1, PT[1] - 0.3, 0], radius=0.11, color=TERRA).set_z_index(3), scale=1.8), run_time=rt)
        until(self, "something twitches", lead=0.15)
        sup = st[5]
        rt = guard(self, 0.9)
        self.play(Succession(Rotate(sup, angle=0.14), Rotate(sup, angle=-0.28), Rotate(sup, angle=0.14)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(qmark(), scale=1.6), run_time=rt)
        until(self, "a check against a prior", lead=0.2)
        ps = prior_stack()
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(p_, shift=UP * 0.25) for p_ in ps], lag_ratio=0.2), FadeIn(l_prior()), run_time=rt)
        until(self, "built over years", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(ps, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B02: the model has its training data; the supervisor has the world ══════════════
CR2 = (-2.0, 1.15)
CRS2 = 0.8
WL_A, WL_B = (0.8, -0.55), (3.4, -0.55)
SL_C = (2.5, -2.15)


def l_training():
    return lbl("training data", (CR2[0], 2.95))


def l_credible():
    return lbl("credible format", (SL_C[0], -3.1), 40)


def world_line():
    return Line(P3(WL_A), P3(WL_B), color=BAR1, stroke_width=7)


def b02_state():
    return VGroup(model(ML, MLS), patient(dot=True), supervisor(), crate(CR2, CRS2), l_training(), world_line(),
                  slip(SL_C, SLS), check(SL_C[0], slip_top(SL_C, SLS)[1] + 0.05, 0.28), l_credible())


class B02_TrainingVsWorld(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        # st: 0 model, 1 patient, 2 l_world, 3 supervisor, 4 slip, 5 l_lowscore, 6 prior, 7 l_prior, 8 qmark
        self.play(FadeOut(st[8]), FadeOut(st[5]), run_time=0.4)
        until(self, "its training data", lead=0.4)
        rt = guard(self, 0.5)
        self.play(FadeIn(crate(CR2, CRS2), shift=DOWN * 0.4), FadeIn(l_training()), run_time=rt, rate_func=ease_in)
        until(self, "supervisor has the world", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Create(world_line()), run_time=rt)
        until(self, "nobody audits", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeOut(st[6]), FadeOut(st[7]), run_time=rt)
        until(self, "credible format", lead=0.4)
        rt = guard(self, 1.0)
        self.play(st[4].animate.move_to(P3(SL_C)), FadeOut(st[2]), run_time=rt)
        until(self, "goes through", lead=0.2)
        rt = guard(self, 0.35)
        self.play(Create(check(SL_C[0], slip_top(SL_C, SLS)[1] + 0.05, 0.28)), FadeIn(l_credible()), run_time=rt)
        done(self)


# ══════════════ B03: problem formulation — two questions, one asked ══════════════
SP3 = (4.3, -1.5)
Q1, Q2 = (-0.6, 0.9), (2.9, 0.9)
Q1_IN = (-3.0, 0.15)
Q2_STOP = (-0.5, 0.15)
ANS = (-2.6, -2.05)


def q_slip(c, text):
    """(slip, label): the label sits above the slip; it moves with it, and fades before the slip enters the model."""
    return slip(c, 1.0), lbl(text, (c[0], c[1] + 1.0))


def l_never():
    return lbl("never asked", (Q2_STOP[0], -0.95))


def b03_state():
    return VGroup(model(ML, MLS), supervisor(SP3), slip(ANS), check(ANS[0], slip_top(ANS)[1] + 0.05, 0.26),
                  *q_slip(Q2_STOP, "life-threatening?"), l_never())


class B03_TwoQuestions(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        rt = guard(self, 0.6)
        self.play(FadeIn(model(ML, MLS), shift=UP * 0.3), FadeIn(supervisor(SP3), shift=UP * 0.3), run_time=rt)
        until(self, "not performance", lead=0.3)
        qa, la = q_slip(Q1, "category?")
        qb, lb = q_slip(Q2, "life-threatening?")
        rt = guard(self, 0.6)
        self.play(FadeIn(qa, shift=DOWN * 0.3), FadeIn(la), FadeIn(qb, shift=DOWN * 0.3), FadeIn(lb), run_time=rt)
        until(self, "The triage system answered", lead=0.2)
        rt = guard(self, 0.8)
        self.play(qa.animate.move_to(P3(Q1_IN)), FadeOut(la), run_time=rt)
        rt = guard(self, 0.35)
        self.play(FadeOut(qa, shift=DOWN * 0.3), run_time=rt)
        until(self, "statistical category", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(slip(ANS), shift=DOWN * 0.4), run_time=rt, rate_func=ease_in)
        until(self, "how likely", lead=0.2)
        rt = guard(self, 0.8)
        self.play(qb.animate.move_to(P3(Q2_STOP)), lb.animate.move_to(P3((Q2_STOP[0], Q2_STOP[1] + 1.0))), run_time=rt)
        until(self, "answered well", lead=0.2)
        rt = guard(self, 0.35)
        self.play(Create(check(ANS[0], slip_top(ANS)[1] + 0.05, 0.26)), run_time=rt)
        until(self, "never asked", lead=0.25)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_never()), run_time=rt)
        done(self)


# ══════════════ B04: tool orchestration — which tool, and no tool yet ══════════════
PX4 = [-4.3, -1.45, 1.45, 4.3]
PY4 = -1.1
PS4 = 1.15
SP4 = (-5.3, 2.05)
CUR_Y = 1.7


def plinth(c, s=PS4):
    return tile(c, s)


def on_plinth(k):
    return plinth_top((PX4[k], PY4), PS4)


def tool_ai():
    c = on_plinth(0)
    return model((c[0], c[1] + 0.05), 1.0)


def tool_human():
    c = on_plinth(1)
    return peg(c[0], c[1] + 0.55, 1.1)


def tool_other():
    c = on_plinth(2)
    return model((c[0], c[1] + 0.05), 1.0, (DARK_TOP, DARK_L, DARK_R))


def l_ai():
    return lbl("AI", (PX4[0], -2.8))


def l_human():
    return lbl("human", (PX4[1], -2.8))


def l_notool():
    return lbl("no tool yet", (PX4[3], -2.8))


def b04_state():
    return VGroup(VGroup(*[plinth((x, PY4)) for x in PX4]), tool_ai(), tool_human(), tool_other(), l_ai(), l_human(), l_notool(),
                  supervisor(SP4, 1.0), cursor(PX4[3], CUR_Y, 1.0), Dot([PX4[3], on_plinth(3)[1] + 0.05, 0], radius=0.14, color=TERRA))


class B04_WhichTool(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        pl = VGroup(*[plinth((x, PY4)) for x in PX4])
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(p_, shift=UP * 0.3) for p_ in pl], lag_ratio=0.15), FadeIn(supervisor(SP4, 1.0)), run_time=rt)
        until(self, "picks the tool", lead=0.3)
        ta, th, to = tool_ai(), tool_human(), tool_other()
        rt = guard(self, 0.7)
        self.play(FadeIn(ta, shift=DOWN * 0.3), FadeIn(th, shift=DOWN * 0.3), FadeIn(to, shift=DOWN * 0.3),
                  FadeIn(l_ai()), FadeIn(l_human()), run_time=rt, rate_func=ease_in)
        until(self, "the AI,", lead=0.2)
        cu = cursor(SP4[0] + 0.7, CUR_Y, 1.0)
        rt = guard(self, 0.4)
        self.play(FadeIn(cu), run_time=rt)
        rt = guard(self, 0.5)
        self.play(cu.animate.move_to([PX4[0], CUR_Y, 0]), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Indicate(ta, color=None, scale_factor=1.08), run_time=rt)
        until(self, "human judgment", lead=0.2)
        rt = guard(self, 0.5)
        self.play(cu.animate.move_to([PX4[1], CUR_Y, 0]), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Indicate(th, color=None, scale_factor=1.08), run_time=rt)
        until(self, "a different model", lead=0.2)
        rt = guard(self, 0.5)
        self.play(cu.animate.move_to([PX4[2], CUR_Y, 0]), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Indicate(to, color=None, scale_factor=1.08), run_time=rt)
        until(self, "no tool yet", lead=0.35)
        rt = guard(self, 0.5)
        self.play(cu.animate.move_to([PX4[3], CUR_Y, 0]), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(Dot([PX4[3], on_plinth(3)[1] + 0.05, 0], radius=0.14, color=TERRA), scale=1.8), FadeIn(l_notool()), run_time=rt)
        until(self, "well enough to deploy", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(pl[3], color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B05: "we should not deploy this here" — and the failure that runs the other way ══════════════
AI5 = (-4.0, -1.05)
AIS5 = 1.2
PL5 = (3.8, -1.55)
SUB5 = plinth_top(PL5, PS4)
SP5 = (0.0, 1.05)
PATH_A, PATH_B = (-2.35, -1.55), (2.55, -1.55)
CX5 = (0.0, -1.55)
AI5_TO = (0.9, -1.05)


def path5():
    return Line(P3(PATH_A), P3(PATH_B), color=BAR1, stroke_width=7)


def l_sub():
    return lbl("sub-problem", (PL5[0], -3.05))


def l_nothere():
    return lbl("not here", (CX5[0] + 1.35, CX5[1] + 0.55))


def l_avail():
    return lbl("available", (AI5_TO[0], 1.6))


def b05_state():
    return VGroup(model(AI5_TO, AIS5), plinth(PL5), slip((SUB5[0], SUB5[1] + 0.02), 0.9), l_sub(), l_avail())


class B05_NoMandate(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        ai = model(AI5, AIS5)
        rt = guard(self, 0.6)
        self.play(FadeIn(ai, shift=UP * 0.3), FadeIn(plinth(PL5), shift=UP * 0.3), FadeIn(l_sub()), run_time=rt)
        pa = path5()
        rt = guard(self, 0.4)
        self.play(FadeIn(slip((SUB5[0], SUB5[1] + 0.02), 0.9), shift=DOWN * 0.3), Create(pa), run_time=rt)
        until(self, "not deploy this here", lead=0.3)
        sup = supervisor(SP5, 1.1)
        rt = guard(self, 0.4)
        self.play(FadeIn(sup, shift=DOWN * 0.3), run_time=rt)
        cx, ln = cross(CX5[0], CX5[1], 0.3), l_nothere()
        rt = guard(self, 0.4)
        self.play(Create(cx), FadeIn(ln), run_time=rt)
        until(self, "most valuable", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(cx, color=None, scale_factor=1.25), run_time=rt)
        until(self, "runs the other way", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeOut(sup), FadeOut(cx), FadeOut(ln), FadeOut(pa), run_time=rt)
        until(self, "because it is available", lead=0.3)
        rt = guard(self, 1.0)
        self.play(ai.animate.move_to(P3(AI5_TO)), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_avail()), run_time=rt)
        done(self)


# ══════════════ B06: interpretive judgment — the number in the domain ══════════════
CR6 = (-4.2, -1.55)
CRS6 = 1.25
HERO = (0.0, 1.75)
CAP6 = (0.0, 0.65)
SL6_L, SL6_R = (-4.2, 1.45), (PC[0], 1.2)


def hero():
    return T("5%", 120).move_to(P3(HERO))


def l_cap6():
    return lbl("the chapter's example", CAP6, 34)


def l_spam():
    return lbl("spam filter", (CR6[0], -3.05))


def l_cancer():
    return lbl("cancer screen", (PC[0], -3.05))


def b06_state():
    return VGroup(supervisor(), hero(), l_cap6(), crate(CR6, CRS6), l_spam(), patient(), l_cancer(),
                  slip(SL6_L, 0.85), check(SL6_L[0], slip_top(SL6_L, 0.85)[1] + 0.05, 0.26),
                  slip(SL6_R, 0.85), cross(SL6_R[0], slip_top(SL6_R, 0.85)[1] + 0.1, 0.26))


class B06_NumberInDomain(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        rt = guard(self, 0.5)
        self.play(FadeIn(supervisor(), shift=UP * 0.3), run_time=rt)
        until(self, "five percent", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(hero(), scale=0.6), FadeIn(l_cap6()), run_time=rt)
        until(self, "spam filter", lead=0.4)
        rt = guard(self, 0.5)
        self.play(FadeIn(crate(CR6, CRS6), shift=UP * 0.3), FadeIn(l_spam()), run_time=rt)
        sa = slip(SL_B, 0.85)
        rt = guard(self, 0.7)
        self.play(sa.animate.move_to(P3(SL6_L)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Create(check(SL6_L[0], slip_top(SL6_L, 0.85)[1] + 0.05, 0.26)), run_time=rt)
        until(self, "cancer screen", lead=0.4)
        rt = guard(self, 0.5)
        self.play(FadeIn(patient(), shift=UP * 0.3), FadeIn(l_cancer()), run_time=rt)
        sb = slip(SL_B, 0.85)
        rt = guard(self, 0.7)
        self.play(sb.animate.move_to(P3(SL6_R)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(Create(cross(SL6_R[0], slip_top(SL6_R, 0.85)[1] + 0.1, 0.26)), run_time=rt)
        until(self, "not the meaning", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(hero(), color=None, scale_factor=1.1), run_time=rt)
        done(self)


# ══════════════ B07: executive integration — where the buck stops ══════════════
SRC = [(-3.7, 1.8), (0.0, 1.8), (3.7, 1.8)]
SRCS = 0.85
OUT7 = [(x, 0.55) for x, _ in SRC]
PL7 = (0.0, -1.45)
PLS7 = 0.95
SP7 = plinth_top(PL7, PLS7)
ROW7 = [(-2.1, -2.75), (0.0, -2.75), (2.1, -2.75)]
DEC7 = (0.0, -2.75)


def sources():
    return VGroup(model(SRC[0], SRCS), model(SRC[1], SRCS, (DARK_TOP, DARK_L, DARK_R)), peg(SRC[2][0], SRC[2][1] + 0.1, 1.0))


def out_slips():
    return VGroup(*[slip(c, 0.75) for c in OUT7])


def l_outputs():
    return lbl("outputs", (1.95, OUT7[1][1]))


def l_decision():
    return lbl("decision", (1.9, DEC7[1]))


def l_buck():
    return lbl("buck stops", (2.35, PL7[1] + 0.1))


def seal(c=DEC7, s=0.85):
    return Dot([c[0], slip_top(c, s)[1] + 0.02, 0], radius=0.13, color=TERRA).set_z_index(3)


def b07_state():
    return VGroup(sources(), plinth(PL7, PLS7), supervisor((SP7[0], SP7[1] + 0.5), 1.0), slip(DEC7, 0.85), seal(), l_decision(), l_buck())


class B07_BuckStops(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        src = sources()
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[FadeIn(s_, shift=UP * 0.3) for s_ in src], lag_ratio=0.2), run_time=rt)
        until(self, "many tools", lead=0.3)
        os_, lo = out_slips(), l_outputs()
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[FadeIn(s_, shift=DOWN * 0.3) for s_ in os_], lag_ratio=0.2), FadeIn(lo), run_time=rt, rate_func=ease_in)
        until(self, "synthesized", lead=0.2)
        rt = guard(self, 0.9)
        self.play(*[s_.animate.move_to(P3(c)) for s_, c in zip(os_, ROW7)], run_time=rt)
        until(self, "one decision", lead=0.2)
        dec = slip(DEC7, 0.85)
        rt = guard(self, 0.5)
        self.play(FadeOut(os_), FadeIn(dec, scale=1.15), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(seal(), scale=1.8), FadeIn(l_decision()), run_time=rt)
        until(self, "someone stands behind", lead=0.2)
        pl, sup = plinth(PL7, PLS7), supervisor((SP7[0], SP7[1] + 0.5), 1.0)
        rt = guard(self, 0.5)
        self.play(FadeIn(pl, shift=UP * 0.3), FadeIn(sup, shift=UP * 0.3), FadeOut(lo), run_time=rt)
        until(self, "buck has to stop", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(l_buck()), Indicate(pl, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B08: no place for it — a pile with no owner ══════════════
PILE8 = [(0.0, -2.55 + k * 0.16) for k in range(3)]


def l_noplace():
    return lbl("no place", (0.0, PL7[1] + 0.35))


def l_noowner():
    return lbl("no owner", (2.2, PILE8[1][1]))


class B08_NoPlace(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        # st: 0 sources, 1 plinth, 2 supervisor, 3 decision slip, 4 seal, 5 l_decision, 6 l_buck
        until(self, "most often missing", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeOut(st[3]), FadeOut(st[4]), FadeOut(st[5]), FadeOut(st[6]), run_time=rt)
        until(self, "no model produces it", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeOut(st[1], shift=DOWN * 0.4), FadeOut(st[2], shift=DOWN * 0.4), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_noplace()), run_time=rt)
        until(self, "no place for it", lead=0.2)
        os_ = out_slips()
        rt = guard(self, 0.5)
        self.play(LaggedStart(*[FadeIn(s_, shift=DOWN * 0.3) for s_ in os_], lag_ratio=0.2), run_time=rt, rate_func=ease_in)
        until(self, "nobody owns", lead=0.6)
        rt = guard(self, 0.9)
        self.play(*[s_.animate.move_to(P3(c)) for s_, c in zip(os_, PILE8)], run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_noowner()), run_time=rt)
        until(self, "dissolves", lead=0.3)
        rt = guard(self, 1.0)
        self.play(*[s_.animate.move_to(P3(c)) for s_, c in zip(os_, OUT7)], run_time=rt)
        done(self)


def b08_state():
    return VGroup(sources(), out_slips(), l_noplace(), l_noowner())


# ══════════════ B09: name the capacity and by whom; where you can't, a gap ══════════════
PX9 = [-4.6, -2.3, 0.0, 2.3, 4.6]
PY9 = 0.95
PS9 = 0.95
GAP = 3
PC9 = (2.3, -2.9)


def plinths9():
    return VGroup(*[tile((x, PY9), PS9) for x in PX9])


def peg_on(k):
    c = plinth_top((PX9[k], PY9), PS9)
    return peg(c[0], c[1] + 0.46, 0.88, badge=True)


def l_gap():
    return lbl("gap", (PX9[GAP], 2.6))


def patient9():
    return VGroup(chair(PC9[0], PC9[1], 1.0), peg(PC9[0], PC9[1] + 1.05, 1.0))


class B09_Gap(Scene):
    def construct(self):
        st = b08_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        pl = plinths9()
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(p_, shift=UP * 0.3) for p_ in pl], lag_ratio=0.15), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(numerals(PX9, -0.15)), run_time=rt)
        until(self, "by whom", lead=0.6)
        pegs = [peg_on(k) for k in range(5) if k != GAP]
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(p_, shift=DOWN * 0.3) for p_ in pegs], lag_ratio=0.22), run_time=rt, rate_func=ease_in)
        until(self, "found a gap", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_gap(), shift=DOWN * 0.2), Indicate(pl[GAP], color=None, scale_factor=1.08), run_time=rt)
        until(self, "where the patients die", lead=0.5)
        pt = patient9()
        pt.shift(RIGHT * 4.0)
        rt = guard(self, 0.9)
        self.play(pt.animate.shift(LEFT * 4.0), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Between, B01_Twitch, B02_TrainingVsWorld, B03_TwoQuestions, B04_WhichTool, B05_NoMandate,
             B06_NumberInDomain, B07_BuckStops, B08_NoPlace, B09_Gap):
    _cls.play = ST.play
