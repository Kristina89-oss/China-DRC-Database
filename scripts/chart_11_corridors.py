import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 8.6))
ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis("off")

ax.text(7, 9.5, "Two corridors, one ore", ha="center", fontsize=17, fontweight="bold", color=INK)
ax.text(7, 9.0, "Competition has shifted from 'who owns the mines' to 'who controls the routes'",
        ha="center", fontsize=10.5, color=NEUTRAL)

# Center - Copperbelt
c = FancyBboxPatch((5.6, 4.3), 2.8, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1",
                   linewidth=0, facecolor=INK, zorder=3)
ax.add_patch(c)
ax.text(7.0, 5.0, "Copperbelt\nDRC + Zambia", ha="center", va="center", color="white",
        fontsize=12, fontweight="bold", linespacing=1.3, zorder=4)

# West - Lobito
w = FancyBboxPatch((0.4, 3.6), 4.4, 2.8, boxstyle="round,pad=0.02,rounding_size=0.1",
                   linewidth=0, facecolor=GOOD, zorder=3)
ax.add_patch(w)
ax.text(2.6, 5.0, "LOBITO CORRIDOR\n\u2190 to the Atlantic\n\nUS \u00b7 EU \u00b7 AfDB \u00b7 AFC\nOperator: Trafigura + Mota-Engil\n$753m (July 2026)\n1,300 km \u00b7 5-8 days to port",
        ha="center", va="center", color="white", fontsize=9.8, fontweight="bold", linespacing=1.55, zorder=4)

# East - TAZARA
e = FancyBboxPatch((9.2, 3.6), 4.4, 2.8, boxstyle="round,pad=0.02,rounding_size=0.1",
                   linewidth=0, facecolor=CN_RED, zorder=3)
ax.add_patch(e)
ax.text(11.4, 5.0, "TAZARA\nto the Indian Ocean \u2192\n\nChina (BRI) \u00b7 30-year concession\nCCECC 80% + Zijin, CMOC,\nJiayou, COSCO at 5% each\n$1.24-1.4bn \u00b7 1,860 km",
        ha="center", va="center", color="white", fontsize=9.8, fontweight="bold", linespacing=1.55, zorder=4)

ax.add_patch(FancyArrowPatch((5.5, 5.0), (4.9, 5.0), arrowstyle="-|>", mutation_scale=22, color=GOOD, lw=3, zorder=2))
ax.add_patch(FancyArrowPatch((8.5, 5.0), (9.1, 5.0), arrowstyle="-|>", mutation_scale=22, color=CN_RED, lw=3, zorder=2))

# Paradox
p = FancyBboxPatch((1.4, 0.7), 11.2, 2.3, boxstyle="round,pad=0.02,rounding_size=0.1",
                   linewidth=2, edgecolor=WARN, facecolor="#FDF6E8", zorder=3)
ax.add_patch(p)
ax.text(7.0, 1.85, "PARADOX: the Western corridor hauls ore from Chinese-owned mines\n\n"
                   "Lobito's open-access model can't exclude Chinese companies - they're its biggest customers.\n"
                   "Zijin owns 39.6% of Kamoa-Kakula (Lobito's largest user) and has also taken a stake in TAZARA.\n"
                   "CMOC accounts for 21.9% of DRC copper exports - and is also a TAZARA shareholder. Chinese groups are hedging both routes.",
        ha="center", va="center", fontsize=10, color=INK, linespacing=1.65, zorder=4)

source_footer(fig, "Sources: Reuters/Ecofin Agency (2026-04), OECD Background Note, ORF, Veracity Worldwide, Africa Finance Corporation, bne IntelliNews, S&P Global.", y=0.02)
save(fig, "11_transport_corridors")
