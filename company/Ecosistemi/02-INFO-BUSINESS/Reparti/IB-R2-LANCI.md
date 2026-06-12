> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.2 (Reparti L2)

# IB-R2-LANCI — Reparto Lanci

> Reparto L2 · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Orchestrare ogni lancio come operazione militare a calendario: pre-lancio, cart open,
cart close, post-lancio. **Un lancio = un workflow con dry-run obbligatorio e go/no-go
formale.** Il regista del cart open: niente improvvisazione, niente scarcity falsa.

---

## Workflow L3

| Workflow | Descrizione |
|---|---|
| `WF-LANCIO` | Lancio completo orchestrato: calendario T-30→T+7, gate, dry-run, go/no-go (dettaglio §4b) |
| `WF-WEBINAR` | Webinar di vendita: script (da `InfoBusiness/Webinar/`), registrazione/live, replay funnel |

---

## Team L4 (Funzioni)

| Team | Responsabilità |
|---|---|
| `T-calendario` | Timeline T-30→T+7, dipendenze, owner per task |
| `T-copy-liaison` | Compone handoff verso MARKETING, verifica rientri vs APSOC ≥80 |
| `T-asset-lancio` | Checklist asset completi (sales page, email, creatives, checkout) prima del gate |
| `T-debrief` | Post-mortem strutturato → ReasoningBank (namespace `infobusiness/reasoningbank`) |

---

## Agenti L5 (roster)

`ib-lanci-coordinator` (Opus durante il lancio), `ib-launch-planner`, `ib-copy-liaison`,
`ib-webinar-producer`, `ib-debriefer`

---

## Flusso WF-LANCIO (sintesi)

```
PRE-LANCIO (T-30 → T-1)
  T-30  ib-launch-planner: calendario + dipendenze + owner
  T-14  HANDOFF → MARKETING: sales page + sequenza pre-lancio [GATE: APSOC ≥80]
  T-1   DRY-RUN completo → Cost-Sentinel
  T-0-ε GO/NO-GO: hive-mind consensus (ib-conductor + Sentinels)
CART OPEN (T0 → T+4/6)
  ib-tracking-analyst riporta conversioni ogni 24h
CART CLOSE — scarcity REALE obbligatoria (Mandato Empire)
POST (T+1 → T+7) — onboarding + debrief + crosssell scout
```

---

## KPI

| KPI | Definizione |
|---|---|
| Aderenza calendario | % task lancio completati entro la data pianificata |
| Conversione lancio | % lista email → acquisto durante cart open |

---

## Quality Gates bloccanti

- **Gate copy lancio APSOC**: ogni copy a conversione → audit ≥80/100 (≥85 per sales page)
- **Gate dry-run + costi**: T-1, simulazione completa OK + budget approvato da Cost-Sentinel
- **Gate go/no-go**: hive-mind consensus unanime dei Sentinels (Brand-Voice + Cost hanno potere di NO)

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS]] sez. 2.2 + 4b (WF-LANCIO)
- [[04-ECOSISTEMA-MARKETING]] — fornitore copy lancio (email, sales page, APSOC gate)
- [[IB-R3-VENDITE-FUNNEL]] — infrastruttura vendita su cui si appoggia il lancio
- [[IB-R4-COMMUNITY-RETENTION]] — riceve acquirenti post-cart close
