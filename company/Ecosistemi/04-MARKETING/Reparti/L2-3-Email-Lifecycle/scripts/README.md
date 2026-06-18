---
Type: SCRIPTS
Status: Planned
Tags: #scripts #email #lifecycle #automazione #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# Scripts — L2.3 Email & Lifecycle

> Script target V2 deterministici da sviluppare nella fase V2-5 (build ecosistema).
> Nessuno di questi script è ancora operativo — sono specifiche di build per 07-FORGE/06-PLATFORM.
> Standard: script deterministici (stesso input → stesso output), dry-run default (Art.4.3 Mandato).

---

## Script 1 — `sequence-builder.py`

**Scopo:** genera il JSON strutturato di una sequenza email a partire dal tipo (lancio/nurture/
onboarding/winback), dall'ICP e dalla mappa segmenti di E3.
**Input:** `tipo_sequenza`, `icp_id`, `segmenti.json` (output E3), `n_email_target`, `timing_template`.
**Output:** `sequence_map.json` con ogni email: trigger, timing, obiettivo, awareness_level,
branch condizionali, flag note_copy per L2.1.
**Logica:** carica i template narrativi per tipo (da ARCHITETTURA.md §2), applica i segmenti
di E3, genera la struttura JSON. Non scrive copy — produce la struttura per E1 e per L2.1.
**Dry-run default:** genera il JSON senza salvarlo nel namespace; `--commit` per salvataggio.
**Owner:** E1 (the script automatizza parte del ragionamento di E1 per sequenze standard).

---

## Script 2 — `deliverability-check.py`

**Scopo:** verifica automatica di spam score e autenticazione dominio su un batch di email.
**Input:** `emails.json` (testo + oggetto di ogni email), `dominio_mittente`, `lista_sample.json` (pseudonimizzata).
**Output:** `deliverability_report.json` con spam_score per email, flag SPF/DKIM/DMARC, issues lista, gate G3 PASS/FAIL.
**Logica:** integra con API di spam scoring (SpamAssassin o equivalente), verifica DNS per
autenticazione dominio, analizza la lista per pattern anomali (bounce, sequenziali, etc.).
**Nota di sicurezza:** NON elabora dati PII raw — richiede lista pseudonimizzata in input;
se `aidefence_has_pii` rileva dati sensibili → blocco immediato.
**Owner:** E2 (the script automizza il gate G3 per check standard; E2 interpreta il report su casi anomali).

---

## Script 3 — `pii-scan-wrapper.py`

**Scopo:** wrapper deterministico attorno a `aidefence_has_pii` — esegue il check PII su
ogni lista o campione prima dell'elaborazione (Mandato Art.7.2).
**Input:** `lista_sample.json` o `emails.json` (qualsiasi file con dati potenzialmente personali).
**Output:** `pii_check_report.json` — esito (PASS/FAIL), tipo di dato sensibile rilevato se FAIL,
raccomandazione (pseudonimizza campo X, rimuovi campo Y).
**Logica:** chiama `aidefence_has_pii`, classifica il tipo di PII rilevato (nome, email raw,
telefono, CF), produce il report. Se FAIL → non procede; blocca e segnala.
**Dry-run default:** sempre (non elabora la lista, solo scansiona un campione).
**Owner:** E2 (il PII check è responsabilità di E2 — questo script lo rende deterministico e loggabile).

---

## Regole per lo sviluppo di questi script

1. **Dry-run default** — ogni script deve avere un flag `--commit` per abilitare il salvataggio
   nel namespace. Senza `--commit`, il default è dry-run (Art.4.3 Mandato).
2. **Idempotente** — lo stesso input produce lo stesso output; eseguire due volte non crea
   duplicati nel namespace.
3. **Log obbligatorio** — ogni esecuzione logga in `marketing/email/sequences/{id}/script_log.json`
   con timestamp, parametri, esito.
4. **Nessun dato PII raw** — nessuno script elabora o salva dati personali raw; solo
   pseudonimizzati o aggregati.

---

## Connessioni

- [[e2-deliverability-guard]] · `agenti/e2-deliverability-guard.md` — owner script 2 e 3
- [[e1-lifecycle-architect]] · `agenti/e1-lifecycle-architect.md` — owner script 1
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — §5 PII policy; §4 namespace
