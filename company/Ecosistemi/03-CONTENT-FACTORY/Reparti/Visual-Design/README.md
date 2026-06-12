> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 2 (CF-R4)

# CF-R4 — VISUAL & DESIGN

> Reparto L2 di 03-CONTENT-FACTORY · Coordinatore: `CF-R4-A01-visual-lead`
> Fonte: dossier 03 §2 (CF-R4), §4a, §4d, §5, §6.

---

## Cosa fa

Produce **caroselli IG, thumbnail, grafiche statiche, template brand**. È il custode del
brand-kit registry: ogni brand della holding (DE/agency, Mentalità Brutale, education,
canali YT, libri KDP, clienti agency) ha la propria identità visiva mantenuta qui.

CF-R4 è il reparto più maturo dell'intera Content-Factory: la carousel-factory
(`Workfolw crea caroselli à/carousel-factory/`) è l'asset core già funzionante — va
wrappato in `cf-carousel`, NON riscritto (ADR-003, regola wrap-non-riscrittura).

### Org interna

| Livello | Team | Contenuto | Owner |
|---|---|---|---|
| L3 | **WF-CAROSELLO** | carousel-factory: slide copy → prompt/design/render → PNG 1080x1350 + caption | CF-R4-A02-slide-copywriter |
| L3 | **WF-THUMB** | thumbnail/copertine: 3 concept → generazione (Canva/Higgsfield) → varianti A/B → resize multi-formato | CF-R4-A03-prompt-engineer |
| L3 | **WF-BRANDKIT** | crea e mantiene `brands/<slug>/` (palette, font, logo, voice, esempi, template Canva) | CF-R4-A06-brandkit-keeper |
| L4 | T-canva-export | export-design nei formati richiesti via Canva MCP | CF-R4-A04-canva-operator |
| L4 | T-resize | declinazioni 1080x1350 / 1080x1920 / 1280x720 per piattaforma | CF-R4-A05-render-operator |
| L4 | T-asset-library | upload-asset, organizzazione cartelle Canva per brand (upload-asset-from-url, create-folder) | CF-R4-A04-canva-operator |

### Agenti L5 (schede complete in `../../Agenti/`)

| ID | Ruolo | Tier |
|---|---|---|
| CF-R4-A01-visual-lead | coordina caroselli/thumbnail/grafiche, gestisce il brand-kit registry | sonnet |
| CF-R4-A02-slide-copywriter | copy slide: hook/body/CTA da formule hook/cta-formulas di carousel-factory | sonnet |
| CF-R4-A03-prompt-engineer | prompt immagine ultra-specifici (Gemini/Higgsfield) per slide e thumbnail | sonnet |
| CF-R4-A04-canva-operator | generate-design, brand templates, export via Canva MCP | haiku |
| CF-R4-A05-render-operator | render Puppeteer (render.mjs), resize, ottimizzazione file | wasm/haiku |
| CF-R4-A06-brandkit-keeper | crea/aggiorna brand_kit, sincronizza con Canva brand kits via `list-brand-kits` | haiku |

---

## Come si collega

**Inbound:**
- `CF-R1` → `brief.json` per ogni pezzo (angle, hook type, n. slide, canale, brand).
- `CF-R3` → copy slide / headline già scritto (per WF-CAROSELLO, fase 02-copy).
- `04-MARKETING` → copy APSOC validato per slide di conversione (CTA slide finale).
- `cf/brand-kits` (BRAIN) → brand_kit e template Canva del tenant.

**Outbound:**
- PNG 1080x1350 (caroselli) / varianti thumbnail → CF-QA-A01 (3 gate sequenziali).
- Manifest deliverable → CF-R5/WF-PUBLISH o WF-DELIVERY via handoff contract.
- Brand-kit aggiornato → `brands/<slug>/` e namespace `cf/brand-kits`.

**Engine layer (registry §5 del dossier):**
- `carousel-design / brand-template / export` → Canva MCP (`mcp__claude_ai_Canva__*`).
- `html-to-png / carousel-render` → puppeteer-render (`render.mjs`).
- `slide-image` (qualità top) → gemini-img (oggi manuale → ramo A WF-CAROSELLO).
- `image-4k / product-shoot` → higgsfield (quando collegato).

---

## Come si ATTIVA e RAGIONA

**Attivazione:** su brief approvato da CF-R1 (WF-CAROSELLO, WF-THUMB) oppure su
richiesta diretta del brand-kit keeper (WF-BRANDKIT, task di manutenzione).

**Logica WF-CAROSELLO (3 rami paralleli):**
1. Slide copy: CF-R4-A02 usa le formule hook/CTA di `carousel-factory/context/` — hook
   in slide 1, body progressivo, CTA misurabile in slide finale.
2. Design → 3 rami alternativi:
   - Ramo A: prompt ultra-specifico (CF-R4-A03) → generazione immagine Gemini (manuale oggi).
   - Ramo B: `generate-design-from-brand-template` via Canva MCP → `perform-editing-operations` → `export-design`.
   - Ramo C: slides.html + render.mjs Puppeteer → PNG.
3. Gate: GATE-FORMATO (1080x1350, ≤8 slide+cover, peso<8MB, contrasto leggibile,
   safe-area) → GATE-BRAND (palette/font/logo vs brand_kit) → GATE-COPY-APSOC.

**Logica WF-THUMB:**
1. CF-R4-A03 genera 3 concept testuali (composizione, emozione, testo overlay).
2. Generazione via Canva o Higgsfield image-4k.
3. Varianti A/B per concept scelto dal committente → T-resize per tutti i formati richiesti.
4. GATE-FORMATO: leggibilità a 10%, peso, safe-area → GATE-BRAND.

**Failure handling:** template Canva non trovato → fallback a render Puppeteer (MAI
silenzioso — loggato in trace.jsonl); brand_kit mancante → blocco + richiesta WF-BRANDKIT
prima di procedere; 2 gate falliti → escalation CF-R4-A01 + `cf/failures`.

## KPI del reparto

| KPI | Definizione | Direzione |
|---|---|---|
| Throughput caroselli | pezzi 1080x1350 consegnati per settimana | ↑ |
| First-pass GATE-BRAND | % output senza correzioni palette/font | ↑ |
| Costo per carosello | token + crediti engine per pezzo (per ramo) | ↓ |
| Brand_kit attivi nel registry | tenant registrati con template Canva collegati | ↑ |

## Connessioni

- [[ECOSISTEMA]] — `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`
- [[BACKBONE]] — `company/Ecosistemi/03-CONTENT-FACTORY/BACKBONE.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §2, §4a, §4d, §5, §6
- `Workfolw crea caroselli à/carousel-factory/` — asset core del WF-CAROSELLO (wrappare, NON riscrivere)

*Fonte: dossier 03 §2, §4, §5, §6 · Aggiornato: 2026-06-11*
