# 🏭 05 — ECOSISTEMA MULTI-BUSINESS (EMPIRE OS · L1 #05)

> **Dossier dell'ecosistema Multi-Business di Digital Empire Group.**
> Business digitali scalabili paralleli: (A) YouTube Automation, (B) Publishing/KDP, (C) E-commerce.
> Coerente al 100% con `00-PIANO-MAESTRO.md` (gerarchia LX→L5, handoff contract, pattern 1-12,
> 3-tier routing, multi-tenant by design, wiki-first).
> Versione: 1.0 · Creato: 2026-06-10 · Priorità: MEDIA-ALTA (YouTube = sotto-ecosistema prioritario)
>
> ⚠️ **Vincolo di onestà:** i canali di riferimento YouTube (`@Legamidiamore`, `@dosementale`)
> NON sono ancora stati analizzati. Il loro studio profondo (frame reali + visione Claude via
> Empire Studio) è la **PRIMA fase di build** (§11, F-MB1). Nessun dato su quei canali in questo
> dossier è inventato: dove servirebbe, c'è un segnaposto `[da ingestione F-MB1]`.

---

## 0. Missione + DONE WHEN

**Missione:** costruire e gestire N business digitali scalabili in parallelo — canali YouTube
completamente automatizzati, un catalogo libri KDP in crescita continua, store e-commerce —
dove ogni "istanza di business" (canale, libro, store) è un `brand_kit` servito dallo stesso
motore di agenti (pattern 11: multi-tenant by design). Multi-Business NON produce asset
materiali: li **ordina** a Content-Factory e li **trasforma in revenue** tramite strategia,
ottimizzazione e pubblicazione.

**DONE WHEN:**
1. Org L2→L5 dei 3 sotto-ecosistemi documentata e navigabile in `company/05-multibusiness/`.
2. Ingestione Empire Studio dei 2 canali riferimento completata → 2 dossier in wiki `sources/`.
3. Primo canale YouTube pilota attivo: niche scelta, calendario, ≥1 video pubblicato che ha
   superato TUTTI e 4 i QA gate (script, audio, visual, SEO).
4. Pipeline libro KDP end-to-end eseguita una volta integrando `Workflow-libri` (book-factory):
   manoscritto → PDF 6x9 → cover → listing → pubblicazione (con review umana).
5. Multi-canale dimostrato: ≥2 canali gestiti in parallelo via swarm, ognuno col suo brand_kit
   e namespace memoria, zero cross-contaminazione di contenuti.
6. E-commerce: struttura minima vitale documentata (anche se non attiva) + backlog fasi future.
7. KPI tracciati per ogni istanza (§10) e loggati in wiki + AgentDB; zero pubblicazioni
   automatiche senza gate verdi.

**OUT OF SCOPE (ora):** spesa API (HeyGen/ElevenLabs/ads) senza ok esplicito; pubblicazione
YouTube/KDP senza review umana nelle prime fasi; e-commerce operativo (solo scheletro).

---

## 1. Posizione nella holding — confini e handoff

Multi-Business è un ecosistema **cliente interno** degli ecosistemi trasversali. Possiede la
strategia e il P&L di ogni istanza; **non duplica** capacità che esistono altrove.

```
              ┌──────────────────────────────────────────────┐
              │   05 MULTI-BUSINESS (questo dossier)          │
              │   strategia · ottimizzazione · pubblicazione  │
              └───────┬───────────┬───────────┬──────────────┘
   ordina asset       │           │           │        consegna output
   (video, libri,     ▼           ▼           ▼        (canali, libri, store)
┌───────────────┐ ┌─────────┐ ┌────────────┐ ┌────────────┐
│03 CONTENT-    │ │04 MARKE-│ │08 INTELLI- │ │09 OPERA-   │
│  FACTORY      │ │  TING   │ │  GENCE     │ │  TIONS     │
│ produzione    │ │ copy    │ │ ricerca,   │ │ swarm,     │
│ materiale     │ │ APSOC,  │ │ Empire     │ │ scheduling,│
│ multi-formato │ │ ads     │ │ Studio     │ │ cost guard │
└───────────────┘ └─────────┘ └────────────┘ └────────────┘
```

**Tabella handoff (contratto Bus: `{from, to, payload, acceptance_criteria}`):**

| Da → A | Cosa ordina | Payload del contratto | Acceptance criteria |
|---|---|---|---|
| MB → **Content-Factory** | Produzione video YouTube (script→voiceover→visual→thumbnail), manoscritti libri, creative store | `{brand_kit, formato, quantità, deadline, spec_tecniche, riferimenti_stile}` | asset conformi a spec (durata, risoluzione, formato file), brand_kit rispettato, consegna entro deadline |
| MB → **Marketing** | Copy listing KDP, descrizioni SEO, titoli, copy ads e-comm, hook script | `{brand_kit, icp, formato_copy, framework: APSOC, vincoli_piattaforma}` | copy passa Copy/APSOC Guild gate + brand gate |
| MB → **Intelligence** | Ricerca niche, analisi competitor, trend, ingestione Empire Studio dei canali riferimento | `{dominio, domande_di_ricerca, output_atteso: dossier_wiki}` | dossier in wiki `sources/` o `synthesis/` con dati verificabili e fonti |
| MB → **Platform** | Tooling (CLI KDP, integrazioni YouTube Data API, store setup) | `{spec_funzionale, API_target, vincoli}` | tool passa verify.sh Empire |
| MB → **Operations** | Esecuzione swarm mass-production, scheduling pubblicazioni, budget | `{workflow_id, parallelismo, budget_max, schedule}` | dry-run ok, Cost-Sentinel verde |
| MB → **Forge** | Nuove skill/team (es. yt-seo-optimizer) | `{gap_capacità, spec_skill}` | skill conforme a progressive disclosure (kernel ≤500 righe) |

