"""scenes.py — claude-liam-watermarks-remover
Title: Four Days, No Dependencies
Rung 1 data: all numbers from REPO-VERIFY.md (books/github/watermarks-remover HEAD 256d90d)

Render (from this folder):
  manim -qh --fps 24 -r 1920,1080 scenes.py B07_LOCHotspot
  mv media/videos/scenes/1080p24/B07_LOCHotspot.mp4 manim/B07.mp4
4K:
  manim -qk --fps 24 -r 3840,2160 scenes.py B07_LOCHotspot
  mv media/videos/scenes/2160p24/B07_LOCHotspot.mp4 manim/B07.mp4
"""
import json, pathlib
import numpy as np
from manim import *

# ── teardown palette (runtime/design/DESIGN.md, _PALETTES["teardown"]) ───────
GROUND  = "#FFFFFF"
INK     = "#2A1A0E"
CRIMSON = "#C8102E"
SLATE   = "#545454"

DISPLAY = "Montserrat"
SERIF   = "EB Garamond"

config.background_color = GROUND

# ── duration table — loaded from beat_sheet.json ──────────────────────────────
DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
        for b in _bs["beats"]
    })
except Exception:
    pass

def dur(bid):
    return DUR.get(bid, 10.0)


# ── B07 — Scripts by LOC — horizontal bar chart ───────────────────────────────
# Source: wc -l skills/remove-ai-marks/scripts/*.py | sort -rn (REPO-VERIFY.md Scene 2)
# top-5 by LOC; common.py annotated as "imported by 13 of 16"
class B07_LOCHotspot(Scene):
    DATA = [
        ("container_meta.py",  855, True),
        ("image_meta.py",      668, False),
        ("text_unicode.py",    449, False),
        ("rewrite_text.py",    436, False),
        ("common.py",          428, False),
    ]
    MAX_LOC   = 855
    BAR_MAX_W = 5.2

    def construct(self):
        d = dur("B07")

        title = Text("Scripts by LOC", font=DISPLAY, color=INK, font_size=44, weight="BOLD")
        title.to_edge(UP, buff=0.70)

        # Build full-width bars; VGroup row per script; stack rows vertically.
        # GrowFromEdge(bar, LEFT) reveals without needing an animate chain.
        rows     = VGroup()
        bar_mobs = []
        val_mobs = []

        for name, loc, hi in self.DATA:
            name_lbl = Text(name, font="PT Mono", color=INK if hi else SLATE, font_size=28)
            bar_w    = (loc / self.MAX_LOC) * self.BAR_MAX_W
            bar      = Rectangle(width=bar_w, height=0.42,
                                 fill_color=INK if hi else SLATE,
                                 fill_opacity=1, stroke_width=0)
            val_lbl  = Text(str(loc), font=DISPLAY, color=INK if hi else SLATE, font_size=28)
            row = VGroup(name_lbl, bar, val_lbl)
            row.arrange(RIGHT, buff=0.30, aligned_edge=DOWN)
            rows.add(row)
            bar_mobs.append(bar)
            val_mobs.append(val_lbl)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.40)
        rows.move_to(ORIGIN + DOWN * 0.15)

        # "imported by 13 of 16" annotation on the last bar (common.py)
        note = Text("imported by 13 of 16", font=SERIF, color=SLATE, font_size=24)
        note.next_to(rows[-1], RIGHT, buff=0.40)

        # Animate
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.7)
        self.wait(0.3)
        for idx, (row, bar, val_lbl) in enumerate(zip(rows, bar_mobs, val_mobs)):
            name_lbl = row[0]
            self.play(FadeIn(name_lbl, shift=RIGHT * 0.1), run_time=0.45)
            self.play(GrowFromEdge(bar, LEFT), run_time=0.65)
            self.play(FadeIn(val_lbl), run_time=0.30)
            if idx == len(self.DATA) - 1:
                self.play(FadeIn(note, shift=LEFT * 0.1), run_time=0.40)

        anim_s = 0.7 + 0.3 + len(self.DATA) * (0.45 + 0.65 + 0.30) + 0.40
        self.wait(max(0.01, d - anim_s))


