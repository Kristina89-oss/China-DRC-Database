import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def box(ax, xy, w, h, text, fc, tc="white", fs=10.5):
    x, y = xy
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                        linewidth=0, facecolor=fc, zorder=3)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", color=tc, fontsize=fs,
            fontweight="bold", linespacing=1.3, zorder=4)


def arrow(ax, p1, p2, color=INK, label=None, lw=2.2, lpos=0.5, fs=8.8, lcolor=None, rad=0.0):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=16, color=color,
                         linewidth=lw, zorder=2, connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)
    if label:
        mx = p1[0] + (p2[0] - p1[0]) * lpos
        my = p1[1] + (p2[1] - p1[1]) * lpos
        ax.text(mx, my, label, ha="center", va="center", fontsize=fs, color=lcolor or color,
                fontweight="bold", zorder=5, bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))


fig, ax = plt.subplots(figsize=(13, 9.8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 12.6)
ax.axis("off")

ax.text(6.5, 12.2, "Beijing's 'dual diplomacy' and the private-security market in the DRC",
        ha="center", fontsize=16.5, fontweight="bold", color=INK)
ax.text(6.5, 11.65, "Arms to both sides of the conflict - and a parallel market of foreign PMCs around minerals",
        ha="center", fontsize=9.8, color=NEUTRAL)

# Center - China
box(ax, (5.0, 9.2), 3.0, 1.3, "China\n(state defense industry)", INK, fs=11.5)

# Left branch - DRC
box(ax, (0.6, 6.6), 4.6, 1.5, "CASC / CATIC\nCH-4 (9 units), Wing Loong 2 (talks),\nJF-17 / J-10 (talks)", CN_RED, fs=9.3)
box(ax, (0.6, 4.0), 4.6, 1.3, "DRC / FARDC\nfighting M23", DRC_BLUE, fs=11)

# Right branch - Rwanda
box(ax, (7.8, 6.6), 4.6, 1.5, "Norinco\nSky Dragon 50 / TL-50 - since 2014,\nfirst foreign buyer", CN_RED, fs=9.3)
box(ax, (7.8, 4.0), 4.6, 1.3, "Rwanda / RDF\nbacks M23", WARN, fs=11)

arrow(ax, (5.8, 9.2), (3.2, 8.1), color=CN_RED, label="supplies")
arrow(ax, (7.7, 9.2), (10.0, 8.1), color=CN_RED, label="supplies")
arrow(ax, (2.9, 6.6), (2.9, 5.3), color=DRC_BLUE, lw=2.4)
arrow(ax, (10.1, 6.6), (10.1, 5.3), color=WARN, lw=2.4)

arrow(ax, (2.9, 4.0), (10.1, 4.0), color=NEUTRAL, label="per DRC intelligence: Rwanda's air defense\nintercepts these same CH-4 drones",
      lpos=0.5, fs=8.6, lcolor=INK, rad=-0.18)

# Bottom block - other security actors (for context)
box(ax, (0.6, 1.1), 5.8, 1.9,
    "Chinese PSCs: mine-perimeter security\nin the south (Lualaba/Katanga) only, no combat\n- unlike the Wagner PMC model",
    NEUTRAL, fs=9.3)
box(ax, (6.6, 1.1), 5.8, 1.9,
    "US / E. Prince (FSG): ~$700m contract\n(Apr 2025) - taxes and security in Katanga;\ncombat-support episode near Uvira (Feb 2026)",
    GOOD, fs=9.3)

source_footer(fig, "Sources: Military Africa, The Diplomat, DefenceWeb, armyrecognition.com, ORF, Reuters/Geeska, Friends of the Congo, africansecurityanalysis.com - details on drone interception rely on DRC intelligence reports and are not independently verified.", y=-0.02)
save(fig, "09_security_actors")
