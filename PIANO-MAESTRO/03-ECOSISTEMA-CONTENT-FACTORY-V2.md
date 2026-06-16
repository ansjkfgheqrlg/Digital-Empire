# 🏭 03 — ECOSISTEMA CONTENT-FACTORY V2 (CF-DE)

> Dossier v2 (V2-2, ADR-007) — amplia il v1 `03-ECOSISTEMA-CONTENT-FACTORY.md` a scala CF-grade (MEGA-reparto). Fonte: 11-PIANO-V2 §2.
>
> Questo dossier SUPERA il v1 dove in conflitto con la direttiva di scala. Il v1 resta riferimento per gli asset reali,
> il contratto di ordine e la topologia dei workflow — qui tutto viene portato a standard CF-grade (MEGA-reparto):
> gerarchia a livelli esplicita (leader ecosistema → capi area → coordinatori → verificatori → worker), ogni area
> è un'organizzazione con team 6-10 agenti + workflow propri. Standard: Content Factory Exponium = UN workflow.
>
> Versione: 2.0 · Creato: 2026-06-16 · Fase: V2-2 (dossier architetturali) · Build effettiva: V2-6 (reparti v2).
> Stato: PROGETTATO — l'architettura target v2 è qui descritta. Ciò che wrappa asset esistenti è marcato
> [WRAPPA-ESISTENTE]; ciò che è interamente nuovo è marcato [TARGET-V2].

---

## 0. Missione + DONE WHEN

**Missione.** CF-DE è la fabbrica dei contenuti trasversale di EMPIRE OS: produce asset multi-formato,
multi-brand, multi-cliente per TUTTI gli ecosistemi e per i clienti esterni. Non ha clienti propri:
ha **committenti** (Agency, Info-Business, Marketing, Multi-Business, DE interno) che emettono ordini
strutturati e ricevono deliverable conformi a gate di qualità parametrici sul brand del committente.

In v2 CF-DE è un **MEGA-REPARTO** — un'azienda dentro l'azienda con gerarchia a livelli propria,
tre aree L2, otto reparti L3 interni, roster 80+ agenti, pipeline produzione CF-grade per ogni formato.
Il v1 aveva il modello giusto; mancavano la profondità gerarchica e la densità di team. Questo dossier
colma entrambe.

**DONE WHEN — la build V2-6 di CF-DE è completa quando:**

1. I 3 capi area (Pre-Produzione, Produzione, Post-Produzione) e i loro 8 reparti L3 esistono in
   `company/03-content-factory/` ognuno come struttura-cartella con: `BACKBONE.md`, cartella `agenti/`
   (6-10 schede millimetriche), cartella `workflow/` (1-5 WF CF-grade), `principi/`, `scripts/`,
   `kpi/`, `state/`.
2. Il contratto di ordine `{committente, brand_kit, icp, formato, quantita, deadline, budget}` è
   validato dal CF-Director e produce `orders/<id>/state.json + trace.jsonl` in tutte le esecuzioni.
3. I 5 workflow chiave (carosello, video, articolo/newsletter, thumbnail, publish) girano end-to-end
   con dry-run e gate QA eseguibili; almeno WF-CAROSELLO + WF-PUBLISH con output reale su brand attivo.
4. Il brand-kit registry è operativo con ≥4 brand (brand-agency, brand-education, brand-personal,
   mentalita-brutale) parametrizzati e validati — nessun contenuto hard-coded su un singolo brand.
5. Il layer motori (engines) espone `generate/check/status/estimate` per tutti i motori attivi;
   aggiungere un motore = 1 riga al registry, zero modifiche all'orchestrazione.
6. Swarm mass-production: un batch ≥10 pezzi prodotto in parallelo con budget guard che blocca PRIMA
   di sforare; zero rework per brand-drift tra tenant.
7. Zero asset orfani: tutti i path della sezione 6 mappati a un reparto con azione completata.
8. Review MAXIMILIAN (passo 5-bis, da V2-3) ha approvato: "struttura visibile nell'Explorer?
   millimetrica? non un file ma un'organizzazione?"

**OUT OF SCOPE (v2):** produzione di copy di conversione / sales (dominio di 04-MARKETING);
pricing dei prodotti Agency (dominio A3); automazione della review umana pre-pubblicazione sociale
(resta obbligatoria per policy Board); nuovi motori a crediti senza approvazione budget esplicita.

---

## 1. Posizione nella holding — CF-DE come FORNITORE ASSET

CF-DE è il fornitore di asset produttivi per l'intera holding. La sua unicità è il modello
**multi-tenant a ordine**: ogni input porta il proprio `brand_kit` + `icp`; nessun contenuto
viene prodotto senza questi due input (pattern 11 del Piano Maestro — non negoziabile).

### Contratto di ordine (unico punto di ingresso, v1 confermato)

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
  "note": "vincoli specifici, CTA richiesta, canali destinazione, engine_preference (opzionale)"
}
```

Nessun lavoro parte senza ordine valido. Il CF-Director rifiuta ordini incompleti con escalation
strutturata al committente (mai improvvisazione).

### Schema brand_kit (cuore del multi-tenant — pattern 11)

```json
{
  "slug": "mentalita-brutale",
  "nome": "Mentalità Brutale",
  "handle": {"ig": "@mentalita.brutale", "tiktok": null, "yt": null},
  "visual": {
    "palette": {"primary": "#hex", "accent": "#hex", "bg": "#hex"},
    "font": {"display": "Anton", "body": "Inter"},
    "logo": "brands/mentalita-brutale/assets/LOGO.png",
    "stile": "dark, gradiente rosso/argento",
    "canva_brand_template_ids": []
  },
  "voice": {
    "tono": "diretto, brutale, zero fronzoli",
    "esempi_si": ["frasi conformi..."],
    "esempi_no": ["frasi bandite..."],
    "parole_vietate": []
  },
  "soul_id": null,
  "canali": [{"tipo": "ig", "publisher": "mentalita_orchestrator.py", "review_umana": true}]
}
```

Un workflow che non accetta `brand_kit` + `icp` non è conforme. Il GATE-BRAND è parametrico:
legge il brand_kit dell'ordine, non un mandato fisso — questa è la differenza strutturale
rispetto al CF Exponium (mono-brand, mono-scopo).

### Matrice handoff con gli altri ecosistemi

| Ecosistema | Ordina a CF-DE | Fornisce a CF-DE | Contratto |
|---|---|---|---|
| 01 AGENCY | Contenuti per clienti (deliverable Content Factory €3.500), creative outreach, case study visuali | brand_kit+icp cliente, accesso account cliente | HC-AG-CF-01 |
| 02 INFO-BUSINESS | Asset lancio: caroselli, VSL, email-ready, grafiche sales page | calendario lancio, offerta, price point | HC-IB-CF-01 (priorità alta in finestra lancio) |
| 04 MARKETING | Creative per ads (ad-creative), visual A/B test; riceve copy APSOC validato | **Copy APSOC completato** — CF scrive solo copy strutturale (slide, caption, script base); MKT scrive persuasione | HC-MK-CF-01 bidirezionale |
| 05 MULTI-BUSINESS | Video YouTube (script→render→thumb), copertine KDP, creative e-commerce | brand_kit canale/libro, nicchia, formato piattaforma | HC-MB-CF-01 (batch ricorrenti) |
| 06 PLATFORM | Grafiche per siti (raro) | Tooling: render farm locale, fix script Puppeteer/ffmpeg, hosting asset | ticket CF→PLATFORM |
| 07 FORGE | — | Nuove skill/agenti CF quando KPI calano o serve un nuovo formato | richiesta CF→FORGE con spec |
| 08 INTELLIGENCE | — | Brief di ricerca: trend, hook che performano, analisi competitor | `intel→cf` brief; `cf→wiki` log obbligatorio |
| 09 OPERATIONS | — | Runtime swarm, scheduling cron, storage asset, cost guard centrale | infrastruttura condivisa |
| LX/L0 Board | Contenuti corporate DE | Mandato Empire (gate non parametrici: pricing policy, "prove non promesse") | governance |

**Regola di precedenza coda:** in conflitto, il CF-Director applica `deadline → revenue impact
(Agency/Lanci) → interno`. Escalation al Board via hive-mind solo se due committenti hanno
stessa priorità e budget non copre entrambi.

---

## 2. Gerarchia a livelli (MEGA-REPARTO)

CF-DE ha una gerarchia propria a 5 livelli. Non un dossier con 5 reparti: un'organizzazione
stratificata con leader, capi area, coordinatori di reparto, verificatori e worker.

```
LIVELLO 0 — CF-DIRECTOR (leader ecosistema)
│   Riceve ordini, valida contratto, smista alle aree, gestisce priorità, riporta al Board.
│   Coordinamento cross-area, budget globale CF, escalation committenti.
│
├── LIVELLO 1 — CAPO AREA PRE-PRODUZIONE (L1-PRE)
│   │   Supervisiona Strategia Contenuti (R1) e Brand-Kit Registry (R2).
│   │   Garantisce che ogni ordine abbia brief valido e brand_kit aggiornato prima della produzione.
│   │
│   ├── LIVELLO 2 — R1 STRATEGIA & BRIEF (coordinatore + team)
│   └── LIVELLO 2 — R2 BRAND-KIT & TENANT REGISTRY (coordinatore + team)
│
├── LIVELLO 1 — CAPO AREA PRODUZIONE (L1-PROD)
│   │   Supervisiona Video (R3), Testuale (R4), Visual & Design (R5).
│   │   Orchestra i team di produzione, risolve conflitti di capacità, sceglie engine.
│   │
│   ├── LIVELLO 2 — R3 PRODUZIONE VIDEO (coordinatore + team)
│   ├── LIVELLO 2 — R4 PRODUZIONE TESTUALE (coordinatore + team)
│   └── LIVELLO 2 — R5 VISUAL & DESIGN / CAROSELLI (coordinatore + team)
│
└── LIVELLO 1 — CAPO AREA POST-PRODUZIONE (L1-POST)
    │   Supervisiona QA & Gate (R6), Pubblicazione & Distribuzione (R7), Apprendimento (R8).
    │   Garantisce che nessun asset esca senza gate verdi; presidia il loop di miglioramento.
    │
    ├── LIVELLO 2 — R6 QA & GATE (coordinatore + team — indipendente dalla produzione)
    ├── LIVELLO 2 — R7 PUBBLICAZIONE & DISTRIBUZIONE (coordinatore + team)
    └── LIVELLO 2 — R8 APPRENDIMENTO & OTTIMIZZAZIONE (coordinatore + team)
