from manim import *
import random, math

# ─── PALETTE ──────────────────────────────────────────────────────────────────
NEO_GREEN = "#00FF41"
NEO_CYAN = "#00FFFF"
NEO_PURPLE = "#BF00FF"
NEO_YELLOW = "#FFFF00"
NEO_RED = "#FF0040"
NEO_WHITE = "#E0FFE0"
NEO_DIM = "#003B00"
NEO_ORANGE = "#FF8C00"
NEO_PINK = "#FF00AA"
BG_BLACK = "#000000"


# ─── HELPERS ──────────────────────────────────────────────────────────────────
def T(txt, sz=48, col=NEO_WHITE, bold=False):
    w = BOLD if bold else NORMAL
    return Text(txt, font="Courier New", font_size=sz, color=col, weight=w)


def hr(col=NEO_GREEN, w=11):
    return Line(LEFT * w / 2, RIGHT * w / 2, color=col, stroke_width=1.2)


def hdr(label, col=NEO_CYAN):
    t = T(label, 38, col, bold=True)
    l = hr(col, 11)
    l.next_to(t, DOWN, buff=0.1)
    return VGroup(t, l)


def glowing_border(col=NEO_GREEN):
    outer = RoundedRectangle(
        width=13.5,
        height=7.6,
        corner_radius=0.15,
        stroke_color=col,
        stroke_width=2.5,
        fill_opacity=0,
    )
    inner = RoundedRectangle(
        width=13.2,
        height=7.3,
        corner_radius=0.1,
        stroke_color=col,
        stroke_width=0.5,
        fill_opacity=0,
    )
    return VGroup(outer, inner)


def rain_chars(n=40):
    g = VGroup()
    pool = "01アイウエオカキ{}[]<>"
    for _ in range(n):
        c = T(
            random.choice(pool),
            sz=13,
            col=ManimColor.from_hex(random.choice([NEO_GREEN, NEO_DIM, "#007020"])),
        )
        c.move_to([random.uniform(-6.5, 6.5), random.uniform(-3.8, 3.8), 0])
        g.add(c)
    return g


def img_placeholder(w=3.0, h=2.2, label="[ IMAGE ]", col=NEO_CYAN):
    box = RoundedRectangle(
        width=w,
        height=h,
        corner_radius=0.12,
        stroke_color=col,
        stroke_width=1.8,
        fill_color="#001515",
        fill_opacity=0.9,
    )
    lbl = T(label, sz=18, col=col)
    lbl.move_to(box)
    # corner ticks
    tl = VGroup(
        Line(ORIGIN, RIGHT * 0.3, color=col, stroke_width=1.5),
        Line(ORIGIN, UP * 0.3, color=col, stroke_width=1.5),
    ).move_to(box.get_corner(UL) + RIGHT * 0.15 + DOWN * 0.15)
    tr = VGroup(
        Line(ORIGIN, LEFT * 0.3, color=col, stroke_width=1.5),
        Line(ORIGIN, UP * 0.3, color=col, stroke_width=1.5),
    ).move_to(box.get_corner(UR) + LEFT * 0.15 + DOWN * 0.15)
    bl = VGroup(
        Line(ORIGIN, RIGHT * 0.3, color=col, stroke_width=1.5),
        Line(ORIGIN, DOWN * 0.3, color=col, stroke_width=1.5),
    ).move_to(box.get_corner(DL) + RIGHT * 0.15 + UP * 0.15)
    br = VGroup(
        Line(ORIGIN, LEFT * 0.3, color=col, stroke_width=1.5),
        Line(ORIGIN, DOWN * 0.3, color=col, stroke_width=1.5),
    ).move_to(box.get_corner(DR) + LEFT * 0.15 + UP * 0.15)
    return VGroup(box, lbl, tl, tr, bl, br)


# ─── BASE ─────────────────────────────────────────────────────────────────────
class NeoSlide(Scene):
    def setup(self):
        self.camera.background_color = BG_BLACK

    def rain_in(self, dur=0.5):
        r = rain_chars(45)
        self.add(r)
        self.wait(dur)
        self.remove(r)

    def flash_in(self, mob, lag=0.05):
        self.play(
            LaggedStart(*[FadeIn(s, shift=DOWN * 0.08) for s in mob], lag_ratio=lag)
        )

    def glitch(self, mob, col_a=NEO_YELLOW, col_b=NEO_GREEN):
        self.play(mob.animate.set_color(col_a), run_time=0.06)
        self.play(mob.animate.set_color(col_b), run_time=0.06)


