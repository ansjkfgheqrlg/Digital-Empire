# department-lead - Playbook

## Flusso operativo
1. Ricevere le run pronte dai reparti di ricerca (YouTube/TikTok).
2. Far estrarre i frame (frame-extractor) secondo la strategia (capitoli o intervalli).
3. Attivare il video-watcher per la visione reale dei frame.
4. Coordinare transcript-processor, knowledge-extractor e context-mapper.
5. Consegnare al Forge il pacchetto analizzato (analysis + atoms) con trace.

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
