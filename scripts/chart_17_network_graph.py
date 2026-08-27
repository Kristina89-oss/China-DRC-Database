import sys, textwrap
sys.path.insert(0, "/home/claude/repo_en/scripts")
from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from graph_data import NODES, EDGES

CAT_COLOR = {
    "cn": CN_RED, "asset": "#FFFFFF", "energy": "#FFFFFF", "drc": DRC_BLUE,
    "west": "#55606A", "corr": WARN, "mil": CN_RED_DARK, "corridor": GOOD,
}
CAT_TEXT = {
    "cn": "white", "asset": INK, "energy": INK, "drc": "white",
    "west": "white", "corr": "white", "mil": "white", "corridor": "white",
}
CAT_BORDER = {
    "asset": CN_GOLD, "energy": GOOD,
}

EDGE_STYLE = {
    "own":      dict(color=None, ls="-",  lw=1.5, alpha=0.85, fs=6.6),
    "deal":     dict(color="#8E44AD", ls=(0,(5,2)), lw=1.4, alpha=0.9, fs=6.6),
    "dispute":  dict(color="#C0392B", ls=(0,(2,1.5)), lw=1.7, alpha=0.95, fs=6.6),
    "corrupt":  dict(color=WARN, ls=(0,(1,1.3)), lw=1.8, alpha=0.95, fs=6.6),
    "military": dict(color=CN_RED_DARK, ls="-", lw=2.0, alpha=0.95, fs=6.6),
    "conflict": dict(color="#C0392B", ls=(0,(3,1)), lw=2.2, alpha=0.95, fs=6.8),
    "corridor": dict(color=GOOD, ls="-", lw=1.6, alpha=0.9, fs=6.6),
    "gov":      dict(color=NEUTRAL, ls=(0,(4,2)), lw=1.0, alpha=0.55, fs=6.2),
}

def zone_grid(ids, x0, x1, y0, y1, cols=None, rows=1):
    n = len(ids)
    pos = {}
    if rows == 1:
        if n == 1:
            xs = [(x0+x1)/2]
        else:
            xs = [x0 + i*(x1-x0)/(n-1) for i in range(n)]
        for i, nid in enumerate(ids):
            pos[nid] = (xs[i], (y0+y1)/2)
    else:
        cols = cols or (n + rows - 1)//rows
        idx = 0
        for r in range(rows):
            yy = y1 - r*(y1-y0)/max(rows-1,1)
            row_ids = ids[idx:idx+cols]
            idx += cols
            if not row_ids: continue
            if len(row_ids) == 1:
                xs = [(x0+x1)/2]
            else:
                xs = [x0 + i*(x1-x0)/(len(row_ids)-1) for i in range(len(row_ids))]
            for i, nid in enumerate(row_ids):
                pos[nid] = (xs[i], yy)
    return pos

POS = {}
POS.update(zone_grid(["cmoc","catl","cnmc","zijin","norinco","sinohydro","crg","huayou","casc","ccecc","cosco"], 3, 51, 31.3, 31.3))
POS.update(zone_grid(["sicomines","tfm","kisanfu","deziwa","kambove","pumpi","commus","mutanda","kamoa","manono","mutoshi","smelter"], 2, 39.5, 24.6, 24.6))
POS.update(zone_grid(["busanga","zongo2","nzilo2"], 42.5, 42.5, 21.8, 27.4, rows=3, cols=1))
POS.update(zone_grid(["gecamines","cominiere","egc","arecoms","snel","drcgov","fardc"], 2, 24, 17.6, 17.6))
POS.update(zone_grid(["ccc","bgfi","kabila"], 2, 14, 11, 11))
POS.update(zone_grid(["rwanda","m23"], 18, 26, 11, 11))
POS.update(zone_grid(["lobito","tazara"], 30, 36, 11, 11))
POS.update(zone_grid(["freeport","glencore","ivanhoe","trafigura","avz","kobold"], 46.5, 46.5, 9.5, 29, rows=6, cols=1))
POS.update(zone_grid(["virtus","managem","erg","fsg","usgov"], 51.5, 51.5, 12, 27.5, rows=5, cols=1))

def wrap_label(t):
    return t

def node_size(label):
    lines = label.split("\n")
    w = max(len(l) for l in lines) * 0.135 + 0.55
    h = 0.62 + 0.52*len(lines)
    return w, h

fig, ax = plt.subplots(figsize=(27, 17.5))
ax.set_xlim(0, 54)
ax.set_ylim(0, 34)
ax.axis("off")

# --- фоновые зоны (подписи областей) ---
def zone_bg(x0,x1,y0,y1,label,color):
    ax.add_patch(FancyBboxPatch((x0,y0), x1-x0, y1-y0, boxstyle="round,pad=0.3,rounding_size=0.3",
                 linewidth=1.1, edgecolor=color, facecolor=color, alpha=0.06, zorder=0))
    ax.text(x0+0.3, y1-0.15, label, fontsize=10.5, fontweight="bold", color=color, va="top", zorder=1)

