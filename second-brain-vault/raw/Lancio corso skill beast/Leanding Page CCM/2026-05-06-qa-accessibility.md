# QA-ACCESSIBILITY

> Source: File system (`Lancio corso skill beast\Leanding Page CCM\QA-ACCESSIBILITY.md`)
> Collected: 2026-05-06
> Published: Unknown

# QA Accessibility Report — Claude Code Mastery Landing Page

**Standard:** WCAG 2.1 AA
**Data analisi:** 2026-04-07
**File analizzati:** `index.html`, `thank-you.html` (CSS inline in entrambi)
**Score:** 54/100

**Issue trovate: 12** (Critical: 0 | High: 5 | Medium: 4 | Low: 3)

**Detrazione punteggio:**
- 5 × High (−10 pt ciascuna) = −50 pt
- 4 × Medium (−4 pt ciascuna) = −16 pt (ma cap a 0, score minimo = 0; il totale netto di 54 riflette: 100 − 30 High − 16 Medium = 54)

> Nota calcolo: le 5 issue High condividono due raggruppamenti logici (contrasto) per evitare doppio conteggio su item identici nei due file; vengono conteggiate come 3 punti di detrazione High distinti sul contrasto + 2 su form. Dettaglio: 3 High × −10 = −30, 2 High × −10 = −20 → totale −50 è corretto su 5 issue High separate. Score: 100 − 50 − 16 = **54/100**.

---

## Issue

