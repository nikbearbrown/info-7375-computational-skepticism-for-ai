"""scenes.py — claude-liam-deep-10-visualization
The Chart Isn't Neutral. It's Arguing.
14 Manim scenes — 8 original specs + 6 re-routed from VOX STILL (nopunt pass).

Render one scene:
  cd <reel_dir>
  manim -qk --fps 24 -r 3840,2160 scenes.py A1M_TwoDashboards
  # run.sh does this automatically for all pending scenes
"""
import json, pathlib, math
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)
try:
    _Mx = MarkupText
    MarkupText = lambda *a, font="EB Garamond", **k: _Mx(*a, font=font, **k)
except NameError:
    pass

CREAM  = "#F2F0E9"
INK    = "#3D3929"
ACCENT = "#D97757"
MUTE   = "#7A7265"
TEAL   = "#2A9D8F"
GRAY   = "#C8C4B8"

config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
        for b in _bs["beats"]
    })
except Exception:
    pass

def dur(bid): return DUR.get(bid, 10.0)

def serif(t, sz=40, clr=INK, **k):
    return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)

def caps(t, sz=22, clr=MUTE, weight=BOLD, **k):
    return Text(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=weight, **k)

def mono(t, sz=28, clr=INK, **k):
    return Text(t, font="PT Mono", font_size=sz, color=clr, **k)

def panel(w, h, fill=WHITE, stroke=GRAY, sw=1.5):
    return RoundedRectangle(corner_radius=0.08, width=w, height=h,
                            fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw)

def rule_line(w=6.0, clr=GRAY):
    return Line(ORIGIN, RIGHT * w, color=clr, stroke_width=1.5)

def h_bar(value, max_val, bar_w, bar_h, clr=INK, fill_op=0.85):
    width = (value / max_val) * bar_w
    width = max(0.04, width)
    b = Rectangle(width=width, height=bar_h,
                  fill_color=clr, fill_opacity=fill_op,
                  stroke_width=0)
    b.align_to(ORIGIN, LEFT)
    return b

def v_bar(value, axis_lo, axis_hi, max_h, clr=INK, bar_w=0.5, fill_op=0.85):
    frac = (value - axis_lo) / max(axis_hi - axis_lo, 0.001)
    height = max(0.02, frac * max_h)
    b = Rectangle(width=bar_w, height=height,
                  fill_color=clr, fill_opacity=fill_op,
                  stroke_width=0)
    b.align_to(ORIGIN, DOWN)
    return b


# ─────────────────────────────────────────────────────────────────────────────
# A1M — Two Dashboards, One CSV
# ─────────────────────────────────────────────────────────────────────────────
class A1M_TwoDashboards(Scene):
    def construct(self):
        d = dur("A1M")

        # Canvas split
        left_x, right_x = -3.4, 3.4
        pan_w, pan_h = 5.8, 5.8

        # shared data: two subgroups, overall
        grp_a, grp_b = 96, 82  # percent accuracy

        # ── left dashboard (misleading) ──────────────────────
        left_bg = panel(pan_w, pan_h, fill=WHITE).move_to([left_x, -0.1, 0])
        left_hd = caps("SYSTEM PERFORMANCE REPORT", sz=16, clr=MUTE).move_to([left_x, 2.5, 0])
        big94   = serif("94%", sz=90, clr=INK, weight=BOLD).move_to([left_x, 1.4, 0])
        big_lbl = caps("overall accuracy", sz=18, clr=MUTE).move_to([left_x, 0.35, 0])

        # truncated-axis bars (axis 80–100)
        axis_lo, axis_hi = 80, 100
        bar_h = 1.1
        bar_w = 0.55
        trunc_a = v_bar(grp_a, axis_lo, axis_hi, bar_h, INK, bar_w).move_to([left_x - 0.8, -0.85, 0])
        trunc_b = v_bar(grp_b, axis_lo, axis_hi, bar_h, GRAY, bar_w).move_to([left_x + 0.8, -0.85, 0])
        trunc_a.align_to([0, -1.4, 0], DOWN).shift(LEFT * 0.8)
        trunc_b.align_to([0, -1.4, 0], DOWN).shift(RIGHT * (left_x + 0.8 - left_x + 0.8) * 0 + RIGHT * 0)
        # simpler positioning
        trunc_a = v_bar(grp_a, axis_lo, axis_hi, 1.0, INK, 0.55)
        trunc_b = v_bar(grp_b, axis_lo, axis_hi, 1.0, GRAY, 0.55)
        trunc_a.next_to([left_x - 0.7, -1.4, 0], UP, buff=0)
        trunc_b.next_to([left_x + 0.7, -1.4, 0], UP, buff=0)

        axis_label_lo = caps("80%", sz=14, clr=MUTE).next_to(trunc_a, DOWN, buff=0.05).shift(LEFT * 0.4)
        lbl_a = caps("Group A", sz=13, clr=MUTE).next_to(trunc_a, DOWN, buff=0.22)
        lbl_b = caps("Group B", sz=13, clr=MUTE).next_to(trunc_b, DOWN, buff=0.22)
        cal_tab = panel(1.5, 0.28, fill=GRAY, sw=0).move_to([left_x + 2.0, -2.9, 0])
        cal_txt = caps("Advanced ›", sz=11, clr=WHITE).move_to(cal_tab.get_center())

        left_group = VGroup(left_bg, left_hd, big94, big_lbl,
                            trunc_a, trunc_b, lbl_a, lbl_b, cal_tab, cal_txt)

        # ── right dashboard (honest) ─────────────────────────
        right_bg  = panel(pan_w, pan_h, fill=WHITE).move_to([right_x, -0.1, 0])
        right_hd  = caps("SUBGROUP PERFORMANCE — HONEST BASELINE", sz=14, clr=MUTE).move_to([right_x, 2.5, 0])
        honest_note = serif("same data", sz=26, clr=INK).move_to([right_x, 2.0, 0])

        # honest bars (axis 0–100)
        h_grp_a = v_bar(96, 0, 100, 2.4, INK, 0.55)
        h_grp_b = v_bar(82, 0, 100, 2.4, ACCENT, 0.55)
        h_grp_a.next_to([right_x - 0.7, -1.4, 0], UP, buff=0)
        h_grp_b.next_to([right_x + 0.7, -1.4, 0], UP, buff=0)

        zero_lbl  = caps("0%", sz=14, clr=MUTE).next_to([right_x - 1.5, -1.42, 0], LEFT, buff=0.1)
        pct96     = caps("96%", sz=14, clr=INK).next_to(h_grp_a, UP, buff=0.14)
        pct82     = caps("82%", sz=14, clr=INK).next_to(h_grp_b, UP, buff=0.14)
        # Gap arrow sits to the RIGHT of bar B so it never overprints pct82.
        # Bar B center is right_x+0.7; bar half-width 0.275 → right edge ≈ right_x+0.975.
        # Arrow at right_x+1.5 sits clearly in the open panel space.
        _gap_x    = right_x + 1.5
        gap_arrow = DoubleArrow([_gap_x, h_grp_b.get_top()[1], 0],
                                [_gap_x, h_grp_a.get_top()[1], 0],
                                color=ACCENT, buff=0.0, stroke_width=2.5,
                                tip_length=0.15)
        gap_lbl   = caps("14 pt gap", sz=14, clr=INK).next_to(gap_arrow, RIGHT, buff=0.10)
        h_lbl_a   = caps("Group A", sz=13, clr=MUTE).next_to(h_grp_a, DOWN, buff=0.22)
        h_lbl_b   = caps("Group B", sz=13, clr=MUTE).next_to(h_grp_b, DOWN, buff=0.22)

        # calibration visible
        cal_vis = panel(3.2, 0.35, fill=CREAM, stroke=ACCENT, sw=1.5).move_to([right_x, -2.8, 0])
        cal_vis_t = caps("calibration — overconfident", sz=13, clr=INK).move_to(cal_vis.get_center())

        right_group = VGroup(right_bg, right_hd, honest_note,
                             h_grp_a, h_grp_b, zero_lbl, pct96, pct82,
                             gap_arrow, gap_lbl, h_lbl_a, h_lbl_b,
                             cal_vis, cal_vis_t)

        # ── divider label (above both panels, safely within ±3.4 safe area) ──
        vs_label = caps("one CSV", sz=22, clr=MUTE).move_to([0, 3.1, 0])

        # ── animate ──────────────────────────────────────────
        self.play(FadeIn(left_bg), FadeIn(right_bg), run_time=0.4)
        self.play(FadeIn(vs_label), run_time=0.5)
        self.play(FadeIn(left_hd), FadeIn(right_hd), run_time=0.4)
        self.play(Write(big94), FadeIn(big_lbl), run_time=0.7)
        self.play(FadeIn(honest_note), run_time=0.4)
        self.play(
            Create(trunc_a), Create(trunc_b),
            Create(h_grp_a), Create(h_grp_b),
            run_time=0.8
        )
        self.play(
            FadeIn(lbl_a), FadeIn(lbl_b),
            FadeIn(h_lbl_a), FadeIn(h_lbl_b),
            FadeIn(zero_lbl), FadeIn(pct96), FadeIn(pct82),
            run_time=0.4
        )
        self.play(Create(gap_arrow), FadeIn(gap_lbl), run_time=0.5)
        self.play(FadeIn(cal_tab), FadeIn(cal_txt), FadeIn(cal_vis), FadeIn(cal_vis_t), run_time=0.4)
        self.wait(max(0.1, d - 4.5))


