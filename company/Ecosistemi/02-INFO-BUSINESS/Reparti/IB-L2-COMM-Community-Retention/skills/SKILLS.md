---
Type: SKILLS
Status: Active
Tags: #skills #community #retention #onboarding #crosssell #IB-L2-COMM
Created: 2026-06-21
Last updated: 2026-06-21
---

# Skill — IB-L2-COMM Community & Retention

> Mappa delle skill del reparto: skill proprie da forgiare + skill esistenti mappate.

---

## Skill proprie del reparto (da forgiare via 07-FORGE — standard §8 V2)

### `crosssell-bridge` — Priorità P0

**Funzione:** gate G-COMM deterministico per il passaggio studente → lead AGENCY. Calcola lo
score (segnale 3pt + completamento ≥50% 2pt + survey positiva 5pt) e applica i check binari
consenso + segnale documentato + score ≥ soglia. Formalizza la logica di IB-COMM-CROSSSELL +
IB-COMM-QA.

**Quando invocarla:** quando IB-COMM-CROSSSELL ha registrato un segnale studente e deve
verificare se è handoff-ready verso 01-AGENCY (mai outreach automatico).

**Input:** `{studente_id, fonte_prodotto, segnale_tipo, percent_progress, survey_positiva, consenso, data_consenso}`
**Output:** `{score, soglia_raggiunta:bool, consenso_verificato:bool, gate:"PASS"|"FAIL", motivo, dossier_HC_IB_AG_01?}` — handoff solo se gate PASS.

**Dipendenze:** richiede consenso letto come dato verificato (non inferito); segnale documentato in namespace.
**PRD da produrre prima della build:** via 07-FORGE, contradiction-analyzer contro
`referrals` e `community-marketing` (skill ausiliarie esistenti mappate qui).

---

## Skill esistenti mappate a IB-L2-COMM

| Skill | Stato | Ruolo in IB-L2-COMM | Note |
|---|---|---|---|
| `onboarding` | Esistente, mappata | Sequenza attivazione studente per IB-COMM-ONBOARDER (email ≤1h, accesso ≤24h, modulo 1 ≤7gg) | Motore del WF-ONBOARDING-STUDENTE; `crosssell-bridge` non la duplica |
| `churn-prevention` | Esistente, mappata | Win-back e recovery per IB-COMM-RETENTION (sequenze gentili, mai invasive) | Owner d'uso IB-COMM-RETENTION; vincolata da R6 |
| `community-marketing` | Esistente, mappata | Strategia rituali WhatsApp/Discord per IB-COMM-ENGAGE | Ausiliaria: fornisce pattern community, non sostituisce il WF |
| `signup` | Esistente, mappata | Attivazione studente a supporto onboarding | Ausiliaria di IB-COMM-ONBOARDER |
| `referrals` | Esistente, mappata | Passaparola studenti e leva social proof | Ausiliaria di IB-COMM-SOCIAL; non genera outreach cross-sell automatico |

---

## Regola anti-contraddizione

Prima di forgiare `crosssell-bridge`:
1. Eseguire `skill-contradiction-analyzer` contro `referrals`, `community-marketing`, `onboarding`.
2. Se sovrapposizione rilevata: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce.
3. Gerarchia: `crosssell-bridge` = gate/motore decisionale; skill esistenti = ausiliarie o knowledge base.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-COMM` — skill area
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — tabella skill del reparto e gate G-COMM
- [[ib-comm-crosssell]] · `agenti/ib-comm-crosssell.md` — agente che invoca `crosssell-bridge`
- [[ib-comm-qa]] · `agenti/ib-comm-qa.md` — esecutore del gate G-COMM nella skill
