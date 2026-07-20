# yt-seo-publisher - Failure Modes

1. **Quota YouTube API esaurita** → Attendere e riprovare con backoff
2. **Video troppo lungo** → Split o compressione
3. **Errore thumbnail** → Usare thumbnail generata da yt-fliki-renderer
4. **Link Manuale mancante** → Blocco pubblicazione (regola ferrea)

**Regola:** Mai pubblicare senza link al Manuale nella descrizione.