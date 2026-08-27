import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(13.5, 8.5))
ax.set_xlim(0, 13); ax.set_ylim(0, 10); ax.axis("off")

ax.text(6.5, 9.55, "The closed loop: copper leaves as raw material, comes back as product", ha="center",
        fontsize=16.5, fontweight="bold", color=INK)
ax.text(6.5, 9.05, "A snapshot of May 2026 - one month of DRC-China bilateral trade",
        ha="center", fontsize=10.3, color=NEUTRAL)

# DRC box
drc = FancyBboxPatch((0.5, 5.3), 3.6, 2.3, boxstyle="round,pad=0.02,rounding_size=0.1",
                      linewidth=0, facecolor=DRC_BLUE, zorder=3)
ax.add_patch(drc)
ax.text(2.3, 6.45, "DRC", ha="center", va="center", color="white", fontsize=15, fontweight="bold", zorder=4)

# China box
cn = FancyBboxPatch((8.9, 5.3), 3.6, 2.3, boxstyle="round,pad=0.02,rounding_size=0.1",
                     linewidth=0, facecolor=CN_RED, zorder=3)
ax.add_patch(cn)
ax.text(10.7, 6.45, "China", ha="center", va="center", color="white", fontsize=15, fontweight="bold", zorder=4)

# Arrow DRC -> China (raw material)
ax.add_patch(FancyArrowPatch((4.1, 7.1), (8.85, 7.1), arrowstyle="-|>", mutation_scale=22,
                              color=DRC_BLUE, lw=3, zorder=2))
ax.text(6.5, 7.55, "raw and semi-processed material", ha="center", fontsize=10.5, fontweight="bold", color=DRC_BLUE)
ax.text(6.5, 7.05, "$2.28bn / month", ha="center", fontsize=13, fontweight="bold", color=INK)

# Arrow China -> DRC (finished goods)
ax.add_patch(FancyArrowPatch((8.85, 5.5), (4.1, 5.5), arrowstyle="-|>", mutation_scale=22,
                              color=CN_RED, lw=3, zorder=2))
ax.text(6.5, 5.9, "finished goods", ha="center", fontsize=10.5, fontweight="bold", color=CN_RED)
ax.text(6.5, 5.35, "$663m / month", ha="center", fontsize=13, fontweight="bold", color=INK)

# Details left (what leaves)
ax.text(2.3, 4.55, "WHAT LEAVES THE DRC", ha="center", fontsize=10.5, fontweight="bold", color=DRC_BLUE)
items_out = ["Refined copper - $1.73bn", "Unwrought copper - $196m", "Copper ore - $128m"]
for i, t in enumerate(items_out):
    ax.text(2.3, 4.15 - i*0.42, t, ha="center", fontsize=10, color=INK)

# Details right (what comes in)
ax.text(10.7, 4.55, "WHAT ENTERS THE DRC", ha="center", fontsize=10.5, fontweight="bold", color=CN_RED)
items_in = ["Batteries - $57.3m  (+507% YoY)", "Transformers - $41.6m  (+873% YoY)", "Insulated wire - $34m  (+276% YoY)"]
for i, t in enumerate(items_in):
    ax.text(10.7, 4.15 - i*0.42, t, ha="center", fontsize=9.6, color=INK)

# Bottom line
box = FancyBboxPatch((1.2, 0.6), 10.6, 1.9, boxstyle="round,pad=0.02,rounding_size=0.1",
                      linewidth=2, edgecolor=WARN, facecolor="#FDF6E8", zorder=3)
ax.add_patch(box)
ax.text(6.5, 1.9, "The DRC runs a trade surplus ($1.62bn/month) - which is exactly why it doesn't see the problem",
        ha="center", fontsize=11, fontweight="bold", color=INK)
ax.text(6.5, 1.25, "The surplus is built on low-value-added raw material. The batteries and transformers it imports\n"
                   "are made from that same Congolese metal - just with someone else's value added.",
        ha="center", fontsize=9.7, color=INK, linespacing=1.5)

source_footer(fig, "Source: OEC (oec.world), Chinese General Administration of Customs data for May 2026; annual context - China-Global South Project.", y=0.02)
save(fig, "13_trade_closed_loop")
