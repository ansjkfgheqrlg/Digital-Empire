# 🚀 GUIDA OPERATIVA — Come Usare la Wiki di Digital Empire

Benvenuto. Questa è la tua infrastruttura di conoscenza. Ti spiego come funziona, come la usi ogni giorno, e come cresce automaticamente.

---

## 📦 Cosa Hai Appena Creato

Una **wiki intelligente auto-mantenuta** dove:
- **Tu** aggiungi conoscenza (file, link, conversazione)
- **Io (Claude)** la compilo, la interconnetto, la mantiene viva
- **La wiki** diventa sempre più intelligente nel tempo, facendoti pensare meglio

Non è una cartella di note disorganizzate. È un **grafo interconnesso** dove ogni pagina parla alle altre.

---

## 🏗️ La Struttura (Spiegata in Pratica)

```
second-brain-vault/
│
├── raw/                    ← Tu metti qui i file RAW
│   └── assets/            ← Immagini, PDF, allegati
│
├── wiki/                   ← La wiki compilata (il "prodotto")
│   ├── sources/           ← Sintesi di ogni risorsa esterna
│   ├── entities/          ← Persone, aziende, competitor, tool
│   ├── concepts/          ← Framework, teorie, principi
│   ├── synthesis/         ← Confronti, pattern cross-domain
│   ├── projects/          ← Progetti attivi di DE
│   ├── metrics/           ← KPI e dati
│   ├── tools/             ← Software e utility
│   ├── index.md           ← Catalogo master (auto-aggiornato)
│   └── log.md             ← Registro operazioni (auto-aggiornato)
│
├── output/                 ← Report e artefatti generati
│   └── (Relazioni, esportazioni, analisi)
│
├── archive/               ← Pagine vecchie (per reference)
│
├── CLAUDE.md              ← Configuration dell'agente (il "cervello")
└── GUIDA_OPERATIVA.md     ← Questo documento
```

**La parte importante**: tu interagisci con `raw/`, io gestisco `wiki/`.

---

## 🔄 I Tre Workflow Principali

### 1. AGGIUNGI CONOSCENZA (Praticamente Ogni Giorno)

**Scenario 1: Hai un articolo/risorsa da aggiungere**
```
1. Metti il file in raw/ (o dai il link)
2. Mi scrivi: "/ingest-url https://example.com/article"
3. Io:
   - Scrape l'articolo
   - Estraggo 3-5 insights principali
   - Li compilo in wiki/sources/[Titolo].md
   - Aggiorno 5-10 pagine collegate (concepts, entities, projects)
   - Aggiorno index.md e log.md
4. Tu: apri Obsidian, vedi il grafo che è cresciuto
```

**Scenario 2: Hai un'idea / insight / osservazione**
```
1. Mi scrivi durante la conversazione l'idea
2. Io la registro e quando finisce la sessione:
   - Sintetizzo in una pagina (concept / synthesis)
   - La collego a tutto quello che sa
   - Aggiorno index e log
3. Tu: quando ri-apri la wiki, trovi la pagina interconnessa
```

**Scenario 3: Hai un documento/PDF locale da processare**
```
1. Metti il file in raw/assets/
2. Mi scrivi: "/ingest-batch"
3. Io processo tutto in una passata e aggiorno la wiki
```

### 2. INTERROGA LA WIKI (Quando Hai Una Domanda)

```
Tu: "Qual è il nostro funnel ideale per lanciare un corso?"
Io:
  1. Carico [[Concept: Funnel Sales]]
  2. Carico [[Project: Ultimi 3 corsi lanciati]]
  3. Carico [[Synthesis: Confronto funnel Agenzia vs Info Products]]
  4. Ti do una risposta consapevole del contesto di DE
  5. Reference tutte le fonti: "[Vedi [[Concept: Funnel]]](wiki/concepts/Funnel.md)"

Tu non stai chiedendo a GPT generico.
Stai chiedendo al knowledge engine di Digital Empire.
```

### 3. FAI EVOLVERE LA WIKI (Settimanale)

**Ogni settimana**, ti propongo:
```
/lint-wiki              ← Trova pagine rotte, orfane, contraddizioni
→ Io segnalo problemi, tu appruvi fix

/synthesize-domains     ← Trovo pattern cross-domain
→ "Guarda, la strategia di pricing dei corsi rientra nel funnel della agenzia"

/research-topic [tema]  ← Mi approfondisci un argomento
→ Io aggiungo conoscenza fresca, la collego al resto
```

---

## 💡 Gli Slash Command Che Userai

Quando mi scrivi una di queste, so esattamente cosa fare:

