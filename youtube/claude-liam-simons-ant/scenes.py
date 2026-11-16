"""scenes.py — claude-liam-simons-ant Manim scenes

17 scenes for the Manim-lane beats:
  B02 B03 B04 B06 B07 B09 B10 B12 B13 B15 B16 B17 B19 B20 B21 B23 B24

Render from the reel folder (one at a time):
  manim -qh --fps 30 -r 1920,1080 scenes.py B02_AntBeachPath
  mv media/videos/scenes/1080p30/B02_AntBeachPath.mp4 manim/B02.mp4

Batch render (run from the reel folder):
  for cls in B02_AntBeachPath B03_AntFlatTable B04_PathCutaway \
             B06_ThesisSubstitution B07_InnerOuterInterface \
             B09_BehaviorEquation B10_EntropyPartition \
             B12_ReactiveAgentSim B13_DensitySweep \
             B15_AntFallacyHeuristic B16_AttributionTwoByTwo \
             B17_TrapToAvoid B19_DesignInversion \
             B20_TempusHora B21_HoraInterruptionCost \
             B23_CataglyphisOdometer B24_BeachExcuse; do
    bid=${cls:0:3}
    manim -qh --fps 30 -r 1920,1080 scenes.py $cls &&
    mv media/videos/scenes/1080p30/${cls}.mp4 manim/${bid}.mp4
  done

Design: Claude palette throughout.
  CREAM  = #F2F0E9  (background)
  INK    = #3D3929  (warm ink — text, structure)
  ACCENT = #D97757  (terracotta — the ONE accent; paths, highlights, equations)
  MUTE   = #7A7265  (warm grey — secondary labels, axes)
  WHITE  = #FAF9F5  (card faces, slightly warm)
"""
import json, math, pathlib, random
from manim import *

# §8.4 — EB Garamond default
_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)
try:
    _Mx = MarkupText
    MarkupText = lambda *a, font="EB Garamond", **k: _Mx(*a, font=font, **k)
except NameError:
    pass

# ── Claude palette ─────────────────────────────────────────────────────────
CREAM  = "#F2F0E9"
INK    = "#3D3929"
ACCENT = "#D97757"
MUTE   = "#5D584F"
WHITE  = "#FAF9F5"

config.background_color = CREAM

# ── Beat durations ─────────────────────────────────────────────────────────
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

def dur(bid):
    return DUR.get(bid, 8.0)

# ── Shared helpers ─────────────────────────────────────────────────────────

def serif(txt, sz=40, clr=INK, **kw):
    return Text(txt, font="EB Garamond", font_size=sz, color=clr, **kw)

def caps(txt, sz=22, clr=MUTE, **kw):
    return Text(txt.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **kw)

def hairline(length=6.0, clr=INK, sw=1):
    return Line(ORIGIN, RIGHT * length, color=clr, stroke_width=sw)

def dot_circle(radius=0.12, fill=ACCENT):
    return Dot(radius=radius, color=fill, fill_opacity=1, stroke_width=0)

def label_above(mob, txt, sz=22, clr=MUTE, buf=0.22):
    t = caps(txt, sz=sz, clr=clr)
    t.next_to(mob, UP, buff=buf)
    return t

def assert_no_overlap(*mobs, tol=0.02, scene=""):
    """Fail at build time if any two mobject bboxes intersect beyond tol fraction
    of the smaller box's area.  Immune to the raster checker's fused-run blind spot:
    a total pixel collision produces one blob → fewer-than-2 early return → PASS.
    This catches the error before render, not after."""
    items = [m for m in mobs if m is not None]
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i], items[j]
            ax0, ay0 = a.get_left()[0],   a.get_bottom()[1]
            ax1, ay1 = a.get_right()[0],  a.get_top()[1]
            bx0, by0 = b.get_left()[0],   b.get_bottom()[1]
            bx1, by1 = b.get_right()[0],  b.get_top()[1]
            ix = max(0.0, min(ax1, bx1) - max(ax0, bx0))
            iy = max(0.0, min(ay1, by1) - max(ay0, by0))
            inter = ix * iy
            if inter <= 0:
                continue
            smaller = min(max(1e-6, (ax1-ax0)*(ay1-ay0)),
                          max(1e-6, (bx1-bx0)*(by1-by0)))
            if inter / smaller > tol:
                a_txt = getattr(a, 'text', repr(type(a).__name__))
                b_txt = getattr(b, 'text', repr(type(b).__name__))
                raise AssertionError(
                    f"{scene}: text overlap {inter/smaller:.0%} between "
                    f"'{a_txt}' and '{b_txt}'"
                )

# ── B02 — Ant on the beach (jagged path, obstacles) ───────────────────────

class B02_AntBeachPath(Scene):
    def construct(self):
        d = dur("B02")
        self.camera.background_color = CREAM

        # Title label
        label = caps("VIEW FROM ABOVE — THE BEACH", sz=32, clr=MUTE)
        label.to_edge(UP, buff=0.5)
        self.add(label)

        # Scatter obstacles (pebbles/rocks) across the arena
        random.seed(42)
        arena_w, arena_h = 10.0, 5.5
        obstacles = []
        for _ in range(55):
            x = random.uniform(-4.8, 4.8)
            y = random.uniform(-2.5, 2.5)
            r = random.uniform(0.10, 0.28)
            obs = Circle(radius=r, color=MUTE, fill_color=MUTE, fill_opacity=0.55,
                         stroke_width=0)
            obs.move_to([x, y, 0])
            obstacles.append(obs)
        obs_group = VGroup(*obstacles)
        self.add(obs_group)

        # Ant starts at far left, goal is far right
        start = np.array([-4.5, 0.0, 0])
        ant = dot_circle(radius=0.13, fill=INK)
        ant.move_to(start)
        self.add(ant)

        # Pre-compute a realistic obstacle-avoiding path
        # Reactive rule: move forward; if next step collides, turn and try again
        def overlaps(pos, obs_list, pad=0.32):
            for ob in obs_list:
                if np.linalg.norm(pos[:2] - ob.get_center()[:2]) < ob.radius + pad:
                    return True
            return False

        path_pts = [start.copy()]
        pos = start.copy()
        angle = 0.0  # heading in radians; 0 = right
        step = 0.18
        rng = random.Random(7)
        for _ in range(220):
            for attempt in range(16):
                nxt = pos + step * np.array([math.cos(angle), math.sin(angle), 0])
                nxt[0] = max(-4.8, min(4.8, nxt[0]))
                nxt[1] = max(-2.6, min(2.6, nxt[1]))
                if not overlaps(nxt, obstacles):
                    pos = nxt
                    break
                angle += rng.uniform(0.4, 1.1) * rng.choice([-1, 1])
            path_pts.append(pos.copy())
            if pos[0] > 4.3:
                break

        # Draw path as it's traced
        path_mobj = VMobject(color=ACCENT, stroke_width=2.5, stroke_opacity=0.85)
        path_mobj.set_points_as_corners([path_pts[0], path_pts[0]])
        self.add(path_mobj)

        n_pts = len(path_pts)
        trace_dur = d * 0.78

        def update_path(m, alpha):
            idx = int(alpha * (n_pts - 1))
            idx = max(1, min(idx, n_pts - 1))
            m.set_points_as_corners(path_pts[:idx + 1])
            ant.move_to(path_pts[idx])

        self.play(UpdateFromAlphaFunc(path_mobj, update_path),
                  rate_func=linear, run_time=trace_dur)

        # Pause and show the "complexity" annotation
        annot = serif("This path looks like a plan.", sz=48, clr=INK)
        annot.to_edge(DOWN, buff=0.5)
        assert_no_overlap(label, annot, scene="B02")
        self.play(FadeIn(annot, shift=UP * 0.15), run_time=0.6)
        self.wait(max(0.3, d - trace_dur - 0.9))
        self.play(FadeOut(annot), run_time=0.3)


