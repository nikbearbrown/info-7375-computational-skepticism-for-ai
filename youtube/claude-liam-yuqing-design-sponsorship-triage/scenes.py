"""Manim scenes for claude-liam-yuqing-design-sponsorship-triage."""
import json, math
from pathlib import Path
from manim import *
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


# Claude palette
CREAM  = "#F2F0E9"
INK    = "#3D3929"
ACCENT = "#D97757"
SOFT   = "#8B8272"

_SHEET = Path(__file__).parent / "beat_sheet.json"
try:
    _bs = json.loads(_SHEET.read_text())
    DUR  = {b["beat_id"]: b.get("actual_duration_s", 10) for b in _bs["beats"]}
except Exception:
    DUR = {}

def _dur(bid, fallback=10):
    return DUR.get(bid) or fallback

def _bg():
    return Rectangle(width=16, height=9, fill_color=CREAM, fill_opacity=1, stroke_width=0)

def _title(text, y=3.0):
    return Text(text, font="EB Garamond", color=INK, font_size=34).move_to([0, y, 0])

def _spark(text, y=-3.5):
    return Text(text, font="EB Garamond", color=SOFT, font_size=22, slant=NORMAL).move_to([0, y, 0])


class B02_BranchReweightOrNewSignal(Scene):
    """Fork: old signals valid → reweight; new risk factor → new signal."""
    def construct(self):
        dur = _dur("B02", 12)
        self.camera.background_color = CREAM

        bg = _bg()
        title = _title("The Question Forks")
        spark = _spark("Fork in the road.")

        # Root node
        root_box = RoundedRectangle(width=3.2, height=0.9, corner_radius=0.1,
                                    fill_color=SOFT, fill_opacity=0.25,
                                    stroke_color=SOFT, stroke_width=1.5)
        root_lbl = Text("Extend to design", font="EB Garamond", color=INK, font_size=26)
        root = VGroup(root_box, root_lbl).move_to([0, 1.0, 0])

        # Left branch: proxies still valid → reweight
        left_box = RoundedRectangle(width=4.0, height=1.2, corner_radius=0.1,
                                    fill_color=SOFT, fill_opacity=0.18,
                                    stroke_color=SOFT, stroke_width=1.5)
        left_q = Text("Proxies still valid", font="EB Garamond", color=INK, font_size=26)
        left_ans = Text("Reweight", font="EB Garamond", color=INK, font_size=26)
        left_lbl = VGroup(left_q, left_ans).arrange(DOWN, buff=0.05)
        left = VGroup(left_box, left_lbl).move_to([-3.6, -1.0, 0])

        # Right branch: new risk factor → new signal
        right_box = RoundedRectangle(width=4.0, height=1.2, corner_radius=0.1,
                                     fill_color=ACCENT, fill_opacity=0.18,
                                     stroke_color=ACCENT, stroke_width=2.0)
        right_q = Text("New risk factor", font="EB Garamond", color=INK, font_size=26)
        right_ans = Text("New signal", font="EB Garamond", color=INK, font_size=26, weight=BOLD)
        right_lbl = VGroup(right_q, right_ans).arrange(DOWN, buff=0.05)
        right = VGroup(right_box, right_lbl).move_to([3.6, -1.0, 0])

        # Arrows
        fork_pt = [0, 0.1, 0]
        arrow_left  = Arrow(fork_pt, left.get_top() + [0, 0.05, 0],
                            color=SOFT, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        arrow_right = Arrow(fork_pt, right.get_top() + [0, 0.05, 0],
                            color=ACCENT, stroke_width=3, max_tip_length_to_length_ratio=0.15)

        self.add(bg)
        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(root), run_time=0.5)
        self.wait(0.4)
        self.play(GrowArrow(arrow_left), FadeIn(left), run_time=0.9)
        self.wait(0.3)
        self.play(GrowArrow(arrow_right), FadeIn(right), run_time=0.9)
        self.wait(0.5)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(max(0.3, dur - 4.6))


