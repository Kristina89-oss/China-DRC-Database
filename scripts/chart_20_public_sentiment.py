import sys
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig = plt.figure(figsize=(17, 14.5))

fig.text(0.5, 0.975, "What Congolese Residents Themselves Say", ha="center", fontsize=21, fontweight="bold", color=INK)
fig.text(0.5, 0.952, "Named, on-the-record voices gathered by journalists and NGOs \u2014 the closest available proxy for grassroots opinion",
         ha="center", fontsize=11, color=NEUTRAL)

ax = fig.add_axes([0.03, 0.06, 0.94, 0.87])
ax.set_xlim(0, 10)
ax.set_ylim(0, 13.4)
ax.axis("off")

def card(x, y, w, h, name, role, quote, theme_color, fs_name=10.3, fs_role=8.2, fs_quote=9.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                 linewidth=0, facecolor="#F7F7F7", zorder=2))
    ax.add_patch(FancyBboxPatch((x, y), 0.09, h, boxstyle="square,pad=0",
                                 linewidth=0, facecolor=theme_color, zorder=3))
    ax.text(x + 0.32, y + h - 0.32, name, fontsize=fs_name, fontweight="bold", color=INK, va="top", zorder=4)
    ax.text(x + 0.32, y + h - 0.72, role, fontsize=fs_role, color=NEUTRAL, va="top", style="italic", zorder=4, linespacing=1.3)
    ax.text(x + 0.32, y + h - 1.18, quote, fontsize=fs_quote, color=INK, va="top", zorder=4, linespacing=1.42)

col_w = 4.75
gap = 0.3
xL, xR = 0.1, 0.1 + col_w + gap

# --- Left column: grievances ---
ax.text(xL, 13.15, "GRIEVANCES", fontsize=12.5, fontweight="bold", color=WARN)
card(xL, 11.55, col_w, 1.5, "Pierre", "Resident, Noa village, copper-cobalt belt",
     "\u201cWe live in an environment that\nbrings us more problems than solutions.\u201d", WARN)
card(xL, 9.85, col_w, 1.5, "Jean Marc Kananga Muleba", "Resident, Kolwezi",
     "Says finding a new home with power and\nwater is unimaginable on the ~$7,500 paid\nper demolished house.", WARN)
card(xL, 8.15, col_w, 1.5, "Adelard Makonga", "Resident, Tshabula village, Kolwezi",
     "Refused a cash payout, held out for a\nproper legal relocation from COMMUS (Zijin).", WARN)
card(xL, 6.45, col_w, 1.5, "Edmond Chansa, 60", "Displaced resident, Kolwezi",
     "Regrets his new living conditions after\nbeing relocated for a COMMUS quarry.", WARN)
card(xL, 4.75, col_w, 1.65, "Unnamed mother", "Kolwezi, reacting to a beating\nof diggers filmed on camera",
     "Says she was deeply shocked to see her\ncompatriots treated so inhumanely; has\nalready gone to the courts.", CN_RED_DARK)
card(xL, 3.1, col_w, 1.45, "Ghislain Chivundu Mutalemba", "Commander, local mining brigade,\nKamituga, South Kivu",
     "\u201cOn contr\u00f4le difficilement ces\nsoci\u00e9t\u00e9s.\u201d (\u201cThese companies are hard\nto keep tabs on.\u201d)", CN_GOLD)
card(xL, 1.4, col_w, 1.5, "Hilaire Isombya", "Civil-society coordinator,\nMwenga, South Kivu",
     "Argues Chinese-linked mining activity\nhas itself become a source of local\ninsecurity.", CN_GOLD)

# --- Right column: civil society + counterpoints + polling ---
ax.text(xR, 13.15, "CIVIL SOCIETY & COUNTERPOINTS", fontsize=12.5, fontweight="bold", color=DRC_BLUE)
card(xR, 11.45, col_w, 1.6, "CNPAV coalition", "\u201cCongo Is Not for Sale\u201d",
     "Sicomines tax breaks cost the treasury\n\\$132m in 2024; below \\$8,000/t copper,\nDRC \u201cwill receive less, or even nothing.\u201d", DRC_BLUE)
card(xR, 9.6, col_w, 1.75, "South Kivu parliamentary commission", "",
     "Formally found six Chinese firms guilty of\nillegal gold/cassiterite mining in Mwenga,\nshielded by local cooperatives, polluting\nrivers with mining chemicals.", DRC_BLUE)
card(xR, 7.95, col_w, 1.55, "Amnesty International + IBGDH", "Joint press conference, Lubumbashi, 2025",
     "Condemned forced evictions in Kolwezi\ncarried out for mining expansion without\nresettlement plans or fair compensation.", DRC_BLUE)
card(xR, 6.55, col_w, 1.3, "Zhu Jing", "Then-Chinese Ambassador to the DRC,\non Twitter, 2021",
     "Warned the DRC \u201cmust not become the\nbattleground for great powers.\u201d", NEUTRAL)
card(xR, 4.95, col_w, 1.5, "Aaron Chen", "GM Operations, MMG Kinsevere\n(China Minmetals), at Cobalt Institute congress",
     "Publicly demanded Kinshasa clarify its\ncobalt quota rules, calling his firm's\nallocation insufficient and damaging.", CN_RED)
card(xR, 3.35, col_w, 1.5, "Chinese Embassy in DRC", "Official public messaging, 2024-2026",
     "Consistently frames ties as \u201cwin-win\u201d\nmodernization and deep friendship dating\nto the independence era.", CN_RED)

ax.add_patch(FancyBboxPatch((xR, 0.5), col_w, 2.6, boxstyle="round,pad=0.02,rounding_size=0.09",
                             linewidth=1.6, edgecolor=GOOD, facecolor="#EFF7F1", zorder=2))
ax.text(xR + 0.32, 2.85, "AFROBAROMETER (continent-wide, not DRC-specific)", fontsize=9.6, fontweight="bold", color=GOOD, va="top")
ax.text(xR + 0.32, 2.4, "~60-66% of Africans surveyed across 34-36\ncountries call China's influence \u201cpositive\u201d\n(vs. 13-14% negative) \u2014 similar to the US.\nBut most who know of Chinese loans worry\ntheir country has borrowed too much, and\nthe US still edges out China as preferred\ndevelopment model.", fontsize=8.9, color=INK, va="top", linespacing=1.45)

source_footer(fig, "Sources: Mongabay, RAID ('Beneath the Green'), VOA Afrique, Actualite.cd, Anadolu Agency, AllAfrica, France24 Observers, AFREWATCH, SCMP, Le Blog Auto, Chinese Embassy in DRC, Afrobarometer. Full citations and methodology caveats in data/public_sentiment.json and SOURCES.md.", y=0.01)
save(fig, "20_public_sentiment_wall")
