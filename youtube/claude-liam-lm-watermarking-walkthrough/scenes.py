"""scenes.py — claude-liam-lm-watermarking-walkthrough
Title: The Watermark Is One Line of Code
Render (from this folder):
  manim -qh --fps 24 -r 1920,1080 scenes.py B09_LocHotspot
  mv media/videos/scenes/1080p30/B09_LocHotspot.mp4 manim/B09.mp4
4K:
  manim -qk --fps 24 -r 3840,2160 scenes.py B09_LocHotspot
  mv media/videos/scenes/2160p24/B09_LocHotspot.mp4 manim/B09.mp4
"""
import json, pathlib, math, random
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

CREAM = "#F2F0E9"
INK   = "#3D3929"
ACCENT= "#D97757"   # terracotta — watermark_processor.py highlight, green-list items
RED   = "#A44A32"   # non-green (red-list) items
MUTE  = "#7A7265"
config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _bs["beats"]})
except Exception:
    pass

def dur(bid):
    return DUR.get(bid, 10.0)

def serif(t, sz=36, clr=INK, **k):
    return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)

def caps(t, sz=22, clr=MUTE, **k):
    return _Tx(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **k)

def mono(t, sz=28, clr=INK, **k):
    return _Tx(t, font="PT Mono", font_size=sz, color=clr, **k)

def hairline(x0, x1, y, clr=MUTE):
    return Line([x0, y, 0], [x1, y, 0], color=clr, stroke_width=1)


# ── B09 — LOC hotspot map ────────────────────────────────────────────────────
# Root: 2317 LOC across 7 files. Subdirs: 344,390 "lines of file" (not code).
# watermark_processor.py (282 lines = 12% of root) highlighted in ACCENT.