# ══════════════════════════════════════════════════════════════════════════════
#  S01 – TITLE
# ══════════════════════════════════════════════════════════════════════════════
class S01_Title(NeoSlide):
    def construct(self):
        self.rain_in()
        bd = glowing_border()
        self.play(Create(bd), run_time=0.7)

        tag = T("// OS FROM SCRATCH  ·  OOP EDITION", sz=20, col=NEO_DIM)
        title = T("BUILDING AN\nOPERATING SYSTEM", sz=52, col=NEO_GREEN, bold=True)
        title.set_color_by_gradient(NEO_GREEN, NEO_CYAN)
        sub = T("Object-Oriented Approach", sz=30, col=NEO_CYAN)
        name = T("[ Made by a Real Programmer ]", sz=26, col=NEO_PURPLE)
        cur = T("█", sz=28, col=NEO_GREEN)

        tag.to_corner(UL, buff=0.35)
        title.move_to(UP * 0.6)
        sub.next_to(title, DOWN, buff=0.45)
        name.next_to(sub, DOWN, buff=0.3)
        cur.next_to(name, RIGHT, buff=0.08)

        self.play(FadeIn(tag))
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(sub, shift=UP * 0.15))
        self.play(FadeIn(name))
        self.play(FadeIn(cur))
        self.play(Blink(cur, blinks=2))
        self.glitch(title)
        self.wait(1.5)
        self.play(FadeOut(VGroup(bd, tag, title, sub, name, cur)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S02 – TERRY DAVIS + MEME
# ══════════════════════════════════════════════════════════════════════════════
class S02_Terry(NeoSlide):
    def construct(self):
        self.rain_in(0.4)
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)

        quote = T(
            "\"You're a real programmer when\nyou've made a programming language\nand an operating system\"",
            sz=28,
            col=NEO_YELLOW,
            bold=True,
        )
        quote.to_edge(UP, buff=0.55)

        div = hr(NEO_CYAN, 11)
        div.next_to(quote, DOWN, buff=0.38)

        # Terry facts column
        facts = VGroup(
            T("Terry A. Davis  (1969–2018)", sz=30, col=NEO_CYAN, bold=True),
            T("→  TempleOS  ·  single-user ring-0 OS", sz=24, col=NEO_GREEN),
            T("→  HolyC  ·  compiled in real-time, in RAM", sz=24, col=NEO_GREEN),
            T("→  640×480 VGA  ·  no networking by design", sz=24, col=NEO_WHITE),
            T("→  ~100 000 lines  ·  1 man  ·  ~10 years", sz=24, col=NEO_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        facts.next_to(div, DOWN, buff=0.38)
        facts.to_edge(LEFT, buff=0.7)

        # ASCII meme block
        meme_lines = [
            "┌────────────────────────────┐",
            "│  Terry watching CIA niggers │",
            "│  trying to hack his OS      │",
            "│                            │",
            '│   ( ͡° ͜ʖ ͡°)  "God told me" │',
            "│                            │",
            "│  TempleOS: 100% divine      │",
            "└────────────────────────────┘",
        ]
        meme_grp = VGroup(*[T(l, sz=16, col=NEO_PURPLE) for l in meme_lines]).arrange(
            DOWN, aligned_edge=LEFT, buff=0.03
        )
        meme_grp.next_to(div, DOWN, buff=0.35)
        meme_grp.to_edge(RIGHT, buff=0.45)

        self.play(Write(quote), run_time=1.2)
        self.play(Create(div))
        self.flash_in(facts, 0.12)
        self.flash_in(meme_grp, 0.05)
        self.wait(2.0)
        self.play(FadeOut(VGroup(bd, quote, div, facts, meme_grp)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S03 – PARADIGMS + COMPANIES
# ══════════════════════════════════════════════════════════════════════════════
class S03_Paradigms(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("HARDWARE PARADIGMS", NEO_CYAN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        rows = [
            (
                "❌",
                "Quantum",
                "NOT OS – superposition collapses on read",
                "IBM Q · IonQ · PsiQuantum",
                NEO_RED,
            ),
            (
                "❌",
                "Thermodynamic",
                "NOT OS – entropy-based sampling (Extropic TSU)",
                "Extropic (Guillaume Verdon)",
                NEO_RED,
            ),
            (
                "⚠",
                "Photonic",
                "Possible OS substrate – light-speed bus",
                "Lightmatter · Luminous · Xanadu",
                NEO_YELLOW,
            ),
            (
                "❌",
                "Biological",
                "NOT OS – DNA / protein compute, ms latency",
                "Twist Bioscience · Catalog DNA",
                NEO_RED,
            ),
            (
                "✓",
                "Electronic",
                "YES – silicon CMOS, where OSes live",
                "Intel · AMD · ARM · RISC-V SiFive",
                NEO_GREEN,
            ),
        ]
        items = VGroup()
        for icon, name, desc, companies, col in rows:
            icon_t = T(icon, sz=20, col=col)
            name_t = T(name, sz=21, col=col, bold=True)
            desc_t = T(desc, sz=17, col=NEO_WHITE)
            comp_t = T(companies, sz=15, col=NEO_DIM)
            top = VGroup(icon_t, name_t, desc_t).arrange(
                RIGHT, buff=0.22, aligned_edge=UP
            )
            row = VGroup(top, comp_t).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
            items.add(row)
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        items.next_to(h, DOWN, buff=0.38)
        items.to_edge(LEFT, buff=0.6)

        bit_line = T(
            "P-bit  vs  Bit  vs  Trit  vs  Q-bit  →  next slides", sz=22, col=NEO_PURPLE
        )
        bit_line.to_edge(DOWN, buff=0.35)

        self.flash_in(items, 0.12)
        self.play(FadeIn(bit_line))
        self.wait(1.8)
        self.play(FadeOut(VGroup(bd, h, items, bit_line)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S04 – P-BIT  (with image placeholder)
# ══════════════════════════════════════════════════════════════════════════════
class S04_Pbit(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("PROBABILISTIC BIT  (P-BIT)", NEO_PURPLE)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        # Image placeholder left
        ph = img_placeholder(3.8, 2.8, "[ P-BIT MAGNET\n  DIAGRAM ]", NEO_PURPLE)
        ph.move_to(LEFT * 4.0 + DOWN * 0.5)
        src_lbl = T("Source: Purdue/Tohoku\n(Nature 2019)", sz=14, col=NEO_DIM)
        src_lbl.next_to(ph, DOWN, buff=0.1)

        # Animated probability bar
        bar_bg = Rectangle(
            width=3.0,
            height=0.5,
            stroke_color=NEO_PURPLE,
            stroke_width=1.5,
            fill_color="#100010",
            fill_opacity=1.0,
        )
        bar_fill = Rectangle(
            width=0.0,
            height=0.5,
            stroke_width=0,
            fill_color=NEO_PURPLE,
            fill_opacity=0.8,
        )
        bar_bg.move_to(LEFT * 4.0 + UP * 2.1)
        bar_fill.align_to(bar_bg, LEFT)
        bar_fill.move_to(bar_bg.get_left() + RIGHT * (3.0 / 2), aligned_edge=LEFT)
        bar_lbl = T("P(1) fluctuates 0→1", sz=16, col=NEO_PURPLE)
        bar_lbl.next_to(bar_bg, UP, buff=0.08)

        # Right column
        facts = VGroup(
            T("Purdue Univ + Tohoku Univ  (2019)", sz=22, col=NEO_PURPLE, bold=True),
            T("", sz=5),
            T("Bit:   deterministic  →  0 or 1", sz=20, col=NEO_WHITE),
            T("Qubit: superposition  →  0 AND 1", sz=20, col=NEO_CYAN),
            T("P-bit: probabilistic  →  fluctuates", sz=20, col=NEO_PURPLE),
            T("", sz=5),
            T("→  Room-temperature operation", sz=19, col=NEO_GREEN),
            T("→  Unstable nanomagnets + transistor", sz=19, col=NEO_GREEN),
            T("→  8 p-bits factorised integers (Nature)", sz=19, col=NEO_GREEN),
            T("→  'Poor man's qubit'  (Supriyo Datta)", sz=19, col=NEO_YELLOW),
            T("→  Solves optimization & ML problems", sz=19, col=NEO_WHITE),
            T("→  NOT suitable as OS substrate", sz=19, col=NEO_RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        facts.move_to(RIGHT * 1.8 + DOWN * 0.2)

        self.play(FadeIn(ph), FadeIn(src_lbl))
        self.play(FadeIn(bar_bg), FadeIn(bar_lbl))
        # Animate the probability bar oscillating
        for target_w in [2.1, 0.4, 2.7, 0.9, 1.5]:
            new_fill = Rectangle(
                width=target_w,
                height=0.5,
                stroke_width=0,
                fill_color=NEO_PURPLE,
                fill_opacity=0.8,
            )
            new_fill.align_to(bar_bg, LEFT)
            self.play(Transform(bar_fill, new_fill), run_time=0.25)
        self.flash_in(facts, 0.08)
        self.wait(1.8)
        self.play(
            FadeOut(VGroup(bd, h, ph, src_lbl, bar_bg, bar_fill, bar_lbl, facts)),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S05 – TRITS / SETUN (with image placeholder)
# ══════════════════════════════════════════════════════════════════════════════
class S05_Trits(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("TERNARY  /  TRITS  ·  SETUN", NEO_RED)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        # Left image placeholder
        ph = img_placeholder(3.6, 2.6, "[ SETUN COMPUTER\n  PHOTO  USSR ]", NEO_RED)
        ph.move_to(LEFT * 4.0 + DOWN * 0.5)
        src_lbl = T("Setun  ·  Moscow State Univ  ·  1958", sz=14, col=NEO_DIM)
        src_lbl.next_to(ph, DOWN, buff=0.08)

        # Trit diagram
        trit_row = VGroup()
        for val, col in [("-1", NEO_CYAN), ("0", NEO_WHITE), ("+1", NEO_GREEN)]:
            box = RoundedRectangle(
                width=1.0,
                height=0.9,
                corner_radius=0.08,
                stroke_color=col,
                stroke_width=2,
                fill_color=col,
                fill_opacity=0.12,
            )
            lbl = T(val, sz=28, col=col, bold=True)
            lbl.move_to(box)
            trit_row.add(VGroup(box, lbl))
        trit_row.arrange(RIGHT, buff=0.3)
        trit_row.move_to(LEFT * 4.0 + UP * 2.2)
        trit_title = T("TRIT  (−1, 0, +1)", sz=20, col=NEO_RED)
        trit_title.next_to(trit_row, UP, buff=0.1)

        facts = VGroup(
            T("Nikolay Brusentsov  ·  1958–1959", sz=22, col=NEO_RED, bold=True),
            T("", sz=4),
            T("→  Balanced ternary  −1, 0, +1", sz=20, col=NEO_WHITE),
            T("→  50 machines built  ·  15 yrs operation", sz=20, col=NEO_WHITE),
            T("→  ZERO failures reported", sz=20, col=NEO_GREEN),
            T("→  Lower power than binary of era", sz=20, col=NEO_GREEN),
            T("→  No sign bit  ·  natural arithmetic", sz=20, col=NEO_CYAN),
            T("→  18-trit word = 387 420 489 integers", sz=20, col=NEO_CYAN),
            T("", sz=4),
            T("Why it died: binary chip industry momentum", sz=19, col=NEO_YELLOW),
            T("No ternary CMOS standardized → abandoned", sz=19, col=NEO_RED),
            T("Revival interest: neural nets (−1,0,+1 weights)", sz=19, col=NEO_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        facts.move_to(RIGHT * 1.8 + DOWN * 0.1)

        self.play(FadeIn(ph), FadeIn(src_lbl))
        self.play(FadeIn(trit_title))
        self.flash_in(trit_row, 0.15)
        self.flash_in(facts, 0.08)
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(bd, h, ph, src_lbl, trit_row, trit_title, facts)),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S06 – MIT WOOD PHONE
# ══════════════════════════════════════════════════════════════════════════════
class S06_WoodPhone(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("MIT DIY WOOD PHONE  ·  2012", NEO_ORANGE)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        # Wood phone SVG-style sketch
        body = RoundedRectangle(
            width=1.8,
            height=3.2,
            corner_radius=0.25,
            stroke_color="#8B4513",
            stroke_width=3,
            fill_color="#5C3317",
            fill_opacity=0.6,
        )
        screen = RoundedRectangle(
            width=1.2,
            height=1.4,
            corner_radius=0.1,
            stroke_color=NEO_CYAN,
            stroke_width=1.5,
            fill_color="#001515",
            fill_opacity=0.9,
        )
        screen_txt = T("Number\nplease", sz=14, col=NEO_GREEN)
        screen_txt.move_to(screen)
        screen.move_to(body.get_top() + DOWN * 0.85)

        btn_rows = VGroup()
        for row in range(3):
            r = VGroup()
            for col_i in range(3):
                btn = Circle(
                    radius=0.12,
                    stroke_color="#D2691E",
                    stroke_width=1.5,
                    fill_color="#3D1C00",
                    fill_opacity=0.8,
                )
                r.add(btn)
            r.arrange(RIGHT, buff=0.18)
            btn_rows.add(r)
        btn_rows.arrange(DOWN, buff=0.18)
        btn_rows.move_to(body.get_bottom() + UP * 0.55)

        wood_grain1 = Line(
            body.get_left() + UP * 0.5,
            body.get_right() + UP * 0.5,
            color="#3D1C00",
            stroke_width=0.8,
        )
        wood_grain2 = Line(
            body.get_left() + DOWN * 0.2,
            body.get_right() + DOWN * 0.2,
            color="#3D1C00",
            stroke_width=0.6,
        )

        phone_grp = VGroup(body, wood_grain1, wood_grain2, screen, screen_txt, btn_rows)
        phone_grp.move_to(LEFT * 4.3 + DOWN * 0.1)

        # Paper strip label
        paper = RoundedRectangle(
            width=3.0,
            height=0.5,
            corner_radius=0.06,
            stroke_color=NEO_ORANGE,
            stroke_width=1.2,
            fill_color="#1A0A00",
            fill_opacity=0.9,
        )
        paper_lbl = T("MIT High-Low Tech Group", sz=16, col=NEO_ORANGE)
        paper_lbl.move_to(paper)
        paper.next_to(phone_grp, DOWN, buff=0.25)
        paper_lbl.move_to(paper)

        facts = VGroup(
            T(
                "David Mellis  ·  MIT Media Lab  (2012)",
                sz=22,
                col=NEO_ORANGE,
                bold=True,
            ),
            T("", sz=4),
            T("→  Laser-cut plywood + veneer case", sz=20, col=NEO_WHITE),
            T("→  SM5100B GSM Module (SparkFun)", sz=20, col=NEO_WHITE),
            T("→  1.8″ 160×128 TFT screen (Adafruit)", sz=20, col=NEO_WHITE),
            T("→  Standard SIM · any GSM provider", sz=20, col=NEO_GREEN),
            T("→  ~$150 in parts · open-source design", sz=20, col=NEO_GREEN),
            T("→  Voice calls (SMS addable same HW)", sz=20, col=NEO_CYAN),
            T("", sz=4),
            T("Veneer flexures → physical button press", sz=19, col=NEO_YELLOW),
            T("Proof: wood IS a valid compute substrate", sz=19, col=NEO_YELLOW),
            T("Source: The Verge / MIT High-Low Tech  2012", sz=16, col=NEO_DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        facts.move_to(RIGHT * 1.7 + DOWN * 0.15)

        self.play(Create(phone_grp), run_time=1.0)
        self.play(FadeIn(paper), FadeIn(paper_lbl))
        self.flash_in(facts, 0.08)
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(bd, h, phone_grp, paper, paper_lbl, facts)), run_time=0.5
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S07 – WHERE TO PROCESS: CPU/GPU/TPU/FPGA/ASIC
# ══════════════════════════════════════════════════════════════════════════════
class S07_Processors(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("WHERE DOES THE MAGIC HAPPEN?", NEO_CYAN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        units = [
            (
                "CPU",
                "Few fast cores · OS & scheduler live here · ring-0 privilege",
                NEO_GREEN,
            ),
            (
                "GPU",
                "1000s of tiny cores · NO persistent memory · NO ring-0 · no IO",
                NEO_RED,
            ),
            ("TPU", "Matrix/tensor unit · Google · ML train/infer only", NEO_CYAN),
            ("FPGA", "Reconfigurable logic · OS-like control possible", NEO_YELLOW),
            (
                "ASIC",
                "Fixed-function · best perf/watt · Apple M-series SoC",
                NEO_PURPLE,
            ),
        ]
        boxes = VGroup()
        for label, desc, col in units:
            box = RoundedRectangle(
                width=12.2,
                height=0.75,
                corner_radius=0.08,
                stroke_color=col,
                stroke_width=1.5,
                fill_color=col,
                fill_opacity=0.06,
            )
            lbl = T(label, sz=22, col=col, bold=True)
            dsc = T(desc, sz=17, col=NEO_WHITE)
            row = VGroup(lbl, dsc).arrange(RIGHT, buff=0.5, aligned_edge=UP)
            row.to_edge(LEFT, buff=0.65)
            row.move_to(box.get_left() + RIGHT * 6.1, coor_mask=UP + DOWN)
            boxes.add(VGroup(box, row))
        boxes.arrange(DOWN, buff=0.17)
        boxes.next_to(h, DOWN, buff=0.4)

        arch = T(
            "Von Neumann (shared bus)  vs  Harvard (split program/data memory)  →  next slide",
            sz=19,
            col=NEO_PURPLE,
        )
        arch.to_edge(DOWN, buff=0.32)

        self.flash_in(boxes, 0.1)
        self.play(FadeIn(arch))
        self.wait(1.8)
        self.play(FadeOut(VGroup(bd, h, boxes, arch)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S08 – Von Neumann vs Harvard  (image placeholder)
# ══════════════════════════════════════════════════════════════════════════════
class S08_VonNeumann(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("VON NEUMANN  vs  HARVARD ARCHITECTURE", NEO_YELLOW)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        # Image placeholder (user can swap real image here)
        ph = img_placeholder(
            5.5, 3.4, "[ ARCHITECTURE\n  DIAGRAM IMAGE\n  insert here ]", NEO_YELLOW
        )
        ph.move_to(LEFT * 3.5 + DOWN * 0.4)
        src = T(
            "en.eeworld.com.cn reference · replace with diagram", sz=13, col=NEO_DIM
        )
        src.next_to(ph, DOWN, buff=0.08)

        vn = VGroup(
            T("VON NEUMANN", sz=22, col=NEO_CYAN, bold=True),
            T("• Single shared bus", sz=19, col=NEO_WHITE),
            T("• Data + instructions same RAM", sz=19, col=NEO_WHITE),
            T("• Bottleneck: memory bandwidth", sz=19, col=NEO_RED),
            T("• Desktop / server CPUs", sz=19, col=NEO_WHITE),
            T("• Most OSes live here", sz=19, col=NEO_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        hv = VGroup(
            T("HARVARD", sz=22, col=NEO_PURPLE, bold=True),
            T("• Separate instruction / data buses", sz=19, col=NEO_WHITE),
            T("• No bottleneck on fetch", sz=19, col=NEO_GREEN),
            T("• Used in MCUs, DSPs, FPGAs", sz=19, col=NEO_WHITE),
            T("• ARM Cortex-M (modified Harvard)", sz=19, col=NEO_CYAN),
            T("• Harder to do self-modifying code", sz=19, col=NEO_YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        panels = VGroup(vn, hv).arrange(DOWN, buff=0.35)
        panels.move_to(RIGHT * 2.8 + DOWN * 0.2)

        self.play(FadeIn(ph), FadeIn(src))
        self.flash_in(vn, 0.1)
        self.flash_in(hv, 0.1)
        self.wait(1.8)
        self.play(FadeOut(VGroup(bd, h, ph, src, panels)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S09 – ISA: ARM / x86 / RISC-V
# ══════════════════════════════════════════════════════════════════════════════
class S09_ISA(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("ISA: ARM  ·  x86  ·  RISC-V", NEO_GREEN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        data = [
            (
                "ARM",
                NEO_CYAN,
                [
                    "RISC · energy efficient",
                    "Mobile, Apple M1+",
                    "Closed ISA (licence fee)",
                    "Good OS support",
                ],
            ),
            (
                "x86",
                NEO_YELLOW,
                [
                    "CISC · complex inst set",
                    "Desktops/servers",
                    "Intel/AMD duopoly",
                    "Legacy bloat but fast",
                ],
            ),
            (
                "RISC-V",
                NEO_GREEN,
                [
                    "Open ISA · royalty-free",
                    "AI edge / embedded",
                    "Custom extensions OK",
                    "Growing OS ecosystem",
                    "WHY AI: vector ext.",
                    "Not GPU, CPU-class!",
                ],
            ),
        ]
        cols = VGroup()
        for name, col, pts in data:
            box = RoundedRectangle(
                width=3.9,
                height=4.2,
                corner_radius=0.15,
                stroke_color=col,
                stroke_width=2,
                fill_color=col,
                fill_opacity=0.05,
            )
            title_t = T(name, sz=26, col=col, bold=True)
            bullets = VGroup(*[T("• " + p, sz=17, col=NEO_WHITE) for p in pts]).arrange(
                DOWN, aligned_edge=LEFT, buff=0.16
            )
            content = VGroup(title_t, bullets).arrange(
                DOWN, buff=0.22, aligned_edge=LEFT
            )
            content.move_to(box).shift(LEFT * 0.1)
            cols.add(VGroup(box, content))
        cols.arrange(RIGHT, buff=0.5)
        cols.next_to(h, DOWN, buff=0.45)

        note = T(
            "RISC-V for AI: open vector ext (RVV) → embedded inference, not GPU replacement",
            sz=18,
            col=NEO_PURPLE,
        )
        note.to_edge(DOWN, buff=0.32)

        self.flash_in(cols, 0.15)
        self.play(FadeIn(note))
        self.wait(1.8)
        self.play(FadeOut(VGroup(bd, h, cols, note)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S10 – GPU MISCONCEPTION (why GPU has no OS)
# ══════════════════════════════════════════════════════════════════════════════
class S10_GPUMisconception(NeoSlide):
    def construct(self):
        bd = glowing_border(NEO_RED)
        self.play(Create(bd), run_time=0.5)

        big = T('"I built an OS for the GPU"', sz=40, col=NEO_RED, bold=True)
        big.move_to(UP * 2.7)
        face = T("( ͡° ͜ʖ ͡°)   really?", sz=36, col=NEO_YELLOW)
        face.next_to(big, DOWN, buff=0.35)
        div = hr(NEO_CYAN, 11)
        div.next_to(face, DOWN, buff=0.35)

        why = T("WHY A GPU CANNOT HOST AN OS:", sz=26, col=NEO_CYAN, bold=True)
        why.next_to(div, DOWN, buff=0.3)

        reasons = VGroup(
            T(
                "❌  No persistent memory  →  VRAM is HOST-MANAGED, wiped on context switch",
                sz=19,
                col=NEO_WHITE,
            ),
            T(
                "❌  No interrupt controller  →  GPU cannot handle hardware events",
                sz=19,
                col=NEO_WHITE,
            ),
            T(
                "❌  No I/O subsystem  →  GPU has ZERO direct disk/net/USB access",
                sz=19,
                col=NEO_RED,
            ),
            T(
                "❌  No ring 0/3 privilege  →  GPU has no protection domain architecture",
                sz=19,
                col=NEO_WHITE,
            ),
            T(
                "❌  You talk to GPU via API (CUDA/OpenCL)  →  it IS managed by the CPU OS",
                sz=19,
                col=NEO_YELLOW,
            ),
            T(
                "✓   GPU = accelerator, not host  ·  OS manages the GPU, not vice-versa",
                sz=19,
                col=NEO_GREEN,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        reasons.next_to(why, DOWN, buff=0.28)
        reasons.to_edge(LEFT, buff=0.6)

        self.play(Write(big), run_time=0.7)
        self.play(FadeIn(face))
        self.play(Create(div))
        self.play(FadeIn(why))
        self.flash_in(reasons, 0.1)
        self.wait(2.0)
        self.play(FadeOut(VGroup(bd, big, face, div, why, reasons)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S11 – FORMAL DEFINITION
# ══════════════════════════════════════════════════════════════════════════════
class S11_Definition(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("FORMAL DEFINITION OF OS", NEO_CYAN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        defn = T(
            "An operating system (OS) is a system software layer that\n"
            "manages the hardware resources of a computer and provides\n"
            "services, abstractions, and interfaces that enable\n"
            "application programs and users to execute and interact\n"
            "with the system efficiently, securely, and reliably.",
            sz=22,
            col=NEO_WHITE,
        )
        defn.next_to(h, DOWN, buff=0.45)

        keys = VGroup(
            T("→  manages hardware resources", sz=22, col=NEO_GREEN),
            T("→  provides services & abstractions", sz=22, col=NEO_CYAN),
            T("→  efficient  ·  secure  ·  reliable", sz=22, col=NEO_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        keys.to_edge(DOWN, buff=0.45)

        self.play(Write(defn), run_time=1.8)
        self.flash_in(keys, 0.15)
        self.wait(1.5)
        self.play(FadeOut(VGroup(bd, h, defn, keys)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S12 – OS IN PYTHON
# ══════════════════════════════════════════════════════════════════════════════
class S12_PythonOS(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("OPERATING SYSTEM IN PYTHON???", NEO_RED)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        left_h = T("🚫 Skeptic:", sz=26, col=NEO_RED, bold=True)
        left_p = VGroup(
            T("No compile → binary output", sz=19, col=NEO_WHITE),
            T("No raw pointer arithmetic", sz=19, col=NEO_WHITE),
            T("Can't inline assembler", sz=19, col=NEO_WHITE),
            T("GIL kills parallelism", sz=19, col=NEO_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        left_col = VGroup(left_h, left_p).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        right_h = T("✓ Smart guy:", sz=26, col=NEO_GREEN, bold=True)
        right_p = VGroup(
            T("Save state in .pkl / shelve", sz=19, col=NEO_WHITE),
            T("ctypes / cffi → raw pointers", sz=19, col=NEO_WHITE),
            T("subprocess → run asm/shell", sz=19, col=NEO_WHITE),
            T("Cython / Mypyc → compile to .so", sz=19, col=NEO_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        right_col = VGroup(right_h, right_p).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        cols = VGroup(left_col, right_col).arrange(RIGHT, buff=1.2)
        cols.next_to(h, DOWN, buff=0.5)

        verdict = T(
            "Best: C / C++ / Rust / Asm  ·  Python OK for prototyping bootable disk tools",
            sz=19,
            col=NEO_YELLOW,
        )
        verdict.to_edge(DOWN, buff=0.35)

        self.flash_in(left_col, 0.1)
        self.flash_in(right_col, 0.1)
        self.play(FadeIn(verdict))
        self.wait(1.8)
        self.play(FadeOut(VGroup(bd, h, cols, verdict)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S13 – BOOT LOADER  (register animation)
# ══════════════════════════════════════════════════════════════════════════════
class S13_BootLoader(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("BOOT LOADER", NEO_GREEN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        defn = T(
            "First program after power-on · inits HW → loads kernel → hands control over.",
            sz=20,
            col=NEO_WHITE,
        )
        defn.next_to(h, DOWN, buff=0.32)
        self.play(Write(defn), run_time=0.8)

        # ── MEMORY LIST (left side) ──────────────────────────────────────────
        mem_title = T("MEMORY", sz=18, col=NEO_CYAN, bold=True)
        mem_cells = VGroup()
        mem_data = [
            ("0x7C00", "[ MBR CODE   ]", NEO_GREEN),
            ("0x7E00", "[ STAGE2 BTL ]", NEO_CYAN),
            ("0x0500", "[ BIOS DATA  ]", NEO_DIM),
            ("0x1000", "[ KERNEL     ]", NEO_RED),
            ("0x9000", "[ STACK      ]", NEO_YELLOW),
        ]
        for addr, label, col in mem_data:
            box = Rectangle(
                width=3.6,
                height=0.52,
                stroke_color=col,
                stroke_width=1.4,
                fill_color=col,
                fill_opacity=0.08,
            )
            addr_t = T(addr, sz=14, col=col)
            lbl_t = T(label, sz=14, col=NEO_WHITE)
            row = VGroup(addr_t, lbl_t).arrange(RIGHT, buff=0.3)
            row.move_to(box)
            mem_cells.add(VGroup(box, row))
        mem_cells.arrange(DOWN, buff=0.06)
        mem_grp = VGroup(mem_title, mem_cells).arrange(DOWN, buff=0.12)
        mem_grp.move_to(LEFT * 4.0 + DOWN * 0.4)

        # ── REGISTERS (right side) ───────────────────────────────────────────
        reg_title = T("REGISTERS", sz=18, col=NEO_YELLOW, bold=True)
        regs = VGroup()
        reg_data = [
            ("CS", "0x0000", NEO_YELLOW),
            ("IP", "0x7C00", NEO_GREEN),
            ("DS", "0x0000", NEO_CYAN),
            ("SP", "0x9000", NEO_WHITE),
        ]
        for rname, rval, rcol in reg_data:
            rb = Rectangle(
                width=3.2,
                height=0.52,
                stroke_color=rcol,
                stroke_width=1.4,
                fill_color=rcol,
                fill_opacity=0.1,
            )
            rn = T(rname, sz=16, col=rcol, bold=True)
            rv = T(rval, sz=16, col=NEO_WHITE)
            rrow = VGroup(rn, rv).arrange(RIGHT, buff=0.55)
            rrow.move_to(rb)
            regs.add(VGroup(rb, rrow))
        regs.arrange(DOWN, buff=0.12)
        reg_grp = VGroup(reg_title, regs).arrange(DOWN, buff=0.12)
        reg_grp.move_to(RIGHT * 3.5 + DOWN * 0.4)

        # Draw memory cells (faded)
        self.play(FadeIn(mem_title), FadeIn(reg_title))
        for cell in mem_cells:
            self.play(FadeIn(cell), run_time=0.15)

        # Show registers
        for reg in regs:
            self.play(FadeIn(reg), run_time=0.2)

        # ── ANIMATION: IP register loads from 0xFFFF0 → 0x7C00 ──────────────
        arrow = Arrow(
            reg_grp.get_left() + LEFT * 0.1,
            mem_cells[0].get_right() + RIGHT * 0.1,
            buff=0.05,
            color=NEO_GREEN,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        )
        arrow_lbl = T("CS:IP → MBR", sz=15, col=NEO_GREEN)
        arrow_lbl.next_to(arrow, UP, buff=0.05)

        self.play(GrowArrow(arrow), FadeIn(arrow_lbl))

        # Flash the MBR cell
        self.play(mem_cells[0].animate.set_stroke(color=NEO_YELLOW), run_time=0.15)
        self.play(mem_cells[0].animate.set_stroke(color=NEO_GREEN), run_time=0.15)

        # Animate kernel load: MBR → KERNEL cell lights up
        kern_arrow = CurvedArrow(
            mem_cells[0].get_bottom(),
            mem_cells[3].get_top(),
            angle=TAU / 8,
            color=NEO_RED,
            stroke_width=2,
        )
        kern_lbl = T("loads kernel→0x1000", sz=13, col=NEO_RED)
        kern_lbl.next_to(kern_arrow, RIGHT, buff=0.1)
        self.play(Create(kern_arrow), FadeIn(kern_lbl))
        self.play(
            mem_cells[3].animate.set_fill(color=NEO_RED, opacity=0.3), run_time=0.3
        )

        blink_t = T("BOOT!", sz=22, col=NEO_GREEN, bold=True)
        blink_t.next_to(mem_grp, DOWN, buff=0.2)
        self.play(FadeIn(blink_t))
        self.play(Blink(blink_t, blinks=2))

        self.wait(1.2)
        self.play(
            FadeOut(
                VGroup(
                    bd,
                    h,
                    defn,
                    mem_grp,
                    reg_grp,
                    arrow,
                    arrow_lbl,
                    kern_arrow,
                    kern_lbl,
                    blink_t,
                )
            ),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S14 – PROCESS SCHEDULER
# ══════════════════════════════════════════════════════════════════════════════
class S14_Scheduler(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("PROCESS SCHEDULER", NEO_CYAN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        defn = T(
            "Selects which runnable process gets CPU time · determines order & duration.",
            sz=20,
            col=NEO_WHITE,
        )
        defn.next_to(h, DOWN, buff=0.32)
        self.play(Write(defn), run_time=0.8)

        # CPU box
        cpu_box_ = RoundedRectangle(
            width=2.2,
            height=1.1,
            corner_radius=0.1,
            stroke_color=NEO_GREEN,
            stroke_width=2.5,
            fill_opacity=0,
        )
        cpu_lbl = T("CPU", sz=28, col=NEO_GREEN, bold=True)
        cpu_lbl.move_to(cpu_box_)
        cpu_grp = VGroup(cpu_box_, cpu_lbl)
        cpu_grp.move_to(RIGHT * 3.5 + DOWN * 0.4)

        procs = ["P1", "P2", "P3", "P4"]
        pcols = [NEO_CYAN, NEO_PURPLE, NEO_YELLOW, NEO_RED]
        queue = VGroup()
        for p, c in zip(procs, pcols):
            b = RoundedRectangle(
                width=1.3,
                height=0.7,
                corner_radius=0.08,
                stroke_color=c,
                stroke_width=1.8,
                fill_color=c,
                fill_opacity=0.12,
            )
            t = T(p, sz=22, col=c, bold=True)
            t.move_to(b)
            queue.add(VGroup(b, t))
        queue.arrange(RIGHT, buff=0.22)
        queue.move_to(LEFT * 2.5 + DOWN * 0.4)

        q_lbl = T("Ready Queue →", sz=18, col=NEO_DIM)
        q_lbl.next_to(queue, UP, buff=0.12)

        sched_arrow = Arrow(
            queue.get_right(),
            cpu_grp.get_left(),
            buff=0.1,
            color=NEO_GREEN,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.14,
        )

        self.play(FadeIn(q_lbl))
        for p in queue:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.22)
        self.play(Create(cpu_grp))
        self.play(GrowArrow(sched_arrow))

        p1 = queue[0].copy()
        self.play(p1.animate.move_to(cpu_grp).scale(0.8), run_time=0.6)
        self.play(FadeOut(p1), run_time=0.2)
        self.play(queue[1:].animate.shift(LEFT * 1.55), run_time=0.45)
        self.wait(1.0)
        self.play(
            FadeOut(VGroup(bd, h, defn, queue, cpu_grp, sched_arrow, q_lbl)),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S15 – FILE SYSTEM
# ══════════════════════════════════════════════════════════════════════════════
class S15_FileSystem(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("FILE SYSTEM", NEO_PURPLE)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        defn = T(
            "Organises, stores, retrieves and manages persistent data on storage devices.",
            sz=20,
            col=NEO_WHITE,
        )
        defn.next_to(h, DOWN, buff=0.32)
        self.play(Write(defn), run_time=0.8)

        root = T("/", sz=30, col=NEO_PURPLE, bold=True)
        root.move_to(UP * 0.9)

        branches = {
            "bin": (LEFT * 3.8, NEO_GREEN),
            "dev": (LEFT * 1.9, NEO_CYAN),
            "etc": (ORIGIN, NEO_YELLOW),
            "home": (RIGHT * 1.9, NEO_WHITE),
            "proc": (RIGHT * 3.8, NEO_RED),
        }
        bnodes = {}
        lines_ = VGroup()
        for nm, (pos, col) in branches.items():
            n = T(nm, sz=24, col=col, bold=True)
            n.move_to(DOWN * 0.3 + pos)
            bnodes[nm] = n
            lines_.add(
                Line(root.get_bottom(), n.get_top(), color=col, stroke_width=1.2)
            )

        types = T("ext4  FAT32  NTFS  ZFS  BTRFS  HFS+", sz=22, col=NEO_CYAN)
        types.to_edge(DOWN, buff=0.38)

        self.play(FadeIn(root))
        self.play(Create(lines_), run_time=0.7)
        self.flash_in(VGroup(*bnodes.values()), 0.12)
        self.play(FadeIn(types))
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(bd, h, defn, lines_, root, *bnodes.values(), types)),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S16 – PAGING
# ══════════════════════════════════════════════════════════════════════════════
class S16_Paging(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("PAGING / VIRTUAL MEMORY", NEO_YELLOW)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        defn = T(
            "Fixed-size pages (virtual) ↔ frames (physical) → isolation & protection.",
            sz=20,
            col=NEO_WHITE,
        )
        defn.next_to(h, DOWN, buff=0.32)
        self.play(Write(defn), run_time=0.7)

        n = 4
        v_pages = VGroup()
        p_frames = VGroup()
        for i in range(n):
            vp = RoundedRectangle(
                width=1.5,
                height=0.52,
                corner_radius=0.06,
                stroke_color=NEO_CYAN,
                stroke_width=1.5,
                fill_color=NEO_CYAN,
                fill_opacity=0.08,
            )
            T(f"VP {i}", sz=17, col=NEO_CYAN).move_to(vp)
            v_pages.add(VGroup(vp, T(f"VP {i}", sz=17, col=NEO_CYAN)))

            pf = RoundedRectangle(
                width=1.5,
                height=0.52,
                corner_radius=0.06,
                stroke_color=NEO_GREEN,
                stroke_width=1.5,
                fill_color=NEO_GREEN,
                fill_opacity=0.08,
            )
            T(f"PF {i}", sz=17, col=NEO_GREEN).move_to(pf)
            p_frames.add(VGroup(pf, T(f"PF {i}", sz=17, col=NEO_GREEN)))

        v_pages.arrange(DOWN, buff=0.18)
        p_frames.arrange(DOWN, buff=0.18)
        v_pages.move_to(LEFT * 4.2 + DOWN * 0.1)
        p_frames.move_to(RIGHT * 4.2 + DOWN * 0.1)

        pt_box = RoundedRectangle(
            width=2.2,
            height=3.0,
            corner_radius=0.1,
            stroke_color=NEO_YELLOW,
            stroke_width=2,
            fill_color=NEO_YELLOW,
            fill_opacity=0.05,
        )
        pt_lbl = T("PAGE\nTABLE", sz=20, col=NEO_YELLOW, bold=True)
        pt_lbl.move_to(pt_box)
        pt_grp = VGroup(pt_box, pt_lbl)
        pt_grp.move_to(DOWN * 0.1)

        v_lbl = T("Virtual\nAddresses", sz=18, col=NEO_CYAN)
        v_lbl.next_to(v_pages, UP, buff=0.12)
        p_lbl = T("Physical\nFrames", sz=18, col=NEO_GREEN)
        p_lbl.next_to(p_frames, UP, buff=0.12)

        self.play(FadeIn(v_lbl), FadeIn(p_lbl))
        for vp, pf in zip(v_pages, p_frames):
            self.play(
                FadeIn(vp, shift=RIGHT * 0.2),
                FadeIn(pf, shift=LEFT * 0.2),
                run_time=0.22,
            )
        self.play(FadeIn(pt_grp))

        arr_in = VGroup(
            *[
                Arrow(
                    v_pages[i].get_right(),
                    pt_grp.get_left(),
                    buff=0.05,
                    color=NEO_CYAN,
                    stroke_width=1.0,
                    max_tip_length_to_length_ratio=0.14,
                )
                for i in range(n)
            ]
        )
        arr_out = VGroup(
            *[
                Arrow(
                    pt_grp.get_right(),
                    p_frames[i].get_left(),
                    buff=0.05,
                    color=NEO_GREEN,
                    stroke_width=1.0,
                    max_tip_length_to_length_ratio=0.14,
                )
                for i in range(n)
            ]
        )
        self.play(Create(arr_in), run_time=0.4)
        self.play(Create(arr_out), run_time=0.4)
        self.wait(1.2)
        self.play(
            FadeOut(
                VGroup(
                    bd,
                    h,
                    defn,
                    v_pages,
                    p_frames,
                    pt_grp,
                    arr_in,
                    arr_out,
                    v_lbl,
                    p_lbl,
                )
            ),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S17 – SYSTEM CALLS
# ══════════════════════════════════════════════════════════════════════════════
class S17_SysCalls(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("SYSTEM CALLS", NEO_CYAN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        defn = T(
            "Controlled interface: user-space requests kernel services.",
            sz=20,
            col=NEO_WHITE,
        )
        defn.next_to(h, DOWN, buff=0.32)
        self.play(Write(defn), run_time=0.7)

        u_box = RoundedRectangle(
            width=3.8,
            height=1.2,
            corner_radius=0.1,
            stroke_color=NEO_CYAN,
            stroke_width=2,
            fill_color=NEO_CYAN,
            fill_opacity=0.07,
        )
        u_lbl = T("User Space\n(ring 3)", sz=20, col=NEO_CYAN)
        u_lbl.move_to(u_box)
        u_grp = VGroup(u_box, u_lbl)
        u_grp.move_to(LEFT * 3.2 + DOWN * 0.4)

        k_box = RoundedRectangle(
            width=3.8,
            height=1.2,
            corner_radius=0.1,
            stroke_color=NEO_RED,
            stroke_width=2,
            fill_color=NEO_RED,
            fill_opacity=0.07,
        )
        k_lbl = T("Kernel Space\n(ring 0)", sz=20, col=NEO_RED)
        k_lbl.move_to(k_box)
        k_grp = VGroup(k_box, k_lbl)
        k_grp.move_to(RIGHT * 3.2 + DOWN * 0.4)

        arr_call = Arrow(
            u_grp.get_right(),
            k_grp.get_left(),
            buff=0.1,
            color=NEO_GREEN,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.14,
        )
        arr_ret = Arrow(
            k_grp.get_left(),
            u_grp.get_right(),
            buff=0.1,
            color=NEO_YELLOW,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.14,
        )
        l_call = T("syscall()", sz=18, col=NEO_GREEN)
        l_call.next_to(arr_call, UP, buff=0.08)
        l_ret = T("return", sz=18, col=NEO_YELLOW)
        l_ret.next_to(arr_ret, DOWN, buff=0.08)

        ex = T(
            "read() · write() · fork() · exec() · mmap() · ioctl() · open() · close()",
            sz=18,
            col=NEO_PURPLE,
        )
        ex.to_edge(DOWN, buff=0.35)

        self.play(FadeIn(u_grp), FadeIn(k_grp))
        self.play(GrowArrow(arr_call), FadeIn(l_call))
        self.play(GrowArrow(arr_ret), FadeIn(l_ret))
        self.play(FadeIn(ex))
        self.wait(1.5)
        self.play(
            FadeOut(
                VGroup(bd, h, defn, u_grp, k_grp, arr_call, arr_ret, l_call, l_ret, ex)
            ),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S18 – INTERRUPTS & TRAPS
# ══════════════════════════════════════════════════════════════════════════════
class S18_Interrupts(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("INTERRUPTS  &  TRAPS", NEO_RED)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        def panel(title, col, points, pos):
            box = RoundedRectangle(
                width=5.5,
                height=3.6,
                corner_radius=0.12,
                stroke_color=col,
                stroke_width=2,
                fill_color=col,
                fill_opacity=0.05,
            )
            ttl = T(title, sz=26, col=col, bold=True)
            pts = VGroup(*[T("• " + p, sz=19, col=NEO_WHITE) for p in points]).arrange(
                DOWN, aligned_edge=LEFT, buff=0.2
            )
            content = VGroup(ttl, pts).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
            content.move_to(box).shift(LEFT * 0.15)
            grp = VGroup(box, content)
            grp.move_to(pos)
            return grp

        int_grp = panel(
            "INTERRUPT",
            NEO_YELLOW,
            [
                "Async HW signal",
                "Keyboard, timer, NIC",
                "Pauses current exec",
                "OS ISR fires → resumes",
            ],
            LEFT * 3.1 + DOWN * 0.2,
        )
        trap_grp = panel(
            "TRAP",
            NEO_RED,
            [
                "Sync CPU exception",
                "Div-by-zero, page fault",
                "Generated by instruction",
                "OS trap handler fires",
            ],
            RIGHT * 3.1 + DOWN * 0.2,
        )

        self.play(FadeIn(int_grp), run_time=0.6)
        self.play(FadeIn(trap_grp), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(VGroup(bd, h, int_grp, trap_grp)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S19 – KERNEL PANIC
# ══════════════════════════════════════════════════════════════════════════════
class S19_KernelPanic(NeoSlide):
    def construct(self):
        bd = glowing_border(NEO_RED)
        self.play(Create(bd), run_time=0.5)

        skull = Text("💀", font_size=80)
        skull.move_to(UP * 2.1)
        self.play(FadeIn(skull, scale=0.4), run_time=0.4)

        kp = T("KERNEL PANIC", sz=52, col=NEO_RED, bold=True)
        kp.next_to(skull, DOWN, buff=0.2)
        self.play(Write(kp), run_time=0.5)

        defn = T(
            "Fatal OS fault: kernel halts to prevent further data corruption.",
            sz=22,
            col=NEO_WHITE,
        )
        defn.next_to(kp, DOWN, buff=0.35)
        self.play(FadeIn(defn))

        exs = VGroup(
            T("Linux:   Kernel panic - not syncing: VFS: ...", sz=18, col=NEO_RED),
            T("macOS:   *** panic: We are hanging here ***", sz=18, col=NEO_RED),
            T("Windows: :( STOP 0x0000007B BSOD", sz=18, col=NEO_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        exs.next_to(defn, DOWN, buff=0.35)

        self.flash_in(exs, 0.15)
        for _ in range(2):
            self.play(bd.animate.set_stroke(color=NEO_YELLOW), run_time=0.1)
            self.play(bd.animate.set_stroke(color=NEO_RED), run_time=0.1)
        self.wait(1.2)
        self.play(FadeOut(VGroup(bd, skull, kp, defn, exs)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S20 – KERNEL COMPONENTS
# ══════════════════════════════════════════════════════════════════════════════
class S20_Kernel(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)
        h = hdr("THE KERNEL", NEO_GREEN)
        h.to_edge(UP, buff=0.45)
        self.play(FadeIn(h))

        defn = T(
            "Privileged core · manages HW, processes, memory, devices & syscalls.",
            sz=20,
            col=NEO_WHITE,
        )
        defn.next_to(h, DOWN, buff=0.32)
        self.play(Write(defn), run_time=0.7)

        center = Circle(
            radius=1.15,
            color=NEO_GREEN,
            stroke_width=2.5,
            fill_color="#001100",
            fill_opacity=0.9,
        )
        c_lbl = T("KERNEL", sz=22, col=NEO_GREEN, bold=True)
        center.move_to(DOWN * 0.8)
        c_lbl.move_to(center)

        sats = {
            "Process\nScheduler": (UP * 2.1 + LEFT * 0.0, NEO_CYAN),
            "Memory\nManager": (LEFT * 3.4 + DOWN * 0.8, NEO_PURPLE),
            "File\nSystem": (RIGHT * 3.4 + DOWN * 0.8, NEO_YELLOW),
            "Device\nDrivers": (DOWN * 2.5, NEO_RED),
            "System\nCalls": (UP * 1.2 + RIGHT * 3.1, NEO_WHITE),
        }
        sat_grps = {}
        sat_lines = VGroup()
        for nm, (pos, col) in sats.items():
            sb = Circle(
                radius=0.68,
                color=col,
                stroke_width=1.5,
                fill_color=BG_BLACK,
                fill_opacity=0.9,
            )
            sb.move_to(pos + DOWN * 0.8)
            sl_ = T(nm, sz=14, col=col, bold=True)
            sl_.move_to(sb)
            sat_grps[nm] = VGroup(sb, sl_)
            sat_lines.add(
                Line(center.get_center(), sb.get_center(), color=col, stroke_width=1.0)
            )

        self.play(FadeIn(VGroup(center, c_lbl)))
        self.play(Create(sat_lines), run_time=0.7)
        self.flash_in(VGroup(*sat_grps.values()), 0.12)
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(bd, h, defn, center, c_lbl, sat_lines, *sat_grps.values())),
            run_time=0.5,
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S21 – BATTERY NOT INCLUDED
# ══════════════════════════════════════════════════════════════════════════════
class S21_NotIncluded(NeoSlide):
    def construct(self):
        bd = glowing_border(NEO_RED)
        self.play(Create(bd), run_time=0.5)

        hd = T("BATTERY NOT INCLUDED", sz=44, col=NEO_RED, bold=True)
        hd.to_edge(UP, buff=0.48)
        self.play(Write(hd), run_time=0.6)

        inc = VGroup(
            T("KERNEL INCLUDES:", sz=24, col=NEO_GREEN, bold=True),
            T("✓ Filesystem driver", sz=22, col=NEO_GREEN),
            T("✓ Process scheduler", sz=22, col=NEO_GREEN),
            T("✓ System call interface", sz=22, col=NEO_GREEN),
            T("✓ Memory manager (MMU)", sz=22, col=NEO_GREEN),
            T("✓ Interrupt/trap handler", sz=22, col=NEO_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        notinc = VGroup(
            T("NOT IN KERNEL:", sz=24, col=NEO_RED, bold=True),
            T("❌ Shell / Terminal", sz=22, col=NEO_RED),
            T("❌ Text editor (vim/nano)", sz=22, col=NEO_RED),
            T("❌ GUI / Window manager / Desktop", sz=22, col=NEO_RED),
            T("❌ Programming languages & interpreters", sz=22, col=NEO_RED),
            T("❌ Web browser / media player", sz=22, col=NEO_RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        panels = VGroup(inc, notinc).arrange(RIGHT, buff=1.3)
        panels.next_to(hd, DOWN, buff=0.45)

        note = T(
            "Linux kernel ~30M lines  |  Plan9 ~100k lines  |  TempleOS ~100k lines",
            sz=18,
            col=NEO_PURPLE,
        )
        note.to_edge(DOWN, buff=0.32)

        self.flash_in(inc, 0.1)
        self.flash_in(notinc, 0.1)
        self.play(FadeIn(note))
        self.wait(2.0)
        self.play(FadeOut(VGroup(bd, hd, panels, note)), run_time=0.5)


# ══════════════════════════════════════════════════════════════════════════════
#  S22 – OOP ASSEMBLY (final assembly slide-by-slide)
# ══════════════════════════════════════════════════════════════════════════════
class S22_Assembly(NeoSlide):
    def construct(self):
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)

        hd = T("ASSEMBLING THE OS  ·  OOP", sz=40, col=NEO_GREEN, bold=True)
        hd.set_color_by_gradient(NEO_GREEN, NEO_CYAN)
        hd.to_edge(UP, buff=0.45)
        line = hr(NEO_GREEN, 12)
        line.next_to(hd, DOWN, buff=0.1)
        self.play(FadeIn(hd), Create(line))

        classes = [
            ("class BootLoader", NEO_YELLOW),
            ("class FileSystem", NEO_PURPLE),
            ("class Scheduler", NEO_CYAN),
            ("class Pager", NEO_WHITE),
            ("class SysCall", NEO_GREEN),
            ("class Interrupt", NEO_RED),
        ]
        class_boxes = VGroup()
        for cname, col in classes:
            b = RoundedRectangle(
                width=3.5,
                height=0.65,
                corner_radius=0.08,
                stroke_color=col,
                stroke_width=1.8,
                fill_color=col,
                fill_opacity=0.07,
            )
            t = T(cname, sz=19, col=col, bold=True)
            t.move_to(b)
            class_boxes.add(VGroup(b, t))

        class_boxes.arrange_in_grid(2, 3, buff=(0.4, 0.28))
        class_boxes.next_to(line, DOWN, buff=0.45)

        kern_banner = RoundedRectangle(
            width=12.2,
            height=0.75,
            corner_radius=0.1,
            stroke_color=NEO_GREEN,
            stroke_width=2.5,
            fill_color=NEO_GREEN,
            fill_opacity=0.1,
        )
        kern_txt = T(
            "class Kernel(BootLoader, FileSystem, Scheduler, Pager, SysCall, Interrupt):",
            sz=19,
            col=NEO_GREEN,
            bold=True,
        )
        kern_txt.move_to(kern_banner)
        kern_grp = VGroup(kern_banner, kern_txt)
        kern_grp.to_edge(DOWN, buff=0.35)

        for box in class_boxes:
            self.play(FadeIn(box, scale=0.7), run_time=0.2)
        self.wait(0.3)

        arrows_ = VGroup(
            *[
                Arrow(
                    box.get_bottom(),
                    kern_grp.get_top(),
                    buff=0.05,
                    color=NEO_DIM,
                    stroke_width=1.0,
                    max_tip_length_to_length_ratio=0.1,
                )
                for box in class_boxes
            ]
        )
        self.play(Create(arrows_), run_time=0.7)
        self.play(FadeIn(kern_grp))
        self.glitch(kern_grp)

        self.wait(2.0)
        self.play(
            FadeOut(VGroup(bd, hd, line, class_boxes, arrows_, kern_grp)), run_time=0.5
        )


# ══════════════════════════════════════════════════════════════════════════════
#  S23 – END CARD
# ══════════════════════════════════════════════════════════════════════════════
class S23_EndCard(NeoSlide):
    def construct(self):
        self.rain_in(0.5)
        bd = glowing_border()
        self.play(Create(bd), run_time=0.5)

        big = T("NOW GO BUILD IT.", sz=56, col=NEO_GREEN, bold=True)
        big.set_color_by_gradient(NEO_GREEN, NEO_CYAN, NEO_PURPLE)
        big.move_to(UP * 1.5)

        sub = T("Your OS. Your rules. Your ring-0.", sz=30, col=NEO_CYAN)
        sub.next_to(big, DOWN, buff=0.45)

        cta = T("git init my_os  &&  vim kernel/main.c", sz=26, col=NEO_GREEN)
        cta.next_to(sub, DOWN, buff=0.4)

        tip = T(
            "Start: write a 512-byte MBR that prints 'Hello' in 16-bit real mode.",
            sz=20,
            col=NEO_DIM,
        )
        tip.next_to(cta, DOWN, buff=0.28)

        cur = T("█", sz=30, col=NEO_GREEN)
        cur.next_to(cta, RIGHT, buff=0.06)

        self.play(Write(big), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1))
        self.play(FadeIn(cta))
        self.play(FadeIn(cur))
        self.play(Blink(cur, blinks=3))
        self.play(FadeIn(tip))

        rain2 = rain_chars(55)
        rain2.set_opacity(0.12)
        self.add(rain2)
        self.wait(3.0)
        self.play(FadeOut(VGroup(bd, big, sub, cta, cur, tip, rain2)), run_time=1.0)


# ══════════════════════════════════════════════════════════════════════════════
#  FULL PRESENTATION  ← render this
# ══════════════════════════════════════════════════════════════════════════════
class FullPresentation(
    S01_Title,
    S02_Terry,
    S03_Paradigms,
    S04_Pbit,
    S05_Trits,
    S06_WoodPhone,
    S07_Processors,
    S08_VonNeumann,
    S09_ISA,
    S10_GPUMisconception,
    S11_Definition,
    S12_PythonOS,
    S13_BootLoader,
    S14_Scheduler,
    S15_FileSystem,
    S16_Paging,
    S17_SysCalls,
    S18_Interrupts,
    S19_KernelPanic,
    S20_Kernel,
    S21_NotIncluded,
    S22_Assembly,
    S23_EndCard,
):
    def setup(self):
        self.camera.background_color = BG_BLACK

    def construct(self):
        slide_names = [
            S01_Title,
            S02_Terry,
            S03_Paradigms,
            S06_WoodPhone,
            S04_Pbit,
            S05_Trits,
            S07_Processors,
            S08_VonNeumann,
            S09_ISA,
            S10_GPUMisconception,
            S11_Definition,
            S12_PythonOS,
            S13_BootLoader,
            S14_Scheduler,
            S15_FileSystem,
            S16_Paging,
            S17_SysCalls,
            S18_Interrupts,
            S19_KernelPanic,
            S20_Kernel,
            S21_NotIncluded,
            S22_Assembly,
            S23_EndCard,
        ]
        for SlideClass in slide_names:
            SlideClass.construct(self)
