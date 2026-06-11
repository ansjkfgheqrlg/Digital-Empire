# 🏭 03 — CONTENT-FACTORY (CF-DE)

> **Livello:** L1 · **Priorità:** ALTA · **Stato:** parziale (asset maturi esistono, coordinazione in build)
> **Fonte di verità:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` (dossier vincolante)
> **Modello di riferimento:** Content Factory di Exponium (AION GROUP) — da superare, non da copiare.

---

## 1. Missione

Produrre **contenuti multi-formato, multi-brand, multi-cliente** per TUTTI gli ecosistemi
di EMPIRE OS e per i clienti esterni: caroselli IG, video UGC/avatar, articoli, newsletter,
thumbnail, grafiche, pubblicazione schedulata multi-canale.

CF-DE è la fabbrica trasversale della holding: **non ha clienti propri, ha committenti**.
Chiunque (Agency, Info-Business, Multi-Business, Marketing, la stessa DE) emette un **ordine**
e riceve deliverable conformi a gate di qualità.

**Regola fondante (pattern #11 multi-tenant):** tutto ciò che in CF Exponium era hard-coded
sul brand Exponium qui diventa **input**. Un workflow che non accetta `brand_kit` + `icp`
non è conforme.

---

## 2. DONE WHEN

1. **Contratto di ordine standard attivo**: ogni richiesta entra come
   `{committente, brand_kit, icp, formato, quantità, deadline, budget}` e produce
   `orders/<id>/state.json + trace.jsonl`.
2. **Brand-kit registry operativo** con ≥4 brand (DE/agency, Mentalità Brutale,
   education/corsi, ≥1 cliente o canale).
3. **I 5 workflow chiave** (carosello, video, articolo, thumbnail, publish) girano
   end-to-end con dry-run e QA gate; almeno carosello + publish con output REALE.
4. **Engine layer multi-motore attivo**: aggiungere un motore = 1 riga di registry,
   zero modifiche all'orchestrazione.
5. **Swarm mass-production**: un batch ≥10 pezzi prodotto in parallelo con budget guard
   che blocca PRIMA di sforare.
6. **Zero asset orfani**: tutti i path legacy mappati a un reparto con azione completata.

---

## 3. La differenza vs CF Exponium (dove la superiamo)

| Dimensione | CF Exponium (AION) | CF-DE |
|---|---|---|
| Scopo | Mono-scopo: solo il lancio Exponium | **Multi-tenant**: N committenti, ogni ordine porta `brand_kit` + `icp` |
| Brand | 1 (Exponium, voce di Marco) | Registry di brand: DE, Mentalità Brutale, clienti agency, canali YT, libri KDP |
| Formati | Video/immagini (reel UGC, avatar) | Video + caroselli + testuale + grafiche + email-ready |
| Distribuzione | Consegna interna al team lancio | Reparto L2 dedicato: Pubblicazione & Distribuzione multi-canale schedulata |
| Brand gate | Mandato fisso Exponium | **Gate parametrico**: legge il brand_kit dell'ordine |
| Motori | Higgsfield + HeyGen | + Canva MCP, ffmpeg, TTS, render Puppeteer nello stesso registry |
| Eredità identica | — | state.json + trace.jsonl per ordine, swarm con budget guard, QA a cancelli, engines.sh come pattern |

---

## 4. Organigramma L1 → L5

```
L1  03-CONTENT-FACTORY — coordinatore: CF-A00-conductor (riceve ordini, smista, precedenze)
 │
 ├── L2  CF-R1 STRATEGIA CONTENUTI ......... Reparti/Strategia/
 │     L3: WF-BRIEF · WF-CALENDAR
 │     L4: T-hook · T-angle · T-trend-intake
 │
 ├── L2  CF-R2 PRODUZIONE VIDEO ............ Reparti/Produzione-Video/
 │     L3: WF-VIDEO-UGC · WF-VIDEO-AVATAR · WF-SHORTFORM   → Workflow/WF-VIDEO/
 │     L4: T-voiceover · T-subtitle · T-montaggio · T-render-queue
 │
 ├── L2  CF-R3 PRODUZIONE TESTUALE ......... Reparti/Produzione-Testuale/
 │     L3: WF-ARTICOLO · WF-NEWSLETTER · WF-SCRIPT          → Workflow/WF-ARTICOLO/
 │     L4: T-caption · T-headline · T-repurpose
 │
 ├── L2  CF-R4 VISUAL & DESIGN ............. Reparti/Visual-Design/
 │     L3: WF-CAROSELLO · WF-THUMB · WF-BRANDKIT            → Workflow/WF-CAROSELLO/ · Workflow/WF-THUMB/
 │     L4: T-canva-export · T-resize · T-asset-library
 │
 ├── L2  CF-R5 PUBBLICAZIONE & DISTRIBUZIONE Reparti/Pubblicazione/
 │     L3: WF-PUBLISH · WF-DELIVERY · WF-FEEDBACK           → Workflow/WF-PUBLISH/
 │     L4: T-utm · T-uploader · T-postcheck
 │
 ├── Layer ENGINE (L4 condiviso) ........... Funzioni/
 │     T-CANVA · T-HIGGSFIELD · T-HEYGEN · T-FFMPEG · T-TTS · T-RENDER-PUPPETEER
 │
 ├── L5  31 agenti (schede complete in Agenti/) — tier WASM/Haiku/Sonnet
 ├── ⊕  CF-QA-A01-gatekeeper (Quality Guild trasversale)
 └── ⊕  CF-SENT-cost + CF-SENT-brand (Sentinels always-on)
