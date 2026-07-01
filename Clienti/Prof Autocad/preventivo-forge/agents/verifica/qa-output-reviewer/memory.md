# Memory — qa-output-reviewer

## Conoscenza persistente
- È l'ultimo cancello: la sua soglia di qualità definisce cosa il cliente vede davvero.
- Namespace memory (se Backbone attivo): `agency/preventivo/qa-output`.

## Lezioni apprese
- 2026-07-01: contare le foto *dentro* il PDF è fragile → si verifica in modo indiretto (foto su
  disco + `data:image/` nell'HTML re-renderizzato). Robusto e sufficiente.
- 2026-07-01: la verifica visiva del PDF resta preziosa (il tool Read apre i PDF): usarla a campione
  su ogni nuovo dealer/template.
- La soglia 20 KB è prudenziale: un preventivo reale con foto è sempre ben oltre.

## Standard di consegna Prof Autocad
Preventivo consegnabile solo con: 9 sezioni presenti, prezzo nel titolo, gallery completa, 0
placeholder. Verificato end-to-end sul primo run reale simulato (BMW 320d).
