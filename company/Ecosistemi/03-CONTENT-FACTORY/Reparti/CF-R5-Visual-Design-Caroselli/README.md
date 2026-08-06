---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #visual #design #caroselli #CF-R5 #produzione
Created: 2026-06-19
Last updated: 2026-06-19
---

# CF-R5 — Visual & Design / Caroselli

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R5`
> **Standard:** CF-grade (ADR-007) · **Wrappa carousel-factory ATTIVO (ADR-003 — NON modificare il runtime)**

---

## Missione

Produrre **caroselli IG, thumbnail, grafiche statiche e template brand** su ogni ordine
validato che richiede output visivo. L'asset più maturo di Digital Empire — il
`carousel-factory` — viene wrappato tramite la skill `cf-carousel` senza toccare il
runtime originale (ADR-003: wrap, mai riscrittura).

Il reparto lavora su quattro engine paralleli: **Canva MCP** (via `cf-r5-canva`) per i
template brand, **render locale** (via `cf-r5-render` + `render.mjs` Puppeteer) per la
pipeline HTML→PNG ad alto controllo, **prompt AI diretto** (Ramo A, Gemini/Higgsfield),
e **Arena Agent Workspace** (Ramo D, via `cf-carousel-arena`). La scelta tra gli engine
è responsabilità di `cf-r5-coord` in base al brand_kit e al brief ricevuto.

**Stato reale (2026-08-06, non presunto)**: dei 4 rami, solo il **Ramo D è stato
verificato con un output reale** (primo carosello Preventa, `orders/
CF-2026-PREVENTA-001/`, [[CP-20260805-013]]). Rami A/B/C restano progettati ma mai
eseguiti — nessuna prova di run prima di questa data. Vedi ARCHITETTURA.md per il
dettaglio del Ramo D.

---

## Cosa fa il reparto

1. **Riceve il brief** da CF-R1 con `struttura_formato: slide-deck` e `icp.dolori`.
2. **Scrive il copy slide** (hook/body/CTA) con `cf-r5-slidecopy` usando le formule del carousel-factory.
3. **Genera i visual** tramite tre rami paralleli: prompt Gemini/Higgsfield (ramo A),
   template Canva brand (ramo B), HTML→render.mjs PNG (ramo C).
4. **Applica i gate** GATE-FORMATO (dimensioni, peso, contrasto, safe-area) e GATE-BRAND
   (palette, font, logo) tramite `cf-r5-qa`, che blocca e non suggerisce.
5. **Ridimensiona** negli 4 formati standard con `cf-r5-resize`.
6. **Apprende** dalla correlazione hook visivo/composizione con CTR tramite `cf-r5-learn`.

## Cosa NON fa

- Non scrive copy di conversione APSOC: quello è 04-MARKETING L2.1.
- Non pubblica sui canali social: quello è CF-R7 (Pubblicazione & Distribuzione).
- Non valida il brand_kit: quello è CF-R2 (Brand-Kit & Tenant Registry).
- Non genera script video o articoli: quello è CF-R3/CF-R4.
- Non modifica il runtime `carousel-factory/` (ADR-003 — vincolo assoluto).
- Non genera contenuto senza brand_kit + icp (pattern 11 CF-DE: zero contenuto hard-coded su singolo brand).

---

## Roster del reparto (10 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R5-COORD` | Coordinatore Visual & Design | `agenti/cf-r5-coord.md` | coordinator | sonnet | Orchestra i 4 workflow; sceglie Canva vs render locale; riporta a L1-PROD |
| `CF-R5-QA` | Verificatore Gate Visual | `agenti/cf-r5-qa.md` | verifier | sonnet | GATE-FORMATO + GATE-BRAND; BLOCCA e non suggerisce |
| `CF-R5-SLIDECOPY` | Slide Copywriter | `agenti/cf-r5-slidecopy.md` | worker | sonnet | Copy slide caroselli hook/body/CTA da formule carousel-factory; applica icp.dolori |
| `CF-R5-PROMPT` | Prompt Engineer Visual | `agenti/cf-r5-prompt.md` | worker | sonnet | Prompt immagini ultra-specifici Gemini/Higgsfield: composizione, stile, palette, negative prompt |
| `CF-R5-CANVA` | Canva Operator | `agenti/cf-r5-canva.md` | worker | haiku | generate-design, brand-template, perform-editing-operations, export via MCP Canva |
| `CF-R5-RENDER` | Render Operator | `agenti/cf-r5-render.md` | worker | wasm/haiku | Render Puppeteer render.mjs HTML→PNG 1080x1350; resize; ottimizzazione file |
| `CF-R5-CONCEPT` | Concept & Art Director | `agenti/cf-r5-concept.md` | worker | sonnet | 3 concept visivi per thumbnail; A/B testing concept |
| `CF-R5-ASSET` | Asset Library Manager | `agenti/cf-r5-asset.md` | worker | haiku | Upload-asset Canva per brand; cartelle organizzate; naming convention |
| `CF-R5-RESIZE` | Resize & Format Specialist | `agenti/cf-r5-resize.md` | worker | haiku | Declinazioni 1080x1350/1080x1920/1280x720/1080x1080 |
| `CF-R5-LEARN` | Visual Performance Analyst | `agenti/cf-r5-learn.md` | worker | sonnet | Correla hook visivo/composizione con CTR; pattern in `cf/patterns` |