**Regola di confine (non negoziabile):** se un task è "creare un asset" → Content-Factory.
Se è "scrivere copy persuasivo" → Marketing. Se è "capire/ricercare" → Intelligence.
Multi-Business tiene SOLO: scelta niche/prodotto, calendario, QA gate finale d'istanza,
ottimizzazione metadati, pubblicazione, monitoraggio revenue.

---

## 2. I tre sotto-ecosistemi (org L2 → L3 → L4)

### 2.1 (A) YOUTUBE AUTOMATION — `MB-YT` (priorità: ALTA)

| Reparto L2 | Workflow L3 (team end-to-end) | Funzioni L4 (un team per funzionalità) |
|---|---|---|
| **YT-Strategia** | `WF-YT-NICHE` (scelta niche e validazione) · `WF-YT-CHANNEL-LAUNCH` (setup canale + brand_kit) · `WF-YT-CALENDAR` (calendario editoriale) | T-niche-scout · T-competitor-map · T-keyword-yt · T-brandkit-builder · T-calendar-planner |
| **YT-Produzione (interfaccia)** | `WF-YT-VIDEO-ORDER` (ordina il video a Content-Factory e ne valida la consegna — NON produce) | T-brief-compiler · T-handoff-validator · T-asset-receiver |
| **YT-Ottimizzazione** | `WF-YT-OPT` (titolo, descrizione, tag, end screen, A/B thumbnail) | T-title-lab · T-description-seo · T-tags · T-endscreen-cards · T-thumb-ab |
| **YT-Pubblicazione** | `WF-YT-PUBLISH` (upload via YouTube Data API, scheduling, clip cross-platform) · `WF-YT-ANALYTICS` (lettura metriche → feedback a Strategia) | T-uploader-api · T-scheduler · T-clip-crossposter · T-metrics-reader · T-retention-analyst |

### 2.2 (B) PUBLISHING/KDP — `MB-PUB` (priorità: MEDIA-ALTA, asset già esistenti)

| Reparto L2 | Workflow L3 | Funzioni L4 |
|---|---|---|
| **PUB-Ricerca** | `WF-PUB-NICHE` (niche KDP, validazione domanda, analisi BSR/competizione) | T-kdp-niche-scout · T-keyword-kdp · T-competition-grader |
| **PUB-Produzione (interfaccia)** | `WF-PUB-BOOK-ORDER` (ordina manoscritto+immagini a Content-Factory) · `WF-PUB-LAYOUT` (book-factory: impaginazione 6x9 — asset esistente `Workflow-libri/`) | T-manuscript-brief · T-image-prompts · T-layout-engine · T-book-qa |
| **PUB-Packaging** | `WF-PUB-COVER` (cover front+spine+back) · `WF-PUB-LISTING` (titolo, sottotitolo, descrizione A+, 7 keyword, categorie — copy ordinato a Marketing) | T-cover-spec · T-listing-builder · T-category-picker |
| **PUB-Pubblicazione** | `WF-PUB-PUBLISH` (upload KDP, pricing, review pre-pubblicazione) · `WF-PUB-MONITOR` (BSR, recensioni, royalty → feedback a Ricerca) | T-kdp-uploader · T-pricing · T-royalty-tracker · T-review-watcher |

### 2.3 (C) E-COMMERCE — `MB-ECOM` (priorità: MEDIA, da zero — solo struttura minima §6)

| Reparto L2 | Workflow L3 | Funzioni L4 |
|---|---|---|
| **ECOM-Ricerca** | `WF-ECOM-PRODUCT` (ricerca prodotto, validazione margine) | T-product-scout · T-margin-calculator |
| **ECOM-Store** | `WF-ECOM-STORE` (setup store, listing — copy a Marketing, visual a Content-Factory) | T-store-setup · T-listing-ecom |
| **ECOM-Crescita** | `WF-ECOM-ADS` (campagne — strategia con Marketing) · `WF-ECOM-FULFILL` (monitor ordini/fulfillment) | T-ads-liaison · T-fulfillment-monitor |

---

## 3. Roster agenti L5

Ogni team L3/L4 = 1 coordinator + N worker (regola strutturale CF). Tier secondo il 3-tier
routing del Backbone: **WASM** (regole/parsing), **Haiku** (task ripetitivi), **Sonnet**
(produzione/analisi), **Opus** (decisioni strategiche, QA finale).

