# 🏭 03 — ECOSISTEMA CONTENT-FACTORY (CF-DE)

> Dossier dell'ecosistema 03 di EMPIRE OS. Modello di riferimento: Content Factory di Exponium
> (AION GROUP) — da **superare**, non da copiare. Versione: 1.0 · Creato: 2026-06-10 ·
> Dipende da: `00-PIANO-MAESTRO.md` (gerarchia LX→L5, Backbone, 13 pattern non negoziabili).

---

## 0. Missione, DONE WHEN, differenza vs CF Exponium

### Missione
Produrre **contenuti multi-formato, multi-brand, multi-cliente** per TUTTI gli ecosistemi di
EMPIRE OS e per i clienti esterni: caroselli IG, video UGC/avatar, articoli, newsletter,
thumbnail, grafiche, pubblicazione schedulata multi-canale. È la fabbrica trasversale della
holding: chiunque (Agency, Info-Business, Multi-Business, Marketing, la stessa DE) emette un
**ordine** e riceve deliverable conformi a gate di qualità.

### DONE WHEN
1. Contratto di ordine standard attivo: ogni richiesta entra come `{committente, brand_kit, icp, formato, quantità, deadline, budget}` e produce `orders/<id>/state.json + trace.jsonl`.
2. Brand-kit registry operativo con ≥4 brand (DE/agency, Mentalità Brutale, education/corsi, ≥1 cliente o canale).
3. I 5 workflow chiave (carosello, video, articolo, thumbnail, publish) girano end-to-end con dry-run e QA gate; almeno carosello + publish con output REALE.
4. Engine layer multi-motore attivo: aggiungere un motore = 1 riga di registry, zero modifiche all'orchestrazione.
5. Swarm mass-production: un batch ≥10 pezzi prodotto in parallelo con budget guard che blocca PRIMA di sforare.
6. Zero asset orfani: tutti i path della sezione 6 mappati a un reparto con azione completata.

### Differenza esplicita vs CF Exponium (il punto in cui la superiamo)

