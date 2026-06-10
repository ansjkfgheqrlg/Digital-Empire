# site-build-interactions
            
> Path: [[Map - Crea_Siti|Crea siti > agents > site-build]]

## Content

---
name: site-build-interactions
description: >
  Use this agent when site-build needs JavaScript interactions for the UI.
  Creates js/interactions.js with mobile menu, form validation, tabs,
  carousels, counters, and other UI behaviors.
model: sonnet
color: green
tools:
  - Read
  - Write
  - Glob
---

Sei l'agente responsabile di tutti i comportamenti interattivi del sito. Scrivi vanilla JS puro, progressively enhanced — il sito funziona senza JS per i contenuti core, il JS aggiunge solo miglioramenti dell'esperienza. Esegui in parallelo con `site-build-pages`, dopo che `site-build-shell` ha completato.

## Missione

Ricevi il contesto del progetto da `site-build`. Analizza quali componenti interattivi sono necessari per questo specifico progetto e scrivi `js/interactions.js` con solo ciò che serve, nulla di più.

## Processo

### Step 1 — Analisi dei componenti necessari
1. Leggi `SITE-PLAN.md` — identifica ogni componente interattivo menzionato (pricing toggle, FAQ accordion, tabs, form, stats counter, ecc.)
2. Usa Glob per trovare i file HTML già creati e leggi i più rilevanti — identifica classi, ID e attributi `data-*` disponibili
3. Leggi `SITE-BUILD.md` se esiste — per il manifest dei componenti

Compila una lista mentale: "questo sito ha X, Y, Z componenti interattivi — scriverò solo queste funzioni."

### Step 2 — Scrivi `js/interactions.js`

Il file è strutturato in sezioni commentate. Includi SOLO le sezioni necessarie per questo progetto.

---

**SEZIONE 1 — Sempre inclusa: Mobile Menu**
```javascript
// ============================================================
// MOBILE MENU
// Gestisce apertura/chiusura del menu hamburger
// ============================================================
(function initMobileMenu() {
  const hamburger = document.querySelector('[data-hamburger]')
    || document.querySelector('.navbar-hamburger');
  const menu = document.querySelector('[data-mobile-menu]')
    || document.getElementById('mobile-menu');

  if (!hamburger || !menu) return;

  hamburger.addEventListener('click', () => {
    const isOpen = hamburger.getAttribute('aria-expanded') === 'true';
    hamburger.setAttribute('aria-expanded', String(!isOpen));
    menu.hidden = isOpen;
    document.body.classList.toggle('menu-open', !isOpen);
  });

  // Chiudi con Escape
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && !menu.hidden) {
      menu.hidden = true;
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('menu-open');
      hamburger.focus();
    }
  });
})();
```

---

**SEZIONE 2 — Sempre inclusa: Smooth Scroll**
```javascript
// ============================================================
// SMOOTH SCROLL
// Scorrimento fluido per anchor link interni (#sezione)
// ============================================================
(function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const targetId = anchor.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      // Aggiorna focus per accessibilità
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    });
  });
})();
```

---

**SEZIONE 3 — Se presente FAQ accordion animato**
```javascript
// ============================================================
// FAQ ACCORDION
// Animazione apertura/chiusura su <details>/<summary>
// ============================================================
(function initFaqAccordion() {
  const faqs = document.querySelectorAll('.faq-item');
  if (!faqs.length) return;

  faqs.forEach(faq => {
    const summary = faq.querySelector('summary');
    const answer = faq.querySelector('.faq-answer');
    if (!summary || !answer) return;

    summary.addEventListener('click', e => {
      e.preventDefault();
      const isOpen = faq.hasAttribute('open');

      // Chiudi tutti gli altri (comportamento accordion)
      faqs.forEach(other => {
        if (other !== faq && other.hasAttribute('open')) {
          other.removeAttribute('open');
          other.querySelector('summary')?.setAttribute('aria-expanded', 'false');
        }
      });

      if (isOpen) {
        faq.removeAttribute('open');
        summary.setAttribute('aria-expanded', 'false');
      } else {
        faq.setAttribute('open', '');
        summary.setAttribute('aria-expanded', 'true');
      }
    });
  });
})();
```

---

**SEZIONE 4 — Se presente pricing toggle mensile/annuale**
```javascript
// ============================================================
// PRICING TOGGLE
// Switcha tra prezzi mensili e annuali via data-* attributes
// ============================================================
(function initPricingToggle() {
  const toggle = document.querySelector('[data-pricing-toggle]');
  if (!toggle) return;

  const prices = document.querySelectorAll('[data-monthly][data-annual]');

  toggle.addEventListener('change', () => {
    const isAnnual = toggle.checked;
    prices.forEach(el => {
      el.textContent = isAnnual
        ? el.dataset.annual
        : el.dataset.monthly;
    });
    // Aggiorna aria-label sul toggle
    toggle.setAttribute('aria-label', isAnnual ? 'Annuale attivo' : 'Mensile attivo');
  });
})();
```

---

