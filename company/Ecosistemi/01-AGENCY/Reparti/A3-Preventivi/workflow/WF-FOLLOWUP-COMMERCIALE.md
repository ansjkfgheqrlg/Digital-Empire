---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #preventivi #followup #commerciale #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-FOLLOWUP-COMMERCIALE — Presidio 10gg Post-Invio

> **ID:** WF-A3-002 · **Owner:** `ag-a3-fup` · **Reparto:** A3 Preventivi
> **Trigger:** proposta inviata da `WF-PREVENTIVO` (stato `inviato`)
> **Standard:** TARGET-V2

---

## Scopo

Presidiare i 10 giorni successivi all'invio del preventivo con **3 touch non invasivi** (D+3, D+7,
D+10) per portare ogni proposta a un esito chiaro: win o loss. Nessun touch invasivo, rispetto
assoluto dei segnali "no", e — in ogni caso — **motivo di loss SEMPRE registrato**. Su win, il
workflow attiva la catena verso la firma (HC-AG-AM-01 ad A7 + scope ad A4). Su loss, passa il
testimone ad AG-A3-LEARN. Nessun preventivo resta "in sospeso" oltre D+10.

---

## Attori

| Step | Agente A3 | Esterno / Umano |
|---|---|---|
| Sequenza 3 touch | `ag-a3-fup` | Lead (risponde / non risponde) |
| Coordinamento esito | `ag-a3-coord` | Max (verifica firma + pagamento su win) |
| Registrazione loss | `ag-a3-learn` | — |
| Handoff win | `ag-a3-coord` | A7 (`HC-AG-AM-01`) + A4 (scope congelato) |

---

## Flusso passo-passo

```
[TRIGGER]
Proposta inviata (stato inviato) → AG-A3-FUP
  {preventivo_id, lead_id, data_invio, prodotto, thread_conversazione}
         │
         ▼
[STEP 0] AG-A3-FUP — programmazione sequenza
  → aggiorna stato preventivo: inviato → in_followup
  → schedula 3 touch: D+3 (valore), D+7 (prova), D+10 (chiusura)
         │
         ▼
[STEP 1] D+3 — TOUCH VALORE
  → non "hai deciso?": un chiarimento o un elemento di valore ancorato al problema del cliente
  → GATE-NO: segnale "no" → chiudi sequenza come LOSS (vai a STEP 4)
  → risposta positiva → prepara handoff WIN (vai a STEP 5)
  → nessuna risposta → prosegui a D+7
         │
         ▼
[STEP 2] D+7 — TOUCH PROVA
  → caso/prova pertinente alla nicchia del cliente (prove non promesse)
  → GATE-NO: "no" → LOSS · positiva → WIN · nessuna risposta → prosegui a D+10
         │
         ▼
[STEP 3] D+10 — TOUCH CHIUSURA
  → chiusura gentile: porta aperta, nessuna pressione
  → risposta positiva → WIN · "no" o silenzio → LOSS "no risposta"
  → NESSUN quarto contatto
         │
         ├───────────────► [STEP 4] LOSS
         │                   → AG-A3-FUP passa segnali raccolti ad AG-A3-LEARN
         │                   → AG-A3-LEARN registra MOTIVO in agency/reasoning (sempre)
         │                   → aggiorna stato preventivo: in_followup → loss
         │
         └───────────────► [STEP 5] WIN
                             → AG-A3-COORD attiva HC-AG-AM-01 ad A7 (profilo cliente + KAM)
                             → scope congelato → A4 Delivery (countdown 7gg ad ambiente conforme)
                             → firma + verifica pagamento = UMANO (Max); handoff A4 parte solo dopo
                             → aggiorna stato preventivo: in_followup → win
```

---

## Gate bloccanti

| Gate | Condizione | Owner | Effetto |
|---|---|---|---|
| GATE-NO — rispetto del "no" | Qualsiasi segnale di rifiuto | AG-A3-FUP | Chiude la sequenza come LOSS immediatamente; nessun touch ulteriore |
| GATE-MAX-3 — non invasività | Massimo 3 touch in 10gg | AG-A3-FUP | Dopo D+10 nessun quarto contatto; esito forzato (loss "no risposta") |
| GATE-MOTIVO — loss documentato | Ogni loss ha un motivo registrato | AG-A3-LEARN | Loss non chiudibile senza causa in `agency/reasoning` |
| GATE-PAGAMENTO — win verificato | Firma + pagamento verificati (umano) | Max | Handoff ad A4 non parte senza verifica |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "preventivo_id": "PREV-001",
  "lead_id": "LEAD-001",
  "data_invio": "2026-06-22T14:00:00Z",
  "prodotto": "Outreach Factory €4.000",
  "thread_conversazione": "storico contatti da A2"
}
```

**Output finale:**
```json
{
  "preventivo_id": "PREV-001",
  "touch_eseguiti": ["D+3", "D+7", "D+10"],
  "esito": "win | loss",
  "handoff": "HC-AG-AM-01 + A4 (se win) | AG-A3-LEARN (se loss)",
  "stato": "win | loss"
}
```

---

## State

File: `agency/03-preventivi/{preventivo_id}/state.json` — campo `stato` evolve
`inviato → in_followup → win|loss`; ogni touch e l'esito sono registrati con timestamp.
- Ripartibilità a freddo: se il presidio si interrompe, AG-A3-FUP riprende dal touch non ancora eseguito.
- L'esito loss alimenta `WF-LOSS-ANALYSIS` via AG-A3-LEARN.

---

## Failure & recovery

- Richiesta sconto per chiudere → non si rinegozia il prezzo (B-003); segnalazione ad AG-A3-COORD.
- Richiesta di modifica scope/prodotto → nuovo preventivo se cambia il prodotto (rientra in WF-PREVENTIVO).
- Obiezione ricorrente non gestibile → segnalata ad AG-A3-LEARN/A5 anche su win (libreria obiezioni).
- Win senza pagamento verificato → handoff ad A4 in attesa; nessuna delivery avviata.

---

## Connessioni

- [[ag-a3-fup]] · `agenti/ag-a3-fup.md` — owner del workflow
- [[ag-a3-learn]] · `agenti/ag-a3-learn.md` — registra il motivo di ogni loss
- [[ag-a3-coord]] · `agenti/ag-a3-coord.md` — coordina l'handoff alla firma
- [[WF-PREVENTIVO]] · `workflow/WF-PREVENTIVO.md` — workflow a monte
- [[WF-LOSS-ANALYSIS]] · `workflow/WF-LOSS-ANALYSIS.md` — workflow a valle (aggregazione loss)
