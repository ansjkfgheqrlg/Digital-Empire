# 🏭 05 — ECOSISTEMA MULTI-BUSINESS V2 (Dossier EMPIRE OS · L1 #05)

> Dossier v2 (V2-2, ADR-007) — amplia il v1 `05-ECOSISTEMA-MULTIBUSINESS.md` a scala CF-grade.
> Fonte: `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md` §2.
>
> **Ecosistema L1 #05 della holding Digital Empire Group.** Tre sotto-ecosistemi paralleli —
> (A) YouTube Automation `MB-YT`, (B) Publishing/KDP `MB-PUB`, (C) E-commerce `MB-ECOM` — più
> un nuovo livello di governo trasversale multi-istanza, `MB-Portfolio`. Multi-Business NON
> produce asset materiali: li **ordina** a Content-Factory/Marketing e li trasforma in revenue
> tramite strategia, ottimizzazione, pubblicazione e gestione di portafoglio.
>
> Versione: 2.0 · Creato: 2026-07-19 · Fase roadmap: V2-2 (dossier architetturale) · Build
> effettiva: V2-6 (reparti v2 ecosistema per ecosistema, ordine 01→04→03→02→**05** — MB è
> l'ultimo ecosistema della sequenza V2-6, si veda §10).
> Supera il v1 `05-ECOSISTEMA-MULTIBUSINESS.md` per profondità e scala. Il v1 resta riferimento
> per dati sui canali, asset mappati e vincoli di onestà. Standard: CF-grade (§0 piano V2).
>
> ⚠️ **Vincolo di onestà (invariato dal v1, non negoziabile):** i canali di riferimento YouTube
> (`@Legamidiamore`, `@dosementale`) NON sono ancora stati analizzati. L'ingestione Empire
> Studio (F-MB1) resta la PRIMA fase di build, prerequisito bloccante per YT-Strategia. Nessun
> dato su quei canali è inventato in questo dossier: dove servirebbe, resta il segnaposto
> `[da ingestione F-MB1]`. **E-commerce resta scheletro dormiente fino a F-MB7** (§10) — anche
> in v2, deliberatamente sotto lo standard di scala altrove applicato (si veda §2.4). **Zero
> spesa API senza ok esplicito di Max** (vincolo globale, invariato).

---

## 0. Missione + DONE WHEN

**MISSIONE:** costruire e gestire N business digitali scalabili in parallelo — canali YouTube
completamente automatizzati, un catalogo libri KDP in crescita continua, store e-commerce —
dove ogni "istanza di business" (canale, libro, store) è un `brand_kit` servito dallo stesso
motore di agenti (pattern 11: multi-tenant by design). In v2, Multi-Business non è più "3
elenchi di reparti": è un **ecosistema a 4 componenti** — 3 sotto-business operativi + un
livello di **governo di portafoglio** (`MB-Portfolio`, nuovo) che decide quando aprire/chiudere
un'istanza, alloca il budget cross-istanza e mantiene il registro dei `brand_kit` attivi. Ogni
reparto L2 dei 3 sotto-business diventa, come richiesto da §2 della direttiva di scala, una vera
organizzazione: team 6-10 agenti (lead + QA + specialisti) e 1-5 workflow CF-grade.

**DONE WHEN (misurabili):**

1. I 12 reparti L2 (§2) hanno org L3/L4 documentata, team a schede tabellari complete
   (lead + QA + specialisti), e almeno un workflow CF-grade eseguibile end-to-end ciascuno.
2. Org L2→L5 dei 3 sotto-ecosistemi + `MB-Portfolio` documentata e navigabile in
   `company/05-multibusiness/`.
3. Ingestione Empire Studio dei 2 canali riferimento completata → 2 dossier in wiki `sources/`
   + 1 synthesis comparativa (F-MB1, invariato).
4. Primo canale YouTube pilota attivo: niche scelta, calendario, ≥1 video pubblicato che ha
   superato TUTTI e 4 i QA gate (script, audio, visual, SEO) + il Policy/Brand gate.
5. Pipeline libro KDP end-to-end eseguita una volta integrando `Workflow-libri` (book-factory):
   manoscritto → PDF 6x9 → cover → listing → pubblicazione (con review umana).
6. Multi-canale dimostrato: ≥2 canali gestiti in parallelo via swarm, ognuno col suo brand_kit
   e namespace memoria, zero cross-contaminazione — verificato da `MB-Portfolio` (isolamento
   memoria) invece che lasciato a convenzione implicita come in v1.
7. `MB-Portfolio` ha eseguito almeno un ciclo di `WF-MB-PORTFOLIO-REVIEW` con decisione
   documentata (apri/tieni/kill istanza) e un `brand_kit registry` popolato e senza duplicati.
8. E-commerce: struttura minima vitale documentata (team ridotti, agenti dormienti) + backlog
   fasi future — NON espansa oltre lo scheletro finché F-MB7 non è aperta.
9. KPI tracciati per ogni istanza e per l'ecosistema (§7) e loggati in wiki + AgentDB; zero
   pubblicazioni automatiche senza gate verdi (invariato dal v1).
10. Skill proprie dell'ecosistema forgiate (§6, almeno le P1) via 07-FORGE con
    PRD+architettura (standard §8 piano V2).

**OUT OF SCOPE (ora):** spesa API (HeyGen/ElevenLabs/ads) senza ok esplicito; pubblicazione
YouTube/KDP senza review umana nelle prime fasi; e-commerce operativo (solo scheletro, vedi
§2.4); espansione dei team ECOM oltre 5 agenti/reparto prima di F-MB7 (rischio "cattedrale
prima del primo video", §11).

---

## 1. Posizione nella holding — confini e handoff

Multi-Business resta un ecosistema **cliente interno** degli ecosistemi trasversali. Possiede
la strategia e il P&L di ogni istanza; **non duplica** capacità che esistono altrove. In v2 il
confine resta identico al v1: cambia la profondità organizzativa interna, non i rapporti con
gli altri ecosistemi.

```
              ┌───────────────────────────────────────────────────────┐
              │   05 MULTI-BUSINESS V2 (questo dossier)                │
              │   MB-Portfolio (governo) · strategia · ottimizzazione  │
              │   · pubblicazione · performance                       │
              └───────┬───────────┬───────────┬───────────┬───────────┘
   ordina asset       │           │           │           │  consegna output
   (video, libri,     ▼           ▼           ▼           ▼  (canali, libri, store)
┌───────────────┐ ┌─────────┐ ┌────────────┐ ┌────────────┐
│03 CONTENT-    │ │04 MARKE-│ │08 INTELLI- │ │09 OPERA-   │
│  FACTORY V2   │ │  TING V2│ │  GENCE     │ │  TIONS     │
│ produzione    │ │ copy    │ │ ricerca,   │ │ swarm,     │
│ materiale     │ │ APSOC,  │ │ Empire     │ │ scheduling,│
│ multi-formato │ │ ads     │ │ Studio     │ │ cost guard │
└───────────────┘ └─────────┘ └────────────┘ └────────────┘
```

**Tabella handoff (contratto Bus: `{from, to, payload, acceptance_criteria}`, invariata dal
v1, con reparto emittente ora esplicito):**

| Da → A | Cosa ordina | Reparto MB emittente | Payload del contratto | Acceptance criteria |
|---|---|---|---|---|
| MB → **Content-Factory** | Produzione video YouTube (script→voiceover→visual→thumbnail), manoscritti libri, creative store | YT-Produzione-Ordini, PUB-Produzione-Ordini, ECOM-Store | `{brand_kit, formato, quantità, deadline, spec_tecniche, riferimenti_stile}` | asset conformi a spec (durata, risoluzione, formato file), brand_kit rispettato, consegna entro deadline |
| MB → **Marketing** | Copy listing KDP, descrizioni SEO, titoli, copy ads e-comm, hook script | YT-Ottimizzazione, PUB-Packaging, ECOM-Crescita | `{brand_kit, icp, formato_copy, framework: APSOC, vincoli_piattaforma}` | copy passa Copy/APSOC Guild gate + brand gate (04-MARKETING-V2 §7.1 G1/G2) |
| MB → **Intelligence** | Ricerca niche, analisi competitor, trend, ingestione Empire Studio dei canali riferimento | YT-Strategia, PUB-Ricerca, ECOM-Ricerca | `{dominio, domande_di_ricerca, output_atteso: dossier_wiki}` | dossier in wiki `sources/` o `synthesis/` con dati verificabili e fonti |
| MB → **Platform** | Tooling (CLI KDP, integrazioni YouTube Data API, store setup) | YT-Pubblicazione, PUB-Pubblicazione | `{spec_funzionale, API_target, vincoli}` | tool passa verify.sh Empire |
| MB → **Operations** | Esecuzione swarm mass-production, scheduling pubblicazioni, budget | MB-Portfolio | `{workflow_id, parallelismo, budget_max, schedule}` | dry-run ok, Cost-Sentinel verde |
| MB → **Forge** | Nuove skill/team (es. yt-seo-optimizer, mb-portfolio-registry) | mb-conductor / MB-Portfolio | `{gap_capacità, spec_skill}` | skill conforme a progressive disclosure (kernel ≤500 righe) |

**Regola di confine (non negoziabile, invariata):** se un task è "creare un asset" →
Content-Factory. Se è "scrivere copy persuasivo" → Marketing. Se è "capire/ricercare" →
Intelligence. Multi-Business tiene SOLO: scelta niche/prodotto, calendario, QA gate finale
d'istanza, ottimizzazione metadati, pubblicazione, monitoraggio revenue, governo di
portafoglio multi-istanza (**nuovo** in v2, prima implicito in mb-conductor).

---

## 2. Reparti L2 v2 — da 11 a 12 reparti (revisione motivata)

Il v1 aveva 11 reparti L2 (4 in MB-YT, 4 in MB-PUB, 3 in MB-ECOM), tutti descritti come righe
tabellari senza gerarchia interna. In v2, applicando §2 della direttiva di scala, ogni reparto
diventa un'organizzazione (team 6-10 con lead + QA + specialisti, 1-5 workflow CF-grade). Le
decisioni di revisione, motivate:

- **+1 reparto trasversale, `MB-Portfolio` (NUOVO).** Il v1 lasciava la gestione multi-istanza
  (quando aprire un secondo canale, come allocare budget tra istanze, come evitare
  cross-contaminazione di memoria, come tenere un registro dei `brand_kit` attivi) come regole
  sparse in §4.5 e affidate implicitamente a `mb-conductor` da solo. Alla scala v2 questo è un
  vero lavoro organizzativo ricorrente (§4.5 del v1 lo descrive già come un intero pattern
  swarm), non una nota a margine: merita un reparto con team e workflow propri.
- **NESSUNA scissione di Analytics/Performance in reparto proprio** (a differenza di
  04-MARKETING-V2, che ha promosso Analytics a L2.4 dedicato). Motivazione della scelta
  opposta: in Marketing l'Analytics serve l'INTERO ecosistema trasversalmente su tutti i
  committenti; in Multi-Business le metriche (retention YouTube, BSR libro) sono strettamente
  accoppiate all'istanza appena pubblicata e al reparto che l'ha pubblicata — separarle
  creerebbe un handoff extra senza reale guadagno di focus. Le funzioni di performance restano
  quindi dentro `YT-Pubblicazione` e `PUB-Pubblicazione`, ma con specialisti dedicati (non più
  1 funzione L4 isolata come in v1). Se il carico di lavoro lo giustificherà (KPI §7), la
  scissione resta un'opzione futura tracciata in BACKLOG (si veda §11, rischio "reparto
  sovraccarico").
- **MB-ECOM resta a 3 reparti, DELIBERATAMENTE sotto lo standard 6-10.** Il v1 identifica
  esplicitamente il rischio "costruire la cattedrale prima del primo video" (v1 §12). Applicare
  lo standard pieno a un sotto-ecosistema dichiarato dormiente fino a F-MB7 contraddirebbe
  quella lezione. In v2 i team ECOM crescono a 5 agenti (lead + QA + 3 specialisti, sotto il
  minimo 6 della direttiva) invece di restare a 2-3 come nel v1: sufficienti per una scheda
  organizzativa completa, non per un'operatività reale prematura. Lo standard pieno (6-10) si
  applica in E1 (§2.4), quando l'e-commerce viene attivato.
- **YT e PUB restano a 4 reparti ciascuno** (Strategia/Ricerca, Produzione-Ordini, Packaging o
  Ottimizzazione, Pubblicazione), gli stessi 4 del v1: la struttura era già corretta, mancava
  solo la profondità. Ogni reparto passa da 2-4 agenti a 6-7.

```
05-MULTI-BUSINESS (L1) — coordinatore: mb-conductor
 ├── MB-PORTFOLIO (trasversale)              ← NUOVO v2: governo multi-istanza, budget, brand_kit registry
 ├── (A) MB-YT — YouTube Automation (priorità ALTA)
 │    ├── YT-Strategia
 │    ├── YT-Produzione-Ordini (interfaccia verso Content-Factory)
 │    ├── YT-Ottimizzazione
 │    └── YT-Pubblicazione (incl. performance/analytics)
 ├── (B) MB-PUB — Publishing/KDP (priorità MEDIA-ALTA, asset già esistenti)
 │    ├── PUB-Ricerca
 │    ├── PUB-Produzione-Ordini (interfaccia verso Content-Factory)
 │    ├── PUB-Packaging
 │    └── PUB-Pubblicazione (incl. monitor)
 └── (C) MB-ECOM — E-commerce (priorità MEDIA, dormiente fino a F-MB7)
      ├── ECOM-Ricerca
      ├── ECOM-Store
      └── ECOM-Crescita
 ⊕   MB-QA-Sentinel-Liaison (trasversale, interfaccia con Quality/Cost/Brand Sentinel del Backbone)
```

---

### 2.1 (A) MB-YT — YouTube Automation

#### 2.1.0 Vincolo fondativo (invariato dal v1)

I canali da REPLICARE E SUPERARE sono `youtube.com/@Legamidiamore` e `youtube.com/@dosementale`
(video interamente AI: voiceover TTS + visual AI + script). **Non sono ancora stati studiati.**
F-MB1 (§10) ordina a Intelligence un'ingestione **Empire Studio** dedicata (frame reali +
visione Claude) che produce per ciascun canale un dossier wiki con: niche e angolo, formato
video, struttura script ricorrente, stile visual, durata media, cadenza reale, packaging
titolo/thumbnail, segnali di monetizzazione. Tutti i parametri marcati `[da ingestione F-MB1]`
in questo capitolo vengono fissati SOLO dopo quel dossier.

#### YT-Strategia

**Missione:** scelta niche, lancio canale, calendario editoriale. **Dove il v1 era carente:**
5 funzioni L4 senza gerarchia né QA — la scorecard niche non aveva un verificatore dedicato
prima di essere approvata da `mb-conductor`.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-yt-strategy-coord` | YT-Strategia Lead | coordinator | sonnet | Coordina il reparto; riceve dossier F-MB1; risponde dei KPI di canale a `mb-conductor` |
| `mb-yt-strategy-qa` | YT-Strategia QA | verifier | sonnet | **NUOVO v2:** verifica la scorecard niche (domanda, competizione, RPM stimato, producibilità AI, rischio policy) prima che passi a `mb-conductor` per l'ok umano |
| `mb-yt-niche-scout` | Niche Scout | worker | sonnet | Scansione niche, volume/competizione, RPM stimato per niche |
| `mb-yt-competitor-mapper` | Competitor Mapper | worker | sonnet | Mappa canali competitor (attivo dopo ingestione F-MB1) |
| `mb-yt-keyword-miner` | Keyword Miner | worker | haiku | Keyword research YouTube (search/suggest/tag) |
| `mb-yt-brandkit-builder` | Brand-Kit Builder | worker | sonnet | Compila brand_kit canale (voce, palette, stile visual, persona) |
| `mb-yt-calendar-planner` | Calendar Planner | worker | haiku | Calendario editoriale per canale, cadenza, stagionalità |

**Workflow L3 CF-grade (4):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-YT-NICHE` | Scelta niche e validazione (input: dossier F-MB1 + criteri RPM/competizione/producibilità AI) | `mb-yt-strategy-qa` verifica la scorecard; ok umano finale |
| `WF-YT-CHANNEL-LAUNCH` | Setup canale + brand_kit (nome, persona, voce TTS, palette, template thumbnail, lingua) | `mb-conductor` (ok umano obbligatorio) |
| `WF-YT-CALENDAR` | Calendario editoriale 30 giorni con titoli provvisori e keyword target | `mb-yt-strategy-coord` approva; registrato in `MB-Portfolio` |
| `WF-YT-COMPETITOR-INGEST` | **NUOVO v2:** ordina/aggiorna l'ingestione Empire Studio dei canali riferimento (prima esecuzione = F-MB1; poi ri-scan periodico) | 2+ dossier in wiki `sources/`; pattern salvati in `mb/yt/patterns` |

#### YT-Produzione-Ordini (interfaccia verso Content-Factory)

**Missione:** ordina il video a Content-Factory e ne valida la consegna — NON produce.
**Dove il v1 era carente:** 3 funzioni L4 (brief-compiler, handoff-validator, asset-receiver)
senza coordinatore né QA dedicato al tracciamento ordini in corso.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-yt-order-lead` | YT-Produzione-Ordini Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; smista slot calendario in ordini CF; tiene la coda ordini |
| `mb-yt-handoff-validator` | Handoff Validator (QA) | verifier | sonnet | Valida la consegna CF contro acceptance criteria del contratto — **blocca** se non conforme |
| `mb-yt-brief-compiler` | Brief Compiler | worker | sonnet | Compila il brief-ordine video per Content-Factory |
| `mb-yt-asset-receiver` | Asset Receiver | worker | haiku | Riceve gli asset consegnati da CF, li archivia, li instrada a YT-Ottimizzazione |
| `mb-yt-spec-translator` | Spec Translator | worker | haiku | **NUOVO v2:** traduce lo slot calendario (niche, keyword target, formato) in spec tecniche del contratto CF (durata, TTS, stile visual) |
| `mb-yt-order-tracker` | Order Tracker | worker | wasm/haiku | **NUOVO v2:** stato ordini in corso (`in coda`/`in produzione`/`consegnato`/`rifiutato`), alimenta `MB-Portfolio` per il cost-attribution |

**Workflow L3 CF-grade (2):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-YT-VIDEO-ORDER` | Ordina il video a CF: `{brand_kit, formato, quantità, spec: durata/TTS/stile_visual, deadline}` → consegna: script+audio+video+thumbnail | `mb-yt-handoff-validator` verifica la consegna vs contratto |
| `WF-YT-ORDER-QA` | **NUOVO v2:** ciclo di rifiuto/rework — se la consegna CF non passa la validazione, ri-apre l'ordine con feedback specifico invece di rilanciare da zero | Consegna corretta entro 2 cicli di rework, altrimenti escalation a `mb-yt-order-lead` |

#### YT-Ottimizzazione

**Missione:** titolo, descrizione, tag, end screen, A/B thumbnail. **Dove il v1 era carente:**
coordinatore + 3 specialisti, nessun QA dedicato al gate SEO (il gate #4 era descritto ma senza
owner strutturale oltre al coordinatore stesso).

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-yt-opt-coord` | YT-Ottimizzazione Lead | coordinator | sonnet | Coordina il reparto e i 4 QA gate video (§7.1) |
| `mb-yt-opt-qa` | YT-Ottimizzazione QA | verifier | sonnet | **NUOVO v2:** possiede il gate #4 SEO come funzione dedicata (separata dal coordinatore); verifica anche il Policy/Brand gate pre-upload |
| `mb-yt-title-smith` | Title Smith | worker | sonnet | Genera/testa varianti titolo (CTR-first, policy-safe) |
| `mb-yt-seo-writer` | SEO Writer | worker | haiku | Descrizione SEO, tag, capitoli/timestamp |
| `mb-yt-thumb-strategist` | Thumbnail Strategist | worker | sonnet | Spec thumbnail + A/B test (produzione a CF) |
| `mb-yt-endscreen-builder` | End Screen Builder | worker | haiku | **NUOVO v2:** end screen + cards, playlist linking, CTA di navigazione interna al canale |

**Workflow L3 CF-grade (2):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-YT-OPT` | Titolo finale, descrizione SEO, tag, end screen, thumbnail scelta | `mb-yt-opt-qa` — gate #4 SEO + Policy/Brand gate |
| `WF-YT-THUMB-AB` | **NUOVO v2 (formalizza T-thumb-ab del v1):** test A/B sistematico di 2+ varianti thumbnail su leggibilità 120px e CTR stimato | Vince la variante con miglior punteggio leggibilità; risultato → `mb/yt/patterns` |

#### YT-Pubblicazione (incl. performance/analytics)

**Missione:** upload via YouTube Data API, scheduling, clip cross-platform, lettura metriche →
feedback a Strategia. **Dove il v1 era carente:** uploader/clipper/retention-analyst come 3
funzioni isolate senza lead né QA condiviso; nessuno "possedeva" il ciclo pubblicazione→dato
come processo unico.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-yt-publish-coord` | YT-Pubblicazione Lead | coordinator | sonnet | Coordina pubblicazione, scheduling, cross-posting e il loop analytics→strategia |
| `mb-yt-publish-qa` | YT-Pubblicazione QA | verifier | sonnet | **NUOVO v2:** verifica pre-upload la checklist Policy/Brand completa (Art. Mandato) prima del lancio effettivo |
| `mb-yt-uploader` | Uploader | worker | wasm/haiku | Upload via YouTube Data API, metadata, end screen |
| `mb-yt-scheduler` | Scheduler | worker | haiku | **NUOVO v2 (promosso da funzione L4):** gestisce la coda di scheduling multi-canale, evita collisioni di cadenza tra istanze |
| `mb-yt-clipper` | Clipper / Cross-Poster | worker | haiku | Ordina clip verticali a CF e li distribuisce (Shorts/TikTok/Reels) |
| `mb-yt-retention-analyst` | Retention Analyst | worker | sonnet | Legge analytics, individua drop-off, propone correzioni script; distilla pattern in `mb/yt/patterns` |

**Workflow L3 CF-grade (3):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-YT-PUBLISH` | Video pubblicato/schedulato + clip cross-platform + entry log wiki | `mb-yt-publish-qa` (review umana in fase iniziale, revocabile dopo 20 pubblicazioni consecutive senza correzioni — §7) |
| `WF-YT-ANALYTICS` | Report retention/CTR a 48h/7gg/28gg + raccomandazioni → memoria + calendario | Dati minimi per verdetto (anti-rumore); mai forzato sotto soglia |
| `WF-YT-CROSSPOST` | **NUOVO v2:** distribuzione clip su Shorts/TikTok/Reels con adattamento formato per piattaforma | `mb-yt-clipper` verifica conformità formato/policy per piattaforma prima della pubblicazione |

---

### 2.2 (B) MB-PUB — Publishing/KDP

#### PUB-Ricerca

**Missione:** niche KDP, validazione domanda, analisi BSR/competizione. **Dove il v1 era
carente:** un solo agente nominato in roster (`mb-pub-niche-scout`), le altre 2 funzioni L4
(keyword-kdp, competition-grader) esistevano solo come righe tabellari senza agente proprio.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-pub-res-lead` | PUB-Ricerca Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; smista le richieste di niche verso Marketing/Intelligence per copy e dati |
| `mb-pub-res-qa` | PUB-Ricerca QA | verifier | sonnet | **NUOVO v2:** verifica la scheda niche (BSR, keyword, gap catalogo, producibilità) prima dell'approvazione |
| `mb-pub-niche-scout` | Niche Scout KDP | worker | sonnet | Niche research KDP (BSR, keyword, gap catalogo) |
| `mb-pub-keyword-kdp` | Keyword Analyst KDP | worker | haiku | **NUOVO v2 (promosso da funzione L4):** keyword research KDP dedicata (separata dal niche scout) |
| `mb-pub-competition-grader` | Competition Grader | worker | sonnet | **NUOVO v2 (promosso da funzione L4):** analisi competizione/BSR dei titoli comparabili |
| `mb-pub-gap-analyst` | Catalog Gap Analyst | worker | haiku | **NUOVO v2:** analizza il catalogo esistente (LIBRO 1-5, §5) per individuare gap di collana/serie |

**Workflow L3 CF-grade (2):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-PUB-NICHE` | Niche KDP, validazione domanda, analisi BSR/competizione, scheda + spec libro (formato, lunghezza, angolo) | `mb-pub-res-qa` verifica prima dell'approvazione `mb-pub-res-lead` |
| `WF-PUB-CATALOG-GAP` | **NUOVO v2:** analisi periodica del catalogo pubblicato per identificare collane/serie mancanti o titoli di follow-up | Report gap con priorità; input diretto a `WF-PUB-NICHE` |

#### PUB-Produzione-Ordini (interfaccia verso Content-Factory)

**Missione:** ordina manoscritto+immagini a Content-Factory; esegue book-factory
(impaginazione 6x9 — asset esistente `Workflow-libri/`). **Dove il v1 era carente:**
`mb-pub-layout-operator` e `mb-pub-book-qa` erano gli unici agenti nominati; manuscript-brief
e image-prompts restavano funzioni L4 senza titolare.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-pub-order-lead` | PUB-Produzione-Ordini Lead | coordinator | sonnet | **NUOVO v2:** coordina l'ordine del manoscritto a CF e l'ingresso in book-factory |
| `mb-pub-order-handoff-validator` | Order Handoff Validator | verifier | sonnet | **NUOVO v2:** valida che il manoscritto+immagini consegnato da CF rispetti il brief prima di passarlo a layout |
| `mb-pub-manuscript-brief` | Manuscript Brief Writer | worker | sonnet | **NUOVO v2 (promosso da funzione L4):** compila il brief manoscritto per CF (capitoli, parole, stile, angolo) |
| `mb-pub-image-prompts` | Image Prompt Writer | worker | haiku | **NUOVO v2 (promosso da funzione L4):** compila `image_prompts.yaml` per le immagini interne del libro |
| `mb-pub-layout-operator` | Layout Operator | worker | wasm/haiku | Esegue book-factory (`Workflow-libri/scripts/orchestrator.py`) |
| `mb-pub-book-qa` | Book QA (QA) | verifier | sonnet | QA PDF (formato 6x9, immagini, typo) — estende `qa_checker.py`; possiede il Layout Gate |

**Workflow L3 CF-grade (2):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-PUB-BOOK-ORDER` | Ordina manoscritto+immagini a Content-Factory: `{brand_kit, formato: manoscritto_md + image_prompts.yaml, quantità: 1, spec}` | `mb-pub-order-handoff-validator` verifica la consegna vs brief |
| `WF-PUB-LAYOUT` | Impaginazione 6x9 tramite book-factory ESISTENTE (`Workflow-libri/`): orchestrator.py → generate_images → build_book → qa_checker | `mb-pub-book-qa` — Layout Gate (§7.1) |

#### PUB-Packaging

**Missione:** cover front+spine+back; titolo, sottotitolo, descrizione A+, 7 keyword,
categorie (copy ordinato a Marketing). **Dove il v1 era carente:** un solo agente
(`mb-pub-listing-builder`) copriva 3 funzioni L4 distinte senza coordinatore né QA.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-pub-pkg-lead` | PUB-Packaging Lead | coordinator | sonnet | **NUOVO v2:** coordina cover + listing; smista il copy a Marketing (APSOC) |
| `mb-pub-pkg-qa` | PUB-Packaging QA | verifier | sonnet | **NUOVO v2:** possiede il Cover Gate + Listing Gate (§7.1) |
| `mb-pub-cover-spec` | Cover Spec Writer | worker | haiku | **NUOVO v2 (promosso da funzione L4):** spec cover (trim+spine calcolati da n. pagine reale) → ordine a CF |
| `mb-pub-listing-builder` | Listing Builder | worker | haiku | Assembla listing (copy da Marketing) + categorie + 7 keyword |
| `mb-pub-category-picker` | Category Picker | worker | haiku | **NUOVO v2 (promosso da funzione L4):** sceglie le 3 categorie KDP coerenti con la niche |
| `mb-pub-keyword7-optimizer` | 7-Keyword Optimizer | worker | haiku | **NUOVO v2:** ottimizza le 7 keyword KDP (no keyword stuffing, copertura niche) |

**Workflow L3 CF-grade (2):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-PUB-COVER` | Cover print-ready + versione ebook, dimensioni trim+bleed corrette per il n. pagine reale | `mb-pub-pkg-qa` — Cover Gate |
| `WF-PUB-LISTING` | Titolo, sottotitolo, descrizione A+ (APSOC via Marketing), 7 keyword, categorie, pricing | `mb-pub-pkg-qa` — Listing Gate |

#### PUB-Pubblicazione (incl. monitor)

**Missione:** upload KDP, pricing, review pre-pubblicazione; BSR, recensioni, royalty →
feedback a Ricerca. **Dove il v1 era carente:** `mb-pub-publisher` e `mb-pub-royalty-tracker`
esistevano; pricing e compliance restavano senza titolare esplicito.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-pub-pub-lead` | PUB-Pubblicazione Lead | coordinator | sonnet | **NUOVO v2:** coordina upload, pricing, review pre-pubblicazione e il loop monitor→ricerca |
| `mb-pub-compliance-checker` | Compliance Checker (QA) | verifier | sonnet | **NUOVO v2:** possiede il Compliance Gate (checklist contenuti KDP + disclosure AI) prima dell'upload |
| `mb-pub-kdp-uploader` | KDP Uploader | worker | haiku | Upload KDP + checklist pre-pubblicazione |
| `mb-pub-pricing` | Pricing Specialist | worker | haiku | **NUOVO v2 (promosso da funzione L4):** determina pricing in base a formato/lunghezza/niche |
| `mb-pub-royalty-tracker` | Royalty Tracker | worker | wasm/haiku | Monitora BSR/royalty/recensioni, feedback loop verso PUB-Ricerca |
| `mb-pub-review-watcher` | Review Watcher | worker | haiku | **NUOVO v2 (promosso da funzione L4):** monitora recensioni per segnali qualitativi (non solo BSR) |

**Workflow L3 CF-grade (2):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-PUB-PUBLISH` | Upload KDP, pricing, review umana obbligatoria, checklist conformità (incl. disclosure AI) | `mb-pub-compliance-checker` — Compliance Gate + review umana |
| `WF-PUB-MONITOR` | BSR, recensioni, royalty → feedback a PUB-Ricerca | Dati minimi per decisione; un libro sotto soglia 90gg → decisione kill/relaunch |

---

### 2.3 (C) MB-ECOM — E-commerce (dormiente, DELIBERATAMENTE sotto lo standard 6-10)

**Ora (scheletro, zero spesa):** org L2-L4 documentata, agenti definiti ma **dormienti**
(nessuno spawna finché E1 non è approvata), namespace memoria riservato (`mb/ecom/*`), un solo
workflow attivabile ora: `WF-ECOM-PRODUCT` (ricerca prodotto pura, eseguita da Intelligence su
ordine MB, output = dossier wiki). Team a 5 agenti (non 6-10): lead + QA + 3 specialisti,
esplicitamente sotto lo standard di scala per rispettare il vincolo "no cattedrale prima del
primo video" (v1 §12, confermato in §11 di questo dossier).

#### ECOM-Ricerca

| ID | Agente | Tipo | Tier | Ruolo operativo | Stato |
|---|---|---|---|---|---|
| `mb-ecom-res-lead` | ECOM-Ricerca Lead | coordinator | sonnet | Coordina ricerca prodotto e validazione margine | dormiente |
| `mb-ecom-res-qa` | ECOM-Ricerca QA | verifier | sonnet | Verifica margine/domanda/logistica prima della scheda prodotto | dormiente |
| `mb-ecom-product-scout` | Product Scout | worker | sonnet | Ricerca prodotto + margini | dormiente |
| `mb-ecom-margin-calculator` | Margin Calculator | worker | haiku | Calcolo margine netto per prodotto candidato | dormiente |
| `mb-ecom-demand-analyst` | Demand Analyst | worker | haiku | Validazione domanda (trend, stagionalità) | dormiente |

**Workflow (1, unico attivabile ora):** `WF-ECOM-PRODUCT` — ricerca prodotto, validazione
margine → dossier wiki. Gate: dossier verificabile con fonti; nessuna decisione di acquisto.

#### ECOM-Store

| ID | Agente | Tipo | Tier | Ruolo operativo | Stato |
|---|---|---|---|---|---|
| `mb-ecom-store-lead` | ECOM-Store Lead | coordinator | sonnet | Coordina setup store e listing | dormiente (attiva a E2) |
| `mb-ecom-store-qa` | ECOM-Store QA | verifier | sonnet | Verifica conformità listing/store al brand_kit | dormiente |
| `mb-ecom-store-setup` | Store Setup | worker | haiku | Setup store, configurazione tecnica (con 06-Platform) | dormiente |
| `mb-ecom-listing-ecom` | Listing Builder E-commerce | worker | haiku | Listing prodotto (copy a Marketing, visual a CF) | dormiente |
| `mb-ecom-pod-liaison` | POD/Publishing Liaison | worker | sonnet | **Sinergia dichiarata in v1 §6:** interfaccia con PUB per print-on-demand derivato dai libri (stessi brand_kit, stesse cover) | dormiente |

**Workflow (attivabile a E2):** `WF-ECOM-STORE` — setup store, listing (copy a Marketing,
visual a Content-Factory). Gate: E1 chiusa, budget approvato.

#### ECOM-Crescita

| ID | Agente | Tipo | Tier | Ruolo operativo | Stato |
|---|---|---|---|---|---|
| `mb-ecom-growth-lead` | ECOM-Crescita Lead | coordinator | sonnet | Coordina ads e fulfillment | dormiente (attiva a E3/E4) |
| `mb-ecom-growth-qa` | ECOM-Crescita QA | verifier | sonnet | Verifica unit economics prima dello scaling | dormiente |
| `mb-ecom-ads-liaison` | Ads Liaison | worker | sonnet | Strategia campagne (con Marketing/Advertising) | dormiente |
| `mb-ecom-fulfillment-monitor` | Fulfillment Monitor | worker | wasm/haiku | Monitor ordini/fulfillment/anomalie | dormiente |
| `mb-ecom-unit-economics-analyst` | Unit Economics Analyst | worker | sonnet | Analisi margine netto post-ads/fulfillment, decisione scaling | dormiente |

**Workflow (attivabili a E3/E4):** `WF-ECOM-ADS` (campagne, strategia con Marketing) ·
`WF-ECOM-FULFILL` (monitor ordini/fulfillment). Gate: E2 live con tracking attivo (ADS); E3 con
unit economics positivi (FULFILL/scaling).

**Fasi future (invariate dal v1, ordine vincolato):**

| Fase | Cosa | Gate di ingresso |
|---|---|---|
| E1 | Scelta modello (dropshipping / POD / digitale — il POD si aggancia naturalmente a MB-PUB) | dossier WF-ECOM-PRODUCT + decisione `mb-conductor` + ok umano |
| E2 | Store MVP: 1 store, ≤10 listing | E1 chiusa, budget approvato |
| E3 | Ads test (strategia con Marketing) | E2 live, tracking attivo |
| E4 | Fulfillment monitor + scaling | E3 con unit economics positivi |

**Sinergia prioritaria (invariata):** la prima incarnazione e-commerce sarà probabilmente
**POD/merch derivato dal Publishing** — decisione formale in E1, non ora.

---

### 2.4 MB-Portfolio (trasversale, NUOVO reparto v2)

**Missione:** governo di portafoglio multi-istanza. In v1 le regole di §4.5 ("un canale nuovo
si apre SOLO quando il precedente ha gate stabili"; "memoria isolata per canale") esistevano
ma senza un titolare organizzativo — erano istruzioni per `mb-conductor` da applicare da solo.
In v2 diventano il lavoro di un reparto dedicato: decide apertura/chiusura istanze, alloca
budget cross-istanza, mantiene il registro `brand_kit` (anti-duplicazione niche/angolo tra
canali — v1 §4.5 regola (a)), verifica l'isolamento di memoria tra istanze.

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-port-lead` | MB-Portfolio Lead | coordinator | opus | Decide apertura/chiusura istanze; riporta a `mb-conductor`; arbitra conflitti di budget tra istanze |
| `mb-port-qa` | Portfolio Isolation QA | verifier | sonnet | Verifica che ogni istanza legga SOLO il proprio namespace + i pattern condivisi (`mb/yt/patterns`, `mb/pub/patterns`) — **blocca** su cross-contaminazione |
| `mb-port-budget-allocator` | Budget Allocator | worker | sonnet | Alloca budget per istanza sotto Cost-Sentinel; cost-attribution per canale/libro/store |
| `mb-port-brandkit-registry` | Brand-Kit Registry Keeper | worker | haiku | Mantiene il registro di tutti i `brand_kit` attivi (canali, libri, store); verifica niche/angolo NON duplicati (regola v1 §4.5a) |
| `mb-port-launch-gate` | Instance Launch Gate | verifier | sonnet | Verifica i criteri di apertura nuova istanza (F-MB5: ≥10 video con ≥80% gate verdi al primo colpo) prima di autorizzare uno swarm nuovo |
| `mb-port-report-analyst` | Portfolio Report Analyst | worker | sonnet | Report mensile revenue/costo per istanza → `mb-conductor` → C-Suite |

**Workflow L3 CF-grade (3):**

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| `WF-MB-PORTFOLIO-REVIEW` | Revisione mensile di tutte le istanze attive (canali/libri/store): KPI, costo, decisione tieni/kill/rilancia | `mb-port-lead` decide con dati da `WF-YT-ANALYTICS`/`WF-PUB-MONITOR`; mai a opinione |
| `WF-MB-INSTANCE-LAUNCH-GATE` | Verifica i criteri F-MB5 prima di autorizzare l'apertura di una nuova istanza via swarm | `mb-port-launch-gate` verifica soglia ≥80% gate verdi; `mb-port-brandkit-registry` verifica niche/angolo distinto |
| `WF-MB-BRANDKIT-REGISTRY` | Mantiene aggiornato il registro `brand_kit` cross-istanza; rileva duplicati/collisioni di niche | `mb-port-brandkit-registry`; zero brand_kit duplicati nel registro |

---

### MB-QA-Sentinel-Liaison (trasversale, invariato dal v1)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-qa-sentinel-liaison` | Sentinel Liaison | worker | sonnet | Interfaccia con Quality/Brand/Cost Sentinel del Backbone; smista escalation da gate rossi ricorrenti |

### mb-conductor (L1, invariato dal v1)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `mb-conductor` | MB-Conductor | coordinator | opus | Dirige l'ecosistema, alloca budget tra A/B/C (via `MB-Portfolio`), risponde alla C-Suite |

---

## 3. Roster agenti completo

### Riepilogo per reparto

| Reparto | Agenti (v1 → v2) | Lead | QA | Specialisti |
|---|---|---|---|---|
| mb-conductor (L1) | 1 → 1 | — | — | — |
| MB-Portfolio (NUOVO) | 0 → 6 | `mb-port-lead` | `mb-port-qa` | 4 |
| YT-Strategia | 5 → 7 | `mb-yt-strategy-coord` | `mb-yt-strategy-qa` | 5 |
| YT-Produzione-Ordini | 3 → 6 | `mb-yt-order-lead` | `mb-yt-handoff-validator` | 4 |
| YT-Ottimizzazione | 4 → 6 | `mb-yt-opt-coord` | `mb-yt-opt-qa` | 4 |
| YT-Pubblicazione | 4 → 6 | `mb-yt-publish-coord` | `mb-yt-publish-qa` | 4 |
| PUB-Ricerca | 1 → 6 | `mb-pub-res-lead` | `mb-pub-res-qa` | 4 |
| PUB-Produzione-Ordini | 2 → 6 | `mb-pub-order-lead` | `mb-pub-order-handoff-validator` | 4 |
| PUB-Packaging | 1 → 6 | `mb-pub-pkg-lead` | `mb-pub-pkg-qa` | 4 |
| PUB-Pubblicazione | 2 → 6 | `mb-pub-pub-lead` | `mb-pub-compliance-checker` | 4 |
| ECOM-Ricerca | 1 → 5 | `mb-ecom-res-lead` | `mb-ecom-res-qa` | 3 |
| ECOM-Store | 0 → 5 | `mb-ecom-store-lead` | `mb-ecom-store-qa` | 3 |
| ECOM-Crescita | 2 → 5 | `mb-ecom-growth-lead` | `mb-ecom-growth-qa` | 3 |
| MB-QA-Sentinel-Liaison | 1 → 1 | — | — | — |
| **TOTALE** | **~28 → 72** | 11 | 11 | 46 + 4 singoli |

*(Il v1 aveva ~28 agenti registrati (di cui diversi solo come funzione L4, non come agente
nominato). In v2 il roster sale a 72: applicare lo standard §2 piano V2 — minimo 6 agenti per
reparto operativo, lead + QA sempre presenti — a 12 reparti produce naturalmente un numero
sopra la stima 45-65 indicata nell'incarico. Si è scelto di rispettare lo standard invece di
comprimerlo artificialmente sotto il minimo, specialmente perché MB copre 3 sotto-business
paralleli (non 1 come Marketing) più il nuovo layer di portafoglio. Il conteggio resta
comunque disciplinato: MB-ECOM è tenuto a 5/reparto — sotto lo standard — proprio per non
gonfiare il roster su un'area dormiente (§2.4).)*

**Spawn on-demand via Ruflo `agent_spawn` (§8):** i coordinator/QA esistono solo quando il
loro workflow è attivo; i worker WASM/Haiku sono pool riusabili tra canali/libri. Gli agenti
ECOM restano a stato `dormiente` in AgentDB fino a F-MB7/E1: definiti, non spawnati.

---

## 4. Workflow chiave CF-grade

### (a) Pipeline YouTube end-to-end (per canale, dalla niche al video pubblicato)

```
FASE 1 · STRATEGIA (YT-Strategia)      FASE 2 · PRODUZIONE (handoff CF via YT-Produzione-Ordini)
┌─────────────────────────┐            ┌─────────────────────────────────┐
│ WF-YT-COMPETITOR-INGEST  │            │ WF-YT-VIDEO-ORDER                │
│ WF-YT-NICHE              │───brief───▶│  → script (gate #1) → voiceover  │
│ WF-YT-CHANNEL-LAUNCH     │  ordine    │    TTS (gate #2) → visual/       │
│ WF-YT-CALENDAR           │            │    B-roll/avatar (gate #3) →     │
└─────────────────────────┘            │    thumbnail                     │
                                        └───────────────┬───────────────────┘
FASE 4 · PUBBLICAZIONE (YT-Pubblicazione)                │ consegna validata (WF-YT-ORDER-QA)
┌─────────────────────────┐            FASE 3 · OTTIMIZZAZIONE (YT-Ottimizzazione)
│ WF-YT-PUBLISH            │◀───────────┌─────────────────────────────────┐
│ WF-YT-CROSSPOST          │            │ WF-YT-OPT: titolo+descrizione    │
│ WF-YT-ANALYTICS ─────────┼──feedback─▶│    SEO, tag, end screen          │
└──────────┬────────────────┘           │ WF-YT-THUMB-AB                   │
           │                            └─────────────────────────────────┘
           └──────────────────────────► MB-Portfolio: WF-MB-PORTFOLIO-REVIEW
```

I passi di produzione (script, voiceover, visual, thumbnail) sono **eseguiti da
Content-Factory** (03-ECOSISTEMA-CONTENT-FACTORY-V2) su ordine `WF-YT-VIDEO-ORDER`;
Multi-Business valida la consegna e possiede tutti i gate.

### (b) Pipeline Publishing/KDP end-to-end (integra asset esistenti)

```
1. RICERCA (PUB-Ricerca)                 WF-PUB-NICHE + WF-PUB-CATALOG-GAP
        │                                  → scheda niche + spec libro
2. ORDINE MANOSCRITTO (PUB-Produzione-Ordini)
        │                                  WF-PUB-BOOK-ORDER → Content-Factory
3. IMPAGINAZIONE (PUB-Produzione-Ordini)
        │                                  WF-PUB-LAYOUT: book-factory ESISTENTE
        │                                  (Workflow-libri/) → book_final.pdf 6x9  [LAYOUT GATE]
4. PACKAGING (PUB-Packaging)
        │                                  WF-PUB-COVER [COVER GATE] + WF-PUB-LISTING [LISTING GATE]
5. PUBBLICAZIONE (PUB-Pubblicazione)
        │                                  WF-PUB-PUBLISH: upload KDP, review umana  [COMPLIANCE GATE]
6. MONITOR (PUB-Pubblicazione)            WF-PUB-MONITOR → feedback a (1) + MB-Portfolio
```

### (c) Governo multi-istanza — N canali/libri in parallelo via swarm (esteso a MB-Portfolio)

**Ogni istanza (canale, libro, store) = un `brand_kit`** (pattern 11). In v2 il layer
`MB-Portfolio` governa esplicitamente ciò che nel v1 era implicito:

```
mb-conductor
   └── MB-Portfolio: WF-MB-INSTANCE-LAUNCH-GATE (verifica criteri F-MB5 prima di autorizzare)
        │
        └── swarm_init(topology: hierarchical)
             ├── canale-1 (brand_kit_1) → squadra YT completa, namespace mb/yt/canale-1
             ├── canale-2 (brand_kit_2) → squadra clonata, namespace mb/yt/canale-2
             │      (autorizzato SOLO da WF-MB-INSTANCE-LAUNCH-GATE)
             ├── libro-1 (brand_kit_L1) → squadra PUB completa, namespace mb/pub/libro-1
             └── ... N istanze, pool worker Haiku/WASM condiviso
        │
        └── WF-MB-PORTFOLIO-REVIEW (mensile) → tieni / kill / rilancia per istanza
        └── mb-port-qa: verifica isolamento memoria (zero cross-contaminazione)
```

Regole multi-istanza (invariate dal v1, ora enforcement esplicito di `MB-Portfolio`):
(a) niche diverse o angoli diversi — mai due istanze identiche, verificato da
`mb-port-brandkit-registry`; (b) memoria isolata per istanza + memoria condivisa
`mb/yt/patterns` / `mb/pub/patterns`, verificato da `mb-port-qa`; (c) Cost-Sentinel con budget
per-istanza, allocato da `mb-port-budget-allocator`; (d) una nuova istanza si apre SOLO quando
la precedente ha gate stabili, verificato da `mb-port-launch-gate` (criterio F-MB5).

### (d) Loop performance → pattern (analogo al loop ottimizzazione di 04-MARKETING-V2 §4b)

```
1. RACCOLTA     YT: mb-yt-retention-analyst legge analytics 48h/7gg/28gg
                PUB: mb-pub-royalty-tracker + mb-pub-review-watcher leggono BSR/recensioni
2. DIAGNOSI     Drop-off per sezione script (YT) / sezione listing debole (PUB)
3. DISTILLA     Pattern vincente → mb/yt/patterns o mb/pub/patterns
                Anti-pattern (fallimento) → stesso namespace, marcato come tale
4. REVISIONE    YT-Strategia/YT-Ottimizzazione o PUB-Ricerca/PUB-Packaging riaprono
                SOLO la sezione diagnosticata (mai riscrittura totale — regola anti-deriva,
                identica a 04-MARKETING-V2 §4b)
5. CONSOLIDA    Winner → pattern library; wiki/log.md aggiornato; MB-Portfolio ne tiene conto
                nella prossima WF-MB-PORTFOLIO-REVIEW
   └────────────────────────────────────────────────► torna a 1 (loop continuo)
```

---

## 5. Asset esistenti wrappati (ADR-003: wrapper, MAI riscrittura)

Mappatura invariata dal v1 nei path e nell'azione (zero orfani, F3 Piano Maestro); aggiornata
solo nel reparto destinazione per riflettere la nuova organizzazione §2.

| Path | Reparto destinazione v2 | Azione |
|---|---|---|
| `Workflow-libri/` (CLAUDE.md, scripts/, agents/, templates/) | PUB-Produzione-Ordini / `WF-PUB-LAYOUT` | Wrappare come motore L3 (owner: `mb-pub-layout-operator`); non riscrivere |
| `Workflow-libri/📚 Piano Completo Sistema Multi-Age.md` | PUB-Produzione-Ordini (documentazione) | Ingerire in wiki `tools/` |
| `KDP - prodottti digitali/LIBRO 1..5` | PUB-Pubblicazione / `WF-PUB-MONITOR` | Censire catalogo: stato, listing, BSR (owner: `mb-pub-royalty-tracker`); input a `WF-PUB-CATALOG-GAP` |
| `KDP - prodottti digitali/GPT - KDP Carousel Factory` | PUB-Packaging → ordini a Content-Factory | Valutare riuso per promo social |
| `KDP - prodottti digitali/Leanding Page` | 06-Platform per conto di PUB-Pubblicazione | Audit + eventuale empire-style |
| `Lanco ebook/` | PUB-Packaging + Info-Business (confine: ebook venduto fuori KDP = Info-Business) | Ingestione wiki + decisione confine |
| `Strategia Ebook _ Kpd - pr. TikTock (2).pdf` | Intelligence → dossier per PUB-Ricerca | Ingestione Empire Studio/wiki |
| `caroselli/`, `Workfolw crea caroselli à/` | Content-Factory (produzione) — MB è solo committente | Migrare a CF, MB li ordina via contratto |
| Skill `printing-press*` (9 skill) | Platform/Forge — al servizio di PUB-Produzione-Ordini | Registrare nel registro skill (07-BACKBONE); modello scorecard per i gate MB |
| Skill `book-to-skill` | PUB-Pubblicazione → Info-Business (ponte) | Registrare + definire trigger post-pubblicazione |
| Skill `video` | Content-Factory (riferimento produzione) | Registrare; MB la invoca solo via ordine (YT-Produzione-Ordini) |
| Wiki `Map - Kdp_-_Prodottti_Digitali.md`, `Map - Workflow-Libri.md`, `Map - Lanco_Ebook.md` | BRAIN (wiki) | Aggiornare con la nuova org MB v2 |

---

## 6. Skill NUOVE da forgiare (via 07-FORGE, standard §8 piano V2: PRD → architettura → build)

**Esistenti riusate da MB (nessuna modifica richiesta, invariate dal v1):** `printing-press` +
suite · `book-to-skill` · `content-forge` · `cro-copy-architect` / `market-copy` ·
`seo-audit` / `ai-seo` / `schema` · `analytics` · `memory-empire` / `wiki-context` ·
`swarm-orchestration` / `sparc-methodology`.

**NUOVE da creare (kernel ≤500 righe, references/ separate):**

| Skill nuova | Reparto | Cosa fa | Priorità |
|---|---|---|---|
| `yt-niche-research` | YT-Strategia | Scorecard niche: domanda, competizione, RPM stimato, producibilità AI, rischio policy | P1 (post F-MB1) |
| `yt-script-engine` | YT-Produzione-Ordini | Brief script retention-first per CF: hook, loop, struttura `[pattern da ingestione F-MB1]` | P1 |
| `yt-seo-optimizer` | YT-Ottimizzazione | Titolo/descrizione/tag/capitoli policy-safe; checklist SEO Gate #4 | P1 |
| `thumbnail-factory` | YT-Ottimizzazione | Spec + A/B test thumbnail (generazione a CF); test leggibilità 120px | P1 |
| `yt-channel-brandkit` | YT-Strategia | Genera il brand_kit canale completo (persona, voce TTS, stile visual, naming) | P1 |
| `mb-portfolio-registry` | MB-Portfolio | **NUOVA v2:** gestisce il registro brand_kit cross-istanza; rileva duplicati niche/angolo | **P0** — blocca l'apertura di canali doppioni |
| `mb-instance-launch-gate` | MB-Portfolio | **NUOVA v2:** implementa la checklist F-MB5 (≥10 video, ≥80% gate verdi) come verifica eseguibile | **P0** |
| `yt-publish-api` | YT-Pubblicazione | Upload/scheduling via YouTube Data API + end screen + playlist (CLI via printing-press) | P2 |
| `yt-retention-analyst` | YT-Pubblicazione | Lettura analytics → diagnosi drop-off → raccomandazioni a script brief | P2 |
| `kdp-niche-research` | PUB-Ricerca | Scorecard niche KDP (BSR, keyword, stagionalità, competizione) | P1 |
| `kdp-catalog-gap-scout` | PUB-Ricerca | **NUOVA v2:** analizza catalogo pubblicato per gap collana/serie | P2 |
| `kdp-listing-builder` | PUB-Packaging | Listing completo: 7 keyword, categorie, descrizione (copy da Marketing), pricing | P2 |
| `kdp-compliance-gate` | PUB-Pubblicazione | Checklist policy KDP pre-pubblicazione (incl. disclosure AI) | P2 |
| `order-handoff-validator` | YT-Produzione-Ordini / PUB-Produzione-Ordini | **NUOVA v2:** generico, condiviso: valida consegna CF contro acceptance_criteria del contratto | P2 |
| `ecom-product-research` | ECOM-Ricerca | Scorecard prodotto (margine, domanda, logistica) | P3 (F-MB7) |

**Regola anti-contraddizione (invariata):** prima di creare ogni skill nuova →
`skill-contradiction-analyzer` contro le esistenti.

---

## 7. KPI + Quality Gates

### 7.1 QA gate video (tutti bloccanti — pattern 4 Piano Maestro, invariati dal v1, owner esplicito v2)

| Gate | Quando | Criteri di pass (misurabili) | Owner v2 |
|---|---|---|---|
| **#1 Script Gate** | dopo consegna script da CF | hook nei primi 15s; struttura retention (loop aperti, payoff); aderenza brand_kit; lunghezza entro ±10% del target; zero claim non verificabili; similarità < soglia vs ultimi 20 script (anti-ripetitività); grammatica pulita | `mb-yt-opt-qa` + Brand-Voice Sentinel |
| **#2 Audio Gate** | dopo voiceover TTS | zero artefatti/glitch; pronuncia corretta; pacing conforme brand_kit; loudness -14 LUFS; durata audio = durata script ±5% | `mb-yt-handoff-validator` |
| **#3 Visual Gate** | dopo montaggio + thumbnail | risoluzione ≥1080p; zero frame neri/corrotti/watermark; coerenza stile visual; sync audio-video; thumbnail leggibile a 120px | `mb-yt-handoff-validator` + Quality Sentinel |
| **#4 SEO Gate** | dopo `WF-YT-OPT` | titolo ≤100 caratteri con keyword primaria; descrizione ≥200 parole con keyword/timestamp/CTA; 10-15 tag; end screen + cards impostate; metadata policy-safe | `mb-yt-opt-qa` |
| **+ Policy/Brand Gate** | pre-upload, sempre | checklist policy YouTube (contenuto AI: disclosure dove richiesta, no spam) + Mandato Empire | `mb-yt-publish-qa` + Sentinelle-Empire |

### 7.2 QA gate libro (invariati dal v1, owner esplicito v2)

| Gate | Criteri | Owner v2 |
|---|---|---|
| **Layout Gate** | PDF esattamente 6x9; ogni capitolo ha pagina immagine; zero placeholder grigi; `qa_report.md` verde | `mb-pub-book-qa` |
| **Cover Gate** | dimensioni trim+bleed corrette; testo dorso leggibile; conformità template KDP | `mb-pub-pkg-qa` |
| **Listing Gate** | titolo/sottotitolo senza keyword stuffing; descrizione APSOC approvata da Marketing; 7 keyword + 3 categorie coerenti | `mb-pub-pkg-qa` |
| **Compliance Gate** | checklist contenuti KDP (no contenuto ingannevole/duplicato; disclosure AI) + review umana finale | `mb-pub-compliance-checker` |

### 7.3 Gate NUOVI v2 (livello portafoglio e ordini)

| Gate | Quando | Criteri | Owner |
|---|---|---|---|
| **Order-QA Gate** | dopo ogni consegna da Content-Factory | consegna conforme all'acceptance_criteria del contratto; max 2 cicli di rework, poi escalation | `mb-yt-handoff-validator` / `mb-pub-order-handoff-validator` |
| **Instance Launch Gate** | prima di aprire una nuova istanza (canale/libro/store) | ≥10 pezzi pubblicati sull'istanza precedente con ≥80% gate verdi al primo colpo (criterio F-MB5) | `mb-port-launch-gate` |
| **Brand-Kit Uniqueness Gate** | prima di registrare un nuovo brand_kit | niche/angolo NON duplicato rispetto a istanze esistenti nello stesso sotto-business | `mb-port-brandkit-registry` |

### 7.4 KPI

| Livello | KPI | Soglia / uso |
|---|---|---|
| Video (48h/7gg) | CTR thumbnail; retention media %; % vista primi 30s; impression | baseline dopo i primi 10 video del canale — NON si inventano benchmark prima `[da ingestione F-MB1 + dati reali]` |
| Canale (mensile) | iscritti; watch-time; RPM (post-monetizzazione); % video gate-verdi al primo colpo; costo/video | ogni metrica letta da `WF-YT-ANALYTICS` → memoria |
| Libro (mensile) | BSR; vendite/royalty; recensioni (media, n); resa pipeline (giorni niche→pubblicato) | `WF-PUB-MONITOR`; libro sotto soglia 90gg → decisione kill/relaunch |
| Portafoglio (mensile, NUOVO v2) | n. istanze attive con gate stabili; revenue per istanza; costo agenti per istanza; % istanze aperte che superano il Launch Gate al primo tentativo | `WF-MB-PORTFOLIO-REVIEW` → report a C-Suite |
| Qualità (sempre) | 100% pubblicazioni passate dai gate; 0 strike policy; 0 rejection monetizzazione non previste | qualsiasi strike → freeze istanza + post-mortem ReasoningBank |

**Quality gates riassunto (tutti bloccanti):** Script/Audio/Visual/SEO + Policy/Brand per video
(§7.1); Layout/Cover/Listing/Compliance per libro (§7.2); Order-QA/Instance Launch/Brand-Kit
Uniqueness per il layer portafoglio (§7.3); dry-run + Cost-Sentinel per ogni ordine a
Content-Factory; review umana su ogni pubblicazione finché `mb-conductor` + C-Suite non
revocano il vincolo (criterio: 20 pubblicazioni consecutive senza correzioni umane).

---

## 8. Integrazione Ruflo

```
Ruflo = COORDINA (swarm per istanza, memoria, routing) · Claude Code = ESEGUE
```

**Topologia:** `hierarchical` (default holding) — `mb-conductor` coordinatore di ecosistema;
`mb-port-lead` coordinatore del layer portafoglio; lead di reparto (`mb-yt-strategy-coord`,
`mb-yt-order-lead`, `mb-yt-opt-coord`, `mb-yt-publish-coord`, `mb-pub-res-lead`,
`mb-pub-order-lead`, `mb-pub-pkg-lead`, `mb-pub-pub-lead`, `mb-ecom-*-lead`) coordinatori L2.
Fan-out `mesh` SOLO dentro batch paralleli disgiunti (istanze diverse, varianti thumbnail).

| Bisogno MB | Tool Ruflo | Configurazione |
|---|---|---|
| N canali / N libri in parallelo | `swarm_init` topology **hierarchical**, un branch per istanza | fan-out su istanze disgiunte; pipeline dentro ogni istanza sequenziale (le 4 fasi YT/PUB) |
| Apertura nuova istanza | `agent_spawn` autorizzato SOLO dopo `WF-MB-INSTANCE-LAUNCH-GATE` verde | coordinator on-demand; pool worker Haiku/WASM condiviso tra istanze |
| Decisioni (aprire istanza, killare niche, allocare budget) | `hive-mind propose/vote` (raft) con C-Suite, mediato da `MB-Portfolio` | solo decisioni con spesa o rischio policy |
| Memoria | `memory_store/search` namespace dedicati (§9) | ogni write rilevante → anche wiki `log.md` (pattern 12); `mb-port-qa` verifica isolamento |
| Apprendimento | `reasoningbank-*` su ogni gate rosso; `neural_train` sui pattern titolo/thumbnail/listing vincenti | feedback `WF-YT-ANALYTICS` e `WF-PUB-MONITOR` → `mb/yt|pub/patterns` |
| Costi | Cost-Sentinel + budget per-istanza allocato da `mb-port-budget-allocator`; dry-run default (pattern 3) | nessun ordine a CF senza stima costo |

---

## 9. Namespace memoria (convenzione estesa dal v1)

```
mb/strategy                       decisioni di portafoglio (quali business, quali budget) — ora popolato da MB-Portfolio
mb/portfolio/instances            registro istanze attive (canale/libro/store), stato, KPI aggregati       [NUOVO v2]
mb/portfolio/brandkit-registry    registro brand_kit cross-istanza, anti-duplicazione niche/angolo          [NUOVO v2]
mb/yt/patterns                    pattern cross-canale (hook, titoli, thumbnail che funzionano)
mb/yt/<canale-slug>/              brand_kit, calendario, storico video, metriche, gate-log
mb/yt/<canale-slug>/orders        stato ordini in corso verso Content-Factory                                [NUOVO v2]
mb/pub/patterns                   pattern cross-libro (niche, listing, cover)
mb/pub/<libro-slug>/              spec, stato pipeline, qa_report, royalty
mb/pub/<libro-slug>/orders        stato ordini manoscritto/immagini verso Content-Factory                    [NUOVO v2]
mb/ecom/<store-slug>/             (riservato, dormiente fino a F-MB7)
```

**Regola d'isolamento (invariata, ora verificata attivamente da `mb-port-qa`):** un agente che
lavora su `canale-1` legge `mb/yt/canale-1/*` + `mb/yt/patterns`, MAI il namespace di un altro
canale (anti cross-contaminazione §4c).

---

## 10. Build plan v2 (F-MB1...F-MB7, allineate a V2-6)

Questo dossier appartiene alla fase **V2-2** della roadmap (`11-PIANO-V2-DIRETTIVA-SCALA.md`
§10): è l'architettura target, non ancora la build. La costruzione effettiva dei 12 reparti —
team spawnati, workflow eseguiti, agenti attivi — avviene in **V2-6**, che segue l'ordine
`01→04→03→02→05`: Multi-Business è **l'ultimo ecosistema** della sequenza V2-6, dopo Agency,
Marketing, Content-Factory e Info-Business. Le fasi F-MB1...F-MB7 (invariate nell'ordine dal
v1) sono il piano di dettaglio da eseguire quando arriva il turno di 05 in V2-6.

| Fase | Cosa | Gate di uscita |
|---|---|---|
| **F-MB1 — INGESTIONE** (prima, vincolante) | Sessione dedicata Empire Studio su `@Legamidiamore` e `@dosementale`: frame reali + visione Claude. Ordine a Intelligence: `{dominio: yt-automation, output: 2 dossier}`. Estrarre: niche/angolo, formato, struttura script, stile visual/TTS, packaging, cadenza, segnali di monetizzazione | 2 dossier in wiki `sources/` + 1 synthesis comparativa; pattern operativi estratti e salvati in `mb/yt/patterns` |
| **F-MB2 — SCAFFOLDING V2** | Org `company/05-multibusiness/` (L2→L5) per tutti e 12 i reparti (incl. `MB-Portfolio`); namespace memoria §9; registrazione asset §5; ordini alla Forge per le skill P0/P1 (§6) | struttura navigabile; skill P0 (`mb-portfolio-registry`, `mb-instance-launch-gate`) consegnate e conformi; zero orfani tra gli asset §5 |
| **F-MB3 — CANALE PILOTA** | `WF-YT-NICHE` (informata dai dossier F-MB1) → `WF-YT-CHANNEL-LAUNCH` → brand_kit → calendario 30gg; `mb-port-brandkit-registry` registra la prima istanza | scheda niche approvata da `mb-yt-strategy-qa` + ok umano; canale creato; calendario pronto; registro portfolio inizializzato |
| **F-MB4 — PRIMO VIDEO** | Primo giro completo: ordine a CF → 4 gate + Policy/Brand → ottimizzazione → pubblicazione con review umana (= F7 Piano Maestro: "primo video pubblicato") | 1 video pubblicato con tutti i gate verdi; post-mortem in ReasoningBank |
| **F-MB5 — REGIME + MULTI-CANALE** | Cadenza warm-up sul pilota; quando ≥10 video con ≥80% gate verdi al primo colpo → `WF-MB-INSTANCE-LAUNCH-GATE` autorizza il secondo canale via swarm (brand_kit_2) | 2 canali in parallelo, memoria isolata (`mb-port-qa` verde), cost-attribution per canale |
| **F-MB6 — PUBLISHING RILANCIO** | Pipeline §4b end-to-end su 1 libro nuovo: wrapper book-factory, gate libro, listing via Marketing, pubblicazione con review | 1 libro pubblicato gate-verde; catalogo LIBRO 1-5 censito in `WF-PUB-MONITOR`; primo `WF-PUB-CATALOG-GAP` eseguito |
| **F-MB7 — E-COMM MVP** | Solo dopo F-MB5 e F-MB6 stabili: fase E1-E2 (§2.4); team ECOM portati a standard 6-10 SOLO qui | dossier prodotto + decisione modello + store MVP (se approvato) |

Ogni fase: checkpoint memoria, log in `wiki/log.md`, verify Empire verde prima di passare
oltre (ciclo a 9 passi ADR-006, `10-METODO-CICLO-FASE.md`).

---

## 11. Pre-mortem — rischi v2 (amplia §12 del v1)

| Rischio | Probabilità/Impatto | Mitigazione |
|---|---|---|
| **Ban/strike policy YouTube** (reused content, spam, metadata ingannevoli, network di canali) | media / critico | Policy/Brand Gate pre-upload obbligatorio (`mb-yt-publish-qa`); niche/angoli distinti per canale verificati da `mb-port-brandkit-registry`; cadenza warm-up; freeze immediato + post-mortem al primo strike |
| **Rejection monetizzazione YPP** (contenuto "ripetitivo/riutilizzato" tipico dei canali full-AI) | alta / alto | originalità misurata (similarity check nel Script Gate); valore aggiunto reale per video; studio F-MB1 `[da ingestione F-MB1]` |
| **Contenuto ripetitivo / decadimento qualità su volume** | alta / alto | soglia similarità vs ultimi 20 script; `WF-YT-ANALYTICS` retro-alimenta i brief; la cadenza non supera mai la capacità dei gate |
| **Disclosure contenuti AI** (YouTube: contenuti sintetici realistici; KDP: dichiarazione AI) | media / medio | checklist disclosure dentro Policy Gate (YT) e Compliance Gate (KDP), owner esplicito v2 |
| **Copyright** (musica, B-roll, immagini) | media / alto | nei contratti verso CF: solo asset generati o licenziati, fonte tracciata; Visual Gate verifica watermark |
| **Costi API** (HeyGen, ElevenLabs, image gen) fuori controllo su N istanze | media / medio | dry-run con stima costo; Cost-Sentinel + `mb-port-budget-allocator` con budget per-istanza; nessuna spesa senza ok esplicito |
| **Sospensione account KDP** | bassa / critico | Compliance Gate + review umana obbligatoria; mai mass-publishing low-effort |
| **Dipendenza da piattaforma** (YouTube/Amazon cambiano regole) | media / alto | clip cross-platform (`WF-YT-CROSSPOST`); e-comm/landing proprie come secondo canale di revenue |
| **Costruire la cattedrale prima del primo video** (rischio originario v1, ESTESO in v2 al layer portafoglio) | media / alto | F-MB4 forza output reale presto; ECOM tenuto a 5 agenti/reparto (non 6-10) fino a F-MB7; `MB-Portfolio` stesso NON si allarga oltre 6 agenti finché non gestisce ≥2 istanze reali |
| **`MB-Portfolio` diventa un livello burocratico senza valore** (rischio NUOVO v2: un reparto di governo su 1 sola istanza attiva è overhead puro) | media / medio | i workflow di `MB-Portfolio` restano dormienti in pratica (poche esecuzioni) finché non ci sono ≥2 istanze; il reparto è pre-costruito per lo scaling, non per gestire 1 canale |
| **YT-Pubblicazione sovraccarico** (pubblicazione + performance nello stesso reparto, 6 agenti per 2 funzioni distinte — rischio NUOVO v2, conseguenza della decisione §2 di NON separare Performance) | media / medio | se i KPI (§7.4, tasso di consegna per settimana, tempo medio diagnosi) mostrano collo di bottiglia, la scissione in reparto Performance dedicato resta un'opzione già progettata (analoga a 04-MARKETING-V2 L2.4) — tracciata in BACKLOG, non nello scope di questa fase |
| **Roster gonfiato senza esecuzione reale** (72 agenti su carta, la maggior parte mai spawnati) | alta nella fase V2-2/scaffolding | gli agenti sono `agent_spawn on-demand` (§8): esistere in un dossier ≠ girare; V2-6 esegue solo ciò che il piano di build §10 richiede fase per fase, mai tutto insieme |
| **Divergenza wiki/AgentDB sulle N istanze** | media / medio | pattern 12 wiki-first: ogni gate, pubblicazione e decisione logga in `wiki/log.md`; wiki-syncer di Memory Empire |

---

## 12. Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia LX→L5, backbone, pattern 1-12, roadmap F7/F9+
- [[05-ECOSISTEMA-MULTIBUSINESS]] — il v1 da cui si parte; resta riferimento per i dati sui canali e i vincoli di onestà (F-MB1)
- [[11-PIANO-V2-DIRETTIVA-SCALA]] §2 — direttiva suprema che governa questo dossier (ADR-007)
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] — fornitore di tutta la produzione materiale MB (video, manoscritti, cover, creative)
- [[04-ECOSISTEMA-MARKETING-V2]] — copy APSOC per listing, titoli, ads; modello di riferimento per il formato di questo dossier
- [[10-METODO-CICLO-FASE]] — ciclo a 9 passi con cui si esegue la build V2-6 di questo ecosistema
- [[Empire_Studio]] — motore dell'ingestione F-MB1 (frame reali + visione Claude)
- [[Memory_Empire]] — archiviazione e enrichment della conoscenza MB; namespace §9
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo: swarm, memoria, consensus (§8)
- [[Map - Workflow-Libri]] · [[Map - Kdp_-_Prodottti_Digitali]] — asset Publishing esistenti (§5)
- ADR-003 (wrap, non riscrittura) · ADR-007 (V2, CF-grade) · ADR-005 (minuzie → BACKLOG) · ADR-002 (memory-first) · ADR-006 (ciclo a 9 passi)