class B03_SettledVsContested(Scene):
    """SWE bar solid in 'qualifies' zone; Design bar wavers at threshold."""
    def construct(self):
        dur = _dur("B03", 14)
        self.camera.background_color = CREAM

        bg = _bg()
        title = _title("Specialty-Occupation Risk")
        spark = _spark("Settled vs contested.")

        # Threshold line
        threshold = Line([-5.5, 0, 0], [5.5, 0, 0], color=SOFT, stroke_width=2)
        above_lbl = Text("Qualifies", font="EB Garamond", color=SOFT, font_size=22).move_to([4.5, 0.4, 0])
        deny_lbl  = Text("Scrutiny", font="EB Garamond", color=SOFT, font_size=22).move_to([4.5, -0.4, 0])
        dashed = DashedLine([-5.5, 0, 0], [5.5, 0, 0], dash_length=0.25, color=SOFT, stroke_width=1.5)

        # SWE bar — solid, comfortably above threshold
        swe_bar = Rectangle(width=2.2, height=2.8, fill_color=SOFT, fill_opacity=0.7, stroke_width=0)
        swe_bar.align_to([0, 0, 0], DOWN).move_to([-2.8, 0, 0])
        swe_bar.shift(UP * 2.8 / 2)
        swe_lbl = Text("SWE / DS", font="EB Garamond", color=INK, font_size=22).next_to(swe_bar, DOWN, buff=0.2)
        swe_note = Text("settled", font="EB Garamond", color=SOFT, font_size=22).next_to(swe_bar, UP, buff=0.15)

        # Design bar — wavers (starts below, animates up through threshold)
        design_bar_low = Rectangle(width=2.2, height=0.6, fill_color=ACCENT, fill_opacity=0.6, stroke_width=0)
        design_bar_low.move_to([2.8, -0.7, 0])
        design_lbl = Text("Design", font="EB Garamond", color=INK, font_size=22).next_to(design_bar_low, DOWN, buff=0.2)

        design_bar_high = Rectangle(width=2.2, height=1.9, fill_color=ACCENT, fill_opacity=0.6, stroke_width=0)
        design_bar_high.move_to([2.8, 0.55, 0])
        design_note = Text("contested", font="EB Garamond", color=INK, font_size=22).next_to(design_bar_high, UP, buff=0.15)

        question = Text("role-specific", font="EB Garamond", color=SOFT, font_size=22).next_to(design_bar_high, RIGHT, buff=0.2)

        self.add(bg)
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(dashed), FadeIn(above_lbl), FadeIn(deny_lbl), run_time=0.6)
        self.play(FadeIn(swe_bar), FadeIn(swe_lbl), FadeIn(swe_note), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(design_bar_low), FadeIn(design_lbl), run_time=0.6)
        self.wait(0.4)
        # Waver: grow up through threshold
        self.play(Transform(design_bar_low, design_bar_high), run_time=1.0)
        self.play(FadeIn(design_note), FadeIn(question), run_time=0.5)
        # Waver back down
        self.play(Transform(design_bar_low, Rectangle(width=2.2, height=0.6,
                                                       fill_color=ACCENT, fill_opacity=0.6,
                                                       stroke_width=0).move_to([2.8, -0.7, 0])),
                  run_time=0.7)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(max(0.3, dur - 6.1))


