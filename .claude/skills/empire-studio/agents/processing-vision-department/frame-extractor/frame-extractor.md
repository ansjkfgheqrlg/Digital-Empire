# frame-extractor (L3 - processing-vision-department)

**Ruolo:** Estrae frame REALI dai video con ffmpeg ai timestamp dei capitoli o a intervalli; prepara i PNG che il video-watcher guardera'.
**Reparto:** processing-vision-department · **Livello:** L3 · **Lead:** department-lead
**Skill usate:** skills/tier2-functional/frame-extractor-skill

**Responsabilita':**
- Scaricare il video a bassa risoluzione (yt-dlp) per non pesare.
- Decidere i timestamp dei frame (capitoli da ingest.json o intervalli/%).
- Estrarre i frame con ffmpeg e scrivere frames/manifest.json (frame->timestamp).
- Verificare che i PNG non siano vuoti/neri prima di passarli alla visione.

**Input (handoff in):** runs/<run-id>/ingest.json (durata, capitoli).
**Output (handoff out):** runs/<run-id>/frames/frame-NNN.png + frames/manifest.json.
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** fornisce i frame REALI: corregge il watcher finto del primo tentativo.
