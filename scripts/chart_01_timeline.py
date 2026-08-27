import sys, textwrap
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt


# (date label, short text, category)
events = [
    ("Apr 2008", "Sicomines:\n68% China / 32%\nGecamines", "cn"),
    ("Nov 2016", "CMOC: 56%\nof Tenke Fungurume\nfor $2.65bn", "cn"),
    ("Apr 2021", "CATL - 25%\nof Kisanfu for\n$137.5m", "cn"),
    ("Nov 2021", "Congo Hold-up:\nleak of 3.5m\nBGFIBank docs", "corr"),
    ("Feb 2023", "IGF audit: $822m\ninvested vs.\n~$10bn profit", "corr"),
    ("Oct 2023", "Busanga dam\ncomes online,\n240 MW", "energy"),
    ("Mar 2024", "Sicomines:\nAmendment 5 -\nup to $7bn", "cn"),
    ("Feb 2025", "DRC halts\ncobalt\nexports", "drc"),
    ("Apr 2025", "E. Prince: ~$700m\ncontract for\nKatanga security", "us"),
    ("Oct 2025", "Ban to quotas:\n96,600 t/yr\nfor 2026-2027", "drc"),
    ("Dec 2025", "US-DRC\nminerals\npact in DC", "us"),
    ("Mar 2026", "New Sicomines\naudit\n(2008-2024)", "corr"),
    ("Apr 2026", "Virtus Minerals -\nfirst US deal\nunder the program", "us"),
    ("Jul 2026", "Customs failure:\n$1.1bn of cobalt\nexports at risk", "drc"),
]

color_map = {"cn": CN_RED, "corr": WARN, "energy": CN_GOLD, "drc": DRC_BLUE, "us": GOOD}
label_map = {
    "cn": "China expansion & deals",
    "corr": "Corruption & audits",
    "energy": "Energy",
    "drc": "DRC protectionism",
    "us": "US counter-play",
}

n = len(events)
xs = list(range(n))
# 4 alternating levels (near/far, up/down) so labels of neighboring
# points in the same direction don't collide
levels = [1.0, -1.0, 0.5, -0.5]

fig, ax = plt.subplots(figsize=(18, 9.5))
ax.axhline(0, color=INK, linewidth=1.6, zorder=1)
ax.set_xlim(-0.6, n - 0.4)
ax.set_ylim(-1.55, 1.55)

for i, (date, text, cat) in enumerate(events):
    x = xs[i]
    lvl = levels[i % 4]
    sign = 1 if lvl > 0 else -1
    color = color_map[cat]
    ax.plot([x, x], [0, lvl * 0.30], color=color, linewidth=2, zorder=2)
    ax.scatter([x], [0], color=color, s=130, zorder=4, edgecolor="white", linewidth=1.4)
    y0 = lvl * 0.36
    va = "bottom" if sign > 0 else "top"
    ax.text(x, y0, date, fontsize=11, fontweight="bold", color=color, ha="center", va=va)
    y1 = y0 + sign * 0.155
    ax.text(x, y1, text, fontsize=8.6, color=INK, ha="center", va=va, linespacing=1.4)

ax.set_yticks([])
ax.set_xticks([])
for spine in ("top", "right", "left", "bottom"):
    ax.spines[spine].set_visible(False)
ax.grid(False)

ax.set_title("From the 'deal of the century' to an audit: China's DRC footprint, 2008-2026",
             fontsize=16, fontweight="bold", color=INK, pad=10)
ax.text(0.5, 1.045, "(events are ordered sequentially, not on a linear time scale)",
        transform=ax.transAxes, ha="center", fontsize=9.5, color=NEUTRAL, style="italic")

handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=c, markersize=11, label=label_map[k])
           for k, c in color_map.items()]
ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.05),
          ncol=5, frameon=False, fontsize=11)

source_footer(fig, "Sources: EITI, AidData, Mining.com, Bloomberg, Reuters, PPLAAF/The Sentry, ARECOMS/IEA, CFR - full list in SOURCES.md",
              y=0.01)
save(fig, "01_timeline_2008_2026")
