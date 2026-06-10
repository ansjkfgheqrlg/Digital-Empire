# SOP-MARKETING

> Source: File system (`Crea siti\system\SOP-MARKETING.md`)
> Collected: 2026-05-06
> Published: Unknown

# SOP — Marketing Suite Workflow
> Standard Operating Procedure per analisi marketing, audit e produzione contenuti.
> Versione: 1.0 | Sistema: /market | Comando avvio: `/market`

---

## Overview del Sistema

La Marketing Suite è composta da 15 skill + 5 agenti specializzati.

**3 modalità d'uso:**
1. **Audit completo** — analisi di un sito/brand esistente (5 agenti paralleli)
2. **Produzione contenuti** — generazione di copy, social, email, ads
3. **Strategia** — funnel, proposta cliente, brand voice, lancio prodotto

---

## Workflow 1 — Audit Marketing Completo

### Quando usarlo
- Prima di creare un sito (analizza competitor e benchmark settore)
- Prima di un restyling (identifica cosa non funziona)
- Per un cliente nuovo (capire la situazione attuale)
- Per analizzare un competitor diretto

### Procedura
```
/market audit <url>
```

Lancia 5 agenti in parallelo simultaneo:

| Agente | Analizza | Output |
|--------|---------|--------|
| `market-competitive` | Posizionamento vs competitor | Score competitivo + gap |
| `market-content` | Messaging, narrativa, coerenza brand | Content audit + gap |
| `market-conversion` | Funnel, CTA, friction, trust signals | CRO opportunities |
| `market-strategy` | Brand identity, growth, canali | Strategic recommendations |
| `market-technical` | SEO tecnico, vitals, indexability | Technical issues priority |

**Output combinato:** `MARKET-AUDIT.md` con score 0-100 e piano di intervento prioritario.

**Tempo stimato:** 5-10 minuti (agenti in parallelo).

---

### Follow-up dopo Audit

```bash
# Analisi brand approfondita
/market brand <url>

# Analisi copy per ispirazione e benchmarking
/market copy <url>

# Analisi competitor diretti multipli
/market competitors <url>
```

---

## Workflow 2 — Produzione Contenuti

### Copy & Messaging
```
/market copy
```
- Analizza copy esistente + propone varianti
- Genera headline, subheadline, body copy
- A/B variants per test

### Social Media
```
/market social
```
- Piano editoriale mensile (30 post)
- Formato per piattaforma: LinkedIn, Instagram, X, Facebook
- Template caption + hashtag + CTA

### Email Sequences
```
/market emails
```
- Welcome sequence (3-5 email)
- Nurture sequence (7-10 email)
- Launch sequence (5-7 email)
- Re-engagement sequence (3 email)

### Advertising
```
/market ads
```
- Copy per Meta Ads (headline + testo + CTA)
- Copy per Google Ads (titolo + descrizione)
- Varianti A/B (3+ per formato)

---

## Workflow 3 — Strategia e Pianificazione

### Brand Voice
```
/market brand <url>
```
- Analizza tono di voce attuale
- Definisce: personalità brand, attributi, do/don't
- Output: `BRAND-VOICE.md`

### Landing Page Ottimizzazione
```
/market landing <url>
```
- CRO analysis: above-fold, headline, proof, CTA
- Priorità intervento 1-3 (high impact/low effort)
- Wireframe ottimizzato

### Funnel Analysis
```
/market funnel
```
- Mappa funnel esistente
- Identifica drop-off points
- Propone sequenza ottimale (Awareness → Interest → Desire → Action)
- Output: `FUNNEL-ANALYSIS.md`

### Piano di Lancio
```
/market launch
```
- Timeline pre-lancio (30/14/7/1 giorni prima)
- Checklist attività marketing
- Social posts per fase
- Email sequence lancio
- Output: `LAUNCH-PLAYBOOK.md`

### Proposta Cliente
```
/market proposal
```
Input: tipo servizio, cliente target, budget range
Output: proposta professionale pronta per il cliente con:
- Executive summary
- Diagnosi situazione attuale
- Soluzione proposta
- Deliverables + timeline
- Investimento
- Prossimi passi

---

## Workflow 4 — Report e Analisi

### Report Marketing (Markdown)
```
/market report
```
- Aggrega dati di campagne/attività
- Metriche chiave con benchmark
- Insight + raccomandazioni
- Output: `MARKETING-REPORT.md`

### Report PDF
```
/market report-pdf
```
- Stesso contenuto del report markdown
- Formattato per stampa/invio cliente
- Output: PDF professionale

### SEO Content Audit
```
/market seo
```
- Analisi keyword presence
- Ottimizzazione on-page
- Content gap analysis
- Internal linking opportunities
- Output: `SEO-CONTENT-AUDIT.md`

---

## Workflow 5 — Analisi Competitiva Profonda

```
1. /market audit <url-tuo-sito>          ← baseline tua situazione
2. /market competitors <url-competitor-1> ← analisi competitor 1
3. /market competitors <url-competitor-2> ← analisi competitor 2
4. /market brand                          ← definisci differenziazione
5. /market copy                           ← aggiorna messaging
```

---

## Struttura Output Marketing

```
<progetto>/marketing/
├── MARKET-AUDIT.md           ← da /market audit
├── BRAND-VOICE.md            ← da /market brand
├── FUNNEL-ANALYSIS.md        ← da /market funnel
├── LAUNCH-PLAYBOOK.md        ← da /market launch
├── MARKETING-REPORT.md       ← da /market report
├── SEO-CONTENT-AUDIT.md      ← da /market seo
├── social/
│   ├── content-calendar.md
│   └── posts/
├── emails/
│   ├── welcome-sequence.md
│   ├── nurture-sequence.md
│   └── launch-sequence.md
└── ads/
    ├── meta-ads.md
    └── google-ads.md
```

---

## Template Inclusi nel Sistema

In `skills/market/templates/`:
| File | Contenuto |
|------|-----------|
| `content-calendar.md` | Piano editoriale 30 giorni |
| `email-launch.md` | Template email lancio |
| `email-nurture.md` | Template nurture sequence |
| `email-welcome.md` | Template welcome sequence |
| `launch-checklist.md` | Checklist lancio prodotto |
| `proposal-template.md` | Template proposta cliente |

---

## Script Python Inclusi

In `skills/market/scripts/`:
| Script | Funzione |
|--------|---------|
| `analyze_page.py` | Estrae dati SEO e contenuto da URL |
| `competitor_scanner.py` | Scansione competitiva automatica |
| `generate_pdf_report.py` | Genera PDF da report markdown |
| `social_calendar.py` | Genera calendario contenuti |

Uso: `python skills/market/scripts/analyze_page.py <url>`

---

## Referimenti
- Skill orchestratore: `skills/market/SKILL.md`
- Tutti i sotto-comandi: `skills/market-*/SKILL.md`
- Script Python: `skills/market/scripts/`
- Template: `skills/market/templates/`
