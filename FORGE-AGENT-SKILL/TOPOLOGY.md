---
intestazione_adr008: { proprietario: FORGE-AGENT-SKILL (06b-FORGE), controllore: fas-qa-gate + METHOD-GUARD, origine: FORGE — MIR-9 dogfooding (2026-07-20, CP-20260720-013), governo: ADR-001/002/006/008/009 }
---

# TOPOLOGY — Reparto FORGE-AGENT-SKILL (v1, 2026-07-20)
*Primo team dell'impero con topology.md pubblica: dogfooding della regola MIR-9.
Ogni team futuro forgiato dal reparto compila il proprio da `templates/TOPOLOGY-TEMPLATE.md`.*

## 1. Tipo
**pipeline con gate finale** (hier-lite): il conductor orchestra a monte, gli smith costruiscono
in sequenza, il qa-gate chiude a valle. Non mesh: nessun nodo parla lateralmente senza passare
dal conductor (una sola responsabilità per edge). Non queen-swarm: build artigianali ≤4 pezzi,
niente raccoglitori paralleli continui.

## 2. Nodi
| # | Agente | Ruolo | Spec | Owner |
|---|---|---|---|---|
| N0 | **fas-conductor** | intake, RECALL, FORGE-PLAN, sezione `## ASK` (MIR-3), registrazione ADR-008, handoff | `agents/fas-conductor/` | 06b-FORGE L2.1/L2.2 |
| N1 | **fas-skill-smith** | forge skill: MKD → kernel ≤550r + references + evals (criterio skill-creator) | `agents/fas-skill-smith/` | 06b-FORGE L2.1 |
| N2 | **fas-agent-smith** | forge agenti: MKD → 7 file canonici (R2), write-early | `agents/fas-agent-smith/` | 06b-FORGE L2.2 |
| N3 | **fas-qa-gate** | verifica indipendente: checklist 7 punti bloccante, verbale | `agents/fas-qa-gate/spec.md` | 06b-FORGE L2.5 (METHOD-GUARD) |

## 3. Entry point
Richiesta capability da ecosistema/Max ("ci serve agente/skill X") → N0 intake+RECALL
(skills-map + REGISTRO: niente duplicati — kill-criteria WF-AGENT-NEW).

## 4. Edges / contratti
| Da → A | Contratto | Quando |
|---|---|---|
| richiedente → N0 | brief/sorgente → richiesta validata o rifiutata con motivo (RECALL) | intake |
| N0 → N1/N2 | FORGE-PLAN (`memory/plans/`, sezione `## ASK` compilata) + MKD (`memory/mkd/`, coverage ≥95%) | dopo PLAN+ASK |
| N1/N2 → N3 | cartella deliverable completa (7-file o skill formato completo) + segnalazione `0.9` | a build chiusa + self-review |
| N3 → N0 | verbale PASS/FAIL (`memory/checkpoints/GATE-<slug>-<data>.md`) con elenco difetti | gate |
| N3(FAIL) → N1/N2 | ritorno con lista difetti (max 2 giri, poi escalation) | gate FAIL |
| N0 → richiedente | artefatto registrato (REGISTRO+skills-map) + nota retro | consegna |

## 5. Escalation & failure
- Gate FAIL×2 stesso difetto → N0 decide (fix rapido vs ADR vs stop) → irrisolto: Max.
- Ogni nodo ha failure-modes propri (R3). Anti-recidiva: stessa causa 2 volte → nuova regola in `rules/`
  (protocollo Ispettorato, dossier 15 — ora anche REGISTRO-SUCCESSI per ciò che funziona).

## 6. Memory touchpoints (ADR-002)
Legge PRIMA: `memory/INDEX.md` (backlog+priorità), `company/Memory/INDEX.md` + STATO-EMPIRE (Regola Zero),
skills-map/REGISTRO (anti-duplicati). Scrive DOPO: `memory/plans/`, `memory/mkd/`, `memory/checkpoints/`,
`memory/INDEX.md`, REGISTRO-IMPRESA, skills-map, CP globale in `company/Memory/checkpoints/`.

## 7. Observability
Verbali GATE in `memory/checkpoints/` + CP globali giornata (`company/Memory/checkpoints/CP-*`) +
skills-map versionata = cronologia completa di cosa è uscito dal reparto e con quale esito.

## 8. Kill-criteria
30 giorni senza artefatti registrati → review Max (fondere? ridurre roster?).
Se un output migliore nasce fuori dal reparto con lo stesso scopo → wrap ADR-003 dell'esterno, mai rebuild.

## 9. Schema
```
[richiedente] → N0 conductor ─PLAN+MKD─→ N1 skill-smith ─┐
                       │ (RECALL/ASK)    N2 agent-smith ├─v0.9→ N3 qa-gate ─PASS→ registrazione → [consegna]
                       ↑_______________ FAIL (max 2 giri) _|                        ↗ verbale in memory/
```
