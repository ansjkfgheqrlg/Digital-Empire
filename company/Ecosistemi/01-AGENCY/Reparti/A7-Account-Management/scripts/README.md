---
Type: TOOL
Status: Experimental
Tags: #scripts #account-management #automazione #health #nps #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# scripts — A7 Account Management & Customer Success

> Script **previsti** del reparto. Sono wrapper sui motori esistenti (ADR-003): leggono e scrivono
> lo state in `agency/a7/*`, non reimplementano `churn-prevention`, `upsell-mapper`, `support-90`
> né `revops`. Nessuno script invia comunicazioni al cliente: l'invio resta umano.

---

## `health_scan.py`

**Cosa fa:** esegue la scansione settimanale di salute su tutti i clienti attivi. Legge milestone
(`agency/a7/clients`), SLA ticket (`agency/a4/sla`, sola lettura) e touchpoint recenti; applica le
soglie di `churn-prevention`; scrive la dashboard e propone gli alert ad AG-A7-COORD.

- **Input:** `--client-id <id>` (opzionale; senza, scansiona tutti i clienti attivi) · `--dry-run`
- **Output:** `agency/a7/health/{client_id}` aggiornato · alert proposti in `agency/a7/alerts`
- **Return code:** `0` scan completo, nessun alert · `1` errore di lettura state · `2` **alert alzato**
  (rosso o giallo) — il chiamante deve instradarlo ad AG-A7-COORD · `3` segnali insufficienti →
  `health_score: [DM]` (mai uno score inventato)

---

## `alert_watchdog.py`

**Cosa fa:** verifica che ogni alert aperto in `agency/a7/alerts` abbia un'azione correttiva
registrata entro **24h** dal timestamp del segnale (R2). A scadenza, escala ad AG-DIR.

- **Input:** `--window-hours 24` (default) · `--dry-run`
- **Output:** lista alert scaduti · escalation registrata in `agency/a7/alerts/{alert_id}.stato`
- **Return code:** `0` nessun alert scaduto · `1` errore state · `2` **alert scaduti trovati** →
  escalation AG-DIR emessa (bloccante: il ciclo del cliente non avanza)

---

## `nps_collect.py`

**Cosa fa:** prepara il ciclo di raccolta NPS a G+90 — identifica i clienti in scadenza, prepara la
richiesta (che AG-A7-COMM drafta e **Max invia**), registra la risposta ricevuta e i follow-up.
**Non invia nulla in autonomia** e **non stima mai un NPS** (R5, P5).

- **Input:** `--client-id <id>` · `--record <0-10>` (registra una risposta già ricevuta) ·
  `--followup` (segna un follow-up eseguito, max 2)
- **Output:** campo `nps` + `nps_data_raccolta` in `agency/a7/clients/{client_id}`; touchpoint in
  `agency/a7/touchpoints`
- **Return code:** `0` NPS registrato · `1` errore state · `2` **NPS ancora `[DM]`** dopo 2 follow-up
  → closure `chiuso_con_riserva` + escalation AG-DIR · `3` tentativo di scrivere un NPS non
  dichiarato dal cliente → **rifiutato** (violazione R5)

---

## `kpi_snapshot.py`

**Cosa fa:** calcola i KPI del reparto **dallo state** (mai da stime) e scrive lo snapshot datato
in `agency/a7/gates/`. È l'unica fonte del report mensile verso AG-DIR.

- **Input:** `--period YYYY-MM` · `--format md|json`
- **Output:** snapshot KPI in `agency/a7/gates/kpi-{period}.{md|json}`
- **Return code:** `0` snapshot completo · `1` errore state · `2` **KPI non calcolabile** (dato di
  input mancante, es. SLA ticket non prodotto da A4) → il KPI vale `[DM]`, non zero; segnalato a QA

---

## `state_lint.py`

**Cosa fa:** valida l'integrità del namespace `agency/a7/*` prima di ogni commit. Controlla le
invarianti bloccanti: `kam` popolato su ogni cliente (R1), nessun PII/segreto nello state (R7),
touchpoint loggati contro la cadenza (R3), nessun `nps` scritto senza `nps_data_raccolta`.

- **Input:** `--path agency/a7` · `--strict` (default in CI)
- **Output:** report violazioni con puntatore preciso (chiave, campo, regola violata)
- **Return code:** `0` state pulito · `1` errore di lettura · `2` **violazione bloccante** (R1/R3/R5/R7)
  → il commit **non passa**

---

## Convenzioni comuni

- Ogni script è **idempotente**: rieseguirlo sullo stesso state non duplica alert, touchpoint o record.
- Ogni script accetta `--dry-run` e stampa cosa **farebbe** senza scrivere.
- Nessuno script decide un'azione correttiva, concede una leva commerciale (R6) o invia una
  comunicazione: propone, registra, blocca. La decisione è di AG-A7-COORD o di Max.
- `return code 2` significa sempre **"condizione bloccante rilevata"**, mai "errore tecnico".

---

## Connessioni

- [[ag-a7-health]] · `agenti/ag-a7-health.md` — consumatore principale di `health_scan.py`
- [[ag-a7-qa]] · `agenti/ag-a7-qa.md` — consumatore di `state_lint.py` e `kpi_snapshot.py`
- [[REGOLE]] · `regole/REGOLE.md` — le invarianti che gli script rendono eseguibili
- [[KPI]] · `kpi/KPI.md` — le metriche calcolate da `kpi_snapshot.py`
