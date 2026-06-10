# 📣 04 — ECOSISTEMA MARKETING (Dossier EMPIRE OS)

> **Ecosistema L1 #04 della holding Digital Empire Group.** Il motore di persuasione
> trasversale: ogni parola che esce da EMPIRE OS con l'obiettivo di generare un'azione
> misurabile passa da qui. **Il Copywriting è la PRIORITÀ ASSOLUTA** di questo ecosistema:
> non si costruisce nulla negli altri reparti finché il reparto Copywriting non è operativo.
> Versione: 1.0 · Creato: 2026-06-10 · Padre: `00-PIANO-MAESTRO.md` · Fase roadmap: F5
> Modello: AION GROUP / Content Factory Exponium (LX→L5, team canonici, handoff contract, QA gate).

---

## 0. Missione + DONE WHEN

**MISSIONE:** trasformare ogni asset di Digital Empire (offerte agency, lanci info-business,
contenuti, listing, video) in copy che converte, secondo il framework **APSOC**
(Attenzione → Problema → Soluzione/Promessa → Obiezioni → CTA) + **CPB** (Claim → Proof → Benefit),
nella brand voice del Mandato Empire: diretta, provocatoria, trasparente, **"prove non promesse"**.

Marketing non possiede prodotti propri: è un **ecosistema di servizio trasversale**.
Il suo prodotto è il copy degli altri 8 ecosistemi — più le campagne (ads, email) e
l'intelligenza di ottimizzazione che ne misura l'effetto.

**DONE WHEN:**
1. Il reparto Copywriting è live con il **Copy Workflow Orchestration Layer inglobato come
   motore** (zero riscrittura) e risponde a richieste cross-ecosistema via handoff contract.
2. Ogni richiesta di copy entra con il contratto `{committente, formato, awareness_level,
   icp, obiettivo, deadline}` e esce SOLO con score A8 ≥80 (≥85 sales page) + brand gate verde.
3. I 4 reparti L2 (Copywriting, Advertising, Email, Analytics) hanno org L3/L4 documentata
   e almeno un workflow L3 eseguito end-to-end ciascuno.
4. Tutte le skill marketing esistenti (cro-copy-architect, market-*, emails, ads, …) sono
   mappate a un reparto: **zero skill orfane**.
5. Il loop di ottimizzazione data-driven è attivo: performance → reasoningbank → revisione
   copy, con pattern vincenti per ICP salvati nei namespace Ruflo dedicati.
6. Almeno 3 ecosistemi committenti (Agency, Info-Business, Content-Factory) hanno ricevuto
   e accettato copy reale prodotto dal sistema.

**OUT OF SCOPE (ora):** spesa ads reale senza ok esplicito dell'utente (vincolo globale
del Piano Maestro); pubblicazione automatica senza review umana nelle prime fasi; SEO
tecnico (→ PLATFORM) e produzione contenuti editoriali (→ CONTENT-FACTORY).

---

## 1. Posizione nella holding — Marketing serve TUTTI

```
                         👑 LX — Mandato Empire (brand voice, APSOC, "prove non promesse")
                          │        + Brand-Voice Sentinel (always-on su ogni output)
                          │
L0  C-Suite ──── CMO ─────┤
                          │
L1  04-MARKETING  ◄────── handoff contract ──────► tutti gli altri ecosistemi
        │
        ├── richiede a: 08-INTELLIGENCE (ricerca ICP, trend), 03-CONTENT-FACTORY (asset visivi
        │   per ads), 06-PLATFORM (landing/tracking), 09-OPERATIONS (runtime swarm, cost guard)
        └── serve: 01, 02, 03, 05 (vedi tabella sotto) + se stessa (marketing di DE)
```

### 1.1 Handoff espliciti — chi chiede cosa a Marketing

| Committente (L1) | Cosa richiede | Formato tipico | Workflow di destinazione |
|---|---|---|---|
| **01 AGENCY** | Copy preventivi/proposte commerciali; copy outreach (email/DM/LinkedIn); copy landing offerte (Outreach Factory, Content Factory, Second Brain, Engine Room) | `proposta`, `cold-email`, `landing` | WF-COPY-REVIEW su output beast-preventivi; standard APSOC+V per outreach |
| **02 INFO-BUSINESS** | Copy lancio completo: sales page, sequenza email lancio, VSL, ads di lancio | `sales-page`, `email-seq`, `vsl`, `ad` | WF-COPY-SALES-PAGE + WF-EMAIL-LAUNCH + WF-ADS-CAMPAIGN |
| **03 CONTENT-FACTORY** | Copy per asset: hook, caption, titoli, script intro, CTA nei contenuti | `social`, `hook`, `headline` | WF-COPY-SOCIAL + T-HEADLINE |
| **05 MULTI-BUSINESS** | Titoli/descrizioni YouTube; copy listing KDP/e-commerce; description app | `yt-meta`, `listing` | T-HEADLINE + WF-COPY-QUICK con pattern industry-specific |
| **04 MARKETING (sé)** | Campagne ads DE, email list DE, ottimizzazione funnel DE | tutti | tutti |

