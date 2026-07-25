# K07 — SECTION TEMPLATES (10 Template HTML Completi)

> Template pronti per ogni tipo di sezione. Tutti conformi a K00 (silver mixing), K01 (5 leggi), K02 (grain), K05 (lowercase+strong). Personalizza contenuto e palette.

---

## TEMPLATE 1 — HERO (dark, headline gradient, CTA gold)

```html
<section id="hero" style="position:relative;background:#020202;min-height:100vh;display:flex;align-items:center;overflow:hidden;">

  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.45;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <!-- DUST CANVAS -->
  <canvas id="dust-canvas" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2;"></canvas>

  <!-- CONTENT -->
  <div style="position:relative;z-index:20;max-width:900px;margin:0 auto;padding:120px 24px 80px;text-align:center;">

    <!-- Eyebrow label -->
    <p style="font-family:'Inter',sans-serif;font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#94A3B8;margin-bottom:24px;" class="reveal">
      [LABEL EYEBROW]
    </p>

    <!-- Headline -->
    <h1 style="font-family:'Cinzel',serif;font-size:clamp(2.5rem,6vw,5.5rem);font-weight:400;line-height:1.1;letter-spacing:-0.02em;background:linear-gradient(90deg,#94A3B8 0%,#E2E8F0 30%,#E3C878 50%,#FFFFFF 60%,#E3C878 70%,#CBD5E1 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;filter:drop-shadow(0px 4px 1px rgba(0,0,0,0.9));margin-bottom:24px;" class="reveal" data-delay="1">
      [HEADLINE PRINCIPALE]
    </h1>

    <!-- Subheadline -->
    <p style="font-size:1.125rem;font-weight:300;color:#94A3B8;max-width:600px;margin:0 auto 40px;line-height:1.7;" class="reveal" data-delay="2">
      [SUBHEADLINE] — <strong>[BENEFICIO CHIAVE]</strong> in [TIMEFRAME].
    </p>

    <!-- CTA Buttons -->
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;" class="reveal" data-delay="3">
      <button style="font-family:'Inter',sans-serif;font-size:0.875rem;font-weight:600;letter-spacing:0.08em;text-transform:lowercase;color:#020202;background:linear-gradient(135deg,#E3C878,#D4AF37);padding:16px 40px;border:none;border-radius:2px;cursor:pointer;transition:all 0.3s;box-shadow:0 4px 24px rgba(212,175,55,0.3);" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 32px rgba(212,175,55,0.5)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(212,175,55,0.3)'">
        [CTA PRINCIPALE]
      </button>
      <button style="font-family:'Inter',sans-serif;font-size:0.875rem;font-weight:600;letter-spacing:0.08em;text-transform:lowercase;color:#CBD5E1;background:transparent;padding:14px 38px;border:1px solid rgba(148,163,184,0.5);border-radius:2px;cursor:pointer;transition:all 0.3s;" onmouseover="this.style.borderColor='#E3C878';this.style.color='#E3C878'" onmouseout="this.style.borderColor='rgba(148,163,184,0.5)';this.style.color='#CBD5E1'">
        [CTA SECONDARIA]
      </button>
    </div>

    <!-- Social proof micro -->
    <p style="margin-top:32px;font-size:0.8125rem;color:#64748B;" class="reveal" data-delay="4">
      oltre <strong style="color:#94A3B8;">[NUMERO]</strong> [SOCIAL PROOF]
    </p>

  </div>
</section>
```

---

## TEMPLATE 2 — SOCIAL PROOF NUMBERS (dark, 3 numeri grandi)

```html
<section style="position:relative;background:#0a0a0a;padding:80px 0;overflow:hidden;">
  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.40;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:1000px;margin:0 auto;padding:0 24px;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px;text-align:center;">

      <div class="reveal">
        <div style="font-family:'Cinzel',serif;font-size:clamp(2.5rem,5vw,4rem);font-weight:600;background:linear-gradient(90deg,#E3C878,#FFFFFF,#E3C878);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
          <span class="counter" data-target="[NUM1]" data-suffix="[SUFFIX1]">0</span>
        </div>
        <p style="font-size:0.875rem;color:#64748B;margin-top:8px;text-transform:lowercase;"><strong style="color:#94A3B8;">[LABEL1]</strong></p>
      </div>

      <div class="reveal" data-delay="1">
        <div style="font-family:'Cinzel',serif;font-size:clamp(2.5rem,5vw,4rem);font-weight:600;background:linear-gradient(90deg,#E3C878,#FFFFFF,#E3C878);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
          <span class="counter" data-target="[NUM2]" data-suffix="[SUFFIX2]">0</span>
        </div>
        <p style="font-size:0.875rem;color:#64748B;margin-top:8px;text-transform:lowercase;"><strong style="color:#94A3B8;">[LABEL2]</strong></p>
      </div>

      <div class="reveal" data-delay="2">
        <div style="font-family:'Cinzel',serif;font-size:clamp(2.5rem,5vw,4rem);font-weight:600;background:linear-gradient(90deg,#E3C878,#FFFFFF,#E3C878);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
          <span class="counter" data-target="[NUM3]" data-suffix="[SUFFIX3]">0</span>
        </div>
        <p style="font-size:0.875rem;color:#64748B;margin-top:8px;text-transform:lowercase;"><strong style="color:#94A3B8;">[LABEL3]</strong></p>
      </div>

    </div>
  </div>
</section>
```

