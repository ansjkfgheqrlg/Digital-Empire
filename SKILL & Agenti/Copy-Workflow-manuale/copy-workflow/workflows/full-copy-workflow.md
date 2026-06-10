# Full Copy Workflow
> Pipeline completo: da zero a copy finale professionale

**Durata stimata**: 60-120 minuti (dipende dalla complessità)
**Quando usarlo**: Lanci importanti, sales page, campagne con budget significativo
**Attiva**: Tutti gli 8 agenti in sequenza

---

## Overview del Pipeline

```
INPUT: Descrizione prodotto + target + obiettivo
   │
   ▼
FASE 1 — STRATEGIA (A1 + A2 in parallelo)
   ├── A1: Briefing completo + obiettivi copy
   └── A2: Avatar + Pain Points + Language Map
   │
   ▼
FASE 2 — SCRITTURA APSOC (A3 → A7, sequenziale)
   ├── A3: Attention (3 headline + hook apertura)
   ├── A4: Problem (pain point amplificato)
   ├── A5: Solution (USP + benefits + post-acquisto)
   ├── A6: Objections (CPB per obiezioni principali)
   └── A7: CTA (closing + urgenza + micro-copy)
   │
   ▼
FASE 3 — QA (A8)
   ├── Assemblaggio coerente
   ├── Score APSOC (target: ≥80)
   └── Report miglioramenti
   │
   ▼
OUTPUT: Copy finale + QA report + Note strategiche
```

---

## Fase 1 — Briefing + Ricerca (30-45 min)

### Input Richiesto dall'Utente

```
OBBLIGATORI:
□ Prodotto/servizio (descrizione + prezzo)
□ Tipo di copy (ad / sales page / email / VSL / altro)
□ Target (anche descrizione generica)
□ Obiettivo (vendita diretta / lead gen / awareness)

UTILI MA NON OBBLIGATORI:
□ USP conosciuto
□ Testimonianze disponibili
□ Copy passati (cosa ha funzionato/non funzionato)
□ Competitor principali
□ Mood atteso (urgente / emozionale / professionale / comico)
```

### A1 — Briefing Analyst

**Spawn condition**: Sempre (salvo briefing completo già fornito)

**Task**:
1. Raccogliere tutti i dati dal briefing
2. Identificare o costruire l'USP
3. Definire la posizione del copy nel funnel
4. Documentare gap e rischi

**Output**: `briefing-completo.md` + `obiettivi-copy.md`

**Tempo**: 10-15 minuti

### A2 — Target Analyst

**Spawn condition**: Sempre (può girare in parallelo con A1)

**Task**:
1. Costruire buyer avatar completo
2. Mappare pain points e conseguenze
3. Creare language map (come parla il target)

**Output**: `avatar.md` + `pain-points.md` + `language-map.md`

**Tempo**: 15-20 minuti

### Gate Fase 1 → Fase 2

Prima di procedere alla scrittura, verifica:
- [ ] Briefing ha tutti i dati critici
- [ ] USP identificato (reale o finto)
- [ ] Avatar ha nome, età, problema preciso e almeno 3 obiezioni
- [ ] Language map ha almeno 5 frasi tipiche del target

Se mancano elementi critici → chiedi all'utente prima di procedere.

---

## Fase 2 — Scrittura APSOC (45-60 min)

### A3 — Attention Writer (10 min)

**Input**: briefing + avatar + pain-points
**Task**: Scrivere 3 headline + hook di apertura
**Output**: `attention-section.md`

**Checkpoint**: Presenta le 3 headline all'utente prima di procedere?
- Se copy è per A/B test → sì, fai scegliere
- Se pipeline automatico → procedi con la headline consigliata

### A4 — Problem Writer (10 min)

**Input**: tutto precedente + attention-section
**Task**: Sezione problema amplificata
**Output**: `problem-section.md`

**Regola critica**: Nessuna menzione del prodotto in questa sezione.

### A5 — Solution Writer (10 min)

