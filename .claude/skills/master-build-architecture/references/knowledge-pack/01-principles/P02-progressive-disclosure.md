# P02 — Progressive Disclosure

> **Definizione canonica**: Carica conoscenza on-demand, mai tutto insieme. Il kernel (entry point) resta deliberatamente snello; il dettaglio sta in reference caricati solo quando rilevanti. Mira a non saturare il context window con materiale inutile alla decisione corrente.

## Perché funziona

### 1. Il context window è una risorsa scarsa
Anche con modelli da 200k+ token, ogni token in context costa: in compute, in latency, e — più importante — in **attenzione del modello**. Più cose in context, meno il modello si concentra su quelle critiche.

Il fenomeno [lost-in-the-middle](https://arxiv.org/abs/2307.03172) (Liu et al., 2023) documenta empiricamente che istruzioni nel centro di prompt lunghi vengono "ignorate". Quindi un kernel `SKILL.md` di 2000 righe diluisce le sue stesse istruzioni.

### 2. La conoscenza ha gerarchia naturale
Non tutto è ugualmente urgente. Per costruire una skill, il modello che la sta usando deve sapere:
- **Sempre**: invariant principali, routing, agenti disponibili
- **Spesso**: shape canoniche del target corrente
- **Raramente**: dettagli sui failure mode di un agente specifico
- **Quasi mai**: esempi storici di altre skill

Caricare tutto upfront è inefficiente e controproducente.

### 3. La struttura suggerisce il pensiero
Quando organizzi conoscenza in 3 livelli (kernel + reference + scripts), forzi una decisione: "questa cosa è kernel-level o reference-level?". La risposta a questa domanda costringe a pensare alla **criticità** della cosa. È un'euristica architetturale built-in.

## Come applicarlo (operativo)

### I 3 livelli Anthropic

Per una skill:

```
Level 1 — Kernel (SEMPRE in context)
  └─ SKILL.md (≤500 righe)
      - Routing table (chi fa cosa, vai a quale file)
      - Invariant cardinali
      - Inventario agenti/script
      - Decision tree principale

Level 2 — References (caricati ON-DEMAND)
  └─ references/
      - stages/ (uno per stage del pipeline)
      - patterns/ (framework cognitivi)
      - processes/ (dettaglio operativo per target)
      - schemas/ (forme canoniche)
      - conventions/ (naming, anti-pattern)

Level 3 — Tools (CHIAMATI quando applicabili)
  └─ scripts/ (Python, eseguibili)
      - operazioni deterministiche
      - validation
      - packaging
```

### Regola operativa: ogni file ha un trigger

Per ogni file in `references/`, esisti un trigger esplicito nel kernel:

```markdown
| Sei a | Vai a |
|---|---|
| Devi pianificare un nuovo target | references/processes/<target>.md |
| Stai validando uno schema | references/schemas/<entity>.schema.md |
| Vuoi capire un pattern P3 | references/patterns/P3-*.md |
```

Senza trigger nel kernel, il reference non viene mai aperto = è morto.

### Soglie pragmatiche

| Livello | Soglia raccomandata |
|---|---|
| SKILL.md | 200-500 righe (Anthropic), idealmente 200-300 |
| Reference file | 100-400 righe |
| Script Python | 50-300 righe (>300 splittare in moduli) |
| Schema JSON | piccolo (50-200 righe), human-readable companion .md sì |

Se sfondi le soglie, splitta in più file con link tra loro.

### La gerarchia dei `references/`

Sub-organizzazione interna ai references che funziona:

```
references/
├── stages/         (numerati 01-NN: ordine sequenziale del pipeline)
├── patterns/       (sigle P1-Pn: framework cognitivi)
├── processes/      (uno per target: doc.md, agent.md, ecc.)
├── schemas/        (dual file: .schema.md + .schema.json)
├── conventions/    (naming, anti-pattern, style)
└── external/       (mirror di docs esterne, es. skill-creator.md)
```

Non è obbligatoria, ma in 4-5 skill che ho visto è quasi universale.

## Esempi

### Esempio 1 — content-forge (nostro caso)

`SKILL.md` di content-forge: **236 righe**, contiene:
- Frontmatter (name, description pushy)
- Invariant cardinali (no riassunti, MKD sempre, ecc.)
- Loop principale 10-stage (overview)
- Tabella routing (8 voci)
- Inventario agenti (tabella con 20 voci)
- Workspace di run (tree)
- Quando NON attivarsi

Tutti i dettagli operativi sono in references/. Quando il Conductor decide di spawnare B4 (skill-builder), apre `agents/builders/skill-builder-agent.md` (220 righe) E `references/processes/skill.md` (350 righe), niente altro.

**Token efficiency**: il Conductor inizia con ~3000 token (SKILL.md) e carica ~5000 token solo quando entra in Stage 6 per il target skill. Senza progressive disclosure caricherebbe 50000+ token upfront.

### Esempio 2 — Anthropic skill-creator

`skill-creator/SKILL.md` (uploaded reference) è **412 righe**. Routing rigoroso:
- Quando creare nuova skill → sezione "Creating a skill"
- Quando ottimizzare description → `scripts/run_loop.py`
- Quando validare → `scripts/aggregate_benchmark.py`
- Subagenti spec → `agents/grader.md`, `agents/comparator.md`

Stesso pattern: kernel snello + dettagli on-demand.

### Esempio 3 — ➕ (esempio non-Anthropic, software architecture)

Stessa filosofia in **Domain-Driven Design** (Eric Evans): la *Ubiquitous Language* è il kernel sempre presente; *Bounded Contexts* sono "reference" che entrano in scope solo quando lavori in quel contesto specifico. Stesso meccanismo cognitivo: ridurre il carico mentale globale forzando struttura locale.

Altri esempi: **Sphinx documentation** con index + autodoc on-demand; **OpenAPI specs** con paths/ separati per endpoint.

## Anti-pattern correlato

**AP05 — Monolithic SKILL.md**: tutto nel kernel, references/ vuota. Sintomo: SKILL.md > 800 righe, descrive ogni agente in dettaglio, contiene anche gli script come code blocks. Risultato: lost-in-the-middle, kernel illeggibile, manutenzione impossibile.

**Anti-pattern duale**: **Over-fragmentation** — splittare ogni cosetta in un file separato. Risultato: 200 file in `references/`, ognuno di 20 righe, navigazione impossibile, indici stessi confusi. Soglia: se un reference è <50 righe E non ha vita propria, fondilo con un fratello.

## Decision tree: "questa info va nel kernel o in reference?"

```
L'info è necessaria a OGNI decisione del Conductor?
├─ SÌ → kernel (SKILL.md)
└─ NO → continua
   ├─ L'info è specifica a uno stage/target/agente?
   │  ├─ SÌ → reference dedicato a quello stage/target/agente
   │  └─ NO → continua
   ├─ L'info è una shape strutturata da validare?
   │  ├─ SÌ → references/schemas/ (dual md + json)
   │  └─ NO → continua
   ├─ L'info è un framework cognitivo riutilizzabile?
   │  ├─ SÌ → references/patterns/Pn-*.md
   │  └─ NO → continua
   ├─ L'info è una convenzione (naming, style)?
   │  ├─ SÌ → references/conventions/
   │  └─ NO → references/<altro>/ (decidi categoria)
```

## Quando NON applicare progressive disclosure

- **Skill molto piccole** (≤200 righe totali): l'overhead di reference + indici non vale. Tieni tutto in SKILL.md.
- **Skill single-purpose senza decision tree**: se la skill fa UNA cosa in modo lineare, references/ è overkill.
- **Documentazione tutorial** (non skill): un tutorial lineare beneficia di lettura continua, non on-demand.

## Riferimenti esterni

- **Anthropic Claude Skills docs** — Articolo "Three-level loading system" formalizza esplicitamente il pattern come raccomandazione.
- **Liu et al., 2023** — "Lost in the Middle: How Language Models Use Long Contexts" — base empirica.
- **Eric Evans**, *Domain-Driven Design* (2003) — analogia concettuale: Ubiquitous Language come kernel, Bounded Contexts come reference.
- **Andy Matuschak**, *Evergreen Notes* — principio "Notes should be concept-oriented" come applicazione di disclosure a livello atomico.

## Connessioni con altri principi

- Combina con: P07 (Three-Level Architecture) — progressive disclosure è il **meccanismo** del three-level
- Combina con: P05 (Markdown + Python Embedded) — la decisione "md vs py embedded" è una sub-decisione di "che livello?"
- Tensione con: P08 (Depth Over Breadth) — depth chiede file lunghi, disclosure chiede splitting. Risoluzione: depth applica al contenuto di OGNI file singolo; disclosure applica all'organizzazione tra file.
