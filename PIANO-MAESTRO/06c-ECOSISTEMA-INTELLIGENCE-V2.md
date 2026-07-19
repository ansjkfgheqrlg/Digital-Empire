# 🧠 06c — ECOSISTEMA INTELLIGENCE V2 (Dossier EMPIRE OS)

> Dossier v2 (V2-2, ADR-007) — amplia a scala CF-grade la sezione "08 · INTELLIGENCE"
> del v1 `06-ECOSISTEMI-CORE.md` (righe ~262-378). Fonte: `11-PIANO-V2-DIRETTIVA-SCALA.md` §2.
>
> **Origine di questo file:** il v1 `06-ECOSISTEMI-CORE.md` copriva in un solo dossier i
> 4 ecosistemi core trasversali (PLATFORM · FORGE · INTELLIGENCE · OPERATIONS). In V2-2
> Lotto 3 è stato deciso di SPLITTARLI in 4 dossier V2 indipendenti — uno per ecosistema,
> come già fatto per i business 01-05. Questo file copre **solo INTELLIGENCE**; gli altri
> tre sono [[06a-ECOSISTEMA-PLATFORM-V2]], [[06b-ECOSISTEMA-FORGE-V2]] e
> [[06d-ECOSISTEMA-OPERATIONS-V2]] (quest'ultimo scritto in coppia con questo). La matrice
> di dipendenza tra i 4 core resta quella del v1 (Chiusura, righe ~508-521):
> `INTELLIGENCE → FORGE → PLATFORM`, con `OPERATIONS` trasversale a tutti e tre. Il v1
> resta intatto come riferimento.
>
> **Ecosistema L1 #08 della holding Digital Empire Group.** Metafora OS: *file system + RAM*.
> Versione: 2.0 · Creato: 2026-07-19 · Fase roadmap: V2-2 Lotto 3
> Standard: CF-grade (§0 piano V2 `11-PIANO-V2-DIRETTIVA-SCALA.md`).

---

## 0. Missione + DONE WHEN

**MISSIONE:** essere il cervello della holding — fornire a ogni ecosistema **contesto prima
di agire** e **apprendimento dopo aver agito**. Quattro motori: la wiki `second-brain-vault`
come fonte di verità umana (pattern #12 Piano Maestro), AgentDB/ReasoningBank come memoria
semantica degli agenti, **Empire Studio** come sistema di ingestione (link/video con frame
reali + visione Claude, 9 reparti interni, 50 agenti), **Memory Empire v3** come router +
archivio + enrichment pipeline (5 reparti interni, agenti 7-file).

**VINCOLO CARDINALE (ereditato dal v1, non negoziabile):** Empire Studio e Memory Empire si
inglobano **COSÌ COME SONO** — sono sistemi attivi e testati. INTELLIGENCE li *organizza*
sotto di sé come reparti-wrapper con team di liaison snelli; **non riscrive, non duplica e
non ricostruisce i loro roster interni** (Empire Studio ha già i suoi 9 reparti/50 agenti in
`SKILL & Agenti/Empire Studio Suite/empire-studio/agents/`, verificato su disco: reparti
`conductor`, `forge-wiki-department`, `memory-management-department` e altri; Memory Empire
v3 ha già i suoi 5 reparti in `~/.claude/skills/memory-empire/`). Qualsiasi evoluzione dei
due motori passa per 06b-FORGE con eval prima/dopo, mai per modifica diretta da INTELLIGENCE.
L'espansione v2 reale si concentra sui 3 reparti che nel v1 erano più leggeri: SECOND-BRAIN,
RESEARCH, LEARNING.

**Confine con l'ecosistema 10 MEMORY (ADR-002, invariato dal v1):** INTELLIGENCE custodisce
la **conoscenza** (esterna ingerita + wiki + pattern appresi dagli agenti); l'ecosistema
10 MEMORY (`company/Memory/`, dossier `09-ECOSISTEMA-MEMORY.md`) custodisce la **memoria
operativa** (checkpoint CP, decisioni ADR, piani, stato, sessioni — "ciò che l'azienda FA",
non "ciò che l'azienda IMPARA da fuori" — vedi 09-MEMORY §0 OUT OF SCOPE). Il reparto L2 qui
sotto chiamato "MEMORY (= Memory Empire v3)" è il motore di *knowledge routing/enrichment*,
NON è l'ecosistema 10. Regola memory-first (pattern #13): ogni team di INTELLIGENCE interroga
`company/Memory/` prima di agire e scrive CP dopo, come tutti gli altri ecosistemi.

**DONE WHEN (misurabili):**
1. I 5 reparti L2 hanno org L3/L4 documentata; INGESTION e MEMORY hanno un team liaison
   (6 agenti ciascuno) che fa da wrapper, mai un roster duplicato; SECOND-BRAIN, RESEARCH,
   LEARNING hanno team 6-10 agenti a schede millimetriche e almeno un workflow CF-grade
   eseguito end-to-end ciascuno.
2. Ogni ecosistema, prima di un task non banale, ottiene un context pack (`wiki-context` +
   `memory_search`) tramite `WF-WIKI-CONTEXT` e dopo logga l'esito (wiki/log.md +
   ReasoningBank) — copertura ≥95%.
3. Empire Studio risponde come servizio: qualsiasi link/video/repo passato da qualsiasi
   ecosistema viene ingerito e archiviato integrale in knowledge/ + wiki tramite la coda
   liaison INGESTION, senza intervento manuale nel routing.
4. Memory Empire instrada il 100% delle richieste DE al workflow giusto (rete di sicurezza)
   e arricchisce skill esistenti senza romperle (gate G-SAFE-ENRICH sempre verde).
5. Wiki e AgentDB non divergono: `WF-WIKI-SYNC` attivo, log obbligatorio rispettato
   (mitigazione rischio #6 Piano Maestro); zero pagine wiki senza ≥2-3 cross-link.
6. RESEARCH consegna dossier con fonti tracciate (zero dati inventati — "prove non promesse"
   vale anche internamente) ad almeno 3 ecosistemi committenti (Agency, Marketing,
   Content-Factory).
7. LEARNING chiude almeno un ciclo completo: fallimento/successo → pattern distillato →
   pattern riusato da un altro ecosistema (namespace cross-ecosistema).
8. I namespace AgentDB `intelligence/` sono inizializzati; ogni workflow produce state
   ripartibile a freddo (test amnesia §6 piano V2).
9. Skill proprie dell'ecosistema forgiate (≥3: `context-pack`, `wiki-sync-guard`,
   `ingest-router`) via 06b-FORGE con PRD+architettura (standard §8 piano V2).

**OUT OF SCOPE (ora):** riscrittura interna di Empire Studio o Memory Empire (vincolo
cardinale sopra); memoria operativa della holding (checkpoint/ADR/stato) → ecosistema
10 MEMORY, non qui; spesa API di ingestione senza budget dichiarato → 06d-OPERATIONS.

---

## 1. Posizione nella holding — INTELLIGENCE è il fornitore di contesto di tutti

```
                    👑 LX — Mandato Empire (Art.5 Wiki-First, "prove non promesse")
                              |
L0  C-Suite ────── CTO/Chief-Forge (supervisione Backbone BRAIN) ──┤
                              |
L1  08-INTELLIGENCE ◄────── handoff contract ──────► tutti gli altri ecosistemi
        │
        ├── DIPENDE DA: 09-OPERATIONS (runtime swarm ingestione, cost guard, scheduling
        │              WF-WIKI-GARDEN/WF-TREND), 06b-FORGE (evoluzione Empire Studio/
        │              Memory Empire, forgiatura skill nuove)
        └── SERVE:    01-AGENCY        — ricerca lead/ICP, dossier competitor
                      02-INFO-BUSINESS — ricerca audience, materiale corsi (Empire Studio)
                      03-CF            — ingestione fonti, trend contenuti
                      04-MARKETING     — customer insight, pattern copy vincenti (input A2/BR4)
                      05-MULTI-BUSINESS — analisi canali YT riferimento, nicchie KDP
                      06a-PLATFORM     — ricerca tecnica (stack, librerie, competitor tecnici)
                      06b-FORGE        — materiale ingerito + pattern ReasoningBank (materia
                                        prima per forgiare/arricchire skill)
                      06d-OPERATIONS   — riceve log/metriche, restituisce pattern distillati
```

### 1.1 Handoff espliciti — chi chiede cosa a INTELLIGENCE

| Committente | Cosa richiede | Formato tipico | Reparto / Workflow destinazione |
|---|---|---|---|
| **01 AGENCY** | Ricerca lead/ICP, dossier competitor, ricerca cliente pre-preventivo | `icp`, `competitor`, `customer-research` | RESEARCH — WF-CUSTOMER / WF-COMPETITOR / WF-ICP-DISCOVERY |
| **02 INFO-BUSINESS** | Ricerca audience, materiale corso ingerito (video/canale riferimento) | `audience-research`, `ingest-video` | RESEARCH + INGESTION — WF-CUSTOMER / WF-INGEST-VIDEO |
| **03 CONTENT-FACTORY** | Ingestione fonti (canali, articoli), trend contenuti | `ingest-web`, `trend` | INGESTION + RESEARCH — WF-INGEST-WEB / WF-TREND |
| **04 MARKETING** | Customer insight, pattern copy vincenti per ICP (input A2/BR4/S2) | `pattern-query`, `customer-research` | RESEARCH + LEARNING — WF-CUSTOMER / lettura `intelligence/learning/patterns/{ecosistema}` |
| **05 MULTI-BUSINESS** | Analisi canali YouTube di riferimento, nicchie KDP | `ingest-video`, `trend` | INGESTION + RESEARCH — WF-INGEST-VIDEO / WF-TREND |
| **06a PLATFORM** | Ricerca tecnica (stack, librerie, competitor tecnici) prima di scelte d'architettura | `tech-research` | RESEARCH — WF-COMPETITOR (variante tecnica) |
| **06b FORGE** | Materiale ingerito MKD-ready per forgiare/arricchire skill; pattern sui fallimenti | `knowledge-pull`, `pattern-query` | INGESTION (pull da knowledge/) + LEARNING (ReasoningBank) |
| **06d OPERATIONS** | Log run, metriche, costi da distillare in pattern e pagine wiki | `pattern-distill` | LEARNING — WF-REASONINGBANK |
| **QUALSIASI ecosistema** | Context pack pre-task: `{pagine wiki, memorie, pattern, fonti}` | `context-pack` | SECOND-BRAIN — WF-WIKI-CONTEXT |

**Regola non negoziabile:** nessun ecosistema ingerisce contenuto esterno o scrive pagine
wiki "a mano" fuori standard — passa dalla coda liaison INGESTION o dal reparto SECOND-BRAIN
(garanzia di archiviazione integrale, mai riassunti — G-INTEGRAL). Un ecosistema può proporre
una bozza di pagina, ma la pubblicazione formale (frontmatter, cross-link, log) passa da qui.

### 1.2 Contratto di richiesta (handoff contract standard)

```json
{
  "committente": "01-AGENCY | 02-INFO | 03-CF | 04-MKT | 05-MB | 06a-PLT | 06b-FRG | 06d-OPS",
  "tipo_richiesta": "ingest-video | ingest-web | ingest-doc | context-pack | customer-research | competitor | trend | pattern-query | knowledge-pull",
  "target": "link | video | file | domanda | icp | competitor_url | ecosistema",
  "urgenza": "bassa | media | alta",
  "deadline": "YYYY-MM-DD"
}
```

Campi opzionali: `icp` (per ricerche legate a un avatar già esistente), `formato_output`
(dossier, brief, pattern-list), `vincoli` (lunghezza, fonti minime). Risposta di
INTELLIGENCE: `{esito, pagine_wiki_prodotte, memorie_collegate, pattern_usati, fonti,
workflow_eseguito}`.

**Regole del contratto (non negoziabili):**
- Richiesta di ingestione senza `target` valido → il router (INGESTION liaison, ING1)
  restituisce errore, non inventa la fonte.
- Richiesta `context-pack` senza `committente` → SECOND-BRAIN non produce output generico:
  chiede il committente (il context pack è sempre mirato a un ecosistema).
- Dossier di ricerca senza fonti tracciate → output non valido, non si consegna
  (Mandato "prove non promesse" vale anche sul lavoro interno).

---

## 2. Reparti L2 v2 — 5 reparti (stessi del v1, riequilibrati per profondità)

Il v1 aveva 5 reparti descritti allo stesso livello di dettaglio. In v2 la profondità è
riequilibrata secondo il vincolo cardinale: INGESTION e MEMORY restano **wrapper leggeri**
(team liaison di 6 agenti, zero duplicazione dei motori interni); SECOND-BRAIN, RESEARCH e
LEARNING — dove il v1 era oggettivamente più leggero (2-3 agenti ciascuno) — diventano
reparti pieni da 6-8 agenti con gerarchia e workflow CF-grade propri.

```
08-INTELLIGENCE (L1) — coordinatore: INT-Conductor
 ├── L2.1 INGESTION      ← WRAPPER di Empire Studio (così com'è: 9 reparti/50 agenti interni)
 ├── L2.2 MEMORY         ← WRAPPER di Memory Empire v3 (così com'è: 5 reparti interni)
 ├── L2.3 SECOND-BRAIN   ← ESPANSO v2: wiki ops, template, log enforcement, context pack
 ├── L2.4 RESEARCH       ← ESPANSO v2: customer, competitor, trend, sintesi mercato
 └── L2.5 LEARNING       ← ESPANSO v2: ReasoningBank, neural, promozione pattern
 ⊕   INT-Observer (trasversale, monitora i KPI dell'intero ecosistema, riporta al CTO)
```

---

### L2.1 — INGESTION (wrapper Empire Studio — NON duplicare i 50 agenti interni)

**Missione:** essere l'unico front-door ufficiale verso Empire Studio per qualsiasi
ecosistema che debba ingerire link/video/repo/documenti. Il team liaison non fa ingestione
esso stesso — la fa Empire Studio con i suoi 9 reparti interni (`conductor`,
`forge-wiki-department`, `memory-management-department`, e gli altri 6 verificati su disco
in `SKILL & Agenti/Empire Studio Suite/empire-studio/agents/`) — il team liaison **riceve,
classifica, traccia lo SLA e verifica l'handoff finale** (pagine wiki prodotte, evento costo
emesso verso 06d-OPERATIONS).

