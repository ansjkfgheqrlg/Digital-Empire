# tiktok-ingester - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| URL TikTok non standard | yt-dlp non riconosce | normalizza URL | extract fallisce | prova URL canonico |
| Regione bloccata | contenuto non disponibile | rileva geoblock | errore region | segnala, salta |
| Descrizione assente | metadata poveri | usa hashtag | campi vuoti | affidati alla visione |
| Audio-solo | nessun visual utile | rileva tipo | frame statici | tratta come audio, transcript-only |
| Rate limit | 429 | richieste sobrie | HTTP 429 | attendi e ritenta |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
