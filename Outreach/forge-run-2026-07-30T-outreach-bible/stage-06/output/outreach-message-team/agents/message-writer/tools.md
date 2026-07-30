# Tools — message-writer

## `read_value_offer`

- **Description**: legge la value offer prodotta da `case-study-forge` per il lead
  corrente — obbligatorio prima di scrivere il Pilastro 3.
- **When to use**: sempre, prima di scrivere un draft (tranne se già presente
  nell'handoff ricevuto).
- **Input schema**: `{"lead_id": "str"}`
- **Output schema**: `{"value_offer": {"tipo": "str", "descrizione": "str", "asset_prodotto": "str|null"}}`
- **Side effects**: nessuno.
- **Errors possible**: `value_offer_missing` — se case-study-forge non ha ancora
  prodotto nulla per questo lead, NON procedere a scrivere (violerebbe il Pilastro 3),
  segnala `ESCALATION: value offer mancante`.
- **Example invocation**: `{"lead_id": "kaufmann-sas-brescia"}`
- **Example response**: `{"value_offer": {"tipo": "artificial_case_study", "descrizione": "PDF preventivo di esempio", "asset_prodotto": null}}`

## `write_draft`

- **Description**: scrive il draft nel lead-state e lo passa in handoff a `rule-keeper`.
- **When to use**: al termine di ogni bozza (o correzione post-rigetto).
- **Input schema**: `{"lead_id": "str", "testo": "str", "canale": "linkedin|whatsapp|email", "gancio_usato": "str", "tentativo_numero": "int"}`
- **Output schema**: `{"ok": true, "handoff_id": "str"}`
- **Side effects**: append a `storico_messaggi` nel lead-state, cambia `stage` a `draft_scritto`.
- **Errors possible**: `write_conflict` (rilegge e riprova).
- **Example invocation**: `{"lead_id": "kaufmann-sas-brescia", "testo": "Ciao, sono Max...", "canale": "whatsapp", "gancio_usato": "gancio-4-import", "tentativo_numero": 1}`
- **Example response**: `{"ok": true, "handoff_id": "ho-2026-07-30-001"}`
