---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #ricerca #lead #intelligence #agency #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# ARCHITETTURA — A1 Ricerca & Market Intelligence

> Documento di architettura interna del reparto. Descrive forma, missione, gerarchia,
> flussi, gate, confini e namespace. Reparto L2 di 01-AGENCY.

---

## 1. Forma e missione

**Forma:** reparto CF-grade, topologia `star`. Un coordinatore (AG-A1-COORD) orchestra
8 agenti specializzati su 3 workflow. Un verificatore (AG-A1-QA) è bloccante su ogni output.

**Missione.** Alimentare il funnel di 01-AGENCY con **lead qualificati** e fornire a
Acquisizione (A2), Preventivi (A3) e Delivery (A4) l'**intelligence di nicchia** per vendere
e consegnare meglio. A1 è il primo anello della pipeline revenue: senza A1, A2 non ha nulla
da contattare e A3 non ha dossier per la discovery call.

**Posizionamento V2:** team di 9 agenti, 3 workflow CF-grade.
Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md` §A1.

**ADR-003 WRAP-not-rewrite:** A1 NON riscrive lo scraper runtime esistente. Wrappa
`Outreach/Outreach Workflow/` (scraper multi-fonte, `extractor.py`, `qualifier.py`),
`competitor.py`, `cro_audit.py`, la skill `market-audit` e la skill `icp-radar`.
Li documenta, li orchestra, ne legge/scrive lo stato — mai ne propone la riscrittura.

---

## 2. Gerarchia interna (roster 9 agenti)

```
01-AGENCY (L1) — AG-DIR
   └── A1 Ricerca & Market Intelligence (L2)
         │
         AG-A1-COORD (coordinatore, sonnet)
         ├── AG-A1-SCRAPE (runner scraper, haiku)
         │     → Maps / Apify / Outscraper / Google in parallelo
         ├── AG-A1-EXTRACT (estrattore, haiku)
         │     → raw HTML/JSON → schede lead strutturate
         ├── AG-A1-QUAL (qualificatore ICP, sonnet)
         │     → score lead vs ICP corrente; triage
         ├── AG-A1-ICP (ICP profiler, sonnet)
         │     → crea/aggiorna profili ICP per nicchia (skill icp-radar)
         ├── AG-A1-COMP (analista competitor/audit, sonnet)
         │     → dossier competitor (competitor.py, cro_audit.py, market-audit)
         ├── AG-A1-INTEL (analista di mercato, sonnet)
         │     → trend di nicchia; sourcing da 08-INTELLIGENCE
         ├── AG-A1-BRIEF (brief pre-call, sonnet)
         │     → aggrega dossier per la discovery call di A8-Closing
         └── AG-A1-QA (verificatore dati, sonnet)
               → valida score ICP, freschezza, GDPR-light; blocca lead incompleti
```

**Principio di coordinamento:** AG-A1-COORD riceve il task, decide la priorità delle nicchie,
spacchetta in fan-out `star` e riporta ad AG-DIR. AG-A1-QA è bloccante su ogni output del
reparto: nessun lead, nessun report intel, nessun dossier pre-call esce senza il suo gate.

---

## 3. Flussi principali (3 workflow CF-grade)

### 3.1 WF-LEAD-SOURCING [WRAPPA-ESISTENTE]

```
[TRIGGER: run schedulata da 09-OPERATIONS | richiesta lead da A2]
         │
         ▼
AG-A1-COORD — nicchia nuova? → prima AG-A1-ICP (non si scrappa senza ICP esplicito)
         │
         ▼
