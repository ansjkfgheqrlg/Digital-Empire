# Coverage — max17-v02-beggiato-team

## Numeri

- Frame densi estratti (1 ogni 2.0s): **597** (`frame-001.png` → `frame-597.png`, timestamp 0:00 → 19:52)
- Frame unici elencati in `scenes.md`: **165**
- Frame guardati in questo ingest: **165/165 unici (100%)**
- Frame NON elencati (duplicati sotto soglia): **432** — restano su disco in `frames/` ma non sono stati riguardati singolarmente, perché identici (sotto soglia) a un frame già elencato e già guardato.

## Criterio di selezione

`scene_detector.py` calcola un delta percettivo tra frame consecutivi. Sotto la **soglia 3.0** un frame è considerato "schermata invariata" rispetto al frame precedente già registrato in `scenes.md` (tipicamente: webcam ferma che parla, slide statica tenuta a lungo, pagina non scrollata) e viene escluso dalla lista da guardare — non cancellato, solo non ri-osservato.

Esempio del meccanismo: la riga `#23` di `scenes.md` (`frame-034.png`, ts 1:06) ha una "schermata dura" di **208.0 secondi** — cioè la slide "DA UN LINK AL PIANO MARKETING" resta a video, con solo micro-variazioni (mano che gesticola, cursore che si muove) fino a `frame-138.png` (ts 4:34). Tutti i 103 frame intermedi (035-137) sono sotto soglia e non compaiono in `scenes.md`.

## Come è stata condotta la copertura

- **Righe 1-23 di scenes.md** (frame-001 → frame-034, ts 0:00-1:06): guardate in una sessione precedente di questo stesso task, documentate in `notes_working.md` (frame-001 → frame-030 uno per uno, più un controllo di conferma su frame-031 → frame-060 che copre anche il frame-034 richiesto).
- **Righe 24-165 di scenes.md** (frame-138 → frame-597, ts 4:34-19:52): guardate integralmente in questa sessione, a blocchi di 5 Read, in ordine cronologico, senza saltarne nessuna.
- **Transcript italiano integrale** (`transcript_clean.txt`, 994 righe, caption a scorrimento con testo duplicato riga per riga) letto per intero in 4 blocchi da ~180-220 righe, dall'inizio (00:00:02) alla fine (00:19:53).
- **Metadata** (`yJOCyyP77bA.info.json`) letti per titolo, canale, durata, data upload, view count.

## Frame illeggibili o parzialmente illeggibili

Nessun frame è risultato completamente illeggibile (nessun `[media removed: request limit]` residuo — ogni volta che è comparso nei batch da 5, il frame è stato riletto singolarmente prima di proseguire, come da vincolo tecnico). Alcuni frame presentano testo troppo piccolo per una trascrizione integrale certa al 100%:

- `frame-342.png` (@11:22) — file `copywriter-pmi.md` aperto nell'IDE: il frontmatter e il corpo principale sono leggibili, ma la sezione "Come riscrivi" è tagliata fuori dallo schermo e non ricostruibile da nessun altro frame del video. Alcune singole parole del frontmatter sono segnate con incertezza nel documento principale.
- `frame-410.png` / `frame-411.png` (@13:28-13:30, sezione Piano SEO "Verifiche dal vivo" e tabelle azioni) — testo molto piccolo; la sostanza è stata confermata comunque grazie a `frame-512.png` (stesso testo, zoom/scroll diverso, pienamente leggibile) usato come fonte primaria nel documento finale.
- Radar chart in `frame-006.png` / `frame-558.png` / `frame-559.png`: gli assi e le due sagome (Marco Calzature vs Musto Calzature stima) sono chiaramente distinguibili, ma i valori numerici esatti sui singoli assi del radar non sono etichettati a schermo (il grafico è solo visivo, senza assi numerati) — non riportati come numeri nel documento per questo motivo.

## Correzione di lettura tra frame e audio (documentata per trasparenza)

Durante la trascrizione del frame-439 (Instagram di Marco Calzature) una prima lettura visiva aveva suggerito un numero di follower nell'ordine delle 80K. Il confronto con il transcript audio (00:14:33: *"vediamo che abbiamo circa 41.000 follower. Perfetto, 45..."*) ha corretto la lettura: il numero reale è ~40-45K, coerente con il dato dichiarato nel deliverable (~41K). Il documento finale riporta la cifra confermata dall'audio, non la prima lettura visiva incerta — per rispetto della regola NO-FINTO si segnala qui l'auto-correzione invece di ometterla.
