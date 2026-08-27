import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def box(ax, xy, w, h, title, sub, fc, tc="white", fs_t=9.6, fs_s=7.6):
    x, y = xy
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                        linewidth=0, facecolor=fc, zorder=4)
    ax.add_patch(p)
    ax.text(x + w/2, y + h*0.66, title, ha="center", va="center", color=tc, fontsize=fs_t,
            fontweight="bold", zorder=5, linespacing=1.2)
    ax.text(x + w/2, y + h*0.28, sub, ha="center", va="center", color=tc, fontsize=fs_s,
            zorder=5, linespacing=1.2, alpha=0.92)
    return (x, y, w, h)


def arrow(ax, p1, p2, color=INK, label=None, lw=1.8, rad=0.0, lpos=0.5, fs=8, style="-|>"):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=14, color=color,
                         linewidth=lw, zorder=2, connectionstyle=f"arc3,rad={rad}",
                         shrinkA=6, shrinkB=6)
    ax.add_patch(a)
    if label:
        mx, my = p1[0] + (p2[0]-p1[0])*lpos, p1[1] + (p2[1]-p1[1])*lpos
        ax.text(mx, my, label, fontsize=fs, color=color, ha="center", va="center", zorder=6,
                fontweight="bold", bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))


fig, ax = plt.subplots(figsize=(19, 15))
ax.set_xlim(0, 19); ax.set_ylim(0, 15); ax.axis("off")

ax.text(9.5, 14.6, "Who's who: the people on both sides", ha="center", fontsize=20, fontweight="bold", color=INK)
ax.text(9.5, 14.1, "Current and historical figures - diplomats, executives, ministers, the corruption network",
        ha="center", fontsize=11, color=NEUTRAL)

col_w = 6.6
xl, xr = 0.6, 11.8

ax.text(xl + col_w/2, 13.5, "CHINA", ha="center", fontsize=14, fontweight="bold", color=CN_RED)
ax.text(xr + col_w/2, 13.5, "DRC", ha="center", fontsize=14, fontweight="bold", color=DRC_BLUE)

# --- CHINA, current ---
b_zhao = box(ax, (xl, 12.1), col_w, 1.0, "Zhao Bin", "Chinese Ambassador to the DRC", CN_RED)
b_wang = box(ax, (xl, 10.85), col_w, 1.0, "Wang Xiaohong", "State Councillor, Minister of Public Security", CN_RED)
b_liu  = box(ax, (xl, 9.6), col_w, 1.0, "Liu Jianfeng", "Chairman, CMOC (since 2025)", CN_RED)
b_peng = box(ax, (xl, 8.35), col_w, 1.0, "Peng Xuhui", "CEO, CMOC Group", CN_RED)
b_sun  = box(ax, (xl, 7.1), col_w, 1.15, "Sun Ruiwen", "Chief Commercial Officer, CMOC \u00b7\nex-chairman, Busanga Dam & China Railway Resource Group", CN_RED_DARK, fs_s=7.2)
b_duwei = box(ax, (xl, 5.55), col_w, 1.0, "Du Wei", "Intermediary, Congo Construction Co.", WARN)

# --- DRC, current ---
b_tshi = box(ax, (xr, 12.1), col_w, 1.0, "Felix Tshisekedi", "President of the DRC (since 2019)", DRC_BLUE)
b_shab = box(ax, (xr, 10.85), col_w, 1.0, "J. Shabani Lukoo Bihango", "Deputy PM, Interior Ministry", DRC_BLUE)
b_watum = box(ax, (xr, 9.6), col_w, 1.0, "Louis Watum Kabamba", "Minister of Mines (since 2025)", DRC_BLUE)
b_kabemba = box(ax, (xr, 8.35), col_w, 1.0, "Baraka Kabemba", "CEO, Gecamines (since 2026)", DRC_BLUE)
b_luabeya = box(ax, (xr, 7.1), col_w, 1.0, "Patrick Mpoyi Luabeya", "President, ARECOMS", DRC_BLUE)
b_selemani = box(ax, (xr, 5.55), col_w, 1.0, "Francis Selemani", "Kabila's brother, ex-head of BGFIBank", WARN)

