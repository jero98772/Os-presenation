from manim import *
import random

# ── PALETTE ──────────────────────────────────────────────────
NEO_GREEN = "#00FF41"
NEO_CYAN = "#00FFFF"
NEO_PURPLE = "#BF00FF"
NEO_YELLOW = "#FFFF00"
NEO_RED = "#FF0040"
NEO_WHITE = "#E0FFE0"
NEO_DIM = "#003B00"
BG_BLACK = "#000000"


# ── HELPERS ───────────────────────────────────────────────────
def T(text, size=22, color=NEO_WHITE, bold=False):
    return Text(
        text,
        font="Courier New",
        font_size=size,
        color=color,
        weight=BOLD if bold else NORMAL,
    )


def neo_box(w, h, color=NEO_GREEN, fill_op=0.07, radius=0.1):
    return RoundedRectangle(
        width=w,
        height=h,
        corner_radius=radius,
        stroke_color=color,
        stroke_width=2,
        fill_color=color,
        fill_opacity=fill_op,
    )


def hline(color=NEO_GREEN, width=11):
    return Line(LEFT * width / 2, RIGHT * width / 2, color=color, stroke_width=1)


def rain_chars(n=30, opacity=1.0):
    pool = "01アイウエカキクサシスセタチツ{}[]<>"
    g = VGroup()
    for _ in range(n):
        c = Text(
            random.choice(pool),
            font="Courier New",
            font_size=14,
            color=random.choice([NEO_GREEN, NEO_DIM, "#007020"]),
        )
        c.move_to([random.uniform(-6.5, 6.5), random.uniform(-3.8, 3.8), 0])
        g.add(c)
    g.set_opacity(opacity)
    return g


def sec_hdr(text, color=NEO_CYAN):
    t = T(text, 36, color, bold=True)
    l = hline(color)
    l.next_to(t, DOWN, buff=0.1)
    return VGroup(t, l)


def glow_border(color=NEO_GREEN):
    return RoundedRectangle(
        width=13,
        height=7.4,
        corner_radius=0.15,
        stroke_color=color,
        stroke_width=2,
        fill_opacity=0,
    )


