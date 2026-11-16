"""ACT I · Two Failures That Passed  (B01-B08, all Manim)

One cast for the act: the PATIENT DOT (a small grey dot, never a person), the HOSPITAL OUTLINE, the four TILES
(ASKED / DID / REPORTED / STATE), the ENVELOPE with one terracotta dot (the secret) and the VALID / RIGHT circles.
Numbers on screen are only the ones in factcheck/PRIMARIES.md (Wong et al. 2021; Shapira et al. 2026 Case #1).
"""

A1_XS = [-4.65, -1.55, 1.55, 4.65]           # four tile centres
A1_TY, A1_TH, A1_TW = 0.4, 3.2, 2.85          # tile centre y, height, width
A1_NAMES = ["ASKED", "DID", "REPORTED", "STATE"]


def a1_hospital(cx, cy, s=1.0, color=INK, sw=5, fill=True):
    """A hospital outline: body, plus-sign, door. Filled with the stage colour so ghost copies behind it hide."""
    w, h = 2.4 * s, 1.9 * s
    by = cy - 0.2 * s
    body = Rectangle(width=w, height=h, stroke_color=color, stroke_width=sw,
                     fill_color=STAGE, fill_opacity=1 if fill else 0).move_to([cx, by, 0])
    c, a = 0.34 * s, 0.12 * s
    ccy = by + 0.3 * s
    pts = [(-a, c), (a, c), (a, a), (c, a), (c, -a), (a, -a), (a, -c), (-a, -c), (-a, -a), (-c, -a), (-c, a), (-a, a)]
    cross = Polygon(*[[cx + px, ccy + py, 0] for px, py in pts], stroke_color=color, stroke_width=sw - 1, fill_opacity=0)
    door = Rectangle(width=0.5 * s, height=0.62 * s, stroke_color=color, stroke_width=sw - 1,
                     fill_opacity=0).move_to([cx, by - h / 2 + 0.31 * s, 0])
    return VGroup(body, cross, door)


def a1_env(cx, cy, w=1.5, h=1.0, color=INK):
    """An envelope outline (rectangle + V flap) and, separately, the terracotta dot that is the secret."""
    rect = Rectangle(width=w, height=h, stroke_color=color, stroke_width=5, fill_opacity=0).move_to([cx, cy, 0])
    f1 = Line([cx - w / 2, cy + h / 2, 0], [cx, cy + 0.08, 0], color=color, stroke_width=5)
    f2 = Line([cx + w / 2, cy + h / 2, 0], [cx, cy + 0.08, 0], color=color, stroke_width=5)
    dot = Dot([cx, cy - 0.24, 0], radius=0.11, color=TERRA)
    return VGroup(rect, f1, f2), dot


def a1_tiles(strong=()):
    """The four tiles: (outline, header) pairs. Outline-only, header in ink."""
    out = []
    for x, n in zip(A1_XS, A1_NAMES):
        box = RoundedRectangle(width=A1_TW, height=A1_TH, corner_radius=0.2, fill_opacity=0,
                               stroke_color=INK if n in strong else DIM, stroke_width=5).move_to([x, A1_TY, 0])
        hd = T(n, 34, INK, True).move_to([x, A1_TY + A1_TH / 2 - 0.45, 0])
        out.append((box, hd))
    return out


def a1_body(x, s, y=A1_TY - 0.2, size=40):
    """Centered multi-line tile text: one Text per line (Text() left-aligns its lines)."""
    ls = s.split("\n")
    g = VGroup(*[T(l, size).move_to([x, y + (len(ls) - 1) * 0.3 - i * 0.6, 0]) for i, l in enumerate(ls)])
    return g


def a1_dot_grid(cx, cy, cols, rows, sp, r, color=BAR1):
    dots = VGroup()
    x0 = cx - (cols - 1) * sp / 2
    y0 = cy + (rows - 1) * sp / 2
    for j in range(rows):
        for i in range(cols):
            dots.add(Dot([x0 + i * sp, y0 - j * sp, 0], radius=r, color=color))
    return dots


