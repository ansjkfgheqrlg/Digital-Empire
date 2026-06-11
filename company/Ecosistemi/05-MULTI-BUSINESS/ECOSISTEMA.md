# 🏭 05 — MULTI-BUSINESS

> **Livello:** L1 · **Priorità:** MEDIA-ALTA (YouTube = sotto-ecosistema prioritario) · **Stato:** parziale (KDP + Workflow-libri attivi; YT/E-comm da costruire)
> **Dossier vincolante:** `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md` · **Backbone locale:** `BACKBONE.md`
>
> ⚠️ **Vincolo di onestà (dal dossier §0):** i canali YouTube di riferimento `@Legamidiamore` e
> `@dosementale` NON sono ancora stati analizzati. Ogni parametro che dipende da loro è marcato
> `[da ingestione F-MB1]` e si fissa SOLO dopo l'ingestione Empire Studio (F-MB1). Nessun dato
> su quei canali in questa documentazione è inventato.

---

## 1. Missione

Costruire e gestire **N business digitali scalabili in parallelo** — canali YouTube completamente
automatizzati, un catalogo libri KDP in crescita continua, store e-commerce — dove ogni
"istanza di business" (canale, libro, store) è un `brand_kit` servito dallo stesso motore di
agenti (**pattern 11: multi-tenant by design**).

Multi-Business **NON produce asset materiali**: li **ordina** a Content-Factory e li
**trasforma in revenue** tramite strategia, ottimizzazione e pubblicazione. La regola di
confine (non negoziabile, dossier §1):

- creare un asset → **03 Content-Factory**
- scrivere copy persuasivo → **04 Marketing**
- capire/ricercare → **08 Intelligence**
- Multi-Business tiene SOLO: scelta niche/prodotto, calendario, QA gate finale d'istanza,
  ottimizzazione metadati, pubblicazione, monitoraggio revenue.

## 2. DONE WHEN

1. Org L2→L5 dei 3 sotto-ecosistemi documentata e navigabile (questa cartella).
2. Ingestione Empire Studio dei 2 canali riferimento completata → 2 dossier in wiki `sources/`.
3. Primo canale YouTube pilota attivo: niche scelta, calendario, ≥1 video pubblicato che ha
   superato TUTTI e 4 i QA gate (script, audio, visual, SEO).
4. Pipeline libro KDP end-to-end eseguita una volta integrando `Workflow-libri/` (book-factory):
   manoscritto → PDF 6x9 → cover → listing → pubblicazione (con review umana).
5. Multi-canale dimostrato: ≥2 canali in parallelo via swarm, ognuno col suo brand_kit e
   namespace memoria, zero cross-contaminazione.
6. E-commerce: struttura minima vitale documentata (anche se non attiva) + backlog fasi future.
7. KPI tracciati per ogni istanza (§7) e loggati in wiki + AgentDB; zero pubblicazioni
   automatiche senza gate verdi.

**OUT OF SCOPE (ora):** spesa API (HeyGen/ElevenLabs/ads) senza ok esplicito; pubblicazione
YouTube/KDP senza review umana nelle prime fasi; e-commerce operativo (solo scheletro).

---

## 3. I tre sotto-ecosistemi — org L2 → L5

### 3.1 (A) YOUTUBE AUTOMATION — `MB-YT` · priorità ALTA

Pipeline end-to-end **16 step** (dossier §4.1) in 4 fasi, con **4 QA gate bloccanti** + Policy/Brand gate:

```
FASE 1 RICERCA/STRATEGIA (step 1-4)   FASE 2 PRODUZIONE via CF (step 5-9)
1 niche research                       5 research argomento video
2 competitor map [da ingestione F-MB1] 6 script           → GATE #1 Script
3 brand_kit canale                     7 voiceover TTS    → GATE #2 Audio
4 calendario editoriale                8 visual AI/B-roll → GATE #3 Visual
                                       9 thumbnail        → (con gate #3)
FASE 3 OTTIMIZZAZIONE (step 10-12)    FASE 4 PUBBLICAZIONE (step 13-16)
10 titolo + descrizione SEO            13 upload YouTube Data API
11 tag + end screen + cards            14 scheduling
12 SEO gate (#4) + brand gate          15 clip cross-platform
                                       16 analytics → feedback a FASE 1
```

