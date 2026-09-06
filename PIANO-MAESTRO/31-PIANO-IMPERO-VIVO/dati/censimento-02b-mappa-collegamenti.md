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

### FONTE 5a — `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md`

MB si autodefinisce **"cliente interno degli ecosistemi trasversali"** (`:45`) e *"non duplica capacita'
che esistono altrove"*: e' l'ecosistema che ORDINA piu' di tutti e produce quasi nulla in proprio
(`:186-188`: *"i passi 5-9 sono eseguiti da Content-Factory su ordine `WF-YT-VIDEO-ORDER`;
Multi-Business valida la consegna e possiede i gate"*). Contratto Bus dichiarato:
`{from, to, payload, acceptance_criteria}` (`:64`) — schema n.2 del censimento gemello, l'unico
riusato tale e quale. Verifica su disco: `ls company/05-multibusiness` → **inesistente**; nessun
ordine, nessun `brand_kit`. **Se CF non riceve l'ordine, MB non produce nulla: e' l'ecosistema piu'
dipendente dell'Impero.** Nota di merito: MB e' l'unico che nomina un agente il cui unico mestiere
e' **verificare cio' che rientra** (`mb-yt-handoff-validator`, `:128`) e uno che **ordina e non
produce** (`:89`).

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 160 | 05-MULTI-BUSINESS | 03-CONTENT-FACTORY | produzione video YouTube (script→voiceover→visual→thumbnail), manoscritti libri, creative store — payload `{brand_kit, formato, quantita', deadline, spec_tecniche, riferimenti_stile}` | asset conformi a spec (durata, risoluzione, formato file), brand_kit rispettato, consegna entro deadline | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:68` | NO | INTER · MAI (**il piu' pesante dell'Impero: senza di lui MB non ha prodotto**) |
| 161 | 05-MULTI-BUSINESS | 04-MARKETING | copy listing KDP, descrizioni SEO, titoli, copy ads e-comm, hook script — payload `{brand_kit, icp, formato_copy, framework: APSOC, vincoli_piattaforma}` | copy passa Copy/APSOC Guild gate + brand gate | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:69` | NO | INTER · MAI (specchio di #126) |
| 162 | 05-MULTI-BUSINESS | 08-INTELLIGENCE | ricerca niche, analisi competitor, trend, ingestione Empire Studio dei canali riferimento — `{dominio, domande_di_ricerca, output_atteso: dossier_wiki}` | dossier in wiki `sources/` o `synthesis/` con **dati verificabili e fonti** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:70` | NO | INTER · MAI |
| 163 | 05-MULTI-BUSINESS | 06-PLATFORM | tooling: CLI KDP, integrazioni YouTube Data API, store setup — `{spec_funzionale, API_target, vincoli}` | **tool passa `verify.sh` Empire** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:71` | NO | INTER · MAI |
| 164 | 05-MULTI-BUSINESS | 09-OPERATIONS | esecuzione swarm mass-production, scheduling pubblicazioni, budget — `{workflow_id, parallelismo, budget_max, schedule}` | dry-run ok, **Cost-Sentinel verde** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:72` | NO | INTER · MAI |
| 165 | 05-MULTI-BUSINESS | 07-FORGE | nuove skill/team (es. `yt-seo-optimizer`) — `{gap_capacita', spec_skill}` | skill conforme a progressive disclosure (kernel ≤500 righe) | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:73` | NO | INTER · MAI |
| 166 | 03-CONTENT-FACTORY | 05-MB (`mb-yt-handoff-validator`) | **consegna di ritorno**: script + audio + video + thumbnail contro il contratto `WF-YT-VIDEO-ORDER` | **4 gate bloccanti in serie**: #1 Script (hook 15s, similarita' < soglia vs ultimi 20 script), #2 Audio (-14 LUFS, durata ±5%), #3 Visual (≥1080p, thumbnail leggibile a 120px), #4 SEO — gate rosso = pacchetto rispedito al team con report di failure in ReasoningBank | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:197`, `:206-210`, `:212-213` | NO | INTER · MAI (**il ritorno meglio specificato di tutto l'Impero: 4 gate misurabili e un rimando scritto**) |
| 167 | 05-MB (`WF-PUB-BOOK-ORDER`) | 03-CONTENT-FACTORY | ordine manoscritto `{brand_kit, formato: manoscritto_md + image_prompts.yaml, quantita': 1, spec: n_capitoli/parole/stile}` | GATE LAYOUT a valle su `book_final.pdf` 6x9 + `qa_report.md` verde | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:249-253` | NO | INTER · MAI |
| 168 | 05-MB (`WF-PUB-COVER`) | 03-CONTENT-FACTORY | spec cover (trim+spine calcolati dal n. pagine reale) | **Cover Gate**: dimensioni trim+bleed corrette per il n. pagine reale; testo dorso leggibile; conformita' template KDP | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:255-256`, `:288` | NO | INTER · MAI |
| 169 | 05-MB (`WF-PUB-LISTING`) | 04-MARKETING | richiesta copy listing KDP (APSOC), 7 keyword, categorie, pricing | **Listing Gate**: no keyword stuffing (policy KDP); **descrizione APSOC approvata da Marketing**; 7 keyword + 3 categorie coerenti con la niche | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:257-258`, `:289` | NO | INTER · MAI |
| 170 | 05-MB (`WF-YT-ANALYTICS`) | calendario + memoria `mb/yt/patterns` | metriche 48h/7gg/28gg → report retention/CTR + raccomandazioni che **retro-alimentano i brief** | *"la cadenza non supera mai la capacita' dei gate"* | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:199`, `:427` | NO | INTRA · MAI (**ciclo chiuso progettato, mai chiuso**) |
| 171 | 05-MB (`WF-PUB-MONITOR`) | fase 1 (niche research) | BSR, recensioni, royalty → "feedback a (1)" | non dichiarato | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:260` | NO | INTRA · **VAGO** · MAI |
| 172 | 05-MB / MB-PUB (skill `book-to-skill`) | 02-INFO-BUSINESS | libro pubblicato → skill/asset riusabile: **cross-sell libro → corso** ("ponte", trigger post-pubblicazione da definire) | trigger post-pubblicazione **non ancora definito** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:275`, `:319` | NO | INTER · **VAGO** · MAI (gemello inverso di #59/#80) |
| 173 | `Lanco ebook/` (ebook venduto fuori KDP) | 02-INFO-BUSINESS | confine di proprieta' del prodotto: "ebook venduto fuori KDP = Info-Business" | **decisione di confine mai presa** ("Ingestione wiki + decisione confine") | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:311` | NO | INTER · **VAGO** · MAI |
| 174 | 05-MB (`caroselli/`, Carousel Factory) | 03-CONTENT-FACTORY | caroselli/promo social: *"MB e' solo committente"* — da migrare a CF e ordinare via contratto | non dichiarato | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:316`, `:273` | NO | INTER · MAI |
| 175 | 05-MB (`WF-ECOM-PRODUCT`) | 08-INTELLIGENCE | ricerca prodotto e-commerce "eseguita da Intelligence su ordine MB", output = dossier wiki | dossier WF-ECOM-PRODUCT + decisione `mb-conductor` + **ok umano** per passare a E1 | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:293-296` | NO | INTER · MAI |
| 176 | 05-MB (E2 store MVP) | 04-MARKETING + 03-CONTENT-FACTORY | ≤10 listing: "copy → Marketing, visual → Content-Factory" | E1 chiusa, budget approvato | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:297` | NO | INTER · MAI |
| 177 | 05-MB (`KDP - prodottti digitali/Leanding Page`) | 06-PLATFORM | landing KDP gestita "da Platform per conto di MB-PUB" | audit + eventuale `empire-style` | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:310` | NO | INTER · **VAGO** · MAI |
| 178 | 05-MB (F-MB2 scaffolding) | 07-FORGE | "ordini alla Forge per le skill P1" | skill P1 consegnate e conformi; **zero orfani tra gli asset §7** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:410` | NO | INTER · MAI |
| 179 | `Strategia Ebook _ Kpd - pr. TikTock.pdf` | 08-INTELLIGENCE → MB-PUB | conoscenza di lancio/promo da ingerire e riusare in `WF-PUB-LISTING` | ingestione Empire Studio / wiki | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md:312`, `:276` | NO | INTER · **VAGO** · MAI |

### FONTE 5b — `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md`

La V2 dichiara la tabella handoff **"invariata dal v1"** (`:95`) e aggiunge una sola colonna: il
**reparto MB emittente** (`:98`). E' l'unico dossier dell'Impero che dica non solo "chi ordina a chi"
ma **quale reparto interno firma l'ordine**. Il guadagno vero della V2 sta altrove: introduce il
**ciclo di rifiuto** (`WF-YT-ORDER-QA`, `:228`) e il **tracciamento dello stato ordine**
(`mb-yt-order-tracker`, `:221`) — cioe' gli unici due pezzi dell'Impero che sappiano dire *dove sta
adesso* un passaggio di consegne. Righe qui sotto: solo cio' che il v1 non diceva.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 180 | MB / YT-Produzione-Ordini + PUB-Produzione-Ordini + ECOM-Store | 03-CONTENT-FACTORY | stesso ordine del v1 (#160) ma con **reparto emittente nominato** | invariati | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:100` | NO | INTER · MAI |
| 181 | MB / YT-Ottimizzazione + PUB-Packaging + ECOM-Crescita | 04-MARKETING | copy listing/SEO/titoli/ads con reparto emittente nominato | *"copy passa Copy/APSOC Guild gate + brand gate (**04-MARKETING-V2 §7.1 G1/G2**)"* — **unico rimando incrociato a un gate di un altro dossier in tutto l'Impero** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:101` | NO | INTER · MAI |
| 182 | MB / YT-Strategia + PUB-Ricerca + ECOM-Ricerca | 08-INTELLIGENCE | ricerca niche/competitor/trend con reparto emittente nominato | dossier in wiki con dati verificabili e fonti | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:102` | NO | INTER · MAI |
| 183 | MB / YT-Pubblicazione + PUB-Pubblicazione | 06-PLATFORM | tooling con reparto emittente nominato | tool passa `verify.sh` Empire | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:103` | NO | INTER · MAI |
| 184 | MB / MB-Portfolio | 09-OPERATIONS | swarm mass-production, scheduling, budget — emesso dal **nuovo layer di portafoglio** | dry-run ok, Cost-Sentinel verde | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:104` | NO | INTER · MAI |
| 185 | MB / `mb-conductor` + MB-Portfolio | 07-FORGE | skill nuove (`yt-seo-optimizer`, `mb-portfolio-registry`, `order-handoff-validator` P2) | kernel ≤500 righe; **skill P0 consegnate e conformi**, zero orfani | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:105`, `:648`, `:759` | NO | INTER · MAI |
| 186 | 03-CONTENT-FACTORY (consegna non conforme) | MB (`WF-YT-ORDER-QA`) | **ciclo di rifiuto/rework**: la consegna CF che non passa la validazione **ri-apre l'ordine con feedback specifico invece di rilanciare da zero** | consegna corretta entro **2 cicli di rework**, poi escalation a `mb-yt-order-lead` | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:228`, `:681` | NO | INTER · MAI (**il quarto e ultimo canale di ritorno scritto dell'Impero — e l'unico INTER con contatore di tentativi**) |
| 187 | 03-CONTENT-FACTORY | `mb-yt-asset-receiver` → YT-Ottimizzazione | asset consegnati ricevuti, archiviati e **instradati** al reparto successivo | non dichiarato | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:219` | NO | INTER → INTRA · MAI (**unico "instradatore di consegne" nominato in tutto l'Impero**) |
| 188 | `mb-yt-order-tracker` | `MB-Portfolio` (cost-attribution) | stato di ogni ordine in corso: `in coda` / `in produzione` / `consegnato` / `rifiutato` | non dichiarato | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:221` | NO | INTRA · MAI (**l'unico organo dell'Impero che saprebbe dire dove sta un passaggio adesso**) |
| 189 | 03-CONTENT-FACTORY | `mb-pub-order-handoff-validator` | manoscritto + immagini: validazione **prima** dell'ingresso in book-factory (layout) | rispetto del brief verificato prima del passaggio a layout | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:312`, `:322` | NO | INTER · MAI |
| 190 | `mb-pub-res-lead` (PUB-Ricerca) | 04-MARKETING + 08-INTELLIGENCE | "smista le richieste di niche verso Marketing/Intelligence per copy e dati" | non dichiarato | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:288` | NO | INTER · **VAGO** · MAI |
| 191 | `mb-pub-pkg-lead` (PUB-Packaging) | 04-MARKETING | "smista il copy a Marketing (APSOC)" per cover + listing | non dichiarato oltre il Listing Gate | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:333` | NO | INTER · **VAGO** · MAI |
| 192 | `WF-YT-COMPETITOR-INGEST` | 08-INTELLIGENCE (Empire Studio) | ordine/aggiornamento dell'ingestione dei canali di riferimento (prima esecuzione = F-MB1, poi ri-scan periodico) | **2+ dossier in wiki `sources/`; pattern salvati in `mb/yt/patterns`** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:177`, `:206` | NO | INTER · MAI |
| 193 | `mb-port-report-analyst` | `mb-conductor` → C-Suite | report mensile revenue/costo per istanza | `WF-MB-PORTFOLIO-REVIEW`: decisione tieni/kill/rilancia **con dati da `WF-YT-ANALYTICS`/`WF-PUB-MONITOR`, mai a opinione** | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:450`, `:458` | NO | INTRA → INTER (L0) · MAI |
| 194 | `mb-port-launch-gate` | `mb-conductor` / swarm | autorizzazione ad aprire una nuova istanza (canale/libro/store) | **≥10 video con ≥80% gate verdi al primo colpo** (F-MB5) + niche/angolo non duplicato nel registro `brand_kit` | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:449`, `:459`, `:718` | NO | INTRA · MAI |
| 195 | `mb-qa-sentinel-liaison` | Quality/Brand/Cost Sentinel (Backbone) | escalation da gate rossi ricorrenti | non dichiarato | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:468` | NO | INTER (Backbone) · **VAGO** · MAI |
| 196 | `mb-port-qa` (Portfolio Isolation QA) | ogni istanza MB | verifica che ogni istanza legga **solo** il proprio namespace + i pattern condivisi — **blocca** su cross-contaminazione | zero cross-contaminazione di memoria fra istanze | `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md:446` | NO | INTRA · MAI |

### FONTE 6 — `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md`

E' il dossier che dichiara il principio da cui dipende TUTTA la mappa: *"Nessun ecosistema business
tocca direttamente codice, creazione di agenti, memoria o runtime: **lo chiede ai core via handoff
contract**"* (`:11`). Cioe': i 5 ecosistemi che incassano non possono muoversi senza 4 passaggi di
consegne verso i core. La **Matrice di dipendenza Core × Business** (`:501-506`) e' l'unica tabella
20-celle dell'Impero in cui ogni cella e' un passaggio dichiarato, e nessuna cella e' vuota.
L'invariante di chiusura e' esplicito: *"i 4 core non generano revenue diretta — il loro KPI ultimo
e' il KPI degli altri 5"* (`:535`). Verifica su disco: nessuna delle 20 celle ha un contratto, un file
o un log; `company/Ecosistemi/06-PLATFORM|07-FORGE|08-INTELLIGENCE|09-OPERATIONS/` contengono solo
`ECOSISTEMA.md`/`BACKBONE.md`/cartelle vuote di scaffolding.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 197 | 01-AGENCY | 06-PLATFORM | `{brief cliente, brand_kit, icp, scope, deadline}` | sito/implementazione consegnata + **codice in custodia cliente** | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:47` | NO | INTER · MAI (gemello di #10 `HC-AG-PL-01`) |
| 198 | 04-MARKETING | 06-PLATFORM | copy APSOC validato | *"PLATFORM non scrive copy: **lo monta**"* — confine non valicabile | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:48` | NO | INTER · MAI |
| 199 | 03-CONTENT-FACTORY | 06-PLATFORM | asset visual/video | embed + ottimizzazione performance (Lighthouse ≥90 sui siti consegnati, `:129`) | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:49` | NO | INTER · MAI |
| 200 | 06-PLATFORM | 09-OPERATIONS | **ogni build/deploy emette evento** `{commessa, costo, durata, esito}` per cost attribution | evento emesso a ogni build, senza eccezioni | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:50` | NO | INTER · MAI (**se esistesse, sarebbe il primo euro misurato dell'Impero**) |
| 201 | 06-PLATFORM | 08-INTELLIGENCE | post-mortem tecnici, ADR d'architettura | → wiki `tools/` + ReasoningBank | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:51` | NO | INTER · MAI |
| 202 | 07-FORGE | 06-PLATFORM | nuovi agenti/skill engineering (es. skill `site-*`) | **consegnati E installati** | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:52` | NO | INTER · MAI |
| 203 | 08-INTELLIGENCE | 06-PLATFORM | ricerca tecnica (stack, librerie, competitor tecnici) | **prima di ogni scelta d'architettura** (vincolo temporale, non solo di contenuto) | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:53` | NO | INTER · MAI |
| 204 | QUALSIASI ecosistema | 07-FORGE | `{capability mancante, contesto, KPI attesi, budget}` | artefatto consegnato + **eval report**; tempo richiesta→consegna ≤2 giorni per skill semplice | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:163`, `:242` | NO | INTER (9→1) · MAI |
| 205 | 08-INTELLIGENCE | 07-FORGE | materiale raw ingerito (Empire Studio) + pattern ReasoningBank | input per forgiare/arricchire skill | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:164`, `:282` | NO | INTER · MAI (**dichiarato da entrambe le parti**) |
| 206 | 07-FORGE | 08-INTELLIGENCE | ogni artefatto creato → pagina wiki `tools/` + log | *"enrichment skill esistenti passa per Memory Empire"* | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:165` | NO | INTER · MAI |
| 207 | 07-FORGE | 09-OPERATIONS | ogni nuovo agente dichiara tier modello + costo stimato | **budget guard pre-approvazione**; registrazione nel cost model | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:166`, `:399` | NO | INTER · MAI (**dichiarato da entrambe le parti**) |
| 208 | 07-FORGE | Backbone Identity-HR | assunzione/ritiro agenti | **registro unico aggiornato a ogni forgiatura** | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:167` | NO | INTER (Backbone) · MAI |
| 209 | LX / Board | 07-FORGE | mandato per ecosistemi interi nuovi (es. F9+ E-commerce) | `ecosystem-scaffold` (F5) | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:168`, `:531` | NO | INTER · MAI |
| 210 | QUALSIASI | 08-INTELLIGENCE | `{link/video/file/domanda}` | ingestione integrale **oppure** context pack `{pagine wiki, memorie, pattern, fonti}` | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:282` | NO | INTER (9→1) · MAI |
| 211 | 08-INTELLIGENCE | 07-FORGE | conoscenza distillata MKD-ready + pattern ReasoningBank sui fallimenti | MKD-ready | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:283` | NO | INTER · MAI |
| 212 | 08-INTELLIGENCE | 04-MARKETING + 01-AGENCY | ricerca cliente (`customer-research`), profili competitor (`competitor-profiling`), trend | non dichiarato | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:284` | NO | INTER · **VAGO** · MAI (gemello di #13, #25, #128, #145) |
| 213 | 08-INTELLIGENCE | 03-CONTENT-FACTORY + 05-MULTI-BUSINESS | analisi canali di riferimento (F7: ingestione 2 canali YouTube via Empire Studio) | non dichiarato | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:285` | NO | INTER · MAI |
| 214 | 09-OPERATIONS | 08-INTELLIGENCE | log run, metriche, costi | **distillati in pattern e pagine wiki** (post-mortem) | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:286`, `:398` | NO | INTER · MAI (**dichiarato da entrambe le parti**) |
| 215 | 08-INTELLIGENCE | Backbone BRAIN | *"e' l'ecosistema che OPERA il Brain del backbone (wiki + AgentDB + ReasoningBank)"* | nessuno | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:287` | NO | INTER (Backbone) · **VAGO** (rapporto di proprieta', non passaggio) |
| 216 | QUALSIASI | 09-OPERATIONS | `{workflow, parametri, budget_max, schedule}` | run eseguita/schedulata + report `{esito, costo, durata}` | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:397` | NO | INTER (9→1) · MAI |
| 217 | 09-OPERATIONS | QUALSIASI | **alert**: budget all'80%, run fallita, drift di costo, processo zombie | nessuno | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:398` | NO | INTER (1→9) · MAI (**unico broadcast dell'Impero: uno a tutti**) |
| 218 | 09-OPERATIONS | Board (L0) | report costi settimanale per ecosistema + dashboard | cadenza settimanale | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:400` | NO | INTER · MAI |
| 219 | 09-OPERATIONS | 06-PLATFORM | richieste tooling (script scheduling, dashboard) — *"OPERATIONS le usa, PLATFORM le scrive"* | non dichiarato | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:402` | NO | INTER · MAI |
| 220 | 06-PLATFORM | AGENCY / INFO-BUS / CF / MKT / MB | **matrice di dipendenza, riga 1**: siti clienti + code custody · sales page + piattaforma corsi · tooling pubblicazione · landing/funnel tecnici · SaaS/App + automazioni KDP/YT | nessuno per cella | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:503` | NO | INTER ×5 · **VAGO** (matrice, non contratti) · MAI |
| 221 | 07-FORGE | AGENCY / INFO-BUS / CF / MKT / MB | **riga 2**: team delivery + skill preventivi · team lancio + skill prodotto · team per formato/canale · skill copy/ads nuove · **interi rami nuovi (YT, Ecomm)** | nessuno per cella | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:504` | NO | INTER ×5 · **VAGO** · MAI |
| 222 | 08-INTELLIGENCE | AGENCY / INFO-BUS / CF / MKT / MB | **riga 3**: ricerca lead/ICP + dossier competitor · ricerca audience + materiale corsi · ingestione fonti + trend · customer insight + pattern copy vincenti · analisi canali YT + nicchie KDP | nessuno per cella | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:505` | NO | INTER ×5 · **VAGO** · MAI |
| 223 | 09-OPERATIONS | AGENCY / INFO-BUS / CF / MKT / MB | **riga 4**: run outreach schedulate + costi per commessa · costi lancio + scheduling email · mass-production swarm + render queue · budget ads guard + attribution · batch libri/video + cron | nessuno per cella | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:506` | NO | INTER ×5 · **VAGO** · MAI |
| 224 | 08-INTELLIGENCE | 07-FORGE → 06-PLATFORM | **catena di dipendenza interna ai core**: contesto/materia prima → skill/agenti/team → build | ordine di costruzione vincolato: INTELLIGENCE prima, OPERATIONS subito dopo (*"il cost guard deve esistere PRIMA di moltiplicare gli agenti"*), FORGE terza, PLATFORM in parallelo | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:511-520` | NO | INTER · MAI |
| 225 | TUTTI (9 ecosistemi) | 09-OPERATIONS | eventi costo/run da tutti — chiusura del cerchio della catena core | nessuno | `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:514-517` | NO | INTER (9→1) · MAI |

### FONTE 6a — `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md`

Regola gemella di quella di MARKETING, ma sul codice: *"nessun ecosistema business scrive o modifica
codice di produzione in autonomia. Puo' fornire brief e contenuti (copy, asset), ma **l'implementazione
e il deploy vivono in PLATFORM**"* (`:91-93`). Contratto d'ingresso
`{committente, formato, brand_kit, scope, deadline, budget_max}` (`:361`) — **ottavo schema**; risposta
`{deliverable, url_staging_prod, verify_report, security_report, costo_evento, workflow_eseguito}`
(`:377`), l'unico contratto di ritorno dell'Impero che porti con se' **il costo dell'operazione**.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 226 | 01-AGENCY | 06a-PLATFORM | sito cliente completo, implementazione tecnica, **code custody a fine commessa** | G-SEC + G-QA + G-BRAND + G-DEPLOY verdi; lead time brief→deploy ≤10 giorni lavorativi; Lighthouse ≥90 | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:83`, `:186`, `:476-478` | NO | INTER · MAI (**e' il pezzo tecnico del Gate Delivery #22: senza custody il cliente non e' libero**) |
| 227 | 02-INFO-BUSINESS | 06a-PLATFORM | sales page tecnica, piattaforma corsi/membership | WF-SITE-FULL o WF-LANDING-RAPIDA; gate G-QA | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:84` | NO | INTER · MAI (gemello di #55/#74 `HC-PL-IB-01`) |
| 228 | 03-CONTENT-FACTORY | 06a-PLATFORM | tooling di pubblicazione; embed e ottimizzazione performance di asset visual/video | non dichiarato oltre T-site-qa | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:85` | NO | INTER · MAI (gemello di #98) |
| 229 | 04-MARKETING (L2.6) | 06a-PLATFORM | implementazione tecnica di landing/funnel disegnati da Conversion Architecture | brief tecnico approvato (cfr. #148) | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:86`, `:564` | NO | INTER · MAI (**dichiarato da entrambe le parti**) |
| 230 | 05-MULTI-BUSINESS | 06a-PLATFORM | MVP SaaS/App, automazioni KDP/YT (book-factory automation) | `plt-product-qa` verde; **PRD quality score ≥75 rispettato a build** | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:87`, `:228` | NO | INTER · MAI |
| 231 | 06b-FORGE | 06a-PLATFORM | installazione di nuovi agenti/skill engineering consegnati | reparto destinatario scelto per competenza della skill | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:88` | NO | INTER · MAI |
| 232 | 06c-INTELLIGENCE | 06a-PLATFORM | ricerca tecnica **"in ingresso, non su richiesta"** | *"L2.1/L2.2 consultano PRIMA di ogni scelta stack"* | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:89` | NO | INTER · MAI (**unico passaggio dell'Impero dichiarato non richiesto ma dovuto**) |
| 233 | 06b-FORGE (`frg-prd-architect`) | 06a-PLATFORM (`plt-prd-intake`) | PRD → tradotto in task di build | PRD quality score ≥75 | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:216`, `:228` | NO | INTER · MAI (**unico passaggio con agente ricevente dedicato su entrambi i lati**) |
| 234 | 06a-PLATFORM | committente (qualsiasi) | risposta `{deliverable, url_staging_prod, verify_report, security_report, **costo_evento**, workflow_eseguito}` | `WF-EMPIRE-VERIFY-PIPELINE` verde prima di ogni handoff | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:295`, `:377` | NO | INTER · MAI (**unico ritorno che porta il costo con se': e' il pezzo mancante di #200**) |
| 235 | `plt-director` | `platform/handoffs/log` | registro richieste/risposte cross-ecosistema | non dichiarato | `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md:519` | NO (namespace mai creato) | INTER · MAI |

### FONTE 6b — `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md`

Terza regola-cardine dello stesso tipo: *"nessun ecosistema crea agenti, skill o team in autonomia.
Ogni capability nuova passa dalla FORGE"* (`:98-99`). Contratto `{ecosistema, gap, target, kpi_attesi,
budget}` (`:350`), risposta `{artefatto_consegnato, eval_report, registro_hr_aggiornato,
workflow_eseguito}` (`:370`). FORGE e' l'unico ecosistema che dichiara di **servire tutti e nove** gli
altri piu' il Board (`:74-82`). Il dossier ammette da solo il buco piu' grave dell'Impero:
*"~248 agenti progettati, 19 censiti"* nel registro Identity-HR (`:547`) — cioe' il registro dei
destinatari dei passaggi e' disallineato dal reale del 92%.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 236 | QUALSIASI ecosistema | 06b-FORGE | `capability-request`: skill, agente, team o workflow mancante | **artefatto senza eval = non consegnabile (G-EVAL non bypassabile)**; ≤2 giorni per skill semplice | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:89`, `:119`, `:463`, `:472` | NO | INTER (9→1) · MAI |
| 237 | 06a-PLATFORM | 06b-FORGE | nuove skill/agenti engineering (prima skill prevista: `empire-verify`) | skill consegnata con **eval verde** (milestone F1) | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:90`, `:530` | NO | INTER · MAI (**dichiarato da entrambe le parti**) |
| 238 | 04-MARKETING | 06b-FORGE | skill copy/ads nuove: `empire-brand-gate`, `copy-request-router`, `brand-strategy-gate` | `contradiction-analyzer` verde + eval ≥ soglia | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:91`, `:167`, `:561` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #138) |
| 239 | 01-AGENCY + 02-INFO-BUSINESS | 06b-FORGE | team delivery / team lancio completi | `frg-org-designer` approva la gerarchia; **`frg-handoff-designer` verifica ogni contratto I/O** | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:92`, `:195`, `:206` | NO | INTER · MAI (**il progettista dei contratti dell'Impero e' un agente mai creato**) |
| 240 | 05-MULTI-BUSINESS | 06b-FORGE | interi rami nuovi (YT, E-comm) | **mandato Board richiesto**; `frg-ecosystem-qa` verifica conformita' §0 piano V2 | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:93`, `:266`, `:272` | NO | INTER · MAI |
| 241 | 06c-INTELLIGENCE | 06b-FORGE | materiale raw ingerito + pattern ReasoningBank **"in ingresso"** → `content-forge` lo trasforma | **MKD intermedio SEMPRE presente (mai saltato); mai riassumere, sempre espandere** | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:94`, `:239`, `:531` | NO | INTER · MAI |
| 242 | LX/Board | 06b-FORGE | mandato per ecosistemi interi o revisione dello standard organizzativo | mandato Board **formalmente chiuso** a fine WF-ECOSYSTEM-NEW | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:95`, `:272` | NO | INTER · MAI |
| 243 | 06b-FORGE | 06c-INTELLIGENCE | ogni artefatto creato → pagina wiki `tools/` | consegna al committente **e** pagina wiki, insieme | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:80`, `:392` | NO | INTER · MAI |
| 244 | 06b-FORGE | 06d-OPERATIONS | dichiarazione tier modello + costo stimato per ogni nuovo agente | **budget guard pre-approvazione** | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:81` | NO | INTER · MAI |
| 245 | 06b-FORGE (`frg-hr-registrar`) | Backbone Identity-HR | censimento agenti a ogni forgiatura | **G-REGISTRY: artefatto non consegnabile finche' il registro non e' coerente (100% agenti censiti)** — oggi 19 censiti su ~248 progettati | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:465`, `:547` | NO | INTER (Backbone) · MAI (**il gate che, se acceso oggi, bloccherebbe ogni consegna dell'Impero**) |
| 246 | 06b-FORGE (`WF-SKILL-RETIRE`) | tutti gli ecosistemi committenti | **notifica di deprecazione** di una skill ritirata | skill deprecata segnalata a tutti i committenti; **nessun riferimento orfano** | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:170` | NO | INTER (1→9) · MAI (**secondo broadcast dell'Impero, dopo l'alert di OPERATIONS #217**) |
| 247 | `frg-orchestration-builder` | committente | script eseguibili reali (`.py`/`.ps1`) e non solo markdown | *"**vietato consegnare un ruolo in un markdown**"* (standard §0 piano V2) | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:232` | NO | INTER · MAI (**la regola che l'intero censimento dimostra violata**) |
| 248 | `frg-chief` | `forge/handoffs/log` + Board | coda richieste, arbitrato priorita' fra committenti, escalation | violazioni dei pattern non negoziabili (#1,#6,#7,#8) → escalation a `frg-chief` (WF-PATTERN-AUDIT) | `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:313`, `:323`, `:516` | NO | INTER · MAI |

### FONTE 6c — `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md`

Quarta regola-cardine dello stesso tipo: *"nessun ecosistema ingerisce contenuto esterno o scrive
pagine wiki 'a mano' fuori standard"* (`:119-122`). E' l'ecosistema che dovrebbe **precedere** tutti
gli altri: *"ogni ecosistema, prima di un task non banale, ottiene un context pack"* (`:56`), con
**copertura ≥95% dei task non banali** (`:270`) — cioe' 9 passaggi in entrata prima di ogni lavoro
serio dell'Impero. Contratto `{committente, tipo_richiesta, target, urgenza, deadline}` (`:127-133`),
risposta `{esito, pagine_wiki_prodotte, memorie_collegate, pattern_usati, fonti, workflow_eseguito}`
(`:137-139`). Due regole di rifiuto proprie: *"pattern-query senza corrispondenza → **restituisce
errore, non inventa la fonte**"* (`:143`) e *"context-pack senza committente → non produce output
generico: **chiede il committente**"* (`:144-145`).

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 249 | 01-AGENCY | 06c-INTELLIGENCE | ricerca lead/ICP, dossier competitor, **ricerca cliente pre-preventivo** | R-QA: fonti tracciate, zero dati inventati, **dossier senza fonti = non si consegna** | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:109`, `:146`, `:298` | NO | INTER · MAI (gemello di #13/#25) |
| 250 | 02-INFO-BUSINESS | 06c-INTELLIGENCE | ricerca audience, materiale corso ingerito (video/canale di riferimento) | G-INTEGRAL (archiviazione integrale, mai riassunti) | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:110` | NO | INTER · MAI (gemello di #54/#73) |
| 251 | 03-CONTENT-FACTORY | 06c-INTELLIGENCE | ingestione fonti (canali, articoli), trend contenuti | G-INTEGRAL + fonti tracciate | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:111` | NO | INTER · MAI (gemello di #100) |
| 252 | 04-MARKETING | 06c-INTELLIGENCE | customer insight, **pattern copy vincenti per ICP** (lettura di `intelligence/learning/patterns/{ecosistema}`) | *"`pattern-query` senza corrispondenza → **restituisce errore, non inventa la fonte**"* | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:112`, `:143` | NO | INTER · MAI (gemello di #145) |
| 253 | 05-MULTI-BUSINESS | 06c-INTELLIGENCE | analisi canali YouTube di riferimento, nicchie KDP | 2+ dossier in wiki `sources/` (cfr. #192) | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:113` | NO | INTER · MAI (**dichiarato da entrambe le parti**) |
| 254 | 06a-PLATFORM | 06c-INTELLIGENCE | ricerca tecnica (stack, librerie, competitor tecnici) **prima** delle scelte d'architettura | fonti tracciate | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:114` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #232) |
| 255 | 06b-FORGE | 06c-INTELLIGENCE | `knowledge-pull` + `pattern-query`: materiale MKD-ready e pattern sui fallimenti | MKD-ready; pattern esistente o errore | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:115` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #241) |
| 256 | 06d-OPERATIONS | 06c-INTELLIGENCE | log run, metriche, costi da distillare (`pattern-distill` → WF-REASONINGBANK) | *"riceve log/metriche, **restituisce pattern distillati**"* — l'unico scambio bidirezionale dichiarato in una riga sola | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:102`, `:116` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #214) |
| 257 | QUALSIASI ecosistema | 06c-INTELLIGENCE (SECOND-BRAIN / SB3) | **context pack pre-task** `{pagine wiki, memorie, pattern, fonti}` | pack consegnato entro SLA; **copertura ≥95% dei task non banali**; senza `committente` non produce output generico | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:56`, `:117`, `:144-145`, `:270`, `:450` | NO | INTER (9→1) · MAI (**il passaggio piu' a monte di tutto l'Impero: dovrebbe precedere ogni task non banale, e non e' mai avvenuto**) |
| 258 | qualsiasi ecosistema (bozza di pagina) | SECOND-BRAIN | *"un ecosistema puo' proporre una bozza di pagina, ma **la pubblicazione formale** (frontmatter, cross-link, log) passa da qui"* | **G-STRUCT + G-LOG + G-LINK**: blocca pagine senza cross-link o senza log | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:121-122`, `:264`, `:273` | NO | INTER · MAI |
| 259 | ING-LEAD (team liaison) | Empire Studio (conductor) | richiesta di ingestione video/canale — *"il team liaison e' il **SOLO** punto di contatto; zero modifiche interne"* | ING-QA verifica **G-INTEGRAL**: contenuto integrale, mai un riassunto — **blocca la chiusura del ticket** se fallisce; ticket con SLA tracciato | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:177`, `:189`, `:194`, `:200-201`, `:479` | NO | INTER (verso motore esistente) · MAI |
| 260 | MEM-LEAD (team liaison) | Memory Empire v3 | richieste DE instradate al router + enrichment di skill esistenti | **G-SAFE-ENRICH**: backup + diff + verifica non-regressione **tutti e tre obbligatori**, mai bypassabile, prima di toccare una skill attiva | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:221`, `:224`, `:234`, `:480` | NO | INTER (verso motore esistente) · MAI (**il gate piu' severo dell'Impero**) |
| 261 | R4 (`WF-MARKET-SYNTHESIS`) | committente o Board | dossier di sintesi da dati grezzi Empire Studio + ricerche R1-R3 | R-QA verifica **tracciabilita' delle fonti prima della consegna** | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:308` | NO | INTER · MAI |
| 262 | `INT-OBSERVER` | Board | KPI d'ecosistema: copertura context pack, ingestioni completate, **divergenze wiki/AgentDB**, pattern riusati | "alimenta il report Board" | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:354` | NO | INTER · **VAGO** · MAI |
| 263 | 06d-OPERATIONS | 06c-INTELLIGENCE | runtime swarm per l'ingestione, cost guard, scheduling di `WF-WIKI-GARDEN`/`WF-TREND` — "DIPENDE DA" | non dichiarato | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:88-89` | NO | INTER · **VAGO** · MAI |
| 264 | 06b-FORGE | 06c-INTELLIGENCE | evoluzione di Empire Studio / Memory Empire + forgiatura delle 3 skill proprie (`context-pack`, `wiki-sync-guard`, `ingest-router`) | skill forgiate **con PRD + architettura** (standard §8 piano V2) | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:73`, `:89-90` | NO | INTER · MAI |
| 265 | 06c-INTELLIGENCE | ecosistema 10-MEMORY | **confine dichiarato**: memoria operativa della holding (checkpoint/ADR/stato) *"non qui"* | out of scope esplicito | `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md:77-78` | NO | INTER · **VAGO** (confine, non passaggio) |

### FONTE 6d — `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md`

E' l'unico ecosistema che si dichiara **obbligatorio e bidirezionale con tutti**: *"e' l'unico
ecosistema con cui OGNI altro ha un handoff obbligatorio bidirezionale (**ogni run passa da qui e ogni
run genera un evento di ritorno**)"* (`:78-81`). Quinta e ultima regola-cardine: *"nessun workflow
gira in produzione reale senza dry-run con stima costi (G-DRYRUN) e senza budget dichiarato
(G-BUDGET). **Nessuna eccezione, nemmeno per run interne di OPERATIONS su se stesso**"* (`:101-103`).
Contratto `{ecosistema_richiedente, workflow, parametri, budget_max, schedule, dry_run}` (`:107-116`);
risposta `{esito, costo_reale, durata, tier_usato, evento_ledger_id, alert_generati}` (`:118-119`).
Tre rifiuti scritti: senza `budget_max` **COST GUARD rifiuta prima che RUNTIME spawni** (`:123`);
`dry_run: false` senza conferma umana **bloccata** (`:124-125`); run schedulata senza `rollback_plan`
**rifiutata** (`:126`). **Questo e' l'ecosistema che, se acceso, farebbe misurare all'Impero il primo
euro** — ed e' il tema del gemello B-043 (*"DE non misura un solo euro"*).

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 266 | QUALSIASI ecosistema | 06d-OPERATIONS (RUNTIME) | esecuzione run (swarm, batch, singola) entro budget dichiarato | **G-DRYRUN + G-BUDGET**; senza `budget_max` la run e' rifiutata prima dello spawn | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:86`, `:101-103`, `:123` | NO | INTER (9→1) · MAI |
| 267 | 01-AGENCY | 06d-OPERATIONS (SCHEDULING) | scheduling run outreach giornaliere (`avvia-email`/`ig`/`parallel`) | run schedulata senza `rollback_plan` → **rifiutata** (G-RUNBOOK) | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:87`, `:126` | NO | INTER · MAI (gemello di #15/#49 `HC-AG-OP-01`) |
| 268 | 02-INFO-BUSINESS | 06d-OPERATIONS | scheduling email lancio + costi lancio | budget approvato prima del go (cfr. #90 Gate Dry-Run + Costi) | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:88` | NO | INTER · MAI (gemello di #60/#76/#81) |
| 269 | 03-CONTENT-FACTORY | 06d-OPERATIONS | mass-production swarm, render queue (`swarm --parallel N --budget N`) | G-BUDGET | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:89` | NO | INTER · MAI (gemello di #102) |
| 270 | 04-MARKETING | 06d-OPERATIONS (COST GUARD) | budget ads guard, **cost attribution per campagna** | `dry_run: false` senza conferma umana esplicita → bloccata (Art.4.3 Mandato) | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:90`, `:124-125` | NO | INTER · MAI (gemello di #131) |
| 271 | 05-MULTI-BUSINESS | 06d-OPERATIONS | batch produzione libri/video, cron pubblicazione | dry-run ok, Cost-Sentinel verde | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:91` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #164/#184) |
| 272 | 06a-PLATFORM | 06d-OPERATIONS | **evento `{commessa, costo, durata, esito}` per ogni build/deploy** | WF-ATTRIBUTION | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:92` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #200/#234) |
| 273 | 06b-FORGE | 06d-OPERATIONS | registrazione nel cost model di ogni nuovo agente `{agente, tier, costo_stimato}` | WF-TIER-ROUTING | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:93` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #207/#244) |
| 274 | 06c-INTELLIGENCE | 06d-OPERATIONS | log/metriche da distillare + scheduling di `WF-WIKI-GARDEN`/`WF-TREND` | MONITORING (log) + SCHEDULING (cron) | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:94` | NO | INTER · MAI (**dichiarato da entrambe le parti**, cfr. #256/#263) |
| 275 | 06d-OPERATIONS (WF-WATCH) | TUTTI | **alert push**: budget all'80%, run fallita, drift di costo, processo zombie | evento push, nessun criterio di accettazione dichiarato | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:95` | NO | INTER (1→9) · MAI (terzo broadcast, cfr. #217/#246) |
| 276 | 06d-OPERATIONS (WF-BOARD-REPORT) | Board (L0) | report costi settimanale per ecosistema + dashboard | cadenza settimanale | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:96` | NO | INTER · MAI (gemello di #218) |
| 277 | 06d-OPERATIONS | committente (qualsiasi) | **ritorno obbligatorio di ogni run**: `{esito, costo_reale, durata, tier_usato, evento_ledger_id, alert_generati}` | *"ogni run genera un evento di ritorno"*, senza eccezioni | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:78-81`, `:118-119` | NO | INTER (1→9) · MAI (**il ritorno che manca all'Impero intero: nessuna run ha mai reso un `costo_reale`**) |
| 278 | 06a-PLATFORM | 06d-OPERATIONS | script di scheduling/dashboard: *"PLATFORM li scrive, OPERATIONS li usa"* — "DIPENDE DA" | non dichiarato | `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:75-76` | NO | INTER · **VAGO** · MAI (gemello di #219) |

### FONTE 7 — `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md`

Non e' un ecosistema: e' **la strada su cui tutti i passaggi di questa mappa dovrebbero viaggiare**.
Dichiara *"nessuna azione isolata, ogni passaggio di lavoro tra agenti, team, reparti ed ecosistemi
e' un messaggio tracciato e append-only"* (`:55-57`). Il contratto e' il **nono schema** censito
(`:71-83`) — ed e' l'unico dell'Impero con un campo `status` a sei valori
(`pending|accepted|in_progress|done|rejected|escalated`), cioe' l'unico che sappia raccontare la
**vita** di un passaggio e non solo la sua partenza. Tre regole di rifiuto: (a) handoff senza
`acceptance_criteria` misurabili e' **INVALIDO** e il coordinator lo rifiuta; (b) `status=rejected`
DEVE includere note correttive; (c) **2 reject consecutivi → escalation automatica** al reparto
superiore via gbus (`:85-87`). Il gemello `dati/censimento-02-collegamenti.md` ha gia' accertato che
**il Bus non ha mai trasportato niente**: qui si registra solo cosa avrebbe dovuto trasportare.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 279 | qualsiasi team | qualsiasi team **dentro** lo stesso ecosistema | livello **INTRA** via `company/orchestrator/bus.sh` → `company/runtime/bus/<eco>/messages.jsonl` | handoff con `acceptance_criteria` misurabili, altrimenti INVALIDO | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:59-61`, `:85` | script esiste, **traffico zero** (cfr. `dati/censimento-02-collegamenti.md`) | INTRA · MAI |
| 280 | ecosistema / BOARD / EMPIRE | ecosistema / BOARD / EMPIRE | livello **INTER** via `gbus.sh` → `company/runtime/group-bus/messages.jsonl`; mittenti e destinatari **validati contro Identity-HR** | destinatario esistente nel registro HR (oggi 19 agenti censiti su ~248: la validazione rifiuterebbe quasi tutti) | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:62-64` | script esiste, **traffico zero** | INTER · MAI |
| 281 | mittente di handoff "pesante" | destinatario | payload multi-file (copy, video, report) come file in `company/Ecosistemi/<ECO>/handoffs/{inbox,outbox,archive}/H-<id>.json` — *"il jsonl trasporta il riferimento, la cartella trasporta il contenuto"* | schema JSON validato da `validate-handoff.sh` | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:65-68`, `:95-96` | **NO** — su disco esistono solo `01-agency/A1..A4/handoffs` e `Backbone/Bus/handoffs`, nessun `inbox/outbox/archive` | INTER · MAI |
| 282 | coordinator ricevente | mittente | **rifiuto**: `status=rejected` con note correttive obbligatorie | 2 reject consecutivi → `type: escalation` automatica al reparto superiore via gbus | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:85-87`, `:413` | NO | INTRA+INTER · MAI (**il canale di ritorno universale dell'Impero — quello che rende inutili i quattro canali locali #104/#117/#156/#186 se acceso**) |
| 283 | ogni gate/run/handoff | `company/metrics/runs.jsonl` | eventi standard `run_done`, `gate_passed`, `gate_failed`, `handoff_rejected`, `swarm_done`, `lead_generated`, `content_published`, **`sale_closed`**, `evolution` — ognuno con `{eco, reparto, team, agente, brand_kit, costo}` | KPI Backbone: **backlog bus (messaggi pending >24h) = 0**; **handoff invalidi (senza acceptance criteria) = 0%** | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:219-222`, `:495-496` | NO | INTER · MAI (**`sale_closed` e' l'evento che collegherebbe la mappa a un incasso: non e' mai stato emesso**) |
| 284 | metriche | `cost/by-{agent,team,eco,brand}.json` → dashboard | cost-attribution multi-tenant: *"quanto costa servire il cliente X? quanto costa il canale YT Y?"* | rigenerati da `costs.sh` | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:223-226` | NO | INTER · MAI |
| 285 | metriche | `neural_train` / `autopilot_predict` / `evolve` → 07-FORGE | pattern, previsione colli di bottiglia, **creazione/ritiro agenti automatico** | fallback senza MCP: i jsonl locali bastano | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:229-232` | NO | INTER · MAI |
| 286 | Sentinelle (Quality) | team + Quality-Guild → CTO → Board | **escalation a soglia**: pass_rate <90% su 10 run · **2 reject consecutivi stesso team** · trend qualita' in calo per 3 cicli → blocco consegna + richiesta rework con note | soglie numeriche esplicite | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:413` | NO | INTER · MAI |
| 287 | skill `empire-handoff` (P0 #3) | Bus | *"crea/valida/instrada handoff conformi al contract §1.1"* (wrapper di `bus.sh`/`gbus.sh`) | conformita' al contract §1.1 | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:370` | **skill mai forgiata** (solo `gbus.sh` come script) | INTER · MAI (**e' l'attrezzo con cui l'Impero dovrebbe fare i passaggi, e non esiste**) |
| 288 | B2.3 (fase di build) | primi workflow reali | *"wiring nei primi workflow reali (outreach AGENCY, F4)"* — il primo aggancio previsto del Bus a lavoro vero | handoff di test che **attraversa 2 ecosistemi e torna `done`** (gate B2) | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:94-96`, `:512` | NO | INTER · MAI (**il gate B2 non e' mai stato superato: nessun handoff e' mai tornato `done`**) |
| 289 | Board / Governance | tutti gli ecosistemi | topologia di lavoro assegnata per ecosistema (AGENCY hierarchical, INFO-BUSINESS **ring** — *"ogni fase passa il testimone"*, CF hierarchical+mesh, MARKETING **star** — *"ogni output copy passa dal hub"*, MB mesh, PLATFORM hierarchical, FORGE star, INTELLIGENCE mesh, OPERATIONS mesh) | nessuno | `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:249-257` | NO | INTER · **VAGO** (regola di forma, non passaggio) · MAI |

### FONTE 8 — `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md`

E' il **secondo** ecosistema a dichiararsi obbligatorio con tutti (dopo OPERATIONS): *"MEMORY serve
TUTTI gli ecosistemi ed e' servito da tutti: e' l'unico ecosistema con cui **ogni** team ha un
handoff obbligatorio bidirezionale"* (`:37-40`). I suoi 4 contratti hanno un prefisso proprio
(`HC-ME-*`) e sono i soli codici contratto dell'Impero **effettivamente in uso operativo**: la regola
memory-first di `CLAUDE.md` e' viva, i checkpoint si scrivono (questo censimento stesso ne e' prova).
Restano pero' non-passaggi nel senso di questa mappa: sono uomo→file, non ecosistema→ecosistema.
L'enforcement e' l'unico dell'Impero che sia **cablato e non solo scritto** (hook SessionStart,
`CLAUDE.md`, Memory-Sentinel, `verify-empire.sh`, `:170-186`). E la regola piu' pesante:
*"l'acceptance criteria di OGNI team L3/L4 della holding include 'CP scritto in Memory' — **un handoff
senza CP-id e' invalido per contratto**"* (`:180-182`) — cioe' TUTTI i 288 passaggi censiti finora
sarebbero invalidi, perche' nessuno porta un CP-id.

| # | DA | A | COSA PASSA | CRITERIO DI ACCETTAZIONE | FONTE | CONTRATTO ESISTE? | MAI PERCORSO? |
|---|---|---|---|---|---|---|---|
| 290 | qualsiasi team (pre-task) | 10-MEMORY | `HC-ME-PRE`: `{task_id, ecosistema, descrizione, keywords}` | **context-pack restituito**: stato + CP/ADR/piani rilevanti + pattern AgentDB; se MEMORY segnala contraddizione con un ADR attivo → **STOP + escalation Board** | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:44`, `:155` | codice usato, **file di contratto no** | INTER (10→1) · **parzialmente percorso** (regola memory-first attiva via hook, mai come handoff fra ecosistemi) |
| 291 | qualsiasi team (post-task) | 10-MEMORY | `HC-ME-POST`: `{task_id, esito, output_paths, lezioni, **costi**}` | CP scritto + INDEX aggiornato + STATO aggiornato; **il team committente riceve conferma CP-id — senza CP-id il task NON e' chiuso** | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:45`, `:105`, `:158-160` | codice usato, contratto no | INTER (10→1) · **parzialmente percorso** (i CP esistono; il campo `costi` non e' mai stato compilato da nessuno) |
| 292 | Board / qualsiasi team | 10-MEMORY | `HC-ME-ADR`: `{decisione, contesto, alternative, conseguenze}` | ADR-NNN registrato + **contradiction-check vs ADR attivi passato**; conflitto → escalation hive-mind Board | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:46`, `:162-164` | codice usato, contratto no | INTER · **parzialmente percorso** (gli ADR esistono e sono numerati fino a ADR-023) |
| 293 | Board / 07-FORGE | 10-MEMORY | `HC-ME-PLAN`: nuovo piano o revisione | versionato in `plans/` + STATO aggiornato | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:47` | codice usato, contratto no | INTER · **parzialmente percorso** |
| 294 | 10-MEMORY | ReasoningBank (Backbone BRAIN) | **flusso continuo**: fallimenti distillati in pattern | pattern nel namespace AgentDB `patterns` | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:48` | NO | INTER · MAI (**nessun pattern e' mai stato depositato: e' lo stesso buco di #28, #89, #137, #155, #285**) |
| 295 | 10-MEMORY | wiki (06c-INTELLIGENCE) | **flusso continuo**: eventi rilevanti per gli umani → entry in `wiki/log.md` | non dichiarato oltre la entry | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:49` | NO | INTER · **parzialmente percorso** (il `log.md` viene aggiornato, ma a mano dalla regola WIKI-FIRST, non da MEMORY come ecosistema) |
| 296 | Memory-Sentinel | escalation | scansione periodica: task/sessioni **senza CP** → escalation | `verify-empire.sh`: INDEX aggiornato, **0 CP orfani**, STATO coerente col filesystem, ADR senza conflitti | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:183-186`, `:232` | NO (sentinella mai costruita) | INTER · MAI |
| 297 | 10-MEMORY | ogni team L3/L4 della holding | **CP-id come requisito di validita' di ogni handoff**: *"un handoff senza CP-id e' invalido per contratto"* (G-ME2) | CP-id presente in ogni handoff | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:180-182`, `:232` | NO | INTER (10→9) · MAI (**la regola che invalida per contratto tutti gli altri 296 passaggi di questa mappa**) |
| 298 | Memory Empire skill (`~/.claude/skills/memory-empire/`) | 10-MEMORY | **rapporto di partenariato**: resta motore di INTELLIGENCE per la conoscenza esterna; MEMORY ne riusa i pattern (handoff JSON, backup→append→log→rollback) | non dichiarato | `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:194` | NO | INTER · **VAGO** · MAI |
