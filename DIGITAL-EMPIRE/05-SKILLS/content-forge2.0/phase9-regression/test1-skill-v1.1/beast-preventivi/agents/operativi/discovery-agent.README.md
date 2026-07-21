# Discovery Agent

Sub-agente di `beast-preventivi`. Conduce la Discovery Call con il prospect.

## Quando si attiva

Quando l'utente inizia una nuova qualifica cliente:
- `/preventivo nuovo-cliente` invocato senza preventivo già fatto
- O esplicitamente: `/preventivo discovery <nome>`

## Come si usa

Il freelancer apre una call con il prospect. Durante la call, paste delle risposte del prospect → l'agent suggerisce la prossima domanda + analizza fit-score in tempo reale.

A fine call, l'agent produce un **qualification report** che decide:
- ✅ Procedi col preventivo (passa a pricing-agent)
- ⏸ Aspetta info aggiuntiva
- ❌ Disqualify (non sprecare tempo)

## Tool usati

- `qualification_scorer` (calcolo deterministico fit-score)
- `red_flag_detector` (regex/pattern + LLM judgment sui 5 segnali non-fit)
