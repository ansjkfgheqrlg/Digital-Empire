---
Type: STATE
Status: Active
Tags: #state #content-factory #CF-R6 #namespace #qa #failures #reasoningbank
Created: 2026-06-23
Last updated: 2026-06-23
---

# State — CF-R6 QA & Gate

> **Reparto:** CF-R6 QA & Gate · **Area:** Post-Produzione
> **Namespace:** `cf/qa` + `cf/failures` (ReasoningBank)
> **Schema principale:** `orders/<id>/05-qa/verdict.json`

---

## Namespace AgentDB

### `cf/qa`

Coda QA attiva e storico verdetti. Ogni entry rappresenta lo stato corrente di un
deliverable nel processo QA di CF-R6.

**Schema entry `cf/qa`:**
```json
{
  "order_id": "CF-2026-0061",
  "deliverable_path": "orders/CF-2026-0061/04-render/PNG/carosello-001/",
  "formato": "carosello-ig",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json",
  "stato": "PASS | FAIL | in_review | in_rework | gate_bloccato",
  "gate_corrente": "FORMAT | BRAND | COPY | MANDATO | completato",
  "n_rework": 0,
  "ts_ingresso": "2026-06-23T14:30:00Z",
  "ts_verdetto": "2026-06-23T14:45:00Z",
  "cf_r7_abilitato": true
}
```

**Stati validi:**
- `in_review`: deliverable prelevato, QA in corso.
- `in_rework`: FAIL emesso, specifica inviata al reparto produttore.
- `gate_bloccato`: errore tecnico durante un gate (agente non disponibile); escalation a L1-POST.
- `PASS`: tutti e 4 i gate verdi; CF-R7 abilitato.
- `FAIL`: dopo n_rework ≥ 2 e escalation; in attesa di decisione L1-POST.

### `cf/failures` — ReasoningBank

Archivio strutturato dei pattern di gate falliti. CF-R6-LEARN è il solo agente
autorizzato a scrivere in questo namespace.

**Schema entry `cf/failures`:**
```json
{
  "pattern_id": "PAT-COPY-HOOK-CAROSELLO-001",
  "gate": "GATE-COPY",
  "criterio": "hook assente o debole nella prima slide",
  "formato": "carosello-ig",
  "brand_coinvolti": ["mentalita-brutale", "brand-education"],
  "n_occorrenze": 5,
  "status": "SPECULATIVO | CONFERMATO | RISOLTO",
  "prima_occorrenza": "2026-06-10T09:00:00Z",
  "ultima_occorrenza": "2026-06-23T15:10:00Z",
  "causa_ipotizzata": "CF-R5-SLIDECOPY non riceve hook_type obbligatorio dal brief",
  "azione_proposta": "hook_type obbligatorio in brief.json; blocco in WF-BRIEF se assente",
  "segnalato_a": ["CF-Director", "07-FORGE"],
  "ts_segnalazione": "2026-07-06T10:00:00Z",
  "risolto_in": null
}
```

**Status validi:**
- `SPECULATIVO`: n < 3; osservazione in archivio; non segnalata ufficialmente.
- `CONFERMATO`: n ≥ 3; segnalata nel report mensile a CF-Director e 07-FORGE.
- `RISOLTO`: il pattern non si ripresenta da ≥3 mesi; azione implementata da FORGE.

---

## Schema `orders/<id>/05-qa/verdict.json`

File prodotto da CF-R6 al termine di WF-QA-SINGOLO. È il documento ufficiale del verdetto.
CF-R7 non può procedere senza un `verdict.json` con `verdetto_finale: "PASS"`.

```json
{
  "order_id": "CF-2026-0061",
  "deliverable_path": "orders/CF-2026-0061/04-render/PNG/carosello-001/",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json",
  "gate_formato": {
    "esito": "PASS | FAIL",
    "dimensioni": "1080x1350 CONFORME",
    "peso_max_mb": 6.2,
    "n_slide": 8,
    "codec": "N/A",
    "loudness_lufs": "N/A",
    "safe_area": "CONFORME",
    "motivi_fail": []
  },
  "gate_brand": {
    "esito": "PASS | FAIL",
    "palette": "CONFORME",
    "font": "CONFORME",
    "logo": "N/A",
    "tone_voice": "CONFORME",
    "motivi_fail": []
  },
  "gate_copy": {
    "esito": "PASS | FAIL",
    "hook_presente": true,
    "hook_posizione": "slide 1, prima riga",
    "social_proof_verificabile": true,
    "cta_unica": true,
    "motivi_fail": []
  },
  "mandato_compliance": {
    "esito": "PASS | FAIL",
    "claim_non_verificabili": 0,
    "genericita": 0,
    "prove_non_promesse": "CONFORME",
    "motivi_fail": []
  },
  "verdetto_finale": "PASS | FAIL",
  "n_rework": 0,
  "ts_verdetto": "2026-06-23T14:45:00Z",
  "owner_qa": "CF-R6-COORD"
}
```

---

## Regole di integrità (non negoziabili)

1. **Tutti i campi popolati**: ogni campo di `verdict.json` deve essere valorizzato;
   un campo vuoto o null equivale a gate non eseguito → verdetto FAIL automatico
   con motivo "gate non completato: campo [nome_campo] non valorizzato".
2. **PASS unanime**: `verdetto_finale: "PASS"` è valido solo se tutti e 4 i campi
   `gate_formato.esito`, `gate_brand.esito`, `gate_copy.esito`, `mandato_compliance.esito`
   sono "PASS". Qualsiasi combinazione diversa = verdetto_finale FAIL.
3. **CF-R7 bloccato senza PASS**: CF-R7 controlla `orders/<id>/05-qa/verdict.json` prima
   di procedere; se il file non esiste o `verdetto_finale` non è "PASS" → CF-R7 blocca.
4. **Immutabilità post-PASS**: un `verdict.json` con `verdetto_finale: "PASS"` non viene
   mai sovrascritto; se il committente chiede modifiche post-PASS, il deliverable modificato
   ricomincia WF-QA-SINGOLO come nuovo deliverable con nuovo `order_id` o nuovo ciclo.
5. **Tracciabilità rework**: ogni ciclo rework incrementa `n_rework` in verdict.json e
   appende una riga a `trace.jsonl` con `{ts, gate_fallito, motivo, destinatario_rework}`.

---

## Struttura directory ordine

```
orders/CF-2026-0061/
├── order.json              ← contratto di ordine (CF-Director)
├── state.json              ← stato corrente per fase
├── trace.jsonl             ← log eventi engine e gate
├── 01-brief/
│   └── brief.json
├── 02-copy/
│   └── slides-copy.json
├── 03-design/
│   └── slides/
├── 04-render/
│   └── PNG/carosello-001/
└── 05-qa/
    └── verdict.json        ← prodotto da CF-R6 (questo schema)
```

---

## Connessioni

- [[cf-r6-coord]] · `agenti/cf-r6-coord.md` — scrive e legge `cf/qa`
- [[cf-r6-learn]] · `agenti/cf-r6-learn.md` — scrive e aggiorna `cf/failures`
- [[WF-QA-SINGOLO]] · `workflow/WF-QA-SINGOLO.md` — produce `orders/<id>/05-qa/verdict.json`
