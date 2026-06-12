# Wrapper L3 -- Skill Creator (FORGE / Skill-Factory)

> **Codice sorgente: `SKILL & Agenti/SKILL/Skill - skill creator/`**
> Strumento core della FORGE per generare nuove skill.

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | skill-creator |
| Ecosistema | 07-FORGE |
| Reparto L2 | Skill-Factory |
| Stato | ACTIVE |
| Codice sorgente | `SKILL & Agenti/SKILL/Skill - skill creator/` |

## Cosa fa

Genera nuove skill Claude Code conformi allo standard MKD:
- Riceve una descrizione funzionale
- Produce il file SKILL.md con frontmatter YAML + corpo strutturato
- Output: skill deployabile in `.claude/skills/`

## Handoff Contract (ingresso)

```json
{
  "from": "Chief-Forge | qualsiasi ecosistema",
  "to": "skill-creator",
  "payload": {
    "nome_skill": "",
    "ecosistema_target": "",
    "funzione": "",
    "input_attesi": [],
    "output_attesi": [],
    "esempio_uso": ""
  },
  "acceptance_criteria": [
    "SKILL.md con frontmatter YAML valido",
    "Descrizione trigger chiara (quando attivare)",
    "Almeno 1 esempio concreto"
  ]
}
```

## System OMEGA

Per architettura di progetti piu' complessi: `System OMEGA - Creazione proggetti e skill per Claude/`.

---

## Come si inserisce nella pipeline FORGE

Questo wrapper copre il motore reale del reparto SKILL-WORKS (L2.1). Il flusso completo è
documentato in `WF-SKILL-NEW.md` — la skill-creator è la fase T-draft e T-eval-runner del
workflow. Non si usa mai "a mano" senza una spec approvata da `frg-chief` (gate G-SPEC).

### Posizione nella gerarchia

- **Reparto**: SKILL-WORKS (L2.1) → `Reparti/SKILL-WORKS/README.md`
- **Workflow**: WF-SKILL-NEW (creazione) · WF-SKILL-IMPROVE (miglioramento) · WF-SKILL-AUDIT (audit)
- **Agente operatore**: `frg-skill-smith` (Sonnet)

### Gate obbligatori prima dell'uso

1. **G-SPEC**: spec.md approvata (frg-chief) — cosa fa, cosa NON fa, acceptance criteria
2. **Controllo duplicati**: `skills-map.yaml` verificato (zero nuove skill se esiste già una analoga)
3. **Materia prima da INTELLIGENCE**: se Empire Studio ha già ingerito materiale → parti da quello

### Output consegnabile (definizione di "done")

- SKILL.md con frontmatter YAML valido + kernel ≤500 righe
- Eval report con pass_rate ≥85%
- skill-contradiction-analyzer verde (G-CONTRADICTION)
- Entry in `company/skills-map.yaml`
- Pagina wiki `second-brain-vault/wiki/tools/Tool_<nome-skill>.md`

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]] · [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]]
