---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #community #retention #onboarding #crosssell #IB-L2-COMM
Created: 2026-06-21
Last updated: 2026-06-21
---

# Script — IB-L2-COMM Community & Retention

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da IB-COORD-COMMUNITY senza approvazione aggiuntiva.

---

## Script pianificati (build in V2)

### `onboarding-tracker.py`

**Scopo:** legge lo stato accesso/progress da formazione-admin + formazione-student per una
coorte e produce il report milestone (accesso ≤24h, modulo 1 ≤7gg) con flag per studente.
IB-COMM-HEALTH lo usa per il report di coorte; gli studenti in ritardo vengono marcati per
recovery (IB-COMM-RETENTION).

**Input:** `{coorte_id, studenti[]:{studente_id, ultimo_accesso, moduli_completati[], percent_progress}}`
**Output:** `{coorte_id}_health.json` in `infobusiness/community/health/` con flag `onboarding_24h`, `modulo1_7gg`, `a_rischio`.
**Prerequisiti:** lettura piattaforma autorizzata; nessuna PII oltre `studente_id` (R8).

---

### `crosssell-scorer.py`

**Scopo:** calcola lo score deterministico di un segnale cross-sell (segnale 3pt + completamento
≥50% 2pt + survey positiva 5pt) e prepara il dossier candidato. NON decide l'handoff: produce
il candidato che IB-COMM-QA verifica al gate G-COMM (consenso). Score ≥5 senza consenso resta
in attesa, non passa.

**Input:** `{studente_id, segnale_tipo, percent_progress, survey_positiva:bool, consenso:bool, data_consenso}`
**Output:** `crosssell_candidate.json` con `score`, `soglia_raggiunta`, `consenso_presente`, `gate_richiesto:true` — in `infobusiness/community/crosssell/`.
**Prerequisiti:** segnale documentato; il campo consenso non è calcolato, è letto come dato verificato.

---

### `engagement-report.py`

**Scopo:** aggrega i log dei rituali settimanali (prompt, bonus, Q&A) e il login/interazione per
produrre il report mensile engagement della community (% studenti attivi/settimana, progress
medio, segnali abbandono). Supporto a IB-COMM-HEALTH per il report a IB-COORD-COMMUNITY.

**Input:** `{mese, coorte_id, log_rituali[], attivita_studenti[]:{studente_id, settimane_attive}}`
**Output:** `{mese}_community.md` in `infobusiness/community/engagement/` con tabella engagement + flag `[DM]` dove la baseline non esiste ancora.
**Prerequisiti:** log rituali presenti; nessun numero inventato (P5) — celle senza dato = `[DM]`.

---

## Convenzioni

- Tutti gli script producono file in `infobusiness/community/` (namespace corretto) — mai fuori.
- Nessuno script fa outreach o invii autonomi: producono dati e dossier, non contattano studenti (R2).
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Nessuna PII oltre l'identificativo: `studente_id` / `lead_id`, mai email/telefono (R8).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria su cui gli script scrivono
- [[state/README]] · `state/README.md` — schema dei file JSON prodotti dagli script
- [[WF-ONBOARDING-STUDENTE]] · `workflow/WF-ONBOARDING-STUDENTE.md` — usa `onboarding-tracker.py`
- [[WF-COMMUNITY-ATTIVA]] · `workflow/WF-COMMUNITY-ATTIVA.md` — usa `engagement-report.py`
