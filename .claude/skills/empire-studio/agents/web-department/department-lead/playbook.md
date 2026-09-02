# department-lead - Playbook

## Flusso operativo
1. Classificare l'input: query di ricerca, singola pagina, o sito da crawlare.
2. Delegare la ricerca avanzata a web-researcher (Playwright, no API).
3. Far crawlare i siti rilevanti a site-crawler e estrarre il contenuto a doc-extractor.
4. Far catturare screenshot delle sezioni chiave (UI/diagrammi) per la visione.
5. Consegnare a Processing materiale testuale + eventuali screenshot con trace a URL.

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
