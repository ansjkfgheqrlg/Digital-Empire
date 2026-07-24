# 📐 PLAN v2 — Skill `content-forge` (comando `/forge`)

> **Cosa cambia rispetto a v1:**
> 1. ➕ Architettura **multi-agente** esplicita: ruoli, responsabilità, system prompt, modalità di spawn (§4).
> 2. ➕ **Processo completo per ogni singolo target** (8 processi end-to-end, §6).
> 3. ➕ Inventario **scripts** e **references** con razionale puntuale per ognuno (§7-8).
> 4. ➕ Diagramma di **flusso di controllo** tra Conductor e agenti (§5).

---

## 0. Filosofia rivista

Una skill `content-forge` ben fatta non è "un grosso prompt in `SKILL.md`". È un **sistema operativo cognitivo** in cui:

- `SKILL.md` è il **kernel** (routing minimale + invarianti + handoff).
- Gli **agenti** in `agents/` sono **processi specializzati** che si spawnano via il Task tool di Claude Code.
- Gli **scripts** in `scripts/` sono **operazioni deterministiche** (verifiche, parsing, packaging) — fanno ciò che gli LLM fanno male o lentamente.
- I **references** in `references/` sono **conoscenza on-demand** — caricati solo dall'agente che serve.
- I **templates** in `assets/templates/` sono **forme canoniche** dei target — non vengono compilati ciecamente ma usati come scaffolding.

> Stessa filosofia di Anthropic skill-creator (che ha `agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md`, `scripts/aggregate_benchmark.py`, ecc.). Stiamo aderendo a un pattern già provato.

---

## 1-3. (Invariate da v1)

Conservate da PLAN.md: intent, 9 pattern cognitivi P1-P9, 8 target. Non rielaboro per brevità.

---

## 4. 🤖 Architettura multi-agente (la parte mancante in v1)

### 4.1 Modello di esecuzione

`content-forge` usa **3 livelli di esecuzione**:

| Livello | Chi esegue | Cosa esegue | Esempio |
|---|---|---|---|
| **L1 — Conductor** | l'istanza principale di Claude che ha invocato la skill | routing, decisioni, dialogo con l'utente, ASK phase | "Quale target vuoi?" |
| **L2 — Specialist Agents** | subagenti spawnati via Task tool | lavoro cognitivo specializzato e isolato | analisi, build di un target, critica |
| **L3 — Scripts** | Python via Bash | operazioni deterministiche e veloci | coverage check, lint, packaging |

Gli L2 sono **stateless tra loro**: il Conductor passa loro i file di lavoro (KG, atoms, drafts) come input e raccoglie l'output su disco in `<workspace>/forge-run-<timestamp>/`.

### 4.2 Inventario degli agenti — **12 agenti specializzati**

Divisi in 4 famiglie. Ognuno ha un file in `agents/<nome>.md` con il proprio system prompt.

#### 🅰️ Family A — Pipeline cognitiva (4 agenti, sequenziali)

| # | Agente | Ruolo | Quando spawnato | Output |
|---|---|---|---|---|
| **A1** | `ingestion-agent` | Pulisce trascript (rimuove timestamp, filler, ripetizioni vocali), de-duplica, segmenta in chunk semantici | Stage 1, sempre | `cleaned.md`, `chunks.json` |
| **A2** | `analyst-agent` | Applica P1-P9 ai chunk. **Spawnato in parallelo** (1 per chunk se il sorgente è grande) | Stage 2, sempre | `atoms-<chunk>.json` |
| **A3** | `knowledge-graph-agent` | Assembla gli atomi in un grafo coerente: deduplica, collega, gerarchizza, individua lacune | Stage 3, sempre (1 istanza) | `kg.json`, `kg.md` (vista umana) |
| **A4** | `target-advisor-agent` | Legge il KG, propone 1-3 target con razionale tipo "questo contenuto è soprattutto procedurale → adatto a `agent` o `workflow`" | Stage 4, solo se l'utente non ha specificato il target | `recommendation.md` |

#### 🅱️ Family B — Target builders (8 agenti, 1 per target — il cuore operativo)

Ogni builder **possiede il processo end-to-end** del suo target. Vedi §6 per i processi.

