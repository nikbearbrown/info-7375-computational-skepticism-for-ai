from manim import *
import numpy as np

# ── Palette ──────────────────────────────────────────────────────────────────
BG    = "#FAF9F5"
INK   = "#3D3929"
ACC   = "#D97757"
SOFT  = "#73705F"
GHOST = "#A9A491"


# ── B05_WinTally ─────────────────────────────────────────────────────────────
class B05_WinTally(Scene):
    """Isotype tally: 5 wins / 3 losses / 1 tie, then ring on 3 wins.
    Duration ~11s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Invited Scoreboard", font="Georgia", color=INK,
                     font_size=36).to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.6)

        # Build rows
        def make_circle(fill, stroke):
            return Circle(radius=0.22, fill_color=fill, fill_opacity=1,
                          stroke_color=stroke, stroke_width=2)

        rows = []
        configs = [
            ("W", 5, ACC,   INK,  "wins"),
            ("L", 3, GHOST, SOFT, "losses"),
            ("T", 1, INK,   INK,  "tie"),
        ]

        group_vobjs = []
        for row_idx, (letter, count, fill, stroke, label_text) in enumerate(configs):
            circles = VGroup(*[make_circle(fill, stroke) for _ in range(count)])
            circles.arrange(RIGHT, buff=0.18)
            row_label = Text(f"{letter}  {count}  {label_text}", font="Georgia",
                             color=SOFT, font_size=22)
            row_label.next_to(circles, RIGHT, buff=0.35)
            row_group = VGroup(circles, row_label)
            row_group.move_to(UP * (0.7 - row_idx * 1.0))
            group_vobjs.append((circles, row_group))

        for circles, row_group in group_vobjs:
            self.play(FadeIn(row_group), run_time=0.5)
            self.wait(0.3)

        self.wait(0.5)

        # Draw terracotta ring around first 3 win circles
        win_circles = group_vobjs[0][0]
        target_circles = VGroup(*[win_circles[i] for i in range(3)])
        ring = SurroundingRectangle(target_circles, color=ACC, buff=0.12,
                                    corner_radius=0.25, stroke_width=3)
        contamination_label = Text("contamination?", font="Georgia",
                                   color=ACC, font_size=22)
        contamination_label.next_to(ring, DOWN, buff=0.18)

        self.play(Create(ring), run_time=0.8)
        self.play(FadeIn(contamination_label), run_time=0.5)
        self.wait(1.5)


# ── B10_FootnoteReveal ────────────────────────────────────────────────────────
class B10_FootnoteReveal(Scene):
    """Two-column header, starred cell, footnote fade, terracotta underline.
    Duration ~12s."""

    def construct(self):
        self.camera.background_color = BG

        # Column headers
        col_cheaper = Text("THE CHEAPER MODEL", font="Georgia", color=SOFT,
                           font_size=26)
        col_premium = Text("THE PREMIUM MODEL", font="Georgia", color=INK,
                           font_size=26)
        col_cheaper.move_to(LEFT * 3 + UP * 2.0)
        col_premium.move_to(RIGHT * 1.8 + UP * 2.0)

        divider = Line(UP * 2.5 + ORIGIN, DOWN * 0.5 + ORIGIN,
                       color=SOFT, stroke_width=1.5).shift(LEFT * 0.5)

        self.play(FadeIn(col_cheaper), FadeIn(col_premium),
                  Create(divider), run_time=0.7)
        self.wait(0.3)

        # Starred cell in the premium column
        star_cell = Text("† ████████", font="Georgia", color=INK, font_size=32)
        star_cell.move_to(RIGHT * 1.8 + UP * 0.8)
        self.play(FadeIn(star_cell), run_time=0.5)
        self.wait(0.4)

        # Footnote fades in
        footnote = Text("† = unrestricted variant (not the product in the price row)",
                        font="Georgia", color=SOFT, font_size=19)
        footnote.move_to(DOWN * 0.8)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.7)
        self.wait(0.5)

        # Terracotta underline draws under starred cell
        underline = Line(
            star_cell.get_left() + DOWN * 0.28,
            star_cell.get_right() + DOWN * 0.28,
            color=ACC, stroke_width=4
        )
        self.play(Create(underline), run_time=0.7)
        self.wait(0.3)

        # Bottom serif label
        serif_label = Text("this cell ≠ the product you priced",
                           font="Georgia", color=ACC, font_size=22)
        serif_label.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(serif_label), run_time=0.6)
        self.wait(1.5)


# ── B16_HarnessEquation ───────────────────────────────────────────────────────
class B16_HarnessEquation(Scene):
    """Equation builds term by term; harness+fallback recolor to ACC.
    Duration ~13s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("What was scored", font="Georgia", color=SOFT,
                     font_size=30).to_edge(UP, buff=0.75)
        self.play(FadeIn(title), run_time=0.5)

        # Build equation piece by piece
        t_score   = Text("score", font="Georgia", color=INK, font_size=48)
        t_eq      = Text(" = ", font="Georgia", color=SOFT, font_size=48)
        t_f       = Text("f( ", font="Georgia", color=INK, font_size=48)
        t_model   = Text("model", font="Georgia", color=INK, font_size=48)
        t_comma1  = Text(",  ", font="Georgia", color=SOFT, font_size=48)
        t_harness = Text("harness", font="Georgia", color=INK, font_size=48)
        t_comma2  = Text(",  ", font="Georgia", color=SOFT, font_size=48)
        t_fallback = Text("fallback", font="Georgia", color=INK, font_size=48)
        t_close   = Text(" )", font="Georgia", color=INK, font_size=48)

        eq = VGroup(t_score, t_eq, t_f, t_model, t_comma1,
                    t_harness, t_comma2, t_fallback, t_close)
        eq.arrange(RIGHT, buff=0.05)
        eq.move_to(ORIGIN)

        terms = [t_score, t_eq, t_f, t_model, t_comma1,
                 t_harness, t_comma2, t_fallback, t_close]
        for term in terms:
            term.set_opacity(0)
        self.add(*terms)

        for term in terms:
            self.play(term.animate.set_opacity(1), run_time=0.35)
            self.wait(0.15)

        self.wait(0.4)

        # Recolor harness and fallback to terracotta — no scale (buff=0.05 row; scale bleeds into neighbors)
        self.play(
            t_harness.animate.set_color(ACC),
            t_fallback.animate.set_color(ACC),
            run_time=0.5
        )
        self.wait(0.4)

        serif_label = Text("the model column hides these two terms",
                           font="Georgia", color=ACC, font_size=22)
        serif_label.next_to(eq, DOWN, buff=0.55)
        self.play(FadeIn(serif_label), run_time=0.6)
        self.wait(1.5)