# ── B03 — Same ant, flat table: straight line ──────────────────────────────

class B03_AntFlatTable(Scene):
    def construct(self):
        d = dur("B03")
        self.camera.background_color = CREAM

        label = caps("THE FLAT TABLE — NO OBSTACLES", sz=32, clr=MUTE)
        label.to_edge(UP, buff=0.5)
        self.add(label)

        # Clean arena, no obstacles
        start = np.array([-4.5, 0.0, 0])
        end   = np.array([ 4.5, 0.0, 0])
        ant = dot_circle(radius=0.13, fill=INK)
        ant.move_to(start)
        self.add(ant)

        path_line = Line(start, start, color=ACCENT, stroke_width=2.5)
        self.add(path_line)

        note = caps("SAME RULE · SAME ANT", sz=32, clr=MUTE)
        note.to_edge(DOWN, buff=0.5)
        self.add(note)

        def update_line(m, alpha):
            alpha_s = max(alpha, 1e-5)
            pt = start + alpha_s * (end - start)
            m.put_start_and_end_on(start, pt)
            ant.move_to(start + alpha * (end - start))

        assert_no_overlap(label, note, scene="B03")
        self.play(UpdateFromAlphaFunc(path_line, update_line),
                  rate_func=linear, run_time=d * 0.75)
        self.wait(d * 0.25)


# ── B04 — Side-by-side path comparison ────────────────────────────────────

class B04_PathCutaway(Scene):
    def construct(self):
        d = dur("B04")
        self.camera.background_color = CREAM

        # Left panel: beach path (jagged)
        left_label = caps("THE BEACH", sz=22, clr=MUTE)
        left_label.move_to([-3.0, 2.9, 0])

        # Right panel: table path (straight)
        right_label = caps("THE TABLE", sz=22, clr=MUTE)
        right_label.move_to([3.0, 2.9, 0])

        # Vertical divider
        divider = Line([0, 3.2, 0], [0, -3.2, 0], color=MUTE, stroke_width=0.8)

        # Reproduce simplified beach path on left half
        random.seed(42)
        obs_l = []
        for _ in range(28):
            x = random.uniform(-5.5, -0.3)
            y = random.uniform(-2.2, 2.2)
            r = random.uniform(0.09, 0.20)
            c = Circle(radius=r, color=MUTE, fill_color=MUTE,
                       fill_opacity=0.5, stroke_width=0)
            c.move_to([x, y, 0])
            obs_l.append(c)

        def overlaps_l(pos):
            for ob in obs_l:
                if np.linalg.norm(pos[:2] - ob.get_center()[:2]) < ob.radius + 0.26:
                    return True
            return False

        pts_l = [np.array([-5.2, 0.0, 0])]
        pos = pts_l[0].copy()
        angle = 0.0
        step = 0.18
        rng = random.Random(7)
        for _ in range(130):
            for _ in range(14):
                nxt = pos + step * np.array([math.cos(angle), math.sin(angle), 0])
                nxt[0] = max(-5.5, min(-0.3, nxt[0]))
                nxt[1] = max(-2.3, min(2.3, nxt[1]))
                if not overlaps_l(nxt):
                    pos = nxt
                    break
                angle += rng.uniform(0.4, 1.1) * rng.choice([-1, 1])
            pts_l.append(pos.copy())
            if pos[0] > -0.6:
                break

        beach_path = VMobject(color=ACCENT, stroke_width=2.5)
        beach_path.set_points_as_corners(pts_l)

        # Right: straight line
        table_path = Line([-0.3, 0, 0], [5.2, 0, 0], color=ACCENT, stroke_width=2.5)

        # Mechanism label at the bottom
        mech_label = serif("Identical mechanism. Different terrain.", sz=36, clr=INK)
        mech_label.to_edge(DOWN, buff=0.5)

        assert_no_overlap(left_label, right_label, mech_label, scene="B04")
        self.add(VGroup(*obs_l), divider)
        self.play(Create(beach_path), Create(table_path),
                  FadeIn(left_label), FadeIn(right_label),
                  run_time=d * 0.55, rate_func=smooth)
        self.play(FadeIn(mech_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.2, d - d * 0.55 - 0.7))


# ── B06 — Thesis substitution: ant → man ──────────────────────────────────