Regola: **nessun ecosistema scrive copy di conversione in autonomia**. Può fare bozze,
ma il gate A8 + brand gate vive qui. (Content-Factory scrive contenuti editoriali in
autonomia; quando un contenuto ha CTA di conversione, la CTA passa dal gate Marketing.)

### 1.2 Contratto di richiesta copy (handoff contract standard)

Ogni richiesta entra nel BUS come messaggio strutturato — campi obbligatori:

```json
{
  "committente": "01-AGENCY | 02-INFO | 03-CF | 05-MB | 04-MKT",
  "formato": "ad | sales-page | email-seq | cold-email | landing | vsl | social | headline | listing | yt-meta | proposta | review",
  "awareness_level": "unaware | problem-aware | solution-aware | product-aware | most-aware",
  "icp": "riferimento ICP/avatar (id namespace o brief inline)",
  "obiettivo": "azione misurabile attesa (es. reply, opt-in, acquisto, click)",
  "deadline": "YYYY-MM-DD"
}
```

Campi opzionali (pattern #11 multi-tenant del Piano Maestro): `brand_kit` (default: Mandato
Empire; override per clienti agency / canali YT / brand KDP), `materiali` (briefing, proof,
case study disponibili), `vincoli` (lunghezza, piattaforma, policy), `acceptance_criteria`
(extra rispetto al gate standard).

**Regole del contratto:**
- Richiesta senza `icp` → il router spawna prima A2 (Target Analyst) o T-AVATAR. Non si scrive copy senza avatar.
- Richiesta senza `awareness_level` → il router lo deduce dal funnel stage e lo dichiara nel payload di risposta (mai implicito).
- La risposta di Marketing è anch'essa un handoff contract: `{copy_finale, score_A8, qa_report, brand_gate: pass/fail, pattern_usati}`.

---

## 2. Reparti L2

```
04-MARKETING (L1) — coordinatore: MKT-Conductor
 ├── L2.1 COPYWRITING                ← PRIORITÀ ASSOLUTA. Motore: Copy Workflow Orchestration Layer
 ├── L2.2 ADVERTISING                ← campagne paid (Meta, Google, LinkedIn, TikTok)
 ├── L2.3 EMAIL MARKETING            ← lifecycle: lancio, nurture, win-back/post-cancel
 └── L2.4 ANALYTICS & OTTIMIZZAZIONE ← tracking, attribution, esperimenti, loop reasoningbank
 ⊕   Copy/APSOC Guild (trasversale, condivisa con tutta la holding)
 ⊕   Brand-Voice Sentinel (always-on, riporta a LX)
```

### L2.1 — COPYWRITING (priorità massima)

**Missione:** produrre ogni copy di conversione della holding via APSOC+CPB, con QA a
100 punti. **Ingloba il Copy Workflow Orchestration Layer esistente come motore: il
sistema NON si riscrive, si monta dentro l'organigramma con un wrapper di handoff.**

| Livello | Team | Contenuto |
|---|---|---|
| Coordinatore L2 | `copy-master` (orchestratore esistente) | Router decisionale: riceve il contratto, sceglie il workflow L3, spawna A1-A8 |
| L3 (workflow) | WF-COPY-FULL | Pipeline completo A1→A8 (motore: `full-copy-workflow.md`) |
| L3 | WF-COPY-AD | Ad copy 3 varianti (motore: `quick-ad-workflow.md`) |
| L3 | WF-COPY-SALES-PAGE | Sales page, gate ≥85 (motore: `sales-page-workflow.md`) |
| L3 | WF-COPY-EMAIL | Sequenze email — eseguito per conto di L2.3 (motore: `email-sequence-workflow.md`) |
| L3 | WF-COPY-VSL | Script VSL 8-20 min (motore: `vsl-workflow.md`) |
| L3 | WF-COPY-SOCIAL | 5 post in sequenza strategica (motore: `social-post-workflow.md`) |
| L4 (funzioni) | T-HEADLINE | headline-forge: 10+ headline con formule |
| L4 | T-OBJECTIONS | objections-forge: CPB per obiezione |
| L4 | T-AVATAR | target-avatar: buyer persona completa |
| L4 | T-FUNNEL | funnel-designer: architettura funnel |
| L4 | T-REVIEW | copy-review: score 100pt su copy esistente |
| L4 | T-APSOC | apsoc-builder: costruzione APSOC interattiva |