# ── B19_EffortDials ───────────────────────────────────────────────────────────
class B19_EffortDials(Scene):
    """Two arc-based gauge dials at different effort settings.
    Duration ~14s."""

    def construct(self):
        self.camera.background_color = BG

        def make_dial(label_text, fraction, color, center):
            """fraction: 0.0–1.0 position of needle along arc."""
            # Arc background
            arc_bg = Arc(radius=1.2, start_angle=PI * 0.85,
                         angle=-PI * 0.7, color=GHOST, stroke_width=8)
            arc_bg.move_arc_center_to(center)

            # Filled arc
            filled_angle = PI * 0.7 * fraction
            arc_fill = Arc(radius=1.2, start_angle=PI * 0.85,
                           angle=-filled_angle, color=color, stroke_width=8)
            arc_fill.move_arc_center_to(center)

            # Needle
            needle_angle = PI * 0.85 - filled_angle
            needle_end = center + 1.0 * np.array([
                np.cos(needle_angle), np.sin(needle_angle), 0])
            needle = Line(center, needle_end, color=INK, stroke_width=4)
            needle_dot = Dot(center, color=INK, radius=0.08)

            # Label
            dial_label = Text(label_text, font="Georgia", color=INK,
                              font_size=22)
            dial_label.move_to(center + DOWN * 1.55)

            return VGroup(arc_bg, arc_fill, needle, needle_dot), dial_label

        left_center  = LEFT * 3.2 + UP * 0.3
        right_center = RIGHT * 3.2 + UP * 0.3

        left_dial,  left_label  = make_dial("the premium model",  0.88, INK, left_center)
        right_dial, right_label = make_dial("the cheaper model",  0.22, GHOST, right_center)

        self.play(Create(left_dial[0]), Create(right_dial[0]), run_time=0.5)
        self.play(
            Create(left_dial[1]),  Create(left_dial[2]),
            Create(left_dial[3]),
            Create(right_dial[1]), Create(right_dial[2]),
            Create(right_dial[3]),
            run_time=1.0
        )
        self.play(FadeIn(left_label), FadeIn(right_label), run_time=0.5)
        self.wait(0.5)

        # Center label
        center_label = Text("not the same race", font="Georgia",
                            color=INK, font_size=28)
        center_label.move_to(UP * 0.3)
        self.play(FadeIn(center_label), run_time=0.6)
        self.wait(0.5)

        caption = Text("(illustrative effort levels)", font="Georgia",
                       color=SOFT, font_size=20)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2.0)


# ── B20_NonMonotonicCurve ─────────────────────────────────────────────────────
class B20_NonMonotonicCurve(Scene):
    """Non-monotonic score vs compute curve with terracotta dot.
    Duration ~13s."""

    def construct(self):
        self.camera.background_color = BG

        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=8,
            y_length=5,
            axis_config={"color": SOFT, "stroke_width": 2,
                         "include_ticks": False},
            tips=True,
        )
        axes.move_to(ORIGIN + DOWN * 0.3)

        x_label = Text("compute budget →", font="Georgia",
                       color=SOFT, font_size=20)
        x_label.next_to(axes, DOWN, buff=0.15)
        y_label = Text("score →", font="Georgia", color=SOFT, font_size=20)
        y_label.next_to(axes, LEFT, buff=0.1)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=0.8)

        # Non-monotonic path: rises, dips, rises again
        # Points in axes coordinates
        curve_points_ax = [
            [0.5, 1.5], [2.0, 5.5], [3.5, 6.8], [4.5, 5.2],
            [5.5, 4.6], [6.5, 6.5], [8.0, 8.5], [9.0, 9.0]
        ]
        curve_points = [axes.c2p(x, y) for x, y in curve_points_ax]

        curve = VMobject(color=INK, stroke_width=3)
        curve.set_points_smoothly(curve_points)

        self.play(Create(curve), run_time=1.8)
        self.wait(0.3)

        # Terracotta dot at the dip region (~x=5.0, y=4.6)
        dot_pos = axes.c2p(5.0, 4.6)
        dot = Dot(dot_pos, color=ACC, radius=0.12)
        dot_label = Text("arbitrary\nmeasurement choice", font="Georgia",
                         color=ACC, font_size=18)
        dot_label.next_to(dot, RIGHT, buff=0.2)

        self.play(GrowFromCenter(dot), run_time=0.5)
        self.play(FadeIn(dot_label), run_time=0.5)
        self.wait(0.4)

        serif_label = Text("where you measure determines the winner",
                           font="Georgia", color=INK, font_size=22)
        serif_label.to_edge(UP, buff=0.7)
        self.play(FadeIn(serif_label), run_time=0.6)
        self.wait(1.9)