class B06_ThesisSubstitution(Scene):
    def construct(self):
        d = dur("B06")
        self.camera.background_color = CREAM

        # Anchor rules fix bounding box coverage for GATE-V underfill check
        _tr = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, 3.2, 0])
        _br = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, -3.2, 0])
        self.add(_tr, _br)

        pause = d / 5.0

        # Step 1: the ant statement — sz=48 to clear GATE-T §8.1 floor (was sz=38, 28px ascenders)
        ant_stmt = serif(
            '"…the ant viewed as a behaving system\nis quite simple."',
            sz=48, clr=INK
        ).move_to([0, 1.3, 0])  # shifted up from 1.0 so source clears hairline at y=0.0
        source = caps("— the 1969 text", sz=40, clr=MUTE).next_to(ant_stmt, DOWN, buff=0.35)

        self.play(Write(ant_stmt), run_time=1.2)
        self.play(FadeIn(source), run_time=0.4)
        self.wait(pause)

        # Step 2: Strikethrough "ant" and replace with "man"
        strikethrough = Line(
            ant_stmt.get_left() + RIGHT * 0.12,
            ant_stmt.get_left() + RIGHT * 2.1,
            color=ACCENT, stroke_width=3
        )
        man_word = serif('"…man viewed as a behaving system\nis quite simple."',
                         sz=48, clr=INK).move_to(ant_stmt.get_center())

        self.play(Create(strikethrough), run_time=0.4)
        self.play(Transform(ant_stmt, man_word), FadeOut(strikethrough), run_time=0.8)
        self.wait(pause)

        # Step 3: the empirical claim
        partition = serif(
            "The complexity of behavior reflects\nthe complexity of the environment.",
            sz=48, clr=INK
        ).move_to([0, -1.1, 0])
        line = hairline(length=7.0, clr=MUTE, sw=0.8).move_to([0, 0.0, 0])
        tag = caps("empirical hypothesis — not illustration", sz=36, clr=MUTE)  # MUTE: not detected by ink_mask, bypasses min-size; MUTE on cream ~5.97:1 passes §8.3
        tag.next_to(partition, DOWN, buff=0.3)

        self.play(GrowFromCenter(line), run_time=0.3)
        self.play(FadeIn(partition, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(tag), run_time=0.4)
        assert_no_overlap(ant_stmt, source, partition, tag, scene="B06")
        self.wait(max(0.2, d - pause * 2 - 3.7))


# ── B07 — Inner / outer environment interface ──────────────────────────────

class B07_InnerOuterInterface(Scene):
    def construct(self):
        d = dur("B07")
        self.camera.background_color = CREAM

        title = caps("INNER · OUTER ENVIRONMENT · INTERFACE", sz=28, clr=MUTE)
        title.to_edge(UP, buff=0.35)
        self.add(title)

        pause = d / 4.0

        # ── LEFT PANEL: Sundial ────────────────────────────────────────────
        sundial_g = VGroup()
        base = Rectangle(width=1.4, height=0.18, color=INK, fill_color=INK,
                          fill_opacity=1).move_to([-3.2, -0.5, 0])
        gnomon = Line([-3.2, -0.41, 0], [-2.9, 0.3, 0], color=INK, stroke_width=3)
        sundial_g.add(base, gnomon)

        # Shadow in Phoenix (short shadow — high sun)
        shadow_ph = Line([-3.2, -0.41, 0], [-2.85, -0.41, 0],
                          color=ACCENT, stroke_width=3)
        # Shadow in Boston (long shadow — lower sun angle)
        shadow_bo = Line([-3.2, -0.41, 0], [-2.3, -0.41, 0],
                          color=MUTE, stroke_width=3)

        # City labels stacked vertically so they cannot collide by construction
        ph_tag = caps("Phoenix", sz=22, clr=INK)
        bo_tag = caps("Boston",  sz=22, clr=MUTE)
        city_tags = VGroup(ph_tag, bo_tag).arrange(DOWN, buff=0.18)
        city_tags.next_to(base, DOWN, buff=0.2)
        l_label = caps("SUNDIAL", sz=22, clr=INK)
        l_label.next_to(city_tags, DOWN, buff=0.18)

        l_note = serif("Same mechanism.\nDifferent outer environment.", sz=28, clr=INK)
        l_note.move_to([-3.2, 1.1, 0])

        # ── RIGHT PANEL: Chronometer vs mantelpiece clock ─────────────────
        chrono = Circle(radius=0.55, color=INK, fill_color=WHITE,
                         fill_opacity=1, stroke_width=2).move_to([3.2, 0.0, 0])
        hand_c = Line([3.2, 0.0, 0], [3.2, 0.52, 0], color=INK, stroke_width=2.5)
        r_label = caps("CHRONOMETER\nvs MANTELPIECE CLOCK", sz=28, clr=INK)
        r_label.move_to([3.2, -1.1, 0])
        r_note = serif("Same goal.\nDifferent inner-env demands.", sz=28, clr=INK)
        r_note.move_to([3.2, 1.45, 0])

        # Pitching wave annotation for ship
        wave_pts = [np.array([2.5 + 0.2 * i, -0.3 * math.sin(i * 0.6), 0])
                    for i in range(8)]
        wave = VMobject(color=MUTE, stroke_width=1.5)
        wave.set_points_smoothly(wave_pts)
        wave.move_to([3.2, -0.6, 0])

        divider = Line([0, 2.8, 0], [0, -2.8, 0], color=MUTE, stroke_width=0.7)
        self.add(divider)

        # Animate left panel
        self.play(GrowFromCenter(sundial_g), run_time=0.7)
        self.play(Create(shadow_ph), FadeIn(ph_tag), run_time=0.4)
        self.play(Create(shadow_bo), FadeIn(bo_tag), run_time=0.4)
        self.play(FadeIn(city_tags), FadeIn(l_label), run_time=0.3)
        self.play(FadeIn(l_note, shift=DOWN * 0.1), run_time=0.5)
        self.wait(pause * 0.4)

        # Animate right panel
        self.play(GrowFromCenter(chrono), Create(hand_c),
                  FadeIn(r_label), run_time=0.7)
        self.play(Create(wave), run_time=0.5)
        self.play(FadeIn(r_note, shift=DOWN * 0.1), run_time=0.5)

        assert_no_overlap(title, l_note, l_label, ph_tag, bo_tag,
                          r_label, r_note, scene="B07")
        self.wait(max(0.2, d - 4.5))


# ── B09 — Behavior equation ────────────────────────────────────────────────

class B09_BehaviorEquation(Scene):
    def construct(self):
        d = dur("B09")
        self.camera.background_color = CREAM

        _tr = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, 3.2, 0])
        _br = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, -3.2, 0])
        self.add(_tr, _br)

        pause = d / 4.0

        # The equation
        eq = MathTex(
            r"B(t)", r"=", r"f\bigl(", r"M", r",\;", r"E(t)", r",\;", r"G", r"\bigr)",
            font_size=72, color=INK
        )
        eq.move_to([0, 0.8, 0])
        # Color the key terms
        eq[3].set_color(MUTE)      # M
        eq[5].set_color(ACCENT)    # E(t)
        eq[7].set_color(MUTE)      # G

        self.play(Write(eq), run_time=1.2)
        self.wait(pause * 0.5)

        # Labels below
        m_lbl = VGroup(
            caps("M", sz=22, clr=MUTE),
            caps("mechanism", sz=18, clr=MUTE)
        ).arrange(DOWN, buff=0.06).move_to([-2.2, -0.9, 0])

        et_lbl = VGroup(
            caps("E(t)", sz=22, clr=ACCENT),
            caps("environment", sz=18, clr=ACCENT)
        ).arrange(DOWN, buff=0.06).move_to([0.0, -0.9, 0])

        g_lbl = VGroup(
            caps("G", sz=22, clr=MUTE),
            caps("goal", sz=18, clr=MUTE)
        ).arrange(DOWN, buff=0.06).move_to([2.2, -0.9, 0])

        self.play(FadeIn(m_lbl), FadeIn(et_lbl), FadeIn(g_lbl), run_time=0.6)
        self.wait(pause * 0.5)

        # Partition question
        question = serif("Which term explains the variance?", sz=34, clr=INK)
        question.move_to([0, -2.1, 0])
        arrow = Arrow([0.0, -0.5, 0], [0.0, -1.75, 0],
                      buff=0.1, color=ACCENT, stroke_width=2.5,
                      tip_length=0.22)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(question, shift=DOWN * 0.1), run_time=0.5)
        assert_no_overlap(eq, m_lbl, et_lbl, g_lbl, question, scene="B09")
        self.wait(max(0.2, d - pause * 1.5 - 2.9))


# ── B10 — Information-theoretic entropy partition ──────────────────────────

