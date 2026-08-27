import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
import numpy as np

stages = ["Extraction\n(upstream)", "Refining\n(midstream)", "Cathodes & cells\n(downstream)"]
drc = [74, 4, 0]
cn = [75, 78, 85]

x = np.arange(len(stages))
w = 0.36

fig, ax = plt.subplots(figsize=(12, 7.2))
b1 = ax.bar(x - w/2, drc, width=w, color=DRC_BLUE, label="DRC", zorder=3)
b2 = ax.bar(x + w/2, cn, width=w, color=CN_RED, label="China", zorder=3)

for bars in (b1, b2):
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, h + 2, f"~{int(h)}%", ha="center",
                    fontsize=12, fontweight="bold", color=INK)
        else:
            ax.text(bar.get_x() + bar.get_width()/2, 2, "\u22480", ha="center", fontsize=10,
                    color=NEUTRAL, style="italic")

clean_ax(ax)
ax.set_xticks(x)
ax.set_xticklabels(stages, fontsize=12)
ax.set_ylim(0, 100)
ax.set_ylabel("share of world volume, %", fontsize=11)
ax.legend(loc="upper left", frameon=False, fontsize=12)
ax.set_title("The real chokepoint isn't the mines - it's the refineries", fontsize=16, fontweight="bold", pad=16)

ax.annotate("this is where\nDRC loses it all", xy=(1 - w/2, 4), xytext=(0.62, 33),
            fontsize=10.5, color=DRC_BLUE, fontweight="bold", ha="center",
            arrowprops=dict(arrowstyle="->", color=DRC_BLUE, lw=1.6))

ax.text(0.5, -0.20, "The DRC supplies ~74% of world cobalt output but refines under 5% of it domestically.\nThe June 2026 concentrate export ban is Kinshasa's first attempt to attack the midstream.",
        transform=ax.transAxes, ha="center", fontsize=10.5, color=INK, linespacing=1.5)

source_footer(fig, "Sources: IEA Global Critical Minerals Outlook 2026, Cobalt Institute/Statista, AidData; estimates of China's share of cobalt refining vary (70-80%) - the average is used.", y=-0.28)
save(fig, "10_value_chain_chokepoint")
