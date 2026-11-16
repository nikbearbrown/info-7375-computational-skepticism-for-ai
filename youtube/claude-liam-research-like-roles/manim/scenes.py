"""Manim scenes — claude-liam-research-like-roles
Deep-explainer: Bear's feedback on Zening's Computational Skepticism final project.
Palette: claude stage — cream #F2F0E9, ink #3D3929, terracotta #D97757, mute #7A7265.
All schematic numbers labeled "illustrative" — no real statistics claimed.
14pt legibility floor: all on-screen text >= 18pt rendered size.
"""
from manim import *

# ── palette ──────────────────────────────────────────────────────────────────
CREAM    = "#F2F0E9"
INK      = "#3D3929"
TERRA    = "#D97757"
MUTE     = "#7A7265"
GOOD     = "#3D7A4A"

config.background_color = CREAM
config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width  = 1920


def ink(text, size=36, **kw):
    return Text(text, color=INK, font_size=size, font="EB Garamond", **kw)

def terra(text, size=36, **kw):
    return Text(text, color=TERRA, font_size=size, font="EB Garamond", **kw)

def mute_t(text, size=28, **kw):
    return Text(text, color=MUTE, font_size=size, font="EB Garamond", **kw)

def good_t(text, size=32, **kw):
    return Text(text, color=GOOD, font_size=size, font="EB Garamond", **kw)


# ── B06 — Circularity Loop ────────────────────────────────────────────────────
class B06_CircularityLoop(Scene):
    """~14s  Define → Sample → Redefine → (loop back). Terracotta loop arrow."""

    def construct(self):
        # Three nodes in a row
        nodes_text = ["Define\nConstruct", "Sample\nPostings", "Redefine\nConstruct"]
        colors = [INK, INK, INK]
        nodes = []
        x_positions = [-4.0, 0.0, 4.0]

        for label, x in zip(nodes_text, x_positions):
            box = RoundedRectangle(
                corner_radius=0.15, width=2.6, height=1.4,
                color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
            ).move_to([x, 0.8, 0])
            txt = Text(label, color=INK, font_size=32, font="EB Garamond") \
                      .move_to(box.get_center())
            nodes.append(VGroup(box, txt))

        # Step 1 — node 1 appears
        self.play(FadeIn(nodes[0]), run_time=0.5)
        self.wait(0.8)

        # Arrow node1 → node2
        arr12 = Arrow(
            nodes[0].get_right(), nodes[1].get_left(),
            color=INK, buff=0.1, stroke_width=3, tip_length=0.2
        )
        self.play(GrowArrow(arr12), run_time=0.4)
        self.play(FadeIn(nodes[1]), run_time=0.4)
        self.wait(0.6)

        # Arrow node2 → node3
        arr23 = Arrow(
            nodes[1].get_right(), nodes[2].get_left(),
            color=INK, buff=0.1, stroke_width=3, tip_length=0.2
        )
        self.play(GrowArrow(arr23), run_time=0.4)
        self.play(FadeIn(nodes[2]), run_time=0.4)
        self.wait(0.5)

        # Terracotta loop arrow: curves from Redefine back down/left to Define
        loop = CurvedArrow(
            nodes[2].get_bottom() + DOWN * 0.1,
            nodes[0].get_bottom() + DOWN * 0.1,
            color=TERRA, stroke_width=4, angle=-TAU / 5, tip_length=0.22
        )
        self.play(Create(loop), run_time=1.0)
        self.wait(0.4)

        # Label on loop
        loop_lbl = terra("never can fail", size=28) \
            .move_to([0.0, -1.4, 0])
        self.play(Write(loop_lbl), run_time=0.5)
        self.wait(1.2)