AG-A1-SCRAPE — fonti in parallelo: Maps · Apify · Outscraper · Google
  (wrappa scraper/*.py — log per fonte in agency/leads)
         │
         ▼
AG-A1-EXTRACT — raw → schede lead (nome, email, telefono, sito, settore)
  (wrappa extractor.py)
         │
         ▼
AG-A1-QUAL — score lead vs ICP corrente (wrappa qualifier.py); triage:
  qualificato / nurture / scarta CON motivo
         │
         ▼
AG-A1-QA — GATE: completezza dati ≥80%, no duplicati, GDPR-light
  → PASS: store in leads.db + agency/leads
  → FAIL: lead incompleto bloccato; motivo registrato
```

### 3.2 WF-MARKET-INTEL [TARGET-V2]

```
[TRIGGER: cadenza settimanale per report nicchia | on-demand audit prospect]
         │
         ▼
AG-A1-INTEL (ricerca trend, sourcing da 08-INTELLIGENCE)
  +  AG-A1-COMP (audit competitor per prospect — competitor.py, cro_audit.py, market-audit)
         │
         ▼
AG-A1-ICP — aggiorna profilo ICP della nicchia (skill icp-radar)
         │
         ▼
AG-A1-QA — GATE: fonti citate e verificabili (ADR-002 wiki-first); nessuna metrica inventata
  → report in agency/intel: {nicchia, trend, competitor_top3, ICP_aggiornato, opportunita}
  → ingest in 08-INTELLIGENCE
```

### 3.3 WF-BRIEF-PRE-CALL [TARGET-V2]

```
[TRIGGER: A8-Closing richiede dossier pre-call per il lead Y, ≥2h prima della call]
         │
         ▼
AG-A1-BRIEF aggrega:
  lead score (da agency/leads) + audit problema (competitor.py, cro_audit.py)
  + ICP match (agency/a1/icp) + contesto nicchia (agency/intel)
         │
         ▼
AG-A1-QA — GATE: nessun campo "da compilare" vuoto; dossier completo
         │
         ▼
documento MD/PDF strutturato → consegnato ad A8-Closing ≥2h prima della call
```

---

## 4. Gate del reparto

| Gate | Workflow | Condizione PASS | Owner |
|---|---|---|---|
| G-SOURCING | WF-LEAD-SOURCING | Completezza dati ≥80%, no duplicati, GDPR-light | AG-A1-QA |
| G-INTEL | WF-MARKET-INTEL | Fonti citate e verificabili; nessuna metrica inventata (Mandato Art.2) | AG-A1-QA |
| G-BRIEF | WF-BRIEF-PRE-CALL | Nessun campo vuoto; dossier consegnato prima della call (SLA) | AG-A1-QA |
| G-ICP | WF-MARKET-INTEL | ICP con fonti citate prima dello scraping di nuova nicchia | AG-A1-QA |

**Regola d'oro:** AG-A1-QA non ha deroga per urgenza. Un lead incompleto, un report con
metrica inventata, un dossier con campi vuoti = FAIL. Escalation, non bypass.

---

## 5. Confine con i reparti vicini

| Aspetto | A1 Ricerca | Reparto partner |
|---|---|---|
| Scraping runtime | Wrappa e orchestra (ADR-003) | `Outreach/Outreach Workflow/` possiede il runtime |
| Outreach | Consegna lead qualificati in leads.db | A2-Acquisizione esegue il contatto |
| Preventivo | Consegna dossier pre-call + audit problema | A3-Preventivi costruisce l'offerta |
| Discovery call | Consegna brief pre-call ≥2h prima | A8-Closing conduce la call |
| ICP / trend | Produce e cita fonti | 08-INTELLIGENCE è sorgente e destinazione ingest |

---

## 6. Namespace memoria — `agency/a1` + `agency/leads`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/leads` | Lead, score, stato funnel (specchio semantico di leads.db) | AG-A1-EXTRACT, AG-A1-QUAL |
| `agency/a1/sourcing` | Run di sourcing: fonte, n. raw, n. qualificati, errori | AG-A1-SCRAPE, AG-A1-COORD |
| `agency/a1/icp` | Profili ICP per nicchia (con fonti citate) | AG-A1-ICP |
| `agency/a1/intel` | Report nicchia: trend, competitor_top3, opportunità | AG-A1-INTEL |
| `agency/a1/dossier` | Dossier pre-call per discovery (A8) | AG-A1-BRIEF |
| `agency/reasoning` | Motivi di scarto lead, failure distillati (pattern) | AG-A1-COORD, AG-A1-QUAL |

**Regola di integrità:** ogni lead in `agency/leads` ha campo `score` e `fonte`. Ogni report
in `agency/a1/intel` ha campo `fonti[]` non vuoto. Senza, l'artefatto non è chiuso.

---

## 7. State e ripartibilità

Ogni run di WF-LEAD-SOURCING produce `agency/a1/sourcing/state.json` con:
- `run_id`, `nicchia`, `fonti[]` con n. raw per fonte
- `n_qualificati`, `n_scartati`, `errori[]`
- `gate_qa` — pending / PASS / FAIL + motivo
- `last_updated` — timestamp

Questo permette la **ripartibilità a freddo**: una run interrotta riprende dall'ultima fonte
completata senza riscrappare tutto (test amnesia §6 V2).

---

## 8. Struct-checklist del reparto

- [ ] ARCHITETTURA.md (questo file)
- [ ] README.md (overview + handoff — preesistente, mantenuto)
- [ ] agenti/ — 9 schede (una per agente del roster)
- [ ] kpi/KPI.md · principi/PRINCIPI.md · regole/REGOLE.md
- [ ] scripts/README.md · skills/SKILLS.md · state/README.md
- [ ] workflow/ — WF-LEAD-SOURCING · WF-MARKET-INTEL · WF-BRIEF-PRE-CALL

---

## Connessioni

- [[README]] · `README.md` — missione, roster, handoff del reparto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
- [[WF-LEAD-SOURCING]] · `workflow/WF-LEAD-SOURCING.md`
- [[WF-MARKET-INTEL]] · `workflow/WF-MARKET-INTEL.md`
- [[WF-BRIEF-PRE-CALL]] · `workflow/WF-BRIEF-PRE-CALL.md`
- [[state/README]] · `state/README.md` — namespace `agency/a1` + `agency/leads`