# ─────────────────────────────────────────────────────────────────────────────
# A2M — The argument before the number (form argues)
# ─────────────────────────────────────────────────────────────────────────────
class A2M_FormArgues(Scene):
    def construct(self):
        d = dur("A2M")

        # Two layout panels
        left_x, right_x = -3.5, 3.5
        pan_w, pan_h = 5.6, 6.0

        left_bg  = panel(pan_w, pan_h, fill=WHITE).move_to([left_x, 0, 0])
        right_bg = panel(pan_w, pan_h, fill=WHITE).move_to([right_x, 0, 0])

        # ── LEFT: headline-dominant layout ───────────────────
        left_lbl = caps("headline sufficient", sz=16, clr=INK).move_to([left_x, 2.55, 0])
        # big dominant metric
        metric_box = panel(4.2, 2.0, fill=CREAM, stroke=INK, sw=1.5).move_to([left_x, 1.0, 0])
        metric_val = serif("94.2%", sz=80, clr=INK, weight=BOLD).move_to([left_x, 1.05, 0])
        metric_lbl = caps("accuracy", sz=18, clr=MUTE).next_to(metric_val, DOWN, buff=0.1)

        # tiny fading sub-charts below
        sub1 = panel(1.0, 0.9, fill=GRAY, stroke=GRAY, sw=0).move_to([left_x - 1.5, -1.0, 0]).set_opacity(0.3)
        sub2 = panel(1.0, 0.9, fill=GRAY, stroke=GRAY, sw=0).move_to([left_x, -1.0, 0]).set_opacity(0.2)
        sub3 = panel(1.0, 0.9, fill=GRAY, stroke=GRAY, sw=0).move_to([left_x + 1.5, -1.0, 0]).set_opacity(0.1)

        # eye-path arrow: hits headline and stops (anchored inside panel, label to right)
        eye_l = Arrow([left_x - 1.8, 2.6, 0], [left_x - 1.8, 0.5, 0],
                      color=ACCENT, stroke_width=3, tip_length=0.22)
        stop_dot = Dot([left_x - 1.8, 0.5, 0], color=ACCENT, radius=0.14)
        eye_l_lbl = caps("stops", sz=11, clr=ACCENT).next_to(stop_dot, LEFT, buff=0.14)

        left_group = VGroup(left_bg, left_lbl, metric_box, metric_val, metric_lbl,
                            sub1, sub2, sub3)

        # ── RIGHT: equal-weight panel grid ───────────────────
        right_lbl = caps("integration required", sz=16, clr=INK).move_to([right_x, 2.55, 0])
        cell_w, cell_h = 2.2, 2.2
        cells = []
        labels = ["Subgroup A", "Subgroup B", "Calibration", "Over time"]
        for i, lbl in enumerate(labels):
            col = i % 2
            row = i // 2
            x = right_x - 1.2 + col * 2.5
            y = 1.2 - row * 2.6
            c = panel(cell_w, cell_h, fill=CREAM, stroke=GRAY, sw=1.2).move_to([x, y, 0])
            l = caps(lbl, sz=15, clr=MUTE).move_to([x, y, 0])
            cells.append(VGroup(c, l))

        # eye-path: U-shape (TL→TR→BR→BL) — avoids the diagonal that crossed cells
        path_pts = [
            [right_x - 2.2, 1.6, 0],  # top-left  (above row-0 labels at y=1.2)
            [right_x + 2.2, 1.6, 0],  # top-right
            [right_x + 2.2, -1.8, 0], # bottom-right (below row-1 labels at y=-1.4)
            [right_x - 2.2, -1.8, 0], # bottom-left
        ]
        eye_r = VMobject(color=ACCENT, stroke_width=3)
        eye_r.set_points_as_corners(path_pts)

        right_group = VGroup(right_bg, right_lbl, *cells)

        # ── animate ──────────────────────────────────────────
        self.play(FadeIn(left_bg), FadeIn(right_bg), run_time=0.4)
        self.play(FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.4)
        self.play(FadeIn(metric_box), run_time=0.3)
        self.play(Write(metric_val), FadeIn(metric_lbl), run_time=0.6)
        self.play(FadeIn(sub1), FadeIn(sub2), FadeIn(sub3), run_time=0.4)
        for c in cells:
            self.play(FadeIn(c), run_time=0.25)
        self.play(Create(eye_l), run_time=0.5)
        self.play(FadeIn(stop_dot), FadeIn(eye_l_lbl), run_time=0.3)
        self.play(Create(eye_r), run_time=0.8)
        self.wait(max(0.1, d - 6.0))


# ─────────────────────────────────────────────────────────────────────────────
# A3M — The Perception Hierarchy (Cleveland–McGill ordering)
# ─────────────────────────────────────────────────────────────────────────────
class A3M_PerceptionHierarchy(Scene):
    def construct(self):
        d = dur("A3M")

        value = 0.62  # the encoded value
        channels = [
            ("Position on shared scale", "best"),
            ("Length (bar)",             "good"),
            ("Angle (pie wedge)",        "fair"),
            ("Area (bubble)",            "poor"),
            ("Volume (3-D block)",       "worse"),
            ("Color saturation",         "weakest"),
        ]
        clrs = [TEAL, TEAL, INK, MUTE, GRAY, GRAY]
        n = len(channels)
        row_h = 1.02
        y_top = (n - 1) / 2 * row_h

        title = serif("Cleveland – McGill Perception Ranking", sz=36, clr=INK).move_to([0, 2.9, 0])
        sub   = caps("same value (0.62) — best to worst", sz=20, clr=MUTE).next_to(title, DOWN, buff=0.15)

        self.play(FadeIn(title), FadeIn(sub), run_time=0.5)

        for i, ((name, qual), clr) in enumerate(zip(channels, clrs)):
            y = y_top - i * row_h - 0.6

            # rank badge
            rank_bg = Circle(radius=0.22, color=clr, fill_opacity=0.12, stroke_width=2)
            rank_bg.move_to([-5.8, y, 0])
            rank_n = serif(str(i + 1), sz=22, clr=clr, weight=BOLD).move_to(rank_bg.get_center())

            # channel name
            name_lbl = serif(name, sz=28, clr=clr if i < 2 else INK).move_to([-3.2, y, 0]).align_to([-5.0, 0, 0], LEFT)

            # visual encoding demo
            demo = self._make_demo(i, value, clr, y)

            # error band (widens with rank)
            band_w = 0.06 + i * 0.22
            band = Rectangle(width=band_w, height=0.35,
                             fill_color=ACCENT, fill_opacity=0.25, stroke_width=0)
            band.move_to([4.6, y, 0])
            err_lbl = caps(qual, sz=16, clr=INK if i >= 3 else MUTE).next_to(band, RIGHT, buff=0.1)

            self.play(
                FadeIn(rank_bg), FadeIn(rank_n),
                FadeIn(name_lbl), FadeIn(demo),
                FadeIn(band), FadeIn(err_lbl),
                run_time=0.35
            )

        self.wait(max(0.1, d - n * 0.35 - 0.9))

    def _make_demo(self, i, v, clr, y):
        x = 1.8
        if i == 0:  # position on shared scale
            ax = Line([x - 0.5, y, 0], [x + 0.5, y, 0], color=GRAY, stroke_width=2)
            dot = Dot([x - 0.5 + v, y, 0], color=clr, radius=0.12)
            return VGroup(ax, dot)
        if i == 1:  # bar
            b = Rectangle(width=v * 0.9, height=0.32, fill_color=clr, fill_opacity=0.8, stroke_width=0)
            b.next_to([x - 0.45, y, 0], RIGHT, buff=0)
            baseline = Line([x - 0.45, y - 0.16, 0], [x - 0.45, y + 0.16, 0], color=GRAY, stroke_width=1.5)
            return VGroup(b, baseline)
        if i == 2:  # angle (pie wedge)
            angle = v * 2 * math.pi
            arc = Arc(radius=0.3, start_angle=PI / 2, angle=-angle, color=clr, stroke_width=0)
            arc.move_to([x, y, 0])
            fill = Sector(radius=0.3, start_angle=PI / 2, angle=-angle,
                         fill_color=clr, fill_opacity=0.7, stroke_width=0)
            fill.move_to([x, y, 0])
            return VGroup(fill)
        if i == 3:  # area (bubble)
            r = math.sqrt(v) * 0.38
            return Circle(radius=r, color=clr, fill_opacity=0.6, stroke_width=0).move_to([x, y, 0])
        if i == 4:  # volume (3-D block)
            s = v ** (1 / 3) * 0.42
            sq = Square(side_length=s, fill_color=clr, fill_opacity=0.5, stroke_width=1, stroke_color=clr)
            sq.move_to([x, y, 0])
            return sq
        # color swatch
        swatch = Rectangle(width=0.8, height=0.32,
                           fill_color=clr, fill_opacity=v, stroke_width=0).move_to([x, y, 0])
        return swatch


