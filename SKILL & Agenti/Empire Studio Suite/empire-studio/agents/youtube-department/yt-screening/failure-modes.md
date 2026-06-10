# yt-screening - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Falsi negativi | video rilevanti scartati | match su titolo+descrizione+tag | shortlist troppo corta | allenta la soglia, includi i borderline con score basso |
| Falsi positivi | clickbait irrilevante incluso | penalizza titoli generici | score alti su contenuti vaghi | richiedi conferma o declassa |
| Focus vuoto | nessun criterio | fallback a recency+views | focus assente | ordina per recency e prendi i top N |
| Metadata poveri | titoli non descrittivi | usa anche durata/capitoli | descrizioni vuote | segnala incertezza, lascia decidere al lead |
| Lingua mista | video in lingue diverse | rileva lingua dal titolo | set multilingua | raggruppa per lingua, prioritizza quella utile |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
