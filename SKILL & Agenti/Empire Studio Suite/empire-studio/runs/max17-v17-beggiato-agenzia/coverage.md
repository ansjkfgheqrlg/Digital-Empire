# Coverage — max17-v17-beggiato-agenzia

## Numeri (dichiarazione onesta — copertura PARZIALE dei frame, campionamento sistematico)

- Video: **4h17m00s (15.420s)**, il piu' lungo del lotto `max17`. Scaricato a 360p (158,30 MB) con
  `frame_extractor.py --interval 8 --height 360`.
- Frame densi estratti (1 ogni 8,0s): **1.928** (`frame-0001.png` -> `frame-1928.png`, 0:00 ->
  4:16:56), confermati contro `frames/manifest.json`.
- Frame unici (`scene_detector.py --threshold 10 --interval 8`): **158/1.928 (-91,8%)**.
- **Frame guardati nativamente in questa sessione: 24 su 1.928 totali (1,2%), 24 su 158 unici
  (15,2%)**.
- **Trascrizione audio: 100% letta** — file `.vtt` originale (44.552 righe grezze con caption a
  scorrimento duplicate riga per riga, gia' fornito pronto in `runs/max-17-2026-09/subs/`)
  ripulito con uno script Python locale (deduplica dei cue ripetuti tenendo solo le righe senza
  tag `<c>` ancora in costruzione, nessun contenuto alterato o inventato) in
  `clean_transcript.txt` (5.550 righe uniche), letto per intero in **12 blocchi** da questa
  sessione, dall'inizio (00:00:00) alla fine (04:17:01).

**Questa NON e' una copertura totale dei frame** ed e' dichiarata esplicitamente come
campionamento mirato — non per limite di tempo/budget saltato a caso, ma per una scelta
metodologica motivata sotto.

## Perche' il campionamento e' appropriato per QUESTO video

A differenza di `max17-v16` (evento dal vivo puro, dove quasi tutto il contenuto informativo sta
nell'audio), questo video e' **misto**:

1. **Prima ~2h53m (capitoli 1-6, Intro -> Acquisizione clienti)**: talking-head + lavagna
   Excalidraw disegnata a mano in diretta. Come per v16, i disegni restano fissi a schermo per
   lunghi tratti — `scenes.md` conferma durate fino a **1.888 secondi (31,5 minuti)** senza un
   cambio di scena sopra soglia (`frame-0631`, inizio del capitolo Acquisizione clienti) e
   **1.752 secondi (29,2 minuti)** per il capitolo Pricing (`frame-0411`). In questi tratti il
   contenuto informativo denso e' quasi tutto nel parlato che commenta il disegno via via che
   viene costruito.
2. **Ultimi ~80 minuti (capitoli 7-14, Fulfillment -> Hiring & Scaling)**: **screen-share reale e
   denso** — un documento Whimsical, la piattaforma GoHighLevel (dashboard, funnel builder,
   custom fields, calendario, workflow automation) e Meta Ads Manager, con schermate che
   cambiano molto piu' spesso (click, tab, scroll). `scenes.md` conferma **62 dei 158 frame
   unici (39%) cadono nei soli 2.503 secondi (16,5% della durata totale) del capitolo
   GoHighLevel** — la densita' di scene-change per minuto in questa sezione e' quasi 4 volte
   la media del resto del video, confermando che l'intervallo scelto (8s) e la concentrazione
   del campione qui sono corrette.

Per questo la strategia adottata e' stata: **leggere il 100% dell'audio** (dove sta comunque la
maggioranza delle regole/framework, anche nella parte a screen-share, dove il narratore spiega a
voce quello che clicca) e **concentrare il campione visivo sulle sezioni a schermo condiviso
reale** (piattaforme esterne: Upwork, Fiverr, LinkedIn, GoHighLevel, Meta Ads, Whimsical) dove il
contenuto a schermo aggiunge informazione che l'audio da solo non trasmette (numeri esatti su
dashboard, struttura di menu, campi di un form) — esattamente come richiesto dall'invariante
NO-FINTO: se non ho guardato il frame, non scrivo cosa contiene.

## Come e' stata condotta la copertura

- **Trascrizione**: file sorgente `rvpRQD43wdY.it.vtt` (44.552 righe, gia' presente in
  `runs/max-17-2026-09/subs/` prima di questa sessione, copiato/ingerito in questo run tramite
  `yt_ingest.py --input "https://youtu.be/rvpRQD43wdY" --run max17-v17-beggiato-agenzia`, che ha
  ri-scaricato lo stesso file dei sottotitoli — verificato identico). Deduplicato con uno script
  Python locale (`clean_vtt.py`, salvato nello scratchpad di sessione, non nel repo) che tiene
  solo le righe di testo **senza** tag `<c>` (cioe' le righe "settlement" del cue, non quelle
  ancora in costruzione parola-per-parola) e le deduplica se identiche alla riga precedente —
  nessun contenuto riscritto o inventato, solo compressione meccanica del formato rolling-caption
  di YouTube. Risultato: `clean_transcript.txt`, 5.550 righe con timestamp preservati, letto per
  intero in **12 blocchi da ~500 righe** (righe 1-500, 501-1000, ... fino a 5001-5550).
- **Frame guardati nativamente (24, elencati con motivo della scelta)**:

| Frame | Timestamp | Motivo della scelta |
|---|---|---|
| `frame-0001.png` | 0:00 | Apertura video — verifica del contenuto reale del primo frame (B-roll giornalistico) |
| `frame-0029.png` | 3:44 | Whiteboard Eurostat AI adoption (capitolo 2) |
| `frame-0221.png` | 29:20 | Titolo capitolo "Che nicchia devo scegliere?" |
| `frame-0263.png` | 35:04 | Disegno Blue/Red Ocean con esempio Tesla (verifica contenuto oltre il titolo) |
| `frame-0411.png` | 54:40 | Titolo capitolo "Come prezzare un'offerta?" |
| `frame-0451.png` | 60:08 | Matrice pricing DIY/DWY/DFY x Tempo/Unita'/Risultato (verifica contenuto reale della matrice) |
| `frame-0631.png` | 1:24:00 | Lista numerata a schermo dei 6 metodi di acquisizione clienti |
| `frame-0676.png` | 1:30:08 | Diagramma warm network (mappatura rubrica) |
| `frame-0751.png` | 1:40:08 | Schema messaggio di richiesta referral |
| `frame-0899.png` | 1:59:44 | Struttura email fredda (oggetto + cold reading) |
| `frame-1075.png` | 2:23:12 | Grafico curve cold/organico/ads nel tempo |
| `frame-1139.png` | 2:31:44 | Verifica transizione LinkedIn analytics (contenuto minimo, confermato) |
| `frame-1235.png` | 2:44:32 | Demo reale piattaforma Upwork (job listing) |
| `frame-1299.png` | 2:53:04 | Verifica transizione talking-head post-Fiverr |
| `frame-1401.png` | 3:06:40 | Flowchart Whimsical fulfillment (parte 1) |
| `frame-1440.png` | 3:11:52 | Flowchart Whimsical fulfillment (parte 2) |
| `frame-1511.png` | 3:21:20 | Dashboard reale GoHighLevel (gentes.ai) |
| `frame-1590.png` | 3:31:52 | Funnel steps GoHighLevel (Valutazione/Grazie) |
| `frame-1651.png` | 3:40:00 | Lista funnel GoHighLevel |
| `frame-1687.png` | 3:44:48 | Pipeline Opportunities GoHighLevel (immobiliare) |
| `frame-1745.png` | 3:52:32 | Meta Ads Manager, campagna reale in bozza |
| `frame-1781.png` | 3:57:20 | Titolo capitolo "Scaling & Hiring" |
| `frame-1875.png` | 4:09:52 | Grafico salario/fatturato post-assunzione CTO + SOP |
| `frame-1928.png` | 4:16:56 | Ultimo frame — chiusura video |

- **Metadata**: `ingest.json` letto per intero (titolo, uploader "Giovanni Beggiato", durata
  15.420s, 14 capitoli ufficiali usati per strutturare `video-analysis.md`). `frames/manifest.json`
  interrogato per confermare i timestamp esatti dei frame elencati sopra. `scenes.json`/`scenes.md`
  interrogati per calcolare la concentrazione di scene-change nel capitolo GoHighLevel (62/158
  unici in 2.503s su 15.420s totali).
- **Confronto con la codebase DE**: verificata via `Grep` l'esistenza/contenuto di
  `.claude/skills/agency-scalping/SKILL.md`, `.claude/skills/client-handover/SKILL.md`,
  `.claude/skills/delivery-playbook/SKILL.md`, `.claude/skills/cro/SKILL.md` prima di scrivere i
  gap nella sezione Consigli della pagina wiki — dettaglio dei pattern cercati e risultato in
  quella sezione, non assunti a fiducia.

## Frame illeggibili o parzialmente illeggibili

- Nessun frame tra quelli guardati e' risultato illeggibile o ambiguo — tutti i 24 frame elencati
  hanno mostrato con chiarezza il contenuto atteso (whiteboard, dashboard, form, chart).
- **Non verificato visivamente** (dichiarato, non presentato come letto): la matrice di pricing
  completa con tutte le celle riempite (solo la cella iniziale DIY-Unita' e' stata vista a
  schermo in `frame-0451.png`; le altre celle sono riportate in `video-analysis.md`/`atoms.json`
  come ricostruite dalla sola trascrizione audio, dove l'autore le descrive verbalmente mentre le
  disegna fuori dai frame campionati). Stesso discorso per il dettaglio completo del workflow di
  automazione GoHighLevel (i nodi if/else oltre il primo blocco chiamata non sono stati
  ingranditi a schermo in nessun frame guardato).

## Correzioni / cautele di lettura documentate per trasparenza

- **Verifica dell'apertura video**: il primo frame (`frame-0001.png`, 0:00) non mostra il
  relatore ma una clip di repertorio giornalistico (la Presidente del Consiglio Giorgia Meloni a
  un podio istituzionale) usata come B-roll per il tema "cambiamento epocale" — non e' un errore
  di estrazione (verificato contro `frames/manifest.json`, timestamp coerente con l'indice), e'
  una scelta editoriale di montaggio dichiarata come tale in `video-analysis.md`, non presentata
  come dichiarazione del relatore.
- **`ingest.json` vs sottotitoli gia' pronti**: `yt_ingest.py` ha ri-scaricato `rvpRQD43wdY.it.vtt`
  nel nuovo run invece di limitarsi a copiare il file gia' presente in `runs/max-17-2026-09/subs/`
  — verificato con `wc -l` che il file scaricato ha lo stesso numero di righe (44.552) del file
  gia' pronto, quindi nessuna perdita di dati, solo download ridondante non evitato dallo script.
- I numeri finanziari e le percentuali dichiarati a voce dal relatore (35+ milioni di euro
  gestiti nella nicchia da agenzia+community, 54.000 follower LinkedIn, close rate 30%, etc.)
  **non sono verificati indipendentemente** da questa sessione oltre a quanto confermato
  visivamente nei frame elencati sopra (dashboard GoHighLevel con revenue 10,92K€/conversion
  9,09% — coerente con l'affermazione verbale). Riportati sempre come "dichiarazione dell'autore"
  o "verificato a schermo" a seconda del caso, mai confusi tra loro.

## Riepilogo finale

- **Frame guardati nativamente: 24/1.928 (1,2%) — campionamento mirato dichiarato, concentrato
  sulle sezioni a screen-share reale, non copertura totale.**
- **Trascrizione audio: 5.550/5.550 righe uniche lette (100%)**, corrispondenti a tutte le 44.552
  righe grezze del `.vtt` originale, lette in 12 blocchi.
- **Atomi estratti in `atoms.json`: 31** — 20 confermati anche/soprattutto dall'audio (nessun
  riferimento frame), 11 confermati anche con riferimento frame diretto (KA-002, 003, 006, 009,
  010, 014, 016, 020, 024, 025, 026, 028, 029, 031 — alcuni con doppio frame).
- **Nessun frame e' stato descritto senza essere stato realmente aperto e guardato in questa
  sessione** (regola NO-FINTO) — dove il contenuto di un frame non guardato viene menzionato
  (es. celle intermedie della matrice pricing, dettaglio completo del workflow GoHighLevel), e'
  sempre esplicitamente qualificato come "ricostruito dalla trascrizione audio, non guardato a
  schermo in questa sessione".
- **Nulla di sospetto trovato**: tutti i contenuti a schermo verificati (dashboard, funnel,
  pipeline, campagna Ads) corrispondono esattamente a quanto descritto a voce, incluse le cifre
  (es. conversion rate 9,09% descritto a voce come "9%"). L'unica sorpresa e' editoriale, non di
  contenuto: il primo frame del video e' una clip di repertorio istituzionale, non il relatore.
