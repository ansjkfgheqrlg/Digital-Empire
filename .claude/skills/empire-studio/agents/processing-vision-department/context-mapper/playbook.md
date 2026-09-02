# context-mapper - Playbook

## Flusso operativo
1. Assemblare un KG degli atomi (relazioni: prerequisito, esempio-di, contraddice).
2. Collegare i nuovi atomi a knowledge-state esistente (cosa l'ecosistema gia' sa).
3. Rilevare gap (concetti citati ma non spiegati) per eventuale ricerca aggiuntiva.
4. Preparare la mappa per il Forge (come raggruppare le note wiki).

## Esempi
- Happy: input valido -> context-mapper produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
