import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt

labels = ["CMOC\n(China)", "Glencore", "Other producers\n(ERG, Huayou, etc.)", "Strategic\nreserve (ARECOMS)"]
values = [31200, 22800, 33000, 9600]
colors = [CN_RED, DRC_BLUE, NEUTRAL, CN_GOLD]

fig, ax = plt.subplots(figsize=(10.5, 8.2))
wedges, _ = ax.pie(values, colors=colors, startangle=-90, counterclock=False,
                    wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2))

for w, val, lab in zip(wedges, values, labels):
    ang = (w.theta2 + w.theta1) / 2
    import numpy as np
    x = np.cos(np.radians(ang))
    y = np.sin(np.radians(ang))
    ax.annotate(f"{lab}\n{val:,} t", xy=(x*0.79, y*0.79), xytext=(x*1.32, y*1.18),
                ha="center", fontsize=10.8, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="-", color=NEUTRAL, lw=1))

ax.text(0, 0.06, "96,600", ha="center", va="center", fontsize=27, fontweight="bold", color=INK)
ax.text(0, -0.10, "tonnes/year", ha="center", va="center", fontsize=13, color=NEUTRAL)
ax.text(0, -0.22, "2026-2027", ha="center", va="center", fontsize=11, color=NEUTRAL)

ax.set_title("How the DRC quotas cobalt exports", fontsize=16, fontweight="bold", pad=52, y=1.0)

fig.subplots_adjust(top=0.80, bottom=0.08)

source_footer(fig, "Sources: ARECOMS (Decision No. 004/2025), IEA Policy Database, GreenStocksResearch/IEA Global Critical Minerals Outlook 2026, Reuters - 2026 company quotas; the 87,000t base quota is allocated pro rata to historical exports.", y=-0.03)
save(fig, "07_cobalt_quota_breakdown")
