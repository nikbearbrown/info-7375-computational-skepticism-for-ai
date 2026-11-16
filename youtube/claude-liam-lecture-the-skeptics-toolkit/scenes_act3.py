"""GROUP 3 · Acts III-IV  (B18–B27, all Manim)

Cast for these ten beats: the CHECK MARK (ink, drawn with two lines), outlined round tiles, the circle (model / world),
the swan (built from an ellipse, a bezier neck, a small circle and a triangle), and ONE terracotta dot that marks the thing
the voice is pointing at. No person tokens anywhere. Numbers on screen are the verified ones in factcheck/PRIMARIES.md;
anything else is labelled schematic / illustrative.
"""

A3_FRAME_NOTE = "x in +-6.2, y in +-3.3"


def a3_swan(cx, cy, s=1.0, black=False):
    """A swan from primitives: ellipse body, bezier neck, circle head, triangle beak and tail. (cx, cy) = body centre."""
    fill = INK if black else CARD
    body = Ellipse(width=0.95 * s, height=0.46 * s, fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4)
    body.move_to([cx, cy, 0])
    neck = CubicBezier(np.array([cx + 0.30 * s, cy + 0.10 * s, 0]), np.array([cx + 0.62 * s, cy + 0.20 * s, 0]),
                       np.array([cx + 0.05 * s, cy + 0.48 * s, 0]), np.array([cx + 0.40 * s, cy + 0.72 * s, 0]))
    neck.set_stroke(INK, 7 if not black else 8).set_fill(opacity=0)
    head = Circle(radius=0.085 * s, fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx + 0.43 * s, cy + 0.74 * s, 0])
    beak = Polygon([cx + 0.50 * s, cy + 0.79 * s, 0], [cx + 0.50 * s, cy + 0.69 * s, 0], [cx + 0.68 * s, cy + 0.73 * s, 0],
                   fill_color=INK, fill_opacity=1, stroke_width=0)
    tail = Polygon([cx - 0.40 * s, cy + 0.02 * s, 0], [cx - 0.62 * s, cy + 0.22 * s, 0], [cx - 0.36 * s, cy + 0.14 * s, 0],
                   fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=3)
    return VGroup(tail, body, neck, head, beak)


def a3_turkey(cx, cy, s=1.0):
    """A turkey from primitives: round body, tail fan of three arcs, small head, beak, two legs."""
    body = Circle(radius=0.38 * s, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    fan = VGroup(*[Arc(radius=(0.52 + 0.14 * k) * s, start_angle=PI * 0.62, angle=PI * 0.76, arc_center=[cx, cy, 0],
                       stroke_color=INK if k == 0 else DIM, stroke_width=4) for k in range(3)])
    head = Circle(radius=0.14 * s, fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx + 0.52 * s, cy + 0.3 * s, 0])
    beak = Polygon([cx + 0.64 * s, cy + 0.36 * s, 0], [cx + 0.64 * s, cy + 0.24 * s, 0], [cx + 0.82 * s, cy + 0.3 * s, 0],
                   fill_color=INK, fill_opacity=1, stroke_width=0)
    legs = VGroup(Line([cx - 0.1 * s, cy - 0.38 * s, 0], [cx - 0.1 * s, cy - 0.72 * s, 0], color=INK, stroke_width=4),
                  Line([cx + 0.12 * s, cy - 0.38 * s, 0], [cx + 0.12 * s, cy - 0.72 * s, 0], color=INK, stroke_width=4))
    return VGroup(fan, legs, body, head, beak)


