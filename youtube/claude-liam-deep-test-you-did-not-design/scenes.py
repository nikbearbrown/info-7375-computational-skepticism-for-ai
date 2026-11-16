"""
scenes.py — claude-liam-deep-test-you-did-not-design
The Test You Did Not Design. — Computational Skepticism for AI, channel claude-liam

Palette: Claude brand (FIDELITY — never retinted)
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider

MANIM beats (10): A1M A1M2 A2M A2M2 A2M3 A3M A4M A5M A6M A6M2
Durations are read from beat_sheet.json (actual_duration_s after audio lock,
estimated_duration_s before) so the scene always conforms to the clock.
"""

import json, os, random
from manim import *
import numpy as np

# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass

try:
    BOLD
except NameError:
    BOLD = "BOLD"; NORMAL = "NORMAL"

PAGE   = "#FAF9F5"
STAGE  = "#F2F0E9"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"
config.background_color = PAGE

_HERE = os.path.dirname(os.path.abspath(__file__))
try:
    _SHEET = json.load(open(os.path.join(_HERE, "beat_sheet.json")))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 12.0)
           for b in _SHEET["beats"]}
except Exception:
    DUR = {}

def dur_of(bid, fallback=14.0):
    return float(DUR.get(bid, fallback))


class _Beat(Scene):
    """Clock helper: self.seek(frac) waits until frac*dur has elapsed.
    State is lazy (no reliance on setup()/__init__) so the render-free static
    checker, which stubs Scene, can execute construct() unchanged."""
    BID = "B00"
    @property
    def dur(self):
        if not hasattr(self, "_dur"):
            self._dur = dur_of(self.BID)
        return self._dur
    @property
    def elapsed(self):
        return getattr(self, "_elapsed", 0.0)
    @elapsed.setter
    def elapsed(self, v):
        self._elapsed = v
    def go(self, *anims, rt=0.5, **kw):
        if anims:
            self.play(*anims, run_time=rt, **kw)
        self.elapsed = self.elapsed + rt
    def seek(self, frac):
        target = frac * self.dur
        if target > self.elapsed:
            self.wait(target - self.elapsed); self.elapsed = target
    def finish(self):
        rest = self.dur - self.elapsed
        if rest > 0.05:
            self.wait(rest)


# run.sh discovers scenes by the literal `class X(Scene)` signature, so the clock helpers are
# attached to Scene itself rather than used as a base class.
for _n in ("go", "seek", "finish"):
    setattr(Scene, _n, getattr(_Beat, _n))
Scene.dur = _Beat.dur
Scene.elapsed = _Beat.elapsed
Scene.BID = "B00"

def label(s, size=30, color=SOFT, weight=NORMAL):
    return Text(s, font_size=size, color=color, weight=weight)

def title(s, size=48):
    return Text(s, font_size=size, color=INK, weight=BOLD)

def underline(mob, color=SPARK):
    return Line(mob.get_corner(DL) + DOWN * 0.08, mob.get_corner(DR) + DOWN * 0.08,
                color=color, stroke_width=3)


