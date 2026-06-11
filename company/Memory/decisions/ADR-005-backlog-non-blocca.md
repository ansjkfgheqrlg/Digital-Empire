# ADR-005 — I blocker minori non fermano la costruzione: vanno in BACKLOG

- **Data:** 2026-06-11
- **Stato:** ATTIVO
- **Decisori:** Max (direttiva esplicita)

## Contesto
Durante F4 la costruzione si è "fermata" segnalando come bloccanti due item minori
(token FB, prezzo di un prodotto). Max ha corretto la rotta: sono cavolate rimandabili,
la costruzione dell'azienda viene prima.

## Decisione
1. Un task/decisione è BLOCCANTE solo se impedisce **strutturalmente** la fase corrente
   (es. manca l'architettura, gate rosso, dipendenza tecnica vera).
2. Tutto il resto (credenziali da rinnovare, prezzi da decidere, dettagli cosmetici) va in
   **`company/Memory/BACKLOG.md`** con una riga: cosa, note, quando serve davvero.
3. Le fasi della roadmap si riformulano per aggirare i backlog item: si costruisce
   l'infrastruttura e si lascia lo slot pronto (es. outreach: si wrappa il workflow anche
   senza token FB; prezzo manuale: lo proporrà il futuro team-prezzi, B-003).
4. Le decisioni di prezzo NON si chiedono più a Max una per una: nasce un **team prezzi**
   (skill `pricing` + beast-preventivi come motori) che propone, Max approva a lotti.
5. Ritmo: **fase → gate → controllo → fase successiva**. Mai tutto in una volta,
   mai fermarsi per minuzie.

## Conseguenze
- STATO-EMPIRE non elenca più questi item come "blocchi": puntano al BACKLOG.
- I gate delle fasi vengono riletti: se un criterio dipende da un backlog item,
  si sostituisce con un criterio infrastrutturale (slot pronto + test dry).

## Contradiction-check
Nessun conflitto con ADR-001/004. Rafforza il metodo Dynamic Workflow del Piano Maestro §7.
