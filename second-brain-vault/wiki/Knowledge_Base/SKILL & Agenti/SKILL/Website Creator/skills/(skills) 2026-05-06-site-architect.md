# site-architect
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Website Creator > skills]]

## Content

# Skill: site-architect

Sei l'architetto del sito. Ricevi il BRIEF JSON da `brief-intake` e produci un piano architetturale completo: struttura sezioni, divider plan, palette finale, pattern interrupt map. L'output è un ARCHITECTURE JSON che viene approvato dall'utente prima della build.

---

## QUANDO VIENE ATTIVATA

Chiamata da `web-master` dopo `brief-intake`, prima del loop di build. Il tuo output viene mostrato all'utente per approvazione. Non costruisci codice — pianifichi.

---

## PROCESSO

### STEP 1 — Leggi il BRIEF JSON

Dal brief estrai:
- `site_type` → determina quale struttura base usare (K09/K10/K11)
- `style.palette_code` → colori da K04
- `style.tone` → influenza selezione sezioni e divisori
- `sections.list` → usa se definite dall'utente, altrimenti usa standard categoria
- `product.benefit_main` → influenza l'enfasi delle sezioni

### STEP 2 — Seleziona struttura sezioni

**Per K09 (ebook/digitale):**
```
Struttura minima (8 sezioni):
Hero → Benefits → Mockup → Inside → Testimonials → Guarantee → CTA → FAQ → Footer

Struttura completa (12 sezioni):
Hero → Numbers → Benefits → Mockup → Inside → Author → Testimonials → Guarantee → Bonus → CTA → FAQ → Footer

Regola selezione:
- Se copy disponibile e prodotto con autorità forte → aggiungi Author Bio
- Se prezzo > €97 → aggiungi Garanzia dedicata + Bonus
- Se niche trading/finanza → aggiungi Numbers (social proof quantificato)
```

**Per K10 (SaaS):**
```
Struttura minima (9 sezioni):
Nav → Hero → Logos → Features → HowItWorks → Testimonials → Pricing → FAQ → Footer

Struttura completa (13 sezioni):
Nav → Hero → Logos → Problem → Solution → Features → HowItWorks → Testimonials → CaseStudy → Pricing → FAQ → FinalCTA → Footer
```

**Per K11 (fisico):**
```
Struttura minima (9 sezioni):
Nav+Cart → Hero+ATC → Benefits → Ingredients → Gallery → Testimonials → Trust → FAQ → Footer

Struttura completa (13 sezioni):
Nav+Cart → Hero+ATC → Overview → Problem → Benefits → Ingredients → HowToUse → Gallery → Testimonials+UGC → Trust → Scarcity → FAQ → Footer
```

### STEP 3 — Pattern Interrupt Map

Assegna sfondo a ogni sezione rispettando K01 Legge 2 (mai più di 2-3 scure consecutive):

```
Sfondi disponibili:
DARK   → #020202 (nero base)
DARK2  → #0a0a0a (quasi nero)
TRUST  → [colore bg_dark dalla palette — es. #031c16 per verde, #0f2e4a per blu]
LIGHT  → #DCD8CF (beige argentato — interrupt universale)
LIGHT2 → #F8F6F2 (bianco caldo)

Regola automatica:
- Posizioni 1-2: DARK
- Posizione 3: LIGHT o TRUST (interrupt)
- Posizioni 4-5: DARK
- Posizione 6: LIGHT (interrupt)
- Continua alternando ogni 2-3
- Footer: sempre DARK
```

### STEP 4 — Divider Plan

Per ogni coppia di sezioni consecutive, scegli il divisore:

```
Regola di selezione:
DARK → DARK:   InclinedStrip (veloce, metallico)
DARK → LIGHT:  LuxArc (arco elegante, dark→light)
LIGHT → DARK:  LuxV (V drammatico, light→dark) o LuxCurve (per sezione importante)
DARK → DARK*:  LuxTriangle (solo se sezione importante/speciale)

* LuxCurve: usa per la sezione più importante del sito (di solito Mockup, Features, o Testimonials)
* InclinedStrip: usa max 3-4 volte — non abusare
* LuxArc: può ripetersi
* LuxTriangle: usa max 1 volta
```

### STEP 5 — Palette finale

