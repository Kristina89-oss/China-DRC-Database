import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig = plt.figure(figsize=(16, 13))
gs = fig.add_gridspec(2, 2, height_ratios=[1.05, 1], width_ratios=[1.15, 1],
                       hspace=0.38, wspace=0.28, left=0.06, right=0.96, top=0.88, bottom=0.10)

fig.text(0.5, 0.965, "Who actually guards China's assets in the DRC",
          ha="center", fontsize=20, fontweight="bold", color=INK)
fig.text(0.5, 0.935, "Not the PLA, and not a 'second Wagner' - state-licensed PSCs, plus hiring FARDC itself",
          ha="center", fontsize=11.5, color=NEUTRAL)

# --- Panel 1: companies (top-left) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.axis("off")
ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)
ax1.text(0, 9.6, "PSCs confirmed to be operating in the DRC", fontsize=13, fontweight="bold", color=CN_RED)

companies = [
    ("DeWe Security Service", "Founded 2011. The most visible. Operates in the DRC, Cameroon,\nChad, Nigeria, Djibouti, Ethiopia. 352 full-time staff\nabroad + ~3,000 local hires (globally)."),
    ("Huaxin Zhong An Security Group", "One of 3 companies licensed to carry weapons abroad.\nSpecializes in maritime escort + facility security."),
    ("Shandong Huawei/Haiwei Security", "Per the Africa Center, specializes specifically\nin guarding Chinese mines in southern Africa."),
    ("China Security Technology, VSS Security", "In Sudan/South Sudan they accompany local forces\non operations - the most 'permissive' model."),
]
y = 8.75
for name, desc in companies:
    n_lines = desc.count("\n") + 1
    box_h = 0.75 + 0.42 * n_lines
    ax1.add_patch(FancyBboxPatch((0, y-box_h), 10, box_h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                  linewidth=0, facecolor="#F7F2EC", zorder=2))
    ax1.text(0.25, y-0.28, name, fontsize=10.8, fontweight="bold", color=CN_RED_DARK, zorder=3, va="top")
    ax1.text(0.25, y-0.72, desc, fontsize=8.7, color=INK, zorder=3, linespacing=1.5, va="top")
    y -= box_h + 0.35

# --- Panel 2: scale in context (top-right) ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.axis("off")
ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)
ax2.text(0, 9.6, "Scale in context", fontsize=13, fontweight="bold", color=CN_RED)

stats = [
    ("20 of 5,000", "Chinese PSCs are licensed to work abroad"),
    ("14 African countries", "including the DRC - where Chinese PSCs operate"),
    ("35,000+", "DeWe + Huaxin Zhong An contractors across 50 countries"),
    ("> 2,500", "more than the PLA's entire personnel\non the continent (peacekeepers + the Djibouti base)"),
    ("$10bn/year", "spent by Chinese state companies on security worldwide"),
    ("0", "PLA bases in the DRC; the PLA's only overseas\nbase in Africa is in Djibouti"),
]
y = 8.6
for big, small in stats:
    ax2.text(0.2, y, big, fontsize=17, fontweight="bold", color=CN_RED, va="top")
    ax2.text(3.6, y+0.05, small, fontsize=9, color=INK, va="top", linespacing=1.35)
    y -= 1.42

# --- Panel 3: incidents timeline (bottom-left) ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.axis("off")
ax3.set_xlim(0, 10); ax3.set_ylim(0, 10)
ax3.text(0, 9.6, "Documented incidents around facility security", fontsize=13, fontweight="bold", color=WARN)

incidents = [
    ("2019-06", "TFM: ~10,000 artisanal miners forcibly evicted (Amnesty Int'l)"),
    ("2021-07", "COMMUS/Zijin, Kolwezi: 2 miners beaten by guards - video went viral"),
    ("2021-11", "Gold mine, east: 2 Chinese + a Congolese woman + a Ugandan killed, 10 missing"),
    ("2023-09", "Ambush in Lamba, Fizi (S. Kivu): 2 Chinese, 1 Ghanaian, 1 FARDC soldier killed"),
    ("2023-10", "Attack on a gold concession in Fizi: site security was provided by FARDC, not a PSC"),
    ("2018-2025", "AFREWATCH: \u226535 cases of violence against miners near mine perimeters"),
]
y = 8.7
for date, text in incidents:
    ax3.add_patch(plt.Circle((0.25, y), 0.11, color=WARN, zorder=3))
    ax3.text(0.65, y+0.32, date, fontsize=9.3, fontweight="bold", color=WARN, va="bottom")
    ax3.text(0.65, y-0.05, text, fontsize=8.5, color=INK, va="top", linespacing=1.3, wrap=True)
    y -= 1.42

# --- Panel 4: why there's no "second Wagner" (bottom-right) ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis("off")
ax4.set_xlim(0, 10); ax4.set_ylim(0, 10)
ax4.text(0, 9.6, "Why there's no 'second Wagner' in the DRC", fontsize=13, fontweight="bold", color=GOOD)

reasons = [
    "The non-interference doctrine remains\ndiplomatically valuable for Beijing",
    "Risk of neo-colonialism accusations - the number\nof human-rights complaints is already rising\n(434 allegations over 2021-25, see the human-rights track)",
    "The model already works through control\nof processing and capital,\nnot military control of territory",
]
y = 8.5
for r in reasons:
    ax4.add_patch(FancyBboxPatch((0, y-1.15), 10, 1.35, boxstyle="round,pad=0.02,rounding_size=0.08",
                                  linewidth=1.3, edgecolor=GOOD, facecolor="#EFF7F1", zorder=2))
    ax4.text(0.3, y-0.45, r, fontsize=9.3, color=INK, va="center", linespacing=1.4, zorder=3)
    y -= 1.65

ax4.add_patch(FancyBboxPatch((0, y-1.5), 10, 1.7, boxstyle="round,pad=0.02,rounding_size=0.08",
                              linewidth=1.5, edgecolor=WARN, facecolor="#FDF6E8", zorder=2))
ax4.text(5, y-0.65, "BUT: the 26 May 2026 China-DRC police\ncooperation agreement is shifting the threshold\ntoward policing and law enforcement",
          fontsize=9.3, fontweight="bold", color=WARN, ha="center", va="center", linespacing=1.4, zorder=3)

source_footer(fig, "Sources: Carnegie Endowment, Africa Center for Strategic Studies, Military Africa, Grey Dynamics, VOA, Atlas Institute, AFREWATCH, Amnesty International, Mining.com, Copperbelt Katanga Mining, SCMP. Full links in SOURCES.md.", y=0.02)
save(fig, "19_china_security_presence")
