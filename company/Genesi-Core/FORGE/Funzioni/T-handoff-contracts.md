# T-handoff-contracts — Funzione L4: Contratti di Handoff

> **Ecosistema:** Genesi-Core / FORGE · **Reparto:** AGENT-WORKS (L2.2) · **Workflow:** WF-TEAM-NEW · WF-ECOSYSTEM-NEW
> **Schema canonico di riferimento:** `Schema-Team` / `Schema-Ecosistema` (ARCHITETTURA) — la forma arriva da lì
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]] · [[Motori/Mappa-Motori.md]]

---

## Missione
Definire i **contratti di handoff** tra i componenti di un team o ecosistema che la FORGE costruisce:
schema JSON validato con `acceptance_criteria` misurabili. Un handoff senza acceptance criteria è
INVALIDO — il coordinator lo rifiuta automaticamente. ARCHITETTURA disegna *quali* handoff servono
(struttura); T-handoff-contracts li riempie col contenuto reale (payload, criteri).

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
  "payload": { "task": "", "files": [], "brand_kit": "DE | <cliente>", "icp": "" },
  "acceptance_criteria": ["criterio 1 misurabile", "criterio 2 misurabile"],
  "status": "pending | accepted | in_progress | done | rejected | escalated"
}
```

---

## Responsabilità
- Definire il contratto INTRA-TEAM (coordinator → worker, worker → worker).
- Definire il contratto INTER-TEAM (team → ecosistema esterno).
- Verificare che ogni acceptance criteria sia misurabile (non "buono", ma "≤150 parole" o "APSOC completo").
- Produrre `contracts/HC-template.json` per ogni team nuovo.
- Aggiornare `company/Backbone/Bus/contracts/` coi nuovi contratti.

---

## Regole operative (dal dossier Backbone §1.1)
1. **Handoff senza acceptance_criteria misurabili = INVALIDO** — il coordinator lo rifiuta.
2. **status=rejected DEVE includere note correttive** — senza note il reject è invalido.
3. **2 reject consecutivi** → `type: escalation` automatica al reparto superiore via gbus.
4. **brand_kit obbligatorio** — pattern #11 multi-tenant: ogni handoff dichiara per chi è il lavoro.

---

## Handoff INTRA vs INTER
| Tipo | Path bus | Quando |
|---|---|---|
| INTRA | `company/runtime/bus/<eco>/messages.jsonl` | passaggio interno al team (coordinator ↔ worker) |
| INTER | `company/runtime/group-bus/messages.jsonl` + `handoffs/` | passaggio tra ecosistemi diversi |

Deliverable multi-file → file in `company/Ecosistemi/<ECO>/handoffs/{inbox,outbox,archive}/H-<id>.json`;
il jsonl trasporta solo il riferimento.

## Esempio Genesi Core: `HC-ARCH-FORGE`
ARCHITETTURA → FORGE: `from=Genesi-Core/ARCHITETTURA/WF-ARCH-DESIGN`, `to=Genesi-Core/FORGE/WF-FORGE-PIPELINE`,
payload `{blueprint, schema, struttura}`, acceptance `["blueprint validato da struct-gate", "schema canonico rispettato"]`.

## KPI
| Metrica | Target |
|---|---|
| Handoff invalidi (senza acceptance criteria) | 0% |
| Reject senza note correttive | 0 |
| Escalation automatiche → risolte ≤24h | 100% |
| Team senza HC-template dopo WF-TEAM-NEW | 0 |