# ── B25_CostFormula ───────────────────────────────────────────────────────────
class B25_CostFormula(Scene):
    """Cost-per-task formula builds term by term; pass_rate in ACC.
    Duration ~16s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("The True Cost Formula", font="Georgia", color=INK,
                     font_size=34).to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.6)

        # Terms
        segments = [
            ("cost/task", INK),
            ("  =  ", SOFT),
            ("(price/token × tokens)", INK),
            ("  ÷  pass_rate", ACC),
            ("  ×  (1 + retries)", INK),
        ]

        term_mobjects = []
        for text, color in segments:
            t = Text(text, font="Georgia", color=color, font_size=38)
            term_mobjects.append(t)

        # Arrange in two lines: first 3 terms, then next 2
        line1 = VGroup(*term_mobjects[:3]).arrange(RIGHT, buff=0.05)
        line2 = VGroup(*term_mobjects[3:]).arrange(RIGHT, buff=0.05)
        line1.move_to(UP * 0.6)
        line2.next_to(line1, DOWN, buff=0.45)

        for t in term_mobjects:
            t.set_opacity(0)
        self.add(*term_mobjects)

        # Reveal line 1 terms
        for t in term_mobjects[:3]:
            self.play(t.animate.set_opacity(1), run_time=0.5)
            self.wait(0.3)

        # Reveal line 2 terms
        for t in term_mobjects[3:]:
            self.play(t.animate.set_opacity(1), run_time=0.5)
            self.wait(0.3)

        self.wait(0.4)

        # Pulse on pass_rate term (term_mobjects[3])
        pass_term = term_mobjects[3]
        self.play(pass_term.animate.scale(1.1), run_time=0.3)
        self.play(pass_term.animate.scale(1.0 / 1.1), run_time=0.3)

        # Serif label below
        serif_label = Text("this denominator can flip the ranking",
                           font="Georgia", color=ACC, font_size=22)
        serif_label.next_to(line2, DOWN, buff=0.5)
        self.play(FadeIn(serif_label), run_time=0.6)
        self.wait(2.0)


# ── B26_CostBars ──────────────────────────────────────────────────────────────
class B26_CostBars(Scene):
    """Two scenario bar charts showing per-task cost ranking reversal.
    Duration ~14s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Per-Task Cost (illustrative)", font="Georgia",
                     color=INK, font_size=32).to_edge(UP, buff=0.45)
        self.play(FadeIn(title), run_time=0.5)

        # Scenario A: cheaper-token model has HIGHER per-task cost (bad)
        #             premium model has LOWER per-task cost
        # Scenario B: cheaper-token model has LOWER per-task cost (good)
        #             premium model has HIGHER per-task cost

        def bar(height, color, label_text, x_center, y_base=-1.8):
            rect = Rectangle(width=0.9, height=height,
                             fill_color=color, fill_opacity=0.85,
                             stroke_color=color, stroke_width=1.5)
            rect.move_to(np.array([x_center, y_base + height / 2, 0]))
            lbl = Text(label_text, font="Georgia", color=INK, font_size=17)
            lbl.move_to(np.array([x_center, y_base - 0.28, 0]))
            return VGroup(rect, lbl)

        # Scenario A — left pair
        # x-centers 2.0 apart (was 1.3) so labels (1.5-1.7 wide) don't overlap
        a_cheap   = bar(3.4, GHOST, "cheaper/token", -4.85)
        a_premium = bar(2.0, INK,   "premium/token", -2.85)
        scenario_a_label = Text("Scenario A", font="Georgia",
                                color=SOFT, font_size=20)
        scenario_a_label.move_to(LEFT * 3.85 + UP * 2.2)  # midpoint of -4.85/-2.85

        # Scenario B — right pair (ranking reversed)
        b_cheap   = bar(1.6, GHOST, "cheaper/token", 1.85)
        b_premium = bar(3.0, INK,   "premium/token", 3.85)
        scenario_b_label = Text("Scenario B", font="Georgia",
                                color=SOFT, font_size=20)
        scenario_b_label.move_to(RIGHT * 2.85 + UP * 2.2)  # midpoint of 1.85/3.85

        # Arrow between scenarios
        arrow = Arrow(LEFT * 1.0 + UP * 0.6, RIGHT * 1.0 + UP * 0.6,
                      color=ACC, stroke_width=3, buff=0.1)
        arrow_label = Text("ranking reverses", font="Georgia",
                           color=ACC, font_size=20)
        arrow_label.next_to(arrow, UP, buff=0.1)

        self.play(FadeIn(scenario_a_label), Create(a_cheap),
                  Create(a_premium), run_time=0.8)
        self.wait(0.5)
        self.play(GrowArrow(arrow), FadeIn(arrow_label), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(scenario_b_label), Create(b_cheap),
                  Create(b_premium), run_time=0.8)
        self.wait(0.5)

        # Split at the em-dash so inter-phrase gap is explicit (buff=0.22 ≈ 60 px at 4K)
        # — prevents the Georgia 'a'→consonant sidebearing from being mistaken for a
        #   word space after downscale / H.264 compression.
        cap_left  = Text("(NOT real measurements", font="Georgia", color=SOFT, font_size=18)
        cap_right = Text("— mechanism only)", font="Georgia", color=SOFT, font_size=18)
        caption = VGroup(cap_left, cap_right).arrange(RIGHT, buff=0.22)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(1.5)


