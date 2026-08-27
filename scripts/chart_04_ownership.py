import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt

# project, China share %, who exactly (China), remainder and its holder
projects = [
    ("Sicomines\n(flagship RFI deal)", 68, "China Railway + Sinohydro", 32, "Gecamines"),
    ("Kisanfu (KFM)", 95, "CMOC 71.25% + CATL 23.75%", 5, "DRC (state)"),
    ("Tenke Fungurume\n(TFM)", 80, "CMOC", 20, "Gecamines"),
    ("Pumpi", 75, "Wanbao Mining (Norinco)", 25, "Managem 20% + DRC 5%"),
    ("Kambove", 55, "CNMC", 45, "Gecamines"),
    ("Deziwa", 51, "CNMC", 49, "Gecamines"),
    ("Manono Lithium\n(Cominiere's site)", 61, "Zijin Mining", 39, "Cominiere (state)"),
]
projects = sorted(projects, key=lambda p: p[1])

labels = [p[0] for p in projects]
cn = [p[1] for p in projects]
other = [p[3] for p in projects]

fig, ax = plt.subplots(figsize=(12, 7.5))
y = range(len(projects))

ax.barh(y, cn, color=CN_RED, height=0.62, label="China share", zorder=3)
ax.barh(y, other, left=cn, color=DRC_BLUE, height=0.62, label="DRC / other", zorder=3)

for i, (name, c, who_cn, o, who_o) in enumerate(projects):
    ax.text(c / 2, i, f"{c}%", ha="center", va="center", color="white", fontweight="bold", fontsize=11.5)
    ax.text(c + o / 2, i, f"{o}%", ha="center", va="center", color="white", fontweight="bold", fontsize=10.5)
    ax.text(101.5, i, who_cn, va="center", ha="left", fontsize=9, color=CN_RED_DARK)

ax.set_yticks(list(y))
ax.set_yticklabels(labels, fontsize=11)
ax.set_xlim(0, 100)
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.xaxis.set_major_formatter(lambda v, pos: f"{int(v)}%")
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)
ax.grid(axis="x", alpha=0.5)
ax.tick_params(length=0)
ax.set_xlim(0, 165)
ax.axvline(100, color=INK, linewidth=0.8, alpha=0.3)

ax.legend(loc="lower right", frameon=False, fontsize=10.5)
ax.set_title("Who owns the DRC's key mines", fontsize=16, fontweight="bold", pad=16)

source_footer(fig, "Sources: CMOC, CATL, CNMC filings; Freeport-McMoRan SEC filings; Wikipedia/CMOC Group; Mining.com, Bankable - shares rounded as of the latest deal date.")
save(fig, "04_ownership_by_project")
