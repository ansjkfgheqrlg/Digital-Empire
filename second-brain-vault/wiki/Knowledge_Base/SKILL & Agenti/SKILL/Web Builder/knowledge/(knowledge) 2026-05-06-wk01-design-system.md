# WK01-design-system
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Web Builder > knowledge]]

## Content

# WK01 — Design System: Digital Empire Web Standard

## REGOLA 1: SILVER MIXING (OBBLIGATORIA, SEMPRE)

Ogni colore nel sito DEVE avere una componente silver. Nessun colore puro isolato.

### Palette Silver di Base
```css
--silver-100: #F8FAFC;
--silver-200: #E2E8F0;
--silver-300: #CBD5E1;
--silver-400: #94A3B8;
--silver-500: #64748B;
```

### Come Mescolare Colori con Silver (esempi per 10 colori base)

**Rosso + Silver:**
```css
background: linear-gradient(135deg, #94A3B8 0%, #E2E8F0 30%, #DC2626 60%, #991B1B 100%);
/* oppure per testo: color: #C0A0A8 (rosso desaturato con grigio silver) */
```

**Blu + Silver:**
```css
background: linear-gradient(135deg, #94A3B8 0%, #E2E8F0 25%, #1D4ED8 60%, #1E3A5F 100%);
```

**Verde + Silver:**
```css
background: linear-gradient(135deg, #94A3B8 0%, #D1E8E0 30%, #059669 60%, #065F46 100%);
```

**Viola + Silver:**
```css
background: linear-gradient(135deg, #94A3B8 0%, #E8D5F0 30%, #7C3AED 60%, #4C1D95 100%);
```

**Arancione + Silver:**
```css
background: linear-gradient(135deg, #94A3B8 0%, #F0E8D5 30%, #EA580C 60%, #9A3412 100%);
```

**Oro/Gold + Silver (dal sito Agency):**
```css
background: linear-gradient(135deg,
  #94A3B8 0%,
  #E2E8F0 15%,
  #E3C878 35%,
  #FFFFFF 50%,
  #E3C878 65%,
  #E2E8F0 85%,
  #94A3B8 100%
);
```

**Nero + Silver (pattern interrupt scuro):**
```css
background: #020202;
/* accent: bordi e highlights in #94A3B8 */
border: 1px solid rgba(148, 163, 184, 0.3);
box-shadow: inset 0 1px 0 rgba(255,255,255,0.05), 0 0 30px rgba(148,163,184,0.1);
```

**Bianco + Silver (pattern interrupt chiaro):**
```css
background: #FFFFFF;
/* accent: shadows silver */
box-shadow: 0 4px 24px rgba(148,163,184,0.2), 0 1px 4px rgba(148,163,184,0.3);
```

**Cyan + Silver:**
```css
background: linear-gradient(135deg, #94A3B8, #E0F7FA, #0891B2);
```

**Rosa/Magenta + Silver:**
```css
background: linear-gradient(135deg, #94A3B8, #FCE7F3, #DB2777);
```

### Regola per i Bordi (sempre silver)
```css
border: 1px solid rgba(148, 163, 184, 0.4);
/* per elementi premium: */
border: 1px solid;
border-image: linear-gradient(135deg, #94A3B8, #E2E8F0, #94A3B8) 1;
```

---

## REGOLA 2: GRAIN TEXTURE (OGNI SEZIONE, SENZA ECCEZIONI)

### Implementazione Standard (copia esatta dal sito Agency)
```html
<!-- Wrapper sezione con grana -->
<section style="position: relative; overflow: hidden;">
  <!-- Contenuto sezione -->
  <div class="section-content">...</div>

  <!-- Layer grana — va SEMPRE come ultimo figlio -->
  <div style="
    position: absolute;
    inset: 0;
    background-image: url('https://grainy-gradients.vercel.app/noise.svg');
    filter: contrast(170%) brightness(150%);
    opacity: 0.38;
    mix-blend-mode: overlay;
    pointer-events: none;
    z-index: 10;
  "></div>
</section>
```

### Variante Grana Digitale (per sezioni tech/scure)
```html
<div style="
  position: absolute;
  inset: 0;
  background-image: url(\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E\");
  background-size: 100px 100px;
  filter: contrast(160%) brightness(40%);
  opacity: 0.3;
  mix-blend-mode: screen;
  pointer-events: none;
  z-index: 10;
"></div>
```

### Regole Opacity per Tipo di Sfondo
- Sfondo nero scuro: opacity `0.40-0.45`
- Sfondo scuro colorato: opacity `0.35-0.40`
- Sfondo chiaro/bianco: opacity `0.25-0.35` (ridotta per non sporcare)
- Sfondo bianco puro: opacity `0.20` + `mix-blend-mode: multiply`

---

## REGOLA 3: PATTERN INTERRUPT (ALMENO 1 PER SITO)

### Schema Alternanza Sezioni
```
Sezione 1: SCURA (#020202 o colore scuro)
Sezione 2: CHIARA (#FFFFFF o crema #FFFEF5)
Sezione 3: SCURA
...
```

### CSS Sezione Scura
```css
.section-dark {
  background-color: #020202;
  color: #FFFFFF;
}
```

### CSS Sezione Chiara
```css
.section-light {
  background-color: #FFFFFF;
  color: #020202;
}
/* oppure crema calda */
.section-cream {
  background-color: #FFFEF5;
  color: #1a1a1a;
}
```

---

## SHADOW SYSTEM (3D Premium)

### Shadow Card (stile sito Agency)
```css
/* Card su sfondo scuro */
box-shadow:
  inset 0 1px 0 rgba(255,255,255,0.08),
  0 4px 16px rgba(0,0,0,0.4),
  0 1px 4px rgba(148,163,184,0.1);

/* Card su sfondo chiaro */
box-shadow:
  inset 0 1px 0 rgba(255,255,255,1),
  0 4px 24px rgba(148,163,184,0.25),
  0 2px 8px rgba(0,0,0,0.08);
```

### Button Shadow (lifting effect)
```css
.btn {
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.9),
    0 2px 4px rgba(0,0,0,0.3);
  transition: all 0.2s ease;
}
.btn:hover {
  transform: translateY(-2px);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.9),
    0 6px 12px rgba(0,0,0,0.35);
}
.btn:active {
  transform: translateY(1px);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.6),
    0 1px 2px rgba(0,0,0,0.2);
}
```

---

## TYPOGRAPHY SCALE

```css
/* Font stack (Google Fonts) */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;700&display=swap');

/* Heading premium */
.heading-display {
  font-family: 'Cinzel', serif;
  font-weight: 700;
  letter-spacing: 0.02em;
}

/* Body elegante */
.body-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  line-height: 1.7;
}

/* Bold inline (per regola lowercase+bold) */
strong, .bold-word {
  font-weight: 700;
  /* su sfondo scuro: */
  color: #E2E8F0; /* silver-200, più luminoso del testo normale */
}
```

---

## ANIMAZIONI CSS

```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes shimmer {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}

/* Shimmer effect su testo */
.text-shimmer {
  background: linear-gradient(90deg, #94A3B8 0%, #FFFFFF 50%, #94A3B8 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 3s linear infinite;
}
```

### Scroll Reveal (Intersection Observer — vanilla JS)
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(el => {
    if (el.isIntersecting) {
      el.target.style.opacity = '1';
      el.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
  observer.observe(el);
});
```

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