class B09_ThreeSignalsThreeTreatments(Scene):
    """Three signal rows each get a different tag: lag-adjust, disaggregate, re-baserate."""
    def construct(self):
        dur = _dur("B09", 15)
        self.camera.background_color = CREAM

        bg = _bg()
        title = _title("Three Signals — Three Treatments")
        spark = _spark("Three, not one.")

        signals = [
            ("SEC Form D funding", "lag-adjust"),
            ("Sponsorship history", "disaggregate by job family"),
            ("ATS activity", "re-baserate for design"),
        ]

        rows = VGroup()
        for label, tag in signals:
            sig_box = RoundedRectangle(width=4.0, height=0.9, corner_radius=0.08,
                                       fill_color=SOFT, fill_opacity=0.15,
                                       stroke_color=SOFT, stroke_width=1.0)
            sig_lbl = Text(label, font="EB Garamond", color=INK, font_size=26)
            sig_grp = VGroup(sig_box, sig_lbl).arrange(IN)
            sig_grp[0].move_to([0, 0, 0])
            sig_grp[1].move_to([0, 0, 0])

            arrow = Arrow([2.0, 0, 0], [2.7, 0, 0], color=SOFT, stroke_width=2.5,
                          max_tip_length_to_length_ratio=0.2)

            tag_box = RoundedRectangle(width=4.2, height=0.9, corner_radius=0.08,
                                       fill_color=SOFT, fill_opacity=0.15,
                                       stroke_color=SOFT, stroke_width=1.5)
            tag_lbl = Text(tag, font="EB Garamond", color=INK, font_size=26)
            tag_grp = VGroup(tag_box, tag_lbl).arrange(IN)
            tag_grp[0].move_to([0, 0, 0])
            tag_grp[1].move_to([0, 0, 0])

            row = VGroup(sig_grp, arrow, tag_grp).arrange(RIGHT, buff=0.2)
            rows.add(row)

        rows.arrange(DOWN, buff=0.6).move_to([0, 0.1, 0])

        # "not reweight" stamp that fades
        stamp = Text("not just 'reweight'", font="EB Garamond", color=SOFT, font_size=20,
                     slant=NORMAL).move_to([0, -2.7, 0])

        self.add(bg)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(0.3)
        for row in rows:
            sig_part, arr_part, tag_part = row[0], row[1], row[2]
            self.play(FadeIn(sig_part), run_time=0.5)
            self.play(GrowArrow(arr_part), FadeIn(tag_part), run_time=0.7)
            self.wait(0.3)
        self.play(FadeIn(stamp), run_time=0.5)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(max(0.3, dur - 6.8))


class B11_OverfitThinData(Scene):
    """Curve bends hard through 5 scattered points, fails on 6th held-out point."""
    def construct(self):
        dur = _dur("B11", 14)
        self.camera.background_color = CREAM

        bg = _bg()
        title = _title("Thin Data — Overfitting Risk")
        spark = _spark("Fits cases, not patterns.")

        ax = Axes(
            x_range=[0, 10, 2], y_range=[0, 10, 2],
            x_length=9, y_length=5.5,
            axis_config={"color": SOFT, "stroke_width": 1.5},
            x_axis_config={"include_numbers": False, "include_tip": False},
            y_axis_config={"include_numbers": False, "include_tip": False},
            tips=False,
        ).move_to([0, -0.2, 0])
        x_lbl = Text("Calibration cases", font="EB Garamond", color=SOFT, font_size=26).next_to(ax, DOWN, buff=0.15)
        y_lbl = Text("Predicted score", font="EB Garamond", color=SOFT, font_size=26).rotate(PI/2).next_to(ax, LEFT, buff=0.15)

        # 5 known points (spread, not on one line)
        known_xs = [1, 2.5, 4, 6, 8]
        known_ys = [3, 7, 2, 8, 5]
        known_dots = VGroup(*[
            Dot(ax.c2p(x, y), radius=0.18, color=INK)
            for x, y in zip(known_xs, known_ys)
        ])

        # Overfitted curve passing through all 5
        curve_pts = [ax.c2p(x, y) for x, y in zip(known_xs, known_ys)]
        # Add endpoints at edges
        curve_pts = [ax.c2p(0.3, 5)] + curve_pts + [ax.c2p(9.0, 4)]
        fitted_curve = VMobject(color=SOFT, stroke_width=3)
        fitted_curve.set_points_smoothly(curve_pts)

        # Held-out point at x=9.5, y=7 — far from curve
        held_x, held_y = 9.0, 8.5
        held_dot = Dot(ax.c2p(held_x, held_y), radius=0.18, color=INK)
        held_lbl = Text("held-out", font="EB Garamond", color=INK, font_size=34).next_to(held_dot, UP, buff=0.1)
        miss_arrow = Arrow(ax.c2p(9.0, 4.3), ax.c2p(9.0, 7.9), color=SOFT,
                           stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        miss_lbl = Text("MISS", font="EB Garamond", color=INK, font_size=34, weight=BOLD).next_to(miss_arrow, RIGHT, buff=0.1)

        known_lbl = Text("5 known cases", font="EB Garamond", color=INK, font_size=32).move_to([-3.2, 2.3, 0])

        self.add(bg)
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.7)
        self.play(FadeIn(known_dots), run_time=0.6)
        self.play(Create(fitted_curve), run_time=1.2)
        self.play(FadeIn(known_lbl), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(held_dot), FadeIn(held_lbl), run_time=0.5)
        self.play(GrowArrow(miss_arrow), FadeIn(miss_lbl), run_time=0.7)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(max(0.3, dur - 6.6))