```

**Invariant cardinale:** R6 QA & Gate è indipendente da TUTTI i reparti di produzione. Chi produce
non si auto-valuta. Il capo area Post-Produzione garantisce questa separazione — non è bypassabile.

---

## 3. Aree e Reparti L2 v2

### CF-R0 — CF-DIRECTOR (leader ecosistema) [TARGET-V2]

**Missione.** Ingresso unico degli ordini, validazione contratto, smistamento alle aree, gestione
priorità e coda, presidio KPI globali, escalation al Board. Il v1 aveva "CF-A00-conductor" come
singolo agente. In v2 il Director è un team dedicato.

**Team agenti (7):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-D-LEAD | CF-Director Lead | opus | Valida ogni ordine in ingresso; decide priorità coda; riporta al Board |
| CF-D-QA | Order Gate Verificatore | sonnet | Controlla completezza contratto: brand_kit+icp presenti e validi; budget dichiarato |
| CF-D-DISPATCH | Order Dispatcher | sonnet | Smista ordini validati alle 3 aree; aggiorna coda in `cf/orders` |
| CF-D-SCHED | Scheduler & Capacity Planner | sonnet | Piano di carico per area; alert se capacità insufficiente; proposta batch merging |
| CF-D-BUDGET | Budget Sentinel Coordinator | haiku | Aggrega stime engine da tutte le aree; alerta CF-D-LEAD se ordine sfora soglia globale |
| CF-D-STATUS | Order Status Monitor | haiku | Dashboard stato ordini in tempo reale; alert committenti su milestone critiche |
| CF-D-LEARN | Director Pattern Learner | sonnet | Aggrega pattern da tutte le aree; report mensile qualità → Board + FORGE |

**Workflow CF-grade (2):**

**WF-ORDER-INTAKE** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: validare ogni ordine in ingresso e aprire la cartella progetto
- Flusso: ordine in ingresso → CF-D-QA (gate: brand_kit+icp presenti, budget dichiarato, formato riconosciuto) → CF-D-DISPATCH crea `orders/<id>/` con state.json+trace.jsonl → CF-D-SCHED assegna slot e area → notifica committente
- Gate BLOCCANTE: ordine con brand_kit mancante o icp mancante = rifiuto automatico con motivo strutturato
- State: `orders/<id>/order.json` + `cf/orders` (registry globale ordini attivi)
- Script: `cf-order` skill [WRAPPA-ESISTENTE]; [TARGET-V2]: aggiunta validazione multi-tenant e capacity check

**WF-DIRECTOR-REVIEW** [TARGET-V2]
- Scopo: review settimanale KPI globali CF + escalation a Board se necessario
- Flusso: CF-D-STATUS aggrega KPI per reparto → CF-D-LEARN elabora pattern → CF-D-LEAD produce report → se KPI calano per 2 cicli: richiesta a 07-FORGE (ADR-007)
- Gate: report entro lunedì ore 10; nessuna metrica inventata (Mandato Art.2)

**Namespace:** `cf/orders` · `cf/kpi`

---

### AREA PRE-PRODUZIONE

#### CF-R1 — STRATEGIA & BRIEF [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Trasformare ogni ordine in un brief eseguibile: angle, hook type, struttura per formato,
calendario, assegnazione reparti di produzione. Nessun contenuto si produce senza brief approvato.
Il v1 aveva un team L4 con 4 funzioni. In v2: team di 8 agenti, 3 workflow CF-grade.

**Team agenti (8):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R1-COORD | Coordinatore Strategia & Brief | sonnet | Orchestra i 3 workflow; riporta a L1-PRE; decide se un angolo è conforme al Mandato prima del brief |
| CF-R1-QA | Verificatore Brief | sonnet | Gate brief: tutti i campi obbligatori (angle, hook_type, struttura, canali, vincoli); blocca se incompleto |
| CF-R1-ANALYST | Brief Analyst | sonnet | Parse ordine; carica brand_kit+icp; identifica vincoli specifici per formato |
| CF-R1-ANGLE | Angle Strategist | sonnet | Produce 3 angle alternativi per ogni brief (da libreria formule + trend INTELLIGENCE) |
| CF-R1-HOOK | Hook Selector | haiku | Sceglie formula hook da libreria (hook-formulas del carousel-factory) coerente con icp |
| CF-R1-TREND | Trend Intake Specialist | haiku | Riceve brief trend da 08-INTELLIGENCE; aggiorna libreria angle per brand/nicchia |
| CF-R1-CAL | Calendar Planner | sonnet | Piano editoriale multi-brand: slot, mix formati, ricorrenze; usa skill content-strategy |
| CF-R1-LEARN | Brief Performance Analyst | sonnet | Correla angle/hook con first-pass rate → aggiorna libreria formule; pattern in `cf/patterns` |

**Workflow CF-grade (3):**

**WF-BRIEF** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: da ordine validato a `brief.json` per ogni pezzo da produrre
- Flusso: CF-R1-ANALYST (carica brand_kit+icp, identifica vincoli) → CF-R1-ANGLE (3 angle) → CF-R1-HOOK (seleziona hook type da libreria) → CF-R1-QA (gate: tutti i campi obbligatori) → `orders/<id>/01-brief/brief.json`
- Gate BLOCCANTE: brief.json deve contenere: angle, hook_type, struttura_formato, canali, vincoli_brand, word_count/durata stimata; mancante = rifiuto con motivo
- State: `orders/<id>/state.json` → fase 01-brief completata con timestamp e owner
- Dry-run: produce `brief-draft.json` senza assegnare slot produzione (zero impatto coda)

**WF-CALENDAR** [TARGET-V2]
- Scopo: piano editoriale multi-brand per committenti con calendario ricorrente
- Flusso: CF-R1-CAL aggrega slot disponibili per area → mix formati per brand (es. 3 caroselli/sett + 1 video/sett per Mentalità Brutale) → CF-R1-TREND aggiunge finestre trend → piano settimanale in `cf/calendars/<brand>`
- Gate: piano consegnato entro venerdì per settimana successiva; nessun slot senza brand_kit validato
- Integrazione: piano si intreccia con WF-CALENDAR di 04-MARKETING per coordinare lancio ads + contenuti organici

**WF-TREND-BRIEF** [TARGET-V2]
- Scopo: brief specializzato per contenuti a finestra temporale stretta (trend, news di nicchia)
- Flusso: `intel→cf` brief da 08-INTELLIGENCE → CF-R1-TREND → CF-R1-ANGLE (angle virale urgente) → CF-R1-QA (gate accelerato ≤30 min) → priorità alta in coda produzione
- Gate: latenza intake→brief ≤1h; trend datato >48h non processato (scartato con motivo)

**Namespace:** `cf/briefs` · `cf/calendars` · `cf/patterns` (hook/angle per brand)
**KPI:** lead time ordine→brief; % brief completi al primo giro; angle usati vs scartati per brand.

---

#### CF-R2 — BRAND-KIT & TENANT REGISTRY [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Creare, mantenere e validare tutti i `brand_kit` e `icp.json` dell'ecosistema. Custode
dell'identità visiva e vocale di ogni tenant. Impedisce il brand-drift. Il v1 aveva solo la funzione
`T-asset-library` e `CF-R4-A06-brandkit-keeper`. In v2: reparto autonomo con 6 agenti, 2 workflow.

**Team agenti (6):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R2-COORD | Coordinatore Brand-Kit | sonnet | Gestisce registry brand; approvazione nuovi tenant; riporta a L1-PRE |
| CF-R2-QA | Verificatore Brand Gate | sonnet | Valida ogni brand_kit: schema completo, palette HEX valida, voice con esempi si/no; blocca brand_kit incompleti |
| CF-R2-CREATOR | Brand-Kit Builder | sonnet | Crea `brands/<slug>/` completo da brief di onboarding tenant (palette, font, logo, voice, soul_id, canali) |
| CF-R2-CANVA | Canva Brand Sync Operator | haiku | Sincronizza brand_kit con Canva brand kits (list-brand-kits, upload-asset); mantiene template Canva per brand |
| CF-R2-DRIFT | Brand Drift Monitor | haiku | Campiona output prodotti vs brand_kit ogni ciclo; alert CF-R2-COORD se deviazione detected |
| CF-R2-ICP | ICP Profiler | sonnet | Crea/aggiorna `brands/<slug>/icp.json`: dolori, desideri, obiezioni, awareness level, linguaggio per brand |

**Workflow CF-grade (2):**

**WF-BRAND-ONBOARDING** [WRAPPA-ESISTENTE (carousel-factory/brands/) + TARGET-V2]
- Scopo: onboardare un nuovo tenant nel registry a partire da brief o da asset esistenti
- Flusso: brief tenant (nome, visuale, voce, canali) → CF-R2-CREATOR crea struttura `brands/<slug>/` → CF-R2-ICP compila `icp.json` → CF-R2-CANVA crea brand kit Canva + carica logo → CF-R2-QA (gate: schema completo) → CF-R2-COORD approva → tenant disponibile per ordini
- Gate BLOCCANTE: brand_kit non approvato = nessun ordine processato per quel tenant; [WRAPPA]: i 4 brand in `carousel-factory/brands/` diventano seed del registry senza riscrittura
- State: `brands/<slug>/state.json` (onboarding phase, approvazione, ultima sync Canva)

**WF-BRAND-MAINTENANCE** [TARGET-V2]
- Scopo: mantenere brand_kit aggiornati e monitorare brand-drift sistematicamente
- Flusso: CF-R2-DRIFT campiona ≥5 output per brand ogni ciclo → compara vs brand_kit → se deviazione: alert CF-R2-COORD → correzione o aggiornamento brand_kit → CF-R2-QA re-valida → versione patchata con changelog
- Cadenza: campionamento ogni ciclo produzione; aggiornamento brand_kit su richiesta committente o su evidenza drift
- Gate: nessun aggiornamento brand_kit senza approvazione CF-R2-COORD + committente brand (se esterno)

**Namespace:** `cf/brand-kits` · `brands/<slug>/` per ogni tenant
**KPI:** n. tenant attivi; brand_kit completi/incompleti; drift alerts per ciclo; latenza onboarding.

---

### AREA PRODUZIONE

#### CF-R3 — PRODUZIONE VIDEO [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Produrre video pronti alla pubblicazione: UGC (Higgsfield), avatar/talking-head (HeyGen),
short-form montati (ffmpeg+TTS). Eredita la pipeline CF Exponium (Soul ID → Image 4K → Motion → Montaggio)
e la parametrizza per multi-tenant e multi-engine. Il v1 aveva 8 agenti e 3 workflow. In v2: 10 agenti, 4 workflow.

**Team agenti (10):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R3-COORD | Coordinatore Produzione Video | sonnet | Orchestra le pipeline video; sceglie engine via capability; riporta a L1-PROD |
| CF-R3-QA | Verificatore Gate Video | sonnet | Esegue GATE-FORMATO video (durata, aspect, codec, loudness) + GATE-BRAND (soul coerente, palette); blocca e non suggerisce |
| CF-R3-SOUL | Soul-ID Curator | haiku | Gestisce soul-id Higgsfield per brand: ricorrenza personaggio, coerenza visiva tra video dello stesso brand |
| CF-R3-IMG | Image Operator (4K) | haiku | Generazione immagini 4K via Higgsfield (port da hf-studio CF Exponium, parametrizzato per brand_kit) |
| CF-R3-MOTION | Motion Operator | haiku | Image→video motion via Higgsfield; gestisce durata e intensità per tipo di contenuto |
| CF-R3-AVATAR | Avatar Operator | haiku | Render HeyGen avatar/talking-head; script→avatar→render; sceglie avatar coerente con brand_kit.voice |
| CF-R3-VO | Voiceover Operator | haiku | TTS voiceover (edge-tts/ElevenLabs) calibrato su `brand_kit.voice`; verifica qualità audio |
| CF-R3-EDIT | Editor ffmpeg | haiku | Montaggio: cut, crop 9:16/1:1/16:9, subtitle-burn, audio-mix, concat, loudness normalizzazione |
| CF-R3-QUEUE | Render Queue Manager | wasm/haiku | Coda render; stima crediti via `estimate()`; blocco pre-render se sfora budget.crediti_engine |
| CF-R3-LEARN | Video Performance Analyst | sonnet | Correla tipo video/soul/durata con engagement (da WF-FEEDBACK) → pattern in `cf/patterns` |

**Workflow CF-grade (4):**

**WF-VIDEO-UGC** [WRAPPA-ESISTENTE (hf-studio CF Exponium) + TARGET-V2]
- Scopo: pipeline video UGC completa via Higgsfield (soul-id ricorrente → immagini 4K → motion → montaggio)
- Flusso: `brief.json` → CF-R3-SOUL (soul-id per brand, crea se non esiste) → CF-R3-IMG (immagini 4K per scene) → CF-R3-MOTION (image→video motion) → CF-R3-QUEUE (stima costi → CF-SENT-COST approva/blocca) → render → CF-R3-VO (voiceover se richiesto) → CF-R3-EDIT (montaggio+subtitle+audio) → CF-R3-QA (GATE-FORMATO + GATE-BRAND)
- Gate: CF-SENT-COST approva prima di ogni render (exit 2 se sfora); CF-R3-QA blocca se codec/aspect/loudness fuori spec
- State: `orders/<id>/state.json` fase 02-video-ugc; `trace.jsonl` ogni chiamata engine con engine_id + crediti stimati
- Dry-run: produce `ugc-intent.json` (prompt, parametri, costo stimato) per ogni engine call — zero crediti consumati
- [WRAPPA]: port parametrizzato di hf-studio CF Exponium (brand_kit al posto di Exponium hard-coded); mai modificare l'originale

**WF-VIDEO-AVATAR** [WRAPPA-ESISTENTE (heygen-studio CF Exponium) + TARGET-V2]
- Scopo: pipeline avatar/talking-head via HeyGen per brand senza soul-id visivo (es. newsletter video, tutorial)
- Flusso: script (da CF-R4 WF-SCRIPT o WF-NEWSLETTER) → CF-R3-AVATAR sceglie avatar coerente con brand_kit → CF-R3-QUEUE stima → render HeyGen → CF-R3-EDIT (intro/outro, subtitle) → CF-R3-QA
- Gate: avatar coerente con voice tone del brand_kit (CF-R3-QA verifica); nessun render senza stima approvata
- Dry-run: produce `avatar-intent.json` (avatar_id, script, durata, costo stimato)
- [WRAPPA]: port di heygen-studio CF Exponium parametrizzato

**WF-SHORTFORM** [TARGET-V2]
- Scopo: montaggio reel/TikTok/Shorts da asset esistenti senza generazione nuova
- Flusso: asset esistenti (video raw, B-roll, immagini) da `orders/<id>/assets/` → CF-R3-EDIT (cut, crop 9:16, sottotitoli, audio) → CF-R3-QA (GATE-FORMATO shortform: ≤60s, 9:16, loudness)
- Gate: durata entro limiti piattaforma (IG 60s, TikTok 3min, YT Shorts 60s); nessun asset coperto da copyright non liberato
- Costo: zero crediti engine (ffmpeg locale)

**WF-BATCH-VIDEO** [TARGET-V2]
- Scopo: produzione batch ≥5 video in parallelo con swarm mesh
- Flusso: CF-R3-COORD fan-out N job indipendenti → CF-R3-QUEUE aggrega stima costi Σ → CF-SENT-COST approva/blocca → N worker paralleli (CF-R3-IMG + CF-R3-MOTION in parallelo per job) → merge risultati → CF-R3-QA su ogni video
- Gate: CF-SENT-COST approva il TOTALE batch prima di avviare qualsiasi render; 1 video fallito non ferma il batch; 3 video falliti → escalation CF-R3-COORD
- Swarm topology: mesh per job paralleli; cap paralleli dalla `budget.tier_max` dell'ordine

**Namespace:** `cf/video` · `cf/souls` (soul-id per brand) · `cf/render-queue`
**KPI:** video prodotti/ciclo; costo per video per engine; first-pass GATE-FORMATO; GATE-BRAND pass rate.

---

#### CF-R4 — PRODUZIONE TESTUALE [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Articoli, newsletter, script video, caption, descrizioni — testo lungo e strutturato.
Il copy di conversione (sales, ads, APSOC) è dominio di 04-MARKETING. CF-R4 produce contenuto;
MARKETING produce persuasione. Sui pezzi ibridi (newsletter con CTA) CF scrive il corpo e richiede
via handoff il blocco APSOC a MARKETING. Il v1 aveva 4 agenti e 3 workflow. In v2: 8 agenti, 4 workflow.

**Team agenti (8):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R4-COORD | Coordinatore Produzione Testuale | sonnet | Orchestra i 4 workflow testuali; gestisce handoff con MARKETING per blocchi APSOC; riporta a L1-PROD |
| CF-R4-QA | Verificatore Gate Copy | sonnet | GATE-COPY preliminare: struttura valida, hook+CTA presenti, zero claim non verificabili; blocca e non suggerisce |
| CF-R4-WRITE | Senior Writer | sonnet | Draft articoli/newsletter/script da brief; applica brand voice del brand_kit; profondità ≥ brief richiede |
| CF-R4-SEO | SEO/AI-SEO Optimizer | haiku | Pass SEO e AI-SEO su articoli: keyword density, heading structure, meta, schema; usa skill seo-audit + ai-seo |
| CF-R4-REPURP | Repurposing Specialist | haiku | Derivati multi-formato da un pezzo madre (skill content-forge): 1 articolo → caption, thread, email, slide copy |
| CF-R4-CAPTION | Caption & Hashtag Writer | haiku | Caption+hashtag calibrati per canale (IG/LinkedIn/TikTok) dal brand_kit.voice e limits piattaforma |
| CF-R4-HEADLINE | Headline Variator | haiku | Varianti titolo per A/B test (n=3 per pezzo); coerenti con hook del brief |
| CF-R4-LEARN | Text Performance Analyst | sonnet | Correla struttura/angolo con engagement testuale → pattern in `cf/patterns`; aggiorna libreria hook |

**Workflow CF-grade (4):**

**WF-ARTICOLO** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: da brief a articolo completo (blog, knowledge base, pillar) con pass SEO
- Flusso: `brief.json` → CF-R4-WRITE (outline → draft completo) → CF-R4-SEO (pass SEO/AI-SEO) → CF-R4-QA (GATE-COPY: struttura, claim verificabili, zero genericità) → GATE-BRAND (tone vs brand_kit) → output: `md` / `html` / email-ready → delivery o publish (blog via 06-PLATFORM)
- Gate: GATE-COPY (struttura heading valida, hook in apertura, CTA coerente con canale); GATE-BRAND (tone voice campionato vs brand_kit.voice.esempi)
- Dry-run: produce outline + stima lunghezza/tier; nessun draft scritto
- State: `orders/<id>/02-copy/articolo.md` + fase in state.json

**WF-NEWSLETTER** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: newsletter completa con corpo CF e blocco CTA via handoff MARKETING
- Flusso: brief → CF-R4-WRITE (corpo newsletter) → CF-R4-CAPTION (preview text, oggetto email ×3 varianti) → richiesta `HC-MK-CF-01` a 04-MARKETING per blocco APSOC/CTA → attesa blocco → merge → CF-R4-QA (GATE-COPY) → GATE-BRAND → output email-ready
- Gate: handoff MARKETING richiesto prima che il blocco CTA venga scritto da CF (confine non valicabile); merge solo con blocco APSOC approvato dalla Copy Guild di MARKETING
- Dipendenza: 04-MARKETING deve essere attivo e rispondere entro SLA dichiarato

**WF-SCRIPT** [TARGET-V2]
- Scopo: script video (YouTube lungo, reel, VSL base) per CF-R3
- Flusso: brief → CF-R4-WRITE (script con struttura: hook 3s, corpo, CTA) → CF-R4-HEADLINE (3 varianti titolo) → CF-R4-QA (GATE-COPY: hook nei 3s, CTA presente, parole_vietate assenti da brand_kit) → output script.md → handoff a CF-R3 (WF-VIDEO-UGC o WF-VIDEO-AVATAR)
- Gate: hook deve essere nei primi 3 secondi/righe; CTA unica; nessuna parola_vietata dal brand_kit

**WF-REPURPOSING** [TARGET-V2]
- Scopo: da un pezzo madre (articolo/video/podcast) derivare N formati secondari in batch
- Flusso: asset madre → CF-R4-REPURP (skill content-forge: transcript/text → derivati) → per ogni formato: CF-R4-CAPTION (se social) o CF-R4-WRITE (se articolo derivato) → CF-R4-QA per ogni derivato → delivery
- Gate: ogni derivato trattato come ordine indipendente (gate COPY + BRAND su ognuno); nessuna abbreviazione per batch
- Valore: moltiplica il ROI di ogni pezzo madre; riduce il costo per contenuto secondario

**Namespace:** `cf/text` · `cf/scripts` · `cf/captions`
**KPI:** lead time brief→draft; GATE-COPY first-pass rate; derivati prodotti per pezzo madre.

---

#### CF-R5 — VISUAL & DESIGN / CAROSELLI [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Caroselli IG, thumbnail, grafiche statiche, template brand. L'asset più maturo di DE
(carousel-factory). In v2: reparto allargato con 10 agenti, 4 workflow CF-grade. Il carousel-factory
viene wrappato — NON riscritto (ADR-003).

**Team agenti (10):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R5-COORD | Coordinatore Visual & Design | sonnet | Orchestra i 4 workflow; riporta a L1-PROD; gestisce capacità Canva MCP vs render locale |
| CF-R5-QA | Verificatore Gate Visual | sonnet | GATE-FORMATO (dimensioni, peso, contrasto, safe-area) + GATE-BRAND (palette, font, logo); blocca e non suggerisce |
| CF-R5-SLIDECOPY | Slide Copywriter | sonnet | Copy slide caroselli (hook/body/CTA da formule carousel-factory); applica icp.dolori per hook |
| CF-R5-PROMPT | Prompt Engineer Visual | sonnet | Prompt immagini ultra-specifici per Gemini/Higgsfield: composizione, stile, palette brand, negative prompt |
| CF-R5-CANVA | Canva Operator | haiku | generate-design, brand-template, perform-editing-operations, export via MCP Canva; conosce ogni operazione Canva MCP |
| CF-R5-RENDER | Render Operator | wasm/haiku | Render Puppeteer (render.mjs): HTML→PNG 1080x1350; resize multi-formato; ottimizzazione file |
| CF-R5-CONCEPT | Concept & Art Director | sonnet | 3 concept visivi per thumbnail (composizione, testo sovrapposto, emozione target); sceglie il migliore con A/B |
| CF-R5-ASSET | Asset Library Manager | haiku | Upload-asset Canva per brand; cartelle Canva organizzate per brand_kit; naming convention |
| CF-R5-RESIZE | Resize & Format Specialist | haiku | Declinazioni multi-formato: 1080x1350 (IG carosello), 1080x1920 (stories/reel), 1280x720 (YT thumb), 1080x1080 (post quadrato) |
| CF-R5-LEARN | Visual Performance Analyst | sonnet | Correla hook visivo/composizione con CTR (da WF-FEEDBACK) → pattern in `cf/patterns` |

**Workflow CF-grade (4):**

**WF-CAROSELLO** [WRAPPA-ESISTENTE (carousel-factory) + TARGET-V2] — asset più maturo DE
- Scopo: carosello IG batch da brief a deliverable completo (PNG + caption)
- Flusso: `brief.json` → CF-R5-SLIDECOPY (hook→body→CTA da formule carousel-factory) → [swarm fan-out N job]:
  - Ramo A: CF-R5-PROMPT → prompt Gemini per slide [oggi: generazione manuale, collo di bottiglia noto]
  - Ramo B: CF-R5-CANVA → create-design-from-brand-template → perform-editing-operations → export 1080x1350
  - Ramo C: HTML slides → CF-R5-RENDER → render.mjs Puppeteer → PNG 1080x1350
  → CF-R5-QA (GATE-FORMATO: 1080x1350, ≤8 slide+cover, peso < 8MB/slide, testo leggibile, no tagli safe-area)
  → CF-R5-QA (GATE-BRAND: palette, font, logo) → CF-R6-GATE (GATE-COPY-APSOC) → caption+hashtag (CF-R5-CANVA caption export o CF-R4-CAPTION) → delivery/publish
  → report batch aggregato (pezzi ok / rework / costo)
- Gate: GATE-FORMATO su ogni carosello (non sul batch); 2 rework falliti → escalation CF-R5-COORD + `cf/failures`
- State: `orders/<id>/03-design/slides-copy.json` → `03-design/design/` → `04-render/PNG/` → state.json per fase
- Dry-run: produce solo copy+prompt (ramo A completo) — a costo zero; già funzionante
- [WRAPPA]: carousel-factory in `Workfolw crea caroselli à/carousel-factory/` wrappato in skill `cf-carousel` senza toccare il runtime; path puliti in `company/03-content-factory/wf-carosello/`

**WF-THUMBNAIL** [WRAPPA-ESISTENTE (concept nel v1) + TARGET-V2]
- Scopo: thumbnail YouTube e copertine; varianti A/B per ogni pezzo
- Flusso: brief (titolo video, canale, emozione target) → CF-R5-CONCEPT (3 concept testuali: composizione, testo, emozione) → generazione: Canva (template brand) | Higgsfield image-4k | canvas-design → CF-R5-RESIZE (varianti A/B × 2 per concept scelto) → GATE-FORMATO (leggibilità a 10%, peso, safe-area) → GATE-BRAND → delivery; committente sceglie variante → scelta in `cf/patterns`
- Gate: 3 concept prodotti prima della generazione (approvazione CF-R5-COORD se richiesta dal brief); GATE-FORMATO sempre: leggibilità testo a thumbnail 10% di larghezza
- Dry-run: solo 3 concept testuali (zero generazione immagini)

**WF-GRAFICA-STATICA** [TARGET-V2]
- Scopo: grafiche one-shot per ads, banner, post singoli non-carosello
- Flusso: brief (dimensioni, uso, canale) → CF-R5-CANVA (brand-template o generate-design) → CF-R5-RESIZE (tutti i formati richiesti dall'ordine) → CF-R5-QA (GATE-FORMATO: dimensioni esatte, peso, margini) → GATE-BRAND → delivery
- Gate: dimensioni esatte del canale target; peso sotto soglia piattaforma; margini brand_kit rispettati

**WF-BRANDKIT-VISUAL** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: produrre e aggiornare i visual del brand_kit (template Canva, palette applicata, logo in tutti i formati)
- Flusso: richiesta da CF-R2 (WF-BRAND-ONBOARDING) → CF-R5-CANVA crea brand kit Canva + template per ogni formato standard → CF-R5-ASSET carica tutti gli asset in cartella Canva del brand → CF-R5-QA valida → notifica CF-R2 di sync avvenuta
- Gate: template per ogni formato standard (1080x1350, 1080x1920, 1280x720, 1080x1080) creato e approvato CF-R2-QA

**Namespace:** `cf/design` · `cf/thumbnails` · `cf/graphics`
**KPI:** caroselli prodotti/ciclo per brand; GATE-FORMATO first-pass rate; costo per carosello per ramo.

---

### AREA POST-PRODUZIONE

#### CF-R6 — QA & GATE [TARGET-V2] — INDIPENDENTE DALLA PRODUZIONE

**Missione.** Garantire che nessun asset esca da CF-DE senza superare i 3 gate (FORMATO, BRAND, COPY).
Indipendente da tutti i reparti di produzione — chi produce non si auto-valuta (regola ferrosa; gap
critico del v1: il gatekeeper era un singolo agente senza reparto autonomo). In v2: 8 agenti, 3 workflow.

**Team agenti (8):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R6-COORD | QA Lead | opus | Assegna revisore a ogni deliverable; riporta a L1-POST (NON a L1-PROD: indipendenza assoluta) |
| CF-R6-FORMAT | Gate Formato Verificatore | haiku | GATE-FORMATO: dimensioni, peso, codec, loudness, struttura — automatizzabile al 100%; script eseguibili |
| CF-R6-BRAND | Gate Brand Verificatore | sonnet | GATE-BRAND: palette vs brand_kit, font, logo, tone voice (campionamento vs esempi brand_kit.voice) |
| CF-R6-COPY | Gate Copy Verificatore (APSOC) | sonnet | GATE-COPY: hook presente (3s video / prima slide / prima riga testo), problema+promessa coerenti con icp, social proof solo reale, CTA unica e misurabile; usa skill cro-copy-architect |
| CF-R6-MANDATO | Mandato Compliance Verificatore | sonnet | Controllo invariant non-parametrici del Mandato Empire: "prove non promesse", zero claim non verificabili, zero genericità; trasversale su ogni formato |
| CF-R6-REWORK | Rework Coordinator | haiku | Gestisce il ciclo di rework: motivo strutturato → rinvia a reparto corretto con specifica; traccia n. rework per pezzo |
| CF-R6-BATCH | Batch QA Coordinator | sonnet | Per batch ≥5 pezzi: coordina QA parallelo, aggrega report, calcola first-pass rate del batch |
| CF-R6-LEARN | QA Pattern Analyst | sonnet | Pattern di gate falliti → `cf/failures` (ReasoningBank); report mensile a CF-Director e 07-FORGE |

**Workflow CF-grade (3):**

**WF-QA-SINGOLO** [TARGET-V2]
- Scopo: review completa di un singolo deliverable (3 gate sequenziali)
- Flusso: deliverable da reparto produzione → CF-R6-FORMAT (GATE-FORMATO: oggettivo, automatizzabile) → se verde: CF-R6-BRAND (GATE-BRAND: parametrico su brand_kit dell'ordine) → se verde: CF-R6-COPY (GATE-COPY-APSOC: hook, promessa, social proof, CTA) → CF-R6-MANDATO (compliance Mandato: no claim inventati) → CF-R6-COORD: verdetto PASS o FAIL con motivo strutturato
- Gate: i 3 gate sono sequenziali; un ROSSO ferma il pezzo e attiva CF-R6-REWORK; 2 rework falliti sullo stesso pezzo → escalation CF-R6-COORD + entry `cf/failures`
- State: `orders/<id>/05-qa/verdict.json` (gate, esito, motivo, n_rework)

**WF-QA-BATCH** [TARGET-V2]
- Scopo: QA parallelo su batch ≥5 pezzi con report aggregato
- Flusso: CF-R6-BATCH distribuisce pezzi → N istanze WF-QA-SINGOLO in parallelo → merge risultati → CF-R6-BATCH produce report aggregato (n. ok / n. rework / first-pass rate / costo rework)
- Gate: ogni pezzo trattato come WF-QA-SINGOLO (nessuna abbreviazione per batch); report al committente con dettaglio per pezzo

**WF-QUALITY-AUDIT** [TARGET-V2]
- Scopo: audit mensile della qualità complessiva dell'ecosistema CF
- Flusso: CF-R6-LEARN campiona tutti i gate falliti del mese → pattern per formato/brand/tipo → CF-R6-COORD produce report → ad CF-Director + a 07-FORGE se gap strutturale ricorrente
- Gate: audit cadenza mensile obbligatorio; ogni pattern richiede ≥3 casi per essere segnalato; nessuna conclusione su n < 3

**Namespace:** `cf/qa` · `cf/failures` (ReasoningBank)
**KPI:** first-pass rate per formato; gate FORMATO/BRAND/COPY pass rate separati; n. rework per ciclo; latenza QA per pezzo.

---

#### CF-R7 — PUBBLICAZIONE & DISTRIBUZIONE [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Portare i deliverable con gate verdi sui canali: IG, TikTok, LinkedIn, YouTube, Drive cliente.
Schedulazione, adattamento per canale, verifica post-pubblicazione. CF Exponium NON aveva questo reparto:
qui DE lo supera. Il v1 aveva 5 agenti e 3 workflow. In v2: 8 agenti, 4 workflow CF-grade.

**Team agenti (8):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R7-COORD | Coordinatore Pubblicazione | sonnet | Orchestra la coda publish; assegna slot da WF-CALENDAR; riporta a L1-POST |
| CF-R7-QA | Verificatore Pre-Publish | sonnet | Check pre-publish: gate verdi in state.json, review umana eseguita, token canale validi |
| CF-R7-ADAPT | Channel Adapter | haiku | Adatta caption/formato per canale: lunghezza, hashtag, aspect ratio, mention, link |
| CF-R7-PUBLISH | Social Publisher | wasm/haiku | Esegue publish IG/TikTok/LinkedIn via orchestratori Python esistenti (main_orchestrator.py, mentalita_orchestrator.py) |
| CF-R7-YT | YouTube Publisher | haiku | Upload video YT: titolo, descrizione, thumbnail selezionata, tag, playlist, programma uscita |
| CF-R7-DELIVER | Delivery Packager | haiku | Pacchetto + manifest per consegna a committenti non-social (Drive, email, transfer); naming standard |
| CF-R7-CHECK | Post-Publish Verifier | haiku | Screenshot/verifica live del post pubblicato; check URL attivo; log `trace.jsonl` con URL definitivo |
| CF-R7-FEEDBACK | Performance Collector | haiku | Raccolta metriche a 48h e 7gg → `cf/patterns` (cosa funziona per quale brand/formato) + handoff a 04-MARKETING Analytics |

**Workflow CF-grade (4):**

**WF-PUBLISH-SOCIAL** [WRAPPA-ESISTENTE (main_orchestrator.py, mentalita_orchestrator.py) + TARGET-V2]
- Scopo: pubblicazione schedulata su IG/TikTok/LinkedIn da coda ordinata
- Flusso: deliverable con gate verdi → CF-R7-QA (pre-publish: gate verdi in state.json + review umana eseguita + token validi) → CF-R7-ADAPT (adattamento per canale) → REVIEW UMANA (gate manuale, obbligatorio fino a rimozione da Board) → CF-R7-PUBLISH (via orchestratori Python) → CF-R7-CHECK (verifica live) → log trace + wiki/log.md entry
- Gate PRE-PUBLISH: nessuna pubblicazione senza gate verdi in state.json; nessuna pubblicazione senza review umana (policy Board invariata); token scaduti → alert CF-R7-COORD + blocco
- State: `orders/<id>/state.json` publish[] per canale con esito e URL definitivo
- Dry-run: genera piano pubblicazione (cosa, dove, quando, con quale caption) senza toccare i canali
- [WRAPPA]: orchestratori Python in `SKILL & Agenti/Workflow pubblicazione automatica/` — wrappati senza modifica runtime; token FB/IG rinnovati in CF-F4

**WF-PUBLISH-YT** [TARGET-V2]
- Scopo: upload e schedulazione video YouTube con tutti i metadati
- Flusso: video con gate verdi + thumbnail selezionata (da WF-THUMBNAIL) → CF-R7-YT (upload, metadati, playlist, orario uscita ottimale per canale) → CF-R7-CHECK (verifica URL video live) → log trace
- Gate: thumbnail selezionata e approvata (scelta committente da varianti A/B); titolo conforme al brand_kit.voice

**WF-DELIVERY-PACKAGER** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: consegna asset a committenti non-social (drive cliente, email, transfer)
- Flusso: deliverable con gate verdi → CF-R7-DELIVER (naming convention, manifest.json con lista asset, checksum) → consegna via canale richiesto dall'ordine → CF-R7-CHECK (conferma ricezione committente) → closure ordine in state.json
- Gate: manifest.json presente e completo; nessuna consegna senza conferma ricezione

**WF-FEEDBACK-LOOP** [TARGET-V2]
- Scopo: chiudere il loop tra pubblicazione e miglioramento del processo produttivo
- Flusso: 48h post-publish: CF-R7-FEEDBACK raccoglie reach/engagement dalla piattaforma → 7gg: raccoglie metriche complete → `memory_store("cf/patterns", {brand, formato, hook, metriche})` → handoff a 04-MARKETING Analytics per analisi ads + organico integrata → CF-R6-LEARN per aggiornamento gate soglie
- Gate: almeno 2 misurazioni (48h + 7gg) per chiudere il loop; nessuna conclusione su n < 5 pezzi dello stesso tipo per brand

**Namespace:** `cf/publish` · `cf/delivery`
**KPI:** % slot calendario rispettati; latenza gate verdi→pubblicazione; post-check green rate; metriche per formato/brand.

---

#### CF-R8 — APPRENDIMENTO & OTTIMIZZAZIONE [TARGET-V2]

**Missione.** Distillare le lezioni dall'intera pipeline CF-DE e tradurle in miglioramenti strutturati.
Assente nel v1 come reparto autonomo (gap critico). In v2: team di 6 agenti, 2 workflow CF-grade.
Riporta a L1-POST ma opera in modo trasversale su tutti i reparti.

**Team agenti (6):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| CF-R8-COORD | Coordinatore Apprendimento | sonnet | Orchestra i 2 workflow; aggiorna la libreria hook/formule; propone ADR su pattern strutturali; riporta a L1-POST |
| CF-R8-QA | Verificatore Pattern | sonnet | Valida pattern proposti: almeno 3 casi, fonte tracciabile, nessuna correlazione inventata |
| CF-R8-HOOK | Hook Pattern Analyst | sonnet | Analizza quali hook/angle performano per brand/formato/nicchia → aggiorna libreria formule CF-R1 |
| CF-R8-ENGINE | Engine Performance Analyst | sonnet | Analizza qualità output per engine (Canva vs Puppeteer vs Higgsfield) → ottimizza routing capability→engine |
| CF-R8-REASONING | ReasoningBank Distiller | sonnet | Distilla pattern da `cf/failures` → lezioni strutturate → propone fix a reparti + richieste a 07-FORGE |
| CF-R8-NEURAL | Neural Pattern Trainer | haiku | Alimenta neural_train con pattern validati da `cf/patterns` quando ci sono dati reali sufficienti |

**Workflow CF-grade (2):**

**WF-PATTERN-DISTILLATION** [TARGET-V2]
- Scopo: da ogni fallimento e ogni successo produttivo estrarre pattern distillati e aggiornare le librerie
- Flusso: ogni post-task: hook CF-R8-HOOK (pattern hook da performance 7gg) + CF-R8-REASONING (distilla failures da `cf/failures`) + CF-R8-ENGINE (qualità engine) → CF-R8-QA (valida pattern: ≥3 casi, fonte tracciabile) → `memory_store("cf/patterns", pattern_validato)` + aggiornamento librerie CF-R1 + notifica a CF-Director
- Gate: nessun pattern senza ≥3 casi; nessuna conclusione inventata (Mandato Art.2 — "prove non promesse")
- Cadenza: settimanale per hook/angle; mensile per engine e failures

**WF-IMPROVEMENT-CYCLE** [TARGET-V2]
- Scopo: ciclo mensile di miglioramento strutturato: pattern → proposta → implementazione → validazione
- Flusso: CF-R8-COORD aggrega top-3 problemi del mese (da WF-QUALITY-AUDIT + WF-PATTERN-DISTILLATION) → CF-R8-REASONING propone fix (se strutturale: richiesta a 07-FORGE; se skill: richiesta a CF-R1/team) → CF-Director approva → implementazione → 4 settimane osservazione → CF-R8-QA valida miglioramento
- Gate: max 3 improvement attivi contemporaneamente; ogni improvement tracciato in ADR se cambia architettura

**Namespace:** `cf/patterns` · `cf/failures` · `cf/improvements`
**KPI:** n. pattern distillati/mese; n. improvement implementati e validati; riduzione failures rate MoM.

---

## 4. Roster agenti consolidato

Convenzione id: `CF-<reparto>-<ruolo>`. Tier: wasm/haiku = meccanico/alto-volume · sonnet = analisi/scrittura · opus = ragionamento critico/gate bloccanti.

| Livello | Ruolo | N. Agenti | Lead/QA |
|---|---|---|---|
| L0 — CF-Director | Director + team | 7 | CF-D-LEAD (opus) / CF-D-QA (sonnet) |
| L1 — Capi Area | Pre / Prod / Post (3 figure distinte) | 3 | segnalate nei rispettivi team |
| L2 — R1 Strategia & Brief | coordinatore + team | 8 | CF-R1-COORD (sonnet) / CF-R1-QA (sonnet) |
| L2 — R2 Brand-Kit Registry | coordinatore + team | 6 | CF-R2-COORD (sonnet) / CF-R2-QA (sonnet) |
| L2 — R3 Produzione Video | coordinatore + team | 10 | CF-R3-COORD (sonnet) / CF-R3-QA (sonnet) |
| L2 — R4 Produzione Testuale | coordinatore + team | 8 | CF-R4-COORD (sonnet) / CF-R4-QA (sonnet) |
| L2 — R5 Visual & Design | coordinatore + team | 10 | CF-R5-COORD (sonnet) / CF-R5-QA (sonnet) |
| L2 — R6 QA & Gate | coordinatore + team | 8 | CF-R6-COORD (opus) / CF-R6-FORMAT (haiku) |
| L2 — R7 Pubblicazione | coordinatore + team | 8 | CF-R7-COORD (sonnet) / CF-R7-QA (sonnet) |
| L2 — R8 Apprendimento | coordinatore + team | 6 | CF-R8-COORD (sonnet) / CF-R8-QA (sonnet) |
| Sentinelle always-on | Cost + Brand (CF-locali) | 2 | CF-SENT-COST (wasm) / CF-SENT-BRAND (haiku) |

**TOTALE: 76 agenti** (incluse sentinelle).

**Tabella per reparto:**

| Reparto | Lead | QA | Specialisti | Tier prevalente |
|---|---|---|---|---|
| CF-Director | CF-D-LEAD (opus) | CF-D-QA (sonnet) | DISPATCH, SCHED, BUDGET, STATUS, LEARN | sonnet/haiku |
| R1 Strategia | CF-R1-COORD | CF-R1-QA | ANALYST, ANGLE, HOOK, TREND, CAL, LEARN | sonnet/haiku |
| R2 Brand-Kit | CF-R2-COORD | CF-R2-QA | CREATOR, CANVA, DRIFT, ICP | sonnet/haiku |
| R3 Video | CF-R3-COORD | CF-R3-QA | SOUL, IMG, MOTION, AVATAR, VO, EDIT, QUEUE, LEARN | haiku (produzione), sonnet (coord/learn) |
| R4 Testuale | CF-R4-COORD | CF-R4-QA | WRITE(sonnet), SEO, REPURP, CAPTION, HEADLINE, LEARN | sonnet/haiku |
| R5 Visual | CF-R5-COORD | CF-R5-QA | SLIDECOPY, PROMPT, CANVA, RENDER, CONCEPT, ASSET, RESIZE, LEARN | sonnet/haiku/wasm |
| R6 QA & Gate | CF-R6-COORD (opus) | CF-R6-FORMAT | BRAND, COPY, MANDATO, REWORK, BATCH, LEARN | opus/sonnet |
| R7 Publish | CF-R7-COORD | CF-R7-QA | ADAPT, PUBLISH, YT, DELIVER, CHECK, FEEDBACK | sonnet/haiku/wasm |
| R8 Apprendimento | CF-R8-COORD | CF-R8-QA | HOOK, ENGINE, REASONING, NEURAL | sonnet/haiku |
| Sentinelle | CF-SENT-COST | CF-SENT-BRAND | — | wasm/haiku (always-on) |

**Topologia swarm (Ruflo):**

| Livello/Reparto | Topologia | Razionale |
|---|---|---|
| CF-DE root | hierarchical (CF-Director → 3 capi area → 8 coord reparto) | gerarchia mega-reparto a livelli |
| R1 Strategia | pipeline (ANALYST→ANGLE→HOOK→QA) | flusso sequenziale brief |
| R2 Brand-Kit | star (COORD → CREATOR, ICP, CANVA, DRIFT) | task indipendenti per tenant |
| R3 Video | pipeline (ugc/avatar) + star (batch fan-out N job paralleli) | pipeline per job singolo; mesh per batch |
| R4 Testuale | pipeline (WRITE→SEO→QA) per articolo; mesh per repurposing | dipendenze sequenziali copy |
| R5 Visual | pipeline (SLIDECOPY→PROMPT→CANVA/RENDER→QA) + fan-out rami | 3 rami paralleli per carosello |
| R6 QA | pipeline sequenziale (FORMAT→BRAND→COPY→MANDATO) | gate non bypassabili, non parallelizzabili |
| R7 Publish | pipeline (QA→ADAPT→REVIEW→PUBLISH→CHECK) | sequenza obbligatoria pre-publish |
| R8 Apprendimento | mesh piccolo (HOOK↔ENGINE↔REASONING↔QA) | analisi incrociata |

---

## 5. Workflow chiave CF-grade (pipeline produzione multi-formato)

Tutti condividono il **project state** unificato (eredità CF Exponium):

```
orders/<order_id>/
├── order.json            # il contratto validato
├── state.json            # fase corrente, gate superati, costi consumati, n_rework
├── trace.jsonl           # ogni evento append-only {ts, agent, event, payload, engine, cost_estimated}
├── 01-brief/             # brief.json per ogni pezzo
├── 02-copy/              # testo, script, caption
├── 03-design/            # prompt, design files, HTML
├── 04-render/            # PNG, video, asset finali
├── 05-qa/                # verdict.json per gate, motivi rework
└── 06-delivery/          # asset verdi, manifest.json, URL pubblicazione
```

**Regole comuni (invariant cardinali):**
- Dry-run default alla prima esecuzione di ogni workflow (stima costi, zero effetti reali)
- Nessuna fase salta il gate precedente (gate sequenziali, non bypassabili)
- `brand_kit` + `icp` obbligatori su ogni ordine (pattern 11 — non negoziabile)
- Ogni fallimento → `trace.jsonl` + `cf/failures` (ReasoningBank distilla entro 24h)
- Review umana obbligatoria pre-pubblicazione social (policy Board — non rimuovibile in V2)
- MAI sforare il budget: `estimate()` di ogni engine prima di eseguire; CF-SENT-COST blocca

### Pipeline end-to-end (ordine → delivery)

```
[ORDINE validato] ──► [R1 BRIEF] ──► [R2 BRAND-KIT check] ──► [ROUTING FORMATO]
                                                                        │
                          ┌─────────────────────────────────────────────┤
                          │                    │                         │
                     [R3 VIDEO]         [R4 TESTUALE]             [R5 VISUAL]
                          │                    │                         │
                          └─────────────────────────────────────────────┤
                                                                         ▼
                                                               [R6 QA & GATE (3 gate)]
                                                                         │
                                              ┌──────────────────────────┤
                                              │                           │
                                        [REWORK]                  [GATE VERDI]
                                              │                           │
                                    torna a reparto                 [R7 PUBLISH / DELIVER]
                                    produzione                           │
                                                                    [R8 FEEDBACK LOOP]
