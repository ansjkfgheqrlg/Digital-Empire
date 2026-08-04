# DEC-001 — Template PDF ufficiale = modello Novacar + REGOLE SACRE

**Data:** 2026-07-01 · **Da:** Max

## Decisione
Il PDF del preventivo deve seguire **esattamente** il modello del cliente
`Preventivo BMW Z4 2003 FR 3.0i.pdf` (concessionaria **Novacar srl**). I dati erano corretti;
i problemi erano solo di **stile/impaginazione**.

## Regole nate da qui (inviolabili → `../../regole/REGOLE-SACRE.md`)
- Pag.1 = solo logo · logo in alto a sx in ogni pagina · pag.2 = dati azienda + titolo + scheda tecnica.
- Sezioni: equipaggiamento, condizioni di garanzia, "Totale in strada (Iva inclusa)".
- **Immagini: tutte, complete (mai tagliate), grandezza perfetta, ben visibili.**
- Ultima pagina = solo logo. Migliorie di font/eleganza SÌ, rimozioni NO.

## Conseguenze operative
- Nuovo dealer `concessionarie/novacar/` con dati reali + `logo.png` (estratto dal modello).
- Rimosso il placeholder "Prof Autocad" (dealer → `novacar`, default).
- Nuovi agenti di controllo: `qa-regole-checker` (Gate R) + `qa-immagini` (Gate IMG).
- `render_pdf.py` + `templates/` da rifare sul modello Novacar (task Gael, Half B).
- Aggiunto ecosistema `Memory/` (decisioni + storico preventivi).