# ── B07 — Coding Scheme ───────────────────────────────────────────────────────
class B07_CodingScheme(Scene):
    """~15s  Five criteria StateCards stacking. Finalize-before-sampling underline."""

    CRITERIA = [
        "1  Ambiguous deliverable",
        "2  Small / inferrable team size",
        "3  Single flat reporting line",
        "4  Evaluation emphasis over execution",
        "5  AI-assisted implementation explicit",
    ]

    def construct(self):
        header = ink("Checkable Coding Scheme", size=44) \
            .move_to([0, 3.0, 0])
        underline = Line(
            header.get_left() + LEFT * 0.1,
            header.get_right() + RIGHT * 0.1,
            color=TERRA, stroke_width=2
        ).next_to(header, DOWN, buff=0.08)
        self.play(Write(header), Create(underline), run_time=0.6)

        # Criteria cards
        y_start = 1.8
        gap = 0.88
        cards = []
        for i, crit in enumerate(self.CRITERIA):
            card_bg = RoundedRectangle(
                corner_radius=0.1, width=11.0, height=0.68,
                color=MUTE, fill_color=CREAM, fill_opacity=1, stroke_width=1
            ).move_to([0, y_start - i * gap, 0])
            card_txt = ink(crit, size=30).move_to(card_bg.get_center())
            card_txt.align_to(card_bg, LEFT).shift(RIGHT * 0.3)
            cards.append(VGroup(card_bg, card_txt))

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.15), run_time=0.35)
            self.wait(0.15)

        # Bottom instruction
        instruction = terra("Finalize BEFORE sampling", size=34) \
            .move_to([0, y_start - len(self.CRITERIA) * gap - 0.3, 0])
        self.play(Write(instruction), run_time=0.5)
        self.wait(1.2)


# ── B12 — Posting Splits ─────────────────────────────────────────────────────
class B12_PostingSplit(Scene):
    """~14s  One posting card at top; fork to Lab vs Factory. Same words, divergent structure."""

    def construct(self):
        # Top posting card
        post_bg = RoundedRectangle(
            corner_radius=0.15, width=10.0, height=1.2,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        ).move_to([0, 2.8, 0])
        post_txt = mute_t(
            '"research-forward… ownership… innovative team"', size=30
        ).move_to(post_bg.get_center())
        posting = VGroup(post_bg, post_txt)
        self.play(FadeIn(posting), run_time=0.5)
        self.wait(0.6)

        # Fork lines
        fork_top = Line([0, 2.2, 0], [0, 1.5, 0], color=INK, stroke_width=2)
        fork_left  = Line([0, 1.5, 0], [-3.6, 0.6, 0], color=GOOD,  stroke_width=2.5)
        fork_right = Line([0, 1.5, 0], [ 3.6, 0.6, 0], color=TERRA, stroke_width=2.5)
        self.play(Create(fork_top), run_time=0.25)
        self.play(Create(fork_left), Create(fork_right), run_time=0.5)

        # Left card — Lab
        lab_bg = RoundedRectangle(
            corner_radius=0.15, width=5.8, height=2.8,
            color=GOOD, fill_color=CREAM, fill_opacity=1, stroke_width=2.5
        ).move_to([-3.6, -0.9, 0])
        lab_hdr = good_t("R&D Lab", size=34).move_to([-3.6, 0.2, 0])
        lab_l1 = mute_t("· exploratory, open-ended work", size=25).move_to([-3.6, -0.5, 0])
        lab_l2 = mute_t("· flat team, advisor–student dynamic", size=25).move_to([-3.6, -1.0, 0])
        lab_l3 = mute_t("· outcome: prove / disprove a claim", size=25).move_to([-3.6, -1.5, 0])
        self.play(FadeIn(VGroup(lab_bg, lab_hdr, lab_l1, lab_l2, lab_l3)), run_time=0.5)

        # Right card — Factory
        fac_bg = RoundedRectangle(
            corner_radius=0.15, width=5.8, height=2.8,
            color=TERRA, fill_color=CREAM, fill_opacity=1, stroke_width=2.5
        ).move_to([3.6, -0.9, 0])
        fac_hdr = terra("Feature Factory", size=34).move_to([3.6, 0.2, 0])
        fac_l1 = mute_t("· fully-specified tickets, JIRA queue", size=25).move_to([3.6, -0.5, 0])
        fac_l2 = mute_t("· PM-driven, multiple approval layers", size=25).move_to([3.6, -1.0, 0])
        fac_l3 = mute_t("· outcome: ship the spec", size=25).move_to([3.6, -1.5, 0])
        self.play(FadeIn(VGroup(fac_bg, fac_hdr, fac_l1, fac_l2, fac_l3)), run_time=0.5)
        self.wait(0.4)

        # Bottom label
        lbl = terra("same words, different reality", size=32).move_to([0, -2.7, 0])
        self.play(Write(lbl), run_time=0.4)
        self.wait(1.2)


