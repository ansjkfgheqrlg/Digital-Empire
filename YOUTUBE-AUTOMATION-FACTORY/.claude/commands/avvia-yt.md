---
description: Avvia il flusso completo YouTube Automation Factory per il canale Legami d'Amore (script → Fliki → QC → cartella pronta)
---

# /avvia-yt — Flusso completo Legami d'Amore

Argomento opzionale: `$ARGUMENTS` = URL del video sorgente (competitor) da cui ricavare lo script.
Se assente, prendi il prossimo video non ancora usato da `CALENDARIO-LEGAMIDIAMORE.md`.

Canale target: **sempre `legamidiamore`**. Non toccare mai la config `dosementale`.

Esegui questi passi IN SEQUENZA, senza fermarti a chiedere conferma tra un passo e l'altro
(salvo errore reale o gate bloccante):

## 1. Script + spec (Fasi 1-4, sincrono, veloce)

```
cd 02-AUTOMAZIONI-E-SCRIPTS
python apex7_orchestrator.py run --canale legamidiamore --phase 4 --video-sorgente <URL>
```

Se un gate fallisce (niche-gate, regolatore-originalita, n-grammi), riscrivi lo script in
`05-TEMPLATES-E-KIT/script-adattati/<video-id>.md` seguendo le regole apprese (vedi
`company/Memory/checkpoints/CP-20260819-001.md`: 2400-2700 parole per la voce femminile,
frasi-trigger "lo chiamano X" su riga singola, min 3 concetti nominati, no 8+ parole identiche
al sorgente) e ripeti la Fase 3-4 finché non passa.

## 2. Metadati + SEO (Fase 5 senza upload)

```
python apex7_orchestrator.py run --canale legamidiamore --phase 5 --skip-thumbnail --resume --run-id <run-id>
```

Pulisci a mano `05-TEMPLATES-E-KIT/metadati.json` se i tag auto-generati contengono
etichette-pattern interne invece di keyword vere (bug noto, non ancora fixato in automatico).
Verifica titolo ≤ 60-70 char (penalità SEO se troppo lungo).

## 3. Generazione video reale via Fliki (asincrono — qui sta il collo di bottiglia)

```
python fliki_client.py --canale legamidiamore --run-id <run-id>
```

Annota il `fileId` restituito SUBITO (serve per riprendere senza rigenerare se la rete cade
o il processo si interrompe). Poi avvia il polling in background:

```
python -u fliki_poll_only.py <fileId> "<nome-file>.mp4" 7200
```

Se il polling fallisce per rete, RIPRENDI con lo stesso `fileId` — non rilanciare mai
`fliki_client.py` da capo (spreca credito reale). Se resta `queued` per >20 min è un problema
lato Fliki, non mio: nessuna azione possibile se non aspettare o controllare il dashboard Fliki.

## 4. QC reale

Quando il file .mp4 è scaricato:

```
ffprobe -v error -show_entries format=duration -of csv=p=0 <file>.mp4
python regolatori.py --video-id <video-id> --mp4 <file>.mp4
```

Durata reale deve essere ≥ 720s. Se il gate fallisce, NON procedere allo step 5.

## 5. Cartella pronta

Sposta il video in `VIDEO-PRONTI/video-NN/` (prossimo numero libero) con:
- `video.mp4`
- `copy.md` (titolo/descrizione/tag da `metadati.json`)

**STOP qui.** Nessun upload finché Max non ha messo manualmente una copertina reale nella
cartella — regola permanente, nessuna eccezione (vedi `apex7_orchestrator.py` run_phase_5,
blocco `--video-folder` senza cover → `return False`).

## 6. Upload (solo quando la copertina c'è)

```
python apex7_orchestrator.py run --canale legamidiamore --phase 5 --upload --video-folder ../VIDEO-PRONTI/video-NN --skip-thumbnail
```

Visibilità sempre **Private**, mai pubblico senza conferma esplicita di Max per quel video
specifico.

## Limiti reali di questo comando (dillo sempre a Max se chiede aggiornamenti)

- Il passo 3 (Fliki) non è velocizzabile da qui: è coda del loro server, non mio codice.
- Questo comando gira DENTRO la sessione Claude Code attiva sul PC di Max — non è un cron
  esterno. Se il PC si spegne o va in sleep, o la sessione si chiude, tutto si ferma (i processi
  in background muoiono con il processo padre). Non promettere mai "gira da solo offline" senza
  ricordarlo.
- Aggiorna sempre Max con % di completamento + elenco puntato per fase (regola permanente,
  vedi memoria `feedback_status_update_bullet_percent`).
