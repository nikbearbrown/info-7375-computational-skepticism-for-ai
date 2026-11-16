"""
kit.py — the lecture's shared drawing + pacing kit. NOT imported: assemble_scenes.py pastes it at the top of
scenes.py (Gate A copies only scenes.py). It is show-tell's iso_kit (palette, Iso projection, pacing helpers
until/finish) plus the midpoint guard (ST/guard/done) from show-tell-context-is-a-budget, plus a few lecture helpers.
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
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ─────────────── midpoint guard: GATE T and Gate V sample each clip at its MIDPOINT ───────────────
class ST:
    """No animation straddles the clip midpoint: one that would cross it is shortened to land before it, or
    starts just after it, so the midpoint frame is always a still. assemble_scenes.py attaches it to every
    beat class (the classes stay literal `(Scene)` for run.sh's scene discovery)."""
    def play(self, *anims, **kw):
        if not all(isinstance(a, Wait) for a in anims):
            kw["run_time"] = guard(self, float(kw.get("run_time", 1.0)))
        return Scene.play(self, *anims, **kw)


def guard(self, rt):
    """Returns the run time to use so an animation of length rt starting now does not straddle the midpoint.
    Call it BEFORE staging anything off-position."""
    tgt = _TARGET.get(type(self).__name__.split("_")[0], 0)
    if not tgt:
        return rt
    mid, t0 = tgt / 2.0, _elapsed(self)
    if t0 < mid + 0.06 and t0 + rt > mid - 0.06:
        room = mid - 0.08 - t0
        if room >= 0.6 * rt and room > 0.25:
            return room
        Scene.wait(self, max(0.02, mid + 0.08 - t0))
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


# ─────────────── lecture helpers ───────────────
MONO = "Menlo"


def M(s, size=32, color=INK):
    """Monospace text for real code/log lines (Menlo). Size floor 32 at this frame."""
    return Text(s, font=MONO, color=color, font_size=size)


def dim_arrow(a, b, color=INK, w=5, tip=0.16):
    """A dimension line with arrow tips at both ends (a, b are scene points)."""
    return DoubleArrow(np.array(a, dtype=float), np.array(b, dtype=float), buff=0, color=color, stroke_width=w,
                       tip_length=tip, max_tip_length_to_length_ratio=0.45)


# ══════════════════════════════ scenes_act1.py ══════════════════════════════
"""ACT I · Two Failures That Passed  (B01-B08, all Manim)

One cast for the act: the PATIENT DOT (a small grey dot, never a person), the HOSPITAL OUTLINE, the four TILES
(ASKED / DID / REPORTED / STATE), the ENVELOPE with one terracotta dot (the secret) and the VALID / RIGHT circles.
Numbers on screen are only the ones in factcheck/PRIMARIES.md (Wong et al. 2021; Shapira et al. 2026 Case #1).
"""

A1_XS = [-4.65, -1.55, 1.55, 4.65]           # four tile centres
A1_TY, A1_TH, A1_TW = 0.4, 3.2, 2.85          # tile centre y, height, width
A1_NAMES = ["ASKED", "DID", "REPORTED", "STATE"]


def a1_hospital(cx, cy, s=1.0, color=INK, sw=5, fill=True):
    """A hospital outline: body, plus-sign, door. Filled with the stage colour so ghost copies behind it hide."""
    w, h = 2.4 * s, 1.9 * s
    by = cy - 0.2 * s
    body = Rectangle(width=w, height=h, stroke_color=color, stroke_width=sw,
                     fill_color=STAGE, fill_opacity=1 if fill else 0).move_to([cx, by, 0])
    c, a = 0.34 * s, 0.12 * s
    ccy = by + 0.3 * s
    pts = [(-a, c), (a, c), (a, a), (c, a), (c, -a), (a, -a), (a, -c), (-a, -c), (-a, -a), (-c, -a), (-c, a), (-a, a)]
    cross = Polygon(*[[cx + px, ccy + py, 0] for px, py in pts], stroke_color=color, stroke_width=sw - 1, fill_opacity=0)
    door = Rectangle(width=0.5 * s, height=0.62 * s, stroke_color=color, stroke_width=sw - 1,
                     fill_opacity=0).move_to([cx, by - h / 2 + 0.31 * s, 0])
    return VGroup(body, cross, door)


def a1_env(cx, cy, w=1.5, h=1.0, color=INK):
    """An envelope outline (rectangle + V flap) and, separately, the terracotta dot that is the secret."""
    rect = Rectangle(width=w, height=h, stroke_color=color, stroke_width=5, fill_opacity=0).move_to([cx, cy, 0])
    f1 = Line([cx - w / 2, cy + h / 2, 0], [cx, cy + 0.08, 0], color=color, stroke_width=5)
    f2 = Line([cx + w / 2, cy + h / 2, 0], [cx, cy + 0.08, 0], color=color, stroke_width=5)
    dot = Dot([cx, cy - 0.24, 0], radius=0.11, color=TERRA)
    return VGroup(rect, f1, f2), dot


def a1_tiles(strong=()):
    """The four tiles: (outline, header) pairs. Outline-only, header in ink."""
    out = []
    for x, n in zip(A1_XS, A1_NAMES):
        box = RoundedRectangle(width=A1_TW, height=A1_TH, corner_radius=0.2, fill_opacity=0,
                               stroke_color=INK if n in strong else DIM, stroke_width=5).move_to([x, A1_TY, 0])
        hd = T(n, 34, INK, True).move_to([x, A1_TY + A1_TH / 2 - 0.45, 0])
        out.append((box, hd))
    return out


def a1_body(x, s, y=A1_TY - 0.2, size=40):
    """Centered multi-line tile text: one Text per line (Text() left-aligns its lines)."""
    ls = s.split("\n")
    g = VGroup(*[T(l, size).move_to([x, y + (len(ls) - 1) * 0.3 - i * 0.6, 0]) for i, l in enumerate(ls)])
    return g


def a1_dot_grid(cx, cy, cols, rows, sp, r, color=BAR1):
    dots = VGroup()
    x0 = cx - (cols - 1) * sp / 2
    y0 = cy + (rows - 1) * sp / 2
    for j in range(rows):
        for i in range(cols):
            dots.add(Dot([x0 + i * sp, y0 - j * sp, 0], radius=r, color=color))
    return dots


# ── B01 · a model in hundreds of hospitals, then 27,697 patients ──────────────────────────────────────────────
class B01_Hospitals(Scene):
    def construct(self):
        g2 = a1_hospital(-3.2, 0.45, 1.0, GHOST, 4)
        g1 = a1_hospital(-3.7, 0.2, 1.0, GHOST, 4)
        h = a1_hospital(-4.2, -0.05, 1.0, INK, 5)
        lab = T("sepsis model", 38).move_to([-3.2, -1.95, 0])
        self.add(h, lab)
        until(self, "hundreds of American hospitals", lead=0.2)
        self.add(g1, g2)
        g2.set_z_index(-2); g1.set_z_index(-1)
        self.play(FadeIn(g1), FadeIn(g2), run_time=0.5)
        until(self, "Then researchers", lead=0.4)
        frame = RoundedRectangle(width=5.5, height=3.2, corner_radius=0.2, fill_opacity=0, stroke_color=DIM,
                                 stroke_width=5).move_to([2.35, -0.1, 0])
        self.play(Create(frame), run_time=0.5)
        until(self, "checked it against", lead=0.3)
        dots = a1_dot_grid(2.35, -0.1, 16, 9, 0.3, 0.09)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.012, run_time=1.4))
        until(self, "twenty-seven thousand", lead=0.2)
        num = T("27,697 patients", 62).move_to([2.35, 2.45, 0])
        self.play(FadeIn(num), run_time=0.4)
        done(self)