| ID agente | Ruolo | Tipo | Tier |
|---|---|---|---|
| `mb-conductor` | Dirige l'ecosistema, alloca budget tra A/B/C, risponde alla C-Suite | coordinator | Opus |
| `mb-yt-strategy-coord` | Coordina YT-Strategia (niche, lancio canali, calendari) | coordinator | Sonnet |
| `mb-yt-niche-scout` | Scansione niche, volume/competizione, RPM stimato per niche | worker | Sonnet |
| `mb-yt-competitor-mapper` | Mappa canali competitor (dopo ingestione F-MB1) | worker | Sonnet |
| `mb-yt-keyword-miner` | Keyword research YouTube (search/suggest/tag) | worker | Haiku |
| `mb-yt-brandkit-builder` | Compila brand_kit canale (voce, palette, stile visual, persona) | worker | Sonnet |
| `mb-yt-calendar-planner` | Calendario editoriale per canale, cadenza, stagionalità | worker | Haiku |
| `mb-yt-brief-compiler` | Compila il brief-ordine video per Content-Factory | worker | Sonnet |
| `mb-yt-handoff-validator` | Valida la consegna CF contro acceptance criteria del contratto | worker | Sonnet |
| `mb-yt-opt-coord` | Coordina YT-Ottimizzazione e i 4 QA gate video | coordinator | Sonnet |
| `mb-yt-title-smith` | Genera/testa varianti titolo (CTR-first, policy-safe) | worker | Sonnet |
| `mb-yt-seo-writer` | Descrizione SEO, tag, capitoli/timestamp | worker | Haiku |
| `mb-yt-thumb-strategist` | Spec thumbnail + A/B test (produzione a CF) | worker | Sonnet |
| `mb-yt-publish-coord` | Coordina pubblicazione, scheduling, cross-posting | coordinator | Sonnet |
| `mb-yt-uploader` | Upload via YouTube Data API, metadata, end screen | worker | WASM/Haiku |
| `mb-yt-clipper` | Ordina clip verticali a CF e li distribuisce (Shorts/TikTok/Reels) | worker | Haiku |
| `mb-yt-retention-analyst` | Legge analytics, individua drop-off, propone correzioni script | worker | Sonnet |
| `mb-pub-coord` | Coordina l'intera pipeline libro KDP | coordinator | Sonnet |
| `mb-pub-niche-scout` | Niche research KDP (BSR, keyword, gap catalogo) | worker | Sonnet |
| `mb-pub-layout-operator` | Esegue book-factory (`Workflow-libri/scripts/orchestrator.py`) | worker | WASM/Haiku |
| `mb-pub-book-qa` | QA PDF (formato 6x9, immagini, typo) — estende `qa_checker.py` | worker | Sonnet |
| `mb-pub-listing-builder` | Assembla listing (copy da Marketing) + categorie + 7 keyword | worker | Haiku |
| `mb-pub-publisher` | Upload KDP + pricing + checklist pre-pubblicazione | worker | Haiku |
| `mb-pub-royalty-tracker` | Monitora BSR/royalty/recensioni, feedback loop | worker | WASM/Haiku |
| `mb-ecom-coord` | Coordina e-commerce (dormiente fino a F-MB7) | coordinator | Sonnet |
| `mb-ecom-product-scout` | Ricerca prodotto + margini | worker | Sonnet |
| `mb-ecom-fulfill-monitor` | Monitor ordini/fulfillment/anomalie | worker | WASM/Haiku |
| `mb-qa-sentinel-liaison` | Interfaccia con Quality/Brand/Cost Sentinels del Backbone | worker | Sonnet |

> Spawn on-demand via Ruflo `agent_spawn` (§9): i coordinator esistono solo quando il loro
> workflow è attivo; i worker WASM/Haiku sono pool riusabili tra canali/libri.

---

## 4. YOUTUBE AUTOMATION in profondità

### 4.0 Vincolo fondativo — prima l'ingestione, poi la build

I canali da REPLICARE E SUPERARE sono `youtube.com/@Legamidiamore` e `youtube.com/@dosementale`
(video interamente AI: voiceover TTS + visual AI + script). **Non sono ancora stati studiati.**
La F-MB1 (§11) ordina a Intelligence un'ingestione **Empire Studio** dedicata (frame reali +
visione Claude) che produce per ciascun canale un dossier wiki con: niche e angolo, formato
video, struttura script ricorrente, stile visual, durata media, cadenza reale, packaging
titolo/thumbnail, segnali di monetizzazione. Tutti i parametri marcati `[da ingestione F-MB1]`
in questo capitolo vengono fissati SOLO dopo quel dossier.

### 4.1 Pipeline end-to-end per canale (dalla niche al video pubblicato)