| # | Agente | Target | Quando |
|---|---|---|---|
| **B1** | `doc-builder-agent` | `doc` | Stage 5 |
| **B2** | `agent-builder-agent` | `agent` | Stage 5 |
| **B3** | `team-builder-agent` | `team` | Stage 5 |
| **B4** | `skill-builder-agent` | `skill` | Stage 5 |
| **B5** | `workflow-builder-agent` | `workflow` | Stage 5 |
| **B6** | `orchestration-builder-agent` | `orchestration` | Stage 5 |
| **B7** | `wiki-builder-agent` | `wiki` (Obsidian) | Stage 5 |
| **B8** | `custom-builder-agent` | `custom` | Stage 5 |

Solo **uno** dei B viene spawnato per run (in base al target scelto). Il Conductor gli passa: KG, atoms, risposte dell'utente alla ASK phase, template del target.

#### 🅲 Family C — Quality & Verification (3 agenti, post-build)

| # | Agente | Ruolo | Quando |
|---|---|---|---|
| **C1** | `coverage-verifier-agent` | Verifica che ogni atomo del KG sia coperto nell'output. Riceve `kg.json` + output. Lavora insieme allo script `coverage_check.py` (script trova match grezzi, agente decide se la copertura è semantica o solo lessicale) | Stage 6, sempre |
| **C2** | `quality-critic-agent` | QA indipendente: legge l'output con occhi nuovi, lo critica rispetto agli anti-pattern (riassunto, semplificazione, esempi mancanti). Restituisce lista di rilievi azionabili | Stage 6, sempre |
| **C3** | `target-schema-validator-agent` | Verifica che l'output rispetti la forma canonica del target (es. per `agent`: presenza di `agent.md` + `system_prompt.md` + `eval_cases.json` con campi obbligatori) | Stage 6, sempre |

#### 🅳 Family D — Meta-coordinatori (2 agenti, su richiesta)

| # | Agente | Ruolo | Quando |
|---|---|---|---|
| **D1** | `question-designer-agent` | Genera la lista di domande della **ASK phase** in modo intelligente — non un questionario fisso, ma domande che dipendono da cosa il KG dice del contenuto. Es: se non c'è nessun riferimento a tool esterni, non chiede "che strumenti userà l'agente?" come domanda secca, ma "ho notato che il contenuto non parla di strumenti — l'agente ne deve usare? Quali?" | Stage 5, inizio di ogni target |
| **D2** | `conductor` (è una pseudo-agente: è il main Claude, ma con il suo system prompt definito in `agents/conductor.md`) | Coordinatore principale. Non spawnato — è chi spawna gli altri. Il suo SP definisce: come scegliere quale agente spawnare, come passare lo stato, come gestire fallimenti, come parlare all'utente | Sempre attivo |

**Totale: 12 agenti** (4 pipeline + 8 builder + 3 QA + 1 designer) + il Conductor (che è il caller della skill stessa).

### 4.3 Modalità di spawn e isolamento

- **Pipeline cognitiva** (A1, A2, A3, A4): sequenziale. A2 può fan-out in parallelo se il sorgente supera 20k token.
- **Builder** (B*): uno solo per run, ma può a sua volta spawnare sub-task (es. `skill-builder-agent` può spawnare il `quality-critic-agent` su una bozza per critica intermedia).
- **QA** (C1, C2, C3): spawnati in parallelo a fine build.
- **Question designer** (D1): spawnato una volta per target, all'inizio della ASK phase.

Tutti gli agenti L2 ricevono:
- path al workspace `<workspace>/forge-run-<ts>/`
- riferimenti specifici da leggere (es. `references/patterns/P5-procedural-decomposition.md`)
- istruzioni di output: dove scrivere e in che formato

---

## 5. Diagramma di flusso di controllo

