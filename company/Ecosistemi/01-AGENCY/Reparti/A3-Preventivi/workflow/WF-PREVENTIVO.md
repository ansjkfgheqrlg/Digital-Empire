---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #preventivi #problem-first #gate #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-PREVENTIVO — Da Brief Call a Proposta Inviata in 48h

> **ID:** WF-A3-001 · **Owner:** `ag-a3-coord` · **Reparto:** A3 Preventivi
> **Trigger:** discovery call avvenuta + trascrizione/appunti disponibili
> **Standard:** WRAPPA-ESISTENTE (beat-preventivi + proposal-gate v1) + TARGET-V2 (state, trace, learning)

---

## Scopo

Trasformare il brief di una discovery call in una **proposta problem-first inviata entro 48h**,
con pricing a catalogo fisso (mai sconti improvvisati) e gate finale bloccante. Flusso lineare a
pipeline: brief → audit → proposta → pricing → gate → approvazione → invio. La proposta apre sempre
con il problema del cliente, promette solo ciò che può provare, e vende l'autonomia del cliente
("l'agenzia progettata per essere licenziata"). Nessun documento esce senza Gate Preventivo verde.

---

## Attori

| Step | Agente A3 | Esterno / Umano |
|---|---|---|
| Ricezione e countdown | `ag-a3-coord` | A2 (fornisce call), A1 (dossier pre-call) |
| Brief strutturato | `ag-a3-brief` | Max (integra vincoli ambiente se mancano) |
| Quantificazione problema | `ag-a3-audit` | — |
| Scrittura proposta | `ag-a3-prop` | — |
| Pricing a catalogo | `ag-a3-price` | team-prezzi (B-003) come fonte del listino |
| Gate Preventivo | `ag-a3-qa` | — |
| Approvazione + invio | `ag-a3-coord` | Max (verifica pagamento alla firma) |
| Follow-up | `ag-a3-fup` | → `WF-FOLLOWUP-COMMERCIALE` |

---

## Flusso passo-passo

```
[TRIGGER]
Call avvenuta + trascrizione → AG-A3-COORD
  {lead_id, trascrizione_call, dossier_precall (da A1)}
         │
         ▼
[STEP 0] AG-A3-COORD — avvio + RECALL
  → avvia countdown 48h call→invio
  → memory_search("agency/03-preventivi") — preventivi simili, motivi di loss
  → memory_search("agency/reasoning") — pattern vincenti/persi nella nicchia
  → GATE-0: trascrizione utilizzabile? Sì → prosegui; no → richiesta appunti a Max
         │
         ▼
[STEP 1] AG-A3-BRIEF — brief strutturato (skill discovery-call-brief)
  → estrae: problema (parole cliente), awareness level (aware/unaware), stack attuale, vincoli ambiente
  → GATE-1: vincoli ambiente presenti?
     • mancanti → richiesta integrazione a Max PRIMA di scrivere (servono ad A4; il countdown 48h resta)
     • presenti → prosegui
         │
         ▼
[STEP 2] AG-A3-AUDIT — quantifica il problema (market-audit + cro_audit.py [WRAPPA])
  → trasforma il problema in dimensione misurabile/stimabile con fonte dichiarata
  → produce prove citabili (nessun numero senza fonte; altrimenti [DM])
         │
         ▼
[STEP 3] AG-A3-PROP — preventivo problem-first (beast-preventivi + market-proposal)
  → recall pattern vincenti da agency/reasoning
  → apertura = problema del cliente (MAI Digital Empire)
  → adatta tono all'awareness level (aware/unaware)
  → soluzione orientata all'autonomia; promesse = prove dell'audit
         │
         ▼
[STEP 4] AG-A3-PRICE — seleziona prodotto/bundle dal CATALOGO FISSO
  → mappa problema → prodotto: Outreach €4.000 / Content €3.500 / Second Brain €2.500 / Engine Room €8.000
  → NESSUNO sconto, nessun prezzo inventato (B-003); razionale prodotto→problema
         │
         ▼
[STEP 5] AG-A3-QA — GATE PREVENTIVO (skill proposal-gate) — BLOCCANTE
  → check: problema apre il doc · awareness corretto · solo pricing catalogo · promesse=prove ·
    scope ≤7gg · clausola proprietà codice + €0 canoni · supporto 90gg · brand voice
  → GATE-2: PASS → prosegui; FAIL → diagnosi per item → AG-A3-PROP rework (countdown 48h resta) → re-gate
         │
         ▼
[STEP 6] AG-A3-COORD — approvazione + invio
  → approva SOLO dopo gate PASS
  → invio ≤48h dalla call
  → record in agency/03-preventivi/{id} (stato: inviato)
  → attiva AG-A3-FUP → WF-FOLLOWUP-COMMERCIALE
         │
         ▼
[ESITO] (gestito da WF-FOLLOWUP-COMMERCIALE)
  → WIN: HC-AG-AM-01 ad A7 + scope congelato ad A4 (firma/pagamento umani, Max)
  → LOSS: AG-A3-LEARN registra motivo in agency/reasoning
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Trascrizione utilizzabile | Appunti/trascrizione call presenti e leggibili | AG-A3-COORD | Avvio del workflow |
| G1 — Vincoli ambiente nel brief | Vincoli ambiente/server catturati (servono ad A4) | AG-A3-BRIEF | Passaggio alla scrittura |
| G2 — Gate Preventivo (proposal-gate) | Tutti gli item conformi (problema apre, prezzo catalogo, prove, clausole, scope, supporto, voice) | AG-A3-QA | Invio della proposta |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "lead_id": "LEAD-001",
  "call_source": "A2-Acquisizione",
  "trascrizione_call": "appunti discovery call",
  "dossier_precall": "agency/01-ricerca/dossier/LEAD-001",
  "deadline_invio": "call + 48h"
}
```

