> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 SKILL-WORKS · L3 WF-SKILL-AUDIT

# WF-SKILL-AUDIT — Workflow L3: Audit Anti-Drift delle Skill

**Ecosistema:** 07-FORGE · **Reparto:** SKILL-WORKS (L2.1) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Rilevare **contraddizioni, duplicazioni e drift** tra skill della holding prima che
arrivino in produzione o periodicamente sulle skill già installate. Strumento principale:
`skill-contradiction-analyzer`. Gate obbligatorio (G-CONTRADICTION) su ogni rilascio.

---

## Quando si usa

- Prima di ogni consegna di skill nuova o migliorata (gate G-CONTRADICTION in WF-SKILL-NEW e WF-SKILL-IMPROVE)
- Audit periodico trimestrale sull'intero set di 121+ skill (pianificato da OPERATIONS/WF-CRON)
- Quando due skill dello stesso dominio vengono aggiornate in cicli ravvicinati (rischio divergenza)
- Su richiesta del Drift-Sentinel (Backbone) quando rileva anomalie nell'output di skill correlate

---

## Fasi del workflow

| Fase | Attore | Output | Azione |
|---|---|---|---|
| **Selezione scope** | `frg-contradiction-gate` | lista skill da auditare (singola, coppia, set tematico, full) | definita da `frg-chief` in base al trigger |
| **Scan contradiction-analyzer** | `frg-contradiction-gate` | report JSON: contraddizioni classificate per severità | `skill-contradiction-analyzer` su ogni coppia/set |
| **Triage** | `frg-contradiction-gate` + `frg-chief` | contraddizioni classificate: bloccanti / warnings / informative | bloccanti = stop rilascio; warnings = log + segnalazione |
| **Risoluzione bloccanti** | `frg-skill-smith` | skill corrette o riscoping | torna a WF-SKILL-NEW / WF-SKILL-IMPROVE per fix |
| **Segnalazione warnings** | `frg-hr-registrar` | issue aperta in `forge/evals/` | Drift-Sentinel notificato se impatta schema canonico |
| **Report audit** | `frg-contradiction-gate` | audit-report.md in `forge/evals/` + entry wiki/log.md | archivio permanente per trend analysis |

---

## Classificazione contraddizioni

| Severità | Definizione | Azione |
|---|---|---|
| **BLOCCANTE** | Due skill affermano comportamenti opposti per lo stesso input; una skill nega un invariante di un'altra | Blocca il rilascio; richiede risoluzione PRIMA di ship |
| **WARNING** | Due skill hanno overlap di funzione (rischio duplicazione) o linguaggio inconsistente | Log + segnalazione; risoluzione nel ciclo successivo |
| **INFORMATIVA** | Differenze stilistiche, naming inconsistente, ma semantica coerente | Registrata per il ciclo di standardizzazione (Copy/APSOC Guild) |

---

## Scope dell'audit trimestrale (pianificato)

OPERATIONS/WF-CRON pianifica l'audit completo ogni 90 giorni:
- Input: intero `skills-map.yaml` (121+ skill)
- Output: contradiction-report-YYYYMMDD.md in `forge/evals/`
- Distribuzione: `frg-chief` → Board (C-Suite) → notifica Drift-Sentinel

---

## KPI

| Metrica | Target |
|---|---|
| Contraddizioni bloccanti rilasciate in produzione | 0 |
| Tempo risoluzione contraddizione bloccante | ≤ 1 giorno |
| Copertura audit trimestrale (skill auditata / totale) | 100% |
| Warnings risolti entro ciclo successivo | ≥ 70% |
