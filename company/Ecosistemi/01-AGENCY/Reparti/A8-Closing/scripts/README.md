---
Type: TOOL
Status: Active
Tags: #scripts #agency #closing #automazione #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# Scripts — A8 Closing / Sales-Call

> Script operativi del reparto. Deterministici, idempotenti, senza LLM in-the-loop dove possibile:
> quello che si può verificare con un `if`, non lo si chiede a un modello.
> Ogni script legge/scrive **solo** dentro il namespace `agency/a8` (vedi `state/README.md`).

---

## `gate_precall.py` — check automatici del Gate Prep

**Cosa fa:** esegue la parte meccanica della checklist di AG-A8-QA sul dossier pre-call, prima che
il verificatore valuti il resto. Verifica: blocchi vuoti, promesse senza prova né `[DM]`, lessico di
scarsità/pressione (R4), prezzi non presenti nel catalogo fisso (R5), SLA ≥2h (R6), PII negli
schemi di state (R7).

**Input:**
- `--call-id CALL-001` (obbligatorio)
- `--dossier agency/a8/prep/CALL-001/dossier.md`
- `--catalogo` path al catalogo prezzi fisso (B-003)
- `--now` timestamp ISO (default: ora corrente)

**Output:**
- Aggiorna `agency/a8/prep/{call_id}/state.json` → campo `qa_gate` (`PASS` / `FAIL` + motivo) e
  `sla_2h_rispettata`.
- Stampa su stdout la lista delle violazioni: `regola | posizione | motivo`.

**Return code:**
- `0` — tutti i check meccanici passati (il gate umano/agente può procedere)
- `1` — almeno una violazione bloccante (R2/R3/R4/R5/R6/R7) → dossier in rework
- `2` — input mancante o dossier illeggibile (non è un FAIL di gate: è un errore di esecuzione)

---

## `check_sla.py` — sorveglianza SLA 2h

**Cosa fa:** scansiona le call in calendario e i debrief aperti; segnala (a) i dossier non ancora
`PASS` a meno di 2h dalla call — rischio **call scoperta** (KPI K9); (b) i debrief non chiusi oltre
2h dalla fine call (R6). Pensato per esecuzione schedulata (ogni 30 min).

**Input:**
- `--calls agency/a8/prep/` + `agency/a8/calls/`
- `--soglia-ore 2` (default)

**Output:**
- Elenco `call_id` a rischio, con ore residue e stato del gate.
- Notifica ad AG-A8-COORD (escalation ad AG-DIR se la SLA non è più recuperabile).

**Return code:**
- `0` — nessuna call a rischio
- `1` — almeno una call a rischio SLA (segnalata, non bloccata: la decisione è di AG-A8-COORD)
- `2` — namespace non accessibile

---

## `debrief_integrity.py` — integrità del namespace `calls`

**Cosa fa:** applica R7 in modo meccanico su tutto `agency/a8/calls`: trova i record con `esito`
popolato ma `motivo` vuoto (call **non chiuse**), i `da-ricontattare` senza data nel next step, e
qualunque PII (pattern email/telefono/nome) finito negli schemi di state.

**Input:**
- `--namespace agency/a8/calls`
- `--fix-pii` (opzionale: rimuove il PII rilevato invece di limitarsi a segnalarlo)

**Output:**
- Report `call_id | problema | regola violata`.
- Con `--fix-pii`: elenco dei campi ripuliti (mai una cancellazione silenziosa).

**Return code:**
- `0` — namespace integro
- `1` — almeno una call senza motivo o un PII rilevato → blocca la chiusura del debrief (R7)
- `2` — namespace non accessibile

---

## `pattern_threshold.py` — soglia 3 evidenze (R8)

**Cosa fa:** prima che AG-A8-LEARN pubblichi un pattern verso A5 / A3 / 08-INTELLIGENCE, verifica
che ogni pattern con `consolidato: true` abbia ≥3 evidenze (`call_id`) realmente esistenti in
`agency/a8/calls`. Declassa ad aneddoto `[DM]` quelli sotto soglia.

**Input:**
- `--patterns agency/a8/patterns/`
- `--min-evidenze 3` (default)

**Output:**
- Pattern promossi (pubblicabili) e pattern declassati a `[DM]`, con motivo.
- Aggiorna il campo `consolidato` nei file pattern.

**Return code:**
- `0` — tutti i pattern rispettano la soglia
- `1` — almeno un pattern declassato (pubblicazione bloccata per quel pattern, R8)
- `2` — errore di lettura del namespace

---

## Regole comuni a tutti gli script

- **Idempotenti:** rieseguire uno script sullo stesso input non cambia il risultato né duplica record.
- **Confinati:** scrivono **solo** in `agency/a8/**`. Mai in `agency/a1|a2|a3|a5` (ADR-003).
- **Zero PII:** nessuno script scrive nomi, email o telefoni; `debrief_integrity.py` li rimuove.
- **Il return code è il gate:** `1` significa "artefatto in rework", non "warning ignorabile".

---

## Connessioni

- [[ag-a8-qa]] · `agenti/ag-a8-qa.md` — usa `gate_precall.py` come motore dei check meccanici
- [[REGOLE]] · `regole/REGOLE.md` — R2–R8, le regole che questi script rendono verificabili
- [[state/README]] · `state/README.md` — namespace su cui gli script operano
