---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R7 #publish #social #instagram #tiktok #linkedin #orchestratori #review-umana
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-PUBLISH-SOCIAL — Pubblicazione Social (IG / TikTok / LinkedIn)

> **Reparto:** CF-R7 Pubblicazione & Distribuzione · **Area:** Post-Produzione
> **[WRAPPA] orchestratori Python ATTIVI: `main_orchestrator.py` + `mentalita_orchestrator.py` — runtime NON modificato (ADR-003)**
> **REVIEW UMANA OBBLIGATORIA:** gate manuale non bypassabile (policy Board)

---

## Scopo

Portare deliverable con gate verdi CF-R6 sui canali social (IG, TikTok, LinkedIn) tramite
gli orchestratori Python esistenti wrappati. La pipeline garantisce tre invariant assoluti:
(1) nessuna pubblicazione senza gate verdi in state.json, (2) nessuna pubblicazione senza
review umana documentata, (3) nessuna pubblicazione con token canale scaduti.

**Dry-run:** produce un piano di pubblicazione completo (asset, canali, caption adattate,
orari, orchestratore) senza toccare alcun canale. Utile per review umana prima dell'esecuzione.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | DRY-RUN (opzionale ma raccomandato) | CF-R7-COORD | `order.json` + state.json | `publish-plan.json` a zero effetti | Piano visibile per review |
| 1 | Pre-check gate | CF-R7-QA | state.json + canali ordine | `pre-publish-verdict.json` | Gate verdi CF-R6 + review umana + token: tutti PASS |
| 2 | Adattamento per canale | CF-R7-ADAPT | Asset + caption base + brand_kit | `channel_packs[]` per ogni canale | Caption entro limite canale; handle corretti |
| 3 | REVIEW UMANA | — (gate manuale) | `publish-plan.json` o `channel_packs[]` | `state.json → review_umana.eseguita: true` | Obbligatorio; pipeline ferma fino a ok umano |
| 4 | Pubblicazione | CF-R7-PUBLISH | `channel_packs[]` + review confermata | URL pubblicazione per canale [WRAPPA] | review_umana.eseguita: true nell'input |
| 5 | Verifica live | CF-R7-CHECK | URL da passo 4 | `check_results[]` con HTTP status | URL attivi per tutti i canali |
| 6 | Log e chiusura | CF-R7-COORD | check_results + URL | state.json aggiornato + trace.jsonl | tutti_attivi: true |
| 7 | Feedback schedulato | CF-R7-FEEDBACK | URL + ts_publish | scheduling 48h + 7gg in state.json | — |

---

## Dry-run (passo 0 — raccomandato)

Il dry-run produce un piano di pubblicazione senza toccare i canali:

```json
{
  "order_id": "CF-2026-0088",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "piano_pubblicazione": [
    {
      "canale": "instagram",
      "asset": "orders/CF-2026-0088/06-delivery/carousel-001/",
      "caption_preview": "Hook: Se aspetti la motivazione, hai già perso...\n[30 hashtag]",
      "orario": "2026-06-23T09:00:00Z",
      "orchestratore": "mentalita_orchestrator.py",
      "token_status": "VALIDO"
    },
    {
      "canale": "linkedin",
      "asset": "orders/CF-2026-0088/06-delivery/carousel-001/",
      "caption_preview": "Hook professionale...\n[4 hashtag]",
      "orario": "2026-06-23T09:05:00Z",
      "orchestratore": "main_orchestrator.py",
      "token_status": "VALIDO"
    }
  ],
  "pre_check": { "gate_verdi": true, "review_umana_presente": false, "tutti_token_validi": true },
  "decisione": "PRONTO — in attesa review umana prima di eseguire"
}
```

Il committente legge il piano dry-run e documenta la propria approvazione in state.json
(`review_umana.eseguita: true, ts: "...", nome: "..."`). Solo dopo la pipeline avanza al passo 4.

---

## Gate non bypassabili

