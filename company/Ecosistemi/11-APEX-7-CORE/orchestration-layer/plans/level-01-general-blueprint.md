# LIVELLO 1/7 — Piano generale di costruzione dell’Orchestration Layer

**Versione:** 1.0.0  
**Stato:** PROPOSTO — attende approvazione  
**Natura:** blueprint generale, volutamente non definitivo  
**Vincolo:** il Livello 2 sarà una riscrittura migliorativa completa, non un’appendice.

---

## 1. Critica iniziale del brief

Questa sezione espone valutazioni verificabili, non ragionamenti privati.

| Osservazione | Rischio | Risposta del piano L1 |
|---|---|---|
| “Tantissimi agenti” non equivale a qualità | costo, latenza, conflitti | team minimo iniziale; espansione solo su evidenza |
| “Flusso di pensieri” può diventare una catena opaca | decisioni non auditabili | usare un **Decision Protocol** con input, opzioni, evidenze e verdetto |
| Memoria senza confini diventa accumulo | dati obsoleti, privacy, rumore | memoria a livelli con TTL, versioni e ownership |
| Auto-miglioramento autonomo è pericoloso | regressioni e deriva | proposte in shadow mode; promozione umana |
| RuFlo cambia rapidamente | lock-in e API instabili | integrazione tramite adapter sostituibile |
| Costruire tutto subito impedisce il controllo | sistema non testabile | vertical slice prima dell’espansione |

**Verdetto:** prima si costruisce il sistema che costruisce e verifica l’Orchestration Layer; poi si implementa l’Orchestration Layer stesso.

---

## 2. Visione

L’Orchestration Layer è il sistema nervoso operativo tra intenzione e azione:

```text
Intento utente
  → interpretazione e classificazione del rischio
  → pianificazione verificabile
  → validazione policy/security/quality
  → delega ad agenti e skill
  → esecuzione controllata
  → osservazione e gestione errori
  → memoria e apprendimento supervisionato
  → risposta finale token-efficiente
```

Non contiene logica di dominio specifica. Coordina capacità esterne tramite contratti stabili.

---

## 3. Obiettivi e priorità

| Priorità | Obiettivo | Risultato atteso |
|---:|---|---|
| P0 | Sicurezza e controllo | nessuna azione critica senza policy e autorizzazione |
| P0 | Stato consistente | workflow ripristinabili, side effect idempotenti |
| P0 | Auditabilità | ogni decisione operativa ha identità, causa ed evidenza |
| P1 | Qualità | gate oggettivi prima di avanzamento o rilascio |
| P1 | Resilienza | timeout, retry selettivi, circuit breaker, compensazione |
| P1 | Modularità | RuFlo, provider LLM, broker e storage sostituibili |
| P2 | Efficienza | budget per token, costo, tempo e concorrenza |
| P2 | Adattamento | routing e strategie migliorabili senza auto-modifica incontrollata |

### Non-obiettivi della prima release

- autonomia senza limiti;
- decine di agenti sempre attivi;
- “exactly once” distribuito promesso senza prove;
- auto-modifica di sicurezza, schema o workflow attivo;
- supporto multi-region prima della stabilità single-region.

---

## 4. Principi costituzionali

1. **Deterministic core, probabilistic edge:** stato e policy sono deterministici; gli LLM propongono.
2. **Validate by risk:** i controlli crescono con l’impatto dell’azione.
3. **Evidence over confidence:** nessun PASS senza prova.
4. **Least privilege:** agente e skill ricevono solo capacità necessarie.
5. **Idempotency before retry:** nessun retry su side effect non protetto.
6. **Fail explicit:** errore = codice, causa, impatto, recovery, owner.
7. **Compensate or stop:** mai continuare da uno stato incoerente.
8. **Memory is governed:** ogni ricordo ha fonte, validità, accesso e ciclo di vita.
9. **Minimal effective swarm:** si usa il minor numero di agenti che supera il benchmark.
10. **Human sovereignty:** override e arresto umano sempre disponibili per azioni critiche.
11. **Replaceable infrastructure:** il dominio non dipende direttamente da RuFlo o da un provider.
12. **Token economy after correctness:** NERVE-SAVE comprime solo dopo verifica di sicurezza e completezza.