# ── B18 · Hume: checks accumulate, 'guarantee' stays at zero, the world quietly does some of the work ──────────────────
class B18_Hume(Scene):
    def construct(self):
        title = T("Hume", 40).move_to([-4.6, 2.9, 0])
        self.add(title)
        until(self, "A model that has been right", lead=1.0)
        cols, rows = 8, 4
        marks = VGroup(*[check(-5.2 + i * 0.5, 1.95 - j * 0.5, s=0.16, color=INK, w=6) for j in range(rows) for i in range(cols)])
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.06), run_time=1.9)
        until(self, "no logical guarantee", lead=1.0)
        gl = T("guarantee", 44).move_to([3.4, 1.9, 0])
        zero = T("0", 150).move_to([3.4, 0.35, 0])
        self.play(FadeIn(gl), GrowFromCenter(zero), run_time=0.7)
        until(self, "The world was doing", lead=0.3)
        world = Circle(radius=0.8, stroke_color=INK, stroke_width=5).move_to([-3.4, -2.05, 0])
        wl = T("world", 40).move_to([-1.3, -2.05, 0])
        ups = VGroup(*[Arrow([x, -1.2, 0], [x, -0.1, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18) for x in (-4.3, -3.4, -2.5)])
        self.play(Create(world), FadeIn(wl), run_time=0.6)
        self.play(LaggedStart(*[Create(a) for a in ups], lag_ratio=0.3), run_time=0.8)
        until(self, "until it stopped", lead=0.2)
        dot = Dot([-3.4, -2.05, 0], radius=0.1, color=TERRA)
        self.play(FadeOut(ups), FadeIn(dot), run_time=0.6)
        done(self)


# ── B19 · the turkey: day counter to 1,000, confidence curve rises, then 1,001 and the axe ─────────────────────────────
class B19_Turkey(Scene):
    def construct(self):
        ox, oy = -4.5, -2.2
        y_ax = Arrow([ox, oy, 0], [ox, 1.4, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        x_ax = Arrow([ox, oy, 0], [5.0, oy, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        conf = T("confidence", 38).move_to([-2.9, 1.65, 0])
        sch = T("schematic", 32, DIM).move_to([4.5, -2.8, 0])
        turkey = a3_turkey(-5.2, 2.35, 0.9)
        day = T("day", 44).move_to([1.6, 2.3, 0])
        vt = ValueTracker(1)
        counter = always_redraw(lambda: T(f"{int(round(vt.get_value())):,}", 84).move_to([4.15, 2.3, 0]))
        self.add(y_ax, x_ax, conf, sch, turkey, day, counter)
        pts = [np.array([ox + 0.0 + 7.5 * k / 40, oy + 3.3 * (1 - np.exp(-(7.5 * k / 40) / 2.2)), 0.0]) for k in range(41)]
        curve = VMobject(color=INK, stroke_width=7).set_points_smoothly(pts)
        dot = Dot(pts[0], radius=0.12, color=TERRA)
        self.add(dot)
        until(self, "fed every morning", lead=0.6)
        self.play(Create(curve), MoveAlongPath(dot, curve), vt.animate.set_value(1000), run_time=3.2, rate_func=linear)
        until(self, "the farmer comes", lead=0.9)
        self.play(vt.animate.set_value(1001), run_time=0.2)
        handle = Line([3.7, -0.75, 0], [4.45, 0.35, 0], color=INK, stroke_width=7)
        head = Polygon([4.28, 0.2, 0], [4.62, 0.62, 0], [4.05, 0.85, 0], [3.8, 0.45, 0], fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4)
        axe = VGroup(handle, head)
        self.play(FadeIn(axe, shift=DOWN * 0.5), run_time=0.4)
        drop = Line(pts[-1], [pts[-1][0], oy, 0], color=INK, stroke_width=7)
        self.play(Create(drop), dot.animate.move_to([pts[-1][0], oy, 0]), run_time=0.5)
        done(self)


# ── B20 · correlation line over a hidden mechanism that flips ──────────────────────────────────────────────────────────
class B20_Mechanism(Scene):
    def construct(self):
        ox, oy = -5.6, -2.4
        y_ax = Arrow([ox, oy, 0], [ox, 1.9, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        x_ax = Arrow([ox, oy, 0], [-0.7, oy, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        self.add(y_ax, x_ax)
        line = Line([-5.0, -1.9, 0], [-1.4, 1.2, 0], color=BAR1, stroke_width=6)
        jit = [0.12, -0.1, 0.08, -0.14, 0.1, -0.06, 0.13, -0.1, 0.05]
        dots = VGroup(*[Dot([-5.0 + 3.6 * t, -1.9 + 3.1 * t + jit[i], 0], radius=0.1, color=INK) for i, t in enumerate(np.linspace(0, 1, 9))])
        self.play(Create(line), LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.12), run_time=1.6)
        until(self, "It knew the correlation", lead=0.2)
        cl = T("correlation", 40).move_to([-3.2, 2.55, 0])
        self.play(FadeIn(cl), run_time=0.4)
        until(self, "not the mechanism", lead=0.9)
        cx, cy = 3.2, 0.3
        blk = DashedVMobject(RoundedRectangle(width=2.6, height=2.6, corner_radius=0.2, stroke_color=DIM, stroke_width=5), num_dashes=40).move_to([3.2, 0.3, 0])
        ml = T("mechanism", 40).move_to([3.2, 2.2, 0])
        pivot = Dot([cx, cy, 0], radius=0.12, color=INK)
        lever = Line([cx, cy, 0], [cx - 0.85, cy + 0.65, 0], color=DIM, stroke_width=7)
        self.play(Create(blk), FadeIn(ml), Create(lever), FadeIn(pivot), run_time=0.8)
        until(self, "the mechanism changed", lead=0.3)
        solid = RoundedRectangle(width=2.6, height=2.6, corner_radius=0.2, stroke_color=INK, stroke_width=5).move_to([cx, cy, 0])
        targets = [-0.15, -0.5, -0.4, -1.1, -0.9, -1.6, -1.4, -2.0, -2.3]
        self.play(Rotate(lever, angle=PI, about_point=np.array([cx, cy, 0])), FadeIn(solid), run_time=0.9)
        self.play(*[d.animate.shift(DOWN * (-g) * 0.9) for d, g in zip(dots, targets)], run_time=0.9)
        ml2 = T("model", 38).move_to([-0.35, 1.45, 0])
        self.play(FadeIn(ml2), run_time=0.3)
        until(self, "is that turkey", lead=0.9)
        tk = a3_turkey(4.6, -2.0, 0.85)
        self.play(FadeIn(tk), run_time=0.5)
        done(self)


# ── B21 · Zillow: two bars and a quarter of the staff ─────────────────────────────────────────────────────────────────
class B21_Zillow(Scene):
    def construct(self):
        base_y, k = -1.9, 0.0095
        title = T("Zillow", 40).move_to([-4.7, 2.85, 0])
        cap = T("per Zillow 8-K, Nov 2021", 32, DIM).move_to([3.9, -2.85, 0])
        self.add(title, cap)
        ground = Line([-6.0, base_y, 0], [0.2, base_y, 0], color=DIM, stroke_width=4)
        self.play(Create(ground), run_time=0.3)
        until(self, "three hundred four", lead=1.4)
        h1 = 304.4 * k
        b1 = Rectangle(width=1.4, height=h1, fill_color=BAR1, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-4.7, base_y + h1 / 2, 0])
        n1 = T("$304.4M", 42).move_to([-4.7, base_y + h1 + 0.5, 0])
        l1 = T("Q3\nwrite-down", 32).move_to([-4.7, base_y - 0.65, 0])
        self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=0.7)
        self.play(FadeIn(n1), run_time=0.3)
        until(self, "expected more than", lead=0.5)
        h2, h2x = 240 * k, 25 * k
        b2 = Rectangle(width=1.4, height=h2, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-1.6, base_y + h2 / 2, 0])
        b2x = DashedVMobject(Rectangle(width=1.4, height=h2x, stroke_color=INK, stroke_width=4), num_dashes=16).move_to([-1.6, base_y + h2 + h2x / 2, 0])
        n2 = T("$240–265M", 42).move_to([-1.6, base_y + h2 + h2x + 0.5, 0])
        l2 = T("expected\nQ4 charges", 32).move_to([-1.6, base_y - 0.65, 0])
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=0.7)
        self.play(Create(b2x), FadeIn(n2), run_time=0.5)
        until(self, "about a quarter", lead=0.9)
        sq = VGroup(*[RoundedRectangle(width=0.9, height=0.9, corner_radius=0.12, stroke_color=INK, stroke_width=5).move_to([1.9 + 1.2 * i, 0.9, 0])
                      for i in range(4)])
        self.play(LaggedStart(*[Create(s) for s in sq], lag_ratio=0.25), run_time=0.9)
        cross = VGroup(Line([5.15, 0.6, 0], [5.85, 1.2, 0], color=INK, stroke_width=5), Line([5.15, 1.2, 0], [5.85, 0.6, 0], color=INK, stroke_width=5))
        self.play(sq[3].animate.set_fill(GHOST, 1), Create(cross), run_time=0.5)
        pc = T("25% of staff", 40).move_to([3.7, -0.55, 0])
        self.play(FadeIn(pc), run_time=0.4)
        done(self)


# ── B22 · Google Flu Trends: 108 week tiles, 100 filled ───────────────────────────────────────────────────────────────
class B22_FluTiles(Scene):
    def construct(self):
        cols, rows, sp = 18, 6, 0.4
        gx, gy = -5.3, 1.9
        empty = set([4, 17, 29, 41, 52, 66, 79, 94])     # 8 weeks that were not too high: tile order is schematic
        tiles = []
        for n in range(108):
            r, c = divmod(n, cols)
            t = RoundedRectangle(width=0.32, height=0.32, corner_radius=0.06, stroke_color=DIM, stroke_width=3).move_to([gx + c * sp, gy - r * sp, 0])
            tiles.append(t)
        title = T("Flu Trends", 40).move_to([-4.6, 2.9, 0])
        cap = T("Lazer et al., Science, 2014", 32, DIM).move_to([3.9, -2.8, 0])
        sch = T("tile order schematic", 32, DIM).move_to([-3.2, -1.05, 0])
        self.add(title, cap)
        until(self, "From August", lead=0.9)
        self.play(LaggedStart(*[Create(t) for t in tiles], lag_ratio=0.012), FadeIn(sch), run_time=1.6)
        until(self, "a hundred of a hundred", lead=1.5)
        fills = [t.animate.set_fill(BAR1, 1).set_stroke(INK, 3) for n, t in enumerate(tiles) if n not in empty]
        self.play(LaggedStart(*fills, lag_ratio=0.012), run_time=1.5)
        n100 = T("100", 120).move_to([3.7, 1.55, 0])
        of = T("of 108 weeks", 40).move_to([3.7, 0.35, 0])
        hi = T("too high", 40).move_to([3.7, -0.4, 0])
        self.play(GrowFromCenter(n100), FadeIn(of), FadeIn(hi), run_time=0.6)
        until(self, "big data hubris", lead=0.4)
        q = T("“big data hubris”", 46).move_to([-2.6, -2.1, 0])
        dot = Dot([-5.35, -2.1, 0], radius=0.11, color=TERRA)
        self.play(FadeIn(q), FadeIn(dot), run_time=0.6)
        done(self)


# ── B23 · confidence belongs to the model; the arrow only runs one way; the supervisor's check ─────────────────────────
class B23_OneWay(Scene):
    def construct(self):
        model = Circle(radius=1.15, stroke_color=INK, stroke_width=5).move_to([-3.4, 0.7, 0])
        world = Circle(radius=1.15, stroke_color=INK, stroke_width=5).move_to([3.4, 0.7, 0])
        ml = T("model", 40).move_to([-3.4, 0.7, 0])
        wl = T("world", 40).move_to([3.4, 0.7, 0])
        cf = T("confidence", 38).move_to([-3.4, 2.3, 0])
        cdot = Dot([-3.4, 1.2, 0], radius=0.1, color=TERRA)
        self.add(model, ml)
        self.play(FadeIn(cf), FadeIn(cdot), run_time=0.5)
        until(self, "not to the world", lead=0.5)
        self.play(Create(world), FadeIn(wl), run_time=0.5)
        fwd = Arrow([-2.15, 1.0, 0], [2.15, 1.0, 0], buff=0, color=INK, stroke_width=6, tip_length=0.25)
        self.play(Create(fwd), run_time=0.5)
        until(self, "owes the model nothing", lead=0.5)
        back = DashedLine([2.15, 0.4, 0], [-2.15, 0.4, 0], color=DIM, stroke_width=5, dash_length=0.2)
        tip = Triangle(fill_color=DIM, fill_opacity=1, stroke_width=0).scale(0.14).rotate(PI / 6).move_to([-2.25, 0.4, 0])
        xm = VGroup(Line([-0.2, 0.22, 0], [0.2, 0.58, 0], color=INK, stroke_width=6), Line([-0.2, 0.58, 0], [0.2, 0.22, 0], color=INK, stroke_width=6))
        self.play(Create(back), FadeIn(tip), Create(xm), run_time=0.7)
        until(self, "cannot tell when", lead=0.6)
        ring = Circle(radius=1.5, stroke_color=DIM, stroke_width=4).move_to([3.4, 0.7, 0])
        self.play(Create(ring), run_time=0.5)
        until(self, "Only the supervisor", lead=0.3)
        br = VGroup(Line([-3.4, -0.7, 0], [-3.4, -1.3, 0], color=INK, stroke_width=5), Line([-3.4, -1.3, 0], [3.4, -1.3, 0], color=INK, stroke_width=5),
                    Line([3.4, -1.3, 0], [3.4, -0.7, 0], color=INK, stroke_width=5))
        ck = check(0.0, -1.3, s=0.3, color=INK, w=9)
        sup = T("supervisor", 44).move_to([0, -2.4, 0])
        self.play(Create(br), run_time=0.6)
        self.play(Create(ck), FadeIn(sup), run_time=0.5)
        done(self)


# ── B24 · a claim card with three blanks: metric, threshold, window ───────────────────────────────────────────────────
class B24_Blanks(Scene):
    def construct(self):
        card = RoundedRectangle(width=4.6, height=1.3, corner_radius=0.25, stroke_color=DIM, stroke_width=5).move_to([-3.0, 2.0, 0])
        ct = T("performs well", 42).move_to([-3.0, 2.0, 0])
        self.add(card, ct)
        until(self, "what would performing badly", lead=1.5)
        twin = DashedVMobject(RoundedRectangle(width=4.6, height=1.3, corner_radius=0.25, stroke_color=DIM, stroke_width=5), num_dashes=44).move_to([3.0, 2.0, 0])
        tt = T("performs badly?", 42, DIM).move_to([3.0, 2.0, 0])
        self.play(Create(twin), FadeIn(tt), run_time=0.7)
        until(self, "On which metric", lead=0.3)
        xs = [-4.1, 0.0, 4.1]
        slots = VGroup(*[RoundedRectangle(width=3.2, height=1.9, corner_radius=0.2, stroke_color=DIM, stroke_width=4).move_to([x, -0.6, 0]) for x in xs])
        names = VGroup(*[T(w, 40).move_to([x, -2.2, 0]) for w, x in zip(["metric", "threshold", "window"], xs)])
        self.play(LaggedStart(*[Create(s) for s in slots], lag_ratio=0.2), FadeIn(names), run_time=0.8)
        # glyphs fill the blanks one by one
        bars = VGroup(*[Rectangle(width=0.32, height=h, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([xs[0] - 0.55 + 0.55 * i, -0.6 - 0.8 + h / 2, 0])
                        for i, h in enumerate([0.6, 1.1, 0.8])])
        wave = VMobject(color=DIM, stroke_width=5).set_points_smoothly([np.array([xs[1] - 1.2 + 0.4 * i, -0.65 + 0.45 * np.sin(i * 0.9), 0]) for i in range(7)])
        thr = Line([xs[1] - 1.3, -0.35, 0], [xs[1] + 1.3, -0.35, 0], color=INK, stroke_width=5)
        brk = VGroup(Line([xs[2] - 1.2, -0.3, 0], [xs[2] - 1.2, -0.9, 0], color=INK, stroke_width=5), Line([xs[2] + 1.2, -0.3, 0], [xs[2] + 1.2, -0.9, 0], color=INK, stroke_width=5),
                     Line([xs[2] - 1.2, -0.6, 0], [xs[2] + 1.2, -0.6, 0], color=INK, stroke_width=5),
                     *[Line([xs[2] - 0.8 + 0.4 * i, -0.75, 0], [xs[2] - 0.8 + 0.4 * i, -0.45, 0], color=DIM, stroke_width=4) for i in range(5)])
        dot = Dot([xs[0], -0.6, 0], radius=0.1, color=TERRA)
        until(self, "past what threshold", lead=1.2)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.2), FadeIn(dot), run_time=0.6)
        until(self, "past what threshold", lead=-0.1)
        self.play(dot.animate.move_to([xs[1], 0.0, 0]), Create(wave), run_time=0.5)
        self.play(Create(thr), run_time=0.3)
        until(self, "over what window", lead=0.3)
        self.play(dot.animate.move_to([xs[2], 0.0, 0]), Create(brk), run_time=0.5)
        done(self)


# ── B25 · white swans accumulate; one black swan ends the claim ───────────────────────────────────────────────────────
class B25_Swans(Scene):
    def construct(self):
        claim = T("all swans are white", 44).move_to([-1.2, 2.6, 0])
        self.add(claim)
        whites = VGroup()
        for j, y in enumerate([0.55, -1.1]):
            for i in range(4):
                whites.add(a3_swan(-5.0 + 1.5 * i, y, 1.0))
        until(self, "No count of white swans", lead=0.4)
        self.play(LaggedStart(*[FadeIn(w, shift=UP * 0.15) for w in whites], lag_ratio=0.25), run_time=1.6)
        until(self, "One black swan", lead=0.2)
        blk = a3_swan(3.6, -0.25, 1.5, black=True)
        self.play(GrowFromCenter(blk), run_time=0.6)
        ring = Circle(radius=1.35, stroke_color=INK, stroke_width=5).move_to([3.7, 0.0, 0])
        dot = Dot([3.7, 1.55, 0], radius=0.11, color=TERRA)
        self.play(Create(ring), FadeIn(dot), whites.animate.set_opacity(0.35), run_time=0.7)
        until(self, "trying to break it", lead=0.3)
        brk = T("break it", 44).move_to([3.7, -2.1, 0])
        self.play(FadeIn(brk), run_time=0.4)
        done(self)


# ── B26 · internal validation counts white swans; external test tries for the black one ───────────────────────────────
class B26_Unrefuted(Scene):
    def construct(self):
        mid = Line([0, 2.6, 0], [0, -1.0, 0], color=DIM, stroke_width=4)
        hl = T("internal validation", 38).move_to([-3.1, 2.7, 0])
        hr = T("external test", 38).move_to([3.1, 2.7, 0])
        self.add(mid, hl, hr)
        whites = VGroup()
        for j, y in enumerate([1.0, -0.4]):
            for i in range(3):
                whites.add(a3_swan(-4.5 + 1.6 * i, y, 0.9))
        until(self, "only ever got white-swan", lead=0.3)
        self.play(LaggedStart(*[FadeIn(w) for w in whites], lag_ratio=0.2), run_time=1.3)
        checks = VGroup(*[check(-5.3 + 1.6 * i, -1.6, s=0.17, color=INK, w=6) for i in range(3)], *[check(-5.3 + 1.6 * i, -1.6 + 0.0, s=0.0, color=INK, w=0) for i in range(0)])
        self.play(LaggedStart(*[Create(c) for c in checks], lag_ratio=0.3), run_time=0.7)
        until(self, "serious attempt", lead=0.2)
        slot = DashedVMobject(Circle(radius=1.3, stroke_color=DIM, stroke_width=5), num_dashes=30).move_to([3.1, 0.4, 0])
        q = T("?", 80, DIM).move_to([3.1, 0.4, 0])
        self.play(Create(slot), FadeIn(q), run_time=0.6)
        until(self, "another health system", lead=0.2)
        blk = a3_swan(3.1, 0.2, 1.4, black=True)
        self.play(FadeOut(q), FadeIn(blk), run_time=0.5)
        until(self, "Unrefuted is not", lead=0.3)
        eq = T("unrefuted ≠ validated", 46).move_to([0, -2.4, 0])
        self.play(FadeIn(eq), run_time=0.5)
        done(self)


# ── B27 · rewrite: the vague claim fits every outcome; the specific one names its failure ─────────────────────────────
class B27_Rewrite(Scene):
    def construct(self):
        sep = Line([-6.0, 0.35, 0], [6.0, 0.35, 0], color=DIM, stroke_width=3)
        self.add(sep)
        t1 = T("vague", 32, DIM).move_to([-4.5, 2.1, 0])
        r1 = T("robust", 50).move_to([-3.6, 1.2, 0])
        self.play(FadeIn(t1), FadeIn(r1), run_time=0.4)
        xs = [1.0 + 1.15 * i for i in range(5)]
        o1 = VGroup(*[Circle(radius=0.28, stroke_color=INK, stroke_width=4).move_to([x, 1.2, 0]) for x in xs])
        c1 = VGroup(*[check(x, 1.2, s=0.17, color=INK, w=6) for x in xs])
        until(self, "The system is robust", lead=0.2)
        self.play(LaggedStart(*[Create(o) for o in o1], lag_ratio=0.15), run_time=0.6)
        until(self, "becomes", lead=1.6)
        t2 = T("specific", 32, DIM).move_to([-4.4, -0.3, 0])
        r2 = T("error rate < 2%", 44).move_to([-3.4, -1.0, 0])
        r2b = T("over 30 days", 40).move_to([-3.4, -1.75, 0])
        self.play(FadeIn(t2), FadeIn(r2), FadeIn(r2b), run_time=0.5)
        o2 = VGroup(*[Circle(radius=0.28, stroke_color=INK, stroke_width=4).move_to([x, -1.2, 0]) for x in xs])
        self.play(LaggedStart(*[Create(o) for o in o2], lag_ratio=0.15), run_time=0.6)
        until(self, "fits any outcome", lead=0.8)
        self.play(LaggedStart(*[Create(c) for c in c1], lag_ratio=0.12), run_time=0.8)
        until(self, "names what would make it false", lead=1.2)
        keep = [0, 1, 3]
        c2 = VGroup(*[check(xs[i], -1.2, s=0.17, color=INK, w=6) for i in keep])
        fails = VGroup(*[VGroup(Line([xs[i] - 0.17, -1.37, 0], [xs[i] + 0.17, -1.03, 0], color=INK, stroke_width=7),
                                Line([xs[i] - 0.17, -1.03, 0], [xs[i] + 0.17, -1.37, 0], color=INK, stroke_width=7)) for i in (2, 4)])
        self.play(LaggedStart(*[Create(c) for c in c2], lag_ratio=0.15), run_time=0.6)
        self.play(LaggedStart(*[Create(f) for f in fails], lag_ratio=0.2), run_time=0.5)
        until(self, "illustrations", lead=0.8)
        ill = T("illustrative thresholds", 34, DIM).move_to([0, -2.85, 0])
        dot = Dot([xs[2] + 0.55, -1.2, 0], radius=0.1, color=TERRA)
        self.play(FadeIn(ill), FadeIn(dot), run_time=0.4)
        done(self)