# ── B33_ComplianceGate ────────────────────────────────────────────────────────
class B33_ComplianceGate(Scene):
    """Decision diamond: Can you deploy it? YES → capability. NO → lead = 0.
    Duration ~11s."""

    def construct(self):
        self.camera.background_color = BG

        # Diamond — kept narrower to stay inside safe area
        diamond = Polygon(
            UP * 1.0, RIGHT * 1.7, DOWN * 1.0, LEFT * 1.7,
            fill_color=BG, fill_opacity=1,
            stroke_color=INK, stroke_width=3
        )
        diamond.move_to(UP * 0.5)
        question = Text("Can you deploy it?", font="Georgia",
                        color=INK, font_size=24)
        question.move_to(diamond.get_center())

        self.play(Create(diamond), FadeIn(question), run_time=0.8)
        self.wait(0.3)

        # YES arrow → RIGHT → capability box
        yes_start = diamond.get_right()
        yes_end   = yes_start + RIGHT * 1.8
        yes_arrow = Arrow(yes_start, yes_end, color=INK,
                          stroke_width=3, buff=0.05)
        yes_label = Text("YES", font="Georgia", color=INK, font_size=22)
        yes_label.next_to(yes_arrow, UP, buff=0.1)

        cap_box = RoundedRectangle(width=2.0, height=0.9, corner_radius=0.15,
                                   fill_color=BG, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2)
        cap_box.next_to(yes_end, RIGHT, buff=0.1)
        cap_text = Text("capability\nanalysis begins", font="Georgia",
                        color=INK, font_size=22)
        cap_text.move_to(cap_box.get_center())

        self.play(GrowArrow(yes_arrow), FadeIn(yes_label), run_time=0.5)
        self.play(Create(cap_box), FadeIn(cap_text), run_time=0.5)
        self.wait(0.3)

        # NO arrow → DOWN → zero box (terracotta)
        no_start = diamond.get_bottom()
        no_end   = no_start + DOWN * 1.8
        no_arrow = Arrow(no_start, no_end, color=ACC,
                         stroke_width=3, buff=0.05)
        no_label = Text("NO", font="Georgia", color=ACC, font_size=22)
        no_label.next_to(no_arrow, RIGHT, buff=0.1)

        zero_box = RoundedRectangle(width=3.0, height=0.9, corner_radius=0.15,
                                    fill_color=BG, fill_opacity=1,
                                    stroke_color=ACC, stroke_width=2)
        zero_box.next_to(no_end, DOWN, buff=0.1)
        zero_text = Text("benchmark lead = 0", font="Georgia",
                         color=ACC, font_size=22)
        zero_text.move_to(zero_box.get_center())

        self.play(GrowArrow(no_arrow), FadeIn(no_label), run_time=0.5)
        self.play(Create(zero_box), FadeIn(zero_text), run_time=0.6)
        self.wait(2.0)


# ── B36_FiveChecks ────────────────────────────────────────────────────────────
class B36_FiveChecks(Scene):
    """Five checklist rows build; all recolor to ACC stroke; serif label fades.
    Duration ~14s."""

    def construct(self):
        self.camera.background_color = BG

        checks = [
            "1.  Headline purity — which variant?",
            "2.  System score — the harness is inside",
            "3.  Effort matched — same settings?",
            "4.  Per-task cost — not per token",
            "5.  Compliance gate — before capability",
        ]

        cards = []
        for i, text in enumerate(checks):
            card = RoundedRectangle(width=8.5, height=0.72, corner_radius=0.18,
                                    fill_color=BG, fill_opacity=1,
                                    stroke_color=GHOST, stroke_width=2)
            label = Text(text, font="Georgia", color=INK, font_size=24)
            label.move_to(card.get_center())
            group = VGroup(card, label)
            group.move_to(UP * (1.8 - i * 0.95))
            cards.append((card, group))

        for card, group in cards:
            self.play(FadeIn(group, shift=RIGHT * 0.15), run_time=0.45)
            self.wait(0.2)

        self.wait(0.4)

        # All cards recolor stroke to ACC
        self.play(
            *[card.animate.set_stroke(color=ACC, width=2.5)
              for card, _ in cards],
            run_time=0.7
        )
        self.wait(0.3)

        serif_label = Text("the reusable lens", font="Georgia",
                           color=ACC, font_size=26)
        serif_label.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(serif_label), run_time=0.6)
        self.wait(1.5)


# ── B02_ComparisonTable ───────────────────────────────────────────────────────
class B02_ComparisonTable(Scene):
    """Drawn comparison table; terracotta circles on winning rows. ~11s."""

    def construct(self):
        self.camera.background_color = BG

        x_lbl, x_a, x_b = -3.0, 1.2, 3.1
        row_ys = [2.0, 1.4, 0.8, 0.2, -0.4, -1.0, -1.6, -2.2, -2.8]

        h_task = Text("TASK SET", font="Georgia", color=SOFT, font_size=19)
        h_task.move_to([x_lbl, 2.55, 0])
        h_a = Text("PREMIUM", font="Georgia", color=INK, font_size=19)
        h_a.move_to([x_a, 2.55, 0])
        h_b = Text("CHEAPER", font="Georgia", color=INK, font_size=19)
        h_b.move_to([x_b, 2.55, 0])
        sep = Line([-5.2, 2.32, 0], [4.4, 2.32, 0], color=INK, stroke_width=1.5)
        self.play(FadeIn(VGroup(h_task, h_a, h_b)), Create(sep), run_time=0.5)

        data = [
            ("1","✓","✗"), ("2","✓","✗"), ("3","✗","✓"),
            ("4","✓","✗"), ("5","✓","✗"), ("6","=","="),
            ("7","✗","✓"), ("8","✗","✓"), ("9","✓","✗"),
        ]
        win_a_indices = [0, 1, 3, 4, 8]
        row_a_texts = []

        for i, (lbl, ra, rb) in enumerate(data):
            y = row_ys[i]
            c_a = INK if ra == "✓" else (GHOST if ra == "=" else SOFT)
            c_b = INK if rb == "✓" else (GHOST if rb == "=" else SOFT)
            t_lbl = Text(f"Task set {lbl}", font="Georgia", color=SOFT, font_size=19)
            t_lbl.move_to([x_lbl, y, 0])
            t_a = Text(ra, font="Georgia", color=c_a, font_size=22)
            t_a.move_to([x_a, y, 0])
            t_b = Text(rb, font="Georgia", color=c_b, font_size=22)
            t_b.move_to([x_b, y, 0])
            self.play(FadeIn(VGroup(t_lbl, t_a, t_b)), run_time=0.35)
            row_a_texts.append(t_a)

        self.wait(0.3)

        for idx in win_a_indices:
            ring = Circle(radius=0.25, color=ACC, stroke_width=2.5)
            ring.move_to(row_a_texts[idx].get_center())
            self.play(Create(ring), run_time=0.25)

        self.wait(1.5)