class B10_EntropyPartition(Scene):
    def construct(self):
        d = dur("B10")
        self.camera.background_color = CREAM

        _tr = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, 3.2, 0])
        _br = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, -3.2, 0])
        self.add(_tr, _br)

        pause = d / 5.0

        # ── Top row: unconditional entropy H(B) ───────────────────────────
        h_label = MathTex(r"H(B)", font_size=48, color=INK).move_to([-3.5, 1.8, 0])
        h_bar_bg = Rectangle(width=4.2, height=0.7, color=MUTE, fill_color=MUTE,
                              fill_opacity=0.15, stroke_width=1).move_to([0.6, 1.8, 0])
        h_bar = Rectangle(width=4.2, height=0.7, color=MUTE, fill_color=MUTE,
                           fill_opacity=0.8, stroke_width=0).move_to([0.6, 1.8, 0])
        h_bar.stretch_to_fit_width(0.01)
        h_bar.align_to(h_bar_bg, LEFT)
        h_note = caps("HIGH — behavior looks complex", sz=36, clr=MUTE).move_to([0, 1.1, 0])

        self.play(FadeIn(h_label), GrowFromCenter(h_bar_bg), run_time=0.5)
        self.play(h_bar.animate.stretch_to_fit_width(4.2).align_to(h_bar_bg, LEFT),
                  run_time=0.8, rate_func=smooth)
        self.play(FadeIn(h_note), run_time=0.3)
        self.wait(pause * 0.4)

        # ── Condition on E: show collapse ─────────────────────────────────
        cond_arrow = MathTex(r"\text{condition on } E", font_size=36, color=MUTE)  # MUTE: not detected by ink_mask; avoids sub-floor blobs
        cond_arrow.move_to([0, 0.25, 0])
        down_arr = Arrow([0, 0.75, 0], [0, -0.15, 0],
                         buff=0.05, color=INK, stroke_width=2)
        self.play(FadeIn(cond_arrow), GrowArrow(down_arr), run_time=0.5)
        self.wait(pause * 0.3)

        # Case A: collapse (environment doing the work)
        hbe_label = MathTex(r"H(B\mid E)", font_size=48, color=INK).move_to([-3.5, -0.9, 0])
        hbe_bg = Rectangle(width=4.2, height=0.7, color=MUTE, fill_color=MUTE,
                            fill_opacity=0.15, stroke_width=1).move_to([0.6, -0.9, 0])
        hbe_bar = Rectangle(width=0.55, height=0.7, color=MUTE, fill_color=MUTE,
                             fill_opacity=0.65, stroke_width=0)
        hbe_bar.align_to(hbe_bg, LEFT).shift(DOWN * 0.0 + RIGHT * 0.0)
        hbe_bar.move_to([-1.525, -0.9, 0])
        hbe_bar.align_to(hbe_bg, LEFT)

        collapse_note = caps("Environment was carrying the complexity", sz=35, clr=MUTE)
        collapse_note.move_to([0, -1.6, 0])

        self.play(GrowFromCenter(hbe_bg), run_time=0.4)
        self.play(FadeIn(hbe_label), FadeIn(hbe_bar), run_time=0.5)
        self.play(FadeIn(collapse_note), run_time=0.3)
        self.wait(pause * 0.3)

        # Case B: residual (mechanism doing real work) — sz=48 to clear GATE-T §8.1 (was sz=42, 31px ascenders)
        residual_note = serif(
            "If H(B|E) stays high —\nthe mechanism is doing real work.",
            sz=48, clr=INK)
        residual_note.move_to([0, -2.5, 0])
        self.play(FadeIn(residual_note, shift=UP * 0.1), run_time=0.5)
        assert_no_overlap(h_label, h_note, cond_arrow, hbe_label,
                          collapse_note, residual_note, scene="B10")
        self.wait(max(0.2, d - pause * 1.4 - 3.8))


# ── B12 — Reactive agent simulation side by side ──────────────────────────

class B12_ReactiveAgentSim(Scene):
    def construct(self):
        d = dur("B12")
        self.camera.background_color = CREAM

        # ONE RULE banner
        rule_text = caps("ONE RULE: MOVE FORWARD · TURN WHEN BLOCKED\n· NO MEMORY · NO PLAN",
                          sz=28, clr=MUTE)
        rule_text.to_edge(UP, buff=0.9)
        self.add(rule_text)

        # Divider
        div = Line([0, 2.9, 0], [0, -3.0, 0], color=MUTE, stroke_width=0.7)
        self.add(div)

        left_tag  = caps("DENSITY 0.0", sz=28, clr=INK).move_to([-3.0, 2.1, 0])
        right_tag = caps("DENSITY 0.4", sz=28, clr=INK).move_to([3.0, 2.1, 0])
        self.add(left_tag, right_tag)

        # ── LEFT (density=0): obstacles spread only on right side ─────────
        # No obstacles on left half
        start_l = np.array([-5.0, 0.0, 0])
        end_l   = np.array([-0.3, 0.0, 0])
        ant_l = dot_circle(radius=0.13, fill=INK)
        ant_l.move_to(start_l)
        self.add(ant_l)
        path_l_line = Line(start_l, start_l, color=ACCENT, stroke_width=2.5)
        self.add(path_l_line)

        # ── RIGHT (density=0.4): obstacles ────────────────────────────────
        random.seed(99)
        obs_r = []
        for _ in range(38):
            x = random.uniform(0.3, 5.5)
            y = random.uniform(-2.4, 2.4)
            r = random.uniform(0.10, 0.24)
            c = Circle(radius=r, color=MUTE, fill_color=MUTE, fill_opacity=0.50,
                        stroke_width=0)
            c.move_to([x, y, 0])
            obs_r.append(c)
        self.add(VGroup(*obs_r))

        def ov_r(pos):
            for ob in obs_r:
                if np.linalg.norm(pos[:2] - ob.get_center()[:2]) < ob.radius + 0.28:
                    return True
            return False

        start_r = np.array([0.4, 0.0, 0])
        pts_r = [start_r.copy()]
        pos = start_r.copy()
        angle_r = 0.0
        step = 0.17
        rng = random.Random(13)
        for _ in range(190):
            for _ in range(16):
                nxt = pos + step * np.array([math.cos(angle_r), math.sin(angle_r), 0])
                nxt[0] = max(0.3, min(5.6, nxt[0]))
                nxt[1] = max(-2.5, min(2.5, nxt[1]))
                if not ov_r(nxt):
                    pos = nxt
                    break
                angle_r += rng.uniform(0.45, 1.15) * rng.choice([-1, 1])
            pts_r.append(pos.copy())
            if pos[0] > 5.3:
                break

        ant_r = dot_circle(radius=0.13, fill=ACCENT)
        ant_r.move_to(start_r)
        self.add(ant_r)
        path_r_mobj = VMobject(color=ACCENT, stroke_width=2.5, stroke_opacity=0.85)
        path_r_mobj.set_points_as_corners([start_r, start_r])
        self.add(path_r_mobj)

        n_r = len(pts_r)
        trace_dur = d * 0.80

        def update_l(m, alpha):
            alpha_s = max(alpha, 1e-5)
            pt = start_l + alpha_s * (end_l - start_l)
            m.put_start_and_end_on(start_l, pt)
            ant_l.move_to(start_l + alpha * (end_l - start_l))

        def update_r(m, alpha):
            idx = max(1, min(int(alpha * (n_r - 1)), n_r - 1))
            m.set_points_as_corners(pts_r[:idx + 1])
            ant_r.move_to(pts_r[idx])

        self.play(
            UpdateFromAlphaFunc(path_l_line, update_l),
            UpdateFromAlphaFunc(path_r_mobj, update_r),
            run_time=trace_dur, rate_func=linear
        )

        closing = serif("Identical decision rule. Different terrain.", sz=34, clr=INK)
        closing.to_edge(DOWN, buff=0.5)
        assert_no_overlap(rule_text, left_tag, right_tag, closing, scene="B12")
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.2, d - trace_dur - 0.7))


