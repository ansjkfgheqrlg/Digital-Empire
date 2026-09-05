# CENSIMENTO 02b — LA MAPPA DEI COLLEGAMENTI

> **Non l'infrastruttura, ma la MAPPA: quali collegamenti l'Impero ha PROGETTATO di avere,
> scritti nei suoi dossier, e che quasi nessuno ha mai costruito.**
> Rilevazione: 2026-09-06 · Autore: DOOM BOT 02b · Committente: EMPERATOR
> Gemello: `dati/censimento-02-collegamenti.md` (infrastruttura: bus, contratti, registri, tracce).
> Metodo: ogni riga viene da un file aperto, citata con `file:riga`. Nessuna riga senza fonte.
> Legenda: **INTRA** = dentro lo stesso ecosistema · **INTER** = fra ecosistemi diversi ·
> **VAGO** = passaggio dichiarato senza carico o senza criterio.

---

## STATO DELLO SPOGLIO

| # | Fonte | Stato |
|---|---|---|
| 1 | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` + `-V2` | in corso |

---

## TABELLA DEI PASSAGGI DI CONSEGNE

### FONTE 1a — `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md`

Nota di contesto: la fonte apre la sezione 1 con la frase *"Ogni passaggio e' un handoff contract
`{from, to, payload, acceptance_criteria}` sul BUS"* (`01-ECOSISTEMA-AGENCY.md:34`). Sedici passaggi
INTER sono nominati con un codice contratto proprio (`HC-XX-YY-01`). Verifica su disco
(`find company empire -iname "*handoff*" -o -iname "HC-*"`): **nessuno dei 16 codici esiste come file**.
Gli unici 4 contratti scritti sono INTRA-AGENCY (A1→A2, A2→A3, A3→A4, A4→A6) e sono `"status": "template"`.
`grep -rn "HC-" --include=*.py --include=*.sh` su `company/` e `empire/` → **0 risultati**: nessun codice
nomina un contratto.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 1 | 01-AGENCY | 02-INFO-BUSINESS | `HC-AG-IB-01` lead non pronto: lead qualificato "non ora/budget basso" + storico conversazione | lead taggato con motivo, consenso contatto valido | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:38` | NO — file inesistente | INTER · MAI |
| 2 | 02-INFO-BUSINESS | 01-AGENCY | `HC-IB-AG-01` upsell student: cliente corso/community con segnali agency | profilo ICP compilato, fonte tracciata | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:39` | NO | INTER · MAI |
| 3 | 01-AGENCY | 03-CONTENT-FACTORY | `HC-AG-CF-01` richiesta asset cliente: `{client_brand_kit, icp, formati, deadline}` | asset conformi al brand gate del CLIENTE (multi-tenant, pattern 11) | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:40` | NO | INTER · MAI |
| 4 | 03-CONTENT-FACTORY | 01-AGENCY | `HC-CF-AG-01` consegna asset: pacchetto contenuti pronto per setup su server cliente | passato QA gate CF + brand gate | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:41` | NO | INTER · MAI |
| 5 | 01-AGENCY | 04-MARKETING | `HC-AG-MK-01` brief copy: brief APSOC + dati performance reali (reply rate, win rate) | brief completo, numeri reali, no metriche inventate | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:42` | NO | INTER · MAI |
| 6 | 04-MARKETING | 01-AGENCY | `HC-MK-AG-01` copy maggiore: sales page, sequenze, refresh template outreach, copy preventivi | passato Copy/APSOC Guild + gate Bibbia | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:43` | NO | INTER · MAI |
| 7 | 01-AGENCY | 05-MULTI-BUSINESS | `HC-AG-MB-01` know-how delivery: playbook setup/handover riusabili | playbook versionato in wiki | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:44` | NO | INTER · MAI |
| 8 | 05-MULTI-BUSINESS | 01-AGENCY | `HC-MB-AG-01` proof: demo reali (es. canale YT automatizzato) come prova nelle vendite | "prove non promesse": solo risultati verificabili | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:45` | NO | INTER · MAI |
| 9 | 06-PLATFORM | 01-AGENCY | `HC-PL-AG-01` tooling: dashboard, fix landing `agency-empire-landing`, infra, siti cliente | build verde, deploy verificato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:46` | NO | INTER · MAI |
| 10 | 01-AGENCY | 06-PLATFORM | `HC-AG-PL-01` feature request: richieste dashboard/landing/script con priorita' e KPI atteso | ticket con acceptance criteria misurabile | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:47` | NO | INTER · MAI |
| 11 | 07-FORGE | 01-AGENCY | `HC-FG-AG-01` nuovi agenti/skill quando un KPI di reparto cala sotto soglia per 2 cicli | team a schema canonico, skill ≤500 righe kernel | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:48` | NO | INTER · MAI |
| 12 | 01-AGENCY | 07-FORGE | `HC-AG-FG-01` richiesta organico: gap funzionale documentato + KPI che lo dimostra | gap non coperto da skill esistente (verifica registro) | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:49` | NO | INTER · MAI |
| 13 | 08-INTELLIGENCE | 01-AGENCY | `HC-IN-AG-01` intelligence: ricerca ICP/nicchie/trend, template second-brain per delivery €2.500 | fonti citate, ingest in wiki completato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:50` | NO | INTER · MAI |
| 14 | 01-AGENCY | 08-INTELLIGENCE | `HC-AG-IN-01` dati campo: obiezioni reali, motivi di rifiuto, domande ricorrenti | anonimizzati (aidefence has_pii), tag per nicchia | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:51` | NO | INTER · MAI |
| 15 | 09-OPERATIONS | 01-AGENCY | `HC-OP-AG-01` runtime: scheduling run giornaliere (email/LinkedIn/IG), cost guard, backup `leads.db` | run loggata, budget rispettato, dry-run disponibile | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:52` | NO | INTER · MAI |
| 16 | 01-AGENCY | 09-OPERATIONS | `HC-AG-OP-01` job: nuovi job da schedulare (follow-up, report settimanale) | job idempotente, con kill-switch | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:53` | NO | INTER · MAI |
| 17 | A1-RICERCA (`WF-LEAD-SOURCING`) | A2-ACQUISIZIONE | lead qualificato in `leads.db` con score ICP | qualifier score ≥ soglia | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:210` | SI — `company/01-agency/A1-RICERCA/handoffs/HC-A1-A2-leads.json` (status template) | INTRA · percorso 1 volta (simulazione 11 giu) |
| 18 | A2-ACQUISIZIONE (3 WF outreach) | A2 `WF-REPLY-FOLLOWUP` | messaggi inviati → risposte da gestire (email ≤500/gg cap 100/h, LI 20+20+30, IG 30 DM) | **Gate Bibbia** (blocca invio) | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:211-212` | NO | INTRA · il codice outreach gira, ma senza contratto |
| 19 | A2-ACQUISIZIONE | A3-PREVENTIVI | conversazione gestita → call prenotata | triage corretto; no risposta a "no" | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:212-213` | SI — `company/01-agency/A2-ACQUISIZIONE/handoffs/HC-A2-A3-call.json` | INTRA · 1 sola volta |
| 20 | AG-A3-BRIEF-W | UMANO (Max) — discovery call | dossier pre-call (lead + audit + competitor) | dossier pre-call consegnato prima della call | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:213` | NO | INTRA · MAI |
| 21 | A3-PREVENTIVI (`WF-PREVENTIVO`) | UMANO + T-pricing-config → A4-DELIVERY | proposta problem-first inviata ≤48h → firma + pagamento one-time | **Gate Preventivo**; pagamento verificato; scope congelato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:214-216` | SI — `company/01-agency/A3-PREVENTIVI/handoffs/HC-A3-A4-contratto.json` | INTRA · 1 sola volta |
| 22 | A4-DELIVERY (`WF-DELIVERY-*`) | CLIENTE | setup workflow sul server del cliente → run test → training → **handover codice** | **Gate Delivery**: UAT firmata dal cliente, nessuna dipendenza residua da DE | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:217`, `:329` | NO | INTRA/esterno · MAI |
| 23 | A4-DELIVERY (`WF-SUPPORTO-90GG`) | A6 | cliente a fine supporto 90gg → testimonianza + case study + proposta upsell | SLA rispettato; "prove non promesse": solo metriche reali del cliente | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:218` | SI — `company/01-agency/A4-DELIVERY/handoffs/HC-A4-A6-testimonianza.json` | INTRA · 1 sola volta |
| 24 | A6 (`WF-CASE-STUDY`) | 03-CONTENT-FACTORY | case study APSOC → produzione asset via 03 CF → pubblicazione | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:145` | NO | INTER · MAI |
| 25 | 08-INTELLIGENCE | A1 `T-icp-profiler` | definizione/aggiornamento ICP per nicchia ("input da 08 INTELLIGENCE") | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:75` | NO | INTER · **VAGO** · MAI |
| 26 | A1 `WF-MARKET-INTEL` | A2-ACQUISIZIONE + A3-PREVENTIVI | report nicchia/competitor/trend | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:71` | NO | INTRA · **VAGO** · MAI |
| 27 | `HC-AG-IN-01` (obiezioni reali) | A5 `T-objection-handler` | libreria obiezioni reali → risposte testate | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:135` | NO | INTRA · **VAGO** · MAI |
| 28 | 01-AGENCY (fallimenti) | ReasoningBank corporate (10-MEMORY) | ogni fallimento (bounce, ghosting, preventivo perso, delivery in ritardo) come pattern distillato | causa distillata (pattern 5) | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:26`, `:220-221`, `:302` | NO | INTER · MAI |
| 29 | A6 `T-upsell-mapper` | A3-PREVENTIVI / cliente | mappa cliente→offerta successiva (prodotto singolo → Engine Room €8.000 → referral) | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:148`, `:270` | NO | INTRA · **VAGO** · MAI |
| 30 | tutti gli altri 8 ecosistemi | 01-AGENCY | "AGENCY e' il pilastro revenue della holding: tutto il resto di EMPIRE OS lo alimenta o lo amplifica" | nessuno | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:16` | NO | INTER · **VAGO** (dichiarazione di principio) |
| 31 | 03-CONTENT-FACTORY + 04-MARKETING | 01-AGENCY | "fornitori principali via handoff contract" | nessuno | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:378` | NO | INTER · **VAGO** (ridondante con #4 e #6) |

