# K04 — COLOR SYSTEM (Silver Mixing + 12 Palette)

> Sistema colori completo. Usa questo file ogni volta che devi generare una palette per un progetto.

---

## VARIABILI CSS BASE (da inserire in ogni `:root`)

```css
:root {
  /* Silver base (immutabili) */
  --silver-cool:   #94A3B8;
  --silver-light:  #E2E8F0;
  --silver-medium: #CBD5E1;
  --silver-dark:   #64748B;

  /* Sfondi */
  --bg-darkest:    #020202;
  --bg-dark:       #0a0a0a;
  --bg-beige:      #DCD8CF;
  --bg-white:      #F8F6F2;

  /* Tipografia su scuro */
  --text-muted:    #94A3B8;  /* corpo testo */
  --text-base:     #CBD5E1;  /* testo normale */
  --text-bright:   #E2E8F0;  /* strong, emphasis */

  /* Tipografia su chiaro */
  --text-light-muted:  #374151;
  --text-light-base:   #1F2937;
  --text-light-bright: #020202;

  /* Scrollbar */
  --scrollbar-track: #0a0a0a;
  --scrollbar-thumb: #333333;
  --scrollbar-hover: #E3C878;
}

/* Scrollbar CSS custom */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--scrollbar-track); }
::-webkit-scrollbar-thumb { background: var(--scrollbar-thumb); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--scrollbar-hover); }
```

---

## 12 PALETTE PRE-GENERATE

### PALETTE 1 — ORO/SILVER (default Agency, lusso universale)
```css
--color-primary:   #E3C878;
--color-secondary: #D4AF37;
--color-accent:    #94A3B8;
--color-bg-main:   #020202;
--color-bg-alt:    #0a0a0a;
--color-bg-light:  #DCD8CF;
--gradient-hero: linear-gradient(135deg, #020202 0%, #0f1a0a 50%, #020202 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #E3C878, #FFF, #E3C878, #E2E8F0, #94A3B8);
```

### PALETTE 2 — VERDE SILVER (wellness, finanza, sostenibilità)
```css
--color-primary:   #4A9B7A;
--color-secondary: #2D6A4F;
--color-accent:    #94A3B8;
--color-bg-main:   #031c16;
--color-bg-alt:    #051f18;
--color-bg-light:  #E8EDE9;
--gradient-hero: linear-gradient(135deg, #031c16 0%, #051f18 50%, #031c16 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #4A9B7A, #A8D5BE, #4A9B7A, #E2E8F0, #94A3B8);
```

### PALETTE 3 — VIOLA SILVER (tech, creatività, premium)
```css
--color-primary:   #7B6FA8;
--color-secondary: #6B5B95;
--color-accent:    #94A3B8;
--color-bg-main:   #1A1028;
--color-bg-alt:    #130D1F;
--color-bg-light:  #E8E6F0;
--gradient-hero: linear-gradient(135deg, #1A1028 0%, #130D1F 50%, #1A1028 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #7B6FA8, #C5C0D8, #7B6FA8, #E2E8F0, #94A3B8);
```

### PALETTE 4 — ROSSO SILVER (urgency, salute, energia, trading)
```css
--color-primary:   #C0505A;
--color-secondary: #9B3D45;
--color-accent:    #94A3B8;
--color-bg-main:   #1A0608;
--color-bg-alt:    #120305;
--color-bg-light:  #F0E8E9;
--gradient-hero: linear-gradient(135deg, #1A0608 0%, #120305 50%, #1A0608 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #C0505A, #E8A0A8, #C0505A, #E2E8F0, #94A3B8);
```

### PALETTE 5 — BLU SILVER (SaaS, finanza, professionale)
```css
--color-primary:   #4A7FB5;
--color-secondary: #3D6E9E;
--color-accent:    #94A3B8;
--color-bg-main:   #0f2e4a;
--color-bg-alt:    #0a2238;
--color-bg-light:  #E6EEF4;
--gradient-hero: linear-gradient(135deg, #0f2e4a 0%, #0a2238 50%, #0f2e4a 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #4A7FB5, #A0C4E0, #4A7FB5, #E2E8F0, #94A3B8);
```

### PALETTE 6 — CYAN SILVER (tech, innovazione, futuro)
```css
--color-primary:   #4A9DAB;
--color-secondary: #3D8A96;
--color-accent:    #94A3B8;
--color-bg-main:   #041C20;
--color-bg-alt:    #031419;
--color-bg-light:  #E6F0F2;
--gradient-hero: linear-gradient(135deg, #041C20 0%, #031419 50%, #041C20 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #4A9DAB, #A0D5DE, #4A9DAB, #E2E8F0, #94A3B8);
```

### PALETTE 7 — ROSA SILVER (lifestyle, beauty, wellness femminile)
```css
--color-primary:   #C48A9A;
--color-secondary: #B5778A;
--color-accent:    #94A3B8;
--color-bg-main:   #1A0A10;
--color-bg-alt:    #120508;
--color-bg-light:  #F2EAEd;
--gradient-hero: linear-gradient(135deg, #1A0A10 0%, #120508 50%, #1A0A10 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #C48A9A, #E8C0CA, #C48A9A, #E2E8F0, #94A3B8);
```

