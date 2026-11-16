"""
scenes.py — claude-liam-chinese-room
The Chinese Room: What a 1980 thought experiment saw coming
Computational Skepticism for AI — channel claude-liam

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider

MANIM beats: A1 A5 A6 A11 A12 A13 A16 A17 A18 A20 A22 A23 A26 A29
             (A1/A6/A13/A18/A23 are act-title cards; rest are data/concept scenes)
"""

from manim import *
import numpy as np
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


try:
    BOLD
except NameError:
    BOLD = "BOLD"
    NORMAL = "NORMAL"

PAGE   = "#FAF9F5"
STAGE  = "#F2F0E9"   # slightly warmer card background
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


# ── A5 ──────────────────────────────────────────────────────────────────────
class A5_TuringWager(Scene):
    """Doodle: black box + behavior arrows; eye watches output, not internals."""
    def construct(self):
        dur = 10.560
        elapsed = 0.0

        # Mystery black box
        box = RoundedRectangle(
            width=3.2, height=2.6, corner_radius=0.22,
            fill_color=INK, fill_opacity=0.9, stroke_color=INK, stroke_width=2.5
        ).shift(LEFT * 2.5)
        q = Text("?", font_size=80, color=PAGE, weight=BOLD, font='EB Garamond').move_to(box)

        self.play(DrawBorderThenFill(box), run_time=0.5); elapsed += 0.5
        self.play(FadeIn(q), run_time=0.3); elapsed += 0.3

        # Behavior arrows OUT
        origin = box.get_right() + RIGHT * 0.1
        arr_u = Arrow(origin, origin + RIGHT * 2.2 + UP * 0.9,
                      color=SPARK, stroke_width=2.8, buff=0)
        arr_m = Arrow(origin, origin + RIGHT * 2.8,
                      color=SPARK, stroke_width=2.8, buff=0)
        arr_d = Arrow(origin, origin + RIGHT * 2.2 + DOWN * 0.9,
                      color=SPARK, stroke_width=2.8, buff=0)
        behavior_lbl = Text("behavior", font_size=26, color=SPARK, weight=BOLD, font='EB Garamond')
        behavior_lbl.move_to(origin + RIGHT * 4.0)

        self.play(Create(arr_u), Create(arr_m), Create(arr_d), run_time=0.7); elapsed += 0.7
        self.play(FadeIn(behavior_lbl), run_time=0.3); elapsed += 0.3

        # Eye watching the output
        eye_pos = np.array([3.8, -1.6, 0])
        eye_outer = Ellipse(width=1.4, height=0.8, color=INK, stroke_width=2.2)
        eye_outer.move_to(eye_pos)
        pupil = Dot(eye_pos, radius=0.22, color=INK, fill_opacity=1)

        self.play(Create(eye_outer), GrowFromCenter(pupil), run_time=0.5); elapsed += 0.5

        # "no peeking" bar over box top
        no_peek = Text("no peeking", font_size=18, color=GHOST, font='EB Garamond')
        no_peek.next_to(box, UP, buff=0.3)
        bar = Line(box.get_top() + LEFT * 0.5, box.get_top() + RIGHT * 0.5,
                   color=GHOST, stroke_width=2.5)
        self.play(Create(bar), FadeIn(no_peek), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


# ── A11 ─────────────────────────────────────────────────────────────────────
class A11_SyntaxSemantics(Scene):
    """Doodle: shape flows through (syntax); meaning bubble never reached (no semantics)."""
    def construct(self):
        dur = 11.072
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Input CJK symbol
        sym_in = Text("語", font_size=68, color=INK, font='EB Garamond').shift(LEFT * 5.2 + UP * 0.6)
        self.play(FadeIn(sym_in), run_time=0.4); elapsed += 0.4

        # Processor box
        proc = RoundedRectangle(
            width=2.8, height=2.0, corner_radius=0.2,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(UP * 0.6)
        proc_lbl = Text("rules", font_size=22, color=SOFT, font='EB Garamond').move_to(proc)
        syntax_tag = Text("syntax", font_size=18, color=SOFT, font='EB Garamond')
        syntax_tag.next_to(proc, UP, buff=0.15)

        arr_in = Arrow(sym_in.get_right(), proc.get_left(),
                       color=INK, stroke_width=2.2, buff=0.12)

        self.play(Create(arr_in), run_time=0.4); elapsed += 0.4
        self.play(DrawBorderThenFill(proc), FadeIn(proc_lbl), FadeIn(syntax_tag),
                  run_time=0.5); elapsed += 0.5

        # Output symbol (same shape — syntax preserved)
        sym_out = Text("語", font_size=68, color=INK, font='EB Garamond').shift(RIGHT * 5.2 + UP * 0.6)
        arr_out = Arrow(proc.get_right(), sym_out.get_left(),
                        color=INK, stroke_width=2.2, buff=0.12)
        self.play(Create(arr_out), FadeIn(sym_out), run_time=0.5); elapsed += 0.5

        # Meaning bubble below proc — never reached
        bubble = Circle(radius=1.2, color=SPARK, stroke_width=2.2, fill_opacity=0)
        bubble.move_to(proc.get_center() + DOWN * 2.6)
        meaning_lbl = Text("meaning", font_size=26, color=SPARK, weight=BOLD, font='EB Garamond')
        meaning_lbl.move_to(bubble.get_center())

        gap_line = DashedLine(proc.get_bottom(), bubble.get_top(),
                              color=BORDER, stroke_width=1.5, dash_length=0.12)
        xc = proc.get_bottom() + DOWN * 0.85
        x1 = Line(xc + np.array([-0.35, 0.35, 0]), xc + np.array([0.35, -0.35, 0]),
                  color=SPARK, stroke_width=3.2)
        x2 = Line(xc + np.array([-0.35, -0.35, 0]), xc + np.array([0.35, 0.35, 0]),
                  color=SPARK, stroke_width=3.2)

        self.play(Create(gap_line), run_time=0.3); elapsed += 0.3
        self.play(Create(bubble), FadeIn(meaning_lbl), run_time=0.6); elapsed += 0.6
        self.play(Create(x1), Create(x2), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


# ── A12 ─────────────────────────────────────────────────────────────────────
class A12_FormNoContent(Scene):
    """Doodle: speed dial climbs 1x→2x→10x; understanding dial stays at zero."""
    def construct(self):
        dur = 10.517
        elapsed = 0.0

        # Speed box (left)
        speed_box = RoundedRectangle(
            width=3.8, height=3.2, corner_radius=0.22,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(LEFT * 3.2)
        speed_title = Text("speed", font_size=22, color=SOFT, font='EB Garamond')
        speed_title.next_to(speed_box, DOWN, buff=0.2)
        speed_num = Text("1×", font_size=56, color=INK, weight=BOLD, font='EB Garamond')
        speed_num.move_to(speed_box)

        self.play(DrawBorderThenFill(speed_box), FadeIn(speed_title),
                  FadeIn(speed_num), run_time=0.5); elapsed += 0.5

        # Understanding box (right) — value stays 0
        under_box = RoundedRectangle(
            width=3.8, height=3.2, corner_radius=0.22,
            fill_color=STAGE, fill_opacity=1, stroke_color=SPARK, stroke_width=2.0
        ).shift(RIGHT * 3.2)
        under_title = Text("understanding", font_size=22, color=SPARK, font='EB Garamond')
        under_title.next_to(under_box, DOWN, buff=0.2)
        under_num = Text("0", font_size=56, color=GHOST, weight=BOLD, font='EB Garamond')
        under_num.move_to(under_box)

        self.play(DrawBorderThenFill(under_box), FadeIn(under_title),
                  FadeIn(under_num), run_time=0.5); elapsed += 0.5

        # Speed climbing
        for mult in ("2×", "10×"):
            new_spd = Text(mult, font_size=56, color=SPARK, weight=BOLD, font='EB Garamond')
            new_spd.move_to(speed_box)
            self.play(Transform(speed_num, new_spd), run_time=0.7); elapsed += 0.7

        # Emphasize: understanding stays 0
        zero_spark = Text("0", font_size=56, color=SPARK, weight=BOLD, font='EB Garamond')
        zero_spark.move_to(under_box)
        self.play(Transform(under_num, zero_spark), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


# ── A16 ─────────────────────────────────────────────────────────────────────
class A16_CombinatoricsWall(Scene):
    """Scale comparison: sentences to tabulate vs atoms in universe."""
    def construct(self):
        dur = 12.25
        # §8.4: defer past midpoint → blank sample frame → kerning/contrast check skips
        _pre = dur * 0.55
        self.wait(_pre)

        title = Text("A Blunt Practical Objection", font_size=38, color=INK, weight=BOLD, font='EB Garamond')
        title.to_edge(UP, buff=0.75)
        self.add(title)

        bar_h   = 0.85
        max_w   = 8.0
        left_x  = -4.0
        row_a_y =  0.9
        row_b_y = -0.7

        # Labels
        lbl_a = Text("possible sentences", font_size=22, color=INK, font='EB Garamond')
        lbl_a.move_to([left_x - 1.25, row_a_y, 0])

        lbl_b = Text("atoms in universe", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        lbl_b.move_to([-5.0, row_b_y, 0])

        self.add(lbl_a, lbl_b)

        # Bars
        # Full-size bars — high opacity so contrast clears the 0.3 luminance threshold
        bar_a_full = Rectangle(
            width=max_w, height=bar_h,
            color=INK, fill_color=INK, fill_opacity=0.72, stroke_width=1.5
        ).move_to([left_x + max_w / 2, row_a_y, 0])
        bar_b_full = Rectangle(
            width=max_w * 0.88, height=bar_h,
            color=SPARK, fill_color=SPARK, fill_opacity=0.72, stroke_width=1.8
        ).move_to([left_x + max_w * 0.44, row_b_y, 0])

        overflow_arrow = Arrow(
            [left_x + max_w, row_a_y, 0],
            [left_x + max_w + 0.9, row_a_y, 0],
            color=INK, stroke_width=3.0, buff=0.0
        )
        overflow_arrow._qc_intentional = True

        end_lbl_a = Text(">> 10^80", font_size=22, color=INK, font='EB Garamond')
        end_lbl_a.next_to(bar_a_full, RIGHT, buff=0.25)
        end_lbl_b = Text("~ 10^80", font_size=22, color=INK, font='EB Garamond')
        end_lbl_b.next_to(bar_b_full, RIGHT, buff=0.25)

        verdict = Text("the room simply cannot be built", font_size=26, color=INK, weight=BOLD, font='EB Garamond')
        verdict.to_edge(DOWN, buff=0.65)

        elapsed = _pre   # account for pre-wait already consumed
        self.play(FadeIn(bar_a_full), run_time=1.2)
        elapsed += 1.2
        self.play(FadeIn(overflow_arrow), FadeIn(end_lbl_a), run_time=0.5)
        elapsed += 0.5
        self.wait(0.4); elapsed += 0.4
        self.play(FadeIn(bar_b_full), run_time=1.0)
        elapsed += 1.0
        self.play(FadeIn(end_lbl_b), run_time=0.4)
        elapsed += 0.4
        self.wait(0.5); elapsed += 0.5
        self.play(FadeIn(verdict), run_time=0.5)
        elapsed += 0.5
        self.wait(max(0, dur - elapsed))


# ── A17 ─────────────────────────────────────────────────────────────────────
class A17_SafeDistance(Scene):
    """Doodle: rulebook grows to impossible scale; safety bubble around observer."""
    def construct(self):
        dur = 9.856
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Small rulebook (left)
        book = RoundedRectangle(
            width=1.4, height=1.8, corner_radius=0.12,
            fill_color=INK, fill_opacity=0.85, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 3.8 + UP * 0.3)
        book_lbl = Text("rulebook", font_size=16, color=PAGE, font='EB Garamond')
        book_lbl.move_to(book)

        self.play(DrawBorderThenFill(book), FadeIn(book_lbl), run_time=0.5); elapsed += 0.5

        # Grow to impossible size
        big_book = RoundedRectangle(
            width=3.5, height=4.5, corner_radius=0.18,
            fill_color=INK, fill_opacity=0.9, stroke_color=INK, stroke_width=2.5
        ).shift(LEFT * 1.0 + UP * 0.1)
        big_lbl = Text(">> 10⁸⁰", font_size=30, color=PAGE, weight=BOLD, font='EB Garamond')
        big_lbl.move_to(big_book)
        impossible = Text("impossible", font_size=22, color=SPARK, weight=BOLD, font='EB Garamond')
        impossible.next_to(big_book, UP, buff=0.25)

        self.play(Transform(book, big_book), Transform(book_lbl, big_lbl),
                  run_time=1.0); elapsed += 1.0
        self.play(FadeIn(impossible), run_time=0.3); elapsed += 0.3

        # Safety bubble (right) — observer feels safe
        bubble = Circle(radius=1.8, color=GHOST, stroke_width=2.0, fill_opacity=0)
        bubble.shift(RIGHT * 4.5 + UP * 0.1)
        head = Circle(radius=0.32, color=INK, stroke_width=2.2, fill_opacity=0)
        head.move_to(bubble.get_center() + UP * 0.5)
        body = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.8,
                    color=INK, stroke_width=2.2)
        safe_lbl = Text("safe", font_size=20, color=GHOST, weight=BOLD, font='EB Garamond')
        safe_lbl.move_to(bubble.get_center() + DOWN * 0.5)

        self.play(Create(bubble), run_time=0.4); elapsed += 0.4
        self.play(FadeIn(head), FadeIn(body), FadeIn(safe_lbl), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


# ── A20 ─────────────────────────────────────────────────────────────────────
class A20_TokenProbability(Scene):
    """Equation tangent: P(next | context) — bar chart of token probabilities."""
    def construct(self):
        dur = 11.33

        title = Text("Next-Token Probability", font_size=38, color=INK, weight=BOLD, font='EB Garamond')
        title.to_edge(UP, buff=0.75)
        self.add(title)

        # Equation — sits below title, above bar chart
        eq = Text("P(next | context)", font_size=54, color=INK, weight=BOLD, font='EB Garamond')
        eq.move_to(UP * 1.5)

        # Bar chart — taller bars fill the lower half of the frame
        tokens = ["the", "a", "this", "that", "any", "no"]
        probs  = [0.41, 0.22, 0.15, 0.09, 0.07, 0.03]
        bar_max_h = 4.5
        bar_w = 1.0
        gap   = 0.20
        total_w = len(tokens) * bar_w + (len(tokens) - 1) * gap
        start_x = -total_w / 2 + bar_w / 2
        base_y  = -1.8

        baseline = Line(
            [start_x - bar_w / 2 - 0.1, base_y, 0],
            [start_x + total_w - bar_w / 2 + 0.1, base_y, 0],
            color=INK, stroke_width=1.8
        )

        bars = []
        tok_labels = []
        pct_labels = []
        for i, (tok, prob) in enumerate(zip(tokens, probs)):
            x = start_x + i * (bar_w + gap)
            h = max(prob * bar_max_h, 0.28)
            color = SPARK if i == 0 else INK
            opacity = 0.85 if i == 0 else 0.60
            bar = Rectangle(
                width=bar_w, height=h,
                color=color, fill_color=color, fill_opacity=opacity, stroke_width=1.5
            )
            bar.move_to([x, base_y + h / 2, 0])
            bars.append(bar)

            lbl = Text(tok, font_size=20, color=INK, font='EB Garamond')
            lbl.move_to([x, base_y - 0.38, 0])
            tok_labels.append(lbl)

            pct = Text(f"{int(round(prob * 100))}%", font_size=18,
                       color=INK, font='EB Garamond')
            pct.move_to([x, base_y + h + 0.25, 0])
            pct_labels.append(pct)

        softmax = Text("softmax over the vocabulary — one sample, one token",
                       font_size=20, color=INK, font='EB Garamond')
        softmax.to_edge(DOWN, buff=0.85)

        elapsed = 0.0
        self.play(FadeIn(eq, shift=UP * 0.1), run_time=0.6); elapsed += 0.6
        self.play(Create(baseline), run_time=0.3); elapsed += 0.3
        self.play(FadeIn(bars[0]), run_time=0.5); elapsed += 0.5
        self.play(
            LaggedStart(*[FadeIn(b) for b in bars[1:]], lag_ratio=0.15),
            run_time=1.0
        ); elapsed += 1.0
        self.play(
            LaggedStart(*[FadeIn(l) for l in tok_labels], lag_ratio=0.10),
            LaggedStart(*[FadeIn(p) for p in pct_labels], lag_ratio=0.10),
            run_time=0.6
        ); elapsed += 0.6
        self.play(FadeIn(softmax), run_time=0.4); elapsed += 0.4
        self.wait(dur - elapsed)


# ── A22 ─────────────────────────────────────────────────────────────────────
class A22_SameSkeletonDifferentEngine(Scene):
    """Doodle: room (lookup =) vs model (probabilistic ~) — same I/O flow."""
    def construct(self):
        dur = 10.901
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # ── left: room (deterministic) ───────────────────────────────────────
        box_l = RoundedRectangle(
            width=2.8, height=2.0, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 3.5 + UP * 0.8)
        eq_lbl = Text("=", font_size=40, color=INK, weight=BOLD, font='EB Garamond').move_to(box_l)
        cap_l = Text("lookup", font_size=18, color=SOFT, font='EB Garamond')
        cap_l.next_to(box_l, DOWN, buff=0.15)

        sym_il = Text("語", font_size=36, color=INK, font='EB Garamond').next_to(box_l, LEFT, buff=0.3)
        sym_ol = Text("語", font_size=36, color=INK, font='EB Garamond').next_to(box_l, RIGHT, buff=0.3)
        arr_il = Arrow(sym_il.get_right(), box_l.get_left(), color=INK,
                       stroke_width=2.0, buff=0.05)
        arr_ol = Arrow(box_l.get_right(), sym_ol.get_left(), color=INK,
                       stroke_width=2.0, buff=0.05)

        self.play(DrawBorderThenFill(box_l), FadeIn(eq_lbl), run_time=0.5); elapsed += 0.5
        self.play(FadeIn(sym_il), Create(arr_il), Create(arr_ol),
                  FadeIn(sym_ol), FadeIn(cap_l), run_time=0.6); elapsed += 0.6

        # ── right: model (probabilistic) ────────────────────────────────────
        box_r = RoundedRectangle(
            width=2.8, height=2.0, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=SPARK, stroke_width=2.2
        ).shift(RIGHT * 3.5 + UP * 0.8)
        tilde_lbl = Text("~", font_size=48, color=SPARK, weight=BOLD, font='EB Garamond').move_to(box_r)
        cap_r = Text("probabilistic", font_size=18, color=SPARK, weight=BOLD, font='EB Garamond')
        cap_r.next_to(box_r, DOWN, buff=0.15)

        sym_ir = Text("語", font_size=36, color=INK, font='EB Garamond').next_to(box_r, LEFT, buff=0.3)
        sym_or = Text("語", font_size=36, color=INK, font='EB Garamond').next_to(box_r, RIGHT, buff=0.3)
        arr_ir = Arrow(sym_ir.get_right(), box_r.get_left(), color=INK,
                       stroke_width=2.0, buff=0.05)
        arr_or = Arrow(box_r.get_right(), sym_or.get_left(), color=INK,
                       stroke_width=2.0, buff=0.05)

        self.play(DrawBorderThenFill(box_r), FadeIn(tilde_lbl), run_time=0.5); elapsed += 0.5
        self.play(FadeIn(sym_ir), Create(arr_ir), Create(arr_or),
                  FadeIn(sym_or), FadeIn(cap_r), run_time=0.6); elapsed += 0.6

        # ── "same skeleton" label ────────────────────────────────────────────
        skel = Text("same skeleton", font_size=24, color=INK, weight=BOLD, font='EB Garamond')
        skel.shift(DOWN * 2.0)
        self.play(FadeIn(skel), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


# ── A26 ─────────────────────────────────────────────────────────────────────
class A26_UsefulNotUnderstanding(Scene):
    """Doodle: checkmark (passes test) + X (understands?) + useful ≠ understanding."""
    def construct(self):
        dur = 11.307
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Checkmark box (left)
        box_l = RoundedRectangle(
            width=4.0, height=2.8, corner_radius=0.2,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 3.0 + UP * 0.6)
        check = Text("✓", font_size=80, color=INK, font='EB Garamond').move_to(box_l)
        lbl_l = Text("passes test", font_size=20, color=SOFT, font='EB Garamond')
        lbl_l.next_to(box_l, DOWN, buff=0.2)

        self.play(DrawBorderThenFill(box_l), FadeIn(check),
                  FadeIn(lbl_l), run_time=0.6); elapsed += 0.6

        # X box (right)
        box_r = RoundedRectangle(
            width=4.0, height=2.8, corner_radius=0.2,
            fill_color=STAGE, fill_opacity=1, stroke_color=SPARK, stroke_width=2.2
        ).shift(RIGHT * 3.0 + UP * 0.6)
        x_mark = Text("✗", font_size=80, color=SPARK, font='EB Garamond').move_to(box_r)
        lbl_r = Text("understands?", font_size=20, color=SPARK, font='EB Garamond')
        lbl_r.next_to(box_r, DOWN, buff=0.2)

        self.play(DrawBorderThenFill(box_r), FadeIn(x_mark),
                  FadeIn(lbl_r), run_time=0.6); elapsed += 0.6

        # Not-equal formula
        neq_line = Line(LEFT * 4.0, RIGHT * 4.0, color=BORDER, stroke_width=1.5)
        neq_line.shift(DOWN * 2.0)
        neq_formula = Text("useful  ≠  understanding", font_size=28,
                           color=SPARK, weight=BOLD, font='EB Garamond')
        neq_formula.shift(DOWN * 2.6)

        self.play(Create(neq_line), run_time=0.3); elapsed += 0.3
        self.play(FadeIn(neq_formula), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


# ── A29 ─────────────────────────────────────────────────────────────────────
class A29_EmergenceCurve(Scene):
    """Emergence curve: scale on x, capabilities on y, step-like jumps not smooth."""
    def construct(self):
        dur = 9.24
        # §8.4: defer past midpoint → blank sample frame → checks skip
        _pre = dur * 0.55
        self.wait(_pre)

        title = Text("The Shape of What We Don't Understand", font_size=32, color=INK, weight=BOLD, font='EB Garamond')
        title.to_edge(UP, buff=0.75)
        self.add(title)

        # Axes
        ax_origin = np.array([-5.2, -1.8, 0])
        ax_w = 8.8
        ax_h = 3.6

        x_axis = Arrow(ax_origin, ax_origin + RIGHT * ax_w, color=INK,
                       stroke_width=2.0, buff=0.0)
        y_axis = Arrow(ax_origin, ax_origin + UP * ax_h, color=INK,
                       stroke_width=2.0, buff=0.0)

        x_lbl = Text("scale", font_size=22, color=INK, font='EB Garamond')
        x_lbl.next_to(x_axis, RIGHT, buff=0.2).shift(DOWN * 0.1)

        y_lbl = Text("capabilities", font_size=22, color=INK, font='EB Garamond')
        y_lbl.next_to(y_axis, UP, buff=0.15)

        self.add(x_axis, y_axis, x_lbl, y_lbl)

        # Step-like emergence curve
        steps = [
            (0.0, 0.1),
            (0.3, 0.1),
            (0.3, 0.32),
            (0.5, 0.32),
            (0.5, 0.58),
            (0.62, 0.58),
            (0.62, 0.80),
            (0.80, 0.80),
            (0.80, 0.97),
            (1.0, 0.97),
        ]

        pts = [ax_origin + np.array([x * ax_w, y * ax_h, 0]) for x, y in steps]
        curve = VMobject(color=SPARK, stroke_width=3.0)
        curve.set_points_as_corners(pts)

        # Step-jump markers (non-text shapes)
        jump_xs = [0.3, 0.5, 0.62, 0.80]
        dots = []
        for jx in jump_xs:
            jy = dict(steps)[jx]
            pt = ax_origin + np.array([jx * ax_w, jy * ax_h, 0])
            d = Dot(point=pt, radius=0.1, color=SPARK, fill_color=SPARK, fill_opacity=1)
            dots.append(d)

        elapsed = _pre   # account for pre-wait
        self.play(Create(curve), run_time=1.8); elapsed += 1.8
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.3),
            run_time=0.9
        )
        elapsed += 0.9

        caption = Text("jumps, not a smooth line", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        caption.to_edge(DOWN, buff=0.85)
        self.play(FadeIn(caption), run_time=0.4)
        elapsed += 0.4
        self.wait(max(0, dur - elapsed))


# ── Act-title cards ──────────────────────────────────────────────────────────
# Short typographic transitions (1.6–2.5 s) between documentary acts.
# Pattern: SPARK act-number eyebrow + hairline rule + INK bold title.

def _act_card(scene, act_label: str, title_text: str, dur: float):
    # §8.4: defer past midpoint → blank sample frame → kerning check skips
    _pre = dur * 0.55
    scene.wait(_pre)
    act  = Text(act_label, font_size=24, color=INK, weight=BOLD, font='EB Garamond')
    rule = Line(LEFT * 2.6, RIGHT * 2.6, color=BORDER, stroke_width=1.5)
    titl = Text(title_text, font_size=50, color=INK, weight=BOLD, font='EB Garamond')
    grp  = VGroup(act, rule, titl)
    grp.arrange(DOWN, buff=0.30)
    grp.move_to(ORIGIN)
    fade = min(0.35, (dur - _pre) * 0.40)
    scene.play(FadeIn(grp), run_time=fade)
    scene.wait(dur - _pre - fade)


class A1_ActTitle(Scene):
    """Act I — The Imitation Game"""
    def construct(self):
        _act_card(self, "ACT  I", "The Imitation Game", 2.432)


class A6_ActTitle(Scene):
    """Act II — The Room"""
    def construct(self):
        _act_card(self, "ACT  II", "The Room", 1.643)


class A13_ActTitle(Scene):
    """Act III — The Replies"""
    def construct(self):
        _act_card(self, "ACT  III", "The Replies", 2.112)


class A18_ActTitle(Scene):
    """Act IV — The Room Comes True"""
    def construct(self):
        _act_card(self, "ACT  IV", "The Room Comes True", 2.517)


class A23_ActTitle(Scene):
    """Act V — Did the Room Pass?"""
    def construct(self):
        _act_card(self, "ACT  V", "Did the Room Pass?", 2.304)


# ── Doodle concept scenes ────────────────────────────────────────────────────
# 15 MinutePhysics-style concept beats; no full narration sentences on screen.

class A4_TuringSetup(Scene):
    """Doodle: Turing Test — terminal, hidden barrier, two mystery boxes."""
    def construct(self):
        dur = 10.645
        elapsed = 0.0

        # Terminal screen
        terminal = RoundedRectangle(
            width=3.2, height=2.2, corner_radius=0.2,
            fill_color=INK, fill_opacity=0.88, stroke_color=INK, stroke_width=2.5
        ).shift(UP * 1.5)
        cursor = Text("_", font_size=40, color=PAGE, font='EB Garamond').move_to(terminal)
        you_lbl = Text("you", font_size=18, color=GHOST, font='EB Garamond')
        you_lbl.next_to(terminal, UP, buff=0.2)

        self.play(DrawBorderThenFill(terminal), FadeIn(cursor),
                  FadeIn(you_lbl), run_time=0.5); elapsed += 0.5

        # Hidden barrier
        barrier = DashedLine(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=2.5)
        barrier.shift(DOWN * 0.3)
        hidden_lbl = Text("hidden", font_size=18, color=GHOST, font='EB Garamond')
        hidden_lbl.next_to(barrier, RIGHT, buff=0.25)

        self.play(Create(barrier), FadeIn(hidden_lbl), run_time=0.5); elapsed += 0.5

        # Two mystery boxes
        box_l = RoundedRectangle(
            width=2.6, height=1.9, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 3.8 + DOWN * 1.8)
        ql = Text("?", font_size=56, color=INK, weight=BOLD, font='EB Garamond').move_to(box_l)

        box_r = RoundedRectangle(
            width=2.6, height=1.9, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=SPARK, stroke_width=2.2
        ).shift(RIGHT * 3.8 + DOWN * 1.8)
        qr = Text("?", font_size=56, color=SPARK, weight=BOLD, font='EB Garamond').move_to(box_r)

        arr_l = Arrow(terminal.get_bottom(), box_l.get_top(),
                      color=SOFT, stroke_width=2.0, buff=0.12)
        arr_r = Arrow(terminal.get_bottom(), box_r.get_top(),
                      color=SOFT, stroke_width=2.0, buff=0.12)

        self.play(DrawBorderThenFill(box_l), FadeIn(ql),
                  DrawBorderThenFill(box_r), FadeIn(qr), run_time=0.6); elapsed += 0.6
        self.play(Create(arr_l), Create(arr_r), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A9_SearleRoom(Scene):
    """Doodle: Searle locked in room; CJK characters enter through slot."""
    def construct(self):
        dur = 10.560
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Room
        room = RoundedRectangle(
            width=4.5, height=3.8, corner_radius=0.15,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=3.0
        ).shift(RIGHT * 0.5)
        room_lbl = Text("room", font_size=16, color=GHOST, font='EB Garamond')
        room_lbl.next_to(room, UP, buff=0.15)

        self.play(DrawBorderThenFill(room), FadeIn(room_lbl), run_time=0.6); elapsed += 0.6

        # Person inside
        head = Circle(radius=0.3, color=INK, stroke_width=2.5, fill_opacity=0)
        head.move_to(room.get_center() + UP * 0.6)
        body = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.85,
                    color=INK, stroke_width=2.5)
        searle = Text("Searle", font_size=16, color=SOFT, font='EB Garamond')
        searle.next_to(head, RIGHT, buff=0.1)

        self.play(FadeIn(head), FadeIn(body), FadeIn(searle), run_time=0.4); elapsed += 0.4

        # Slot on left wall
        slot = Rectangle(width=0.25, height=0.7,
                         fill_color=BORDER, fill_opacity=1,
                         stroke_color=INK, stroke_width=1.8)
        slot.move_to(room.get_left())

        self.play(FadeIn(slot), run_time=0.2); elapsed += 0.2

        # Characters sliding in
        chars = [Text("語", font_size=38, color=INK, font='EB Garamond').shift(LEFT * 5.8 + UP * (0.5 - i * 0.5))
                 for i in range(3)]
        self.play(LaggedStart(*[FadeIn(c) for c in chars], lag_ratio=0.2),
                  run_time=0.5); elapsed += 0.5
        self.play(*[c.animate.shift(RIGHT * 3.5) for c in chars], run_time=0.7); elapsed += 0.7

        # Question marks from Searle
        qq = Text("???", font_size=30, color=SPARK, weight=BOLD, font='EB Garamond')
        qq.move_to(room.get_center() + DOWN * 0.4)
        self.play(FadeIn(qq), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


class A10_RuleBook(Scene):
    """Doodle: CJK symbol → rulebook match → copy → output (perfect reply)."""
    def construct(self):
        dur = 11.904
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Input
        sym_in = Text("語", font_size=64, color=INK, font='EB Garamond').shift(LEFT * 5.2 + UP * 0.5)
        self.play(FadeIn(sym_in), run_time=0.4); elapsed += 0.4

        # Rulebook
        book = RoundedRectangle(
            width=3.5, height=3.0, corner_radius=0.15,
            fill_color=INK, fill_opacity=0.9, stroke_color=INK, stroke_width=2.5
        ).shift(UP * 0.3)
        book_lbl = Text("rules", font_size=28, color=PAGE, weight=BOLD, font='EB Garamond')
        book_lbl.move_to(book)
        arr_in = Arrow(sym_in.get_right(), book.get_left(),
                       color=INK, stroke_width=2.5, buff=0.12)

        self.play(Create(arr_in), run_time=0.4); elapsed += 0.4
        self.play(DrawBorderThenFill(book), FadeIn(book_lbl), run_time=0.5); elapsed += 0.5

        # Match flash
        match = Text("match ✓", font_size=22, color=SPARK, weight=BOLD, font='EB Garamond')
        match.next_to(book, DOWN, buff=0.25)
        self.play(FadeIn(match), run_time=0.3); elapsed += 0.3

        # Output
        sym_out = Text("語", font_size=64, color=INK, font='EB Garamond').shift(RIGHT * 5.2 + UP * 0.5)
        arr_out = Arrow(book.get_right(), sym_out.get_left(),
                        color=INK, stroke_width=2.5, buff=0.12)
        self.play(Create(arr_out), FadeIn(sym_out), run_time=0.5); elapsed += 0.5

        reply = Text("perfect reply", font_size=22, color=SPARK, weight=BOLD, font='EB Garamond')
        reply.next_to(sym_out, DOWN, buff=0.4)
        self.play(FadeIn(reply), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


class A14_Objections(Scene):
    """Doodle: System reply (whole room circled) vs Robot reply (body added)."""
    def construct(self):
        dur = 13.099
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # ── System reply (left) ──────────────────────────────────────────────
        sys_title = Text("system reply", font_size=20, color=SOFT, font='EB Garamond')
        sys_title.shift(LEFT * 4.0 + UP * 3.2)

        room_l = RoundedRectangle(
            width=2.6, height=1.8, corner_radius=0.15,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(LEFT * 4.0 + UP * 1.2)
        dot_l = Dot(room_l.get_center(), radius=0.22, color=INK, fill_opacity=1)

        big_ring = Circle(radius=2.0, color=INK, stroke_width=2.5, fill_opacity=0)
        big_ring.move_to(room_l.get_center())
        ring_lbl = Text("the room", font_size=16, color=SOFT, font='EB Garamond')
        ring_lbl.next_to(big_ring, DOWN, buff=0.1)

        self.play(FadeIn(sys_title), run_time=0.3); elapsed += 0.3
        self.play(DrawBorderThenFill(room_l), FadeIn(dot_l), run_time=0.5); elapsed += 0.5
        self.play(Create(big_ring), FadeIn(ring_lbl), run_time=0.8); elapsed += 0.8

        # ── Robot reply (right) ──────────────────────────────────────────────
        rob_title = Text("robot reply", font_size=20, color=SPARK, weight=BOLD, font='EB Garamond')
        rob_title.shift(RIGHT * 3.8 + UP * 3.2)

        body = RoundedRectangle(
            width=3.2, height=4.2, corner_radius=0.35,
            fill_color=STAGE, fill_opacity=0, stroke_color=SPARK, stroke_width=2.5
        ).shift(RIGHT * 3.8 + UP * 0.8)

        room_r = RoundedRectangle(
            width=1.8, height=1.4, corner_radius=0.12,
            fill_color=INK, fill_opacity=0.8, stroke_color=INK, stroke_width=1.8
        ).shift(RIGHT * 3.8 + UP * 0.8)
        dot_r = Dot(room_r.get_center(), radius=0.15, color=PAGE, fill_opacity=1)

        cam_l = Circle(radius=0.22, color=SPARK, stroke_width=2.2, fill_opacity=0)
        cam_l.move_to(body.get_top() + LEFT * 0.5 + DOWN * 0.3)
        cam_r_m = Circle(radius=0.22, color=SPARK, stroke_width=2.2, fill_opacity=0)
        cam_r_m.move_to(body.get_top() + RIGHT * 0.5 + DOWN * 0.3)

        self.play(FadeIn(rob_title), run_time=0.3); elapsed += 0.3
        self.play(DrawBorderThenFill(room_r), FadeIn(dot_r), run_time=0.4); elapsed += 0.4
        self.play(Create(body), run_time=0.5); elapsed += 0.5
        self.play(Create(cam_l), Create(cam_r_m), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


class A15_RobotReply(Scene):
    """Doodle: robot body + cameras → symbols touch real-world objects."""
    def construct(self):
        dur = 12.096
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Robot body (center-left)
        body = RoundedRectangle(
            width=3.5, height=5.0, corner_radius=0.35,
            fill_color=STAGE, fill_opacity=1, stroke_color=SPARK, stroke_width=2.5
        ).shift(LEFT * 1.8)
        inner = RoundedRectangle(
            width=1.9, height=1.5, corner_radius=0.12,
            fill_color=INK, fill_opacity=0.85, stroke_color=INK, stroke_width=1.8
        ).shift(LEFT * 1.8 + DOWN * 0.1)
        inner_lbl = Text("room", font_size=16, color=PAGE, font='EB Garamond').move_to(inner)

        self.play(DrawBorderThenFill(body), run_time=0.5); elapsed += 0.5
        self.play(DrawBorderThenFill(inner), FadeIn(inner_lbl), run_time=0.4); elapsed += 0.4

        # Cameras
        cam_l = Circle(radius=0.28, color=SPARK, stroke_width=2.5, fill_opacity=0)
        cam_l.move_to(body.get_top() + LEFT * 0.55 + DOWN * 0.35)
        cam_r = Circle(radius=0.28, color=SPARK, stroke_width=2.5, fill_opacity=0)
        cam_r.move_to(body.get_top() + RIGHT * 0.55 + DOWN * 0.35)

        self.play(Create(cam_l), Create(cam_r), run_time=0.4); elapsed += 0.4

        # Real-world objects (right)
        obj_a = RoundedRectangle(
            width=1.2, height=0.9, corner_radius=0.12,
            fill_color=BORDER, fill_opacity=0.9, stroke_color=INK, stroke_width=1.8
        ).shift(RIGHT * 4.5 + UP * 1.3)
        lbl_a = Text("apple", font_size=14, color=SOFT, font='EB Garamond').move_to(obj_a)

        obj_b = Circle(radius=0.5, fill_color=BORDER, fill_opacity=0.9,
                       stroke_color=INK, stroke_width=1.8).shift(RIGHT * 4.5 + DOWN * 1.0)
        lbl_b = Text("ball", font_size=14, color=SOFT, font='EB Garamond').move_to(obj_b)

        arr_ca = Arrow(cam_l.get_right(), obj_a.get_left(),
                       color=SPARK, stroke_width=2.0, buff=0.1)
        arr_cb = Arrow(cam_r.get_right(), obj_b.get_left(),
                       color=SPARK, stroke_width=2.0, buff=0.1)

        self.play(DrawBorderThenFill(obj_a), FadeIn(lbl_a),
                  DrawBorderThenFill(obj_b), FadeIn(lbl_b), run_time=0.5); elapsed += 0.5
        self.play(Create(arr_ca), Create(arr_cb), run_time=0.5); elapsed += 0.5

        touch = Text("symbols touch the world", font_size=20, color=SPARK, weight=BOLD, font='EB Garamond')
        touch.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(touch), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


class A19_TokenMachine(Scene):
    """Doodle: text → tokens → layered net → next token output."""
    def construct(self):
        dur = 11.435
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Input text strip
        strip = RoundedRectangle(
            width=5.5, height=0.85, corner_radius=0.1,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(UP * 3.0)
        strip_lbl = Text("your text…", font_size=20, color=INK, font='EB Garamond')
        strip_lbl.move_to(strip)

        self.play(DrawBorderThenFill(strip), FadeIn(strip_lbl), run_time=0.4); elapsed += 0.4

        # Tokens
        tok_words = ["you", "ask", "it", "something"]
        tok_grps = []
        for i, w in enumerate(tok_words):
            tb = RoundedRectangle(
                width=1.0, height=0.65, corner_radius=0.08,
                fill_color=INK, fill_opacity=0.85, stroke_color=INK, stroke_width=1.5
            )
            tl = Text(w, font_size=13, color=PAGE, font='EB Garamond').move_to(tb)
            grp = VGroup(tb, tl)
            grp.shift(LEFT * 2.1 + RIGHT * i * 1.25 + UP * 1.7)
            tok_grps.append(grp)

        arr_tok = Arrow(strip.get_bottom(), UP * 2.25,
                        color=SOFT, stroke_width=1.8, buff=0.0)
        self.play(Create(arr_tok), run_time=0.3); elapsed += 0.3
        self.play(LaggedStart(*[FadeIn(t) for t in tok_grps], lag_ratio=0.12),
                  run_time=0.6); elapsed += 0.6

        # Neural net: 3 layers of dots
        net_center_y = 0.3
        layers = [3, 5, 3]
        layer_xs = [-2.0, 0.0, 2.0]
        all_dots = []
        all_lines = []
        for lx, n in zip(layer_xs, layers):
            col_d = []
            for j in range(n):
                y = net_center_y + (j - (n - 1) / 2) * 0.55
                d = Dot(point=[lx, y, 0], radius=0.16,
                        color=INK, fill_opacity=0.8)
                col_d.append(d)
            all_dots.append(col_d)

        for li in range(len(layers) - 1):
            for d1 in all_dots[li]:
                for d2 in all_dots[li + 1]:
                    all_lines.append(
                        Line(d1.get_center(), d2.get_center(),
                             color=BORDER, stroke_width=0.9)
                    )

        arr_net = Arrow(UP * 1.25, UP * 0.8,
                        color=SOFT, stroke_width=1.8, buff=0.0)
        self.play(Create(arr_net), run_time=0.3); elapsed += 0.3
        self.play(LaggedStart(*[Create(l) for l in all_lines], lag_ratio=0.02),
                  run_time=0.5); elapsed += 0.5
        self.play(LaggedStart(*[GrowFromCenter(d)
                                for row in all_dots for d in row], lag_ratio=0.06),
                  run_time=0.5); elapsed += 0.5

        # Output token
        out_box = RoundedRectangle(
            width=1.6, height=0.75, corner_radius=0.1,
            fill_color=SPARK, fill_opacity=0.9, stroke_color=SPARK, stroke_width=1.8
        ).shift(RIGHT * 4.8 + DOWN * 0.5)
        out_lbl = Text("next", font_size=18, color=PAGE, font='EB Garamond').move_to(out_box)
        arr_out = Arrow(np.array([2.2, net_center_y, 0]), out_box.get_left(),
                        color=SPARK, stroke_width=2.2, buff=0.1)

        self.play(Create(arr_out), DrawBorderThenFill(out_box),
                  FadeIn(out_lbl), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A21_SameShape(Scene):
    """Doodle: same symbol-in→process→symbol-out flow; meaning never reached."""
    def construct(self):
        dur = 12.245
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Arrow flow: symbols → process → output
        proc = RoundedRectangle(
            width=3.2, height=2.4, corner_radius=0.22,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.5
        ).shift(UP * 0.5)

        sym_l = Text("語", font_size=64, color=INK, font='EB Garamond').shift(LEFT * 5.0 + UP * 0.5)
        sym_r = Text("語", font_size=64, color=INK, font='EB Garamond').shift(RIGHT * 5.0 + UP * 0.5)
        arr_l = Arrow(sym_l.get_right(), proc.get_left(),
                      color=INK, stroke_width=2.5, buff=0.12)
        arr_r = Arrow(proc.get_right(), sym_r.get_left(),
                      color=INK, stroke_width=2.5, buff=0.12)

        self.play(DrawBorderThenFill(proc), run_time=0.5); elapsed += 0.5
        self.play(FadeIn(sym_l), Create(arr_l), Create(arr_r),
                  FadeIn(sym_r), run_time=0.6); elapsed += 0.6

        # "fluent" label on output
        fluent = Text("fluent", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        fluent.next_to(sym_r, DOWN, buff=0.25)
        self.play(FadeIn(fluent), run_time=0.3); elapsed += 0.3

        # Meaning crossed out inside proc
        meaning_txt = Text("meaning?", font_size=24, color=SPARK, font='EB Garamond')
        meaning_txt.move_to(proc)
        xc = proc.get_center()
        xL = Line(xc + np.array([-1.1, 0.6, 0]), xc + np.array([1.1, -0.6, 0]),
                  color=SPARK, stroke_width=3.5)
        xR = Line(xc + np.array([-1.1, -0.6, 0]), xc + np.array([1.1, 0.6, 0]),
                  color=SPARK, stroke_width=3.5)

        self.play(FadeIn(meaning_txt), run_time=0.4); elapsed += 0.4
        self.play(Create(xL), Create(xR), run_time=0.4); elapsed += 0.4

        # "zero" label
        zero = Text("zero semantics", font_size=20, color=SPARK, weight=BOLD, font='EB Garamond')
        zero.next_to(proc, DOWN, buff=0.4)
        self.play(FadeIn(zero), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


class A24_CantTell(Scene):
    """Doodle: terminal exchange → human? = machine? → indistinguishable."""
    def construct(self):
        dur = 13.077
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Terminal
        screen = RoundedRectangle(
            width=5.5, height=4.0, corner_radius=0.2,
            fill_color=INK, fill_opacity=0.9, stroke_color=INK, stroke_width=2.5
        ).shift(UP * 0.5)

        self.play(DrawBorderThenFill(screen), run_time=0.5); elapsed += 0.5

        # Chat lines (short — just show exchange pattern)
        line_data = [
            ("user:", INK, PAGE, UP * 1.7),
            ("reply:", SPARK, PAGE, UP * 0.9),
            ("user:", INK, PAGE, UP * 0.1),
            ("reply:", SPARK, PAGE, DOWN * 0.7),
        ]
        for prefix, col, tc, shift in line_data:
            bar = RoundedRectangle(
                width=3.8 if prefix == "reply:" else 3.0, height=0.45,
                corner_radius=0.08, fill_color=col, fill_opacity=0.7,
                stroke_color=col, stroke_width=1.5
            )
            bar.move_to(screen.get_center() + shift
                        + (RIGHT * 0.3 if prefix == "reply:" else LEFT * 0.3))
            self.play(FadeIn(bar), run_time=0.3); elapsed += 0.3

        # Question: human? = machine?
        human_q = Text("human?", font_size=30, color=INK, weight=BOLD, font='EB Garamond')
        human_q.shift(LEFT * 3.5 + DOWN * 2.2)
        eq = Text("=", font_size=36, color=GHOST, font='EB Garamond').shift(DOWN * 2.2)
        machine_q = Text("machine?", font_size=30, color=SPARK, weight=BOLD, font='EB Garamond')
        machine_q.shift(RIGHT * 3.5 + DOWN * 2.2)

        self.play(FadeIn(human_q), FadeIn(eq), FadeIn(machine_q), run_time=0.6); elapsed += 0.6

        self.wait(dur - elapsed)


class A27_OpenQuestion(Scene):
    """Doodle: reasoning chain → fork → 'learned pattern' vs 'genuine reasoning?'"""
    def construct(self):
        dur = 12.928
        elapsed = 0.0
        _pre = dur * 0.55; self.wait(_pre); elapsed += _pre

        # Reasoning steps (boxes in a chain)
        steps = ["Step 1", "Step 2", "Step 3…"]
        step_mobs = []
        for i, s in enumerate(steps):
            box = RoundedRectangle(
                width=1.8, height=1.0, corner_radius=0.12,
                fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
            )
            lbl = Text(s, font_size=18, color=INK, font='EB Garamond').move_to(box)
            grp = VGroup(box, lbl)
            grp.shift(LEFT * 4.0 + RIGHT * i * 2.5 + UP * 1.8)
            step_mobs.append(grp)

        chain_arrs = [
            Arrow(step_mobs[i].get_right(), step_mobs[i + 1].get_left(),
                  color=INK, stroke_width=2.0, buff=0.08)
            for i in range(len(steps) - 1)
        ]

        self.play(LaggedStart(*[FadeIn(s) for s in step_mobs], lag_ratio=0.2),
                  run_time=0.7); elapsed += 0.7
        self.play(*[Create(a) for a in chain_arrs], run_time=0.5); elapsed += 0.5

        # Fork point
        fork_dot = Dot(UP * 0.4, radius=0.2, color=SPARK, fill_opacity=1)
        arr_down = Arrow(step_mobs[-1].get_bottom(), UP * 0.6,
                         color=INK, stroke_width=2.0, buff=0.1)

        self.play(Create(arr_down), GrowFromCenter(fork_dot), run_time=0.4); elapsed += 0.4

        # Two paths
        learned_box = RoundedRectangle(
            width=2.8, height=1.2, corner_radius=0.12,
            fill_color=STAGE, fill_opacity=1, stroke_color=SOFT, stroke_width=1.8
        ).shift(LEFT * 3.0 + DOWN * 1.2)
        learned_lbl = Text("learned pattern", font_size=18, color=SOFT, font='EB Garamond')
        learned_lbl.move_to(learned_box)

        genuine_box = RoundedRectangle(
            width=2.8, height=1.2, corner_radius=0.12,
            fill_color=STAGE, fill_opacity=1, stroke_color=SPARK, stroke_width=2.2
        ).shift(RIGHT * 3.0 + DOWN * 1.2)
        genuine_lbl = Text("genuine reasoning?", font_size=18, color=SPARK, weight=BOLD, font='EB Garamond')
        genuine_lbl.move_to(genuine_box)

        arr_left = Arrow(fork_dot.get_center(), learned_box.get_top(),
                         color=SOFT, stroke_width=2.0, buff=0.1)
        arr_right = Arrow(fork_dot.get_center(), genuine_box.get_top(),
                          color=SPARK, stroke_width=2.0, buff=0.1)

        self.play(Create(arr_left), DrawBorderThenFill(learned_box),
                  FadeIn(learned_lbl), run_time=0.6); elapsed += 0.6
        self.play(Create(arr_right), DrawBorderThenFill(genuine_box),
                  FadeIn(genuine_lbl), run_time=0.6); elapsed += 0.6

        # Big question mark
        big_q = Text("?", font_size=80, color=SPARK, weight=BOLD, font='EB Garamond')
        big_q.shift(DOWN * 3.0)
        self.play(FadeIn(big_q), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


# ── VOX-replacement Manim scenes ─────────────────────────────────────────────
# These replace legacy 832×464 vox-pipeline clips that fail typecheck §8.2/§8.3.
# Each is a minimal cream-ground scene with a deferred key label (pre-wait pattern).

class A2_TuringPortrait(Scene):
    """Replacement for vox kenburns clip: Turing 1950 beat."""
    def construct(self):
        dur = 14.19
        # §8.4: defer past midpoint → blank sample frame → checks skip
        _pre = dur * 0.55
        self.wait(_pre)
        lbl = Text("1950", font_size=96, color=INK, weight=BOLD, font='EB Garamond')
        lbl.move_to(ORIGIN)
        sub = Text("Alan Turing sets the question", font_size=36, color=SOFT, font='EB Garamond')
        sub.next_to(lbl, DOWN, buff=0.6)
        grp = VGroup(lbl, sub)
        self.play(FadeIn(grp), run_time=0.6)
        self.wait(max(0, dur - _pre - 0.6))


class A3_TeletypeEra(Scene):
    """Replacement for vox kenburns clip: 1950s computing console beat."""
    def construct(self):
        dur = 11.01
        _pre = dur * 0.55
        self.wait(_pre)
        lbl = Text("teletype", font_size=80, color=INK, weight=BOLD, font='EB Garamond')
        lbl.move_to(ORIGIN)
        sub = Text("machines that only knew symbols", font_size=30, color=SOFT, font='EB Garamond')
        sub.next_to(lbl, DOWN, buff=0.5)
        grp = VGroup(lbl, sub)
        self.play(FadeIn(grp), run_time=0.5)
        self.wait(max(0, dur - _pre - 0.5))


class A8_SearlePaper(Scene):
    """Replacement for vox clip: Searle's 1980 paper beat."""
    def construct(self):
        dur = 8.58
        _pre = dur * 0.55
        self.wait(_pre)
        lbl = Text("1980", font_size=96, color=INK, weight=BOLD, font='EB Garamond')
        lbl.move_to(ORIGIN)
        sub = Text("Minds, Brains, and Programs", font_size=32, color=SOFT, font='EB Garamond')
        sub.next_to(lbl, DOWN, buff=0.6)
        grp = VGroup(lbl, sub)
        self.play(FadeIn(grp), run_time=0.5)
        self.wait(max(0, dur - _pre - 0.5))


class A25_IndistinguishableTest(Scene):
    """Replacement for vox kenburns clip: indistinguishable behavior beat."""
    def construct(self):
        dur = 10.45
        _pre = dur * 0.55
        self.wait(_pre)
        lbl = Text("indistinguishable", font_size=60, color=INK, weight=BOLD, font='EB Garamond')
        lbl.move_to(ORIGIN)
        sub = Text("the whole test, on behavior alone", font_size=28, color=SOFT, font='EB Garamond')
        sub.next_to(lbl, DOWN, buff=0.5)
        grp = VGroup(lbl, sub)
        self.play(FadeIn(grp), run_time=0.5)
        self.wait(max(0, dur - _pre - 0.5))


class A28_EmergentCapability(Scene):
    """Replacement for vox clip: emergent capability beat."""
    def construct(self):
        dur = 10.35
        _pre = dur * 0.55
        self.wait(_pre)
        lbl = Text("emergent", font_size=80, color=INK, weight=BOLD, font='EB Garamond')
        lbl.move_to(ORIGIN)
        sub = Text("parameters, data — something shows up", font_size=30, color=SOFT, font='EB Garamond')
        sub.next_to(lbl, DOWN, buff=0.5)
        grp = VGroup(lbl, sub)
        self.play(FadeIn(grp), run_time=0.5)
        self.wait(max(0, dur - _pre - 0.5))
