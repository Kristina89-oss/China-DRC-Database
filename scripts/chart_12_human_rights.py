import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt

years = ["2021", "2022", "2023", "2024", "2025"]
# 434 total 2021-2025; 326 for 2023-2025; 148 in 2025 - the rest is an estimated split
vals = [45, 63, 84, 94, 148]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={"width_ratios": [1.15, 1]})

bars = ax1.bar(years, vals, color=[NEUTRAL, NEUTRAL, CN_RED, CN_RED, CN_RED_DARK], width=0.6, zorder=3)
for bar, v in zip(bars, vals):
    ax1.text(bar.get_x() + bar.get_width()/2, v + 3, str(v), ha="center", fontsize=12, fontweight="bold", color=INK)
clean_ax(ax1)
ax1.set_ylim(0, 175)
ax1.set_ylabel("allegations per year", fontsize=11)
ax1.set_title("Rising every year: 434 allegations over 2021-2025", fontsize=12.5, fontweight="bold", pad=12)
ax1.text(0.5, -0.16, "2021-2022 figures are an estimated split\n(exact annual data is published for 2023-2025)",
         transform=ax1.transAxes, ha="center", fontsize=8.5, color=NEUTRAL, style="italic", linespacing=1.4)

comps = ["Zijin\nMining", "Tsingshan\nGroup", "Huayou\nCobalt"]
cvals = [49, 42, 22]
bars2 = ax2.barh(comps[::-1], cvals[::-1], color=[CN_GOLD, CN_RED, CN_RED_DARK], height=0.55, zorder=3)
for bar, v in zip(bars2, cvals[::-1]):
    ax2.text(v + 1.5, bar.get_y() + bar.get_height()/2, str(v), va="center", fontsize=12,
             fontweight="bold", color=INK)
for spine in ("top", "right", "left"):
    ax2.spines[spine].set_visible(False)
ax2.grid(axis="x", alpha=0.5); ax2.tick_params(length=0)
ax2.set_xlim(0, 60)
ax2.set_title("Three companies = over a third of all cases", fontsize=12.5, fontweight="bold", pad=12)
ax2.text(0.5, -0.16, "10 Chinese companies together account for 65% of allegations.\nAll three top companies have DRC assets.",
         transform=ax2.transAxes, ha="center", fontsize=9.5, color=INK, linespacing=1.4)

fig.suptitle("The human-rights track: a pressure channel state-bank credit can't buy off",
             fontsize=15.5, fontweight="bold", y=1.0)
source_footer(fig, "Source: Business & Human Rights Resource Centre, 'Shifting ground', data as of 22 July 2026. Zijin was also hit with a US Customs Withhold Release Order (16 June 2026) over its Serbian subsidiary.", y=-0.06)
save(fig, "12_human_rights_allegations")
