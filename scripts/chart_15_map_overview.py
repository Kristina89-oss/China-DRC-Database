import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Ellipse

# Rough, simplified schematic DRC outline (not for navigation), (lon, lat)
drc_outline = [
    (12.2,-5.9),(12.4,-5.0),(13.6,-4.4),(14.8,-4.85),(16.2,-3.6),(17.5,-4.1),
    (17.9,-6.9),(18.0,-7.9),(19.4,-7.3),(20.6,-6.9),(21.9,-7.4),(22.4,-9.9),
    (23.0,-10.8),(24.0,-11.5),(24.3,-12.9),(25.3,-11.6),(28.6,-12.9),(28.9,-9.0),
    (29.3,-6.5),(29.3,-4.45),(29.0,-2.75),(29.6,-1.35),(29.75,0.15),(30.8,1.0),
    (30.4,3.5),(29.0,4.5),(27.4,5.1),(25.2,5.05),(22.4,4.7),(18.6,4.2),
    (17.7,3.5),(16.0,2.4),(14.6,2.2),(13.0,-1.0),(12.2,-5.9)
]
xs = [p[0] for p in drc_outline]; ys=[p[1] for p in drc_outline]

fig, ax = plt.subplots(figsize=(12, 12.5))
ax.fill(xs, ys, color="#EFEFEF", zorder=1, edgecolor=NEUTRAL, linewidth=1.3)

# zones of interest
def zone(cx, cy, w, h, color, angle=0):
    e = Ellipse((cx, cy), w, h, angle=angle, facecolor=color, alpha=0.28, edgecolor=color, linewidth=1.6, zorder=2)
    ax.add_patch(e)

zone(25.9, -10.9, 4.6, 3.2, CN_RED, angle=-20)      # south - copper/cobalt
zone(28.7, -1.9, 3.6, 5.4, WARN, angle=25)          # east - conflict/gold
zone(14.3, -5.0, 3.6, 2.6, DRC_BLUE)                # west - capital/energy
zone(27.4, -7.4, 2.2, 2.6, CN_GOLD, angle=10)       # Manono/Tanganyika - lithium

cities = [
    ("Kinshasa", 15.31, -4.32, DRC_BLUE, "star"),
    ("Kolwezi", 25.47, -10.72, CN_RED, "dot"),
    ("Lubumbashi", 27.48, -11.66, CN_RED, "dot"),
    ("Manono", 27.42, -7.30, CN_GOLD, "dot"),
    ("Goma", 29.22, -1.68, WARN, "dot"),
    ("Bukavu", 28.86, -2.50, WARN, "dot"),
]
for name, lon, lat, color, marker in cities:
    if marker == "star":
        ax.scatter([lon],[lat], marker="*", s=420, color=color, edgecolor="white", linewidth=1.2, zorder=5)
    else:
        ax.scatter([lon],[lat], marker="o", s=110, color=color, edgecolor="white", linewidth=1.3, zorder=5)
    ax.annotate(name, (lon,lat), xytext=(7,6), textcoords="offset points", fontsize=11.5, fontweight="bold", color=INK, zorder=6)

# neighbours
neighbours = [
    ("ANGOLA", 15.5, -9.6), ("ZAMBIA", 26.5, -13.6), ("TANZANIA", 32.3, -7.6),
    ("RWANDA", 30.6, -3.05), ("UGANDA", 31.5, 1.6), ("SOUTH SUDAN", 27.5, 6.1),
    ("CAR", 20.5, 5.9), ("R. CONGO", 15.5, 0.6), ("BURUNDI", 31.3, -4.35),
]
for name, lon, lat in neighbours:
    ax.text(lon, lat, name, fontsize=9.3, color=NEUTRAL, ha="center", style="italic")

# corridors
ax.add_patch(FancyArrowPatch((22.0,-9.6), (13.4,-11.7), arrowstyle="-|>", mutation_scale=20,
                              color=GOOD, lw=2.6, connectionstyle="arc3,rad=-0.15", zorder=4))
ax.text(13.0,-13.1, "Lobito Corridor\n\u2192 Atlantic", fontsize=9.7, color=GOOD, fontweight="bold", ha="center", linespacing=1.3)

ax.add_patch(FancyArrowPatch((27.4,-12.4), (33.0,-15.2), arrowstyle="-|>", mutation_scale=20,
                              color=CN_RED, lw=2.6, connectionstyle="arc3,rad=-0.15", zorder=4))
ax.text(33.6,-15.9, "TAZARA\n\u2192 Indian\nOcean", fontsize=9.7, color=CN_RED, fontweight="bold", ha="left", linespacing=1.3)

ax.set_xlim(10, 36); ax.set_ylim(-17, 8)
ax.set_aspect("equal")
ax.axis("off")

ax.set_title("Map 1. The DRC: three zones of the story and two export corridors", fontsize=16.5, fontweight="bold", pad=14)

handles = [
    mpatches.Patch(color=CN_RED, alpha=0.5, label="South - copper/cobalt (the report's main topic)"),
    mpatches.Patch(color=CN_GOLD, alpha=0.5, label="Tanganyika - lithium (Manono)"),
    mpatches.Patch(color=WARN, alpha=0.5, label="East - M23 conflict & illegal gold"),
    mpatches.Patch(color=DRC_BLUE, alpha=0.5, label="West - capital & energy (Inga)"),
]
ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=10, bbox_to_anchor=(-0.02,-0.02))

source_footer(fig, "Schematic map for orientation only - simplified borders, not for navigation and not geographically precise in detail.", y=0.01)
save(fig, "15_map_overview")
