---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #strategia #backlog #IB-L2-STRA
Created: 2026-06-21
Last updated: 2026-06-21
---

# State — IB-L2-STRA Strategia & Intelligence

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto.

---

## Namespace memoria del reparto

AgentDB root: `infobusiness/strategia/`

| Namespace | Path file-system | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Backlog | `backlog/idee.json` + `backlog/archivio/` | Coda idee con score /100, stato, priorità, fonti; archivio idee scartate | IB-STRA-BACKLOG | IB-COORD-STRATEGIA, IB-STRA-QA, IB-STRA-ROADMAP |
| Intelligence | `intelligence/state.json` + `trend_YYYYMM.md` + `fonti.json` | Stato WF-PRODUCT-INTELLIGENCE, report trend mensile, registro fonti | IB-STRA-INTEL | IB-STRA-COMP, IB-STRA-BACKLOG, IB-STRA-QA |
| Competitor | `competitor/{competitor_id}_dossier_YYYYMMDD.md` | Audit offerta competitor (prodotti, prezzi, posizionamento) con fonte+data | IB-STRA-COMP | IB-COORD-STRATEGIA, IB-STRA-BACKLOG |
| ICP | `icp/icp_infobusiness.md` + `icp_changelog.md` | Profilo ICP info-business corrente (≠ ICP AGENCY) + storico revisioni | IB-STRA-ICP | tutti gli specialisti |
| Roadmap | `roadmap/roadmap_corrente.md` + `roadmap_archivio/` | Roadmap prodotti 6-12 mesi approvata + versioni precedenti | IB-STRA-ROADMAP | IB-COORD-STRATEGIA, IB-L2-LANC |

---

## Struttura file di stato

### Backlog (`infobusiness/strategia/backlog/idee.json`)

```json
{
  "idee": [
    {
      "idea_id": "IDEA-012",
      "titolo": "Mini-corso 'Claude Code per consulenti'",
      "formato": "mini-corso | ebook | comunità | template-pack",
      "ruolo": "lead_magnet | pagamento | cross-sell_AGENCY",
      "score": 82,
      "score_breakdown": {"domanda": 18, "gap": 18, "fit_icp": 17, "fattibilita": 16, "revenue": 13},
      "soglia": "priorita_alta",
      "fonti": ["trend_202606.md", "dossier_competitor_202606.md", "community_log_47richieste"],
      "icp_target": "consulente IT freelance",
      "lead_time_stimato": "[stima] 3 settimane",
      "stato": "idea | parcheggiata | in-validazione | validato | in-produzione | live",
      "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
    }
  ]
}
```

### Intelligence (`infobusiness/strategia/intelligence/state.json`)

```json
{
  "workflow": "WF-PRODUCT-INTELLIGENCE",
  "ultimo_run": "2026-06",
  "trigger_ultimo_run": "ciclo_mensile | evento_mercato",
  "temi_attivi": [
    {"tema": "AI operativa no-code per micro-business", "forza_segnale": "alta", "fonti": ["url+data"]}
  ],
  "fonti_registrate": 12,
  "idee_generate_ultimo_run": 4,
  "qa_gate": "pending | PASS | FAIL",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Roadmap (`infobusiness/strategia/roadmap/roadmap_corrente.md` — front-matter di stato)

```json
{
  "roadmap_id": "ROADMAP-2026Q3",
  "orizzonte_mesi": 12,
  "prodotti": [
    {"prodotto": "Mini-corso consulenti", "idea_id": "IDEA-012", "lead_time_gg": 21,
     "data_lancio_pianificata": "2026-09-01", "buffer_da_precedente_gg": 35, "stato": "pianificato"}
  ],
  "buffer_min_gg": 30,
  "icp_check": "PASS | FAIL",
  "qa_gate": "pending | PASS | FAIL",
  "approvato_da_director": false,
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Regole di integrità dei namespace

1. **Idea senza `fonti`** — un'idea con `score >0` ma `fonti: []` è invalida. Lo score senza fonte
   non è candidabile (R1 + R3). IB-STRA-QA blocca; IB-STRA-BACKLOG è responsabile.

2. **Idea con `stato: in-validazione`** — deve avere `score ≥60` **e** `qa_gate: PASS` registrato.
   Nessuna idea raggiunge `in-validazione` senza handoff HC-STRA-PROD-01 datato.

3. **Roadmap senza lead time o buffer** — una roadmap con `approvato_da_director: true` deve avere
   `lead_time_gg` per ogni prodotto e nessun `buffer_da_precedente_gg < 30`. IB-STRA-ROADMAP è responsabile.

4. **Dato senza provenienza** — ogni voce in `fonti.json` ha `url` + `data_rilevazione`. Un dato
   referenziato da un'idea ma assente in `fonti.json` è un'anomalia bloccante in G-FONTI.

5. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che riprende un
   workflow interrotto legge `intelligence/state.json` o il front-matter roadmap per sapere a quale
   step riprendere. Lo state deve rispecchiare esattamente il punto attuale del workflow.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Idea (backlog) | Step [4] WF-PRODUCT-INTELLIGENCE | Ad ogni ri-scoring o cambio stato | Idea <40 → `backlog/archivio/`; idea live → resta con stato `live` |
| Intelligence state | Primo run WF-PRODUCT-INTELLIGENCE | Ad ogni step del ciclo mensile | Non eliminato; `trend_YYYYMM.md` storicizzato per mese |
| Dossier competitor | Step [2] WF-PRODUCT-INTELLIGENCE | Nuovo file datato per ogni audit | Versioni datate conservate (tracciamento evoluzione offerta) |
| ICP | Aggiornamento trimestrale o evento | Step [3] WF-PRODUCT-INTELLIGENCE | Revisioni tracciate in `icp_changelog.md` |
| Roadmap | Step iniziale WF-ROADMAP-PRODOTTI | Dopo ogni lancio + ciclo trimestrale | Versione precedente → `roadmap_archivio/` (deriva tracciata) |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §Namespace memoria` — albero file-system completo
- [[WF-PRODUCT-INTELLIGENCE]] · `workflow/WF-PRODUCT-INTELLIGENCE.md` — produce backlog + intelligence state
- [[WF-ROADMAP-PRODOTTI]] · `workflow/WF-ROADMAP-PRODOTTI.md` — produce roadmap state
- [[REGOLE]] · `regole/REGOLE.md` — R1/R3 fondano le regole di integrità 1-2
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
