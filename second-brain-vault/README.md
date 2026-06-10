# 🧠 Digital Empire — Second Brain Wiki

L'infrastruttura di conoscenza di Digital Empire. Un sistema intelligente dove tu aggiungi conoscenza, io la compilo, e il grafo diventa sempre più intelligente.

---

## 🎯 Cos'è Questo?

**Una wiki auto-mantenuta** dove:
- Tutto ciò che sai su Digital Empire (agenzia, info products, SaaS, marketing, AI) è **strutturato e interconnesso**
- Quando aggiungi una nuova fonte/insight, **io la compilo automaticamente** in pagine con cross-linking
- Ogni pagina sa parlare alle altre — non sono note isolate
- Il sistema **cresce e migliora ogni giorno**

È il sistema di **Andrej Karpathy** (OpenAI, Tesla), usato dalle migliori menti per gestire la loro conoscenza personale. Ora lo usi tu.

---

## 📊 In Numeri (Visione)

| Metrica | Attualmente | Mese 1 | Trimestre 1 |
|---|---|---|---|
| **Pagine** | 0 | ~50-100 | 200+ |
| **Interconnessioni** | 0 | ~200 | 1000+ |
| **Tempo setup** | ✅ Fatto | — | — |
| **Valore per te** | Infra pronta | Vera knowledge base | Consulente che conosce tutto di DE |

---

## 🏗️ Architettura in 60 Secondi

```
┌─────────────────────────────────────────────────┐
│            DIGITAL EMPIRE                       │
├─────────────────────────────────────────────────┤
│                                                 │
│  RAW/ (Tu metti qui)                           │
│  ├─ Articoli, PDF, file, link, note raw        │
│  └─ Formato libero, nessun vincolo             │
│         ↓↓↓ (Io elaboro) ↓↓↓                   │
│  WIKI/ (Io gestisco qui)                       │
│  ├─ Sources/ — Sintesi risorse esterne         │
│  ├─ Entities/ — Persone, aziende, tool         │
│  ├─ Concepts/ — Framework, teorie              │
│  ├─ Synthesis/ — Confronti cross-domain        │
│  ├─ Projects/ — I vostri progetti              │
│  ├─ Metrics/ — KPI e dati                      │
│  ├─ Tools/ — Software che usi                  │
│  ├─ index.md — Catalogo master (auto)          │
│  └─ log.md — Registro operazioni (auto)        │
│         ↓↓↓ (Tu leggi) ↓↓↓                     │
│  OBSIDIAN (Tu naviga qui)                      │
│  ├─ Apri i link, vedi il grafo                 │
│  ├─ Naviga le connessioni                      │
│  └─ Scopri insight nascosti                    │
│         ↓↓↓ (Io conosco) ↓↓↓                   │
│  CLAUDE CODE (Io rispondi sapendo)             │
│  ├─ Carichi il contesto di DE                  │
│  ├─ Faccio risposte consapevoli                │
│  └─ Reference le pagine usate                  │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🚀 Flusso di Lavoro (Il Ciclo)

```
1. TU AGGIUNGI CONOSCENZA
   "Questo articolo su AI for marketing mi piace"
   → Metti link in raw/
   
2. IO PROCESSO
   "/ingest-url https://..."
   → Estraggo insights
   → Compilo in wiki/sources/
   → Collego a 5-10 pagine esistenti
   
3. TU NAVIGHI (Obsidian)
   → Vedi le nuove pagine
   → Clicca sui link, scopri connessioni
   → Capisci il contesto più profondo
   
4. TU CHIEDI (A me, Claude Code)
   "Basandomi su tutto quello che sai, come lancio il prossimo corso?"
   → Io carico il contesto automaticamente
   → Ti do una risposta consapevole di Digital Empire
   → Reference alle pagine rilevanti
   
5. COMPOUNDING
   → Ogni nuova pagina rende tutte le altre più intelligenti
   → Ogni interrogazione ti migliora il pensiero
   → La wiki diventa il tuo vantaggio competitivo
```

---

## 📚 Documenti Principali

| File | Cosa Leggi | Quando |
|---|---|---|
| **QUICKSTART.md** | Come partire in 5 min | Subito, ora |
| **GUIDA_OPERATIVA.md** | Workflow dettagliato + FAQ | Oggi, prima di usare |
| **CLAUDE.md** | Come funziona internamente | Reference, leggi come serve |
| **wiki/index.md** | Catalogo di tutte le pagine | Sempre, per orientarti |
| **wiki/log.md** | Registro di operazioni | Ogni settimana, vedi la storia |

---

## ⚡ I 6 Comandi Che Userai

Tutti questi li capisco e so come rispondere:

```bash
/ingest-url [URL]              # Aggiungi un articolo
/ingest-batch                  # Processa tutto in raw/
/query-wiki [domanda]          # Domanda alla wiki
/lint-wiki                     # Health check (settimanale)
/synthesize-domains            # Trovi pattern cross-agenzia
/research-topic [tema]         # Approfondimento nuovo
```

Non serve memorizzarli. Possiamo anche usare linguaggio naturale, capisco lo stesso.

---

## 🎯 Casi d'Uso (Esempi Reali)

### Caso 1: Stai Lanciando un Nuovo Corso
```
Tu: "Lanciamo il corso Skill Beast v2. Qual è la strategia?"

Io (automaticamente):
  1. Carico [[Project: Lancio Skill Beast v1]] (learnings precedenti)
  2. Carico [[Concept: Funnel info products]]
  3. Carico [[Metric: Conversion rates corsi precedenti]]
  4. Carico [[Synthesis: Confronto funnel agenzia vs corsi]]
  5. Ti do una strategia basata su TUTTA la conoscenza di DE
  
