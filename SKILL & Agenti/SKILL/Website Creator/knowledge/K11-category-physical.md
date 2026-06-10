# K11 — CATEGORIA: PRODOTTI FISICI / E-COMMERCE / DTC

> Struttura, stili e pattern per prodotti fisici: cosmetici, integratori, lifestyle, gadget, food.

---

## STRUTTURA SEZIONI (ordine ottimale)

```
1. [NAV]           Nav sticky con icona carrello
2. [HERO]          Hero — product shot dominante + ATC button
3. [OVERVIEW]      Product Overview — prezzo + rating + varianti + ATC
4. [DIVIDER]       LuxV
5. [PROBLEM]       Problem/Need — perché questo prodotto è necessario
6. [DIVIDER]       LuxCurve (sezione benefits curva)
7. [BENEFITS]      Benefits — 5-7 benefici specifici
8. [DIVIDER]       InclinedStrip
9. [INGREDIENTS]   Ingredienti/Componenti — cosa c'è dentro
10. [DIVIDER]      LuxArc (dark → light)
11. [HOW TO USE]   Come si usa — 3-4 step semplici
12. [DIVIDER]      LuxV
13. [GALLERY]      Galleria prodotto — foto da angolazioni diverse
14. [DIVIDER]      InclinedStrip
15. [TESTIMONIALS] Testimonianze + UGC — recensioni + foto reali
16. [TRUST]        Trust indicators — certificazioni, spedizione, garanzie
17. [DIVIDER]      LuxArc
18. [SCARCITY]     Scarcity/Urgency — offerta limitata
19. [CTA]          CTA finale con ATC
20. [DIVIDER]      LuxV
21. [FAQ]          FAQ
22. [FOOTER]       Footer
```

---

## STILI PER SOTTO-CATEGORIA

### Luxury Cosmetics / Skincare
- **Palette:** PALETTE 1 (oro/silver) o PALETTE 7 (rosa silver)
- **Sfondo:** bianco caldo `#F8F6F2` + accenti nero `#020202`
- **Whitespace:** generoso — il prodotto respira
- **Font:** Cinzel per titoli, Inter light per body
- **Tono:** Esclusivo, ritualistico ("il tuo rituale serale"), scientifico-elegante
- **Visual:** foto clean su sfondo bianco o marble texture

### Fitness / Supplements / Sport
- **Palette:** PALETTE 2 (verde) o PALETTE 8 (arancione)
- **Sfondo:** scuro dominante `#020202`
- **Tono:** Energico, performativo, bold ("massimizza ogni allenamento")
- **Visual:** before/after, atleta in azione, packaging prominente

### Lifestyle / DTC / Casa
- **Palette:** PALETTE 8 (arancione/terracotta silver) o PALETTE 9 (teal)
- **Sfondo:** earth tones argentati — `#E8E0D4`, `#DCD8CF`
- **Tono:** Caldo, quotidiano, desiderabile ("il dettaglio che trasforma la tua giornata")

### Mass-Market / Consumer Goods
- **Palette:** PALETTE 5 (blu) o PALETTE 1 (oro)
- **Sfondo:** bianco/chiaro dominante per accessibilità
- **Tono:** Chiaro, diretto, valore prominente, rating grandi

---

## SEZIONI SPECIFICHE — DETTAGLIO

### HERO PRODOTTO FISICO
```
Struttura:
- Layout: product shot 60-70% dell'hero (dominante)
- Headline: beneficio principale (non nome prodotto)
  Esempio: "la pelle che hai sempre voluto — in 28 giorni"
  Esempio: "more energy. better focus. zero crash."
- Subheadline: key ingredients + risultato
- Rating + numero recensioni (sotto headline)
- ATC button: full-width su mobile, 280px+ su desktop
- Price display: prezzo barrato + prezzo scontato + badge %
- Micro-copy: "spedizione gratuita · resi gratuiti · [N] in stock"
```

