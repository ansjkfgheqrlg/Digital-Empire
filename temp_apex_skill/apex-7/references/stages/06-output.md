# Stage 6: Final Output

## Obiettivo
Assemblare l'output finale, aggiornare la memoria e presentare il risultato all'utente.

## Agente Responsabile
**ORCHESTRATOR** (AG-01)

## Input
- Output approvato (passato CRITIC e GATE)
- Tutti i report di sessione
- Stato completo del sistema

## Processo

1. Assemblare output finale da:
   - Draft approvato (da WRITER/REFINER)
   - Context Package (da ANALYST)
   - PLAN (da PLANNER)
   - Critique Report (da CRITIC)
   - Gate Report (da GATE AGENT)

2. Aggiornare tutti i layer di memoria:
   - Working Memory: stato finale
   - Decision Log: decisioni della sessione
   - Strategy Store: eventuali nuove strategie
   - Architecture Snapshots: se evoluzione applicata
   - Compressed Knowledge: lessons learned

3. Creare Architecture Snapshot se:
   - Evoluzione applicata in questa sessione
   - Nuova strategia promossa a best_practice
   - Gate threshold modificato

4. Preparare riepilogo sessione

5. Presentare all'utente

## Output

### Riepilogo Sessione
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[APEX-7] Sessione Completata
Session ID: {sess-uuid}
Durata: {N} minuti
Cicli totali: {N}
Agenti attivati: {lista}
Quality score finale: {X}/10
Gate superato: L{N}→L{N+1}
Decisioni salvate: {N}
Strategie aggiornate: {N}
Evoluzioni applicate: {N}
Memory updates: {N} record
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT FINALE:
{output completo}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Post-Actions
1. Emetti `system.output.final`
2. Aggiorna `evolution_tracker.py` con metriche sessione
3. Se auto-evolve attivo: programma prossima evoluzione
4. Archivia sessione completa

## Criteri di Completamento
- [x] Output finale assemblato
- [x] Tutti i layer memoria aggiornati
- [x] Riepilogo sessione presentato
- [x] Evento `system.output.final` emesso
- [x] Metriche registrate per evolution tracking
