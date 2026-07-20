# WORKFLOW S4 — Mentalita.Brutale 100% Auto (Versione Operativa)

**Owner:** YouTube Department + Carousel Factory  
**Goal:** Pipeline completamente automatica

---

## Fasi

| Fase | Nome | Agente | Output |
|------|------|--------|--------|
| 1 | Wrap | carousel-factory (ADR-003) | Motore wrappato |
| 2 | Gate QA | qa-gate-agent | Controllo qualità |
| 3 | Scheduler | scheduler-agent | Pubblicazione automatica |
| 4 | Report | yt-performance-analyzer | Performance report |
| 5 | Memory | checkpoint-manager | CP |

**Agenti:** qa-gate-agent, scheduler-agent

**Memory Path:** `company/Memory/ESTATE-WORKSHOP/stream-S4/`