### PALETTE 8 — ARANCIONE SILVER (lifestyle, food, DTC warm)
```css
--color-primary:   #C47A3A;
--color-secondary: #A86530;
--color-accent:    #94A3B8;
--color-bg-main:   #1A0E05;
--color-bg-alt:    #120A03;
--color-bg-light:  #F2EBE0;
--gradient-hero: linear-gradient(135deg, #1A0E05 0%, #120A03 50%, #1A0E05 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #C47A3A, #E0B880, #C47A3A, #E2E8F0, #94A3B8);
```

### PALETTE 9 — TEAL SILVER (salute, natura, meditazione)
```css
--color-primary:   #3D7A72;
--color-secondary: #2F6560;
--color-accent:    #94A3B8;
--color-bg-main:   #041518;
--color-bg-alt:    #030F12;
--color-bg-light:  #E6EFEE;
--gradient-hero: linear-gradient(135deg, #041518 0%, #030F12 50%, #041518 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #3D7A72, #9AC5C0, #3D7A72, #E2E8F0, #94A3B8);
```

### PALETTE 10 — NAVY SILVER (luxury, autorità, istituzionale)
```css
--color-primary:   #E3C878;
--color-secondary: #94A3B8;
--color-accent:    #CBD5E1;
--color-bg-main:   #020617;
--color-bg-alt:    #0A1628;
--color-bg-light:  #E6E8F0;
--gradient-hero: linear-gradient(135deg, #020617 0%, #0A1628 50%, #020617 100%);
--gradient-accent: linear-gradient(90deg, #64748B, #CBD5E1, #E3C878, #FFF, #E3C878, #CBD5E1, #64748B);
```

### PALETTE 11 — EMERALD SILVER (finanza, investimenti, prosperità)
```css
--color-primary:   #026c4a;
--color-secondary: #4A9B7A;
--color-accent:    #94A3B8;
--color-bg-main:   #031c16;
--color-bg-alt:    #020F0C;
--color-bg-light:  #E0EDE8;
--gradient-hero: linear-gradient(135deg, #031c16 0%, #020F0C 50%, #031c16 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #026c4a, #80C8A8, #026c4a, #E2E8F0, #94A3B8);
```

### PALETTE 12 — BURGUNDY SILVER (lusso maturo, vino, high-end)
```css
--color-primary:   #8B3A4E;
--color-secondary: #6B2B3A;
--color-accent:    #94A3B8;
--color-bg-main:   #150508;
--color-bg-alt:    #0D0305;
--color-bg-light:  #F0E6E9;
--gradient-hero: linear-gradient(135deg, #150508 0%, #0D0305 50%, #150508 100%);
--gradient-accent: linear-gradient(90deg, #94A3B8, #E2E8F0, #8B3A4E, #C890A0, #8B3A4E, #E2E8F0, #94A3B8);
```

---

## ALGORITMO DI SCELTA PALETTE

Dato il tipo di prodotto/servizio:

| Categoria | Palette consigliata |
|-----------|---------------------|
| Ebook trading/finanza | PALETTE 1 (oro/silver) o PALETTE 4 (rosso) |
| Ebook wellness/fitness | PALETTE 2 (verde) o PALETTE 9 (teal) |
| Ebook educativo | PALETTE 5 (blu) o PALETTE 1 (oro) |
| SaaS generico | PALETTE 5 (blu) o PALETTE 3 (viola) |
| SaaS fintech | PALETTE 10 (navy) o PALETTE 11 (emerald) |
| SaaS creativo | PALETTE 3 (viola) o PALETTE 6 (cyan) |
| Prodotto fisico luxury | PALETTE 1 (oro) o PALETTE 12 (burgundy) |
| Prodotto fisico fitness | PALETTE 2 (verde) o PALETTE 8 (arancione) |
| Prodotto fisico beauty | PALETTE 7 (rosa) o PALETTE 1 (oro) |
| Lifestyle/DTC | PALETTE 8 (arancione) o PALETTE 9 (teal) |

---

## COME APPLICARE LA PALETTE AL PROGETTO

```css
/* 1. Definisci le variabili palette nel :root */
:root {
  --color-primary: [valore palette scelta];
  --color-secondary: [valore];
  /* ...etc */
}

/* 2. Usa le variabili invece di hex diretti */
.cta-button { background: var(--color-primary); }
h1 { color: var(--color-primary); }
.card-border { border-color: rgba(var(--color-primary-rgb), 0.3); }

/* 3. Gradient text con palette colori */
.gradient-text {
  background: linear-gradient(90deg, var(--silver-cool), var(--color-primary), var(--silver-light));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

---

## VERIFICA COLORI — REGOLA PRATICA

Se un colore hex ti sembra "troppo vivido" o "plastico", argentizzalo così:

```css
/* Overlay silver su qualsiasi elemento colorato */
.element-to-silver {
  position: relative;
}
.element-to-silver::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(148,163,184,0.2), transparent 60%);
  mix-blend-mode: overlay;
  pointer-events: none;
}
```

Questo trucco aggiunge una velatura silver su qualsiasi elemento senza cambiare l'hex.
