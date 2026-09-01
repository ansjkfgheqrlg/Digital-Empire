# Exponium Content Factory — Contenuto Integrale

**Fonte:** Repo su disco `C:\Users\Utente\Desktop\qui tutto\Lavoro\Exponium\second-brain-exponium\Ecosistema - Content Factory`
**Data ingestione:** 2026-06-09
**Tipo fonte:** Repo architettonica (file MD + SH + YAML)
**Nome in codice sistema:** AION Studio — *Agentic Intelligent Orchestration Network*

---

## CONTESTO E SCOPO

Azienda di agenti AI (holding **AION GROUP**) costruita per il lancio di Exponium (software algo 16 livelli). Struttura enterprise a gerarchie multiple, 8 direzioni, backbone condiviso, 68+ check automatici, produzione di massa parallela, auto-miglioramento. Scope: **contenuti per il lancio Exponium** — non fa nulla di generico.

Il founder ha costruito questa come prodotto per cliente Exponium. Max vuole farne una versione personale per Digital Empire — più grande (agency + info products + SaaS, non solo lancio singolo prodotto).

---

## PLAN-00-VISION — La Visione Completa

### Obiettivo del sistema
Costruire una "azienda di agenti" che produce, in modo coordinato e con qualità professionale:
- Video (text-to-video, image-to-video, pipeline immagine→video, video editing/montaggio, Vibe Motion/motion control, multi-clip con audio)
- Immagini in altissima qualità (4K), foto prodotto, marketplace cards, personaggi coerenti (Soul ID)
- Contenuti & marketing: copy, ad creative, script/VSL, SEO, social, piani di lancio

### 8 Principi guida (non negoziabili)
- P1 Gerarchia chiara: Board → Direzioni → Team → Sottoteam → Agenti
- P2 Un team per workflow: ogni workflow/funzionalità ha il suo team dedicato
- P3 Coordinamento esplicito: comunicazione via message bus + memoria condivisa + handoff formali
- P4 SOP vive: ogni processo è una SOP versionata, misurata e migliorata
- P5 Qualità by-design: QA e contradiction-check integrati nella pipeline
- P6 Tutto è registrato: ogni job → log + artefatto + metrica
- P7 Riuso degli asset installati: 144 agenti, 98 skill, 181 comandi orchestrati, non reinventati
- P8 Costi sotto controllo: budget crediti Higgsfield gestito come risorsa aziendale

### Struttura cartelle fisica
```
orchestration/
├── vendor/                 # asset installati (ruflo, content-forge, ...)
├── company/                # definizione azienda (org, teams, characters)
├── sop/                    # procedure operative versionate
├── orchestrator/           # codice orchestration layer (conductor, bus, state, dispatch)
├── runtime/                # esecuzione (bus, memory, projects/<id>/)
└── metrics/                # KPI, log evolutivi, miglioramento SOP
```

---

## PLAN-01-ARCHITECTURE — Architettura Dettagliata

### Gerarchia a 3 livelli
```
L3 (alto)   — REPARTI (Direzioni D1..D8) — comandano tutto, ricevono dal Conductor
L2 (medio)  — TEAM-WORKFLOW — gestiscono workflow end-to-end
L1 (base)   — TEAM-FUNZIONE — un team per ogni funzionalità, eseguono il lavoro
```

Regola: un ordine scende L3→L2→L1, il risultato risale L1→L2→L3 e torna al Conductor.

### Schema team canonico (da content-forge team-builder)
Ogni team è definito con:
- Topology (queen-led / mesh / pipeline)
- Coordinator (agente capo-team, mappato a asset reale)
- Agents (ID · ruolo · input · output · ASSET · skill usate · criterio accettazione)
- Communication protocol
- Handoff rules (cosa passa al team successivo)
- Failure handling
- Shared state (cartella nel project-state)
- Eval cases (come si misura la qualità)

### Le 8 Direzioni

**D1 — STRATEGY & PRODUCT**
Queen: D1-QUEEN. Asset: product-manager-skills (49 skill, 6 comandi), context-engineering-advisor.
- T1.1 Discovery & Brief: Intent Parser → Audience/Avatar → Reference Scout → Brief Writer → output: brief.json
- T1.2 Roadmap & Prioritization: Task Decomposer → Prioritizer → Budget Planner → output: roadmap.json

