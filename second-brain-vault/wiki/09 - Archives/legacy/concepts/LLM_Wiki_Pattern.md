# LLM Wiki — Il Pattern di Andrej Karpathy

- **Categoria**: 📐 Framework / 🔧 Metodologia
- **Origine**: Andrej Karpathy (co-fondatore OpenAI, ex director of AI Tesla)
- **Facilità**: 🟡 Intermedia
- **Applicabilità per DE**: Fondazione del nostro secondo cervello, come creiamo e manteniamo conoscenza
- **Tags**: `#llm-wiki` `#knowledge-base` `#second-brain` `#obsidian` `#karpathy`

## 📖 Definizione

Il **LLM Wiki Pattern** è un metodo rivoluzionario per gestire conoscenza personale. Non scrivi mai la wiki tu stesso — è l'LLM (come Claude) a scriverla e mantenerla completamente. Tu sei responsabile del sourcing e delle domande giuste; l'LLM fa il lavoro pesante: riassumere, cross-referenziare, archiviare, bookkeeping.

Il principio fondamentale: **Non cercatore + RAG tradizionale**, ma **scrittore LLM + markdown strutturato**. L'LLM non solo legge le tue note — le scrive e le mantiene costantemente.

Pubblicato da Karpathy: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## 🧬 Componenti Core

### 1. **Lo Spazio di Lavoro Fisico**
- Un vault Obsidian locale (markdown plain)
- Cartelle: `raw/` (inbox), `wiki/` (la knowledge base compilata), `output/` (report)
- Nessun RAG embeddings — tutto leggibile, transparent

### 2. **Le 3 Operazioni Fondamentali**

**INGEST**: Aggiungi una nuova fonte alla collezione `raw/`. Chiedi all'LLM di processar la:
- Legge la fonte
- Aggiorna pagine esistenti
- Crea pagine nuove dove serve
- Aggiorna indice + log

**QUERY**: Fai domande contro la wiki, non contro file scollegati:
- L'LLM lavora su pagine già strutturate, cross-linkate, sintetizzate
- Risposte migliori perché il contesto è organizzato

**LINT**: Health check sulla wiki:
- Trova claim obsoleti, contraddizioni
- Rileva link mancanti, pagine orfane
- Suggerisce concetti che meritano pagina propria

### 3. **Il File CLAUDE.md — Cuore del Sistema**
È il file di configurazione che dice all'LLM come comportarsi da bibliotecario:
- Architettura della wiki
- Definizione delle operazioni (INGEST, QUERY, LINT, SYNTHESIS, RESEARCH)
- Template per ogni tipo di pagina
- Regole di cross-linking
- Tone, perspective, integration con Claude Code

### 4. **La Struttura della Wiki**
```
vault/
├── raw/              ← Inbox (file che aggiungi)
├── wiki/             ← Knowledge base mantenuta dall'LLM
│   ├── sources/      ← Sintesi risorse esterne
│   ├── entities/     ← Persone, aziende, tool
│   ├── concepts/     ← Idee, framework, teorie
│   ├── synthesis/    ← Confronti, pattern cross-domain
│   ├── projects/     ← Progetti attivi
│   ├── metrics/      ← KPI, dati
│   ├── tools/        ← Software usati
│   ├── index.md      ← Catalogo master (auto)
│   └── log.md        ← Registro operazioni (auto)
├── output/           ← Report generati
└── CLAUDE.md         ← Configuration
```

## 🎯 Come Lo Applichiamo in Digital Empire

Usiamo il pattern per trasformare tutta la conoscenza di DE (strategie, progetti, learnings, tool, competitor intel) in una rete interconnessa che migliora ogni giorno:

1. **Scarico conoscenza grezza** in `raw/` (file, PDF, documenti, materiale di marketing, formazione, contesto)
2. **Inizio INGEST** → classifico, compilo, creo pagine nella wiki, collego tutto
3. **Le pagine crescono** → ogni nuova risorsa tocca 5-15 pagine esistenti
4. **Il grafo diventa intelligente** → quando chiedo qualcosa, ho contesto completo di DE

Quando lanciamo un nuovo corso (es. Claude Code Mastery):
- Carico [[Claude_Code_Mastery_Launch]] ← strategia, timeline, team
- Carico  ← metodologia provata
- Carico  ← cosa ha funzionato
- Carico  ← baseline per il progetto

Risultato: una risposta che sa TUTTO di DE e di come lanciaremo questo corso.

## ⚡ Varianti / Critiche

**Variante: Advanced Repository Systems**
- `eugeniughelbur/obsidian-second-brain` — 4 layer, 25+ comandi
- `huytieu/COG-second-brain` — 17 AI skills, 6 worker agents
- `jamesmcroft/obsidian-ai-second-brain` — Template + skill instructions

Tutte basate su Karpathy ma estese con automazioni, team collaboration, research toolkit.

**Obiezione: "E se l'LLM allucinata?"**
- Il sistema è robusto perché:
  - Testo markdown plain è leggibile (tu controlli sempre)
  - Cross-link = consistenza verificabile (link a pagine che non esistono si vedono)
  - LINT rileva incoerenze automaticamente
  - La wiki mantiene il source material originale in `raw/`

**Limite: Quando NON usare**
- Per dati che cambiano ogni ora (live dashboards) — usare database
- Per discussioni in tempo reale con il team — usare Slack
- Per dataset enormi (milioni di record) — usare warehouse + RAG

## 📊 Metriche Associate

- 
- 
- 
- 

## 🔗 Correlazioni

- Fondamento per  — note atomiche e interconnesse
- Ispirato da  — PARA methodology
- Implementato con  — editor locale markdown
- Mantenuto da 
- Usato per [[Digital_Empire_Agency_Strategy]]

## 💻 Tool che lo Implementano

-  — Editor locale, graph view
- [[Manuale_Claude_Code_Product]] — Agente che scrive e mantiene le pagine
-  — Web to raw/ automatico (opzionale)
-  — Versioning per team collaboration (opzionale)

## 📚 Risorse Essenziali

- **Gist originale**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Repository di base**: https://github.com/NicholasSpisak/second-brain
- **Sistema avanzato**: https://github.com/huytieu/COG-second-brain
- **Con skill definitions**: https://github.com/jamesmcroft/obsidian-ai-second-brain

## 📍 Metadata

- **Date Added**: 2026-04-29
- **Mastery Level**: 🟢 Esperto (è la base di tutto ciò che facciamo)
- **Use Count**: Sistema fondante — usato in tutti i progetti
- **Confidence**: Alta
- **Next Review**: 2026-05-13 (dopo primo mese di uso)