class B09_LocHotspot(Scene):
    def construct(self):
        d = dur("B09")

        ROOT_FILES = [
            ("extended_watermark_processor.py", 625),
            ("levenshtein.py",                  468),
            ("watermark_processor.py",          282),
            ("demo_watermark.py",               253),
            ("alternative_prf_schemes.py",      239),
            ("normalizers.py",                  235),
            ("compute_sensitivity.py",          215),
        ]
        ROOT_TOTAL  = 2317
        SUBDIR_TOTAL = 344390

        MAX_BAR = 7.0          # max bar width in Manim units (for extended_wm)
        BAR_H   = 0.38
        GAP     = 0.20
        LABEL_X = -4.2         # left edge of file name labels
        BAR_X0  = -1.6         # left edge of bars
        TOP_Y   = 2.8          # top of first bar

        title = caps("root files — lines of code", sz=20, clr=MUTE)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.3)

        bar_mobjects = []
        for i, (fname, loc) in enumerate(ROOT_FILES):
            y = TOP_Y - i * (BAR_H + GAP)
            color = ACCENT if fname == "watermark_processor.py" else INK
            alpha = 0.90 if fname == "watermark_processor.py" else 0.60
            w = (loc / max(f[1] for f in ROOT_FILES)) * MAX_BAR

            bar = Rectangle(width=w, height=BAR_H,
                             fill_color=color, fill_opacity=alpha, stroke_width=0)
            bar.move_to([BAR_X0 + w/2, y, 0])

            short = fname if len(fname) <= 30 else fname[:28] + "…"
            lbl = mono(short, sz=17, clr=INK)
            lbl.to_edge(LEFT, buff=0.9)   # buff ≥ 0.81 keeps left edge inside ±6.3 safe area
            lbl.set_y(y)

            cnt = mono(f"{loc:,}", sz=17, clr=INK)
            cnt.move_to([BAR_X0 + w + 0.22 + cnt.width/2, y, 0])

            self.play(
                FadeIn(lbl),
                GrowFromEdge(bar, LEFT),
                FadeIn(cnt),
                run_time=0.28,
            )
            bar_mobjects.append((bar, lbl, cnt, fname, w, y))

        # Annotate watermark_processor.py with pct-of-root
        wp_bar = bar_mobjects[2][0]
        brace = Brace(wp_bar, direction=UP, color=INK, buff=0.06)
        brace_lbl = serif("12% of root", sz=20, clr=INK)
        brace_lbl.next_to(brace, UP, buff=0.05)
        self.play(FadeIn(brace), FadeIn(brace_lbl), run_time=0.4)

        # Separator
        sep_y = TOP_Y - 7 * (BAR_H + GAP) - 0.05
        sep = hairline(-6.0, 6.0, sep_y, clr=MUTE)
        self.play(GrowFromPoint(sep, sep.get_left()), run_time=0.3)

        # Subdir mass — labels only (bar would be 148× wider than root; can't show at scale)
        sub_label_y = sep_y - 0.45
        sub_eyebrow = caps("subdirectories — lines of file, not code", sz=19, clr=MUTE)
        sub_eyebrow.move_to([0, sub_label_y, 0])
        self.play(FadeIn(sub_eyebrow), run_time=0.3)

        # Capped subdir bar (centered, stays within ±5.5 frame safe area)
        sub_bar_y = sub_label_y - 0.52
        sub_w = 11.0   # centered at 0: from -5.5 to +5.5
        sub_bar = Rectangle(width=sub_w, height=BAR_H,
                             fill_color=MUTE, fill_opacity=0.35, stroke_width=0)
        sub_bar.move_to([0, sub_bar_y, 0])

        # Scale break marker at right edge (within frame)
        brk_x = 5.5
        brk1 = Line([brk_x - 0.12, sub_bar_y + BAR_H/2 + 0.12, 0],
                    [brk_x + 0.12, sub_bar_y - BAR_H/2 - 0.12, 0], color=CREAM, stroke_width=3)
        brk2 = Line([brk_x + 0.06, sub_bar_y + BAR_H/2 + 0.12, 0],
                    [brk_x + 0.30, sub_bar_y - BAR_H/2 - 0.12, 0], color=CREAM, stroke_width=3)

        sub_cnt = mono("344,390", sz=19, clr=MUTE)
        sub_cnt.move_to([0, sub_bar_y, 0])   # label inside bar

        self.play(GrowFromEdge(sub_bar, LEFT), run_time=0.45)
        self.play(FadeIn(VGroup(brk1, brk2)), FadeIn(sub_cnt), run_time=0.3)

        # Bottom line: the idea is 282 lines
        foot = serif("The algorithm is 282 lines. Everything around it is apparatus.", sz=26, clr=INK)
        foot.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(foot, shift=UP * 0.08), run_time=0.5)

        anim_time = 0.3 + len(ROOT_FILES)*0.28 + 0.4 + 0.3 + 0.3 + 0.45 + 0.3 + 0.5
        self.wait(max(0.01, d - anim_time))


# ── B23 — Vocabulary partition ───────────────────────────────────────────────
# 10×10 grid of 100 dots (representing 50,257-token vocabulary, γ=0.5).
# Green (ACCENT) = green-list at this position. Red = not-green.
# At each of 6 token positions, the partition reshuffles completely.

