import sys
import numpy as np
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt

projects = ["Tenke\nFungurume", "Kisanfu\n(phase 1)", "Deziwa", "Kambove", "Pumpi"]
copper = [280.3, 100, 80, 35, 40]     # kt
cobalt = [21.6, 30, 22, 0, 5]         # kt (Kambove - not published)

x = np.arange(len(projects))
w = 0.36

fig, ax = plt.subplots(figsize=(12, 7))
b1 = ax.bar(x - w/2, copper, width=w, color=DRC_BLUE, label="Copper, kt/yr", zorder=3)
b2 = ax.bar(x + w/2, cobalt, width=w, color=CN_GOLD, label="Cobalt, kt/yr", zorder=3)

for bars in (b1, b2):
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, h + 4, f"{h:g}", ha="center", fontsize=10.5, fontweight="bold", color=INK)
        else:
            ax.text(bar.get_x() + bar.get_width()/2, 4, "n/a", ha="center", fontsize=9, color=NEUTRAL, style="italic")

clean_ax(ax)
ax.set_xticks(x)
ax.set_xticklabels(projects, fontsize=11.5)
ax.set_ylabel("thousand tonnes per year", fontsize=11)
ax.set_ylim(0, 310)
ax.legend(loc="upper right", frameon=False, fontsize=11)
ax.set_title("Output at China's DRC mines (2022-2023 snapshot)", fontsize=15.5, fontweight="bold", pad=16)

ax.text(0.5, -0.22,
        "TFM + KFM (CMOC) alone had grown to a combined 741.1kt of copper and 117.5kt of cobalt per year by 2025",
        transform=ax.transAxes, ha="center", fontsize=10, color=CN_RED_DARK, fontweight="bold")

source_footer(fig, "Sources: CMOC/CNMC/Wanbao Mining corporate reporting, Cobalt Institute, CSIS - Kambove: cobalt figures were not published separately.", y=-0.30)
save(fig, "05_production_by_project")
