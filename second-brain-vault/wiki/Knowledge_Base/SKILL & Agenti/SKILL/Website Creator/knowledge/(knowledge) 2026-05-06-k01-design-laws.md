# K01-design-laws
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Website Creator > knowledge]]

## Content

# K01 — LE 5 LEGGI D'ORO DEL DESIGN

> Queste 5 leggi si aggiungono alla Legge Cosmica (K00) e sono non negoziabili. Ogni sito prodotto da questo sistema deve rispettarle tutte e 5.

---

## LEGGE 1 — GRAIN TEXTURE DOPPIO LAYER

**Regola:** Ogni `<section>` del sito deve contenere il doppio layer grana. Nessuna sezione è piatta.

**Perché:** La grana aggiunge profondità tattile, simula materiali premium (pellicola fotografica, carta di lusso, metallo lavorato). Una sezione senza grana sembra digitale, economica, vuota.

**Come applicarla:** Vedi K02 per il codice esatto. Il pattern è:
- Layer 1: Film grain (URL esterno, filtri CSS aggressivi)
- Layer 2: Digital noise (SVG feTurbulence inline, opacità screen)
- (Opzionale) Layer 3: Grid sottile su sfondi molto scuri

**Verifica:** Ogni `<section>` ha almeno 2 `<div>` con `pointer-events:none` e `position:absolute` per la grana.

---

## LEGGE 2 — PATTERN INTERRUPT DARK↔LIGHT

**Regola:** Non possono esserci più di 2-3 sezioni consecutive dello stesso tono. Deve esserci almeno 1 sezione chiara ogni 3 sezioni scure (o viceversa).

**Perché:** Il pattern interrupt mantiene l'attenzione. La monotonia visiva fa scorrere la pagina senza leggere. Il contrasto drammatico dark→light obbliga l'occhio a rileggere da capo.

**Palette sfondi approvata:**
- Scuri: `#020202`, `#0a0a0a`, `#0f2e4a`, `#031c16`
- Medi: `#1a1a2e`, `#0d1b2a`
- Chiari: `#DCD8CF` (beige argentato), `#F8F6F2` (bianco caldo), `#E8E4DC`

**Pattern tipico:**
```
Hero (dark) → Benefits (dark) → [INTERRUPT] Product Mockup (light/beige)
→ Author (dark) → Testimonials (dark) → [INTERRUPT] FAQ (light) → Footer (dark)
```

**Verifica:** Scansiona gli sfondi delle sezioni in ordine — trovi almeno 1 sezione chiara ogni 3 scure.

---

## LEGGE 3 — TYPOGRAPHY LOWERCASE + STRONG

**Regola A — Tutto lowercase:**
Tutti i titoli e i testi sono in minuscolo. Nessun `ALL CAPS` tranne abbreviazioni (CTA, FAQ, SEO). `text-transform: lowercase` o scritto direttamente in minuscolo nell'HTML.

**Perché:** Il lowercase è più leggibile, più moderno, meno aggressivo. Il lusso non urla — sussurra con autorità.

**Regola B — Strong visibile:**
In ogni `<p>` e `<li>`, almeno 1-2 parole sono racchiuse in `<strong>`. Il `<strong>` deve essere visivamente distinto dal corpo testo:
- Su sfondo scuro: corpo `color: #94A3B8` (silver muted), `<strong>` `color: #E2E8F0` (silver chiaro) + `font-weight: 700-800`
- Su sfondo chiaro: corpo `color: #374151`, `<strong>` `color: #020202` + `font-weight: 700-800`

**CSS obbligatorio:**
```css
p { font-weight: 300; color: #94A3B8; line-height: 1.7; }
p strong { font-weight: 700; color: #E2E8F0; }
li { font-weight: 300; color: #94A3B8; }
li strong { font-weight: 700; color: #E2E8F0; }

/* Su sezioni chiare */
.section-light p { color: #374151; }
.section-light p strong { color: #020202; font-weight: 800; }
```

**Verifica:** Ogni `<p>` e `<li>` nel file ha almeno 1 `<strong>`.

---

## LEGGE 4 — ALMENO 1 SVG DIVIDER NOTEVOLE

**Regola:** Tra le sezioni principali deve esserci almeno 1 divisore SVG della libreria (K03). Non basta un `border-top`. Il divisore deve avere il gradient metallic oro-silver.

**Divisori disponibili (K03):**
1. **LuxArc** — arco a V, separa dark→light, elegante
2. **LuxV** — V verso il basso, separa light→dark, drammatico
3. **LuxCurve** — curva quadratica, sezione inizia curva (IL PIÙ BELLO)
4. **LuxTriangle** — triangolo clip-path CSS, dark sections
5. **InclinedStrip** — striscia metallica inclinata -2.5°, veloce da inserire

**Quando usare quale:**
- Da dark section a light section → LuxArc
- Da light section a dark section → LuxV o LuxCurve
- Divisore veloce tra due dark sections → InclinedStrip
- Sezione hero con entrata drammatica → LuxTriangle

**Verifica:** L'HTML finale ha almeno 1 elemento SVG con stroke e il gradient metallic.

---

## LEGGE 5 — ALMENO 1 SEZIONE CON BORDO CURVO

**Regola:** Almeno una sezione deve avere il bordo superiore curvato via clip-path quadratic bezier o SVG clipPath. Questo crea il passaggio più elegante tra sezioni.

**Tecnica LuxCurve (la preferita):**
```css
/* La sezione che inizia curva */
.section-curved {
  clip-path: path('M 0,40 Q 50%,0 100%,40 L 100%,100% L 0,100% Z');
  /* oppure con percentuali */
  clip-path: ellipse(55% 8% at 50% 0%);
  padding-top: 80px; /* compensa il clip */
}
```

**Tecnica SVG clipPath inline:**
```html
<svg style="position:absolute;width:0;height:0">
  <defs>
    <clipPath id="curve-top" clipPathUnits="objectBoundingBox">
      <path d="M 0,1 Q 0.5,0 1,1 V 1.1 H 0 Z"/>
    </clipPath>
  </defs>
</svg>
<section style="clip-path:url(#curve-top); padding-top:60px;">
  <!-- contenuto -->
</section>
```

**Verifica:** C'è almeno 1 sezione con `clip-path` contenente `Q` (quadratic bezier) o `ellipse`.

---

## CHECKLIST RAPIDA (5 LEGGI)

Prima di consegnare:

```
[ ] L1 GRAIN: ogni <section> ha 2 div grana con position:absolute e pointer-events:none?
[ ] L2 INTERRUPT: c'è almeno 1 sezione chiara ogni 3 scure?
[ ] L3 LOWERCASE: tutti i titoli sono in minuscolo?
[ ] L3 STRONG: ogni <p> e <li> ha almeno 1 <strong>?
[ ] L4 DIVIDER: c'è almeno 1 SVG divisore con gradient metallic?
[ ] L5 CURVA: c'è almeno 1 sezione con clip-path curvo (Q o ellipse)?
```

Se manca anche uno solo → il sito non è pronto per la consegna.

---

## GERARCHIA DELLE LEGGI

```
K00 — Legge Cosmica (colori argentizzati) — ASSOLUTA
  ↓
K01 — 5 Leggi d'Oro — NON NEGOZIABILI
  ↓
K02 — Codice grana esatto
K03 — Libreria divisori esatta
K04-K08 — Sistemi specifici
  ↓
K09/K10/K11 — Regole per categoria
```

Una violazione a K00 o K01 invalida l'intero sito.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
