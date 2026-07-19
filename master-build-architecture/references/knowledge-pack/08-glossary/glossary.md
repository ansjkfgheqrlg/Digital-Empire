# Glossary — Skill Planning & Architecture

> Termini chiave usati in tutto il knowledge pack. Letti **prima** di tutto il resto.

## A

### Agent
Un sottosistema specializzato (LLM + system prompt + tools opzionali) che svolge una funzione cognitiva singola dentro una skill. Diverso da "script": un agente fa giudizi, uno script esegue logica deterministica.

### Anti-pattern
Pattern ricorrente che **sembra** giusto ma produce esiti negativi. Catalogato esplicitamente per essere evitato. Esempi: "scaffold as deliverable", "permissive schemas".

### Atom (Knowledge Atom)
Unità informativa indivisibile estratta dal sorgente. Ispirato a Evergreen Notes (Andy Matuschak): un atomo = un concetto. Granularità tipica: 60-200 parole nel sorgente.

### ASK Phase
Fase del loop interactive scaffolding in cui un agente fa domande mirate all'utente per raccogliere input mancanti prima di costruire. Generata dinamicamente da un agente dedicato (Question Designer), non da checklist statica.

## B

### Builder Agent
Famiglia di agenti specializzati nella **costruzione** di un target specifico. In content-forge: B1 doc-builder, B2 agent-builder, ecc. Uno per ogni target canonico.

## C

### Canonical Form
Struttura standard di file/sezioni/campi che un certo tipo di output deve avere per essere considerato "completo". Validata da schema. Esempio: un agente ha 7 file canonici (agent.md, system_prompt.md, tools.md, playbook.md, failure_modes.md, eval_cases.json, README.md).

### Conductor
Il **coordinatore principale** di una skill complessa. È l'istanza LLM che ha invocato la skill (L1), non un sottoagente spawnato. Decide quale agente attivare quando, mantiene lo stato del run, parla con l'utente.

### Coverage
Percentuale di atomi del Knowledge Graph che compaiono nell'output finale. Verificata da check lessicale + semantico. Soglie tipiche: 85-100% per target.

### Critique (Self-Critique)
Step di un agente in cui rilegge il proprio output con "occhi nuovi" cercando issue specifici. Diverso da critique esterna (fatta da agenti QA dedicati).

## D

### Depth Pass
Stage in cui agenti optimizer rifiniscono l'output del builder. Inventato in Phase 9 per risolvere il problema di "skill che escono magre" anche se sintatticamente valide.

### Discovery (in pipeline)
Fase iniziale di analisi del sorgente, prima di produrre output. In content-forge: Stage 1-4 (Ingestion → Analysis → KG → MKD).

## F

### Failure Mode
Modo specifico in cui un agente/skill può fallire, documentato in tabella con: failure | sintomo | prevenzione | rilevamento | recupero. Cittadino di prima classe nella documentazione di ogni agente.

### Formula Validator
Agente (O5 in content-forge) che verifica che i framework/formule citati dal sorgente siano applicati **completamente** nell'output (es. CPB = Claim + Proof + Benefit, devono esserci tutti e tre).

### Frontmatter
Blocco YAML in cima a un file markdown con metadata strutturati (name, description, agent_id, ecc.). Parsato da validator e agenti.

## H

### Humanizer
Agente (O4 in content-forge) che elimina LLM-speak dall'output ("leverage", "comprehensive", "In summary", aperture stereotipate). Condizionale: attivo solo se output è human-facing.

## I

### Interactive Scaffolding
Pattern operativo: invece di generare un artefatto complesso in un colpo, l'agente apre una mini-conversazione strutturata (PLAN → ASK → BUILD → CRITIQUE → ITERATE). La skill insegna il pattern applicandolo a sé stessa.

## K

### Kernel (di una skill)
Il file principale `SKILL.md`. Snello (≤500 righe Anthropic recommendation), contiene routing e invariant. Tutto il resto in references/ on-demand.

### Knowledge Graph (KG)
Output di Stage 3: struttura machine-readable con atoms, clusters, edges, gaps. È la lingua franca consumata da tutti gli agenti successivi.

### Knowledge Pack
Cartella di conoscenza strutturata pensata per essere **input** ad altre skill o reference per umani. Diversa da una skill: non ha SKILL.md, non si attiva, è dati.

## M

### Master Knowledge Document (MKD)
🌟 Concetto cardine introdotto in PLAN-v5. Documento ampliato del sorgente, prodotto **sempre** prima di andare al target finale. Base canonica da cui tutti i builder attingono. Ampliamento (mai compressione) del contenuto sorgente.

### Meta-recursive
Proprietà di una skill che usa pattern propri per produrre sé stessa o altre skill. Esempio: `content-forge` con target=skill può produrre altre skill applicando il suo stesso processo.

## N

### No-Summary Principle
Postura culturale anti-LLM: l'output rispetta o supera la lunghezza del sorgente. Espansione, non compressione. Anti-pattern: usare "in sintesi", "riassumendo", "tldr". Enforced via lint automatico.

## O

### Optimizer Agent
Famiglia di agenti (Ox in content-forge) attivi in Stage 7 dopo il builder. Lavorano in-place sull'output draft del builder per arricchirlo prima della QA.

### Orchestration Layer
Target/concetto: livello sopra workflow e agenti che decide dinamicamente quale invocare in base a routing rules + policies + budget. Richiede un registry di componenti esistenti.

## P

