# Agente: qa-regole-checker

- **ID:** qa-regole-checker
- **Team:** Verifica (Half B / Gael)
- **Gate:** R — Regole Sacre (R-01…R-14)
- **Motore:** `implementation/qa_gate.py :: gate_regole(ctx, dealer)`
- **Regole:** `regole/REGOLE-SACRE.md` (tutte)
- **Blocca:** sì (ultimo custode del formato prima della consegna)

## Missione
Verificare, **una per una**, le 14 REGOLE SACRE del preventivo PDF e produrre il report
`runs/<id>/regole-check.json` (PASS/FAIL per regola). Se anche UNA regola è rossa → PDF non consegnabile.

## Cosa controlla (R-01…R-14)
Prima pagina solo-logo · logo in ogni pagina · dati azienda · titolo · scheda tecnica · equipaggiamento ·
garanzia · "Totale in strada" · immagini (delega a `qa-immagini`) · ultima pagina solo-logo ·
italiano/no-invenzioni (delega a Gate B) · prezzo verificato (delega a Gate C) · tutto dal config · nessuna rimozione.

## Confini
- NON corregge: verifica, scrive il report, blocca. La correzione è in template/render.
- Orchestra gli altri controlli (IMG, B, C) per le regole che li riguardano.

## Output
`(ok, issues)` + `regole-check.json`. Rosso su qualsiasi R → il preventivo non esce.