---

## 5. Fase 1 — Team che costruisce l’Orchestration Layer

Il primo artefatto è un **Builder Swarm controllato**, non l’intero runtime.

| Agente | Responsabilità unica | Deliverable | Non può |
|---|---|---|---|
| BUILD-LEAD | coordina backlog, dipendenze e gate | piano di incremento | approvare il proprio lavoro |
| ARCHITECT | definisce componenti e contratti | ADR, diagrammi, interfacce | implementare policy di comodo |
| RUFLO-SCOUT | verifica capacità reali RuFlo | capability matrix e smoke test | inventare API |
| IMPLEMENTER | produce vertical slice | codice e migrazioni | cambiare architettura senza ADR |
| TESTER | crea test e failure injection | suite e risultati | abbassare soglie per far passare test |
| SECURITY | threat model e policy | controlli, findings, sign-off | essere bypassato su azioni critiche |
| GATEKEEPER | valuta evidenze indipendenti | gate report PASS/FAIL | correggere direttamente il proprio oggetto di valutazione |

### Protocollo del Builder Swarm

```text
BUILD-LEAD assegna
  → ARCHITECT specifica
  → RUFLO-SCOUT verifica dipendenze
  → IMPLEMENTER costruisce
  → TESTER + SECURITY valutano in parallelo
  → GATEKEEPER emette verdetto
  → PASS: checkpoint; FAIL: remediation limitata; 3 FAIL: escalation umana
```

---

## 6. Ecosistemi interni dell’Orchestration Layer

| Ecosistema | Funzione | Componenti principali |
|---|---|---|
| Governance | regole e autorizzazioni | policy engine, risk classifier, approval gate |
| Cognitivo | interpretazione e pianificazione | intent parser, planner, critic, decision protocol |
| Esecuzione | gestione workflow e agenti | state machine, scheduler, task router, agent registry |
| Azioni | uso sicuro delle skill | tool gateway, sandbox, capability tokens |
| Memoria | stato e conoscenza | working memory, episodic log, semantic store, archive |
| Qualità | verifica degli output | schema validator, quality gates, NERVE-SAVE |
| Resilienza | contenimento dei guasti | timeout, retry, breaker, compensation, DLQ |
| Osservabilità | comprensione del runtime | logs, metrics, traces, audit records |
| Evoluzione | miglioramento supervisionato | experiment registry, benchmark, change proposals |

---

## 7. Flusso di mentalità

Definisce **come il sistema si comporta sempre**, indipendentemente dal task:

```text
1. Prudenza: assumere input incompleto e servizi fallibili.
2. Chiarezza: separare fatto, ipotesi, decisione e rischio.
3. Proporzionalità: controllo e costo commisurati all’impatto.
4. Reversibilità: preferire azioni annullabili e checkpoint.
5. Evidenza: richiedere prove prima di promuovere stato o strategia.
6. Economia: usare agenti, token e tool solo se aggiungono valore misurabile.
7. Apprendimento controllato: registrare esiti; non auto-modificarsi in produzione.
```

---

## 8. Protocollo di ragionamento osservabile

Non registra monologhi interni. Produce un **Decision Record** compatto e auditabile:

1. **Frame:** obiettivo, vincoli, dati mancanti, classe di rischio.
2. **Recall:** precedenti rilevanti con fonte e validità.
3. **Options:** massimo tre strategie realmente diverse.
4. **Evaluate:** impatto, costo, reversibilità, sicurezza, evidenze.
5. **Select:** decisione e motivazione sintetica.
6. **Plan:** step, owner, dipendenze, criteri di completamento.
7. **Challenge:** critic indipendente cerca failure mode e assunti falsi.
8. **Gate:** policy/security/quality decidono PASS, REMEDIATE o ESCALATE.
9. **Execute:** task autorizzati entro budget e timeout.
10. **Observe:** risultati, errori e side effect.
11. **Learn:** memoria aggiornata con esito e confidence.
12. **Compress:** NERVE-SAVE prepara l’output finale senza eliminare dati necessari.

### Decision Record minimo

