---
name: content-forge2.0
description: 'Transforms raw, long, messy textual content (YouTube transcripts, workshop recordings, scattered articles, internal briefs, raw braindumps — single file OR an entire folder of files) into high-value operational artifacts: expanded markdown documents, AI agents, multi-agent teams, official Anthropic skills, executable workflows, orchestration layers, Obsidian second-brain wiki notes, or custom injections (system prompts to embed in n8n/CrewAI/LangGraph, RAG knowledge packs, parametrized templates). Never summarizes — always EXPANDS: every informational atom from the source becomes a richer, more structured, more complete version, with added examples, schemas, and cross-references. Always produces a Master Knowledge Document (MKD) as intermediate step — the "perfect document" — from which the requested target artifact is then built. Use this skill whenever the user has raw text and wants to operationalize/refactor/expand it, even if they describe the target informally ("I have
  these transcripts and want to make an agent", "ho questi appunti e vorrei trasformarli in qualcosa", "I want to turn this messy doc into something useful for my team"). Triggers on Italian phrases like "ho dei transcript/appunti/file da trasformare in...", "voglio estrarre tutto da questo materiale", "ho una cartella con...", and English equivalents. DO NOT use this skill for: summaries/TL;DRs (it does the opposite — expands), simple file operations (rename/translate/format), single-question Q&A, code generation requests, or when source is <500 words (overkill). Make sure to consider this skill whenever the user mentions raw content + transformation intent, even without explicit "forge" keyword.'
---

# `content-forge` — Skill kernel

> Comando di invocazione: `/forge <source-path> [--target=<target>] [--name=<slug>] [--recursive] [--ext=md,txt]`
> Invocazione naturale: descrivi cosa hai e cosa vuoi ottenere.
> Source-path può essere un singolo file O una cartella (vedi §Input supportati).

---

## ⚠️ Invariant cardinali (non negoziabili)

1. **No riassunti.** Mai. L'output rispetta o supera la lunghezza del sorgente. Espansione, non compressione.
2. **No invenzione di fatti.** Tutto ciò che non è nel sorgente ma è generato da Forge (esempi, schemi, controesempi) DEVE essere etichettato con `➕`.
3. **Coverage degli atomi.** Ogni atomo del Knowledge Graph DEVE comparire nell'output finale (soglia per target; 100% nel MKD).
4. **MKD sempre prodotto** (Stage 4). Indipendentemente dal target finale, viene generato il Master Knowledge Document come base canonica.
5. **Interactive scaffolding** obbligatoria per i target complessi (`agent`, `team`, `skill`, `workflow`, `orchestration`, `wiki`, `custom`). Mai output diretto senza PLAN → ASK → BUILD → CRITIQUE → ITERATE.
6. **Progressive disclosure.** Questo kernel rimane snello: il dettaglio sta in `references/`. Carica solo ciò che serve quando serve.

Catalogo completo anti-pattern: `references/conventions/anti-patterns.md`.

---

## 📥 Input supportati

| Tipo | Esempio | Comportamento |
|---|---|---|
| Singolo file | `/forge transcript.md` | Pipeline standard, 1 sorgente |
| Cartella flat | `/forge ./yt-transcripts/` | Tutti `*.md`/`*.txt`, multi-source |
| Cartella ricorsiva | `/forge ./materiale/ --recursive` | Anche sotto-cartelle |
| Lista esplicita | `/forge file1.md,file2.md,file3.md` | File elencati |
| Glob | `/forge "yt-*.md"` | Match con pattern |

### Limiti di dimensione

```
Comfort zone:
  - single file: 500 - 200k parole
  - folder:      1k - 500k parole totali, 1-30 file

Hard limit per run:
  - single file: 500k parole
  - folder:      1M parole totali, 100 file
```

Fuori dalla comfort zone → il Conductor avvisa l'utente prima di procedere.
Oltre l'hard limit → Conductor chiede di splittare in più run.

### Multi-source: cosa cambia

Quando passi una cartella o lista di file:
- Ogni file è trattato come **sorgente parallelo**
- Il KG fonde concetti cross-source con tracciabilità (chi ha detto cosa)
- Il MKD può citare le fonti ("come spiegato in [video 3]")
- I builder dei target finali ereditano la tracciabilità

