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

### FONTE 1b — `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md`

La V2 dichiara i 16 handoff del v1 "restano validi" (`:56`) e ne aggiunge 6 nuovi (`:60-69`),
tutti verso i 4 reparti nuovi A7-A10. Nessuno dei 6 esiste su disco.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 32 | A4-DELIVERY | A7 Account Mgmt | `HC-AG-AM-01`: `{client_id, prodotto, milestone, contatti_referenti}` alla firma contratto | profilo cliente aperto in `agency/clients`; KAM assegnato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:64` | NO | INTRA · MAI |
| 33 | A2-ACQUISIZIONE | A8 Closing | `HC-AG-CL-01`: `{lead_id, call_transcript, dossier_pre-call, preventivo_id}` dopo risposta positiva | preventivo inviato; slot call chiusura proposto | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:65` | NO | INTRA · MAI |
| 34 | 01-AGENCY | A9 Partnership | `HC-AG-PT-01`: `{lead_non-icp, settore, motivo_esclusione}` quando un lead qualificato non rientra nei 3 prodotti DE | lead taggato; consenso contatto valido; nessun dato PII nudo | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:66` | NO | INTRA · MAI |
| 35 | A4-DELIVERY/Supporto | A10 QA-Cliente | `HC-AG-QC-01`: `{client_id, delivery_id, UAT_checklist}` dopo Gate Delivery | QA indipendente assegnato; checklist firmata | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:67`, `:513` | NO | INTRA · MAI |
| 36 | A9 Partnership | 01-AGENCY (A2) | `HC-PT-AG-01`: `{referral_lead, partner_id, commission_rate}` quando un partner invia un prospect | profilo ICP precompilato; fonte tracciata; AG-A9-QA blocca lead senza ICP | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:68`, `:482`, `:748` | NO | INTRA · MAI |
| 37 | 04-MARKETING | A8 Closing | `HC-MK-AG-02`: script di chiusura ottimizzato (APSOC, obiezioni post-preventivo) | passato Copy/APSOC Guild + gate Bibbia | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:69` | NO | INTER · MAI |
| 38 | A1 `WF-BRIEF-PRE-CALL` | A8 Closing / Max | dossier PDF/MD (ICP match + contesto nicchia) consegnato ≥2h prima della call | dossier consegnato ≥2h prima; nessun campo "da compilare" vuoto | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:135-136`, `:584` | NO | INTRA · MAI |
| 39 | AG-A1-ICP (`icp-radar`) | A9 Partnership | profili ICP per nicchia — "alimenta A9" | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:109` | NO | INTRA · **VAGO** · MAI |
| 40 | AG-A2-BOOK | A8 Closing + A7 Account Mgmt | slot proposto → conferma → `HC-AG-CL-01` ad A8 + `HC-AG-AM-01` ad A7 (anagrafica aperta) | slot confermato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:187`, `:586` | NO | INTRA · MAI |
| 41 | AG-A3-LEARN (loss preventivo) | 08-INTELLIGENCE | motivo di perdita registrato in `agency/reasoning` → `HC-AG-IN-01` | win/loss con causa | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:216`, `:233` | NO | INTER · MAI |
| 42 | A3 (win preventivo) | A7 Account Mgmt | esito win → `HC-AG-AM-01` + contratto | non dichiarato oltre il contract | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:232`, `:445` | NO | INTRA · MAI |
| 43 | 01-AGENCY (A4 Content Factory delivery) | 03-CONTENT-FACTORY | richiesta `HC-AG-CF-01` → ricezione motore → schema G+0→G+7 | conforme al brand gate cliente | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:280`, `:358` | NO | INTER · MAI |
| 44 | 08-INTELLIGENCE | A4 (delivery Second Brain) | richiesta template `HC-IN-AG-01` → configurazione vault → training workflow | fonti citate, ingest wiki completato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:285` | NO | INTER · MAI |
| 45 | AG-A5-LEARN | `agency/outreach` (memoria) | analisi reply rate per template → varianti — "alimenta `agency/outreach`" | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:315` | NO | INTRA · **VAGO** · MAI |
| 46 | A5 (`AG-A5-QA`) | A8 Closing | script discovery call e script chiusura per Max, verificati (no claim senza proof, no dependency-language) | conforme Brand Voice (Mandato Art.2) | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:326-328`, `:441` | NO | INTRA · MAI |
| 47 | AG-A6 | 06-PLATFORM | ticket landing/dashboard → `HC-AG-PL-01` → review AG-A6-QA → deploy | ticket con acceptance criteria misurabile | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:364` | NO | INTER · MAI |
| 48 | A2 | A9 (`AG-A9-QUALIFY`) | lead non-ICP da A2 → valutazione partner potenziale / nurture / archivio | non dichiarato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:466` | NO | INTRA · **VAGO** · MAI |
| 49 | 09-OPERATIONS | A1 (`leads.db`) | storage + backup schedulato di `Outreach/Outreach Workflow/leads.db` via `HC-AG-OP-01`; pre-flight check token su ogni run | run loggata, budget rispettato | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:612`, `:742` | NO | INTER · MAI |
| 50 | tutti i 10 reparti AGENCY | `agency/kpi` → dashboard | metriche per reparto per ciclo — "alimenta dashboard" | KPI visibili e alimentati da **dati reali** | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:39`, `:700`, `:726` | NO | INTRA · **VAGO** · MAI |
| 51 | 01-AGENCY | tutti gli ecosistemi (budget) | revenue → budget operativo: "vengono alimentati da essa (revenue → budget operativo)" | nessuno | `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md:52-53` | NO | INTER · **VAGO** (nessun contratto, nessun destinatario nominato) |

### FONTE 2a — `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md`

Qui i passaggi INTER non hanno un codice contratto: hanno una tabella "Handoff in INGRESSO" (`:38-46`)
e "Handoff in USCITA" (`:48-55`) piu' un formato JSON di esempio (`:57-70`) con campi
`from/to/payload/acceptance_criteria/deadline/fallback` — **un quinto schema**, diverso dai tre gia'
censiti in `dati/censimento-02-collegamenti.md`. Nessuno di questi handoff esiste su disco.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 52 | 03-CONTENT-FACTORY | 02-INFO-BUSINESS / Reparto Prodotto | moduli video corso (script approvato → video montato), caroselli/reel pre-lancio, thumbnail | formato/durata da brief; brand voice gate passato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:42` | NO | INTER · MAI |
| 53 | 04-MARKETING | 02-INFO-BUSINESS / Reparto Lanci | sequenze email lancio (pre-lancio, cart open, cart close), copy sales page, ad copy | APSOC ≥80/100; CTA univoca; zero claim non provabili | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:43` | NO | INTER · MAI |
| 54 | 08-INTELLIGENCE | 02-INFO-BUSINESS / Prodotto + Lanci | customer research, trend, ingest fonti (Thought Leader Funnel / Founder Authority Stack), pattern da ReasoningBank | atomi archiviati in wiki + namespace memoria | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:44` | NO | INTER · MAI |
| 55 | 06-PLATFORM | 02-INFO-BUSINESS / Reparto Prodotto | piattaforma corso (Supabase + Next.js), checkout, paywall tecnico, fix | deploy verde + smoke test studente | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:45` | NO | INTER · MAI |
| 56 | 07-FORGE | 02-INFO-BUSINESS / tutti i reparti | nuovi agenti/skill su richiesta (es. skill `course-architect`) | skill passa skill-creator eval | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:46` | NO | INTER · MAI |
| 57 | 02-INFO-BUSINESS | 01-AGENCY / Reparto Acquisizione | **lead caldi cross-sell**: acquirenti corso/ebook con bisogno di implementazione (domande community, moduli avanzati, richieste dirette) | `{lead, fonte_prodotto, segnale, score}`; lead consenziente; segnale documentato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:52`, `:348` | NO | INTER · MAI (gemello di #2 `HC-IB-AG-01`) |
| 58 | 02-INFO-BUSINESS | 03-CONTENT-FACTORY / Reparto Strategia | brief contenuti pre-lancio (angoli, hook, calendario), estratti corso riusabili come organico | brief con ICP + obiettivo per pezzo | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:53` | NO | INTER · MAI |
| 59 | 02-INFO-BUSINESS | 05-MULTI-BUSINESS / Publishing-KDP | contenuto corso/ebook riconfezionabile per KDP (multi-tenant by design) | diritti/formato verificati | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:54` | NO | INTER · MAI |
| 60 | 02-INFO-BUSINESS | 09-OPERATIONS / Cost guard | stima costi lancio (dry-run), scheduling sequenze | budget approvato prima del go | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:55` | NO | INTER · MAI |
| 61 | Board / C-Suite | `ib-conductor` | obiettivi di ecosistema → smistamento ai reparti, ritorno KPI | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:141` | NO | INTER · **VAGO** · MAI |
| 62 | `T-design-prodotto` | 03-CONTENT-FACTORY | copertine, slide, workbook → handoff a CF per i video | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:90` | NO | INTER · **VAGO** · MAI |
| 63 | `T-copy-liaison` / `ib-copy-liaison` | 04-MARKETING | compone gli handoff verso MARKETING e **verifica i rientri contro acceptance criteria** | APSOC ≥80 sui rientri | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:101`, `:154` | NO | INTER · MAI (unico "verificatore di rientro" nominato in tutto l'Impero) |
| 64 | `T-crosssell` / `ib-crosssell-scout` (skill `referrals`) | 01-AGENCY | scoring segnali "vuole l'implementazione fatta" → handoff contract | lead consenziente + segnale documentato + score | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:130`, `:166`, `:292` | NO | INTER · MAI |
| 65 | WF-CORSO (task 4) | 03-CONTENT-FACTORY | script video → moduli video montati | durata, formato, qualita' audio | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:186` | NO | INTER · MAI |
| 66 | Reparto Prodotto | L2-VENDITE (INTRA) | corso live su piattaforma + asset vendita preliminari | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:191` | NO | INTRA · **VAGO** · MAI |
| 67 | WF-LANCIO T-28 | 08-INTELLIGENCE | richiesta customer research / angoli (frame Thought Leader Funnel) | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:201` | NO | INTER · MAI |
| 68 | WF-LANCIO T-21 | 03-CONTENT-FACTORY | contenuti organici pre-lancio (calendario brief per pezzo) | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:202` | NO | INTER · MAI |
| 69 | WF-LANCIO T-14 | 04-MARKETING | sales page + sequenza pre-lancio | **GATE: APSOC ≥80/100** | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:203` | NO | INTER · MAI |
| 70 | `Lancio corso skill beast/lezione n.1.mp4` + `content-carousels.html` | 03-CONTENT-FACTORY | lezione pilota → WF-CORSO; caroselli → handoff CF | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md:249` | NO | INTER · **VAGO** · MAI |

### FONTE 2b — `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md`

La V2 promuove i passaggi generici del v1 a **11 contratti nominati** (`HC-CF-IB-01` … `HC-IB-OP-01`,
`:71-90`). Nessuno esiste su disco. Nota: il v1 diceva `HC-IB-AG-01` "documentato nel v1" (`:68`) —
in realta' nel v1 quel codice compare solo dentro `01-ECOSISTEMA-AGENCY.md:39`, mai come file.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 71 | 03-CONTENT-FACTORY | 02-IB / Area Prodotto | `HC-CF-IB-01`: moduli video corso, caroselli pre-lancio, thumbnail | formato/durata da brief; brand voice gate; **zero asset senza brief di origine** | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:75` | NO | INTER · MAI |
| 72 | 04-MARKETING | 02-IB / Area Lanci | `HC-MK-IB-01`: sequenze email lancio, copy sales page, ad copy | APSOC ≥80/100; CTA univoca; zero claim non provabili; nomenclatura file da brief | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:76` | NO | INTER · MAI |
| 73 | 08-INTELLIGENCE | 02-IB / Prodotto + Lanci | `HC-IN-IB-01`: customer research, trend nicchia, ingest fonti, pattern ReasoningBank | atomi in wiki + namespace `infobusiness/intel`; fonte citata | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:77` | NO | INTER · MAI |
| 74 | 06-PLATFORM | 02-IB / Area Prodotto | `HC-PL-IB-01`: piattaforma corso (Supabase + Next.js), checkout, paywall, fix bug | deploy verde + smoke test studente; uptime 99%; handoff con credentials | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:78`, `:175`, `:219`, `:415` | NO | INTER · MAI |
| 75 | 07-FORGE | 02-IB / tutte le aree | `HC-FO-IB-01`: nuovi agenti/skill su richiesta | skill passa skill-creator eval; scheda agente millimetrica conforme V2 | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:79` | NO | INTER · MAI |
| 76 | 09-OPERATIONS | 02-IB / Lanci + Prodotto | `HC-OP-IB-01`: budget approvato per lancio, scheduling run, cost report | approvazione scritta prima del go/no-go; stima costi dry-run inclusa | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:80` | NO | INTER · MAI |
| 77 | 02-IB / Area Community | 01-AGENCY (Acquisizione) | `HC-IB-AG-01`: lead caldi cross-sell con segnale esplicito | `{lead_id, fonte_prodotto, segnale_esplicito, score, consenso}`; score ≥5; nessun outreach automatico senza consenso; valida IB-COMM-QA | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:86`, `:487`, `:537`, `:817` | NO | INTER · MAI |
| 78 | 02-IB / Area Lanci | 03-CONTENT-FACTORY | `HC-IB-CF-01`: brief contenuti pre-lancio (angoli, hook, calendario, ICP) | brief con ICP + obiettivo per pezzo + scadenza T-21 | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:87`, `:297` | NO | INTER · MAI |
| 79 | 02-IB / Area Vendite | 04-MARKETING | `HC-IB-MK-01`: briefing funnel evergreen — offer stack, sales page, email nurture | offer stack approvato dall'Area Vendite prima del briefing | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:88`, `:279`, `:298` | NO | INTER · MAI |
| 80 | 02-IB / Area Prodotto | 05-MULTI-BUSINESS (Publishing/KDP) | `HC-IB-MB-01`: contenuto corso/ebook riconfezionabile per KDP | diritti verificati; formato conforme; decision scritto nel catalogo | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:89` | NO | INTER · MAI |
| 81 | 02-IB / Area Lanci | 09-OPERATIONS | `HC-IB-OP-01`: stima costi lancio (dry-run), scheduling sequenze, report post-lancio | budget approvato prima del go; reale vs piano nel debrief | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:90` | NO | INTER · MAI |
| 82 | IB-PROD-WRITER | 03-CONTENT-FACTORY | script lezioni/capitoli (voce DE) → "consegna a CONTENT-FACTORY per video" | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:174`, `:217` | NO | INTER · **VAGO** · MAI |
| 83 | IB-PROD-DESIGN | 03-CONTENT-FACTORY | brief grafiche (copertine ebook, slide, workbook, certificato) | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:176` | NO | INTER · **VAGO** · MAI |
| 84 | Area Prodotto (WF-CORSO / WF-EBOOK) | IB-L2-VEND (Area Vendite) | corso live + asset vendita; file ebook (PDF+ePub) + pagina download + asset lancio | **Gate Qualita' Prodotto**: 100% atomi fonte coperti, outcome verificabile per lezione, smoke test studente verde | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:225`, `:245`, `:811` | NO | INTRA · MAI |
| 85 | Area Lanci (WF-LANCIO) | IB-L2-COMM | onboarding acquirenti ≤24h → WF-ONBOARDING-STUDENTE | % onboarding ≤24h ≥90% | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:319`, `:864` | NO | INTRA · MAI |
| 86 | Area Lanci (debrief) | Area Vendite + 04-MARKETING | libreria evergreen + "segnalazione a 04-MARKETING per update template" | non dichiarato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:367` | NO | INTRA + INTER · **VAGO** · MAI |
| 87 | Area Strategia | Area Prodotto | product backlog di idee pre-validate: "L'Area Prodotto non dovrebbe mai cercare idee: le riceve gia'" | **Gate Validazione Idea**: score ≥60/100 + ≥5 "si', lo comprerei" reali | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:552`, `:570-571`, `:810` | NO | INTRA · MAI |
| 88 | Board C-Suite (COO/CRO-Revenue) | `ib-director` | obiettivi → smistamento ai 5 Capi Area; ritorno KPI trimestrali | solo `ib-director` sblocca escalation L3 | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:623` | NO | INTER · MAI |
| 89 | 02-IB (debrief lancio) | ReasoningBank (10-MEMORY) → 07-FORGE | WF-DEBRIEF-LANCIO → ReasoningBank → aggiornamento skill/agenti via FORGE | ≥3 pattern in ReasoningBank; ≥1 skill arricchita da dati reali lancio | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:866` | NO | INTER · MAI |
| 90 | Cost-Sentinel + 09-OPERATIONS | Area Lanci (gate T-1) | approvazione budget dry-run prima del go | **Gate Dry-Run + Costi**: simulazione OK + budget approvato | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:814` | NO | INTER · MAI |
| 91 | Quality-Sentinel + Brand-Voice-Sentinel + Cost-Sentinel | `ib-director` (T-0) | consenso hive-mind unanime per go/no-go lancio — **UN NO blocca** | consensus unanime a 5 voci | `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md:815` | NO | INTER (sentinelle corporate) · MAI |

