# Process: `skill` — Anthropic Official Skill (META)

> Builder: `skill-builder-agent` (B4)
> Stage: 5
> Tempo medio stimato: 3-5 turni utente + 3-4 iterazioni
> **Reference primaria**: `references/external/skill-creator.md` (la guida ufficiale)

---

## 1. Identità

Il target `skill` trasforma il KG in **una skill ufficiale Anthropic**, conforme al pattern di `skill-creator`. È **meta**: usiamo `content-forge` (a sua volta una skill) per produrne un'altra.

Output: cartella di skill completa, packaging-ready, con `SKILL.md`, frontmatter, references, scripts (se servono), agents (se servono), assets, evals. Pronta per `package_skill.py` → `.skill`.

> Differenza chiave vs `agent`: una skill è **invocabile dichiarativamente** ("ho bisogno di X" → Claude la attiva), un agente è **istanziato esplicitamente**. La skill incapsula expertise riusabile a basso costo cognitivo.

## 2. Forma canonica dell'output

Identica a quella che la guida `skill-creator.md` definisce:

```
output/
└── <skill-slug>/
    ├── SKILL.md                  # kernel con frontmatter (name + description)
    ├── agents/                   # se servono subagenti
    ├── references/
    │   ├── stages/               # se la skill è pipeline-based
    │   ├── patterns/             # se ha framework cognitivi
    │   ├── processes/            # se ha più sotto-processi
    │   ├── schemas/              # se valida output strutturato
    │   └── conventions/          # naming, style, anti-pattern
    ├── scripts/                  # se servono operazioni deterministiche
    ├── assets/
    │   ├── templates/            # forme canoniche di output
    │   └── examples/             # esempi end-to-end
    ├── evals/
    │   └── evals.json            # 4-6 test prompts (no assertions yet)
    └── README.md
```

### SKILL.md (frontmatter canonico)

```markdown
---
name: <skill-slug>
description: <descrizione "pushy" che include cosa fa AND quando usarla, con anti-undertriggering>
---

# <Skill Name>

<corpo della skill, ≤500 righe ideali, con routing e pointer ai references>
```

## 3. Input atteso

```
inputs/
├── kg.json
├── atoms/
├── source_meta.json
└── user_answers.json
```

## 4. PLAN (cosa fa il builder)