Risposta:
  "Per Skill Beast v2, raccomando:
   - Email sequence: come in [[Project: SB v1]] ma ottimizzato
   - Landing page: testare questo messaggio (è emerso da [[Synthesis: ...]])
   - Timing: lanciare con le stesse metriche di successo ([[Metric: ...]])"
```

### Caso 2: Vedi Competitor Fare Qualcosa di Interessante
```
Tu: "Ho visto che Competitor X usa questa strategia di pricing"
     "/ingest-url [link al loro sito]"

Io:
  1. Scrape il loro sito
  2. Compilo in [[Entity: Competitor X]]
  3. Creo [[Synthesis: Confronto pricing nostro vs Competitor X]]
  4. Aggiorno [[Concept: Pricing strategies]]
  5. Noti automaticamente come rientra nel vostro modello
```

### Caso 3: Notare Pattern Nascosti
```
Tu: "Voglio capire se c'è una connessione tra retention clienti 
     agenzia e performance dei loro siti"

Io:
  1. Carico [[Project: Clienti agenzia]]
  2. Carico [[Metric: Retention agenzia]]
  3. Carico [[Metric: Performance siti (bounce rate, ecc)]]
  4. Connetto i dati e noto il pattern
  5. Ti segnalo: "Guarda, c'è una correlazione qui"
  6. Creo [[Synthesis: Retention agenzia ← Performance siti]]
```

---

## 🧬 Come Funziona il Compounding

```
Settimana 1:
  Aggiungi: 5 file → Wiki ha 20 pagine

Settimana 2:
  Aggiungi: 10 file + 2 articoli
  → Wiki ha 50 pagine TOTALI
  → Ma le nuove pagine sono collegate a 20 pagine precedenti
  → Il grafo è 3x più denso
  → Mie risposte 3x migliori

Settimana 4:
  Wiki ha 100+ pagine, 500+ link
  → Un'idea nuova che dai "tocca" altre 10 pagine automaticamente
  → Scopri connessioni che non avresti visto
  → È come avere un consulente che conosce TUTTO di DE

Mese 3:
  Wiki ha 200+ pagine, 1000+ interconnessioni
  → La wiki CONOSCE il vostro business meglio di chiunque
  → Quando parli di nuova direzione, io vedo tutti i precedenti paralleli
  → Diventa il vostro competitive advantage vero
```

---

## 🛠️ Stack Tecnico

- **Editor**: Obsidian (locale, markdown)
- **Storage**: Cartella normale su disco (locale, nessun cloud)
- **Format**: Markdown plain (leggibile, portable)
- **Agent**: Claude Code (io, che elaboro)
- **Interconnessione**: Link markdown + grafo Obsidian

**Perché questo?** Semplice, affidabile, trasparente. Tutto è leggibile, niente è nascosto.

---

## 🚦 Roadmap Primo Mese

**Week 1:**
- ✅ Setup (già fatto!)
- [ ] Popola raw/ con materiale grezzo DE
- [ ] Primo /ingest-batch
- [ ] Prova /query-wiki

**Week 2:**
- [ ] Aggiungi 10-15 articoli/risorse su marketing, AI, business
- [ ] Vedi il grafo crescere in Obsidian
- [ ] Inizia a notare pattern

**Week 3:**
- [ ] /lint-wiki settimanale
- [ ] /synthesize-domains (guarda agenzia ↔ info products)
- [ ] Primo /research-topic su tema rilevante

**Week 4:**
- [ ] Review totale
- [ ] Decide se architettura va estesa (nuove categorie?)
- [ ] Pianifica expansion trimestrale

---

## 🔐 Privacy & Ownership

- ✅ **La wiki è tua.** Cartella locale nel tuo computer.
- ✅ **Nessuno vede questo** se non vuoi.
- ✅ **Controlli tutto.** Decide tu cosa rimanere privato, cosa no.
- ✅ **Puoi backupizzare** come vuoi (git, cloud, usb).

---

## 💬 FAQ Rapide

**D: Quanto costa?**
R: Nulla. È markdown locale + Claude Code (che hai già).

**D: Quanto tempo occupa manutenzione?**
R: Minimo. Io mantengo tutto. Tu: 5 min/settimana per /lint-wiki.

**D: Posso usare questa wiki con il resto del mio team?**
R: Sì. Puoi condividere la cartella, farla collaborativa, come vuoi.

**D: Come collaboro con il team?**
R: Git + Wiki = collaborazione totale. Ogni membro aggiunge conoscenza, io la compilo.

---

## 🚀 **INIZIA ORA**

1. Leggi **QUICKSTART.md** (5 min)
2. Apri Obsidian, seleziona questa cartella
3. Metti il primo file in `raw/`
4. Scrivi: `/ingest-batch`
5. Guarda la magia

---

## 📞 Dove Sei Adesso

**In questa directory hai:**
```
second-brain-vault/
├── README.md (questo file — punto di partenza)
├── QUICKSTART.md (come partire veloce)
├── GUIDA_OPERATIVA.md (workflow dettagliato)
├── CLAUDE.md (come funziona il sistema)
├── raw/ (dove metti i file)
├── wiki/ (dove vivi la magia)
│   ├── index.md (catalogo master)
│   ├── log.md (registro operazioni)
│   └── [categorie vuote, pronte per essere populate]
└── output/ (report e artefatti)
```

**Prossimo step**: Leggi QUICKSTART.md, poi torniamo qui per il primo ingest.

---

**Creato il**: 2026-04-29  
**Versione**: 1.0 — Production Ready  
**Status**: ✅ Pronto per uso

Benvenuto nel tuo secondo cervello. 🧠