```json
{
  "decision_id": "DEC-uuid",
  "goal": "string",
  "risk_class": "R0|R1|R2|R3",
  "facts": [],
  "assumptions": [],
  "options": [],
  "selected": "string",
  "evidence": [],
  "expected_result": "string",
  "rollback": "string|null",
  "approvals": [],
  "status": "PROPOSED|APPROVED|REJECTED|EXECUTED"
}
```

---

## 9. Agenti mentali del runtime

| Agente | Ruolo mentale | Input | Output |
|---|---|---|---|
| INTENT | comprende bisogno e ambiguità | richiesta | intent contract |
| RISK | classifica impatto | intent + contesto | R0–R3 |
| PLANNER | costruisce piano eseguibile | intent contract | task graph |
| SKEPTIC | cerca assunti e failure mode | task graph | challenge report |
| RULE-GUARDIAN | applica policy | azione proposta | approve/reject/escalate |
| ROUTER | seleziona agente/skill | task autorizzato | assignment |
| MEMORY-CURATOR | governa ricordi | eventi/esiti | record versionati |
| RECOVERY | sceglie retry/compensazione | failure context | recovery action |
| GATE | valuta criteri di qualità | output + rubrica | gate report |
| NERVE-SAVE | ottimizza espressione | output validato | risposta finale |
| META-OBSERVER | rileva pattern | metriche e gate | change proposal |

**Regola:** questi sono ruoli logici. Non devono diventare processi separati se una funzione deterministica è sufficiente.

---

## 10. Skill di conoscenza

Le skill sono pacchetti versionati, non prompt liberi.

```text
skill/
  manifest.yaml       # id, versione, owner, rischio, permessi
  instructions.md     # procedura operativa
  schemas/             # input/output JSON Schema
  examples/            # casi validi e non validi
  policies/            # limiti e precondizioni
  tests/               # contract e regression test
  changelog.md
```

Categorie iniziali:

- architecture-decisions;
- workflow-design;
- RuFlo integration;
- secure-tool-use;
- failure-recovery;
- memory-governance;
- quality-evaluation;
- token-economy;
- observability;
- deployment-readiness.

---

## 11. Ecosistema di memoria pianificato

| Layer | Contiene | Persistenza | Scrittura |
|---|---|---|---|
| Working | contesto del workflow | breve/TTL | orchestrator |
| State | stato canonico e checkpoint | durevole | state machine |
| Episodic | eventi ed esiti | durevole | event/audit writer |
| Decision | ADR e Decision Record | versionata | decision service |
| Semantic | conoscenza recuperabile | indicizzata | memory curator |
| Strategy | strategie e benchmark | versionata | evolution service approvato |
| Archive | record obsoleti/sostituiti | immutabile | retention process |

Il futuro **Plan Memory Agent** indicizzerà tutti i sette piani, risponderà con citazioni ai file e non potrà alterare gli originali. Verrà implementato dopo il Livello 7, insieme al runtime, per evitare di congelare una semantica prematura.

---

## 12. Architettura logica iniziale

```text
Client/API
   │
   ▼
Ingress → Identity/Tenant → Intent & Risk
   │
   ▼
Orchestration Core ─────→ Policy/Approval
   │                         │
   ├→ Planner/Task Graph     │
   ├→ State/Checkpoint       │
   ├→ Agent & Skill Router ←─┘
   │        │
   │        ├→ RuFlo Adapter → RuFlo swarm/runtime
   │        └→ Tool Gateway  → servizi/repository/CI
   │
   ├→ Event & Recovery → DLQ/Compensation
   ├→ Memory Services
   ├→ Quality Gate → NERVE-SAVE
   └→ Logs/Metrics/Traces/Audit
```

---

## 13. Struttura repository file per file — baseline L1

