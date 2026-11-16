"""
Manim scenes for show-tell-fluency-is-not-evidence (show-tell skill; INFO 7375 course film, ordered by Bear on
2026-09-28 in SHOW-TELL-FLUENCY-TRAP.md: the fluency trap from chapter 1).

SHOW-TELL: every beat is ONE drawn isometric illustration in the Claude palette, at most
a few words of label, and Liam's narration does the explaining. The ISO KIT block below
is the skill's shared drawing kit (brutalist.art/skills/make/show-tell/templates/iso_kit.py);
it is pasted, not imported, because the toolkit's Gate A copies only scenes.py. The kit, pacing
helpers and midpoint guard are copied from the sibling course film show-tell-five-things-the-model-cant-do
(with its larger end slack, _END = 0.15, for 24 fps frame rounding).

The fluency trap. One cast, whole film: the PAGE (an upright white sheet with grey lines: the artifact); the READER peg;
two GAUGES above him (confidence in the output, confidence in his own judgment), each a semicircle with an ink needle;
the WORLD, a dark block with one terracotta lamp (in the chapter's case it is the account); a MODEL block; and, in the
mechanism beats, the page drawn as two sheets, FORM in front and CONTENT behind, bound by one terracotta dot.
Stage one: the ragged lines smooth and the first needle climbs. Stage two: the second needle follows the first. Same shape:
a second page of the same shape, marked wrong, gets the same check. The case: a report with two checks, both needles high,
the account never visited; a non-fluent copy makes the reader ask and a line reaches the account. Not distrust: a stop board
between the reader and the page. The three moves: two tiles and a line from artifact to world with a question on it. Form and
content: a colleague's page moves as one bound pair; the model's page has no binding and the content slides out on its own
under a cross while the form stays tidy. Structural: pages on the hill of training data get checks; one slides onto the tail,
same shape, gets a cross, and the needle rises anyway. The anchor: a criterion card written while the page is still a ghost,
then held against it; without it the needle swings all the way. The close: the page's empty outline lifts off and a cross
stands between it and the world.
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



# ═════════════════════════════ the film: the shape of a sentence is not evidence ═════════════════════════════
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


def qmark(c, size=64):
    return T("?", size).move_to(P3(c))


def ring(c, r=1.5):
    """A grey ring that grows and fades: a pulse. Also a membership change for Gate A, whose stub ignores moves,
    text and removals inside a group (SKILL.md, choosing-the-right-claude-model B06)."""
    return Circle(radius=r, stroke_color=BAR1, stroke_width=6, fill_opacity=0).move_to(P3(c))


def pulse(self, c, r=1.5, rt=0.8):
    rg = ring(c, r)
    rt = guard(self, rt)                      # guard the grow AND the fade as one span
    Scene.play(self, GrowFromCenter(rg), run_time=rt * 0.5)
    Scene.play(self, FadeOut(rg), run_time=rt * 0.5)


# ─── the MODEL block and the WORLD block (a dark block with one terracotta lamp) ───
def model(c, s=1.0, tones=(AG_TOP, AG_L, AG_R)):
    i = rig_at(c[0], c[1], s, 1.5, 1.5)
    body = i.box(0, 0, 0, 1.5, 1.5, 0.95, *tones)
    ports = VGroup(*[i.box(1.5 * f, -0.16, 0.3, 0.24, 0.16, 0.32, GHOST, BOX_IN1, BOX_IN2, sw=1) for f in (0.2, 0.6)])
    return VGroup(body, ports)


def world(c, s=1.0):
    i = rig_at(c[0], c[1], s, 1.4, 1.4)
    body = i.box(0, 0, 0, 1.4, 1.4, 1.0, DARK_TOP, DARK_L, DARK_R)
    lamp = Dot(i.p(0.4, 0, 0.6), radius=0.1 * s, color=TERRA).set_z_index(3)
    return VGroup(body, lamp)


# ─── the PAGE: an upright sheet standing on the stage (the artifact) ───
PW, PH, PD = 1.8, 2.0, 0.12
LZ = (0.80, 0.66, 0.52, 0.38, 0.24)


def page_rig(c, s):
    """Rig whose standing face (the x-z plane at y = 0) has its base centred on screen point c."""
    return Iso(c[0] - PW * C30 * s / 2.0, c[1] - PW * 0.5 * s / 2.0, s)


def page_body(i, face=CARD, side=PAGE_R, top=PAGE_L, stroke=INK, sw=4):
    return VGroup(i.quad([(PW, 0, 0), (PW, PD, 0), (PW, PD, PH), (PW, 0, PH)], side, stroke, sw),
                  i.quad([(0, 0, PH), (PW, 0, PH), (PW, PD, PH), (0, PD, PH)], top, stroke, sw),
                  i.quad([(0, 0, 0), (PW, 0, 0), (PW, 0, PH), (0, 0, PH)], face, stroke, sw))


def tidy_lines(i, color=BAR2, sw=5):
    return VGroup(*[Line(i.p(0.2, 0, PH * z), i.p(PW - 0.2 - (0.45 if k == 4 else 0.0), 0, PH * z), color=color, stroke_width=sw)
                    for k, z in enumerate(LZ)])


RAG = [((0.2, 0.75), (0.95, 1.4)), ((0.2, 0.5), (0.7, 1.6)), ((0.35, 1.0), (1.2, 1.55)), ((0.2, 0.6), (0.85, 1.15), (1.3, 1.6)), ((0.2, 0.9),)]
JIT = (0.03, -0.04, 0.02, -0.03, 0.04)


def ragged_lines(i, color=BAR2, sw=5):
    segs = []
    for k, (z, row) in enumerate(zip(LZ, RAG)):
        for n, (a, b) in enumerate(row):
            dz = JIT[k] * (1 if n % 2 == 0 else -1)
            segs.append(Line(i.p(a, 0, PH * z + JIT[k]), i.p(b, 0, PH * z + JIT[k] + dz), color=color, stroke_width=sw))
    return VGroup(*segs)


def page(c, s=1.0, kind="tidy"):
    i = page_rig(c, s)
    g = VGroup(page_body(i))
    if kind == "tidy":
        g.add(tidy_lines(i))
    elif kind == "ragged":
        g.add(ragged_lines(i))
    return g


def ghost_page(c, s=1.0):
    """An unread page: the standing face as a grey outline on the stage colour, no lines."""
    i = page_rig(c, s)
    return VGroup(i.quad([(0, 0, 0), (PW, 0, 0), (PW, 0, PH), (0, 0, PH)], STAGE, BAR2, 4))


def shape_outline(c, s=1.0):
    """The page's shape and nothing else: its standing outline in ink, no fill."""
    i = page_rig(c, s)
    return Polygon(i.p(0, 0, 0), i.p(PW, 0, 0), i.p(PW, 0, PH), i.p(0, 0, PH), fill_opacity=0, stroke_color=INK, stroke_width=4)


