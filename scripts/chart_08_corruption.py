import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path
import matplotlib.patches as mpatches


def box(ax, xy, w, h, text, fc, tc="white", fs=10.5):
    x, y = xy
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                        linewidth=0, facecolor=fc, zorder=3)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", color=tc, fontsize=fs,
            fontweight="bold", linespacing=1.3, zorder=4)
    return (x + w/2, y), (x + w/2, y + h), (x, y + h/2), (x + w, y + h/2)


def arrow(ax, p1, p2, color=INK, label=None, lw=2.2, style="-|>", rad=0.0, lpos=0.5, fs=9.2, lcolor=None):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=18, color=color,
                         linewidth=lw, zorder=2, connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)
    if label:
        mx = p1[0] + (p2[0] - p1[0]) * lpos
        my = p1[1] + (p2[1] - p1[1]) * lpos
        ax.text(mx, my, label, ha="center", va="center", fontsize=fs, color=lcolor or color,
                fontweight="bold", backgroundcolor="white", zorder=5,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))


fig, ax = plt.subplots(figsize=(12.5, 9.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.axis("off")

# Top level - sources
b_cn = box(ax, (0.4, 9.6), 4.6, 1.5, "China Railway Group + Sinohydro\n(Sicomines shareholders, 68%)", CN_RED)
b_state = box(ax, (7.0, 9.6), 4.6, 1.5, "DRC Central Bank + Gecamines\n(state funds)", DRC_BLUE)

# Middle level - the gateway
b_ccc = box(ax, (1.6, 6.7), 4.0, 1.5, "Congo Construction Co. (CCC)\nshell company,\nintermediary - Du Wei", CN_GOLD, tc=INK, fs=9.6)
b_bgfi = box(ax, (6.8, 6.7), 4.6, 1.5, "BGFIBank DRC\nrun by Kabila's brother,\n40% owned by his sister", WARN, fs=9.8)

# Bottom level - recipients
b_kab = box(ax, (3.0, 3.8), 6.0, 1.5, "Joseph Kabila's network\nfamily, associates -\npolitical cover for the contract", CN_RED_DARK, fs=10)

# Outcome
b_out = box(ax, (2.6, 0.9), 6.8, 1.4, "Outcome: political untouchability\nof the Sicomines contract (2008-2024)", INK)

# Arrows
arrow(ax, (2.7, 9.6), (3.2, 8.2), color=CN_RED, label="transfers\nvia CCC", lpos=0.35)
arrow(ax, (9.3, 9.6), (9.1, 8.2), color=DRC_BLUE, label="\\$94.5m +\n\\$20m", lpos=0.4, fs=8.6)
arrow(ax, (3.6, 6.7), (5.6, 5.3), color=CN_GOLD, lcolor=WARN, label="\\$55-65m", lpos=0.5)
arrow(ax, (9.0, 6.7), (6.8, 5.3), color=WARN, label="\u2265 \\$138m total\nvia BGFIBank", lpos=0.55, fs=8.6)
arrow(ax, (6.0, 3.8), (6.0, 2.3), color=CN_RED_DARK, lw=2.6)

ax.set_ylim(0, 13.2)
ax.text(6, 12.75, "Congo Hold-up: how an offshore bank protected the deal of the century",
        ha="center", fontsize=16.5, fontweight="bold", color=INK)
ax.text(6, 12.2, "Reconstructed from the leak of 3.5 million BGFIBank documents (PPLAAF, Mediapart, The Sentry, EIC, 19 media outlets + 5 NGOs, 2021)",
        ha="center", fontsize=9.7, color=NEUTRAL)

source_footer(fig, "Sources: The Sentry ('The Backchannel', 2021), PPLAAF, Mediapart, Al Jazeera, L'Orient Today - amounts for individual branches of the scheme vary across reports ($55-65m for CCC); full list in SOURCES.md.", y=0.01)
save(fig, "08_corruption_money_flow")
