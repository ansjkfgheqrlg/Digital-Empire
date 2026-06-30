---
Type: STATE
Status: Active
Tags: #state #content-factory #CF-R8 #namespace #patterns #failures #improvements #apprendimento
Created: 2026-06-30
Last updated: 2026-06-30
---

# State — CF-R8 Apprendimento & Ottimizzazione

> **Reparto:** CF-R8 Apprendimento & Ottimizzazione · **Area:** Post-Produzione
> **Namespace primari:** `cf/patterns` + `cf/failures` (lettura) + `cf/improvements`
> **Regola cardinale:** append-only sui pattern; nessuna modifica retroattiva senza versioning esplicito

---

## Namespace AgentDB

### `cf/patterns`

Archivio dei pattern operativi validati. Owner scrittura: CF-R8-QA (dopo gate di validazione).
Lettura: CF-R8-COORD, CF-R8-HOOK, CF-R8-ENGINE, CF-R8-NEURAL, CF-R1-LEARN (per aggiornamento libreria).
Sola lettura per tutti i reparti di produzione.

**Schema entry `cf/patterns`:**
```json
{
  "pattern_id": "PAT-R8-HOOK-MB-CAROSELLO-001",
  "tipo": "hook | engine | failure-distillato",
  "contesto": {
    "brand": "mentalita-brutale",
    "formato": "carosello-ig",
    "nicchia": "mindset"
  },
  "pattern": "Hook di tipo interrogativo-numerico associato a engagement superiore alla media in 3 caroselli nel periodo 6-20 giugno 2026",
  "esempi": [
    {
      "order_id": "CF-2026-0041",
      "osservazione": "Hook 'Perché il 90% dei tuoi post non porta follower?' — engagement [DM]",
      "namespace": "cf/patterns",
      "key": "CF-R7-FEEDBACK-2026-06-06",
      "ts": "2026-06-06T10:00:00Z"
    },
    {
      "order_id": "CF-2026-0055",
      "osservazione": "Hook '3 errori che uccidono il tuo reach ogni giorno' — engagement [DM]",
      "namespace": "cf/patterns",
      "key": "CF-R7-FEEDBACK-2026-06-13",
      "ts": "2026-06-13T10:00:00Z"
    },
    {
      "order_id": "CF-2026-0063",
      "osservazione": "Hook 'Quanto vale davvero un follower nel 2026?' — engagement [DM]",
      "namespace": "cf/patterns",
      "key": "CF-R7-FEEDBACK-2026-06-20",
      "ts": "2026-06-20T10:00:00Z"
    }
  ],
  "n_casi": 3,
  "validato_da": "CF-R8-QA",
  "ts_validazione": "2026-06-30T09:30:00Z",
  "azione_proposta": "Aumentare peso hook_type 'interrogativo-numerico' in libreria CF-R1 per contesto {brand: mentalita-brutale, formato: carosello-ig, nicchia: mindset}",
  "stato": "VALIDATO | IN_IMPROVEMENT | IMPLEMENTATO",
  "improvement_id": null,
  "neural_trained": false,
  "ts_neural_training": null,
  "versione": "1.0"
}
```

**Stati validi:**
- `VALIDATO`: pattern superato i 4 gate QA; in archivio; proposta CF-R1 inviata o in attesa.
- `IN_IMPROVEMENT`: pattern ha un improvement aperto in `cf/improvements`.
- `IMPLEMENTATO`: improvement chiuso con status RISOLTO; pattern confermato efficace.

---

### `cf/failures` — ReasoningBank

Archivio strutturato dei gate falliti. Owner scrittura: CF-R6-LEARN (sorgente primaria).
CF-R8-REASONING legge e distilla; non scrive nuove entry — aggiorna solo il campo `status`
quando un pattern è RISOLTO (tramite CF-R8-COORD).

Per lo schema completo di `cf/failures` vedere `../CF-R6-QA-Gate/state/README.md §cf/failures`.

**Interazione di CF-R8 con `cf/failures`:**

| Operazione | Agente | Campo modificato |
|---|---|---|
| Lettura entries CONFERMATO | CF-R8-REASONING | nessuna scrittura |
| Update status → RISOLTO | CF-R8-COORD (post-validazione improvement) | `status`, `risolto_in` |
| Lettura storica per analisi engine | CF-R8-ENGINE | nessuna scrittura |

CF-R8 non crea nuove entry in `cf/failures`: questa responsabilità è esclusiva di CF-R6-LEARN.

---

### `cf/improvements`

Tracking del ciclo di miglioramento. Owner scrittura: CF-R8-COORD.
Lettura: CF-Director, L1-POST, CF-R8-QA (per validazione effetto).

