# PLANNING-P2 — Gap Analysis & Risk Register
> Livello 2 di 7 · migliora P1 aggiungendo: cosa manca e cosa può rompersi, con fix e proprietari.
> Regola: ogni gap ha UN fix assegnato; ogni rischio ha trigger osservabile + mitigazione + owner.

## 1. GAP REGISTER (12 gap, tutti chiusi da un fix)

| # | Gap | Blocca | Fix chirurgico | Owner | Entro |
|---|-----|--------|----------------|-------|-------|
| G-01 | Prezzo Manuale non deciso (B-003) | S2 S3 S4 | **DEC-EST-001: default €67/€97 + veto window 21/07 h20:00** (decide in 30 sec o vale il default) | Max | 21/07 |
| G-02 | Lista 7 concessionari non formalizzata | S1 | Tabella: nome, stato relazione, canale preferito, ultimo contatto | Max | 21/07 |
| G-03 | Offerta "Partenza Anticipata" non definita nei termini | S1 | Termini standard in WF-S1: setup −30% O 1° mese gratis, attivazione entro 31/07, prezzo bloccato 2026 | Claude→Max | 21/07 |
| G-04 | Account checkout non verificato (Stripe/Gumroad esiste? KYC completo?) | S2 | Verifica 10 min; fallback ladder P5 (Gumroad→PayPal→link diretto) | Gael | 22/07 |
| G-05 | Audit pagine mai fatto (P0.2) | S3 S4 | AUDIT-PAGINE-20260721.md: follower, ultimo post, accessi, 2FA, bio/link | Gael | 21/07 |
| G-06 | Chiave Fliki non testata | S5 | Test API `GET /me` o render 10s; esito in metrics | Gael | 23/07 |
| G-07 | Pipeline pubblicazione IG (anello mancante: scheduler+report) | S4 | WF-S4: Meta Graph API / Buffer; gate E2E 24/07 | Gael | 24/07 |
| G-08 | Nome prodotto S6 non scelto | S6 | **DEC-EST-002: default Preventa + veto entro 22/07 h12:00** | Max | 22/07 |
| G-09 | Case study Novacar mai scritto | S6 | case-study-forge: tempi reali, PDF esempio, schermate, preventivo tipo | Claude | 23/07 |
| G-10 | Nicchia YouTube non scelta | S5 | **DEC-EST-004: default AI/Claude IT** + conferma dati yt-niche-scout | Max | 24/07 |
| G-11 | Revenue minima della settimana non espressa in € | tutti | Definita in P6: minimo = 1 setup concessionario incassato | Chief Forge | 21/07 |
| G-12 | Nessuna dashboard giornaliera | controllo | Tracker EOD h19:00 (07-CONTROL/DASHBOARD) + metric in memoria | Claude | da 21/07 |

## 2. RISK REGISTER (top 10)

| # | Rischio | Prob. | Impatto | Trigger osservabile | Mitigazione | Owner |
|---|---------|-------|---------|--------------------|-------------|-------|
| R-01 | Max non trova tempo per call ai 7 | media | alto | 0 contatti entro 22/07 h12:00 | **WhatsApp-first asincrono** con offerta a scadenza 31/07: chiudi senza call; call solo su richiesta | Max |
| R-02 | Obiezione "ci sentiamo a settembre" | alta | alto | risposta dilatoria a ≥3 lead | Bonus che scade 31/07 + argomento: "a settembre sei GIÀ operativo, non stai installando" (script WF-S1) | Max/Claude |
| R-03 | B-003 resta aperto oltre il veto | media | critico | nessuna decisione h20:00 21/07 | Scatta il **default DEC-EST-001** automaticamente (status → ATTIVA) | sistema |
| R-04 | Checkout: setup Stripe/Gumroad lento (KYC) | media | alto | account non attivo entro 22/07 h18:00 | Fallback ladder P5: Gumroad → PayPal.me → link bonifico su landing | Gael |
| R-05 | Chiave Fliki assente/non funzionante | media | medio | test API fallito 23/07 | Fallback video ladder (script→stock footage→TTS→ffmpeg); S5 slitta, **non tocca S1/S2** | Gael |
| R-06 | Riattivazione IG troppo aggressiva → limit/ban | media | medio | action-block o reach azzerata | Rampa 1 post/giorno/pagina; solo API ufficiali; zero bot-actions | Gael |
| R-07 | Overload Gael (audit+funnel+pipeline+YT+kit) | alta | alto | task non chiusi EOD 22/07 | Sequenza rigida P3 + **diritto di slittamento S5→settimana prox** (gate G5) | Chief Forge |
| R-08 | Violazione vincolo "1 solo swarm Opus" | media | medio | 2 swarm attivi insieme | Coda swarm esplicita in workflows.yaml: priorità S1>S2>S6>S5 | Chief Forge |
| R-09 | Scope creep funnel (perfezione invece di vendibile) | alta | medio | funnel non live entro 22/07 | **Definition of Done "vendibile"** congelata in WF-S2: landing+checkout+3 email. STOP. | Gael |
| R-10 | Metriche vanity (follower, like) scambiate per risultati | media | medio | report senza € o lead | Regola P6: solo incassi, anticipi, lead, vendite contano | tutti |

## 3. Miglioramento strutturale introdotto da P2
**Pattern "decisione pre-confezionata"**: ogni decisione di Max arriva già con default + razionale + **veto window**. Max spende 30 secondi (veto/ok), mai 2 ore. Applicato a: prezzo (DEC-EST-001), nome (DEC-EST-002), nicchia (DEC-EST-004). Estendibile via `memory_manager.py decision`.

---
⛓️ Trace P12: `PLANNING-P2#estate-2026` · input: P1 · memory: DEC-EST-001/002/004
