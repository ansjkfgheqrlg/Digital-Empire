# doc-extractor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Boilerplate incluso | nav/ads nel testo | euristiche main-content | rumore | ripulisci con euristiche piu' forti |
| Code rotto | snippet sformattati | preserva <pre>/<code> | code mescolato | ripristina i blocchi |
| Tabelle perse | dati tabellari appiattiti | converti tabelle in markdown | tabella assente | ricostruisci dalla struttura |
| Trace mancante | testo senza URL | trace obbligatoria | campo vuoto | riassocia all'URL sorgente |
| Encoding | caratteri rotti | utf-8 robusto | mojibake | normalizza encoding |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
