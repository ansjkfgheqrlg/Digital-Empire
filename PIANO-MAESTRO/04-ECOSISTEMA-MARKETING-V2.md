# 📣 04 — ECOSISTEMA MARKETING V2 (Dossier EMPIRE OS)

> Dossier v2 (V2-2, ADR-007) — amplia il v1 `04-ECOSISTEMA-MARKETING.md` a scala CF-grade.
> Fonte: 11-PIANO-V2 §2.
>
> **Ecosistema L1 #04 della holding Digital Empire Group.** Il motore di persuasione
> trasversale: ogni parola che esce da EMPIRE OS con obiettivo di generare un'azione
> misurabile passa da qui. **Il Copywriting è la PRIORITÀ ASSOLUTA** di questo ecosistema
> e della holding intera. Marketing è il CUSTODE OPERATIVO del Mandato Art.2 (Brand Voice,
> APSOC, "prove non promesse").
>
> Versione: 2.0 · Creato: 2026-06-16 · Fase roadmap: V2-2
> Supera il v1 `04-ECOSISTEMA-MARKETING.md` per profondità e scala. Il v1 resta riferimento.
> Standard: CF-grade (§0 piano V2 `11-PIANO-V2-DIRETTIVA-SCALA.md`).

---

## 0. Missione + DONE WHEN

**MISSIONE:** trasformare ogni asset di Digital Empire — offerte agency, lanci info-business,
contenuti, listing, video, campagne — in copy che converte, secondo il framework **APSOC**
(Attenzione → Problema → Soluzione/Promessa → Obiezioni → CTA) + **CPB** (Claim → Proof →
Benefit), nella brand voice del Mandato Empire: diretta, provocatoria, trasparente, **"prove
non promesse"** (Art.2 Mandato). Marketing non possiede prodotti propri: è un **ecosistema
di servizio trasversale** e di governo del copy per l'intera holding.

In v2 Marketing non è un reparto con 4 sottoaree: è un **MEGA-REPARTO / azienda interna**
con gerarchia a livelli propria (MKT-Conductor → capi reparto L2 → coordinatori L3 →
verificatori e worker L4-L5), 6 reparti L2 completi (vs 4 del v1), team da 6-10 agenti
ciascuno, e workflow CF-grade strutturati (cartella-workflow con gerarchia, script, skill,
state, QA a cancelli, memoria namespace dedicata — standard §0 piano V2).

**DONE WHEN (misurabili):**
1. I 6 reparti L2 hanno org L3/L4 documentata, team 6-10 agenti a schede millimetriche,
   e almeno un workflow CF-grade eseguito end-to-end ciascuno.
2. Ogni richiesta di copy entra con il contratto `{committente, formato, awareness_level,
   icp, obiettivo, deadline}` e esce SOLO con score APSOC ≥80 (≥85 sales page) + brand
   gate G2 verde. Il gate è deterministico, non bypassabile (Art.4 Mandato).
3. I reparti Brand/Creative e Conversion Architecture — nuovi rispetto al v1 — hanno team
   e almeno un workflow ciascuno.
4. Tutte le skill marketing esistenti (cro-copy-architect, market-*, emails, ads, …) sono
   mappate a un reparto: **zero skill orfane** (come in v1, ma ora con reparto assegnato
   anche per Brand/Creative).
5. Il loop di ottimizzazione data-driven è attivo: performance → ReasoningBank → revisione
   copy, pattern vincenti per ICP salvati in `marketing/copy/patterns/{icp}`.
6. Almeno 3 ecosistemi committenti (Agency, Info-Business, Content-Factory) hanno ricevuto
   e accettato copy gated prodotto dal sistema.
7. I namespace AgentDB `marketing/` sono inizializzati; ogni workflow produce state
   ripartibile a freddo (test amnesia §6 piano V2).
8. Skill proprie dell'ecosistema forgiate (≥3: empire-brand-gate, copy-request-router,
   brand-strategy-gate) via 07-FORGE con PRD+architettura (standard §8 piano V2).

**OUT OF SCOPE (ora):** spesa ads reale senza ok esplicito di Max (vincolo globale);
pubblicazione automatica senza review umana nelle prime fasi; SEO tecnico (→ 06-PLATFORM);
produzione contenuti editoriali (→ 03-CONTENT-FACTORY).

---

## 1. Posizione nella holding — Marketing è il FORNITORE copy di tutti

```
                    👑 LX — Mandato Empire (Art.2 Brand Voice, APSOC, "prove non promesse")
                              + Brand-Voice Sentinel (always-on su ogni output)
                              |
L0  C-Suite ────── CMO ───────┤  (CMO = workflow CF-grade v2, non singolo file)
                              |
L1  04-MARKETING  ◄────── handoff contract ──────► tutti gli altri ecosistemi
        │
        ├── DIPENDE DA: 08-INTELLIGENCE (ricerca ICP, trend, competitor data),
        │              03-CONTENT-FACTORY (visual/creative per ads, brief design),
        │              06-PLATFORM (landing/tracking, Conversion Architecture con 06),
        │              09-OPERATIONS (runtime swarm, cost guard, scheduling)
        └── SERVE:    01-AGENCY      — copy outreach, preventivi, proposte
                      02-INFO-BUSINESS — copy lancio completo (sales page, VSL, email)
                      03-CF           — hook, headline, caption, CTA conversione
                      05-MB           — titoli YT, listing KDP, description app
                      04-MKT (sé)     — campagne DE, email list DE, brand identity
```

### 1.1 Handoff espliciti — chi chiede cosa a Marketing (tabella completa)

| Committente | Cosa richiede | Formato tipico | Reparto / Workflow destinazione |
|---|---|---|---|
| **01 AGENCY** | Copy preventivi/proposte; cold email/DM/LinkedIn; copy landing offerte (Outreach Factory, Content Factory, Second Brain, Engine Room) | `proposta`, `cold-email`, `landing` | L2.1 WF-COPY-FULL / WF-COPY-REVIEW |
| **02 INFO-BUSINESS** | Copy lancio completo: sales page, sequenza email lancio, VSL, ads di lancio | `sales-page`, `email-seq`, `vsl`, `ad` | L2.1 WF-COPY-SALES-PAGE + L2.3 WF-EMAIL-LAUNCH + L2.2 WF-ADS-CAMPAIGN |
| **03 CONTENT-FACTORY** | Hook, caption, titoli, script intro, CTA nei contenuti | `social`, `hook`, `headline` | L2.1 WF-COPY-SOCIAL + T-HEADLINE |
| **05 MULTI-BUSINESS** | Titoli/descrizioni YouTube; copy listing KDP/e-commerce; description app | `yt-meta`, `listing` | T-HEADLINE + WF-COPY-QUICK + L2.6 |
| **04 MKT (sé)** | Campagne ads DE, email list DE, brand identity DE, ottimizzazione funnel DE | tutti | tutti i reparti |

**Regola non negoziabile:** nessun ecosistema scrive copy di conversione in autonomia.
Può fare bozze, ma il gate APSOC + brand gate vivono in Marketing. (03-CF scrive contenuti
editoriali in autonomia; quando un contenuto ha CTA di conversione, la CTA passa dal gate.)

### 1.2 Contratto di richiesta copy (handoff contract standard — identico al v1, è già solido)

