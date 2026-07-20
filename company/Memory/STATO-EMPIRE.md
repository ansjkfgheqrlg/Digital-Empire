# STATO EMPIRE -- aggiornato 2026-07-20 (ordine Max: PIVOT AREUS — Empire Desk riparte dalla piattaforma Aureus)

## ⚠️ COORDINAMENTO 2026-07-20 — MENTALITÀ BRUTALE SOCIAL OPERATING SYSTEM (Arena)
**BUILD APERTA — owner esclusivo di questo ciclo: Arena Agent.** Obiettivo: chiudere il gap S4 del dossier 16 con una base operativa API-first per `mentalita.brutale`: autorizzazione Meta, produzione→QA→scheduler→publish→insights→learning, memoria progetto e skill operativa. ARCHITETTURA + Chief-Forge + FORGE sono attivati come catena di governo; gli asset esistenti vengono wrappati (ADR-003), non riscritti.

**Scope di scrittura riservato durante il ciclo:**
- `Page IG - Mentalità Brutale/OPERATING-SYSTEM/` e `.claude/skills/mentalita-brutale-operator/` (nuovi);
- configurazioni con password in chiaro dentro `SKILL & Agenti/Workflow pubblicazione automatica/` **solo per bonifica sicurezza** (sostituzione con env, nessun rewrite runtime);
- registri `company/REGISTRO-IMPRESA.md`, `company/skills-map.yaml`, Memory e wiki (solo conductor a chiusura).

**Fuori scope / non toccare:** `EmpireDesk/` e soprattutto `EmpireDesk/platform/`/UI (ownership Max), Outreach, PreventivoForge, runtime carousel-factory esistente. Nessuna pubblicazione LIVE e nessuna spesa: prima dry-run, token-health e gate. Il ciclo si chiude con CP, gate/test, rimozione di questo blocco e push.

## 🚨🚨🚨 ORDINE MAX 2026-07-20 — PIVOT: EMPIRE DESK = AUREUS AGENCY OS TRASFORMATA IN APP (leggere dossier 17 §0-bis)
**Max ha bocciato la UI launcher v0.1/v2** (struttura sbagliata: questa è l'app GESTIONALE del team,
non un derivato PreventivoForge). Base nuova = piattaforma di Max **"Aureus Agency OS"** (repo
`Gestionale-Team---Areus-Piattaforma-By-Digital-Empire`), **importata in `EmpireDesk/platform/`**
(build verificata, anteprima testata in finestra app — Claude/Max, CP-20260720-001).
**Regole: grafica INTOCCABILE (pixel-perfect) · prima l'app, poi le funzioni (fase 2) · Max = SOLO
grafica/UI/UX (via Claude) · GAEL = TUTTO il resto.**

**▶️ GAEL — riprendi da qui (dettagli dossier 17 §0-bis):**
- **G1 (per primo):** `app.py` serve `platform/dist/` come root (stessa origin delle API `/api/*`
  esistenti) + finestra chrome-app → l'app che si apre È Aureus. Prima: `npm install` in platform/
  (node_modules gitignorato) + `npm run build`. Vecchia `ui/index.html` → `/legacy` (fallback temporaneo).
- **G2:** build exe con dist inclusa + test doppio click.
- **G3:** B1-B4 restano (loader moduli/scheduler/notify/taskboard) = solo backend. Moduli A1-A3 di Max
  restano validi (route+dati); i loro panel_html = provvisori (UI la rifà Max in stile Aureus, fase 2).
- **NON toccare il contenuto di `platform/`** (= grafica = Max), salvo config di build concordate.

