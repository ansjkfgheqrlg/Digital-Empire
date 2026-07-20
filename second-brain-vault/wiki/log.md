# Wiki Log — Registro operazioni

## 2026-07-20 (FORGE-AGENT-SKILL — MIR-9: topology.md obbligatorio per team)
- BUILD: `templates/TOPOLOGY-TEMPLATE.md` (canonico ADR-008: tipo hier/pipeline/mesh/queen-swarm motivato,
  nodi = solo agenti 7-file reali [no agenti fantasma], entry point, edges con contratti input→output,
  escalation FAIL×2, memory touchpoints ADR-002, observability, kill-criteria, schema ASCII; regola:
  UNA pagina di puntatori — se non ci sta, il design è troppo complesso) + **R2-bis** in rules/ + step 6
  WF-AGENT-NEW + qa-gate checklist p.1 estesa.
- DOGFOODING: `FORGE-AGENT-SKILL/TOPOLOGY.md` — prima topology pubblica dell'impero: pipeline con gate
  finale (N0 conductor → N1/N2 smiths → N3 qa-gate → registrazione), 6 edges con contratti, escalation,
  kill-criteria 30gg-inattività. Esempio di riferimento nel template.
- Trigger check ASK-PROTOCOL: T1-T4 assenti (task procedurale additivo) → 0 domande (documentato in CP).
- Update: pagina [[tools/Tool_Forge_Agent_Skill_Reparto]], REGISTRO-IMPRESA §3, dossier 18 (inv. 9 ✅, MIR-9 ✅),
  STATO RIPRESA. CP-20260720-013.

## 2026-07-20 (MIR-12 — Review APSOC sito istituzionale Agency page)
- REVIEW: `Agency page - Copia/COPY-REVIEW-APSOC-SITO.md` — audit completo 13 sezioni del sito evoluto
  (metodo APSOC/CPB: la stessa dottrina `CPB_Gestioneobiezioni.md` del repo). Score **78/100** (gate 85).
  Struttura da lodare: 4 Diagnosi pain-first, calcolatore funnel, WhyUs, meta-copy TOV perfetto.
  **5 P0 bloccanti pre-pubblicazione**: 8 claim numerici senza fonte (50 mercati, +600%, Dubai, uptime… Art.2),
  tracking 0% (schema eventi uniforme consegnato: view_hero/select_area/click_cta/submit_lead/lead_fail),
  form che simula successo su errore (lead persi), GDPR senza consenso nei 2 form, offerta gratuita
  in 3 versioni (€500/40min vs kit YouTube 15min). **ASK-PROTOCOL prima applicazione reale**: Q1 offerta
  unica (rec: 15 min), Q2 sedi/metriche footer vere?, Q3 "Social Growth" vs MKD — default marcati.
  Delta: `Agency page/` vecchia = da deprecare. index.md aggiornato (riga entities) + Entity_Brand_Offer
  (nota applicazione canone). → [[tools/Tool_Copy_Workflow_Orchestration]]. CP-20260720-012.

## 2026-07-20 (YouTube Lead Machine — magnet #2: Checklist CRO 21 Punti)
- BUILD: `Formazzione/Youtube/LEAD-MAGNET-02-checklist-cro-21-punti.md` — secondo lead magnet del funnel:
  TOFU un-gated (link descrizione video V01/V02/V06 + pinned comment), 21 controlli in 5 zone
  (prima schermata / offerta / fiducia / conversione / velocità-tecnica) con tabella punteggio diagnostica
  e CTA finale → Analisi Gratuita (magnet #1 BOFU, gate 3 domande). Naming Hormozi (3 varianti, raccomandata
  «21 Punti per Smettere di Perdere Clienti dal Tuo Sito»). Review APSOC secondo pass: **93/100 PASS**
  (sezione aggiunta in `COPY-REVIEW-APSOC.md`, 3 difetti chiusi in stesura). Regole rispettate: il magnet
  risolve un problema stretto e rivela il core (Hormozi), zero cannibalizzazione magnet #1, TOV DE pulito.