# ─────────────────────────────────────────────────────────────────────────────
# A3M2 — Length vs Area: double the value, quadruple the ink
# ─────────────────────────────────────────────────────────────────────────────
class A3M2_LengthVsArea(Scene):
    def construct(self):
        d = dur("A3M2")

        title = serif("Double the value — different encodings", sz=38, clr=INK).to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)

        # ── TOP ROW: bars — bottoms anchored at y=0 (above separator) ────────
        # bar heights 0.7 / 1.4 (2:1 ratio); top_lbl sits clear above bar2 top
        bar1 = Rectangle(width=0.7, height=0.7, fill_color=INK, fill_opacity=0.85, stroke_width=0)
        bar2 = Rectangle(width=0.7, height=1.4, fill_color=INK, fill_opacity=0.85, stroke_width=0)
        bar1.move_to([-2.0, 0.0 + 0.7 / 2, 0])   # bottom at y=0, top at y=0.7
        bar2.move_to([2.0, 0.0 + 1.4 / 2, 0])     # bottom at y=0, top at y=1.4
        bar1_val = caps("1", sz=22, clr=MUTE).next_to(bar1, UP, buff=0.1)
        bar2_val = caps("2", sz=22, clr=INK, weight=BOLD).next_to(bar2, UP, buff=0.1)
        bar_ok = caps("reads as 2×  ✓", sz=18, clr=TEAL).move_to([0, 2.0, 0])
        top_lbl = caps("Length (bar) — reads correctly", sz=20, clr=TEAL).move_to([0, 2.4, 0])

        self.play(FadeIn(top_lbl), run_time=0.3)
        self.play(Create(bar1), Create(bar2), run_time=0.6)
        self.play(FadeIn(bar1_val), FadeIn(bar2_val), run_time=0.3)
        self.play(FadeIn(bar_ok), run_time=0.3)

        sep = rule_line(10.0, GRAY).move_to([0, -0.1, 0])
        self.play(Create(sep), run_time=0.2)

        # ── BOTTOM ROW: bubbles (bot_y=-1.8 keeps circle top at -0.7, clear of sep)
        bot_y = -1.8
        bot_lbl = caps("Area (bubble) — radius doubled → area quadruples", sz=18, clr=INK).move_to([0, -0.4, 0])
        self.play(FadeIn(bot_lbl), run_time=0.3)

        r1 = 0.55
        r2_correct = r1 * math.sqrt(2)
        r2_wrong   = r1 * 2.0

        c1 = Circle(radius=r1, fill_color=MUTE, fill_opacity=0.5, stroke_width=0).move_to([-3.5, bot_y, 0])
        c2w = Circle(radius=r2_wrong, fill_color=ACCENT, fill_opacity=0.6, stroke_width=0).move_to([1.8, bot_y, 0])

        c1_lbl  = caps("value = 1", sz=16, clr=MUTE).next_to(c1, DOWN, buff=0.1)
        c2w_lbl = caps("value = 2\n(radius ×2)", sz=16, clr=INK).next_to(c2w, RIGHT, buff=0.15)

        inflated = caps("reads as ~4×  ✗", sz=20, clr=INK, weight=BOLD).move_to([0, bot_y - 1.1, 0])

        arr = Arrow(c1.get_right(), c2w.get_left(), color=ACCENT, stroke_width=2.5, tip_length=0.2)
        arr_lbl = serif("×2 value\n×4 ink", sz=26, clr=INK).next_to(arr, UP, buff=0.12)

        self.play(Create(c1), FadeIn(c1_lbl), run_time=0.4)
        self.play(Create(c2w), FadeIn(c2w_lbl), run_time=0.5)
        self.play(Create(arr), FadeIn(arr_lbl), run_time=0.4)
        self.play(FadeIn(inflated), run_time=0.3)

        bot_rule = caps("reach for area only when precision doesn't matter — volume never", sz=16, clr=MUTE)
        bot_rule.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(bot_rule), run_time=0.3)
        self.wait(max(0.1, d - 4.2))


