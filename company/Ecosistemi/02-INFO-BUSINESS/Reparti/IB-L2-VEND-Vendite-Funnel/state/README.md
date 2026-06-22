---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #vendite #funnel #IB-L2-VEND
Created: 2026-06-21
Last updated: 2026-06-21
---

# State — IB-L2-VEND Vendite & Funnel

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto.

---

## Namespace memoria del reparto

Radice AgentDB: `infobusiness/vendite/`

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Sales page | `infobusiness/vendite/salespage/{prodotto_id}/` | offer stack, copy APSOC, qa_log, state build/deploy/tracking | IB-VEND-OFFER + IB-VEND-SALESPAGE | IB-VEND-QA, IB-COORD-VENDITE, 06-PLATFORM |
| Evergreen | `infobusiness/vendite/evergreen/{prodotto_id}/` | opt-in + lead magnet, sequenza nurture, metriche per step | IB-VEND-LEAD + IB-VEND-SALESPAGE | IB-VEND-QA, IB-VEND-TRACK, IB-VEND-CRO |
| Funnel (CRO) | `infobusiness/vendite/funnel/` | test A/B, metriche step, offer stack corrente | IB-VEND-CRO | IB-COORD-VENDITE, IB-VEND-TRACK |
| Tracking | `infobusiness/vendite/tracking/` | config eventi/UTM, report conversioni per periodo | IB-VEND-TRACK | IB-VEND-CRO, IB-COORD-VENDITE, ib-director |

---

## Struttura file di stato

### Sales page state (`infobusiness/vendite/salespage/{prodotto_id}/state.json`)

```json
{
  "prodotto_id": "manuale-claude-code",
  "data_avvio": "YYYY-MM-DD",
  "offer_stack_status": "in_progress | completo | attesa_B003",
  "prezzi_approvati_B003": false,
  "copy_apsoc_status": "richiesto | in_produzione | gated | non_richiesto",
  "apsoc_score": null,
  "qa_gate": "pending | PASS | FAIL",
  "qa_fail_motivo": "optional — dettaglio se FAIL",
  "build_status": "non_inviato | inviato_06_platform | live",
  "tracking_status": "assente | configurato | debug_verde",
  "checkout_testato": false,
  "stato_finale": "in_progress | live | archiviato",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Evergreen state (`infobusiness/vendite/evergreen/{prodotto_id}/state.json`)

```json
{
  "prodotto_id": "manuale-claude-code",
  "data_avvio": "YYYY-MM-DD",
  "opt_in_status": "richiesto | gated | live",
  "lead_magnet": "descrizione asset (es. ebook gratuito)",
  "nurture_status": {
    "n_email": 5,
    "email_gated": [true, true, false, false, false],
    "frame": "founder_authority_stack"
  },
  "salespage_evergreen_status": "bozza | gated | live",
  "scarcity_check": "nessuna_scarcity_artificiale | bonus_reale_a_scadenza",
  "checkout_status": "non_configurato | configurato | testato",
  "ab_test_in_corso": "optional — test_id se attivo",
  "stato_finale": "in_progress | live | archiviato",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Test A/B state (`infobusiness/vendite/funnel/tests/{test_id}.json`)

```json
{
  "test_id": "TEST-001",
  "prodotto_id": "manuale-claude-code",
  "step_target": "opt-in | email_N | sales_page | checkout",
  "data_avvio": "YYYY-MM-DD",
  "ipotesi": "ipotesi falsificabile (non 'proviamo a vedere')",
  "elemento_cambiato": "un solo elemento (headline | cta | bump | ...)",
  "rollout_traffico_pct": 50,
  "metrica_primaria": "opt_in | cta_click | purchase",
  "campione_minimo": null,
  "campione_sufficiente": false,
  "decisione": "adottato | scartato | in_corso",
  "rationale": "obbligatorio anche se scartato",
  "data_chiusura": "YYYY-MM-DD"
}
```

---

## Regole di integrità dei namespace

1. **Sales page live senza prezzo approvato** — un `state.json` con `stato_finale: "live"` deve
   avere `prezzi_approvati_B003: true`. Altrimenti il funnel non può andare live (vincolo B-002/B-003).
   IB-VEND-OFFER + IB-VEND-QA responsabili.

2. **Output live senza `qa_gate: PASS`** — nessuna sales page o sequenza nurche può essere `live`
   con `qa_gate` diverso da `PASS`. Gate G-VEND bloccante (Regola R3).

3. **Test senza `decisione`** — un test in `funnel/tests/` non può essere chiuso (`data_chiusura`
   popolata) senza campo `decisione` ∈ {adottato, scartato}, con `campione_sufficiente: true` e
   `rationale` presente (Regola R5). IB-VEND-CRO responsabile.

4. **Evergreen con scarcity artificiale** — `scarcity_check` deve valere `nessuna_scarcity_artificiale`
   oppure `bonus_reale_a_scadenza`; mai una deadline finta (Regola R4). IB-VEND-QA responsabile.

5. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che riprende
   un workflow interrotto legge lo state per sapere a quale step riprendere. Lo state deve
   rispecchiare esattamente il punto attuale del workflow.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Sales page state | Step 1 WF-SALESPAGE | Ad ogni step (offer → copy → gate → build → tracking) | Dopo go live; non eliminato |
| Evergreen state | Step 1 WF-FUNNEL-EVERGREEN | Ad ogni step del loop (opt-in → nurture → page → checkout) | Dopo go live; loop CRO continua |
| Test A/B state | Step 1 WF-CRO-OTTIMIZZAZIONE | Durante il test fino al campione minimo | Dopo chiusura con decisione; non eliminato |
| Tracking report | Settimanale (loop evergreen) | Non aggiornato dopo emissione | Archiviato per periodo |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace `infobusiness/vendite/` e integrazione cross-reparto
- [[WF-SALESPAGE]] · `workflow/WF-SALESPAGE.md` — produce sales page state
- [[WF-FUNNEL-EVERGREEN]] · `workflow/WF-FUNNEL-EVERGREEN.md` — produce evergreen state
- [[WF-CRO-OTTIMIZZAZIONE]] · `workflow/WF-CRO-OTTIMIZZAZIONE.md` — produce test A/B state
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