---

## TEMPLATE 3 — PROBLEMA (dark, testo emotivo)

```html
<section style="position:relative;background:#020202;padding:100px 0;overflow:hidden;">
  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.45;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:800px;margin:0 auto;padding:0 24px;text-align:center;">
    <p style="font-family:'Inter',sans-serif;font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#C0505A;margin-bottom:24px;" class="reveal">il problema</p>
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(2rem,4vw,3.5rem);font-weight:600;color:#E2E8F0;line-height:1.2;margin-bottom:32px;" class="reveal" data-delay="1">
      [HEADLINE PROBLEMA]
    </h2>
    <p style="font-size:1.0625rem;color:#94A3B8;line-height:1.8;margin-bottom:20px;" class="reveal" data-delay="2">
      [FRASE 1 PROBLEMA]. <strong>[PUNTO DOLENTE PRINCIPALE]</strong> che ti blocca ogni giorno.
    </p>
    <p style="font-size:1.0625rem;color:#94A3B8;line-height:1.8;" class="reveal" data-delay="3">
      [FRASE 2]. ma la verità è che <strong>[CAUSA REALE DEL PROBLEMA]</strong> — non è colpa tua.
    </p>
  </div>
</section>
```

---

## TEMPLATE 4 — SOLUZIONE / PATTERN INTERRUPT (light, beige argentato)

```html
<section style="position:relative;background:#DCD8CF;padding:100px 0;overflow:hidden;">
  <!-- GRAIN (light version) -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.35;mix-blend-mode:multiply;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.20;mix-blend-mode:multiply;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:800px;margin:0 auto;padding:0 24px;text-align:center;">
    <p style="font-family:'Inter',sans-serif;font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#4A9B7A;margin-bottom:24px;" class="reveal">la soluzione</p>
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(2rem,4vw,3.5rem);font-weight:600;color:#020202;line-height:1.2;margin-bottom:32px;" class="reveal" data-delay="1">
      [HEADLINE SOLUZIONE]
    </h2>
    <p style="font-size:1.0625rem;color:#374151;line-height:1.8;margin-bottom:20px;" class="reveal" data-delay="2">
      [DESCRIZIONE SOLUZIONE]. <strong>[NOME PRODOTTO/SISTEMA]</strong> è stato progettato per [TARGET] che vogliono [BENEFICIO].
    </p>
  </div>
</section>
```

---

## TEMPLATE 5 — 3-STEP PROCESS (dark, card con numero)

```html
<section style="position:relative;background:#020202;padding:100px 0;overflow:hidden;">
  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.45;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:1100px;margin:0 auto;padding:0 24px;">
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(2rem,4vw,3rem);color:#E2E8F0;text-align:center;margin-bottom:64px;" class="reveal">come funziona</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:32px;">

      <!-- Step card (ripeti per ogni step) -->
      <div class="reveal" data-delay="1" style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:4px;padding:40px 32px;transition:border-color 0.3s;" onmouseover="this.style.borderColor='rgba(227,200,120,0.3)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.06)'">
        <div style="font-family:'Cinzel',serif;font-size:3rem;font-weight:900;background:linear-gradient(90deg,#E3C878,#FFFFFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:16px;">01</div>
        <h3 style="font-family:'Cinzel',serif;font-size:1.25rem;color:#E2E8F0;margin-bottom:12px;">[TITOLO STEP 1]</h3>
        <p style="font-size:0.9375rem;color:#94A3B8;line-height:1.7;"><strong>[AZIONE CHIAVE]</strong> per [RISULTATO STEP].</p>
      </div>

      <!-- Ripeti per step 2 e 3 cambiando numero e contenuto -->

    </div>
  </div>
</section>
```

