# Master relationship graph: nodes and edges compiled from every data/*.json file in the repo.
# category controls the node's color and placement zone.

NODES = {
    # --- China: companies and state entities (zone CN) ---
    "cmoc":     ("CMOC Group", "cn"),
    "catl":     ("CATL", "cn"),
    "cnmc":     ("CNMC", "cn"),
    "zijin":    ("Zijin Mining", "cn"),
    "norinco":  ("Norinco\n(Wanbao Mining)", "cn"),
    "sinohydro":("Sinohydro", "cn"),
    "crg":      ("China Railway\nGroup", "cn"),
    "huayou":   ("Zhejiang\nHuayou Cobalt", "cn"),
    "casc":     ("CASC / CATIC", "cn"),
    "ccecc":    ("CCECC", "cn"),
    "cosco":    ("COSCO Shipping", "cn"),

    # --- Assets: mines and metallurgy (zone ASSET) ---
    "sicomines":("Sicomines", "asset"),
    "tfm":      ("Tenke\nFungurume", "asset"),
    "kisanfu":  ("Kisanfu", "asset"),
    "deziwa":   ("Deziwa", "asset"),
    "kambove":  ("Kambove", "asset"),
    "pumpi":    ("Pumpi", "asset"),
    "commus":   ("COMMUS", "asset"),
    "mutanda":  ("Mutanda\n(MUMI)", "asset"),
    "kamoa":    ("Kamoa-Kakula", "asset"),
    "manono":   ("Manono\nLithium", "asset"),
    "mutoshi":  ("Mutoshi", "asset"),
    "smelter":  ("Lualaba Copper\nSmelter", "asset"),

    # --- Energy (zone ENERGY) ---
    "busanga":  ("Busanga Dam", "energy"),
    "zongo2":   ("Zongo II Dam", "energy"),
    "nzilo2":   ("Nzilo II /\n\"Heshima\"", "energy"),

    # --- DRC state (zone DRC) ---
    "gecamines":("Gecamines", "drc"),
    "cominiere":("Cominiere", "drc"),
    "egc":      ("EGC", "drc"),
    "arecoms":  ("ARECOMS", "drc"),
    "snel":     ("SNEL", "drc"),
    "drcgov":   ("DRC\nGovernment", "drc"),
    "fardc":    ("FARDC", "drc"),

    # --- West and others (zone WEST) ---
    "freeport": ("Freeport-\nMcMoRan", "west"),
    "glencore": ("Glencore", "west"),
    "ivanhoe":  ("Ivanhoe Mines", "west"),
    "trafigura":("Trafigura", "west"),
    "avz":      ("AVZ Minerals", "west"),
    "kobold":   ("KoBold Metals", "west"),
    "virtus":   ("Virtus Minerals", "west"),
    "managem":  ("Managem", "west"),
    "erg":      ("ERG", "west"),
    "fsg":      ("Frontier Services\nGroup (E. Prince)", "west"),
    "usgov":    ("US\nGovernment", "west"),

    # --- Corruption (zone CORR) ---
    "ccc":      ("Congo\nConstruction Co.", "corr"),
    "bgfi":     ("BGFIBank", "corr"),
    "kabila":   ("Kabila's\nnetwork", "corr"),

    # --- Military / conflict (zone MIL) ---
    "rwanda":   ("Rwanda (RDF)", "mil"),
    "m23":      ("M23", "mil"),

    # --- Corridors (zone CORRIDOR) ---
    "lobito":   ("Lobito\nCorridor", "corridor"),
    "tazara":   ("TAZARA", "corridor"),
}

# (source, target, type, label)
EDGES = [
    # ownership
    ("sinohydro","sicomines","own","68%*"),
    ("crg","sicomines","own",""),
    ("huayou","sicomines","own","(since 2026)"),
    ("gecamines","sicomines","own","32%"),
    ("cmoc","tfm","own","80%"),
    ("gecamines","tfm","own","20%"),
    ("cmoc","kisanfu","own","71.25%"),
    ("catl","kisanfu","own","23.75%"),
    ("cnmc","deziwa","own","51%"),
    ("gecamines","deziwa","own","49%"),
    ("cnmc","kambove","own","55%"),
    ("gecamines","kambove","own","45%"),
    ("norinco","pumpi","own","75%"),
    ("managem","pumpi","own","20%"),
    ("zijin","commus","own","~70%"),
    ("gecamines","commus","own","~28%"),
    ("glencore","mutanda","own","95%"),
    ("ivanhoe","kamoa","own","39.6%"),
    ("zijin","kamoa","own","39.6%"),
    ("zijin","manono","own","61%"),
    ("cominiere","manono","own","39%"),
    ("cnmc","smelter","own","60%"),
    ("virtus","mutoshi","own","2026"),
    ("cmoc","nzilo2","own",""),
    ("snel","nzilo2","own",""),
    ("sinohydro","busanga","own",""),
    ("sinohydro","zongo2","own",""),
    ("kamoa","smelter","deal","tolling"),

    # deals/history
    ("freeport","cmoc","deal","sold TFM'16,\nKisanfu '20"),
    ("avz","kobold","deal","~$1bn ('25,\nUS-brokered)"),
    ("norinco","mutoshi","deal","lost bid\n$1.4bn ('24)"),

    # disputes
    ("avz","drcgov","dispute","ICSID arbitration"),
    ("avz","cominiere","dispute","ICC award:\n\u20ac39.1m"),

    # corruption
    ("crg","ccc","corrupt",""),
    ("sinohydro","ccc","corrupt",""),
    ("ccc","bgfi","corrupt","$55-65m"),
    ("bgfi","kabila","corrupt","\u2265$138m"),
    ("drcgov","bgfi","corrupt","$94.5m"),
    ("gecamines","bgfi","corrupt","$20m"),

    # military
    ("casc","fardc","military","CH-4 drones"),
    ("norinco","rwanda","military","Sky Dragon 50"),
    ("fsg","drcgov","military","~$700m\ncontract"),
    ("rwanda","m23","military","support (per\nUN reporting)"),
    ("m23","fardc","conflict","conflict"),
    ("drcgov","fardc","gov",""),

    # corridors
    ("trafigura","lobito","corridor","operator"),
    ("kamoa","lobito","corridor","exports"),
    ("ccecc","tazara","corridor","80%"),
    ("zijin","tazara","corridor","5%"),
    ("cmoc","tazara","corridor","5%"),
    ("cosco","tazara","corridor","5%"),

    # state regulation / international
    ("usgov","drcgov","gov","Strategic\nPartnership '25"),
    ("drcgov","arecoms","gov",""),
    ("drcgov","gecamines","gov",""),
    ("drcgov","cominiere","gov",""),
    ("drcgov","egc","gov",""),
    ("drcgov","snel","gov",""),
]
