# Wiki-secondBrain
            
> Path: [[Map - General|general]]

## Content

LLM Wiki / Second Brain 

### Cos'è e da dove nasce — La storia vera

Questo è il metodo **più nuovo e rivoluzionario**, ed è nato da una persona specifica: **Andrej Karpathy** (co-fondatore di OpenAI, ex director of AI di Tesla).

Karpathy ha pubblicato un thread sull'uso degli LLM per costruire knowledge base personali: dumpa materiale grezzo in una cartella, lascia che l'LLM lo compili in una wiki strutturata, e usa Obsidian per sfogliare tutto. Ha poi esteso la teoria includendo un "idea file" volutamente vago per lasciare spazio alla creatività. L'idea file è disponibile qui: **https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f**

### Il principio fondamentale

**Non scrivi mai (o quasi mai) la wiki tu stesso — è l'LLM a scriverla e mantenerla tutta**. Tu sei responsabile del sourcing, dell'esplorazione e delle domande giuste. L'LLM fa tutto il lavoro pesante: riassumere, cross-referenziare, archiviare, e il "bookkeeping" che rende una knowledge base davvero utile nel tempo.

In pratica: hai l'agente LLM aperto su un lato e Obsidian sull'altro. L'LLM fa modifiche basandosi sulla conversazione, e tu sfoglia i risultati in tempo reale seguendo i link, controllando la graph view, leggendo le pagine aggiornate. **Obsidian è l'IDE; l'LLM è il programmatore; la wiki è il codebase.**

### Perché è superiore agli altri metodi (onestamente)

Karpathy ha condiviso un approccio alla gestione della conoscenza personale che **bypassa completamente il RAG tradizionale**. Invece di embeddare le tue note in vettori e fare ricerca semantica, le struttura come file markdown plain che un LLM può leggere direttamente. L'LLM non cerca solo nelle tue note — **le scrive e le mantiene**.

E la parte più potente: **questo sistema si compone**. Ogni nuova fonte che l'LLM ingerisce rende l'intera wiki più intelligente. Diventa una rete che cresce sempre più densa nel tempo.

---

## 🏗️ L'ARCHITETTURA DEL SISTEMA — Come funziona tecnicamente

### La struttura delle cartelle (da Karpathy + community)

La struttura vault raccomandata è:
```
your-vault/
├── raw/          # Il tuo inbox — qui metti le fonti
│   └── assets/  # Immagini e allegati
├── wiki/         # La wiki mantenuta dall'LLM
│   ├── sources/  # Un riassunto per ogni fonte
│   ├── entities/ # Persone, organizzazioni, prodotti
│   ├── concepts/ # Idee, framework, teorie
│   ├── synthesis/# Confronti, analisi, temi
│   ├── index.md  # Catalogo master di tutte le pagine
│   └── log.md    # Registro cronologico delle operazioni
├── output/       # Report e artefatti generati
└── CLAUDE.md     # Config dell'agente
```

### Le 3 operazioni fondamentali

Karpathy riduce il sistema a **tre operazioni**: ingest, query, e lint.
- **Ingest** = aggiungere una nuova fonte alla collezione raw e chiedere al modello di processarla. Il modello legge la fonte, aggiorna le pagine esistenti, ne crea di nuove dove serve, aggiorna l'indice e aggiunge un'entry al log.
- **Query** = fare domande contro la wiki, non contro un mucchio di file scollegati. Questo migliora la qualità delle risposte perché il modello lavora su pagine che già contengono struttura, cross-link e sintesi.
- **Lint** = health check sulla wiki. Il modello cerca claim obsoleti, contraddizioni, link mancanti, pagine orfane e concetti che meritano una propria pagina.

### Il file CLAUDE.md — Il cuore del sistema

La magia sta nel **file di config dell'agente** (CLAUDE.md, AGENTS.md, ecc.) alla radice del vault. È qui che dici all'LLM come comportarsi da tuo bibliotecario — l'architettura, le operazioni, il formato delle pagine e le regole che deve seguire.