# ── B01 · a model in hundreds of hospitals, then 27,697 patients ──────────────────────────────────────────────
class B01_Hospitals(Scene):
    def construct(self):
        g2 = a1_hospital(-3.2, 0.45, 1.0, GHOST, 4)
        g1 = a1_hospital(-3.7, 0.2, 1.0, GHOST, 4)
        h = a1_hospital(-4.2, -0.05, 1.0, INK, 5)
        lab = T("sepsis model", 38).move_to([-3.2, -1.95, 0])
        self.add(h, lab)
        until(self, "hundreds of American hospitals", lead=0.2)
        self.add(g1, g2)
        g2.set_z_index(-2); g1.set_z_index(-1)
        self.play(FadeIn(g1), FadeIn(g2), run_time=0.5)
        until(self, "Then researchers", lead=0.4)
        frame = RoundedRectangle(width=5.5, height=3.2, corner_radius=0.2, fill_opacity=0, stroke_color=DIM,
                                 stroke_width=5).move_to([2.35, -0.1, 0])
        self.play(Create(frame), run_time=0.5)
        until(self, "checked it against", lead=0.3)
        dots = a1_dot_grid(2.35, -0.1, 16, 9, 0.3, 0.09)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.012, run_time=1.4))
        until(self, "twenty-seven thousand", lead=0.2)
        num = T("27,697 patients", 62).move_to([2.35, 2.45, 0])
        self.play(FadeIn(num), run_time=0.4)
        done(self)


