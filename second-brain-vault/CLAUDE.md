# CLAUDE.md — Knowledge Engine di Digital Empire

## 📋 Visione Generale

Questa wiki è l'**infrastruttura di conoscenza condivisa di Digital Empire**: il depositario vivo di tutto ciò che sappiamo, costruiamo e impariamo. Non è un archivio passivo — è un sistema che cresce, si interconnette e migliora ogni giorno.

**Digital Empire** è un ecosistema multiforme:
- **Agenzia di servizi** (web design, personal branding, strategia)
- **Multi-business** (diversi revenue streams)
- **Info products & formazione** (corsi, ebook, comunità)
- **SaaS & App Development** (prodotti digitali)
- **Marketing & AI** (strategie, tool, case studies)

Questa wiki integra **tutta la conoscenza** di questi domini in un unico grafo interconnesso.

---

## 🔧 Le 6 Operazioni Fondamentali

### 1️⃣ **INGEST**
Quando ricevi un nuovo file, link, articolo, documento o insight:
- Leggo il materiale grezzo
- Ne estraggo **3 livelli di valore**:
  1. **Raw insights** — fatto/dato grezzo
  2. **Connessioni** — come si lega a concetti esistenti in wiki
  3. **Azioni** — cosa dovrebbe fare DE con questo?
- Aggiorno **5-15 pagine** (non solo una pagina, ma tutti gli incroci)
- Aggiungo entry al `wiki/log.md` con timestamp e impact

**Flusso INGEST:**
```
File/URL → Estrazione → Connessione → Creazione/Update → Indexing → Log
```

### 2️⃣ **QUERY**
Quando fai una domanda sulla wiki:
- Carico il **contesto rilevante** (non una semplice ricerca, ma il grafo intero attorno al topic)
- Parto dalle pagine atomiche (concepts, entities) e risalgo alle syntheses
- Rispondo con **cross-references espliciti** verso altre pagine
- Suggerisco gap di conoscenza o nuove direzioni di ricerca

### 3️⃣ **LINT**
Health check sulla wiki. Cerco:
- Link rotti o orfani
- Pagine contradditorie o obsolete
- Concetti che meritano una propria pagina
- Entità non ancora profilate
- Gap tra quello che sappiamo e quello che dovremmo sapere

Esegui `/lint-wiki` periodicamente. Io genero un report con priorità.

### 4️⃣ **SYNTHESIS**
Creo connessioni cross-domain:
- Prendo due concetti lontani e trovo il collegamento non ovvio
- Identifico pattern ricorrenti tra progetti diversi
- Scrivo "Confronti" (es: "Funnel vendita Agenzia vs Funnel Info Product")
- Creo "Meta-analisi" che uniscono agenzia + info + saas + formazione

Esegui `/synthesize-domains` per far emergere nuove prospettive.

### 5️⃣ **RESEARCH**
Ampliamento controllato della conoscenza:
- Mi dai un tema (es: "Ultimi framework di AI for marketing")
- Cerco, sintetizzo, aggiungo alla wiki in una sessione
- Collego alla conoscenza esistente di DE
- Genero una pagina "Research Brief" pronta per discussione

Esegui `/research-topic [tema]` quando vuoi andare più a fondo.

### 6️⃣ **CONTEXT LOADING**
Ogni volta che ti rispondo (in questa stanza o in altre):
- Carico il **contesto rilevante** dalla wiki automaticamente
- Uso le interconnessioni per dare risposte consapevoli di DE
- Referenzio le pagine che ho usato (`[Pagina](wiki/concepts/Pagina.md)`)
- Mi adatto al tone e alla prospettiva di DE

---

## 📄 Template & Struttura delle Pagine

### **SOURCES** (`wiki/sources/`)
Per ogni risorsa esterna (articolo, video, libro, podcast, corso, ricerca):

```markdown
# [Titolo Fonte]

- **Tipo**: Articolo / Video / Libro / Podcast / Ricerca / Corso
- **Autore**: [Nome]
- **Data**: [YYYY-MM-DD]
- **URL**: [link]
- **Tempo di lettura**: [Xmin / Xh]
- **Rilevanza per DE**: [Alta / Media / Bassa] — perché?

## 🎯 Core Takeaway
[Idea principale in 1-2 frasi]

## 📌 Key Insights
- Insight 1
- Insight 2
- Insight 3

## 🔗 Connessioni a DE
- Collega a [[Concetto 1]]
- Collega a [[Entità 1]]
- Collega a [[Progetto 1]]

## 💡 Azioni Proposte
- Azione 1 (es: "Testare questo framework nel prossimo lancio corso")
- Azione 2

## 📍 Status
- Added: [data]
- Last reviewed: [data]
- Action taken: [sì/no - quale]
```