I passi 5-9 sono **eseguiti da Content-Factory** su ordine `WF-YT-VIDEO-ORDER`; MB valida la
consegna e possiede i gate.

| Reparto L2 | Workflow L3 | Funzioni L4 |
|---|---|---|
| [YT-Strategia](Reparti/YT-Strategia/README.md) | WF-YT-NICHE · WF-YT-CHANNEL-LAUNCH · WF-YT-CALENDAR | T-niche-scout · T-competitor-map · T-keyword-yt · T-brandkit-builder · T-calendar-planner |
| [YT-Produzione](Reparti/YT-Produzione/README.md) (interfaccia) | WF-YT-VIDEO-ORDER | T-brief-compiler · T-handoff-validator · T-asset-receiver |
| [YT-Ottimizzazione](Reparti/YT-Ottimizzazione/README.md) | WF-YT-OPT | T-title-lab · T-description-seo · T-tags · T-endscreen-cards · T-thumb-ab |
| [YT-Pubblicazione](Reparti/YT-Pubblicazione/README.md) | WF-YT-PUBLISH · WF-YT-ANALYTICS | T-uploader-api · T-scheduler · T-clip-crossposter · T-metrics-reader · T-retention-analyst |

**Multi-canale:** ogni canale = un `brand_kit`; lo stesso motore serve N canali via swarm
(branch per istanza, namespace `mb/yt/<canale-slug>/`, pool worker Haiku/WASM condiviso).
Mai due canali identici; memoria isolata + `mb/yt/patterns` condiviso; budget per-canale;
un canale nuovo si apre solo con gate stabili sul precedente (F-MB5).

### 3.2 (B) PUBLISHING/KDP — `MB-PUB` · priorità MEDIA-ALTA (asset esistenti)

Pipeline libro **7 step** (dossier §5.1), un workflow per step:

```
1 WF-PUB-NICHE       niche/keyword KDP, BSR competitor → scheda niche + spec libro
2 WF-PUB-BOOK-ORDER  ordine manoscritto+image_prompts a Content-Factory
3 WF-PUB-LAYOUT      book-factory ESISTENTE (Workflow-libri/) → PDF 6x9   [GATE LAYOUT]
4 WF-PUB-COVER       spec cover (trim+spine) → ordine a CF                [GATE COVER]
5 WF-PUB-LISTING     copy a Marketing (APSOC), 7 keyword, categorie       [GATE LISTING]
6 WF-PUB-PUBLISH     upload KDP + review umana obbligatoria               [GATE COMPLIANCE]
7 WF-PUB-MONITOR     BSR, recensioni, royalty → feedback a (1)
```

| Reparto L2 | Workflow L3 | Funzioni L4 |
|---|---|---|
| [PUB-Ricerca](Reparti/PUB-Ricerca/README.md) | WF-PUB-NICHE | T-kdp-niche-scout · T-keyword-kdp · T-competition-grader |
| [PUB-Produzione](Reparti/PUB-Produzione/README.md) (interfaccia) | WF-PUB-BOOK-ORDER · WF-PUB-LAYOUT | T-manuscript-brief · T-image-prompts · T-layout-engine · T-book-qa |
| [PUB-Packaging](Reparti/PUB-Packaging/README.md) | WF-PUB-COVER · WF-PUB-LISTING | T-cover-spec · T-listing-builder · T-category-picker |
| [PUB-Pubblicazione](Reparti/PUB-Pubblicazione/README.md) | WF-PUB-PUBLISH · WF-PUB-MONITOR | T-kdp-uploader · T-pricing · T-royalty-tracker · T-review-watcher |

`Workflow-libri/` (book-factory: orchestrator.py → generate_images → build_book → qa_checker)
diventa il motore di WF-PUB-LAYOUT **così com'è** (wrapper, mai riscrittura — ADR-003).
Catalogo esistente `KDP - prodottti digitali/LIBRO 1..5` → censito da WF-PUB-MONITOR.

### 3.3 (C) E-COMMERCE — `MB-ECOM` · priorità MEDIA (solo struttura minima)

