---
Type: STATE
Status: Active
Tags: #state #CF-R5 #visual #namespace #trace #state-machine #design #amnesia-test
Created: 2026-06-23
Last updated: 2026-06-23
---

# State — CF-R5 Visual & Design / Caroselli

> Ogni ordine design è ripartibile a freddo dal `state.json` + `trace.jsonl`.
> Regola amnesia test: se un agente muore durante il render, il successivo riparte
> dalla fase indicata in state.json senza perdere il lavoro precedente.

---

## Namespace AgentDB

| Namespace | Contenuto | Owner | Operazioni |
|---|---|---|---|
| `cf/design` | Stato produzione design per ordine: `{order_id, workflow, brand, ramo_attivo, fase_corrente, gate_formato, gate_brand, n_rework}` | CF-R5-COORD | store dopo ogni fase; retrieve per ripresa a freddo |
| `cf/thumbnails` | Stato ordini thumbnail: `{order_id, brand_slug, concept_approvato, variante_ab_scelta, ctr_7gg, thumbnail_selezionata_path}` | CF-R5-COORD | store a concept approvato; update a scelta committente e metriche feedback |
| `cf/graphics` | Stato ordini grafiche statiche: `{order_id, brand_slug, formati_target, delivery_path, gate_esito}` | CF-R5-COORD | store a ricezione ordine; update a delivery completata |

---

## Schema state.json — ordine carosello (WF-CAROSELLO)

```json
{
  "order_id": "CF-2026-0101",
  "workflow": "WF-CAROSELLO",
  "brand": "mentalita-brutale",
  "brand_kit_path": "brands/mentalita-brutale/brand-kit.json",
  "ramo_attivo": "B",
  "avviato_il": "2026-06-23T09:00:00Z",
  "fasi": {
    "00-dry-run": {
      "stato": "completato | in_corso | non_avviato | rework",
      "ts": "2026-06-23T09:00:00Z",
      "slides_copy_path": "orders/CF-2026-0101/03-design/slides-copy.json",
      "prompt_set_path": "orders/CF-2026-0101/03-design/prompt-set.json",
      "approvazione": "APPROVATO | REWORK | PENDING"
    },
    "03-design": {
      "stato": "completato",
      "ts": "2026-06-23T09:15:00Z",
      "ramo": "B",
      "output_path": "orders/CF-2026-0101/03-design/canva-export/",
      "n_slide": 9
    },
    "04-render": {
      "stato": "completato",
      "ts": "2026-06-23T09:20:00Z",
      "png_path": "orders/CF-2026-0101/04-render/PNG/",
      "n_png": 9
    },
    "gate-formato": {
      "stato": "PASS | FAIL | non_eseguito",
      "ts": "2026-06-23T09:21:00Z",
      "n_fail": 0,
      "verdict_path": "orders/CF-2026-0101/05-qa/verdict-formato.json"
    },
    "gate-brand": {
      "stato": "PASS | FAIL | non_eseguito",
      "ts": "2026-06-23T09:22:00Z",
      "n_fail": 0,
      "verdict_path": "orders/CF-2026-0101/05-qa/verdict-brand.json"
    },
    "caption": {
      "stato": "completato",
      "ts": "2026-06-23T09:23:00Z",
      "caption_path": "orders/CF-2026-0101/caption.txt",
      "hashtag_path": "orders/CF-2026-0101/hashtag-set.txt"
    },
    "handoff-cf-r6": {
      "stato": "in_attesa | completato",
      "ts": null,
      "pronto_per_cf_r6": true
    }
  },
  "n_rework": 0,
  "crediti_engine": 0,
  "stato_finale": "in_produzione | gate_pass | in_rework | consegnato | fallito"
}
```

---

## Schema state.json — ordine thumbnail (WF-THUMBNAIL)

