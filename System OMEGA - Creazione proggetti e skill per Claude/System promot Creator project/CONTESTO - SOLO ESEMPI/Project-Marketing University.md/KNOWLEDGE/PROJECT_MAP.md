# ═══════════════════════════════════════════════════════════════
# 🗺️ PROJECT MAP — Marketing University
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Progetto: Marketing University — Biblioteca Operativa di Formazione Marketing
# Ultimo Aggiornamento: [Data di creazione]
# ═══════════════════════════════════════════════════════════════

## 📋 PANORAMICA DEL PROGETTO

Marketing University è un sistema operativo di apprendimento che trasforma
materiale formativo (corsi, libri, guide, video, documenti) in framework
azionabili, li cataloga in una biblioteca strutturata a 6 aree, li collega
ai 5 progetti attivi di Digital Empire, e ne traccia l'applicazione nel tempo.

### Ciclo Operativo Fondamentale
MATERIALE → STUDIO → ESTRAZIONE → CATALOGAZIONE → COLLEGAMENTO → APPLICAZIONE → VALIDAZIONE → INSEGNAMENTO
↓ ↓ ↓ ↓
Scheda Framework Progetto Target Risultato Contenuto
Misurabile (Video/Libro/Post)

text


---

## 📚 STRUTTURA COMPLETA DEL PROGETTO

### 🧠 Custom Instructions (System Prompt)

| File | Scopo | Sezioni Principali |
|------|-------|--------------------|
| `CUSTOM_INSTRUCTIONS.md` | Definisce identità, comportamento, processi di ragionamento e workflow dell'AI | 9 sezioni: Identità, Ragionamento, Input, Output, KB Usage, Errori, Vincoli, Workflow, Qualità |

### 📚 Knowledge Base — Indice Completo dei File

| # | Nome File | Categoria | Priorità | Righe Stimate | Collegamento CI | Scopo |
|---|-----------|-----------|----------|---------------|-----------------|-------|
| 1 | `PROJECT_MAP.md` | NAVIGAZIONE | P0 | ~250 | Sezione 5.1 | Indice navigabile dell'intero progetto |
| 2 | `KB_01_LIBRARY_ARCHITECTURE.md` | CORE_LOGIC | P0 | ~450 | Sezione 2.1, 5.2, 8.1 | Struttura completa delle 6 aree × 4 sottoaree della biblioteca |
| 3 | `KB_02_EXTRACTION_ENGINE.md` | PROCESSES | P0 | ~400 | Sezione 2.2, 8.1 | Protocollo di estrazione framework + template scheda + esempi |
| 4 | `KB_03_PROJECT_CONNECTION_MATRIX.md` | CORE_LOGIC | P0 | ~300 | Sezione 2.3, 5.2, 8.1 | Matrice di collegamento area → progetto + trigger |
| 5 | `KB_04_STUDY_METHOD_PIPELINE.md` | PROCESSES | P0 | ~350 | Sezione 2.2, 8.1 | Metodo a 5 step (Studia → Estrai → Applica → Valida → Insegna) |
| 6 | `KB_05_WEEKLY_MONTHLY_ROUTINE.md` | PROCESSES | P1 | ~250 | Sezione 8.2 | Calendario studio settimanale + review mensile |
| 7 | `KB_06_RESPONSE_TEMPLATES.md` | TEMPLATES | P0 | ~500 | Sezione 4.1, 4.2 | Template output per ogni tipo di interazione |
| 8 | `KB_07_QUICK_REFERENCE_PROTOCOL.md` | PROCESSES | P1 | ~200 | Sezione 8.2 | Protocollo di ricerca rapida nella biblioteca |
| 9 | `KB_08_FRAMEWORKS_REGISTRY.md` | DATA_HANDLING | P0 | ~300 | Sezione 2.2, 5.2 | Registro strutturato dei framework estratti + tracking status |
| 10 | `KB_09_STUDY_PRIORITY_ENGINE.md` | CORE_LOGIC | P1 | ~300 | Sezione 2.4, 8.2 | Motore decisionale per suggerire cosa studiare |
| 11 | `KB_10_QUALITY_VALIDATION.md` | CONFIGURATION | P1 | ~250 | Sezione 9.1, 9.2 | Metriche di qualità + checklist validazione |
| 12 | `KB_11_SYSTEM_RULES_AND_EDGE_CASES.md` | SAFETY | P1 | ~300 | Sezione 6, 7 | Regole inviolabili + gestione scenari anomali |
| 13 | `KB_12_SETUP_AND_ONBOARDING.md` | PROCESSES | P1 | ~250 | Sezione 8.3 | Protocollo setup prima settimana + caricamento materiale |
| 14 | `KB_13_DOMAIN_GLOSSARY.md` | DOMAIN_KNOWLEDGE | P2 | ~200 | Sezione 5.4 | Glossario termini marketing + definizioni operative |
| 15 | `KB_14_PRELOADED_FRAMEWORKS.md` | DATA_HANDLING | P1 | ~400 | Sezione 5.2, 8.1 | Framework pre-estratti dai documenti già in possesso |