def kraft_sheet(c, s=1.0, lines=0, stroke=INK):
    """A kraft sheet standing like the page (the CONTENT sheet, the criterion card, the stop board)."""
    i = page_rig(c, s)
    g = VGroup(page_body(i, BOX_L, BOX_R, BOX_TOP, stroke, 4))
    if lines:
        g.add(VGroup(*[Line(i.p(0.2, 0, PH * z), i.p(PW - 0.2, 0, PH * z), color=BAR1, stroke_width=5) for z in (0.62, 0.42)[:lines]]))
    return g


def page_tr(c, s=1.0):
    """Screen point of the standing face's top-right corner."""
    return (c[0] + PW * C30 * s / 2.0, c[1] + PW * 0.5 * s / 2.0 + PH * s)


# ─── the READER peg, tiles ───
def peg(x, y, s=1.0, badge=False):
    body = RoundedRectangle(width=0.62 * s, height=0.95 * s, corner_radius=0.2 * s, fill_color=BOX_L, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    head = Circle(radius=0.27 * s, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4) \
        .move_to([x, y + 0.475 * s + 0.27 * s + 0.06, 0])
    g = VGroup(body, head)
    if badge:
        g.add(Dot([x, y + 0.2 * s, 0], radius=0.09 * s, color=TERRA))
    return g


def tile(c, s=0.7):
    i = rig_at(c[0], c[1], s, 1.2, 1.2)
    return i.box(0, 0, 0, 1.2, 1.2, 0.45)


# ─── the GAUGES: a semicircle with an ink needle ───
GR = 1.15
A_LOW, A_MID, A_HIGH = 2.85, PI / 2, 0.30      # needle angles from the pivot (left = low, right = high)


def gauge_face(c, r=GR):
    pts = [P3((c[0] + r * np.cos(t), c[1] + r * np.sin(t))) for t in np.linspace(0.0, PI, 48)]
    return Polygon(*pts, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4)


def needle(c, ang, L=0.92):
    return VGroup(Line(P3(c), P3((c[0] + L * np.cos(ang), c[1] + L * np.sin(ang))), color=INK, stroke_width=9),
                  Dot(P3(c), radius=0.1, color=INK))


def gauge(c, ang=A_LOW, r=GR):
    return VGroup(gauge_face(c, r), needle(c, ang, 0.8 * r))


def swing(g, c, frm, to):
    """Rotate a gauge's needle (g[1]) about its pivot from angle frm to angle to."""
    return Rotate(g[1], angle=to - frm, about_point=P3(c))


# ─── the cast's home positions ───
RD = (-4.3, -1.5)
RDS = 1.3
PG = (-1.3, -2.3)        # the page, in front of the reader
WD = (4.4, -1.6)         # the model block, later the world / the account
GA = (-3.0, 1.55)        # gauge: confidence in the output
GB = (0.3, 1.55)         # gauge: confidence in your own judgment
LY = -3.05               # label row under the cast


def reader():
    return peg(RD[0], RD[1], RDS)


def l_reader():
    return lbl("reader", (RD[0], LY))


def l_model():
    return lbl("model", (WD[0], LY))


def l_world():
    return lbl("the world", (WD[0], LY))


def l_account():
    return lbl("the account", (WD[0], LY))


def l_ga():
    return lbl("output", (GA[0], 0.95))


def l_gb():
    return lbl("own judgment", (GB[0], 0.95))


# ══════════════ B00: two Botspeak pillars ══════════════
T1, T2 = (-4.4, 1.6), (-1.5, 1.6)
ASK_A, ASK_B = (-3.0, -1.95), (3.6, -2.05)
CRIT0 = (-2.75, -1.0)
PG_OUT = (2.2, -2.3)


def l_deleg():
    return lbl("delegation", (T1[0], 2.85))


def l_eval():
    return lbl("evaluation", (T2[0], 2.85))


def b00_state():
    return VGroup(reader(), l_reader(), model(WD), l_model(), tile(T1), l_deleg(), tile(T2), l_eval(),
                  kraft_sheet(CRIT0, 0.55, 2, DEV_EDGE), page(PG, 1.0, "ragged"))


class B00_TwoPillars(Scene):
    def construct(self):
        self.play(FadeIn(reader(), shift=UP * 0.3), FadeIn(l_reader()), FadeIn(model(WD), shift=UP * 0.3), FadeIn(l_model()), run_time=0.6)
        until(self, "Strategic delegation", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(tile(T1), shift=UP * 0.3), FadeIn(l_deleg()), run_time=rt)
        until(self, "what to ask", lead=0.2)
        ask = page(ASK_A, 0.5, "tidy")
        rt = guard(self, 0.35)
        self.play(FadeIn(ask, shift=UP * 0.2), run_time=rt)
        rt = guard(self, 0.9)
        self.play(ask.animate.move_to(P3(ASK_B)), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeOut(ask, shift=DOWN * 0.2), run_time=rt)
        until(self, "Critical evaluation", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(tile(T2), shift=UP * 0.3), FadeIn(l_eval()), run_time=rt)
        until(self, "what comes back", lead=0.3)
        pg = page(PG_OUT, 1.0, "ragged")
        rt = guard(self, 0.4)
        self.play(FadeIn(pg, shift=DOWN * 0.3), run_time=rt, rate_func=ease_in)
        rt = guard(self, 0.9)
        self.play(pg.animate.shift(P3(PG) - P3(PG_OUT)), run_time=rt)
        until(self, "criteria you set", lead=0.3)
        rt = guard(self, 0.4)
        self.play(FadeIn(kraft_sheet(CRIT0, 0.55, 2, DEV_EDGE), shift=UP * 0.2), run_time=rt)
        done(self)


# ══════════════ B01: neither pillar protects you from the trap ══════════════
def b01_state():
    return VGroup(reader(), l_reader(), model(WD), l_model(), page(PG, 1.0, "ragged"), gauge(GA, A_LOW), l_ga())


class B01_NeitherProtects(Scene):
    def construct(self):
        st = b00_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 model, 3 l_model, 4 tile1, 5 l_deleg, 6 tile2, 7 l_eval, 8 crit card, 9 page
        until(self, "neither of them", lead=0.6)
        ga = gauge(GA, A_LOW)
        rt = guard(self, 0.6)
        self.play(FadeOut(st[4]), FadeOut(st[5]), FadeOut(st[6]), FadeOut(st[7]), FadeOut(st[8]),
                  FadeIn(ga, shift=UP * 0.3), FadeIn(l_ga()), run_time=rt)
        until(self, "the trap", lead=0.2)
        pulse(self, (GA[0], GA[1] + 0.45), 1.5, 0.6)
        until(self, "its own section", lead=0.4)
        pulse(self, (PG[0], PG[1] + 1.1), 1.7)
        done(self)


# ══════════════ B02: stage one ══════════════
def l_fluent():
    return lbl("fluent", (PG[0], -3.1))


def b02_state():
    return VGroup(reader(), l_reader(), model(WD), l_model(), page(PG, 1.0, "tidy"), gauge(GA, A_HIGH), l_ga(), l_fluent())


class B02_StageOne(Scene):
    def construct(self):
        st = b01_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 model, 3 l_model, 4 page (ragged), 5 gauge A, 6 l_ga
        pg = st[4]
        until(self, "The prose smooths out", lead=0.3)
        i = page_rig(PG, 1.0)
        tl = tidy_lines(i)
        rt = guard(self, 0.7)
        self.play(FadeOut(pg[1]), FadeIn(tl), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_fluent()), run_time=rt)
        until(self, "the needle climbs", lead=0.3)
        rt = guard(self, 0.9)
        self.play(swing(st[5], GA, A_LOW, A_HIGH), run_time=rt)
        until(self, "not surprising", lead=0.3)
        pulse(self, (GA[0], GA[1] + 0.45), 1.5)
        done(self)


