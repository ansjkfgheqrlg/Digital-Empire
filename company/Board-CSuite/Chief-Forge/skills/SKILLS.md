# SKILLS — Chief-Forge

> Skill proprie della figura Chief-Forge (livello L0).
> Fonte: [[BP-Chief-Forge]] §Skill proprie · [[Chief-Forge.md]] (v1) · [[07-FORGE/ECOSISTEMA.md]]

---

## Skill 1: `forge-intake`

**Scopo:** standardizzare e validare ogni richiesta di nuova capability in ingresso a Chief-Forge.
Trasforma richieste in linguaggio naturale (spesso incomplete o ambigue) in brief strutturati
pronti per la decisione del conductor.

**Owner:** `cf-intake-router`

**Input:**
```json
{
  "testo_libero": "abbiamo bisogno di qualcosa per X",
  "ecosistema_richiedente": "XX-ECO",
  "urgenza": "CRITICAL | HIGH | NORMAL | LOW"
}
```

**Output:**
```json
{
  "request_id": "CF-REQ-YYYYMMDD-NNN",
  "gap_validato": "riformulazione precisa del gap",
  "tipo": "skill | agente | team | workflow | ecosistema",
  "kpi_attesi": ["..."],
  "budget_stimato": "...",
  "raccomandazione": "BUILD | REUSE | EXTEND | REJECT",
  "analisi_duplicati": {...},
  "brief_completo": true
}
```

**Logica kernel:** estrae le dimensioni obbligatorie da testo libero (cosa manca, quale KPI
cambia, budget, urgenza), verifica la presenza di un problema reale, lancia l'analisi duplicati
in parallelo, sintetizza il brief con raccomandazione motivata.

**Eval criteria:**
- Il brief include sempre un KPI misurabile
- La raccomandazione è sempre motivata (mai solo "BUILD" senza contesto)
- Duplicati sempre verificati prima del brief
- Format JSON valido e completo

**Path previsto:** `company/skills/forge-intake/` (da forgiare da FORGE con questo blueprint)

---

## Skill 2: `agent-registry` (Identity-HR)

**Scopo:** mantenere e interrogare il registro completo di tutti gli agenti di EMPIRE OS.
Funziona sia come database (CRUD) sia come audit engine (rileva anomalie).

**Owner:** `cf-agent-registry`

**Input (CRUD):**
```json
{
  "operazione": "LEGGI | REGISTRA | AGGIORNA | RITIRA",
  "agente_id": "...",
  "dati_agente": {
    "ruolo": "...", "tier": "...", "ecosistema_owner": "...",
    "path_scheda": "...", "eval_score": 0, "costo_stimato_mese": "..."
  }
}
```

**Output (LEGGI / AUDIT):**
```json
{
  "agente_id": "...",
  "record": {...},
  "anomalie": ["orfano", "degradato", "fantasma"],
  "snapshot_holding": {
    "totale": 0, "active": 0, "deprecated": 0, "costo_totale": "USD"
  }
}
```

**Logica kernel:** CRUD sul namespace `board/chief-forge/registry`; audit settimanale
automatico che confronta i record con la struttura reale in `company/`; genera report
anomalie con classificazione di gravità.

**Eval criteria:**
- Copertura 100%: ogni agente trovato in `company/` deve essere nel registro
- Nessun record con campi critici nulli (id, ruolo, tier, ecosistema_owner)
- Audit settimanale produce report entro 1h dal trigger

**Path previsto:** `company/skills/agent-registry/` (da forgiare da FORGE)

---

## Skill 3: `capability-gap-radar`

**Scopo:** analisi proattiva del gap capability: identifica aree dove EMPIRE OS manca di
skill o agenti critici PRIMA che gli ecosistemi le richiedano. Trasforma l'analisi reattiva
(risponde alle richieste) in analisi proattiva (anticipa i bisogni).

**Owner:** `cf-conductor` (con input da `cf-skill-portfolio` e `cf-agent-registry`)

**Input:**
```json
{
  "scope": "holding | ecosistema_specifico",
  "ecosistema_target": "XX-ECO | null",
  "profondita": "SUPERFICIALE | COMPLETA",
  "confronto_con_roadmap": true
}
```

**Output:**
```json
{
  "gap_identificati": [
    {
      "area": "...",
      "tipo_gap": "skill_mancante | agente_mancante | workflow_mancante",
      "impatto_stimato": "CRITICO | ALTO | BASSO",
      "ecosistemi_impattati": ["XX-ECO"],
      "artefatto_suggerito": "...",
      "priorita_suggerita": "P0 | P1 | P2"
    }
  ],
  "gap_coperti_recentemente": ["..."],
  "raccomandazione_prossime_forgiature": ["..."]
}
```

**Logica kernel:** confronta la mappa capability attuale (portfolio + registry) con la roadmap
degli ecosistemi e con i KPI storici (da `cf-memoria`). Identifica i gap per impatto su Agency/revenue
prima, poi per impatto su Operations, poi il resto. Produce un backlog prioritizzato.

**Eval criteria:**
- Ogni gap identificato ha un impatto collegato a un KPI misurabile
- Nessun gap duplica una richiesta già in pipeline intake
- Output include sempre gap ad alto impatto Agency (revenue-first)
- Eseguibile senza intervento umano in modalità SUPERFICIALE

**Path previsto:** `company/skills/capability-gap-radar/` (da forgiare da FORGE)

---

## Note sulle skill

Queste 3 skill sono le skill **proprie** della figura Chief-Forge: le usa internamente per
il suo funzionamento. Non sono skill degli ecosistemi clienti.

Lo stato attuale è **da forgiare**: i blueprint sono qui descritti; la build parte via
WF-CAPABILITY-INTAKE con tipo `skill` per ognuna.

Skill P0 (da forgiare prima): `forge-intake` (blocca il funzionamento di cf-intake-router
senza un formato validato), poi `agent-registry` (blocca WF-HR-REGISTRY), poi
`capability-gap-radar` (arricchisce ma non blocca il flusso base).
