# L5 — OUTPUT: Ruflo Orchestration

**Livello:** 5  
**Stato:** COMPLETATO  
**Data:** 2026-07-20

---

## Ruflo Topology per il Workshop

| Topologia | Descrizione | Utilizzo Principale | Stream |
|-----------|-------------|---------------------|--------|
| **Hierarchical** | Queen = Chief Forge / conductor | Coordinamento generale del Workshop | Tutti |
| **Pipeline** | Flusso sequenziale | 9 Stage Empire Studio | S5 |
| **Mesh** | Comunicazione bidirezionale | Verification ↔ Memory | Tutti |
| **Swarm** | Forgiatura parallela | Creazione agenti con content-forge2.0 | L6 |

### Integrazione Memory

- Ruflo `memory_store` obbligatorio
- Ogni agente chiama `memory_manager.py`
- Memory come layer persistente secondario

### Agenti Ruflo-specifici

- `ruflo-bridge`
- `swarm-coordinator`
- `memory-distributor`

---

**Checkpoint L5:** CP-20260720-L5  
**Prossimo:** L6 — Content-Forge Integration