**D2 — CREATIVE / PRODUCTION**
Queen: D2-QUEEN. Asset: hf-studio (Higgsfield), marketingskills image/video, cli-printing-press.
- T2.5 Characters/Soul ID (⭐ centrale per UGC): Reference Curator → Soul Trainer → Identity QA → Character Librarian
- T2.1 Image 4K: Prompt Engineer → Model Selector → Image Generator → Image QA → output: frames.json (4K)
- T2.2 Video (text/image-to-video): Scene Writer → Model/Duration Selector → Video Generator → Video QA → output: clips.json
- T2.3 Motion/Vibe Motion (⭐): Motion Designer → Animator (hf-studio pipeline/draw_to_video/reframe) → Motion QA
- T2.4 Video Editing/Montaggio: Timeline Builder → Cutter/Stitcher → Audio/Caption → Export QA → output: final_video.json
- T2.6 Product Shoot (e-commerce, on-demand): Shoot Planner → Card Generator → Product QA

**D3 — OPERATIONS (runtime)**
Queen: D3-QUEEN. Asset: hf-studio/lib.sh, ruflo swarm/memory.
- T3.1 Render Queue: Dispatcher → Worker Pool → Retry/Watchdog (pattern: mesh-coordinator per parallelismo)
- T3.2 Cost & Credits: Cost Estimator → Budget Guard (blocca se sfora budget)
- T3.3 Asset Storage: Organizer → Versioner

**D4 — MARKETING & GROWTH**
Queen: D4-QUEEN. Asset: marketingskills (42 skill), copy-workflow APSOC (11 agenti).
- T4.1 Copy (APSOC): Avatar → Headline → Body APSOC → Objections → Review (score /100)
- T4.2 Ad Creative & Social: Ad variants → Social posts → Caption/Hook (≥3 varianti per canale)
- T4.3 SEO & Distribution: SEO → Programmatic → Directories
- T4.4 Launch & Funnel: Funnel designer → Email → Pricing → Launch plan

**D5 — QUALITY & GOVERNANCE (Verificatori)**
Queen: D5-QUEEN. Asset: skill-contradiction-analyzer (Python), content-forge QA agents.
- T5.1 Output QA: Spec check → Brand check → Coverage (100% spec o → rimando con note)
- T5.2 Coherence/Contradiction (gate CI): Analyzer → Fast verdict (0 contraddizioni bloccanti)
- T5.3 Brand & Policy: Guidelines → Rights/Compliance → Final Sign-off

**D6 — ORCHESTRATION & EVOLUTION (il capo di tutti)**
Queen: D6-QUEEN = Conductor/Board. Asset: content-forge (conductor, builders, self-improvement), ruflo (hive-mind, memory, coordination).
- T6.1 Conductor: riceve brief, emette royal directives, instrada L3→L2→L1, aggrega, consegna
- T6.2 Coordination Bus: Message Router → Memory Manager → State Keeper (mantiene runtime/bus/ e runtime/memory/)
- T6.3 Self-Improvement: Failure Detector → Triage → Phase Planner (legge fallimenti, aggiorna SOP)
- T6.4 Builders/Forge: team-builder · agent-builder · workflow-builder · orchestration-builder (crea nuovi team on-demand)

**D7 — RESEARCH (dati prima della produzione)**
Queen: D7-QUEEN. Asset: marketingskills, content-forge knowledge-graph-agent.
- T7.1 Trend & Market Research: trends social, formati che funzionano
- T7.2 Reference & Style Research: riferimenti visivi/stilistici
- T7.3 Knowledge Base: archivia scoperte, riusabili dai team
- Regola: i team produzione NON partono senza il pacchetto-ricerca di D7

**D8 — ENGINEERING / CODE (solo codice)**
Queen: D8-QUEEN. Asset: ruflo (python-specialist, typescript-specialist, security-auditor), skill-contradiction-analyzer, cli-printing-press.
- T8.1 Code Custody: struttura, naming, niente duplicati
- T8.2 Python QA: lint/test + contradiction-analyzer runner
- T8.3 Tooling Foundry: fabbrica CLI quando servono (es. CLI video editing per T2.4)
- T8.4 Review & Refactor: codice migliora nel tempo
- Regola: nessun reparto modifica codice senza passare da D8