---

## TEMPLATE 6 — FEATURE GRID (dark, 2×3 cards)

```html
<section style="position:relative;background:#0a0a0a;padding:100px 0;overflow:hidden;">
  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.40;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:1200px;margin:0 auto;padding:0 24px;">
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(2rem,4vw,3rem);color:#E2E8F0;text-align:center;margin-bottom:16px;" class="reveal">[TITOLO SEZIONE]</h2>
    <p style="color:#64748B;text-align:center;max-width:500px;margin:0 auto 64px;" class="reveal" data-delay="1">[SOTTOTITOLO SEZIONE]</p>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;">
      <!-- Feature card (ripeti 6 volte) -->
      <div class="reveal" data-delay="1" style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:4px;padding:32px;transition:all 0.3s;" onmouseover="this.style.borderColor='rgba(227,200,120,0.25)';this.style.background='rgba(255,255,255,0.04)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.05)';this.style.background='rgba(255,255,255,0.02)'">
        <div style="font-size:1.75rem;margin-bottom:16px;">[ICONA EMOJI]</div>
        <h3 style="font-family:'Cinzel',serif;font-size:1rem;color:#E2E8F0;margin-bottom:10px;">[NOME FEATURE]</h3>
        <p style="font-size:0.875rem;color:#94A3B8;line-height:1.6;"><strong>[BENEFICIO]</strong> — [DESCRIZIONE].</p>
      </div>
    </div>
  </div>
</section>
```

---

## TEMPLATE 7 — TESTIMONIANZA (dark, card large)

```html
<section style="position:relative;background:#020202;padding:100px 0;overflow:hidden;">
  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.45;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:800px;margin:0 auto;padding:0 24px;">
    <div class="reveal" style="background:rgba(255,255,255,0.03);border:1px solid rgba(227,200,120,0.15);border-radius:4px;padding:48px;">
      <!-- Rating -->
      <div style="color:#E3C878;font-size:1.25rem;letter-spacing:4px;margin-bottom:24px;">★★★★★</div>
      <!-- Quote -->
      <blockquote style="font-family:'Playfair Display',serif;font-size:clamp(1.1rem,2vw,1.5rem);font-style:italic;color:#CBD5E1;line-height:1.6;margin-bottom:32px;">
        "[TESTO TESTIMONIANZA — emozione + risultato specifico + trasformazione]"
      </blockquote>
      <!-- Author -->
      <div style="display:flex;align-items:center;gap:16px;">
        <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#E3C878,#94A3B8);display:flex;align-items:center;justify-content:center;font-family:'Cinzel',serif;font-weight:700;color:#020202;">[INIZIALE]</div>
        <div>
          <div style="font-weight:600;color:#E2E8F0;font-size:0.9375rem;">[NOME COGNOME]</div>
          <div style="font-size:0.8125rem;color:#64748B;">[RUOLO / PROVENIENZA]</div>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## TEMPLATE 8 — CTA SECTION (colore dominante)

```html
<section style="position:relative;background:linear-gradient(135deg,[BG-INIZIO],[BG-FINE]);padding:120px 0;overflow:hidden;">
  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.40;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:700px;margin:0 auto;padding:0 24px;text-align:center;">
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(2rem,4vw,3.5rem);color:#E2E8F0;line-height:1.2;margin-bottom:20px;" class="reveal">[HEADLINE CTA]</h2>
    <p style="font-size:1.0625rem;color:#94A3B8;margin-bottom:40px;" class="reveal" data-delay="1">
      [FRASE URGENZA/MOTIVAZIONE] — <strong>[GARANZIA O ASSICURAZIONE]</strong>.
    </p>
    <button class="reveal" data-delay="2" style="font-family:'Inter',sans-serif;font-size:1rem;font-weight:700;letter-spacing:0.08em;text-transform:lowercase;color:#020202;background:linear-gradient(135deg,#E3C878,#D4AF37);padding:20px 56px;border:none;border-radius:2px;cursor:pointer;transition:all 0.3s;box-shadow:0 4px 32px rgba(212,175,55,0.4);animation:pulse 2s infinite;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 12px 40px rgba(212,175,55,0.6)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 32px rgba(212,175,55,0.4)'">
      [TESTO CTA PRINCIPALE]
    </button>
    <p style="margin-top:16px;font-size:0.8125rem;color:#64748B;" class="reveal" data-delay="3">[MICRO-COPY RASSICURANTE]</p>
  </div>
