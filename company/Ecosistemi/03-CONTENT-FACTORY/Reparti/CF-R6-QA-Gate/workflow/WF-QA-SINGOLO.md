---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R6 #qa #gate #singolo #apsoc #mandato #post-produzione
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-QA-SINGOLO — Review Completa Singolo Deliverable

> **Reparto:** CF-R6 QA & Gate · **Area:** Post-Produzione
> **Gate sequenziali obbligatori:** FORMATO → BRAND → COPY → MANDATO
> **Invariant:** 1 gate ROSSO ferma il pezzo; 2 rework falliti → escalation + `cf/failures`

---

## Scopo

Review completa di un singolo deliverable (video, carosello, testo, thumbnail, grafica)
attraverso i 4 gate sequenziali di CF-R6. Output: verdetto PASS o FAIL con motivo
strutturato in `orders/<id>/05-qa/verdict.json`. Solo i deliverable con verdetto PASS
possono procedere a CF-R7 (Pubblicazione & Distribuzione).

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate / Condizione |
|---|---|---|---|---|---|
| 0 | Prelievo dalla coda | CF-R6-COORD | `cf/qa` con `pronto_per_cf_r6: true` | Sessione QA aperta | state.json fasi produzione complete |
| 1 | GATE-FORMATO | CF-R6-FORMAT | path deliverable + specifiche ordine | `gate_formato` in verdict.json | PASS → passo 2 · FAIL → passo 5 |
| 2 | GATE-BRAND | CF-R6-BRAND | path deliverable + brand_kit.json | `gate_brand` in verdict.json | PASS → passo 3 · FAIL → passo 5 |
| 3 | GATE-COPY APSOC | CF-R6-COPY | copy_path + icp.json | `gate_copy` in verdict.json | PASS → passo 4 · FAIL → passo 5 |
| 4 | MANDATO COMPLIANCE | CF-R6-MANDATO | copy_path + deliverable | `mandato_compliance` in verdict.json | PASS → passo 6 · FAIL → passo 5 |
| 5 | REWORK | CF-R6-REWORK | gate_fallito + motivo strutturato | specifica rework → reparto produttore | n_rework < 2 → rientro da passo 0 · n_rework ≥ 2 → escalation |
| 6 | VERDETTO PASS | CF-R6-COORD | tutti e 4 i gate verdi | verdict.json PASS + state.json aggiornato | CF-R7 abilitato |

---

## Regole sequenziali (non negoziabili)

1. I gate si eseguono nell'ordine fisso: FORMATO → BRAND → COPY → MANDATO.
2. Al primo gate FAIL, la sequenza si interrompe: i gate successivi non vengono eseguiti.
3. Il Mandato viene eseguito solo se i 3 gate precedenti sono PASS: non è opzionale, ma
   ha senso solo su un deliverable già conforme a formato, brand e struttura copy.
4. Dopo il rework, il deliverable rientra dal passo 0 (prelievo): WF-QA-SINGOLO
   ricomincia dall'inizio, non dal gate che aveva fallito. Questo garantisce che
   le correzioni non introducano nuovi problemi in gate già passati.
5. Il PASS è unanime: tutti e 4 i gate devono essere verdi. Non esiste "quasi PASS".

---

## Gate FORMATO (passo 1) — criteri per formato

| Formato | Dimensioni | Peso | Codec | Struttura |
|---|---|---|---|---|
| Carosello IG | 1080×1350 px | ≤8 MB/slide | PNG | ≤8 slide + cover; safe-area libera |
| Video Reel/Shorts | 720×1280 px (9:16) | — | h264 o h265 | ≤60s; loudness -14 LUFS ±2 dB |
| Video TikTok | 720×1280 px (9:16) | — | h264 o h265 | ≤3min; loudness -14 LUFS ±2 dB |
| Video YouTube | 1280×720 o 1920×1080 px (16:9) | — | h264 o h265 | durata da ordine; loudness -14 LUFS ±2 dB |
| Thumbnail | 1280×720 px | ≤2 MB | PNG o JPG | testo leggibile al 10% larghezza |
| Grafica statica | da ordine | da ordine | PNG o JPG | margini brand_kit rispettati |

---

## Gate BRAND (passo 2) — criteri parametrici

Il gate legge `brand_kit.json` dell'ordine — non ha criteri fissi.

- Palette: colori dominanti campionati (5 punti per visual) confrontati vs
  `brand_kit.visual.palette.primary + .accent + .bg` con tolleranza ±5% su HEX.
- Font: `brand_kit.visual.font.display` per headline; `.body` per testi corpo.
- Logo: se richiesto dal brief, presente e non distorto.
- Tone of voice: 3-5 frasi campionate confrontate vs `brand_kit.voice.esempi_si/esempi_no`;
  assenza di `brand_kit.voice.parole_vietate`.

---

## Gate COPY (passo 3) — criteri APSOC

