# 🧠 MEMORY — Indice Maestro (Ecosistema 10, EMPIRE OS)

> **Regola memory-first (pattern #13):** questo file si carica all'INIZIO di ogni sessione
> e prima di ogni task. Dopo ogni task: checkpoint in `checkpoints/`. Una riga per voce,
> solo puntatori — il contenuto vive nei file.

## Stato corrente
- [STATO-EMPIRE.md](STATO-EMPIRE.md) — fase roadmap, lavori in corso, RIPRESA DA

## Decisioni attive (ADR)
- [ADR-001](decisions/ADR-001-empire-os-10-ecosistemi.md) — EMPIRE OS: holding di 10 ecosistemi su modello AION GROUP
- [ADR-002](decisions/ADR-002-memory-first.md) — Pattern memory-first: interroga prima, checkpoint dopo, sempre
- [ADR-003](decisions/ADR-003-migrazione-wrap-non-riscrittura.md) — Migrazione asset = wrap, mai riscrittura; sistemi attivi intoccabili finché sostituto non validato
- [ADR-004](decisions/ADR-004-github-monorepo-sync.md) — Monorepo GitHub ansjkfgheqrlg/digital-empire + sync automatico bidirezionale Max↔Gael
- [ADR-005](decisions/ADR-005-backlog-non-blocca.md) — Blocker minori → BACKLOG.md, mai fermare la costruzione; team-prezzi per le decisioni di prezzo
- [ADR-006](decisions/ADR-006-ciclo-fase-9-passi.md) — Ciclo di Fase Empire a 9 passi (metodo ufficiale, swarm obbligatorio per Max e Gael) → `PIANO-MAESTRO/10-METODO-CICLO-FASE.md`
- [ADR-007](decisions/ADR-007-piano-v2-scala.md) — **PIANO V2 Direttiva di Scala**: 1 workflow=CF Exponium, Board=workflow×10+ agenti, reparti=team+workflow CF-grade, Mandato-ecosistema, organo MAXIMILIAN → `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md`
- [ADR-008](decisions/ADR-008-catena-intestazione-controllo.md) — **Catena intestazione e controllo**: nessun artefatto orfano — ogni cosa ha proprietario+controllore+origine(FORGE)+governo(Mandato), anagrafe in `company/REGISTRO-IMPRESA.md` + `skills-map.yaml`, FORGE=ufficio anagrafe, 5-bis verifica intestazione
- [ADR-009](decisions/ADR-009-toolkit-esterni-ufficiali-forge-agent-skill.md) — **Toolkit esterni ufficiali** (copy-workflow · master-build-architecture · content-forge2.0 vendored, mai sovrascrivere col clone GitHub) + **reparto FORGE-AGENT-SKILL** istituito (officina agenti/skill, gate fas-qa-gate)

## Corpus Maximilian
- [direttiva-20260611-scala-v2](maximilian-corpus/direttiva-20260611-scala-v2.md) — prima direttiva integrale di Max (addestramento organo MAXIMILIAN; ogni futura direttiva si appende qui)

## Backlog
- [BACKLOG.md](BACKLOG.md) — cose rimandabili (token FB, prezzo manuale, team-prezzi B-003, ...)

## Checkpoint
- [CP-20260720-015](checkpoints/CP-20260720-015.md) — **MIR-5 sprint 2: retrofit `skill-cro-ricerca` / Client Research Engine** — wrap canonico 6 satelliti (master 1.625r + 7 knowledge intoccati, diff=0); **scoperta MANIFEST FANTASMA** (5 template referenziati assenti → debito D1: "il corpo vince sul manifest"); zero tool by design dichiarato; MKD 26/26=100%; GATE retro PASS 7/7; skills-map v1.6 (stats invariate); sprint 3 candidato CRO Copy Architect — sessione Claude
- [CP-20260720-014](checkpoints/CP-20260720-014.md) — **MIR-5 CAMPAGNA AVVIATA · sprint 1: retrofit `youtube-script-factory`** — da orfana ADR-008 a canonica+registrata (skills-map v1.5): wrap 6 satelliti (md master intoccato), **3 tool python estratti da markdown** (py_compile 3/3, regola deriva "md vince"), MKD 17/17=100%, PLAN+ASK, GATE retro PASS 7/7 (modalità RETROMODE inaugurata) — sessione Claude
- [CP-20260720-013](checkpoints/CP-20260720-013.md) — **MIR-9 CHIUSA: topology.md obbligatorio per team** — `FORGE-AGENT-SKILL/templates/TOPOLOGY-TEMPLATE.md` (1 pagina puntatori, nodi=7-file reali no agenti fantasma, edges con contratti, kill-criteria) + R2-bis + WF-AGENT-NEW step 6 + qa-gate p.1 + **`TOPOLOGY.md` reparto** (dogfooding: pipeline con gate finale N0→N1/N2→N3→registrazione) — sessione Claude
- [CP-20260720-012](checkpoints/CP-20260720-012.md) — **MIR-12: REVIEW APSOC SITO "Agency page" (78/100)** — audit 13 sezioni vs canone MKD → 5 P0 bloccanti (claim senza fonte Art.2, tracking 0% + schema eventi uniforme, form fake-success, GDPR, offerta doppia 15/40 min) + **ASK-PROTOCOL prima applicazione reale** (Q1-Q3 per Max); merge main (Ispettorato M1 Max) con kit rinumerato -011 (4ª collisione) — sessione Claude
- [CP-20260720-011](checkpoints/CP-20260720-011.md) — **YOUTUBE LEAD MACHINE: kit di lancio COMPLETO** (scheda Cliente d'Oro, SETUP-CANALE copy pronta, lead magnet "Analisi Gratuita" + 5 messaggi speed-to-lead, batch #1 con 6 script hook/scaletta/CTA + 2 concept copertina) — sessione Claude *(era -001→-004→-011: collisioni con pivot Aureus e con Ispettorato M1 di Max)*
- [CP-20260720-010](checkpoints/CP-20260720-010.md) — **LEAD MAGNET #2: Checklist CRO in 21 Punti** (magnet TOFU un-gated del funnel W7: 21 controlli/5 zone + scoring diagnostico + ponte CTA → Analisi Gratuita; naming Hormozi; review APSOC secondo pass 93/100 PASS; REGISTRO §3 + cross-ref magnet #1/skill/progetto) — sessione Claude
- [CP-20260720-009](checkpoints/CP-20260720-009.md) — **MIR-3 CHIUSA: ASK formale obbligatorio nei FORGE-PLAN** — `FORGE-AGENT-SKILL/workflows/ASK-PROTOCOL.md` (trigger T1-T4, max 3 domande mirate con raccomandazione+default `[ASSUNZIONE]`, replies ↳) + step ASK in WF-SKILL-NEW (4) e WF-AGENT-NEW (5) + qa-gate p.7 esteso; merge main squashed (G1 chiuso e2e, U1 slice 1, Empire Studio 10/29) con CP miei rinumerati 002→007/003→008 — sessione Claude
- [CP-20260720-008](checkpoints/CP-20260720-008.md) — **TOOLCHAIN VS CODE adottata**: scansione completa plugin (14 categorie su censimento reale 7.6k md/867 py/181 yaml) → dossier `PIANO-MAESTRO/19-TOOLCHAIN-VSCODE.md` (Tier 1-3 + 8 sconsigliati, mappa W1-W10) + `.vscode/` committato (extensions+settings: agente unico Claude Code, mai format-on-save, telemetry off) — sessione Claude *(era -003, rinumerato: collisione con verifica G1 di Gael)*
- [CP-20260720-007](checkpoints/CP-20260720-007.md) — **ADR-009: 3 toolkit esterni ufficiali** (copy-workflow vendor + review APSOC kit YouTube score→90-93; master-build-architecture → dossier 18 revisione impero 12 MIR; content-forge2.0 engine) + **nuovo reparto FORGE-AGENT-SKILL** (4 agenti, WF-AGENT/SKILL-NEW, R1-R4) + skills-map v1.2 — sessione Claude *(era -002, rinumerato: collisione con Empire Studio 10/29 di Gael)*
- [CP-20260720-006](checkpoints/CP-20260720-006.md) — **MIR RETROFIS + MKD BRAND-OFFER**: memory/ + REGISTRO-ERRORI standardizzati nei runtime W1 Outreach (OE-1..5), W4 caroselli (CE-1..4), W7 YouTube kit (YE-1..3), wrap ADR-003; MKD brand-offer da Materiale Agency (12 sezioni, ➕ marcate) → REGISTRO-IMPRESA §3, dossier 18 MIR-1/2/6/11 ✅ — sessione Claude
- [CP-20260720-005](checkpoints/CP-20260720-005.md) — **PRIMA SKILL FORGIATA DAL REPARTO: `/youtube-lead-machine`** (WF-SKILL-NEW 7/7 step: RECALL anti-doppione → MKD 25/25 atomi → kernel 118r + 6 references + evals 7 + failure-modes 8 → evals loop 3 ritocchi → GATE fas-qa-gate PASS 7/7 → skills-map v1.3 + REGISTRO §3 + wiki). Merge pivot Aureus: CP kit YouTube rinumerato -004 — sessione Claude
- [CP-20260720-004](checkpoints/CP-20260720-004.md) — **ISPETTORATO GENERALE: M1 fondamenta costruite** — `company/Ispettorato/`: registro errori empire-wide (10 voci REALI migrate), REGISTRO-REVISIONI + REGISTRO-SUCCESSI (nuovi, studia anche i successi e i cicli di correzione — "meglio al primo colpo"), KPI empire-wide; dossier 15 esteso (agente 11 revision-analyst); M3 in build (11 agenti CF-grade) — Max via Claude *(riga aggiunta in merge: mancava su main)*
- [CP-20260720-003](checkpoints/CP-20260720-003.md) — EmpireDesk G1: verifica statica del commit 85548a30 (Aureus come root), nessun difetto trovato, ancora da testare a runtime — Gael
- [CP-20260720-002](checkpoints/CP-20260720-002.md) — Empire Studio: video 10/29 andrei-pascu-001 completato (Ahp_6rHSOsU, Google Docs copywriter). Stage 3-9 chiusi (Stage 1+2 già fatti da Max l'11/07): 16 frame letti, VTT integrale, 20 KA, 2 pagine wiki, Memory Empire C-H, tracker aggiornato. RIPRESA DA video 11/29 (nRm7JLsP1bc) — Gael
- [CP-20260720-001](checkpoints/CP-20260720-001.md) — EMPIRE DESK PIVOT AREUS: U0 completato, piattaforma Aureus Agency OS importata come base app — Max
- [CP-20260719-009](checkpoints/CP-20260719-009.md) — **YOUTUBE LEAD MACHINE avviato**: ingest 7 video (5 Media Profit + Hormozi + Think Media, trascrizioni complete) → strategia operativa `Formazzione/Youtube/STRATEGIA-YOUTUBE-LEAD-MAGNET.md` (8 sezioni, piano 30gg) + 7 note video + 7 pagine wiki — sessione Claude *(era -007, rinumerato: collisione con B1 di Gael)*
- [CP-20260719-008](checkpoints/CP-20260719-008.md) — Risolta collisione reale Gael/Max su `EmpireDesk/ui/index.html` (2 redesign paralleli della stessa feature pannelli-moduli, 8 blocchi in conflitto): tenuto il design UI di Max (nav-tab), `app.py` riallineato al SUO contratto (`/api/modules`, non `/api/panels`). Preso atto: Gael non tocca più `ui/index.html` (ownership passata a Max) — Gael
- [CP-20260719-007](checkpoints/CP-20260719-007.md) — ⚠️ **Empire Desk B1: seam moduli costruito** (loader `modules/*.py` isolato, validazione schema tile anti-crash, dispatcher routes condiviso HTTP/pywebview, switcher pannelli UI + CSS per i 3 moduli di Max, fix grafico proattivo header flex). 2 bug trovati e corretti in autorevisione (EDE-6/7), 0 lanciati. NON eseguito: ambiente sessione senza Python/Node — Gael
- [CP-20260719-006](checkpoints/CP-20260719-006.md) — Risolto conflitto di sync GitHub (SYNC-CONFLICT.txt) + collisione numerazione checkpoint (002/003 rinumerati 004/005); merge REGISTRO-ERRORI EmpireDesk senza perdita dati; push riuscito, main allineato — Max
- [CP-20260719-005](checkpoints/CP-20260719-005.md) — Skill ufficiale `master-app-builder` installata in `.claude/skills/` (kernel v2.1 + Fase 0.0 pattern-mining su PreventivoForge/EmpireDesk + tie-in reparti 06a-PLATFORM L2.2/06b-FORGE L2.1; verificata presente nell'elenco skill) — Max
- [CP-20260719-004](checkpoints/CP-20260719-004.md) — ⚠️ **Empire Desk v0.1: P1-P3 costruiti** (shell 3-motori Chrome-app/pywebview/Tkinter, 8 tile, subprocess reale con log live; 3 bug reali trovati+corretti in revisione statica: sys.executable da frozen, WinError193 su .bat, pause-hang senza stdin=DEVNULL; trovato ma NON toccato EDE-2 path hardcoded nei bat Outreach — ADR-003). P4 selftest/build bloccato: ambiente sessione senza Python/Node — Gael
- [CP-20260719-003](checkpoints/CP-20260719-003.md) — **EMPIRE DESK: divisione lavoro metà/metà Max↔Gael** + planning aggiornato (dossier 17 §5, Half A dati/business Max · Half B core/runtime Gael) — Max
- [CP-20260719-002](checkpoints/CP-20260719-002.md) — **ADR-008 catena intestazione e controllo**: ogni artefatto ha proprietario+controllore+origine+governo; `REGISTRO-IMPRESA.md` + `skills-map.yaml` v1.1 — Max
- [CP-20260719-001](checkpoints/CP-20260719-001.md) — **V2-2 Lotto 3 COMPLETATO**: 5 dossier V2 (05-MULTI-BUSINESS-V2 + split 06-CORE in 06a-Platform/06b-Forge/06c-Intelligence/06d-Operations), ~229 agenti progettati, gate+review pass, V2-INDEX.md aggiornato — Gael
- [CP-20260711-002](checkpoints/CP-20260711-002.md) — 🏁 **01-AGENCY CHIUSO 10/10** (182 file, 74 agenti, 28 WF; batch-3 A7/A8/A9/A10; il gate ha trovato+chiuso 2 difetti veri: namespace divergente → `NAMESPACE.md` canonico `agency/a<N>`, 6 README v1 stantii → riscritti; RETRO: write-early + idempotenza sospesa sui residui v1) — Max
- [CP-20260703-001](checkpoints/CP-20260703-001.md) — **Novacar: GUI App PREMIUM (pywebview HTML/CSS)** (Gael, priorità #1 Max): `ui/index.html` luxury slate+argento (font premium, gradienti/ombre/hover, log colorato), `app.py` pywebview + bridge + fallback Tkinter, titolo "Novacar srl", +glossario Sitzeinstellung. GUI premium confermata WebView2 (dev+.exe). PDF NON toccato (ownership Max). — Gael
- [CP-20260702-003](checkpoints/CP-20260702-003.md) — **Novacar: PDF modello Novacar + Gate IMG/R + App .exe COSTRUITA** (Gael): template rifatto sul modello (R-01…R-14), `gate_img`+`gate_regole`+`regole-check.json`, 2 agenti QA (qa-immagini, qa-regole-checker), fix logo su bianco. Selftest 6/6 gate verdi + 14/14 regole OK; `PreventivoForge.exe` costruito e validato (dealer Novacar, PDF via cdp). — Gael
- [CP-20260702-002](checkpoints/CP-20260702-002.md) — **Prof Autocad: App Desktop (GUI) + motore PDF .exe-ready** (Gael): `app.py` Tkinter argento wrappa run.py, `avvia-app.bat`, `build_exe.bat`+spec PyInstaller, `render_pdf` motore cdp/Chrome (no Playwright, flag remote-allow-origins). Selftest 4 gate verdi, PDF cdp-chrome. — Gael
- [CP-20260701-003](checkpoints/CP-20260701-003.md) — **Prof Autocad: scraping LIVE mobile.de RISOLTO (Chrome+CDP bypassa Akamai) + parser su `__INITIAL_STATE__` + prova reale GLA** (EXIT 0, 4 gate verdi, 47.490→51.915 €, PDF 810KB foto vere) — Max
- [CP-20260701-002](checkpoints/CP-20260701-002.md) — **Prof Autocad: PreventivoForge gate wiring + test END-TO-END** (Max): gate B/C/D in run.py + fix UTF-8; run --manual GLA → PDF 60KB, 4 gate verdi, 33.900→37.917 €. Live scrape bloccato solo da qui (anti-bot). — Max
- [CP-20260701-001](checkpoints/CP-20260701-001.md) — **CLIENTE Prof Autocad · PreventivoForge Half B COMPLETA** (S3 translate+copy, S5 PDF Playwright, QA Gate A/B/C/D, R3/R5/R6, 6 agenti CF-grade/42 file; test run.py --manual BMW 320d → PDF 63KB, 4 gate ALL GREEN; ADR-003 rispettato, €0 API) — Gael
- [CP-20260630-003](checkpoints/CP-20260630-003.md) — **Prof Autocad: PreventivoForge Half A COMPLETA** (fondamenta: 4 agenti CF-grade 7-file + R1/R2/R4 + orchestration + CLAUDE.md cliente) — Max
- [CP-20260630-002](checkpoints/CP-20260630-002.md) — **CLIENTE Prof Autocad: PreventivoForge Half A FATTA** (mobile.de DE → preventivo IT PDF, prezzo ×1.03+1500+1500, multi-tenant; scraper/parser/pricer/regia/skill `/preventivo-auto`, testato; Half B → Gael handoff) — Max
- [CP-20260623-001](checkpoints/CP-20260623-001.md) — STEP 5: **01-AGENCY batch-2** (A4-Delivery+A5-Copy+A6-Marketing CF-grade: 51 file, 21 agenti, 9 WF; A5 riusa Gate Bibbia A2 pattern-6; gate verde, 5-bis APPROVA → 01-AGENCY 6/10) — Max
- [CP-20260622-002](checkpoints/CP-20260622-002.md) — STEP 5: **01-AGENCY batch-1** (A1+A2+A3 CF-grade: 58 file, 27 agenti, 10 WF; A2 wrappa runtime outreach LIVE ADR-003; gate verde, 5-bis APPROVA) — Max
- [CP-20260622-001](checkpoints/CP-20260622-001.md) — **02-INFO-BUSINESS CHIUSO** (5/5 reparti V2: 94 file, 42 agenti, 12 WF; +34 file = 6 cartelle std/reparto + 4 WF; gate verde, 5-bis APPROVA) — Max
- [CP-20260619-016](checkpoints/CP-20260619-016.md) — **03-CONTENT-FACTORY COMPLETO** (9/9 reparti, 158 file, 71 agenti, 28 WF): CF-R8 Apprendimento (ULTIMO) + chiusura ecosistema, 5-bis APPROVA — Gael
- [CP-20260619-015](checkpoints/CP-20260619-015.md) — STEP 5: 03-CONTENT-FACTORY CF-R7 Pubblicazione & Distribuzione costruita CF-grade (18 file, 8 agenti, 4 WF, wrap orchestratori publish, review umana) — Gael
- [CP-20260619-014](checkpoints/CP-20260619-014.md) — STEP 5: 03-CONTENT-FACTORY CF-R6 QA & Gate costruita CF-grade (17 file, 8 agenti, 3 WF, indipendente dalla produzione) — Gael
- [CP-20260619-013](checkpoints/CP-20260619-013.md) — STEP 5: 03-CONTENT-FACTORY CF-R5 Visual & Design / Caroselli costruita CF-grade (20 file, 10 agenti, 4 WF, wrap carousel-factory) — Gael
- [CP-20260619-012](checkpoints/CP-20260619-012.md) — STEP 5: 03-CONTENT-FACTORY CF-R4 Produzione Testuale costruita CF-grade (18 file, 8 agenti, 4 WF, confine CF/MARKETING) — Gael
- [CP-20260619-011](checkpoints/CP-20260619-011.md) — STEP 5: 03-CONTENT-FACTORY CF-R3 Produzione Video costruita CF-grade (20 file, 10 agenti, 4 WF, wrap hf/heygen-studio, dry-run Art.4.3) — Gael
- [CP-20260619-010](checkpoints/CP-20260619-010.md) — STEP 5: 03-CONTENT-FACTORY CF-R2 Brand-Kit Registry costruita CF-grade (14 file, 6 agenti, 2 WF, multi-tenant) — Gael
- [CP-20260619-009](checkpoints/CP-20260619-009.md) — STEP 5: 03-CONTENT-FACTORY CF-R1 Strategia & Brief costruita CF-grade (17 file, 8 agenti, 3 WF, 0 stub) — Gael
- [CP-20260619-008](checkpoints/CP-20260619-008.md) — STEP 5: 03-CONTENT-FACTORY CF-R0 Director costruita CF-grade (15 file, 7 agenti, 2 WF, contratto ordine multi-tenant) — Gael
- [CP-20260618-007](checkpoints/CP-20260618-007.md) — **04-MARKETING COMPLETO** (6/6 reparti, 114 file, 44 agenti): L2.1 Copywriting wrap motore attivo + chiusura ecosistema, 5-bis APPROVA — Gael
- [CP-20260618-006](checkpoints/CP-20260618-006.md) — STEP 5 batch 3: L2.4 Analytics costruita CF-grade (18 file, 7 agenti, 3 WF, loop §4b) — Gael
- [CP-20260618-005](checkpoints/CP-20260618-005.md) — STEP 5 batch 2: L2.3 Email & Lifecycle costruita CF-grade (19 file, 7 agenti, 4 WF, 0 stub, PII Art.7.2) — Gael
- [CP-20260618-004](checkpoints/CP-20260618-004.md) — STEP 5 batch 2: L2.2 Advertising costruita CF-grade (19 file, 8 agenti, 3 WF, 0 stub) — Gael
- [CP-20260618-003](checkpoints/CP-20260618-003.md) — STEP 5 batch 1: L2.5 Brand & Creative Strategy costruita CF-grade (17 file, 6 agenti, 3 WF, 0 stub, Mandato Art.2) — Gael
- [CP-20260618-002](checkpoints/CP-20260618-002.md) — STEP 5 batch 1: L2.6 Conversion Architecture costruita CF-grade (17 file, 6 agenti, 3 WF, 0 stub) — Gael
- [CP-20260618-001](checkpoints/CP-20260618-001.md) — STEP 4-heavy CHIUSO: CFO completato → Board C-Suite V2 completa 7/7 (~70 agenti, 5-bis APPROVA) — Max
- [CP-20260617-003](checkpoints/CP-20260617-003.md) — STEP 4-heavy batch 3: figure Board CMO + CRO costruite (42 file, 20 agenti, 5-bis Maximilian APPROVA) — Gael
- [CP-20260617-002](checkpoints/CP-20260617-002.md) — STEP 4-heavy batch 2: figure Board CTO + COO costruite (42 file, 20 agenti, 5-bis Maximilian APPROVA) — Gael
- [CP-20260617-001](checkpoints/CP-20260617-001.md) — STEP 4-heavy batch 1: figure Board CEO + Chief-Forge costruite (42 file, 20 agenti, struct-gate + 5-bis Maximilian APPROVA) — Gael
- [CP-20260616-010](checkpoints/CP-20260616-010.md) — STEP 4(c): blueprint Board via ARCHITETTURA (8 file, 70 agenti progettati, primo uso reale WF-ARCH-DESIGN) — Max
- [CP-20260616-009](checkpoints/CP-20260616-009.md) — STEP 3: organo MAXIMILIAN (15 file, review-gate 5-bis + maximilian-standard-gate eseguibile, gate+review PASS) — Max
- [CP-20260616-008](checkpoints/CP-20260616-008.md) — STEP 2 Genesi Core: FORGE completa (34 file, Mappa-Motori 15 motori reali, gate+review PASS) — Max
- [CP-20260616-007](checkpoints/CP-20260616-007.md) — STEP 1 Genesi Core: organo ARCHITETTURA costruito (dossier 14 + 30 file, gate+review PASS) — Max
- [CP-20260616-006](checkpoints/CP-20260616-006.md) — V2-2 lotto 2: dossier v2 mega-reparti CONTENT-FACTORY (5 livelli/76 agenti) + INFO-BUSINESS (48 agenti) — Gael
- [CP-20260616-005](checkpoints/CP-20260616-005.md) — V2-2 lotto 1: dossier v2 AGENCY (10 reparti/75 agenti) + MARKETING (6 reparti/49 agenti) — Gael
- [CP-20260616-004](checkpoints/CP-20260616-004.md) — V2-2: dossier MANDATO-ecosistema (PIANO-MAESTRO/13) — blueprint governo per V2-5 — Gael
- [CP-20260616-003](checkpoints/CP-20260616-003.md) — V2-2 AVVIATA: dossier MAXIMILIAN (PIANO-MAESTRO/12) — blueprint organo per V2-3 — Gael
- [CP-20260616-002](checkpoints/CP-20260616-002.md) — F1-bis COMPLETATO: gate verde (0 vuote, 0 magri, 317 file) + review pass; prossima V2-2 — Gael
- [CP-20260616-001](checkpoints/CP-20260616-001.md) — Fix collisione case-insensitive 06-PLATFORM/Reparti (5 doppioni MAIUSCOLO rimossi, contenuto arricchito preservato) — Gael
- [CP-20260613-001](checkpoints/CP-20260613-001.md) — Fix critico Empire Studio: RULES.md + agenti verification aggiornati + run Andrei Pascu avviata
- [CP-20260611-008](checkpoints/CP-20260611-008.md) — PIANO V2 Direttiva di Scala codificata (ADR-007) + corpus Maximilian + pivot roadmap V2
- [CP-20260611-007](checkpoints/CP-20260611-007.md) — F4 GATE VERDE: ciclo dry-run end-to-end CY-20260611-001 (Gael) — gate PASS 113/113
- [CP-20260611-006](checkpoints/CP-20260611-006.md) — F4 B2 wrap 4 WF outreach come L3 + agency-trace.ps1 (Gael) — gate PASS 107/107
- [CP-20260611-005](checkpoints/CP-20260611-005.md) — Metodo 9 passi (ADR-006) + handover a Gael; F1-bis arricchimento a metà (session limit)
- [CP-20260611-004](checkpoints/CP-20260611-004.md) — F4 AGENCY live B1 completato (Gael) — gate PASS 97/97
- [CP-20260611-003](checkpoints/CP-20260611-003.md) — F3 Migrazione asset completato (Gael) — gate PASS 70/70
- [CP-20260611-002](checkpoints/CP-20260611-002.md) — F2 Backbone operativo completato (Gael) — gate PASS 59/59
- [CP-20260611-001](checkpoints/CP-20260611-001.md) — F1 Scaffolding EMPIRE OS completato (Gael) — gate PASS 92/92
- [CP-20260610-001](checkpoints/CP-20260610-001.md) — Prodotto PIANO-MAESTRO completo (10 dossier, swarm 7 agenti + conductor)
- [CP-20260610-002](checkpoints/CP-20260610-002.md) — GitHub monorepo + sync: LIVE (push 966 MiB + motore testato)
- [CP-20260610-003](checkpoints/CP-20260610-003.md) — Skill `empire-context` creata (project-level, condivisa con Gael via repo)

## Piani
- [PIANI.md](plans/PIANI.md) — registro piani versionati (→ PIANO-MAESTRO/)

## Sessioni
- [session-20260610](sessions/session-20260610.md) — produzione Piano Maestro EMPIRE OS

## Template (usare SEMPRE questi)
- [CP-template](templates/CP-template.md) · [ADR-template](templates/ADR-template.md) · [session-template](templates/session-template.md)

## Cartelle operative
- `tasks/<ecosistema>/` — log task per ecosistema (01-agency … 10-memory)
- `state/<progetto-id>/` — state.json + trace.jsonl per progetto/ordine in corso
- `audit/` — audit trail modifiche e backup refs
