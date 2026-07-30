# Outreach Message Team

Team di 4 agenti per scrivere e validare messaggi di cold outreach (LinkedIn DM,
WhatsApp, email) applicando **sempre** il framework in
`Outreach/knowledge/bibbia-messaggi-outreach.md` — Effetto Barnum, Inganno Arcobaleno, i
5 Pilastri, la sequenza di follow-up a 3 step. Nessun messaggio esce senza passare dal
gatekeeper (`rule-keeper`).

## Come istanziare

Nessuna installazione software: sono system prompt per agenti Claude, da invocare tramite
il tool Agent/Task (o come sub-processi di un orchestratore che gira la pipeline).

1. **Prerequisito**: `Outreach/knowledge/bibbia-messaggi-outreach.md` deve esistere (è
   il MKD di questo forge-run, vedi `stage-04/master.md`).
2. **Stato condiviso**: crea la cartella `Outreach/knowledge/outreach-message-team-state/`
   (un JSON per lead, schema in `shared_state.md`).
3. **Ordine di invocazione per un nuovo lead**: `case-study-forge` → `message-writer` →
   `rule-keeper` (loop se respinto) → `followup-sequencer` (per il ciclo di vita
   successivo).

## Come lanciarlo (esempio di orchestrazione manuale)

```
1. Nuovo lead arriva (es. da preventa-maps-scraper, o inserito a mano)
2. Invoca case-study-forge con {lead_id, nicchia, dati_lead}
3. Invoca message-writer (legge automaticamente la value_offer appena scritta)
4. Invoca rule-keeper sul draft prodotto
   - Se RESPINTO: torna al punto 3 con la motivazione
   - Se APPROVATO: procedi
5. Invia il messaggio nel canale reale (WhatsApp/LinkedIn/Email — fuori dal team,
   delegato agli strumenti di invio già esistenti in questo repo, es.
   Outreach/WhatsApp Automation/send_message.py)
6. Da qui in poi, invoca followup-sequencer periodicamente (es. 1 volta/giorno) su
   tutti i lead in stage in_attesa
```

## File di riferimento

- `topology.md` — perché questa topologia (Gatekeeper + Pipeline)
- `shared_state.md` — schema dello stato di ogni lead
- `communication_protocol.md` — formato esatto degli handoff tra agenti
- `coordinator.md` — mandato di coordinamento di rule-keeper
- `handoff_rules.md` — matrice completa chi-passa-cosa-a-chi
- `failure_handling.md` — cosa fa il team se qualcosa va storto (livello team)
- `team_eval_cases.json` — 8 scenari end-to-end per validare il team
- `agents/<ruolo>/` — spec completa di ognuno dei 4 agenti (7 file canonici ciascuno)

## Estensione dichiarata

Il framework sorgente parla esplicitamente di LinkedIn DM. L'applicazione a WhatsApp ed
email è un'estensione richiesta da Max (stessi 5 pilastri, adattati solo nella
lunghezza/formato per canale) — marcata `➕` nel MKD.
