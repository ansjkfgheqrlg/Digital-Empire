# 📐 PLAN — Skill `content-forge` (comando `/forge`)

> Documento di pianificazione **prima** dell'architettura.
> Nessun file di skill viene scritto finché questo piano non è approvato.

---

## 0. TL;DR

Costruiamo una skill ufficiale (formato Anthropic, conforme a `skill-creator`) che:

1. Si attiva con il comando `/forge` o naturalmente (description "pushy").
2. Riceve in input contenuto grezzo, lungo, disordinato (tipicamente transcript YouTube in `.md`).
3. **NON riassume mai.** Estrae *tutto* il valore semantico, lo struttura, lo arricchisce con schemi/esempi/spiegazioni proprie, e lo riscrive da zero in forma più ampia, ordinata e completa del materiale originale.
4. Offre **8 target di trasformazione** (`doc`, `agent`, `team`, `skill`, `workflow`, `orchestration`, `wiki`, `custom`).
5. **🔑 Insight chiave**: ogni target non è generato in un'unica botta. Ogni target apre una **mini-conversazione strutturata**: plan → domande all'utente → architettura → costruzione iterativa. Esattamente come ci stiamo comportando noi due adesso. La skill è *meta-ricorsiva*: applica a sé stessa il pattern che insegna.

---

## 1. Intent e principi guida