zone_bg(1, 52.6, 30.0, 32.6, "CHINA - COMPANIES & STATE CORPORATIONS", CN_RED)
zone_bg(1, 41.4, 23.1, 26.1, "DRC ASSETS - MINES & METALLURGY", CN_GOLD)
zone_bg(41.6, 44.6, 20.6, 28.6, "ENERGY", GOOD)
zone_bg(1, 25.4, 16.3, 19.0, "DRC GOVERNMENT", DRC_BLUE)
zone_bg(1, 15.4, 9.6, 12.5, "CORRUPTION (Congo Hold-up)", WARN)
zone_bg(16.8, 27.4, 9.6, 12.5, "EASTERN CONFLICT", CN_RED_DARK)
zone_bg(28.8, 37.4, 9.6, 12.5, "EXPORT CORRIDORS", GOOD)
zone_bg(45.2, 53.6, 8.3, 30.3, "WEST / US", "#55606A")

# --- рёбра (рисуем раньше узлов) ---
def draw_edge(a, b, etype, label):
    if a not in POS or b not in POS: return
    x1,y1 = POS[a]; x2,y2 = POS[b]
    st = EDGE_STYLE[etype]
    color = st["color"] or CAT_COLOR.get(NODES[a][1], NEUTRAL)
    if etype == "own" and isinstance(color, str) and color == "#FFFFFF":
        color = NEUTRAL
    dx, dy = x2-x1, y2-y1
    dist = (dx**2+dy**2)**0.5
    rad = 0.05 if dist < 12 else 0.12
    if abs(y1-y2) < 0.01 and abs(x1-x2) > 15:
        rad = 0.18
    arrow = FancyArrowPatch((x1,y1),(x2,y2), arrowstyle="-|>", mutation_scale=9,
                             color=color, linewidth=st["lw"], linestyle=st["ls"],
                             alpha=st["alpha"], connectionstyle=f"arc3,rad={rad}",
                             shrinkA=14, shrinkB=14, zorder=2)
    ax.add_patch(arrow)
    if label:
        mx, my = x1+dx*0.5, y1+dy*0.5
        # небольшое смещение перпендикулярно линии, чтобы не наезжать на неё
        if dist > 0:
            px, py = -dy/dist, dx/dist
        else:
            px, py = 0,0
        mx += px*rad*dist*0.5
        my += py*rad*dist*0.5
        ax.text(mx, my, label, fontsize=st["fs"], color=color, ha="center", va="center",
                zorder=3, bbox=dict(boxstyle="round,pad=0.08", fc="white", ec="none", alpha=0.82))

for a,b,etype,label in EDGES:
    draw_edge(a,b,etype,label)

# --- узлы ---
for nid,(label,cat) in NODES.items():
    if nid not in POS: continue
    x,y = POS[nid]
    w,h = node_size(label)
    fc = CAT_COLOR[cat]
    tc = CAT_TEXT[cat]
    ec = CAT_BORDER.get(cat, "none")
    lw = 1.6 if cat in ("asset","energy") else 0
    box = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.02,rounding_size=0.09",
                          linewidth=lw, edgecolor=ec, facecolor=fc, zorder=4)
    ax.add_patch(box)
    ax.text(x, y, label, ha="center", va="center", fontsize=7.6, fontweight="bold",
            color=tc, zorder=5, linespacing=1.25)

ax.text(27, 33.6, "Relationship map: who is connected to whom in China's DRC presence",
        ha="center", fontsize=21, fontweight="bold", color=INK)

# легенда типов рёбер
legend_items = [
    ("own", "Ownership / stake"), ("deal", "Deal / sale"), ("dispute", "Legal dispute"),
    ("corrupt", "Corruption flow"), ("military", "Arms supplies"),
    ("conflict", "Armed conflict"), ("corridor", "Export corridor"), ("gov", "State regulation"),
]
lx = 1.0
ly = 6.6
for key, lab in legend_items:
    st = EDGE_STYLE[key]
    c = st["color"] or NEUTRAL
    ax.plot([lx, lx+1.15], [ly, ly], color=c, linewidth=st["lw"], linestyle=st["ls"], alpha=st["alpha"])
    ax.text(lx+1.35, ly, lab, fontsize=9.3, va="center", color=INK)
    lx += 1.35 + len(lab)*0.155 + 1.3

ax.set_ylim(-0.5, 34)

source_footer(fig, "Full sources and uncertainty ranges for every link are in SOURCES.md and data/*.json. * Sicomines shares: 68% consortium (Sinohydro + China Railway Group, plus Zhejiang Huayou since 2026).", y=0.005)
save(fig, "17_master_network_graph")
