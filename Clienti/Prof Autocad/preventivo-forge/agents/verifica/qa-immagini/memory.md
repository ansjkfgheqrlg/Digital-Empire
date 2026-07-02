# Memory — qa-immagini

## Conoscenza persistente
- R-09 è la regola sacra più a rischio: le foto sono il cuore commerciale del preventivo.
- Namespace memory (se Backbone attivo): `agency/preventivo/qa-immagini`.

## Lezioni apprese
- 2026-07-02: il template DEVE usare `object-fit: contain` (mai `cover`): con `cover` le auto
  venivano ritagliate. Il gate ora verifica esplicitamente l'assenza di `cover`.
- Le foto vanno incorporate in alta risoluzione (scraper usa `rule=mo-1600`), ridimensionate a
  ~1500px lato: nitide ma PDF non enorme.

## Standard Novacar
2 foto grandi per pagina, dimensione uniforme, proporzioni originali rispettate. Tutte presenti.