# ── B12 — Imported-by counts — vertical bar chart ────────────────────────────
# Source: grep -rhE '^(import|from) ' skills --include='*.py' (REPO-VERIFY.md Scene 3)
# common.py imported by 13 scripts; text_unicode / image_meta by 6 each; etc.
class B12_ImportFan(Scene):
    # (name, count, highlight, short_label)
    DATA = [
        ("common.py",      13, True,  "common"),
        ("text_unicode",    6, False, "txt_uni"),
        ("image_meta",      6, False, "img_meta"),
        ("container_meta",  3, False, "cntr_meta"),
        ("audit_lib",       2, False, "audit_lib"),
        ("inspect_file",    1, False, "insp_file"),
    ]
    MAX_COUNT = 13
    BAR_MAX_H = 3.8

    def construct(self):
        d = dur("B12")

        title = Text("Imported by (scripts)", font=DISPLAY, color=INK,
                     font_size=44, weight="BOLD")
        title.to_edge(UP, buff=0.70)

        BAR_W    = 1.05
        GAP      = 0.32
        n        = len(self.DATA)
        total_w  = n * BAR_W + (n - 1) * GAP
        baseline = DOWN * (self.BAR_MAX_H / 2 + 0.20)   # shared baseline for all bars

        bar_mobs = VGroup()
        cnt_mobs = VGroup()
        lbl_mobs = VGroup()

        for idx, (name, count, hi, short) in enumerate(self.DATA):
            x_off = RIGHT * (-total_w / 2 + idx * (BAR_W + GAP) + BAR_W / 2)
            bar_h = (count / self.MAX_COUNT) * self.BAR_MAX_H

            # Bar: bottom sits on the baseline; center is baseline_y + bar_h/2
            bar = Rectangle(width=BAR_W, height=bar_h,
                            fill_color=INK if hi else SLATE,
                            fill_opacity=1, stroke_width=0)
            bar.next_to(baseline + x_off, UP, buff=0)

            cnt = Text(str(count), font=DISPLAY, color=INK if hi else SLATE,
                       font_size=30, weight="BOLD" if hi else "NORMAL")
            cnt.next_to(bar, UP, buff=0.12)

            lbl = Text(short, font="PT Mono", color=INK if hi else SLATE, font_size=18)
            lbl.next_to(bar, DOWN, buff=0.18)

            bar_mobs.add(bar)
            cnt_mobs.add(cnt)
            lbl_mobs.add(lbl)

        # Animate
        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.6)
        self.wait(0.2)
        for bar, cnt, lbl in zip(bar_mobs, cnt_mobs, lbl_mobs):
            self.play(
                GrowFromEdge(bar, DOWN),
                FadeIn(lbl, shift=UP * 0.1),
                run_time=0.6,
            )
            self.play(FadeIn(cnt), run_time=0.25)

        anim_s = 0.6 + 0.2 + n * (0.6 + 0.25)
        self.wait(max(0.01, d - anim_s))


