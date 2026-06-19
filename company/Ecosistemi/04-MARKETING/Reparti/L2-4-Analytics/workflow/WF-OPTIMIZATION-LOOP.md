---
Type: WORKFLOW
Status: Active
Tags: #workflow #loop #ottimizzazione #ReasoningBank #apsoc #copy #analytics #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-OPTIMIZATION-LOOP — Loop Data-Driven di Ottimizzazione

> **ID:** WF-AN-002 · **Owner:** `an-lead` · **Reparto:** L2.4 Analytics & Ottimizzazione
> **Trigger:** campagna attiva da ≥7 giorni con dati sufficienti per diagnosi

---

## Scopo

Chiudere il cerchio tra dato di performance e revisione di copy. È il workflow che
rende il sistema auto-migliorante: ogni run di copy o campagna alimenta la ReasoningBank
con pattern vincenti e antipattern per ICP, che il COPY-MASTER usa nel prossimo ciclo.

Il loop ha 6 passi fissi. Ogni passo produce un output strutturato che diventa input
del passo successivo. Il ciclo è tracciato in `state.json` e ripartibile a freddo.

**Gate d'uscita:** ciclo completo con tutti i 6 passi tracciati in state.json. Pattern
distillati solo con evidenza ripetuta (regola anti-rumore AN4: ≥2 run indipendenti).

---

## Attori

| Passo | Agente | Responsabilità |
|---|---|---|
| 1 — Raccolta | `an2-attribution-analyst` + `an5-funnel-analyst` | Performance per copy_id e drop rate per sezione APSOC |
| 2 — Diagnosi | `an2-attribution-analyst` | Quale sezione APSOC sotto-performa? |
| 3 — Distilla | `an4-insight-distiller` | Performance → pattern/antipattern ReasoningBank |
| 4 — Revisione | `an-lead` (richiesta a COPY-MASTER L2.1) | Rework mirato sezione diagnosticata |
| 5 — Test | `an3-experiment-designer` | Vecchia variante vs nuova — verdetto statistico |
| 6 — Consolida | `an4-insight-distiller` + `an-lead` | Winner → pattern library; wiki/log.md |

---

## Flusso passo-passo

