# ADR-012 — Nuovo motore di orchestrazione canonico: `orchestration-layer`

**Data**: 2026-08-26
**Decisione presa da**: Neri (via Emperator Agent), su richiesta esplicita
**Stato**: Attivo — Fase 1 (innesto) completata, Fase 2 (migrazione consumatori) NON iniziata

## Contesto

Neri ha portato un progetto costruito in Antigravity IDE (Gemini), cartella
`C:\Users\olhad\.gemini\antigravity-ide\scratch\token-orchestration\orchestration-layer`:
un control plane di orchestrazione multi-agente production-oriented, W0→W13
(builder swarm, plan memory BM25 citation-first, contratti JSON Schema 2020-12,
adapter Postgres 16 async, governance OPA/Rego default-deny, tool gateway a
grant single-use, bridge RuFlo pinnato `ruflo@3.38.19`, recovery/chaos harness,
API FastAPI + worker durevole, PRR/runbook). 148 test verdi (11 skip = richiedono
Postgres/OPA/RuFlo reali non disponibili in locale).

**ADR-010/ADR-011 già impongono** un solo motore di orchestrazione canonico,
`company/Ecosistemi/11-APEX-7-CORE/`, e **vietano nuove linee divergenti fuori
da quella cartella** (ADR-011 aveva già censito 6 linee parallele come problema,
non 4 come si credeva prima).

## Decisione

Chiesto esplicitamente a Neri come trattare la nuova linea rispetto al canone.
Risposta: **sostituisce il canone** — `orchestration-layer/` diventa il nuovo
motore ufficiale, non un esperimento satellite.

**Eseguito in questa sessione (Fase 1)**:
- Copiato `orchestration-layer/` dentro `company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/`
  (niente storia git da preservare: la cartella sorgente non era un repo git).
- **NON archiviato** il vecchio `orchestrator/ruflo_core.py` + `orchestration/` (bus, dag,
  gates, healing, pipeline, contracts): un primo tentativo di `git mv` in
  `_archivio_orchestration_v1/` ha rotto **7 test** perché `calc/engine.py`,
  `arena_generator.py`, `main.py` e `test_calc.py`/`test_orchestration.py` li importano
  ancora direttamente in produzione. Ripristinato subito (ADR-003: sistema attivo,
  intoccabile finché il sostituto non è validato E i consumatori migrati).
- Trovato e risolto un problema d'ambiente indipendente ma bloccante: un **install pip
  editable globale** di `orchestration-layer` puntava alla cartella scratch originale e
  collideva a livello di nome Python (`orchestrator`) con quello di `11-APEX-7-CORE`,
  rompendo i test del motore attivo su qualunque macchina con quell'editable install.
  Disinstallato (`pip uninstall orchestration-layer`) — non era un pacchetto di produzione,
  solo residuo del build in Antigravity.
- Verificato con esecuzione reale: motore vecchio 92/92 test verdi (invariato), nuovo
  motore 148 test verdi (11 skip) eseguito dentro il repo con `PYTHONPATH=src`.

## Cosa NON è stato fatto (Fase 2, lavoro separato e reale)

- **Nessun consumatore migrato**: `calc/engine.py`, `arena_generator.py`, `main.py`
  continuano a usare il vecchio `orchestrator`/`orchestration`. Il nuovo motore non è
  ancora agganciato a nessun workflow reale della holding (Preventa, Content Factory,
  YouTube, Outreach).
- **RuFlo bridge non certificato in questo ambiente**: richiede `npm install` +
  `npm test` + `npm run certify:smoke` dentro `orchestration-layer/ruflo_bridge/` — non
  eseguito in questa sessione.
- **Nessun credential provider**: il README del progetto stesso dichiara
  `agent_execute` non certificato senza credenziali provider — routing di produzione
  resta disabilitato, `LocalRuntime` attivo.
- **PRR (Production Readiness Review) del progetto stesso è NO_GO**: owner mancanti,
  nessun pentest esterno, nessun KMS/HSM, nessun Postgres 16 reale, nessun failover
  gestito. Questo vale per l'infrastruttura interna del progetto, non solo per
  l'integrazione in Digital Empire.

## Perché non ho fatto la migrazione completa in questa sessione

Rewiring dei 3 consumatori reali (`calc/engine.py`, `arena_generator.py`, `main.py`)
verso contratti/API completamente diversi (da funzioni Python dirette a
workflow-command JSON Schema + gateway OPA) è un lavoro di porting non banale,
non "vedere il layer esistere nel repo". Farlo di corsa avrebbe rischiato di
rompere in silenzio 3 stream di produzione già verificati (CP-20260813-002).

## RIPRESA DA

1. Decidere con Neri/Max l'ordine di migrazione dei 3 consumatori (probabilmente
   `calc/engine.py` prima, è il più piccolo e isolato).
2. Certificare il bridge RuFlo (`npm install --ignore-scripts && npm test` dentro
   `orchestration-layer/ruflo_bridge/`).
3. Solo dopo Fase 2 completa: archiviare `orchestrator/`+`orchestration/` legacy con
   `git mv` (mai cancellare, storia preservata) e chiudere questo ADR come "sostituito
   per intero".

## Collegamenti

- [[ADR-010-fusione-ruflo-apex7]]
- [[ADR-011-quinta-implementazione-apex7]]
- [[ADR-003-migrazione-wrap-non-riscrittura]]
