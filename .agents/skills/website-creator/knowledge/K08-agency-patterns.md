# K08 — AGENCY PATTERNS (Pattern Architetturali dall'Agency)

> Pattern estratti direttamente dall'analisi del sito Agency. Questi sono i "segreti" visivi che lo rendono premium.

---

## PATTERN 1 — MULTI-LAYER Z-INDEX STACK

L'Agency usa un sistema di layer stratificati. Ogni sezione è un universo:

```
z-index: 1   → StarBackground (fondo globale, raramente necessario nelle landing)
z-index: 2   → Canvas (particelle, effetti globali)
z-index: 9   → Grid layer (opzionale)
z-index: 10  → Grain Layer 1 (film grain)
z-index: 11  → Grain Layer 2 (digital noise)
z-index: 15  → Decorazioni SVG (linee divisori interni alla sezione)
z-index: 20  → Contenuto principale (testi, immagini, bottoni)
z-index: 50  → Elementi overlap (tooltip, dropdown)
z-index: 100 → Nav sticky
z-index: 200 → Modali, overlay
```

**Regola:** Il contenuto principale è SEMPRE a z-index 20+. I grain layer sono SEMPRE a z-index 10-11. Mai invertire questo ordine.

---

## PATTERN 2 — GOLD BUTTON (6 varianti)

```css
/* Variante 1: Filled Gold (default CTA) */
.btn-gold {
  background: linear-gradient(135deg, #E3C878 0%, #D4AF37 50%, #C5A059 100%);
  color: #020202;
  font-weight: 700;
  padding: 16px 40px;
  border: none;
  border-radius: 2px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 24px rgba(212,175,55,0.3);
}
.btn-gold:hover {
  transform: translateY(-2px);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.3),
    0 8px 32px rgba(212,175,55,0.5);
}

/* Variante 2: Gold Outline */
.btn-gold-outline {
  background: transparent;
  color: #E3C878;
  border: 1px solid #E3C878;
  padding: 14px 38px;
  border-radius: 2px;
  transition: all 0.3s;
}
.btn-gold-outline:hover {
  background: rgba(227,200,120,0.1);
  box-shadow: 0 0 20px rgba(227,200,120,0.2);
}

/* Variante 3: Metallic Gradient (per CTA principali grandi) */
.btn-metallic {
  background: linear-gradient(90deg, #8E9BAF, #D4AF37, #FFD700, #D4AF37, #8E9BAF);
  color: #020202;
  font-weight: 800;
  padding: 20px 56px;
  border: none;
  border-radius: 2px;
  font-size: 1rem;
  letter-spacing: 0.08em;
  transition: all 0.3s;
}
.btn-metallic:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(212,175,55,0.6);
}

/* Variante 4: Ghost Dark (secondary su sfondi scuri) */
.btn-ghost-dark {
  background: transparent;
  color: #CBD5E1;
  border: 1px solid rgba(148,163,184,0.4);
  padding: 14px 38px;
  border-radius: 2px;
  transition: all 0.3s;
}
.btn-ghost-dark:hover {
  border-color: #94A3B8;
  color: #E2E8F0;
  background: rgba(148,163,184,0.05);
}

/* Variante 5: Pulse (per CTA urgenza) */
.btn-pulse {
  animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(212,175,55,0.4); }
  50%       { box-shadow: 0 0 0 12px rgba(212,175,55,0); }
}

/* Variante 6: Full Width Mobile */
.btn-full-mobile {
  width: 100%;
  text-align: center;
  padding: 18px 24px;
}
@media (min-width: 768px) {
  .btn-full-mobile { width: auto; }
}
```

---

## PATTERN 3 — CARD METALLIC

```css
/* Card base con bordo argentato e hover oro */
.card-metallic {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 4px;
  padding: 32px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.card-metallic::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(227,200,120,0.03), transparent 60%);
  pointer-events: none;
}

.card-metallic:hover {
  border-color: rgba(227,200,120,0.3);
  background: rgba(255,255,255,0.04);
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}

/* Card con accent color border-top */
.card-accent {
  border-top: 2px solid #E3C878;
}

/* Card con inner glow */
.card-glow:hover {
  box-shadow:
    inset 0 0 30px rgba(227,200,120,0.05),
    0 8px 32px rgba(0,0,0,0.5);
}
```

---

## PATTERN 4 — DROP SHADOW TESTO (dall'Agency)

```css
/* Il drop shadow esatto dell'Agency per headline premium */
.text-shadow-premium {
  filter:
    drop-shadow(0px 4px 1px rgba(0,0,0,0.9))
    drop-shadow(0px 0px 30px rgba(253,230,138,0.15));
}

/* Versione più intensa per hero headline */
.text-shadow-hero {
  filter:
    drop-shadow(0px 6px 2px rgba(0,0,0,0.95))
    drop-shadow(0px 0px 40px rgba(227,200,120,0.2))
    drop-shadow(0px 0px 80px rgba(227,200,120,0.1));
}

/* Versione sottile per h3 */
.text-shadow-subtle {
  filter: drop-shadow(0px 2px 1px rgba(0,0,0,0.8));
}
```