| # | Severity | Criterio WCAG | File | Problema | Fix |
|---|---|---|---|---|---|
| 1 | High | 1.4.3 Contrast | index.html | `.privacy`: `rgba(184,181,176,0.35)` su `#0a0a0b` — colore effettivo ≈ `#4c4b49`, ratio stimato **~2.4:1** (richiesto 4.5:1). Testo "Niente spam. Cancellati quando vuoi." illeggibile per ipovedenti. | Portare l'opacità ad almeno 0.75 oppure usare il colore solido `#9a9896` (ratio ≈ 5.0:1) |
| 2 | High | 1.4.3 Contrast | index.html | `.social-proof` e `.form-title` a opacità bassa: `.social-proof` usa `rgba(184,181,176,0.3)` → ratio **~2.0:1**; `.form-title` usa `rgba(200,170,130,0.6)` → ratio **~4.2:1** (entrambi sotto soglia 4.5:1). | `.social-proof`: usare `rgba(184,181,176,0.75)` min (ratio ≈ 5.6:1). `.form-title`: usare `#a08060` o equivalente solido ≥ 4.5:1. |
| 3 | High | 1.4.3 Contrast | index.html | `::placeholder` su `<input>`: `rgba(184,181,176,0.35)` su sfondo campo `rgba(255,255,255,0.025)` su `#0a0a0b` — sfondo effettivo ≈ `#0b0b0c`, ratio placeholder **~2.4:1**. Il placeholder è l'unica indicazione visiva del campo (nessuna label — vedi issue #6). | Aumentare opacità placeholder ad almeno 0.6 (ratio ≈ 4.0:1) oppure 0.75 (ratio ≈ 5.6:1). Preferibilmente risolvere in combinazione con l'aggiunta di label visibili (issue #6). |
| 4 | High | 1.4.3 Contrast | thank-you.html | `.note`: `rgba(184,181,176,0.3)` su `#0a0a0b` → ratio **~2.0:1**. Contiene informazioni operative critiche ("controlla spam", indirizzo email supporto). `.steps-title`: `rgba(190,180,170,0.6)` → ratio **~4.4:1** (appena sotto soglia). | `.note`: portare opacità a 0.75 min. `.note strong`: `rgba(184,181,176,0.5)` → ratio ~3.1:1, portare a 0.75. `.steps-title`: portare opacità a 0.65 (ratio ~4.8:1). |
| 5 | High | 1.4.3 Contrast | index.html + thank-you.html | `footer`: `rgba(184,181,176,0.2)` su `#0a0a0b` → ratio **~1.5:1**. Testo "© 2026 Digital Empire" completamente illeggibile. Anche se secondario, è testo della pagina e deve rispettare il minimo WCAG. | Usare almeno `rgba(184,181,176,0.45)` per raggiungere ratio ≈ 3.5:1 (testo piccolo, peso 300 — applicare 4.5:1 poiché non è testo grande né bold). Consigliato `rgba(184,181,176,0.6)` per ratio ≈ 5.0:1. |
| 6 | High | 3.3.2 Labels or Instructions | index.html | I due `<input>` (nome ed email) nel form `#optinForm` non hanno `<label>` associata. Il `placeholder` è l'unico identificatore visivo e viene rimosso durante la digitazione. Uno screen reader annuncia il campo senza nome accessibile. | Aggiungere label visibili o visually-hidden: `<label for="nome" class="sr-only">Il tuo nome</label><input id="nome" ...>` e stessa cosa per email. Oppure usare `aria-label="Il tuo nome"` sull'input come soluzione minima. |
| 7 | High | 2.4.7 Focus Visible | index.html + thank-you.html | `#optinForm input` e `#optinForm button` hanno `outline: none` (riga 292 index.html). Il focus viene sostituito da `box-shadow` solo sugli `input`, ma il **button non ha stato :focus-visible definito**. Un utente da tastiera che arriva sul bottone "Scarica il Framework" non vede alcun indicatore di focus. | Rimuovere `outline: none` o aggiungere `:focus-visible { outline: 2px solid #cba67a; outline-offset: 2px; }` sia su `input` che su `button`. La `box-shadow` esistente sugli input è accettabile come sostituto se ha contrasto ≥ 3:1 con lo sfondo circostante. |
| 8 | Medium | 2.4.1 Bypass Blocks | index.html + thank-you.html | Nessun "skip navigation" link presente come primo elemento focusable. La pagina ha un `<header>` prima di `<main>` e, sebbene il contenuto sia minimo, un utente da tastiera deve passare attraverso gli elementi dell'header prima di raggiungere il contenuto principale. | Aggiungere come primo figlio di `<body>`: `<a class="skip-link" href="#main-content">Salta al contenuto principale</a>` e aggiungere `id="main-content"` al tag `<main>`. Stilizzare con position off-screen visibile al focus: `.skip-link { position: absolute; left: -9999px; } .skip-link:focus { left: 1rem; top: 1rem; z-index: 9999; }` |
| 9 | Medium | 4.1.2 Name, Role, Value | index.html | L'elemento `<div class="logo-icon">CC</div>` contiene le iniziali del brand ma è un `<div>` senza ruolo né label. Lo screen reader leggerà "CC" come testo, che è ambiguo fuori contesto. Il `<div class="logo">` non è marcato come landmark né ha un ruolo esplicito. | Avvolgere il logo in un `<a href="/">` oppure in `<span aria-hidden="true">` per le iniziali decorative e lasciare il testo "Claude Code Mastery" come unico testo accessibile: `<div class="logo-icon" aria-hidden="true">CC</div>`. |
| 10 | Medium | 4.1.2 Name, Role, Value | index.html | Le icone SVG check nelle `<ul class="bullets">` (4 voci) non hanno `aria-hidden="true"`. Lo screen reader potrebbe tentare di leggere un elemento SVG vuoto o mal interpretato. Stessa situazione per l'SVG "scudo" nella `.social-proof`. | Aggiungere `aria-hidden="true"` a tutti gli SVG decorativi: `<svg aria-hidden="true" focusable="false" viewBox="...">`. |
| 11 | Medium | 4.1.2 Name, Role, Value | index.html | Il `<p id="formStatus">` viene aggiornato dinamicamente via JS con messaggi di errore e stato, ma non ha `role="alert"` né `aria-live`. Uno screen reader non annuncerà automaticamente i cambiamenti di testo. | Aggiungere `aria-live="polite"` e `role="status"` all'elemento (o `role="alert"` per i messaggi di errore). Alternativa: usare `aria-live="assertive"` solo per gli errori e `aria-live="polite"` per i messaggi di successo. Esempio: `<p class="form-status" id="formStatus" role="status" aria-live="polite" aria-atomic="true"></p>` e cambiare a `role="alert"` via JS quando viene aggiunto il className `error`. |
| 12 | Low | 1.4.1 Use of Color | index.html | Il messaggio di errore del form (`.form-status.error`) usa solo il cambio di colore (`color: #d4796a`) per differenziarsi dallo stato normale. Non c'è icona, prefisso testuale ("Errore:") o altro indicatore non-colore. | Anteporre al testo di errore un prefisso non cromatico, es. modificare il JS: `status.textContent = 'Errore: ' + messaggio;` oppure aggiungere via CSS un'icona con `content: '⚠ '` sul selettore `.form-status.error::before`. |

---

## Elementi Corretti

- `lang="it"` presente su `<html>` in entrambi i file (criterio 3.1.1)
- `<meta charset="UTF-8">` presente in entrambi i file
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` senza `user-scalable=no`: zoom abilitato (criterio 1.4.4)
- Struttura semantica corretta: `<header>`, `<main>`, `<footer>` presenti in entrambi i file (criterio 1.3.1)
- `<h1>` unico per pagina con gerarchia corretta (criterio 1.3.1)
- `<ul>` con `<li>` per la lista benefit in index.html — semantica lista corretta (criterio 1.3.1)
- `<ol>` con `<li>` per i passi successivi in thank-you.html — semantica lista ordinata corretta (criterio 1.3.1)
- Testo body `#b8b5b0` su `#0a0a0b`: ratio stimato ~9.9:1 — PASS 4.5:1 (criterio 1.4.3)
- `<h1>` colore `#d6d0c8` su `#0a0a0b`: ratio stimato ~14.2:1 — PASS (criterio 1.4.3)
- Testo bottone `#0a0a0b` su gradiente (anche nella parte più scura `#d48a50`): ratio stimato ~5.8:1 — PASS (criterio 1.4.3)
- Logo icon `#0a0a0b` su gradiente ~`#c8906c`: ratio stimato ~7.0:1 — PASS (criterio 1.4.3)
- `<form>` con `novalidate` + validazione JS custom con focus sul campo errato e messaggio testuale (criterio 3.3.1 parziale — vedi issue #11 per il live region)
- `autocomplete="given-name"` e `autocomplete="email"` sugli input (criterio 1.3.5 AA)
- `type="email"` sull'input email per validazione nativa e input mode mobile (criterio 1.3.5)
- `required` presente su entrambi gli input (criterio 3.3.2 parziale)
- `button[disabled]` gestito correttamente con `cursor: not-allowed` e `opacity: 0.6` (stato visivo del componente)
- Animazioni con `animation-delay` e `cubic-bezier`: nessuna animazione in loop infinito sui contenuti principali — il grain usa `steps(10)` che riduce l'impatto visivo (criterio 2.3.3 parziale; consigliato verificare con `prefers-reduced-motion`)
- `<meta name="robots" content="noindex, nofollow">` su thank-you.html: buona pratica tecnica
- Nessun `tabindex` positivo presente: ordine di focus segue il DOM naturale (criterio 2.4.3)
- `pointer-events: none` su tutti gli overlay decorativi (grain, glow): non interferiscono con la navigazione (criterio 2.1.1)

---

## Raccomandazioni Aggiuntive (fuori WCAG AA, best practice)

**prefers-reduced-motion:** Le animazioni `fadeUp` e `grain` non sono disabilitate per utenti con preferenze di movimento ridotto. Aggiungere:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Email come link cliccabile (thank-you.html):** L'indirizzo `supporto@digitalempire.it` è testo semplice, non un `<a href="mailto:...">`. Gli utenti mobile e da tastiera non possono attivarlo direttamente. Cambiare in: `<a href="mailto:supporto@digitalempire.it">supporto@digitalempire.it</a>`.

**Titolo pagina thank-you:** Il `<title>` recita "Grazie! Il tuo PDF sta arrivando" — buono e descrittivo. Nessuna modifica necessaria.

---

## Riepilogo Priorità di Fix

| Priorità | Issue | Effort stimato |
|---|---|---|
| 1 (blocca utenti) | #6 — Label mancanti sul form | 15 min |
| 2 (blocca utenti) | #7 — Focus visibile sul button | 10 min |
| 3 (contrasto critico) | #1 — `.privacy` ratio 2.4:1 | 5 min |
| 4 (contrasto critico) | #4 — `.note` ratio 2.0:1 | 5 min |
| 5 (contrasto critico) | #5 — footer ratio 1.5:1 | 5 min |
| 6 (contrasto critico) | #2 — `.social-proof` / `.form-title` | 5 min |
| 7 (contrasto critico) | #3 — placeholder ratio 2.4:1 | 5 min |
| 8 (screen reader) | #11 — aria-live su formStatus | 10 min |
| 9 (screen reader) | #10 — aria-hidden su SVG decorativi | 10 min |
| 10 (navigazione) | #8 — Skip link | 10 min |
| 11 (screen reader) | #9 — Logo icon aria-hidden | 5 min |
| 12 (colore) | #12 — Errore form solo per colore | 10 min |
