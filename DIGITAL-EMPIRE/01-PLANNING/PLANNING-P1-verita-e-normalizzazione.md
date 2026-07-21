# PLANNING-P1 — Verità & Normalizzazione
> Livello 1 di 7 · 2026-07-21 · Owner: Strategy Dept · Input: Dossier "16 — PIANO ESTATE REVENUE" (19/07)
> Metodo: Mandato Art.2 — prove non promesse, anche verso noi stessi. Nessun numero inventato, ogni atomo ancorato (P12).

## 1. Estrazione normalizzata dei fatti (fact table canonica)

| # | Fatto | Fonte | Stato verifica |
|---|-------|-------|----------------|
| F-01 | PreventivoForge funziona ed è consegnato (Novacar live: GUI, PDF, .exe) | dossier S1/S6 | ✅ dichiarato, prova: installazione Novacar |
| F-02 | 7 lead concessionari "quasi confermati" per settembre | dossier S1 | ⚠️ da ricontrollare: lista nomi/stato/canale non ancora prodotta (task Max G1) |
| F-03 | Manuale Claude Code: 203pp pronto, SENZA prezzo (B-003 aperto da giugno) | dossier S2 | ✅ blocco confermato |
| F-04 | carousel-factory ha brand mentalita-brutale già configurato (ADR-003: wrappare) | dossier S4 | ✅ motore esistente |
| F-05 | Chiave Fliki SOLO in .env locale | dossier regola 4 | ⚠️ esistenza/funzionamento chiave NON verificato → test obbligatorio |
| F-06 | Vincolo: un solo swarm Opus alla volta (CP-20260711-002) | dossier regola 6 | ✅ vincolo di scheduling |
| F-07 | mentalita.brutale si riattiva SOLO con automazione 100% (condizione Max) | dossier S4 | ✅ condizione vincolante |
| F-08 | Runtime outreach A2 attivo; A1 può scrapare dealer import-DE | dossier S6 | ✅ motori attivi |
| F-09 | S5 (YouTube) NON produce revenue a 7 giorni (AdSense: 1k iscritti + 4k ore) | dossier §0 | ✅ corretto: S5 = compounding + lead-gen |
| F-10 | Il dossier NON definisce una soglia revenue minima in € | audit P1 | ❌ gap → corretto in P6 |

## 2. Anomalie trovate (correzioni chirurgiche)

| # | Anomalia | Impatto | Correzione applicata |
|---|----------|---------|----------------------|
| A-01 | **Disallineamento calendario reale**: il piano assegna G1 a "sab 19-20". Oggi è **martedì 21/07**: G1-G2 sono già consumati e i task G1 (B-003, audit, lista 7) **non risultano chiusi**. | Critico: 2/7 giorni bruciati, soglie a rischio | **DEC-EST-003**: ribasatura totale 21→26 su date assolute (vedi P3/P7) |
| A-02 | **Etichette giorni errate nel dossier**: "G2 (lun 21)" — ma il 21/07/2026 è **martedì**. Tutta la griglia giorni è sfasata di 1. | Medio: confusione esecutiva | Solo date assolute da qui in poi (regola P7-R8) |
| A-03 | **"Certezza >95%" è dichiarata come proprietà dello stream** (S1). In realtà è una **catena condizionale**: P(incasso) = P(contatto effettivo entro 48h) × P(offerta chiara) × P(chiusura). Se Max non contatta entro 22/07, la certezza decade. | Alto: rischio falsa sicurezza | Riformulata in forma misurabile in P6 (formula + soglie oneste) |
| A-04 | **Dipendenze implicite mai dichiarate**: account Stripe/Gumroad (esistente? KYC?), accessi alle pagine IG (password/2FA), chiave Fliki (attiva?), numero dei 7 lead con canale di contatto. | Alto: blocchi a metà settimana | Checklist "attivazioni G1" in P3, verifiche in WF-S* |
| A-05 | **Nessun criterio di stop**: il dossier non dice quando un'attività va abbandonata (es. S5 se la chiave Fliki non va). | Medio: rischio scope creep | Kill-criteria + gates per stream in P5 |

## 3. Asset confermati (si WRAPPANO, non si riscrivono — ADR-003)
- PreventivoForge + fabbrica `/nuovo-concessionario` + kill-switch licenze.
- carousel-factory (brand mentalita-brutale configurato).
- Runtime outreach A1/A2, script A5/A8 (WF-CLOSING-PREP), beast-preventivi/pricing.
- Motore site-* (empire-premium-style), case-study-forge, cro-copy-architect (APSOC).
- Skill clonate il 21/07: content-forge2.0, master-build-architecture, ruflo → `05-SKILLS/`.

## 4. Handoff → P2
Input certificato per l'analisi gap/rischi: 10 fatti verificati, 5 anomalie corrette, 3 decisioni-default già registrate in memoria (DEC-EST-001/002/004).

---
⛓️ Trace P12: `PLANNING-P1#estate-2026` · fonte: dossier-16 (19/07) · memory: CP-001, DEC-EST-001..004
