# STRATEGY.md — Ecosistema Content Ingest: Strategia Operativa Completa e Flussi

**Scopo di questo documento:** Definire in modo preciso, architettato e non ambiguo **come** l'ecosistema funziona giorno per giorno. Tutti i flussi, handoff, verifiche, aggiornamenti di memoria, ruoli dei reparti e agenti. Questo è il "manuale operativo" ufficiale.

Basato su:
- Requisiti utente (gerarchia aziendale 4 livelli, video "guardato" con visual, content-forge → wiki, update flussi esistenti, agenti completi, solo CLI).
- Principi da master-build-architecture (P07 three-level + flussi, PT01 conductor-with-subagents, P10 memory, PT05 7-file agents, P09 failure-modes, P12 traceability, P13 meta-recursive).
- Content-Forge 2.0 pipeline (9 stage + MKD always + depth + SI).

## 1. Principi Guida della Strategia (Non Negoziabili)

1. **Memory è il cuore pulsante** — Ogni singola decisione, architettura, sessione, bug, errore, problema, handoff, aggiornamento deve essere registrato nell'ecosistema di memory **immediatamente**. Non esiste azione senza trace in memory.
2. **Verifica e Controllo sono continui e proattivi** — Non c'è "fase di verifica" alla fine. C'è un intero reparto (Verification & Control) che monitora in tempo reale, audita, e blocca o corregge.
3. **Gerarchia chiara con escalation** — L1 Conductor decide e coordina. L2 Teams eseguono. L3 Agents fanno il lavoro specialistico. L4 Skills sono tool. Verification Team può escalation a L1 in caso di problemi gravi.
4. **"Video va visto" è sacro** — Nessun video viene considerato "processato" senza visual analysis + frame + descrizioni dei passaggi mostrati.
5. **Content-Forge è il motore di strutturazione** — Dopo ogni ingestion + watch, SEMPRE si passa da content-forge per MKD + wiki.
6. **Aggiornamento flussi esistenti è un output obbligatorio** — Ogni volta che ingeriamo conoscenza rilevante, generiamo proposal concreti per migliorare altri ecosistemi/workflow.
7. **CLI-only e trasparenza totale** — Tutto tracciabile, loggato, riproducibile senza API esterne.
8. **One-by-one + Self-Improvement** — Costruiamo e miglioriamo un agente/skill/reparto alla volta, usando il memory e il Verification Team per validare.

## 2. Gerarchia e Reparti (4 Livelli Aziendali)

### L1 — Director / Conductor
- Unico punto di contatto con l'utente.
- Decide quali team attivare.
- Gestisce escalation dal Verification Team.
- Responsabile finale della qualità e degli update ai flussi esistenti.
- **Deve** far aggiornare la memory dopo ogni sua decisione.

### L2 — Department Teams (i "reparti")

**1. Ingestion Department** (operatività)
- Responsabile di prendere input grezzi (link, canali, web) e trasformarli in materiale grezzo strutturato.
- Sub-agenti L3: yt-channel-ingester, tiktok-ingester, web-researcher, video-single-ingester.

**2. Processing & Analysis Department** (operatività + "visione")
- Responsabile di "guardare" i video e estrarre conoscenza profonda.
- Sub-agenti L3: video-watcher-agent (usa L4 video-watcher-skill), transcript-processor, visual-analyzer, knowledge-extractor, context-mapper.

**3. Forge & Wiki Integration Department** (operatività)
- Responsabile di trasformare il materiale in conoscenza operativa tramite content-forge e inserirla nella wiki.
- Genera anche proposal di update per flussi esistenti.
- Sub-agenti L3: content-forge-invoker (usa L4 wrapper), wiki-ingester, knowledge-packager, update-proposer.

**4. Verification & Control Department** (NUOVO — il "reparto di verifica e controllori" che hai chiesto)
- **Intero reparto dedicato alla verifica continua**.
- Non è QA alla fine: è controllo proattivo e reattivo durante tutto il flusso.
- Responsabilità:
  - Verificare che ogni step rispetti gli invariant (memory update, visual analysis presente, trace P12, CLI-only, no invention).
  - Auditare coverage (atomi da video/frame → wiki).
  - Controllare qualità visiva ("i passaggi mostrati sono stati catturati?").
  - Triage di bug/errori/problemi.
  - Bloccare handoff se qualcosa non va.
  - Generare report di verifica per L1.
