# section-patterns
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Skill empire-premium-style > references]]

## Content

# Section Patterns — Galleria pattern Empire

**REGOLA D'ORO**: Il file canonico con tutti i pattern **già scritti e testati** è `reference-page-full.tsx` in questa stessa cartella. Apri quel file e usalo come "libreria di sezioni" da cui COPIARE il codice esatto, sostituendo solo il copy/contenuti con quelli del sito source.

## Mapping sezioni source → Pattern Empire

Quando classifichi le sezioni del sito source, consulta questa tabella. Ogni pattern ha: bg alternato, max-w, struttura, componenti chiave. Linee = `reference-page-full.tsx:NN`.

| Pattern ID | Sezione riferimento | bg | Linee | Usalo per |
|---|---|---|---|---|
| `hero-dark-chips` | HERO | bg-ink | 25-88 | Homepage hero, header principale di ogni pagina |
| `stats-3-cards-silver` | STATS 3 blocchi | bg-ink | 90-110 | Numeri, metriche, risultati, "247+ call fatte" |
| `focus-prose-dark` | ASCOLTA BENE | bg-ink | 112-136 | Manifesto, dichiarazione, testo denso emotivo |
| `problem-solution-split-paper` | PROBLEMA | bg-paper | 138-180 | Prima/dopo, corso tipico vs questa offerta, before/after |
| `metodo-steps-paper` | METODO | bg-paper | 182-211 | Come funziona, processo, metodologia, step numerati |
| `is-for-dual-dark` | PER CHI È / NON È | bg-ink | 213-256 | Target audience, qualifica/disqualifica |
| `timeline-paper` | TIMELINE dopo prenoti | bg-paper | 258-289 | Cosa succede dopo, roadmap, timeline temporale |
| `trasparenza-callout-dark` | TRASPARENZA (carte scoperte) | bg-ink | (vedi file) | Sezioni di onestà, disclaimer, "perché gratis" |
| `value-stack-card` | VALUE STACK | bg-grey/bg-ink | (vedi file) | Pricing, cosa include, calcolo valore |
| `chi-sono-split` | CHI SONO | bg-ink | (vedi file) | About, founder, team intro |
| `cosa-esci-con-grid` | COSA ESCI CON | bg-grey | (vedi file) | Deliverable, benefici tangibili, outcome |
| `testimonials-3-paper` | TESTIMONIAL | bg-paper | (vedi file) | Social proof, quote clienti |
| `case-study-3col-paper` | CASE STUDY | bg-paper | (vedi file) | Before/In call/After, transformation stories |
| `faq-list-paper` | FAQ | bg-paper | (vedi file) | Domande frequenti, obiezioni |
| `garanzia-callout-dark` | GARANZIA / OBIEZIONE | bg-ink con corner-brackets | (vedi file) | Rischio zero, unica obiezione gestita |
| `cta-final-bracketed-dark` | CTA FINALE | bg-ink-2 | (vedi file) | Chiusura, ultima CTA forte |
| `footer-ink-2` | FOOTER | bg-ink-2 | (vedi file) | Footer minimale |

## Mapping semantico — da input source a pattern

Quando vedi una sezione nel source che dice…

- "Chi siamo / About us" → `chi-sono-split`
- "I nostri servizi / Features / Benefits" → `metodo-steps-paper` (se 3-5 step) o `cosa-esci-con-grid` (se 3-6 benefit)
- "Come funziona / How it works / Process" → `metodo-steps-paper` o `timeline-paper`
- "Testimonianze / Reviews" → `testimonials-3-paper`
- "FAQ / Domande" → `faq-list-paper`
- "Prezzi / Pricing / Piani" → `value-stack-card` (adatta, no APSOC-specific)
- "Contatti / Book now / Prenota" → `cta-final-bracketed-dark`
- "Numeri / Stats / Metrics" → `stats-3-cards-silver`
- "Perché noi / Why us" → `problem-solution-split-paper` o `focus-prose-dark`
- Sezione non mappabile chiaramente → scegli il pattern per bg alternato + card-paper se chiara/grid, card-dark se densa/dark. Usa sempre Reveal + bubble eyebrow + h2 silver-mixed.

