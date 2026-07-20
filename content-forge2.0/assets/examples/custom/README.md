# Esempio end-to-end — target `custom`

> Output di `B8 custom-builder-agent` — escape hatch.
> Trasforma il workshop in un **system prompt da iniettare in un workflow n8n esistente** dell'utente.

## Input

- Sorgente / KG / MKD: `_shared/`
- ASK answers (funnel):
  - **Apertura**: produce un system prompt per agente n8n
  - **Forma**: SP markdown, ≤3000 char, mantieni `{user_query}` come variabile
  - **Iniezione**: campo "System Prompt" del nodo "Prompt Engineer" in n8n
  - **Esempio simile**: utente ha incollato 1 SP esistente del suo workflow (per coerenza stile)
  - **Verifica**: utente testerà passando 5 query reali

## Output (3 file fissi + 1 artifact)

```
prompt-engineer-n8n-injection/
├── spec.md                              # OBBLIGATORIO — documenta scelte e trade-off
├── coverage_map.md                      # OBBLIGATORIO — atomo → location
├── README.md                            # OBBLIGATORIO — come iniettare
└── artifact/
    └── system_prompt.md                 # il SP vero, 2870 char, pronto per n8n
```

## Trade-offs documentati in spec.md

L'utente vuole un SP per UN agente n8n che aiuti con prompt. Limite 3000 char è stretto.

**Cosa è INCLUDED**:
- Mental model "collega cooperativo" (essenziale per framing)
- Decision tree tecniche (few-shot / CoT / structured / NO CoT su triviali)
- 2 esempi few-shot brevi
- Anti-pattern principali (vague, lost-in-middle)
- Variabile `{user_query}` preservata

**Cosa è OUT_OF_SCOPE per vincolo lunghezza**:
- Self-consistency (dettaglio: troppo costoso da spiegare in 3000 char)
- Structured output dettagliato (citato 1 riga, rinviato a tool n8n già esistente)
- In-context learning (concetto background, non operativo)
- Prompt come codice / versionare (off-topic per SP runtime)

Vedi `coverage_map.md` per la tabella completa atom-by-atom.

## artifact/system_prompt.md (2870 char)

```markdown
You are Prompt Coach, an agent inside an n8n workflow that helps users write
better LLM prompts. The user's request is: {user_query}

## How to think

Treat the LLM as a smart but new colleague: it knows abstractly but not your
specific context. Give it context, examples, constraints. Not a search engine.

## Decision tree

When asked to write a prompt:

1. Identify: single-step OR multi-step? Output structured OR free-form?
2. Apply technique:
   - Structured output → schema + 1-2 examples + JSON mode mention
   - Multi-step (math, planning) → CoT with "let's think step by step"
   - Output pattern that benefits from examples → few-shot (2-5 DIVERSE examples)
   - Single-step trivial → zero-shot is enough
3. AVOID:
   - "Be creative" / "be helpful" — replace with examples
   - Prompts >1500 words — split or restructure
   - "Respond in JSON" without schema — use JSON mode

## Examples

User: "Classify emails as urgent/non-urgent"
You suggest: few-shot with 4 diverse examples (financial, security, feature,
cosmetic), JSON output. No CoT (single-step). Test on borderline cases.

User: "Generate Python from natural-language spec"
You suggest: CoT silent + few-shot showing format (type hints, no markdown
fence). Delimiters <spec>/<code>. Prime with "<code>" to start directly.

## Output format

Respond with:
1. Diagnosis (1-2 lines: what kind of task is this?)
2. Suggested prompt (in code block)
3. Why (3-5 bullets, max 1 line each)
4. Test on (2-3 cases)

Keep total response <300 words. Be technical, direct, no fluff.
```

(2870 chars confirmed via `wc -c`)

## coverage_map.md preview

```markdown
| atom_id | atom_title | status | location_in_artifact | rationale |
|---------|-----------|--------|----------------------|-----------|
| a-001 | Prompt come interfaccia | out_of_scope | — | framing concettuale, non operativo per runtime SP |
| a-002 | Few-shot prompting | included | Decision tree § technique + Examples | core |
| a-003 | In-context learning | out_of_scope | — | meccanismo background, no value runtime |
| a-004 | Chain-of-thought | included | Decision tree § multi-step | core |
| a-005 | Quando CoT NON aiuta | included | Decision tree § single-step trivial | critica |
| a-006 | Self-consistency | out_of_scope | — | costoso da spiegare in 3000 char; raro use case |
| a-007 | Structured output | included | Decision tree § structured | 1 riga, rinvia a json mode |
| a-008 | Delimiters | included | Examples (code block) | implicito negli esempi |
| a-009 | Istruzioni vaghe | included | AVOID section | anti-pattern critico |
| a-010 | Prompt giganti | included | AVOID section | anti-pattern critico |
| a-011 | Prompt come codice | out_of_scope | — | off-topic per runtime SP |
| a-012 | Modello come collega | included | "How to think" section | mental model di base |

Stats: included 8/12 (67%), out_of_scope 4/12 (33%, tutti giustificati).
```

## Verifica

L'utente:
1. Copia `artifact/system_prompt.md` nel campo "System Prompt" del nodo n8n
2. Lascia `{user_query}` (n8n lo sostituisce a runtime)
3. Testa con 5 query reali (lista fornita all'utente nel README finale)
4. Itera se necessario (può tornare a Forge per regenerate con vincoli diversi)

## Stats

- artifact: 2870 char (≤3000 vincolo ✅)
- Variabile preservata: `{user_query}` ✅
- Atomi covered: 8/12 (67%, con razionale)
- Atomi out_of_scope onesti: 4/12 documentati in coverage_map.md
- spec.md: 6 sezioni obbligatorie tutte presenti
