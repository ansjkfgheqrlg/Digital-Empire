# 🏛️ DIGITAL EMPIRE — APEX System v2.0

> Sistema operativo per agenzia AI: prompt engineering + swarm logic + memory ecosystem

## Quick Start

```bash
# Vedi stato del sistema
cd digital-empire
python3 orchestrator.py status

# Leggi la memoria
python3 orchestrator.py memory decisions
python3 orchestrator.py memory knowledge

# Vedi i workflow disponibili
python3 orchestrator.py workflow

# Registra una decisione
python3 orchestrator.py decision "Nuova strategia pricing" "Test A/B ha mostrato +23% conversione"
```

## Cosa fa

3 stream di produzione:
- **Skill Forge** → Trasforma appunti in file `SKILL.md` eseguibili
- **Carousel Engine** → Genera slide Instagram premium (glassmorphism)
- **Cold Outreach** → Sequenze email B2B con framework APSOC

Ogni output ha un **quality gate** (≥ 7.5/10) e viene salvato in memoria.

## Usa i Prompt in Arena.ai

I file in `prompts/` sono pronti da copiare-incollare:
- `prompts/skill-forge-v2.md` → Per generare skill AI
- `prompts/carousel-engine-v2.md` → Per generare caroselli Instagram
- `prompts/cold-outreach-v2.md` → Per generare cold email

## Documentazione

→ [ARCHITECTURE.md](ARCHITECTURE.md) — Architettura completa del sistema
