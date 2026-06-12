# ✅ Quality Guild — Guild

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 4.2
> **Expertise:** QA gate, acceptance criteria, contradiction-analyzer, rubriche di valutazione, "definizione di done"
> **Serve:** tutti gli ecosistemi — ogni delivery passa dal Quality Gate prima di uscire
> **Sponsor C-level:** CTO (empire-cto)
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/Governance/README.md]]

---

## Identità

| Campo | Valore |
|---|---|
| **Guild Master** | `quality-guild-master` (L5 coordinator, namespace AgentDB: `patterns/quality/`) |
| **Tipo** | Guild trasversale — expertise su richiesta, non gerarchia verticale |
| **Deliverable principale** | Rubriche di valutazione per verify.sh cat.3 + benchmark interni |
| **Ingaggio** | Passivo (`memory_search "acceptance criteria"`) o attivo (guild_request) |

---

## Cosa standardizza

### 1. Acceptance Criteria standard (invariante del Pattern #2)

Ogni handoff contract deve avere acceptance criteria misurabili. La Quality Guild definisce e mantiene i template:

| Tipo deliverable | Acceptance criteria standard |
|---|---|
| Cold email | ≤ 200 parole · APSOC score ≥ 80 · una sola CTA · zero claim senza proof |
| Sales page | APSOC ≥ 85 · ≥ 3 obiezioni · CPB su ogni claim principale · pricing corretto |
| Codice workflow | dry-run funzionante · zero segreti in file tracciati · acceptance test documentato |
| Documento ADR | contesto + decisione + conseguenze + data + contradiction-check passato |
| Handoff contract | da, a, payload, acceptance_criteria (≥1), status — tutti i campi presenti |
| Skill/agente nuovo | system prompt conforme standard Prompt Guild · eval gate superato · assegnato a reparto |
| Contenuto social | hook nei primi 3 righi · brand_kit dichiarato · nessun claim non verificabile |

Un handoff senza acceptance criteria misurabili è INVALIDO — il coordinator lo rifiuta automaticamente (Pattern #2).

### 2. Rubriche di valutazione (fornite a verify.sh categoria 3)

La Guild mantiene le rubriche usate dal Quality Sentinel e da verify.sh per valutare i deliverable:
- **Rubrica copy** (per APSOC audit): punteggio per sezione (A, P, S, O, C), criteri pass/fail, note correttive standard
- **Rubrica codice** (per sistemi): dry-run ✓, zero segreti ✓, test documentato ✓, wrap non riscrittura ✓
- **Rubrica documenti normativi**: contradiction-check ✓, ADR se architetturale ✓, checkpoint Memory ✓

### 3. Definizione di "Done" per tipo di deliverable

La Guild standardizza la definizione di Done (DoD) per ogni tipo:
- **Copy done** = APSOC gate G1 ≥ 80 + Brand gate G2 pass + revisione umana (F1-F7) + checkpoint Memory
- **Workflow done** = dry-run testato + acceptance test documentato + handoff firmato + checkpoint Memory
- **Ecosistema done** (chiusura fase) = verify-empire verde (tutte e 5 le categorie) + STATO-EMPIRE aggiornato
- **Skill done** = prompt conforme + eval gate superato + skill assegnata a reparto in skills-map.yaml

### 4. Testing e contradiction-check

- **contradiction-analyzer** (skill installata): ogni nuova skill, SOP o documento normativo passa il check contro ADR attivi e Mandato prima del merge
- **Benchmark interni**: la Guild mantiene un set di test cases rappresentativi per tipo di deliverable — usati per misurare prima/dopo le revisioni
- **Regression check**: quando un gate viene modificato (soglie, categorie), la Guild verifica che i test cases precedentemente approvati continuino a passare

---

## Deliverable

- **Rubriche di valutazione** — per ogni tipo di deliverable, versionatee, usate da verify.sh e Quality Sentinel
- **Benchmark test cases** — set di esempi pass/fail per ogni rubrica
- **DoD registry** — definizioni di Done per tipo, aggiornate a ogni evoluzione dei gate
- **Acceptance criteria template** — per tipo di handoff, pronti da copiare nei contratti HC

---

## Come si richiede supporto alla Guild

```json
{
  "from": "<ecosistema_richiedente>",
  "to": "Quality-Guild",
  "tipo": "guild_request",
  "sottotipo": "rubrica_request | dod_clarification | acceptance_criteria_template | contradiction_check",
  "brief": "necessito acceptance criteria per handoff AGENCY→MARKETING su preventivo",
  "deliverable_type": "preventivo",
  "contesto": "...",
  "formato_atteso": "lista acceptance criteria numerata, misurabili",
  "deadline": "YYYY-MM-DD"
}
```

---

## KPI

| Metrica | Target |
|---|---|
| Handoff con acceptance criteria conformi allo standard | 100% (obiettivo F3) |
| Rubriche disponibili per tipo di deliverable principale | ≥ 5 (F3) |
| Gate bypassati (per definizione) | 0 |
| Pass-rate verify.sh al primo colpo | ≥ 90% (KPI Backbone) |
| Test cases nel benchmark per rubrica | ≥ 5 (pass + fail) |

---

## Stato

Struttura creata (F1). Agenti L5 da assegnare in F3 (migrazione asset + registro Identity-HR).
Guild Master disponibile in consultazione manuale (F1-F3): usa skill `verification-quality` e `contradiction-analyzer` per QA immediato.
