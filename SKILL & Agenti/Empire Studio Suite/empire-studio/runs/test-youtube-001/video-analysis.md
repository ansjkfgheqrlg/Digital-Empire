# Video Analysis - "Me at the zoo" (jNQXAC9IVRw)

- **Source:** https://www.youtube.com/watch?v=jNQXAC9IVRw
- **Durata:** 0:00:19 · **Capitoli:** 3 · **Frame estratti:** 6
- **Visione eseguita da:** Claude (lettura nativa dei PNG estratti con ffmpeg) - NON da uno script
- **Nota onesta:** questo e' lo SMOKE TEST del motore (video storico di 19s, contenuto minimo).
  Serve a provare che la pipeline ingest -> frame veri -> visione reale funziona end-to-end.
  In uso reale il target sarebbe un tutorial sostanzioso (es. 2h design system).

## Transcript (reale, da yt-dlp)
> "All right, so here we are in front of the elephants. The cool thing about
> these guys is that they have really, really, really long trunks. And that's
> cool. And that's pretty much all there is to say."

## Visual Timeline (descrizioni REALI dai frame osservati)
- **0:00:00 (frame-001.png) [Intro]** - Esterno di uno zoo. Inquadratura ravvicinata
  di un giovane uomo (capelli scuri corti, giacca grigia con interno rosso) al centro,
  espressione neutra, sguardo leggermente fuori camera (sta iniziando a parlare). Sullo
  sfondo: recinto degli elefanti con sbarre metalliche, parete rocciosa, fieno a terra,
  due elefanti. Ripresa amatoriale, bassa risoluzione (digitale primi anni 2000).
- **0:00:05 (frame-003.png) ["The cool thing"]** - Il ragazzo e' girato leggermente,
  guarda verso la camera mentre parla. Dietro la sua spalla destra un elefante e'
  ben visibile, con la proboscide distesa - coincide col momento in cui nel transcript
  nomina le "long trunks". Il "passaggio mostrato" (l'elefante reale dietro di lui)
  e' visibile solo dal video, non dal testo.
- **0:00:17 (frame-006.png) [End]** - Primo piano del ragazzo con un accenno di
  sorriso, sguardo in camera: sta chiudendo ("that's pretty much all there is to say").
  Elefanti ancora sullo sfondo.

## Key Visual Passages (cio' che si vede ma il testo non dice)
- L'ambiente e' uno zoo reale all'aperto con recinto in sbarre e parete rocciosa
  (trace: frame-001/003/006). Il transcript dice solo "elephants".
- La sincronia gesto/parola: l'elefante con proboscide compare in quadro proprio sul
  riferimento alle "trunks" (trace: frame-003 @ 0:05).

## Knowledge Atoms (con trace P12)
- **Atom:** Il video e' il primo caricato su YouTube (rilevanza storica), girato come
  clip amatoriale a camera fissa allo zoo di San Diego.
  ➕ (contesto noto, non dal frame) · trace: jNQXAC9IVRw#0:00 + frame-001.png
- **Atom:** Struttura della clip = intro a camera (0:00) -> punto centrale "trunks"
  con soggetto inquadrato + elefante (0:05) -> chiusura (0:17).
  trace: jNQXAC9IVRw#0:05 + frame-003.png

## Metadata
- Tools usati: yt-dlp (ingest + subs + video 360p), ffmpeg (6 frame ai capitoli/intervalli).
- Frames + timestamp: vedi `frames/manifest.json`.
- **Trace (P12):** ogni descrizione visiva e' ancorata a un frame PNG reale + timestamp.
  Nessuna descrizione inventata (regola NO-FINTO).
