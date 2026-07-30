# Failure Modes — followup-sequencer

| ID | Failure | Sintomo | Prevenzione | Rilevamento | Recupero |
|----|---------|---------|-------------|-------------|----------|
| fm-001 | Invia follow-up troppo presto (stesso giorno) | Lead riceve 2 messaggi ravvicinati, percepiti come spam | Tempo minimo esplicito (2-3gg / 5-7gg) nel system_prompt | Controllo `ultimo_invio` prima di ogni handoff | Non genera l'handoff finché il minimo non è passato |
| fm-002 | Genera un 4° tentativo | Lead ricontattato oltre la sequenza dichiarata | Vincolo esplicito "mai oltre tentativo 3" | Check `tentativo_numero == 3` blocca ulteriori richieste | Marca archiviato invece di richiedere un altro draft |
| fm-003 | Continua la sequenza dopo una risposta | Lead che ha già risposto riceve comunque un follow-up | `mark_responded` interrompe immediatamente qualunque handoff pendente | Controllo `stage == risposto` prima di ogni azione | Cancella handoff pendenti, non genera nulla di nuovo |
| fm-004 | Richiede lo stesso angolo per tentativo 2/3 | message-writer riceve la richiesta senza specificare "angolo diverso" | Campo `angolo_richiesto` obbligatorio in ogni handoff | rule-keeper comunque farebbe da secondo controllo, ma non deve arrivare a quel punto | Include sempre lo storico completo nell'handoff |
| fm-005 | Timestamp mancante/corrotto blocca la decisione | Non sa se è già passato il tempo minimo | Nessuna assunzione di default silenziosa | Errore esplicito alla lettura | ESCALATION, non decide alla cieca |
| fm-006 | Accelera la cadenza per "smaltire" molti lead in coda | Tempi minimi ridotti sotto pressione di volume | Nessuna eccezione di velocità dichiarata nel system_prompt | Audit: tempo medio tra tentativi non deve scendere sotto i minimi dichiarati | Richiamo alla regola, nessuna eccezione concessa |
