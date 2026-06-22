---
Type: SKILLS
Status: Active
Tags: #skills #lanci #campagne #launch #infobusiness #IB-L2-LANC
Created: 2026-06-21
Last updated: 2026-06-21
---

# Skill — IB-L2-LANC Lanci & Campagne

> Mappa delle skill del reparto: skill proprie da forgiare + skill esistenti mappate.

---

## Skill proprie del reparto (da forgiare via 07-FORGE — standard §8 V2)

### `launch-runbook` — Priorità P0

**Funzione:** genera il calendario T-30→T+7 deterministico + checklist gate per ogni step del
lancio. Formalizza la logica di IB-LANC-PLANNER (timeline) e di IB-COORD-LANCI (sequenza gate).
Rende riproducibile l'intero scheletro del lancio prima della compilazione dei contenuti.

**Quando invocarla:** quando un prodotto a gate PASS con budget approvato entra in IB-L2-LANC e
IB-COORD-LANCI deve impostare il calendario completo del lancio.

**Input:** `{lancio_id, prodotto, data_cart_open, durata_cart_giorni, webinar, owner_map, budget_OPS}`
**Output:** `calendario.md` (timeline con owner + dipendenze) + scheletro `state.json` con gate per step
+ checklist per ogni gate (APSOC, asset-complete, dry-run, go/no-go).

**Dipendenze:** richiede prerequisiti R1 (prodotto a gate PASS + budget approvato) verificati prima.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro `launch`
(skill esistente mappata qui).

---

### `launch-debrief-distiller` — Priorità P2

**Funzione:** esegue il post-mortem strutturato: piano vs reale per KPI, root cause degli scarti
≥10%, distillazione di ≥3 pattern validati per `reasoningbank/`. Formalizza la logica di
IB-LANC-DEBRIEF in WF-DEBRIEF-LANCIO e prepara l'input di WF-FOLLOWUP-COPY (top copy).

**Quando invocarla:** a cart close completato, entro T+7, su un lancio con tracking reale disponibile.

**Input:** `{lancio_id, calendario.md, tracking_reale, dry-run.md, costo_reale}`
**Output:** `debrief.md` con piano vs reale + root cause + ≥3 pattern per ReasoningBank + top 3 email
/ top 3 hook (con metriche reali) come handoff a WF-FOLLOWUP-COPY.

**Dipendenze:** richiede tracking reale post cart close; non si invoca su lancio non chiuso.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro `emails`
(skill esistente mappata qui).

---

## Skill esistenti mappate a IB-L2-LANC

| Skill | Stato | Ruolo in IB-L2-LANC | Note |
|---|---|---|---|
| `launch` | Esistente, mappata | Playbook lancio per IB-COORD-LANCI e IB-LANC-PLANNER | `launch-runbook` implementa/estende questa skill; no doppio standard |
| `market-launch` | Esistente, mappata | Orchestrazione lancio lato MK per IB-LANC-COPY-LIAISON | Ausiliaria: copre il lato 04-MARKETING dell'handoff HC-IB-MK-01 |
| `emails` | Esistente, mappata | Supervisione sequenze cart open/close per IB-LANC-COPY-LIAISON | Ausiliaria; il copy resta prodotto da 04-MARKETING (R2) |
| `cro-copy-architect` | Esistente, mappata | Riferimento APSOC per il gate IB-LANC-QA | Per audit/gate, non per scrittura: QA non suggerisce copy (R4) |
| `market-launch` (gate) | Esistente | Pattern lancio storici come knowledge base | Knowledge base, non motore del workflow IB-L2-LANC |

---

## Regola anti-contraddizione

Prima di forgiare `launch-runbook` e `launch-debrief-distiller`:
1. Eseguire `skill-contradiction-analyzer` contro `launch`, `market-launch`, `emails`, `cro-copy-architect`.
2. Se sovrapposizione rilevata: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce.
3. Gerarchia: skill nuova = motore; skill esistente = ausiliaria o knowledge base.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-LANC — skill area
- [[WF-LANCIO]] · `workflow/WF-LANCIO.md` — workflow che usa `launch-runbook`
- [[IB-LANC-DEBRIEF]] · `agenti/IB-LANC-DEBRIEF.md` — owner di `launch-debrief-distiller`
- [[ARCHITETTURA]] · `ARCHITETTURA.md` §Skill del reparto — mapping skill holding