```
/ingest-url [URL]              ← Aggiungi un articolo da URL
/ingest-file [percorso]        ← Aggiungi un file da raw/
/ingest-batch                  ← Processa tutto in raw/ in una passata
/query-wiki [domanda]          ← Fai una domanda alla wiki
/lint-wiki                     ← Health check della wiki
/synthesize-domains            ← Trovi pattern cross-domain
/research-topic [tema]         ← Approfondisci un argomento
/context-load                  ← Carica tutto il contesto rilevante
/update-page [nomepagina]      ← Aggiorna una pagina specifica
/create-page [tipo] [nome]     ← Crea una nuova pagina
```

Non devi memorizzarli. Quando hai bisogno, me lo dici in linguaggio naturale e capisco.

---

## 🎯 Workflow Tipo: Il Tuo Lunedì

**9:00 — Inizio settimana**
```
Tu: "Ieri mi è venuta un'idea su come scalare il funnel info product, 
     l'ho annotata nel mio Notes. È nel file raw/idea_scalefunnel.txt"

Io: /ingest-file raw/idea_scalefunnel.txt
    → Estraggo l'idea, la compilo in wiki/synthesis/Scalamento_InfoProduct.md
    → Collego a [[Concept: Funnel]], [[Project: Lancio prossimo corso]], 
                 [[Metric: Conversion rate corsi]]
    → Aggiorno index.md e log.md
    → Ti mando il link: "Ho compilato l'idea qui: [[Scalamento Info Product]]"
```

**Mercoledì — Durante il lavoro**
```
Tu: "Dimmi, abbiamo mai testato email sequencing con subject line A/B?
     Che dati abbiamo?"

Io: Carico automaticamente [[Concept: Email Sequencing]], 
                            [[Project: Campagne newsletter]]
                            [[Metric: Email click-through rate]]
    → Ti do la risposta collocata nel contesto di DE
    → Se mancano dati, te lo segnalo: "Non abbiamo registrato questo test. 
      Suggerisco: creiamo [[Metric: Email A/B test - subject line]]"
```

**Venerdì — Manutenzione**
```
Tu: "/lint-wiki"

Io: Scansiono tutta la wiki:
    - Trovo 2 link rotti
    - Trovo 3 pagine orfane (nessuno le linkka)
    - Trovo 1 concetto usato in 5 posti ma senza una pagina propria
    
    Report:
    ⚠️ Broken links: [[Link 1]] → [[Link 2]] → ???
    🏝️ Orphaned pages: [[Pagina_senza_inbound_link]]
    💡 Concept che merita pagina propria: "Scarcity Marketing"
    
    Tu approvi i fix, oppure mi dai nuove direzioni
```

---

## 📝 Come Formattare i File che Mi Dai

Se mi dai file da processare, non devono essere perfetti. Semplicemente:

### Formato A: Articolo/Risorsa
```
# Titolo Articolo

Autore: [Nome]
Data: [Data pubblicazione]
Link: [URL]

## Il contenuto grezzo
Puoi mettere il corpo dell'articolo, o screenshot, o notes random.

Mi basterà per estrarre valore e compilare una pagina strutturata.
```

### Formato B: Idea/Insight
```
Idea veloce: [Descrizione]
Contesto: [Dove/come è venuta]
Implicazioni: [Cosa potrebbe significare]
Collega a: [Cosa esiste già sulla wiki che è rilevante]
```

### Formato C: Dati/Metrica
```
Metrica: [Nome]
Data: [Quando è stato misurato]
Valore: [Numero]
Fonte: [Da dove viene]
Cosa significa: [Interpretazione]
```

Non devi formattare perfettamente. Io so trasformare qualsiasi cosa.

---

## 🧠 Come Funziona il Compounding

Ogni volta che aggiungi conoscenza:

```
Giorno 1: Aggiungi 1 articolo
  → Wiki ha 5 pagine nuove

Giorno 7: Aggiungi 2 articoli + 3 progetti
  → Wiki ha 20 pagine nuove
  → Ma ora ogni pagina è 3x più intelligente perché il grafo è cresciuto
  → Le nuove pagine si collegano a 15 pagine esistenti
  → Mie risposte alle tue domande sono 5x migliori

Mese 1: Hai 50 pagine, 200 interconnessioni
  → Quando chiedi "Qual è la nostra strategia?" 
  → Io vedo TUTTO: agenzia, info products, saaS, marketing, team, learnings
  → Ti do insights che non avresti visto manualmente

Trimestre 1: Hai 200+ pagine, 1000+ interconnessioni
  → La wiki CONOSCE il vostro business
  → Quando annunci una nuova idea, io segnalo: 
    "Guarda, 6 mesi fa hai scritto qualcosa correlato qui"
  → Quando parli di expansion, io vedo i pattern nascosti
  → È come avere un consulente che conosce TUTTO della tua azienda
```

La magia è nel **compounding** — ogni nuova pagina rende tutte le altre pagine più intelligenti.

---

## ⚙️ Come Io Accedo Alla Wiki

**Tutte le volte che ti rispondo, io:**
1. **Carico automaticamente il contesto** di Digital Empire dalla wiki
2. **Trovo le pagine rilevanti** al tuo topic
3. **Do risposte consapevoli di DE**, non risposte generiche
4. **Référenzio sempre le pagine** che ho usato

