# K03-divider-library
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Website Creator > knowledge]]

## Content

# K03 — DIVIDER LIBRARY (5 Divisori dall'Agency)

> Codice esatto dei 5 divisori estratti dal sito Agency e convertiti in vanilla HTML. Copia-incolla direttamente senza modifiche strutturali.

---

## GRADIENT METALLIC STANDARD (condiviso da tutti i divisori)

```css
--gradient-metallic: linear-gradient(
  90deg,
  #94A3B8 0%,
  #E2E8F0 20%,
  #E3C878 45%,
  #FFFFFF 50%,
  #E3C878 55%,
  #E2E8F0 80%,
  #94A3B8 100%
);
```

Questo gradient simula una superficie metallica illuminata al centro (oro brillante) che sfuma verso argento freddo ai lati.

---

## DIVISORE 1 — LuxArc

**Quando usarlo:** Passaggio da sezione SCURA a sezione CHIARA. Forma: arco a V con la punta verso il basso che si solleva al centro. L'arco sembra una porta ad arco di palazzo nobile.

**Aspetto:** triangolo/arco argentato-oro con highlight bianco, altezza 100-150px.

```html
<!-- LuxArc: dark → light -->
<div style="position:relative; height:100px; overflow:hidden; background:[COLORE-SEZIONE-SOPRA];">

  <!-- Sfondo della sezione SOTTO (chiaro) che riempie l'arco -->
  <div style="
    position:absolute;
    inset:0;
    clip-path: polygon(0% 100%, 0% 35%, 50% 0%, 100% 35%, 100% 100%);
    background:[COLORE-SEZIONE-SOTTO];
  "></div>

  <!-- Stroke SVG metallico sull'arco -->
  <svg viewBox="0 0 1200 100" preserveAspectRatio="none"
    style="position:absolute;inset:0;width:100%;height:100%;">
    <defs>
      <linearGradient id="luxArcGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="#94A3B8"/>
        <stop offset="20%"  stop-color="#E2E8F0"/>
        <stop offset="45%"  stop-color="#E3C878"/>
        <stop offset="50%"  stop-color="#FFFFFF"/>
        <stop offset="55%"  stop-color="#E3C878"/>
        <stop offset="80%"  stop-color="#E2E8F0"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <!-- Linea arco metallica -->
    <path d="M 0,100 L 0,35 L 600,0 L 1200,35 L 1200,100"
      fill="none"
      stroke="url(#luxArcGrad)"
      stroke-width="2"/>
    <!-- Highlight bianco sopra il bordo -->
    <path d="M 0,100 L 0,35 L 600,0 L 1200,35 L 1200,100"
      fill="none"
      stroke="rgba(255,255,255,0.9)"
      stroke-width="1"
      style="mix-blend-mode:overlay;"/>
  </svg>

</div>
```

**Desktop:** height 150px | **Mobile:** height 100px (media query)

---

## DIVISORE 2 — LuxV

**Quando usarlo:** Passaggio da sezione CHIARA a sezione SCURA. Forma: V con la punta verso il basso al centro della pagina. Drammatico, invita a scendere.

```html
<!-- LuxV: light → dark -->
<div style="position:relative; height:80px; overflow:hidden; background:[COLORE-SEZIONE-SOPRA];">

  <!-- Sfondo scuro che riempie il V inferiore -->
  <div style="
    position:absolute;
    inset:0;
    clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 50% 40%, 0% 100%);
    background:[COLORE-SEZIONE-SOTTO];
  "></div>

  <!-- Stroke SVG metallico sulla V -->
  <svg viewBox="0 0 1200 80" preserveAspectRatio="none"
    style="position:absolute;inset:0;width:100%;height:100%;">
    <defs>
      <linearGradient id="luxVGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="#94A3B8"/>
        <stop offset="20%"  stop-color="#E2E8F0"/>
        <stop offset="45%"  stop-color="#E3C878"/>
        <stop offset="50%"  stop-color="#FFFFFF"/>
        <stop offset="55%"  stop-color="#E3C878"/>
        <stop offset="80%"  stop-color="#E2E8F0"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M -100,0 L 600,80 L 1300,0"
      fill="none"
      stroke="url(#luxVGrad)"
      stroke-width="2"/>
    <path d="M -100,0 L 600,80 L 1300,0"
      fill="none"
      stroke="rgba(255,255,255,0.9)"
      stroke-width="1"
      style="mix-blend-mode:overlay;"/>
  </svg>

</div>
```

---

## DIVISORE 3 — LuxCurve (IL PIÙ BELLO)

**Quando usarlo:** La sezione che SEGUE questo divisore inizia con il bordo superiore curvato. È il divisore più elegante — la sezione sembra emergere dalla pagina come un'onda.

**Tecnica:** La sezione successiva usa `clip-path` SVG per tagliare il bordo superiore in curva quadratica bezier.

