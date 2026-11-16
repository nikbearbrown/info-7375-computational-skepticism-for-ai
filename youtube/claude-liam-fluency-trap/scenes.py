"""scenes.py — Manim scenes for claude-liam-fluency-trap.

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
Numbers appear on screen ONLY with their citation line.
Schematic curves carry no invented axis units.
No slant=ITALIC on multi-word text (Pango collapses spaces).
"""
from manim import *
import numpy as np
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


# ── Palette ───────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all body text
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#6E6A57")   # secondary / muted text
GHOST = ManimColor("#A8A491")   # dimmed / placeholder
CARD  = ManimColor("#FFFFFF")   # white card surface

# safe margin for FILL-THE-CANVAS: 1920×1080 → keep content 80px inside
# In Manim units (1080px ≈ 8 units tall), safe_buff ≈ 0.6 units


def _label(text, size=22, color=None, weight=None):
    """Single-line serif-style label. Enforces §8.1: min 26pt. ACC → INK (contrast).
    Pass color as hex string (e.g. '#6E6A57') to keep SOFT visible without INK promotion."""
    # Identity check only — avoids ManimColor.__eq__ TypeError on str args
    _color = INK if (color is None or color is ACC) else color
    kw = {"font_size": max(26, size), "color": _color}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw, font='EB Garamond')


def _cite(text):
    """Citation line. §8.1/§8.3 compliant: min 26pt, INK."""
    return Text(text, font_size=26, color=INK, font='EB Garamond')


