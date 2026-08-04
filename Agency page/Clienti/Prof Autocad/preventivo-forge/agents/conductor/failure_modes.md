# Failure modes — conductor

| Failure | Sintomo | Prevenzione | Rilevazione | Recupero |
|---|---|---|---|---|
| Scraping bloccato (anti-bot) | HTML con marker blocco / vuoto | profilo persistente + UA + consenso | `_looks_blocked()` | headful o `--manual`; exit 2 |
| S1 senza foto | `images=[]` | scroll lazy-load + retry | Gate A | stop, richiedi manuale |
| Prezzo non estratto | `price_listed_eur=null` | JSON-LD + fallback testo | Gate A / S4 ValueError | stop, verifica annuncio |
| Schema non valido | `_schema_errors` | mappe robuste in parser | `validate_against_schema` | warning; stop se critico |
| Half B assente | S3/S5 `skipped` | import difensivo | `_optional()` None | nota handoff (non errore) |
| Gate rosso ripetuto | stesso gate fallisce 2× | retry mirato | contatore run | STOP + report umano |
| Dealer inesistente | `FileNotFoundError` | `list_dealers()` prima | load_dealer | messaggio con dealer disponibili |
| Scrittura fuori run dir | file inattesi | path via RunContext | review trace | bug: correggi, non consegnare |