# ── B02 · 1,709 of 2,552 ghosted; 6,971 of 38,455 alerts ──────────────────────────────────────────────────────
class B02_Missed(Scene):
    def construct(self):
        grid = a1_dot_grid(-3.5, 0.0, 10, 10, 0.34, 0.12)
        top = T("2,552 sepsis patients", 38).move_to([-3.5, 2.5, 0])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in grid], lag_ratio=0.008, run_time=0.9), FadeIn(top))
        until(self, "two of every three", lead=0.3)
        rng = np.random.RandomState(7)
        idx = list(rng.permutation(100)[:67])
        missed = [grid[i] for i in idx]
        self.play(AnimationGroup(*[d.animate.set_fill(BAR1, 0).set_stroke(DIM, 3) for d in missed], lag_ratio=0.01, run_time=1.0))
        until(self, "one thousand, seven hundred nine", lead=0.2)
        ml = T("1,709 missed · 67%", 38).move_to([-3.5, -2.2, 0])
        self.play(FadeIn(ml), run_time=0.4)
        until(self, "And it raised alerts", lead=0.5)
        bar = Rectangle(width=5.4, height=0.7, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([3.2, 0.5, 0])
        bl = T("38,455 hospitalizations", 36).move_to([3.2, 1.45, 0])
        self.play(Create(bar), FadeIn(bl), run_time=0.5)
        until(self, "eighteen percent", lead=0.4)
        part = Rectangle(width=0.97, height=0.7, stroke_width=0, fill_color=BAR1, fill_opacity=1).move_to([0.5 + 0.485, 0.5, 0])
        pl = T("6,971 alerts · 18%", 38).move_to([2.55, -0.5, 0])
        self.play(GrowFromEdge(part, LEFT), FadeIn(pl), run_time=0.6)
        done(self)


# ── B03 · two columns: the builders' measures vs the bedside ──────────────────────────────────────────────────
class B03_Measures(Scene):
    def construct(self):
        div = Line([0, -2.7, 0], [0, 2.7, 0], color=DIM, stroke_width=4)
        h1 = T("Builders' measures", 40).move_to([-3.1, 2.45, 0])
        h2 = T("At  the bedside", 40).move_to([3.1, 2.45, 0])
        self.add(div, h1, h2)
        rows = ["validated", "published", "cleared"]
        for i, r in enumerate(rows):
            y = 1.1 - i * 1.15
            lab = T(r, 40).move_to([-4.0, y, 0])
            ck = check(-1.75, y, 0.24, INK, 8)
            self.play(FadeIn(lab), Create(ck), run_time=0.45)
        until(self, "valid by the tests they chose", lead=0.2)
        dots = VGroup(*[Dot([x, 0.9, 0], radius=0.3, color=BAR1) for x in (2.0, 3.1, 4.2)])
        self.play(FadeIn(dots), run_time=0.4)
        until(self, "wrong about the question", lead=0.3)
        self.play(dots[0].animate.set_fill(BAR1, 0).set_stroke(DIM, 5), dots[1].animate.set_fill(BAR1, 0).set_stroke(DIM, 5),
                  run_time=0.6)
        until(self, "which patient is getting sicker", lead=0.8)
        ml = T("missed 2 of 3", 46).move_to([3.1, -0.35, 0])
        self.play(FadeIn(ml), run_time=0.4)
        done(self)


# ── B04 · an agent, a mailbox and a delete request ────────────────────────────────────────────────────────────
class B04_Request(Scene):
    def construct(self):
        chip = Square(side_length=1.5, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([-0.3, 0.2, 0])
        pins = VGroup()
        for k in (-0.4, 0.0, 0.4):
            pins.add(Line([-0.3 - 0.75, 0.2 + k, 0], [-0.3 - 1.1, 0.2 + k, 0], color=INK, stroke_width=6))
            pins.add(Line([-0.3 + 0.75, 0.2 + k, 0], [-0.3 + 1.1, 0.2 + k, 0], color=INK, stroke_width=6))
        core = Circle(radius=0.3, stroke_color=DIM, stroke_width=5).move_to([-0.3, 0.2, 0])
        al = T("agent", 42).move_to([-0.3, -1.3, 0])
        self.add(chip, pins, core, al)
        until(self, "Agents of Chaos", lead=0.6)
        cap = T("Agents of Chaos · Shapira et al., 2026", 32).move_to([0, -3.0, 0])
        self.play(FadeIn(cap), run_time=0.5)
        until(self, "asked an agent", lead=0.3)
        tile = RoundedRectangle(width=2.5, height=1.0, corner_radius=0.2, stroke_color=INK, stroke_width=5,
                                fill_opacity=0).move_to([-4.7, 0.2, 0])
        tt = T("delete", 40).move_to([-4.7, 0.2, 0])
        rl = T("request", 34).move_to([-4.7, 1.15, 0])
        a1 = Arrow([-3.4, 0.2, 0], [-1.7, 0.2, 0], buff=0, color=INK, stroke_width=5, tip_length=0.22)
        self.play(FadeIn(tile), FadeIn(tt), FadeIn(rl), Create(a1), run_time=0.7)
        until(self, "named Ash", lead=0.2)
        ash = T("Ash", 46).move_to([-0.3, -1.3, 0])
        self.play(FadeOut(al), FadeIn(ash), run_time=0.4)
        until(self, "delete an email", lead=0.3)
        env, dot = a1_env(4.5, 0.2)
        el = T("secret email", 38).move_to([4.5, -1.3, 0])
        a2 = Arrow([1.25, 0.2, 0], [3.55, 0.2, 0], buff=0, color=INK, stroke_width=5, tip_length=0.22)
        self.play(Create(env), FadeIn(el), Create(a2), run_time=0.7)
        until(self, "held a secret", lead=0.3)
        self.play(GrowFromCenter(dot), run_time=0.35)
        done(self)


# ── B05 · ASKED / DID / REPORTED, the reset and the report ────────────────────────────────────────────────────
class B05_Report(Scene):
    def construct(self):
        tiles = a1_tiles()
        for box, hd in tiles:
            self.add(box, hd)
        ask = a1_body(A1_XS[0], "delete\nemail")
        self.add(ask)
        slot = Rectangle(width=0.8, height=0.8, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([-5.3, -2.2, 0])
        x1 = Line([-5.6, -1.9, 0], [-5.0, -2.5, 0], color=DIM, stroke_width=5)
        x2 = Line([-5.6, -2.5, 0], [-5.0, -1.9, 0], color=DIM, stroke_width=5)
        sl = T("no delete tool", 34).move_to([-3.3, -2.2, 0])
        self.play(FadeIn(slot), Create(x1), Create(x2), FadeIn(sl), run_time=0.6)
        until(self, "reset its own local email setup", lead=0.4)
        did = a1_body(A1_XS[1], "local\nreset")
        self.play(FadeIn(did), tiles[1][0].animate.set_stroke(INK, 5), run_time=0.5)
        until(self, "and reported", lead=0.3)
        rep = a1_body(A1_XS[2], "reset\ncompleted", y=A1_TY + 0.05)
        quote = T("“Email account RESET completed.”", 32).move_to([3.0, -2.25, 0])
        self.play(FadeIn(rep), FadeIn(quote), tiles[2][0].animate.set_stroke(INK, 5), run_time=0.5)
        until(self, "claimed the secret", lead=0.3)
        ck = check(A1_XS[2], A1_TY - 0.75, 0.24, INK, 8)
        self.play(Create(ck), run_time=0.4)
        done(self)


# ── B06 · the real mailbox still holds the email: report and state disagree ───────────────────────────────────
class B06_State(Scene):
    def construct(self):
        tiles = a1_tiles()
        for box, hd in tiles:
            self.add(box, hd)
        ask = a1_body(A1_XS[0], "delete\nemail")
        did = a1_body(A1_XS[1], "local\nreset")
        rep = a1_body(A1_XS[2], "reset\ncompleted", y=A1_TY + 0.05)
        ck = check(A1_XS[2], A1_TY - 0.75, 0.24, INK, 8)
        for b in (0, 1, 2):
            tiles[b][0].set_stroke(INK, 5)
        self.add(ask, did, rep, ck)
        until(self, "the real mailbox", lead=0.3)
        self.play(tiles[3][0].animate.set_stroke(INK, 5), run_time=0.4)
        ml = T("mail server", 34).move_to([A1_XS[3], -1.65, 0])
        self.play(FadeIn(ml), run_time=0.3)
        until(self, "the email was still there", lead=1.3)
        env, dot = a1_env(A1_XS[3], A1_TY + 0.3, 1.4, 0.95)
        st = T("still there", 38).move_to([A1_XS[3], A1_TY - 0.65, 0])
        self.play(Create(env), FadeIn(st), run_time=0.5)
        self.play(GrowFromCenter(dot), run_time=0.3)
        until(self, "and false about the world", lead=0.5)
        arr = dim_arrow([A1_XS[2], -2.3, 0], [A1_XS[3], -2.3, 0])
        ne = T("≠", 54).move_to([(A1_XS[2] + A1_XS[3]) / 2, -2.85, 0])
        self.play(Create(arr), FadeIn(ne), run_time=0.5)
        self.play(Indicate(ne, scale_factor=1.25, color=INK), run_time=0.6)
        done(self)


# ── B07 · the composite patient: a chart, a score tag, a wait, a clot ─────────────────────────────────────────
class B07_Composite(Scene):
    def construct(self):
        board = Rectangle(width=2.2, height=3.1, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([-4.8, -0.2, 0])
        clip = Rectangle(width=0.9, height=0.34, stroke_color=INK, stroke_width=5, fill_color=STAGE, fill_opacity=1).move_to([-4.8, 1.37, 0])
        rows = VGroup(*[Line([-5.55, 0.6 - i * 0.6, 0], [-4.05, 0.6 - i * 0.6, 0], color=DIM, stroke_width=5) for i in range(4)])
        cl = T("composite patient", 36).move_to([-3.7, 2.45, 0])
        self.add(board, clip, rows, cl)
        # the vessel: leg (bottom) to lung (top)
        vessel = Line([3.6, -1.25, 0], [3.6, 1.3, 0], color=DIM, stroke_width=7)
        leg = RoundedRectangle(width=1.0, height=1.1, corner_radius=0.25, stroke_color=INK, stroke_width=5,
                               fill_opacity=0).move_to([3.6, -1.85, 0])
        lung = Ellipse(width=1.9, height=1.2, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([3.6, 1.9, 0])
        leg_l = T("leg", 36).move_to([5.1, -1.85, 0])
        lung_l = T("lung", 36).move_to([5.2, 1.9, 0])
        until(self, "She is a composite", lead=0.3)
        self.play(FadeIn(leg), FadeIn(lung), Create(vessel), FadeIn(leg_l), FadeIn(lung_l), run_time=0.7)
        clot = Dot([3.6, -1.85, 0], radius=0.16, color=TERRA)
        clot_l = T("clot", 36).move_to([2.2, -1.85, 0])
        self.play(GrowFromCenter(clot), FadeIn(clot_l), run_time=0.4)
        until(self, "forty-nine-year-old", lead=0.2)
        age = T("49 years", 40).move_to([-1.8, 1.55, 0])
        self.play(FadeIn(age), run_time=0.35)
        until(self, "swollen leg", lead=0.2)
        sw = T("swollen leg", 40).move_to([-1.8, 0.75, 0])
        self.play(FadeIn(sw), run_time=0.35)
        until(self, "scores her low-acuity", lead=0.3)
        tag = RoundedRectangle(width=3.7, height=0.85, corner_radius=0.2, stroke_color=INK, stroke_width=5,
                               fill_opacity=0).move_to([-1.8, -0.3, 0])
        tgt = T("LOW-ACUITY", 36, INK, True).move_to([-1.8, -0.3, 0])
        self.play(FadeIn(VGroup(tag, tgt), shift=DOWN * 0.3), run_time=0.45)
        until(self, "She waits", lead=0.1)
        clk = Circle(radius=0.55, stroke_color=INK, stroke_width=5).move_to([-2.5, -1.75, 0])
        hand = Line([-2.5, -1.75, 0], [-2.5, -1.35, 0], color=INK, stroke_width=6)
        hand2 = Line([-2.5, -1.75, 0], [-2.15, -1.75, 0], color=INK, stroke_width=6)
        wl = T("waits", 38).move_to([-1.05, -1.75, 0])
        self.play(Create(clk), Create(hand), Create(hand2), FadeIn(wl), run_time=0.5)
        self.play(Rotate(hand, angle=-PI, about_point=np.array([-2.5, -1.75, 0])), run_time=0.6)
        until(self, "moves to her lung", lead=0.5)
        self.play(clot.animate.move_to([3.6, 1.55, 0]), run_time=1.0)
        done(self)


# ── B08 · VALID vs RIGHT: two circles that do not coincide ────────────────────────────────────────────────────
class B08_ValidRight(Scene):
    def construct(self):
        valid = Circle(radius=1.7, stroke_color=INK, stroke_width=6).move_to([0, 0, 0])
        right = Circle(radius=1.7, stroke_color=DIM, stroke_width=6).move_to([0, 0, 0])
        target = Dot([0, 0, 0], radius=0.14, color=TERRA)
        vl = T("valid", 46).move_to([0, 2.45, 0])
        rl = T("right", 46).move_to([0, -2.45, 0])
        self.add(right, valid, vl, rl, target)
        self.wait(0.4)
        until(self, "and wrong about", lead=0.2)
        self.play(VGroup(valid, vl).animate.shift(LEFT * 3.1),
                  VGroup(right, target).animate.shift(RIGHT * 3.1),
                  rl.animate.move_to([3.1, 2.45, 0]), run_time=0.9)
        until(self, "That gap", lead=0.3)
        arr = dim_arrow([-1.4, 0, 0], [1.4, 0, 0])
        gl = T("gap", 40).move_to([0, 0.55, 0])
        self.play(Create(arr), FadeIn(gl), run_time=0.6)
        until(self, "tools to see", lead=0.9)
        self.play(Indicate(VGroup(arr, gl), scale_factor=1.15, color=INK), run_time=0.8)
        done(self)


# ══════════════════════════════ scenes_act2.py ══════════════════════════════
"""ACTS II-III · A Method, Not a Mood / Doubt Is an Inspection  (B09-B17, all Manim)

One cast for the two acts: the outlined CLAIM CARD (a rounded rectangle, ink outline, no fill) and the things that
test it: slots, a dial, curves, check marks. Terracotta is only ever a dot. No person is drawn anywhere.
Numbers on screen are the SEC Release 34-70694 figures (see factcheck/act2.md); nothing is invented.
"""
import math as _m


def a2_card(w, h, color=INK, sw=5):
    """Outline-only rounded card (no fill: Gate B fails fills behind text)."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.2, fill_opacity=0, stroke_color=color, stroke_width=sw)


def a2_polar(c, r, deg):
    return np.array([c[0] + r * _m.cos(deg * _m.pi / 180), c[1] + r * _m.sin(deg * _m.pi / 180), 0.0])


def a2_cross(x, y, s=0.32, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


# ── B09 · a method: moves you can perform, teach, check ───────────────────────────────────────────────────
class B09_Method(Scene):
    def construct(self):
        claim = a2_card(4.4, 1.1, DIM, 5).move_to([0, 2.15, 0])
        cl = T("A claim", 40).move_to([0, 2.15, 0])
        mood = DashedVMobject(Circle(radius=1.0, stroke_color=DIM, stroke_width=5), num_dashes=18).move_to([-3.6, -0.4, 0])
        ml = T("mood", 40, DIM).move_to([-3.6, -0.4, 0])
        self.add(claim, cl)
        self.play(Create(mood), FadeIn(ml), run_time=0.6)
        until(self, "I mean a method", lead=0.1)
        self.play(FadeOut(mood), FadeOut(ml), run_time=0.4)
        xs = [-3.8, 0.0, 3.8]
        names = ["Perform", "Teach", "Check"]
        slots, labs = [], []
        for x, n in zip(xs, names):
            s = a2_card(3.2, 1.7, DIM, 5).move_to([x, -0.75, 0])
            l = T(n, 42).move_to([x, -0.45, 0])
            slots.append(s)
            labs.append(l)
        arrows = [Arrow([-1.3, 1.55, 0], [-3.8, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2),
                  Arrow([0, 1.55, 0], [0, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2),
                  Arrow([1.3, 1.55, 0], [3.8, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)]
        self.play(*[Create(a) for a in arrows], *[FadeIn(s) for s in slots], *[FadeIn(l) for l in labs], run_time=0.7)
        cues = ["perform on a claim", "teach", "and check"]
        for x, s, c in zip(xs, slots, cues):
            until(self, c, lead=0.1)
            ck = check(x - 0.2, -1.2, 0.22, INK, 8)
            dot = Dot([x + 1.3, -0.02, 0], radius=0.12, color=TERRA)
            self.play(s.animate.set_stroke(INK, 8), Create(ck), FadeIn(dot), run_time=0.4)
        done(self)


# ── B10 · belief box + a conditions dial that drifts ──────────────────────────────────────────────────────
class B10_Conditions(Scene):
    def construct(self):
        C = np.array([3.3, 0.2, 0.0])
        box = a2_card(4.2, 1.9, DIM, 5).move_to([-3.6, 0.3, 0])
        b1 = T("Belief", 34, DIM).move_to([-3.6, 0.8, 0])
        b2 = T("chair holds me", 40).move_to([-3.6, 0.1, 0])
        self.add(box, b1, b2)
        bg = Arc(radius=1.4, start_angle=0, angle=PI, arc_center=C, color=DIM, stroke_width=6)
        safe = Arc(radius=1.4, start_angle=55 * DEGREES, angle=70 * DEGREES, arc_center=C, color=INK, stroke_width=12)
        hub = Dot(C, radius=0.1, color=INK)
        needle = Line(C, a2_polar(C, 1.15, 90), color=INK, stroke_width=7)
        cl = T("conditions", 38).move_to([3.3, -0.95, 0])
        self.play(Create(bg), Create(safe), FadeIn(hub), Create(needle), FadeIn(cl), run_time=0.8)
        rest = Arrow([-1.3, 0.3, 0], [1.3, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        rl = T("rests on", 34, DIM).move_to([0, 0.85, 0])
        until(self, "how you formed a belief", lead=0.8)
        self.play(Create(rest), FadeIn(rl), run_time=0.5)
        until(self, "so you notice", lead=0.2)
        self.play(Rotate(needle, angle=-75 * DEGREES, about_point=C.copy()), run_time=1.3)
        tip = Dot(a2_polar(C, 1.7, 15), radius=0.14, color=TERRA)
        nl = T("notice", 38).move_to([5.0, 1.55, 0])
        self.play(FadeIn(tip), FadeIn(nl), run_time=0.4)
        done(self)


# ── B11 · looks right rises, the urge to check falls ──────────────────────────────────────────────────────
class B11_Urge(Scene):
    def construct(self):
        ya = Arrow([-5.0, -2.2, 0], [-5.0, 2.5, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        xa = Arrow([-5.0, -2.2, 0], [3.6, -2.2, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        sch = T("schematic", 32, DIM).move_to([4.7, -2.75, 0])
        self.add(ya, xa, sch)

        def sg(t):
            return 1.0 / (1.0 + _m.exp(-9.0 * (t - 0.5)))

        up = ParametricFunction(lambda t: np.array([-4.4 + 7.2 * t, -1.5 + 3.0 * sg(t), 0.0]), t_range=[0, 1, 0.01],
                                color=INK, stroke_width=8)
        dn = ParametricFunction(lambda t: np.array([-4.4 + 7.2 * t, 1.5 - 3.0 * sg(t), 0.0]), t_range=[0, 1, 0.01],
                                color=DIM, stroke_width=8)
        l_up = T("looks right", 38).move_to([4.6, 1.5, 0])
        l_dn = T("urge to check", 38, DIM).move_to([4.6, -1.5, 0])
        until(self, "checking what looks right", lead=0.2)
        self.play(Create(up), run_time=1.5)
        self.play(FadeIn(l_up), run_time=0.3)
        until(self, "the urge to run them", lead=1.0)
        self.play(Create(dn), run_time=1.5)
        self.play(FadeIn(l_dn), run_time=0.3)
        until(self, "is weakest", lead=0.2)
        cross = Dot([-0.8, 0.0, 0], radius=0.16, color=TERRA)
        ring = Circle(radius=0.42, stroke_color=INK, stroke_width=5).move_to([-0.8, 0.0, 0])
        self.play(FadeIn(cross), Create(ring), run_time=0.4)
        until(self, "It is confidence", lead=0.2)
        conf = T("confidence", 50, INK, bold=True).move_to([0.2, 2.8, 0])
        self.play(FadeIn(conf), run_time=0.4)
        done(self)


# ── B12 · four moves, four questions; the load-test beam ──────────────────────────────────────────────────
class B12_FourMoves(Scene):
    def construct(self):
        xs = [-4.65, -1.55, 1.55, 4.65]
        names = ["Doubt", "Induction", "Falsify", "Slice"]
        qs = ["What would\nbreak it?", "What has\nchanged?", "What would\nrefute it?", "What is\nunseen?"]
        cues = ["Doubt.", "Induction.", "Falsifiability.", "And the slice"]
        cards = []
        for x, n, q, c in zip(xs, names, qs, cues):
            until(self, c, lead=0.15)
            card = a2_card(2.85, 2.6).move_to([x, 0.9, 0])
            nm = T(n, 40).move_to([x, 1.75, 0])
            qq = T(q, 32, DIM).move_to([x, 0.65, 0])
            dot = Dot([x + 1.05, 2.0, 0], radius=0.1, color=TERRA)
            self.play(FadeIn(card), FadeIn(nm), FadeIn(qq), FadeIn(dot), run_time=0.4)
            cards.append(card)
        until(self, "structural engineer", lead=0.3)
        beam = Rectangle(width=6.0, height=0.28, stroke_color=INK, stroke_width=6, fill_opacity=0).move_to([0, -2.25, 0])
        sup = VGroup(*[Polygon([x, -2.41, 0], [x - 0.35, -2.95, 0], [x + 0.35, -2.95, 0], stroke_color=DIM, stroke_width=5,
                               fill_opacity=0) for x in (-2.3, 2.3)])
        self.play(FadeIn(beam), Create(sup), run_time=0.4)
        until(self, "load-test a beam", lead=0.6)
        load = Arrow([-1.0, -0.7, 0], [-1.0, -2.02, 0], buff=0, color=INK, stroke_width=7, tip_length=0.25)
        ll = T("load test", 36).move_to([1.2, -1.3, 0])
        self.play(Create(load), FadeIn(ll), run_time=0.5)
        ck = check(2.9, -1.3, 0.22, INK, 8)
        self.play(Create(ck), run_time=0.3)
        done(self)


# ── B13 · tear down every belief, keep one move: claim -> ? -> what would make it wrong ────────────────────
class B13_Inspect(Scene):
    def construct(self):
        xs = [-4.6, -2.3, 0.0, 2.3, 4.6]
        sq = [a2_card(1.2, 1.2, DIM, 5).move_to([x, 0.3, 0]) for x in xs]
        self.add(*sq)
        dn = T("Descartes", 40).move_to([0.0, 1.9, 0])
        self.play(FadeIn(dn), run_time=0.3)
        for i in (4, 3, 2, 1):
            x = a2_cross(xs[i], 0.3, 0.3, INK, 7)
            self.play(Create(x), run_time=0.25)
            self.play(FadeOut(sq[i]), FadeOut(x), run_time=0.25)
        keep = sq[0]
        self.play(keep.animate.set_stroke(INK, 8), dn.animate.move_to([-4.6, 1.7, 0]), run_time=0.5)
        cl = T("Claim", 40).move_to([-4.6, -0.7, 0])
        a1 = Arrow([-3.85, 0.3, 0], [-2.1, 0.3, 0], buff=0, color=INK, stroke_width=6, tip_length=0.22)
        q = Circle(radius=0.75, stroke_color=INK, stroke_width=7).move_to([-1.2, 0.3, 0])
        qm = T("?", 72).move_to([-1.2, 0.3, 0])
        self.play(FadeIn(cl), Create(a1), Create(q), FadeIn(qm), run_time=0.7)
        until(self, "what would have to be true", lead=0.4)
        a2 = Arrow([-0.35, 0.3, 0], [1.55, 0.3, 0], buff=0, color=INK, stroke_width=6, tip_length=0.22)
        card = a2_card(4.0, 2.4).move_to([3.7, 0.3, 0])
        wi = T("Wrong if…", 42).move_to([3.7, 0.95, 0])
        blanks = VGroup(*[DashedLine([2.2, y, 0], [5.2, y, 0], color=DIM, stroke_width=5) for y in (0.3, -0.15, -0.6)])
        self.play(Create(a2), FadeIn(card), FadeIn(wi), Create(blanks), run_time=0.7)
        done(self)


# ── B14 · rebuild figure: a success claim branches into three checks that each need evidence ──────────────
class B14_Checks(Scene):
    def construct(self):
        xs = [-4.2, 0.0, 4.2]
        claim = a2_card(4.6, 1.0, DIM, 5).move_to([0, 2.5, 0])
        cl = T("Success claim", 40).move_to([0, 2.5, 0])
        self.add(claim, cl)
        names = ["Coverage", "Inputs", "Context"]
        qs = ["Seen cases\nlike this?", "Signal\nmeasured?", "Same hospital\nas tested?"]
        cues = ["underrepresented", "Or the inputs", "Or today's hospital"]
        for x, n, q, c in zip(xs, names, qs, cues):
            until(self, c, lead=0.9)
            br = Line([0, 2.0, 0] if x == 0 else [x * 0.35, 2.0, 0], [x, 1.45, 0], color=INK, stroke_width=5)
            ck = a2_card(3.5, 1.0, DIM, 5).move_to([x, 0.95, 0])
            nm = T(n, 40).move_to([x, 0.95, 0])
            qq = T(q, 34, DIM).move_to([x, -0.35, 0])
            ev = DashedVMobject(a2_card(3.2, 0.9, DIM, 5), num_dashes=28).move_to([x, -1.85, 0])
            evl = T("evidence", 34, DIM).move_to([x, -1.85, 0])
            dot = Dot([x + 1.45, -1.25, 0], radius=0.11, color=TERRA)
            self.play(Create(br), FadeIn(ck), FadeIn(nm), run_time=0.4)
            self.play(FadeIn(qq), Create(ev), FadeIn(evl), FadeIn(dot), run_time=0.4)
        done(self)


# ── B15 · eight servers, seven updated, one missed; a flag wakes old code ─────────────────────────────────
class B15_Servers(Scene):
    def construct(self):
        xs = [-5.25 + 1.5 * i for i in range(8)]
        tiles = [a2_card(1.2, 1.2, DIM, 5).move_to([x, 1.5, 0]) for x in xs]
        date = T("Aug 1, 2012", 44).move_to([-3.2, -0.5, 0])
        self.add(*tiles, date)
        until(self, "put new software", lead=0.5)
        for i in range(7):
            ck = check(xs[i] - 0.2, 1.5, 0.22, INK, 8)
            self.play(tiles[i].animate.set_stroke(INK, 7), Create(ck), run_time=0.18)
        t7 = T("7 updated", 40).move_to([-3.2, -1.3, 0])
        self.play(FadeIn(t7), run_time=0.3)
        until(self, "missed one", lead=0.2)
        miss = Dot([xs[7], 2.35, 0], radius=0.13, color=TERRA)
        t8 = T("1 missed", 40).move_to([-3.2, -2.1, 0])
        self.play(FadeIn(miss), FadeIn(t8), run_time=0.3)
        pole = Line([5.25, 0.55, 0], [5.25, -0.4, 0], color=INK, stroke_width=6)
        flag = Polygon([5.25, -0.1, 0], [5.95, -0.25, 0], [5.25, -0.4, 0], fill_color=DIM, fill_opacity=1, stroke_color=DIM,
                       stroke_width=3)
        fl = T("flag", 36, DIM).move_to([4.45, 0.1, 0])
        card = a2_card(5.4, 1.4, GHOST, 5).move_to([3.2, -2.0, 0])
        pp = T("Power Peg", 42, DIM).move_to([1.9, -2.0, 0])
        yr = T("2003", 42, DIM).move_to([4.7, -2.0, 0])
        until(self, "a reused flag", lead=0.6)
        self.play(Create(pole), FadeIn(flag), FadeIn(fl), FadeIn(card), FadeIn(pp), FadeIn(yr), run_time=0.5)
        until(self, "woke code", lead=0.2)
        link = Arrow([5.25, -0.5, 0], [5.25, -1.28, 0], buff=0, color=INK, stroke_width=6, tip_length=0.2)
        wake = Dot([0.3, -2.0, 0], radius=0.13, color=TERRA)
        self.play(flag.animate.shift(UP * 0.85).set_color(INK), Create(link), card.animate.set_stroke(INK, 7),
                  pp.animate.set_color(INK), yr.animate.set_color(INK), FadeIn(wake), run_time=0.8)
        done(self)


# ── B16 · 45 minutes, and what the clock did ──────────────────────────────────────────────────────────────
class B16_Clock(Scene):
    def construct(self):
        frame = Rectangle(width=11.0, height=0.5, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([0, 2.2, 0])
        t0 = Line([-5.5, 1.75, 0], [-5.5, 1.5, 0], color=INK, stroke_width=5)
        t1 = Line([5.5, 1.75, 0], [5.5, 1.5, 0], color=INK, stroke_width=5)
        lab = T("45 minutes", 44).move_to([0, 3.0, 0])
        self.add(frame, t0, t1)
        self.play(FadeIn(lab), run_time=0.3)
        prog = Rectangle(width=11.0, height=0.5, stroke_width=0, fill_color=BAR2, fill_opacity=1).move_to([0, 2.2, 0])
        head = Dot([5.5, 2.2, 0], radius=0.17, color=TERRA)
        self.play(GrowFromEdge(prog, LEFT), run_time=1.6)
        self.play(FadeIn(head), run_time=0.2)
        cells = []
        spec = [(-4.1, "4,000,000+", "executions"), (0.0, "154", "stocks"), (4.1, "$460M+", "lost")]
        cues = ["over four million", "hundred fifty-four", "more than four hundred"]
        for (x, big, small), c in zip(spec, cues):
            until(self, c, lead=0.5)
            box = a2_card(3.7, 2.2, INK, 5).move_to([x, -0.35, 0])
            n = T(big, 44, INK, bold=True).move_to([x, 0.0, 0])
            s = T(small, 38, DIM).move_to([x, -0.85, 0])
            self.play(FadeIn(box), FadeIn(n), FadeIn(s), run_time=0.4)
        until(self, "according to", lead=0.2)
        src = T("per the SEC", 40).move_to([0, -2.4, 0])
        bar = Line([-1.7, -1.9, 0], [1.7, -1.9, 0], color=DIM, stroke_width=4)
        self.play(FadeIn(src), Create(bar), run_time=0.4)
        done(self)


# ── B17 · succeeded is not the same claim as doing what we intend ─────────────────────────────────────────
class B17_NotEqual(Scene):
    def construct(self):
        left = a2_card(4.6, 1.9, DIM, 5).move_to([-3.5, 0.5, 0])
        lt = T("Deployment\nsucceeded", 42).move_to([-3.5, 0.5, 0])
        self.add(left, lt)
        until(self, "The system is doing", lead=0.2)
        right = a2_card(4.6, 1.9, DIM, 5).move_to([3.5, 0.5, 0])
        rt = T("Doing what\nwe intend", 42).move_to([3.5, 0.5, 0])
        self.play(FadeIn(right), FadeIn(rt), run_time=0.5)
        until(self, "different claims", lead=0.6)
        e1 = Line([-0.6, 0.75, 0], [0.6, 0.75, 0], color=INK, stroke_width=9)
        e2 = Line([-0.6, 0.25, 0], [0.6, 0.25, 0], color=INK, stroke_width=9)
        sl = Line([-0.45, -0.1, 0], [0.45, 0.9, 0], color=INK, stroke_width=9)
        self.play(Create(e1), Create(e2), Create(sl), run_time=0.5)
        until(self, "stand in for", lead=1.0)
        arr = Arrow([-3.3, -1.6, 0], [3.3, -1.6, 0], buff=0, color=DIM, stroke_width=6, tip_length=0.25)
        self.play(Create(arr), run_time=0.6)
        stop = Line([0, -2.1, 0], [0, -1.1, 0], color=INK, stroke_width=10)
        sd = Dot([0, -1.6, 0], radius=0.15, color=TERRA)
        self.play(Create(stop), FadeIn(sd), run_time=0.4)
        done(self)


# ══════════════════════════════ scenes_act3.py ══════════════════════════════
"""GROUP 3 · Acts III-IV  (B18–B27, all Manim)

Cast for these ten beats: the CHECK MARK (ink, drawn with two lines), outlined round tiles, the circle (model / world),
the swan (built from an ellipse, a bezier neck, a small circle and a triangle), and ONE terracotta dot that marks the thing
the voice is pointing at. No person tokens anywhere. Numbers on screen are the verified ones in factcheck/PRIMARIES.md;
anything else is labelled schematic / illustrative.
"""

A3_FRAME_NOTE = "x in +-6.2, y in +-3.3"


def a3_swan(cx, cy, s=1.0, black=False):
    """A swan from primitives: ellipse body, bezier neck, circle head, triangle beak and tail. (cx, cy) = body centre."""
    fill = INK if black else CARD
    body = Ellipse(width=0.95 * s, height=0.46 * s, fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4)
    body.move_to([cx, cy, 0])
    neck = CubicBezier(np.array([cx + 0.30 * s, cy + 0.10 * s, 0]), np.array([cx + 0.62 * s, cy + 0.20 * s, 0]),
                       np.array([cx + 0.05 * s, cy + 0.48 * s, 0]), np.array([cx + 0.40 * s, cy + 0.72 * s, 0]))
    neck.set_stroke(INK, 7 if not black else 8).set_fill(opacity=0)
    head = Circle(radius=0.085 * s, fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx + 0.43 * s, cy + 0.74 * s, 0])
    beak = Polygon([cx + 0.50 * s, cy + 0.79 * s, 0], [cx + 0.50 * s, cy + 0.69 * s, 0], [cx + 0.68 * s, cy + 0.73 * s, 0],
                   fill_color=INK, fill_opacity=1, stroke_width=0)
    tail = Polygon([cx - 0.40 * s, cy + 0.02 * s, 0], [cx - 0.62 * s, cy + 0.22 * s, 0], [cx - 0.36 * s, cy + 0.14 * s, 0],
                   fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=3)
    return VGroup(tail, body, neck, head, beak)


def a3_turkey(cx, cy, s=1.0):
    """A turkey from primitives: round body, tail fan of three arcs, small head, beak, two legs."""
    body = Circle(radius=0.38 * s, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    fan = VGroup(*[Arc(radius=(0.52 + 0.14 * k) * s, start_angle=PI * 0.62, angle=PI * 0.76, arc_center=[cx, cy, 0],
                       stroke_color=INK if k == 0 else DIM, stroke_width=4) for k in range(3)])
    head = Circle(radius=0.14 * s, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx + 0.52 * s, cy + 0.3 * s, 0])
    beak = Polygon([cx + 0.64 * s, cy + 0.36 * s, 0], [cx + 0.64 * s, cy + 0.24 * s, 0], [cx + 0.82 * s, cy + 0.3 * s, 0],
                   fill_color=INK, fill_opacity=1, stroke_width=0)
    legs = VGroup(Line([cx - 0.1 * s, cy - 0.38 * s, 0], [cx - 0.1 * s, cy - 0.72 * s, 0], color=INK, stroke_width=4),
                  Line([cx + 0.12 * s, cy - 0.38 * s, 0], [cx + 0.12 * s, cy - 0.72 * s, 0], color=INK, stroke_width=4))
    return VGroup(fan, legs, body, head, beak)


# ── B18 · Hume: checks accumulate, 'guarantee' stays at zero, the world quietly does some of the work ──────────────────
class B18_Hume(Scene):
    def construct(self):
        title = T("Hume", 40).move_to([-4.6, 2.9, 0])
        self.add(title)
        until(self, "A model that has been right", lead=1.0)
        cols, rows = 8, 4
        marks = VGroup(*[check(-5.2 + i * 0.5, 1.95 - j * 0.5, s=0.16, color=INK, w=6) for j in range(rows) for i in range(cols)])
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.06), run_time=1.9)
        until(self, "no logical guarantee", lead=1.0)
        gl = T("guarantee", 44).move_to([3.4, 1.9, 0])
        zero = T("0", 150).move_to([3.4, 0.35, 0])
        self.play(FadeIn(gl), GrowFromCenter(zero), run_time=0.7)
        until(self, "The world was doing", lead=0.3)
        world = Circle(radius=0.8, stroke_color=INK, stroke_width=5).move_to([-3.4, -2.05, 0])
        wl = T("world", 40).move_to([-1.3, -2.05, 0])
        ups = VGroup(*[Arrow([x, -1.2, 0], [x, -0.1, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18) for x in (-4.3, -3.4, -2.5)])
        self.play(Create(world), FadeIn(wl), run_time=0.6)
        self.play(LaggedStart(*[Create(a) for a in ups], lag_ratio=0.3), run_time=0.8)
        until(self, "until it stopped", lead=0.2)
        dot = Dot([-3.4, -2.05, 0], radius=0.1, color=TERRA)
        self.play(FadeOut(ups), FadeIn(dot), run_time=0.6)
        done(self)


# ── B19 · the turkey: day counter to 1,000, confidence curve rises, then 1,001 and the axe ─────────────────────────────
class B19_Turkey(Scene):
    def construct(self):
        ox, oy = -4.5, -2.2
        y_ax = Arrow([ox, oy, 0], [ox, 1.4, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        x_ax = Arrow([ox, oy, 0], [5.0, oy, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        conf = T("confidence", 38).move_to([-2.9, 1.65, 0])
        sch = T("schematic", 32, DIM).move_to([4.5, -2.8, 0])
        turkey = a3_turkey(-5.2, 2.35, 0.9)
        day = T("day", 44).move_to([1.6, 2.3, 0])
        vt = ValueTracker(1)
        counter = always_redraw(lambda: T(f"{int(round(vt.get_value())):,}", 84).move_to([4.15, 2.3, 0]))
        self.add(y_ax, x_ax, conf, sch, turkey, day, counter)
        pts = [np.array([ox + 0.0 + 7.5 * k / 40, oy + 3.3 * (1 - np.exp(-(7.5 * k / 40) / 2.2)), 0.0]) for k in range(41)]
        curve = VMobject(color=INK, stroke_width=7).set_points_smoothly(pts)
        dot = Dot(pts[0], radius=0.12, color=TERRA)
        self.add(dot)
        until(self, "fed every morning", lead=0.6)
        self.play(Create(curve), MoveAlongPath(dot, curve), vt.animate.set_value(1000), run_time=3.2, rate_func=linear)
        until(self, "the farmer comes", lead=0.9)
        self.play(vt.animate.set_value(1001), run_time=0.2)
        handle = Line([3.7, -0.75, 0], [4.45, 0.35, 0], color=INK, stroke_width=7)
        head = Polygon([4.28, 0.2, 0], [4.62, 0.62, 0], [4.05, 0.85, 0], [3.8, 0.45, 0], fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4)
        axe = VGroup(handle, head)
        self.play(FadeIn(axe, shift=DOWN * 0.5), run_time=0.4)
        drop = Line(pts[-1], [pts[-1][0], oy, 0], color=INK, stroke_width=7)
        self.play(Create(drop), dot.animate.move_to([pts[-1][0], oy, 0]), run_time=0.5)
        done(self)


# ── B20 · correlation line over a hidden mechanism that flips ──────────────────────────────────────────────────────────
class B20_Mechanism(Scene):
    def construct(self):
        ox, oy = -5.6, -2.4
        y_ax = Arrow([ox, oy, 0], [ox, 1.9, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        x_ax = Arrow([ox, oy, 0], [-0.7, oy, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        self.add(y_ax, x_ax)
        line = Line([-5.0, -1.9, 0], [-1.4, 1.2, 0], color=BAR1, stroke_width=6)
        jit = [0.12, -0.1, 0.08, -0.14, 0.1, -0.06, 0.13, -0.1, 0.05]
        dots = VGroup(*[Dot([-5.0 + 3.6 * t, -1.9 + 3.1 * t + jit[i], 0], radius=0.1, color=INK) for i, t in enumerate(np.linspace(0, 1, 9))])
        self.play(Create(line), LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.12), run_time=1.6)
        until(self, "It knew the correlation", lead=0.2)
        cl = T("correlation", 40).move_to([-3.2, 2.55, 0])
        self.play(FadeIn(cl), run_time=0.4)
        until(self, "not the mechanism", lead=0.9)
        cx, cy = 3.2, 0.3
        blk = DashedVMobject(RoundedRectangle(width=2.6, height=2.6, corner_radius=0.2, stroke_color=DIM, stroke_width=5), num_dashes=40).move_to([3.2, 0.3, 0])
        ml = T("mechanism", 40).move_to([3.2, 2.2, 0])
        pivot = Dot([cx, cy, 0], radius=0.12, color=INK)
        lever = Line([cx, cy, 0], [cx - 0.85, cy + 0.65, 0], color=DIM, stroke_width=7)
        self.play(Create(blk), FadeIn(ml), Create(lever), FadeIn(pivot), run_time=0.8)
        until(self, "the mechanism changed", lead=0.3)
        solid = RoundedRectangle(width=2.6, height=2.6, corner_radius=0.2, stroke_color=INK, stroke_width=5).move_to([cx, cy, 0])
        targets = [-0.15, -0.5, -0.4, -1.1, -0.9, -1.6, -1.4, -2.0, -2.3]
        self.play(Rotate(lever, angle=PI, about_point=np.array([cx, cy, 0])), FadeIn(solid), run_time=0.9)
        self.play(*[d.animate.shift(DOWN * (-g) * 0.9) for d, g in zip(dots, targets)], run_time=0.9)
        ml2 = T("model", 38).move_to([-0.35, 1.45, 0])
        self.play(FadeIn(ml2), run_time=0.3)
        until(self, "is that turkey", lead=0.9)
        tk = a3_turkey(4.6, -2.0, 0.85)
        self.play(FadeIn(tk), run_time=0.5)
        done(self)


# ── B21 · Zillow: two bars and a quarter of the staff ─────────────────────────────────────────────────────────────────
class B21_Zillow(Scene):
    def construct(self):
        base_y, k = -1.9, 0.0095
        title = T("Zillow", 40).move_to([-4.7, 2.85, 0])
        cap = T("per Zillow 8-K, Nov 2021", 32, DIM).move_to([3.9, -2.85, 0])
        self.add(title, cap)
        ground = Line([-6.0, base_y, 0], [0.2, base_y, 0], color=DIM, stroke_width=4)
        self.play(Create(ground), run_time=0.3)
        until(self, "three hundred four", lead=1.4)
        h1 = 304.4 * k
        b1 = Rectangle(width=1.4, height=h1, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-4.7, base_y + h1 / 2, 0])
        n1 = T("$304.4M", 42).move_to([-4.7, base_y + h1 + 0.5, 0])
        l1 = T("Q3\nwrite-down", 32).move_to([-4.7, base_y - 0.65, 0])
        self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=0.7)
        self.play(FadeIn(n1), run_time=0.3)
        until(self, "expected more than", lead=0.5)
        h2, h2x = 240 * k, 25 * k
        b2 = Rectangle(width=1.4, height=h2, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-1.6, base_y + h2 / 2, 0])
        b2x = DashedVMobject(Rectangle(width=1.4, height=h2x, stroke_color=INK, stroke_width=4), num_dashes=16).move_to([-1.6, base_y + h2 + h2x / 2, 0])
        n2 = T("$240–265M", 42).move_to([-1.6, base_y + h2 + h2x + 0.5, 0])
        l2 = T("expected\nQ4 charges", 32).move_to([-1.6, base_y - 0.65, 0])
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=0.7)
        self.play(Create(b2x), FadeIn(n2), run_time=0.5)
        until(self, "about a quarter", lead=0.9)
        sq = VGroup(*[RoundedRectangle(width=0.9, height=0.9, corner_radius=0.12, stroke_color=INK, stroke_width=5).move_to([1.9 + 1.2 * i, 0.9, 0])
                      for i in range(4)])
        self.play(LaggedStart(*[Create(s) for s in sq], lag_ratio=0.25), run_time=0.9)
        cross = VGroup(Line([5.15, 0.6, 0], [5.85, 1.2, 0], color=INK, stroke_width=5), Line([5.15, 1.2, 0], [5.85, 0.6, 0], color=INK, stroke_width=5))
        self.play(sq[3].animate.set_fill(GHOST, 1), Create(cross), run_time=0.5)
        pc = T("25% of staff", 40).move_to([3.7, -0.55, 0])
        self.play(FadeIn(pc), run_time=0.4)
        done(self)


# ── B22 · Google Flu Trends: 108 week tiles, 100 filled ───────────────────────────────────────────────────────────────
class B22_FluTiles(Scene):
    def construct(self):
        cols, rows, sp = 18, 6, 0.4
        gx, gy = -5.3, 1.9
        empty = set([4, 17, 29, 41, 52, 66, 79, 94])     # 8 weeks that were not too high: tile order is schematic
        tiles = []
        for n in range(108):
            r, c = divmod(n, cols)
            t = RoundedRectangle(width=0.32, height=0.32, corner_radius=0.06, stroke_color=DIM, stroke_width=3).move_to([gx + c * sp, gy - r * sp, 0])
            tiles.append(t)
        title = T("Flu Trends", 40).move_to([-4.6, 2.9, 0])
        cap = T("Lazer et al., Science, 2014", 32, DIM).move_to([3.9, -2.8, 0])
        sch = T("tile order schematic", 32, DIM).move_to([-3.2, -1.05, 0])
        self.add(title, cap)
        until(self, "From August", lead=0.9)
        self.play(LaggedStart(*[Create(t) for t in tiles], lag_ratio=0.012), FadeIn(sch), run_time=1.6)
        until(self, "a hundred of a hundred", lead=1.5)
        fills = [t.animate.set_fill(BAR1, 1).set_stroke(INK, 3) for n, t in enumerate(tiles) if n not in empty]
        self.play(LaggedStart(*fills, lag_ratio=0.012), run_time=1.5)
        n100 = T("100", 120).move_to([3.7, 1.55, 0])
        of = T("of 108 weeks", 40).move_to([3.7, 0.35, 0])
        hi = T("too high", 40).move_to([3.7, -0.4, 0])
        self.play(GrowFromCenter(n100), FadeIn(of), FadeIn(hi), run_time=0.6)
        until(self, "big data hubris", lead=0.4)
        q = T("“big data hubris”", 46).move_to([-2.6, -2.1, 0])
        dot = Dot([-5.35, -2.1, 0], radius=0.11, color=TERRA)
        self.play(FadeIn(q), FadeIn(dot), run_time=0.6)
        done(self)


# ── B23 · confidence belongs to the model; the arrow only runs one way; the supervisor's check ─────────────────────────
class B23_OneWay(Scene):
    def construct(self):
        model = Circle(radius=1.15, stroke_color=INK, stroke_width=5).move_to([-3.4, 0.7, 0])
        world = Circle(radius=1.15, stroke_color=INK, stroke_width=5).move_to([3.4, 0.7, 0])
        ml = T("model", 40).move_to([-3.4, 0.7, 0])
        wl = T("world", 40).move_to([3.4, 0.7, 0])
        cf = T("confidence", 38).move_to([-3.4, 2.3, 0])
        cdot = Dot([-3.4, 1.2, 0], radius=0.1, color=TERRA)
        self.add(model, ml)
        self.play(FadeIn(cf), FadeIn(cdot), run_time=0.5)
        until(self, "not to the world", lead=0.5)
        self.play(Create(world), FadeIn(wl), run_time=0.5)
        fwd = Arrow([-2.15, 1.0, 0], [2.15, 1.0, 0], buff=0, color=INK, stroke_width=6, tip_length=0.25)
        self.play(Create(fwd), run_time=0.5)
        until(self, "owes the model nothing", lead=0.5)
        back = DashedLine([2.15, 0.4, 0], [-2.15, 0.4, 0], color=DIM, stroke_width=5, dash_length=0.2)
        tip = Triangle(fill_color=DIM, fill_opacity=1, stroke_width=0).scale(0.14).rotate(PI / 6).move_to([-2.25, 0.4, 0])
        xm = VGroup(Line([-0.2, 0.22, 0], [0.2, 0.58, 0], color=INK, stroke_width=6), Line([-0.2, 0.58, 0], [0.2, 0.22, 0], color=INK, stroke_width=6))
        self.play(Create(back), FadeIn(tip), Create(xm), run_time=0.7)
        until(self, "cannot tell when", lead=0.6)
        ring = Circle(radius=1.5, stroke_color=DIM, stroke_width=4).move_to([3.4, 0.7, 0])
        self.play(Create(ring), run_time=0.5)
        until(self, "Only the supervisor", lead=0.3)
        br = VGroup(Line([-3.4, -0.7, 0], [-3.4, -1.3, 0], color=INK, stroke_width=5), Line([-3.4, -1.3, 0], [3.4, -1.3, 0], color=INK, stroke_width=5),
                    Line([3.4, -1.3, 0], [3.4, -0.7, 0], color=INK, stroke_width=5))
        ck = check(0.0, -1.3, s=0.3, color=INK, w=9)
        sup = T("supervisor", 44).move_to([0, -2.4, 0])
        self.play(Create(br), run_time=0.6)
        self.play(Create(ck), FadeIn(sup), run_time=0.5)
        done(self)


# ── B24 · a claim card with three blanks: metric, threshold, window ───────────────────────────────────────────────────
class B24_Blanks(Scene):
    def construct(self):
        card = RoundedRectangle(width=4.6, height=1.3, corner_radius=0.25, stroke_color=DIM, stroke_width=5).move_to([-3.0, 2.0, 0])
        ct = T("performs well", 42).move_to([-3.0, 2.0, 0])
        self.add(card, ct)
        until(self, "what would performing badly", lead=1.5)
        twin = DashedVMobject(RoundedRectangle(width=4.6, height=1.3, corner_radius=0.25, stroke_color=DIM, stroke_width=5), num_dashes=44).move_to([3.0, 2.0, 0])
        tt = T("performs badly?", 42, DIM).move_to([3.0, 2.0, 0])
        self.play(Create(twin), FadeIn(tt), run_time=0.7)
        until(self, "On which metric", lead=0.3)
        xs = [-4.1, 0.0, 4.1]
        slots = VGroup(*[RoundedRectangle(width=3.2, height=1.9, corner_radius=0.2, stroke_color=DIM, stroke_width=4).move_to([x, -0.6, 0]) for x in xs])
        names = VGroup(*[T(w, 40).move_to([x, -2.2, 0]) for w, x in zip(["metric", "threshold", "window"], xs)])
        self.play(LaggedStart(*[Create(s) for s in slots], lag_ratio=0.2), FadeIn(names), run_time=0.8)
        # glyphs fill the blanks one by one
        bars = VGroup(*[Rectangle(width=0.32, height=h, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([xs[0] - 0.55 + 0.55 * i, -0.6 - 0.8 + h / 2, 0])
                        for i, h in enumerate([0.6, 1.1, 0.8])])
        wave = VMobject(color=DIM, stroke_width=5).set_points_smoothly([np.array([xs[1] - 1.2 + 0.4 * i, -0.65 + 0.45 * np.sin(i * 0.9), 0]) for i in range(7)])
        thr = Line([xs[1] - 1.3, -0.35, 0], [xs[1] + 1.3, -0.35, 0], color=INK, stroke_width=5)
        brk = VGroup(Line([xs[2] - 1.2, -0.3, 0], [xs[2] - 1.2, -0.9, 0], color=INK, stroke_width=5), Line([xs[2] + 1.2, -0.3, 0], [xs[2] + 1.2, -0.9, 0], color=INK, stroke_width=5),
                     Line([xs[2] - 1.2, -0.6, 0], [xs[2] + 1.2, -0.6, 0], color=INK, stroke_width=5),
                     *[Line([xs[2] - 0.8 + 0.4 * i, -0.75, 0], [xs[2] - 0.8 + 0.4 * i, -0.45, 0], color=DIM, stroke_width=4) for i in range(5)])
        dot = Dot([xs[0], -0.6, 0], radius=0.1, color=TERRA)
        until(self, "past what threshold", lead=1.2)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.2), FadeIn(dot), run_time=0.6)
        until(self, "past what threshold", lead=-0.1)
        self.play(dot.animate.move_to([xs[1], 0.0, 0]), Create(wave), run_time=0.5)
        self.play(Create(thr), run_time=0.3)
        until(self, "over what window", lead=0.3)
        self.play(dot.animate.move_to([xs[2], 0.0, 0]), Create(brk), run_time=0.5)
        done(self)


# ── B25 · white swans accumulate; one black swan ends the claim ───────────────────────────────────────────────────────
class B25_Swans(Scene):
    def construct(self):
        claim = T("all swans are white", 44).move_to([-1.2, 2.6, 0])
        self.add(claim)
        whites = VGroup()
        for j, y in enumerate([0.55, -1.1]):
            for i in range(4):
                whites.add(a3_swan(-5.0 + 1.5 * i, y, 1.0))
        until(self, "No count of white swans", lead=0.4)
        self.play(LaggedStart(*[FadeIn(w, shift=UP * 0.15) for w in whites], lag_ratio=0.25), run_time=1.6)
        until(self, "One black swan", lead=0.2)
        blk = a3_swan(3.6, -0.25, 1.5, black=True)
        self.play(GrowFromCenter(blk), run_time=0.6)
        ring = Circle(radius=1.35, stroke_color=INK, stroke_width=5).move_to([3.7, 0.0, 0])
        dot = Dot([3.7, 1.55, 0], radius=0.11, color=TERRA)
        self.play(Create(ring), FadeIn(dot), whites.animate.set_opacity(0.35), run_time=0.7)
        until(self, "trying to break it", lead=0.3)
        brk = T("break it", 44).move_to([3.7, -2.1, 0])
        self.play(FadeIn(brk), run_time=0.4)
        done(self)


# ── B26 · internal validation counts white swans; external test tries for the black one ───────────────────────────────
class B26_Unrefuted(Scene):
    def construct(self):
        mid = Line([0, 2.6, 0], [0, -1.0, 0], color=DIM, stroke_width=4)
        hl = T("internal validation", 38).move_to([-3.1, 2.7, 0])
        hr = T("external test", 38).move_to([3.1, 2.7, 0])
        self.add(mid, hl, hr)
        whites = VGroup()
        for j, y in enumerate([1.0, -0.4]):
            for i in range(3):
                whites.add(a3_swan(-4.5 + 1.6 * i, y, 0.9))
        until(self, "only ever got white-swan", lead=0.3)
        self.play(LaggedStart(*[FadeIn(w) for w in whites], lag_ratio=0.2), run_time=1.3)
        checks = VGroup(*[check(-5.3 + 1.6 * i, -1.6, s=0.17, color=INK, w=6) for i in range(3)], *[check(-5.3 + 1.6 * i, -1.6 + 0.0, s=0.0, color=INK, w=0) for i in range(0)])
        self.play(LaggedStart(*[Create(c) for c in checks], lag_ratio=0.3), run_time=0.7)
        until(self, "serious attempt", lead=0.2)
        slot = DashedVMobject(Circle(radius=1.3, stroke_color=DIM, stroke_width=5), num_dashes=30).move_to([3.1, 0.4, 0])
        q = T("?", 80, DIM).move_to([3.1, 0.4, 0])
        self.play(Create(slot), FadeIn(q), run_time=0.6)
        until(self, "another health system", lead=0.2)
        blk = a3_swan(3.1, 0.2, 1.4, black=True)
        self.play(FadeOut(q), FadeIn(blk), run_time=0.5)
        until(self, "Unrefuted is not", lead=0.3)
        eq = T("unrefuted ≠ validated", 46).move_to([0, -2.4, 0])
        self.play(FadeIn(eq), run_time=0.5)
        done(self)


# ── B27 · rewrite: the vague claim fits every outcome; the specific one names its failure ─────────────────────────────
class B27_Rewrite(Scene):
    def construct(self):
        sep = Line([-6.0, 0.35, 0], [6.0, 0.35, 0], color=DIM, stroke_width=3)
        self.add(sep)
        t1 = T("vague", 32, DIM).move_to([-4.5, 2.1, 0])
        r1 = T("robust", 50).move_to([-3.6, 1.2, 0])
        self.play(FadeIn(t1), FadeIn(r1), run_time=0.4)
        xs = [1.0 + 1.15 * i for i in range(5)]
        o1 = VGroup(*[Circle(radius=0.28, stroke_color=INK, stroke_width=4).move_to([x, 1.2, 0]) for x in xs])
        c1 = VGroup(*[check(x, 1.2, s=0.17, color=INK, w=6) for x in xs])
        until(self, "The system is robust", lead=0.2)
        self.play(LaggedStart(*[Create(o) for o in o1], lag_ratio=0.15), run_time=0.6)
        until(self, "becomes", lead=1.6)
        t2 = T("specific", 32, DIM).move_to([-4.4, -0.3, 0])
        r2 = T("error rate < 2%", 44).move_to([-3.4, -1.0, 0])
        r2b = T("over 30 days", 40).move_to([-3.4, -1.75, 0])
        self.play(FadeIn(t2), FadeIn(r2), FadeIn(r2b), run_time=0.5)
        o2 = VGroup(*[Circle(radius=0.28, stroke_color=INK, stroke_width=4).move_to([x, -1.2, 0]) for x in xs])
        self.play(LaggedStart(*[Create(o) for o in o2], lag_ratio=0.15), run_time=0.6)
        until(self, "fits any outcome", lead=0.8)
        self.play(LaggedStart(*[Create(c) for c in c1], lag_ratio=0.12), run_time=0.8)
        until(self, "names what would make it false", lead=1.2)
        keep = [0, 1, 3]
        c2 = VGroup(*[check(xs[i], -1.2, s=0.17, color=INK, w=6) for i in keep])
        fails = VGroup(*[VGroup(Line([xs[i] - 0.17, -1.37, 0], [xs[i] + 0.17, -1.03, 0], color=INK, stroke_width=7),
                                Line([xs[i] - 0.17, -1.03, 0], [xs[i] + 0.17, -1.37, 0], color=INK, stroke_width=7)) for i in (2, 4)])
        self.play(LaggedStart(*[Create(c) for c in c2], lag_ratio=0.15), run_time=0.6)
        self.play(LaggedStart(*[Create(f) for f in fails], lag_ratio=0.2), run_time=0.5)
        until(self, "illustrations", lead=0.8)
        ill = T("illustrative thresholds", 34, DIM).move_to([0, -2.85, 0])
        dot = Dot([xs[2] + 0.55, -1.2, 0], radius=0.1, color=TERRA)
        self.play(FadeIn(ill), FadeIn(dot), run_time=0.4)
        done(self)


# ══════════════════════════════ scenes_act4.py ══════════════════════════════
"""GROUP 4 · Act VI "The slice you can see" (B28-B33) and Act VII "Cheap to make, dear to check" (B34-B37).

Cast, Act VI: the ARTIFACT/WORLD pair drawn as outlines, dashed ghosts for what is never seen, and the lit SLICE of a disk.
Cast, Act VII: effort bars, candidate circles, a stack of boxes with the same hole, a clipboard for the human check.
No people anywhere; the patient is a clot, a tube and a gurney.
"""


def a4_label(s, x, y, size=36, color=INK):
    return T(s, size, color).move_to([x, y, 0])


def a4_x(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


def a4_ghost(center, r, dashes=18):
    return DashedVMobject(Circle(radius=r, color=DIM, stroke_width=5).move_to(center), num_dashes=dashes)


# ── B28 · you never see the cause ────────────────────────────────────────────────────────────────────────
class B28_Unseen(Scene):
    def construct(self):
        ground = Line([-5.6, -2.3, 0], [-2.2, -2.3, 0], color=INK, stroke_width=7)
        apple = VGroup(Circle(radius=0.32, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5),
                       Line([0, 0.32, 0], [0.06, 0.58, 0], color=INK, stroke_width=5)).move_to([-3.9, 2.2, 0])
        oc = np.array([3.4, 0.1, 0.0])
        orbit = Circle(radius=2.0, color=DIM, stroke_width=6).move_to(oc)
        sun = Circle(radius=0.38, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to(oc)
        body = Dot(oc + np.array([-2.0 * 0.5, 2.0 * 0.866, 0]), radius=0.17, color=INK)
        self.add(ground, apple, orbit, sun, body)
        until(self, "You never see causation", lead=0.3)
        ghost = a4_ghost([0, 0.3, 0], 0.65)
        l1 = DashedLine([-0.65, 0.3, 0], [-3.3, 0.3, 0], color=DIM, stroke_width=5)
        l2 = DashedLine([0.65, 0.3, 0], [1.4, 0.3, 0], color=DIM, stroke_width=5)
        cause = a4_label("cause", 0, -0.75)
        self.play(Create(ghost), Create(l1), Create(l2), FadeIn(cause), run_time=0.7)
        until(self, "Nobody has seen gravity", lead=0.2)
        self.play(Indicate(VGroup(ghost, cause), scale_factor=1.12, color=INK), run_time=0.6)
        until(self, "an apple falling", lead=0.6)
        lab_a = a4_label("apple falling", -3.9, -2.85)
        hit = Dot([-3.25, -2.3, 0], radius=0.13, color=TERRA)
        self.play(apple.animate.move_to([-3.9, -1.95, 0]), FadeIn(lab_a), run_time=0.7, rate_func=ease_in)
        self.play(GrowFromCenter(hit), run_time=0.2)
        until(self, "an orbit bending", lead=1.2)
        lab_o = a4_label("orbit bending", 3.4, -2.85)
        arc = Arc(radius=2.0, start_angle=2 * PI / 3, angle=-PI * 0.55, arc_center=oc)
        body.move_to(arc.get_start())
        self.play(MoveAlongPath(body, arc), FadeIn(lab_o), run_time=0.9)
        done(self)


# ── B29 · the lit slice and the outside ───────────────────────────────────────────────────────────────────
class B29_Slice(Scene):
    def construct(self):
        c = np.array([-1.5, 0.2, 0.0])
        disk = Circle(radius=2.2, fill_color=GHOST, fill_opacity=0.45, stroke_color=DIM, stroke_width=6).move_to(c)
        sl = Sector(radius=2.2, start_angle=20 * DEGREES, angle=60 * DEGREES, arc_center=c, fill_color=BOX_L, fill_opacity=1,
                    stroke_color=INK, stroke_width=5)
        out_l = a4_label("outside", -1.5, -2.75)
        sl_l = a4_label("slice", 1.0, 1.95)
        self.add(disk, sl, out_l, sl_l)
        kant = a4_label("Kant", 4.3, 1.9, 40)
        until(self, "Kant said better instruments", lead=0.2)
        tele = VGroup(Rectangle(width=1.5, height=0.4, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5),
                      Line([-0.75, 0, 0], [-0.95, 0.0, 0], color=INK, stroke_width=8)).rotate(133 * DEGREES).move_to([1.7, -0.25, 0])
        self.play(FadeIn(kant), FadeIn(tele), run_time=0.5)
        ticks = VGroup(*[Line(c + np.array([0.7 * np.cos(a * DEGREES), 0.7 * np.sin(a * DEGREES), 0]),
                              c + np.array([2.05 * np.cos(a * DEGREES), 2.05 * np.sin(a * DEGREES), 0]), color=DIM, stroke_width=3)
                         for a in (28, 40, 52, 64, 74)])
        self.play(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.25), run_time=1.2)
        until(self, "never close that gap", lead=0.1)
        self.play(Indicate(out_l, scale_factor=1.15, color=INK), run_time=0.5)
        until(self, "weaker view", lead=0.2)
        wide = Sector(radius=2.2, start_angle=4 * DEGREES, angle=92 * DEGREES, arc_center=c, fill_opacity=0, stroke_color=INK, stroke_width=5)
        wk = a4_label("weaker view", 4.3, 0.15, 40)
        wk2 = a4_label("the course author's", 4.3, -0.55, 32)
        self.play(Create(wide), FadeIn(wk), FadeIn(wk2), run_time=0.8)
        until(self, "approaching without arriving", lead=0.3)
        reach = Dot(c + np.array([2.2 * np.cos(4 * DEGREES), 2.2 * np.sin(4 * DEGREES), 0]), radius=0.15, color=TERRA)
        self.add(reach)
        self.play(MoveAlongPath(reach, Arc(radius=2.2, start_angle=4 * DEGREES, angle=-80 * DEGREES, arc_center=c)), run_time=1.6)
        until(self, "we see a slice", lead=0.2)
        self.play(Indicate(sl, scale_factor=1.06, color=INK), run_time=0.6)
        until(self, "there is an outside", lead=0.2)
        self.play(Indicate(VGroup(out_l), scale_factor=1.2, color=INK), run_time=0.6)
        done(self)


# ── B30 · artifact | ? | world ────────────────────────────────────────────────────────────────────────────
class B30_ThreeQuestions(Scene):
    def construct(self):
        ab = RoundedRectangle(width=2.6, height=2.2, corner_radius=0.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-3.9, 0.3, 0])
        lines = VGroup(*[Line([-4.7, y, 0], [-3.1, y, 0], color=DIM, stroke_width=5) for y in (0.8, 0.3, -0.2)])
        wb = RoundedRectangle(width=2.6, height=2.2, corner_radius=0.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([3.9, 0.3, 0])
        rings = VGroup(*[Circle(radius=r, color=DIM, stroke_width=5).move_to([3.9, 0.3, 0]) for r in (0.35, 0.75)])
        link = DashedLine([-2.4, 0.3, 0], [2.4, 0.3, 0], color=DIM, stroke_width=5)
        self.add(ab, lines, wb, rings, link)
        until(self, "What is the artifact?", lead=0.2)
        l1 = a4_label("artifact", -3.9, -1.3)
        d1 = Dot([-3.9, -1.85, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(l1), FadeIn(d1), Indicate(VGroup(ab, lines), scale_factor=1.06, color=INK), run_time=0.6)
        until(self, "What is the world?", lead=0.2)
        l2 = a4_label("world", 3.9, -1.3)
        d2 = Dot([3.9, -1.85, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(l2), FadeIn(d2), Indicate(VGroup(wb, rings), scale_factor=1.06, color=INK), run_time=0.6)
        until(self, "the relationship between them", lead=0.3)
        arr = dim_arrow([-2.45, 0.3, 0], [2.45, 0.3, 0], w=7, tip=0.22)
        q = a4_label("?", 0, 1.15, 80)
        l3 = a4_label("relationship", 0, -0.5)
        self.play(FadeOut(link), Create(arr), FadeIn(q), FadeIn(l3), run_time=0.7)
        until(self, "when the output is fluent", lead=0.2)
        d3 = Dot([0, -1.05, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(d3), run_time=0.3)
        done(self)


# ── B31 · everything checked on one side, the clot on the other ─────────────────────────────────────────
class B31_Gurney(Scene):
    def construct(self):
        div = Line([0.1, 2.9, 0], [0.1, -2.7, 0], color=GHOST, stroke_width=5)
        h1 = a4_label("artifact", -3.9, 2.5, 40)
        h2 = a4_label("world", 3.6, 2.5, 40)
        self.add(div, h1, h2)
        rows = [("score", 1.3, "The triage system produced a score"), ("model", 0.3, "the model"), ("metrics", -0.7, "the metrics")]
        labs, cks = [], []
        for name, y, _ in rows:
            labs.append(a4_label(name, -4.5, y))
            cks.append(check(-2.4, y - 0.05, 0.2, INK, 8))
        until(self, "The triage system produced a score", lead=0.1)
        self.play(FadeIn(labs[0]), Create(cks[0]), run_time=0.5)
        until(self, "The patient had a clot", lead=0.1)
        tube = VGroup(Line([1.9, 1.62, 0], [5.4, 1.62, 0], color=DIM, stroke_width=6), Line([1.9, 1.0, 0], [5.4, 1.0, 0], color=DIM, stroke_width=6))
        clot = Dot([3.6, 1.31, 0], radius=0.24, color=TERRA)
        box = Square(side_length=0.5, color=DIM, stroke_width=5).move_to([1.0, 1.31, 0])
        cl = a4_label("clot", 3.6, 0.4)
        self.play(Create(tube), GrowFromCenter(clot), Create(box), FadeIn(cl), run_time=0.7)
        until(self, "reviewed the score", lead=0.1)
        self.play(FadeIn(labs[1]), Create(cks[1]), run_time=0.4)
        self.play(FadeIn(labs[2]), Create(cks[2]), run_time=0.4)
        until(self, "gurney", lead=0.2)
        bed = Rectangle(width=3.4, height=0.32, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([3.6, -1.1, 0])
        legs = VGroup(Line([2.2, -1.26, 0], [2.2, -1.85, 0], color=INK, stroke_width=5), Line([5.0, -1.26, 0], [5.0, -1.85, 0], color=INK, stroke_width=5))
        wheels = VGroup(Circle(radius=0.17, color=INK, stroke_width=5).move_to([2.2, -2.0, 0]), Circle(radius=0.17, color=INK, stroke_width=5).move_to([5.0, -2.0, 0]))
        comp = a4_label("composite case", 3.6, -2.85, 32, DIM)
        self.play(Create(bed), Create(legs), Create(wheels), FadeIn(comp), run_time=0.7)
        done(self)


# ── B32 · the ring lands on the corner marker ───────────────────────────────────────────────────────────
class B32_Xray(Scene):
    def construct(self):
        plate = Rectangle(width=4.2, height=4.8, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=6).move_to([-3.6, -0.1, 0])
        lungs = VGroup(Ellipse(width=1.5, height=2.4, color=DIM, stroke_width=6).move_to([-4.3, -0.1, 0]),
                       Ellipse(width=1.5, height=2.4, color=DIM, stroke_width=6).move_to([-2.9, -0.1, 0]))
        spine = Line([-3.6, 1.6, 0], [-3.6, -1.7, 0], color=GHOST, stroke_width=6)
        marker = VGroup(Rectangle(width=0.55, height=0.36, color=INK, stroke_width=5), Line([-0.15, 0, 0], [0.15, 0, 0], color=DIM, stroke_width=4)).move_to([-5.0, 1.9, 0])
        self.add(plate, lungs, spine, marker)
        until(self, "detect COVID", lead=0.3)
        ring = Circle(radius=1.55, color=TERRA, stroke_width=8).move_to([-3.6, -0.1, 0])
        self.play(Create(ring), run_time=0.8)
        until(self, "DeGrave", lead=0.3)
        who = VGroup(a4_label("DeGrave, Janizek", 3.4, 0.55, 34), a4_label("& Lee, 2021", 3.4, 0.0, 34))
        self.play(FadeIn(who), run_time=0.4)
        until(self, "confounding factors", lead=0.3)
        self.play(ring.animate.scale(0.3).move_to([-5.0, 1.9, 0]), run_time=1.0)
        until(self, "accurate-looking", lead=0.3)
        q = T("“appear accurate, but\nfail when tested in\nnew hospitals”", 38).move_to([3.4, 2.0, 0])
        self.play(FadeIn(q), run_time=0.5)
        def hosp(x):
            return VGroup(Rectangle(width=0.9, height=0.9, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5),
                          Line([-0.2, 0, 0], [0.2, 0, 0], color=DIM, stroke_width=5), Line([0, -0.2, 0], [0, 0.2, 0], color=DIM, stroke_width=5)).move_to([x, -1.2, 0])
        h1, h2 = hosp(1.7), hosp(4.6)
        t1, t2 = a4_label("known", 1.7, -2.25, 32), a4_label("new", 4.6, -2.25, 32)
        self.play(FadeIn(h1), FadeIn(t1), Create(check(2.75, -1.25, 0.2, INK, 8)), run_time=0.5)
        self.play(FadeIn(h2), FadeIn(t2), Create(a4_x(5.65, -1.2)), run_time=0.5)
        done(self)


# ── B33 · artifact / world / relationship for a recidivism score ───────────────────────────────────────
class B33_Score(Scene):
    def construct(self):
        r1, r2, r3 = 2.2, 0.9, -1.1
        l1 = a4_label("artifact", -4.9, r1)
        l2 = a4_label("world", -4.9, r2)
        l3 = a4_label("relationship", -4.9, r3)
        self.add(l1)
        until(self, "A recidivism score", lead=0.2)
        bar = RoundedRectangle(width=4.6, height=0.5, corner_radius=0.25, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([0.6, r1, 0])
        pt = Dot([1.6, r1, 0], radius=0.2, color=INK)
        self.play(Create(bar), GrowFromCenter(pt), run_time=0.6)
        until(self, "A person's future conduct", lead=0.2)
        far = DashedLine([-1.2, r2, 0], [4.8, r2, 0], color=DIM, stroke_width=6)
        tip = Arrow([4.0, r2, 0], [5.3, r2, 0], buff=0, color=DIM, stroke_width=6, tip_length=0.25)
        self.play(FadeIn(l2), Create(far), Create(tip), run_time=0.6)
        until(self, "Between them sit arrest records", lead=0.2)
        c1 = Circle(radius=0.3, color=INK, stroke_width=5).move_to([-1.7, -0.45, 0])
        c2 = Circle(radius=0.3, color=INK, stroke_width=5).move_to([-1.7, -1.95, 0])
        n1, n2 = a4_label("policing", -1.7, 0.1, 34), a4_label("behavior", -1.7, -2.55, 34)
        rec = Rectangle(width=1.0, height=1.3, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([1.2, r3, 0])
        rl = VGroup(*[Line([0.9, r3 + dy, 0], [1.5, r3 + dy, 0], color=DIM, stroke_width=4) for dy in (0.3, 0.0, -0.3)])
        a1 = Arrow([-1.35, -0.55, 0], [0.65, -1.0, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        a2 = Arrow([-1.35, -1.85, 0], [0.65, -1.3, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        rn = a4_label("arrest records", 4.2, r3, 36)
        self.play(FadeIn(l3), Create(c1), Create(c2), FadeIn(n1), FadeIn(n2), run_time=0.6)
        self.play(Create(a1), Create(a2), Create(rec), Create(rl), FadeIn(rn), run_time=0.7)
        until(self, "ProPublica", lead=0.3)
        pp = a4_label("ProPublica, 2016", 4.4, -2.7, 34)
        self.play(FadeIn(pp), run_time=0.4)
        done(self)


# ── B34 · checking is cheap, finding is dear ────────────────────────────────────────────────────────────
class B34_Factors(Scene):
    def construct(self):
        div = Line([0.1, 2.7, 0], [0.1, -2.7, 0], color=GHOST, stroke_width=5)
        lc = a4_label("check", -3.2, 2.5, 40)
        lf = a4_label("find", 3.3, 2.5, 40)
        target = Rectangle(width=3.0, height=2.0, color=DIM, stroke_width=6).move_to([-3.2, 0.0, 0])
        cells = VGroup(*[Circle(radius=0.2, color=INK, stroke_width=4).move_to([1.15 + 0.7 * i, 1.2 - 0.7 * j, 0])
                         for j in range(4) for i in range(6)])
        self.add(div, lc, lf, target, cells)
        until(self, "Hand me the factors", lead=0.2)
        fw = Line([-4.7, -1.4, 0], [-1.7, -1.4, 0], color=INK, stroke_width=8)
        fh = Line([-5.1, -1.0, 0], [-5.1, 1.0, 0], color=INK, stroke_width=8)
        self.play(Create(fw), Create(fh), run_time=0.6)
        until(self, "multiply them", lead=0.3)
        fill = Rectangle(width=3.0, height=2.0, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=6).move_to([-3.2, 0.0, 0])
        self.play(FadeIn(fill), Create(check(-3.2, 0.0, 0.35, INK, 12)), run_time=0.6)
        until(self, "Finding them is hard", lead=0.2)
        hop = Dot(cells[0].get_center(), radius=0.14, color=TERRA)
        self.add(hop)
        path = [0, 1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12]
        step = 1 / 15
        for k in path[1:]:
            self.play(hop.animate.move_to(cells[k].get_center()), run_time=step, rate_func=linear)
        done(self)


# ── B35 · the asymmetry runs backwards ───────────────────────────────────────────────────────────────────
class B35_Backwards(Scene):
    def construct(self):
        lp = a4_label("produce", -5.0, 1.1)
        lv = a4_label("verify", -5.0, -0.5)
        axis = Line([-3.7, 1.9, 0], [-3.7, -1.3, 0], color=DIM, stroke_width=5)
        tag = a4_label("schematic", 4.9, 2.9, 32, DIM)
        self.add(lp, lv, axis, tag)
        until(self, "Producing an output is cheap", lead=0.2)
        pb = Rectangle(width=0.3, height=0.5, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([-3.55, 1.1, 0])
        pd = Dot([-3.0, 1.1, 0], radius=0.12, color=TERRA)
        self.play(FadeIn(pb), GrowFromCenter(pd), run_time=0.4)
        until(self, "Verifying it can take", lead=0.2)
        vb = Rectangle(width=6.6, height=0.5, fill_color=BAR2, fill_opacity=1, stroke_color=DIM, stroke_width=3).move_to([-0.4, -0.5, 0])
        vd = Dot([3.1, -0.5, 0], radius=0.12, color=TERRA)
        self.play(GrowFromEdge(vb, LEFT), run_time=2.2, rate_func=linear)
        self.play(GrowFromCenter(vd), run_time=0.3)
        until(self, "compare kinds of work", lead=0.3)
        cap = T("compares kinds of work,\nnot measured costs", 36).move_to([0, -2.4, 0])
        self.play(FadeIn(cap), run_time=0.5)
        done(self)


# ── B36 · the stream, the few checks, the one that was wrong ──────────────────────────────────────────────
class B36_Stream(Scene):
    def construct(self):
        def cell(i, j):
            return np.array([-4.4 + 1.1 * i, 1.8 - 1.15 * j, 0.0])
        circ = [[Circle(radius=0.33, color=DIM, stroke_width=5).move_to(cell(i, j)) for i in range(9)] for j in range(3)]
        until(self, "If you do not budget", lead=0.0)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in circ[0]], lag_ratio=0.2), run_time=1.4)
        until(self, "Outputs pour out", lead=0.2)
        self.play(LaggedStart(*[GrowFromCenter(c) for row in circ[1:] for c in row], lag_ratio=0.06), run_time=1.6)
        until(self, "checks do not", lead=0.2)
        marks = [check(*cell(i, j)[:2], 0.17, INK, 8) for (i, j) in ((1, 0), (5, 1), (7, 2))]
        self.play(*[Create(m) for m in marks], run_time=0.5)
        lg_c = check(-2.6, -2.55, 0.17, INK, 8)
        lg_t = a4_label("checked", -1.5, -2.55, 34)
        lg_o = Circle(radius=0.22, color=DIM, stroke_width=5).move_to([0.6, -2.55, 0])
        lg_u = a4_label("unchecked", 1.9, -2.55, 34)
        self.play(FadeIn(lg_c), FadeIn(lg_t), FadeIn(lg_o), FadeIn(lg_u), run_time=0.4)
        until(self, "until one is the patient", lead=0.2)
        p = cell(4, 2)
        wr = a4_x(p[0], p[1], 0.18, INK, 9)
        wd = Dot(p, radius=0.12, color=TERRA)
        self.play(Create(wr), GrowFromCenter(wd), run_time=0.5)
        lg_x = a4_x(3.9, -2.55, 0.17)
        lg_w = a4_label("wrong", 4.9, -2.55, 34)
        self.play(FadeIn(lg_x), FadeIn(lg_w), run_time=0.4)
        until(self, "the email never deleted", lead=0.3)
        self.play(Indicate(VGroup(wr, wd), scale_factor=1.5, color=INK), run_time=0.6)
        done(self)


# ── B37 · model checking model, the same hole ────────────────────────────────────────────────────────────
class B37_SameHole(Scene):
    def construct(self):
        lo = Rectangle(width=3.0, height=1.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-2.6, -1.0, 0])
        hl = DashedVMobject(Circle(radius=0.3, color=INK, stroke_width=5).move_to([-2.6, -1.0, 0]), num_dashes=12)
        l_lo = a4_label("model", 0.2, -1.0)
        self.add(lo, hl, l_lo)
        until(self, "another model, one layer up", lead=0.5)
        up = Rectangle(width=3.0, height=1.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-2.6, 1.4, 0])
        hu = DashedVMobject(Circle(radius=0.3, color=INK, stroke_width=5).move_to([-2.6, 1.4, 0]), num_dashes=12)
        l_up = a4_label("model", 0.2, 1.4)
        arr = Arrow([-2.6, -0.35, 0], [-2.6, 0.75, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        self.play(Create(up), Create(hu), FadeIn(l_up), Create(arr), run_time=0.8)
        until(self, "with the same problem", lead=0.3)
        guide = DashedLine([-2.6, -2.9, 0], [-2.6, 3.0, 0], color=GHOST, stroke_width=5)
        err = Dot([-2.6, -2.8, 0], radius=0.17, color=TERRA)
        self.add(guide, err)
        self.play(err.animate.move_to([-2.6, 2.9, 0]), run_time=1.0, rate_func=linear)
        until(self, "a human can do", lead=0.4)
        clip = VGroup(RoundedRectangle(width=2.0, height=2.6, corner_radius=0.15, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5),
                      Rectangle(width=0.8, height=0.3, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).shift(UP * 1.3)).move_to([4.0, 0.2, 0])
        ck = VGroup(*[check(3.5, y, 0.14, INK, 7) for y in (0.8, 0.2, -0.4)])
        ln = VGroup(*[Line([3.75, y, 0], [4.6, y, 0], color=DIM, stroke_width=4) for y in (0.8, 0.2, -0.4)])
        l_h = a4_label("human check", 4.0, -1.6, 34)
        self.play(FadeIn(clip), Create(ck), Create(ln), FadeIn(l_h), run_time=0.8)
        done(self)


# ══════════════════════════════ scenes_act5.py ══════════════════════════════
"""ACT VIII · Five things a supervisor does (B38-B43)   ACT IX · The fluency trap (B44-B49)

Cast, Act VIII: the FIVE SLOTS. B38 stands them up empty; B39-B42 show one small five-dot strip (top right) whose lit dot
marks which capacity is on screen; B43 lights all five and converges them on one decision.
Cast, Act IX: NODES and ARROWS (output -> confidence -> evaluation), a pair of sliders, a gate with a missing check.
Numbers on screen: only "5%" (spoken in B42, the chapter's own example), tagged "illustrative". No people tokens.
"""


def a5_card(w, h, color=DIM, sw=4, r=0.2):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_opacity=0, stroke_color=color, stroke_width=sw)


def a5_ghost_lines(cx, cy, w, n=3, gap=0.3, color=GHOST):
    """n ghost text lines (the shape of prose, no words) centred on (cx, cy)."""
    return VGroup(*[Line([cx - w / 2, cy + (n - 1) * gap / 2 - i * gap, 0], [cx + w / 2 - (0.6 if i == n - 1 else 0), cy + (n - 1) * gap / 2 - i * gap, 0],
                         color=color, stroke_width=5) for i in range(n)])


def a5_strip(active):
    """Five small dots, top right. Dots before `active` are done (ghost), `active` is lit (terracotta), the rest outline."""
    out = VGroup()
    for i in range(5):
        x = 2.4 + 0.8 * i
        if i == active:
            d = Circle(radius=0.19, fill_color=TERRA, fill_opacity=1, stroke_color=TERRA, stroke_width=2)
        elif i < active:
            d = Circle(radius=0.19, fill_color=GHOST, fill_opacity=1, stroke_color=DIM, stroke_width=3)
        else:
            d = Circle(radius=0.19, fill_opacity=0, stroke_color=DIM, stroke_width=3)
        out.add(d.move_to([x, 3.0, 0]))
    return out


def a5_title(s):
    return T(s, 40).move_to([-3.6, 3.0, 0])


def a5_dial(cx, cy, band_frac, needle_frac):
    """Semicircle dial. Returns (base, band, needle_at_up, pivot, angle_to_rotate)."""
    c = np.array([cx, cy, 0.0])
    base = Arc(radius=1.5, start_angle=PI, angle=-PI, color=GHOST, stroke_width=16).move_arc_center_to(c)
    band = Arc(radius=1.5, start_angle=PI, angle=-PI * band_frac, color=INK, stroke_width=16).move_arc_center_to(c)
    needle = Line(c, c + np.array([0, 1.3, 0]), color=INK, stroke_width=7)
    pivot = Dot(c, radius=0.13, color=INK)
    return base, band, needle, pivot, PI * (0.5 - needle_frac), c


# ═════════════════════════════ ACT VIII ═════════════════════════════

class B38_FiveSlots(Scene):
    def construct(self):
        head = T("The supervisor", 40).move_to([0, 2.7, 0])
        base = Line([-5.9, -1.9, 0], [5.9, -1.9, 0], color=GHOST, stroke_width=5)
        self.add(head, base)
        xs = [-4.6, -2.3, 0.0, 2.3, 4.6]
        slots = [a5_card(1.9, 2.2, DIM, 5).move_to([x, 0.1, 0]) for x in xs]
        self.play(LaggedStart(*[Create(s) for s in slots], lag_ratio=0.25), run_time=1.5)
        until(self, "Capacities", lead=0.2)
        until(self, "things a person can do", lead=0.1)
        holes = [DashedVMobject(Circle(radius=0.55, color=DIM, stroke_width=4).move_to([x, 0.1, 0]), num_dashes=14, dashed_ratio=0.55) for x in xs]
        self.play(LaggedStart(*[Create(h) for h in holes], lag_ratio=0.15), run_time=0.9)
        until(self, "There are five", lead=0.45)
        nums = [T(str(i + 1), 44).move_to([x, -1.4, 0]) for i, x in enumerate(xs)]
        self.play(LaggedStart(*[FadeIn(n) for n in nums], lag_ratio=0.1), run_time=0.6)
        dot = Dot([xs[4] + 0.75, 1.0, 0], radius=0.13, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.3)
        done(self)


class B39_Twitch(Scene):
    def construct(self):
        title, strip = a5_title("Plausibility auditing"), a5_strip(0)
        cloud = Circle(radius=2.0, color=DIM, stroke_width=5).move_to([-1.9, -0.35, 0])
        spots = [(-2.6, 0.2), (-1.5, 0.7), (-2.2, -0.6), (-1.1, -0.1), (-1.9, -1.2), (-0.8, -0.9), (-2.7, 0.9), (-1.6, 0.0), (-1.4, -1.6)]
        dots = VGroup(*[Dot([x, y, 0], radius=0.1, color=BAR2) for x, y in spots])
        k_l = T("known world", 36, DIM).move_to([-1.9, -2.75, 0])
        self.add(title, strip, cloud, dots, k_l)
        until(self, "the kind of thing that could be true", lead=0.3)
        o_l = T("score", 36).move_to([3.9, 0.95, 0])
        out = Dot([5.0, 0.35, 0], radius=0.2, color=INK)
        self.play(FadeIn(out), FadeIn(o_l), run_time=0.3)
        self.play(out.animate.move_to([2.3, -0.35, 0]), run_time=0.9)
        until(self, "feels a twitch", lead=0.2)
        for dx in (-0.16, 0.32, -0.32, 0.16):
            self.play(out.animate.shift(RIGHT * dx), run_time=0.09)
        ring1 = Circle(radius=0.5, color=INK, stroke_width=6).move_to(out.get_center())
        ring2 = Circle(radius=0.85, color=DIM, stroke_width=4).move_to(out.get_center())
        mark = Dot([2.3, 0.62, 0], radius=0.1, color=TERRA)
        t_l = T("twitch", 38).move_to([4.6, -1.35, 0])
        self.play(Create(ring1), run_time=0.3)
        self.play(Create(ring2), GrowFromCenter(mark), FadeIn(t_l), run_time=0.4)
        done(self)


class B40_TwoQuestions(Scene):
    def construct(self):
        title, strip = a5_title("Problem formulation"), a5_strip(1)
        q1 = a5_card(4.8, 1.5, INK, 6).move_to([-2.4, 1.0, 0])
        q1t = T("Which category?", 40).move_to([-2.4, 1.0, 0])
        q2 = a5_card(4.8, 1.5, DIM, 4).move_to([-2.4, -1.2, 0])
        q2t = T("Life-threatening?", 40, DIM).move_to([-2.4, -1.2, 0])
        self.add(title, strip, q1, q1t)
        box1 = Square(side_length=1.0, color=DIM, stroke_width=5).move_to([2.0, 1.0, 0])
        self.add(box1)
        until(self, "The triage system answered", lead=0.2)
        self.play(Create(check(2.0, 1.0, 0.3, INK, 10)), run_time=0.5)
        a1 = T("answered", 38).move_to([4.5, 1.0, 0])
        self.play(FadeIn(a1), run_time=0.3)
        until(self, "The clinical question was", lead=0.4)
        self.play(FadeIn(q2t), Create(DashedVMobject(q2.copy(), num_dashes=26, dashed_ratio=0.55)), run_time=0.7)
        box2 = Square(side_length=1.0, color=DIM, stroke_width=5).move_to([2.0, -1.2, 0])
        self.play(Create(box2), run_time=0.4)
        until(self, "never asked", lead=0.4)
        a2 = T("never asked", 38).move_to([4.6, -1.2, 0])
        gap = Dot([2.0, -1.2, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(a2), GrowFromCenter(gap), run_time=0.4)
        done(self)


class B41_FourOptions(Scene):
    def construct(self):
        title, strip = a5_title("Tool orchestration"), a5_strip(2)
        task = a5_card(3.0, 1.7, DIM, 6).move_to([-4.35, -0.1, 0])
        task_t = T("Sub-problem", 36).move_to([-4.35, -0.1, 0])
        self.add(title, strip, task, task_t)
        labels = ["AI model", "A person", "Second model", "No tool yet"]
        ys = [1.55, 0.35, -0.85, -2.05]
        cards, texts, arrows = [], [], []
        until(self, "An AI, a person", lead=0.3)
        for i in range(4):
            c = a5_card(3.6, 0.95, DIM, 4).move_to([2.5, ys[i], 0])
            t = T(labels[i], 38).move_to([2.5, ys[i], 0])
            a = Arrow([-2.75, -0.1, 0], [0.55, ys[i], 0], buff=0, color=DIM, stroke_width=4, tip_length=0.18)
            cards.append(c); texts.append(t); arrows.append(a)
            if i < 3:
                self.play(Create(a), Create(c), FadeIn(t), run_time=0.45)
        until(self, "the hardest call of all", lead=0.3)
        self.play(Create(arrows[3]), Create(cards[3]), FadeIn(texts[3]), run_time=0.5)
        until(self, "Saying we should not deploy", lead=0.3)
        ring = a5_card(3.9, 1.2, INK, 8).move_to([2.5, ys[3], 0])
        spark = Dot([4.55, ys[3] + 0.55, 0], radius=0.13, color=TERRA)
        self.play(Create(ring), GrowFromCenter(spark), arrows[3].animate.set_color(INK).set_stroke(width=7), run_time=0.6)
        done(self)


class B42_SameNumber(Scene):
    def construct(self):
        title, strip = a5_title("Interpretive judgment"), a5_strip(3)
        hero = T("5%", 76).move_to([0, 1.95, 0])
        b1, band1, n1, p1, ang1, c1 = a5_dial(-3.2, -0.5, 0.45, 0.2)
        b2, band2, n2, p2, ang2, c2 = a5_dial(3.2, -0.5, 0.08, 0.2)
        l1 = T("Spam filter", 40).move_to([-3.2, -1.4, 0])
        l2 = T("Cancer screen", 40).move_to([3.2, -1.4, 0])
        cap = T("illustrative", 32, DIM).move_to([0, -3.0, 0])
        self.add(title, strip, hero, b1, b2, l1, l2, cap)
        self.play(Create(band1), Create(band2), run_time=0.5)
        until(self, "A five percent false-positive rate", lead=0.2)
        self.play(FadeIn(n1), FadeIn(p1), FadeIn(n2), FadeIn(p2), run_time=0.3)
        self.play(Rotate(n1, angle=ang1, about_point=c1), Rotate(n2, angle=ang2, about_point=c2), run_time=0.9)
        until(self, "suits a spam filter", lead=0.2)
        self.play(Create(check(-3.2, -2.25, 0.34, INK, 10)), run_time=0.5)
        until(self, "catastrophic", lead=0.3)
        x1 = Line([2.85, -1.95, 0], [3.55, -2.65, 0], color=INK, stroke_width=10)
        x2 = Line([2.85, -2.65, 0], [3.55, -1.95, 0], color=INK, stroke_width=10)
        self.play(Create(x1), Create(x2), run_time=0.5)
        done(self)


class B43_OneDecision(Scene):
    def construct(self):
        title = T("Executive integration", 40).move_to([-3.6, 3.0, 0])
        names = ["Plausibility", "Formulation", "Tools", "Judgment", "Integration"]
        ys = [1.9, 0.95, 0.0, -0.95, -1.9]
        self.add(title)
        until(self, "combining tools", lead=0.2)
        nodes, labs = [], []
        for i in range(5):
            n = Circle(radius=0.34, fill_color=TERRA, fill_opacity=1, stroke_color=TERRA, stroke_width=2).move_to([-3.1, ys[i], 0])
            nodes.append(n)
            labs.append(T(names[i], 36).move_to([-5.0, ys[i], 0]))
        self.play(LaggedStart(*[FadeIn(VGroup(n, l)) for n, l in zip(nodes, labs)], lag_ratio=0.25), run_time=1.3)
        until(self, "one decision", lead=0.2)
        box = a5_card(3.0, 1.5, INK, 7).move_to([3.5, 0, 0])
        box_t = T("Decision", 40).move_to([3.5, 0, 0])
        arrows = [Arrow([-2.6, ys[i], 0], [1.85, ys[i] * 0.35, 0], buff=0, color=DIM, stroke_width=4, tip_length=0.16) for i in range(5)]
        self.play(Create(box), FadeIn(box_t), run_time=0.5)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15), run_time=1.2)
        until(self, "Somewhere the buck must stop", lead=0.2)
        pole = Line([3.5, 0.75, 0], [3.5, 1.75, 0], color=INK, stroke_width=6)
        flag = Polygon([3.5, 1.75, 0], [4.4, 1.5, 0], [3.5, 1.25, 0], fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4)
        owner = Dot([3.5, 1.75, 0], radius=0.13, color=TERRA)
        o_l = T("owner", 36).move_to([5.3, 1.5, 0])
        self.play(Create(pole), Create(flag), GrowFromCenter(owner), FadeIn(o_l), run_time=0.6)
        until(self, "you have found a gap", lead=0.3)
        hole = DashedVMobject(Circle(radius=0.34, color=DIM, stroke_width=5).move_to([-3.1, ys[2], 0]), num_dashes=12, dashed_ratio=0.55)
        g_l = T("gap", 40).move_to([-0.6, 0.0, 0])
        self.play(FadeOut(nodes[2]), FadeOut(arrows[2]), Create(hole), FadeIn(g_l), run_time=0.7)
        done(self)


# ═════════════════════════════ ACT IX ═════════════════════════════

class B44_TwoCards(Scene):
    def construct(self):
        head = T("Botspeak", 40).move_to([0, 3.0, 0])
        c1 = a5_card(3.0, 1.9, INK, 6).move_to([-4.5, 0.5, 0])
        t1 = T("Strategic\ndelegation", 38).move_to([-4.5, 0.5, 0])
        self.add(head)
        until(self, "Strategic delegation", lead=0.3)
        ai = a5_card(1.8, 1.3, DIM, 5).move_to([0, 0.5, 0])
        ai_t = T("AI", 42).move_to([0, 0.5, 0])
        a_out = Arrow([-2.95, 0.5, 0], [-1.0, 0.5, 0], buff=0, color=INK, stroke_width=6, tip_length=0.2)
        self.play(Create(c1), FadeIn(t1), run_time=0.5)
        self.play(Create(a_out), Create(ai), FadeIn(ai_t), run_time=0.6)
        until(self, "Critical evaluation", lead=0.5)
        c2 = a5_card(3.0, 1.9, INK, 6).move_to([4.5, 0.5, 0])
        t2 = T("Critical\nevaluation", 38).move_to([4.5, 0.5, 0])
        a_in = Arrow([1.0, 0.5, 0], [2.95, 0.5, 0], buff=0, color=INK, stroke_width=6, tip_length=0.2)
        self.play(Create(a_in), Create(c2), FadeIn(t2), run_time=0.6)
        until(self, "criteria you set before", lead=0.3)
        sheet = a5_card(1.7, 1.4, DIM, 4).move_to([4.5, -2.1, 0])
        lines = a5_ghost_lines(4.5, -2.1, 1.1, 3, 0.3, DIM)
        s_l = T("set first", 36, DIM).move_to([1.9, -2.1, 0])
        up = Arrow([4.5, -1.35, 0], [4.5, -0.55, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.16)
        self.play(Create(sheet), Create(lines), FadeIn(s_l), Create(up), run_time=0.7)
        done(self)


class B45_TwoSteps(Scene):
    def construct(self):
        xs = [-4.5, 0.0, 4.5]
        nodes = [Circle(radius=0.85, color=INK if i == 0 else DIM, stroke_width=6 if i == 0 else 5).move_to([xs[i], 1.1, 0]) for i in range(3)]
        wave = ParametricFunction(lambda t: np.array([xs[0] + t, 1.1 + 0.28 * np.sin(t * 5.2), 0]), t_range=[-0.55, 0.55], color=INK, stroke_width=6)
        self.add(nodes[0], wave)
        l1 = T("Fluent\noutput", 36).move_to([xs[0], -0.55, 0])
        self.add(l1)
        until(self, "the more confident you are in the output", lead=0.4)
        a1 = Arrow([-3.5, 1.1, 0], [-1.0, 1.1, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        self.play(Create(a1), Create(nodes[1]), run_time=0.7)
        g1 = Arc(radius=0.5, start_angle=PI, angle=-PI * 0.8, color=INK, stroke_width=7).move_arc_center_to([xs[1], 0.95, 0])
        self.play(Create(g1), FadeIn(T("Confidence\nin answer", 36).move_to([xs[1], -0.55, 0])), run_time=0.6)
        until(self, "Then that confidence raises", lead=0.3)
        a2 = Arrow([1.0, 1.1, 0], [3.5, 1.1, 0], buff=0, color=INK, stroke_width=9, tip_length=0.3)
        tdot = Dot([2.25, 1.75, 0], radius=0.15, color=TERRA)
        self.play(Create(a2), Create(nodes[2]), GrowFromCenter(tdot), run_time=0.7)
        g2 = Arc(radius=0.5, start_angle=PI, angle=-PI * 0.9, color=INK, stroke_width=7).move_arc_center_to([xs[2], 0.95, 0])
        g2b = Arc(radius=0.3, start_angle=PI, angle=-PI * 0.9, color=DIM, stroke_width=6).move_arc_center_to([xs[2], 0.95, 0])
        self.play(Create(g2), Create(g2b), FadeIn(T("Confidence\nin judgment", 36).move_to([xs[2], -0.55, 0])), run_time=0.6)
        until(self, "any answer of the same shape", lead=0.4)
        sq = [Square(side_length=0.8, color=DIM, stroke_width=5).move_to([-1.5 + 1.5 * i, -2.45, 0]) for i in range(3)]
        lab = T("same shape", 36, DIM).move_to([4.2, -2.45, 0])
        self.play(LaggedStart(*[Create(s) for s in sq], lag_ratio=0.25), FadeIn(lab), run_time=0.8)
        self.play(LaggedStart(*[Create(check(-1.5 + 1.5 * i, -2.45, 0.22, INK, 8)) for i in range(3)], lag_ratio=0.3), run_time=0.9)
        done(self)


class B46_FormContent(Scene):
    def construct(self):
        head = T("Independent", 40).move_to([-3.6, 3.0, 0])
        # two sliders (left)
        tr1 = Line([-5.9, 1.5, 0], [-1.7, 1.5, 0], color=BAR1, stroke_width=8)
        tr2 = Line([-5.9, -0.5, 0], [-1.7, -0.5, 0], color=BAR1, stroke_width=8)
        k1 = Dot([-3.8, 1.5, 0], radius=0.22, color=INK)
        k2 = Dot([-3.8, -0.5, 0], radius=0.22, color=INK)
        n1 = T("Form", 40).move_to([-3.8, 2.2, 0])
        n2 = T("Content", 40).move_to([-3.8, 0.2, 0])
        e1a, e1b = T("plain", 32, DIM).move_to([-5.3, 0.85, 0]), T("fluent", 32, DIM).move_to([-2.3, 0.85, 0])
        e2a, e2b = T("wrong", 32, DIM).move_to([-5.3, -1.15, 0]), T("right", 32, DIM).move_to([-2.3, -1.15, 0])
        # plane (right)
        plane = Square(side_length=3.6, color=DIM, stroke_width=5).move_to([3.6, 0, 0])
        vx = Line([3.6, -1.8, 0], [3.6, 1.8, 0], color=GHOST, stroke_width=4)
        hx = Line([1.8, 0, 0], [5.4, 0, 0], color=GHOST, stroke_width=4)
        self.add(head, tr1, tr2, n1, n2, e1a, e1b, e2a, e2b, k1, k2, plane, vx, hx)
        until(self, "Form and content are independent", lead=0.2)
        self.play(k1.animate.move_to([-2.4, 1.5, 0]), run_time=0.7)
        self.play(k2.animate.move_to([-5.0, -0.5, 0]), run_time=0.7)
        until(self, "AI broke that link", lead=0.3)
        self.play(k1.animate.move_to([-5.0, 1.5, 0]), k2.animate.move_to([-2.4, -0.5, 0]), run_time=0.8)
        until(self, "maximally fluent and maximally wrong", lead=1.0)
        self.play(k1.animate.move_to([-2.4, 1.5, 0]), k2.animate.move_to([-5.0, -0.5, 0]), run_time=0.8)
        pt = Dot([4.9, -1.2, 0], radius=0.2, color=TERRA)
        ring = Circle(radius=0.45, color=INK, stroke_width=6).move_to([4.9, -1.2, 0])
        c_l = T("fluent, wrong", 36).move_to([3.6, -2.45, 0])
        self.play(GrowFromCenter(pt), Create(ring), FadeIn(c_l), run_time=0.6)
        done(self)


class B47_MissingCheck(Scene):
    def construct(self):
        report = a5_card(4.6, 1.8, DIM, 6).move_to([-3.6, 0.55, 0])
        q = T("Email account RESET\ncompleted", 34).move_to([-3.6, 0.55, 0])
        r_l = T("report", 36).move_to([-3.6, 2.0, 0])
        self.add(report, q, r_l)
        src = T("Shapira et al., 2026", 32, DIM).move_to([0, -3.0, 0])
        self.add(src)
        until(self, "fluent and well formed", lead=0.3)
        path = Line([-1.2, 0.55, 0], [2.2, 0.55, 0], color=DIM, stroke_width=5)
        gate = DashedVMobject(Circle(radius=0.65, color=DIM, stroke_width=5).move_to([0.2, 0.55, 0]), num_dashes=16, dashed_ratio=0.55)
        g_l = T("no check", 36, DIM).move_to([0.2, 1.75, 0])
        world = a5_card(2.4, 1.8, DIM, 6).move_to([4.7, 0.55, 0])
        w_l = T("world", 36).move_to([4.7, 2.0, 0])
        env = VGroup(Rectangle(width=1.2, height=0.8, color=INK, stroke_width=5),
                     Line([-0.6, 0.4, 0], [0, 0.0, 0], color=INK, stroke_width=5), Line([0, 0.0, 0], [0.6, 0.4, 0], color=INK, stroke_width=5)).move_to([4.7, 0.55, 0])
        self.play(Create(path), Create(gate), FadeIn(g_l), run_time=0.7)
        self.play(Create(world), FadeIn(w_l), Create(env), run_time=0.7)
        until(self, "The prose did the checking", lead=0.3)
        pulse = Dot([-1.2, 0.55, 0], radius=0.17, color=TERRA)
        self.play(FadeIn(pulse), run_time=0.15)
        self.play(pulse.animate.move_to([2.2, 0.55, 0]), run_time=1.1)
        until(self, "not let fluency do epistemic work", lead=0.5)
        still = T("still there", 36).move_to([4.7, -1.1, 0])
        self.play(FadeIn(still), Indicate(env, color=INK, scale_factor=1.15), run_time=0.7)
        done(self)


class B48_OrderOfOperations(Scene):
    def construct(self):
        head = T("Order", 40).move_to([0, 3.0, 0])
        self.add(head)
        n1, n2, n3 = [T(s, 46).move_to([x, 2.0, 0]) for s, x in zip("123", (-4.6, -0.6, 3.5))]
        crit = a5_card(2.8, 1.9, INK, 6).move_to([-4.6, 0.2, 0])
        crit_l = a5_ghost_lines(-4.6, 0.2, 1.6, 3, 0.32, DIM)
        c_t = T("criterion", 36).move_to([-4.6, -1.4, 0])
        self.add(n1)
        until(self, "write down what a wrong answer would look like", lead=0.6)
        body = RoundedRectangle(width=0.8, height=0.6, corner_radius=0.08, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-3.6, 0.9, 0])
        shackle = Arc(radius=0.22, start_angle=0, angle=PI, color=INK, stroke_width=6).move_arc_center_to([-3.6, 1.18, 0])
        self.play(Create(crit), Create(crit_l), FadeIn(c_t), run_time=0.6)
        self.play(Create(body), Create(shackle), run_time=0.4)
        until(self, "Then read it", lead=0.3)
        a1 = Arrow([-3.0, 0.2, 0], [-1.9, 0.2, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18)
        out = a5_card(2.0, 1.9, DIM, 5).move_to([-0.6, 0.2, 0])
        out_l = a5_ghost_lines(-0.6, 0.2, 1.2, 3, 0.32, GHOST)
        o_t = T("output", 36).move_to([-0.6, -1.4, 0])
        self.play(FadeIn(n2), Create(a1), Create(out), Create(out_l), FadeIn(o_t), run_time=0.8)
        until(self, "record pass, fail, or unknown", lead=0.5)
        a2 = Arrow([0.6, 0.2, 0], [1.6, 0.2, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18)
        self.play(FadeIn(n3), Create(a2), run_time=0.4)
        for i, s in enumerate(["pass", "fail", "unknown"]):
            p = a5_card(2.6, 0.8, INK if s == "unknown" else DIM, 5).move_to([3.5, 1.0 - 1.0 * i, 0])
            t = T(s, 38).move_to([3.5, 1.0 - 1.0 * i, 0])
            self.play(Create(p), FadeIn(t), run_time=0.4)
        done(self)


class B49_Diverge(Scene):
    def construct(self):
        title = T("Where they part", 40).move_to([-3.6, 3.0, 0])
        ax = Arrow([-5.6, -2.3, 0], [5.8, -2.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        ay = Arrow([-5.6, -2.3, 0], [-5.6, 2.4, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        fam = T("familiar", 36, DIM).move_to([-4.1, -2.85, 0])
        edge = T("edge cases", 36, DIM).move_to([4.1, -2.85, 0])
        cap = T("schematic", 32, DIM).move_to([-4.2, 2.45, 0])
        self.add(title, ax, ay, fam, edge, cap)
        until(self, "learn to produce outputs that resemble correct ones", lead=0.5)

        def res(t):                 # resemblance stays high
            return np.array([t, 1.5 - 0.1 * (t + 5.0) / 10.0, 0])

        def cor(t):                 # correctness tracks it, then falls away at the edge
            f = 1.5 - 0.1 * (t + 5.0) / 10.0
            drop = 3.1 / (1.0 + np.exp(-(t - 2.2) * 2.2))
            return np.array([t, f - drop, 0])

        c_res = ParametricFunction(res, t_range=[-5.0, 5.0], color=INK, stroke_width=8)
        c_cor = ParametricFunction(cor, t_range=[-5.0, 5.0], color=BAR1, stroke_width=8)
        self.play(Create(c_res), Create(c_cor), run_time=2.6)
        r_l = T("sounds right", 36).move_to([-1.3, 2.2, 0])
        k_l = T("is right", 36, DIM).move_to([-3.3, -0.35, 0])
        self.play(FadeIn(r_l), FadeIn(k_l), run_time=0.4)
        until(self, "Where resemblance and correctness come apart", lead=0.4)
        gap = dim_arrow([5.15, 1.0, 0], [5.15, -1.45, 0], INK, 6)
        spark = Dot([5.15, -1.95, 0], radius=0.13, color=TERRA)
        self.play(Create(gap), GrowFromCenter(spark), run_time=0.6)
        done(self)


# ══════════════════════════════ scenes_act6.py ══════════════════════════════
"""ACT X · Skepticism as a team practice  (B50-B55, all Manim)

One cast for the act: outlined cards, round check-circles, a post/gate on a track, and ONE terracotta dot (the thing that
slips through, the gap, the failure). Nothing is a person. Numbers on screen: none (all schematic); the only quoted
words are the report line in B53, taken from the Agents of Chaos paper (factcheck/PRIMARIES.md).
"""


def a10_post(x, y, color=INK):
    """A gate post: a vertical bar with a cross-bar on top."""
    return VGroup(Line([x, y - 0.55, 0], [x, y + 0.55, 0], color=color, stroke_width=8),
                  Line([x - 0.3, y + 0.55, 0], [x + 0.3, y + 0.55, 0], color=color, stroke_width=8))


def a10_chk(x, y, r=0.32, color=INK):
    """A check inside a ring."""
    return VGroup(Circle(radius=r, color=color, stroke_width=5).move_to([x, y, 0]),
                  check(x, y + 0.02, 0.17, color, 6))


def a10_card(x, y, w, h, color=DIM, sw=4):
    return RoundedRectangle(width=w, height=h, corner_radius=0.2, fill_opacity=0, stroke_color=color, stroke_width=sw).move_to([x, y, 0])


def a10_env(x, y, w=1.1, h=0.74, color=INK, sw=5):
    """An envelope: outline plus the V flap."""
    return VGroup(Rectangle(width=w, height=h, stroke_color=color, stroke_width=sw, fill_opacity=0).move_to([x, y, 0]),
                  Line([x - w / 2, y + h / 2, 0], [x, y - 0.02, 0], color=color, stroke_width=sw),
                  Line([x + w / 2, y + h / 2, 0], [x, y - 0.02, 0], color=color, stroke_width=sw))


def a10_cross(x, y, s=0.22, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


# ── B50 · one checkpoint vs the moves built into the workflow ────────────────────────────────────────────────
class B50_Fragile(Scene):
    def construct(self):
        y1, y2 = 1.2, -1.6
        tr1 = Line([-5.7, y1, 0], [5.7, y1, 0], color=DIM, stroke_width=5)
        lab1 = T("one checkpoint", 34).move_to([-4.0, y1 + 1.0, 0])
        post1 = a10_post(0.8, y1)
        self.add(tr1, lab1, post1)
        a = Dot([-4.6, y1, 0], radius=0.2, color=BAR1)
        bad = Dot([-3.0, y1, 0], radius=0.2, color=TERRA)
        self.play(GrowFromCenter(a), GrowFromCenter(bad), run_time=0.5)
        self.play(a.animate.move_to([0.8, y1, 0]), run_time=0.8)
        ck1 = a10_chk(0.8, y1 + 1.1)
        self.play(Create(ck1), run_time=0.4)
        self.play(a.animate.move_to([5.0, y1, 0]), run_time=0.8)
        until(self, "It depends", lead=0.3)
        self.play(post1.animate.set_color(GHOST), FadeOut(ck1), run_time=0.5)
        miss = T("missed", 34).move_to([0.8, y1 - 1.0, 0])
        self.play(FadeIn(miss), run_time=0.3)
        until(self, "remembering", lead=0.8)
        self.play(bad.animate.move_to([4.2, y1, 0]), run_time=1.0)
        until(self, "Durable teams", lead=0.3)
        tr2 = Line([-5.7, y2, 0], [5.7, y2, 0], color=DIM, stroke_width=5)
        lab2 = T("built in", 34).move_to([-4.6, y2 + 1.0, 0])
        xs = [-2.4, 0.4, 3.2]
        posts = [a10_post(x, y2) for x in xs]
        cks = [a10_chk(x, y2 + 1.1) for x in xs]
        self.play(Create(tr2), FadeIn(lab2), *[Create(p) for p in posts], run_time=0.5)
        a2 = Dot([-5.0, y2, 0], radius=0.2, color=BAR1)
        bad2 = Dot([-5.6, y2, 0], radius=0.2, color=TERRA)
        self.play(GrowFromCenter(a2), GrowFromCenter(bad2), run_time=0.3)
        self.play(a2.animate.move_to([5.0, y2, 0]), LaggedStart(*[Create(c) for c in cks], lag_ratio=0.35),
                  bad2.animate.move_to([-3.2, y2, 0]), run_time=1.2)
        ring = Circle(radius=0.36, color=INK, stroke_width=5).move_to([-3.2, y2, 0])
        self.play(Create(ring), run_time=0.3)
        done(self)


# ── B51 · three insert points; "nobody" is the undefended gap ────────────────────────────────────────────────
class B51_InsertPoints(Scene):
    def construct(self):
        xs = [-4.4, -1.5, 1.4, 4.3]
        ys = -0.9
        cy = 1.0
        segs = VGroup(*[Line([xs[i] + 0.45, ys, 0], [xs[i + 1] - 0.45, ys, 0], color=DIM, stroke_width=5) for i in range(3)])
        circs = VGroup(*[Circle(radius=0.45, color=DIM, stroke_width=5).move_to([x, ys, 0]) for x in xs])
        names = ["ship", "run", "review", "act"]
        labs = VGroup(*[T(n, 40).move_to([x, -1.9, 0]) for n, x in zip(names, xs)])
        self.add(segs, circs, labs)
        tops = ["checklist", "monitoring", "handoff"]

        def stem(x):
            return Line([x, cy - 0.75, 0], [x, ys + 0.45, 0], color=DIM, stroke_width=5)

        def top_lab(t, x):
            return T(t, 40).move_to([x, 2.4, 0])

        # 1 checklist
        c1 = a10_card(xs[0], cy, 1.9, 1.5, INK)
        c1_in = VGroup(check(xs[0] - 0.55, cy + 0.36, 0.22, INK, 6), Line([xs[0] - 0.3, cy + 0.36, 0], [xs[0] + 0.6, cy + 0.36, 0], color=DIM, stroke_width=5),
                       Line([xs[0] - 0.62, cy - 0.02, 0], [xs[0] + 0.6, cy - 0.02, 0], color=DIM, stroke_width=5),
                       Line([xs[0] - 0.62, cy - 0.4, 0], [xs[0] + 0.6, cy - 0.4, 0], color=DIM, stroke_width=5))
        self.play(Create(c1), Create(c1_in), Create(stem(xs[0])), FadeIn(top_lab(tops[0], xs[0])), run_time=0.6)
        # 2 monitoring
        until(self, "Put the falsification conditions", lead=0.25)
        c2 = a10_card(xs[1], cy, 1.9, 1.5, INK)
        zz = [(-0.7, -0.25), (-0.35, 0.2), (0.0, -0.1), (0.35, 0.3), (0.7, 0.0)]
        c2_in = VGroup(*[Line([xs[1] + zz[i][0], cy + zz[i][1], 0], [xs[1] + zz[i + 1][0], cy + zz[i + 1][1], 0], color=INK, stroke_width=5) for i in range(4)])
        self.play(Create(c2), Create(c2_in), Create(stem(xs[1])), FadeIn(top_lab(tops[1], xs[1])), run_time=0.6)
        # 3 handoff
        until(self, "Put the shift questions", lead=0.25)
        c3 = a10_card(xs[2], cy, 1.9, 1.5, INK)
        c3_in = VGroup(Circle(radius=0.22, color=INK, stroke_width=5).move_to([xs[2] - 0.55, cy, 0]),
                       Circle(radius=0.22, color=INK, stroke_width=5).move_to([xs[2] + 0.55, cy, 0]),
                       Line([xs[2] - 0.33, cy, 0], [xs[2] + 0.33, cy, 0], color=INK, stroke_width=5))
        self.play(Create(c3), Create(c3_in), Create(stem(xs[2])), FadeIn(top_lab(tops[2], xs[2])), run_time=0.6)
        # the question walks the line
        until(self, "For each capacity", lead=0.2)
        ring = Circle(radius=0.64, color=INK, stroke_width=6).move_to([xs[0], ys, 0])
        self.play(Create(ring), run_time=0.4)
        until(self, "by whom", lead=0.3)
        self.play(ring.animate.move_to([xs[1], ys, 0]), run_time=0.4)
        until(self, "seeing what", lead=0.3)
        self.play(ring.animate.move_to([xs[2], ys, 0]), run_time=0.4)
        until(self, "nobody", lead=0.5)
        self.play(ring.animate.move_to([xs[3], ys, 0]), run_time=0.4)
        c4 = a10_card(xs[3], cy, 1.9, 1.5, GHOST, 5)
        q_dot = Dot([xs[3], cy, 0], radius=0.2, color=TERRA)
        self.play(Create(c4), GrowFromCenter(q_dot), FadeIn(top_lab("nobody", xs[3])), run_time=0.5)
        gap = T("undefended gap", 40).move_to([3.8, -2.7, 0])
        self.play(FadeIn(gap), run_time=0.4)
        done(self)


# ── B52 · before run / during run / before action ────────────────────────────────────────────────────────────
class B52_ThreeCheckpoints(Scene):
    def construct(self):
        xs = [-3.9, 0.0, 3.9]
        line = Line([-5.8, 2.0, 0], [5.8, 2.0, 0], color=DIM, stroke_width=5)
        phases = ["before run", "during run", "before action"]
        plabs = VGroup(*[T(p, 34).move_to([x, 2.65, 0]) for p, x in zip(phases, xs)])
        self.add(line, plabs)
        pdots = [Dot([x, 2.0, 0], radius=0.14, color=INK) for x in xs]
        # 1 lock the prediction
        body = RoundedRectangle(width=1.3, height=1.0, corner_radius=0.15, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([xs[0], 0.45, 0])
        shackle = Arc(radius=0.4, start_angle=0, angle=PI, color=INK, stroke_width=5).move_to([xs[0], 1.4, 0])
        key = Dot([xs[0], 0.45, 0], radius=0.1, color=INK)
        self.play(GrowFromCenter(pdots[0]), Create(body), Create(shackle), run_time=0.5)
        self.play(shackle.animate.move_to([xs[0], 1.15, 0]), GrowFromCenter(key), run_time=0.4)
        p_lab = T("prediction", 34).move_to([xs[0], -0.55, 0])
        self.add(p_lab)
        # 2 keep the record
        until(self, "Keep the record", lead=0.3)
        self.play(GrowFromCenter(pdots[1]), run_time=0.3)
        rec = []
        for i, yy in enumerate([1.0, 0.55, 0.1]):
            ln = Line([xs[1] - 0.9, yy, 0], [xs[1] + 0.5 + 0.2 * (i % 2), yy, 0], color=DIM, stroke_width=6)
            dt = Dot([xs[1] - 1.1, yy, 0], radius=0.09, color=INK)
            rec.append(VGroup(dt, ln))
            self.play(Create(ln), GrowFromCenter(dt), run_time=0.3)
        r_lab = T("record", 34).move_to([xs[1], -0.55, 0])
        self.add(r_lab)
        # 3 a named check of the actual state
        until(self, "Before action", lead=0.3)
        self.play(GrowFromCenter(pdots[2]), run_time=0.3)
        scard = a10_card(xs[2] + 0.1, 0.55, 1.7, 1.2, DIM)
        lens = Circle(radius=0.5, color=INK, stroke_width=6).move_to([xs[2] - 0.2, 0.75, 0])
        handle = Line([xs[2] + 0.16, 0.39, 0], [xs[2] + 0.62, -0.05, 0], color=INK, stroke_width=8)
        self.play(Create(scard), Create(lens), Create(handle), run_time=0.6)
        s_lab = T("actual state", 34).move_to([xs[2], -0.55, 0])
        self.add(s_lab)
        # ledger
        until(self, "Keep the original prediction", lead=0.3)
        led = a10_card(0.0, -2.2, 7.0, 1.9, DIM)
        t1 = T("predicted", 34).move_to([-2.4, -1.85, 0])
        l1 = Line([0.2, -1.85, 0], [1.9, -1.85, 0], color=INK, stroke_width=6)
        self.play(Create(led), FadeIn(t1), Create(l1), run_time=0.6)
        until(self, "append what you observed", lead=0.3)
        t2 = T("observed", 34).move_to([-2.4, -2.6, 0])
        l2 = Line([0.2, -2.6, 0], [1.4, -2.6, 0], color=INK, stroke_width=6)
        dt2 = Dot([1.7, -2.6, 0], radius=0.12, color=TERRA)
        self.play(FadeIn(t2), Create(l2), GrowFromCenter(dt2), run_time=0.5)
        until(self, "never rewrite", lead=0.3)
        arr = Arrow([2.8, -2.55, 0], [2.8, -1.85, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18)
        xx = a10_cross(2.8, -2.2)
        nr = T("no rewrite", 34).move_to([4.75, -2.2, 0])
        self.play(Create(arr), Create(xx), FadeIn(nr), run_time=0.5)
        done(self)


# ── B53 · Ash: the four tiles return as the running case ────────────────────────────────────────────────────
class B53_AshReturns(Scene):
    def construct(self):
        xs = [-4.35, -1.45, 1.45, 4.35]
        y0 = 0.3
        heads = ["ASKED", "DID", "REPORTED", "STATE"]
        subs = ["delete email", "local reset", "reset\ncompleted", "email\nstill there"]
        tiles = [a10_card(x, y0, 2.6, 2.6, DIM) for x in xs]
        hl = [T(h, 34).move_to([x, 2.6, 0]) for h, x in zip(heads, xs)]
        sl = [T(s, 32).move_to([x, -2.0, 0]) for s, x in zip(subs, xs)]
        # icons
        i_ask = a10_env(xs[0], y0)
        scr = Rectangle(width=1.4, height=0.9, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([xs[1], y0 + 0.2, 0])
        base = Line([xs[1] - 0.8, y0 - 0.45, 0], [xs[1] + 0.8, y0 - 0.45, 0], color=DIM, stroke_width=6)
        ghost = a10_env(xs[1], y0 + 0.2, 0.7, 0.46, GHOST, 4)
        i_did = VGroup(scr, base, ghost)
        i_rep = check(xs[2] - 0.2, y0 + 0.1, 0.55, INK, 12)
        srv1 = Rectangle(width=1.5, height=0.7, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([xs[3], y0 + 0.55, 0])
        srv2 = Rectangle(width=1.5, height=0.7, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([xs[3], y0 - 0.3, 0])
        env_in = a10_env(xs[3], y0 + 0.55, 0.66, 0.44, INK, 4)
        i_state = VGroup(srv1, srv2, env_in)
        icons = [i_ask, i_did, i_rep, i_state]
        for k in range(4):
            self.play(Create(tiles[k]), Create(icons[k]), FadeIn(hl[k]), FadeIn(sl[k]), run_time=0.5)
            self.wait(0.15)
        until(self, "true about the local machine", lead=0.2)
        self.play(tiles[1].animate.set_stroke(INK, 8), tiles[2].animate.set_stroke(INK, 8), run_time=0.4)
        until(self, "false about the system", lead=0.6)
        gap = dim_arrow([1.45, 1.78, 0], [4.35, 1.78, 0], color=INK)
        mark = a10_cross(2.9, 1.78, 0.2, INK, 7)
        t_dot = Dot([5.1, 1.25, 0], radius=0.2, color=TERRA)
        self.play(tiles[3].animate.set_stroke(INK, 8), Create(gap), Create(mark), GrowFromCenter(t_dot), run_time=0.5)
        # the running case: a lens sweeps the four tiles
        until(self, "running case", lead=0.1)
        lens = VGroup(Circle(radius=0.75, color=INK, stroke_width=6).move_to([xs[0], y0, 0]),
                      Line([xs[0] + 0.53, y0 - 0.53, 0], [xs[0] + 0.95, y0 - 0.95, 0], color=INK, stroke_width=8))
        self.play(Create(lens), run_time=0.4)
        ticks = []
        for k in (1, 2, 3):
            self.play(lens.animate.shift(RIGHT * (xs[k] - xs[k - 1])), run_time=0.7)
            ticks.append(Dot([xs[k], -1.2, 0], radius=0.1, color=INK))
            self.play(GrowFromCenter(ticks[-1]), run_time=0.15)
        done(self)


# ── B54 · three failures compressed; the capacities that catch them ──────────────────────────────────────────
class B54_ThreeFailures(Scene):
    def construct(self):
        xs = [-3.9, 0.0, 3.9]
        cy = 0.9
        labs = ["correct, harmful", "fluent, wrong", "success, nothing"]
        cards = [a10_card(x, cy, 3.4, 2.4, DIM) for x in xs]
        ll = [T(t, 34).move_to([x, 2.55, 0]) for t, x in zip(labs, xs)]
        # 1 correct + harmful
        tri = Polygon([xs[0] + 0.8, cy + 0.6, 0], [xs[0] + 0.35, cy - 0.3, 0], [xs[0] + 1.25, cy - 0.3, 0], color=INK, stroke_width=6)
        bang = Line([xs[0] + 0.8, cy + 0.2, 0], [xs[0] + 0.8, cy - 0.05, 0], color=INK, stroke_width=6)
        c1 = VGroup(check(xs[0] - 0.9, cy, 0.4, INK, 10), tri, bang)
        # 2 fluent + wrong
        c2 = VGroup(*[Line([xs[1] - 1.3, cy + dy, 0], [xs[1] + 0.1 + dl, cy + dy, 0], color=DIM, stroke_width=6)
                      for dy, dl in ((0.5, 0.2), (0.0, 0.0), (-0.5, 0.15))], a10_cross(xs[1] + 1.1, cy, 0.25, INK, 9))
        # 3 success + nothing
        empty = Rectangle(width=0.9, height=0.9, stroke_color=GHOST, stroke_width=5, fill_opacity=0).move_to([xs[2] + 0.85, cy, 0])
        c3 = VGroup(check(xs[2] - 0.9, cy, 0.4, INK, 10), empty)
        reveal = [(cards[0], c1, ll[0]), (cards[1], c2, ll[1]), (cards[2], c3, ll[2])]
        until(self, "AI can be technically", lead=0.1)
        self.play(Create(cards[0]), Create(c1), FadeIn(ll[0]), run_time=0.6)
        until(self, "It can be fluent", lead=0.3)
        self.play(Create(cards[1]), Create(c2), FadeIn(ll[1]), run_time=0.6)
        until(self, "It can report", lead=0.3)
        self.play(Create(cards[2]), Create(c3), FadeIn(ll[2]), run_time=0.6)
        # the net of capacities
        until(self, "The capacities", lead=0.2)
        net_y = -1.6
        net = Line([-5.6, net_y, 0], [5.6, net_y, 0], color=DIM, stroke_width=5)
        stakes = VGroup(*[Dot([x, net_y, 0], radius=0.14, color=INK) for x in (-5.4, -1.95, 1.95, 5.4)])
        self.play(Create(net), LaggedStart(*[GrowFromCenter(s) for s in stakes], lag_ratio=0.25), run_time=0.9)
        drops = [Dot([x, cy - 1.45, 0], radius=0.2, color=TERRA) for x in xs]
        self.play(*[GrowFromCenter(d) for d in drops], run_time=0.3)
        self.play(*[d.animate.move_to([d.get_center()[0], net_y + 0.28, 0]) for d in drops], run_time=0.8, rate_func=ease_in)
        until(self, "supervisory", lead=0.2)
        sup = T("supervisory, human", 34).move_to([0.0, -2.6, 0])
        self.play(FadeIn(sup), run_time=0.4)
        done(self)


# ── B55 · the open question: trust anyway? ──────────────────────────────────────────────────────────────────
def a10_scale(th, px=-1.8, py=0.7, L=2.3, drop=1.0):
    """Balance at tilt th (>0: left pan down, i.e. checking heavier). Pans hang level."""
    lx, ly = px - L * np.cos(th), py - L * np.sin(th)
    rx, ry = px + L * np.cos(th), py + L * np.sin(th)
    beam = Line([lx, ly, 0], [rx, ry, 0], color=INK, stroke_width=8)
    parts = [beam]
    for ex, ey in ((lx, ly), (rx, ry)):
        py_ = ey - drop
        parts.append(Line([ex, ey, 0], [ex - 0.5, py_, 0], color=DIM, stroke_width=4))
        parts.append(Line([ex, ey, 0], [ex + 0.5, py_, 0], color=DIM, stroke_width=4))
        parts.append(Polygon([ex - 0.6, py_, 0], [ex + 0.6, py_, 0], [ex + 0.4, py_ - 0.3, 0], [ex - 0.4, py_ - 0.3, 0],
                             color=INK, stroke_width=5))
    return VGroup(*parts)


class B55_TrustAnyway(Scene):
    def construct(self):
        px, py = -1.8, 0.7
        post = Line([px, py, 0], [px, -1.5, 0], color=DIM, stroke_width=8)
        foot = Line([px - 0.8, -1.5, 0], [px + 0.8, -1.5, 0], color=DIM, stroke_width=8)
        pivot = Dot([px, py, 0], radius=0.14, color=INK)
        title = T("trust anyway?", 40).move_to([px, 2.95, 0])
        l_lab = T("cost of checking", 34).move_to([px - 2.3, -2.2, 0])
        r_lab = T("cost of error", 34).move_to([px + 2.3, -2.2, 0])
        sc = a10_scale(0.0)
        self.add(post, foot, pivot, title)
        self.play(Create(sc), run_time=0.6)
        self.play(FadeIn(l_lab), FadeIn(r_lab), run_time=0.4)
        until(self, "checking costs", lead=0.3)
        self.play(Transform(sc, a10_scale(0.2)), run_time=0.7)
        until(self, "than being wrong", lead=0.3)
        self.play(Transform(sc, a10_scale(-0.2)), run_time=0.7)
        until(self, "Bear has no clean answer", lead=0.0)
        self.play(Transform(sc, a10_scale(0.05)), run_time=0.6)
        # what would change my mind: a schematic where confidence tracks truth
        until(self, "And he would change", lead=0.2)
        head = T("change my mind", 34).move_to([4.2, 2.35, 0])
        ax_x = Line([2.6, -0.9, 0], [5.8, -0.9, 0], color=DIM, stroke_width=5)
        ax_y = Line([2.6, -0.9, 0], [2.6, 1.8, 0], color=DIM, stroke_width=5)
        pts = [(2.6, -0.3), (3.4, 0.3), (4.2, 0.1), (5.0, 0.9), (5.8, 1.3)]
        truth = VGroup(*[Line([pts[i][0], pts[i][1], 0], [pts[i + 1][0], pts[i + 1][1], 0], color=INK, stroke_width=7) for i in range(4)])
        conf = VGroup(*[Line([pts[i][0], pts[i][1] + 0.3, 0], [pts[i + 1][0], pts[i + 1][1] + 0.3, 0], color=BAR1, stroke_width=7) for i in range(4)])
        cap = T("tracks truth", 34).move_to([4.2, -1.45, 0])
        sch = T("schematic", 32, DIM).move_to([4.2, -2.1, 0])
        self.play(FadeIn(head), Create(ax_x), Create(ax_y), run_time=0.5)
        self.play(Create(truth), run_time=0.7)
        self.play(Create(conf), run_time=0.7)
        self.play(FadeIn(cap), FadeIn(sch), run_time=0.4)
        done(self)


# attach the midpoint guard (see ST); the classes stay literal `(Scene)` for run.sh's scene discovery
import re as _re
for _n, _c in list(globals().items()):
    if isinstance(_c, type) and issubclass(_c, Scene) and _c is not Scene and _re.match(r"^B[A-Z0-9]+_", _n):
        _c.play = ST.play
