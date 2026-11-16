"""scenes.py — claude-liam-pick-your-pebble
Topic: Pick Your Pebble — how to choose a red-team target and write its Dossier
Render: python3 -m manim scenes.py <ClassName> -r 1920,1080 --fps 30 --format mp4
  mv media/videos/scenes/1080p30/<ClassName>.mp4 media/<BXX>.mp4
"""
import json, pathlib, math
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

CREAM = "#F2F0E9"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#7A7265"
TEAL = "#2A9D8F"; CRIMSON = "#C1121F"
config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _bs["beats"]})
except Exception:
    pass

def dur(bid): return DUR.get(bid, 8.0)
def serif(t, sz=40, clr=INK, **k): return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)
def caps(t, sz=24, clr=MUTE, **k): return Text(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **k)
def card(w, h, fill=WHITE, stroke=INK, sw=2): return RoundedRectangle(corner_radius=0.12, width=w, height=h, fill_color=fill, fill_opacity=1.0, stroke_color=stroke, stroke_width=sw)


class B02_FastestPath(Scene):
    """Y-fork: two paths to a Pebble converge at YOUR PEBBLE (terracotta).
    TERRACOTTA MOMENT: the convergence circle."""
    def construct(self):
        d = dur("B02")

        # Header inside safe area (safe top ≈ 3.4; move_to y=2.95 keeps text clear)
        header = caps("fastest path to done", sz=28, clr=MUTE).move_to([0, 2.95, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Fork origin dot
        origin = Dot(color=INK, radius=0.08).move_to([0, 1.9, 0])
        self.play(FadeIn(origin), run_time=0.2)

        # Left branch: DOG-FOOD IT (teal)
        left_arrow = Arrow(start=[0, 1.9, 0], end=[-3.2, 0.1, 0],
                           color=TEAL, stroke_width=4, buff=0, tip_length=0.22)
        left_label = serif("DOG-FOOD IT", sz=40, clr=TEAL, weight=BOLD).move_to([-3.6, 0.9, 0])
        left_sub   = serif("you already run it", sz=26, clr=MUTE).move_to([-3.6, 0.4, 0])
        self.play(GrowArrow(left_arrow), run_time=0.6)
        self.play(FadeIn(left_label, shift=LEFT*0.1), FadeIn(left_sub, shift=LEFT*0.1), run_time=0.4)

        # Right branch: PUBLIC CASE (ink)
        # Sub-label placed BELOW the convergence arrows to avoid overlapping arrow body
        right_arrow = Arrow(start=[0, 1.9, 0], end=[3.4, 0.4, 0],
                            color=INK, stroke_width=4, buff=0, tip_length=0.22)
        right_label = serif("PUBLIC CASE", sz=40, clr=INK, weight=BOLD).move_to([3.6, 1.5, 0])
        right_sub   = serif("documented failure\nno auth question", sz=24, clr=MUTE,
                            line_spacing=0.9).move_to([3.5, -0.8, 0])
        self.play(GrowArrow(right_arrow), run_time=0.6)
        self.play(FadeIn(right_label, shift=RIGHT*0.1), FadeIn(right_sub, shift=RIGHT*0.1), run_time=0.4)

        # Convergence: YOUR PEBBLE (terracotta — the ONE accent)
        # Dot + label BELOW dot (avoids "label on a curve" audit flag)
        conv_left  = Arrow(start=[-3.2, 0.1, 0], end=[0, -1.7, 0],
                           color=TEAL, stroke_width=3, buff=0, tip_length=0.16)
        conv_right = Arrow(start=[3.4, 0.4, 0],  end=[0, -1.7, 0],
                           color=INK,  stroke_width=3, buff=0, tip_length=0.16)
        pebble_dot = Circle(radius=0.42, fill_color=ACCENT, fill_opacity=1.0,
                            stroke_width=0).move_to([0, -1.7, 0])
        pebble_lbl = caps("YOUR PEBBLE", sz=26, clr=ACCENT).next_to(pebble_dot, DOWN, buff=0.2)
        self.play(GrowArrow(conv_left), GrowArrow(conv_right), run_time=0.5)
        self.play(GrowFromCenter(pebble_dot), run_time=0.4)
        self.play(FadeIn(pebble_lbl), run_time=0.3)

        self.wait(max(0.01, d - 6.5))


class B03_HonestyFloor(Scene):
    """ARTIFACT vs WORLD with honesty floor gap.
    Two arrow passes: crimson (stops at artifact) then teal (crosses to world).
    No terracotta accent — this beat uses teal/crimson as the semantic pair."""
    def construct(self):
        d = dur("B03")

        # --- ARTIFACT zone (left) ---
        artifact_box = card(3.6, 2.0, fill=WHITE, stroke=INK, sw=2).move_to([-3.5, 0.7, 0])
        artifact_cap = caps("artifact", sz=22, clr=MUTE).next_to(artifact_box, UP, buff=0.15)
        artifact_lbl = serif("SUCCESS REPORT", sz=26, clr=INK, weight=BOLD).move_to([-3.5, 0.95, 0])
        artifact_chk = serif("✓ email sent", sz=28, clr=TEAL).move_to([-3.5, 0.45, 0])
        self.play(FadeIn(artifact_box), FadeIn(artifact_cap), run_time=0.4)
        self.play(FadeIn(artifact_lbl, shift=UP*0.05), FadeIn(artifact_chk, shift=UP*0.05), run_time=0.4)

        # --- Gap separator + label ABOVE separator line ---
        gap_line = Line([0, -0.4, 0], [0, 2.0, 0], color=MUTE, stroke_width=1.5)
        gap_lbl  = serif("THE HONESTY FLOOR", sz=28, clr=INK).move_to([0, 2.35, 0])
        self.play(FadeIn(gap_line), FadeIn(gap_lbl, shift=UP*0.06), run_time=0.5)

        # --- WORLD zone (right) ---
        world_box  = card(3.6, 2.0, fill=WHITE, stroke=INK, sw=2).move_to([3.5, 0.7, 0])
        world_cap  = caps("world", sz=22, clr=MUTE).next_to(world_box, UP, buff=0.15)
        world_lbl  = serif("ACTUAL SENT FOLDER", sz=24, clr=INK, weight=BOLD).move_to([3.5, 0.95, 0])
        world_sub  = serif("real state", sz=26, clr=MUTE).move_to([3.5, 0.45, 0])
        self.play(FadeIn(world_box), FadeIn(world_cap), run_time=0.4)
        self.play(FadeIn(world_lbl, shift=UP*0.05), FadeIn(world_sub, shift=UP*0.05), run_time=0.4)

        # --- WITHOUT CARING: arrow stops at artifact, crimson X ---
        dont_label = serif("without caring:", sz=24, clr=CRIMSON).move_to([-2.2, -0.9, 0])
        dont_arrow = Arrow(start=[-5.8, -1.3, 0], end=[-1.5, -1.3, 0],
                           color=CRIMSON, stroke_width=3, buff=0, tip_length=0.18)
        dont_x   = Text("×", font="Helvetica", font_size=44, color=CRIMSON).move_to([-0.8, -1.3, 0])
        dont_sub = serif("trust the report", sz=22, clr=CRIMSON).move_to([-2.4, -1.7, 0])
        self.play(FadeIn(dont_label), run_time=0.3)
        self.play(GrowArrow(dont_arrow), run_time=0.5)
        self.play(FadeIn(dont_x), FadeIn(dont_sub), run_time=0.3)

        # --- WITH CARING: teal arrow crosses gap; sub stays inside safe area (y > -3.4) ---
        do_label = serif("with caring:", sz=24, clr=TEAL).move_to([0.6, -0.9, 0])
        do_arrow = Arrow(start=[-5.8, -2.4, 0], end=[3.2, -2.4, 0],
                         color=TEAL, stroke_width=3, buff=0, tip_length=0.18)
        do_check = Text("✓", font="Helvetica", font_size=44, color=TEAL).move_to([3.8, -2.4, 0])
        do_sub   = serif("check the world", sz=22, clr=TEAL).move_to([1.2, -2.85, 0])
        self.play(FadeIn(do_label), run_time=0.3)
        self.play(GrowArrow(do_arrow), run_time=0.7)
        self.play(FadeIn(do_check), FadeIn(do_sub), run_time=0.3)

        self.wait(max(0.01, d - 8.5))


class B07_ArtifactVsWorld(Scene):
    """ARTIFACT ≠ WORLD — the one discipline.
    TERRACOTTA MOMENT: 'LIES?' overlay on the artifact."""
    def construct(self):
        d = dur("B07")

        # --- ARTIFACT block (left) ---
        art_box = card(3.6, 2.6, fill=WHITE, stroke=INK, sw=2).move_to([-3.4, 0.4, 0])
        art_cap = caps("artifact", sz=24, clr=MUTE).next_to(art_box, UP, buff=0.18)
        # art_lbl near top; ✓ near bottom; LIES? in middle — all separated vertically
        art_lbl = serif("SUCCESS REPORT", sz=26, clr=INK, weight=BOLD).move_to([-3.4, 1.1, 0])
        art_chk = serif("✓", sz=38, clr=TEAL).move_to([-3.4, -0.15, 0])
        self.play(FadeIn(art_box), FadeIn(art_cap), run_time=0.4)
        self.play(FadeIn(art_lbl, shift=UP*0.05), FadeIn(art_chk, shift=UP*0.05), run_time=0.4)

        # TERRACOTTA MOMENT: "LIES?" in the middle gap between art_lbl (top) and ✓ (bottom)
        lies_lbl = serif("LIES?", sz=48, clr=ACCENT, weight=BOLD).move_to([-3.4, 0.42, 0])
        self.play(FadeIn(lies_lbl, shift=UP*0.08), run_time=0.45)

        # --- Center separator + THE ONE DISCIPLINE label ---
        # Label placed ABOVE the separator line to avoid "label on a curve" audit error
        disc_lbl = caps("the one discipline", sz=22, clr=INK).move_to([0, 2.1, 0])
        sep = DashedLine(start=[0, 1.7, 0], end=[0, -1.2, 0],
                         color=MUTE, stroke_width=2, dash_length=0.18)
        self.play(FadeIn(disc_lbl), FadeIn(sep), run_time=0.45)

        # --- WORLD block (right) ---
        world_box = card(3.6, 2.6, fill=WHITE, stroke=INK, sw=2).move_to([3.4, 0.4, 0])
        world_cap = caps("world", sz=24, clr=MUTE).next_to(world_box, UP, buff=0.18)
        world_lbl = serif("ACTUAL STATE", sz=28, clr=INK, weight=BOLD).move_to([3.4, 0.8, 0])
        # Magnifying glass: a circle + handle line
        mg_circle = Circle(radius=0.38, stroke_color=INK, stroke_width=3, fill_opacity=0).move_to([3.3, 0.1, 0])
        mg_handle = Line([3.55, -0.15, 0], [3.75, -0.45, 0], color=INK, stroke_width=4)
        self.play(FadeIn(world_box), FadeIn(world_cap), run_time=0.4)
        self.play(FadeIn(world_lbl, shift=UP*0.05),
                  Create(mg_circle), Create(mg_handle), run_time=0.4)

        # --- Bottom annotation ---
        note = serif("Your hunch names the gap.", sz=34, clr=INK).to_edge(DOWN, buff=0.85)
        self.play(FadeIn(note, shift=UP*0.08), run_time=0.5)

        self.wait(max(0.01, d - 7.0))