```text
orchestration-layer/
├── README.md                         # scopo, quick start, limiti
├── pyproject.toml                    # package, toolchain e versioni
├── uv.lock                           # dipendenze Python bloccate
├── package.json                      # tool RuFlo/Node, se richiesti
├── package-lock.json                 # dipendenze Node bloccate
├── Makefile                          # comandi riproducibili
├── .env.example                     # sole chiavi configurabili, nessun secret
├── .gitignore
├── LICENSE
│
├── docs/
│   ├── architecture/
│   │   ├── context.md                # confini e attori
│   │   ├── containers.md             # servizi principali
│   │   ├── components.md             # componenti interni
│   │   └── threat-model.md           # trust boundary e minacce
│   ├── adr/                          # decisioni architetturali
│   ├── plans/                        # checkpoint L1–L7
│   ├── runbooks/                     # incidenti e recovery
│   └── api/                          # contratti pubblici
│
├── src/orchestrator/
│   ├── __init__.py
│   ├── bootstrap.py                  # composition root
│   ├── config.py                     # config tipizzata
│   ├── domain/
│   │   ├── models.py                 # workflow, task, decision, failure
│   │   ├── states.py                 # state machine
│   │   ├── policies.py               # regole di dominio pure
│   │   └── events.py                 # eventi interni tipizzati
│   ├── application/
│   │   ├── commands.py               # casi d’uso di scrittura
│   │   ├── queries.py                # casi d’uso di lettura
│   │   ├── planner.py                # task graph
│   │   ├── dispatcher.py             # delega controllata
│   │   ├── gates.py                  # coordinamento quality gate
│   │   └── recovery.py               # retry/compensazione/escalation
│   ├── ports/
│   │   ├── agent_runtime.py           # porta runtime agenti
│   │   ├── state_store.py             # porta stato
│   │   ├── event_bus.py               # porta eventi
│   │   ├── memory.py                  # porta memoria
│   │   ├── policy_engine.py           # porta policy
│   │   ├── tool_gateway.py            # porta azioni esterne
│   │   └── telemetry.py               # porta observability
│   ├── adapters/
│   │   ├── ruflo/                     # adapter RuFlo, API da verificare
│   │   ├── persistence/               # implementazioni DB
│   │   ├── messaging/                 # broker/outbox
│   │   ├── llm/                       # provider model
│   │   ├── tools/                     # sandbox e connettori
│   │   └── telemetry/                 # OTel/log/metrics
│   ├── agents/
│   │   ├── registry.py                # catalogo ruoli
│   │   ├── contracts.py               # input/output degli agenti
│   │   └── prompts/                   # prompt versionati
│   ├── memory/
│   │   ├── schemas.py                 # record e namespace
│   │   ├── curator.py                 # lifecycle e qualità
│   │   └── retrieval.py               # query contestuale
│   ├── quality/
│   │   ├── gate_engine.py             # PASS/FAIL/ESCALATE
│   │   ├── rubrics.py                 # criteri misurabili
│   │   └── nerve_save.py              # ottimizzazione output
│   └── api/
│       ├── app.py                     # endpoint/transport
│       ├── schemas.py                 # contratti API
│       └── dependencies.py            # wiring richieste
│
├── skills/
│   ├── registry.yaml                  # indice skill
│   └── core/                          # pacchetti skill versionati
│
├── builder_swarm/
│   ├── agents.yaml                    # team di costruzione
│   ├── prompts/                       # prompt dei builder
│   ├── gates/                         # rubriche di costruzione
│   └── workflows/                     # build-test-review
│
├── memory_store/
│   ├── plans/                         # copie immutabili L1–L7
│   ├── checkpoints/                   # stato per livello
│   ├── rules/                         # governance memoria
│   └── schemas/                       # schema record
│
├── deploy/
│   ├── docker/
│   ├── kubernetes/
│   └── observability/
│
├── migrations/                        # migrazioni persistenti
├── scripts/                           # setup, smoke, benchmark
├── tests/
│   ├── unit/
│   ├── contract/
│   ├── integration/
│   ├── end_to_end/
│   ├── chaos/
│   └── fixtures/
└── .github/workflows/
    ├── ci.yml
    ├── security.yml
    └── release.yml
```

**Nota realistica:** questa è una mappa logica. L2 dovrà eliminare file inutili, scegliere stack e assegnare contratti; crearli tutti ora produrrebbe scaffolding vuoto.

---

## 14. Fasi generali di costruzione

