"""scenes.py — claude-liam-lecture-probability-and-the-confidence-illusion (INFO 7375, Lecture 2 of 13)

One Manim scene per body beat, plus ten act titles. Recurring cast per act is listed in ACTS.md. Laws applied from
the start (toolkit gate notes): explicit coordinates; every scene adds a non-text shape after its first frame; text >= 32;
terracotta only as dots; rings round text are grey; nothing crosses a label; safe area +-6.2 x +-3.3.
Every number on screen is computed in evidence/evidence.py or asserted here; seeded runs say so on screen.
Pacing: until(self, phrase) waits for the phrase's share of the measured narration.
"""
from manim import *
import numpy as np
import math
import random as _random
import json as _json
import os as _os

STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
SOFT = "#5F5B51"; DARK_TOP = "#3A3530"; DARK_L = "#26221F"
BAR1 = "#8B8F96"; BAR2 = "#B4AFA6"; BAR3 = "#D9D4C7"; BOX_L = "#DCC9AA"
SERIF = "EB Garamond"
config.background_color = STAGE
_HERE = _os.path.dirname(_os.path.abspath(__file__))

try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}
try:
    _CAL = _json.load(open(_os.path.join(_HERE, "evidence", "calib.json")))
    _SER = _json.load(open(_os.path.join(_HERE, "evidence", "series.json")))
except Exception:
    _CAL = {"bins_before": [[0.5, 0.6, 1, 0.55, 0.52], [0.6, 0.7, 1, 0.65, 0.59], [0.7, 0.8, 1, 0.75, 0.63], [0.8, 0.9, 1, 0.85, 0.70], [0.9, 1.0, 1, 0.97, 0.855]],
            "bins_after": [[0.5, 0.6, 1, 0.55, 0.56], [0.6, 0.7, 1, 0.65, 0.66], [0.7, 0.8, 1, 0.75, 0.74], [0.8, 0.9, 1, 0.85, 0.855], [0.9, 1.0, 1, 0.94, 0.94]],
            "T": 2.19, "accuracy": 0.746}
    _SER = {"gauss_means": [0.0] * 500, "cauchy_means": [0.0] * 500}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - 0.12 - _elapsed(self)) if target else 2.0)


def T(s, size=34, color=INK, bold=False, maxw=None):
    t = Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
    if maxw and t.width > maxw:
        t.scale(maxw / t.width)
    return t


def M(tex, size=48, color=INK):
    return MathTex(tex, font_size=size, color=color)


def stage():
    c = RoundedRectangle(width=12.2, height=6.0, corner_radius=0.18, fill_color=CARD, fill_opacity=1,
                         stroke_color=GHOST, stroke_width=5).move_to([0, -0.15, 0])
    hd = RoundedRectangle(width=12.0, height=0.26, corner_radius=0.08, fill_color=DARK_TOP, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([0, 2.69, 0])
    return c, hd


def open_stage(self, *extra):
    st, hd = stage()
    self.play(FadeIn(st), FadeIn(hd), *[FadeIn(e) for e in extra], run_time=0.4)
    return st, hd


def box(cx, cy, w, h, fill=CARD, stroke=GHOST, sw=4):
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to([cx, cy, 0])


def dbox(cx, cy, w, h, fill=DARK_L):
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=fill, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0).move_to([cx, cy, 0])


def fbar(x0, y, w, h, color=BAR1):
    w = max(w, 0.02)
    return Rectangle(width=w, height=h, fill_color=color, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([x0 + w / 2, y, 0])


def vbar(x, y0, h, w=1.0, color=BAR1):
    h = max(h, 0.03)
    return Rectangle(width=w, height=h, fill_color=color, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([x, y0 + h / 2, 0])


def hline(x0, x1, y, color=GHOST, w=4):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=w)


def vline(x, y0, y1, color=GHOST, w=4):
    return Line([x, y0, 0], [x, y1, 0], color=color, stroke_width=w)


def seg(p0, p1, color=INK, w=5):
    return Line([p0[0], p0[1], 0], [p1[0], p1[1], 0], color=color, stroke_width=w)


def dashed(p0, p1, color=DIM, w=4):
    return DashedLine([p0[0], p0[1], 0], [p1[0], p1[1], 0], color=color, stroke_width=w, dash_length=0.12)


def arrow(p0, p1, color=DIM, w=6):
    return Arrow([p0[0], p0[1], 0], [p1[0], p1[1], 0], buff=0.05, color=color, stroke_width=w, max_tip_length_to_length_ratio=0.2)


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cross(x, y, s=0.2, color=SOFT, w=6):
    return VGroup(Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w),
                  Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w))


def tdot(x, y, r=0.1):
    return Dot([x, y, 0], radius=r, color=TERRA)


def idot(x, y, r=0.1, color=INK):
    return Dot([x, y, 0], radius=r, color=color)


def ring(cx, cy, w, h):
    return RoundedRectangle(width=w, height=h, corner_radius=0.1, stroke_color=DIM, stroke_width=4, fill_opacity=0).move_to([cx, cy, 0])


def circ(cx, cy, r, color=SOFT, sw=5, fill=None):
    return Circle(radius=r, stroke_color=color, stroke_width=sw, fill_color=fill or CARD, fill_opacity=1 if fill else 0).move_to([cx, cy, 0])


def poly(pts, color=INK, w=6):
    m = VMobject(stroke_color=color, stroke_width=w, fill_opacity=0)
    m.set_points_as_corners([[p[0], p[1], 0] for p in pts])
    return m


