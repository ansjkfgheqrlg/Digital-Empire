# Protocollo di comunicazione — Outreach Message Team

**File-based**, coerente con lo `shared_state.md`: ogni agente legge il lead-state JSON,
esegue il proprio compito, scrive il proprio output nello stesso file (read-modify-write),
e produce un **handoff envelope** in-memory/nel log per il prossimo agente della catena.

## Handoff envelope canonico

```json
{
  "from_agent": "case-study-forge | message-writer | rule-keeper | followup-sequencer",
  "to_agent": "message-writer | rule-keeper | followup-sequencer | (fine ciclo)",
  "lead_id": "str",
  "timestamp": "ISO-datetime",
  "payload": { "...": "specifico per tipo di handoff, vedi sotto" },
  "context_refs": ["Outreach/knowledge/outreach-message-team-state/<lead_id>.json"],
  "expectation": "str — cosa deve fare il destinatario",
  "trace_id": "str (lead_id + tentativo_numero, per tracciabilità)"
}
```

## Handoff specifici

### 1. case-study-forge → message-writer
```json
{"payload": {"value_offer": "descrizione + asset_prodotto"}, "expectation": "Scrivi il draft usando questa value offer nel Pilastro 3"}
```

### 2. message-writer → rule-keeper
```json
{"payload": {"draft_testo": "str", "gancio_usato": "str", "canale": "linkedin|whatsapp|email"}, "expectation": "Valida contro i 5 pilastri, approva o respingi con motivazione puntuale"}
```

### 3. rule-keeper → message-writer (RIGETTO)
```json
{"payload": {"pilastri_violati": ["pilastro_3_valore_anticipato"], "motivazione": "str puntuale, con citazione della regola violata da master.md"}, "expectation": "Riscrivi SOLO le parti che violano i pilastri indicati, non l'intero messaggio se non necessario"}
```

### 4. rule-keeper → followup-sequencer (APPROVAZIONE + invio avvenuto)
```json
{"payload": {"testo_approvato": "str", "tentativo_numero": "int"}, "expectation": "Monitora risposta, decidi quando/se attivare il tentativo successivo"}
```

### 5. followup-sequencer → message-writer (richiesta nuovo tentativo)
```json
{"payload": {"tentativo_numero": "int (2 o 3)", "angolo_richiesto": "diverso_valore | breakup_scarsita", "storico_precedente": ["testi dei tentativi precedenti, per NON ripeterli"]}, "expectation": "Scrivi un nuovo draft con angolo diverso, stesso lead"}
```

## Formato universale del rifiuto (usato SOLO da rule-keeper)

Il rifiuto deve sempre citare l'atomo esatto violato da `master.md` (non un giudizio
generico tipo "non mi convince"). Esempio reale:

> RESPINTO — Pilastro 4 (Micro-commitment) violato: il draft chiede "possiamo fare una
> call di 30 minuti?" al primo messaggio. Vedi master.md#atom-pillar-4-microcommitment:
> il primo messaggio deve chiedere un impegno minimo (es. "mandami un link"), mai una
> call diretta.

Questo formato è vincolante per tutti gli agenti del team (vedi `agents/rule-keeper/system_prompt.md`).
