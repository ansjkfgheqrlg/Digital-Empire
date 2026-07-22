# Skill: divider-forge

Sei il costruttore di divisori SVG. Per ogni coppia di sezioni consecutive, generi il codice HTML+SVG del divisore corretto dalla libreria K03.

---

## QUANDO VIENE ATTIVATA

Chiamata da `web-master` nel loop di build, subito dopo ogni sezione (tranne l'ultima). Input: tipo divisore + colori da ARCHITECTURE JSON.

---

## INPUT RICHIESTO

```
- divider_type: "inclined_strip" | "lux_arc" | "lux_v" | "lux_curve" | "lux_triangle"
- color_above: hex sfondo sezione precedente
- color_below: hex sfondo sezione successiva
- palette: oggetto palette (per gradient metallic custom se necessario)
- position: numero progressivo (per ID univoci nei gradient SVG)
```

---

## SELEZIONE AUTOMATICA

Se `web-master` non specifica il tipo, usa questa regola:

```
color_above DARK + color_below DARK   → inclined_strip
color_above DARK + color_below LIGHT  → lux_arc
color_above LIGHT + color_below DARK  → lux_v (o lux_curve se è la transizione principale)
color_above LIGHT + color_below LIGHT → inclined_strip (raro)
Per sezione speciale/importante         → lux_curve o lux_triangle
```

---

## CODICE DIVISORI

### INCLINED STRIP

```html
<!-- Divisore: InclinedStrip [pos] -->
<div style="position:relative;height:48px;overflow:hidden;margin:-12px 0;z-index:5;">
  <div style="position:absolute;left:-5%;right:-5%;top:50%;transform:translateY(-50%) rotate(-2.5deg);height:24px;background:linear-gradient(90deg,#8E9BAF 0%,#CBD5E1 15%,#D4AF37 35%,#FFD700 50%,#D4AF37 65%,#CBD5E1 85%,#8E9BAF 100%);box-shadow:0 -1px 0 rgba(255,255,255,0.9),0 1px 8px rgba(0,0,0,0.6);overflow:hidden;position:relative;">
    <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.30;mix-blend-mode:overlay;pointer-events:none;"></div>
    <div style="position:absolute;top:0;left:0;right:0;height:1px;background:rgba(255,255,255,0.9);"></div>
    <div style="position:absolute;bottom:0;left:0;right:0;height:1px;background:rgba(0,0,0,0.4);"></div>
  </div>
</div>
```

---

### LUX ARC (dark → light)

```html
<!-- Divisore: LuxArc [pos] (dark→light) -->
<div style="position:relative;height:120px;overflow:hidden;background:[COLOR_ABOVE];">
  <!-- Sfondo sezione sotto che riempie l'arco -->
  <div style="position:absolute;inset:0;clip-path:polygon(0% 100%,0% 30%,50% 0%,100% 30%,100% 100%);background:[COLOR_BELOW];"></div>
  <!-- Stroke SVG metallico -->
  <svg viewBox="0 0 1200 120" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%;">
    <defs>
      <linearGradient id="luxArcGrad[POS]" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="#94A3B8"/>
        <stop offset="20%"  stop-color="#E2E8F0"/>
        <stop offset="45%"  stop-color="#E3C878"/>
        <stop offset="50%"  stop-color="#FFFFFF"/>
        <stop offset="55%"  stop-color="#E3C878"/>
        <stop offset="80%"  stop-color="#E2E8F0"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M 0,120 L 0,36 L 600,0 L 1200,36 L 1200,120"
      fill="none"
      stroke="url(#luxArcGrad[POS])"
      stroke-width="2.5"/>
    <path d="M 0,120 L 0,36 L 600,0 L 1200,36 L 1200,120"
      fill="none"
      stroke="rgba(255,255,255,0.85)"
      stroke-width="1"
      style="mix-blend-mode:overlay;"/>
  </svg>
</div>
```

**Mobile:** aggiungi `@media (max-width:768px) { .divider-arc { height: 80px; } }`

---

### LUX V (light → dark)

```html
<!-- Divisore: LuxV [pos] (light→dark) -->
<div style="position:relative;height:90px;overflow:hidden;background:[COLOR_ABOVE];">
  <!-- Sfondo scuro che riempie la V inferiore -->
  <div style="position:absolute;inset:0;clip-path:polygon(0% 0%,100% 0%,100% 100%,50% 35%,0% 100%);background:[COLOR_BELOW];"></div>
  <!-- Stroke SVG metallico -->
  <svg viewBox="0 0 1200 90" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%;">
    <defs>
      <linearGradient id="luxVGrad[POS]" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="#94A3B8"/>
        <stop offset="20%"  stop-color="#E2E8F0"/>
        <stop offset="45%"  stop-color="#E3C878"/>
        <stop offset="50%"  stop-color="#FFFFFF"/>
        <stop offset="55%"  stop-color="#E3C878"/>
        <stop offset="80%"  stop-color="#E2E8F0"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M -150,0 L 600,90 L 1350,0"
      fill="none"
      stroke="url(#luxVGrad[POS])"
      stroke-width="2.5"/>
    <path d="M -150,0 L 600,90 L 1350,0"
      fill="none"
      stroke="rgba(255,255,255,0.85)"
      stroke-width="1"
      style="mix-blend-mode:overlay;"/>
  </svg>
</div>
```

---

### LUX CURVE (bordo curvo sulla sezione successiva)

Questo divisore è diverso dagli altri: **non è un elemento separato** — modifica la sezione successiva aggiungendo un bordo superiore curvo e una linea decorativa.

```html
<!-- LuxCurve: [POS] — aggiunge bordo curvo alla sezione successiva -->
<!-- PASSO 1: SVG clipPath (inserisci prima della sezione o in head) -->
<svg style="position:absolute;width:0;height:0;overflow:hidden;">
  <defs>
    <clipPath id="luxCurve[POS]" clipPathUnits="objectBoundingBox">
      <path d="M 0,0.07 Q 0.5,0 1,0.07 L 1,1.1 L 0,1.1 Z"/>
    </clipPath>
  </defs>
</svg>

<!-- PASSO 2: La sezione successiva usa questo clipPath -->
<!-- Aggiungi al <section> dello step successivo:
     clip-path: url(#luxCurve[POS]);
     padding-top: 80px;
     (il grain layers vengono inclusi normalmente nella sezione)
-->

<!-- PASSO 3: Linea decorativa sulla curva (dentro la sezione successiva, z-index:15) -->
<div style="position:absolute;top:0;left:0;right:0;height:70px;pointer-events:none;z-index:15;">
  <svg viewBox="0 0 1200 70" preserveAspectRatio="none" style="width:100%;height:100%;">
    <defs>
      <linearGradient id="curveLine[POS]" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="transparent"/>
        <stop offset="10%"  stop-color="#94A3B8"/>
        <stop offset="40%"  stop-color="#E3C878"/>
        <stop offset="50%"  stop-color="#FFFFFF"/>
        <stop offset="60%"  stop-color="#E3C878"/>
        <stop offset="90%"  stop-color="#94A3B8"/>
        <stop offset="100%" stop-color="transparent"/>
      </linearGradient>
    </defs>
    <path d="M -60,60 Q 600,0 1260,60"
      fill="none"
      stroke="url(#curveLine[POS])"
      stroke-width="1.5"/>
  </svg>
</div>
```

**ISTRUZIONI D'USO:**
1. `section-forge` deve sapere che questa sezione usa LuxCurve — includi il clipPath SVG dentro la sezione (prima dei grain layers) e aggiungi `clip-path:url(#luxCurve[POS])` allo stile della sezione stessa
2. Aumenta `padding-top` a 80-100px per compensare il clip
3. La linea decorativa va dentro la sezione, z-index 15 (sopra grain, sotto contenuto)

---

### LUX TRIANGLE

```html
<!-- Divisore: LuxTriangle [pos] -->
<div style="position:relative;height:140px;background:[COLOR_ABOVE];overflow:visible;z-index:5;">
  <!-- Triangolo con sfondo scuro -->
  <div style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:220px;height:110px;background:linear-gradient(180deg,[COLOR_ABOVE] 0%,[COLOR_BELOW] 100%);clip-path:polygon(0% 0%,50% 100%,100% 0%);overflow:hidden;">
    <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.40;mix-blend-mode:overlay;pointer-events:none;"></div>
  </div>
  <!-- Linea perimetro metallica -->
  <svg viewBox="0 0 220 110" style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:220px;height:110px;overflow:visible;">
    <defs>
      <linearGradient id="triGrad[POS]" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="#94A3B8"/>
        <stop offset="50%"  stop-color="#E3C878"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M 0,0 L 110,110 L 220,0"
      fill="none"
      stroke="url(#triGrad[POS])"
      stroke-width="1.5"/>
    <path d="M 0,0 L 110,110 L 220,0"
      fill="none"
      stroke="rgba(255,255,255,0.6)"
      stroke-width="0.8"
      style="mix-blend-mode:overlay;"/>
  </svg>
  <!-- Sfondo continuo della sezione sotto -->
  <div style="position:absolute;bottom:0;left:0;right:0;height:30px;background:[COLOR_BELOW];"></div>
</div>
```

---

## REGOLE FINALI

1. **ID gradient univoci**: ogni divisore usa `[POS]` per differenziare gli ID SVG — es. `luxArcGrad3`, `luxVGrad5`
2. **Niente spazi bianchi tra sezione e divisore**: usa `margin:-1px 0` se vedi gap
3. **LuxCurve**: comunicare a `section-forge` che la sezione successiva ha il clip — non è un tag HTML separato ma una proprietà della sezione
4. **Mobile**: InclinedStrip e LuxArc/V si adattano naturalmente. LuxTriangle nascondilo su mobile (`display:none` sotto 480px) se lo spazio è troppo ridotto
5. **Grain nel divisore**: solo InclinedStrip e LuxTriangle hanno grain interno — LuxArc e LuxV no (troppo sottili)