| Fase | Scopo | Output | Gate principale |
|---:|---|---|---|
| 1 | Costituire Builder Swarm | ruoli, permessi, workflow, rubriche | indipendenza del Gatekeeper |
| 2 | Consolidare requisiti e rischi | NFR, threat model, casi R0–R3 | requisiti testabili |
| 3 | Definire dominio e contratti | modelli, porte, state machine, eventi | zero dipendenze infrastrutturali nel dominio |
| 4 | Costruire vertical slice | un workflow R1 end-to-end | stato recuperabile e audit completo |
| 5 | Integrare RuFlo | adapter + capability tests | nessuna API presunta |
| 6 | Aggiungere memoria e quality | checkpoint, retrieval, gate, NERVE-SAVE | qualità e access control |
| 7 | Resilienza e security | retry, breaker, compensazione, sandbox | failure injection superata |
| 8 | Observability e benchmark | SLO dashboard, cost/quality benchmark | swarm giustificato dai dati |
| 9 | Pre-produzione | canary, runbook, rollback, DR | readiness review |
| 10 | Produzione controllata | rilascio graduale | SLO e stop conditions rispettati |

---

## 15. Strategia d’implementazione dopo i sette piani

1. Congelare il Livello 7 come specifica candidata.
2. Creare Builder Swarm e repository reale.
3. Implementare un solo vertical slice R1.
4. Costruire Plan Memory Agent in modalità read-only.
5. Integrare RuFlo dietro adapter sulla base di smoke test.
6. Aggiungere R2 e R3 solo dopo state recovery e security gate.
7. Espandere agenti soltanto se benchmark qualità/costo lo giustifica.
8. Eseguire canary con kill switch e rollback.

---

## 16. Quality Gate L1 → L2

| ID | Criterio | PASS richiesto |
|---|---|---|
| C1 | Visione e confini coerenti | nessuna logica di dominio nel core orchestration |
| C2 | Priorità esplicite | P0/P1/P2 con non-obiettivi |
| C3 | Builder Swarm definito | owner, deliverable e separazione valutatore/autore |
| C4 | Ecosistemi coperti | governance, cognizione, esecuzione, azioni, memoria, qualità, resilienza, osservabilità, evoluzione |
| C5 | Protocolli mentali auditabili | Decision Record, non monologo interno |
| C6 | Architettura iniziale | confini e adapter RuFlo presenti |
| C7 | Struttura repository | ogni directory ha responsabilità unica |
| C8 | Roadmap implementativa | vertical slice prima dell’espansione |
| C9 | Memoria futura pianificata | piani/checkpoint immutabili e Plan Memory Agent read-only |
| C10 | Approvazione umana | via esplicito dell’utente |

**Soglia:** 10/10. Nessuna tolleranza perché L1 stabilisce i confini di tutti i livelli successivi.

---

## 17. Autocritica del Piano L1

### Cosa funziona

- organizza obiettivi, priorità, principi, team e architettura;
- distingue ruoli mentali da processi reali, evitando agenti inutili;
- introduce memoria, skill e ragionamento osservabile senza inventare implementazioni;
- mette il vertical slice prima della complessità distribuita;
- rispetta il vincolo di integrazione RuFlo tramite adapter.

### Difetti da correggere nel Livello 2

1. Stack tecnologico non scelto.
2. Struttura file ancora sovradimensionata e non validata contro casi d’uso.
3. Contratti tra componenti non definiti.
4. State machine e tassonomia errori solo nominate.
5. Builder Swarm privo di prompt, budget e policy operative.
6. Memoria priva di schema, query model e ACL concreti.
7. Nessuna matrice build-vs-buy.
8. Nessun dimensionamento di costo, latenza o throughput.
9. Nessun piano di test per dimostrare che RuFlo aggiunga valore.
10. Deployment target e compliance non determinati.

### Valutazione

| Dimensione | Voto /10 |
|---|---:|
| Chiarezza generale | 9.0 |
| Realismo | 8.8 |
| Completezza concettuale | 8.7 |
| Implementabilità immediata | 5.5 |
| Specificità | 6.2 |

**Verdetto:** base generale solida ma deliberatamente insufficiente per iniziare la produzione. Il Livello 2 dovrà trasformarla in un’architettura logica contrattuale, ridurre lo scaffolding e chiudere le decisioni tecniche principali.
