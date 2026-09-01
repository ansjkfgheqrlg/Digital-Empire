# AG-6 — Motion Concepts
> Momento Anti-Gravity #6 | Fase 8.1 — Motion Engineering Strategy
> Usa questo template prima di scegliere le animazioni per esplorare idee innovative.

---

## Quando usare questo template

**Fase:** 8.1 — prima di iniziare il motion engineering, dopo che il sito è stato builddato
**Obiettivo:** scoprire concetti di motion innovativi e non ovvi per l'aesthetic del progetto

---

## Struttura del Prompt AG-6

```
Sei un motion designer e interaction designer senior.
Sto progettando le animazioni per questo sito:

CONTESTO:
Tipo sito: [es. landing page info business / SaaS / portfolio]
Aesthetic axis: [nome movimento]
Stack tecnico: [A: HTML+GSAP / B: React+Motion / C: altro]
Settore: [settore]
Audience: [descrizione — specialmente: sono tech-savvy? apprezzano le animazioni?]

STRUTTURA PAGINA (PATH A — 15 sezioni):
[lista delle sezioni presenti nel sito]

WOW MOMENTS CANDIDATI CHE HO IDENTIFICATO:
1. [sezione/momento candidato 1]
2. [sezione/momento candidato 2]
3. [sezione/momento candidato 3]

ANIMAZIONI STANDARD GIÀ PREVISTE (le includo sempre):
- Scroll reveal su card/grid (fade-up + stagger 60ms)
- Hero entrance sequence (timeline orchestrata 1.1s)
- Navbar scroll shrink + backdrop-filter
- Counter animation su statistiche

---

CHIEDO:
1. WOW MOMENTS REVIEW: I miei 3 candidati sono le scelte giuste per [aesthetic axis]?
   C'è uno che è "troppo SaaS/tech" per questo settore? Quale lo sostituiresti e con cosa?

2. SIGNATURE MOTION: Qual è il gesto/animazione "firma" che potrebbe diventare
   riconoscibile come parte del brand di questo sito?
   Non deve essere complesso — spesso le animazioni più memorabili sono sottilissime.
   Es: "ogni H2 che entra in viewport porta con sé una linea silver che si disegna sotto"

3. MICRO-INTERACTIONS NON OVVIE: 5 micro-animazioni sottili che un visitatore
   non nota consapevolmente ma che contribuiscono alla sensazione di "premium".
   Specifico per [aesthetic axis] e [settore].

4. MOTION COME NARRATIVA: C'è un modo in cui la sequenza di animazioni della pagina
   può raccontare la storia del brand dall'alto al basso? Come il motion stesso diventa copy?

5. COSA EVITARE: Per [aesthetic axis] + [audience], quali animazioni sembrano
   immediatamente "sito economico" o "AI-generated"? Lista con spiegazione del perché.

6. PERFORMANCE VS POETRY: Se devo scegliere tra un'animazione molto bella (costosa
   in performance) e una più semplice (leggerissima), qual è la soglia?
   Per questo tipo di sito, quale % di visitatori ha hardware che supporta animazioni ricche?
```

---

## Come usare l'output

1. **Scegli** il signature motion — implementalo come primo elemento speciale
2. **Seleziona** 3-5 micro-interactions da includere nel js/animations.js
3. **Valuta** il motion-as-narrative — se fattibile, annota in OPUS-STATUS.md
4. **Aggiungi** alla lista "Da evitare" del Polish Loop Pass 6
5. **Calibra** complessità in base alla soglia performance suggerita

Di' a opus-director: "AG-6 completato, motion strategy definita" → procede con /site animate.