- Update: cross-ref in LEAD-MAGNET-01, reference LEAD-MAGNET-OPS della skill, pagina progetto, REGISTRO §3.
  Resta: export PDF grafico (Max/Gael) → upload → link in SETUP-CANALE. CP-20260720-010.

## 2026-07-20 (FORGE-AGENT-SKILL — MIR-3: ASK formale obbligatorio)
- BUILD: `FORGE-AGENT-SKILL/workflows/ASK-PROTOCOL.md` (canonico; trigger T1-T4, max 3 domande mirate
  ognuna 1 decisione con opzioni+raccomandazione+default `[ASSUNZIONE]`, replies tracciate ↳, gate doppio
  conductor+qa-gate p.7) + step **ASK** inserito in WF-SKILL-NEW (step 4, rinumerata 1-8) e WF-AGENT-NEW
  (step 5, rinumerata 1-10). Chiude l'invariante #3 dell'architettura madre (PLAN→ASK→BUILD→CRITIQUE→ITERATE)
  che era ⚠️ parziale. → pagina [[tools/Tool_Forge_Agent_Skill_Reparto]] aggiornata, REGISTRO-IMPRESA §3 +1 riga,
  dossier 18 MIR-3 ✅. CP-20260720-009.
- MERGE: allineato a main squashed (G1 EmpireDesk chiuso e2e selftest 13/13, U1 slice 1 Operazioni Reali,
  Empire Studio video 10/29 = CP-20260720-002 Gael, verifica statica G1 = CP-20260720-003 Gael) — le mie
  voci CP 002/003 di oggi rinumerate **007/008** (pattern collisioni add/add già applicato altre volte oggi).

## 2026-07-20 (Empire Studio — video 10/29, Gael)
- INGEST: Empire Studio — video Ahp_6rHSOsU (Andrei Pascu, cat1-copywriting, video 10/29). Formato tutorial screen-share 11m08s — Google Docs (macOS) + talking head PiP. Stage 1-5 completati: 334 frame @2s (3-digit naming), 16 frame letti nativamente, NO-FINTO PASS. 16 VP schermo: doc diviso pagine→senza pagine, menu File Impostazione pagina, Google Drive file list, outline heading popolato, note gialle "[inserire logo]"/"[inserire capibara]", menu dropdown stato, badge [in corso]/[da iniziare], indice+segnalibro, pannello Stili "Aggiorna Intestazione", contatore parole live, outro CTA. VTT 2505 righe letto integralmente (9 capitoli ufficiali del video). 20 KA P12-traced. Concepts: pulizia formato no-pagine, heading→outline navigabile, aggiorna stile in blocco, note colorate come heading dedicato, dropdown stato = mini-kanban, segnalibri+link, conteggio caratteri live, sistema cartelle Clienti visibile/non-visibile. → 2 pagine create: Source_Andrei_Pascu_Google_Docs_Copywriter, Concept_Google_Docs_Copywriter_Workflow. index.md +2 entry sezione Copywriting. WATCH-001: N_video=10 = N_MemoryEmpire=10 → MATCH ✅

- INGEST/BUILD: clonati e integrati 3 toolkit ufficiali (`copy-workflow/`, `content-forge2.0/`, master-build-architecture su main confermata versione di riferimento); installati 3 wrapper in `.claude/skills/` (copy-workflow, content-forge, master-build-architecture).
- BUILD: nuovo reparto `FORGE-AGENT-SKILL/` (4 agenti fas-*, WF-AGENT-NEW/WF-SKILL-NEW, rules R1-R4, memory/) per la creazione di nuovi agenti e skill — direttiva Max "impero con più workflow".
- BUILD: `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md` (master-build-architecture applicata: 10 invarianti audit, 10 workflow mappa, 12 migliorie MIR) + ADR-009 + REGISTRO-IMPRESA + skills-map v1.2.
- APPLY copy-workflow (MIR-2 P0): review APSOC kit YouTube → `Formazzione/Youtube/COPY-REVIEW-APSOC.md` (score 78-84→90-93; patch applicate: descrizione canale v2, hook V01 v2, varianti CTA).
- → 4 pagine tool create (Copy_Workflow, Content_Forge_2, Master_Build_Architecture, Forge_Agent_Skill_Reparto). index.md aggiornato. CP-20260720-007 (era -002, rinumerato).

