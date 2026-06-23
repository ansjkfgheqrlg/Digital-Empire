---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R4 #articolo #seo #gate-copy #gate-brand #pipeline
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-ARTICOLO — Pipeline Articolo Blog / Knowledge Base

> **Reparto:** CF-R4 Produzione Testuale · **Area:** Produzione
> **[WRAPPA-ESISTENTE + TARGET-V2] — nessun runtime esistente modificato (ADR-003)**
> **Dry-run disponibile (passo 0):** produce outline + stima a costo zero prima del draft

---

## Scopo

Produrre articoli blog, pillar page e knowledge base completi a partire dal `brief.json`
approvato da CF-R1. Il workflow copre: outline → draft → pass SEO/AI-SEO → GATE-COPY
(CF-R4-QA) → GATE-BRAND (CF-R4-QA) → output finale in `.md` / `.html`. Il gate CF-R6
(globale) avviene dopo, in modo indipendente da questo workflow.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | Dry-run outline | CF-R4-WRITE | `brief.json` + `brand_kit.voice` | `02-copy/outline.json` (stima lunghezza, tier, heading) | nessun draft scritto; zero costo |
| 1 | Redazione draft | CF-R4-WRITE | `brief.json` + `brand_kit` + outline approvato | `02-copy/articolo-draft.md` | auto-verifica interna CF-R4-WRITE |
| 2 | Varianti headline | CF-R4-HEADLINE | `brief.json` + titolo draft | `02-copy/headline-varianti.json` (×3 per A/B test) | coerenza con hook_type del brief |
| 3 | Pass SEO/AI-SEO | CF-R4-SEO | `articolo-draft.md` + keyword target | `02-copy/articolo-seo.md` + `seo-report.json` | keyword density, heading structure, meta |
| 4 | GATE-COPY interno | CF-R4-QA | `articolo-seo.md` + `brief.json` + `brand_kit.voice` | `05-qa/gate-copy-internal.json` | struttura, hook apertura, claim verificabili, parole_vietate assenti |
| 5 | GATE-BRAND interno | CF-R4-QA | `articolo-seo.md` + `brand_kit.voice` | `05-qa/gate-brand-internal.json` | tone campionato vs brand_kit.voice.esempi |
| 6 | Output finale | CF-R4-COORD | `articolo-seo.md` + gate PASS | `02-copy/articolo-final.md` + `02-copy/articolo-final.html` | state.json aggiornato; `pronto_per_cf_r6: true` |

---

## Dry-run (passo 0 — obbligatorio prima del draft)

Prima di avviare la redazione, CF-R4-WRITE produce l'outline a costo zero:

```json
{
  "order_id": "CF-2026-0101",
  "tipo_workflow": "WF-ARTICOLO",
  "dry_run": true,
  "brand": "brand-agency",
  "angle": "gap-contenuto-conversione",
  "hook_type": "domanda-provocatoria",
  "struttura_proposta": {
    "H1": "Il Gap che Svuota il Budget di Contenuto",
    "H2": [
      "Il contenuto informativo non converte da solo",
      "Il problema non è la frequenza: è il percorso",
      "Come costruire il ponte",
      "Il passo successivo"
    ]
  },
  "word_count_stimato": 1350,
  "tier_consigliato": "sonnet",
  "note": "outline pronto; nessun draft avviato"
}
```

Se il committente ha impostato `show_outline: true` nel brief, CF-R4-COORD attende
l'approvazione prima di avviare il passo 1. Altrimenti procede direttamente.

---

## Gate di uscita

**GATE-COPY (CF-R4-QA, passo 4 — obbligatorio):**
- Struttura heading valida: H1 unico, H2 coerenti con struttura_formato, nessun salto di livello
- Hook nelle prime 3 righe / primo paragrafo; corrisponde al hook_type del brief
- CTA strutturale presente (per articolo: direzione narrativa in chiusura, non APSOC)
- Zero claim non verificabili: nessuna percentuale senza fonte, nessuna promessa garantita
- Zero parole_vietate dal brand_kit.voice
- Word count nel range ±20% del brief

**GATE-BRAND (CF-R4-QA, passo 5 — obbligatorio):**
- Tone of voice campionato vs brand_kit.voice.esempi_si e esempi_no (≥5 campioni)
- Nessuna occorrenza di parole_vietate (controllo aggiuntivo su testo finale)
- Stile coerente con il tono dichiarato (es. "diretto, autorevole" → frasi brevi, verbi attivi)

