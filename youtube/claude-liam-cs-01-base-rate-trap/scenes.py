"""scenes.py — claude-liam-cs-01-base-rate-trap Manim scenes (STD retrofit)

10 TELLS beats rebuilt as Manim animations:
  B01 B02 B04 B05 B07 B08 B09 B10 B11 B12

Render (from this folder):
  python3 -m manim scenes.py B01_Title -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B02_PopulationGridSweep -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B04_FlaggedBucketFill -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B05_RarityNoiseDivergence -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B07_DotGridSweepAndBucket -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B08_AccuracyMisreadHighlight -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B09_FraudQueueNoise -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B10_PositivePrecisionHighlight -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B11_BaseRateCheckFix -r 1920,1080 --fps 30 --format mp4
  python3 -m manim scenes.py B12_HospitalSepsisExample -r 1920,1080 --fps 30 --format mp4

Move outputs:
  mv media/videos/scenes/1080p30/B01_Title.mp4 media/B01.mp4  (etc.)

Color semantics from beat_sheet.json:
  TEAL    = true positives / correctly flagged
  CRIMSON = false positives / noise in the bucket
  GOLD    = the base rate / the key number
  SLATE   = healthy population
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

# ── Palette ──────────────────────────────────────────────────────────────────
CREAM   = "#F2F0E9"
INK     = "#3D3929"
ACCENT  = "#D97757"   # terracotta — ONE focal moment (B07)
MUTE    = "#7A7265"
TEAL    = "#2A9D8F"
CRIMSON = "#C1121F"
GOLD    = "#E9C46A"
SLATE_C = "#8D99AE"

config.background_color = CREAM

# ── Durations from beat sheet ────────────────────────────────────────────────
DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _bs["beats"]
    })
except Exception:
    pass

def dur(bid): return DUR.get(bid, 8.0)


# ── Shared helpers ────────────────────────────────────────────────────────────

def card(w, h, fill=WHITE, stroke=INK, sw=2, radius=0.12):
    return RoundedRectangle(corner_radius=radius, width=w, height=h,
                            fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw)

def serif(txt, sz=40, clr=INK, **kw):
    return Text(txt, font="EB Garamond", font_size=sz, color=clr, **kw)

def caps(txt, sz=24, clr=MUTE, **kw):
    return Text(txt.upper(), font="Montserrat", font_size=sz, color=clr,
                weight=BOLD, **kw)

def hairline(length=6, clr=INK, sw=1):
    return Line(ORIGIN, RIGHT * length, color=clr, stroke_width=sw)


# ─────────────────────────────────────────────────────────────────────────────
# B01_Title — "Your 99%-accurate test just came back positive—and you're almost certainly fine."
# Show: title text scan-lines in, key stat flashes terracotta
# ─────────────────────────────────────────────────────────────────────────────
class B01_Title(Scene):
    def construct(self):
        d = dur("B01")  # 5.7s

        eyebrow = caps("THE 99% TRAP", sz=28, clr=MUTE)
        line1 = serif("Your test came back positive.", sz=60, clr=INK)
        line2 = serif("You're almost certainly fine.", sz=60, clr=INK)

        group = VGroup(eyebrow, line1, line2).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        # Scan in lines sequentially
        self.play(FadeIn(eyebrow, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(line1, shift=UP * 0.12), run_time=0.8)
        self.play(FadeIn(line2, shift=UP * 0.12), run_time=0.8)
        self.wait(max(0.01, d - 2.1))


# ─────────────────────────────────────────────────────────────────────────────
# B02_PopulationGridSweep — 10,000 people, 1 sick, 99% test, 100 flagged, 1% PPV
# Show: grid of 100 dots (representing 10K), sweep flags 1 gold + ~1 crimson,
#       bucket fills to show ratio
# ─────────────────────────────────────────────────────────────────────────────
class B02_PopulationGridSweep(Scene):
    def construct(self):
        d = dur("B02")  # 19.05s

        eyebrow = caps("10,000 people — 1 sick", sz=24, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Scale context shown BEFORE grid (avoids dot-overlap in layout audit)
        scale_lbl = caps("each dot ≈ 100 people", sz=20, clr=MUTE).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(scale_lbl), run_time=0.3)
        self.wait(0.3)
        self.remove(scale_lbl)  # clear before dots appear

        # Draw a 10×10 grid of small dots (each dot = 100 people)
        # 1 dot = the sick person's "block" (gold), rest = healthy (slate)
        rows, cols = 10, 10
        dot_r = 0.22
        spacing = 0.6
        dots = []
        grid_group = VGroup()

        for r in range(rows):
            for c in range(cols):
                x = (c - cols / 2 + 0.5) * spacing
                y = (rows / 2 - r - 0.5) * spacing
                dot = Dot(radius=dot_r, color=SLATE_C, fill_opacity=1.0)
                dot.move_to([x, y - 0.3, 0])
                dots.append(dot)
                grid_group.add(dot)

        self.play(FadeIn(grid_group), run_time=0.8)
        self.wait(0.5)

        # "1 sick person" — highlight top-left dot gold
        sick_dot = dots[0]
        self.play(sick_dot.animate.set_fill(GOLD, opacity=1.0), run_time=0.6)
        sick_lbl = caps("1 sick", sz=20, clr=GOLD).next_to(sick_dot, LEFT, buff=0.15)
        self.play(FadeIn(sick_lbl), run_time=0.3)
        self.wait(0.4)

        # Sweep the test — turn sick dot TEAL (true positive)
        sweep_lbl = caps("test sweeps…", sz=22, clr=MUTE).move_to([4.5, 3.0, 0])
        self.play(FadeIn(sweep_lbl), run_time=0.3)
        self.play(sick_dot.animate.set_color(TEAL), run_time=0.5)
        self.remove(sick_lbl)

        # False positives: 1% of 99 remaining "dot blocks" = ~1 dot highlighted crimson
        # Show: first dot after the sick one turns crimson (representing 99 people flagged)
        fp_dot = dots[1]
        fp_lbl = caps("99 false positives", sz=18, clr=CRIMSON)
        fp_lbl.next_to(grid_group, RIGHT, buff=0.4)
        self.play(fp_dot.animate.set_fill(CRIMSON, opacity=1.0), run_time=0.6)
        self.play(FadeIn(fp_lbl), run_time=0.4)
        self.wait(0.5)

        # Bucket: clear grid scaffolding, show flagged dots with ratio
        self.remove(sweep_lbl)
        self.remove(grid_group)
        self.remove(fp_lbl)
        bucket_bg = card(3.8, 1.2, fill=WHITE, stroke=INK, sw=2).move_to([4.0, -0.5, 0])
        bucket_lbl = caps("positives bucket", sz=20, clr=MUTE).next_to(bucket_bg, UP, buff=0.1)
        t_dot = Dot(radius=0.25, color=TEAL).move_to([3.2, -0.5, 0])
        c_dot_s = Dot(radius=0.25, color=CRIMSON).next_to(t_dot, RIGHT, buff=0.3)
        c_dots_label = serif("99×", sz=36, clr=CRIMSON).next_to(c_dot_s, RIGHT, buff=0.2)

        self.play(FadeIn(bucket_bg), FadeIn(bucket_lbl), run_time=0.5)
        self.play(FadeIn(t_dot), FadeIn(c_dot_s), FadeIn(c_dots_label), run_time=0.6)
        self.wait(0.4)

        # Final stat: fraction + label (fraction bar adds sharp horizontal edge → LV)
        frac_top = serif("1 sick", sz=44, clr=TEAL).move_to([-1.5, -1.0, 0])
        frac_bar = Line([-2.4, -1.45, 0], [-0.6, -1.45, 0], color=INK, stroke_width=3)
        frac_bot = serif("100 flagged", sz=44, clr=CRIMSON).move_to([-1.5, -1.9, 0])
        frac_bar._qc_intentional = True
        pct_lbl = serif("= 1% chance you have the disease", sz=36, clr=INK).move_to([1.8, -1.45, 0])
        self.play(FadeIn(frac_top), FadeIn(frac_bar), FadeIn(frac_bot), run_time=0.5)
        self.play(FadeIn(pct_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.01, d - 11.0))


# ─────────────────────────────────────────────────────────────────────────────
# B04_FlaggedBucketFill — error × healthy population = noise. Bucket = 99:1 crimson
# ─────────────────────────────────────────────────────────────────────────────
class B04_FlaggedBucketFill(Scene):
    def construct(self):
        d = dur("B04")  # 21.93s

        eyebrow = caps("1% error × 9,999 healthy people", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Left side: math building up
        eq1 = serif("9,999 healthy people", sz=44, clr=INK).move_to([-3.5, 1.5, 0])
        eq2 = serif("× 1% error rate", sz=44, clr=INK).move_to([-3.5, 0.6, 0])
        eq_line = Line([-5.8, 0.1, 0], [-1.2, 0.1, 0], color=INK, stroke_width=2)
        eq3 = serif("≈ 99 false positives", sz=48, clr=CRIMSON).move_to([-3.5, -0.5, 0])

        self.play(FadeIn(eq1, shift=RIGHT * 0.1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(eq2, shift=RIGHT * 0.1), run_time=0.6)
        self.play(GrowFromPoint(eq_line, eq_line.get_left()), run_time=0.4)
        self.play(FadeIn(eq3, shift=UP * 0.1), run_time=0.7)
        self.wait(0.5)

        # Right side: the bucket (vertical bar chart style)
        bucket_x = 3.0
        # Bucket container
        bucket_rect = Rectangle(width=1.6, height=4.0, color=INK, stroke_width=2.5,
                                 fill_opacity=0).move_to([bucket_x, -0.3, 0])
        bucket_rect._qc_intentional = True  # structural container, not a data axis
        bucket_cap = caps("FLAGGED\nBUCKET", sz=18, clr=MUTE).next_to(bucket_rect, UP, buff=0.15)
        self.play(Create(bucket_rect), FadeIn(bucket_cap), run_time=0.5)

        # Fill crimson (99 false positives) — animate fill from bottom
        crimson_fill = Rectangle(width=1.4, height=3.88, fill_color=CRIMSON, fill_opacity=0.85,
                                  stroke_width=0)
        crimson_fill.align_to(bucket_rect, DOWN).shift(UP * 0.06).shift(RIGHT * (bucket_x - 0))
        crimson_fill.move_to([bucket_x, -0.31, 0])
        crimson_fill.set_height(0.001)
        crimson_fill.align_to(bucket_rect, DOWN).shift(UP * 0.06)

        # Simpler: animate height
        crimson_bar = Rectangle(width=1.4, color=CRIMSON, fill_opacity=0.85, stroke_width=0)
        crimson_bar.set_height(3.82).move_to([bucket_x, -0.31, 0])
        crimson_bar.scale(1).align_to(bucket_rect, DOWN).shift(UP * 0.08)
        crimson_bar._qc_intentional = True

        self.play(GrowFromEdge(crimson_bar, DOWN), run_time=1.5)
        # Label outside the bucket to avoid bucket-border overlap
        fp_in_bucket = caps("99 false positives", sz=14, clr=CRIMSON).next_to(bucket_rect, RIGHT, buff=0.25).set_y(-0.31)
        self.play(FadeIn(fp_in_bucket), run_time=0.4)

        # 1 teal dot at top of bucket
        teal_sliver = Rectangle(width=1.4, height=0.10, fill_color=TEAL, fill_opacity=1,
                                  stroke_width=0)
        teal_sliver.align_to(bucket_rect, UP).shift(DOWN * 0.07).shift(RIGHT * (bucket_x - 0))
        teal_sliver.move_to([bucket_x, crimson_bar.get_top()[1] + 0.05, 0])

        # Just show a teal dot at top
        tp_dot = Dot(radius=0.18, color=TEAL).move_to([bucket_x, bucket_rect.get_top()[1] - 0.22, 0])
        tp_dot._qc_intentional = True
        self.play(FadeIn(tp_dot), run_time=0.5)
        # Label outside bucket right border to avoid label-on-line detection
        tp_lbl = caps("1 true positive", sz=15, clr=TEAL).next_to(bucket_rect, RIGHT, buff=0.25).set_y(1.48)
        self.play(FadeIn(tp_lbl), run_time=0.3)
        self.wait(0.5)

        # Final: "1% chance after testing positive"
        result = serif("P(sick | positive) = 1%", sz=44, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.01, d - 12.0))


# ─────────────────────────────────────────────────────────────────────────────
# B05_RarityNoiseDivergence — accuracy and base rate live in separate equations
# Show: two number tracks split apart — accuracy stays high, noise grows
# ─────────────────────────────────────────────────────────────────────────────
class B05_RarityNoiseDivergence(Scene):
    def construct(self):
        d = dur("B05")  # 22.17s

        eyebrow = caps("two separate equations", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Two tracks
        y_acc = 1.2
        y_base = -1.2
        x_start = -5.0
        x_end = 5.0

        acc_line = Line([x_start, y_acc, 0], [x_end, y_acc, 0], color=TEAL, stroke_width=4)
        acc_line._qc_intentional = True  # thematic track, not a data axis
        base_line = Line([x_start, y_base, 0], [x_end, y_base, 0], color=CRIMSON, stroke_width=4)
        base_line._qc_intentional = True

        acc_lbl = caps("TEST ACCURACY", sz=24, clr=TEAL).move_to([x_start + 2.0, y_acc + 0.45, 0])
        base_lbl = caps("BASE RATE", sz=24, clr=CRIMSON).move_to([x_start + 1.5, y_base - 0.45, 0])

        # Accuracy value stays high (flat line)
        acc_val = serif("99%", sz=52, clr=TEAL).move_to([3.5, y_acc, 0])
        # Base rate is tiny
        base_val = serif("0.01%", sz=52, clr=CRIMSON).move_to([3.5, y_base, 0])

        # Center: noise section — noise_lbl above not_same's y-range to avoid text-on-text
        noise_lbl = serif("noise manufactured:", sz=38, clr=INK).move_to([0, 0.4, 0])
        noise_count = serif("99 false alarms per true case", sz=36, clr=CRIMSON).move_to([0, -0.7, 0])

        self.play(Create(acc_line), run_time=0.7)
        self.play(FadeIn(acc_lbl), FadeIn(acc_val), run_time=0.5)
        self.wait(0.3)
        self.play(Create(base_line), run_time=0.7)
        self.play(FadeIn(base_lbl), FadeIn(base_val), run_time=0.5)
        self.wait(0.5)

        # Arrow showing they're NOT the same thing
        arrow = Arrow([0, y_acc - 0.3, 0], [0, y_base + 0.3, 0],
                      color=MUTE, stroke_width=3, buff=0.1)
        arrow._qc_intentional = True  # annotation connector, not a data axis
        not_same = caps("≠ same equation", sz=22, clr=MUTE).next_to(arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow), FadeIn(not_same), run_time=0.7)
        self.wait(0.4)

        # Result: the noise calculation
        self.play(FadeIn(noise_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(noise_count, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))


# ─────────────────────────────────────────────────────────────────────────────
# B07_DotGridSweepAndBucket — the key animation: dot grid sweep, bucket fills
# TERRACOTTA MOMENT (highest impact beat in this video)
# ─────────────────────────────────────────────────────────────────────────────
class B07_DotGridSweepAndBucket(Scene):
    def construct(self):
        d = dur("B07")  # 22.46s

        eyebrow = caps("10,000 people — the sweep", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        # Grid: 25×8 dots (200 dots, representing 10K as 50 each)
        rows, cols = 8, 25
        dot_r = 0.14
        spacing_x, spacing_y = 0.42, 0.45
        dots = []
        grid_group = VGroup()

        for r in range(rows):
            for c in range(cols):
                x = (c - cols / 2 + 0.5) * spacing_x - 1.8
                y = (rows / 2 - r - 0.5) * spacing_y + 0.3
                dot = Dot(radius=dot_r, color=SLATE_C, fill_opacity=0.5)
                dot.move_to([x, y, 0])
                dots.append(dot)
                grid_group.add(dot)

        self.play(FadeIn(grid_group), run_time=0.6)

        # Sick dot = dot[0] (top-left), show GOLD
        sick_idx = 0
        dots[sick_idx].scale(1.5)
        self.play(dots[sick_idx].animate.set_fill(GOLD, opacity=1.0), run_time=0.4)
        gold_lbl = caps("1 sick (gold)", sz=18, clr=GOLD).move_to([-4.0, 2.5, 0])
        self.play(FadeIn(gold_lbl), run_time=0.2)
        self.wait(0.3)

        # Sweep animation: vertical sweep line passing left-to-right
        sweep_line = Line([grid_group.get_left()[0], grid_group.get_top()[1] + 0.1, 0],
                          [grid_group.get_left()[0], grid_group.get_bottom()[1] - 0.1, 0],
                          color=ACCENT, stroke_width=3, stroke_opacity=0.7)
        self.play(FadeIn(sweep_line), run_time=0.2)

        # As sweep passes sick dot — flag it TEAL (terracotta accent on sweep line)
        self.play(
            sweep_line.animate.move_to([dots[sick_idx].get_center()[0] + 0.05,
                                        sweep_line.get_center()[1], 0]),
            run_time=0.4
        )
        self.play(dots[sick_idx].animate.set_color(TEAL), run_time=0.3)
        teal_lbl = caps("true positive (teal)", sz=18, clr=TEAL).move_to([-1.0, 2.5, 0])
        self.play(FadeIn(teal_lbl), run_time=0.2)

        # Continue sweep — flag 3 random dots as crimson (representing 99 false positives)
        false_pos_indices = [12, 45, 78, 101, 134]
        self.play(
            sweep_line.animate.move_to([grid_group.get_center()[0],
                                        sweep_line.get_center()[1], 0]),
            run_time=0.8
        )
        for idx in false_pos_indices[:3]:
            self.play(dots[idx].animate.set_fill(CRIMSON, opacity=1.0), run_time=0.15)

        crimson_lbl = caps("99 false positives (crimson)", sz=18, clr=CRIMSON).move_to([2.8, 2.5, 0])
        self.play(FadeIn(crimson_lbl), run_time=0.2)

        # Sweep to the end
        self.play(
            sweep_line.animate.move_to([grid_group.get_right()[0] + 0.1,
                                        sweep_line.get_center()[1], 0]),
            *[dots[i].animate.set_fill(CRIMSON, opacity=0.9)
              for i in false_pos_indices[3:]],
            run_time=0.8
        )
        self.play(FadeOut(sweep_line), run_time=0.2)
        self.wait(0.3)

        # BUCKET: right side — fills crimson overwhelmingly
        bucket_x = 5.5
        bucket_rect = Rectangle(width=1.3, height=3.5, color=INK, stroke_width=2.5,
                                  fill_opacity=0).move_to([bucket_x, 0.0, 0])
        bucket_rect._qc_intentional = True
        bucket_cap = caps("POSITIVES\nBUCKET", sz=16, clr=MUTE).next_to(bucket_rect, UP, buff=0.1)
        self.play(Create(bucket_rect), FadeIn(bucket_cap), run_time=0.4)

        # Fill crimson bar growing from bottom — TERRACOTTA MOMENT (accent border)
        crimson_bar = Rectangle(width=1.1, fill_color=CRIMSON, fill_opacity=0.9, stroke_width=0)
        crimson_bar.set_height(0.01)
        crimson_bar.align_to(bucket_rect, DOWN).shift(UP * 0.07).move_to(
            [bucket_x, bucket_rect.get_bottom()[1] + 0.07, 0])
        target_h = 3.35
        final_crimson = Rectangle(width=1.1, height=target_h,
                                   fill_color=CRIMSON, fill_opacity=0.9, stroke_width=0)
        final_crimson.align_to(bucket_rect, DOWN).shift(UP * 0.07)
        final_crimson._qc_intentional = True

        bucket_rect.set_stroke(color=ACCENT, width=4)  # terracotta accent on the bucket
        self.play(GrowFromEdge(final_crimson, DOWN), run_time=1.2)

        # 1 teal dot at the top
        tp_dot = Dot(radius=0.18, color=TEAL).move_to([bucket_x, bucket_rect.get_top()[1] - 0.2, 0])
        tp_dot._qc_intentional = True
        self.play(FadeIn(tp_dot), run_time=0.3)

        # Label: "bucket is overwhelmingly noise"
        noise_lbl = serif("overwhelmingly noise", sz=36, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(noise_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 13.0))


# ─────────────────────────────────────────────────────────────────────────────
# B08_AccuracyMisreadHighlight — wrong reading struck through, correct one types in
# ─────────────────────────────────────────────────────────────────────────────
class B08_AccuracyMisreadHighlight(Scene):
    def construct(self):
        d = dur("B08")  # 18.37s

        eyebrow = caps("what '99% accurate' actually means", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Wrong reading
        wrong_lbl = caps("what we HEAR:", sz=22, clr=MUTE).move_to([-4.5, 1.5, 0])
        wrong = serif('"if I test positive,\n99% chance I am sick"', sz=44, clr=INK)
        wrong.move_to([0.5, 0.8, 0])

        wrong_bg = RoundedRectangle(corner_radius=0.12, width=7.0, height=1.9,
                                    fill_color=CRIMSON, fill_opacity=0.06,
                                    stroke_color=CRIMSON, stroke_width=1)
        wrong_bg.move_to([0.5, 0.8, 0])
        self.play(FadeIn(wrong_lbl), FadeIn(wrong_bg), run_time=0.3)
        self.play(FadeIn(wrong, shift=UP * 0.1), run_time=0.7)
        self.wait(0.5)

        # Strike through the wrong reading
        strike = Line(wrong.get_left() + LEFT * 0.2, wrong.get_right() + RIGHT * 0.2,
                      color=CRIMSON, stroke_width=6)
        strike._qc_intentional = True
        self.play(GrowFromPoint(strike, strike.get_left()), run_time=0.6)
        self.wait(0.3)

        # Correct reading fades in below
        correct_lbl = caps("what it ACTUALLY means:", sz=22, clr=MUTE).move_to([-3.8, -1.0, 0])
        correct = serif('"accuracy = per-person\nclassification rate"', sz=44, clr=TEAL)
        correct.move_to([0.5, -2.0, 0])

        self.play(FadeIn(correct_lbl), run_time=0.3)
        self.play(FadeIn(correct, shift=UP * 0.1), run_time=0.7)
        self.wait(0.5)

        # Separator: "what's in the bucket depends on the BASE RATE"
        bucket_note = serif("Bucket contents depend on the base rate.", sz=36, clr=INK)
        bucket_note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(bucket_note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.01, d - 8.0))


# ─────────────────────────────────────────────────────────────────────────────
# B09_FraudQueueNoise — fraud detection: queue fills with noise
# ─────────────────────────────────────────────────────────────────────────────
class B09_FraudQueueNoise(Scene):
    def construct(self):
        d = dur("B09")  # 26.77s

        eyebrow = caps("fraud detection — 99% accurate model", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Setup stats
        stats = VGroup(
            serif("fraud rate: 1 in 10,000 transactions", sz=36, clr=INK),
            serif("model accuracy: 99%", sz=36, clr=INK),
        ).arrange(DOWN, buff=0.3).move_to([0, 1.5, 0])
        self.play(FadeIn(stats, shift=UP * 0.1), run_time=0.7)
        self.wait(0.5)

        # Queue visualization: a list of flagged items
        queue_title = caps("FRAUD QUEUE (flagged positives)", sz=22, clr=MUTE).move_to([0, 0.2, 0])
        self.play(FadeIn(queue_title), run_time=0.3)

        # Draw queue items — 1 real fraud (teal) + 99 false alarms (crimson)
        queue_items = []
        y_start = -0.2
        for i in range(10):  # show 10 representative items
            color = TEAL if i == 0 else CRIMSON
            label = "FRAUD" if i == 0 else "LEGITIMATE"
            bar = Rectangle(width=5.0, height=0.28, fill_color=color, fill_opacity=0.85,
                             stroke_width=0)
            bar._qc_intentional = True
            bar.move_to([0, y_start - i * 0.35, 0])
            count = "× 1" if i == 0 else "× 99 like this"
            txt_lbl = caps(count if i == 1 else "", sz=14, clr=color if i < 2 else MUTE)
            txt_lbl.next_to(bar, RIGHT, buff=0.1)
            queue_items.append(VGroup(bar, txt_lbl))

        for item in queue_items:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.15)

        # "analysts spend time clearing noise"
        analyst_note = serif("analysts: mostly clearing false alarms", sz=34, clr=INK)
        analyst_note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(analyst_note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.01, d - 10.0))


# ─────────────────────────────────────────────────────────────────────────────
# B10_PositivePrecisionHighlight — metric label morphs: ACCURACY → PRECISION
# ─────────────────────────────────────────────────────────────────────────────
class B10_PositivePrecisionHighlight(Scene):
    def construct(self):
        d = dur("B10")  # 16.64s

        eyebrow = caps("the metric that matters in rare-event domains", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Old metric: ACCURACY (greyed out, wrong)
        old_metric = serif("ACCURACY", sz=80, clr=MUTE)
        old_metric.move_to([0, 0.5, 0])
        old_note = caps("(misleading in rare-event domains)", sz=22, clr=MUTE).next_to(old_metric, DOWN, buff=0.25)
        old_bg = RoundedRectangle(corner_radius=0.12, width=5.5, height=1.6,
                                  fill_color=MUTE, fill_opacity=0.07,
                                  stroke_color=MUTE, stroke_width=1).move_to([0, 0.4, 0])
        old_bg._qc_intentional = True
        self.play(FadeIn(old_bg), run_time=0.2)
        self.play(FadeIn(old_metric, shift=UP * 0.1), FadeIn(old_note), run_time=0.6)
        self.wait(0.4)

        # Strike through accuracy
        strike = Line(old_metric.get_left() + LEFT * 0.1,
                      old_metric.get_right() + RIGHT * 0.1,
                      color=CRIMSON, stroke_width=7)
        strike._qc_intentional = True
        self.play(GrowFromPoint(strike, strike.get_left()), run_time=0.5)
        self.wait(0.3)

        # New metric: PRECISION (positive predictive value)
        new_metric = serif("PRECISION", sz=80, clr=TEAL)
        new_metric.move_to([0, -1.2, 0])
        formula = serif("true positives / all flagged positives", sz=34, clr=INK)
        formula.next_to(new_metric, DOWN, buff=0.3)

        self.play(FadeIn(new_metric, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(formula, shift=UP * 0.1), run_time=0.5)

        # Underline the question
        q = serif("What fraction of your positives pile is real?", sz=34, clr=INK)
        q.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


# ─────────────────────────────────────────────────────────────────────────────
# B11_BaseRateCheckFix — checklist: base rate question → precision math → false alarm count
# ─────────────────────────────────────────────────────────────────────────────
class B11_BaseRateCheckFix(Scene):
    def construct(self):
        d = dur("B11")  # 19.07s

        eyebrow = caps("the fix — ask before you build", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        items = [
            ("1.", "How rare is the positive class?", INK),
            ("2.", "What fraction of flagged cases will be real?", INK),
            ("3.", "99% accurate + 1-in-10K base rate", CRIMSON),
            ("4.", "= 99 false alarms per true hit", CRIMSON),
        ]

        checks = []
        for i, (num, text, clr) in enumerate(items):
            num_lbl = serif(num, sz=40, clr=MUTE)
            txt_lbl = serif(text, sz=40, clr=clr)
            row = VGroup(num_lbl, txt_lbl).arrange(RIGHT, buff=0.3)
            row.move_to([0, 1.5 - i * 0.95, 0])
            checks.append(row)

        for row in checks:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.5)
            self.wait(0.2)

        # Checkmark next to items 1 and 2
        for i in range(2):
            ck = Text("✓", font="Helvetica", font_size=40, color=TEAL)
            ck.next_to(checks[i], LEFT, buff=0.3)
            self.play(FadeIn(ck), run_time=0.3)

        # Final note
        note = serif("Know this before you promise anyone your model works.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.5))


# ─────────────────────────────────────────────────────────────────────────────
# B12_HospitalSepsisExample — hospital queue: 35 flags, 2 real + 33 false
# ─────────────────────────────────────────────────────────────────────────────
class B12_HospitalSepsisExample(Scene):
    def construct(self):
        d = dur("B12")  # 31.08s

        eyebrow = caps("hospital sepsis model — 98% accurate, 3/1,000 base rate", sz=22, clr=MUTE)
        eyebrow.to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Setup
        setup = VGroup(
            serif("35 flags per day", sz=44, clr=INK),
            serif("2 real sepsis + 33 false alarms", sz=44, clr=INK),
        ).arrange(DOWN, buff=0.35).move_to([0, 1.5, 0])
        self.play(FadeIn(setup[0], shift=UP * 0.1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(setup[1], shift=UP * 0.1), run_time=0.6)
        self.wait(0.4)

        # Flag queue: 35 rows, 2 teal at top, 33 crimson below
        queue_lbl = caps("NURSE ALERT QUEUE", sz=22, clr=MUTE).move_to([0, 0.2, 0])
        self.play(FadeIn(queue_lbl), run_time=0.3)

        bar_w, bar_h = 5.5, 0.07
        spacing = 0.10
        bars = []
        for i in range(35):
            color = TEAL if i < 2 else CRIMSON
            bar = Rectangle(width=bar_w, height=bar_h,
                            fill_color=color, fill_opacity=0.8, stroke_width=0)
            bar._qc_intentional = True
            bar.move_to([0, 0.1 - i * spacing, 0])
            bars.append(bar)

        # Show bars animating in quickly
        for bar in bars[:5]:
            self.play(FadeIn(bar, shift=RIGHT * 0.1), run_time=0.08)
        for bar in bars[5:]:
            self.add(bar)
        self.wait(0.3)

        # Nurses start ignoring bottom (grey out bottom half)
        fade_anims = [bar.animate.set_fill(opacity=0.25) for bar in bars[17:]]
        ignore_lbl = caps("nurses quietly deprioritize the bottom…", sz=20, clr=MUTE)
        ignore_lbl.to_edge(DOWN, buff=1.4)
        self.play(*fade_anims, FadeIn(ignore_lbl), run_time=1.0)
        self.wait(0.4)

        # The 2 real cases are in bottom half
        for bar in bars[18:20]:
            self.play(bar.animate.set_fill(TEAL, opacity=1.0), run_time=0.3)
        danger = serif("real sepsis cases — now in the deprioritized zone", sz=30, clr=CRIMSON)
        danger.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(danger, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 15.0))
