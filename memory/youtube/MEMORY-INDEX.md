# MEMORY-INDEX.md — YouTube Ecosystem

> **Ecosystem:** YouTube Automation & Content Production
> **Owner:** Gael
> **Started:** 2026-07-19
> **Status:** 🟢 Fase 1 in corso — Agenti Research completati

---

## 📊 Stato Attuale

**Fase:** 1 - Fondamenta (in corso)
**Progresso:** 20%
**Agenti creati:** 2/23 (yt-competitor-scout, yt-trend-analyzer)
**Workflow creati:** 0/17
**Video pubblicati:** 0

---

## 📁 Indice Checkpoints

- [CP-001-yt-competitor-scout-start] 2026-07-20: Inizio creazione agente yt-competitor-scout
- [CP-002-yt-competitor-scout-complete] 2026-07-20: Agente yt-competitor-scout completato (7 file canonici)
- [CP-003-yt-trend-analyzer-start] 2026-07-20: Inizio creazione agente yt-trend-analyzer
- [CP-004-yt-trend-analyzer-complete] 2026-07-20: Agente yt-trend-analyzer completato (7 file canonici)
- [CP-005-youtube-infrastructure-start] 2026-07-20: Inizio setup infrastruttura YouTube (API, workspace)

---

## 📁 Indice Decisioni

- [DEC-001-nicchie-prioritarie] 2026-07-20: Nicchie prioritarie selezionate: "Claude Code", "AI coding", "programming tutorials"
- [DEC-002-agenti-research-priority] 2026-07-20: Priorità agenti research: yt-competitor-scout, yt-trend-analyzer, yt-keyword-researcher, yt-audience-analyst

---

## 📁 Indice Sessioni

- [SES-001-agenti-research-creation] 2026-07-20: Sessione creazione agenti YouTube Research (2 agenti completati)

---

## 📁 Indice Plans

- **PLAN-v1-youtube-ecosystem.md** — Piano ecosistema YouTube completo (creato in SISTEMA-TASK-GAEL.md)
- **PLAN-v2-content-calendar.md** — Piano contenuti mensile (da creare)
- **PLAN-v3-agenti-research.md** — Piano agenti research (in corso)

---

## 📁 Indice Architectures

- **ARCH-001-youtube-pipeline.md** — Architettura pipeline YouTube (definita in README.md)

---

## 📁 Knowledge Base

### Competitors
- `Claude_Code_20260720.json` — Analisi competitor (da generare con primo run)

### Trends
- `Claude_Code_20260720.json` — Analisi trend (da generare con primo run)

### Best Practices
- `youtube-best-practices.md` — Best practices YouTube (da creare)

### Analytics
- `youtube-analytics-baseline.md` — Baseline metriche (da creare)

---

## 📁 Agenti Creati

### yt-competitor-scout ✅ COMPLETATO
**Path:** `SKILL & Agenti/YouTube/agents/research/yt-competitor-scout/`
**File:** 7/7
- spec.md ✅
- system-prompt.md ✅
- tools.md ✅
- playbook.md ✅
- evals.md ✅
- failure-modes.md ✅
- memory.md ✅

**Capabilities:**
- Ricerca competitor YouTube
- Analisi canali e video
- Identificazione gap di mercato
- Estrazione best practices

### yt-trend-analyzer ✅ COMPLETATO
**Path:** `SKILL & Agenti/YouTube/agents/research/yt-trend-analyzer/`
**File:** 7/7
- spec.md ✅
- system-prompt.md ✅
- tools.md ✅
- playbook.md ✅
- evals.md ✅
- failure-modes.md ✅
- memory.md ✅

**Capabilities:**
- Analisi trend con Google Trends
- Ricerca keyword con Keyword Planner
- Analisi stagionalità
- Generazione forecast

---

## 🔄 Update Protocol

1. Dopo ogni azione significativa → creare CP
2. Dopo ogni decisione → creare DEC
3. Alla fine di ogni sessione → creare SES
4. Aggiornare questo INDEX dopo ogni CP/DEC/SES

---

## 🎯 Prossimo Step

**Agenti Research rimanenti:**
1. yt-keyword-researcher (da creare)
2. yt-audience-analyst (da creare)

**STEP 1: Setup Infrastruttura (2 ore)**
1. Setup Memory System ✅ (directory create, MEMORY-INDEX attivo)
2. Setup Fliki API (verificare chiave, test chiamata)
3. Setup YouTube API (verificare OAuth, test upload)
4. Setup Workspace ✅ (directory create)
5. Checkpoint CP-005

**STEP 2: Completamento Agenti Research (4 ore)**
6. Creazione yt-keyword-researcher (7 file canonici)
7. Creazione yt-audience-analyst (7 file canonici)
8. Test integrazione agenti (1 ricerca completa end-to-end)
9. Checkpoint CP-006

---

*Ultimo aggiornamento: 2026-07-20 19:00*
