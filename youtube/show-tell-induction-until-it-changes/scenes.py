"""
Manim scenes for show-tell-induction-until-it-changes (show-tell skill; INFO 7375 course film, Film 2 of
SHOW-TELL-THREE-MOVES.md: induction, Hume).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py. The kit, pacing
helpers and midpoint guard are copied from the sibling course film show-tell-skepticism-is-a-method.

Induction works until the world changes. The SUN rises over a horizon and each morning a day page lands
on a CALENDAR stack (Hume's Enquiry, 1748); tomorrow is only a ghost page and a ghost sun (no guarantee);
tomorrow's page turns solid and gets a plan and a check (custom, "the great guide of human life").
The HISTORY LINE of online shopping's share of US retail (US Census Bureau, 2010Q1-2020Q2, current
vintage) beside a kraft PARCEL: forecast bands one step ahead land on it (induction works); its quarterly
STEPS drop out as small grey bars inside one band (stationary); one SHOP over time and six SHOPS at once
share one average line (ergodic); the line jumps from about 12% to about 16% in 2020Q2 (COVID); the SYSTEM,
a kraft machine with a lever, drops equal step blocks until the lever flips and a giant block drops; a dark
MODEL block extends the old line while its confidence bar stays full; the rule: same system, trust (a check);
lever flipped, a lamp lights and a scan runs back over the history (check).
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


_SLACK = {"B06": 0.12}     # extra end slack: B06's 24 fps frame rounding ran its 4K clip 0.027 s past its audio (BUILD-LOG)


def done(self):
    """finish() plus a pacing report (a clip must not outrun its audio: compile centre-cuts it)."""
    bid = type(self).__name__.split("_")[0]
    t = _elapsed(self)
    tgt = _TARGET.get(bid, 0)
    print(f"[pace] {bid} content={t:.2f}s target={tgt:.2f}s" + ("  OVER" if t > tgt - 0.1 else ""))
    if tgt:
        self.wait(max(0.05, tgt - t - 0.05 - _SLACK.get(bid, 0.0)))     # end 0.05 s under the audio (4K frame rounding)
    else:
        self.wait(2.0)







# ═════════════════════════════ the film: induction works until the world changes ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
PAD = "#E6E1D6"            # within Gate V's INK_DELTA of the stage


def P3(c):
    c = np.array(c, dtype=float)
    return np.array([c[0], c[1], 0.0])


def rig_at(cx, cy, s, w, d):
    """An Iso rig that centres a w x d footprint on screen point (cx, cy)."""
    return Iso(cx - (w - d) * C30 * s / 2.0, cy - (w + d) * 0.5 * s / 2.0, s)


def lbl(s, c, size=42):
    return T(s, size).move_to(P3(c))


# ─── the SUN, the HORIZON and the CALENDAR stack of days (Hume) ───
HZ_Y = -0.9
SUN_X = -3.0
SUN_R = 0.8
SUN_UP, SUN_DOWN = 1.2, -2.0


def ground():
    g = Polygon([-6.15, -3.25, 0], [0.9, -3.25, 0], [0.9, HZ_Y, 0], [-6.15, HZ_Y, 0], fill_color=STAGE, fill_opacity=1, stroke_width=0)
    g.set_z_index(3)
    hz = Line([-6.1, HZ_Y, 0], [0.7, HZ_Y, 0], color=DEV_EDGE, stroke_width=6).set_z_index(4)
    return VGroup(g, hz)


def sun(y=SUN_UP):
    return Circle(radius=SUN_R, fill_color=TERRA, fill_opacity=1, stroke_width=0).move_to([SUN_X, y, 0]).set_z_index(1)


def ghost_sun():
    return Circle(radius=SUN_R, fill_color=GHOST, fill_opacity=1, stroke_color=BAR2, stroke_width=5).move_to([SUN_X, HZ_Y + 0.05, 0]).set_z_index(1)


CAL = (3.55, -1.75)
CS = 1.3
CW, CD, PH, PP = 2.2, 1.8, 0.12, 0.16
PLH = 0.45


def cal_rig():
    return rig_at(CAL[0], CAL[1], CS, CW, CD)


def plinth():
    return cal_rig().box(0, 0, 0, CW, CD, PLH, DARK_TOP, DARK_L, DARK_R)


def day_page(k, ghost=False):
    i = cal_rig()
    if ghost:
        return i.box(0.1, 0.1, PLH + k * PP, CW - 0.2, CD - 0.2, PH, GHOST, GHOST, GHOST, sw=0).set_z_index(1)
    g = VGroup(*[i.quad(q, f, stroke=BAR1, sw=3) for q, f in (
        ([(0.1, 0.1, PLH + k * PP), (0.1, CD - 0.1, PLH + k * PP), (0.1, CD - 0.1, PLH + k * PP + PH), (0.1, 0.1, PLH + k * PP + PH)], PAGE_L),
        ([(0.1, 0.1, PLH + k * PP), (CW - 0.1, 0.1, PLH + k * PP), (CW - 0.1, 0.1, PLH + k * PP + PH), (0.1, 0.1, PLH + k * PP + PH)], PAGE_R),
        ([(0.1, 0.1, PLH + k * PP + PH), (CW - 0.1, 0.1, PLH + k * PP + PH), (CW - 0.1, CD - 0.1, PLH + k * PP + PH), (0.1, CD - 0.1, PLH + k * PP + PH)], PAGE_TOP))])
    return g.set_z_index(1)


NDAYS = 5


def plan_lines():
    i = cal_rig()
    zt = PLH + NDAYS * PP + PH
    return VGroup(*[Line(i.p(0.5, CD * f, zt), i.p(CW - 0.5 - (0.4 if k == 2 else 0.0), CD * f, zt), color=BAR1, stroke_width=7)
                    for k, f in enumerate((0.7, 0.5, 0.3))]).set_z_index(2)


def l_hume():
    return lbl("Hume's Enquiry, 1748", (-3.0, 2.6), 46)


def l_tomorrow():
    return lbl("tomorrow?", (CAL[0], 2.1))


def l_custom():
    return lbl("custom", (CAL[0] - 0.6, 2.1))


def cal_check():
    return check(CAL[0] + 1.0, 2.1, 0.3)


def b00_state():
    return VGroup(ground(), plinth(), VGroup(*[day_page(k) for k in range(NDAYS)]), day_page(NDAYS, ghost=True), ghost_sun(),
                  l_hume(), l_tomorrow())


# ══════════════ B00: Hume — the sun has risen every morning ══════════════
class B00_Sun(Scene):
    def construct(self):
        gr, pl = ground(), plinth()
        self.play(FadeIn(gr), FadeIn(pl, shift=UP * 0.3), run_time=0.6)
        until(self, "David Hume", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_hume()), run_time=rt)
        until(self, "The sun has risen", lead=0.3)
        sn = sun(SUN_DOWN)
        self.add(sn)
        rt = guard(self, 0.8)
        self.play(sn.animate.move_to([SUN_X, SUN_UP, 0]), run_time=rt)
        until(self, "every morning", lead=0.3)
        pgs = [day_page(k) for k in range(NDAYS)]
        rt = guard(self, 1.8)
        self.play(LaggedStart(*[FadeIn(p_, shift=DOWN * 0.4) for p_ in pgs], lag_ratio=0.5), run_time=rt, rate_func=ease_in)
        until(self, "Does that prove", lead=0.2)
        rt = guard(self, 0.6)
        self.play(sn.animate.move_to([SUN_X, SUN_DOWN, 0]), run_time=rt)
        self.remove(sn)
        gp, gs, lt = day_page(NDAYS, ghost=True), ghost_sun(), l_tomorrow()
        rt = guard(self, 0.6)
        self.play(FadeIn(gp, shift=DOWN * 0.3), FadeIn(gs), FadeIn(lt), run_time=rt)
        until(self, "no contradiction", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(gs, color=None, scale_factor=1.12), run_time=rt)
        until(self, "The past gives", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(gp, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B01: custom, the great guide of human life ══════════════
class B01_Custom(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        gp, lt = st[3], st[6]
        until(self, "Only a fool", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(st[2], color=None, scale_factor=1.05), run_time=rt)
        until(self, "we live by it", lead=0.4)
        sp = day_page(NDAYS)
        rt = guard(self, 0.6)
        self.play(FadeOut(gp), FadeIn(sp, shift=DOWN * 0.3), FadeOut(lt), run_time=rt)
        pl = plan_lines()
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[Create(x) for x in pl], lag_ratio=0.3), run_time=rt)
        until(self, "He called that custom", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeIn(l_custom()), Create(cal_check()), run_time=rt)
        until(self, "the great guide", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(sp, pl), color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ─── the HISTORY LINE: online share of US retail sales (US Census Bureau, seasonally adjusted, %) ───
# 2010Q1 .. 2020Q2, the Census series as currently revised (FRED ECOMPCTSA, source: US Census Bureau), sources/.
SHARE = [4.2, 4.4, 4.6, 4.6, 4.7, 4.8, 4.9, 5.1, 5.2, 5.3, 5.5, 5.6, 5.6, 5.8, 5.9, 6.1, 6.2, 6.3, 6.5, 6.6, 6.9,
         7.0, 7.2, 7.4, 7.7, 7.8, 8.0, 8.2, 8.4, 8.7, 8.9, 9.1, 9.4, 9.6, 9.7, 9.9, 10.0, 10.3, 10.8, 11.2, 11.9, 16.3]
NQ = len(SHARE)            # 42 quarters
Q19 = 39                   # 2019Q4
AVG_STEP = 0.18            # mean quarterly step 2010Q1-2019Q4 (7.0 points / 39 steps)
CX0, CX1 = -1.2, 5.7
YB, YS = -2.8, 0.36


def qx(q):
    return CX0 + (CX1 - CX0) * q / (NQ - 1)


def vy(v, dy=0.0):
    return YB + dy + v * YS


def pt(q, dy=0.0):
    return np.array([qx(q), vy(SHARE[q], dy), 0.0])


def hist(a, b, dy=0.0, sw=8):
    return VMobject(color=INK, stroke_width=sw).set_points_as_corners([pt(q, dy) for q in range(a, b + 1)]).set_z_index(2)


def axis(dy=0.0):
    return Line([CX0 - 0.25, YB + dy, 0], [CX1 + 0.2, YB + dy, 0], color=DEV_EDGE, stroke_width=4)


def end_dot(q, dy=0.0):
    return Dot(pt(q, dy), radius=0.12, color=TERRA).set_z_index(3)


def trend_band():
    """The old line carried forward: the 2017Q3-2019Q4 slope (0.256 points a quarter) extended to 2020Q2 (about 11.7%)."""
    a = pt(30)
    b = np.array([qx(NQ - 1), vy(SHARE[30] + (SHARE[Q19] - SHARE[30]) / (Q19 - 30) * (NQ - 1 - 30)), 0.0])
    return Line(a, b, color=BAR2, stroke_width=26).set_z_index(1)


def band(q, n=6, dy=0.0):
    a = pt(q, dy)
    b = np.array([qx(q + n), vy(SHARE[q] + AVG_STEP * n, dy), 0.0])
    return Line(a, b, color=BAR2, stroke_width=26).set_z_index(1)


def parcel(c, s=1.0, w=1.3, d=1.1, h=0.9):
    i = rig_at(c[0], c[1], s, w, d)
    body = i.box(0, 0, 0, w, d, h)
    ym, t = d / 2, 0.12
    strap = VGroup(i.quad([(0, ym - t, h), (w, ym - t, h), (w, ym + t, h), (0, ym + t, h)], BAR1, sw=0),
                   i.quad([(0, ym - t, h), (0, ym + t, h), (0, ym + t, h - 0.3), (0, ym - t, h - 0.3)], BAR1, sw=0))
    seal = Dot(i.p(w / 2, ym, h), radius=0.09, color=TERRA)
    return VGroup(body, strap, seal)


PC2 = (-3.7, -1.25)


def l_share():
    return lbl("online share", (1.0, 1.6))


def l_4():
    return lbl("4%", (CX0 - 0.6, vy(SHARE[0])), 40)


def l_11(dy=0.0):
    return lbl("11%", (qx(Q19) - 0.25, vy(SHARE[Q19], dy) + 0.55), 40)


def l_census2():
    return lbl("per the Census Bureau", (1.0, 1.05), 36)


def b02_state():
    return VGroup(parcel(PC2, 1.2), axis(), hist(0, Q19), end_dot(Q19), l_share(), l_4(), l_11(), l_census2())


# ══════════════ B02: induction works — ten years of a steady line ══════════════
class B02_History(Scene):
    def construct(self):
        st0 = b01_end()
        self.add(st0)
        self.play(FadeOut(st0), run_time=0.45)
        pc, ax = parcel(PC2, 1.2), axis()
        rt = guard(self, 0.6)
        self.play(FadeIn(pc, shift=DOWN * 0.6), Create(ax), run_time=rt, rate_func=ease_in)
        until(self, "online shopping's share", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_share()), run_time=rt)
        until(self, "climbed slowly", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_4()), run_time=rt)
        rt = guard(self, 1.6)
        self.play(Create(hist(0, 20)), run_time=rt, rate_func=linear)
        until(self, "to about eleven", lead=0.3)
        rt = guard(self, 1.4)
        self.play(Create(hist(20, Q19)), run_time=rt, rate_func=linear)
        rt = guard(self, 0.4)
        self.play(FadeIn(end_dot(Q19), scale=1.6), FadeIn(l_11()), run_time=rt)
        until(self, "per the U.S. Census Bureau", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_census2()), run_time=rt)
        until(self, "Extend the line", lead=0.2)
        for q in (6, 18, 30):
            rt = guard(self, 0.55)
            self.play(Create(band(q)), run_time=rt)
        done(self)


def b01_end():
    return VGroup(ground(), plinth(), VGroup(*[day_page(k) for k in range(NDAYS + 1)]), plan_lines(), ghost_sun(), l_hume(),
                  l_custom(), cal_check())


# ══════════════ B03: the steps held — stationary ══════════════
DY3 = 1.0
SB_Y = -3.05
SB_K = 2.0


def steps():
    g = VGroup()
    for i in range(Q19):
        d = round(SHARE[i + 1] - SHARE[i], 1)
        h = max(0.05, d * SB_K)
        g.add(Rectangle(width=0.13, height=h, fill_color=(BAR1, BAR2)[i % 2], fill_opacity=1, stroke_width=0)
              .move_to([qx(i + 1), SB_Y + h / 2, 0]))
    return g


def step_band():
    return Rectangle(width=qx(Q19) - qx(1) + 0.4, height=0.5 * SB_K + 0.1, fill_color=PAD, fill_opacity=1, stroke_width=0) \
        .move_to([(qx(1) + qx(Q19)) / 2, SB_Y + (0.5 * SB_K + 0.1) / 2, 0]).set_z_index(-1)


def l_step():
    return lbl("each step", (-3.2, -2.55))


def l_stat():
    return lbl("stationary", (-3.2, -2.55))


def b03_state():
    return VGroup(axis(DY3), hist(0, Q19, DY3), end_dot(Q19, DY3), l_11(DY3), step_band(), steps(), l_stat())


class B03_Steps(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        pc, ax, ln, dt, ls, l4, l11, lc = st
        until(self, "Notice what held", lead=0.3)
        rt = guard(self, 0.6)
        self.play(FadeOut(VGroup(pc, ls, l4, lc)), run_time=rt)
        until(self, "it kept rising", lead=0.3)
        rt = guard(self, 0.8)
        self.play(VGroup(ax, ln, dt, l11).animate.shift(UP * DY3), run_time=rt)
        until(self, "Each quarter added", lead=0.3)
        sb = steps()
        rt = guard(self, 1.6)
        ls1 = l_step()
        self.play(LaggedStart(*[GrowFromEdge(b_, DOWN) for b_ in sb], lag_ratio=0.08), FadeIn(ls1), run_time=rt)
        until(self, "called stationary", lead=0.4)
        bd = step_band()
        rt = guard(self, 0.6)
        self.play(FadeIn(bd), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeOut(ls1), FadeIn(l_stat()), run_time=rt)
        until(self, "quietly relies on", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(sb, color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ══════════════ B04: ergodic — one shop over time = all the shops at once ══════════════
BASE4 = -1.2
LEFT_H = [1.7, 2.3, 1.4, 2.1, 1.8, 2.1]      # one shop, six periods: mean 1.9
RIGHT_H = [2.2, 1.5, 2.0, 1.6, 2.2]           # five shops, one moment: mean 1.9
AVG4 = BASE4 + sum(LEFT_H) / len(LEFT_H)
LX = [-4.0 + 0.6 * k for k in range(6)]
RX = [1.0 + 1.1 * k for k in range(5)]


def shop(c, s=0.55):
    w = d = 1.0
    h = 0.85
    i = rig_at(c[0], c[1], s, w, d)
    body = i.box(0, 0, 0, w, d, h, sw=3)
    for f in body:
        f.set_stroke(DEV_EDGE)
    awn = i.quad([(0.05, 0, h - 0.28), (w - 0.05, 0, h - 0.28), (w - 0.05, 0, h - 0.06), (0.05, 0, h - 0.06)], BAR2, stroke=DEV_EDGE, sw=2)
    door = i.quad([(0.35, 0, 0), (0.65, 0, 0), (0.65, 0, 0.45), (0.35, 0, 0.45)], BAR1, stroke=DEV_EDGE, sw=2)
    return VGroup(body, awn, door)


def bar4(x, h):
    return Rectangle(width=0.42, height=h, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([x, BASE4 + h / 2, 0])


def base4():
    return VGroup(Line([LX[0] - 0.4, BASE4, 0], [LX[-1] + 0.4, BASE4, 0], color=DEV_EDGE, stroke_width=4),
                  Line([RX[0] - 0.4, BASE4, 0], [RX[-1] + 0.4, BASE4, 0], color=DEV_EDGE, stroke_width=4))


def avg_line():
    return Line([LX[0] - 0.4, AVG4, 0], [RX[-1] + 0.4, AVG4, 0], color=INK, stroke_width=7).set_z_index(2)


def avg_dot():
    return Dot([(LX[-1] + RX[0]) / 2, AVG4, 0], radius=0.13, color=TERRA).set_z_index(3)


def l_time():
    return lbl("over time", ((LX[0] + LX[-1]) / 2, -1.8))


def l_across():
    return lbl("across shops", ((RX[0] + RX[-1]) / 2, -2.85))


def l_ergodic():
    return lbl("ergodic", (-0.2, 2.1), 46)


class B04_Shops(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        s0 = shop((-5.3, -1.9), 0.9)
        bs = base4()
        rt = guard(self, 0.6)
        self.play(FadeIn(s0, shift=UP * 0.3), Create(bs[0]), run_time=rt)
        until(self, "following one shop", lead=0.3)
        lb = [bar4(x, h) for x, h in zip(LX, LEFT_H)]
        rt = guard(self, 1.2)
        self.play(LaggedStart(*[GrowFromEdge(b_, DOWN) for b_ in lb], lag_ratio=0.25), FadeIn(l_time()), run_time=rt)
        until(self, "looking across all the shops", lead=0.4)
        shops = [shop((x, -2.05), 0.55) for x in RX]
        rb = [bar4(x, h) for x, h in zip(RX, RIGHT_H)]
        rt = guard(self, 1.2)
        self.play(Create(bs[1]), LaggedStart(*[FadeIn(VGroup(s_, b_), shift=UP * 0.3) for s_, b_ in zip(shops, rb)], lag_ratio=0.15),
                  FadeIn(l_across()), run_time=rt)
        until(self, "gives the same average", lead=0.6)
        rt = guard(self, 1.0)
        self.play(Create(avg_line()), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(avg_dot(), scale=1.6), FadeIn(l_ergodic()), run_time=rt)
        until(self, "stand in for the whole", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(*lb), color=None, scale_factor=1.05), run_time=rt)
        done(self)


def b04_state():
    return VGroup(shop((-5.3, -1.9), 0.9), base4(), *[bar4(x, h) for x, h in zip(LX, LEFT_H)],
                  *[shop((x, -2.05), 0.55) for x in RX], *[bar4(x, h) for x, h in zip(RX, RIGHT_H)],
                  avg_line(), avg_dot(), l_time(), l_across(), l_ergodic())


# ══════════════ B05: COVID — the line breaks ══════════════
PC5 = [(-4.75, -1.95), (-2.75, -1.95), (-3.75, -1.05)]


def hero5():
    return T("12% → 16%", 76, INK, bold=True).move_to([-3.4, 2.45, 0])


def l_census5():
    return lbl("per the Census Bureau", (-3.4, 1.5), 36)


def l_2020():
    return lbl("2020", (qx(NQ - 1) - 0.25, YB + 0.4), 38)


def b05_state():
    return VGroup(*[parcel(c, 0.95) for c in PC5], axis(), hist(0, NQ - 1), trend_band(), end_dot(NQ - 1),
                  hero5(), l_census5(), l_2020())


class B05_Break(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        p1 = parcel(PC5[0], 0.95)
        ax, ln = axis(), hist(0, Q19)
        rt = guard(self, 0.6)
        self.play(FadeIn(p1, shift=DOWN * 0.4), FadeIn(VGroup(ax, ln)), run_time=rt)
        until(self, "COVID changed", lead=0.3)
        rest = [parcel(c, 0.95) for c in PC5[1:]]
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(p_, shift=DOWN * 0.6) for p_ in rest], lag_ratio=0.4), run_time=rt, rate_func=ease_in)
        until(self, "shopping moved online", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Create(hist(Q19, NQ - 2)), run_time=rt)
        until(self, "In a single quarter", lead=0.2)
        bd = trend_band()
        rt = guard(self, 0.6)
        self.play(Create(bd), FadeIn(l_2020()), run_time=rt)
        until(self, "jumped", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Create(hist(NQ - 2, NQ - 1)), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.3)
        self.play(FadeIn(end_dot(NQ - 1), scale=1.6), run_time=rt)
        until(self, "to about sixteen", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(hero5(), scale=1.15), FadeIn(l_census5()), run_time=rt)
        until(self, "then one giant one", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(*rest), color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B06: the system changed ══════════════
MC = (-3.4, -0.95)
MW, MD, MH = 2.2, 1.8, 1.8
MS = 1.0
BELT_Y = -2.2
SMALL_X = [1.3, 2.3, 3.3, 4.3, 5.3]


def m_rig(c=MC, s=MS):
    return rig_at(c[0], c[1], s, MW, MD)


def machine(c=MC, s=MS):
    i = m_rig(c, s)
    body = i.box(0, 0, 0, MW, MD, MH)
    slot = i.quad([(0, 0.8, 0.35), (0, 1.0, 0.35), (0, 1.0, 1.45), (0, 0.8, 1.45)], BAR1, sw=0)
    chute = i.quad([(1.45, 0, 0.12), (2.0, 0, 0.12), (2.0, 0, 0.62), (1.45, 0, 0.62)], DARK_R, sw=0)
    return VGroup(body, slot, chute)


def knob(up=False, c=MC, s=MS):
    i = m_rig(c, s)
    return Circle(radius=0.2 * s, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to(i.p(0, 0.9, 1.2 if up else 0.6))


def lamp(on=False, c=MC, s=MS):
    i = m_rig(c, s)
    return Circle(radius=0.2 * s, fill_color=TERRA if on else GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4) \
        .move_to(i.p(1.0, 0, 1.3))


def belt():
    return VGroup(Polygon([-1.9, BELT_Y - 0.3, 0], [5.95, BELT_Y - 0.3, 0], [5.95, BELT_Y + 0.05, 0], [-1.9, BELT_Y + 0.05, 0],
                          fill_color=PAD, fill_opacity=1, stroke_width=0),
                  Line([-1.9, BELT_Y - 0.3, 0], [5.95, BELT_Y - 0.3, 0], color=DEV_EDGE, stroke_width=4))


def block(x, size=0.45, big=False):
    i = rig_at(x, BELT_Y + size * 0.5, 1.0, size, size)
    b = i.box(0, 0, 0, size, size, size, sw=4 if big else 3)
    if not big:
        for f in b:
            f.set_stroke(DEV_EDGE)
    return b.set_z_index(2)


BIG_X = -0.35


def l_system(c=(-3.1, 2.55)):
    return lbl("the system", c)


def l_changed():
    return lbl("changed", (-5.3, 1.8))


def b06_state():
    return VGroup(belt(), machine(), knob(True), *[block(x) for x in SMALL_X], block(BIG_X, 1.2, True), l_system(), l_changed())


class B06_System(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        bl, mc, kn = belt(), machine(), knob()
        sm = [block(x) for x in SMALL_X]
        rt = guard(self, 0.6)
        self.play(FadeIn(VGroup(bl, mc, kn), shift=UP * 0.3), run_time=rt)
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(b_, shift=RIGHT * 0.5) for b_ in reversed(sm)], lag_ratio=0.2), run_time=rt)
        until(self, "The system that made", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_system()), run_time=rt)
        until(self, "had changed", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Transform(kn, knob(True)), FadeIn(l_changed()), run_time=rt)
        until(self, "Hume saw", lead=0.2)
        bg = block(BIG_X, 1.2, True)
        rt = guard(self, 0.7)
        self.play(FadeIn(bg, shift=RIGHT * 0.8 + DOWN * 0.3), run_time=rt, rate_func=ease_in)
        until(self, "the past may be no rule", lead=0.3)
        rt = guard(self, 0.6)
        self.play(*[b_.animate.set_opacity(0.35) for b_ in sm], run_time=rt)
        done(self)


# ══════════════ B07: the model makes the same bet ══════════════
MB = (-4.35, -1.0)
CB_X = -2.3
CB_BASE, CB_H, CB_G, CB_N = -2.5, 0.42, 0.07, 5


def model_block():
    i = rig_at(MB[0], MB[1], 1.0, 1.5, 1.5)
    body = i.box(0, 0, 0, 1.5, 1.5, 0.9, "#2E2A26", "#1B1815", "#141210")
    ports = VGroup(*[i.box(1.5 * f, -0.16, 0.28, 0.24, 0.16, 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1) for f in (0.2, 0.6)])
    return VGroup(body, ports)


def conf_bar():
    return VGroup(*[Rectangle(width=0.6, height=CB_H, fill_color=(BAR1, BAR2)[k % 2], fill_opacity=1, stroke_width=0)
                    .move_to([CB_X, CB_BASE + CB_G + (CB_H + CB_G) * k + CB_H / 2, 0]) for k in range(CB_N)])


def l_model():
    return lbl("model", (MB[0], 1.15))


def l_conf():
    return lbl("confidence", (CB_X - 0.65, -3.0))


def scan(x):
    return Line([x, -2.4, 0], [x, 2.5, 0], color=TERRA, stroke_width=8).set_z_index(4)


def b07_state():
    return VGroup(model_block(), conf_bar(), axis(), hist(0, NQ - 1), trend_band(), end_dot(NQ - 1), l_model(), l_conf())


class B07_Model(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        mb, ax, ln = model_block(), axis(), hist(0, NQ - 2)
        rt = guard(self, 0.6)
        self.play(FadeIn(mb, shift=DOWN * 0.4), FadeIn(VGroup(ax, ln)), FadeIn(l_model()), run_time=rt)
        until(self, "makes the same bet", lead=0.3)
        sc = scan(qx(0))
        self.add(sc)
        rt = guard(self, 1.2)
        self.play(sc.animate.move_to([qx(NQ - 2), 0.05, 0]), run_time=rt, rate_func=linear)
        self.remove(sc)
        until(self, "trained on a stationary past", lead=0.3)
        cb = conf_bar()
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.15) for x in cb], lag_ratio=0.3), FadeIn(l_conf()), run_time=rt)
        until(self, "shipped into a moving present", lead=0.3)
        bd = trend_band()
        rt = guard(self, 0.7)
        self.play(Create(bd), run_time=rt)
        until(self, "After the change", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Create(hist(NQ - 2, NQ - 1)), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.3)
        self.play(FadeIn(end_dot(NQ - 1), scale=1.6), run_time=rt)
        until(self, "exactly as confident", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(cb, color=None, scale_factor=1.08), run_time=rt)
        done(self)


# ══════════════ B08: the rule — trust while the system is the same; when it changes, check ══════════════
MC8 = (-3.9, -1.0)
MS8 = 0.85
H8 = [(-0.9, -1.9), (-0.25, -1.62), (0.4, -1.4), (1.05, -1.1), (1.7, -0.9), (2.35, -0.6), (3.0, -0.38), (3.65, -0.1), (4.3, 0.15), (4.95, 0.42)]


def hist8():
    return VMobject(color=INK, stroke_width=8).set_points_as_corners([np.array([x, y, 0]) for x, y in H8]).set_z_index(2)


def axis8():
    return Line([-1.2, -2.35, 0], [5.4, -2.35, 0], color=DEV_EDGE, stroke_width=4)


def dot8():
    return Dot([H8[-1][0], H8[-1][1], 0], radius=0.12, color=TERRA).set_z_index(3)


def l_trust():
    return lbl("trust", (2.9, 1.75))


def chk8():
    return check(1.7, 1.75, 0.3)


def l_check():
    return lbl("check", (2.0, -2.9))


class B08_Rule(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        mc, kn, lp = machine(MC8, MS8), knob(False, MC8, MS8), lamp(False, MC8, MS8)
        ax, h8 = axis8(), hist8()
        rt = guard(self, 0.7)
        self.play(FadeIn(VGroup(mc, kn, lp), shift=UP * 0.3), FadeIn(ax), Create(h8), FadeIn(l_system((-3.9, 1.95))), run_time=rt)
        until(self, "the right bet", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(dot8(), scale=1.5), run_time=rt)
        until(self, "trust the pattern", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Create(chk8()), FadeIn(l_trust()), run_time=rt)
        until(self, "When the world changes", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Transform(kn, knob(True, MC8, MS8)), Transform(lp, lamp(True, MC8, MS8)), run_time=rt)
        until(self, "go back and check", lead=0.3)
        sc = Line([H8[-1][0] + 0.3, -2.3, 0], [H8[-1][0] + 0.3, 1.0, 0], color=TERRA, stroke_width=8).set_z_index(4)
        self.add(sc)
        rt = guard(self, 1.0)
        self.play(sc.animate.shift(LEFT * (H8[-1][0] - H8[0][0] + 0.6)), FadeIn(l_check()), run_time=rt, rate_func=linear)
        self.remove(sc)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Sun, B01_Custom, B02_History, B03_Steps, B04_Shops, B05_Break, B06_System, B07_Model, B08_Rule):
    _cls.play = ST.play
