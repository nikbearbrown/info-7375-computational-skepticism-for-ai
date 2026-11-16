"""scenes.py — Manim scenes for claude-liam-dashboard-that-lied.

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
Schematic curves carry no invented axis units.
No slant=ITALIC on multi-word text (Pango collapses spaces).
Equation tangent group: B12_DoOperator card rebuilt as starting state in B13.
"""
from manim import *
import numpy as np
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


# ── Palette ───────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#6E6A57")
GHOST = ManimColor("#A8A491")
CARD  = ManimColor("#FFFFFF")


def _label(text, size=22, color=None, weight=None):
    """Single-line label. No slant=ITALIC on multi-word text."""
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw, font='EB Garamond')


def _cite(text):
    return Text(text, font_size=14, color=SOFT, font='EB Garamond')


# ─────────────────────────────────────────────────────────────────────────────
#  B03_GreenLine
#  WAU rises 2.1M → 2.5M; clean, no tell. +18% chip lands in terracotta.
# ─────────────────────────────────────────────────────────────────────────────
class B03_GreenLine(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("The Green Line", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 3.2, 1],
            x_length=10.5,
            y_length=4.4,
            axis_config={
                "color": INK, "stroke_width": 1.3,
                "include_tip": True, "include_numbers": False,
            },
            tips=True,
        ).shift(DOWN * 0.55)

        y_lbl = _label("WAU", size=17, color=SOFT).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.45)
        self.play(Create(ax), FadeIn(y_lbl), run_time=0.8)

        # Clean rising line — deliberately no tell; endpoint at x=6.5 keeps chip within safe area
        wau_line = ax.plot(
            lambda x: 0.28 + x * 0.362,
            x_range=[0, 6.5],
            color=INK,
            stroke_width=3.0,
        )
        start_dot = Dot(ax.c2p(0, 0.28), color=INK, radius=0.09)
        end_dot   = Dot(ax.c2p(6.5, 2.633), color=INK, radius=0.09)
        start_lbl = _label("2.1M", size=15, color=SOFT).next_to(start_dot, LEFT, buff=0.2)
        end_lbl   = _label("2.5M", size=15, color=SOFT).next_to(end_dot, RIGHT, buff=0.15)

        self.play(FadeIn(start_dot), FadeIn(start_lbl), run_time=0.4)
        self.play(Create(wau_line), run_time=2.5, rate_func=rate_functions.smooth)
        self.play(FadeIn(end_dot), FadeIn(end_lbl), run_time=0.5)

        # +18% chip — ONE terracotta accent
        chip = Rectangle(width=1.85, height=0.54, color=ACC, stroke_width=2.0,
                          fill_color=CARD, fill_opacity=1
                          ).next_to(end_dot, UP, buff=0.3)
        chip_lbl = _label("+18%", size=20, color=ACC, weight="BOLD").move_to(chip)
        self.play(FadeIn(chip), FadeIn(chip_lbl), run_time=0.7)

        cite = _cite("Johnson & Johnson loyalty-program WAU case").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cite), run_time=0.4)
        self.wait(0.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_VanishingDenominator
#  EU dots fade silently; bar fraction recomputes upward.
#  "felt like good news." — terracotta underline.
# ─────────────────────────────────────────────────────────────────────────────
class B04_VanishingDenominator(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("The Vanishing Denominator", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Dot grid: 10 cols × 4 rows; cols 7–9 = EU records ────────────────
        cols, rows = 10, 4
        dot_r = 0.19
        dx, dy = 1.12, 0.78
        x_start = -(cols - 1) * dx / 2

        regular_dots = VGroup()
        eu_dots = VGroup()

        for row in range(rows):
            for col in range(cols):
                x = x_start + col * dx
                y = 1.55 - row * dy
                d = Circle(radius=dot_r, color=INK,
                            fill_color=INK, fill_opacity=0.6, stroke_width=0)
                d.move_to([x, y, 0])
                if col >= 7:
                    eu_dots.add(d)
                else:
                    regular_dots.add(d)

        eu_brace = Brace(eu_dots, direction=UP, color=GHOST, buff=0.1)
        eu_tag   = _label("400k EU records", size=14, color=GHOST
                           ).next_to(eu_brace, UP, buff=0.08)

        self.play(FadeIn(regular_dots), FadeIn(eu_dots), run_time=0.8)
        self.play(FadeIn(eu_brace), FadeIn(eu_tag), run_time=0.5)

        # ── Fraction display: Active ÷ Total ──────────────────────────────────
        bar_y = -2.0
        total_w = 8.2
        active_w = total_w * (28 / 40)  # 28 active of 40 total (schematic)

        total_bar = Rectangle(width=total_w, height=0.46, color=GHOST,
                               stroke_width=1.3, fill_color=GHOST, fill_opacity=0.4
                               ).move_to([0.1, bar_y, 0])
        active_bar = Rectangle(width=active_w, height=0.46, color=INK,
                                stroke_width=0, fill_color=INK, fill_opacity=0.55
                                ).move_to(total_bar).align_to(total_bar, LEFT)

        total_tag  = _label("Total", size=14, color=SOFT).next_to(total_bar, LEFT, buff=0.2)
        active_tag = _label("Active", size=13, color=CARD).move_to(active_bar)
        ratio_lbl  = _label("WAU", size=17, weight="BOLD").next_to(total_bar, RIGHT, buff=0.35)
        eq_lbl     = _label("=", size=17, color=SOFT).next_to(ratio_lbl, RIGHT, buff=0.18)
        ratio_val  = _label("70%", size=17).next_to(eq_lbl, RIGHT, buff=0.15)

        self.play(
            FadeIn(total_bar), FadeIn(active_bar),
            FadeIn(total_tag), FadeIn(active_tag),
            FadeIn(ratio_lbl), FadeIn(eq_lbl), FadeIn(ratio_val),
            run_time=0.7,
        )

        # ── EU dots fade — no alarm, no X, just absence ───────────────────────
        self.wait(0.35)
        self.play(
            FadeOut(eu_dots), FadeOut(eu_brace), FadeOut(eu_tag),
            run_time=1.8,
        )

        # ── Total bar shrinks; ratio climbs ───────────────────────────────────
        new_total_w = total_w * (28 / 40) + 0.5   # schematic: EU removed
        total_bar_2 = Rectangle(width=new_total_w, height=0.46, color=GHOST,
                                 stroke_width=1.3, fill_color=GHOST, fill_opacity=0.4
                                 ).move_to(total_bar).align_to(total_bar, LEFT)
        ratio_val_2 = _label("83%", size=17).next_to(eq_lbl, RIGHT, buff=0.15)

        self.play(
            Transform(total_bar, total_bar_2),
            Transform(ratio_val, ratio_val_2),
            run_time=1.4,
            rate_func=rate_functions.smooth,
        )

        # ── "felt like good news." — terracotta underline ─────────────────────
        stamp = _label("felt like good news.", size=22, weight="BOLD"
                        ).to_edge(DOWN, buff=0.9)
        underline = Line(
            stamp.get_left() + LEFT * 0.05,
            stamp.get_right() + RIGHT * 0.05,
            color=ACC, stroke_width=2.0,
        ).next_to(stamp, DOWN, buff=0.06)
        self.play(FadeIn(stamp), Create(underline), run_time=0.8)
        self.wait(0.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B10_RemoveThePromos
#  Revenue line with promo spikes; spikes deleted; ghost baseline rises;
#  actual revenue sags below. "more data would not have helped." — ACC period.
# ─────────────────────────────────────────────────────────────────────────────
class B10_RemoveThePromos(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Remove the Promotions", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 4.5, 1],
            x_length=10.5,
            y_length=4.2,
            axis_config={
                "color": INK, "stroke_width": 1.3,
                "include_tip": True, "include_numbers": False,
            },
            tips=True,
        ).shift(DOWN * 0.6)

        x_lbl = _label("time", size=16, color=SOFT).next_to(ax.x_axis, DOWN, buff=0.35)
        y_lbl = _label("revenue", size=16, color=SOFT).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.42)
        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.8)

        # Base line with promo spikes at x = 2, 4, 6, 8
        promo_xs = [2.0, 4.0, 6.0, 8.0]
        base_y = 1.4
        spike_h = 1.8

        def base_line_fn(x):
            return base_y

        base_curve = ax.plot(base_line_fn, x_range=[0, 10], color=SOFT, stroke_width=2.0)
        self.play(Create(base_curve), run_time=0.8)

        # Promo spikes as triangle-ish VMobjects
        spike_mobs = VGroup()
        promo_labels = VGroup()
        for px in promo_xs:
            pts = [
                ax.c2p(px - 0.35, base_y),
                ax.c2p(px, base_y + spike_h),
                ax.c2p(px + 0.35, base_y),
            ]
            spike = Polygon(*pts, color=INK, fill_color=INK, fill_opacity=0.45,
                             stroke_width=1.5)
            spike_mobs.add(spike)
            lbl = _label("PROMO", size=11, color=SOFT).next_to(ax.c2p(px, base_y), DOWN, buff=0.15)
            promo_labels.add(lbl)

        self.play(FadeIn(spike_mobs), FadeIn(promo_labels), run_time=1.0)

        # ── Delete spikes one by one ──────────────────────────────────────────
        self.wait(0.2)
        for i in range(len(promo_xs)):
            self.play(
                FadeOut(spike_mobs[i]),
                FadeOut(promo_labels[i]),
                run_time=0.45,
            )

        # ── Ghost "expected baseline" rises (the wrong assumption) ────────────
        expected_y = base_y + 0.9
        _ghost_base = ax.plot(
            lambda x: expected_y,
            x_range=[0, 10],
            color=GHOST,
            stroke_width=1.8,
        )
        ghost_line = DashedVMobject(_ghost_base, num_dashes=20, dashed_ratio=0.5)
        ghost_lbl = _label("expected", size=14, color=GHOST
                            ).next_to(ax.c2p(9.5, expected_y), RIGHT, buff=0.1
                            ).shift(UP * 0.25)
        self.play(Create(ghost_line), FadeIn(ghost_lbl), run_time=0.9)

        # ── Actual revenue sags below the old base ────────────────────────────
        actual_y = base_y - 0.7
        actual_line = ax.plot(
            lambda x: actual_y,
            x_range=[0, 10],
            color=INK,
            stroke_width=2.5,
        )
        actual_lbl = _label("actual", size=14, color=INK
                             ).next_to(ax.c2p(9.5, actual_y), RIGHT, buff=0.1
                             ).shift(DOWN * 0.25)
        self.play(Create(actual_line), FadeIn(actual_lbl), run_time=1.0,
                  rate_func=rate_functions.smooth)

        # ── "more data would not have helped." — ACC period ───────────────────
        msg_main = _label("more data would not have helped", size=20, weight="BOLD"
                           ).to_edge(DOWN, buff=0.9)
        msg_dot  = Text(".", font_size=22, color=ACC, font='EB Garamond'
                         ).next_to(msg_main, RIGHT, buff=0.02).align_to(msg_main, DOWN)
        self.play(FadeIn(msg_main), FadeIn(msg_dot), run_time=0.8)
        self.wait(0.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B12_DoOperator  (equation tangent group — card persists into B13)
#  P(Y|X) and P(Y|do(X)) appear side by side; do() glows terracotta.
#  "Johnson's decision" chip lands under P(Y|X) — the wrong side.
# ─────────────────────────────────────────────────────────────────────────────
class B12_DoOperator(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Seeing · Doing", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Left card: P(Y | X) ───────────────────────────────────────────────
        left_card = Rectangle(width=4.8, height=3.4, color=INK, stroke_width=1.5,
                               fill_color=CARD, fill_opacity=1).shift(LEFT * 3.2 + DOWN * 0.1)

        eq_left = MathTex(r"P(Y \mid X)", font_size=46, color=INK
                           ).move_to(left_card).shift(UP * 0.55)
        left_label = _label("conditional", size=16, color=SOFT
                             ).move_to(left_card).shift(UP * 0.0)
        left_gloss = _label("observe a world", size=15, color=SOFT
                             ).move_to(left_card).shift(DOWN * 0.55)

        self.play(FadeIn(left_card), run_time=0.5)
        self.play(Write(eq_left), run_time=1.1)
        self.play(FadeIn(left_label), FadeIn(left_gloss), run_time=0.6)

        # ── Right card: P(Y | do(X)) — do() in terracotta ────────────────────
        right_card = Rectangle(width=4.8, height=3.4, color=INK, stroke_width=1.5,
                                fill_color=CARD, fill_opacity=1).shift(RIGHT * 3.2 + DOWN * 0.1)

        # Build equation with colored do() — three-part MathTex
        eq_right = MathTex(
            r"P(Y \mid ", r"\mathrm{do}", r"(X))",
            font_size=46,
        ).move_to(right_card).shift(UP * 0.55)
        eq_right[0].set_color(INK)
        eq_right[1].set_color(ACC)   # ONE terracotta accent
        eq_right[2].set_color(INK)

        right_label = _label("interventional", size=16, color=SOFT
                              ).move_to(right_card).shift(UP * 0.0)
        right_gloss = _label("make a world", size=15, color=SOFT
                              ).move_to(right_card).shift(DOWN * 0.55)

        self.play(FadeIn(right_card), run_time=0.4)
        self.play(Write(eq_right), run_time=1.2)
        self.play(FadeIn(right_label), FadeIn(right_gloss), run_time=0.6)

        # ── Pearl attribution ─────────────────────────────────────────────────
        pearl_cite = _cite("Judea Pearl — Causality (2000)").to_edge(DOWN, buff=1.1)
        self.play(FadeIn(pearl_cite), run_time=0.4)

        # ── Johnson's decision chip lands under P(Y|X) — wrong side ──────────
        chip = Rectangle(width=2.6, height=0.52, color=INK, stroke_width=1.4,
                          fill_color=GHOST, fill_opacity=0.5
                          ).next_to(left_card, DOWN, buff=0.25)
        chip_lbl = _label("Johnson's decision", size=14, color=INK).move_to(chip)
        arrow_down = Arrow(
            left_card.get_bottom() + DOWN * 0.05,
            chip.get_top() + UP * 0.05,
            color=INK, stroke_width=1.5, tip_length=0.18,
        )
        self.play(GrowArrow(arrow_down), FadeIn(chip), FadeIn(chip_lbl), run_time=0.9)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_CategoryBoundary  (equation tangent group continued)
#  Equation card persists (rebuilt); recorded-world tiles; do-arrow off shelf.
#  "not a data shortage. a category boundary." — terracotta.
# ─────────────────────────────────────────────────────────────────────────────
class B13_CategoryBoundary(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("A Category Boundary", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Equation card persists from B12 — rebuilt small at top ───────────
        eq_group = VGroup()

        obs_box = Rectangle(width=2.8, height=1.1, color=SOFT, stroke_width=1.2,
                             fill_color=CARD, fill_opacity=1).shift(LEFT * 3.5 + UP * 2.2)
        obs_eq  = MathTex(r"P(Y \mid X)", font_size=26, color=INK).move_to(obs_box)

        int_box = Rectangle(width=3.0, height=1.1, color=INK, stroke_width=1.5,
                             fill_color=CARD, fill_opacity=1).shift(RIGHT * 0.2 + UP * 2.2)
        int_eq  = MathTex(
            r"P(Y \mid ", r"\mathrm{do}", r"(X))",
            font_size=26,
        ).move_to(int_box)
        int_eq[0].set_color(INK)
        int_eq[1].set_color(ACC)
        int_eq[2].set_color(INK)

        vs_lbl = _label("vs", size=16, color=SOFT).move_to(LEFT * 1.4 + UP * 2.2)

        eq_group.add(obs_box, obs_eq, int_box, int_eq, vs_lbl)
        self.play(FadeIn(eq_group), run_time=0.6)

        # ── Shelf of recorded-world tiles ─────────────────────────────────────
        tile_w, tile_h = 1.5, 0.7
        tile_gap = 0.18
        n_tiles = 5   # 5 tiles: last tile right-edge ≈ x=3.27, leaving room for arrow + 2 extras
        tile_y = 0.55
        tiles = VGroup()
        for i in range(n_tiles):
            x = -4.2 + i * (tile_w + tile_gap)
            t = Rectangle(width=tile_w, height=tile_h, color=SOFT,
                           stroke_width=1.1, fill_color=GHOST, fill_opacity=0.3
                           ).move_to([x, tile_y, 0])
            lbl = _label("promo-world", size=10, color=SOFT).move_to(t)
            tiles.add(t, lbl)

        shelf_label = _label("the historical record", size=16, color=SOFT
                              ).next_to(tiles, DOWN, buff=0.22)
        self.play(FadeIn(tiles), FadeIn(shelf_label), run_time=0.9)

        # ── do-arrow points off the shelf into empty space ────────────────────
        shelf_right = tiles[-2].get_right()  # last tile (right edge)
        do_arrow = Arrow(
            shelf_right + RIGHT * 0.1,
            shelf_right + RIGHT * 2.0,
            color=INK, stroke_width=2.2, tip_length=0.22,
        )
        do_world_lbl = _label("do-world", size=16, color=INK
                               ).next_to(do_arrow.get_tip(), UP, buff=0.4)
        self.play(GrowArrow(do_arrow), FadeIn(do_world_lbl), run_time=0.9)

        # ── More tiles pour in — none land where the arrow points ─────────────
        extra_tiles = VGroup()
        for i in range(1):   # 1 extra tile: final x=4.2, right edge=4.95 — within ±6.3 safe area
            x = -4.2 + (n_tiles + i) * (tile_w + tile_gap)
            t = Rectangle(width=tile_w, height=tile_h, color=SOFT,
                           stroke_width=1.1, fill_color=GHOST, fill_opacity=0.25
                           ).move_to([x, tile_y, 0]).shift(LEFT * 3.5)
            # no labels on extra tiles — avoids overlap with the do-arrow shaft
            extra_tiles.add(t)

        self.play(
            extra_tiles.animate.shift(RIGHT * 3.5),
            run_time=1.0, rate_func=rate_functions.smooth,
        )
        self.wait(0.2)

        # ── "not a data shortage. a category boundary." — terracotta ─────────
        conclusion = _label("not a data shortage.", size=20, weight="BOLD"
                             ).to_edge(DOWN, buff=1.1)
        conclusion2 = _label("a category boundary.", size=20, color=ACC, weight="BOLD"
                              ).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(conclusion), run_time=0.5)
        self.play(FadeIn(conclusion2), run_time=0.6)
        self.wait(0.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B15_ConfounderDAG
#  Z → X, Z → Y drawn; observe-mode co-pulse; do-mode severs Z→X.
#  Terracotta ring on Z: "one hidden parent".
# ─────────────────────────────────────────────────────────────────────────────
class B15_ConfounderDAG(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("The Confounder", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Node positions ─────────────────────────────────────────────────────
        z_pos = UP * 1.6
        x_pos = LEFT * 4.0 + DOWN * 1.2
        y_pos = RIGHT * 4.0 + DOWN * 1.2

        node_r = 0.52

        z_circle = Circle(radius=node_r, color=INK, stroke_width=2.2,
                           fill_color=CARD, fill_opacity=1).move_to(z_pos)
        x_circle = Circle(radius=node_r, color=INK, stroke_width=1.8,
                           fill_color=CARD, fill_opacity=1).move_to(x_pos)
        y_circle = Circle(radius=node_r, color=INK, stroke_width=1.8,
                           fill_color=CARD, fill_opacity=1).move_to(y_pos)

        z_lbl = _label("Z", size=26, weight="BOLD").move_to(z_circle)
        x_lbl = _label("X", size=26, weight="BOLD").move_to(x_circle)
        y_lbl = _label("Y", size=26, weight="BOLD").move_to(y_circle)

        z_sub = _label("high spender", size=13, color=SOFT).next_to(z_circle, UP, buff=0.6)
        x_sub = _label("loyalty\nmember", size=13, color=SOFT).next_to(x_circle, DOWN, buff=0.2)
        y_sub = _label("order\nvalue", size=13, color=SOFT).next_to(y_circle, DOWN, buff=0.2)

        self.play(
            FadeIn(z_circle), FadeIn(z_lbl), FadeIn(z_sub),
            FadeIn(x_circle), FadeIn(x_lbl), FadeIn(x_sub),
            FadeIn(y_circle), FadeIn(y_lbl), FadeIn(y_sub),
            run_time=0.9,
        )

        # ── Edges ─────────────────────────────────────────────────────────────
        # Z → X
        zx_start = z_circle.get_left() + DOWN * 0.2
        zx_end   = x_circle.get_top() + RIGHT * 0.1
        zx_arrow = Arrow(zx_start, zx_end, color=INK, stroke_width=2.0, tip_length=0.22)

        # Z → Y
        zy_start = z_circle.get_right() + DOWN * 0.2
        zy_end   = y_circle.get_top() + LEFT * 0.1
        zy_arrow = Arrow(zy_start, zy_end, color=INK, stroke_width=2.0, tip_length=0.22)

        # X → Y
        xy_start = x_circle.get_right()
        xy_end   = y_circle.get_left()
        xy_arrow = Arrow(xy_start, xy_end, color=GHOST, stroke_width=1.5,
                          tip_length=0.2)

        self.play(Create(zx_arrow), Create(zy_arrow), Create(xy_arrow), run_time=1.0)

        # ── Observe mode: X and Y pulse together ─────────────────────────────
        obs_label = _label("observe:", size=16, color=SOFT).to_edge(LEFT, buff=0.88).shift(DOWN * 3.0)
        x_pulse = Circle(radius=node_r + 0.2, color=SOFT, stroke_width=1.2,
                          fill_opacity=0, stroke_opacity=0.6).move_to(x_pos)
        y_pulse = Circle(radius=node_r + 0.2, color=SOFT, stroke_width=1.2,
                          fill_opacity=0, stroke_opacity=0.6).move_to(y_pos)

        self.play(FadeIn(obs_label), run_time=0.3)
        self.play(FadeIn(x_pulse), FadeIn(y_pulse), run_time=0.6)
        self.play(
            x_pulse.animate.scale(1.25),
            y_pulse.animate.scale(1.25),
            run_time=0.7, rate_func=rate_functions.there_and_back,
        )
        self.play(FadeOut(x_pulse), FadeOut(y_pulse), FadeOut(obs_label), run_time=0.4)

        # ── do-mode: Z→X severed; X pulses, Y unmoved ─────────────────────────
        do_label = _label("do(X):", size=16, color=INK).to_edge(LEFT, buff=0.88).shift(DOWN * 3.0)
        self.play(FadeIn(do_label), run_time=0.3)

        # Sever Z→X: replace with a crossed-out marker
        cut_h = Line(
            zx_arrow.get_center() + UP * 0.25 + LEFT * 0.15,
            zx_arrow.get_center() + DOWN * 0.25 + RIGHT * 0.15,
            color=INK, stroke_width=3.0,
        )
        cut_v = Line(
            zx_arrow.get_center() + DOWN * 0.25 + LEFT * 0.15,
            zx_arrow.get_center() + UP * 0.25 + RIGHT * 0.15,
            color=INK, stroke_width=3.0,
        )
        self.play(FadeOut(zx_arrow), run_time=0.4)
        self.play(Create(cut_h), Create(cut_v), run_time=0.5)

        # X pulses alone; Y unmoved
        x_pulse2 = Circle(radius=node_r + 0.2, color=INK, stroke_width=1.5,
                           fill_opacity=0, stroke_opacity=0.8).move_to(x_pos)
        self.play(FadeIn(x_pulse2), run_time=0.4)
        self.play(
            x_pulse2.animate.scale(1.3),
            run_time=0.7, rate_func=rate_functions.there_and_back,
        )
        self.play(FadeOut(x_pulse2), run_time=0.3)

        # ── Terracotta ring on Z: "one hidden parent" — ONE ACC accent ────────
        z_ring = Circle(radius=node_r + 0.28, color=ACC, stroke_width=2.8,
                         fill_opacity=0).move_to(z_pos)
        hidden_lbl = _label("one hidden parent", size=18, color=ACC, weight="BOLD"
                             ).to_edge(DOWN, buff=0.85)
        self.play(Create(z_ring), FadeIn(hidden_lbl), run_time=0.8)
        self.wait(0.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B17_TheLadder
#  Three rungs draw in turn: SEEING · DOING · IMAGINING.
#  DASHBOARD chip on rung one; DECISION chip on rung two.
#  Rung three glows terracotta: "worlds that never existed".
# ─────────────────────────────────────────────────────────────────────────────
class B17_TheLadder(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Pearl's Ladder", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Ladder structure ──────────────────────────────────────────────────
        rung_w   = 9.5
        rung_h   = 1.0
        rung_gap = 0.55
        rail_w   = 0.12

        # y centers for rungs (bottom to top: rung 1, 2, 3)
        rung_ys = [-1.65, -0.1, 1.45]
        rung_data = [
            ("SEEING",     "what co-occurs?",         r"P(Y \mid X)"),
            ("DOING",      "what if I act?",           r"P(Y \mid \mathrm{do}(X))"),
            ("IMAGINING",  "what would have?",         r"P(Y_x \mid X')"),
        ]

        rung_rects = []
        for i, (ry, (label, question, _)) in enumerate(zip(rung_ys, rung_data)):
            rect = Rectangle(width=rung_w, height=rung_h, color=INK,
                              stroke_width=1.6, fill_color=CARD, fill_opacity=0.9
                              ).move_to([0, ry, 0])
            rung_rects.append(rect)

        # Side rails
        left_rail  = Line([-(rung_w / 2 + 0.25), rung_ys[0] - rung_h / 2, 0],
                           [-(rung_w / 2 + 0.25), rung_ys[2] + rung_h / 2, 0],
                           color=INK, stroke_width=rail_w * 50)
        right_rail = Line([ (rung_w / 2 + 0.25), rung_ys[0] - rung_h / 2, 0],
                           [ (rung_w / 2 + 0.25), rung_ys[2] + rung_h / 2, 0],
                           color=INK, stroke_width=rail_w * 50)

        self.play(Create(left_rail), Create(right_rail), run_time=0.6)

        # ── Draw rungs in turn ─────────────────────────────────────────────────
        chips_group = VGroup()
        for i, (ry, (label, question, eq_str)) in enumerate(zip(rung_ys, rung_data)):
            rung_c = rung_rects[i].get_fill_color()
            self.play(FadeIn(rung_rects[i]), run_time=0.5)

            lbl = _label(label, size=19, weight="BOLD").move_to([-(rung_w / 2 - 1.4), ry, 0])
            q   = _label(question, size=15, color=SOFT).move_to([0.6, ry, 0])
            eq  = MathTex(eq_str, font_size=22, color=INK).move_to([(rung_w / 2 - 1.5), ry, 0])
            if i == 1:
                eq[0].set_color(INK)
                if len(eq) > 1:
                    eq[1].set_color(INK)

            self.play(FadeIn(lbl), FadeIn(q), FadeIn(eq), run_time=0.55)

        # ── DASHBOARD chip on rung 1 ──────────────────────────────────────────
        dash_chip = Rectangle(width=2.4, height=0.5, color=SOFT, stroke_width=1.3,
                               fill_color=GHOST, fill_opacity=0.5
                               ).next_to(rung_rects[0], DOWN, buff=0.18)
        dash_lbl  = _label("DASHBOARD", size=13, color=SOFT).move_to(dash_chip)
        self.play(FadeIn(dash_chip), FadeIn(dash_lbl), run_time=0.5)

        # ── DECISION chip on rung 2 ────────────────────────────────────────────
        dec_chip = Rectangle(width=2.4, height=0.5, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1
                              ).next_to(rung_rects[1], DOWN, buff=0.18)
        dec_lbl  = _label("DECISION", size=13, color=INK).move_to(dec_chip)
        self.play(FadeIn(dec_chip), FadeIn(dec_lbl), run_time=0.5)

        # ── Rung 3 glows terracotta — ONE ACC accent ───────────────────────────
        rung3_highlight = Rectangle(
            width=rung_w + 0.1, height=rung_h + 0.1,
            color=ACC, stroke_width=2.5, fill_opacity=0,
        ).move_to([0, rung_ys[2], 0])
        worlds_lbl = _label("worlds that never existed", size=17, color=ACC, weight="BOLD"
                             ).to_edge(DOWN, buff=0.85)
        self.play(Create(rung3_highlight), FadeIn(worlds_lbl), run_time=0.9)
        self.wait(0.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B22_ConceptDrift
#  Data flows; regime shift; model extrapolates the dead regime.
#  "reality has left." — terracotta period.
# ─────────────────────────────────────────────────────────────────────────────
class B22_ConceptDrift(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Concept Drift", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 4.5, 1],
            x_length=10.5,
            y_length=4.2,
            axis_config={
                "color": INK, "stroke_width": 1.3,
                "include_tip": True, "include_numbers": False,
            },
            tips=True,
        ).shift(DOWN * 0.55)

        x_lbl = _label("time", size=16, color=SOFT).next_to(ax.x_axis, DOWN, buff=0.35)
        y_lbl = _label("signal", size=16, color=SOFT).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.42)
        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.8)

        # ── Regime 1 data points (x=0→4) ─────────────────────────────────────
        np.random.seed(7)
        r1_xs = np.linspace(0.3, 4.0, 10)
        r1_ys = 1.0 + r1_xs * 0.3 + np.random.normal(0, 0.18, len(r1_xs))
        r1_dots = VGroup(*[
            Dot(ax.c2p(x, y), radius=0.09, color=INK, fill_opacity=0.65)
            for x, y in zip(r1_xs, r1_ys)
        ])
        self.play(FadeIn(r1_dots), run_time=0.7)

        # ── Fitted model from regime 1 ─────────────────────────────────────────
        model_line = ax.plot(
            lambda x: 1.0 + x * 0.3,
            x_range=[0, 10],
            color=INK, stroke_width=2.2,
        )
        model_lbl = _label("model", size=15, color=INK).next_to(ax.c2p(8.5, 1.0 + 8.5 * 0.3), UP, buff=0.45)
        self.play(Create(model_line), FadeIn(model_lbl), run_time=0.8)

        # ── Regime shift marker at x=5 ───────────────────────────────────────
        shift_line = DashedLine(
            ax.c2p(5, 0), ax.c2p(5, 4.5),
            color=SOFT, stroke_width=1.5, dash_length=0.14,
        )
        shift_lbl = _label("regime shift", size=14, color=SOFT
                            ).next_to(ax.c2p(5, 4.0), RIGHT, buff=0.12)
        self.play(Create(shift_line), FadeIn(shift_lbl), run_time=0.7)

        # ── Regime 2 data points — new, higher slope ──────────────────────────
        r2_xs = np.linspace(5.2, 9.5, 10)
        r2_ys = 2.5 + (r2_xs - 5) * 0.0 + np.random.normal(0, 0.22, len(r2_xs))  # flat drift
        r2_dots = VGroup(*[
            Dot(ax.c2p(x, y), radius=0.09, color=SOFT, fill_opacity=0.65)
            for x, y in zip(r2_xs, r2_ys)
        ])
        self.play(FadeIn(r2_dots), run_time=0.8)

        # ── Model extrapolates old regime — confidence band ────────────────────
        conf_band = ax.get_area(
            ax.plot(lambda x: 1.0 + x * 0.3 + 0.35, x_range=[5, 10], color=INK),
            bounded_graph=ax.plot(lambda x: 1.0 + x * 0.3 - 0.35, x_range=[5, 10]),
            x_range=[5, 10],
            color=INK,
            opacity=0.12,
        )
        self.play(FadeIn(conf_band), run_time=0.6)
        self.wait(0.2)

        # ── "reality has left." — terracotta period — ONE ACC accent ─────────
        msg_main = _label("reality has left", size=22, weight="BOLD").to_edge(DOWN, buff=0.9)
        msg_dot  = Text(".", font_size=24, color=ACC, font='EB Garamond'
                         ).next_to(msg_main, RIGHT, buff=0.02).align_to(msg_main, DOWN)
        self.play(FadeIn(msg_main), FadeIn(msg_dot), run_time=0.8)
        self.wait(0.5)