```html
<!-- LuxCurve: applica alla sezione che deve avere il bordo curvo -->

<!-- PASSO 1: Inserisci il clipPath SVG nell'<head> o prima della sezione -->
<svg style="position:absolute;width:0;height:0;overflow:hidden;">
  <defs>
    <clipPath id="lux-curve-top" clipPathUnits="objectBoundingBox">
      <path d="M 0,0.08 Q 0.5,0 1,0.08 L 1,1 L 0,1 Z"/>
    </clipPath>
  </defs>
</svg>

<!-- PASSO 2: La sezione con il bordo curvo -->
<section style="
  position: relative;
  background: [COLORE-SEZIONE];
  clip-path: url(#lux-curve-top);
  padding-top: 80px;
  overflow: hidden;
">
  <!-- Grain layers dentro la curva -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.40;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.25;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <!-- Linea decorativa sulla curva -->
  <div style="
    position:absolute; top:0; left:0; right:0; height:60px;
    pointer-events:none; z-index:15;
  ">
    <svg viewBox="0 0 1200 60" preserveAspectRatio="none" style="width:100%;height:100%;">
      <defs>
        <linearGradient id="curveLineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%"   stop-color="#94A3B8"/>
          <stop offset="45%"  stop-color="#E3C878"/>
          <stop offset="50%"  stop-color="#FFFFFF"/>
          <stop offset="55%"  stop-color="#E3C878"/>
          <stop offset="100%" stop-color="#94A3B8"/>
        </linearGradient>
      </defs>
      <path d="M -50,50 Q 600,0 1250,50"
        fill="none"
        stroke="url(#curveLineGrad)"
        stroke-width="1.5"/>
    </svg>
  </div>

  <!-- Contenuto sezione -->
  <div style="position:relative; z-index:20; max-width:1200px; margin:0 auto; padding:0 24px;">
    <!-- contenuto -->
  </div>
</section>
```

---

## DIVISORE 4 — LuxTriangle

**Quando usarlo:** Elemento decorativo standalone tra due sezioni scure. Crea un rombo/triangolo scuro con bordo metallico che fluttua tra le sezioni.

```html
<!-- LuxTriangle: elemento decorativo tra sezioni dark -->
<div style="position:relative; height:120px; overflow:visible; z-index:5;">

  <!-- Triangolo con sfondo scuro -->
  <div style="
    position:absolute;
    left:50%; top:0;
    transform:translateX(-50%);
    width:200px; height:100px;
    background: linear-gradient(180deg, #0f2e4a 0%, #020202 100%);
    clip-path: polygon(0% 0%, 50% 100%, 100% 0%);
  ">
    <!-- Grain nel triangolo -->
    <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.40;mix-blend-mode:overlay;pointer-events:none;clip-path:polygon(0% 0%, 50% 100%, 100% 0%);"></div>
  </div>

  <!-- Linea SVG metallica sul perimetro del triangolo -->
  <svg viewBox="0 0 200 100"
    style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:200px;height:100px;overflow:visible;">
    <defs>
      <linearGradient id="triGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="#94A3B8"/>
        <stop offset="50%"  stop-color="#E3C878"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M 0,0 L 100,100 L 200,0"
      fill="none"
      stroke="url(#triGrad)"
      stroke-width="1.5"/>
  </svg>

</div>
```

---

## DIVISORE 5 — InclinedStrip

**Quando usarlo:** Separatore veloce e impattante tra qualsiasi coppia di sezioni. Striscia metallica inclinata -2.5°. Occhio immediato, senso di movimento.

```html
<!-- InclinedStrip -->
<div style="position:relative; height:48px; overflow:hidden; margin:-12px 0;">
  <div style="
    position:absolute;
    left:-5%; right:-5%;
    top:50%; transform:translateY(-50%) rotate(-2.5deg);
    height:24px;
    background: linear-gradient(90deg, #8E9BAF 0%, #CBD5E1 15%, #D4AF37 35%, #FFD700 50%, #D4AF37 65%, #CBD5E1 85%, #8E9BAF 100%);
    box-shadow:
      0 -1px 0 rgba(255,255,255,0.9),
      0 1px 8px rgba(0,0,0,0.6);
    overflow:hidden;
  ">
    <!-- Grain sulla striscia -->
    <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.30;mix-blend-mode:overlay;pointer-events:none;"></div>
    <!-- Highlight superiore -->
    <div style="position:absolute;top:0;left:0;right:0;height:1px;background:rgba(255,255,255,0.9);"></div>
    <!-- Shadow inferiore -->
    <div style="position:absolute;bottom:0;left:0;right:0;height:1px;background:rgba(0,0,0,0.4);"></div>
  </div>
</div>
```

---

## GUIDA RAPIDA — QUALE DIVISORE USARE

| Transizione | Divisore consigliato |
|-------------|----------------------|
| Hero (dark) → Benefits (dark) | InclinedStrip |
| Benefits (dark) → Mockup (light) | LuxArc |
| Mockup (light) → Inside (dark) | LuxV |
| Inside (dark) → Author (dark) | InclinedStrip |
| Author (dark) → Testimonials (dark) | LuxCurve (per la sezione Testimonials) |
| Testimonials (dark) → FAQ (light) | LuxArc |
| FAQ (light) → Footer (dark) | LuxV |
| Qualsiasi → Sezione speciale | LuxTriangle (standalone) |

**Regola:** InclinedStrip per transizioni same-tone, LuxArc/LuxV per transizioni dark↔light, LuxCurve per la sezione più importante.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
