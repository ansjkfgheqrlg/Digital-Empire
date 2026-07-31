# 📏 Regole fisse — Fabbrica Video "Dose Mentale"

> Regole date da Gael più volte (2026-07-29), non richiederle di nuovo. Riferimento tecnico
> completo: [CP-20260729-009](checkpoints/CP-20260729-009.md), [CP-20260729-010](checkpoints/CP-20260729-010.md).
> *(rinumerati da CP-20260729-001/002 nel merge del 2026-07-30 per collisione con due checkpoint
> diversi creati in parallelo da un'altra sessione.)*

## Cosa NON è questo progetto
Il "Manuale Claude Code" è un progetto **morto, non più attivo**. Non nominarlo mai più in
relazione a questo lavoro. Questo NON è un funnel verso un info-prodotto.

## Cosa È questo progetto
Un canale YouTube (comprato già monetizzato, gestito da Gael/Max — non compito di Claude)
il cui unico obiettivo è **guadagnare dalle visualizzazioni**, copiando/adattando i video reali
del canale **@dosementale** (`https://www.youtube.com/@dosementale`) — contenuto reale:
spiritualità, psicologia, saggezza biblica/buddista, motivazione/storie di vita, salute e
benessere per un pubblico adulto/anziano.

## Flusso obbligatorio per ogni video
1. Scegliere un video reale da `@dosementale` per velocity (views/età, soglia maturità 24h) —
   stesso criterio già usato in F2 di `apex7_orchestrator.py`, applicato però su questo canale,
   non sui 20 canali AI del vecchio niche-scout.
2. Scaricare il transcript reale (yt-dlp `--write-auto-sub`) e riscrivere (non copiare verbatim)
   uno script adattato sullo stesso argomento reale, formato HOOK/INTRO/CORPO/CTA.
3. Copertina: `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/arena_thumbnail.py` (Arena.ai
   via Playwright, profilo persistente `chrome-profile-arena/` — sessione già loggata, non
   richiedere login di nuovo salvo scadenza). **La copertina si ADATTA da quella reale del video
   sorgente, non si inventa** (regola di Gael, 2026-07-31): scaricare
   `https://i.ytimg.com/vi/<VIDEO_ID>/maxresdefault.jpg` in `05-TEMPLATES-E-KIT/source-thumbnail/`,
   allegarla alla chat Arena e chiedere una MODIFICA (posa + testo) mantenendone il linguaggio
   visivo. **Se la chat non funziona, chiuderla e aprirne una nuova** invece di insistere.
4. Video: `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py` (API Fliki reale).

## Standard qualità obbligatori (verificare sempre col file reale, non fidarsi della sola risposta API)
- **Durata ≥ 12 minuti** — **causa reale trovata (2026-07-30, dopo 5 run reali sprecati a
  sospettare il parametro `duration`)**: la durata di un video "script" dipende dalla lunghezza
  REALE del testo (parole da narrare a ritmo naturale, ~140 parole/min in italiano), non dal
  campo `duration`. `duration` in MINUTI e' stato provato in 4 combinazioni diverse (assente,
  `720` creduto erroneamente secondi, `0` = "usa il testo cosi' com'e'", `15` minuti reali) **con
  la stessa identica struttura a 4 scene, ottenendo SEMPRE 230.592s identico** — prova che il
  parametro non era la leva. La vera causa: lo script scritto aveva solo ~560 parole (~230s di
  lettura naturale) invece delle ~2.000 parole necessarie per 12-15 minuti. **Prima di generare,
  contare le parole reali dello script e stimare `parole/140` minuti — se sotto 12, espandere il
  contenuto (non il parametro API) prima di lanciare la generazione.** Verificare comunque sempre
  con `ffprobe -show_entries format=duration` sul file scaricato.