## REGOLE DI ALTERNANZA BG

Ordine tipico delle sezioni (puoi saltare o riordinare, ma MAI due bg uguali consecutivi):

```
bg-ink (hero) → bg-ink (stats se c'è) → bg-ink (prose focus) → bg-paper (problema) → bg-paper (metodo) → bg-ink (is-for) → bg-paper (timeline) → bg-ink (trasparenza) → bg-grey (value stack) → bg-ink (chi sono) → bg-grey (cosa esci con) → bg-paper (testimonials) → bg-paper (case study) → bg-ink (garanzia) → bg-paper (faq) → bg-ink-2 (cta finale) → bg-ink-2 (footer)
```

Se il source ha meno sezioni, contrai. Se ne ha di più, riusa lo schema alternato.

## MICROPATTERN OBBLIGATORI

### Hero (OGNI homepage/landing DEVE avere)
- `<section className="bg-ink relative overflow-hidden">`
- Marquee border-b (12 ripetizioni di 4 testi + ✦ arancione)
- 4 silver-chip flottanti (top-left, top-right, bottom-left, bottom-right)
- `bubble-orange` con icona Sparkles → eyebrow "Posti limitati" o equivalente
- `pre-headline` tag maiuscolo (es. "Brand presenta · <Titolo>")
- H1 diviso in 2 span: `text-silver-white` + `text-silver-orange`
- Subtitle con `<strong className="text-silver-orange font-semibold">` sui concetti chiave e UN `hl-block` su UNA frase
- CTA large + Shield icon "Nessuna carta · Nessun impegno"

### Ogni H2
- Pattern: `<span className="text-silver-black">riga 1</span><br/><span className="text-orange-pure italic font-medium">riga 2.</span>` su paper/grey
- Pattern: `<span className="text-silver-white">riga 1</span><br/><span className="text-orange-pure italic">riga 2.</span>` su dark

### Ogni bubble eyebrow
- Sezioni dark → `bubble-ink` o `bubble-orange`
- Sezioni paper → `bubble-orange` o `bubble-silver`

### Ogni card lista
- su paper → `card-paper` con icone lucide-react `Check`/`X`/`ArrowRight`
- su dark → `card-dark` con icone lucide-react
- `card-orange` per il "dopo/vincente" nei confronti problema-soluzione
- `card-silver-orange` per offerte premium isolate

### Ogni step numerato
- `<div className="step-num shrink-0">{i + 1}</div>` in flex con contenuto

### Ogni sezione non-hero
- Deve avere `section section-border-t` come classi oltre al bg
- Wrapper `<Reveal>` su h2, bubble, e sui figli principali con delay crescenti

## COMPONENTE CTA (sempre uguale, da mettere in cima a `page.tsx`)

```tsx
function CTA({ large = false, label = "<CTA label del source>" }: { large?: boolean; label?: string }) {
  return (
    <a href={BOOKING_URL} className={`btn-orange ${large ? "btn-orange--lg" : ""} group`}>
      {label}
      <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
    </a>
  );
}
```

E `const BOOKING_URL = "<link del source>"` in alto.

## ASSET HANDLING

- Immagini del source → copiale in `public/` mantenendo nomi.
- Se mancano → usa placeholder grafici: icone lucide-react + card-silver-orange/card-paper.
- Non inventare MAI URL di immagini esterne.
- Background image → sostituisci con pattern Empire (`bg-ink` + `grain-fine` + silver-chip) salvo che il source abbia immagine fotografica esplicita rilevante.

## COSA NON FARE

- Mai pulsanti che non siano `btn-orange` o `btn-ghost`
- Mai grid con più di 3 colonne su desktop (Empire è respirato)
- Mai font diverso da Onest
- Mai gradient generici stile "blue-500 to-purple-500" — solo i 3 silver-mixed + orange gradient
- Mai card con `bg-white` flat senza `card-paper` (mancano shadow/border)
- Mai rimuovere grain-fine "perché disturba"
- Mai shadcn components inline — usa solo le classi CSS raw di `design-tokens.css`

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
