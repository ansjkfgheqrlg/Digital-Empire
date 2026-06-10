# QA-PERFORMANCE
            
> Path: [[Map - Crea_Siti|Crea siti > Siti CCM]]

## Content

# QA-PERFORMANCE — Claude Code Mastery Landing Page
**Analisi:** 2026-04-07
**File analizzati:** `index.html`, `thank-you.html`
**Metodo:** Static code analysis (nessun tool di misurazione live)

---

## Performance — index.html: 74/100 | thank-you.html: 83/100

Score composito medio: **78/100**

Detrazione applicata:
- 1x High (-8): Google Fonts render-blocking senza async pattern
- 1x High (-8): grain animation su pseudo-elemento 200% viewport senza `will-change`
- 1x Medium (-3): `backdrop-filter: blur(20px)` su elementi above-the-fold
- 1x Medium (-3): LCP text-based con font esterno (dipendenza dalla rete per il contenuto principale)
- 1x Medium (-3): `setTimeout` artificiale di 1000ms prima del redirect (index.html)
- 1x Low (-1): `console.log` lasciato in produzione (index.html)

---

## Core Web Vitals Estimate

| Metrica | Rischio | Target | Note |
|---|---|---|---|
| LCP | Medio | < 2.5s | LCP candidate e' il testo h1. Dipende da quando Inter viene renderizzato: se il font e' in cache o la CDN risponde veloce, < 1.5s; se Google Fonts e' lento (cold load), potenzialmente 2-3s |
| CLS | Basso | < 0.1 | Nessuna immagine. Font con `display=swap` nell'URL Google. Le animazioni `fadeUp` usano solo `opacity` e `transform` — nessun layout shift. Rischio residuo minimo dalla promozione di layer con `backdrop-filter` |
| INP | Basso | < 200ms | JS minimo (index.html). Solo un event listener su submit. Nessun scroll/resize listener. Nessun calcolo pesante sul main thread |

---

## Issue

### Critical

Nessun issue Critical rilevato.

---

### High

| # | File | Problema | Impatto stimato | Fix |
|---|---|---|---|---|
| H1 | entrambi | **Google Fonts caricato come `<link rel="stylesheet">` sincrono nell'head** senza pattern async (`media="print"` + `onload`) | Blocca il rendering fino al completamento del download del CSS da fonts.googleapis.com. Su connessione lenta o cold start, ritarda il First Contentful Paint di 200-600ms stimati. Il `preconnect` aiuta ma non elimina il blocco | Sostituire con il pattern async: `<link rel="stylesheet" href="..." media="print" onload="this.media='all'">` piu' un `<noscript>` fallback. In alternativa: self-hosting del font Inter via `@font-face` locale |
| H2 | entrambi | **`body::after` (grain animation) opera su un pseudo-elemento 200%x200% del viewport senza `will-change: transform`** | Il browser deve gestire una paint area di 4x il viewport a ogni step dell'animazione `steps(10)`. Senza `will-change`, il browser potrebbe non promuovere il layer in anticipo, causando re-paint periodici. Su mobile con GPU debole e' il principale candidato a frame drops (INP/jank percepito) | Aggiungere `will-change: transform` al `body::after`. Considerare di ridurre il pseudo-elemento a `110% x 110%` con translate max del 5% — l'effetto grain e' visivamente identico ma il footprint di memoria GPU scende drasticamente |

---

### Medium