```
FASE 1 · RICERCA/STRATEGIA          FASE 2 · PRODUZIONE (handoff CF)
┌─────────────────────────┐         ┌─────────────────────────────────┐
│ 1. niche research        │         │ 5. research argomento video      │
│ 2. competitor map        │────────▶│ 6. script (gate #1)              │
│    [da ingestione F-MB1] │  brief  │ 7. voiceover TTS (gate #2)       │
│ 3. brand_kit canale      │  ordine │ 8. visual AI/B-roll/avatar (g.#3)│
│ 4. calendario editoriale │         │ 9. thumbnail (con gate #3)       │
└─────────────────────────┘         └───────────────┬─────────────────┘
                                                     │ consegna validata
FASE 4 · PUBBLICAZIONE               FASE 3 · OTTIMIZZAZIONE
┌─────────────────────────┐         ┌─────────────────────────────────┐
│ 13. upload YouTube API   │◀────────│ 10. titolo + descrizione SEO     │
│ 14. scheduling           │         │ 11. tag + end screen + cards     │
│ 15. clip cross-platform  │         │ 12. SEO gate (#4) + brand gate   │
│ 16. analytics → feedback │         └─────────────────────────────────┘
└─────────────────────────┘
```

I passi 5-9 sono **eseguiti da Content-Factory** (reparti Video/Visual/Testuale) su ordine
`WF-YT-VIDEO-ORDER`; Multi-Business valida la consegna e possiede i gate.

### 4.2 Un workflow per fase

| Workflow | Fase | Input | Output | Owner gate |
|---|---|---|---|---|
| `WF-YT-NICHE` | 1 | dossier ingestione F-MB1, criteri (RPM, competizione, producibilità AI) | scheda niche validata + scorecard (domanda, competizione, monetizzabilità, fit AI) | mb-yt-strategy-coord |
| `WF-YT-CHANNEL-LAUNCH` | 1 | scheda niche | brand_kit canale (nome, persona, voce TTS, palette, template thumbnail, lingua) + canale creato | mb-conductor (ok umano) |
| `WF-YT-CALENDAR` | 1 | brand_kit + keyword map | calendario 30 giorni con titoli provvisori e keyword target | mb-yt-strategy-coord |
| `WF-YT-VIDEO-ORDER` | 2 | slot calendario | contratto a CF `{brand_kit, formato: video_long/short, quantità, spec: durata/TTS/stile_visual, deadline}` → consegna: script+audio+video+thumbnail | mb-yt-handoff-validator |
| `WF-YT-OPT` | 3 | video consegnato + keyword target | titolo finale, descrizione SEO, tag, end screen, thumbnail scelta | mb-yt-opt-coord |
| `WF-YT-PUBLISH` | 4 | pacchetto ottimizzato gate-verde | video pubblicato/schedulato + clip cross-platform + entry log wiki | mb-yt-publish-coord (review umana in fase iniziale) |
| `WF-YT-ANALYTICS` | 4→1 | metriche a 48h/7gg/28gg | report retention/CTR + raccomandazioni → memoria + calendario | mb-yt-retention-analyst |

### 4.3 QA gate per video (tutti bloccanti — pattern 4 del Piano Maestro)

| Gate | Quando | Criteri di pass (misurabili) | Chi blocca |
|---|---|---|---|
| **#1 Script Gate** | dopo consegna script da CF | hook nei primi 15s; struttura retention (loop aperti, payoff); aderenza brand_kit (tono, persona); lunghezza entro ±10% del target; zero claim non verificabili; similarità < soglia vs ultimi 20 script del canale (anti-ripetitività); lingua/grammatica pulita | mb-yt-opt-coord + Brand-Voice Sentinel |
| **#2 Audio Gate** | dopo voiceover TTS | zero artefatti/glitch udibili; pronuncia corretta nomi/numeri; pacing conforme a brand_kit; loudness normalizzata (target -14 LUFS); durata audio = durata script ±5% | mb-yt-handoff-validator |
| **#3 Visual Gate** | dopo montaggio + thumbnail | risoluzione ≥1080p; zero frame neri/corrotti/watermark di tool; coerenza stile visual col brand_kit; sync audio-video; thumbnail leggibile a dimensione piccola (test 120px), volto/soggetto + ≤4 parole | mb-yt-handoff-validator + Quality Sentinel |
| **#4 SEO Gate** | dopo WF-YT-OPT | titolo ≤100 caratteri con keyword primaria; descrizione ≥200 parole con keyword, timestamp e CTA; 10-15 tag pertinenti; end screen + cards impostate; metadata policy-safe (niente clickbait ingannevole, niente keyword stuffing) | mb-yt-seo-writer + mb-yt-opt-coord |
| **+ Policy/Brand Gate** | pre-upload, sempre | checklist policy YouTube (reused content, contenuto AI: disclosure dove richiesta, no spam) + Mandato Empire | Sentinelle-Empire |

Un gate rosso → il pacchetto torna al team responsabile col report di failure (loggato in
ReasoningBank, pattern 5). Mai override manuale senza decisione di `mb-conductor`.

### 4.4 Cadenza di pubblicazione (policy di default, da calibrare con F-MB1)

