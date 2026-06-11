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
