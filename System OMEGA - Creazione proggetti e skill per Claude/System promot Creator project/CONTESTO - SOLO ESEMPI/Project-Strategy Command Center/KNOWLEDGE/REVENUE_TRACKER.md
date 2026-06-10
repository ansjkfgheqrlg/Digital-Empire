# ═══════════════════════════════════════════════════════════════
# 📄 REVENUE_TRACKER.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: DATA_HANDLING
# Priorità: P1 — CRITICO
# Dipendenze: DASHBOARD_ENGINE.md (i dati mensili vengono dalla dashboard), GERARCHIA_PILLAR.md (per verificare la distribuzione %)
# Referenziato da: Custom Instructions — Sezione 5.2, Sezione 8.3 (Step 6)
# ═══════════════════════════════════════════════════════════════

## 📋 SCOPO

Questo file è il database storico del revenue di Digital Empire. Raccoglie i dati di revenue per pillar per ogni mese dall'inizio, permettendo trend analysis, confronti temporali, previsioni e identificazione di pattern stagionali.

Senza storico → ogni mese è un'isola. Con storico → ogni mese è un punto su una curva. La curva racconta la storia del business meglio di qualsiasi singolo numero.

Principio fondante: "Il trend conta più del singolo dato. Un mese da €5.000 dopo 3 mesi da €2.000 è crescita. Un mese da €5.000 dopo 3 mesi da €7.000 è declino. Il numero è lo stesso. Il trend è opposto."

---

## 📖 CONTENUTO PRINCIPALE

### 1. REVENUE MENSILE PER PILLAR
═══════════════════════════════════════════════════════════
TABELLA REVENUE MENSILE — DIGITAL EMPIRE
Ultimo aggiornamento: [DATA]
═══════════════════════════════════════════════════════════

┌───────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Mese/Anno │ Agenzia │ Info-Biz │ YouTube │ KDP │ AI Inf. │ Altro │ TOTALE │
│ │ CRO │ │ │ │ │ │ │
├───────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
│ [MM/AAAA] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │
└───────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

ISTRUZIONI:

Aggiungi 1 riga alla fine di ogni mese (nella review mensile Step 6)
Non cancellare mai righe — lo storico è sacro
Se un dato è zero → scrivi €0, non lasciare vuoto
Se un pillar non è ancora attivo → scrivi "N/A"
La colonna "Altro" include revenue non classificabile nei pillar
text


### 2. REVENUE TRIMESTRALE (AGGREGATO)
═══════════════════════════════════════════════════════════
TABELLA REVENUE TRIMESTRALE
═══════════════════════════════════════════════════════════

