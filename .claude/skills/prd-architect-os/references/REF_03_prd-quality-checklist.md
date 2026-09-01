# REF_03 — PRD Quality Checklist
## Sistema di Scoring 0-100 per Validation Engine

Questo file è il **Validation Engine** del PRD Architect OS.
Eseguilo SEMPRE prima di consegnare un PRD. Se il score è sotto 65, lista i blockers e offri di risolverli.

---

## 🔴 LIVELLO 0 — GATE CHECKS (BLOCCANTI)

Se anche UN SOLO gate fallisce → **Score = 0, PRD bloccato. Non procedere.**

```
GATE 1: Problem Statement
□ Esiste una sezione "Problema" o "Problem Statement"
□ Il problema è descritto come DOLORE dell'utente (non come soluzione)
□ È presente almeno 1 evidenza che il problema esiste (dato, citazione, intervista)

GATE 2: Target Utente
□ Esiste una persona primaria identificata
□ La persona NON è "chiunque" o "professionisti in generale"
□ La persona ha almeno: ruolo, contesto, obiettivo primario

GATE 3: User Stories
□ Esiste almeno 1 user story con formato corretto
□ La user story ha almeno 1 acceptance criteria misurabile

GATE 4: Metriche
□ Esiste almeno 1 metrica di successo
□ La metrica NON è vaga (no "aumentare la retention")
□ La metrica ha un target numerico specifico
```

**Se un Gate fallisce:**
> "🔴 GATE CHECK FALLITO: [quale gate] — Il PRD non può essere valutato. 
> Risolvi prima di procedere con il Quality Score."

---

## 📊 LIVELLO 1 — STRUTTURA (max 30 punti)

### 1.1 Header e Versionamento (6 punti)
```
□ Titolo specifico e descrittivo (non "PRD Feature X") — 1pt
□ Versione presente (es: v1.0) — 1pt
□ Status presente (DRAFT/IN REVIEW/APPROVED) — 1pt
□ Data creazione presente — 1pt
□ Revisori identificati — 1pt
□ Change log con almeno 1 riga — 1pt
```

### 1.2 Sezioni Obbligatorie per Tipo (12 punti)

**Tipo B (MVP Lean) — verifica presenza di:**
```
□ TL;DR o Executive Summary — 2pt
□ Problem Statement — 2pt
□ Target Utente/Persona — 2pt
□ Success Metrics — 2pt
□ User Stories (≥3) — 2pt
□ Scope IN/OUT — 2pt
```

**Tipo A (Enterprise) — aggiuntivi:**
```
□ Executive Summary — 1pt
□ Permissions e Roles Matrix — 1pt
□ Analytics Spec dettagliata — 1pt
□ Rischi e Mitigazioni — 1pt
□ Migration/Rollout Plan — 1pt
□ Appendix — 1pt
```

**Tipo D (Vibecoding) — aggiuntivi:**
```
□ Tech Stack vincolante — 2pt
□ Schema DB outline — 2pt
□ AI Constraints sezione — 2pt
```

### 1.3 Timeline e Milestones (6 punti)
```
□ Timeline presente con date o time-box — 2pt
□ Milestones identificate (almeno 3) — 2pt
□ Owner per ogni milestone — 1pt
□ Status per ogni milestone — 1pt
```

### 1.4 Open Questions (6 punti)
```
□ Sezione Open Questions presente — 2pt
□ Ogni domanda ha un owner — 2pt
□ Ogni domanda ha una deadline — 1pt
□ Almeno 1 domanda contrassegnata come "resolved" (se PRD non è v1.0) — 1pt
```

---

## 📝 LIVELLO 2 — QUALITÀ CONTENUTO (max 40 punti)

### 2.1 Problem Statement (10 punti)
```
□ Il problema è descritto con DATI, non opinioni — 3pt
□ Cita almeno 2 fonti di evidenza diverse — 3pt
□ Spiega perché le soluzioni attuali non bastano — 2pt
□ Quantifica l'impatto (tempo perso, costo, frequenza) — 2pt
```

**Score 0**: Solo affermazioni senza dati
**Score 5**: Dati presenti ma una sola fonte
**Score 10**: 2+ fonti diverse, problema quantificato, gap competitivo chiaro

### 2.2 Target Utente (8 punti)
```
□ Persona primaria strutturata (non solo nome) — 2pt
□ Jobs-to-be-done in formato "Quando X, voglio Y, in modo da Z" — 2pt
□ Quote rappresentativa (frase che potrebbe dire) — 2pt
□ Frustrazione principale documentata — 1pt
□ Disponibilità a pagare indicata (se SaaS) — 1pt
```

### 2.3 User Stories (10 punti)
```
□ Formato corretto: "Come [utente], voglio [azione], in modo da [beneficio]" — 2pt
□ Acceptance criteria TESTABILI (PASSA SE / FALLISCE SE) — 4pt
□ Priority P0/P1/P2 per ogni story — 2pt
□ Effort stimato per ogni story — 1pt
□ Epic/raggruppamento logico delle stories — 1pt
```

**Red flag**: "L'utente deve poter" senza formato JTBD = -2pt
**Red flag**: Acceptance criteria come "il sistema deve funzionare" = -2pt

### 2.4 Success Metrics (6 punti)
```
□ North Star Metric identificata (1 sola) — 2pt
□ North Star ha target numerico + timeframe + tool di misurazione — 2pt
□ Almeno 2 Primary Metrics con target specifici — 1pt
□ Guardrail Metrics presenti — 1pt
```

