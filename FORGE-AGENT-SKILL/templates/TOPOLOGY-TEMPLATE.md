---
intestazione_adr008: { proprietario: FORGE-AGENT-SKILL (06b-FORGE, via fas-conductor), controllore: fas-qa-gate (checklist p.1) + METHOD-GUARD, origine: FORGE — MIR-9 dossier 18 (2026-07-20, CP-20260720-013), governo: ADR-001/002/006/008 }
---

# TOPOLOGY-TEMPLATE — il file `topology.md` obbligatorio di OGNI team forgiato (MIR-9)

Quando il deliverable di WF-AGENT-NEW è un **team (≥2 agenti coordinati)**, la cartella del team
deve contenere `topology.md` compilato da questo template. Regola R2-bis: team senza topology.md
= FAIL al gate (come un agente senza memory/).

**Filosofia:** la topologia è UNA pagina (puntatori, non contenuto — pattern INDEX).
Se il grafo non sta in una pagina chiara, la topologia è troppo complessa → anti-pattern:
ridurre i nodi o spezzare in due team con un contratto tra loro.

---

## 1. Tipo di topologia
`[ hier | pipeline | mesh | queen-swarm ]` — sceglierne UNA e scrivere in 1 riga **perché questa
e non le altre** (es. "pipeline: output di A è input di B, niente orchestrazione continua").
Anti-pattern: mesh senza bisogno (ogni nodo parla con tutti = nessuno è responsabile di niente).

## 2. Nodi (gli agenti) — tabella
| # | Agente | Ruolo (1 riga) | Spec (7-file) | Ecosistema owner |
|---|---|---|---|---|
| N1 | slug-nome | cosa fa, per chi | `percorso/spec.md` | 0X-DEP |

Vincolo: **ogni nodo DEVE esistere** come agente 7-file (R2). Nodi evocati nella mappa ma mai
costruiti = agenti fantasma = FAIL gate.

## 3. Entry point & trigger
Chi invoca il team, quando, con quale input (una riga + esempio se serve).

## 4. Edges / handoff — tabella dei contratti
| Da → A | Contratto (input atteso → output promesso) | Quando avviene |
|---|---|---|
| N1 → N2 | MKD → bozza | dopo step 3 |
| N2 → N3 | v0.9 → verbale PASS/FAIL | a build chiusa |

Regola: ogni handoff dichiara il contratto ESATTO (cosa passa, non "ci si aggiorna").
Handoff senza contratto = il punto dove i team muoiono (lezione impero).

## 5. Escalation & failure path
FAIL×2 stesso difetto → conductor del team decide (fix rapido vs ADR vs stop) → se irrisolto: Max.
Ogni nodo dichiara come fallisce (R3: failure-modes.md del nodo, richiamato qui solo per puntatore).

## 6. Memory touchpoints (ADR-002)
Quali file di memoria ogni nodo LEGGE prima e SCRIVE dopo (es. `memory/plans/`, REGISTRO-ERRORI,
checkpoint). Team che non lascia tracce = team che non impara (invariante 1: memory-first dal passo zero).

## 7. Observability
Come si vede cosa è successo dopo un run: verbali gate, CP globali, trace/log minimi.

## 8. Kill-criteria / sunsetting
Quando questo team smette di esistere (es. output sostituito, 30 giorni di inattività → review Max).
Niente team zombie nel reparto (regola impero: mai workflow orfani — ADR-008).

## 9. Schema (ASCII o mermaid, facoltativo ma consigliato)
```
[richiedente] → N0 conductor → N1 smith ⤳ N2 gate ⤳ registrazione → [consegna]
                      ↑______FAIL×2______|
```

---
*Esempio compilato di riferimento: `FORGE-AGENT-SKILL/TOPOLOGY.md` (topologia del reparto stesso,
dogfooding — il reparto è il primo team dell'impero con topology.md pubblica).*
