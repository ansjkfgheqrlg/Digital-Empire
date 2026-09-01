# Humanizer Agent

Sub-agente di `beast-preventivi`.

## Ruolo

Riscrive il copy del preventivo eliminando LLM-speak e adattandolo al tono del freelancer. Sostituisce 'leverage' con 'sfrutta', elimina 'In summary', spezza liste eccessive in prosa, mantiene voice italiana informale-pragmatica.

## Quando si attiva

Spawnato dall'orchestrator della skill durante la fase corrispondente del pipeline.

## File

- `humanizer-agent.md` — agent spec
- `humanizer-agent.system_prompt.md` — SP pronto per copy-paste
- `humanizer-agent.tools.md` — tool spec
- `humanizer-agent.playbook.md` — esempi conversazionali
- `humanizer-agent.failure_modes.md` — gestione errori
- `humanizer-agent.eval_cases.json` — test cases
