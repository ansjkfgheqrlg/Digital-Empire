# 🧾 REGISTRO-ERRORI — carousel-factory (W4) (MIR-6 — standard regola Max 07-05)

> Owner: 03-CONTENT-FACTORY/CF-R5 · Controllore: CF-R6 · Standardizzato da FORGE-AGENT-SKILL (2026-07-20). ADR-003: motore vendored intoccabile; i fix stanno nei wrapper.

| # | Errore | Causa | Fix applicato | Regola per non ripeterlo |
|---|---|---|---|---|
| CE-1 | Run fallisce con exit 1 senza produrre nulla | `generate.js` richiede il **path JSON del carosello** come argomento (`process.argv[2]`); senza → errore (scoperto in B0 EmpireDesk, CP-20260719-007/008) | Tile EmpireDesk corretta (campo input JSON) da Gael | Qualsiasi chiamata al motore passa il JSON valido; selftest/health-check del chiamante DEVE includere un input minimo reale (mai "bottone vuoto"). |
| CE-2 | "Manca l'input": chiamante punta a `input/` vuota | Nessun JSON carosello preparato in `carousel-factory/input/` | Convenzione: ogni batch dichiara il file JSON in memory/run-note | Prima della run: verificare presenza del JSON input previsto (checklist pre-run). |
| CE-3 | Path non risolti da ambienti Windows con percorso contenente accenti/spazi | Cartella padre `Workfolw crea caroselli à/` (spazi + lettera accentata) nella root | Quote obbligatorie nei path; wrapper robusti (B0 EmpireDesk) | Nei .bat/script: path sempre tra doppi apici; nei subprocess: array args, mai stringa unica da concatenare. |
| CE-4 | Brand sbagliato nell'output | Run lanciata senza selezione brand esplicita | Parametro brand dichiarato nel comando run | Il nome brand è sempre esplicito nel comando/run-note; default vietati in produzione. |

**Anti-recidiva:** 2 ripetizioni dello stesso errore → regola promossa nel workflow CF-R5 o in `FORGE-AGENT-SKILL/rules/`.
