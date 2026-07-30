# rule-keeper

Gatekeeper del team `outreach-message-team`. Valida ogni draft di messaggio contro i 5
Pilastri di `Outreach/knowledge/bibbia-messaggi-outreach.md` prima che possa essere
inviato. Approva/respinge in formato binario, sempre con motivazione ancorata a un atomo
preciso della Bibbia — mai un giudizio di stile.

**Installazione**: nessuna dipendenza esterna. Richiede solo accesso in lettura a
`bibbia-messaggi-outreach.md` e in lettura/scrittura a
`Outreach/knowledge/outreach-message-team-state/<lead_id>.json`.

**Uso base**: riceve un handoff da `message-writer` (draft + lead_id + tentativo_numero),
applica la checklist in `system_prompt.md`, risponde APPROVATO o RESPINTO secondo il
template. Vedi `playbook.md` per esempi completi, `eval_cases.json` per i test di
validazione.
