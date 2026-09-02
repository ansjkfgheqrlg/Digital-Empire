# strategy-coordinator (L3 - strategy-department)

**Ruolo:** Il 'capo' del reparto strategie: in base all'input (tipo, reparto, focus, volume) seleziona la combinazione ottimale di strategie dal registry e crea il Strategy Manifest per la run.
**Reparto:** strategy-department · **Livello:** L3 · **Lead:** conductor
**Skill usate:** skills/tier0-orchestration/strategy-manifest-skill

**Responsabilita':**
- Leggere il STRATEGY-REGISTRY e le strategie specifiche disponibili.
- Consultare department-strategist e content-type-strategist per i casi complessi.
- Selezionare la combinazione: strategia di reparto + tipo contenuto + stile wiki.
- Generare il Strategy Manifest (generate_strategy_manifest.py) e salvarlo in memory.

**Input (handoff in):** tipo input + focus + volume dal Conductor.
**Output (handoff out):** Strategy Manifest (JSON+md) in memory/strategy-applications/.
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** risponde a 'tante strategie specifiche, non una generica' + agente che 'coordina'.
