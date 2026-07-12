---
Type: REPARTO
Status: Active
Tags: #reparto #agency #ricerca #lead #icp #market-intelligence #A1
Created: 2026-07-11
Last updated: 2026-07-11
---

# A1 — Ricerca & Market Intelligence

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
> **Standard:** CF-grade (ADR-007) · **Topologia:** `star` — 1 coordinatore, 7 worker, 1 verificatore bloccante

---

## Missione

Alimentare il funnel di 01-AGENCY con **lead qualificati** e fornire ai reparti a valle
l'**intelligence di nicchia** necessaria per vendere e consegnare meglio.

A1 è il primo anello della pipeline revenue: senza A1, A2-Acquisizione non ha nessuno da
contattare, A3-Preventivi non ha audit del problema e A8-Closing arriva in discovery call
senza dossier. Il reparto non riscrive lo scraper runtime esistente: lo **wrappa** e lo
orchestra (ADR-003 WRAP-not-rewrite) — `Outreach/Outreach Workflow/`, `extractor.py`,
`qualifier.py`, `competitor.py`, `cro_audit.py`.

---

## Roster del reparto (9 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A1-COORD` | Coordinatore Ricerca | `agenti/ag-a1-coord.md` | coordinator | sonnet | Decide priorità nicchie, fan-out `star`, riporta ad AG-DIR |
| `AG-A1-SCRAPE` | Runner Scraper | `agenti/ag-a1-scrape.md` | worker | haiku | Esegue le fonti in parallelo: Maps · Apify · Outscraper · Google |
| `AG-A1-EXTRACT` | Estrattore | `agenti/ag-a1-extract.md` | worker | haiku | Raw HTML/JSON → schede lead strutturate (wrappa `extractor.py`) |
| `AG-A1-QUAL` | Qualificatore ICP | `agenti/ag-a1-qual.md` | worker | sonnet | Score lead vs ICP corrente + triage (wrappa `qualifier.py`) |
| `AG-A1-ICP` | ICP Profiler | `agenti/ag-a1-icp.md` | worker | sonnet | Crea/aggiorna i profili ICP per nicchia (skill `icp-radar`) |
| `AG-A1-COMP` | Analista Competitor & Audit | `agenti/ag-a1-comp.md` | worker | sonnet | Dossier competitor + audit problema (`competitor.py`, `cro_audit.py`) |
| `AG-A1-INTEL` | Analista di Mercato | `agenti/ag-a1-intel.md` | worker | sonnet | Trend di nicchia; sourcing da 08-INTELLIGENCE |
| `AG-A1-BRIEF` | Brief Pre-Call | `agenti/ag-a1-brief.md` | worker | sonnet | Aggrega il dossier per la discovery call di A8-Closing |
| `AG-A1-QA` | Verificatore Dati | `agenti/ag-a1-qa.md` | verifier | sonnet | Valida score, freschezza, GDPR-light; **bloccante** su ogni output |

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-LEAD-SOURCING** | `workflow/WF-LEAD-SOURCING.md` | Dalla nicchia al lead qualificato in `leads.db`: scraping multi-fonte → estrazione → qualifica ICP | G-SOURCING (AG-A1-QA): completezza dati ≥80%, no duplicati, GDPR-light |
| **WF-MARKET-INTEL** | `workflow/WF-MARKET-INTEL.md` | Report di nicchia: trend, competitor top3, ICP aggiornato, opportunità | G-INTEL (AG-A1-QA): fonti citate e verificabili; nessuna metrica inventata |
| **WF-BRIEF-PRE-CALL** | `workflow/WF-BRIEF-PRE-CALL.md` | Dossier pre-call per A8: lead score + audit problema + ICP match + contesto nicchia | G-BRIEF (AG-A1-QA): nessun campo vuoto; consegna ≥2h prima della call |

---

## Skill del reparto

| Skill | Stato | Owner agente |
|---|---|---|
| `icp-radar` | esistente, mappata (WRAPPA) | AG-A1-ICP — profili ICP con fonti citate |
| `market-audit` | esistente, mappata (WRAPPA) | AG-A1-COMP — audit marketing del prospect |
| `competitor-profiling` | esistente, mappata (WRAPPA) | AG-A1-COMP — dossier competitor strutturato |
| `market-competitors` · `customer-research` | esistenti, ausiliarie | AG-A1-COMP · AG-A1-ICP |