Entry point invariato: `/copywriting full|ad|sales-page|email|vsl|social|headline|objections|avatar|funnel|review`.

### L2.2 — ADVERTISING

**Missione:** campagne paid end-to-end (strategia → creative → setup → monitoraggio →
iterazione) su Meta, Google, LinkedIn, TikTok. Il copy delle ads viene SEMPRE da L2.1
(WF-COPY-AD); Advertising possiede targeting, budget, struttura campagna, testing creativo.

| Livello | Team | Contenuto |
|---|---|---|
| L3 | WF-ADS-CAMPAIGN | Campagna end-to-end: brief → strategia (S3) → creative → setup → launch (vedi §4b) |
| L3 | WF-ADS-CREATIVE-TEST | Batch testing creativo: fan-out varianti → matrice test → winner |
| L4 | T-AUDIENCE | Ricerca e definizione audience/segmenti per piattaforma |
| L4 | T-CREATIVE-BATCH | Generazione varianti a scala (skill ad-creative) + brief visual a Content-Factory |
| L4 | T-BUDGET-BID | Allocazione budget, strategia bid, pacing (sotto Cost-Sentinel) |
| L4 | T-AD-COMPLIANCE | Check policy piattaforma (claim sanitari, before/after, ecc.) pre-pubblicazione |

### L2.3 — EMAIL MARKETING

**Missione:** email lifecycle "warm" — lancio, nurture, onboarding, win-back/post-cancel.
**Confine col cold:** il cold outreach operativo (Outreach Workflow, writer.py) resta in
01-AGENCY; Marketing possiede lo **standard APSOC+V** (wiki: Framework_Cold_Outreach_APSOC)
e fa da QA/evoluzione dei template cold via T-REVIEW.

| Livello | Team | Contenuto |
|---|---|---|
| L3 | WF-EMAIL-LAUNCH | Sequenza lancio prodotto (committente tipico: 02-INFO) |
| L3 | WF-EMAIL-NURTURE | Welcome + nurture + re-engagement lista |
| L3 | WF-EMAIL-WINBACK | Post-cancel / churn prevention (skill churn-prevention + emails) |
| L4 | T-SUBJECT | Subject line testing (usa T-HEADLINE come motore) |
| L4 | T-SEGMENT | Segmentazione lista per ICP e awareness level |
| L4 | T-DELIVERABILITY | Igiene lista, warm-up, spam-score, autenticazione dominio |

### L2.4 — ANALYTICS & OTTIMIZZAZIONE

