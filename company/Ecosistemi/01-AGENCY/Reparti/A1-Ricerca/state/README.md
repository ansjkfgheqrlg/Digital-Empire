---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #ricerca #lead #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# State — A1 Ricerca & Market Intelligence

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto. Namespace: `agency/a1` (+ `agency/leads`).

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Leads | `agency/leads` | Lead, score, fonte, stato funnel (specchio semantico di leads.db) | AG-A1-EXTRACT, AG-A1-QUAL | AG-A1-QA, AG-A1-BRIEF, A2 |
| Sourcing | `agency/a1/sourcing` | Run sourcing: fonte, n. raw, n. qualificati, errori, gate | AG-A1-SCRAPE, AG-A1-COORD | AG-A1-QA, AG-DIR |
| ICP | `agency/a1/icp` | Profili ICP per nicchia (con fonti citate) | AG-A1-ICP | AG-A1-QUAL, 08-INTELLIGENCE |
| Intel | `agency/a1/intel` | Report nicchia: trend, competitor_top3, opportunità, fonti | AG-A1-INTEL | A2, A3, 08-INTELLIGENCE |
| Dossier | `agency/a1/dossier` | Dossier pre-call per discovery (A8) | AG-A1-BRIEF | A8-Closing, A3 |
| Reasoning | `agency/reasoning` | Motivi scarto lead, failure distillati (pattern) | AG-A1-COORD, AG-A1-QUAL | tutto il reparto |

---

## Struttura file di stato

### Sourcing run state (`agency/a1/sourcing/{run_id}/state.json`)

```json
{
  "run_id": "RUN-001",
  "nicchia": "ristorazione-roma",
  "icp_ref": "agency/a1/icp/ristorazione-roma",
  "data_avvio": "YYYY-MM-DD",
  "fonti": [
    {"fonte": "maps", "n_raw": 0, "stato": "completata | in_corso | errore"},
    {"fonte": "apify", "n_raw": 0, "stato": "completata"},
    {"fonte": "outscraper", "n_raw": 0, "stato": "completata"},
    {"fonte": "google", "n_raw": 0, "stato": "completata"}
  ],
  "n_estratti": 0,
  "n_qualificati": 0,
  "n_scartati": 0,
  "errori": [],
  "gate_qa": "pending | PASS | FAIL",
  "gate_qa_motivo": "optional — dettaglio se FAIL",
  "stato_finale": "in_progress | store_completo | archiviato",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Lead record (`agency/leads/{lead_id}.json`)

```json
{
  "lead_id": "LEAD-0001",
  "nicchia": "ristorazione-roma",
  "fonte": "maps",
  "nome": "...",
  "email": "...",
  "telefono": "...",
  "sito": "https://...",
  "settore": "...",
  "score": 0,
  "stato_funnel": "qualificato | nurture | scartato",
  "motivo_scarto": "optional — se scartato",
  "data_scraping": "YYYY-MM-DD",
  "gdpr_light": true,
  "dedup_check": true
}
```

### Intel report (`agency/a1/intel/{report_id}.json`)

```json
{
  "report_id": "INTEL-001",
  "nicchia": "ristorazione-roma",
  "data": "YYYY-MM-DD",
  "trend": "descrizione segnale qualitativo",
  "competitor_top3": ["...", "...", "..."],
  "icp_aggiornato": "agency/a1/icp/ristorazione-roma",
  "opportunita": "...",
  "fonti": ["https://...", "dataset:...", "skill:market-audit"],
  "ingest_08_intelligence": true
}
```

### Dossier pre-call (`agency/a1/dossier/{dossier_id}.json`)

```json
{
  "dossier_id": "DOSS-001",
  "lead_id": "LEAD-0001",
  "call_prevista": "YYYY-MM-DDTHH:MM:SSZ",
  "profilo_lead": "score + stato funnel + dati chiave",
  "audit_problema": "output competitor.py + cro_audit.py + market-audit",
  "competitor": ["...", "...", "..."],
  "icp_match": "agency/a1/icp/...",
  "contesto_nicchia": "estratto da agency/a1/intel",
  "campi_vuoti": [],
  "consegnato_a8": "YYYY-MM-DDTHH:MM:SSZ",
  "sla_2h_rispettata": true
}
```

---

## Regole di integrità dei namespace

1. **Lead senza `score` o `fonte`** — un lead in `agency/leads` deve avere `score` e `fonte`
   popolati. Senza, non è un lead chiuso. AG-A1-QUAL è responsabile.

2. **Lead scartato senza `motivo_scarto`** — un lead con `stato_funnel: "scartato"` deve avere
   `motivo_scarto` (R7). Il motivo va anche in `agency/reasoning`.

3. **Report intel senza `fonti[]`** — un report in `agency/a1/intel` con `fonti[]` vuoto non
   può essere ingestato in 08-INTELLIGENCE (R4). AG-A1-QA è responsabile.

4. **Dossier con `campi_vuoti` non vuoto** — un dossier con campi vuoti non può avere
   `consegnato_a8` valorizzato (R6/P6). AG-A1-BRIEF dichiara [DM] + motivo, non lascia vuoto.

5. **Ripartibilità a freddo** — ogni `state.json` ha `last_updated` e `stato` per fonte. Una
   run interrotta riprende dall'ultima fonte completata senza riscrappare tutto.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Sourcing state | Step 1 WF-LEAD-SOURCING | Ad ogni fonte / step | Dopo `store_completo`; non eliminato |
| Lead record | Step EXTRACT WF-LEAD-SOURCING | A qualifica e a cambio stato funnel | Persistente in leads.db; mai eliminato |
| Intel report | Step finale WF-MARKET-INTEL | Non aggiornato dopo ingest | Archiviato; linkato a 08-INTELLIGENCE |
| Dossier pre-call | Step 1 WF-BRIEF-PRE-CALL | Fino a consegna ad A8 | Archiviato dopo la call; non eliminato |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §6-7` — namespace e ripartibilità
- [[WF-LEAD-SOURCING]] · `workflow/WF-LEAD-SOURCING.md` — produce sourcing state + lead record
- [[WF-MARKET-INTEL]] · `workflow/WF-MARKET-INTEL.md` — produce intel report
- [[WF-BRIEF-PRE-CALL]] · `workflow/WF-BRIEF-PRE-CALL.md` — produce dossier pre-call
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