## 2026-07-20 (Toolchain VS Code — scansione completa)
- SCAN: censimento stack da `git ls-files` (8.123 png / 7.625 md / 867 py / 600 json / 596 tsx+ts / 471 go / 181 yaml / 107 pdf) + scansione Marketplace 14 categorie aggiornata al giorno (deprecazioni verificate: Cody Free discontinuato 2025-07-23, Dendron abbandonato, Ruff publisher `charliermarsh` confermato).
- BUILD: `PIANO-MAESTRO/19-TOOLCHAIN-VSCODE.md` (Tier 1=10 subito / Tier 2=11 per area / Tier 3=12 opzionali / 8 sconsigliati con motivo; mappa W1-W10; gate verifica) + `.vscode/extensions.json` (22 raccomandate, 2 unwanted) + `.vscode/settings.json` (format-on-save OFF per ADR-003, telemetry OFF, spellcheck it+en).
- Decisioni: agente AI = solo `anthropic.claude-code` (Copilot/Cody/Cline = duplicati esclusi); Markdown Memo abilita i wikilink `[[...]]` del vault in VS Code; niente markdownlint (rumore su 7.6k file legacy).
- → 1 pagina tool creata ([[tools/Tool_VSCode_Toolchain]]), index.md +1. CP-20260720-008 (era -003, rinumerato).

## 2026-07-20 (FORGE-AGENT-SKILL — prima skill forgiata: youtube-lead-machine)
- BUILD: WF-SKILL-NEW completa (MIR-11): RECALL anti-doppione (script-factory e copy-workflow restano, delegati) → PLAN → MKD (25/25 atomi, `memory/mkd/`) → skill `.claude/skills/youtube-lead-machine/` (kernel 118r + references×6 + evals 7 scenari + failure-modes F1-F8) → evals loop con 3 ritocchi → **GATE fas-qa-gate PASS 7/7** (`FORGE-AGENT-SKILL/memory/checkpoints/GATE-youtube-lead-machine-2026-07-20.md`).
- REGISTRAZIONE: skills-map v1.3 (61 mappati), REGISTRO-IMPRESA §3, STATO-EMPIRE, INDEX.
- → 1 pagina tool creata ([[tools/Tool_Youtube_Lead_Machine_Skill]]), index.md +1. CP-20260720-005.

## 2026-07-20 (FORGE-AGENT-SKILL — MIR retrofis + MKD brand-offer)
- BUILD (MIR-1+6): memory locale + REGISTRO-ERRORI standardizzati per 3 runtime → `Outreach/` (OE-1..5),
  `Workfolw crea caroselli à/` (CE-1..4), `Formazzione/Youtube/` (YE-1..3). Wrap ADR-003 (file aggiuntivi, 0 tocco runtime).
- BUILD (MIR-2): MKD Brand-Offer DE (`FORGE-AGENT-SKILL/memory/mkd/MKD-brand-offer-DE.md`, 12 sezioni da 475 righe sorgente,
  ➕ marcate, assumption ledger). Registrato in REGISTRO-IMPRESA §3.
- → 1 pagina creata ([[entities/Entity_Brand_Offer_DE]]), index.md +1. Dossier 18 MIR-1/2/6/11 marcati ✅. CP-20260720-006.

## 2026-07-20 (YouTube Lead Machine — kit di lancio)
- BUILD: kit eseguibile completo in `Formazzione/Youtube/`: CLIENTE-DORO.md (scheda ICP da `Materiale Agency`), SETUP-CANALE.md (copy pronta: nome/descrizione/banner/link/playlist), LEAD-MAGNET-01-analisi-gratuita.md (magnet "Analisi Gratuita 15 min" + gate qualifica + 5 messaggi automazione speed-to-lead pronti + metriche), batch-01/ (PIANO + 6 script completi hook verbatim/scaletta/CTA sui 4 pilastri: 2 ricerca TOFU, 1 educazione, 1 metodo 5 step, 1 audit dal vivo, 1 prova sociale) + 2 concept copertina AI in `batch-01/copertine/`. → pagina progetto [[Project_YouTube_Lead_Machine]] aggiornata. CP-20260720-011 (era -004, rinumerato: collisione con Ispettorato M1 di Max).

