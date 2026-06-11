# A1 — RICERCA (Lead & Market Intelligence)

> Reparto L2 di 01-AGENCY · Coordinatore: `AG-A1-COORD` (sonnet) · Topologia: `star`
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1

## Cosa fa

Alimenta il funnel con **lead qualificati** e dà a Preventivi (A3) e Delivery (A4)
l'**intelligence di nicchia** per vendere e consegnare meglio. È il primo anello della
pipeline revenue: senza A1, A2 non ha nulla da contattare.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-LEAD-SOURCING` | scraping (Maps/Apify/Outscraper) → estrazione → arricchimento → qualifica → `leads.db` |
| L3 | `WF-MARKET-INTEL` | nicchia/competitor/trend → report per Acquisizione e Preventivi (regole `01_ricerca_no_sito.md`, `02_ricerca_ads_funnel_scarsi.md`, `06_ricerca_ai_prospects.md`) |
| L4 | `T-scraper` | run scraper multi-fonte (maps_browser_scraper, apify_scraper, outscraper_scraper, google_scraper) |
| L4 | `T-extractor` | estrazione contatti/dati dal raw (extractor.py) |
| L4 | `T-qualifier` | scoring lead vs ICP (qualifier.py + regola `03_qualifica_lead.md`) |
| L4 | `T-icp-profiler` | definizione/aggiornamento ICP per nicchia (input da 08 INTELLIGENCE, skill `icp-radar`) |
| L4 | `T-competitor-profiler` | dossier competitor del prospect (competitor.py, cro_audit.py, skill `market-audit`) |

Agenti L5: `AG-A1-COORD` · `AG-A1-SCRAPE-W` · `AG-A1-EXTRACT-W` · `AG-A1-QUAL-W` ·
`AG-A1-ICP-W` · `AG-A1-COMP-W` (schede in `../../Agenti/`).

## Come si collega

| Direzione | Con chi | Cosa passa |
|---|---|---|
| → A2 Acquisizione | intra-BUS | lead qualificati (score ≥ soglia) in `leads.db`, pronti per outreach |
| → A3 Preventivi | intra-BUS | dossier pre-call: profilo lead + audit problema + competitor |
| ← 08 INTELLIGENCE | `HC-IN-AG-01` | ricerca ICP/nicchie/trend con fonti citate |
| ← 09 OPERATIONS | `HC-OP-AG-01` | scheduling run scraper, backup `leads.db` |
| Memoria | `agency/leads` | lead, score, stato funnel (specchio semantico di leads.db, non sostituto) |

Asset esistenti (azione F3): `Outreach/Outreach Workflow/` parte scraping/qualifica = **wrappa**;
`leads.db` = **usa-così** + backup; `Agenti/Agency/sub-agents/` (ai-implementation, cro-funnel,
no-website) = **evolvi** in profili di T-icp-profiler; regole `outreach/rules/01..06` = **usa-così**.

## 🧠 Come si ATTIVA e RAGIONA

**Trigger.**
1. Run schedulata giornaliera (via 09 OPERATIONS) per il sourcing continuo.
2. Richiesta esplicita di A2 ("servono N lead per la nicchia X") o di A3 ("dossier pre-call per il lead Y").
3. KPI in calo (% qualifica scende per 2 cicli) → richiesta intelligence a 08 o organico a FORGE.

**Decomposizione.** `AG-A1-COORD` riceve il task e lo spacchetta in fan-out `star`:
- nicchia nuova? → prima `T-icp-profiler` (non si scrappa senza ICP esplicito);
- ICP esistente? → `T-scraper` in parallelo sulle fonti (Maps, Apify, Outscraper, Google),
  poi `T-extractor` sul raw, poi `T-qualifier` in serie;
- richiesta pre-call? → `T-competitor-profiler` + estratto da `agency/leads`.

**Esecuzione.** Ogni worker opera con dry-run disponibile (stima volumi senza run reale).
`T-qualifier` applica lo scoring di `qualifier.py` contro l'ICP corrente: score ≥ soglia →
lead promosso in `leads.db` con tag nicchia/fonte; sotto soglia → scartato CON motivo
(il motivo alimenta `agency/reasoning`). `memory_search` su `agency/leads` prima di ogni
inserimento per dedup.

**Handoff.** Lead qualificati → A2 via stato in `leads.db` + evento `lead_generated` in metrics.
Dossier pre-call → A3 come handoff intra con acceptance criteria ("profilo + problema quantificato
+ 3 competitor"). Report nicchia → A2/A3 in `WF-MARKET-INTEL`.

**Failure.**
- Fonte scraper down/bloccata → retry con backoff, poi switch fonte alternativa, poi alert a 09 OPS.
- % qualifica < baseline per 2 cicli → AG-A1-COORD apre `HC-AG-IN-01`/`HC-AG-FG-01` (ICP da rivedere o skill mancante).
- Dati stantii (freschezza KPI fuori soglia) → re-run sourcing prioritario sulla nicchia interessata.
- Ogni fallimento distillato in `agency/reasoning` (pattern #5).

## KPI

| KPI | Definizione |
|---|---|
| Lead qualificati/gg | n. lead con score ≥ soglia inseriti in leads.db |
| % qualifica su scraped | qualificati / totale raccolti |
| Freschezza dati | età media dei dati lead al momento dell'outreach |

## Connessioni

- `../../Workflow/WF-LEAD-SOURCING/` · `../../Workflow/WF-MARKET-INTEL/`
- `../../Funzioni/T-scraper/` · `../../Funzioni/T-qualifier/` · `../../Funzioni/T-icp-profiler/`
- `../A2-Acquisizione/` (cliente interno primario) · `../A3-Preventivi/` (dossier pre-call)