---

## 🔗 MATRICE DI DIPENDENZE TRA FILE

| File | Dipende Da | Alimenta | Criticità |
|------|-----------|----------|-----------|
| `PROJECT_MAP.md` | Nessuno | Tutti (navigazione) | P0 — Indice |
| `KB_01_LIBRARY_ARCHITECTURE.md` | Nessuno | KB_02, KB_03, KB_07, KB_08, KB_09, KB_14 | P0 — Fondazione |
| `KB_02_EXTRACTION_ENGINE.md` | KB_01 | KB_08, KB_06 | P0 — Processo Core |
| `KB_03_PROJECT_CONNECTION_MATRIX.md` | KB_01 | KB_02, KB_09, KB_06 | P0 — Routing |
| `KB_04_STUDY_METHOD_PIPELINE.md` | KB_02, KB_03 | KB_05, KB_06 | P0 — Metodo |
| `KB_05_WEEKLY_MONTHLY_ROUTINE.md` | KB_04 | KB_06, KB_10 | P1 — Calendario |
| `KB_06_RESPONSE_TEMPLATES.md` | KB_02, KB_03, KB_04, KB_08 | Nessuno (output finale) | P0 — Output |
| `KB_07_QUICK_REFERENCE_PROTOCOL.md` | KB_01, KB_08 | KB_06 | P1 — Ricerca |
| `KB_08_FRAMEWORKS_REGISTRY.md` | KB_01, KB_02 | KB_07, KB_09, KB_06 | P0 — Database |
| `KB_09_STUDY_PRIORITY_ENGINE.md` | KB_01, KB_03, KB_08 | KB_06 | P1 — Decisioni |
| `KB_10_QUALITY_VALIDATION.md` | KB_02, KB_04 | KB_06 | P1 — Qualità |
| `KB_11_SYSTEM_RULES_AND_EDGE_CASES.md` | Nessuno | Tutti (vincoli) | P1 — Safety |
| `KB_12_SETUP_AND_ONBOARDING.md` | KB_01, KB_02, KB_04 | KB_08, KB_14 | P1 — Setup |
| `KB_13_DOMAIN_GLOSSARY.md` | Nessuno | Tutti (terminologia) | P2 — Reference |
| `KB_14_PRELOADED_FRAMEWORKS.md` | KB_01, KB_02, KB_03 | KB_08 | P1 — Contenuto Iniziale |

---

## 🔄 MAPPA DEI WORKFLOW

| # | Workflow | File Coinvolti | Trigger | Output |
|---|----------|---------------|---------|--------|
| W1 | Analisi Materiale Nuovo | KB_01, KB_02, KB_03, KB_06, KB_08 | Utente fornisce materiale formativo | Schede Framework Estratto catalogate |
| W2 | Ricerca Framework Rapida | KB_01, KB_07, KB_08, KB_06 | Utente chiede un concetto/framework specifico | Framework step-by-step + esempio + applicazione |
| W3 | Suggerimento Studio | KB_01, KB_03, KB_08, KB_09, KB_06 | Utente chiede "cosa studiare questa settimana" | Problema → Area → Materiale → Azione prevista |
| W4 | Review Settimanale | KB_05, KB_08, KB_10, KB_06 | Venerdì (check applicazione) | Status aggiornamento schede + blocchi identificati |
| W5 | Review Mensile | KB_05, KB_08, KB_09, KB_10, KB_06 | Primo lunedì del mese | Report statistiche + gap + priorità mese prossimo |
| W6 | Validazione Framework | KB_04, KB_08, KB_10, KB_06 | 30 giorni dopo applicazione | Status Validato/Non Validato + documentazione risultati |

---

## 🔀 MATRICE DI ROUTING — TIPO DI RICHIESTA → WORKFLOW

