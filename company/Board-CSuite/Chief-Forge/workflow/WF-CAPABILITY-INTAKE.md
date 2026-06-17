# WF-CAPABILITY-INTAKE — Richiesta Capability → Forgiatura → Registro

> Workflow CF-grade | Owner: `cf-conductor` | Figura: Chief-Forge
> Blueprint: [[BP-Chief-Forge]] | Versione: 1.0 · 2026-06-17

---

## Scopo

Trasformare una richiesta di nuova capability (skill, agente, team, workflow) proveniente da
qualsiasi ecosistema in un artefatto forgiato, valutato e registrato. È il flusso principale
di Chief-Forge: gestisce il ciclo completo intake → decisione → blueprint → build → eval → registro.

---

## Trigger

- Qualsiasi ecosistema invia una richiesta nel namespace `board/chief-forge/intake`
- Formato minimo obbligatorio: `{ecosistema_richiedente, gap_descritto, tipo_richiesta, urgenza}`
- Se urgenza = CRITICAL: il flusso si avvia entro 30min dalla ricezione

---

## Input

```json
{
  "tipo": "richiesta_capability",
  "ecosistema_richiedente": "XX-ECO",
  "gap_descritto": "...",
  "tipo_richiesta": "skill | agente | team | workflow",
  "kpi_attesi": ["..."],
  "budget_disponibile": "USD | non specificato",
  "urgenza": "CRITICAL | HIGH | NORMAL | LOW"
}
```

---

## Flusso passo-passo

```
FASE 1 — INTAKE E VALIDAZIONE
  cf-intake-router
    ├─ Valida formato (campi obbligatori presenti?)
    │     └─ Se incompleta → risposta ecosistema con lista mancanze → STOP (attende integrazione)
    ├─ Assegna CF-REQ-YYYYMMDD-NNN
    ├─ Lancia analisi parallela:
    │     ├─ cf-skill-portfolio: duplicati skill?
    │     ├─ cf-agent-registry: agenti equivalenti?
    │     └─ cf-contradiction-warden: conflitti con esistenti?
    └─ Sintetizza brief validato con raccomandazione

  [Gate G1: brief validato completo]
    PASS → Fase 2
    FAIL → Richiesta integrazione all'ecosistema; loop

FASE 2 — DECISIONE CONDUCTOR
  cf-conductor
    ├─ Consulta cf-memoria: pattern analoghi nel passato?
    ├─ Valuta urgenza vs impatto vs budget
    └─ Decide:
          ├─ REUSE → informa ecosistema con path artefatto esistente → FINE
          ├─ EXTEND → cf-forge-liaison: modifica puntuale senza blueprint → skip Fase 3 → Fase 4
          ├─ REJECT → risposta motivata all'ecosistema → FINE
          ├─ DEFER → inserisce in backlog con priorità e data revisione → FINE (per ora)
          └─ BUILD → Fase 3

  [Gate G2: decisione registrata con motivazione]

FASE 3 — BLUEPRINT (solo se BUILD)
  cf-conductor → cf-architettura-liaison
    ├─ Compila arch_request (tipo, scopo, vincoli, eval_criteria, deadline)
    ├─ Invia ad ARCHITETTURA namespace arch/intake
    ├─ Monitora: blueprint atteso entro deadline
    └─ Riceve blueprint con struct_gate

  [Gate G3: struct_gate PASS da ARCHITETTURA]
    PASS → Fase 4
    FAIL → cf-architettura-liaison richiede revisione ad ARCHITETTURA (max 1 revisione)

FASE 4 — BUILD
  cf-architettura-liaison → cf-forge-liaison
    ├─ Consegna forge_brief con blueprint_id
    ├─ cf-forge-liaison compila forge_order e invia a FORGE (frg-chief)
    ├─ FORGE esegue il workflow appropriato (WF-SKILL-NEW | WF-AGENT-NEW | WF-TEAM-NEW | ...)
    └─ Monitora avanzamento; gestisce blocchi

  [Gate G4: artefatto consegnato da FORGE con eval_report]

FASE 5 — EVAL GATE
  cf-forge-liaison → cf-eval-warden
    ├─ Riceve eval_package (artefatto + eval_report grezzo)
    ├─ Verifica pass_rate ≥ threshold (default 85%)
    └─ Decisione:
          ├─ PASS → Fase 6
          └─ FAIL ciclo 1 → invia iterate a FORGE con gap specifici → torna a Fase 4
               └─ FAIL ciclo 2 → escalation a cf-conductor → CEO se necessario

  [Gate G5: eval gate PASS]

FASE 6 — REGISTRO E CONSEGNA
  cf-eval-warden → cf-agent-registry + cf-skill-portfolio
    ├─ cf-agent-registry: REGISTRA nuovo agente (se tipo agente)
    ├─ cf-skill-portfolio: AGGIUNGI nuova skill (se tipo skill)
    ├─ cf-memoria: registra forgiatura chiusa con pattern
    └─ cf-conductor: notifica ecosistema richiedente → consegna path artefatto

  [FINE: artefatto nel registro, ecosistema notificato]
```

---

## State machine

| Stato | Descrizione | Transizione |
|---|---|---|
| `INTAKE_PENDING` | Richiesta ricevuta, validazione in corso | → `BRIEF_READY` o `INCOMPLETE` |
| `BRIEF_READY` | Brief validato, attende decisione conductor | → `DECISION_MADE` |
| `BLUEPRINT_PENDING` | Inviato ad ARCHITETTURA | → `BLUEPRINT_READY` |
| `BUILD_IN_PROGRESS` | In coda/build FORGE | → `BUILD_DELIVERED` |
| `EVAL_PENDING` | Artefatto in gate eval | → `EVAL_PASS` o `EVAL_FAIL_1` o `EVAL_FAIL_2` |
| `REGISTERED` | Artefatto nel registro, chiuso | terminale |
| `REJECTED` | Rifiutato con motivazione | terminale |
| `DEFERRED` | In backlog con data revisione | → riattiva da `INTAKE_PENDING` |

---

## KPI di flusso

| Metrica | Target |
|---|---|
| Tempo totale intake → consegna (urgenza NORMAL) | da misurare |
| Tempo intake → decisione conductor | ≤4h |
| Artefatti PASS al primo ciclo eval | da misurare |
| Richieste CRITICAL senza decisione >24h | 0 |

---

## Connessioni

- [[agenti/cf-conductor.md]] · [[agenti/cf-intake-router.md]] · [[agenti/cf-architettura-liaison.md]]
- [[agenti/cf-forge-liaison.md]] · [[agenti/cf-eval-warden.md]]
- [[agenti/cf-skill-portfolio.md]] · [[agenti/cf-agent-registry.md]] · [[agenti/cf-memoria.md]]
- [[07-FORGE/Workflow/WF-SKILL-NEW.md]] · [[07-FORGE/Workflow/WF-AGENT-NEW.md]]
- [[14-DOSSIER-ARCHITETTURA]] — per WF-ARCH-DESIGN (blueprint)
