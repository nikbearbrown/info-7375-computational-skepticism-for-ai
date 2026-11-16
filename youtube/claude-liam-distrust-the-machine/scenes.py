"""
scenes.py — Manim scenes for claude-liam-distrust-the-machine
"Knowing Enough to Distrust the Machine" (Theorist.ai, Bear Brown, v1 2026-03-13)

Five scenes (B09, B13, B18, B19, B20). All schematic — no invented magnitudes.
Palette: Claude cream (#FAF9F5 PAGE), warm ink (#3D3929 INK), terracotta (#D97757 SPARK).
Run via: python scenes.py <BID> --output media/<BID>.mp4
"""

from __future__ import annotations
import sys
import math
import subprocess
from manim import *

# ── palette ──────────────────────────────────────────────────────────────────
PAGE    = "#FAF9F5"
INK     = "#3D3929"
SPARK   = "#D97757"
MUTED   = "#7A7265"
BORDER  = "#D0C9BB"
SERIF   = "EB Garamond"
SANS    = "DM Sans"


# ─────────────────────────────────────────────────────────────────────────────
# B09 — The capability bars leave the chart
# Four horizontal bars: arithmetic, retrieval, syntax, dense-pattern.
# Each rises past a "best human" ceiling line, then caps near frame top with
# an upward arrow — schematic signal that it exceeds the chart.
# Schematic only — no invented magnitudes.
# ─────────────────────────────────────────────────────────────────────────────
class B09_OffTheChart(Scene):
    def construct(self):
        self.camera.background_color = PAGE

        labels   = ["Arithmetic", "Fact retrieval", "Syntax", "Pattern recognition"]
        bar_w    = 1.0
        spacing  = 2.0
        ceiling  = 2.5          # "best human" threshold y (schematic)
        base_y   = -2.8

        # Track x positions for each bar (used by arrows below)
        xs = [(i - 1.5) * spacing for i in range(len(labels))]

        # Axes
        ax_line = Line(
            [-(spacing * 1.5), base_y, 0],
            [spacing * 2.2, base_y, 0],
            stroke_width=2, color=MUTED
        )
        self.play(Create(ax_line), run_time=0.4)

        # "Best human" dashed line
        human_line = DashedLine(
            [-(spacing * 1.5), base_y + ceiling, 0],
            [spacing * 2.2, base_y + ceiling, 0],
            dash_length=0.2, stroke_width=1.5, color=MUTED, stroke_opacity=0.6
        )
        human_label = Text(
            "best human", font=SANS, font_size=24, color=MUTED
        ).next_to(human_line, RIGHT, buff=0.15)
        self.play(Create(human_line), FadeIn(human_label, shift=RIGHT*0.2), run_time=0.5)

        bars     = []
        lbl_mobs = []
        for x, lbl in zip(xs, labels):
            bar = Rectangle(
                width=bar_w, height=0.01,
                fill_color=INK, fill_opacity=0.75, stroke_width=0
            ).move_to([x, base_y, 0]).align_to(
                [x, base_y, 0], DOWN
            )
            lbl_mob = Text(lbl, font=SERIF, font_size=26, color=INK).move_to(
                [x, base_y - 0.35, 0]
            )
            bars.append(bar)
            lbl_mobs.append(lbl_mob)
            self.add(bar)

        self.play(
            *[FadeIn(l, shift=UP*0.1) for l in lbl_mobs],
            run_time=0.5
        )

        # Grow bars: each reaches ceiling, then caps near frame top
        # Final height 6.0 → top at base_y+6.0 = 3.2 (frame top = 4.0, safe)
        for x, bar in zip(xs, bars):
            self.play(
                bar.animate.stretch_to_fit_height(ceiling).align_to(
                    [0, base_y, 0], DOWN
                ),
                run_time=0.5, rate_func=smooth
            )
            # Color shift as it hits the ceiling
            self.play(bar.animate.set_fill(SPARK), run_time=0.15)
            # Cap within frame — arrow indicates chart continues beyond
            self.play(
                bar.animate.stretch_to_fit_height(6.0).align_to(
                    [0, base_y, 0], DOWN
                ),
                run_time=0.45, rate_func=rush_into
            )
            # Upward arrow: tip at ~3.25 (pixel ~101 from safe top=54), well within frame
            arr = Arrow(
                [x, 2.5, 0], [x, 3.0, 0],
                stroke_width=3, color=SPARK, buff=0, tip_length=0.25
            ).set_opacity(0.85)
            self.play(FadeIn(arr), run_time=0.15)

        self.wait(0.3)

        # Strike-through "frighten" → "reorganize"
        frighten = Text("frighten", font=SERIF, font_size=52, color=INK).to_edge(DOWN, buff=0.6)
        self.play(Write(frighten), run_time=0.4)
        strike = Line(frighten.get_left(), frighten.get_right(), stroke_width=3, color=SPARK)
        self.play(Create(strike), run_time=0.3)

        reorganize = Text("reorganize", font=SERIF, font_size=52, color=SPARK).next_to(
            frighten, DOWN, buff=0.25
        )
        self.play(Write(reorganize), run_time=0.5)
        self.wait(1.0)


