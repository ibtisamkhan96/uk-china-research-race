"""UK vs China university research race - a LinkedIn carousel.

Generates ten 1080x1350 portrait slides (PNG) plus a combined PDF for
LinkedIn document posts. Compares the two countries' university research
contributions across modern deep-tech domains.

Figures and claims are compiled from public reporting (ASPI Critical
Technology Tracker, Nature Index, Nobel records, university public
records) and are illustrative of research strengths, not a precise
league table.
"""
import textwrap

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch

# ------------------------------------------------------------- theme
BG = "#0C1322"
PANEL_UK = "#11203A"
PANEL_CN = "#2A1620"
EDGE = "#27344F"
UKBLUE = "#5B9BFF"
CNRED = "#FF5252"
GOLD = "#E8B84B"
TEXT = "#ECF1FB"
MUTED = "#90A0BC"

plt.rcParams.update({"font.family": "Arial", "text.color": TEXT})

W, H, DPI = 10.8, 13.5, 100  # 1080 x 1350 portrait


def new_slide():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")
    # top accent bar split UK | China
    ax.add_patch(plt.Rectangle((0, 0.985), 0.5, 0.015, facecolor=UKBLUE))
    ax.add_patch(plt.Rectangle((0.5, 0.985), 0.5, 0.015, facecolor=CNRED))
    return fig, ax


def rbox(ax, x, y, w, h, fc, ec=EDGE):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle="round,pad=0.006,rounding_size=0.018",
                 facecolor=fc, edgecolor=ec, linewidth=1.0))


def wrap(s, n):
    return "\n".join(textwrap.wrap(s, n))


def footer(ax, n):
    ax.text(0.06, 0.035, "Ibtisam Ahmed Khan", fontsize=12, color=MUTED,
            fontweight="bold")
    ax.text(0.06, 0.018, "MSc, Tsinghua University", fontsize=10, color=MUTED)
    ax.text(0.94, 0.027, f"{n} / 10", fontsize=12, color=GOLD, ha="right",
            fontweight="bold", family="Consolas")


