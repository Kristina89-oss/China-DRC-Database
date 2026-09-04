# China's Footprint in the DRC: a Database

A structured database and set of infographics on China's presence in the Democratic Republic of the Congo's mining, energy, corruption, and military dimensions. All figures are checked against open sources as of **August 2026**; the verification status of every section is in [`SOURCES.md`](./SOURCES.md).

---

## Key Findings

**1. The real chokepoint isn't the mines - it's the refineries.** The DRC supplies ~74% of world cobalt output, but refines less than 5% of it domestically. China controls 70-80% of world cobalt refining capacity. Ownership of the mines is visible and gets all the attention; control of processing is invisible and is where the real leverage sits. ([chart](charts/10_value_chain_chokepoint.png))

**2. China's presence runs through one bank, not just the mines.** The "Congo Hold-up" investigation traced how China Railway Group and Sinohydro - the very companies behind the flagship Sicomines deal - moved $55-65m through a shell company into BGFIBank DRC, a bank run by former president Joseph Kabila's brother. State funds from the Central Bank and Gecamines flowed through the same bank. The result: two decades of political untouchability for the Sicomines contract. ([chart](charts/08_corruption_money_flow.png) · [data](data/corruption_network.json))

**3. The DRC has shifted from object to regulator.** Since 2025, Kinshasa has moved from a cobalt export ban, to an export quota system (96,600 t/year), to an outright ban on exporting copper/cobalt *concentrates* (June 2026) - attacking the processing stage directly rather than just trading in volumes. Prices are up 160% since the ban began. ([chart](charts/02_cobalt_price_trend.png))

**4. Nobody involved is anonymous.** This database names 51 companies and institutions and 21 individuals - ambassadors, CEOs, ministers, and the people who moved the money - and maps exactly how they connect. One CMOC executive personally chaired both a Sicomines-era hydropower company and a China Railway Group subsidiary before rising to his current post. A former DRC prime minister who signed the original 2008 deal is now the government's most prominent critic of it. ([network graph](charts/17_master_network_graph.png) · [people map](charts/18_people_network.png))

**5. China's military footprint is smaller than you'd expect - and it isn't the PLA.** Security for Chinese-linked mines relies on licensed-but-state-controlled private security companies (DeWe Security, Huaxin Zhong An) - and, on at least one documented occasion, on the DRC's own army (FARDC) hired to guard a Chinese gold concession. China supplies drones to the DRC army and air-defense systems to Rwanda simultaneously. In May 2026, Beijing and Kinshasa signed a *police* (not military) cooperation agreement - the clearest sign of where this is actually heading. ([chart](charts/19_china_security_presence.png))

**6. There are two unrelated "Chinas" operating in the country.** Organized state corporations run the copper-cobalt belt in the south under contract. In the east, hundreds of small, often-illegal Chinese gold operators work outside the law - so much so that China's own foreign ministry has publicly ordered some of them to leave. ([chart](charts/14_two_chinas_comparison.png))

