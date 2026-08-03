# Failure Modes — message-writer

| ID | Failure | Sintomo | Prevenzione | Rilevamento | Recupero |
|----|---------|---------|-------------|-------------|----------|
| fm-001 | Scrive senza value offer (Pilastro 3 vuoto) | Draft con offerta vaga tipo "posso aiutarti" | Tool `read_value_offer` obbligatorio prima di scrivere | rule-keeper respinge per Pilastro 3 | ESCALATION invece di inventare un'offerta |
| fm-002 | Menziona il prezzo nel tentativo 1/2 | Draft con "i miei prezzi partono da..." | Vincolo esplicito nel system_prompt | rule-keeper respinge per Pilastro 3 | Rimuove ogni riferimento a prezzo, riscrive chiusura |
| fm-003 | Doppia CTA ambigua | "fammi sapere / oppure chiamami" | Regola "una sola richiesta" nel system_prompt | rule-keeper respinge per Pilastro 4 | Sceglie la richiesta a minor attrito, elimina l'altra |
| fm-004 | Ripete l'angolo psicologico tra tentativi | Tentativo 2 quasi identico al 1 (sinonimi) | Riceve sempre lo storico da followup-sequencer prima di scrivere il follow-up | rule-keeper confronta con storico e respinge | Cambia esplicitamente leva psicologica (Barnum→Rainbow o viceversa) |
| fm-005 | Draft troppo lungo per il canale | WhatsApp da 150 parole | Soglie di lunghezza esplicite per canale nel system_prompt | rule-keeper respinge per Pilastro 5 | Comprime mantenendo tutti gli elementi essenziali |
| fm-006 | Tono da "venditore" (superlativi, hype) | "Offerta fantastica e unica nel suo genere!" | Vincolo di tono esplicito | Review qualitativa periodica (non sempre automatica) | Riscrive con tono colloquiale-paritario |
| fm-007 | Inventa un case study/risultato non fornito | "Ho aiutato 50 aziende a raddoppiare le vendite" senza dato reale da case-study-forge | Vincolo esplicito "mai inventare numeri/risultati" | Confronto con l'output di case-study-forge | Rimuove il claim inventato, usa solo ciò che case-study-forge ha fornito |
