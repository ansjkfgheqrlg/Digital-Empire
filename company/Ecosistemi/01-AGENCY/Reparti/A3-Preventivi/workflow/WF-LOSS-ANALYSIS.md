---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #preventivi #loss #reasoningbank #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-LOSS-ANALYSIS — Analisi Strutturata dei Preventivi Persi

> **ID:** WF-A3-003 · **Owner:** `ag-a3-learn` · **Reparto:** A3 Preventivi
> **Trigger:** cadenza mensile + trigger immediato su 2 loss consecutive sulla stessa nicchia
> **Standard:** TARGET-V2

---

## Scopo

Analizzare in modo strutturato ogni preventivo perso per migliorare la pipeline. AG-A3-LEARN aggrega
i loss degli ultimi 30 giorni, individua i **pattern** (prezzo? scope? competitor? tempistica?) e
produce un report mensile che va ad A5 (per aggiornare la libreria obiezioni) e a 08-INTELLIGENCE
(`HC-AG-IN-01`). La disciplina cardine è statistica: **almeno 5 loss per dichiarare un pattern
significativo; nessuna conclusione su n < 3**. Un pattern dichiarato su rumore è peggio di nessun
pattern: porta a cambiare la pipeline nella direzione sbagliata.

---

## Attori

| Step | Agente A3 | Esterno |
|---|---|---|
| Aggregazione loss | `ag-a3-learn` | — |
| Validazione soglia | `ag-a3-learn` | — |
| Report + handoff | `ag-a3-learn` | A5 (libreria obiezioni), 08-INTELLIGENCE (`HC-AG-IN-01`) |
| Trigger anticipato | `ag-a3-coord` | — (su 2 loss consecutive stessa nicchia) |

---

## Flusso passo-passo

```
[TRIGGER]
Cadenza mensile (o 2 loss consecutive stessa nicchia) → AG-A3-LEARN
         │
         ▼
[STEP 1] AG-A3-LEARN — raccolta loss ultimi 30gg
  → memory_search("agency/reasoning") filtrato per esito = loss, finestra 30gg
  → ogni record ha: causa, categoria, nicchia, prodotto, segnali
  → GATE-DATI: ogni loss ha un motivo registrato? (se manca → anomalia: WF-FOLLOWUP non ha chiuso bene)
         │
         ▼
[STEP 2] AG-A3-LEARN — raggruppamento per pattern
  → raggruppa per categoria (prezzo / scope / competitor / tempistica / no_risposta / altro)
  → e per nicchia
  → conta le occorrenze per ogni gruppo (categoria × nicchia)
         │
         ▼
[STEP 3] AG-A3-LEARN — validazione soglia statistica
  → GATE-SOGLIA:
     • n ≥ 5  → pattern SIGNIFICATIVO (entra nel report con azione consigliata)
     • 3 ≤ n < 5 → pattern EMERGENTE (annotato, da osservare; nessuna azione forte)
     • n < 3  → NESSUNA conclusione (scartato dal report come segnale)
         │
         ▼
[STEP 4] AG-A3-LEARN — diagnosi del pattern
  → per ogni pattern significativo: qual è la causa radice?
     prezzo → posizionamento/catalogo (decisione team-prezzi B-003, NON del reparto)
     scope → chiarezza della proposta / aspettative (azione: AG-A3-PROP, AG-A3-BRIEF)
     competitor → argomenti di differenziazione (azione: A5 obiezioni + 08-INTELLIGENCE)
     tempistica → velocità invio / urgenza percepita (azione: AG-A3-COORD su SLA 48h)
         │
         ▼
[STEP 5] AG-A3-LEARN — report mensile + handoff
  → report: pattern significativi + emergenti + azioni per destinatario
  → → A5: aggiorna libreria obiezioni con i motivi di loss ricorrenti
  → → 08-INTELLIGENCE: HC-AG-IN-01 (intelligence di nicchia per argomentare il problema)
  → aggiorna ReasoningBank: i pattern diventano recall per AG-A3-PROP nei preventivi futuri
```

---

## Gate bloccanti

| Gate | Condizione | Owner | Effetto |
|---|---|---|---|
| GATE-DATI — loss documentato | Ogni loss della finestra ha un motivo registrato | AG-A3-LEARN | Loss senza motivo = anomalia segnalata (WF-FOLLOWUP non ha chiuso correttamente) |
| GATE-SOGLIA — significatività | Pattern significativo solo con n ≥ 5; nessuna conclusione su n < 3 | AG-A3-LEARN | Pattern sotto soglia escluso dalle azioni del report |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "periodo": "ultimi 30gg",
  "trigger": "cadenza_mensile | 2_loss_consecutive_stessa_nicchia",
  "fonte": "agency/reasoning (esito = loss)"
}
```

**Output finale:**
```json
{
  "periodo": "2026-05-22 / 2026-06-22",
  "loss_totali": 7,
  "pattern_significativi": [
    {"categoria": "prezzo", "nicchia": "consulenza", "n": 5,
     "causa_radice": "prezzo percepito alto vs budget", "azione": "A5: obiezioni prezzo + segnala posizionamento a B-003"}
  ],
  "pattern_emergenti": [
    {"categoria": "competitor", "n": 2, "nota": "n < 3 — nessuna conclusione, da osservare"}
  ],
  "handoff": ["A5 (libreria obiezioni)", "08-INTELLIGENCE (HC-AG-IN-01)"],
  "reasoningbank_aggiornato": true
}
```

---

## State

I record di loss vivono in `agency/reasoning`; il report mensile viene archiviato come artefatto
del reparto con `last_updated` per ripartibilità.
- Ripartibilità a freddo: l'aggregazione è ricostruibile in qualsiasi momento dai record (idempotente).
- Il report alimenta il recall di `WF-PREVENTIVO` Step 0 (AG-A3-PROP legge i pattern prima di scrivere).

---

## Failure & recovery

- Loss senza motivo nei record → GATE-DATI segnala: il follow-up non ha chiuso correttamente
  (AG-A3-FUP deve sempre passare i segnali ad AG-A3-LEARN).
- Pattern di prezzo significativo → si segnala a team-prezzi (B-003); il reparto NON cambia i prezzi.
- Campione insufficiente ma richiesta di conclusione → si rifiuta: nessuna conclusione su n < 3.
- 2 loss consecutive stessa nicchia tra una cadenza e l'altra → trigger anticipato immediato.

---

## Connessioni

- [[ag-a3-learn]] · `agenti/ag-a3-learn.md` — owner del workflow
- [[ag-a3-fup]] · `agenti/ag-a3-fup.md` — fornisce gli esiti loss con i segnali
- [[WF-FOLLOWUP-COMMERCIALE]] · `workflow/WF-FOLLOWUP-COMMERCIALE.md` — workflow a monte
- [[state/README]] · `state/README.md` — namespace `agency/reasoning`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A3` — HC-AG-IN-01
