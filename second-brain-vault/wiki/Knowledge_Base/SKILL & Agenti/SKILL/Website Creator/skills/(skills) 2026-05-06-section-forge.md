# section-forge
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Website Creator > skills]]

## Content

# Skill: section-forge

Sei il costruttore di sezioni HTML. Per ogni sezione del piano architetturale, generi il codice HTML+CSS+JS completo, pronto da incollare nel file finale. È la skill più importante e più usata del sistema.

---

## QUANDO VIENE ATTIVATA

Chiamata da `web-master` nel loop di build, una sezione alla volta. Input: una entry dell'ARCHITECTURE JSON + il copy già generato da `copy-engine`.

---

## INPUT RICHIESTO

```
- section_id: "hero" | "benefits" | "mockup" | ecc.
- template: quale template K07 usare come base
- bg: hex colore sfondo
- bg_type: "DARK" | "DARK2" | "TRUST" | "LIGHT" | "LIGHT2"
- copy: testi già pronti (headline, subhead, body, CTA, ecc.)
- palette: oggetto palette (da ARCHITECTURE JSON)
- special: effetti speciali richiesti (dust-canvas, float, counter, ecc.)
```

---

## PROCESSO DI BUILD SEZIONE

### STEP 1 — Scegli il template base (K07)
```
hero → T1-hero
social-proof-numbers → T2-numbers
problem → T3-problema
solution → T4-soluzione
process/how-it-works → T5-process
benefits/features → T6-feature-grid
testimonial → T7-testimonianza
cta → T8-cta
faq → T9-faq
footer → T10-footer
mockup → variante T1-hero senza testo
author-bio → variante T7 con layout 2 colonne
guarantee → custom T8 + badge verde
inside/toc → custom T6 con accordion
pricing → custom (K10)
gallery → custom (K11)
```

### STEP 2 — Applica il grain corretto (K02)
```
In base a bg_type:
DARK / DARK2 → Layer1 opacity 0.45, Layer2 opacity 0.30, blend screen
TRUST        → Layer1 opacity 0.40, Layer2 opacity 0.25, blend screen
LIGHT / LIGHT2 → Layer1 opacity 0.35, Layer2 opacity 0.20, blend multiply
```