Entrambi i gate devono essere PASS prima di procedere al passo 6. Un FAIL blocca il
pezzo e avvia rework con specifica strutturata. 2 rework consecutivi → escalation L1-PROD.

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0101",
  "workflow": "WF-ARTICOLO",
  "brand": "brand-agency",
  "avviato_il": "2026-06-23T09:00:00Z",
  "fasi": {
    "00-dry-run": { "stato": "completato", "ts": "2026-06-23T09:01:00Z", "outline_path": "02-copy/outline.json" },
    "01-draft": { "stato": "completato", "ts": "2026-06-23T09:12:00Z", "word_count": 1387, "draft_path": "02-copy/articolo-draft.md" },
    "02-headline": { "stato": "completato", "ts": "2026-06-23T09:14:00Z", "n_varianti": 3 },
    "03-seo": { "stato": "completato", "ts": "2026-06-23T09:18:00Z", "seo_path": "02-copy/articolo-seo.md" },
    "04-gate-copy": { "stato": "completato", "ts": "2026-06-23T09:20:00Z", "esito": "PASS", "n_rework": 0 },
    "05-gate-brand": { "stato": "completato", "ts": "2026-06-23T09:22:00Z", "esito": "PASS", "n_rework": 0 },
    "06-output": { "stato": "completato", "ts": "2026-06-23T09:23:00Z", "final_md": "02-copy/articolo-final.md", "final_html": "02-copy/articolo-final.html" }
  },
  "pronto_per_cf_r6": true,
  "stato_finale": "completato"
}
```

---

## Output finale (formato)

L'articolo viene consegnato in due formati:

1. **Markdown** (`articolo-final.md`): per knowledge base interne, Second Brain, GitHub Pages.
2. **HTML** (`articolo-final.html`): per blog WordPress/Webflow via 06-PLATFORM o consegna diretta.

Entrambi includono in header il `seo-report.json` come commento con: keyword_target,
keyword_density, meta_description, schema_type suggerito.

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0101 · brand: brand-agency · formato: articolo · 1200-1600 parole
· keyword: "content marketing che converte" · canali: blog, newsletter seed

**Passo 0 (dry-run):** CF-R4-WRITE legge brief → outline con H1 + 4 H2 + stima 1350 parole.
Committente: `show_outline: false` → procede a passo 1 direttamente.

**Passo 1 (draft):** CF-R4-WRITE — hook "Stai pubblicando ogni giorno, ma il fatturato
non si muove. Perché?" → corpo 4 sezioni → chiusura strutturale "Il passo successivo
è smettere di produrre contenuto e iniziare a costruire percorsi". 1387 parole. Auto-verifica: PASS.

**Passo 2 (headline):** CF-R4-HEADLINE produce 3 varianti:
- "Il Gap che Svuota il Budget di Contenuto"
- "Pubblichi Ogni Giorno e Non Converti: Ecco Perché"
- "Content Marketing che Converte: Il Problema non è la Frequenza"

**Passo 3 (SEO):** CF-R4-SEO — keyword "content marketing che converte" in H1, H2-1, meta;
density 1.8%; meta_description 158 caratteri. Nessuna modifica strutturale al testo.

**Passo 4 (GATE-COPY):** CF-R4-QA — 7/7 campi PASS. Hook in righe 1-2 (tipo domanda-provocatoria). PASS.

**Passo 5 (GATE-BRAND):** CF-R4-QA — 5 campioni tono: frasi brevi, verbi attivi, zero "forse".
Nessuna parola_vietata. PASS.

**Passo 6 (output):** CF-R4-COORD → `articolo-final.md` + `articolo-final.html`.
state.json: `pronto_per_cf_r6: true`. Lead time: 23 minuti.

---

## Connessioni

- [[cf-r4-coord]] · `agenti/cf-r4-coord.md` — orchestra questo workflow
- [[cf-r4-write]] · `agenti/cf-r4-write.md` — passi 0 e 1
- [[cf-r4-headline]] · `agenti/cf-r4-headline.md` — passo 2
- [[cf-r4-seo]] · `agenti/cf-r4-seo.md` — passo 3
- [[cf-r4-qa]] · `agenti/cf-r4-qa.md` — passi 4 e 5
- [[CF-R6-QA-Gate]] · gate globale indipendente dopo questo workflow
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §5(c) WF-ARTICOLO pipeline end-to-end