### 2.5 Analytics Events (6 punti)
```
□ Almeno 3 eventi analytics definiti — 2pt
□ Ogni evento ha nome specifico (snake_case) — 1pt
□ Ogni evento ha properties definite — 2pt
□ Tool di misurazione specificato (PostHog, Mixpanel, GA4...) — 1pt
```

---

## ⚠️ LIVELLO 3 — EDGE CASES (max 15 punti)

### 3.1 Empty States (4 punti)
```
□ Almeno 2 empty state documentati per feature principali — 2pt
□ Ogni empty state ha: trigger + contenuto + CTA — 2pt
```

### 3.2 Loading States (3 punti)
```
□ Almeno 2 loading state documentati — 1pt
□ Tipo di feedback visivo specificato (spinner/skeleton/progress) — 1pt
□ Durata stimata per operazioni >1s — 1pt
```

### 3.3 Error States (5 punti)
```
□ Almeno 3 error state documentati — 2pt
□ Ogni errore ha messaggio SPECIFICO (non "si è verificato un errore") — 2pt
□ Ogni errore ha un'azione suggerita/recovery path — 1pt
```

### 3.4 Edge Cases Speciali (3 punti)
```
□ Gestione offline documentata (se applicabile) — 1pt
□ Permission denied / feature gating documentato — 1pt
□ Rate limiting / piano limits documentato (se applicabile) — 1pt
```

---

## 📊 LIVELLO 4 — ANALYTICS SPEC (max 10 punti)

### 4.1 Events Coverage (5 punti)
```
□ Evento per ogni milestone utente critico (signup, first_action, conversion) — 3pt
□ Evento per ogni stato del funnel principale — 2pt
```

### 4.2 Implementation Spec (5 punti)
```
□ Codice JavaScript/pseudocodice per gli eventi — 3pt
□ Properties definite con tipo di dato (string, number, boolean) — 2pt
```

---

## 🔄 LIVELLO 5 — CONSISTENZA (max 5 punti)

### 5.1 Consistenza Interna (3 punti)
```
□ Nessuna contraddizione tra sezioni diverse — 2pt
□ Terminologia consistente (stesso nome per stessa feature) — 1pt
```

### 5.2 Referenze Funzionanti (2 punti)
```
□ Tutte le referenze interne puntano a sezioni esistenti — 1pt
□ Nessuna sezione "da completare" o "[TBD]" nei punti critici — 1pt
```

---

## 📊 PRD QUALITY REPORT — TEMPLATE OUTPUT

```markdown
## 📊 PRD QUALITY REPORT — [Nome PRD]

**Analizzato il**: [Data]
**Tipo PRD**: [A/B/C/D/E]
**Versione**: [v1.x]

---

### Score Finale: [X]/100 — [Emoji + Status]

| Livello | Score | Max | % |
|---------|-------|-----|---|
| Gate Checks | ✅ PASS / ❌ FAIL | PASS | — |
| Struttura | [L1] | 30 | [p1]% |
| Qualità Contenuto | [L2] | 40 | [p2]% |
| Edge Cases | [L3] | 15 | [p3]% |
| Analytics | [L4] | 10 | [p4]% |
| Consistenza | [L5] | 5 | [p5]% |

---

### ✅ Punti di Forza
1. [Punto forte con riferimento specifico alla sezione]
2. [Punto forte]
3. [Punto forte]

### ⚠️ Warnings (risolvi prima dell'approvazione)
1. [Warning con riferimento specifico + come risolvere]
2. [Warning]

### 🔴 Blockers (risolvi prima di procedere allo sviluppo)
1. [Blocker critico con riferimento + azione richiesta]

### 💡 Raccomandazioni Prioritarie
1. [Prima cosa da fare per migliorare il PRD]
2. [Seconda]
3. [Terza]

---
*"Vuoi che risolva uno specifico blocker? Dimmi quale e procedo."*
```

---

## Interpretazione Score

| Score | Status | Cosa Significa | Azione |
|-------|--------|----------------|--------|
| 0 | 🔴 BLOCCATO | Gate check fallito | Non procedere allo sviluppo. Risolvi gate. |
| 1-49 | 🔴 INSUFFICIENTE | Troppo incompleto | Riscrivere sezioni fondamentali |
| 50-64 | 🟠 BOZZA | Utilizzabile per discussione | NON passare allo sviluppo ancora |
| 65-79 | 🟡 DRAFT APPROVABILE | Può avviare sviluppo | Con warnings espliciti — monitora |
| 80-89 | 🟢 BUONO | Solido, pronto per engineering | Review engineering prima di approvare |
| 90-100 | 🔵 ECCELLENTE | Production-ready | Approvabile con sign-off formale |

---

## Checklist Rapida Pre-Consegna (30 secondi)

Prima di dare il PRD a qualsiasi destinatario, verifica:

```
□ Problem Statement ha almeno 1 dato quantitativo
□ Persona primaria ha nome + ruolo + JTBD
□ Ogni user story P0 ha acceptance criteria PASSA SE / FALLISCE SE
□ Almeno 3 error state con messaggi specifici
□ North Star Metric ha target numerico + timeframe + tool
□ Out-of-Scope ha almeno 2 feature con motivazione e timeline
□ Nessuna sezione "[TBD]" o "da definire" nei punti P0
□ Change log aggiornato
□ PRD Quality Report incluso in fondo
```

Se anche un solo check fallisce → il PRD non è pronto.