### ATC BUTTON (Add to Cart — sempre visible)
```html
<!-- ATC sticky su mobile -->
<div id="atc-sticky" style="
  display:none; /* mostrato da JS quando hero esce dallo schermo */
  position:fixed;
  bottom:0; left:0; right:0;
  padding:12px 16px;
  background:rgba(2,2,2,0.97);
  border-top:1px solid rgba(227,200,120,0.2);
  z-index:90;
  backdrop-filter:blur(8px);
">
  <div style="display:flex;gap:12px;align-items:center;max-width:480px;margin:0 auto;">
    <div>
      <div style="font-size:0.8125rem;color:#94A3B8;">[NOME PRODOTTO]</div>
      <div style="font-family:'Cinzel',serif;font-size:1rem;color:#E3C878;">[PREZZO]</div>
    </div>
    <button style="flex:1;padding:14px;font-size:0.875rem;font-weight:700;color:#020202;background:linear-gradient(135deg,#E3C878,#D4AF37);border:none;border-radius:2px;cursor:pointer;">aggiungi al carrello</button>
  </div>
</div>

<script>
window.addEventListener('scroll', function() {
  var hero = document.getElementById('hero-section');
  if (!hero) return;
  var heroBottom = hero.getBoundingClientRect().bottom;
  var sticky = document.getElementById('atc-sticky');
  sticky.style.display = heroBottom < 0 ? 'block' : 'none';
});
</script>
```

### INGREDIENTS / COMPONENTI
```
Due formati:

1. Lista con icone (mass-market, supplements):
- Grid 2-3 colonne
- Icona ingrediente + nome + beneficio specifico
- Badge "clinicamente testato" o "naturale al 100%"

2. Cards con storia sourcing (luxury):
- Card singola per ingrediente chiave
- Origine geografica ("olio d'argan dal Marocco")
- Proprietà specifica + percentuale formulazione
- Immagine ingrediente grezzo
```

```html
<!-- Lista ingredienti formato grid -->
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;">
  <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:4px;padding:20px;text-align:center;">
    <div style="font-size:2rem;margin-bottom:8px;">[ICONA]</div>
    <div style="font-family:'Cinzel',serif;font-size:0.875rem;color:#E2E8F0;margin-bottom:6px;">[INGREDIENTE]</div>
    <div style="font-size:0.8125rem;color:#94A3B8;"><strong>[BENEFICIO]</strong></div>
  </div>
</div>
```

### HOW TO USE (3-4 step)
```
Stile numeri grandi Cinzel + frecce o linea connettore:
Step 1: [AZIONE SEMPLICE] — [quanto tempo/quanto]
Step 2: [AZIONE] — [dettaglio]
Step 3: [RISULTATO ATTESO]
Step 4: (opzionale) [RIPETI / CICLO]
```

### GALLERY PRODOTTO (slider vanilla)
```html
<div style="position:relative;overflow:hidden;">
  <div id="gallery-track" style="display:flex;transition:transform 0.4s ease;gap:16px;">
    <div style="min-width:calc(50% - 8px);height:400px;background:linear-gradient(135deg,[COLORE1],[COLORE2]);border-radius:4px;display:flex;align-items:center;justify-content:center;color:#374151;">[IMMAGINE 1]</div>
    <div style="min-width:calc(50% - 8px);height:400px;background:linear-gradient(135deg,[COLORE2],[COLORE3]);border-radius:4px;display:flex;align-items:center;justify-content:center;color:#374151;">[IMMAGINE 2]</div>
    <!-- altre immagini -->
  </div>
  <!-- Controlli -->
  <button onclick="galleryPrev()" style="position:absolute;left:16px;top:50%;transform:translateY(-50%);width:40px;height:40px;border-radius:50%;background:rgba(2,2,2,0.8);border:1px solid rgba(255,255,255,0.1);color:#E2E8F0;cursor:pointer;font-size:1.25rem;">‹</button>
  <button onclick="galleryNext()" style="position:absolute;right:16px;top:50%;transform:translateY(-50%);width:40px;height:40px;border-radius:50%;background:rgba(2,2,2,0.8);border:1px solid rgba(255,255,255,0.1);color:#E2E8F0;cursor:pointer;font-size:1.25rem;">›</button>
</div>

<script>
var galleryIndex = 0;
function galleryMove(dir) {
  var track = document.getElementById('gallery-track');
  var items = track.children.length;
  galleryIndex = (galleryIndex + dir + items) % items;
  var itemW = track.children[0].offsetWidth + 16;
  track.style.transform = 'translateX(-' + (galleryIndex * itemW) + 'px)';
}
function galleryPrev(){ galleryMove(-1); }
function galleryNext(){ galleryMove(1); }
</script>
```

