import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt

plants = [
    ("Nzilo I\n(1953, legacy)", 100, "Existing, non-Chinese", NEUTRAL, "operating"),
    ("Zongo II", 150, "Sinohydro \u00b7 $360m", CN_RED, "operating since 2018"),
    ("Busanga", 240, "Sicomines consortium \u00b7 $660m", CN_RED, "operating since 2023"),
    ("Nzilo II /\n\"Heshima\"", 200, "CMOC + Lualaba Power \u00b7 >$470m", CN_GOLD, "under construction, target 2028-29"),
]

fig, ax = plt.subplots(figsize=(11, 7))
labels = [p[0] for p in plants]
vals = [p[1] for p in plants]
colors = [p[3] for p in plants]

bars = ax.bar(labels, vals, color=colors, width=0.55, zorder=3)
for bar, (name, mw, detail, c, status) in zip(bars, plants):
    ax.text(bar.get_x() + bar.get_width()/2, mw + 8, f"{mw} MW", ha="center", fontsize=13, fontweight="bold", color=INK)
    ax.text(bar.get_x() + bar.get_width()/2, mw + 26, f"({status})", ha="center", fontsize=8.8, color=NEUTRAL, style="italic")
    ax.text(bar.get_x() + bar.get_width()/2, mw / 2, detail, ha="center", va="center", fontsize=8.3,
            color="white", rotation=90 if mw > 60 else 0, linespacing=1.3)

clean_ax(ax)
ax.set_ylim(0, 300)
ax.set_ylabel("Installed capacity, MW", fontsize=11)
ax.set_title("The Lualaba River hydropower cascade: power almost entirely for the mines", fontsize=15, fontweight="bold", pad=16)

total_cn = 150 + 240 + 200
ax.text(0.99, 0.95, f"590 MW of Chinese financing\nout of {sum(vals)} MW in the cascade",
        transform=ax.transAxes, ha="right", va="top", fontsize=11, color=CN_RED_DARK, fontweight="bold")

source_footer(fig, "Sources: AidData (China Eximbank), Wikipedia (Zongo II), Herbert Smith Freehills / CMOC press releases, Bankable Africa - Busanga: up to 170 MW is directly reserved for Sicomines.", y=-0.10)
save(fig, "06_hydropower_cascade")
