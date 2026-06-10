# ADR-002 — Pattern memory-first: interroga prima, checkpoint dopo, sempre

- **Data:** 2026-06-10
- **Stato:** ATTIVO
- **Decisori:** Max (richiesta esplicita, urgenza massima)

## Contesto
Senza memoria operativa centralizzata ogni sessione riparte da zero, le decisioni si
perdono o si contraddicono, i task chiusi non lasciano traccia verificabile.

## Decisione
1. Esiste l'**ecosistema 10 MEMORY** (`company/Memory/`): checkpoint, decisioni (ADR),
   piani, sessioni, stato, audit. Dossier: `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md`.
2. **PRIMA di qualsiasi task**: interrogare MEMORY (INDEX + STATO-EMPIRE + CP/ADR rilevanti).
3. **DOPO ogni task**: scrivere checkpoint CP. Nessun task è chiuso senza CP-id.
4. Ogni decisione architetturale/strategica → ADR con contradiction-check.
5. È il pattern #13 del Piano Maestro, non negoziabile, cablato via hook + CLAUDE.md +
   acceptance criteria di ogni team + Memory-Sentinel + verify-empire.sh.

## Alternative scartate
- Affidarsi solo alla wiki — è la vista umana, non registro operativo strutturato.
- Affidarsi solo ad AgentDB — opaco per l'uomo, non navigabile nell'Explorer.
- Memoria personale di Claude — è di Claude, non dell'azienda.

## Conseguenze
- Overhead minimo per task (template CP 30 secondi) in cambio di ripresa a freddo garantita.
- MEMORY si costruisce PER PRIMO (F1 task 1.0, fasi ME-0→ME-5).

## Contradiction-check
Nessun conflitto con ADR-001 (lo estende). Confini netti con INTELLIGENCE (conoscenza
esterna) e Backbone BRAIN (infrastruttura): definiti in 09-ECOSISTEMA-MEMORY.md §1.