# ── B17 — Cumulative commits step-line chart ──────────────────────────────────
# Source: git log --date=format:'%m-%d' --pretty=%ad | sort | uniq -c (REPO-VERIFY.md Scene 4)
# v0.4.0 verified at 2026-08-13 via git for-each-ref. HEAD 256d90d = 2026-08-14.
class B17_FourDayChurn(Scene):
    DAYS = [
        ("Aug 11", 11,  "day 1",   False),
        ("Aug 12", 31,  "day 2",   True),    # peak slope
        ("Aug 13", 48,  "v0.4.0",  True),    # tag created 2026-08-13
        ("Aug 14", 49,  "HEAD",    False),   # 256d90d — one commit after tag
    ]
    MAX_COMMITS = 49
    CHART_W = 8.5
    CHART_H = 3.5

    def construct(self):
        d = dur("B17")

        title = Text("Cumulative commits", font=DISPLAY, color=INK,
                     font_size=40, weight="BOLD")
        title.to_edge(UP, buff=0.70)

        origin = DOWN * 2.0 + LEFT * 3.8
        x_axis = Arrow(origin, origin + RIGHT * (self.CHART_W + 0.3),
                       stroke_width=2, color=INK, buff=0)
        y_axis = Arrow(origin, origin + UP * (self.CHART_H + 0.3),
                       stroke_width=2, color=INK, buff=0)

        day_xs = [
            origin[0] + (i + 1) * self.CHART_W / (len(self.DAYS) + 0.5)
            for i in range(len(self.DAYS))
        ]

        def y_for(commits):
            return origin[1] + (commits / self.MAX_COMMITS) * self.CHART_H

        # Y-axis tick marks
        y_tick_mobs = VGroup()
        for commits, label in [(0, "0"), (11, "11"), (31, "31"), (49, "49")]:
            y = y_for(commits)
            tick = Line(origin + LEFT * 0.15 + UP * (y - origin[1]),
                        origin + RIGHT * 0.15 + UP * (y - origin[1]),
                        stroke_width=1.5, color=SLATE)
            t = Text(label, font="PT Mono", color=SLATE, font_size=22)
            t.next_to(tick.get_left(), LEFT, buff=0.12)
            y_tick_mobs.add(VGroup(tick, t))

        # X-axis day labels
        x_tick_mobs = VGroup()
        for i, (day_name, _, _, _) in enumerate(self.DAYS):
            x = day_xs[i]
            tick_pos = np.array([x, origin[1], 0])
            tick = Line(tick_pos + DOWN * 0.15, tick_pos + UP * 0.15,
                        stroke_width=1.5, color=SLATE)
            t = Text(day_name, font="PT Mono", color=SLATE, font_size=22)
            t.next_to(tick, DOWN, buff=0.15)
            x_tick_mobs.add(VGroup(tick, t))

        # Step-line dots and annotations
        plot_points = []
        value_mobs  = VGroup()
        ann_mobs    = VGroup()
        for i, (day_name, cum, annotation, is_peak) in enumerate(self.DAYS):
            x = day_xs[i]
            y = y_for(cum)
            dot = Dot(np.array([x, y, 0]), radius=0.11, color=INK)

            val_lbl = Text(str(cum), font=DISPLAY, color=INK,
                           font_size=26, weight="BOLD" if is_peak else "NORMAL")
            val_lbl.next_to(dot, UR, buff=0.12)

            ann_color = CRIMSON if annotation == "v0.4.0" else SLATE
            ann_lbl = Text(annotation, font=SERIF, color=ann_color, font_size=24)
            ann_lbl.next_to(dot, UP, buff=0.30)

            plot_points.append((dot, val_lbl, ann_lbl, x, y))
            value_mobs.add(val_lbl)
            ann_mobs.add(ann_lbl)

        # Step-line segments (horizontal → vertical for each day transition)
        segments = []
        for i in range(1, len(plot_points)):
            _, _, _, x0, y0 = plot_points[i - 1]
            _, _, _, x1, y1 = plot_points[i]
            horiz = Line(np.array([x0, y0, 0]), np.array([x1, y0, 0]),
                         stroke_width=2.5, color=SLATE)
            vert  = Line(np.array([x1, y0, 0]), np.array([x1, y1, 0]),
                         stroke_width=2.5, color=INK)
            segments.append((horiz, vert))

        # Origin point and first horizontal segment (day 0 → Aug 11)
        start_x   = origin[0] + 0.5 * self.CHART_W / (len(self.DAYS) + 0.5)
        start_dot = Dot(np.array([start_x, origin[1], 0]), radius=0.08, color=SLATE)
        start_seg = Line(np.array([start_x, origin[1], 0]),
                         np.array([day_xs[0], origin[1], 0]),
                         stroke_width=2.5, color=SLATE)

        # Animate
        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.6)
        self.play(Create(x_axis), Create(y_axis), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(m) for m in y_tick_mobs], lag_ratio=0.12, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(m) for m in x_tick_mobs], lag_ratio=0.12, run_time=0.8))
        self.play(FadeIn(start_dot), Create(start_seg), run_time=0.5)

        for i, (dot, val_lbl, ann_lbl, _, _) in enumerate(plot_points):
            if i < len(segments):
                h, v = segments[i]
                self.play(Create(h), run_time=0.4)
                self.play(Create(v), FadeIn(dot, scale=1.3), run_time=0.5)
            else:
                self.play(FadeIn(dot, scale=1.3), run_time=0.4)
            self.play(FadeIn(val_lbl), FadeIn(ann_lbl), run_time=0.35)

        anim_s = 0.6 + 0.7 + 0.8 + 0.8 + 0.5 + len(self.DAYS) * (0.4 + 0.5 + 0.35)
        self.wait(max(0.01, d - anim_s))


