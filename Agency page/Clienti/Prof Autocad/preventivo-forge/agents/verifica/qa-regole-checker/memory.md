# Memory — qa-regole-checker

## Conoscenza persistente
- `REGOLE-SACRE.md` è la legge del formato: va riletta a OGNI generazione. Questo agente la incarna.
- `regole-check.json` è la prova di conformità del singolo preventivo (audit per il cliente/socio).
- Namespace memory (se Backbone attivo): `agency/preventivo/qa-regole`.

## Lezioni apprese
- 2026-07-02: le regole si verificano sull'HTML renderizzato (fedele al PDF): serve il `dealer` per
  re-renderizzare. Senza dealer il check è parziale.
- Le regole specialistiche NON si duplicano: R-09→qa-immagini, R-11→Gate B, R-12→Gate C. Questo
  agente le orchestra e aggrega, evitando logiche divergenti.
- R-14 è l'AND di tutte: garantisce che "nessun elemento manca".

## Standard Novacar
Ogni PDF deve essere **indistinguibile per struttura** dal modello `Preventivo BMW Z4 ...pdf`
(contenuto diverso, struttura identica). Il report lo certifica regola per regola.