### Pattern (Architecture Pattern)
Soluzione ricorrente a problema ricorrente, documentata con shape + when to apply + trade-off + esempi. Diverso da principio (più astratto) e processo (più sequenziale).

### Pipeline Stage
Una fase numerata del processo end-to-end di una skill. Esempio: content-forge ha 10 stage (Ingestion → ... → Self-Improvement). Ogni stage ha input atteso, output prodotto, contract con stage successivo.

### Principle (Architecture Principle)
Asserzione fondante che guida decisioni di design. Più astratto di un pattern. Esempio: "Progressive Disclosure" è un principio, "Conductor with Subagents" è un pattern.

### Progressive Disclosure
Principio Anthropic: caricare conoscenza on-demand. SKILL.md snello, references/ caricato solo quando serve, scripts/ chiamati solo quando applicabili. Mira a non saturare il context window inutilmente.

### Pushy Description
Description del frontmatter di una skill scritta in modo "aggressivo" per combattere undertriggering. Usa marker tipo "make sure", "whenever", "even if", "do not use". Anthropic recommendation per evitare che skill utili non triggerino.

## Q

### QA (Quality Assurance, in pipeline)
Stage di validazione esterna dell'output prodotto da builder + optimizer. In content-forge: Stage 8 con C1 coverage-verifier + C3 schema-validator in parallelo.

### Question Designer
Agente (D1 in content-forge) che genera dinamicamente le domande della ASK phase basandosi sul KG specifico del run. Non checklist statica.

## R

### Reference (in skill)
File markdown caricato on-demand dal Conductor. Vive in `references/`. Organizzato per categoria: stages/, patterns/, processes/, schemas/, conventions/, external/.

### RACI Strict
Pattern per design di team multi-agente: ogni responsabilità ha **un solo agente Responsible**. Niente overlap. Validato meccanicamente.

## S

### Scaffold
Output strutturalmente valido ma con contenuto magro o placeholder. **Anti-pattern**: chiamarlo "skill" quando in realtà è scaffold. La differenza la fa il content depth.

### Schema (in content-forge)
File JSON Schema Draft 2020-12 + companion file markdown human-readable. Per ogni target c'è uno schema canonico. Tightening v0.3 in Phase 9 ha aggiunto vincoli stringenti su content (parole min, file min, ecc.).

### Self-Improvement Loop
Stage 10 in content-forge: il sistema osserva sé stesso, logga failure mode, fa triage, genera piani di phase future. **Senza azione manuale dell'utente.** Silenzioso e condizionale.

### Shape (Target Shape)
Forma canonica di un certo tipo di artefatto. Esempio: shape di un agente = 7 file canonici con sezioni specifiche. Mappata via Pattern P9 (Target-Shape Mapping).

### Specialist Agent
Subagente con scope ristretto e ben definito. Spawnato dal Conductor via Task tool. Opposto di "general purpose agent".

### Stage
Vedi Pipeline Stage.

### Steel-manning (P4 pattern)
Tecnica argomentativa: per ogni claim, generare la **migliore obiezione possibile** e una risposta forte. Anti-pattern: "straw-manning" (formulare obiezione debole per smontarla facilmente).

## T

### Target
In content-forge: tipo di artefatto finale richiesto dall'utente. 8 target canonici: doc, agent, team, skill, workflow, orchestration, wiki, custom.

### Three-Level Architecture
Pattern di organizzazione di una skill complessa: L1 Conductor (caller) + L2 Specialists (subagenti) + L3 Tools (script Python). Ogni livello ha responsabilità distinte.

### Triage (di failure mode)
Processo di categorizzazione di un failure mode appena loggato: assegna severity (blocker/major/minor), category, scope (hotfix/phase-N), confidence, effort. In content-forge fatto da SI2 automaticamente.

## U

### Undertriggering
Tendenza degli LLM a NON invocare una skill quando in realtà sarebbe utile. Combattuta con description "pushy" e ottimizzazione iterativa della description.

## V

### Validator (Schema Validator)
Componente che verifica se un output rispetta lo schema canonico del target. In content-forge: C3 agent + scripts/schema_validator.py. Bloccante: se schema fail, pipeline non procede.

---

## Sigle agenti ricorrenti (in content-forge come esempio)

| Sigla | Famiglia | Nome |
|---|---|---|
| A1 | Pipeline | ingestion-agent |
| A2 | Pipeline | analyst-agent |
| A3 | Pipeline | knowledge-graph-agent |
| A4 | Pipeline | target-advisor-agent |
| A5 | Pipeline | mkd-builder-agent |
| B1-B8 | Builders | doc/agent/team/skill/workflow/orchestration/wiki/custom-builder-agent |
| C1, C3 | QA | coverage-verifier, target-schema-validator |
| D1 | Meta | question-designer-agent |
| O1-O5 | Optimizers | skill-depth, agent-depth, reference-expander, humanizer, formula-validator |
| SI1-SI3 | Self-Improvement | failure-detector, triage, phase-planner |

---

## Sigle nel knowledge pack

| Sigla | Significato |
|---|---|
| **P01-P15** | Principles (in `01-principles/`) |
| **PT01-PT11** | Patterns (in `02-patterns/`) |
| **AP01-AP09** | Anti-patterns (in `03-anti-patterns/`) |
| **PR01-PR07** | Processes (in `04-processes/`) |
| **DT01-DT06** | Decision Trees (in `05-decision-trees/`) |
| **CS01-CS04** | Case Studies (in `06-case-studies/`) |
