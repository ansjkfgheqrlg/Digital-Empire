# Handoff Rules — Outreach Message Team

Matrice completa: chi passa cosa a chi, quando, in che formato, con quale validazione.

| Da | A | Quando | Cosa (payload) | Formato | Validazione richiesta |
|---|---|---|---|---|---|
| (input esterno: scraper/Max) | case-study-forge | Nuovo lead disponibile | `dati_lead`, `nicchia`, `canale` | JSON, schema `shared_state.md` | `nicchia` non vuota |
| case-study-forge | message-writer | Value offer decisa | `value_offer` (tipo, descrizione, asset) | JSON, vedi `communication_protocol.md` §1 | `descrizione` non vuota e concreta (no frasi vaghe tipo "posso aiutarti") |
| message-writer | rule-keeper | Draft pronto (primo tentativo o correzione) | `draft_testo`, `gancio_usato`, `canale`, `tentativo_numero` | JSON, vedi `communication_protocol.md` §2 | `draft_testo` non vuoto, `canale` valido (linkedin\|whatsapp\|email) |
| rule-keeper | message-writer | Draft respinto | `pilastri_violati`, `motivazione` | JSON, vedi `communication_protocol.md` §3 | `motivazione` deve citare un `#atom-` di bibbia-messaggi-outreach.md |
| rule-keeper | followup-sequencer | Draft approvato e (presumibilmente) inviato | `testo_approvato`, `tentativo_numero` | JSON, vedi `communication_protocol.md` §4 | `tentativo_numero` coerente con lo storico |
| followup-sequencer | message-writer | Serve tentativo successivo (2 o 3) | `tentativo_numero`, `angolo_richiesto`, `storico_precedente` | JSON, vedi `communication_protocol.md` §5 | `storico_precedente` non vuoto se `tentativo_numero > 1` |
| followup-sequencer | (fine ciclo) | Risposta ricevuta O 3° tentativo esaurito | — | Aggiornamento `stage` nel lead-state | — |
| Qualunque agente | Max (fuori dal team) | ESCALATION di qualunque tipo | Messaggio testuale esplicito con prefisso `ESCALATION:` | Testo semplice | Nessuna — è sempre valido fermarsi e chiedere |

## Regola generale di validazione degli handoff

Ogni handoff che non rispetta il proprio schema minimo (campi obbligatori mancanti) **non
viene processato silenziosamente** — l'agente ricevente risponde con
`ESCALATION: handoff malformato — campo mancante <nome campo>` invece di procedere con
dati parziali/indovinati.
