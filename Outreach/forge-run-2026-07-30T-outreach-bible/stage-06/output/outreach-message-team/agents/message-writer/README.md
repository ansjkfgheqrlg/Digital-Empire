# message-writer

Copywriter del team `outreach-message-team`. Scrive draft di messaggi cold outreach
(LinkedIn/WhatsApp/Email) applicando i 5 Pilastri della Bibbia. Riceve la value offer da
`case-study-forge`, passa il draft a `rule-keeper` per validazione, corregge sui rigetti.

**Installazione**: nessuna dipendenza esterna oltre l'accesso al lead-state JSON e a
`bibbia-messaggi-outreach.md`.

**Uso base**: riceve handoff con `lead_id`, `nicchia`, `canale`, `tentativo_numero`;
recupera la value offer; scrive secondo la struttura in `system_prompt.md`; passa a
rule-keeper. Vedi `playbook.md` per esempi end-to-end.
