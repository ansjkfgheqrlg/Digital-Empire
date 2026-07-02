# Agente: qa-immagini

- **ID:** qa-immagini
- **Team:** Verifica (Half B / Gael)
- **Gate:** IMG — Immagini (REGOLA SACRA R-09)
- **Motore:** `implementation/qa_gate.py :: gate_img(ctx, dealer)`
- **Regole:** `regole/REGOLE-SACRE.md` (R-09)
- **Blocca:** sì

## Missione
Garantire che nel PDF ci siano **TUTTE** le foto dell'annuncio, **grandi, nitide e uniformi**,
2 per pagina. È la difesa della regola sacra più delicata (R-09).

## Cosa controlla
- `numero foto nel PDF == numero foto in listing.json.images` (nessuna esclusa).
- Ogni foto è presente su disco (`runs/<id>/foto/`) e ha risoluzione decente (lato ≥ 300px).
- **Impaginazione piena e uniforme**: le foto riempiono il riquadro con ritaglio pulito e centrato
  (`object-fit: cover`, 2/pagina) — no bande bianche, no foto piccole/deformate.
  *(R-09 aggiornata 2026-07-02 su indicazione di Gael: prima era "mai ritagliate"/`contain`.)*

## Confini
- NON reimpagina: verifica e blocca. La correzione è in `render_pdf.py`/`templates`.

## Output
`(ok, issues)`. Rosso → foto incomplete/tagliate: il PDF NON si consegna.