---

## CUORE TECNICO

### Project-State (una cartella per progetto)
```
runtime/projects/<id>/
├── state.json        # fase, task, owner, status, budget
├── trace.jsonl       # log cronologico audit-proof
├── 01-brief/ 02-roadmap/ characters/ images/ clips/
├── motion/ final/ copy/ product/ manifest.json
```

state.json schema:
```json
{ "id":"ugc-001", "phase":"production", "budget":{"cap":50,"spent":12.4},
  "tasks":[{"id":"T2.5","status":"DONE"},{"id":"T2.1","status":"RUNNING"}] }
```

### Message Bus
```
runtime/bus/messages.jsonl
```
Formato handoff contract:
```json
{"from":"T6.1","to":"D2-QUEEN","priority":"HIGH",
 "type":"directive","payload":{...},"acceptance":[...],"ts":"..."}
```

### SOP UGC end-to-end
```
1. D1  → Brief + Roadmap + Budget
2. D7  → Ricerca (trend, riferimenti)        [parallelo a 1]
3. D6  → Conductor dispaccia le direttive
4. D2  → T2.5 Soul → T2.1 Img4K → T2.3 Motion → T2.4 Montaggio
   D3  → esegue job, controlla costi, salva   [durante 4]
5. D4  → Copy + caption + hook social
6. D5  → QA + contradiction check (gate)
7. D8  → controlla/ordina il codice usato     [trasversale]
8. D6  → aggrega, consegna, registra metriche → Self-Improvement
```

### Mappa asset → dove viene usato
| Asset | Reparto/Team |
|---|---|
| hf-studio (Higgsfield) | D2 (produzione), D3 (esecuzione) |
| ruflo (hive-mind/swarm/memory) | D6 (orchestrazione), D3 (queue), D8 (specialist/security) |
| content-forge2.0 | D6 (conductor, builders, self-improvement), D7 (knowledge-graph) |
| copy-workflow (APSOC) | D4 T4.1 (copy) |
| marketingskills (42) | D4 (ad/social/seo/launch), D7 (research), D1 (avatar) |
| product-manager-skills (49) | D1 (brief, roadmap, prioritize, strategy) |
| context-engineering-advisor | trasversale (D1, D2 prompt, D7) |
| skill-contradiction-analyzer (Python) | D5 T5.2 (gate coerenza), D8 T8.2 |
| cli-printing-press | D8 T8.3 (fabbrica CLI, es. video editing) |

---

## PLAN-02-BUILD — Piano di Costruzione Esecutivo

