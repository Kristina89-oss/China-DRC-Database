"""
Общий стиль для всех графиков репозитория.
Палитра: красный/золото — активы, связанные с КНР; синий/жёлтый — ДРК/прочее.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- Палитра ---
CN_RED = "#C0392B"        # доля/активы КНР
CN_RED_DARK = "#8E2A20"
CN_GOLD = "#D4A017"       # акцент КНР (вторичный)
DRC_BLUE = "#1B4F72"      # доля ДРК / государство
DRC_YELLOW = "#F1C40F"    # ДРК акцент
NEUTRAL = "#7F8C8D"       # прочее / нейтральное
INK = "#232B33"           # текст/оси
GRID = "#E3E6E8"
BG = "#FFFFFF"
GOOD = "#1E8449"          # рост/позитив (для ДРК)
WARN = "#B9770E"

FONT = "DejaVu Sans"

plt.rcParams.update({
    "font.family": FONT,
    "font.size": 12,
    "text.color": INK,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.facecolor": BG,
    "figure.facecolor": BG,
    "savefig.facecolor": BG,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.8,
    "axes.axisbelow": True,
})


def clean_ax(ax, grid_axis="y"):
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    ax.grid(axis=grid_axis, alpha=0.6)
    ax.tick_params(length=0)


def save(fig, name, tight=True):
    path = f"/home/claude/repo_en/charts/{name}.png"
    if tight:
        fig.savefig(path, dpi=200, bbox_inches="tight", facecolor=BG)
    else:
        fig.savefig(path, dpi=200, facecolor=BG)
    plt.close(fig)
    print(f"saved {path}")


def source_footer(fig, text, y=-0.02):
    fig.text(0.01, y, text, fontsize=8.5, color=NEUTRAL, ha="left", va="top")