# ── A1M — the battery ───────────────────────────────────────────────────────
class A1M_Battery(Scene):
    """The whole battery is on screen from frame 0 as ghost rows; each row fills and lights on its spoken word; SHIPPED is its own row; the unscored question is the terracotta last row."""
    BID = "A1M"
    def construct(self):
        t = title("The Validation Battery", 50).to_edge(UP, buff=0.8)
        rows = ["Accuracy on validation — 94%", "Internal review thresholds — met",
                "Regulatory submission — cleared", "Fairness metrics — within tolerance"]
        ats = [0.05, 0.22, 0.36, 0.50]
        y0, dy = 1.95, 0.95
        ghosts = []
        for i, r in enumerate(rows):
            y = y0 - i * dy
            box = RoundedRectangle(width=9.0, height=0.8, corner_radius=0.12, fill_color=PAGE, fill_opacity=1,
                                   stroke_color=BORDER, stroke_width=2).move_to([-1.6, y, 0])
            txt = label(r, 36, GHOST).next_to(box.get_left(), RIGHT, buff=0.45)
            lamp = Circle(radius=0.2, color=BORDER, stroke_width=2.5, fill_opacity=0).move_to([3.45, y, 0])
            ghosts.append((box, txt, lamp))
        # two empty rows at the foot of the form — the battery is a form with six lines from frame 0
        tail_ghosts = [RoundedRectangle(width=9.0, height=0.8, corner_radius=0.12, fill_color=PAGE, fill_opacity=1,
                                        stroke_color=BORDER, stroke_width=2).move_to([-1.6, y0 - k * dy, 0]) for k in (4, 5)]
        self.go(FadeIn(t, shift=DOWN * 0.2), *[FadeIn(m) for g in ghosts for m in g], *[FadeIn(g) for g in tail_ghosts], rt=0.5)
        for i, ((box, txt, lamp), a) in enumerate(zip(ghosts, ats)):
            self.seek(a)
            y = y0 - i * dy
            fbox = RoundedRectangle(width=9.0, height=0.8, corner_radius=0.12, fill_color=STAGE, fill_opacity=1,
                                    stroke_color=BORDER, stroke_width=2).move_to([-1.6, y, 0])
            ftxt = label(rows[i], 36, INK).next_to(fbox.get_left(), RIGHT, buff=0.45)
            flamp = Circle(radius=0.2, color=INK, fill_color=INK, fill_opacity=1).move_to([3.45, y, 0])
            ok = Text("PASS", font_size=30, color=INK, weight=BOLD).next_to(flamp, RIGHT, buff=0.25)
            self.go(Transform(box, fbox), Transform(txt, ftxt), Transform(lamp, flamp), FadeIn(ok), rt=0.4)
        self.seek(0.62)
        y = y0 - 4 * dy
        sbox = RoundedRectangle(width=9.0, height=0.8, corner_radius=0.12, fill_color=INK, fill_opacity=1,
                                stroke_color=INK, stroke_width=2).move_to([-1.6, y, 0])
        stxt = Text("Deployed", font_size=36, color=PAGE, weight=BOLD).next_to(sbox.get_left(), RIGHT, buff=0.45)
        stamp = Text("SHIPPED", font_size=30, color=INK, weight=BOLD).move_to([4.25, y, 0])
        self.go(Transform(tail_ghosts[0], sbox), FadeIn(stxt), FadeIn(stamp, scale=1.3), rt=0.4)
        self.seek(0.78)
        y = y0 - 5 * dy
        box5 = RoundedRectangle(width=9.0, height=0.8, corner_radius=0.12, fill_color=PAGE, fill_opacity=1,
                                stroke_color=SPARK, stroke_width=3).move_to([-1.6, y, 0])
        txt5 = label("What is going on with THIS patient?", 36, SPARK, BOLD).next_to(box5.get_left(), RIGHT, buff=0.45)
        lamp5 = Circle(radius=0.2, color=SPARK, stroke_width=3, fill_opacity=0).move_to([3.45, y, 0])
        un = Text("UNSCORED", font_size=30, color=SPARK, weight=BOLD).next_to(lamp5, RIGHT, buff=0.25)
        self.go(Transform(tail_ghosts[1], box5), Write(txt5), rt=0.7)
        self.go(Create(lamp5), FadeIn(un), rt=0.3)
        self.finish()