| Fase canale | Cadenza | Razionale |
|---|---|---|
| Warm-up (settimane 1-4) | 2-3 video/settimana | costruire libreria senza triggare spam detection; raccogliere dati retention |
| Regime (mese 2+) | da definire `[da ingestione F-MB1: cadenza reale dei canali riferimento]` — default 3-5/settimana se i gate reggono | la cadenza NON supera mai la capacità dei gate: qualità > volume |
| Shorts/clip | 1-2/giorno derivati dai long-form | costo marginale basso (clip ordinati a CF) |

### 4.5 Multi-canale: N canali in parallelo via swarm

**Ogni canale = un `brand_kit`** (pattern 11). Lo stesso motore (workflow §4.2) serve N canali:

```
mb-conductor
   └── swarm_init(topology: hierarchical)
        ├── canale-1 (brand_kit_1) → squadra: strategy+opt+publish, namespace mb/yt/canale-1
        ├── canale-2 (brand_kit_2) → squadra clonata,             namespace mb/yt/canale-2
        └── canale-N ...           → spawn on-demand, pool worker Haiku/WASM condiviso
```

Regole multi-canale: (a) niche diverse o angoli diversi — mai due canali identici (rischio
spam network); (b) memoria isolata per canale + memoria condivisa `mb/yt/patterns` per i
pattern che funzionano ovunque; (c) Cost-Sentinel con budget per-canale; (d) un canale nuovo
si apre SOLO quando il precedente ha gate stabili (criterio in §11, F-MB5).

---

## 5. PUBLISHING/KDP in profondità

### 5.1 Pipeline libro end-to-end (integra asset esistenti)

```
1. NICHE RESEARCH        WF-PUB-NICHE: keyword KDP, BSR competitor, gap catalogo
        │                  → scheda niche + spec libro (formato, lunghezza, angolo)
2. ORDINE MANOSCRITTO    WF-PUB-BOOK-ORDER → Content-Factory:
        │                  {brand_kit, formato: manoscritto_md + image_prompts.yaml,
        │                   quantità: 1, spec: n_capitoli/parole/stile}
3. IMPAGINAZIONE         WF-PUB-LAYOUT: book-factory ESISTENTE (Workflow-libri/)
        │                  orchestrator.py → generate_images → build_book → qa_checker
        │                  output: book_final.pdf 6x9 + qa_report.md   [GATE LAYOUT]
4. COVER                 WF-PUB-COVER: spec cover (trim+spine da n. pagine) → ordine a CF
        │                  → cover print-ready + versione ebook          [GATE COVER]
5. LISTING               WF-PUB-LISTING: copy a Marketing (APSOC), 7 keyword,
        │                  categorie, pricing                            [GATE LISTING]
6. PUBBLICAZIONE         WF-PUB-PUBLISH: upload KDP, review umana obbligatoria,
        │                  checklist conformità KDP (incl. disclosure contenuto AI)
7. MONITOR               WF-PUB-MONITOR: BSR, recensioni, royalty → feedback a (1)
```

### 5.2 Integrazione asset esistenti

| Asset | Come si integra |
|---|---|
| `Workflow-libri/` (book-factory: 3 agenti — Image Generator, Layout Engine, QA) | Diventa il motore di `WF-PUB-LAYOUT` così com'è (migrazione = wrapper, mai riscrittura — rischio §9 del Piano Maestro). I 3 agenti interni diventano funzioni L4: T-image-prompts, T-layout-engine, T-book-qa |
| `KDP - prodottti digitali/` (LIBRO 1-5, Carousel Factory, landing) | LIBRO 1-5 = backlog/catalogo da censire in `WF-PUB-MONITOR`; Carousel Factory → promo social (ordini a Content-Factory/Marketing) |
| Suite `printing-press*` (genera CLI Go ship-ready per API, con polish/score/publish) | Doppio uso: (a) Platform la usa per forgiare il tooling MB (es. CLI `kdp-helper`, CLI YouTube Data API); (b) il suo pattern score→polish→publish è il modello dei QA gate MB (scorecard prima della pubblicazione) |
| `book-to-skill` | Converte i libri prodotti in skill → asset riusabile da Info-Business (cross-sell: libro → corso) |
| `Lanco ebook/`, `Strategia Ebook _ Kpd - pr. TikTock.pdf` | Conoscenza di lancio/promo → da ingerire in wiki (Intelligence) e riusare in WF-PUB-LISTING |

### 5.3 QA gate libro

| Gate | Criteri |
|---|---|
| **Layout Gate** | PDF esattamente 6x9; ogni capitolo ha pagina immagine; zero placeholder grigi residui; `qa_report.md` verde |
| **Cover Gate** | dimensioni trim+bleed corrette per il n. pagine reale; testo dorso leggibile; conformità template KDP |
| **Listing Gate** | titolo/sottotitolo senza keyword stuffing (policy KDP); descrizione APSOC approvata da Marketing; 7 keyword + 3 categorie coerenti con la niche |
| **Compliance Gate** | checklist contenuti KDP (no contenuto ingannevole/duplicato; disclosure AI dove richiesto da KDP) + review umana finale |

---

## 6. E-COMMERCE — struttura minima vitale + fasi future

