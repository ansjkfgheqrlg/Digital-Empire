# Tools — case-study-forge

## `lookup_real_case_studies`

- **Description**: cerca tra i case study reali noti dell'azienda/freelancer uno
  pertinente alla nicchia del lead.
- **When to use**: sempre, primo step per ogni nuovo lead.
- **Input schema**: `{"nicchia": "str"}`
- **Output schema**: `{"found": bool, "case_study": {"descrizione": "str", "risultato_misurabile": "str"} | null}`
- **Side effects**: nessuno (sola lettura, es. da un file `case-studies-reali.json`
  mantenuto manualmente da Max/team commerciale).
- **Errors possible**: `store_not_found` (il file/store non esiste ancora — trattare come
  `found: false`, non bloccare).
- **Example invocation**: `{"nicchia": "concessionario-auto-import"}`
- **Example response**: `{"found": false, "case_study": null}`

## `write_value_offer`

- **Description**: scrive la value offer nel lead-state, secondo lo schema descritto in
  `system_prompt.md`.
- **When to use**: dopo aver deciso l'offerta (reale o artificiale).
- **Input schema**: `{"lead_id": "str", "value_offer": {"tipo": "str", "descrizione": "str", "asset_prodotto": "str|null"}}`
- **Output schema**: `{"ok": true}`
- **Side effects**: aggiorna `stage` del lead a `value_offer_pronta`.
- **Errors possible**: `write_conflict`.
- **Example invocation**: `{"lead_id": "kaufmann-sas-brescia", "value_offer": {"tipo": "artificial_case_study", "descrizione": "PDF preventivo di esempio su annuncio reale", "asset_prodotto": null}}`
- **Example response**: `{"ok": true}`