**Missione:** misurare l'effetto di ogni copy/campagna e chiudere il cerchio: i dati
diventano pattern (reasoningbank) e i pattern diventano revisioni di copy. È il reparto
che rende il sistema **auto-migliorante** (pattern #5 del Piano Maestro).

| Livello | Team | Contenuto |
|---|---|---|
| L3 | WF-TRACKING-SETUP | Tracking plan, UTM, eventi, conversion API (skill analytics) |
| L3 | WF-OPTIMIZATION-LOOP | Loop data-driven: performance → diagnosi → reasoningbank → revisione (vedi §4d) |
| L3 | WF-AB-TEST | Disegno ed esecuzione esperimenti (skill ab-testing, ipotesi → varianti → verdetto) |
| L4 | T-ATTRIBUTION | Attribuzione per canale/campagna/copy |
| L4 | T-REPORT | Report periodici per committente (skill market-report / market-report-pdf) |
| L4 | T-INSIGHT-DISTILLER | Distilla i risultati in pattern per ICP → namespace memoria + wiki |

---

## 3. Roster agenti L5

Gli agenti **esistenti** del Copy Workflow entrano nel roster così come sono (file in
`SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/agents/` e `orchestrators/`):
NON si duplicano, si registrano nell'Identity-HR del Backbone con il loro path.

| Codice | Agente | Reparto | Ruolo | Stato |
|---|---|---|---|---|
| MKT-0 | MKT-Conductor | L1 Marketing | Coordinatore ecosistema: riceve handoff dal BUS, smista ai reparti | **NUOVO** |
| — | copy-master | L2.1 | Orchestratore/router del motore copy (coordinatore L2.1) | ESISTENTE (`orchestrators/copy-master.md`) |
| A1 | Briefing Analyst | L2.1 | Raccolta requisiti → briefing-completo.md | ESISTENTE |
| A2 | Target Analyst | L2.1 | Avatar + pain points + language map | ESISTENTE |
| A3 | Attention Writer | L2.1 | Headline + hook (9 strategie) | ESISTENTE |
| A4 | Problem Writer | L2.1 | Problema amplificato (regola: no prodotto) | ESISTENTE |
| A5 | Solution Writer | L2.1 | USP + benefits + post-acquisto | ESISTENTE |
| A6 | Objections Handler | L2.1 | CPB per obiezione (10 tipi) | ESISTENTE |
| A7 | CTA Writer | L2.1 | CTA profondo + urgenza | ESISTENTE |
| A8 | Copy Reviewer | L2.1 | Score APSOC 100pt — **è il QA gate** | ESISTENTE |
| S1 | Funnel Strategist | L2.1 (servizio a tutti) | Architettura funnel multi-step | ESISTENTE (`agents/strategy/`) |
| S2 | Positioning Strategist | L2.1 (servizio a tutti) | Posizionamento, USP, angolo di mercato | ESISTENTE |
| S3 | Campaign Strategist | L2.1 → presta a L2.2 | Strategia campagna multi-canale | ESISTENTE |
| AD1 | Audience Analyst | L2.2 | Ricerca audience, segmenti, lookalike per piattaforma | NUOVO |
| AD2 | Creative Iterator | L2.2 | Varianti creative a scala da winner (skill ad-creative) | NUOVO |
| AD3 | Media Buyer | L2.2 | Struttura campagna, budget, bid, pacing | NUOVO |
| AD4 | Ad Compliance Checker | L2.2 | Policy Meta/Google/LinkedIn/TikTok pre-flight | NUOVO |
| E1 | Lifecycle Architect | L2.3 | Disegno sequenze (trigger, timing, branching) | NUOVO |
| E2 | Deliverability Guard | L2.3 | Spam score, igiene lista, autenticazione | NUOVO |
| E3 | Segmentation Analyst | L2.3 | Segmenti per ICP × awareness × comportamento | NUOVO |
| AN1 | Tracking Engineer | L2.4 | Tracking plan, UTM, eventi (con 06-PLATFORM) | NUOVO |
| AN2 | Attribution Analyst | L2.4 | Attribuzione e lettura performance per copy/canale | NUOVO |
| AN3 | Experiment Designer | L2.4 | Ipotesi, varianti, dimensionamento test | NUOVO |
| AN4 | Insight Distiller | L2.4 | Performance → pattern reasoningbank + wiki | NUOVO |
| SEN-BV | Brand-Voice Sentinel | trasversale (riporta a LX) | Blocca output non conformi al Mandato Empire | NUOVO (pattern Sentinels) |

**Conteggio:** 13 esistenti (copy-master + A1-A8 + S1-S3, già scritti e testati) + 13 nuovi.
I nuovi agenti si creano via 07-FORGE con schema team canonico (coordinator, I/O espliciti,
acceptance criteria, failure handling, shared_state — pattern #1).

---

## 4. Workflow chiave

### (a) Richiesta copy cross-ecosistema — routing per formato

```
[Ecosistema committente]
   │  handoff contract {committente, formato, awareness_level, icp, obiettivo, deadline}
   ▼
MKT-Conductor ──► valida contratto (campi obbligatori? icp esiste in memoria?)
   │                 ├─ icp mancante → spawna A2 / T-AVATAR prima di tutto
   │                 └─ awareness mancante → deduce + dichiara
   ▼
copy-master ──► memory_search("marketing/copy/patterns/{icp}") ← pattern vincenti pregressi
   │
   ▼  ROUTING PER FORMATO
   ├─ ad / yt-meta / listing  → WF-COPY-AD (varianti rapide)
   ├─ sales-page / landing    → WF-COPY-SALES-PAGE (gate ≥85)
   ├─ email-seq               → WF-COPY-EMAIL (in coordinamento con L2.3)
   ├─ cold-email / proposta   → standard APSOC+V / beast-preventivi + T-REVIEW
   ├─ vsl                     → WF-COPY-VSL
   ├─ social / hook / headline→ WF-COPY-SOCIAL / T-HEADLINE
   ├─ review                  → T-REVIEW (score su copy esistente)
   └─ progetto complesso      → WF-COPY-FULL (A1→A8) + S1/S2/S3 se serve strategia
   ▼
A8 Copy Reviewer ──► score <80 (o <85 sales page) → iterazione (max 3, poi escalation a umano)
   ▼
Brand-Voice Sentinel ──► brand gate Mandato Empire (vedi §8) → fail = blocco, non deroga
   ▼
Risposta handoff: {copy_finale, score_A8, qa_report, brand_gate, pattern_usati}
   └─► hooks post-task: memory_store del risultato + entry in wiki/log.md
```

### (b) Campagna ads end-to-end

```
Brief campagna (committente + budget OK esplicito dell'utente — MAI spesa autonoma)
   ▼
S3 Campaign Strategist ── obiettivo, canali, struttura, KPI target
   ▼
AD1 Audience Analyst ── segmenti per piattaforma ──┐
   ▼                                               │ parallelo (swarm fan-out)
WF-COPY-AD (L2.1) ── 3+ varianti copy APSOC ───────┤
   ▼                                               │
handoff a 03-CONTENT-FACTORY ── visual/creative ───┘
   ▼
AD2 Creative Iterator ── matrice copy × visual × audience
   ▼
AD4 Compliance ── policy check → AD3 Media Buyer ── setup campagna (dry-run di default)
   ▼
LAUNCH (previa approvazione umana) → monitoraggio AN2 → dati a WF-OPTIMIZATION-LOOP
   └─ winner → AD2 itera nuove varianti dal winner (loop creativo continuo)
```

### (c) Sequenze email — lancio + nurture + post-cancel

```
LANCIO (committente: 02-INFO-BUSINESS)
  E1 disegna sequenza (es. pre-lancio → apertura → proof → obiezioni → scarcity → chiusura)
  → WF-COPY-EMAIL scrive ogni email (APSOC per email, A6 per le email-obiezione)
  → E3 segmenta lista per awareness → E2 verifica deliverability → gate A8 + brand gate
  → consegna a committente per invio (review umana nelle prime fasi)

NURTURE (lista DE / liste clienti multi-tenant via brand_kit)
  E1 disegna welcome + valore ricorrente → T-SUBJECT genera/testa subject
  → WF-AB-TEST su subject e CTA → AN4 distilla pattern aperture/click per ICP

POST-CANCEL / WIN-BACK (committenti: 02-INFO, 05-MB/SaaS)
  trigger churn → E1 sequenza win-back (skill churn-prevention)
  → A6 Objections Handler centrale: il churn È un'obiezione non gestita
  → exit survey → insight a AN4 → pattern "motivi di churn per ICP" in memoria
```

### (d) Loop ottimizzazione data-driven (il cerchio che si chiude)

```
1. RACCOLTA    AN1/AN2: performance per copy_id (CTR, reply, opt-in, vendite, per canale)
2. DIAGNOSI    AN2 + T-REVIEW: il copy sotto-performa su quale sezione APSOC?
               (hook debole = A, drop a metà = P/S, click senza conversione = O/C)
3. DISTILLA    AN4 Insight Distiller → reasoningbank-* :
               - fallimento → anti-pattern ("ICP dentisti: hook su fatturato = ignorato")
               - successo  → pattern vincente → memory_store in marketing/copy/patterns/{icp}
4. REVISIONE   copy-master riapre il copy SOLO sulla sezione diagnosticata
               (mai riscrittura totale di un copy che performa parzialmente)
5. TEST        WF-AB-TEST: vecchia vs nuova variante → verdetto con criterio predefinito
6. CONSOLIDA   winner → pattern library; wiki/log.md aggiornato; neural_train periodico
   └──────────────────────► torna a 1 (loop continuo)
```

Regola anti-deriva: nessuna revisione di copy basata su opinioni — solo su dati del loop
o su score A8. "Prove non promesse" vale anche internamente.

---

## 5. Asset esistenti → reparto (migrazione = mappatura + wrapper, MAI riscrittura)

| Asset (path) | Reparto | Azione |
|---|---|---|
| `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` (intero sistema: SKILL.md, copy-master, A1-A8, S1-S3, 6 sub-skill, 6 workflow, 4 template, references, evals) | L2.1 Copywriting | **INGLOBA come motore.** Wrapper di handoff sopra `/copywriting`; registrazione agenti in Identity-HR; zero modifiche ai file finché il wrapper non è validato |
| Skill globale `cro-copy-architect` | L2.1 + Copy/APSOC Guild | Knowledge layer condiviso (pattern #6): la usano tutti gli ecosistemi che toccano copy |
| Skill `copywriting`, `copy-workflow` (globali) | L2.1 | Entry point — restano invocabili così come sono |
| Skill `copy-editing` | L2.1 / T-REVIEW | Sub-funzione QA editoriale |
| Skill `marketing-psychology` | Copy/APSOC Guild | Reference trasversale (bias, trigger) per A3-A7 e Advertising |
| Skill `cro` | L2.4 | Ottimizzazione page-level dentro WF-OPTIMIZATION-LOOP |
| Skill `ab-testing` | L2.4 / WF-AB-TEST | Motore disegno esperimenti |
| Skill `analytics` | L2.4 / WF-TRACKING-SETUP | Motore tracking plan |
| Skill `ads` | L2.2 / WF-ADS-CAMPAIGN | Strategia campagna, targeting, bidding |
| Skill `ad-creative` | L2.2 / T-CREATIVE-BATCH | Generazione varianti a scala |
| Skill `emails` | L2.3 | Motore sequenze lifecycle |
| Skill `cold-email` | L2.3 (standard) | Standard di scrittura; esecuzione operativa resta in 01-AGENCY |
| Skill `churn-prevention` | L2.3 / WF-EMAIL-WINBACK | Post-cancel, save offer, dunning |
| Skill `sms`, `popups` | L2.3 (canali secondari) | Adottate quando un committente le richiede |
| Skill `market` (orchestratore suite) | L1 / MKT-Conductor | **Da arbitrare**: si sovrappone a MKT-Conductor → contradiction-analyzer in M1, poi assorbire o ritirare |
| Skill `market-copy`, `market-brand` | L2.1 | Ausiliarie; il motore primario resta il Copy Workflow (no doppio standard) |
| Skill `market-ads` | L2.2 | Ausiliaria di T-CREATIVE-BATCH |
| Skill `market-emails` | L2.3 | Ausiliaria di E1 |
| Skill `market-funnel` | L2.1 / S1 | Ausiliaria del Funnel Strategist |
| Skill `market-audit`, `market-report`, `market-report-pdf` | L2.4 / T-REPORT | Reporting per committente |
| Skill `market-landing`, `market-launch`, `market-proposal`, `market-seo`, `market-social`, `market-competitors` | cross | In prestito a: 06-PLATFORM (landing), 02-INFO (launch), 01-AGENCY (proposal), 03-CF (seo/social), 08-INTEL (competitors) — registrate qui come origine |
| Skill `seo-audit`, `ai-seo`, `schema` | cross (03-CF / 06-PLATFORM) | NON di Marketing: mappate nei dossier 03/06; qui solo consultate da AN per visibilità |
| Skill `marketing-ideas`, `content-strategy`, `customer-research`, `competitor-profiling` | supporto | Input di S2/S3 e A2; ownership primaria in 08-INTELLIGENCE |
| Wiki `concepts/Framework_Cold_Outreach_APSOC.md` | L2.1/L2.3 — BRAIN | Fonte di verità dello standard APSOC+V (Barnum, Inganno Arcobaleno, 5 pilastri, matematica follow-up ~20/40/30%) — referenziata dai team, non duplicata |
| Wiki `tools/Tool_Copy_Workflow_Orchestration.md` | BRAIN | Documentazione del motore — da aggiornare quando il wrapper è live |

---

## 6. Skill esistenti + NUOVE da creare

**Esistenti (riusate, vedi §5):** cro-copy-architect, copywriting, copy-workflow, copy-editing,
cro, emails, cold-email, churn-prevention, ads, ad-creative, ab-testing, analytics,
marketing-psychology, sms, popups, suite market-* (15), beast-preventivi (in prestito da 01).

**NUOVE da creare (via 07-FORGE, pattern #7 progressive disclosure, kernel ≤500 righe):**

| Skill nuova | Reparto | Cosa fa | Priorità |
|---|---|---|---|
| `empire-brand-gate` | LX/Sentinel | Checklist brand gate Mandato Empire eseguibile (vedi §8): voce, "prove non promesse", APSOC compliance, claim pricing corretti | P0 — serve dal giorno 1 |
| `copy-request-router` | MKT-Conductor | Implementa il contratto §1.2 + routing per formato §4a | P0 |
| `copy-performance-loop` | L2.4 | Codifica il loop §4d: diagnosi per sezione APSOC, scrittura pattern in reasoningbank/namespace | P1 |
| `icp-pattern-library` | L2.1/L2.4 | Lettura/scrittura strutturata dei pattern vincenti per ICP (schema record: icp, formato, sezione, pattern, evidenza, data) | P1 |
| `awareness-router` | L2.1 | Adatta struttura APSOC al livello di awareness (unaware → most-aware: dosaggio A/P vs O/C) | P2 |
| `ads-compliance` | L2.2 | Pre-flight policy Meta/Google/LinkedIn/TikTok | P2 |
| `email-lifecycle-architect` | L2.3 | Disegno sequenze con trigger/timing/branching (formalizza E1) | P2 |

Regola anti-contraddizione: prima di creare ogni skill nuova → `skill-contradiction-analyzer`
contro le esistenti (rischio concreto: sovrapposizione con suite market-*).

---

## 7. Integrazione Ruflo

**Topologia:** `hierarchical` (default holding) — MKT-Conductor coordinatore di ecosistema;
copy-master coordinatore L2.1; fan-out swarm `mesh` SOLO dentro i batch paralleli
(varianti ads, fan-out creative §4b). Decisioni cross-reparto contese (es. budget tra
campagne) → escalation a C-Suite hive-mind (raft), non risolte localmente.

| Funzione | Tool Ruflo | Uso in Marketing |
|---|---|---|
| Spawn pipeline A1→A8 | `agent_spawn` sequenziale | Ogni agente riceve l'output del precedente come input (handoff interno) |
| Fan-out varianti | `swarm_init` + `task_orchestrate` | 3+ varianti ad / 10 headline in parallelo |
| Pattern pre-scrittura | `memory_search` | copy-master interroga i pattern ICP PRIMA di scrivere (workflow adattivi, pattern §7 Piano Maestro) |
| Salvataggio esiti | `memory_store` + hooks post-task | Score, pattern, anti-pattern dopo ogni run |
| Apprendimento | `reasoningbank-*`, `neural_train` | Loop §4d, distillazione fallimenti |
| Sicurezza input | `aidefence_scan/has_pii` | Briefing e liste email (PII!) prima dell'elaborazione |

**Namespace memoria (AgentDB/HNSW) — convenzione `marketing/...`:**

| Namespace | Contenuto |
|---|---|
| `marketing/copy/patterns/{icp}` | **Pattern copy vincenti per ICP** (hook, angoli, CPB che hanno performato) — il cuore del vantaggio cumulativo |
| `marketing/copy/antipatterns/{icp}` | Cosa NON funziona per quell'ICP (da reasoningbank) |
| `marketing/copy/scores` | Storico score A8 per copy_id (trend qualità) |
| `marketing/avatars/{icp}` | Avatar completi prodotti da A2/T-AVATAR (riuso cross-ecosistema) |
| `marketing/ads/experiments` | Matrici test, varianti, verdetti |
| `marketing/email/sequences` | Sequenze validate riusabili (per brand_kit) |
| `marketing/handoffs/log` | Registro richieste/risposte cross-ecosistema |

Wiki-first (pattern #12): i pattern consolidati con evidenza forte vengono ANCHE scritti in
pagine wiki (`concepts/` o `synthesis/`) + entry `wiki/log.md`; AgentDB resta l'indice
semantico operativo per gli agenti.

---

## 8. KPI + Quality Gates

### Quality gates (bloccanti, in serie — pattern #4)

| Gate | Chi | Soglia | Esito fail |
|---|---|---|---|
| **G1 — Score APSOC** | A8 Copy Reviewer | ≥80/100 standard · **≥85 sales page** (regola esistente, invariata) | Iterazione mirata (max 3) → escalation umana |
| **G2 — Brand gate Mandato Empire** | Brand-Voice Sentinel (`empire-brand-gate`) | Checklist binaria: voce diretta/provocatoria/trasparente · ogni claim ha una proof ("prove non promesse") · struttura APSOC rispettata (P prima di S, −15 automatico se violato) · pricing one-time/no-canoni mai contraddetto · zero AI-slop (keyword hard-coded nicchia, niente icebreaker generici) | Blocco non derogabile. Solo LX può sbloccare |
| **G3 — Compliance** (solo ads/email) | AD4 / E2 | Policy piattaforma OK · spam score OK · PII gestita | Blocco fino a fix |
| **G4 — Contract check** | MKT-Conductor | La risposta soddisfa gli `acceptance_criteria` del contratto del committente | Rework o rinegoziazione contratto |

### KPI (da misurare — **nessuna baseline storica esiste: si stabilisce in fase M1-M2**, niente numeri inventati)

| KPI | Reparto | Definizione |
|---|---|---|
| First-pass rate G1 | L2.1 | % copy che passa A8 ≥80 alla prima iterazione |
| Time-to-copy per formato | L2.1 | Dalla richiesta valida alla consegna gated (target indicativi dai workflow esistenti: ad 15-20 min, sales page 90-120 min) |
| Handoff acceptance rate | L1 | % consegne accettate dal committente senza rework |
| CTR / CPC / CPA per campagna | L2.2 | Per piattaforma; confronto solo variante-vs-variante, mai vs numeri esterni |
| Open / click / reply rate | L2.3 | Per sequenza e segmento ICP |
| Esperimenti chiusi con verdetto / mese | L2.4 | Velocità di apprendimento del loop §4d |
| Pattern ICP consolidati | L2.4 | Conteggio record validati in `marketing/copy/patterns/*` (crescita = il sistema impara) |
| Costo per run di copy | trasversale | Cost-attribution per agente (Cost-Sentinel, pattern #9) |

---

## 9. Fasi di build ordinate (dentro F5 della roadmap globale)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **M1 — Scaffolding + motore** | Cartella ecosistema in `company/04-marketing/` (L2→L4 documentati); wrapper handoff sopra `/copywriting`; registrazione copy-master + A1-A8 + S1-S3 in Identity-HR; skill `empire-brand-gate` + `copy-request-router` (P0); contradiction-analyzer su suite market-* | Una richiesta col contratto §1.2 attraversa il motore e esce gated (G1+G2) |
| **M2 — Primo handoff reale** | Integrazione BUS con 01-AGENCY: copy reale per outreach/preventivo; baseline KPI iniziale registrata | Il committente accetta la consegna (G4 verde) senza intervento manuale nel routing |
| **M3 — Email Marketing live** | Team E1-E3; WF-EMAIL-LAUNCH + NURTURE + WINBACK; primo handoff da 02-INFO-BUSINESS (sequenza lancio) | Una sequenza completa gated e consegnata |
| **M4 — Advertising live** | Team AD1-AD4; WF-ADS-CAMPAIGN in dry-run (pattern #3) con matrice creativa completa; `ads-compliance` | Campagna completa pronta al lancio in dry-run; lancio reale SOLO con ok umano su spesa |
| **M5 — Analytics + loop** | Team AN1-AN4; WF-TRACKING-SETUP; `copy-performance-loop` + `icp-pattern-library`; primi pattern in `marketing/copy/patterns/*` | Un ciclo completo §4d eseguito su copy reale (dato → pattern → revisione → test) |
| **M6 — Agenti reali + auto-miglioramento** | A1-A8 via `agent_spawn` Ruflo (non solo file-based); Brand-Voice Sentinel always-on; reasoningbank + neural_train attivi; KPI dashboard (con Observability del Backbone) | Loop attivo senza intervento; DONE WHEN §0 tutti verdi |

Vincolo d'ordine non negoziabile: **M1-M2 (Copywriting) prima di tutto il resto.** Advertising
ed Email senza il motore copy gated produrrebbero output non conformi al Mandato.

---

## 10. Rischi + mitigazioni

| Rischio | Mitigazione |
|---|---|
| **Riscrittura accidentale del Copy Workflow** durante l'integrazione (il sistema funziona già) | Regola ferrea: migrazione = wrapper + registrazione, mai modifica ai file del motore; i file in `Copy-Workflow-manuale/` restano fonte di verità finché il wrapper non è validato (M1) |
| **Doppio standard di copy** (suite market-* vs Copy Workflow vs cro-copy-architect che danno indicazioni divergenti) | contradiction-analyzer in M1; gerarchia esplicita: Copy Workflow = motore, cro-copy-architect = knowledge Guild, market-* = ausiliarie; in conflitto vince il motore |
| **AI-slop**: copy generico che passa lo score ma non converte | G2 include check anti-slop (keyword hard-coded nicchia, regole Barnum/Rainbow da Framework_Cold_Outreach_APSOC); il loop §4d corregge sulla realtà, non sullo score |
| **Loop di ottimizzazione senza dati** (volumi bassi → verdetti rumorosi) | AN3 dimensiona i test prima di lanciarli; sotto soglia minima il verdetto è "inconclusivo", mai forzato; i pattern si consolidano solo con evidenza ripetuta |
| **Spesa ads non autorizzata** | Dry-run di default (pattern #3); AD3 non può lanciare senza approvazione umana esplicita; Cost-Sentinel con budget guard (pattern #9) |
| **Collo di bottiglia**: tutti gli ecosistemi in coda su un solo motore copy | Priorità nel contratto via `deadline` + arbitrato MKT-Conductor; fan-out swarm sui formati brevi; escalation a C-Suite se due committenti confliggono |
| **Drift della brand voice** su output multi-tenant (clienti agency con voce diversa) | `brand_kit` esplicito nel contratto: il G2 valida contro il brand kit dichiarato (Mandato Empire di default); Brand-Voice Sentinel logga ogni override |
| **Wiki e AgentDB divergono** sui pattern copy | Pattern consolidati scritti in entrambi (pattern #12) + wiki-syncer di Memory Empire + log obbligatorio |
| **PII nelle liste email** | `aidefence_has_pii` obbligatorio prima di ogni elaborazione lista; E2 owner della policy |

---

## Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia, backbone, pattern non negoziabili
- [[Tool_Copy_Workflow_Orchestration]] — il motore del reparto Copywriting
- [[Framework_Cold_Outreach_APSOC]] — standard APSOC+V, Barnum, 5 pilastri, follow-up
- [[01-ECOSISTEMA-AGENCY]] — primo committente (M2)
- [[02-ECOSISTEMA-INFOBUSINESS]] — committente lanci (M3)
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — fornitore visual / committente hook
- [[07-BACKBONE-RUFLO-SKILLS]] — registro skill e integrazione Ruflo