**Ora (scheletro, zero spesa):** org L2-L4 documentata (§2.3), agenti definiti ma dormienti,
namespace memoria riservato (`mb/ecom/*`), un solo workflow attivabile: `WF-ECOM-PRODUCT`
(ricerca prodotto pura, eseguita da Intelligence su ordine MB, output = dossier wiki).

**Fasi future (post F-MB7, ordine vincolato):**

| Fase | Cosa | Gate di ingresso |
|---|---|---|
| E1 | Scelta modello (dropshipping / POD / digitale — il POD si aggancia naturalmente a MB-PUB: stessi brand_kit, stesse cover) | dossier WF-ECOM-PRODUCT + decisione mb-conductor + ok umano |
| E2 | Store MVP: 1 store, ≤10 listing (copy → Marketing, visual → Content-Factory) | E1 chiusa, budget approvato |
| E3 | Ads test (strategia con Marketing/Advertising) | E2 live, tracking attivo |
| E4 | Fulfillment monitor + scaling | E3 con unit economics positivi |

**Sinergia prioritaria:** la prima incarnazione e-commerce sarà probabilmente **POD/merch
derivato dal Publishing** (riuso asset, rischio minimo) — decisione formale in E1, non ora.

---

## 7. Asset esistenti → reparto (mappatura, zero orfani — F3 del Piano Maestro)

| Path | Reparto destinazione | Azione |
|---|---|---|
| `Workflow-libri/` (CLAUDE.md, scripts/, agents/, templates/) | MB-PUB / WF-PUB-LAYOUT | Wrappare come motore L3; non riscrivere |
| `Workflow-libri/📚 Piano Completo Sistema Multi-Age.md` | MB-PUB (documentazione) | Ingerire in wiki `tools/` |
| `KDP - prodottti digitali/LIBRO 1..5` | MB-PUB / WF-PUB-MONITOR | Censire catalogo: stato, listing, BSR |
| `KDP - prodottti digitali/GPT - KDP Carousel Factory` | MB-PUB packaging → ordini a Content-Factory | Valutare riuso per promo social |
| `KDP - prodottti digitali/Leanding Page` | Platform (siti) per conto di MB-PUB | Audit + eventuale empire-style |
| `Lanco ebook/` | MB-PUB + Info-Business (confine: ebook venduto fuori KDP = Info-Business) | Ingestione wiki + decisione confine |
| `Strategia Ebook _ Kpd - pr. TikTock (2).pdf` | Intelligence → dossier per MB-PUB | Ingestione Empire Studio/wiki |
| `caroselli/`, `Workfolw crea caroselli à/` | Content-Factory (produzione) — MB è solo committente | Migrare a CF, MB li ordina via contratto |
| Skill `printing-press*` (9 skill) | Platform/Forge — al servizio di MB-PUB | Registrare nel registro skill (07-BACKBONE) |
| Skill `book-to-skill` | MB-PUB → Info-Business (ponte) | Registrare + definire trigger post-pubblicazione |
| Skill `video` | Content-Factory (riferimento produzione) | Registrare; MB la invoca solo via ordine |
| Wiki `Map - Kdp_-_Prodottti_Digitali.md`, `Map - Workflow-Libri.md`, `Map - Lanco_Ebook.md` | BRAIN (wiki) | Aggiornare con la nuova org MB |

---

## 8. Skill — esistenti riusate + NUOVE da forgiare

**Esistenti riusate da MB (nessuna modifica richiesta):**

| Skill | Uso in MB |
|---|---|
| `printing-press` + suite | Forgia CLI tooling (kdp-helper, yt-api) via Platform; modello scorecard per i gate |
| `book-to-skill` | Libro pubblicato → skill → asset Info-Business |
| `content-forge` | Trasforma dossier ingestione F-MB1 in agenti/workflow operativi |
| `cro-copy-architect` / `market-copy` | Copy listing/descrizioni (eseguite da Marketing su ordine MB) |
| `seo-audit` / `ai-seo` / `schema` | Riferimento per descrizioni e landing dei libri |
| `analytics` | Tracking landing/clip cross-platform |
| `memory-empire` / `wiki-context` | Contesto + archiviazione di ogni operazione MB |
| `swarm-orchestration` / `sparc-methodology` | Metodo di build e coordinamento multi-canale |

**NUOVE da creare (ordini alla Forge — contratto §1; kernel ≤500 righe, references/ separate):**

| Skill nuova | Scopo | Priorità |
|---|---|---|
| `yt-niche-research` | Scorecard niche: domanda, competizione, RPM stimato, producibilità AI, rischio policy | P1 (post F-MB1) |
| `yt-script-engine` | Brief script retention-first per CF: hook, loop, struttura per formato `[pattern da ingestione F-MB1]` | P1 |
| `yt-seo-optimizer` | Titolo/descrizione/tag/capitoli policy-safe; checklist SEO Gate #4 | P1 |
| `thumbnail-factory` | Spec + A/B test thumbnail (generazione a CF); test leggibilità 120px | P1 |
| `yt-channel-brandkit` | Genera il brand_kit canale completo (persona, voce TTS, stile visual, naming) | P1 |
| `yt-publish-api` | Upload/scheduling via YouTube Data API + end screen + playlist (CLI via printing-press) | P2 |
| `yt-retention-analyst` | Lettura analytics → diagnosi drop-off → raccomandazioni a script brief | P2 |
| `kdp-niche-research` | Scorecard niche KDP (BSR, keyword, stagionalità, competizione) | P1 |
| `kdp-listing-builder` | Listing completo: 7 keyword, categorie, descrizione (copy da Marketing), pricing | P2 |
| `kdp-compliance-gate` | Checklist policy KDP pre-pubblicazione (incl. disclosure AI) | P2 |
| `ecom-product-research` | Scorecard prodotto (margine, domanda, logistica) | P3 (F-MB7) |

