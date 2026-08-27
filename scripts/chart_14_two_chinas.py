import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(14, 8.8))
ax.set_xlim(0, 14); ax.set_ylim(0, 10.9); ax.axis("off")

ax.text(7, 10.35, "Two Chinas in Congo", ha="center", fontsize=18, fontweight="bold", color=INK)
ax.text(7, 9.85, "State corporations in Katanga and freelance gold miners in the east - not one strategy, but two unrelated ones",
        ha="center", fontsize=10.5, color=NEUTRAL)

rows = [
    ("Mineral", "copper and cobalt", "gold"),
    ("Provinces", "Lualaba, Haut-Katanga", "South Kivu, Ituri"),
    ("Actor type", "CMOC, Zijin, CNMC - state corporations", "hundreds of small private firms"),
    ("Legal status", "official concessions, contracts", "skirting the law via cooperatives"),
    ("Scale", "a few dozen large projects", "147-547+ firms, estimates vary"),
    ("Beijing's response", "diplomatic defense of the deals", "the MFA itself orders a shutdown"),
    ("Kinshasa's response", "audits, contract renegotiation", "arrests, trials, provincial suspensions"),
    ("Landmark event", "Sicomines Amendment 5, 2024", "first brokers sentenced - 7 years, 2025"),
]

x_left, x_mid, x_right = 0.3, 5.0, 9.7
w_mid, w_right = 4.5, 4.0
y0 = 8.75
row_h = 0.92

# column headers
ax.text(x_mid + w_mid/2, y0 + 0.62, "KATANGA (south)", ha="center", fontsize=13, fontweight="bold", color=CN_RED)
ax.text(x_right + w_right/2, y0 + 0.62, "SOUTH KIVU (east)", ha="center", fontsize=13, fontweight="bold", color=WARN)

for i, (label, cat, kivu) in enumerate(rows):
    y = y0 - i * row_h
    bg = "#F7F7F7" if i % 2 == 0 else "#FFFFFF"
    ax.add_patch(FancyBboxPatch((0.1, y - row_h + 0.12), 13.8, row_h - 0.12,
                                 boxstyle="square,pad=0", linewidth=0, facecolor=bg, zorder=1))
    ax.text(x_left, y - row_h/2 + 0.12, label, ha="left", va="center", fontsize=10.3,
            fontweight="bold", color=INK, zorder=2)
    ax.text(x_mid + w_mid/2, y - row_h/2 + 0.12, cat, ha="center", va="center", fontsize=9.8,
            color=INK, zorder=2, wrap=True)
    ax.text(x_right + w_right/2, y - row_h/2 + 0.12, kivu, ha="center", va="center", fontsize=9.8,
            color=INK, zorder=2, wrap=True)

source_footer(fig, "Sources: VOA, AP, Africa Defense Forum, IFRI, Business & Human Rights Centre, Copperbelt Katanga Mining - estimates of the number of firms in South Kivu vary by year and source (147-547+).", y=0.01)
save(fig, "14_two_chinas_comparison")
