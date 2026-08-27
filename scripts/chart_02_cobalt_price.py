import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# (year-fraction, price $/t, label)
points = [
    (2022.25, 82000, "Apr 2022\n$82,000\n(peak, $80-88k across indices)"),
    (2023.9, 34000, "late 2023\n~$34,000\n(CMOC surplus)"),
    (2024.58, 24900, "Aug 2024\n$24,900\n(7-year low)"),
    (2025.05, 21550, "early 2025\n$21,550\n(market bottom)"),
    (2025.96, 52900, "Dec 2025\n~$52,900\n(post-ban)"),
    (2026.5, 57320, "Jul 2026\n$57,320\n(+160% off the bottom)"),
]

fig, ax = plt.subplots(figsize=(13, 7.2))

xs = [p[0] for p in points]
ys = [p[1] for p in points]

# policy zones
ax.axvspan(2025.13, 2025.79, color=DRC_BLUE, alpha=0.08, zorder=0)
ax.text(2025.46, 104000, "Export ban\n(ARECOMS)", ha="center", fontsize=9, color=DRC_BLUE, fontweight="bold")
ax.axvspan(2025.79, 2026.6, color=GOOD, alpha=0.08, zorder=0)
ax.text(2026.2, 104000, "Quota regime\n96,600 t/yr", ha="center", fontsize=9, color=GOOD, fontweight="bold")

ax.plot(xs, ys, color=CN_RED, linewidth=2.6, marker="o", markersize=9,
        markerfacecolor=CN_RED, markeredgecolor="white", markeredgewidth=1.5, zorder=5)

for x, y, label in points:
    offset = 7500
    ax.annotate(label, (x, y), xytext=(x, y + offset), fontsize=8.7, ha="center", va="bottom",
                color=INK, linespacing=1.35)

clean_ax(ax)
ax.set_ylim(0, 118000)
ax.set_xlim(2021.9, 2026.85)
ax.set_ylabel("US$ per tonne of metal (approximate)", fontsize=11)
ax.set_xticks([2022, 2023, 2024, 2025, 2026])
ax.yaxis.set_major_formatter(lambda v, pos: f"{int(v/1000)}k")
ax.set_yticks([0, 20000, 40000, 60000, 80000, 100000])

ax.set_title("The cobalt seesaw: how the DRC turned the market against China's dumping",
             fontsize=15.5, fontweight="bold", pad=16)

source_footer(fig, "Sources: Cobalt Institute, Fastmarkets, S&P Global, IEA/ARECOMS, Reuters, MiningWeekly, Evidencity - an approximate trend across different price indices, not a single continuous series.")
save(fig, "02_cobalt_price_trend")