---

---

## ⚡ Quick start (3 esempi reali)

### Esempio 1 — Singolo file → skill ufficiale
```
Utente: /forge transcripts_rag.md --target=skill --name=rag-coach
```
Cosa fa il Conductor:
1. A1 pulisce `transcripts_rag.md` (rimuove timestamp, filler)
2. A2 (xN parallel) estrae atomi dai chunk
3. A3 assembla KG
4. **A5 produce il MKD** (~12k parole, base canonica)
5. Salta A4 (target già scelto)
6. D1 genera domande adattive: "trigger phrases?", "subagenti?", "scripts?"
7. B4 (skill-builder) costruisce la skill
8. C1+C3 fanno QA
9. Packaging finale: `rag-coach/` + MKD bonus

### Esempio 2 — Cartella → wiki Obsidian
```
Utente: /forge ~/Materiale/yt-transcripts/ --target=wiki --recursive
```
Cosa fa: come sopra, ma A1 enumera tutti i `.md` ricorsivamente, traccia ogni file in `sources.json`, e B7 produce note atomiche Obsidian con tracciabilità della fonte ("come spiegato in [video 3]").

### Esempio 3 — Senza target (Forge propone)
```
Utente: ho questi appunti raw_thoughts.md sul mio second brain, vorrei farne qualcosa di più operativo ma non so esattamente cosa
```
Cosa fa: trigger naturale (senza `/forge` esplicito). Pipeline Stage 1-4. Poi **A4 propone 1-3 target** con razionale: "score alto per `wiki` (concetti atomici), `doc` (espansione narrativa), o `agent` (se hai ruolo specifico)". L'utente sceglie.

### Esempio 4 — Custom injection
```
Utente: ho customer_success_playbook.md (~15k parole), voglio iniettarlo come system prompt nel mio agente n8n. Max 3000 char, mantieni {customer_tier} come variabile.
```
Cosa fa: target=custom, B8 entra in modalità funnel ASK (forma, destinazione, vincoli), produce `artifact/system_prompt.md` rispettando i vincoli + `coverage_map.md` che dichiara cosa è incluso e cosa out-of-scope per limiti di lunghezza.


## 🗺 Routing: chi fa cosa, dove

| Sei a | Vai a |
|---|---|
| Capire il pipeline complessivo | `references/stages/01..09-*.md` |
| Sapere quale pattern cognitivo applicare | `references/patterns/P1..P9-*.md` |
| Costruire un target specifico | `references/processes/<target>.md` |
| Validare un output strutturato | `references/schemas/<entity>.schema.{md,json}` |
| Spawnare un agente specialista | `agents/<famiglia>/<nome>-agent.md` |
| Eseguire una operazione deterministica | `scripts/<nome>.py` |
| Scaffolding di un output | `assets/templates/<target>/` |

---

## 🔄 Il loop principale (10 stage)

```
INVOCAZIONE /forge <source> [opzioni]
    │
    ▼
[Stage 1] Ingestion             → A1 ingestion-agent
                                  (single-file O folder multi-source)
                                  Output: cleaned.md + chunks.json + sources.json
[Stage 2] Deep Analysis         → A2 analyst-agent (xN parallel)
                                  Output: atoms-*.json
[Stage 3] Knowledge Graph       → A3 knowledge-graph-agent
                                  Output: kg.json + kg.md + gaps.md
[Stage 4] 🌟 MASTER KNOWLEDGE   → A5 mkd-builder-agent  (SEMPRE)
          DOCUMENT (MKD)          Output: master.md + glossary.md + faq.md + schemas.md
[Stage 5] Target Selection      → A4 target-advisor-agent (se target non specificato)
                                  Output: recommendation.md
[Stage 6] Interactive Build     → D1 question-designer + Bx target-builder
                                  PLAN → ASK → BUILD → SELF-CRITIQUE → ITERATE
                                  Output: stage-06/output/<artifact-slug>/ (DRAFT)
[Stage 7] 🆕 DEPTH PASS         → Team Ox (O1+O2 parallel, then O3, O5, O4)
                                  Espande skill nested, completa agenti,
                                  arricchisce reference, valida formule, humanizza
                                  Obbligatorio per skill/team/workflow/orchestration
                                  Output: stage-07/{o1..o5}-report.json + modifiche in-place
[Stage 8] External QA           → C1 coverage-verifier + C3 schema-validator (parallel)
                                  Soglie post-Stage 7 più stringenti
                                  Output: qa-report.md
[Stage 9] Packaging             → scripts/package_target.py
                                  Output: stage-09/packaged/
                                  (include SEMPRE il MKD come bonus)
[Stage 10] 🆕 SELF-IMPROVEMENT  → SI1 + SI2 + SI3 (silenzioso, condizionale)
           OBSERVE                Auto-logga failure mode, fa triage, genera
                                  phase plan. L'utente non vede mai questo stage.
                                  Vede solo se chiede "Forge, cosa hai trovato?".
```

