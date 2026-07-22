# K06 — ANIMATIONS (Vanilla JS dall'Agency)

> Tutte le animazioni sono convertite da React+Framer Motion a vanilla HTML+CSS+JS. Zero framework, zero dipendenze.

---

## ANIMAZIONE 1 — SCROLL REVEAL (IntersectionObserver)

L'animazione più importante. Ogni elemento che entra in viewport appare con fade+slide.

```html
<!-- Aggiungi classe .reveal agli elementi da animare -->
<div class="reveal">contenuto che appare allo scroll</div>

<style>
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
/* Variante con delay (staggered) */
.reveal[data-delay="1"] { transition-delay: 0.1s; }
.reveal[data-delay="2"] { transition-delay: 0.2s; }
.reveal[data-delay="3"] { transition-delay: 0.3s; }
.reveal[data-delay="4"] { transition-delay: 0.4s; }
.reveal[data-delay="5"] { transition-delay: 0.5s; }
</style>

<script>
// Scroll Reveal — IntersectionObserver
(function() {
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  reveals.forEach(function(el) { observer.observe(el); });
})();
</script>
```

**Uso tipico:**
```html
<!-- Hero title: no delay -->
<h1 class="reveal">headline principale</h1>

<!-- Card grid con stagger -->
<div class="reveal" data-delay="1">card 1</div>
<div class="reveal" data-delay="2">card 2</div>
<div class="reveal" data-delay="3">card 3</div>
```

---

## ANIMAZIONE 2 — FLOAT (elementi flottanti)

Per immagini, icone, mockup di prodotti — effetto levitazione perpetua.

```css
@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33%       { transform: translateY(-12px) rotate(1deg); }
  66%       { transform: translateY(-20px) rotate(-1deg); }
}

@keyframes float-slow {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-15px); }
}

.float {
  animation: float 6s ease-in-out infinite;
}

.float-slow {
  animation: float-slow 8s ease-in-out infinite;
}

/* Con shadow che si riduce in alto (effetto profondità) */
.float-shadow {
  animation: float 6s ease-in-out infinite;
  filter: drop-shadow(0 20px 30px rgba(0,0,0,0.5));
}
.float-shadow:hover {
  filter: drop-shadow(0 30px 40px rgba(212,175,55,0.3));
}
```

---

## ANIMAZIONE 3 — SHIMMER TEXT

Luccichio che scorre sul testo gradient. Usato su headline e prezzi.

```css
@keyframes shimmerMove {
  0%   { background-position: -200% center; }
  100% { background-position: 200% center; }
}

.shimmer-text {
  background: linear-gradient(
    90deg,
    #94A3B8 0%,
    #E2E8F0 30%,
    #E3C878 45%,
    #FFFFFF 50%,
    #E3C878 55%,
    #E2E8F0 70%,
    #94A3B8 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmerMove 3s linear infinite;
}
```

---

## ANIMAZIONE 4 — TWINKLE (stelle/particelle statiche)

Per elementi decorativi tipo stelline nell'hero.

```css
@keyframes twinkle {
  0%, 100% { opacity: 0.4; transform: scale(0.8); }
  50%       { opacity: 1;   transform: scale(1.1); }
}

.twinkle {
  animation: twinkle 4s ease-in-out infinite;
}

/* Staggered per multiple stelle */
.twinkle:nth-child(2) { animation-delay: 1s; }
.twinkle:nth-child(3) { animation-delay: 2s; }
.twinkle:nth-child(4) { animation-delay: 3s; }
```

---

## ANIMAZIONE 5 — DUST CANVAS (particelle volanti)

Convertito da `DustCanvas.tsx` dell'Agency. Canvas API pura.

```html
<canvas id="dust-canvas" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2;"></canvas>

<script>
(function() {
  var canvas = document.getElementById('dust-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var W, H, particles = [];

  function resize() {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  // Crea 60 particelle
  for (var i = 0; i < 60; i++) {
    particles.push({
      x:     Math.random() * W,
      y:     Math.random() * H,
      r:     Math.random() * 1.5 + 0.3,
      speedX: (Math.random() - 0.5) * 0.3,
      speedY: -(Math.random() * 0.3 + 0.1),
      opacity: Math.random() * 0.6 + 0.2,
      // Colore: oro o silver
      color: Math.random() > 0.5 ? '212,175,55' : '148,163,184'
    });
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(function(p) {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(' + p.color + ',' + p.opacity + ')';
      ctx.fill();

      // Muovi
      p.x += p.speedX;
      p.y += p.speedY;

      // Wrap-around
      if (p.y < -5)    p.y = H + 5;
      if (p.x < -5)    p.x = W + 5;
      if (p.x > W + 5) p.x = -5;
    });
    requestAnimationFrame(draw);
  }
  draw();
})();
</script>
```

