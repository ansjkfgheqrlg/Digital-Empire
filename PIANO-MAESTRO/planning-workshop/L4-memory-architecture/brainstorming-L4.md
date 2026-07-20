# L4 — BRAINSTORMING: Memory Architecture

**Livello:** 4  
**Data:** 2026-07-20  
**Focus:** Progettazione dell'Ecosistema di Memoria per il Workshop

---

## Requisiti Chiave (dal brief utente)

- Salvare **tutte le decisioni**
- Salvare **piani di architettura**
- Salvare **planning**
- Salvare **restorming**
- Salvare **checkpoint**
- Gestione **ultra chirurgica** e operativa
- Gestito dai **Reparti Forge**

---

## Brainstorming — Componenti del Memory System

### 1. Categorie di Memoria

| Categoria | Contenuto | Esempi | Responsabile |
|-----------|-----------|--------|--------------|
| **decisions** | Tutte le decisioni chiave | Prezzo Manuale, Nicchia YT, Nome Preventivo | Chief Forge |
| **architecture** | Architetture e workflow | S5 Empire Studio, WF-YT-*, Ruflo Topology | Strategy Department |
| **planning** | Task board, Gantt, roadmap | Taskboard Workshop, Gantt L1-L8 | Chief Forge |
| **restorming** | Sessioni di revisione e miglioramento | RST-001, RST-002 | Strategy + Memory |
| **checkpoints** | Checkpoint giornalieri e di fine livello | CP-20260720-L1, CP-20260720-L2 | Memory Management |
| **performance** | Metriche reali | Revenue, video generati, funnel live | Verification |

### 2. Protocollo di Salvataggio (P10 + P12)

- Ogni decisione → file dedicato in `decisions/`
- Ogni architettura → `architecture/`
- Ogni planning → `planning/`
- Ogni restorming → `restorming/`
- Ogni fine livello/stream → `checkpoints/`
- Metriche → `performance/`

**Tracciabilità:** Ogni file deve contenere `trace` e `source`.

### 3. Integrazione con Ruflo

- Ruflo `memory_store` per memoria distribuita
- Ogni agente deve chiamare `memory_manager.py` dopo azioni critiche
- Memory come "sistema nervoso" secondario

### 4. Struttura Cartelle

```
company/Memory/ESTATE-WORKSHOP-PLANNING/
company/Memory/ESTATE-WORKSHOP/          ← Memory operativo Workshop
```

---

## Output Livello 4

**Memory System Design** definito con 6 categorie principali.

**Prossimo:** L5 — Ruflo Orchestration

**Checkpoint L4 salvato.**