### FONTE 3a — `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md`

CF e' l'unico ecosistema che dichiara un **modello committente/fornitore esplicito**: *"non ha clienti
propri, ha committenti"* (`:45`). L'ingresso e' un "Contratto di ordine" JSON (`:49-61`) e *"nessun
lavoro parte senza ordine valido"* (`:63`). Verifica su disco: `find . -type d -name "orders"` → **0
risultati**; `find . -name "brand-kit.json"` → **0 risultati**. Il punto d'ingresso unico non esiste,
quindi ogni ordine dei 9 ecosistemi committenti e' MAI PERCORSO per costruzione.
Lo schema handoff interno di CF (`:96-103`, campi `from/to/order_id/payload/acceptance_criteria/on_reject`)
e' un **sesto schema** diverso da tutti gli altri.

| # | DA (committente) | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 92 | 01-AGENCY | 03-CF | ordina contenuti per i clienti (deliverable "Content Factory €3.500"), creative per outreach, case study visuali | ordine valido `{committente, brand_kit, icp, formato, quantita, deadline, budget}` | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:110`, `:49-63` | NO (`orders/` non esiste) | INTER · MAI |
| 93 | 01-AGENCY | 03-CF | fornisce `brand_kit` + `icp` dei clienti + accesso account cliente | brand_kit conforme allo schema `:66-88` | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:110` | NO (`brand-kit.json` non esiste su disco) | INTER · MAI |
| 94 | 02-INFO-BUSINESS | 03-CF | ordina asset lancio: caroselli, VSL/video corso, email-ready, grafiche sales page; fornisce calendario lancio, offerta, price point | priorita' alta in finestra lancio | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:111` | NO | INTER · MAI |
| 95 | 04-MARKETING | 03-CF | ordina creative per ads (`ad-creative`), visual A/B test | BUS bidirezionale | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:112` | NO | INTER · MAI |
| 96 | 04-MARKETING | 03-CF | fornisce **copy APSOC validato** (Copy Guild). Confine: *"il copy che vende e' SEMPRE di Marketing; CF scrive solo copy strutturale: slide, caption, script base"* | APSOC validato dalla Copy Guild | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:112`, `:520` | NO | INTER · MAI |
| 97 | 05-MULTI-BUSINESS | 03-CF | ordina video YouTube (script→render→thumbnail), copertine/interni KDP, creative e-commerce; fornisce brand_kit canale/libro, nicchia, formato piattaforma | batch ricorrenti | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:113` | NO | INTER · MAI |
| 98 | 06-PLATFORM | 03-CF | fornisce tooling: render farm locale, fix script Puppeteer/ffmpeg, hosting asset (in cambio: grafiche per siti, raro) | ticket `cf→platform` | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:114` | NO | INTER · MAI |
| 99 | 07-FORGE | 03-CF | fornisce nuove skill/agenti CF quando i KPI calano o serve un formato nuovo | richiesta `cf→forge` con spec | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:115` | NO | INTER · MAI |
| 100 | 08-INTELLIGENCE | 03-CF | brief di ricerca: trend, hook che funzionano, analisi competitor | `intel→cf` brief | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:116`, `:136` (`T-trend-intake`) | NO | INTER · MAI |
| 101 | 03-CF | 08-INTELLIGENCE / wiki | **ogni output di CF da loggare in wiki** | `cf→wiki` log **obbligatorio** | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:116` | NO | INTER · MAI |
| 102 | 09-OPERATIONS | 03-CF | runtime swarm, scheduling cron, storage asset, cost guard centrale | infrastruttura condivisa | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:117` | NO | INTER · **VAGO** · MAI |
| 103 | LX/L0 Board | 03-CF | ordina contenuti corporate DE; fornisce Mandato Empire (gate non parametrici: pricing policy, "prove non promesse") | governance | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:118` | NO | INTER · MAI |
| 104 | CF-R4 `WF-CAROSELLO` | CF-R5 `WF-PUBLISH` | `{asset_dir: orders/<id>/06-delivery/, manifest: manifest.json}` | 3 gate verdi in `state.json`; caption presente per ogni canale richiesto; `on_reject`: torna a CF-R4 con motivo strutturato, 2 reject → escalation CF-A00 | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:96-103`, `:255`, `:282` | NO | INTRA · MAI (**unico handoff dell'Impero con regola di rifiuto scritta**) |
| 105 | CF-R5-A04 delivery-packager | committente (qualsiasi) | pacchetto + manifest in Drive/cartella cliente (`WF-DELIVERY`, committenti non-social) | acceptance criteria handoff | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:166`, `:204`, `:255` | NO | INTER · MAI |
| 106 | CF-R5 `WF-FEEDBACK` | 04-MARKETING Analytics + `cf/patterns` | performance post-pubblicazione → cosa funziona per quale brand | non dichiarato | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:167` | NO | INTER · **VAGO** · MAI |
| 107 | CF `WF-NEWSLETTER` | 04-MARKETING | blocco CTA in handoff a MKT | non dichiarato | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:150` | NO | INTER · **VAGO** · MAI |
| 108 | committente | CF-A00-conductor | ordine → validazione contratto → smistamento ai reparti, gestione precedenze; ordini incompleti rifiutati con **escalation al committente, non improvvisazione** | ordine completo | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:63-64`, `:178` | NO | INTER · MAI |
| 109 | CF-R3 (`WF-ARTICOLO`/`WF-NEWSLETTER`) | 04-MARKETING Copy Guild | handoff APSOC (GATE-COPY-APSOC eseguito con `cro-copy-architect`, in handoff con la Copy Guild) | gate APSOC verde | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:478`, `:500` | NO | INTER · MAI |
| 110 | 05-MB (YouTube) | CF | il committente 05-MB riceve le varianti A/B (dry-run: solo i 3 concept) | non dichiarato | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:306` | NO | INTER · **VAGO** · MAI |

### FONTE 3b — `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md`

La V2 riprende la stessa matrice del v1 (`:108-122`) e le mette **un codice contratto** dove il v1
aveva solo "BUS". Due codici sono nuovi (`HC-MK-CF-01`, `HC-MB-CF-01`); gli altri due riusano i codici
gia' dichiarati da AGENCY e INFO-BUSINESS — il che rende `HC-AG-CF-01` e `HC-IB-CF-01` gli unici due
handoff dell'Impero **dichiarati da entrambe le parti** (mittente e destinatario), pur non esistendo.
Le righe che ripetono il v1 non sono ri-numerate: qui solo cio' che il v1 non diceva.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 111 | 04-MARKETING | 03-CF (R4) | `HC-MK-CF-01` **bidirezionale**: MKT ordina creative/visual A/B; CF chiede il blocco APSOC/CTA | *"handoff MARKETING richiesto prima che il blocco CTA venga scritto da CF (confine non valicabile); merge solo con blocco APSOC approvato dalla Copy Guild"* | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:114`, `:375-376` | NO | INTER · MAI (**il piu' vincolante di tutto l'Impero: blocca la produzione CF**) |
| 112 | 05-MULTI-BUSINESS | 03-CF | `HC-MB-CF-01`: batch ricorrenti video YT/copertine KDP/creative e-commerce | batch ricorrenti; brand_kit canale/libro | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:115` | NO | INTER · MAI |
| 113 | committente | CF-D-DISPATCH | ordine → gate CF-D-QA (brand_kit+icp presenti, budget dichiarato, formato riconosciuto) → crea `orders/<id>/state.json+trace.jsonl` → CF-D-SCHED assegna slot → **notifica committente** | gate d'ingresso a 3 criteri | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:191` | NO (`orders/` non esiste) | INTER · MAI |
| 114 | CF-R1 (piano editoriale) | 04-MARKETING `WF-CALENDAR` | *"il piano si intreccia con WF-CALENDAR di 04-MARKETING per coordinare lancio ads + contenuti organici"* | piano consegnato entro venerdi' per settimana successiva; nessuno slot senza brand_kit validato | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:238-239` | NO | INTER · **VAGO** ("si intreccia") · MAI |
| 115 | committente brand (se esterno) | CF-R2 (registry) | approvazione aggiornamento `brand_kit` su richiesta o su evidenza drift | nessun aggiornamento senza approvazione CF-R2-COORD **+ committente brand** | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:279-280` | NO | INTER · MAI |
| 116 | CF-R4 (`WF-SCRIPT-VIDEO`) | CF-R3 (`WF-VIDEO-UGC`/`WF-VIDEO-AVATAR`) | `script.md` con hook 3s, corpo, CTA | GATE-COPY: hook nei 3s, CTA presente, `parole_vietate` assenti da brand_kit | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:381` | NO | INTRA · MAI |
| 117 | CF-R6-REWORK | reparto d'origine | motivo strutturato → rinvio al reparto corretto con specifica; traccia n. rework per pezzo | ogni pezzo trattato come singolo (nessuna abbreviazione per batch) | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:470`, `:485` | NO | INTRA · MAI (**secondo canale di ritorno scritto dell'Impero**) |
| 118 | CF-R7-DELIVER | committente non-social | pacchetto + `manifest.json` (lista asset, checksum) via canale richiesto dall'ordine → CF-R7-CHECK conferma ricezione → closure ordine | manifest completo; **nessuna consegna senza conferma ricezione** | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:512`, `:533-534` | NO | INTER · MAI (**unico handoff con ricevuta di ritorno**) |
| 119 | CF-R7-FEEDBACK | 04-MARKETING Analytics + `cf/patterns` + CF-R6-LEARN | metriche a 48h e 7gg → `memory_store("cf/patterns", {brand, formato, hook, metriche})` → analisi ads+organico integrata → aggiornamento soglie gate | non dichiarato | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:514`, `:538` | NO | INTER + INTRA · MAI |
| 120 | committente | CF-R5 (thumbnail/varianti) | il committente **sceglie** la variante A/B → scelta registrata in `cf/patterns` | thumbnail selezionata e approvata dal committente; titolo conforme a `brand_kit.voice` | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:434`, `:529` | NO | INTER · MAI |
| 121 | CF-D-BUDGET | CF-D-LEAD → Board (hive-mind) | alert se un ordine sfora la soglia globale; escalation al Board se due committenti hanno stessa priorita' e il budget non copre entrambi | precedenza `deadline → revenue impact (Agency/Lanci) → interno` | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:183`, `:124-126` | NO | INTRA → INTER · MAI |
| 122 | CF-R8 | Board / ADR | propone ADR su pattern strutturali dalla libreria hook/formule | non dichiarato | `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md:556` | NO | INTER · **VAGO** · MAI |