1. **Carica la reference**: legge `references/external/skill-creator.md` per assicurarsi di seguire la guida ufficiale.
2. Analizza il KG per identificare la **"skill shape"**:
   - quando dovrebbe triggerare? (clusters che indicano contesti d'uso)
   - cosa produce? (cluster procedurali con output canonico)
   - serve pipeline o single-shot?
   - serve stato o stateless?
3. Decide se servono **subagenti** (sì se ci sono fasi logiche distinte ognuna con scope isolabile).
4. Decide se servono **script** (sì se ci sono operazioni deterministiche / verifiche / packaging).
5. Decide la **gerarchia delle reference** (progressive disclosure, mai >500 righe in SKILL.md).
6. Propone un nome e una description-bozza.
7. Restituisce PLAN al Conductor.

## 5. ASK (domande generate da D1)

1. **Nome**: "Propongo `<slug>` come nome. Confermi?"
2. **Trigger phrases**: "La skill dovrebbe attivarsi quando l'utente dice cose come <esempi>. Mancano contesti? Ce ne sono di rischiosi (potrebbe triggerare quando non serve)?"
3. **Description style**: "Anthropic raccomanda description 'pushy' per combattere l'undertriggering. Ti propongo: '<bozza>'. Va bene?"
4. **Subagenti**: "Dal KG sembra che serva <N> subagenti per: <lista ruoli>. Confermi? Vuoi accorpare/splittare?"
5. **Scripts**: "Identifico questi candidati a script Python: <lista>. Per ciascuno: ti convince il razionale (deterministico, veloce, riusabile)?"
6. **Templates**: "L'output canonico è <descrizione>. Vuoi che includa template scaffolding o partiamo da zero ogni volta?"
7. **Test cases iniziali**: "Propongo questi 4 prompt di test: <lista>. Sono realistici? Vuoi aggiungerne altri?"
8. **Ambiente target**: "Claude Code, Claude.ai, Cowork, o tutti?"
9. **Compatibility**: "Servono MCP, tool specifici, dipendenze esterne?"

## 6. BUILD (ordine di scrittura — critico)

L'ordine segue la guida ufficiale `skill-creator`:

1. **`references/external/<original-skill-creator-link>`**: già presente, è la nostra reference.
2. **`SKILL.md` kernel v0**: frontmatter + scheletro con pointer ai (futuri) references. Tieni ≤500 righe già dalla v0.
3. **`references/conventions/`**: anti-pattern, naming, style. Vanno scritti presto perché altri file ci si appoggiano.
4. **`references/stages/` o `references/processes/`** (a seconda della shape): contenuto dettagliato.
5. **`references/patterns/`** se la skill ha framework cognitivi.
6. **`references/schemas/`** se valida output strutturato.
7. **`agents/<nome>.md`** per ogni subagente identificato. Ognuno: identità, ruolo, input, output, system prompt, esempi.
8. **`scripts/<nome>.py`** per ogni script. Ognuno: docstring, CLI args, test in `scripts/tests/test_<nome>.py`.
9. **`assets/templates/`**: template scheletro per ogni forma di output canonica.
10. **`assets/examples/`**: 1-2 esempi end-to-end completi.
11. **`evals/evals.json`**: 4-6 test prompts in formato skill-creator (id, prompt, expected_output, files). **Senza assertions per ora** (le aggiunge la fase di test in roadmap).
12. **Self-critique** (vedi §7).
13. **SKILL.md v1**: scrittura definitiva dopo che tutti i references sono in piedi (così il kernel può fare pointer corretti).
14. **README.md**: indice, come è stato generato, come installarlo, come testarlo.

## 7. Self-critique (interna)

Il builder verifica conformità alla guida skill-creator:

- **Description pushy**: contiene sia "cosa fa" sia "quando usarla"? È un po' aggressiva contro l'undertriggering?
- **SKILL.md ≤500 righe**: se vicino al limite, c'è hierarchy sufficiente?
- **Progressive disclosure**: nessun reference è caricato sempre? Ogni reference ha pointer chiari?
- **Esempi**: ogni pattern non-banale ha un esempio?
- **"Explain the why"**: ci sono ALWAYS/NEVER senza spiegazione? Rosso.
- **Subagenti specs complete**: ogni agente ha SP, input, output, esempi?
- **Scripts robusti**: ogni script ha docstring, CLI args, test?
- **Templates utili**: ogni template è effettivamente referenziato da qualche istruzione?
- **Evals realistici**: i 4 test prompts sembrano cose che un vero utente direbbe?
- **No conflitti di trigger**: la description non si sovrappone a skill comuni (verifica con 5 prompt di near-miss)?

Output: `self-critique.md`. Loop su rilievi bloccanti.

## 8. Critique esterna (C1 + C3)

- **C1 `coverage-verifier`**: ogni atomo del KG è riflesso da qualche parte (kernel, reference, agente, esempio). Soglia 90%.
- **C3 `schema-validator`**: validazione contro `schemas/skill.schema.md`:
  - frontmatter ha `name` e `description`
  - `SKILL.md` ≤ N righe (configurabile, default 500)
  - tutti i pointer interni risolvono
  - agenti dichiarati esistono fisicamente
  - scripts dichiarati eseguono (smoke test via subprocess)
  - evals.json valida

## 9. Iterate

Tipici fix:
- riscrivere description per migliorare triggering (la guida ha sezione apposita su questo)
- snellire SKILL.md spostando in references
- aggiungere esempi mancanti
- riformulare ALWAYS/NEVER in "perché"

Quando il builder finisce, propone all'utente il **description optimization loop** (in roadmap, non obbligatorio).

## 10. Failure modes del processo

| Failure | Sintomo | Mitigazione |
|---|---|---|
| SKILL.md monolitico | >500 righe, tutto inline | Splittare in references e mettere solo routing nel kernel |
| Description debole | Skill non triggera nei test | Riscrivere in stile pushy con esempi specifici di contesto |
| Subagenti inutili | Agente che fa solo 1 chiamata | Collassare in instruction inline |
| Scripts non testati | Smoke test fail | Aggiungere `tests/` per ogni script |
| Templates morti | Template mai referenziato | Eliminare o aggiungere pointer |
| Evals banali | Tutti passerebbero anche senza skill | Riscrivere con realistici prompt utente |

## 11. Esempio realistico

Input: 4 articoli + 1 video tutorial su "system design interview prep" → KG con 96 atomi.
ASK: nome `sd-interview-coach`, trigger su "preparami per system design / mock interview / progetta sistema scalabile per X", subagenti = {`problem-clarifier`, `architecture-drafter`, `tradeoff-analyzer`, `mock-interviewer`}, scripts = {`diagram_renderer.py`, `requirements_extractor.py`}, templates = canonical SD interview answer template.

Output:
- `SKILL.md` 380 righe con routing
- 4 subagenti completi
- 12 reference files in stages/patterns/conventions
- 2 scripts con test
- 3 template (clarification questions, architecture canvas, tradeoff matrix)
- 5 eval cases
- `README.md`

Coverage: 94%. Schema: OK. Smoke test scripts: OK.

## 12. Handoff al Conductor

- path `output/<skill-slug>/`
- `build-report.json`
- `next-suggestions.md` (es. "vuoi che esegua il description optimization loop di skill-creator?", "vuoi che pacchetti subito in .skill?")

---

## 13. 📎 Appendice — Shape esatti (embedded)

### `evals.json` — shape canonica (skill-creator compliant)

```python
# evals.json shape — usare ESATTAMENTE questi campi
evals_schema = {
    "skill_name": str,              # slug della skill
    "evals": [                      # 4-6 entries iniziali
        {
            "id": int,              # progressivo 1..N
            "prompt": str,          # prompt utente realistico, sostanziale (vedi guida)
            "expected_output": str, # descrizione dell'output atteso
            "files": list[str],     # path di file in input, [] se nessuno
            # "assertions": list[dict]  # aggiunte DOPO, in fase di test
        }
    ]
}
```

### `SKILL.md` frontmatter — shape canonica

```python
frontmatter = {
    "name": str,        # slug, kebab-case
    "description": str  # "pushy", include cosa-fa AND quando-usarla, con anti-undertriggering
}
# Il corpo segue il frontmatter, ≤500 righe ideali.
```

### Regex check description "pushy"

```python
import re
PUSHY_MARKERS = [
    r"\bmake sure\b",
    r"\bwhenever\b",
    r"\beven if\b",
    r"\balways\b",
    r"\buse this\b"
]
def is_pushy(description: str) -> bool:
    """Descrizione 'pushy' = anti-undertriggering. Ha ≥1 marker forte."""
    return any(re.search(p, description, re.I) for p in PUSHY_MARKERS)
```
