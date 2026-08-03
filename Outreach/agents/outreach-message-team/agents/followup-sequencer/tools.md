# Tools — followup-sequencer

## `check_lead_status`

- **Description**: legge stage, tentativo_numero, data ultimo invio e storico messaggi
  di un lead.
- **When to use**: ad ogni ciclo di controllo periodico (es. giornaliero).
- **Input schema**: `{"lead_id": "str"}`
- **Output schema**: `{"stage": "str", "tentativo_numero": "int", "ultimo_invio": "ISO-datetime", "storico_messaggi": [...]}`
- **Side effects**: nessuno.
- **Errors possible**: `lead_not_found`.
- **Example invocation**: `{"lead_id": "kaufmann-sas-brescia"}`
- **Example response**: `{"stage": "in_attesa", "tentativo_numero": 1, "ultimo_invio": "2026-07-28T10:01:00", "storico_messaggi": [...]}`

## `request_next_attempt`

- **Description**: genera l'handoff verso message-writer per il tentativo successivo.
- **When to use**: quando il tempo minimo dall'ultimo invio è passato e `tentativo_numero < 3`.
- **Input schema**: `{"lead_id": "str", "tentativo_numero": "int", "storico_precedente": ["str", "..."]}`
- **Output schema**: `{"ok": true, "handoff_id": "str"}`
- **Side effects**: nessuna modifica al lead-state finché message-writer non produce il nuovo draft (lo stage resta `in_attesa` fino a nuova validazione).
- **Errors possible**: `write_conflict`.
- **Example invocation**: vedi esempio in `system_prompt.md`.
- **Example response**: `{"ok": true, "handoff_id": "ho-2026-07-30-014"}`

## `mark_archived`

- **Description**: marca un lead come archiviato dopo il tentativo 3 senza risposta.
- **When to use**: solo dopo che sono passati i giorni minimi dal tentativo 3 e non è
  arrivata risposta.
- **Input schema**: `{"lead_id": "str"}`
- **Output schema**: `{"ok": true}`
- **Side effects**: `stage → archiviato`, il lead esce dal ciclo attivo.
- **Errors possible**: `write_conflict`.
- **Example invocation**: `{"lead_id": "kaufmann-sas-brescia"}`
- **Example response**: `{"ok": true}`

## `mark_responded`

- **Description**: marca un lead come risposto, interrompendo qualunque follow-up
  programmato.
- **When to use**: appena arriva segnale di risposta (webhook o controllo manuale).
- **Input schema**: `{"lead_id": "str"}`
- **Output schema**: `{"ok": true}`
- **Side effects**: `stage → risposto`, cancella eventuali handoff pendenti verso message-writer per questo lead.
- **Errors possible**: `write_conflict`.
- **Example invocation**: `{"lead_id": "kaufmann-sas-brescia"}`
- **Example response**: `{"ok": true}`