# ── A1M2 — not an anomaly, a structure ─────────────────────────────────────
class A1M2_NotAnomaly(Scene):
    """One passed→shipped→harmed card tagged 'anomaly?'; two more stack; a bracket flips the tag to 'structure'."""
    BID = "A1M2"
    def construct(self):
        def seq_card(y):
            g = VGroup()
            words = ["passed", "shipped", "harmed"]
            xs = [-3.6, 0.0, 3.6]
            for w, x in zip(words, xs):
                chip = RoundedRectangle(width=2.9, height=0.9, corner_radius=0.14, fill_color=STAGE,
                                        fill_opacity=1, stroke_color=BORDER, stroke_width=2).move_to([x, y, 0])
                tx = Text(w, font_size=36, color=INK, weight=BOLD).move_to(chip)
                g.add(chip, tx)
            for x in [-1.8, 1.8]:
                g.add(Arrow([x - 0.35, y, 0], [x + 0.35, y, 0], color=SOFT, stroke_width=3, buff=0,
                            max_tip_length_to_length_ratio=0.5))
            return g
        tag = label("anomaly?", 40, SOFT).to_edge(UP, buff=0.7)
        c1 = seq_card(1.4)
        self.go(FadeIn(c1, shift=UP * 0.2), FadeIn(tag), rt=0.6)
        self.seek(0.30)
        c2 = seq_card(0.0); self.go(FadeIn(c2, shift=UP * 0.2), rt=0.45)
        self.seek(0.45)
        c3 = seq_card(-1.4); self.go(FadeIn(c3, shift=UP * 0.2), rt=0.45)
        self.seek(0.70)
        br = Brace(VGroup(c1, c2, c3), LEFT, color=SPARK, buff=0.35)
        newtag = Text("structure", font_size=44, color=SPARK, weight=BOLD).move_to(tag)
        self.go(GrowFromCenter(br), Transform(tag, newtag), rt=0.6)
        sub = label("what was always going to happen", 30, SOFT).to_edge(DOWN, buff=0.7)
        self.go(FadeIn(sub), rt=0.4)
        self.finish()


# ── A2M — symbols and referents ────────────────────────────────────────────
class A2M_SymbolsReferents(Scene):
    """SYMBOLS box (glyphs shuffle) · WORLD box (patient mark) · dashed arrow stops at a ring · the reader supplies the solid arrow · boxes slide apart on 'diverge'."""
    BID = "A2M"
    def construct(self):
        rng = random.Random(7)
        glyphs = "αβγδεζηθλμξπσφψω∆∑∫≈≠"
        sym_box = RoundedRectangle(width=4.2, height=3.8, corner_radius=0.2, fill_color=STAGE, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2.5).move_to([-3.8, 0.35, 0])
        sym_lbl = Text("SYMBOLS", font_size=36, color=SOFT, weight=BOLD).next_to(sym_box, UP, buff=0.2)
        gl = Text(" ".join(rng.choice(glyphs) for _ in range(5)), font_size=54, color=INK).move_to(sym_box)
        self.go(DrawBorderThenFill(sym_box), FadeIn(sym_lbl), FadeIn(gl), rt=0.6)
        self.seek(0.18)
        world_box = RoundedRectangle(width=4.2, height=3.8, corner_radius=0.2, fill_color=PAGE, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2.5).move_to([3.8, 0.35, 0])
        world_lbl = Text("WORLD", font_size=36, color=SOFT, weight=BOLD).next_to(world_box, UP, buff=0.2)
        patient = VGroup(Circle(radius=0.4, color=INK, stroke_width=3).shift(UP * 0.7),
                         Line(DOWN * 0.2, DOWN * 1.35, color=INK, stroke_width=3),
                         Line(DOWN * 0.2, DOWN * 0.2 + LEFT * 0.7 + DOWN * 0.65, color=INK, stroke_width=3),
                         Line(DOWN * 0.2, DOWN * 0.2 + RIGHT * 0.7 + DOWN * 0.65, color=INK, stroke_width=3))
        patient.move_to(world_box.get_center() + UP * 0.1)
        p_lbl = label("this patient", 30, SOFT).next_to(patient, DOWN, buff=0.15)
        self.go(DrawBorderThenFill(world_box), FadeIn(world_lbl), Create(patient), FadeIn(p_lbl), rt=0.6)
        # glyph shuffle x2
        for _ in range(2):
            gl2 = Text(" ".join(rng.choice(glyphs) for _ in range(5)), font_size=54, color=INK).move_to(sym_box)
            self.go(Transform(gl, gl2), rt=0.35)
        self.seek(0.32)
        ring = Circle(radius=0.62, color=INK, stroke_width=3).move_to([0.0, 0.35, 0])
        dashed = DashedLine(sym_box.get_right() + RIGHT * 0.1, ring.get_left(), color=INK, stroke_width=2.5,
                            dash_length=0.18)
        norep = label("no representation of the referents", 30, SOFT).move_to([0.0, -2.05, 0])
        self.go(Create(dashed), rt=0.5); self.go(Create(ring), FadeIn(norep), rt=0.4)
        self.seek(0.50)
        reader = VGroup(Circle(radius=0.22, color=SPARK, stroke_width=2.5, fill_color=SPARK, fill_opacity=1),
                        Line(DOWN * 0.22, DOWN * 0.8, color=SPARK, stroke_width=2.5)).move_to([0.0, 2.75, 0])
        r_lbl = Text("the reader", font_size=30, color=SPARK, weight=BOLD).next_to(reader, RIGHT, buff=0.2)
        solid = Arrow(reader.get_bottom() + DOWN * 0.05, world_box.get_top() + UP * 0.05 + LEFT * 0.8,
                      color=SPARK, stroke_width=4, buff=0)
        m_lbl = Text("meaning supplied here", font_size=32, color=SPARK, weight=BOLD).move_to([0.0, -2.8, 0])
        self.go(FadeIn(reader), FadeIn(r_lbl), rt=0.3)
        self.go(GrowArrow(solid), FadeIn(m_lbl), rt=0.5)
        self.seek(0.78)
        self.go(VGroup(sym_box, sym_lbl, gl).animate.shift(LEFT * 0.35),
                VGroup(world_box, world_lbl, patient, p_lbl).animate.shift(RIGHT * 0.35),
                FadeOut(dashed), FadeOut(ring), FadeOut(norep), rt=0.8)
        div = Text("diverge", font_size=40, color=SOFT).move_to([0.0, 0.35, 0])
        self.go(FadeIn(div), rt=0.3)
        self.finish()


