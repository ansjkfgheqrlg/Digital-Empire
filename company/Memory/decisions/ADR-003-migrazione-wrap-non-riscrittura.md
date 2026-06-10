# ADR-003 — Migrazione asset = wrap, mai riscrittura

- **Data:** 2026-06-10
- **Stato:** ATTIVO
- **Decisori:** sessione di pianificazione (recepito in tutti i dossier 01-07)

## Contesto
DE ha asset funzionanti e attivi: pipeline outreach (email/LinkedIn/IG), copy-workflow
(A1-A8+S1-S3), workflow libri, caroselli, sistema Crea Siti, Empire Studio, Memory Empire.
Riscriverli durante la migrazione in EMPIRE OS = rischio regressione su sistemi che
producono valore OGGI.

## Decisione
La migrazione (F3) è **mappatura + wrapper**: ogni asset diventa un team-workflow L3 con
README + handoff contract, ma il codice resta dov'è e com'è. I sistemi ATTIVI (outreach
in primis) non si toccano finché il sostituto non è validato in parallelo.
Empire Studio e Memory Empire si inglobano COSÌ COME SONO.

## Alternative scartate
- Riscrittura "pulita" dentro company/ — mesi di lavoro, rischio rompere il revenue.
- Lasciare gli asset fuori dalla holding — orfani, zero coordinazione (problema attuale).

## Conseguenze
- F3 è veloce (inventario + skills-map.yaml + wrapper).
- Il debito di refactoring si paga solo quando un KPI lo giustifica (decide la FORGE).

## Contradiction-check
Nessun conflitto con ADR-001/002.