```

### (a) WF-CAROSELLO — carosello IG batch [vedi §3 CF-R5]

Flusso principale:

| Fase | Owner | Input | Output | Gate |
|---|---|---|---|---|
| 01-brief | CF-R1 | order.json, brand_kit, icp | brief.json (angle, hook_type, n. slide, canali) | campi obbligatori completi |
| 02-copy | CF-R5-SLIDECOPY | brief.json, hook/cta-formulas carousel-factory | slides-copy.json | GATE-COPY preliminare (hook+CTA presenti) |
| 03-design | CF-R5-PROMPT/CANVA/RENDER | slides-copy.json, brand_kit | prompt Gemini / design Canva / slides.html | — |
| 04-render | CF-R5-RENDER | design | PNG 1080x1350 per slide | GATE-FORMATO |
| 05-qa | CF-R6 (3 gate) | PNG + copy + caption | verdict.json con gate in state.json | GATE-BRAND + GATE-COPY + MANDATO |
| 06-delivery | CF-R7 | asset verdi | manifest + handoff a WF-PUBLISH-SOCIAL / committente | acceptance criteria handoff |

### (b) WF-VIDEO — UGC / avatar multi-engine [vedi §3 CF-R3]

Flusso principale:

| Fase | Owner | Engine | Gate |
|---|---|---|---|
| 01-brief + script | CF-R1 + CF-R4 (WF-SCRIPT) | — | brief + script con hook 3s |
| 02-stima | CF-R3-QUEUE | estimate() Σ → CF-SENT-COST | BLOCCO se sfora budget |
| 03-asset UGC | CF-R3 SOUL+IMG+MOTION | higgsfield (port CF Exponium) | engine check verde |
| 03-asset avatar | CF-R3-AVATAR | heygen (port CF Exponium) | engine check verde |
| 04-voiceover | CF-R3-VO | tts (edge-tts / ElevenLabs) | no clipping audio |
| 05-montaggio | CF-R3-EDIT | ffmpeg | GATE-FORMATO (durata, aspect, codec, loudness) |
| 06-qa | CF-R6 | — | GATE-BRAND (soul coerente) + GATE-COPY (hook 3s, CTA) |
| 07-delivery | CF-R7 | — | handoff contract |

### (c) WF-ARTICOLO / WF-NEWSLETTER [vedi §3 CF-R4]

```
ordine → brief (keyword/topic, icp) → outline (approvazione committente se richiesta)
  → draft (CF-R4-WRITE) → SEO/AI-SEO pass (CF-R4-SEO)
  → [newsletter: blocco CTA APSOC da 04-MARKETING via HC-MK-CF-01]
  → CF-R6 QA: GATE-COPY (struttura, claim verificabili, zero genericità) → GATE-BRAND (tone vs brand_kit)
  → formato output (md / html / email-ready) → CF-R7: delivery o publish (blog via 06-PLATFORM)