```
┌──────────────────────────────────────────────────────────────────┐
│                          CONDUCTOR (L1)                          │
│  • legge SKILL.md • parla con l'utente • spawna agenti L2        │
│  • mantiene stato in <workspace>/forge-run-<ts>/state.json       │
└────────────────────────────────┬─────────────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        ▼                        ▼                        ▼
   ┌─────────┐    ┌──────────────────────────┐    ┌──────────────┐
   │ Stage 1 │───▶│  A1 ingestion-agent      │───▶│ cleaned.md   │
   └─────────┘    └──────────────────────────┘    │ chunks.json  │
                                                  └──────┬───────┘
        ┌─────────────────────────────────────────────────┘
        ▼
   ┌─────────┐    ┌──────────────────────────┐    ┌──────────────┐
   │ Stage 2 │═══▶│  A2 analyst-agent ×N     │───▶│ atoms-*.json │
   └─────────┘    │  (parallelo su chunk)    │    └──────┬───────┘
                  └──────────────────────────┘           │
        ┌─────────────────────────────────────────────────┘
        ▼
   ┌─────────┐    ┌──────────────────────────┐    ┌──────────────┐
   │ Stage 3 │───▶│  A3 knowledge-graph      │───▶│ kg.json      │
   └─────────┘    └──────────────────────────┘    │ kg.md        │
                                                  └──────┬───────┘
        ┌─────────────────────────────────────────────────┘
        ▼
   ┌─────────┐    ┌──────────────────────────┐
   │ Stage 4 │───▶│  A4 target-advisor       │──▶ Conductor mostra
   └─────────┘    │  (solo se target ignoto) │    proposta all'utente
                  └──────────────────────────┘    + raccoglie scelta
        │
        ▼
   ┌─────────┐    ┌──────────────────────────┐
   │ Stage 5 │───▶│  D1 question-designer    │──▶ Conductor pone
   │  (ASK)  │    │  (per il target scelto)  │    domande all'utente
   └─────────┘    └──────────────────────────┘
        │
        ▼
   ┌─────────┐    ┌──────────────────────────┐
   │ Stage 5 │───▶│  Bx target-builder       │───▶ output/ del target
   │ (BUILD) │    │  (1 dei 8)               │
   └─────────┘    └──────────────────────────┘
        │
        ▼
   ┌─────────┐    ┌──────────────────────────┐
   │ Stage 6 │═══▶│  C1 coverage-verifier    │┐
   │  (QA)   │    │  C2 quality-critic       │├─▶ qa-report.md
   └─────────┘    │  C3 schema-validator     │┘    (parallelo)
                  └──────────────────────────┘
        │
        ▼
   se PASS → Stage 7 packaging
   se FAIL → loop ITERATE: Bx riceve qa-report e rilavora
```

Legenda: `───▶` sequenziale, `═══▶` parallelo possibile.

---

## 6. 🛠️ Processi end-to-end per ciascun target (la seconda parte mancante)

Per **ogni target** definisco il processo completo: cosa fa il builder, in che ordine, con quali agenti di supporto, quali domande all'utente, quale forma canonica produce, come si verifica.

> Sintesi qui — la spiegazione completa di ciascun processo vivrà in `references/processes/<target>.md`.

### 6.1 Processo `doc` (Expanded Markdown Document)

**Builder**: `doc-builder-agent`

1. **PLAN interno**: definisce TOC dal KG (capitoli = cluster di atomi correlati, sezioni = atomi).
2. **ASK** (via D1): registro? audience? lunghezza minima? glossario sì/no? FAQ sì/no? lingua? convenzioni di formattazione (mermaid/ascii)?
3. **BUILD** (ordine):
   1. Scaffold TOC e frontmatter
   2. Per ogni capitolo: scrittura ampliata (P1+P2+P4+P7)
   3. Cross-reference interni (P8)
   4. Glossario auto-estratto
   5. FAQ generata da steel-manning (P4)
4. **CRITIQUE**: C1 (coverage), C2 (qualità), check lunghezza ≥ sorgente
5. **ITERATE**: rilavora sezioni segnalate

**Forma canonica output**:
```
output/
├── document.md          # il doc principale (TOC + tutto)
├── glossary.md          # auto-estratto
└── faq.md               # da steel-manning
```

---

### 6.2 Processo `agent` (Single Agent)

**Builder**: `agent-builder-agent`