```json
{
  "order_id": "CF-2026-0110",
  "workflow": "WF-THUMBNAIL",
  "brand": "mentalita-brutale",
  "fasi": {
    "00-concept-set": {
      "stato": "completato",
      "ts": "2026-06-23T10:00:00Z",
      "concept_set_path": "orders/CF-2026-0110/03-design/concept-set.json",
      "concept_approvato": "A | B | C | null"
    },
    "02-generazione": {
      "stato": "completato | non_avviato",
      "ts": null,
      "thumbnail_master_path": "orders/CF-2026-0110/03-design/thumbnail-master.png",
      "engine": "canva | gemini | higgsfield"
    },
    "03-resize": {
      "stato": "completato",
      "ts": null,
      "varianti": {}
    },
    "gate-formato": { "stato": "PASS | FAIL | non_eseguito", "leggibilita_10pct": "PASS | FAIL" },
    "gate-brand": { "stato": "PASS | FAIL | non_eseguito" },
    "ab-choice": {
      "stato": "in_attesa | completato",
      "scelta_committente": "A | B | null",
      "ts": null
    }
  },
  "thumbnail_selezionata_path": null,
  "n_rework": 0
}
```

---

## Schema trace.jsonl (append-only, ogni riga un evento)

Il file `orders/<order_id>/trace.jsonl` è append-only. Ogni operazione significativa
(fase completata, gate eseguito, engine call, rework richiesto) appende una riga:

```json
{"ts":"2026-06-23T09:00:00Z","agent":"cf-r5-slidecopy","event":"dry_run_completato","engine_id":null,"nota":"slides-copy.json e prompt-set.json prodotti; costo 0 crediti"}
{"ts":"2026-06-23T09:01:00Z","agent":"cf-r5-coord","event":"dry_run_approvato","engine_id":null,"nota":"ramo B scelto; avvio canva export"}
{"ts":"2026-06-23T09:15:00Z","agent":"cf-r5-canva","event":"canva_export_completato","engine_id":"canva","nota":"9 PNG esportati in 03-design/canva-export/"}
{"ts":"2026-06-23T09:21:00Z","agent":"cf-r5-qa","event":"gate_formato_pass","engine_id":null,"nota":"GATE-FORMATO PASS su 9 PNG; peso max 4.1MB; contrasto min 16:1"}
{"ts":"2026-06-23T09:22:00Z","agent":"cf-r5-qa","event":"gate_brand_pass","engine_id":null,"nota":"GATE-BRAND PASS; palette mentalita-brutale; font Anton; logo presente"}
{"ts":"2026-06-23T09:23:00Z","agent":"cf-r5-coord","event":"handoff_cf_r6","engine_id":null,"nota":"pronto_per_cf_r6: true; state.json aggiornato"}
```

---

## Regole di integrità state.json

1. **Sequenzialità gate:** `gate-brand` non può essere PASS se `gate-formato` non è PASS.
   Uno state.json con `gate-formato: FAIL` e `gate-brand: PASS` è corrotto e va segnalato
   a CF-R5-COORD immediatamente.
2. **Dry-run prima di generazione:** in trace.jsonl deve esserci una riga con
   `event: "dry_run_completato"` PRIMA di qualsiasi `event: "canva_export_completato"` o
   `event: "render_avviato"`. Mancanza = segnalazione CF-R5-COORD.
3. **n_rework consistente:** se `n_rework > 0` in state.json, ci deve essere almeno una
   riga `event: "gate_formato_fail"` o `event: "gate_brand_fail"` in trace.jsonl.
4. **Concept approvato prima di generazione:** in WF-THUMBNAIL, `02-generazione.stato`
   non può essere "completato" se `00-concept-set.concept_approvato` è null.

---

## Ripresa a freddo (amnesia test)

Se CF-R5-CANVA muore dopo l'export Canva ma prima di aggiornare state.json:
1. CF-R5-COORD rileva che la fase `03-design` non è segnata come "completato" in state.json.
2. Controlla trace.jsonl: c'è un evento `canva_export_completato`?
3. Sì → i file esistono in `03-design/canva-export/`; riprende dal passo successivo (gate).
4. No → l'export è in stato incerto; CF-R5-CANVA deve verificare via `get-design` MCP
   se il design esiste in Canva e rieseguire l'export se necessario.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dettaglio schema trace e regola dry-run
- [[cf-r5-coord]] · `agenti/cf-r5-coord.md` — aggiorna state.json a ogni fase
- [[WF-CAROSELLO]] · `workflow/WF-CAROSELLO.md` — flusso principale che popola questo schema
