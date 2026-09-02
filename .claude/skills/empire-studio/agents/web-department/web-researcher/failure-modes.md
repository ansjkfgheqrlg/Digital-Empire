# web-researcher - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Query povere | risultati irrilevanti | varia le query | match debole | riformula con sinonimi/operatori |
| SEO spam | fonti di bassa qualita' | filtra per autorevolezza | domini spam | scarta |
| Captcha motore | ricerca bloccata | navigazione sobria | captcha | usa fonti dirette/documentazione |
| Bolla linguistica | solo risultati in 1 lingua | query multilingua | lingua unica | aggiungi query in altra lingua |
| Troppi risultati | rumore | cap top-N | lista enorme | tieni i piu' pertinenti/autorevoli |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