**GATE PRE-PUBLISH (passo 1 — CF-R7-QA):**
```
1. Gate verdi CF-R6 in state.json → gate_formato + gate_brand + gate_copy + gate_mandato: tutti PASS
2. review_umana.eseguita: true in state.json
3. check_token() per ogni canale → VALIDO
```
Manca anche uno solo → BLOCCO. Non si avanza.

**GATE REVIEW UMANA (passo 3 — manuale):**
La pipeline si ferma e aspetta. Non c'è timeout automatico per avanzare senza approvazione umana.
Il committente o il socio documenta la review in state.json prima di riavviare la pipeline.

---

## I/O JSON completo di esempio

**Input ordine:**
```json
{
  "order_id": "CF-2026-0088",
  "brand_kit": "brands/mentalita-brutale/brand-kit.json",
  "canali": ["instagram", "linkedin"],
  "asset_path": "orders/CF-2026-0088/06-delivery/",
  "slot_calendario": "2026-06-23T09:00:00Z",
  "gate_verdi_cf_r6": true
}
```

**Output finale (state.json aggiornato):**
```json
{
  "order_id": "CF-2026-0088",
  "workflow": "WF-PUBLISH-SOCIAL",
  "fasi": {
    "01-pre-check":   { "stato": "PASS", "ts": "2026-06-23T08:58:00Z" },
    "02-adapt":       { "stato": "completato", "canali": ["instagram", "linkedin"], "ts": "2026-06-23T08:59:00Z" },
    "03-review-umana":{ "stato": "completato", "eseguita": true, "ts": "2026-06-23T09:00:00Z", "nome": "Gael" },
    "04-publish": {
      "instagram": { "stato": "PUBBLICATO", "url": "https://www.instagram.com/p/...", "ts": "2026-06-23T09:05:00Z" },
      "linkedin":  { "stato": "PUBBLICATO", "url": "https://www.linkedin.com/posts/...", "ts": "2026-06-23T09:06:00Z" }
    },
    "05-check":       { "stato": "URL_ATTIVO", "tutti_attivi": true, "ts": "2026-06-23T09:08:00Z" },
    "06-feedback":    { "ts_48h": "2026-06-25T09:05:00Z", "ts_7gg": "2026-06-30T09:05:00Z" }
  }
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0088 · brand: mentalita-brutale · carosello IG+LI · slot 09:00

**Passo 0 (dry-run):** Piano generato → inviato a Gael per review. Piano mostra asset,
caption preview IG (2100 char, 30 hashtag) e LI (600 char, 4 hashtag), orchestratori.

**Passo 1 (pre-check):** Gate CF-R6: PASS; review_umana.eseguita: true (Gael, 08:55); token IG e LI: VALIDI → PASS.

**Passo 2 (adapt):** Caption IG calibrata (hook 125 char + testo + 30 hashtag); LI versione professionale. Pack prodotti.

**Passo 3 (review umana):** Già eseguita (08:55) → pipeline avanza.

**Passo 4 (publish):**
- IG: `mentalita_orchestrator.py` [WRAPPA] → URL IG in 12s.
- LI: `main_orchestrator.py` [WRAPPA] → URL LI in 9s.

**Passo 5 (check):** GET URL IG → 200 OK; GET URL LI → 200 OK → tutti_attivi: true.

**Passo 6:** state.json chiuso con URL. trace.jsonl: 6 righe aggiunte.

**Passo 7:** Feedback schedulato 48h (2026-06-25T09:05) e 7gg (2026-06-30T09:05).

---

## Connessioni

- [[cf-r7-coord]] · `agenti/cf-r7-coord.md` — orchestra questo workflow
- [[cf-r7-qa]] · `agenti/cf-r7-qa.md` — gate pre-publish passo 1
- [[cf-r7-publish]] · `agenti/cf-r7-publish.md` — executor passo 4 [WRAPPA]
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §5(e) WF-PUBLISH-SOCIAL`