class B23_VocabPartition(Scene):
    def construct(self):
        d = dur("B23")
        rng = random.Random(42)   # seeded: deterministic across same-frame-twice

        COLS, ROWS = 20, 10
        N = COLS * ROWS          # 200 dots
        GREEN = N // 2           # γ=0.5

        DOT_R = 0.13
        SPACING = 0.38
        GRID_W  = (COLS - 1) * SPACING
        GRID_H  = (ROWS - 1) * SPACING
        ORIGIN_X = -GRID_W / 2
        ORIGIN_Y =  GRID_H / 2 - 0.6

        POSITIONS = 6
        SEED_STATES = [list(range(N)) for _ in range(POSITIONS)]
        for s in SEED_STATES:
            rng.shuffle(s)

        def make_dots(green_indices):
            green_set = set(green_indices[:GREEN])
            dots = []
            for i in range(N):
                col = i % COLS
                row = i // COLS
                x = ORIGIN_X + col * SPACING
                y = ORIGIN_Y - row * SPACING
                color = ACCENT if i in green_set else RED
                alpha = 0.82 if i in green_set else 0.55
                d_ = Circle(radius=DOT_R, fill_color=color, fill_opacity=alpha,
                            stroke_width=0)
                d_.move_to([x, y, 0])
                dots.append(d_)
            return VGroup(*dots)

        title = caps("vocabulary · γ = 0.5 · position-dependent partition", sz=20, clr=MUTE)
        title.to_edge(UP, buff=0.65)   # buff≥0.65 keeps center within ±3.35 safe y
        self.play(FadeIn(title), run_time=0.3)

        # Legend — placed below title, not at bottom (avoids overlap with footer)
        leg_g = Circle(radius=0.10, fill_color=ACCENT, fill_opacity=0.85, stroke_width=0)
        leg_r = Circle(radius=0.10, fill_color=RED,    fill_opacity=0.60, stroke_width=0)
        leg_gl = serif("green list", sz=20, clr=ACCENT)
        leg_rl = serif("not green", sz=20, clr=RED)
        legend = VGroup(
            VGroup(leg_g, leg_gl).arrange(RIGHT, buff=0.12),
            VGroup(leg_r, leg_rl).arrange(RIGHT, buff=0.12),
        ).arrange(RIGHT, buff=0.5)
        legend.next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(legend), run_time=0.3)

        # Build annotation slot — positioned above the safe-area floor
        ann = serif("Position 1 · key × prev_token → RNG → partition", sz=24, clr=INK)
        ann.to_edge(DOWN, buff=0.9)    # center at y ≈ -3.1, within safe area
        self.play(FadeIn(ann), run_time=0.3)

        # Initial dots — Position 1
        dots = make_dots(SEED_STATES[0])
        self.play(LaggedStart(*[FadeIn(d_, shift=DOWN*0.04) for d_ in dots],
                              lag_ratio=0.008, run_time=1.2))

        hold_per = 0.7
        transition_per = 0.65

        for pos in range(1, POSITIONS):
            self.wait(hold_per)
            new_dots = make_dots(SEED_STATES[pos])
            new_ann = serif(f"Position {pos+1} · key × prev_token → RNG → partition",
                            sz=24, clr=INK)
            new_ann.to_edge(DOWN, buff=0.9)
            self.play(
                Transform(dots, new_dots),
                Transform(ann, new_ann),
                run_time=transition_per,
            )

        self.wait(hold_per)
        never = serif("Never stored. No green-list file anywhere in this repository.", sz=26, clr=INK)
        never.to_edge(DOWN, buff=0.9)    # same slot as ann — transform replaces it cleanly
        self.play(Transform(ann, never), run_time=0.5)

        anim_time = 0.3+0.3+0.3+1.2 + (POSITIONS-1)*(hold_per+transition_per) + hold_per + 0.5
        self.wait(max(0.01, d - anim_time))


# ── B27 — Logit bars: high entropy vs low entropy ───────────────────────────
# Left panel: 6 near-equal logit bars (high entropy). Apply +δ=2.0 to green
# bars → argmax flips. Right panel: 1 dominant bar (low entropy). Apply +δ →
# argmax unchanged. Teardown palette: green bars in ACCENT, others in INK/MUTE.