- **Voce di alta qualità** — non il primo risultato di un filtro genere andato in fallback.
- **Sottotitoli sempre presenti, precisi, senza errori** — richiede un `subtitlePresetId` REALE,
  ottenibile solo cliccando "Copy subtitle preset ID" su `fliki.ai/info/subtitle` via Playwright
  (non è nell'HTML statico né in chiamate di rete intercettabili). I 30 preset reali sono in
  `memory/fliki_subtitle_presets.json` (`fliki_subtitle_presets.py`), elencati per riferimento.

## ⛔ Configurazione Fliki APPROVATA da Gael — non modificare (2026-07-31)
Gael ha visto il video v8 e ha detto: **"il video era perfetto, non modificare le regole e non
cambiare niente, d'ora in poi falli tutti così"**. I valori esatti in `fliki_client.py`:
```
"subtitlePresetId": "builtin-legacy-bold"
"highlightSubtitles": True      # effetto karaoke parola-per-parola: È VOLUTO
"duration": 720                 # inerte (l'API vuole 1-15 minuti), ma fa parte dell'approvato
"visuals": "stock"
"sceneBreakdown": "lineBreak"
"aspectRatio": "16:9", "resolution": "1080p"
```
Avevo proposto di passare a un preset più grande con `highlightSubtitles: False` (frasi intere):
**proposta respinta, non riproporla.** L'effetto karaoke è lo stile voluto, coerente col canale
sorgente. Se un output soddisfa i requisiti dichiarati e resta solo una questione di gusto: si
segnala e si CHIEDE, non si cambia di propria iniziativa.
- **`duration`**: per riferimento, l'API lo accetta in MINUTI (range 1-15), quindi 720 è fuori
  range e viene ignorato — la durata dipende dal NUMERO DI PAROLE dello script, mai da questo
  campo. Documentazione: `developer.fliki.ai/docs/api/generate/video`.

## Limite noto — velocità Fliki (non un bug da rincorrere in loop)
Verificato a fondo (documentazione ufficiale + test reali ripetuti): l'API Fliki non espone
nessun parametro di priorità/velocità/tier. Il tempo "queued" (~860-970s, ~14-16 min) osservato
è lato server, praticamente costante indipendentemente da contenuto/durata richiesta — non
riducibile lato client. Se serve sotto i 10 minuti totali, l'unica leva è un eventuale tier a
pagamento più alto sull'account Fliki (da verificare sul loro dashboard, non nel codice).

## Registro auto-miglioramento — errori reali fatti, da non ripetere (2026-07-30)
Gael ha chiesto esplicitamente un vero automiglioramento: ogni errore va salvato e mai ripetuto.
Dettaglio esteso nella memoria persistente Claude `errori_da_non_ripetere_fabbrica_video.md`.
Sintesi:
1. **Buffering output**: avvolgere `sys.stdout` in `io.TextIOWrapper` grezzo per fix di encoding
   rende l'output invisibile per decine di minuti quando rediretto su file (buffering a blocchi,
   non a riga). Usare `sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)` o
   `flush=True` sui print, e verificare SEMPRE che l'output compaia in tempo reale.
2. **`duration` Fliki**: vedi sopra — non è la leva, è la lunghezza reale del testo.
3. **Filtro voce case-sensitive**: l'API ritorna `"MALE"/"FEMALE"` maiuscolo, un confronto con
   `"male"` minuscolo non trova mai nulla — sempre confronti case-insensitive su campi da API.
4. **Sottotitoli**: mai assumere che un parametro abbia funzionato — verificare col file mp4
   reale (ffmpeg frame-extract) prima di dichiarare un video pronto.
5. **Canale sbagliato**: generato un intero video sul funnel Claude Code (morto) prima di
   verificare che Gael intendesse @dosementale — quando l'utente fa riferimento a qualcosa "già
   detto" non presente nel contesto, verificarlo concretamente prima di costruire.
6. **Modalità Arena sbagliata**: generata la prima copertina in Battle Mode invece di Direct+Max
   — quando l'utente nomina un'opzione UI specifica, esplorare l'interfaccia reale prima di usare
   un default plausibile.
7. **File di debug cancellati prima di leggerli**: non ripulire un artefatto diagnostico nella
   stessa risposta in cui lo si genera.
8. **Non terminare processi in background senza permesso esplicito**: un processo lento ma vivo
   (CPU bassa, nessun crash, entro un timeout interno noto) non va ucciso unilateralmente —
   butta via tempo reale già speso lato server. Chiedere prima.
