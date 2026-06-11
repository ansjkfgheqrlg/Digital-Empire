# Reparto L2.4 — ECOSYSTEM-WORKS (forgia interi ecosistemi)

> **Ecosistema:** 07-FORGE · **Livello:** L2 · **Owner:** Chief-Forge (`frg-chief`) — **solo su mandato Board**
> Workflow L3: `../../Workflow/WF-ECOSYSTEM-NEW/`

## Cosa fa

ECOSYSTEM-WORKS è il livello massimo della forgiatura: crea **interi ecosistemi L1**
(business unit complete) quando la holding entra in un nuovo territorio — es. F9+:
E-commerce. È il reparto che rende vera la premessa del Piano Maestro: *"il piano è
la micro-base — la FORGE può creare nuovi ecosistemi senza toccare l'architettura"*.

Output di una forgiatura d'ecosistema (tutto o niente):
- **Org completa L2→L5**: reparti, workflow, funzioni, roster agenti con tier
- **ECOSISTEMA.md + BACKBONE.md** (topologia swarm, namespace memoria, handoff con gli altri 9)
- **Dossier PIANO-MAESTRO** nuovo (proposto alla Board, che lo ratifica)
- **Namespace memoria dedicato** (`ruflo memory init --namespace <eco>`)
- **Registrazione**: roster in Identity-HR, skill in skills-map, evento costo a OPERATIONS

## Come si collega

| Con | Relazione |
|---|---|
| LX / Board (L0) | UNICO committente valido: il mandato per un ecosistema nuovo arriva via hive-mind consensus (raft); Chief-Forge propone, il Board approva |
| AGENT-WORKS | fornisce i roster L5 e i team canonici dell'ecosistema nuovo |
| SKILL-WORKS | forgia le skill proprie dell'ecosistema (o mappa quelle esistenti) |
| WORKFLOW-WORKS | il dossier dell'ecosistema nasce come MKD/PRD tipo A (Enterprise) |
| INTELLIGENCE | ricerca di mercato pre-mandato (WF-TREND, WF-COMPETITOR): un ecosistema senza dati di mercato non si propone |
| OPERATIONS | business case con budget: costo di run stimato dell'ecosistema PRIMA dello scaffold |
| 10 MEMORY | la decisione di creare l'ecosistema diventa ADR in `company/Memory/decisions/` |

Funzioni L4: riusa `../../Funzioni/T-org-design/`, `../../Funzioni/T-handoff-contracts/`,
`../../Funzioni/T-shared-state-schema/` (di AGENT-WORKS — stessa meccanica, scala maggiore).
Skill da forgiare a supporto: `ecosystem-scaffold` (genera struttura L2-L5 + BACKBONE.md
da template — priorità ALTA).

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** SOLO mandato Board (L0) ratificato via consensus. Nessun ecosistema
nasce da iniziativa di un singolo agente o reparto. Fase di roadmap: F9+ (il primo
dry-run previsto è l'ecosistema E-commerce — fase build F5 della FORGE).

**Ragionamento:**
1. **Il mandato è completo?** — missione, revenue model, DONE WHEN, budget, sponsor
   C-Suite. Mandato incompleto → respinto a Board con richiesta di integrazione.
2. **Ricerca prima del disegno** — dossier INTELLIGENCE (mercato, competitor, trend)
   come input obbligatorio; un ecosistema è una scommessa di business, non un esercizio.
3. **Copiare il modello, non reinventarlo** — la struttura segue questo stesso scheletro
   (ECOSISTEMA.md, BACKBONE.md, Reparti/, Workflow/, Funzioni/, Agenti/) e i 13 pattern;
   ciò che cambia è il contenuto, mai la forma.
4. **Confini espliciti con gli altri 9** — per ogni ecosistema esistente: cosa riceve,
   cosa fornisce, cosa NON fa (anti-overlap). Senza matrice di confine → non si scaffolda.
5. **Dry-run prima del via** — lo scaffold completo si valida a vuoto (struttura
   navigabile, handoff coerenti, verify verde) prima di spawnare il primo agente reale.
6. **Tutto o niente** — un ecosistema mezzo-scaffoldato non si consegna: o tutti i
   deliverable della lista in "Cosa fa", o rollback.

**Anti-pattern vietati:** ecosistemi creati per entusiasmo senza mandato; scaffold senza
dossier di mercato; divergenza dal template (ogni ecosistema con struttura diversa =
drift architetturale, intervento Drift-Sentinel).

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 ECOSYSTEM-WORKS · Aggiornato: 2026-06-11*
