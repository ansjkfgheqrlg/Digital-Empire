---
Type: TOOL
Status: Active
Tags: #skill #account-management #churn #upsell #retention #revops #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# SKILLS — A7 Account Management & Customer Success

> **ADR-003 — wrap, mai riscrivere.** Le 4 skill primarie di A7 (`churn-prevention`, `support-90`,
> `upsell-mapper`, `revops`) **esistono già** nell'impero. A7 le mappa e le invoca. Nessun motore
> viene riscritto. L'unica skill nuova prevista è `account-health-monitor` (P2), che è essa stessa
> un wrapper di aggregazione su `churn-prevention`.

---

## `churn-prevention` — esistente, mappata

**Chi la usa:** AG-A7-HEALTH (motore principale) · AG-A7-COORD (scelta azione correttiva) ·
AG-A7-MID (lettura attrito precoce) · AG-A7-CLOSE (lettura detrattori NPS ≤6)

**Input:**
```json
{
  "client_id": "...",
  "segnali": {
    "ticket_aperti": 3,
    "ticket_in_ritardo": 1,
    "giorni_da_ultimo_contatto": 7,
    "milestone_in_ritardo": 1,
    "nps_intermedio": "0-10 | [DM]"
  },
  "storico_alert": ["alert precedenti e loro esito"]
}
```

**Output:**
```json
{
  "rischio": "basso | medio | alto",
  "segnali_oltre_soglia": [{"segnale": "...", "valore": 3, "soglia": 2}],
  "azioni_suggerite": ["check_call", "escalation_A4", "coinvolgimento_Max"],
  "confidenza": "alta | media | bassa | [DM] se segnali insufficienti"
}
```

---

## `support-90` — esistente, mappata

**Chi la usa:** AG-A7-COORD (playbook del supporto 90gg) · AG-A7-ONBOARD (prima settimana) ·
AG-A7-MID (touchpoint di metà percorso) · AG-A7-COMM (tono e template) · AG-A7-CLOSE (chiusura)

**Input:**
```json
{
  "client_id": "...",
  "fase": "kickoff | mid | supporto | chiusura",
  "contratto": {"tipo": "sprint | retainer", "durata_supporto_gg": 90},
  "milestone": [{"nome": "...", "stato": "..."}]
}
```

**Output:**
```json
{
  "cadenza_touchpoint": "settimanale | bisettimanale",
  "azioni_di_fase": ["cosa fare in questa fase"],
  "cosa_non_promettere": ["date non confermate da A4", "risultati non misurati"],
  "escalation_path": "AG-A7-COORD → AG-DIR → Max"
}
```

---

## `upsell-mapper` — esistente, mappata

**Chi la usa:** AG-A7-CLOSE (motore principale a G+90) · AG-A7-MID (qualifica dei delta di scope) ·
AG-A7-COORD (lettura prima dell'handoff ad A3-Preventivi)

**Input:**
```json
{
  "client_id": "...",
  "nps": "0-10 (mai [DM]: senza NPS non si mappa upsell)",
  "delta_scope_registrati": ["richieste fuori scope emerse nel ciclo"],
  "feedback_qualitativo": {"cosa_ha_funzionato": "...", "cosa_no": "..."},
  "contratto_originale": {"tipo": "sprint", "scope": "..."}
}
```

**Output:**
```json
{
  "opportunita": [
    {"tipo": "upsell_sprint | retainer | cross_sell_corso", "destinazione": "A3-Preventivi | 02-INFO-BUSINESS", "razionale": "...", "priorita": "alta | media"}
  ],
  "referral_proponibile": "true solo se nps >= 8",
  "consenso_case_study": "richiesto | confermato | negato"
}
```

---

## `revops` — esistente, mappata (ausiliaria)

**Chi la usa:** AG-A7-QA (coerenza economica del ciclo, retention/expansion metrics) ·
AG-A7-HEALTH (trend aggregato) · AG-A7-CLOSE (qualifica economica dell'opportunità)

**Input:**
```json
{
  "periodo": "YYYY-MM",
  "clienti": [{"client_id": "...", "esito_ciclo": "...", "upsell_referral": "..."}]
}
```

**Output:**
```json
{
  "retention_rate": "0-1 | [DM]",
  "expansion_signals": [{"client_id": "...", "tipo": "retainer"}],
  "churn_rate": "0-1 | [DM]",
  "note": "ogni metrica non calcolabile dallo state vale [DM], mai zero"
}
```

---

## `account-health-monitor` — P2, da costruire

**Chi la userà:** AG-A7-HEALTH. Wrapper di aggregazione: raccoglie i 3 gruppi di segnali (milestone,
SLA ticket da A4, reattività/clima), invoca `churn-prevention` e produce lo score unico + il trend.

**Input:**
```json
{
  "client_id": "...",
  "fonti": ["agency/a7/clients", "agency/a4/sla", "agency/a7/touchpoints"],
  "finestra": "settimanale"
}
```

**Output:**
```json
{
  "health_score": "verde | giallo | rosso | [DM]",
  "trend": "in_miglioramento | stabile | in_peggioramento | [DM]",
  "alert_da_alzare": [{"alert_id": "...", "priorita": "alta"}],
  "timestamp": "ISO-8601"
}
```

**Vincolo di costruzione:** non reimplementa le soglie di `churn-prevention` — le **legge**. Se i
segnali di input mancano, restituisce `[DM]`, mai uno score fabbricato (P5, R5).

---

## Connessioni

- [[ag-a7-health]] · `agenti/ag-a7-health.md` — utente di `churn-prevention` e `account-health-monitor`
- [[ag-a7-close]] · `agenti/ag-a7-close.md` — utente di `upsell-mapper`
- [[PRINCIPI]] · `principi/PRINCIPI.md` — P5 vincola l'output di ogni skill: `[DM]` mai zero
- [[A3-Preventivi]] · `../A3-Preventivi/` — destinatario dell'output di `upsell-mapper`
