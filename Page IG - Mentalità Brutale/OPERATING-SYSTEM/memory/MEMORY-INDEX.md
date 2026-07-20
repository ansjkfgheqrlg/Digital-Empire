# MB-OS MEMORY INDEX

## Stato

- **Data:** 2026-07-20
- **Fase:** 001 — foundations/API-first
- **Modalità runtime iniziale:** SHADOW
- **Target:** CERTIFIED_AUTO
- **Live:** NON certificato; nessun token nel repository.

## Decisioni

- `decisions/ADR-MB-001-api-first-instagram-login.md` — Graph API ufficiale, Instagram Login.
- `decisions/ADR-MB-002-progressive-autonomy.md` — SHADOW→SUPERVISED→CERTIFIED_AUTO→PAUSED.
- `decisions/ADR-MB-003-wrap-existing-engines.md` — wrap carousel/publisher legacy, no rewrite.

## Checkpoint

- `checkpoints/CP-MB-20260720-001.md` — architettura, runtime, skill e security remediation.

## Evidence gaps

1. Video originali non presenti nel checkout: Reel Pattern Extractor non forgiato.
2. OAuth Meta non eseguito in sandbox.
3. Staging HTTPS non configurato.
4. Canary/permalink/insights live non testati.
5. Password precedentemente committate devono essere ruotate dall'owner; la rimozione corrente non le revoca.

## RIPRESA DA

1. Ruotare password e attivare 2FA.
2. Completare `architecture/02-AUTHORIZATION-META.md` nel Meta Dashboard.
3. Configurare `.env` + mirror HTTPS.
4. `doctor --online`.
5. 5 dry-run reali → 1 canary SUPERVISED → snapshot Insights +48h.
6. Certificare solo con evidence reale.
7. Acquisire ≥10 Reel e lanciare Empire Studio/Content-Forge per pattern video.