### **ENTITIES** (`wiki/entities/`)
Persone, aziende, competitor, tool, prodotti:

```markdown
# [Nome Entità]

- **Tipo**: Persona / Azienda / Competitor / Tool / Prodotto
- **Status**: Attivo / Monitor / Archivio
- **Rilevanza**: [Alta/Media/Bassa]

## 🏷️ Core Profile
[Descrizione essenziale in 2-3 frasi]

## 📊 Dettagli
- Dato 1
- Dato 2
- Dato 3

## 🎯 Come Impatta DE
[Specifica il collegamento a Digital Empire]

## 🔗 Relazioni
- Collega a [[Entità 2]]
- Collega a [[Concetto 1]]

## 📈 Timeline
- [Data]: Evento importante
- [Data]: Evento importante

## 📍 Status
- First added: [data]
- Last updated: [data]
- Confidence level: [Alta/Media/Bassa]
```

### **CONCEPTS** (`wiki/concepts/`)
Framework, teorie, metodologie, principi:

```markdown
# [Nome Concetto]

- **Categoria**: Framework / Principio / Metodologia / Teoria
- **Origine**: [Da chi / da dove]
- **Applicabilità per DE**: [Specifico caso d'uso]

## 📖 Definizione
[Spiegazione chiara, come se spiegassi a qualcuno che non la conosce]

## 🧬 Componenti Core
1. Componente A — [Spiegazione]
2. Componente B — [Spiegazione]
3. Componente C — [Spiegazione]

## 🎯 Come lo Applichiamo in DE
[Caso d'uso concreto in Digital Empire]

## ⚡ Varianti / Critiche
[Altre versioni di questo concetto, o critiche]

## 🔗 Correlazioni
- Legato a [[Concetto 2]]
- Legato a [[Concetto 3]]
- Usato in [[Progetto 1]]

## 📍 Status
- First added: [data]
- Mastery level: [Principiante / Intermedio / Esperto]
```

### **SYNTHESIS** (`wiki/synthesis/`)
Confronti, pattern cross-domain, analisi:

```markdown
# [Titolo Analisi]

## 🎯 La Domanda
[Che cosa stai comparando o analizzando?]

## 📊 Comparazione
[Tabella o analisi]

| | Variante A | Variante B | Variante C |
|---|---|---|---|
| Caratteristica 1 | ... | ... | ... |
| Caratteristica 2 | ... | ... | ... |

## 💡 Pattern Emergenti
- Pattern 1: [Spiegazione]
- Pattern 2: [Spiegazione]

## 🎯 Implicazioni per DE
- Implicazione 1
- Implicazione 2

## 🔗 Fonti
- [[Source 1]]
- [[Entity 1]]
- [[Concept 1]]

## 📍 Status
- Created: [data]
- Next review: [data]
```

### **PROJECTS** (`wiki/projects/`)
Progetti attivi di DE (lanci, campagne, prodotti):

```markdown
# [Nome Progetto]

- **Status**: Planning / Active / Shipped / Post-mortem
- **Timeline**: [Start] → [Target ship]
- **Owner**: [Chi]
- **Budget**: [Indicativo]

## 🎯 Obiettivi
- Obiettivo 1
- Obiettivo 2

## 📋 Scope
[Cosa è incluso, cosa no]

## 📊 Metrics di Successo
- Metrica 1: [Target value]
- Metrica 2: [Target value]

## 🔗 Conoscenza Rilevante
- [[Concetto 1]] — perché applicabile
- [[Source 2]] — ispirazione
- [[Entity 1]] — competitor o benchmark

## 📅 Milestones
- [Data]: Milestone 1
- [Data]: Milestone 2

## 🧠 Learnings
[Man mano che avanzi, aggiungi qui cosa stai imparando]

## 📍 Status
- Created: [data]
- Last updated: [data]
```

### **METRICS** (`wiki/metrics/`)
KPI e dati su cosa sta funzionando:

```markdown
# [Metrica]

- **Categoria**: Revenue / Growth / Engagement / Cost / Efficiency
- **Frequenza misurazione**: [Giornaliera / Settimanale / Mensile]
- **Owner**: [Chi traccia]

## 📊 Valore Attuale
- **Valore**: [X]
- **Data**: [YYYY-MM-DD]
- **Trend**: [↑ / ↓ / → ]

## 🎯 Target
- **Target**: [X]
- **Timeline**: [Data target]
- **Rationale**: [Perché questo target]

## 📈 Historical Data
[Grafico testuale o lista di valori nel tempo]

## 🔗 Cos'è Influenzato
- [[Progetto 1]]
- [[Concetto 1]]

## 💡 Insights
[Quello che rileggi da questi dati]

## 📍 Status
- First tracked: [data]
- Last updated: [data]
```