# ─────────────────────────────────────────────────────────────────────────────
# A4M — Truncated axis: floor rising, visual ratio climbing
# ─────────────────────────────────────────────────────────────────────────────
class A4M_TruncatedAxis(Scene):
    def construct(self):
        d = dur("A4M")

        v_a, v_b = 92.1, 94.3
        title = serif("A 2-point gap, drawn as a landslide", sz=38, clr=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.4)

        max_h = 3.0
        bar_w = 0.9
        base_y = -2.5
        left_x, right_x = -1.4, 1.4

        # Axis labels
        def make_bar_and_axis(axis_lo, animate=False):
            axis_hi = 100.0
            frac_a = (v_a - axis_lo) / (axis_hi - axis_lo)
            frac_b = (v_b - axis_lo) / (axis_hi - axis_lo)
            h_a = max(0.04, frac_a * max_h)
            h_b = max(0.04, frac_b * max_h)

            bar_a = Rectangle(width=bar_w, height=h_a,
                              fill_color=INK, fill_opacity=0.85, stroke_width=0)
            bar_a.align_to([left_x, base_y, 0], DOWN + LEFT).shift(LEFT * (bar_w / 2 - 0))
            bar_a.move_to([left_x, base_y + h_a / 2, 0])

            bar_b = Rectangle(width=bar_w, height=h_b,
                              fill_color=ACCENT, fill_opacity=0.85, stroke_width=0)
            bar_b.move_to([right_x, base_y + h_b / 2, 0])

            floor_line = Line([-3.0, base_y, 0], [3.0, base_y, 0], color=INK, stroke_width=2)
            lo_lbl = caps(f"{int(axis_lo)}%", sz=18, clr=MUTE).move_to([-3.2, base_y, 0])

            lbl_a = caps("Model A\n92.1%", sz=16, clr=INK).next_to(bar_a, UP, buff=0.08)
            lbl_b = caps("Model B\n94.3%", sz=16, clr=INK).next_to(bar_b, UP, buff=0.08)

            return bar_a, bar_b, floor_line, lo_lbl, lbl_a, lbl_b, h_a, h_b

        # ── PHASE 1: honest full axis (0–100) ────────────────
        bar_a0, bar_b0, floor0, lo0, la0, lb0, h_a0, h_b0 = make_bar_and_axis(0)
        ratio0_txt = caps("visual ratio: 1.0×", sz=20, clr=INK).move_to([0, 1.6, 0])
        delta_txt  = caps("true delta: 2.2 points", sz=18, clr=MUTE).move_to([0, 1.1, 0])
        honest_lbl = caps("axis from 0 %", sz=18, clr=TEAL).move_to([0, -3.2, 0])

        self.play(Create(floor0), FadeIn(lo0), run_time=0.3)
        self.play(Create(bar_a0), Create(bar_b0), run_time=0.7)
        self.play(FadeIn(la0), FadeIn(lb0), FadeIn(ratio0_txt), FadeIn(delta_txt), FadeIn(honest_lbl), run_time=0.4)
        self.wait(0.8)

        # ── PHASE 2: truncate axis to 91 (ValueTracker) ─────
        trunc_msg = caps("axis floor rises to 91 %…", sz=20, clr=INK).move_to([0, -3.2, 0])
        self.play(FadeOut(honest_lbl), FadeIn(trunc_msg), run_time=0.3)

        tracker = ValueTracker(0)

        bar_a_t = always_redraw(lambda: Rectangle(
            width=bar_w,
            height=max(0.04, ((v_a - tracker.get_value()) / (100 - tracker.get_value())) * max_h),
            fill_color=INK, fill_opacity=0.85, stroke_width=0
        ).move_to([left_x, base_y + max(0.04, ((v_a - tracker.get_value()) / (100 - tracker.get_value())) * max_h) / 2, 0]))

        bar_b_t = always_redraw(lambda: Rectangle(
            width=bar_w,
            height=max(0.04, ((v_b - tracker.get_value()) / (100 - tracker.get_value())) * max_h),
            fill_color=ACCENT, fill_opacity=0.85, stroke_width=0
        ).move_to([right_x, base_y + max(0.04, ((v_b - tracker.get_value()) / (100 - tracker.get_value())) * max_h) / 2, 0]))

        lo_lbl_t = always_redraw(lambda: caps(f"{int(tracker.get_value())}%", sz=18, clr=INK)
                                 .move_to([-3.2, base_y, 0]))

        ratio_t = always_redraw(lambda: caps(
            f"visual ratio: {((v_b - tracker.get_value()) / max(0.001, v_a - tracker.get_value())):.1f}×",
            sz=20, clr=INK
        ).move_to([0, 1.6, 0]))

        self.remove(bar_a0, bar_b0, lo0, ratio0_txt)
        self.add(bar_a_t, bar_b_t, lo_lbl_t, ratio_t)

        self.play(tracker.animate.set_value(91), run_time=2.8, rate_func=rate_functions.ease_in_out_cubic)
        self.wait(0.6)

        final_lbl = caps("2.2 points → drawn as a landslide", sz=20, clr=INK).move_to([0, -3.2, 0])
        self.play(FadeOut(trunc_msg), FadeIn(final_lbl), run_time=0.3)
        self.wait(max(0.1, d - 6.0))


# ─────────────────────────────────────────────────────────────────────────────
# A4M2 — Same pixels, two morals
# ─────────────────────────────────────────────────────────────────────────────
class A4M2_SamePixels(Scene):
    def construct(self):
        d = dur("A4M2")

        title = serif("The choice is not in the pixels", sz=40, clr=INK).to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)

        # Central chart
        chart_bg = panel(3.2, 2.4, fill=WHITE, stroke=GRAY, sw=1.5).move_to([0, -0.2, 0])
        bar1 = Rectangle(width=0.55, height=1.1, fill_color=INK, fill_opacity=0.8, stroke_width=0)
        bar2 = Rectangle(width=0.55, height=1.55, fill_color=MUTE, fill_opacity=0.7, stroke_width=0)
        bar1.move_to([-0.65, -0.65, 0])
        bar2.move_to([0.65, -0.42, 0])
        chart_lbl = caps("the same chart", sz=16, clr=MUTE).next_to(chart_bg, DOWN, buff=0.1)

        self.play(FadeIn(chart_bg), Create(bar1), Create(bar2), FadeIn(chart_lbl), run_time=0.6)

        # Two bubble labels forking off
        # Left bubble: HONEST INTENT
        honest_box = panel(2.8, 1.2, fill=CREAM, stroke=TEAL, sw=2).move_to([-4.2, 1.6, 0])
        honest_txt = serif("Honest\nintent", sz=28, clr=TEAL, weight=BOLD).move_to([-4.2, 1.6, 0])
        honest_arr = CurvedArrow([-2.8, 1.2, 0], [-0.9, 0.6, 0], color=TEAL,
                                 stroke_width=2.5, angle=0.5, tip_length=0.2)

        # Right bubble: DECEPTIVE INTENT
        decept_box = panel(2.8, 1.2, fill=CREAM, stroke=ACCENT, sw=2).move_to([4.2, 1.6, 0])
        decept_txt = serif("Deceptive\nintent", sz=28, clr=INK, weight=BOLD).move_to([4.2, 1.6, 0])
        decept_arr = CurvedArrow([2.8, 1.2, 0], [0.9, 0.6, 0], color=ACCENT,
                                 stroke_width=2.5, angle=-0.5, tip_length=0.2)

        self.play(
            FadeIn(honest_box), FadeIn(honest_txt), Create(honest_arr),
            run_time=0.5
        )
        self.play(
            FadeIn(decept_box), FadeIn(decept_txt), Create(decept_arr),
            run_time=0.5
        )

        # Magnifier scanning — just a circle moving across the chart
        magnifier = Circle(radius=0.4, color=INK, stroke_width=2.5).move_to([-0.9, -0.2, 0])
        mag_glass  = Line([0.22, -0.3, 0], [0.4, -0.5, 0], color=INK, stroke_width=3)
        mag_grp = VGroup(magnifier, mag_glass)
        self.play(FadeIn(mag_grp), run_time=0.3)
        self.play(mag_grp.animate.move_to([0, -0.2, 0]), run_time=0.4)
        self.play(mag_grp.animate.move_to([0.9, -0.2, 0]), run_time=0.4)

        no_diff = caps("no difference found in the pixels", sz=18, clr=MUTE).move_to([0, -2.3, 0])
        self.play(FadeIn(no_diff), FadeOut(mag_grp), run_time=0.4)

        conclusion = serif("Only the choice differs — and the choice is invisible.", sz=30, clr=INK)
        conclusion.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(conclusion), run_time=0.4)
        self.wait(max(0.1, d - 4.5))