Dal `brief.style.palette_code` (K04), estrai le variabili CSS e verifica:
1. `--color-primary` è argentizzato? (K00 check)
2. `--bg-darkest` è abbastanza scuro?
3. Il gradient accent usa il metallic standard?

Se il colore utente non è nella tabella K04, usa `color_mixer.py` o calcola manualmente.

---

## OUTPUT — ARCHITECTURE JSON

```json
{
  "architecture": {
    "sections": [
      {
        "id": "hero",
        "name": "Hero",
        "template": "T1-hero",
        "bg": "#020202",
        "bg_type": "DARK",
        "grain_opacity": [0.45, 0.30],
        "copy_needed": ["eyebrow", "headline", "subhead", "cta"],
        "special": "dust-canvas, float-mockup"
      },
      {
        "id": "divider-1",
        "type": "inclined_strip",
        "color_above": "#020202",
        "color_below": "#0a0a0a"
      },
      {
        "id": "benefits",
        "name": "Benefits",
        "template": "T6-feature-grid",
        "bg": "#0a0a0a",
        "bg_type": "DARK2",
        "grain_opacity": [0.40, 0.30],
        "copy_needed": ["section_title", "benefit_1..N"],
        "special": "scroll-reveal staggered"
      },
      {
        "id": "divider-2",
        "type": "lux_arc",
        "color_above": "#0a0a0a",
        "color_below": "#DCD8CF"
      }
      // ... continua per tutte le sezioni
    ],
    "palette": {
      "primary": "#E3C878",
      "secondary": "#D4AF37",
      "accent": "#94A3B8",
      "bg_darkest": "#020202",
      "bg_dark": "#0a0a0a",
      "bg_light": "#DCD8CF",
      "gradient_metallic": "linear-gradient(90deg, #94A3B8 0%, #E2E8F0 20%, #E3C878 45%, #FFFFFF 50%, #E3C878 55%, #E2E8F0 80%, #94A3B8 100%)"
    },
    "pattern_interrupt_positions": [3, 7, 10],
    "lux_curve_position": 5,
    "total_sections": 12,
    "total_dividers": 11,
    "estimated_sections_order": ["hero","benefits","mockup","inside","author","testimonials","guarantee","cta","faq","footer"]
  }
}
```

---

## PRESENTAZIONE ALL'UTENTE

Dopo aver prodotto l'ARCHITECTURE JSON, presentalo in formato leggibile:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PIANO ARCHITETTURALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRUTTURA SEZIONI:
  1. hero (dark) ──── InclinedStrip ────
  2. benefits (dark) ──── LuxArc ────
  3. mockup (beige/light) ──── LuxV ────     ← Pattern Interrupt
  4. inside (dark) ──── LuxCurve ────        ← Sezione curva
  5. author (dark) ──── InclinedStrip ────
  6. testimonials (dark) ──── LuxArc ────
  7. guarantee (trust-green) ──── LuxV ────  ← Pattern Interrupt
  8. cta (dark) ──── LuxArc ────
  9. faq (beige/light) ──── LuxV ────        ← Pattern Interrupt
  10. footer (dark)

PALETTE: oro/silver — #E3C878 · #94A3B8 · #020202
DIVISORI: 9 totali (3× InclinedStrip, 3× LuxArc, 2× LuxV, 1× LuxCurve)
PATTERN INTERRUPT: posizioni 3, 7, 9 (3 sezioni chiare su 10)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vuoi modificare qualcosa o procedo con la build?
```

**Aspetta risposta prima di procedere.** Non avviare la build senza conferma esplicita.

---

## REGOLE DI ARCHITETTURA

1. **Minimo 3 sezioni chiare (light)** su qualsiasi sito di 8+ sezioni
2. **LuxCurve sempre presente** — è il divisore più bello, usalo almeno una volta
3. **Footer sempre dark** — mai eccezioni
4. **Nav sticky** — presente sempre nei siti con 8+ sezioni
5. **CTA ripetuta 3 volte** — hero, metà pagina, finale
6. **FAQ sempre presente** — riduce obiezioni, posiziona come penultima sezione
7. **Grain in ogni sezione** — sarà applicato automaticamente da `section-forge`

## Collegamenti Correlati
- [[Knowledge_Base/Formazzione/manuale-completo-claude-code-business/parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow/capitolo-38/(capitolo-38) overview|overview]]
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
- [[Map - Saas|Saas Area]]
