# Esempio end-to-end — target `skill`

> Output di `B4 skill-builder-agent` (meta: skill che produce una skill).
> Trasforma il workshop in una **skill ufficiale Anthropic** che assiste sviluppatori a scrivere prompt complessi.

## Input

- Sorgente / KG / MKD: `_shared/`
- ASK answers:
  - Nome skill: `prompt-engineer-helper`
  - Comando: `/pe-help`
  - Trigger phrases: "scrivimi un prompt", "perché il mio prompt non funziona", "voglio CoT/few-shot"
  - Subagenti: nessuno (skill semplice, no sub-pipeline)
  - Scripts: 1 (`measure_prompt_complexity.py` — conta token, identifica anti-pattern)
  - Templates: 3 (zero-shot, few-shot, CoT) come scaffold
  - Test cases: 5 prompt realistici
  - Ambiente: Claude Code

## Output (conforme a skill-creator)

```
prompt-engineer-helper/
├── SKILL.md                              # kernel ≤500 righe
├── references/
│   ├── stages/
│   │   └── 01-decide-techniques.md       # decision tree
│   ├── patterns/
│   │   ├── few-shot.md
│   │   ├── cot.md
│   │   ├── self-consistency.md
│   │   └── structured-output.md
│   └── conventions/
│       ├── anti-patterns.md
│       └── naming.md
├── assets/
│   └── templates/
│       ├── zero-shot.template.md
│       ├── few-shot.template.md
│       └── cot.template.md
├── scripts/
│   ├── measure_prompt_complexity.py
│   └── tests/test_measure.py
├── evals/
│   └── evals.json                        # 5 test cases iniziali (no assertions)
└── README.md
```

## SKILL.md preview

```yaml
---
name: prompt-engineer-helper
description: >-
  Helps developers write effective prompts for LLM applications: chooses the
  right technique (zero/few-shot, CoT, self-consistency, structured output),
  composes the prompt with proper delimiters, suggests test cases, flags
  anti-patterns. Use whenever the user wants to write a prompt for a complex
  task, asks "why doesn't my prompt work", or wants to apply specific techniques
  (CoT, few-shot, structured output). Make sure to consider this skill even if
  the user doesn't explicitly say "prompt engineering" — context like "I need
  the LLM to do X reliably" is enough to trigger.
---
# Prompt Engineer Helper
... (routing + invariant + decision tree)
```

## Conformità skill-creator

- ✅ Description pushy (5 marker)
- ✅ SKILL.md ≤500 righe (180 stimato)
- ✅ Progressive disclosure (5 reference files)
- ✅ 1 script con test
- ✅ 3 template
- ✅ 5 eval cases senza assertions (da aggiungere in fase test)

## Stats

- Coverage atomi KG: 90% (alcuni atomi puramente framing non sono nella skill, sono nel doc target invece)
- SKILL.md: 180 righe, description 380 char (within 1000-2000 range)
- Pushy markers: 5/6
- Subagenti: 0 (decisione: KG troppo cohesive per giustificarli)
- Script: 1 con 4 test pytest