### 8 BUILD in sequenza
- BUILD-1 (✅ FATTO): Fondamenta — company/org/*.yaml (hierarchy, directions, roster) + struttura cartelle runtime/
- BUILD-2 (✅ FATTO & TESTATO): Orchestratore minimo — lib-orch.sh, state.sh, bus.sh, conductor.sh
- BUILD-3 (✅ FATTO & TESTATO — video reale prodotto 2026-05-29): MVP verticale — T2.5 Soul → T2.1 Img4K → T2.3 Motion → T2.4 Montaggio, con hf-studio reale
- BUILD-4 (✅ FATTO & TESTATO): Reparti supporto — D1 Strategy, D7 Research, D4 Marketing con copy/caption/hook
- BUILD-5 (⏭️ PROSSIMO): Qualità + Codice — D5 QA gate + D8 contradiction-analyzer + lint Python
- BUILD-6 (⏳): Self-improvement — D6 legge fallimenti, aggiorna SOP
- BUILD-7 (⏳): Funzionalità avanzate — editing pro, video t2v, product e-commerce
- BUILD-8 (⏳): GitHub — versioning, repo, CI

### Comandi operativi BUILD-3 (funzionanti)
```bash
cd ~/orchestration/orchestrator
ID=$(./conductor.sh new "<brief UGC>")
./dispatch.sh ugc "$ID"                    # run reale
./dispatch.sh ugc "$ID" --dry             # stima costo senza generare
./dispatch.sh ugc "$ID" --soul <soul_id>  # con personaggio ricorrente
./conductor.sh status "$ID"
```

### Test reale BUILD-3 (2026-05-29)
- Progetto creato via Conductor → workflow UGC eseguito end-to-end
- Output: keyframe 4K verticale (9:16) + clip animata + master final_ugc.mp4 (2 MB)
- Costo: ~12 crediti (95 → 83)
- Error-handling: un fallimento permessi → escalation a D6, poi auto-fix via bootstrap.sh

---

## ASSET INSTALLATI — INSTALL MANIFEST

| # | Asset | Tipo | Contenuto chiave |
|---|---|---|---|
| 1 | context-engineering-advisor | Skill (globale) | Context engineering consulenza |
| 2 | ruflo | Framework orchestrazione | 108 agenti + 168 comandi (swarm, hive-mind, sparc, consensus, github, memory, coordination) |
| 3 | marketingskills | 42 skill marketing | ads, ad-creative, copywriting, cro, seo, analytics, video, social, launch, pricing |
| 4 | cli-printing-press | Generatore CLI agent-native | Stampa CLI Go + skill + MCP server per qualsiasi API/sito |
| 5 | product-manager-skills | 49 skill PM + 7 comandi | discover, plan-roadmap, prioritize, strategy, write-prd |
| 6 | skill-contradiction-analyzer | Meta-skill QA | /analizza /confronta — rileva contraddizioni tra skill (Python) |
| 7 | content-forge2.0 | Forge agenti/team/workflow | 25 agenti builder/optimizer/qa/self-improvement |
| 8 | copy-workflow | Sistema copywriting multi-agente | 11 agenti + 6 skill, framework APSOC |

**Totali:** 144 agenti (108 ruflo + 25 content-forge + 11 copy-workflow) · ~98 skill · 181 comandi · 1 motore Higgsfield

---

## AGENTI VERIFICATORI (GATE POST-STEP)

3 agenti automatici via `orchestrator/verify.sh`:
- V1 Integrity Checker (D8): struttura file, sintassi bash, YAML, permessi, asset vendor
- V2 Output QA (D5): integrità progetti, state.json, video finale, task DONE, trace
- V3 Memory Auditor (D6): coerenza MEMORY-INDEX, checkpoint/ADR linkati, indice aggiornato

Integrati in `mem.sh checkpoint` → girano a ogni nuovo checkpoint. Ultimo run: 42 PASS / 0 FAIL.

---

## SKILL EXPONIUM-CONTEXT (second brain Exponium)

Costruita con content-forge v2.0 (Stage 1→4):
- 90 atomi estratti da 4 sorgenti (briefing call, documento legale, guida commerciali, script mail)
- 14.062 parole sorgente → 45.148 parole MKD-pack (espansione 3.21×)

Struttura skill:
- Kernel SKILL.md (≤500 righe, anti-undertriggering)
- 1 conductor sempre-attivo su trigger Exponium
- 6 sub-agents domain-trained: copywriter (CONSOB-safe) · compliance-validator · sales-assistant · lead-qualifier · memory-keeper · gap-tracker
- References in 5 aree: product · compliance · icp · voice · operations + external + conventions + schemas
- Memory ecosystem: decisions/ · projects/ · checkpoints/ · open-questions/ · best-practices/ + numbers-evidence.md
- 2 scripts Python con pytest: compliance_lint.py (16/16 PASS) · memory_keeper.py (11/11 PASS)
- 9 gap pre-popolati in memory/open-questions/

---

## METODOLOGIA (METHOD-SWARM)

### SPARC applicato a ogni piano/artefatto
- Specification: obiettivo, scope, vincoli
- Pseudocode: logica alto livello prima del dettaglio
- Architecture: diagrammi, confini, contratti (organigrammi + handoff)
- Refinement: criteri accettazione + eval_cases
- Completion: SOP + metrics

### Hierarchical Swarm (ruflo queen→workers)
- Decomposizione task: ogni obiettivo grande → sotto-task con dipendenze e sequenza
- Delega specializzata: worker (agente-asset) più adatto per ogni sotto-task
- Parallelizzazione: task indipendenti pianificati per esecuzione simultanea
- Memoria condivisa: runtime/memory/ + runtime/projects/<id>/state.json
- Royal directives: Conductor emette direttive prioritizzate (CRITICAL/HIGH/NORMAL)

### Convenzioni di nomenclatura
- Direzioni: D1..D8 · Team: Tx.y · Agenti: Tx.y-Ann (es. T2.5-A01)
- Stati task: PENDING → RUNNING → REVIEW → DONE | FAILED
- Priorità: CRITICAL > HIGH > NORMAL > LOW

---

## 10 PATTERN ARCHITETTONICI CHIAVE (da replicare per DE)

1. **Team canonico con schema fisso**: ogni team ha coordinator, agents con input/output espliciti, acceptance criteria, failure handling, shared_state
2. **Handoff contract**: ogni passaggio tra team è un messaggio strutturato con acceptance criteria `{from, to, payload, acceptance_criteria}`
3. **Dry run mode**: ogni workflow ha modalità stima-costo senza effetti reali (`--dry`)
4. **Gate obbligatorio**: niente esce senza passare per QA/compliance gate (D5)
5. **ReasoningBank / Self-Improvement**: ogni fallimento loggato e distillato in pattern per non ripetersi (D6.3)
6. **Skill come knowledge layer separato**: lo stesso skill è usabile da più agenti in più reparti
7. **Progressive disclosure nel SKILL.md**: kernel ≤500 righe, tutto il dettaglio in `references/`
8. **Invariant cardinali**: regole non negoziabili scritte esplicitamente nel SKILL.md
9. **Cost guard**: agente dedicato al budget che blocca prima di sforare (T3.2)
10. **Sentinels / Verificatori always-on**: agenti di monitoraggio sempre accesi (V1 Integrity + V2 Output QA + V3 Memory Auditor)

---

## CONFRONTO EXPONIUM CF vs DIGITAL EMPIRE

| Ecosistema CF | Ruolo in DE | Delta aggiunto per DE |
|---|---|---|
| STUDIO (D2) | Creazione contenuti | Multi-brand, multi-cliente |
| GROWTH (D4) | Marketing + copy APSOC | Outreach agency, lead gen |
| INTELLIGENCE (D7) | Research e trend | Competitive intel per clienti |
| PLATFORM (D8) | Engineering | Produzione SaaS, Second Brain prodotto |
| FORGE (D6.4) | Crea nuovi team | Crea interi info products (corsi, ebook) |
| OPERATIONS (D3) | Runtime e massa | Gestione multi-progetto multi-cliente |
| ❌ assente | — | CLIENT DELIVERY (reparti CRO, delivery sprint) |
| ❌ assente | — | SALES (outreach, funnel, onboarding clienti) |
| ❌ assente | — | PRODUCT (info products: corsi, ebook, membership) |

CF è mono-scopo (solo lancio Exponium). DE deve essere multi-scopo: Agency + Info Products + SaaS.

---

## STATO BUILD (2026-06-09)

| Build | Cosa | Stato |
|---|---|---|
| BUILD 1 | Fondamenta (company/org, cartelle) | ✅ COMPLETATO |
| BUILD 2 | Orchestratore minimo (conductor, bus, state) | ✅ COMPLETATO & TESTATO |
| BUILD 3 | MVP UGC reale (video prodotto 2026-05-29) | ✅ COMPLETATO & TESTATO |
| BUILD 4 | Reparti supporto (D1, D7, D4) | ✅ COMPLETATO & TESTATO |
| BUILD 5 | QA avanzato + lint | ⏳ PROSSIMO |
| BUILD 6 | Self-improvement attivo | ⏳ |
| BUILD 7 | Editing pro, video t2v, product | ⏳ |
| BUILD 8 | GitHub | ⏳ |

### Cosa manca ancora
- BUILD 5-8 da completare
- Prima produzione con budget reale allocato (completato solo test a 12 crediti)
- Audio/TTS nel montaggio
- Auto-pubblicazione social (API Instagram/TikTok/YouTube)
- Dati reali per D7 INTELLIGENCE (oggi usa conoscenza generica)
- Dashboard web visuale
- FORGE esecutiva autonoma (D6.4 builders attivi)
