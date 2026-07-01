# Agente: qa-output-reviewer

- **ID:** qa-output-reviewer
- **Team:** Verifica (Half B / Gael)
- **Gate:** D — Output finale (PDF)
- **Motore:** `implementation/qa_gate.py :: gate_d(ctx, dealer)`
- **Regola:** `rules/R6-qa-gate.md` · a monte: `rules/R5-pdf-render.md`
- **Blocca:** sì (ultimo cancello prima della consegna al cliente)

## Missione
Ultimo controllo prima che il PDF vada al cliente: verificare che il preventivo sia **completo,
coerente e senza difetti visibili**.

## Cosa controlla
- Esiste `preventivo_*.pdf` e pesa > 20 KB.
- Sezioni presenti: scheda tecnica, descrizione, dotazioni non vuote.
- Prezzo presente nel `final_title`.
- Tutte le foto di `listing.json` sono su disco (gallery completa).
- (Con `dealer`) re-render HTML: 0 placeholder `{{ }}`, immagini incorporate.

## Confini
- NON rigenera il PDF: verifica l'output esistente (può re-renderizzare l'HTML solo per ispezione).
- È l'unico gate che guarda l'artefatto finale, non solo i dati.

## Output
`(ok, issues)`. Verde → preventivo consegnabile. Rosso → non consegnare.
