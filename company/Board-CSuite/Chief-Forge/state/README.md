# STATE — Chief-Forge

> Schema dello state della figura Chief-Forge: namespace, struttura, campi, ciclo di vita.
> Fonte: [[BP-Chief-Forge]] · [[ARCHITETTURA.md]] §6 · [[agenti/cf-memoria.md]]

---

## Namespace principale

```
board/chief-forge/
├── intake/          ← richieste in ingresso e loro stato pipeline
├── portfolio/       ← catalogo skill vivente
├── registry/        ← Identity-HR (agenti della holding)
├── eval/            ← storico gate eval
├── arch-liaison/    ← log richieste blueprint ad ARCHITETTURA
├── forge-liaison/   ← log ordini e consegne FORGE
├── ecosystem-builder/ ← proposte e mandati ecosistemi
├── contradiction/   ← analisi contraddizioni
├── memoria/         ← storico forgiature, pattern, snapshots
│   ├── snapshots/   ← snapshot settimanali dello stato completo
│   └── archivio/    ← record >180gg senza correlazione pattern attivi
└── conductor/       ← decisioni conductor e log escalation
```

---

## Schema: richiesta in intake

```json
{
  "request_id": "CF-REQ-YYYYMMDD-NNN",
  "stato": "INTAKE_PENDING | BRIEF_READY | BLUEPRINT_PENDING | BUILD_IN_PROGRESS | EVAL_PENDING | REGISTERED | REJECTED | DEFERRED",
  "ecosistema_richiedente": "XX-ECO",
  "gap_descritto_originale": "...",
  "gap_validato": "...",
  "tipo": "skill | agente | team | workflow | ecosistema",
  "urgenza": "CRITICAL | HIGH | NORMAL | LOW",
  "kpi_attesi": [],
  "budget_disponibile": "USD | non specificato",
  "raccomandazione_intake": "BUILD | REUSE | EXTEND | REJECT",
  "decisione_conductor": "BUILD | REUSE | EXTEND | REJECT | DEFER",
  "motivo_decisione": "...",
  "blueprint_id": "ARCH-BP-YYYYMMDD-NNN | null",
  "forge_order_id": "CF-FO-YYYYMMDD-NNN | null",
  "gate_id": "CF-GATE-YYYYMMDD-NNN | null",
  "artefatto_id": "... | null",
  "path_artefatto": "company/... | null",
  "timestamp_ricezione": "YYYY-MM-DDTHH:MM:SSZ",
  "timestamp_decisione": "YYYY-MM-DDTHH:MM:SSZ | null",
  "timestamp_blueprint": "YYYY-MM-DDTHH:MM:SSZ | null",
  "timestamp_build_start": "YYYY-MM-DDTHH:MM:SSZ | null",
  "timestamp_eval": "YYYY-MM-DDTHH:MM:SSZ | null",
  "timestamp_chiusura": "YYYY-MM-DDTHH:MM:SSZ | null"
}
```

---

## Schema: record agente in Identity-HR (registry)

```json
{
  "agente_id": "nome-agente",
  "ruolo": "...",
  "tier": "haiku | sonnet | opus",
  "tipo": "coordinator | worker | bridge | gatekeeper | registrar | analyst | memory-keeper | executive-specialist",
  "ecosistema_owner": "XX-ECO",
  "figura_appartenenza": "board/chief-forge | 01-agency | ...",
  "path_scheda": "company/...",
  "stato": "registered | active | obsoleto_candidato | degradato | deprecated",
  "eval_score_iniziale": 0,
  "eval_score_ultimo": 0,
  "data_eval_ultimo": "YYYY-MM-DD",
  "costo_stimato_mese": "USD | non tracciato",
  "frequenza_invocazione_stimata": "alta | media | bassa | rara",
  "ultimo_invoco": "YYYY-MM-DDTHH:MM:SSZ | null",
  "data_registrazione": "YYYY-MM-DD",
  "data_ritiro": "YYYY-MM-DD | null",
  "motivo_ritiro": "... | null",
  "forge_order_id_build": "CF-FO-YYYYMMDD-NNN",
  "note": "..."
}
```

---

## Schema: skill nel portfolio

```json
{
  "skill_id": "nome-skill",
  "path": "company/skills/nome-skill/",
  "stato": "active | deprecated | experimental",
  "tipo": "atomic | composite",
  "ecosistema_owner": "XX-ECO",
  "agenti_che_usano": ["agente-id-1", "agente-id-2"],
  "eval_score": 0,
  "data_forgiatura": "YYYY-MM-DD",
  "data_ultimo_aggiornamento": "YYYY-MM-DD",
  "duplicato_di": "nome-skill | null",
  "forge_order_id": "CF-FO-YYYYMMDD-NNN",
  "note": "..."
}
```

---

## Schema: gate eval

```json
{
  "gate_id": "CF-GATE-YYYYMMDD-NNN",
  "eval_package_id": "CF-EP-YYYYMMDD-NNN",
  "forge_order_id": "CF-FO-YYYYMMDD-NNN",
  "artefatto_id": "...",
  "tipo": "skill | agente | team | workflow | ecosistema",
  "decisione": "PASS | FAIL",
  "pass_rate": 0,
  "threshold": 85,
  "test_count": 0,
  "failures": [],
  "gap_specifici": [],
  "istruzioni_iterate": "... | null",
  "ciclo": 1,
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Schema: pattern in memoria

```json
{
  "pattern_id": "CF-PAT-NNN",
  "descrizione": "...",
  "contesto": "tipo X da ecosistema Y",
  "outcome_tipico": {
    "eval_score_medio": 0,
    "cicli_medi": 0,
    "tempo_medio_gg": 0
  },
  "raccomandazione": "...",
  "fonte_richieste": ["CF-REQ-YYYYMMDD-NNN"],
  "data_prima_osservazione": "YYYY-MM-DD",
  "data_ultimo_aggiornamento": "YYYY-MM-DD",
  "frequenza_osservazione": 0
}
```

---

## Ciclo di vita dello state

1. **Creazione:** ogni evento crea o aggiorna un record nello state (mai cancella — archivia)
2. **Transizioni:** ogni cambio di `stato` è tracciato con timestamp separato
3. **Snapshot settimanale:** `cf-memoria` produce un snapshot dell'intero namespace ogni lunedì
4. **Archivio:** record >180gg senza correlazione con pattern attivi → spostati in `memoria/archivio/`
5. **Ripristino:** in caso di anomalia, lo snapshot più recente è la fonte di verità

---

## ID convention

| Prefisso | Tipo | Esempio |
|---|---|---|
| `CF-REQ-` | Richiesta intake | CF-REQ-20260617-001 |
| `CF-ARCH-` | Richiesta blueprint ad ARCHITETTURA | CF-ARCH-20260617-001 |
| `CF-FO-` | Forge order a FORGE | CF-FO-20260617-001 |
| `CF-FB-` | Forge brief (liaison to forge) | CF-FB-20260617-001 |
| `CF-EP-` | Eval package (forge to warden) | CF-EP-20260617-001 |
| `CF-GATE-` | Gate eval decision | CF-GATE-20260617-001 |
| `CF-PROP-` | Proposta ecosistema | CF-PROP-20260617-001 |
| `CF-MANDATO-` | Mandato ecosistema approvato | CF-MANDATO-20260617-001 |
| `CF-PAT-` | Pattern distillato da memoria | CF-PAT-001 |
| `CF-SNAP-` | Snapshot settimanale | CF-SNAP-20260617 |