# ══════════════ B03: stage two, the trap ══════════════
LINK_A, LINK_B = (GA[0] + GR + 0.12, GA[1]), (GB[0] - GR - 0.12, GB[1])


def link():
    return Line(P3(LINK_A), P3(LINK_B), color=BAR1, stroke_width=7)


def b03_state():
    return VGroup(reader(), l_reader(), model(WD), l_model(), page(PG, 1.0, "tidy"), gauge(GA, A_HIGH), l_ga(),
                  gauge(GB, A_HIGH), l_gb(), link())


class B03_StageTwo(Scene):
    def construct(self):
        st = b02_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 model, 3 l_model, 4 page, 5 gauge A, 6 l_ga, 7 l_fluent
        self.play(FadeOut(st[7]), run_time=0.4)
        until(self, "your own", lead=0.5)
        gb = gauge(GB, A_LOW)
        rt = guard(self, 0.6)
        self.play(FadeIn(gb, shift=UP * 0.3), FadeIn(l_gb()), run_time=rt)
        until(self, "A second needle", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Create(link()), run_time=rt)
        rt = guard(self, 0.9)
        self.play(swing(gb, GB, A_LOW, A_HIGH), run_time=rt)
        until(self, "read well", lead=0.3)
        rt = guard(self, 0.5)
        self.play(Indicate(st[4], color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ══════════════ B04: any answer that arrives in the same shape ══════════════
PG2 = (1.15, -2.3)
WR = (2.6, -1.05)
CK1 = (-0.05, 0.05)
CK2 = (PG2[0] + 1.25, 0.3)


def l_same():
    return lbl("same shape", (PG2[0], -3.1))


def l_wrong():
    return lbl("wrong", (WR[0] + 0.15, WR[1] + 0.6))


def b04_state():
    return VGroup(reader(), l_reader(), model(WD), l_model(), page(PG, 1.0, "tidy"), gauge(GA, A_HIGH), l_ga(),
                  gauge(GB, A_HIGH), l_gb(), link(), page(PG2, 1.0, "tidy"), l_same(), cross(*WR, 0.24), l_wrong(),
                  check(*CK1, 0.28), check(*CK2, 0.28))


class B04_SameShape(Scene):
    def construct(self):
        st = b03_state()
        self.add(st)
        until(self, "evaluation booster", lead=0.4)
        rt = guard(self, 0.6)
        self.play(FadeIn(page(PG2, 1.0, "tidy"), shift=LEFT * 0.6), FadeIn(l_same()), run_time=rt)
        until(self, "the wrong evaluations", lead=0.3)
        rt = guard(self, 0.35)
        self.play(Create(cross(*WR, 0.24)), FadeIn(l_wrong()), run_time=rt)
        until(self, "a good answer", lead=0.3)
        rt = guard(self, 0.35)
        self.play(Create(check(*CK1, 0.28)), run_time=rt)
        until(self, "the same shape", lead=0.3)
        rt = guard(self, 0.35)
        self.play(Create(check(*CK2, 0.28)), run_time=rt)
        done(self)


# ══════════════ B05: the chapter's case, the report ══════════════
RC1, RC2 = (0.05, -0.9), (0.05, -1.7)


def l_deleted():
    return lbl("deleted", (1.3, RC1[1]))


def l_secured():
    return lbl("secured", (1.3, RC2[1]))


def b05_state():
    return VGroup(reader(), l_reader(), world(WD), l_account(), page(PG, 1.0, "tidy"), gauge(GA, A_HIGH), l_ga(),
                  gauge(GB, A_HIGH), l_gb(), link(), check(*RC1, 0.26), l_deleted(), check(*RC2, 0.26), l_secured())


class B05_TheReport(Scene):
    def construct(self):
        st = b04_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 model, 3 l_model, 4 page, 5 gauge A, 6 l_ga, 7 gauge B, 8 l_gb, 9 link,
        #     10 page2, 11 l_same, 12 wrong cross, 13 l_wrong, 14 check1, 15 check2
        self.play(FadeOut(st[10]), FadeOut(st[11]), FadeOut(st[12]), FadeOut(st[13]), FadeOut(st[14]), FadeOut(st[15]),
                  FadeOut(st[2]), FadeOut(st[3]), run_time=0.45)
        rt = guard(self, 0.5)
        self.play(FadeIn(world(WD), shift=UP * 0.3), FadeIn(l_account()),
                  swing(st[5], GA, A_HIGH, A_LOW), swing(st[7], GB, A_HIGH, A_LOW), run_time=rt)
        until(self, "The email had been deleted", lead=0.3)
        rt = guard(self, 0.35)
        self.play(Create(check(*RC1, 0.26)), FadeIn(l_deleted()), run_time=rt)
        until(self, "The account had been secured", lead=0.3)
        rt = guard(self, 0.35)
        self.play(Create(check(*RC2, 0.26)), FadeIn(l_secured()), run_time=rt)
        until(self, "trusted it", lead=0.3)
        rt = guard(self, 0.9)
        self.play(swing(st[5], GA, A_LOW, A_HIGH), swing(st[7], GB, A_LOW, A_HIGH), run_time=rt)
        until(self, "did not deceive", lead=0.2)
        rt = guard(self, 0.5)
        self.play(Indicate(st[4], color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ══════════════ B06: a non-fluent reader would have asked ══════════════
PGR = (1.7, -2.3)
QM6 = (RD[0], 0.55)
ARC_A, ARC_B = (-3.7, 0.4), (3.6, 0.25)


def l_nonfluent(c=PGR):
    return lbl("non-fluent", (c[0], -3.1))


def l_asked():
    return lbl("asked", (0.0, 1.85))


def ask_arc():
    return ArcBetweenPoints(P3(ARC_A), P3(ARC_B), angle=-PI / 3, color=BAR1, stroke_width=7)


def b06_state():
    return VGroup(reader(), l_reader(), world(WD), l_account(), page(PG, 1.0, "tidy"),
                  check(*RC1, 0.26), l_deleted(), check(*RC2, 0.26), l_secured())


class B06_NonFluent(Scene):
    def construct(self):
        st = b05_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 world, 3 l_account, 4 page, 5 gauge A, 6 l_ga, 7 gauge B, 8 l_gb, 9 link,
        #     10 check, 11 l_deleted, 12 check, 13 l_secured
        self.play(FadeOut(st[5]), FadeOut(st[6]), FadeOut(st[7]), FadeOut(st[8]), FadeOut(st[9]), run_time=0.45)
        i = page_rig(PG, 1.0)
        pg, tl, rl, ln = st[4], None, ragged_lines(i), l_nonfluent(PG)
        rt = guard(self, 0.6)
        self.play(FadeOut(pg[1]), FadeIn(rl), FadeIn(ln), run_time=rt)
        until(self, "asked the basic questions", lead=0.3)
        qm, arc, la = qmark(QM6), ask_arc(), l_asked()
        rt = guard(self, 0.3)
        self.play(FadeIn(qm, scale=1.6), run_time=rt)
        rt = guard(self, 0.9)
        self.play(Create(arc), FadeIn(la), run_time=rt)
        until(self, "the fluency was the trap", lead=0.3)
        tl = tidy_lines(i)
        rt = guard(self, 0.6)
        self.play(FadeOut(qm), FadeOut(arc), FadeOut(la), FadeOut(rl), FadeOut(ln), FadeIn(tl), run_time=rt)
        until(self, "did the work", lead=0.2)
        rt = guard(self, 0.6)
        self.play(Indicate(VGroup(st[4], st[10], st[12]), color=None, scale_factor=1.05), run_time=rt)
        done(self)


# ══════════════ B07: not distrust; stop ══════════════
LIFT = 0.5
BOARD = (-2.95, -2.1)


def l_useful():
    return lbl("more useful", (0.2, 1.15))


def l_stop():
    return lbl("stop", (BOARD[0], 0.4))


def b07_state():
    return VGroup(reader(), l_reader(), world(WD), l_account(), page((PG[0], PG[1] + LIFT), 1.0, "tidy"),
                  page(PGR, 1.0, "ragged"), l_nonfluent(), l_useful(), gauge(GA, A_MID), l_ga(), kraft_sheet(BOARD, 0.8), l_stop())


class B07_Stop(Scene):
    def construct(self):
        st = b06_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 world, 3 l_account, 4 page, 5 check, 6 l_deleted, 7 check, 8 l_secured
        self.play(FadeOut(st[5]), FadeOut(st[6]), FadeOut(st[7]), FadeOut(st[8]), run_time=0.4)
        rt = guard(self, 0.5)
        self.play(FadeIn(page(PGR, 1.0, "ragged"), shift=UP * 0.3), FadeIn(l_nonfluent()), run_time=rt)
        until(self, "more useful", lead=0.6)
        rt = guard(self, 0.7)
        self.play(st[4].animate.shift(UP * LIFT), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_useful()), run_time=rt)
        until(self, "epistemic work", lead=0.3)
        ga = gauge(GA, A_LOW)
        rt = guard(self, 0.5)
        self.play(FadeIn(ga, shift=UP * 0.3), FadeIn(l_ga()), run_time=rt)
        until(self, "sounds right", lead=1.3)
        rt = guard(self, 0.6)
        self.play(swing(ga, GA, A_LOW, A_MID), run_time=rt)
        until(self, "stop", lead=0.5)
        rt = guard(self, 0.35)
        self.play(FadeIn(kraft_sheet(BOARD, 0.8), shift=DOWN * 0.5), FadeIn(l_stop()), run_time=rt, rate_func=ease_in)
        done(self)


# ══════════════ B08: the three moves ══════════════
TD, TP = (0.5, 0.9), (2.9, 0.9)
LN_A, LN_B = (-0.3, -1.3), (2.95, -1.3)
QM8 = (1.3, -0.75)


def l_artifact():
    return lbl("artifact", (PG[0], -3.1))


def l_descartes():
    return lbl("Descartes", (TD[0], 2.0))


def l_popper():
    return lbl("Popper", (TP[0], 2.0))


def rel_line():
    return Line(P3(LN_A), P3(LN_B), color=BAR1, stroke_width=7)


def b08_state():
    return VGroup(reader(), l_reader(), world(WD), l_world(), page(PG, 1.0, "tidy"), l_artifact(),
                  tile(TD), l_descartes(), tile(TP), l_popper(), rel_line(), qmark(QM8))


class B08_ThreeMoves(Scene):
    def construct(self):
        st = b07_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 world, 3 l_account, 4 page, 5 ragged, 6 l_nonfluent, 7 l_useful, 8 gauge, 9 l_ga, 10 board, 11 l_stop
        self.play(*[FadeOut(st[k]) for k in (3, 5, 6, 7, 8, 9, 10, 11)], st[4].animate.shift(DOWN * LIFT), run_time=0.5)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_world()), FadeIn(l_artifact()), run_time=rt)
        until(self, "move from Descartes", lead=0.6)
        rt = guard(self, 0.5)
        self.play(FadeIn(tile(TD), shift=UP * 0.3), FadeIn(l_descartes()), run_time=rt)
        until(self, "move from Popper", lead=0.6)
        rt = guard(self, 0.5)
        self.play(FadeIn(tile(TP), shift=UP * 0.3), FadeIn(l_popper()), run_time=rt)
        until(self, "look at the world", lead=0.3)
        rt = guard(self, 0.9)
        self.play(Create(rel_line()), run_time=rt)
        until(self, "the relationship", lead=0.3)
        rt = guard(self, 0.35)
        self.play(FadeIn(qmark(QM8), scale=1.6), run_time=rt)
        done(self)


# ══════════════ B09: form and content, the human heuristic ══════════════
CO = (3.9, -1.5)
PS = (1.5, -2.3)                      # the two-sheet page, in front of the colleague
BOFF = (-0.43, 0.25)                  # the back (content) sheet sits one half-unit behind, in iso


def l_colleague():
    return lbl("colleague", (CO[0], LY))


def bind_dot(c):
    tr = page_tr(c, 1.0)
    return Dot(P3((tr[0] - PW * C30 / 2.0 - 0.21, tr[1] + 0.12)), radius=0.12, color=TERRA).set_z_index(4)


def two_sheets(c, bound=True):
    back = kraft_sheet((c[0] + BOFF[0], c[1] + BOFF[1]), 1.0)
    back.set_z_index(0)
    front = page(c, 1.0, "tidy")
    front.set_z_index(2)
    g = VGroup(back, front)
    if bound:
        g.add(bind_dot(c))
    return g


def l_form(c=PS):
    return lbl("form", (c[0] + 1.45, c[1] + 2.9))


def l_content(c=PS):
    return lbl("content", (c[0] - 1.5, c[1] + 3.2))


def b09_state():
    ts = two_sheets(PG)
    return VGroup(reader(), l_reader(), peg(CO[0], CO[1], RDS), l_colleague(), ts, l_form(PG), l_content(PG), check(*CK1, 0.28))


class B09_HumanHeuristic(Scene):
    def construct(self):
        st = b08_state()
        self.add(st)
        self.play(*[FadeOut(st[k]) for k in range(2, len(st))], run_time=0.45)
        until(self, "well-formed sentence", lead=0.4)
        rt = guard(self, 0.5)
        self.play(FadeIn(peg(CO[0], CO[1], RDS), shift=UP * 0.3), FadeIn(l_colleague()), run_time=rt)
        until(self, "clear, organized prose", lead=0.3)
        ts = two_sheets(PS)
        lf, lc = l_form(PS), l_content(PS)
        rt = guard(self, 0.6)
        self.play(FadeIn(ts[0], shift=UP * 0.3), FadeIn(ts[1], shift=UP * 0.3), FadeIn(lf), FadeIn(lc), run_time=rt)
        rt = guard(self, 0.3)
        self.play(FadeIn(ts[2], scale=1.8), run_time=rt)
        until(self, "evidence of the thinking", lead=0.3)
        grp = VGroup(ts, lf, lc)
        rt = guard(self, 0.9)
        self.play(grp.animate.shift(P3(PG) - P3(PS)), run_time=rt)
        until(self, "reliable", lead=0.6)
        rt = guard(self, 0.35)
        self.play(Create(check(*CK1, 0.28)), run_time=rt)
        done(self)


# ══════════════ B10: AI broke it, form and content independent ══════════════
BS = (PS[0] + BOFF[0], PS[1] + BOFF[1])      # where the content sheet starts (behind the front sheet)
BS_OUT = (-2.2, BS[1])                       # where it slides to, on its own
CX10 = (-1.1, 0.85)


def l_content10():
    return lbl("content", (BS_OUT[0], -3.1))


def b10_state():
    return VGroup(reader(), l_reader(), model(WD), l_model(), page(PS, 1.0, "tidy"), l_form(PS),
                  kraft_sheet(BS_OUT, 1.0), l_content10(), cross(*CX10, 0.24), gauge(GA, A_HIGH), l_ga())


class B10_Independent(Scene):
    def construct(self):
        st = b09_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 colleague, 3 l_colleague, 4 two sheets (bound), 5 l_form, 6 l_content, 7 check
        self.play(*[FadeOut(st[k]) for k in range(2, len(st))], run_time=0.45)
        rt = guard(self, 0.5)
        self.play(FadeIn(model(WD), shift=UP * 0.3), FadeIn(l_model()), run_time=rt)
        until(self, "The form comes from", lead=0.4)
        ts = two_sheets(PS, bound=False)
        rt = guard(self, 0.6)
        self.play(FadeIn(ts[0], shift=LEFT * 0.4), FadeIn(ts[1], shift=LEFT * 0.4), FadeIn(l_form(PS)), run_time=rt)
        until(self, "The content is whatever", lead=0.3)
        rt = guard(self, 1.0)
        self.play(ts[0].animate.shift(P3(BS_OUT) - P3(BS)), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_content10()), run_time=rt)
        until(self, "maximally wrong", lead=0.3)
        rt = guard(self, 0.35)
        self.play(Create(cross(*CX10, 0.24)), run_time=rt)
        until(self, "fluency alone", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(gauge(GA, A_HIGH), shift=UP * 0.3), FadeIn(l_ga()), run_time=rt)
        done(self)