**Input**: tutto precedente + problem-section
**Task**: Presentazione prodotto + USP + benefits + post-acquisto
**Output**: `solution-section.md`

### A6 — Objections Handler (10 min)

**Input**: tutto precedente + solution-section
**Task**: CPB per almeno 2 obiezioni principali (3 per sales page)
**Output**: `objections-section.md`

**Nota**: Se mancano prove reali → usa processi logici + showoff + garanzie ipotetiche (segnalate).

### A7 — CTA Writer (5-10 min)

**Input**: tutto il precedente
**Task**: CTA profondo + urgenza + micro-copy
**Output**: `cta-section.md`

---

## Fase 3 — QA e Assemblaggio (15-20 min)

### A8 — Copy Reviewer

**Task**:
1. Assemblare tutte le sezioni in un copy coerente
2. Applicare la checklist APSOC (100 punti)
3. Identificare e segnalare problemi critici

**Gate di qualità**:
- Score ≥ 80 → Consegna diretta
- Score 70-79 → Consegna con note, 1 iterazione suggerita
- Score < 70 → Rilancia l'agente con score peggiore

**Max iterazioni per agente**: 2 prima di escalation utente

---

## Output Finale

### Pacchetto Consegnato

```
copy-finale.md           → Il copy completo pronto per l'uso
qa-report.md             → Score + problemi + suggerimenti
briefing-completo.md     → Documentazione di riferimento
avatar.md                → Buyer persona per future campagne
note-strategiche.md      → Decisioni chiave prese durante il run
```

### Note Strategiche (auto-generate)

Il sistema documenta automaticamente:
- Headline scelta + perché
- Strategia problema usata + perché
- USP: reale o finto (e com'è stato costruito)
- Obiezioni gestite + prove usate
- Tipo di urgenza nel CTA + motivazione

---

## Varianti del Full Workflow

### Versione Accelerata (30-45 min)

Salta:
- `language-map.md` (A2 semplificato)
- CPB per obiezioni secondarie (A6 lite)
- 2 delle 3 headline alternative (A3 → solo 1 headline top)

Usa quando: deadline stretta, prodotto semplice, target già noto.

### Versione Estesa (2-3 ore)

Aggiungi:
- Analisi copy competitor (A1 ampliato)
- 5 headline con analisi A/B test setup
- CPB per 4+ obiezioni
- Variante copy per mobile vs desktop
- Sequenza email di follow-up (3-5 email)

Usa quando: lancio prodotto importante, budget advertising alto, vuoi massimizzare il CR.

---

## Checklist Pre-Lancio

Prima di pubblicare il copy generato:

### Copy
- [ ] Headline testata internamente (mostrala a 3 persone del target)
- [ ] Nessun errore grammaticale
- [ ] Promesse verificabili (nessuna affermazione falsa)
- [ ] Lunghezza appropriata al formato
- [ ] Struttura visiva invitante (paragrafi, grassetti, titoli)

### Business
- [ ] Il CTA funziona (link, pulsante, form)
- [ ] Il post-acquisto descritto corrisponde alla realtà
- [ ] Le testimonianze usate sono reali e approvate
- [ ] Le garanzie offerte sono effettivamente erogabili
- [ ] Non ci sono violazioni legali per il settore

### Technical
- [ ] Copy ottimizzato per mobile (se applicabile)
- [ ] Meta descrizione scritta (per landing page)
- [ ] Tag UTM configurati per tracking

---

## Troubleshooting

| Problema | Soluzione |
|---|---|
| Target troppo vago | Torna a A2 con più domande specifiche |
| USP non esiste | Costruisci USP finto (guida in A5) |
| Nessuna prova disponibile | Usa processi logici + showoff + garanzie |
| Copy troppo lungo | A8 produce versione condensata |
| Tono sbagliato | Rilancia A3-A7 con vincolo di tono da language-map |
| Score QA basso su Problema | Rilancia A4 con istruzione "più show don't tell" |
| Score QA basso su Obiezioni | Rilancia A6 con lista obiezioni specifiche da gestire |
