# PT03 — Builder then Optimizer

> **Shape canonica**: Separa **costruzione** da **rifinitura**. Il builder produce un DRAFT strutturalmente valido ma minimo. Poi un team di optimizer specializzati arricchisce, espande, valida prima della QA finale. **Mai chiedere a un singolo agente di fare entrambi**: scope troppo largo = qualità degradata.

## Quando applicarlo

✅ **Applica se**:
- L'output finale ha aspetti multipli da curare (struttura + content depth + style + validità formule)
- Il builder produrrebbe scaffold senza pass aggiuntivo
- Vuoi modularità per aggiungere optimizer in futuro

❌ **NON applicare se**:
- Output ha 1 dimensione di qualità chiara
- Pipeline veloce single-pass è sufficiente
- Nessuna lezione di reali bug "scaffold-as-output"

## Perché funziona

### 1. Single-responsibility per agente
Builder fa "struttura corretta". Optimizer fa "depth/style/validation". Ognuno con SP focused → quality boost rispetto a "agente che fa tutto".

### 2. Layering = iterazione mirata
Se output è strutturalmente OK ma magro → re-spawn solo optimizer rilevante. Se output è strutturalmente sbagliato → re-spawn builder. Bug isolato = fix isolato.

### 3. Optimizer team è estensibile
Aggiungere nuovo optimizer (es. "code-style-checker") = aggiungere 1 agente in `agents/optimizers/`. No modifica del builder esistente.

## Esempio dal nostro percorso

**Phase 9** di content-forge ha aggiunto questo pattern esplicitamente per fixare bug v1.0:

```
Stage 6 (Builder)
  Bx produce DRAFT
       ↓
Stage 7 (Depth Pass — Team Ox)
  O1 skill-depth        → espande sub-skill magre
  O2 agent-depth        → completa agenti 7/7 file canonici
  O3 reference-expander → arricchisce reference 50→300 righe
  O5 formula-validator  → verifica completezza formule
  O4 humanizer          → elimina LLM-speak
       ↓
Stage 8 (QA esterna)
  C1 + C3 valida output post-optimizer
```

**Prima di Phase 9**: builder produceva scaffold, QA passava (schema permissive), utente ottienava skill thin.
**Dopo Phase 9**: builder produce DRAFT, optimizer arricchisce, QA blocca se ancora thin, utente ottienava skill production-ready.

## Pattern di handoff Builder → Optimizer

Builder può lasciare **flag espliciti** per orchestrare optimizer:

```markdown
<!-- FORGE_OX_FLAG agent=O2 reason="expand playbook with 4 more edge cases" -->
<!-- FORGE_OX_FLAG agent=O3 reason="add anti-pattern section here" -->
<!-- FORGE_OX_FLAG agent=O5 reason="verify CPB framework all 3 components" -->
```

Optimizer scansionano per loro flag, danno priorità. Senza flag, fanno comunque pass standard.

## ➕ Esempio in altri domini

**Drafting → Editing in writing**: writer produce primo draft, editor rifina. Stessa filosofia. Hemingway: "Write drunk, edit sober" — separazione esplicita.

**Compiler frontend → optimizer → backend**: parser produce AST, optimizer passes (constant folding, dead code elimination, ecc.), code generator. Stesso layering.

**Photography**: scatti raw, post-processing in Lightroom. Builder = camera, Optimizer = Lightroom.

**Construction**: framing → finishing. Builder construct walls, optimizer ("finisher") fa drywall + paint + trim.

## Anti-pattern correlato

**Builder-as-finisher**: chiedere al builder di produrre output finale rifinito. Sintomo: SP del builder gigante, contiene istruzioni su style + structure + validation + tone. Quality degrada perché scope troppo largo.

**Anti-pattern duale**: **Optimizer-as-builder** — optimizer che fa structural changes invece di rifiniture. Sintomo: O3 reference-expander che decide quali file creare. Out-of-scope. Fix: enforce confini stretti per ogni optimizer.

## Trade-off

| Pro | Contro |
|---|---|
| Modularity quality | 2x cost (builder + optimizer pass) |
| Single-responsibility | Coordination complexity |
| Easy to add new optimizer | Latency aggiuntiva |
| Issue isolation (builder vs optimizer) | Più SP da mantenere |

## Decision tree

```
Il tuo output ha dimensioni multiple di qualità?
(struttura + depth + style + validità + ...)
├─ NO → single-pass builder OK
└─ SÌ → continua
   ├─ Hai osservato bug "scaffold passato come deliverable"?
   │  ├─ SÌ → builder+optimizer mandatory
   │  └─ NO → ancora utile per modularity futura
   │
   ├─ Quante dimensioni distinte?
   │  ├─ 2-3 → 2-3 optimizer
   │  ├─ 4-5 → team Ox (content-forge model)
   │  └─ >5 → forse over-engineered, group simili
   │
   └─ Implementa:
      1. Builder produces DRAFT (struttura corretta + content minimo reale)
      2. Optimizer team in agents/optimizers/
      3. Spawn order: parallel quando possibile (O1+O2), poi sequential per dependencies
      4. Optimizer flag pattern per builder→optimizer hints
      5. Stage 7 (post-build, pre-QA) come dedicato
```

## Connessioni

- Combina con: PT02 (Pipeline Stages) — optimizer come stage dedicato
- Combina con: PT11 (Validation with Auto-Fix) — optimizer come auto-fix pass
- Necessario per: P08 (Depth Over Breadth)
- Esempi reali: Phase 9 di content-forge

## Riferimenti

- LLVM compiler passes (multi-stage optimization)
- Editor as separate role from writer (publishing industry)
- Anthropic skill-creator pattern di review/iterate