### UGC GRID (User Generated Content)
```html
<!-- Grid stile Instagram -->
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;max-width:900px;margin:0 auto;">
  <div style="aspect-ratio:1;background:rgba(255,255,255,0.05);border-radius:4px;overflow:hidden;position:relative;cursor:pointer;" onmouseover="this.querySelector('.ugc-overlay').style.opacity='1'" onmouseout="this.querySelector('.ugc-overlay').style.opacity='0'">
    <div style="width:100%;height:100%;background:linear-gradient(135deg,[COLORE1],[COLORE2]);display:flex;align-items:center;justify-content:center;color:#374151;font-size:0.875rem;">[FOTO CLIENTE]</div>
    <div class="ugc-overlay" style="position:absolute;inset:0;background:rgba(2,2,2,0.7);display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity 0.3s;opacity:0;padding:16px;text-align:center;">
      <div style="color:#E3C878;font-size:0.875rem;margin-bottom:4px;">★★★★★</div>
      <div style="color:#CBD5E1;font-size:0.8125rem;">"[BREVE QUOTE]"</div>
      <div style="color:#94A3B8;font-size:0.75rem;margin-top:8px;">— [NOME]</div>
    </div>
  </div>
  <!-- Ripeti per altri 8 foto -->
</div>
```

### TRUST INDICATORS
```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:24px;text-align:center;padding:40px 0;">

  <div>
    <div style="font-size:2rem;margin-bottom:8px;">🚀</div>
    <div style="font-family:'Cinzel',serif;font-size:0.875rem;color:#E2E8F0;margin-bottom:4px;">spedizione rapida</div>
    <div style="font-size:0.8125rem;color:#64748B;"><strong>24-48 ore</strong> garantite</div>
  </div>

  <div>
    <div style="font-size:2rem;margin-bottom:8px;">↩</div>
    <div style="font-family:'Cinzel',serif;font-size:0.875rem;color:#E2E8F0;margin-bottom:4px;">resi gratuiti</div>
    <div style="font-size:0.8125rem;color:#64748B;"><strong>30 giorni</strong> senza costi</div>
  </div>

  <div>
    <div style="font-size:2rem;margin-bottom:8px;">🔒</div>
    <div style="font-family:'Cinzel',serif;font-size:0.875rem;color:#E2E8F0;margin-bottom:4px;">pagamento sicuro</div>
    <div style="font-size:0.8125rem;color:#64748B;"><strong>SSL · Stripe · PayPal</strong></div>
  </div>

  <div>
    <div style="font-size:2rem;margin-bottom:8px;">🏆</div>
    <div style="font-family:'Cinzel',serif;font-size:0.875rem;color:#E2E8F0;margin-bottom:4px;">certificato</div>
    <div style="font-size:0.8125rem;color:#64748B;"><strong>[CERTIFICAZIONE]</strong></div>
  </div>

</div>
```

### SCARCITY / URGENCY
```html
<div style="background:rgba(192,80,90,0.08);border:1px solid rgba(192,80,90,0.25);border-radius:4px;padding:20px 24px;text-align:center;margin:32px 0;">
  <p style="color:#C0505A;font-size:0.9375rem;margin:0;">
    ⚠ <strong>solo [N] unità rimaste</strong> al prezzo attuale · il prezzo aumenta tra:
    <span id="scarcity-timer" style="font-family:'Cinzel',serif;font-size:1.25rem;color:#E3C878;margin-left:8px;"></span>
  </p>
</div>
```