## 2026-07-19 (YouTube Lead Machine — avvio progetto)
- INGEST: 7 video YouTube lead-generation (`Formazzione/Youtube/Rebdere YOUTUBE un Lead magnet.txt`): 5× Lorenzo Ricchieri/Media Profit (metodo completo: mindset, 4 pilastri, funnel TOFU-MOFU-BOFU, 4h/settimana), Alex Hormozi (lead magnet), Sean Cannell/Think Media (framework 3 step + trust) + 2 infografiche NotebookLM. Trascrizioni complete lette (7 video, ~2h11m).
- BUILD: strategia operativa `Formazzione/Youtube/STRATEGIA-YOUTUBE-LEAD-MAGNET.md` (8 sezioni: mindset, posizionamento Schwartz, 4 pilastri, funnel con MOFU=audit CRO, lead magnet su misura, metodo 4 ore, speed-to-lead 391%/78%, piano 30 giorni + 7 errori mortali) + 7 note per video in `note-video/`.
- → 7 pagine wiki create: Project_YouTube_Lead_Machine (01 - Projects/), Source_MediaProfit_YouTube_Lead_Machine, Source_Hormozi_Lead_Magnet, Source_ThinkMedia_YouTube_Lead_Framework, Concept_YouTube_Funnel_TOFU_MOFU_BOFU, Concept_Lead_Magnet_Hormozi, Concept_Speed_To_Lead. index.md +7 (nuova sezione YouTube Marketing / Lead Generation).

## 2026-07-19 (Empire Desk — collisione UI risolta, Gael)
- FIX/COORD: scoperta al pull una collisione reale — Max ha ridisegnato `EmpireDesk/ui/index.html`
  in parallelo (nav-tab "Empire Premium") con lo stesso obiettivo del mio switcher pannelli, ma
  un contratto di rete diverso (`/api/modules` vs il mio `/api/panels`). Risolto merge manuale
  (8 blocchi): tenuto il design di Max, `app.py` riallineato al suo contratto esatto
  (`modules_public()`, route `api/modules`, chiave `panel_html`). STATO-EMPIRE aggiornato da Max
  nel frattempo: ownership `ui/index.html` passata a Max — confermato, Gael non lo tocca più.
  → CP-20260719-008 + REGISTRO-ERRORI EDE-8.

