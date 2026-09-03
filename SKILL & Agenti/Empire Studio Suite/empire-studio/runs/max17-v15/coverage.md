# Coverage — max17-v15 (`sno_IcNbYFM`)

## Il numero vero

- **Frame densi presenti su disco**: **523** file `frame-NNN.png` in `frames/` (+ `manifest.json`).
  Estratti a 1 ogni 4.0s (2092s di durata / 4s ≈ 523).
- **Frame unici indicati da `scenes.json` / `scenes.md`**: **226** (soglia 3.0, riduzione 56,8%).
  *Nota tecnica*: `scene_detector.py` era stato lanciato una prima volta coi valori di default
  (assumendo un intervallo di estrazione di 2.0s) producendo timestamp dimezzati e sbagliati in
  `scenes.md`. Rilanciato con `--interval 4` (il vero intervallo di questo run, confermato da
  `frames/manifest.json`): stessa selezione di 226 frame unici, timestamp ora corretti e coerenti
  coi capitoli di `ingest.json` (0:00→34:48).
- **Frame guardati davvero da me**: **82 distinti**, tutti a schermo pieno (nessun ritaglio/zoom
  usato in questo run: i documenti Notion con i prompt erano già a font leggibile a 1280×720, a
  differenza del codice terminale di v07-rizzo).
- **Copertura sull'elenco `scenes.md`**: **82 / 226 = 36,3%**.
- **Copertura sul totale dei frame estratti**: 82 / 523 = 15,7%.

**Non gonfio il numero.** Sotto c'è esattamente cosa manca e perché non cambia la sostanza
dell'analisi.

## Metodo seguito

1. Lettura integrale di `transcript_clean.txt` (voce narrante, un blocco unico di ~849 righe con
   timestamp) prima di aprire qualunque frame, per orientarmi sulla struttura del video.
2. Rigenerazione di `scenes.json`/`scenes.md` con `scripts/scene_detector.py --run max17-v15
   --interval 4` (il run non li aveva, a differenza di v01-artem/v07-rizzo che li avevano già).
3. Lettura dei frame **a gruppi di 4-6 per messaggio**, mai di più, seguendo l'ordine cronologico
   di `scenes.md` e privilegiando, dentro ogni capitolo di `ingest.json`, i frame con schermate di
   testo denso (report demo, dashboard finale, documento Notion con i 6 prompt, SKILL.md, file
   tree `.claude/skills/`) rispetto ai frame ripetuti di solo talking-head.
4. Nessun frame è risultato troppo piccolo per essere letto senza zoom: il documento Notion con i
   prompt e la dashboard HTML finale sono entrambi testo a piena risoluzione 1280×720, leggibili
   direttamente.

## Frame guardati — elenco (82, in ordine cronologico)

001, 002, 005, 006, 007, 008, 009, 011, 014, 017, 019, 020, 027, 031, 035, 039, 042, 046, 050,
051, 067, 070, 072, 074, 077, 083, 088, 092, 096, 111, 115, 121, 128, 131, 141, 151, 157, 162,
165, 183, 193, 201, 209, 217, 221, 229, 241, 245, 249, 255, 285, 301, 306, 318, 328, 334, 343,
353, 360, 364, 377, 392, 399, 408, 415, 419, 432, 439, 445, 447, 461, 476, 482, 484, 488, 490,
498, 509, 513, 517, 521, 523

## Cosa NON ho guardato, e perché non cambia il risultato

**144 frame dell'elenco `scenes.md` (unici) non sono stati aperti**, oltre ai ~297 frame densi già
esclusi dallo scene-detector come duplicati sotto soglia. Il video è quasi interamente **screen
recording statico + talking-head**, non un disegno a mano libera come in v07-rizzo: la maggior
parte dei frame non aperti sono di due tipi, entrambi non-lacune di contenuto:

| Tipo di frame non aperto | Esempio di blocco | Perché non è una lacuna |
|---|---|---|
| Talking-head puro (nessun testo a schermo, solo Beggiato che parla) | 054-059, 098-108, 135-140, 168-182, 224-228, 259-265, 287-300, 369-376, 380-391 (parziale), 420-431 (parziale), 450-460 (parziale), 462-475, 500-508 (parziale) | Il contenuto verbale è integralmente coperto da `transcript_clean.txt`, letto per intero |
| Scroll intermedio della stessa schermata (stessa pagina Notion/dashboard/editor, poche righe più in basso o più in alto) | es. 022-026, 040-041, 043-045, 052-066, 078-082, 084-091, 093-095, 116-120, 122-127, 132-140, 142-150, 152-156, 158-164, 184-192, 194-200, 202-220 (parziale), 222-228 (parziale), 230-254 (parziale), 256-284 (parziale), 286-300, 302-334 (parziale), 335-364 (parziale), 365-419 (parziale), 420-461 (parziale), 462-523 (parziale) | Aperto il frame iniziale e finale di ogni sequenza di scroll: il contenuto testuale pieno è ricostruito dai frame guardati immediatamente prima/dopo |

