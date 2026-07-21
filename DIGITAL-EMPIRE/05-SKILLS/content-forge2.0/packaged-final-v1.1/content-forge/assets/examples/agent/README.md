# Esempio end-to-end — target `agent`

> Esempio realistico di output prodotto da `B2 agent-builder-agent`.
> Dal workshop "Prompt Engineering Avanzato" → un agente operativo che aiuta gli sviluppatori a scrivere prompt migliori per task complessi.

## Input

- Sorgente: `_shared/source.md`
- KG: `_shared/kg.json`
- MKD: `_shared/master.md`
- ASK answers utente:
  - Nome agente: `prompt-coach`
  - Modello target: `claude-sonnet-4`
  - Tool disponibili: `read_file`, `web_search` (per cercare paper / best practices)
  - Utente finale: "developer mid-senior che deve scrivere prompt per task complessi"
  - Criteri di successo: "user dichiara prompt usabile al primo try ≥70% dei casi"
  - Tono: tecnico, diretto, no fluff

## Output

```
prompt-coach/
├── agent.md              # spec principale (role, goals, constraints, metriche)
├── system_prompt.md      # SP pronto per copy-paste
├── tools.md              # 2 tool con schema I/O
├── playbook.md           # 6 conversazioni (4 happy + 1 edge + 1 failure recovery)
├── failure_modes.md      # 7 failure mode con prevenzione/rilevamento/recupero
├── eval_cases.json       # 12 casi (40% happy, 30% edge, 20% failure, 10% constraint)
└── README.md             # questo file
```

## Cosa B2 ha fatto (in pratica)

1. Letto KG → identificato "agent shape": dominio = prompt engineering, ruolo = coach
2. Letto MKD → estratto la prosa per "How to think" (mental model "collega cooperativo") e "How to act" (procedura: capisci task → identifica complessità → applica tecniche → valida)
3. Letto FAQ MKD → trasformato in failure modes ("utente chiede di fare CoT su task triviale" → coach segnala)
4. Generato eval cases bilanciati
5. Self-critique sul SP → 2 issue minori (ambiguità) → patch → v1

## Stats

- Coverage atomi: 92% (8 atomi puramente "framing" non sono mappati 1:1 nell'agente)
- SP lunghezza: 1280 parole (sotto soglia 1500)
- Playbook: 6 conversazioni
- Eval cases: 12 (5 happy, 4 edge, 2 failure, 1 constraint)