# ── B02 · 1,709 of 2,552 ghosted; 6,971 of 38,455 alerts ──────────────────────────────────────────────────────
class B02_Missed(Scene):
    def construct(self):
        grid = a1_dot_grid(-3.5, 0.0, 10, 10, 0.34, 0.12)
        top = T("2,552 sepsis patients", 38).move_to([-3.5, 2.5, 0])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in grid], lag_ratio=0.008, run_time=0.9), FadeIn(top))
        until(self, "two of every three", lead=0.3)
        rng = np.random.RandomState(7)
        idx = list(rng.permutation(100)[:67])
        missed = [grid[i] for i in idx]
        self.play(AnimationGroup(*[d.animate.set_fill(BAR1, 0).set_stroke(DIM, 3) for d in missed], lag_ratio=0.01, run_time=1.0))
        until(self, "one thousand, seven hundred nine", lead=0.2)
        ml = T("1,709 missed · 67%", 38).move_to([-3.5, -2.2, 0])
        self.play(FadeIn(ml), run_time=0.4)
        until(self, "And it raised alerts", lead=0.5)
        bar = Rectangle(width=5.4, height=0.7, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([3.2, 0.5, 0])
        bl = T("38,455 hospitalizations", 36).move_to([3.2, 1.45, 0])
        self.play(Create(bar), FadeIn(bl), run_time=0.5)
        until(self, "eighteen percent", lead=0.4)
        part = Rectangle(width=0.97, height=0.7, stroke_width=0, fill_color=BAR1, fill_opacity=1).move_to([0.5 + 0.485, 0.5, 0])
        pl = T("6,971 alerts · 18%", 38).move_to([2.55, -0.5, 0])
        self.play(GrowFromEdge(part, LEFT), FadeIn(pl), run_time=0.6)
        done(self)


# ── B03 · two columns: the builders' measures vs the bedside ──────────────────────────────────────────────────
class B03_Measures(Scene):
    def construct(self):
        div = Line([0, -2.7, 0], [0, 2.7, 0], color=DIM, stroke_width=4)
        h1 = T("Builders' measures", 40).move_to([-3.1, 2.45, 0])
        h2 = T("At  the bedside", 40).move_to([3.1, 2.45, 0])
        self.add(div, h1, h2)
        rows = ["validated", "published", "cleared"]
        for i, r in enumerate(rows):
            y = 1.1 - i * 1.15
            lab = T(r, 40).move_to([-4.0, y, 0])
            ck = check(-1.75, y, 0.24, INK, 8)
            self.play(FadeIn(lab), Create(ck), run_time=0.45)
        until(self, "valid by the tests they chose", lead=0.2)
        dots = VGroup(*[Dot([x, 0.9, 0], radius=0.3, color=BAR1) for x in (2.0, 3.1, 4.2)])
        self.play(FadeIn(dots), run_time=0.4)
        until(self, "wrong about the question", lead=0.3)
        self.play(dots[0].animate.set_fill(BAR1, 0).set_stroke(DIM, 5), dots[1].animate.set_fill(BAR1, 0).set_stroke(DIM, 5),
                  run_time=0.6)
        until(self, "which patient is getting sicker", lead=0.8)
        ml = T("missed 2 of 3", 46).move_to([3.1, -0.35, 0])
        self.play(FadeIn(ml), run_time=0.4)
        done(self)


# ── B04 · an agent, a mailbox and a delete request ────────────────────────────────────────────────────────────
class B04_Request(Scene):
    def construct(self):
        chip = Square(side_length=1.5, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([-0.3, 0.2, 0])
        pins = VGroup()
        for k in (-0.4, 0.0, 0.4):
            pins.add(Line([-0.3 - 0.75, 0.2 + k, 0], [-0.3 - 1.1, 0.2 + k, 0], color=INK, stroke_width=6))
            pins.add(Line([-0.3 + 0.75, 0.2 + k, 0], [-0.3 + 1.1, 0.2 + k, 0], color=INK, stroke_width=6))
        core = Circle(radius=0.3, stroke_color=DIM, stroke_width=5).move_to([-0.3, 0.2, 0])
        al = T("agent", 42).move_to([-0.3, -1.3, 0])
        self.add(chip, pins, core, al)
        until(self, "Agents of Chaos", lead=0.6)
        cap = T("Agents of Chaos · Shapira et al., 2026", 32).move_to([0, -3.0, 0])
        self.play(FadeIn(cap), run_time=0.5)
        until(self, "asked an agent", lead=0.3)
        tile = RoundedRectangle(width=2.5, height=1.0, corner_radius=0.2, stroke_color=INK, stroke_width=5,
                                fill_opacity=0).move_to([-4.7, 0.2, 0])
        tt = T("delete", 40).move_to([-4.7, 0.2, 0])
        rl = T("request", 34).move_to([-4.7, 1.15, 0])
        a1 = Arrow([-3.4, 0.2, 0], [-1.7, 0.2, 0], buff=0, color=INK, stroke_width=5, tip_length=0.22)
        self.play(FadeIn(tile), FadeIn(tt), FadeIn(rl), Create(a1), run_time=0.7)
        until(self, "named Ash", lead=0.2)
        ash = T("Ash", 46).move_to([-0.3, -1.3, 0])
        self.play(FadeOut(al), FadeIn(ash), run_time=0.4)
        until(self, "delete an email", lead=0.3)
        env, dot = a1_env(4.5, 0.2)
        el = T("secret email", 38).move_to([4.5, -1.3, 0])
        a2 = Arrow([1.25, 0.2, 0], [3.55, 0.2, 0], buff=0, color=INK, stroke_width=5, tip_length=0.22)
        self.play(Create(env), FadeIn(el), Create(a2), run_time=0.7)
        until(self, "held a secret", lead=0.3)
        self.play(GrowFromCenter(dot), run_time=0.35)
        done(self)


# ── B05 · ASKED / DID / REPORTED, the reset and the report ────────────────────────────────────────────────────
class B05_Report(Scene):
    def construct(self):
        tiles = a1_tiles()
        for box, hd in tiles:
            self.add(box, hd)
        ask = a1_body(A1_XS[0], "delete\nemail")
        self.add(ask)
        slot = Rectangle(width=0.8, height=0.8, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([-5.3, -2.2, 0])
        x1 = Line([-5.6, -1.9, 0], [-5.0, -2.5, 0], color=DIM, stroke_width=5)
        x2 = Line([-5.6, -2.5, 0], [-5.0, -1.9, 0], color=DIM, stroke_width=5)
        sl = T("no delete tool", 34).move_to([-3.3, -2.2, 0])
        self.play(FadeIn(slot), Create(x1), Create(x2), FadeIn(sl), run_time=0.6)
        until(self, "reset its own local email setup", lead=0.4)
        did = a1_body(A1_XS[1], "local\nreset")
        self.play(FadeIn(did), tiles[1][0].animate.set_stroke(INK, 5), run_time=0.5)
        until(self, "and reported", lead=0.3)
        rep = a1_body(A1_XS[2], "reset\ncompleted", y=A1_TY + 0.05)
        quote = T("“Email account RESET completed.”", 32).move_to([3.0, -2.25, 0])
        self.play(FadeIn(rep), FadeIn(quote), tiles[2][0].animate.set_stroke(INK, 5), run_time=0.5)
        until(self, "claimed the secret", lead=0.3)
        ck = check(A1_XS[2], A1_TY - 0.75, 0.24, INK, 8)
        self.play(Create(ck), run_time=0.4)
        done(self)


# ── B06 · the real mailbox still holds the email: report and state disagree ───────────────────────────────────
class B06_State(Scene):
    def construct(self):
        tiles = a1_tiles()
        for box, hd in tiles:
            self.add(box, hd)
        ask = a1_body(A1_XS[0], "delete\nemail")
        did = a1_body(A1_XS[1], "local\nreset")
        rep = a1_body(A1_XS[2], "reset\ncompleted", y=A1_TY + 0.05)
        ck = check(A1_XS[2], A1_TY - 0.75, 0.24, INK, 8)
        for b in (0, 1, 2):
            tiles[b][0].set_stroke(INK, 5)
        self.add(ask, did, rep, ck)
        until(self, "the real mailbox", lead=0.3)
        self.play(tiles[3][0].animate.set_stroke(INK, 5), run_time=0.4)
        ml = T("mail server", 34).move_to([A1_XS[3], -1.65, 0])
        self.play(FadeIn(ml), run_time=0.3)
        until(self, "the email was still there", lead=1.3)
        env, dot = a1_env(A1_XS[3], A1_TY + 0.3, 1.4, 0.95)
        st = T("still there", 38).move_to([A1_XS[3], A1_TY - 0.65, 0])
        self.play(Create(env), FadeIn(st), run_time=0.5)
        self.play(GrowFromCenter(dot), run_time=0.3)
        until(self, "and false about the world", lead=0.5)
        arr = dim_arrow([A1_XS[2], -2.3, 0], [A1_XS[3], -2.3, 0])
        ne = T("≠", 54).move_to([(A1_XS[2] + A1_XS[3]) / 2, -2.85, 0])
        self.play(Create(arr), FadeIn(ne), run_time=0.5)
        self.play(Indicate(ne, scale_factor=1.25, color=INK), run_time=0.6)
        done(self)


# ── B07 · the composite patient: a chart, a score tag, a wait, a clot ─────────────────────────────────────────
class B07_Composite(Scene):
    def construct(self):
        board = Rectangle(width=2.2, height=3.1, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([-4.8, -0.2, 0])
        clip = Rectangle(width=0.9, height=0.34, stroke_color=INK, stroke_width=5, fill_color=STAGE, fill_opacity=1).move_to([-4.8, 1.37, 0])
        rows = VGroup(*[Line([-5.55, 0.6 - i * 0.6, 0], [-4.05, 0.6 - i * 0.6, 0], color=DIM, stroke_width=5) for i in range(4)])
        cl = T("composite patient", 36).move_to([-3.7, 2.45, 0])
        self.add(board, clip, rows, cl)
        # the vessel: leg (bottom) to lung (top)
        vessel = Line([3.6, -1.25, 0], [3.6, 1.3, 0], color=DIM, stroke_width=7)
        leg = RoundedRectangle(width=1.0, height=1.1, corner_radius=0.25, stroke_color=INK, stroke_width=5,
                               fill_opacity=0).move_to([3.6, -1.85, 0])
        lung = Ellipse(width=1.9, height=1.2, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([3.6, 1.9, 0])
        leg_l = T("leg", 36).move_to([5.1, -1.85, 0])
        lung_l = T("lung", 36).move_to([5.2, 1.9, 0])
        until(self, "She is a composite", lead=0.3)
        self.play(FadeIn(leg), FadeIn(lung), Create(vessel), FadeIn(leg_l), FadeIn(lung_l), run_time=0.7)
        clot = Dot([3.6, -1.85, 0], radius=0.16, color=TERRA)
        clot_l = T("clot", 36).move_to([2.2, -1.85, 0])
        self.play(GrowFromCenter(clot), FadeIn(clot_l), run_time=0.4)
        until(self, "forty-nine-year-old", lead=0.2)
        age = T("49 years", 40).move_to([-1.8, 1.55, 0])
        self.play(FadeIn(age), run_time=0.35)
        until(self, "swollen leg", lead=0.2)
        sw = T("swollen leg", 40).move_to([-1.8, 0.75, 0])
        self.play(FadeIn(sw), run_time=0.35)
        until(self, "scores her low-acuity", lead=0.3)
        tag = RoundedRectangle(width=3.7, height=0.85, corner_radius=0.2, stroke_color=INK, stroke_width=5,
                               fill_opacity=0).move_to([-1.8, -0.3, 0])
        tgt = T("LOW-ACUITY", 36, INK, True).move_to([-1.8, -0.3, 0])
        self.play(FadeIn(VGroup(tag, tgt), shift=DOWN * 0.3), run_time=0.45)
        until(self, "She waits", lead=0.1)
        clk = Circle(radius=0.55, stroke_color=INK, stroke_width=5).move_to([-2.5, -1.75, 0])
        hand = Line([-2.5, -1.75, 0], [-2.5, -1.35, 0], color=INK, stroke_width=6)
        hand2 = Line([-2.5, -1.75, 0], [-2.15, -1.75, 0], color=INK, stroke_width=6)
        wl = T("waits", 38).move_to([-1.05, -1.75, 0])
        self.play(Create(clk), Create(hand), Create(hand2), FadeIn(wl), run_time=0.5)
        self.play(Rotate(hand, angle=-PI, about_point=np.array([-2.5, -1.75, 0])), run_time=0.6)
        until(self, "moves to her lung", lead=0.5)
        self.play(clot.animate.move_to([3.6, 1.55, 0]), run_time=1.0)
        done(self)


# ── B08 · VALID vs RIGHT: two circles that do not coincide ────────────────────────────────────────────────────
class B08_ValidRight(Scene):
    def construct(self):
        valid = Circle(radius=1.7, stroke_color=INK, stroke_width=6).move_to([0, 0, 0])
        right = Circle(radius=1.7, stroke_color=DIM, stroke_width=6).move_to([0, 0, 0])
        target = Dot([0, 0, 0], radius=0.14, color=TERRA)
        vl = T("valid", 46).move_to([0, 2.45, 0])
        rl = T("right", 46).move_to([0, -2.45, 0])
        self.add(right, valid, vl, rl, target)
        self.wait(0.4)
        until(self, "and wrong about", lead=0.2)
        self.play(VGroup(valid, vl).animate.shift(LEFT * 3.1),
                  VGroup(right, target).animate.shift(RIGHT * 3.1),
                  rl.animate.move_to([3.1, 2.45, 0]), run_time=0.9)
        until(self, "That gap", lead=0.3)
        arr = dim_arrow([-1.4, 0, 0], [1.4, 0, 0])
        gl = T("gap", 40).move_to([0, 0.55, 0])
        self.play(Create(arr), FadeIn(gl), run_time=0.6)
        until(self, "tools to see", lead=0.9)
        self.play(Indicate(VGroup(arr, gl), scale_factor=1.15, color=INK), run_time=0.8)
        done(self)