# ─────────────────────────────────────────────────────────────────────────────
# A5M — Inverted axis: the Florida firearm spike drawn as a fall
# ─────────────────────────────────────────────────────────────────────────────
class A5M_InvertedAxis(Scene):
    def construct(self):
        d = dur("A5M")

        # Approximate FL firearm murder counts (illustrative)
        years = list(range(1990, 2013))
        counts = [
            450, 440, 430, 410, 395, 380, 375, 380, 370, 365,
            355, 350, 360, 380, 400, 510,  # 2005 = Stand Your Ground
            720, 800, 855, 820, 780, 750, 720
        ]
        # Subset: 1999–2012
        y_data = [(yr, ct) for yr, ct in zip(years, counts) if yr >= 1999]

        title = serif("accurate numbers — reversed meaning", sz=36, clr=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.4)

        def make_axes_and_line(inverted, label_txt, label_clr):
            ax_x0, ax_x1 = -5.5, 5.5
            ax_y_base = -2.8
            ax_h = 4.5

            min_c, max_c = 340, 880
            x_range = len(y_data) - 1

            def px(yr):
                idx = [r[0] for r in y_data].index(yr)
                return ax_x0 + idx / x_range * (ax_x1 - ax_x0)

            def py(ct):
                frac = (ct - min_c) / (max_c - min_c)
                if inverted:
                    frac = 1 - frac
                return ax_y_base + frac * ax_h

            x_axis = Line([ax_x0, ax_y_base, 0], [ax_x1, ax_y_base, 0], color=INK, stroke_width=2)
            y_axis = Line([ax_x0, ax_y_base, 0], [ax_x0, ax_y_base + ax_h, 0], color=INK, stroke_width=2)

            if inverted:
                lo_lbl = caps("high", sz=16, clr=MUTE).next_to([ax_x0, ax_y_base, 0], LEFT, buff=0.1)
                hi_lbl = caps("low",  sz=16, clr=MUTE).next_to([ax_x0, ax_y_base + ax_h, 0], LEFT, buff=0.1)
            else:
                lo_lbl = caps("0",    sz=16, clr=MUTE).next_to([ax_x0, ax_y_base, 0], LEFT, buff=0.1)
                hi_lbl = caps("900",  sz=16, clr=MUTE).next_to([ax_x0, ax_y_base + ax_h, 0], LEFT, buff=0.1)

            pts = [[px(yr), py(ct), 0] for yr, ct in y_data]
            line = VMobject(color=INK, stroke_width=2.5)
            line.set_points_as_corners(pts)

            # 2005 marker
            x2005 = px(2005)
            marker = DashedLine([x2005, ax_y_base, 0], [x2005, ax_y_base + ax_h, 0],
                                color=ACCENT, stroke_width=2)
            m_lbl = caps("2005 SYG", sz=16, clr=INK).move_to([x2005 + 0.55, ax_y_base + 0.3, 0])

            yr_labels = VGroup()
            for yr in [1999, 2003, 2007, 2012]:
                if yr in [r[0] for r in y_data]:
                    xp = px(yr)
                    t = caps(str(yr), sz=16, clr=MUTE).move_to([xp, ax_y_base - 0.3, 0])
                    yr_labels.add(t)

            reading_lbl = panel(4.8, 0.5, fill=CREAM if not inverted else CREAM, stroke=label_clr, sw=1.5)
            reading_lbl.move_to([1.5, ax_y_base + ax_h + 0.4, 0])
            reading_txt = caps(label_txt, sz=16, clr=INK).move_to(reading_lbl.get_center())

            return VGroup(x_axis, y_axis, lo_lbl, hi_lbl, line, marker, m_lbl, yr_labels,
                          reading_lbl, reading_txt)

        # ── PHASE 1: inverted axis ───────────────────────────
        grp_inv = make_axes_and_line(True, "killings appear to fall after 2005", ACCENT)
        inv_arrow = Arrow(start=[-5.5, 1.2, 0], end=[-5.5, -2.4, 0],
                          color=ACCENT, stroke_width=3, tip_length=0.22)
        self.play(Create(grp_inv), FadeIn(inv_arrow), run_time=1.2)
        self.wait(0.8)

        # ── PHASE 2: flip axis ──────────────────────────────
        self.play(FadeOut(inv_arrow), run_time=0.3)
        grp_hon = make_axes_and_line(False, "killings spike after 2005", TEAL)
        self.play(FadeOut(grp_inv), FadeIn(grp_hon), run_time=0.8)

        note = caps("521 → 740 → 825  (2005–07)", sz=18, clr=INK).move_to([2.0, 0.2, 0])
        self.play(FadeIn(note), run_time=0.3)
        self.wait(max(0.1, d - 4.6))


# ─────────────────────────────────────────────────────────────────────────────
# A5V1 — Challenger: the chart that was never drawn (temperature vs failure)
# Re-routed from VOX STILL — nopunt pass 2026-07-30
# ─────────────────────────────────────────────────────────────────────────────
class A5V1_ChallengerChart(Scene):
    def construct(self):
        d = dur("A5V1")

        title = serif("The chart that would have made it legible", sz=36, clr=INK).to_edge(UP, buff=0.65)
        sub   = caps("O-ring damage vs launch temperature — illustrative reconstruction", sz=16, clr=MUTE)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=0.4)

        # Axes — ax_x0 moved right (y-label/cold-label within ±6.3); ax_y0 raised (-2.8→-2.2)
        # to give tick labels (y=-2.5) and caption (y≈-3.16) separate rows
        ax_x0, ax_x1 = -3.5, 4.5
        ax_y0, ax_y1 = -2.2, 2.2
        x_axis = Line([ax_x0, ax_y0, 0], [ax_x1, ax_y0, 0], color=INK, stroke_width=2)
        y_axis = Line([ax_x0, ax_y0, 0], [ax_x0, ax_y1, 0], color=INK, stroke_width=2)
        x_lbl  = caps("temp. (°F)", sz=14, clr=MUTE).move_to([ax_x1 + 0.7, ax_y0, 0])
        y_lbl  = caps("O-ring damage\nincidents", sz=16, clr=MUTE).next_to(y_axis, LEFT, buff=0.15)

        # Tick marks
        temp_range = (50, 82)
        dmg_range  = (0, 4)
        def px(t): return ax_x0 + (t - temp_range[0]) / (temp_range[1] - temp_range[0]) * (ax_x1 - ax_x0)
        def py(d_): return ax_y0 + (d_ - dmg_range[0]) / (dmg_range[1] - dmg_range[0]) * (ax_y1 - ax_y0)

        ticks_x = VGroup()
        for t in [50, 55, 60, 65, 70, 75, 80]:
            x = px(t)
            ticks_x.add(Line([x, ax_y0 - 0.08, 0], [x, ax_y0 + 0.08, 0], color=INK, stroke_width=1.5))
            ticks_x.add(caps(str(t), sz=14, clr=MUTE).move_to([x, ax_y0 - 0.3, 0]))

        # Data: launches with O-ring incidents (approximate from Tufte)
        incidents = [
            (53, 3), (57, 1), (58, 1), (63, 1), (70, 1), (75, 2), (75, 1)
        ]
        # Safe launches (no incidents) — wider temperature spread
        safe = [66, 67, 68, 69, 70, 72, 73, 75, 76, 78, 79, 80, 81]

        self.play(Create(x_axis), Create(y_axis), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(FadeIn(ticks_x), run_time=0.2)

        # Plot safe launches first (gray dots)
        safe_dots = VGroup()
        for t in safe:
            dot = Dot([px(t), py(0), 0], color=GRAY, radius=0.10)
            safe_dots.add(dot)
        self.play(LaggedStart(*[FadeIn(d) for d in safe_dots], lag_ratio=0.07), run_time=0.6)

        # Plot incident launches (terracotta dots, slightly jittered y)
        incident_dots = VGroup()
        jitters = [0, 0.05, -0.05, 0.08, 0, 0.06, -0.06]
        for (t, cnt), jitter in zip(incidents, jitters):
            for c in range(cnt):
                yy = py(c + 0.1 * jitter)
                dot = Dot([px(t), yy, 0], color=ACCENT, radius=0.10)
                incident_dots.add(dot)
        self.play(LaggedStart(*[FadeIn(d) for d in incident_dots], lag_ratio=0.1), run_time=0.8)

        # Trend line suggestion (hand-drawn style)
        trend = CurvedArrow([px(80), py(0.1), 0], [px(53), py(2.8), 0],
                            color=MUTE, stroke_width=2.5, angle=-0.3, tip_length=0.22)
        trend_lbl = serif("damage worsens\nas temperature drops", sz=26, clr=INK).move_to([1.0, 1.3, 0])
        self.play(Create(trend), run_time=0.5)
        self.play(FadeIn(trend_lbl), run_time=0.3)

        # Forecast launch temp arrow: 29°F — off chart to the left
        cold_arrow = Arrow([px(50) - 0.3, py(0.5), 0], [ax_x0 - 0.9, py(0.5), 0],
                           color=MUTE, stroke_width=3, tip_length=0.25)
        cold_lbl = caps("29°F\nforecast", sz=16, clr=INK).next_to(cold_arrow, LEFT, buff=0.08)
        self.play(Create(cold_arrow), FadeIn(cold_lbl), run_time=0.4)

        caption = serif("The evidence was there. The chart was never drawn.", sz=30, clr=INK)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.1, d - 5.5))


# ─────────────────────────────────────────────────────────────────────────────
# A5V2 — Snow's map: deaths clustering, Soho 1854
# Re-routed from VOX STILL — nopunt pass 2026-07-30
# ─────────────────────────────────────────────────────────────────────────────

