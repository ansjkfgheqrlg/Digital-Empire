# 📚 02 — ECOSISTEMA INFO-BUSINESS (Lanci & Prodotti Informativi)

> Dossier L1 di EMPIRE OS — Digital Empire Group. Dipende da `00-PIANO-MAESTRO.md`
> (gerarchia LX→L5, Corporate Backbone, 13 pattern non negoziabili, Ruflo).
> Versione: 1.0 · Creato: 2026-06-10 · Fase roadmap di riferimento: **F6** (primo lancio assistito).

---

## 0. Missione + DONE WHEN

**Missione:** trasformare l'Info-Business di DE da *lanci episodici e manuali* a una
**macchina industriale di produzione e lancio di prodotti informativi**: ogni corso, ebook,
webinar e community nasce da materiale raw già posseduto, passa gate di qualità misurabili,
viene lanciato con un calendario orchestrato da agenti e poi venduto in evergreen — alimentando
con lead caldi l'ecosistema AGENCY (stesso posizionamento AI/automazione).

**DONE WHEN (misurabili):**

| # | Criterio | Verifica |
|---|---|---|
| 1 | Catalogo prodotti formalizzato: ogni prodotto attivo ha prezzo deciso, target, promessa, funnel assegnato (oggi "Manuale Claude Code" ha prezzo = "NON LO SO" → inaccettabile) | `InfoBusiness/CATALOGO` senza campi vuoti |
| 2 | WF-CORSO produce un corso completo: da cartella raw → MKD → curriculum → lezioni → piattaforma Supabase, senza intervento manuale tranne i gate | corso "Vendi la Skill n.1" caricato in piattaforma |
| 3 | WF-LANCIO esegue un lancio end-to-end con calendario T-30→T+7, copy gate APSOC ≥80/100, dry-run completo prima del go | primo lancio orchestrato (gate F6 del Piano Maestro) |
| 4 | Funnel evergreen attivo: lead magnet → sequenza email → sales page → checkout, con tracking eventi funzionante | percorso cliccabile end-to-end + eventi in analytics |
| 5 | Ogni acquirente entra in onboarding automatico ≤24h; i lead qualificati passano ad AGENCY via handoff contract | handoff `infobusiness→agency` testato |
| 6 | Debrief post-lancio scritto in ReasoningBank; zero asset Info-Business orfani (tabella §5 completa) | entry ReasoningBank + inventario 100% |

**OUT OF SCOPE (ora):** ads a pagamento senza ok esplicito; pubblicazione automatica di email/post
senza review umana nei primi 2 lanci; affiliazioni; prodotti high-ticket con sales call (fase successiva).

---

## 1. Posizione nella holding — handoff espliciti

INFO-BUSINESS è ecosistema **revenue** (come AGENCY) ma è anche il **moltiplicatore di autorità**:
ogni prodotto info rafforza il posizionamento "implementazioni AI" e prepara il cross-sell agency.

### 1.1 Handoff in INGRESSO

| Da | A | Payload | Acceptance criteria |
|---|---|---|---|
| **CONTENT-FACTORY** → INFO-BUSINESS | Reparto Prodotto | Moduli video corso (script approvato → video montato), caroselli/reel pre-lancio, thumbnail | formato/durata da brief; brand voice gate passato |
| **MARKETING** → INFO-BUSINESS | Reparto Lanci | Sequenze email lancio (pre-lancio, cart open, cart close), copy sales page, ad copy | APSOC ≥80/100; CTA univoca; zero claim non provabili |
| **INTELLIGENCE** → INFO-BUSINESS | Reparto Prodotto + Lanci | Customer research, trend, ingest fonti (es. Thought Leader Funnel / Founder Authority Stack dal video Beggiato), pattern da ReasoningBank | atomi archiviati in wiki + namespace memoria |
| **PLATFORM** → INFO-BUSINESS | Reparto Prodotto | Piattaforma corso (Supabase + Next.js), checkout, paywall tecnico, fix | deploy verde + smoke test studente |
| **FORGE** → INFO-BUSINESS | Tutti i reparti | Nuovi agenti/skill su richiesta (es. skill `course-architect`) | skill passa skill-creator eval |

