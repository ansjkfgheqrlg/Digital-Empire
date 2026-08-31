# Wiki Log — Registro operazioni

## 2026-08-29 (Empire Studio — cs2online: sezione "AI - Le basi" COMPLETA 9/9, Claude)
- INGEST: proseguito in autonomia dopo l'ordine Max (Lezione 16 + Bonus 1-6), completate le
  lezioni mancanti della prima sezione: Lezione 7 (Diversi tipi di contesto, teoria — gerarchia
  vision/obiettivo/target/task), Lezione 8 (Context engineering, teoria — tesi "expertise per
  l'input, non solo l'output"), Lezione 9 (Come dare contesto alle AI, pratica — 4 modi:
  allega tutto/allega rilevante/Cowork/Projects, struttura cartelle confermata identica a
  lezione 6). → 3 pagine nuove sources/Source_CS2_Lezione_0{7,8,9}_*.md.
  **Sezione "AI - Le basi" ORA COMPLETA al 100% (9/9 lezioni).**
- ENRICHMENT: nessuna nuova patch — tutti i pattern trovati (garbage-in-garbage-out, 6a-7a
  variante) erano già confermati/applicati nelle sessioni precedenti dello stesso corso.
  Stato: 17/40 lezioni cs2online completate. Tracker: `MASTER-RUN-TRACKER.md`.

## 2026-08-29 (Empire Studio — cs2online: ordine Max completato, Lezione 16 + Bonus 1-6, Claude)
- INGEST: completato l'ordine di lavoro richiesto da Max ("vai a lezione 16, poi tutte le Bonus,
  fermati quando hai finito"). Lezioni processate in sequenza: 16 (Copy primary text ads),
  Bonus 1 (Automatizzare processi, teoria), Bonus 2 (Advertising report, scoperto uso reportlab
  già presente in `market-report-pdf` — convergenza indipendente), Bonus 3 (Collegare Claude a
  qualsiasi cosa — MCP/Connectors/Zapier), Bonus 4 (Claude Skills — valida esternamente il
  formato skill già usato da DE), Bonus 5 (Projects dentro Cowork), Bonus 6 (Automatizzare
  processi con skills — lezione capstone, SKILL.md reale "sviluppo-preventivo" trascritto per
  intero, gap trovato in `beast-preventivi` ma non applicato per anti-overfitting).
  → 6 pagine nuove (sources/Source_CS2_Lezione_16_*.md, sources/Source_CS2_Bonus_0{3,4,5,6}_*.md).
- ENRICHMENT: 1 patch reale (lezione 13, sessione precedente, voice-of-customer YouTube —
  già loggata). Nessuna nuova patch in questa sessione: tutti i gap trovati (Bonus 6 pattern
  refuse-if-missing-data) sono fonte singola/interna al corso, propriamente non applicati per
  regola anti-overfitting DE.
  Stato completo: 14/40 lezioni cs2online fatte. Tracker: `MASTER-RUN-TRACKER.md`.

## 2026-08-29 (Empire Studio — cs2online salta a "AI per copywriting", PATCH reale skill, Claude)
- INGEST: su richiesta Max, saltate lezioni 7-12 del run `andrei-pascu-cs2online-001`, priorità
  spostata su sezione "AI - per copywriting". Lezione 13 ("Come faccio la ricerca di copywriting
  con l'AI") completata: video 27:14 min, 38 frame visionati nativamente, demo end-to-end su
  cliente reale (Simone Ferretti/SoundBox Studio: ClickUp → Gemini transcript → Claude Project →
  Perplexity parallelo → MarkEdit). → sources/Source_CS2_Lezione_13_Ricerca_Copywriting_AI.md.
- ENRICHMENT: **prima convergenza cross-run** del progetto Andrei Pascu — tecnica "ricerca
  voice-of-customer da recensioni YouTube" confermata 3 volte indipendenti (2 video YouTube del
  run `andrei-pascu-001` + questa lezione del corso a pagamento). **Patch reale applicata** a
  `C:\Users\Utente\.claude\skills\copywriting\SKILL.md`, sezione "Customer Language Over Company
  Language", con fonte dichiarata inline.

## 2026-08-27 (Empire Studio — NUOVO RUN corso a pagamento Claude Speedrun 2, Claude)
- INGEST: avviato run `andrei-pascu-cs2online-001` — corso membership a pagamento di Andrei Pascu
  (andrei-copy.com/cs2online, distinto dai video YouTube già coperti in `andrei-pascu-001`).
  Login autenticato via Playwright, 40 lezioni mappate (7 sezioni). Regola nuova di Max: solo
  lezioni pratiche fanno frame-by-frame, lezioni teoriche archiviano testo/trascrizione/risorse.
  Lezioni 1-6 completate (29/06 + LEZIONE 6 = prima PRATICA del run: video scaricato, 43 frame
  visionati nativamente su segmenti demo Excalidraw/Finder/MarkEdit/VS Code/Claude.ai, workflow
  PDF→JSON per brand guidelines documentato per intero). Pipeline + Memory Empire verificati
  per tutte. → 6 pagine sources/Source_CS2_Lezione_0{1..6}_*.md.
  ⚠️ Anomalia: skill `prompt-engegniring-skill` elencata nel sistema ma non trovata su disco —
  segnalata a Max, non risolta. Tracker: `empire-studio/runs/andrei-pascu-cs2online-001/MASTER-RUN-TRACKER.md`.

## 2026-08-26 (Piano editoriale 70 video/30gg/3 strategie @Legamidiamore CHIUSO, Claude)
- UPDATE: `entities/Entity_Legami_dAmore_Channel.md` — piano editoriale mensile completo:
  70 video reali, 3 strategie (A/B/C) mappate 1:1 su 3 canali competitor verificati con
  scraping fresco oggi (2 dei 6 storici risultati fuori nicchia, esclusi). Deliverable PDF
  20 pagine + calendario MD + dati JSON/CSV in `YOUTUBE-AUTOMATION-FACTORY/`. Dettaglio:
  `company/Memory/checkpoints/CP-20260826-003.md`.

## 2026-08-26 (Empire Studio — cat2-marketing AVVIATO, Livello 2 confermato da Max, Claude)
- Max ha confermato via AskUserQuestion di procedere su Livello 2 (cat2-cat7, ~52 video curati),
  sequenziale nel thread principale, senza fermate intermedie fino a fine budget/scope. URL siti e
  corso a pagamento di Andrei Pascu ancora NON forniti — restano bloccanti per quella fase separata.
- INGEST: video 1/cat2 (`VYyIF1r6tkw`, "The 2 most used funnels in social marketing", 5m36s) —
  talking-head + lavagna digitale, 10/168 frame campionati (VTT integrale letto per intero). 9 KA,
  4 pattern. Prima connessione diretta del run con la skill `copy-workflow/skills/funnel-designer`
  (mai toccata in cat1): ROAS e soglie prezzo già coperti in dettaglio, nessuna patch necessaria.
  1 gap reale registrato come PROPOSTA (non patchato, fonte singola, anti-overfitting): diagnosi
  "funnel di contatti come stampella per prodotto/copy debole" mancante in `funnel-economics.md`
  sezione "Segnali di Funnel Rotto".
- INGEST: video 2/cat2 (`hnPa2zspu3k`, "L'ordine del funnel cambia tutto", 33s) — reel rapid-fire,
  17/17 frame (coverage 100%). 6 KA, 3 pattern: 5 domande "cosa viene prima?" su step funnel, ordine
  come vincolo strutturale non convenzione. Nessuna patch, contenuto già implicito in `funnel-designer`.
- INGEST: video 3/cat2 (`8Pf7d57Q0Jk`, "Come generare contatti con le ads", 13m58s) — consulenza
  reale con cliente (Vasco, fotovoltaico), ROAS ~15 reale. 10/419 frame campionati, VTT processato
  con script dedup locale per efficienza. 14 KA, 5 pattern — il più denso di cat2 finora. 3 patch
  reali applicate: `ads/SKILL.md` (3-Tier Campaign Lifecycle Esperimento/Evolvo/Awareness + criterio
  spegnimento=ritorno), `ads/references/audience-targeting.md` (Content-Based Targeting), `lead-magnets/SKILL.md`
  (lead magnet problema adiacente).

## 2026-08-26 (Empire Studio — cat1-copywriting COMPLETATO 29/29, esecuzione sequenziale ininterrotta, Claude)
- Continuazione diretta del blocco precedente (video 21-24), su richiesta esplicita di Max di non
  fermarsi e completare l'obiettivo in modo credit-efficient. Completati i restanti 5 video del
  run senza interruzioni: 25, 26, 27, 28, 29.
- INGEST: video 25/29 (`uqa06rlgmj4`, "Come migliorare con gli hook (1 consiglio)", 57s) — street
  interview reale, 29/29 frame. 8 KA, 3 pattern. Nota di cautela: la sotto-tecnica "citazione di
  ricerca senza fonte" (KA-06) è in attrito diretto col gate anti-clichè esistente (video 11) —
  segnalata, nessuna patch (il gate esistente è già corretto).
- INGEST: video 26/29 (`eze4oqwb6aw`, "Sono un copywriter, è ovvio che...", 26s) — montaggio
  personal branding, 13/13 frame. 3 KA (il più leggero del run fino a quel punto) — contenuto di
  formato/branding, non tecnica di copy per clienti.
- INGEST: video 27/29 (`-zUDxSdaKRY`, "6 livelli di tono di voce", 25s) — stessa frase ripetuta 6
  volte con delivery diversa, badge onscreen. 13/13 frame. 7 KA, 3 pattern — primo video del run
  su delivery vocale/fisica, dominio scoperto senza skill DE dedicato.
- INGEST: video 28/29 (`_yUzEe29aTQ`, "copy.exe - adesso disponibile", 2m38s) — funnel lancio
  evento live, 10/79 frame campionati. 7 KA, 4 pattern: segmentazione pubblico a 4 tier con
  posizionamento esplicito, seconda conferma della tesi "AI non sostituisce" (video 21).
- INGEST: video 29/29 (`6ITBjfPQg3I`, "scrittore professionale di PDF", 4s — il più corto del run)
  — formato meme "Poi:", 2/2 frame. 2 KA.