# ══════════════ B11: structural, outputs that resemble correct outputs ══════════════
MD11 = (-4.6, -2.1)
HX0, HX1 = -4.0, 2.4
HPX = [-2.9, -1.5, -0.1]
HPS = 0.5


def hill_y(x):
    return -0.4 + 1.4 * np.exp(-((x + 1.5) / 1.5) ** 2)


def hill(n=44):
    xs = np.linspace(HX0, HX1, n)
    return VGroup(*[Line(P3((xs[k], hill_y(xs[k]))), P3((xs[k + 1], hill_y(xs[k + 1]))), color=INK, stroke_width=6) for k in range(n - 1)])


def tail_line():
    return Line(P3((HX1, hill_y(HX1))), P3((5.4, -0.4)), color=INK, stroke_width=6)


def hill_page(x):
    return page((x, hill_y(x)), HPS, "tidy")


def hill_check(x):
    return check(x + 0.75, hill_y(x) + 1.45, 0.22)


def l_model11():
    return lbl("model", (MD11[0], LY))


def l_training():
    return lbl("training data", (-1.5, -1.2))


def b11_state():
    return VGroup(model(MD11, 0.9), l_model11(), hill(), tail_line(), l_training(),
                  VGroup(*[hill_page(x) for x in HPX]), VGroup(*[hill_check(x) for x in HPX]))