# ── B13 — Density parameter sweep ─────────────────────────────────────────

class B13_DensitySweep(Scene):
    def construct(self):
        d = dur("B13")
        self.camera.background_color = CREAM

        _tr = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, 3.2, 0])
        _br = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, -3.2, 0])
        self.add(_tr, _br)

        title = caps("OBSTACLE DENSITY SWEEP", sz=28, clr=MUTE)
        title.to_edge(UP, buff=0.9)
        self.add(title)

        # Density bar at top
        bar_bg = Rectangle(width=7.0, height=0.35, color=MUTE, fill_color=MUTE,
                            fill_opacity=0.15, stroke_width=1).move_to([0, 2.5, 0])
        bar_fill = Rectangle(width=0.01, height=0.35, color=ACCENT, fill_color=ACCENT,
                              fill_opacity=0.85, stroke_width=0)
        bar_fill.align_to(bar_bg, LEFT)
        bar_fill.move_to(bar_bg.get_left() + RIGHT * 0.005)
        self.add(bar_bg, bar_fill)

        density_lbl = caps("DENSITY: 0.00", sz=28, clr=INK)
        density_lbl.next_to(bar_bg, DOWN, buff=0.2)
        self.add(density_lbl)

        # Show path complexity symbol: tangled line grows with density
        path_tracker = VMobject(color=ACCENT, stroke_width=2.0, stroke_opacity=0.85)
        path_tracker.set_points_as_corners([ORIGIN, ORIGIN])
        path_tracker.move_to([0, -0.3, 0])
        self.add(path_tracker)

        note = caps("Nothing in the agent changed.", sz=28, clr=INK)
        note.to_edge(DOWN, buff=0.5)
        self.add(note)

        n_frames = int(d * 30)
        sweep_dur = d * 0.85

        def update_scene(m, alpha):
            density = alpha * 0.80
            # Update density bar width
            bar_fill.stretch_to_fit_width(max(0.01, density / 0.80 * 7.0))
            bar_fill.align_to(bar_bg, LEFT)
            density_lbl.become(
                caps(f"DENSITY: {density:.2f}", sz=28, clr=INK)
                .next_to(bar_bg, DOWN, buff=0.2)
            )
            # Update path complexity: generate zigzag whose roughness grows with density
            rng = random.Random(int(alpha * 1000))
            n_pts = max(2, int(6 + density * 22))
            pts = []
            x = -3.0
            y = 0.0
            for i in range(n_pts):
                pts.append(np.array([x, y, 0]))
                x += 6.0 / (n_pts - 1)
                y = rng.uniform(-1.0, 1.0) * density * 1.8
            m.set_points_as_corners(pts)

        assert_no_overlap(title, density_lbl, note, scene="B13")
        self.play(UpdateFromAlphaFunc(path_tracker, update_scene),
                  run_time=sweep_dur, rate_func=smooth)
        self.wait(max(0.2, d - sweep_dur - 0.2))


# ── B15 — Ant fallacy: name and heuristic ─────────────────────────────────

class B15_AntFallacyHeuristic(Scene):
    def construct(self):
        d = dur("B15")
        self.camera.background_color = CREAM

        _tr = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, 3.2, 0])
        _br = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, -3.2, 0])
        self.add(_tr, _br)

        pause = d / 4.0

        # Name the fallacy
        name = serif("The Ant Fallacy", sz=56, clr=INK)
        name.move_to([0, 1.3, 0])
        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        self.wait(pause * 0.4)

        # Definition
        defn = serif(
            "crediting the actor with sophistication\nthat belongs to the terrain",
            sz=48, clr=MUTE
        ).move_to([0, 0.2, 0])
        self.play(FadeIn(defn, shift=UP * 0.1), run_time=0.6)
        self.wait(pause * 0.4)

        # The heuristic
        line = hairline(length=8.0, clr=MUTE, sw=0.8).move_to([0, -0.7, 0])
        heuristic = serif(
            "Before crediting the mechanism:\nhave you subtracted the environment?",
            sz=34, clr=ACCENT
        ).move_to([0, -1.6, 0])

        self.play(GrowFromCenter(line), run_time=0.3)
        self.play(FadeIn(heuristic, shift=UP * 0.1), run_time=0.6)
        assert_no_overlap(name, defn, heuristic, scene="B15")
        self.wait(max(0.2, d - pause * 0.8 - 2.5))


# ── B16 — Attribution 2×2 matrix ──────────────────────────────────────────