### 1.1 Cosa NON è questa skill
- ❌ Un riassuntore. Riassunto = perdita di informazione. Proibito.
- ❌ Un re-formatter cosmetico.
- ❌ Una skill template "scrivi un .md di output". Deve avere logica di trasformazione vera.
- ❌ Materiale per *studiare* (l'output non si legge per imparare; è materia prima per costruire).
- ❌ Un sistema "one-shot" che ti sputa fuori l'artefatto. Per i target complessi (`agent`, `team`, `workflow`, `orchestration`, `wiki`) **deve dialogare**.

### 1.2 Cosa È questa skill
- ✅ Un **content engineering pipeline** componibile: input grezzo → atomi di conoscenza → riscrittura amplificata → artifact target.
- ✅ Un sistema che **estrae più di quanto è esplicito** (inferenza, esempi propri, schemi, controesempi, gerarchie).
- ✅ Un sistema che **conosce le "forme canoniche"** di ogni target: un agente non si scrive come una wiki.
- ✅ Un sistema **meta-ricorsivo**: per ogni target complesso, replica il pattern *"plan → ask → architect → build → critique → iterate"* che è lo stesso pattern di `skill-creator`.
- ✅ Un sistema **componibile**: blocchi (pattern + stage + target) che si combinano, non un monolite.

### 1.3 Principio chiave: "expansion over compression"
Per ogni unità informativa nel sorgente, l'output deve contenere:
- versione canonica/pulita della stessa informazione,
- + contesto implicito (cosa si dà per scontato),
- + almeno un esempio concreto (auto-generato se manca, etichettato),
- + uno schema/diagramma/decision-tree quando applicabile,
- + connessioni semantiche con altre unità.

Risultato: l'output è quasi sempre **più lungo** del sorgente, mai più corto.

### 1.4 Principio chiave 2: "interactive scaffolding" (l'insight nuovo)
Per i target complessi, la skill **non** genera l'output finale al primo turno. Segue il loop:

```
PLAN  ─►  ASK (domande mirate)  ─►  ARCHITECTURE (scheletro + contratti)
   ▲                                          │
   └────────  ITERATE  ◄──  CRITIQUE  ◄──  BUILD (riempimento)
```

Questo è esattamente lo stile di `skill-creator` e di come stiamo lavorando adesso.
La skill **insegna** il pattern *applicandolo*.

---

## 2. Casi d'uso reali → test cases

| # | Scenario | Input | Target tipico | Modalità |
|---|----------|-------|---------------|----------|
| 1 | 4 transcript YouTube su prompt engineering | `.md` ~30k token disordinato | `skill` o `doc` | Interattiva |
| 2 | Workshop 2h su cold outreach B2B | `.md` narrativo | `agent` o `workflow` | Interattiva |
| 3 | Serie articoli su sistemi RAG avanzati | `.md` misto, codice | `wiki` o `team` | Interattiva |
| 4 | "Voglio iniettarlo in un mio workflow esistente" | `.md` + descrizione workflow | `custom` (system prompt injection) | Interattiva |

---

## 3. Architettura concettuale (alto livello)

```
                      ┌─────────────────────────────────┐
                      │ INVOCAZIONE / COMANDO /forge    │
                      │ (input: contenuto [+target?])   │
                      └────────────────┬────────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │ STAGE 1 — INGESTION & NORMALIZATION         │
                │ (clean transcript noise, dedupe, segmenta)  │
                └──────────────────────┬──────────────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │ STAGE 2 — DEEP ANALYSIS (multi-pass)        │
                │ Applica P1..P9: extract → classify → map    │
                └──────────────────────┬──────────────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │ STAGE 3 — KNOWLEDGE GRAPH BUILD             │
                │ (atomi, relazioni, esempi, lacune)          │
                └──────────────────────┬──────────────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │ STAGE 4 — TARGET SELECTION                  │
                │ (se non dato: propone 1-3 target sensati)   │
                └──────────────────────┬──────────────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │ STAGE 5 — INTERACTIVE BUILD (per target)    │
                │  ┌─────────────────────────────────────┐    │
                │  │ 5a. PLAN del target                 │    │
                │  │ 5b. ASK (domande mirate)            │    │
                │  │ 5c. ARCHITECTURE (scheletro/contr.) │    │
                │  │ 5d. BUILD (riempimento)             │    │
                │  │ 5e. CRITIQUE (self-check)           │    │
                │  │ 5f. ITERATE (loop)                  │    │
                │  └─────────────────────────────────────┘    │
                └──────────────────────┬──────────────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │ STAGE 6 — COVERAGE & ANTI-SUMMARY CHECK     │
                │ (verifica oggettiva via scripts/)           │
                └──────────────────────┬──────────────────────┘
                                       │
                ┌──────────────────────▼──────────────────────┐
                │ STAGE 7 — PACKAGING & DELIVERY              │
                └─────────────────────────────────────────────┘
```

Ogni stage è un pattern modulare caricato via *progressive disclosure*: in `SKILL.md` resta solo il routing; le istruzioni dettagliate stanno in `references/stages/`.

---

## 4. I 9 pattern cognitivi (il "cervello")

| Pattern | Cosa fa | Quando si applica |
|---|---|---|
| **P1 — Atomic Concept Extraction** | Spezza il contenuto in "atomi" concettuali indivisibili (alla Andy Matuschak) | Sempre, stage 2 |
| **P2 — Claim → Evidence → Example** | Per ogni affermazione: tesi + supporto + esempio (genera quelli mancanti, etichettati) | Sempre |
| **P3 — Hierarchy & Dependency Mapping** | Gerarchia prerequisiti tra concetti | Sempre, alimenta il KG |
| **P4 — Steel-manning & Counter-examples** | Per ogni tesi: migliore obiezione + risposta | Doc, wiki, skill |
| **P5 — Procedural Decomposition** | Trasforma "how-to" in step + decision points + failure modes | Agent, workflow, skill |
| **P6 — Mental Model Surfacing** | Estrae i modelli mentali impliciti dell'autore originale | Sempre |
| **P7 — Schema/Diagram Generation** | Per ogni concetto strutturato: schema (ASCII/mermaid/tabella) | Doc, wiki, skill |
| **P8 — Cross-Reference Weaving** | Link semantici interni + suggerimenti di link esterni alla wiki | Wiki, doc |
| **P9 — Target-Shape Mapping** | Conosce la "forma canonica" di ogni target e ci mappa sopra il KG | Stage 5 |

Ogni pattern in `references/patterns/Pn-<name>.md` spiega *perché* serve, *quando* applicarlo, *quando saltarlo* (no MUST rigidi).

---

## 5. Gli 8 sub-generator (Stage 5 in dettaglio) — TUTTI interattivi

Ogni target ha la sua forma canonica e il suo **playbook conversazionale** in `references/targets/<target>.md`. Il playbook contiene 6 sezioni standard:

```
PLAN     — Cosa stiamo per costruire (3-10 righe)
ASK      — Le 3-6 domande da fare all'utente prima di partire
ARCH     — Lo scheletro file/struttura proposto (vuoto)
BUILD    — Come riempire ogni componente, in che ordine
CRITIQUE — Cosa controllare (checklist + script)
ITERATE  — Cosa chiedere all'utente per il prossimo giro
```

### 5.1 `doc` — Expanded Markdown Document
- Output: `.md` strutturato (TOC + sezioni + esempi + schemi + glossario + FAQ + cross-ref).
- Garantisce: lunghezza ≥ sorgente, coverage 100% degli atomi.
- Interattività: leggera (PLAN + ASK rapido su stile/registro/target audience).

### 5.2 `agent` — Single Agent Spec
- Output: cartella con `agent.md` (role, goals, instructions, tools, examples, constraints, failure modes), `system_prompt.md`, `eval_cases.json`.
- ASK tipico: "Che strumenti ha l'agente? Su che modello gira? Chi è l'utente finale dell'agente? Quali sono i suoi failure mode noti?"
- Mappa: P5 + P6 + P9 → "agent shape".

### 5.3 `team` — Multi-Agent Team
- Output: `team/` con `coordinator.md`, `agents/<role>.md` (n agenti), `communication_protocol.md`, `handoff_rules.md`.
- ASK: "Quanti agenti? Topologia (supervisor / peer-to-peer / pipeline)? Storage condiviso?"

### 5.4 `skill` — Anthropic Official Skill
- Output: skill conforme a `skill-creator.md`: `SKILL.md` + frontmatter + `references/` + `scripts/` se servono + `evals/evals.json`.
- ASK: "Comando? Quando deve triggerare? Ha bisogno di script eseguibili?"
- Meta: questo sub-generator usa `skill-creator` stesso come reference interna.

### 5.5 `workflow` — Complete Workflow
- Output: `workflow/` con `flow.md` (DAG), `agents/`, `skills/`, `triggers.md`, `state.md`, `error_handling.md`.
- ASK: "Trigger (cron, webhook, manuale)? Dove vive lo stato? Cosa succede agli errori?"

### 5.6 `orchestration` — Orchestration Layer
- Output: `orchestration/` con `supervisor.md` (router/planner), `registry.md`, `policies.md`, `observability.md`.
- ASK: "Quali workflow/agenti esistono già da orchestrare? Politiche di routing? Budget/quota?"

### 5.7 `wiki` — Second Brain (Obsidian)
- Output: note atomiche in formato Obsidian (markdown + `[[wikilinks]]` + frontmatter YAML), una nota per atomo (P1), MOC (Map of Content) generato, tag coerenti.
- ASK: "Dove vivono le note? (cartella vault) Tag convention esistente? Template di nota esistente?"

### 5.8 `custom` — Custom Injection
- Output: dipende. Tipicamente system prompt da iniettare in un workflow esistente, snippet, configurazione.
- ASK: "Dove va iniettato? Quale forma deve avere? (system prompt / user message / config block)"

---

## 6. Modalità di invocazione

1. **Esplicita con argomenti**:
   `/forge <path-to-content> --target=skill --name="prompt-engineering-101"`
2. **Esplicita conversazionale**:
   "Forge, prendi `transcripts.md` e trasformalo in un team di agenti."
3. **Implicita** (description pushy):
   Trigger su frasi tipo "ho dei transcript da trasformare in…", "voglio estrarre tutto da questo materiale e farne…".

Se l'utente **non specifica il target**, la skill esegue Stage 1-4 e poi propone 1-3 target con razionale. Mai output diretto senza scelta.

---

## 7. Anti-pattern espliciti (guardrails in `SKILL.md`)

- 🚫 Mai output più corto del sorgente in modalità `doc`/`wiki`.
- 🚫 Mai usare "in sintesi", "riassumendo", "in breve" come modalità operativa.
- 🚫 Mai saltare atomi del sorgente (coverage check obbligatorio in Stage 6).
- 🚫 Mai inventare fatti non presenti nel sorgente — ma *può* (e deve) generare esempi, schemi, controesempi propri, **etichettandoli come tali** ("➕ Esempio generato da Forge").
- 🚫 Mai produrre artefatti incompleti per il target scelto.
- 🚫 Mai saltare la fase ASK per i target complessi (`agent`, `team`, `workflow`, `orchestration`, `wiki`).

---

## 8. Struttura file proposta

```
content-forge/
├── SKILL.md                          # routing principale, ≤500 righe
├── references/
│   ├── stages/
│   │   ├── 01-ingestion.md
│   │   ├── 02-analysis.md
│   │   ├── 03-knowledge-graph.md
│   │   ├── 04-target-selection.md
│   │   ├── 05-interactive-build.md   # il loop PLAN→ASK→ARCH→BUILD→CRITIQUE→ITERATE
│   │   ├── 06-coverage-check.md
│   │   └── 07-packaging.md
│   ├── patterns/
│   │   ├── P1-atomic-extraction.md
│   │   ├── P2-claim-evidence-example.md
│   │   ├── P3-hierarchy-dependency.md
│   │   ├── P4-steelmanning.md
│   │   ├── P5-procedural-decomposition.md
│   │   ├── P6-mental-model-surfacing.md
│   │   ├── P7-schema-generation.md
│   │   ├── P8-cross-reference.md
│   │   └── P9-target-shape-mapping.md
│   ├── targets/                      # i playbook conversazionali
│   │   ├── doc.md
│   │   ├── agent.md
│   │   ├── team.md
│   │   ├── skill.md
│   │   ├── workflow.md
│   │   ├── orchestration.md
│   │   ├── wiki.md
│   │   └── custom.md
│   └── schemas/
│       ├── knowledge-graph.schema.json
│       ├── agent.schema.md
│       ├── team.schema.md
│       ├── workflow.schema.md
│       ├── orchestration.schema.md
│       └── wiki-note.schema.md
├── assets/
│   ├── templates/                    # template scheletro per ogni target
│   │   ├── doc.template.md
│   │   ├── agent/
│   │   ├── team/
│   │   ├── skill/
│   │   ├── workflow/
│   │   ├── orchestration/
│   │   └── wiki-note.template.md
│   └── examples/                     # 1 esempio end-to-end per target (più avanti)
├── scripts/
│   ├── coverage_check.py             # verifica atomi del sorgente nell'output
│   ├── atomizer.py                   # spezza il sorgente in atomi (opzionale, supporto)
│   ├── no_summary_lint.py            # cerca parole-bandiera vietate
│   └── package_target.py             # impacchetta l'output finale
└── evals/
    └── evals.json                    # test cases (§2)
```

---

## 9. Test cases preview

4 test, uno per macro-target:
1. Transcript YouTube prompt-engineering → `skill`
2. Workshop cold outreach → `agent`
3. Serie articoli su RAG → `wiki`
4. Tutorial multi-tool → `workflow`

Assertion oggettive (eseguibili via script):
- `coverage_check.py`: ≥ 95% degli atomi del sorgente compaiono nell'output
- `no_summary_lint.py`: zero occorrenze di parole-bandiera
- output ≥ lunghezza input (per `doc`/`wiki`)
- presenza dei file canonici del target (es. `agent.md` + `system_prompt.md` + `eval_cases.json` per `agent`)
- esempi auto-generati etichettati con marker (`➕ Generato da Forge`)

---

## 10. Roadmap di costruzione

| Fase | Cosa produciamo | Stato |
|---|---|---|
| **0. PLAN** | questo documento | ✅ approvato |
| **1. ARCHITECTURE** | scheletro file completo, indici, contratti tra stage, frontmatter | ⏭ **NEXT** |
| **2. CORE WRITING** | `SKILL.md` + `references/stages/` + `references/patterns/` (contenuti) | |
| **3. TARGETS** | `references/targets/*` + template in `assets/` | |
| **4. SCRIPTS & EVALS** | `scripts/*.py` + `evals/evals.json` | |
| **5. TEST & ITERATE** | run dei 4 test case + revisione + ottimizzazione description | |
| **6. PACKAGING** | `.skill` finale via `package_skill.py` | |

---

## 11. Decisioni confermate

| Decisione | Valore |
|---|---|
| Nome skill | `content-forge` |
| Comando | `/forge` |
| Wiki format | **Obsidian** (markdown + `[[wikilinks]]` + YAML frontmatter) |
| Ambiente | **Claude Code** (subagents, scripts, browser — versione full) |
| Modalità per target | **Interattiva-iterativa** (PLAN → ASK → ARCH → BUILD → CRITIQUE → ITERATE) per *tutti* i target complessi |
