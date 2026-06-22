---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #infobusiness #prodotto #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# State — IB-L2-PROD Produzione Prodotti

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto.

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Validazione | `infobusiness/prod/validazione/` | Idea, score /100, breakdown 5 criteri, MVP result, esito, data | IB-PROD-VALID | IB-COORD-PRODOTTO, IB-PROD-QA |
| Corso | `infobusiness/prod/corso/` | Per corso: fase, gate superati, MKD, curriculum, smoke test, errori bloccanti | IB-COORD-PRODOTTO | IB-PROD-MKD, IB-PROD-CURRIC, IB-PROD-WRITER, IB-PROD-PLATFORM, IB-PROD-QA |
| Ebook | `infobusiness/prod/ebook/` | Per ebook: fase, capitoli, gate, export PDF/ePub, pagina download | IB-COORD-PRODOTTO | IB-PROD-MKD, IB-PROD-EBOOK, IB-PROD-DESIGN, IB-PROD-QA |
| Reasoning | `infobusiness/prod/reasoning/` | Pattern di processo: cosa rallenta, quale formato converte, difetti ricorrenti | IB-PROD-LEARN | IB-COORD-PRODOTTO, tutti |

---

## Layout file-system del namespace

```
infobusiness/prod/
├── validazione/
│   └── state.json                  → idea, score /100, breakdown, MVP result, esito, data
├── corso/
│   ├── state.json                  → per corso: fase corrente, gate superati, errori bloccanti, log
│   ├── MKD-{prodotto}.md           → Master Knowledge Document (100% atomi)
│   ├── atomi-check-{prodotto}.json → checklist quantitativa copertura atomi
│   ├── CURRIC-{prodotto}.md        → curriculum con outcome map
│   └── smoke-test-{prodotto}.json  → log smoke test studente fantasma
├── ebook/
│   └── state.json                  → per ebook: fase, capitoli, gate, export PDF/ePub
└── reasoning/
    └── pattern-{YYYYMMDD}.md       → pattern di processo da IB-PROD-LEARN
```

---

## Struttura file di stato

### Validazione state (`infobusiness/prod/validazione/state.json`)

```json
{
  "idea_id": "IDEA-001",
  "titolo": "nome idea prodotto",
  "fonte_brief": "HC-STRA-IB-01 | backlog | community | segnale agency",
  "score": 0,
  "breakdown": {
    "problema_reale": 0,
    "raw_disponibile": 0,
    "icp_chiaro": 0,
    "differenziazione": 0,
    "posizionamento_de": 0
  },
  "gate_1": "PASS | FAIL",
  "mvp_test": {
    "data_inizio": "YYYY-MM-DD",
    "si_comprerei": 0,
    "soglia": 5,
    "gate_2": "PASS | FAIL | in_corso"
  },
  "esito": "brief_validato | backlog",
  "motivo_fail": "optional — dettaglio se FAIL",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Corso state (`infobusiness/prod/corso/state.json`)

```json
{
  "prodotto_id": "CORSO-001",
  "titolo": "Vendi la Skill",
  "brief_validato": true,
  "fase_corrente": "mkd | curriculum | writing | handoff_cf | deploy | design | done",
  "gate_qa": {
    "atomi_100": "pending | PASS | FAIL",
    "outcome_per_lezione": "pending | PASS | FAIL",
    "brand_voice": "pending | PASS | FAIL",
    "smoke_test": "pending | PASS | FAIL",
    "asset_no_placeholder": "pending | PASS | FAIL"
  },
  "handoff": {
    "HC-CF-IB-01": "non_avviato | inviato | accettato",
    "HC-PL-IB-01": "non_avviato | inviato | smoke_verde",
    "HC-IB-VEND-01": "non_avviato | consegnato"
  },
  "errori_bloccanti": [],
  "stato_finale": "in_progress | live | archiviato",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Ebook state (`infobusiness/prod/ebook/state.json`)

```json
{
  "prodotto_id": "EBOOK-001",
  "titolo": "Manuale Claude Code",
  "brief_validato": true,
  "fase_corrente": "mkd | capitoli | writing | impaginazione | storage | done",
  "capitoli": [{"id": "C1", "cta": true, "esercizio": true, "gated": false}],
  "gate_qa": {
    "atomi_100": "pending | PASS | FAIL",
    "cta_ed_esercizio_per_capitolo": "pending | PASS | FAIL",
    "prove_non_promesse": "pending | PASS | FAIL",
    "leggibile_mobile_link_ok": "pending | PASS | FAIL"
  },
  "export": {"pdf": false, "epub": false, "pagina_download": false},
  "routing_free_paid": "indeciso (B-002 BACKLOG, attende team-prezzi B-003)",
  "stato_finale": "in_progress | pronto | archiviato",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Regole di integrità dei namespace

1. **Prodotto senza `brief_validato: true`** — nessun `state.json` in `corso/` o `ebook/` può avere
   `fase_corrente` oltre la creazione se `brief_validato` è false. IB-PROD-VALID è responsabile (R1).

2. **Corso `live` senza gate QA completi** — un corso in `stato_finale: "live"` deve avere tutti i
   `gate_qa` a `PASS`, inclusi `atomi_100` e `smoke_test`. Altrimenti il prodotto non può essere live (R4/R6).

3. **MKD sotto soglia copertura** — `atomi-check-{prodotto}.json` con `copertura_pct < 100` blocca
   l'avanzamento di fase. IB-PROD-QA è responsabile (R2).

4. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che riprende un
   workflow interrotto legge lo state per sapere a quale fase riprendere. Lo state rispecchia esattamente
   il punto attuale del workflow.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Validazione state | Step 1 WF-VALIDAZIONE | Ad ogni gate (score, MVP) | Dopo esito; non eliminato (anche se BACKLOG) |
| Corso state + MKD/CURRIC | Step 1 WF-CORSO | Ad ogni fase del workflow | Dopo `live`; non eliminato |
| Ebook state | Step 1 WF-EBOOK | Ad ogni fase del workflow | Dopo `pronto`; non eliminato |
| Pattern reasoning | Fine di ogni ciclo (IB-PROD-LEARN) | Append-only | Mai eliminato; consultato in RECALL |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria e handoff contract
- [[WF-VALIDAZIONE]] · `workflow/WF-VALIDAZIONE.md` — produce validazione state
- [[WF-CORSO]] · `workflow/WF-CORSO.md` — produce corso state + MKD + curriculum + smoke test
- [[WF-EBOOK]] · `workflow/WF-EBOOK.md` — produce ebook state + export
- [[KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