┌───────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Trimestre │ Agenzia │ Info-Biz │ YouTube │ KDP │ AI Inf. │ TOTALE │ vs Q-1 │
├───────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ Q1 [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ — │
│ Q2 [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ [+/-]% │
│ Q3 [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ [+/-]% │
│ Q4 [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ [+/-]% │
├───────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ Q1 [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ [+/-]% │
│ ... │ │ │ │ │ │ │ │
└───────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

ISTRUZIONI:

Si compila alla fine di ogni trimestre (review trimestrale)
Somma i 3 mesi del trimestre per ogni pillar
vs Q-1 = variazione % rispetto al trimestre precedente
Formula: ((Revenue Q attuale - Revenue Q precedente) / Revenue Q precedente) × 100
text


### 3. REVENUE ANNUALE (AGGREGATO)
═══════════════════════════════════════════════════════════
TABELLA REVENUE ANNUALE
═══════════════════════════════════════════════════════════

┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Anno │ Agenzia │ Info-Biz │ YouTube │ KDP │ AI Inf. │ TOTALE │ vs Anno │
│ │ │ │ │ │ │ │ prec. │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ — │
│ [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ [+/-]% │
│ [ANNO] │ €[] │ €[] │ €[] │ €[] │ €[] │ €[] │ [+/-]% │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

text


### 4. DISTRIBUZIONE PERCENTUALE (ULTIMO TRIMESTRE)
═══════════════════════════════════════════════════════════
DISTRIBUZIONE REVENUE — Q[N] [ANNO]
═══════════════════════════════════════════════════════════

┌─────────────────┬──────────┬──────────┬──────────┐
│ Pillar │ % Revenue│ % Target │ Status │
├─────────────────┼──────────┼──────────┼──────────┤
│ Agenzia CRO │ [N]% │ 50-60% │ [🟢🟡🔴] │
│ Info-Business │ [N]% │ 20-30% │ [🟢🟡🔴] │
│ YouTube │ [N]% │ 5-15% │ [🟢🟡🔴] │
│ KDP │ [N]% │ 2-5% │ [🟢🟡🔴] │
│ AI Influencer │ [N]% │ 2-5% │ [🟢🟡🔴⚪]│
└─────────────────┴──────────┴──────────┴──────────┘

ANALISI DISTRIBUZIONE:
├── L'agenzia è nel range 50-60%? [SÌ/NO]
│ SE sopra il 70% → l'info-biz è sotto-sviluppato
│ SE sotto il 40% → l'agenzia sta perdendo peso
│ (potrebbe essere ok se l'info-biz cresce, ma
│ verificare che l'agenzia sia stabile)
├── L'info-biz è nel range 20-30%? [SÌ/NO]
│ SE sotto il 10% → il pillar non sta generando
│ SE sopra il 40% → sta diventando dominante
│ (va bene solo se l'agenzia è stabile)
├── I satellite sono sotto il 10%? [SÌ/NO]
│ SE sopra → stanno rubando focus
└── Il revenue totale è in crescita? [SÌ/NO]
SE NO → quale pillar sta calando?

text


### 5. TREND ANALYSIS
═══════════════════════════════════════════════════════════
ANALISI TREND — TEMPLATE
═══════════════════════════════════════════════════════════

REVENUE TOTALE — TREND ULTIMI 6 MESI:
┌───────────┬──────────┬──────────┬──────────┐
│ Mese │ Revenue │ vs M-1 │ Trend │
├───────────┼──────────┼──────────┼──────────┤
│ [M-5] │ €[] │ — │ — │
│ [M-4] │ €[] │ [+/-]% │ [↑↓→] │
│ [M-3] │ €[] │ [+/-]% │ [↑↓→] │
│ [M-2] │ €[] │ [+/-]% │ [↑↓→] │
│ [M-1] │ €[] │ [+/-]% │ [↑↓→] │
│ [M attuale]│ €[] │ [+/-]% │ [↑↓→] │
└───────────┴──────────┴──────────┴──────────┘

TREND COMPLESSIVO 6 MESI: [↑ Crescita / ↓ Calo / → Stabile / ↗ Crescita lenta / ↘ Calo lento]

REVENUE PER PILLAR — TREND ULTIMI 6 MESI:

Agenzia CRO: [M-5] €__ → [M-4] €__ → [M-3] €__ → [M-2] €__ → [M-1] €__ → [M] €__
Trend: [↑↓→]

Info-Business: [M-5] €__ → [M-4] €__ → [M-3] €__ → [M-2] €__ → [M-1] €__ → [M] €__
Trend: [↑↓→]

YouTube: [M-5] €__ → [M-4] €__ → [M-3] €__ → [M-2] €__ → [M-1] €__ → [M] €__
Trend: [↑↓→]

INSIGHT DAL TREND:
├── Pillar in crescita più rapida: ___________________
├── Pillar in stallo o calo: ________________________
├── Stagionalità notata? ____________________________
│ (es: "Agosto sempre basso", "Q4 sempre forte")
├── Correlazioni tra pillar? ________________________
│ (es: "Quando l'agenzia cresce, l'info-biz cresce
│ 2 mesi dopo — perché più casi studio → più
│ contenuto → più trust")
└── Previsione prossimo mese: €[___]
Basata su: [Trend / Pipeline / Lancio previsto]

REVENUE DA CROSS-POLLINATION — TREND:

┌───────────┬──────────┬──────────┐
│ Trimestre │ Rev Cross│ vs Q-1 │
│ │ Poll │ │
├───────────┼──────────┼──────────┤
│ Q[N-3] │ €[] │ — │
│ Q[N-2] │ €[] │ [+/-]% │
│ Q[N-1] │ €[] │ [+/-]% │
│ Q[N] │ €[] │ [+/-]% │
└───────────┴──────────┴──────────┘

Trend cross-poll: [↑↓→]
SE piatto o in calo → le sinergie non stanno
crescendo. Azione: intensifica cross-pollination.

text


### 6. RECORD E MILESTONE
═══════════════════════════════════════════════════════════
RECORD E MILESTONE DI DIGITAL EMPIRE
═══════════════════════════════════════════════════════════

RECORD DI REVENUE:
├── Best month EVER: [Mese/Anno] — €[]
├── Best quarter EVER: Q[N] [Anno] — €[]
├── Best year EVER: [Anno] — €[]
├── Worst month (dopo l'avvio): [Mese/Anno] — €[]
└── Mese con più crescita %: [Mese/Anno] — [+N]%

RECORD PER PILLAR:
├── Agenzia — Best month: [Mese/Anno] — €[]
├── Info-Biz — Best month: [Mese/Anno] — €[]
├── YouTube — Best month: [Mese/Anno] — €[]
├── KDP — Best month: [Mese/Anno] — €[]
└── AI Inf. — Best month: [Mese/Anno] — €[___]

MILESTONE RAGGIUNTI:
┌─────────────────────────────────┬──────────────────┐
│ Milestone │ Data raggiunta │
├─────────────────────────────────┼──────────────────┤
│ Primo €1.000 in un mese │ [DATA o "—"] │
│ Primo €3.000 in un mese │ [DATA o "—"] │
│ Primo €5.000 in un mese │ [DATA o "—"] │
│ Primo €10.000 in un mese │ [DATA o "—"] │
│ Primo cliente agenzia │ [DATA o "—"] │
│ Primo €1.000 da info-biz │ [DATA o "—"] │
│ Primo lead da YouTube │ [DATA o "—"] │
│ Lista email a 100 lead │ [DATA o "—"] │
│ Lista email a 500 lead │ [DATA o "—"] │
│ Lista email a 1.000 lead │ [DATA o "—"] │
│ 10 clienti agenzia cumulativi │ [DATA o "—"] │
│ 5 prodotti info attivi │ [DATA o "—"] │
│ 1.000 iscritti YouTube │ [DATA o "—"] │
│ Primo €100.000 annuali │ [DATA o "—"] │
└─────────────────────────────────┴──────────────────┘

NOTA: Celebra ogni milestone. La crescita è un
processo lungo. Ogni milestone raggiunto è la prova
che il sistema funziona.

text


---

## 🔧 COME UTILIZZARE QUESTO FILE

**Quando consultarlo:**
- Nella review mensile (Step 6: Revenue Analysis) → aggiungi 1 riga alla tabella mensile
- Nella review trimestrale → compila la riga trimestrale + trend analysis
- Nella review annuale → compila la riga annuale + milestone
- Quando l'utente chiede "come va il revenue?" o "qual è il trend?"
- Quando serve una previsione per il mese/trimestre successivo

**Come integrare nella risposta:**
1. Usa i dati storici per CONTESTUALIZZARE il dato attuale
2. Non dire "€3.000 questo mese" → dì "€3.000 questo mese, +15% rispetto al mese scorso, in linea con il trend trimestrale"
3. Identifica i trend per pillar separatamente
4. Segnala i record quando vengono battuti → è un momento di celebrazione
5. Se il trend è negativo per 2+ mesi → collega a ALM-1 (SOGLIE_ALLARME.md)

---

## 🔗 COLLEGAMENTI

- **Dipende da**: `KB/DASHBOARD_ENGINE.md` (i dati mensili vengono dalla dashboard compilata)
- **Alimenta**: `KB/RETROSPETTIVA_ENGINE.md` (revenue per la Parte A), `KB/DECISION_FRAMEWORK.md` (trend per le decisioni di allocazione), `KB/SOGLIE_ALLARME.md` (trend negativo → allarme ALM-1)
- **Collegato a**: `KB/GERARCHIA_PILLAR.md` (distribuzione % vs target), `KB/OKR_SYSTEM.md` (KR di revenue)
- **Custom Instructions**: Sezione 5.2, Sezione 8.3 Step 6

---

## 💡 ESEMPI PRATICI

### Esempio: Revenue analysis con contesto storico

**Situazione:** L'utente dice "Questo mese l'agenzia ha fatto €4.200"

**Risposta tipo (con storico):**
REVENUE AGENZIA — Contesto

Questo mese: €4.200
├── vs mese precedente: €3.800 → +10.5% ↑
├── vs 3 mesi fa: €3.000 → +40% ↑
├── Trend 3 mesi: €3.000 → €3.800 → €4.200 → ↑ costante
├── Record personale? €4.200 > €4.000 (record prec.)
│ → 🎉 NUOVO RECORD AGENZIA
└── Proiezione Q: se mantieni €4.200 → €12.600/Q
Target Q: €[___] → Progresso: [N]%

text


---

## ⚠️ NOTE E AVVERTENZE

1. **Non cancellare MAI righe dallo storico.** Anche i mesi brutti fanno parte della storia. Cancellare i dati negativi = autoinganno.

2. **Aggiorna MENSILMENTE.** Se salti 2-3 mesi → i dati diventano inaffidabili (ricordi male i numeri). Nella review mensile, la prima cosa da fare è inserire il revenue.

3. **I milestone sono importanti per la motivazione.** L'imprenditoria è una maratona. Senza milestone celebrati → sembra che non si faccia mai progresso. Celebra ogni riga compilata nella tabella milestone.

4. **La previsione non è una promessa.** Quando fai una previsione basata sul trend, è un'INDICAZIONE, non una certezza. Usala per pianificare, non per vendere.

5. **Se il revenue di un pillar è a €0 per 3+ mesi**, non è un pillar — è un'idea. O lo attivi con azioni concrete (con timeline) o lo rimuovi dalla tabella e lo metti come "Non attivo".
Ora carica questo file, poi subito dopo carica il prossimo qui sotto.

14B — KNOWLEDGE BASE FILE 13: PROJECT_MAP.md
Dove vai
Stesso processo: "Add content" → "Create content"

Se Claude ti permette di dare un nome al file, chiamalo:

text

PROJECT_MAP.md
Cosa fai
Copia e incolla TUTTO il blocco seguente:

Markdown

# ═══════════════════════════════════════════════════════════════
# 🗺️ PROJECT_MAP.md — Mappa Completa del Progetto
# ═══════════════════════════════════════════════════════════════
# P9 — STRATEGY COMMAND CENTER
# Digital Empire Multi-Business Command Hub
# ═══════════════════════════════════════════════════════════════

## 📋 STRUTTURA COMPLETA DEL PROGETTO

### Custom Instructions
- **CUSTOM_INSTRUCTIONS** — Cervello del Command Center. 9 sezioni: Identità, Processi di Ragionamento, Gestione Input, Generazione Output, Utilizzo Knowledge Base, Gestione Errori, Vincoli, Workflow Operativi, Metriche di Qualità.

### Knowledge Base — Indice Completo

| # | Nome File | Categoria | Priorità | Scopo Principale | Sezione CI che lo usa |
|---|-----------|-----------|----------|------------------|-----------------------|
| 1 | `GERARCHIA_PILLAR.md` | CORE_LOGIC | P0 | Gerarchia non negoziabile dei pillar, allocazione tempo, regole di riallocazione, metafora operativa | Sez. 2.1 Step 3, 5.2, 7.3, 8.1, 8.4 |
| 2 | `DASHBOARD_ENGINE.md` | CORE_LOGIC | P0 | Template dashboard completa (7 sezioni), sistema semaforo, dashboard rapida settimanale, albero diagnostico pillar 🔴 | Sez. 2.1 Step 2, 2.2, 4.4, 5.2, 8.1-8.3 |
| 3 | `OKR_SYSTEM.md` | CORE_LOGIC | P0 | Sistema OKR a 3 livelli (annuale→trimestrale→sprint), 7 regole, template compilabili, processo review, guida KR | Sez. 2.2, 5.2, 8.2-8.4 |
| 4 | `CROSS_POLLINATION_ENGINE.md` | CORE_LOGIC | P0 | 12 flussi di sinergia bidirezionali, azioni specifiche per flusso, checklist settimanale, bridge metrics, log azioni | Sez. 2.2, 5.2, 8.2, 8.3, 8.4, 8.5 |
| 5 | `DECISION_FRAMEWORK.md` | PROCESSES | P0 | Processo decisionale 4 step, formula impatto (Gap×Leva×Velocità), decisioni binarie, allocazione risorse, planning Q+1, decision log | Sez. 2.2, 2.4, 5.2, 8.3 |
| 6 | `FILTRO_ANTI_ADD.md` | SAFETY | P0 | Filtro 5 domande anti-distrazione, classificazione idee (5 esiti), protocollo protezione focus, log idee, Not To Do template, metriche focus | Sez. 2.1 Step 6, 3.1-3.2, 6.1, 7.1, 8.3-8.5 |
| 7 | `SOGLIE_ALLARME.md` | SAFETY | P0 | 6 soglie di allarme (4🔴 + 2🟡), protocolli di risposta dettagliati, pannello monitoraggio, combinazioni multi-allarme, storico | Sez. 2.1 Step 5, 2.3, 5.2, 6.3, 8.1-8.2 |
| 8 | `WORKFLOW_CADENZE.md` | PROCESSES | P1 | 5 cadenze operative (giornaliera→annuale), step dettagliati per ogni cadenza, protocollo recupero cadenze saltate | Sez. 8.1-8.5 |
| 9 | `OUTPUT_TEMPLATES.md` | TEMPLATES | P1 | 15 template preconfigurati (T1-T15) per ogni tipo di output: health check, dashboard, OKR, sprint, gap analysis, piano d'azione, cross-poll, filtro ADD, allarme, decisione, review, retrospettiva, revenue | Sez. 4.1-4.4, 5.2 |
| 10 | `PRODUCT_LADDER.md` | DOMAIN_KNOWLEDGE | P1 | Scala prodotti info-biz (5 livelli: €0→€2000+), dettaglio per livello, funnel di ascensione, 5 bridge offers cross-pillar, catalogo master, checklist review | Sez. 5.2, 8.4 Step 4 |
| 11 | `RETROSPETTIVA_ENGINE.md` | PROCESSES | P1 | Template retrospettiva trimestrale (3 parti: Dati→Analisi→Lezioni), template annuale, guida pattern analysis, archivio retrospettive | Sez. 5.2, 8.4 Step 1 |
| 12 | `REVENUE_TRACKER.md` | DATA_HANDLING | P1 | Database storico revenue (mensile/trimestrale/annuale), distribuzione %, trend analysis, record e milestone | Sez. 5.2, 8.3 Step 6 |
| 13 | `PROJECT_MAP.md` | CONFIGURATION | P2 | QUESTO FILE — mappa navigabile del progetto | — |

---

## 🔗 MATRICE DI DIPENDENZE
OGNI FILE — DA CHI DIPENDE E CHI ALIMENTA
═══════════════════════════════════════════

GERARCHIA_PILLAR.md (FONDAZIONE)
├── Dipende da: NESSUNO (è il file radice)
└── Alimenta: TUTTI gli altri file

DASHBOARD_ENGINE.md
├── Dipende da: GERARCHIA_PILLAR
└── Alimenta: OKR_SYSTEM, DECISION_FRAMEWORK,
SOGLIE_ALLARME, REVENUE_TRACKER

OKR_SYSTEM.md
├── Dipende da: GERARCHIA_PILLAR, DASHBOARD_ENGINE
└── Alimenta: DECISION_FRAMEWORK, FILTRO_ANTI_ADD,
WORKFLOW_CADENZE

CROSS_POLLINATION_ENGINE.md
├── Dipende da: GERARCHIA_PILLAR, DASHBOARD_ENGINE
└── Alimenta: OKR_SYSTEM, DECISION_FRAMEWORK

DECISION_FRAMEWORK.md
├── Dipende da: GERARCHIA, DASHBOARD, OKR, SOGLIE
└── Alimenta: OKR_SYSTEM, FILTRO_ANTI_ADD

FILTRO_ANTI_ADD.md
├── Dipende da: GERARCHIA, DASHBOARD, OKR
└── Alimenta: OKR_SYSTEM, DECISION_FRAMEWORK

SOGLIE_ALLARME.md
├── Dipende da: GERARCHIA, DASHBOARD, CROSS_POLL
└── Alimenta: DECISION_FRAMEWORK, OKR_SYSTEM

WORKFLOW_CADENZE.md
├── Dipende da: TUTTI (usa tutti i file nelle cadenze)
└── Alimenta: È il MOTORE che attiva tutto il resto

OUTPUT_TEMPLATES.md
├── Dipende da: TUTTI (i template si riempiono con
│ i dati degli altri file)
└── Alimenta: Tutte le risposte del Command Center

PRODUCT_LADDER.md
├── Dipende da: GERARCHIA, CROSS_POLLINATION
└── Alimenta: DASHBOARD (revenue per livello), OKR

RETROSPETTIVA_ENGINE.md
├── Dipende da: DASHBOARD, OKR, REVENUE, DECISION
└── Alimenta: OKR (lezioni → nuovi OKR), GERARCHIA

REVENUE_TRACKER.md
├── Dipende da: DASHBOARD
└── Alimenta: RETROSPETTIVA, DECISION, SOGLIE

text


---

## 🔄 MAPPA DEI WORKFLOW

| Workflow | Cadenza | File Coinvolti | Trigger |
|----------|---------|---------------|---------|
| Quick Check | Giornaliero | (nessun file — check mentale) | Ogni mattina |
| Review Settimanale | Lunedì, 1.5h | OKR, DASHBOARD, CROSS_POLL, FILTRO_ADD, SOGLIE, OUTPUT_TEMPLATES | Ogni lunedì |
| Review Mensile | Primo lunedì, 3h | DASHBOARD, OKR, DECISION, CROSS_POLL, REVENUE, FILTRO_ADD, OUTPUT_TEMPLATES | Primo lunedì del mese |
| Review Trimestrale | Ultimo venerdì Q, 6h | RETROSPETTIVA, OKR, DECISION, PRODUCT_LADDER, CROSS_POLL, GERARCHIA, FILTRO_ADD, SOGLIE | Fine trimestre |
| Review Annuale | Dicembre/Gennaio, 8h | RETROSPETTIVA, REVENUE, OKR, GERARCHIA, tutti | Fine anno |
| Filtro Anti-ADD | On-demand | FILTRO_ADD, GERARCHIA, DASHBOARD, OKR | Nuova idea/opportunità |
| Allarme | On-demand | SOGLIE, DASHBOARD, GERARCHIA | Soglia superata |
| Decisione | On-demand | DECISION, DASHBOARD, OKR, GERARCHIA | Scelta da fare |

---

## 📊 STATISTICHE DEL PROGETTO

| Metrica | Valore |
|---------|--------|
| File Knowledge Base | 13 |
| Sezioni Custom Instructions | 9 |
| Template Output disponibili | 15 |
| Flussi Cross-Pollination | 12 |
| Soglie di Allarme | 6 |
| Livelli OKR | 3 |
| Cadenze Operative | 5 |
| Livelli Product Ladder | 5 |
| Bridge Offers | 5 |
| Regole OKR | 7 |
| Domande Filtro Anti-ADD | 5 |
| Scenari Edge Case gestiti | 8 |

---

## 🚀 QUICK START — COME INIZIARE
SE È LA PRIMA VOLTA CHE USI IL COMMAND CENTER:
═══════════════════════════════════════════════

SETTIMANA 1:
├── Compila la Dashboard Rapida (T2) con i dati
│ che hai ora (anche approssimativi)
├── Definisci 1 Objective + 3 KR per l'Agenzia
│ (il pillar più importante)
├── Fai il tuo primo Sprint Mensile (7 task)
└── Scegli 1 azione cross-pollination dalla checklist

SETTIMANA 2-4:
├── Fai la review settimanale ogni lunedì (1.5h)
├── 1 azione cross-pollination per settimana
└── Completa i task dello sprint

MESE 2:
├── Compila la Dashboard Completa (T3) con dati reali
├── Definisci gli OKR per gli altri pillar
├── Aggiungi i dati al Revenue Tracker
└── Definisci la Not To Do list

MESE 3 (FINE Q1):
├── Prima Retrospettiva Trimestrale
├── OKR Q2
├── Product Ladder review
└── Il sistema è ATTIVO e in funzione

text


---

## ⚠️ PRINCIPI DI UTILIZZO

1. **GERARCHIA PRIMA DI TUTTO**: Prima di qualsiasi decisione → verifica GERARCHIA_PILLAR.md
2. **DATI PRIMA DI OPINIONI**: Prima di qualsiasi analisi → compila DASHBOARD_ENGINE.md
3. **FOCUS PRIMA DI AZIONE**: Prima di qualsiasi nuova iniziativa → applica FILTRO_ANTI_ADD.md
4. **COSTANZA PRIMA DI INTENSITÀ**: 1 review settimanale ogni settimana > 1 review intensiva ogni 2 mesi
5. **MENO È MEGLIO**: Max 3 priorità/Q, max 7 task/mese, max 1 azione cross-poll/settimana
Ora carica entrambi i file (REVENUE_TRACKER.md e PROJECT_MAP.md), poi leggi la sezione finale qui sotto.