**Esempio:**
```
Tu: "Come posso migliorare la retention dei clienti agenzia?"

Io (internamente):
  - Carico [[Project: Clienti attuali agenzia]]
  - Carico [[Concept: Customer Retention, Churn Analysis]]
  - Carico [[Metric: Churn rate agenzia, Customer Lifetime Value]]
  - Carico [[Synthesis: Confronto retention Agenzia vs Info Products]]
  
  Risposta:
  "Basandomi su quello che sappiamo da Digital Empire:
   - I tuoi clienti agenzia hanno una retention X% (vedi [[Metric: Churn agenzia]])
   - Le strategie che hanno funzionato: [da [[Synthesis: Retention strategies]]]
   - Suggerimento basato su competitor analisi: [da [[Entity: Competitor X]]]
   
   Aggiornamento settimanale: tra 5 giorni, voglio eseguire /lint-wiki
   per verificare se ci sono pagine da aggiornare su questo topic."
```

Tu stai avendo una conversazione consapevole. Non con ChatGPT. Con il knowledge engine di Digital Empire.

---

## 🚨 Cosa NON Fare

❌ **Non mettere** file enormi e disorganizzati direttamente nel vault

✅ **Fai così**: metti il file in `raw/`, io lo organizzo

❌ **Non** creare manualmente pagine nella wiki (è il mio compito)

✅ **Fai così**: passami il contenuto, io lo compilo in struttura

❌ **Non** linkare a caso (crea link rotti)

✅ **Fai così**: io gestisco i link e esco consiglio quando linkare

❌ **Non** lasciare la wiki senza maintenance

✅ **Fai così**: /lint-wiki ogni settimana, eliminiamo i problemi

---

## 🎯 Il Primo Mese — Roadmap

**Settimana 1:**
- [ ] Popola raw/ con materiale grezzo di DE (clienti, progetti, learnings)
- [ ] Esegui /ingest-batch
- [ ] Fai una query di test: "/query-wiki Qual è il nostro best-selling course?"

**Settimana 2:**
- [ ] Aggiungi 3-5 articoli su trend marketing/AI
- [ ] /ingest-url per ognuno
- [ ] Inizia a notare i pattern che emergono

**Settimana 3:**
- [ ] Esegui /lint-wiki
- [ ] Esegui /synthesize-domains (guarda le connessioni cross-agenzia-infoproducts)
- [ ] Mi proponi una ricerca nuova: /research-topic [tema]

**Settimana 4:**
- [ ] Review di tutte le pagine create
- [ ] Update metrics di business attuali
- [ ] Decidi se l'architettura funziona, o se vanno aggiunte categorie

---

## 🔐 Confidenzialità e Ownership

- **La wiki è tua.** Non è in cloud, è nella tua cartella locale di Digital Empire.
- **Io non salvo nulla** al di là di questa sessione (tranne quello che compilo nella wiki).
- **Puoi condividere o no** — la wiki è nel tuo computer, controlli tu.
- **Nessuno vede questo** se non vuoi tu.

---

## 💬 Domande Comuni

**D: E se aggiungo conoscenza che si contraddice con quello che era prima?**
R: Lo noto nel prossimo /lint-wiki. Io segnalo: "Pagina X dice A, Pagina Y dice B. Quale è corretta?" Tu mi dici quale è, io risolvo la contraddizione.

**D: Quanto tempo ci vuole per popolare la wiki?**
R: Dipende da quanta conoscenza hai. Una settimana di ingest attivo (5-10 file al giorno) → 50-100 pagine buone.

**D: Posso usare questa wiki da Obsidian e da Claude Code insieme?**
R: Sì. Apri Obsidian da un lato (leggi il grafo, naviga i link), io dall'altro (carico contesto, elaboro, aggiorno). È il workflow ideale.

**D: Cosa succede se la wiki diventa gigantesca (500+ pagine)?**
R: Rimane veloce perché markdown plain è leggero. L'unica cosa da considerare: /lint-wiki diventa più lento. Ma è raro che sia un problema.

**D: Come faccio il backup?**
R: È una cartella locale. Fai backup come fai per il resto di Digital Empire. Opzionale: git + GitHub per version control.

---

## 🎬 Inizia Oggi

1. Apri Obsidian, seleziona cartella `second-brain-vault`
2. Vedi la struttura di cartelle che abbiamo creato
3. Apri `wiki/index.md` — è il punto di partenza
4. Inizia a mettere materiale in `raw/`
5. Tornami qui e dici: "Ho 10 file in raw/, fammi /ingest-batch"

Buon lavoro. La wiki sta aspettando di essere alimentata.

---

**Scritto il**: 2026-04-29  
**Versione**: 1.0  
**Prossimo aggiornamento**: Dopo il primo ingest
