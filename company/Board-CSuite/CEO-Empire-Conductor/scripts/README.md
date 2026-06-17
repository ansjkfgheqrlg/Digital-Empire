---
Type: CONCEPT
Status: Active
Tags: #ceo #scripts #dispatch #report #automazione
Created: 2026-06-17
Last updated: 2026-06-17
---

# SCRIPTS — Script di Dispatch e Report della Figura CEO

> Descrizione degli script previsti (non implementazione). Build effettiva: fase V2-build CEO.
> Connessioni: [[WF-DECISIONE-STRATEGICA]] · [[WF-REVIEW-TRIMESTRALE]] · [[STATE]]

---

## Convenzione

Gli script di questa figura sono in Python (logica) e PowerShell (dispatch Windows). Ogni script
legge il proprio input da `state/` o da file JSON passato come argomento, scrive l'output in
`state/` e logga in `scripts/logs/`. Nessun script modifica direttamente i file Memory senza
passare dalla skill `decision-record`.

---

## Script 1: `dispatch_directive.py`

### Cosa fa
Dispatcha un handoff contract verso un ecosistema o figura C-Suite destinataria. Legge il
pacchetto di direttiva prodotto da `ceo-comunicatore`, lo scrive nel bus corporativo (o
nello state target del destinatario), logga il dispatch in `board/ceo/direttive-dispatch`.

### Input
- `handoff_contract.json` — file JSON prodotto da `ceo-comunicatore` con tutti i campi
  obbligatori (handoff_id, da, a, payload, acceptance_criteria, deadline, conferma_richiesta).

### Output
- Scrittura del contratto in `state/direttive-dispatch/<handoff_id>.json`
- Log in `scripts/logs/dispatch_YYYYMMDD.log` con: timestamp, handoff_id, destinatario, esito.
- Return code: 0 se successo, 1 se destinatario non trovato, 2 se campi mancanti.

### Validazione pre-dispatch
Blocca se: `acceptance_criteria` è array vuoto; `deadline` è null o passata; `a` è destinatario
non registrato nel registro-agenti. Non dispatcha mai senza questi controlli.

---

## Script 2: `collect_kpi_report.py`

### Cosa fa
Raccoglie i progress report degli OKR da tutti gli ecosistemi owner. Scrive le richieste in
`state/okr-trimestre/richieste/` e aggrega le risposte ricevute entro la deadline in
`state/okr-trimestre/aggregato_YYYYMMDD.json`. Flagga gli ecosistemi che non hanno risposto.

### Input
- `state/okr-trimestre/okr_correnti.json` — lista OKR con owner e deadline risposta.
- Argomento `--deadline YYYY-MM-DD` — data entro cui le risposte sono attese.

### Output
- `state/okr-trimestre/aggregato_YYYYMMDD.json` — progress aggregato.
- `state/okr-trimestre/mancanti_YYYYMMDD.json` — lista ecosistemi che non hanno risposto.
- Log in `scripts/logs/kpi_collect_YYYYMMDD.log`.

### Logica di raccolta
Legge le risposte da `state/okr-responses/<ecosistema>/<okr_id>_response.json`. Se il file
non esiste entro la deadline → ecosistema marcato come "mancante". Non stima né interpola
risposte mancanti.

---

## Script 3: `board_report.py`

### Cosa fa
Produce il report Board periodico (settimanale o pre-review) aggregando: stato direttive
dispatch (da `state/direttive-dispatch/`), stato OKR (da `state/okr-trimestre/`), alert
aperti (da `state/alerts/`). Output: report MD formattato per il conductor.

### Input
- `--periodo YYYYMMDD-YYYYMMDD` — intervallo temporale del report.
- `--formato markdown | json` — formato output.

### Output
- `reports/board_report_YYYYMMDD.md` (o .json) con sezioni: riepilogo direttive, OKR status,
  alert aperti, decisioni pendenti, nota per il conductor.
- Log in `scripts/logs/board_report_YYYYMMDD.log`.

### Regole di produzione
Nessun numero inventato: ogni campo del report cita la fonte (file state, timestamp, handoff_id).
Se i dati non sono disponibili → campo marcato "dato mancante: richiesta a [source]".

---

## Script 4: `verify_execution.ps1`

### Cosa fa
Monitora lo stato delle direttive dispatched e produce alert per quelle scadute o non confermate.
Gira in background su schedule (es. ogni 4 ore) e scrive gli alert in `state/alerts/`.

### Input
- `state/direttive-dispatch/*.json` — tutti i handoff dispatched con stato e deadline.

### Output
- `state/alerts/YYYYMMDD_HHMM_alert.json` per ogni direttiva scaduta o non confermata.
- Ogni alert contiene: handoff_id, destinatario, scadenza, giorni di ritardo, AC mancanti.
- Log in `scripts/logs/verify_YYYYMMDD.log`.

### Schedule raccomandato
Ogni 4 ore durante la giornata lavorativa. Non gira nelle ore notturne per evitare false allerte.

---

## Script 5: `checkpoint_writer.py`

### Cosa fa
Scrive un checkpoint in `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md` a partire da un
JSON di decisione. Usa il template ufficiale da `company/Memory/templates/`. Non scrive
checkpoint "liberi" senza template. Dopo la scrittura aggiorna automaticamente STATO-EMPIRE.

### Input
- `decisione.json` — JSON della decisione con tutti i campi (titolo, rationale, azioni, voto).
- `--tipo operativa | architetturale` — determina se scrivere solo checkpoint o anche ADR.

### Output
- `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md` — checkpoint scritto.
- Se `--tipo architetturale`: `company/Memory/decisions/ADR-NNN.md` — ADR draft.
- Aggiornamento di `company/Memory/STATO-EMPIRE.md` (sezione RIPRESA DA).
- Return code: 0 successo, 1 template non trovato, 2 contradiction check fallito.

---

## Connessioni

- [[WF-DECISIONE-STRATEGICA]] · `workflow/WF-DECISIONE-STRATEGICA.md`
- [[WF-REVIEW-TRIMESTRALE]] · `workflow/WF-REVIEW-TRIMESTRALE.md`
- [[ceo-comunicatore]] · `agenti/ceo-comunicatore.md`
- [[ceo-verificatore]] · `agenti/ceo-verificatore.md`
- [[ceo-memoria]] · `agenti/ceo-memoria.md`
- [[STATE]] · `state/README.md`