# ── B03_PriceRowReveal ────────────────────────────────────────────────────────
class B03_PriceRowReveal(Scene):
    """Same table + price row slides in; terracotta bracket on price. ~11s."""

    def construct(self):
        self.camera.background_color = BG

        x_lbl, x_a, x_b = -3.0, 1.2, 3.1
        row_ys = [2.0, 1.4, 0.8, 0.2, -0.4, -1.0, -1.6, -2.2, -2.8]

        h_task = Text("TASK SET", font="Georgia", color=SOFT, font_size=19)
        h_task.move_to([x_lbl, 2.55, 0])
        h_a = Text("PREMIUM", font="Georgia", color=INK, font_size=19)
        h_a.move_to([x_a, 2.55, 0])
        h_b = Text("CHEAPER", font="Georgia", color=INK, font_size=19)
        h_b.move_to([x_b, 2.55, 0])
        sep = Line([-5.2, 2.32, 0], [4.4, 2.32, 0], color=INK, stroke_width=1.5)

        data = [
            ("1","✓","✗"), ("2","✓","✗"), ("3","✗","✓"),
            ("4","✓","✗"), ("5","✓","✗"), ("6","=","="),
            ("7","✗","✓"), ("8","✗","✓"), ("9","✓","✗"),
        ]
        win_a = [0,1,3,4,8]
        all_rows = VGroup()
        win_circles = VGroup()
        for i, (lbl, ra, rb) in enumerate(data):
            y = row_ys[i]
            c_a = INK if ra == "✓" else (GHOST if ra == "=" else SOFT)
            c_b = INK if rb == "✓" else (GHOST if rb == "=" else SOFT)
            t_lbl = Text(f"Task set {lbl}", font="Georgia", color=SOFT, font_size=19)
            t_lbl.move_to([x_lbl, y, 0])
            t_a = Text(ra, font="Georgia", color=c_a, font_size=22)
            t_a.move_to([x_a, y, 0])
            t_b = Text(rb, font="Georgia", color=c_b, font_size=22)
            t_b.move_to([x_b, y, 0])
            all_rows.add(t_lbl, t_a, t_b)
            if i in win_a:
                ring = Circle(radius=0.25, color=ACC, stroke_width=2.5)
                ring.move_to(t_a.get_center())
                win_circles.add(ring)

        self.play(FadeIn(VGroup(h_task, h_a, h_b, sep, all_rows)), run_time=0.7)
        self.play(FadeIn(win_circles), run_time=0.4)
        self.wait(0.3)

        # Price row separator + reveal
        price_sep = Line([-5.2, -3.0, 0], [4.4, -3.0, 0],
                         color=INK, stroke_width=1.5)
        price_lbl = Text("Cost per token", font="Georgia", color=INK, font_size=21)
        price_lbl.move_to([x_lbl, -3.3, 0])
        price_a = Text("2×  (illustrative)", font="Georgia", color=INK, font_size=21)
        price_a.move_to([x_a, -3.3, 0])
        price_b = Text("1×  (illustrative)", font="Georgia", color=INK, font_size=21)
        price_b.move_to([x_b, -3.3, 0])
        price_row = VGroup(price_sep, price_lbl, price_a, price_b)
        self.play(FadeIn(price_row, shift=UP * 0.2), run_time=0.7)

        bracket = Line([-5.0, -3.45, 0], [4.2, -3.45, 0],
                       color=ACC, stroke_width=3)
        self.play(Create(bracket), run_time=0.5)
        self.wait(4.5)