**Dove il v1 era già corretto:** `int-studio-conductor` era il singolo punto di contatto.
In v2 diventa un team liaison di 6 con ruoli distinti — senza mai toccare l'interno di
Empire Studio (che ha già il proprio conductor, il proprio QA, la propria memoria).

#### Team L2.1 (6 agenti — team liaison, standard minimo §2 direttiva scala)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `ING-LEAD` | Ingestion Liaison Lead | coordinator | sonnet | (ex `int-studio-conductor`, promosso) Punto di contatto ufficiale con il conductor di Empire Studio; riceve il contratto §1.2, apre la richiesta, riporta l'esito al committente |
| `ING1` | Intake Router | worker | haiku | Classifica `{link\|video\|file\|domanda}` e apre il ticket con Empire Studio nel formato atteso dal suo conductor |
| `ING2` | SLA Tracker | worker | haiku | Monitora il tempo di ingestione; verifica il pattern WATCH (N_video ingeriti = N_pagine Memory Empire prodotte — pattern già in uso, vedi `company/Memory/STATO-EMPIRE.md`) |
| `ING3` | Wiki Handoff Bridge | worker | haiku | Verifica che ogni ingestione completata produca le pagine wiki attese (handoff a SECOND-BRAIN); non scrive wiki, controlla che sia stata scritta |
| `ING4` | Cost Liaison | worker | haiku | Riceve l'evento costo emesso da Empire Studio a fine ingestione → lo inoltra al ledger 06d-OPERATIONS |
| `ING-QA` | Ingestion QA Verifier | verifier | sonnet | Verifica gate G-INTEGRAL: il contenuto archiviato è integrale, mai un riassunto; blocca la chiusura del ticket se la verifica fallisce |

