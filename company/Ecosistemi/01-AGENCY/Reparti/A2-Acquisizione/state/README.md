---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #agency #acquisizione #outreach #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# State — A2 Acquisizione / Outreach

> Definizione dei namespace memoria del reparto, struttura dei file di stato, regole di
> integrità e PII, lifecycle. **Nessuna PII nello schema** (REGOLE R3): solo riferimenti
> interni e contatori. Le baseline KPI sono `[DM]` finché non misurate.

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Outreach (cross-canale) | `agency/outreach` | Template attivi, performance per variante, log invii | AG-A2-WRITE + AG-A2-SEND | AG-A2-COORD, AG-A2-QA |
| Email | `agency/02-acquisizione/email/` | Per batch: inviati, bounce, esiti gate Bibbia | AG-A2-SEND | AG-A2-COORD, AG-A2-QA |
| LinkedIn | `agency/02-acquisizione/linkedin/` | Conn/msg/commenti per giorno, accettazioni | AG-A2-LI | AG-A2-COORD, AG-A2-TRIAGE |
| Instagram | `agency/02-acquisizione/instagram/` | DM/gg, stato follow-up | AG-A2-IG | AG-A2-COORD, AG-A2-TRIAGE |
| Reply | `agency/02-acquisizione/reply/` | Thread per lead, stato triage, esito | AG-A2-TRIAGE + AG-A2-BOOK | AG-A2-COORD, AG-A2-FUP |

Nota: lo state runtime del motore (`leads.db`, `emails_*_ready.json`, sessioni) resta in
`Outreach/Outreach Workflow/` e NON è duplicato qui.

---

## Struttura file di stato

### Email batch state (`agency/02-acquisizione/email/state.json`)

```json
{
  "batch_id": "BATCH-20260622-001",
  "data": "YYYY-MM-DD",
  "cap_giornaliero": 500,
  "cap_orario": 100,
  "inviati_oggi": 0,
  "cap_residuo": 500,
  "bounce": 0,
  "gate_bibbia": { "pass": 0, "fail": 0, "fail_per_check": {"apsoc": 0, "cta": 0, "dependency": 0} },
  "stato_run": "in_corso | completata | cap_raggiunto | sospesa_credenziale",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### LinkedIn state (`agency/02-acquisizione/linkedin/state.json`)

```json
{
  "data": "YYYY-MM-DD",
  "cap": { "connessioni": 20, "messaggi": 20, "commenti": 30 },
  "fatti_oggi": { "connessioni": 0, "messaggi": 0, "commenti": 0 },
  "accettazioni_pending": 0,
  "stato_run": "in_corso | completata | cap_raggiunto | sospesa_sessione",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Instagram state (`agency/02-acquisizione/instagram/state.json`)

```json
{
  "data": "YYYY-MM-DD",
  "cap_dm": 30,
  "dm_inviati_oggi": 0,
  "cap_residuo": 30,
  "followup_pending": 0,
  "stato_run": "in_corso | completata | cap_raggiunto | sospesa_sessione",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Reply thread state (`agency/02-acquisizione/reply/{thread_id}.json`)

```json
{
  "thread_id": "TH-0001",
  "lead_ref": "rif. interno (NO PII — pii_scan: passed)",
  "canale": "email | linkedin | instagram",
  "stato_triage": "interessato | obiezione | no | out_of_office",
  "followup_inviati": 0,
  "slot_proposto": "YYYY-MM-DDTHH:MM | null",
  "slot_confermato": false,
  "esito": "in_gestione | call_confermata | chiuso_no | chiuso_no_risposta",
  "handoff": "HC-AG-CL-01 | null",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Regole di integrità dei namespace

1. **PII-scan obbligatorio** — nessun record nel namespace `reply` viene scritto senza
   `pii_scan: passed` (`aidefence_has_pii`). Lo schema non contiene nomi/email/handle in chiaro.
2. **Cap residuo coerente** — `inviati_oggi + cap_residuo` deve sempre uguagliare il cap del
   giorno. Una run non può portare `cap_residuo` sotto 0 (REGOLE R2).
3. **Gate prima dell'invio** — ogni incremento di `inviati_oggi` (email) deve avere un
   corrispondente PASS in `gate_bibbia.pass`. Invii senza gate verde = anomalia (REGOLE R1).
4. **No handoff senza slot** — un thread con `handoff != null` deve avere `slot_confermato: true`
   (REGOLE R6).
5. **Ripartibilità a freddo** — tutti gli state hanno `last_updated`. Una run interrotta riprende
   dal `cap_residuo` del giorno senza risuperare i lead già processati.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Email/LI/IG state | Inizio run del giorno | A ogni invio (cap residuo) | A fine giornata; storico per ciclo |
| Reply thread state | Prima risposta del lead | A ogni step triage/follow-up/booking | Dopo `call_confermata` o `chiuso_*`; non eliminato |
| Performance variante | Primo invio della variante | A ogni ciclo di reply rate | Variante ritirata se in calo 2 cicli → refresh A5 |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §5` — namespace e regola PII
- [[regole/REGOLE]] · `regole/REGOLE.md` — R2 (cap), R3 (PII), R6 (handoff)
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi state
