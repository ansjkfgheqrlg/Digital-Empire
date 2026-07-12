---
Type: TOOL
Status: Active
Tags: #state #agentdb #namespace #account-management #memoria #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# state — Namespace AgentDB `agency/a7`

> Namespace radice del reparto: **`agency/a7`** (alias esteso in `ARCHITETTURA.md §4`:
> `agency/07-account`). Le due forme indicano lo stesso spazio: `a7` è la chiave AgentDB,
> `07-account` la sua etichetta leggibile nel dossier.
>
> **Lo state è la memoria del reparto.** Un cliente, una relazione, un rischio esistono solo se
> sono scritti qui. Ciò che non è nello state non è avvenuto (R3).

---

## Tabella chiavi

| Chiave | Tipo | Owner (scrittura) | Chi legge | Contenuto |
|---|---|---|---|---|
| `agency/a7/clients/{client_id}` | record | **AG-A7-COORD** | tutto A7 · 08-INTELLIGENCE (aggregato) | Anagrafica, `kam`, fase ciclo, milestone, `nps`, esito upsell/referral |
| `agency/a7/health/{client_id}` | dashboard | **AG-A7-HEALTH** | AG-A7-COORD · MID · CLOSE · QA | Score salute, segnali attivi, soglie superate, trend, timestamp |
| `agency/a7/alerts/{alert_id}` | record | **AG-A7-COORD** (propone AG-A7-HEALTH · chiude AG-A7-QA) | tutto A7 · AG-DIR | Segnale churn, timestamp, azione correttiva, esito, stato |
| `agency/a7/touchpoints/{client_id}` | log append-only | **AG-A7-COMM** (scrivono anche ONBOARD/MID/CLOSE per i propri touchpoint) | tutto A7 | Log: tipo touchpoint, data, contenuto draft, esito invio |
| `agency/a7/gates/{client_id}` | log append-only | **AG-A7-QA** | AG-A7-COORD · AG-DIR | Esito di ogni gate: check, evidenze, PASS/FAIL, timestamp · snapshot KPI |
| `agency/a4/sla/{client_id}` | record **esterno** | **A4-Delivery** | A7 in **sola lettura** | Ticket aperti, in ritardo, % chiusi entro SLA |
| `agency/a3/contratti/{client_id}` | record **esterno** | **A3-Preventivi** | A7 in **sola lettura** | Scope venduto, tipo contratto, durata supporto |

**Confine di scrittura:** A7 **non scrive mai** in `agency/a4/*` né in `agency/a3/*`. Il dato SLA è
prodotto da A4 e letto da A7 (P2). Violare questo confine crea due verità sullo stesso ticket.

---

## Schema file system

```
agency/a7/
├── clients/
│   └── {client_id}/
│       └── state.json          # record cliente — owner AG-A7-COORD
├── health/
│   └── {client_id}/
│       └── dashboard.json      # score + segnali — owner AG-A7-HEALTH
├── alerts/
│   └── {alert_id}.json         # ALRT-{client_id}-NNN — owner AG-A7-COORD
├── touchpoints/
│   └── {client_id}/
│       └── log.jsonl           # append-only — owner AG-A7-COMM
└── gates/
    ├── {client_id}/
    │   └── gates.jsonl         # append-only — owner AG-A7-QA
    └── kpi-{YYYY-MM}.json      # snapshot KPI mensile — owner AG-A7-QA
```

### `clients/{client_id}/state.json`

```json
{
  "client_id": "string — identificativo univoco",
  "kam": "AG-A7-COORD — OBBLIGATORIO, mai vuoto (R1)",
  "fase_ciclo": "onboarding | delivery | supporto | closure | chiuso",
  "contatto": {"nome": "string", "ruolo": "string"},
  "milestone": [{"nome": "string", "attesa": "YYYY-MM-DD", "stato": "loggata | comunicata | completata"}],
  "nps": "0-10 | [DM]",
  "nps_data_raccolta": "YYYY-MM-DD | null",
  "alert_aperti": ["alert_id"],
  "upsell_referral": {"a3": "none | emesso", "a6": "none | emesso", "info": "none | emesso"},
  "esito_ciclo": "chiuso_con_upsell | chiuso_pulito | chiuso_con_riserva | null",
  "last_updated": "ISO-8601"
}
```

