---
Type: WORKFLOW
Status: Active
Tags: #workflow #cro #deal #pipeline #preventivo #chiusura
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-DEAL — Pipeline Deal Agency (Lead → Contratto → Handoff Delivery)

> **ID:** WF-CRO-001 · **Owner:** `cro-conductor` · **Blueprint:** `BP-CRO.md`
> **Trigger:** lead qualificato in stadio "risposta positiva" da A2-Acquisizione

---

## Scopo

Portare ogni opportunità qualificata dall'ingresso nel radar CRO fino alla firma del contratto
e al passaggio strutturato alla delivery, assicurando che ogni step sia presidiato da un agente
dedicato con gate bloccante prima del passaggio al passo successivo.

---

## Attori

| Step | Agente CRO | Agente Agency |
|---|---|---|
| Trigger | `cro-conductor` | A2-BOOK (booking coordinator) |
| Struttura offerta | `cro-deal-desk` | A3-BRIEF + A3-AUDIT |
| Pricing check | `cro-pricing-arbiter` | A3-PRICE |
| Pipeline tracking | `cro-agency-pipeline` | — |
| Chiusura e firma | — | A8-Closing (Max umano) |
| Handoff delivery | `cro-conductor` | HC-AG-AM-01 ad A7 |
| Archivio | `cro-memoria` | A3-LEARN |

---

## Flusso passo-passo

```
[TRIGGER]
Lead "risposta positiva" da A2 → HC-AG-CL-01 ad A8-Closing
         │
         ▼
[STEP 1] cro-agency-pipeline
  → aggiorna snapshot pipeline: lead avanza a stadio "discovery"
  → check SLA: discovery call entro 48h da risposta positiva?
  → GATE: slot discovery call confermato → prosegui; non confermato → alert conductor
         │
         ▼
[STEP 2] Discovery call (MAX umano) + A3-BRIEF
  → Max conduce la call; A3-BRIEF produce brief strutturato entro 4h
  → brief JSON: problema, awareness, stack, budget, ambiente server
         │
         ▼
[STEP 3] cro-deal-desk (struttura offerta)
  → legge il brief; seleziona prodotto/bundle dal catalogo
  → verifica prerequisiti ambiente; identifica scope 7gg
  → produce bozza offerta con pricing da catalogo
  → GATE: brief completo (nessun campo vuoto) → prosegui; incompleto → ritorna ad A3-BRIEF
         │
         ▼
[STEP 4] cro-pricing-arbiter (verifica prezzo)
  → prezzo proposto = catalogo? (Mandato Art.3)
  → se sì: PASS immediato
  → se no: BLOCCA, istruttoria B-003 → lotto MAXIMILIAN/CEO
  → GATE: pricing autorizzato → prosegui; variazione: attendi ok lotto
         │
         ▼
[STEP 5] A3-PROP (preventivo problem-first) + Gate Preventivo
  → A3 scrive il preventivo con struttura problem-first
  → cro-deal-desk esegue proposal-gate (8 check bloccanti)
  → GATE: PASS → invia; FAIL → ritorna ad A3-PROP per correzione
         │
         ▼
[STEP 6] Preventivo inviato → follow-up 10gg (A3-FUP)
  → 3 touch: D+3, D+7, D+10
  → cro-agency-pipeline monitora giorni in stadio "preventivo inviato"
  → GATE: risposta entro 10gg → prosegui; silenzio dopo D+10 → chiusura "loss" + motivo registrato
         │
         ▼
[STEP 7] Call di chiusura (MAX umano) + A8-Closing
  → A8-PREP prepara dossier Max ≥2h prima della call
  → Call: Max chiude o perde
  → A8-DEBRIEF raccoglie esito + motivi entro 2h dalla call
         │
   ┌─────┴─────┐
  WIN         LOSS
   │           │
   ▼           ▼
[STEP 8a]   [STEP 8b]
Contratto   Loss registrato
firmato +   cro-memoria
pagamento   (motivo, prodotto,
one-time    canale, stadio uscita)
   │
   ▼
[STEP 9] Handoff delivery
  → HC-AG-AM-01 ad A7-Account Mgmt (profilo cliente, prodotto, contatti)
  → cro-conductor aggiorna pipeline: deal "chiuso/vinto"
  → cro-memoria archivia deal: win + leva principale
```

---

## Gate bloccanti

| Gate | Condizione PASS | Blocca |
|---|---|---|
| G1 — Slot discovery | Slot confermato entro 48h | `cro-agency-pipeline` alert |
| G2 — Brief completo | Tutti i campi JSON popolati | `cro-deal-desk` ritorna a A3 |
| G3 — Pricing autorizzato | Prezzo = catalogo O ok lotto | `cro-pricing-arbiter` blocca |
| G4 — Proposal-gate | 8/8 check superati | `cro-deal-desk` FAIL → riscrittura |
| G5 — Follow-up completato | 3 touch inviati O risposta ricevuta | A3-FUP + pipeline monitor |
| G6 — Debrief call | Esito + motivi entro 2h | A8-DEBRIEF obbligatorio |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "lead_id": "L-001",
  "stadio_ingresso": "risposta_positiva",
  "canale": "email | linkedin | instagram | referral",
  "fonte": "A2-BOOK"
}
```

**Output finale (win):**
```json
{
  "deal_id": "DEAL-001",
  "esito": "win",
  "prodotto": "Outreach Factory",
  "prezzo": 4000,
  "data_firma": "2026-06-17",
  "handoff_delivery": "HC-AG-AM-01",
  "leva_win": "pricing ok + problema ben qualificato",
  "durata_ciclo_gg": 14
}
```

**Output finale (loss):**
```json
{
  "deal_id": "DEAL-001",
  "esito": "loss",
  "stadio_uscita": "preventivo_inviato",
  "motivo_loss": "budget insufficiente per Engine Room; non disposto a scendere a singolo prodotto",
  "durata_ciclo_gg": 12
}
```

---

## State

File: `board/cro/pipeline/deals-active.json`
- Ogni deal in corso: id, stadio attuale, data ingresso stadio, agente responsabile.
- Aggiornato ad ogni transizione di stadio.
- Archiviato in `board/cro/deals/` dopo chiusura (win o loss).

---

## Connessioni

- [[cro-conductor]] · `agenti/cro-conductor.md`
- [[cro-deal-desk]] · `agenti/cro-deal-desk.md`
- [[cro-pricing-arbiter]] · `agenti/cro-pricing-arbiter.md`
- [[cro-agency-pipeline]] · `agenti/cro-agency-pipeline.md`
- [[cro-memoria]] · `agenti/cro-memoria.md`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md` §A3, A8
- [[WF-PRICING]] · `workflow/WF-PRICING.md`