- **🎉 cat1-copywriting COMPLETATO: 29/29 (100%).** Tutti i video hanno pipeline + Memory Empire (4
  file ciascuno) + pagina wiki Source completi e verificati su disco. MASTER-RUN-TRACKER,
  STATO-EMPIRE, wiki/index.md aggiornati. Segnalazione aperta non risolta: tensione video
  24/`beast-preventivi` (AP-05 vs breakdown prezzi) — da riportare a Max. Prossimo: decisione su
  se procedere con cat2-cat7 curati (Livello 2 del piano NERVE-SOLVE a 2 giorni) o chiudere qui.

## 2026-08-26 (Empire Studio — cat1-copywriting a 24/29, esecuzione sequenziale come da piano NERVE-SOLVE, Claude)
- Continuazione del piano 2 giorni: solo esecuzione sequenziale nel thread principale (nessun batch
  Agent-tool), come deciso il 2026-08-24/25 per evitare il limite di spesa.
- INGEST: video 21/29 (`wTpfKuHJhOE`, "Hormozi si scrive i copy da solo", 47s) — pipeline completa.
  24/24 frame (coverage 100%). 6 KA, 4 pattern. Nessuna patch (contenuto di posizionamento/mindset,
  non tecnica operativa).
- INGEST: video 22/29 (`k_DXsUCIkr8`, "Il vero script DI VENDITA the wolf of wall street", 54s) —
  pipeline completa. 27/27 frame. 5 KA, 4 pattern: script storico Stratton Oakmont, validazione +
  yes-ladder invece di confutazione dell'obiezione — dominio conversazionale, fuori scope per
  `cro-copy-architect` (nessuna patch).
- INGEST: video 23/29 (`NydMBZ2nUTE`, "Copione Wolf of Wall Street", 61s) — stessa fonte del video
  22, estratto diverso (verificato non duplicato). 31/31 frame. 7 KA, 4 pattern: seconda conferma
  indipendente del pattern yes-ladder + nuovo pattern "restringere progressivamente la richiesta".
