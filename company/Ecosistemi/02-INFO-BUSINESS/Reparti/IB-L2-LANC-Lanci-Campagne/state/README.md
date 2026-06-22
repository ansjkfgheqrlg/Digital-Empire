---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #lanci #campagne #IB-L2-LANC
Created: 2026-06-21
Last updated: 2026-06-21
---

# State — IB-L2-LANC Lanci & Campagne

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto.

---

## Namespace memoria del reparto

AgentDB namespace radice: `infobusiness/lanc`. Layout su file-system: `infobusiness/lanci/`.

| Namespace | Path file-system | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Lancio | `infobusiness/lanci/{lancio-id}/` | Calendario, handoff, copy approvati, asset, dry-run, go/no-go, tracking, debrief, gate | IB-COORD-LANCI | tutti gli agenti del reparto |
| Webinar | `infobusiness/lanci/webinar/` | Stato webinar + replay funnel + metriche registrati/partecipanti | IB-LANC-WEBINAR | IB-COORD-LANCI, IB-LANC-QA |
| Libreria evergreen | `infobusiness/lanci/libreria-evergreen/` | Top copy/hook con metriche reali (WF-FOLLOWUP-COPY) | IB-LANC-COPY-LIAISON | IB-COORD-LANCI, 04-MARKETING |
| ReasoningBank | `infobusiness/reasoningbank/` (ns `infobusiness/lanc`) | Pattern distillati per lancio (≥3 per lancio) | IB-LANC-DEBRIEF | tutti; ib-director |

---

## Struttura file di stato

### Lancio state (`infobusiness/lanci/{lancio-id}/state.json`)

```json
{
  "lancio_id": "LANCIO-001",
  "prodotto": "course_id | ebook_id",
  "prodotto_gate_qualita": "PASS | non_verificato",
  "budget_approvato_OPS": true,
  "data_avvio_calendario": "YYYY-MM-DD",
  "data_cart_open": "YYYY-MM-DD",
  "step": {
    "T-30_planner": "pending | done",
    "T-28_HC-IN-IB-01": "pending | inviato | rientrato",
    "T-21_HC-IB-CF-01": "pending | inviato | rientrato",
    "T-14_HC-IB-MK-01": "pending | inviato | rientrato",
    "T-14_gate_APSOC": "pending | PASS | FAIL",
    "T-7_copy_liaison": "pending | validato",
    "T-3_asset": "pending | checklist_100",
    "T-1_dry_run": "pending | PASS | BLOCK",
    "go_nogo": "pending | GO | NO-GO",
    "cart_open": "pending | aperto | chiuso",
    "T+7_debrief": "pending | scritto"
  },
  "gate": {
    "ib_lanc_qa_copy": "pending | PASS | FAIL",
    "ib_lanc_qa_asset": "pending | PASS | FAIL",
    "ib_lanc_qa_dry_run": "pending | PASS | FAIL"
  },
  "go_nogo_voci": {
    "ib-director": "pending | GO | NO",
    "IB-LANC-QA": "pending | GO | NO",
    "Quality-Sentinel": "pending | GO | NO",
    "Brand-Voice-Sentinel": "pending | GO | NO",
    "Cost-Sentinel": "pending | GO | NO"
  },
  "delta_budget_dry_run_pct": null,
  "stato_finale": "in_progress | cart_chiuso | debrief_completo | archiviato",
  "errori": [],
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Webinar state (`infobusiness/lanci/webinar/state.json`)

```json
{
  "webinar_id": "WEBINAR-001",
  "lancio_id": "LANCIO-001",
  "script_status": "bozza | gated | live",
  "script_gate_APSOC": "pending | PASS | FAIL",
  "modalita": "live | registrazione",
  "replay_funnel": "non_configurato | live",
  "scarcity_replay_reale": true,
  "metriche": {"registrati": null, "partecipanti": null},
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Debrief state (`infobusiness/lanci/{lancio-id}/debrief.md` + diff JSON)

```json
{
  "lancio_id": "LANCIO-001",
  "data_debrief": "YYYY-MM-DD",
  "piano_vs_reale": [
    {"kpi": "conversione_cart_open", "pianificato": "[DM]", "reale": "...", "delta_pct": "...", "root_cause": "..."},
    {"kpi": "delta_budget", "pianificato": "...", "reale": "...", "delta_pct": "...", "root_cause": "..."}
  ],
  "pattern_distillati": ["pattern 1", "pattern 2", "pattern 3"],
  "top_copy_followup": {"email": ["..."], "hook": ["..."]},
  "raccomandazione_skill_agente": "...",
  "stato": "scritto"
}
```

---

## Regole di integrità dei namespace

1. **Lancio senza `T+7_debrief: "scritto"`** — un lancio in `stato_finale: "debrief_completo"`
   deve avere il debrief scritto e ≥3 pattern in ReasoningBank (R8). IB-LANC-DEBRIEF è responsabile.
   Anomalia segnalata a ib-director se rilevata.

2. **Cart open senza `T-1_dry_run: "PASS"` e `go_nogo: "GO"`** — nessun lancio può avere
   `cart_open: "aperto"` senza dry-run PASS e go/no-go GO registrati. Violazione = R5/R7.

3. **`go_nogo: "GO"` con un voto `NO`** — incoerenza di integrità: UN solo NO blocca (R7).
   Se anche una sola voce in `go_nogo_voci` è `NO`, `go_nogo` non può essere `GO`.

4. **Lancio senza `prodotto_gate_qualita: "PASS"` o `budget_approvato_OPS: true`** — non può
   passare oltre `T-30_planner` (R1). IB-COORD-LANCI è responsabile.

5. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che riprende
   un lancio interrotto legge lo state per sapere a quale step T-N riprendere. Lo state deve
   rispecchiare esattamente il punto attuale del calendario.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Lancio state | Step T-30 WF-LANCIO (PLANNER) | Ad ogni step del calendario | Dopo `debrief_completo`; non eliminato |
| Webinar state | Avvio WF-WEBINAR | Ad ogni fase (script→gate→live→replay) | Dopo metriche raccolte; non eliminato |
| Debrief | Step T+7 WF-DEBRIEF-LANCIO | Non aggiornato dopo consegna | Archiviato; pattern linkati a ReasoningBank |
| Libreria evergreen | WF-FOLLOWUP-COPY | Append-only con metriche reali | Permanente; solo copy con numeri reali (P6) |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` §Namespace memoria — layout completo dei namespace
- [[WF-LANCIO]] · `workflow/WF-LANCIO.md` — produce lancio state
- [[WF-WEBINAR]] · `workflow/WF-WEBINAR.md` — produce webinar state
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