```json
{
  "committente": "01-AGENCY | 02-INFO | 03-CF | 05-MB | 04-MKT",
  "formato": "ad | sales-page | email-seq | cold-email | landing | vsl | social | headline | listing | yt-meta | proposta | review",
  "awareness_level": "unaware | problem-aware | solution-aware | product-aware | most-aware",
  "icp": "riferimento ICP/avatar (id namespace o brief inline)",
  "obiettivo": "azione misurabile attesa (reply, opt-in, acquisto, click)",
  "deadline": "YYYY-MM-DD"
}
```

Campi opzionali: `brand_kit` (default: Mandato Empire; override per clienti agency o canali YT),
`materiali` (briefing, proof, case study), `vincoli` (lunghezza, piattaforma, policy),
`acceptance_criteria`. Risposta di Marketing: `{copy_finale, score_APSOC, qa_report,
brand_gate: pass/fail, pattern_usati, workflow_eseguito}`.

**Regole del contratto (non negoziabili):**
- Richiesta senza `icp` → spawna A2 (Target Analyst) o T-AVATAR PRIMA di scrivere copy.
- Richiesta senza `awareness_level` → il router lo deduce e lo dichiara nel payload (mai implicito).
- Copy senza gate → output non valido, non si consegna al committente.

---

## 2. Reparti L2 v2 — da 4 a 6 reparti (revisione al rialzo, motivata)

Il v1 aveva 4 reparti (Copywriting, Advertising, Email, Analytics). In v2 si aggiungono:
- **L2.5 Brand/Creative Strategy** — il v1 non aveva un reparto dedicato all'identità di brand,
  al posizionamento visivo e alla strategia creativa. Questi compiti erano dispersi tra L2.1 (S2)
  e menzioni marginali. Con il Mandato Art.2 come invariante assoluta, il brand merita un reparto
  autonomo con gerarchia propria.
- **L2.6 Conversion Architecture** — il v1 aveva solo T-FUNNEL come funzione L4 sotto Copywriting.
  La progettazione di funnel multi-step, landing system e CRO strutturale è abbastanza complessa
  da richiedere un reparto con workflow propri (WF-FUNNEL-DESIGN, WF-CRO-SPRINT).

```
04-MARKETING (L1) — coordinatore: MKT-Conductor
 ├── L2.1 COPYWRITING                ← PRIORITÀ ASSOLUTA. Motore: Copy Workflow Orchestration Layer
 ├── L2.2 ADVERTISING                ← campagne paid (Meta, Google, LinkedIn, TikTok)
 ├── L2.3 EMAIL & LIFECYCLE          ← lifecycle completo: lancio, nurture, win-back, onboarding
 ├── L2.4 ANALYTICS & OTTIMIZZAZIONE ← tracking, attribution, A/B test, loop ReasoningBank
 ├── L2.5 BRAND & CREATIVE STRATEGY  ← NUOVO: identità, posizionamento, creative direction
 └── L2.6 CONVERSION ARCHITECTURE   ← NUOVO: funnel system, landing strategy, CRO strutturale
 ⊕   Copy/APSOC Guild (trasversale, condivisa con tutta la holding)
 ⊕   Brand-Voice Sentinel (always-on, riporta a LX — Art.2 Mandato)
```

---

### L2.1 — COPYWRITING (priorità massima, cuore dell'ecosistema)

**Missione:** produrre ogni copy di conversione della holding via APSOC+CPB, con QA a 100 punti.
**Ingloba il Copy Workflow Orchestration Layer esistente come motore: il sistema NON si riscrive,
si monta dentro l'organigramma con un wrapper di handoff** (ADR-003: wrap, non riscrittura).

**Dove il v1 era carente:** il v1 aveva il team corretto in linea di principio, ma le schede
agenti erano elenchi tabulari, non schede millimetriche (identità, I/O JSON, logica passo-passo,
KPI, escalation, esempi — standard §0 piano V2). In v2 ogni agente è una struttura, non una riga.

#### Team L2.1 (10 agenti — lead + QA + specialisti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `COPY-MASTER` | Copy Master (coordinatore) | coordinator | opus | Router decisionale: riceve il contratto, sceglie il workflow L3, spawna agenti, emette output gated |
| `A1` | Briefing Analyst | worker | sonnet | Raccolta requisiti → briefing-completo.md con ICP, obiettivo, awareness_level validati |
| `A2` | Target Analyst | worker | sonnet | Avatar + pain points + language map → `marketing/avatars/{icp}` |
| `A3` | Attention Writer | worker | opus | Headline + hook (9 strategie — da `concepts/Framework_Cold_Outreach_APSOC.md`) |
| `A4` | Problem Writer | worker | opus | Problema amplificato; regola: NO prodotto — solo il dolore del cliente |
| `A5` | Solution Writer | worker | opus | USP + benefits + visione post-acquisto (P sempre PRIMA di S — Art.4.2 Mandato) |
| `A6` | Objections Handler | worker | sonnet | CPB per ogni obiezione (10 tipi canonici + custom per ICP) |
| `A7` | CTA Writer | worker | opus | CTA profondo + urgenza reale (no scarcity falsa — Art.2.3 Mandato) |
| `A8` | Copy Reviewer | verifier | opus | Score APSOC 100pt — il gate QA; ≥80 standard, ≥85 sales page; **blocca se sotto soglia** |
| `COPY-QA-LEAD` | Copy QA Lead | verifier | opus | **NUOVO v2:** supervisore del gate; decide se un'iterazione è "fix mirato" o "rifacimento totale"; traccia il tasso first-pass rate |

Agenti strategici (prestati a tutti i reparti L2):

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `S1` | Funnel Strategist | worker | sonnet | Architettura funnel multi-step (presta a L2.6) |
| `S2` | Positioning Strategist | worker | sonnet | Posizionamento, USP, angolo di mercato (presta a L2.5) |
| `S3` | Campaign Strategist | worker | sonnet | Strategia campagna multi-canale (presta a L2.2) |

#### Workflow L3 di L2.1 (6 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-COPY-FULL** | Pipeline A1→A8 completa per copy complesso (sales page, proposta, VSL) | Score A8 ≥80/85 + G2 brand gate + G4 contract check |
| **WF-COPY-AD** | 3+ varianti copy APSOC per ads — output veloce (15-20 min target) | A8 ≥80 su ogni variante; compliance G3 |
| **WF-COPY-SALES-PAGE** | Sales page completa con sezioni APSOC strutturate — gate ≥85 | A8 ≥85; P prima di S verifica; G2; G4 |
| **WF-COPY-EMAIL** | Sequenze email APSOC per lancio/nurture/win-back (in coordinamento con L2.3) | A8 ≥80 per email; subject + deliverability check (E2) |
| **WF-COPY-VSL** | Script VSL 8-20 min strutturato per hook video | A8 ≥80; timing check; G2 |
| **WF-COPY-SOCIAL** | 5 post in sequenza strategica (hook + narrazione + CTA) | A8 ≥80; brand gate; pattern library check |

#### Funzioni L4 di L2.1

`T-HEADLINE` (10+ headline con formule) · `T-OBJECTIONS` (CPB per obiezione) · `T-AVATAR`
(buyer persona completa → namespace memoria) · `T-REVIEW` (score 100pt su copy esistente) ·
`T-APSOC` (costruzione APSOC interattiva) · `T-AWARENESS-ROUTER` (adatta struttura APSOC al
livello awareness — unaware vs most-aware: dosaggio A/P vs O/C) **[NUOVO v2]**

---