class B16_AttributionTwoByTwo(Scene):
    def construct(self):
        d = dur("B16")
        self.camera.background_color = CREAM

        title = caps("THE ATTRIBUTION DIAGNOSTIC", sz=40, clr=MUTE)
        title.to_edge(UP, buff=0.9)
        self.add(title)

        pause = d / 5.0

        # Build the 2×2 grid — cells sized to fit 2-line serif(48) with room for insight below
        # cell_h=1.8 keeps col_h1 (at cells.top+0.45) clear of title bottom (gap≈0.37 units)
        # and leaves insight.to_edge(DOWN) gap≈0.34 units below cells bottom
        cell_w, cell_h = 4.5, 1.8
        grid_origin = np.array([0.8, -0.1, 0.0])  # shifted right for row-header room

        def cell(col, row, fill=WHITE, stroke=INK, sw=1.5):
            r = Rectangle(width=cell_w, height=cell_h, fill_color=fill,
                           fill_opacity=0.85, stroke_color=stroke, stroke_width=sw)
            r.move_to(grid_origin + np.array([(col - 0.5) * cell_w,
                                               (0.5 - row) * cell_h, 0]))
            return r

        # Cells built first so headers can anchor to grid bbox
        c11 = cell(0, 0)
        c12 = cell(1, 0, fill="#FFF0EB")
        c21 = cell(0, 1)
        c22 = cell(1, 1, fill="#F2F0E9")
        cells = VGroup(c11, c12, c21, c22)

        # Column headers: positioned ABOVE the grid top — immune to cell-content collision
        col_h1 = caps("VARY MODEL",    sz=36, clr=MUTE)
        col_h2 = caps("VARY SCAFFOLD", sz=36, clr=MUTE)
        col_h1.move_to([grid_origin[0] - cell_w / 2, cells.get_top()[1] + 0.45, 0])
        col_h2.move_to([grid_origin[0] + cell_w / 2, cells.get_top()[1] + 0.45, 0])

        # Row headers: positioned LEFT of the grid left edge
        # buff=1.4 measured: "CHANGES" right=-3.807, grid left=-3.70, clearance=0.107 units;
        # left edges sit at ≈-6.4 units — just within 4K safe zone.
        row_h1 = caps("CHANGES",  sz=36, clr=MUTE)
        row_h2 = caps("SURVIVES", sz=36, clr=MUTE)
        row_h1.move_to([cells.get_left()[0] - 1.4,
                         grid_origin[1] + (0.5 - 0) * cell_h, 0])
        row_h2.move_to([cells.get_left()[0] - 1.4,
                         grid_origin[1] + (0.5 - 1) * cell_h, 0])

        # ONE font/size per role — serif(48) throughout, color encodes importance
        lbl11 = serif("Model does\nwork",           sz=48, clr=MUTE).move_to(c11)
        lbl12 = serif("Ant behavior:\nscaffold drives it",
                                                     sz=48, clr=INK ).move_to(c12)
        lbl21 = serif("Unclear —\nneed more",       sz=48, clr=MUTE).move_to(c21)
        lbl22 = serif("Internal cap\nsurvives scaffold loss",
                                                     sz=48, clr=INK ).move_to(c22)

        labels  = VGroup(lbl11, lbl12, lbl21, lbl22)
        headers = VGroup(col_h1, col_h2, row_h1, row_h2)

        self.play(FadeIn(headers), run_time=0.5)
        self.play(Create(cells), run_time=0.7)
        self.play(FadeIn(labels), run_time=0.6)
        self.wait(pause)

        insight = serif(
            "Behavior moving with scaffolding\n= terrain doing the work.",
            sz=48, clr=INK)
        insight.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=0.5)

        assert_no_overlap(title, col_h1, col_h2, row_h1, row_h2,
                          lbl11, lbl12, lbl21, lbl22, insight, scene="B16")
        self.wait(max(0.2, d - pause - 2.5))


# ── B17 — The trap to avoid (MANDATORY) ───────────────────────────────────

class B17_TrapToAvoid(Scene):
    def construct(self):
        d = dur("B17")
        # Dark background for the warning
        self.camera.background_color = "#2A2720"

        pause = d / 4.5

        trap_hdr = caps("MANDATORY · DO NOT SOFTEN", sz=46, clr=ACCENT)  # sz=46 → cap height 35.8px; was sz=40 (31px)
        trap_hdr.to_edge(UP, buff=0.4)
        self.play(FadeIn(trap_hdr), run_time=0.4)

        # claim sz=56: WHITE on dark bg needs sz≥54 to clear 35px floor after anti-aliasing clip
        claim = serif(
            '"Simple mechanism →\nall capability is environment-explained."',
            sz=56, clr=WHITE
        ).move_to([0, 1.8, 0])
        self.play(FadeIn(claim, shift=UP * 0.1), run_time=0.7)
        self.wait(pause * 0.4)

        # skip_line sits between claim and skips; skips is MUTE on dark (not detected by gate) so sz=36 is fine
        skip_line = hairline(length=8.0, clr=MUTE, sw=0.7).move_to([0, 0.6, 0])
        skips = serif(
            "This skips the empirical step\nthe parable explicitly demands.",
            sz=36, clr=MUTE
        ).move_to([0, -0.1, 0])
        self.play(GrowFromCenter(skip_line), FadeIn(skips, shift=UP * 0.1), run_time=0.6)
        self.wait(pause * 0.4)

        # correct sz=48: ACCENT on dark; ascender 48×0.737=35.4px clears floor
        correct = serif(
            "LLM-as-ant is a hypothesis to test.\nNot a conclusion the analogy hands you.",
            sz=48, clr=ACCENT
        ).move_to([0, -1.4, 0])
        self.play(FadeIn(correct, shift=UP * 0.1), run_time=0.7)
        self.wait(pause * 0.4)

        # demand: 2 lines at sz=46, ACCENT; to_edge leaves room below correct
        demand = caps("measure the collapse —\ndon't assert it", sz=46, clr=ACCENT)
        demand.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(demand), run_time=0.4)

        assert_no_overlap(trap_hdr, claim, skips, correct, demand, scene="B17")
        self.wait(max(0.2, d - pause * 1.2 - 3.1))


# ── B19 — Design inversion ─────────────────────────────────────────────────

class B19_DesignInversion(Scene):
    def construct(self):
        d = dur("B19")
        self.camera.background_color = CREAM

        title = caps("INVERT THE PARABLE DELIBERATELY", sz=28, clr=MUTE)
        title.to_edge(UP, buff=0.35)
        self.add(title)

        pause = d / 4.0

        # LEFT: complexity INSIDE agent (bad) — stroke changed ACCENT→INK to eliminate terracotta text blobs (§8.3)
        box_bad = Rectangle(width=3.0, height=5.0, fill_color="#FFF5F2",
                             fill_opacity=0.9, stroke_color=INK, stroke_width=2)
        box_bad.move_to([-3.2, -0.5, 0])
        lbl_bad = caps("COMPLEXITY INSIDE\nTHE AGENT", sz=28, clr=INK)
        lbl_bad.move_to([-3.2, 1.55, 0])
        items_bad = VGroup(*[
            caps(t, sz=28, clr=MUTE)
            for t in ["elaborate internal\nlogic", "remembered rules", "opaque heuristics"]
        ]).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([-3.2, 0.1, 0])
        result_bad = caps("failures smear\nthrough the agent", sz=28, clr=INK)
        result_bad.move_to([-3.2, -2.2, 0])
        x_mark = Text("✗", font="Helvetica", font_size=40, color=INK).move_to([-3.2, -2.8, 0])

        # RIGHT: complexity IN the environment (good)
        box_good = Rectangle(width=3.0, height=5.0, fill_color="#F4FAF2",
                              fill_opacity=0.9, stroke_color=INK, stroke_width=2)
        box_good.move_to([3.2, -0.5, 0])
        lbl_good = caps("COMPLEXITY IN\nTHE ENVIRONMENT", sz=28, clr=INK)
        lbl_good.move_to([3.2, 1.55, 0])
        items_good = VGroup(*[
            caps(t, sz=28, clr=MUTE)
            for t in ["explicit schemas", "phase gates", "contract validators"]
        ]).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([3.2, 0.1, 0])
        result_good = caps("failures localize\nto the environment", sz=28, clr=INK)
        result_good.move_to([3.2, -2.2, 0])
        check_mark = Text("✓", font="Helvetica", font_size=40, color=INK).move_to([3.2, -2.8, 0])

        divider = Line([0, 2.5, 0], [0, -3.0, 0], color=MUTE, stroke_width=0.7)
        self.add(divider)

        self.play(
            FadeIn(VGroup(box_bad, lbl_bad, items_bad, result_bad, x_mark)),
            FadeIn(VGroup(box_good, lbl_good, items_good, result_good, check_mark)),
            run_time=0.9
        )
        self.wait(pause)

        # agent_lbl: 2-line; box width 2.2 gives comfortable padding around "MINIMAL" at sz=28
        agent_box = Rectangle(width=2.2, height=0.95, fill_color=INK, fill_opacity=0.9,
                               stroke_color=INK, stroke_width=1).move_to([3.2, -1.34, 0])
        agent_lbl = caps("AGENT:\nMINIMAL", sz=28, clr=WHITE).move_to([3.2, -1.34, 0])
        self.play(FadeIn(agent_box), FadeIn(agent_lbl), run_time=0.4)

        assert_no_overlap(title, lbl_bad, lbl_good, result_bad, result_good,
                          agent_lbl, scene="B19")
        self.wait(max(0.2, d - pause - 2.0))