```

Ogni team segue lo schema canonico (pattern #1): coordinator + workers, I/O espliciti,
acceptance criteria, failure handling, shared_state.

---

## 5. Contratto di ordine (unico punto d'ingresso)

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

**Nessun lavoro parte senza ordine valido.** Il CF-A00-conductor rifiuta ordini incompleti
(escalation al committente, non improvvisazione). Precedenza in coda:
`deadline → revenue impact (Agency/Lanci) → interno`.

---

## 6. Flusso tipo end-to-end (esempio: 10 caroselli Mentalità Brutale)

1. **Ordine** — `05-MB` emette ordine `formato: carosello-ig, quantita: 10, brand_kit:
   brands/mentalita-brutale/`. CF-A00 valida il contratto e crea `orders/CF-2026-0001/`.
2. **Brief** — CF-R1 carica brand_kit + icp e produce `brief.json` per ciascun pezzo
   (angle, hook type, n. slide). Pre-task: `memory_search("cf/patterns", brand+formato)`.
3. **Fan-out swarm (mesh)** — 10 job paralleli in CF-R4: slide copy (formule
   carousel-factory) → design (ramo Gemini / Canva MCP / render Puppeteer) → PNG 1080x1350.
4. **Gate sequenziali** — GATE-FORMATO → GATE-BRAND (parametrico sul brand_kit) →
   GATE-COPY-APSOC (CF-QA-A01). Un rosso ferma il pezzo, non il batch.
5. **Delivery/Publish** — caption + hashtag (T-caption), manifest in `06-delivery/`,
   handoff a WF-PUBLISH: slot calendario, review umana, pubblicazione IG, post-check.
6. **Feedback** — a 48h/7gg le metriche tornano a MKT Analytics e a `cf/patterns`
   (cosa funziona per quale brand). Report batch: pezzi ok / rework / costo.

Regole comuni a tutti i flussi: **dry-run default** alla prima esecuzione; nessuna fase
salta il gate precedente; ogni fallimento → `trace.jsonl` + `cf/failures` (ReasoningBank);
pubblicazione automatica con **review umana obbligatoria** finché il Board non rimuove il vincolo.

---

## 7. KPI (da misurare da zero — nessun dato storico)

| KPI | Definizione | Direzione |
|---|---|---|
| Throughput | pezzi consegnati / settimana, per formato | ↑ |
| First-pass rate | % deliverable che superano i 3 gate al primo colpo | ↑ (target dopo 4 settimane di baseline) |
| Lead time | ore da ordine valido a delivery | ↓ |
| Costo per pezzo | crediti+token / deliverable, per formato e per brand | ↓ |
| Rework rate | % pezzi rimandati indietro da un gate o dal committente | ↓ |
| Puntualità publish | % slot calendario rispettati | ↑ |
| Copertura tenant | n. brand_kit attivi serviti nel mese | ↑ |

## 8. Quality gates (sequenziali: formato → brand → copy)

| Gate | Natura | Esempi di check |
|---|---|---|
| **GATE-FORMATO** | oggettivo, automatizzabile 100% | carosello 1080x1350 ≤8 slide+cover; video aspect/durata/codec/-14 LUFS; testo heading structure |
| **GATE-BRAND** | parametrico sul brand_kit dell'ordine | palette hex, font/logo, tone vs `voice`, soul coerente + Mandato Empire sempre attivo ("prove non promesse") |
| **GATE-COPY-APSOC** | con cro-copy-architect + Copy Guild (04-MKT) | hook nei primi 3s/prima slide, P+S espliciti vs icp, social proof reale, CTA unica |

2 rework falliti sullo stesso pezzo → escalation al coordinator + entry in `cf/failures`.

---

## 9. Fasi di build (ordinate, con gate)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **CF-F0** | Scaffolding org: questa cartella con reparti L2, BACKBONE.md, schede agente | struttura navigabile, zero ambiguità sui 5 reparti |
| **CF-F1** | `cf-order` + `cf-brand-kit`: contratto ordine, state machine, registry con i 4 brand seed di carousel-factory | ordine fittizio attraversa tutte le fasi in dry-run con state.json+trace.jsonl corretti |
| **CF-F2** | WF-CAROSELLO live: wrap di carousel-factory in `cf-carousel`, 3 gate eseguibili, primo batch REALE per Mentalità Brutale | ≥5 caroselli reali con 3 gate verdi |
| **CF-F3** | Engine layer: `cf-engines` registry + wrapper canva/ffmpeg/puppeteer/tts; WF-THUMB live via Canva MCP | `engine status` corretto per tutti; 1 thumbnail reale via 2 engine diversi |
| **CF-F4** | WF-PUBLISH live: wrap orchestratori Python, rinnovo token FB/IG, dry-run + review umana + post-check | 1 carosello pubblicato su IG via pipeline completa ordine→publish→log wiki |
| **CF-F5** | CF-R3 live: WF-ARTICOLO + WF-NEWSLETTER con handoff APSOC a 04-MARKETING | 1 articolo + 1 newsletter con gate verdi a un committente reale |
| **CF-F6** | Video multi-engine: port higgsfield-suite + heygen-generate parametrizzati, T-render-queue con cost guard | dry-run completo verde; 1 video reale solo dopo ok budget |
| **CF-F7** | Mass-production + learning: swarm mesh batch ≥10, sentinels always-on, WF-FEEDBACK → cf/patterns | batch 10 pezzi parallelo entro budget; primo pattern distillato |

Ordine motivato: si parte dall'asset più maturo (caroselli) e dal canale già attivo
(IG Mentalità Brutale); i video — che costano crediti — arrivano solo quando gate,
state e budget guard sono provati.

---

## 10. Mappa di questa cartella

```
03-CONTENT-FACTORY/
├── ECOSISTEMA.md            ← questo file
├── BACKBONE.md              ← namespace, topologia, contratti BUS
├── Reparti/
│   ├── Strategia/README.md
│   ├── Produzione-Video/README.md
│   ├── Produzione-Testuale/README.md
│   ├── Visual-Design/README.md
│   └── Pubblicazione/README.md
├── Workflow/
│   ├── WF-CAROSELLO/README.md   WF-VIDEO/README.md   WF-ARTICOLO/README.md
│   ├── WF-THUMB/README.md       WF-PUBLISH/README.md
│   └── caroselli-wrapper.md (wrapper legacy, vedi WF-CAROSELLO)
├── Funzioni/                ← layer engine condiviso (contratto generate/check/status/estimate)
│   ├── T-CANVA/  T-HIGGSFIELD/  T-HEYGEN/  T-FFMPEG/  T-TTS/  T-RENDER-PUPPETEER/
└── Agenti/                  ← 31 schede complete (CF-A00 … CF-SENT-brand)
```

## Connessioni

- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` — dossier vincolante (asset → reparto, skill nuove, rischi)
- `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §6 — i 13 pattern non negoziabili
- `company/Ecosistemi/04-MARKETING/` — Copy Guild APSOC (handoff più frequente: CF chiede copy, MKT chiede creative)
- `company/Ecosistemi/05-MULTI-BUSINESS/` — committente YouTube/KDP
- `Workfolw crea caroselli à/carousel-factory/` — asset più maturo, motore di WF-CAROSELLO

*Fonte: `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` · Aggiornato: 2026-06-11*
