---
Type: STATE
Status: Active
Tags: #state #content-factory #CF-R7 #namespace #orders #publish #delivery
Created: 2026-06-23
Last updated: 2026-06-23
---

# State — CF-R7 Pubblicazione & Distribuzione

> **Namespace AgentDB:** `cf/publish` + `cf/delivery`
> **Schema file:** `orders/<id>/state.json` (publish[] per canale con esito + URL)
> **Regola review umana:** `review_umana.eseguita: true` è precondizione per ogni publish

---

## Namespace AgentDB

CF-R7 usa due namespace distinti nel memory store:

```
cf/publish/<order_id>/<canale>
  → { esito, url, ts, orchestratore, n_check, check_esito }

cf/delivery/<order_id>
  → { manifest_path, zip_path, canale_consegna, drive_url, conferma_ts, conferma_da }
```

---

## Schema orders/<id>/state.json (blocchi CF-R7)

```json
{
  "order_id": "CF-2026-NNNN",
  "workflow": "WF-PUBLISH-SOCIAL | WF-PUBLISH-YT | WF-DELIVERY-PACKAGER",

  "review_umana": {
    "eseguita": false,
    "ts": null,
    "nome": null,
    "note": null
  },

  "06-pre-publish-check": {
    "esito": "PASS | FAIL",
    "gate_cf_r6": "PASS | FAIL",
    "review_umana": "PASS | FAIL",
    "token_check": "PASS | FAIL",
    "motivi_fail": [],
    "ts": null
  },

  "07-adapt": {
    "canali_adattati": [],
    "channel_packs_path": "orders/<id>/06-delivery/channel_packs/",
    "ts": null
  },

  "publish": [
    {
      "canale": "instagram | linkedin | tiktok | youtube",
      "orchestratore": "mentalita_orchestrator.py | main_orchestrator.py | youtube-api",
      "esito": "PUBBLICATO | SCHEDULATO | FAIL",
      "url": null,
      "ts": null,
      "n_retry": 0,
      "motivo_fail": null
    }
  ],

  "08-check": [
    {
      "canale": "instagram | linkedin | tiktok | youtube",
      "url": null,
      "http_status": null,
      "esito": "URL_ATTIVO | FAIL",
      "n_retry": 0,
      "ts_check": null
    }
  ],

  "06-delivery": {
    "consegnato": false,
    "canale_consegna": "drive | email | transfer",
    "drive_url": null,
    "manifest_path": null,
    "zip_path": null,
    "conferma_ricezione": "in_attesa | ricevuta",
    "conferma_ts": null,
    "conferma_da": null,
    "ts_consegna": null
  },

  "feedback_loop": {
    "ts_48h": null,
    "ts_7gg": null,
    "metriche_48h_raccolte": false,
    "metriche_7gg_raccolte": false,
    "completato": false,
    "handoff_marketing_ts": null
  }
}
```

---

## Regola review umana (invariant)

Il campo `review_umana.eseguita` deve essere impostato a `true` PRIMA che CF-R7-PUBLISH
avvii qualsiasi publicazione. CF-R7-QA lo verifica come parte del gate pre-publish.

**Come documentare la review umana:**
```json
{
  "review_umana": {
    "eseguita": true,
    "ts": "2026-06-23T09:00:00Z",
    "nome": "Gael",
    "note": "Piano dry-run letto e approvato. Caption IG OK. Caption LI OK."
  }
}
```

Non si imposta `eseguita: true` senza averla effettivamente eseguita. La review umana
è un gate Board e la tracciabilità è parte del suo valore.

---

## Schema trace.jsonl (CF-R7 — ogni riga append-only)

```jsonl
{"ts":"2026-06-23T08:58:00Z","agent":"cf-r7-qa","event":"pre_publish_check","esito":"PASS","order_id":"CF-2026-0088"}
{"ts":"2026-06-23T08:59:00Z","agent":"cf-r7-adapt","event":"adapt_done","canali":["instagram","linkedin"],"order_id":"CF-2026-0088"}
{"ts":"2026-06-23T09:05:00Z","agent":"cf-r7-publish","event":"publish_done","canale":"instagram","url":"https://www.instagram.com/p/...","orchestratore":"mentalita_orchestrator.py","order_id":"CF-2026-0088"}
{"ts":"2026-06-23T09:07:00Z","agent":"cf-r7-check","event":"post_check","canale":"instagram","url":"https://www.instagram.com/p/...","http_status":200,"esito":"URL_ATTIVO","order_id":"CF-2026-0088"}
{"ts":"2026-06-25T09:05:00Z","agent":"cf-r7-feedback","event":"metriche_48h_raccolte","canale":"instagram","order_id":"CF-2026-0088"}
{"ts":"2026-06-30T09:05:00Z","agent":"cf-r7-feedback","event":"metriche_7gg_raccolte","canale":"instagram","feedback_loop_completato":true,"order_id":"CF-2026-0088"}
```

**Regola:** trace.jsonl è append-only. Nessuna riga si modifica o cancella.
L'URL definitivo del post pubblicato è sempre presente nella riga `publish_done`.

---

## Ciclo di vita stato ordine in CF-R7

```
[asset con gate verdi CF-R6]
         │
         ▼
[review_umana.eseguita = false] → attesa documentazione umana
         │ → true
         ▼
[06-pre-publish-check: PASS] → tutti e tre i controlli verdi
         │
         ▼
[07-adapt: completato] → channel_packs prodotti
         │
         ▼
[publish[canale].esito = PUBBLICATO | SCHEDULATO] → URL ricevuto
         │
         ▼
[08-check[canale].esito = URL_ATTIVO] → URL verificato live
         │
         ▼
[feedback_loop.completato = true] → entrambe le misurazioni raccolte
```

---

## Connessioni

- [[CF-R7-Pubblicazione/ARCHITETTURA]] · `ARCHITETTURA.md` — gate e pipeline completa
- [[cf-r7-qa]] · `agenti/cf-r7-qa.md` — scrive `06-pre-publish-check`
- [[cf-r7-publish]] · `agenti/cf-r7-publish.md` — scrive `publish[]`
- [[cf-r7-feedback]] · `agenti/cf-r7-feedback.md` — scrive `feedback_loop`
