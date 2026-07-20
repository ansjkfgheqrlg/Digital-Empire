# Copy Review — Skill
> Revisione copy esistente con checklist APSOC + score + suggerimenti operativi

## Invocazione

```
/review [incolla il copy qui]
```

O:
```
/review [tipo di copy] → poi incolla il testo
```

---

## Modalità Disponibili

| Modalità | Quando Usarla |
|---|---|
| **Full Review** (default) | Copy completo da analizzare in profondità |
| **Quick Review** (`/review quick`) | Check rapido in 2 minuti, score + 3 punti |
| **Headline Review** (`/review headline`) | Solo la headline e i primi 2 paragrafi |
| **CTA Review** (`/review cta`) | Solo la sezione finale del copy |
| **Objections Review** (`/review objections`) | Solo la gestione obiezioni |

---

## Full Review — Processo

### Step 1 — Identificazione Tipo Copy
Prima di analizzare, identifica:
- Tipo di copy: [Ad / Sales Page / Email / Landing / VSL / Social / Altro]
- Prodotto/servizio: [...]
- Target presunto: [...]
- Tipo di acquisto: [Impulso / Considerato / High-ticket]

### Step 2 — Analisi APSOC Sezione per Sezione
Identifica dove si trovano A, P, S, O, C nel copy.
Se mancano elementi → segnalalo come critical issue.

### Step 3 — Scoring
Applica la checklist di A8 (da `agents/qa/copy-reviewer.md`)

### Step 4 — Revisione Operativa
Per ogni problema trovato, fornisci la correzione specifica (non solo "migliora X" ma "sostituisci X con Y").

---

## Output Full Review

```markdown
# Copy Review — [Identificazione Copy]
Data review: [...]
Tipo copy: [...]
Parole totali: [n]

---

## 🎯 Score APSOC: [__/100]

| Sezione | Score | Max | Problemi |
|---|---|---|---|
| A — Attenzione | | 20 | |
| P — Problema | | 25 | |
| S — Soluzione | | 20 | |
| O — Obiezioni | | 20 | |
| C — CTA | | 15 | |
| Qualità Generale | | ±10 | |

**Verdetto**: [Eccellente ≥90 / Buono 80-89 / Accettabile 70-79 / Da rivedere 60-69 / Bocciato <60]

---

## ✅ Cosa Funziona Bene (Top 3)

1. **[Elemento]**: [Spiegazione in 1-2 righe di perché funziona]
2. **[Elemento]**: [...]
3. **[Elemento]**: [...]

---

## 🔴 Problemi Critici (da correggere subito)

### Problema 1 — [Titolo problema]
**Sezione**: [A/P/S/O/C]
**Problema**: [Descrizione del problema]
**Copy attuale**:
> "[Testo incriminato]"

**Correzione suggerita**:
> "[Testo corretto]"

**Perché funziona meglio**: [1 frase]

---

### Problema 2 — [Titolo]
[stesso schema]

---

## 🟡 Miglioramenti (non critici ma impattanti)

1. [Miglioramento + sezione + come implementarlo]
2. [...]
3. [...]

---

## 🔍 Analisi APSOC Dettagliata

### A — Attenzione
**Headline identificata**: "[testo]"
**Strategia usata**: [...]
**Funziona?**: [Sì/No] — [Motivazione]
**Alternativa migliore**: "[headline alternativa]"

### P — Problema
**Presente?**: [Sì / Parzialmente / No]
**Prima del problema viene la soluzione?**: [Sì (ERRORE) / No (OK)]
**Pain point amplificato?**: [Sì/No]
**Show don't tell?**: [Sì/No + esempio]
**Conseguenza del non agire presente?**: [Sì/No]

### S — Soluzione
**Presente?**: [Sì/No]
**Transizione naturale dal problema?**: [Sì/No]
**USP presente e chiaro?**: [Sì/No — qual è]
**Benefits vs features?**: [% benefits / % features]
**Chiarezza post-acquisto?**: [presente/assente/necessaria]

### O — Obiezioni
**Obiezioni gestite**: [lista]
**Obiezioni non gestite**: [lista — CRITICAL se presenti]
**Framework CPB usato?**: [Sì/No]
**Prove credibili?**: [Sì/No + tipo]

### C — CTA
**Tipo CTA**: [Superficiale/Profondo]
**Micro-copy presente?**: [Sì/No]
**Urgenza presente?**: [Tipo / Assente]
**Coerente con il copy?**: [Sì/No]

---

## 🛡️ Obiezioni Rilevate Non Gestite

[Lista di affermazioni nel copy che generano dubbi nel target ma non vengono gestiti]
1. "[Frase che genera obiezione]" → Obiezione generata: [tipo] → Come gestirla: [soluzione]
2. [...]

---

## 📝 Copy Revisionato (sezione con il problema più grave)

[Riscrittura della sezione più problematica con le correzioni applicate]
```