---

## ANIMAZIONE 6 — COUNTER ANIMATE

Per sezioni con numeri statistici (es. "12.000 clienti", "98% soddisfazione").

```html
<span class="counter" data-target="12000" data-suffix="+">0</span>

<script>
(function() {
  var counters = document.querySelectorAll('.counter');
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      var target = parseInt(el.getAttribute('data-target'));
      var suffix = el.getAttribute('data-suffix') || '';
      var duration = 1500; // ms
      var start = Date.now();
      var interval = setInterval(function() {
        var elapsed = Date.now() - start;
        var progress = Math.min(elapsed / duration, 1);
        // Easing out
        var eased = 1 - Math.pow(1 - progress, 3);
        var current = Math.floor(eased * target);
        el.textContent = current.toLocaleString('it-IT') + suffix;
        if (progress >= 1) {
          el.textContent = target.toLocaleString('it-IT') + suffix;
          clearInterval(interval);
        }
      }, 16);
      observer.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(function(el) { observer.observe(el); });
})();
</script>
```

---

## ANIMAZIONE 7 — MOUSE SPOTLIGHT

Riflesso radiale che segue il cursore dentro una sezione. Effetto premium.

```html
<section id="spotlight-section" style="position:relative; overflow:hidden;">
  <!-- ...contenuto... -->
</section>

<script>
(function() {
  var section = document.getElementById('spotlight-section');
  if (!section) return;
  section.addEventListener('mousemove', function(e) {
    var rect = section.getBoundingClientRect();
    var x = ((e.clientX - rect.left) / rect.width) * 100;
    var y = ((e.clientY - rect.top) / rect.height) * 100;
    section.style.background = 'radial-gradient(circle at ' + x + '% ' + y + '%, rgba(212,175,55,0.12) 0%, transparent 60%), [SFONDO-BASE]';
  });
  section.addEventListener('mouseleave', function() {
    section.style.background = '[SFONDO-BASE]';
  });
})();
</script>
```

---

## ANIMAZIONE 8 — WORD REVEAL

Ogni parola del titolo appare in stagger. Effetto cinematografico.

```html
<h1 id="word-reveal-title">il sistema che trasforma il tuo business</h1>

<script>
(function() {
  var el = document.getElementById('word-reveal-title');
  if (!el) return;
  var words = el.textContent.split(' ');
  el.innerHTML = words.map(function(w, i) {
    return '<span style="display:inline-block;opacity:0;transform:translateY(20px);transition:opacity 0.5s ease,transform 0.5s ease;transition-delay:' + (i * 0.08) + 's">' + w + '&nbsp;</span>';
  }).join('');

  var observer = new IntersectionObserver(function(entries) {
    if (!entries[0].isIntersecting) return;
    el.querySelectorAll('span').forEach(function(span) {
      span.style.opacity = '1';
      span.style.transform = 'translateY(0)';
    });
    observer.unobserve(el);
  }, { threshold: 0.3 });
  observer.observe(el);
})();
</script>
```

---

## ANIMAZIONE 9 — GRAIN MOVEMENT

Il grain "respira" lentamente — senso di vita organica.

```css
@keyframes grainMove {
  0%   { background-position: 0% 0%; }
  25%  { background-position: 10% -5%; }
  50%  { background-position: -5% 10%; }
  75%  { background-position: 5% -10%; }
  100% { background-position: 0% 0%; }
}

/* Applica al Layer 2 grain per movimento lento */
.grain-layer-2 {
  animation: grainMove 12s steps(2) infinite;
}
```

---

## CSS KEYFRAMES GLOBALI (da inserire nel `<head>` una volta sola)

```html
<style>
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-20px); }
}
@keyframes shimmerMove {
  0%   { background-position: -200% center; }
  100% { background-position: 200% center; }
}
@keyframes twinkle {
  0%, 100% { opacity: 0.4; transform: scale(0.8); }
  50%       { opacity: 1;   transform: scale(1.1); }
}
@keyframes grainMove {
  0%,100% { background-position: 0 0; }
  25%     { background-position: 10% -5%; }
  50%     { background-position: -5% 10%; }
  75%     { background-position: 5% -10%; }
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(212,175,55,0.4); }
  50%       { box-shadow: 0 0 0 12px rgba(212,175,55,0); }
}
</style>
```
