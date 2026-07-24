# Copy Reviewer

Sub-agente di `beast-preventivi`.

## Ruolo

Verifica che il preventivo finale rispetti i principi del manuale APSOC: parola 'investimento' (no 'costo'), 5 step canonici presenti, niente 'lista della spesa', data di scadenza presente, struttura multi-pagina (no fattura singola).

## Quando si attiva

Spawnato dall'orchestrator della skill durante la fase corrispondente del pipeline.

## File

- `copy-reviewer.md` — agent spec
- `copy-reviewer.system_prompt.md` — SP pronto per copy-paste
- `copy-reviewer.tools.md` — tool spec
- `copy-reviewer.playbook.md` — esempi conversazionali
- `copy-reviewer.failure_modes.md` — gestione errori
- `copy-reviewer.eval_cases.json` — test cases