---

## 9. Integrazione Ruflo

```
Ruflo = COORDINA (swarm per canale/libro, memoria, routing) · Claude Code = ESEGUE
```

| Bisogno MB | Tool Ruflo | Configurazione |
|---|---|---|
| N canali / N libri in parallelo | `swarm_init` topology **hierarchical** (mb-conductor in cima), un branch per istanza | fan-out su istanze disgiunte; pipeline dentro ogni istanza (le 4 fasi YT sono sequenziali) |
| Spawn squadre per istanza | `agent_spawn` / `managed_agent_*` | coordinator on-demand; pool worker Haiku/WASM condiviso |
| Decisioni (aprire canale, killare niche) | `hive-mind propose/vote` (raft) con C-Suite | solo decisioni con spesa o rischio policy |
| Memoria | `memory_store/search` namespace dedicati (sotto) | ogni write rilevante → anche wiki `log.md` (pattern 12) |
| Apprendimento | `reasoningbank-*` su ogni gate rosso; `neural_train` sui pattern titolo/thumbnail vincenti | feedback WF-YT-ANALYTICS e WF-PUB-MONITOR |
| Costi | Cost-Sentinel + budget per-istanza; dry-run default (pattern 3) | nessun ordine a CF senza stima costo |

**Namespace memoria (convenzione):**

```
mb/strategy                  decisioni di portafoglio (quali business, quali budget)
mb/yt/patterns               pattern cross-canale (hook, titoli, thumbnail che funzionano)
mb/yt/<canale-slug>/         brand_kit, calendario, storico video, metriche, gate-log
mb/pub/patterns              pattern cross-libro (niche, listing, cover)
mb/pub/<libro-slug>/         spec, stato pipeline, qa_report, royalty
mb/ecom/<store-slug>/        (riservato, dormiente)
```

**Regola d'isolamento:** un agente che lavora su `canale-1` legge `mb/yt/canale-1/*` +
`mb/yt/patterns`, MAI il namespace di un altro canale (anti cross-contaminazione §4.5).

---

## 10. KPI + quality gates

| Livello | KPI | Soglia / uso |
|---|---|---|
| Video (48h/7gg) | CTR thumbnail; retention media %; % vista dei primi 30s; impression | baseline fissata dopo i primi 10 video del canale — NON si inventano benchmark prima `[da ingestione F-MB1 + dati reali]` |
| Canale (mensile) | iscritti; watch-time; RPM (post-monetizzazione); % video gate-verdi al primo colpo; costo/video | trend: ogni metrica letta da WF-YT-ANALYTICS → memoria |
| Libro (mensile) | BSR; vendite/royalty; recensioni (media, n); resa pipeline (giorni niche→pubblicato) | WF-PUB-MONITOR; un libro sotto soglia per 90gg → decisione kill/relaunch |
| Ecosistema | revenue per sotto-business; costo agenti per istanza (cost-attribution); n istanze attive con gate stabili | report mensile di mb-conductor alla C-Suite |
| Qualità (sempre) | 100% pubblicazioni passate dai gate; 0 strike policy; 0 rejection monetizzazione non previste | qualsiasi strike → freeze canale + post-mortem ReasoningBank |

**Quality gates riassunto (tutti bloccanti):** Script/Audio/Visual/SEO + Policy/Brand per
video (§4.3); Layout/Cover/Listing/Compliance per libro (§5.3); dry-run + Cost-Sentinel per
ogni ordine a Content-Factory; review umana su ogni pubblicazione finché `mb-conductor` +
C-Suite non revocano il vincolo (criterio: 20 pubblicazioni consecutive senza correzioni umane).

---

## 11. Fasi di build (ordinate, con gate — allineate a F7/F9+ del Piano Maestro)

