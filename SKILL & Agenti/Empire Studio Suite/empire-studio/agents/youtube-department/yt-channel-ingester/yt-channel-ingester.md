# yt-channel-ingester (L3 - youtube-department)

**Ruolo:** Ingerisce canali/playlist YouTube: elenca i video, scarica metadata e sottotitoli dei selezionati, prepara le run.
**Reparto:** youtube-department · **Livello:** L3 · **Lead:** department-lead
**Skill usate:** skills/tier2-functional/yt-ingest-skill

**Responsabilita':**
- Eseguire yt_ingest.py in modalita' canale (extract_flat) per elencare i video.
- Applicare il filtro di screening ricevuto da yt-screening.
- Per ogni video selezionato, scaricare info.json + auto-subs + thumbnail.
- Creare una run per video (o una run con videos.json) per il reparto Vision.

**Input (handoff in):** URL canale + lista id selezionati (da yt-screening) + focus.
**Output (handoff out):** runs/<run-id>/ingest.json (kind=channel) + per-video subs/metadata.
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** risponde a 'mando il link di un canale e tu fai screening di tutti i video'.
