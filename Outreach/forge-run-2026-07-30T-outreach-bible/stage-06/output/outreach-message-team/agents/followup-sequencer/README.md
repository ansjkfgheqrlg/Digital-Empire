# followup-sequencer

Gestisce la cadenza dei 3 tentativi di follow-up (20%/40%/30% tassi attesi) per ogni lead
del team `outreach-message-team`. Decide QUANDO attivare il prossimo tentativo o
archiviare, mai il contenuto (delegato a message-writer). Interrompe la sequenza
immediatamente in caso di risposta.

**Installazione**: nessuna dipendenza esterna oltre l'accesso al lead-state JSON e un
meccanismo (anche manuale) per segnalare le risposte ricevute.

**Uso base**: esegue un controllo periodico (es. giornaliero) su tutti i lead in stage
`in_attesa`, applica la cadenza fissa descritta in `system_prompt.md`. Vedi
`playbook.md` per i casi principali.
