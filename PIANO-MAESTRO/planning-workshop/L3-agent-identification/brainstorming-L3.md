# L3 — BRAINSTORMING: Agent Identification

**Livello:** 3  
**Data:** 2026-07-20  
**Focus:** Identificazione completa di tutti gli agenti necessari per il Workshop

---

## Metodo di Identificazione

Per ogni stream analizziamo:
- Agenti esistenti da riutilizzare
- Agenti nuovi da forgiare con content-forge2.0
- Struttura 7-file obbligatoria
- Skill richieste
- Integrazione con Empire Studio

---

## Agenti per Stream

### S1 — Concessionari

**Nuovi da forgiare:**
- `concessionari-closer` (7 file)
- `offer-forge` (content-forge2.0 wrapper)

**Esistenti:**
- `compliance-auditor`

### S2 — Manuale

**Nuovi:**
- `pricing-strategist`
- `landing-forge`
- `email-lifecycle-specialist`

### S3 — Pagine Lancio

**Nuovi:**
- `carousel-forge` (wrap carousel-factory)

### S4 — Mentalita.Brutale

**Nuovi:**
- `qa-gate-agent`
- `scheduler-agent`

### S5 — YouTube Fliki (Empire Studio)

**Già esistenti (Empire Studio):**
- department-lead
- yt-channel-ingester
- video-single-ingester
- yt-screening

**Nuovi da forgiare (obbligatori):**
- `yt-fliki-renderer` (API Fliki + polling)
- `yt-seo-publisher` (YouTube Data API)
- `yt-performance-analyzer` (CTR/retention + ReasoningBank)
- `yt-niche-scout` (competitor analysis)

**Totale agenti S5:** 8

### S6 — Rebrand

**Nuovi:**
- `case-study-forge`
- `rebrand-namer`

---

## Catalogo Agenti Totali (Stima)

| Categoria | Quantità | Note |
|-----------|----------|------|
| Agenti nuovi da forgiare | 14 | 7-file ciascuno |
| Agenti Empire Studio riutilizzati | 4 | YouTube Department |
| Agenti esistenti (Forge, Memory, Verification) | 8 | Chief Forge, Memory Management, ecc. |

**Totale stimato:** 26 agenti

---

## Regole per Forgiatura Agenti

1. Tutti gli agenti nuovi devono seguire la struttura **7-file**
2. Devono essere forgiati con `content-forge2.0`
3. Devono integrarsi con `ruflo`
4. Devono salvare tutto nel Memory Ecosystem

---

**Prossimo:** L4 — Memory Architecture

**Checkpoint L3 salvato.**