### FONTE 4a — `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md`

MARKETING e' l'ecosistema piu' **richiesto** dell'Impero: *"Il suo prodotto e' il copy degli altri 8
ecosistemi"* (`:20`) e *"nessun ecosistema scrive copy di conversione in autonomia"* (`:68-70`) —
cioe' ogni riga di copy che porta a un incasso dovrebbe attraversare questo collo di bottiglia.
Il contratto d'ingresso e' un JSON `{committente, formato, awareness_level, icp, obiettivo, deadline}`
(`:76-84`) — **settimo schema** diverso dai sei gia' censiti — ed e' l'unico dell'Impero che dichiara
anche il **contratto di risposta**: `{copy_finale, score_A8, qa_report, brand_gate, pattern_usati}`
(`:95`). Verifica su disco: `ls company/04-marketing` → **directory inesistente** (esiste solo
`company/Ecosistemi/04-MARKETING/`); `find company -type d -name handoffs` → solo `01-agency/A1..A4`
e `Backbone/Bus`. **Nessun handoff di MARKETING esiste su disco: ne' in entrata ne' in uscita.**

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 123 | 01-AGENCY | 04-MARKETING | copy preventivi/proposte commerciali; copy outreach (email/DM/LinkedIn); copy landing offerte (Outreach Factory, Content Factory, Second Brain, Engine Room) | WF-COPY-REVIEW su output `beast-preventivi`; standard APSOC+V per outreach | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:63` | NO (`company/04-marketing/` non esiste) | INTER · MAI |
| 124 | 02-INFO-BUSINESS | 04-MARKETING | copy lancio completo: sales page, sequenza email lancio, VSL, ads di lancio | WF-COPY-SALES-PAGE gate ≥85 + WF-EMAIL-LAUNCH + WF-ADS-CAMPAIGN | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:64` | NO | INTER · MAI |
| 125 | 03-CONTENT-FACTORY | 04-MARKETING | copy per asset: hook, caption, titoli, script intro, CTA nei contenuti | WF-COPY-SOCIAL + T-HEADLINE | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:65` | NO | INTER · MAI (specchio di #96 e #111) |
| 126 | 05-MULTI-BUSINESS | 04-MARKETING | titoli/descrizioni YouTube; copy listing KDP/e-commerce; description app | T-HEADLINE + WF-COPY-QUICK con pattern industry-specific | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:66` | NO | INTER · MAI |
| 127 | 04-MARKETING (se' stessa) | 04-MARKETING | campagne ads DE, email list DE, ottimizzazione funnel DE | tutti i gate | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:67` | NO | INTRA · MAI |
| 128 | 08-INTELLIGENCE | 04-MARKETING | ricerca ICP, trend — "richiede a" | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:53` | NO | INTER · **VAGO** · MAI |
| 129 | 03-CONTENT-FACTORY | 04-MARKETING | asset visivi per ads — "richiede a" | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:53-54` | NO | INTER · **VAGO** · MAI |
| 130 | 06-PLATFORM | 04-MARKETING | landing / tracking | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:54` | NO | INTER · **VAGO** · MAI |
| 131 | 09-OPERATIONS | 04-MARKETING | runtime swarm, cost guard | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:54` | NO | INTER · **VAGO** · MAI |
| 132 | committente (01/02/03/05) | MKT-Conductor | richiesta copy come messaggio strutturato sul BUS `{committente, formato, awareness_level, icp, obiettivo, deadline}` + opzionali `brand_kit`/`materiali`/`vincoli`/`acceptance_criteria` | **senza `icp` il router spawna A2/T-AVATAR: "non si scrive copy senza avatar"**; senza `awareness_level` lo deduce e lo dichiara (mai implicito) | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:26-27`, `:74-94`, `:228-233` | NO | INTER · MAI |
| 133 | 04-MARKETING | committente (qualsiasi) | **contratto di risposta**: `{copy_finale, score_A8, qa_report, brand_gate: pass/fail, pattern_usati}` | **G4 Contract check** (MKT-Conductor): la risposta soddisfa gli `acceptance_criteria` del committente, altrimenti rework o rinegoziazione | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:95`, `:251`, `:414` | NO | INTER · MAI (**unico handoff dell'Impero con contratto di ritorno formalizzato**) |
| 134 | 04-MARKETING (WF-ADS-CAMPAIGN) | 03-CONTENT-FACTORY | richiesta visual/creative dentro la campagna ads, in parallelo swarm con WF-COPY-AD | AD4 Compliance policy check prima del setup; **spesa reale vietata senza ok esplicito dell'utente** | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:258`, `:266`, `:270` | NO | INTER · MAI |
| 135 | 04-MARKETING (WF-EMAIL-LAUNCH) | 02-INFO-BUSINESS (committente) | sequenza lancio completa (pre-lancio → apertura → proof → obiezioni → scarcity → chiusura) consegnata per l'invio | gate A8 (≥80) + brand gate; **review umana nelle prime fasi** | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:279-283` | NO | INTER · MAI |
| 136 | 02-INFO-BUSINESS + 05-MB/SaaS (trigger churn) | 04-MARKETING (E1 win-back) | segnale di churn → sequenza win-back + exit survey | *"il churn E' un'obiezione non gestita"* (A6 Objections Handler) | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:289-292` | NO | INTER · MAI |
| 137 | AN4 Insight Distiller | ReasoningBank + `marketing/copy/patterns/{icp}` + `marketing/handoffs/log` + wiki | performance per `copy_id` → anti-pattern / pattern vincente per ICP, poi revisione mirata e A/B test | verdetto "inconclusivo" se sotto soglia volumi (mai forzato); pattern consolidati solo con evidenza ripetuta | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:301-307`, `:391-397`, `:454` | NO | INTRA → INTER (10-MEMORY) · MAI |
| 138 | 04-MARKETING | 07-FORGE | richiesta agenti nuovi (MKT-0, AN4, AD1-AD4, E1-E3) con schema team canonico | `skill-contradiction-analyzer` prima di ogni skill nuova | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:218`, `:366` | NO | INTER · MAI |
| 139 | MKT-Conductor | C-Suite hive-mind (raft) | escalation quando due committenti confliggono sulla stessa deadline / conflitti di priorita' | arbitrato via `deadline` nel contratto; non risolti localmente | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:374-376`, `:456` | NO | INTER · MAI |
| 140 | 04-MARKETING (M2) | 01-AGENCY | **primo handoff reale previsto**: copy reale per outreach/preventivo + baseline KPI | *"il committente accetta la consegna (G4 verde) senza intervento manuale nel routing"* | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:436` | NO | INTER · MAI (**il collegamento che il dossier stesso mette per primo**) |
| 141 | 02-INFO-BUSINESS (M3) | 04-MARKETING | primo handoff da INFO-BUSINESS: sequenza di lancio | una sequenza completa gated e consegnata | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:437` | NO | INTER · MAI |
| 142 | 03-CONTENT-FACTORY | 04-MARKETING (gate CTA) | *"quando un contenuto ha CTA di conversione, la CTA passa dal gate Marketing"* — confine di competenza | gate A8 + brand gate vivono in MARKETING, non in CF | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:68-70` | NO | INTER · MAI (regola di confine, gemella di #111) |

### FONTE 4b — `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md`

La V2 non tocca la tabella dei committenti (`:82-88`, identica al v1) e dichiara il contratto
*"identico al v1, e' gia' solido"* (`:94`). Aggiunge pero' **due reparti nuovi** — L2.5 Brand &
Creative Strategy e L2.6 Conversion Architecture — che generano passaggi che il v1 non aveva, e
sposta il verbo: dove il v1 diceva "richiede a", la V2 scrive **"DIPENDE DA"** (`:68-71`). Aggiunge
al contratto di risposta il campo `workflow_eseguito` (`:449`) e un gate nuovo, **G5 Brand
consistency**, che e' l'unico gate dell'Impero che **rimanda indietro il brief al committente**
(`:592`). Righe qui sotto: solo cio' che il v1 non diceva.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 143 | 04-MARKETING (BR3 Creative Director) | 03-CONTENT-FACTORY | brief visivo/creativo + direction per creative ads, dentro la campagna paid | AD4 Compliance G3 policy check a valle; visual in parallelo swarm con le varianti copy | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:303`, `:484`, `:664` | NO | INTER · MAI (specchio di #95/#111: **entrambe le parti lo dichiarano, nessuna lo costruisce**) |
| 144 | 08-INTELLIGENCE | 04-MARKETING (AD1 Audience Analyst) | ricerca audience, segmenti, lookalike per piattaforma — "input da 08-INTELLIGENCE" | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:212` | NO | INTER · **VAGO** · MAI |
| 145 | 08-INTELLIGENCE | 04-MARKETING (BR4 Brand Analyst, A2, S2) | competitor data, ICP data, trend, awareness di mercato — "in coordinamento con 08-INTELLIGENCE" | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:304`, `:703` | NO | INTER · **VAGO** · MAI |
| 146 | 04-MARKETING (WF-BRAND-KIT-BUILD, L2.5) | qualsiasi committente multi-tenant | `brand_kit` costruito (voice guide + visual brief + ICP + tone chart) **da usare nel contratto handoff** di tutti gli altri | BRAND-LEAD approva; kit depositato in `marketing/brand/kits/{brand_kit_id}` | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:323` | NO | INTER · MAI (**e' il pezzo che manca a CF: `brand-kit.json` non esiste su disco, cfr. #93**) |
| 147 | 04-MARKETING (L2.6 WF-FUNNEL-DESIGN) | L2.1 Copywriting | copy per stage del funnel (ToFu → MoFu → BoFu con mapping APSOC) | CA-QA verifica coerenza APSOC end-to-end; ogni stage ha copy gated | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:351` | NO | INTRA · MAI |
| 148 | 04-MARKETING (L2.6 CA2 / WF-FUNNEL-DESIGN) | 06-PLATFORM | **landing brief tecnico** — *"Marketing possiede la STRATEGIA di conversione; Platform possiede l'implementazione"* | brief tecnico approvato da 06-PLATFORM (gate d'uscita M5) | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:336-337`, `:344`, `:351`, `:665` | NO | INTER · MAI |
| 149 | 04-MARKETING (L2.6 WF-FUNNEL-DESIGN) | L2.3 Email | sequenza email dello stage del funnel | copy gated per stage | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:351` | NO | INTRA · MAI |
| 150 | 04-MARKETING (AN1 Tracking Engineer) | 06-PLATFORM | tracking plan, UTM, eventi, conversion API — "in coordinamento con 06-PLATFORM" | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:277` | NO | INTER · **VAGO** · MAI |
| 151 | AN5 Funnel Analyst | L2.6 + A8 (diagnosi) + CA3 | drop rate per sezione APSOC, bounce, micro-conversion → innesco WF-CRO-SPRINT | verdetto A/B statisticamente valido; implementazione solo dopo gate AN3 | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:280`, `:345`, `:352` | NO | INTRA · MAI |
| 152 | AN3 Experiment Designer | E3 Segmentation Analyst | segmenti per ICP × awareness × comportamento — "input da AN3" | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:247` | NO | INTRA · **VAGO** · MAI |
| 153 | 05-MULTI-BUSINESS / 02-INFO-BUSINESS | 04-MARKETING (E4 Onboarding Specialist) | richiesta sequenze onboarding welcome + attivazione per SaaS/Info | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:248` | NO | INTER · MAI |
| 154 | AN-OBSERVER | MKT-Conductor + report CMO (C-Suite) | anomalie sui KPI dell'intero ecosistema — "alimenta il report CMO" | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:282` | NO | INTRA → INTER (L0) · **VAGO** · MAI |
| 155 | AD6 Creative Analyst | ReasoningBank (10-MEMORY) | pattern di formato/performance dal loop creativo ads | non dichiarato | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:491` | NO | INTER · MAI |
| 156 | BR-QA (**G5 Brand consistency**) | committente | output incoerente col `brand_kit` del cliente → **block + richiesta di brief corretto al committente** | coerenza col brand_kit dichiarato, non solo col Mandato DE | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:592` | NO | INTER · MAI (**terzo canale di ritorno scritto dell'Impero**, dopo CF-R6-REWORK #117 e CF `on_reject` #104) |
| 157 | MKT-Conductor | `marketing/handoffs/log` | ogni richiesta/risposta cross-ecosistema registrata; G4 fallito → rework specifico o rinegoziazione loggata | "Handoff acceptance rate": % consegne accettate senza rework | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:591`, `:600`, `:646` | NO (namespace mai creato) | INTER · MAI (**e' il registro dei passaggi, e non contiene niente**) |
| 158 | BR2 Brand Voice Architect (WF-BRAND-EVOLUTION) | Max (via ADR) | proposta evolutiva del brand DE | *"solo Max modifica Art.2"*; proposta come ADR-bozza, non si attua senza approvazione (Art.5.3 Mandato) | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:324` | NO | INTRA → LX · MAI |
| 159 | tutti i reparti L2 di 04-MKT | committenti esterni | *"ogni reparto ha almeno un handoff reale entro M5"* | nessuno oltre la scadenza M5 | `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:676` | NO | INTER · **VAGO** (promessa di data, non passaggio) · MAI |
