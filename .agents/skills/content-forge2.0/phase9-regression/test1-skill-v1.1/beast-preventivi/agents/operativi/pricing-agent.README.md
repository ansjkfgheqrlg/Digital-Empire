# Pricing Agent

Sub-agente di `beast-preventivi`.

## Ruolo

Calcola il pricing del preventivo applicando la regola delle 3 opzioni (A/B/C), il cushion del 10%, i numeri tondi per B2B, ancorando il mid-tier al budget dichiarato in discovery. Genera anche modalità di pagamento (acconto/saldo/rate).

## Quando si attiva

Spawnato dall'orchestrator della skill durante la fase corrispondente del pipeline.

## File

- `pricing-agent.md` — agent spec
- `pricing-agent.system_prompt.md` — SP pronto per copy-paste
- `pricing-agent.tools.md` — tool spec
- `pricing-agent.playbook.md` — esempi conversazionali
- `pricing-agent.failure_modes.md` — gestione errori
- `pricing-agent.eval_cases.json` — test cases
