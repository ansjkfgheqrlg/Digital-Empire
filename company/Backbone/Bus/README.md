# 📡 BUS — Message Bus a 2 livelli

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 1.1
> **Backbone component.** Sistema nervoso di EMPIRE OS: ogni passaggio di lavoro tra agenti,
> team, reparti ed ecosistemi è un messaggio tracciato e append-only.
> Ispirato a `gbus.sh` di AION GROUP, esteso al multi-tenant con 10 ecosistemi e `brand_kit`.
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/README.md]]

---

## Architettura a 2 livelli

| Livello | Script | File di stato | Mittenti/destinatari validi |
|---|---|---|---|
| **INTRA** (dentro un ecosistema) | `company/orchestrator/bus.sh` | `company/runtime/bus/<ecosistema>/messages.jsonl` | team e reparti dello stesso ecosistema |
| **INTER** (tra ecosistemi) | `company/orchestrator/gbus.sh` | `company/runtime/group-bus/messages.jsonl` | i 10 ecosistemi + `BOARD` + `EMPIRE` (validati vs Identity-HR) |

Per i deliverable "pesanti" (payload multi-file: copy, video, report), il jsonl trasporta il riferimento e la cartella handoffs/ trasporta il contenuto:
`company/Ecosistemi/<ECO>/handoffs/{inbox,outbox,archive}/H-<id>.json`

---

## Handoff Contract standard (obbligatorio — Pattern #2)

```json
{
  "id": "H-20260611-0042",
  "ts": "2026-06-11T15:30:00Z",
  "scope": "inter | intra",
  "from": "AGENCY/Acquisizione/WF-OUTREACH-EMAIL",
  "to": "MARKETING/Copywriting/T-email-writer",
  "priority": "CRITICAL | HIGH | NORMAL | LOW",
  "type": "directive | handoff | result | escalation",
  "payload": {
    "task": "scrivi variante email outreach per vertical Ecommerce",
    "files": ["runtime/bus/agency/brief-eco-001.json"],
    "brand_kit": "DE",
    "icp": "ecommerce D2C, 10-50 dipendenti, problema: outreach manuale"
  },
  "acceptance_criteria": [
    "max 150 parole",
    "APSOC score ≥ 80/100",
    "zero claim senza proof (CPB)",
    "una sola CTA"
  ],
  "status": "pending | accepted | in_progress | done | rejected | escalated"
}
```

**Regole di validità:**
- Un handoff senza `acceptance_criteria` misurabili è INVALIDO — il coordinator lo rifiuta automaticamente
- `status: rejected` DEVE includere `note_correttive` dettagliate
- 2 reject consecutivi dallo stesso team → `type: escalation` automatica al reparto superiore via gbus
- Campo `brand_kit` obbligatorio nel payload inter-ecosistema (Pattern #11 multi-tenant)

---

## Struttura cartelle

```
Bus/
├── handoffs/        ← messaggi in transito (JSON files) — .gitkeep presente
├── fulfilled/       ← handoff completati (archivio audit)
├── rejected/        ← handoff falliti con motivo e note correttive
└── contracts/       ← template HC per ogni coppia ecosistemi
    ├── HC-template.json   ← schema base (già presente ✅)
    └── registry.yaml      ← registro contratti attivi (da creare F2)
```

Script da creare in F2 (task 2.3):
- `bus.sh` — motore INTRA (porta da CF e adatta a 10 ecosistemi)
- `gbus.sh` — motore INTER (porta da CF, aggiunge validazione Identity-HR)
- `validate-handoff.sh` — verifica schema JSON del contratto prima dell'invio

---

## 3-tier routing nel Bus

| Priorità | SLA risposta | Modello coordinator |
|---|---|---|
| `CRITICAL` | immediata (< 5 min) | Sonnet |
| `HIGH` | < 1 ora | Sonnet |
| `NORMAL` | < 4 ore | Haiku |
| `LOW` | < 24 ore | Haiku |

Il coordinator valuta la priorità del handoff e istanzia il tier modello appropriato per la gestione.

---

## Differenza vs CF Exponium

CF ha 6 ecosistemi e payload mono-brand; DE ne ha 10 + il campo `brand_kit`/`icp` obbligatorio (Pattern #11 multi-tenant). CF non ha cartelle handoffs per ecosistema (solo jsonl); DE le aggiunge per i deliverable multi-file.

---

## KPI (monitorati da Observability)

| Metrica | Target |
|---|---|
| Backlog bus (messaggi pending > 24h) | 0 |
| Handoff invalidi (senza acceptance criteria) | 0% |
| Handoff rejected senza note correttive | 0 |
| Escalation automatiche da 2 reject consecutivi | tracciate 100% |

---

## Stato: DA COSTRUIRE (F2, task 2.3)

`HC-template.json` presente ✅ · `handoffs/` cartella presente ✅
Prossimi passi: `bus.sh` + `gbus.sh` + `validate-handoff.sh` + `contracts/registry.yaml`