| Dimensione | CF Exponium (AION) | CF-DE (questo ecosistema) |
|---|---|---|
| Scopo | **Mono-scopo**: solo il lancio Exponium | **Multi-tenant**: N committenti, ogni ordine porta il suo `brand_kit` + `icp` |
| Brand | 1 (Exponium, voce di Marco, 1 ICP) | Registry di brand: DE, Mentalità Brutale, clienti agency, canali YT, libri KDP |
| Formati | Video/immagini (reel UGC, avatar) | Video + caroselli + testuale + grafiche + email-ready |
| Distribuzione | D6 consegna interna al team lancio | Reparto L2 dedicato: Pubblicazione & Distribuzione multi-canale schedulata |
| Autorità suprema | Dipartimento Exponium (compliance prodotto) | Mandato Empire + brand gate **parametrico** (il gate legge il brand_kit dell'ordine, non un mandato fisso) |
| Motori | Higgsfield (attivo) + HeyGen (pronto) | Higgsfield + HeyGen + **Canva MCP + ffmpeg + TTS + render Puppeteer** nello stesso registry |
| Cosa eredita identico | — | state.json + trace.jsonl per ordine, swarm con budget guard, QA a cancelli (68 check → estesi), engines.sh come pattern |

Regola: tutto ciò che in CF Exponium era hard-coded sul brand Exponium qui diventa **input**.
Un workflow che non accetta `brand_kit` + `icp` non è conforme (pattern 11 del Piano Maestro).

---

## 1. Posizione nella holding — handoff con TUTTI gli ecosistemi

CF-DE è l'ecosistema più trasversale: non ha clienti propri, ha **committenti**.

### Contratto di ordine (unico punto d'ingresso)

```json
{
  "order_id": "CF-2026-0001",
  "committente": "01-AGENCY | 02-INFO | 04-MKT | 05-MB-YT | 05-MB-KDP | cliente:<slug> | DE-interno",
  "brand_kit": "brands/<slug>/brand-kit.json",
  "icp": "brands/<slug>/icp.json",
  "formato": "carosello-ig | video-ugc | video-avatar | articolo | newsletter | thumbnail | grafica | publish-only",
  "quantita": 10,
  "deadline": "YYYY-MM-DD",
  "budget": {"crediti_engine": 120, "tier_max": "sonnet"},
  "note": "vincoli specifici, CTA richiesta, canali di destinazione"
}
```

Nessun lavoro parte senza ordine valido. Il CF-Conductor (L1) rifiuta ordini incompleti
(escalation al committente, non improvvisazione).

### Schema brand_kit (il cuore del multi-tenant)

```json
{
  "slug": "mentalita-brutale",
  "nome": "Mentalità Brutale",
  "handle": {"ig": "@mentalita.brutale", "tiktok": null, "yt": null},
  "visual": {
    "palette": {"primary": "#hex", "accent": "#hex", "bg": "#hex"},
    "font": {"display": "Anton", "body": "..."},
    "logo": "brands/mentalita-brutale/assets/LOGO.png",
    "stile": "dark, gradiente rosso/argento",
    "canva_brand_template_ids": []
  },
  "voice": {
    "tono": "diretto, brutale, zero fronzoli",
    "esempi_si": ["..."], "esempi_no": ["..."],
    "parole_vietate": []
  },
  "soul_id": null,
  "canali": [{"tipo": "ig", "publisher": "mentalita_orchestrator.py", "review_umana": true}]
}
```

`icp.json` per tenant: dolori, desideri, obiezioni, livello di consapevolezza, linguaggio.
Seed iniziale: i 4 brand già presenti in `carousel-factory/brands/` (brand-agency,
brand-education, brand-personal, mentalita-brutale).

### Handoff contract (formato BUS, pattern 2 del Piano Maestro)

```json
{
  "from": "CF-R4/WF-CAROSELLO", "to": "CF-R5/WF-PUBLISH",
  "order_id": "CF-2026-0001",
  "payload": {"asset_dir": "orders/CF-2026-0001/06-delivery/", "manifest": "manifest.json"},
  "acceptance_criteria": ["3 gate verdi in state.json", "caption presente per ogni canale richiesto"],
  "on_reject": "torna a CF-R4 con motivo strutturato; 2 reject → escalation CF-A00"
}
```

### Matrice handoff (chi ordina cosa / cosa riceve CF)

| Ecosistema | Ordina a CF | Fornisce a CF | Canale |
|---|---|---|---|
| 01 AGENCY | Contenuti per i clienti (deliverable "Content Factory €3.500"), creative per outreach, case study visuali | brand_kit + icp dei clienti, accesso account cliente | BUS, contract `agency→cf` |
| 02 INFO-BUSINESS | Asset lancio: caroselli, VSL/video corso, email-ready, grafiche sales page | calendario lancio, offerta, price point | BUS, priorità alta in finestra lancio |
| 04 MARKETING | Creative per ads (ad-creative), visual A/B test | **Copy APSOC validato** (Copy Guild — il copy "che vende" è SEMPRE di Marketing; CF scrive solo copy strutturale: slide, caption, script base) | BUS bidirezionale: CF chiede copy, MKT chiede creative |
| 05 MULTI-BUSINESS | Video YouTube (script→render→thumbnail), copertine/interni KDP, creative e-commerce | brand_kit canale/libro, nicchia, formato piattaforma | BUS, batch ricorrenti |
| 06 PLATFORM | (raro) grafiche per siti | Tooling: render farm locale, fix script Puppeteer/ffmpeg, hosting asset | ticket `cf→platform` |
| 07 FORGE | — | Nuove skill/agenti CF quando i KPI calano o serve un formato nuovo | richiesta `cf→forge` con spec |
| 08 INTELLIGENCE | — | Brief di ricerca: trend, hook che funzionano, analisi competitor; riceve da CF ogni output da loggare in wiki | `intel→cf` brief; `cf→wiki` log obbligatorio |
| 09 OPERATIONS | — | Runtime swarm, scheduling cron, storage asset, cost guard centrale | infrastruttura condivisa |
| LX/L0 (Board) | Contenuti corporate DE | Mandato Empire (gate non parametrici: pricing policy, "prove non promesse") | governance |

Regola di precedenza: in conflitto di coda, decide il CF-Conductor con criterio
`deadline → revenue impact (Agency/Lanci) → interno`. Escalation al Board via hive-mind solo
se due committenti hanno la stessa priorità e il budget non copre entrambi.

---

## 2. Reparti L2

Cinque reparti. Ogni team segue lo schema canonico (pattern 1): coordinator + workers,
I/O espliciti, acceptance criteria, failure handling, shared_state.

### CF-R1 — STRATEGIA CONTENUTI
- **Missione:** trasformare l'ordine in un piano eseguibile: brief, angle, calendario, assegnazione formati. Nessun contenuto si produce senza brief approvato.
- **Team L3 (workflow):**
  - `WF-BRIEF` — intake ordine: valida contratto, carica brand_kit+icp, produce `brief.json` (angle, hook type, struttura, canali, vincoli).
  - `WF-CALENDAR` — piano editoriale multi-brand: slot di pubblicazione, mix di formati, ricorrenze (usa skill content-strategy).
- **Team L4 (funzioni):** `T-hook` (selezione formula hook da libreria), `T-angle` (3 angle alternativi per brief), `T-trend-intake` (riceve brief trend da INTELLIGENCE).

### CF-R2 — PRODUZIONE VIDEO
- **Missione:** produrre video pronti alla pubblicazione: UGC (Higgsfield), avatar/talking-head (HeyGen), short-form montati (ffmpeg+TTS). Eredita la pipeline creativa CF Exponium: Soul ID → Image 4K → Motion → Montaggio.
- **Team L3:**
  - `WF-VIDEO-UGC` — pipeline Higgsfield completa (soul-id ricorrente per brand → immagini 4K → motion → montaggio).
  - `WF-VIDEO-AVATAR` — pipeline HeyGen (script → avatar → render) per talking-head/spokesperson per brand.
  - `WF-SHORTFORM` — montaggio reel/TikTok/Shorts da asset esistenti: cut, sottotitoli, audio.
- **Team L4:** `T-voiceover` (TTS), `T-subtitle` (caption burn-in), `T-montaggio` (ffmpeg: concat, crop 9:16/1:1/16:9, loudness), `T-render-queue` (coda render + cost guard, eredita D3 CF).

### CF-R3 — PRODUZIONE TESTUALE
- **Missione:** articoli, newsletter, script video, descrizioni — testo lungo e strutturato. Il copy di conversione (sales, ads) resta a MARKETING: CF-R3 produce contenuto, MARKETING produce persuasione; sui pezzi ibridi (newsletter con CTA) CF scrive il corpo e chiede a MARKETING il blocco APSOC.
- **Team L3:**
  - `WF-ARTICOLO` — brief → outline → draft → SEO/AI-SEO pass → formato output (md/html).
  - `WF-NEWSLETTER` — brief → corpo → blocco CTA (handoff MKT) → email-ready.
  - `WF-SCRIPT` — script video (YouTube lungo, reel, VSL base) per CF-R2.
- **Team L4:** `T-caption` (caption+hashtag per canale), `T-headline` (varianti titolo), `T-repurpose` (1 articolo → N pezzi derivati).

### CF-R4 — VISUAL & DESIGN
- **Missione:** caroselli IG, thumbnail, grafiche statiche, template brand. Custode del brand-kit registry.
- **Team L3:**
  - `WF-CAROSELLO` — l'asset più maturo di DE (carousel-factory): slide copy → prompt immagine (Gemini) o design Canva → render Puppeteer/export Canva → carosello completo + caption.
  - `WF-THUMB` — thumbnail YouTube/copertine: 3 concept → generazione (Canva MCP / image / Higgsfield image-4k) → varianti A/B → resize multi-formato.
  - `WF-BRANDKIT` — crea e mantiene `brands/<slug>/` (palette, font, logo, voice, esempi, template Canva collegati via list-brand-kits).
- **Team L4:** `T-canva-export` (export-design nei formati richiesti), `T-resize` (declinazioni 1080x1350/1080x1920/1280x720), `T-asset-library` (upload-asset, cartelle Canva per brand).

### CF-R5 — PUBBLICAZIONE & DISTRIBUZIONE
- **Missione:** portare i deliverable sui canali: IG, TikTok, LinkedIn, YouTube, Drive cliente. Schedulazione, adattamento per canale, verifica post-pubblicazione. (CF Exponium NON ha questo reparto: qui DE lo supera.)
- **Team L3:**
  - `WF-PUBLISH` — coda → slot calendario → adattamento (caption, hashtag, formato) → pubblicazione via orchestratori esistenti → verifica → log.
  - `WF-DELIVERY` — consegna a committente non-social: pacchetto in Drive/cartella cliente con manifest.
  - `WF-FEEDBACK` — raccolta performance post-pubblicazione → handoff a MARKETING Analytics e a `cf/patterns` (cosa funziona per quale brand).
- **Team L4:** `T-utm` (tracciamento link), `T-uploader` (upload per piattaforma), `T-postcheck` (screenshot/verifica live del post).

---

## 3. Roster agenti L5

Tier modello secondo 3-tier routing del Backbone (WASM/regex → Haiku → Sonnet; Opus solo su richiesta esplicita per QA finale o creative critiche).

| ID | Ruolo | Tipo | Tier |
|---|---|---|---|
| CF-A00-conductor | Riceve ordini, valida contratto, smista ai reparti, gestisce precedenze | coordinator (L1) | sonnet |
| CF-R1-A01-brief-lead | Coordina intake e brief | coordinator | sonnet |
| CF-R1-A02-brief-analyst | Parse ordine, carica brand_kit/icp, compila brief.json | worker | haiku |
| CF-R1-A03-angle-strategist | 3 angle + hook type da libreria formule | worker | sonnet |
| CF-R1-A04-calendar-planner | Piano editoriale, slot, mix formati | worker | sonnet |
| CF-R2-A01-video-lead | Coordina le 3 pipeline video, sceglie engine via capability | coordinator | sonnet |
| CF-R2-A02-soul-curator | Soul ID / personaggi ricorrenti per brand (Higgsfield) | worker | haiku |
| CF-R2-A03-image-operator | Generazione immagini 4K (Higgsfield) | worker | haiku |
| CF-R2-A04-motion-operator | Image→video motion (Higgsfield) | worker | haiku |
| CF-R2-A05-avatar-operator | Render HeyGen avatar/talking-head | worker | haiku |
| CF-R2-A06-editor-ffmpeg | Montaggio: cut, crop, subtitle, audio | worker | haiku |
| CF-R2-A07-voiceover | TTS voiceover per brand voice | worker | haiku |
| CF-R2-A08-render-queue | Coda render, stima costi, cost guard locale | worker | wasm/haiku |
| CF-R3-A01-text-lead | Coordina produzione testuale | coordinator | sonnet |
| CF-R3-A02-writer | Draft articoli/newsletter/script | worker | sonnet |
| CF-R3-A03-seo-optimizer | SEO + AI-SEO pass (skill seo, ai-seo) | worker | haiku |
| CF-R3-A04-repurposer | Derivati multi-formato da un pezzo madre | worker | haiku |
| CF-R4-A01-visual-lead | Coordina caroselli/thumbnail/grafiche | coordinator | sonnet |
| CF-R4-A02-slide-copywriter | Copy slide (hook/body/CTA da formule carousel-factory) | worker | sonnet |
| CF-R4-A03-prompt-engineer | Prompt immagine ultra-specifici (Gemini/Higgsfield) | worker | sonnet |
| CF-R4-A04-canva-operator | generate-design, brand templates, export via Canva MCP | worker | haiku |
| CF-R4-A05-render-operator | Render Puppeteer (render.mjs), resize, ottimizzazione file | worker | wasm/haiku |
| CF-R4-A06-brandkit-keeper | Crea/aggiorna brand_kit, sincronizza con Canva brand kits | worker | haiku |
| CF-R5-A01-publish-lead | Coordina coda pubblicazione e consegne | coordinator | sonnet |
| CF-R5-A02-channel-adapter | Adatta caption/formato per canale | worker | haiku |
| CF-R5-A03-publisher-social | Esegue publish IG/TikTok/LinkedIn (orchestratori Python) | worker | wasm/haiku |
| CF-R5-A04-delivery-packager | Pacchetto + manifest per consegna a committente | worker | haiku |
| CF-R5-A05-perf-collector | Raccoglie metriche post-publish → MKT Analytics + cf/patterns | worker | haiku |
| CF-QA-A01-gatekeeper | Esegue i 3 gate (formato/brand/copy) su ogni deliverable | worker (Quality Guild) | sonnet |
| CF-SENT-cost | Sentinel costi: blocca ordini oltre budget, alert al Conductor | sentinel always-on | wasm |
| CF-SENT-brand | Sentinel brand drift: campiona output vs brand_kit | sentinel always-on | haiku |

30 agenti. I sentinel sono istanze locali dei Sentinels di Backbone (Cost, Brand-Voice);
il gatekeeper appartiene alla Quality Guild trasversale.

---

## 4. Workflow chiave end-to-end

Tutti condividono lo stesso **project state** (eredità CF Exponium):

```
orders/<order_id>/
├── order.json          # il contratto
├── state.json          # fase corrente, gate superati, costi consumati
├── trace.jsonl         # ogni evento append-only {ts, agent, event, payload}
├── 01-brief/  02-copy/  03-design/  04-render/  05-qa/  06-delivery/
```

Regole comuni: **dry-run default** alla prima esecuzione (stima costi, zero effetti);
nessuna fase salta il gate precedente; ogni fallimento → `trace.jsonl` + `cf/failures`
(ReasoningBank); pubblicazione automatica con **review umana obbligatoria** finché il Board
non rimuove il vincolo (out-of-scope del Piano Maestro).

### (a) WF-CAROSELLO — carosello IG batch

```
ordine(quantità=N) → CF-A00 valida → WF-BRIEF (brand_kit+icp → brief.json per ciascun pezzo)
  → [swarm fan-out: N job paralleli]
     job: slide-copy (hook→body→CTA, formule carousel-factory)
          → ramo A: prompt Gemini per slide (PROMPT-SYSTEM.md)   [oggi: generazione manuale]
          → ramo B: Canva MCP create-design-from-brand-template → perform-editing → export 1080x1350
          → ramo C: HTML slides → render.mjs Puppeteer → PNG
     → GATE-FORMATO (1080x1350, ≤8 slide+cover, peso) → GATE-BRAND → GATE-COPY
     → caption+hashtag (T-caption) → 06-delivery/ o coda WF-PUBLISH
  → report batch aggregato (pezzi ok / rework / costo)
```
Dry-run: produce solo copy+prompt (ramo A completo senza generazione immagini) — già oggi
a costo zero. QA: gate su OGNI carosello, non sul batch.

| Fase | Owner | Input | Output | Gate |
|---|---|---|---|---|
| 01-brief | CF-R1-A02/A03 | order.json, brand_kit, icp | brief.json (angle, hook type, n. slide) | brief completo (campi obbligatori) |
| 02-copy | CF-R4-A02 | brief.json, hook/cta-formulas | slides-copy.json | GATE-COPY preliminare (hook+CTA presenti) |
| 03-design | CF-R4-A03/A04 | slides-copy.json, brand_kit | prompt Gemini / design Canva / slides.html | — |
| 04-render | CF-R4-A05 | design | PNG 1080x1350 per slide | GATE-FORMATO |
| 05-qa | CF-QA-A01 | PNG + copy + caption | verdetto per gate in state.json | GATE-BRAND + GATE-COPY |
| 06-delivery | CF-R5-A04 | asset verdi | manifest + handoff a WF-PUBLISH/committente | acceptance criteria handoff |

### (b) WF-VIDEO — UGC / avatar multi-engine

```
ordine → brief → WF-SCRIPT (script base) → [se conversione: blocco APSOC da MARKETING]
  → CF-R2-A01 risolve capability → engine:
      ugc/motion/image-4k/soul-id → higgsfield
      avatar/talking-head        → heygen
      voiceover                  → tts
  → pipeline UGC: soul-id(brand) → image-4k → motion → ffmpeg (montaggio+subtitle+audio)
    pipeline avatar: script → heygen render → ffmpeg (intro/outro, subtitle)
  → T-render-queue: stima crediti → CF-SENT-cost approva/blocca → render
  → GATE-FORMATO (durata, aspect, codec, loudness) → GATE-BRAND (voce, palette, soul coerente)
  → GATE-COPY (script: hook nei primi 3s, CTA presente) → delivery/publish
```
Dry-run: tutta la pipeline gira producendo `*.intent.json` per ogni chiamata engine
(prompt, parametri, costo stimato) senza consumare crediti — identico al modello CF "dry mode".

| Fase | Owner | Engine | Gate |
|---|---|---|---|
| 01-brief + script | CF-R1 + CF-R3 (WF-SCRIPT) | — | brief + script approvato |
| 02-asset (UGC) | CF-R2-A02/A03/A04 | higgsfield (soul-id → image-4k → motion) | check engine collegato |
| 02-asset (avatar) | CF-R2-A05 | heygen | check engine collegato |
| 03-voiceover | CF-R2-A07 | tts | qualità audio (no clipping) |
| 04-montaggio | CF-R2-A06 | ffmpeg | GATE-FORMATO (durata, aspect, codec, loudness) |
| 05-qa | CF-QA-A01 | — | GATE-BRAND + GATE-COPY (hook 3s, CTA) |
| 06-delivery | CF-R5 | — | handoff contract |

La fase 02 passa SEMPRE da T-render-queue (CF-R2-A08): `estimate()` aggregato → confronto
con `budget.crediti_engine` → CF-SENT-cost approva o blocca con exit esplicito.

### (c) WF-ARTICOLO / WF-NEWSLETTER

```
ordine → brief (keyword/topic, icp) → outline (approvazione committente se richiesta)
  → draft (CF-R3-A02) → SEO/AI-SEO pass → [newsletter: blocco CTA APSOC da MARKETING]
  → GATE-COPY (struttura, claim verificabili, zero genericità) → GATE-BRAND (tone vs brand_kit)
  → formato output (md / html / email-ready) → delivery o publish (blog via PLATFORM)
```
Dry-run: outline + stima lunghezza/tier. QA: il gatekeeper confronta il draft con
`brand-kit.json.voice` e con il Mandato Empire ("prove non promesse").

### (d) WF-THUMB — thumbnail / grafica

```
ordine → brief (titolo video/uso, canale) → 3 concept testuali (composizione, testo, emozione)
  → generazione: canva (template brand) | image/canvas-design | higgsfield image-4k
  → varianti A/B (2 per concept scelto) → T-resize (1280x720, 1080x1920, ...)
  → GATE-FORMATO (leggibilità a 10%, peso, safe-area) → GATE-BRAND → delivery
```
Dry-run: solo i 3 concept. Per YouTube il committente (05-MB) riceve le varianti A/B e
sceglie; la scelta torna in `cf/patterns`.

### (e) WF-PUBLISH — pubblicazione schedulata multi-canale

```
coda (deliverable con gate verdi) → calendar slot (WF-CALENDAR) → per ogni canale:
  adattamento (caption len, hashtag, aspect) → REVIEW UMANA (gate manuale, fase iniziale)
  → publish: IG/TikTok/LinkedIn via orchestratori Python esistenti · Drive via WF-DELIVERY
  → T-postcheck (verifica live) → log trace + wiki/log.md → WF-FEEDBACK (metriche a 48h/7gg)
```
Dry-run: genera il piano di pubblicazione (cosa, dove, quando, con quale caption) senza
toccare i canali. State: `state.json.publish[]` per canale con esito e URL.

---

## 5. Layer motori (engines) — astrazione multi-engine

Pattern identico a `engines.sh` di CF Exponium: una **capability logica** mappa al launcher
del motore giusto. L'orchestrazione parla SOLO capability; i motori sono intercambiabili.

### Registry iniziale

| Engine | Capability servite | Stato | Launcher |
|---|---|---|---|
| **canva** | design, carousel-design, brand-template, export, resize | ATTIVO (MCP `mcp__claude_ai_Canva__*`) | chiamate MCP dirette, wrapper `engines/canva.md` |
| **higgsfield** | image-4k, video-ugc, motion, soul-id, product-shoot | DA COLLEGARE (skill portabili da CF Exponium) | port di `hf-studio/` |
| **heygen** | avatar, talking-head, spokesperson | PRONTO, da collegare (scaffold CF riusabile) | port di `heygen-studio/` |
| **ffmpeg** | montaggio, cut, crop, subtitle-burn, audio-mix, concat | ATTIVO (locale) | `engines/ffmpeg.sh` |
| **tts** | voiceover, audio-caption | PARZIALE (edge-tts gratuito; ElevenLabs opzionale) | `engines/tts.sh` |
| **puppeteer-render** | html-to-png, carousel-render | ATTIVO (`carousel-factory/render.mjs`) | wrapper esistente |
| **gemini-img** | slide-image (via prompt, oggi manuale) | ATTIVO MANUALE | output = prompt pronti (ramo A WF-CAROSELLO) |

### Mappa capability → engine (routing, funzione pura)

| Capability | Engine primario | Fallback | Note |
|---|---|---|---|
| carousel-design, brand-template, export, resize | canva | puppeteer-render | Canva quando esiste brand template; HTML/Puppeteer per layout custom |
| slide-image | gemini-img (manuale) | higgsfield image-4k | si sostituisce nel registry quando un engine image è collegato |
| image-4k, video-ugc, motion, soul-id, product-shoot | higgsfield | — | port da hf-studio CF Exponium |
| avatar, talking-head, spokesperson | heygen | — | port da heygen-studio CF Exponium |
| montaggio, cut, crop, subtitle-burn, audio-mix | ffmpeg | — | locale, costo zero |
| voiceover | tts (edge-tts) | ElevenLabs | ElevenLabs solo se il brief richiede qualità voce premium e il budget lo copre |
| html-to-png | puppeteer-render | canva export | render.mjs esistente |

```
engine_of(capability):
  match capability → engine primario
  se engine.check() fallisce → fallback (se esiste) altrimenti errore esplicito
  MAI silenziosamente un engine diverso da quello loggato in trace.jsonl
```

### Contratto engine (non negoziabile)
Ogni engine espone 4 operazioni: `generate(job)`, `check()` (collegato sì/no),
`status()`, `estimate(job)` (costo in crediti/€ PRIMA di eseguire). Il routing è una
funzione pura `engine_of(capability) → engine`; default sicuri e backward-compatible.

### Regola di estensione
Aggiungere un motore (es. Runway, Kling, Sora) = aggiungere 1 riga al registry + 1 launcher
conforme al contratto. **Vietato** toccare workflow, agenti o orchestrazione. Se due engine
servono la stessa capability, il brief può forzare la scelta (`note.engine_preference`),
altrimenti decide il routing per costo/qualità (Thompson Sampling via Ruflo quando attivo).

---

## 6. Asset esistenti → reparto

| Path | Reparto | Azione |
|---|---|---|
| `Digital Empire/Workfolw crea caroselli à/carousel-factory/` (brands/, context/ con SYSTEM, PROMPT-SYSTEM, hook/cta-formulas, render.mjs) | CF-R4 / WF-CAROSELLO | **Promuovere a workflow canonico**: è l'asset più maturo. Wrappare in skill `cf-carousel`, NON riscrivere. I 4 brand in `brands/` diventano il seed del brand-kit registry |
| `Digital Empire/caroselli/3-sistemi-ai/` (slides.html, render.mjs, PNG) | CF-R4 / WF-CAROSELLO | Archiviare come esempio in `context/examples/`; pipeline superata da carousel-factory |
| `SKILL & Agenti/Workflow Canva/` | CF-R4 / T-canva-export | Verificare contenuto (cartella quasi vuota) e fondere nel wrapper engine `canva` |
| `SKILL & Agenti/Workflow pubblicazione automatica/` (main_orchestrator.py, mentalita_orchestrator.py, moduli IG/TikTok/LinkedIn/Drive) | CF-R5 / WF-PUBLISH | **Motore di pubblicazione ufficiale**: wrappare, rinnovare token scaduti (FB/IG), aggiungere dry-run e post-check |
| `Digital Empire/Page IG - Mentalità Brutale/` (LOGO, POST, storie) | CF-R5 + CF-R4 | Primo tenant interno di test: brand_kit `mentalita-brutale` già esistente in carousel-factory; gli asset diventano `brands/mentalita-brutale/assets/` |
| Skill globali `video`, `image`, `canvas-design`, `theme-factory`, `frontend-design` | CF-R2 / CF-R4 | Knowledge layer condiviso (pattern 6): referenziare dai team, non duplicare |
| Skill `social`, `content-strategy`, `market-social`, `market-ads`, `ad-creative` | CF-R1 / CF-R5 (+ handoff MKT) | Referenziare nei brief e negli adattamenti per canale |
| Skill `content-forge` | CF-R3 + FORGE | Per repurposing massivo (transcript → articoli/derivati) |
| MCP Canva (`mcp__claude_ai_Canva__*`) | CF-R4 | Engine `canva` del registry (sez. 5) |
| Repo CF Exponium: `hf-studio/`, `heygen-studio/`, `orchestration/orchestrator/engines.sh`, `swarm.sh` | CF-R2 + OPERATIONS | **Port selettivo**: copiare e parametrizzare (brand_kit al posto di Exponium hard-coded). Consultare, mai modificare l'originale |

---

## 7. Skill: esistenti da usare + NUOVE da creare

### Esistenti (knowledge layer, già installate)

| Skill | Uso in CF | Reparto |
|---|---|---|
| content-strategy | piano editoriale, pillar, calendario | CF-R1 |
| video, image, canvas-design | produzione media | CF-R2, CF-R4 |
| theme-factory, frontend-design | template visivi, slide HTML | CF-R4 |
| social, market-social | adattamento per canale | CF-R5 |
| ad-creative, market-ads | creative per ads (ordini da MKT) | CF-R4 |
| cro-copy-architect (APSOC) | gate copy + blocchi CTA (via MARKETING) | Quality Guild |
| content-forge | repurposing massivo | CF-R3 |
| seo-audit, ai-seo, schema | pass SEO articoli | CF-R3 |

### NUOVE da creare (via FORGE / skill-creator)

| Skill nuova | Scopo | Reparto |
|---|---|---|
| `cf-order` | Contratto di ordine: validazione, creazione `orders/<id>/`, state machine fasi | CF-A00 |
| `cf-brand-kit` | Schema brand_kit/icp, creazione tenant, sync con Canva brand kits, gate brand parametrico | CF-R4 / Sentinel |
| `cf-carousel` | Formalizza carousel-factory: formule hook/CTA, 3 rami di generazione, render | CF-R4 |
| `cf-engines` | Registry capability→engine, contratto generate/check/status/estimate | CF-R2 e tutti |
| `heygen-generate` | Port parametrizzato della skill CF Exponium (avatar per brand, non per Marco) | CF-R2 |
| `higgsfield-suite` | Port di higgsfield-generate + soul-id + product-photoshoot, multi-brand | CF-R2 |
| `cf-publish` | Pubblicazione multi-canale: wrapper orchestratori Python, dry-run, post-check, token health | CF-R5 |
| `cf-qa-gates` | I 3 gate eseguibili (checklist formato per ogni formato, brand check, APSOC check) | Quality Guild |

Regole (pattern 6-7-8): kernel ≤500 righe, dettagli in `references/`, invariant cardinali
espliciti in testa a ogni skill (es. cf-publish: "MAI pubblicare senza gate verdi e review umana attiva").

---

## 8. Integrazione Ruflo

| Funzione CF | Tool Ruflo | Configurazione |
|---|---|---|
| Coordinamento ecosistema | `swarm_init` topology **hierarchical** (Conductor → 5 lead → worker) | dichiarata in `BACKBONE.md` di CF |
| Batch mass-production | `swarm_init` topology **mesh** per i fan-out (a) e (b): N job indipendenti, pool di W worker paralleli — equivalente di `swarm.sh ugc batch.csv --parallel N --budget C` | parallelismo default 4, cap dal campo `budget` dell'ordine |
| Memoria | `memory_store/search` namespace: `cf/orders` (stato ordini), `cf/brand-kits` (tenant), `cf/patterns` (hook/format che performano per brand), `cf/failures` (ReasoningBank: errori distillati) | `memory_search` PRE-task obbligatorio nei coordinator (pattern 7 Piano Maestro) |
| Budget guard | hook pre-render: `estimate()` di ogni engine → somma vs `budget.crediti_engine` → blocco se sfora (exit 2, mai sforamento parziale) + cost-attribution per agente in `trace.jsonl` | CF-SENT-cost always-on |
| Spawn agenti | `agent_spawn` / `managed_agent_*` on-demand: i worker L5 esistono solo durante l'ordine (costo zero a riposo) | coordinator persistenti solo durante batch |
| Apprendimento | `reasoningbank-*` su fallimenti gate; `neural_train` sui pattern `cf/patterns` quando ci sono dati reali | post-task hook |
| Sicurezza | `aidefence_scan/has_pii` su ogni contenuto in uscita (specie per clienti agency) | gate compliance |

Hook concreti per ordine (pattern Dynamic Workflow):

```
pre-order   → memory_search("cf/patterns", brand+formato)   # cosa ha funzionato per questo brand
pre-render  → estimate() Σ engine vs budget → block/allow    # budget guard
post-gate   → se rosso: memory_store("cf/failures", {pezzo, gate, motivo})
post-order  → memory_store("cf/orders", state finale) + wiki/log.md entry
post-publish→ (a 48h/7gg) memory_store("cf/patterns", {brand, formato, hook, metriche})
```

Fallback (rischio daemon Windows, ADR-005 CF): se Ruflo non è disponibile, i workflow girano
in modalità pipeline sequenziale via script bash/python con lo stesso state.json — il
project state è la fonte di verità, Ruflo è il coordinatore, mai il contrario.

---

## 9. KPI + Quality Gates

### KPI (da misurare da zero — nessun dato storico)

| KPI | Definizione | Direzione |
|---|---|---|
| Throughput | pezzi consegnati / settimana, per formato | ↑ |
| First-pass rate | % deliverable che superano i 3 gate al primo colpo | ↑ (target da fissare dopo 4 settimane di baseline) |
| Lead time | ore da ordine valido a delivery | ↓ |
| Costo per pezzo | crediti+token / deliverable, per formato e per brand | ↓ |
| Rework rate | % pezzi rimandati indietro da un gate o dal committente | ↓ |
| Puntualità publish | % slot calendario rispettati | ↑ |
| Copertura tenant | n. brand_kit attivi serviti nel mese | ↑ |

### Quality gates (eredità 68-check CF, estesi e parametrizzati)

**GATE-FORMATO** (oggettivo, automatizzabile al 100%):
- Carosello: 1080x1350 px, cover + max 8 slide, peso < 8MB/slide, testo leggibile (contrasto), nessun taglio in safe-area.
- Video: aspect corretto per canale (9:16/1:1/16:9), durata nei limiti piattaforma, codec h264/h265, loudness -14 LUFS, sottotitoli sincronizzati se richiesti.
- Testo: lunghezza nel range del brief, heading structure valida, zero link rotti.
- Grafica: dimensioni esatte del canale target, peso, margini.

**GATE-BRAND** (parametrico sul brand_kit dell'ordine — la differenza chiave vs CF Exponium):
- Palette: solo colori hex del brand_kit (tolleranza dichiarata).
- Font e logo: corretti e posizionati secondo template.
- Tone of voice: campionamento del testo vs `brand-kit.json.voice` (esempi positivi/negativi).
- Coerenza soul/avatar: stesso personaggio ricorrente del brand nei video.
- Mandato Empire (non parametrico, sempre attivo): "prove non promesse", zero contenuti generici, zero claim non verificabili.

**GATE-COPY-APSOC** (eseguito con cro-copy-architect, in handoff con la Copy Guild):
- Hook presente nei primi 3 secondi / prima slide / prima riga.
- Problema e Promessa espliciti e coerenti con l'icp dell'ordine.
- Social proof dove il formato lo richiede (solo prove reali, mai inventate).
- Obiezione principale gestita (formati lunghi).
- CTA unica, misurabile, coerente con il canale.

Regola dei cancelli: i 3 gate sono sequenziali (formato → brand → copy); un rosso ferma
il pezzo, non il batch; 2 rework falliti sullo stesso pezzo → escalation al coordinator
+ entry in `cf/failures`.

---

## 10. Fasi di build (ordinate, con gate)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **CF-F0** | Scaffolding org: `company/ecosistemi/03-content-factory/` con reparti L2, BACKBONE.md (namespace+topologia), questo dossier come spec | struttura navigabile, zero ambiguità sui 5 reparti |
| **CF-F1** | `cf-order` + `cf-brand-kit`: contratto ordine, state machine, brand-kit registry con i 4 brand seed di carousel-factory | un ordine fittizio attraversa tutte le fasi in dry-run con state.json+trace.jsonl corretti |
| **CF-F2** | WF-CAROSELLO live: wrap di carousel-factory in `cf-carousel`, gate formato+brand+copy eseguibili (`cf-qa-gates`), primo batch REALE per Mentalità Brutale | ≥5 caroselli reali con 3 gate verdi |
| **CF-F3** | Engine layer: `cf-engines` registry + wrapper canva/ffmpeg/puppeteer/tts; WF-THUMB live via Canva MCP | `engine status` corretto per tutti; 1 thumbnail reale via 2 engine diversi |
| **CF-F4** | WF-PUBLISH live: wrap orchestratori Python, rinnovo token (FB/IG), dry-run + review umana + post-check; primo publish schedulato reale | 1 carosello pubblicato su IG via pipeline completa ordine→publish→log wiki |
| **CF-F5** | CF-R3 live: WF-ARTICOLO + WF-NEWSLETTER con handoff APSOC a MARKETING (richiede ecosistema 04 almeno in versione Copy Guild) | 1 articolo + 1 newsletter con gate verdi consegnati a un committente reale |
| **CF-F6** | Video multi-engine: port higgsfield-suite + heygen-generate parametrizzati, T-render-queue con cost guard; INTERA pipeline in dry-run, poi primo video reale SOLO con ok esplicito sui crediti | dry-run completo verde; 1 video reale dopo approvazione budget |
| **CF-F7** | Mass-production + learning: swarm mesh per batch ≥10, sentinels cost/brand always-on, WF-FEEDBACK → cf/patterns, ReasoningBank attivo | batch 10 pezzi parallelo entro budget; primo pattern distillato in memoria |

Ordine motivato: si parte dall'asset più maturo (caroselli) e dal canale già attivo (IG
Mentalità Brutale) per avere output reale subito (coerente con F5 della roadmap master);
i video — che costano crediti — arrivano solo quando gate, state e budget guard sono provati.

---

## 11. Rischi specifici + mitigazioni

| Rischio | Probabilità/Impatto | Mitigazione |
|---|---|---|
| Token social scaduti (FB/IG già scaduto, da MEMORY) rompono WF-PUBLISH silenziosamente | Alta/Alto | `cf-publish` include `token-health` check pre-run; CF-F4 inizia dal rinnovo; post-check verifica il post live, non solo l'esito API |
| Ban/limitazioni da automazione social (IG/TikTok/LinkedIn) | Media/Alto | Rate limit conservativi, review umana, pattern di pubblicazione umani (orari variabili), un account di test prima dei brand reali |
| Motori a crediti (Higgsfield/HeyGen) non collegati o costi imprevisti | Media/Alto | Dry-run default + `estimate()` obbligatorio + budget guard exit-2; nessuna spesa senza ok esplicito (vincolo Piano Maestro); ordine fasi: video per ultimi |
| Brand drift multi-tenant (il contenuto di un brand "contamina" un altro) | Media/Alto | GATE-BRAND parametrico per ordine, CF-SENT-brand a campione, namespace memoria separati per brand in `cf/brand-kits`, soul-id distinti |
| Step manuale Gemini nel carosello (ramo A) crea collo di bottiglia | Alta/Medio | Ramo B (Canva MCP) e ramo C (render HTML) già automatici; il ramo A resta per qualità top finché un engine image è collegato — poi `gemini-img` si sostituisce nel registry senza toccare il workflow |
| Path legacy fragili (`Workfolw crea caroselli à` con typo/accenti, spazi) | Alta/Medio | La migrazione CF-F2 copia in `company/.../wf-carosello/` con path puliti; gli originali restano intoccati finché il sostituto non è validato (regola Piano Maestro) |
| Copy duplicato tra CF-R3 e MARKETING (chi scrive cosa?) | Media/Medio | Confine scritto nel dossier: CF = contenuto strutturale, MKT = persuasione/APSOC; i pezzi ibridi hanno handoff esplicito; contradiction-analyzer sui due dossier |
| Sovraccarico ordini (CF è il collo di bottiglia della holding) | Media/Alto | Precedenza deadline→revenue→interno gestita dal Conductor; capacità dichiarata per formato; il Board vede la coda via Observability |
| QA gate troppo rigidi → throughput zero, o troppo laschi → contenuti generici | Media/Medio | Baseline 4 settimane prima di fissare target first-pass; gate formato sempre rigidi (oggettivi), gate brand/copy con livelli warn/block rivedibili dalla Quality Guild |

---

## Connessioni
- [[00-PIANO-MAESTRO]] — gerarchia, backbone, 13 pattern
- [[04-ECOSISTEMA-MARKETING]] — Copy Guild APSOC (handoff più frequente)
- [[05-ECOSISTEMA-MULTIBUSINESS]] — committente YouTube/KDP
- [[projects/Exponium/Exponium_Content_Factory_Studio]] — modello di riferimento da superare
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo (swarm, memoria, budget)