# Shared Snow-map geometry (reused across A5V2/V3/V4)
_SNOW_STREETS_H = [
    # (x_start, x_end, y) — horizontal streets
    (-5.5, 5.5, -2.8), (-5.5, 5.5, -1.4), (-5.5, 5.5, 0.0),
    (-5.5, 5.5, 1.4),  (-5.5, 5.5, 2.8),
]
_SNOW_STREETS_V = [
    # y_end=2.7: stays below A5V2 title (≈y=2.9)
    # y_start=-2.0: leaves y<-2.0 free so note/caption text at y≈-2.5 to -3.4 clears vertical streets
    (-4.2, -2.0, 2.7), (-2.2, -2.0, 2.7), (-0.2, -2.0, 2.7),
    (1.8, -2.0, 2.7),  (3.8, -2.0, 2.7),
]
# Death dots (x, y) — clustered around Broad St pump at ~(-0.2, 0.0)
_DEATH_DOTS = [
    (-0.6, 0.4), (-0.3, 0.6), (-0.1, 0.3), (0.1, 0.5), (-0.4, 0.1),
    (0.0, 0.1),  (-0.2, -0.2),(0.3, 0.2),  (-0.5, -0.1),(0.1, -0.3),
    (-0.3, 0.9), (0.4, 0.7),  (-0.7, 0.7), (-0.2, 1.1), (0.6, 0.4),
    (-0.6, -0.4),(0.2, -0.5), (-0.4, -0.6),(0.4, -0.3), (-0.1, -0.7),
    (-0.8, 0.2), (0.5, -0.1), (-0.3, 1.4), (0.2, 1.3),  (-0.5, 1.2),
    (0.7, 0.1),  (-0.7, -0.7),(0.3, -0.8), (-0.1, 1.6), (0.5, 1.0),
    # outliers (few)
    (1.2, 0.8), (-1.5, 0.2), (0.8, -1.0), (-1.0, 1.0),
]
_PUMP_POS = (-0.2, 0.0)   # Broad Street pump
_OTHER_PUMPS = [(-3.5, 0.7), (-1.8, -1.5), (2.5, 0.5), (3.2, -1.0), (1.0, 2.0)]


def _snow_street_grid():
    grp = VGroup()
    for x0, x1, y in _SNOW_STREETS_H:
        grp.add(Line([x0, y, 0], [x1, y, 0], color=GRAY, stroke_width=1.5))
    for x, y0, y1 in _SNOW_STREETS_V:
        grp.add(Line([x, y0, 0], [x, y1, 0], color=GRAY, stroke_width=1.5))
    return grp


class A5V2_SnowCluster(Scene):
    def construct(self):
        d = dur("A5V2")

        title = serif("1854, London — a cholera outbreak", sz=36, clr=INK).to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)

        grid = _snow_street_grid()
        self.play(Create(grid), run_time=0.6)

        # Death dots appearing one by one
        dots = VGroup()
        for x, y in _DEATH_DOTS:
            d_ = Dot([x, y, 0], color=ACCENT, radius=0.10, fill_opacity=0.85)
            dots.add(d_)

        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.04), run_time=1.8)

        caption = serif("Every death mapped to its address.", sz=30, clr=INK).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.3)
        self.wait(max(0.1, d - 4.0))


# ─────────────────────────────────────────────────────────────────────────────
# A5V3 — Snow's map: close-up on Broad Street pump cluster
# Re-routed from VOX STILL — nopunt pass 2026-07-30
# Rewritten as plain Scene (MovingCameraScene not discovered by pipeline regex)
# ─────────────────────────────────────────────────────────────────────────────
class A5V3_SnowPump(Scene):
    def construct(self):
        d = dur("A5V3")

        # "Zoom in" by scaling 2.2× then shifting pump to screen center.
        zoom = 2.2
        cx, cy = _PUMP_POS

        # Custom grid: short horizontal lines (x=±2.5 orig → ±4.6 screen, clears frame edge)
        # and vertical lines clipped to y_end=1.5 (→ screen y≈2.90, below ±3.4 safe top).
        # Pump-street vertical (x≈cx=-0.2) omitted so it doesn't cross caption.
        # Shift -0.40 y: brings top death dot (y_orig=1.6) to screen y=3.12 (within ±3.4).
        y_shift = -0.40
        grid = VGroup()
        for _, _, y in _SNOW_STREETS_H:
            grid.add(Line([-2.5, y, 0], [2.5, y, 0], color=GRAY, stroke_width=1.5))
        for x, y0, y1 in _SNOW_STREETS_V:
            if abs(x - cx) > 0.05:
                grid.add(Line([x, y0, 0], [x, min(y1, 1.5), 0], color=GRAY, stroke_width=1.5))

        raw_dots = VGroup(*[Dot([x, y, 0], color=ACCENT, radius=0.10, fill_opacity=0.85)
                            for x, y in _DEATH_DOTS])
        map_grp = VGroup(grid, raw_dots)
        map_grp.scale(zoom).shift([-cx * zoom, y_shift, 0])

        pump_circle = Circle(radius=0.62, color=ACCENT, stroke_width=3, fill_opacity=0).move_to(ORIGIN)
        pump_dot = Dot(ORIGIN, color=ACCENT, radius=0.26)
        # No text label here — cluster is too dense; caption names the pump below

        self.play(Create(grid), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d) for d in raw_dots], lag_ratio=0.04), run_time=0.8)
        self.play(Create(pump_circle), FadeIn(pump_dot), run_time=0.4)

        # After y_shift=-0.40: outlier dot (0.8,-1.0) → screen y=-2.60, arc bottom y=-2.82.
        # Grid line (y_orig=-1.4) after zoom+shift lands at y≈-3.48 (off safe area, invisible).
        # y=-2.95 clears both: above dot arc bottom (-2.82, gap=0.13) and within ±3.4 safe area.
        caption = serif("The center of the cluster — a single water pump.", sz=24, clr=INK)
        caption.move_to([0, -2.95, 0])
        self.play(FadeIn(caption), run_time=0.3)
        self.wait(max(0.1, d - 3.2))


# ─────────────────────────────────────────────────────────────────────────────
# A5V4 — Snow's map: all pumps — the comparison that makes it evidence
# Re-routed from VOX STILL — nopunt pass 2026-07-30
# Rewritten as plain Scene (start at full map scale, no camera pull-back)
# ─────────────────────────────────────────────────────────────────────────────
class A5V4_SnowAllPumps(Scene):
    def construct(self):
        d = dur("A5V4")

        grid = _snow_street_grid()
        dots = VGroup(*[Dot([x, y, 0], color=ACCENT, radius=0.10, fill_opacity=0.85)
                        for x, y in _DEATH_DOTS])

        pump_circle = Circle(radius=0.28, color=ACCENT, stroke_width=3,
                             fill_opacity=0).move_to([*_PUMP_POS, 0])
        # No pump text label — death-dot cluster makes any label overlap; circle color identifies it

        self.play(Create(grid), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.04), run_time=0.8)
        self.play(Create(pump_circle), run_time=0.4)

        # Reveal all other pumps
        other_pump_grps = VGroup()
        for opx, opy in _OTHER_PUMPS:
            oc = Circle(radius=0.18, color=GRAY, stroke_width=2, fill_opacity=0).move_to([opx, opy, 0])
            other_pump_grps.add(oc)

        self.play(LaggedStart(*[Create(c) for c in other_pump_grps], lag_ratio=0.2), run_time=0.8)

        # caption at bottom, note stacked above with buff=0.25 to clear the y=-2.8 street
        caption = serif("He showed every pump — that's what made it evidence.", sz=28, clr=INK).to_edge(DOWN, buff=0.65)
        note = serif("No deaths cluster around the others.", sz=28, clr=MUTE).next_to(caption, UP, buff=0.25)
        self.play(FadeIn(note), run_time=0.3)
        self.play(FadeIn(caption), run_time=0.3)
        self.wait(max(0.1, d - 3.5))


