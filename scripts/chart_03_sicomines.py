import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt

labels = ["Infrastructure\nbuilt\n(by 2023)", "China profit\nextracted\n(by 2023)", "New commitment\n2024-2040\n(if Cu > $8,000/t)"]
values = [822, 10000, 7000]
colors = [DRC_BLUE, CN_RED, CN_GOLD]
hatches = [None, None, "//"]

fig, ax = plt.subplots(figsize=(10.5, 7.5))
bars = ax.bar(labels, values, color=colors, width=0.56, zorder=3)
for bar, h in zip(bars, hatches):
    if h:
        bar.set_hatch(h)
        bar.set_edgecolor("white")
        bar.set_linewidth(1)

for bar, v in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 180, f"${v:,}m".replace(",", ","),
            ha="center", fontsize=13.5, fontweight="bold", color=INK)

clean_ax(ax)
ax.set_ylim(0, 11200)
ax.set_yticks([0, 2000, 4000, 6000, 8000, 10000])
ax.yaxis.set_major_formatter(lambda v, pos: f"${v/1000:g}bn" if v >= 1000 else f"${int(v)}m")
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=11.5)

ax.set_title("Sicomines: \\$1 of infrastructure for every ~\\$12 of profit extracted",
             fontsize=15, fontweight="bold", pad=16)

# ratio annotation arrow
ax.annotate("", xy=(0, 9600), xytext=(1, 9600),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1.4))
ax.text(0.5, 9800, "\u2248 12x", ha="center", fontsize=13, fontweight="bold", color=INK)

source_footer(fig, "Sources: EITI (2024), DRC IGF audit (2023), Reuters/Mining.com, Bloomberg (May 2024) - original 2008 agreement: $6-9bn ($3bn mining + $3-6bn infrastructure).")
save(fig, "03_sicomines_investment_vs_profit")