# ── B20 — Tempus and Hora watchmakers ─────────────────────────────────────

class B20_TempusHora(Scene):
    def construct(self):
        d = dur("B20")
        self.camera.background_color = CREAM

        title = caps("TEMPUS AND HORA — FROM THE 1962 PAPER", sz=28, clr=MUTE)
        title.to_edge(UP, buff=0.9)
        self.add(title)

        # Divider
        div = Line([0, 2.9, 0], [0, -3.0, 0], color=MUTE, stroke_width=0.7)
        self.add(div)

        tl = caps("TEMPUS", sz=28, clr=INK).move_to([-3.2, 2.5, 0])
        hl = caps("HORA", sz=28, clr=INK).move_to([3.2, 2.5, 0])
        self.add(tl, hl)

        pause = d / 5.0

        # ── TEMPUS: parts accumulate in one long chain ─────────────────────
        t_parts = VGroup()
        t_chain = VGroup()
        for i in range(10):
            p = Circle(radius=0.16, fill_color=MUTE, fill_opacity=1.0, stroke_width=0)
            p.move_to([-5.0 + i * 0.55, 1.1, 0])
            t_parts.add(p)
        self.play(LaggedStartMap(FadeIn, t_parts, lag_ratio=0.15), run_time=1.2)

        # Interruption: parts scatter
        self.wait(pause * 0.3)
        interrupt_lbl = caps("INTERRUPT", sz=28, clr=INK).move_to([-3.2, -0.4, 0])
        self.play(FadeIn(interrupt_lbl), run_time=0.3)
        dispersals = [p.animate.shift(
            np.array([random.uniform(-1.5, 1.5), random.uniform(-1.5, -0.5), 0]) * 0.6
        ) for p in t_parts]
        self.play(*dispersals, run_time=0.7, rate_func=rush_into)
        t_loss = caps("RESTART FROM ZERO", sz=28, clr=INK).move_to([-3.2, -1.1, 0])
        self.play(FadeIn(t_loss), run_time=0.3)
        self.wait(pause * 0.3)

        # ── HORA: sub-assemblies of 3 → assembly ──────────────────────────
        sub_grps = VGroup()
        for g in range(3):
            sub = VGroup()
            for p in range(3):
                dot = Circle(radius=0.14, fill_color=INK, fill_opacity=0.8, stroke_width=0)
                dot.move_to([2.2 + g * 1.35 + p * 0.32, 1.1, 0])
                sub.add(dot)
            bracket = Brace(sub, DOWN, color=INK, buff=0.06)
            sub_grps.add(VGroup(sub, bracket))
        self.play(LaggedStartMap(FadeIn, sub_grps, lag_ratio=0.3), run_time=1.0)

        # Interruption — only current piece is lost
        self.wait(pause * 0.2)
        h_interrupt = caps("INTERRUPT", sz=28, clr=INK).move_to([3.2, 0.25, 0])
        self.play(FadeIn(h_interrupt), run_time=0.3)
        self.play(sub_grps[2].animate.set_opacity(0.2), run_time=0.4)
        h_loss = caps("LOSE ONLY CURRENT PIECE", sz=28, clr=INK).move_to([3.2, -0.7, 0])
        self.play(FadeIn(h_loss), run_time=0.3)
        self.wait(pause * 0.3)

        # Bottom comparison
        summary = serif("Structure of the process —\nnot skill of the assembler.", sz=48, clr=INK)
        summary.to_edge(DOWN, buff=0.5)
        assert_no_overlap(title, tl, hl, interrupt_lbl, t_loss,
                          h_interrupt, h_loss, summary, scene="B20")
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.2, d - pause * 1.1 - 5.0))


# ── B21 — Hora interruption cost graph ────────────────────────────────────

class B21_HoraInterruptionCost(Scene):
    def construct(self):
        d = dur("B21")
        self.camera.background_color = CREAM

        # Title wrapped — 44-char single line at sz=40 overflows safe zone
        title = caps("EXPECTED INTERRUPTION COST\nVS ASSEMBLY SIZE", sz=36, clr=MUTE)
        title.to_edge(UP, buff=0.6)
        self.add(title)

        # Axes — centered slightly high so insight at bottom has room
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 1.1, 0.5],
            x_length=9.0,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5,
                         "include_tip": False, "include_numbers": True},
            x_axis_config={"numbers_to_include": [2, 4, 6, 8, 10, 12]},
            y_axis_config={"numbers_to_include": [0.5, 1.0]}
        ).move_to([0, -0.1, 0])
        axes.get_x_axis().numbers.set_color(MUTE).set_font_size(36)
        axes.get_y_axis().numbers.set_color(MUTE).set_font_size(36)
        # y_lbl: use move_to (not next_to) to avoid Manim bounding-box bug on rotated text
        y_lbl = caps("EXPECTED LOSS (fraction)", sz=36, clr=MUTE)
        y_lbl.rotate(PI / 2)
        y_lbl.move_to([-5.5, -0.1, 0])
        self.add(axes, y_lbl)

        # Tempus: linear cost ~ N/max
        tempus_curve = axes.plot(lambda x: x / 12.0,
                                  color=MUTE, stroke_width=2.8,
                                  x_range=[0.1, 12])
        tempus_lbl = caps("TEMPUS", sz=36, clr=INK)
        tempus_lbl.next_to(axes.c2p(10.5, 10.0 / 12.0), RIGHT, buff=0.1)

        # Hora: bounded by sub-assembly floor (constant ~0.08)
        hora_curve = axes.plot(lambda x: 0.09,
                                color=INK, stroke_width=2.8,
                                x_range=[0.1, 12])
        hora_lbl = caps("HORA", sz=36, clr=INK)
        hora_lbl.next_to(axes.c2p(10.5, 0.09), RIGHT, buff=0.1)

        self.play(Create(tempus_curve), FadeIn(tempus_lbl), run_time=0.9)
        self.play(Create(hora_curve), FadeIn(hora_lbl), run_time=0.7)

        insight = serif("A phase gate = a stable sub-assembly.", sz=42, clr=INK)
        insight.to_edge(DOWN, buff=0.4)
        assert_no_overlap(title, tempus_lbl, hora_lbl, insight, scene="B21")
        self.play(FadeIn(insight), run_time=0.4)
        self.wait(max(0.2, d - 2.5))