### 1.2 Handoff in USCITA

| Da | A | Payload | Acceptance criteria |
|---|---|---|---|
| INFO-BUSINESS → **AGENCY** | Reparto Acquisizione AGENCY | **Lead caldi cross-sell**: acquirenti corso/ebook che segnalano bisogno di implementazione fatta-per-loro (segnali: domande in community, completamento moduli avanzati, richieste dirette) | `{lead, fonte_prodotto, segnale, score}`; lead consenziente |
| INFO-BUSINESS → **CONTENT-FACTORY** | Reparto Strategia CF | Brief contenuti pre-lancio (angoli, hook, calendario), estratti corso riusabili come contenuto organico | brief con ICP + obiettivo per pezzo |
| INFO-BUSINESS → **MULTI-BUSINESS** | Publishing/KDP | Contenuto corso/ebook riconfezionabile per KDP (multi-tenant by design) | diritti/formato verificati |
| INFO-BUSINESS → **OPERATIONS** | Cost guard | Stima costi lancio (dry-run), scheduling sequenze | budget approvato prima del go |

**Formato handoff (pattern #2 del Piano Maestro):**

```json
{
  "from": "infobusiness/lanci",
  "to": "marketing/copywriting",
  "payload": { "tipo": "sequenza_email_cart_open", "prodotto": "corso-skill-beast", "icp": "...", "offer_stack": "..." },
  "acceptance_criteria": ["APSOC >= 80/100", "5 email", "1 CTA per email", "zero promesse di guadagno non provate"],
  "deadline": "T-7",
  "fallback": "escalation a ib-lanci-coordinator"
}
```

---

## 2. Reparti L2

Quattro reparti. Ogni team (L3 workflow, L4 funzione) segue lo schema canonico:
coordinator + workers, I/O espliciti, acceptance criteria, failure handling, shared_state.

### 2.1 L2-PRODOTTO — "dalla materia prima al prodotto vendibile"

- **Missione:** trasformare materiale raw (registrazioni, PDF, manuali, transcript in `Formazzione/`)
  in prodotti finiti: ebook, corsi su piattaforma, guide, webinar. Nessun prodotto si crea senza
  validazione idea (score ≥60/100 dal Product Idea Backlog, già definito in `processo lancio.txt`).
- **Team L3 (workflow):**
  - `WF-CORSO` — produzione corso end-to-end (dettaglio §4a)
  - `WF-EBOOK` — raw → MKD → ebook impaginato → sales asset (il Manuale Claude Code 203pp è il prototipo)
  - `WF-VALIDAZIONE` — idea → scoring 5 criteri /100 → test MVP 7 giorni → brief validato (gate d'ingresso di tutto il reparto)
- **Team L4 (funzioni):**
  - `T-mkd` — esegue content-forge: raw → Master Knowledge Document
  - `T-curriculum` — MKD → struttura moduli/lezioni con obiettivi di apprendimento misurabili
  - `T-piattaforma` — caricamento su Supabase+Next.js (riusa gli agenti `formazione-*` esistenti)
  - `T-design-prodotto` — copertine, slide, workbook (handoff a CONTENT-FACTORY per i video)

### 2.2 L2-LANCI — "il regista del cart open"

- **Missione:** orchestrare ogni lancio come operazione militare a calendario: pre-lancio, cart open,
  cart close, post-lancio. Un lancio = un workflow con dry-run obbligatorio e go/no-go formale.
- **Team L3:**
  - `WF-LANCIO` — lancio completo orchestrato (dettaglio §4b)
  - `WF-WEBINAR` — webinar di vendita: script (asset `InfoBusiness/Webinar/` come base), registrazione/live, replay funnel
- **Team L4:**
  - `T-calendario` — timeline T-30→T+7, dipendenze, owner per task
  - `T-copy-liaison` — compone gli handoff verso MARKETING e verifica i rientri contro acceptance criteria
  - `T-asset-lancio` — checklist asset (sales page, email, creatives, checkout) tutti pronti prima del gate
  - `T-debrief` — post-mortem strutturato → ReasoningBank (pattern #5)

### 2.3 L2-VENDITE/FUNNEL — "il motore che vende anche quando il lancio è chiuso"

- **Missione:** costruire e ottimizzare l'infrastruttura di vendita: offer stack, pricing, sales page,
  checkout, paywall, e il funnel evergreen che gira 365 giorni (Funnel Unico Perfetto + Thought Leader
  Funnel come modelli di riferimento).
- **Team L3:**
  - `WF-FUNNEL-EVERGREEN` — lead magnet → nurture → conversione (dettaglio §4c)
  - `WF-SALESPAGE` — brief → copy APSOC → build in stile empire-premium → QA → deploy
- **Team L4:**
  - `T-offer` — value stack, bonus, garanzia, order bump, upsell (skill `pricing` + `paywalls`)
  - `T-checkout` — pagina pagamento, recupero carrelli, ricevute (con PLATFORM)
  - `T-cro-funnel` — test A/B su step del funnel (skill `ab-testing`, `cro`)
  - `T-tracking` — eventi, UTM, attribution (skill `analytics`)

### 2.4 L2-COMMUNITY & RETENTION — "il prodotto inizia dopo l'acquisto"

- **Missione:** onboarding studenti, community attiva (WhatsApp/Discord previsto dal catalogo),
  completamento corsi, testimonianze, referral, e identificazione lead caldi per AGENCY.
- **Team L3:**
  - `WF-ONBOARDING-STUDENTE` — acquisto → accesso ≤24h → primo modulo completato ≤7gg
  - `WF-COMMUNITY` — programmazione contenuti community, moderazione, rituali settimanali
- **Team L4:**
  - `T-onboarding` — sequenza benvenuto + attivazione (skill `onboarding`, `signup`)
  - `T-retention` — segnali di abbandono, win-back (skill `churn-prevention`)
  - `T-social-proof` — raccolta testimonianze/case study a milestone di completamento
  - `T-crosssell` — scoring segnali "vuole l'implementazione fatta" → handoff AGENCY (skill `referrals` per il lato studenti)

---

## 3. Roster agenti L5

Convenzione: prefisso `ib-`. Gli agenti `formazione-*` esistono già in `~/.claude/agents/` e vengono
**arruolati così come sono** (migrazione = mappatura, non riscrittura). Tier = 3-tier routing Ruflo.

| ID | Ruolo | Tipo | Tier modello |
|---|---|---|---|
| `ib-conductor` | Direttore ecosistema: riceve obiettivi dal Board, smista ai reparti, riporta KPI | coordinator (L1) | Opus |
| `ib-prodotto-coordinator` | Coordina WF-CORSO / WF-EBOOK / WF-VALIDAZIONE | coordinator | Sonnet |
| `ib-validator` | Product Idea Backlog: scoring /100, test MVP, brief validato | worker | Sonnet |
| `ib-mkd-forger` | Esegue content-forge su materiale raw → MKD | worker | Sonnet |
| `ib-curriculum-architect` | MKD → struttura moduli, obiettivi, prerequisiti, esercizi | worker | Sonnet |
| `ib-lesson-writer` | Scrive script lezioni/capitoli dal curriculum | worker | Sonnet |
| `formazione-orchestrator` | Coordina la piattaforma corso (esistente) | coordinator (T-piattaforma) | Sonnet |
| `formazione-database` | Schema/dati corso su Supabase (esistente) | worker | Sonnet |
| `formazione-admin` | Pannello admin, gestione iscritti (esistente) | worker | Haiku |
| `formazione-student` | Esperienza studente, progress tracking (esistente) | worker | Haiku |
| `formazione-design` | UI piattaforma e asset visivi (esistente) | worker | Sonnet |
| `ib-lanci-coordinator` | Regista lancio: calendario, gate, go/no-go | coordinator | Opus (solo durante lancio) |
| `ib-launch-planner` | Costruisce timeline T-30→T+7 con dipendenze | worker | Sonnet |
| `ib-copy-liaison` | Prepara handoff a MARKETING, valida i rientri vs APSOC ≥80 | worker | Haiku |
| `ib-webinar-producer` | Script + struttura webinar di vendita + replay funnel | worker | Sonnet |
| `ib-debriefer` | Post-mortem lancio → ReasoningBank | worker | Sonnet |
| `ib-funnel-coordinator` | Coordina funnel evergreen + sales asset | coordinator | Sonnet |
| `ib-offer-architect` | Offer stack, pricing, garanzie, bump/upsell | worker | Sonnet |
| `ib-salespage-builder` | Sales page: copy APSOC + build empire-premium-style | worker | Sonnet |
| `ib-checkout-tech` | Checkout, paywall, recupero carrelli (con PLATFORM) | worker | Haiku |
| `ib-tracking-analyst` | Eventi, UTM, report conversioni per step | worker | Haiku |
| `ib-community-coordinator` | Coordina onboarding, community, retention | coordinator | Sonnet |
| `ib-onboarder` | Sequenza benvenuto + attivazione studente | worker | Haiku |
| `ib-engagement-runner` | Rituali community, prompt discussione, moderazione | worker | Haiku |
| `ib-testimonial-harvester` | Raccolta testimonianze a milestone | worker | Haiku |
| `ib-crosssell-scout` | Scoring lead caldi → handoff contract verso AGENCY | worker | Sonnet |

Totale: **26 agenti** (5 esistenti riusati, 21 da creare via FORGE). Sentinels (Cost, Quality,
Brand-Voice) e Guilds (Copy/APSOC, Quality) sono trasversali: NON duplicati qui.

---

## 4. Workflow chiave end-to-end

### 4a. WF-CORSO — produzione corso da materiale raw

```
INPUT: cartella raw (es. Formazzione/Claude code/) + brief validato (score ≥60 da WF-VALIDAZIONE)
─────────────────────────────────────────────────────────────────────────────
1. ib-mkd-forger        → content-forge sull'intera cartella → MKD (Master Knowledge Document)
   GATE: MKD copre il 100% degli atomi informativi della fonte (zero perdita)
2. ib-curriculum-architect → MKD → curriculum: moduli, lezioni, obiettivi misurabili, esercizi
   GATE: ogni lezione ha 1 outcome verificabile; durata totale dichiarata
3. ib-lesson-writer     → script lezione per lezione (testo per ebook, script video per corso)
   GATE: brand voice gate (Mandato Empire) + zero contenuto generico
4. HANDOFF → CONTENT-FACTORY: script video → moduli video montati (acceptance: durata, formato, qualità audio)
5. formazione-orchestrator → carica su piattaforma: formazione-database (schema/contenuti),
   formazione-admin (accessi), formazione-design (UI), formazione-student (percorso)
   GATE: smoke test "studente fantasma" completa modulo 1 end-to-end
6. T-design-prodotto    → copertina, workbook, certificato
OUTPUT: corso live su piattaforma + asset vendita preliminari → handoff a L2-VENDITE
```

### 4b. WF-LANCIO — lancio completo orchestrato

```
INPUT: prodotto che ha passato il gate qualità prodotto (§8) + budget approvato da OPERATIONS
─────────────────────────────────────────────────────────────────────────────
PRE-LANCIO (T-30 → T-1)
  T-30  ib-launch-planner: calendario completo + dipendenze + owner
  T-28  HANDOFF → INTELLIGENCE: customer research / angoli (Thought Leader Funnel come frame)
  T-21  HANDOFF → CONTENT-FACTORY: contenuti organici pre-lancio (calendario brief per pezzo)
  T-14  HANDOFF → MARKETING: sales page + sequenza pre-lancio  [GATE: APSOC ≥80/100]
  T-7   ib-copy-liaison: tutte le email cart open/close rientrate e validate
  T-3   T-asset-lancio: checklist 100% (page live, checkout testato, tracking attivo)
  T-1   DRY-RUN completo (pattern #3): simulazione invii + stima costi → Cost-Sentinel
  T-0-ε GO/NO-GO: hive-mind consensus (ib-conductor + Quality + Brand-Voice + Cost Sentinel)
CART OPEN (T0 → T+4/6)
  T0    apertura: email 1 + post + webinar (se previsto da WF-WEBINAR)
  T+1..n  sequenza cart open: obiezioni (1 email = 1 obiezione, da APSOC), social proof, FAQ
  ogni 24h: ib-tracking-analyst riporta conversioni per step → micro-aggiustamenti (solo copy, non offerta)
CART CLOSE (ultime 48h)
  scarcity REALE (deadline/bonus a scadenza — mai finta: Mandato Empire), email close x3, chiusura checkout
POST (T+1 → T+7)
  onboarding acquirenti ≤24h (WF-ONBOARDING-STUDENTE) · ib-debriefer: numeri reali vs piano,
  cosa rifare/evitare → ReasoningBank · ib-crosssell-scout: primi segnali cross-sell → AGENCY
OUTPUT: lancio chiuso + debrief + coorte studenti in onboarding
```

### 4c. WF-FUNNEL-EVERGREEN — vendita continua

```
INPUT: prodotto lanciato almeno una volta (il lancio valida l'offerta, l'evergreen la scala)
─────────────────────────────────────────────────────────────────────────────
1. Lead magnet: ebook Manuale Claude Code GRATUITO (già designato nel catalogo come lead magnet
   del corso) oppure asset da skill lead-magnets → opt-in page
2. Sequenza nurture (skill emails + frame Founder Authority Stack): valore → autorità → offerta
3. Sales page evergreen (variante della page di lancio, senza deadline finte)
4. Checkout + order bump + upsell (T-offer) → acquisto
5. Acquirente → WF-ONBOARDING-STUDENTE → community → T-crosssell (lead caldi → AGENCY)
6. Loop: ib-tracking-analyst misura ogni step → T-cro-funnel propone 1 test A/B alla volta
OUTPUT: revenue continua + pipeline lead per AGENCY senza dipendere dai lanci
```

---

## 5. Asset esistenti → reparto

| Path (relativo a `Digital Empire/`) | Reparto | Azione |
|---|---|---|
| `Formazzione/Claude code/MANUALE COMPLETO DI CLAUDE CODE PER IL BUSINESS.md/.pdf` | PRODOTTO | È il prodotto #1 (ebook 203pp pronto): packaging finale + decisione prezzo (DONE WHEN 1) |
| `Formazzione/Agency Scalping/`, `Outreach/`, `Storytelling/`, `Youtube/` + 2 PDF root | PRODOTTO | Materia prima per WF-VALIDAZIONE → candidati corsi futuri (ingest via content-forge) |
| `InfoBusiness/CATALOGO PRODOTTI ATTUALE — Info-Bu.md` | PRODOTTO | Diventa il registro ufficiale prodotti; colmare i campi vuoti (prezzo, metriche) |
| `InfoBusiness/Funnel Unico Perfetto – ....pdf` | VENDITE/FUNNEL | Ingest → blueprint del WF-FUNNEL-EVERGREEN |
| `InfoBusiness/Webinar/` (3 PDF script/apertura) | LANCI | Base del WF-WEBINAR (template apertura storytelling) |
| `Lancio corso skill beast/processo lancio.txt` | PRODOTTO + LANCI | Contiene Product Creation Lab pipeline + scoring ≥60: diventa il kernel di WF-VALIDAZIONE |
| `Lancio corso skill beast/Framework_ICRO_Digital_Empire.pdf` | VENDITE/FUNNEL | Ingest → riferimento per T-cro-funnel |
| `Lancio corso skill beast/Leanding Page CCM`, `Page`, `Sale pag`, `smerd` | VENDITE/FUNNEL | Audit → consolidare in UNA sales page (WF-SALESPAGE), archiviare i duplicati |
| `Lancio corso skill beast/lezione n.1.mp4`, `content-carousels.html` | PRODOTTO / CONTENT-FACTORY | Lezione pilota → WF-CORSO; caroselli → handoff CF |
| `Lanco ebook/Sito- Leanding page` | VENDITE/FUNNEL | Audit → landing ebook nel funnel evergreen (opt-in o sales page) |
| `~/.claude/agents/formazione-{orchestrator,database,admin,student,design}.md` | PRODOTTO (T-piattaforma) | Arruolati as-is nel roster §3; registrati in IDENTITY-HR |
| Wiki: `Framework_Cold_Outreach_APSOC` + brand voice guide v2.0 | trasversale (gate copy) | Fonte del gate APSOC ≥80 e del brand gate |
| Wiki/knowledge: Thought Leader Funnel + Founder Authority Stack (ingest Beggiato) | LANCI + VENDITE | Frame strategico pre-lancio e nurture evergreen |

**Regola migrazione (dal Piano Maestro):** mappatura + wrapper, mai riscrittura. Niente si cancella
finché il sostituto non è validato.

---

## 6. Skill: esistenti da usare + nuove da creare

### 6.1 Esistenti (già installate) → assegnazione

| Skill | Reparto | Uso |
|---|---|---|
| `content-forge` | PRODOTTO | raw → MKD → corso/skill (cuore di WF-CORSO) |
| `launch` + `market-launch` | LANCI | playbook lancio + orchestrazione marketing del lancio |
| `cro-copy-architect` (APSOC) | LANCI + VENDITE | scrittura e AUDIT di ogni copy a conversione (è il giudice del gate ≥80) |
| `pricing` | VENDITE | decisione prezzo prodotti (DONE WHEN 1) |
| `paywalls` | VENDITE | upgrade path, order bump, upsell |
| `emails` | LANCI + COMMUNITY | sequenze lancio + nurture + win-back |
| `lead-magnets` | VENDITE | creazione lead magnet evergreen |
| `signup` + `onboarding` | COMMUNITY | opt-in flow + attivazione studente |
| `churn-prevention` | COMMUNITY | retention community/abbonamenti |
| `referrals` | COMMUNITY | passaparola studenti |
| `community-marketing` | COMMUNITY | strategia community WhatsApp/Discord |
| `customer-research` + `marketing-psychology` | PRODOTTO + LANCI | ICP, angoli, leve persuasive |
| `ab-testing` + `cro` + `analytics` | VENDITE | test funnel + tracking |
| `empire-premium-style` / `site-*` | VENDITE (con PLATFORM) | build sales page premium |
| `webinar` (parte di `InfoBusiness/Webinar` + skill `video`) | LANCI | produzione webinar |

### 6.2 NUOVE da creare (via FORGE / skill-creator)

| Nome | Scopo | Reparto |
|---|---|---|
| `course-architect` | Standardizza MKD → curriculum (moduli, outcome misurabili, esercizi, durata); kernel ≤500 righe + references | PRODOTTO |
| `launch-runbook` | Il calendario T-30→T+7 come macchina: genera timeline, checklist asset, gate, dry-run, go/no-go | LANCI |
| `offer-stack` | Costruzione offerta: value stack, bonus, garanzia, bump/upsell, naming — separata da `pricing` (che decide il numero) | VENDITE |
| `webinar-funnel` | Script webinar di vendita (apertura storytelling dai PDF esistenti) + replay funnel | LANCI |
| `student-success` | Playbook onboarding+completamento: milestone, nudge, raccolta testimonianze | COMMUNITY |
| `launch-debrief` | Post-mortem strutturato: piano vs reale, root cause, pattern → ReasoningBank | LANCI |
| `crosssell-bridge` | Criteri e scoring per identificare lead caldi corso→agency + handoff contract standard | COMMUNITY |

---

## 7. Integrazione Ruflo

- **Topologia swarm:** `hierarchical` (default Empire) con `ib-conductor` come root.
  Durante un lancio: `swarm_init` dedicato al lancio (scope temporaneo), fan-out sui 4 reparti,
  pipeline sequenziale per WF-CORSO (i gate impongono ordine), `coordination_orchestrate` per il calendario.
- **Decisioni:** GO/NO-GO lancio = `hive-mind propose/vote/consensus` (raft) tra ib-conductor,
  Quality-Sentinel, Brand-Voice-Sentinel, Cost-Sentinel. Un NO di Brand-Voice o Cost blocca.
- **Namespace memoria (`memory_store/search`):**

| Namespace | Contenuto |
|---|---|
| `infobusiness/catalogo` | stato prodotti, prezzi, offer stack correnti |
| `infobusiness/prodotto` | MKD, curriculum, decisioni di prodotto |
| `infobusiness/lanci` | calendari, copy approvati, numeri reali per lancio |
| `infobusiness/funnel` | configurazione evergreen, esiti test A/B |
| `infobusiness/community` | segnali studenti, testimonianze, lead cross-sell |
| `infobusiness/reasoningbank` | pattern distillati dai debrief (errori → regole) |

- **Apprendimento:** dopo ogni lancio `ib-debriefer` scrive in ReasoningBank; `neural_train`
  sui pattern di conversione quando ci saranno ≥3 lanci di dati reali (non prima — niente
  training su dati inventati).
- **Costi:** ogni workflow dichiara dry-run cost prima dell'esecuzione; 3-tier routing come da §3
  (Haiku per funzioni meccaniche, Sonnet default, Opus solo conductor e regia lancio).

---

## 8. KPI per reparto + Quality Gates

### 8.1 KPI (da misurare — nessun valore storico esiste oggi, baseline = primo ciclo)

| Reparto | KPI | Definizione |
|---|---|---|
| PRODOTTO | Lead time corso | giorni da brief validato → corso live su piattaforma |
| PRODOTTO | Tasso validazione | % idee che superano score ≥60 + MVP test |
| LANCI | Aderenza calendario | % task lancio completati entro la data pianificata |
| LANCI | Conversione lancio | % lista email → acquisto durante cart open |
| VENDITE | Conversione evergreen | % visitatori sales page → acquisto; % opt-in lead magnet |
| VENDITE | AOV | valore medio ordine (effetto bump/upsell) |
| COMMUNITY | Attivazione | % acquirenti che completano modulo 1 entro 7gg |
| COMMUNITY | Completamento | % studenti che finiscono il corso |
| COMMUNITY | Cross-sell | n. lead qualificati passati ad AGENCY per coorte |

### 8.2 Quality Gates (bloccanti — pattern #4)

| Gate | Quando | Criterio di passaggio |
|---|---|---|
| **Gate validazione idea** | prima di produrre qualsiasi prodotto | score ≥60/100 + ≥5 "sì, lo comprerei" (MVP test da `processo lancio.txt`) |
| **Gate qualità prodotto** | fine WF-CORSO/WF-EBOOK | 100% atomi fonte coperti; ogni lezione ha outcome verificabile; smoke test studente verde; brand voice conforme |
| **Gate copy lancio APSOC** | ogni copy a conversione (page, email, ad) | audit `cro-copy-architect` **≥80/100**; sotto 80 → rework, non si pubblica |
| **Gate brand (Mandato Empire)** | ogni output esterno | "prove non promesse": zero claim di guadagno non documentati, scarcity solo reale |
| **Gate dry-run + costi** | T-1 di ogni lancio; ogni run evergreen nuova | simulazione completa OK + budget approvato da Cost-Sentinel |
| **Gate go/no-go** | T0 lancio | hive-mind consensus unanime dei Sentinels |
| **Gate handoff cross-sell** | invio lead ad AGENCY | lead consenziente + segnale documentato + score |

---

## 9. Fasi di build (ordinate, con gate)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **B0 — Inventario** | Migrazione asset §5: ogni file mappato al reparto, registro IDENTITY-HR per i 5 agenti formazione-* | zero asset orfani; catalogo prodotti senza campi vuoti tranne metriche |
| **B1 — Prodotto #1 pronto a vendere** | Packaging finale Manuale Claude Code: prezzo deciso (skill `pricing`), offer stack, decisione lead-magnet-gratuito vs prodotto-a-pagamento risolta (oggi il catalogo lo indica in entrambi i ruoli) | gate qualità prodotto verde + prezzo/ruolo deciso e scritto nel catalogo |
| **B2 — Funnel evergreen minimo** | Opt-in page + sequenza nurture + sales page APSOC + checkout + tracking | percorso end-to-end cliccabile; gate copy ≥80; eventi tracciati |
| **B3 — Piattaforma corso integrata** | WF-CORSO completo su "Vendi la Skill n.1": content-forge → curriculum → lezioni → piattaforma (agenti formazione-*) | smoke test studente fantasma verde |
| **B4 — Primo lancio orchestrato** | WF-LANCIO sul corso: calendario T-30→T+7, handoff MARKETING/CF reali, dry-run, go/no-go | **= gate F6 del Piano Maestro**: lancio eseguito con gate tutti verdi |
| **B5 — Community + cross-sell** | Community attiva, onboarding automatico, crosssell-bridge → AGENCY | primo handoff lead infobusiness→agency completato |
| **B6 — Auto-miglioramento** | Debrief → ReasoningBank → aggiornamento skill/workflow via FORGE | entry ReasoningBank + almeno 1 skill arricchita dai dati del lancio |

Ordine vincolante: B1 prima di B2 (non si costruisce un funnel su un prodotto senza prezzo);
B3 prima di B4 (non si lancia un corso che non esiste in piattaforma).

---

## 10. Rischi specifici + mitigazioni

| Rischio | Mitigazione |
|---|---|
| **Prodotto senza decisioni commerciali** (prezzo "NON LO SO", ebook contemporaneamente gratuito e a pagamento) | B1 è bloccante: nessun workflow a valle parte senza catalogo completo; `pricing` + `offer-stack` con decisione scritta e datata |
| **Lancio su lista fredda/inesistente** — il funnel social→community→sale page del catalogo non è ancora costruito | B2 (evergreen + lead magnet) viene PRIMA di B4; il primo lancio dimensiona le attese sulla lista reale, non su numeri ipotetici |
| **Copy hype che brucia il brand** (mercato "guru" saturo di promesse) | doppio gate: APSOC ≥80 + brand gate "prove non provate = bloccato"; scarcity solo reale |
| **Dipendenza dai lanci (revenue a denti di sega)** | WF-FUNNEL-EVERGREEN come reparto dedicato, non ripiego post-lancio |
| **Frammentazione asset** (4+ versioni di landing in `Lancio corso skill beast/`) | B0 consolida: UNA sales page canonica, il resto in archivio; wiki-first come fonte di verità |
| **Piattaforma corso incompleta al momento del lancio** | gate B3 (smoke test studente) obbligatorio prima di aprire il carrello; fallback: delivery via area semplice (link protetti) dichiarato nel dry-run |
| **Cross-sell invadente che rompe la fiducia degli studenti** | gate handoff: solo lead con segnale esplicito e consenso; mai outreach automatico sugli studenti |
| **Costi orchestrazione lancio (Opus + swarm)** | Opus solo per conductor e regia lancio; dry-run con stima costi a T-1; Cost-Sentinel con potere di NO al go/no-go |
| **Conoscenza di lancio che evapora dopo l'evento** | `launch-debrief` obbligatorio entro T+7; pattern in ReasoningBank namespace `infobusiness/reasoningbank` |

---

## Connessioni

- [[00-PIANO-MAESTRO]] — architettura holding, pattern non negoziabili, roadmap F6
- [[04-ECOSISTEMA-MARKETING]] — fornitore copy/email (gate APSOC)
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — fornitore moduli video e contenuti pre-lancio
- [[01-ECOSISTEMA-AGENCY]] — destinatario lead caldi cross-sell
- Wiki: [[Framework_Cold_Outreach_APSOC]] · Thought Leader Funnel / Founder Authority Stack (ingest Beggiato 2026-06-09) · [[Tool_Copy_Workflow_Orchestration]]