**▶️ MAX (via Claude):** U0 ✅ (import+build+anteprima) · **U0b ✅ offline-capable (2026-07-20,
`9e86349b`)**: Tailwind runtime + font Inter vendorizzati in `platform/public/` (stesso motore/stessi
woff2 = zero differenze grafiche; l'app ora gira senza internet — verificato live) · U1 in fase 2 =
operatività dentro Aureus nel suo linguaggio grafico (Automations → flussi reali, pannelli
metrics/revenue/licenze). GAEL: dopo il pull ricordati `npm install` + `npm run build` in platform/
(node_modules e dist NON sono nel repo).
**Piano vincolante e completo: `PIANO-MAESTRO/17-EMPIRE-DESK-APP.md` §5 (appena scritto, leggerlo TUTTO).**
Focus totale sull'app. Massimo impegno. Regola d'oro: **MAI toccare i file dell'altro half** (lezione PreventivoForge).

**🔄 AGGIORNAMENTO OWNERSHIP (ordine Max 2026-07-19 sera): LA UI/UX È DI MAX, NON DI GAEL.**
**Gael NON tocca più `ui/index.html`** (grafica/design/estetica = Max via Claude). Gael = tutto il resto.
Dossier 17 §5 aggiornato. Se hai modifiche locali non pushate a `ui/index.html`: pusha ORA e poi stop.

**▶️ GAEL — Half B «Core & Runtime» (owner: app.py · build_exe.bat · empiredesk.spec — NON più ui/):**
- ✅ **B0 fix Caroselli** pushato (`2f885014`) — completa il resto di B0 se manca: selftest 8/8
  verificato + build exe + test doppio click + CP. **v0.1 CHIUSA.**
- **B1 (SBLOCCA integrazione moduli) — SOLO LATO PYTHON:** loader `EmpireDesk/modules/` (contratto
  §5.3) + route `POST /api/modules` → `[{id, tile, panel_html}]` + metodi in `_WebApi` (pywebview)
  + selftest esteso ai moduli. **La parte UI dello switcher NON la fai tu: la fa Max in index.html.**
  Confine = solo quell'API JSON, zero file condivisi.
- **B2** scheduler run programmate · **B3** notifiche fine-run · **B4** taskboard live. Dettagli §5.1.

**✅ MAX — Half A: A1+A2+A3 SCRITTI E TESTATI (2026-07-19 sera, selftest 3/3 PASS):**
- ✅ **A1** `EmpireDesk/modules/metrics.py` — 6/6 fonti reali (probe live: LinkedIn 6 righe oggi,
  458 email in coda, 52 PDF preventivi ultimi 7gg — numeri VERI letti dai file, mai inventati).
- ✅ **A2** `EmpireDesk/modules/revenue.py` + `state/revenue.json` — pipeline 7 slot (Max compila
  nomi/stati), route `revenue/aggiorna` per aggiornare un campo alla volta.
- ✅ **A3** `EmpireDesk/modules/licenze.py` — wrap di gestione-licenze.py (verificati: script,
  licenze.config.json, gh CLI). Sospendi con conferma UI. Zero secrets nell'app.
- ⬜ **A4** fliki: parte quando S5 pronto.
- Tutti a contratto §5.3 (`MODULE{id,tile,routes,panel_html}` + `selftest()` probe-only).
  **GAEL: al tuo B1 (loader modules/) questi 3 si accendono da soli — NON toccarli (§5.4 regola 1).**

**Sequenza: B0 (oggi) → B1 → parallelo pieno A1-A4 ∥ B2-B4. Ogni task chiuso = commit+push+questo blocco aggiornato.**
*(Nota per Gael: se una sessione Claude ti dice "questa task non esiste" → git pull fallito per rete
(errore schannel visto 2 volte oggi) — RIPETI il pull finché passa, l'ordine è QUI e nel dossier 17.)*

*(Nota: un secondo blocco-divisione scritto da una sessione Max parallela citava «§6 dossier 17» —
numerazione vecchia. Rimosso: vale il blocco qui sopra; nel dossier la divisione è la **§5**.
Stesso contenuto, nessun task cambiato. Ordine del giorno Gael dopo B1: task revenue dossier 16.)*

## ✅ GAEL — RISOLTA COLLISIONE UI + PRESO ATTO OWNERSHIP (2026-07-19 sera, CP-20260719-008)
**Al pull di questo blocco ho scoperto che Max aveva già ridisegnato `ui/index.html` in parallelo**
(nav-tab "Empire Premium") con lo stesso obiettivo del mio switcher pannelli di sotto (CP-007),
ma un contratto di rete diverso. Risolto merge manuale (8 blocchi): **tenuto il design di Max**,
`app.py` riallineato al SUO contratto esatto (`POST /api/modules` → `{"modules":[{id,tile,
panel_html}]}` — non più `/api/panels`/chiave `"html"`, mia scelta precedente ora abbandonata).
**Confermo: da ora non tocco più `ui/index.html`** (ownership UI = Max, come scritto qui sopra).
Il blocco sotto (CP-007) descrive lo switcher UI che avevo costruito PRIMA di vedere questo
aggiornamento — la parte Python (loader/validazione/dispatcher) resta valida e attuale, la parte
UI descritta lì (bottone "Pannelli", CSS `.htext`/`.hactions`) è STATA SOSTITUITA dal design di
Max — dettaglio in `EmpireDesk/REGISTRO-ERRORI.md` EDE-8 e `CP-20260719-008.md`.

## ⚠️ GAEL — B1 COSTRUITO (loader moduli), NON ESEGUITO (2026-07-19 sera, CP-20260719-007) — RIPRESA QUI
**Seam `EmpireDesk/modules/` fatto:** `_load_modules()` scandisce `modules/*.py`, importa in
isolamento (un modulo rotto si segnala e si salta, MAI fa cadere l'app), monta `routes`/`tile`/
`panel_html` di ogni modulo. **Validazione schema tile aggiunta** (`_validate_module_tile`) prima
di accettarla — altrimenti una tile-modulo malformata avrebbe fatto KeyError su TUTTE le tile
(bug trovato in autorevisione, mai lanciato). Switcher "Pannelli" in UI (tab per modulo) + CSS
per le classi che i pannelli di Max già usano (`.panel .hint .btn .inp .log-pane`) — senza,
sarebbero apparsi senza stile. **Verificati i 3 moduli di Max (metrics/revenue/licenze): rispettano
il contratto §5.3 esattamente.** Fix grafico proattivo: i 2 bottoni header erano posizionati a
mano (`right:Npx`) → rischio sovrapposizione → convertito a `display:flex` (zero rischio).
**🛑 NON ESEGUITO QUI:** stesso blocco di CP-20260719-004/006 — questa sessione non ha Python/Node
installati, solo revisione statica riga per riga. **RIPRESA (macchina reale):**
1. `git pull` (prendi B1 + i 2 fix EDE-6/7).
2. `cd EmpireDesk && python app.py --selftest` → atteso: 8 tile core + selftest metrics/revenue/
   licenze (~11 righe), tutte OK salvo eventuale EDE-A1 residuo in licenze.py (Max, non mio).
3. `python app.py` → aprire, cliccare "Pannelli", verificare a occhio i 3 tab (stile coerente,
   bottoni funzionanti) + selftest via UI.
4. Se verde: build exe (`build_exe.bat`) + test doppio click + CP di chiusura B0+B1 + comunica a
   Max che può integrare (già può scrivere A4 fliki in parallelo, si aggancia da solo).
Dettaglio completo: `company/Memory/checkpoints/CP-20260719-007.md`.

## ⚠️ GAEL — EMPIRE DESK: P1-P3 FATTI, P4 BLOCCATO (2026-07-19, CP-20260719-004) — RIPRESA QUI
**Cartella nuova `EmpireDesk/` (root del repo).** P1 (shell 3-motori + 8 tile UI) e P2-P3
(TileManager generico: subprocess reale + poll log-live + selftest, copre TUTTE le 8 tile con
lo stesso meccanismo) FATTI. Motore GUI: **Chrome-app → pywebview → Tkinter** (non pywebview-primo
come diceva il dossier alla lettera — applicato subito il pattern evoluto post CP-20260715-001,
per non ripetere il bug WebView2-silenzioso).
**3 bug reali trovati e corretti in revisione statica del codice** (io/conductor, riga per riga —
vedi `EmpireDesk/REGISTRO-ERRORI.md` per il dettaglio):
1. tile Python usavano `sys.executable` risolto all'import → da `.exe` congelato è `EmpireDesk.exe`
   stesso, non un interprete Python (avrebbe rilanciato l'app). Fix: risoluzione a runtime.
2. `.bat` lanciato senza `cmd.exe /c` rischia `WinError 193` su Windows. Fix: sempre `cmd.exe /c`.
3. `AVVIA-EMAIL-LIVE.bat`/`_avvia_ig.bat` finiscono con `pause` → senza `stdin` chiuso il
   subprocess resta appeso per sempre (tile bloccata su "in corso" a vita). Fix: `stdin=DEVNULL`.
**Trovato ma NON toccato (EDE-2, fuori scope):** `run_daily.bat` (LinkedIn) + i 2 bat sopra hanno
path hardcoded di UN'ALTRA macchina (`c:\Users\Utente\...`) — su questo PC potrebbero fallire al
lancio. Non è un bug di EmpireDesk: sono script del runtime Outreach ATTIVO (ADR-003, wrap non
riscrittura) — segnalato, va sistemato nei bat originali (path relativi), non qui.
**🛑 BLOCCO reale per chiudere P4 oggi:** l'ambiente di esecuzione di questa sessione Claude Code
**non ha Python né Node.js installati** (solo stub Microsoft Store 0-byte) → non è stato possibile
eseguire `python app.py --selftest` né buildare l'exe con PyInstaller qui. Codice verificato SOLO
staticamente. **RIPRESA (chiunque continui, Max o Gael, su una macchina con Python+Node+Chrome —
il PC dove gira già PreventivoForge):**
1. `cd EmpireDesk && python app.py --selftest` → deve dare 8/8 PASS (o correggere quel che manca).
2. `python app.py` (dev) → verificare a occhio la GUI (nessun errore grafico, palette slate+argento+
   arancio `#fb4604`, le 8 tile, il pannello log, il bottone Selftest in UI).
3. Provare a lanciare 1-2 tile vere (es. STATO Empire = sola lettura, sicura; PreventivoForge)
   per vedere il log live e l'exit code.
4. `EmpireDesk/build_exe.bat` → `dist/EmpireDesk/EmpireDesk.exe`, testare doppio-click.
5. CP finale + aggiorna questo file + wiki/log + push.
Dettaglio completo: `company/Memory/checkpoints/CP-20260719-004.md`.
*(Nota: questo checkpoint era numerato -002 in locale, ma quel numero era già usato su GitHub da ADR-008 — rinumerato -004 in fase di risoluzione conflitto sync 2026-07-19 21:xx.)*

## ✅ GAEL — V2-2 LOTTO 3 COMPLETATO (2026-07-19, CP-20260719-001)
**Chiuso PRIMA di vedere l'ordine EMPIRE DESK qui sopra (era già a buon punto); ora si passa
a EMPIRE DESK come da ordine Max. RIPRESA V2-2 Lotto 4 (dopo Empire Desk): `07-BACKBONE-
RUFLO-SKILLS-V2.md`, `08-ROADMAP-FASI-V2.md`, `09-ECOSISTEMA-MEMORY-V2.md` — poi V2-2 chiuso
(9/9 ecosistemi + 2/2 organi) e si apre V2-3 (build organo MAXIMILIAN).**

Scritti 5 dossier via swarm 3 agenti paralleli (interrotto una volta a metà per chiusura
sessione, ripreso con successo via SendMessage sul transcript — nessun file perso, nessuna
duplicazione: nessuno dei 5 era ancora stato scritto al momento dell'interruzione):
- `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS-V2.md` (803 righe, 12 reparti incl. nuovo
  `MB-Portfolio` di governo cross-istanza, 72 agenti)
- `PIANO-MAESTRO/06a-ECOSISTEMA-PLATFORM-V2.md` (570 righe, 5 reparti — WEB-ENGINEERING
  mega-reparto, 45 agenti)
- `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md` (567 righe, 5 reparti, 40 agenti — nota meta:
  FORGE si auto-descrive con lo stesso standard che impone agli altri)
- `PIANO-MAESTRO/06c-ECOSISTEMA-INTELLIGENCE-V2.md` (646 righe, 5 reparti, 35 agenti — Empire
  Studio/Memory Empire wrappati come liaison, MAI duplicati nel roster, ADR-003 rispettato)
- `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md` (638 righe, 5 reparti, 37 agenti — 65% Haiku,
  coerente col principio v1 "ecosistema più Haiku-heavy della holding")
**Decisione architetturale presa (chiudeva un pending del roadmap):** split del v1
`06-ECOSISTEMI-CORE.md` in 4 file `06a/06b/06c/06d` (non rinumerati 06/07/08/09 per evitare
collisione con `07-BACKBONE-RUFLO-SKILLS.md`/`08-ROADMAP-FASI.md`/`09-ECOSISTEMA-MEMORY.md`
già esistenti). v1 intatto come riferimento (ADR-003).
**Gate automatico:** 0 stub/TODO/placeholder, 13/13 sezioni (0-12) presenti su tutti e 5 i
file, cross-link coerenti tra i 4 core + verso 00/04/11-PIANO-MAESTRO. **Review indipendente**
(manuale, 5-bis Maximilian non ancora attivo/V2-3): letti a campione 05 e 06b, qualità alta,
coerenti col formato di 04-MARKETING-V2. 1 refuso minore corretto (path duplicato in un
blockquote). `V2-INDEX.md` aggiornato (8/9 ecosistemi blueprint, ~477 agenti progettati totali).

---

## ✅ MAX — Skill ufficiale `master-app-builder` installata (2026-07-19, CP-20260719-005)
Installata in `.claude/skills/master-app-builder/SKILL.md` la skill richiesta da Max per costruire app in modo metodico. Basata sulla bozza più ricca trovata già nella root (`master-app-builder-skill/`, v2.1), non sul v2.0 incollato in chat. Aggiunta **Fase 0.0 — pattern mining**: prima di progettare, cerca precedenti riusabili nel repo (PreventivoForge/Novacar in `Clienti/Prof Autocad/preventivo-forge/`, EmpireDesk) invece di reinventare stack/pattern — coerente con ADR-003. Tie-in di governance con `06a-PLATFORM/L2.2 PRODUCT-ENGINEERING` (uso) e `06b-FORGE/L2.1 SKILL-WORKS` (proprietà skill), letti dai dossier V2 reali, non inventati. Comando: `/master-app-builder`. Verificata presente nell'elenco skill disponibili di Claude Code dopo l'installazione. **NON tocca** l'ordine EMPIRE DESK su Gael qui sopra: task parallelo di Max, nessun conflitto di area. Trovata anche `master-build-architecture/` (root, untracked) con contenuto in inglese non verificabile (path Linux, GitHub esterni, PAT) da una sessione in un ambiente diverso da questo repo — NON usata come fonte, solo segnalata. Dettaglio: `company/Memory/checkpoints/CP-20260719-005.md`.
*(Nota: questo checkpoint era numerato -003 in locale, ma quel numero era già usato su GitHub dalla divisione metà/metà Empire Desk — rinumerato -005 in fase di risoluzione conflitto sync.)*

## ⚠️ PROBLEMA RISOLTO — Conflitto di sync + collisione numerazione checkpoint (2026-07-19, sessione Max)
Il repo era diviso "ahead 1, behind 26" da GitHub (rebase automatico fallito alle 20:37/20:43, vedi ex-`SYNC-CONFLICT.txt`, ora cancellato). Causa: due checkpoint locali (`CP-20260719-002` P1-P3 Empire Desk e `CP-20260719-003` skill master-app-builder) collidevano di numero con due checkpoint reali già su GitHub (`CP-20260719-002` ADR-008 e `CP-20260719-003` divisione metà/metà). Risolto rinumerando i due locali in `CP-20260719-004`/`CP-20260719-005` (contenuto conservato integralmente, nessun dato perso) e aggiornando tutti i riferimenti incrociati in `STATO-EMPIRE.md`/`INDEX.md`. Rebase completato e pushato. Lock file stantio `.git/empire-sync.lock` rimosso (età >5min, lo script lo avrebbe rimosso comunque al giro successivo).

---

# STATO EMPIRE -- aggiornato 2026-07-09 (Max — Empire Studio cat1-copywriting)

## 🛑 DIRETTIVE MAX ASSOLUTE (2026-07-03 — valgono sempre, leggere per prime)
1. **Ordini su Gael = assoluti.** Ogni compito che Max assegna a Gael (o direttiva su di lui) è LEGGE, non preferenza.
   → **ORDINE ATTIVO (aggiornato da Max 2026-07-05, CP-20260705-002): FINESTRA DI LIBERO ARBITRIO PER GAEL
   da lunedì 2026-07-06 a mercoledì 2026-07-08 COMPRESI.** In quei 3 giorni Gael decide LUI cosa fare:
   può continuare PreventivoForge, fare test, risolvere problemi, o proseguire l'Impero — piena libertà, con buonsenso.
   NON bloccarlo, NON reindirizzarlo. Restano valide le regole tecniche (ownership Half A/PDF di Max, schema congelato, coordinamento via questo file).
   ⏰ **OGGI 2026-07-05 la finestra NON è ancora attiva**: vale ancora l'ordine precedente (Impero V2-2/V2-3, bloccarlo su altro).
   ⏰ **Da giovedì 2026-07-09**: la finestra SCADE → torna l'ordine Impero, salvo nuovo ordine di Max.
2. **Aggiornare la versione ad OGNI messaggio, in automatico.** Ad ogni turno di Max E di Gael: leggere questo file + INDEX,
   fare `git pull` (monorepo), e allinearli all'ULTIMA versione dello stato — senza aspettare che lo chiedano. I due soci
   si sincronizzano SOLO via questo stato: mai far partire nessuno da una versione vecchia. Standard: tutto impeccabile.
3. **REGISTRO ERRORI = obbligatorio (Max 2026-07-05).** Ogni errore riscontrato in un progetto va scritto nel suo
   registro con causa + fix + regola per NON ripeterlo. PreventivoForge: `Clienti/Prof Autocad/preventivo-forge/REGISTRO-ERRORI.md`
   + `CHECKLIST-CONSEGNA.md`. **Prima di modificare/consegnare: leggerli. Mai commettere due volte lo stesso errore.**
   Gael: se testi PreventivoForge e trovi un errore, registralo lì. Prendi sempre l'ULTIMA build (git pull / zip rigenerato).


## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 9/29 COMPLETATO (2026-07-11, CP-20260711-001)
**RIPRESA DA: video 10/29 — `Ahp_6rHSOsU` ("Usa Google Docs come un copywriter PRO") — Stage 1+2 DONE (668s=11m08s, 334 frame 3-digit, 9 capitoli)**
Pipeline completata per IWCHN_mE2Vo: Stage 1-5 + Stage 7 + Memory Empire C-H. 25 KA P12-traced. 2 wiki pages create. 12 VP schermo documentati. Live 1h02min — Meta Ads Library tutorial + analisi ads brand italiani (Carisma Shoes, La Palestra boxing, melone costume, Corte CAB VANIGLIA).
- **Top KA**: Meta Ads Library "licenziato e fallire se non usi" · Video=conversione/Photo=retargeting · EU Transparency Reach 1770 Women 30-55 · Imprenditori italiani pieni di soldi · Chiarezza>Creativita "grande danno video incomprensibile"
- **Visual Passages**: VP-002 Ad Library Latvia homepage · VP-004 filter stack 98 results Laurea Online · VP-006 EU Transparency Women 30-55 excl. Toscana+Veneto · VP-011 costume regale supermercato · VP-012 Corte CAB VANIGLIA
- **Nuovi Concetti**: Source_Andrei_Pascu_Ads_Library_Live.md + Concept_Meta_Ads_Library_Competitor_Research.md
- **WATCH-001**: N_video=9, N_MemoryEmpire=9 → MATCH ✅

## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 8/29 COMPLETATO (2026-07-09, CP-20260709-008)
**COMPLETATO — vedi dettagli sotto**
Pipeline completata per lQMO0LdeI2c: Stage 1-5 + Stage 7 + Memory Empire C-H. 29 KA P12-traced. 2 wiki pages create. 6 VP schermo documentati. Live 44:55 — McFit+Dyson analizzati. Mercedes+DJI annunciati ma non analizzati.
- **Top KA**: Brand Famoso Rule · CPA leva €5→€50K/anno · Headline≠Nome Prodotto · CLV Red Bull · Slogan Vibes vs DR · Knowledge=Pricing Leva
- **Visual Passages**: VP-001 McFit Hero "SEMPLICEMENTE IN FORMA" · VP-002 Google "simply fit" · VP-003 McFit+ loyalty · VP-004 Dyson Airwrap headline errore · VP-005 trust badges · VP-006 v15s scarcity
- **Nuovi Concetti**: Source_Andrei_Pascu_Copywriter_Analizza_Live.md + Concept_CLV_Customer_Lifetime_Value.md
- **WATCH-001**: N_video=8, N_MemoryEmpire=8 → MATCH ✅

## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 7/29 COMPLETATO (2026-07-09, CP-20260709-007)
**RIPRESA DA: video 8/29 — `lQMO0LdeI2c` ("Copywriter Analyzes Copywriting — Live") — Stage 1+2 gia avviati**
Pipeline completata per iy13HC9M8z0: Stage 1-5 + Stage 7 + Memory Empire C-H. 26 KA P12-traced. 2 wiki pages create. 4 VP ChatGPT screen documentati.
- **Top KA**: "ottimo ma fa schifo" (paradosso GPT) · Show don't tell violato · 6 Gap AI (linguaggio/obiezioni/creativita/emotivita/strategico/ricerca) · GPT Ceiling Effect · AI-as-Floor Strategy
- **Visual Passages**: VP-001 overlay "COPYWRITER" · VP-002 warm-up ChatGPT · VP-003 Prompt 1 tazze output (3 frame) · VP-004 Prompt 2 specifico output
- **Nuovi Concetti**: Concept_AI_vs_Copywriter_Limiti_e_Usi.md (6 gap + 4 usi + checklist anti-GPT)
- **WATCH-001**: N_video=7, N_MemoryEmpire=7 → MATCH ✅

## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 6/29 COMPLETATO (2026-07-09, CP-20260709-006)
**RIPRESA DA: video 7/29 — `iy13HC9M8z0` ("I corrected ChatGPT's copywriting")**
Pipeline completata per 6WMkz5Q8g6g: Stage 1-5 + Stage 7 + Memory Empire C-H. 22 KA P12-traced. 2 wiki pages create.
- **Top KA**: Feature vs Benefit (formula+formula lista) · Ego dissolution nel copy · Specificità vivida lista scenari · Research sempre obbligatoria · Props fisici in video copy
- **Visual Passages**: VP-001 Beats headphones (frame-050/065/075) · VP-002 action cam GoPro-like (frame-100) · VP-003 end card brand
- **Nuovo Concept**: Concept_Feature_vs_Benefit_Copy.md (con checklist audit + formula operativa)
- **WATCH-001**: N_video=6, N_MemoryEmpire=6 → MATCH ✅

## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 5/29 COMPLETATO (2026-07-09, CP-20260709-005)
**RIPRESA DA: video 6/29 — `6WMkz5Q8g6g` (4 Tips for Writing Persuasive Texts & Copywriting)**
Pipeline completata per sTCwYnWmgcQ: Stage 1-5 + Stage 7 + Memory Empire C-H. 22 KA P12-traced. 2 wiki pages create.
- **Top KA**: "Tutto è copy" · Valore Anticipato · Pricing=valore-non-ore · Reputazione-online=copy · Metodo prodotti inventati
- **Nuovo Concept**: Concept_Valore_Anticipato_Freelance.md
- **WATCH-001**: N_video=5, N_MemoryEmpire=5 → MATCH ✅

## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 4/29 COMPLETATO (2026-07-09, CP-20260709-004)
**RIPRESA DA: video 5/29 — `sTCwYnWmgcQ` (How to Become a Copywriter with Zero Experience)**
Pipeline completata per t67-j2LiXgQ: Stage 1-5 + Stage 7 + Memory Empire C-H. 22 KA P12-traced. 2 wiki pages create.
- **Top KA**: Pain Amplification ("premi sulla ferita") · Urgency ("gli esseri umani rimandano") · Pain vs Pleasure (ogni acquisto) · Step 2 = spiega problema meglio del prospect · Meta-esempio live (corso €249→€690)
- **Visual Passages**: frame-079 (email Parola di Librai) · frame-085 (ad Torpado MTB direct response completo)
- **Nuovo Concept**: Concept_Pain_Amplification_Urgency_Copy.md
- **WATCH-001**: N_video=4, N_MemoryEmpire=4 → MATCH ✅

## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 3/29 COMPLETATO (2026-07-09, CP-20260709-003)
Pipeline completata per jgIgOPAnYNY: Stage 1-5 + Stage 7 + Memory Empire C-H. 24 KA P12-traced. 3 wiki pages create.
- **Top KA**: Formula APSOC (A/P/S/O/C) · "90% copywriter salta la ricerca" · YouTube reviews = voice of customer · briefing 7+1 elementi · "scrivi da ubriaco, rivedi da sobrio"
- **WATCH-001**: N_video=3, N_MemoryEmpire=3 → MATCH ✅

## ✅ MAX — Empire Studio: andrei-pascu-001 cat1-copywriting video 2/29 COMPLETATO (2026-07-05, CP-20260705-001)
Pipeline completata per qOK4WP82Bvo: Stage 1-5 + Stage 7 + Memory Empire C-H. 22 KA P12-traced. 3 wiki pages create.
- **WATCH-001**: N_video=2, N_MemoryEmpire=2 → MATCH ✅

## ✅ MAX — PreventivoForge: CONSEGNA A NOVACAR PRONTA (agg. 2026-07-05, ultimo su main `063cd27`)
**Consegna in 2 giorni. Pacchetto UNICO pronto: `Clienti/Prof Autocad/Consegna-Novacar/PreventivoForge-Novacar.zip` (120 MB, gitignorato).**
Dentro: exe + kill-switch (config Novacar con `license_url`) + riserva AI (.env con chiave Groq) + `LEGGIMI.txt`.
Guida consegna passo-passo: `Clienti/Prof Autocad/COME-CONSEGNARE-A-NOVACAR.md`.
- **Fix 2026-07-04 (testati):** (1) GUI mostra SOLO frasi pulite (milestone), non il log tecnico;
  (2) Chrome scraping NASCOSTO (off-screen, resta headful → Akamai ok);
  (3) **MULTI-LINK fino a 10** (`run_batch` in app.py: ogni link isolato, tutti i PDF in 1 cartella; textarea in GUI);
  (4) **retry Akamai 3x** in `scraper.py _fetch_live_cdp` (challenge intermittente → backoff);
  (5) **PROFILO CHROME PERSISTENTE = anti-blocco IP** (`browser-profile/` fisso riusato: passa Akamai 1 volta →
  riusa il cookie → niente re-challenge → IP pulito con 30+ preventivi/giorno). Bail veloce (fallisce ~1min non 5) + retry visibile in GUI.
  Provato live: retry tentativo1 bloccato→tentativo2 OK; batch mockato 3 link (1 fallito isolato) OK.
  **NB anti-blocco:** rotazione IP gratis NON esiste (IP free = datacenter = Akamai blocca); soluzione €0 = cookie persistente. Proxy residenziali = a pagamento (solo se si scala a centinaia/giorno).
  (6) **FIX CRITICO (2026-07-05, `07d4886`):** lo scraper ora ASPETTA i dati veri (`window.__INITIAL_STATE__`) e li PRETENDE
  per dichiarare successo. Bug precedente (bail a 20s) afferrava la pagina prima del caricamento JS → PDF vuoto/Gate A rosso o falso
  "anti-bot". Profilo persistente ora IBRIDO: tentativo 1 = fisso (cookie), retry = sessione fresca. **Testato live su hotspot:
  Hyundai i20 20.990→24.620, 14 foto, 6 gate verdi, PDF in 35s al 1° tentativo.** L'app FUNZIONA (il blocco era mia regressione, non Akamai).
- **AGGIORNAMENTI 05/07 (ultima build su main `063cd27`, zip rigenerato 120.7 MB):**
  (7) **Traduzione AI COMPLETA** (`da9dfe6`,`db286b1`): AI su equip+scheda PRIMA di costruire descrizione/highlights +
  passata FINALE su TUTTI i campi + 4 tentativi/gestione 429; glossario +TÜV/HU/AU/Vorbereitung. **Validato: 6 auto → 0 residui.**
  (8) **Gate meno severi (solo difetti veri)** (`dff8a7d`,`d771d93`): Gate IMG non blocca su foto piccole del venditore;
  Gate B blocca solo se tedesco nel titolo o abbondante; fix falso positivo km 0.0 (auto nuove).
  (9) **GUI: avanzamento compatto + ARCHIVIO** (`9a0b3a4`): 1 riga/preventivo che si aggiorna ("Preventivo i/N: Pronto") +
  "Tutto caricato in…"; bottone Archivio in alto a dx → griglia blocchi (foto/nome/prezzo/"Apri il preventivo") nella stessa
  interfaccia + freccia ← indietro. Ogni PDF salvato in `archivio/` in automatico.
  (10) **REGISTRO-ERRORI + CHECKLIST-CONSEGNA** (`063cd27`): 9 errori E1-E9 (causa+fix+regola). Direttiva #3 = obbligatori.
- **Riserva AI traduzione ATTIVA** (Groq €0). **Kill-switch LIVE** ("X non paga" → blocco+email). Fabbrica: `/nuovo-concessionario`.
- **Verificato oggi**: 5 auto scrapate→PDF (Hyundai/Skoda/Volvo/Land Rover/VW) · 6 auto tradotte→0 residui.
- **🔴 FIX CRITICO 2026-07-15 (Max, CP-20260715-001): GUI PREMIUM SENZA WEBVIEW2 (motore Chrome-app).**
  Il cliente vedeva la GUI VECCHIA/Tkinter perché sul suo PC mancava il WebView2 Runtime → pywebview
  ripiegava in silenzio. Non riproducibile da Max (WebView2 c'è sul suo PC) → tentativi al buio.
  **Soluzione:** nuovo motore `main_chrome_app()` in `app.py` — la stessa `ui/index.html` premium è servita da
  un mini-server locale (127.0.0.1) e mostrata in una finestra **Google Chrome `--app`** (Chrome è già richiesto
  da scraping+PDF → sempre presente). Bridge JS↔Python via `POST /api/<metodo>`. Ordine motori: Chrome-app →
  pywebview → Tkinter. **Testato estraendo lo zip come Novacar → premium OK** (header scuro, Archivio, bollino
  `v2.1 · 13 lug`, bridge dealers/poll). ⚠️ Scraping NON toccato (headless resta default). Consegna aggiornata:
  `CONSEGNA-NOVACAR-NUOVA/PreventivoForge-v2.1-13lug.zip` (cartella interna `PreventivoForge-v2.1` + `LEGGIMI-PRIMA.txt`).
  ⚠️ **Gael**: `app.py` (nuovo motore GUI) — Half B toccato da Max; `ui/index.html` invariata (riusata identica). REGISTRO-ERRORI E11 + regole 12-13.
- **AGGIORNAMENTO 2026-07-09 (Max, CP-20260709-001): ARCHIVIO SI SVUOTA A OGNI CHIUSURA APP.**
  `archivio.py` +`clear()` (cancella PDF-copia+miniature+indice, NON i PDF di output); `app.py` la chiama dopo chiusura
  finestra (pywebview E Tkinter). **Exe consegna RIBUILDATO** (2026-07-09 10:15) → **zip rigenerato 117.4 MB**
  (`Consegna-Novacar/PreventivoForge-Novacar.zip`, verificato: exe nuovo + `.env` + LEGGIMI + modulo con `def clear()`).
  Test: clear() pieno→vuoto OK, `entries()` vuoto→[]. NB: svuota solo a chiusura pulita (X), non su crash/Task Manager.
- **REGOLA GLOBALE PREZZO (Max 2026-07-09, CP-20260709-002): il 2° fisso (fixed_2=1500) è GUADAGNO, sommato a "Prezzo autovettura".**
  Nel PDF: UNA sola voce servizi "**Immatricolazione, pratiche e trasporto**" = 1.500 (fixed_1); la voce "Trasporto" NON esiste più.
  Il secondo 1.500 (fixed_2 = margine) **si somma alla voce "Prezzo autovettura"** (`listed + fixed_2`), così il guadagno
  è indistinguibile dal prezzo auto e **le voci visibili tornano col totale**. Vale per OGNI preventivo/concessionario
  (unico punto: `render_pdf.py::_price_novacar`, Half B). Totale `final_eur` invariato. ⚠️ **Gael**: `render_pdf.py` toccato da Max (lista sotto).
  Test: Prezzo autovettura **17.450** (15.950+1.500) + Maggiorazione 478 + Immatr./pratiche/trasporto 1.500 = **TOTALE 19.428** (somma esatta).

### ⚠️ GAEL — file Half B che MAX ha toccato (lista COMPLETA — allineati se riprendi GUI/traduzione)
- **`app.py`**: `_StreamToQueue` (fasi compatte + retry visibile) · `run_batch`/`_parse_links` (multi-link 10 + eventi
  strutturati link/phase/linkdone/allpath + salvataggio archivio) · `brand.json`/`_list_dealers` · `_CODE_MSG` 8/9/10 ·
  guard stdout selftest · load `.env` frozen · bridge `archive()`/`open_pdf()` · input `<textarea>`/Tkinter `Text`.
- **`ui/index.html`**: RISCRITTA — avanzamento compatto (1 riga/preventivo) + **vista Archivio** (griglia blocchi + toggle + back).
- **`translate_copy.py`**: `_ai_fill_residuals` SOSTITUITO da `_ai_fix_sources` (AI sulle fonti prima dei derivati) + `_ai_final_sweep` (AI su tutti i campi).
- **`qa_gate.py`**: `gate_img` (solo difetti veri) · `gate_b` (tolleranza residuo minore) · `_specs_consistency` (fix km numerico).
- **`glossary_de_it.py`**: +TÜV/hauptuntersuchung/abgasuntersuchung/vorbereitung.
- **`render_pdf.py`** (2026-07-09): `_price_novacar` — voci prezzo cambiate per REGOLA GLOBALE Max: una sola voce
  "Immatricolazione, pratiche e trasporto" (fixed_1); rimossa la voce "Trasporto" (fixed_2 = guadagno, solo nel totale).
  Template/motore PDF NON toccati (itera `price.lines`, invariato).
- **NUOVI file (miei, Half A)**: `implementation/archivio.py` · `implementation/ai_translate.py` · `implementation/licenza.py` ·
  `gestione-licenze.py` · `nuovo_concessionario.py` · `REGISTRO-ERRORI.md` · `CHECKLIST-CONSEGNA.md` · `COME-CONSEGNARE-A-NOVACAR.md`.
- Mai toccati: `render_pdf.py`, `templates/preventivo.html`, REGOLE-SACRE, schema (congelato).
**GAEL: prendi l'ULTIMA build (git pull / zip rigenerato). Se riprendi GUI/traduzione parti da questi file. Leggi `REGISTRO-ERRORI.md`.**

## 🔴 MAX — PROSSIMO BUILD: ISPETTORATO GENERALE (Performance & Autocritica) — dossier 15 (2026-07-04)
**Direttiva Max (CP-20260704-001): da ora l'Impero si AUTOCRITICA e AUTO-MIGLIORA. Piano = `PIANO-MAESTRO/15-DOSSIER-ISPETTORATO.md`.**
- **Cosa:** nuovo organo trasversale di governo `company/Ispettorato/` — report COMPLETO dopo OGNI utilizzo,
  analisi al millimetro, daily autocritica, **REGISTRO-ERRORI + gate anti-recidiva (mai lo stesso errore 2 volte)**.
  Riporta agli alti ranghi: Board C-Suite + MAXIMILIAN + Max. Indipendente dalla produzione (misura, non costruisce).
- **Roster:** 10 agenti CF-grade (isp-conductor, telemetry-collector, run-auditor, error-registrar, recidiva-sentinel,
  kpi-analyst, report-forger, liaison-altiranghi, improvement-dispatcher, verifier) + 4 WF
  (RUN-AUDIT · DAILY-AUTOCRITICA · RECIDIVA-GATE · REPORT-ALTIRANGHI). Backbone dati JSONL deterministico, €0 API.
- **Fasi MAX (M1→M5):** M1 fondamenta+registro (migra KNOWN ERRORS+lezioni Memory) → M2 pilota PreventivoForge
  (trace in `run.py` + run-report auto) → M3 reparto CF-grade (swarm) → M4 aggancio Impero (RECALL/RETRO, dossier 10,
  handoff MAXIMILIAN/Board/Sentinelle/CF-R8) → M5 estensione (outreach + test negativo recidiva).
- **Owner: SOLO MAX.** Gael NON coinvolto (resta su V2-2/V2-3). Confini anti-duplicazione nel dossier §4.
**PROSSIMA AZIONE MAX: fase M1** (ciclo 9 passi, poi CP+STATO+push).

## ✅ MAX — PreventivoForge: FABBRICA multi-concessionario + KILL-SWITCH LIVE (2026-07-03, CP-002 esteso)
**Pushato su main (`c488968`). Half A avanzata: da 1 cliente a FABBRICA di app clonate + abbonamento operativo.**
- **Fabbrica `nuovo_concessionario.py`**: 1 comando → nuovo concessionario. Un MOTORE, N app. Cambia solo
  nome/dati/logo/prezzo/colori. Ogni app ha `brand.json` (titolo+dealer), si blocca sul suo dealer, PDF col suo stile.
  **Testata a exe frozen**: app clonata "Test Auto srl" → dealer proprio, 6/6 gate verdi (poi artefatti puliti).
- **Kill-switch LIVE**: Gist segreto creato (`gestione-licenze.py` = sospendi/attiva/stato via `gh`). `license_url` cucito
  nel config Novacar. **Test dal vivo: sospendi→preventivo BLOCCATO (exit 10)→riattiva.** Max dice "X non paga" → Claude blocca+email.
- **Skill `/nuovo-concessionario`** + doc `FABBRICA-CONCESSIONARI.md` (spiega tutto: fabbrica + kill-switch).
- **App branding**: `app.py` legge `brand.json`; dealer caricabili anche da accanto all'exe (per app clonata). 2 file mod di app.py già avvisati.
- Segreti locali (gitignorati): `licenze.config.json` (id gist), `.licenza_cache.json`, `Memory/storico-preventivi/*.pdf`.
- **Riserva AI traduzione (€0) — ATTIVA**: `implementation/ai_translate.py` (mio) + hook `_ai_fill_residuals` in
  `translate_copy.py` (⚠️ Half B, 1 aggancio) — traduce i SOLI residui tedeschi. Provider = **Groq gratuito**
  (riuso chiave Outreach), config in `.env` (gitignorato). **Testato dal vivo**: 4/4 termini + auto-riparazione residuo reale;
  sul GLA (glossario copre tutto) AI si attiva 0 volte (nessuna chiamata sprecata). `app.py` frozen carica `.env` accanto all'exe;
  la fabbrica (`--build`) mette il `.env` con la chiave nelle app dei dealer → anche loro si auto-riparano (Max: stessa chiave Outreach).
**RESIDUO:** firma codice SmartScreen (opz.) · test PC senza Chrome · [Max next = ISPETTORATO M1, vedi blocco in cima].

## ✅ MAX — PreventivoForge: GATE IMG/R in run.py + KILL-SWITCH + STORICO + EXE ri-testata (2026-07-03)
**CP-20260703-002. Chiuse TUTTE le PENDING MAX + consegna abbonabile pronta.**
- **Gate IMG + Gate R cablati in `run.py`** (bloccanti dopo Gate D: exit 8=foto/R-09, 9=REGOLE-SACRE). Testati VERDI su run reale.
- **Storico automatico**: ogni PDF consegnato → `Memory/storico-preventivi/<run>_<dealer>_<auto>.pdf` + sidecar JSON (url/prezzo/titolo). Non bloccante.
- **Kill-switch abbonamento = `implementation/licenza.py`** (mio, Half A). Controllo online (`LICENSE_URL` env o `dealer.license_url`) PRIMA di ogni preventivo:
  sospeso→blocca (exit 10); grace su rete-giù; **anti-furbata** (cache: sospeso+offline RESTA bloccato). 6 scenari testati OK. Semplice: stato in un JSON pubblico (Gist) che Max aggiorna.
- **`--remote-allow-origins=*` già presente in `cdp.launch`** (pending #2 = era già chiuso).
- **EXE RICOSTRUITA + ri-testata FROZEN**: `dist/PreventivoForge/PreventivoForge.exe --selftest` → pipeline completa, **6/6 gate + 14/14 REGOLE verdi**, PDF 2.2MB via cdp-chrome, storico OK. Prova che il bundle risolve tutte le dipendenze e Chrome stampa da frozen.
- **Guida consegna = `CONSEGNA-NOVACAR.md`**: requisiti PC concessionario (Chrome+linea normale), uso, SmartScreen, come ATTIVARE/SOSPENDERE il kill-switch via Gist.
- **⚠️ Ho toccato `app.py` (Half B) per 2 righe difensive necessarie:** `_CODE_MSG` +codici 8/9/10; guard `sys.stdout is None` nel ramo `--selftest` (l'exe windowed crashava). Nient'altro di Half B toccato. Gael: allineati a questo.
**GAEL LIBERO:** GUI premium approvata da Max ("esteticamente perfetta") → **riprendi l'Empire** (V2-2/V2-3, vedi sotto). NON toccare Half A (run.py/scraper/parser/pricer/cdp/licenza/schema).
**RESIDUO consegna (non bloccante):** test su PC realmente pulito SENZA Chrome (verificare il messaggio d'errore guida l'utente) + eventuale firma codice per togliere SmartScreen.

## ✅ GAEL — PreventivoForge: PDF NOVACAR + Gate IMG/R + APP .EXE FATTE (2026-07-02)
**HANDOFF-GAEL-2 COMPLETO (CP-20260702-003).** Cliente reale = **Novacar srl**.
- **PDF rifatto sul modello Novacar** (`templates/preventivo.html` + `render_pdf.py`): pag.1 solo-logo, logo header ogni pagina,
  pag.2 dati azienda(P.IVA/PEC)+titolo+scheda tecnica (12 campi, barra scura/righe alternate), pag.3 Equipaggiamento+Garanzia+
  "Totale in strada (Iva inclusa)" con dettaglio, pagine foto 2/pagina **mai tagliate (`contain`)**, ultima pagina solo-logo. Fix logo su bianco.
- **2 nuovi Gate + agenti CF-grade:** `gate_img` (Gate IMG, R-09) + `gate_regole` (Gate R, R-01…R-14 → `regole-check.json`);
  agenti `qa-immagini` + `qa-regole-checker` (7 file each). CATALOG aggiornato.
- **App .exe COSTRUITA e VALIDATA:** `dist/PreventivoForge/PreventivoForge.exe` (PyInstaller, gitignorato). `PreventivoForge.exe --selftest`
  → dealer Novacar, 4 gate verdi, PDF via cdp/Chrome. App `app.py` default dealer=novacar.
- **Verifica:** selftest **6/6 gate verdi (A,B,C,D,IMG,R)** + **14/14 REGOLE-SACRE OK**, PDF ispezionato = conforme al modello. €0 API.
- Half A NON toccata (cdp/run.py/scraper/parser/pricer/schema intatti).
**PENDING MAX (Half A, non bloccante):** (1) **wiring Gate IMG + Gate R in `run.py`** dopo S5 (2 chiamate con `dealer`);
(2) `--remote-allow-origins=*` in `cdp.launch`; (3) storico in `Memory/storico-preventivi/` a ogni run reale.
**RIPRESA GAEL (dopo GO Max):** scelta prossimo ecosistema Empire (05-MULTI-BUSINESS / split 06).

## 🚨 PIVOT V2 (ADR-007 — leggere PRIMA di qualsiasi cosa)
Max ha dettato la **Direttiva di Scala**: `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md`.
In sintesi: 1 workflow = Content Factory Exponium intero · Board C-Suite = 7 workflow da
≥10 agenti l'uno · ogni reparto = team 6-10 agenti + 1-5 workflow CF-grade · Mandato =
ecosistema di governo · Sentinelle multi-workflow · Guilds ricche · nuovo organo
**MAXIMILIAN** (team che incarna Max, corpus in `Memory/maximilian-corpus/`) · knowledge
ingestion delle cartelle formazione · roadmap V2-0…V2-8. **Lo standard v1 è superato.**
→ Per GAEL: il tuo F1-bis in corso VALE (è la base, completalo pure) — ma la fase dopo
NON è più F5: è **V2-2 (dossier v2)** poi **V2-3 (organo MAXIMILIAN)**, vedi roadmap §10
del piano V2. Niente nuove strutture a standard v1 da ora in poi.

## 🧭 DIREZIONE ATTIVA (2026-06-16, Max) — GENESI CORE prima di tutto
Decisione strategica di Max: **basta espandere la mappa in orizzontale. Si costruisce il
NUCLEO GENERATIVO vivo, poi l'azienda nasce da lì.** Ordine NON negoziabile:

1. **ARCHITETTURA (reparto + ecosistema)** — NUOVO, gerarchia altissima. È "una specie di
   FORGE specializzata SOLO nella struttura/architettura di OGNI artefatto che la FORGE crea"
   (NON l'architettura dell'infra Empire — è architettura *per-artefatto*). È il **fulcro del
   nucleo** di ogni operazione FORGE. Va definita e costruita al MILLIMETRO (architettura =
   fondamenta, NON è il "loop di pianificazione" da evitare). Motori reali: `architect-agent`,
   `prd-architect-os`, `agent-architecture`, SPARC, `Skill Master Architecture`, `agent-factory/`.
2. **FORGE completa (reparto + ecosistema)** — costruita ATTORNO ad ARCHITETTURA come suo nucleo.
   Oggi in `company/` è v1 magra (reparti = solo README stub). Da completare al millimetro + resa operativa.
3. **MAXIMILIAN** — attivo e operativo per OGNI operazione/creazione (dossier 12 già pronto, build).
4. **Board C-Suite intero** — come descritto nel messaggio-direttiva di Max (corpus Maximilian).
5. **→ solo allora**: costruzione completa reparto-per-reparto.

**Regola FORMA GIUSTA (Max 2026-06-16, NON meccanica):** NON ogni cosa è "reparto+ecosistema".
Si sceglie la forma con INGEGNO, caso per caso: le cose grandi (FORGE, ARCHITETTURA) = reparto
**+** ecosistema (o di più); altre = solo architettura di **team**, o un **principio**, o uno
**stile**, o un **workflow**, o una **skill**. Mai stampare la stessa forma su tutto. Quando Max
dice "reparto+ecosistema" per FORGE/ARCHITETTURA intende davvero entrambi — ma è quel caso, non una regola universale.

**Coordinamento Max↔Gael (regola Max 2026-06-16):** quasi mai si lavora in contemporanea →
a OGNI inizio sessione si LEGGE+AGGIORNA questo file (stato sempre corrente). Niente "non
lavorate insieme": si lavora sempre, basta che lo stato sia aggiornato così non ci si scontra.

**Substrato (proposto, da confermare all'attivazione):** nativo Claude Code (subagent
`.claude/agents/` + skill + Agent tool) ORA; Ruflo come strato di scala DOPO. La fase 1-2
(definizione ARCHITETTURA+FORGE) è substrato-agnostica: si wrappano motori reali già nativi.

**Lezione 2026-06-16 (collisione case-insensitive):** lo swarm Sonnet di Max su F1-bis ha
duplicato + collisato col lavoro (migliore) di Gael → conflitto git su 5 file 06-PLATFORM/Reparti.
Lavoro Max scartato (superato da V2-2 Gael). Naming Title-Case FISSO obbligatorio (vedi sotto).

---

## Fase roadmap corrente
**V2-2 — DOSSIER v2 — IN CORSO (2026-06-16, Gael).** F1-bis ✅ COMPLETATO (CP-002).

**V2-2 fatto finora — i 2 dossier NUOVI sono completi:**
- ✅ Dossier **MAXIMILIAN** (`PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`, CP-003): blueprint
  organo LX (8 agenti, review-gate 5-bis, 2 workflow, 2 skill) — build in V2-3.
- ✅ Dossier **MANDATO-ecosistema** (`PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`, CP-004):
  blueprint governo (6 custodi, 3 workflow, comando Sentinelle, contradiction-check) — build V2-5.

**V2-2 riscrittura dossier 01-09 a scala v2 (file NUOVI `-V2.md`, v1 intatti):**
- ✅ Lotto 1 (CP-005): 01-AGENCY-V2 (10 reparti, ~75 agenti, 25 WF) + 04-MARKETING-V2 (6 reparti, ~49 agenti, 22 WF)
- ✅ Lotto 2 (CP-006): 03-CONTENT-FACTORY-V2 (mega, 5 livelli, ~76 agenti, 23 WF) + 02-INFO-BUSINESS-V2 (mega, ~48 agenti, 15 WF)
- ⬜ Lotto 3: 05-MULTI-BUSINESS + decisione split 06-CORE (Platform/Forge/Intelligence/Operations → 4 dossier v2?)
- ⬜ Lotto 4: 07-BACKBONE, 08-ROADMAP, 09-MEMORY
- Pattern confermato: swarm 2 agenti/lotto, acceptEdits, Title-Case, idempotente — non muore.
Poi V2-3 (build organo MAXIMILIAN dal dossier 12 — attiva il review-gate 5-bis).
Vedi `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md` §10 (roadmap V2-0…V2-8).

## ⚠️ COORDINAMENTO (anti-collisione)
- 🟢 **GAEL — PRIORITÀ #1 FATTA (2026-07-03, CP-20260703-001): GUI App resa PREMIUM.**
  Motore grafico passato da Tkinter → **pywebview + HTML/CSS** (`ui/index.html`): font di sistema premium
  (Segoe UI Variable), palette slate+argento (invariata, approvata), gradienti/ombre/filo argento, focus-ring,
  hover fluidi, barra avanzamento animata, log colorato, resa nitida WebView2. **Layout/struttura/colore invariati.**
  `app.py`: finestra premium via pywebview + bridge + **fallback automatico Tkinter** (PC senza WebView2). Titolo → "Novacar srl".
  Validato: GUI premium confermata WebView2 in **dev e nell'.exe** (`dist/PreventivoForge/PreventivoForge.exe` ricostruito).
  Glossario: +Sitzeinstellung (sbloccava un preventivo Mercedes CLS reale). **PDF/template/REGOLE NON toccati (ownership Max).**
  → Attende feedback resa (ritocchi tonalità/font/spaziature). Poi (GO Max): scelta ecosistema Empire.
- 🛑 **OWNERSHIP PDF (2026-07-02, Max) — STOP COLLISIONI.** Il **PDF/template/REGOLE** ora li rifinisce **MAX** sul feedback live del cliente.
  **GAEL: NON toccare `implementation/render_pdf.py`, `templates/preventivo.html`, `regole/REGOLE-SACRE.md`** (oggi 2 collisioni su questi file). Tu lavori SOLO su **app.exe / GUI argento** e sui suoi file (`app.py`, build).
  **Decisioni Max (inviolabili):** (1) **min 2 foto per pagina** — layout flex, foto si distribuiscono in altezza, mai overflow, mai 1 sola; (2) **NO CROP** — `object-fit: contain` (regola sacra R-09, Max: "senza tagli"). ⚠️ **Annullato il passaggio a `cover`/ritaglio** fatto da Gael: crop taglia l'auto. Col flex le foto sono grandi e intere (niente bande bianche). Se serve rivedere: decide Max.
- 🟠 **GAEL — TASK PRIORITARIO (2026-07-01): App .exe + PDF template Novacar.** Vedi
  `Clienti/Prof Autocad/preventivo-forge/HANDOFF-GAEL-2.md` + regole inviolabili `.../regole/REGOLE-SACRE.md`.
  In sintesi: (1) rifare `render_pdf.py`+`templates/` sul **modello Novacar** (pag.1 solo logo, logo in ogni pagina,
  pag.2 dati azienda+scheda, pag.3 equip+garanzia+"Totale in strada", foto TUTTE e MAI tagliate, ultima pag. solo logo);
  (2) `render_pdf` usa `cdp.py` (no Playwright, per l'.exe); (3) nuovo agente `qa-immagini` (Gate IMG, R-09);
  (4) nuovo agente `qa-regole-checker` (Gate R, R-01…R-14); (5) **App .exe GUI minimal ARGENTO** (PyInstaller, no Python/Claude per il cliente).
  ✅ **MAX ha già fatto:** scraping LIVE reale (Chrome+CDP), parser dati veri, `cdp.py`, dealer **novacar** (dati+logo reali),
  rimosso placeholder "prof-autocad" (dealer default→novacar), `REGOLE-SACRE.md`, ecosistema `Memory/`, `avvia-preventivo.bat`.
  ⚠️ Wiring Gate R/IMG in `run.py` = Max (dopo che Gael consegna i gate).
- 🟣 **MAX — CLIENTE «Prof Autocad» — PreventivoForge (2026-06-30) — primo cliente ufficiale.**
  Workflow: **annuncio mobile.de (DE) → PREVENTIVO italiano (PDF)**, prezzo finale `esposto×1.03+1500+1500` nel titolo,
  **multi-concessionaria** (config per dealer in `preventivo-forge/concessionarie/<id>/`; prima = `prof-autocad`).
  Architettura: `Clienti/Prof Autocad/preventivo-forge/00-ARCHITETTURA-WORKFLOW.md`. Metodo: architect-agent (RBI) + content-forge + master-build-architecture.
  **✅ HALF A (Max) FATTA e testata:** scraper S1 (Playwright+fallback manuale), parser S2 (→`listing.json`, JSON-LD+DOM),
  pricer S4 (18.000→21.540 ✅), regia `run.py` (multi-tenant, gate A minimo, import difensivo Half B), schema CONGELATI, multi-tenant `dealers.py`, skill `/preventivo-auto`.
  **✅ FONDAMENTA MAX FATTE (CP-20260630-003):** agenti CF-grade 7-file Half A (conductor + op-scraper/op-parser/op-pricer) + CATALOG + R1/R2/R4 + orchestration (supervisor/routing/registry/policies) + CLAUDE.md cliente. **Half A COMPLETA.**
  **✅ HALF B (Gael) COMPLETA e verificata (2026-07-01, CP-20260701-001):** S3 `translate_copy.py`+`glossary_de_it.py` (traduzione deterministica DE→IT ~150 termini),
  S5 `render_pdf.py`+`templates/preventivo.html` (motore Playwright), QA `qa_gate.py` (Gate A/B/C/D bloccanti), RULES R3/R5/R6, 6 agenti CF-grade (42 file), CATALOG aggiornato (Half B ✅).
  **Test end-to-end reale `run.py --manual` (BMW 320d) → PDF 63 KB, 4 gate ALL GREEN** (0 tedesco, prezzo 26.900→30.707 € ricalcolo indipendente), PDF ispezionato. €0 API (gancio LLM OFF, Art.4.3).
  **🟢 PreventivoForge: FUNZIONA END-TO-END LIVE sul primo annuncio reale (Max, 2026-07-01, CP-20260701-003).**
  Risolti 2 problemi critici: (1) **Akamai** bloccava lo scraping → ora **Chrome reale + CDP-attach** lo bypassa in automatico;
  (2) mobile.de non ha JSON-LD auto → parser riscritto su `window.__INITIAL_STATE__` (dati veri). Gate B/C/D wirati in run.py, glossario esteso, fix UTF-8.
  **Prova LIVE GLA (456259857): EXIT 0, 4 gate verdi, 26 foto, 0 tedesco, esposto 47.490 → finale 51.915 €, PDF 810KB con foto vere, ispezionato OK.** €0 API. Fixture regressione salvata.
  RESTA (non bloccante): (a) macchina che gira = Chrome + IP residenziale; (b) traduzione deterministica long-tail → opz. backend LLM (decisione Max); (c) dati reali dealer in config; (d) stile PDF vs BMW Z4; (e) variant titolo perfezionabile.
  Seam CONGELATO = `preventivo-forge/schema/listing.schema.json` (NON toccato). Scope Max/Gael: SOLO sotto `Clienti/Prof Autocad/`.
  **RIPRESA GAEL dopo GO Max:** scelta prossimo ecosistema Empire (05-MULTI-BUSINESS / split 06).
- 🔴 **GAEL STEP 5 ATTIVO ORA (2026-06-18):** dopo 04-MARKETING, costruisco **03-CONTENT-FACTORY**
  (mega-reparto, CF-Director + R1-R8 in 3 aree) dal dossier `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md`,
  sotto `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/<CF-RN-Nome>/` (Title-Case fisso).
  ✅ **batch 1 COMPLETO (CP-008/009):** CF-R0 Director (15 file, 7 agenti, contratto ordine multi-tenant) +
  CF-R1 Strategia & Brief (17 file, 8 agenti, WF-BRIEF/CALENDAR/TREND). Gate verde + 5-bis APPROVA, asset v1 intatti.
  ✅ **batch 2 COMPLETO (CP-010/011):** CF-R2 Brand-Kit Registry (14 file, 6 agenti, multi-tenant) +
  CF-R3 Produzione Video (20 file, 10 agenti, 4 WF, wrap hf/heygen-studio ATTIVI, dry-run Art.4.3). Gate verde + 5-bis APPROVA.
  **AVANZAMENTO 03-CF: 4 reparti su 9** (CF-R0, R1, R2, R3 ✅).
  ✅ **batch 3 COMPLETO (CP-012/013):** CF-R4 Produzione Testuale (18 file, 8 agenti, 4 WF, confine CF/MARKETING) +
  CF-R5 Visual & Design/Caroselli (20 file, 10 agenti, 4 WF, wrap carousel-factory ATTIVO). Gate verde + 5-bis APPROVA.
  Completati dopo il reset col rilancio di 2 agenti idempotenti (aggiunto solo il mancante).
  ✅ **batch 4 COMPLETO (CP-014/015):** CF-R6 QA&Gate (17 file, 8 agenti, 3 WF, INDIPENDENTE dalla produzione) +
  CF-R7 Pubblicazione (18 file, 8 agenti, 4 WF, wrap orchestratori publish ATTIVI, review umana obbligatoria). Gate verde + 5-bis APPROVA.
  ✅ **CF-R8 Apprendimento COMPLETO (CP-20260619-016):** 14 file, 6 agenti, 2 WF (PATTERN-DISTILLATION + IMPROVEMENT-CYCLE), 0 stub.
  🟢🟢 **03-CONTENT-FACTORY COMPLETO — 9/9 reparti (CP-016):** 158 file, **71 agenti CF-grade, 28 workflow.**
  Gate verde + 5-bis APPROVA su tutti i 9 reparti. Asset attivi intatti (carousel-factory, hf/heygen-studio, orchestratori publish).
  SECONDO ecosistema V2 completo di Gael (dopo 04-MARKETING). Nota: 5 stub v1 orfani nei Reparti/ → BACKLOG B-006 (pulizia).
  **PROSSIMO ecosistema Gael:** da concordare — liberi 05-MULTI-BUSINESS (dossier da scrivere) o split 06. NON 01/02 (Max).
- 🟢 **GAEL STEP 5 — 04-MARKETING COMPLETO (2026-06-18, CP-20260618-007):** PRIMO ecosistema V2
  interamente costruito. **6/6 reparti, 114 file, 44 agenti CF-grade, 22 workflow.** Tutti gate verde + 5-bis APPROVA.
  L2-1 Copywriting (24 file, 10 agenti, 6 WF) wrappa il Copy Workflow Orchestration Layer ATTIVO senza
  riscriverlo (ADR-003 — motore verificato git-pulito). L2-2/L2-3/L2-4/L2-5/L2-6 idem. CP batch 002→007.
  v1 schede e motore attivo intatti. **PROSSIMO ecosistema Gael:** da concordare — NON 02-INFO (Max lo sta facendo).
  Candidati liberi: 01-AGENCY (sessione dedicata, outreach attivo), 03-CONTENT-FACTORY (mega), 05-MULTI-BUSINESS.
- 🟢 **02-INFO-BUSINESS CHIUSO (Max, 2026-06-22 — CP-20260622-001):** 5/5 reparti V2 completi.
  Swarm 5 agenti Opus ha aggiunto le 6 cartelle standard mancanti (kpi/principi/regole/scripts/skills/state)
  + 4 workflow (PROD 3, STRA 1). **Reparti V2: 94 file, 42 agenti, 12 WF.** Gate struct VERDE
  (10/10 template, 0 magri, 0 vuoti), 5-bis MAXIMILIAN APPROVA. Namespace `infobusiness/{prod,lanc,vend,comm,stra}`.
  **GAEL: continua 03-CONTENT-FACTORY R4→R8 (02 è chiuso, non serve più toccarlo).**
- 💰 **PIANO ESTATE REVENUE ATTIVO (Max, 2026-07-19) — LEGGERE `PIANO-MAESTRO/16-PIANO-ESTATE-REVENUE.md`.**
  Ordine Max: fatturare entro UNA settimana, certezza ≥95%. Analisi: l'unico stream ≥95% = **S1 anticipare
  i 7 concessionari quasi-confermati da settembre a LUGLIO** (prodotto PreventivoForge già live). Moltiplicatore:
  **S2 Manuale Claude Code** (chiudere PREZZO B-003 il G1 — bloccante). Estate: S3 pagine lancio + S4
  mentalita.brutale (SOLO se automazione 100%, carousel-factory wrap) + S5 canali YouTube-Fliki auto
  (API key in `.env` locale gitignorato — MAI su GitHub).
  **▶️ GAEL — TASK SETTIMANA (in ordine):** (1) 30min: chiudi CF-R8 → 03 9/9; (2) G1: AUDIT ASSET tutte le
  pagine (mentalita.brutale, crea.illtuo_impero, altre pagine lancio+sito) → `05-MULTI-BUSINESS/AUDIT-PAGINE-20260719.md`;
  (3) G2: funnel Manuale (landing empire-premium-style + checkout + 3 email — prezzo arriva da Max G1);
  (4) G2-G3: batch 7 caroselli crea.illtuo_impero + bio→funnel; (5) G3-G4: pipeline mentalita.brutale 100% auto
  (produzione→QA→scheduler→report); (6) G4-G5: WF-YT v1 + test 1 video end-to-end API Fliki; (7) G6: analisi
  competitor 3 nicchie YT → proposta a Max; (8) G7: CP + RETRO con numeri veri. Dettagli nel dossier 16.
  **▶️ MAX — TASK:** G1 prezzo B-003 con team-prezzi · lista 7 concessionari · G2-G4 contattarli (script pronto
  da Claude/A8) · G3 approva funnel · G4-G5 sceglie nicchia YT · G6-G7 push vendita Manuale sui canali caldi.
  **Regola: revenue batte infra questa settimana. Un solo swarm Opus per volta.**
- 🏁 **01-AGENCY CHIUSO — 10/10 reparti (Max, 2026-07-11 — CP-20260711-002).** TERZO ecosistema completo.
  **182 file · 74 agenti · 28 workflow · 23.635 righe.** Gate VERDE, 5-bis MAXIMILIAN APPROVA.
  A1-A6 (batch 1-2) + A7-Account-Mgmt, A8-Closing, A9-Partnership-Referral, A10-QA-Cliente (batch 3).
  A2 wrappa il runtime outreach LIVE (ADR-003, intoccabile). A10 = audit INDIPENDENTE (audita, non costruisce).
  **2 difetti veri trovati dal gate e chiusi:** (1) namespace divergente (87 occorrenze) → canonico `agency/a<N>`,
  mappa autoritativa in `company/Ecosistemi/01-AGENCY/NAMESPACE.md`; (2) 6 README v1 stantii (roster inesistente)
  → riscritti CF-grade. **MAX libero per il prossimo ecosistema.**
  📌 **RETRO — regole nuove vincolanti:** (a) swarm = **WRITE-EARLY** (struttura inline, letture minime, scrivi
  file-per-file subito: da 1 file/21 tool_use a 16 file/20); (b) **l'idempotenza va SOSPESA contro i residui v1**
  (i file v1 vanno SUPERATI esplicitamente, non skippati); (c) un solo swarm Opus per volta (account condiviso).
- 🗄️ *(storico)* **MAX — 01-AGENCY build a BATCH:** dossier `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md`
  (10 reparti A1-A10, ~75 agenti). Reparti su disco erano vuoti.
  **Batch 1 ✅ CHIUSO (CP-20260622-002): A1+A2+A3** (58 file, 27 ag, 10 WF). A2 wrappa runtime outreach LIVE (ADR-003).
  **Batch 2 ✅ CHIUSO (CP-20260623-001): A4-Delivery + A5-Copywriting + A6-Marketing** (51 file, 21 ag, 9 WF,
  gate verde, 5-bis APPROVA). A5 riusa Gate Bibbia di A2 (pattern 6). **AVANZAMENTO 01-AGENCY: 6/10.**
  🟡 **Batch 3 PARZIALE (STOP session-limit 2026-06-23, reset 19:00 Roma):** i 4 agenti sono morti presto.
  Stato ESATTO su disco (RIPRESA chirurgica — completare SOLO i mancanti, idempotente):
  · **A7-Account-Management:** ✅ ARCHITETTURA.md + README.md — MANCA: agenti/ (roster §A7), kpi/principi/regole/scripts/skills/state, workflow/ (WF §A7). Namespace `agency/a7`.
  · **A8-Closing:** ✅ ARCHITETTURA.md + README.md — MANCA: agenti/ (roster §A8), kpi/principi/regole/scripts/skills/state, workflow/ (WF §A8). Namespace `agency/a8`.
  · **A9-Partnership-Referral:** ✅ solo README.md — MANCA: ARCHITETTURA.md + agenti/ + kpi/principi/regole/scripts/skills/state + workflow/. Namespace `agency/a9`.
  · **A10-QA-Cliente:** ❌ cartella ASSENTE — costruire TUTTO da zero (offset dossier 491 limit 45). Namespace `agency/a10`.
  Modello: reparti A1-A6 già fatti. Reference: `04-MARKETING/Reparti/L2-6-Conversion-Architecture/`. Dossier `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md` (A7 off=377/38, A8 off=415/38, A9 off=453/38, A10 off=491/45).
  → completa → gate → 5-bis → CP → **01-AGENCY 10/10 CHIUSO.**
  ⚠️ Scrivo SOLO docs sotto `company/Ecosistemi/01-AGENCY/` — runtime NON si tocca. **GAEL: NON toccare 01-AGENCY.**
  📌 LEZIONE: un solo swarm Opus per volta (account condiviso).
- 🟢 **STEP 4-heavy CHIUSO (2026-06-18):** Board C-Suite V2 = **7/7 figure complete** in
  `company/Board-CSuite/<FIGURA>/`. CEO+Chief-Forge (CP-20260617-001) · CTO+COO (CP-002) ·
  CMO+CRO (CP-003) · **CFO completato da Max (CP-20260618-001)** — ~70 agenti reali, 5-bis MAXIMILIAN APPROVA.
- 🟢 **GENESI CORE FATTO (Max, 2026-06-16) — tutto su origin, working tree pulito:**
  STEP 1 ARCHITETTURA (30 file, CP-007) · STEP 2 FORGE (34 file, CP-008) · STEP 3 MAXIMILIAN
  (15 file, CP-009) · STEP 4(c) blueprint Board (8 file, 70 agenti progettati, CP-010).
- 🟢 **Conflitto git RISOLTO** (Max ha eseguito `git reset --hard HEAD` + `git stash drop`):
  i 5 doppioni MAIUSCOLO superati buttati, tutto committato e pushato. Niente più pendente.
- Nessuno swarm attivo. Lotti 1-2 V2-2 chiusi (01,04,03,02 -V2 committati).
- I dossier v2 sono file NUOVI `-V2.md` accanto ai v1 (che restano riferimento, non toccati).
- REGOLA NAMING swarm (lezione CP-20260616-001): grafia file FISSA (Title-Case), mai
  mischiare MAIUSCOLO/Title-Case → su Windows (core.ignorecase) genera doppioni che
  bloccano i commit. Allowlist progetto include già `Write(company/**)` per gli swarm.

## ▶️ RIPRESA GAEL 2026-06-17 — STEP 4-HEAVY, poi NON FERMARTI MAI (direttiva Max)
**Max ordina: domani prendi tu STEP 4-heavy e NON ti fermi — costruisci a catena, fase dopo
fase, senza chiedere il permesso di continuare. Una fase finisce → CP → push → apri SUBITO la
prossima. Ti fermi solo a budget-guard 20% (chiudi pulito) o se un GATE è rosso 2 volte.**

### ✅ STEP 4-heavy COMPLETATO (2026-06-18, CP-20260618-001) — Board 7/7 figure, ~70 agenti.
### → TASK IMMEDIATO ORA = STEP 5 (vedi CATENA NON-STOP punto 2). Lo STEP 4-heavy qui sotto è STORICO (fatto).

### [STORICO/FATTO] STEP 4-heavy: FORGE costruisce le 7 figure Board dai blueprint
- **Fonte (già pronta):** `company/Board-CSuite/_BLUEPRINT/` — 7 blueprint (BP-CEO, BP-COO, BP-CTO,
  BP-CMO, BP-CRO, BP-CFO, BP-Chief-Forge) + BP-INDEX. Ognuno ha roster 10 agenti, ≥2 workflow,
  skill, handoff, struct-gate checklist, e l'albero cartella da costruire (template V2 §1).
- **Cosa fare:** per ogni figura, la FORGE costruisce il CONTENUTO nella cartella
  `company/Board-CSuite/<FIGURA>/` seguendo il template: `README.md`, `ARCHITETTURA.md`,
  `agenti/` (le 10 schede del roster, CF-grade I/O JSON), `principi/`, `regole/`, `skills/`,
  `scripts/`, `workflow/` (≥2), `kpi/`, `state/`. = ~70 agenti reali + ~14 workflow.
- **Swarm (Dynamic Workflow, idempotente, Title-Case FISSO):** 7 agenti (1 per figura) o 4 batch
  (2 figure ciascuno). Prompt: leggi il BP della figura → costruisci la cartella dal template →
  riusa il v1 `Board-CSuite/<FIGURA>.md` come base del conductor/README. Scope bloccato a 1 figura.
- **GATE:** ogni figura = struct-gate del suo BP (≥10 agenti, ≥2 workflow, 0 magri/0 vuote).
- **REVIEW 5-bis (ORA ATTIVA — l'organo MAXIMILIAN esiste):** applica `company/MAXIMILIAN/Skill/
  maximilian-standard-gate.md` → "Max approverebbe?" su 2-3 figure a campione. RIFAI → ricostruisci.
- **COMMIT:** CP-20260617-NNN + STATO + wiki/log + push. **Poi NON ti fermi.**

### CATENA NON-STOP (apri la prossima appena chiusa la precedente)
1. **STEP 4-heavy** (sopra) — 7 figure Board reali.
2. **STEP 5 — reparto-per-reparto:** costruisci il CONTENUTO V2 di ogni ecosistema dai dossier
   `-V2.md` già pronti (01-AGENCY-V2, 04-MARKETING-V2, 03-CONTENT-FACTORY-V2, 02-INFO-BUSINESS-V2)
   + completa i lotti dossier mancanti (05, split 06, 07/08/09). Un ecosistema per ciclo, swarm
   interno per i reparti. Ogni reparto passa ARCHITETTURA(struttura)→FORGE(contenuto)→MAXIMILIAN(5-bis).
3. Poi: Mandato-ecosistema operativo (dossier 13), Sentinelle, Guilds v2, knowledge ingestion.

### REGOLE NON NEGOZIABILI (valgono per ogni ciclo)
- Metodo 9 passi (`PIANO-MAESTRO/10-METODO-CICLO-FASE.md`) + passo 5-bis MAXIMILIAN (ora attivo).
- Swarm IDEMPOTENTI (verifica l'esistente prima di scrivere — gli agenti muoiono). Title-Case FISSO
  (lezione collisione Windows CP-20260616-001): MAI mischiare MAIUSCOLO/Title-Case → doppioni che bloccano i commit.
- Confine Genesi Core: ARCHITETTURA = struttura, FORGE = contenuto. Non reinventare strutture: usa i BP/dossier.
- Memory-first: RECALL questo file all'inizio, CP+push dopo OGNI fase. Coordinamento: aggiorna SEMPRE questo file.
- Budget-guard 20%: sotto soglia chiudi col COMMIT, NON aprire build nuovi (riparti la sessione dopo).

## Cosa e' stato fatto (ultimo evento in cima)
- 2026-06-18 — **STEP 5 batch 1: L2.6 Conversion Architecture costruita CF-grade** (Gael, CP-20260618-002):
  17 file greenfield in `company/Ecosistemi/04-MARKETING/Reparti/L2-6-Conversion-Architecture/`:
  README + ARCHITETTURA + 6 agenti (conv-lead opus, CA1-CA4 sonnet, CA-QA verifier) + 3 workflow
  (WF-FUNNEL-DESIGN, WF-CRO-SPRINT, WF-LANDING-AUDIT) + principi/regole/skills/scripts/kpi/state.
  Confine esplicito: L2.6 = strategia funnel (NON scrive copy, NON implementa pagine).
  Gate CA-QA bloccante, namespace `marketing/cro/*` definiti. 0 stub.
- 2026-06-18 — **STEP 4-heavy CHIUSO: Board C-Suite V2 completa 7/7** (Max, CP-20260618-001):
  completato il CFO (4 file mancanti: kpi/skills/scripts/state → 10 agenti, 3 WF, 21 file, 0 magri),
  5-bis MAXIMILIAN APPROVA. ~70 agenti Board reali. Next NON-STOP: STEP 5 reparto-per-reparto.
- 2026-06-16 — **STEP 4(c): blueprint Board via ARCHITETTURA** (Max, CP-20260616-010):
  `company/Board-CSuite/_BLUEPRINT/` (8 file, 70 agenti progettati). PRIMO uso reale di WF-ARCH-DESIGN:
  il Genesi Core lavora — ARCHITETTURA disegna la struttura delle 7 figure C-level (cartella-workflow
  CF-grade, roster 10 + workflow + skill + handoff + struct-gate). Inline, 0 swarm (budget-light).
  Next: STEP 4-heavy = FORGE costruisce il contenuto delle 7 figure (in attesa GO Max).
- 2026-06-16 — **STEP 3: organo MAXIMILIAN costruito** (Max, CP-20260616-009): `company/MAXIMILIAN/`
  (15 file). Il team che incarna Max (8 agenti MX-*), review-gate 5-bis WF-REVIEW-MAXIMILIAN +
  skill `maximilian-standard-gate` (8 test binari + scoring deterministico + gate_check.py). Da ora
  ogni fase passa il "Max approverebbe?" prima del commit. Genesi Core+governo = 79 file. Next: STEP 4 Board.
- 2026-06-16 — **STEP 2 GENESI CORE: FORGE completa** (Max, CP-20260616-008): `company/Genesi-Core/FORGE/`
  (34 file, 2264 righe, gate+review PASS). Reparto+ecosistema gemello di ARCHITETTURA: riceve il
  blueprint e costruisce il CONTENUTO. `Motori/Mappa-Motori.md` = 15 motori reali con path verificati
  (skill-creator, content-forge, agent-factory, architect-agent...). Genesi Core ora = 64 file. PUSH
  PENDENTE (conflitto git). Next: STEP 3 MAXIMILIAN.
- 2026-06-16 — **STEP 1 GENESI CORE: organo ARCHITETTURA costruito** (Max, CP-20260616-007):
  dossier 14 + `company/Genesi-Core/ARCHITETTURA/` (30 file, 2075 righe, gate+review PASS).
  Swarm 4 agenti Opus, Dynamic Workflow. ARCHITETTURA = FORGE specializzata nella STRUTTURA;
  sceglie la FORMA GIUSTA (skill/agente/team/principio/stile/workflow/doc/reparto/ecosistema)
  con ingegno e passa il blueprint alla FORGE. PUSH PENDENTE (conflitto git aperto). Next: STEP 2 FORGE.
- 2026-06-13 — **FIX ARCHITETTURA EMPIRE STUDIO** (Max, CP-20260613-001):
  Errore critico: Memory Empire omesso dal pipeline in sessione studio Andrei Pascu.
  Fix: RULES.md creato (checklist non negoziabili + KNOWN ERRORS registry),
  compliance-auditor + error-triage-controller + silent-observer aggiornati con
  Memory Empire guard esplicito + WATCH-001 counter video vs ME calls.
  SKILL.md aggiornato: invariante #0 (session-init) + invariante #8 (Memory Empire).
  Run Andrei Pascu andrei-pascu-001: fermata a Stage 2 video 1 (9CuQI0Cr4Pg, 545 frame pronti).
  Studio da riprendere: Cat 1-7 YouTube @Andrei Pascu (323 video totali, ~270 da studiare).
- 2026-06-11 — **F4 GATE VERDE** (Gael, CP-20260611-007): ciclo dry-run CY-20260611-001
  end-to-end (19 eventi trace.jsonl, 4 HC attraversati, 3 gate PASS) registrato in
  state.json. Criterio ADR-005 (slot pronto + test dry). verify: PASS 113/113.
  Lavorato SOLO in Memory/, scripts/, .claude/skills/ (rispettato blocco swarm).
- 2026-06-11 — **F4 B2 WRAP OUTREACH COMPLETATO** (Gael, CP-20260611-006): 4 team L3
  in company/01-agency/A2-ACQUISIZIONE/L3/ (creati prima del blocco swarm, file NUOVI)
  + scripts/agency-trace.ps1 (logger trace testato). Runtime outreach INVARIATO (ADR-003).
- 2026-06-11 — **F4 B1 AGENCY LIVE INFRASTRUTTURA COMPLETATO** (Gael, CP-20260611-004):
  company/01-agency/ con 6 reparti L2 (BACKBONE.md + handoffs), state.json + trace.jsonl schema,
  4 HC intra-agency, 9 nuove skill FORGE. Gate: PASS 97/97.
- 2026-06-11 — **F3 MIGRAZIONE ASSET COMPLETATO** (Gael, CP-20260611-003):
  51 skill/workflow mappate in skills-map.yaml, 35 cartelle in inventario-asset.yaml,
  8 wrapper L3 (Ecosistemi/<eco>/Workflow/). Gate: PASS 70/70.
- 2026-06-11 — **F2 BACKBONE OPERATIVO COMPLETATO** (Gael, CP-20260611-002):
  ruflo v3.10.41 installato, BUS (handoffs+HC-template), BRAIN (10 namespace),
  registro-agenti.yaml (19 agenti), verify-empire.ps1 PASS 59/59.
- 2026-06-11 — **F1 SCAFFOLDING EMPIRE OS COMPLETATO** (Gael, CP-20260611-001):
  task 1.1–1.7 completati. `company/` navigabile: GRUPPO.md, Mandato, Board-CSuite (7 agenti),
  10 Ecosistemi (ECOSISTEMA.md + BACKBONE.md + 4 sottocartelle ognuno), Backbone (6 componenti),
  Guilds (5), Sentinels (5), Gerarchia, `scripts/gen-empire.py`.
  Gate F1: `python scripts/gen-empire.py --check` → PASS 92/92.
- 2026-06-10 — **PIANO-MAESTRO completo**: 10 file in `Digital Empire/PIANO-MAESTRO/`
  (00 master, 01-05 ecosistemi business, 06 core, 07 backbone+ruflo+skills,
  08 roadmap 12 fasi, 09 MEMORY). Prodotto con swarm di 7 agenti paralleli + conductor.
- 2026-06-10 — **Ecosistema MEMORY** aggiunto su richiesta Max (urgenza massima):
  10° ecosistema, pattern #13 memory-first, costruzione ME-0/ME-1 in corso.
- 2026-06-08 — Studio approfondito repo Content Factory Exponium (AION GROUP) →
  wiki `projects/Exponium/Exponium_Content_Factory_Studio.md`.

## Lavori in corso
- **GitHub monorepo + sync Max↔Gael (ADR-004, CP-002): ✅ LIVE** — repo privato
  `ansjkfgheqrlg/Digital-Empire`, push iniziale 966.63 MiB completato (2026-06-10 21:27).
  PENDENTI: (a) Max incolla blocco hooks in `.claude/settings.json` (contenuto pronto,
  Claude non può editarlo per policy auto-mode), (b) Gael esegue SETUP-GAEL.md sul suo PC
  — DECISIONE Max 2026-06-10: Gael usa l'account GitHub di Max (ansjkfgheqrlg), niente
  invito collaborator; identità distinte solo via git user.name (Max/Gael).
- ✅ ME-0/ME-1 + review coerenza + wiki: COMPLETATI (CP-001).

## Blocchi / pending noti
- **NESSUN BLOCCO STRUTTURALE.** Item minori (token FB, prezzo manuale, team-prezzi, ecc.)
  → spostati in `BACKLOG.md` per direttiva Max (ADR-005): non fermano MAI la costruzione.
  Le fasi si riformulano per aggirarli (slot pronti + test dry).
- Ingestione Empire Studio canali YouTube riferimento (@Legamidiamore, @dosementale) —
  task 7.0 / F-MB1, sessione dedicata (questo è strutturale per F7, non per F4-F6).

## RIPRESA DA (per la prossima sessione)

### 🟡 RIPRESA IMMEDIATA (2026-06-17, Gael — stop crediti) — STEP 4-heavy quasi finito
- **6 figure Board su 7 COMPLETE e approvate**: CEO, Chief-Forge (CP-001), CTO, COO (CP-002),
  CMO, CRO (CP-003). ~126 file, 60 agenti CF-grade. Tutte gate + 5-bis Maximilian APPROVA.
- **CFO = ULTIMA, PARZIALE** in `company/Board-CSuite/CFO/`: fatti ~17 file e 4 agenti
  (cfo-cost-sentinel, cfo-roi-analyst, cfo-runway-tracker, cfo-memoria) + principi/regole/workflow avviati.
  **Mancano:** ~6 agenti (incl. cfo-conductor opus, budget-allocator, 3-tier-router, dry-run-guard, verificatore),
  i workflow completi, e i file di supporto. Riferimento qualità: scheda `CEO-Empire-Conductor/agenti/ceo-priorita-arbiter.md`.
  Blueprint: `_BLUEPRINT/BP-CFO.md`. CFO presidia: budget, cost guard, routing 3-tier, dry-run (Mandato Art.4.3).
- **AZIONE NEXT:** rilancia 1 agente FORGE per COMPLETARE la CFO (prompt idempotente: "completa i file mancanti,
  non ricreare gli esistenti") → gate (10 agenti/3 WF/0 magri/0 vuote/0 stub/v1 CFO.md intatto) → 5-bis → CP-004
  = **STEP 4-heavy COMPLETO** (7 figure, ~70 agenti). Poi STEP 5 (contenuto ecosistemi dai dossier -V2).

### Storico fasi F (completate)
1. Caricare questo file + INDEX.md (memory-first).
2. **F1 COMPLETATO** -- gate PASS 92/92.
3. **F2 COMPLETATO** -- gate PASS 59/59.
4. **F3 COMPLETATO** -- gate PASS 70/70.
5. **F4 GATE VERDE** -- verify PASS 113/113 (CP-004 B1, CP-006 B2, CP-007 ciclo dry).
   AGENCY live: 6 reparti, 4 HC, 4 wrap L3 outreach, state.json+trace.jsonl validati
   con ciclo dry CY-20260611-001, 9 skill F4, agency-trace.ps1 operativo.
6. **Prossime azioni:**
   - **PRIORITA' (handover Max): F1-bis arricchimento company/ col metodo 9 passi (ADR-006)**
     -- vedi ISTRUZIONI PER GAEL sopra. Il blocco swarm Max e' rimosso: company/ e' di Gael.
   - B3 reale: prima call vera -> discovery-call-brief -> beast-preventivi -> proposal-gate
   - Primo ciclo REALE: stesso pattern di CY-20260611-001 con dry_run: false
   - Backlog (ADR-005, non bloccanti): B-001 token FB (runbook in WF-OUTREACH-INSTAGRAM.md),
     B-002/B-003 prezzi via team-prezzi
   - F5: prossima fase roadmap (vedi PIANO-MAESTRO/08-ROADMAP-FASI.md) dopo fine swarm F1-bis
7. **YouTube ingestion** @Legamidiamore + @dosementale -- task 7.0/F-MB1, sessione dedicata