# ── B16 — Snapshot vs Trend ──────────────────────────────────────────────────
class B16_SnapshotVsTrend(Scene):
    """~14s  Left: single dot 'now'. Right: two dots connected by terracotta trend line."""

    def construct(self):
        # Two panels
        divider = DashedLine(
            [0, 3.2, 0], [0, -3.2, 0],
            color=MUTE, stroke_width=1.5, dash_length=0.15
        )
        self.play(Create(divider), run_time=0.3)

        # --- Left panel: snapshot ---
        ax_l = Axes(
            x_range=[2019, 2025, 1], y_range=[0, 1, 1],
            x_length=5.0, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 2, "include_ticks": False},
            tips=False,
        ).move_to([-3.0, 0.0, 0])
        lbl_snap = mute_t("Snapshot", size=32).move_to([-3.0, 2.3, 0])
        self.play(Create(ax_l), FadeIn(lbl_snap), run_time=0.5)

        # Single dot at "2024"
        dot_now = Dot(ax_l.c2p(2024, 0.65), color=INK, radius=0.13)
        dot_lbl_now = mute_t("now", size=24).next_to(dot_now, UP, buff=0.12)
        self.play(FadeIn(dot_now), Write(dot_lbl_now), run_time=0.5)
        self.wait(0.5)

        # --- Right panel: trend ---
        ax_r = Axes(
            x_range=[2019, 2025, 1], y_range=[0, 1, 1],
            x_length=5.0, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 2, "include_ticks": False},
            tips=False,
        ).move_to([3.0, 0.0, 0])
        lbl_trend = mute_t("Trend", size=32).move_to([3.0, 2.3, 0])
        self.play(Create(ax_r), FadeIn(lbl_trend), run_time=0.5)

        dot_before = Dot(ax_r.c2p(2020, 0.28), color=INK, radius=0.13)
        dot_after  = Dot(ax_r.c2p(2024, 0.65), color=INK, radius=0.13)
        self.play(FadeIn(dot_before), run_time=0.3)
        self.play(FadeIn(dot_after),  run_time=0.3)

        # Terracotta trend line
        trend_line = Line(ax_r.c2p(2020, 0.28), ax_r.c2p(2024, 0.65),
                          color=TERRA, stroke_width=4)
        trend_lbl = terra("trend", size=28).move_to(ax_r.c2p(2022.5, 0.55))
        self.play(Create(trend_line), run_time=0.6)
        self.play(Write(trend_lbl), run_time=0.3)
        self.wait(0.4)

        # Bottom label
        bottom = terra("one point ≠ trend", size=34).move_to([0, -2.5, 0])
        self.play(Write(bottom), run_time=0.4)
        self.wait(1.2)


# ── B21 — Fake Trend Chart ───────────────────────────────────────────────────
class B21_FakeTrendChart(Scene):
    """~14s  Bar chart with wide terracotta CI bands on early bars. Label: illustrative."""

    # Schematic data — labeled illustrative
    YEARS   = [2019, 2020, 2021, 2022, 2023, 2024]
    HEIGHTS = [0.18, 0.22, 0.30, 0.48, 0.62, 0.75]
    CI_HALF = [0.32, 0.28, 0.20, 0.10, 0.06, 0.04]  # decreasing CIs

    def construct(self):
        # Illustrative label (top right)
        illu_lbl = mute_t("illustrative", size=22).to_corner(UR, buff=0.35)
        self.add(illu_lbl)

        ax = Axes(
            x_range=[2018.5, 2024.5, 1], y_range=[0, 1.1, 0.5],
            x_length=11.0, y_length=5.0,
            axis_config={"color": INK, "stroke_width": 2},
            y_axis_config={"include_ticks": True},
            tips=False,
        ).move_to([0, -0.2, 0])
        x_labels = VGroup(*[
            mute_t(str(y), size=24).move_to(ax.c2p(y, -0.12))
            for y in self.YEARS
        ])
        y_label = mute_t("% research-like", size=24).rotate(PI / 2) \
            .next_to(ax.get_y_axis(), LEFT, buff=0.25)
        title = ink("Research-Like Posting Rate Over Time", size=36).move_to([0, 3.3, 0])
        self.play(Create(ax), FadeIn(x_labels), FadeIn(y_label),
                  Write(title), run_time=0.7)

        bars = []
        ci_rects = []
        for y, h, ci in zip(self.YEARS, self.HEIGHTS, self.CI_HALF):
            # Bar
            bar = Rectangle(
                width=0.55, height=max(0.02, h * ax.y_length / 1.1),
                color=INK, fill_color=INK, fill_opacity=0.55, stroke_width=0
            )
            bot = ax.c2p(y, 0)
            bar.align_to([bot[0] - 0.275, bot[1], 0], DL)
            # CI rect — terracotta for early (large CI), ink for later
            ci_h = ci * ax.y_length / 1.1
            center_y = ax.c2p(y, h)[1]
            ci_color = TERRA if ci > 0.12 else MUTE
            ci_rect = Rectangle(
                width=0.18, height=ci_h * 2,
                color=ci_color, fill_color=ci_color,
                fill_opacity=0.55, stroke_width=0
            ).move_to([ax.c2p(y, 0)[0], center_y, 0])
            bars.append(bar)
            ci_rects.append(ci_rect)

        # Animate bars one by one
        for bar, ci_rect in zip(bars, ci_rects):
            self.play(GrowFromEdge(bar, DOWN), FadeIn(ci_rect), run_time=0.25)

        # Trend line
        pts = [ax.c2p(y, h) for y, h in zip(self.YEARS, self.HEIGHTS)]
        trend = VMobject(color=TERRA, stroke_width=3)
        trend.set_points_as_corners(pts)
        self.play(Create(trend), run_time=0.5)
        self.wait(0.3)

        # Callout
        callout = terra("small early N — CI spans the chart", size=28) \
            .move_to([-1.5, -3.0, 0])
        arr = Arrow([ax.c2p(2019.5, 0.18 + 0.32)[0], ax.c2p(2019.5, 0.18 + 0.32)[1], 0],
                    callout.get_top(), color=TERRA, buff=0.05,
                    stroke_width=2, tip_length=0.15)
        self.play(Write(callout), GrowArrow(arr), run_time=0.5)
        self.wait(1.2)