# ------------------------------------------------------------- content
DOMAINS = [
    {
        "n": 3, "kick": "ARTIFICIAL INTELLIGENCE", "icon": "AI",
        "uk_inst": "DeepMind (London) · UCL · Cambridge · Oxford · Alan Turing Institute",
        "uk": [
            "AlphaFold cracked protein folding - a 50-year grand challenge",
            "Hassabis & Jumper won the 2024 Nobel Prize in Chemistry",
            "A hub for foundational, science-first AI",
        ],
        "uk_hero": "Where landmark AI systems are invented",
        "cn_inst": "Tsinghua · Peking · Zhejiang · Chinese Academy of Sciences",
        "cn": [
            "Among the world's top universities by AI publication volume",
            "Global leaders in computer vision, LLMs and AI patents",
            "Vast talent pipeline and fast real-world deployment",
        ],
        "cn_hero": "Where AI is published and deployed at scale",
        "verdict": "The UK invents the landmark systems; China dominates volume and deployment.",
    },
    {
        "n": 4, "kick": "EVs & BATTERIES", "icon": "EV",
        "uk_inst": "Oxford · Imperial · The Faraday Institution",
        "uk": [
            "The Li-ion cathode was born at Oxford - Goodenough's",
            "lithium cobalt oxide, 1980 (Nobel Chemistry 2019)",
            "National battery science via the Faraday Institution",
        ],
        "uk_hero": "Seeded the chemistry of modern batteries",
        "cn_inst": "Tsinghua · USTC · CAS  →  CATL · BYD",
        "cn": [
            "CATL and BYD supply roughly half the world's EV batteries",
            "Leads global battery-chemistry research and patents",
            "The planet's fastest lab-to-gigafactory pipeline",
        ],
        "cn_hero": "Scaled batteries to the entire world",
        "verdict": "The UK seeded the chemistry; China scaled it into a global industry.",
    },
    {
        "n": 5, "kick": "AUTONOMOUS VEHICLES", "icon": "AV",
        "uk_inst": "Oxford Robotics Institute → Oxa · Wayve (London)",
        "uk": [
            "Wayve pioneers end-to-end, learning-based driving",
            "Oxa (ex-Oxbotica) spun out of Oxford's robotics labs",
            "Strength in novel AI approaches and safety",
        ],
        "uk_hero": "Leads on new ways to teach cars to drive",
        "cn_inst": "Tsinghua · Baidu Apollo ecosystem",
        "cn": [
            "Tsinghua autonomous-driving labs feed a huge industry",
            "Among the world's largest robotaxi fleets and test mileage",
            "City-scale real-world deployment",
        ],
        "cn_hero": "Leads on scale of real-world testing",
        "verdict": "The UK leads on learning methods; China leads on sheer scale of road testing.",
    },
    {
        "n": 6, "kick": "NANOTECH & MATERIALS", "icon": "NM",
        "uk_inst": "University of Manchester · National Graphene Institute",
        "uk": [
            "Graphene was isolated at Manchester in 2004",
            "Geim & Novoselov won the 2010 Nobel Prize in Physics",
            "A founding moment for 2D materials",
        ],
        "uk_hero": "Made the discovery that defined a field",
        "cn_inst": "Tsinghua · CAS · Zhejiang",
        "cn": [
            "World's largest output of nanotechnology research",
            "Dominates graphene patents and commercialisation",
            "Top global ranks for materials science (Nature Index)",
        ],
        "cn_hero": "Owns the patent and production landscape",
        "verdict": "The UK made the discovery; China owns the patents and production.",
    },
    {
        "n": 7, "kick": "ENERGY MATERIALS & SOLAR", "icon": "PV",
        "uk_inst": "Oxford (Henry Snaith) · Oxford PV",
        "uk": [
            "Perovskite solar breakthroughs pioneered at Oxford",
            "Oxford PV pushes world-record tandem-cell efficiency",
            "Frontier of next-generation photovoltaics",
        ],
        "uk_hero": "Pushes the efficiency frontier",
        "cn_inst": "CAS · Tsinghua · USTC",
        "cn": [
            "Controls over 80% of global solar PV manufacturing",
            "Leads perovskite scale-up from lab to production line",
            "Manufactures the bulk of the energy transition",
        ],
        "cn_hero": "Manufactures the energy transition",
        "verdict": "The UK pushes efficiency records; China manufactures the energy transition.",
    },
    {
        "n": 8, "kick": "SUPPLY CHAIN & LOGISTICS", "icon": "SC",
        "uk_inst": "Cambridge (Inst. for Manufacturing) · Cranfield",
        "uk": [
            "World-leading supply-chain and resilience research",
            "Cranfield: logistics, freight and operations expertise",
            "Strength in theory, modelling and risk",
        ],
        "uk_hero": "Leads the science of supply chains",
        "cn_inst": "Tsinghua · Cainiao / JD research labs",
        "cn": [
            "Smart logistics operated at national scale",
            "World's largest automated warehouses and delivery networks",
            "A live testbed for AI-driven logistics",
        ],
        "cn_hero": "Runs the world's largest logistics experiment",
        "verdict": "The UK leads the theory; China runs the largest live experiment.",
    },
]


# ------------------------------------------------------------- slide drawers
def domain_slide(d):
    fig, ax = new_slide()
    ax.text(0.06, 0.945, f"{d['n']:02d}", fontsize=20, color=GOLD,
            fontweight="bold", family="Consolas")
    ax.text(0.135, 0.945, d["kick"], fontsize=21, color=TEXT,
            fontweight="bold", va="center")
    ax.plot([0.06, 0.94], [0.915, 0.915], color=EDGE, lw=1.2)

    # two panels
    rbox(ax, 0.05, 0.235, 0.43, 0.65, PANEL_UK)
    rbox(ax, 0.52, 0.235, 0.43, 0.65, PANEL_CN)
    ax.text(0.265, 0.855, "UK", fontsize=26, color=UKBLUE, ha="center",
            fontweight="bold")
    ax.text(0.735, 0.855, "CHINA", fontsize=26, color=CNRED, ha="center",
            fontweight="bold")

    for cx, inst, bullets, hero, accent, panel in [
        (0.265, d["uk_inst"], d["uk"], d["uk_hero"], UKBLUE, (0.07, 0.41)),
        (0.735, d["cn_inst"], d["cn"], d["cn_hero"], CNRED, (0.54, 0.41)),
    ]:
        ax.text(cx, 0.815, wrap(inst, 34), fontsize=10.5, color=MUTED,
                ha="center", va="top", linespacing=1.4, style="italic")
        y = 0.745
        for b in bullets:
            ax.text(panel[0], y, "•", fontsize=13, color=accent, va="top")
            ax.text(panel[0] + 0.02, y, wrap(b, 33), fontsize=12.5,
                    color=TEXT, va="top", linespacing=1.4)
            y -= 0.082
        # hero box
        rbox(ax, panel[0] - 0.005, 0.255, 0.40, 0.075,
             "#16294a" if accent == UKBLUE else "#341a24", ec=accent)
        ax.text(cx, 0.293, wrap(hero, 30), fontsize=12.5, color=accent,
                ha="center", va="center", fontweight="bold", linespacing=1.3)

    # verdict
    rbox(ax, 0.05, 0.10, 0.90, 0.105, "#15203a", ec=GOLD)
    ax.text(0.08, 0.178, "THE VERDICT", fontsize=12, color=GOLD,
            fontweight="bold", family="Consolas")
    ax.text(0.08, 0.135, wrap(d["verdict"], 70), fontsize=14.5, color=TEXT,
            va="center", linespacing=1.35)
    footer(ax, d["n"])
    return fig


