# MB-OS MEMORY INDEX

## Stato

- **Data:** 2026-07-20
- **Fase completata:** 002 — analisi, brainstorming e planning
- **Fase esecutiva successiva:** F0/F1/F2 — security + video evidence + Meta auth/media infra
- **Modalità runtime:** SHADOW
- **Target:** CERTIFIED_AUTO
- **Live:** NON certificato; nessun token nel repository.

## Decisioni

- `decisions/ADR-MB-001-api-first-instagram-login.md` — Graph API ufficiale, Instagram Login.
- `decisions/ADR-MB-002-progressive-autonomy.md` — SHADOW→SUPERVISED→CERTIFIED_AUTO→PAUSED.
- `decisions/ADR-MB-003-wrap-existing-engines.md` — wrap carousel/publisher legacy, no rewrite.

## Planning autoritativo

- `../planning/00-INDEX.md` — mappa master.
- `../planning/01-ANALISI-AS-IS.md` — diagnosi e bottleneck.
- `../planning/02-BRAINSTORMING-MASTER.md` — 64 idee / 8 domini.
- `../planning/03-DECISION-MATRIX.md` — convergenza pesata.
- `../planning/04-PIANO-ESECUTIVO-90-GIORNI.md` — roadmap F0→F9.
- `../planning/05-CALENDAR-28D-SEED.md` — 28 brief bilanciati.
- `../planning/06-BUSINESS-MODEL-PLAN.md` — revenue ladder e attribution.
- `../planning/PLAN.json` — 10 fasi / 32 task machine-readable.

## Checkpoint

- `checkpoints/CP-MB-20260720-001.md` — architettura, runtime, skill e security remediation.
- `checkpoints/CP-MB-20260720-002.md` — analisi, brainstorming e planning validati.

## Evidence gaps

1. Video originali non presenti nel checkout: Reel Pattern Extractor non forgiato.
2. OAuth Meta non eseguito in sandbox.
3. Staging HTTPS non configurato.
4. Canary/permalink/insights live non testati.
5. Password precedentemente committate devono essere ruotate dall'owner; la rimozione corrente non le revoca.
6. Funnel/offerta/prezzo non definiti: prima attribution e team-pricing.

## RIPRESA DA — critical path

1. **F0:** ruotare password, revocare sessioni, 2FA; chiudere B-009.
2. **F1 parallelo:** acquisire 10 Reel → ≥120 frame + transcript + rights ledger.
3. **F2 parallelo:** Meta app/OAuth + media host HTTPS + `doctor --online`.
4. **F3/F4:** produzione riproducibile + buffer 4 Reel/3 carousel + 35 verdict.
5. **F5:** 5 dry-run → canary → +48h Insights → certification.
6. **F6:** baseline 28 giorni / 56 snapshot.
7. **F7-F9:** learning → funnel → business test → decisione productization.
