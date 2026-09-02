# video-watcher - Playbook

## Flusso operativo
1. **Ricevi** la run dal lead: `runs/<run-id>/` con `ingest.json`.
2. **Assicurati dei frame.** Se `frames/manifest.json` non esiste, invoca
   `frame_extractor.py --run <run-id>`. Per video lunghi alza `--max-frames`
   (1 per capitolo + intermedi).
3. **Leggi il manifest** dei frame (mappa frame->timestamp->capitolo).
4. **Guarda ogni frame.** Per ogni `frame-NNN.png`: Read -> annota cosa si vede
   (UI, testo leggibile, cursore, stato app, demo, risultato). Sii specifico.
5. **Sincronizza col transcript** a quel timestamp.
6. **Scrivi `video-analysis.md`** con le 4 sezioni canoniche.
7. **Estrai `atoms.json`** (atomi con trace) per il forge.
8. **Checkpoint memory** + handoff al verification (visual-verifier) e poi al forge.

## Esempio reale (smoke test eseguito)
Video "Me at the zoo" (jNQXAC9IVRw), 19s, 3 capitoli, 6 frame estratti.
- frame-001 @0:00 [Intro]: ragazzo al centro davanti al recinto elefanti, sguardo
  fuori camera. frame-003 @0:05 ["The cool thing"]: elefante con proboscide
  visibile dietro la spalla mentre nomina le "trunks" (passaggio mostrato).
  frame-006 @0:17 [End]: chiusura con sorriso.
- Risultato: `video-analysis.md` reale, nessuna descrizione inventata. (Honest:
  contenuto minimo perche' e' uno smoke test; in uso reale -> tutorial sostanziosi.)

## Esempio target reale (design system 2h)
- Capitoli -> frame su ogni passaggio: creazione componente, export token, pannello
  proprieta'. Per ognuno: "a 34:12 il cursore clicca Export, appare JSON con i
  color token a schermo" (visibile solo dal frame, non dal transcript).
- Atomi: "Flusso export token: 1) seleziona componenti 2) Export 3) copia JSON"
  con trace `id#34:12 + frame-007.png`.

## Esempio edge (frame illeggibile)
- Frame nero (transizione/fade): segnalalo "non leggibile @ ts", non inventare,
  chiedi a frame-extractor un frame a +2s.

## Handoff in uscita
Al visual-verifier: "analysis pronta, N frame visti, M atomi, X marcati ➕".
