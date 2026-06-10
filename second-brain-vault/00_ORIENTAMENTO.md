# 🧭 ORIENTAMENTO — Dove Trovaре Cosa

La wiki è pronta. Qui ti spiego dove è tutto.

---

## 📍 I 5 Documenti Che Leggerai Per Primo

### 1. **QUESTO FILE** (che stai leggendo)
- **Cosa è**: Mappa di orientamento
- **Leggi**: 2 min
- **Perché**: Capire dove trovare gli altri documenti

### 2. **README.md**
- **Cosa è**: Porta di ingresso, visione d'insieme del sistema
- **Leggi**: 5 min
- **Quando**: Prima di iniziare
- **Ha**: Architettura, casi d'uso, roadmap

### 3. **QUICKSTART.md**
- **Cosa è**: Come partire in 5 minuti
- **Leggi**: 5 min
- **Quando**: Prima di fare il primo ingest
- **Ha**: Passi concreti, test iniziale

### 4. **GUIDA_OPERATIVA.md**
- **Cosa è**: Workflow dettagliato + FAQ
- **Leggi**: 15 min
- **Quando**: Oggi, prima di usare il sistema
- **Ha**: Scenari reali, come si usa ogni giorno, domande comuni

### 5. **CLAUDE.md**
- **Cosa è**: Configuration del sistema (come io funziono)
- **Leggi**: Come reference (non da leggere tutto d'un fiato)
- **Quando**: Consulta quando hai dubbi su come funziona
- **Ha**: Tutte le operazioni, template, regole

---

## 📚 I Documenti "Di Riferimento" (Consulta Quando Serve)

### **SCHEMA_TEMPLATES.md**
- **Cosa è**: Formato esatto di ogni tipo di pagina
- **Leggi**: Solo le sezioni che servono
- **Quando**: Quando creo una pagina manualmente, o quando vuoi capire il formato
- **Ha**: Template per Sources, Entities, Concepts, Synthesis, Projects, Metrics, Tools

### **ADVANCED_OPERATIONS.md**
- **Cosa è**: Usi sofisticati della wiki
- **Leggi**: Dopo il primo mese
- **Quando**: Quando vuoi usare il sistema al massimo
- **Ha**: Automazioni, batch operations, integrazioni, team collaboration

---

## 🗂️ La Struttura Fisica (Come è Organizzato il Disco)

```
second-brain-vault/                    ← Cartella principale
│
├─ 00_ORIENTAMENTO.md                  ← Questo file (partenza)
├─ README.md                           ← Visione generale
├─ QUICKSTART.md                       ← Come iniziare veloce
├─ GUIDA_OPERATIVA.md                  ← Come usarlo ogni giorno
├─ CLAUDE.md                           ← Configuration (come io funziono)
├─ SCHEMA_TEMPLATES.md                 ← Formato delle pagine
├─ ADVANCED_OPERATIONS.md              ← Usi avanzati
│
├─ raw/                                ← METTI QUI I TUOI FILE
│   ├─ assets/                         ← Immagini, PDF, allegati
│   └─ [I file che aggiungi]
│
├─ wiki/                               ← LA WIKI COMPILATA (Il "prodotto")
│   ├─ index.md                        ← Catalogo master (aggiornato automaticamente)
│   ├─ log.md                          ← Registro operazioni (aggiornato automaticamente)
│   ├─ sources/                        ← Sintesi risorse esterne (le pagine che creo)
│   ├─ entities/                       ← Persone, aziende, tool, competitor
│   ├─ concepts/                       ← Framework, teorie, principi
│   ├─ synthesis/                      ← Confronti, pattern, analisi
│   ├─ projects/                       ← I tuoi progetti attivi
│   ├─ metrics/                        ← KPI e dati
│   ├─ tools/                          ← Software e utility
│   └─ research/                       ← Deep-dive research (futuro)
│
├─ output/                             ← REPORT E ARTEFATTI GENERATI
│   ├─ weekly-reports/                 ← Report settimanali (io li creo)
│   ├─ exports/                        ← PDF, HTML, Markdown esportati
│   └─ presentations/                  ← Presentazioni generate
│
├─ archive/                            ← PAGINE VECCHIE (per reference)
└─ .obsidian/                          ← Configuration Obsidian (non toccare)
```

---

## 🚀 Il Flusso: Primo Mese (Roadmap Concreta)

### **Giorno 1 (Oggi): Setup**
```
☐ Leggi questo file (2 min)
☐ Leggi README.md (5 min)
☐ Leggi QUICKSTART.md (5 min)
☐ Apri Obsidian, connetti a questa cartella (2 min)
☐ Pronto!

Tempo totale: 15 min
```

### **Giorno 2-3: Primo Ingest**
```
☐ Leggi GUIDA_OPERATIVA.md (15 min)
☐ Metti file in raw/ (quello che vuoi ingestire)
☐ Mi scrivi: "/ingest-batch"
☐ Vedi la wiki crescere in Obsidian

Tempo totale: 30 min + attesa
```

### **Settimana 1: Popola**
```
☐ Aggiungi 10-20 file in raw/ (dal tuo materiale di DE)
☐ Esegui /ingest-batch
☐ Fai un test: /query-wiki [domanda su DE]
☐ Naviga il grafo in Obsidian
☐ Prendi confidenza

Tempo totale: 2-3 ore sparse
```

### **Settimana 2: Aggiungi Esterni**
```
☐ Aggiungi 5-10 articoli su trend (marketing, AI, business)
☐ /ingest-url [URL] per ognuno
☐ Guarda come si connettono alla wiki

Tempo totale: 1 ora
```

### **Settimana 3: Manutenzione**
```
☐ /lint-wiki (find e fix problemi)
☐ /synthesize-domains (scopri pattern)
☐ Mi proponi: /research-topic [tema nuovo]

Tempo totale: 30 min
```

### **Settimana 4: Review**
```
☐ Guarda tutte le pagine create
☐ Aggiorna dati/metriche attuali
☐ Decidi se l'architettura è ancora okay
☐ Pianifica il prossimo mese

Tempo totale: 1 ora
```

---

## 🎯 I Tre Comandi che Userai Subito

```bash
/ingest-url [URL]      ← Aggiungi un articolo
/query-wiki [domanda]  ← Chiedi alla wiki  
/lint-wiki             ← Verifica salute della wiki
```

Basta. Inizia con questi tre. Tutto il resto viene dopo.

---

## ❓ Domande Tipiche (E Dove Trovare Risposte)

| Domanda | Dove trovare risposta |
|---|---|
| "Come faccio a iniziare?" | QUICKSTART.md |
| "Come usi il sistema ogni giorno?" | GUIDA_OPERATIVA.md (sezione Workflow) |
| "Quali comandi posso usare?" | GUIDA_OPERATIVA.md (sezione Slash Command) o CLAUDE.md (sezione Operazioni) |
| "Qual è il formato esatto di una pagina?" | SCHEMA_TEMPLATES.md |
| "Come funziona il compounding?" | README.md (sezione Compounding) |
| "Posso usarlo in team?" | ADVANCED_OPERATIONS.md (sezione Team Collaboration) |
| "Come faccio export/report?" | ADVANCED_OPERATIONS.md (sezione Reporting & Export) |
| "Cosa fare quando non so dove trovare qualcosa?" | Questo file (ORIENTAMENTO) |

---

## 🎬 Il Tuo Primo Passo (Adesso)

Scegli uno:

### Opzione A: Quicker (10 min)
1. Leggi QUICKSTART.md
2. Apri Obsidian
3. Torna qui

### Opzione B: Completo (30 min)
1. Leggi README.md
2. Leggi QUICKSTART.md
3. Leggi GUIDA_OPERATIVA.md
4. Apri Obsidian
5. Torna qui

**Raccomandazione**: Opzione B. Sono 30 min ben spesi.

---

## 📊 Documento Summary

| Documento | Lunghezza | Priorità | Tempo |
|---|---|---|---|
| 00_ORIENTAMENTO | 📄 Breve | ⭐⭐⭐⭐⭐ | 5 min |
| README | 📄 Medio | ⭐⭐⭐⭐⭐ | 10 min |
| QUICKSTART | 📄 Breve | ⭐⭐⭐⭐⭐ | 5 min |
| GUIDA_OPERATIVA | 📋 Lungo | ⭐⭐⭐⭐ | 20 min |
| CLAUDE | 📋 Lungo | ⭐⭐⭐ | Reference |
| SCHEMA_TEMPLATES | 📋 Lungo | ⭐⭐⭐ | Reference |
| ADVANCED_OPERATIONS | 📋 Lungo | ⭐⭐ | After 1 month |

---

## ✅ Checklist: Prima di Iniziare

- [ ] Ho letto questo file (ORIENTAMENTO)
- [ ] Ho letto README.md
- [ ] Ho letto QUICKSTART.md
- [ ] Ho aperto Obsidian e selezionato `second-brain-vault`
- [ ] Vedo la struttura di cartelle (raw/, wiki/, output/)
- [ ] Ho visto che wiki/index.md esiste
- [ ] Pronto per il primo ingest

Se tutte le spunte sono fatte, sei pronto a iniziare.

---

## 🚀 Next: Torna al QUICKSTART

Una volta letto questo, leggi **QUICKSTART.md** (5 minuti).

Poi:
```
1. Metti un file test in raw/
2. Scrivi qui: /ingest-batch
3. Vedi la magia in Obsidian
```

---

**File**: 00_ORIENTAMENTO.md  
**Scritto**: 2026-04-29  
**Versione**: 1.0  
**Uso**: Punto di partenza per tutto
