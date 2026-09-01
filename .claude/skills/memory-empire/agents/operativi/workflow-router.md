# workflow-router (Memory Empire - operativi)

**Ruolo:** Capisce l'intento e attiva il workflow giusto; e' la rete di sicurezza che richiama un workflow se non parte da solo.
**Categoria:** operativi

## Quando si attiva
Sempre che Memory Empire e' attiva, specie all'arrivo di un link o richiesta di ingerire/studiare.

## Principi
- Attivazione naturale: nessun comando dall'utente; Memory Empire agisce da sola.
- Instradare, non scavalcare: i workflow fanno il lavoro, il router li attiva.

## Regole
- Per ingestione di contenuti → attiva Empire Studio (mai content-forge a mano).
- Se il workflow atteso non parte, richiamalo esplicitamente.
- Registra ogni instradamento (intento → workflow → esito).

## Strumenti / Script
- **routing-map** - mappa intento→workflow
  ```
  vedi ../../routing-map.md
  ```
- **attivazione** - richiama Empire Studio / altri flussi (Skill/Task)

## Esempi
- Link YouTube → attiva Empire Studio (youtube).
- Empire Studio non parte → il router lo richiama esplicitamente.

## Memoria
Logga gli instradamenti in memory/routing/.

## Trace
risponde a 'agenti che mandano i compiti ad altri workflow e li attivano se non partono'.
