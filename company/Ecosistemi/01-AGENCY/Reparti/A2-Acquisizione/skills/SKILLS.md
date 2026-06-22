---
Type: SKILLS
Status: Active
Tags: #skills #agency #acquisizione #outreach #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# Skill — A2 Acquisizione / Outreach

> Mappa delle skill del reparto: entrypoint operativi (avvio run) + knowledge layer.
> Tutte le skill mappate qui INVOCANO il runtime esistente (ADR-003): nessuna riscrive il motore.

---

## Skill di avvio run (entrypoint operativi — già installate)

| Skill | Workflow | Ruolo in A2 |
|---|---|---|
| `avvia-email` | WF-OUTREACH-EMAIL | Apre la run email completa: scraping → qualifier → writer → Bibbia → invio |
| `avvia-linkedin` | WF-OUTREACH-LINKEDIN | Avvia commenti + connessioni + messaggi LinkedIn (scripts 01→05 + comment_posts.py) |
| `avvia-ig` | WF-OUTREACH-INSTAGRAM | Avvia la run Instagram (hashtag scout → qualifier → DM → follow-up) |
| `avvia-parallel` | EMAIL + INSTAGRAM | Avvia Email + Instagram in parallelo (cap indipendenti per canale) |
| `avvia-scraper` | (a monte) | Raccolta nuovi lead via `scrape_only.py` — popola `leads.db` prima del reparto |

---

## Skill knowledge layer (conoscenza, non avvio)

| Skill | Stato | Ruolo in A2 | Note |
|---|---|---|---|
| `outreach-reply-triage` | Esistente, mappata | Motore di classificazione risposte di AG-A2-TRIAGE | Riusabile anche dai clienti Outreach Factory (pattern #11) |
| `cold-email` | Esistente, mappata | Knowledge base per AG-A2-WRITE / AG-A2-FUP (struttura cold + follow-up) | Conoscenza, non sostituisce writer.py |
| `agency-scalping` | Esistente, mappata | Knowledge base pipeline acquisizione / outreach a freddo | Ausiliaria di AG-A2-COORD |

---

## Mappatura skill → agente → motore wrappato

| Skill | Agente owner | Motore invocato (intoccabile) |
|---|---|---|
| `avvia-email` | AG-A2-COORD → SEND | orchestrator.py + sender.py (cap 100/h, ≤500/gg) |
| `avvia-linkedin` | AG-A2-LI | scripts 01→05 + comment_posts.py (20+20+30/gg) |
| `avvia-ig` | AG-A2-IG | Instagram run_today.py (30 DM/gg) |
| `outreach-reply-triage` | AG-A2-TRIAGE | reply_monitor.py |
| `cold-email` | AG-A2-WRITE / FUP | writer.py / followup_writer.py (knowledge only) |

---

## Regola anti-contraddizione

Le skill di questo reparto NON ridefiniscono il motore di outreach: lo avviano o ne sono il
knowledge layer. Prima di forgiare qualsiasi nuova skill di acquisizione:
1. Eseguire `skill-contradiction-analyzer` contro `cold-email`, `agency-scalping`, `outreach-reply-triage`.
2. Se c'è sovrapposizione: la skill nuova ESTENDE quella esistente, non la ridefinisce.
3. Una skill che proponesse di riscrivere il runtime viola ADR-003 → non si forgia, si apre ADR.

---

## Connessioni

- [[README]] · `README.md` — entrypoint operativi del reparto
- [[scripts/README]] · `scripts/README.md` — come ogni skill invoca il motore esistente
- [[ag-a2-triage]] · `agenti/ag-a2-triage.md` — owner di `outreach-reply-triage`