</section>
```

---

## TEMPLATE 9 — FAQ ACCORDION (light, vanilla JS)

```html
<section style="position:relative;background:#DCD8CF;padding:100px 0;overflow:hidden;">
  <!-- GRAIN light -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.35;mix-blend-mode:multiply;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.20;mix-blend-mode:multiply;pointer-events:none;z-index:11;"></div>

  <div style="position:relative;z-index:20;max-width:800px;margin:0 auto;padding:0 24px;">
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(2rem,4vw,3rem);color:#020202;text-align:center;margin-bottom:56px;" class="reveal">domande frequenti</h2>

    <!-- FAQ Item (ripeti) -->
    <div class="faq-item reveal" style="border-bottom:1px solid rgba(0,0,0,0.1);overflow:hidden;">
      <button onclick="toggleFaq(this)" style="width:100%;text-align:left;padding:24px 0;font-family:'Inter',sans-serif;font-size:1rem;font-weight:600;color:#020202;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;">
        [DOMANDA FAQ]
        <span style="font-size:1.25rem;transition:transform 0.3s;flex-shrink:0;margin-left:16px;">+</span>
      </button>
      <div style="max-height:0;overflow:hidden;transition:max-height 0.4s ease;">
        <p style="padding:0 0 24px;color:#374151;font-size:0.9375rem;line-height:1.7;"><strong>[PUNTO CHIAVE]</strong> — [RISPOSTA COMPLETA].</p>
      </div>
    </div>

  </div>
</section>

<script>
function toggleFaq(btn) {
  var item = btn.parentElement;
  var answer = item.querySelector('div');
  var icon = btn.querySelector('span');
  var isOpen = answer.style.maxHeight && answer.style.maxHeight !== '0px';
  // Chiudi tutte
  document.querySelectorAll('.faq-item div').forEach(function(d) { d.style.maxHeight = '0px'; });
  document.querySelectorAll('.faq-item button span').forEach(function(s) { s.style.transform = 'rotate(0deg)'; s.textContent = '+'; });
  if (!isOpen) {
    answer.style.maxHeight = answer.scrollHeight + 'px';
    icon.style.transform = 'rotate(45deg)';
    icon.textContent = '+';
  }
}
</script>
```

---

## TEMPLATE 10 — FOOTER (dark minimal)

```html
<footer style="position:relative;background:#020202;padding:60px 0 40px;overflow:hidden;border-top:1px solid rgba(227,200,120,0.15);">
  <!-- GRAIN -->
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.35;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>

  <div style="position:relative;z-index:20;max-width:1200px;margin:0 auto;padding:0 24px;">
    <div style="display:grid;grid-template-columns:2fr 1fr 1fr;gap:48px;margin-bottom:48px;">

      <div>
        <div style="font-family:'Cinzel',serif;font-size:1.25rem;color:#E3C878;margin-bottom:16px;">[BRAND NAME]</div>
        <p style="font-size:0.875rem;color:#64748B;line-height:1.7;max-width:280px;"><strong>[TAGLINE]</strong> — [DESCRIZIONE BREVE].</p>
      </div>

      <div>
        <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#64748B;margin-bottom:16px;">link utili</div>
        <ul style="list-style:none;padding:0;margin:0;">
          <li style="margin-bottom:10px;"><a href="#" style="font-size:0.875rem;color:#94A3B8;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#E3C878'" onmouseout="this.style.color='#94A3B8'">[LINK 1]</a></li>
          <li style="margin-bottom:10px;"><a href="#" style="font-size:0.875rem;color:#94A3B8;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#E3C878'" onmouseout="this.style.color='#94A3B8'">[LINK 2]</a></li>
        </ul>
      </div>

      <div>
        <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#64748B;margin-bottom:16px;">legale</div>
        <ul style="list-style:none;padding:0;margin:0;">
          <li style="margin-bottom:10px;"><a href="#" style="font-size:0.875rem;color:#94A3B8;text-decoration:none;">privacy policy</a></li>
          <li style="margin-bottom:10px;"><a href="#" style="font-size:0.875rem;color:#94A3B8;text-decoration:none;">termini e condizioni</a></li>
        </ul>
      </div>

    </div>

    <div style="border-top:1px solid rgba(255,255,255,0.05);padding-top:32px;display:flex;justify-content:space-between;align-items:center;flex-wrap:gap:16px;">
      <p style="font-size:0.8125rem;color:#374151;">© [ANNO] [BRAND]. tutti i diritti riservati.</p>
      <p style="font-size:0.8125rem;color:#374151;">crafted with <strong style="color:#E3C878;">digital empire</strong></p>
    </div>
  </div>
</footer>
```