#### Workflow L3 di L2.1 (4 workflow CF-grade — livello liaison, gli interni restano di Empire Studio)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-INGEST-INTAKE** | Fronte-porta: riceve richiesta, ING1 classifica, apre ticket con SLA tracciato | Ticket aperto con `target` valido e SLA dichiarato |
| **WF-INGEST-VIDEO** | Handoff verso Empire Studio per video/canale (frame reali + visione) → verifica ritorno | ING-QA verifica G-INTEGRAL; ING3 verifica pagine wiki prodotte |
| **WF-INGEST-WEB** | Handoff verso Empire Studio per link/sito/repo | Idem WF-INGEST-VIDEO |
| **WF-INGEST-DOC** | Handoff per file/cartelle (variante `book-to-skill` quando il target è una skill, ponte verso 06b-FORGE) | Idem; se target=skill, handoff esplicito a FORGE con MKD prodotto |

---

### L2.2 — MEMORY (wrapper Memory Empire v3 — NON duplicare i 5 reparti interni)

**Missione:** essere il punto di contatto ufficiale con Memory Empire v3 (router + archivio +
enrichment pipeline, già attivo in `~/.claude/skills/memory-empire/` con i propri 5 reparti
e agenti 7-file). Il team liaison **non instrada esso stesso** le richieste DE — lo fa il
router di Memory Empire — ma verifica che l'instradamento avvenga, che l'archiviazione sia
integrale e che l'enrichment non rompa mai una skill esistente (gate G-SAFE-ENRICH, il più
delicato del reparto: enrichment su skill attive senza backup/diff/non-regressione è un
rischio concreto per l'intera holding).

#### Team L2.2 (6 agenti — team liaison)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `MEM-LEAD` | Memory Liaison Lead | coordinator | sonnet | (ex `int-memory-router`, promosso) Punto di contatto con Memory Empire; riceve richieste DE, verifica che il router le abbia instradate |
| `MEM1` | Route Liaison | worker | haiku | Verifica che ogni richiesta DE passi dal `WF-ROUTE` giusto (rete di sicurezza, KPI 100%) |
| `MEM2` | Archive Liaison | worker | haiku | Verifica archiviazione integrale in `knowledge/` + wiki dopo ogni run di Memory Empire |
| `MEM3` | Enrich Safety Gate | verifier | sonnet | **Gate critico G-SAFE-ENRICH:** backup + diff + verifica non-regressione OBBLIGATORI prima che l'enrichment tocchi una skill attiva; blocca se manca uno dei tre |
| `MEM4` | Auto-Memory Sync | worker | haiku | Sync periodico di `~/.claude/projects/...Digital-Empire/memory/MEMORY.md` (auto-memory) verso la wiki, come da wrap v1 |
| `MEM-QA` | Memory Liaison QA Verifier | verifier | sonnet | Verifica copertura instradamento (KPI 100%) e che nessuna enrichment sia passata senza MEM3 |

#### Workflow L3 di L2.2 (4 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-ROUTE** | Router: ogni richiesta DE → workflow giusto, attivazione di sicurezza (rete di sicurezza Memory Empire) | MEM1 verifica 100% instradamento corretto |
| **WF-ARCHIVE** | Archivio integrale in `knowledge/` + wiki | MEM2 verifica; G-INTEGRAL condiviso con INGESTION |
| **WF-ENRICH** | Enrichment pipeline: nuova conoscenza → skill/workflow esistenti (safe) | MEM3 G-SAFE-ENRICH: backup+diff+non-regressione, mai bypassabile |
| **WF-AUTOMEMORY-SYNC** | Sync periodico auto-memory → wiki (asset esistente wrappato) | MEM4 esegue; divergenze → escalation a SECOND-BRAIN/WF-WIKI-SYNC |

---

### L2.3 — SECOND-BRAIN (wiki ops — ESPANSO rispetto al v1)

