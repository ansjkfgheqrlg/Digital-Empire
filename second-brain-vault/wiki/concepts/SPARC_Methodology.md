---
Type: CONCEPT
Status: Active
Tags: #metodologia #sviluppo #ai #planning #sparc
Created: 2026-05-29
Last updated: 2026-05-29
---

# SPARC Methodology — Framework di Sviluppo Strutturato

## Overview
SPARC è un workflow di sviluppo in 5 fasi che forza la pianificazione prima del codice.
Estratto da Claude-Flow V3. Adottato come standard per tutti i capitoli di Exponium.
**Principio:** non scrivere mai una riga di codice senza spec e architettura definite.

## Le 5 Fasi

```
S — Specification   → cosa costruiamo, perché, done-when
P — Pseudocode      → logica in linguaggio naturale, edge cases
A — Architecture    → struttura file, schemi DB, firme funzioni
R — Refinement      → implementazione iterativa con quality gate
C — Completion      → verifica criteri di accettazione, test, commit
```

### Fase 1 — Specification
**Prima di tutto:** scrivi il contratto.
- Cosa fa il sistema (comportamento utente-facing)
- Perché serve (problema che risolve)
- Done-when (criteri misurabili)
- Out of scope (cosa NON facciamo in questa sessione)

### Fase 2 — Pseudocode
**Prima del codice reale:** scrivi la logica in prosa.
- Flusso dati: cosa entra, cosa esce
- Funzioni chiave e responsabilità
- Edge cases da gestire
- Sequenza operazioni

### Fase 3 — Architecture
**Prima dell'implementazione:** definisci la struttura.
- Albero file/moduli
- Schemi database (SQL scritto per intero)
- Firme funzioni (tipizzate)
- Punti di integrazione con codice esistente
- Decisioni architetturali documentate (con WHY)

### Fase 4 — Refinement
**Implementazione iterativa:**
- 50 righe → test → 50 righe → test (non 500 righe poi test)
- Error handling alle frontiere (input utente, API esterne)
- No hardcoded credentials, no debug print statements
- Ogni funzione testata in isolamento prima di integrare

### Fase 5 — Completion
**Verifica finale:**
- Tutti i criteri di accettazione soddisfatti?
- Test passano (pytest/jest)?
- Code review passata (95% quality gate)?
- Commit messaggio chiaro e descrittivo?

## Template Rapido (incollare all'inizio di ogni capitolo)

```markdown
## SPARC — [Nome Capitolo]

### SPEC
- Cosa: 
- Perché: 
- Done when: [ ] [ ] [ ]
- Out of scope: 

### ARCHITETTURA
- Files: 
- Schema: 
- Funzioni chiave: 

### FASI
[ ] Ph.1 Spec completa
[ ] Ph.2 Pseudocode scritto
[ ] Ph.3 Architettura definita
[ ] Ph.4 Implementazione (iterativa)
[ ] Ph.5 Completamento verificato
```

## Applicazione a Exponium

| Capitolo | SPARC focus |
|---------|-------------|
| Cap.1 (Setup) | Architecture only — definire la struttura cartelle e schema DB |
| Cap.2A-2D (Scrapers) | Full SPARC — scraper complesso, molti edge cases |
| Cap.3 (Bibbia) | Spec pesante — la logica della sequenza email è il prodotto |
| Cap.4 (Humanizer) | Architecture + Refinement — variabili e delay da ottimizzare |
| Cap.6 (Dashboard) | Full SPARC — UI + API + DB tutti connessi |
| Cap.9 (Second Brain) | Full SPARC — sistema di memoria è il nucleo del prodotto |

## Perché funziona
- Elimina il "scrivo codice poi vedo dove vado" → il 60% delle sessioni perse
- Spec scritta = scope creep impossibile
- Architecture prima del codice = nessun refactor dopo 200 righe
- Iterazione piccola = bug trovati subito, non dopo 2 ore

## Connessioni
- [[Tool_ClaudeFlow_Orchestration]] — fonte di questa metodologia
- [[AgentDB_Memory_System]] — Phase 2 SPARC: cercare pattern simili in memoria
- [[Exponium_Outreach_Platform]] — ogni capitolo usa SPARC
- [[Swarm_Orchestration_Pattern]] — SPARC + swarm = Phase 3 con agenti multipli
