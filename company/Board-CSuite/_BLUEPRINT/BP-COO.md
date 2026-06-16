# BLUEPRINT — COO (figura C-level = workflow CF-grade)

> Prodotto da ARCHITETTURA (WF-ARCH-DESIGN, ARCH-BOARD-20260616). Per FORGE. Forma: cartella-workflow (PESANTE).

## Forma scelta + perché
Le operations della holding non sono un ruolo: sono un sistema che monitora backbone, sync, runtime,
SLA, incidenti. Serve un team con monitor always-on + ottimizzatori → cartella-workflow ≥10 agenti.

## Missione della figura
Far girare la macchina ogni giorno: salute del Backbone (BUS/BRAIN), sync Max↔Gael, runtime swarm/cron
(via ecosistema 09-OPERATIONS), SLA, gestione incidenti, ritmo operativo. NON decide COSA produrre (CEO/CRO),
presidia COME gira.

## Struttura cartella (FORGE)
```
Board-CSuite/COO/  ├── README.md ARCHITETTURA.md ├── agenti/(10) principi/ regole/ skills/ scripts/ workflow/(≥2) kpi/ state/
```

## Roster agenti (10)
| Agente | Ruolo | Tier |
|---|---|---|
| coo-conductor | coordina le operations, riporta al CEO | opus |
| coo-backbone-health | monitor BUS/BRAIN/handoff (always-on) | sonnet |
| coo-sync-keeper | sync repo Max↔Gael, anti-collisione, STATO aggiornato | sonnet |
| coo-runtime-marshal | orchestra swarm/cron via 09-OPERATIONS | sonnet |
| coo-sla-tracker | SLA per ecosistema, ritardi | haiku |
| coo-incident-handler | gestisce run fallite, daemon zombie, escalation | sonnet |
| coo-process-optimizer | rimuove colli di bottiglia ricorrenti | sonnet |
| coo-handoff-auditor | verifica i contratti HC tra ecosistemi | haiku |
| coo-cadence-keeper | ritmi operativi, standup, review settimanali | haiku |
| coo-memoria | storico incidenti, pattern operativi | haiku |

## Workflow CF-grade (≥2)
- `WF-OPS-DAILY` — health check backbone + run schedulate + sync → report stato in 30s al CEO.
- `WF-INCIDENT` — rilevazione → triage → contromisura → post-mortem in ReasoningBank.
- `WF-HANDOFF-AUDIT` — campiona i contratti HC tra ecosistemi, segnala rotture.

## Skill proprie (FORGE)
`ops-dashboard` (stato holding in 30s) · `incident-runbook` · `handoff-validator`.

## Handoff
← tutti gli ecosistemi (stato run/HC). → **CEO** (report stato), → **CFO** (eventi costo run), → **09-OPERATIONS** (esecuzione). ← **CTO** (salute tecnica).

## KPI presidiati
Run schedulate completate senza intervento ≥95% · tempo rilevazione incidente ≤15min · 0 collisioni sync · HC rotti aperti.

## Struct-gate checklist
- [ ] ≥10 agenti · [ ] ≥2 workflow · [ ] principi/regole · [ ] ≥3 skill · [ ] scripts · [ ] kpi/state · [ ] 0 magri/0 vuote

## Note per la FORGE
Base dal v1 `COO.md` (operations, backbone health, sync). Collegare a 09-OPERATIONS (runtime reale) e al sync hook esistente.

## Connessioni
- [[BP-INDEX]] · [[BP-CEO]] · [[BP-CFO]] · [[14-DOSSIER-ARCHITETTURA]]