# ─────────────────────────────────────────────────────────────────────────────
# B13 — Gardner's frame — and the question it never faced
# Seven intelligence chips fan out. An 8th appears (naturalist, solid).
# A 9th appears (existential, dashed — tentative). A machine mark approaches.
# A new axis draws: "Which intelligences does technology endanger?"
# ─────────────────────────────────────────────────────────────────────────────
class B13_GardnersFrame(Scene):
    def construct(self):
        self.camera.background_color = PAGE

        # Year label — buff=0.9 keeps it inside safe area left boundary (safe x = ±6.4)
        year = Text("1983", font=SANS, font_size=34, color=MUTED, weight=BOLD).to_corner(UL, buff=0.9)
        self.play(Write(year), run_time=0.4)

        intelligences_7 = [
            "Linguistic", "Logical-\nMathematical", "Spatial",
            "Musical", "Bodily-\nKinesthetic", "Interpersonal", "Intrapersonal"
        ]

        # Fan out 7 chips in a row — fill_opacity 0.40 so ink registers (>28 delta)
        chips = []
        for i, name in enumerate(intelligences_7):
            angle  = (i / 6) * TAU * 0.35 - TAU * 0.35 / 2
            radius = 2.6
            x      = radius * math.sin(angle)
            y      = 0.4 + radius * math.cos(angle) * 0.35
            chip = RoundedRectangle(
                corner_radius=0.15, width=1.6, height=0.8,
                fill_color=INK, fill_opacity=0.40,
                stroke_color=INK, stroke_width=1.5
            ).move_to([x, y, 0])
            label = Text(name, font=SERIF, font_size=18, color=PAGE).move_to(chip.get_center())
            chips.append(VGroup(chip, label))

        self.play(LaggedStart(*[GrowFromCenter(c) for c in chips], lag_ratio=0.12), run_time=1.2)
        self.wait(0.3)

        # 8th chip — naturalist, solid
        eighth = RoundedRectangle(
            corner_radius=0.15, width=1.6, height=0.8,
            fill_color=MUTED, fill_opacity=0.40,
            stroke_color=MUTED, stroke_width=1.5
        ).move_to([3.4, -0.5, 0])
        eighth_lbl = Text("Naturalist\n(1995)", font=SERIF, font_size=17, color=INK).move_to(eighth.get_center())
        self.play(GrowFromCenter(VGroup(eighth, eighth_lbl)), run_time=0.5)

        # 9th chip — existential, tentative
        ninth = RoundedRectangle(
            corner_radius=0.15, width=1.6, height=0.8,
            fill_color=PAGE, fill_opacity=0.0,
            stroke_color=MUTED, stroke_width=2, stroke_opacity=0.4
        ).move_to([3.4, -1.6, 0])
        ninth_lbl = Text("Existential?\n(tentative)", font=SERIF, font_size=16, color=MUTED).move_to([3.4, -1.6, 0])
        ninth_lbl.set_opacity(0.6)
        q = Text("?", font=SERIF, font_size=24, color=SPARK).next_to(ninth, UR, buff=-0.15)
        self.play(Create(ninth), FadeIn(ninth_lbl), Write(q), run_time=0.7)
        self.wait(0.2)

        # Machine mark — buff=0.9 keeps it inside safe area right boundary
        machine = Text("⚙", font=SANS, font_size=52, color=SPARK).to_edge(RIGHT, buff=0.9).shift(UP * 0.5)
        self.play(FadeIn(machine, shift=LEFT), run_time=0.5)

        # New axis draws
        axis = Arrow(
            [-5.5, -2.8, 0], [5.5, -2.8, 0],
            stroke_width=2, color=SPARK, buff=0
        )
        axis_lbl = Text(
            "Which intelligences does technology endanger?",
            font=SANS, font_size=22, color=SPARK
        ).next_to(axis, DOWN, buff=0.18)
        self.play(GrowArrow(axis), run_time=0.5)
        self.play(Write(axis_lbl), run_time=0.6)

        self.wait(0.3)
        changed = Text("The moment changed.", font=SERIF, font_size=40, color=SPARK).to_edge(DOWN, buff=0.7)
        self.play(Write(changed), run_time=0.6)
        self.wait(1.0)


