# Wiki Log — Registro operazioni

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
