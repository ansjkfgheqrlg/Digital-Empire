# Agente: qa-price-verifier

- **ID:** qa-price-verifier
- **Team:** Verifica (Half B / Gael)
- **Gate:** C — Prezzo
- **Motore:** `implementation/qa_gate.py :: gate_c(ctx, dealer)`
- **Regola:** `rules/R6-qa-gate.md` · formula in `rules/R4-pricing.md` (Half A)
- **Blocca:** sì

## Missione
Verificare che il prezzo finale sia **corretto e riproducibile**, ricalcolandolo in modo
**indipendente** dal pricer di Max. È la difesa contro errori di parsing del prezzo esposto e di
formula.

## Cosa controlla
- Ricalcolo indipendente: `round(listed × (1 + pct/100) + fixed_1 + fixed_2) == price.final_eur`.
- Parametri presi da `dealer.pricing_resolved` (vera indipendenza) o, in mancanza, dal `breakdown`.
- Coerenza interna del `breakdown` (`surcharge_eur`).
- `final_title` contiene prezzo formattato + `€` + marca.

## Confini
- NON ricalcola il testo/PDF: solo il prezzo.
- Indipendente dal codice di `pricer.py` (riscrive la formula, non lo importa).

## Output
`(ok, issues)`. Rosso → prezzo non affidabile: **non consegnare** il preventivo.