**7. The US-DRC minerals deal is no longer hypothetical.** What began as a 2025 proposal is now a signed Strategic Partnership Agreement (December 2025), already producing real transactions (Virtus Minerals' April 2026 deal for the Mutoshi deposit) and already facing a constitutional challenge in Kinshasa. ([data](data/us_counterstrategy.json))

**8. The trade relationship is a closed loop.** In one snapshot month, the DRC exported $2.28bn in raw and semi-processed copper to China and imported back $663m in batteries, transformers, and wire - made from that same metal, with someone else's value added. ([chart](charts/13_trade_closed_loop.png))

**9. On the ground, the picture is more mixed than "hegemony" suggests.** Displaced Kolwezi residents describe $7,500 compensation for a demolished house as unlivable; a mother whose neighbors were filmed being whipped on a Chinese mine manager's orders says she's already gone to court. Yet continent-wide polling (Afrobarometer) finds roughly 60-66% of Africans still rate China's overall influence as positive - a reminder that grievance and goodwill coexist. ([testimony](charts/20_public_sentiment_wall.png))

**10. There's no "Chinese zone" on the map - ownership is interleaved, not clustered.** Mapped against 145 real concessions in the belt (OpenStreetMap, not hand-picked), a spatial statistics test found Chinese-linked mines are *not* geographically clustered together - every one of the seven confidently-attributed China-linked concessions has at least one non-Chinese neighbor (Glencore, ERG, Gecamines, or the US-controlled Etoile mine) among its three nearest sites. Ownership concentration in this belt is corporate, not territorial. ([data](data/spatial_clustering_test.json))

---

## Consolidated Report (PDF)

Every chart in this repository in a single document - with a short caption under each, a glossary of 30+ companies (who's Chinese, who's DRC state, who's Western), and two orientation maps. Easier to read straight through than opening 19 separate PNGs.

**[\u2192 REPORT.pdf](./REPORT.pdf)**

## Who's Connected to Whom: the Relationship Map

One graph, 51 nodes and 57 edges, ties together ownership, deals, corruption flows, arms supplies, legal disputes, and export corridors from every section below. Line color and style encode the relationship type (legend is on the chart itself).

![Relationship map](charts/17_master_network_graph.png)

*Full resolution is in `charts/17_master_network_graph.png` (5400\u00d73500 px) if you want to zoom into any part of it. Uncertainty ranges for the dollar amounts are, as throughout this database, in SOURCES.md.*

## Who's Who: the People

Companies and state bodies are an abstraction. The people who negotiate and take the bribes are not. Below are 21 figures on both sides: their role, their influence, and their scandals (rumors and allegations are flagged separately from confirmed facts).

![People on both sides](charts/18_people_network.png)

Full dossiers (with a verification status for each) are in [`data/key_people.json`](data/key_people.json).

## Military Presence: Who Actually Guards the Assets

The answer is shorter than you'd expect: not the PLA. China keeps fewer formal troops in the DRC than private security contractors - and part of the security burden in the east is simply outsourced to the DRC's own army for a fee.

![Guarding China's assets](charts/19_china_security_presence.png)

Company-by-company and incident-by-incident detail is in [`data/china_security_presence.json`](data/china_security_presence.json).

## What Residents Themselves Say

Everything above is corporate filings, government data, and journalism. This section is different: named,
on-the-record voices of Congolese residents, civil-society groups, and officials, gathered from local news
coverage and NGO field reports (a live public "forum" specific to this topic barely exists in searchable
form, so journalist-mediated testimony is the closest available proxy). Read with the caveat that this is
qualitative and anecdotal, not verified fact about events.

![What residents say](charts/20_public_sentiment_wall.png)

Full quotes, sourcing, and the methodology caveat are in [`data/public_sentiment.json`](data/public_sentiment.json).

---

## Timeline, 2008-2026

![Timeline](charts/01_timeline_2008_2026.png)

**Key observation:** events sharply accelerate after 2023 - this isn't a gradual process, it's an accelerating pushback by DRC and US regulators against a Chinese expansion model that had been settled for over a decade.

## Cobalt Market: Dumping and Protectionism

![Cobalt price, 2022-2026](charts/02_cobalt_price_trend.png)
![Export quota, 2026-2027](charts/07_cobalt_quota_breakdown.png)

### The Export-Control Escalation Ladder

| Date | Measure |
|---|---|
| 22 Feb 2025 | Full cobalt export ban (ARECOMS Decision No. 001/2025) |
| Jun / Sep 2025 | Two extensions of the ban |
| 16 Oct 2025 | Quotas: 18,125 t for the rest of 2025; **96,600 t/year** for 2026-2027 |
| Dec 2025 | 10% royalty prepayment within 48 hours, pre-shipment compliance certificate |
| 29 Jun 2026 | Unused H1-2026 quotas moved into the strategic reserve |
| 29 Jun 2026 | **Ban on copper and cobalt concentrate exports** + a 55%-coefficient tax on by-products |

A direct parallel to Indonesia, which banned nickel-ore exports in 2020. The DRC's constraint remains the same as before: actual exports run at only 33-50% of allocated quotas because of customs and logistics failures.

## Sicomines: Anatomy of the Deal of the Century

![Infrastructure vs. profit](charts/03_sicomines_investment_vs_profit.png)

| Parameter | Value |
|---|---|
| China consortium's share | 68% (Sinohydro, China Railway) |
| Gecamines' (DRC) share | 32% |
| Infrastructure built by 2023 | $822m |
| China's profit extracted by 2023 | ~$10bn |
| New 2024-2040 commitment | $7bn (if Cu > $8,000/t, zero if \u2264 $5,200/t) |
| New comprehensive audit | launched March 2026, covering 2008-2024 |

## Who Owns the Mines

![Ownership by project](charts/04_ownership_by_project.png)
![Production by project](charts/05_production_by_project.png)

## Energy: Dams Built for the Mines

![Hydropower cascade](charts/06_hydropower_cascade.png)

## The Real Chokepoint in the Market

![Extraction vs. refining](charts/10_value_chain_chokepoint.png)

## Export Corridors

![Lobito vs. TAZARA](charts/11_transport_corridors.png)

## Corruption: the Congo Hold-up Case

![Money-flow diagram](charts/08_corruption_money_flow.png)

## Military Dimension

![Dual diplomacy](charts/09_security_actors.png)

## The Human-Rights Track

![Allegations against Chinese projects](charts/12_human_rights_allegations.png)

## Trade and the "Two Chinas"

![Closed trade loop](charts/13_trade_closed_loop.png)
![Katanga vs. South Kivu](charts/14_two_chinas_comparison.png)

### Artisanal Mining: EGC Finally Gets Moving

After five years of dormancy, the state monopoly **Entreprise Generale du Cobalt** shipped its first traceable batch - 1,000 t - in November 2025, and in 2026 became the first Congolese company to export via the Lobito corridor (~3,000 t in H1 2026, using 100% of its quota - well above the roughly 60% national average). Problems remain: at the Mutoshi pilot site, the number of artisanal miners grew almost fivefold after formalization collapsed in 2021; AFREWATCH continues to document collapses at unregulated sites.

### Kolwezi's Environment: the 2026 Scientific Evidence

A joint study by RAID, AFREWATCH, Source International, and the University of Lubumbashi (June 2026, 8 communities near Kolwezi and Fungurume) found WHO particulate-matter limits exceeded at **every single** measurement point, and a well 200m from a tailings dam that was 100 times more acidic than recommended, with manganese and aluminum up to 14 times over health limits. The mines involved: TFM (CMOC), COMMUS (Zijin), and Mutanda (Glencore). CMOC and Glencore responded substantively; Zijin/COMMUS did not.

## A Spatial Test: Do Chinese-Linked Concessions Cluster Geographically?

The concessions named above (TFM, Kisanfu, Deziwa, COMMUS...) get all the attention, but they sit inside a much larger, mostly-unnamed mining landscape - 171 real quarry/pit polygons mapped in OpenStreetMap across the Lualaba/Haut-Katanga belt. Worth checking rather than assuming: does Chinese ownership concentrate in one part of the belt, or is it spread through it?

OSM tags individual pits, not concession boundaries - TFM alone (one 1,600 sq km concession) is split across 23 separate OSM polygons. Dissolving same-concession pits into single units brings the raw 171 polygons down to **145 real, distinct concessions**. Of those, ownership research (company reports, Wikipedia, Global Witness, mindat.org, the TFM 2014 technical report) could confidently attribute only **15** - 7 China-linked (TFM/CMOC, Kisanfu/CMOC+CATL, Deziwa/CNMC, COMMUS/Zijin, Kalongwe/Chengtun, Ruashi/Jinchuan, Shituru/Pengxin), 1 joint venture (Kamoa-Kakula: Ivanhoe/Canada + Zijin/China, 39.6% each), 7 non-Chinese (Mutanda, Kansuki, Tilwezembe - all Glencore; Kakanda - ERG/Kazakhstan; Kamatanda, Shinkolobwe - Gecamines/DRC state; L'Etoile du Congo - Chemaf/Virtus, US).

A spatial join-count test (`libpysal` + `esda`, k-nearest-neighbor weights, 999 permutations) on those 15 units found **no clustering**: observed China-China neighbor pairs (4.5) came in *below* the number expected under pure spatial randomness (6.0), p = 0.955. Every China-linked concession's nearest neighbors include a non-Chinese operator. Full attribution table, sources, and the sensitivity check (excluding the joint venture) are in [`data/spatial_clustering_test.json`](data/spatial_clustering_test.json).

**Caveat:** only 15 of 145 mapped concessions have a confirmed operator in this dataset - this describes the well-documented majors, not the full mining landscape, and the small labeled sample limits statistical power regardless of the true pattern.

---

## Repository Structure

```
├── README.md                       - this file
├── SOURCES.md                      - full source list + verification status for every claim
├── REPORT.pdf                      - the consolidated report
├── charts/                         - 19 infographics (PNG, 200dpi)
├── data/                           - structured data (JSON)
│   ├── sicomines.json              - the RFI deal: terms, audits, Amendment 5
│   ├── mining_projects.json        - 7 projects: ownership, investment, production
│   ├── cobalt_market.json          - 2022-2026 prices, ARECOMS export quotas
│   ├── energy_hydropower.json      - the Lualaba dam cascade + Grand Inga
│   ├── corruption_network.json     - nodes and amounts in the Congo Hold-up scheme
│   ├── military_dimension.json     - arms supplies, PMCs/PSCs
│   ├── us_counterstrategy.json     - minerals-for-security, Manono, KoBold
│   ├── value_chain_control.json    - extraction vs. refining: where the chokepoint is
│   ├── export_controls_2026.json   - the concentrate ban, the escalation ladder
│   ├── transport_corridors.json    - Lobito vs. TAZARA
│   ├── human_rights_legal.json     - BHRC data, the Zijin Withhold Release Order
│   ├── two_chinas_east.json        - illegal Chinese gold mining in South Kivu
│   ├── environment_health.json     - the scientific pollution evidence near Kolwezi
│   ├── trade_dependency.json       - DRC-China trade volume, the closed loop
│   ├── artisanal_mining_egc.json   - EGC and formalizing artisanal mining
│   ├── key_people.json             - 21 individuals: China and DRC, roles, scandals, influence
│   ├── china_security_presence.json - Chinese PSCs, scale, incidents
│   ├── public_sentiment.json       - named resident/civil-society testimony, Afrobarometer polling
│   ├── timeline.json               - 34 events, machine-readable
│   └── spatial_clustering_test.json - 145-concession spatial test: do China-linked mines cluster?
└── scripts/
    ├── style.py                    - shared chart styling
    ├── graph_data.py               - nodes/edges for the relationship graph
    └── chart_0X_*.py               - generation code for every chart (matplotlib)
```

## How to Use This

- **Regenerate a chart**: `pip install matplotlib && python3 scripts/chart_0X_name.py`
- **Pull the raw data**: any file in `data/*.json` loads directly (`pandas.read_json`, `jq`, etc.)
- **Check a claim**: look for the `"sources"` / `"verification_status"` field inside the relevant JSON, or the table in `SOURCES.md`

## Important Caveats

- Per-mine production figures (except CMOC's 2025 combined totals) are a **2022-2023 snapshot** from corporate reporting; more recent per-project figures are fragmented in public sources.
- Several Congo Hold-up dollar amounts **vary between primary reports** ($55-65m for one branch of the scheme) - ranges are given rather than a single figure.
- The claim that Rwanda's Sky Dragon 50 systems intercept DRC's CH-4 drones rests on DRC intelligence reporting and has no independent confirmation.
- Original analytical judgments (as opposed to facts) from the three source reports this project began from are labeled as such and not presented as verified data.

## License

Data and code are provided as-is for research purposes, with attribution. Verify primary sources before using this in publications.