| # | File | Problema | Impatto stimato | Fix |
|---|---|---|---|---|
| M1 | entrambi | **`backdrop-filter: blur(20px)` su `.form-wrapper` e `.steps`** | Forza la promozione di un compositing layer e richiede un blur pass GPU su ogni frame in cui l'elemento e' visibile. Su Safari mobile e dispositivi low-end puo' ridurre il frame rate a 30fps durante le animazioni di entrata (`fadeUp`) | Ridurre a `blur(8px)` o rimuovere: l'effetto visivo e' quasi identico dato lo sfondo quasi opaco. Alternativa: usare `background: rgba(255,255,255,0.04)` solido senza blur |
| M2 | index.html | **LCP dipende da font web esterno (Inter) senza fallback visivamente equivalente** | Se Inter non carica (timeout Google Fonts, offline, ecc.), il browser usa `-apple-system` / `BlinkMacSystemFont` che ha metriche diverse: possibile piccolo CLS al FOUT anche con `display=swap` | Aggiungere `size-adjust`, `ascent-override`, `descent-override` nel fallback `@font-face` per far corrispondere le metriche di Inter a quelle del font di sistema. Oppure self-hosting |
| M3 | index.html | **`setTimeout(1000ms)` prima del redirect a `thank-you.html`** | Aggiunge 1 secondo artificiale alla navigazione post-submit senza valore funzionale (il codice non esegue operazioni asincrone reali in quel secondo — la logica e' tutta sincrona prima del timeout) | Rimuovere il timeout: eseguire `window.location.href = 'thank-you.html'` direttamente dopo la validazione, oppure usarlo solo come feedback visivo minimo (200ms) |

---

### Low

| # | File | Problema | Impatto stimato | Fix |
|---|---|---|---|---|
| L1 | index.html | **`console.log('Opt-in:', { nome, email })` a riga 539 in produzione** | Nessun impatto performance misurabile. Espone dati utente (nome, email) nella console del browser — problema di data privacy piu' che di performance | Rimuovere prima del deploy su dominio pubblico |
| L2 | entrambi | **CSS inline non minificato** | I `<style>` tag di index.html pesano circa 7.5KB non compressi, thank-you.html circa 5.5KB. Gzip/Brotis sul server ridurra' a ~2KB ciascuno automaticamente, quindi l'impatto reale e' basso | Accettabile per single-file deployment. Se si volesse ottimizzare: minificare rimuove ~15-20% del peso non compresso |
| L3 | entrambi | **`body::before` (grain statico) ha `background-size: 200px` con SVG `feTurbulence` inline come data URI** | Il browser decodifica il data URI SVG e applica il filtro feTurbulence a ogni tile. Non e' animato, quindi avviene una volta sola. Impatto trascurabile su desktop; su mobile very low-end potrebbe aggiungere 5-10ms al primo paint | Accettabile. Se si cercasse il massimo: pre-renderizzare il grain come PNG base64 tiny e usarlo come background-image |

---

## Analisi Dettagliata per Area

### Critical Rendering Path

**index.html:**
```
<head>
  preconnect fonts.googleapis.com      [OK — riduce DNS+TCP latency]
  preconnect fonts.gstatic.com         [OK — riduce latency download font]
  <link rel="stylesheet" href="fonts.googleapis.com/...display=swap">  [BLOCCO]
  <style> ~7.5KB CSS inline </style>   [OK — no extra request]
</head>
<body>
  ...contenuto...
  <script> inline JS ~600 bytes </script>  [OK — fine body, non blocca rendering]
</body>
```

Il singolo punto di blocco e' Google Fonts. Il browser non puo' procedere al rendering finche' non ha scaricato il CSS da `fonts.googleapis.com` (che poi referenzia i file `.woff2` da `fonts.gstatic.com`). Con `preconnect` il handshake e' gia' aperto, quindi il costo aggiuntivo e' solo il trasferimento del CSS (~1-2KB) e poi il file Inter (~17KB per i pesi 300/400/500/600/700 in subset latino). Con `display=swap`, il testo viene mostrato con il fallback immediatamente e Inter sostituisce al caricamento — questo previene il FOIT ma puo' causare un micro-reflow visibile.

**thank-you.html:**
Identico pattern Google Fonts. Nessun JS — clean.

---

### Analisi Animazioni

**`grain` (body::after) — ATTENZIONE**

```css
body::after {
  width: 200%;
  height: 200%;
  /* area = 4x viewport */
  animation: grain 8s steps(10) infinite;
}
```

L'elemento copre 4 volte l'area del viewport. La funzione `steps(10)` significa 10 discrete posizioni ogni 8 secondi — il browser calcola una nuova composizione ogni 800ms. Poiche' l'animazione usa solo `transform: translate()`, si qualifica per compositing sul thread GPU separato (compositor thread) senza coinvolgere il main thread. Questo e' corretto e sicuro per l'INP.

Il rischio e' sulla **memoria GPU**: un pseudo-elemento 200%x200% su un viewport 390px mobile = ~608,000px di area da tenere in texture. Su dispositivi con < 2GB RAM e GPU integrata, potrebbe aumentare la pressione sulla memoria grafica. L'aggiunta di `will-change: transform` risolve promuovendo il layer in anticipo invece che al primo frame dell'animazione.

**`fadeUp` (hero e content) — OK**

```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

Usa solo `opacity` e `transform` — entrambe proprieta' gestite dal compositor senza layout/paint. Gli staggered delays (0.15s, 0.25s, 0.35s...) sono un pattern consolidato e non introducono layout thrashing. La durata 800ms con cubic-bezier `(0.16, 1, 0.3, 1)` e' nella norma.

---

### Immagini

Nessuna immagine raster (`<img>`) in nessuno dei due file. Tutto il visual e' realizzato con:
- CSS gradients (bg-glow, accents)
- SVG inline (checkmark icons, shield icon)
- SVG data URI (grain texture)
- CSS shapes (logo-icon, check boxes)

Questo elimina completamente i rischi LCP da immagini non ottimizzate, `fetchpriority` mancante, dimensioni non dichiarate e formati non-WebP. E' una scelta progettuale eccellente per una landing page opt-in.

**LCP candidate effettivo:** Il testo `h1` e' il Largest Contentful Paint candidate. Il browser lo puo' misurare solo dopo che Inter e' disponibile (o dopo che `display=swap` ha mostrato il fallback). In pratica, l'LCP misurato da Chrome sara' il momento in cui h1 appare con il font di sistema (fallback) — potenzialmente molto veloce (< 1s) — ma il "visual completeness" percepito arriva quando Inter carica.

---

### JavaScript

**index.html** — unico script, inline, fine body:
- IIFE (immediately invoked) — non polluta il global scope: bene
- Event listener su `submit`: singolo, nessun problema
- Validazione sincrona inline: nessun impatto performance
- `console.log` espone dati utente
- `setTimeout(1000)` aggiunge latenza artificiale
- Nessun `fetch` o chiamata XHR — il form non invia dati a un endpoint reale nel codice attuale (solo redirect locale)

**thank-you.html** — zero JavaScript. Ottimo.

---

## Ottimizzazioni Consigliate Post-Deploy

### Priorita' Alta (impatto diretto sul LCP misurabile)

1. **Async Google Fonts** — Sostituire il caricamento sincrono con:
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'">
   <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"></noscript>
   ```
   Questo carica il font in modo non bloccante. Il FCP migliorera' di 200-600ms su cold load.

2. **`will-change: transform` sul grain animato** — Aggiungere a `body::after`:
   ```css
   body::after {
     will-change: transform;
     /* resto invariato */
   }
   ```

### Priorita' Media

3. **Ridurre `backdrop-filter: blur(20px)` a `blur(6px)`** — Visivamente quasi identico, costo GPU ridotto del ~70%.

4. **Rimuovere `setTimeout(1000ms)`** in index.html — Il redirect deve avvenire appena la validazione passa, non dopo un secondo.

5. **Self-hosting Inter** — Scaricare i file `.woff2` e servirli localmente elimina la dipendenza da Google Fonts CDN e permette `font-display: swap` via `@font-face` locale con `size-adjust` per CLS zero.

### Priorita' Bassa

6. **Rimuovere `console.log`** prima del deploy pubblico (privacy dato email/nome utente).

7. **Configurare headers di cache** — Se deployato su Vercel o Netlify, aggiungere regole di cache per i file statici. Per single-page HTML il beneficio e' limitato, ma utile per risorse future.

8. **Ridurre l'area del pseudo-elemento grain** — Da `200%x200%` a `120%x120%` con offset massimo ridotto da `35%` a `15%`: l'effetto grain e' percettivamente identico, la texture GPU scende da 4x a 1.44x il viewport.

---

## Riepilogo Scoring

| File | Punteggio | Limitazione principale |
|---|---|---|
| index.html | 74/100 | Google Fonts sincrono + grain senza will-change + backdrop-filter + setTimeout |
| thank-you.html | 83/100 | Google Fonts sincrono + grain senza will-change + backdrop-filter |

Le due pagine sono architetturalmente sane (nessuna immagine, JS minimo, animazioni compositor-safe). I fix High-priority sono tutti applicabili in meno di 30 minuti di lavoro e porterebbero entrambi i file vicino a 95/100.

## Collegamenti Correlati
- [[Knowledge_Base/Stubs/headers|headers]]
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