**Schema entry `cf/improvements`:**
```json
{
  "improvement_id": "IMP-R8-2026-07-001",
  "pattern_id_riferimento": "PAT-R8-FAILURE-COPY-HOOK-001",
  "problema": "hook_type non obbligatorio in brief.json — Gate-COPY FAIL per hook assente (5 occorrenze giugno 2026)",
  "proposta_fix": "Aggiungere hook_type come campo obbligatorio in brief.json; gate CF-R1-QA blocca brief privi di hook_type",
  "tipo_fix": "puntuale | strutturale | architetturale",
  "reparto_destinatario": "CF-R1 | CF-R2 | CF-R3 | CF-R4 | CF-R5 | 07-FORGE | Board",
  "verifica_attesa": "Riduzione Gate-COPY fail rate per criterio hook nei 30gg successivi",
  "stato": "proposto | approvato | in_implementazione | in_osservazione | chiuso | rifiutato",
  "ts_proposta": "2026-07-01T10:00:00Z",
  "ts_approvazione": "2026-07-01T14:00:00Z",
  "ts_implementazione": null,
  "ts_inizio_osservazione": null,
  "ts_fine_osservazione": null,
  "ts_chiusura": null,
  "verdetto_finale": "RISOLTO | PARZIALE | RECIDIVA | null",
  "delta_kpi_misurato": null,
  "adr_generato": null,
  "note": ""
}
```

**Stati validi `cf/improvements`:**
- `proposto`: proposta formulata da CF-R8-REASONING, non ancora presentata a CF-Director.
- `approvato`: CF-Director ha approvato; fix non ancora implementato.
- `in_implementazione`: reparto destinatario o 07-FORGE sta lavorando sul fix.
- `in_osservazione`: fix implementato; 4 settimane di osservazione in corso.
- `chiuso`: CF-R8-QA ha emesso verdetto RISOLTO o PARZIALE dopo osservazione.
- `rifiutato`: CF-Director ha rifiutato la proposta con motivazione.

---

## Regole di integrità (non negoziabili)

1. **Append-only su `cf/patterns`**: nessuna entry viene eliminata; se una entry diventa
   obsoleta viene marcata `stato: "OBSOLETO"` con motivo e ts_obsolescenza. Le entry
   obsolete rimangono nell'archivio per tracciabilità storica.
2. **Fonte tracciabile obbligatoria**: ogni entry in `cf/patterns` deve avere almeno
   1 fonte `{namespace, key, ts}` per ogni caso nell'array `esempi[]`. Un'entry senza
   fonte completa non è un'entry valida — è un difetto di integrità da correggere
   immediatamente da CF-R8-QA.
3. **Versioning libreria CF-R1**: ogni proposta di aggiornamento alla libreria formule
   di CF-R1 deve essere tracciata con il `pattern_id` che la genera e il `ts_proposta`.
   La libreria CF-R1 mantiene il proprio versioning; CF-R8 mantiene il riferimento.
4. **Nessuna scrittura in `cf/failures` da CF-R8** (eccetto update `status`): CF-R8
   non crea nuove entry in `cf/failures`; questa regola protegge l'integrità del
   ReasoningBank di CF-R6-LEARN.
5. **Idempotenza**: i workflow CF-R8 sono idempotenti — una riesecuzione sullo stesso
   periodo non crea duplicati (il controllo Gate-UNICITA lo garantisce per `cf/patterns`;
   il controllo per `improvement_id` lo garantisce per `cf/improvements`).
6. **Max 3 improvement attivi**: `cf/improvements` non deve avere più di 3 entry con
   stato `approvato | in_implementazione | in_osservazione` contemporaneamente. CF-R8-COORD
   verifica questo limite prima di ogni apertura di nuovo improvement.

---

## Struttura directory state ciclo

```
company/Memory/
└── cf-r8-state/             (non ancora creata; creata al primo ciclo reale)
    ├── cycles/
    │   ├── WF-PD-2026-06-30.json    ← state machine WF-PATTERN-DISTILLATION
    │   └── WF-IC-2026-07-01.json    ← state machine WF-IMPROVEMENT-CYCLE
    └── reports/
        └── report-2026-06.json      ← report mensile per CF-Director
```

I namespace `cf/patterns`, `cf/failures`, `cf/improvements` risiedono nel sistema AgentDB
di claude-flow (inizializzati in F2 Backbone Operativo con i 10 namespace; `cf/improvements`
è il namespace aggiuntivo specifico di CF-R8).

---

## Connessioni

- [[cf-r8-coord]] · `agenti/cf-r8-coord.md` — scrive e legge `cf/improvements`; coordina archiviazione in `cf/patterns`
- [[cf-r8-qa]] · `agenti/cf-r8-qa.md` — scrive in `cf/patterns` (post-validazione); legge per Gate-UNICITA
- [[CF-R6-QA-Gate/state/README]] · `../CF-R6-QA-Gate/state/README.md` — schema completo `cf/failures` (sorgente primaria CF-R8)