---

## Quick Review (< 2 minuti)

```markdown
# Quick Review
Score: [__/100]

Top 3 problemi:
1. [Problema + fix in 1 riga]
2. [Problema + fix in 1 riga]
3. [Problema + fix in 1 riga]

Raccomandazione: [Usa così / Rivedi la sezione X / Riscivi da capo la sezione Y]
```

---

## Errori Più Comuni nel Copy (Red Flag List)

Questi errori abbassano il score automaticamente:

| Errore | Impatto | Come Riconoscerlo |
|---|---|---|
| Soluzione prima del problema | -15 | Prodotto menzionato prima del pain point |
| Headline generica | -10 | Potrebbe essere usata per qualsiasi prodotto |
| Features senza benefits | -8 | Elenco di caratteristiche tecniche senza "il che significa che..." |
| Obiezioni generate ma non gestite | -10 | Claim forti senza prove a supporto |
| CTA superficiale ("compra ora") | -5 | CTA non collegato al pain point |
| Linguaggio del marketer nel problem | -8 | "Pain point", "buyer journey", gergo marketing nel body copy |
| Tono arrogante senza giustificazione | -5 | Superlative non supportate da prove |
| Assenza di urgenza o conseguenza del non agire | -5 | Il target può rimandare senza costo percepito |
| Copy troppo lungo senza struttura visiva | -3 | Nessun titolo di sezione, nessun grassetto, paragrafi enormi |
| Ripetizioni inutili | -3/cad. | Stessa parola chiave ripetuta inutilmente |

---

## Struttura della Skill

```
copy-review/
├── SKILL.md                                    ← questo file (entry point)
├── references/
│   ├── scoring-guide.md                        ← criteri di punteggio per sezione APSOC, penalizzatori automatici, benchmark per tipo copy
│   └── riscrittura-patterns.md                 ← 7 pattern chirurgici: headline generica, show don't tell, features→benefits, obiezioni generate, CTA profonda, amplificazione dolore, transizione P→S
├── assets/
│   └── templates/
│       └── review-template.md                  ← template operativo 5-step: analisi strutturale → scoring → report → riscrittura sezione debole
└── agents/
    └── reviewer-agent.md                       ← A8: system prompt completo, 5 modalità review, processo fase per fase, regole non negoziabili, calibrazione score
```

## Routing Rapido

| Se hai bisogno di... | File |
|---|---|
| Sapere come assegnare il punteggio per ogni sezione | `references/scoring-guide.md` |
| Capire cosa penalizza automaticamente | `references/scoring-guide.md` |
| Pattern di fix chirurgico per un problema specifico | `references/riscrittura-patterns.md` |
| Come convertire features in benefits | `references/riscrittura-patterns.md` (Pattern 3) |
| Come riscrivere una CTA superficiale | `references/riscrittura-patterns.md` (Pattern 5) |
| Template completo per la revisione | `assets/templates/review-template.md` |
| System prompt agente revisore A8 | `agents/reviewer-agent.md` |