Scheletro a zero spesa: org documentata, agenti definiti ma **dormienti**, namespace
`mb/ecom/*` riservato. Unico workflow attivabile: `WF-ECOM-PRODUCT` (ricerca prodotto pura,
eseguita da Intelligence su ordine MB, output = dossier wiki).

| Reparto L2 | Workflow L3 (dormienti tranne WF-ECOM-PRODUCT) | Funzioni L4 |
|---|---|---|
| [ECOM-Ricerca](Reparti/ECOM-Ricerca/README.md) | WF-ECOM-PRODUCT | T-product-scout · T-margin-calculator |
| [ECOM-Store](Reparti/ECOM-Store/README.md) | WF-ECOM-STORE | T-store-setup · T-listing-ecom |
| [ECOM-Crescita](Reparti/ECOM-Crescita/README.md) | WF-ECOM-ADS · WF-ECOM-FULFILL | T-ads-liaison · T-fulfillment-monitor |

Fasi future E1→E4 (gate vincolati, post F-MB7): scelta modello (POD agganciato a MB-PUB è
la sinergia prioritaria) → store MVP ≤10 listing → ads test → fulfillment + scaling.

---

## 4. Roster agenti L5 (28 — schede complete in `Agenti/`)

| ID | Ruolo | Tipo | Tier |
|---|---|---|---|
| [mb-conductor](Agenti/mb-conductor.md) | Dirige l'ecosistema, alloca budget A/B/C, risponde alla C-Suite | coordinator | Opus |
| [mb-yt-strategy-coord](Agenti/mb-yt-strategy-coord.md) | Coordina YT-Strategia | coordinator | Sonnet |
| [mb-yt-niche-scout](Agenti/mb-yt-niche-scout.md) | Scansione niche, volume/competizione, RPM stimato | worker | Sonnet |
| [mb-yt-competitor-mapper](Agenti/mb-yt-competitor-mapper.md) | Mappa canali competitor (post F-MB1) | worker | Sonnet |
| [mb-yt-keyword-miner](Agenti/mb-yt-keyword-miner.md) | Keyword research YouTube | worker | Haiku |
| [mb-yt-brandkit-builder](Agenti/mb-yt-brandkit-builder.md) | Compila brand_kit canale | worker | Sonnet |
| [mb-yt-calendar-planner](Agenti/mb-yt-calendar-planner.md) | Calendario editoriale per canale | worker | Haiku |
| [mb-yt-brief-compiler](Agenti/mb-yt-brief-compiler.md) | Compila il brief-ordine video per CF | worker | Sonnet |
| [mb-yt-handoff-validator](Agenti/mb-yt-handoff-validator.md) | Valida la consegna CF (gate #2/#3) | worker | Sonnet |
| [mb-yt-opt-coord](Agenti/mb-yt-opt-coord.md) | Coordina YT-Ottimizzazione e i 4 QA gate | coordinator | Sonnet |
| [mb-yt-title-smith](Agenti/mb-yt-title-smith.md) | Varianti titolo CTR-first, policy-safe | worker | Sonnet |
| [mb-yt-seo-writer](Agenti/mb-yt-seo-writer.md) | Descrizione SEO, tag, capitoli | worker | Haiku |
| [mb-yt-thumb-strategist](Agenti/mb-yt-thumb-strategist.md) | Spec thumbnail + A/B test | worker | Sonnet |
| [mb-yt-publish-coord](Agenti/mb-yt-publish-coord.md) | Coordina pubblicazione e cross-posting | coordinator | Sonnet |
| [mb-yt-uploader](Agenti/mb-yt-uploader.md) | Upload via YouTube Data API | worker | WASM/Haiku |
| [mb-yt-clipper](Agenti/mb-yt-clipper.md) | Ordina clip verticali a CF e li distribuisce | worker | Haiku |
| [mb-yt-retention-analyst](Agenti/mb-yt-retention-analyst.md) | Analytics → diagnosi drop-off → correzioni | worker | Sonnet |
| [mb-pub-coord](Agenti/mb-pub-coord.md) | Coordina l'intera pipeline libro KDP | coordinator | Sonnet |
| [mb-pub-niche-scout](Agenti/mb-pub-niche-scout.md) | Niche research KDP (BSR, keyword, gap) | worker | Sonnet |
| [mb-pub-layout-operator](Agenti/mb-pub-layout-operator.md) | Esegue book-factory (orchestrator.py) | worker | WASM/Haiku |
| [mb-pub-book-qa](Agenti/mb-pub-book-qa.md) | QA PDF 6x9 — estende qa_checker.py | worker | Sonnet |
| [mb-pub-listing-builder](Agenti/mb-pub-listing-builder.md) | Assembla listing + categorie + 7 keyword | worker | Haiku |
| [mb-pub-publisher](Agenti/mb-pub-publisher.md) | Upload KDP + pricing + checklist | worker | Haiku |
| [mb-pub-royalty-tracker](Agenti/mb-pub-royalty-tracker.md) | Monitora BSR/royalty/recensioni | worker | WASM/Haiku |
| [mb-ecom-coord](Agenti/mb-ecom-coord.md) | Coordina e-commerce (dormiente fino a F-MB7) | coordinator | Sonnet |
| [mb-ecom-product-scout](Agenti/mb-ecom-product-scout.md) | Ricerca prodotto + margini | worker | Sonnet |
| [mb-ecom-fulfill-monitor](Agenti/mb-ecom-fulfill-monitor.md) | Monitor ordini/fulfillment | worker | WASM/Haiku |
| [mb-qa-sentinel-liaison](Agenti/mb-qa-sentinel-liaison.md) | Interfaccia con le Sentinelle del Backbone | worker | Sonnet |

Spawn on-demand via Ruflo `agent_spawn`: i coordinator esistono solo quando il loro workflow
è attivo; i worker WASM/Haiku sono pool riusabili tra canali/libri.

---

## 5. Flusso tipo (un video YouTube, dalla slot calendario alla pubblicazione)

1. `mb-yt-calendar-planner` espone la slot del giorno (titolo provvisorio + keyword target).
2. `mb-yt-brief-compiler` compila l'ordine a Content-Factory: `{brand_kit, formato: video_long,
   quantità: 1, spec: durata/TTS/stile_visual, deadline}` — dry-run costo → Cost-Sentinel.
3. CF produce script → **GATE #1** (mb-yt-opt-coord + Brand-Voice Sentinel); voiceover →
   **GATE #2**; visual+thumbnail → **GATE #3** (mb-yt-handoff-validator + Quality Sentinel).
4. `WF-YT-OPT`: titolo (title-smith) + descrizione/tag (seo-writer) + thumbnail scelta
   (thumb-strategist) → **GATE #4 SEO**.
5. `mb-qa-sentinel-liaison` esegue il **Policy/Brand Gate** pre-upload (checklist policy
   YouTube + Mandato Empire).
6. `mb-yt-uploader` carica via YouTube Data API; `mb-yt-publish-coord` schedula; review umana
   (vincolo attivo finché 20 pubblicazioni consecutive senza correzioni).
7. `mb-yt-clipper` ordina clip verticali a CF e li distribuisce (Shorts/TikTok/Reels).
8. A 48h/7gg/28gg `mb-yt-retention-analyst` legge le metriche → raccomandazioni → memoria
   `mb/yt/<canale>/` + calendario. Ogni gate rosso → ReasoningBank.

## 6. Quality gate (tutti bloccanti — pattern 4)

| Pipeline | Gate | Owner |
|---|---|---|
| Video | #1 Script · #2 Audio · #3 Visual · #4 SEO · +Policy/Brand pre-upload | mb-yt-opt-coord · mb-yt-handoff-validator · mb-qa-sentinel-liaison |
| Libro | Layout · Cover · Listing · Compliance (+ review umana finale) | mb-pub-coord + mb-pub-book-qa |
| Ordini a CF | dry-run + Cost-Sentinel verde prima di ogni ordine | mb-conductor |

Un gate rosso → il pacchetto torna al team responsabile col report di failure (ReasoningBank,
pattern 5). Mai override manuale senza decisione di `mb-conductor`.

## 7. KPI

| Livello | KPI | Soglia / uso |
|---|---|---|
| Video (48h/7gg) | CTR thumbnail; retention media %; % vista primi 30s; impression | baseline fissata dopo i primi 10 video del canale — NON si inventano benchmark prima `[da ingestione F-MB1 + dati reali]` |
| Canale (mensile) | iscritti; watch-time; RPM (post-monetizzazione); % video gate-verdi al primo colpo; costo/video | trend letto da WF-YT-ANALYTICS → memoria |
| Libro (mensile) | BSR; vendite/royalty; recensioni (media, n); resa pipeline (giorni niche→pubblicato) | WF-PUB-MONITOR; libro sotto soglia 90gg → decisione kill/relaunch |
| Ecosistema | revenue per sotto-business; costo agenti per istanza; n istanze attive con gate stabili | report mensile di mb-conductor alla C-Suite |
| Qualità | 100% pubblicazioni passate dai gate; 0 strike policy; 0 rejection monetizzazione impreviste | strike → freeze canale + post-mortem ReasoningBank |

## 8. Fasi di build (gate di uscita per fase — dossier §11)

| Fase | Cosa | Gate di uscita |
|---|---|---|
| **F-MB1 INGESTIONE** (prima, vincolante) | Empire Studio su `@Legamidiamore` e `@dosementale` (frame reali + visione Claude), ordine a Intelligence | 2 dossier wiki `sources/` + 1 synthesis; pattern in `mb/yt/patterns` |
| **F-MB2 SCAFFOLDING** | Questa org L2→L5, namespace memoria, registrazione asset, skill P1 alla Forge | struttura navigabile; skill P1 consegnate; zero orfani |
| **F-MB3 CANALE PILOTA** | WF-YT-NICHE → WF-YT-CHANNEL-LAUNCH → brand_kit → calendario 30gg | niche approvata + ok umano; canale creato |
| **F-MB4 PRIMO VIDEO** | Primo giro completo: ordine a CF → 4 gate → pubblicazione con review umana | 1 video pubblicato gate-verde; post-mortem ReasoningBank |
| **F-MB5 REGIME + MULTI-CANALE** | Warm-up; con ≥10 video e ≥80% gate verdi al primo colpo → secondo canale | 2 canali in parallelo, memoria isolata, cost-attribution |
| **F-MB6 PUBLISHING RILANCIO** | Pipeline 7 step su 1 libro nuovo via wrapper book-factory | 1 libro pubblicato gate-verde; catalogo LIBRO 1-5 censito |
| **F-MB7 E-COMM MVP** | Solo dopo F-MB5+F-MB6 stabili: fasi E1-E2 | dossier prodotto + decisione modello + store MVP (se ok) |

Cadenza pubblicazione YT: warm-up 2-3 video/settimana; regime `[da ingestione F-MB1: cadenza
reale dei canali riferimento]` — default 3-5/settimana SE i gate reggono (qualità > volume);
Shorts 1-2/giorno derivati dai long-form.

## 9. Rischi principali (mitigazioni complete: dossier §12)

- **Ban/strike policy YouTube** → Policy Gate pre-upload obbligatorio, niche distinte, warm-up, freeze immediato al primo strike.
- **Rejection monetizzazione YPP** (contenuto "ripetitivo") → similarity check anti-ripetitività nello Script Gate, valore aggiunto per video, studio F-MB1.
- **Costi API fuori controllo** → dry-run, Cost-Sentinel per-istanza, 3-tier routing, zero spesa senza ok.
- **Sospensione KDP** → Compliance Gate + review umana, mai mass-publishing low-effort.
- **Cattedrale prima del primo video** → F-MB4 forza output reale presto.

## Connessioni

- `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md` — dossier vincolante
- `../03-CONTENT-FACTORY/` — fornitore di tutta la produzione materiale
- `../04-MARKETING/` — copy APSOC per listing, titoli, ads
- `../08-INTELLIGENCE/` — ricerca, Empire Studio (motore F-MB1)
- `Workflow-libri/` — book-factory reale wrappato da WF-PUB-LAYOUT

*Fonte: `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md` · Aggiornato: 2026-06-11*
