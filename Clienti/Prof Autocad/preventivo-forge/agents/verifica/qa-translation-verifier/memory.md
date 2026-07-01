# Memory — qa-translation-verifier

## Conoscenza persistente
- I residui tedeschi ricorrenti sono il segnale più prezioso: ogni blocco → una voce nuova nel
  glossario di S3. Nel tempo il gate diventa "quasi sempre verde" perché il glossario cresce.
- Namespace memory (se Backbone attivo): `agency/preventivo/qa-translation`.

## Lezioni apprese
- 2026-07-01: gli umlaut traslitterati (ue/oe/ae) causavano residui → fix in S3, non nel gate.
- 2026-07-01: i nomi colore costruttore vanno esclusi a monte, non "perdonati" dal gate.
- Il rilevamento tedesco DEVE restare indipendente dalla tabella di traduzione, altrimenti un
  errore del traduttore verrebbe "assolto" dal gate.

## Principio
Un gate che si ammorbidisce per far passare il lavoro non è un gate. Qui si corregge la fonte (S3).
