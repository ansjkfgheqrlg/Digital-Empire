# QA-MOBILE
            
> Path: [[Map - Crea_Siti|Crea siti > Siti CCM]]

## Content

# QA Mobile & Cross-Browser — Claude Code Mastery Landing Page

**Data analisi:** 2026-04-07
**File analizzati:** `index.html`, `thank-you.html`
**Metodologia:** Analisi statica del codice (HTML + CSS inline)

---

## Mobile & Cross-Browser — 81/100

**Issue trovate:** 6 (Critical: 0 | High: 1 | Medium: 3 | Low: 2)

---

### Issue

| Severity | File | Problema | Fix |
|---|---|---|---|
| High | index.html | `#optinForm input` ha `font-size: 0.9375rem` (15px con root 16px) — iOS Safari fa zoom automatico su qualsiasi input con font-size < 16px; l'utente mobile vede la pagina scattare e zoomarsi al tap sul campo | Imposta `font-size: 1rem` (16px) sugli input. Il design non cambia visivamente in modo apprezzabile, ma blocca il comportamento di zoom involontario |
| Medium | index.html, thank-you.html | `backdrop-filter: blur(20px)` su `.form-wrapper` e `.steps` non ha il prefisso `-webkit-backdrop-filter` — su iOS Safari < 15.4 e su alcuni browser Chromium su Android l'effetto glass scompare silenziosamente | Aggiungi `-webkit-backdrop-filter: blur(20px)` prima della proprietà standard. Pattern: `-webkit-backdrop-filter: blur(20px); backdrop-filter: blur(20px);` |
| Medium | thank-you.html | `body { min-height: 100vh; display: flex; }` + `main { flex: 1; }` crea il centramento verticale dei contenuti basandosi su `100vh`. Su iOS Safari la barra dell'indirizzo riduce l'altezza reale della viewport: il contenuto potrebbe non risultare perfettamente centrato o mostrare uno scrollbar indesiderato | Sostituisci `min-height: 100vh` con `min-height: 100dvh` (dynamic viewport height) con fallback: `min-height: 100vh; min-height: 100dvh;` — i browser che non supportano `dvh` useranno il valore precedente |
| Medium | index.html, thank-you.html | Nessun uso di `env(safe-area-inset-bottom)` nel padding del footer — su iPhone con home indicator (iPhone X in poi) il footer `padding-bottom: 2.5rem` potrebbe non essere sufficiente su alcuni orientamenti o potrebbe risultare tagliato dietro la barra gesturale | Aggiungi al footer: `padding-bottom: calc(2.5rem + env(safe-area-inset-bottom, 0px))` — il fallback a `0px` garantisce nessun impatto su browser che non supportano la variabile |
| Low | index.html, thank-you.html | `body::after` ha un'animazione `grain` continua (8s loop, `steps(10)`) su un elemento `200% x 200%` con `position: fixed`. Su dispositivi mobile di fascia bassa e su Android con risparmio energetico attivo, animazioni CSS su pseudo-elementi di grandi dimensioni possono causare jank e drenaggio della batteria | Valuta di disabilitare l'animazione con `@media (prefers-reduced-motion: reduce)` o di usare un approccio con canvas/WebGL solo se la performance viene confermata problematica nei test reali |
| Low | index.html, thank-you.html | SVG `feTurbulence` usato come data URI in `background-image` per l'effetto grain — su alcune versioni di Android WebView (< Chromium 85) e su Firefox per Android datato, i filtri SVG inline in data URI possono non essere renderizzati. L'effetto è puramente decorativo (opacity 0.035) quindi il fallback è graceful, ma vale la pena documentarlo | Nessuna azione necessaria. Il degradamento è silenzioso e non impatta l'usabilità. Annotare nel brief tecnico per future manutenzioni |

---

### Elementi Corretti

