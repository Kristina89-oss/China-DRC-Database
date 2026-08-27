import sys, math
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

color_map = {"cn": CN_RED, "west": DRC_BLUE, "mixed": CN_GOLD, "energy": GOOD, "city": INK}
label_map = {"cn": "Chinese-controlled", "west": "Western company",
             "mixed": "Mixed ownership", "energy": "Energy", "city": "City"}

fig, ax = plt.subplots(figsize=(13, 9.2))

# --- distant, genuinely separated sites (km from Kolwezi kept proportional) ---
far_sites = [
    ("Tenke Fungurume", 3.9, 1.35, "cn", "CMOC 80%"),
    ("Kisanfu", 5.1, 2.55, "cn", "CMOC+CATL 95%"),
    ("Kambove", 6.5, -0.9, "cn", "CNMC 55%"),
    ("Busanga dam", 2.1, 3.9, "energy", "Sicomines consortium"),
    ("Lubumbashi", 9.8, -3.2, "city", "city, regional capital, ~120 km"),
]
for name, x, y, cat, own in far_sites:
    color = color_map[cat]
    marker = "s" if cat == "city" else ("^" if cat == "energy" else "o")
    size = 260 if cat == "city" else 170
    ax.scatter([x], [y], s=size, color=color, marker=marker, edgecolor="white", linewidth=1.4, zorder=5)
    ax.annotate(name, (x, y), xytext=(9, 7), textcoords="offset points", fontsize=11, fontweight="bold", color=INK, zorder=6)
    ax.annotate(own, (x, y), xytext=(9, -8), textcoords="offset points", fontsize=8.8, color=NEUTRAL, zorder=6)

# --- dense cluster around Kolwezi: arranged in a ring, since real sites sit 2-15 km apart ---
hub_x, hub_y = 0, 0
ax.add_patch(Circle((hub_x, hub_y), 1.55, facecolor="#F2F2F2", edgecolor=NEUTRAL, linewidth=1, zorder=1, alpha=0.7))
ax.scatter([hub_x], [hub_y], s=300, color=INK, marker="s", edgecolor="white", linewidth=1.5, zorder=5)
ax.annotate("Kolwezi", (hub_x, hub_y), xytext=(0, 14), textcoords="offset points",
            fontsize=12.5, fontweight="bold", color=INK, ha="center", zorder=6)
ax.annotate("~600,000 pop.", (hub_x, hub_y), xytext=(0, -20), textcoords="offset points",
            fontsize=8.6, color=NEUTRAL, ha="center", zorder=6)

ring = [
    ("COMMUS", "cn", "Zijin ~70%"),
    ("Kamoa-Kakula", "mixed", "Ivanhoe 39.6% / Zijin 39.6%"),
    ("Mutanda (MUMI)", "west", "Glencore 95%"),
    ("Pumpi", "cn", "Wanbao (Norinco) 75%"),
    ("Deziwa", "cn", "CNMC 51%"),
    ("Nzilo I/II dams", "energy", "CMOC + SNEL"),
]
n = len(ring)
radius = 2.55
for i, (name, cat, own) in enumerate(ring):
    ang = math.radians(90 - i * (360 / n))
    x = hub_x + radius * math.cos(ang)
    y = hub_y + radius * math.sin(ang) * 0.72
    color = color_map[cat]
    marker = "^" if cat == "energy" else "o"
    ax.scatter([x], [y], s=170, color=color, marker=marker, edgecolor="white", linewidth=1.4, zorder=5)
    ha = "left" if x >= 0 else "right"
    dx = 9 if x >= 0 else -9
    ax.annotate(name, (x, y), xytext=(dx, 6), textcoords="offset points", fontsize=10.3,
                fontweight="bold", color=INK, ha=ha, zorder=6)
    ax.annotate(own, (x, y), xytext=(dx, -9), textcoords="offset points", fontsize=8.3,
                color=NEUTRAL, ha=ha, zorder=6)
    ax.plot([hub_x, x*0.35], [hub_y, y*0.35], color=NEUTRAL, linewidth=0.6, alpha=0.5, zorder=1)

ax.set_xlim(-4.2, 11.5)
ax.set_ylim(-5.4, 5.0)
ax.set_aspect("equal")
ax.axis("off")

fig.subplots_adjust(top=0.90)
ax.set_title("Map 2. The copper-cobalt cluster around Kolwezi (Lualaba)", fontsize=16.5, fontweight="bold", pad=16)

handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=c, markersize=11, label=label_map[k])
           for k, c in color_map.items() if k not in ("city", "energy")]
handles.append(plt.Line2D([0], [0], marker="^", color="w", markerfacecolor=GOOD, markersize=11, label=label_map["energy"]))
handles.append(plt.Line2D([0], [0], marker="s", color="w", markerfacecolor=INK, markersize=10, label="City"))
ax.legend(handles=handles, loc="lower left", frameon=True, framealpha=0.9, fontsize=10)

source_footer(fig, "Schematic: distances between sites near Kolwezi (actually 2-15 km) are enlarged for legibility; not for navigation. Relative positions reconstructed from open descriptions (e.g. 'TFM - 110 km northwest of Lubumbashi', 'Kisanfu - 33 km from TFM'); exact coordinates are not published by the companies.", y=0.0)
save(fig, "16_map_mining_belt")