# ── B22 — Co-Occurrence vs Causation ─────────────────────────────────────────
class B22_CoOccurrence(Scene):
    """~13s  Two parallel lines; label co-occurrence; terracotta X over causal arrow."""

    def construct(self):
        ax = Axes(
            x_range=[2020, 2025, 1], y_range=[0, 1, 0.5],
            x_length=10.0, y_length=5.0,
            axis_config={"color": INK, "stroke_width": 2},
            tips=False,
        ).move_to([0, 0.0, 0])
        x_labels = VGroup(*[
            mute_t(str(y), size=24).move_to(ax.c2p(y, -0.12))
            for y in range(2020, 2026)
        ])
        self.play(Create(ax), FadeIn(x_labels), run_time=0.5)

        # Line 1 — LLM adoption
        llm_pts = [ax.c2p(y, v) for y, v in
                   [(2020, 0.10), (2021, 0.18), (2022, 0.38), (2023, 0.62), (2024, 0.82)]]
        llm_line = VMobject(color=INK, stroke_width=3.5)
        llm_line.set_points_as_corners(llm_pts)
        llm_lbl = ink("LLM adoption", size=28).next_to(
            ax.c2p(2024, 0.82), RIGHT, buff=0.1)
        self.play(Create(llm_line), FadeIn(llm_lbl), run_time=0.7)

        # Line 2 — research-like postings
        rl_pts = [ax.c2p(y, v) for y, v in
                  [(2020, 0.15), (2021, 0.22), (2022, 0.35), (2023, 0.55), (2024, 0.72)]]
        rl_line = VMobject(color=MUTE, stroke_width=3.5)
        rl_line.set_points_as_corners(rl_pts)
        rl_lbl = mute_t("research-like postings", size=28).next_to(
            ax.c2p(2024, 0.72), RIGHT, buff=0.1)
        self.play(Create(rl_line), FadeIn(rl_lbl), run_time=0.7)
        self.wait(0.3)

        # "co-occurrence" label between lines
        co_lbl = ink("co-occurrence", size=34).move_to([0, -0.5, 0])
        self.play(Write(co_lbl), run_time=0.4)
        self.wait(0.3)

        # Dashed causal arrow (INK)
        mid_left  = ax.c2p(2022, 0.38)
        mid_right = ax.c2p(2022, 0.35)
        causal_arr = DashedVMobject(
            Arrow(mid_left, mid_right, buff=0.05, color=INK,
                  stroke_width=2, tip_length=0.15),
            num_dashes=12
        )
        self.play(Create(causal_arr), run_time=0.4)

        # Terracotta X over causal arrow
        x_center = ax.c2p(2022, 0.365)
        x1 = Line(
            [x_center[0] - 0.35, x_center[1] + 0.35, 0],
            [x_center[0] + 0.35, x_center[1] - 0.35, 0],
            color=TERRA, stroke_width=5
        )
        x2 = Line(
            [x_center[0] - 0.35, x_center[1] - 0.35, 0],
            [x_center[0] + 0.35, x_center[1] + 0.35, 0],
            color=TERRA, stroke_width=5
        )
        self.play(Create(x1), Create(x2), run_time=0.4)
        self.wait(1.2)


