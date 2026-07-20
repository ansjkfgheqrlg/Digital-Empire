# MB-OS · Fase 001 — SPEC + PRE-MORTEM

- **Data:** 2026-07-20
- **Mandato:** automatizzare l'operatività Instagram di `@mentalita.brutale` da produzione a apprendimento, con autorizzazione API ufficiale e controllo reversibile.
- **Owner:** Chief-Forge → ARCHITETTURA → FORGE; owner operativo CF-R0/CF-R6/CF-R7/CF-R8.
- **Riferimenti:** ADR-002, ADR-003, ADR-006, ADR-008; dossier 03 v2 e dossier 16 S4.

## DONE WHEN misurabili

1. Esiste un blueprint navigabile per authorization → content → QA → schedule → publish → insights → learning.
2. Il runtime API-first esegue almeno `doctor`, `validate`, `plan`, `enqueue`, `run-due`, `collect` e resta dry-run per default.
3. Nessun segreto è hard-coded nei file correnti del vecchio publisher; esiste `.env.example` senza valori reali.
4. La pubblicazione live richiede 5 gate PASS, token health, rate-limit check, flag env, modalità `CERTIFIED_AUTO` e kill switch `ACTIVE`.
5. Esiste una skill project-level che trasforma richieste e nuovi contenuti in workflow/knowledge/skill secondo Content-Forge.
6. Test automatici su validazione, idempotenza, live guard, scoring e secret scan passano.
7. Registro impresa, skills-map, wiki, Memory e checkpoint sono aggiornati.

## Out of scope della fase

- Inserire token, app secret o password reali.
- Pubblicare sul profilo reale senza OAuth e certificazione completati sul PC dell'owner.
- Riscrivere `carousel-factory` o il vecchio `mentalita_orchestrator.py` (ADR-003).
- Inventare risultati, follower, benchmark o pattern video non osservati.
- Automatizzare spam, engagement artificiale, scraping autenticato o aggiramento delle policy Meta.

## Dipendenze

- Account Instagram professionale owner-managed.
- Meta Business app con configurazione Instagram Login.
- Asset live su URL HTTPS pubblici durante il fetch di Meta.
- Per immagini: conversione JPEG tramite Pillow; per render: Node/Puppeteer del motore esistente.
- Per analisi video completa: file originali accessibili; nel checkout non sono presenti video tracciati.

## PRE-MORTEM

| Come fallisce | Segnale precoce | Contromisura incorporata |
|---|---|---|
| Token scade e lo scheduler fallisce in silenzio | `doctor --online` rosso; 401/190 | refresh prima della scadenza, health obbligatorio, alert e nessun retry cieco |
| Un contenuto non conforme viene pubblicato | gate mancanti o evidence vuota | 5 gate bloccanti indipendenti; default SHADOW; idempotency hash |
| Browser automation rompe dopo una modifica UI | selettori non trovati | percorso primario Graph API v25.0; vecchio browser runtime resta solo fallback non certificato |
| Meta non riesce a scaricare i media | URL privato, PNG, redirect Drive | staging HTTPS pubblico; JPEG; preflight HEAD; niente URL pagina Drive |
| Il learning ottimizza rumore | decisioni su 1 post | n≥3, confronto stesso formato, mediana, claim di correlazione e non causalità |
| Drift di brand verso frasi tossiche o motivazione vuota | QA copy/brand basso | brand-kit canonico, safety gate, forbidden claims, R6 indipendente |
| Doppia pubblicazione dopo retry/crash | stesso asset appare due volte | hash contenuto unico + publication record + retry idempotente |
| Segreti finiscono di nuovo su Git | password/token trovati da scan | env/.env locale ignorata, test secret scan, rotazione obbligatoria dei segreti storici |
| “Automazione totale” diventa assenza di controllo | pubblicazioni durante anomalia | kill switch, daily cap interno, circuit breaker, PAUSED immediato |
| Strategia video viene inventata senza aver visto i video | pattern senza frame/timestamp | evidence ledger; stato `PENDING_SOURCE`; Empire Studio deve vedere frame e file integrale |

## Reversibilità e budget guard

- Tutto è additivo sotto `OPERATING-SYSTEM/`; i motori attivi restano intatti.
- SQLite e `.env` sono locali/ignorati; Git ripristina gli artefatti tracciati.
- Nessuna API a pagamento e nessun side effect in test.
- Se il build si interrompe: ripresa da `memory/MEMORY-INDEX.md`; nessuna duplicazione grazie a hash e migrazioni idempotenti.