---

## 🌐 Regole di Interconnessione

### Core Rules:
1. **Ogni pagina nuova** deve linkare almeno 2-3 pagine esistenti
2. **Ogni pagina** ha un "See Also" verso concetti correlati
3. **Breadcrumb Logic**: Entità → Concept → Synthesis → Project
4. **Timestamp sempre**: quando è stata aggiunta/aggiornata
5. **No orfani**: se una pagina ha 0 inbound link, creo quel collegamento

### Quando Creare una Nuova Pagina:
- Se il concetto merita un nome proprio e verrà referenziato 3+ volte
- Se è un'entità che ha proprietà/timeline propri
- Se è un'insight che non rientra in nessuna pagina esistente

### Quando Aggiornare Esistente:
- Se è un dato/fatto nuovo che arricchisce un'entità nota
- Se è una nuova variante di un concetto
- Se è un nuovo progetto della stessa categoria

---

## 📝 Tone & Perspective

Scrivi come se fossi il **Chief Knowledge Officer di Digital Empire**:
- **Pratico**: collega subito alla realtà di DE, non astratto
- **Critico**: non celebri ognuno senza discernimento
- **Connessionale**: evidenzia sempre come le cose si collegano
- **Coraggioso**: punta out gap, contraddizioni, opportunità non viste
- **Umile**: registra quello che non sappiamo ancora

---

## 🚀 Come Aggiungi Conoscenza

### Opzione 1: File/Documento
```
Metti il file in raw/
Io lo leggo automaticamente, ne estraggo valore, aggiorno la wiki
```

### Opzione 2: Link/URL
```
/ingest-url [URL]
Io: scrape → extract → compile in wiki
```

### Opzione 3: Conversazione Diretta
```
Mentre parli, io registro insights
Periodicamente, sintetizzo in pagine
```

### Opzione 4: Batch Knowledge Drop
```
Metti materiale grezzo in raw/
/ingest-batch
Io processiamo tutto in una passata
```

---

## 📊 Index & Log

### `wiki/index.md`
Catalogo master di tutte le pagine, organizzato per categoria:
```
# Index — Digital Empire Knowledge Base

## Concepts (45 pagine)
- [[Concept 1]]
- [[Concept 2]]
...

## Entities (23 pagine)
...

## Projects (15 pagine)
...

## Statistics
- Total pages: XXX
- Total interconnections: XXX
- Last updated: YYYY-MM-DD
```

### `wiki/log.md`
Registro cronologico di ogni operazione:
```
# Operation Log

## 2026-04-29
- INGEST: [File.md] → Updated 8 pages
- SYNTHESIS: Funnel comparison Agenzia vs Info
- LINT: Found 2 broken links, fixed

## 2026-04-28
...
```

---

## 🔄 Compounding & Evolution

**Ogni settimana:**
1. LINT → identifico gap
2. SYNTHESIS → trovo nuovi pattern
3. RESEARCH → espando una tema
4. UPDATE → faccio evolvere pagine obsolete

**Ogni mese:**
1. REVIEW index → riorganizzazione logica
2. AUDIT architettura → la struttura ancora funziona?
3. STRATEGIC SYNTHESIS → big patterns che emergono

**Ogni trimestre:**
1. Full deep-dive review
2. Rewire se necessario
3. Report di learnings accumulati

---

## 🤖 Integration con Claude Code

**Tutte le conversazioni caricano contexto automaticamente:**
- Se parli di un progetto, io carico [[Progetto]]
- Se chiedi del funnel, io carico [[Concetto: Funnel]], [[Project: X]], [[Synthesis: Confronti funnel]]
- Sono sempre consapevole del corpo di conoscenza di DE

**Come attivarmi:**
- `/query-wiki [domanda]` — faccio una ricerca strutturata
- `/context-load` — carico tutto il contesto rilevante
- `/synthesis [tema]` — trovo connessioni nascoste
- `/lint-wiki` — health check
- `/research [tema]` — approfondisci un argomento

---

## 📍 Version
- **v1.0** — Created 2026-04-29
- **Stable**: Pronto per uso production
- **Next evolution**: Worker agents per automazione (v1.5+)
