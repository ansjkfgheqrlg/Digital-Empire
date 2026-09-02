# Coverage — max17-v01-artem

## Numeri

- Frame densi estratti (1 ogni 2.0s): **230** (`frame-001.png` → `frame-230.png`, timestamp 0:00 → 7:38)
- Frame unici elencati in `scenes.md`: **117**
- Frame guardati in questo ingest: **117/117 unici (100%)**
- Frame NON elencati (duplicati sotto soglia 3.0): **113** — restano su disco in `frames/` ma non sono stati riguardati singolarmente, perché identici (sotto soglia) a un frame già elencato e già guardato.

## Criterio di selezione

`scene_detector.py` calcola un delta percettivo tra frame consecutivi. Sotto la **soglia 3.0** un frame è considerato "schermata invariata" rispetto al frame precedente già registrato in `scenes.md` (tipicamente: webcam ferma che parla, chat ChatGPT statica mentre l'autore legge, slide Excalidraw tenuta ferma) e viene escluso dalla lista da guardare. Esempio del meccanismo: la riga `#98` di `scenes.md` (`frame-176.png`, ts 5:50) ha una "schermata dura" di **26.0 secondi** (post LinkedIn fermo mentre l'autore commenta a voce), la più lunga del video insieme a `frame-207.png` (18.0s, slide riassuntiva finale).

## Come è stata condotta la copertura

Questo ingest è stato eseguito in **due sessioni** a causa di un errore di rete del server nella prima (nessun file era arrivato su disco al momento dell'interruzione, nonostante tutti i 117 frame fossero già stati osservati in memoria).

- **Sessione 1 e Sessione 2 (rilettura integrale per sicurezza — regola NO-FINTO)**: tutti i 117 frame di `scenes.md` sono stati riletti, in ordine cronologico, a blocchi di **5 Read per messaggio** (mai di più), dalla riga 1 (`frame-001.png`, 0:00) alla riga 117 (`frame-230.png`, 7:38), senza saltarne nessuno. Nessun frame è stato descritto sulla base di un ricordo di sessioni precedenti senza rileggerlo in questa sessione.
- **Sottotitoli inglesi integrali** (`JdAQzAcWR6k.en.vtt`, 1865 righe, caption a scorrimento con testo duplicato riga per riga) letti per intero in 2 blocchi (righe 1-994 e 995-1865), dall'inizio (00:00:00) alla fine (00:07:42).
- **Metadata** (`ingest.json`) letti per titolo, canale/autore, durata, URL, capitoli ufficiali (7 capitoli con timestamp).
- **Confronto con la codebase DE**: lette `.claude/skills/carousel-empire/SKILL.md` (per intero) e `.claude/skills/image/SKILL.md` (sezione modelli AI generation) per fondare `## CONFRONTO CON DIGITAL EMPIRE` e `## CONSIGLI` su nomi di skill reali e verificati, non inventati.

## Frame illeggibili o parzialmente illeggibili

Nessun frame è risultato completamente illeggibile. Alcuni frame presentano testo troppo piccolo o parzialmente sfocato per una trascrizione integrale certa al 100%:

- `frame-004.png` / `frame-005.png` / `frame-006.png` (@0:06-0:10, Instagram Insights del carosello già pubblicato) — il numero esatto di "Views" nel pannello destro non è leggibile con certezza per offuscamento/compressione dello screenshot in due dei tre frame; si è riportata come fonte primaria la dichiarazione verbale ("nearly 100,000 views", 00:00:06) invece di una cifra letta con incertezza. Interactions (12,911), Comments (6,003) e Shares (1,743) sono invece leggibili con confidenza alta in `frame-004.png`/`frame-006.png`.
- `frame-072.png` / `frame-074.png` (@2:22-2:26, documento "THE CAROUSEL BIBLE") — leggero motion blur da scroll; il titolo esatto della sezione "1.2 [...] Work: The Psychology" ha una parola tagliata dal blur, non ricostruibile con certezza al 100%. Statistiche e citazioni nella stessa pagina sono invece leggibili con confidenza alta.
- `frame-134.png` (@4:26, Google Doc "Rest of the slides", Prompt Master 2) — testo piccolo ma nel complesso leggibile; la voce "utility details" nella lista "Match slide 1's" è la meno nitida delle otto voci elencate (confidenza media, non alta come il resto del prompt).
- `frame-196.png` / `frame-199.png` / `frame-200.png` (@6:29-6:32, prompt digitato per "recreate this infographic") — testo su più righe piccole, in parte sfocate. Trascritto come **best-effort con frammenti tra parentesi quadre** nel documento finale, esplicitamente marcato come confidenza "inferito" nell'atomo KA-025 di `atoms.json`, non come citazione integrale certa.
- `frame-224.png` (@7:26, community Skool) — il nome esatto della community non è perfettamente leggibile (assomiglia a "Artemis" ma non riportato come certo); i titoli dei post nella home sono invece leggibili con confidenza alta.

## Correzioni / cautele di lettura documentate per trasparenza

- Nella tabella comparativa iniziale (frame-001/007/011, lavagna Excalidraw "ChatGPT Image for Instagram Carousel"), "Carousel 2 (No reference)" mostra lo stesso claim ("Google just killed SEO. GEO is in.") dell'infografica LinkedIn generata più avanti nel video (frame-201, "Google Search Changed. SEO Alone Is Not Enough."), ma con uno stile grafico diverso (bianco/nero minimale nel teaser iniziale vs. infografica densa e colorata nel risultato finale). Non è stato assunto che siano lo stesso artefatto identico — sono riportati come due varianti dello stesso contenuto/claim in `video-analysis.md`, senza forzare un'equivalenza 1:1 non verificabile dai frame disponibili.
- Il badge/etichetta blu piccola visibile in alto a sinistra della slide 1 nello screenshot Instagram Insights (frame-004) non è stato trascritto come testo certo: la risoluzione non permette una lettura affidabile.
- L'ordine esatto delle slide 4, 6 e 7 del carosello Morning Routine (tra la slide "01 — WAKE UP AT 7AM" e la slide "05 — JOURNAL + PRAY") non è ricostruibile con certezza dai frame disponibili: sono visibili solo thumbnail non ingrandite nel tool Publer (frame-157/158) e un frammento isolato ("tough. / It's about doing a hard thing before the world starts asking for your attention.", frame-153) di cui non è leggibile il numero/etichetta di slide esatto. Riportato con avviso esplicito in `video-analysis.md` invece di essere numerato con falsa certezza.

## Riepilogo finale

- **Frame guardati: 117/117 (100%)**
- **Atomi estratti in `atoms.json`: 40**
- **Prompt integrali recuperati parola per parola: 4** — (1) prompt di copy reale "morning routine" (KA-008), (2) PROMPT MASTER 1 "Slide 1 Prompt" completo con tutte le sezioni incluse le Rules (KA-015), (3) PROMPT MASTER 2 "Slide [X] Prompt" completo (KA-016), (4) prompt meta "GPT Stage 2 Carousel" per generare un carosello dimostrativo sul metodo (KA-031). Il quinto prompt del video (LinkedIn "recreate this infographic", KA-025) è recuperato solo in forma di frammenti leggibili, non integrale — dichiarato esplicitamente come tale.