class B11_Resemble(Scene):
    def construct(self):
        st = b10_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        rt = guard(self, 0.5)
        self.play(FadeIn(model(MD11, 0.9), shift=UP * 0.3), FadeIn(l_model11()), run_time=rt)
        until(self, "It is structural", lead=0.2)
        rt = guard(self, 1.1)
        self.play(Create(hill()), Create(tail_line()), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_training()), run_time=rt)
        until(self, "Where resemblance", lead=0.2)
        pgs = [hill_page(x) for x in HPX]
        rt = guard(self, 0.8)
        self.play(LaggedStart(*[FadeIn(p_, shift=UP * 0.3) for p_ in pgs], lag_ratio=0.25), run_time=rt)
        until(self, "works well", lead=0.3)
        rt = guard(self, 0.6)
        self.play(LaggedStart(*[Create(hill_check(x)) for x in HPX], lag_ratio=0.3), run_time=rt)
        done(self)


# ══════════════ B12: where they diverge, the same shape on the tail ══════════════
EP_A, EP_B = (0.9, hill_y(0.9)), (3.9, -0.4)
CX12 = (4.65, 1.05)
G12 = (2.3, 2.05)
GR12 = 0.9


def l_edge():
    return lbl("edge case", (EP_B[0], -1.2))


def l_ga12():
    return lbl("output", (G12[0], G12[1] - 0.65))