---

## 📚 LE REPOSITORY GITHUB — Le migliori trovate

Eccole tutte, dalla migliore alla più avanzata:

---

### 🥇 1. `NicholasSpisak/second-brain` ⭐ CONSIGLIATA PER INIZIARE
🔗 **https://github.com/NicholasSpisak/second-brain**

**LLM-maintained personal knowledge base for Obsidian**, basato sul pattern LLM Wiki di Andrej Karpathy.

Richiede: Obsidian, un AI coding agent (Claude Code, Codex, Cursor, Gemini CLI), e Node.js. Il setup è guidato: digita `/second-brain` nel tuo agente AI — ti guida attraverso nome, posizione, dominio e strumenti. Poi installa Obsidian Web Clipper configurato per salvare nella cartella `raw/` del tuo vault.

Tool opzionali ma raccomandati: `summarize` (riassume link, file e media dalla CLI), `qmd` (motore di ricerca locale per file markdown, diventa importante man mano che la wiki cresce), `agent-browser` (automazione browser per ricerca web).

---

### 🥈 2. `eugeniughelbur/obsidian-second-brain` ⭐ PIÙ AVANZATA
🔗 **https://github.com/eugeniughelbur/obsidian-second-brain**

La maggior parte dei tool per il second brain ti rende il **custode/janitor**. Questa skill inverte tutto: tu pensi, lavori e parli. Claude gestisce la memoria. Poi usa quella memoria per farti pensare meglio — facendo emergere ciò che ti sfugge, sfidando le tue assunzioni, connettendo ciò che non avresti mai collegato, sintetizzando pattern che non hai chiesto.

Ha 4 layer: **Layer 1** (21 comandi) — operazioni, Claude ricorda tutto; **Layer 2** (4 comandi) — thinking tools, sfida le tue idee e fa emergere pattern nascosti; **Layer 3** (1 comando) — Context Engine, Claude sa chi sei; **Layer 4** (5 comandi) — Research Toolkit, Claude tira dentro nuova conoscenza.

---

### 🥉 3. `Ar9av/obsidian-wiki`
🔗 **https://github.com/Ar9av/obsidian-wiki**

Framework per agenti AI per costruire e mantenere una wiki Obsidian usando il pattern LLM Wiki di Karpathy.

---

### 🏅 4. `huytieu/COG-second-brain` ⭐ LA PIÙ COMPLESSA
🔗 **https://github.com/huytieu/COG-second-brain**

**Self-evolving second brain con 17 AI skills, 6 worker agents, e people CRM** — ispirato a Garry Tan's gstack e gbrain. Funziona con Claude Code, Cursor, Kiro, Gemini CLI, Codex.

Si ispira a: **Zettelkasten** (note atomiche e intercollegabili come fondamento della conoscenza), **Building a Second Brain** di Tiago Forte (organizzazione PARA, progressive summarization), **GTD** di David Allen (cattura tutto, processa sistematicamente).

---

### 🏅 5. `jamesmcroft/obsidian-ai-second-brain`
🔗 **https://github.com/jamesmcroft/obsidian-ai-second-brain**

Starter template per costruire un Second Brain AI-augmented usando Obsidian, il metodo CODE/PARA, e AI skills, inclusi template, query e istruzioni AI per iniziare.

Le **custom skills** sono instruction set dettagliate e riutilizzabili, salvate come markdown, che dicono agli agenti AI esattamente come eseguire specifici workflow di conoscenza. Le skill non sono semplici prompt — codificano i percorsi reali delle cartelle del tuo vault, le strutture dei template e le convenzioni di cross-linking, producendo output affidabile e radicato invece di supposizioni allucinatorie.

---

### 🏅 6. `your-papa/obsidian-Smart2Brain` (Plugin Obsidian diretto)
🔗 **https://github.com/your-papa/obsidian-Smart2Brain**