9. **Doppio-wrapping di stdout** (2026-07-30): il fix del punto 1 applicato in due moduli dello
   stesso processo (`fliki_client.py` importa `apex7_orchestrator`) crea due `TextIOWrapper` sullo
   stesso buffer — il GC del primo chiude il buffer del secondo → `ValueError: I/O operation on
   closed file`. Usare SEMPRE `reconfigure()`, mai un nuovo `io.TextIOWrapper`.
10. **Scena troppo lunga = job Fliki bloccato in coda all'infinito** (2026-07-30): un blocco da
    594 parole (~4 min in una sola scena) ha tenuto un job in `queued` per oltre un'ora senza mai
    passare a `processing` né dare errore. Dividere sempre il testo in scene da max ~130 parole
    (mai a metà frase): `_split_into_bounded_chunks` in `fliki_client.py`. Un `queued` che supera
    di molto i 14-17 min normali è sintomo di scene troppo grandi, non di lentezza.
11. **Residui del progetto morto nel CODICE, non solo nei contenuti** (2026-07-31): dopo il pivot,
    `build_prompt()` di `arena_thumbnail.py` conteneva ancora hardcoded l'estetica "terminal/
    console, arancione #fb4604, tech coding tutorial" del Manuale Claude Code — il prompt inviato
    contraddiceva il brief riscritto. Anche `candidati-video.json` aveva ancora i video del vecchio
    canale tech. Dopo un pivot, fare grep del vecchio dominio anche dentro il codice (stringhe
    hardcoded, prompt, default CLI, nomi file).
12. **Non salvare come candidato un'immagine caricata da noi**: raccogliere solo i `src` comparsi
    DOPO l'invio del messaggio, altrimenti la miniatura sorgente allegata finisce tra i risultati.

13. **Il pivot va fatto anche sul MOTORE, non solo sui contenuti** (2026-07-31): tutto
    `apex7_orchestrator.py` F1→F5 era rimasto cablato sul funnel morto (scouting fra 20 canali AI,
    20 idee pre-scritte per il Manuale, keyword fissa "claude code", CTA verso il Manuale) e un
    run end-to-end sovrascriveva gli artefatti reali. Inoltre `agents.py` (simulazione ritirata)
    scriveva nella stessa cartella dei file veri e i suoi log finti alimentavano
    `learned_rules.json`. Dopo un pivot: lanciare la pipeline e leggere OGNI artefatto rigenerato.
14. **Keyword = porzione contigua del titolo** (2026-07-31): `seo_score.py` cerca la keyword come
    sottostringa esatta — parole sparse ("camminare contano davvero") non vengono mai trovate.
    Verificare con `keyword in titolo.lower()`.

## Come gira oggi il flusso (riscritto il 2026-07-31)
`python apex7_orchestrator.py run --phase 6` esegue:
- **F1** — canale target FISSO @dosementale, confermato su video/viste/età reali. L'indice Cash
  Cow e' riportato ma NON blocca (era il gate di scelta fra 20 canali, decisione che non esiste
  piu': il canale e' una scelta di business).
- **F2** — sceglie il video da copiare per velocity reale. **Gate reale della pipeline**: se
  nemmeno il migliore supera 20 viste/ora, fallisce onestamente.
- **F3** — usa lo script adattato in `05-TEMPLATES-E-KIT/script-adattati/<videoId>.md`. Se manca,
  scarica il transcript REALE (yt-dlp), scrive `<videoId>.DA-SCRIVERE.md` col materiale e si
  ferma: lo script va riscritto a mano (mai copiato verbatim, mai generato a runtime). Blocca
  anche se lo script e' sotto i 12 minuti stimati.
- **F4/F5** — spec Fliki, metadati (keyword italiana dal nostro titolo) e brief miniatura con la
  copertina reale del video sorgente scaricata automaticamente.
Poi: `arena_thumbnail.py` (copertina) e `fliki_client.py --file-name <nome>` (video).

## Esito verificato (2026-07-31)
Video reale conforme a tutti gli standard: 727s (12min 7s), voce maschile reale (Calimero),
sottotitoli visibili verificati su più fotogrammi, 19 scene bilanciate, nessun blocco in coda.
