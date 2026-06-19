# PROJECT_MAP
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > System promot Creator project > CONTESTO - SOLO ESEMPI > Project-Strategy Command Center > KNOWLEDGE]]

## Content

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

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
