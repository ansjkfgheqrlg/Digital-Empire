# yt-channel-ingester - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Paginazione canale incompleta | mancano video recenti | playlistend ampio poi filtra | conteggio < atteso | rilancia con playlistend maggiore |
| Rate limit yt-dlp | 429/timeout | richieste sobrie, no download di massa | errori HTTP nei log | attendi e ritenta in batch piu' piccoli |
| Sottotitoli in lingua sbagliata | vtt non in en/it | subtitleslangs multipli | lingua vtt != richiesta | prendi auto-sub disponibili, segnala a transcript-processor |
| Video shorts misti | shorts irrilevanti nel set | filtro per durata minima | durate <60s in massa | escludi gli shorts se il focus e' su long-form |
| ID duplicati tra playlist | stesso video piu' volte | dedup per id | id ripetuti in videos.json | deduplica mantenendo la prima occorrenza |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