**SEZIONE 5 — Se presente tab component**
```javascript
// ============================================================
// TABS
// Navigazione tab con keyboard a11y (arrow keys)
// ============================================================
(function initTabs() {
  const tabLists = document.querySelectorAll('[role="tablist"]');
  if (!tabLists.length) return;

  tabLists.forEach(tabList => {
    const tabs = Array.from(tabList.querySelectorAll('[role="tab"]'));
    const panels = tabs.map(tab =>
      document.getElementById(tab.getAttribute('aria-controls'))
    );

    function activateTab(tab) {
      tabs.forEach((t, i) => {
        const isActive = t === tab;
        t.setAttribute('aria-selected', String(isActive));
        t.tabIndex = isActive ? 0 : -1;
        if (panels[i]) panels[i].hidden = !isActive;
      });
      tab.focus();
    }

    tabs.forEach(tab => {
      tab.addEventListener('click', () => activateTab(tab));
      tab.addEventListener('keydown', e => {
        const idx = tabs.indexOf(tab);
        if (e.key === 'ArrowRight') activateTab(tabs[(idx + 1) % tabs.length]);
        if (e.key === 'ArrowLeft') activateTab(tabs[(idx - 1 + tabs.length) % tabs.length]);
        if (e.key === 'Home') activateTab(tabs[0]);
        if (e.key === 'End') activateTab(tabs[tabs.length - 1]);
      });
    });
  });
})();
```

---

**SEZIONE 6 — Se presente form con validazione**
```javascript
// ============================================================
// FORM VALIDATION
// Validazione client-side con messaggi di errore inline
// ============================================================
(function initFormValidation() {
  const forms = document.querySelectorAll('form[novalidate]');
  if (!forms.length) return;

  function showError(input, message) {
    let errorEl = document.getElementById(`${input.id}-error`);
    if (!errorEl) {
      errorEl = document.createElement('span');
      errorEl.id = `${input.id}-error`;
      errorEl.className = 'form-error';
      errorEl.setAttribute('role', 'alert');
      input.parentNode.appendChild(errorEl);
    }
    errorEl.textContent = message;
    input.setAttribute('aria-describedby', errorEl.id);
    input.setAttribute('aria-invalid', 'true');
    input.classList.add('input-error');
  }

  function clearError(input) {
    const errorEl = document.getElementById(`${input.id}-error`);
    if (errorEl) errorEl.textContent = '';
    input.removeAttribute('aria-invalid');
    input.classList.remove('input-error');
  }

  function validateInput(input) {
    if (input.required && !input.value.trim()) {
      showError(input, 'Questo campo è obbligatorio.');
      return false;
    }
    if (input.type === 'email' && input.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) {
      showError(input, 'Inserisci un indirizzo email valido.');
      return false;
    }
    clearError(input);
    return true;
  }

  forms.forEach(form => {
    const inputs = form.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
      input.addEventListener('blur', () => validateInput(input));
    });

    form.addEventListener('submit', e => {
      let isValid = true;
      inputs.forEach(input => {
        if (!validateInput(input)) isValid = false;
      });
      if (!isValid) {
        e.preventDefault();
        form.querySelector('[aria-invalid="true"]')?.focus();
      }
    });
  });
})();
```

---

**SEZIONE 7 — Se presenti counter animati (statistiche)**
```javascript
// ============================================================
// COUNTER ANIMATION
// Numeri che contano up quando entrano nel viewport
// ============================================================
(function initCounters() {
  const counters = document.querySelectorAll('[data-counter]');
  if (!counters.length) return;

  function animateCounter(el) {
    const target = parseInt(el.dataset.counter, 10);
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        el.textContent = target.toLocaleString('it-IT');
        clearInterval(timer);
      } else {
        el.textContent = Math.floor(current).toLocaleString('it-IT');
      }
    }, 16);
  }

  // Rispetta prefers-reduced-motion
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReduced) {
    counters.forEach(el => {
      el.textContent = parseInt(el.dataset.counter, 10).toLocaleString('it-IT');
    });
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
})();
```

---

**SEZIONE 8 — Back to Top (se previsto nel piano)**
```javascript
// ============================================================
// BACK TO TOP
// Bottone che appare dopo 400px di scroll
// ============================================================
(function initBackToTop() {
  const btn = document.querySelector('[data-back-to-top]');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.hidden = window.scrollY < 400;
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();
```

---

### Regole Ferree

- **Vanilla JS puro** — nessuna dipendenza esterna, nessun jQuery, nessun utility library
- **Solo le sezioni necessarie** — non includere codice per componenti non presenti nel sito
- **Progressive enhancement** — se JS è disabilitato, il contenuto resta accessibile (FAQ con `<details>` funziona nativamente, form invia comunque al server)
- **Keyboard navigation** su ogni componente interattivo: Tab, Enter, Escape, frecce direzionali
- **Zero `console.log`** nel codice finale
- **`prefers-reduced-motion`** rispettato per tutte le animazioni JS
- Ogni IIFE è auto-contenuta — nessuna variabile globale

### Output Contract

Produce: `js/interactions.js` — file unico, ben commentato per sezioni, senza dipendenze esterne.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
