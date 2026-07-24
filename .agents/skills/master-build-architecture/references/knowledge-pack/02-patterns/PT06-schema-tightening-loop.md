# PT06 — Schema Tightening Loop

> **Shape canonica**: Comincia con schema permissivo (per non bloccare early development). Man mano che il sistema viene usato e identifichi categorie di bug, **stringi lo schema** per prevenirli. Schema evolve attraverso versioni (v0.1 permissive → v0.2 properties populated → v0.3 minimum constraints). Lo schema è guardian crescentemente severo.

## Quando applicarlo

✅ **Applica se**:
- Hai schema per validare output
- Stai iterando attivamente sulla skill
- Vedi bug ricorrenti che lo schema NON cattura

❌ **NON applicare se**:
- Skill stabile mature (schema già giusto)
- Schema non esiste affatto (prima crea, poi tighten)
- Prototipo throwaway

## Perché funziona

### 1. Schema permissivo all'inizio = velocity early-stage
Se schema v0.1 ha `additionalProperties: true` e zero `required`, qualsiasi cosa passa. Builder può sperimentare. Fine.

Se invece schema v0.1 è già stringentissimo, ogni piccolo cambio del builder richiede update schema. Velocity uccisa.

### 2. Tightening based on evidence = surgical
Quando hai osservato 3 bug "playbook tutti uguali", aggiungi `playbook_min_conversations: 5` con `categories_required: [happy, edge, failure_recovery]`. Schema diventa più severo solo dove serve.

Senza tightening evidence-based: schema sia troppo permissive (passa bug) sia troppo strict (blocca casi legittimi).

### 3. Versioning schema = upgrade path chiaro
v0.3 può rifiutare cose che v0.2 accettava. Output v0.2 può essere migrato a v0.3 con script di migration. Versioning chiaro evita "scrivo da capo".

## Esempio dal nostro percorso

`agent.schema.json` versioning in content-forge:

**v0.1.0-draft (Phase 1 — scaffold)**:
```json
{"type": "object", "properties": {}, "additionalProperties": true}
```
Praticamente vuoto. Tutto passa.

**v0.2.0-draft (Phase 2 — properties populated)**:
```json
{
  "required_files": ["agent.md", "system_prompt.md", "tools.md",
                     "playbook.md", "failure_modes.md", "eval_cases.json", "README.md"]
}
```
Almeno controlla che file esistano. Ma non checka contenuto.

**v0.3.0 (Phase 9 — Phase 9 tightening)**:
```json
{
  "required_files": [...],
  "agent_md_min_words": 400,
  "system_prompt_min_words": 500,
  "system_prompt_max_words": 1500,
  "playbook_min_conversations": 5,
  "failure_modes_min_count": 7,
  "eval_cases_min": 8,
  "eval_cases_max": 15,
  "additionalProperties": false
}
```
Adesso blocca scaffold con file vuoti, playbook con 1 conversation, ecc.

**Trigger del tightening**: bug osservati nei test reali (Phase 7 e Test #1/#2 utente).

## Workflow di tightening

```
1. OSSERVA bug ricorrenti che schema NON cattura
   (es. "agente generato con 3 file canonici invece di 7")
       ↓
2. IDENTIFICA constraint mancante
   (es. "manca enforcement di required_files completi")
       ↓
3. AGGIORNA schema (nuova version v0.X)
   - Aggiungi constraint
   - Bump version in $id
   - Update schema_version field
       ↓
4. AGGIORNA validator (scripts/schema_validator.py)
   - Per ogni nuovo constraint, funzione di check
   - Test pytest per ogni check
       ↓
5. RUN su artifact esistenti per migration
   - Quali ora fail con nuovo schema?
   - Patcha quelli legittimi, deprecate quelli scaffold-y
       ↓
6. UPDATE builder per produrre output che passa nuovo schema
   - SP del builder ora aware del constraint
   - Self-critique del builder include check del constraint
       ↓
7. RUN end-to-end test reale
   - Schema nuova versione cattura nuovi casi reali?
   - Test passa?
       ↓
8. DOC change in PLAN-vN+1.md
   - Cosa è cambiato in schema
   - Perché (link a bug osservato)
   - Migration notes
```

## ➕ Esempio in altri domini

**Database schema migration** (Rails migrations, Flask-Migrate): schema evolve via versioning. Up + down migrations. Stesso pattern.

**TypeScript strict mode progression**: comincia non-strict, abilita `strictNullChecks` → `strict` → `noImplicitAny`. Tightening graduale.

**Linting rules**: ESLint config evolve. Aggiungi rule, fix issue trovati, abilita più rule. Tightening loop.

**API versioning** (REST/GraphQL): v1 → v2 con breaking changes documentate, deprecation period.

## Anti-pattern correlato

**Schema-as-suggestion**: schema esiste ma validator non blocca. Sintomo: "skipped on failure". Risultato: schema decorativo, niente enforcement.

**Anti-pattern duale**: **Big-bang tightening** — passare da v0.1 permissive a v0.5 super-strict in 1 step. Tutto fail, panic refactor di settimane. Fix: incrementale (v0.1 → v0.2 → v0.3, una categoria di constraint per volta).

## Trade-off

| Pro | Contro |
|---|---|
| Cattura bug ricorrenti | Schema da mantenere |
| Forza quality builder | Migration cost tra versioni |
| Evidence-based evolution | Frequenti updates |
| Version chiaro | Schema validator complessità cresce |

## Decision tree

```
Hai schema attivo per i tuoi target output?
├─ NO → prima crea schema v0.1 permissivo
└─ SÌ → continua
   ├─ Hai osservato bug che lo schema non cattura?
   │  ├─ NO → schema sufficient, no tighten
   │  └─ SÌ → continua
   ├─ Il bug è ripetibile / categorico?
   │  ├─ NO (one-off) → fix manuale, no schema change
   │  └─ SÌ (pattern) → aggiungi constraint
   │
   └─ Tighten:
      1. Bump version (es. v0.2 → v0.3)
      2. Aggiungi constraint con razionale documentato
      3. Update validator + test pytest
      4. Run su artifact esistenti, fix o deprecate
      5. Update builder per essere aware
      6. Doc in PLAN-vN+1
```

## Quando NON tightening

- Bug è bug del builder, non gap dello schema. Fix builder direttamente.
- Constraint sarebbe troppo specifico (blocca casi legittimi). Fix builder con instruction nel SP invece.
- Sei in middle di big release. Tighten dopo.

## Connessioni

- Necessario per: P06 (Shapes & Canonical Forms) — shape evolve via tightening
- Necessario per: P08 (Depth Over Breadth) — content minimums enforced
- Combina con: PT11 (Validation with Auto-Fix) — tightening + auto-fix = pair
- Esempio reale: Phase 9 schema v0.3 di content-forge

## Riferimenti

- Database migration patterns (Sadalage & Fowler, *Refactoring Databases*)
- TypeScript strict mode flags evolution
- ESLint rule progression strategies
- JSON Schema versioning best practices