| Fase | Cosa | Gate di uscita |
|---|---|---|
| **F-MB1 — INGESTIONE** (prima, vincolante) | Sessione dedicata Empire Studio su `@Legamidiamore` e `@dosementale`: frame reali + visione Claude. Ordine a Intelligence: `{dominio: yt-automation, output: 2 dossier}`. Estrarre: niche/angolo, formato, struttura script, stile visual/TTS, packaging, cadenza, segnali di monetizzazione | 2 dossier in wiki `sources/` + 1 synthesis comparativa; pattern operativi estratti e salvati in `mb/yt/patterns` |
| **F-MB2 — SCAFFOLDING** | Org `company/05-multibusiness/` (L2→L5), namespace memoria, registrazione asset §7, ordini alla Forge per le skill P1 (§8) | struttura navigabile; skill P1 consegnate e conformi; zero orfani tra gli asset §7 |
| **F-MB3 — CANALE PILOTA** | WF-YT-NICHE (informata dai dossier F-MB1) → WF-YT-CHANNEL-LAUNCH → brand_kit → calendario 30gg | scheda niche approvata da mb-conductor + ok umano; canale creato; calendario pronto |
| **F-MB4 — PRIMO VIDEO** | Primo giro completo: ordine a CF → 4 gate → ottimizzazione → pubblicazione con review umana (= F7 Piano Maestro: "primo video pubblicato") | 1 video pubblicato con tutti i gate verdi; post-mortem in ReasoningBank |
| **F-MB5 — REGIME + MULTI-CANALE** | Cadenza warm-up sul pilota; quando ≥10 video con ≥80% gate verdi al primo colpo → secondo canale via swarm (brand_kit_2) | 2 canali in parallelo, memoria isolata, cost-attribution per canale |
| **F-MB6 — PUBLISHING RILANCIO** | Pipeline §5 end-to-end su 1 libro nuovo: wrapper book-factory, gate libro, listing via Marketing, pubblicazione con review | 1 libro pubblicato gate-verde; catalogo LIBRO 1-5 censito in WF-PUB-MONITOR |
| **F-MB7 — E-COMM MVP** | Solo dopo F-MB5 e F-MB6 stabili: fase E1-E2 (§6) | dossier prodotto + decisione modello + store MVP (se approvato) |

Ogni fase: checkpoint memoria, log in `wiki/log.md`, verify Empire verde prima di passare oltre.

---

## 12. Rischi & mitigazioni

| Rischio | Probabilità/Impatto | Mitigazione |
|---|---|---|
| **Ban/strike policy YouTube** (reused content, spam, metadata ingannevoli, network di canali) | media / critico | Policy/Brand Gate pre-upload obbligatorio; niche/angoli distinti per canale; cadenza warm-up; mai pubblicazione automatica senza gate; freeze immediato + post-mortem al primo strike |
| **Rejection monetizzazione YPP** (contenuto "ripetitivo/riutilizzato" tipico dei canali full-AI) | alta / alto | originalità misurata (similarity check anti-ripetitività nel Script Gate); valore aggiunto reale per video (angolo, struttura, dati); studio F-MB1 di come i canali riferimento superano questo scoglio `[da ingestione F-MB1]` |
| **Contenuto ripetitivo / decadimento qualità su volume** | alta / alto | soglia similarità vs ultimi 20 script; rotazione format dal calendario; WF-YT-ANALYTICS che retro-alimenta i brief; la cadenza non supera mai la capacità dei gate |
| **Disclosure contenuti AI** (YouTube: contenuti sintetici realistici; KDP: dichiarazione AI) | media / medio | checklist disclosure dentro Policy Gate (YT) e Compliance Gate (KDP); regola fissa: si dichiara dove la piattaforma lo richiede, sempre |
| **Copyright** (musica, B-roll, immagini nei video e nei libri) | media / alto | nei contratti verso CF: solo asset generati o licenziati, fonte tracciata nel payload; Visual Gate verifica watermark/asset sospetti |
| **Costi API** (HeyGen, ElevenLabs, image gen) fuori controllo su N canali | media / medio | dry-run con stima costo prima di ogni ordine; Cost-Sentinel con budget per-istanza; 3-tier routing; nessuna spesa senza ok esplicito (OUT OF SCOPE §0) |
| **Sospensione account KDP** (qualità, duplicazione, violazioni) | bassa / critico | Compliance Gate + review umana obbligatoria; qualità via book-qa; mai mass-publishing di libri low-effort |
| **Dipendenza da piattaforma** (YouTube/Amazon cambiano regole) | media / alto | clip cross-platform (Shorts/TikTok/Reels) per de-rischiare la distribuzione; e-comm/landing proprie come secondo canale di revenue; monitoraggio policy in WF-PUB-MONITOR / WF-YT-ANALYTICS |
| **Costruire la cattedrale prima del primo video** | media / alto | la roadmap §11 forza output reale presto (F-MB4 = video vero); scheletro e-comm congelato fino a F-MB7 |
| **Divergenza wiki/AgentDB sulle N istanze** | media / medio | pattern 12 wiki-first: ogni gate, pubblicazione e decisione logga in `wiki/log.md`; wiki-syncer di Memory Empire |

---

## Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia, backbone, pattern 1-12, roadmap F7/F9+
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — fornitore di tutta la produzione materiale MB
- [[04-ECOSISTEMA-MARKETING]] — copy APSOC per listing, titoli, ads
- [[Empire_Studio]] — motore dell'ingestione F-MB1 (frame reali + visione Claude)
- [[Memory_Empire]] — archiviazione e enrichment della conoscenza MB
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo: swarm, memoria, consensus
- [[Map - Workflow-Libri]] · [[Map - Kdp_-_Prodottti_Digitali]] — asset Publishing esistenti