class B27_LogitBars(Scene):
    def construct(self):
        d = dur("B27")

        # ---------- geometry ----------
        PANEL_W  = 5.0
        BAR_W    = 0.48
        BAR_GAP  = 0.18
        BASELINE = -1.8
        MAX_H    = 3.2

        # ---------- data ----------
        # High entropy: 6 near-equal bars (logits before bias)
        HIGH_LOGITS = [2.1, 1.9, 2.3, 2.0, 1.8, 2.2]
        HIGH_GREEN  = {0, 2, 4}          # green-list indices

        # Low entropy: 1 dominant (Barack → Obama)
        LOW_LOGITS  = [5.8, 0.9, 1.1, 0.7, 1.0, 0.8]
        LOW_GREEN   = {0, 2, 5}

        DELTA = 2.0
        LOGIT_MAX = max(max(HIGH_LOGITS), max(LOW_LOGITS)) + DELTA + 0.3

        def px(logit):
            return (logit / LOGIT_MAX) * MAX_H

        def make_bars(logits, green_set, x_center, biased=False):
            n = len(logits)
            total_w = n * BAR_W + (n - 1) * BAR_GAP
            x0 = x_center - total_w / 2
            bars = []
            for i, lg in enumerate(logits):
                x = x0 + i * (BAR_W + BAR_GAP) + BAR_W/2
                h = px(lg)
                color = ACCENT if i in green_set else INK
                alpha = 0.85 if i in green_set else 0.55
                bar = Rectangle(width=BAR_W, height=h,
                                fill_color=color, fill_opacity=alpha, stroke_width=0)
                bar.move_to([x, BASELINE + h/2, 0])
                bars.append(bar)
            return bars

        # Panel centers
        L_X = -3.2
        R_X =  3.2

        # ---------- titles ----------
        l_title = caps("high entropy", sz=26, clr=MUTE).move_to([L_X, 2.9, 0])
        r_title = caps("low entropy", sz=26, clr=MUTE).move_to([R_X, 2.9, 0])
        self.play(FadeIn(l_title), FadeIn(r_title), run_time=0.4)

        # Baseline lines
        bl_l = hairline(L_X - PANEL_W/2, L_X + PANEL_W/2, BASELINE - 0.02)
        bl_r = hairline(R_X - PANEL_W/2, R_X + PANEL_W/2, BASELINE - 0.02)
        self.play(FadeIn(bl_l), FadeIn(bl_r), run_time=0.3)

        # ---------- LEFT panel — initial bars ----------
        l_bars = make_bars(HIGH_LOGITS, HIGH_GREEN, L_X)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in l_bars],
                              lag_ratio=0.1, run_time=0.8))

        # ---------- RIGHT panel — initial bars ----------
        r_bars = make_bars(LOW_LOGITS, LOW_GREEN, R_X)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in r_bars],
                              lag_ratio=0.1, run_time=0.6))

        self.wait(0.4)

        # ---------- Apply +δ to LEFT panel ----------
        delta_lbl = serif("+δ = 2.0", sz=26, clr=ACCENT).move_to([L_X, 2.3, 0])
        self.play(FadeIn(delta_lbl, shift=DOWN*0.08), run_time=0.35)

        HIGH_BIASED = [lg + DELTA if i in HIGH_GREEN else lg
                       for i, lg in enumerate(HIGH_LOGITS)]
        l_bars_new = make_bars(HIGH_BIASED, HIGH_GREEN, L_X, biased=True)

        # Find old and new argmax
        old_argmax_h = HIGH_LOGITS.index(max(HIGH_LOGITS))
        new_argmax_h = HIGH_BIASED.index(max(HIGH_BIASED))

        self.play(*[Transform(l_bars[i], l_bars_new[i]) for i in range(len(l_bars))],
                  run_time=0.8)

        if old_argmax_h != new_argmax_h:
            flip_lbl = serif("choice flips", sz=22, clr=ACCENT)
            flip_lbl.move_to([L_X, BASELINE - 0.45, 0])
            arr = Arrow([L_X, BASELINE - 0.25, 0],
                        [L_X + (new_argmax_h - old_argmax_h) * (BAR_W + BAR_GAP) * 0.7, BASELINE - 0.25, 0],
                        color=ACCENT, stroke_width=3, max_tip_length_to_length_ratio=0.25)
            self.play(FadeIn(flip_lbl), GrowArrow(arr), run_time=0.45)

        # ---------- Apply +δ to RIGHT panel ----------
        delta_lbl_r = serif("+δ = 2.0", sz=26, clr=ACCENT).move_to([R_X, 2.3, 0])
        self.play(FadeIn(delta_lbl_r, shift=DOWN*0.08), run_time=0.35)

        LOW_BIASED = [lg + DELTA if i in LOW_GREEN else lg
                      for i, lg in enumerate(LOW_LOGITS)]
        r_bars_new = make_bars(LOW_BIASED, LOW_GREEN, R_X, biased=True)

        self.play(*[Transform(r_bars[i], r_bars_new[i]) for i in range(len(r_bars))],
                  run_time=0.8)

        old_argmax_l = LOW_LOGITS.index(max(LOW_LOGITS))
        new_argmax_l = LOW_BIASED.index(max(LOW_BIASED))
        if old_argmax_l == new_argmax_l:
            hold_lbl = serif("Barack → Obama\nargmax unchanged", sz=24, clr=INK)
            hold_lbl.move_to([R_X, BASELINE - 0.55, 0])
            self.play(FadeIn(hold_lbl), run_time=0.4)

        # Bottom note
        note = serif("The watermark is invisible at low entropy. It only bites when there is a real choice.", sz=24, clr=INK)
        note.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(note, shift=UP*0.06), run_time=0.5)

        anim_time = 0.4+0.3+0.8+0.6+0.4+0.35+0.8+0.45+0.35+0.8+0.4+0.5
        self.wait(max(0.01, d - anim_time))