def lock(cx, cy, open_=False):
    body = RoundedRectangle(width=0.42, height=0.34, corner_radius=0.06, fill_color=SOFT, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([cx, cy, 0])
    shackle = Arc(radius=0.14, start_angle=0, angle=PI, color=SOFT, stroke_width=6, arc_center=[cx + (0.2 if open_ else 0.0), cy + 0.17 + (0.1 if open_ else 0.0), 0])
    return VGroup(body, shackle)


def axes(x0, y0, w, h, xlab=None, ylab=None, color=SOFT):
    g = VGroup(seg((x0, y0), (x0 + w, y0), color, 5), seg((x0, y0), (x0, y0 + h), color, 5))
    return g


def gauge(cx, cy, r, val=0.5, labels=("0", "1")):
    arc = Arc(radius=r, start_angle=math.radians(15), angle=math.radians(150), color=GHOST, stroke_width=12, arc_center=[cx, cy, 0])
    hub = Dot([cx, cy, 0], radius=0.11, color=INK)
    return arc, hub


def needle_at(cx, cy, r, val, color=INK):
    a = math.radians(165 - 150 * val)
    return Line([cx, cy, 0], [cx + r * 0.8 * math.cos(a), cy + r * 0.8 * math.sin(a), 0], color=color, stroke_width=9)


def tip_at(cx, cy, r, val):
    a = math.radians(165 - 150 * val)
    return Dot([cx + r * 0.8 * math.cos(a), cy + r * 0.8 * math.sin(a), 0], radius=0.1, color=TERRA)


def cap(txt, y=-2.75, size=32, x=0, color=SOFT):
    return T(txt, size, color).move_to([x, y, 0])


def title_at(txt, y=2.2, size=40):
    return T(txt, size, INK, bold=True, maxw=11.0).move_to([0, y, 0])


def grid_img(arr, h):
    """A pixel-art grid as an image (nearest neighbour), height h units (Rectangle stand-in if images are unavailable)."""
    try:
        im = ImageMobject(arr)
        try:
            im.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        except Exception:
            pass
        im.height = h
        return im
    except Exception:
        return Rectangle(width=h * arr.shape[1] / arr.shape[0], height=h, fill_color=BAR3, fill_opacity=1, stroke_width=0, stroke_opacity=0)


def _pb_dir():
    env = _os.environ.get("ART_HOME")
    cands = [env and _os.path.join(env, "professor-bear")]
    here = _os.path.dirname(_os.path.abspath(__file__))
    for _ in range(8):
        cands.append(_os.path.join(here, "brutalist.art", "professor-bear"))
        cands.append(_os.path.join(here, "professor-bear"))
        here = _os.path.dirname(here)
    cands.append("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/professor-bear")
    for c in cands:
        if c and _os.path.isdir(c):
            return c
    return cands[-1]


_PB_RATIOS = {"1x1": (1.0, 229), "2x3": (2 / 3, 28), "16x9": (16 / 9, 13)}


def _pb_circle(path):
    """A circular cut (alpha outside the circle), cached beside the set in _crops/. Cropping is fine (Bear, 2026-10-07)."""
    from PIL import Image as _Im, ImageDraw as _Dr
    out_dir = _os.path.join(_os.path.dirname(path), "_crops"); _os.makedirs(out_dir, exist_ok=True)
    out = _os.path.join(out_dir, _os.path.splitext(_os.path.basename(path))[0] + "-circle.png")
    if not _os.path.exists(out):
        im = _Im.open(path).convert("RGBA"); w, h = im.size; s = min(w, h); top = max(0, (h - s) // 3)
        im = im.crop(((w - s) // 2, top, (w - s) // 2 + s, top + s))
        mask = _Im.new("L", (s, s), 0); _Dr.Draw(mask).ellipse((0, 0, s - 1, s - 1), fill=255)
        im.putalpha(mask); im.save(out)
    return out


def professor_bear(ratio="2x3", height=3.0, seed=None, x=0.0, y=0.0, frame=True, shape="rect"):
    """A Professor Bear portrait (random within `ratio`; `seed` = the beat id for a stable pick across re-renders).
    Returns a Group: kraft drop shadow, the photo, an ink frame. Place with `x, y`; size with `height`.
    `shape="circle"` gives a round cut (use a 1x1 portrait). Cropping is fine: circle, rounded square, tight head shot."""
    import random as _random
    ar, n = _PB_RATIOS[ratio]
    k = _random.Random(str(seed) if seed is not None else None).randint(1, n)
    path = _os.path.join(_pb_dir(), f"professor-bear-{ratio}-{k:02d}.png")
    circle = shape == "circle"
    if circle:
        ar = 1.0
    w = height * ar
    if circle:
        shadow = Circle(radius=height / 2, fill_color=BOX_L, fill_opacity=1, stroke_width=0).move_to([x + 0.12, y - 0.12, 0])
        border = Circle(radius=height / 2, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([x, y, 0])
    else:
        shadow = Rectangle(width=w, height=height, fill_color=BOX_L, fill_opacity=1, stroke_width=0).move_to([x + 0.12, y - 0.12, 0])
        border = Rectangle(width=w, height=height, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([x, y, 0])
    try:
        img = ImageMobject(_pb_circle(path) if circle else path)
        img.height = height
        img.move_to([x, y, 0])
    except Exception:
        img = Rectangle(width=w, height=height, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    g = Group(shadow, img, border) if frame else Group(img)
    g.path = path
    return g
# ═════════════════════════ ACT TITLES ═════════════════════════
_ACTS = ["A Number That Looks Like a Fact", "Probability Is a Degree of Belief", "Conditioning and the Chain",
         "The Ninety-Nine Percent Test", "Bayes Runs Backward", "Rare Events Everywhere", "Every Number Is a Claim",
         "Calibration", "When Averages Stop Settling", "Four Questions"]


def _act_title(self, k):
    st, hd = stage()
    name = T(_ACTS[k - 1], 64, INK, bold=True, maxw=11.0).move_to([0, 0.5, 0])
    dots = VGroup(*[idot(-2.7 + i * 0.6, -1.0, 0.11, GHOST) for i in range(10)])
    self.play(FadeIn(st), FadeIn(hd), FadeIn(name), FadeIn(dots), run_time=0.5)
    done = VGroup(*[idot(-2.7 + i * 0.6, -1.0, 0.11, INK) for i in range(k - 1)])
    self.play(FadeIn(done), run_time=0.3)
    self.play(FadeIn(tdot(-2.7 + (k - 1) * 0.6, -1.0, 0.17)), run_time=0.3)
    finish(self)


class A1_Title(Scene):
    def construct(self): _act_title(self, 1)
class A2_Title(Scene):
    def construct(self): _act_title(self, 2)
class A3_Title(Scene):
    def construct(self): _act_title(self, 3)
class A4_Title(Scene):
    def construct(self): _act_title(self, 4)
class A5_Title(Scene):
    def construct(self): _act_title(self, 5)
class A6_Title(Scene):
    def construct(self): _act_title(self, 6)
class A7_Title(Scene):
    def construct(self): _act_title(self, 7)
class A8_Title(Scene):
    def construct(self): _act_title(self, 8)
class A9_Title(Scene):
    def construct(self): _act_title(self, 9)
class A10_Title(Scene):
    def construct(self): _act_title(self, 10)


# ═════════════════════════ ACT I ═════════════════════════
class B01_Column(Scene):
    def construct(self):
        st, hd = open_stage(self)
        rows = [("case 0412", "0.94"), ("case 0187", "0.91"), ("case 0933", "0.88"), ("case 0560", "0.87"), ("case 0721", "0.85")]
        lab = T("classifier output (constructed example)", 32, SOFT).move_to([-2.4, 2.1, 0])
        self.play(FadeIn(lab), run_time=0.3)
        grp = VGroup()
        for i, (a, b) in enumerate(rows):
            y = 1.35 - i * 0.78
            grp.add(VGroup(T(a, 38, INK).move_to([-4.3, y, 0], aligned_edge=LEFT), T(b, 44, INK, bold=True).move_to([-1.2, y, 0], aligned_edge=LEFT),
                           hline(-4.4, -0.3, y - 0.39, GHOST, 3)))
        until(self, "Point nine four")
        self.play(LaggedStart(*[FadeIn(r) for r in grp], lag_ratio=0.35), run_time=2.4)
        tile = box(3.6, 0.45, 3.2, 2.9, CARD, SOFT, 5)
        tl = T("dashboard", 34, SOFT).move_to([3.6, 1.55, 0])
        until(self, "ready for a dashboard")
        self.play(FadeIn(tile), FadeIn(tl), run_time=0.4)
        bars = VGroup(*[fbar(2.4, 0.9 - i * 0.55, w, 0.3, BAR1) for i, w in enumerate([2.1, 1.9, 1.7])])
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.3), run_time=1.2)
        until(self, "It looks finished")
        self.play(Create(check(3.6, -0.55, 0.28, INK, 9)), FadeIn(tdot(5.0, 1.55)), run_time=0.5)
        finish(self)


class B02_Formatted(Scene):
    def construct(self):
        st, hd = open_stage(self)
        score = T("0.94", 120, INK, bold=True).move_to([-3.0, 0.5, 0])
        tag = T("a degree of belief", 38, SOFT).move_to([-3.0, -1.0, 0])
        self.play(FadeIn(score), run_time=0.4)
        self.play(FadeIn(tag), run_time=0.5)
        until(self, "formatted to look like facts")
        ticks = VGroup(*[seg((1.0 + i * 0.55, 0.0), (1.0 + i * 0.55, 0.28 if i % 2 else 0.5), SOFT, 5) for i in range(9)])
        ruler = VGroup(Rectangle(width=4.6, height=0.7, fill_color=BOX_L, fill_opacity=1, stroke_color=SOFT, stroke_width=4).move_to([3.3, 0.35, 0]), ticks)
        rl = T("looks measured", 34, SOFT).move_to([3.3, -0.65, 0])
        self.play(FadeIn(ruler), FadeIn(rl), run_time=0.7)
        until(self, "Nothing in it says")
        q = T("94 of 100?", 52, INK, bold=True).move_to([3.3, 1.7, 0])
        self.play(FadeIn(q), FadeIn(tdot(3.3, 2.25)), run_time=0.6)
        finish(self)


class B03_ThreeUnsaid(Scene):
    def construct(self):
        st, hd = open_stage(self)
        score = T("0.94", 90, INK, bold=True).move_to([0, 1.4, 0])
        self.play(FadeIn(score), run_time=0.4)
        slot1 = box(-3.0, -0.6, 4.6, 1.5, CARD, GHOST, 5)
        slot2 = box(3.0, -0.6, 4.6, 1.5, CARD, GHOST, 5)
        self.play(FadeIn(slot1), FadeIn(slot2), run_time=0.5)
        until(self, "how common the thing you are hunting is")
        t1 = T("how common is it?", 38, INK).move_to([-3.0, -0.6, 0])
        self.play(FadeIn(t1), run_time=0.6)
        until(self, "whether training rewarded")
        t2 = T("what training rewarded", 36, INK).move_to([3.0, -0.6, 0])
        self.play(FadeIn(t2), run_time=0.6)
        until(self, "point eight five")
        self.play(Transform(score, T("0.85?", 90, INK, bold=True).move_to([0, 1.4, 0])), FadeIn(tdot(0, 0.5)), run_time=0.7)
        finish(self)


class B04_Earned(Scene):
    def construct(self):
        st, hd = open_stage(self)
        base = hline(-3.2, 3.2, -1.8, SOFT, 5)
        self.play(Create(base), run_time=0.3)
        until(self, "radiates")
        b1 = vbar(-1.6, -1.8, 3.6, 1.6, BAR3)
        l1 = T("radiated", 36, INK).move_to([-1.6, -2.3, 0])
        self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=0.9)
        until(self, "has earned")
        b2 = vbar(1.6, -1.8, 1.9, 1.6, BAR1)
        l2 = T("earned", 36, INK).move_to([1.6, -2.3, 0])
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=0.9)
        until(self, "plausibility auditing")
        br = VGroup(seg((3.0, 0.1), (3.0, 1.8), INK, 5), seg((2.8, 0.1), (3.0, 0.1), INK, 5), seg((2.8, 1.8), (3.0, 1.8), INK, 5))
        gap = T("the gap", 40, INK, bold=True).move_to([4.3, 0.95, 0])
        self.play(Create(br), FadeIn(gap), FadeIn(tdot(3.0, 2.15)), run_time=0.8)
        finish(self)


class B05_ThreeTools(Scene):
    def construct(self):
        st, hd = open_stage(self)
        xs = [-4.0, 0.0, 4.0]
        for x in xs:
            self.add(box(x, 0.1, 3.4, 3.4, CARD, GHOST, 5))
        self.play(FadeIn(VGroup(*[box(x, 0.1, 3.4, 3.4, CARD, GHOST, 5) for x in xs])), run_time=0.3)
        until(self, "A calculation")
        pts = VGroup(*[idot(-4.9 + (i % 5) * 0.45, 0.65 - (i // 5) * 0.45, 0.07, BAR2) for i in range(20)])
        pts[7].set_color(INK)
        l1 = T("rare events", 36, INK).move_to([-4.0, -1.35, 0])
        self.play(FadeIn(pts), FadeIn(l1), run_time=0.7)
        until(self, "A diagnostic")
        diag = seg((-1.3, -0.9), (1.3, 1.5), SOFT, 5)
        dots = VGroup(*[idot(-0.9 + i * 0.5, -0.5 + i * 0.4 - (0.0 if i < 3 else (i - 2) * 0.25), 0.09, INK) for i in range(5)])
        l2 = T("calibration", 36, INK).move_to([0, -1.35, 0])
        self.play(Create(diag), FadeIn(dots), FadeIn(l2), run_time=0.7)
        until(self, "a warning")
        pl = [[3.1 + i * 0.05, -0.8 + 2.0 * math.exp(-((i * 0.05 - 0.9) ** 2) / 0.25)] for i in range(0, 37)]
        curve = poly(pl, INK, 6)
        tail = poly([[4.6, -0.75], [5.0, -0.45], [5.4, -0.15]], DIM, 6)
        l3 = T("heavy tails", 36, INK).move_to([4.0, -1.35, 0])
        self.play(Create(curve), Create(tail), FadeIn(l3), run_time=0.8)
        finish(self)


# ═════════════════════════ ACT II ═════════════════════════
class B06_BitToDial(Scene):
    def construct(self):
        st, hd = open_stage(self)
        bit = box(-3.2, 0.2, 1.8, 1.8, CARD, SOFT, 6)
        one = T("1", 90, INK, bold=True).move_to([-3.2, 0.2, 0])
        lab = T("a bit", 38, SOFT).move_to([-3.2, -1.2, 0])
        self.play(FadeIn(bit), FadeIn(one), FadeIn(lab), run_time=0.4)
        until(self, "A test passes or fails")
        self.play(Transform(one, T("0", 90, INK, bold=True).move_to([-3.2, 0.2, 0])), run_time=0.4)
        self.play(Transform(one, T("1", 90, INK, bold=True).move_to([-3.2, 0.2, 0])), run_time=0.4)
        until(self, "Probability is a different animal")
        arc, hub = gauge(2.7, -0.3, 1.9)
        n = needle_at(2.7, -0.3, 1.9, 0.7)
        l0 = T("0", 36, INK).move_to([0.6, 0.0, 0]); l1 = T("1", 36, INK).move_to([4.8, 0.0, 0])
        dl = T("a dial", 38, SOFT).move_to([2.7, -1.5, 0])
        self.play(FadeIn(arc), FadeIn(hub), FadeIn(l0), FadeIn(l1), FadeIn(dl), Create(n), run_time=0.9)
        self.play(FadeIn(tip_at(2.7, -0.3, 1.9, 0.7)), run_time=0.3)
        finish(self)


class B07_Belief(Scene):
    def construct(self):
        st, hd = open_stage(self)
        line = seg((-4.5, 0.0), (4.5, 0.0), SOFT, 6)
        t0 = seg((-4.5, -0.2), (-4.5, 0.2), SOFT, 6); t1 = seg((4.5, -0.2), (4.5, 0.2), SOFT, 6)
        l0 = T("0", 40, INK).move_to([-4.5, -0.6, 0]); l1 = T("1", 40, INK).move_to([4.5, -0.6, 0])
        self.play(Create(line), FadeIn(t0), FadeIn(t1), FadeIn(l0), FadeIn(l1), run_time=0.7)
        until(self, "degree of belief")
        mk = tdot(-4.5, 0.0, 0.16)
        self.play(FadeIn(mk), run_time=0.2)
        self.play(mk.animate.move_to([2.1, 0.0, 0]), run_time=1.2)
        lb = T("how confident to be", 40, INK).move_to([0, 1.3, 0])
        self.play(FadeIn(lb), run_time=0.5)
        until(self, "given what you currently know")
        lg = T("given what you know", 38, SOFT).move_to([0, -1.6, 0])
        self.play(FadeIn(lg), run_time=0.5)
        finish(self)


class B08_TwoEngineers(Scene):
    def construct(self):
        st, hd = open_stage(self)
        pa = professor_bear("1x1", 1.7, seed="B08a", x=-4.4, y=1.2, shape="circle")
        pb = professor_bear("1x1", 1.7, seed="B08b", x=4.4, y=1.2, shape="circle")
        ev = box(0, 1.2, 3.0, 1.6, CARD, DIM, 5)
        evl = T("same evidence", 34, INK).move_to([0, 1.2, 0])
        self.play(FadeIn(pa), FadeIn(pb), FadeIn(ev), FadeIn(evl), run_time=0.6)
        until(self, "walked in with different priors")
        ba = fbar(-5.3, -1.1, 1.0, 0.45, BAR1); bb = fbar(3.0, -1.1, 1.6, 0.45, BAR1)
        la = T("prior", 34, SOFT).move_to([-4.4, -1.75, 0]); lb = T("prior", 34, SOFT).move_to([4.4, -1.75, 0])
        self.play(GrowFromEdge(ba, LEFT), GrowFromEdge(bb, LEFT), FadeIn(la), FadeIn(lb), run_time=0.8)
        until(self, "Probability is always conditional")
        a1 = arrow((-1.6, 1.2), (-3.3, 1.2)); a2 = arrow((1.6, 1.2), (3.3, 1.2))
        self.play(Create(a1), Create(a2), run_time=0.5)
        ba2 = fbar(-5.3, -1.1, 2.0, 0.45, INK); bb2 = fbar(3.0, -1.1, 2.6, 0.45, INK)
        self.play(Transform(ba, ba2), Transform(bb, bb2), run_time=0.9)
        both = T("both reasoned correctly", 40, INK, bold=True).move_to([0, -2.7, 0])
        self.play(FadeIn(both), FadeIn(tdot(0, -2.2)), run_time=0.5)
        finish(self)


class B09_SampleSpace(Scene):
    def construct(self):
        st, hd = open_stage(self)
        tray = RoundedRectangle(width=7.4, height=1.7, corner_radius=0.15, stroke_color=SOFT, stroke_width=5, fill_opacity=0).move_to([-1.6, -0.7, 0])
        om = M(r"\Omega", 60).move_to([-5.75, -0.7, 0])
        tiles = VGroup(*[VGroup(box(-4.5 + i * 1.15, -0.7, 0.95, 0.95, CARD, SOFT, 4), T(str(i + 1), 44, INK, bold=True).move_to([-4.5 + i * 1.15, -0.7, 0])) for i in range(6)])
        self.play(Create(tray), FadeIn(om), FadeIn(tiles), run_time=0.9)
        until(self, "A sample space")
        l1 = T("every outcome", 36, SOFT).move_to([-1.6, -2.0, 0])
        self.play(FadeIn(l1), run_time=0.4)
        until(self, "An event")
        ev = VGroup(tiles[1], tiles[3], tiles[5])
        self.play(ev.animate.shift([0, 1.5, 0]), run_time=0.8)
        l2 = T("event: even faces", 36, INK).move_to([-1.0, 2.15, 0])
        self.play(FadeIn(l2), run_time=0.4)
        until(self, "assigns each event a number")
        sc = seg((3.7, 0.2), (3.7, 2.0), SOFT, 5)
        pm = VGroup(seg((3.5, 0.2), (3.9, 0.2), SOFT, 5), seg((3.5, 2.0), (3.9, 2.0), SOFT, 5))
        self.play(Create(sc), FadeIn(pm), run_time=0.5)
        self.play(FadeIn(tdot(3.7, 1.1, 0.15)), FadeIn(T("a number", 34, INK).move_to([5.0, 1.1, 0])), run_time=0.6)
        finish(self)


class B10_Axioms(Scene):
    def construct(self):
        st, hd = open_stage(self)
        ys = [1.5, 0.1, -1.3]
        eqs = [M(r"P(A)\geq 0", 52), M(r"P(\Omega)=1", 52), M(r"P(A\cup B)=P(A)+P(B)", 46)]
        words = ["never negative", "something happens", "disjoint events add"]
        for e, y in zip(eqs, ys):
            e.move_to([-2.9, y, 0])
        wl = [T(w, 34, SOFT).move_to([-2.9, y - 0.62, 0]) for w, y in zip(words, ys)]
        until(self, "Never negative")
        fl = hline(3.2, 5.6, 1.0, SOFT, 4)
        b1 = fbar(3.5, 1.35, 1.6, 0.0 + 0.3, BAR1)
        self.play(FadeIn(eqs[0]), FadeIn(wl[0]), FadeIn(fl), run_time=0.5)
        self.play(GrowFromEdge(fbar(4.2, 1.15, 1.2, 0.3, BAR1), DOWN), run_time=0.5)
        until(self, "whole sample space")
        self.play(FadeIn(eqs[1]), FadeIn(wl[1]), run_time=0.5)
        full = vbar(4.4, -0.35, 1.2, 1.4, BAR1)
        self.play(GrowFromEdge(full, DOWN), run_time=0.5)
        until(self, "events that cannot both occur")
        self.play(FadeIn(eqs[2]), FadeIn(wl[2]), run_time=0.5)
        s1 = vbar(3.9, -1.9, 0.9, 0.9, BAR1); s2 = vbar(5.0, -1.9, 0.45, 0.9, BAR2)
        self.play(GrowFromEdge(s1, DOWN), GrowFromEdge(s2, DOWN), run_time=0.5)
        self.play(s2.animate.move_to([3.9, -1.9 + 0.9 + 0.225, 0]), run_time=0.7)
        finish(self)


class B11_Consequences(Scene):
    def construct(self):
        st, hd = open_stage(self)
        base = hline(-5.0, -0.5, -1.8, SOFT, 5)
        top = dashed((-5.0, 1.4), (-0.5, 1.4), DIM, 4)
        one = T("1", 36, SOFT).move_to([-5.4, 1.4, 0])
        self.play(Create(base), Create(top), FadeIn(one), run_time=0.5)
        until(self, "Nothing happening")
        em = T("nothing:  P = 0", 38, INK).move_to([-2.8, -2.4, 0])
        self.play(FadeIn(em), run_time=0.4)
        until(self, "the chance that an event does not happen")
        ev = vbar(-3.9, -1.8, 1.6, 1.4, BAR1)
        self.play(GrowFromEdge(ev, DOWN), run_time=0.6)
        comp = vbar(-3.9, -0.2, 1.6, 1.4, BAR3)
        self.play(GrowFromEdge(comp, DOWN), run_time=0.6)
        eq1 = M(r"P(\emptyset)=0", 52).move_to([2.7, 1.0, 0])
        eq2 = M(r"P(A^{c})=1-P(A)", 52).move_to([2.7, -0.5, 0])
        self.play(FadeIn(eq1), run_time=0.4)
        self.play(FadeIn(eq2), run_time=0.5)
        until(self, "Everything else here")
        self.play(FadeIn(tdot(2.7, -1.7)), run_time=0.4)
        finish(self)


class B12_Classical(Scene):
    def construct(self):
        st, hd = open_stage(self)
        bag = RoundedRectangle(width=3.4, height=2.6, corner_radius=0.5, stroke_color=SOFT, stroke_width=6, fill_color=BOX_L, fill_opacity=1).move_to([-3.0, -0.4, 0])
        self.play(FadeIn(bag), run_time=0.5)
        until(self, "a bag holds")
        cols = [DIM, BAR2, GHOST, SOFT, TERRA]
        balls = VGroup(*[Circle(radius=0.28, fill_color=c, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([-4.1 + i * 0.62, -0.4, 0]) for i, c in enumerate(cols)])
        self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.8) for b in balls], lag_ratio=0.2), run_time=1.4)
        until(self, "drawing yellow")
        yl = T("yellow", 38, INK).move_to([0.0, 1.0, 0])
        self.play(FadeIn(yl), Create(arrow((-0.4, 0.75), (-1.45, -0.15), SOFT, 5)), run_time=0.6)
        fr = M(r"\frac{1}{5}", 96).move_to([3.4, 0.2, 0])
        self.play(FadeIn(fr), run_time=0.6)
        finish(self)


def _flips(n, seed=11):
    rng = _random.Random(seed)
    return [1 if rng.random() < 0.5 else 0 for _ in range(n)]


class B13_Frequentist(Scene):
    def construct(self):
        st, hd = open_stage(self)
        fl = _flips(400)
        row = VGroup()
        for i in range(20):
            on = fl[i] == 1
            row.add(Square(side_length=0.36, fill_color=INK if on else GHOST, fill_opacity=1, stroke_color=SOFT, stroke_width=2).move_to([-3.4 + i * 0.4, 2.0, 0]))
        heads = sum(fl[:20])
        self.play(LaggedStart(*[FadeIn(s) for s in row], lag_ratio=0.1), run_time=1.5)
        fr = T(f"{heads} heads in 20 tosses", 38, INK).move_to([-1.6, 1.3, 0])
        self.play(FadeIn(fr), run_time=0.4)
        until(self, "Keep tossing")
        ax = axes(-5.0, -2.4, 10.0, 3.0)
        half = dashed((-5.0, -0.9), (5.0, -0.9), DIM, 4)
        pts = []
        s = 0
        for i, f in enumerate(fl):
            s += f
            pts.append([-5.0 + 10.0 * (i + 1) / 400, -2.4 + 3.0 * (s / (i + 1))])
        curve = poly(pts[4:], INK, 5)
        self.play(Create(ax), Create(half), run_time=0.5)
        self.play(Create(curve), run_time=3.0)
        until(self, "settles toward a limit")
        self.play(FadeIn(T("limit", 34, SOFT).move_to([5.55, -0.9, 0])), FadeIn(tdot(5.0 - 0.0, -0.9, 0.12)), run_time=0.5)
        finish(self)


class B14_Bayesian(Scene):
    def construct(self):
        st, hd = open_stage(self)
        base = hline(-4.6, 4.6, -1.5, SOFT, 5)
        pr = vbar(-3.4, -1.5, 0.8, 1.3, BAR2)
        lp = T("prior", 38, INK).move_to([-3.4, -2.0, 0])
        self.play(Create(base), GrowFromEdge(pr, DOWN), FadeIn(lp), run_time=0.7)
        until(self, "see evidence")
        ev = arrow((-2.2, 0.0), (1.2, 0.0), INK, 7)
        lv = T("evidence", 38, INK).move_to([-0.5, 0.55, 0])
        self.play(Create(ev), FadeIn(lv), run_time=0.7)
        po = vbar(2.6, -1.5, 2.3, 1.3, BAR1)
        lpo = T("posterior", 38, INK).move_to([2.6, -2.0, 0])
        self.play(GrowFromEdge(po, DOWN), FadeIn(lpo), run_time=0.8)
        until(self, "Use all three")
        tags = VGroup(T("classical", 34, SOFT).move_to([-3.6, 2.15, 0]), T("frequentist", 34, SOFT).move_to([0, 2.15, 0]), T("Bayesian", 34, INK, bold=True).move_to([3.6, 2.15, 0]))
        self.play(FadeIn(tags), FadeIn(tdot(3.6, 1.75)), run_time=0.7)
        finish(self)


# ═════════════════════════ ACT III ═════════════════════════
class B15_Shrink(Scene):
    def construct(self):
        st, hd = open_stage(self)
        W, H, x0, y0 = 6.0, 3.2, -5.6, -1.9
        world = Rectangle(width=W, height=H, stroke_color=SOFT, stroke_width=5, fill_color=CARD, fill_opacity=1).move_to([x0 + W / 2, y0 + H / 2, 0])
        Bn = Rectangle(width=0.6 * W, height=H, stroke_color=INK, stroke_width=5, fill_color=BAR2, fill_opacity=1).move_to([x0 + 0.3 * W, y0 + H / 2, 0])
        An = Rectangle(width=0.65 * W, height=0.5 * H, stroke_color=SOFT, stroke_width=4, fill_color=BAR1, fill_opacity=0.7).move_to([x0 + (0.35 + 0.325) * W, y0 + 0.25 * H, 0])
        AB = Rectangle(width=0.25 * W, height=0.5 * H, stroke_width=0, stroke_opacity=0, fill_color=SOFT, fill_opacity=1).move_to([x0 + (0.35 + 0.125) * W, y0 + 0.25 * H, 0])
        self.play(FadeIn(world), run_time=0.4)
        self.play(FadeIn(An), run_time=0.4)
        lbA = T("A", 44, INK, bold=True).move_to([x0 + 0.82 * W, y0 + 0.25 * H, 0])
        self.add(lbA)
        until(self, "Learning that B happened")
        self.play(FadeIn(Bn), FadeIn(AB), FadeIn(T("B", 44, INK, bold=True).move_to([x0 + 0.15 * W, y0 + 0.5 * H, 0])), run_time=0.5)
        until(self, "shrinks the world to B")
        tB = Rectangle(width=W, height=H, stroke_color=INK, stroke_width=5, fill_color=BAR2, fill_opacity=1).move_to([x0 + W / 2, y0 + H / 2, 0])
        tAB = Rectangle(width=W * 0.25 / 0.6, height=0.5 * H, stroke_width=0, stroke_opacity=0, fill_color=SOFT, fill_opacity=1).move_to([x0 + W * 0.25 / 0.6 / 2, y0 + 0.25 * H, 0])
        self.play(FadeOut(world), FadeOut(An), FadeOut(lbA), Transform(Bn, tB), Transform(AB, tAB), run_time=1.3)
        until(self, "the overlap, divided by B")
        eq = M(r"P(A\mid B)=\frac{P(A\cap B)}{P(B)}", 42).move_to([3.4, 0.4, 0])
        self.play(FadeIn(eq), run_time=0.7)
        self.play(FadeIn(tdot(3.4, -1.0, 0.12)), run_time=0.3)
        finish(self)


def _cases():
    return {"flag": set(range(76)), "acute": set(range(30)) | set(range(76, 91))}


def _case_grid(x0=-5.2, y0=1.9, s=0.42):
    cs = _cases()
    g = VGroup()
    for i in range(100):
        r, c = divmod(i, 10)
        flag = i in cs["flag"]; ac = i in cs["acute"]
        g.add(Square(side_length=s * 0.84, fill_color=(DIM if ac else CARD), fill_opacity=1,
                     stroke_color=(INK if flag else GHOST), stroke_width=(4 if flag else 2)).move_to([x0 + c * s, y0 - r * s, 0]))
    return g


class B16_TriageLog(Scene):
    def construct(self):
        st, hd = open_stage(self)
        cs = _cases()
        g = _case_grid()
        base = VGroup(*[Square(side_length=0.35, fill_color=CARD, fill_opacity=1, stroke_color=GHOST, stroke_width=2).move_to(m.get_center()) for m in g])
        self.play(FadeIn(base), run_time=0.8)
        lab = T("100 cases in a triage log", 36, SOFT).move_to([-3.1, -2.6, 0])
        self.play(FadeIn(lab), run_time=0.3)
        until(self, "seventy-six percent")
        flag = VGroup(*[Square(side_length=0.35, fill_opacity=0, stroke_color=INK, stroke_width=4).move_to(g[i].get_center()) for i in sorted(cs["flag"])])
        self.play(FadeIn(flag), run_time=0.9)
        c1 = T("76 flagged", 40, INK, bold=True).move_to([3.4, 1.4, 0])
        self.play(FadeIn(c1), run_time=0.3)
        until(self, "forty-five percent")
        ac = VGroup(*[Square(side_length=0.35, fill_color=DIM, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to(g[i].get_center()) for i in sorted(cs["acute"])])
        self.play(FadeIn(ac), run_time=0.9)
        c2 = T("45 high-acuity", 40, INK, bold=True).move_to([3.4, 0.5, 0])
        self.play(FadeIn(c2), run_time=0.3)
        until(self, "thirty percent are both")
        both = VGroup(*[Square(side_length=0.35, fill_opacity=0, stroke_color=TERRA, stroke_width=0, stroke_opacity=0).move_to(g[i].get_center()) for i in range(30)])
        c3 = T("30 both", 40, INK, bold=True).move_to([3.4, -0.4, 0])
        self.play(FadeIn(c3), FadeIn(VGroup(*[tdot(g[i].get_center()[0], g[i].get_center()[1], 0.06) for i in range(0, 30, 3)])), run_time=0.8)
        finish(self)


class B17_Flagged(Scene):
    def construct(self):
        st, hd = open_stage(self)
        cs = _cases()
        g = _case_grid()
        self.play(FadeIn(g), run_time=0.6)
        until(self, "A flagged case arrives")
        self.play(*[g[i].animate.set_opacity(0.15) for i in range(76, 100)], run_time=0.8)
        eq = M(r"\frac{30}{76}\approx 39.5\%", 56).move_to([3.4, 1.0, 0])
        self.play(FadeIn(eq), run_time=0.6)
        until(self, "Lower than")
        base = hline(1.4, 5.4, -1.2, SOFT, 5)
        b1 = fbar(1.4, -0.65, 4.0 * 0.395, 0.45, BAR1); b2 = fbar(1.4, -1.85, 4.0 * 0.45, 0.45, BAR3)
        l1 = T("flagged: 39.5%", 34, INK).move_to([1.4, -0.15, 0], aligned_edge=LEFT); l2 = T("no information: 45%", 34, INK).move_to([1.4, -1.35, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(b1, LEFT), run_time=0.6)
        self.play(GrowFromEdge(b2, LEFT), FadeIn(l1), FadeIn(l2), run_time=0.7)
        finish(self)


class B18_WhyLower(Scene):
    def construct(self):
        st, hd = open_stage(self)
        base = vline(-4.3, -2.3, 1.7, SOFT, 5)
        until(self, "If flag and acuity were unrelated")
        eq = M(r"0.76\times0.45=0.342", 50).move_to([0.0, 2.15, 0])
        self.play(Create(base), FadeIn(eq), run_time=0.5)
        b1 = fbar(-4.0, 0.6, 34.2 * 0.11, 0.7, BAR3)
        l1 = T("if unrelated: 34.2%", 36, INK).move_to([-4.0, 1.35, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(b1, LEFT), FadeIn(l1), run_time=0.8)
        until(self, "They show up thirty percent")
        b2 = fbar(-4.0, -0.8, 30.0 * 0.11, 0.7, BAR1)
        l2 = T("in this log: 30%", 36, INK).move_to([-4.0, -0.05, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(b2, LEFT), FadeIn(l2), run_time=0.8)
        br = VGroup(seg((-4.0 + 30 * 0.11, -1.55), (-4.0 + 34.2 * 0.11, -1.55), INK, 5), seg((-4.0 + 30 * 0.11, -1.7), (-4.0 + 30 * 0.11, -1.4), INK, 5), seg((-4.0 + 34.2 * 0.11, -1.7), (-4.0 + 34.2 * 0.11, -1.4), INK, 5))
        gp = T("less than chance", 38, INK, bold=True).move_to([1.6, -2.25, 0])
        until(self, "the flag goes with high acuity less than chance")
        self.play(Create(br), FadeIn(gp), FadeIn(tdot(-0.6, -1.55)), run_time=0.7)
        finish(self)


class B19_Multiply(Scene):
    def construct(self):
        st, hd = open_stage(self)
        e1 = M(r"P(A\mid B)=\frac{P(A\cap B)}{P(B)}", 50).move_to([0, 1.5, 0])
        self.play(FadeIn(e1), run_time=0.6)
        until(self, "Rearrange the definition")
        e2 = M(r"P(A\cap B)=P(B)\,P(A\mid B)", 54).move_to([0, 0.1, 0])
        self.play(FadeIn(e2), Create(arrow((0, 0.95), (0, 0.65), DIM, 6)), run_time=0.8)
        until(self, "Chain it")
        e3 = M(r"P(A_1\cap A_2\cap A_3)=P(A_1)\,P(A_2\mid A_1)\,P(A_3\mid A_1\cap A_2)", 38).move_to([0, -1.5, 0])
        self.play(FadeIn(e3), run_time=0.9)
        self.play(FadeIn(tdot(0, -2.4, 0.12)), run_time=0.3)
        finish(self)


class B20_Chain(Scene):
    def construct(self):
        st, hd = open_stage(self)
        xs = [-4.6, -2.3, 0.0, 2.3]
        yS = 0.6
        nodes = [circ(x, yS, 0.32, INK, 5, CARD) for x in xs]
        names = ["start", "call 1", "call 2", "call 3"]
        self.play(FadeIn(VGroup(*nodes)), run_time=0.4)
        until(self, "The first succeeds")
        probs = ["0.9", "0.85", "0.8"]
        labs = []
        for i in range(3):
            e = arrow((xs[i] + 0.38, yS), (xs[i + 1] - 0.38, yS), INK, 6)
            lb = T(probs[i], 40, INK, bold=True).move_to([(xs[i] + xs[i + 1]) / 2, yS + 0.5, 0])
            f = seg((xs[i + 1] - 0.9, yS - 0.4), (xs[i + 1] - 0.9, yS - 1.4), DIM, 4)
            fx = cross(xs[i + 1] - 0.9, yS - 1.7, 0.18, DIM, 5)
            fl = T(["0.1", "0.15", "0.2"][i], 34, SOFT).move_to([xs[i + 1] - 0.4, yS - 1.0, 0])
            self.play(Create(e), FadeIn(lb), Create(f), FadeIn(fx), FadeIn(fl), run_time=0.7)
            if i == 0:
                until(self, "Given that")
            if i == 1:
                until(self, "given both")
        until(self, "Multiply along the path")
        res = M(r"0.9\times0.85\times0.8=0.612", 54).move_to([3.0, -1.9, 0])
        self.play(FadeIn(res), run_time=0.7)
        cap_ = T("constructed numbers", 32, SOFT).move_to([-3.6, -2.7, 0])
        self.play(FadeIn(cap_), FadeIn(tdot(xs[3] + 0.0, yS, 0.2)), run_time=0.5)
        finish(self)


class B21_OneBit(Scene):
    def construct(self):
        st, hd = open_stage(self)
        bx = box(-4.2, 0.4, 2.8, 1.6, CARD, DIM, 5)
        tx = T("task complete", 34, INK).move_to([-4.2, 0.7, 0])
        self.play(FadeIn(bx), FadeIn(tx), Create(check(-4.2, 0.0, 0.28, INK, 9)), run_time=0.7)
        until(self, "One bit")
        lb = T("one bit", 36, SOFT).move_to([-4.2, -1.0, 0])
        self.play(FadeIn(lb), run_time=0.4)
        until(self, "a product of three shrinking conditionals")
        vals = [0.9, 0.765, 0.612]; names = ["call 1", "calls 1 to 2", "all three"]
        bars = VGroup(); ls = VGroup()
        for i, (v, n) in enumerate(zip(vals, names)):
            y = 1.5 - i * 1.3
            bars.add(fbar(-1.0, y, 6.4 * v, 0.5, BAR1 if i < 2 else INK))
            ls.add(T(n, 32, INK).move_to([-1.0, y + 0.48, 0], aligned_edge=LEFT))
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.4), FadeIn(ls), run_time=1.8)
        until(self, "about sixty-one percent")
        self.play(FadeIn(T("61%", 52, INK, bold=True).move_to([5.2, -1.1, 0])), FadeIn(tdot(5.2, -0.5, 0.12)), run_time=0.5)
        finish(self)


class B22_Independence(Scene):
    def construct(self):
        st, hd = open_stage(self)
        rows = [("independent", [0.9, 0.81, 0.729], BAR3, 1.5), ("honest", [0.9, 0.765, 0.612], BAR1, -0.7)]
        until(self, "treats the steps as independent")
        grp = {}
        for nm, vals, col, y0 in rows:
            t = T(nm, 36, INK, bold=True).move_to([-5.3, y0 + 0.5, 0], aligned_edge=LEFT)
            bs = VGroup(*[fbar(-5.3, y0 - i * 0.5, 7.0 * v, 0.36, col) for i, v in enumerate(vals)])
            grp[nm] = (t, bs)
        t, bs = grp["independent"]
        self.play(FadeIn(t), LaggedStart(*[GrowFromEdge(b, LEFT) for b in bs], lag_ratio=0.3), run_time=1.4)
        self.play(FadeIn(T("72.9%", 40, INK, bold=True).move_to([1.2, 0.5, 0])), run_time=0.4)
        until(self, "Real failures cluster")
        t, bs = grp["honest"]
        self.play(FadeIn(t), LaggedStart(*[GrowFromEdge(b, LEFT) for b in bs], lag_ratio=0.3), run_time=1.4)
        self.play(FadeIn(T("61.2%", 40, INK, bold=True).move_to([0.5, -1.7, 0])), run_time=0.4)
        br = VGroup(seg((-5.3 + 7.0 * 0.612, -2.4), (-5.3 + 7.0 * 0.729, -2.4), INK, 5), seg((-5.3 + 7.0 * 0.612, -2.55), (-5.3 + 7.0 * 0.612, -2.25), INK, 5), seg((-5.3 + 7.0 * 0.729, -2.55), (-5.3 + 7.0 * 0.729, -2.25), INK, 5))
        until(self, "nearly twelve points")
        self.play(Create(br), FadeIn(T("11.7 points", 38, INK, bold=True).move_to([1.6, -2.4, 0])), FadeIn(tdot(3.5, -2.4, 0.1)), run_time=0.6)
        finish(self)


class B23_Partition(Scene):
    def construct(self):
        st, hd = open_stage(self)
        strip = VGroup(); xs = -4.0
        for w, nm, col in ((0.4, "A1", BAR3), (0.3, "A2", BAR2), (0.3, "A3", BAR3)):
            r = Rectangle(width=8.0 * w, height=1.1, fill_color=col, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([xs + 4.0 * w, 0.8, 0])
            strip.add(VGroup(r, T(nm, 34, INK, bold=True).move_to(r.get_center())))
            xs += 8.0 * w
        self.play(FadeIn(strip), run_time=0.7)
        until(self, "do not overlap and cover everything")
        cap_ = T("scenarios that do not overlap", 34, SOFT).move_to([0, 1.85, 0])
        self.play(FadeIn(cap_), run_time=0.4)
        eq = M(r"P(B)=\sum_{i} P(A_i)\,P(B\mid A_i)", 54).move_to([0, -0.7, 0])
        until(self, "find the probability inside each")
        self.play(FadeIn(eq), run_time=0.8)
        until(self, "weight by how often each occurs")
        self.play(*[s[0].animate.set_fill(INK, 0.35) for s in strip], run_time=0.6)
        self.play(*[s[0].animate.set_fill(BAR2, 1) for s in strip], run_time=0.3)
        until(self, "and add")
        self.play(FadeIn(tdot(0, -1.7, 0.14)), FadeIn(T("a rate you cannot measure directly", 36, INK).move_to([0, -2.4, 0])), run_time=0.6)
        finish(self)


class B24_Fleet(Scene):
    def construct(self):
        st, hd = open_stage(self)
        share = [40, 30, 30]; err = [2, 3, 5]; nm = ["A", "B", "C"]
        hdr = T("version     share     errs", 32, SOFT).move_to([-4.0, 2.1, 0])
        self.play(FadeIn(hdr), run_time=0.3)
        rows = VGroup()
        for i in range(3):
            y = 1.3 - i * 0.8
            rows.add(VGroup(T(nm[i], 42, INK, bold=True).move_to([-5.2, y, 0]), T(f"{share[i]}%", 40, INK).move_to([-3.7, y, 0]), T(f"{err[i]}%", 40, INK).move_to([-2.4, y, 0])))
        until(self, "A handles forty percent")
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.5), run_time=2.2)
        until(self, "Overall error")
        contrib = [0.8, 0.9, 1.5]
        x = 0.0; bars = VGroup(); lbs = VGroup()
        for c, n_ in zip(contrib, nm):
            b = fbar(x, -0.2, c, 0.8, BAR1 if n_ != "C" else INK)
            bars.add(b); lbs.add(T(n_, 34, INK).move_to([x + c / 2, -0.9, 0])); x += c
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.4), FadeIn(lbs), run_time=1.6)
        tot = T("3.2%", 56, INK, bold=True).move_to([x + 1.1, -0.2, 0])
        until(self, "a number no single version reports")
        self.play(FadeIn(tot), FadeIn(tdot(x + 1.1, 0.6, 0.12)), run_time=0.6)
        finish(self)


# ═════════════════════════ ACT IV ═════════════════════════
class B25_PickANumber(Scene):
    def construct(self):
        st, hd = open_stage(self)
        c1 = box(-4.3, 1.2, 3.2, 1.3, CARD, SOFT, 5); t1 = T("1 in 10,000", 40, INK, bold=True).move_to([-4.3, 1.2, 0])
        c2 = box(-4.3, -0.5, 3.2, 1.3, CARD, SOFT, 5); t2 = T("99% accurate", 38, INK, bold=True).move_to([-4.3, -0.5, 0])
        until(self, "about one person in ten thousand")
        self.play(FadeIn(c1), FadeIn(t1), run_time=0.5)
        until(self, "ninety-nine percent accurate")
        self.play(FadeIn(c2), FadeIn(t2), run_time=0.5)
        until(self, "A patient tests positive")
        pos = circ(-0.2, 0.4, 0.55, INK, 6, CARD); pl = T("+", 64, INK, bold=True).move_to([-0.2, 0.4, 0])
        self.play(FadeIn(pos), FadeIn(pl), run_time=0.5)
        until(self, "pick a number")
        slot = box(3.7, 0.4, 3.4, 1.7, CARD, INK, 6)
        q = T("P(sick) = ?", 46, INK, bold=True).move_to([3.7, 0.4, 0])
        self.play(Create(arrow((0.5, 0.4), (1.9, 0.4), SOFT, 6)), FadeIn(slot), FadeIn(q), run_time=0.7)
        lk = lock(3.7, -1.3, True)
        self.play(FadeIn(lk), run_time=0.4)
        self.play(Transform(lk, lock(3.7, -1.3, False)), FadeIn(tdot(5.0, 1.5)), run_time=0.5)
        finish(self)


class B26_TheStudy(Scene):
    def construct(self):
        st, hd = open_stage(self)
        cells = VGroup(*[Square(side_length=0.5, fill_color=BAR2, fill_opacity=1, stroke_color=SOFT, stroke_width=2).move_to([-4.2 + (i % 10) * 0.62, 1.8 - (i // 10) * 0.62, 0]) for i in range(60)])
        self.play(FadeIn(cells), run_time=0.8)
        lb = T("60 Harvard physicians and students, 1978", 34, SOFT).move_to([-1.9, -2.15, 0])
        self.play(FadeIn(lb), run_time=0.4)
        until(self, "Eleven answered correctly")
        corr = [cells[i] for i in range(11)]
        self.play(*[c.animate.set_fill(INK, 1) for c in corr], run_time=0.5)
        self.play(*[c.animate.move_to([3.2 + (j % 4) * 0.62, 1.1 - (j // 4) * 0.62, 0]) for j, c in enumerate(corr)], run_time=0.9)
        l1 = T("11 correct", 38, INK, bold=True).move_to([4.5, 2.0, 0]); l1b = T("(about 2%)", 32, SOFT).move_to([4.5, -0.85, 0])
        self.play(FadeIn(l1), FadeIn(l1b), run_time=0.4)
        until(self, "Twenty-seven")
        ns = [cells[i] for i in range(11, 38)]
        self.play(*[c.animate.set_fill(DIM, 1) for c in ns], run_time=0.5)
        l2 = T("27 said 95%", 38, INK, bold=True).move_to([4.5, -1.6, 0])
        self.play(FadeIn(l2), FadeIn(tdot(3.1, -1.6, 0.1)), run_time=0.6)
        finish(self)


def _people_img(sick=None, fps=None, n=100, cell=6):
    """n x n people as a nearest-neighbour image: healthy dim, positives ink."""
    a = np.zeros((n * cell, n * cell, 3), dtype=np.uint8); a[:, :] = (250, 249, 245)
    rng = _random.Random(3)
    allc = [(r, c) for r in range(n) for c in range(n)]
    sickc = (37, 62)
    fpl = set()
    if fps:
        pool = [x for x in allc if x != sickc]
        rng.shuffle(pool); fpl = set(pool[:fps])
    for (r, c) in allc:
        col = (180, 175, 166)
        if (r, c) == sickc and sick:
            col = (61, 57, 41)
        if (r, c) in fpl:
            col = (61, 57, 41)
        a[r * cell + 1:r * cell + cell - 1, c * cell + 1:c * cell + cell - 1] = col
    return a, fpl, sickc


class B27_TenThousand(Scene):
    def construct(self):
        st, hd = open_stage(self)
        a, _, sc = _people_img(sick=False)
        im = grid_img(a, 4.6)
        im.move_to([-2.9, 0.0, 0])
        self.play(FadeIn(im), run_time=0.8)
        lb = T("10,000 people", 40, INK, bold=True).move_to([-2.9, -2.65, 0])
        self.play(FadeIn(lb), run_time=0.4)
        until(self, "On average one is sick")
        x = -2.9 - 2.3 + (sc[1] + 0.5) * 4.6 / 100; y = 2.3 - (sc[0] + 0.5) * 4.6 / 100 - 0.0
        y = 0.0 + 2.3 - (sc[0] + 0.5) * 4.6 / 100
        rg = circ(x, y, 0.25, INK, 5)
        self.play(Create(rg), FadeIn(tdot(x, y, 0.07)), run_time=0.6)
        t1 = T("1 sick", 40, INK, bold=True).move_to([3.2, 1.0, 0]); t1b = T("caught by the test", 34, SOFT).move_to([3.2, 0.45, 0])
        self.play(FadeIn(t1), FadeIn(t1b), run_time=0.5)
        until(self, "healthy")
        t2 = T("9,999 healthy", 40, INK, bold=True).move_to([3.2, -0.6, 0])
        self.play(FadeIn(t2), run_time=0.5)
        finish(self)


class B28_FalseAlarms(Scene):
    def construct(self):
        st, hd = open_stage(self)
        a0, _, sc = _people_img(sick=True)
        im = grid_img(a0, 4.6).move_to([-2.9, 0.0, 0])
        self.add(im)
        self.play(FadeIn(Square(side_length=0.01, stroke_width=0, stroke_opacity=0, fill_opacity=0)), run_time=0.2)
        until(self, "one percent of healthy people")
        t = T("1% of healthy people", 38, INK, bold=True).move_to([3.4, 1.2, 0])
        self.play(FadeIn(t), run_time=0.5)
        a1, fps, _ = _people_img(sick=True, fps=100)
        im2 = grid_img(a1, 4.6).move_to([-2.9, 0.0, 0])
        until(self, "about a hundred false positives")
        s_ = 4.6 / 100
        ov = VGroup(*[Dot([-2.9 - 2.3 + (c + 0.5) * s_, 2.3 - (r + 0.5) * s_, 0], radius=0.035, color=INK) for (r, c) in sorted(fps)])
        self.play(FadeIn(im2), FadeIn(ov), run_time=0.6)
        self.remove(im)
        t2 = T("about 100 false positives", 36, INK, bold=True).move_to([3.4, 0.1, 0])
        t3 = T("0.01 x 9,999 = 99.99", 34, SOFT).move_to([3.4, -0.6, 0])
        self.play(FadeIn(t2), FadeIn(t3), FadeIn(tdot(0.2, 0.1)), run_time=0.6)
        finish(self)


class B29_OneIn101(Scene):
    def construct(self):
        st, hd = open_stage(self)
        a1, fps, sc = _people_img(sick=True, fps=100)
        im = grid_img(a1, 4.6).move_to([-3.4, 0.0, 0]); self.add(im)
        s = 4.6 / 100
        def pos(rc):
            return [-3.4 - 2.3 + (rc[1] + 0.5) * s, 2.3 - (rc[0] + 0.5) * s, 0]
        until(self, "So a hundred and one people")
        sq = VGroup(*[Square(side_length=0.06, fill_color=INK, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to(pos(rc)) for rc in sorted(fps)])
        sk = Square(side_length=0.06, fill_color=INK, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to(pos(sc))
        pool = VGroup(sk, *sq)
        self.add(pool)
        tgt = []
        for i in range(101):
            r, c = divmod(i, 11)
            tgt.append([2.2 + c * 0.36, 1.6 - r * 0.36, 0])
        self.play(*[pool[i].animate.move_to(tgt[i]).scale(4.5) for i in range(101)], FadeOut(im), run_time=1.6)
        until(self, "one of them is sick")
        rg = circ(tgt[0][0], tgt[0][1], 0.3, TERRA, 6)
        self.play(Create(rg), run_time=0.5)
        until(self, "About one percent")
        self.play(FadeIn(T("1 in 101", 56, INK, bold=True).move_to([4.3, -2.1, 0])), FadeIn(T("not 99", 36, SOFT).move_to([4.3, -2.7, 0])), run_time=0.6)
        finish(self)


class B30_WrongDirection(Scene):
    def construct(self):
        st, hd = open_stage(self)
        a = box(-4.0, 0.2, 2.6, 1.3, CARD, SOFT, 5); ta = T("sick", 44, INK, bold=True).move_to([-4.0, 0.2, 0])
        b = box(4.0, 0.2, 2.6, 1.3, CARD, SOFT, 5); tb = T("positive", 42, INK, bold=True).move_to([4.0, 0.2, 0])
        self.play(FadeIn(a), FadeIn(ta), FadeIn(b), FadeIn(tb), run_time=0.5)
        until(self, "Ninety-nine percent is the chance")
        a1 = arrow((-2.6, 0.7), (2.6, 0.7), INK, 7)
        l1 = M(r"P(+\mid \mathrm{sick})=0.99", 40).move_to([0, 1.45, 0])
        self.play(Create(a1), FadeIn(l1), run_time=0.8)
        until(self, "You needed the chance")
        a2 = arrow((2.6, -0.3), (-2.6, -0.3), DIM, 7)
        l2 = M(r"P(\mathrm{sick}\mid +)=\;?", 40).move_to([0, -1.05, 0])
        self.play(Create(a2), FadeIn(l2), run_time=0.8)
        until(self, "takes the base rate")
        br = T("base rate", 40, INK, bold=True).move_to([0, -2.2, 0])
        self.play(FadeIn(br), FadeIn(tdot(0, -1.7, 0.14)), run_time=0.6)
        finish(self)


# ═════════════════════════ ACT V ═════════════════════════
class B31_Bayes(Scene):
    def construct(self):
        st, hd = open_stage(self)
        lhs = M(r"P(D\mid +)=", 54).move_to([-4.6, 0.3, 0])
        fr = M(r"\frac{P(D)\,P(+\mid D)}{P(D)\,P(+\mid D)+P(H)\,P(+\mid H)}", 50).move_to([0.9, 0.3, 0])
        self.play(FadeIn(lhs), run_time=0.4)
        until(self, "The posterior is the prior times the likelihood")
        self.play(FadeIn(fr), run_time=1.0)
        l1 = T("top: prior x likelihood", 36, INK, bold=True).move_to([0.9, 1.9, 0])
        self.play(FadeIn(l1), run_time=0.6)
        until(self, "everything that could produce a positive")
        l2 = T("bottom: everything that could produce a positive", 34, SOFT).move_to([0.9, -1.7, 0])
        self.play(FadeIn(l2), run_time=0.7)
        until(self, "run the other way")
        self.play(FadeIn(tdot(0, -2.5)), run_time=0.4)
        finish(self)


class B33_Hundredfold(Scene):
    def construct(self):
        st, hd = open_stage(self)
        c1 = T("1 in 10,000", 52, INK, bold=True).move_to([-3.9, 1.5, 0])
        c2 = T("1 in 102", 52, INK, bold=True).move_to([3.9, 1.5, 0])
        self.play(FadeIn(c1), run_time=0.4)
        until(self, "raised the probability")
        ar = arrow((-1.8, 1.5), (1.8, 1.5), INK, 8)
        mx = T("about 98 times", 40, INK, bold=True).move_to([0, 2.15, 0])
        self.play(Create(ar), FadeIn(mx), FadeIn(c2), run_time=0.9)
        until(self, "the prior was so low")
        sc = hline(-5.0, 5.0, -1.0, SOFT, 6)
        t0 = T("0", 34, SOFT).move_to([-5.0, -1.55, 0]); t1 = T("1", 34, SOFT).move_to([5.0, -1.55, 0])
        self.play(Create(sc), FadeIn(t0), FadeIn(t1), run_time=0.5)
        m1 = seg((-5.0 + 0.001, -1.0 + 0.0), (-5.0 + 0.001, -0.6), INK, 6)
        m2 = seg((-5.0 + 10 * 0.0098, -1.0), (-5.0 + 10 * 0.0098, -0.45), INK, 8)
        self.play(Create(m1), Create(m2), run_time=0.5)
        until(self, "still small")
        self.play(FadeIn(T("still small on the full scale", 38, INK).move_to([0, -0.25, 0])), FadeIn(tdot(-4.7, -0.3, 0.1)), run_time=0.6)
        finish(self)


class B34_TwoNumbers(Scene):
    def construct(self):
        st, hd = open_stage(self)
        one = box(0, 1.2, 4.0, 1.3, CARD, INK, 6); t = T("99% accurate", 44, INK, bold=True).move_to([0, 1.2, 0])
        self.play(FadeIn(one), FadeIn(t), run_time=0.5)
        until(self, "double duty")
        l = box(-3.3, -1.0, 4.6, 1.6, CARD, SOFT, 5); r = box(3.3, -1.0, 4.6, 1.6, CARD, SOFT, 5)
        a1 = arrow((-0.6, 0.45), (-2.6, -0.1), SOFT, 6); a2 = arrow((0.6, 0.45), (2.6, -0.1), SOFT, 6)
        self.play(Create(a1), Create(a2), FadeIn(l), FadeIn(r), run_time=0.7)
        until(self, "as the rate for catching the sick")
        tl = T("sensitivity", 42, INK, bold=True).move_to([-3.3, -0.8, 0]); sl = T("catches the sick", 34, SOFT).move_to([-3.3, -1.4, 0])
        self.play(FadeIn(tl), FadeIn(sl), run_time=0.5)
        until(self, "and as the rate for clearing the healthy")
        tr = T("specificity", 42, INK, bold=True).move_to([3.3, -0.8, 0]); sr = T("clears the healthy", 34, SOFT).move_to([3.3, -1.4, 0])
        self.play(FadeIn(tr), FadeIn(sr), FadeIn(tdot(0, -2.5)), run_time=0.5)
        finish(self)


class B35_BackwardFleet(Scene):
    def construct(self):
        st, hd = open_stage(self)
        contrib = [0.8, 0.9, 1.5]; nm = ["A", "B", "C"]
        until(self, "Run Bayes backward")
        x = -4.0; bars = VGroup(); lbs = VGroup()
        for c, n_ in zip(contrib, nm):
            b = fbar(x, 0.9, c * 0.8, 0.8, BAR1 if n_ != "C" else INK)
            bars.add(b); lbs.add(T(n_, 34, INK).move_to([x + c * 0.4, 1.5, 0])); x += c * 0.8
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.3), FadeIn(lbs), run_time=1.2)
        lw = T("only the wrong outputs", 36, SOFT).move_to([-1.6, 2.05, 0])
        self.play(FadeIn(lw), run_time=0.3)
        until(self, "C handles thirty percent")
        tgt = []; xx = -4.0
        for c in contrib:
            w = 8.0 * c / 3.2
            tgt.append(fbar(xx, -0.8, w, 0.9, BAR1)); xx += w
        tgt[2].set_color(INK)
        self.play(*[Transform(bars[i], tgt[i]) for i in range(3)], FadeOut(lbs), FadeOut(lw), run_time=1.2)
        pcts = ["25%", "28%", "47%"]; xx = -4.0; pl = VGroup()
        for c, p in zip(contrib, pcts):
            w = 8.0 * c / 3.2
            pl.add(T(p, 44, INK, bold=True).move_to([xx + w / 2, -1.7, 0])); xx += w
        until(self, "forty-seven percent of the errors")
        self.play(FadeIn(pl), FadeIn(tdot(-4.0 + 8.0 * 2.0 / 3.2 + 8.0 * 1.5 / 3.2 / 2, -0.15, 0.12)), run_time=0.6)
        finish(self)


# ═════════════════════════ ACT VI ═════════════════════════
def _ppv(br):
    s = 0.99; f = 0.01
    return br * s / (br * s + (1 - br) * f)


class B36_BaseRateSlider(Scene):
    def construct(self):
        st, hd = open_stage(self)
        x0, x1, y0, y1 = -5.0, 4.6, -2.2, 1.9
        ax = axes(x0, y0, x1 - x0, y1 - y0)
        def px(lg): return x0 + (lg + 5.0) / 3.0 * (x1 - x0 - 0.4) + 0.2
        def py(v): return y0 + v * (y1 - y0 - 0.2)
        pts = [[px(-5.0 + 3.0 * i / 60), py(_ppv(10 ** (-5.0 + 3.0 * i / 60)))] for i in range(61)]
        curve = poly(pts, INK, 6)
        labs = VGroup(*[T(s, 32, SOFT).move_to([px(lg), y0 - 0.4, 0]) for lg, s in ((-5, "1 in 100,000"), (-4, "1 in 10,000"), (-3, "1 in 1,000"), (-2, "1 in 100"))])
        labs[0].move_to([px(-5) + 0.5, y0 - 0.4, 0]); labs[3].move_to([px(-2) - 0.3, y0 - 0.4, 0])
        self.play(Create(ax), FadeIn(labs), run_time=0.6)
        self.play(Create(curve), run_time=1.2)
        mk = tdot(px(-2), py(_ppv(0.01)), 0.15)
        until(self, "a positive is a coin flip")
        self.play(FadeIn(mk), run_time=0.3)
        rd = T("50%", 46, INK, bold=True).move_to([px(-2) - 0.9, py(0.5) + 0.5, 0])
        self.add(rd)
        for lg, txt, ph in ((-3, "9%", "nine percent"), (-4, "1%", "one percent at one in ten thousand"), (-5, "0.1%", "a tenth of a percent")):
            until(self, ph)
            self.play(mk.animate.move_to([px(lg), py(_ppv(10 ** lg)), 0]), Transform(rd, T(txt, 46, INK, bold=True).move_to([px(lg) + 0.6, py(_ppv(10 ** lg)) + 0.7, 0])), run_time=0.8)
        finish(self)


class B37_Everywhere(Scene):
    def construct(self):
        st, hd = open_stage(self)
        chips = ["fraud", "intrusions", "screening", "moderation"]
        cs = VGroup()
        for i, c in enumerate(chips):
            cs.add(VGroup(box(-4.3 + i * 0.0, 1.8 - i * 0.85, 2.6, 0.7, CARD, DIM, 4), T(c, 34, INK).move_to([-4.3, 1.8 - i * 0.85, 0])))
        until(self, "fraud")
        self.play(LaggedStart(*[FadeIn(c) for c in cs], lag_ratio=0.35), run_time=1.6)
        fun = Polygon([-1.4, 1.6, 0], [1.6, 1.6, 0], [0.5, -0.6, 0], [-0.3, -0.6, 0], stroke_color=INK, stroke_width=6, fill_color=CARD, fill_opacity=1)
        until(self, "An excellent detector")
        self.play(Create(fun), run_time=0.5)
        dots = VGroup(*[idot(-0.8 + (i % 4) * 0.5, 1.2 - (i // 4) * 0.35, 0.09, BAR2) for i in range(12)])
        self.play(FadeIn(dots), run_time=0.5)
        out = VGroup(*[idot(0.1 + 0.0, -1.1 - i * 0.28, 0.09, BAR2) for i in range(4)] + [idot(0.1, -2.2, 0.1, INK)])
        self.play(FadeIn(out), run_time=0.6)
        until(self, "raise the base rate")
        e1 = arrow((1.1, -0.2), (3.0, 0.6), SOFT, 6); t1 = T("raise the base rate", 34, INK).move_to([4.2, 0.9, 0])
        self.play(Create(e1), FadeIn(t1), run_time=0.5)
        until(self, "accept more missed cases")
        e2 = arrow((1.1, -0.6), (3.0, -1.4), SOFT, 6); t2 = T("accept more misses", 34, INK).move_to([4.3, -1.7, 0])
        self.play(Create(e2), FadeIn(t2), FadeIn(tdot(0.1, -2.7, 0.1)), run_time=0.5)
        finish(self)


class B38_Fatigue(Scene):
    def construct(self):
        st, hd = open_stage(self)
        tiles = VGroup(); marks = VGroup()
        for i in range(8):
            r, c = divmod(i, 4)
            x, y = -3.6 + c * 2.4, 1.3 - r * 1.5
            tiles.add(box(x, y, 1.9, 1.1, CARD, SOFT, 4))
            marks.add(T("!", 50, INK, bold=True).move_to([x, y, 0]))
        until(self, "Operators check the first alerts")
        self.play(LaggedStart(*[FadeIn(tiles[i]) for i in range(8)], lag_ratio=0.15), FadeIn(marks), run_time=1.6)
        until(self, "False")
        xs = []
        for i in range(3):
            r, c = divmod(i, 4)
            xs.append(cross(-3.6 + c * 2.4, 1.3 - r * 1.5, 0.3, SOFT, 7))
        self.play(*[Create(x) for x in xs], *[FadeOut(marks[i]) for i in range(3)], run_time=0.8)
        until(self, "Within weeks")
        rest = [cross(-3.6 + (i % 4) * 2.4, 1.3 - (i // 4) * 1.5, 0.3, SOFT, 7) for i in range(3, 8) if i != 7]
        self.play(*[Create(x) for x in rest], *[FadeOut(marks[i]) for i in range(3, 7)], *[tiles[i].animate.set_opacity(0.5) for i in range(7)], run_time=0.9)
        until(self, "they miss the real one")
        self.play(FadeOut(marks[7]), FadeIn(tdot(-3.6 + 3 * 2.4, 1.3 - 1.5, 0.2)), run_time=0.4)
        self.play(FadeIn(T("the real one", 36, INK, bold=True).move_to([0.0, -2.2, 0])), run_time=0.5)
        finish(self)


class B39_SepsisAlerts(Scene):
    def construct(self):
        st, hd = open_stage(self)
        k = 0.42
        t0 = T("one published external validation of a hospital sepsis model", 32, SOFT, maxw=11.0).move_to([0, 2.25, 0])
        self.play(FadeIn(t0), run_time=0.4)
        until(self, "fired on eighteen percent")
        b1 = fbar(-5.0, 0.95, 18 * k, 0.6, BAR1); l1 = T("alerts: 18% of hospitalizations", 36, INK).move_to([-5.0, 1.55, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(b1, LEFT), FadeIn(l1), run_time=0.8)
        until(self, "while sepsis was seven percent")
        b2 = fbar(-5.0, -0.35, 7 * k, 0.6, BAR2); l2 = T("sepsis: 7%", 36, INK).move_to([-5.0, 0.2, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(b2, LEFT), FadeIn(l2), run_time=0.8)
        until(self, "Alerts were right twelve percent")
        b3 = fbar(-5.0, -1.55, 12 * k, 0.6, INK); l3 = T("alerts that were right: 12%", 36, INK).move_to([-5.0, -0.95, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(b3, LEFT), FadeIn(l3), FadeIn(tdot(0.6, -1.7, 0.12)), run_time=0.8)
        self.play(FadeIn(T("Wong et al., JAMA Internal Medicine, 2021", 32, SOFT).move_to([0, -2.55, 0])), run_time=0.4)
        finish(self)


def _waffle(caught):
    cols, rows = 58, 44
    a = np.zeros((rows * 6, cols * 6, 3), dtype=np.uint8); a[:, :] = (250, 249, 245)
    for i in range(cols * rows):
        r, c = divmod(i, cols)
        col = (61, 57, 41) if i < caught else (180, 175, 166)
        a[r * 6 + 1:r * 6 + 5, c * 6 + 1:c * 6 + 5] = col
    return a


class B40_Missed(Scene):
    def construct(self):
        st, hd = open_stage(self)
        im0 = grid_img(_waffle(0), 4.4).move_to([-2.4, -0.1, 0])
        self.play(FadeIn(im0), run_time=0.6)
        lb = T("2,552 sepsis cases", 38, INK, bold=True).move_to([-2.4, -2.65, 0])
        self.play(FadeIn(lb), run_time=0.3)
        until(self, "missed sixty-seven percent")
        im1 = grid_img(_waffle(843), 4.4).move_to([-2.4, -0.1, 0])
        self.play(FadeIn(im1), run_time=0.6)
        self.remove(im0)
        t1 = T("caught: 843", 40, INK, bold=True).move_to([4.0, 0.9, 0]); t2 = T("missed: 1,709", 40, INK, bold=True).move_to([4.0, -0.2, 0])
        until(self, "seventeen hundred and nine")
        self.play(FadeIn(t1), FadeIn(t2), FadeIn(tdot(2.0, -0.2, 0.1)), run_time=0.6)
        finish(self)


# ═════════════════════════ ACT VII ═════════════════════════
class B41_BooleanOutput(Scene):
    def construct(self):
        st, hd = open_stage(self)
        f = box(-3.9, 0.7, 2.6, 1.8, CARD, SOFT, 5); ft = T("42", 80, INK, bold=True).move_to([-3.9, 0.7, 0]); fl = T("a fact", 38, SOFT).move_to([-3.9, -0.7, 0])
        self.play(FadeIn(f), FadeIn(ft), FadeIn(fl), run_time=0.6)
        until(self, "A model returning point nine one")
        c = box(2.8, 0.7, 2.8, 1.8, CARD, INK, 6); ct = T("0.91", 80, INK, bold=True).move_to([2.8, 0.7, 0]); cl = T("a claim", 38, INK, bold=True).move_to([2.8, -0.7, 0])
        self.play(FadeIn(c), FadeIn(ct), FadeIn(cl), run_time=0.6)
        until(self, "conditional on its parameters")
        tags = ["its parameters", "its training data", "where it is deployed"]
        cues = ["conditional on its parameters", "its training data", "assumptions about where"]
        for i, t in enumerate(tags):
            y = -1.45 - i * 0.55
            until(self, cues[i])
            self.play(FadeIn(T(t, 32, INK).move_to([2.8, y, 0])), FadeIn(tdot(1.0, y, 0.07)), run_time=0.5)
        finish(self)


class B42_ThreeConditions(Scene):
    def construct(self):
        st, hd = open_stage(self)
        plate = VGroup(RoundedRectangle(width=5.4, height=0.6, corner_radius=0.1, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([0, 0.9, 0]),
                       T("0.87", 52, INK, bold=True).move_to([0, 0.9, 0]))
        legs = VGroup(*[seg((x, 0.6), (x, -1.2), SOFT, 10) for x in (-2.2, 0.0, 2.2)])
        ls = ["resembles\ntraining data", "confidence\ncalibrated", "nothing\nhas shifted"]
        lb = VGroup(*[T(s, 32, INK).move_to([x, -1.9, 0]) for x, s in zip((-2.2, 0.0, 2.2), ls)])
        lb[0].move_to([-2.9, -1.95, 0]); lb[2].move_to([2.9, -1.95, 0])
        self.play(FadeIn(plate), run_time=0.4)
        until(self, "if this patient resembles")
        self.play(Create(legs[0]), FadeIn(lb[0]), run_time=0.5)
        until(self, "if the confidence is calibrated")
        self.play(Create(legs[1]), FadeIn(lb[1]), run_time=0.5)
        until(self, "if nothing has shifted")
        self.play(Create(legs[2]), FadeIn(lb[2]), run_time=0.5)
        until(self, "Remove any condition")
        self.play(FadeOut(legs[2]), plate.animate.rotate(-0.18).shift([0, -0.15, 0]), run_time=0.7)
        self.play(FadeIn(tdot(0, -2.5)), run_time=0.3)
        finish(self)


def _sunrise(x, y, col=INK, w=5):
    arc = Arc(radius=0.34, start_angle=0, angle=PI, color=col, stroke_width=w, arc_center=[x, y, 0])
    base = seg((x - 0.55, y), (x + 0.55, y), col, w)
    rays = VGroup(*[seg((x + 0.5 * math.cos(a), y + 0.5 * math.sin(a)), (x + 0.7 * math.cos(a), y + 0.7 * math.sin(a)), col, w - 1) for a in (0.5, PI / 2, PI - 0.5)])
    return VGroup(arc, base, rays)


class B43_Hume(Scene):
    def construct(self):
        st, hd = open_stage(self)
        until(self, "You have seen the sun rise")
        suns = VGroup(*[_sunrise(-4.9 + i * 1.25, 0.4) for i in range(8)])
        self.play(LaggedStart(*[FadeIn(s) for s in suns], lag_ratio=0.25), run_time=2.6)
        until(self, "Does that guarantee tomorrow")
        nxt = _sunrise(5.2, 0.4, DIM, 5)
        dl = T("?", 90, INK, bold=True).move_to([5.2, 1.7, 0])
        self.play(FadeIn(nxt), FadeIn(dl), run_time=0.6)
        until(self, "His answer: no")
        lg = T("no logical guarantee", 42, INK, bold=True).move_to([0, -1.5, 0])
        self.play(FadeIn(lg), run_time=0.5)
        until(self, "the world cooperates")
        self.play(FadeIn(T("the world cooperates", 38, SOFT).move_to([0, -2.3, 0])), FadeIn(tdot(-5.4, -1.5, 0.1)), run_time=0.5)
        finish(self)


def _bell(cx, base, h, s, n=40, span=2.5):
    pts = [[cx - span + 2 * span * i / n, base + h * math.exp(-((-span + 2 * span * i / n) ** 2) / (2 * s * s))] for i in range(n + 1)]
    return pts


class B44_PastAndFuture(Scene):
    def construct(self):
        st, hd = open_stage(self)
        base = hline(-5.3, 5.3, -1.6, SOFT, 5)
        past = poly(_bell(-1.8, -1.6, 2.6, 0.9), INK, 7)
        pl = T("training: the past", 36, INK, bold=True).move_to([-3.0, 1.6, 0])
        self.play(Create(base), Create(past), FadeIn(pl), run_time=0.9)
        until(self, "deployment is the future")
        fut = poly(_bell(-1.8, -1.6, 2.6, 0.9), DIM, 7)
        fl = T("deployment: the future", 36, SOFT, bold=True).move_to([3.2, 1.9, 0])
        self.play(Create(fut), FadeIn(fl), run_time=0.5)
        until(self, "distribution shift")
        self.play(fut.animate.shift([3.9, 0, 0]), run_time=1.4)
        sh = T("distribution shift", 42, INK, bold=True).move_to([0.8, -2.45, 0])
        self.play(FadeIn(sh), FadeIn(tdot(0.8, -2.0, 0.1)), run_time=0.5)
        finish(self)


class B45_GreenDashboard(Scene):
    def construct(self):
        st, hd = open_stage(self)
        p1 = box(-3.0, 0.5, 5.0, 3.6, CARD, DIM, 5); t1 = T("inputs", 34, SOFT).move_to([-3.0, 2.0, 0])
        p2 = box(3.1, 1.2, 3.4, 1.6, CARD, DIM, 5); t2 = T("confidence", 32, SOFT).move_to([3.1, 1.75, 0]); n2 = T("0.94", 56, INK, bold=True).move_to([3.1, 1.05, 0])
        p3 = box(3.1, -1.1, 3.4, 1.8, CARD, DIM, 5); t3 = T("actual outcomes", 32, SOFT).move_to([3.1, -0.45, 0])
        self.play(FadeIn(VGroup(p1, t1, p2, t2, n2, p3, t3)), run_time=0.6)
        bx = [[-4.5 + 0.06 * i, -0.6 + 1.5 * math.exp(-((0.06 * i - 1.0) ** 2) / 0.3)] for i in range(0, 34)]
        c1 = poly(bx, DIM, 6); c2 = poly(bx, INK, 6)
        until(self, "Its confidence was calculated")
        self.play(Create(c2), run_time=0.6)
        b3 = fbar(1.7, -1.5, 2.8, 0.4, INK); self.play(GrowFromEdge(b3, LEFT), run_time=0.4)
        until(self, "inputs slide away")
        self.play(c2.animate.shift([1.6, 0, 0]), run_time=1.6)
        until(self, "stays green")
        self.play(FadeIn(check(5.1, 1.0, 0.2, INK, 8)), run_time=0.4)
        until(self, "Only outcomes")
        self.play(Transform(b3, fbar(1.7, -1.5, 1.0, 0.4, INK)), FadeIn(tdot(4.6, -1.1, 0.11)), run_time=1.0)
        self.play(FadeIn(T("shape only", 32, SOFT).move_to([-3.0, -2.55, 0])), run_time=0.3)
        finish(self)


class B46_Shortcuts(Scene):
    def construct(self):
        st, hd = open_stage(self)
        def xray(cx, cy, mark):
            fr = box(cx, cy, 2.6, 2.2, DARK_L, DARK_L, 3)
            ribs = VGroup(*[Arc(radius=0.9 - 0.18 * k, start_angle=PI + 0.4, angle=PI - 0.8, color=GHOST, stroke_width=4, arc_center=[cx, cy + 0.5 - 0.0, 0]) for k in range(3)])
            g = VGroup(fr, ribs)
            if mark:
                g.add(T("L", 34, CARD, bold=True).move_to([cx - 0.95, cy + 0.75, 0]))
            return g
        xa = xray(-3.9, 0.9, True); xb = xray(3.9, 0.9, False)
        la = T("hospital A", 36, INK, bold=True).move_to([-3.9, 2.3, 0]); lb = T("hospital B", 36, INK, bold=True).move_to([3.9, 2.3, 0])
        self.play(FadeIn(xa), FadeIn(xb), FadeIn(la), FadeIn(lb), run_time=0.7)
        until(self, "confounding shortcuts")
        rg = circ(-4.85, 1.65, 0.38, TERRA, 6)
        self.play(Create(rg), run_time=0.5)
        sl = T("reads the marker, not the lung", 32, INK, maxw=4.6).move_to([-3.5, -0.7, 0])
        self.play(FadeIn(sl), run_time=0.4)
        until(self, "look accurate in testing")
        ba = fbar(-5.2, -1.4, 2.6, 0.4, INK); ta = T("accurate", 32, INK).move_to([-2.0, -1.4, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(ba, LEFT), FadeIn(ta), run_time=0.6)
        until(self, "fail at new hospitals")
        bb = fbar(2.2, -1.4, 1.0, 0.4, INK); tb = T("fails", 32, INK).move_to([3.4, -1.4, 0], aligned_edge=LEFT)
        self.play(GrowFromEdge(bb, LEFT), FadeIn(tb), run_time=0.6)
        self.play(FadeIn(T("illustration of the mechanism", 32, SOFT).move_to([0, -2.5, 0])), run_time=0.3)
        finish(self)


class B47_WhatMustHold(Scene):
    def construct(self):
        st, hd = open_stage(self)
        rec = box(0, 1.3, 7.4, 0.9, BAR3, INK, 5); rt = T("the track record", 40, INK, bold=True).move_to([0, 1.3, 0])
        self.play(FadeIn(rec), FadeIn(rt), run_time=0.5)
        until(self, "what would have to remain true")
        cond = ["same kind\nof inputs", "same\nbase rates", "same cause\nand effect"]
        xs = [-3.2, 0.0, 3.2]
        for x, c in zip(xs, cond):
            self.play(Create(seg((x, 0.85), (x, -0.5), SOFT, 9)), FadeIn(T(c, 32, INK).move_to([x, -1.05, 0])), run_time=0.5)
        until(self, "If you cannot answer that")
        qs = VGroup(*[T("?", 60, DIM, bold=True).move_to([x, -2.1, 0]) for x in xs])
        self.play(FadeIn(qs), run_time=0.5)
        until(self, "You just have not noticed")
        self.play(FadeIn(tdot(0, -2.7, 0.12)), run_time=0.3)
        finish(self)


# ═════════════════════════ ACT VIII ═════════════════════════
def _diag(x0=-5.0, y0=-2.5, s=4.8):
    """Reliability-diagram frame: x stated 0.5..1.0 -> [x0, x0+s]; y actual 0.5..1.0 -> [y0, y0+s*0.8]."""
    return x0, y0, s


def _rp(st, ac, x0=-5.0, y0=-2.5, w=5.2, h=4.2):
    return [x0 + (st - 0.5) / 0.5 * w, y0 + (ac - 0.5) / 0.5 * h]


def _frame(self, x0=-5.0, y0=-2.5, w=5.2, h=4.2):
    ax = axes(x0, y0, w, h)
    diag = dashed((x0, y0), (x0 + w, y0 + h), DIM, 5)
    xl = T("stated confidence", 32, SOFT).move_to([x0 + w / 2, y0 - 0.45, 0]); yl = T("actual", 32, SOFT).move_to([x0 - 0.2, y0 + h + 0.35, 0])
    return ax, diag, xl, yl


class B48_SevenHundred(Scene):
    def construct(self):
        st, hd = open_stage(self)
        t = T("says 70% on 1,000 cases", 40, INK, bold=True).move_to([0, 2.15, 0])
        self.play(FadeIn(t), run_time=0.4)
        k = 0.0075
        base = vline(-4.2, -2.2, 1.6, SOFT, 4)
        mark = dashed((-4.2 + 700 * k, -2.2), (-4.2 + 700 * k, 1.6), DIM, 5)
        self.play(Create(base), Create(mark), FadeIn(T("700", 34, SOFT).move_to([-4.2 + 700 * k, -2.8, 0])), run_time=0.5)
        data = [(700, "calibrated", 0.8), (400, "overconfident", -0.4), (900, "underconfident", -1.6)]
        for v, nm, y in data:
            if v == 700:
                until(self, "about seven hundred")
            if v == 400:
                until(self, "If four hundred do")
            if v == 900:
                until(self, "nine hundred")
            b = fbar(-4.2, y, v * k, 0.6, INK if v == 700 else BAR1)
            self.play(GrowFromEdge(b, LEFT), FadeIn(T(f"{v}  {nm}", 34, INK).move_to([max(-4.2 + v * k, 1.05) + 0.3, y, 0], aligned_edge=LEFT) if v != 900 else T(f"{v}  {nm}", 34, INK).move_to([-4.1, y - 0.62, 0], aligned_edge=LEFT)), run_time=0.7)
        self.play(FadeIn(tdot(-4.6, 0.8, 0.1)), run_time=0.3)
        finish(self)


class B49_Diagonal(Scene):
    def construct(self):
        st, hd = open_stage(self)
        ax, diag, xl, yl = _frame(self, -3.0, -2.5, 5.2, 4.2)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=0.6)
        until(self, "A calibrated model hugs the diagonal")
        self.play(Create(diag), run_time=0.7)
        until(self, "A miscalibrated one peels away")
        pts = [_rp(0.5 + 0.5 * i / 20, 0.5 + 0.5 * (i / 20) - 0.45 * (max(0.0, i / 20 - 0.35) ** 1.5) * 1.6, -3.0, -2.5) for i in range(21)]
        peel = poly(pts, INK, 7)
        self.play(Create(peel), run_time=1.2)
        until(self, "the shape of the peel")
        up = poly([_rp(0.5 + 0.5 * i / 20, min(1.0, 0.5 + 0.5 * (i / 20) + 0.25 * (max(0.0, i / 20 - 0.25) ** 1.2)), -3.0, -2.5) for i in range(21)], BAR1, 6)
        self.play(Create(up), run_time=0.8)
        self.play(FadeIn(T("overconfident", 36, INK, bold=True).move_to([4.7, -0.5, 0])), FadeIn(T("underconfident", 36, SOFT).move_to([4.7, 1.5, 0])), FadeIn(tdot(3.1, -0.5, 0.1)), run_time=0.6)
        self.play(FadeIn(T("shape only", 32, SOFT).move_to([4.7, -2.4, 0])), run_time=0.3)
        finish(self)


class B50_OurSimulation(Scene):
    def construct(self):
        st, hd = open_stage(self)
        ax, diag, xl, yl = _frame(self, -5.4, -2.5, 5.4, 4.2)
        self.play(Create(ax), Create(diag), FadeIn(xl), FadeIn(yl), run_time=0.7)
        cap_ = VGroup(T("our simulation: 20,000 cases", 34, SOFT).move_to([2.6, 1.9, 0]), T("accuracy 0.746", 34, SOFT).move_to([2.6, 1.35, 0]))
        self.play(FadeIn(cap_), run_time=0.3)
        until(self, "Sorted by stated confidence")
        dots = VGroup()
        for r in _CAL["bins_before"]:
            p = _rp(r[3], r[4], -5.4, -2.5, 5.4, 4.2)
            d = idot(p[0], p[1], 0.13, INK); dots.add(d)
            self.play(FadeIn(d), run_time=0.45)
        until(self, "badly overconfident at the top")
        top = _CAL["bins_before"][-1]; p = _rp(top[3], top[4], -5.4, -2.5, 5.4, 4.2)
        self.play(Create(circ(p[0], p[1], 0.32, TERRA, 6)), run_time=0.5)
        self.play(FadeIn(T("states 0.97", 38, INK, bold=True).move_to([2.6, 0.5, 0])), FadeIn(T("right 0.86", 38, INK, bold=True).move_to([2.6, -0.2, 0])), run_time=0.6)
        finish(self)


class B51_Guo(Scene):
    def construct(self):
        st, hd = open_stage(self)
        for k, (x0, nm, bend) in enumerate(((-5.6, "a decade earlier", 0.02), (0.6, "modern networks", 0.35))):
            ax = axes(x0, -2.0, 4.6, 3.6)
            dg = dashed((x0, -2.0), (x0 + 4.6, 1.6), DIM, 5)
            lb = T(nm, 36, INK, bold=True).move_to([x0 + 2.3, 2.2, 0])
            pts = [[x0 + 4.6 * i / 20, -2.0 + 3.6 * (i / 20) - 3.6 * bend * (max(0, i / 20 - 0.3) ** 1.4)] for i in range(21)]
            cv = poly(pts, INK, 7)
            self.play(Create(ax), Create(dg), FadeIn(lb), run_time=0.5)
            self.play(Create(cv), run_time=0.9)
            if k == 0:
                until(self, "poorly calibrated")
        self.play(FadeIn(T("schematic; Guo et al., ICML 2017", 32, SOFT).move_to([0, -2.75, 0])), FadeIn(tdot(5.4, -1.0, 0.1)), run_time=0.5)
        finish(self)


def _softmax(z, t):
    e = [math.exp(v / t) for v in z]; s = sum(e)
    return [v / s for v in e]


class B52_Temperature(Scene):
    def construct(self):
        st, hd = open_stage(self)
        eq = M(r"\mathrm{softmax}(z/T)", 60).move_to([0, 2.0, 0])
        self.play(FadeIn(eq), run_time=0.6)
        until(self, "Divide the logits")
        z = [2.0, 1.0, 0.1]
        p1 = _softmax(z, 1.0); p2 = _softmax(z, 2.19)
        base = hline(-3.4, 3.4, -1.8, SOFT, 5)
        names = ["class 1", "class 2", "class 3"]
        bars = VGroup(*[vbar(-2.2 + i * 2.2, -1.8, 3.2 * p1[i], 1.1, INK if i == 0 else BAR1) for i in range(3)])
        lbs = VGroup(*[T(n, 32, INK).move_to([-2.2 + i * 2.2, -2.3, 0]) for i, n in enumerate(names)])
        tt = T("T = 1", 40, INK, bold=True).move_to([4.5, 0.4, 0])
        self.play(Create(base), FadeIn(lbs), run_time=0.4)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars], FadeIn(tt), run_time=0.8)
        until(self, "With T above one")
        tgt = [vbar(-2.2 + i * 2.2, -1.8, 3.2 * p2[i], 1.1, INK if i == 0 else BAR1) for i in range(3)]
        self.play(*[Transform(bars[i], tgt[i]) for i in range(3)], Transform(tt, T("T = 2.19", 40, INK, bold=True).move_to([4.5, 0.4, 0])), run_time=1.4)
        self.play(FadeIn(T("same order, softer", 34, SOFT).move_to([4.0, -0.4, 0])), FadeIn(tdot(-2.2, 0.0 - 0.0 + 0.9, 0.1)), run_time=0.5)
        finish(self)


class B53_FitT(Scene):
    def construct(self):
        st, hd = open_stage(self)
        ax, diag, xl, yl = _frame(self, -5.4, -2.5, 5.4, 4.2)
        self.play(Create(ax), Create(diag), FadeIn(xl), FadeIn(yl), run_time=0.5)
        before = VGroup(*[idot(*_rp(r[3], r[4], -5.4, -2.5, 5.4, 4.2)[:2], 0.13, INK) for r in _CAL["bins_before"]])
        self.play(FadeIn(before), run_time=0.5)
        until(self, "two point one nine")
        self.play(FadeIn(T(f"fitted T = {_CAL['T']}", 44, INK, bold=True).move_to([3.2, 1.6, 0])), run_time=0.5)
        until(self, "The dots slide onto the diagonal")
        after = [idot(*_rp(r[3], r[4], -5.4, -2.5, 5.4, 4.2)[:2], 0.13, INK) for r in _CAL["bins_after"]]
        self.play(*[Transform(before[i], after[i]) for i in range(5)], run_time=1.5)
        until(self, "Accuracy did not change")
        self.play(FadeIn(T("accuracy 74.6% before", 36, INK).move_to([3.2, 0.5, 0])), FadeIn(T("accuracy 74.6% after", 36, INK).move_to([3.2, -0.2, 0])), FadeIn(tdot(0.2, 0.2, 0.1)), run_time=0.7)
        finish(self)


class B54_Decorative(Scene):
    def construct(self):
        st, hd = open_stage(self)
        a1, h1 = gauge(-3.0, -0.4, 1.9); a2, h2 = gauge(3.0, -0.4, 1.9)
        l1 = T("confidence", 40, INK, bold=True).move_to([-3.0, -1.5, 0]); l2 = T("correctness", 40, INK, bold=True).move_to([3.0, -1.5, 0])
        n1 = needle_at(-3.0, -0.4, 1.9, 0.9); n2 = needle_at(3.0, -0.4, 1.9, 0.55)
        self.play(FadeIn(a1), FadeIn(h1), FadeIn(a2), FadeIn(h2), FadeIn(l1), FadeIn(l2), run_time=0.6)
        until(self, "confidence and correctness were separable")
        self.play(Create(n1), Create(n2), run_time=0.8)
        until(self, "The number was decorative")
        self.play(FadeIn(tip_at(-3.0, -0.4, 1.9, 0.9)), run_time=0.3)
        until(self, "un-decorate it")
        self.play(Transform(n1, needle_at(-3.0, -0.4, 1.9, 0.57)), run_time=1.0)
        self.play(FadeIn(tdot(0, 0.0, 0.14)), run_time=0.3)
        until(self, "average calibration")
        self.play(FadeIn(T("average calibration only", 36, SOFT).move_to([0, 2.15, 0])), run_time=0.4)
        finish(self)


class B55_GoesStale(Scene):
    def construct(self):
        st, hd = open_stage(self)
        ax, diag, xl, yl = _frame(self, -5.4, -2.5, 5.4, 4.2)
        self.play(Create(ax), Create(diag), FadeIn(xl), FadeIn(yl), run_time=0.5)
        dots = VGroup(*[idot(*_rp(r[3], r[4], -5.4, -2.5, 5.4, 4.2)[:2], 0.13, INK) for r in _CAL["bins_after"]])
        self.play(FadeIn(dots), run_time=0.5)
        until(self, "drifts from that calibration set")
        ar = arrow((1.4, 1.7), (3.8, 1.7), SOFT, 7)
        self.play(Create(ar), FadeIn(T("the world moves", 36, INK, bold=True).move_to([2.6, 2.3, 0])), run_time=0.7)
        until(self, "goes stale, silently")
        tg = [idot(*_rp(r[3], r[4] - 0.14 * (r[3] - 0.5) / 0.5, -5.4, -2.5, 5.4, 4.2)[:2], 0.13, INK) for r in _CAL["bins_after"]]
        self.play(*[Transform(dots[i], tg[i]) for i in range(5)], run_time=1.6)
        until(self, "on the day the world moves")
        self.play(FadeIn(T("no alarm", 40, INK, bold=True).move_to([3.2, -0.6, 0])), FadeIn(tdot(1.6, -0.6, 0.1)), run_time=0.5)
        finish(self)


class B56_RejectCondition(Scene):
    def construct(self):
        st, hd = open_stage(self)
        ax, diag, xl, yl = _frame(self, -5.4, -2.5, 5.4, 4.2)
        self.play(Create(ax), Create(diag), FadeIn(xl), FadeIn(yl), run_time=0.5)
        until(self, "decide in advance")
        x0, y0, w, h = -5.4, -2.5, 5.4, 4.2
        band = Polygon([x0, y0, 0], [x0 + w, y0 + h - 0.45, 0], [x0 + w, y0 + h + 0.45 - 0.9, 0], [x0, y0 + 0.0, 0], stroke_width=0, stroke_opacity=0, fill_color=GHOST, fill_opacity=0.7)
        band = Polygon([x0 + 0.0, y0 - 0.0, 0], [x0 + w, y0 + h - 0.8, 0], [x0 + w, y0 + h, 0], stroke_width=0, stroke_opacity=0, fill_color=GHOST, fill_opacity=0.7)
        self.play(FadeIn(band), FadeIn(T("reject below this line", 34, INK).move_to([3.3, -0.1, 0])), FadeIn(T("(example criterion)", 32, SOFT).move_to([3.3, -0.65, 0])), run_time=0.8)
        until(self, "never trust a stated probability")
        dots = VGroup()
        for r in _CAL["bins_before"]:
            d = idot(*_rp(r[3], r[4], x0, y0, w, h)[:2], 0.13, INK); dots.add(d)
        self.play(FadeIn(dots), run_time=0.6)
        until(self, "judging a score by how confident it sounds")
        top = _CAL["bins_before"][-1]; p = _rp(top[3], top[4], x0, y0, w, h)
        self.play(Create(circ(p[0], p[1], 0.32, TERRA, 6)), FadeIn(T("rejected", 40, INK, bold=True).move_to([3.3, 1.2, 0])), run_time=0.6)
        finish(self)


class B57_YourIntervals(Scene):
    def construct(self):
        st, hd = open_stage(self)
        rng = _random.Random(9)
        truth_x = 0.0
        hit = [True, False, True, False, False, True, False, True, False, False]
        until(self, "ninety percent intervals")
        ivs = VGroup(); tk = VGroup()
        for i, h in enumerate(hit):
            y = 2.0 - i * 0.4
            c = rng.uniform(-0.8, 0.8)
            lo = c - 0.5; hi = c + 0.5
            tx = c + (0.0 if h else (0.9 if i % 2 else -0.9))
            ivs.add(seg((-3.5 + lo * 1.4, y), (-3.5 + hi * 1.4, y), SOFT, 7))
            tk.add(idot(-3.5 + tx * 1.4, y, 0.08, INK if h else DIM))
        self.play(LaggedStart(*[Create(s) for s in ivs], lag_ratio=0.12), run_time=1.4)
        tl = vline(-3.5, -2.2, 2.3, GHOST, 3)
        self.play(FadeIn(tk), run_time=0.5)
        until(self, "far less often than ninety")
        sc = hline(1.0, 5.4, 0.0, SOFT, 6)
        t0 = T("0", 32, SOFT).move_to([1.0, -0.45, 0]); t1 = T("100%", 32, SOFT).move_to([5.4, -0.45, 0])
        tg = seg((1.0 + 4.4 * 0.9, -0.3), (1.0 + 4.4 * 0.9, 0.3), INK, 7); tgl = T("90% target", 34, INK, bold=True).move_to([1.0 + 4.4 * 0.9 - 0.2, 0.75, 0])
        self.play(Create(sc), FadeIn(t0), FadeIn(t1), Create(tg), FadeIn(tgl), run_time=0.7)
        until(self, "between thirty and sixty")
        band = fbar(1.0 + 4.4 * 0.3, 0.0, 4.4 * 0.3, 0.45, BAR1)
        self.play(GrowFromEdge(band, LEFT), FadeIn(T("hit rate: 30 to 60%", 34, INK, bold=True).move_to([2.9, -1.1, 0])), run_time=0.7)
        self.play(FadeIn(T("illustration, not data", 32, SOFT).move_to([-3.5, -2.6, 0])), FadeIn(tdot(5.4, 0.9, 0.1)), run_time=0.4)
        finish(self)


# ═════════════════════════ ACT IX ═════════════════════════
class B58_TwoRequirements(Scene):
    def construct(self):
        st, hd = open_stage(self)
        n = 9
        hs = [math.comb(n, k) / 2 ** n for k in range(n + 1)]
        bars = VGroup(*[vbar(-3.6 + k * 0.8, -1.8, hs[k] * 7.0, 0.7, BAR2) for k in range(n + 1)])
        base = hline(-4.3, 3.3, -1.8, SOFT, 5)
        until(self, "sums of many independent variables")
        self.play(Create(base), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.12), run_time=1.6)
        bell = poly([[-3.9 + 7.8 * i / 40, -1.8 + 7.0 * 0.246 * math.exp(-((-3.9 + 7.8 * i / 40) ** 2) / 2.88)] for i in range(41)], INK, 6)
        until(self, "look like a bell curve")
        self.play(Create(bell), run_time=0.8)
        until(self, "independence, and finite variance")
        g1 = box(4.2, 0.9, 3.2, 0.9, CARD, SOFT, 5); t1 = T("independent", 34, INK, bold=True).move_to([4.4, 0.9, 0])
        g2 = box(4.2, -0.5, 3.2, 0.9, CARD, SOFT, 5); t2 = T("finite variance", 32, INK, bold=True).move_to([4.4, -0.5, 0])
        self.play(FadeIn(g1), FadeIn(t1), FadeIn(g2), FadeIn(t2), run_time=0.6)
        self.play(FadeIn(lock(2.95, 0.9)), FadeIn(lock(2.95, -0.5)), FadeIn(tdot(4.2, 1.65, 0.1)), run_time=0.5)
        finish(self)


class B59_QuietFailure(Scene):
    def construct(self):
        st, hd = open_stage(self)
        base = hline(-5.4, 5.4, -1.8, SOFT, 5)
        bell = poly([[-5.0 + 10.0 * i / 80, -1.8 + 3.2 * math.exp(-((-5.0 + 10.0 * i / 80 - 0.0) ** 2) / 1.8)] for i in range(81)], INK, 7)
        self.play(Create(base), Create(bell), run_time=0.7)
        until(self, "Independence breaks")
        tg = T("independence breaks: networks, memory", 34, INK, bold=True, maxw=11.0).move_to([0, 2.1, 0])
        self.play(FadeIn(tg), run_time=0.5)
        until(self, "Finite variance breaks")
        tail = poly([[-5.0 + 10.0 * i / 80, -1.8 + 3.2 * 0.9 / ((1 + ((-5.0 + 10.0 * i / 80) / 0.9) ** 2))] for i in range(81)], DIM, 7)
        self.play(Create(tail), run_time=1.0)
        t2 = T("finite variance breaks: heavy tails", 34, INK, bold=True, maxw=11.0).move_to([0, 1.55, 0])
        self.play(FadeIn(t2), run_time=0.4)
        until(self, "too common for averaging")
        self.play(FadeIn(Rectangle(width=2.2, height=0.5, fill_color=GHOST, fill_opacity=0.9, stroke_width=0, stroke_opacity=0).move_to([4.2, -1.55, 0])), FadeIn(T("the tail", 34, INK).move_to([4.2, -2.3, 0])), FadeIn(tdot(4.2, -1.05, 0.1)), run_time=0.6)
        finish(self)


class B60_NeverSettles(Scene):
    def construct(self):
        st, hd = open_stage(self)
        gm = _SER["gauss_means"]; cm = _SER["cauchy_means"]
        x0, x1 = -5.2, 5.0
        lo = min(min(cm), min(gm)); hi = max(max(cm), max(gm))
        lo = min(lo, -8.0); hi = max(hi, 1.5)
        def py(v): return -2.3 + (v - lo) / (hi - lo) * 4.3
        def px(i): return x0 + (x1 - x0) * i / (len(gm) - 1)
        ax = axes(x0, -2.3, x1 - x0, 4.3)
        zero = dashed((x0, py(0)), (x1, py(0)), DIM, 4)
        self.play(Create(ax), Create(zero), FadeIn(T("draws", 32, SOFT).move_to([x1 - 0.4, -2.75, 0])), run_time=0.5)
        until(self, "From a bell curve")
        g = poly([[px(i), py(gm[i])] for i in range(3, len(gm), 2)], INK, 6)
        self.play(Create(g), run_time=2.0)
        self.play(FadeIn(T("bell curve: 0.009", 36, INK, bold=True).move_to([-3.0, py(0.0) - 0.55, 0])), run_time=0.4)
        until(self, "From a Koshee distribution")
        c = poly([[px(i), py(cm[i])] for i in range(3, len(cm), 1)], DIM, 6)
        self.play(Create(c), run_time=3.0)
        until(self, "minus forty-three thousand")
        jmp = max(range(1, len(cm)), key=lambda i: abs(cm[i] - cm[i - 1]))
        self.play(Create(circ(px(jmp), py(cm[jmp]), 0.3, TERRA, 6)), FadeIn(T("one draw moved it by 12", 34, INK, bold=True).move_to([-1.2, py(-5.0), 0])), run_time=0.7)
        until(self, "minus six point eight")
        self.play(FadeIn(T("Cauchy: -6.8", 36, INK, bold=True).move_to([3.4, py(cm[-1]) + 0.55, 0])), run_time=0.4)
        finish(self)


class B61_CostOfError(Scene):
    def construct(self):
        st, hd = open_stage(self)
        small = VGroup(*[Square(side_length=0.2, fill_color=BAR2, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([-5.0 + (i % 16) * 0.26, 1.2 - (i // 16) * 0.26, 0]) for i in range(64)])
        until(self, "wastes ten dollars")
        self.play(FadeIn(small), run_time=0.8)
        self.play(FadeIn(T("$10 per false alarm", 36, INK, bold=True).move_to([-3.1, -0.45, 0])), run_time=0.4)
        until(self, "a missed breach costs")
        big = Rectangle(width=2.6, height=3.2, fill_color=INK, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([4.1, 0.0, 0])
        self.play(GrowFromEdge(big, DOWN), run_time=0.9)
        self.play(FadeIn(T("$500,000 per\nmissed breach", 34, INK, bold=True).move_to([4.1, -2.3, 0])), FadeIn(T("not to scale", 32, SOFT).move_to([4.1, 2.0, 0])), FadeIn(tdot(2.5, 1.8, 0.1)), run_time=0.6)
        self.play(FadeIn(T("made-up numbers", 32, SOFT).move_to([-3.1, -1.2, 0])), run_time=0.3)
        finish(self)


class B62_TailAware(Scene):
    def construct(self):
        st, hd = open_stage(self)
        base = hline(-5.0, 0.6, -1.9, SOFT, 5)
        until(self, "An average-loss metric")
        b1 = vbar(-3.6, -1.9, 0.5, 1.5, BAR2); l1 = T("average loss", 36, INK).move_to([-3.6, -2.45, 0])
        self.play(Create(base), GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=0.7)
        until(self, "the rare catastrophic case")
        b2 = vbar(-1.2, -1.9, 3.8, 1.5, INK); l2 = T("worst case", 36, INK).move_to([-1.2, -2.45, 0])
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), FadeIn(tdot(-1.2, 2.2, 0.12)), run_time=0.8)
        items = ["tail-aware metrics", "worst-case analysis", "adversarial inputs"]
        cues = ["tail-aware metrics", "worst-case analysis", "adversarial inputs"]
        for i, (t, c) in enumerate(zip(items, cues)):
            until(self, c)
            y = 1.3 - i * 1.0
            self.play(FadeIn(box(3.5, y, 3.8, 0.75, CARD, SOFT, 4)), FadeIn(T(t, 32, INK).move_to([3.5, y, 0])), Create(check(1.2, y, 0.15, INK, 7)), run_time=0.5)
        finish(self)


class B63_Impolite(Scene):
    def construct(self):
        st, hd = open_stage(self)
        rng = _random.Random(4)
        pts = VGroup(*[idot(-5.0 + abs(rng.gauss(0, 1.1)) * 1.3, -1.0 + rng.uniform(-0.9, 0.9), 0.07, INK) for _ in range(40)])
        axl = hline(-5.4, 5.4, -2.2, SOFT, 5)
        self.play(Create(axl), FadeIn(pts), run_time=0.8)
        until(self, "no clean way to tell")
        tail = Rectangle(width=4.0, height=3.0, stroke_color=DIM, stroke_width=4, fill_opacity=0).move_to([3.3, -0.7, 0])
        self.play(Create(DashedVMobject(tail, num_dashes=40)) if False else Create(tail), FadeIn(T("?", 90, DIM, bold=True).move_to([3.3, -0.7, 0])), run_time=0.7)
        until(self, "mathematically impolite")
        self.play(FadeIn(T("a sample cannot show the tail", 36, INK).move_to([0, 1.9, 0])), run_time=0.5)
        until(self, "assume heavy tails when errors can harm people")
        self.play(FadeIn(T("heuristic, not a calculation", 38, INK, bold=True).move_to([0, 1.3, 0])), FadeIn(tdot(0, 0.7, 0.12)), run_time=0.6)
        finish(self)


# ═════════════════════════ ACT X ═════════════════════════
def _mini(kind, cx, cy):
    g = VGroup()
    if kind == "prior":
        g.add(*[idot(cx - 0.5 + (i % 5) * 0.25, cy + 0.3 - (i // 5) * 0.25, 0.06, BAR2) for i in range(15)], idot(cx + 0.25, cy + 0.05, 0.08, INK))
    elif kind == "score":
        g.add(T("0.94", 54, INK, bold=True).move_to([cx, cy, 0]))
    elif kind == "tail":
        g.add(poly([[cx - 0.9 + 1.8 * i / 20, cy - 0.5 + 0.9 / (1 + ((i - 6) / 2.2) ** 2)] for i in range(21)], INK, 5))
    elif kind == "shift":
        g.add(poly(_bell(cx - 0.4, cy - 0.5, 0.9, 0.3, 20, 0.7), INK, 5), poly(_bell(cx + 0.4, cy - 0.5, 0.9, 0.3, 20, 0.7), DIM, 5))
    return g


class B64_Interpretation(Scene):
    def construct(self):
        st, hd = open_stage(self)
        ks = ["prior", "score", "tail", "shift"]
        names = ["forgets\nthe prior", "trusts\nthe number", "averages\nthe tail", "assumes\nno change"]
        cues = ["forgets the prior", "trusts the stated number", "averages over a heavy tail", "assumes the world"]
        xs = [-4.5, -1.5, 1.5, 4.5]
        for k, n_, c, x in zip(ks, names, cues, xs):
            until(self, c)
            self.play(FadeIn(box(x, 0.2, 2.7, 2.6, CARD, SOFT, 4)), FadeIn(_mini(k, x, 0.5)), FadeIn(T(n_, 32, INK, maxw=2.5).move_to([x, -0.75, 0])), run_time=0.6)
        self.play(FadeIn(tdot(0, -2.0, 0.12)), run_time=0.3)
        finish(self)


class B65_FourQuestions(Scene):
    def construct(self):
        st, hd = open_stage(self)
        xs = [-4.5, -1.5, 1.5, 4.5]
        qs = ["base rate?", "calibrated?", "cost of error?", "what changed?"]
        marks = ["prior", "calib", "tail", "shift"]
        cues = ["What is the base rate", "Is the model calibrated", "distribution of the cost", "what has changed since training"]
        for i, (x, q, m, c) in enumerate(zip(xs, qs, marks, cues)):
            until(self, c)
            if m == "calib":
                mk = VGroup(seg((x - 0.6, 0.0), (x + 0.6, 0.9), SOFT, 5), *[idot(x - 0.5 + j * 0.3, 0.05 + j * 0.22 - (0.0 if j < 2 else (j - 1) * 0.08), 0.07, INK) for j in range(5)])
            else:
                mk = _mini(m, x, 0.5)
            self.play(FadeIn(box(x, 0.4, 2.7, 3.0, CARD, SOFT, 4)), FadeIn(mk), FadeIn(T(str(i + 1), 44, INK, bold=True).move_to([x, 1.45, 0])), FadeIn(T(q, 34, INK, maxw=2.5).move_to([x, -0.75, 0])), run_time=0.6)
        self.play(FadeIn(tdot(0, -2.1, 0.12)), run_time=0.3)
        finish(self)


class B66_OpenEdge(Scene):
    def construct(self):
        st, hd = open_stage(self)
        outp = box(-4.0, 0.6, 2.8, 1.2, CARD, SOFT, 5); ot = T("outputs", 38, INK, bold=True).move_to([-4.0, 0.6, 0])
        det = box(0.0, 0.6, 2.6, 1.2, CARD, INK, 6); dt = T("detector", 38, INK, bold=True).move_to([0, 0.6, 0])
        self.play(FadeIn(outp), FadeIn(ot), FadeIn(det), FadeIn(dt), run_time=0.6)
        until(self, "detected shift from outputs alone")
        self.play(Create(arrow((-2.5, 0.6), (-1.4, 0.6), INK, 7)), run_time=0.5)
        until(self, "without outcomes")
        out2 = box(4.2, 0.6, 2.8, 1.2, CARD, DIM, 4); o2 = T("outcomes", 38, SOFT, bold=True).move_to([4.2, 0.6, 0])
        self.play(FadeIn(out2), FadeIn(o2), Create(dashed((1.4, 0.6), (2.7, 0.6), DIM, 5)), run_time=0.7)
        until(self, "remains an open problem")
        self.play(FadeIn(T("?", 80, DIM, bold=True).move_to([2.05, 1.5, 0])), FadeIn(T("open problem", 42, INK, bold=True).move_to([0, -1.5, 0])), FadeIn(tdot(0, -0.9, 0.12)), run_time=0.7)
        finish(self)