# ── A2M2 — the data is always less than the world (equation tangent) ───────
class A2M2_DataWorld(Scene):
    """WORLD region · DATA sample inside · a deployment dot walks across the edge · the edge flashes terracotta · competence(DATA) ≠ competence(WORLD)."""
    BID = "A2M2"
    def construct(self):
        world = Ellipse(width=11.0, height=5.6, color=INK, stroke_width=2.5, fill_color=PAGE, fill_opacity=1)
        world.move_to([0, 0.15, 0])
        w_lbl = Text("WORLD", font_size=34, color=INK, weight=BOLD).move_to(world.get_top() + DOWN * 0.45)
        self.go(Create(world), FadeIn(w_lbl), rt=0.6)
        self.seek(0.20)
        data = Ellipse(width=6.2, height=3.2, color=INK, stroke_width=2.5, fill_color=STAGE, fill_opacity=1)
        data.move_to([-1.6, -0.2, 0])
        d_lbl = Text("DATA (the sample)", font_size=30, color=INK, weight=BOLD).move_to(data.get_center() + UP * 0.45)
        self.go(DrawBorderThenFill(data), FadeIn(d_lbl), rt=0.6)
        self.seek(0.40)
        comp = label("competence is over DATA", 28, SOFT).move_to(data.get_center() + DOWN * 0.2)
        self.go(FadeIn(comp), rt=0.4)
        self.seek(0.62)
        dot = Dot([-2.4, -0.9, 0], radius=0.14, color=INK)
        d_lbl2 = label("deployment", 26, SOFT).next_to(dot, DOWN, buff=0.15)
        self.go(FadeIn(dot), FadeIn(d_lbl2), rt=0.3)
        edge_pt = np.array([1.35, -0.6, 0])
        self.go(dot.animate.move_to(edge_pt), FadeOut(d_lbl2), rt=1.2)
        self.seek(0.85)
        edge = Ellipse(width=6.2, height=3.2, color=SPARK, stroke_width=5).move_to(data)
        b_lbl = Text("the boundary", font_size=30, color=SPARK, weight=BOLD).next_to(data, RIGHT, buff=0.5).shift(UP * 0.6)
        self.go(Create(edge), FadeIn(b_lbl), rt=0.5)
        self.go(dot.animate.move_to(edge_pt + RIGHT * 1.6), rt=0.6)
        eq = Text("competence(DATA)  ≠  competence(WORLD)", font_size=34, color=INK).to_edge(DOWN, buff=0.8)
        self.go(FadeIn(eq), rt=0.4)
        self.finish()


