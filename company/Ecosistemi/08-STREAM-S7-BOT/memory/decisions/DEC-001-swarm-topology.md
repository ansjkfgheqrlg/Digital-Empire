# DEC-001: Migrazione a Swarm Topology

**Timestamp**: 2026-07-23
**Fase**: Fase 4 (Target Selection & Vision Refinement)
**Principi Collegati**: P07 (Three-Level Arch), PT01 (Conductor-with-Subagents)

## Contesto
L'ecosistema S7 attuale consiste in script lineari ed è considerato non idoneo (Expectancy negativa in modalità retail come dimostrato da `report-studio.md`). La richiesta è di trasformarlo in una macchina da guerra gerarchica, in stile "Digital Empire".

## Decisione
Si abbandona la struttura "Script Monolitico" e si adotta la "Swarm Topology" (Principi Ruflo). L'ecosistema verrà governato da un agente Queen/Conductor chiamato **Chief Forge**. Saranno attivati reparti specifici:
- Forgiatura (Content-Forge Pipeline per elaborare nuovi edge di mercato e trascrizioni)
- Quant/Dati
- Execution & Risk

## Conseguenze
- Ogni reparto avrà una sua directory in `agents/`.
- Verranno creati i file canonici (7 file per agente).
- Il passaggio di informazioni (es. "Segnale BUY" generato dai Quant e approvato dal Risk) avverrà tramite aggiornamenti condivisi nel Memory Ecosystem.