# ── B23 — Keyword Sensitivity ────────────────────────────────────────────────
class B23_KeywordSensitivity(Scene):
    """~12s  Two-column swap table. Terracotta diff on count change."""

    def construct(self):
        header = ink("Keyword Sensitivity Check", size=42).move_to([0, 3.2, 0])
        h_line = Line(
            [-7.0, 2.7, 0], [7.0, 2.7, 0], color=MUTE, stroke_width=1.5
        )
        self.play(Write(header), Create(h_line), run_time=0.5)

        # Column headers
        col1h = ink("Term", size=30).move_to([-3.5, 2.1, 0])
        col2h = ink("Flagged postings (schematic)", size=30).move_to([2.0, 2.1, 0])
        self.play(Write(col1h), Write(col2h), run_time=0.3)

        # Row 1: experimentation
        r1a = [ink('"experimentation"', size=28).move_to([-3.5, 1.2, 0]),
               ink("N₁",  size=28).move_to([2.0, 1.2, 0])]
        r1b = [terra('"iterative"', size=28).move_to([-3.5, 0.5, 0]),
               terra("N₂  (Δ = –N₁)", size=28).move_to([2.0, 0.5, 0])]
        for el in r1a:
            self.play(Write(el), run_time=0.25)
        self.wait(0.2)
        for el in r1b:
            self.play(Write(el), run_time=0.25)
        self.wait(0.3)

        # Separator line
        sep = Line([-7.0, 0.1, 0], [7.0, 0.1, 0], color=MUTE, stroke_width=1)
        self.play(Create(sep), run_time=0.15)

        # Row 2: research-forward
        r2a = [ink('"research-forward"', size=28).move_to([-3.5, -0.5, 0]),
               ink("N₃", size=28).move_to([2.0, -0.5, 0])]
        r2b = [terra('"data-driven"', size=28).move_to([-3.5, -1.2, 0]),
               terra("N₄  (Δ = –N₃)", size=28).move_to([2.0, -1.2, 0])]
        for el in r2a:
            self.play(Write(el), run_time=0.25)
        self.wait(0.2)
        for el in r2b:
            self.play(Write(el), run_time=0.25)
        self.wait(0.4)

        # Bottom label
        verdict = terra("large Δ = surface vocabulary, not construct", size=30) \
            .move_to([0, -2.4, 0])
        self.play(Write(verdict), run_time=0.4)
        self.wait(1.2)


# ── B24 — Two Open Questions ──────────────────────────────────────────────────
class B24_OpenQuestions(Scene):
    """~13s  Two large StateCards. Q1 then Q2 drop in. Terracotta question marks."""

    def construct(self):
        header = ink("Open Questions", size=46).move_to([0, 3.2, 0])
        h_line = Line(
            [-5.5, 2.72, 0], [5.5, 2.72, 0], color=TERRA, stroke_width=2
        )
        self.play(Write(header), Create(h_line), run_time=0.4)
        self.wait(0.3)

        # Q1 card
        q1_bg = RoundedRectangle(
            corner_radius=0.2, width=14.0, height=2.0,
            color=MUTE, fill_color=CREAM, fill_opacity=1, stroke_width=1.5
        ).move_to([0, 1.2, 0])
        q1_num = terra("Q1", size=40).move_to([-6.3, 1.2, 0])
        q1_txt = ink(
            "What non-posting source can validate\nthat a flagged posting describes a\nresearch-structured job?",
            size=28, line_spacing=1.3
        ).move_to([0.5, 1.2, 0])
        q1_mark = terra("?", size=48).move_to([6.6, 1.2, 0])
        q1 = VGroup(q1_bg, q1_num, q1_txt, q1_mark)
        self.play(FadeIn(q1, shift=DOWN * 0.2), run_time=0.6)
        self.wait(0.7)

        # Q2 card
        q2_bg = RoundedRectangle(
            corner_radius=0.2, width=14.0, height=2.0,
            color=MUTE, fill_color=CREAM, fill_opacity=1, stroke_width=1.5
        ).move_to([0, -1.2, 0])
        q2_num = terra("Q2", size=40).move_to([-6.3, -1.2, 0])
        q2_txt = ink(
            "What is a defensible pre-LLM baseline year—\nand why that year?",
            size=28, line_spacing=1.3
        ).move_to([0.5, -1.2, 0])
        q2_mark = terra("?", size=48).move_to([6.6, -1.2, 0])
        q2 = VGroup(q2_bg, q2_num, q2_txt, q2_mark)
        self.play(FadeIn(q2, shift=DOWN * 0.2), run_time=0.6)
        self.wait(1.4)
