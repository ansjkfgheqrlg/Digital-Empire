---
name: site-qa
description: "Quality assurance completo del sito web costruito. Lancia 4 agenti in parallelo che coprono validita e struttura HTML, accessibilita WCAG 2.1 AA, performance e Core Web Vitals, responsive e cross-browser. Produce QA-REPORT.md con severity rating e istruzioni di fix. Usala su /site qa, prima di un deploy, o quando serve verificare la qualita tecnica di un sito appena generato."
---

Sei la skill di quality assurance del sistema /site. Il tuo compito è analizzare il sito costruito su 4 dimensioni — HTML, Accessibilità, Performance, Mobile — e produrre un report con scoring e istruzioni di fix.

## Trigger

Attivata da `/site qa`. Eseguita dopo `/site build`, in parallelo con `/site seo`.

## Input Necessari

- Tutti i file `*.html`, `*.css`, `*.js` nella CWD
- `SITE-BUILD.md` — manifest dei file del progetto
- `SITE-PLAN.md` — per verificare che tutte le pagine previste siano state costruite

## Processo

### Step 1 — Leggi il progetto
Leggi tutti i file rilevanti nella CWD per avere il contesto completo prima di lanciare gli agenti.

### Step 2 — Lancia 4 agenti in parallelo
Usa il tool Agent per lanciare simultaneamente:
- `site-qa-html` — validità HTML e struttura semantica
- `site-qa-accessibility` — WCAG 2.1 AA compliance
- `site-qa-performance` — performance e Core Web Vitals
- `site-qa-mobile` — responsive e cross-browser

Passa a ogni agente il contesto del progetto (file letti) e chiedi un JSON strutturato con: `score` (0-100), `issues` (array con `severity`, `description`, `file`, `fix`).

### Step 3 — Calcola il Site Quality Score
Applica i pesi per calcolare il punteggio finale:

| Dimensione | Peso |
|---|---|
| HTML Quality | 25% |
| Accessibility | 30% |
| Performance | 25% |
| Mobile/Responsive | 20% |

Formula: `SCORE = html*0.25 + accessibility*0.30 + performance*0.25 + mobile*0.20`

Classifica il risultato:
- 90-100 → Deploy-Ready ✅
- 75-89 → Good (deploy con attenzione ai Medium)
- 60-74 → Needs Work (risolvi tutti gli High prima del deploy)
- 0-59 → Blocco Deploy ❌

### Step 4 — Prioritizza le issue
Aggrega tutte le issue dai 4 agenti e classificale per severity:
- **Critical** — blocca il deploy (link rotti, pagine mancanti, form non funzionanti, errori JS globali)
- **High** — da risolvere prima del lancio (contrasto colore insufficiente, immagini senza alt, title mancante)
- **Medium** — da risolvere idealmente prima del lancio (performance minori, heading hierarchy imperfetta)
- **Low** — iterazione post-lancio (ottimizzazioni cosmetiche, nice-to-have)

### Step 5 — Gate di deploy
Se esistono issue **Critical** non risolte:
1. Mostra un warning prominente nel report
2. Aggiungi una sezione "BLOCKERS" all'inizio del QA-REPORT.md
3. Quando la skill `/site deploy` viene invocata, questa deve leggere QA-REPORT.md e chiedere conferma esplicita prima di procedere

### Step 6 — Genera QA-REPORT.md
Scrivi il report nella CWD con questa struttura:

```markdown
# QA Report — [Nome Progetto]
**Data:** [data]
**Site Quality Score:** [score]/100 — [etichetta]

---

## ⚠️ BLOCKERS CRITICI (se presenti)
[lista issue Critical — risolvi prima del deploy]

---

## Scoring Breakdown

| Dimensione | Score | Peso | Contributo |
|---|---|---|---|
| HTML Quality | [n]/100 | 25% | [n] |
| Accessibility | [n]/100 | 30% | [n] |
| Performance | [n]/100 | 25% | [n] |
| Mobile/Responsive | [n]/100 | 20% | [n] |
| **TOTALE** | **[n]/100** | | |

---

## HTML Quality — [score]/100
[issue trovate con severity, descrizione, file, istruzione di fix]

## Accessibility — [score]/100
[issue trovate]

## Performance — [score]/100
[issue trovate]

## Mobile/Responsive — [score]/100
[issue trovate]

---

## Fix Summary
| Severity | Count | Status |
|---|---|---|
| Critical | [n] | ❌ Da risolvere |
| High | [n] | ⚠️ Da risolvere |
| Medium | [n] | 🔶 Consigliato |
| Low | [n] | ℹ️ Opzionale |
```

### Step 7 — Aggiorna SITE-STATUS.md
Segna la fase QA come completata. Se ci sono issue Critical, aggiungile alla sezione Blockers del file di status.

## Output

- `QA-REPORT.md` — report completo con scoring, issue per dimensione, fix instructions

## Comunicazione Finale

Al termine mostra all'utente:
1. Il Site Quality Score con etichetta
2. Il numero di issue per severity
3. I prossimi passi: issue critiche da risolvere, o conferma che il sito è deploy-ready
4. Il comando suggerito: `/site deploy [platform]`