```
[TRIGGER]
AN-OBSERVER o AN-LEAD: campagna CAMP-XXX ha KPI sotto target
  → apre ciclo WF-OPTIMIZATION-LOOP su campagna_id
  → state.json inizializzato con ciclo_id e timestamp
        │
        ▼
[PASSO 1 — RACCOLTA]
  AN2: performance per copy_id (CTR, opt-in rate, vendite, reply per canale)
  AN5: drop rate per sezione APSOC su landing/funnel (dove abbandona il lettore?)
  → output strutturato con copy_ids, metriche, sezioni, run_indipendenti disponibili
  → stato ciclo: "raccolta_completata"

        │
        ▼
[PASSO 2 — DIAGNOSI]
  AN2 + AN5: quale sezione APSOC corrisponde al drop/problema?
  → CTR basso = sezione A (hook) 
  → alto CTR ma bassa conversione landing = sezione P/S o struttura landing
  → alta visita CTA ma bassa conversione = sezione O (obiezioni non risolte)
  → diagnosi con metrica esplicita: "sezione A debole su CP-001, CTR 0.9% vs 2.8% CP-002"
  → stato ciclo: "diagnosi_completata"
  → GATE-1: diagnosi con evidenza dati (non opinione) → prosegui

        │
        ▼
[PASSO 3 — DISTILLA]
  AN4: verifica regola anti-rumore → ≥2 run indipendenti stessa ICP stessa osservazione?
  → SÌ: distilla pattern/antipattern → memory_store in marketing/copy/patterns/{icp}
        e marketing/copy/antipatterns/{icp}
  → NO: "segnale da monitorare" in state, nessun pattern scritto nel namespace
  → se pattern con evidenza forte (n_run ≥3): scrive anche in wiki/log.md (wiki-first)
  → stato ciclo: "distillazione_completata"

        │
        ▼
[PASSO 4 — REVISIONE MIRATA]
  AN-LEAD → COPY-MASTER (L2.1):
  → richiesta revisione SOLO sulla sezione diagnosticata (regola anti-deriva)
  → non riscrittura totale di un copy che performa parzialmente
  → contratto revisione: {copy_id, sezione_da_rivedere, diagnosi, pattern_applicabili}
  → COPY-MASTER produce la variante revised con nuovi pattern ReasoningBank
  → stato ciclo: "variante_prodotta"

        │
        ▼
[PASSO 5 — TEST]
  AN3: disegna il test A/B (vecchia variante vs nuova variante sulla sezione rivista)
  → calcola campione minimo PRIMA del lancio
  → fissa criterio di verdetto predefinito (non modificabile post-lancio)
  → test lanciato da AD3 (L2.2) o dal sistema email per campagne email
  → attesa campione → verdetto: PASS (winner identificato) o INCONCLUSIVO
  → stato ciclo: "test_completato"

        │
        ▼
[PASSO 6 — CONSOLIDA]
  AN4: winner → aggiorna pattern in ReasoningBank con nuova evidenza (n_run aumenta)
  AN-LEAD: chiude il ciclo → state.json finale → memory_store ciclo
  wiki/log.md: entry del ciclo completato (cosa appreso, copy_id coinvolti, ICP)
  → stato ciclo: "consolidato"
  → ricomincia da [PASSO 1] sulla prossima campagna attiva (loop continuo)
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Diagnosi con dati | La diagnosi di sezione ha almeno una metrica esplicita (non opinione) | AN2 | Passaggio al passo 3 |
| G2 — Anti-rumore | ≥2 run indipendenti per la stessa osservazione prima della distillazione | AN4 | Scrittura pattern nel namespace |
| G3 — Campione pre-test | Dimensione campione calcolata e verificata da AN3 prima del lancio test | AN3 | Avvio test A/B |
| G4 — Verdetto valido | p-value soddisfa criterio predefinito O campione raggiunto con criterio met | AN3 | Consolidamento come pattern |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "ciclo_id": "LOOP-001",
  "campagna_id": "CAMP-001",
  "copy_ids": ["CP-001", "CP-002"],
  "icp": "freelance-digitale-ita",
  "kpi_sotto_target": {"CTR": 0.009, "target": 0.025},
  "trigger_source": "AN-OBSERVER"
}
```

**Output finale:**
```json
{
  "ciclo_id": "LOOP-001",
  "stato": "consolidato",
  "diagnosi": "sezione A debole su CP-001 — hook su problema non efficace per ICP freelance-digitale-ita",
  "pattern_distillato": "marketing/copy/patterns/freelance-digitale-ita — hook benefit numerico",
  "antipattern_distillato": "marketing/copy/antipatterns/freelance-digitale-ita — hook problema",
  "test_id": "EXP-001",
  "verdetto": "B winner (hook benefit) — CTR 2.8% vs 0.9%",
  "copy_revisionato": "CP-001-revised con hook benefit",
  "wiki_aggiornata": true,
  "durata_ciclo_giorni": 12
}
```

---

## State

File: `marketing/analytics/optimization-loops/{ciclo_id}/state.json`
- Aggiornato dopo ogni passo con timestamp e output del passo.
- Ripartibile a freddo: se il ciclo viene interrotto, si riprende dall'ultimo passo completato.
- `stato` possibili: raccolta_aperta | raccolta_completata | diagnosi_completata |
  distillazione_completata | variante_prodotta | test_completato | consolidato | inconclusivo

---

## Connessioni

- [[an-lead]] · `agenti/an-lead.md`
- [[an2-attribution-analyst]] · `agenti/an2-attribution-analyst.md`
- [[an4-insight-distiller]] · `agenti/an4-insight-distiller.md`
- [[WF-AB-TEST]] · `workflow/WF-AB-TEST.md` — passo 5 del loop
- [[WF-TRACKING-SETUP]] · `workflow/WF-TRACKING-SETUP.md` — prerequisito: dati devono esistere
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §4b`