def l_sameshape12():
    return lbl("same shape", (4.7, 2.3))


class B12_EdgeCase(Scene):
    def construct(self):
        st = b11_state()
        self.add(st)
        until(self, "Where they diverge", lead=0.3)
        ep = page(EP_A, HPS, "tidy")
        rt = guard(self, 0.4)
        self.play(FadeIn(ep, shift=UP * 0.3), run_time=rt)
        until(self, "novel situations", lead=0.2)
        rt = guard(self, 1.0)
        self.play(ep.animate.shift(P3(EP_B) - P3(EP_A)), run_time=rt)
        rt = guard(self, 0.4)
        self.play(FadeIn(l_edge()), run_time=rt)
        until(self, "no basis", lead=2.2)
        rt = guard(self, 0.35)
        self.play(Create(cross(*CX12, 0.24)), run_time=rt)
        until(self, "the shape that makes you trust it", lead=0.4)
        g = gauge(G12, A_LOW, GR12)
        rt = guard(self, 0.5)
        self.play(FadeIn(g, shift=UP * 0.3), FadeIn(l_ga12()), run_time=rt)
        rt = guard(self, 0.8)
        self.play(swing(g, G12, A_LOW, A_HIGH), FadeIn(l_sameshape12()), run_time=rt)
        done(self)