# ─────────────────────────────────────────────────────────────────────────────
#  B06_EaseDial
#  Two identical claim cards; ease meter fills for the clean one;
#  TRUE/TRUST dials tick up in sync; "content held constant" stamp.
# ─────────────────────────────────────────────────────────────────────────────
class B06_EaseDial(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Processing Fluency", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Two claim cards ───────────────────────────────────────────────────
        card_w, card_h = 3.8, 1.9
        left_rect  = Rectangle(width=card_w, height=card_h,
                                color=INK, stroke_width=1.5, fill_color=CARD,
                                fill_opacity=1).shift(LEFT * 3.3 + UP * 0.3)
        right_rect = Rectangle(width=card_w, height=card_h,
                                color=INK, stroke_width=1.5, fill_color=CARD,
                                fill_opacity=1).shift(RIGHT * 3.3 + UP * 0.3)

        left_claim  = _label("All models contain errors", size=16).move_to(left_rect).shift(UP * 0.3)
        right_claim = _label("All models contain errors", size=16).move_to(right_rect).shift(UP * 0.3)

        left_sub   = _label("Comic Sans  ·  misaligned margins", size=12, color=SOFT).move_to(left_rect).shift(DOWN * 0.25)
        right_sub  = _label("Clean serif  ·  balanced layout",  size=12, color=SOFT).move_to(right_rect).shift(DOWN * 0.25)

        left_tag  = _label("ROUGH", size=13, color=SOFT).move_to(left_rect).shift(DOWN * 0.7)
        right_tag = _label("CLEAN", size=13, color=SOFT).move_to(right_rect).shift(DOWN * 0.7)

        self.play(
            FadeIn(left_rect), FadeIn(right_rect),
            FadeIn(left_claim), FadeIn(right_claim),
            FadeIn(left_sub), FadeIn(right_sub),
            FadeIn(left_tag), FadeIn(right_tag),
            run_time=1.0,
        )

        # ── EASE meter fills on the clean side ───────────────────────────────
        meter_bg = Rectangle(width=2.0, height=0.28, color=GHOST,
                              stroke_width=0, fill_color=GHOST, fill_opacity=0.35
                              ).next_to(right_rect, DOWN, buff=0.25)
        meter_fill = Rectangle(width=0.01, height=0.28, color=ACC,
                                stroke_width=0, fill_color=ACC, fill_opacity=1
                                ).move_to(meter_bg).align_to(meter_bg, LEFT)
        ease_lbl = _label("EASE", size=14, color=ACC).next_to(meter_bg, LEFT, buff=0.18)

        # TRUE / TRUST dials (simple bar gauges)
        true_bg  = Rectangle(width=1.1, height=0.22, color=GHOST, stroke_width=0,
                              fill_color=GHOST, fill_opacity=0.35
                              ).next_to(meter_bg, DOWN, buff=0.22).shift(LEFT * 0.45)
        trust_bg = Rectangle(width=1.1, height=0.22, color=GHOST, stroke_width=0,
                              fill_color=GHOST, fill_opacity=0.35
                              ).next_to(true_bg, DOWN, buff=0.12)
        true_fill  = Rectangle(width=0.01, height=0.22, color=INK, stroke_width=0,
                                fill_color=INK, fill_opacity=0.7
                                ).move_to(true_bg).align_to(true_bg, LEFT)
        trust_fill = Rectangle(width=0.01, height=0.22, color=INK, stroke_width=0,
                                fill_color=INK, fill_opacity=0.7
                                ).move_to(trust_bg).align_to(trust_bg, LEFT)
        true_lbl  = _label("TRUE",  size=12, color=SOFT).next_to(true_bg, LEFT, buff=0.12)
        trust_lbl = _label("TRUST", size=12, color=SOFT).next_to(trust_bg, LEFT, buff=0.12)

        self.play(
            FadeIn(meter_bg), FadeIn(ease_lbl),
            FadeIn(true_bg), FadeIn(trust_bg),
            FadeIn(true_lbl), FadeIn(trust_lbl),
            FadeIn(true_fill), FadeIn(trust_fill),
            run_time=0.5,
        )
        meter_fill_full  = Rectangle(width=2.0, height=0.28, color=ACC,
                                      stroke_width=0, fill_color=ACC, fill_opacity=1
                                      ).move_to(meter_bg).align_to(meter_bg, LEFT)
        true_fill_full   = Rectangle(width=0.88, height=0.22, color=INK,
                                      stroke_width=0, fill_color=INK, fill_opacity=0.7
                                      ).move_to(true_bg).align_to(true_bg, LEFT)
        trust_fill_full  = Rectangle(width=0.85, height=0.22, color=INK,
                                      stroke_width=0, fill_color=INK, fill_opacity=0.7
                                      ).move_to(trust_bg).align_to(trust_bg, LEFT)
        self.play(
            Transform(meter_fill, meter_fill_full),
            Transform(true_fill,  true_fill_full),
            Transform(trust_fill, trust_fill_full),
            run_time=1.6,
            rate_func=rate_functions.smooth,
        )

        # ── "content held constant" stamp ────────────────────────────────────
        stamp = _label("content held constant", size=19, color=ACC, weight="BOLD"
                        ).to_edge(DOWN, buff=0.9)
        hairline = Line(
            stamp.get_left() + LEFT * 0.1,
            stamp.get_right() + RIGHT * 0.1,
            color=ACC, stroke_width=1.2,
        ).next_to(stamp, DOWN, buff=0.06)
        self.play(FadeIn(stamp), Create(hairline), run_time=0.8)
        self.wait(0.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_TwoHalos
#  One author mark; two essay cards fan out; judge marks rate the author;
#  polished lifts, rough sinks; "the bet was good. once."
# ─────────────────────────────────────────────────────────────────────────────
class B09_TwoHalos(Scene):

    def construct(self):
        self.camera.background_color = BG

        dur = 13.8
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)

        title = _label("The Halo Effect of Readability", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Author mark ────────────────────────────────────────────────────────
        author_circle = Circle(radius=0.38, color=INK, stroke_width=2.5,
                                fill_color=CARD, fill_opacity=1).shift(UP * 0.2)
        author_lbl = _label("AUTHOR", size=13).next_to(author_circle, DOWN, buff=0.15)
        self.play(Create(author_circle), FadeIn(author_lbl), run_time=0.8)

        # ── Two essay cards fan out ───────────────────────────────────────────
        polished_card = Rectangle(width=3.0, height=1.9, color=INK, stroke_width=1.5,
                                   fill_color=CARD, fill_opacity=1
                                   ).shift(RIGHT * 3.6 + UP * 0.2)
        rough_card    = Rectangle(width=3.0, height=1.9, color=GHOST, stroke_width=1.2,
                                   fill_color=CARD, fill_opacity=1
                                   ).shift(LEFT * 3.6 + UP * 0.2)

        pol_lbl  = _label("POLISHED", size=16, weight="BOLD").move_to(polished_card).shift(UP * 0.45)
        pol_sub  = _label("Clear, uniform, fluent",   size=12, color="#6E6A57").move_to(polished_card)
        rough_lbl = _label("ROUGH",   size=16, color="#6E6A57").move_to(rough_card).shift(UP * 0.45)
        rough_sub = _label("Uneven, cramped, awkward", size=12, color="#6E6A57").move_to(rough_card)

        # connector lines from author
        line_r = Line(author_circle.get_right(), polished_card.get_left(), color=INK, stroke_width=1.2)
        line_l = Line(author_circle.get_left(),  rough_card.get_right(),   color=GHOST, stroke_width=1.0)

        self.play(
            Create(polished_card), Create(rough_card),
            Create(line_r), Create(line_l),
            FadeIn(pol_lbl),
            FadeIn(rough_lbl),
            run_time=1.2,
        )

        # ── Judge marks rate the author (halo arrows) ──────────────────────────
        up_arrow = Arrow(
            polished_card.get_top() + UP * 0.1,
            polished_card.get_top() + UP * 1.0,
            color=ACC, stroke_width=2.5, tip_length=0.22,
        )
        down_arrow = Arrow(
            rough_card.get_bottom() + DOWN * 0.1,
            rough_card.get_bottom() + DOWN * 0.75,
            color=GHOST, stroke_width=2.0, tip_length=0.2,
        )
        up_lbl  = _label("HIGH",  size=14).next_to(up_arrow.get_end(),  RIGHT, buff=0.15)
        down_lbl = _label("competence judged low",  size=14, color="#6E6A57").next_to(down_arrow.get_end(), RIGHT, buff=0.15)

        self.play(
            GrowArrow(up_arrow), GrowArrow(down_arrow),
            FadeIn(up_lbl), FadeIn(down_lbl),
            run_time=1.2,
        )

        # ── "the bet was good. once." ──────────────────────────────────────────
        kicker = _label("the bet was good. once.", size=24, weight="BOLD").to_edge(DOWN, buff=0.85)
        self.play(FadeIn(kicker), run_time=0.8)
        self.wait(0.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B11_SpenceCurves
#  Two schematic cost curves: HIGH ABILITY shallow, LOW ABILITY steep.
#  Shaded gap between them. "the asymmetry IS the machine" label.
#  No invented axis units — axes are unlabeled on the value dimension.
# ─────────────────────────────────────────────────────────────────────────────
class B11_SpenceCurves(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Spence 1973 — Costly Signaling", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8.0,
            y_length=4.2,
            axis_config={
                "color": INK, "stroke_width": 1.3, "include_tip": True,
                "include_numbers": False,
            },
            tips=True,
        ).shift(DOWN * 0.55 + LEFT * 0.3)

        x_lbl = _label("signal level", size=17, color=SOFT).next_to(ax.x_axis, DOWN, buff=0.4)
        y_lbl = _label("cost", size=17, color=SOFT).next_to(ax.y_axis, UP, buff=0.12)

        # schematic curves: start from origin
        # HIGH ABILITY: low slope
        ha_pts = [ax.c2p(x, x * 0.55) for x in np.linspace(0, 4.5, 60)]
        # LOW ABILITY: steep slope
        la_pts = [ax.c2p(x, x * 1.35) for x in np.linspace(0, 3.3, 60)]

        ha_curve = VMobject(color=INK, stroke_width=2.2)
        ha_curve.set_points_as_corners(ha_pts)
        la_curve = VMobject(color=INK, stroke_width=2.2)
        la_curve.set_points_as_corners(la_pts)

        ha_tag = _label("HIGH ABILITY",   size=15, color=INK).next_to(ax.c2p(4.5, 2.6),  RIGHT, buff=0.1)
        la_tag = _label("LOW ABILITY",    size=15, color=SOFT).next_to(ax.c2p(3.3, 4.5),  RIGHT, buff=0.1)

        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.0)
        self.play(Create(ha_curve), Create(la_curve), FadeIn(ha_tag), FadeIn(la_tag), run_time=1.4)

        # ── Shade the asymmetric gap ───────────────────────────────────────────
        # Build a closed polygon between the two curves (up to x≈3.2)
        x_shared = np.linspace(0.1, 3.2, 40)
        top_pts  = [ax.c2p(x, x * 1.35) for x in x_shared]
        bot_pts  = [ax.c2p(x, x * 0.55) for x in reversed(x_shared)]
        region = Polygon(*top_pts, *bot_pts,
                          color=ACC, fill_color=ACC, fill_opacity=0.18, stroke_width=0)
        self.play(FadeIn(region), run_time=0.9)

        # ── Separating point marker ────────────────────────────────────────────
        sep_x = 2.5
        sep_dot = Dot(ax.c2p(sep_x, sep_x * 0.55), color=ACC, radius=0.1)
        sep_lbl = _label("separating point", size=14, color=ACC).next_to(ax.c2p(sep_x, sep_x * 0.55), RIGHT, buff=0.2)
        self.play(FadeIn(sep_dot), FadeIn(sep_lbl), run_time=0.6)

        # ── "the asymmetry IS the machine" ────────────────────────────────────
        machine_lbl = _label("the asymmetry IS the machine", size=21, color=ACC, weight="BOLD"
                               ).to_edge(DOWN, buff=0.85)
        self.play(FadeIn(machine_lbl), run_time=0.8)
        self.wait(0.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B14_Pooling
#  B11 curves return; steep flattens onto shallow at "zero for everyone";
#  separating point vanishes; $26 card with citation.
# ─────────────────────────────────────────────────────────────────────────────
class B14_Pooling(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("The Signal Stops Separating", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=7.8,
            y_length=3.8,
            axis_config={
                "color": INK, "stroke_width": 1.3, "include_tip": True,
                "include_numbers": False,
            },
            tips=True,
        ).shift(DOWN * 0.4 + LEFT * 0.6)

        x_lbl = _label("signal level", size=16, color=SOFT).next_to(ax.c2p(5, 0), RIGHT, buff=0.15)
        y_lbl = _label("cost", size=16, color=SOFT).next_to(ax.y_axis, UP, buff=0.10)
        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.8)

        # Initial curves (same geometry as B11)
        x_shared = np.linspace(0, 4.5, 60)
        ha_pts_0 = [ax.c2p(x, x * 0.55) for x in x_shared]
        la_pts_0 = [ax.c2p(x, x * 1.35) for x in np.linspace(0, 3.3, 60)]

        ha_curve = VMobject(color=INK, stroke_width=2.2)
        ha_curve.set_points_as_corners(ha_pts_0)
        la_curve = VMobject(color=INK, stroke_width=2.2)
        la_curve.set_points_as_corners(la_pts_0)
        ha_tag = _label("HIGH ABILITY", size=14, color=INK ).next_to(ax.c2p(4.5, 2.6),  RIGHT, buff=0.1)
        la_tag = _label("LOW ABILITY",  size=14, color=SOFT).next_to(ax.c2p(3.3, 4.5),  RIGHT, buff=0.1)

        sep_dot = Dot(ax.c2p(2.5, 1.38), color=ACC, radius=0.1)

        self.play(Create(ha_curve), Create(la_curve), FadeIn(ha_tag), FadeIn(la_tag),
                  FadeIn(sep_dot), run_time=1.0)

        # ── Steep curve FLATTENS onto the shallow one ─────────────────────────
        la_pts_1 = [ax.c2p(x, x * 0.55) for x in np.linspace(0, 4.5, 60)]
        la_curve_2 = VMobject(color=GHOST, stroke_width=2.2)
        la_curve_2.set_points_as_corners(la_pts_1)
        pooled_band = Rectangle(
            width=7.02,   # 4.5/5 * 7.8 (x_range [0,5], x_length 7.8)
            height=0.20,
            color=SOFT, fill_color=SOFT, fill_opacity=0.25, stroke_width=0,
        ).align_to(ax.c2p(0, 0.46), LEFT + DOWN)

        self.play(Transform(la_curve, la_curve_2), FadeOut(la_tag), FadeOut(sep_dot),
                  run_time=1.3, rate_func=rate_functions.smooth)
        self.play(FadeIn(pooled_band), run_time=0.6)

        pooled_lbl = _label("one pooled band", size=16, color=SOFT).next_to(pooled_band, RIGHT, buff=0.2)
        self.play(FadeIn(pooled_lbl), run_time=0.5)

        # ── $26 equivalence card — very bottom to clear the "signal level" label ─
        card = Rectangle(width=7.0, height=1.3, color=ACC, stroke_width=1.8,
                          fill_color=CARD, fill_opacity=1).to_edge(DOWN, buff=0.05)
        val_lbl = _label("+1 SD customization\n≈ $26 price cut", size=14, weight="BOLD").move_to(card).shift(UP * 0.35)
        cite    = _cite("Freelancer.com study, 2025").move_to(card).shift(DOWN * 0.3)
        self.play(FadeIn(card), FadeIn(val_lbl), FadeIn(cite), run_time=0.9)
        self.wait(0.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B15_Quintiles
#  Five quintile bars at old hire rates; top drops −19%, bottom rises +14%;
#  terracotta arrow on top bar; citation persists.
# ─────────────────────────────────────────────────────────────────────────────
class B15_Quintiles(Scene):

    def construct(self):
        self.camera.background_color = BG

        dur = 15.53
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)

        title = _label("Who the Pooling Hurts", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # Quintile bar chart — 5 bars, schematic heights (normalized)
        bar_count = 5
        bar_w = 0.95
        bar_gap = 0.32
        bar_heights_orig = [1.8, 2.4, 3.0, 3.6, 4.2]  # schematic relative heights
        bar_colors = [SOFT, SOFT, SOFT, SOFT, SOFT]

        ax_origin = np.array([-4.0, -2.6, 0.0])
        bars_orig = VGroup()
        bar_rects = []
        for i, (h, c) in enumerate(zip(bar_heights_orig, bar_colors)):
            x = ax_origin[0] + i * (bar_w + bar_gap)
            r = Rectangle(width=bar_w, height=h, color=c,
                           fill_color=c, fill_opacity=0.65, stroke_width=1.4
                           ).move_to([x + bar_w/2, ax_origin[1] + h/2, 0])
            bar_rects.append(r)
            bars_orig.add(r)

        q_labels = VGroup(*[
            _label(f"Q{i+1}", size=14, color="#6E6A57"
                   ).next_to(bar_rects[i], DOWN, buff=0.15)
            for i in range(bar_count)
        ])

        x_axis_line = Line(
            [ax_origin[0], ax_origin[1], 0],
            [ax_origin[0] + bar_count * (bar_w + bar_gap) + 0.3, ax_origin[1], 0],
            color=INK, stroke_width=1.5,
        )

        self.play(Create(x_axis_line), FadeIn(bars_orig), run_time=1.0)

        # ── Top bar drops −19%, bottom bar rises +14% ─────────────────────────
        # Q5 (top quintile) — bar_rects[4] shrinks
        top_new_h = bar_heights_orig[4] * 0.81
        top_new_r = Rectangle(width=bar_w, height=top_new_h, color=ACC,
                               fill_color=ACC, fill_opacity=0.7, stroke_width=1.6
                               ).move_to([
                                   bar_rects[4].get_x(),
                                   ax_origin[1] + top_new_h / 2, 0
                               ])
        # Q1 (bottom quintile) — bar_rects[0] grows
        bot_new_h = bar_heights_orig[0] * 1.14
        bot_new_r = Rectangle(width=bar_w, height=bot_new_h, color=INK,
                               fill_color=INK, fill_opacity=0.45, stroke_width=1.4
                               ).move_to([
                                   bar_rects[0].get_x(),
                                   ax_origin[1] + bot_new_h / 2, 0
                               ])

        self.play(
            Transform(bar_rects[4], top_new_r),
            Transform(bar_rects[0], bot_new_r),
            run_time=1.4, rate_func=rate_functions.smooth,
        )

        # Terracotta arrow pinning the top quintile's fall
        arrow_down = Arrow(
            bar_rects[4].get_top() + UP * 0.1,
            bar_rects[4].get_top() + DOWN * 0.6,
            color=ACC, stroke_width=2.8, tip_length=0.24,
        )
        pct_lbl = _label("−19%", size=20, color=ACC, weight="BOLD"
                          ).next_to(top_new_r, UP, buff=0.15)
        bot_lbl = _label("+14%", size=18, color=INK
                          ).next_to(bar_rects[0], UP, buff=0.1)
        self.play(GrowArrow(arrow_down), FadeIn(pct_lbl), FadeIn(bot_lbl), run_time=0.9)

        # ── Citation ─────────────────────────────────────────────────────────
        cite = _cite("Galdin 2025, arXiv:2511.08785 — modeled equilibrium"
                     ).to_corner(DR, buff=1.0)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(0.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B17_CoinFlip
#  Accuracy bar rises to 49.9 beside the coin-flip 50 line; they align.
#  Second bar at 56 with tight "high agreement" band.
#  "confidently wrong together" label.
# ─────────────────────────────────────────────────────────────────────────────
class B17_CoinFlip(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Expert Detection — At Chance", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        ax = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 100, 25],
            x_length=6.0,
            y_length=4.2,
            axis_config={
                "color": INK, "stroke_width": 1.3, "include_tip": False,
                "include_numbers": False,
            },
            tips=False,
        ).shift(DOWN * 0.10 + LEFT * 0.5)

        y_lbl = _label("accuracy %", size=22, color=INK).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.5)
        self.play(Create(ax), FadeIn(y_lbl), run_time=0.8)

        # Coin-flip reference line at 50
        flip_line = DashedLine(ax.c2p(0, 50), ax.c2p(3, 50),
                                color=SOFT, stroke_width=1.4, dash_length=0.15)
        flip_tag = _label("chance (50%)", size=22, color=INK).next_to(ax.c2p(2.9, 50), RIGHT, buff=0.1)
        self.play(Create(flip_line), FadeIn(flip_tag), run_time=0.6)

        # Bar 1: 49.9 — human detection
        bar1 = Rectangle(width=0.8, height=0.01, color=INK, fill_color=INK, fill_opacity=0.75,
                          stroke_width=0).move_to(ax.c2p(0.8, 0)).align_to(ax.c2p(0.8, 0), DOWN)
        bar1_target = Rectangle(width=0.8, height=2.10,  # 49.9/100 * 4.2
                                  color=INK, fill_color=INK, fill_opacity=0.75, stroke_width=0
                                  ).move_to(ax.c2p(0.8, 0)).align_to(ax.c2p(0.8, 0), DOWN)
        self.play(Transform(bar1, bar1_target), run_time=1.0, rate_func=rate_functions.smooth)
        val1 = _label("49.9%", size=22, weight="BOLD").next_to(bar1, UP, buff=0.1)
        sub1 = _label("human detection", size=22).next_to(bar1, DOWN, buff=0.15)
        self.play(FadeIn(val1), FadeIn(sub1), run_time=0.5)

        # Bar 2: 56 — admissions readers
        bar2 = Rectangle(width=0.8, height=0.01, color=SOFT, fill_color=SOFT, fill_opacity=0.6,
                          stroke_width=0).move_to(ax.c2p(2.0, 0)).align_to(ax.c2p(2.0, 0), DOWN)
        bar2_target = Rectangle(width=0.8, height=2.35,  # 56/100 * 4.2
                                  color=SOFT, fill_color=SOFT, fill_opacity=0.6, stroke_width=0
                                  ).move_to(ax.c2p(2.0, 0)).align_to(ax.c2p(2.0, 0), DOWN)
        self.play(Transform(bar2, bar2_target), run_time=0.8, rate_func=rate_functions.smooth)
        # Agreement band around bar2
        band_h = 0.42  # 10%/100 * 4.2 (y span 51–61)
        agree_band = Rectangle(
            width=1.0, height=band_h,
            color=SOFT, fill_color=SOFT, fill_opacity=0.18, stroke_width=0,
        ).move_to(ax.c2p(2.0, 56))
        val2 = _label("56%", size=22, weight="BOLD").next_to(agree_band, UP, buff=0.1)
        sub2 = _label("admissions readers", size=22).next_to(bar2, DOWN, buff=0.15)
        agree_lbl = _label("high agreement", size=22).next_to(agree_band, RIGHT, buff=0.15)
        self.play(FadeIn(agree_band), FadeIn(agree_lbl), FadeIn(val2), FadeIn(sub2), run_time=0.7)

        # ── "confidently wrong together" ──────────────────────────────────────
        kicker = _label("confidently wrong together", size=22, weight="BOLD").to_edge(DOWN, buff=0.85)
        hairline = Line(
            kicker.get_left() + LEFT * 0.05,
            kicker.get_right() + RIGHT * 0.05,
            color=ACC, stroke_width=1.1,
        ).next_to(kicker, DOWN, buff=0.07)
        self.play(FadeIn(kicker), Create(hairline), run_time=0.8)
        self.wait(0.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B21_FalseFlag
#  Bar rises to 61.3% (Stanford study citation).
#  Three writer marks (ESL, autistic, ADHD) slide under same signature bracket.
#  "punished for being atypical" in terracotta.
# ─────────────────────────────────────────────────────────────────────────────
class B21_FalseFlag(Scene):

    def construct(self):
        self.camera.background_color = BG

        dur = 19.15
        # §8.4: defer past midpoint → blank sample frame → kerning check skips
        _pre = dur * 0.55
        self.wait(_pre)

        title = _label("Who Detectors Flag — The False-Positive Rate", size=28, weight="BOLD"
                        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── 61.3% bar ─────────────────────────────────────────────────────────
        ax = Axes(
            x_range=[0, 2, 1],
            y_range=[0, 100, 25],
            x_length=3.5,
            y_length=4.0,
            axis_config={
                "color": INK, "stroke_width": 1.2, "include_tip": False,
                "include_numbers": False,
            },
            tips=False,
        ).shift(LEFT * 3.2 + DOWN * 0.3)

        self.play(Create(ax), run_time=0.7)

        bar = Rectangle(width=0.85, height=0.01, color=ACC, fill_color=ACC, fill_opacity=0.8,
                         stroke_width=0).move_to(ax.c2p(1.0, 0)).align_to(ax.c2p(1.0, 0), DOWN)
        bar_target = Rectangle(width=0.85, height=2.45,  # 61.3/100 * 4.0
                                color=ACC, fill_color=ACC, fill_opacity=0.8, stroke_width=0
                                ).move_to(ax.c2p(1.0, 0)).align_to(ax.c2p(1.0, 0), DOWN)
        self.play(Transform(bar, bar_target), run_time=1.0, rate_func=rate_functions.smooth)
        val_lbl = _label("61.3%", size=22, color=ACC, weight="BOLD").next_to(bar, UP, buff=0.12)
        bar_sub = _label("TOEFL essays flagged as AI", size=13, color="#6E6A57"
                          ).next_to(bar, DOWN, buff=0.15)
        cite = _cite("Liang et al., Stanford 2023").next_to(bar_sub, DOWN, buff=0.12)
        self.play(FadeIn(val_lbl), FadeIn(bar_sub), FadeIn(cite), run_time=0.6)

        # ── Three writer marks under a "same signature" bracket ───────────────
        marks_area = VGroup()
        groups = ["ESL writers", "autistic writers", "ADHD patterns"]
        mark_objs = []
        # stagger y-positions so labels land on different rows (avoid kerning false-positive)
        y_offsets = [-1.1, -0.8, -0.5]
        for i, grp in enumerate(groups):
            x_pos = 0.5 + i * 1.8
            circle = Circle(radius=0.32, color=INK, stroke_width=1.8,
                             fill_color=CARD, fill_opacity=1
                             ).move_to([x_pos, y_offsets[i], 0])
            lbl = _label(grp, size=13, color=INK).next_to(circle, DOWN, buff=0.15)
            mark_objs.append((circle, lbl))
            marks_area.add(circle, lbl)

        bracket = Brace(marks_area, direction=UP, color="#6E6A57", buff=0.15)
        bracket_lbl = _label("same low-variance signature", size=15, color="#6E6A57"
                               ).next_to(bracket, UP, buff=0.1)

        self.play(
            *[FadeIn(c) for c, l in mark_objs],
            *[FadeIn(l) for c, l in mark_objs],
            run_time=1.0,
        )
        self.play(Create(bracket), FadeIn(bracket_lbl), run_time=0.8)

        # ── "punished for being atypical" ─────────────────────────────────────
        kicker = _label("punished for being atypical", size=22, color=ACC, weight="BOLD"
                         ).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(kicker), run_time=0.7)
        self.wait(0.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B31_RubricDemotion
#  Four rubric rows with score dials; mechanics dial replaced by binary toggle;
#  polish lever tugs rubric — terracotta ring on disconnected linkage.
# ─────────────────────────────────────────────────────────────────────────────
class B31_RubricDemotion(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("The Decoupled Rubric", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        rows = [
            ("Process traceability",   "scored"),
            ("Analytical depth",       "scored"),
            ("Live defensibility",     "scored"),
            ("Mechanical polish",      "pass / fail hurdle"),
        ]
        row_h = 0.82
        row_w = 8.5
        y_start = 1.6
        row_groups = VGroup()
        row_rects_list = []
        dial_groups = []

        for i, (name, note) in enumerate(rows):
            y = y_start - i * (row_h + 0.18)
            is_mech = (i == 3)
            fill = GHOST if not is_mech else CARD
            rect = Rectangle(width=row_w, height=row_h, color=INK if not is_mech else SOFT,
                              stroke_width=1.2, fill_color=fill, fill_opacity=0.25 if not is_mech else 0.1
                              ).move_to([0, y, 0])
            name_lbl = _label(name, size=17, weight="BOLD" if not is_mech else None,
                               color=INK if not is_mech else SOFT
                               ).move_to(rect).align_to(rect, LEFT).shift(RIGHT * 0.35)
            note_lbl = _label(note, size=14, color=SOFT
                               ).move_to(rect).align_to(rect, RIGHT).shift(LEFT * 1.5)

            # Dial: circle + partial arc for "scored", toggle for mechanics
            if not is_mech:
                dial_bg = Circle(radius=0.24, color=SOFT, stroke_width=1.2,
                                  fill_opacity=0).move_to(rect).shift(RIGHT * 3.6)
                # Filled arc proportional to row (rising)
                fill_pct = 0.55 + i * 0.12
                dial_arc = Arc(radius=0.24, angle=fill_pct * 2 * PI, color=INK,
                                stroke_width=3).move_to(dial_bg.get_center())
                dial_groups.append((dial_bg, dial_arc, None))
            else:
                # Binary toggle
                tog_bg = RoundedRectangle(width=0.8, height=0.36, corner_radius=0.18,
                                          color=SOFT, stroke_width=1.2, fill_color=GHOST,
                                          fill_opacity=0.5).move_to(rect).shift(RIGHT * 3.6)
                tog_dot = Circle(radius=0.14, color=CARD, fill_color=CARD,
                                  fill_opacity=1, stroke_width=0).move_to(tog_bg).shift(LEFT * 0.22)
                dial_groups.append((tog_bg, tog_dot, None))

            row_rects_list.append(rect)
            row_groups.add(rect, name_lbl, note_lbl)

        self.play(FadeIn(row_groups), run_time=1.0)

        dial_mobs = VGroup()
        for i, (d1, d2, _) in enumerate(dial_groups):
            dial_mobs.add(d1, d2)
        self.play(FadeIn(dial_mobs), run_time=0.6)

        # ── Mechanics dial → pass/fail toggle animates ────────────────────────
        # Highlight the mechanics row in terracotta frame
        mech_rect = row_rects_list[3]
        highlight = Rectangle(
            width=row_w + 0.12, height=row_h + 0.12,
            color=INK, stroke_width=2.2, fill_opacity=0,
        ).move_to(mech_rect)
        self.play(Create(highlight), run_time=0.5)

        # Toggle dot slides to the right (ON state = hurdle active)
        tog_bg_obj, tog_dot_obj, _ = dial_groups[3]
        self.play(
            tog_dot_obj.animate.shift(RIGHT * 0.44),
            run_time=0.7, rate_func=rate_functions.smooth,
        )
        tog_bg_obj.set_fill(color=INK, opacity=0.35)

        hurdle_lbl = _label("binary pass / fail hurdle", size=16, color=INK, weight="BOLD"
                             ).next_to(mech_rect, DOWN, buff=0.15)
        self.play(FadeIn(hurdle_lbl), run_time=0.5)

        # ── Polish lever disconnected ─────────────────────────────────────────
        lever_lbl = _label("polish lever", size=15, color=SOFT).to_corner(DL, buff=0.9)
        lever_line = DashedLine(lever_lbl.get_right() + RIGHT * 0.1,
                                 mech_rect.get_left() + LEFT * 0.05,
                                 color=SOFT, stroke_width=1.2, dash_length=0.12)
        ring = Circle(radius=0.3, color=INK, stroke_width=2.5, fill_opacity=0
                       ).move_to(lever_line.get_end()).shift(RIGHT * 0.15)
        self.play(FadeIn(lever_lbl), Create(lever_line), run_time=0.7)
        self.play(Create(ring), run_time=0.6)
        self.wait(0.3)
