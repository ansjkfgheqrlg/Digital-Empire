> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 1.1 Bus · 06-ECOSISTEMI-CORE.md sez. 07 L4

# T-handoff-contracts — Funzione L4: Contratti di Handoff

**Ecosistema:** 07-FORGE · **Reparto:** AGENT-WORKS (L2.2) · **Workflow:** WF-TEAM-NEW · WF-ECOSYSTEM-NEW

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Definire i **contratti di handoff** tra i componenti di un team o ecosistema: schema JSON
validato con `acceptance_criteria` misurabili. Un handoff senza acceptance criteria è
INVALIDO — il coordinator lo rifiuta automaticamente.

---

## Schema handoff contract standard (HC-v1 — vincolante)

```json
{
  "id": "H-YYYYMMDD-NNNN",
  "ts": "ISO 8601",
  "scope": "intra | inter",
  "from": "ECO/Reparto/WF-nome",
  "to": "ECO/Reparto/T-nome",
  "priority": "CRITICAL | HIGH | NORMAL | LOW",
  "type": "directive | handoff | result | escalation",
  "payload": {
    "task": "descrizione del task",
    "files": ["path/file1", "path/file2"],
    "brand_kit": "DE | <cliente>",
    "icp": "riferimento ICP attivo"
  },
  "acceptance_criteria": [
    "criterio 1 misurabile",
    "criterio 2 misurabile"
  ],
  "status": "pending | accepted | in_progress | done | rejected | escalated"
}
```

---

## Responsabilità di T-handoff-contracts

- Definire il contratto INTRA-TEAM (coordinator → worker e worker → worker)
- Definire il contratto INTER-TEAM (team verso ecosistema esterno)
- Verificare che ogni acceptance criteria sia misurabile (non "buono", ma "≤150 parole" o "APSOC completo")
- Produrre il `contracts/HC-template.json` per ogni team nuovo
- Aggiornare `company/Backbone/Bus/contracts/` con i nuovi contratti

---

## Regole operative (dal dossier Backbone §1.1)

1. **Un handoff senza acceptance_criteria misurabili è INVALIDO** — il coordinator lo rifiuta
2. **status=rejected DEVE includere note correttive** — senza note il reject è invalido
3. **2 reject consecutivi** → `type: escalation` automatica al reparto superiore via gbus
4. **brand_kit obbligatorio** — pattern #11 multi-tenant: ogni handoff dichiara per chi è il lavoro

---

## Handoff INTRA vs INTER

| Tipo | Path bus | Quando |
|---|---|---|
| INTRA | `company/runtime/bus/<eco>/messages.jsonl` | passaggio interno al team (coordinator ↔ worker) |
| INTER | `company/runtime/group-bus/messages.jsonl` + `handoffs/` | passaggio tra ecosistemi diversi |

I deliverable multi-file (copy, video, report) viaggiano come file in
`company/Ecosistemi/<ECO>/handoffs/{inbox,outbox,archive}/H-<id>.json`;
il jsonl trasporta solo il riferimento.

---

## KPI

| Metrica | Target |
|---|---|
| Handoff invalidi (senza acceptance criteria) | 0% |
| Reject senza note correttive | 0 |
| Escalation automatiche (2 reject consecutivi) → risolte ≤24h | 100% |
| Team senza HC-template definito | 0 dopo WF-TEAM-NEW |