Per il contratto di ogni stage: `references/stages/`.

---

## 🎯 Selezione del target finale

8 target finali. Se l'utente non ne specifica uno, spawna `A4 target-advisor-agent` in Stage 5 e proponi 1-3 candidati con razionale.

| Target | Builder | Processo |
|---|---|---|
| `doc` | `agents/builders/doc-builder-agent.md` | `references/processes/doc.md` |
| `agent` | `agents/builders/agent-builder-agent.md` | `references/processes/agent.md` |
| `team` | `agents/builders/team-builder-agent.md` | `references/processes/team.md` |
| `skill` | `agents/builders/skill-builder-agent.md` | `references/processes/skill.md` |
| `workflow` | `agents/builders/workflow-builder-agent.md` | `references/processes/workflow.md` |
| `orchestration` | `agents/builders/orchestration-builder-agent.md` | `references/processes/orchestration.md` |
| `wiki` | `agents/builders/wiki-builder-agent.md` | `references/processes/wiki.md` |
| `custom` | `agents/builders/custom-builder-agent.md` | `references/processes/custom.md` |

> Nota: dato che il MKD è prodotto in Stage 4 sempre, il target `doc` è essenzialmente un "MKD adapter" — più snello degli altri builder.

---

## 🤖 Inventario agenti (20 specialisti + Conductor)

| Famiglia | Agente | Quando | File |
|---|---|---|---|
| A — Pipeline | `ingestion-agent` (A1) | Stage 1 — sempre | `agents/pipeline/ingestion-agent.md` |
| A — Pipeline | `analyst-agent` (A2) | Stage 2 — sempre (parallelo) | `agents/pipeline/analyst-agent.md` |
| A — Pipeline | `knowledge-graph-agent` (A3) | Stage 3 — sempre | `agents/pipeline/knowledge-graph-agent.md` |
| A — Pipeline | **`mkd-builder-agent` (A5)** 🆕 | **Stage 4 — sempre** | `agents/pipeline/mkd-builder-agent.md` |
| A — Pipeline | `target-advisor-agent` (A4) | Stage 5 — solo se target ignoto | `agents/pipeline/target-advisor-agent.md` |
| B — Builders | `<target>-builder-agent` (B1-B8) | Stage 6 — uno per run | `agents/builders/*.md` |
| C — QA | `coverage-verifier-agent` (C1) | Stage 7 — sempre | `agents/qa/coverage-verifier-agent.md` |
| C — QA | `target-schema-validator-agent` (C3) | Stage 7 — sempre | `agents/qa/target-schema-validator-agent.md` |
| 🆕 O — Optimizers | `skill-depth-agent` (O1) | Stage 7 — espande skill nested | `agents/optimizers/skill-depth-agent.md` |
| 🆕 O — Optimizers | `agent-depth-agent` (O2) | Stage 7 — completa agenti (7 file canonici) | `agents/optimizers/agent-depth-agent.md` |
| 🆕 O — Optimizers | `reference-expander-agent` (O3) | Stage 7 — arricchisce reference scheletriche | `agents/optimizers/reference-expander-agent.md` |
| 🆕 O — Optimizers | `humanizer-agent` (O4) | Stage 7 — elimina LLM-speak (condizionale) | `agents/optimizers/humanizer-agent.md` |
| 🆕 O — Optimizers | `formula-validator-agent` (O5) | Stage 7 — valida formule del sorgente | `agents/optimizers/formula-validator-agent.md` |
| 🆕 SI — Self-Improvement | `failure-detector-agent` (SI1) | Stage 10 — logga FM auto (silenzioso) | `agents/self-improvement/failure-detector-agent.md` |
| 🆕 SI — Self-Improvement | `triage-agent` (SI2) | Stage 10 — triage FM auto | `agents/self-improvement/triage-agent.md` |
| 🆕 SI — Self-Improvement | `phase-planner-agent` (SI3) | Stage 10 — genera phase plan auto (silenzioso) | `agents/self-improvement/phase-planner-agent.md` |
| D — Meta | `question-designer-agent` (D1) | Stage 6 — sempre per target complessi | `agents/meta/question-designer-agent.md` |
| — | `conductor` | il caller stesso (te) | `agents/conductor.md` |