# ── SINGLE SCENE ──────────────────────────────────────────────
class FullPresentation(Scene):
    def setup(self):
        self.camera.background_color = BG_BLACK

    # ── shared helpers that use self.play / self.wait ─────────
    def rain(self, dur=0.5, n=35, op=1.0):
        r = rain_chars(n, op)
        self.add(r)
        self.wait(dur)
        self.remove(r)

    def flash_in(self, mob, lag=0.05):
        items = mob if isinstance(mob, (list, tuple)) else list(mob)
        for m in items:
            self.play(FadeIn(m, shift=DOWN * 0.08), run_time=0.22)

    def slide_border(self, color=NEO_GREEN):
        b = glow_border(color)
        self.play(Create(b), run_time=0.4)
        return b

    def out(self, *mobs):
        self.play(FadeOut(VGroup(*mobs)), run_time=0.5)

    # ═════════════════════════════════════════════════════════
    def construct(self):
        self.slide_01_title()
        self.slide_02_terry()
        self.slide_03_paradigms()
        self.slide_04_wood()
        self.slide_05_processors()
        self.slide_06_isa()
        self.slide_07_gpu_myth()
        self.slide_08_definition()
        self.slide_09_python_os()
        self.slide_10_bootloader()
        self.slide_11_scheduler()
        self.slide_12_filesystem()
        self.slide_13_paging()
        self.slide_14_syscalls()
        self.slide_15_interrupts()
        self.slide_16_kernel_panic()
        self.slide_17_kernel()
        self.slide_18_not_included()
        self.slide_19_assembly()
        self.slide_20_end()

    # ═══════════════════════════════════════════════════════
    # SLIDE 01 – TITLE
    # ═══════════════════════════════════════════════════════
    def slide_01_title(self):
        self.rain(0.4)
        b = self.slide_border()

        tag = T("// OS FROM SCRATCH", 18, NEO_DIM)
        title = T("BUILDING AN\nOPERATING SYSTEM", 52, NEO_GREEN, bold=True)
        title.set_color_by_gradient(NEO_GREEN, NEO_CYAN)
        sub = T("Object-Oriented Approach", 26, NEO_CYAN)
        name = T("[ Made by a Real Programmer ]", 22, NEO_PURPLE)
        cur = T("█", 28, NEO_GREEN)

        tag.to_corner(UL, buff=0.4)
        title.move_to(UP * 0.5)
        sub.next_to(title, DOWN, buff=0.45)
        name.next_to(sub, DOWN, buff=0.3)
        cur.next_to(name, RIGHT, buff=0.08)

        self.play(FadeIn(tag))
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.15))
        self.play(FadeIn(name))
        self.play(FadeIn(cur))
        self.play(Blink(cur, blinks=2))
        self.wait(1.2)
        self.out(b, tag, title, sub, name, cur)

    # ═══════════════════════════════════════════════════════
    # SLIDE 02 – TERRY DAVIS
    # ═══════════════════════════════════════════════════════
    def slide_02_terry(self):
        self.rain(0.3)
        b = self.slide_border()

        quote = T(
            "\"You're a real programmer\nwhen you've made a programming\nlanguage and an operating system\"",
            26,
            NEO_YELLOW,
            bold=True,
        )
        quote.move_to(UP * 1.8)
        dash = T("— The Community", 20, NEO_DIM)
        dash.next_to(quote, DOWN, buff=0.25)
        div = hline(NEO_CYAN, 10)
        div.next_to(dash, DOWN, buff=0.4)

        info = VGroup(
            T("Terry A. Davis", 30, NEO_CYAN, bold=True),
            T("→  TempleOS  (single-user, ring-0 only, 64-bit)", 22, NEO_GREEN),
            T("→  HolyC  (custom language, real-time compilation)", 22, NEO_PURPLE),
            T("→  100 000 lines  ·  1 man  ·  1 God", 22, NEO_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        info.next_to(div, DOWN, buff=0.3)

        self.play(Write(quote), run_time=1.2)
        self.play(FadeIn(dash))
        self.play(Create(div))
        self.flash_in(info)
        self.wait(1.8)
        self.out(b, quote, dash, div, info)

    # ═══════════════════════════════════════════════════════
    # SLIDE 03 – HARDWARE PARADIGMS
    # ═══════════════════════════════════════════════════════
    def slide_03_paradigms(self):
        b = self.slide_border()
        hdr = sec_hdr("HARDWARE PARADIGMS OF COMPUTATION", NEO_CYAN)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        rows = [
            ("❌", "Quantum", "NOT OS – no classical control flow", NEO_RED),
            ("❌", "Thermodynamic", "NOT OS – entropy-based, no binary", NEO_RED),
            ("⚠", "Photonic", "Possible – optical compute", NEO_YELLOW),
            ("❌", "Biological", "NOT OS – DNA / protein compute", NEO_RED),
            ("✓", "Electronic", "YES – silicon Von-Neumann, our world", NEO_GREEN),
        ]

        items = VGroup()
        for icon, name, desc, col in rows:
            row = VGroup(
                T(icon, 20, col),
                T(name, 22, col, bold=True),
                T(desc, 18, NEO_WHITE),
            ).arrange(RIGHT, buff=0.35, aligned_edge=UP)
            items.add(row)
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        items.next_to(hdr, DOWN, buff=0.45)
        items.to_edge(LEFT, buff=0.6)

        bits = T("P-bit  vs  Bit  vs  Trit  vs  Q-bit", 22, NEO_PURPLE)
        bits.to_edge(DOWN, buff=0.4)

        self.flash_in(items)
        self.play(FadeIn(bits))
        self.wait(1.5)
        self.out(b, hdr, items, bits)

    # ═══════════════════════════════════════════════════════
    # SLIDE 04 – WOOD TRANSISTORS
    # ═══════════════════════════════════════════════════════
    def slide_04_wood(self):
        b = self.slide_border()
        hdr = sec_hdr("WOOD TRANSISTORS & MIT WOOD PHONE", NEO_YELLOW)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        # Symbolic transistor diagram
        body = Rectangle(
            width=1.4,
            height=2.2,
            stroke_color="#8B4513",
            stroke_width=3,
            fill_color="#3B1A08",
            fill_opacity=0.7,
        )
        gate = Line(LEFT * 0.55, RIGHT * 0.55, color="#D2691E", stroke_width=3)
        gate.next_to(body, LEFT, buff=0)
        src = Arrow(
            ORIGIN,
            DOWN * 0.6,
            color=NEO_GREEN,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        )
        src.next_to(body, DOWN, buff=0)
        drain = Arrow(
            ORIGIN,
            UP * 0.6,
            color=NEO_GREEN,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        )
        drain.next_to(body, UP, buff=0)

        lg = T("Gate", 16, "#D2691E")
        lg.next_to(gate, LEFT, buff=0.08)
        ls = T("Source", 14, NEO_GREEN)
        ls.next_to(src, DOWN, buff=0.04)
        ld = T("Drain", 14, NEO_GREEN)
        ld.next_to(drain, UP, buff=0.04)

        trans = VGroup(body, gate, src, drain, lg, ls, ld)
        trans.scale(0.9).move_to(LEFT * 3.8 + DOWN * 0.3)

        facts = VGroup(
            T("MIT Wood Innovation Lab (2023)", 24, NEO_YELLOW, bold=True),
            T("Transistors from cellulose nano-fibers", 21, NEO_WHITE),
            T("Wood-based smartphone prototype", 21, NEO_WHITE),
            T("Biodegradable electronics – future green HW", 21, NEO_WHITE),
            T("Still classical binary → OS compatible!", 21, NEO_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        facts.move_to(RIGHT * 2.0 + DOWN * 0.2)

        self.play(Create(trans), run_time=0.9)
        self.flash_in(facts)
        self.wait(1.5)
        self.out(b, hdr, trans, facts)

    # ═══════════════════════════════════════════════════════
    # SLIDE 05 – WHERE TO PROCESS
    # ═══════════════════════════════════════════════════════
    def slide_05_processors(self):
        b = self.slide_border()
        hdr = sec_hdr("WHERE DOES THE MAGIC HAPPEN?", NEO_CYAN)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        units = [
            ("CPU", "General purpose · few fast cores · OS lives here", NEO_GREEN),
            ("GPU", "Massively parallel · thousands of tiny cores", NEO_CYAN),
            ("TPU", "Tensor ops · Google · ML training & inference", NEO_PURPLE),
            ("FPGA", "Reconfigurable logic gates · hardware emulation", NEO_YELLOW),
            ("ASIC", "Fixed-function · highest perf/watt · e.g. Apple M-chip", NEO_RED),
        ]

        boxes = VGroup()
        for label, desc, col in units:
            box = RoundedRectangle(
                width=11,
                height=0.75,
                corner_radius=0.08,
                stroke_color=col,
                stroke_width=1.5,
                fill_color=col,
                fill_opacity=0.07,
            )
            row = VGroup(T(label, 22, col, bold=True), T(desc, 18, NEO_WHITE)).arrange(
                RIGHT, buff=0.5
            )
            row.move_to(box).to_edge(LEFT, buff=0.75)
            boxes.add(VGroup(box, row))
        boxes.arrange(DOWN, buff=0.18).next_to(hdr, DOWN, buff=0.4)

        arch = T(
            "Von Neumann (shared bus)  vs  Harvard (split memory) architecture",
            20,
            NEO_PURPLE,
        )
        arch.to_edge(DOWN, buff=0.38)

        self.flash_in(boxes)
        self.play(FadeIn(arch))
        self.wait(1.5)
        self.out(b, hdr, boxes, arch)

    # ═══════════════════════════════════════════════════════
    # SLIDE 06 – ISA
    # ═══════════════════════════════════════════════════════
    def slide_06_isa(self):
        b = self.slide_border()
        hdr = sec_hdr("ISA:  ARM  ·  x86  ·  RISC-V", NEO_GREEN)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        data = [
            (
                "ARM",
                NEO_CYAN,
                [
                    "RISC · energy-efficient",
                    "Mobile / Apple M1+",
                    "Closed ISA (licence)",
                ],
            ),
            (
                "x86",
                NEO_YELLOW,
                [
                    "CISC · complex instructions",
                    "Desktops & servers",
                    "Intel / AMD duopoly",
                ],
            ),
            (
                "RISC-V",
                NEO_GREEN,
                [
                    "Open ISA · royalty-free",
                    "AI edge devices",
                    "Custom extensions OK",
                    "Future of embedded OS",
                ],
            ),
        ]
        cols = VGroup()
        for name, col, pts in data:
            box = neo_box(3.7, 3.6, col)
            title_t = T(name, 26, col, bold=True)
            bullets = VGroup(*[T("• " + p, 17, NEO_WHITE) for p in pts]).arrange(
                DOWN, aligned_edge=LEFT, buff=0.15
            )
            content = VGroup(title_t, bullets).arrange(
                DOWN, buff=0.2, aligned_edge=LEFT
            )
            content.move_to(box).shift(LEFT * 0.1)
            cols.add(VGroup(box, content))

        cols.arrange(RIGHT, buff=0.45).next_to(hdr, DOWN, buff=0.5)

        note = T("RISC-V → perfect for AI-edge OSes (not GPU OS!)", 20, NEO_PURPLE)
        note.to_edge(DOWN, buff=0.38)

        self.flash_in(cols)
        self.play(FadeIn(note))
        self.wait(1.8)
        self.out(b, hdr, cols, note)

    # ═══════════════════════════════════════════════════════
    # SLIDE 07 – GPU MYTH
    # ═══════════════════════════════════════════════════════
    def slide_07_gpu_myth(self):
        b = self.slide_border()

        big = T('"I built an OS for the GPU"', 40, NEO_RED, bold=True)
        big.move_to(UP * 2.6)
        face = T("( ͡° ͜ʖ ͡°)", 50, NEO_YELLOW)
        face.next_to(big, DOWN, buff=0.3)
        why = T("WHY IS THIS HARD TO UNDERSTAND?", 28, NEO_CYAN, bold=True)
        why.next_to(face, DOWN, buff=0.4)

        pts = VGroup(
            T("• A GPU has NO interrupt controller", 20, NEO_WHITE),
            T("• A GPU cannot boot itself", 20, NEO_WHITE),
            T("• A GPU has no privileged / user rings", 20, NEO_WHITE),
            T("• A GPU is an accelerator — not a HOST", 20, NEO_RED, bold=True),
            T("• The OS manages the GPU, not vice versa", 20, NEO_GREEN, bold=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        pts.next_to(why, DOWN, buff=0.3).to_edge(LEFT, buff=0.8)

        self.play(Write(big), run_time=0.7)
        self.play(FadeIn(face))
        self.play(FadeIn(why))
        self.flash_in(pts)
        self.wait(1.8)
        self.out(b, big, face, why, pts)

    # ═══════════════════════════════════════════════════════
    # SLIDE 08 – FORMAL DEFINITION
    # ═══════════════════════════════════════════════════════
    def slide_08_definition(self):
        b = self.slide_border()
        hdr = T("FORMAL DEFINITION OF OS", 34, NEO_CYAN, bold=True)
        hdr.to_edge(UP, buff=0.5)
        hl = hline(NEO_CYAN)
        hl.next_to(hdr, DOWN, buff=0.1)
        self.play(FadeIn(hdr), Create(hl))

        defn = Text(
            "An operating system (OS) is a system software\n"
            "layer that manages the hardware resources of a\n"
            "computer and provides services, abstractions,\n"
            "and interfaces that enable application programs\n"
            "and users to execute and interact with the system\n"
            "efficiently, securely, and reliably.",
            font="Courier New",
            font_size=22,
            color=NEO_WHITE,
            line_spacing=1.4,
        )
        defn.next_to(hl, DOWN, buff=0.4)

        kws = VGroup(
            T("► manages hardware resources", 22, NEO_GREEN),
            T("► provides services & abstractions", 22, NEO_CYAN),
            T("► efficient · secure · reliable", 22, NEO_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        kws.to_edge(DOWN, buff=0.4)

        self.play(Write(defn), run_time=2.0)
        self.flash_in(kws)
        self.wait(1.5)
        self.out(b, hdr, hl, defn, kws)

    # ═══════════════════════════════════════════════════════
    # SLIDE 09 – PYTHON OS DEBATE
    # ═══════════════════════════════════════════════════════
    def slide_09_python_os(self):
        b = self.slide_border()
        hdr = sec_hdr("OPERATING SYSTEM IN PYTHON???", NEO_RED)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        lh = T("🚫  Skeptic says:", 24, NEO_RED, bold=True)
        lp = VGroup(
            T("No write→compile→binary pipeline", 19, NEO_WHITE),
            T("No raw pointer arithmetic", 19, NEO_WHITE),
            T("Can't inline assembler", 19, NEO_WHITE),
            T("GIL blocks true parallelism", 19, NEO_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        left = VGroup(lh, lp).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        rh = T("✓   Smart guy says:", 24, NEO_GREEN, bold=True)
        rp = VGroup(
            T("Save state in .pkl / shelve", 19, NEO_WHITE),
            T("Combine with C via ctypes / cffi", 19, NEO_WHITE),
            T("Call asm from subprocess / pty", 19, NEO_WHITE),
            T("Compile with Cython / Mypyc", 19, NEO_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        right = VGroup(rh, rp).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        both = VGroup(left, right).arrange(RIGHT, buff=1.1)
        both.next_to(hdr, DOWN, buff=0.5)

        verdict = T(
            "Best: C / C++ / Rust / Assembly — Python can bootstrap!", 20, NEO_YELLOW
        )
        verdict.to_edge(DOWN, buff=0.4)

        self.flash_in(left)
        self.flash_in(right)
        self.play(FadeIn(verdict))
        self.wait(1.8)
        self.out(b, hdr, both, verdict)

    # ═══════════════════════════════════════════════════════
    # SLIDE 10 – BOOT LOADER (animated pipeline)
    # ═══════════════════════════════════════════════════════
    def slide_10_bootloader(self):
        b = self.slide_border()
        hdr = sec_hdr("BOOT LOADER", NEO_GREEN)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        defn = T(
            "First program after power-on: init HW → load kernel → hand over control.",
            20,
            NEO_WHITE,
        )
        defn.next_to(hdr, DOWN, buff=0.35)
        self.play(Write(defn), run_time=0.9)

        stages = [
            ("POWER ON", NEO_YELLOW),
            ("BIOS/UEFI", NEO_CYAN),
            ("MBR/GPT", NEO_PURPLE),
            ("GRUB", NEO_GREEN),
            ("KERNEL", NEO_RED),
        ]

        sboxes = VGroup()
        for label, col in stages:
            box = neo_box(1.85, 0.72, col)
            lbl = T(label, 17, col, bold=True)
            lbl.move_to(box)
            sboxes.add(VGroup(box, lbl))
        sboxes.arrange(RIGHT, buff=0.4).next_to(defn, DOWN, buff=0.65)

        arrows = VGroup(
            *[
                Arrow(
                    sboxes[i].get_right(),
                    sboxes[i + 1].get_left(),
                    buff=0.05,
                    color=NEO_GREEN,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.2,
                )
                for i in range(len(sboxes) - 1)
            ]
        )

        # Code snippet
        code_lines = VGroup(
            T("[0x7C00] MBR loaded ✓", 18, NEO_GREEN),
            T("Jumping to 0x100000…", 18, NEO_CYAN),
            T("Kernel entry: _start()", 18, NEO_RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        code_lines.to_edge(DOWN, buff=0.4)

        for sb in sboxes:
            self.play(FadeIn(sb, scale=0.8), run_time=0.28)
        for ar in arrows:
            self.play(Create(ar), run_time=0.18)
        self.flash_in(code_lines)

        cur = T("█", 20, NEO_RED)
        cur.next_to(code_lines[-1], RIGHT, buff=0.05)
        self.play(FadeIn(cur))
        self.play(Blink(cur, blinks=3))
        self.wait(1.0)
        self.out(b, hdr, defn, sboxes, arrows, code_lines, cur)

    # ═══════════════════════════════════════════════════════
    # SLIDE 11 – SCHEDULER (animated queue)
    # ═══════════════════════════════════════════════════════
    def slide_11_scheduler(self):
        b = self.slide_border()
        hdr = sec_hdr("PROCESS SCHEDULER", NEO_CYAN)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        defn = T(
            "Selects which runnable process gets CPU time · determines order & duration.",
            20,
            NEO_WHITE,
        )
        defn.next_to(hdr, DOWN, buff=0.35)
        self.play(Write(defn), run_time=0.9)

        # CPU box
        cpu_box = neo_box(2.1, 1.15, NEO_GREEN)
        cpu_lbl = T("CPU", 26, NEO_GREEN, bold=True)
        cpu_lbl.move_to(cpu_box)
        cpu = VGroup(cpu_box, cpu_lbl)
        cpu.move_to(RIGHT * 3.8 + DOWN * 0.6)

        # Queue
        procs = [
            ("P1", NEO_CYAN),
            ("P2", NEO_PURPLE),
            ("P3", NEO_YELLOW),
            ("P4", NEO_RED),
        ]
        queue = VGroup()
        for name, col in procs:
            bx = neo_box(1.2, 0.65, col)
            lb = T(name, 20, col, bold=True)
            lb.move_to(bx)
            queue.add(VGroup(bx, lb))
        queue.arrange(RIGHT, buff=0.18)
        queue.move_to(LEFT * 2.6 + DOWN * 0.6)

        qlbl = T("Ready Queue →", 18, NEO_DIM)
        qlbl.next_to(queue, UP, buff=0.12)

        sched_arrow = Arrow(
            queue.get_right(),
            cpu.get_left(),
            buff=0.1,
            color=NEO_GREEN,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.15,
        )

        self.play(FadeIn(qlbl))
        for p in queue:
            self.play(FadeIn(p, shift=RIGHT * 0.25), run_time=0.2)
        self.play(FadeIn(cpu))
        self.play(Create(sched_arrow))

        # Dispatch P1
        p1_copy = queue[0].copy()
        self.play(p1_copy.animate.move_to(cpu).scale(0.8), run_time=0.65)
        self.play(FadeOut(p1_copy), run_time=0.2)
        self.play(queue[1:].animate.shift(LEFT * 1.38), run_time=0.45)
        self.wait(1.0)
        self.out(b, hdr, defn, queue, cpu, sched_arrow, qlbl)

    # ═══════════════════════════════════════════════════════
    # SLIDE 12 – FILE SYSTEM
    # ═══════════════════════════════════════════════════════
    def slide_12_filesystem(self):
        b = self.slide_border()
        hdr = sec_hdr("FILE SYSTEM", NEO_PURPLE)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        defn = T(
            "Organises, stores, retrieves and manages persistent data on storage devices.",
            20,
            NEO_WHITE,
        )
        defn.next_to(hdr, DOWN, buff=0.35)
        self.play(Write(defn), run_time=0.9)

        root = T("/", 30, NEO_PURPLE, bold=True)
        root.move_to(UP * 0.75)

        branches = {
            "bin": (LEFT * 3.6, NEO_GREEN),
            "dev": (LEFT * 1.8, NEO_CYAN),
            "etc": (ORIGIN, NEO_YELLOW),
            "home": (RIGHT * 1.8, NEO_WHITE),
            "proc": (RIGHT * 3.6, NEO_RED),
        }

        nodes, lines_ = VGroup(), VGroup()
        for name, (pos, col) in branches.items():
            n = T(name, 22, col, bold=True)
            n.move_to(DOWN * 0.4 + pos)
            nodes.add(n)
            lines_.add(
                Line(root.get_bottom(), n.get_top(), color=col, stroke_width=1.2)
            )

        types = T("ext4  FAT32  NTFS  ZFS  BTRFS  HFS+", 20, NEO_CYAN)
        types.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(root))
        self.play(Create(lines_), run_time=0.7)
        self.flash_in(nodes)
        self.play(FadeIn(types))
        self.wait(1.5)
        self.out(b, hdr, defn, root, lines_, nodes, types)

    # ═══════════════════════════════════════════════════════
    # SLIDE 13 – PAGING (animated)
    # ═══════════════════════════════════════════════════════
    def slide_13_paging(self):
        b = self.slide_border()
        hdr = sec_hdr("PAGING SYSTEM  (VIRTUAL MEMORY)", NEO_YELLOW)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        defn = T(
            "Divides virtual + physical memory into fixed-size pages/frames → isolation & protection.",
            19,
            NEO_WHITE,
        )
        defn.next_to(hdr, DOWN, buff=0.3)
        self.play(Write(defn), run_time=0.9)

        n = 4
        vpages, pframes = VGroup(), VGroup()
        for i in range(n):
            vp = neo_box(1.4, 0.5, NEO_CYAN, 0.08)
            vt = T(f"VP {i}", 16, NEO_CYAN)
            vt.move_to(vp)
            vpages.add(VGroup(vp, vt))

            pf = neo_box(1.4, 0.5, NEO_GREEN, 0.08)
            pt = T(f"PF {i}", 16, NEO_GREEN)
            pt.move_to(pf)
            pframes.add(VGroup(pf, pt))

        vpages.arrange(DOWN, buff=0.16).move_to(LEFT * 4.3 + DOWN * 0.3)
        pframes.arrange(DOWN, buff=0.16).move_to(RIGHT * 4.3 + DOWN * 0.3)

        pt_box = neo_box(2.0, 2.7, NEO_YELLOW, 0.06)
        pt_lbl = T("PAGE\nTABLE", 18, NEO_YELLOW, bold=True)
        pt_lbl.move_to(pt_box)
        ptg = VGroup(pt_box, pt_lbl).move_to(DOWN * 0.3)

        vlbl = T("Virtual\nAddress", 18, NEO_CYAN)
        vlbl.next_to(vpages, UP, buff=0.12)
        plbl = T("Physical\nRAM", 18, NEO_GREEN)
        plbl.next_to(pframes, UP, buff=0.12)

        arr_in = VGroup(
            *[
                Arrow(
                    vpages[i].get_right(),
                    ptg.get_left(),
                    buff=0.05,
                    color=NEO_CYAN,
                    stroke_width=1.2,
                    max_tip_length_to_length_ratio=0.12,
                )
                for i in range(n)
            ]
        )
        arr_out = VGroup(
            *[
                Arrow(
                    ptg.get_right(),
                    pframes[i].get_left(),
                    buff=0.05,
                    color=NEO_GREEN,
                    stroke_width=1.2,
                    max_tip_length_to_length_ratio=0.12,
                )
                for i in range(n)
            ]
        )

        self.play(FadeIn(vlbl), FadeIn(plbl))
        for vp, pf in zip(vpages, pframes):
            self.play(
                FadeIn(vp, shift=RIGHT * 0.15),
                FadeIn(pf, shift=LEFT * 0.15),
                run_time=0.22,
            )
        self.play(FadeIn(ptg))
        self.play(Create(arr_in), run_time=0.5)
        self.play(Create(arr_out), run_time=0.5)
        self.wait(1.2)
        self.out(b, hdr, defn, vpages, pframes, ptg, arr_in, arr_out, vlbl, plbl)

    # ═══════════════════════════════════════════════════════
    # SLIDE 14 – SYSTEM CALLS
    # ═══════════════════════════════════════════════════════
    def slide_14_syscalls(self):
        b = self.slide_border()
        hdr = sec_hdr("SYSTEM CALLS", NEO_CYAN)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        defn = T(
            "Controlled interface: user-space program requests kernel services.",
            20,
            NEO_WHITE,
        )
        defn.next_to(hdr, DOWN, buff=0.35)
        self.play(Write(defn), run_time=0.8)

        ub = neo_box(3.8, 1.2, NEO_CYAN)
        ul = T("User Space\n(ring 3)", 20, NEO_CYAN)
        ul.move_to(ub)
        ug = VGroup(ub, ul).move_to(LEFT * 3.3 + DOWN * 0.6)

        kb = neo_box(3.8, 1.2, NEO_RED)
        kl = T("Kernel Space\n(ring 0)", 20, NEO_RED)
        kl.move_to(kb)
        kg = VGroup(kb, kl).move_to(RIGHT * 3.3 + DOWN * 0.6)

        a1 = CurvedArrow(
            ug.get_right(),
            kg.get_left(),
            angle=-TAU / 6,
            color=NEO_GREEN,
            stroke_width=2,
        )
        a2 = CurvedArrow(
            kg.get_left(),
            ug.get_right(),
            angle=-TAU / 6,
            color=NEO_YELLOW,
            stroke_width=2,
        )
        l1 = T("syscall()", 18, NEO_GREEN)
        l1.next_to(a1, UP, buff=0.08)
        l2 = T("return", 18, NEO_YELLOW)
        l2.next_to(a2, DOWN, buff=0.08)

        examples = T(
            "read() · write() · fork() · exec() · mmap() · ioctl()", 20, NEO_PURPLE
        )
        examples.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(ug), FadeIn(kg))
        self.play(Create(a1), FadeIn(l1))
        self.play(Create(a2), FadeIn(l2))
        self.play(FadeIn(examples))
        self.wait(1.5)
        self.out(b, hdr, defn, ug, kg, a1, a2, l1, l2, examples)

    # ═══════════════════════════════════════════════════════
    # SLIDE 15 – INTERRUPTS & TRAPS
    # ═══════════════════════════════════════════════════════
    def slide_15_interrupts(self):
        b = self.slide_border()
        hdr = sec_hdr("INTERRUPTS  &  TRAPS", NEO_RED)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        def panel(title, pts, col, side):
            box = neo_box(5.4, 3.6, col)
            tl = T(title, 26, col, bold=True)
            bul = VGroup(*[T("• " + p, 18, NEO_WHITE) for p in pts]).arrange(
                DOWN, aligned_edge=LEFT, buff=0.18
            )
            content = VGroup(tl, bul).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
            content.move_to(box).shift(LEFT * 0.1)
            grp = VGroup(box, content)
            grp.move_to(side + DOWN * 0.4)
            return grp

        ip = panel(
            "INTERRUPT",
            [
                "Async signal from hardware",
                "e.g. keyboard, timer tick",
                "Pauses current execution",
                "OS handles → resumes",
            ],
            NEO_YELLOW,
            LEFT * 3.1,
        )

        tp = panel(
            "TRAP",
            [
                "Sync exception from instruction",
                "e.g. div-by-zero, page fault",
                "Generated by current instr.",
                "→ OS trap handler fires",
            ],
            NEO_RED,
            RIGHT * 3.1,
        )

        self.play(FadeIn(ip), run_time=0.7)
        self.play(FadeIn(tp), run_time=0.7)
        self.wait(1.8)
        self.out(b, hdr, ip, tp)

    # ═══════════════════════════════════════════════════════
    # SLIDE 16 – KERNEL PANIC
    # ═══════════════════════════════════════════════════════
    def slide_16_kernel_panic(self):
        b = glow_border(NEO_RED)
        self.play(Create(b), run_time=0.4)

        skull = Text("💀", font_size=80).move_to(UP * 2.1)
        self.play(FadeIn(skull, scale=0.3), run_time=0.4)

        kp = T("KERNEL  PANIC", 50, NEO_RED, bold=True)
        kp.next_to(skull, DOWN, buff=0.2)
        self.play(Write(kp), run_time=0.6)

        defn = T(
            "Fatal OS error: kernel detects unrecoverable fault.\n"
            "Halts execution to prevent further data corruption.",
            22,
            NEO_WHITE,
        )
        defn.next_to(kp, DOWN, buff=0.4)
        self.play(FadeIn(defn))

        examples = VGroup(
            T("Linux  : Kernel panic - not syncing", 20, NEO_RED),
            T("macOS  : *** panic: We are hanging here", 20, NEO_RED),
            T("Windows: :( STOP 0x0000000A  BSOD", 20, NEO_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        examples.next_to(defn, DOWN, buff=0.38)
        self.flash_in(examples)

        # Red border blink
        for _ in range(2):
            self.play(b.animate.set_stroke(color=NEO_YELLOW), run_time=0.1)
            self.play(b.animate.set_stroke(color=NEO_RED), run_time=0.1)

        self.wait(1.2)
        self.out(b, skull, kp, defn, examples)

    # ═══════════════════════════════════════════════════════
    # SLIDE 17 – KERNEL
    # ═══════════════════════════════════════════════════════
    def slide_17_kernel(self):
        b = self.slide_border()
        hdr = sec_hdr("THE  KERNEL", NEO_GREEN)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr))

        defn = T(
            "Privileged core of the OS. Manages HW, processes, memory, devices & syscalls.",
            19,
            NEO_WHITE,
        )
        defn.next_to(hdr, DOWN, buff=0.3)
        self.play(Write(defn), run_time=0.9)

        center = Circle(
            radius=1.1,
            color=NEO_GREEN,
            stroke_width=2.5,
            fill_color="#001100",
            fill_opacity=0.95,
        )
        center.move_to(DOWN * 0.85)
        clbl = T("KERNEL", 20, NEO_GREEN, bold=True)
        clbl.move_to(center)

        sats = {
            "Process\nScheduler": (UP * 2.0 + LEFT * 0.2, NEO_CYAN),
            "Memory\nManager": (LEFT * 3.6 + DOWN * 0.85, NEO_PURPLE),
            "File\nSystem": (RIGHT * 3.6 + DOWN * 0.85, NEO_YELLOW),
            "Device\nDrivers": (DOWN * 2.6, NEO_RED),
            "System\nCalls": (UP * 1.1 + RIGHT * 3.2, NEO_WHITE),
        }

        sat_grps, sat_lines = [], VGroup()
        for name, (pos, col) in sats.items():
            sc = Circle(
                radius=0.68,
                color=col,
                stroke_width=1.5,
                fill_color=BG_BLACK,
                fill_opacity=0.95,
            )
            sc.move_to(pos)
            sl = T(name, 14, col, bold=True)
            sl.move_to(sc)
            sg = VGroup(sc, sl)
            sat_grps.append(sg)
            sat_lines.add(
                Line(center.get_center(), sc.get_center(), color=col, stroke_width=1.0)
            )

        kern_grp = VGroup(center, clbl)
        self.play(FadeIn(kern_grp))
        self.play(Create(sat_lines), run_time=0.8)
        self.flash_in(sat_grps)
        self.wait(1.5)
        self.out(b, hdr, defn, kern_grp, sat_lines, *sat_grps)

    # ═══════════════════════════════════════════════════════
    # SLIDE 18 – BATTERY NOT INCLUDED
    # ═══════════════════════════════════════════════════════
    def slide_18_not_included(self):
        b = glow_border(NEO_RED)
        self.play(Create(b), run_time=0.4)

        hdr = T("BATTERY NOT INCLUDED", 40, NEO_RED, bold=True)
        hdr.to_edge(UP, buff=0.5)
        self.play(Write(hdr), run_time=0.6)

        inc = VGroup(
            T("KERNEL INCLUDES:", 24, NEO_GREEN, bold=True),
            T("✓ Filesystem driver", 20, NEO_GREEN),
            T("✓ Process scheduler", 20, NEO_GREEN),
            T("✓ System calls", 20, NEO_GREEN),
            T("✓ Memory pager", 20, NEO_GREEN),
            T("✓ Interrupt handler", 20, NEO_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        exc = VGroup(
            T("NOT IN THE KERNEL:", 24, NEO_RED, bold=True),
            T("❌ Shell / Terminal", 20, NEO_RED),
            T("❌ Text editors (vim, nano…)", 20, NEO_RED),
            T("❌ GUI / Window manager", 20, NEO_RED),
            T("❌ Programming languages & interpreters", 20, NEO_RED),
            T("❌ Web browsers, games, apps…", 20, NEO_RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        panels = VGroup(inc, exc).arrange(RIGHT, buff=1.2)
        panels.next_to(hdr, DOWN, buff=0.5)
        dv = Line(
            panels.get_top() + UP * 0.1,
            panels.get_bottom() + DOWN * 0.1,
            color=NEO_DIM,
            stroke_width=1,
        ).move_to(panels)

        note = T("Linux kernel ≈ 30M lines   |   Plan 9 ≈ 100k lines", 18, NEO_PURPLE)
        note.to_edge(DOWN, buff=0.35)

        self.flash_in(inc)
        self.play(Create(dv))
        self.flash_in(exc)
        self.play(FadeIn(note))
        self.wait(2.0)
        self.out(b, hdr, panels, dv, note)

    # ═══════════════════════════════════════════════════════
    # SLIDE 19 – OOP ASSEMBLY
    # ═══════════════════════════════════════════════════════
    def slide_19_assembly(self):
        b = self.slide_border()
        hdr = T("ASSEMBLING THE OS  (OOP)", 38, NEO_GREEN, bold=True)
        hdr.set_color_by_gradient(NEO_GREEN, NEO_CYAN)
        hdr.to_edge(UP, buff=0.45)
        hl = hline(NEO_GREEN)
        hl.next_to(hdr, DOWN, buff=0.1)
        self.play(FadeIn(hdr), Create(hl))

        classes = [
            ("class BootLoader", NEO_YELLOW),
            ("class FileSystem", NEO_PURPLE),
            ("class Scheduler", NEO_CYAN),
            ("class Pager", NEO_WHITE),
            ("class SysCall", NEO_GREEN),
            ("class Interrupt", NEO_RED),
        ]

        cboxes = VGroup()
        for cname, col in classes:
            bx = neo_box(3.2, 0.62, col)
            lb = T(cname, 17, col, bold=True)
            lb.move_to(bx)
            cboxes.add(VGroup(bx, lb))

        cboxes.arrange_in_grid(2, 3, buff=(0.3, 0.22))
        cboxes.next_to(hl, DOWN, buff=0.42)

        kern_bx = neo_box(11.0, 0.72, NEO_GREEN, fill_op=0.12)
        kern_tx = T(
            "class Kernel(BootLoader, FileSystem, Scheduler, Pager, SysCall, Interrupt)",
            17,
            NEO_GREEN,
            bold=True,
        )
        kern_tx.move_to(kern_bx)
        kern_grp = VGroup(kern_bx, kern_tx)
        kern_grp.to_edge(DOWN, buff=0.35)

        for box in cboxes:
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
                for box in cboxes
            ]
        )
        self.play(Create(arrows_), run_time=0.8)
        self.play(FadeIn(kern_grp))

        # Flash
        for col in [NEO_YELLOW, NEO_GREEN]:
            self.play(kern_grp[0].animate.set_stroke(color=col), run_time=0.1)
        self.wait(2.0)
        self.out(b, hdr, hl, cboxes, arrows_, kern_grp)

    # ═══════════════════════════════════════════════════════
    # SLIDE 20 – END CARD
    # ═══════════════════════════════════════════════════════
    def slide_20_end(self):
        self.rain(0.5, n=45, op=0.4)
        b = self.slide_border()

        big = T("NOW GO BUILD IT.", 58, NEO_GREEN, bold=True)
        big.set_color_by_gradient(NEO_GREEN, NEO_CYAN, NEO_PURPLE)
        big.move_to(UP * 1.5)

        sub = T("Your OS. Your rules. Your ring-0.", 28, NEO_CYAN)
        sub.next_to(big, DOWN, buff=0.45)

        cmd = T("git init my_os && vim kernel/main.c", 26, NEO_GREEN)
        cmd.next_to(sub, DOWN, buff=0.4)

        tip = T("Start: boot sector → print 'Hello' in 16-bit real mode.", 20, NEO_DIM)
        tip.next_to(cmd, DOWN, buff=0.28)

        cur = T("█", 30, NEO_GREEN)
        cur.next_to(cmd, RIGHT, buff=0.06)

        self.play(Write(big), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.15))
        self.play(FadeIn(cmd))
        self.play(FadeIn(cur))
        self.play(Blink(cur, blinks=3))
        self.play(FadeIn(tip))

        rain2 = rain_chars(50, 0.12)
        self.add(rain2)
        self.wait(2.5)
        self.out(b, big, sub, cmd, tip, cur, rain2)
