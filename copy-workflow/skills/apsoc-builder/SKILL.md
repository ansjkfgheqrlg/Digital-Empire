# APSOC Builder — Skill
> Genera copy persuasivo completo seguendo il framework APSOC in modalità interattiva

## Invocazione

```
/apsoc [tipo-copy] [prodotto]
```

Esempi:
- `/apsoc ad "corso di copywriting"`
- `/apsoc sales-page "software di gestione clienti"`
- `/apsoc email "consulenza marketing"`

Invocazione naturale: "scrivi un'ad per X usando APSOC" o "costruisci il copy per X"

---

## Il Framework APSOC in Pillole

```
A → Attenzione    Cattura. Vendi la lettura, non il prodotto.
P → Problema      Descrivi il dolore. Prima il problema, poi la soluzione.
S → Soluzione     Presenta il prodotto come risposta naturale.
O → Obiezioni     Anticipa i dubbi. Gestiscili con CPB.
C → Call to Action Chiedi l'azione. Sii specifico, profondo, urgente.
```

---

## Processo Interattivo

### Step 1 — Raccolta Dati Minimi (3 domande)

```
Domanda 1: Cosa vendi? (prodotto/servizio + prezzo indicativo)
Domanda 2: A chi? (descrivi il tuo cliente ideale in 2-3 righe)
Domanda 3: Che tipo di copy? (ad / sales page / email / landing page / post social)
```

Se l'utente vuole saltare → usa defaults ragionevoli e segnalali.

### Step 2 — Proposta Struttura

Prima di scrivere, mostra il piano:
```
STRUTTURA APSOC PROPOSTA per [Prodotto] — [Tipo Copy]

A: Strategia headline → [Curiosità / Pain Point / USP / Urgenza]
   Motivo: [perché questa strategia per questo target]

P: Approccio problema → [Storytelling / Scenario / Domanda / Statistica]
   Pain point principale: [...]

S: USP identificato → [...]
   Top 3 benefits: [...]

O: Obiezioni principali → [...]
   Prove da usare: [...]

C: Tipo CTA → [Profondo / Urgenza di tempo / Conseguenza del non agire]

Lunghezza stimata: [X parole]

Procedo? (o vuoi modificare qualcosa?)
```

### Step 3 — Scrittura Sezione per Sezione

Scrivi il copy sezione per sezione, mostrando ogni sezione separatamente con un commento strategico.

### Step 4 — Assemblaggio e Revisione

Assembla, presenta il copy completo e il QA score sintetico.

---

## Output

### Copy Completo con Note Strategiche

```markdown
---
COPY: [Nome Prodotto]
Tipo: [tipo copy]
Score APSOC: [X/100]
---

## HEADLINE
[Testo headline]

💡 Strategia: [spiegazione in 1 riga]

---

## APERTURA / ATTENZIONE
[Testo]

---

## PROBLEMA
[Testo]

⚠️ Pain point: [quale leva emotiva è stata usata]

---

## SOLUZIONE
[Testo]

🎯 USP: [l'USP usato]

---

## OBIEZIONI
[Testo]

🛡️ Obiezioni gestite: [lista]

---

## CTA
[Testo]

⚡ Urgenza: [tipo e motivazione]

---
PAROLE TOTALI: [n]
```

---

## Varianti Copy

Dopo il copy principale, offri automaticamente:
1. **Versione A/B headline**: Headline alternativa con strategia diversa
2. **Versione corta**: Se il copy è lungo, versione condensata per ads
3. **Versione email**: Adattamento per email marketing

---

## Modalità Rapida (Quick APSOC)

Per chi ha fretta: `/apsoc quick [prodotto in 1 frase]`

Produce copy in < 2 minuti con:
- 1 headline
- Apertura + problema in 3 righe
- Soluzione + USP in 2 righe
- CTA diretto

Nessuna domanda interattiva — usa defaults ottimistici e segnala i gap.

---

## Struttura della Skill

```
apsoc-builder/
├── SKILL.md                                    ← questo file (entry point)
├── references/
│   └── sezione-per-sezione.md                  ← guida operativa completa: 6 strategie headline, 4 livelli amplificazione, show don't tell, ponte P→S, framework CPB in sezione O, anatomia CTA profonda, errori comuni per sezione
├── assets/
│   └── templates/
│       └── apsoc-canvas.md                     ← canvas pre-scrittura: 5 sezioni compilabili (A/P/S/O/C), checklist pre-scrittura, verifica USP, traduzione features→benefits
└── agents/
    └── apsoc-conductor.md                      ← orchestratore processo: 6 fasi (briefing → plan → produzione → assemblaggio → QA → A8), modalità rapida, gestione gap, routing interno
```

## Routing Rapido

| Se hai bisogno di... | File |
|---|---|
| Come scegliere la strategia headline per awareness level | `references/sezione-per-sezione.md` |
| Scrivere una sezione P con amplificazione a 4 livelli | `references/sezione-per-sezione.md` |
| Come costruire il ponte narrativo P→S | `references/sezione-per-sezione.md` |
| Errori comuni per ogni sezione APSOC | `references/sezione-per-sezione.md` |
| Pianificare il copy prima di scrivere | `assets/templates/apsoc-canvas.md` |
| Processo completo produzione copy (6 fasi) | `agents/apsoc-conductor.md` |
| Routing verso altre skill (headline, obiezioni, review) | `agents/apsoc-conductor.md` |