# ─────────────────────────────────────────────────────────────────────────────
# B18 — Network: property lives on edges, not nodes
# Five nodes (roles) in an elliptical layout (rx=4.0, ry=2.0) to fill frame.
# Labels placed OUTSIDE the dots so each dot is a solid dark disk (no internal
# white text splitting the fill into arcs that trigger the §8.6b overlap check).
# Edges draw; glow appears on edges — NOT on nodes.
# A bounding box isolates one node; edge glow fades inside it.
# ─────────────────────────────────────────────────────────────────────────────
class B18_Network(Scene):
    def construct(self):
        self.camera.background_color = PAGE

        # Title anchors the top of the safe area
        title = Text("Intelligence lives between us.", font=SERIF, font_size=44, color=INK)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)

        roles  = ["scientist", "economist", "citizen", "researcher", "voter"]
        n      = len(roles)
        # rx=4.0 keeps rightmost/leftmost nodes clear of the frame edge with room for labels
        rx, ry = 4.0, 2.0
        positions = [
            [rx * math.cos(TAU * i / n - TAU / 4),
             ry * math.sin(TAU * i / n - TAU / 4), 0]
            for i in range(n)
        ]
        # Label directions: avoid frame edges; economist/voter go inward (LEFT/RIGHT)
        label_dirs = [LEFT, LEFT, UP, UP, RIGHT]

        # Phase 1: solid dots, labels outside — dots are uninterrupted dark disks
        # so §8.6b blob detection sees a square blob (w/h≈1) and filters it out.
        nodes  = []
        labels = []
        for pos, role, ldir in zip(positions, roles, label_dirs):
            dot = Circle(radius=0.42, fill_color=INK, fill_opacity=0.55,
                         stroke_color=INK, stroke_width=2.5).move_to(pos)
            lbl = Text(role, font=SERIF, font_size=26, color=INK)
            lbl.next_to(dot, ldir, buff=0.12)
            nodes.append(dot)
            labels.append(lbl)

        self.play(
            LaggedStart(*[GrowFromCenter(VGroup(d, l)) for d, l in zip(nodes, labels)], lag_ratio=0.18),
            run_time=1.0
        )
        node_lbl = Text("Each individual.", font=SANS, font_size=26, color=MUTED).to_edge(DOWN, buff=0.7)
        self.play(Write(node_lbl), run_time=0.4)
        self.wait(0.3)

        # Phase 2: draw edges with glow
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                e = Line(positions[i], positions[j],
                         stroke_width=4.5, stroke_color=INK, stroke_opacity=0.50)
                edges.append(e)

        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.06), run_time=0.8)

        edge_lbl = Text("The intelligence lives here.", font=SERIF, font_size=30, color=INK).to_edge(DOWN, buff=0.7)
        self.play(
            FadeOut(node_lbl, shift=DOWN*0.2),
            Write(edge_lbl),
            run_time=0.5
        )
        self.wait(0.4)

        # Phase 3: bounding box around one node — edge glow fades inside
        solo_pos = positions[0]
        box = SurroundingRectangle(
            nodes[0], color=INK, stroke_width=2, buff=0.55, corner_radius=0.2
        )
        box_lbl = Text("Individual intelligence\nframework", font=SANS, font_size=22, color=INK).next_to(
            box, UP, buff=0.15
        )

        connected_edges = [e for e in edges if (
            np.allclose(e.get_start(), solo_pos, atol=0.3) or
            np.allclose(e.get_end(), solo_pos, atol=0.3)
        )]

        self.play(
            Create(box),
            Write(box_lbl),
            *[e.animate.set_stroke(opacity=0.08) for e in connected_edges],
            run_time=0.8
        )

        final_lbl = Text(
            "Every MI framework is a framework of individuals.\nThis is what it misses.",
            font=SERIF, font_size=26, color=INK, line_spacing=1.4
        ).to_edge(DOWN, buff=0.3)
        self.play(
            FadeOut(edge_lbl, shift=DOWN*0.2),
            Write(final_lbl),
            run_time=0.8
        )
        self.wait(1.2)


