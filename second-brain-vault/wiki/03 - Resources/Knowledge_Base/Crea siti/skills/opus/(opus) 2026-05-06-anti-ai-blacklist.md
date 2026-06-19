# ANTI-AI-BLACKLIST
            
> Path: [[Map - Crea_Siti|Crea siti > skills > opus]]

## Content

# ANTI-AI BLACKLIST — Pattern Proibiti OPUS
> Queste regole si applicano in OGNI fase di ogni progetto OPUS.
> Qualsiasi violazione viene segnalata come BLOCKER e blocca il progresso alla fase successiva.
> opus-director le conosce a memoria e le verifica attivamente.

---

## FONT VIETATI

### Font PROIBITI come font principale
- **Inter** — il font più usato dall'AI, segnala immediatamente generazione automatica
- **Roboto** — Google Material Design default, generico al massimo
- **Arial** — system fallback, comunica "nessuna scelta tipografica"
- **Helvetica** — corporate anni '90, senza personalità nel contesto web
- **system-ui / -apple-system** — usato da chi non ha scelto nulla
- Qualsiasi sans-serif generico "di default" senza personalità

### Font APPROVATI (hanno carattere, non generici)
Sans-serif con personalità: Satoshi, Cabinet Grotesk, DM Sans, Plus Jakarta Sans, Space Grotesk, Outfit, Sora, Epilogue, Geist
Serif con carattere: Cormorant Garamond, Playfair Display, Lora, Fraunces, DM Serif Display, Libre Baskerville
Font variabili: preferire sempre versioni variabili dove disponibili

---

## COLORI VIETATI

### Palette AI-generica (proibita)
- **Purple gradient su sfondo bianco** — #8B5CF6, #6366F1, #7C3AED e varianti → il segnale più forte di AI
- **Blue-to-purple gradient** — la combo più abusata nei siti AI
- **Teal-to-blue gradient** — secondo pattern più comune
- **Pure black #000000** come colore di testo o background principale
- **Pure white #FFFFFF** come background principale (off-white warm è OK)
- **4-5 colori distribuiti in modo uniforme** — senza gerarchia, tutti "uguali"
- Colori con saturazione > 65% come colore dominante del sito
- Qualsiasi palette che "sembra Figma Community template"

### Regola Silver-Mixed (obbligatoria)
OGNI colore nel sito — incluso il brand primary — deve essere silver-mixed:
- Saturazione ridotta del 20-35% rispetto al colore base
- Luminosità aumentata del 5-10%
- Nessun colore completamente saturo, nemmeno il brand
- Test: il colore sembra "stampato su carta patinata di lusso"? → approvato

---

## LAYOUT VIETATI

### Pattern strutturali AI-generici
- **Button pill-shape ovunque** — border-radius: 9999px come stile unico di tutti i bottoni
- **Layout 2-3 colonne simmetriche identiche** — grid uniforme che non cambia mai
- **Gap uguale ovunque** — stesso spacing applicato a tutto indiscriminatamente
- **Hero: headline + subheadline + CTA button centrati** — esattamente al centro, icone sotto → il pattern più inflazionato
- **Card grid 3 colonne con icona + titolo + testo** → AI pattern per eccellenza
- **Corporate design anni 2010** — box-shadow ovunque, card ovunque, tutto boxed, tutto uguale
- **Sezioni alternate colore chiarissimo/scurissimo** in sequenza regolare e prevedibile

### Layout APPROVATI
- Asimmetria intenzionale: ratios 7/5, 8/4, 3/7 invece di sempre 6/6
- Full-bleed + container alternati con intenzione
- Grid che cambia da sezione a sezione (non sempre la stessa)
- Un elemento dominante per sezione, non gerarchia uguale su tutto

---

## COMPORTAMENTO UI VIETATO

### Animazioni
- Transizioni istantanee (nessun easing, nessuna curva) — tutto appare/scompare di scatto
- Animazioni decorative senza funzione — si muovono "perché sì"
- Hover states identici al default (nessun feedback visivo)
- Float animation su icone o immagini senza motivo
- Scroll animations su TUTTO (ogni singolo elemento che appare con fadeUp identico)
- Duration > 1200ms per qualsiasi animazione singola

### Testo
- CTA generico: "Scopri di più", "Clicca qui", "Inizia ora" senza contesto
- Headline che inizia con "Benvenuto" o "Scopri"
- Subheadline che ripete l'headline con parole diverse
- Testo che dice "Siamo una azienda leader nel settore" o simili
- Feature list: feature tecnica prima, beneficio mai
- Font-weight 700+ (bold pieno) nel corpo del testo come stile dominante
- Title Case su tutti gli headings → stile corporate/generico
- Lorem ipsum o placeholder text nel prodotto finale

### Struttura
- Stessa sezione "hero uguale" per ogni tipo di sito
- FAQ con domande generiche che nessuno pone realmente
- "I nostri valori" con icone decorative e testo vago
- Team grid con foto stock di persone che non esistono
- Testimonianze senza nome, cognome, azienda reali
- Prezzi "a partire da" senza specificare per cosa

---

## TEST DI VERIFICA ANTI-AI

### Test 1 — Il Test del Concorrente
"Un altro sito nel mio stesso settore potrebbe usare esattamente questo design?"
→ Se SÌ: il design non è abbastanza specifico. Ripartire da aesthetic axis.

### Test 2 — Il Test dell'Agenzia
"Se questo sito fosse presentato da un'agenzia di lusso da $50.000, sembrerebbe credibile?"
→ Se NO: identificare esattamente gli elementi che abbassano la percezione.

### Test 3 — Il Test del Font
"Se coprissimo tutti i testi e guardiamo solo la forma delle lettere, la tipografia ha carattere?"
→ Se NO: cambiare font. Il font è la prima cosa che comunica o non comunica qualità.

### Test 4 — Il Test del Colore
"I colori di questo sito sono silver-mixed (leggermente desaturati e prezioso)?"
→ Se NO: applicare il processo silver-mixing a tutti i colori.

### Test 5 — Il Test dello Spacing
"Se raddoppiassimo lo spazio bianco in ogni sezione, il sito migliorerebbe?"
→ Se SÌ: c'è ancora troppa compressione. Aumentare lo spacing.

### Test 6 — Il Test della Grana
"Ogni singolo sfondo ha la texture grain (SVG fractalNoise, background-size ≤ 200px)?"
→ Se NO: aggiungere il grain layer. Non è opzionale.

### Test 7 — Il Test della Gerarchia
"Guardando il sito al 20% di zoom, si distinguono chiaramente 4-5 livelli di testo?"
→ Se NO: la gerarchia tipografica non è abbastanza marcata.

---

## COME USA QUESTA LISTA OPUS-DIRECTOR

1. **Phase 4.1** — verifica aesthetic axis contro Test 1 e Test 2
2. **Phase 4.7** — Design Tokens Lock: ogni token passa la blacklist
3. **Phase 9, Pass 1** — ANTI-AI PASS: controlla OGNI elemento del sito
4. **In qualsiasi momento** — se opus-director vede una violazione, la segnala come BLOCKER

Formato del BLOCKER:
```
🚨 BLOCKER — ANTI-AI VIOLATION
Elemento: [descrizione]
Regola violata: [regola dalla blacklist]
Fix richiesto: [come correggere]
Fase: non si procede fino alla risoluzione
```

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
