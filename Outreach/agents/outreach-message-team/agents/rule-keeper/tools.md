# Tools — rule-keeper

## `read_lead_state`

- **Description**: legge il file JSON dello stato del lead corrente per confrontare il
  nuovo draft con lo storico dei tentativi precedenti (necessario per il controllo
  "angolo diverso" sui follow-up).
- **When to use**: sempre, prima di validare un draft con `tentativo_numero > 1`.
- **Input schema**:
```json
{"lead_id": "str"}
```
- **Output schema**:
```json
{"lead_id": "str", "storico_messaggi": [{"tentativo": 1, "testo": "str", "gancio_usato": "str"}], "stage": "str"}
```
- **Side effects**: nessuno (sola lettura).
- **Errors possible**: `lead_not_found` (file assente — segnala ESCALATION, non procedere alla cieca).
- **Example invocation**:
```json
{"lead_id": "kaufmann-sas-brescia-333744000"}
```
- **Example response**:
```json
{"lead_id": "kaufmann-sas-brescia-333744000", "storico_messaggi": [{"tentativo": 1, "testo": "Ciao...", "gancio_usato": "gancio-4-import"}], "stage": "in_attesa"}
```

## `write_validation_result`

- **Description**: scrive l'esito della validazione (approvato/respinto + checklist) nel
  lead-state, secondo lo schema di `shared_state.md`.
- **When to use**: dopo ogni validazione, sempre — è l'unico modo per il resto del team
  di sapere l'esito.
- **Input schema**:
```json
{
  "lead_id": "str",
  "esito": "approvato | respinto",
  "checklist": {"pilastro_1_personalizzazione": true, "pilastro_2_chiarezza_3sec": true, "pilastro_3_valore_anticipato": false, "pilastro_4_microcommitment": true, "pilastro_5_basso_attrito": true},
  "note": "str"
}
```
- **Output schema**: `{"ok": true}` oppure `{"ok": false, "error": "str"}`.
- **Side effects**: modifica permanente il lead-state (append a `storico_messaggi`,
  aggiorna `stage`).
- **Errors possible**: `write_conflict` (file modificato da un altro processo nel
  frattempo — rilegge e riprova una volta, poi ESCALATION).
- **Example invocation**: vedi Input schema sopra.
- **Example response**: `{"ok": true}`.