def cover_slide():
    fig, ax = new_slide()
    ax.text(0.06, 0.86, "THE RESEARCH RACE", fontsize=22, color=GOLD,
            fontweight="bold", family="Consolas")
    ax.text(0.06, 0.745, "UK", fontsize=82, color=UKBLUE, fontweight="bold")
    ax.text(0.40, 0.762, "vs", fontsize=42, color=MUTED, style="italic")
    ax.text(0.06, 0.625, "CHINA", fontsize=82, color=CNRED, fontweight="bold")
    ax.text(0.06, 0.545, "Whose universities are building the future\nin the lab?",
            fontsize=24, color=TEXT, va="top", linespacing=1.35)
    ax.text(0.06, 0.40, "AI   ·   EVs & batteries   ·   autonomous vehicles\n"
            "nanotech   ·   energy materials   ·   supply chain",
            fontsize=16, color=MUTED, va="top", linespacing=1.9)
    ax.text(0.06, 0.235, "Swipe to see who leads each\ndeep-tech frontier  →",
            fontsize=18, color=GOLD, va="top", linespacing=1.4,
            fontweight="bold")
    ax.text(0.06, 0.07, "A data story by Ibtisam Ahmed Khan  ·  MSc, Tsinghua University",
            fontsize=13, color=MUTED)
    return fig


def bigpicture_slide():
    fig, ax = new_slide()
    ax.text(0.06, 0.945, "02", fontsize=20, color=GOLD, fontweight="bold",
            family="Consolas")
    ax.text(0.135, 0.945, "TWO SUPERPOWERS OF SCIENCE", fontsize=21,
            color=TEXT, fontweight="bold", va="center")
    ax.plot([0.06, 0.94], [0.915, 0.915], color=EDGE, lw=1.2)

    rbox(ax, 0.05, 0.50, 0.90, 0.37, PANEL_UK)
    ax.text(0.09, 0.825, "THE UK", fontsize=22, color=UKBLUE,
            fontweight="bold")
    ax.text(0.09, 0.785, "Foundational breakthroughs, Nobel-grade discoveries,\n"
            "and outsized impact for its size.", fontsize=15.5, color=TEXT,
            va="top", linespacing=1.4)
    ax.text(0.09, 0.665, "Oxford · Cambridge · Imperial · Manchester · UCL",
            fontsize=14, color=MUTED, style="italic")
    ax.text(0.09, 0.60, "Graphene, the Li-ion cathode, perovskite solar and\n"
            "AlphaFold were all seeded in UK labs.", fontsize=15.5,
            color=TEXT, va="top", linespacing=1.4)

    rbox(ax, 0.05, 0.105, 0.90, 0.37, PANEL_CN)
    ax.text(0.09, 0.43, "CHINA", fontsize=22, color=CNRED, fontweight="bold")
    ax.text(0.09, 0.39, "Unmatched scale of output and the fastest pipeline\n"
            "from research paper to global product.", fontsize=15.5,
            color=TEXT, va="top", linespacing=1.4)
    ax.text(0.09, 0.27, "Tsinghua · Peking · Zhejiang · SJTU · USTC · CAS",
            fontsize=14, color=MUTED, style="italic")
    ax.text(0.09, 0.205, "Now leads the world in high-impact research across\n"
            "most critical technologies (ASPI tracker).", fontsize=15.5,
            color=TEXT, va="top", linespacing=1.4)
    footer(ax, 2)
    return fig


