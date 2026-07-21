# PT11 — Validation with Auto-Fix

> **Shape canonica**: Validation non blocca solamente; **tenta auto-fix** dove possibile. Schema validator fail → loop ITERATE che ri-spawnano agent appropriato con feedback specifico sui gap. Max N iterazioni automatiche (es. 3) prima di escalation all'utente. **Cattura bug + risolve bug + escalate solo per problemi davvero strutturali.**

## Quando applicarlo

✅ **Applica se**:
- Hai validator/schema check attivi
- I gap rilevati sono spesso auto-fixabili (es. file mancante, content troppo corto)
- Vuoi UX dove user vede successo invece di error log

❌ **NON applicare se**:
- Errori richiedono sempre judgment umano
- Risorse limitate (auto-fix costa token)
- Schema non ancora maturo (potresti auto-fixare cose sbagliate)

## Perché funziona

### 1. Loop chiuso = output usable invece di "FAIL log"
Senza auto-fix: validator dice "manca tools.md" → utente deve capire + fixare manualmente.
Con auto-fix: validator detecta → spawn O2 con focus "crea tools.md per agente X" → fix → re-validate → PASS.

Utente vede successo. Sa che dietro c'è iterazione, ma non deve gestirla.

### 2. Bounded iteration = no infinite loops
Hard cap (es. max 3 iterazioni) previene loop infiniti se fix non funziona. Dopo cap, escalation all'utente con context.

Senza cap: edge case "fix introduce nuovo bug che fa fail il validator differently" → loop infinito.

### 3. Auto-fix feedback è insegnamento per builder
Quando O2 viene spawnato per fixare gap che B4 ha lasciato, B4 vede pattern: "oh, ogni volta che genero skill mi manca tools.md → next time lo genero subito". Implicit learning via repetition.

## Esempio dal nostro percorso

content-forge Stage 7 → Stage 8 loop:

```
Stage 6 — Builder Bx produces DRAFT
       ↓
Stage 7 — Optimizer team Ox arricchisce in-place
       ↓
Stage 8 — QA validation (C1 + C3)
       │
       ├─ PASS → Stage 9 (packaging)
       │
       └─ FAIL → analyze qa-report
            │
            ├─ Gap categorizzato per agent ownership:
            │    "skill X manca references/" → re-spawn O1 con focus su X
            │    "agent Y manca playbook" → re-spawn O2 con focus su Y
            │    "DAG ha ciclo" → re-spawn B5 (builder, problema strutturale)
            │
            └─ Re-run Stage 7 (parziale) → re-validate Stage 8
                 │
                 ├─ PASS → procedi
                 ├─ FAIL ma iteration <3 → ITERATE
                 └─ FAIL e iteration ≥3 → ESCALATE user
```

### Esempio concreto Phase 9 Test #2

Test #2 v1.0 baseline aveva 31 Phase 9 issues. Senza auto-fix: utente avrebbe visto report di 31 errori, dovrebbe fixare a mano.

Con Phase 9 auto-fix:
- Spawn O1 → espande 6 sub-skill aggiungendo references
- Spawn O2 → completa 8 agenti con 7/7 file
- Re-validate
- 0 issues
- Packaging procede

Utente vede solo "v1.1 ready". Niente errori esposti.

## Decision logic per auto-fix vs escalation

```python
def decide_fix_strategy(qa_report, current_iteration):
    issues = qa_report["checks"]

    # Categorizza issue
    auto_fixable = []
    needs_user = []

    for issue in issues:
        if can_auto_fix(issue):
            auto_fixable.append(issue)
        else:
            needs_user.append(issue)

    if needs_user:
        return "escalate_user", needs_user

    if current_iteration >= MAX_ITERATIONS:
        return "escalate_user", auto_fixable  # auto-fix has failed multiple times

    return "auto_fix", auto_fixable


def can_auto_fix(issue):
    """Issue auto-fixable se:
    - Categoria 'structural' (file mancante → genera)
    - Categoria 'content' (content magro → espandi)
    - Categoria 'frontmatter' (campo mancante → aggiungi)

    NON auto-fixable se:
    - Categoria 'semantic' (significato sbagliato → human judgment)
    - Categoria 'conflict' (vincoli incompatibili → user decide)
    - Risorse esaurite (token budget)
    """
    AUTO_FIXABLE_CATEGORIES = {"structural", "content", "frontmatter"}
    return issue["category"] in AUTO_FIXABLE_CATEGORIES
```

## ➕ Esempio in altri domini

**Linters with auto-fix** (ESLint --fix, Prettier, black): trovano issue + applicano fix automatici. Solo errori non-auto-fixable mostrati all'utente.

**Git rebase --interactive con autosquash**: detecta fixup! commits, applica fix automatici. Conflict manuale solo se merge fail.

**CI/CD with retry logic**: test transient failure → auto-retry. Solo persistent failure escalata.

**Database migrations with rollback**: migration fail → auto-rollback. Solo errori manuali se rollback fail.

## Anti-pattern correlato

**Validator-as-rejector**: validator fail = stop. Utente deve fix manuale. Burden on user.

**Anti-pattern duale**: **Infinite auto-fix loop** — no max iteration, validator fail → auto-fix → introduce new issue → validator fail → ... Fix: hard cap MAX_ITERATIONS = 3.

**Edge anti-pattern**: **Auto-fix everything** — auto-fix anche issue che richiedono judgment. Fix introduce bug semantici. Fix: whitelist categorie auto-fixable (structural, content, frontmatter), blacklist categorie human (semantic, conflict).

## Trade-off

| Pro | Contro |
|---|---|
| UX boost (no error log esposto) | Token cost per re-run agenti |
| Riduzione burden user | Latency aggiuntiva |
| Implicit learning via repetition | Risk di fix sbagliato che maschera bug reale |
| Bounded retries safe | Implementation complexity |

## Decision tree

```
Hai validator/schema check attivi?
├─ NO → prima implementa validation, poi PT11
└─ SÌ → continua
   ├─ Gap sono spesso auto-fixabili (file mancante, content magro)?
   │  ├─ NO → validation only (no auto-fix)
   │  └─ SÌ → continua
   ├─ Hai budget per iteration cost?
   │  ├─ NO → validation only + manual fix
   │  └─ SÌ → procedi auto-fix
   │
   └─ Implementa:
      1. Categorize issues (auto-fixable vs human-judgment)
      2. Per ogni categoria auto-fixable, mappa a agente fix appropriato
      3. Loop ITERATE con MAX_ITERATIONS hard cap (3 default)
      4. Re-validate after fix
      5. Escalate to user se: human-judgment issue OR max iterations reached
      6. Tutto silent per user finché success/escalation
```

## Quando NON auto-fix

- Issue di categoria "semantic" (es. "output dice cosa contraria al sorgente") — judgment needed
- Issue persistente dopo 2+ iterazioni — segno che fix automatico non funziona, escalate
- Budget token esaurito — escalate
- Edge case unfamiliar (validator non sa come fixare) — escalate

## Connessioni

- Combina con: PT06 (Schema Tightening Loop) — tighten + auto-fix = pair
- Combina con: PT07 (Silent Observer) — auto-fix è silent se PASS, observer se FAIL
- Implementa: P09 (Failure Modes) — "recupero" colonna = auto-fix attivo
- Esempio reale: content-forge Stage 7+8 loop

## Riferimenti

- ESLint --fix, Prettier, black autofix
- Database migration rollback patterns
- CI/CD retry logic (GitHub Actions, GitLab CI)
- Code formatters with auto-correction
- Anthropic skill-creator iterate pattern