---

## PATTERN 5 — PATTERN INTERRUPT (sfondo non standard)

Dall'Agency: le sezioni "trust" e "how we work" hanno sfondi unici che rompono il flusso.

```css
/* Sfondo Trust — Deep Green (come l'Agency) */
.bg-trust {
  background: #031c16;
}

/* Sfondo Pattern Interrupt — Beige argentato */
.bg-interrupt-light {
  background: #DCD8CF;
}

/* Sfondo Alternativo navy */
.bg-navy {
  background: #0f2e4a;
}

/* Sfondo Gradient dramatico per sezioni CTA */
.bg-cta-gradient {
  background: linear-gradient(180deg, #020202 0%, #0f1a08 50%, #020202 100%);
}
```

---

## PATTERN 6 — BACKDROP BLUR NAV

```html
<nav style="
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  background: rgba(2,2,2,0.7);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.3s ease;
">
  <div style="font-family:'Cinzel',serif;color:#E3C878;font-size:1.25rem;">[BRAND]</div>
  <div style="display:flex;gap:32px;align-items:center;">
    <a href="#" style="font-size:0.875rem;color:#94A3B8;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#E2E8F0'" onmouseout="this.style.color='#94A3B8'">[LINK]</a>
    <button style="font-size:0.875rem;font-weight:600;color:#020202;background:linear-gradient(135deg,#E3C878,#D4AF37);padding:10px 24px;border:none;border-radius:2px;cursor:pointer;">[CTA NAV]</button>
  </div>
</nav>
```

---

## PATTERN 7 — SECTION INDICATOR (micro-navigazione)

```html
<!-- Pallini di navigazione laterali (come Agency) -->
<div style="position:fixed;right:24px;top:50%;transform:translateY(-50%);z-index:50;display:flex;flex-direction:column;gap:8px;">
  <a href="#section1" style="width:8px;height:8px;border-radius:50%;background:#64748B;display:block;transition:all 0.3s;" title="hero"></a>
  <a href="#section2" style="width:8px;height:8px;border-radius:50%;background:#64748B;display:block;transition:all 0.3s;" title="benefits"></a>
  <!-- active state -->
  <a href="#section3" style="width:8px;height:8px;border-radius:50%;background:#E3C878;display:block;box-shadow:0 0 8px rgba(227,200,120,0.5);" title="current"></a>
</div>
```

---

## PATTERN 8 — SILVER LINE DECORATOR

Linea decorativa orizzontale con gradient metallic. Usata spesso come separatore sottile.

```html
<div style="
  height: 1px;
  background: linear-gradient(90deg, transparent 0%, #94A3B8 20%, #E3C878 50%, #94A3B8 80%, transparent 100%);
  margin: 40px auto;
  max-width: 400px;
"></div>
```

---

## PATTERN 9 — HIGHLIGHT BOX (info box premium)

```html
<div style="
  background: rgba(227,200,120,0.05);
  border: 1px solid rgba(227,200,120,0.2);
  border-left: 3px solid #E3C878;
  border-radius: 2px;
  padding: 20px 24px;
  margin: 24px 0;
">
  <p style="font-size:0.9375rem;color:#CBD5E1;margin:0;line-height:1.6;">
    <strong style="color:#E3C878;">[LABEL]:</strong> [CONTENUTO HIGHLIGHT BOX]
  </p>
</div>
```

---

## PATTERN 10 — PRICE DISPLAY

```html
<div style="display:flex;align-items:baseline;gap:8px;justify-content:center;margin:24px 0;">
  <!-- Prezzo barrato -->
  <span style="font-size:1.25rem;color:#374151;text-decoration:line-through;">[PREZZO ORIGINALE]</span>
  <!-- Prezzo attuale -->
  <span style="font-family:'Cinzel',serif;font-size:3.5rem;font-weight:700;background:linear-gradient(90deg,#E3C878,#FFFFFF,#E3C878);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">[PREZZO ATTUALE]</span>
</div>
<!-- Sconto badge -->
<div style="display:inline-block;background:rgba(192,80,90,0.15);border:1px solid rgba(192,80,90,0.4);color:#C0505A;font-size:0.75rem;font-weight:700;padding:4px 12px;border-radius:2px;letter-spacing:0.1em;">RISPARMI [X]%</div>
```

---

## CHECKLIST PATTERN AGENCY

Prima di finalizzare qualsiasi sito, verifica:

```
[ ] Nav sticky con backdrop-filter?
[ ] Almeno 1 card con hover border oro?
[ ] Drop shadow premium sulle headline?
[ ] Almeno 1 pattern interrupt (sfondo non-standard)?
[ ] Gold button con lifting hover effect?
[ ] Scrollbar custom (track nero, hover oro)?
[ ] Font Cinzel per headline (non Inter)?
[ ] Z-index stack corretto (grain 10-11, contenuto 20+)?
```