- Sub-agenti L3 (tutti con 7 file):
  - coverage-controller-agent
  - visual-verifier-agent (controlla che ci siano frame + descrizioni dettagliate dei passaggi)
  - compliance-auditor-agent (verifica rispetto a strategy, principles, CLI-only)
  - error-triage-controller-agent (gestisce bug, errori, problemi)
  - silent-observer-agent (monitora silenziosamente, come PT07)
  - workflow-compliance-agent (verifica che i flussi rispettino la strategia definita qui)
  - real-time-monitor-agent (se possibile in futuro con hook)

**5. Memory Management Department** (NUOVO — l'"intero ecosistema di memoria" che hai chiesto)
- **Reparto dedicato a gestire l'intero ecosistema di memoria**.
- Non è solo uno script: sono **agenti** che attivamente leggono, scrivono, audiano, propagano e mantengono la memoria.
- Responsabilità:
  - Dopo **ogni** decisione, architettura, sessione, bug, errore, problema, handoff, aggiornamento → gli agenti di questo reparto devono registrare.
  - Mantenere le cartelle per categoria (vedi sotto).
  - Propagare aggiornamenti (es. se un bug viene fixato, aggiornare tutti i workflow-state e knowledge-state rilevanti).
  - Audire la memoria periodicamente.
  - Generare report di "stato memoria" per Verification Team e L1.
- Sub-agenti L3 (tutti con 7 file):
  - memory-architect-agent (progetta e mantiene la struttura della memory)
  - checkpoint-manager-agent
  - decision-codifier-agent (registra decisioni in formato ADR)
  - bug-error-tracker-agent (dedicato a bug, errori, problemi)
  - session-archiver-agent
  - update-propagator-agent (propaga cambiamenti a workflow-state, knowledge-state, agent-state)
  - memory-auditor-agent (verifica che tutto sia stato aggiornato correttamente)
  - knowledge-state-manager-agent
  - architecture-versioner-agent
  - workflow-state-manager-agent

### L3 — Specialized Agents
Ogni agente L3 deve avere i **7 file canonici**:
1. <name>.md (spec + ruolo)
2. system-prompt.md
3. tools.md (CLI + script + schemas)
4. playbook.md (flusso dettagliato + esempi)
5. evals.md (casi di test)
6. failure-modes.md (tabella)
7. memory.md (come questo agente interagisce con l'ecosistema di memory)

### L4 — Skills / Tools
Skill complete con SKILL.md + references + script Python + templates + principi + regole.

## 3. Ecosistema di Memoria (come hai chiesto: "intero ecosistema di memoria")

**Struttura cartelle (categorie separate):**

memory/
├── checkpoints/              # CP-XXX dopo ogni azione/step
├── decisions/                # DEC-XXX (ADR: contesto, decisione, alternative, rationale, conseguenze, trace)
├── sessions/                 # SES-XXX (log conversazionali / run)
├── plans/                    # PLAN-vN e strategie
├── architectures/            # Versioni di architetture e flussi
├── bugs/                     # Bug report dettagliati
├── errors/                   # Errori tecnici e recovery
├── updates/                  # Ogni aggiornamento (a skill, agente, flusso, wiki, memory stessa)
├── workflow-state/           # Stato corrente di tutti i workflow/ecosistemi conosciuti
├── knowledge-state/          # Cosa sa attualmente l'ecosistema (per update proposal)
├── agent-state/              # Stato e performance di ogni agente/team
├── verification-logs/        # Log di verifiche fatte dal Verification Team
└── architecture-versions/    # Storico versioni di architetture

**Regola d'oro della Memory:**
- **Dopo OGNI cosa** (decisione del Conductor, handoff tra team, risultato di un L3, bug rilevato, errore, fix, update a un flusso, inserimento in wiki, ecc.) → almeno un agente del Memory Management Department deve essere coinvolto (o il manager script + audit da memory-auditor).
- Il Verification Team controlla che questo sia avvenuto.

**Agenti del Memory Management Department** sono responsabili di:
- Scrivere nei file giusti.
- Mantenere l'INDEX.md sempre aggiornato.
- Propagare (es. un nuovo bug in bugs/ → update in workflow-state se rilevante).
- Eseguire audit periodici.

## 4. Flusso Operativo Principale (come si fanno le cose)

**Fase 0 — Invocazione + Memory Bootstrap**
- Conductor riceve input.
- Memory Management Team crea CP-000 + struttura run.
- Conductor fa piano iniziale e lo registra come DEC.

**Fase 1 — Ingestion (Ingestion Team)**
- L3 ingester usa L4 yt-ingest-skill.
- Al termine di ogni video/canale processato → Memory Management registra in checkpoints + knowledge-state + workflow-state (se rilevante).
- Verification Team (compliance-auditor + visual-verifier se video) controlla prima di handoff.

**Fase 2 — Processing & "Visione" (Processing Team)**
- video-watcher-agent + L4 skill produce frame + visual analysis.
- **Verification & Control** (visual-verifier-agent) controlla che i passaggi mostrati siano descritti in modo dettagliato.
- Ogni frame e atomo → Memory Management registra (knowledge-state, agent-state).
- Se verification fallisce → error-triage + bug report in bugs/.

**Fase 3-4 — KG + MKD**
- Memory update.

**Fase 5-6 — Forge (Forge Team)**
- content-forge-invoker usa L4 wrapper → content-forge.
- Output wiki notes + MKD.
- update-proposer genera proposal per flussi esistenti.
- **Verification Team** (coverage-controller + compliance-auditor) verifica trace e coverage.
- Memory Management: registra in updates/, knowledge-state, workflow-state, architecture-versions.

**Fase 7-8 — QA + Verifica Finale (Verification & Control Department)**
- Questo è il momento in cui il reparto di verifica entra in modo pesante.
- coverage-controller, visual-verifier, workflow-compliance, error-triage.
- Se tutto ok → handoff a L1.
- Se problemi → blocca e crea ticket in bugs/errors + escalation a Conductor.

**Fase 9 — Wiki Insertion + Update Flussi + Chiusura**
- wiki-ingester inserisce.
- update-proposer consegna proposal all'utente (o lo mette in un posto per la wiki).
- Memory Management chiude il run con CP finale + update a tutti gli state rilevanti.

**Fase 10 — Self-Improvement & Memory Audit (Memory + Verification)**
- silent-observer + memory-auditor + bug-error-tracker analizzano il run.
- Generano improvement per playbook, agenti, strategy.
- Tutto registrato in updates/ e verification-logs/.

## 5. Handoff e Coordinamento

- Tutti gli handoff sono strutturati (JSON con input/output attesi + memory requirement).
- Prima di ogni handoff: agente chiamante deve aver aggiornato la memory.
- Verification Team può inserire "verification checkpoint" tra un team e l'altro.

## 6. Come si Aggiorna Tutto

Ogni aggiornamento (bug fix, miglioramento di un agente, nuova regola nella strategy, nuova conoscenza da wiki) deve:
1. Essere registrato dal Memory Management Team (updates/, agent-state, workflow-state, ecc.).
2. Essere verificato dal Verification & Control Department.
3. Essere propagato dove rilevante (es. se cambia la strategy → aggiornare playbook di tutti gli agenti).

## 7. Stato Attuale della Strategia (al momento della scrittura)

Questa STRATEGY.md è la prima versione completa. Sarà viva e aggiornata dal Memory Management Department e dal Verification Team.

**Prossimi passi per rendere questa strategia operativa:**
- Creare i 7 file completi per tutti gli agenti del Verification & Control Team e del Memory Management Team.
- Implementare script di supporto per gli agenti di memory (es. auto-propagation).
- Aggiungere nel Conductor playbook il riferimento obbligatorio a questa STRATEGY.md.

---

**Trace (P12):** Questo documento è stato creato in risposta diretta alla tua richiesta di "un intero reparto che deve verificare... controllori" + "un intero ecosistema di memory... agenti che gestiscono tutto questo ecosistema di memoria" + "va costruita tutta la strategia e il modo in cui si andranno a funzionare il flusso".

La strategia è ora definita. Il lavoro di implementazione degli agenti e dei tool di memory continua one-by-one.