**Sezioni specifiche non lette per intero, dichiarate onestamente**:
- Il codice sorgente di `metriche.py`, `costruisci_command_center.py`, `verifica_dashboard.py` è
  stato visto negli editor durante la generazione ma **non ingrandito riga per riga** — a
  differenza dei documenti Notion (che erano già a font leggibile), il codice negli editor passava
  troppo velocemente fra un frame e l'altro per una trascrizione carattere-per-carattere onesta.
  L'analisi riporta quindi solo ciò che i prompt e le didascalie del Notion dichiarano sul codice,
  mai il codice stesso come se fosse stato letto.
- I **sette documenti di riferimento** citati per ogni skill (come ragiona un CFO, quadri di
  analisi, glossario metriche, specifica dashboard, formule coi limiti, modello dati, trappole
  QuickBooks) non sono mai aperti singolarmente a schermo nel video: solo il loro elenco e la loro
  funzione sono dichiarati nel documento Notion (frame-360).
- Le **"dodici tabelle" del Command Center** menzionate a voce non sono tutte mostrate per intero:
  la dashboard finale ne mostra diverse (alert, executive summary, margine, crediti, margine per
  servizio) ma non è confermato che tutte e dodici siano state viste a schermo in questo video.

## Frame illeggibili

Nessun frame è risultato illeggibile. Diversamente da v07-rizzo (terminale piccolo, necessità di
zoom 4-9x), in questo video tutti i testi a schermo — report demo, documento Notion, SKILL.md,
file tree, dashboard finale — sono già a dimensione leggibile nei 1280×720 nativi.

## Trascrizione

- Sorgente: `sno_IcNbYFM.it.vtt`, già ripulita in `transcript_clean.txt` (849 righe con timestamp
  al secondo, 1 riga per frase incrementale, stile "captions a scorrimento" YouTube auto-generate).
- **Letta integralmente**, in un unico passaggio prima di aprire i frame.
- Nessuna discrepanza rilevante fra trascrizione e frame è stata riscontrata sui numeri chiave
  (93 giorni, 4.198.187, 132.727, ecc.): questi compaiono scritti nella dashboard HTML stessa,
  quindi trascritti da testo statico ad alta confidenza, non da audio.

## Riepilogo copertura per capitolo (dai capitoli dichiarati in `ingest.json`)

| Capitolo | Timestamp | Frame guardati nel blocco | Stato |
|---|---|---|---|
| Introduzione | 0:00–1:16 | 001, 002, 005, 006, 007, 008, 009, 011, 014, 017, 019 | coperto |
| Demo del report finale dell'AI CFO | 1:16–3:15 | 020, 027, 031, 035, 039, 042, 046 | coperto (dashboard letta per intero) |
| Connessione a QuickBooks via API | 3:15–7:21 | 050, 051, 067, 070, 072, 074, 077, 083, 088, 092, 096 | coperto |
| Creazione del modello dati Python | 7:21–10:42 | 111, 115, 121, 128, 131 | coperto (Prompt 1 letto per intero) |
| Collegamento QuickBooks e download dati | 10:42–15:56 | 141, 151, 157, 162, 165, 183, 193 | coperto (Prompt 2 letto per intero) |
| Integrazione parametri esterni | 15:56–20:14 | 201, 209, 217, 221, 229, 241, 245, 249, 255 | coperto |
| Costruzione del motore di calcolo deterministico | 20:14–24:32 | 285, 301, 306, 318, 328, 334, 343, 353 | coperto (Prompt 3 + bug del test di determinismo letti per intero) |
| Logica degli alert e segnali di rischio | 24:32–27:34 | 360, 364, 377, 392, 399 | coperto (Prompt 4 letto per intero) |
| Import delle skill (Analista Finanziario + AI CFO) | 27:34–30:29 | 408, 415, 419, 432, 439, 445, 447, 461 | coperto (SKILL.md di ai-cfo letto per intero) |
| Creazione della dashboard e prompt anti-allucinazione | 30:29–32:12 | 476, 482 | coperto (Prompt 5 + Prompt 6 letti per intero) |
| Risultato finale e considerazioni conclusive | 32:12–34:52 | 484, 488, 490, 498, 509, 513, 517, 521, 523 | coperto (dashboard finale confrontata frame-per-frame con la demo iniziale) |

---

*Coverage compilata il 2026-09-03 · Empire Studio · run `max17-v15` · NO-FINTO: PASS con copertura
parziale dichiarata (82/226 scene uniche, 82/523 frame totali). Tutti i 6 prompt del video, le
sezioni chiave del report demo e del risultato finale, e il `SKILL.md` di `ai-cfo` sono stati letti
per intero, non riassunti a memoria.*