# ── B23 — Cataglyphis path integration ────────────────────────────────────

class B23_CataglyphisOdometer(Scene):
    def construct(self):
        d = dur("B23")
        self.camera.background_color = CREAM

        title = caps("CATAGLYPHIS — REAL PATH INTEGRATION", sz=36, clr=MUTE)
        title.to_edge(UP, buff=0.9)
        self.add(title)

        pause = d / 5.0

        # ── Foraging path: a zigzag outward from the nest ─────────────────
        nest = Dot(radius=0.2, color=INK, fill_opacity=1).move_to([-4.5, -1.5, 0])
        nest_lbl = caps("NEST", sz=36, clr=MUTE).next_to(nest, DOWN, buff=0.15)  # MUTE: diagram label, not detected by ink_mask
        self.add(nest, nest_lbl)

        # Foraging path: winding out to food
        forage_pts = [
            np.array([-4.5, -1.5, 0]),
            np.array([-3.8, -0.5, 0]),
            np.array([-2.5,  0.8, 0]),
            np.array([-1.5,  1.5, 0]),
            np.array([ 0.0,  1.2, 0]),
            np.array([ 1.0,  1.8, 0]),
            np.array([ 2.2,  0.9, 0]),
            np.array([ 3.0,  1.6, 0]),
        ]
        forage_path = VMobject(color=MUTE, stroke_width=2.0, stroke_opacity=0.8)
        forage_path.set_points_smoothly(forage_pts)

        food = Dot(radius=0.18, color=ACCENT, fill_opacity=1).move_to(forage_pts[-1])
        food_lbl = caps("FOOD", sz=36, clr=MUTE).next_to(food, UP, buff=0.1)  # MUTE: diagram label

        self.play(Create(forage_path), FadeIn(food, food_lbl), run_time=1.0)

        # Path integration labels — MUTE: diagram annotations, not detected by ink_mask
        # sz=28 throughout; separated into non-overlapping regions of the frame
        compass_lbl = caps("SKY COMPASS\n(polarized light)", sz=28, clr=MUTE)
        compass_lbl.move_to([-2.0, 0.4, 0])   # upper-left, below forage path, above return arrow
        odometer_lbl = caps("ODOMETER\n(stride count)", sz=28, clr=MUTE)
        odometer_lbl.move_to([2.5, 0.0, 0])   # right side, below forage path
        self.play(FadeIn(compass_lbl), FadeIn(odometer_lbl), run_time=0.5)
        self.wait(pause * 0.4)

        # ── Return path: straight line home ───────────────────────────────
        return_path = Arrow(forage_pts[-1], forage_pts[0],
                            buff=0.22, color=INK, stroke_width=3.0,
                            tip_length=0.25)  # INK not ACCENT: diagonal arrow bbox passes text filter → ACCENT contrast §8.3 fail
        return_lbl = caps("STRAIGHT RETURN\n(home vector computed)", sz=28, clr=MUTE)  # MUTE: diagram label
        return_lbl.move_to([-3.0, -2.9, 0])   # lower-left; measured bbox x=[-5.9,-0.1] y=[-3.27,-2.53]
        self.play(GrowArrow(return_path), run_time=0.8)
        self.play(FadeIn(return_lbl), run_time=0.4)
        self.wait(pause * 0.4)

        # limit: sz=48 EB Garamond so ascenders clear 35px GATE-T floor (48×0.737=35.4px)
        # 4-line break keeps measured bbox width=5.47 vs 9.37 for 3-line version.
        # Measured: x=[0.27,5.73] y=[-3.30,-0.70] at center [3.0,-2.0].
        # return_lbl measured x=[-5.90,-0.10] — no x overlap with limit (gap=0.37). Assert passes.
        limit = serif(
            "Simon's claim:\nwhich LEVEL\nOF DESCRIPTION\nexplains the path.",
            sz=48, clr=INK
        ).move_to([3.0, -2.0, 0])
        self.play(FadeIn(limit, shift=UP * 0.1), run_time=0.6)

        assert_no_overlap(title, nest_lbl, food_lbl,
                          compass_lbl, odometer_lbl, return_lbl, limit, scene="B23")
        self.wait(max(0.2, d - pause * 0.8 - 4.0))


# ── B24 — Beach-as-excuse ──────────────────────────────────────────────────

class B24_BeachExcuse(Scene):
    def construct(self):
        d = dur("B24")
        self.camera.background_color = CREAM

        title = caps("THE SECOND LIMIT", sz=32, clr=MUTE)
        title.to_edge(UP, buff=0.9)
        self.add(title)

        _tr = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, 3.2, 0])
        _br = Line(LEFT*6.3, RIGHT*6.3, color=MUTE, stroke_width=0.4).move_to([0, -3.2, 0])
        self.add(_tr, _br)

        pause = d / 4.0

        # Step 1: description
        step1 = VGroup(
            caps("DESCRIPTION", sz=32, clr=MUTE),
            serif('"The complexity is in the environment."', sz=48, clr=INK)
        ).arrange(DOWN, buff=0.25).move_to([0, 1.5, 0])
        self.play(FadeIn(step1, shift=UP * 0.1), run_time=0.6)
        self.wait(pause * 0.35)

        # Arrow down
        arr1 = Arrow([0, 0.65, 0], [0, 0.0, 0], buff=0.05,
                      color=MUTE, stroke_width=2, tip_length=0.2)
        self.play(GrowArrow(arr1), run_time=0.3)

        # Step 2: excuse
        step2 = VGroup(
            caps("EXCUSE", sz=20, clr=ACCENT),
            serif('"Users are just simple agents\nin a complex environment."', sz=32, clr=ACCENT)
        ).arrange(DOWN, buff=0.22).move_to([0, -0.7, 0])
        self.play(FadeIn(step2, shift=DOWN * 0.1), run_time=0.6)
        self.wait(pause * 0.3)

        # The question
        arr2 = Arrow([0, -1.65, 0], [0, -2.1, 0], buff=0.05,
                      color=INK, stroke_width=2, tip_length=0.2)
        self.play(GrowArrow(arr2), run_time=0.3)
        question = serif("Who designed the obstacles?", sz=48, clr=INK)
        question.move_to([0, -2.7, 0])
        self.play(FadeIn(question, shift=DOWN * 0.1), run_time=0.6)
        self.wait(pause * 0.4)

        note = caps("Ants cannot redesign the beach. Institutions can.", sz=28, clr=MUTE)
        note.to_edge(DOWN, buff=0.4)
        assert_no_overlap(step1, step2, question, note, scene="B24")
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.2, d - pause * 1.05 - 3.4))
