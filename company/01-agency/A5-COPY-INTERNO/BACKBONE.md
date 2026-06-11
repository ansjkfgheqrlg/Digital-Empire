# BACKBONE — A5 COPY INTERNO

> Reparto L2 di 01-AGENCY. Schema canonico: coordinator, I/O, acceptance_criteria, failure_handling, shared_state.

## Coordinator

**AG-A5-COORD** (sonnet) — orchestratore reparto.
Responsabilita': copy operativo quotidiano (template email/DM, micro-copy preventivi, script call).
I pezzi grandi (sales page, sequenze lunghe) si chiedono a 04-MARKETING via HC-AG-MK-01.

## Team L3 / L4

| ID | Livello | Tipo | Flusso |
|---|---|---|---|
| WF-COPY-OUTREACH | L3 | workflow | analisi reply reali -> varianti APSOC -> gate Bibbia -> rollout graduale |
| T-apsoc-writer | L4 | worker (sonnet) | scrittura/variazione copy (skill cro-copy-architect, market-copy) |
| T-objection-handler | L4 | worker (sonnet) | libreria obiezioni reali (da HC-AG-IN-01) -> risposte testate |
| T-copy-qa | L4 | worker (sonnet) | Gate Bibbia (bibbia_team.py riusato — pattern 6: una skill, molti reparti) |

## I/O

**Input:**
- Dati performance template (reply rate, positive reply rate) da agency/outreach
- Obiezioni reali dalle conversazioni (da agency/conversations via A2)
- Dati campo (obiezioni, domande ricorrenti) da 08-INTELLIGENCE via HC-AG-IN-01

**Output:**
- Template refreshati -> A2 (rollout graduale)
- Libreria obiezioni aggiornata -> agency/outreach
- Copy micro (preventivi, script) -> A3

## Acceptance Criteria

- Ogni output DEVE passare Gate Bibbia prima del rilascio
- Claim verificabili: solo "prove non promesse" (Mandato Empire)
- Framework APSOC applicato (Attenzione->Problema->Soluzione->Obiezioni->CTA)
- Score APSOC >= 80/100 (sales page >= 85)
- CTA standard: presentazione-empire.vercel.app

## Failure Handling

| Failure | Azione |
|---|---|
| Gate Bibbia FAIL | Rework; log motivo; aggiorna linee guida writer |
| Reply rate cala dopo rollout | Rollback al template precedente (graduale!); log come esperimento fallito |
| Obiezione non in libreria | Aggiungi a T-objection-handler; richiedi caso reale da A2 |

## Asset esistenti

| Path | Team |
|---|---|
| Skill `cro-copy-architect` (APSOC) | T-apsoc-writer |
| Skill `cold-email` | T-apsoc-writer (email) |
| Suite `market-*` (15 skill) | T-apsoc-writer |
| `bibbia_team.py` (esistente in Outreach) | T-copy-qa |

## Connessioni

- `A2-ACQUISIZIONE/BACKBONE.md` — consegna template refreshati
- `A3-PREVENTIVI/BACKBONE.md` — micro-copy preventivi
- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` sez. 2 (A5)