# ── B31 — Binomial null vs observed ─────────────────────────────────────────
# Left: T=200, narrow distribution, observed count > z_threshold → DETECTED
# Right: T=40, wide distribution, same fraction, z < z_threshold → INSUFFICIENT POWER
# z_threshold=4.0 (verified at watermark_processor.py L125), γ=0.5 (L37)

class B31_BinomialNull(Scene):
    def construct(self):
        d = dur("B31")

        # Parameters
        GAMMA = 0.5
        Z_THRESHOLD = 4.0

        # T=200 scenario
        T_L = 200
        MEAN_L = GAMMA * T_L                          # 100
        STD_L  = math.sqrt(T_L * GAMMA * (1 - GAMMA)) # ≈7.07
        OBS_L  = 130                                   # observed green count
        Z_L    = (OBS_L - MEAN_L) / STD_L             # ≈4.24 > 4.0

        # T=40 scenario — same green fraction (130/200 = 0.65 → 26/40)
        T_R = 40
        MEAN_R = GAMMA * T_R
        STD_R  = math.sqrt(T_R * GAMMA * (1 - GAMMA))
        OBS_R  = round(0.65 * T_R)                    # 26
        Z_R    = (OBS_R - MEAN_R) / STD_R             # ≈1.90 < 4.0

        # ---------- layout ----------
        L_X = -3.5
        R_X =  3.5
        BASELINE = -1.5
        MAX_H    = 3.0
        SIGMA_RANGE = 5.0   # draw ±5σ

        def gaussian_curve(mu, sigma, x_center, scale_x=0.3, scale_y=1.0):
            def curve_func(t):
                x = mu + t * sigma * SIGMA_RANGE / 5.0
                y = math.exp(-0.5 * ((t * SIGMA_RANGE / 5.0) ** 2)) / (math.sqrt(2 * math.pi))
                return [x_center + (x - mu) * scale_x, BASELINE + y * scale_y, 0]
            return ParametricFunction(curve_func, t_range=[-5, 5, 0.05],
                                      color=INK, stroke_width=2.5)

        # Scale so the parametric curve peak reaches 80% of MAX_H.
        # The parametric function y = exp(-0.5*t²)/√(2π) peaks at 1/√(2π) ≈ 0.399,
        # independent of σ.  (Previous code divided by the TRUE density peak 1/(σ√2π),
        # over-inflating SCALE_Y by a factor of STD_L ≈ 7 and sending curves off-screen.)
        PEAK_PARAM = 1.0 / math.sqrt(2 * math.pi)   # peak of the parametric y value
        SCALE_Y = 0.80 * MAX_H / PEAK_PARAM          # ≈ 6.0  (was ≈ 42, far off-screen)

        # For T=200, scale_x so ±5σ stays within panel (panel half-width ~2.5u):
        SCALE_X_L = 2.0 / (SIGMA_RANGE * STD_L)
        # For T=40, same x-scale so the wider distribution is visually wider
        SCALE_X_R = SCALE_X_L

        # ---------- titles — shifted off the mean-line x to avoid label-on-line audit error ----------
        l_title = serif("T = 200 tokens", sz=22, clr=MUTE).move_to([L_X - 1.4, 2.9, 0])
        r_title = serif("T = 40 tokens",  sz=22, clr=MUTE).move_to([R_X + 1.4, 2.9, 0])
        self.play(FadeIn(l_title), FadeIn(r_title), run_time=0.3)

        bl_l = hairline(L_X - 2.8, L_X + 2.8, BASELINE - 0.02)
        bl_r = hairline(R_X - 2.8, R_X + 2.8, BASELINE - 0.02)
        self.play(FadeIn(bl_l), FadeIn(bl_r), run_time=0.3)

        # ---------- LEFT curve (narrow) ----------
        l_curve = gaussian_curve(MEAN_L, STD_L, L_X, scale_x=SCALE_X_L, scale_y=SCALE_Y)
        self.play(Create(l_curve), run_time=0.8)

        # NULL mean marker
        l_mean_line = DashedLine([L_X, BASELINE, 0], [L_X, BASELINE + 0.80*MAX_H, 0],
                                 color=MUTE, stroke_width=1.5, dash_length=0.12)
        l_mean_lbl = mono(f"γT={int(MEAN_L)}", sz=18, clr=MUTE)
        l_mean_lbl.next_to(l_mean_line, DOWN, buff=0.08)
        self.play(FadeIn(l_mean_line), FadeIn(l_mean_lbl), run_time=0.3)

        # Observed marker
        l_obs_x = L_X + (OBS_L - MEAN_L) * SCALE_X_L
        l_obs_h = math.exp(-0.5*((OBS_L-MEAN_L)/STD_L)**2)/(STD_L*math.sqrt(2*math.pi)) * SCALE_Y
        l_obs_line = Line([l_obs_x, BASELINE, 0], [l_obs_x, BASELINE + l_obs_h + 0.2, 0],
                          color=ACCENT, stroke_width=2.5)
        l_obs_dot = Dot([l_obs_x, BASELINE + l_obs_h + 0.2, 0], color=ACCENT, radius=0.09)
        l_obs_lbl = mono(f"obs={OBS_L}", sz=18, clr=ACCENT)
        l_obs_lbl.next_to(l_obs_dot, RIGHT, buff=0.15)   # RIGHT avoids overlap with vertical obs line
        self.play(FadeIn(l_obs_line), FadeIn(l_obs_dot), FadeIn(l_obs_lbl), run_time=0.4)

        # z-score annotation
        l_z_lbl = serif(f"z = {Z_L:.2f}", sz=22, clr=ACCENT)
        l_z_lbl.move_to([L_X + 1.3, 1.0, 0])
        self.play(FadeIn(l_z_lbl), run_time=0.3)

        # z_threshold dashed line
        l_thr_x = L_X + Z_THRESHOLD * STD_L * SCALE_X_L
        l_thr_line = DashedLine([l_thr_x, BASELINE, 0], [l_thr_x, BASELINE + MAX_H*0.5, 0],
                                 color=RED, stroke_width=1.5, dash_length=0.10)
        l_thr_lbl = mono(f"z={Z_THRESHOLD:.0f}", sz=16, clr=RED)
        l_thr_lbl.next_to(l_thr_line, UP, buff=0.06)
        self.play(FadeIn(l_thr_line), FadeIn(l_thr_lbl), run_time=0.3)

        detect_lbl = serif("DETECTED", sz=26, clr=ACCENT)
        detect_lbl.move_to([L_X, BASELINE - 0.52, 0])
        self.play(FadeIn(detect_lbl), run_time=0.3)

        # ---------- RIGHT curve (wide) ----------
        r_curve = gaussian_curve(MEAN_R, STD_R, R_X, scale_x=SCALE_X_R, scale_y=SCALE_Y)
        self.play(Create(r_curve), run_time=0.8)

        r_mean_line = DashedLine([R_X, BASELINE, 0], [R_X, BASELINE + 0.30*MAX_H, 0],
                                 color=MUTE, stroke_width=1.5, dash_length=0.12)
        r_mean_lbl = mono(f"γT={int(MEAN_R)}", sz=18, clr=MUTE)
        r_mean_lbl.next_to(r_mean_line, DOWN, buff=0.08)
        self.play(FadeIn(r_mean_line), FadeIn(r_mean_lbl), run_time=0.3)

        r_obs_x = R_X + (OBS_R - MEAN_R) * SCALE_X_R
        r_obs_h = math.exp(-0.5*((OBS_R-MEAN_R)/STD_R)**2)/(STD_R*math.sqrt(2*math.pi)) * SCALE_Y
        r_obs_line = Line([r_obs_x, BASELINE, 0], [r_obs_x, BASELINE + r_obs_h + 0.2, 0],
                          color=MUTE, stroke_width=2.5)
        r_obs_dot = Dot([r_obs_x, BASELINE + r_obs_h + 0.2, 0], color=MUTE, radius=0.09)
        r_obs_lbl = mono(f"obs={OBS_R}", sz=18, clr=MUTE)
        r_obs_lbl.next_to(r_obs_dot, RIGHT, buff=0.15)   # RIGHT avoids overlap with vertical obs line
        self.play(FadeIn(r_obs_line), FadeIn(r_obs_dot), FadeIn(r_obs_lbl), run_time=0.4)

        r_z_lbl = serif(f"z = {Z_R:.2f}", sz=22, clr=MUTE)
        r_z_lbl.move_to([R_X + 1.3, 1.0, 0])
        self.play(FadeIn(r_z_lbl), run_time=0.3)

        r_thr_x = R_X + Z_THRESHOLD * STD_R * SCALE_X_R
        r_thr_line = DashedLine([r_thr_x, BASELINE, 0], [r_thr_x, BASELINE + MAX_H*0.5, 0],
                                 color=RED, stroke_width=1.5, dash_length=0.10)
        r_thr_lbl = mono(f"z={Z_THRESHOLD:.0f}", sz=16, clr=RED)
        r_thr_lbl.next_to(r_thr_line, UP, buff=0.06)
        self.play(FadeIn(r_thr_line), FadeIn(r_thr_lbl), run_time=0.3)

        no_detect = serif("INSUFFICIENT POWER", sz=22, clr=MUTE)
        no_detect.move_to([R_X, BASELINE - 0.52, 0])
        self.play(FadeIn(no_detect), run_time=0.3)

        # Bottom note
        note = serif("Detection returns a p-value. A p-value is not a ruling.", sz=26, clr=INK)
        note.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(note, shift=UP*0.06), run_time=0.5)

        anim_time = 0.3+0.3+0.8+0.3+0.4+0.3+0.3+0.3+0.8+0.3+0.4+0.3+0.3+0.3+0.5
        self.wait(max(0.01, d - anim_time))
