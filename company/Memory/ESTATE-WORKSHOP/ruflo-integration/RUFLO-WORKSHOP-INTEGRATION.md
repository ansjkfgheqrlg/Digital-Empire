# RUFLO — Workshop Integration Plan (Aggiornato)

**Data:** 2026-07-20  
**Owner:** Chief Forge Department

---

## Topologia Ruflo per il Workshop

| Topologia     | Uso Principale                  | Stream | Queen                     |
|---------------|----------------------------------|--------|---------------------------|
| Hierarchical  | Coordinamento generale           | Tutti  | Chief Forge (conductor)   |
| Pipeline      | 9 Stage Empire Studio            | S5     | department-lead           |
| Mesh          | Verification ↔ Memory            | Tutti  | verification + memory     |
| Swarm         | Forgiatura parallela agenti      | L6     | content-forge-invoker     |

---

## Integrazione Memory

- Ogni agente deve chiamare `ruflo memory_store`
- Memory Ecosystem come layer persistente
- Checkpoint automatico tramite ruflo

---

## Agenti Ruflo da attivare

- `ruflo-bridge`
- `swarm-coordinator`
- `memory-distributor`

---

## Prossimi passi

1. Inizializzare ruflo swarm
2. Collegare ogni workflow a ruflo
3. Testare su yt-fliki-renderer

**Creato da Chief Forge Department**