1. **PLAN interno**: identifica nel KG la "agent shape" (role, scope, tools impliciti, failure modes menzionati).
2. **ASK** (via D1, personalizzato):
   - Nome dell'agente?
   - Modello target (Sonnet/Opus/Haiku/altro)?
   - Strumenti disponibili (filesystem/web/code execution/MCP custom)?
   - Utente finale (chi parla con l'agente)?
   - Criteri di successo misurabili?
   - Failure mode che già conosci e vuoi prevenire?
3. **BUILD**:
   1. `system_prompt.md` v0 — versione ricca, ampliata dal KG con P5+P6
   2. `agent.md` — role, goals, instructions, constraints, examples (P2), failure modes, tool use guidelines
   3. `eval_cases.json` — 8-15 casi generati dal KG (input prompt + expected behavior)
   4. `playbook.md` — esempi conversazionali realistici (P2 amplificato)
   5. Spawn **quality-critic** su `system_prompt.md` per round di critica
   6. Revisione system_prompt → v1
4. **CRITIQUE**: C1+C2+C3 (schema agente)
5. **ITERATE**: ripete dal punto 4 fino a OK utente

**Forma canonica output**:
```
output/
└── <agent-name>/
    ├── agent.md
    ├── system_prompt.md
    ├── eval_cases.json
    ├── playbook.md
    └── README.md          # come usarlo
```

---

### 6.3 Processo `team` (Multi-Agent Team)

**Builder**: `team-builder-agent`

1. **PLAN interno**: dal KG identifica **ruoli distinti** non sovrapposti (chi fa cosa).
2. **ASK** (via D1):
   - Topologia: supervisor / pipeline / peer-to-peer / hub-spoke?
   - Quanti agenti pensi servano? (proposta del builder + scelta utente)
   - Storage condiviso (filesystem/db/none)?
   - Protocollo di handoff (file-based / message-based)?
   - Modello per ogni ruolo (Opus per planner, Sonnet per worker, ecc.)?
   - Trigger del team (manuale / continuo)?
3. **BUILD**:
   1. `topology.md` — diagramma e razionale della topologia scelta
   2. `coordinator.md` — il system prompt del coordinatore (se topologia supervisor)
   3. `agents/<role>.md` — un file per ogni agente (system prompt + responsabilità + tools)
   4. `communication_protocol.md` — formato dei messaggi/file di handoff
   5. `handoff_rules.md` — chi passa cosa a chi, quando
   6. `failure_handling.md` — cosa fa il team se un agente fallisce
   7. `team_eval_cases.json` — scenari end-to-end
4. **CRITIQUE**: C1+C2+C3, più check di **disgiunzione dei ruoli** (no overlap)
5. **ITERATE**

**Forma canonica output**:
```
output/
└── <team-name>/
    ├── topology.md
    ├── coordinator.md
    ├── agents/
    │   ├── role-1.md
    │   ├── role-2.md
    │   └── ...
    ├── communication_protocol.md
    ├── handoff_rules.md
    ├── failure_handling.md
    ├── team_eval_cases.json
    └── README.md
```

---

### 6.4 Processo `skill` (Anthropic Official Skill — meta!)

**Builder**: `skill-builder-agent` (è meta: usa `skill-creator` come reference)

1. **PLAN**: dal KG identifica la "skill shape": quando dovrebbe triggerare? Cosa produce? Sequenza di passi che incapsula?
2. **ASK**:
   - Nome skill + comando di trigger?
   - Description "pushy" (parole di trigger naturali)?
   - Servono script Python? Quali?
   - Servono subagenti? Quali ruoli?
   - Test cases che già conosci?
3. **BUILD**:
   1. `SKILL.md` con frontmatter (name + description con anti-undertriggering wording)
   2. `references/` (suddivisione progressiva del KG)
   3. `agents/` se servono
   4. `scripts/` se servono (proposta dal builder, conferma utente)
   5. `assets/templates/` se ci sono forme canoniche di output
   6. `evals/evals.json` con 4-6 test prompts
4. **CRITIQUE**: C1+C2+C3 + verifica conformità a `skill-creator.md`
5. **ITERATE**

**Forma canonica output**: struttura identica a `content-forge` stessa (meta!).

---

### 6.5 Processo `workflow` (Complete Workflow)

**Builder**: `workflow-builder-agent`

1. **PLAN**: dal KG estrae il DAG dei passi (P5 è centrale qui).
2. **ASK**:
   - Trigger (cron, webhook, manuale, evento)?
   - Stato (dove vive: filesystem, db, queue)?
   - Idempotenza richiesta?
   - Step paralleli o tutto sequenziale?
   - Quali step richiedono un agente vs uno script vs una skill esistente?
   - Cosa succede agli errori (retry, fallback, alert, halt)?
   - Osservabilità (log, metriche)?
3. **BUILD**:
   1. `flow.md` — DAG human-readable con descrizione di ogni step
   2. `flow.mermaid` — diagramma
   3. `state.md` — schema dello stato + transizioni
   4. `triggers.md`
   5. `agents/` per ogni step che usa un agente
   6. `skills/` per ogni step che usa una skill (anche solo riferimento)
   7. `scripts/` per ogni step deterministico
   8. `error_handling.md`
   9. `observability.md`
   10. `runbook.md` — come operarlo in produzione
4. **CRITIQUE**: C1+C2+C3 + verifica completezza del DAG (nessun nodo orfano, nessun deadlock)
5. **ITERATE**

---

### 6.6 Processo `orchestration` (Orchestration Layer)

**Builder**: `orchestration-builder-agent`

1. **PLAN**: identifica i workflow/agenti che il layer deve orchestrare e le regole di routing dal KG.
2. **ASK**:
   - Quali workflow/agenti esistono già da orchestrare (utente li elenca)?
   - Routing rule-based o LLM-based?
   - Policies (budget, quota, priorità, sicurezza)?
   - SLA, fallback paths?
   - Observability stack?
3. **BUILD**:
   1. `supervisor.md` — system prompt del supervisor LLM (se LLM-based)
   2. `registry.md` — catalogo dei componenti orchestrati
   3. `routing.md` — regole di routing
   4. `policies.md` — budget, quote, priorità, security
   5. `observability.md` — log, metriche, tracing
   6. `failure_modes.md` — cosa va male e come si gestisce
4. **CRITIQUE**: C1+C2+C3
5. **ITERATE**

---

### 6.7 Processo `wiki` (Obsidian Second Brain)

**Builder**: `wiki-builder-agent`

1. **PLAN**: spezza il KG in atomi-nota (P1), uno per concetto. Identifica MOC candidati.
2. **ASK**:
   - Path del vault Obsidian?
   - Cartella di destinazione?
   - Tag convention esistente (es. `#area/...`, `#status/...`)?
   - Template di nota esistente da rispettare?
   - Naming convention dei file?
   - Lingua (italiano/inglese/mista)?
   - Vuoi MOC o solo note atomiche?
3. **BUILD**:
   1. Una nota per atomo: `<atom-slug>.md` con frontmatter YAML + body + `[[wikilinks]]` (P8)
   2. MOC: `MOC - <topic>.md` con struttura ad albero e link a tutte le note
   3. `index.md` di entry point
   4. **Verifica wikilink integrity** via `obsidian_packager.py` (no link rotti, slug normalizzati)
4. **CRITIQUE**: C1 (ogni atomo è una nota o è citato), C3 (frontmatter valido)
5. **ITERATE**

**Forma canonica output**:
```
output/
└── vault-import/
    ├── MOC - <topic>.md
    ├── index.md
    ├── atom-1.md
    ├── atom-2.md
    └── ...
```

L'utente trascina `vault-import/` nel suo vault Obsidian.

---

### 6.8 Processo `custom` (Custom Injection / escape hatch)

**Builder**: `custom-builder-agent`

1. **PLAN**: l'unico builder che ha PLAN dinamico, perché il target è ignoto.
2. **ASK** (più aperto del solito):
   - Cosa devo produrre? (system prompt? config block? snippet? altro?)
   - Dove andrà iniettato (descrivi il contesto/workflow esistente)?
   - Formato richiesto? Vincoli di lunghezza? Variabili da rispettare?
   - Esempio di qualcosa di simile che già esiste?
3. **BUILD**: artefatto su misura, sempre con copertura del KG e nessun riassunto.
4. **CRITIQUE**: C1+C2 (C3 saltato perché non c'è schema canonico) + check vincoli dell'utente.
5. **ITERATE**

---

## 7. 📜 Inventario scripts (8 script, con razionale)

Ogni script ha un motivo preciso: fa una cosa che agli LLM verrebbe male o costosa.

| # | Script | Razionale | Usato da |
|---|---|---|---|
| **S1** | `transcript_cleaner.py` | Rimozione deterministica di timestamp YouTube (`00:01:23`), filler ("uh", "you know", ripetizioni vocali). Fare questo con un LLM è uno spreco di token. | A1 ingestion-agent |
| **S2** | `atomizer.py` | Preprocessing NLP: segmentazione in periodi/paragrafi, estrazione N-grammi candidati come "atomi" da proporre all'A2. È un *supporto* all'analyst, non lo sostituisce. | A2 analyst-agent |
| **S3** | `coverage_check.py` | Confronta `kg.json` (atomi) vs output. Per ogni atomo cerca occorrenze lessicali + semantiche (embedding cosine). Restituisce report di copertura. Indispensabile per la garanzia "no riassunto". | C1 coverage-verifier |
| **S4** | `no_summary_lint.py` | Cerca parole-bandiera vietate ("in sintesi", "riassumendo", "in breve", "TL;DR"), pattern di compressione (es. "tre punti chiave:"), e segnala. | C1, C2 |
| **S5** | `length_check.py` | Verifica che lunghezza output ≥ lunghezza input nei target che lo richiedono (`doc`, `wiki`). | C1 |
| **S6** | `schema_validator.py` | Valida l'output del builder contro lo schema canonico del target (file presenti, frontmatter corretto, campi obbligatori). Usa `references/schemas/`. | C3 schema-validator |
| **S7** | `obsidian_packager.py` | Per il target `wiki`: normalizza slug dei file, verifica integrità dei `[[wikilinks]]`, genera MOC. Roba meccanica che un LLM sbaglierebbe. | B7 wiki-builder |
| **S8** | `package_target.py` | Assembla la cartella finale `output/`, fa zip/tar se richiesto, crea `README.md` di handoff. | Stage 7 packaging |

**Totale: 8 script.** Tutti hanno test inclusi in `scripts/tests/`.

---

## 8. 📚 Inventario references (con razionale di gruppi)

### 8.1 Stages (7) — `references/stages/`
Documentano il *cosa fa* di ogni stage del pipeline. Caricati dal Conductor solo quando entra in quello stage.

### 8.2 Patterns (9) — `references/patterns/`
I 9 framework cognitivi P1-P9. Caricati dagli analyst/builder solo quando applicano il pattern. Ognuno: cosa fa, perché serve, quando applicarlo, quando saltarlo, esempi.

### 8.3 Processes (8) — `references/processes/` ← **NUOVO in v2**
Un file per target con il processo end-to-end completo (versione lunga di §6 qui). Caricati solo dal builder corrispondente. **Questa è la sede dei "interi processi" che hai richiesto.**

### 8.4 Schemas (6) — `references/schemas/`
Forma canonica formale (validabile da `schema_validator.py`) di: `knowledge-graph`, `agent`, `team`, `skill`, `workflow`, `orchestration`, `wiki-note`. Caricati da C3.

### 8.5 Conventions (3) — `references/conventions/`
- `naming.md` — convenzioni di naming per file, slug, ID atomi
- `markdown-style.md` — convenzioni di formattazione
- `anti-patterns.md` — il catalogo completo degli anti-pattern con esempi reali

### 8.6 Skill-creator mirror (1) — `references/external/skill-creator.md`
Copia (o riferimento) della guida ufficiale `skill-creator.md`, usata da B4 `skill-builder-agent` come reference primaria.

**Totale: ~34 file di reference**, distribuiti secondo *progressive disclosure*: nessun agente carica più di 2-4 reference per task.

---

## 9. 📁 Struttura file finale (aggiornata v2)

```
content-forge/
├── SKILL.md                              # kernel: routing + invarianti, ≤500 righe
├── agents/                               # 🤖 12 agenti specializzati
│   ├── conductor.md                      # SP del coordinatore principale
│   ├── pipeline/
│   │   ├── ingestion-agent.md            # A1
│   │   ├── analyst-agent.md              # A2
│   │   ├── knowledge-graph-agent.md      # A3
│   │   └── target-advisor-agent.md       # A4
│   ├── builders/
│   │   ├── doc-builder-agent.md          # B1
│   │   ├── agent-builder-agent.md        # B2
│   │   ├── team-builder-agent.md         # B3
│   │   ├── skill-builder-agent.md        # B4
│   │   ├── workflow-builder-agent.md     # B5
│   │   ├── orchestration-builder-agent.md # B6
│   │   ├── wiki-builder-agent.md         # B7
│   │   └── custom-builder-agent.md       # B8
│   ├── qa/
│   │   ├── coverage-verifier-agent.md    # C1
│   │   ├── quality-critic-agent.md       # C2
│   │   └── target-schema-validator-agent.md # C3
│   └── meta/
│       └── question-designer-agent.md    # D1
├── references/
│   ├── stages/                           # 7 stage docs
│   ├── patterns/                         # 9 pattern docs (P1-P9)
│   ├── processes/                        # 8 process docs (uno per target) ⭐
│   ├── schemas/                          # 6 schema canonici
│   ├── conventions/                      # 3 conventions
│   └── external/
│       └── skill-creator.md              # mirror della guida ufficiale
├── assets/
│   └── templates/                        # template scheletro per ogni target
│       ├── doc/
│       ├── agent/
│       ├── team/
│       ├── skill/
│       ├── workflow/
│       ├── orchestration/
│       ├── wiki/
│       └── custom/
├── scripts/                              # 8 script con razionale puntuale
│   ├── transcript_cleaner.py             # S1
│   ├── atomizer.py                       # S2
│   ├── coverage_check.py                 # S3
│   ├── no_summary_lint.py                # S4
│   ├── length_check.py                   # S5
│   ├── schema_validator.py               # S6
│   ├── obsidian_packager.py              # S7
│   ├── package_target.py                 # S8
│   └── tests/                            # test per ogni script
└── evals/
    └── evals.json                        # 4+ test cases (uno per macro-target)
```

**Conteggio finale:**
- **12 agenti** (4 pipeline + 8 builder + 3 QA + 1 designer + il Conductor)
- **8 script** Python
- **34 file di reference**
- **8 set di template**
- **1 file SKILL.md** kernel

---

## 10. Roadmap di costruzione (aggiornata)

| Fase | Cosa produciamo | Stato |
|---|---|---|
| **0. PLAN v1** | piano iniziale | ✅ |
| **0b. PLAN v2** | piano aggiornato con agenti + processi | ⏳ **questo documento, in attesa di approvazione** |
| **1. ARCHITECTURE** | scheletro file completo (tutti i file vuoti con i loro indici e header) | ⏭ next |
| **2. AGENTI** | system prompt completi per i 12 agenti + Conductor | |
| **3. PROCESSES** | 8 file `references/processes/` con processi end-to-end | |
| **4. PATTERNS & STAGES** | contenuto vero di stages/ e patterns/ | |
| **5. SCRIPTS & SCHEMAS** | 8 script Python + 6 schemi + test | |
| **6. SKILL.md KERNEL** | scrittura finale del kernel | |
| **7. TEMPLATES** | template di scaffolding per ogni target | |
| **8. EVALS & TEST** | evals.json + run dei 4 test case + iterazione | |
| **9. PACKAGING** | `.skill` finale | |

---

## 11. Decisioni che vorrei confermare prima di passare a Fase 1

1. **Numero di agenti**: ti propongo 12 specialisti + Conductor. È un numero alto ma ognuno ha un ruolo isolato e necessario. Se ti sembrano troppi, posso accorpare (es. C1+C3 → unico QA agent, o A1+A2 → unico ingestion+analyst). Mi dici se questa granularità ti convince?

2. **Question designer (D1)**: è un'invenzione che non avevi chiesto esplicitamente. L'ho inserito perché la fase ASK è critica e merita un agente dedicato che adatta le domande al KG specifico, invece di una checklist statica. Ti sembra valga, o lo collassiamo dentro a ogni builder?

3. **Quality critic (C2) come agente separato vs critica interna del builder**: io lo terrei separato perché "occhi nuovi" funzionano meglio. Confermi?

4. **Processi per target — livello di profondità**: in §6 ho dato la versione condensata. La versione lunga (1 file di reference per processo, anche 200-400 righe ognuno con esempi reali) la scriviamo in Fase 3. Va bene questo livello di dettaglio per il piano?

Se confermi questi 4 punti (o mi correggi), parto subito con la **Fase 1 — Architecture**: creo tutta la struttura `content-forge/` con i ~60 file vuoti ma con i loro header, frontmatter, indici e contratti, pronti per essere riempiti in Fase 2+.
