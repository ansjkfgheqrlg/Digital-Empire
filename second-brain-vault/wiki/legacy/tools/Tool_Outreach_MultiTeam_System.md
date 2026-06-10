---
Type: TOOL
Status: Active — Writer APSOC completo (200-300 parole, free call, trasparenza) — 2026-05-05
Tags: #automation #outreach #lead-generation #multi-agent #groq #email
Created: 2026-04-30
Last updated: 2026-05-05
---

# Tool: Outreach Multi-Team System v2.0

## Overview

Sistema di cold email completamente automatico che trova lead su Facebook Ads, qualifica, scrive email APSOC-powered con tono Andrei Pascu, verifica la qualità con 3 check umano/AI, e invia 300 email/giorno. Costo operativo: **$0/giorno** (tutto NVIDIA Nemotron gratuito via OpenRouter).

## Architettura — 6 Team Coordinati

```
python run.py
 └── OrchestratorAgent (orchestrator.py)
      │
      ├── TEAM 1 — INTELLIGENCE
      │    ├── ScraperAgent       → 600 business da Facebook Ad Library API
      │    ├── ExtractorAgent     → email dai siti web (requests + BS4)
      │    └── QualifierAgent     → score 0-100, template A/B/C [NVIDIA free]
      │
      ├── TEAM 2 — COPY KNOWLEDGE  [NVIDIA free]
      │    └── CopyKnowledgeAgent → briefing pack: esempi, regole, apertura suggerita
      │
      ├── TEAM 3 — STRATEGY  [NVIDIA free]
      │    └── StrategistAgent    → hook angle + brief 80 parole
      │
      ├── TEAM 4 — COPY  [NVIDIA free]
      │    ├── EmailDrafterAgent  → email APSOC con context completo
      │    └── SubjectLineAgent   → 3 varianti oggetto (A/B/C)
      │
      ├── TEAM 5 — HUMAN VOICE QA  [NVIDIA free, revision loop]
      │    ├── HumannessChecker       → score 1-10
      │    ├── DirectResponseReviewer → score 1-10
      │    └── BrandValidator         → score 1-10 (benchmark: Andrei Pascu)
      │         media < 7 → 1 retry writer → secondo check → scarto se ancora fail
      │
      └── TEAM 6 — DELIVERY  [Python gratuito]
           ├── SenderAgent   → Gmail SMTP (300 email/giorno)
           └── TrackerAgent  → SQLite deduplicazione + CSV log
```

## Modelli AI Utilizzati (aggiornato 2026-05-04)

Rotation interleaved: Groq (primary) → OpenRouter (fallback). Max 4 tentativi per chiamata.

| Tentativo | Modello | Provider | Limiti |
|---|---|---|---|
| 1 | llama-3.3-70b-versatile | Groq | 6000 TPM, 1000 req/day |
| 2 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | free tier |
| 3 | llama-3.1-8b-instant | Groq | 6000 TPM, 14400 req/day |
| 4 | nvidia/nemotron-3-nano:free | OpenRouter | free tier |

**TOTALE costo: $0/giorno**

### Delay tra chiamate (calibrati su 6000 TPM Groq)
- Writer: 20s (3 call/min × ~1700 token = 5100 TPM)
- CopyKnowledge: 8s
- Strategist: 8s
- Humanizer: 4s (external), 3s (internal tra i 3 check)

## Knowledge Base (3 file)

- `knowledge/apsoc.py` — Framework APSOC completo, Templates A/B/C, CPB, DR principles
- `knowledge/brand_voice.py` — Tono DE, benchmark Andrei Pascu, vocabolario vietato/approvato
- `knowledge/copy_training.py` — 30+ esempi email reali, anti-esempi, micro-regole per settore

## I 3 Template

| Template | Target | Angolo |
|---|---|---|
| **A** | Business senza sito web | "Perde clienti che cercano online" |
| **B** | Business con ads + funnel scarso | "Paga per click che non convertono" |
| **C** | Aziende strutturate (10+ dip.) | "Automatizza [processo], risparmia Xh/settimana" |

## Setup Rimanente

1. **FB_ACCESS_TOKEN** — Token Facebook Ad Library (5 min, SETUP.md sez. 2)
2. **GMAIL_APP_PASSWORD** — App Password Gmail 16 caratteri (3 min, SETUP.md sez. 3)

OPENROUTER_API_KEY già configurata nel `.env`.

## Comando Lancio

```bash
cd "Digital Empire/Outreach"
pip install -r requirements.txt          # Prima volta
python run.py --target 10 --anteprima   # Test
python run.py                            # Produzione 300/giorno
```

## Struttura File

```
Outreach/
├── run.py                 ← entry point
├── requirements.txt
├── .env                   ← credenziali
├── SETUP.md               ← guida configurazione
├── knowledge/
│   ├── apsoc.py
│   ├── brand_voice.py
│   └── copy_training.py
├── agents/
│   ├── orchestrator.py
│   ├── scraper.py
│   ├── extractor.py
│   ├── qualifier.py
│   ├── copy_knowledge.py
│   ├── strategist.py
│   ├── writer.py
│   ├── humanizer.py
│   └── sender.py
└── output/
    ├── leads.db
    └── YYYY-MM-DD_invio_log.csv
```

## Metriche Target

- **Lead trovati/giorno**: 600+ (2× buffer per compensare chi non ha email)
- **Lead con email**: ~300-360 (50-60% conversion)
- **Lead qualificati**: ~200-250 (score ≥ 40)
- **Email scritte**: 300
- **QA pass rate atteso**: 80%+ al primo tentativo
- **Email inviate**: 300/giorno
- **Costo**: $0/giorno

## Connessioni

- [[Concept_APSOC_Email_Application]] — framework usato nelle email
- [[Concept_Human_Voice_QA]] — sistema QA qualità
- [[Andrei_Pascu]] — benchmark tono
- [[Project_Outreach_Automation_Implementation]] — progetto padre