Dettaglio e regola anti-contraddizione → `skills/SKILLS.md`.

---

## KPI del reparto

| KPI | Owner | Definizione | Baseline |
|---|---|---|---|
| Lead qualificati/gg | AG-A1-QUAL | Lead con score ≥ soglia inseriti in `leads.db` al giorno | [DM] |
| % qualifica su scraped | AG-A1-QUAL | Lead qualificati / totale raccolti per run | [DM] |
| Dossier pre-call entro SLA | AG-A1-BRIEF | % dossier consegnati ad A8 ≥2h prima della call | [DM] — target 100% |
| Report con fonti verificabili | AG-A1-INTEL | % report con campo `fonti[]` non vuoto e link verificabili | [DM] — target 100% |
| Gate bypass rate | AG-A1-QA | Output consegnati senza gate QA / tot output | Target 0 (Mandato Art.4.1) |

Dettaglio completo → `kpi/KPI.md`.

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | 09-OPERATIONS | Trigger della run di sourcing schedulata + backup `leads.db` |
| ← riceve da | A2-Acquisizione | Richiesta lead su nicchia specifica (funnel in esaurimento) |
| ← riceve da | 08-INTELLIGENCE | Segnali di mercato e trend come sorgente per AG-A1-INTEL |
| → consegna a | A2-Acquisizione | Lead qualificati in `leads.db` + `agency/leads` (con `score` e `fonte`) |
| → consegna a | A3-Preventivi | Audit problema + dossier competitor per costruire l'offerta |
| → consegna a | A8-Closing | Brief pre-call completo, ≥2h prima della discovery call |
| → consegna a | 08-INTELLIGENCE | Report di nicchia per ingest (trend, competitor top3, ICP) |

---

## Gate del reparto

**Presidio unico: AG-A1-QA — bloccante, senza deroga per urgenza.**

| Gate | Workflow | Blocca se |
|---|---|---|
| G-SOURCING | WF-LEAD-SOURCING | Completezza dati <80%, duplicati in `leads.db`, violazione GDPR-light |
| G-INTEL | WF-MARKET-INTEL | Metrica senza fonte citata o fonte non verificabile (Mandato Art.2) |
| G-BRIEF | WF-BRIEF-PRE-CALL | Campi "da compilare" vuoti o dossier fuori SLA |
| G-ICP | WF-MARKET-INTEL | Scraping di nicchia nuova avviato senza profilo ICP esplicito |

Un lead incompleto, un report con metrica inventata, un dossier con campi vuoti = FAIL.
**Escalation ad AG-DIR, mai bypass.**

---

## Namespace AgentDB

**Chiave canonica: `agency/a1`** (+ `agency/leads`, condiviso con A2) — fonte di verità: `../../NAMESPACE.md`.

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/leads` | Lead, score, stato funnel (specchio semantico di `leads.db`) | AG-A1-EXTRACT, AG-A1-QUAL |
| `agency/a1/sourcing` | Run di sourcing: fonte, n. raw, n. qualificati, errori | AG-A1-SCRAPE, AG-A1-COORD |
| `agency/a1/icp` | Profili ICP per nicchia (con fonti citate) | AG-A1-ICP |
| `agency/a1/intel` | Report nicchia: trend, competitor_top3, opportunità | AG-A1-INTEL |
| `agency/a1/dossier` | Dossier pre-call per la discovery di A8 | AG-A1-BRIEF |

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`
- Stato e ripartibilità a freddo → `state/README.md`

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — forma, gerarchia, flussi, gate, namespace
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
- [[ag-a1-qa]] · `agenti/ag-a1-qa.md` — verificatore bloccante del reparto
- [[WF-LEAD-SOURCING]] · `workflow/WF-LEAD-SOURCING.md`
- [[WF-BRIEF-PRE-CALL]] · `workflow/WF-BRIEF-PRE-CALL.md`
- [[A2-Acquisizione]] · destinatario dei lead qualificati
- [[A8-Closing]] · destinatario del brief pre-call