# ─────────────────────────────────────────────────────────────────────────────
# B19 — The lossy compression
# Author nodes feed text-marks into a compressor funnel.
# Model emits pattern back as a mirror. Edge-lines DO NOT pass the funnel.
# Credit label: "Ted Chiang · The New Yorker · 2023"
# ─────────────────────────────────────────────────────────────────────────────
class B19_LossyCompression(Scene):
    def construct(self):
        self.camera.background_color = PAGE

        # Title anchors the top of the safe area
        title = Text("The Lossy Compression", font=SERIF, font_size=44, color=INK)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)

        # Author nodes — fill_opacity 0.55 so blended color registers as ink (delta>28)
        author_positions = [[-5.0, 1.8, 0], [-5.0, 0.0, 0], [-5.0, -1.8, 0]]
        author_mobs = []
        for pos in author_positions:
            dot = Circle(radius=0.32, fill_color=INK, fill_opacity=0.55,
                         stroke_color=INK, stroke_width=2.0).move_to(pos)
            author_mobs.append(dot)

        self.play(LaggedStart(*[GrowFromCenter(d) for d in author_mobs], lag_ratio=0.2), run_time=0.7)

        # Compressor funnel — MUTED fill at 0.65 so it registers as ink
        funnel = Polygon(
            [-1.2, 2.2, 0], [1.2, 2.2, 0], [0.55, -0.4, 0], [-0.55, -0.4, 0],
            fill_color=MUTED, fill_opacity=0.65, stroke_color=INK, stroke_width=2
        ).move_to([0, 0, 0])
        funnel_lbl = Text("compress", font=SANS, font_size=20, color=PAGE, weight=BOLD).move_to([0, 0.5, 0])
        self.play(DrawBorderThenFill(funnel), Write(funnel_lbl), run_time=0.6)

        # Model — fill_opacity 0.55 so it registers as ink
        model = RoundedRectangle(corner_radius=0.2, width=2.0, height=1.1,
                                 fill_color=INK, fill_opacity=0.55,
                                 stroke_color=INK, stroke_width=2).move_to([4.5, 0, 0])
        model_lbl = Text("LLM", font=SANS, font_size=24, color=PAGE, weight=BOLD).move_to([4.5, 0, 0])
        self.play(GrowFromCenter(VGroup(model, model_lbl)), run_time=0.5)

        # Text-mark flows
        for pos in author_positions:
            line = Line(pos, [0, pos[1] * 0.3, 0], stroke_width=2.5, color=INK, stroke_opacity=0.70)
            self.play(Create(line), run_time=0.2)

        # Flow continues from funnel to model
        out_line = Arrow(
            [0.55, -0.4, 0], [3.4, 0, 0],
            stroke_width=3.0, color=INK, stroke_opacity=0.85, buff=0.05
        )
        self.play(GrowArrow(out_line), run_time=0.4)

        # Edge connections between authors (DO NOT pass through funnel)
        for i, pa in enumerate(author_positions):
            for j, pb in enumerate(author_positions):
                if j <= i:
                    continue
                edge = DashedLine(pa, pb, dash_length=0.15, stroke_width=2.5,
                                  color=SPARK, stroke_opacity=0.80)
                self.play(Create(edge), run_time=0.25)

        self.wait(0.3)

        edge_dissolve = Text("friction · disagreement · trust", font=SERIF, font_size=22,
                              color=SPARK, slant=ITALIC).to_edge(DOWN, buff=1.1)
        self.play(Write(edge_dissolve), run_time=0.5)
        self.wait(0.2)

        self.play(
            *[FadeOut(m, shift=RIGHT * 0.5) for m in self.mobjects
              if isinstance(m, DashedLine)],
            run_time=0.7
        )

        closing = Text(
            "Our own pattern-making, reflected back.",
            font=SERIF, font_size=34, color=SPARK
        ).to_edge(DOWN, buff=0.18)
        self.play(
            FadeOut(edge_dissolve, shift=DOWN * 0.3),
            Write(closing),
            run_time=0.7
        )
        self.wait(1.2)


