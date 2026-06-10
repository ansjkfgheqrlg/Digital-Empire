# K05-typography
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Website Creator > knowledge]]

## Content

# K05 — TYPOGRAPHY SYSTEM

> Font, scale, regole lowercase+strong, gradient text. Da applicare a ogni sezione.

---

## IMPORT GOOGLE FONTS (da inserire nell'`<head>`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Inter:wght@200;300;400;600;700;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
```

**Font e loro ruolo:**
- **Cinzel** — titoli display, headline principale, elementi luxury (serif classico romano)
- **Inter** — body text, UI, tutto il resto (sans-serif moderna, altissima leggibilità)
- **Playfair Display** — citazioni, author bio, elementi editoriali (serif elegante, opzionale)

---

## SCALE TIPOGRAFICA

```css
/* RESET TIPOGRAFICO BASE */
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

body {
  font-family: 'Inter', sans-serif;
  font-weight: 300;
  font-size: 1rem;
  line-height: 1.7;
  color: #94A3B8;
  text-transform: lowercase;
}

/* HEADINGS */
h1, .h1 {
  font-family: 'Cinzel', serif;
  font-size: clamp(2.5rem, 6vw, 6rem);
  font-weight: 400;
  line-height: 1.1;
  letter-spacing: -0.02em;
  text-transform: lowercase;
}

h2, .h2 {
  font-family: 'Cinzel', serif;
  font-size: clamp(2rem, 4vw, 4rem);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.02em;
  text-transform: lowercase;
}

h3, .h3 {
  font-family: 'Cinzel', serif;
  font-size: clamp(1.4rem, 2.5vw, 2rem);
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -0.01em;
  text-transform: lowercase;
}

h4, .h4 {
  font-family: 'Inter', sans-serif;
  font-size: 1.125rem;
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: 0.01em;
  text-transform: lowercase;
}

/* BODY */
p {
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: 300;
  line-height: 1.7;
  color: #94A3B8;
  margin-bottom: 1em;
}

/* LISTE */
li {
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: 300;
  line-height: 1.7;
  color: #94A3B8;
  margin-bottom: 0.5em;
}

/* STRONG — regola fondamentale */
strong {
  font-weight: 700;
  color: #E2E8F0;
}

/* LABEL / EYEBROW (sopra i titoli) */
.label {
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase; /* ECCEZIONE: solo le label eyebrow sono uppercase */
  color: #94A3B8;
}

/* CAPTION */
.caption {
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 300;
  color: #64748B;
  line-height: 1.5;
}

/* QUOTE (Playfair Display) */
blockquote {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.2rem, 2vw, 1.8rem);
  font-weight: 400;
  font-style: italic;
  line-height: 1.5;
  color: #CBD5E1;
}
```

---

## REGOLA LOWERCASE — DETTAGLI

**Cosa va in lowercase:**
- Tutti i titoli h1, h2, h3
- Tutti i body text (già scritto in minuscolo)
- Label dei bottoni CTA: "ottieni accesso ora", "inizia gratis", "scopri di più"
- Item delle liste
- Alt text immagini

**ECCEZIONI (non vanno in lowercase):**
- Abbreviazioni standard: SaaS, FAQ, CTA, SEO, ROI, API
- Nomi propri di brand/prodotti: "ChatGPT", "Stripe", "Apple"
- Unità di misura: "30-day", "24/7"
- Numeri e metriche: "4.8/5", "+2.000 clienti"

**Implementazione CSS:**
```css
/* Metodo 1: CSS (più sicuro, si applica automaticamente) */
h1, h2, h3, h4, h5, h6 { text-transform: lowercase; }
.cta-text { text-transform: lowercase; }

/* Metodo 2: scritto direttamente minuscolo nell'HTML */
<h1>il titolo della sezione hero</h1>
```

---

## REGOLA STRONG — DETTAGLI

**Ogni `<p>` e `<li>` deve avere 1-2 `<strong>`.**

**Dove mettere lo strong:**
- Sul beneficio principale della frase
- Sul numero o dato statistico
- Sul termine chiave che il lettore deve ricordare

**Esempio CORRETTO:**
```html
<p>questo sistema ti permette di <strong>creare siti web professionali</strong> in meno di 2 ore, senza scrivere una riga di codice.</p>
<li>oltre <strong>12.000 clienti soddisfatti</strong> in 47 paesi</li>
<li>garanzia <strong>rimborso completo</strong> entro 30 giorni</li>
```

**Esempio SBAGLIATO:**
```html
<p>questo sistema ti permette di creare siti web professionali in meno di 2 ore.</p>
<!-- ❌ nessun strong → viola K01 Legge 3 -->
```

**CSS strong per sezioni chiare:**
```css
.section-light strong { color: #020202; font-weight: 800; }
.section-light p { color: #374151; }
.section-light li { color: #374151; }
```

---

## GRADIENT TEXT (dall'Agency)

```css
/* Gradient text dorato — per headline principali */
.gradient-text-gold {
  background: linear-gradient(
    90deg,
    #94A3B8 0%,
    #E2E8F0 30%,
    #E3C878 55%,
    #FFFFFF 65%,
    #E3C878 75%,
    #CBD5E1 100%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0px 4px 1px rgba(0,0,0,0.9))
          drop-shadow(0px 0px 30px rgba(253,230,138,0.15));
}

/* Gradient text silver — per titoli sezioni chiare */
.gradient-text-silver {
  background: linear-gradient(
    90deg,
    #64748B 0%,
    #94A3B8 40%,
    #E2E8F0 60%,
    #94A3B8 100%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Shimmer effect sul gradient text */
.gradient-text-shimmer {
  background-size: 200% auto;
  animation: shimmerText 3s linear infinite;
}
@keyframes shimmerText {
  0%   { background-position: -200% center; }
  100% { background-position: 200% center; }
}
```

---

## BOTTONI CTA — TIPOGRAFIA

```css
/* Bottone CTA dorato (principale) */
.btn-cta {
  font-family: 'Inter', sans-serif;
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: lowercase;
  color: #020202;
  background: linear-gradient(135deg, #E3C878, #D4AF37);
  padding: 16px 40px;
  border-radius: 2px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 24px rgba(212, 175, 55, 0.3);
}

.btn-cta:hover {
  transform: translateY(-2px);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.3),
    0 8px 32px rgba(212, 175, 55, 0.5);
}

/* Bottone outline silver */
.btn-outline {
  font-family: 'Inter', sans-serif;
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: lowercase;
  color: #CBD5E1;
  background: transparent;
  padding: 14px 38px;
  border: 1px solid rgba(148, 163, 184, 0.5);
  border-radius: 2px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  border-color: #E3C878;
  color: #E3C878;
}
```

---

## MOBILE TYPOGRAPHY

```css
@media (max-width: 768px) {
  h1 { font-size: clamp(2rem, 8vw, 3rem); }
  h2 { font-size: clamp(1.6rem, 6vw, 2.5rem); }
  h3 { font-size: clamp(1.2rem, 4vw, 1.6rem); }
  p  { font-size: 0.9375rem; }
  li { font-size: 0.9375rem; }
}
```

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Saas|Saas Area]]
