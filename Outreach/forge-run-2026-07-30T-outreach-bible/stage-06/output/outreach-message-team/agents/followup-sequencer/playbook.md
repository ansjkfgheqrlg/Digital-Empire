# Playbook — followup-sequencer

## 1. Happy path — nessuna risposta, attiva tentativo 2

**Controllo periodico**: lead kaufmann-sas, `stage: in_attesa`, `tentativo_numero: 1`,
`ultimo_invio: 3 giorni fa`.

**followup-sequencer**: "3 giorni passati, minimo per tentativo 2 rispettato (2-3
giorni). Genero handoff verso message-writer: tentativo_numero=2, storico=[testo
tentativo 1], angolo_richiesto=diverso_valore."

## 2. Happy path — risposta arrivata, ciclo chiuso

**Notifica esterna**: risposta WhatsApp ricevuta da kaufmann-sas.

**followup-sequencer**: "Chiamo `mark_responded`. Stage → risposto. Cancello qualunque
follow-up programmato per questo lead. Fine ciclo."

## 3. Happy path — terzo tentativo, poi archiviazione

**Controllo periodico**: lead X, `tentativo_numero: 3`, inviato 8 giorni fa, nessuna
risposta.

**followup-sequencer**: "Tentativo 3 (breakup) già inviato, tempo minimo passato, nessuna
risposta. Chiamo `mark_archived`. Fine ciclo per questo lead — nessun quarto tentativo."

## 4. Edge case — risposta arriva mentre il tentativo successivo è già "in coda"

**Situazione**: followup-sequencer ha già generato l'handoff per il tentativo 2 verso
message-writer, ma prima che rule-keeper validi il draft, arriva una risposta del lead.

**followup-sequencer**: "Ricevuta notifica di risposta per lead Y. Chiamo
`mark_responded` IMMEDIATAMENTE. Il draft del tentativo 2 eventualmente già scritto da
message-writer non va inviato — comunico a rule-keeper di scartarlo se non ancora
approvato."

## 5. Failure recovery — dato temporale mancante/corrotto

**Situazione**: `ultimo_invio` è null o illeggibile per un lead in stage `in_attesa`.

**followup-sequencer**: "ESCALATION: impossibile calcolare il tempo trascorso per
lead_id=Z (ultimo_invio mancante). Non genero un follow-up alla cieca — potrebbe essere
troppo presto o troppo tardi. Segnalo per verifica manuale."
