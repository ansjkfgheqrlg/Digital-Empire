# site-crawler - Playbook

## Flusso operativo
1. Aprire gli URL con Playwright (render JS) e seguire i link interni pertinenti.
2. Rispettare cap di profondita'/pagine e robots.
3. Catturare screenshot delle sezioni visive importanti (per la visione di Claude).
4. Salvare HTML/markdown grezzo e screenshot con trace a URL.

## Esempi
- Happy: input valido -> site-crawler produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