---

## 📂 Workspace di run

```
<workspace>/forge-run-<ISO-timestamp>/
├── inputs/          (link/copia del sorgente: file o cartella)
├── stage-01/        (cleaned.md, chunks.json, sources.json)
├── stage-02/        (atoms-*.json)
├── stage-03/        (kg.json, kg.md, gaps.md)
├── stage-04/        (🌟 master.md, glossary.md, faq.md, schemas.md, mkd-report.json)
├── stage-05/        (recommendation.md — solo se target ignoto)
├── stage-06/        (output/<artifact-slug>/, ask-set.json, user_answers.json)
├── stage-07/        (🆕 o1-o5 report depth pass)
├── stage-08/        (coverage-report, schema-report, qa-report — soglie post-Ox più stringenti)
├── stage-09/        (packaged/<artifact-slug>/ + master-knowledge-document/ bonus)
├── stage-10/        (eventuali report SI1/SI2/SI3 di questo run — silenziosi)
├── state.json       (stato Conductor)
└── trace.jsonl      (log di tutti gli spawn + handoff)
```

---

## 🚦 Quando questa skill NON deve attivarsi

Per evitare overtriggering, **NON attivare** se l'intent è uno dei seguenti.
Per ognuno, un esempio concreto e cosa proporre invece:

| Anti-intent | Esempio di prompt | Cosa fare invece |
|---|---|---|
| **Riassunto / TL;DR** | "puoi farmi un riassunto in 5 punti di questo articolo?" | Decline gentile: "Forge fa l'opposto (espande). Vuoi un'altra strategia di compressione?" |
| **Rename / file ops** | "rinomina tutti i file in ./transcripts/ aggiungendo prefisso 'old_'" | Usa `Bash` / `Read` direttamente, niente Forge |
| **Traduzione** | "traduci questo .md da italiano a inglese mantenendo struttura" | Translation diretta inline, niente Forge |
| **Reformat cosmetico** | "rifai la formattazione di questo file (heading consistenti, liste con `-`)" | Edit/format diretto, niente Forge |
| **Code generation** | "scrivi una funzione Python che raggruppa una lista di dict" | Coding diretto, niente Forge |
| **Single-question Q&A** | "che differenza c'è tra few-shot e CoT prompting?" | Risposta diretta, niente Forge |
| **Estrazione mirata** | "estrai solo le tabelle dati da questo PDF in CSV" | Tool di estrazione dedicato, niente Forge |
| **Indexing per RAG** | "ho una cartella di docs, fammi lo script per indicizzarli in chromadb" | RAG pipeline diretta, niente Forge |
| **Opinion / chat** | "ho letto questo articolo, cosa ne pensi?" | Conversazione libera, niente Forge |
| **Sorgente troppo piccolo** | input < 500 parole | Avvisa: "pipeline overkill. Vuoi modalità leggera o annullare?" |

> ⚠️ **Near-miss pericolosi**: queste richieste **sembrano** Forge ma non lo sono. La parola "transcript" o "trasformare" da sola non basta: serve INTENT di trasformazione + espansione + output operativo riusabile.

## 📖 Per il Conductor

Leggi il tuo system prompt completo in `agents/conductor.md` prima di procedere.
Lì trovi: come parlare all'utente, come gestire stato e fallimenti, come decidere quando spawnare cosa, e come applicare gli invarianti cardinali (incluso il nuovo Stage 4 MKD obbligatorio).
