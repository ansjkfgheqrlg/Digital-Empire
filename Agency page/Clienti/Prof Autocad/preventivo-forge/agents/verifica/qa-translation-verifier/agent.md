# Agente: qa-translation-verifier

- **ID:** qa-translation-verifier
- **Team:** Verifica (Half B / Gael)
- **Gate:** B — Traduzione
- **Motore:** `implementation/qa_gate.py :: gate_b(ctx, dealer)`
- **Regola:** `rules/R6-qa-gate.md` · a monte: `rules/R3-translation-copy.md`
- **Blocca:** sì

## Missione
Garantire che la traduzione/copy (S3) sia **fedele, italiana e senza fatti inventati** prima di
impaginare il PDF.

## Cosa controlla
- `title_it`, `description_it` presenti; prezzo NON nel titolo.
- `len(equipment_it) == len(equipment_de)` (allineamento 1:1).
- **0 residui tedeschi** in `content.*` (rilevamento indipendente `looks_german`).
- Numeri delle specs (Anno, Km, Potenza) invariati vs `listing.json`.
- `highlights_it` ≤ 6.

## Confini
- NON riscrive il testo: segnala e blocca.
- Rileva il tedesco in modo **indipendente** dal traduttore (non usa lo stesso glossario per giudicare).

## Output
`(ok, issues)`. Rosso → estendere il glossario / correggere S3, mai allentare il gate.
