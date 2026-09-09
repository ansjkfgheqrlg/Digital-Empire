# MT-4GNU — S2c - i sei test rossi dei controlli, scritti PRIMA dei controlli

- **Padre:** TASK-LANCI-BUILD-W3
- **Data:** 2026-09-09
- **Ordine:** 8

## Cosa fa

S2c. I sei test rossi dei controlli di questa meta', **scritti prima dei controlli**:
`GATE-PUB-1`, `GATE-STR-1`, `GATE-PRD-1`, `GATE-INT-1`, `GATE-PRV-1`, `GATE-OFF-1`.

INV-04: un controllo senza un caso che lo faccia fallire e' decorativo per costruzione. Per
questo questa micro-task viene **prima** di [[MT-GHZ6]] e non insieme: chi prende quella
trova gia' i rossi da far passare.

## Gate di chiusura

`python -m pytest tests/rossi/ -v` gira e **fallisce** come deve, sei casi su sei.

## Output

