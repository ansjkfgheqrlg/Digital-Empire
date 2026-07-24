# ORCHESTRATOR — Playbook

## Scenario 1: Primo Input Utente

1. Ricevi input → leggi per intero
2. Memory.RECALL per contesto passato
3. Mostra banner APEX-7 avviato
4. Emetti `task.created`
5. Attiva PLANNER con contesto completo
6. Ricevi PLAN → valida (ha senso? completo?)
7. Mostra PLAN all'utente
8. Procedi a Stage 2

## Scenario 2: Critique Loop

1. Ricevi verdict da CRITIC
2. SE PASS → procedi a Stage 4 (Gate)
3. SE REFINE → attiva REFINER, attendi, torna a CRITIC
4. SE RESTART → salva contesto fallimento, torna a Stage 1
5. Tieni contatore iterazioni (max 3)
6. SE iterazione 3 con REFINE → ESCALATE a META

## Scenario 3: Gate Result

1. Ricevi Gate Report
2. SE PASSED → procedi (Stage 5 o Stage 6)
3. SE FAILED (1a/2a) → remediation a REFINER
4. SE FAILED (3a) → ESCALATE a META
5. SE safety gate fail → STOP, escalation HUMAN

## Scenario 4: Human Override

1. Ricevi "stop"/"pausa"/"cambia"
2. Salva Working Memory corrente
3. Metti in pausa tutti gli agenti
4. Comunica stato all'utente
5. Aspetta istruzioni
6. Riprendi da checkpoint o modifica rotta

## Scenario 5: Meta Activation

1. Ogni 3 cicli → attiva META AGENT
2. Mostra System Analysis Report
3. Applica micro-interventions automatici
4. Proponi macro-interventions all'utente
5. Aggiorna memoria con evoluzioni

## Scenario 6: Final Output

1. Assembla output finale
2. Aggiorna tutti i layer memoria
3. Crea Architecture Snapshot se evoluto
4. Mostra riepilogo sessione
5. Emetti `system.output.final`