class B16_ConvergeNewSignal(Scene):
    """Reweight path fades; new signal slots in; tracks converge."""
    def construct(self):
        dur = _dur("B16", 14)
        self.camera.background_color = CREAM

        bg = _bg()
        title = _title("Weights ≠ Missing Signal")
        spark = _spark("Recognize the new risk.")

        # Two paths start as fork (reweight vs new signal)
        model_box = RoundedRectangle(width=3.2, height=0.85, corner_radius=0.1,
                                     fill_color=INK, fill_opacity=0.12,
                                     stroke_color=INK, stroke_width=1.5)
        model_lbl = Text("Reallocation Engine", font="EB Garamond", color=INK, font_size=20)
        model = VGroup(model_box, model_lbl).move_to([0, 2.5, 0])

        # Reweight path (left, fades out)
        rw_box = RoundedRectangle(width=3.0, height=0.85, corner_radius=0.1,
                                  fill_color=SOFT, fill_opacity=0.18,
                                  stroke_color=SOFT, stroke_width=1.5)
        rw_lbl = Text("Reweight existing 3", font="EB Garamond", color=SOFT, font_size=20)
        rw = VGroup(rw_box, rw_lbl).move_to([-3.5, 0.4, 0])

        # New signal path (right, brightens)
        ns_box = RoundedRectangle(width=3.2, height=0.85, corner_radius=0.1,
                                  fill_color=SOFT, fill_opacity=0.18,
                                  stroke_color=SOFT, stroke_width=2.0)
        ns_lbl = Text("+ defensibility signal", font="EB Garamond", color=INK, font_size=20, weight=BOLD)
        ns = VGroup(ns_box, ns_lbl).move_to([3.5, 0.4, 0])

        # Arrows from model
        arr_rw = Arrow(model.get_bottom(), rw.get_top(), color=SOFT, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.15)
        arr_ns = Arrow(model.get_bottom(), ns.get_top(), color=SOFT, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.15)

        # Convergence: both paths merge into "new signal, not new weights"
        conv_box = RoundedRectangle(width=4.5, height=0.9, corner_radius=0.1,
                                    fill_color=SOFT, fill_opacity=0.18,
                                    stroke_color=SOFT, stroke_width=2.0)
        conv_lbl = Text("New signal, not new weights.", font="EB Garamond", color=INK,
                        font_size=22, weight=BOLD)
        conv = VGroup(conv_box, conv_lbl).move_to([0, -1.8, 0])

        arr_conv_ns = Arrow(ns.get_bottom(), conv.get_top(), color=SOFT, stroke_width=2.0,
                            max_tip_length_to_length_ratio=0.15)

        self.add(bg)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(model), run_time=0.5)
        self.play(GrowArrow(arr_rw), FadeIn(rw), GrowArrow(arr_ns), FadeIn(ns), run_time=1.0)
        self.wait(0.5)
        # Reweight path fades
        self.play(FadeOut(rw, shift=LEFT * 0.5), FadeOut(arr_rw, shift=LEFT * 0.3), run_time=0.8)
        # New signal converges
        self.play(GrowArrow(arr_conv_ns), FadeIn(conv), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(max(0.3, dur - 5.7))