# ── A2M3 — six percent, at the boundary ────────────────────────────────────
class A2M3_SixPercent(Scene):
    """100 dots, 6 terracotta scattered; a boundary line draws; the six slide to the boundary on 'clustered'."""
    BID = "A2M3"
    def construct(self):
        rng = random.Random(94)
        idx = list(range(100)); rng.shuffle(idx); fail = set(idx[:6])
        dots = VGroup()
        x0, y0, step = -5.2, 2.45, 0.58
        for i in range(100):
            r, c = divmod(i, 10)
            col = SPARK if i in fail else INK
            d = Dot([x0 + c * step, y0 - r * step, 0], radius=0.15, color=col)
            dots.add(d)
        t = title("94 / 100", 44).move_to([2.6, 2.45, 0])
        self.go(FadeIn(t), rt=0.3)
        self.go(LaggedStart(*[FadeIn(d, scale=0.6) for d in dots], lag_ratio=0.01), rt=1.4)
        lbl = label("six failures — scattered?", 30, SOFT).move_to([-2.9, -3.15, 0])
        self.go(FadeIn(lbl), rt=0.3)
        self.seek(0.45)
        bx = x0 + 9 * step + 0.55
        bline = DashedLine([bx, y0 + 0.4, 0], [bx, y0 - 9 * step - 0.3, 0], color=INK, stroke_width=3, dash_length=0.2)
        b_lbl = label("where the data ran out", 28, INK).rotate(90 * DEGREES).next_to(bline, RIGHT, buff=0.2)
        self.go(Create(bline), FadeIn(b_lbl), rt=0.6)
        self.seek(0.70)
        fails = [dots[i] for i in sorted(fail)]
        targets = [np.array([bx - 0.3, y0 - 0.2 - k * step * 1.45, 0]) for k in range(6)]
        self.go(*[d.animate.move_to(tp) for d, tp in zip(fails, targets)], rt=1.0)
        new_lbl = Text("clustered at the boundary", font_size=32, color=SPARK, weight=BOLD).move_to([-2.9, -3.15, 0])
        self.go(Transform(lbl, new_lbl), rt=0.4)
        self.finish()


# ── A3M — both moves at once ───────────────────────────────────────────────
class A3M_BothMoves(Scene):
    """Axes: tests behavior × names the limits; two failure corners; the validator dot locks top-right."""
    BID = "A3M"
    def construct(self):
        ox, oy = -4.6, -2.4
        xax = Arrow([ox, oy, 0], [ox + 9.6, oy, 0], color=INK, stroke_width=3, buff=0)
        yax = Arrow([ox, oy, 0], [ox, oy + 5.4, 0], color=INK, stroke_width=3, buff=0)
        xl = label("tests behavior  →", 34, INK).next_to(xax, DOWN, buff=0.15).shift(RIGHT * 3.0)
        yl = label("names the limits  →", 34, INK).rotate(90 * DEGREES).next_to(yax, LEFT, buff=0.15).shift(UP * 1.1)
        self.go(Create(xax), Create(yax), FadeIn(xl), FadeIn(yl), rt=0.7)
        self.seek(0.25)
        dot = Dot([ox + 8.4, oy + 0.6, 0], radius=0.17, color=INK)
        d1 = label("behavior is evidence", 32, SOFT).next_to(dot, UP, buff=0.15)
        self.go(FadeIn(dot), FadeIn(d1), rt=0.4)
        self.seek(0.45)
        top = np.array([ox + 8.4, oy + 4.6, 0])
        self.go(dot.animate.move_to(top), FadeOut(d1), rt=0.8)
        self.seek(0.60)
        c1 = label("only tests → misses the limits", 32, SOFT).move_to([ox + 6.2, oy + 0.75, 0])
        c2 = label("only invokes limits → skips the testing", 32, SOFT).move_to([ox + 3.2, oy + 4.8, 0])
        self.go(FadeIn(c1), FadeIn(c2), rt=0.5)
        self.seek(0.85)
        ring = Circle(radius=0.45, color=SPARK, stroke_width=4).move_to(top)
        both = Text("both moves at once", font_size=34, color=SPARK, weight=BOLD).next_to(ring, DOWN, buff=0.25).shift(LEFT * 1.3)
        self.go(Create(ring), FadeIn(both), rt=0.5)
        self.finish()