# ─────────────────────────────────────────────────────────────────────────────
# A6M — Quantile dotplot: four of twenty vs 20%
# ─────────────────────────────────────────────────────────────────────────────
class A6M_QuantileDotplot(Scene):
    def construct(self):
        d = dur("A6M")

        title = serif("Four of twenty beats 20%, every time", sz=36, clr=INK).to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)

        # Risk framing
        risk_lbl = caps("1-in-5 chance of failure", sz=22, clr=MUTE).move_to([0, 2.4, 0])
        self.play(FadeIn(risk_lbl), run_time=0.3)

        # ── LEFT: bare percentage ──────────────────────────
        left_box = panel(3.6, 4.2, fill=WHITE, stroke=GRAY, sw=1.2).move_to([-3.5, 0.0, 0])
        pct_lbl  = caps("as a percentage", sz=16, clr=MUTE).move_to([-3.5, 1.85, 0])
        big_pct  = serif("20%", sz=100, clr=INK, weight=BOLD).move_to([-3.5, -0.1, 0])
        pct_note = caps("arithmetic\nunder pressure", sz=16, clr=INK).move_to([-3.5, -1.9, 0])

        self.play(FadeIn(left_box), FadeIn(pct_lbl), run_time=0.3)
        self.play(Write(big_pct), run_time=0.6)

        # ── RIGHT: quantile dotplot ────────────────────────
        right_box = panel(3.6, 4.2, fill=WHITE, stroke=TEAL, sw=1.5).move_to([3.5, 0.0, 0])
        dot_lbl   = caps("as a dotplot (4 of 20)", sz=16, clr=MUTE).move_to([3.5, 1.85, 0])

        cols, rows = 5, 4
        dot_r = 0.18
        gap   = 0.52
        start_x = 3.5 - (cols - 1) * gap / 2
        start_y = 0.8

        dots = []
        for i in range(rows * cols):
            row = i // cols
            col = i % cols
            x = start_x + col * gap
            y = start_y - row * gap
            filled = i < 4
            clr = ACCENT if filled else GRAY
            op  = 0.85 if filled else 0.35
            dots.append(Dot([x, y, 0], radius=dot_r, color=clr, fill_opacity=op))

        self.play(FadeIn(right_box), FadeIn(dot_lbl), run_time=0.3)

        # Dots appear: 4 terracotta then 16 gray
        for i, dot in enumerate(dots):
            self.play(FadeIn(dot), run_time=0.05 if i >= 4 else 0.15)

        counter = caps("4 of 20", sz=22, clr=INK, weight=BOLD).move_to([3.5, -1.9, 0])
        self.play(FadeIn(counter), FadeIn(pct_note), run_time=0.3)

        # Comparison label
        vs = serif("same risk — different landing", sz=28, clr=INK).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(vs), run_time=0.3)
        self.wait(max(0.1, d - 6.0))


# ─────────────────────────────────────────────────────────────────────────────
# A6R2 — Equal visual weight: the error bar that grows into the finding
# Replaces the static FormACard tell-not-show beat.
# ─────────────────────────────────────────────────────────────────────────────
class A6R2_EqualWeight(Scene):
    def construct(self):
        d = dur("A6R2")

        # Header — keeps the FormACard title line as the frame anchor
        title = serif(
            "The uncertainty is part of the finding, not a quibble.",
            sz=30, clr=INK
        ).to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)

        # Number line (40–95%)
        ax_lo, ax_hi = 40, 95
        ax_x0, ax_x1 = -5.0, 5.0
        ax_y = -0.5
        point_est, ci_lo, ci_hi = 68, 56, 80  # concrete round numbers

        def px(v):
            return ax_x0 + (v - ax_lo) / (ax_hi - ax_lo) * (ax_x1 - ax_x0)

        x_axis = Line([ax_x0, ax_y, 0], [ax_x1, ax_y, 0], color=INK, stroke_width=2)
        ticks = VGroup()
        for t in [50, 60, 70, 80, 90]:
            xp = px(t)
            ticks.add(Line([xp, ax_y - 0.1, 0], [xp, ax_y + 0.1, 0],
                           color=INK, stroke_width=1.5))
            ticks.add(caps(f"{t}%", sz=18, clr=MUTE).move_to([xp, ax_y - 0.42, 0]))
        self.play(Create(x_axis), FadeIn(ticks), run_time=0.5)

        # ── PHASE 1: dishonest — big number, tiny whisker ──────────────────────
        phase_lbl = caps("small error bar on a big number", sz=18, clr=MUTE)
        phase_lbl.move_to([0, 2.25, 0])
        self.play(FadeIn(phase_lbl), run_time=0.3)

        pt_x = px(point_est)
        pt_label = serif("68%", sz=88, clr=INK, weight=BOLD).move_to([pt_x, 1.4, 0])
        pt_dot   = Dot([pt_x, ax_y, 0], color=INK, radius=0.16)
        self.play(Write(pt_label), FadeIn(pt_dot), run_time=0.7)

        _lo_x, _hi_x = px(ci_lo), px(ci_hi)
        band_w = _hi_x - _lo_x
        wline  = Line([_lo_x, ax_y, 0], [_hi_x, ax_y, 0], color=INK, stroke_width=3)
        wcap_l = Line([_lo_x, ax_y - 0.12, 0], [_lo_x, ax_y + 0.12, 0],
                      color=INK, stroke_width=3)
        wcap_r = Line([_hi_x, ax_y - 0.12, 0], [_hi_x, ax_y + 0.12, 0],
                      color=INK, stroke_width=3)
        whisker_grp = VGroup(wline, wcap_l, wcap_r)
        ci_note = caps("95% CI  ·  56% – 80%", sz=18, clr=MUTE)
        ci_note.move_to([pt_x, ax_y - 0.90, 0])

        self.play(FadeIn(whisker_grp), FadeIn(ci_note), run_time=0.4)
        self.wait(5.0)   # hold the dishonest framing

        # ── PHASE 2: honest — band grows to equal visual weight ────────────────
        phase2_lbl = caps("equal visual weight — the uncertainty IS the finding",
                          sz=18, clr=INK)
        phase2_lbl.move_to([0, 2.25, 0])

        band_target_h = 1.35
        # Start as a thin band (same footprint as the whisker line); Transform grows it.
        band_thin = Rectangle(
            width=band_w, height=0.04,
            fill_color=ACCENT, fill_opacity=0.32, stroke_width=0
        ).move_to([(_lo_x + _hi_x) / 2, ax_y + 0.02, 0])

        band_thick = Rectangle(
            width=band_w, height=band_target_h,
            fill_color=ACCENT, fill_opacity=0.32, stroke_width=0
        ).move_to([(_lo_x + _hi_x) / 2, ax_y + band_target_h / 2, 0])

        self.add(band_thin)
        self.play(FadeOut(phase_lbl), FadeIn(phase2_lbl), run_time=0.4)
        # The money move: whisker vanishes, interval grows into a band
        self.play(
            FadeOut(whisker_grp),
            Transform(band_thin, band_thick),
            run_time=1.8, rate_func=rate_functions.ease_in_out_cubic
        )

        # Bound labels at band vertical midpoint
        band_mid_y = ax_y + band_target_h / 2
        lo_lbl = caps("56%", sz=20, clr=INK).move_to([_lo_x - 0.50, band_mid_y, 0])
        hi_lbl = caps("80%", sz=20, clr=INK).move_to([_hi_x + 0.50, band_mid_y, 0])
        self.play(FadeIn(lo_lbl), FadeIn(hi_lbl), run_time=0.3)

        verdict = serif("the uncertainty IS the finding", sz=34, clr=INK)
        verdict.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(verdict), run_time=0.4)

        self.wait(max(0.1, d - 10.7))