# ── B09_FootnoteChart ─────────────────────────────────────────────────────────
class B09_FootnoteChart(Scene):
    """Bar chart with star on one bar; ring draws; footnote fades in. ~12s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Benchmark Launch Chart", font="Georgia",
                     color=INK, font_size=32)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)

        bar_data = [
            ("Task A", 0.55, GHOST),
            ("Task B†", 0.82, INK),
            ("Task C", 0.47, GHOST),
        ]
        bar_w = 1.2
        bar_xs = [-3.0, 0.0, 3.0]
        baseline_y = -1.4
        max_h = 3.2

        axes_line = Line([-4.5, baseline_y, 0], [4.5, baseline_y, 0],
                         color=INK, stroke_width=1.5)
        self.play(Create(axes_line), run_time=0.3)

        bars = []
        for (label, frac, col), bx in zip(bar_data, bar_xs):
            h = frac * max_h
            rect = Rectangle(width=bar_w, height=h, fill_color=col,
                              fill_opacity=0.85, stroke_color=INK,
                              stroke_width=1.5)
            rect.move_to([bx, baseline_y + h / 2, 0])
            bl = Text(label, font="Georgia", color=INK, font_size=22)
            bl.move_to([bx, baseline_y - 0.35, 0])
            bars.append((rect, bl))
            self.play(Create(rect), FadeIn(bl), run_time=0.4)

        self.wait(0.4)

        ring = SurroundingRectangle(bars[1][0], color=ACC, buff=0.1,
                                    corner_radius=0.12, stroke_width=3)
        self.play(Create(ring), run_time=0.5)

        footnote = Text("† unrestricted variant scored this row",
                        font="Georgia", color=INK, font_size=21)
        footnote.to_edge(DOWN, buff=0.8)
        caption = Text("(illustrative — not real measurements)", font="Georgia",
                       color=SOFT, font_size=18)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(footnote), run_time=0.5)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(3.5)


# ── B13_RoutingDiagram ────────────────────────────────────────────────────────
class B13_RoutingDiagram(Scene):
    """Prompt → router → safety filter → model; flagged reroutes to fallback. ~13s."""

    def construct(self):
        self.camera.background_color = BG

        def node(txt, col=INK, w=2.6, h=0.7):
            box = RoundedRectangle(width=w, height=h, corner_radius=0.12,
                                   fill_color=BG, fill_opacity=1,
                                   stroke_color=col, stroke_width=2)
            label = Text(txt, font="Georgia", color=INK, font_size=22)
            label.move_to(box.get_center())
            return VGroup(box, label)

        ys_main = [2.6, 1.5, 0.4, -0.7, -1.8]
        x_main  = -1.5
        node_labels = ["prompt", "router", "safety filter", "model", "fallback"]
        node_colors = [INK, INK, INK, INK, INK]
        nodes = []
        for lbl, col, y in zip(node_labels, node_colors, ys_main):
            nd = node(lbl, col=col)
            nd.move_to([x_main, y, 0])
            nodes.append(nd)

        for nd in nodes[:4]:
            self.play(FadeIn(nd), run_time=0.35)

        arrows_main = []
        for i in range(3):
            a = Arrow(
                [x_main, ys_main[i] - 0.36, 0],
                [x_main, ys_main[i+1] + 0.36, 0],
                color=INK, stroke_width=2.5, buff=0
            )
            self.play(GrowArrow(a), run_time=0.22)

        self.wait(0.3)

        self.play(FadeIn(nodes[4]), run_time=0.35)
        reroute = CurvedArrow(
            [x_main + 1.3, ys_main[1], 0],
            [x_main + 1.3, ys_main[4] + 0.36, 0],
            color=ACC, angle=TAU / 5, stroke_width=2.5
        )
        flag_label = Text("if flagged →", font="Georgia",
                          color=INK, font_size=26)
        flag_label.move_to([x_main + 3.2, (ys_main[1] + ys_main[4]) / 2, 0])
        self.play(Create(reroute), FadeIn(flag_label), run_time=0.6)
        self.wait(0.3)

        cap = Text("The 'model' column wraps all of this",
                   font="Georgia", color=INK, font_size=22)
        cap.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ── B14_InferenceStack ────────────────────────────────────────────────────────
class B14_InferenceStack(Scene):
    """Vertical inference stack: prompt → router → filter → model → fallback. ~13s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Inference Stack", font="Georgia",
                     color=INK, font_size=30)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)

        labels = ["prompt", "router", "safety filter", "model", "fallback"]
        ys = [1.8, 0.9, 0.0, -0.9, -1.8]
        x_c = 0.0

        for i, (lbl, y) in enumerate(zip(labels, ys)):
            box = RoundedRectangle(width=3.2, height=0.72, corner_radius=0.14,
                                   fill_color=BG, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2)
            box.move_to([x_c, y, 0])
            txt = Text(lbl, font="Georgia", color=INK, font_size=24)
            txt.move_to(box.get_center())
            self.play(FadeIn(VGroup(box, txt), shift=RIGHT * 0.1), run_time=0.4)
            if i < len(ys) - 1:
                arrow = Arrow([x_c, y - 0.37, 0], [x_c, ys[i+1] + 0.37, 0],
                              color=INK, stroke_width=2.5, buff=0)
                self.play(GrowArrow(arrow), run_time=0.25)

        cap = Text("every component has a policy — all were inside the benchmark",
                   font="Georgia", color=SOFT, font_size=20)
        cap.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ── B15_FallbackNode ──────────────────────────────────────────────────────────
class B15_FallbackNode(Scene):
    """Same stack; fallback box highlights in ACC; label appears. ~12s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Inference Stack", font="Georgia",
                     color=INK, font_size=30)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.4)

        labels = ["prompt", "router", "safety filter", "model", "fallback"]
        ys = [1.8, 0.9, 0.0, -0.9, -1.8]
        x_c = 0.0

        boxes_vgroup = VGroup()
        arrows_vg = VGroup()
        fallback_grp = None

        for i, (lbl, y) in enumerate(zip(labels, ys)):
            box = RoundedRectangle(width=3.2, height=0.72, corner_radius=0.14,
                                   fill_color=BG, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2)
            box.move_to([x_c, y, 0])
            txt = Text(lbl, font="Georgia", color=INK, font_size=24)
            txt.move_to(box.get_center())
            grp = VGroup(box, txt)
            boxes_vgroup.add(grp)
            if lbl == "fallback":
                fallback_grp = grp
            if i < len(ys) - 1:
                a = Arrow([x_c, y - 0.37, 0], [x_c, ys[i+1] + 0.37, 0],
                          color=INK, stroke_width=2.5, buff=0)
                arrows_vg.add(a)

        self.play(FadeIn(boxes_vgroup), Create(arrows_vg), run_time=0.8)
        self.wait(0.4)

        ring = SurroundingRectangle(fallback_grp, color=INK, buff=0.1,
                                    stroke_width=3)
        note = Text("part of the score came from here",
                    font="Georgia", color=INK, font_size=21)
        note.move_to([x_c + 3.8, ys[-1], 0])
        arr_note = Arrow([x_c + 2.3, ys[-1], 0], [x_c + 1.75, ys[-1], 0],
                         color=ACC, stroke_width=2.5, buff=0.05)
        self.play(Create(ring), run_time=0.5)
        self.play(FadeIn(note), GrowArrow(arr_note), run_time=0.5)
        self.wait(4.5)


# ── B22_BlankEffortField ──────────────────────────────────────────────────────
class B22_BlankEffortField(Scene):
    """Spec form; 'Effort' row has blank value; terracotta ring draws. ~11s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Model Specification Sheet", font="Georgia",
                     color=INK, font_size=30)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)

        fields = [
            ("Score",         "84.2  (illustrative)"),
            ("Context",       "200 k tokens"),
            ("Latency",       "3.1 s  (illustrative)"),
            ("Effort level",  ""),
            ("Pricing tier",  "Standard"),
        ]
        x_key, x_val = -2.8, 1.4
        ys = [1.6, 0.8, 0.0, -0.8, -1.6]

        effort_row_g = None
        for i, (key, val) in enumerate(fields):
            y = ys[i]
            k_txt = Text(key, font="Georgia", color=INK, font_size=23)
            k_txt.move_to([x_key, y, 0])
            sep = Text(":", font="Georgia", color=SOFT, font_size=23)
            sep.move_to([-0.5, y, 0])
            if i == 3:
                dash = DashedLine([-0.1, y - 0.25, 0], [3.5, y - 0.25, 0],
                                  color=SOFT, stroke_width=1.5, dash_length=0.2)
                effort_row_g = VGroup(k_txt, sep, dash)
                self.play(FadeIn(effort_row_g), run_time=0.4)
            else:
                v_txt = Text(val, font="Georgia", color=SOFT, font_size=23)
                v_txt.move_to([x_val, y, 0])
                self.play(FadeIn(VGroup(k_txt, sep, v_txt)), run_time=0.35)

        self.wait(0.3)

        ring = SurroundingRectangle(effort_row_g, color=INK, buff=0.15,
                                    corner_radius=0.12, stroke_width=3)
        blank_label = Text("Effort: ——", font="Georgia",
                           color=INK, font_size=22)
        blank_label.next_to(ring, RIGHT, buff=0.3)
        self.play(Create(ring), run_time=0.5)
        self.play(FadeIn(blank_label), run_time=0.4)
        self.wait(3.2)


