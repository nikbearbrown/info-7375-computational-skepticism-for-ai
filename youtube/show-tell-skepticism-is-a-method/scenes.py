"""
Manim scenes for show-tell-skepticism-is-a-method (show-tell skill; INFO 7375 course film).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

"What I mean by skepticism" (chapter 1 of INFO 7375, lines 33-97): skepticism is a method, not a mood.
A white CLAIM page on a dark plinth and a kraft TOOLBOX whose three MOVE tags (1, 2, 3) rise out; the claim
gets neat lines, an ink check and a full CONFIDENCE bar while the tags sink back (the enemy is confidence);
Descartes turns doubt into three CHECK crates (data, inputs, setting); eight dark SERVERS, seven get the code,
the eighth is missed and pours orders ($460M+, per the SEC); a kraft TURKEY, a feeding tray and a rising
confidence curve that drops on day 1,001; 108 WEEK tiles, 100 too high (Google Flu Trends, per Science 2014);
white SWANS and one black swan turn the claim's check into a cross; three BEDS and an outside test (2 of 3
missed, per JAMA Intern Med 2021); a kraft BEAM on dark posts takes a load test and holds.
A midpoint guard (ST / guard, from show-tell-context-is-a-budget, 0.22 s margin) keeps every
animation off the clip midpoint, where GATE T and Gate V sample.
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


def done(self):
    """finish() plus a pacing report (a clip must not outrun its audio: compile centre-cuts it)."""
    bid = type(self).__name__.split("_")[0]
    t = _elapsed(self)
    tgt = _TARGET.get(bid, 0)
    print(f"[pace] {bid} content={t:.2f}s target={tgt:.2f}s" + ("  OVER" if t > tgt - 0.1 else ""))
    if tgt:
        self.wait(max(0.05, tgt - t - 0.05))     # end 0.05 s under the audio (4K frame rounding)
    else:
        self.wait(2.0)




# ═════════════════════════════ the film: skepticism is a method, not a mood ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
PAD = "#E6E1D6"            # within Gate V's INK_DELTA of the stage
TAGC = BOX_L


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=42):
    return T(s, size).move_to(P3(c))


def cross(x, y, s=0.22, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=INK, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=INK, stroke_width=w))


# ─── the CLAIM: a white page on a dark plinth ───
CLW, CLD, CLH = 2.0, 1.6, 0.5
CL = (0.4, -1.3)
CLS = 1.25


def claim(c=CL, s=CLS):
    i = rig_at(c[0], c[1], s, CLW, CLD)
    plinth = i.box(0, 0, 0, CLW, CLD, CLH, DARK_TOP, DARK_L, DARK_R)
    page = i.box(0.15, 0.15, CLH, CLW - 0.3, CLD - 0.3, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=4)
    return VGroup(plinth, page)


def claim_lines(c=CL, s=CLS):
    i = rig_at(c[0], c[1], s, CLW, CLD)
    zt = CLH + 0.06
    return VGroup(*[Line(i.p(0.4, CLD * f, zt), i.p(CLW - 0.4 - (0.35 if k == 2 else 0.0), CLD * f, zt), color=BAR2, stroke_width=6)
                    for k, f in enumerate((0.72, 0.5, 0.28))])


def badge_pt(c=CL):
    return (c[0], c[1] + 2.35)


def l_claim(c=CL):
    return lbl("claim", (c[0], c[1] - 1.55))


# ─── the TOOLBOX and its three MOVE tags ───
TBW, TBD, TBH = 2.0, 1.2, 0.8
TB = (-4.4, -1.4)
TBS = 1.2
TAG_DX = [-1.0, 0.0, 1.0]


def toolbox(c=TB, s=TBS):
    i = rig_at(c[0], c[1], s, TBW, TBD)
    back, front = i.open_box(0, 0, 0, TBW, TBD, TBH)
    return back, front


def tag(k, c):
    c = P3(c)
    return VGroup(RoundedRectangle(width=0.84, height=0.68, corner_radius=0.16, fill_color=TAGC, fill_opacity=1, stroke_width=0).move_to(c),
                  T(str(k), 48, INK, bold=True).move_to(c)).set_z_index(1)


def tag_up(k, c=TB, s=TBS):
    return (c[0] + TAG_DX[k - 1] * s / TBS, c[1] + 2.45 * s / TBS)


def tags(c=TB, s=TBS):
    return VGroup(*[tag(k, tag_up(k, c, s)).scale(s / TBS) for k in (1, 2, 3)])


def l_method():
    return lbl("method", (TB[0], TB[1] + 3.3))


# ══════════════ B00: a method, not a mood ══════════════
def b00_state():
    back, front = toolbox()
    return VGroup(claim(), l_claim(), back, tags(), front, l_method())


class B00_Method(Scene):
    def construct(self):
        cl = claim()
        self.play(FadeIn(cl, shift=LEFT * 0.6), run_time=0.6)
        self.play(FadeIn(l_claim()), run_time=0.3)
        until(self, "A method", lead=0.3)
        back, front = toolbox()
        rt = guard(self, 0.6)
        self.play(FadeIn(VGroup(back, front), shift=DOWN * 0.7), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_method()), run_time=rt)
        until(self, "They can be taught", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(cl, color=None, scale_factor=1.04), run_time=rt)
        until(self, "Three philosophers", lead=0.1)
        tg = tags()
        rt = guard(self, 1.4)
        self.play(LaggedStart(*[FadeIn(t_, shift=UP * 0.9) for t_ in tg], lag_ratio=0.35), run_time=rt)
        done(self)


# ══════════════ B01: the enemy is confidence ══════════════
BAR_X, BAR_BASE, NSEG = 4.4, -2.3, 6
SEGH, SEGG = 0.45, 0.07


def conf_bar(n=NSEG):
    return VGroup(*[Rectangle(width=1.0, height=SEGH, fill_color=(BAR1, BAR2)[i % 2], fill_opacity=1, stroke_width=0)
                    .move_to([BAR_X, BAR_BASE + SEGG + (SEGH + SEGG) * i + SEGH / 2, 0]) for i in range(n)])


def l_looks():
    return lbl("looks right", (badge_pt()[0], badge_pt()[1] + 0.95))


def l_conf():
    return lbl("confidence", (BAR_X, BAR_BASE - 0.5))


def badge(c=CL):
    return check(*badge_pt(c), 0.33)


def b01_state():
    back, front = toolbox()
    return VGroup(claim(), claim_lines(), l_claim(), back, front, badge(), l_looks(), conf_bar(), l_conf())


class B01_Confidence(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        cl, tg = st[0], st[3]
        self.play(FadeOut(st[5]), run_time=0.3)
        until(self, "doubting what looks right", lead=0.3)
        ln = claim_lines()
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[Create(x) for x in ln], lag_ratio=0.3), run_time=rt)
        until(self, "neatly formatted", lead=0.2)
        bd = badge()
        rt = guard(self, 0.5)
        self.play(Create(bd), FadeIn(l_looks()), run_time=rt)
        until(self, "That's when the moves matter", lead=0.2)
        br = conf_bar()
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.15) for x in br], lag_ratio=0.3), FadeIn(l_conf()), run_time=rt)
        until(self, "the urge to skip them", lead=0.1)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeOut(t_, shift=DOWN * 0.9) for t_ in tg], lag_ratio=0.25), run_time=rt, rate_func=ease_in)
        until(self, "It's confidence", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(br, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B02: Descartes — doubt becomes a checklist ══════════════
CR_X0 = 3.9
CR_YS = [2.2, 0.65, -0.9]
CR_NAMES = ["data", "inputs", "setting"]
CRW = 0.8


def crate(y, x=CR_X0, s=0.75):
    i = rig_at(x, y - 0.3, s, CRW, CRW)
    return i.box(0, 0, 0, CRW, CRW, 0.6)


def crate_lbl(k):
    return lbl(CR_NAMES[k], (CR_X0 + 1.5, CR_YS[k]))


def crate_chk(k):
    return check(CR_X0 - 1.0, CR_YS[k], 0.26)


def b02_state():
    back, front = toolbox()
    return VGroup(claim(), claim_lines(), l_claim(), back, tag(1, tag_up(1)), front, badge(),
                  VGroup(*[crate(y) for y in CR_YS]), VGroup(*[crate_lbl(k) for k in range(3)]),
                  VGroup(*[crate_chk(k) for k in range(3)]))


class B02_Doubt(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[6], st[7], st[8])), run_time=0.4)
        until(self, "Move one", lead=0.3)
        rt = guard(self, 0.7)
        self.play(FadeIn(tag(1, tag_up(1)), shift=UP * 0.9), run_time=rt)
        until(self, "what would have to be true", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(st[0], color=None, scale_factor=1.04), run_time=rt)
        until(self, "a checklist", lead=0.3)
        crs = [crate(y) for y in CR_YS]
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.5) for c in crs], lag_ratio=0.3), run_time=rt, rate_func=ease_in)
        for k, ph in enumerate(("the training data", "the inputs", "the setting")):
            until(self, ph, lead=0.15)
            rt = guard(self, 0.3)
            self.play(FadeIn(crate_lbl(k)), run_time=rt)
        until(self, "Each one, you can check", lead=0.2)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[Create(crate_chk(k)) for k in range(3)], lag_ratio=0.35), run_time=rt)
        done(self)


# ══════════════ B03: Knight Capital — eight servers, one missed ══════════════
SV_X = [-5.25 + 1.5 * k for k in range(8)]
SV_Y = -1.6
SVW = 0.9
SVS = 0.9


def server_at(x, y=SV_Y):
    i = rig_at(x, y, SVS, SVW, SVW)
    stack, lights = i.server(0, 0, 0, SVW, SVW, slab=0.42, n=2)
    for d in lights:
        d.scale(1.7)
    return stack, lights, i


def servers():
    st, lt, rigs = VGroup(), VGroup(), []
    for x in SV_X:
        s_, l_, i = server_at(x)
        st.add(s_)
        lt.add(l_)
        rigs.append(i)
    return st, lt, rigs


def code_page(i):
    return i.box(0.12, 0.12, 0.88, SVW - 0.24, SVW - 0.24, 0.05, PAGE_TOP, PAGE_L, PAGE_R, sw=3)


def l_missed():
    return lbl("missed", (SV_X[7], 0.35))


def hero_loss():
    return T("$460M+", 120, INK, bold=True).move_to([-1.1, 2.2, 0])


def l_sec():
    return lbl("per the SEC", (-1.1, 1.1), 40)


def sv_chk(k):
    return check(SV_X[k], 0.3, 0.22)


def b03_state():
    st, lt, rigs = servers()
    for k in range(8):
        lt[k].set_color(TERRA)
    return VGroup(st, lt, VGroup(*[code_page(rigs[k]) for k in range(7)]), hero_loss(), l_sec(),
                  VGroup(*[sv_chk(k) for k in range(8)]))


class B03_Knight(Scene):
    def construct(self):
        st0 = b02_state()
        self.add(st0)
        self.play(FadeOut(st0), run_time=0.45)
        sv, lt, rigs = servers()
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[FadeIn(VGroup(s_, l_), shift=UP * 0.4) for s_, l_ in zip(sv, lt)], lag_ratio=0.12), run_time=rt)
        until(self, "put new code", lead=0.2)
        pages = [code_page(rigs[k]) for k in range(7)]
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[FadeIn(p_, shift=DOWN * 0.7) for p_ in pages], lag_ratio=0.18), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[VGroup(*lt[k]).animate.set_color(TERRA) for k in range(7)], lag_ratio=0.15), run_time=rt)
        until(self, "missed one", lead=0.2)
        lm = l_missed()
        rt = guard(self, 0.4)
        self.play(FadeIn(lm), Indicate(sv[7], color=None, scale_factor=1.06), run_time=rt)
        until(self, "woke up", lead=0.3)
        rt = guard(self, 0.4)
        self.play(VGroup(*lt[7]).animate.set_color(TERRA), run_time=rt)
        until(self, "over four million trades", lead=0.6)
        src = np.array([SV_X[7], SV_Y + 0.9, 0])
        rt = guard(self, 1.6)
        sl = []
        for j in range(9):
            s_ = slip().scale(0.7).move_to(src)
            sl.append(s_)
        self.add(*sl)
        tg = [np.array([SV_X[7] + 0.4 + 0.35 * (j % 3), SV_Y + 5.6 + 0.3 * j, 0]) for j in range(9)]
        self.play(LaggedStart(*[s_.animate.move_to(t_) for s_, t_ in zip(sl, tg)], lag_ratio=0.15), run_time=rt, rate_func=ease_in)
        self.remove(*sl)
        until(self, "Knight lost", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(hero_loss(), scale=1.15), FadeIn(l_sec()), run_time=rt)
        until(self, "Ask what would make", lead=0.2)
        rt = guard(self, 0.3)
        self.play(FadeOut(lm), run_time=rt)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[Create(sv_chk(k)) for k in range(8)], lag_ratio=0.12), run_time=rt)
        done(self)


def slip():
    card = RoundedRectangle(width=0.8, height=0.52, corner_radius=0.08, fill_color=PAGE_TOP, fill_opacity=1,
                            stroke_color=INK, stroke_width=4)
    ln = VGroup(Line([-0.24, 0.07, 0], [0.26, 0.07, 0], color=BAR1, stroke_width=6),
                Line([-0.24, -0.09, 0], [0.12, -0.09, 0], color=BAR1, stroke_width=6))
    return VGroup(card, ln).set_z_index(10)


# ══════════════ B04: Hume — the turkey ══════════════
TK = (-3.9, -0.4)
TKS = 1.2


def turkey(c=TK, s=TKS):
    x, y = c
    fc = np.array([x - 0.55, y + 0.05, 0])
    fan = VGroup(*[AnnularSector(inner_radius=0.0, outer_radius=1.25, angle=PI / 5, start_angle=PI / 5 * k, arc_center=fc,
                                 fill_color=(BOX_FLOOR, BOX_IN1)[k % 2], fill_opacity=1, stroke_width=0) for k in range(5)])
    rim = Arc(radius=1.25, start_angle=0, angle=PI, arc_center=fc, color=INK, stroke_width=6)
    body = Ellipse(width=1.7, height=1.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    neck = Line([x + 0.5, y + 0.25, 0], [x + 0.85, y + 0.85, 0], color=BOX_L, stroke_width=26)
    head = Circle(radius=0.27, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x + 0.95, y + 1.0, 0])
    beak = Polygon([x + 1.2, y + 1.05, 0], [x + 1.45, y + 0.97, 0], [x + 1.2, y + 0.88, 0],
                   fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=3)
    wattle = Dot([x + 1.12, y + 0.72, 0], radius=0.1, color=TERRA)
    legs = VGroup(Line([x - 0.2, y - 0.5, 0], [x - 0.25, y - 1.05, 0], color=BAR1, stroke_width=10),
                  Line([x + 0.25, y - 0.5, 0], [x + 0.3, y - 1.05, 0], color=BAR1, stroke_width=10))
    g = VGroup(fan, rim, legs, body, neck, head, beak, wattle)
    return g.scale(s, about_point=np.array([x, y, 0]))


TRAY = (-2.2, -2.5)


def tray():
    i = rig_at(TRAY[0], TRAY[1], 0.9, 1.5, 1.0)
    back, front = i.open_box(0, 0, 0, 1.5, 1.0, 0.3)
    grain = VGroup(*[Dot(i.p(0.3 + 0.3 * (k % 4), 0.3 + 0.35 * (k // 4), 0.02), radius=0.07, color=BOX_R).set_z_index(1) for k in range(8)])
    return back, grain, front


AX_Y = -2.35
CUR = [(-0.7 + 0.18 * k, -2.1 + 3.2 * (1 - np.exp(-(0.18 * k) / 1.9))) for k in range(31)]   # x -1.2 .. 4.2


def axis():
    return Line([-0.95, AX_Y, 0], [5.6, AX_Y, 0], color=DEV_EDGE, stroke_width=4)


def curve_part(a, b):
    pts = [np.array([x, y, 0]) for x, y in CUR[a:b + 1]]
    return VMobject(color=INK, stroke_width=8).set_points_smoothly(pts)


def l_confc():
    return lbl("confidence", (0.6, 0.9))


def day(s):
    return T(s, 60, INK, bold=True).move_to([2.9, 2.55, 0])


def drop():
    x, y = CUR[-1]
    return VGroup(Line([x, y, 0], [x + 0.25, AX_Y + 0.25, 0], color=INK, stroke_width=8),
                  Dot([x + 0.25, AX_Y + 0.25, 0], radius=0.13, color=TERRA))


def b04_state():
    back, grain, front = tray()
    return VGroup(turkey(), back, front, axis(), curve_part(0, 30), drop(), l_confc(), day("day 1,001"))


class B04_Turkey(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        ax = axis()
        rt = guard(self, 0.5)
        self.play(Create(ax), FadeIn(l_confc()), run_time=rt)
        until(self, "no guarantee", lead=0.3)
        rt = guard(self, 0.4)
        self.play(Indicate(ax, color=None, scale_factor=1.02), run_time=rt)
        until(self, "Picture a turkey", lead=0.3)
        tk = turkey()
        back, grain, front = tray()
        rt = guard(self, 0.6)
        self.play(FadeIn(tk, shift=RIGHT * 0.5), FadeIn(VGroup(back, grain, front), shift=DOWN * 0.3), run_time=rt)
        until(self, "fed every morning", lead=0.2)
        ctr = day("day 1")
        rt = guard(self, 0.3)
        self.play(FadeIn(ctr), run_time=rt)
        segs = [(0, 8, "day 10"), (8, 16, "day 100"), (16, 30, "day 1,000")]
        for a, b, lab in segs:
            rt = guard(self, 0.75)
            self.play(Create(curve_part(a, b)), Transform(ctr, day(lab)), Indicate(grain, color=None, scale_factor=1.15), run_time=rt)
        until(self, "Each meal makes it surer", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(tk, color=None, scale_factor=1.04), run_time=rt)
        until(self, "one thousand and one", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Transform(ctr, day("day 1,001")), FadeOut(grain), run_time=rt)
        dp = drop()
        rt = guard(self, 0.5)
        self.play(Create(dp[0]), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.3)
        self.play(FadeIn(dp[1], scale=1.5), run_time=rt)
        done(self)


# ══════════════ B05: Google Flu Trends — a turkey with a spreadsheet ══════════════
GC, GR = 18, 6
GT, GP = 0.3, 0.36
GX0, GY0 = -1.9, -2.45
LOW = {3, 11, 20, 34, 52, 67, 88, 101}      # the 8 weeks that were not too high (positions illustrative)
TK5 = (-4.3, -0.9)


def tiles():
    g = VGroup()
    for n in range(GC * GR):
        r, c = divmod(n, GC)
        g.add(Square(side_length=GT, fill_color=GHOST, fill_opacity=1, stroke_width=0)
              .move_to([GX0 + c * GP + GT / 2, GY0 + (GR - 1 - r) * GP + GT / 2, 0]))
    return g


def hero_flu():
    return T("100 of 108", 96, INK, bold=True).move_to([1.35, 2.2, 0])


def l_weeks():
    return lbl("weeks too high", (1.35, 1.05))


def l_sci():
    return lbl("per Science, 2014", (1.35, -3.0), 36)


def b05_state():
    tl = tiles()
    for n in range(GC * GR):
        if n not in LOW:
            tl[n].set_fill(BAR1)
    return VGroup(turkey(TK5, TKS * 0.8), tl, hero_flu(), l_weeks(), l_sci())


class B05_Flu(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        tk = st[0]
        self.play(FadeOut(VGroup(*[st[i] for i in range(1, 8)])), run_time=0.45)
        rt = guard(self, 0.6)
        self.play(tk.animate.scale(0.8, about_point=np.array([TK[0], TK[1], 0])).shift(np.array([TK5[0] - TK[0], TK5[1] - TK[1], 0])), run_time=rt)
        until(self, "Google Flu Trends", lead=0.3)
        tl = tiles()
        rt = guard(self, 0.6)
        self.play(FadeIn(tl, shift=UP * 0.3), FadeIn(l_weeks()), run_time=rt)
        until(self, "From August", lead=0.2)
        hi = [n for n in range(GC * GR) if n not in LOW]
        rt = guard(self, 2.0)

        def fill(g, a):
            m = int(a * len(hi))
            for j in range(m):
                tl[hi[j]].set_fill(BAR1)
            return g
        self.play(UpdateFromAlphaFunc(tl, fill), run_time=rt, rate_func=linear)
        for n in hi:
            tl[n].set_fill(BAR1)
        until(self, "one hundred of", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(hero_flu(), scale=1.15), run_time=rt)
        until(self, "per a paper in Science", lead=0.2)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_sci()), run_time=rt)
        until(self, "A turkey with a spreadsheet", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(tk, color=None, scale_factor=1.08), run_time=rt)
        until(self, "not to the world", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(tl, color=None, scale_factor=1.03), run_time=rt)
        done(self)


# ══════════════ B06: Popper — white swans, one black swan ══════════════
CL6 = (-4.1, -1.3)
SW_X = [-0.9, 1.2, 3.3]
SW_Y = -1.1
BS_X = 5.25
SWS = 1.3


def swan(x, y=SW_Y, dark=False, s=SWS):
    fill = DARK_TOP if dark else PAGE_TOP
    body = Ellipse(width=1.15, height=0.52, fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    tail = Polygon([x - 0.5, y + 0.05, 0], [x - 0.78, y + 0.3, 0], [x - 0.42, y + 0.2, 0],
                   fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4)
    path = [np.array([x + 0.32, y + 0.12, 0]), np.array([x + 0.5, y + 0.45, 0]), np.array([x + 0.3, y + 0.7, 0]), np.array([x + 0.42, y + 0.95, 0])]
    neck_o = VMobject(color=INK, stroke_width=20).set_points_smoothly(path)
    neck_i = VMobject(color=fill, stroke_width=11).set_points_smoothly(path)
    head = Circle(radius=0.14, fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x + 0.46, y + 1.0, 0])
    beak = Dot([x + 0.66, y + 0.97, 0], radius=0.075, color=TERRA)
    return VGroup(tail, body, neck_o, neck_i, head, beak).scale(s, about_point=np.array([x, y, 0]))


def water():
    return Polygon([-2.0, SW_Y - 0.55, 0], [6.1, SW_Y - 0.55, 0], [6.1, SW_Y - 0.1, 0], [-2.0, SW_Y - 0.1, 0],
                   fill_color=PAD, fill_opacity=1, stroke_width=0).set_z_index(-2)


def l_white():
    return lbl("white swans", (1.2, 0.95))


def l_black():
    return lbl("black swan", (4.85, 0.95))


def b06_state():
    return VGroup(claim(CL6), claim_lines(CL6), l_claim(CL6), cross(*badge_pt(CL6), 0.3), water(),
                  VGroup(*[swan(x) for x in SW_X]), swan(BS_X, dark=True), l_white(), l_black())


class B06_Swans(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        cl, ln, lc, bd = claim(CL6), claim_lines(CL6), l_claim(CL6), check(*badge_pt(CL6), 0.33)
        rt = guard(self, 0.6)
        self.play(FadeIn(VGroup(cl, ln), shift=RIGHT * 0.5), FadeIn(lc), FadeIn(bd), run_time=rt)
        until(self, "can't be wrong", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(cl, ln), color=None, scale_factor=1.05), run_time=rt)
        until(self, "piling up successes", lead=0.3)
        wa = water()
        sws = [swan(x) for x in SW_X]
        rt = guard(self, 1.3)
        self.play(FadeIn(wa), LaggedStart(*[FadeIn(s_, shift=LEFT * 0.6) for s_ in sws], lag_ratio=0.3), run_time=rt)
        until(self, "No count of white swans", lead=0.2)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_white()), run_time=rt)
        until(self, "One black swan", lead=0.3)
        bs = swan(BS_X, dark=True)
        rt = guard(self, 0.6)
        self.play(FadeIn(bs, shift=DOWN * 0.4), FadeIn(l_black()), run_time=rt)
        until(self, "disproves it", lead=0.2)
        cx = cross(*badge_pt(CL6), 0.3)
        rt = guard(self, 0.5)
        self.play(FadeOut(bd), Create(cx), run_time=rt)
        done(self)


# ══════════════ B07: the sepsis model's outside test ══════════════
BED_X = [-4.0, -0.1, 3.8]
BED_Y = -1.4
BDW, BDD = 2.1, 0.95
LAMP_Y = 0.9


def bed(x, y=BED_Y, s=1.0):
    i = rig_at(x, y, s, BDW, BDD)
    base = i.box(0, 0, 0, BDW, BDD, 0.3, DARK_TOP, DARK_L, DARK_R)
    mat = i.box(0, 0, 0.3, BDW, BDD, 0.22)
    pillow = i.box(BDW - 0.6, 0.12, 0.52, 0.45, BDD - 0.24, 0.12, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    blanket = i.box(0.05, 0.05, 0.52, BDW - 0.8, BDD - 0.1, 0.1, PAGE_TOP, PAGE_L, PAGE_R, sw=3)
    return VGroup(base, mat, blanket, pillow)


def lamp(x, on=False):
    return Circle(radius=0.28, fill_color=TERRA if on else GHOST, fill_opacity=1, stroke_color=DEV_EDGE, stroke_width=3).move_to([x, LAMP_Y, 0])


def l_cases():
    return lbl("sepsis cases", (-0.1, -2.95))


def hero_sep():
    return T("2 of 3 missed", 90, INK, bold=True).move_to([-0.1, 2.6, 0])


def l_jama():
    return lbl("per JAMA Intern Med, 2021", (-0.1, 1.7), 36)


def scanline(x):
    return Line([x, -2.4, 0], [x, 1.35, 0], color=TERRA, stroke_width=8)


class B07_Sepsis(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        beds = [bed(x) for x in BED_X]
        lamps = [lamp(x) for x in BED_X]
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(VGroup(b_, l_), shift=UP * 0.4) for b_, l_ in zip(beds, lamps)], lag_ratio=0.25),
                  FadeIn(l_cases()), run_time=rt)
        until(self, "hundreds of U.S. hospitals", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(*lamps), color=None, scale_factor=1.2), run_time=rt)
        until(self, "When outside researchers", lead=0.3)
        rt = guard(self, 2.0)
        sc = scanline(-5.6)
        self.add(sc)
        self.play(sc.animate.move_to([5.6, -0.52, 0]), run_time=rt, rate_func=linear)
        self.remove(sc)
        until(self, "it missed about", lead=0.3)
        rt = guard(self, 0.4)
        self.play(lamps[0].animate.set_fill(TERRA), run_time=rt)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[Create(cross(x + 0.75, LAMP_Y, 0.22)) for x in BED_X[1:]], lag_ratio=0.4), run_time=rt)
        until(self, "two of every three", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(hero_sep(), scale=1.15), FadeIn(l_jama()), run_time=rt)
        done(self)


def b07_state():
    return VGroup(*[bed(x) for x in BED_X], lamp(BED_X[0], True), lamp(BED_X[1]), lamp(BED_X[2]),
                  *[cross(x + 0.75, LAMP_Y, 0.22) for x in BED_X[1:]], l_cases(), hero_sep(), l_jama())


# ══════════════ B08: the moves are tools — a load test on a beam ══════════════
BM = (1.9, -0.9)
BMW, BMD = 4.2, 0.8
TB8 = (-4.4, -1.6)
TB8S = 1.0


def beam_rig():
    return rig_at(BM[0], BM[1], 1.0, BMW, BMD)


def posts():
    i = beam_rig()
    return VGroup(i.box(0.2, 0.05, -1.3, 0.6, 0.7, 1.3, DARK_TOP, DARK_L, DARK_R),
                  i.box(BMW - 0.8, 0.05, -1.3, 0.6, 0.7, 1.3, DARK_TOP, DARK_L, DARK_R))


def beam():
    return beam_rig().box(0, 0, 0, BMW, BMD, 0.45)


def weight(z=0.45):
    return beam_rig().box(BMW / 2 - 0.5, 0.0, z, 1.0, 0.8, 0.8, DARK_TOP, DARK_L, DARK_R)


def l_load():
    p = beam_rig().p(BMW / 2, 0.4, 1.25)
    return lbl("load test", (p[0] - 2.4, p[1] + 0.55))


def l_tools():
    return lbl("tools", (TB8[0], TB8[1] + 2.9))


def beam_chk():
    p = beam_rig().p(BMW / 2, 0.4, 1.25)
    return check(p[0] + 0.1, p[1] + 0.75, 0.3)


class B08_Beam(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        ps, bm = posts(), beam()
        rt = guard(self, 0.6)
        self.play(FadeIn(ps, shift=UP * 0.4), FadeIn(bm, shift=DOWN * 0.4), run_time=rt)
        until(self, "The moves are tools", lead=0.3)
        back, front = toolbox(TB8, TB8S)
        tg = tags(TB8, TB8S)
        rt = guard(self, 0.5)
        self.play(FadeIn(VGroup(back, front), shift=DOWN * 0.5), FadeIn(l_tools()), run_time=rt)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(t_, shift=UP * 0.8) for t_ in tg], lag_ratio=0.3), run_time=rt)
        until(self, "load test on a beam", lead=0.3)
        wt = weight(2.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(wt, shift=DOWN * 0.3), FadeIn(l_load()), run_time=rt)
        rt = guard(self, 0.6)
        self.play(wt.animate.shift(np.array(weight(0.45)[2].get_center()) - np.array(wt[2].get_center())), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.4)
        self.play(VGroup(bm, wt).animate.shift(DOWN * 0.08), run_time=rt)
        until(self, "comes back clean", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Create(beam_chk()), run_time=rt)
        until(self, "Either way", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(tg, color=None, scale_factor=1.15), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Method, B01_Confidence, B02_Doubt, B03_Knight, B04_Turkey, B05_Flu, B06_Swans, B07_Sepsis, B08_Beam):
    _cls.play = ST.play