- Meta viewport `width=device-width, initial-scale=1.0` presente e corretto in entrambi i file; nessun `user-scalable=no`
- Nessuna larghezza fissa pericolosa: tutti i contenitori usano `max-width` (600px, 540px) senza `width` assoluta, nessun overflow orizzontale atteso
- CTA button (`padding: 1rem 2rem`, font 15px) produce un touch target di circa 52-54px di altezza — superiore alla soglia minima di 44px (Apple HIG)
- Input fields (`padding: 0.9375rem 1.125rem`) producono touch target di circa 52px — adeguato; il problema e' solo il font-size (vedi issue High sopra)
- Media query presenti in entrambi i file: `@media (min-width: 640px)` in entrambi, `@media (min-width: 768px)` aggiuntivo in index.html
- Nessun pattern hover-only che nasconde contenuto: tutti gli `:hover` sono puramente decorativi (colore, ombra, translateY)
- `background-clip: text` usato correttamente con doppia dichiarazione: `-webkit-background-clip: text` + `background-clip: text` + `-webkit-text-fill-color: transparent`
- `position: fixed` su `body::before`, `body::after` e `.bg-glow` senza `overflow: scroll` — nessun rischio del bug iOS di scroll bloccato
- Layout completamente fluid: flexbox con `flex-direction: column`, gap e padding in `rem` — nessun elemento rigido che causa overflow
- `font-size` del body text (0.9375rem = 15px) e dei bullets accettabile per la lettura su mobile; il problema e' limitato agli input del form
- Spaziatura tra elementi touch adeguata: i bullets usano `gap: 1.125rem`, il form usa `gap: 0.75rem` tra input
- CSS features usate (`linear-gradient`, `radial-gradient`, `backdrop-filter`, `flexbox`, `CSS animations`) tutte supportate universalmente su browser moderni (Chrome 80+, Firefox 79+, Safari 14+, Edge 80+)
- Nessun CSS custom property (`var()`) — nessun problema di compatibilita' con browser legacy
- Nessun JavaScript con API moderne problematiche: il form JS usa `var`, `function`, `setTimeout`, `window.location.href` — massima compatibilita' cross-browser
- `prefers-reduced-motion` non gestito per `fadeUp` animations — non critico ma da considerare per accessibilita' (fuori scope mobile, rilevante per a11y audit)

---

### Note Cross-Browser per CSS Features Specifiche

**`backdrop-filter`**
Support: Chrome 76+, Edge 79+, Firefox 103+, Safari 9+ (con prefisso `-webkit-`), iOS Safari 9+ (con prefisso).
Il mancato prefisso causa la perdita dell'effetto glass su iOS Safari < 15.4 senza prefisso. Il card rimane visibile grazie al `background: rgba(255,255,255,0.015)` ma appare piatto. Aggiungere il prefisso e' un fix di 1 riga senza rischi.

**`background-clip: text`**
Gia' correttamente gestito con doppio prefisso. Nessuna azione.

**SVG `feTurbulence` in data URI**
Decorativo e graceful-degrading. Support universale su browser moderni. Nessuna azione.

**`min-height: 100dvh`**
Support: Chrome 108+, Firefox 101+, Safari 15.4+. Il pattern di fallback `min-height: 100vh; min-height: 100dvh;` e' lo standard raccomandato — browser che non supportano `dvh` ignorano la seconda dichiarazione e usano la prima.

---

### Test Manuali Raccomandati Post-Deploy

- [ ] Chrome DevTools: emula iPhone 14 (390px) e iPhone SE (375px) — verificare che il tap sul campo nome non causi zoom (richiede fix font-size)
- [ ] Chrome DevTools: emula Samsung Galaxy S21 (360px) — verificare che il form sia completamente visibile senza scroll orizzontale
- [ ] Chrome DevTools: emula iPad (768px) — verificare che il layout a colonna singola resti leggibile e non mostri spazi vuoti eccessivi
- [ ] Firefox Responsive Design Mode a 375px — verificare il centramento verticale della thank-you page con e senza barra degli strumenti
- [ ] Safari su iPhone reale (iOS 15+): testare il tap su entrambi gli input e verificare l'assenza di zoom (dopo fix) e la fluidita' dello scroll
- [ ] Safari su iPhone reale: verificare che il footer non sia tagliato dalla home bar su iPhone senza tasto fisico
- [ ] Test con `prefers-reduced-motion: reduce` attivo (impostazioni accessibilita' iOS/Android) — verificare che la grain animation si fermi dopo il fix consigliato
- [ ] Lighthouse audit modalita' Mobile (Performance + Accessibility) — attenzione al score Performance per la grain animation continua
- [ ] Test tap con dito vero sul CTA button su un dispositivo Android reale a 360px — verificare che il bottone risponda al primo tap senza miss-tap
- [ ] Verifica orientamento landscape su iPhone SE (568px larghezza) — il form deve rimanere usabile senza scroll eccessivo

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
