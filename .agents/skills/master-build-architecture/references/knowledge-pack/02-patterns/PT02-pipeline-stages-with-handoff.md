# PT02 — Pipeline Stages with Handoff

> **Shape canonica**: Il lavoro è organizzato in N stage numerati sequenziali. Ogni stage ha: input atteso (file/struttura precisa), output prodotto (file/struttura precisa), contratto con stage successivo. Handoff esplicito = JSON con stato/path/summary tra stage.

## Quando applicarlo

✅ **Applica se**:
- Processo end-to-end ha >3 fasi distinte
- Le fasi hanno dipendenze sequenziali chiare
- Vuoi poter "riprendere" da uno stage specifico (debugging, iterazione)

❌ **NON applicare se**:
- Processo monolitico inseparabile
- Tutte le fasi devono girare insieme atomicamente
- Stage <2 minuti ciascuno (overhead handoff sproporzionato)

## Perché funziona

### 1. Stage = unità di responsabilità
Ogni stage ha un owner (un agente o uno script). Quando qualcosa va male, sai dove guardare. Senza stage, il problema è "in qualche punto della pipeline".

### 2. Handoff esplicito = debug ovvio
JSON di handoff `{"status": "ok", "outputs": [...], "summary": "...", "next_should": "..."}` rende ovvio cosa è successo. Senza handoff, devi ricostruire stato dai file.

### 3. Stage indipendenti = parallelizzazione opportunistica
Se stage N+1 non dipende da output di stage N+2, puoi parallelizzare. content-forge fa A2 analyst-agent xN in parallelo perché chunks sono indipendenti.

## Esempio dal nostro percorso

`content-forge` ha 10 stage:

```
Stage 1 — Ingestion           A1 → cleaned.md + chunks.json + sources.json
Stage 2 — Analysis            A2 (xN) → atoms-*.json
Stage 3 — Knowledge Graph     A3 → kg.json + kg.md
Stage 4 — MKD                 A5 → master.md + glossary.md + faq.md
Stage 5 — Target Selection    A4 → recommendation.md (opzionale)
Stage 6 — Build               D1 + Bx → output/<artifact>/
Stage 7 — Depth Pass          Ox → arricchimento in-place
Stage 8 — QA                  C1 + C3 → qa-report.md
Stage 9 — Packaging           script → packaged/
Stage 10 — Self-Improvement   SI1+SI2+SI3 → failure-modes-log/
```

Ogni stage ha:
- **Input attesi** (esplicitati nel SP dell'agente principale)
- **Output canonici** (file specifici)
- **Contratto con stage successivo** (documentato in `references/stages/NN-*.md`)

## Handoff schema canonico

```python
handoff_envelope = {
    "status": "ok" | "needs_user_input" | "failed",
    "stage": int,
    "agent": str,
    "outputs_written": list[str],   # paths produced
    "summary_for_conductor": str,    # 2-3 frasi
    "next_suggestions": str,         # hint per Conductor
    "metrics": dict,                 # opzionali (token, duration, coverage, ecc.)
}
```

Conductor parsa, decide cosa fare next.

## ➕ Esempio in altri domini

**CI/CD pipelines** (Jenkins, GitHub Actions): stage = checkout → build → test → deploy. Handoff = artifact between stages.

**ETL** (Extract Transform Load): stage = extract → transform → load. Esattamente lo stesso pattern.

**Manufacturing assembly line** (Toyota): stage = ogni stazione, handoff = pezzo che passa a stazione successiva. Origin storico del pattern.

## Anti-pattern correlato

**Implicit handoff**: stage si passano dati attraverso side effect (modify global state) senza contratto esplicito. Sintomo: stage funziona standalone ma fail nel pipeline.

**Anti-pattern duale**: **Over-staging** — splittare in 50 micro-stage da 30 secondi ciascuno. Overhead handoff > beneficio. Soglia: ogni stage dovrebbe valere ≥1-2 min di lavoro reale.

## Trade-off

| Pro | Contro |
|---|---|
| Debug isolato per stage | Overhead handoff (file I/O, JSON parse) |
| Resume from any stage | Filesystem dependency |
| Documentation per stage | Più file da mantenere |
| Parallelism opportunistico | Coordination overhead |

## Decision tree

```
Processo ha >3 fasi distinte?
├─ NO → no pipeline, processo lineare
└─ SÌ → continua
   ├─ Le fasi hanno output salvabili su file?
   │  ├─ NO → stage in-memory (no resume)
   │  └─ SÌ → stage con artifact su disk
   │
   ├─ Vuoi poter riprendere da uno stage specifico?
   │  ├─ SÌ → stage persistenti, handoff via file
   │  └─ NO → handoff in-memory OK
   │
   └─ Implementa:
      1. Numera stage 01..NN
      2. Per ogni stage: references/stages/NN-name.md
      3. Per ogni stage: output canonical paths
      4. Handoff JSON schema fissato
      5. Conductor tiene state.json con current_stage
```

## Connessioni

- Combina con: PT01 (Conductor with Subagents)
- Combina con: PT03 (Builder then Optimizer)
- Validato da: schema di state.json, schema di handoff envelope
- Vedi anche: PR03 (from-scaffold-to-content process)

## Riferimenti

- CI/CD pipeline patterns (Humble & Farley, *Continuous Delivery*)
- ETL canonical pattern (Kimball)
- Toyota Production System (Womack & Jones)
