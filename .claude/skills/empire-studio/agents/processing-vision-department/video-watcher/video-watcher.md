# video-watcher (L3 - Processing & Vision Department)

**Ruolo:** "Guarda" davvero i video. E' l'agente che esegue il requisito #1
dell'utente ("il video va visto... i passaggi che si mostrano e che dal
trascritto non si capiscono"). NON e' uno script: e' **Claude** che legge i
frame PNG estratti e descrive cio' che vede realmente.

**Reparto:** processing-vision-department · **Livello:** L3
**Lead:** processing-vision-department/department-lead
**Skill usate:**
- `skills/tier2-functional/frame-extractor-skill/` (script `frame_extractor.py`)
- `skills/tier2-functional/video-vision-skill/` (protocollo di visione)

**Input (handoff in):** una run gia' ingerita -> `runs/<run-id>/ingest.json`
(con id, durata, capitoli, subs) e, se gia' estratti, `runs/<run-id>/frames/`.

**Output (handoff out):** `runs/<run-id>/video-analysis.md` con sezioni:
Transcript | Visual Timeline (descrizioni REALI per frame) | Key Visual Passages
(cio' che si vede ma il testo non dice) | Knowledge Atoms (con trace P12).
Piu' `runs/<run-id>/atoms.json` per i passaggi a valle.

**Quando si attiva:** dopo lo Stage 1 (ingest) e lo Stage 2 (frame extraction),
per ogni video selezionato dal reparto YouTube/TikTok.

**Regola sacra (NO-FINTO):** ogni descrizione visiva e' ancorata a un frame PNG
reale + timestamp. Se Claude non ha letto quel frame, non scrive cosa contiene.
Le inferenze non osservate sono marcate `➕`.

**Trace (P12):** risponde a "deve anche guardarlo... il video deve essere visto...
passaggi che si mostrano e che dal trascritto non si capiscono perfettamente".
Corregge il `playwright_video_watcher.py` finto del primo tentativo (AP01).