---

## COPY RULES PRODOTTI FISICI

### Headline (emozione + beneficio + prova)
```
Formula: [EMOZIONE] + [BENEFICIO SPECIFICO] + [TIMEFRAME/CONDIZIONE]

Esempi:
"la pelle luminosa che meritavi — in 28 giorni o rimborsiamo tutto"
"aumenta forza e resistenza del 40% — formula brevettata, risultati in 3 settimane"
"il dettaglio di stile che tutti noteranno — spedizione in 24 ore"
```

### Descrizione beneficio (non ingrediente)
```
❌ "contiene acido ialuronico al 2%"
✓  "idrata in profondità per 72 ore consecutive — la tua pelle resta morbida dal mattino alla sera"

❌ "formula con whey protein isolate"
✓  "recupero muscolare accelerato — torna ad allenarti il giorno dopo senza dolori"
```

### Ingredienti (racconta la storia)
```
❌ "olio d'argan"
✓  "olio d'argan biologico del Marocco — estratto a freddo per preservare il 100% dei nutrienti attivi"
```

### CTA Labels
```
✓ "aggiungi al carrello"
✓ "ordina ora — consegna in 24-48h"
✓ "prova [NOME] — garanzia 30 giorni"
✓ "voglio il mio [NOME]"
```

---

## PRICE DISPLAY PRODOTTO FISICO

```html
<div style="margin:24px 0;">
  <!-- Prezzo barrato -->
  <span style="font-size:1rem;color:#374151;text-decoration:line-through;margin-right:8px;">[PREZZO PIENO]</span>
  <!-- Badge sconto -->
  <span style="background:rgba(192,80,90,0.15);border:1px solid rgba(192,80,90,0.4);color:#C0505A;font-size:0.75rem;font-weight:700;padding:3px 8px;border-radius:2px;margin-right:12px;">-[X]%</span>
  <!-- Prezzo attuale -->
  <span style="font-family:'Cinzel',serif;font-size:2.5rem;font-weight:700;color:#E3C878;">[PREZZO SCONTATO]</span>
  <!-- Micro info -->
  <p style="font-size:0.8125rem;color:#64748B;margin-top:8px;">iva inclusa · spedizione gratuita · [N] in stock</p>
</div>

<!-- Varianti prodotto (colori, taglie) -->
<div style="margin:20px 0;">
  <div style="font-size:0.8125rem;color:#94A3B8;margin-bottom:10px;">scegli la variante:</div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;">
    <button style="padding:8px 16px;border:1px solid #E3C878;background:rgba(227,200,120,0.1);color:#E3C878;border-radius:2px;font-size:0.8125rem;cursor:pointer;">[VARIANTE 1]</button>
    <button style="padding:8px 16px;border:1px solid rgba(148,163,184,0.3);background:transparent;color:#94A3B8;border-radius:2px;font-size:0.8125rem;cursor:pointer;">[VARIANTE 2]</button>
  </div>
</div>
```

---

## MOBILE SPECIFICO (prodotti fisici)

```css
@media (max-width: 768px) {
  /* Hero: foto sopra, info sotto */
  .product-hero { flex-direction: column; }
  .product-image { width: 100%; height: 300px; }

  /* Ingredienti: 2 colonne */
  .ingredients-grid { grid-template-columns: repeat(2, 1fr); }

  /* Gallery: 1 immagine alla volta */
  .gallery-item { min-width: 100%; }

  /* UGC: 2 colonne su mobile */
  .ugc-grid { grid-template-columns: repeat(2, 1fr); }

  /* Trust: 2 colonne */
  .trust-grid { grid-template-columns: repeat(2, 1fr); }
}
```