def verdict_slide():
    fig, ax = new_slide()
    ax.text(0.06, 0.945, "09", fontsize=20, color=GOLD, fontweight="bold",
            family="Consolas")
    ax.text(0.135, 0.945, "BREAKTHROUGHS vs SCALE", fontsize=21, color=TEXT,
            fontweight="bold", va="center")
    ax.plot([0.06, 0.94], [0.915, 0.915], color=EDGE, lw=1.2)

    ax.text(0.06, 0.85, "The pattern repeats across every frontier:",
            fontsize=17, color=MUTED, va="top")

    pairs = [
        (UKBLUE, "The UK invents.",
         "Graphene, Li-ion cathodes, perovskite solar and AlphaFold "
         "were first imagined in British labs. Quality, firsts and "
         "Nobel-grade discovery."),
        (CNRED, "China industrialises.",
         "Backed by unmatched publication and patent volume, China turns "
         "research into global industry faster than anyone - from "
         "batteries to solar to logistics."),
    ]
    y = 0.76
    for accent, head, body in pairs:
        rbox(ax, 0.05, y - 0.215, 0.90, 0.205,
             PANEL_UK if accent == UKBLUE else PANEL_CN, ec=accent)
        ax.text(0.09, y - 0.04, head, fontsize=23, color=accent,
                fontweight="bold")
        ax.text(0.09, y - 0.085, wrap(body, 62), fontsize=15.5, color=TEXT,
                va="top", linespacing=1.45)
        y -= 0.27

    rbox(ax, 0.05, 0.10, 0.90, 0.10, "#15203a", ec=GOLD)
    ax.text(0.5, 0.15, "The UK still invents disproportionately.\n"
            "China increasingly owns the path from paper to product.",
            fontsize=15.5, color=GOLD, ha="center", va="center",
            fontweight="bold", linespacing=1.4)
    footer(ax, 9)
    return fig


def cta_slide():
    fig, ax = new_slide()
    ax.text(0.06, 0.86, "YOUR TURN", fontsize=22, color=GOLD,
            fontweight="bold", family="Consolas")
    ax.text(0.06, 0.76, "Which model wins\nthe next decade?", fontsize=40,
            color=TEXT, va="top", fontweight="bold", linespacing=1.2)
    ax.text(0.06, 0.55, "Foundational breakthroughs, or the scale to turn\n"
            "every breakthrough into an industry?", fontsize=18, color=MUTED,
            va="top", linespacing=1.5)
    ax.text(0.06, 0.43, "Tell me what you think in the comments.",
            fontsize=18, color=UKBLUE, va="top", fontweight="bold")

    rbox(ax, 0.05, 0.165, 0.90, 0.16, "#11182a")
    ax.text(0.09, 0.285, "SOURCES & HONEST CAVEAT", fontsize=12, color=GOLD,
            fontweight="bold", family="Consolas")
    ax.text(0.09, 0.245, wrap("Compiled from public reporting: ASPI Critical "
            "Technology Tracker, Nature Index, Nobel records and university "
            "public information. Figures illustrate research strengths, not a "
            "precise league table.", 74), fontsize=12.5, color=MUTED,
            va="top", linespacing=1.45)
    ax.text(0.06, 0.075, "Ibtisam Ahmed Khan  ·  MSc, Tsinghua University  ·  "
            "data + code on GitHub", fontsize=13, color=TEXT, fontweight="bold")
    return fig


# ------------------------------------------------------------- assemble
slides = [cover_slide(), bigpicture_slide()]
slides += [domain_slide(d) for d in DOMAINS]
slides += [verdict_slide(), cta_slide()]

for i, fig in enumerate(slides, 1):
    fig.savefig(f"slides/slide_{i:02d}.png", dpi=DPI, facecolor=BG)

with PdfPages("carousel/uk_china_research_race.pdf") as pdf:
    for fig in slides:
        pdf.savefig(fig, facecolor=BG)
for fig in slides:
    plt.close(fig)

print(f"Wrote {len(slides)} slides + PDF")