- **Hook**: presente nella posizione attesa (video: ≤3s; carosello: prima slide; testo: prima riga).
- **Problema + promessa**: il problema evocato è in `icp.dolori`; la promessa è proporzionata.
- **Social proof**: solo prova verificabile e concreta (screenshot, dato con fonte); nessuna
  social proof vaga ("molti clienti...") o senza attribuzione.
- **CTA**: esattamente 1 CTA principale e misurabile; 0 CTA → FAIL; 2+ CTA → FAIL.

---

## Mandato compliance (passo 4) — criteri invariant

- Zero affermazioni di risultato senza prova inclusa nel deliverable.
- Zero claim non verificabili (superlativi assoluti, statistiche senza fonte, garanzie
  senza condizioni).
- Zero genericità strutturale (frasi applicabili a qualsiasi nicchia senza modifiche).

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0061",
  "workflow": "WF-QA-SINGOLO",
  "fasi": {
    "00-prelievo":     { "stato": "completato", "ts": "2026-06-23T14:30:00Z" },
    "01-gate-formato": { "stato": "completato", "ts": "2026-06-23T14:32:00Z", "esito": "PASS" },
    "02-gate-brand":   { "stato": "completato", "ts": "2026-06-23T14:36:00Z", "esito": "PASS" },
    "03-gate-copy":    { "stato": "completato", "ts": "2026-06-23T14:40:00Z", "esito": "PASS" },
    "04-mandato":      { "stato": "completato", "ts": "2026-06-23T14:44:00Z", "esito": "PASS" },
    "05-qa":           { "stato": "completato", "ts": "2026-06-23T14:45:00Z", "verdetto": "PASS" }
  },
  "n_rework": 0,
  "pronto_per_cf_r7": true
}
```

**Esempio con rework (passo 5 attivato):**
```json
{
  "order_id": "CF-2026-0062",
  "workflow": "WF-QA-SINGOLO",
  "fasi": {
    "00-prelievo":     { "stato": "completato", "ts": "2026-06-23T14:30:00Z" },
    "01-gate-formato": { "stato": "completato", "ts": "2026-06-23T14:32:00Z", "esito": "PASS" },
    "02-gate-brand":   { "stato": "completato", "ts": "2026-06-23T14:36:00Z", "esito": "PASS" },
    "03-gate-copy":    { "stato": "completato", "ts": "2026-06-23T14:40:00Z", "esito": "FAIL", "motivo": "hook assente nella prima slide" },
    "04-mandato":      { "stato": "non_eseguito", "ts": null },
    "05-rework":       { "stato": "in_corso", "ts": "2026-06-23T14:41:00Z", "destinatario": "CF-R4", "n_rework": 1 }
  },
  "n_rework": 1,
  "pronto_per_cf_r7": false
}
```

---

## Ciclo rework integrato

```
FAIL gate N
    │
    ▼
CF-R6-REWORK
  specifica strutturata → reparto produttore
  incremento n_rework in state.json
    │
    ▼ (rework eseguito)
WF-QA-SINGOLO ricomincia da passo 0
    │
n_rework = 2 dopo secondo FAIL?
    │ SÌ
    ▼
CF-R6-COORD: escalation L1-POST
  + entry cf/failures (ReasoningBank)
  + notifica CF-Director
  → nessun terzo rework senza autorizzazione L1-POST
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0061 · brand: mentalita-brutale · formato: carosello-ig · 8 slide

**Passo 0:** CF-R6-COORD preleva da `cf/qa`; state.json fasi produzione complete.

**Passo 1 — FORMAT:** 9 PNG (8 slide + cover), ogni file 1080×1350 px, peso max 6.8 MB,
safe-area libera → GATE-FORMATO PASS.

**Passo 2 — BRAND:** palette campionata #1a1a1a + #ff4444 → CONFORME; font Anton+Inter
→ CONFORME; tone "Smetti di postare contenuti inutili" → match esempi_si → CONFORME
→ GATE-BRAND PASS.

**Passo 3 — COPY:** hook slide 1 presente → PASS; dolore icp evocato slide 2 → PASS;
screenshot DM cliente slide 6 → PASS; 1 CTA slide 8 → PASS → GATE-COPY PASS.

**Passo 4 — MANDATO:** 0 claim non verificabili; 0 genericità; prova in slide 6 → PASS
→ MANDATO COMPLIANCE PASS.

**Passo 6 — VERDETTO:** PASS. `orders/CF-2026-0061/05-qa/verdict.json` completato.
state.json → `"05-qa": "completato"`, `pronto_per_cf_r7: true`.
CF-R7 notificato e abilitato per questo deliverable.

---

## Connessioni

- [[cf-r6-coord]] · `agenti/cf-r6-coord.md` — orchestra l'intero workflow
- [[cf-r6-format]] · `agenti/cf-r6-format.md` — passo 1
- [[cf-r6-brand]] · `agenti/cf-r6-brand.md` — passo 2
- [[cf-r6-rework]] · `agenti/cf-r6-rework.md` — gestisce passo 5 su ogni FAIL
- [[CF-R6-QA-Gate/ARCHITETTURA]] · `ARCHITETTURA.md` — topologia e gate dettagliati