### L2.2 — ADVERTISING (campagne paid end-to-end)

**Missione:** campagne paid end-to-end (strategia → creative → setup → monitoraggio →
iterazione) su Meta, Google, LinkedIn, TikTok. Il copy delle ads viene SEMPRE da L2.1
(WF-COPY-AD); Advertising possiede targeting, budget, struttura campagna, testing creativo.

**Dove il v1 era carente:** 4 agenti (AD1-AD4) senza coordinatore di reparto dedicato e
senza un Campaign Lead che risponda del reparto come unità. In v2 il reparto ha 8 agenti
con lead, QA e specialisti.

#### Team L2.2 (8 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `ADS-LEAD` | Advertising Lead | coordinator | opus | **NUOVO v2:** coordina il reparto; riceve brief da MKT-Conductor; assegna workflow; risponde dei KPI paid |
| `AD1` | Audience Analyst | worker | sonnet | Ricerca audience, segmenti, lookalike per piattaforma; input da 08-INTELLIGENCE |
| `AD2` | Creative Iterator | worker | sonnet | Varianti creative a scala dal winner (skill ad-creative); fan-out swarm |
| `AD3` | Media Buyer | worker | sonnet | Struttura campagna, budget, bid, pacing (sotto Cost-Sentinel; dry-run default Art.4.3) |
| `AD4` | Ad Compliance Checker | verifier | sonnet | Policy Meta/Google/LinkedIn/TikTok pre-flight — blocca se non conforme (G3) |
| `AD5` | Platform Specialist | worker | sonnet | **NUOVO v2:** specialista per piattaforma (split Meta vs Google vs LinkedIn vs TikTok) — sa le differenze di formato/algoritmo/policy |
| `AD6` | Creative Analyst | worker | sonnet | **NUOVO v2:** analizza le performance creative (CTR per creative, heat map dei formati) e identifica pattern per AD2 |
| `AD-QA` | Ads QA Verifier | verifier | sonnet | **NUOVO v2:** verifica che ogni campagna rispetti il brand_kit dichiarato, il pricing corretto e i vincoli legali prima del lancio |

#### Workflow L3 di L2.2 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-ADS-CAMPAIGN** | Campagna end-to-end: brief → S3 strategia → AD1 audience → WF-COPY-AD copy → creative → setup → dry-run | G1 copy ≥80; G3 compliance; G4 contratto; ok umano per spesa reale (Art.4.3) |
| **WF-CREATIVE-TEST** | Batch testing creativo: fan-out varianti → matrice copy × visual × audience → verdetto statistico | AN3 verifica dimensione campione; verdetto solo con soglia minima raggiunta |
| **WF-ADS-PERFORMANCE** | Loop monitoraggio continuo: AN2 → diagnosi → AD2 iterazione dal winner → aggiornamento `marketing/ads/experiments` | Dati minimi per verdetto; mai forzato sotto soglia (regola anti-rumore) |

---

### L2.3 — EMAIL & LIFECYCLE (completo, non solo lancio)

**Missione:** email lifecycle completo — lancio, onboarding, nurture, win-back/post-cancel,
transazionale. **Confine col cold:** il cold outreach operativo (Outreach Workflow, writer.py)
resta in 01-AGENCY; Marketing possiede lo **standard APSOC+V** e fa QA/evoluzione dei
template cold via T-REVIEW.

**Dove il v1 era carente:** 3 agenti (E1-E3) senza lead di reparto e senza un agente dedicato
all'onboarding e al transazionale. In v2 il reparto è autonomo con 7 agenti.

#### Team L2.3 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `EMAIL-LEAD` | Email & Lifecycle Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; progetta la strategia di comunicazione lifecycle; risponde dei KPI email |
| `E1` | Lifecycle Architect | worker | sonnet | Disegno sequenze (trigger, timing, branching per awareness × comportamento) |
| `E2` | Deliverability Guard | verifier | sonnet | Spam score, igiene lista, autenticazione dominio (SPF/DKIM/DMARC); PII check obbligatorio (Art.7) |
| `E3` | Segmentation Analyst | worker | sonnet | Segmenti per ICP × awareness × comportamento (input da AN3) |
| `E4` | Onboarding Specialist | worker | sonnet | **NUOVO v2:** sequenze onboarding welcome + attivazione per SaaS/Info (committente 05-MB / 02-INFO) |
| `E5` | Win-Back Specialist | worker | sonnet | **NUOVO v2:** sequenze post-cancel e churn prevention (skill churn-prevention); A6 Objections Handler è l'asse portante |
| `E-QA` | Email QA Verifier | verifier | sonnet | **NUOVO v2:** verifica ogni email vs A8 score + brand gate + deliverability prima dell'invio |