---

## Workflow del reparto (4 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-CAROSELLO** | `workflow/WF-CAROSELLO.md` | Carosello IG batch da brief a PNG + caption [WRAPPA carousel-factory] | GATE-FORMATO 1080x1350 ≤8 slide <8MB; GATE-BRAND palette/font/logo |
| **WF-THUMBNAIL** | `workflow/WF-THUMBNAIL.md` | 3 concept → generazione → resize A/B | GATE-FORMATO leggibilità testo a 10%; GATE-BRAND |
| **WF-GRAFICA-STATICA** | `workflow/WF-GRAFICA-STATICA.md` | Grafiche one-shot ads/banner/post | GATE-FORMATO dimensioni esatte canale |
| **WF-BRANDKIT-VISUAL** | `workflow/WF-BRANDKIT-VISUAL.md` | Template Canva per ogni formato standard su richiesta CF-R2 | Template tutti i 4 formati standard approvati CF-R2-QA |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/design` | Deliverable caroselli e grafiche; state.json fasi 03-design/04-render |
| `cf/thumbnails` | Concept e thumbnail per ordine; varianti A/B; scelta committente |
| `cf/graphics` | Grafiche statiche; resize multi-formato; asset brand Canva |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Caroselli prodotti/ciclo per brand | CF-R5-COORD | N. caroselli con GATE verde per brand nel ciclo; [DM] baseline |
| GATE-FORMATO first-pass rate | CF-R5-QA | N. deliverable GATE-FORMATO PASS al primo tentativo / tot prodotti |
| Costo per carosello per ramo | CF-R5-COORD | Crediti engine per carosello distinti per ramo A/B/C; [DM] baseline |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-R1 (Strategia & Brief) | `brief.json` con struttura_formato slide-deck, angle, hook_type, icp.dolori |
| ← riceve da | CF-R2 (Brand-Kit Registry) | `brand_kit.json` validato per ogni tenant: palette, font, logo, canva_brand_template_ids |
| ← riceve da | CF-R4 (Produzione Testuale) | Caption+hashtag per i caroselli (quando CF-R4-CAPTION è owner) |
| → consegna a | CF-R6 (QA & Gate) | PNG slides + caption per GATE-COPY-APSOC indipendente |
| → consegna a | CF-R7 (Pubblicazione) | Deliverable con gate verde + manifest per publish |
| → consegna a | CF-R2 (Brand-Kit Registry) | Template Canva creati via WF-BRANDKIT-VISUAL (sync asset) |

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- ADR-003 (wrap, non riscrittura): `carousel-factory/` runtime intatto, sempre.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R5`
- [[CF-R1-Strategia-Brief]] · fornitore brief.json con struttura_formato slide-deck
- [[CF-R2-Brand-Kit-Tenant-Registry]] · fornitore brand_kit + canva_brand_template_ids
- [[CF-R6-QA-Gate]] · verificatore GATE-COPY-APSOC indipendente dalla produzione
