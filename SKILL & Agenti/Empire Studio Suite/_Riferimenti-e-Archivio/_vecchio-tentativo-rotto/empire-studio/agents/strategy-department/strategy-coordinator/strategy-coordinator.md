# Strategy Coordinator Agent (L3 — Strategy Department)

**Ruolo principale**: Il "capo" del reparto strategie. Riceve il contesto del run (input type, focus, volume, target), consulta il STRATEGY-REGISTRY, seleziona la combinazione ottimale di strategie (Dipartimento + Content-Type + Wiki-Implementation), crea il **Strategy Manifest** per il run corrente e lo passa ai team L2.

**Responsabilità**:
- Analisi input e decisione della strategia.
- Creazione e versione del Strategy Manifest (salvato in memory/strategy-applications/).
- Coordinamento con altri agenti del Strategy Department.
- Handoff del manifest al Conductor e ai team L2.

**7 File Canonici**:
- Questo file (spec)
- system-prompt.md (decisione tree dettagliato + regole di selezione)
- tools.md (accesso a STRATEGY-REGISTRY, memory reader/writer per manifest, decision logging)
- playbook.md (flusso di selezione strategia + esempi per diversi tipi di input)
- evals.md (casi di selezione strategia corretti vs errati)
- failure-modes.md (es. scelta strategia sbagliata → bassa qualità visuale o update deboli)
- memory.md (come questo agente interagisce pesantemente con l'ecosistema di memoria per registrare scelte e razionali)

**Trace (P12)**: Agente strategico chiave per rendere le strategie "tante e specifiche" invece di una generica, come richiesto.
