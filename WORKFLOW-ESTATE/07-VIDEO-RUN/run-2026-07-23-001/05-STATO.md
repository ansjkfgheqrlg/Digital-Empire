# 05 — STATO (onestà sul render)

> Regola del lotto: questo file dichiara **esattamente cosa esiste su disco**, mai di più. Se non
> c'è un file video, questo file lo dice, dice perché, e dice cosa serve per averlo.

Run: `run-2026-07-23-001` · Aggiornato manualmente il: 2026-07-23 (poi anche da
`empire/tools/video_pack.py` con l'opzione `--render`, vedi log automatico in fondo).

---

## Ladder di render (da `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-S5-YOUTUBE.md` §2)

### Gradino 1 — Fliki API: **MORTO, non tentato**
`FLIKI_API_KEY` è vuota nel `.env` — fatto verificato dal coordinatore del lotto **prima** di
questo lavoro (dossier di lancio del lotto), non da questo tool: né `video_pack.py` né questa run
leggono mai `.env`, per vincolo esplicito del perimetro di questo lotto. Nessun tentativo di
chiamata API Fliki è stato fatto. Nessuna richiesta della chiave è stata fatta a Max.

### Gradino 2 — script + stock footage + TTS + ffmpeg: **PARZIALE**
Scomposizione onesta dei 4 componenti:
| Componente | Stato | Dettaglio |
|---|---|---|
| Script | **FATTO** | `01-SCRIPT-IT.md` + `02-TTS.txt`, 10 scene, contenuto originale (vedi `00-SCELTA.md` §gate anti-copia) |
| Stock footage | **NON NECESSARIO per questo video** | è un tutorial procedurale: il contenuto visivo è screen recording reale (terminale), non b-roll Pexels — vedi nota in `03-SHOTLIST.md` |
| TTS (audio sintetizzato) | **NON FATTO** | nessun motore di sintesi vocale disponibile nel perimetro di questo lotto ("nessuna dipendenza nuova": niente pip install di motori TTS, niente chiavi API di servizi TTS a pagamento) |
| ffmpeg | **verificato con comando reale** | vedi log automatico sotto — questo tool esegue `ffmpeg -version` davvero, non lo suppone |

### Gradino 3 — consegna del pacchetto-render + errore registrato: **QUESTO È IL RISULTATO DI QUESTA RUN**
Il pacchetto-render (script scena-per-scena, testo TTS pulito, shotlist, pacchetto SEO) è
**completo e validato** (`python empire/tools/video_pack.py --check run-2026-07-23-001` → verde).
Questo è il risultato accettabile e previsto dal piano quando il gradino 1 è morto e il gradino 2
non può chiudersi per mancanza di asset (audio narrato + registrazione schermo), non di script.

---

## Dichiarazione esplicita

**Non esiste, in questa cartella o altrove in questo run, alcun file video (.mp4/.mov/.webm) né
alcun file audio narrato (.wav/.mp3).** Chi apre questa cartella aspettandosi un video pubblicabile
non lo troverà: troverà il pacchetto completo per produrlo.

## Cosa serve esattamente per completare il video (in ordine)
1. **Una registrazione schermo reale** delle scene 1, 3, 5, 6, 7, 8 (terminale + browser): richiede
   un umano (o uno strumento di screen recording) su una macchina con Node.js e Claude Code
   installabili davvero, con un piccolo progetto di test che riproduca il bug descritto nello
   script. Non producibile da questo tool.
2. **Sintesi vocale del testo in `02-TTS.txt`**: serve un motore TTS (locale o servizio esterno) non
   incluso nel perimetro/dipendenze di questo lotto. Alternative note ma non implementate qui:
   motore TTS di sistema, servizio TTS a pagamento, oppure — se si riattiva — Fliki stesso una
   volta che `FLIKI_API_KEY` sarà valorizzata.
3. **Montaggio** con `ffmpeg` (verificato presente in questo ambiente, vedi log sotto) una volta che
   punti 1 e 2 esistono come file.
4. **Grafiche/slide** per le scene 2, 4, 9, 10 (generabili senza registrazione, solo testo/layout).
5. **M-EST-8 — canale + credenziali di pubblicazione**: questo lotto non ha (e non doveva avere)
   accesso a un canale YouTube reale né a credenziali di upload. Serve che Max fornisca: canale
   YouTube di destinazione, e se si vuole automatizzare l'upload, le credenziali OAuth per
   `youtube_uploader.py` / `youtube_uploader_playwright.py` (già presenti in
   `.claude/skills/youtube-automation-factory/scripts/`, fuori dal perimetro scrivibile di questo
   lotto).
6. **URL reale della Parte 1 del Manuale** (e del Manuale completo): `04-SEO-PACK.md` contiene
   placeholder espliciti, non link inventati — vanno sostituiti da Max/dal reparto funnel prima
   della pubblicazione.

---

<!-- VIDEO_PACK:RENDER-LOG:START -->

*Ultimo tentativo di render: 2026-07-24T08:41:05+02:00*

- ffmpeg: PRESENTE — ffmpeg version 8.1.1-full_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers
- audio narrato su disco: NO
- video su disco: NO
- esito: **gradino 2 incompleto**: ffmpeg c'e', manca la traccia audio narrata.
- serve: sintesi vocale di `WORKFLOW-ESTATE/07-VIDEO-RUN/run-2026-07-23-001/02-TTS.txt` + registrazione schermo.
- si resta al **gradino 3**: pacchetto-render consegnato, video NON prodotto.

<!-- VIDEO_PACK:RENDER-LOG:END -->
