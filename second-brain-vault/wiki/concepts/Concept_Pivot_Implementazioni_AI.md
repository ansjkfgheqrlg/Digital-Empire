---
Type: CONCEPT
Status: Active
Tags: #outreach #pivot #ai-implementation #positioning #apsoc #strategia
Created: 2026-06-04
Last updated: 2026-06-04
---

# Pivot Strategico — Da Landing Page a 3 Implementazioni AI

## Overview
Documenta il pivot di posizionamento del sistema di outreach di Digital Empire. L'agenzia ha **smesso di vendere "landing page / CRO"** e ora vende **3 prodotti = implementazioni AI**: workflow installati sui server del cliente, codice sorgente incluso, €0 canoni mensili, setup in 7 giorni, automazione al 100%. Il pivot ricalibra l'intero motore outreach (target, framework, copy, link) attorno a questa nuova offerta.

---

## Dettagli

### Perché il pivot
La vecchia leva — "miglioro le tue conversioni" — **offende chi fa marketing di mestiere** (agenzie, SMM, copywriter): è come dire che non sanno fare il loro lavoro. La nuova leva non tocca la competenza del prospect ma la sua **operatività**: "ti stravolgo l'operatività". Tesi di fondo:

- Un workflow risolve **UN problema al 1000%** → l'unica obiezione residua diventa la **fiducia**, non il valore.
- Prodotto **in hype** (AI applicata, automazione reale) → attenzione naturale del mercato.
- **Ticket alto** (€10k è accettabile) perché l'automazione è al 100% e il cliente possiede il codice.
- Collega i due business più potenti di Digital Empire: **Agency** e **Info Business**.

### I 3 prodotti (= implementazioni AI)
1. **Outreach Factory** — automatizza l'outreach al 100% (300+ email/giorno via Gmail + canali social).
2. **Content Factory** — l'AI genera copy CRO e costruisce grafiche/caroselli social e script video in automatico.
3. **Second Brain** — knowledge base a grafo che dà memoria e contesto permanente all'LLM (Context Engineering, scuola Karpathy).

Caratteristiche comuni dell'offerta: **workflow installato sui server del cliente**, **codice sorgente incluso**, **€0 canoni mensili** (solo API a consumo), **setup 7 giorni**, **automazione 100%**, sconto lancio.

### Framework APSOC ricalibrato
Il framework [[Framework_Cold_Outreach_APSOC]] resta la spina dorsale del copy ma viene ritarato sulla nuova offerta:

- **A — Attenzione** → hype dell'automazione AI (non più Barnum generico sul settore).
- **P — Problema** → UN solo problema operativo concreto del prospect.
- **S — Soluzione** → il workflow che lo risolve al 100% (codice tuo, €0 canoni, 7 giorni).
- **O — Obiezione** → ne resta UNA sola: la **fiducia**. Si abbatte con demo live + presentazione di qualità estrema.
- **C — CTA** → guarda la presentazione (link) + prenota una call, con sconto lancio.

### Match prodotto ↔ target (qualifier)
Il qualifier ora abbina il prodotto-gancio al tipo di lead, via template e nuovo campo `prodotto_guida`:

| Template | Prodotto guida | Target tipico |
|---|---|---|
| A | **Outreach Factory** | chi deve acquisire clienti (agency, freelancer marketing) |
| B | **Content Factory** | chi produce contenuti (info-business, coach, SMM, copywriter) |
| C | **Second Brain** | chi ha bisogno di memoria/contesto operativo (consulenti, team) |

### Policy link nel primo messaggio
- Inserito il link presentazione nel CTA: `PRESENTATION_URL = https://presentazione-empire.vercel.app/`.
- Link agenzia in firma: `AGENCY_URL = https://agency-empire-kohl.vercel.app`.
- Applicato su **Email + LinkedIn + Instagram**.
- **Rimosso il vecchio HARD-BLOCK** che scartava le email contenenti link (in `bibbia_team.py`) e abolita la regola "link = HARD FAIL" nella Bibbia.
- Deliverability mitigata tenendo il **volume basso (25-30 email/giorno)**.

### Nuovo target
Da professionisti locali a player del marketing e del digitale:
- **IN**: Agency, Info Business (info-product, coach, formatori), Marketing pros (SMM, copywriter, freelance ads), ecommerce.
- **OUT**: professionisti locali (dentisti, avvocati, ristoranti, artigiani, salute) — eliminati da scraper SETTORI, hashtag Instagram, ricerche LinkedIn e keyword bio.
- **Chiavi settore canoniche**: `agenzia`, `info_product`, `coach`, `smm_freelance`, `ecommerce`, `consulente`, `default`.

### Impatti sul sistema outreach
File toccati (solo ricalibrazione, codice già implementato e compilante):
- `knowledge/`: `apsoc.py`, `brand_voice.py`, `copy_training.py`, `bibbia_outreach.md`.
- `agents/`: `scraper`, `qualifier`, `strategist`, `copy_knowledge`, `writer`, `bibbia_team`, `humanizer`, `followup_writer`, `conversation_manager`.
- `LinkedIn Automation/`: `config.py`, `personalize.py`.
- `Instagram Automation/`: `config.py`, `personalize.py`.
- `.env.example`.

Le catene operative (Email, LinkedIn, Instagram), i comandi di avvio e la struttura a sotto-agenti restano invariate: cambiano offerta, target, angolo di copy e policy link. Il riferimento operativo aggiornato è in `SISTEMA_OUTREACH_COMPLETO.md`.

---

## Connessioni
- [[Map - Outreach]]
- [[Framework_Cold_Outreach_APSOC]]
- [[Agency_Empire_Landing]]
- [[projects/Outreach/Email_Audit_v1_v2]]