**Smart Second Brain** è un plugin Obsidian gratuito e open-source per migliorare la gestione della conoscenza. Funziona come assistente personale, alimentato da LLM come ChatGPT o Llama2. Le performance dipendono dall'LLM scelto. — Attenzione: questo usa RAG classico, non il pattern Wiki.

---

### 🏅 7. `khoj-ai/khoj` (Self-hosted, il più completo in assoluto)
🔗 **https://github.com/khoj-ai/khoj**

Chatta con qualsiasi LLM locale o online (llama3, qwen, gemma, mistral, gpt, claude, gemini, deepseek). Ottieni risposte da internet e dai tuoi documenti (immagini, PDF, markdown, Notion, Word). Accessibile da Browser, Obsidian, Desktop, Telefono o WhatsApp. Crea agenti con conoscenza custom, persona e strumenti. Automatizza la ricerca ripetitiva.

---

## 🚀 GUIDA PRATICA — Come iniziare OGGI

### Step 1: Installa i prerequisiti
1. **Obsidian** → scarica da obsidian.md (gratis)
2. **Claude Code** → il CLI di Anthropic (o in alternativa Cursor, Gemini CLI, Codex)
3. **Obsidian Web Clipper** → estensione browser

### Step 2: Clona la repository base
```bash
# La più semplice per iniziare:
npm install -g @nicholasspisak/second-brain
# Poi apri il tuo agente AI e digita:
/second-brain
```

### Step 3: Configura la struttura
Inizia con un vault fresco in Obsidian. Un nome letterale come `toolnerd-secondbrain` funziona bene perché è facile da referenziare nel terminale, nel tuo coding tool e nelle impostazioni del Web Clipper. Tieni il vault **locale**. Questo ti dà cartelle e file ordinari sottostanti, che è esattamente quello che vuoi quando un agente legge da `raw/` e scrive in `wiki/`.

### Step 4: Il flusso di lavoro quotidiano
Le operazioni giornaliere sono semplici slash commands: `/ingest-url` (dagli un URL, Claude estrae l'articolo e lo compila nella wiki, toccando 5-15 pagine in un singolo passaggio), `/process-inbox` (pensieri veloci e note vengono classificati e integrati automaticamente), e `/lint-wiki` (health check che trova link rotti, pagine orfane, contraddizioni e gap di contenuto).

---

## ⚖️ CONFRONTO FINALE ONESTO — Quale scegliere?

| | RAG | Agentic RAG | Wiki/Second Brain |
|---|---|---|---|
| **Difficoltà setup** | Media | Alta | Bassa |
| **Costo** | Medio | Alto | Basso |
| **Scala** | Enterprise | Enterprise | Personale/Team piccolo |
| **Manutenzione** | Manuale | Semi-auto | Automatica (LLM) |
| **Compounding** | ❌ | Parziale | ✅ Si compone nel tempo |
| **Trasparenza** | Bassa | Media | Alta (tutto leggibile) |
| **Best per** | Grandi dataset aziendali | Query complesse multi-step | Il tuo secondo cervello personale |

Per chi sta valutando cosa costruire: la risposta onesta è — **inizia con il pattern Wiki, e passa al RAG solo quando la context window diventa un bottleneck reale**, non ipotetico.

---

## 💡 Il Concetto più Profondo (da capire davvero)

**La parte tediosa del mantenere una knowledge base non è la lettura o il pensiero — è il bookkeeping**: aggiornare i cross-reference, tenere i riassunti aggiornati, notare quando nuovi dati contraddicono vecchie affermazioni, mantenere la coerenza tra decine di pagine. **Gli esseri umani abbandonano le wiki perché il peso della manutenzione cresce più velocemente del valore**.

E questa è esattamente la ragione per cui il pattern LLM Wiki è una rivoluzione: delega all'LLM esattamente la parte che gli umani odiano fare. Tu pensi, esplori, fai domande — lui organizza, collega, sintetizza.

**Link fondamentale da salvare subito:** 🔗 https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f — il Gist originale di Karpathy, il punto di partenza di tutto.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