| Tipo di Richiesta dell'Utente | Workflow Attivato | File KB Primari | Sezione CI |
|-------------------------------|-------------------|-----------------|------------|
| "Analizza questo materiale / corso / libro" | W1 — Analisi Materiale | KB_02, KB_03, KB_08 | 8.1 |
| "Cerca / Trovami il framework per..." | W2 — Ricerca Rapida | KB_07, KB_08 | 8.2 |
| "Cosa dovrei studiare?" | W3 — Suggerimento Studio | KB_09, KB_03 | 8.2 |
| "Review settimanale" | W4 — Review Settimanale | KB_05, KB_08, KB_10 | 8.2 |
| "Review mensile" | W5 — Review Mensile | KB_05, KB_08, KB_09 | 8.2 |
| "Questo framework ha funzionato / non ha funzionato" | W6 — Validazione | KB_04, KB_08, KB_10 | 8.2 |
| "Aggiungi alla biblioteca" | W1 (sottoprocesso) | KB_01, KB_08 | 8.1 |
| "Mostra tutti i framework dell'area X" | W2 (variante) | KB_01, KB_08 | 8.2 |
| "Collega questo concetto al progetto X" | W1 (sottoprocesso) | KB_03 | 8.1 |
| Materiale formativo inviato senza istruzioni | W1 — Analisi Materiale (default) | KB_02, KB_03, KB_08 | 8.1 |

---

## 📐 ARCHITETTURA VISUALE DEL SISTEMA
┌──────────────────────────────────────────────────────────────────────┐
│ MARKETING UNIVERSITY — ARCHITETTURA │
├──────────────────────────────────────────────────────────────────────┤
│ │
│ INPUT UTENTE │
│ ┌─────────────┐ ┌────────────┐ ┌──────────────┐ ┌────────────┐ │
│ │ Materiale │ │ Ricerca │ │ "Cosa │ │ Review │ │
│ │ Formativo │ │ Framework │ │ studiare?" │ │ Sett/Mens │ │
│ └──────┬──────┘ └─────┬──────┘ └──────┬───────┘ └─────┬──────┘ │
│ │ │ │ │ │
│ ▼ ▼ ▼ ▼ │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ CUSTOM INSTRUCTIONS (Cervello) │ │
│ │ Identità → Ragionamento → Routing → Elaborazione → Output │ │
│ └───────────────────────┬──────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ KNOWLEDGE BASE (14 File) │ │
│ │ │ │
│ │ FONDAZIONE PROCESSI DATI │ │
│ │ ┌────────────┐ ┌──────────────┐ ┌──────────────┐ │ │
│ │ │ KB_01 │ │ KB_02 │ │ KB_08 │ │ │
│ │ │ Library │────▶│ Extraction │──▶│ Frameworks │ │ │
│ │ │ Architecture│ │ Engine │ │ Registry │ │ │
│ │ └────────────┘ └──────────────┘ └──────────────┘ │ │
│ │ ┌────────────┐ ┌──────────────┐ ┌──────────────┐ │ │
│ │ │ KB_03 │ │ KB_04 │ │ KB_14 │ │ │
│ │ │ Connection │ │ Study Method │ │ Preloaded │ │ │
│ │ │ Matrix │ │ Pipeline │ │ Frameworks │ │ │
│ │ └────────────┘ └──────────────┘ └──────────────┘ │ │
│ │ │ │
│ │ SUPPORTO OUTPUT CONTROLLO │ │
│ │ ┌────────────┐ ┌──────────────┐ ┌──────────────┐ │ │
│ │ │ KB_05-07 │ │ KB_06 │ │ KB_10-11 │ │ │
│ │ │ Routine, │ │ Response │ │ Quality, │ │ │
│ │ │ Quick Ref │ │ Templates │ │ Rules │ │ │
│ │ └────────────┘ └──────────────┘ └──────────────┘ │ │
│ │ ┌────────────┐ ┌──────────────┐ │ │
│ │ │ KB_09 │ │ KB_12-13 │ │ │
│ │ │ Priority │ │ Setup, │ │ │
│ │ │ Engine │ │ Glossary │ │ │
│ │ └────────────┘ └──────────────┘ │ │
│ └──────────────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ OUTPUT VERSO PROGETTI │ │
│ │ │ │
│ │ ⚡ Agency 🎥 YouTube 📚 KDP 🤖 AI Lab 🧠 Strategy │ │
│ │ Operations Lead Engine Content Influencer Command │ │
│ │ Factory Lab Center │ │
│ │ │ │
│ │ Framework Script Copy Caption Decisioni │ │
│ │ copy → video → libri → social → strategiche │ │
│ │ clienti contenuti vendita engagement → growth │ │
│ └──────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘

text


---

## 📊 STATISTICHE DEL PROGETTO

| Metrica | Valore |
|---------|--------|
| File totali | 16 (1 CI + 15 KB) |
| Righe totali stimate | ~4.600+ |
| Workflow operativi | 6 |
| Processi di ragionamento | 7 |
| Edge cases coperti | 10 |
| Aree della biblioteca | 6 |
| Sottoaree totali | 24 |
| Template output | 7 |
| Blocchi codice Python | 15+ |
| Configurazioni JSON | 8+ |