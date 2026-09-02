# tiktok-ingester (L3 - tiktok-department)

**Ruolo:** Ingerisce video TikTok singoli con yt-dlp (metadata, eventuali subs, thumbnail), preparando la run per la visione densa.
**Reparto:** tiktok-department · **Livello:** L3 · **Lead:** department-lead
**Skill usate:** skills/tier2-functional/tiktok-ingest-skill

**Responsabilita':**
- Eseguire yt_ingest.py su URL TikTok.
- Recuperare metadata (autore, descrizione, hashtag) utili al focus.
- Segnalare la durata per la pianificazione frame densi.
- Gestire i casi senza subs (frequenti su TikTok).

**Input (handoff in):** URL TikTok singolo.
**Output (handoff out):** runs/<run-id>/ingest.json + metadata.
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** ingestione TikTok come per i video YouTube.
