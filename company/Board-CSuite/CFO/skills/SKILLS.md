---
Type: CONCEPT
Status: Active
Tags: #cfo #skills #budget-guard #cost-ledger #tier-router
Created: 2026-06-18
Last updated: 2026-06-18
---

# SKILLS — Skill Proprie della Figura CFO

> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CFO.md` §"Skill proprie"
> Connessioni: [[WF-BUDGET]] · [[WF-COST-REPORT]] · [[cfo-budget-guard]]

---

## Skill 1: `budget-guard`

### Scopo
Blocca una run PRIMA che superi il budget dichiarato per il suo workflow/ecosistema. È il cuore
del cost guard: nessuna spesa parte se la stima la porta oltre l'envelope. Predica il pattern #9
(blocco pre-sforo) e #3 (dry-run di default).

### Come funziona
Riceve la richiesta di run con la stima di costo (da dry-run) + l'envelope corrente dell'ecosistema.
Confronta stima vs residuo. Se la stima sta dentro → approva con riserva (decrementa l'envelope).
Se la porterebbe oltre → BLOCCA e restituisce il delta mancante. Mai "approva e vediamo".

### Input
```json
{
  "workflow": "WF-SITE-FULL",
  "ecosistema": "06-PLATFORM",
  "stima_costo": {"valore": 120, "unita": "crediti", "fonte": "dry-run"},
  "envelope_residuo": 300
}
```

### Output
```json
{
  "esito": "approvato | bloccato_pre_sforo",
  "envelope_dopo": 180,
  "delta_mancante": 0,
  "richiede_ok_umano": false,
  "timestamp": "ISO8601"
}
```

### Regole interne
- Senza stima dry-run → BLOCCA (non si approva al buio, pattern #3).
- Spesa API/crediti REALE → sempre `richiede_ok_umano = true` (passa a `cfo-spend-approver`).
- L'envelope decrementa atomico all'approvazione; nessun decremento retroattivo.
- Sforo registrato come anomalia (KPI 1) → post-mortem.

---

## Skill 2: `cost-ledger`

### Scopo
Registra ogni evento di costo della holding (chi/cosa/quanto/per quale commessa) e produce i
report di attribuzione. È la fonte di verità dei costi: una run senza evento ledger è invalida (G-ATTRIBUTION).

### Come funziona
Riceve un evento di costo a fine run (da qualsiasi ecosistema/OPERATIONS), lo normalizza (agente,
run_id, commessa, ecosistema, tier, costo, durata, esito), lo appende al ledger del giorno (append-only),
aggiorna gli aggregati per ecosistema. Su richiesta produce il report periodico.

### Input
```json
{
  "modalita": "registra | report",
  "evento": {
    "run_id": "RUN-20260618-014", "ecosistema": "01-AGENCY", "agente": "outreach-writer",
    "tier": "haiku", "costo": 8, "durata_s": 42, "commessa": "cliente-X", "esito": "ok"
  },
  "periodo_report": "2026-06-12/2026-06-18"
}
```

### Output
```json
{
  "registrato": true,
  "ledger_path": "state/ledger/eventi_20260618.json",
  "aggregato_ecosistema": {"01-AGENCY": 142, "06-PLATFORM": 310},
  "copertura": "98.5%",
  "nota": "2 run senza evento (flaggate per OPERATIONS)"
}
```

### Regole interne
- Append-only: gli eventi non si modificano né cancellano, solo si archiviano.
- Ogni evento cita la fonte (run_id reale); nessun costo stimato nel ledger consuntivo.
- Copertura < 98% → alert a `cfo-cost-sentinel` (KPI 2 a rischio).

---

## Skill 3: `tier-router`

### Scopo
Decide il tier modello giusto per ogni task (WASM / Haiku / Sonnet-Opus) secondo complessità e
criticità, per minimizzare il costo senza degradare la qualità. Enforcement del 3-tier routing.

### Come funziona
Riceve il task con i suoi attributi (tipo, criticità, deterministico?, volume). Applica la matrice:
deterministico/ripetitivo → WASM/Haiku; ragionamento standard → Sonnet; giudizio critico/raro → Opus.
Registra la decisione per il KPI 3 (quota tier economico).

### Input
```json
{
  "task": "normalizza 500 record lead",
  "attributi": {"deterministico": true, "criticita": "bassa", "volume": "alto", "richiede_giudizio": false}
}
```

### Output
```json
{
  "tier_scelto": "haiku",
  "motivo": "deterministico + alto volume + no giudizio → tier economico",
  "alternativa_scartata": "sonnet (costo non giustificato)",
  "registrato_in": "state/tier-decisions/20260618.json"
}
```

### Regole interne
- Default al tier più economico che regge il task; si sale solo con motivo esplicito.
- Giudizio critico/standard-azienda (es. review MAXIMILIAN) → mai sotto Opus/Sonnet.
- Thompson Sampling (via Ruflo, quando attivo) per affinare la matrice sui dati reali.

---

## Connessioni

- [[cfo-budget-guard]] · `agenti/cfo-budget-guard.md`
- [[cfo-cost-accountant]] · `agenti/cfo-cost-accountant.md`
- [[cfo-tier-router]] · `agenti/cfo-tier-router.md`
- [[WF-BUDGET]] · `workflow/WF-BUDGET.md`
- [[STATE]] · `state/README.md`
