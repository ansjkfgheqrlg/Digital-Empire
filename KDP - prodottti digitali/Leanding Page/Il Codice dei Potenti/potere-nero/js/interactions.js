/* ═══════════════════════════════════════════════
   IL CODICE DEI POTENTI — INTERACTIONS
   Film-grade multi-octave grain + scroll reveals
   ═══════════════════════════════════════════════ */

/* ─── Film-grade grain texture (3-layer composited noise) ─── */
(function generateGrain() {
  var dpr = window.devicePixelRatio || 1;
  var tile = 512;
  var physical = Math.round(tile * dpr);

  var c = document.createElement('canvas');
  c.width = physical;
  c.height = physical;
  var ctx = c.getContext('2d');

  /* Layer 1 — fine 1:1 pixel noise (base texture) */
  var imgData = ctx.createImageData(physical, physical);
  var d = imgData.data;
  for (var i = 0; i < d.length; i += 4) {
    var v = (Math.random() * 255) | 0;
    d[i] = v; d[i + 1] = v; d[i + 2] = v;
    d[i + 3] = 28;
  }
  ctx.putImageData(imgData, 0, 0);

  /* Layer 2 — medium grain clusters (2x2 CSS px, DPR-scaled) */
  ctx.globalCompositeOperation = 'screen';
  var b2 = Math.max(2, Math.round(2 * dpr));
  for (var y1 = 0; y1 < physical; y1 += b2) {
    for (var x1 = 0; x1 < physical; x1 += b2) {
      var v2 = Math.random();
      ctx.fillStyle = 'rgba(' + ((v2 * 255) | 0) + ',' + ((v2 * 255) | 0) + ',' + ((v2 * 255) | 0) + ',' + (v2 * 0.09).toFixed(3) + ')';
      ctx.fillRect(x1, y1, b2, b2);
    }
  }

  /* Layer 3 — coarse organic blobs (4x4 CSS px, sparse) */
  var b3 = Math.max(4, Math.round(4 * dpr));
  for (var y2 = 0; y2 < physical; y2 += b3) {
    for (var x2 = 0; x2 < physical; x2 += b3) {
      if (Math.random() > 0.55) {
        var v3 = Math.random();
        ctx.fillStyle = 'rgba(' + ((v3 * 255) | 0) + ',' + ((v3 * 255) | 0) + ',' + ((v3 * 255) | 0) + ',' + (v3 * 0.05).toFixed(3) + ')';
        ctx.fillRect(x2, y2, b3, b3);
      }
    }
  }
  ctx.globalCompositeOperation = 'source-over';

  var url = c.toDataURL('image/png');

  var el = document.createElement('div');
  el.id = 'grain-canvas';
  el.style.cssText =
    'position:fixed;inset:0;width:100%;height:100%;' +
    'pointer-events:none;z-index:9999;' +
    'opacity:0.34;mix-blend-mode:overlay;' +
    'background-image:url(' + url + ');' +
    'background-size:' + tile + 'px ' + tile + 'px;' +
    'background-repeat:repeat;' +
    'image-rendering:crisp-edges;' +
    'image-rendering:pixelated;';
  document.body.prepend(el);

  /* Living-film animation: shift grain position */
  setInterval(function () {
    el.style.backgroundPosition =
      ((Math.random() * tile) | 0) + 'px ' +
      ((Math.random() * tile) | 0) + 'px';
  }, 80);
})();

/* ─── Image fallback handler ─── */
document.querySelectorAll('img').forEach(function (img) {
  img.addEventListener('error', function () {
    var card = this.closest('.book-card');
    if (card) card.classList.add('no-img');
    this.style.display = 'none';
  });
});

/* ─── Scroll reveal ─── */
var revealEls = document.querySelectorAll(
  '.character-card, .book-layout, .inside-header, .cta-content, .book-fan, .roadmap-header, .roadmap-step'
);

var revealObs = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      revealObs.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.1,
  rootMargin: '0px 0px -40px 0px'
});

revealEls.forEach(function (el) {
  el.classList.add('reveal-ready');
  revealObs.observe(el);
});

/* ─── Smooth scroll ─── */
document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
  anchor.addEventListener('click', function (e) {
    var target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
