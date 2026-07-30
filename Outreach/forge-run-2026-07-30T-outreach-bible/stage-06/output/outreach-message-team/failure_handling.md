# Failure Handling — Outreach Message Team (livello team)

Per i failure mode specifici di ogni agente, vedi `agents/<ruolo>/failure_modes.md`.
Questo file copre i failure **tra** agenti (handoff, coordinamento, stato condiviso).

| # | Failure | Punto di rottura | Rilevamento | Recupero |
|---|---|---|---|---|
| 1 | case-study-forge non risponde/si blocca su una nicchia nuova | Handoff case-study-forge → message-writer | ESCALATION esplicita da case-study-forge | Il lead resta in `stage: nuovo`, Max decide il pattern per la nicchia, poi il ciclo riparte da case-study-forge |
| 2 | message-writer scrive un draft che rule-keeper respinge 3 volte di seguito sullo stesso lead | Loop message-writer ↔ rule-keeper | Contatore respingimenti per lead (soglia 3) | Il lead viene marcato `bloccato_qualita`, segnalato a Max per revisione manuale invece di continuare il loop all'infinito (evita spreco di cicli) |
| 3 | rule-keeper approva per errore un messaggio che viola un pilastro | Uscita dal gate senza controllo reale | Audit periodico a campione dello storico messaggi | Se scoperto prima dell'invio effettivo, blocco manuale; se scoperto dopo, log come incidente e review del `system_prompt.md` di rule-keeper |
| 4 | followup-sequencer perde traccia di un lead (nessun controllo periodico eseguito) | Lead bloccato indefinitamente in `in_attesa` | Controllo periodico esterno: lead con `in_attesa` da più di 10 giorni senza transizione è un'anomalia | Verifica manuale, riattivazione forzata del controllo per quel lead |
| 5 | Due agenti scrivono sullo stesso lead-state in concorrenza (race condition) | Scrittura file JSON | Errore di scrittura (`write_conflict`) o dati incoerenti rilevati a lettura | Read-modify-write con rilettura: chi scrive rilegge sempre prima di modificare (vedi `shared_state.md` §Regola di concorrenza); nella pratica il flusso è sequenziale quindi il rischio è basso |
| 6 | Il lead-state file non esiste per un lead_id referenziato in un handoff | Qualunque agente che tenta di leggere | Errore esplicito `lead_not_found` | ESCALATION immediata, nessun agente inventa uno stato di default per procedere |
| 7 | Max chiede una modifica alle regole della Bibbia a metà di un ciclo attivo | Cambio delle regole "sotto i piedi" del team | Nessuno — è un evento esterno intenzionale | Il team aggiorna `bibbia-messaggi-outreach.md`, rule-keeper applica le nuove regole dal prossimo draft in poi; i messaggi già approvati/inviati non vengono retroattivamente invalidati |

## Principio generale

In caso di dubbio non coperto da questa tabella: **fermarsi e segnalare (ESCALATION) è
sempre preferibile a procedere con un'assunzione silenziosa.** Questo vale per ogni
agente del team, coerente con il mandato di rule-keeper (mai approvare "quasi ok").