# ── B33 — Dependency count — stdlib imports by category ──────────────────────
# Source: grep -rhE '^(import|from) ' skills --include='*.py' | awk '{print $2}' | sort -u
# requirements-dev.txt: pytest==9.1.1 + pip-audit==2.10.1 only. Core = zero third-party.
class B33_DependencyCount(Scene):
    CATEGORIES = [
        ("text / string",  ["re", "unicodedata"]),
        ("file / I-O",     ["pathlib", "io", "os", "gzip", "json", "zipfile", "zlib", "xml.etree"]),
        ("process",        ["subprocess", "sys", "argparse", "urllib"]),
        ("data",           ["collections", "dataclasses", "struct", "typing"]),
    ]

    def construct(self):
        d = dur("B33")

        title = Text("stdlib imports — all 16 scripts", font=DISPLAY, color=INK,
                     font_size=42, weight="BOLD")
        title.to_edge(UP, buff=0.70)

        footer_line1 = Text(
            "zero third-party packages in the core",
            font=SERIF, color=SLATE, font_size=24,
        )
        footer_line2 = Text(
            "no model · no GPU · no pip install",
            font=SERIF, color=SLATE, font_size=24,
        )
        footer = VGroup(footer_line1, footer_line2).arrange(DOWN, buff=0.12)
        footer.to_edge(DOWN, buff=0.72)

        category_groups = VGroup()
        for cat_name, modules in self.CATEGORIES:
            cat_lbl = Text(cat_name, font=DISPLAY, color=INK, font_size=30, weight="BOLD")
            pills = VGroup()
            for mod in modules:
                pill_text = Text(mod, font="PT Mono", color=INK, font_size=24)
                pill_bg   = SurroundingRectangle(
                    pill_text, buff=0.12,
                    fill_color=GROUND, fill_opacity=1,
                    stroke_color=SLATE, stroke_width=1.5,
                    corner_radius=0.12,
                )
                pills.add(VGroup(pill_bg, pill_text))
            pills.arrange(RIGHT, buff=0.16)
            row = VGroup(cat_lbl, pills)
            row.arrange(RIGHT, aligned_edge=UP, buff=0.40)
            category_groups.add(row)

        category_groups.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        category_groups.move_to(ORIGIN + DOWN * 0.15)

        # Animate
        self.play(FadeIn(title, shift=DOWN * 0.12), run_time=0.6)
        self.wait(0.2)
        for group in category_groups:
            cat_lbl, pills_grp = group[0], group[1]
            self.play(FadeIn(cat_lbl, shift=RIGHT * 0.12), run_time=0.4)
            self.play(
                LaggedStart(*[FadeIn(p, shift=UP * 0.08) for p in pills_grp],
                            lag_ratio=0.10, run_time=0.65),
            )
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)

        anim_s = 0.6 + 0.2 + len(self.CATEGORIES) * (0.4 + 0.65) + 0.5
        self.wait(max(0.01, d - anim_s))