```

### (d) WF-THUMBNAIL / WF-GRAFICA-STATICA [vedi §3 CF-R5]

```
ordine → brief (titolo video/uso, canale) → 3 concept testuali (CF-R5-CONCEPT)
  → generazione: Canva brand-template | Higgsfield image-4k | canvas-design
  → varianti A/B (CF-R5-RESIZE) → CF-R6: GATE-FORMATO (leggibilità 10%, peso, safe-area) → GATE-BRAND
  → committente sceglie variante → scelta in cf/patterns → CF-R7 delivery
```

### (e) WF-PUBLISH-SOCIAL [vedi §3 CF-R7]

```
coda (deliverable con gate verdi) → CF-R7-QA (pre-publish: gate verdi + token validi)
  → CF-R7-ADAPT (caption len, hashtag, aspect per canale)
  → REVIEW UMANA (gate manuale obbligatorio — non bypassabile)
  → CF-R7-PUBLISH: IG/TikTok/LinkedIn via orchestratori Python | Drive via WF-DELIVERY-PACKAGER
  → CF-R7-CHECK (verifica live post/URL) → log trace + wiki/log.md
  → CF-R7-FEEDBACK: metriche a 48h+7gg → cf/patterns + 04-MARKETING Analytics
```

---

## 6. Layer motori (engines) — astrazione multi-engine

Registry invariato dal v1 (modello corretto) + stato aggiornato:

| Engine | Capability servite | Stato | Launcher |
|---|---|---|---|
| **canva** | design, carousel-design, brand-template, export, resize | ATTIVO (MCP `mcp__claude_ai_Canva__*`) | chiamate MCP dirette, wrapper `engines/canva.md` |
| **higgsfield** | image-4k, video-ugc, motion, soul-id, product-shoot | DA COLLEGARE (port da CF Exponium hf-studio/) | `engines/higgsfield.sh` (port parametrizzato) |
| **heygen** | avatar, talking-head, spokesperson | DA COLLEGARE (port da CF Exponium heygen-studio/) | `engines/heygen.sh` (port parametrizzato) |
| **ffmpeg** | montaggio, cut, crop, subtitle-burn, audio-mix, concat | ATTIVO (locale) | `engines/ffmpeg.sh` |
| **tts** | voiceover, audio-caption | PARZIALE (edge-tts gratuito) | `engines/tts.sh` |
| **puppeteer-render** | html-to-png, carousel-render | ATTIVO (`carousel-factory/render.mjs`) | wrapper esistente [WRAPPA-ESISTENTE] |
| **gemini-img** | slide-image (oggi manuale — collo di bottiglia noto) | ATTIVO MANUALE | output = prompt pronti (ramo A carosello) |

**Contratto engine (non negoziabile):** ogni engine espone `generate(job)`, `check()` (collegato sì/no),
`status()`, `estimate(job)` (costo PRIMA di eseguire). Routing: `engine_of(capability) → engine`;
funzione pura — MAI silenziosamente diverso da quello loggato in `trace.jsonl`.

**Regola di estensione:** aggiungere un motore = 1 riga al registry + 1 launcher conforme al contratto.
Vietato toccare workflow, agenti o orchestrazione. Default sicuri e backward-compatible.

---

## 7. Asset esistenti wrappati (ADR-003 — wrap, mai riscrittura)

Regola: `usa-così` (invariato, solo registrato) · `wrappa` (invariato + interfaccia contract/log) · `evolvi` (modifiche DOPO validazione wrapper).

| Path | Reparto v2 | Azione | Marca |
|---|---|---|---|
| `Workfolw crea caroselli à/carousel-factory/` (brands/, context/, hook/cta-formulas, render.mjs) | CF-R5 / WF-CAROSELLO | **wrappa** in skill `cf-carousel`; path puliti in `company/03-content-factory/wf-carosello/`; 4 brand seed diventano registry R2 | [WRAPPA-ESISTENTE] |
| `caroselli/3-sistemi-ai/` (slides.html, render.mjs, PNG) | CF-R5 / WF-CAROSELLO | Archivia come esempio in `context/examples/`; pipeline superata da carousel-factory | [WRAPPA-ESISTENTE → archive] |
| `SKILL & Agenti/Workflow Canva/` | CF-R5 / CF-R2 | Verifica contenuto e fonde nel wrapper engine `canva` | [WRAPPA-ESISTENTE] |
| `SKILL & Agenti/Workflow pubblicazione automatica/` (main_orchestrator.py, mentalita_orchestrator.py, moduli IG/TikTok/LinkedIn/Drive) | CF-R7 / WF-PUBLISH-SOCIAL | **Motore di pubblicazione ufficiale**: wrappa senza toccare runtime; rinnovo token FB/IG in CF-F4; aggiunta dry-run + post-check | [WRAPPA-ESISTENTE] |
| `Page IG - Mentalità Brutale/` (LOGO, POST, storie) | CF-R7 + CF-R2 | Primo tenant interno di test; brand_kit `mentalita-brutale` seed esistente in carousel-factory; asset → `brands/mentalita-brutale/assets/` | [WRAPPA-ESISTENTE] |
| Skill `video`, `image`, `canvas-design`, `theme-factory`, `frontend-design` | CF-R3 / CF-R5 | Knowledge layer condiviso (pattern 6): referenziare, non duplicare | [usa-così] |
| Skill `social`, `content-strategy`, `market-social`, `market-ads`, `ad-creative` | CF-R1 / CF-R7 | Referenziare nei brief e negli adattamenti per canale | [usa-così] |
| Skill `content-forge` | CF-R4 + 07-FORGE | Per repurposing massivo (transcript → derivati) | [usa-così] |
| Skill `cro-copy-architect` (APSOC) | CF-R6-COPY | GATE-COPY eseguibile | [usa-così] |
| Skill `seo-audit`, `ai-seo`, `schema` | CF-R4-SEO | Pass SEO articoli | [usa-così] |
| MCP Canva (`mcp__claude_ai_Canva__*`) | CF-R5 + CF-R2 | Engine `canva` del registry (layer motori) | [usa-così] |
| CF Exponium `hf-studio/`, `heygen-studio/`, `orchestration/engines.sh`, `swarm.sh` | CF-R3 + 09-OPERATIONS | **Port selettivo** parametrizzato: brand_kit al posto di Exponium hard-coded; consultare, mai modificare l'originale | [WRAPPA-ESISTENTE → port] |

**Nuove skill da creare (via 07-FORGE, kernel ≤500 righe, references/ per il dettaglio):**

| Skill | Scopo | Reparto |
|---|---|---|
| `cf-order` | Contratto ordine: validazione, creazione `orders/<id>/`, state machine fasi | CF-Director |
| `cf-brand-kit` | Schema brand_kit/icp, creazione tenant, sync Canva, GATE-BRAND parametrico | CF-R2 / Sentinel |
| `cf-carousel` | Formalizza carousel-factory: formule hook/CTA, 3 rami, render | CF-R5 |
| `cf-engines` | Registry capability→engine, contratto generate/check/status/estimate | CF-R3 + tutti |
| `heygen-generate` | Port parametrizzato skill CF Exponium (avatar multi-brand) | CF-R3 |
| `higgsfield-suite` | Port di higgsfield-generate + soul-id + product-photoshoot multi-brand | CF-R3 |
| `cf-publish` | Pubblicazione multi-canale: wrapper orchestratori Python, dry-run, post-check, token health | CF-R7 |
| `cf-qa-gates` | I 3 gate eseguibili (FORMATO per formato, BRAND parametrico, APSOC) | CF-R6 |
| `cf-brief` | Produzione brief.json: angle + hook_type + struttura + validazione | CF-R1 |
| `cf-repurpose` | Repurposing batch: pezzo madre → N derivati con gate su ognuno | CF-R4 |

---

## 8. KPI + Quality Gates

### KPI (da misurare da zero — nessun target inventato, baseline 4 settimane)

| KPI | Definizione | Reparto owner | Direzione |
|---|---|---|---|
| Throughput | pezzi consegnati / settimana per formato e per brand | CF-Director | ↑ |
| First-pass rate | % deliverable che superano i 3 gate al primo giro | CF-R6 | ↑ (baseline prima, target dopo) |
| Lead time | ore da ordine valido a delivery per formato | CF-Director | ↓ |
| Costo per pezzo | crediti+token / deliverable per formato e per brand | CF-D-BUDGET | ↓ |
| Rework rate | % pezzi rimandati indietro da un gate o dal committente | CF-R6 | ↓ |
| Puntualità publish | % slot calendario rispettati | CF-R7 | ↑ |
| Copertura tenant | n. brand_kit attivi serviti nel mese | CF-R2 | ↑ |
| Brand-drift rate | % output con deviazione brand_kit (campionamento CF-SENT-BRAND) | CF-R2 + Sentinel | ↓ |
| Gate FORMATO pass rate | per formato (carosello/video/testo/grafica) | CF-R6 | ↑ |
| Feedback loop latency | giorni da pubblicazione a pattern distillato in cf/patterns | CF-R8 | ↓ |

### Quality Gates

**GATE-FORMATO** (oggettivo, automatizzabile al 100% — CF-R6-FORMAT):
- Carosello: 1080×1350 px, cover + max 8 slide, peso < 8MB/slide, testo leggibile (contrasto WCAG AA), nessun taglio in safe-area.
- Video: aspect corretto per canale (9:16 / 1:1 / 16:9), durata nei limiti piattaforma, codec h264/h265, loudness -14 LUFS, sottotitoli sincronizzati se richiesti.
- Testo: lunghezza nel range del brief ±10%, heading structure valida (H1 unico, H2-H3 presenti), zero link rotti.
- Grafica: dimensioni esatte canale target, peso sotto soglia piattaforma, margini brand rispettati.

**GATE-BRAND** (parametrico sul brand_kit dell'ordine — CF-R6-BRAND — differenza chiave vs CF Exponium):
- Palette: solo colori hex del brand_kit (tolleranza ±5% luminosità per sfumature).
- Font e logo: corretti e posizionati secondo template brand_kit.visual.
- Tone of voice: campionamento del testo vs `brand_kit.voice.esempi_si` e `esempi_no` (5 campioni min).
- Coerenza soul/avatar: stesso soul_id ricorrente del brand nei video (CF-R3-SOUL garantisce).
- Parole_vietate: zero occorrenze delle `brand_kit.voice.parole_vietate`.

**GATE-COPY-APSOC** (CF-R6-COPY con skill cro-copy-architect — in handoff con Copy Guild MARKETING):
- Hook nei primi 3 secondi / prima slide / prima riga.
- Problema e Promessa espliciti e coerenti con `icp.dolori` e `icp.desideri`.
- Social proof dove il formato lo richiede: **solo prove reali, mai inventate** (Mandato Art.2).
- Obiezione principale gestita (formati lunghi: articoli, VSL, newsletter).
- CTA unica, misurabile, coerente con il canale e `icp.awareness_level`.

**GATE-MANDATO** (CF-R6-MANDATO — non parametrico, sempre attivo, trasversale):
- "Prove non promesse": zero claim su risultati non verificati dal committente.
- Zero contenuti generici: ogni pezzo ha un angle specifico (no "10 consigli per le aziende").
- Zero PII: `aidefence_has_pii` su ogni contenuto in uscita (specie ordini Agency).
- Zero link/riferimenti non verificati.

**Regola dei cancelli:** FORMAT → BRAND → COPY → MANDATO sequenziali; un ROSSO ferma il pezzo,
non il batch; 2 rework sullo stesso pezzo → escalation CF-R6-COORD + `cf/failures`.

---

## 9. Memoria / Namespace

**Namespace AgentDB** (prefisso `cf/`):

| Namespace | Contenuto | Reparto owner |
|---|---|---|
| `cf/orders` | stato ordini attivi/chiusi, registry globale | CF-Director |
| `cf/briefs` | brief.json per ordine, libreria angle/hook per brand | CF-R1 |
| `cf/calendars` | piani editoriali per brand, slot settimana | CF-R1 |
| `cf/brand-kits` | registry tenant, versioni brand_kit, sync Canva | CF-R2 |
| `cf/patterns` | hook/angle/formato che performano per brand (da WF-FEEDBACK) | CF-R8 |
| `cf/failures` | errori distillati da gate falliti → ReasoningBank | CF-R6 + CF-R8 |
| `cf/video` | stato render video, soul-id per brand, render-queue | CF-R3 |
| `cf/souls` | soul-id Higgsfield per brand (coerenza cross-ordine) | CF-R3 |
| `cf/text` | articoli/newsletter/script per ordine | CF-R4 |
| `cf/design` | caroselli, grafiche, thumbnail per ordine | CF-R5 |
| `cf/qa` | verdetti QA per ordine, pattern difetti | CF-R6 |
| `cf/publish` | log pubblicazioni, URL post live, metriche | CF-R7 |
| `cf/improvements` | improvement cycle attivi/chiusi | CF-R8 |
| `cf/kpi` | KPI per reparto per ciclo (alimenta dashboard CF-Director) | CF-Director |

**Hook operativi per ordine (pattern Dynamic Workflow):**

```
pre-order   → memory_search("cf/patterns", brand+formato)   # cosa ha funzionato per questo brand
pre-render  → estimate() Σ engine vs budget → block/allow   # CF-SENT-COST
post-gate   → se ROSSO: memory_store("cf/failures", {pezzo, gate, motivo, n_rework})
post-order  → memory_store("cf/orders", state finale) + wiki/log.md entry
post-publish→ (48h+7gg) memory_store("cf/patterns", {brand, formato, hook, metriche})
```

**Regole operative:**
- `aidefence_has_pii` prima di ogni store di contenuti per clienti Agency.
- Dry-run obbligatorio su ogni workflow prima di ogni run reale.
- Ogni ordine: `state.json` + `trace.jsonl` (test amnesia: ripartibile a freddo dal state).
- Indici a 2 livelli: `cf/INDEX.md` (reparti) + `cf/<reparto>/INDEX.md`.
- Log ReasoningBank: ogni failure distillato entro 24h dall'evento.

**Fallback runtime (rischio daemon Windows, ADR-005):** se Ruflo/AgentDB non disponibile,
i workflow girano in modalità pipeline sequenziale via script bash/python con lo stesso
state.json — il project state è la fonte di verità, Ruflo è il coordinatore, mai il contrario.

---

## 10. Build Plan CF-DE V2-6

Allineato a V2-6 del Piano Maestro (§10). Ciclo a 9 passi (ADR-006) per ogni fase. Passo 5-bis
REVIEW MAXIMILIAN attivo da V2-3. Ordine motivato: asset più maturo (caroselli) e canale attivo
(IG Mentalità Brutale) prima — video costosi per ultimi, dopo che gate e budget guard sono provati.

| Fase | Cosa | Gate di validazione |
|---|---|---|
| **CF-F0** | Scaffolding org: `company/03-content-factory/` con struttura mega-reparto a livelli (CF-Director, 3 capi area, 8 reparti L2), BACKBONE.md, namespace agenti/ con placeholder schede millimetriche | Struttura navigabile Explorer; gerarchia 5 livelli visibile; zero ambiguità sui reparti |
| **CF-F1** | `cf-order` + `cf-brand-kit`: contratto ordine, state machine, brand-kit registry con 4 brand seed da carousel-factory; CF-R1 WF-BRIEF dry-run completo | Ordine fittizio percorre tutte le fasi in dry-run con state.json+trace.jsonl corretti; brand_kit validato per 4 tenant |
| **CF-F2** | WF-CAROSELLO live: wrap carousel-factory in `cf-carousel`, gate CF-R6 eseguibili (`cf-qa-gates`), CF-R5 e CF-R6 attivi, primo batch REALE per Mentalità Brutale | ≥5 caroselli reali con 3 gate verdi; report batch aggregato; path puliti in `company/03-content-factory/` |
| **CF-F3** | Engine layer: `cf-engines` registry + wrapper canva/ffmpeg/puppeteer/tts; CF-R5 WF-THUMBNAIL live via Canva MCP; CF-R2 WF-BRAND-ONBOARDING per tutti i tenant | `engine_of(capability).check()` verde per tutti; 1 thumbnail reale via 2 engine diversi; tutti i brand_kit validati |
| **CF-F4** | WF-PUBLISH-SOCIAL live: wrap orchestratori Python, rinnovo token FB/IG, dry-run + review umana + CF-R7-CHECK; primo publish schedulato reale; CF-R7-FEEDBACK attivo | 1 carosello pubblicato su IG via pipeline completa ordine→publish→log wiki; feedback loop 48h avviato |
| **CF-F5** | CF-R4 live: WF-ARTICOLO + WF-NEWSLETTER + WF-REPURPOSING con handoff APSOC a 04-MARKETING (richiede ecosistema 04 attivo con Copy Guild); CF-R8 WF-PATTERN-DISTILLATION attivo | 1 articolo + 1 newsletter con gate verdi consegnati a committente reale; primo pattern distillato in `cf/patterns` |
| **CF-F6** | CF-R3 live: port higgsfield-suite + heygen-generate parametrizzati; CF-R3-QUEUE + CF-SENT-COST; INTERA pipeline video in dry-run, poi primo video reale SOLO con ok esplicito budget | Dry-run completo verde con costi stimati; 1 video reale dopo approvazione budget esplicita |
| **CF-F7** | Mass-production + loop: swarm mesh batch ≥10 pezzi, CF-SENT-BRAND always-on, CF-R8 WF-IMPROVEMENT-CYCLE mensile, ReasoningBank attivo su tutti i fallimenti | Batch 10 pezzi parallelo entro budget; first-pass rate ≥X% (baseline da misurare); primo improvement cycle completato |
| **CF-F8** | Multi-committente full: Agency + Info-Business + Multi-Business in produzione parallela; dashboard KPI CF-Director visibile | Ordini da 3 committenti diversi serviti in parallelo senza brand-drift; KPI sez. 8 visibili e alimentati |

---

## 11. Rischi specifici + mitigazioni

| Rischio | Probabilità/Impatto | Mitigazione |
|---|---|---|
| Token social scaduti (FB/IG già scaduto, da MEMORY) rompono WF-PUBLISH-SOCIAL silenziosamente | Alta/Alto | CF-R7-QA esegue `token-health` check pre-ogni-run; CF-F4 inizia dal rinnovo; CF-R7-CHECK verifica post live, non solo esito API |
| Brand drift multi-tenant (contenuto di un brand "contamina" un altro) | Media/Alto | GATE-BRAND parametrico per ordine (CF-R6-BRAND); CF-SENT-BRAND campionamento always-on; namespace memoria separati per brand; soul-id distinti per tenant in CF-R3-SOUL |
| Ban/limitazioni automazione social (IG/TikTok/LinkedIn) | Media/Alto | Rate limit conservativi ereditati da v1; review umana obbligatoria; pattern pubblicazione umani (orari variabili); account test prima dei brand reali |
| Motori a crediti (Higgsfield/HeyGen) non collegati o costi imprevisti | Media/Alto | Dry-run default + `estimate()` obbligatorio + CF-SENT-COST exit-2; nessuna spesa senza ok esplicito; video per ultimi nell'ordine fasi |
| Collo di bottiglia WF-BRIEF quando coda ordini è alta | Media/Medio | CF-D-SCHED plan capacità area; batch merging di ordini con stesso brand; CF-R1-TREND accelera brief urgenti |
| Ramo A carosello (Gemini manuale) come collo di bottiglia | Alta/Medio | Rami B (Canva MCP) e C (render HTML) già automatici e prioritari; ramo A solo per qualità top; si sostituisce nel registry appena un engine image è collegato senza toccare il workflow |
| Path legacy fragili (`Workfolw crea caroselli à` con typo/accenti, spazi) | Alta/Medio | CF-F2 copia in `company/03-content-factory/wf-carosello/` con path puliti; originali intoccati fino a validazione sostituto (ADR-003) |
| Copy duplicato tra CF-R4 e 04-MARKETING (chi scrive cosa?) | Media/Medio | Confine scritto: CF = contenuto strutturale, MKT = persuasione/APSOC; pezzi ibridi con handoff HC-MK-CF-01 esplicito; CF-R6-MANDATO verifica che CF non scriva APSOC autonomamente |
| R6 QA bypassato dalla produzione sotto pressione | Alta/Alto | R6 è indipendente: coordinator diverso, namespace diverso, riporta a L1-POST (non L1-PROD); nessun deliverable può andare a R7 senza `state.json.qa.verdict === "PASS"` — controllo automatico in WF-PUBLISH-SOCIAL |
| Sovraccarico ordini (CF è il collo di bottiglia della holding) | Media/Alto | CF-D-SCHED gestisce capacità; CF-Director pubblica capacità dichiarata per formato; Board vede coda via Observability; priorità `deadline → revenue → interno` documentata |
| QA gate troppo rigidi → throughput zero, o troppo laschi → contenuti generici | Media/Medio | Baseline 4 settimane prima di fissare soglie; GATE-FORMATO sempre rigido (oggettivo); GATE-BRAND/COPY con livelli `warn/block` rivedibili da CF-R8 ogni ciclo improvement |
| Assenza di 04-MARKETING attivo blocca WF-NEWSLETTER | Media/Medio | WF-NEWSLETTER segnala handoff pending in state.json; CF-R4-COORD alerta CF-Director; nel frattempo produce il corpo senza blocco CTA (non consegna, ma non si ferma) |
| Swarm che muore sul limite crediti durante build (lezione CP-005) | Alta/Alto | Build a lotti idempotenti (ADR-006); checkpoint STATO-EMPIRE dopo ogni fase; naming Title-Case fisso; mai due swarm grossi insieme sullo stesso account |

---

## Connessioni

- [[11-PIANO-V2-DIRETTIVA-SCALA]] §2 — la direttiva che governa questo dossier (fonte suprema); §0 per la definizione di workflow CF-grade
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — il v1 (riferimento per asset reali, contratto ordine, 5 workflow base, layer motori, rischi noti)
- [[01-ECOSISTEMA-AGENCY-V2]] — esempio di dossier v2 allo stesso livello di dettaglio (stesso lotto V2-2)
- [[12-DOSSIER-MAXIMILIAN]] — review 5-bis attiva da V2-3; "abbastanza ampio? millimetrico? si vede nell'Explorer?"
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] — enforcement Articoli 1-7 su ogni output; GATE-MANDATO (sez. 8)
- [[00-PIANO-MAESTRO]] — gerarchia LX→L5; CF-DE = ecosistema L1 #03; 13 pattern non negoziabili
- `04-ECOSISTEMA-MARKETING.md` — handoff più frequente: Copy Guild APSOC (HC-MK-CF-01 bidirezionale)
- `02-ECOSISTEMA-INFO-BUSINESS.md` — committente lancio (asset VSL, caroselli, email)
- `05-ECOSISTEMA-MULTIBUSINESS.md` — committente YouTube/KDP (video, copertine, creative)
- `07-ECOSISTEMA-FORGE.md` — crea skill/team quando KPI calano 2 cicli (ADR-007); riceve `cf-order`, `cf-brand-kit`, `cf-carousel`, `cf-engines`, `cf-publish`, `cf-qa-gates` da forgiare
- `09-ECOSISTEMA-OPERATIONS.md` — scheduling run, cost guard centrale, storage asset, backup
- `projects/Exponium/Exponium_Content_Factory_Studio` — modello di riferimento (CF Exponium = 1 workflow standard); port selettivo hf-studio + heygen-studio
- `company/Memory/maximilian-corpus/direttiva-20260611-scala-v2.md` — standard di scala; "Content Factory e altri... reparti enormi, come intere aziende dentro l'azienda: un leader, dei capi, una gerarchia solida a livelli"
- ADR-007 (pivot V2, fonte suprema) · ADR-006 (ciclo 9 passi + 5-bis) · ADR-005 (minuzie → BACKLOG) · ADR-003 (wrap, non riscrittura) · ADR-002 (memory-first)