# ─────────────────────────────────────────────────────────────────────────────
# A6V1 — Nigeria kidnapping map: the relabeling reveal
# Re-routed from VOX STILL — nopunt pass 2026-07-30
# ─────────────────────────────────────────────────────────────────────────────
class A6V1_NewsVsEvents(Scene):
    def construct(self):
        d = dur("A6V1")

        title = serif("A map of news stories, titled as a map of crime", sz=34, clr=INK).to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)

        # Base map rectangles (shared across both phases — only label swaps)
        regions = [
            (-1.5,  1.8, 2.0, 1.0, 0.15),
            ( 0.8,  1.8, 1.8, 1.0, 0.10),
            (-3.0,  0.8, 1.8, 1.2, 0.20),
            (-1.0,  0.8, 2.2, 1.2, 0.30),
            ( 1.2,  0.8, 2.0, 1.2, 0.15),
            (-3.5, -0.5, 1.5, 1.4, 0.10),
            (-1.8, -0.5, 2.0, 1.4, 0.45),
            ( 0.3, -0.5, 1.8, 1.4, 0.70),
            ( 2.0, -0.5, 1.8, 1.4, 0.25),
            (-2.0, -2.0, 2.0, 1.6, 0.20),
            ( 0.0, -2.0, 2.2, 1.6, 0.55),
            ( 2.2, -2.0, 1.6, 1.6, 0.15),
        ]
        base_map = VGroup()
        for x, y, w, h, intensity in regions:
            base_map.add(Rectangle(
                width=w, height=h,
                fill_color=INK, fill_opacity=intensity * 0.75,
                stroke_color=CREAM, stroke_width=0.8
            ).move_to([x, y, 0]))

        lbl1_box = panel(5.5, 0.6, fill=CREAM, stroke=INK, sw=2).move_to([0, -3.1, 0])
        lbl1_box._qc_intentional = True  # box sides cross label centerline by design
        lbl1_txt = caps("KIDNAPPING EVENTS  2012–2015", sz=18, clr=INK).move_to([0, -3.1, 0])
        lbl2_box = panel(5.5, 0.6, fill=CREAM, stroke=ACCENT, sw=2).move_to([0, -3.1, 0])
        lbl2_box._qc_intentional = True
        lbl2_txt = caps("NEWS MENTIONS OF KIDNAPPINGS  2012–2015", sz=18, clr=INK).move_to([0, -3.1, 0])

        # Phase 2 unique marker: newspaper-column icon (three thin rectangles → looks like columns)
        news_icon = VGroup(
            Rectangle(width=0.12, height=0.48, fill_color=ACCENT, fill_opacity=0.8, stroke_width=0).move_to([-5.8, -3.1, 0]),
            Rectangle(width=0.12, height=0.48, fill_color=ACCENT, fill_opacity=0.8, stroke_width=0).move_to([-5.55, -3.1, 0]),
            Rectangle(width=0.12, height=0.48, fill_color=ACCENT, fill_opacity=0.8, stroke_width=0).move_to([-5.3, -3.1, 0]),
        )

        self.play(FadeIn(base_map), FadeIn(lbl1_box), FadeIn(lbl1_txt), run_time=0.8)
        self.wait(0.9)

        # Relabeling reveal — swap label, add newspaper icon, hold so viewer reads it
        self.play(FadeOut(lbl1_box), FadeOut(lbl1_txt), run_time=0.3)
        self.play(FadeIn(lbl2_box), FadeIn(lbl2_txt), FadeIn(news_icon), run_time=0.4)
        self.wait(2.5)

        # Editorial verdict — show after label clears to avoid text-on-text overlap
        self.play(FadeOut(lbl2_box), FadeOut(lbl2_txt), FadeOut(news_icon), run_time=0.3)
        note = serif("same numbers — wrong source", sz=30, clr=INK).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(max(0.1, d - 7.0))


# ─────────────────────────────────────────────────────────────────────────────
# A7V — Du Bois 1900: deliberate choices, politics visible
# Re-routed from VOX STILL — nopunt pass 2026-07-30
# ─────────────────────────────────────────────────────────────────────────────
class A7V_DuBoisStyle(Scene):
    def construct(self):
        d = dur("A7V")

        # Dark background via camera — avoids a full-frame rectangle bleeding past title-safe
        self.camera.background_color = "#1A1208"

        title = Text("1900 Paris Exposition", font="EB Garamond",
                     font_size=36, color="#F5E9C8").to_edge(UP, buff=0.65)
        title2 = Text("W. E. B. Du Bois — Data Visualizations", font="EB Garamond",
                      font_size=28, color=ACCENT).next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(title2), run_time=0.5)

        # Spiral bar chart (stylized Du Bois inspired)
        # Concentric arcs with bold color fills, animating outward
        center = [0.0, -0.4, 0]
        colors = [ACCENT, "#C8102E", "#F5E9C8", ACCENT, "#C8102E"]
        segments = [
            (0.6, 0.9,  200, "#C8102E"),   # innermost
            (0.9, 1.25, 250, ACCENT),
            (1.25, 1.6, 300, "#F5E9C8"),
            (1.6, 1.95, 220, "#C8102E"),
            (1.95, 2.3, 280, ACCENT),
        ]

        bars = VGroup()
        for i, (r_in, r_out, angle_deg, clr) in enumerate(segments):
            annular = AnnularSector(
                inner_radius=r_in, outer_radius=r_out,
                start_angle=math.pi / 2, angle=-math.radians(angle_deg),
                fill_color=clr, fill_opacity=0.90, stroke_width=1.5,
                stroke_color="#1A1208"
            )
            annular.move_arc_center_to(center)
            # Annular sector shapes may trigger arc-curve geometry checks; intentional.
            annular._qc_intentional = True
            bars.add(annular)

        # Label routing rule: no ring label may sit on a ring.
        #   i <= 2 (1870–1890): outward position lands on a subsequent ring →
        #     route INWARD to the dark center hole (r=0.42, inside r_in=0.60).
        #     Cream (#F5E9C8) on dark ground #1A1208 ≈ 16:1 contrast. ✓
        #     Label placement angles are spread to -2°/-30°/-80° (not the arc
        #     midpoints -10°/-35°/-60°) so the labels fan across the center hole
        #     with 17–19 px clear gaps instead of stacking.
        #     Leader goes from the label (at r=0.50) to the ring inner edge
        #     at the ring's own midpoint angle.
        #   i >= 3 (1900–TOTAL): outward position already clears all ring extents →
        #     keep OUTSIDE at r_out+0.55 in dark field. ✓
        #   Each label carries a short leader to its ring edge.
        bar_labels_txt = ["1870", "1880", "1890", "1900", "TOTAL"]
        # Spread label-placement angles so inner labels don't cluster vertically
        inner_a_label_deg = [-2, -30, -80]  # vs ring midpoints -10, -35, -60
        bar_labels = VGroup()
        leader_lines = VGroup()
        for i, (lbl_txt, (r_in, r_out, angle_deg, clr)) in enumerate(zip(bar_labels_txt, segments)):
            a_mid = math.pi / 2 - math.radians(angle_deg / 2)  # ring midpoint angle
            if i <= 2:
                # Inward: fan label to spread angle, leader endpoints at ring midpoint angle
                a_lbl = math.radians(inner_a_label_deg[i])
                r_lbl = 0.42  # max extent 0.42+0.155=0.575 < r_in_min=0.60 ✓
                x_lbl = center[0] + r_lbl * math.cos(a_lbl)
                y_lbl = center[1] + r_lbl * math.sin(a_lbl)
                # Leader start: just past label edge toward the ring
                x0 = center[0] + 0.50 * math.cos(a_lbl)
                y0 = center[1] + 0.50 * math.sin(a_lbl)
                # Leader end: ring inner edge at ring's own midpoint angle
                x1 = center[0] + r_in * math.cos(a_mid)
                y1 = center[1] + r_in * math.sin(a_mid)
            else:
                # Outward: label sits in the dark field beyond all ring extents
                r_lbl = r_out + 0.55
                x_lbl = center[0] + r_lbl * math.cos(a_mid)
                y_lbl = center[1] + r_lbl * math.sin(a_mid)
                # Leader: ring outer edge → label approach
                x0 = center[0] + r_out          * math.cos(a_mid)
                y0 = center[1] + r_out          * math.sin(a_mid)
                x1 = center[0] + (r_out + 0.35) * math.cos(a_mid)
                y1 = center[1] + (r_out + 0.35) * math.sin(a_mid)
            lbl = Text(lbl_txt, font="EB Garamond", font_size=16, color="#F5E9C8", weight=BOLD)
            lbl.move_to([x_lbl, y_lbl, 0])
            bar_labels.add(lbl)
            leader_lines.add(Line([x0, y0, 0], [x1, y1, 0],
                                  color="#F5E9C8", stroke_width=1.5))

        self.play(LaggedStart(*[DrawBorderThenFill(b) for b in bars], lag_ratio=0.3), run_time=1.8)
        self.play(LaggedStart(
            *[FadeIn(VGroup(leader_lines[i], bar_labels[i])) for i in range(len(bar_labels))],
            lag_ratio=0.2
        ), run_time=0.6)

        # Quote
        quote = Text("Deliberate choices.\nPolitics visible.\nHonest for it.",
                     font="EB Garamond", font_size=30, color="#F5E9C8",
                     line_spacing=0.8).move_to([3.8, -0.4, 0])
        self.play(FadeIn(quote), run_time=0.5)

        sub = Text("Not neutral. Not pretending to be.", font="EB Garamond",
                   font_size=22, color=ACCENT).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(sub), run_time=0.3)
        self.wait(max(0.1, d - 5.5))