**Missione:** custodire la wiki `second-brain-vault/wiki/` come fonte di verità umana
(pattern #12 Piano Maestro, regola Wiki-First di `CLAUDE.md`), servire context pack pre-task
a chiunque, garantire zero divergenza wiki↔AgentDB e zero pagine orfane. Struttura verificata
su disco: `second-brain-vault/wiki/index.md`, `log.md`, `MOCs.md` + sottocartelle
`concepts/`, `entities/`, `projects/`, `tools/`, `sources/`, `synthesis/` — struttura
**intoccabile**, si popola, non si riprogetta.

**Dove il v1 era carente:** solo 2 agenti (`int-librarian`, `int-sync-keeper`), nessun
riconoscimento esplicito dei trigger "nuova conoscenza" descritti in `CLAUDE.md` §2 e nessun
gate che verifichi la creazione pagina secondo il template. In v2 il reparto ha 8 agenti con
lead e QA propri.

#### Team L2.3 (8 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `SB-LEAD` | Second-Brain Lead | coordinator | opus | **NUOVO v2:** coordina il reparto; arbitra la creazione di nuove cartelle/pagine; risponde del rispetto della regola Wiki-First davanti a INTELLIGENCE e alla Board |
| `SB1` | Wiki Librarian | worker | haiku | (ex `int-librarian`) Index, cross-link (≥2-3 per pagina), individua pagine orfane |
| `SB2` | Sync Keeper | worker | haiku | (ex `int-sync-keeper`) Controllo divergenza wiki ↔ AgentDB |
| `SB3` | Context Packer | worker | haiku | (ex `int-context-packer`) Compone il context pack pre-task `{pagine wiki, memorie, pattern, fonti}` per qualsiasi ecosistema |
| `SB4` | Page Architect | worker | sonnet | **NUOVO v2:** applica il template pagina (`CLAUDE.md` "Template rapido"), garantisce frontmatter `Type/Status/Tags/Created/Last updated`, sceglie la cartella corretta (concepts/entities/projects/tools/sources/synthesis) |
| `SB5` | Log Enforcer | worker | haiku | **NUOVO v2:** garantisce che ogni operazione wiki produca una entry in `log.md` (formato `## [Data] - INGEST: ... → N pagine`) — Art.5.2 Mandato / regola Wiki-First |
| `SB6` | Knowledge Signal Recognizer | worker | sonnet | **NUOVO v2:** riconosce nella conversazione/nei handoff i segnali di "nuova conoscenza" elencati in `CLAUDE.md` §2 (nuovo progetto, nuovo cliente, nuova decisione, nuova metrica) e propone la pagina — non chiede il permesso, propone e SB4 la costruisce |
| `SB-QA` | Second-Brain QA Verifier | verifier | sonnet | **NUOVO v2:** gate G-LOG + G-LINK + G-STRUCT prima che una pagina/aggiornamento sia "done"; blocca pagine senza cross-link o senza log |

#### Workflow L3 di L2.3 (5 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-WIKI-CONTEXT** | Context pack loader pre-task per ogni ecosistema (SB3) | Pack consegnato entro SLA; copertura KPI ≥95% task non banali |
| **WF-WIKI-SYNC** | Wiki ↔ AgentDB bridge (anti-divergenza) + log.md enforcement | SB2 zero divergenze aperte >7gg |
| **WF-WIKI-GARDEN** | Manutenzione: cross-link ≥2-3 per pagina, index.md, pagine orfane | SB1 + SB-QA; schedulata via 06d-OPERATIONS/WF-CRON |
| **WF-WIKI-NEW-PAGE** | SB6 riconosce il segnale → SB4 applica template → SB-QA verifica frontmatter+cross-link → SB5 logga | G-STRUCT + G-LOG verdi prima della pubblicazione |
| **WF-WIKI-INGEST-SIGNAL** | Riconoscimento automatico dei trigger `CLAUDE.md` §2 ("sto lavorando su...", "ho un nuovo cliente...", ecc.) durante una conversazione qualsiasi in questa directory | SB6 propone senza chiedere permesso (regola esplicita CLAUDE.md); SB-QA verifica prima della pubblicazione |

---

### L2.4 — RESEARCH (ESPANSO rispetto al v1)

**Missione:** produrre ricerca verificabile (customer, competitor, trend, sintesi di
mercato) per qualsiasi ecosistema committente, sempre con fonti tracciate — "prove non
promesse" vale anche sul lavoro di ricerca interno: zero conclusioni senza fonte.

**Dove il v1 era carente:** 3 agenti (`int-customer-researcher`, `int-competitor-analyst`,
`int-trend-scout`) senza lead di reparto, senza QA dedicato e senza un agente che sintetizzi
i dati grezzi ingeriti da Empire Studio in dossier strutturati per la Board.

#### Team L2.4 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `RES-LEAD` | Research Lead | coordinator | opus | **NUOVO v2:** coordina il reparto, prioritizza la coda multi-committente, arbitra conflitti di deadline tra ecosistemi |
| `R1` | Customer Researcher | worker | sonnet | (ex `int-customer-researcher`) ICP, interviste, JTBD per Agency e Marketing |
| `R2` | Competitor Analyst | worker | sonnet | (ex `int-competitor-analyst`) Dossier competitor da URL, anche variante tecnica per PLATFORM |
| `R3` | Trend Scout | worker | haiku | (ex `int-trend-scout`) Radar trend (mercato, AI, piattaforme), brief mensile alla Board |
| `R4` | Market Data Synthesizer | worker | sonnet | **NUOVO v2:** aggrega i dati grezzi ingeriti da Empire Studio + le ricerche R1/R2/R3 in un dossier strutturato leggibile dalla Board |
| `R5` | ICP/Avatar Librarian | worker | haiku | **NUOVO v2:** gestisce il namespace `intelligence/research/icp/{icp}`, versioning degli avatar riusati cross-ecosistema (in coordinamento con `marketing/avatars/{icp}`) |
| `R-QA` | Research QA Verifier | verifier | sonnet | **NUOVO v2:** verifica che ogni dossier abbia fonti tracciate e zero dati inventati prima della consegna al committente |

#### Workflow L3 di L2.4 (5 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-CUSTOMER** | Customer-research: ICP, interviste, JTBD | R-QA fonti tracciate; output in `intelligence/research/icp/{icp}` |
| **WF-COMPETITOR** | Competitor-profiling + market-competitors: dossier da URL | R-QA fonti tracciate; output in `intelligence/research/competitors/{competitor}` |
| **WF-TREND** | Radar trend → brief mensile alla Board | R3 + R4; cadenza mensile schedulata (06d-OPERATIONS/WF-CRON) |
| **WF-ICP-DISCOVERY** | **NUOVO v2:** discovery ICP end-to-end quando un committente non ha ancora un avatar (richiesta senza `icp` valido) | R1 + R5; avatar pubblicato in namespace prima che Marketing/Agency possano usarlo |
| **WF-MARKET-SYNTHESIS** | **NUOVO v2:** dati grezzi Empire Studio + ricerche R1-R3 → dossier di sintesi per un committente o per la Board | R4 sintetizza; R-QA verifica tracciabilità fonti prima della consegna |

---

### L2.5 — LEARNING (ESPANSO rispetto al v1)

**Missione:** rendere la holding auto-migliorante (pattern #5 Piano Maestro): ogni
fallimento e ogni successo diventano un pattern riusabile in ReasoningBank/AgentDB, e — se
l'evidenza è forte — vengono promossi a pagina wiki (Art.5.2 Mandato, wiki-first). LEARNING è
il reparto che chiude il cerchio tra ciò che succede in produzione (04-MARKETING,
01-AGENCY, 03-CONTENT-FACTORY, ...) e ciò che INTELLIGENCE sa.

**Dove il v1 era carente:** solo `int-pattern-distiller` come agente nominato (il workflow
`WF-NEURAL` esisteva ma senza un agente owner); nessuna distinzione tra pattern di
fallimento (ReasoningBank classico) e pattern di successo; nessun meccanismo esplicito per
far viaggiare un pattern da un namespace ecosistema a un altro.

#### Team L2.5 (6 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `LRN-LEAD` | Learning Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; decide quali pattern hanno evidenza sufficiente per la promozione a wiki |
| `L1` | Pattern Distiller (fallimenti) | worker | sonnet | (ex `int-pattern-distiller`) Da fallimenti loggati a pattern riusabili (ReasoningBank, pattern #5) |
| `L2` | Neural Trainer | worker | sonnet | **NUOVO v2:** owner esplicito di `WF-NEURAL`: gestisce cicli `neural_train` + autopilot periodici |
| `L3` | Success Pattern Miner | worker | haiku | **NUOVO v2:** estrae pattern anche dai successi (non solo dai fallimenti) — es. pattern copy vincenti già coperti da Marketing, ma generalizzabili ad altri ecosistemi |
| `L4` | Cross-Ecosystem Pattern Bridge | worker | sonnet | **NUOVO v2:** assicura che un pattern nato in un namespace ecosistema (es. `marketing/copy/patterns/{icp}`) sia leggibile/riusabile da un altro tramite l'indice `intelligence/learning/` |
| `L-QA` | Learning QA Verifier | verifier | haiku | **NUOVO v2:** verifica che ogni pattern salvato abbia evidenza (non opinioni) — regola anti-rumore, stesso principio di 04-MARKETING §4b |

#### Workflow L3 di L2.5 (4 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-REASONINGBANK** | Ogni fallimento loggato → distillato in pattern (pattern #5) | L-QA verifica evidenza; nessun pattern da opinione singola |
| **WF-NEURAL** | `neural_train` + autopilot: i workflow leggono pattern prima di agire | L2 owner; cadenza periodica schedulata (06d-OPERATIONS) |
| **WF-PATTERN-PROMOTE** | **NUOVO v2:** pattern con evidenza forte e ripetuta → promosso a pagina wiki (`concepts/` o `synthesis/`) | LRN-LEAD approva; SB4/SECOND-BRAIN pubblica; entry log.md |
| **WF-CROSS-ECOSYSTEM-SYNC** | **NUOVO v2:** sincronizza pattern tra namespace di ecosistemi diversi tramite L4 | Pattern indicizzato in `intelligence/learning/index`; nessuna duplicazione silenziosa |

---

## 3. Roster agenti completo (tutti i reparti)

### INT-Conductor + INT-Observer (L1)

| ID | Agente | Tipo | Tier | Ruolo |
|---|---|---|---|---|
| `INT-0` | INT-Conductor | coordinator | opus | Coordinatore ecosistema L1: riceve handoff dal BUS, valida contratto §1.2, smista ai reparti, gestisce coda multi-committente, escalation a C-Suite (CTO/Chief-Forge) |
| `INT-OBSERVER` | Intelligence Observability Lead | verifier | sonnet | **NUOVO v2:** monitora i KPI dell'intero ecosistema (copertura context pack, ingestioni completate, divergenze wiki/AgentDB, pattern riusati); alimenta il report Board |

### L2.1 Ingestion — liaison (6 agenti)

`ING-LEAD` · `ING1` · `ING2` · `ING3` · `ING4` · `ING-QA`
**Wrappa** Empire Studio (50 agenti interni, NON registrati qui — vedi §5.1).

### L2.2 Memory — liaison (6 agenti)

`MEM-LEAD` · `MEM1` · `MEM2` · `MEM3` · `MEM4` · `MEM-QA`
**Wrappa** Memory Empire v3 (5 reparti interni, agenti 7-file, NON registrati qui — vedi §5.1).

### L2.3 Second-Brain (8 agenti)

`SB-LEAD` [nuovo] · `SB1` · `SB2` · `SB3` · `SB4` [nuovo] · `SB5` [nuovo] · `SB6` [nuovo] · `SB-QA` [nuovo]

### L2.4 Research (7 agenti)

`RES-LEAD` [nuovo] · `R1` · `R2` · `R3` · `R4` [nuovo] · `R5` [nuovo] · `R-QA` [nuovo]

### L2.5 Learning (6 agenti)

`LRN-LEAD` [nuovo] · `L1` · `L2` [nuovo] · `L3` [nuovo] · `L4` [nuovo] · `L-QA` [nuovo]

### Conteggio roster v2

| Categoria | Agenti esistenti (dal v1) | Agenti nuovi v2 | Totale |
|---|---|---|---|
| INT-Conductor + Observer (L1) | 0 | 2 | 2 |
| L2.1 Ingestion (liaison) | 1 (ING-LEAD ex int-studio-conductor) | 5 | 6 |
| L2.2 Memory (liaison) | 1 (MEM-LEAD ex int-memory-router) | 5 | 6 |
| L2.3 Second-Brain | 3 (SB1, SB2, SB3 ex librarian/sync-keeper/context-packer) | 5 | 8 |
| L2.4 Research | 3 (R1, R2, R3) | 4 | 7 |
| L2.5 Learning | 1 (L1 ex int-pattern-distiller) | 5 | 6 |
| **TOTALE** | **9** | **26** | **35** |

*(Il v1 aveva 10 agenti registrati. In v2 se ne riusano 9 con ruolo promosso/rinominato, e se
ne aggiungono 26 per portare SECOND-BRAIN/RESEARCH/LEARNING allo standard 6-10 e dare a
INGESTION/MEMORY un team liaison completo senza duplicare i motori interni.)*

---

## 4. Workflow chiave CF-grade

### (a) Routing cross-ecosistema — flusso di ingresso principale

```
[Ecosistema committente]
   │  handoff contract {committente, tipo_richiesta, target, urgenza, deadline}
   ▼
INT-Conductor ──► valida contratto (target valido? committente riconosciuto?)
   │
   ▼  ROUTING PER TIPO RICHIESTA
   ├─ ingest-video / ingest-web / ingest-doc → L2.1 INGESTION (liaison → Empire Studio)
   ├─ context-pack                           → L2.3 SECOND-BRAIN / WF-WIKI-CONTEXT
   ├─ customer-research / competitor / trend → L2.4 RESEARCH
   ├─ pattern-query                          → L2.5 LEARNING (lettura namespace)
   └─ knowledge-pull                         → L2.1 INGESTION (pull da knowledge/ già ingerita)
   ▼
Reparto destinazione esegue il workflow L3 → gate specifico del reparto
   ▼
Risposta handoff: {esito, pagine_wiki_prodotte, memorie_collegate, pattern_usati, fonti,
                    workflow_eseguito}
   └─► hooks post-task: memory_store risultato + entry in wiki/log.md (regola Wiki-First)
```

### (b) Ingestione end-to-end (INGESTION liaison × Empire Studio)

```
Committente ── {link|video|file} ──► ING1 Intake Router (classifica, apre ticket)
   ▼
Empire Studio (9 reparti interni, conductor + forge-wiki-department +
memory-management-department + altri — NON toccati, NON duplicati)
   │  esegue: frame reali + visione Claude → knowledge/ integrale + wiki
   ▼
ING2 SLA Tracker ── verifica WATCH-001 (N_video ingeriti = N_pagine prodotte, MATCH ✅)
   ▼
ING3 Wiki Handoff Bridge ── verifica pagine wiki attese presenti
   ▼
ING-QA ── G-INTEGRAL: contenuto integrale, mai riassunto
   ▼
ING4 Cost Liaison ── evento costo → 06d-OPERATIONS/cost-ledger
   ▼
Esito al committente + entry wiki/log.md
```

### (c) Context pack pre-task (SECOND-BRAIN, il servizio più usato dell'intera holding)

```
Qualsiasi ecosistema, prima di un task non banale
   ▼
SB6 Knowledge Signal Recognizer ── (se il task genera nuova conoscenza, propone WF-WIKI-NEW-PAGE)
   ▼
SB3 Context Packer ── wiki-context loader:
   │   memory_search("wiki/index", "wiki/log", namespace ecosistema richiedente)
   ▼
Pack consegnato: {pagine wiki rilevanti, memorie AgentDB, pattern LEARNING, fonti}
   ▼
Ecosistema richiedente esegue il task CON contesto (mai "ciechi" — v1 §0)
   ▼
Dopo il task: risultato → SB5 Log Enforcer verifica entry log.md
```

### (d) Loop apprendimento cross-ecosistema (LEARNING, il cerchio che si chiude)

```
1. EVENTO       Un workflow di un ecosistema qualsiasi fallisce o ha successo notevole
2. LOG          L'ecosistema logga in company/Memory/ + wiki/log.md (regola memory-first)
3. DISTILLA     L1 (fallimenti) / L3 (successi) → pattern in
                intelligence/learning/patterns/{ecosistema}
4. VERIFICA     L-QA: il pattern ha evidenza ripetuta, non è un'opinione singola
5. PROMUOVE     Se evidenza forte → WF-PATTERN-PROMOTE → pagina wiki (concepts/synthesis)
6. DIFFONDE     L4 Cross-Ecosystem Pattern Bridge indicizza il pattern per altri ecosistemi
7. RIUSA        Un altro ecosistema (es. 04-MARKETING) legge il pattern PRIMA di agire
   └──────────────────────────────────────────► torna a 1 (loop continuo)
```

---

## 5. Asset esistenti wrappati (ADR-003: mappatura + wrapper, MAI riscrittura)

### 5.1 Motori primari — NON duplicare, solo registrare il wrapper

| Asset | Reparto | Azione v2 |
|---|---|---|
| `SKILL & Agenti/Empire Studio Suite/empire-studio/` (README.md, RULES.md, SKILL.md, `agents/` — verificato su disco: reparti `conductor`, `forge-wiki-department`, `memory-management-department` e altri, oltre 2000 file, agenti 7-file completi) | L2.1 INGESTION | **INGLOBA COSÌ COM'È.** Team liaison ING-* è il SOLO punto di contatto; zero modifiche interne finché non passa per 06b-FORGE |
| `~/.claude/skills/memory-empire/` v3 (agents, departments, knowledge, scripts, routing-map.md) | L2.2 MEMORY | **INGLOBA COSÌ COM'È.** Team liaison MEM-* è il SOLO punto di contatto; enrichment SOLO dietro G-SAFE-ENRICH (MEM3) |
| `~/.claude/projects/...Digital-Empire/memory/MEMORY.md` (auto-memory) | L2.2 MEMORY | **WRAPPA** — sync periodico verso wiki (MEM4, `WF-AUTOMEMORY-SYNC`) |

### 5.2 Wiki — struttura intoccabile, si popola

| Asset | Reparto | Azione v2 |
|---|---|---|
| `second-brain-vault/wiki/index.md`, `log.md`, `MOCs.md` (verificato su disco) | L2.3 SECOND-BRAIN | **USA** — fonte di verità, file esistenti, struttura intoccabile |
| `second-brain-vault/wiki/{concepts,entities,projects,tools,sources,synthesis}/` | L2.3 SECOND-BRAIN | **USA** — SB4 Page Architect rispetta questa tassonomia, non ne crea altre |

### 5.3 Skill esistenti — mapping a reparto (zero skill orfane)

| Skill | Reparto | Azione v2 |
|---|---|---|
| `wiki-context` | L2.3 / WF-WIKI-CONTEXT | **USA** — motore di SB3 |
| `memory-management` | L2.2 | **USA** — motore MEM-* |
| `customer-research` | L2.4 / WF-CUSTOMER | **USA** — motore R1 |
| `competitor-profiling`, `market-competitors` | L2.4 / WF-COMPETITOR | **USA** — motore R2 |
| `book-to-skill` | L2.1 / WF-INGEST-DOC | **USA** — ponte verso 06b-FORGE quando il target è una skill |
| Ruflo `memory_store/search`, ReasoningBank, AgentDB HNSW, `neural_train` | L2.5 LEARNING | **USA** — namespace `intelligence/learning/*` (vedi §9) |
| `SKILL & Agenti/Orchestracion layer - databese RAG/` | L2.5 LEARNING | **EVOLVI** — valutare integrazione con AgentDB, non urgente |
| Empire Studio skill propria (`SKILL.md` in `empire-studio/`) | L2.1 | **USA** — entry point ufficiale del motore, invocabile così com'è |

---

## 6. Skill NUOVE da forgiare (via 06b-FORGE, standard §8 piano V2: PRD → architettura → build)

| Skill nuova | Reparto | Cosa fa | Priorità |
|---|---|---|---|
| `context-pack` | L2.3 SECOND-BRAIN | Output standard pre-task: 1 comando → `{pagine wiki rilevanti, memorie, pattern, fonti}` per qualsiasi ecosistema — formalizza SB3 | **P0** |
| `wiki-sync-guard` | L2.3 SECOND-BRAIN | Check periodico divergenza wiki/AgentDB + report pagine orfane e log mancanti — formalizza SB2/SB5 | **P0** |
| `ingest-router` | L2.1 INGESTION | Front-door unica: classifica `{link\|video\|file\|domanda}` e instrada a Empire Studio / Memory Empire / Research — formalizza ING1 | **P0** |
| `wiki-page-architect` | L2.3 SECOND-BRAIN | Applica il template pagina + frontmatter + tassonomia cartelle in un comando — formalizza SB4 | P1 |
| `memory-safety-diff` | L2.2 MEMORY | Backup + diff + non-regressione automatico prima di ogni enrichment su skill attiva — formalizza il gate MEM3 | P1 |
| `research-source-tracker` | L2.4 RESEARCH | Traccia obbligatoriamente le fonti di ogni affermazione in un dossier di ricerca; blocca l'export senza fonte | P1 |
| `trend-radar` | L2.4 RESEARCH | Brief mensile trend per la Board (formato fisso, fonti tracciate) — formalizza R3/R4 | MEDIA |
| `pattern-promotion-gate` | L2.5 LEARNING | Verifica evidenza ripetuta prima di promuovere un pattern da AgentDB a pagina wiki — formalizza L-QA/WF-PATTERN-PROMOTE | MEDIA |

**Regola anti-contraddizione:** prima di creare ogni skill nuova → `skill-contradiction-analyzer`
contro le esistenti (`wiki-context`, `memory-management`, `customer-research`,
`competitor-profiling`, `book-to-skill`). Rischio concreto: `ingest-router` vs il conductor
interno di Empire Studio → la skill nuova è un front-door ESTERNO che chiama il conductor,
non lo sostituisce.

---

## 7. KPI + Quality Gates

### 7.1 Quality gates (bloccanti, in serie)

| Gate | Chi | Soglia | Esito fail |
|---|---|---|---|
| **G-INTEGRAL** | ING-QA (Ingestion) / MEM2 (Memory) | Contenuto archiviato INTEGRALE, mai solo riassunto | Blocco chiusura ticket; richiesta nuova ingestione |
| **G-LOG** | SB5 Log Enforcer | Ogni operazione wiki produce entry in `wiki/log.md` | Pagina non pubblicabile finché il log non esiste |
| **G-LINK** | SB1 / SB-QA | ≥2-3 cross-link per pagina wiki nuova | Pagina bloccata finché non ha i link minimi |
| **G-STRUCT** | SB-QA | Frontmatter completo (`Type/Status/Tags/Created/Last updated`) e cartella corretta | Rework da SB4 prima della pubblicazione |
| **G-SAFE-ENRICH** | MEM3 Enrich Safety Gate | Backup + diff + verifica non-regressione PRIMA di toccare una skill attiva | Blocco non derogabile; enrichment annullato |
| **G-SOURCE** | R-QA (Research) | Ogni affermazione di un dossier ha una fonte tracciata | Dossier non consegnabile al committente |
| **G-EVIDENCE** | L-QA (Learning) | Pattern salvato solo con evidenza ripetuta, mai da opinione singola | Pattern scartato, non entra in ReasoningBank |

### 7.2 KPI (riusa e amplia quelli del v1)

| KPI | Reparto | Definizione |
|---|---|---|
| Copertura context pack | L2.3 | % task non banali preceduti da contesto — target v1: ≥95% |
| Ingestioni completate senza intervento manuale | L2.1 | % — target v1: ≥90% |
| Divergenze wiki/AgentDB aperte >7gg | L2.3 | Target v1: 0 |
| Pagine wiki nuove con ≥2 cross-link | L2.3 | Target v1: 100% |
| Pattern ReasoningBank riusati (memory_search hit) | L2.5 | Target v1: trend crescente mese/mese |
| SLA ingestione (WATCH-001: N_video = N_pagine prodotte) | L2.1 | MATCH ✅ richiesto su ogni batch (pattern già in uso, vedi STATO-EMPIRE) |
| Copertura fonti tracciate nei dossier RESEARCH | L2.4 | **NUOVO v2** — target: 100%, zero dati inventati |
| Pattern promossi a wiki / pattern totali | L2.5 | **NUOVO v2** — misura la qualità del filtro L-QA, nessun target minimo imposto (anti-rumore) |
| Enrichment con G-SAFE-ENRICH verde al primo giro | L2.2 | **NUOVO v2** — target: 100%, zero skill rotte da enrichment |

---

## 8. Integrazione Ruflo (TopologyOrchestration)

**Topologia:** `hierarchical` (default holding) — INT-Conductor coordinatore di ecosistema;
lead di reparto (ING-LEAD, MEM-LEAD, SB-LEAD, RES-LEAD, LRN-LEAD) coordinatori L2. Fan-out
`mesh` SOLO dentro batch paralleli (es. ingestione multi-video di un canale, ricerca
multi-competitor). Decisioni cross-reparto (es. priorità tra un'ingestione urgente e una
ricerca urgente) → escalation a INT-Conductor, non risolte localmente.

| Funzione | Tool Ruflo | Uso in INTELLIGENCE |
|---|---|---|
| Pattern pre-lettura | `memory_search` | SB3/L1/L4 interrogano pattern PRIMA di produrre context pack o ricerca |
| Salvataggio esiti | `memory_store` + hooks post-task | Pattern, pagine wiki prodotte, esiti ingestione dopo ogni run |
| Apprendimento | ReasoningBank + `neural_train` | L2 owner del ciclo periodico; L1/L3 distillano |
| Sicurezza input | `aidefence_scan` / `aidefence_has_pii` | Su ogni documento/lista ingerita (research su clienti reali può contenere PII) |
| State per workflow | state.json per esecuzione | Ogni workflow CF-grade ripartibile a freddo (test amnesia §6 piano V2) |
| Fan-out batch | `swarm_init` + `task_orchestrate` | Ingestione multi-video, ricerca multi-competitor in parallelo |

---

## 9. Namespace memoria — `intelligence/...` (AgentDB/HNSW)

| Namespace | Contenuto | Owner |
|---|---|---|
| `intelligence/ingestion/queue` | Ticket di ingestione aperti/chiusi con SLA | ING-LEAD scrive |
| `intelligence/ingestion/sla` | Storico WATCH-001 (N_video vs N_pagine, MATCH/MISMATCH) | ING2 scrive |
| `intelligence/memory/route-log` | Registro instradamenti Memory Empire | MEM1 scrive |
| `intelligence/memory/enrich-diffs` | Backup+diff di ogni enrichment (per audit e rollback) | MEM3 scrive |
| `intelligence/wiki/context-packs/{committente}` | Ultimi context pack consegnati per ecosistema | SB3 scrive |
| `intelligence/wiki/sync-status` | Stato sync wiki↔AgentDB, divergenze aperte | SB2 scrive |
| `intelligence/research/icp/{icp}` | Avatar/ICP prodotti da R1/R5 (riuso cross-ecosistema con `marketing/avatars/{icp}`) | R1/R5 scrivono |
| `intelligence/research/competitors/{competitor}` | Dossier competitor | R2 scrive |
| `intelligence/research/trends` | Brief trend mensili | R3/R4 scrivono |
| `intelligence/learning/patterns/{ecosistema}` | Pattern distillati per ecosistema di origine | L1/L3 scrivono |
| `intelligence/learning/antipatterns/{ecosistema}` | Anti-pattern (cosa NON funziona) | L1 scrive |
| `intelligence/learning/promotions` | Registro pattern promossi a pagina wiki | LRN-LEAD scrive |
| `intelligence/handoffs/log` | Registro richieste/risposte cross-ecosistema | INT-Conductor scrive |

**Wiki-first (pattern #12 Piano Maestro, Art.5.2 Mandato):** i pattern consolidati con
evidenza forte vengono ANCHE scritti in pagine wiki (`concepts/` o `synthesis/`) + entry
`wiki/log.md`. AgentDB resta l'indice semantico operativo per gli agenti. In conflitto
wiki ↔ AgentDB: **vince la wiki**; AgentDB si reindicizza (SB2/WF-WIKI-SYNC).

---

## 10. Build plan v2

### Sequenza milestone (ordine non negoziabile: liaison prima di espansione)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **I1 — Formalizzazione liaison** | Team ING-* e MEM-* costruiti (6+6 agenti); wrapper handoff sopra Empire Studio e Memory Empire; zero modifiche interne | Una richiesta di ingestione e una di routing attraversano il wrapper senza toccare gli interni |
| **I2 — SECOND-BRAIN operativo** | Team SB-* (8 agenti); `WF-WIKI-CONTEXT` usato in un flusso AGENCY reale; `context-pack` (P0) forgiata | Context pack consegnato e usato da un task reale di un altro ecosistema |
| **I3 — Wiki hygiene a regime** | `WF-WIKI-GARDEN` + `WF-WIKI-SYNC` schedulati (via 06d-OPERATIONS); `wiki-sync-guard` (P0) forgiata | Primo report sync pulito, zero pagine orfane |
| **I4 — RESEARCH operativo** | Team RES-* (7 agenti); `research-source-tracker` forgiata; primo dossier consegnato a un committente reale | G-SOURCE verde su un dossier reale consegnato |
| **I5 — LEARNING attivo** | Team LRN-* (6 agenti); `WF-REASONINGBANK` logga i primi fallimenti dei workflow live (outreach); `pattern-promotion-gate` forgiata | Primi pattern distillati e almeno un pattern promosso a pagina wiki |
| **I6 — Ciclo cross-ecosistema chiuso** | `WF-CROSS-ECOSYSTEM-SYNC` attivo; un pattern nato in un ecosistema riusato da un altro (es. Marketing → Content-Factory) | DONE WHEN §0 punto 7 verificato su un caso reale |

---

## 11. Pre-mortem — rischi v2

| Rischio | Probabilità | Mitigazione |
|---|---|---|
| **Duplicazione accidentale** dei 50 agenti Empire Studio o dei 5 reparti Memory Empire dentro il roster INTELLIGENCE | Alta se non presidiato | Vincolo cardinale esplicito in §0; roster liaison fissato a 6+6; ogni PR/build che tocca `agents/` interni di Empire Studio o Memory Empire va fermata e passata per 06b-FORGE |
| **Confusione tra INTELLIGENCE e l'ecosistema 10 MEMORY** (checkpoint/ADR vs conoscenza esterna) | Media | §0 "Confine con l'ecosistema 10 MEMORY" esplicito e citato in ogni sezione rilevante; owner diversi, namespace diversi (`intelligence/*` vs `memory/*`) |
| **Wiki/AgentDB divergenti senza che nessuno se ne accorga** (rischio #6 Piano Maestro) | Media | `WF-WIKI-SYNC` schedulato, SB2 owner, KPI "divergenze aperte >7gg = 0" |
| **RESEARCH che consegna dati inventati** ("prove non promesse" violata anche internamente) | Media | G-SOURCE bloccante (R-QA), skill `research-source-tracker` obbligatoria prima dell'export |
| **Enrichment che rompe una skill attiva** (Memory Empire tocca qualcosa di live) | Alta se non presidiato | G-SAFE-ENRICH non derogabile (MEM3): backup+diff+non-regressione SEMPRE prima di modificare |
| **Pattern promossi senza evidenza sufficiente** (rumore in ReasoningBank/wiki) | Media | L-QA gate anti-opinione; promozione solo con evidenza ripetuta (stesso principio del loop Marketing §4b) |
| **SECOND-BRAIN diventa collo di bottiglia** (tutti gli ecosistemi in coda per un context pack) | Media | SB3 con SLA tracciato; fan-out swarm sui pack semplici; escalation a INT-Conductor se coda cresce |
| **PII nei materiali di ricerca o ingestione** (interviste clienti, liste, dati personali) | Media | `aidefence_has_pii` obbligatorio su ogni documento ingerito o dossier di ricerca prima dell'elaborazione |
| **Schede agenti liaison troppo leggere** (il rischio "è solo un file markdown" che Max denuncia) | Media | Standard §0 piano V2 obbligatorio anche per i team liaison; INT-OBSERVER verifica che ogni scheda abbia I/O, KPI, escalation, anche se il team è piccolo |

---

## 12. Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia LX→L5, backbone, pattern non negoziabili, i 10 ecosistemi
- [[11-PIANO-V2-DIRETTIVA-SCALA]] §0-2 — direttiva suprema che governa questo dossier (ADR-007)
- [[06-ECOSISTEMI-CORE]] — il v1 da cui si parte (sezione "08 · INTELLIGENCE", righe ~262-378); resta riferimento
- [[06a-ECOSISTEMA-PLATFORM-V2]] — riceve ricerca tecnica da RESEARCH; committente handoff §1.1
- [[06b-ECOSISTEMA-FORGE-V2]] — riceve materiale MKD-ready da INGESTION + pattern da LEARNING; unico autorizzato a evolvere Empire Studio/Memory Empire
- [[06d-ECOSISTEMA-OPERATIONS-V2]] — scritto in coppia con questo file; fornisce runtime/scheduling/cost-guard a tutti i workflow qui sopra; riceve log/metriche da distillare
- `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md` — ecosistema 10 MEMORY; confine esplicito §0; NON è lo stesso di "Memory Empire" (L2.2 qui)
- [[04-ECOSISTEMA-MARKETING-V2]] — committente RESEARCH (customer insight, pattern copy) e consumatore di LEARNING (pattern cross-ecosistema)
- `SKILL & Agenti/Empire Studio Suite/empire-studio/` — motore reale di L2.1 (verificato su disco)
- `~/.claude/skills/memory-empire/` — motore reale di L2.2
- `second-brain-vault/wiki/` — motore reale di L2.3 (index.md, log.md, MOCs.md, 6 sottocartelle)
- [[07-BACKBONE-RUFLO-SKILLS]] — registro skill e integrazione Ruflo; tutte le skill §6 vanno registrate qui
- `company/Memory/STATO-EMPIRE.md` — pattern WATCH-001 (N_video=N_MemoryEmpire) citato in §4b e §7.2, in uso reale da Empire Studio
- ADR-002 (confine INTELLIGENCE/MEMORY) · ADR-003 (wrap, non riscrittura) · ADR-007 (V2, CF-grade) · ADR-005 (minuzie → BACKLOG)
