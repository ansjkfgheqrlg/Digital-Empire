---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #agency #preventivi #reasoning #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# State — A3 Preventivi

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto.

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Preventivi | `agency/a3/` | Ogni preventivo: id, lead, prodotto, esito gate, data invio, stato | AG-A3-COORD | AG-A3-QA, AG-A3-FUP, AG-A3-PROP (recall) |
| Reasoning | `agency/reasoning` | Win/loss con causa, categoria, nicchia; pattern del ReasoningBank | AG-A3-LEARN | AG-A3-PROP (recall), AG-A3-COORD |

---

## Struttura file di stato

### Preventivo state (`agency/a3/{preventivo_id}/state.json`)

```json
{
  "preventivo_id": "PREV-001",
  "lead_id": "LEAD-001",
  "call_source": "A2-Acquisizione",
  "data_call": "YYYY-MM-DDTHH:MM:SSZ",
  "prodotto": "Outreach Factory | Content Factory | Second Brain | Engine Room",
  "prezzo": 4000,
  "awareness_level": "aware | unaware",
  "vincoli_ambiente_completi": true,
  "esito_gate": "pending | PASS | FAIL",
  "gate_fail_motivo": "optional — diagnosi se FAIL",
  "data_invio": "YYYY-MM-DDTHH:MM:SSZ",
  "stato": "in_lavorazione | inviato | in_followup | win | loss",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Reasoning record (`agency/reasoning` — un record per esito)

```json
{
  "preventivo_id": "PREV-001",
  "esito": "win | loss",
  "causa": "descrizione (obbligatoria, anche se 'motivo non emerso')",
  "categoria": "prezzo | scope | competitor | tempistica | no_risposta | altro",
  "nicchia": "consulenza",
  "prodotto": "Outreach Factory",
  "segnali": "obiezioni / silenzio / competitor menzionato (da AG-A3-FUP)",
  "riusabile_come": "pattern: descrizione riusabile in recall",
  "data": "YYYY-MM-DD"
}
```

---

## Regole di integrità dei namespace

1. **Loss senza `causa`** — un record con `esito: "loss"` deve avere `causa` popolata (Regola R7).
   Un loss senza motivo non è chiuso e alimenta WF-LOSS-ANALYSIS con dati incompleti. AG-A3-LEARN
   è responsabile.

2. **Preventivo `inviato` senza `esito_gate: PASS`** — un preventivo non può essere in stato
   `inviato` se `esito_gate` non è `PASS`. Nessun invio senza gate verde (Regola R1). AG-A3-COORD
   è responsabile.

3. **Prezzo fuori catalogo** — il campo `prezzo` deve essere uno dei valori del catalogo fisso
   (4000/3500/2500/8000). Qualsiasi altro valore è un'anomalia (violazione R2/R3). AG-A3-QA blocca.

4. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che riprende
   un workflow interrotto legge lo state per sapere a quale step ripartire. Lo state rispecchia
   esattamente il punto attuale (es. `in_lavorazione` con `vincoli_ambiente_completi: false` →
   il WF è in attesa di integrazione da Max).

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Preventivo state | Step 0 WF-PREVENTIVO | Ad ogni step (gate, invio, follow-up, esito) | Dopo `win`/`loss`; non eliminato (recall futuro) |
| Reasoning record | Alla chiusura esito (WF-FOLLOWUP) | Non aggiornato dopo la scrittura | Permanente; base del ReasoningBank |
| Report loss mensile | Step 5 WF-LOSS-ANALYSIS | Non aggiornato dopo consegna | Archiviato; pattern linkati ai record |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` §4 — namespace e integrazione con altri reparti
- [[WF-PREVENTIVO]] · `workflow/WF-PREVENTIVO.md` — produce il preventivo state
- [[WF-FOLLOWUP-COMMERCIALE]] · `workflow/WF-FOLLOWUP-COMMERCIALE.md` — aggiorna stato → win/loss
- [[WF-LOSS-ANALYSIS]] · `workflow/WF-LOSS-ANALYSIS.md` — legge i reasoning record
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