**Output finale:**
```json
{
  "preventivo_id": "PREV-001",
  "lead_id": "LEAD-001",
  "prodotto": "Outreach Factory",
  "prezzo": 4000,
  "esito_gate": "PASS",
  "data_invio": "YYYY-MM-DDTHH:MM:SSZ",
  "stato": "inviato",
  "namespace_state": "agency/03-preventivi/PREV-001"
}
```

---

## State

File: `agency/03-preventivi/{preventivo_id}/state.json` — per ogni preventivo: `id`, `lead`,
`prodotto`, `esito_gate`, `data_invio`, `stato` (inviato/in_followup/win/loss).
- Aggiornato ad ogni step; `last_updated` sempre presente.
- Permette la **ripartibilità a freddo**: se il workflow si interrompe (es. attesa integrazione da
  Max sui vincoli ambiente), un agente riprende dallo step esatto leggendo lo state — senza riestrarre il contesto.
- Il record resta nel namespace per il recall dei preventivi futuri (Step 0).

---

## Failure & recovery

- Gate Preventivo FAIL → rework con le note del gate (mai bypass); il countdown 48h NON si ferma.
- Brief incompleto sui vincoli ambiente → richiesta a Max prima di scrivere; il countdown delivery
  7gg (A4) parte solo ad ambiente conforme.
- Richiesta sconto fuori catalogo → NO automatico; deroga = decisione Board (B-003).
- Trascrizione assente → il WF non parte a vuoto: AG-A3-COORD richiede appunti.

---

## Connessioni

- [[ag-a3-coord]] · `agenti/ag-a3-coord.md` — owner del workflow
- [[ag-a3-qa]] · `agenti/ag-a3-qa.md` — Gate Preventivo bloccante (G2)
- [[ag-a3-prop]] · `agenti/ag-a3-prop.md` — scrittura problem-first
- [[WF-FOLLOWUP-COMMERCIALE]] · `workflow/WF-FOLLOWUP-COMMERCIALE.md` — presidio post-invio
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A3`
