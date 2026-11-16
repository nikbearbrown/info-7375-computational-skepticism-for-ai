"""
Manim scenes for show-tell-the-slice-you-can-see (show-tell skill; INFO 7375 course film, ordered by Bear on
2026-09-27 in SHOW-TELL-KANT.md as a companion to the three "moves" films: Kant, and humility about the slice we see).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py. The kit, pacing
helpers and midpoint guard are copied from the sibling course film show-tell-a-test-that-cant-fail
(itself from show-tell-induction-until-it-changes), with its larger end slack (_END = 0.15) for 24 fps frame rounding.

You only see a slice. The MIND (a kraft box with a lens) looks down-right through an upright kraft FRAME at
a dark THING (the thing in itself); what forms on the near side is its APPEARANCE, a kraft copy (Kant, 1781).
A sight line stops at the frame (a cross: know); a thought arc reaches the thing (a check: think); the thing
pulses: it is there. The frame lifts off the world and docks onto the mind ('space', 'time', 'cause'): the
frame is ours. An APPLE drops from a ledge and a dot rides an ORBIT (seen, seen); a grey link joins them
(inferred); 'cause' on the frame pulses (Hume's problem, Kant's answer). A kraft TELESCOPE between the mind
and the thing casts a pale wedge of view; a bigger lens sharpens the wedge's edges without widening it
(sharper, not bigger). Two panels: an ink WALL between a mind and a thing (in principle: Kant) and an ink
curve climbing toward a grey limit line it never touches (Bear's view: asymptotic). A dim ROOM with a kraft
LANTERN and a pale lit patch (the slice) and grey walls beyond (outside). A dark MODEL block in the lit patch
with its pages and a check (its slice); ghost outlines beyond the patch.
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



# ═════════════════════════════ the film: you only see a slice ═════════════════════════════
DEV_EDGE = "#917A55"      # dark kraft outline, SMALL objects only (GATE T counts grey < 120 as text)
PAD = "#E6E1D6"            # within Gate V's INK_DELTA of the stage
AG_TOP, AG_L, AG_R = "#2E2A26", "#1B1815", "#141210"   # the thing in itself / the model (darker than DARK_*, never fuses with ink)
RM_FLOOR, RM_WALL_A, RM_WALL_B = "#9EA2A9", "#B4B8BE", "#A9ADB4"   # the dim room (all greys above 120: never read as type)
RM_EDGE = "#C9CDD2"        # the faint wall-base edges
GHOST_OUT = "#C2C6CB"      # ghost outlines beyond the lit patch
LIT = "#F3E9D8"            # the lit patch (kraft top tone)


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


def shadow(c, w=1.6, h=0.5, dy=-0.75):
    return Ellipse(width=w, height=h, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(P3((c[0], c[1] + dy))).set_z_index(-1)


# ─── the MIND: a kraft box with a lens on its right-front face; it looks down-right (along -y) ───
MW, MD, MH = 1.4, 1.4, 1.3
MC = (-4.6, 0.2)


def mind(c=MC, s=1.0):
    i = rig_at(c[0], c[1], s, MW, MD)
    body = i.box(0, 0, 0, MW, MD, MH)
    lens = Circle(radius=0.3 * s, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4) \
        .move_to(i.p(MW * 0.5, 0, MH * 0.55)).set_z_index(2)
    return VGroup(body, lens)


def lens_pt(c=MC, s=1.0):
    i = rig_at(c[0], c[1], s, MW, MD)
    return i.p(MW * 0.5, 0, MH * 0.55)


# ─── the FRAME: four kraft bars in the plane y = 0 (parallel to the mind's lens face) ───
FX, FY, FS, FT = -0.35, -1.55, 2.3, 0.34


def frame(ox=FX, oy=FY, s=1.0, f=FS, t=FT):
    i = Iso(ox, oy, s)

    def q(x0, z0, x1, z1):
        return i.quad([(x0, 0, z0), (x1, 0, z0), (x1, 0, z1), (x0, 0, z1)], BOX_L, sw=3)
    return VGroup(q(0, 0, f, t), q(0, f - t, f, f), q(0, t, t, f - t), q(f - t, t, f, f - t))


DOCK = (lens_pt()[0] + 0.3, lens_pt()[1] - 0.2)
DOCK_S = 0.62


def frame_docked():
    f = frame()
    f.scale(DOCK_S).move_to(P3(DOCK))
    return f.set_z_index(3)


# ─── the THING in itself (dark) and its APPEARANCE (kraft) ───
TW_, TD_, TH_ = 1.8, 1.8, 1.5
TC = (3.9, -1.6)


def thing(c=TC, s=1.0):
    i = rig_at(c[0], c[1], s, TW_, TD_)
    return i.box(0, 0, 0, TW_, TD_, TH_, AG_TOP, AG_L, AG_R)


AW = 0.95
AC = (-2.3, -0.3)


def appearance(c=AC, s=1.0):
    i = rig_at(c[0], c[1], s, AW, AW)
    return i.box(0, 0, 0, AW, AW, AW)


def l_kant():
    return lbl("Kant, 1781", (-4.6, 2.75), 48)


def l_app():
    return lbl("appearance", (-2.3, -1.5))


def l_thing():
    return lbl("thing in itself", (3.9, -2.95))


def b00_state():
    return VGroup(mind(), l_kant(), frame(), thing(), appearance(), shadow(AC), l_app(), l_thing())


class B00_Split(Scene):
    def construct(self):
        m = mind()
        self.play(FadeIn(m, shift=RIGHT * 0.4), run_time=0.6)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_kant()), run_time=rt)
        until(self, "Kahnt split", lead=0.3)
        fr = frame()
        rt = guard(self, 0.7)
        self.play(Create(fr), run_time=rt)
        rt = guard(self, 0.6)
        th = thing()
        th.shift(RIGHT * 0.8)
        self.add(th)
        self.play(th.animate.shift(LEFT * 0.8), run_time=rt)
        until(self, "Phenomena", lead=0.3)
        ap = appearance()
        rt = guard(self, 0.6)
        self.play(GrowFromCenter(ap), FadeIn(l_app()), run_time=rt)
        until(self, "Noomenna", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(l_thing()), Indicate(th, color=None, scale_factor=1.04), run_time=rt)
        until(self, "near side", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(shadow(AC)), Indicate(ap, color=None, scale_factor=1.08), run_time=rt)
        done(self)


# ══════════════ B01: think but never know; the thing is there ══════════════
SIGHT_END = (-1.25, None)   # x where the sight line stops (just before the frame); y from the line


def sight_pts():
    a = lens_pt()
    b = P3(TC)
    x1 = SIGHT_END[0]
    y1 = a[1] + (b[1] - a[1]) * (x1 - a[0]) / (b[0] - a[0])
    return a, np.array([x1, y1, 0.0])


def sight():
    a, b = sight_pts()
    return Line(a, b, color=BAR1, stroke_width=7)


def k_cross():
    a, b = sight_pts()
    return cross(b[0] + 0.45, b[1] + 0.12, 0.24)


def l_know():
    return lbl("know", (-1.2, 1.0))


THOUGHT_END = (3.3, 1.2)


def thought():
    return ArcBetweenPoints(lens_pt(), P3(THOUGHT_END), angle=-PI / 2.2, color=BAR2, stroke_width=7)


def k_think():
    return check(3.9, 1.5, 0.3)


def l_think():
    return lbl("think", (3.9, 2.35))


def b01_state():
    return VGroup(b00_state(), sight(), k_cross(), l_know(), thought(), k_think(), l_think())


class B01_ThinkNotKnow(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        th = st[3]
        rt = guard(self, 0.7)
        self.play(Create(sight()), run_time=rt)
        until(self, "never know", lead=0.35)
        rt = guard(self, 0.4)
        self.play(Create(k_cross()), FadeIn(l_know()), run_time=rt)
        until(self, "In Kahnt's words", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(st[2], color=None, scale_factor=1.03), run_time=rt)
        until(self, "the power of thinking", lead=0.4)
        rt = guard(self, 0.9)
        self.play(Create(thought()), run_time=rt)
        rt = guard(self, 0.4)
        self.play(Create(k_think()), FadeIn(l_think()), run_time=rt)
        until(self, "never said", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(th, color=None, scale_factor=1.06), run_time=rt)
        until(self, "would be absurd", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(th, color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B02: the frame is ours: space, time, cause ══════════════
LX = -2.0


def l_space():
    return lbl("space", (LX, 2.75))


def l_time():
    return lbl("time", (LX, 2.15))


def l_cause():
    return lbl("cause", (LX, 1.55))


def b02_state():
    return VGroup(mind(), frame_docked(), thing(), appearance(), shadow(AC), l_app(), l_thing(), l_space(), l_time(), l_cause())


class B02_Frame(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        base = st[0]
        self.play(FadeOut(VGroup(st[1], st[2], st[3], st[4], st[5], st[6], base[1])), run_time=0.45)
        fr = base[2]
        until(self, "Not from the world", lead=0.3)
        rt = guard(self, 0.5)
        self.play(fr.animate.shift(UP * 0.6), run_time=rt)
        until(self, "From us", lead=0.2)
        rt = guard(self, 0.9)
        self.play(fr.animate.scale(DOCK_S).move_to(P3(DOCK)), run_time=rt)
        fr.set_z_index(3)
        until(self, "Space and time", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_space()), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_time()), run_time=rt)
        until(self, "cause and effect", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_cause()), run_time=rt)
        until(self, "already framed", lead=0.5)
        ap = base[4]
        rt = guard(self, 0.3)
        self.play(FadeOut(ap), run_time=rt)
        rt = guard(self, 0.5)
        self.play(GrowFromCenter(appearance()), run_time=rt)
        done(self)


# ══════════════ B03: gravity, inferred (Hume's problem, Kant's answer) ══════════════
LC = (1.5, 1.5)
LW, LD, LH = 1.2, 0.9, 0.45
APPLE_TOP = (1.5, 2.36)
APPLE_FLOOR = (1.5, -1.5)
OC = (4.3, 0.9)


def ledge():
    i = rig_at(LC[0], LC[1], 1.0, LW, LD)
    return i.box(0, 0, 0, LW, LD, LH)


def apple(c):
    body = Circle(radius=0.36, fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3(c))
    stem = Line([c[0], c[1] + 0.34, 0], [c[0] + 0.12, c[1] + 0.62, 0], color=INK, stroke_width=5)
    return VGroup(body, stem).set_z_index(2)


def apple_shadow():
    return shadow(APPLE_FLOOR, 1.3, 0.38, -0.46)


def sphere():
    return Circle(radius=0.45, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(P3(OC))


def orbit():
    return Ellipse(width=3.0, height=1.25, color=INK, stroke_width=5).move_to(P3(OC))


def moon():
    e = orbit()
    return Dot(e.point_from_proportion(0.0), radius=0.12, color=TERRA).set_z_index(3)


def l_seen_a():
    return lbl("seen", (1.5, -2.45))


def l_seen_o():
    return lbl("seen", (4.3, -0.55))


def link():
    return Line([1.95, -1.35, 0], [2.55, 0.3, 0], color=BAR2, stroke_width=7)


def l_inferred():
    return lbl("inferred", (3.2, -1.75))


def b03_state():
    return VGroup(mind(), frame_docked(), l_cause(), ledge(), apple(APPLE_FLOOR), apple_shadow(), l_seen_a(),
                  sphere(), orbit(), moon(), l_seen_o(), link(), l_inferred())


class B03_Gravity(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        self.play(FadeOut(VGroup(st[2], st[3], st[4], st[5], st[6], st[7], st[8])), run_time=0.45)
        rt = guard(self, 0.5)
        ap = apple(APPLE_TOP)
        self.play(FadeIn(ledge(), shift=UP * 0.3), FadeIn(ap), run_time=rt)
        until(self, "You see the apple", lead=0.2)
        rt = guard(self, 0.7)
        self.play(ap.animate.move_to(P3(APPLE_FLOOR) + np.array([0.0, 0.14, 0.0])), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.3)
        self.play(FadeIn(apple_shadow()), FadeIn(l_seen_a()), run_time=rt)
        until(self, "You see the orbit", lead=0.3)
        sp, ob = sphere(), orbit()
        rt = guard(self, 0.5)
        self.play(FadeIn(sp), Create(ob), run_time=rt)
        mn = moon()
        rt = guard(self, 1.3)
        self.add(mn)
        self.play(MoveAlongPath(mn, ob), FadeIn(l_seen_o()), run_time=rt, rate_func=linear)
        until(self, "The cause, you infer", lead=0.2)
        lk = link()
        rt = guard(self, 0.6)
        self.play(Create(lk), FadeIn(l_inferred()), run_time=rt)
        until(self, "David Hume", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(lk, color=None, scale_factor=1.1), run_time=rt)
        until(self, "the connection comes from us", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(st[9], color=None, scale_factor=1.2), run_time=rt)
        until(self, "textbook", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(lk, color=None, scale_factor=1.1), run_time=rt)
        done(self)


# ══════════════ B04: a sharper slice, not a bigger one ══════════════
TC4 = (4.4, -1.4)
TUC = (-0.6, -0.6)
TUW, TUD, TUH = 0.8, 2.6, 0.8


def tube_rig():
    return rig_at(TUC[0], TUC[1], 1.0, TUW, TUD)


def telescope():
    i = tube_rig()
    tube = i.box(0, 0, 0, TUW, TUD, TUH)
    post = Rectangle(width=0.18, height=1.15, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to(P3((TUC[0], TUC[1] - 1.35)))
    base = Ellipse(width=1.1, height=0.32, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to(P3((TUC[0], TUC[1] - 1.95)))
    return VGroup(base, post, tube)


def lens_big(scale=1.0):
    i = tube_rig()
    return Circle(radius=0.3 * scale, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4) \
        .move_to(i.p(TUW * 0.5, 0, TUH * 0.5)).set_z_index(2)


def wedge(edge=GHOST):
    i = tube_rig()
    a = i.p(TUW * 0.5, 0, TUH * 0.5) + np.array([0.3, 0.0, 0.0])
    return Polygon(a, [3.4, 0.55, 0], [3.4, -2.25, 0], fill_color=LIT, fill_opacity=1, stroke_color=edge, stroke_width=5).set_z_index(-1)


def l_sharper():
    return lbl("sharper", (2.0, 1.25))


def l_notbigger():
    return lbl("not bigger", (2.0, -2.8))


def b04_state():
    return VGroup(mind(), frame_docked(), thing(TC4), telescope(), lens_big(1.5), wedge(INK), l_sharper(), l_notbigger())


class B04_Telescope(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(VGroup(*[st[k] for k in range(2, 13)])), run_time=0.45)
        rt = guard(self, 0.5)
        self.play(FadeIn(thing(TC4), shift=LEFT * 0.3), run_time=rt)
        rt = guard(self, 0.6)
        ln = lens_big()
        self.play(FadeIn(telescope(), shift=UP * 0.3), FadeIn(ln), run_time=rt)
        wd = wedge()
        rt = guard(self, 0.7)
        self.play(FadeIn(wd), run_time=rt)
        until(self, "Kahnt says no", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(st[1], color=None, scale_factor=1.06), run_time=rt)
        until(self, "space, time and the categories", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(st[1], color=None, scale_factor=1.06), run_time=rt)
        until(self, "sharper slice", lead=0.6)
        rt = guard(self, 0.6)
        self.play(ln.animate.scale(1.5), wd.animate.set_stroke(INK, 5), FadeIn(l_sharper()), run_time=rt)
        until(self, "Not a bigger one", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(wd, color=None, scale_factor=1.03), FadeIn(l_notbigger()), run_time=rt)
        done(self)


# ══════════════ B05: two views: shut in principle (Kant) vs asymptotic (Bear's view) ══════════════
AX_Y5 = -2.1
LIM_Y = 1.65
CX0, CX1 = 1.0, 5.7
TOOL_X = [1.9, 3.1, 4.4]
MC5, TC5, WC5 = (-5.0, -1.3), (-1.9, 0.0), (-3.45, -0.55)


def curve_y(x):
    return 1.5 - 3.4 * np.exp(-0.85 * (x - CX0))


def axis5():
    return Line([CX0 - 0.2, AX_Y5, 0], [CX1 + 0.3, AX_Y5, 0], color=BAR1, stroke_width=5)


def limit():
    return Line([CX0 - 0.2, LIM_Y, 0], [CX1 + 0.3, LIM_Y, 0], color=BAR2, stroke_width=6)


def curve():
    xs = np.linspace(CX0, CX1, 40)
    return VMobject(color=INK, stroke_width=6).set_points_smoothly([[x, curve_y(x), 0] for x in xs])


def tool(x):
    i = rig_at(x, curve_y(x) - 0.62, 1.0, 0.5, 0.5)
    return i.box(0, 0, 0, 0.5, 0.5, 0.5)


def end_dot():
    return Dot([CX1, curve_y(CX1), 0], radius=0.12, color=TERRA).set_z_index(3)


def l_bear():
    return lbl("Bear's view", (3.4, 2.6), 48)


def l_asym():
    return lbl("asymptotic", (3.4, -2.65))


def wall():
    i = rig_at(WC5[0], WC5[1], 1.0, 0.3, 2.0)
    return i.box(0, 0, 0, 0.3, 2.0, 2.2, AG_TOP, AG_L, AG_R)


def l_principle():
    return lbl("in principle", (-3.45, -2.65))


def b05_state():
    return VGroup(axis5(), limit(), VGroup(*[tool(x) for x in TOOL_X]), curve(), end_dot(), l_bear(), l_asym(),
                  mind(MC5, 0.7), thing(TC5, 0.6), wall(), l_principle())


class B05_TwoViews(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        until(self, "Bear's view", lead=0.4)
        rt = guard(self, 0.5)
        self.play(FadeIn(l_bear()), Create(axis5()), Create(limit()), run_time=rt)
        la, lp = l_asym(), l_principle()
        until(self, "ever-better tools", lead=0.3)
        tl = [tool(x) for x in TOOL_X]
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(t_, shift=UP * 0.3) for t_ in tl], lag_ratio=0.4), run_time=rt)
        until(self, "approaching", lead=0.2)
        rt = guard(self, 1.2)
        self.play(Create(curve()), run_time=rt)
        until(self, "Asymptotic", lead=0.2)
        rt = guard(self, 0.4)
        self.play(FadeIn(end_dot(), scale=1.6), FadeIn(la), run_time=rt)
        until(self, "shut in principle", lead=0.6)
        rt = guard(self, 0.5)
        self.play(FadeIn(mind(MC5, 0.7), shift=RIGHT * 0.3), FadeIn(thing(TC5, 0.6), shift=LEFT * 0.3), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeIn(wall(), shift=DOWN * 0.5), FadeIn(lp), run_time=rt, rate_func=ease_in)
        until(self, "shut in practice", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(*tl), color=None, scale_factor=1.1), run_time=rt)
        until(self, "holds both", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(lp, color=None, scale_factor=1.1), Indicate(la, color=None, scale_factor=1.1), run_time=rt)
        done(self)


# ══════════════ B06: a lantern in a large dim room ══════════════
RC, RS, RW = (0.0, -0.75), 0.88, 5.6
RZ = 1.7


def room_rig():
    return rig_at(RC[0], RC[1], RS, RW, RW)


def room():
    i = room_rig()
    z = RZ
    floor = i.quad([(0, 0, 0), (RW, 0, 0), (RW, RW, 0), (0, RW, 0)], RM_FLOOR, sw=0)
    wall_r = i.quad([(RW, 0, 0), (RW, RW, 0), (RW, RW, z), (RW, 0, z)], RM_WALL_B, sw=0)
    wall_l = i.quad([(0, RW, 0), (RW, RW, 0), (RW, RW, z), (0, RW, z)], RM_WALL_A, sw=0)
    return VGroup(floor, wall_r, wall_l).set_z_index(0)


def wall_edges():
    i = room_rig()
    return VGroup(Line(i.p(RW, 0, 0), i.p(RW, RW, 0), color=RM_EDGE, stroke_width=5),
                  Line(i.p(0, RW, 0), i.p(RW, RW, 0), color=RM_EDGE, stroke_width=5)).set_z_index(1)


LAN = (2.8, 2.8)


def patch():
    i = room_rig()
    return Ellipse(width=4.2, height=2.4, fill_color=LIT, fill_opacity=1, stroke_width=0).move_to(i.p(LAN[0], LAN[1], 0)).set_z_index(1)


def lantern():
    i = room_rig()
    body = i.box(LAN[0] - 0.35, LAN[1] - 0.35, 0, 0.7, 0.7, 0.9)
    flame = Dot(i.p(LAN[0], LAN[1], 0.92), radius=0.16, color=TERRA)
    return VGroup(body, flame).set_z_index(2)


def l_slice():
    i = room_rig()
    p = i.p(LAN[0], LAN[1], 0)
    return lbl("the slice", (p[0], p[1] - 0.7)).set_z_index(4)


def l_outside():
    return lbl("outside", (2.1, 1.2)).set_z_index(4)


def b06_state():
    return VGroup(room(), patch(), lantern(), l_slice(), l_outside(), wall_edges())


class B06_Lantern(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        rm = room()
        self.play(FadeIn(rm), run_time=0.7)
        until(self, "see a slice", lead=0.6)
        ln = lantern()
        rt = guard(self, 0.5)
        self.play(FadeIn(ln, shift=DOWN * 0.6), run_time=rt, rate_func=ease_in)
        pt = patch()
        rt = guard(self, 0.7)
        self.play(GrowFromCenter(pt), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_slice()), run_time=rt)
        until(self, "outside the slice", lead=0.3)
        lo = l_outside()
        rt = guard(self, 0.4)
        self.play(FadeIn(lo), run_time=rt)
        until(self, "there is an outside at all", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(lo, color=None, scale_factor=1.15), run_time=rt)
        until(self, "Picture a lantern", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(ln[1], color=None, scale_factor=1.6), run_time=rt)
        until(self, "lit patch", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(pt, color=None, scale_factor=1.06), run_time=rt)
        until(self, "still there", lead=0.4)
        rt = guard(self, 0.8)
        self.play(Create(wall_edges()), run_time=rt)
        until(self, "there is an outside", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(lo, color=None, scale_factor=1.15), run_time=rt)
        done(self)


# ══════════════ B07: a model's confidence is about its slice ══════════════
MDL = (3.5, 1.7)


def model():
    i = room_rig()
    body = i.box(MDL[0] - 0.35, MDL[1] - 0.35, 0, 0.7, 0.7, 0.6, AG_TOP, AG_L, AG_R)
    ports = VGroup(*[i.box(MDL[0] - 0.35 + 0.7 * f, MDL[1] - 0.35 - 0.12, 0.18, 0.12, 0.12, 0.2, GHOST, BOX_IN1, BOX_IN2, sw=1) for f in (0.2, 0.6)])
    return VGroup(body, ports).set_z_index(2)


def pages():
    i = room_rig()
    return VGroup(i.page(1.3, 3.2, 0, 0.75, 0.95), i.page(2.1, 3.5, 0, 0.75, 0.95)).set_z_index(1.5)


def pages_check():
    i = room_rig()
    p = i.p(1.675, 3.675, 0.1)
    return check(p[0] + 0.07, p[1] + 0.02, 0.26).set_z_index(4)


def l_model():
    i = room_rig()
    return lbl("model", (2.85, -0.75)).set_z_index(4)


def l_itsslice():
    i = room_rig()
    p = i.p(LAN[0], LAN[1], 0)
    return lbl("its slice", (p[0], p[1] - 0.7)).set_z_index(4)


def ghosts():
    i = room_rig()
    out = VGroup()
    for (x, y) in ((0.8, 4.3), (4.7, 4.1)):
        b = i.box(x, y, 0, 0.6, 0.6, 0.55, RM_FLOOR, RM_FLOOR, RM_FLOOR, sw=3)
        b.set_stroke(GHOST_OUT, 3)
        out.add(b)
    return out.set_z_index(1)


class B07_Model(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        ls = st[3]
        until(self, "confidence about its slice", lead=0.9)
        rt = guard(self, 0.5)
        self.play(FadeIn(model(), shift=DOWN * 0.4), FadeIn(l_model()), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.5)
        self.play(FadeIn(pages(), shift=DOWN * 0.3), run_time=rt)
        rt = guard(self, 0.5)
        self.play(FadeOut(ls), FadeIn(l_itsslice()), Create(pages_check()), run_time=rt)
        until(self, "outside the patch", lead=0.3)
        rt = guard(self, 0.7)
        self.play(Create(ghosts()), run_time=rt)
        until(self, "lantern was lighting", lead=0.3)
        rt = guard(self, 0.6)
        self.play(Indicate(st[1], color=None, scale_factor=1.06), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_Split, B01_ThinkNotKnow, B02_Frame, B03_Gravity, B04_Telescope, B05_TwoViews, B06_Lantern, B07_Model):
    _cls.play = ST.play