# ── A4M — the exposure spectrum ────────────────────────────────────────────
class A4M_ExposureSpectrum(Scene):
    """Exposure axis; left marker (product line, thin gap bar); right markers per spoken item; the gap bar swells; two labels."""
    BID = "A4M"
    def construct(self):
        ax = Line([-5.8, -0.6, 0], [5.8, -0.6, 0], color=INK, stroke_width=3)
        axl = label("exposure to the limits  →", 36, SOFT).next_to(ax, DOWN, buff=0.2).shift(RIGHT * 3.4)
        self.go(Create(ax), FadeIn(axl), rt=0.5)
        lm = Dot([-4.5, -0.6, 0], radius=0.14, color=INK)
        l_lbl = label("product images\non a line", 36, INK).next_to(lm, UP, buff=0.25)
        gap = Rectangle(width=0.5, height=0.35, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-4.5, 1.75, 0])
        g_lbl = label("data–world gap", 36, SOFT).next_to(gap, UP, buff=0.12)
        self.go(FadeIn(lm), FadeIn(l_lbl), FadeIn(gap), FadeIn(g_lbl), rt=0.5)
        self.seek(0.35)
        m1 = label("skepticism = methodology", 36, INK).move_to([-3.2, -2.3, 0])
        self.go(FadeIn(m1), rt=0.4)
        self.seek(0.50)
        items = ["clinical", "vehicle", "judicial", "agentic"]
        xs = [1.4, 2.8, 4.2, 5.6]
        for it, x in zip(items, xs):
            d = Dot([x, -0.6, 0], radius=0.14, color=INK)
            l = label(it, 36, INK).next_to(d, UP, buff=0.25)
            self.go(FadeIn(d), FadeIn(l), rt=0.3)
        self.seek(0.72)
        big = Rectangle(width=4.8, height=0.35, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([3.5, 1.75, 0])
        self.go(Transform(gap, big), g_lbl.animate.next_to(big, UP, buff=0.12), rt=0.9)
        self.seek(0.88)
        m2 = Text("skepticism = the safety mechanism", font_size=36, color=SPARK, weight=BOLD).move_to([2.3, -2.3, 0])
        self.go(FadeIn(m2), rt=0.4)
        self.finish()


# ── A5M — the limit case ───────────────────────────────────────────────────
class A5M_LimitCase(Scene):
    """A stakes gauge fills; a dashed threshold 'refusal becomes binding'; three markers on their words; the gauge crosses in terracotta."""
    BID = "A5M"
    def construct(self):
        frame = Rectangle(width=1.6, height=5.6, color=INK, stroke_width=2.5).move_to([-4.6, 0.1, 0])
        f_lbl = label("stakes", 30, INK).next_to(frame, DOWN, buff=0.2)
        fill = Rectangle(width=1.6, height=0.05, fill_color=INK, fill_opacity=1, stroke_width=0)
        fill.move_to(frame.get_bottom() + UP * 0.025)
        self.go(Create(frame), FadeIn(f_lbl), FadeIn(fill), rt=0.5)
        thr_y = frame.get_bottom()[1] + 3.4
        thr = DashedLine([-5.7, thr_y, 0], [5.9, thr_y, 0], color=INK, stroke_width=2.5, dash_length=0.2)
        t_lbl = label("obligation to refuse becomes binding", 30, INK).next_to(thr, DOWN, buff=0.18).shift(RIGHT * 1.6)
        self.go(Create(thr), FadeIn(t_lbl), rt=0.5)
        self.seek(0.30)
        def fill_to(h, rt):
            new = Rectangle(width=1.6, height=h, fill_color=INK, fill_opacity=1, stroke_width=0)
            new.move_to(frame.get_bottom() + UP * h / 2)
            self.go(Transform(fill, new), rt=rt)
        fill_to(2.4, 0.9)
        marks = [("three patients harmed", 0.45, 3.9), ("an unjust sentence", 0.60, 4.5), ("a life", 0.72, 5.1)]
        for s, a, h in marks:
            self.seek(a)
            y = frame.get_bottom()[1] + h
            mk = Dot([-2.9, y, 0], radius=0.12, color=INK)
            ml = label(s, 30, INK).next_to(mk, RIGHT, buff=0.2)
            self.go(FadeIn(mk), FadeIn(ml), rt=0.3)
        self.seek(0.88)
        new = Rectangle(width=1.6, height=5.35, fill_color=SPARK, fill_opacity=1, stroke_width=0)
        new.move_to(frame.get_bottom() + UP * 5.35 / 2)
        ov = Text("override: fictional", font_size=32, color=SPARK, weight=BOLD).move_to([2.2, -2.5, 0])
        self.go(Transform(fill, new), FadeIn(ov), rt=0.7)
        self.finish()


# ── A6M — the calibration gap (shape only) ─────────────────────────────────
class A6M_CalibrationGap(Scene):
    """Reliability diagram: dashed diagonal; marker at stated 0.9 drops to a band well below; terracotta gap bracket. No fabricated numbers on the band."""
    BID = "A6M"
    def construct(self):
        ox, oy, L = -5.4, -2.65, 5.7
        xax = Arrow([ox, oy, 0], [ox + L + 0.6, oy, 0], color=INK, stroke_width=3, buff=0)
        yax = Arrow([ox, oy, 0], [ox, oy + L + 0.6, 0], color=INK, stroke_width=3, buff=0)
        xl = label("stated confidence  →", 32, INK).next_to(xax, DOWN, buff=0.12).shift(RIGHT * 1.6)
        yl = label("actual hit rate  →", 32, INK).rotate(90 * DEGREES).next_to(yax, LEFT, buff=0.12).shift(UP * 1.0)
        diag = DashedLine([ox, oy, 0], [ox + L, oy + L, 0], color=GHOST, stroke_width=2.5, dash_length=0.2)
        dl = label("perfectly calibrated", 28, GHOST).move_to([ox + L + 1.7, oy + L - 0.2, 0])
        self.go(Create(xax), Create(yax), FadeIn(xl), FadeIn(yl), rt=0.5)
        self.go(Create(diag), FadeIn(dl), rt=0.5)
        self.seek(0.25)
        px = ox + 0.9 * L
        m = Dot([px, oy + 0.9 * L, 0], radius=0.16, color=INK)
        ml = label("stated: 90%", 32, INK).next_to(m, RIGHT, buff=0.3).shift(DOWN * 0.35)
        tick = Line([px, oy - 0.1, 0], [px, oy + 0.1, 0], color=INK, stroke_width=3)
        self.go(FadeIn(m), FadeIn(ml), Create(tick), rt=0.4)
        self.seek(0.40)
        band = Rectangle(width=0.8, height=1.0, fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2)
        band.move_to([px, oy + 0.58 * L, 0])
        bl = label("well below", 32, INK).next_to(band, RIGHT, buff=0.25)
        self.go(FadeIn(band), FadeIn(bl), m.animate.move_to([px, oy + 0.6 * L, 0]), FadeOut(ml), rt=0.9)
        self.seek(0.65)
        nb = label("nobody runs the experiment on them", 32, SOFT).move_to([3.0, -1.6, 0])
        self.go(FadeIn(nb), rt=0.4)
        self.seek(0.85)
        br = Brace(Line([px + 0.5, oy + 0.6 * L, 0], [px + 0.5, oy + 0.9 * L, 0]), RIGHT, color=SPARK, buff=0.1)
        gl = Text("the gap", font_size=40, color=SPARK, weight=BOLD).next_to(br, RIGHT, buff=0.25)
        ghost = Dot([px, oy + 0.9 * L, 0], radius=0.16, color=GHOST)
        self.go(FadeIn(ghost), GrowFromCenter(br), FadeIn(gl), rt=0.5)
        self.finish()


# ── A6M2 — the structure of the next failure ───────────────────────────────
class A6M2_NextFailure(Scene):
    """The Act I sequence as a template with blanks; each fills on its clause; a terracotta STOP halts the chain."""
    BID = "A6M2"
    def construct(self):
        ys = [2.0, 0.5, -1.0]
        fills = ["cleared every review", "a context the data didn't reach", "a question never scoped"]
        blanks = []
        for y in ys:
            box = RoundedRectangle(width=8.4, height=1.15, corner_radius=0.14, fill_color=STAGE, fill_opacity=1,
                                   stroke_color=BORDER, stroke_width=2).move_to([-1.9, y, 0])
            b = Text("[            ]", font_size=40, color=GHOST).move_to(box)
            blanks.append((box, b))
        t = label("the structure of the next failure", 40, SOFT).to_edge(UP, buff=0.7)
        harm_box = RoundedRectangle(width=8.4, height=1.15, corner_radius=0.14, fill_color=PAGE, fill_opacity=1,
                                    stroke_color=GHOST, stroke_width=2).move_to([-1.9, -2.55, 0])
        harm = Text("harm", font_size=40, color=GHOST).move_to(harm_box)
        arrows = [Arrow([-1.9, ys[i] - 0.58, 0], [-1.9, ys[i + 1] + 0.58, 0], color=SOFT, stroke_width=3, buff=0.05)
                  for i in range(2)]
        a3 = Arrow([-1.9, ys[2] - 0.58, 0], [-1.9, -2.55 + 0.58, 0], color=GHOST, stroke_width=3, buff=0.05)
        self.go(FadeIn(t), *[FadeIn(bx) for bx, _ in blanks], *[FadeIn(b) for _, b in blanks],
                FadeIn(harm_box), FadeIn(harm), *[Create(a) for a in arrows], Create(a3), rt=0.6)
        for (box, b), s_, a in zip(blanks, fills, [0.30, 0.45, 0.58]):
            self.seek(a)
            nt = Text(s_, font_size=40, color=INK, weight=BOLD).move_to(box)
            self.go(Transform(b, nt), rt=0.4)
        self.seek(0.75)
        halt = Line([-2.8, -1.78, 0], [-1.0, -1.78, 0], color=SPARK, stroke_width=9)
        stop = VGroup(RegularPolygon(n=8, radius=0.95, color=SPARK, fill_color=SPARK, fill_opacity=1, stroke_width=0),
                      Text("STOP", font_size=36, color=PAGE, weight=BOLD)).move_to([4.15, -0.1, 0])
        self.go(Create(halt), FadeIn(stop, scale=1.5), rt=0.4)
        self.seek(0.90)
        who = VGroup(Text("recognizes · has authority", font_size=28, color=SPARK, weight=BOLD),
                     Text("· uses both", font_size=28, color=SPARK, weight=BOLD)).arrange(DOWN, buff=0.15).move_to([4.15, -1.9, 0])
        self.go(FadeIn(who), rt=0.4)
        self.finish()