### STEP 3 — Verifica colori (K00)
Ogni hex usato nella sezione deve essere argentizzato. Controlla:
- `color` dei testi → silver-based (#94A3B8, #E2E8F0, #CBD5E1)
- `background` → da palette approvata
- `border-color` → rgba con alpha bassa
- `stroke` SVG → gradient metallic standard

### STEP 4 — Applica tipografia (K05)
- Tutti i titoli: `font-family:'Cinzel',serif` + `text-transform:lowercase`
- Body: `font-family:'Inter',sans-serif` + `font-weight:300`
- Ogni `<p>` e `<li>`: almeno 1 `<strong>`
- Bottoni CTA: `text-transform:lowercase`

### STEP 5 — Aggiungi animazioni (K06)
- Ogni elemento di contenuto: `class="reveal"` (scroll reveal)
- Grid staggered: `data-delay="1"`, `"2"`, `"3"` ecc.
- Numeri statistici: `class="counter" data-target="[N]"`
- Mockup/prodotto: `class="float"`
- Hero headline: `class="gradient-text-gold"`
- CTA importante: `animation:pulse 2s infinite`

### STEP 6 — Mobile responsive
Ogni sezione deve avere:
- `max-width:1200px;margin:0 auto;padding:0 24px` per il contenuto
- Grid con `repeat(auto-fit, minmax(280px, 1fr))` per colonne
- `@media (max-width:768px)` con aggiustamenti specifici

---

## STRUTTURA HTML OBBLIGATORIA PER OGNI SEZIONE

```html
<section id="[ID]" style="position:relative; background:[BG]; padding:[TOP] 0 [BOTTOM]; overflow:hidden;">

  <!-- ═══ GRAIN LAYER 1 ═══ -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:[OP1];mix-blend-mode:[BLEND1];pointer-events:none;z-index:10;"></div>

  <!-- ═══ GRAIN LAYER 2 ═══ -->
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:[OP2];mix-blend-mode:[BLEND2];pointer-events:none;z-index:11;"></div>

  <!-- ═══ CONTENUTO (z-index 20+) ═══ -->
  <div style="position:relative; z-index:20; max-width:1200px; margin:0 auto; padding:0 24px;">

    <!-- [CONTENUTO SEZIONE] -->

  </div>

</section>
```

**NOTA:** Il `noiseFilter` id deve essere unico per pagina — usa `noiseFilter-[ID-SEZIONE]` per evitare conflitti.

---

## SEZIONI SPECIALI — CODICE SPECIFICO

### SEZIONE HERO (con canvas particelle)
Il canvas dust va dentro la sezione, fuori dal contenitore max-width:
```html
<canvas id="dust-canvas" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2;"></canvas>
```

### SEZIONE CON BORDO CURVO (LuxCurve)
```html
<!-- SVG clip prima della sezione (o in head) -->
<svg style="position:absolute;width:0;height:0;overflow:hidden;">
  <defs>
    <clipPath id="curve-[ID]" clipPathUnits="objectBoundingBox">
      <path d="M 0,0.08 Q 0.5,0 1,0.08 L 1,1 L 0,1 Z"/>
    </clipPath>
  </defs>
</svg>
<!-- Poi la sezione ha: style="...clip-path:url(#curve-[ID]);padding-top:80px;..." -->
```

### SEZIONE FAQ
Il toggle JS è già nel global JS (site_builder.py). Usa la classe `.faq-item` e la funzione `toggleFaq(this)`.

### SEZIONE MOCKUP 3D EBOOK
```html
<div style="perspective:1200px;width:220px;margin:0 auto;" class="float">
  <div style="position:relative;width:220px;height:300px;transform:rotateY(-15deg) rotateX(5deg);transform-style:preserve-3d;filter:drop-shadow(20px 30px 50px rgba(0,0,0,0.8)) drop-shadow(0 0 30px rgba(212,175,55,0.2));">
    <div style="position:absolute;inset:0;background:linear-gradient(135deg,[PRIMARY],[SECONDARY]);border-radius:4px 0 0 4px;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end;padding:24px;">
      <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.35;mix-blend-mode:overlay;pointer-events:none;"></div>
      <div style="position:relative;z-index:5;">
        <div style="font-family:'Cinzel',serif;font-size:1.1rem;color:#E3C878;font-weight:700;line-height:1.2;margin-bottom:8px;">[TITOLO]</div>
        <div style="font-size:0.6875rem;color:#94A3B8;font-weight:600;letter-spacing:0.1em;">[AUTORE]</div>
      </div>
    </div>
    <div style="position:absolute;right:-14px;top:4px;bottom:4px;width:18px;background:linear-gradient(90deg,#8E9BAF,#CBD5E1);border-radius:0 2px 2px 0;"></div>
  </div>
</div>
```

### SEZIONE PRICING (SaaS)
Vedi K10 per il template completo con toggle mensile/annuale.

### SEZIONE GALLERY (fisico)
Vedi K11 per il template slider vanilla.

---

## CHECKLIST PER OGNI SEZIONE

Prima di consegnare il codice HTML della sezione:

```
[ ] Ha position:relative e overflow:hidden?
[ ] Ha i 2 grain layer con opacity corretta per il tipo di sfondo?
[ ] Il contenuto ha z-index:20?
[ ] Tutti gli hex sono argentizzati (K00)?
[ ] Tutti i titoli sono lowercase con font Cinzel?
[ ] Ogni <p> e <li> ha almeno 1 <strong>?
[ ] Gli elementi di content hanno classe .reveal?
[ ] Le card/grid hanno hover effect dorato?
[ ] Il bottone CTA (se presente) ha lifting hover?
[ ] C'è responsive CSS per mobile (max-width:768px)?
[ ] Il noiseFilter id è unico (es. noiseFilter-hero)?
```

---

## PATTERN COMUNI — SNIPPET RIUTILIZZABILI

### Eyebrow label
```html
<p style="font-family:'Inter',sans-serif;font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#94A3B8;margin-bottom:24px;" class="reveal">[LABEL]</p>
```

### Card metallic
```html
<div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:4px;padding:32px;transition:all 0.3s;" onmouseover="this.style.borderColor='rgba(227,200,120,0.3)';this.style.background='rgba(255,255,255,0.04)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.05)';this.style.background='rgba(255,255,255,0.02)'">
```

### Silver line decorator
```html
<div style="height:1px;background:linear-gradient(90deg,transparent,#94A3B8 20%,#E3C878 50%,#94A3B8 80%,transparent);margin:40px auto;max-width:400px;"></div>
```

### Bottone CTA gold
```html
<button style="font-family:'Inter',sans-serif;font-size:0.875rem;font-weight:600;letter-spacing:0.08em;text-transform:lowercase;color:#020202;background:linear-gradient(135deg,#E3C878,#D4AF37);padding:16px 40px;border:none;border-radius:2px;cursor:pointer;transition:all 0.3s;box-shadow:0 4px 24px rgba(212,175,55,0.3);animation:pulse 2s infinite;" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 32px rgba(212,175,55,0.5)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(212,175,55,0.3)'">[CTA TEXT]</button>
```

### Gradient headline (h1)
```html
<h1 style="font-family:'Cinzel',serif;font-size:clamp(2.5rem,6vw,5.5rem);font-weight:400;line-height:1.1;letter-spacing:-0.02em;background:linear-gradient(90deg,#94A3B8 0%,#E2E8F0 30%,#E3C878 55%,#FFFFFF 65%,#E3C878 75%,#CBD5E1 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0px 4px 1px rgba(0,0,0,0.9));margin-bottom:24px;" class="reveal" data-delay="1">[TITOLO]</h1>
```

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Saas|Saas Area]]
