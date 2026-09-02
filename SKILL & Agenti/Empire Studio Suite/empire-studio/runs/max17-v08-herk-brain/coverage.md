# Coverage — max17-v08-herk-brain (DTCyvo6cC54)

## Range guardato
0:00 → 30:58 (intero video, 1859s / 30m59) — copertura totale end-to-end.

## Frame
- **130/130 frame unici guardati su 930 densi estratti** (1 frame ogni 2.0s dal video sorgente).
- Criterio di selezione: soglia di deduplicazione visiva **3.0** (delta percettivo minimo tra frame consecutivi per essere considerato "cambio di schermata reale").
- **800 frame duplicati esclusi** automaticamente in fase di ingest (identici o quasi-identici a un frame già elencato in `scenes.md`) — nessun frame è stato cancellato dal disco, restano tutti in `frames/`, ma solo i 130 elencati in `scenes.md` sono stati effettivamente osservati e descritti.
- Ordine di lettura: sequenziale, in blocchi da 5, seguendo esattamente l'ordine cronologico di `scenes.md` (frame-001 → frame-930).

## Trascrizione
- Fonte: `DTCyvo6cC54.en.vtt` (formato WebVTT con caption a cascata parola-per-parola, fortemente ridondante — 8384 righe grezze).
- Ripulita con script Python di deduplica (rimozione dei blocchi che sono prefisso stretto del blocco successivo) → `transcript_clean.txt`, 1047 righe, letta **per intero** dall'inizio alla fine.
- Nessun file `.it.srt` presente nella run dir (solo `.en.vtt`); il file italiano menzionato nel brief non esiste su disco — usato solo l'inglese disponibile.

## Frame illeggibili o parzialmente illeggibili (dichiarati)
- `frame-232.png @ 7:42` — slide di transizione "Table-stakes and plumbing", fortemente sfocata da motion-blur editoriale del video stesso; solo il titolo è leggibile, il corpo testo è illeggibile.
- `frame-732.png` → `frame-756.png` (@ 24:22–25:10, una decina di frame) — sequenza LightRAG **volutamente sfocata dall'autore** ("I'm going to have to blur some of this stuff out because this is legitimately my entire second brain in our business"). Blur editoriale intenzionale, non un limite dell'estrazione. Un solo frame in questa finestra (`frame-745/746/749.png @ 24:48-24:56`) risulta leggibile perché lo zoom si ferma temporaneamente su un nodo con pannello proprietà aperto ("7-Day AIS Challenge").
- Nessun altro frame dei 130 è risultato completamente illeggibile; alcuni screenshot di codice/JSON sono parzialmente troncati a bordo schermo (es. `entities.sample.json` commento troncato, `context-window.md` ultima riga di "Symptoms include the agent ignoring [...]" tagliata) — riportati nel report con "[tagliato]"/"[troncato]" dove applicabile, mai completati per invenzione.

## Note metodologiche
- Nessun frame è stato descritto "alla cieca": ogni contenuto testuale integrale riportato in `video-analysis.md` e `atoms.json` è stato letto direttamente da almeno un frame reale, spesso ricostruito unendo 2-3 frame consecutivi che mostrano la stessa schermata con lo scroll avanzato (es. `Level 2/CLAUDE.md` ricostruito da frame-315 + frame-318; `Level 4/CLAUDE.md` ricostruito da 5 frame in sequenza di scroll).
- Il file `ingest.json` conferma i capitoli ufficiali YouTube usati come scheletro del walkthrough cronologico.