# top-tier links
arrow(ax, (xl+col_w, 12.6), (xr, 12.6), color=NEUTRAL, label="diplomatic channel", lpos=0.5, rad=0.05)
arrow(ax, (xl+col_w, 11.35), (xr, 11.35), color=GOOD, label="26 May 2026 agreement\n(police, cyber, fraud)", lpos=0.5, rad=-0.05, fs=7.5)
arrow(ax, (xl+col_w, 10.1), (xr, 10.1), color=CN_RED, label="quota & contract\nregulation", lpos=0.5, rad=0.05, fs=7.5)
arrow(ax, (xl+col_w, 8.6), (xr, 8.6), color=CN_RED, label="Sicomines talks,\n2026 audit", lpos=0.5, rad=-0.05, fs=7.5)
arrow(ax, (xl+col_w, 7.6), (xr, 7.6), color=CN_RED_DARK, label="Sun Ruiwen personally chaired\nBusanga Dam (2012-17)", lpos=0.5, rad=0.05, fs=7)

# corruption channel below
arrow(ax, (xl+col_w, 6.0), (xr, 6.0), color=WARN, label="CCC \u2192 BGFIBank\n$55-65m", lpos=0.5, rad=-0.15, fs=7.5, style="-|>")

b_net = box(ax, (xr, 4.0), col_w, 1.05, "Joseph Kabila's network", "Zoe Kabila \u00b7 Jaynet Kabila - relatives,\nbusiness interests in mineral provinces", CN_RED_DARK, fs_s=7.2)
arrow(ax, (xr+col_w/2, 5.55), (xr+col_w/2, 5.05), color=WARN, lw=2.2)

# --- Historical block at the bottom, full width ---
ax.text(9.5, 3.35, "HISTORY: FROM SIGNING TO DEATH SENTENCE", ha="center", fontsize=11.5, fontweight="bold", color=NEUTRAL)

hb_w = 4.35
h_y = 1.55
hist = [
    ("Adolphe Muzito", "DRC Prime Minister\nwhen Sicomines was\nsigned (2008)", DRC_BLUE, 0.4),
    ("Joseph Kabila", "Ex-president; signed the deal.\nSentenced to death in absentia\nfor treason (30 Sep 2025)", CN_RED_DARK, 0.4+hb_w+0.5),
    ("Albert Yuma Mulimbi", "Ex-chairman, Gecamines\n(until 2021), Kabila loyalist", NEUTRAL, 0.4+2*(hb_w+0.5)),
    ("Kizito Pakabomba", "Ex-Minister of Mines\n(2024-25): imposed the\ncobalt export ban", NEUTRAL, 0.4+3*(hb_w+0.5)),
]
for i, (t, s, c, x) in enumerate(hist):
    box(ax, (x, h_y), hb_w, 1.25, t, s, c, fs_t=9.5, fs_s=7.3)

arrow(ax, (0.4+hb_w, h_y+0.6), (0.4+hb_w+0.5, h_y+0.6), color=NEUTRAL, label="", rad=0)
ax.text(9.5, 0.55,
        "Muzito signed the deal as PM (2008) - today, as Tshisekedi's budget minister, he publicly calls its result 'zero for the country.'\n"
        "Yuma and Pakabomba have been replaced by successors oriented toward reworking ties with China and partnering with the US (Kabemba, Watum Kabamba).",
        ha="center", fontsize=9, color=INK, linespacing=1.6)

source_footer(fig, "Sources and a status breakdown for each figure (fact / allegation / one party's claim) are in data/key_people.json and SOURCES.md. Positions current as of August 2026.", y=0.005)
save(fig, "18_people_network")