# ── B27_ReceiptVsSticker ──────────────────────────────────────────────────────
class B27_ReceiptVsSticker(Scene):
    """Price tag (left) vs itemized receipt (right) building line by line. ~13s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Price Tag  vs  Per-Task Receipt",
                     font="Georgia", color=INK, font_size=28)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)

        divider = Line([0, 2.0, 0], [0, -2.8, 0],
                       color=GHOST, stroke_width=1.2)
        self.play(Create(divider), run_time=0.3)

        # LEFT: price tag
        tag_box = RoundedRectangle(width=3.5, height=2.0, corner_radius=0.25,
                                   fill_color=BG, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2)
        tag_box.move_to([-2.8, 0.5, 0])
        tag_lbl = Text("price / token", font="Georgia", color=SOFT, font_size=20)
        tag_lbl.move_to([-2.8, 0.9, 0])
        tag_val = Text("$X.XX  (illustrative)", font="Georgia",
                       color=INK, font_size=24)
        tag_val.move_to([-2.8, 0.15, 0])
        tag_note = Text("one number", font="Georgia", color=SOFT, font_size=18)
        tag_note.move_to([-2.8, -0.72, 0])  # box bottom is y=-0.5; clear by 0.22
        self.play(Create(tag_box), FadeIn(tag_lbl), run_time=0.4)
        self.play(FadeIn(tag_val), FadeIn(tag_note), run_time=0.4)
        self.wait(0.3)

        # RIGHT: itemized receipt lines
        receipt_items = [
            "Input tokens ......... $X.XX",
            "Retries .............. $X.XX",
            "Verbosity overhead ... $X.XX",
            "Re-run cost .......... $X.XX",
        ]
        r_ys = [1.4, 0.7, 0.0, -0.7]
        for item, ry in zip(receipt_items, r_ys):
            t = Text(item, font="Georgia", color=INK, font_size=19)
            t.move_to([3.0, ry, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.1), run_time=0.4)

        total_sep = Line([1.2, -1.1, 0], [5.0, -1.1, 0],
                         color=INK, stroke_width=1)
        total_txt = Text("TOTAL ................ $XX.XX", font="Georgia",
                         color=INK, font_size=19)
        total_txt.move_to([3.0, -1.45, 0])
        caption = Text("(illustrative — not real measurements)", font="Georgia",
                       color=SOFT, font_size=17)
        caption.to_edge(DOWN, buff=0.6)
        self.play(Create(total_sep), FadeIn(total_txt), run_time=0.4)
        self.play(FadeIn(caption), run_time=0.3)
        self.wait(3.5)


# ── B28_ReceiptDetail ─────────────────────────────────────────────────────────
class B28_ReceiptDetail(Scene):
    """Same receipt; highlight bar tracks each line as narration names it. ~13s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Per-Task Receipt", font="Georgia",
                     color=INK, font_size=30)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.4)

        items = [
            ("Input tokens", "$X.XX"),
            ("Retries", "$X.XX"),
            ("Verbosity overhead", "$X.XX"),
            ("Re-run cost", "$X.XX"),
        ]
        ys = [1.5, 0.6, -0.3, -1.2]
        labels_objs = []
        for (item, val), y in zip(items, ys):
            row_line = Text(
                f"{item} .............. {val}  (illustrative)",
                font="Georgia", color=SOFT, font_size=22
            )
            row_line.move_to([0, y, 0])
            labels_objs.append(row_line)

        self.play(FadeIn(VGroup(*labels_objs)), run_time=0.5)
        self.wait(0.3)

        # highlight bar starts at row 0 — non-text shape gives the checker distinct states
        bar = Rectangle(width=8.5, height=0.45, color=ACC,
                        stroke_width=1.5, fill_opacity=0.08,
                        fill_color=ACC)
        bar.move_to([0, ys[0], 0])
        self.play(FadeIn(bar), run_time=0.3)

        for i, obj in enumerate(labels_objs):
            highlight = Text(
                f"{items[i][0]} .............. {items[i][1]}  (illustrative)",
                font="Georgia", color=INK, font_size=22
            )
            highlight.move_to(obj.get_center())
            anims = [Transform(obj, highlight)]
            if i > 0:
                anims.append(bar.animate.move_to([0, ys[i], 0]))
            self.play(*anims, run_time=0.4)
            self.wait(1.0)

        total_sep = Line([-4.0, -1.85, 0], [4.0, -1.85, 0],
                         color=INK, stroke_width=1)
        total_txt = Text("TOTAL  ≠  price / token × tokens",
                         font="Georgia", color=INK, font_size=22)
        total_txt.move_to([0, -2.25, 0])
        self.play(FadeOut(bar), Create(total_sep), FadeIn(total_txt), run_time=0.5)

        caption = Text("(illustrative — not real measurements)", font="Georgia",
                       color=SOFT, font_size=17)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption), run_time=0.3)
        self.wait(2.0)