def b12_state():
    return VGroup(b11_state(), page(EP_B, HPS, "tidy"), l_edge(), cross(*CX12, 0.24), gauge(G12, A_HIGH, GR12), l_ga12(), l_sameshape12())


# ══════════════ B13: before you read, the criterion ══════════════
PG13 = (1.8, -2.3)
CR13 = (-2.0, -1.6)
CRS = 0.55


def l_unread():
    return lbl("unread", (PG13[0], -3.1))


def l_criterion(c=CR13):
    return lbl("criterion", (c[0], -3.1))


def l_lowrisk():
    return lbl("low risk", (CR13[0], 0.2))


def b13_state():
    return VGroup(reader(), l_reader(), gauge(GA, A_LOW), l_ga(), ghost_page(PG13), l_unread(),
                  kraft_sheet(CR13, CRS, 2, DEV_EDGE), l_criterion(), l_lowrisk())


class B13_Before(Scene):
    def construct(self):
        st = b12_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        rt = guard(self, 0.6)
        self.play(FadeIn(reader(), shift=UP * 0.3), FadeIn(l_reader()), FadeIn(gauge(GA, A_LOW), shift=UP * 0.3), FadeIn(l_ga()), run_time=rt)
        until(self, "Before you read", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeIn(ghost_page(PG13), shift=UP * 0.3), FadeIn(l_unread()), run_time=rt)
        until(self, "specify what a wrong answer", lead=0.2)
        cr = kraft_sheet(CR13, CRS, 0, DEV_EDGE)
        rt = guard(self, 0.5)
        self.play(FadeIn(cr, shift=UP * 0.3), FadeIn(l_criterion()), run_time=rt)
        until(self, "specifically", lead=0.2)
        i = page_rig(CR13, CRS)
        ln1 = Line(i.p(0.2, 0, PH * 0.62), i.p(PW - 0.2, 0, PH * 0.62), color=BAR1, stroke_width=5)
        rt = guard(self, 0.4)
        self.play(Create(ln1), run_time=rt)
        until(self, "low risk", lead=0.3)
        ln2 = Line(i.p(0.2, 0, PH * 0.42), i.p(PW - 0.2, 0, PH * 0.42), color=BAR1, stroke_width=5)
        rt = guard(self, 0.4)
        self.play(Create(ln2), FadeIn(l_lowrisk()), run_time=rt)
        done(self)