## 2026-07-19 (Empire Desk B1 — seam moduli, Gael)
- BUILD: `EmpireDesk/app.py` — loader `modules/*.py` (contratto dossier 17 §5.3): import isolato
  per file (un modulo rotto si segnala e si salta, mai crash dell'app), validazione schema tile
  anti-KeyError, dispatcher routes condiviso HTTP/pywebview, `global_selftest()` che include ogni
  modulo. `ui/index.html`: switcher "Pannelli" (tab per modulo) + CSS per le classi già usate dai
  3 pannelli di Max (metrics/revenue/licenze) — senza sarebbero apparsi senza stile. Fix grafico
  proattivo: header da posizionamento assoluto calcolato a mano a `display:flex` (eliminato rischio
  sovrapposizione bottoni). 2 bug trovati e corretti in autorevisione prima di ogni lancio (EDE-6/7).
  **NON eseguito**: sessione senza Python/Node → verifica reale rimandata a macchina con l'ambiente
  giusto. → CP-20260719-007 + STATO-EMPIRE aggiornati.

## 2026-07-19 (Empire Desk v0.1 — P1-P3, Gael)
- BUILD: nuova cartella `EmpireDesk/` — app launcher `.exe` di tutte le automazioni Digital Empire
  (ordine Max, dossier `PIANO-MAESTRO/17-EMPIRE-DESK-APP.md`). `app.py` con 3 motori GUI in
  fallback (Chrome-app → pywebview → Tkinter, applicato subito il pattern anti-WebView2 di
  CP-20260715-001), `TileManager` (subprocess reale su 8 automazioni + poll log-live + selftest),
  `ui/index.html` premium slate+argento+arancio `#fb4604`. 3 bug reali trovati e corretti in
  revisione statica del codice (sys.executable da frozen rilanciava l'app invece dello script;
  WinError193 su .bat senza cmd.exe /c; pause-hang su AVVIA-EMAIL-LIVE.bat/_avvia_ig.bat senza
  stdin=DEVNULL). Trovato ma non toccato: path hardcoded di un'altra macchina nei bat Outreach
  (ADR-003, fuori scope). **P4 (selftest+build exe) bloccato**: sessione senza Python/Node
  installati → da completare su macchina reale. → CP-20260719-002 + STATO-EMPIRE aggiornati.

## 2026-07-19 (V2-2 Lotto 3 — Gael)
- INGEST/BUILD: PIANO-MAESTRO, 5 dossier V2 nuovi via swarm 3 agenti paralleli: `05-ECOSISTEMA-MULTIBUSINESS-V2.md` (12 reparti, 72 agenti, nuovo reparto trasversale MB-Portfolio) + split del v1 `06-ECOSISTEMI-CORE.md` in `06a-ECOSISTEMA-PLATFORM-V2.md` (45 agenti), `06b-ECOSISTEMA-FORGE-V2.md` (40 agenti), `06c-ECOSISTEMA-INTELLIGENCE-V2.md` (35 agenti), `06d-ECOSISTEMA-OPERATIONS-V2.md` (37 agenti). Decisione: naming `06a/06b/06c/06d` per evitare collisione con dossier 07/08/09 già esistenti. Gate automatico verde (0 stub, 13/13 sezioni), review a campione fatta. `V2-INDEX.md` e `STATO-EMPIRE.md` aggiornati. → CP-20260719-001.

## 2026-07-11 (Empire Studio — video 9/29)
- INGEST: Empire Studio — video IWCHN_mE2Vo (Andrei Pascu, cat1-copywriting, video 9/29). Formato live session 1h02min — screen share Meta Ads Library + talking head PiP. Stage 1-5 completati: 1858 frame @2s (4-digit naming), 14 frame letti nativamente, NO-FINTO PASS. 12 VP schermo: Meta Ad Library homepage (Latvia location), gaming search Italy, filter stack ~98 results Laurea Online, real estate ads, EU Transparency Women 30-55 Reach 1770, shoe store owner DIY ad, Carisma shoes lifestyle, Andrei nighttime, palestra A/B test boxing, royal costume supermarket food ad, Corte CAB VANIGLIA dessert. VTT 11730 righe letto integralmente. 25 KA P12-traced. Concepts: Meta Ads Library stack, EU Transparency intelligence, Video vs Photo rule, Template Ads detection, Dan Lock Gap, Chiarezza > Creativita, email=staple ecommerce. → 2 pagine create: Source_Andrei_Pascu_Ads_Library_Live, Concept_Meta_Ads_Library_Competitor_Research. WATCH-001: N_video=9 = N_MemoryEmpire=9 → MATCH ✅

## 2026-07-09 (Empire Studio — video 8/29)
- INGEST: Empire Studio — video lQMO0LdeI2c (Andrei Pascu, cat1-copywriting, video 8/29). Formato live session 44:55 — screen share McFit+Dyson + talking head PiP. Stage 1-5 completati: 1348 frame @2s (4-digit naming), 13 frame letti nativamente, NO-FINTO PASS. 6 VP schermo: McFit Hero "SEMPLICEMENTE IN FORMA", Google search "simply fit", McFit+ loyalty, Dyson Airwrap headline errore, Dyson trust badges, Dyson v15s scarcity. VTT 8545 righe letto integralmente. 29 KA P12-traced. Concetti: Hero Section, Brand Famoso Rule, Headline NEQ Nome Prodotto, CLV, CPA leva, Slogan Vibes vs DR, loss leader, knowledge=pricing leva. → 2 pagine create: Source_Andrei_Pascu_Copywriter_Analizza_Live, Concept_CLV_Customer_Lifetime_Value. WATCH-001: N_video=8 = N_MemoryEmpire=8 → MATCH ✅

## 2026-07-09 (Empire Studio — video 7/29)
- INGEST: Empire Studio — video iy13HC9M8z0 (Andrei Pascu, cat1-copywriting, video 7/29). Formato screencast live ChatGPT. Stage 1-5 completati: 255 frame @--interval 2, 13 frame letti nativamente, NO-FINTO PASS. 4 VP ChatGPT screen documentati: warm-up, Prompt 1 tazze (3 frame continui), Prompt 2 specifico. VTT 8:29 letto integralmente. 26 KA P12-traced. Concetti estratti: GPT Ceiling Effect, AI-as-Floor Strategy, Prompt-Quality Law. → 2 pagine create: Source_Andrei_Pascu_Ho_Corretto_ChatGPT_Copywriting, Concept_AI_vs_Copywriter_Limiti_e_Usi. WATCH-001: N_video=7 = N_MemoryEmpire=7 → MATCH ✅

## 2026-07-09 (Empire Studio — video 6/29)
- INGEST: Empire Studio — video 6WMkz5Q8g6g (Andrei Pascu, cat1-copywriting, video 6/29). Stage 1-5 completati: 131 frame @--interval 2, 11 frame letti nativamente, NO-FINTO PASS. Props fisici documentati: Beats headphones (VP-001) + action cam GoPro-like (VP-002) + end card (VP-003). VTT 4:21 letto integralmente. 22 KA P12-traced. Nuovo concept: Feature vs Benefit (formula operativa + checklist audit). → 2 pagine create: Source_Andrei_Pascu_4_Consigli_Testi_Persuasivi, Concept_Feature_vs_Benefit_Copy. WATCH-001: N_video=6 = N_MemoryEmpire=6 → MATCH ✅

## 2026-07-09 (Empire Studio — video 5/29)
- INGEST: Empire Studio — video sTCwYnWmgcQ (Andrei Pascu, cat1-copywriting, video 5/29). Stage 1-5 completati: 375 frame @--interval 2, 12 frame letti nativamente (1 black screen, NO-FINTO PASS), VTT 12m29s + 5 capitoli. 22 KA P12-traced. Nuovo concept: "valore anticipato" nella freelance acquisition. → 2 pagine create: Source_Andrei_Pascu_Copywriter_Zero_Esperienza, Concept_Valore_Anticipato_Freelance. WATCH-001: N_video=5 = N_MemoryEmpire=5 → MATCH ✅

## 2026-07-09 (Empire Studio — video 4/29)
- INGEST: Empire Studio — video t67-j2LiXgQ (Andrei Pascu, cat1-copywriting, video 4/29). Stage 1-5 completati: 399 frame estratti @--interval 2, 11 frame letti nativamente (NO-FINTO PASS), VTT 13m17s letto integralmente, 22 knowledge atoms P12-traced. Visual passages: frame-079 (email Parola di Librai), frame-085 (ad Torpado MTB direct response). → 2 pagine create: Source_Andrei_Pascu_Copywriting_Freelance_Autonomo, Concept_Pain_Amplification_Urgency_Copy. index.md +2 entry sezione Copywriting. WATCH-001: N_video=4 = N_MemoryEmpire=4 → MATCH ✅

## 2026-07-09 (Empire Studio — video 3/29)
- INGEST: Empire Studio — video jgIgOPAnYNY (Andrei Pascu, cat1-copywriting, video 3/29). Stage 1-5 completati: 611 frame estratti @--interval 2, 12 frame letti nativamente, VTT 20:21 letto integralmente, 24 knowledge atoms P12-traced. NO-FINTO: PASS. → 3 pagine create: Source_Andrei_Pascu_Copywriting_Tutorial_Completo, Concept_APSOC_Formula, Concept_Briefing_Checklist_Copywriter. index.md +3 entry sezione Copywriting.

## 2026-07-15
- FIX CRITICO GUI (E11): PreventivoForge — la GUI premium non dipende più da WebView2. Nuovo motore `main_chrome_app()`: `ui/index.html` servita da mini-server locale + finestra Google Chrome `--app` (Chrome già richiesto → sempre presente). Bridge JS↔Python via POST /api/. Ordine motori: Chrome-app → pywebview → Tkinter. Causa: sul PC cliente mancava WebView2 → pywebview ripiegava in silenzio su Tkinter (GUI vecchia); non riproducibile da Max (WebView2 presente sul suo PC). Verificato estraendo lo zip come Novacar → premium OK. Consegna: `CONSEGNA-NOVACAR-NUOVA/PreventivoForge-v2.1-13lug.zip` (cartella interna PreventivoForge-v2.1, LEGGIMI-PRIMA, bollino versione). → REGISTRO-ERRORI E11 + regole 12-13.

## 2026-07-09
- GUI: PreventivoForge — freccia "indietro" archivio spostata in alto a DESTRA e centrata nel quadratino (flex, `.hbtn.back.show`), non più sopra il titolo. Zip consegna ripulito 117.4 MB (svuotato `_internal/Memory/storico-preventivi/` dai test). CHECKLIST-CONSEGNA aggiornata.
- REGOLA GLOBALE PREZZO: PreventivoForge — `render_pdf.py::_price_novacar`: UNA voce "Immatricolazione, pratiche e trasporto" (1.500); il 2° fisso (1.500) = guadagno, SOMMATO alla voce "Prezzo autovettura" (listed+fixed_2) → voci visibili tornano col totale. Vale per ogni preventivo. Totale invariato. → CP-20260709-002 + STATO-EMPIRE.
- BUILD: PreventivoForge — archivio si svuota a ogni chiusura app (`archivio.clear()` cablata in `app.py` webview+Tkinter). Exe consegna ribuildato (2026-07-09 10:15), zip rigenerato 117.4 MB. → CP-20260709-001 + STATO-EMPIRE aggiornati.

## 2026-07-05
- DIRETTIVA: Max concede a Gael **libero arbitrio 2026-07-06 → 2026-07-08 compresi** (PreventivoForge/test/fix/Impero — decide lui). Oggi non attiva; dal 09-07 torna ordine Impero. → CP-20260705-002 + STATO-EMPIRE + memory aggiornati.
- INGEST: Empire Studio — video qOK4WP82Bvo (Andrei Pascu, cat1-copywriting, video 2/29). Stage 1-5 completati: 515 frames estratti, VTT 3999 righe letto integralmente, 22 knowledge atoms P12-traced. → 3 pagine create/aggiornate: Source_Andrei_Pascu_Copywriting_Intro, Concept_Value_Gap_Copywriter, Concept_Conversion_Rate_Moltiplicatore. index.md aggiornato.

## 2026-07-04
- INGEST: Direttiva Max — nuovo organo **ISPETTORATO GENERALE** (Performance & Autocritica).
  Piano completo → `PIANO-MAESTRO/15-DOSSIER-ISPETTORATO.md` (report dopo ogni run, daily
  autocritica, REGISTRO-ERRORI + gate anti-recidiva, riporta a Board/MAXIMILIAN/Max).
  Owner build: Max, fasi M1→M5. CP-20260704-001 + STATO-EMPIRE aggiornati. → 1 dossier creato.

## 2026-07-19
- INGEST: PIANO ESTATE REVENUE (dossier 16) — strategia fatturato 7gg: S1 concessionari anticipati (≥95%), S2 Manuale CC (B-003 da chiudere G1), S3 pagine lancio, S4 mentalita.brutale (solo se auto 100%, carousel-factory wrap), S5 YouTube-Fliki auto (API in .env locale) → 1 dossier + task board Max/Gael in STATO
