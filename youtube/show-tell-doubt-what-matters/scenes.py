"""
Manim scenes for show-tell-doubt-what-matters (show-tell skill; INFO 7375 course film, SHOW-TELL-THREE-MOVES film 1).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py.

Radical doubt (Descartes), aimed by risk (Bear, 2026-09-27: "you can't doubt everything, but you should doubt
what your job depends on"). Cast: the BELIEF HOUSE (kraft blocks on a dark foundation) that Descartes tears
down once in his life (Meditations, 1641); the doubt LENS (an ink magnifier) over a CLAIM CARD, which yields a
CHECKLIST; a row of claim cards the lens can't keep up with while an HOURGLASS drains; the CABIN he lives in
while rebuilding (Discourse, 1637: a provisional code); the FOREST and a traveller PEG who walks one straight
line out; the RISK FLOOR (3 x 3: chance wrong x cost if wrong, not measured) with the CHAIR and everyday claim
cubes in the just-act corner and three dark TOWERS (triage score, dose, your number) that get the lens; and a
BALANCE where doubt is added until it matches the cost of being wrong.
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





# ═════════════════════════════ the film: doubt what your work depends on ═════════════════════════════
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


# ─── the doubt LENS: an ink magnifier ───
def lens(c, s=1.0):
    x, y = c
    R = 0.55
    a0, a1 = R * 0.7071, (R + 0.95) * 0.7071
    u, n = np.array([0.7071, -0.7071, 0]), np.array([0.7071, 0.7071, 0]) * 0.13
    p0, p1 = np.array([x + a0, y - a0, 0]), np.array([x + a1, y - a1, 0])
    handle = Polygon(p0 + n, p1 + n, p1 - n, p0 - n, fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    glass = Circle(radius=R, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=14).move_to([x, y, 0])
    glint = Dot([x - 0.2, y + 0.2, 0], radius=0.08, color=TERRA)
    return VGroup(handle, glass, glint).scale(s, about_point=np.array([x, y, 0])).set_z_index(8)


# ─── a CLAIM CARD: a white card on a dark stand, with a kraft offset under it ───
def card(c, s=1.0, lines=True):
    x, y = c
    w, h = 1.5, 2.0
    sh = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color=BOX_R, fill_opacity=1, stroke_width=0).move_to([x + 0.13, y + 0.07, 0])
    body = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([x, y + 0.2, 0])
    stand = Rectangle(width=w + 0.5, height=0.42, fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y - h / 2 - 0.01, 0])
    g = VGroup(sh, body, stand)
    if lines:
        g.add(*[Line([x - 0.45, y + 0.2 + dy, 0], [x + 0.45 - (0.3 if k == 2 else 0), y + 0.2 + dy, 0], color=BAR2, stroke_width=9)
                for k, dy in enumerate((0.45, 0.05, -0.35))])
    return g.scale(s, about_point=np.array([x, y, 0]))


# ══════════════ B00: Descartes tears down the house of beliefs, once ══════════════
HS = 1.05
HW, HD = 4.5, 1.3
BW, BH, NCOL, NLEV = 1.0, 0.7, 4, 3
KEEP = (0, 0)             # the one block left standing (column 0 = nearest, level 0)


def house_rig(cx=1.4, cy=-1.75):
    return rig_at(cx, cy, HS, HW, HD)


def foundation(i):
    return i.box(0, 0, 0, HW, HD, 0.35, DARK_TOP, DARK_L, DARK_R)


def hblock(i, col, lev):
    return i.box(0.1 + 1.1 * col, 0.15, 0.35 + 0.75 * lev, BW, BW, BH)


def crack(i, col, lev):
    x0, z0 = 0.1 + 1.1 * col, 0.35 + 0.75 * lev
    pts = [i.p(x0 + 0.3, 0.15, z0 + BH), i.p(x0 + 0.52, 0.15, z0 + 0.46), i.p(x0 + 0.36, 0.15, z0 + 0.28), i.p(x0 + 0.62, 0.15, z0 + 0.02)]
    return VMobject(color=DEV_EDGE, stroke_width=8).set_points_as_corners(pts).set_z_index(3)


def order():
    """Draw order: far columns first (larger x is further back), low levels first."""
    return [(c, l) for c in range(NCOL - 1, -1, -1) for l in range(NLEV)]


def house(i):
    blocks = {}
    for c, l in order():
        blocks[(c, l)] = hblock(i, c, l)
    return blocks


def keep_dot(i):
    x0, z0 = 0.1 + 1.1 * KEEP[0], 0.35 + 0.75 * KEEP[1]
    return Dot(i.p(x0 + BW / 2, 0.15 + BW / 2, z0 + BH), radius=0.11, color=TERRA).set_z_index(4)


def l_desc():
    return T("Descartes", 60, INK, bold=True).move_to([-3.95, 2.35, 0])


def l_med():
    return lbl("Meditations, 1641", (-3.95, 1.45))


def l_beliefs():
    return lbl("beliefs", (5.2, 0.4))


def b00_state():
    i = house_rig()
    return VGroup(foundation(i), hblock(i, *KEEP), keep_dot(i), l_desc(), l_med())


class B00_House(Scene):
    def construct(self):
        i = house_rig()
        fd = foundation(i)
        bl = house(i)
        self.play(FadeIn(fd, shift=UP * 0.3), run_time=0.4)
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(bl[k], shift=DOWN * 0.3) for k in order()], lag_ratio=0.12), run_time=rt)
        lb = l_beliefs()
        rt = guard(self, 0.4)
        self.play(FadeIn(lb), FadeIn(l_desc()), run_time=rt)
        until(self, "published in sixteen", lead=0.3)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_med()), run_time=rt)
        until(self, "any reason to doubt", lead=0.5)
        doomed = [k for k in order() if k != KEEP]
        cr = {k: crack(i, *k) for k in doomed}
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[Create(cr[k]) for k in doomed], lag_ratio=0.1), run_time=rt)
        until(self, "and rebuild from", lead=0.9)
        rt = guard(self, 1.6)
        top_first = sorted(doomed, key=lambda k: (-k[1], k[0]))
        self.play(LaggedStart(*[FadeOut(VGroup(bl[k], cr[k]), shift=UP * 0.45) for k in top_first], lag_ratio=0.1),
                  FadeOut(lb), run_time=rt)
        until(self, "after knowledge", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(keep_dot(i), scale=1.6), run_time=rt)
        done(self)


# ══════════════ B01: the course borrows the move — the lens turns doubt into a checklist ══════════════
CC1 = (-1.4, -0.2)
LENS1 = (-1.1, 0.55)
CB = (3.6, -0.1)


def clipboard(c=CB):
    x, y = c
    board = RoundedRectangle(width=2.4, height=3.1, corner_radius=0.12, fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([x, y, 0])
    paper = Rectangle(width=2.0, height=2.5, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=BAR1, stroke_width=3).move_to([x, y - 0.15, 0])
    clip = RoundedRectangle(width=0.95, height=0.36, corner_radius=0.08, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([x, y + 1.55, 0])
    rows = VGroup()
    for k in range(3):
        ry = row_y(k, c)
        rows.add(Square(side_length=0.4, fill_opacity=0, stroke_color=BAR1, stroke_width=4).move_to([x - 0.55, ry, 0]),
                 Line([x - 0.15, ry, 0], [x + 0.75, ry, 0], color=BAR2, stroke_width=9))
    return VGroup(board, paper, clip, rows)


def row_y(k, c=CB):
    return c[1] + 0.55 - 0.72 * k


def row_chk(k, c=CB):
    return check(c[0] - 0.55, row_y(k, c) + 0.02, 0.2, INK, 8).set_z_index(3)


def l_claim1():
    return lbl("claim", (CC1[0], -2.35))


def l_doubt1():
    return lbl("doubt", (-4.0, 1.7))


def l_check():
    return lbl("checklist", (CB[0], -2.35))


def b01_state():
    return VGroup(card(CC1), lens(LENS1), clipboard(), VGroup(*[row_chk(k) for k in range(3)]), l_claim1(), l_doubt1(), l_check())


class B01_Lens(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        cd = card(CC1)
        rt = guard(self, 0.5)
        self.play(FadeIn(cd, shift=UP * 0.3), FadeIn(l_claim1()), run_time=rt)
        until(self, "one question", lead=0.4)
        ln = lens((-4.4, 0.4))
        rt = guard(self, 0.4)
        self.play(FadeIn(ln, shift=RIGHT * 0.4), FadeIn(l_doubt1()), run_time=rt)
        until(self, "what would have to be true", lead=0.3)
        rt = guard(self, 0.9)
        self.play(ln.animate.shift(np.array([LENS1[0] + 4.4, LENS1[1] - 0.4, 0])), run_time=rt)
        until(self, "a list of things", lead=0.4)
        cb = clipboard()
        rt = guard(self, 0.5)
        self.play(FadeIn(cb, shift=DOWN * 0.4), FadeIn(l_check()), run_time=rt, rate_func=ease_in)
        until(self, "go and check", lead=0.6)
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[Create(row_chk(k)) for k in range(3)], lag_ratio=0.35), run_time=rt)
        done(self)


# ══════════════ B02: you can't doubt everything — the queue outruns the lens ══════════════
QY = -1.3
QS = 0.42
QX = [-5.45 + 1.05 * k for k in range(11)]
N0 = 7
HG = (3.9, 1.55)


def qcard(k):
    return card((QX[k], QY), QS, lines=False)


def q_chk(k):
    return check(QX[k], QY + 0.95, 0.17, INK, 7)


def hourglass(frac=0.0, c=HG):
    """frac: share of the sand that has run into the bottom bulb."""
    x, y = c
    Hh, Wd = 1.0, 0.8
    glass = VGroup(Polygon([x - Wd, y + Hh, 0], [x + Wd, y + Hh, 0], [x, y, 0], fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5),
                   Polygon([x - Wd, y - Hh, 0], [x + Wd, y - Hh, 0], [x, y, 0], fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5))
    caps = VGroup(Rectangle(width=2 * Wd + 0.4, height=0.22, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([x, y + Hh + 0.11, 0]),
                  Rectangle(width=2 * Wd + 0.4, height=0.22, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([x, y - Hh - 0.11, 0]))
    return VGroup(glass, sand(frac, c), caps)


def sand(frac, c=HG):
    x, y = c
    Hh, Wd = 1.0, 0.8
    top = max(0.02, 1.0 - frac) * 0.8          # top sand: a triangle down to the neck, height shrinking
    tp = Polygon([x - Wd * top * 0.92, y + Hh * top * 0.92, 0], [x + Wd * top * 0.92, y + Hh * top * 0.92, 0], [x, y + 0.04, 0],
                 fill_color=BOX_R, fill_opacity=1, stroke_width=0)
    b = max(0.02, frac) * 0.8                   # bottom sand: a trapezoid growing up from the base
    bp = Polygon([x - Wd * 0.92, y - Hh + 0.04, 0], [x + Wd * 0.92, y - Hh + 0.04, 0],
                 [x + Wd * (1 - b) * 0.92, y - Hh + 0.04 + Hh * b * 0.92, 0], [x - Wd * (1 - b) * 0.92, y - Hh + 0.04 + Hh * b * 0.92, 0],
                 fill_color=BOX_R, fill_opacity=1, stroke_width=0)
    return VGroup(tp, bp).set_z_index(1)


def l_claims():
    return lbl("claims", (-4.4, -2.85))


def l_time():
    return lbl("time", (5.35, HG[1]))


def lens_q(k):
    return (QX[k], QY + 0.3)


def b02_state():
    return VGroup(*[qcard(k) for k in range(11)], VGroup(*[q_chk(k) for k in range(3)]), hourglass(0.85), l_claims(), l_time(),
                  lens(lens_q(3), 0.75))


class B02_Queue(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        ln = st[1]
        self.play(FadeOut(VGroup(st[0], st[2], st[3], st[4], st[5], st[6])), run_time=0.4)
        qs = [qcard(k) for k in range(N0)]
        rt = guard(self, 0.7)
        self.play(LaggedStart(*[FadeIn(q, shift=UP * 0.3) for q in qs], lag_ratio=0.12), FadeIn(l_claims()),
                  ln.animate.scale(0.75).move_to(np.array([lens_q(0)[0] + 0.11, lens_q(0)[1] - 0.11, 0])), run_time=rt)
        until(self, "Every check costs time", lead=0.3)
        hg = hourglass(0.0)
        rt = guard(self, 0.4)
        self.play(FadeIn(hg), FadeIn(l_time()), run_time=rt)
        sd = hg[1]
        new = [qcard(k) for k in range(N0, 11)]
        for k in range(3):
            rt = guard(self, 0.25)
            self.play(Create(q_chk(k)), run_time=rt)
            a, b = k / 3.0 * 0.85, (k + 1) / 3.0 * 0.85

            def run(m, t, a=a, b=b):
                m.become(sand(a + (b - a) * t))
                return m
            rt = guard(self, 0.6)
            self.play(ln.animate.shift(RIGHT * 1.05), UpdateFromAlphaFunc(sd, run), run_time=rt)
            if k < 2:
                rt = guard(self, 0.3)
                self.play(FadeIn(new[2 * k], shift=LEFT * 0.4), FadeIn(new[2 * k + 1], shift=LEFT * 0.4), run_time=rt)
        until(self, "the work just waits", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(*new), color=None, scale_factor=1.06), run_time=rt)
        done(self)


# ══════════════ B03: Descartes' other house — the provisional code ══════════════
HX3 = -2.3            # the belief house moves left to make room for the cabin
CAB = (3.9, -1.1)
CBW, CBD, CBH = 1.8, 1.4, 1.1


def cabin_rig():
    return rig_at(CAB[0], CAB[1], 1.05, CBW, CBD)


def cabin(lit=False):
    i = cabin_rig()
    body = i.box(0, 0, 0, CBW, CBD, CBH)
    ym = CBD / 2
    roof = VGroup(i.quad([(0, 0, CBH), (0, CBD, CBH), (0, ym, CBH + 0.75)], BOX_L),
                  i.quad([(-0.08, -0.12, CBH - 0.06), (CBW + 0.12, -0.12, CBH - 0.06), (CBW + 0.12, ym, CBH + 0.75), (-0.08, ym, CBH + 0.75)], DARK_R))
    door = i.quad([(1.1, 0, 0), (1.5, 0, 0), (1.5, 0, 0.8), (1.1, 0, 0.8)], DARK_L, sw=3)
    win = window(lit)
    return VGroup(body, roof, door, win)


def window(lit):
    i = cabin_rig()
    return i.quad([(0.3, 0, 0.4), (0.8, 0, 0.4), (0.8, 0, 0.85), (0.3, 0, 0.85)], TERRA if lit else GHOST, stroke=DEV_EDGE, sw=3)


def rules():
    i = rig_at(1.7, -2.45, 0.65, 3.6, 1.0)
    return VGroup(*[i.page(0.1 + 1.25 * k, 0.0, 0.0, 1.0, 1.0) for k in range(3)])


def l_rebuild():
    return lbl("rebuilding", (-3.7, 1.2))


def l_disc():
    return lbl("Discourse, 1637", (3.9, 2.35))


def l_code():
    return lbl("provisional code", (4.3, -2.75))


REBUILT = [(1, 0), (2, 0)]


def b03_state():
    i = house_rig(HX3)
    return VGroup(foundation(i), hblock(i, 2, 0), hblock(i, 1, 0), hblock(i, *KEEP), keep_dot(i), cabin(True), rules(), l_disc(), l_code())


class B03_Cabin(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        i = house_rig(HX3)
        rem = VGroup(foundation(i), hblock(i, *KEEP), keep_dot(i))
        rt = guard(self, 0.5)
        self.play(FadeIn(rem, shift=UP * 0.3), FadeIn(l_rebuild()), run_time=rt)
        until(self, "Discourse on the Method", lead=0.3)
        cb = cabin(False)
        rt = guard(self, 0.6)
        self.play(FadeIn(cb, shift=DOWN * 0.6), FadeIn(l_disc()), run_time=rt, rate_func=ease_in)
        until(self, "pull down your house", lead=0.3)
        nb = [hblock(i, *k) for k in REBUILT]
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(b_, shift=DOWN * 0.8) for b_ in reversed(nb)], lag_ratio=0.4), run_time=rt, rate_func=ease_in)
        self.bring_to_front(rem[1], rem[2])
        until(self, "another house to live in", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Transform(cb[3], window(True)), run_time=rt)
        until(self, "a provisional code", lead=0.4)
        rl = rules()
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(r_, shift=RIGHT * 0.4) for r_ in rl], lag_ratio=0.3), FadeIn(l_code()), run_time=rt)
        done(self)


# ══════════════ B04: the traveller lost in a forest walks one straight line ══════════════
PEG = (-0.7, -0.55)
EXIT = (5.35, -0.55)
KEEP_OUT = [(-1.6, -0.75, 0.2, 1.6)]      # the clearing around the traveller and the 'lost' label (x0, y0, x1, y1)
FOREST_X1 = 3.3                            # the forest ends here; the straight line walks out into open ground


TREE_SH = "#A08868"      # tree shade: grey ~140, above GATE T's 120 text floor, dark enough for Gate V contrast


def tree(x, y, s=1.0):
    h, w = 0.95 * s, 0.4 * s
    left = Polygon([x, y + h, 0], [x - w, y, 0], [x, y, 0], fill_color=BOX_R, fill_opacity=1, stroke_width=0)
    right = Polygon([x, y + h, 0], [x, y, 0], [x + w, y, 0], fill_color=TREE_SH, fill_opacity=1, stroke_width=0)
    trunk = Rectangle(width=0.13 * s, height=0.24 * s, fill_color=TREE_SH, fill_opacity=1, stroke_width=0).move_to([x, y - 0.12 * s, 0])
    return VGroup(trunk, left, right)


def tree_spots():
    spots = []
    rows = [2.25, 1.05, -0.15, -1.75, -2.95]
    for r, y in enumerate(rows):
        for k in range(12):
            x = -5.7 + 1.05 * k + (0.5 if r % 2 else 0.0)
            if x > FOREST_X1:
                continue
            bad = any(x0 < x + 0.4 and x - 0.4 < x1 and y0 < y + 0.95 and y - 0.24 < y1 for x0, y0, x1, y1 in KEEP_OUT)
            if not bad:
                spots.append((x, y))
    return spots


def forest():
    sp = sorted(tree_spots(), key=lambda p: -p[1])        # back rows first
    return VGroup(*[tree(x, y) for x, y in sp])


def peg(c=PEG):
    x, y = c
    shadow = Ellipse(width=0.62, height=0.2, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([x, y - 0.02, 0])
    body = Polygon([x - 0.2, y, 0], [x + 0.2, y, 0], [x + 0.1, y + 0.5, 0], [x - 0.1, y + 0.5, 0], fill_color=INK, fill_opacity=1, stroke_width=0)
    head = Circle(radius=0.17, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([x, y + 0.66, 0])
    return VGroup(shadow, body, head).set_z_index(6)


def wander():
    x, y = PEG
    pts = [(x, y), (x - 0.7, y + 0.35), (x - 0.2, y + 0.75), (x + 0.45, y + 0.3), (x - 0.35, y - 0.3), (x - 0.9, y + 0.1), (x - 0.4, y + 0.55)]
    return VMobject(color=DIM, stroke_width=7).set_points_smoothly([np.array([a, b, 0]) for a, b in pts]).set_z_index(5)


def straight():
    return Line([PEG[0] + 0.35, PEG[1], 0], [EXIT[0] - 0.2, EXIT[1], 0], color=INK, stroke_width=9).set_z_index(5)


def exit_dot():
    return Dot([EXIT[0], EXIT[1], 0], radius=0.14, color=TERRA).set_z_index(6)


def l_lost():
    return lbl("lost", (-0.7, 1.3))


def l_on():
    return lbl("straight on", (4.95, 1.05))


def b04_state():
    return VGroup(forest(), straight(), exit_dot(), peg((EXIT[0] - 0.55, EXIT[1])), l_on())


class B04_Forest(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        fo = forest()
        pg = peg()
        lo = l_lost()
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(t_, shift=UP * 0.2) for t_ in fo], lag_ratio=0.02), FadeIn(pg), FadeIn(lo), run_time=rt)
        until(self, "wander from side to side", lead=0.4)
        wd = wander()
        rt = guard(self, 1.1)
        self.play(Create(wd), pg.animate.shift(LEFT * 0.25), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeOut(wd), pg.animate.shift(RIGHT * 0.25), run_time=rt)
        until(self, "Pick a direction", lead=0.3)
        sl = straight()
        rt = guard(self, 0.7)
        self.play(Create(sl), run_time=rt)
        until(self, "you'll likely end up", lead=0.2)
        rt = guard(self, 1.6)
        self.play(pg.animate.move_to(np.array([EXIT[0] - 0.55, EXIT[1] + 0.33, 0])), FadeOut(lo), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(exit_dot(), scale=1.6), FadeIn(l_on()), run_time=rt)
        until(self, "act on what's most probable", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(pg, color=None, scale_factor=1.12), run_time=rt)
        done(self)


# ══════════════ B05–B07: the RISK FLOOR — chance wrong x cost if wrong ══════════════
GS = 1.15
GN, GT_, GG = 3, 1.0, 0.1
GW = GN * GT_ + (GN + 1) * GG       # 3.4
GCEN = (-0.6, -1.25)
PLH = 0.3
RISK_FILL = {1: BOX_TOP, 2: BOX_TOP, 3: BOX_L, 4: BOX_L, 6: BOX_IN2, 9: BOX_FLOOR}


def grid_rig():
    return rig_at(GCEN[0], GCEN[1], GS, GW, GW)


def t0(i, j):
    return GG + (GT_ + GG) * i, GG + (GT_ + GG) * j


def tile(i, j, lit=False):
    r = grid_rig()
    x0, y0 = t0(i, j)
    fill = RISK_FILL[(i + 1) * (j + 1)] if lit else PAD
    return r.quad([(x0, y0, PLH), (x0 + GT_, y0, PLH), (x0 + GT_, y0 + GT_, PLH), (x0, y0 + GT_, PLH)], fill, stroke=DEV_EDGE, sw=2)


def plinth():
    return grid_rig().box(0, 0, 0, GW, GW, PLH, DARK_TOP, DARK_L, DARK_R)


def axis_x():
    r = grid_rig()
    return Arrow(r.p(0.2, -0.45, 0), r.p(GW + 0.2, -0.45, 0), color=BAR1, stroke_width=7, buff=0, max_tip_length_to_length_ratio=0.08)


def axis_y():
    r = grid_rig()
    return Arrow(r.p(-0.45, 0.2, 0), r.p(-0.45, GW + 0.2, 0), color=BAR1, stroke_width=7, buff=0, max_tip_length_to_length_ratio=0.08)


def l_cost():
    return lbl("cost if wrong", (3.55, -3.0))


def l_chance():
    return lbl("chance wrong", (-4.5, -3.0))


def l_notm():
    return lbl("not measured", (GCEN[0], 1.75), 36)


def floor():
    return VGroup(plinth(), *[tile(i, j, True) for j in range(GN - 1, -1, -1) for i in range(GN - 1, -1, -1)])


def b05_state():
    return VGroup(floor(), axis_x(), axis_y(), l_cost(), l_chance(), l_notm())


class B05_Grid(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        pl = plinth()
        tl = {(i, j): tile(i, j) for j in range(GN - 1, -1, -1) for i in range(GN - 1, -1, -1)}
        rt = guard(self, 0.7)
        self.play(FadeIn(pl, shift=UP * 0.3), LaggedStart(*[FadeIn(t_) for t_ in tl.values()], lag_ratio=0.06), run_time=rt)
        until(self, "how likely is it to be wrong", lead=0.4)
        ay = axis_y()
        rt = guard(self, 0.6)
        self.play(GrowArrow(ay), FadeIn(l_chance()), run_time=rt)
        until(self, "what would it cost", lead=0.4)
        ax = axis_x()
        rt = guard(self, 0.6)
        self.play(GrowArrow(ax), FadeIn(l_cost()), run_time=rt)
        until(self, "that's risk", lead=0.4)
        diag = sorted(tl.keys(), key=lambda k: (k[0] + 1) * (k[1] + 1))
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[Transform(tl[k], tile(*k, True)) for k in diag], lag_ratio=0.15), run_time=rt)
        until(self, "not a measured model", lead=0.5)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_notm()), run_time=rt)
        done(self)


def on_tile(i, j, x=0.0, y=0.0):
    """rig coords of a spot on tile (i, j), offset (x, y) from its near corner."""
    x0, y0 = t0(i, j)
    return x0 + x, y0 + y


def chair():
    r = grid_rig()
    x0, y0 = on_tile(0, 0, 0.2, 0.2)
    legs = VGroup(*[r.box(x0 + dx, y0 + dy, PLH, 0.1, 0.1, 0.55, DARK_TOP, DARK_L, DARK_R, sw=2)
                    for dx, dy in ((0.5, 0.0), (0.0, 0.0))])
    back_legs = VGroup(*[r.box(x0 + dx, y0 + dy, PLH, 0.1, 0.1, 0.55, DARK_TOP, DARK_L, DARK_R, sw=2)
                         for dx, dy in ((0.5, 0.5), (0.0, 0.5))])
    seat = r.box(x0 - 0.02, y0 - 0.02, PLH + 0.55, 0.64, 0.64, 0.12)
    back = r.box(x0 - 0.02, y0 + 0.5, PLH + 0.67, 0.64, 0.12, 0.62)
    return VGroup(back_legs, back, legs, seat)


CUBES = [(0, 1), (1, 0), (1, 1), (0, 2), (1, 2)]


def cube(i, j):
    r = grid_rig()
    x0, y0 = on_tile(i, j, 0.28, 0.28)
    return r.box(x0, y0, PLH, 0.45, 0.45, 0.45)


def l_act():
    return lbl("just act", (-4.5, -0.45))


def b06_state():
    return VGroup(b05_state()[:5], chair(), VGroup(*[cube(*k) for k in sorted(CUBES, key=lambda k: -(k[0] + k[1]))]), l_act())


class B06_Chair(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        rt = guard(self, 0.4)
        self.play(FadeOut(st[5]), run_time=rt)
        until(self, "The chair", lead=0.1)
        ch = chair()
        rt = guard(self, 0.7)
        self.play(FadeIn(ch, shift=DOWN * 0.9), run_time=rt, rate_func=ease_in)
        until(self, "land on the floor", lead=0.2)
        rt = guard(self, 0.4)
        self.play(ch.animate.shift(DOWN * 0.06), run_time=rt, rate_func=there_and_back)
        until(self, "Don't doubt it", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(ch, color=None, scale_factor=1.06), run_time=rt)
        until(self, "Most claims", lead=0.3)
        cs = [cube(*k) for k in sorted(CUBES, key=lambda k: -(k[0] + k[1]))]
        rt = guard(self, 1.0)
        self.play(LaggedStart(*[FadeIn(c_, shift=DOWN * 0.6) for c_ in cs], lag_ratio=0.2), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.3)
        self.play(FadeIn(l_act()), run_time=rt)
        done(self)


# ══════════════ B07: the costly claims rise, and get the lens ══════════════
TOWERS = [((2, 2), 1.5, "your number"), ((2, 1), 1.5, "dose"), ((2, 0), 1.5, "triage score")]
LENS7 = (-2.3, 2.45)


def tower(ij, h):
    r = grid_rig()
    x0, y0 = on_tile(*ij, 0.2, 0.2)
    return r.box(x0, y0, PLH, 0.6, 0.6, h, DARK_TOP, DARK_L, DARK_R)


def tower_lbl(name):
    ij, h = [(t[0], t[1]) for t in TOWERS if t[2] == name][0]
    r = grid_rig()
    x0, y0 = on_tile(*ij, 0.2, 0.2)
    top = r.p(x0 + 0.3, y0 + 0.3, PLH + h)
    t = lbl(name, (0, 0))
    return t.move_to(np.array([top[0] + 0.85 + t.width / 2, top[1] + 0.15, 0]))


def b07_state():
    return VGroup(b06_state(), VGroup(*[tower(ij, h) for ij, h, _ in TOWERS]), VGroup(*[tower_lbl(n) for _, _, n in TOWERS]), lens(LENS7, 0.9))


class B07_Towers(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        tws = []
        for ph, (ij, h, name) in zip(("a triage score", "a medication dose", "the number your job"), reversed(TOWERS)):
            until(self, ph, lead=0.3)
            tw = tower(ij, h)
            tws.append(tw)
            rt = guard(self, 0.55)
            self.play(FadeIn(tw, shift=UP * 0.7), FadeIn(tower_lbl(name)), run_time=rt)
        until(self, "someone pays for it", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(VGroup(*tws), color=None, scale_factor=1.05), run_time=rt)
        until(self, "Those get the doubt", lead=0.3)
        ln = lens((-5.0, 2.45), 0.9)
        rt = guard(self, 0.4)
        self.play(FadeIn(ln, shift=RIGHT * 0.3), run_time=rt)
        rt = guard(self, 0.8)
        self.play(ln.animate.shift(np.array([LENS7[0] + 5.0, 0, 0])), run_time=rt)
        done(self)


# ══════════════ B08: doubt in proportion to the cost of being wrong ══════════════
PIV = (0.0, 0.9)
ARM = 3.1
TIP = 0.16         # radians
DROP = ARM * np.sin(TIP)
PLATE_DY = 1.95


def post():
    x, y = PIV
    col = Rectangle(width=0.4, height=3.7, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([x, y - 1.85, 0])
    base = Polygon([x - 1.2, y - 3.95, 0], [x + 1.2, y - 3.95, 0], [x + 0.6, y - 3.55, 0], [x - 0.6, y - 3.55, 0],
                   fill_color=BAR1, fill_opacity=1, stroke_width=0)
    return VGroup(col, base)


def beam_bar():
    x, y = PIV
    return RoundedRectangle(width=2 * ARM + 0.4, height=0.24, corner_radius=0.1, fill_color=DARK_TOP, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([x, y, 0]).set_z_index(2)


def pivot_dot():
    return Dot([PIV[0], PIV[1], 0], radius=0.1, color=TERRA).set_z_index(3)


def pan(side):
    """side -1 = left, +1 = right: two hangers and a kraft plate, level position."""
    x, y = PIV[0] + side * ARM, PIV[1]
    py = y - PLATE_DY
    hang = VGroup(Line([x, y, 0], [x - 0.85, py, 0], color=INK, stroke_width=4), Line([x, y, 0], [x + 0.85, py, 0], color=INK, stroke_width=4))
    plate = Polygon([x - 1.0, py, 0], [x + 1.0, py, 0], [x + 0.75, py - 0.22, 0], [x - 0.75, py - 0.22, 0],
                    fill_color=BOX_R, fill_opacity=1, stroke_color=INK, stroke_width=4)
    return VGroup(hang, plate)


def plate_top(side, lift=0.0):
    return np.array([PIV[0] + side * ARM, PIV[1] - PLATE_DY + lift, 0])


def small_cost(lift=0.0):
    c = plate_top(-1, lift)
    return VGroup(Square(side_length=0.55, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c + UP * 0.275))


def big_cost(lift=0.0):
    c = plate_top(-1, lift)
    return VGroup(Rectangle(width=0.95, height=1.25, fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to(c + UP * 0.625))


def weight(k, lift=0.0):
    c = plate_top(1, lift) + UP * (0.15 + 0.32 * k)
    return Polygon(c + np.array([-0.45, -0.14, 0]), c + np.array([0.45, -0.14, 0]), c + np.array([0.3, 0.14, 0]), c + np.array([-0.3, 0.14, 0]),
                   fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4)


def l_costb():
    return lbl("cost if wrong", (-ARM, -2.45))


def l_doubtb():
    return lbl("doubt", (ARM, -2.45))


class B08_Balance(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.4)
        ps, bm, pd = post(), beam_bar(), pivot_dot()
        lp, rp = VGroup(pan(-1), small_cost()), VGroup(pan(1), weight(0))
        rt = guard(self, 0.7)
        self.play(FadeIn(VGroup(ps, bm, pd, lp, rp), shift=UP * 0.3), FadeIn(l_costb()), FadeIn(l_doubtb()), run_time=rt)
        until(self, "The more it costs", lead=0.3)
        bc = big_cost()
        rt = guard(self, 0.4)
        self.play(FadeOut(lp[1]), FadeIn(bc, shift=DOWN * 0.5), run_time=rt)
        lp.remove(lp[1])
        lp.add(bc)
        rt = guard(self, 0.6)
        self.play(Rotate(bm, TIP, about_point=np.array([PIV[0], PIV[1], 0])), lp.animate.shift(DOWN * DROP), rp.animate.shift(UP * DROP), run_time=rt)
        until(self, "the more doubt a claim gets", lead=0.3)
        ws = [weight(k, DROP) for k in (1, 2, 3)]
        rt = guard(self, 0.9)
        self.play(LaggedStart(*[FadeIn(w_, shift=DOWN * 0.6) for w_ in ws], lag_ratio=0.35), run_time=rt, rate_func=ease_in)
        rp.add(*ws)
        rt = guard(self, 0.6)
        self.play(Rotate(bm, -TIP, about_point=np.array([PIV[0], PIV[1], 0])), lp.animate.shift(UP * DROP), rp.animate.shift(DOWN * DROP), run_time=rt)
        until(self, "Costly to be wrong", lead=0.2)
        ln = lens((-5.4, 2.5), 0.8)
        rt = guard(self, 0.4)
        self.play(FadeIn(ln, shift=RIGHT * 0.3), run_time=rt)
        rt = guard(self, 0.7)
        self.play(ln.animate.shift(np.array([0.6, -1.1, 0])), run_time=rt)
        until(self, "before the world answers", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(ln, color=None, scale_factor=1.12), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_House, B01_Lens, B02_Queue, B03_Cabin, B04_Forest, B05_Grid, B06_Chair, B07_Towers, B08_Balance):
    _cls.play = ST.play
