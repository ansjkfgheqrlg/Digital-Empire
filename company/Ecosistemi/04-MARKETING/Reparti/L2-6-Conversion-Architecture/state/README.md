---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #cro #funnel #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# State — L2.6 Conversion Architecture

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto.

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Funnels | `marketing/cro/funnels/` | Architettura funnel per committente: stage map, brief tecnici, stato workflow, gate CA-QA | CONV-LEAD | CA1, CA4, CA-QA |
| Sprint CRO | `marketing/cro/sprints/` | Sprint CRO: collo di bottiglia, variante, disegno test, verdetto, risultato post-implementazione | CA4 | CONV-LEAD, CA-QA, AN5 |
| Audit | `marketing/cro/audits/` | Audit landing: 4 dimensioni, diagnosi, 3 azioni prioritarie, raccomandazione | CA-QA | CONV-LEAD, CA4 |

---

## Struttura file di stato

### Funnel state (`marketing/cro/funnels/{funnel_id}/state.json`)

```json
{
  "funnel_id": "FUNNEL-001",
  "committente": "02-INFO",
  "prodotto": "nome prodotto",
  "data_avvio": "YYYY-MM-DD",
  "stage_map_status": "in_progress | completata",
  "copy_status": {
    "ToFu": "richiesto | in_produzione | gated | non_richiesto",
    "MoFu": "richiesto | in_produzione | gated | non_richiesto",
    "BoFu": "richiesto | in_produzione | gated | non_richiesto"
  },
  "brief_tecnico_status": {
    "LP-001": "bozza | approvato | inviato_06_platform",
    "LP-002": "bozza | approvato | inviato_06_platform"
  },
  "micro_conversion_schema_status": "assente | prodotto | consegnato_AN5",
  "email_status": {
    "MoFu": "richiesto | gated | non_richiesto",
    "BoFu": "richiesto | gated | non_richiesto"
  },
  "ca_qa_gate": "pending | PASS | FAIL",
  "ca_qa_fail_motivo": "optional — dettaglio se FAIL",
  "stato_finale": "in_progress | handoff_completo | archiviato",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Sprint state (`marketing/cro/sprints/{sprint_id}.json`)

```json
{
  "sprint_id": "SPRINT-001",
  "funnel_id": "FUNNEL-001",
  "landing_id": "LP-BOFU-001",
  "trigger": "drop_report_AN5 | audit_CA_QA",
  "data_avvio": "YYYY-MM-DD",
  "collo_di_bottiglia": "descrizione sezione APSOC + elemento",
  "sezione_APSOC": "A | P | S | O | CTA",
  "variante": "descrizione modifica + ipotesi",
  "tipo_variante": "copy | struttura",
  "copy_gated": true,
  "test_design": {
    "metrica_primaria": "cta_click | form_submit | acquisto",
    "criterio_verdetto": "p-value <0.05",
    "dimensione_campione_validata": true
  },
  "verdetto": "winner_variante | winner_controllo | inconclusivo",
  "implementato": true,
  "data_chiusura": "YYYY-MM-DD",
  "learning": "descrizione del learning (obbligatorio anche se inconclusivo)"
}
```

### Audit state (`marketing/cro/audits/{audit_id}.json`)

```json
{
  "audit_id": "AUDIT-001",
  "url_landing": "https://...",
  "committente": "02-INFO",
  "data_audit": "YYYY-MM-DD",
  "azioni_prioritarie": [
    {"priorita": 1, "elemento": "...", "tipo_intervento": "...", "impatto_stimato": "..."},
    {"priorita": 2, "elemento": "...", "tipo_intervento": "...", "impatto_stimato": "..."},
    {"priorita": 3, "elemento": "...", "tipo_intervento": "...", "impatto_stimato": "..."}
  ],
  "raccomandazione": "sprint_CRO | redesign_strutturale",
  "sprint_generati": ["SPRINT-001"],
  "stato": "completato"
}
```

---

## Regole di integrità dei namespace

1. **Sprint senza `verdetto`** — uno sprint senza campo `verdetto` è uno sprint non chiuso.
   Non può esistere in `marketing/cro/sprints/` senza questo campo popolato alla chiusura.
   CA4 è responsabile. Anomalia segnalata da AN-OBSERVER (L2.4) se rilevata.

2. **Funnel senza `ca_qa_gate`** — un funnel in stato `handoff_completo` deve avere
   `ca_qa_gate: "PASS"`. Se è `FAIL` o `pending` il funnel non può essere in stato `handoff_completo`.

3. **Audit senza 3 azioni** — un audit non può avere `stato: "completato"` se
   `azioni_prioritarie` ha meno di 3 elementi. CA-QA è responsabile.

4. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente
   che riprende un workflow interrotto legge lo state per sapere a quale step riprendere.
   Lo state deve rispecchiare esattamente il punto attuale del workflow.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Funnel state | Step 1 WF-FUNNEL-DESIGN | Ad ogni step del workflow | Dopo `handoff_completo`; non eliminato |
| Sprint state | Step 1 WF-CRO-SPRINT | Ad ogni step del workflow | Dopo chiusura con verdetto; non eliminato |
| Audit state | Step 6 WF-LANDING-AUDIT | Non aggiornato dopo consegna | Archiviato; sprint generati linkati |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — namespace e integrazione con altri sistemi
- [[WF-FUNNEL-DESIGN]] · `workflow/WF-FUNNEL-DESIGN.md` — produce funnel state
- [[WF-CRO-SPRINT]] · `workflow/WF-CRO-SPRINT.md` — produce sprint state
- [[WF-LANDING-AUDIT]] · `workflow/WF-LANDING-AUDIT.md` — produce audit state
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
