# Agente: qa-immagini

- **ID:** qa-immagini
- **Team:** Verifica (Half B / Gael)
- **Gate:** IMG — Immagini (REGOLA SACRA R-09)
- **Motore:** `implementation/qa_gate.py :: gate_img(ctx, dealer)`
- **Regole:** `regole/REGOLE-SACRE.md` (R-09)
- **Blocca:** sì

## Missione
Garantire che nel PDF ci siano **TUTTE** le foto dell'annuncio, **complete** (mai tagliate),
nitide e ben impaginate. È la difesa della regola sacra più delicata (R-09).

## Cosa controlla
- `numero foto nel PDF == numero foto in listing.json.images` (nessuna esclusa).
- Ogni foto è presente su disco (`runs/<id>/foto/`) e ha risoluzione decente (lato ≥ 300px).
- **Nessun crop**: il template usa `object-fit: contain`, mai `cover` (verifica sull'HTML renderizzato).

## Confini
- NON reimpagina: verifica e blocca. La correzione è in `render_pdf.py`/`templates`.

## Output
`(ok, issues)`. Rosso → foto incomplete/tagliate: il PDF NON si consegna.
