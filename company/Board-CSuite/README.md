# Board / C-Suite — Digital Empire Group

> **Livello:** L0 — 7 agenti che governano la holding
> **Decisioni:** via hive-mind consensus (raft) per task cross-ecosistema
> **Voto decisivo in stallo:** CEO / Empire-Conductor

## Roster

| Agente | Ruolo | File |
|---|---|---|
| empire-conductor | CEO — orchestratore supremo, consensus, Mandato gate | [CEO-Empire-Conductor.md](CEO-Empire-Conductor.md) |
| empire-coo | COO — operations quotidiane, backbone health, sync | [COO.md](COO.md) |
| empire-cto | CTO — architettura, Platform, Forge, sicurezza | [CTO.md](CTO.md) |
| empire-cmo | CMO — marketing, content, brand voice, APSOC gate | [CMO.md](CMO.md) |
| empire-cro | CRO — revenue, Agency pipeline, InfoBusiness lanci | [CRO.md](CRO.md) |
| empire-cfo | CFO — budget, cost guard, 3-tier routing | [CFO.md](CFO.md) |
| empire-chief-forge | Chief Forge — skill, agenti, team, nuovi ecosistemi | [Chief-Forge.md](Chief-Forge.md) |

## Quando si convoca il Board

- Task tocca 2+ ecosistemi
- Budget > soglia autorizzata
- Conflitto tra ecosistemi
- Proposta di nuovo ADR
- Decisione che modifica il Mandato (LX)

## Come funziona il consenso (raft)

1. CEO propone decisione
2. C-Suite rilevante vota (sì/no/astensione)
3. Maggioranza semplice → decisione adottata
4. Stallo → voto decisivo CEO
5. Decisione → ADR in `Memory/decisions/` + checkpoint STATO-EMPIRE