**Nessun recapito.** Nessuna email, nessun telefono, nessun dato di pagamento, nessuna credenziale.
Solo `nome` e `ruolo` del contatto (R7). I recapiti vivono nel **CRM**.

---

## Lifecycle stati

### Cliente — `fase_ciclo`

```
[A4-Delivery: cliente live]
        ▼
   onboarding ──(gate QA: kam + milestone comunicate + touchpoint loggato)──▶ delivery
        │
   delivery ──(gate QA: mid-review loggata + delta scope instradati)──▶ supporto
        │
   supporto ──(G+90 raggiunto)──▶ closure
        │
   closure ──(gate QA: NPS raccolto + milestone complete + kam continuo)──▶ chiuso
        │
        └─ FAIL su NPS dopo 2 follow-up ──▶ chiuso_con_riserva (nps: [DM]) + escalation AG-DIR
```

Nessuna transizione avviene senza **PASS di AG-A7-QA**. Il gate non si bypassa (R8).

### Alert — `stato`

```
aperto ──(azione correttiva registrata entro 24h)──▶ in_lavorazione
   │                                                        │
   │ (>24h senza azione)                          (segnale rientrato, verificato da QA)
   ▼                                                        ▼
scaduto → escalation AG-DIR                              chiuso
   (resta APERTO: non si chiude per decorrenza)
```

Un alert **non si autochiude**. Lo chiude AG-A7-QA solo dopo aver verificato che il segnale è
rientrato (R2). La decorrenza dei termini produce escalation, non chiusura.

---

## Regole di accesso

1. **Owner unico per chiave.** Ogni chiave ha **un solo** owner di scrittura (tabella sopra). Gli
   altri agenti leggono. Chi non è owner e vuole modificare un dato lo **propone** all'owner.
2. **Sola lettura sui namespace esterni.** `agency/a4/*` e `agency/a3/*` sono read-only per A7 (P2).
3. **`kam` obbligatorio.** Nessun record in `clients/` può esistere senza `kam` popolato. Un cliente
   orfano è un'anomalia bloccante che ferma ogni altra azione (R1).
4. **Append-only sui log.** `touchpoints/` e `gates/` non si riscrivono: si appendono. La storia
   della relazione non è editabile a posteriori.
5. **`[DM]`, mai zero.** Un dato non misurato vale `[DM]`. Scrivere `0`, una media o una stima al
   posto di un dato mancante è una violazione bloccante (P5, R5).
6. **Nessun PII, nessun segreto.** Solo `nome` e `ruolo`. Nessuna API key, token o credenziale (R7).
   Lo state è versionato in git: un PII nello state è un PII pubblicato.
7. **Ripartibilità a freddo.** Lo state deve bastare a un KAM che rientra dopo un'amnesia di sessione
   per riprendere la relazione dal punto esatto, senza ricostruire il contesto (ARCHITETTURA §6).
8. **Lint pre-commit.** `scripts/state_lint.py --strict` valida R1, R3, R5, R7 su tutto `agency/a7/*`.
   Return code `2` = violazione bloccante → il commit **non passa**.

---

## Connessioni

- [[ag-a7-coord]] · `agenti/ag-a7-coord.md` — owner di `clients/` e `alerts/`
- [[ag-a7-qa]] · `agenti/ag-a7-qa.md` — owner di `gates/`, unico a chiudere gli alert
- [[REGOLE]] · `regole/REGOLE.md` — R1, R3, R5, R7 sono invarianti dello state
- [[A4-Delivery]] · `../A4-Delivery/` — owner di `agency/a4/sla` (read-only per A7)