#### Workflow L3 di L2.3 (4 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-EMAIL-LAUNCH** | Sequenza lancio (pre-lancio → apertura → proof → obiezioni → scarcity → chiusura) per 02-INFO | WF-COPY-EMAIL score ≥80; E2 deliverability OK; G2 brand gate; review umana nelle prime fasi (Art.4.4) |
| **WF-EMAIL-NURTURE** | Welcome + nurture + re-engagement lista; T-SUBJECT genera/testa subject | A8 ≥80; WF-AB-TEST su subject e CTA; AN4 distilla pattern |
| **WF-EMAIL-ONBOARDING** | Sequenza onboarding attivazione per utenti SaaS/Info | E4 progetta; E2 verifica; pattern in `marketing/email/sequences` |
| **WF-EMAIL-WINBACK** | Post-cancel / churn prevention / dunning (skill churn-prevention); exit survey → insight | E5 + A6 (il churn è un'obiezione non gestita); esito → AN4 → pattern "motivi di churn per ICP" |

---

### L2.4 — ANALYTICS & OTTIMIZZAZIONE (il loop che rende il sistema auto-migliorante)

**Missione:** misurare l'effetto di ogni copy/campagna e chiudere il cerchio. I dati diventano
pattern (ReasoningBank) e i pattern diventano revisioni di copy. È il reparto che rende il
sistema **auto-migliorante** (pattern #5 Piano Maestro).

**Dove il v1 era carente:** 4 agenti (AN1-AN4) senza lead di reparto e senza un agente
dedicato all'Observability dell'intero ecosistema. In v2 il reparto ha 7 agenti con gerarchia.

#### Team L2.4 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `AN-LEAD` | Analytics Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; definisce il piano di misurazione per ogni campagna; risponde dei KPI di ottimizzazione |
| `AN1` | Tracking Engineer | worker | sonnet | Tracking plan, UTM, eventi, conversion API (in coordinamento con 06-PLATFORM) |
| `AN2` | Attribution Analyst | worker | sonnet | Attribuzione per canale/campagna/copy; legge performance per copy_id |
| `AN3` | Experiment Designer | worker | sonnet | Ipotesi, varianti, dimensionamento test (minimo statistico prima di dichiarare il vincitore) |
| `AN4` | Insight Distiller | worker | sonnet | Performance → pattern ReasoningBank; scrive in `marketing/copy/patterns/{icp}` e `marketing/copy/antipatterns/{icp}` |
| `AN5` | Funnel Analyst | worker | sonnet | **NUOVO v2:** analisi funnel step-by-step (drop rate per sezione APSOC, bounce, micro-conversion) → input per L2.6 e per A8 diagnosi |
| `AN-OBSERVER` | Marketing Observability Lead | verifier | sonnet | **NUOVO v2:** monitora i KPI dell'intero ecosistema 04-MARKETING; segnala anomalie al MKT-Conductor; alimenta il report CMO |

#### Workflow L3 di L2.4 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-TRACKING-SETUP** | Tracking plan, UTM, eventi, conversion API per ogni campagna/funnel | Verifica AN1: ogni evento tracciato ha un nome, un trigger e un valore misurato; nessun "evento fantasma" |
| **WF-OPTIMIZATION-LOOP** | Loop data-driven §4d: raccolta → diagnosi → distillazione → revisione copy → A/B test → consolida | Ciclo completo tracciato in state.json; pattern consolidati solo con evidenza ripetuta (anti-rumore AN3) |
| **WF-AB-TEST** | Disegno ed esecuzione esperimenti (ipotesi → varianti → dimensione → verdetto) | AN3 verifica dimensione; verdetto con criterio predefinito; esito → `marketing/ads/experiments` |

---

### L2.5 — BRAND & CREATIVE STRATEGY (NUOVO rispetto al v1)

**Missione:** definire, proteggere e evolvere l'identità di brand di Digital Empire e dei
clienti multi-tenant. La strategia creativa è il sistema nervoso visivo e concettuale che
rende il copy coerente, riconoscibile e differenziato. Il v1 non aveva un reparto dedicato:
S2 (Positioning Strategist) era un agente singolo senza reparto, senza workflow e senza
gerarchia. In v2 questo reparto è autonomo.

**Connessione con il Mandato:** questo reparto è il **custode operativo del Mandato Art.2**
— ogni nuova produzione creativa viene verificata contro la Brand Checklist dell'Art.2.
Brand-Voice Sentinel riporta a LX, ma Brand & Creative Strategy è il fornitore della
conoscenza di brand che la Sentinel usa come riferimento.

#### Team L2.5 (6 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `BRAND-LEAD` | Brand Strategy Lead | coordinator | opus | Coordina il reparto; custodisce il brand positioning DE; approva evoluzioni di brand voice |
| `BR1` | Positioning Strategist | worker | opus | (ex S2) Posizionamento, USP, angolo di mercato — differenziazione da competitor |
| `BR2` | Brand Voice Architect | worker | opus | Formalizza e aggiorna le linee guida della brand voice (diretta/provocatoria/trasparente Art.2) per ogni brand_kit |
| `BR3` | Creative Director | worker | sonnet | Brief visivo/creativo per 03-CONTENT-FACTORY; direction per creative ads |
| `BR4` | Brand Analyst | worker | sonnet | Analisi competitor, differenziazione, awareness del mercato (in coordinamento con 08-INTELLIGENCE) |
| `BR-QA` | Brand Consistency Verifier | verifier | sonnet | Verifica che ogni output (copy, creative, landing) sia coerente con il brand_kit dichiarato e il Mandato Art.2 |

#### Workflow L3 di L2.5 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-BRAND-AUDIT** | Audit completo del brand positioning: analisi competitor + voice + differenziazione + gap → report + raccomandazioni | BR-QA verifica coerenza con Mandato Art.2; output in `marketing/brand/audit` |
| **WF-BRAND-KIT-BUILD** | Costruzione brand_kit per nuovo cliente/canale: voice guide + visual brief + ICP + tone chart | BRAND-LEAD approva; kit in `marketing/brand/kits/{brand_kit_id}`; pronto per uso in contratto handoff |
| **WF-BRAND-EVOLUTION** | Proposta evolutiva del brand DE: brief → analisi → proposta → ok Max (solo Max modifica Art.2) | Proposta come ADR-bozza; non si attua senza approvazione Max via ADR (Art.5.3 Mandato) |

---

### L2.6 — CONVERSION ARCHITECTURE (NUOVO rispetto al v1)

**Missione:** progettare l'architettura completa di conversione — funnel multi-step, landing
system, sequenze di pagine, micro-conversion map — in collaborazione con 06-PLATFORM (che
costruisce le pagine tecnicamente). Marketing possiede la STRATEGIA di conversione; Platform
possiede l'implementazione. Il v1 aveva solo T-FUNNEL come funzione L4 sotto L2.1: troppo
poco per un'area che determina l'efficacia di tutto il copy.

#### Team L2.6 (6 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `CONV-LEAD` | Conversion Architecture Lead | coordinator | opus | Coordina il reparto; disegna l'architettura di conversione per ogni committente; risponde dei KPI funnel |
| `CA1` | Funnel Strategist | worker | opus | (ex S1, promosso a L2.6) Architettura funnel multi-step (ToFu → MoFu → BoFu) con mapping APSOC per stage |
| `CA2` | Landing Page Strategist | worker | sonnet | Struttura della landing: hero → proof → offer → objections → CTA; brief tecnico per 06-PLATFORM |
| `CA3` | Micro-Conversion Analyst | worker | sonnet | Mappa micro-conversioni (scroll depth, click CTA, opt-in) → input per AN5 e per ottimizzazione |
| `CA4` | CRO Sprint Lead | worker | sonnet | Esecuzione sprint CRO: identifica collo di bottiglia → variante → test → implementazione (skill cro) |
| `CA-QA` | Conversion QA Verifier | verifier | sonnet | Verifica che ogni funnel rispetti la struttura APSOC end-to-end e i KPI di conversione attesi |

#### Workflow L3 di L2.6 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-FUNNEL-DESIGN** | Design completo del funnel: obiettivo → stage map → copy per stage (handoff a L2.1) → landing brief (handoff a 06-PLATFORM) → sequenza email (handoff a L2.3) | CA-QA verifica coerenza APSOC end-to-end; ogni stage ha copy gated; brief tecnico approvato |
| **WF-CRO-SPRINT** | Sprint ottimizzazione conversione: AN5 identifica drop → CA4 variante → WF-AB-TEST → implementazione → misurazione | Verdetto A/B statisticamente valido; implementazione solo dopo gate AN3; risultato in `marketing/cro/sprints` |
| **WF-LANDING-AUDIT** | Audit landing esistente (struttura APSOC + micro-conversion + velocità + mobile) → report diagnostico + azioni prioritarie | CA-QA + AN5; output in `marketing/cro/audits`; 3 azioni prioritarie con impatto stimato |

---

## 3. Roster agenti completo (tutti i reparti)

### MKT-Conductor (L1)

| ID | Agente | Tipo | Tier | Ruolo |
|---|---|---|---|---|
| `MKT-0` | MKT-Conductor | coordinator | opus | Coordinatore ecosistema L1: riceve handoff dal BUS, valida contratto, smista ai reparti, gestisce coda multi-committente, escalation a C-Suite |

### L2.1 Copywriting (10 + 3 strategici = 13 agenti)

`COPY-MASTER` · `A1` · `A2` · `A3` · `A4` · `A5` · `A6` · `A7` · `A8` · `COPY-QA-LEAD` [nuovo]
+ `S1` (Funnel Strategist, presta a L2.6) · `S2` (Positioning Strategist, presta a L2.5) · `S3` (Campaign Strategist, presta a L2.2)

**Agenti ESISTENTI (dal Copy Workflow Orchestration Layer — NON duplicare, registrare):**
A1, A2, A3, A4, A5, A6, A7, A8, S1, S2, S3, COPY-MASTER (orchestratore esistente in
`SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/`).

### L2.2 Advertising (8 agenti)

`ADS-LEAD` [nuovo] · `AD1` · `AD2` · `AD3` · `AD4` · `AD5` [nuovo] · `AD6` [nuovo] · `AD-QA` [nuovo]

### L2.3 Email & Lifecycle (7 agenti)

`EMAIL-LEAD` [nuovo] · `E1` · `E2` · `E3` · `E4` [nuovo] · `E5` [nuovo] · `E-QA` [nuovo]

### L2.4 Analytics & Ottimizzazione (7 agenti)

`AN-LEAD` [nuovo] · `AN1` · `AN2` · `AN3` · `AN4` · `AN5` [nuovo] · `AN-OBSERVER` [nuovo]

### L2.5 Brand & Creative Strategy (6 agenti — reparto NUOVO)

`BRAND-LEAD` [nuovo] · `BR1` · `BR2` [nuovo] · `BR3` [nuovo] · `BR4` [nuovo] · `BR-QA` [nuovo]

### L2.6 Conversion Architecture (6 agenti — reparto NUOVO)

`CONV-LEAD` [nuovo] · `CA1` · `CA2` [nuovo] · `CA3` [nuovo] · `CA4` [nuovo] · `CA-QA` [nuovo]

### Trasversali

`SEN-BV` Brand-Voice Sentinel (always-on, riporta a LX — Art.2 Mandato)

---

### Conteggio roster v2

| Categoria | Agenti esistenti (dal motore copy) | Agenti nuovi v2 | Totale |
|---|---|---|---|
| MKT-Conductor L1 | 0 | 1 | 1 |
| L2.1 Copywriting | 12 (copy-master, A1-A8, S1-S3) | 1 (COPY-QA-LEAD) | 13 |
| L2.2 Advertising | 4 (AD1-AD4) | 4 (ADS-LEAD, AD5, AD6, AD-QA) | 8 |
| L2.3 Email | 3 (E1-E3) | 4 (EMAIL-LEAD, E4, E5, E-QA) | 7 |
| L2.4 Analytics | 4 (AN1-AN4) | 3 (AN-LEAD, AN5, AN-OBSERVER) | 7 |
| L2.5 Brand (NUOVO) | 1 (S2 promosso) | 5 | 6 |
| L2.6 Conversion (NUOVO) | 1 (S1 promosso) | 5 | 6 |
| Trasversali | 1 (SEN-BV) | 0 | 1 |
| **TOTALE** | **26** | **23** | **49** |

*(Il v1 aveva ~26 agenti registrati, di cui 13 esistenti dal motore copy. In v2 si aggiungono
23 nuovi agenti per portare ogni reparto allo standard 6-10 con lead + QA + specialisti.)*

---

## 4. Workflow chiave CF-grade (pipeline APSOC master + routing)

### (a) Routing cross-ecosistema — il flusso di ingresso principale

```
[Ecosistema committente]
   │  handoff contract {committente, formato, awareness_level, icp, obiettivo, deadline}
   ▼
MKT-Conductor ──► valida contratto (campi obbligatori? icp esiste in namespace memoria?)
   │                 ├─ icp mancante → spawna A2 / T-AVATAR PRIMA di tutto (non si scrive senza avatar)
   │                 └─ awareness mancante → deduce da funnel stage + dichiara nel payload (mai implicito)
   ▼
COPY-MASTER ──► memory_search("marketing/copy/patterns/{icp}") ← pattern vincenti pregressi
   │             (workflow adattivo: il sistema impara da ogni run — pattern #7 Piano Maestro)
   ▼  ROUTING PER FORMATO
   ├─ ad / yt-meta / listing      → WF-COPY-AD (varianti rapide, ~15-20 min)
   ├─ sales-page / landing        → WF-COPY-SALES-PAGE (gate ≥85)
   ├─ email-seq                   → WF-COPY-EMAIL (in coordinamento con L2.3)
   ├─ cold-email / proposta       → standard APSOC+V + T-REVIEW (esecuzione in 01-AGENCY, standard qui)
   ├─ vsl                         → WF-COPY-VSL
   ├─ social / hook / headline    → WF-COPY-SOCIAL / T-HEADLINE
   ├─ review                      → T-REVIEW (score su copy esistente senza riscrittura)
   └─ progetto complesso          → WF-COPY-FULL (A1→A8) + S1/S2/S3 se serve strategia
   ▼
A8 Copy Reviewer ──► score <80 (o <85 sales page) → iterazione mirata COPY-QA-LEAD (max 3, poi escalation umana)
   ▼
Brand-Voice Sentinel ──► G2 brand gate Mandato Art.2 → fail = blocco non derogabile (solo LX sblocca)
   ▼
G4 Contract Check ──► MKT-Conductor verifica acceptance_criteria del committente
   ▼
Risposta handoff: {copy_finale, score_APSOC, qa_report, brand_gate, pattern_usati, workflow_eseguito}
   └─► hooks post-task: memory_store risultato + entry in wiki/log.md (Art.5 Mandato — wiki-first)
```

### (b) Loop ottimizzazione data-driven — il cerchio che si chiude (§4d v1, confermato e ampliato)

```
1. RACCOLTA    AN1/AN2: performance per copy_id (CTR, reply, opt-in, vendite, per canale)
               AN5: drop rate per sezione APSOC (dove il lettore abbandona?)
2. DIAGNOSI    AN2 + T-REVIEW: il copy sotto-performa su quale sezione APSOC?
               (hook debole = A · drop a metà = P/S · click senza conversione = O/C)
3. DISTILLA    AN4 Insight Distiller → ReasoningBank:
               - fallimento → anti-pattern ("ICP dentisti: hook su fatturato = ignorato")
               - successo  → pattern vincente → memory_store in marketing/copy/patterns/{icp}
4. REVISIONE   COPY-MASTER riapre il copy SOLO sulla sezione diagnosticata
               (mai riscrittura totale di un copy che performa parzialmente — regola anti-deriva)
5. TEST        WF-AB-TEST: vecchia vs nuova variante → verdetto con criterio predefinito
6. CONSOLIDA   winner → pattern library; wiki/log.md aggiornato; neural_train periodico
   └──────────────────────────────────────────► torna a 1 (loop continuo, auto-migliorante)
```

Regola anti-deriva: **nessuna revisione di copy basata su opinioni** — solo su dati del loop
o su score A8. "Prove non promesse" vale anche internamente (Art.2.2 Mandato).

### (c) Campagna ads end-to-end

```
Brief campagna (committente + BUDGET OK ESPLICITO di Max — MAI spesa autonoma Art.4.3)
   ▼
S3 Campaign Strategist ── obiettivo, canali, struttura, KPI target
   ▼
AD1 Audience Analyst ── segmenti per piattaforma ──┐
   ▼                                               │ PARALLELO (swarm fan-out)
WF-COPY-AD (L2.1) ── 3+ varianti copy APSOC ───────┤
   ▼                                               │
BR3 Creative Director → handoff 03-CF ── visual ───┘
   ▼
AD5 Platform Specialist ── brief specifico per piattaforma (formato/algoritmo/policy)
   ▼
AD2 Creative Iterator ── matrice copy × visual × audience
   ▼
AD4 Compliance ── G3 policy check → AD3 Media Buyer ── setup campagna (dry-run di default)
   ▼
LAUNCH (previa approvazione umana) → monitoraggio AN2/AN-OBSERVER → WF-ADS-PERFORMANCE
   └─ winner → AD2 itera nuove varianti dal winner (loop creativo continuo)
   └─ AD6 Creative Analyst → pattern di formato/performance → ReasoningBank
```

### (d) Funnel design completo — Marketing × Platform

```
Committente (es. 02-INFO per lancio corso)
   ▼
CONV-LEAD + CA1 ── mappa funnel stage (ToFu → MoFu → BoFu con obiettivo per stage)
   ▼
Per ogni stage:
   WF-COPY-FULL / WF-COPY-SALES-PAGE (L2.1) ── copy gated
   WF-EMAIL-LAUNCH / WF-EMAIL-NURTURE (L2.3) ── email gated
   Brief tecnico landing → 06-PLATFORM (implementa; Marketing definisce la strategia)
   ▼
CA3 Micro-Conversion Analyst ── mappa micro-conversioni per stage
   ▼
CA-QA ── verifica coerenza APSOC end-to-end su tutti gli stage
   ▼
Funnel live → AN5 analisi drop → WF-CRO-SPRINT se serve ottimizzazione
```

---

## 5. Asset esistenti wrappati (ADR-003: mappatura + wrapper, MAI riscrittura)

### 5.1 Motore primario — Copy Workflow Orchestration Layer

| Asset | Reparto | Azione v2 |
|---|---|---|
| `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` (intero sistema: SKILL.md, copy-master, A1-A8, S1-S3, 6 sub-skill, 6 workflow, 4 template, references, evals) | L2.1 Copywriting | **INGLOBA come motore.** Wrapper handoff sopra `/copywriting`; registrazione agenti in Identity-HR; zero modifiche ai file finché il wrapper non è validato (M1). Fonte di verità: il sistema che gira, non i file nuovi |
| `company/Ecosistemi/04-MARKETING/` (cartella buildata in F1-bis: Agenti/, Reparti/, Workflow/, Funzioni/) | tutti i reparti | **BASE ESISTENTE:** i file .md delle schede agenti (A1-A8, AD1-AD4, E1-E3, AN1-AN4, S1-S3, MKT-0, SEN-BV) e workflow esistenti sono il punto di partenza. In v2 si AMPLIANO (schede millimetriche, I/O JSON, logica passo-passo) senza riscrivere ciò che funziona |

### 5.2 Skill esistenti — mapping a reparto (zero skill orfane)

| Skill | Reparto | Gerarchia (motore / ausiliaria / knowledge) |
|---|---|---|
| `cro-copy-architect` | Copy/APSOC Guild (trasversale) | **knowledge layer condiviso** — pattern #6; usata da tutti gli ecosistemi che toccano copy |
| `copywriting`, `copy-workflow` | L2.1 | Entry point — restano invocabili così come sono |
| `copy-editing` | L2.1 / T-REVIEW | Sub-funzione QA editoriale |
| `marketing-psychology` | Copy/APSOC Guild | Reference trasversale (bias, trigger) per A3-A7 e L2.2 |
| `cro` | L2.6 / WF-CRO-SPRINT | Ottimizzazione page-level |
| `ab-testing` | L2.4 / WF-AB-TEST | Motore disegno esperimenti |
| `analytics` | L2.4 / WF-TRACKING-SETUP | Motore tracking plan |
| `ads` | L2.2 / WF-ADS-CAMPAIGN | Strategia campagna, targeting, bidding |
| `ad-creative` | L2.2 / T-CREATIVE-BATCH | Generazione varianti a scala |
| `emails` | L2.3 | Motore sequenze lifecycle |
| `cold-email` | L2.3 (standard) + L2.1 (QA) | Standard scrittura; esecuzione operativa resta in 01-AGENCY |
| `churn-prevention` | L2.3 / WF-EMAIL-WINBACK | Post-cancel, save offer, dunning |
| `sms`, `popups` | L2.3 (canali secondari) | Attivate quando committente le richiede |
| `market` (orchestratore suite) | L1 / MKT-Conductor | **Da arbitrare in M1:** si sovrappone a MKT-Conductor → contradiction-analyzer, poi assorbire o ritirare |
| `market-copy`, `market-brand` | L2.1 / L2.5 | Ausiliarie; motore primario resta Copy Workflow (no doppio standard) |
| `market-ads` | L2.2 | Ausiliaria di T-CREATIVE-BATCH |
| `market-emails` | L2.3 | Ausiliaria di E1 |
| `market-funnel` | L2.6 / CA1 | Ausiliaria del Funnel Strategist (ora in L2.6) |
| `market-audit`, `market-report`, `market-report-pdf` | L2.4 / T-REPORT | Reporting per committente |
| `market-landing` | L2.6 + 06-PLATFORM | Marketing possiede la strategia; Platform l'implementazione |
| `market-launch` | L2.3 + 02-INFO | Ausiliaria di WF-EMAIL-LAUNCH |
| `market-proposal` | L2.1 (via 01-AGENCY) | In prestito ad AGENCY per proposte |
| `market-social`, `market-competitors` | L2.5 (brand) + 08-INTELLIGENCE | Brand identity e competitor data |
| `market-seo` | 03-CF / 06-PLATFORM | NON di Marketing: mappata lì; qui solo consultata da AN5 |
| `marketing-ideas`, `content-strategy`, `customer-research`, `competitor-profiling` | supporto | Input per BR4/S2/S3/A2; ownership primaria in 08-INTELLIGENCE |
| Wiki `concepts/Framework_Cold_Outreach_APSOC.md` | L2.1/L2.3 — BRAIN | Fonte di verità standard APSOC+V — referenziata, non duplicata |
| Wiki `tools/Tool_Copy_Workflow_Orchestration.md` | BRAIN | Documentazione motore — aggiornare quando wrapper live |

---

## 6. Skill NUOVE da forgiare (via 07-FORGE, standard §8 piano V2: PRD → architettura → build)

| Skill nuova | Reparto | Cosa fa | Priorità |
|---|---|---|---|
| `empire-brand-gate` | LX/SEN-BV | Checklist brand gate Mandato Art.2 eseguibile: voce · prove · APSOC · pricing · zero AI-slop · autonomia cliente · brand_kit dichiarato | **P0** — serve dal giorno 1 |
| `copy-request-router` | MKT-Conductor | Implementa il contratto §1.2 + routing per formato §4a; valida campi obbligatori | **P0** |
| `brand-strategy-gate` | L2.5 | Verifica coerenza brand_kit di un output: voce, visual language, differenziazione vs competitor | **P0** |
| `copy-performance-loop` | L2.4 | Codifica il loop §4b: diagnosi per sezione APSOC, scrittura pattern in ReasoningBank/namespace | P1 |
| `icp-pattern-library` | L2.1/L2.4 | Lettura/scrittura strutturata dei pattern vincenti per ICP (schema: icp, formato, sezione, pattern, evidenza, data) | P1 |
| `awareness-router` | L2.1 | Adatta struttura APSOC al livello awareness (unaware → most-aware: dosaggio A/P vs O/C) | P1 |
| `ads-compliance` | L2.2 | Pre-flight policy Meta/Google/LinkedIn/TikTok per formato, claim, visual | P2 |
| `email-lifecycle-architect` | L2.3 | Disegno sequenze con trigger/timing/branching (formalizza E1) | P2 |
| `conversion-funnel-designer` | L2.6 | Architettura funnel multi-step con mapping APSOC per stage e brief tecnico per 06-PLATFORM | P2 |
| `cro-sprint-runner` | L2.6 | Esecuzione sprint CRO: diagnosi collo di bottiglia → variante → test → misurazione | P3 |

**Regola anti-contraddizione:** prima di creare ogni skill nuova → `skill-contradiction-analyzer`
contro le esistenti. Rischio concreto: sovrapposizione `empire-brand-gate` vs Checklist Brand Gate
Mandato Art.2 esistente → la skill IMPLEMENTA la checklist esistente, non la ridefinisce.

---

## 7. KPI + Quality Gates

### 7.1 Quality gates (bloccanti, in serie — Art.4 Mandato, pattern #4)

| Gate | Chi | Soglia | Esito fail |
|---|---|---|---|
| **G1 — Score APSOC** | A8 Copy Reviewer + COPY-QA-LEAD | ≥80/100 standard · ≥85 sales page · P prima di S (violazione = −15 automatico, senza eccezioni — Art.4.2) | Iterazione mirata (max 3 cicli) → escalation umana; non si bypassa |
| **G2 — Brand gate Mandato Art.2** | Brand-Voice Sentinel (`empire-brand-gate`) | Checklist binaria: voce diretta/provocatoria/trasparente · ogni claim ha proof (CPB) · APSOC rispettata · pricing one-time corretto · zero AI-slop · zero dependency-language · brand_kit dichiarato | Blocco non derogabile. Solo LX sblocca. Vale anche per il Board (Art.2.2) |
| **G3 — Compliance** (solo ads/email) | AD4 / E2 / AD-QA / E-QA | Policy piattaforma OK · spam score OK · PII gestita (`aidefence_has_pii` obbligatorio su liste email — Art.7.2) | Blocco fino a fix; escalation a MND-ENFORCEMENT se violazione Art.7 |
| **G4 — Contract check** | MKT-Conductor | La risposta soddisfa gli `acceptance_criteria` del contratto del committente | Rework specifico o rinegoziazione contratto; log in `marketing/handoffs/log` |
| **G5 — Brand consistency** (solo multi-tenant) | BR-QA | Output coerente con brand_kit del cliente (non solo con Mandato DE) | Block + richiesta brief corretto al committente |

### 7.2 KPI (da misurare — nessuna baseline storica esiste: si stabilisce in M1-M2, niente numeri inventati)

| KPI | Reparto | Definizione |
|---|---|---|
| First-pass rate G1 | L2.1 | % copy che passa A8 ≥80 alla prima iterazione (tracciato da COPY-QA-LEAD) |
| Time-to-copy per formato | L2.1 | Dalla richiesta valida alla consegna gated (target indicativi dai workflow esistenti: ad ~15-20 min, sales page ~90-120 min) |
| Handoff acceptance rate | L1 | % consegne accettate dal committente senza rework (tracciato da MKT-Conductor) |
| CTR / CPC / CPA per campagna | L2.2 | Per piattaforma; confronto variante vs variante, mai vs benchmark esterni (niente numeri inventati) |
| Open / click / reply rate | L2.3 | Per sequenza e segmento ICP; baseline da misurare al primo run reale |
| Esperimenti chiusi con verdetto / mese | L2.4 | Velocità di apprendimento del loop §4b |
| Pattern ICP consolidati | L2.4 | Conteggio record validati in `marketing/copy/patterns/*` (crescita = il sistema impara) |
| Brand consistency score | L2.5 | % output che passano G5 al primo tentativo (per cliente/brand_kit) |
| Funnel conversion rate per stage | L2.6 | Drop rate per sezione APSOC nel funnel (da AN5); baseline da primo funnel live |
| Costo per run di copy | trasversale | Cost-attribution per agente (Cost-Sentinel, pattern #9); multi-tenant: per brand_kit |
| Gate bypass rate | trasversale | KPI di qualità del Backbone: deve restare 0 (Art.4.1 Mandato) |

---

## 8. Integrazione Ruflo (TopologyOrchestration)

**Topologia:** `hierarchical` (default holding) — MKT-Conductor coordinatore di ecosistema;
COPY-MASTER coordinatore L2.1; lead di reparto (ADS-LEAD, EMAIL-LEAD, AN-LEAD, BRAND-LEAD,
CONV-LEAD) coordinatori L2. Fan-out `mesh` SOLO dentro batch paralleli (varianti ads, fan-out
creative, 10 headline). Decisioni cross-reparto (es. budget tra campagne) → escalation a
C-Suite hive-mind (raft), non risolte localmente.

| Funzione | Tool Ruflo | Uso in Marketing |
|---|---|---|
| Spawn pipeline A1→A8 | `agent_spawn` sequenziale | Ogni agente riceve output del precedente come input (handoff interno) |
| Fan-out varianti | `swarm_init` + `task_orchestrate` | 3+ varianti ad / 10 headline / batch creative in parallelo |
| Pattern pre-scrittura | `memory_search` | COPY-MASTER interroga pattern ICP PRIMA di scrivere |
| Salvataggio esiti | `memory_store` + hooks post-task | Score, pattern, anti-pattern dopo ogni run |
| Apprendimento | ReasoningBank + `neural_train` | Loop §4b, distillazione fallimenti/successi |
| Sicurezza input | `aidefence_scan` / `aidefence_has_pii` | Briefing e liste email (PII!) prima dell'elaborazione (Art.7.2) |
| State per workflow | state.json per esecuzione | Ogni workflow CF-grade produce record ripartibile a freddo (test amnesia §6 piano V2) |

---

## 9. Namespace memoria — `marketing/...` (AgentDB/HNSW)

| Namespace | Contenuto | Owner |
|---|---|---|
| `marketing/copy/patterns/{icp}` | Pattern copy vincenti per ICP (hook, angoli, CPB che hanno performato) — cuore del vantaggio cumulativo | AN4 scrive, COPY-MASTER legge |
| `marketing/copy/antipatterns/{icp}` | Cosa NON funziona per quell'ICP (da ReasoningBank) | AN4 scrive |
| `marketing/copy/scores` | Storico score APSOC per copy_id (trend qualità) | A8 / COPY-QA-LEAD scrivono |
| `marketing/avatars/{icp}` | Avatar completi prodotti da A2/T-AVATAR (riuso cross-ecosistema) | A2 scrive |
| `marketing/ads/experiments` | Matrici test, varianti, verdetti | AN3 / AD6 scrivono |
| `marketing/email/sequences` | Sequenze validate riusabili (per brand_kit) | E1/E-LEAD scrivono |
| `marketing/brand/kits/{brand_kit_id}` | Brand kit per cliente/canale (voce, visual brief, ICP, tone chart) | BRAND-LEAD scrive |
| `marketing/brand/audit` | Audit brand positioning per cliente | BR4 scrive |
| `marketing/cro/sprints` | Sprint CRO: collo di bottiglia, variante, risultato | CA4 scrive |
| `marketing/cro/audits` | Audit landing: diagnosi + 3 azioni prioritarie | CA-QA / AN5 scrivono |
| `marketing/handoffs/log` | Registro richieste/risposte cross-ecosistema | MKT-Conductor scrive |

**Wiki-first (pattern #12 Piano Maestro, Art.5.2 Mandato):** i pattern consolidati con
evidenza forte vengono ANCHE scritti in pagine wiki (`concepts/` o `synthesis/`) + entry
`wiki/log.md`. AgentDB resta l'indice semantico operativo per gli agenti. In conflitto
wiki ↔ AgentDB: **vince la wiki**; AgentDB si reindicizza.

---

## 10. Build plan v2 (dentro V2-2, poi V2-6 per la build strutturale completa)

### Sequenza milestone (ordine non negoziabile: Copywriting prima di tutto il resto)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **M1 — Scaffolding + motore** | Cartella `company/Ecosistemi/04-MARKETING/` v2 (Reparti L2.5/L2.6 documentati); wrapper handoff sopra `/copywriting`; lead di reparto aggiunti alle schede esistenti; skill `empire-brand-gate` + `copy-request-router` + `brand-strategy-gate` (P0) forgiate; contradiction-analyzer su suite market-* | Una richiesta col contratto §1.2 attraversa il motore e esce gated (G1+G2); lead di reparto risponde del risultato |
| **M2 — Primo handoff reale + brand** | Integrazione BUS con 01-AGENCY: copy reale per outreach/preventivo; baseline KPI; primo brand_kit cliente; WF-BRAND-KIT-BUILD eseguito | Il committente accetta la consegna (G4 verde) senza intervento manuale nel routing; brand kit in namespace |
| **M3 — Email Lifecycle live** | Team E4/E5/E-QA; WF-EMAIL-LAUNCH + ONBOARDING + WINBACK; primo handoff da 02-INFO-BUSINESS (sequenza lancio) | Una sequenza completa gated e consegnata; E2 deliverability check verde |
| **M4 — Advertising live** | Team ADS-LEAD/AD5/AD6/AD-QA; WF-ADS-CAMPAIGN in dry-run con matrice creativa; skill `ads-compliance`; BR3 → 03-CF handoff creative | Campagna completa pronta al lancio in dry-run; lancio reale SOLO con ok umano su spesa (Art.4.3) |
| **M5 — Conversion Architecture live** | Team CONV-LEAD/CA1-CA4/CA-QA; WF-FUNNEL-DESIGN per committente pilota; skill `conversion-funnel-designer`; handoff a 06-PLATFORM | Funnel completo con copy gated per ogni stage; brief tecnico approvato da 06-PLATFORM |
| **M6 — Analytics + loop + auto-miglioramento** | Team AN-LEAD/AN5/AN-OBSERVER; WF-TRACKING-SETUP; skill `copy-performance-loop` + `icp-pattern-library`; primi pattern in `marketing/copy/patterns/*` | Un ciclo completo §4b eseguito su copy reale (dato → pattern → revisione → test); DONE WHEN §0 tutti verdi |

---

## 11. Pre-mortem — rischi v2 (amplia §10 del v1)

| Rischio | Probabilità | Mitigazione |
|---|---|---|
| **Riscrittura accidentale del Copy Workflow** durante l'integrazione | Alta | ADR-003 ferma: migrazione = wrapper + registrazione, mai modifica ai file del motore; file in `Copy-Workflow-manuale/` restano fonte di verità finché il wrapper non è validato (M1) |
| **Doppio standard di copy** (suite market-* vs Copy Workflow vs cro-copy-architect) | Alta | contradiction-analyzer in M1; gerarchia esplicita: Copy Workflow = motore, cro-copy-architect = knowledge Guild, market-* = ausiliarie; in conflitto vince il motore |
| **Reparti L2.5/L2.6 senza committenti immediati** (nuovi, non urgenti) | Media | Non bloccano M1-M4; build parallela in M2-M3; ogni reparto ha almeno un handoff reale entro M5 |
| **AI-slop**: copy generico che passa il score ma non converte | Media | G2 include check anti-slop (Art.2.3 Mandato: keyword hard-coded nicchia, regole Barnum/Rainbow); il loop §4b corregge sulla realtà, non sullo score |
| **Loop ottimizzazione senza dati** (volumi bassi → verdetti rumorosi) | Alta nelle fasi iniziali | AN3 dimensiona i test prima di lanciarli; sotto soglia il verdetto è "inconclusivo", mai forzato; pattern si consolidano solo con evidenza ripetuta |
| **Spesa ads non autorizzata** | Bassa (vincolo esplicito) | Dry-run di default (Art.4.3); AD3 non può lanciare senza ok umano esplicito; Cost-Sentinel budget guard |
| **Collo di bottiglia**: tutti gli ecosistemi in coda su un solo motore copy | Media | Priorità nel contratto via `deadline`; fan-out swarm sui formati brevi; escalation a C-Suite se due committenti confliggono |
| **Drift della brand voice** su output multi-tenant (clienti agency con voce diversa) | Media | `brand_kit` esplicito nel contratto; G2 valida contro brand_kit dichiarato (Mandato DE di default); Brand-Voice Sentinel logga ogni override; G5 verifica coerenza per brand cliente |
| **Schede agenti v2 non millimetriche** (il rischio che denunciava Max: "semplici file markdown") | Alta senza presidio | Standard §0 piano V2 obbligatorio per ogni agente nuovo; COPY-QA-LEAD + AN-OBSERVER tracciano che ogni scheda abbia I/O JSON, logica passo-passo, KPI, escalation |
| **L2.5/L2.6 duplicano funzioni di L2.1** | Media | Confini espliciti: L2.5 = strategia/identità (non scrive copy), L2.6 = architettura funnel (non scrive copy); il copy viene SEMPRE da L2.1 |
| **PII nelle liste email** | Media | `aidefence_has_pii` obbligatorio prima di ogni elaborazione lista; E2 owner della policy (Art.7.2) |

---

## 12. Connessioni

- [[11-PIANO-V2-DIRETTIVA-SCALA]] §0-2 — direttiva suprema che governa questo dossier (ADR-007)
- [[04-ECOSISTEMA-MARKETING]] — il v1 da cui si parte; resta riferimento per il motore copy
- [[12-DOSSIER-MAXIMILIAN]] — revisione 5-bis da V2-3: "Max approverebbe questo ecosistema?"
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] — enforcement legge; Brand-Voice Sentinel risponde a LX
- [[00-PIANO-MAESTRO]] — gerarchia LX→L5, backbone, pattern non negoziabili
- `company/Mandato/MANDATO-EMPIRE.md` — Art.2 (Brand Voice) e Art.4 (gate) sono i vincoli operativi di questo ecosistema
- [[Tool_Copy_Workflow_Orchestration]] — il motore del reparto L2.1 (wiki BRAIN)
- [[Framework_Cold_Outreach_APSOC]] — standard APSOC+V, Barnum, 5 pilastri, follow-up (wiki BRAIN)
- [[01-ECOSISTEMA-AGENCY]] — primo committente (M2); cold outreach operativo vive lì
- [[02-ECOSISTEMA-INFOBUSINESS]] — committente lanci (M3); sales page + VSL + email lancio
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — fornitore visual/creative; committente hook/headline
- [[06-ECOSISTEMA-PLATFORM]] — implementa landing progettate da L2.6; tracking in coordinamento con AN1
- [[07-BACKBONE-RUFLO-SKILLS]] — registro skill e integrazione Ruflo; tutte le skill §5 registrate qui
- [[08-ECOSISTEMA-INTELLIGENCE]] — fornitore ICP data, competitor data, trend; input per A2/BR4/S2
- `company/Ecosistemi/04-MARKETING/` — cartella struttura esistente (Agenti, Reparti, Workflow, Funzioni)
- ADR-003 (wrap, non riscrittura) · ADR-007 (V2, CF-grade) · ADR-005 (minuzie → BACKLOG) · ADR-002 (memory-first)
