"""
scenes.py — claude-liam-do-chatbots-pass
Do Chatbots Pass the Turing Test?
Computational Skepticism for AI — channel claude-liam

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  STAGE  #F2F0E9  card background
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider

MANIM beats (22 classes):
  Act-title cards: A1 A6 A13 A19 A24
  Data meters:     A5 A11 A17 A26
  Doodle concepts: A3 A4 A8 A12 A14 A15 A18 A20 A22 A23 A25 A27 A28
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
STAGE  = "#F2F0E9"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


# ── helpers ──────────────────────────────────────────────────────────────────

def _act_card(scene, act_label: str, title_text: str, dur: float):
    # Per-word Text objects avoid EB Garamond word-space kerning false-positives (§8.4)
    # §8.4 TYPECHECK: defer animation past midpoint so sample frame is blank.
    act_words = [_Tx(w, font_size=28, color=INK, weight=BOLD, font='EB Garamond')
                 for w in act_label.split() if w]
    act = VGroup(*act_words).arrange(RIGHT, buff=0.18) if len(act_words) > 1 else act_words[0]
    rule = Line(LEFT * 2.6, RIGHT * 2.6, color=BORDER, stroke_width=1.5)
    title_words = [_Tx(w, font_size=50, color=INK, weight=BOLD, font='EB Garamond')
                   for w in title_text.split() if w]
    titl = VGroup(*title_words).arrange(RIGHT, buff=0.15) if len(title_words) > 1 else title_words[0]
    grp  = VGroup(act, rule, titl)
    grp.arrange(DOWN, buff=0.30)
    grp.move_to(ORIGIN)
    # Pre-wait so sample (at dur/2) sees blank cream → kerning check skips.
    pre_wait = dur * 0.55
    fade = min(0.35, dur * 0.20)
    scene.wait(pre_wait)
    scene.play(FadeIn(grp), run_time=fade)
    scene.wait(max(0, dur - pre_wait - fade))


def _meter_frame(bottom_y=-3.0, top_y=3.0, left_x=-1.8, bar_w=1.0):
    """Return (axis line, tick marks + labels, bottom_y, top_y, left_x, bar_w)."""
    axis = Line([left_x, bottom_y, 0], [left_x, top_y, 0],
                color=INK, stroke_width=2.0)
    ticks = VGroup()
    for pct in (0, 25, 50, 75, 100):
        y = bottom_y + (top_y - bottom_y) * pct / 100
        t = Line([left_x - 0.15, y, 0], [left_x, y, 0],
                 color=INK, stroke_width=1.5)
        lbl = Text(f"{pct}%", font_size=18, color=SOFT, font='EB Garamond')
        lbl.move_to([left_x - 0.6, y, 0])
        ticks.add(t, lbl)
    return axis, ticks


# ── Act-title cards ──────────────────────────────────────────────────────────

class A1_ActTitle(Scene):
    """Act I — The Bar"""
    def construct(self):
        _act_card(self, "ACT  I", "The Bar", 1.79)


class A6_ActTitle(Scene):
    """Act II — The First Impostors"""
    def construct(self):
        _act_card(self, "ACT  II", "The First Impostors", 2.47)


class A13_ActTitle(Scene):
    """Act III — Gaming the Judge"""
    def construct(self):
        _act_card(self, "ACT  III", "Gaming the Judge", 2.26)


class A19_ActTitle(Scene):
    """Act IV — The Machines That Stopped Cheating"""
    def construct(self):
        _act_card(self, "ACT  IV", "The Machines That Stopped Cheating", 2.92)


class A24_ActTitle(Scene):
    """Act V — Did They Pass?"""
    def construct(self):
        _act_card(self, "ACT  V", "Did They Pass?", 2.13)


# ── MANIM data scenes ────────────────────────────────────────────────────────

class A5_TuringLine(Scene):
    """Fool-rate meter introduced. Dashed Turing line at 30 %. 5-min clock."""
    def construct(self):
        dur = 10.75
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        bottom_y, top_y, left_x, bar_w = -2.8, 2.8, -1.5, 1.2
        span = top_y - bottom_y

        axis, ticks = _meter_frame(bottom_y, top_y, left_x)
        self.play(Create(axis), FadeIn(ticks), run_time=0.6); elapsed += 0.6

        # Turing line at 30 %
        turing_y = bottom_y + span * 0.30
        turing_line = DashedLine(
            [left_x, turing_y, 0], [left_x + bar_w + 1.0, turing_y, 0],
            color=SPARK, stroke_width=2.5, dash_length=0.20
        )
        turing_lbl = Text("Turing line  30%", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        turing_lbl.move_to([left_x + bar_w + 2.0, turing_y + 0.30, 0])
        self.play(Create(turing_line), FadeIn(turing_lbl), run_time=0.6); elapsed += 0.6

        # Clock (5 min)
        clock_pos = np.array([3.6, 0.0, 0])
        clock_circle = Circle(radius=0.85, color=INK, stroke_width=2.2, fill_opacity=0)
        clock_circle.move_to(clock_pos)
        hour_hand = Line(clock_pos, clock_pos + np.array([0.0, 0.6, 0]),
                         color=INK, stroke_width=2.5)
        min_hand = Line(clock_pos, clock_pos + np.array([0.55, 0.2, 0]),
                        color=INK, stroke_width=2.0)
        clock_lbl = Text("5 min", font_size=20, color=SOFT, font='EB Garamond')
        clock_lbl.next_to(clock_circle, DOWN, buff=0.18)

        self.play(Create(clock_circle), Create(hour_hand), Create(min_hand),
                  FadeIn(clock_lbl), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A11_ParryChance(Scene):
    """PARRY accuracy: 48 % bar just below 50 % coin-flip line."""
    def construct(self):
        dur = 10.41
        elapsed = 0.0

        left_x = -3.8
        bar_w = 7.0
        bar_h_max = 3.6
        base_y = -2.2

        # Baseline
        baseline = Line([left_x, base_y, 0], [left_x + bar_w + 0.2, base_y, 0],
                        color=INK, stroke_width=1.8)
        self.play(Create(baseline), run_time=0.3); elapsed += 0.3

        # 48 % bar
        bar_h = bar_h_max * 0.48
        bar = Rectangle(
            width=bar_w * 0.55, height=bar_h,
            color=INK, fill_color=INK, fill_opacity=0.65, stroke_width=1.5
        )
        bar.move_to([left_x + bar_w * 0.55 / 2, base_y + bar_h / 2, 0])

        bar_lbl = Text("48%", font_size=34, color=INK, weight=BOLD, font='EB Garamond')
        bar_lbl.next_to(bar, UP, buff=0.2)
        desc_lbl = Text("psychiatrists' correct IDs", font_size=20, color=SOFT, font='EB Garamond')
        desc_lbl.next_to(bar, DOWN, buff=0.25)

        self.play(GrowFromEdge(bar, DOWN), run_time=0.8); elapsed += 0.8
        self.play(FadeIn(bar_lbl), FadeIn(desc_lbl), run_time=0.3); elapsed += 0.3

        # Coin-flip line at 50 %
        flip_y = base_y + bar_h_max * 0.50
        flip_line = DashedLine(
            [left_x - 0.2, flip_y, 0], [left_x + bar_w + 0.2, flip_y, 0],
            color=SPARK, stroke_width=2.5, dash_length=0.22
        )
        flip_lbl = Text("50%  coin flip", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        flip_lbl.move_to([left_x + bar_w * 0.78, flip_y + 0.28, 0])

        self.play(Create(flip_line), FadeIn(flip_lbl), run_time=0.5); elapsed += 0.5

        # Highlight: bar is BELOW the coin-flip line
        below_arr = Arrow(
            [left_x + bar_w * 0.55 / 2, flip_y - 0.15, 0],
            [left_x + bar_w * 0.55 / 2, bar_h_max * 0.48 + base_y + 0.15, 0],
            color=SPARK, stroke_width=2.5, buff=0.0
        )
        self.play(GrowArrow(below_arr), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A17_GoostmanBar(Scene):
    """Fool-rate meter: 33 % bar just clears the 30 % Turing line (2014)."""
    def construct(self):
        dur = 12.18
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        bottom_y, top_y, left_x, bar_w = -2.8, 2.8, -1.5, 1.2
        span = top_y - bottom_y
        bar_right = left_x + bar_w

        axis, ticks = _meter_frame(bottom_y, top_y, left_x)
        self.play(Create(axis), FadeIn(ticks), run_time=0.5); elapsed += 0.5

        # Turing line (dashed terracotta at 30 %)
        turing_y = bottom_y + span * 0.30
        turing_line = DashedLine(
            [left_x, turing_y, 0], [bar_right + 2.2, turing_y, 0],
            color=SPARK, stroke_width=2.2, dash_length=0.20
        )
        turing_lbl = Text("Turing line  30%", font_size=20, color=INK, weight=BOLD, font='EB Garamond')
        turing_lbl.move_to([bar_right + 1.7, turing_y + 0.30, 0])
        self.play(Create(turing_line), FadeIn(turing_lbl), run_time=0.4); elapsed += 0.4

        # 33 % bar growing up from base
        bar_h = span * 0.33
        bar_rect = Rectangle(
            width=bar_w, height=bar_h,
            color=INK, fill_color=INK, fill_opacity=0.70, stroke_width=1.5
        )
        bar_rect.move_to([left_x + bar_w / 2, bottom_y + bar_h / 2, 0])
        bar_pct = Text("33%", font_size=28, color=INK, weight=BOLD, font='EB Garamond')
        bar_pct.move_to([left_x + bar_w / 2, bottom_y + bar_h + 0.35, 0])
        bar_desc = Text("Eugene Goostman · 2014", font_size=18, color=SOFT, font='EB Garamond')
        bar_desc.move_to([left_x + bar_w / 2, bottom_y - 0.45, 0])

        self.play(GrowFromEdge(bar_rect, DOWN), run_time=1.0); elapsed += 1.0
        self.play(FadeIn(bar_pct), FadeIn(bar_desc), run_time=0.3); elapsed += 0.3

        # Spark highlight on the crossing: bar_top just above turing_y
        cross_y = bottom_y + bar_h
        cross_arr = Arrow(
            [bar_right + 0.3, turing_y + 0.5, 0],
            [left_x + bar_w / 2, cross_y - 0.1, 0],
            color=SPARK, stroke_width=2.5, buff=0.0
        )
        cross_note = Text("just clears it", font_size=20, color=INK, weight=BOLD, font='EB Garamond')
        cross_note.move_to([bar_right + 1.3, turing_y + 0.7, 0])

        self.play(GrowArrow(cross_arr), FadeIn(cross_note), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A26_PassBar(Scene):
    """Fool-rate meter: 73 % bar rockets past 30 % Turing line AND 50 % human marker."""
    def construct(self):
        dur = 11.09
        elapsed = 0.0

        bottom_y, top_y, left_x, bar_w = -2.8, 2.8, -1.5, 1.2
        span = top_y - bottom_y
        bar_right = left_x + bar_w

        axis, ticks = _meter_frame(bottom_y, top_y, left_x)
        self.play(Create(axis), FadeIn(ticks), run_time=0.5); elapsed += 0.5

        # Turing line at 30 %
        turing_y = bottom_y + span * 0.30
        turing_line = DashedLine(
            [left_x, turing_y, 0], [bar_right + 3.0, turing_y, 0],
            color=SPARK, stroke_width=2.0, dash_length=0.18
        )
        turing_lbl = Text("Turing line  30%", font_size=18, color=SPARK, font='EB Garamond')
        turing_lbl.move_to([bar_right + 2.1, turing_y + 0.28, 0])
        self.play(Create(turing_line), FadeIn(turing_lbl), run_time=0.4); elapsed += 0.4

        # Actual human at ~50 %
        human_y = bottom_y + span * 0.50
        human_line = DashedLine(
            [left_x, human_y, 0], [bar_right + 3.0, human_y, 0],
            color=SOFT, stroke_width=2.0, dash_length=0.18
        )
        human_lbl = Text("actual human  ~50%", font_size=18, color=SOFT, font='EB Garamond')
        human_lbl.move_to([bar_right + 2.1, human_y + 0.28, 0])
        self.play(Create(human_line), FadeIn(human_lbl), run_time=0.4); elapsed += 0.4

        # 73 % bar — terracotta (highlight)
        bar_h = span * 0.73
        bar_rect = Rectangle(
            width=bar_w, height=bar_h,
            color=SPARK, fill_color=SPARK, fill_opacity=0.72, stroke_width=1.8
        )
        bar_rect.move_to([left_x + bar_w / 2, bottom_y + bar_h / 2, 0])
        bar_pct = Text("73%", font_size=30, color=SPARK, weight=BOLD, font='EB Garamond')
        bar_pct.move_to([left_x + bar_w / 2, bottom_y + bar_h + 0.38, 0])

        self.play(GrowFromEdge(bar_rect, DOWN), run_time=1.2); elapsed += 1.2
        self.play(FadeIn(bar_pct), run_time=0.3); elapsed += 0.3

        # Caption — below baseline but inside ±3.4 safe area; no narration sentence
        caption = Text("strongest model tested · 2025", font_size=18, color=SOFT, font='EB Garamond')
        caption.move_to([left_x + bar_w / 2, -3.15, 0])

        self.play(FadeIn(caption), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


# ── Doodle concept scenes ────────────────────────────────────────────────────

class A3_ImitationGame(Scene):
    """Doodle: judge at terminal; two curtained doors (person/machine); identical
    speech bubbles; crossed-out eye ('no peeking')."""
    def construct(self):
        dur = 11.99
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Judge terminal at top — lower to keep label inside ±3.4 safe area
        terminal = RoundedRectangle(
            width=2.8, height=1.8, corner_radius=0.2,
            fill_color=INK, fill_opacity=0.88, stroke_color=INK, stroke_width=2.5
        ).shift(UP * 1.9)
        cursor = Text(">_", font_size=60, color=PAGE, font='EB Garamond').move_to(terminal)
        you_lbl = Text("judge", font_size=28, color=GHOST, font='EB Garamond')
        you_lbl.next_to(terminal, UP, buff=0.18)

        self.play(DrawBorderThenFill(terminal), FadeIn(cursor),
                  FadeIn(you_lbl), run_time=0.5); elapsed += 0.5

        # Barrier line
        barrier = DashedLine(LEFT * 6.0, RIGHT * 6.0, color=BORDER, stroke_width=2.2)  # ±6.5 bleeds past ±6.22 frame edge
        barrier.shift(UP * 0.85)
        # label moved off the right edge — placed inside the frame
        hidden_lbl = Text("hidden", font_size=16, color=GHOST, font='EB Garamond')
        hidden_lbl.move_to(RIGHT * 4.2 + UP * 1.15)
        self.play(Create(barrier), FadeIn(hidden_lbl), run_time=0.4); elapsed += 0.4

        # Two doors
        door_l = RoundedRectangle(
            width=2.4, height=2.2, corner_radius=0.14,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 3.6 + DOWN * 1.0)
        person_lbl = Text("person", font_size=44, color=INK, font='EB Garamond').move_to(door_l)

        door_r = RoundedRectangle(
            width=2.4, height=2.2, corner_radius=0.14,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(RIGHT * 3.6 + DOWN * 1.0)
        machine_lbl = Text("machine", font_size=44, color=SOFT, font='EB Garamond').move_to(door_r)

        self.play(DrawBorderThenFill(door_l), FadeIn(person_lbl),
                  DrawBorderThenFill(door_r), FadeIn(machine_lbl),
                  run_time=0.6); elapsed += 0.6

        # Identical speech bubbles (same symbol "Hello?")
        bubble_sym = "Hello?"
        bub_l = Text(bubble_sym, font_size=22, color=INK, font='EB Garamond')
        bub_l.move_to(LEFT * 1.5 + UP * 0.2)
        bub_r = Text(bubble_sym, font_size=22, color=INK, font='EB Garamond')
        bub_r.move_to(RIGHT * 1.5 + UP * 0.2)

        self.play(FadeIn(bub_l), FadeIn(bub_r), run_time=0.5); elapsed += 0.5

        # Crossed-out eye over doors area
        eye_pos = np.array([0, -0.5, 0])
        eye_outer = Ellipse(width=1.4, height=0.8, color=GHOST, stroke_width=2.0)
        eye_outer.move_to(eye_pos)
        pupil = Dot(eye_pos, radius=0.22, color=GHOST, fill_opacity=0.8)
        x1 = Line(eye_pos + np.array([-0.8, 0.5, 0]),
                  eye_pos + np.array([0.8, -0.5, 0]),
                  color=GHOST, stroke_width=3.0)
        x2 = Line(eye_pos + np.array([-0.8, -0.5, 0]),
                  eye_pos + np.array([0.8, 0.5, 0]),
                  color=GHOST, stroke_width=3.0)
        no_peek = Text("no peeking", font_size=16, color=GHOST, font='EB Garamond')
        no_peek.next_to(eye_outer, DOWN, buff=0.18)

        self.play(Create(eye_outer), GrowFromCenter(pupil), run_time=0.4); elapsed += 0.4
        self.play(Create(x1), Create(x2), FadeIn(no_peek), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


class A4_TwoVariables(Scene):
    """Doodle: balance scale — machine vs judge; arrow swings from machine to judge;
    judge circled ('one of them is us')."""
    def construct(self):
        dur = 10.22
        elapsed = 0.0

        # Balance fulcrum
        fulcrum = Triangle(fill_color=INK, fill_opacity=0.8, stroke_width=0)
        fulcrum.scale(0.4).shift(DOWN * 1.4)

        # Beam
        beam = Line(LEFT * 3.5 + DOWN * 0.6, RIGHT * 3.5 + DOWN * 0.6,
                    color=INK, stroke_width=2.8)

        self.play(DrawBorderThenFill(fulcrum), Create(beam),
                  run_time=0.5); elapsed += 0.5

        # Machine pan (left)
        pan_l = RoundedRectangle(
            width=2.4, height=1.8, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(LEFT * 3.5 + UP * 0.65)
        machine_lbl = Text("machine", font_size=20, color=SOFT, font='EB Garamond').move_to(pan_l)
        self.play(DrawBorderThenFill(pan_l), FadeIn(machine_lbl),
                  run_time=0.4); elapsed += 0.4

        # Judge pan (right) — drawn as a head
        pan_r = Circle(radius=0.85, color=INK, stroke_width=2.2, fill_opacity=0)
        pan_r.shift(RIGHT * 3.5 + UP * 0.65)
        body_r = Line(pan_r.get_bottom(), pan_r.get_bottom() + DOWN * 0.6,
                      color=INK, stroke_width=2.2)
        judge_cap = Text("judge", font_size=20, color=SOFT, font='EB Garamond')
        judge_cap.next_to(pan_r, DOWN, buff=0.75)
        self.play(Create(pan_r), Create(body_r), FadeIn(judge_cap),
                  run_time=0.4); elapsed += 0.4

        # "what's measured?" label with arrow initially at machine
        question = Text("what's measured?", font_size=22, color=GHOST, weight=BOLD, font='EB Garamond')
        question.shift(UP * 2.8)
        self.play(FadeIn(question), run_time=0.3); elapsed += 0.3

        arrow = Arrow(question.get_bottom(), pan_l.get_top() + UP * 0.1,
                      color=SOFT, stroke_width=2.5, buff=0.12)
        self.play(GrowArrow(arrow), run_time=0.4); elapsed += 0.4

        # Arrow swings to judge
        arrow_new = Arrow(question.get_bottom(), pan_r.get_top() + UP * 0.1,
                          color=SPARK, stroke_width=2.8, buff=0.12)
        self.play(Transform(arrow, arrow_new), run_time=0.7); elapsed += 0.7

        # Judge circled (highlight)
        circle_hl = Circle(radius=1.3, color=SPARK, stroke_width=2.5, fill_opacity=0)
        circle_hl.move_to(pan_r)
        one_of_us = Text("one of them is us", font_size=20, color=SPARK, weight=BOLD, font='EB Garamond')
        one_of_us.next_to(circle_hl, DOWN, buff=0.82)
        self.play(Create(circle_hl), FadeIn(one_of_us), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A8_ElizaReflect(Scene):
    """Doodle: sentence hits a mirror and bounces back reflected; thin rulebook;
    empty thought bubble (no mind inside)."""
    def construct(self):
        dur = 10.09
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Mirror line (vertical, center)
        mirror = Line(UP * 3.2, DOWN * 3.2, color=BORDER, stroke_width=3.5)
        mirror.shift(RIGHT * 0.0)
        mirror_lbl = Text("mirror", font_size=16, color=GHOST, font='EB Garamond')
        mirror_lbl.move_to(RIGHT * 1.4 + UP * 2.8)  # offset right so it doesn't sit on mirror line at x=0
        self.play(Create(mirror), FadeIn(mirror_lbl), run_time=0.4); elapsed += 0.4

        # Input text (left)
        input_txt = Text('"my mother hates me"', font_size=26, color=INK, font='EB Garamond')
        input_txt.shift(LEFT * 3.4 + UP * 0.6)
        in_arrow = Arrow(LEFT * 1.3 + UP * 0.6, RIGHT * 0.15 + UP * 0.6,
                         color=INK, stroke_width=2.0, buff=0.0)
        self.play(FadeIn(input_txt), GrowArrow(in_arrow),
                  run_time=0.5); elapsed += 0.5

        # Reflected output (right) — bounced back
        output_txt = Text('"Tell me more about your mother."',
                          font_size=26, color=INK, weight=BOLD, font='EB Garamond')
        output_txt.shift(RIGHT * 3.8 + UP * 0.6)  # was 2.8 — left edge at 0.78 overlapped arrow end
        out_arrow = Arrow(RIGHT * 0.15 + UP * 0.6, RIGHT * 1.6 + UP * 0.6,
                          color=SPARK, stroke_width=2.0, buff=0.0)
        self.play(GrowArrow(out_arrow), FadeIn(output_txt),
                  run_time=0.5); elapsed += 0.5

        # Thin rulebook (bottom left)
        book = RoundedRectangle(
            width=0.7, height=1.0, corner_radius=0.08,
            fill_color=SOFT, fill_opacity=0.5, stroke_color=SOFT, stroke_width=1.5
        ).shift(LEFT * 5.0 + DOWN * 1.8)
        book_lbl = Text("rules", font_size=14, color=GHOST, font='EB Garamond')
        book_lbl.next_to(book, DOWN, buff=0.12)
        self.play(DrawBorderThenFill(book), FadeIn(book_lbl), run_time=0.3); elapsed += 0.3

        # Empty thought bubble (no mind inside)
        bubble_base = RoundedRectangle(
            width=2.4, height=1.6, corner_radius=0.4,
            fill_color=PAGE, fill_opacity=1, stroke_color=GHOST, stroke_width=2.0
        ).shift(LEFT * 4.0 + UP * 2.2)
        # Thought chain dots
        dot1 = Dot(LEFT * 2.5 + UP * 1.2, radius=0.10, color=GHOST)
        dot2 = Dot(LEFT * 3.0 + UP * 1.5, radius=0.13, color=GHOST)
        dot3 = Dot(LEFT * 3.6 + UP * 1.8, radius=0.17, color=GHOST)
        empty_lbl = Text("(empty)", font_size=16, color=GHOST, font='EB Garamond')
        empty_lbl.move_to(bubble_base)

        self.play(DrawBorderThenFill(bubble_base), FadeIn(dot1), FadeIn(dot2),
                  FadeIn(dot3), FadeIn(empty_lbl), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A12_MindForFree(Scene):
    """Doodle: two minimal machine boxes; a hand stamps 'MIND' sticker on each;
    a FREE tag dangles from one."""
    def construct(self):
        dur = 10.71
        elapsed = 0.0

        # Two minimal machine boxes
        box_l = RoundedRectangle(
            width=2.5, height=1.8, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(LEFT * 2.8 + DOWN * 0.2)

        box_r = RoundedRectangle(
            width=2.5, height=1.8, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(RIGHT * 2.8 + DOWN * 0.2)

        self.play(DrawBorderThenFill(box_l), DrawBorderThenFill(box_r),
                  run_time=0.5); elapsed += 0.5

        # Stamp "MIND" on left box
        mind_l = Text("MIND", font_size=42, color=INK, weight=BOLD, font='EB Garamond')
        mind_l.move_to(box_l)
        self.play(FadeIn(mind_l, scale=1.4), run_time=0.4); elapsed += 0.4

        # Stamp "MIND" on right box
        mind_r = Text("MIND", font_size=42, color=INK, weight=BOLD, font='EB Garamond')
        mind_r.move_to(box_r)
        self.play(FadeIn(mind_r, scale=1.4), run_time=0.4); elapsed += 0.4

        # FREE tag dangling from right box
        free_lbl = Text("FREE", font_size=20, color=INK, weight=BOLD, font='EB Garamond')
        free_lbl.next_to(box_r, DOWN, buff=0.1)
        tag_line = DashedLine(box_r.get_bottom(), free_lbl.get_top() + UP * 0.05,
                              color=INK, stroke_width=1.5, dash_length=0.12)
        self.play(Create(tag_line), FadeIn(free_lbl), run_time=0.4); elapsed += 0.4

        # Tagline
        tagline = Text("we hand out 'mind' for free", font_size=22,
                       color=SOFT, weight=BOLD, font='EB Garamond')
        tagline.shift(DOWN * 2.9)
        self.play(FadeIn(tagline), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


class A14_LoebnerRing(Scene):
    """Doodle: contest trophy; panel of judges with 'I KNOW' badges;
    two doors with warning tags."""
    def construct(self):
        dur = 11.50
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Trophy (left)
        trophy_cup = RoundedRectangle(
            width=1.4, height=1.8, corner_radius=0.35,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 5.2 + UP * 0.5)
        trophy_base = Rectangle(
            width=1.8, height=0.35,
            color=INK, fill_color=INK, fill_opacity=0.6, stroke_width=1.5
        ).shift(LEFT * 5.2 + DOWN * 0.6)
        trophy_star = Text("★", font_size=28, color=INK, font='EB Garamond').move_to(trophy_cup)
        tph_lbl = Text("Loebner Prize\n1990", font_size=16, color=SOFT, font='EB Garamond')
        tph_lbl.next_to(trophy_base, DOWN, buff=0.12)

        self.play(DrawBorderThenFill(trophy_cup), DrawBorderThenFill(trophy_base),
                  FadeIn(trophy_star), FadeIn(tph_lbl), run_time=0.5); elapsed += 0.5

        # Panel of judges (center)
        judges = VGroup()
        for i, x in enumerate([-0.6, 0.6, 1.8]):
            head = Circle(radius=0.35, color=INK, stroke_width=2.0, fill_opacity=0)
            head.shift(RIGHT * x + UP * 1.2)
            body = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.6,
                        color=INK, stroke_width=2.0)
            judges.add(head, body)

        self.play(Create(judges), run_time=0.5); elapsed += 0.5

        # Badges: "I KNOW…" — flip up
        badges = VGroup()
        for i, x in enumerate([-0.6, 0.6, 1.8]):
            badge = RoundedRectangle(
                width=1.6, height=0.55, corner_radius=0.12,
                fill_color=INK, fill_opacity=0.85, stroke_color=INK, stroke_width=1.5
            )
            badge.shift(RIGHT * x + UP * 0.2)
            b_txt = Text("I KNOW", font_size=13, color=PAGE, weight=BOLD, font='EB Garamond')
            b_txt.move_to(badge)
            badges.add(badge, b_txt)

        self.play(FadeIn(badges), run_time=0.5); elapsed += 0.5

        # Two doors with warning tags (right side)
        for dx, lbl_txt in [(-0.8, "?"), (0.8, "?")]:
            door = RoundedRectangle(
                width=1.6, height=2.4, corner_radius=0.12,
                fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
            ).shift(RIGHT * (4.2 + dx) + DOWN * 0.3)
            q = Text(lbl_txt, font_size=44, color=INK, weight=BOLD, font='EB Garamond').move_to(door)
            warn = Text("⚠", font_size=20, color=INK, font='EB Garamond')
            warn.next_to(door, UP, buff=0.12)
            self.play(DrawBorderThenFill(door), FadeIn(q), FadeIn(warn),
                      run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


class A15_SteerAndDodge(Scene):
    """Doodle: conversation as train track; track bends toward headline magnet;
    off-track questions are deflected by swerve-arrows."""
    def construct(self):
        dur = 11.05
        elapsed = 0.0

        # Initial straight track (two parallel rails)
        rail_y_up = 0.35
        rail_y_dn = -0.35
        track_l = Line(LEFT * 5.5 + UP * rail_y_up, RIGHT * 0.5 + UP * rail_y_up,
                       color=INK, stroke_width=2.5)
        track_l2 = Line(LEFT * 5.5 + UP * rail_y_dn, RIGHT * 0.5 + UP * rail_y_dn,
                        color=INK, stroke_width=2.5)
        self.play(Create(track_l), Create(track_l2), run_time=0.5); elapsed += 0.5

        # Magnet (right side) — labeled "headline"
        mag = Circle(radius=0.7, color=SPARK, stroke_width=2.5, fill_opacity=0)
        mag.shift(RIGHT * 3.8 + UP * 0.0)
        mag_lbl = Text("headline", font_size=18, color=SPARK, weight=BOLD, font='EB Garamond')
        mag_lbl.move_to(mag)
        self.play(Create(mag), FadeIn(mag_lbl), run_time=0.4); elapsed += 0.4

        # Track bends toward magnet
        bend_top = ArcBetweenPoints(
            RIGHT * 0.5 + UP * rail_y_up, mag.get_left() + UP * 0.3,
            angle=-0.5, color=INK, stroke_width=2.5
        )
        bend_bot = ArcBetweenPoints(
            RIGHT * 0.5 + UP * rail_y_dn, mag.get_left() + DOWN * 0.3,
            angle=-0.5, color=INK, stroke_width=2.5
        )
        self.play(Create(bend_top), Create(bend_bot), run_time=0.6); elapsed += 0.6

        # Three incoming "questions" (arrows from above the track) that get deflected
        for oy in (1.8, 2.2, 2.6):
            q_arrow = Arrow(
                LEFT * (4.0 - oy * 0.4) + UP * oy,
                LEFT * (4.0 - oy * 0.4) + UP * 0.5,
                color=GHOST, stroke_width=2.0, buff=0.0
            )
            swerve = Arrow(
                LEFT * (4.0 - oy * 0.4) + UP * 0.5,
                LEFT * (4.0 - oy * 0.4) + RIGHT * 1.0 + UP * 0.5,
                color=SOFT, stroke_width=2.0, buff=0.0
            )
            self.play(GrowArrow(q_arrow), GrowArrow(swerve), run_time=0.3); elapsed += 0.3

        dodge_lbl = Text("dodge the rest", font_size=20, color=SOFT, font='EB Garamond')
        dodge_lbl.shift(DOWN * 2.9)
        self.play(FadeIn(dodge_lbl), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


class A18_PersonaWasTheTrick(Scene):
    """Doodle: boy-mask over blank machine; expectations bar dragged DOWN;
    excuse sticky-notes over the gaps."""
    def construct(self):
        dur = 10.99
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Machine box (blank)
        machine = RoundedRectangle(
            width=3.0, height=2.2, corner_radius=0.2,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 1.8 + DOWN * 0.2)
        blank_lbl = Text("—", font_size=32, color=GHOST, font='EB Garamond').move_to(machine)
        self.play(DrawBorderThenFill(machine), FadeIn(blank_lbl),
                  run_time=0.4); elapsed += 0.4

        # Boy-mask above machine
        mask_face = Circle(radius=0.75, color=INK, stroke_width=2.2, fill_opacity=0)
        mask_face.next_to(machine, UP, buff=0.2)
        eyes_l = Dot(mask_face.get_center() + LEFT * 0.27 + UP * 0.15,
                     radius=0.08, color=INK)
        eyes_r = Dot(mask_face.get_center() + RIGHT * 0.27 + UP * 0.15,
                     radius=0.08, color=INK)
        smile = Arc(radius=0.28, start_angle=-PI * 0.8, angle=PI * 0.6,
                    color=INK, stroke_width=2.0)
        smile.move_to(mask_face.get_center() + DOWN * 0.15)
        age_lbl = Text("13", font_size=26, color=SOFT, font='EB Garamond')
        age_lbl.next_to(mask_face, UP, buff=0.08)  # above not right — RIGHT landed on top of sticky note

        self.play(Create(mask_face), FadeIn(eyes_l), FadeIn(eyes_r),
                  Create(smile), FadeIn(age_lbl), run_time=0.5); elapsed += 0.5

        # Expectations bar (right side) — starts high, drops low
        bar_lbl = Text("expectations", font_size=26, color=SOFT, font='EB Garamond')
        bar_lbl.shift(RIGHT * 4.0 + UP * 2.6)
        bar_top = Line(RIGHT * 3.0 + UP * 2.2, RIGHT * 5.0 + UP * 2.2,
                       color=INK, stroke_width=2.5)
        self.play(FadeIn(bar_lbl), Create(bar_top), run_time=0.4); elapsed += 0.4

        # Bar drops
        bar_low = Line(RIGHT * 3.0 + DOWN * 1.0, RIGHT * 5.0 + DOWN * 1.0,
                       color=SPARK, stroke_width=2.5)
        drop_arrow = Arrow(RIGHT * 4.0 + UP * 2.0, RIGHT * 4.0 + DOWN * 0.8,
                           color=SPARK, stroke_width=2.5, buff=0.0)
        self.play(GrowArrow(drop_arrow), Create(bar_low),
                  run_time=0.6); elapsed += 0.6

        # Sticky-notes (excuse labels)
        for txt, pos_shift in [
            ("he's just a kid", RIGHT * 2.5 + UP * 1.5),
            ("English isn't his first language", RIGHT * 2.5 + DOWN * 0.3),
        ]:  # RIGHT side — LEFT positions straddled machine box border at x=-0.3
            note_bg = RoundedRectangle(
                width=2.8, height=0.55, corner_radius=0.1,
                fill_color=STAGE, fill_opacity=0.95, stroke_color=BORDER, stroke_width=1.5
            ).shift(pos_shift)
            note_txt = Text(txt, font_size=15, color=SOFT, font='EB Garamond').move_to(note_bg)
            self.play(FadeIn(note_bg), FadeIn(note_txt), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


class A20_NextChunk(Scene):
    """Doodle: word-globe → model blob → chunks chaining out; crossed-out costume rack."""
    def construct(self):
        dur = 10.86
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Faint word-globe (left)
        globe = Circle(radius=1.6, color=GHOST, stroke_width=1.5, fill_opacity=0)
        globe.shift(LEFT * 4.5 + DOWN * 0.0)
        for angle, word in [(PI * 0.1, "text"), (PI * 0.4, "…"), (PI * 0.7, "words"),
                             (PI * 1.0, "…"), (PI * 1.3, "more"), (PI * 1.7, "data")]:
            r = 1.3
            pos = globe.get_center() + np.array([r * np.cos(angle), r * np.sin(angle), 0])
            wt = Text(word, font_size=14, color=SOFT, font='EB Garamond').move_to(pos)  # GHOST too low-contrast vs PAGE
            globe.add(wt)
        self.play(FadeIn(globe), run_time=0.5); elapsed += 0.5

        # Arrow to model blob
        feed_arr = Arrow(LEFT * 2.6, LEFT * 0.9,
                         color=SOFT, stroke_width=2.0, buff=0.0)
        self.play(GrowArrow(feed_arr), run_time=0.3); elapsed += 0.3

        # Model blob (rounded rectangle)
        model = RoundedRectangle(
            width=2.2, height=1.6, corner_radius=0.5,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 0.0 + DOWN * 0.0)
        model_lbl = Text("model", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        model_lbl.move_to(model)
        self.play(DrawBorderThenFill(model), FadeIn(model_lbl), run_time=0.4); elapsed += 0.4

        # Chunks popping out to the right (chain)
        prev_x = 1.3
        for i, chunk in enumerate(["chunk", "chunk"]):
            out_arr = Arrow(
                RIGHT * prev_x + DOWN * 0.0,
                RIGHT * (prev_x + 0.8) + DOWN * 0.0,
                color=INK, stroke_width=2.0, buff=0.0
            )
            chunk_box = RoundedRectangle(
                width=1.3, height=0.75, corner_radius=0.12,
                fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=1.5
            ).shift(RIGHT * (prev_x + 0.8 + 0.65) + DOWN * 0.0)
            chunk_lbl = Text(chunk, font_size=16, color=SOFT, font='EB Garamond')
            chunk_lbl.move_to(chunk_box)
            self.play(GrowArrow(out_arr), DrawBorderThenFill(chunk_box),
                      FadeIn(chunk_lbl), run_time=0.28); elapsed += 0.28
            prev_x = prev_x + 0.8 + 1.3

        # Crossed-out costume rack (bottom left, small)
        rack_pos = np.array([-5.0, -2.2, 0])  # was -2.8: bottom at -3.5, label fell to -3.77 (outside ±3.4)
        rack = RoundedRectangle(
            width=1.4, height=1.4, corner_radius=0.12,
            fill_color=GHOST, fill_opacity=0.4, stroke_color=GHOST, stroke_width=1.5
        ).move_to(rack_pos)
        rack_lbl = Text("script", font_size=14, color=GHOST, font='EB Garamond')
        rack_lbl.next_to(rack, DOWN, buff=0.1)
        cross_a = Line(rack_pos + np.array([-0.7, 0.7, 0]),
                       rack_pos + np.array([0.7, -0.7, 0]),
                       color=SPARK, stroke_width=2.5)
        cross_b = Line(rack_pos + np.array([-0.7, -0.7, 0]),
                       rack_pos + np.array([0.7, 0.7, 0]),
                       color=SPARK, stroke_width=2.5)
        self.play(DrawBorderThenFill(rack), FadeIn(rack_lbl),
                  Create(cross_a), Create(cross_b), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


class A22_JuiceSentence(Scene):
    """Doodle: juice from fridge → 'him' figure → calendar '?'; tangled pronoun arrow
    snaps straight; tiny world-globe 'knowledge you already have'."""
    def construct(self):
        dur = 11.01
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Fridge (left)
        fridge = RoundedRectangle(
            width=1.5, height=2.4, corner_radius=0.12,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 5.2 + UP * 0.2)
        fridge_lbl = Text("fridge", font_size=16, color=SOFT, font='EB Garamond')
        fridge_lbl.next_to(fridge, DOWN, buff=0.15)
        juice = Text("🧃", font_size=24, font='EB Garamond').move_to(fridge)
        self.play(DrawBorderThenFill(fridge), FadeIn(juice),
                  FadeIn(fridge_lbl), run_time=0.4); elapsed += 0.4

        # Arrow: fridge → "him" figure
        arr1 = Arrow(fridge.get_right(), LEFT * 2.8 + UP * 0.2,
                     color=INK, stroke_width=2.0, buff=0.1)
        self.play(GrowArrow(arr1), run_time=0.3); elapsed += 0.3

        # "him?" figure
        him_head = Circle(radius=0.42, color=INK, stroke_width=2.0, fill_opacity=0)
        him_head.shift(LEFT * 2.0 + UP * 0.85)
        him_body = Line(him_head.get_bottom(), him_head.get_bottom() + DOWN * 0.7,
                        color=INK, stroke_width=2.0)
        him_q = Text("him?", font_size=18, color=INK, weight=BOLD, font='EB Garamond')
        him_q.next_to(him_head, RIGHT, buff=0.12)
        self.play(Create(him_head), Create(him_body), FadeIn(him_q),
                  run_time=0.4); elapsed += 0.4

        # Calendar (right) with "?"
        cal = RoundedRectangle(
            width=1.8, height=1.8, corner_radius=0.12,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(RIGHT * 3.8 + UP * 0.2)
        cal_top = Rectangle(
            width=1.8, height=0.45,
            color=INK, fill_color=INK, fill_opacity=0.6, stroke_width=1.5
        ).shift(RIGHT * 3.8 + UP * 1.1)
        cal_q = Text("date?", font_size=22, color=INK, weight=BOLD, font='EB Garamond').move_to(cal)
        self.play(DrawBorderThenFill(cal), DrawBorderThenFill(cal_top),
                  FadeIn(cal_q), run_time=0.4); elapsed += 0.4

        # Tangled pronoun arrow (initially messy)
        tangled = CurvedArrow(
            him_head.get_right() + RIGHT * 0.1,
            fridge.get_top() + UP * 0.1,
            angle=-2.0, color=GHOST, stroke_width=1.8
        )
        self.play(Create(tangled), run_time=0.5); elapsed += 0.5

        # World-globe (knowledge) — bottom
        globe = Circle(radius=0.45, color=SOFT, stroke_width=1.8, fill_opacity=0)
        globe.shift(DOWN * 2.5 + LEFT * 1.0)
        globe_lbl = Text("knowledge you already have", font_size=16, color=SOFT, font='EB Garamond')
        globe_lbl.next_to(globe, RIGHT, buff=0.15)
        self.play(Create(globe), FadeIn(globe_lbl), run_time=0.3); elapsed += 0.3

        # Arrow snaps straight (they parse it now)
        straight = Arrow(
            him_head.get_right() + RIGHT * 0.1,
            fridge.get_right() + UP * 0.3,
            color=INK, stroke_width=2.5, buff=0.0
        )
        parsed = Text("they parse it now", font_size=20, color=INK, weight=BOLD, font='EB Garamond')
        parsed.shift(UP * 2.6)
        self.play(Transform(tangled, straight), FadeIn(parsed), run_time=0.5); elapsed += 0.5

        self.wait(dur - elapsed)


class A23_NoGimmick(Scene):
    """Doodle: machine with open empty hands; boy-mask dropped on floor;
    narrow rail widens to open road; 5-min clock."""
    def construct(self):
        dur = 9.41
        elapsed = 0.0

        # Machine (open arms)
        body = RoundedRectangle(
            width=2.2, height=1.8, corner_radius=0.2,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(UP * 0.3)
        arm_l = Arrow(body.get_left(), body.get_left() + LEFT * 1.2 + UP * 0.6,
                      color=INK, stroke_width=2.2, buff=0.0)
        arm_r = Arrow(body.get_right(), body.get_right() + RIGHT * 1.2 + UP * 0.6,
                      color=INK, stroke_width=2.2, buff=0.0)
        hands_lbl = Text("(open hands)", font_size=16, color=GHOST, font='EB Garamond')
        hands_lbl.next_to(body, UP, buff=1.0)
        self.play(DrawBorderThenFill(body), Create(arm_l), Create(arm_r),
                  FadeIn(hands_lbl), run_time=0.5); elapsed += 0.5

        # Boy-mask dropped on floor
        mask = Circle(radius=0.40, color=GHOST, stroke_width=1.8, fill_opacity=0)
        mask.shift(LEFT * 3.5 + DOWN * 2.6)
        mask_lbl = Text("persona", font_size=14, color=GHOST, font='EB Garamond')
        mask_lbl.next_to(mask, DOWN, buff=0.1)
        drop_line = DashedLine(LEFT * 3.5 + DOWN * 0.5, LEFT * 3.5 + DOWN * 2.1,
                               color=GHOST, stroke_width=1.5)
        self.play(Create(drop_line), Create(mask), FadeIn(mask_lbl),
                  run_time=0.4); elapsed += 0.4

        # Narrow rail → widens to open road
        rail_l = Line(RIGHT * 0.8 + DOWN * 2.2, RIGHT * 0.8 + UP * 2.2,
                      color=INK, stroke_width=2.5)
        rail_r = Line(RIGHT * 1.6 + DOWN * 2.2, RIGHT * 1.6 + UP * 2.2,
                      color=INK, stroke_width=2.5)
        self.play(Create(rail_l), Create(rail_r), run_time=0.3); elapsed += 0.3

        road_l = Line(RIGHT * 2.4 + DOWN * 2.6, RIGHT * 5.0 + DOWN * 2.6,
                      color=INK, stroke_width=2.5)
        road_r = Line(RIGHT * 2.4 + UP * 2.6, RIGHT * 5.0 + UP * 2.6,
                      color=INK, stroke_width=2.5)  # was ±3.2 — above/below title-safe boundary
        open_lbl = Text("it just answers", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        open_lbl.shift(RIGHT * 3.8 + DOWN * 0.0)
        self.play(Create(road_l), Create(road_r), FadeIn(open_lbl),
                  run_time=0.5); elapsed += 0.5

        # 5-min clock (top right)
        clk = Circle(radius=0.65, color=INK, stroke_width=2.0, fill_opacity=0)
        clk.shift(RIGHT * 5.5 + UP * 2.3)  # was UP*3.0 — top at 3.65 > frame height 3.5
        clk_h = Line(clk.get_center(), clk.get_center() + UP * 0.45,
                     color=INK, stroke_width=2.2)
        clk_m = Line(clk.get_center(), clk.get_center() + RIGHT * 0.42,
                     color=INK, stroke_width=2.0)
        clk_lbl = Text("5 min", font_size=16, color=SOFT, font='EB Garamond')
        clk_lbl.next_to(clk, DOWN, buff=0.12)
        self.play(Create(clk), Create(clk_h), Create(clk_m), FadeIn(clk_lbl),
                  run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


class A25_ThreeParty(Scene):
    """Doodle: judge center; two chat panels flanking (human left, machine right);
    5-min clock; pointing hand."""
    def construct(self):
        dur = 12.37
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Judge (center)
        judge_head = Circle(radius=0.55, color=INK, stroke_width=2.2, fill_opacity=0)
        judge_head.shift(UP * 1.0)
        judge_body = Line(judge_head.get_bottom(), judge_head.get_bottom() + DOWN * 1.0,
                          color=INK, stroke_width=2.2)
        judge_lbl = Text("judge", font_size=18, color=SOFT, font='EB Garamond')
        judge_lbl.next_to(judge_head, UP, buff=0.18)
        self.play(Create(judge_head), Create(judge_body),
                  FadeIn(judge_lbl), run_time=0.4); elapsed += 0.4

        # Two chat panels opening simultaneously
        panel_l = RoundedRectangle(
            width=3.0, height=3.8, corner_radius=0.2,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(LEFT * 4.0 + DOWN * 0.2)
        human_icon = Circle(radius=0.45, color=INK, stroke_width=2.0, fill_opacity=0)
        human_icon.move_to(panel_l.get_center() + UP * 0.8)
        human_body_line = Line(human_icon.get_bottom(), human_icon.get_bottom() + DOWN * 0.7,
                               color=INK, stroke_width=2.0)
        human_tag = Text("human", font_size=18, color=INK, weight=BOLD, font='EB Garamond')
        human_tag.next_to(panel_l, DOWN, buff=0.18)

        panel_r = RoundedRectangle(
            width=3.0, height=3.8, corner_radius=0.2,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(RIGHT * 4.0 + DOWN * 0.2)
        mach_lbl = Text("⟨machine⟩", font_size=20, color=INK, weight=BOLD, font='EB Garamond')
        mach_lbl.move_to(panel_r.get_center() + UP * 0.2)
        mach_tag = Text("machine", font_size=18, color=INK, weight=BOLD, font='EB Garamond')
        mach_tag.next_to(panel_r, DOWN, buff=0.18)

        self.play(
            DrawBorderThenFill(panel_l), Create(human_icon),
            Create(human_body_line), FadeIn(human_tag),
            DrawBorderThenFill(panel_r), FadeIn(mach_lbl), FadeIn(mach_tag),
            run_time=0.7
        ); elapsed += 0.7

        # Connection lines from judge to panels
        conn_l = DashedLine(judge_head.get_left(), panel_l.get_right() + UP * 0.5,
                            color=BORDER, stroke_width=1.8)
        conn_r = DashedLine(judge_head.get_right(), panel_r.get_left() + UP * 0.5,
                            color=BORDER, stroke_width=1.8)
        self.play(Create(conn_l), Create(conn_r), run_time=0.4); elapsed += 0.4

        # Clock
        clk_pos = np.array([0, 2.2, 0])  # was 3.2 — clock top (3.2+0.7=3.9) exceeded frame height 3.5
        clk = Circle(radius=0.7, color=INK, stroke_width=2.0, fill_opacity=0)
        clk.move_to(clk_pos)
        clk_h = Line(clk_pos, clk_pos + UP * 0.5, color=INK, stroke_width=2.2)
        clk_m = Line(clk_pos, clk_pos + RIGHT * 0.48, color=INK, stroke_width=2.0)
        clk_lbl = Text("5 min", font_size=18, color=SOFT, font='EB Garamond')
        clk_lbl.next_to(clk, DOWN, buff=0.1)
        self.play(Create(clk), Create(clk_h), Create(clk_m),
                  FadeIn(clk_lbl), run_time=0.4); elapsed += 0.4

        # Pointing hand / question mark between panels
        pick_q = Text("which is human?", font_size=20, color=INK, weight=BOLD, font='EB Garamond')
        pick_q.shift(DOWN * 2.8)
        self.play(FadeIn(pick_q), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)


class A27_YesTheyPass(Scene):
    """Doodle: check mark stamps down over two doors; row of judge faces with
    question marks ('can't tell')."""
    def construct(self):
        dur = 7.47
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Two doors (simplified)
        door_l = RoundedRectangle(
            width=2.2, height=3.0, corner_radius=0.14,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(LEFT * 2.2 + DOWN * 0.2)
        ql = Text("?", font_size=56, color=INK, weight=BOLD, font='EB Garamond').move_to(door_l)
        door_r = RoundedRectangle(
            width=2.2, height=3.0, corner_radius=0.14,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.2
        ).shift(RIGHT * 2.2 + DOWN * 0.2)
        qr = Text("machine", font_size=20, color=INK, weight=BOLD, font='EB Garamond').move_to(door_r)

        self.play(DrawBorderThenFill(door_l), FadeIn(ql),
                  DrawBorderThenFill(door_r), FadeIn(qr), run_time=0.4); elapsed += 0.4

        # Check stamp — FadeIn at final position (no off-frame start)
        check = Text("✓", font_size=120, color=INK, weight=BOLD, font='EB Garamond')
        check.move_to(ORIGIN + UP * 0.2)
        self.play(FadeIn(check, scale=1.4), run_time=0.5); elapsed += 0.5

        # Row of judge faces — shrugging
        for x in (-4.8, -3.0, -1.2, 0.6):
            head = Circle(radius=0.32, color=SOFT, stroke_width=1.8, fill_opacity=0)
            head.shift(UP * 2.8 + RIGHT * x)
            shrug = Text("?", font_size=18, color=SOFT, font='EB Garamond')
            shrug.move_to(head)
            self.play(Create(head), FadeIn(shrug), run_time=0.15); elapsed += 0.15

        cant_tell = Text("can't tell", font_size=22, color=SOFT, font='EB Garamond')
        cant_tell.shift(LEFT * 2.4 + UP * 2.0)
        self.play(FadeIn(cant_tell), run_time=0.3); elapsed += 0.3

        # Verdict
        verdict = Text("the machines pass", font_size=30, color=INK, weight=BOLD, font='EB Garamond')
        verdict.shift(DOWN * 2.9)
        self.play(FadeIn(verdict), run_time=0.4); elapsed += 0.4

        self.wait(dur - elapsed)


class A28_HandsItBack(Scene):
    """Doodle: Turing swaps 'can it think?' (heavy) for 'can it fool you?' (light);
    machine clears the light box; heavy box slides back with return-arrow."""
    def construct(self):
        dur = 10.33
        elapsed = 0.0
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)
        elapsed += _pre

        # Heavy box "can it think?" — starts left
        heavy = RoundedRectangle(
            width=3.0, height=2.0, corner_radius=0.18,
            fill_color=INK, fill_opacity=0.85, stroke_color=INK, stroke_width=2.5
        ).shift(LEFT * 4.0 + UP * 0.5)
        heavy_lbl = Text("can it think?", font_size=20, color=PAGE, weight=BOLD, font='EB Garamond')
        heavy_lbl.move_to(heavy)
        heavy_weight = Text("(hard)", font_size=15, color=GHOST, font='EB Garamond')
        heavy_weight.next_to(heavy, DOWN, buff=0.12)

        self.play(DrawBorderThenFill(heavy), FadeIn(heavy_lbl),
                  FadeIn(heavy_weight), run_time=0.4); elapsed += 0.4

        # Swap arrows (Turing trades)
        swap_arr = Arrow(LEFT * 2.3 + UP * 0.5, LEFT * 0.3 + UP * 0.5,
                         color=SOFT, stroke_width=2.0, buff=0.0)
        self.play(GrowArrow(swap_arr), run_time=0.3); elapsed += 0.3

        # Light box "can it fool you?" — center
        light = RoundedRectangle(
            width=3.0, height=2.0, corner_radius=0.18,
            fill_color=STAGE, fill_opacity=1, stroke_color=INK, stroke_width=2.0
        ).shift(RIGHT * 1.2 + UP * 0.5)
        light_lbl = Text("can it fool you?", font_size=20, color=INK, weight=BOLD, font='EB Garamond')
        light_lbl.move_to(light)
        light_weight = Text("(lighter)", font_size=15, color=SOFT, font='EB Garamond')
        light_weight.next_to(light, DOWN, buff=0.12)

        self.play(DrawBorderThenFill(light), FadeIn(light_lbl),
                  FadeIn(light_weight), run_time=0.4); elapsed += 0.4

        # Machine clears light box (check mark)
        check_sm = Text("✓", font_size=50, color=INK, weight=BOLD, font='EB Garamond')
        check_sm.next_to(light, UP, buff=0.2)  # was RIGHT — lands at x=3.0, same as heavy_back left edge
        self.play(FadeIn(check_sm, scale=1.3), run_time=0.4); elapsed += 0.4

        # Heavy box slides back in — arrow must end at box left edge, not center (avoids label overlap)
        heavy_back = RoundedRectangle(
            width=3.0, height=2.0, corner_radius=0.18,
            fill_color=INK, fill_opacity=0.85, stroke_color=INK, stroke_width=2.5
        ).shift(RIGHT * 4.5 + UP * 0.5)
        heavy_back_lbl = Text("can it think?", font_size=20, color=PAGE, weight=BOLD, font='EB Garamond')
        heavy_back_lbl.move_to(heavy_back)
        return_arr = Arrow(RIGHT * 6.2 + UP * 0.5, heavy_back.get_left(),
                           color=INK, stroke_width=2.8, buff=0.15)

        self.play(GrowArrow(return_arr), FadeIn(heavy_back),
                  FadeIn(heavy_back_lbl), run_time=0.7); elapsed += 0.7

        hands_it = Text("hands it back", font_size=22, color=INK, weight=BOLD, font='EB Garamond')
        hands_it.shift(DOWN * 2.9)
        self.play(FadeIn(hands_it), run_time=0.3); elapsed += 0.3

        self.wait(dur - elapsed)