# ══════════════ B14: then read; the anchor ══════════════
CR14 = (0.4, -2.05)


def l_anchor():
    return lbl("anchor", (GA[0], 2.95))


def l_fluency():
    return lbl("fluency", (GA[0], 2.95))


def b14_state():
    return VGroup(reader(), l_reader(), gauge(GA, A_HIGH), l_ga(), page(PG13, 1.0, "tidy"), l_fluency())


class B14_Anchor(Scene):
    def construct(self):
        st = b13_state()
        self.add(st)
        # st: 0 reader, 1 l_reader, 2 gauge A, 3 l_ga, 4 ghost page, 5 l_unread, 6 crit card, 7 l_criterion, 8 l_lowrisk
        until(self, "Then read it", lead=0.1)
        rt = guard(self, 0.6)
        self.play(FadeOut(st[4]), FadeIn(page(PG13, 1.0, "tidy")), FadeOut(st[5]), run_time=rt)
        until(self, "your anchor", lead=0.5)
        rt = guard(self, 0.7)
        self.play(st[6].animate.shift(P3(CR14) - P3(CR13)), st[7].animate.shift(P3((CR14[0], -3.1)) - P3((CR13[0], -3.1))),
                  FadeOut(st[8]), run_time=rt)
        la = l_anchor()
        rt = guard(self, 0.6)
        self.play(swing(st[2], GA, A_LOW, A_MID), FadeIn(la), run_time=rt)
        until(self, "Without it", lead=0.2)
        rt = guard(self, 0.5)
        self.play(FadeOut(st[6]), FadeOut(st[7]), run_time=rt)
        until(self, "except fluency", lead=0.3)
        rt = guard(self, 0.8)
        self.play(swing(st[2], GA, A_MID, A_HIGH), FadeOut(la), FadeIn(l_fluency()), run_time=rt)
        pulse(self, (GA[0], GA[1] + 0.45), 1.5, 0.7)
        done(self)


# ══════════════ B15: the shape of a sentence is not evidence ══════════════
P15A, P15B = (-2.6, -2.4), (0.2, -2.4)
S15 = 0.9
CK15 = (-1.4, -0.3)
CX15 = (1.35, -0.35)
SH15 = (-1.2, 0.5)
CX15B = (2.3, 0.5)


def l_shape():
    return lbl("the shape", (-3.3, 1.5))


def l_notevidence():
    return lbl("not evidence", (CX15B[0], 1.2))


class B15_NotEvidence(Scene):
    def construct(self):
        st = b14_state()
        self.add(st)
        self.play(FadeOut(st), run_time=0.45)
        ga, gb, lga, lgb = gauge(GA, A_HIGH), gauge(GB, A_HIGH), l_ga(), l_gb()
        rt = guard(self, 0.6)
        self.play(FadeIn(page(P15A, S15, "tidy"), shift=UP * 0.3), FadeIn(page(P15B, S15, "tidy"), shift=UP * 0.3),
                  FadeIn(world(WD), shift=UP * 0.3), FadeIn(l_world()), run_time=rt)
        rt = guard(self, 0.5)
        self.play(Create(check(*CK15, 0.26)), Create(cross(*CX15, 0.24)), FadeIn(ga), FadeIn(gb), FadeIn(lga), FadeIn(lgb), run_time=rt)
        until(self, "The shape of a sentence", lead=0.3)
        rt = guard(self, 0.5)
        self.play(FadeOut(ga), FadeOut(gb), FadeOut(lga), FadeOut(lgb), run_time=rt)
        sh = shape_outline(P15A, S15)
        rt = guard(self, 0.9)
        self.play(sh.animate.shift(P3(SH15) - P3(P15A)), FadeIn(l_shape()), run_time=rt)
        until(self, "not evidence", lead=0.3)
        rt = guard(self, 0.4)
        self.play(Create(cross(*CX15B, 0.26)), FadeIn(l_notevidence()), run_time=rt)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
for _cls in (B00_TwoPillars, B01_NeitherProtects, B02_StageOne, B03_StageTwo, B04_SameShape, B05_TheReport, B06_NonFluent,
             B07_Stop, B08_ThreeMoves, B09_HumanHeuristic, B10_Independent, B11_Resemble, B12_EdgeCase, B13_Before,
             B14_Anchor, B15_NotEvidence):
    _cls.play = ST.play