# ── B31_ComplianceFunnel ──────────────────────────────────────────────────────
class B31_ComplianceFunnel(Scene):
    """Funnel: all models → compliance filter → deployable subset. ~16s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Compliance Funnel", font="Georgia",
                     color=INK, font_size=30)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)

        # Top band
        top_band = Polygon(
            [-4.0, 1.6, 0], [4.0, 1.6, 0],
            [3.0, 0.6, 0], [-3.0, 0.6, 0],
            fill_color="#EAE8E0", fill_opacity=1,
            stroke_color=INK, stroke_width=1.5
        )
        top_lbl = Text("All models  (full set)", font="Georgia",
                       color=INK, font_size=23)
        top_lbl.move_to([0, 1.15, 0])

        # Middle filter band
        mid_band = Polygon(
            [-3.0, 0.6, 0], [3.0, 0.6, 0],
            [2.0, -0.4, 0], [-2.0, -0.4, 0],
            fill_color="#F5E8E2", fill_opacity=1,
            stroke_color=ACC, stroke_width=2
        )
        mid_lbl = Text("Compliance filter", font="Georgia",
                       color=ACC, font_size=23)
        mid_lbl.move_to([0, 0.2, 0])
        mid_note = Text(
            "data retention  ·  output certification  ·  privacy",
            font="Georgia", color=ACC, font_size=16
        )
        mid_note.move_to([0, -0.1, 0])

        # Bottom band
        bot_band = Polygon(
            [-2.0, -0.4, 0], [2.0, -0.4, 0],
            [1.3, -1.4, 0], [-1.3, -1.4, 0],
            fill_color="#EAE8E0", fill_opacity=1,
            stroke_color=INK, stroke_width=1.5
        )
        bot_lbl = Text("Deployable subset", font="Georgia",
                       color=INK, font_size=23)
        bot_lbl.move_to([0, -0.9, 0])

        self.play(Create(top_band), FadeIn(top_lbl), run_time=0.6)
        self.wait(0.3)
        self.play(Create(mid_band), FadeIn(mid_lbl), run_time=0.6)
        self.play(FadeIn(mid_note), run_time=0.4)
        self.wait(0.5)
        self.play(Create(bot_band), FadeIn(bot_lbl), run_time=0.6)
        self.wait(0.4)

        cap_arrow = Arrow([0, -1.45, 0], [0, -2.05, 0],
                          color=INK, stroke_width=2.5, buff=0)
        cap_label = Text("capability analysis starts here",
                         font="Georgia", color=INK, font_size=22)
        cap_label.move_to([0, -2.45, 0])
        self.play(GrowArrow(cap_arrow), FadeIn(cap_label), run_time=0.6)
        self.wait(5.0)


# ── B32_ComplianceBinary ──────────────────────────────────────────────────────
class B32_ComplianceBinary(Scene):
    """Binary split: CAN DEPLOY (INK) vs CANNOT DEPLOY (ACC) → lead = 0. ~13s."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Compliance Gate Is Binary",
                     font="Georgia", color=INK, font_size=30)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)

        div = Line([0, 1.5, 0], [0, -2.2, 0],
                   color=GHOST, stroke_width=1.5)
        self.play(Create(div), run_time=0.3)

        # LEFT: CAN DEPLOY
        left_box = RoundedRectangle(width=4.2, height=1.6, corner_radius=0.2,
                                    fill_color=BG, fill_opacity=1,
                                    stroke_color=INK, stroke_width=2.5)
        left_box.move_to([-2.8, 0.4, 0])
        left_lbl = Text("CAN DEPLOY", font="Georgia",
                        color=INK, font_size=28)
        left_lbl.move_to(left_box.get_center())
        left_sub = Text("→ capability analysis begins",
                        font="Georgia", color=SOFT, font_size=19)
        left_sub.move_to([-2.8, -0.65, 0])
        self.play(Create(left_box), FadeIn(left_lbl), run_time=0.5)
        self.play(FadeIn(left_sub), run_time=0.4)
        self.wait(0.4)

        # RIGHT: CANNOT DEPLOY
        right_box = RoundedRectangle(width=4.2, height=1.6, corner_radius=0.2,
                                     fill_color=BG, fill_opacity=1,
                                     stroke_color=ACC, stroke_width=2.5)
        right_box.move_to([2.8, 0.4, 0])
        right_lbl = Text("CANNOT DEPLOY", font="Georgia",
                         color=INK, font_size=28)
        right_lbl.move_to(right_box.get_center())
        right_sub = Text("benchmark lead  =  0", font="Georgia",
                         color=INK, font_size=22)
        right_sub.move_to([2.8, -0.65, 0])
        right_sub2 = Text("(regardless of score)", font="Georgia",
                          color=SOFT, font_size=18)
        right_sub2.move_to([2.8, -1.1, 0])
        self.play(Create(right_box), FadeIn(right_lbl), run_time=0.6)
        self.play(FadeIn(right_sub), FadeIn(right_sub2), run_time=0.5)
        self.wait(4.5)
