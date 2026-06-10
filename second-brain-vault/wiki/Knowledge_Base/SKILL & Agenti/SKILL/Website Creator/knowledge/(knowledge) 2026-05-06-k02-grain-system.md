# K02-grain-system
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Website Creator > knowledge]]

## Content

# K02 — GRAIN SYSTEM (Codice Esatto dall'Agency)

> Questi sono i codici esatti estratti e convertiti dal sito Agency. Copia-incolla direttamente — non inventare varianti.

---

## LAYER 1 — FILM GRAIN (URL esterno, filtri aggressivi)

```html
<div style="
  position: absolute;
  inset: 0;
  background-image: url('https://grainy-gradients.vercel.app/noise.svg');
  filter: contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);
  opacity: 0.45;
  mix-blend-mode: overlay;
  pointer-events: none;
  z-index: 10;
"></div>
```

**Spiegazione filtri:**
- `contrast(350%)` — amplifica la grana al massimo
- `brightness(60%)` — scurisce per non lavare lo sfondo
- `sepia(100%) hue-rotate(260deg) saturate(200%)` — sposta la grana verso toni dorati/viola (effetto pellicola vintage)
- `mix-blend-mode: overlay` — fonde con lo sfondo invece di coprirlo

---

## LAYER 2 — DIGITAL NOISE (SVG feTurbulence inline)

```html
<div style="
  position: absolute;
  inset: 0;
  background-image: url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);
  background-size: 100px 100px;
  filter: contrast(180%) brightness(40%);
  opacity: 0.3;
  mix-blend-mode: screen;
  pointer-events: none;
  z-index: 11;
"></div>
```

**Versione con escaped corretto per attributo HTML inline:**
```html
<div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>
```

**Parametri feTurbulence:**
- `baseFrequency="1.5"` — granularità fine (più alto = più fine)
- `numOctaves="4"` — dettaglio (più octave = più dettagliato)
- `stitchTiles="stitch"` — tiling senza discontinuità

---

## LAYER 3 — GRID SOTTILE (opzionale, solo sfondi molto scuri)

```html
<div style="
  position: absolute;
  inset: 0;
  background:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 60px 60px;
  opacity: 0.10;
  pointer-events: none;
  z-index: 9;
"></div>
```

---

## TABELLA OPACITY PER TIPO DI SFONDO

| Sfondo | Layer 1 opacity | Layer 2 opacity | Layer 2 blend |
|--------|-----------------|-----------------|---------------|
| Nero/near-black (`#020202`, `#0a0a0a`) | 0.45 | 0.30 | screen |
| Scuro colorato (`#0f2e4a`, `#031c16`) | 0.40 | 0.25 | screen |
| Chiaro/beige (`#DCD8CF`, `#F8F6F2`) | 0.35 | 0.20 | multiply |
| Bianco puro (`#FFFFFF`) | 0.25 | 0.15 | multiply |

**Nota:** Su sfondi chiari, Layer 1 cambia `mix-blend-mode` da `overlay` a `multiply`.

---

## TEMPLATE SEZIONE COMPLETO CON GRAIN

```html
<section style="position:relative; background:#020202; padding:80px 0; overflow:hidden;">

  <!-- GRAIN LAYER 1: Film Grain -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.45;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>

  <!-- GRAIN LAYER 2: Digital Noise -->
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <!-- CONTENUTO (z-index sopra il grain) -->
  <div style="position:relative; z-index:20; max-width:1200px; margin:0 auto; padding:0 24px;">
    <!-- qui va il contenuto della sezione -->
  </div>

</section>
```

**IMPORTANTE:** Il contenuto interno deve avere `position:relative; z-index:20` (o superiore) per stare sopra il grain.

---

## GRAIN MOVEMENT ANIMATION (opzionale, aggiunge vita)

```css
@keyframes grainMove {
  0%, 100% { background-position: 0% 0%; }
  25%       { background-position: 10% -5%; }
  50%       { background-position: -5% 10%; }
  75%       { background-position: 5% -10%; }
}

.grain-animated {
  animation: grainMove 8s steps(1) infinite;
}
```

Applica la classe `.grain-animated` al Layer 2 per un effetto grain che "vive" lentamente.

---

## VARIANTI CROMATICHE DEL GRAIN (Layer 1)

### Grain dorato (per sezioni luxury oro)
```
filter: contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);
```
*(default — questo è il grain oro/viola dell'Agency)*

### Grain neutro (per sezioni con palette non-oro)
```
filter: contrast(350%) brightness(60%) sepia(30%) saturate(100%);
```

### Grain verde (per sezioni con palette verde-silver)
```
filter: contrast(350%) brightness(55%) sepia(100%) hue-rotate(120deg) saturate(150%);
```

### Grain blu (per sezioni SaaS dark)
```
filter: contrast(350%) brightness(55%) sepia(100%) hue-rotate(200deg) saturate(180%);
```

---

## NOTE TECNICHE

1. **z-index stack:** grain layer 1 = z-index 10, grain layer 2 = z-index 11, contenuto = z-index 20+
2. **overflow:hidden** sulla sezione è obbligatorio per evitare che il grain esca dai bordi
3. **position:relative** sulla sezione è obbligatorio per il positioning assoluto dei layer
4. Il Layer 1 richiede connessione internet (URL esterno) — fallback: opacità 0 se offline
5. Il Layer 2 è completamente inline — funziona offline
6. Non aggiungere `will-change:transform` ai grain layer — peggiora le performance senza benefici visibili

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Saas|Saas Area]]
