# Leandignpage-prompt

> Source: File system (`Lancio corso skill beast\Leanding Page CCM\CONTESTO\Leandignpage-prompt.md`)
> Collected: 2026-05-06
> Published: Unknown

Crea una landing page di opt-in in un singolo file HTML.

DESIGN:
- Mobile-first, responsive
- Sfondo: gradiente scuro (#0f172a a #1e293b)
- Font: system fonts (Inter se disponibile, altrimenti sans-serif)
- Colore accento: #3b82f6 (blu elettrico)

STRUTTURA HTML:

<header>
  - Logo/Nome: "Claude Code Mastery"
  - Tagline piccola sopra headline
</header>

<main>
  HERO SECTION:
  - Tagline: "Il primo percorso italiano completo su Claude Code"
  - Headline H1: "Il Framework I.C.R.O. — il metodo in 1 pagina che trasforma Claude Code nel tuo collaboratore perfetto"
  - Sub-headline: "12 pagine. 1 framework. 1 template pronto. Gratis."
  
  4 BULLET:
  - Il framework I.C.R.O. in 4 step — la struttura esatta per dare istruzioni che producono output prevedibili
  - 1 template CLAUDE.md compilabile — lo compili in 10 minuti
  - Per chi usa l'AI ma non sa come andare oltre "copia-incolla da ChatGPT"
  - Zero codice richiesto, applicabile dal primo minuto
  
  FORM:
  <form id="optinForm">
    <input type="text" name="nome" placeholder="Nome" required>
    <input type="email" name="email" placeholder="Email" required>
    <button type="submit">Scarica il Framework — Gratis</button>
  </form>
  
  SOTTO FORM:
  <p class="privacy">Niente spam. Cancellati quando vuoi.</p>
</main>

<footer>
  - © 2026 Digital Empire
</footer>

STILE CSS (inline nel <style>):
- Header centrato, padding 2rem
- Hero section: max-width 600px, centrato, padding 3rem 1.5rem
- Headline: font-size 2rem (mobile) / 2.5rem (desktop), font-weight bold, line-height 1.2
- Sub: font-size 1.125rem, colore grigio chiaro
- Bullet: icona check (✓) prima di ogni punto, padding, font-size 1rem
- Form: stack verticale, gap 1rem
- Input: padding 1rem, border-radius 0.5rem, background scuro, testo bianco, border 1px grigio
- Button: background #3b82f6, padding 1rem 2rem, font-weight bold, border-radius 0.5rem, cursor pointer, hover effect
- Privacy: font-size 0.875rem, colore grigio, text-align center

JAVASCRIPT:
- Quando il form viene submitted:
  1. event.preventDefault()
  2. Mostra messaggio "Controllo in corso..."
  3. Simula invio (per ora solo console.log dei dati)
  4. Dopo 1 secondo: redirect a pagina "thank-you.html"

OUTPUT:
- 1 file: index.html
- Tutto inline (CSS e JS dentro l'HTML)
- Pronto per deploy