- INGEST: video 24/29 (`EBU57iVAutA`, "Se scrivi QUESTO nel tuo preventivo NON venderai", 8m46s, 5
  capitoli ufficiali) — pipeline completa. 11/263 frame campionati sui capitoli. 16 KA, 4 pattern —
  **scoperta rilevante**: rivela lo skill DE esistente `beast-preventivi`, molto più maturo su
  questo stesso dominio. La maggior parte del video CONFERMA quello skill (specialmente "mostralo
  in call" e "silenzio post-prezzo", quasi identici). **Tensione reale trovata e segnalata, non
  risolta automaticamente**: la Regola 4 del video (breakdown prezzi per componente su servizi
  complessi) è in apparente contraddizione con l'anti-pattern AP-05 di `beast-preventivi`
  ("preventivo formato fattura" = bloccante). Dettaglio e ipotesi di riconciliazione (non
  verificata) in `memory-empire/knowledge/EBU57iVAutA/enrichment-report.md`.
- RISULTATO: cat1-copywriting **24/29 completati** (5 rimanenti: 25-29). MASTER-RUN-TRACKER,
  STATO-EMPIRE, wiki/index.md aggiornati. Prossimo: video 25 (`uqa06rlgmj4`).

## 2026-08-25 (Empire Studio — cat1-copywriting completato a 20/29, piano 2 giorni NERVE-SOLVE, Claude)
- CONTESTO: Max ha chiesto un piano "one-shot" per finire l'intera missione (~81 video curati) in
  2 giorni. Applicato NERVE-SOLVE (D2): identificato che il vincolo dominante è il limite di spesa
  account (colpito 2 volte in <24h, sempre dentro Agent-tool paralleli, mai nel thread principale
  sequenziale) — dichiarata onestamente l'impossibilità di garantire "100% certo" senza sapere se
  il limite è mensile-esaurito o a finestra ricorrente (solo Max può verificarlo). Piano a 2 livelli:
  Livello 1 (quasi certo) = cat1 completo; Livello 2 (stretch) = cat2-7 secondo budget disponibile.
  Decisione: STOP batch paralleli, solo esecuzione sequenziale da qui in avanti.
- INGEST: video 18/29 (`VbxTgp_fz8Y`, "Revisione copy oF girl", 82s) — completato in sessione
  sequenziale (video-analysis.md già scritto da batch 2, Memory Empire + wiki costruiti da zero).
  41/41 frame (coverage 100%). 10 KA, 4 pattern. Terza conferma nel run del Pain Point Implicito;
  prima volta con "APSOC" mostrato letteralmente a schermo nel materiale sorgente esterno.
- INGEST: video 19/29 (`3zJpI8-7TW4`, "Pulsanti che vendono: ecco come fare i CTA", 7m14s) —
  pipeline completa da zero (solo Stage 1-2 fatti dal batch 2). 13/218 frame campionati. 17 KA,
  5 pattern — primo video del run focalizzato solo su CTA, con guest expert (Gaia, designer).
  Enrichment applicato: 2 patch a `cro-copy-architect/framework-apsoc-operativo.md` (formula CTA
  superficiale/profondo + meccanismo; design visivo del pulsante — primo contenuto UI/UX nello
  skill, con dato quantitativo ghost-button marcato DA VERIFICARE).
- VERIFICATO: video 20/29 (`IYd-VOngDog`) risultava già completo per intero (pipeline+ME+wiki) da
  un agente del batch 2 paralleli del 2026-08-24, sopravvissuto al limite di spesa prima di essere
  interrotto — verificato su disco, aggiunto a index.md (non ancora fatto in precedenza).
- RISULTATO: cat1-copywriting **20/29 completati** (9 rimanenti: 21-29). MASTER-RUN-TRACKER,
  STATO-EMPIRE, wiki/index.md aggiornati. Prossimo: video 21 (`wTpfKuHJhOE`, Hormozi writes his
  own copy), poi 22-29, poi cat2-cat7 curati.
## 2026-08-27 (task SECONDARIE W1 — infrastruttura Impero, Claude)
- Settimana 1 chiusa **6/6** (3 primarie + 3 secondarie).
- TASK-MEMORY-SYNC-W1: nuovo controllo pre-commit (`.githooks/`) che BLOCCA le collisioni
  di ID checkpoint e i CRLF nella memoria. Gate dimostrato con una collisione vera su due
  branch: `git commit exit = 1`. Scoperto che il fix di luglio non veniva usato perche
  `empire mem write` era rotto (`No module named yaml`), non per pigrizia.
- TASK-GITLFS-W1: **ADR-013** — gitignore mirato + guard 5MB, NON Git LFS. Il 70% dei 3,1 GB
  di repo sono PNG, e il motore della crescita sono le copertine KDP (~15 MB a libro), non
  gli screenshot come diceva B-008.
- TASK-ARENA-SESSION-W1: `shared/arena_session.py`, un solo motore di sessione per caroselli
  e arena_thumbnail (run reali su entrambi). Sbloccato il Ramo D dei caroselli, che moriva
  all'import su `playwright_stealth`.
- Nuova pagina: `concepts/Concept_Guardrail_Che_Si_Fanno_Rispettare.md` — il principio
  ricavato: una regola che dipende dalla buona volonta non e un controllo.


## 2026-08-27 (TASK-PUBLISHER-W1 — workflow di pubblicazione consolidato, Claude)
- INGEST: `Workflow pubblicazione automatica/` documentato per la prima volta in wiki →
  1 pagina creata (`tools/Tool_Workflow_Pubblicazione_Automatica.md`).
- Nuovo comando unico `pubblica.py`: una cartella di caroselli già pronti → dry-run
  verificato (default) o pubblicazione reale con `--live`. Gate chiuso sul ramo dry-run:
  6 slide + caption validate, canale dedotto, browser reale su instagram.com, exit 2
  (PASS PARZIALE — manca solo il login una tantum). Nessun post reale creato.
- Verifica onesta dello stato del folder: `push_social.py` era una SIMULAZIONE dichiarata
  obbligatoria dal CLAUDE.md locale, `main_orchestrator.py` non parte proprio, e il
  `publish()` di Instagram ingoiava ogni eccezione. Tutto documentato in
  `DIAGNOSI-PUBLISHER.md` + backlog B-023..B-027, invece di far finta che funzioni.
- Collegamento reale con [[Progetto_Preventa_Carousel]]: la cartella pubblicata è
  l'output di TASK-CAROSELLI-W1 chiuso lo stesso giorno.


## 2026-08-24 (Empire Studio — batch 1 chiuso: video 15/16/17 completati in ripresa, Claude)
- INGEST: video 15/29 (`yX0XZh2PSYo`, "Merge Tag nell'email marketing", 91s) — completato:
  mancava solo `enrichment-report.md` (video-analysis.md e wiki page già presenti da batch 1).
  46/46 frame (coverage 100%). 7 KA, 3 pattern. Enrichment applicato: patch a
  `emails/copy-guidelines.md` (fallback chaining generalizzato oltre il nome).
- INGEST: video 16/29 (`L5_Z63nxXjI`, "Ho rivisto i VOSTRI copy", 11m55s) — Memory Empire
  completo (4 file) + pagina wiki Source, partendo dal video-analysis.md già scritto dal batch 1.
  20/358 frame campionati (coverage 100% dei 6 copy mostrati). 19 KA, 4 pattern — il più denso
  del run cat1 fino a quel punto. Enrichment applicato: patch a
  `cro-copy-architect/pattern-persuasione-cro.md` (nota scarsità/registro brand di lusso).
- INGEST: video 17/29 (`Pv5uzIxp96U`, "Correggo i vostri copy", 33m00s) — pipeline completa da
  zero (Stage 1-2 erano gli unici già fatti dal batch 1): video-analysis.md scritto da transcript
  + 13/991 frame campionati, poi Memory Empire completo + pagina wiki Source. 24 KA, 5 pattern —
  il più denso del run cat1. Conferma indipendente della REGOLA 1 APSOC ("mai soluzione in
  headline") già esistente nel framework DE. Enrichment applicato: patch a
  `cro-copy-architect/pattern-persuasione-cro.md` (ancoraggio multi-livello / tre scatole).
- CHIUSURA BATCH 1: video 14-17/29 tutti completi (14 dal batch parallelo del 2026-08-23, 15-17
  completati in questa sessione di ripresa). cat1-copywriting: 17/29 completati. Checkpoint di
  chiusura: `company/Memory/checkpoints/CP-20260824-001.md` (verificare numerazione prima di
  scrivere).

## 2026-08-23 (Empire Studio — batch 1 paralleli: limite spesa colpito, video 14/29 completo, seconda collisione checkpoint riparata, Claude/Max)
- INGEST: video 14/29 (`nP4ojCzvjr8`, "L'email marketing dal POV dei lettori", 28s) completato
  da un agente parallelo — 14/14 frame letti, 6 KA, nessun concept nuovo (motivato). 1 pagina
  Source nuova.
- ESITO BATCH: lanciati 4 agenti paralleli (video 14-17), solo 1 completato per intero — gli
  altri 3 terminati a metà per limite di spesa mensile dell'account (non un problema di
  architettura: zero collisioni sui file condivisi tra i 4 agenti, isolamento verificato).
  Stato esatto di ripresa per video 15/16/17 in `MASTER-RUN-TRACKER.md` e
  `company/Memory/checkpoints/CP-20260823-010.md`.
- COLLISIONE CHECKPOINT (2ª di oggi, causa diversa): `CP-20260823-001.md` sovrascritto da
  un'altra sessione parallela (contenuto Fliki/YouTube non correlato) — riparato: originale
  ripristinato da git history, contenuto Fliki spostato in `CP-20260823-009.md`. Nessun
  contenuto perso.
- WATCH-001: N_video=14 (solo video 14 pienamente confermato Memory Empire completo in questo
  passaggio; 15/16/17 in stato intermedio, non ancora contati). Checkpoint: CP-20260823-010.

## 2026-08-23 (Empire Studio — Andrei Pascu cat1-copywriting video 13/29 chiuso, avvio batch parallelo, Claude/Max)
- INGEST: pipeline completa per `fGpz-uOgr4k` ("email marketing povero, email marketing ricco",
  29s, 15/15 frame letti = coverage 100%). 4 KA, 1 pagina Source nuova (nessun Concept nuovo:
  video ricicla pattern già catalogati nei video 11-12, non introduce contenuto tecnico nuovo).
  Attribuzione riga-personaggio (povero/ricco) segnalata esplicitamente come non verificata dai
  frame statici — nessuna caption on-screen, solo audio/VTT (principio NO-FINTO rispettato: non
  si inventa un'attribuzione che non si può confermare).
- DECISIONE MAX: scope missione confermato = ~81 video curati del tracker (non i 323 del canale
  intero). Approvato passaggio a batch paralleli di agenti (3-4 video insieme) per velocizzare le
  sessioni rimanenti, con architettura anti-collisione (agenti isolati per cartella video, nessuna
  scrittura su file condivisi da parte loro, serializzazione dei tracker fatta dal conduttore).
- WATCH-001: N_video=13, N_MemoryEmpire=13 → MATCH ✅. Checkpoint: CP-20260823-008.

## 2026-08-23 (Ponte memory-wiki-bridge + /sync-wiki-totale, Claude/Max)
- BUILD: Max ha chiesto conferma se tutto finisce automaticamente in wiki → no, solo Empire
  Studio ci arrivava (wiki-syncer). company/Memory (checkpoint/ADR/STATO-EMPIRE, REGOLA ZERO)
  non aveva nessun percorso verso la wiki — causa identica al buco 16gg trovato piu' sotto in
  questo stesso log (entry `## 2026-08-23` backfill). Costruito nuovo agente 7-file
  **memory-wiki-bridge** (gemello di wiki-syncer, reparto ingestion-archive di Memory Empire) +
  comando **`/sync-wiki-totale`** (zero domande, report MATCH/GAP, verifica grafo senza pagine
  orfane via knowledge-cartographer). ADR-012 registrato. Backlog storico B-019 (pre-luglio
  2026) lasciato esplicitamente fuori scope, richiede via libera Max. → 1 pagina wiki nuova
  (tools/Tool_Memory_Wiki_Bridge.md) + index.md aggiornato. CP-20260823-007.

## 2026-08-23 (Empire Studio continua — Andrei Pascu cat1-copywriting video 12/29, Claude/Max)
- INGEST: pipeline completa per `hb89lccIacY` ("10 strategie PROVATE per EMAIL copywriting per
  vendere sempre", 11m49s, 355 frame, 13 letti nativamente su 10 capitoli + outro dopo verifica
  formato uniforme talking-head). 20 KA, 4 pattern, 1 nuova Source page + 1 nuovo Concept page
  (CTR vs CR — trappola di lettura metriche, generalizzabile oltre l'email).
- ENRICHMENT REALE (non solo proposto): skill `emails` (`references/copy-guidelines.md`) patchata
  2 volte — sezione "Subject Lines" nuova (limite caratteri, no nome iniziale, no clickbait, emoji)
  + distinzione CR/CTR e caveat click-per-link aggiunti a "Metrics to Track".
- NOTA TECNICA: yt-dlp 2026.7.4 dava 403 Forbidden su questo video — aggiornato a 2026.8.19,
  risolto. Segnalato per sessioni future.
- WATCH-001: N_video=12, N_MemoryEmpire=12 → MATCH ✅. Checkpoint: CP-20260823-005 (004 era già preso da Cursor Grok, mappa Digital Empire — collisione risolta, nessun contenuto perso).

## 2026-08-23 (Empire Studio ripreso — Andrei Pascu cat1-copywriting video 11/29, Claude/Max)
- INGEST: run andrei-pascu-001 ripreso dopo blocco (mancava Python/yt-dlp/ffmpeg in sessione
  precedente, ora verificato presente). Pipeline completa per `nRm7JLsP1bc` ("Basta usare
  formule clichè di copywriting"): Stage 1-5 + Stage 7 + Memory Empire C-H. 23/23 frame letti
  (video 46s, coverage totale). 8 KA P12-traced. 1 nuova Source page + 1 nuovo Concept page
  (checklist anti-clichè hook, generalizzabile a tutto il copy/ads DE).
- ENRICHMENT-RESEARCH: vedi `company/Memory/memory-empire/memory/ingestions/2026-08-23-*.md`
  per proposta d'uso del contenuto nella skill `cro-copy-architect` (gate Attenzione/APSOC).
- WATCH-001: N_video=11, N_MemoryEmpire=11 → MATCH ✅. Checkpoint: CP-20260823-003.

## 2026-08-23 (Mappa root Digital Empire, Cursor/Max)
- MAPPA: censimento 49 cartelle di primo livello (~35k file, vendor escluso) + alberi di company, PIANO-MAESTRO, DIGITAL-EMPIRE, empire, wiki, fabbriche.
- ARTEFATTO: canvas `digital-empire-mappa.canvas.tsx` (schema a livelli, catalogo filtrabile, openFile sui file di verità).
- CP: `company/Memory/checkpoints/CP-20260823-004.md`

## 2026-08-06 (Primo carosello Preventa reale: Agent workspace Arena, non il motore grezzo, Claude/Max)
- CORREZIONE: `projects/Preventa/Progetto_Preventa_Carousel.md` descriveva il motore
  sbagliato (Playwright grezzo `ArenaAI/arena_generator.py`, 3 slide gradiente
  hardcoded). Il sistema reale "perfetto" di Max è un Agent workspace dentro Arena
  stessa, raggiungibile via una chat archiviata + comando `/inizio-generazione`.
  Pagina riscritta con il flusso verificato passo-passo.
- INGEST: primo carosello Preventa reale generato e scaricato (8 slide 4K + copy.json,
  11.35MB), verificato con unzip + ispezione visiva. 4 script Playwright riusabili
  scritti. Dettaglio in `company/Memory/checkpoints/CP-20260805-013.md`.

## 2026-08-05 (Pivot @Legamidiamore: audit reale sblocca blocco 07-22, Claude/Max)
- UPDATE: `entities/Entity_Legami_dAmore_Channel.md` — status da "⚠️ Da riconciliare — accessi
  ignoti" a "✅ Riconciliato". Login reale in YouTube Studio (credenziali fornite da Max in chat,
  mai salvate su disco) conferma: canale suo, monetizzato, 14.793 iscritti, revenue €44,02/28gg
  (quasi nulla nonostante i numeri — confermata la diagnosi del 07-22). Corretto anche un dato
  vecchio: non è inglese, è quasi tutto italiano (scrape reale, 60 video). → 1 pagina aggiornata.
- CONTESTO: Max ha messo in pausa il progetto Dose Mentale-copia per dare priorità a questo
  canale esistente. Dettaglio tecnico in `company/Memory/checkpoints/CP-20260805-009.md`.

## 2026-08-05 (Secondo incarico a Neri: fabbrica strategie S7 via Arena, Claude/Max)
- PLAN: Max ha chiesto un prompt completo e autosufficiente per Neri, da usare in Arena.ai per
  progettare una "fabbrica" che genera un agente-strategia dedicato per ogni strategia di
  trading di Stream S7 (oggi: memecoin + NFT, entrambe già costruite). Riusato il metodo
  esistente `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md`, non reinventato. Scritto
  `company/Memory/tasks/TASK-NERI-20260805-S7-STRATEGY-FACTORY-ARENA.md` (fuori wiki, artefatto
  operativo di Memory — qui solo il log e l'aggiornamento di [[entities/Neri]]). Segnalata
  esplicitamente la tensione con l'altro task di Neri (Go/No-Go non ancora consegnato): la
  progettazione via Arena procede in parallelo (zero capitale/esecuzione), gli agenti generati
  restano paper-trading-by-default finché Max non decide.

## 2026-08-03 (Fase 1 + Fase 3 outreach Preventa: filtro import reale + Reparto Produzione, Claude/Max)
- INGEST: chiusura Fase 1 (filtro solo-import reale, bug `categoria` vacuo trovato e
  corretto, verificato su Areus reale 8/29 lead) — CP-20260803-005, nessuna pagina wiki
  nuova (dettaglio tecnico, vive nel checkpoint).
- INGEST: Fase 3, mappati 3 motori caroselli reali sul disco (confusi tra loro fino ad
  oggi) e confermato con Max quale intendeva. Creato Progetto Preventa sotto un nuovo
  concetto "Reparto Produzione" → 2 pagine create:
  [[concepts/Reparto_Produzione_Digital_Empire]], [[projects/Preventa/Progetto_Preventa_Carousel]].
  Sicurezza segnalata (non risolta): credenziali Arena/API in chiaro in
  `caroselli - agency/config.py`, committate in git.

## 2026-08-03 (Primo incarico reale a Neri: strategia Stream S7, Claude/Max)
- PLAN: Max ha chiesto un piano strategico per Stream S7 e di passare l'iniziativa a Neri
  (ricerche, report, architetture). Scritti `company/Ecosistemi/12-STREAM-S7-BOT/
  PIANO-STRATEGICO-S7.md` + `company/Memory/tasks/TASK-NERI-20260803-STREAM-S7-STRATEGIA.md`
  (fuori wiki, sono artefatti operativi di Memory/ecosistema — qui solo il log e l'aggiornamento
  di [[entities/Neri]]). Convergenza notata con CP-20260803-001 (sessione diversa, stessa
  diagnosi indipendente: "non manca codice, manca una decisione"). Interpretazione segnalata:
  passa lo strato strategico a Neri, non l'esecuzione tecnica (resta di Gael).

## 2026-08-03 (Metodo Arena → Workflow Completo, Claude/Max)
- INGEST: Max ha chiesto un piano dettagliato per usare Arena + skill `master-build-architecture`
  + motore APEX-7 (`11-APEX-7-CORE`, ADR-010) per costruire workflow completi (agenti/skill/
  flussi/automazioni). Recuperato dossier 26 (Arena: contratto operativo) da git — perso dal
  disco in un rebase, mai ripristinato — e riletto `13-ARENA-APEX/ECOSISTEMA.md` (Regola APEX:
  nessun agente esce dall'Arena senza APEX-7 integrato/testato). Creato
  `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md` — metodo riusabile in 3 fasi (Arena
  progetta → Claude Code costruisce nel ciclo 9 passi → APEX-7 gate obbligatorio), con prompt
  di apertura pronto e checklist di accettazione. 1 entry aggiunta in index.md
  (Metodologie di Sviluppo).

## 2026-07-30/31 (Bibbia dei Messaggi Outreach + team agenti, Claude/Max)
- INGEST via `/content-forge`: trascrizione video + 2 rielaborazioni di Max sul framework
  LinkedIn cold outreach (Barnum Effect, Rainbow Effect, 5 Pilastri, sequenza follow-up
  3-step) → sorgente grezzo `Outreach/knowledge/raw_linkedin-cold-outreach-framework_2026-07-30.md`
  (7.288 parole). Pipeline completa (KG 16 atomi/6 cluster → MKD → team) in
  `Outreach/forge-run-2026-07-30T-outreach-bible/`.
- BUILD: MKD pubblicato come **Bibbia dei Messaggi** (regola non derogabile, richiesta
  esplicita di Max) in `Outreach/knowledge/bibbia-messaggi-outreach.md` (+glossario+FAQ+schemi).
  Team di 4 agenti (`rule-keeper` gatekeeper, `message-writer`, `case-study-forge`,
  `followup-sequencer`, 7 file canonici ciascuno) in `Outreach/agents/outreach-message-team/`.
- 3 pagine wiki create: [[concepts/Framework_Cold_Outreach_APSOC]] (colmato link dangling
  già presente in index.md), [[concepts/Framework_Barnum_Rainbow_5Pilastri]],
  [[tools/Tool_Outreach_Message_Team]]. index.md sezione Framework aggiornata.
- Cross-link con lavoro già in produzione: `personalizza_messaggi.py` (campagna
  concessionari-preventa) aveva già un Gancio 4 "import" che applica lo stesso principio
  (variabile hard-coded di nicchia) — la Bibbia lo rende esplicito/canonico invece che
  implicito in un singolo script.

## 2026-07-30 (Nuovo membro team: Neri, Claude/Max)
- INGEST: Neri si è unito al team (gestione organizzativa/piani/metodi, non operativo) →
  1 pagina creata [[entities/Neri|Neri]], linkata a [[projects/Piano_Maestro_EMPIRE_OS]],
  [[concepts/SPARC_Methodology]], [[projects/Preventa/Preventa_Logica_Completa_Metodo]].
  Aggiunta sezione "Team" in index.md. Specchio anche in `company/Memory/STATO-EMPIRE.md`
  (nota organi/coordinamento) e memoria persistente Claude (`project_team_neri.md`).

## 2026-07-30 (CORREZIONE — Stream S7: logica completa documentata, Claude/Max)
- Max ha corretto: la richiesta era sul bot S7 (NFT/memecoin Solana), non su Preventa
  (voce sotto, lasciata perché comunque valida ma fuori bersaglio). Letto codice reale
  (`main.py`, `data_manager.py`, `analysis_engine.py`, `risk_manager.py`,
  `execution_engine.py`, `position_monitor.py`, `report-studio.md`, `APEX-7.md`,
  checkpoint CP-20260728-006) → file creato direttamente in
  `company/Ecosistemi/12-STREAM-S7-BOT/LOGICA-COMPLETA-S7.md` (non in wiki: doc tecnico
  legato al codice, resta accanto ad esso). Punto centrale: `report-studio.md` boccia
  già il live trading (expectancy negativa, >85% rischio perdita capitale primo mese) —
  S7 è R&D speculativo 0€ revenue, non un percorso di incasso attuale.

## 2026-07-30 (Preventa: logica completa documentata, Claude/Max)
- INGEST: mappata e documentata tutta la logica del sistema Preventa (scraping import-focus →
  qualificazione → Areus → ganci → invio WhatsApp reale → follow-up), letta dal codice reale
  (`outreach_giornaliero.py`, `run.py`, `checker.py`, `areus.py`, `personalizza_messaggi.py`,
  `send_message.py`, `refresh_session.py`) + checkpoint CP-20260729-007. → 1 pagina creata:
  [[projects/Preventa/Preventa_Logica_Completa_Metodo|Preventa — Logica Completa del Sistema]].
  Obiettivo: base per fissare il Metodo prima di scalare l'operativo.

## 2026-07-23 (Task board Gael operativo + prompt Gemini S7 pronto, Claude/Max)
- PLAN: dossier 25 = task board Gael autorevole. Scoperta chiave: **il lavoro è cablaggio, non costruzione**.
  Asset già su disco: `Outreach/preventa-outreach-pack/` (6 script APSOC concessionari già scritti),
  `Outreach/Outreach Workflow/` (motore live empire_auto_v3.py), `.claude/skills/youtube-automation-factory/`
  (skill completa con conductor+6 operatori+4 gate, mai eseguita). Ordine: G-A outreach concessionari 100%
  auto → G-C sito Preventa+PROVE → G-B YouTube 100% auto → G-D manutenzione.
- BLOCCHI nuovi per Max: M-EST-8 canale YouTube + credenziali API (blocca upload auto), M-EST-9 province scraping.
- S7: prompt copia-incolla per Gemini pronto (`GEM-07-PROMPT-DA-INCOLLARE-S7.md`), paper-trading first.

## 2026-07-23 (Calendario esecutivo V2 + S7 NFT bot delegato Gemini, Claude/Max)
- PLAN: dossier 24 = calendario giorno-per-giorno dal 23/07 (Opzione B outbound). Task Gael (G-EST-1..5) +
  Max (M-EST-4,6,7) sui giorni. Sostituisce il calendario 21→26 del P7.
- DECISIONE D-EST-007: bot NFT/memecoin (S7) APPROVATO come R&D delegato a Gemini, paper-trading first,
  €0 nel piano revenue estate, esecuzione 100% Gemini (isola S1/S2). Brief: `Antigravity-Briefs/GEM-07-S7-NFT-BOT-BRIEF.md`.
  Report S7 analizzato: tecnicamente solido e onesto, ma framing vecchio (Manuale/€131k) riallineato.

## 2026-07-23 (Analisi prodotti DE + IG morto, Claude/Max)
- ANALISI: dossier 23 (potenziale prodotti). Dato reale dal codice `agency-empire/`: i workflow costano
  **€5.000-15.000** (non SaaS). 1 vendita workflow > tutti i 7 concessionari settembre. Riprioritizzazione:
  🥇 Outreach Factory via dogfooding (usare la ns macchina outreach su noi stessi per prenotare demo) ·
  🥈 Preventa (cash veloce volume, sezione sito separata) · 🥉 Content Factory · Corso/Second Brain giù.
- FATTO: IG `crea.illtuo_impero` a zero → fork D-EST-006 risolto in Opzione B (tutto outbound freddo),
  Corso CCM parcheggiato per l'estate. Blocco n.1 = lead freddo + 1 prova (Novacar case study), non altri prodotti.

## 2026-07-23 (Piano Estate V2 diversificato + dati YouTube reali, Claude/Max)
- ANALISI/PLAN: dossier 22 (piano estate V2). Corretti 2 errori miei: prodotto = Corso CCM (non "Manuale"
  = lead magnet); 7 concessionari = settembre non luglio. 5 stream diversificati (Preventa-freddo, Corso
  lean, prodotti sito agency-empire + sezione Preventa, NFT lane speculativa separata, YouTube funnel).
  Fork strategico D-EST-006. Task board Gael (G-EST-1..4) + Max (M-EST-1..5). Verificati su disco:
  `Lancio corso skill beast/` (infra corso completa) + `agency-empire/` (Next.js, 2 workflow live).
- DATI: 2ª estrazione yt-dlp Dose Mentale + Legami d'amore → conferma dossier 20. Prova decisiva sul
  canale-90€: Legami ha già 14.700 iscritti (14× i 1.000 comprabili) e rende ~nulla → gli iscritti non
  sono l'ingrediente mancante, è la view-per-video. Titoli duplicati/ri-uploadati = macchina a churn.
- NFT: 4 video queued per Empire Studio (lane speculativa, capitale a rischio, fuori piano principale).

## 2026-07-22 (Gate-FUNNEL: 4 blocchi reali trovati, Gael/Claude)
- AUDIT: verifica diretta post-CP-023 (che dichiarava "checkout integrato") — trovato invece che
  i link Stripe in `Crea siti/Siti CCM/manuale.html` sono placeholder mai sostituiti (bottone finto),
  l'audit pagine prerequisito non è mai stato fatto, la landing non è deployata su alcun dominio.
  Chiarita con Gael l'identità di `crea.illtuo_impero` (sua pagina personale) — password fornita in
  chat NON salvata in nessun file (regola chiavi solo .env). Preparato il testo bio pronto da
  incollare (manca solo l'URL live). → CP-20260722-003 + STATO-EMPIRE aggiornati con dettaglio
  esatto per ogni blocco.

## 2026-07-22 (Analisi YouTube reale + piano chirurgico estate, Claude/Max)
- RESEARCH/INGEST: estrazione dati REALI via yt-dlp di 3 canali (Dose Mentale @dosementale 198k iscritti
  ma video recenti 649-3300 view = ratio 0,3% gonfiato; Legami d'amore @Legamidiamore 14.7k iscritti,
  471 video, GIÀ attivo inglese — NON il "canale dormiente" che Max ricordava; Andrei Pascu @andreipascu
  solo 8.040 iscritti YouTube, 100-500 view/video). SCOPERTA CHIAVE: Andrei guadagna da PRODOTTI (ebook
  €79 + corso €434), non da adsense — modello autorità→prodotto rende ~100× per spettatore vs faceless→view.
  YouTube-adsense NON è leva cash-7gg; YouTube-funnel-verso-Manuale sì. → 3 pagine: Entity_Dose_Mentale_Channel,
  Entity_Legami_dAmore_Channel, correzione entities/Andrei_Pascu (270k era TikTok/IG, YouTube reale 8k).
  Deliverable: PIANO-MAESTRO/20-ANALISI-YOUTUBE-PIANO-CHIRURGICO.md (piano con confidenza dichiarata per
  riga, pre-mortem) + 19-ARENA-BUILD-LIST.md (8 build + 6 prompt pronti per Arena). DEC-EST-001 sbloccata
  (Manuale €67, veto scaduto). Confidenza onesta ≥1 incasso entro 26/07: ~65-80%, non 99%.

## 2026-07-21 (YouTube Automation Factory — nuova skill, Max)
- INGEST + BUILD: trasformato il workshop YouTube Automation (Video IQ · SEO/certificazione ·
  Fliki · teoria hook/intro/CTA) nella skill operativa `.claude/skills/youtube-automation-factory/`
  (comando `/yt-factory`). Costruita con le 2 skill clonate `ansjkfgheqrlg/master-build-architecture`
  (struttura: 3 livelli, memoria dal passo zero) + `ansjkfgheqrlg/content-forge2.0` (espansione, MKD).
  29 file: kernel (SKILL/MKD/ARCHITECTURE) + 11 agenti (conductor + 6 operatori + 3 gate/audit +
  memory-keeper) + 5 workflow (pipeline 6 fasi con feedback) + 4 reference + 2 tool Python testati
  (`seo_score.py` 0-100, `cashcow_check.py` indice cash cow) + evals + memoria. Serve la linea
  revenue **S5 YouTube-Fliki auto** (dossier 16). → 1 pagina wiki: Concept_YouTube_Automation_Factory.

## 2026-07-21 (Empire Desk B2/B3/B4 — verificati a runtime, Gael)
- BUILD/TEST: `modules/notify.py` (toast Windows nativo PowerShell/WinRT, zero dipendenze pip) +
  `modules/taskboard.py` (task board Max/Gael, seed 18 task reali da dossier 16). Sbloccato Python
  3.12/Node 24 (già installati da sessione precedente via winget, serve solo l'export PATH giusto)
  → primo test a runtime REALE di tutto il seam B1-B4: selftest 15/15 sia in dev sia dall'.exe
  frozen già esistente (senza ricostruirlo). Test funzionale diretto delle routes ha trovato 2 bug
  reali (non visibili dal solo selftest): validazione tile saltata in scheduler.aggiungi con host
  non pronto, id collidenti nello stesso secondo — entrambi corretti e ri-verificati.
  → CP-20260721-001 + REGISTRO-ERRORI EDE-9/10/11 + STATO-EMPIRE aggiornati.

## 2026-07-20 (Empire Studio — video 10/29, Gael)
- INGEST: Empire Studio — video Ahp_6rHSOsU (Andrei Pascu, cat1-copywriting, video 10/29). Formato tutorial screen-share 11m08s — Google Docs (macOS) + talking head PiP. Stage 1-5 completati: 334 frame @2s (3-digit naming), 16 frame letti nativamente, NO-FINTO PASS. 16 VP schermo: doc diviso pagine→senza pagine, menu File Impostazione pagina, Google Drive file list, outline heading popolato, note gialle "[inserire logo]"/"[inserire capibara]", menu dropdown stato, badge [in corso]/[da iniziare], indice+segnalibro, pannello Stili "Aggiorna Intestazione", contatore parole live, outro CTA. VTT 2505 righe letto integralmente (9 capitoli ufficiali del video). 20 KA P12-traced. Concepts: pulizia formato no-pagine, heading→outline navigabile, aggiorna stile in blocco, note colorate come heading dedicato, dropdown stato = mini-kanban, segnalibri+link, conteggio caratteri live, sistema cartelle Clienti visibile/non-visibile. → 2 pagine create: Source_Andrei_Pascu_Google_Docs_Copywriter, Concept_Google_Docs_Copywriter_Workflow. index.md +2 entry sezione Copywriting. WATCH-001: N_video=10 = N_MemoryEmpire=10 → MATCH ✅

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

## 2026-07-24
- BUILD: **WORKFLOW ESTATE completato** — `python -m empire estate` → exit 0 (11 controlli su 13;
  conform 0 block, 207 test). Piano a 3 livelli L1→L2→L3 (ognuno corregge i limiti dichiarati del
  precedente) + `ARCHITETTURA-COMPLETAMENTO.md` + swarm a 6 lotti con perimetri disgiunti.
  Nuovi: `empire/estate.py` (verdetto unico), `flow/decisions.py` (default-più-veto ADR-EST-006),
  `flow/evidence.py` (guardia di provenienza sui dati), `inspect/metrics.py` (6 KPI telemetria),
  `tools/video_pack.py`, landing Preventa. CP-20260724-001.
- LEZIONE (trasversale, vale oltre l'estate): **un controllo che in caso di dubbio rassicura è
  peggio di nessun controllo.** Tre difetti indipendenti della stessa famiglia trovati in un giorno:
  la dashboard coloriva di verde i valori che non sapeva leggere; l'anagrafe ADR-008
  (`skills-map.yaml`) era YAML non valido perché letta solo a occhio, mai da una macchina;
  `video_pack --check` approvava il proprio scheletro. Corollario operativo: ogni registro va
  caricato da un parser almeno una volta, o non è un registro.
- FINDING aperto: i 7 lead di `lead.csv` hanno **0/7** riscontri nelle sorgenti `Outreach/`; i 61
  lead reali dichiarati il 23/07 non esistono su disco. Gate-CONTATTI lasciato rosso di proposito.
  → 0 pagine wiki nuove, 1 lezione registrata.

## 2026-08-03
- INGEST: studio copy @dosementale rigenerato su 36 video reali → 1 pagina aggiornata (synthesis/Studio_Copy_Dose_Mentale.md)

## 2026-08-05
- INGEST: studio copy @dosementale rigenerato su 36 video reali → 1 pagina aggiornata (synthesis/Studio_Copy_Dose_Mentale.md)

## 2026-08-06
- INGEST: studio copy @Legamidiamore + 4 competitor rigenerato su 176 video reali → 1 pagina aggiornata (synthesis/Studio_Copy_Legamidiamore.md)

## 2026-08-22
- INGEST: NERVE-SOLVE (Orchestration Layer 1 — Problem Solving Engine) estratto da `SKILL & Agenti/Orchestracion Layer - Problem solving.zip`, distillato architettura v2.2 in skill Claude Code operativa `.claude/skills/nerve-solve/` (mirror `.agents/skills/`), scartato kernel Python crittografico orfano della fonte. Registrato in `company/skills-map.yaml` (ADR-008) sotto 08-INTELLIGENCE/Cognitive-Control. → 1 pagina wiki nuova (tools/Tool_Nerve_Solve_Orchestration_Layer.md) + index.md aggiornato.

## 2026-08-23
- BACKFILL (buco reale trovato, non simulato): `log.md` non aveva NESSUNA entry tra 2026-08-06 e 2026-08-22 (16 giorni), mentre `company/Memory/checkpoints/` ha 16 checkpoint reali nello stesso periodo (libro KDP, primo video YouTube pubblicato, wrapper IG Preventa, fix self-healing WhatsApp, ecc.) — la causa è l'esistenza di due sistemi di memoria paralleli: `company/Memory/` (REGOLA ZERO) è stato rispettato sempre, la wiki (REGOLA FONDAMENTALE) no. Colmato lo scope concordato con Max (solo il gap 06→22 agosto, non tutta l'estate): 2 pagine nuove (entities/Entity_The_Quiet_Hours_Libro_KDP.md, tools/Tool_Pipeline_Libri_KDP.md — primo libro KDP mai completato, prima non aveva NESSUNA pagina) + 3 pagine aggiornate (entities/Entity_Legami_dAmore_Channel.md: primo video reale pubblicato + 3 in produzione + 4 bug fix; projects/Preventa/Preventa_Logica_Completa_Metodo.md: fix self-healing rete su invio WhatsApp; projects/Preventa/Progetto_Preventa_Carousel.md: wrapper pubblicazione IG dry-run) + index.md aggiornato. Il resto dell'estate (prima di giugno-luglio) NON è stato auditato — richiede via libera esplicita separata.

---

# BACKFILL STORICO 2026-06-10 → 2026-08-20 (eseguito 2026-08-24, `/sync-wiki-totale`, permesso esplicito di Max)

Colma le 30 date con checkpoint reale in `company/Memory/checkpoints/` (228 checkpoint su 47
date di lavoro reale) ma senza nessun riscontro in questo log — il gap storico lasciato
esplicitamente fuori scope dal backfill del 2026-08-23 (B-019). Ordine cronologico
(vecchio→nuovo). Dettaglio checkpoint per checkpoint in `company/Memory/checkpoints/CP-*.md`.

## 2026-06-10 (Piano Maestro EMPIRE OS + GitHub monorepo, Claude/Max)
- BUILD: prodotto il piano fondativo `PIANO-MAESTRO/` (10 dossier ecosistema via swarm 7
  agenti paralleli) + scaffolding iniziale `company/Memory/` (ADR-001 EMPIRE OS 10
  ecosistemi, ADR-002 memory-first, ADR-003 wrap-non-riscrittura). Workspace intero portato
  su GitHub monorepo privato con sync bidirezionale Max↔Gael (ADR-004, `scripts/empire-sync.ps1`).
  Skill `empire-context` creata e installata a livello progetto. → 1 pagina aggiornata
  (projects/Piano_Maestro_EMPIRE_OS.md). CP-20260610-001/002/003.

## 2026-06-11 (F1-F4 scaffolding + Backbone + metodo 9 passi, Gael/Max)
- BUILD: F1 scaffolding `company/` completo (92 check gate verde) — organigramma, Mandato,
  Board C-Suite v1, 10 ecosistemi, Backbone, Guilds/Sentinels. F2 Backbone operativo
  (ruflo/claude-flow installato, BUS/BRAIN/Identity-HR). F3 migrazione asset (51
  skill/workflow mappati, 8 wrapper L3). F4 AGENCY B1 infrastruttura + B2 wrap dei 4
  workflow outreach esistenti (ADR-003) + gate F4 verde su ciclo dry-run end-to-end.
- DECISIONE: **ADR-006** — Ciclo di Fase a 9 passi (RECALL→SPEC→PRE-MORTEM→BUILD→GATE→
  REVIEW→TEST→COMMIT→RETRO), metodo ufficiale per Max e Gael. **ADR-007** — Piano V2,
  direttiva di scala di Max (reparti=team CF-grade, organo MAXIMILIAN, ecosistema-Mandato).
  CP-20260611-001..008.

## 2026-06-13 (Errore Memory Empire riconosciuto e corretto, Max)
- FIX: durante lo studio Andrei Pascu (Empire Studio), il pipeline comunicato a Max ometteva
  gli stage Memory Empire — errore critico (invariante non negoziabile). Corretto: Memory
  Empire reso invariante #0 nel session-init protocol di Empire Studio, agenti
  compliance-auditor/error-triage/silent-observer aggiornati. Apre **ADR-008**. CP-20260613-001.

## 2026-06-16 (Genesi Core: organi ARCHITETTURA+FORGE+MAXIMILIAN, dossier v2, Gael/Max)
- BUILD: fix collisione git case-insensitive; F1-bis chiuso (0 cartelle vuote, gate verde).
  V2-2 avviata: dossier **MAXIMILIAN** (12) + **MANDATO-ecosistema** (13); primi due lotti
  dossier v2 scala (01-AGENCY, 04-MARKETING, 03-CONTENT-FACTORY, 02-INFO-BUSINESS).
- BUILD: **Genesi Core** costruito in 4 STEP dallo stesso giorno — organo **ARCHITETTURA**
  (30 file, progetta la forma di ogni artefatto), organo **FORGE** (34 file, costruisce il
  contenuto attorno al blueprint), organo **MAXIMILIAN** (15 file, review-gate 5-bis "Max
  approverebbe?"), blueprint Board C-Suite (70 agenti progettati su 7 figure). → 1 pagina
  nuova (tools/Tool_APEX7_Core_Motore_Condiviso.md riferisce a questo lavoro indirettamente;
  dettaglio Genesi Core in projects/Piano_Maestro_EMPIRE_OS.md, sezione Evoluzione V2).
  CP-20260616-001..010.

## 2026-06-17 (Board C-Suite V2: CEO/Chief-Forge/CTO/COO/CMO/CRO, Gael)
- BUILD: STEP 4-heavy — FORGE costruisce il contenuto delle figure Board dai blueprint.
  Batch 1 (CEO-Empire-Conductor, Chief-Forge), batch 2 (CTO, COO), batch 3 (CMO, CRO) — ogni
  figura 10 agenti + 3 workflow CF-grade, review 5-bis MAXIMILIAN APPROVA su tutte.
  CP-20260617-001..003.

## 2026-06-18 (CFO chiude Board C-Suite 7/7 + 04-MARKETING completo 6/6, Max/Gael)
- BUILD: CFO completato (Max) → **Board C-Suite V2 7/7 figure complete** (~70 agenti CF-grade).
  STEP 5: costruiti tutti i 6 reparti di 04-MARKETING (L2.6 Conversion Architecture, L2.5
  Brand & Creative, L2.2 Advertising, L2.3 Email & Lifecycle, L2.4 Analytics, L2.1
  Copywriting — wrap del Copy Workflow Orchestration Layer attivo, ADR-003) →
  **04-MARKETING primo ecosistema V2 intero** (114 file/44 agenti/22 workflow).
  CP-20260618-001..007.

## 2026-06-19 (03-CONTENT-FACTORY completo 9/9 reparti, Gael)
- BUILD: costruiti gli 8 reparti CF-R0..CF-R8 del mega-reparto 03-CONTENT-FACTORY (Director,
  Strategia&Brief, Brand-Kit Registry, Produzione Video, Produzione Testuale, Visual&Design/
  Caroselli, QA&Gate, Pubblicazione, Apprendimento — CF-R5/CF-R6 chiusi il 06-23, CF-R8 il
  06-30) → **9/9 reparti completi**, wrap di 3 motori attivi (hf-studio/heygen-studio,
  carousel-factory, orchestratori Python pubblicazione, tutti ADR-003). CP-20260619-008..016.

## 2026-06-22 (02-INFO-BUSINESS completo 5/5 + 01-AGENCY batch-1, Max)
- BUILD: STEP 5 — 02-INFO-BUSINESS chiuso 5/5 reparti (PROD/LANC/VEND/COMM/STRA, 94 file/42
  agenti/12 workflow). 01-AGENCY batch-1: A1-Ricerca, A2-Acquisizione (wrap del runtime
  outreach LIVE — Outreach Workflow/LinkedIn/Instagram, ADR-003 esemplare), A3-Preventivi →
  3/10 reparti. CP-20260622-001/002.

## 2026-06-23 (01-AGENCY batch-2, A4-A6, Max)
- BUILD: A4-Delivery, A5-Copywriting-Interno, A6-Marketing-Interno&Proof → **01-AGENCY 6/10**.
  CP-20260623-001.

## 2026-06-30 (primo video Andrei Pascu ingerito + PreventivoForge avviato, Max)
- INGEST: Empire Studio — primo video della run andrei-pascu-001 ingerito integralmente
  (9CuQI0Cr4Pg, FB Ads pannelli fonoassorbenti) → 2 pagine wiki (già presenti in index.md,
  sezione Copywriting).
- BUILD: primo cliente reale **PreventivoForge** avviato (Prof Autocad, poi rinominato
  Novacar srl) — Half A (Max: scraper/parser/pricer/dealers, prezzo 18.000→21.540€
  verificato) completata con agenti CF-grade + regole RBI + orchestration. → 1 pagina
  aggiornata (01 - Projects/Project_Prof_Autocad_PreventivoForge.md). CP-20260630-001/002/003.

## 2026-07-01 (PreventivoForge: Half B + scraping live risolto, Gael/Max)
- BUILD: Half B completata (Gael — traduzione/copy deterministica, render PDF, QA Gate
  A/B/C/D, 42 file agenti). Scraping LIVE mobile.de risolto: bypass Akamai Bot Manager via
  Chrome reale + CDP invece di Playwright puro, parser sui dati veri
  (`window.__INITIAL_STATE__`). Prova reale: Mercedes GLA 47.490€→51.915€, 4 gate verdi.
  REGOLE-SACRE (14 regole PDF) + template Novacar + dealer reale + ecosistema Memory propri.
  CP-20260701-001..004.

## 2026-07-02 (PreventivoForge: App Desktop + PDF via CDP + .exe, Gael)
- BUILD: App Desktop GUI (prima Tkinter), motore PDF migrato a CDP/Chrome (no Playwright,
  .exe-ready). PDF rifatto sul modello Novacar (Gate IMG + Gate R, 14 REGOLE), primo .exe
  costruito e validato con `--selftest`. CP-20260702-001..003.

## 2026-07-03 (PreventivoForge: GUI premium + kill-switch + consegna, Gael/Max)
- BUILD: GUI premium via pywebview (WebView2, priorità #1 di Max) con fallback Tkinter.
  Kill-switch abbonamento (`licenza.py`, controllo remoto via Gist) cablato in run.py+app.py.
  Storico automatico preventivi. **Consegna abbonabile pronta** — `CONSEGNA-NOVACAR.md`, .exe
  frozen ri-testata 6/6 gate + 14/14 REGOLE. CP-20260703-001/002.

## 2026-07-25 (Refinement agenti operativi APEX-7: misuratore + primi 2 promossi, Max)
- BUILD: `empire/forge.py` — misuratore di quanto un agente è OPERATIVO vs DOCUMENTALE (6
  criteri). Fotografia: 439 agenti, 55 operativo/324 parziale/60 documentale. Primi due
  agenti promossi a operativo: AGENTE-CLOSER-A8, AGENTE-CRO-COPY-ARCHITECT. Filtro corredi
  aggiunto (evals/failure-modes non contati come agenti). CP-20260725-001/002.

## 2026-07-27 (Sync/preventa-agents Phase A-B, APEX-7 Level 2, audit YT-Factory + F1-F3 reali, Claude/Gael/Max)
- FIX: conflitto sync GitHub risolto; `preventa-agents` ricostruito nel pattern
  cartella-per-agente (8 agenti, facade `agents.py` riparata, 13/13 test) dopo un wipe
  lasciato a metà; bug scraper multi-città (sovrascriveva invece di accumulare) fixato,
  19 lead ALTA reali generati, Gate-CONTATTI chiudibile onestamente.
- BUILD: APEX-7 portato a Level 2 operativo end-to-end su Stream S7 (Event Bus, memoria,
  6 gate a rubrica, meta-agent, orchestrator — test 8/8 sezioni verdi).
- AUDIT: YOUTUBE-AUTOMATION-FACTORY — scaffolding APEX-7 reale e testato ma **tutte e 6 le
  fasi hardcoded** (canale/video/script/critic sempre gli stessi, gate strutturalmente
  incapace di fallire). Corrette nella stessa giornata: F1 (scouting su dati reali, gate
  Cash Cow bloccante), F2 (fetch live YouTube reale con cache), F3 (script da materiale
  reale). Agente ANDREI-PASCU-MINER promosso a operativo. → 1 pagina aggiornata
  (concepts/Concept_YouTube_Automation_Factory.md). CP-20260727-001..015.

## 2026-07-28 (ADR-010 fusione APEX-7 + Preventa→Areus + Stream-S7 trading reale + YT-Factory F4-F7, Claude/Gael/Max)
- DECISIONE: **ADR-010** — fusione delle implementazioni APEX-7 divergenti su un motore
  condiviso multi-tenant (`11-APEX-7-CORE`), pilota su YouTube + Stream-S7-Bot.
- BUILD: Preventa — prezzo €2.000 una tantum chiuso, migrazione da Google Sheets ad Areus
  (CRM interno), modulo EmpireDesk `preventa.py`. Comando unico `/avvia-estate-wk`.
  Stream S7: loop trading collegato al bus reale (bug doppia esecuzione fix, RiskManager
  riscritto, feedback loop reale), poi parser Solana reale + position manager + fix spam
  segnali (Gael, verificato su transazioni mainnet vere).
- BUILD: YOUTUBE-AUTOMATION-FACTORY — F4 (spec Fliki multi-scena reale), F5 (metadati/tag
  reali), F6 (audit onesto, mai metriche finte), dashboard riflette l'esito vero, decisione
  motivata di **non migrare** Stream-S7-Bot al motore condiviso (implementazione più matura
  su alcuni assi). → 1 pagina nuova (tools/Tool_APEX7_Core_Motore_Condiviso.md).
  CP-20260728-001..013.

## 2026-07-29 (Centro di comando empire-wide + outreach WhatsApp reale + pivot @dosementale, Claude/Gael/Max)
- BUILD: `empire controllo` (porta d'uscita, modello Playwright non OAuth) e `empire
  cantiere` (porta di costruzione, guida i 3 modelli operativi). TASK-YT-002..007 chiuse
  (YouTube Factory: tutte le fasi P1 reali).
- BUILD: Outreach Preventa — invio WhatsApp reale automatizzato (profilo Chromium
  persistente, non storage_state: le chiavi di sessione WhatsApp Web vivono in IndexedDB),
  flusso giornaliero `/avvia-outreach-preventa` con Gancio 4 import-focus.
- CORREZIONE: il primo contenuto YouTube reale generato era ancora sul funnel morto
  "Manuale Claude Code" — pivot deciso da Gael a **@dosementale** come canale sorgente
  (replica per un canale da vendere già monetizzato, zero funnel). → 1 pagina aggiornata
  (entities/Entity_Dose_Mentale_Channel.md). CP-20260729-001..010.

## 2026-07-31 (Motore YouTube riscritto su @dosementale + Bibbia Messaggi Outreach, Gael/Claude/Max)
- BUILD: `apex7_orchestrator.py` (F1-F5) riscritto per intero su @dosementale — prima era
  solo il contenuto ad essere cambiato, il motore restava cablato sul Manuale Claude Code
  (rischio concreto di sovrascrittura). Config Fliki bloccata `NON MODIFICARE` su richiesta
  di Gael dopo un video approvato.
- BUILD: **Bibbia dei Messaggi Outreach** (Effetto Barnum, Rainbow, 5 Pilastri) + team di 4
  agenti + enforcement reale (`rule_keeper_lint.py`, lint deterministico agganciato prima di
  ogni invio WhatsApp). → 3 pagine wiki già presenti in index.md (sezione Framework).
  CP-20260731-001..005.

## 2026-08-04 (Audit YOUTUBE-AUTOMATION-FACTORY: 6 claim verificati riga per riga, Claude/Max)
- AUDIT: verificate riga per riga (non sui checkpoint) le 6 capacità che Max ricordava
  "implementate perfettamente" — 2 reali ma isolate (mai chiamate dall'orchestratore), 2
  rimosse per scelta (non mancanti), 2 parziali. Rilevata collisione live con una sessione
  Gael attiva sugli stessi file → **pausa su richiesta esplicita di Max** (crediti).
  Nessun file di produzione modificato. CP-20260804-001.

## 2026-08-07 (PIANO KDP: LM Arena abbandonato per il testo, Gael)
- DECISIONE: dopo 2 giorni di debug reale (captcha non aggirabile oltre il primo messaggio
  di una sessione, anche con profilo persistente), Gael decide di abbandonare LM Arena per
  la scrittura dei libri — resta solo per le copertine. Nuovo piano V2-Claude-Code (10
  checkpoint). CP-20260807-001.

## 2026-08-08 (Aureus pulsante YouTube + primo libro KDP completo, Gael/Claude)
- BUILD: Aureus/EmpireDesk — pulsante unico "Produci video + copertina" per YouTube Factory
  (`produci_video_completo.py`, incatena F1-F5 + Arena + Fliki).
- BUILD: **primo libro KDP completo, "The Quiet Hours"** — 115 pagine reali + copertina,
  pacchetto pronto (già in wiki, entities/Entity_The_Quiet_Hours_Libro_KDP.md). CP-20260808-001/002.

## 2026-08-12 (Wrapper pubblicazione Instagram caroselli Preventa, Claude/Max)
- BUILD: `publish_instagram.py` — wrappa il publisher IG reale esistente (ADR-003), dry-run
  verificato sulle 8 slide del carosello #1. Già documentato in
  projects/Preventa/Progetto_Preventa_Carousel.md (sezione "Aggiornamento 2026-08-12").
  CP-20260812-001.

## 2026-08-13 (Outreach self-healing + APEX-7 su 3 stream + orchestration layer 7 gate, Claude)
- FIX: retry self-healing su `page.goto` in `send_message.py` (3 tentativi, 45s) per errori
  di rete intermittenti nell'invio WhatsApp.
- BUILD: i 3 consumatori di produzione (skill-forge, carousel-machine, cold-outreach)
  passano ora dai 7 gate del motore condiviso; `main.py` di APEX-7-CORE riparato su Windows
  (non partiva). **ADR-011** — censimento ADR-010 incompleto, 6 implementazioni APEX-7 non 4.
  Layer di orchestrazione generalizzato innestato in `11-APEX-7-CORE/orchestration/` (audit
  di uno zip di Max trovato con gate che non bloccavano nulla di reale — es. rendimento 500%
  certificato). → 1 pagina nuova (tools/Tool_APEX7_Core_Motore_Condiviso.md). CP-20260813-001..003.

## 2026-08-14 (Workflow KDP 4 step riparato + APEX-7 Calc Layer, Claude)
- FIX: CLI Claude era uno stub mai installato; una volta riparato, il wrapper `.cmd` di npm
  troncava i prompt multi-riga e ignorava silenziosamente `--model haiku` (si pagava il
  modello di default). Flusso corretto per rispettare i 4 step dichiarati (nicchia scelta
  una volta sola, comando `riprendi` per non perdere capitoli già scritti/pagati).
- BUILD: APEX-7 Calc Layer — 16 moduli di calcolo puro (probabilità, royalty KDP, rendimenti)
  dietro un'interfaccia JSON pensata per parlare con altri orchestration layer; corretti 2
  errori finanziari reali trovati nello zip di Max. CP-20260814-001..003.

## 2026-08-15 (Legami d'Amore wiring reale + decisione finale modello scrittura libri, Claude/Gael)
- BUILD: YouTube Factory cablata su @Legamidiamore (voce femminile, upload, tag SEO a 4
  livelli, agente permanente `credential-keeper`).
- DECISIONE: dopo 3 tentativi di automazione falliti (Claude CLI/Haiku, LM Arena ×2), Gael
  decide che **il libro lo scrive Claude in sessione** — il Python smette di chiamare
  modelli e diventa attrezzatura di misura/impaginazione. 3 automazioni archiviate con `git
  mv` (ADR-003, niente cancellato). → 1 pagina aggiornata (tools/Tool_Pipeline_Libri_KDP.md).
  CP-20260815-001..003.

## 2026-08-16 (Primo test reale F1→F5 legamidiamore, Claude)
- BUILD: run reale end-to-end su @Legamidiamore, script scritto da Claude su materiale
  reale (3 iterazioni fino a 12,6 min/critic 8.08), bug tag SEO inquinati da etichette
  interne di pattern copy trovato e fixato. CP-20260816-001.

## 2026-08-17 (Secondo libro KDP "The Ninth Winter" + bug calibrazione pagine, Claude)
- BUILD: **"The Ninth Winter" completato** (24/24 capitoli, 34.897 parole) — prima verifica
  end-to-end del modello "lo scrivo io" su un caso reale imperfetto. Scoperto e corretto un
  bug di calibrazione: 300 parole/pagina dichiarate, 320 reali misurate su due libri veri —
  il PDF viene ora generato sempre, non solo su richiesta. → 1 pagina nuova
  (entities/Entity_The_Ninth_Winter_Libro_KDP.md). CP-20260817-001/002.

## 2026-08-18 (Primo video YouTube pubblicato + regola niente lineette lunghe, Max/Claude)
- MILESTONE: **primo video reale pubblicato dalla YouTube Automation Factory**, su
  @Legamidiamore (youtu.be/2t4BZR3KAiU) — upload finale completato a mano da Max dopo che
  l'automazione Playwright si è scontrata con "Verify it's you" di Google (blocco non
  aggirabile per design). Scelta deliberata di Max: Public, non Private. Già in wiki
  (entities/Entity_Legami_dAmore_Channel.md).
- BUILD: regola "niente lineette lunghe" nei libri (Gael) applicata a mano su 193 righe —
  The Ninth Winter e The Quiet Hours entrambi PUBBLICABILE con copertina/PDF/copy.
  CP-20260818-001/002.

## 2026-08-19 (3 video in produzione + piano "un libro in mezz'ora" CP1-6, Claude)
- BUILD: 3 nuovi video @Legamidiamore in produzione (bug `duration: 720` bloccava ogni
  generazione Fliki, fixato).
- BUILD: piano "un libro in mezz'ora" — bersaglio pagine spostato al centro della finestra,
  gate di blocco in 0,06s, riassunti a formato fisso, codice sceso da 41 a 27,6s (CP-1..6
  verificati con misure reali). Piano concorrente di Gael (`kdp_workflow/`) valutato: presi
  3 pezzi buoni (validatore troncamento, copy KDP arricchito, scheda ispirazione), rifiutata
  l'architettura (già archiviata il 08-15 dopo 3 fallimenti, 5 bug reali trovati nel piano).
  CP-20260819-001..003.

## 2026-08-20 (Terzo libro KDP "The Second-Hand Spellbook", prova cronometrata, Claude)
- BUILD: **CP-7 chiuso** — terzo libro completo in 48 minuti (non i 30 pianificati: il gate
  ha bocciato 3 volte lo stesso difetto, capitoli scritti corti in fretta). L'assunzione
  "320 parole/pagina" è stata falsificata dal libro stesso (stile diverso, scarto di 4,3
  pagine) — corretta la regola: generare il PDF reale prima della consegna finale, non
  fidarsi solo della stima. → 1 pagina nuova
  (entities/Entity_The_Second_Hand_Spellbook_Libro_KDP.md). CP-20260820-001.

## RIEPILOGO backfill 2026-08-24
30/30 date con checkpoint reale coperte (log.md). 6 pagine wiki nuove (tools/
Tool_APEX7_Core_Motore_Condiviso.md, concepts/Concept_Decisioni_Architetturali_ADR.md,
entities/Entity_The_Ninth_Winter_Libro_KDP.md, entities/Entity_The_Second_Hand_Spellbook_Libro_KDP.md)
+ 6 pagine aggiornate (projects/Piano_Maestro_EMPIRE_OS.md, tools/Tool_Pipeline_Libri_KDP.md,
concepts/Concept_YouTube_Automation_Factory.md, entities/Entity_Dose_Mentale_Channel.md,
entities/Entity_The_Quiet_Hours_Libro_KDP.md, 01 - Projects/Project_Prof_Autocad_PreventivoForge.md).
Dettaglio completo: `company/Memory/checkpoints/CP-20260824-*.md`.

## 2026-08-25 (Sync monorepo: build CCM + skill empire-premium-style su GitHub, Claude)
- INGEST: assorbito nel monorepo tutto il lavoro non tracciato del working tree — 103 file,
  ~2,8 MB di soli sorgenti (`.gitignore` ha tenuto fuori `node_modules/`, `.next/`, `dist/`,
  `*.zip`). Tre filoni: **skill `empire-premium-style`** (10 file: design system ccm-premium,
  token congelati, stack Next.js 16 + Tailwind v4 + Lenis + Framer Motion + GSAP),
  **build CCM** (`ccm-sale-page-empire` completo, `ccm-elite-ultimate`, `ccm-full-empire`
  parziale, + pipeline Jinja2 `builder.py` → `index.html` rigenerato),
  **`Landing Page/`** (`ccm-empire` home/masterclass/thank-you + export statico + varianti
  thank-you). → 1 pagina nuova (tools/Tool_Empire_Premium_Style.md) + index.md aggiornato.
- BUILD: `Landing Page/ccm-empire/` era un **repo Git annidato senza remote** (1 solo commit):
  committarlo avrebbe prodotto un gitlink vuoto, non clonabile da nessuno. Assorbito nel
  monorepo dopo backup in doppia copia della sua storia (bundle + copia `.git`).
- ⚠️ SICUREZZA: trovata **chiave API Brevo in chiaro su repo PUBBLICO** — non nuova, era in
  `HEAD` dal commit iniziale `57a0ba0b` in 3 file già tracciati. Va **ruotata su Brevo**, non
  solo rimossa dal codice (storia pubblica già indicizzabile). → backlog B-020.
  CP-20260825-001.

## 2026-08-25 (TASK-KDP-W1: il ciclo KDP si chiude end-to-end, quarto libro, Claude)
- BUILD: chiusi i **tre buchi** che impedivano al flusso KDP di consegnare i suoi tre output
  insieme. (1) Il copy Amazon non aveva **nessun comando**: `salva_copy()` c'era dal 15/08 ma
  nel flusso vivo non lo chiamava nessuno, e nei primi tre libri il copy è stato scritto **a
  mano dentro `progetto.json`** senza validazione (è così che sono passate le lineette lunghe
  nelle descrizioni di due libri già consegnati). Ora `kdp copy <slug> --file copy.json` valida
  prima di salvare e rifiuta senza scrivere. (2) La cartella finale nasceva **solo** col .png
  di copertina: ora nasce comunque, con bloccante esplicito "Copertina assente" in
  `validazione.json`. (3) `COPERTINA-PROMPT.md` ora entra sempre nel pacchetto. Nuovo
  `kdp pacchetto <slug>`: COMPLETO (exit 0) contro CARICABILE SU KDP. 135 test verdi (erano
  127, 8 nuovi). SKILL e SOP allineate nello stesso commit.
- INGEST: **quarto libro prodotto**, "The Winter Term" (dark academia mystery, Maren Ashcroft):
  24/24 capitoli, 39.668 parole, **116 pagine reali contate sul PDF**, 43,2 minuti dal primo
  comando all'ultimo. → pagina `tools/Tool_Pipeline_Libri_KDP.md` aggiornata.
- LEZIONE: il gate di blocco ha bocciato **2 volte su 7** e aveva ragione entrambe (capitoli a
  1.440 e 1.467 parole contro il bersaglio 1.600). La stima a 320 parole/pagina ha sbagliato di
  nuovo, 120,9 stimate contro 113 reali: solo il PDF conta. Scoperto anche che allungare un
  libro finito può rompere la continuità (conflitto Dunleavy cap 17/18, riparato).
  CP-20260825-002.

## 2026-08-27 (TASK-CAROSELLI-W1: un comando, un argomento, carosello nell'Arsenale, Claude)
- BUILD: nuovo comando unico `SKILL & Agenti/Workflow agency creative/caroselli.py`.
  Prima il flusso esisteva ma era in cinque pezzi da lanciare a mano (avvio browser,
  controllo stato, eventuale resume, download separato, scompattamento e `copy.json`
  scritti a mano). Ora: argomento → copy via API → **validazione del copy prima del
  render** (max 7 parole, accent presente nel testo, niente lineette lunghe: un copy
  sbagliato viene rigenerato, non renderizzato) → render locale → deposito ordinato →
  gate automatico che conta i PNG e ne controlla peso e dimensioni reali. 20 test verdi.
- INGEST: primo carosello del Ramo C in `Arsenale Caroselli/Preventa/2026-08-27_quanto-tempo-perdi-a-fare-un-preventivo/`
  (6 slide 1080x1080 + copy.json + caption). Nuovo brand `preventa` in carousel-factory,
  con i colori reali già documentati (#101E3E, #FF4D00, #F6F7F9), non inventati.
- BUILD: **cambio di motore dichiarato**. Il Ramo D (Arena browser), indicato dalla task,
  è verificato fermo: `playwright_stealth` non installato, `session_data/` assente (serve
  login Google interattivo), e comunque non compatibile con "nessun passaggio manuale".
  Usato il Ramo C (render locale), progettato a giugno e mai costruito fino a oggi.
  Reparto CF-R5 aggiornato: nuovo ordine `CF-2026-PREVENTA-002` + `ARCHITETTURA.md`.
- LEZIONE: il renderer produceva slide sbagliate **in silenzio da sempre**. Tre bug reali,
  zero errori nel log, visibili solo aprendo il PNG: `@font-face` su percorso disco
  (Chrome blocca le sottorisorse `file://` da una pagina creata con `page.setContent()`,
  quindi il font non si caricava mai), parola accent concatenata fuori dal ciclo delle
  parole (spazi mangiati, "funzionail render"), screenshot scattato prima dei webfont.
  Conferma diretta della regola in `ArenaAI/KNOWN-ISSUES.md`: un run senza eccezioni non è
  un run riuscito. Trovato anche che `npm install` può uscire con **exit 0** lasciando
  `node_modules/puppeteer` senza `package.json`.
- ⚠️ SICUREZZA (B-021): `caroselli - agency/config.py` è tracciato sul repo **pubblico** con
  `ARENA_EMAIL`, `ARENA_PASSWORD` e due API key in chiaro. Peggio di B-020: qui c'è la
  password di un account. Chiave OpenRouter **viva**. CP-20260825-003.

## 2026-08-31 (audit W1 Gael + task W2, Claude)
- AUDIT: W1 di Gael verificata rieseguendo il codice (135 test verdi, 4 libri 24/24 capitoli,
  `kdp pacchetto` exit 0/1 corretti). 6/6 task chiuse davvero.
- INGEST: 6 difetti misurati non coperti dalle sue task — 0 libri pubblicati su 4 scritti,
  B-018 aggravato (4 nicchie/3 autori, "Also by" vuota), 66 falsi positivi trattino, stima
  pagine sbagliata, magazzino a 1 argomento, reparto Lanci senza file eseguibili.
- TASK: emesse 4 task W2 per Gael (FIX -> PIANO -> 5LIBRI -> LANCI) in
  `company/Memory/tasks/TASK-GAEL-20260831-SETTIMANA-02.md`.
- SYNC: sesta collisione ID checkpoint (B-009) risolta rinumerando; hook pre-commit ADR-013
  attivati sulla macchina di Max (hanno bloccato un PDF da 44 MB al primo giro).
