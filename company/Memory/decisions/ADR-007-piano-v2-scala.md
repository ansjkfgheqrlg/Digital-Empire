# ADR-007 — PIANO V2: la Direttiva di Scala (supera lo standard v1)

- **Data:** 2026-06-11 (sera)
- **Stato:** ATTIVO
- **Decisori:** Max (direttiva integrale dopo analisi completa del workspace — corpus in `maximilian-corpus/direttiva-20260611-scala-v2.md`)

## Contesto
Dopo F1-F4 Max ha analizzato tutto il workspace: la struttura è giusta (ecosistemi corretti,
Memory promossa) ma la SCALA è sbagliata di un ordine di grandezza. Lo standard v1
("scheda agente = file md", "reparto = README", "C-level = 1 agente") è inaccettabile.

## Decisione
1. **Nuova unità di misura:** 1 workflow Empire-grade = il Content Factory di Exponium
   intero (gerarchia, agenti, skill proprie, script reali, QA, runtime, memoria, dry-run).
2. **Board C-Suite:** ogni figura = workflow CF-grade con ≥10 agenti, principi, regole,
   script .py, skill proprie. ~70 agenti totali nel Board.
3. **Reparti:** ogni reparto L2 = team 6-10 agenti con gerarchia interna + 1-5 workflow
   CF-grade. Liste reparti riviste AL RIALZO (Agency: +Delivery, +Account/Supporto,
   +Closing, +Partnership, +QA-cliente). Mega-reparti (Info Business, Content Factory) =
   aziende interne con gerarchia propria a livelli.
4. **Mandato = ecosistema di governo** (team custodi + multi-workflow + enforcement sulle
   Sentinelle). **Sentinelle multi-workflow. Guilds drasticamente più ricche.**
5. **MEMORY si potenzia** per reggere la scala (state per workflow, indici a 2 livelli).
6. **Nuovo organo MAXIMILIAN** (LX, sopra il Board): ≥8 agenti che incarnano carattere/
   standard/decisioni di Max, addestrati sul corpus (`maximilian-corpus/`, mai riassunto).
   Dal V2-3: review-gate "5-bis: Max approverebbe?" in ogni ciclo di fase.
7. **Architettura con skill apposite obbligatoria** (architect-agent, prd-architect-os,
   agent-architecture/SPARC, skill-creator, content-forge) — niente strutture improvvisate.
8. **Knowledge ingestion:** tutte le cartelle di formazione del workspace si trasformano
   in organi interni (mappa in 11-PIANO-V2 §9). Nessuna cartella resta morta.
9. **Roadmap V2-0…V2-8** (11-PIANO-V2 §10) sostituisce la sequenza corrente; si riaggancia
   a F5-F12 con strutture v2. Regola: anticipare i desideri di Max ("fai di più del chiesto").

## Cosa NON cambia
ADR-001..006 restano attivi (10 ecosistemi, memory-first, wrap-non-riscrittura, sync,
backlog, ciclo 9 passi). F1-bis di Gael in corso = BASE valida, non lavoro sprecato.

## Conseguenze
- I DONE WHEN v1 dei dossier 00-09 sono superati dove in conflitto con la scala v2;
  i dossier verranno riscritti/ampliati in V2-2.
- Il costo/tempo di costruzione cresce di un ordine di grandezza: gestito con cicli a
  9 passi, swarm (mai 2 grossi insieme — account condiviso) e fasi disciplinate.

## Contradiction-check
Nessun conflitto con ADR attivi: V2 ALZA gli standard, non li inverte. Verificato contro
ADR-003 (wrap): gli asset esistenti restano wrappati; la scala v2 riguarda le strutture
NUOVE di company/.