# ─────────────────────────────────────────────────────────────────────────────
# B20 — The between: what the funnel strips
# Two author-nodes; idea chip bounces and reshapes on each pass.
# Only the final chip enters the corpus; the bounces dissolve behind it.
# ─────────────────────────────────────────────────────────────────────────────
class B20_TheBetween(Scene):
    def construct(self):
        self.camera.background_color = PAGE

        # Title anchors the top of the safe area
        title = Text("What the funnel strips.", font=SERIF, font_size=44, color=INK)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)

        posA = [-3.5, 0.8, 0]
        posB = [3.5, 0.8, 0]

        # Larger nodes, solid fill so they register as ink
        nodeA = Circle(radius=0.60, fill_color=INK, fill_opacity=0.50,
                       stroke_color=INK, stroke_width=2.5).move_to(posA)
        nodeB = Circle(radius=0.60, fill_color=INK, fill_opacity=0.50,
                       stroke_color=INK, stroke_width=2.5).move_to(posB)
        lblA  = Text("A", font=SERIF, font_size=30, color=PAGE, weight=BOLD).move_to(posA)
        lblB  = Text("B", font=SERIF, font_size=30, color=PAGE, weight=BOLD).move_to(posB)

        self.play(GrowFromCenter(VGroup(nodeA, lblA)), GrowFromCenter(VGroup(nodeB, lblB)), run_time=0.6)

        # Initial idea chip — solid enough fill to register
        idea = RoundedRectangle(corner_radius=0.12, width=1.0, height=0.55,
                                fill_color=INK, fill_opacity=0.75,
                                stroke_color=INK, stroke_width=2.0).move_to(posA)
        idea_lbl = Text("idea₀", font=SERIF, font_size=18, color=PAGE).move_to(posA)
        self.play(GrowFromCenter(VGroup(idea, idea_lbl)), run_time=0.4)

        bounce_traces = []

        # Three bounces: A→B→A→B, idea reshapes each time
        for step, (src, dst, label, w, h) in enumerate([
            (posA, posB, "idea₁", 1.1, 0.60),
            (posB, posA, "idea₂", 1.2, 0.64),
            (posA, posB, "idea₃", 1.3, 0.68),
        ]):
            arc = ArcBetweenPoints(src, dst, angle=0.45 * (1 - 2 * (step % 2)),
                                   stroke_width=2.5, stroke_color=SPARK, stroke_opacity=0.70)
            self.play(Create(arc), run_time=0.3)
            bounce_traces.append(arc)

            new_idea = RoundedRectangle(corner_radius=0.12, width=w, height=h,
                                        fill_color=INK, fill_opacity=0.75,
                                        stroke_color=SPARK, stroke_width=2.5).move_to(dst)
            new_lbl  = Text(label, font=SERIF, font_size=18, color=PAGE).move_to(dst)
            self.play(
                ReplacementTransform(VGroup(idea, idea_lbl), VGroup(new_idea, new_lbl)),
                run_time=0.4
            )
            idea     = new_idea
            idea_lbl = new_lbl

        # Final chip moves into corpus — buff=1.5 keeps label inside safe area right boundary
        corpus = Text("corpus", font=SANS, font_size=26, color=INK).to_edge(RIGHT, buff=1.5).shift(DOWN * 1.0)
        self.play(FadeIn(corpus, shift=LEFT * 0.2), run_time=0.3)
        self.play(idea.animate.move_to([4.8, -1.0, 0]),
                  idea_lbl.animate.move_to([4.8, -1.0, 0]),
                  run_time=0.6, rate_func=smooth)
        self.play(FadeOut(idea), FadeOut(idea_lbl), run_time=0.2)

        # Dissolve all bounce arcs
        self.play(*[FadeOut(b) for b in bounce_traces], run_time=0.6)

        final = Text("Never in the text to begin with.", font=SERIF,
                     font_size=38, color=SPARK).to_edge(DOWN, buff=0.4)
        self.play(Write(final), run_time=0.7)
        self.wait(1.2)


# ─────────────────────────────────────────────────────────────────────────────
# CLI entry point
# Usage: python scenes.py B09 --output media/B09.mp4
# ─────────────────────────────────────────────────────────────────────────────
SCENES = {
    "B09": B09_OffTheChart,
    "B13": B13_GardnersFrame,
    "B18": B18_Network,
    "B19": B19_LossyCompression,
    "B20": B20_TheBetween,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scenes.py <BID> [--output <path>]")
        print(f"Available: {list(SCENES.keys())}")
        sys.exit(1)
    bid = sys.argv[1].upper()
    if bid not in SCENES:
        print(f"Unknown scene {bid}. Available: {list(SCENES.keys())}")
        sys.exit(1)
    out = "media/" + bid + ".mp4"
    for i, a in enumerate(sys.argv):
        if a == "--output" and i + 1 < len(sys.argv):
            out = sys.argv[i + 1]
    cls = SCENES[bid]
    cmd = [
        sys.executable, "-m", "manim",
        __file__, cls.__name__,
        "-qk", "--output_file", out,
        "--format", "mp4"
    ]
    subprocess.run(cmd, check=True)
