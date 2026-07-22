#!/usr/bin/env python3
"""
site_builder.py — HTML Assembler
Digital Empire | Website Creator System

Assembla sezioni HTML, divisori e script in un singolo file index.html
conforme a tutti i requisiti del sistema (K00-K08).

Uso tipico (da web-master.md):
    from site_builder import SiteBuilder

    builder = SiteBuilder(
        site_name="trading-ebook",
        palette="gold",
        title="il metodo dei trader professionisti",
        description="guida al trading sistematico"
    )
    builder.add_section(hero_html)
    builder.add_divider("inclined_strip")
    builder.add_section(benefits_html)
    ...
    builder.build("trading-ebook.html")

Uso da CLI (debug/test):
    python site_builder.py --demo
    python site_builder.py --assemble sections/ --output mysite.html
"""

import sys
import os
import argparse
from pathlib import Path
from datetime import datetime


# =============================================================================
# GOOGLE FONTS IMPORT
# =============================================================================

GOOGLE_FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Cinzel:wght@400;600;700;900&"
    "family=Inter:wght@200;300;400;600;700;800&"
    "family=Playfair+Display:ital,wght@0,400;0,700;1,400&"
    "display=swap"
)


# =============================================================================
# RESET CSS + VARIABILI + KEYFRAMES GLOBALI
# =============================================================================

def get_global_css(palette: dict) -> str:
    return f"""
  /* === RESET === */
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: 'Inter', sans-serif;
    font-weight: 300;
    font-size: 1rem;
    line-height: 1.7;
    color: #94A3B8;
    background: {palette.get('bg_darkest', '#020202')};
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
    overflow-x: hidden;
  }}

  /* === VARIABILI CSS === */
  :root {{
    --color-primary:   {palette.get('primary', '#E3C878')};
    --color-secondary: {palette.get('secondary', '#D4AF37')};
    --color-accent:    {palette.get('accent', '#94A3B8')};
    --silver-cool:     #94A3B8;
    --silver-light:    #E2E8F0;
    --silver-medium:   #CBD5E1;
    --silver-dark:     #64748B;
    --bg-darkest:      {palette.get('bg_darkest', '#020202')};
    --bg-dark:         {palette.get('bg_dark', '#0a0a0a')};
    --bg-light:        {palette.get('bg_light', '#DCD8CF')};
    --text-muted:      #94A3B8;
    --text-base:       #CBD5E1;
    --text-bright:     #E2E8F0;
    --gradient-metallic: linear-gradient(90deg, #94A3B8 0%, #E2E8F0 20%, #E3C878 45%, #FFFFFF 50%, #E3C878 55%, #E2E8F0 80%, #94A3B8 100%);
  }}

  /* === TIPOGRAFIA === */
  h1, h2, h3, h4, h5, h6 {{ text-transform: lowercase; letter-spacing: -0.02em; }}
  h1 {{ font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 6vw, 5.5rem); font-weight: 400; line-height: 1.1; }}
  h2 {{ font-family: 'Cinzel', serif; font-size: clamp(2rem, 4vw, 4rem); font-weight: 600; line-height: 1.2; }}
  h3 {{ font-family: 'Cinzel', serif; font-size: clamp(1.4rem, 2.5vw, 2rem); font-weight: 600; line-height: 1.3; }}
  p  {{ font-weight: 300; color: #94A3B8; line-height: 1.7; margin-bottom: 1em; }}
  p strong  {{ font-weight: 700; color: #E2E8F0; }}
  li {{ font-weight: 300; color: #94A3B8; line-height: 1.7; margin-bottom: 0.5em; }}
  li strong {{ font-weight: 700; color: #E2E8F0; }}
  strong {{ font-weight: 700; color: #E2E8F0; }}
  a {{ color: inherit; transition: color 0.2s; }}

  /* === SCROLLBAR === */
  ::-webkit-scrollbar {{ width: 8px; }}
  ::-webkit-scrollbar-track {{ background: #0a0a0a; }}
  ::-webkit-scrollbar-thumb {{ background: #333; border-radius: 4px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: {palette.get('primary', '#E3C878')}; }}

  /* === SCROLL REVEAL === */
  .reveal {{ opacity: 0; transform: translateY(24px); transition: opacity 0.8s ease, transform 0.8s ease; }}
  .reveal.visible {{ opacity: 1; transform: translateY(0); }}
  .reveal[data-delay="1"] {{ transition-delay: 0.1s; }}
  .reveal[data-delay="2"] {{ transition-delay: 0.2s; }}
  .reveal[data-delay="3"] {{ transition-delay: 0.3s; }}
  .reveal[data-delay="4"] {{ transition-delay: 0.4s; }}
  .reveal[data-delay="5"] {{ transition-delay: 0.5s; }}

  /* === KEYFRAMES === */
  @keyframes float {{
    0%, 100% {{ transform: translateY(0px); }}
    50%       {{ transform: translateY(-20px); }}
  }}
  @keyframes shimmerMove {{
    0%   {{ background-position: -200% center; }}
    100% {{ background-position: 200% center; }}
  }}
  @keyframes twinkle {{
    0%, 100% {{ opacity: 0.4; transform: scale(0.8); }}
    50%       {{ opacity: 1;   transform: scale(1.1); }}
  }}
  @keyframes grainMove {{
    0%,100% {{ background-position: 0 0; }}
    25%     {{ background-position: 10% -5%; }}
    50%     {{ background-position: -5% 10%; }}
    75%     {{ background-position: 5% -10%; }}
  }}
  @keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(30px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
  }}
  @keyframes pulse {{
    0%, 100% {{ box-shadow: 0 0 0 0 rgba(212,175,55,0.4); }}
    50%       {{ box-shadow: 0 0 0 12px rgba(212,175,55,0); }}
  }}

  /* === UTILITY === */
  .gradient-text-gold {{
    background: linear-gradient(90deg, #94A3B8 0%, #E2E8F0 30%, #E3C878 55%, #FFFFFF 65%, #E3C878 75%, #CBD5E1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0px 4px 1px rgba(0,0,0,0.9)) drop-shadow(0px 0px 30px rgba(253,230,138,0.15));
  }}
  .float {{ animation: float 6s ease-in-out infinite; }}
  .shimmer-text {{
    background: linear-gradient(90deg, #94A3B8 0%, #E2E8F0 30%, #E3C878 45%, #FFFFFF 50%, #E3C878 55%, #E2E8F0 70%, #94A3B8 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmerMove 3s linear infinite;
  }}

  /* === MOBILE BASE === */
  @media (max-width: 768px) {{
    h1 {{ font-size: clamp(2rem, 8vw, 3rem); }}
    h2 {{ font-size: clamp(1.6rem, 6vw, 2.5rem); }}
    h3 {{ font-size: clamp(1.2rem, 4vw, 1.6rem); }}
    p  {{ font-size: 0.9375rem; }}
  }}
"""


# =============================================================================
# GLOBAL JS
# =============================================================================

GLOBAL_JS = """
// === SCROLL REVEAL ===
(function() {
  var reveals = document.querySelectorAll('.reveal');
  if (!reveals.length) return;
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  reveals.forEach(function(el) { observer.observe(el); });
})();

// === COUNTER ANIMATE ===
(function() {
  var counters = document.querySelectorAll('.counter');
  if (!counters.length) return;
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      var target = parseInt(el.getAttribute('data-target') || '0');
      var suffix = el.getAttribute('data-suffix') || '';
      var duration = 1500;
      var start = Date.now();
      var interval = setInterval(function() {
        var elapsed = Date.now() - start;
        var progress = Math.min(elapsed / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(eased * target).toLocaleString('it-IT') + suffix;
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

// === DUST CANVAS (se presente) ===
(function() {
  var canvas = document.getElementById('dust-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var W, H, particles = [];
  function resize() { W = canvas.width = canvas.offsetWidth; H = canvas.height = canvas.offsetHeight; }
  resize();
  window.addEventListener('resize', resize);
  for (var i = 0; i < 60; i++) {
    particles.push({
      x: Math.random() * (W || 1200), y: Math.random() * (H || 800),
      r: Math.random() * 1.5 + 0.3,
      speedX: (Math.random() - 0.5) * 0.3,
      speedY: -(Math.random() * 0.3 + 0.1),
      opacity: Math.random() * 0.6 + 0.2,
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
      p.x += p.speedX; p.y += p.speedY;
      if (p.y < -5) p.y = H + 5;
      if (p.x < -5) p.x = W + 5;
      if (p.x > W + 5) p.x = -5;
    });
    requestAnimationFrame(draw);
  }
  draw();
})();

// === FAQ TOGGLE (se presente) ===
function toggleFaq(btn) {
  var item = btn.parentElement;
  var answer = item.querySelector('div');
  var icon = btn.querySelector('span');
  var isOpen = answer.style.maxHeight && answer.style.maxHeight !== '0px';
  document.querySelectorAll('.faq-item div').forEach(function(d) { d.style.maxHeight = '0px'; });
  document.querySelectorAll('.faq-item button span').forEach(function(s) { s.style.transform = 'rotate(0deg)'; });
  if (!isOpen) { answer.style.maxHeight = answer.scrollHeight + 'px'; if(icon) icon.style.transform = 'rotate(45deg)'; }
}
"""


# =============================================================================
# PALETTES
# =============================================================================

PALETTES = {
    'gold': {
        'primary': '#E3C878', 'secondary': '#D4AF37', 'accent': '#94A3B8',
        'bg_darkest': '#020202', 'bg_dark': '#0a0a0a', 'bg_light': '#DCD8CF',
    },
    'green': {
        'primary': '#4A9B7A', 'secondary': '#2D6A4F', 'accent': '#94A3B8',
        'bg_darkest': '#031c16', 'bg_dark': '#051f18', 'bg_light': '#E8EDE9',
    },
    'violet': {
        'primary': '#7B6FA8', 'secondary': '#6B5B95', 'accent': '#94A3B8',
        'bg_darkest': '#1A1028', 'bg_dark': '#130D1F', 'bg_light': '#E8E6F0',
    },
    'red': {
        'primary': '#C0505A', 'secondary': '#9B3D45', 'accent': '#94A3B8',
        'bg_darkest': '#1A0608', 'bg_dark': '#120305', 'bg_light': '#F0E8E9',
    },
    'blue': {
        'primary': '#4A7FB5', 'secondary': '#3D6E9E', 'accent': '#94A3B8',
        'bg_darkest': '#0f2e4a', 'bg_dark': '#0a2238', 'bg_light': '#E6EEF4',
    },
}


# =============================================================================
# SITE BUILDER CLASS
# =============================================================================

class SiteBuilder:
    """
    Assembla sezioni e divisori in un singolo file HTML vanilla.

    Uso:
        builder = SiteBuilder(site_name="mysite", palette="gold", title="Il mio sito")
        builder.add_section(html_string)
        builder.add_divider("inclined_strip")
        builder.build("mysite.html")
    """

    def __init__(
        self,
        site_name: str = "website",
        palette: str = "gold",
        title: str = "landing page",
        description: str = "",
        lang: str = "it",
    ):
        self.site_name = site_name
        self.palette_name = palette
        self.palette = PALETTES.get(palette.lower(), PALETTES['gold'])
        self.title = title
        self.description = description or title
        self.lang = lang
        self.blocks = []  # lista di (tipo, html)

    def add_section(self, html: str) -> None:
        """Aggiunge una sezione HTML."""
        self.blocks.append(('section', html.strip()))

    def add_divider(self, divider_type: str = "inclined_strip",
                    color_above: str = "#020202", color_below: str = "#020202") -> None:
        """
        Aggiunge un divisore SVG dalla libreria K03.
        divider_type: 'lux_arc' | 'lux_v' | 'lux_curve' | 'lux_triangle' | 'inclined_strip'
        """
        html = self._get_divider_html(divider_type, color_above, color_below)
        self.blocks.append(('divider', html))

    def add_raw_html(self, html: str) -> None:
        """Aggiunge HTML grezzo (nav, script extra, ecc.)."""
        self.blocks.append(('raw', html.strip()))

    def build(self, output_path: str = None) -> str:
        """
        Assembla e scrive il file HTML finale.
        Returns il path del file scritto.
        """
        if not output_path:
            output_path = f"{self.site_name}-index.html"

        html = self._build_html()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"\n  ✅ File generato: {output_path}")
        print(f"     Sezioni: {sum(1 for t,_ in self.blocks if t=='section')}")
        print(f"     Divisori: {sum(1 for t,_ in self.blocks if t=='divider')}")
        print(f"     Dimensione: {len(html)/1024:.1f} KB")
        print(f"\n  Prossimo passo: python quality_check.py {output_path}\n")

        return output_path

    def _build_html(self) -> str:
        """Costruisce il documento HTML completo."""
        css = get_global_css(self.palette)
        body_content = '\n'.join(html for _, html in self.blocks)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        return f"""<!DOCTYPE html>
<html lang="{self.lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{self.description}">
  <title>{self.title}</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{GOOGLE_FONTS_URL}" rel="stylesheet">

  <style>
{css}
  </style>

  <!--
    Generated by Website Creator System
    Digital Empire | {timestamp}
    Palette: {self.palette_name}
    K00 Legge Cosmica: silver mixing active
    K01 5 Leggi d'Oro: grain + interrupt + lowercase + strong + dividers + curve
  -->
</head>
<body>

{body_content}

<script>
{GLOBAL_JS}
</script>

</body>
</html>"""

    def _get_divider_html(self, divider_type: str, color_above: str, color_below: str) -> str:
        """Genera HTML divisore dalla libreria K03."""

        if divider_type == 'lux_arc':
            return f"""<!-- LuxArc Divider (dark→light) -->
<div style="position:relative;height:100px;overflow:hidden;background:{color_above};">
  <div style="position:absolute;inset:0;clip-path:polygon(0% 100%,0% 35%,50% 0%,100% 35%,100% 100%);background:{color_below};"></div>
  <svg viewBox="0 0 1200 100" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%;">
    <defs>
      <linearGradient id="luxArcGrad{id(self)}" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#94A3B8"/><stop offset="20%" stop-color="#E2E8F0"/>
        <stop offset="45%" stop-color="#E3C878"/><stop offset="50%" stop-color="#FFFFFF"/>
        <stop offset="55%" stop-color="#E3C878"/><stop offset="80%" stop-color="#E2E8F0"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M 0,100 L 0,35 L 600,0 L 1200,35 L 1200,100" fill="none" stroke="url(#luxArcGrad{id(self)})" stroke-width="2"/>
    <path d="M 0,100 L 0,35 L 600,0 L 1200,35 L 1200,100" fill="none" stroke="rgba(255,255,255,0.9)" stroke-width="1" style="mix-blend-mode:overlay;"/>
  </svg>
</div>"""

        elif divider_type == 'lux_v':
            return f"""<!-- LuxV Divider (light→dark) -->
<div style="position:relative;height:80px;overflow:hidden;background:{color_above};">
  <div style="position:absolute;inset:0;clip-path:polygon(0% 0%,100% 0%,100% 100%,50% 40%,0% 100%);background:{color_below};"></div>
  <svg viewBox="0 0 1200 80" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%;">
    <defs>
      <linearGradient id="luxVGrad{id(self)}" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#94A3B8"/><stop offset="20%" stop-color="#E2E8F0"/>
        <stop offset="45%" stop-color="#E3C878"/><stop offset="50%" stop-color="#FFFFFF"/>
        <stop offset="55%" stop-color="#E3C878"/><stop offset="80%" stop-color="#E2E8F0"/>
        <stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M -100,0 L 600,80 L 1300,0" fill="none" stroke="url(#luxVGrad{id(self)})" stroke-width="2"/>
    <path d="M -100,0 L 600,80 L 1300,0" fill="none" stroke="rgba(255,255,255,0.9)" stroke-width="1" style="mix-blend-mode:overlay;"/>
  </svg>
</div>"""

        elif divider_type == 'lux_triangle':
            return f"""<!-- LuxTriangle Divider -->
<div style="position:relative;height:120px;overflow:visible;z-index:5;">
  <div style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:200px;height:100px;background:linear-gradient(180deg,{color_above} 0%,{color_below} 100%);clip-path:polygon(0% 0%,50% 100%,100% 0%);">
    <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.40;mix-blend-mode:overlay;pointer-events:none;clip-path:polygon(0% 0%,50% 100%,100% 0%);"></div>
  </div>
  <svg viewBox="0 0 200 100" style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:200px;height:100px;overflow:visible;">
    <defs>
      <linearGradient id="triGrad{id(self)}" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#94A3B8"/><stop offset="50%" stop-color="#E3C878"/><stop offset="100%" stop-color="#94A3B8"/>
      </linearGradient>
    </defs>
    <path d="M 0,0 L 100,100 L 200,0" fill="none" stroke="url(#triGrad{id(self)})" stroke-width="1.5"/>
  </svg>
</div>"""

        else:  # inclined_strip (default)
            return f"""<!-- InclinedStrip Divider -->
<div style="position:relative;height:48px;overflow:hidden;margin:-12px 0;">
  <div style="position:absolute;left:-5%;right:-5%;top:50%;transform:translateY(-50%) rotate(-2.5deg);height:24px;background:linear-gradient(90deg,#8E9BAF 0%,#CBD5E1 15%,#D4AF37 35%,#FFD700 50%,#D4AF37 65%,#CBD5E1 85%,#8E9BAF 100%);box-shadow:0 -1px 0 rgba(255,255,255,0.9),0 1px 8px rgba(0,0,0,0.6);overflow:hidden;">
    <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.30;mix-blend-mode:overlay;pointer-events:none;"></div>
    <div style="position:absolute;top:0;left:0;right:0;height:1px;background:rgba(255,255,255,0.9);"></div>
    <div style="position:absolute;bottom:0;left:0;right:0;height:1px;background:rgba(0,0,0,0.4);"></div>
  </div>
</div>"""


# =============================================================================
# CLI — DEMO MODE
# =============================================================================

def build_demo() -> None:
    """Genera un sito demo per testare il sistema."""
    builder = SiteBuilder(
        site_name="demo",
        palette="gold",
        title="demo — website creator system",
        description="sito dimostrativo del Website Creator System"
    )

    # Hero
    builder.add_section("""
<section id="hero" style="position:relative;background:#020202;min-height:100vh;display:flex;align-items:center;overflow:hidden;">
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.45;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.3;mix-blend-mode:screen;pointer-events:none;z-index:11;"></div>
  <canvas id="dust-canvas" style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2;"></canvas>
  <div style="position:relative;z-index:20;max-width:900px;margin:0 auto;padding:120px 24px 80px;text-align:center;">
    <p style="font-family:'Inter',sans-serif;font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#94A3B8;margin-bottom:24px;" class="reveal">website creator system · demo</p>
    <h1 class="gradient-text-gold reveal" data-delay="1">il sistema che crea siti web premium in ore, non settimane</h1>
    <p style="font-size:1.125rem;font-weight:300;color:#94A3B8;max-width:600px;margin:24px auto 40px;line-height:1.7;" class="reveal" data-delay="2">ogni sito generato rispetta la <strong>legge cosmica silver mixing</strong> e le <strong>5 leggi d'oro del design</strong> — qualità enterprise garantita.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;" class="reveal" data-delay="3">
      <button style="font-family:'Inter',sans-serif;font-size:0.875rem;font-weight:600;letter-spacing:0.08em;text-transform:lowercase;color:#020202;background:linear-gradient(135deg,#E3C878,#D4AF37);padding:16px 40px;border:none;border-radius:2px;cursor:pointer;transition:all 0.3s;box-shadow:0 4px 24px rgba(212,175,55,0.3);" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform=''">inizia subito</button>
      <button style="font-family:'Inter',sans-serif;font-size:0.875rem;font-weight:600;letter-spacing:0.08em;text-transform:lowercase;color:#CBD5E1;background:transparent;padding:14px 38px;border:1px solid rgba(148,163,184,0.5);border-radius:2px;cursor:pointer;">scopri come funziona</button>
    </div>
  </div>
</section>""")

    builder.add_divider('inclined_strip')

    # FAQ section (light — pattern interrupt)
    builder.add_section("""
<section style="position:relative;background:#DCD8CF;padding:100px 0;overflow:hidden;">
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.35;mix-blend-mode:multiply;pointer-events:none;z-index:10;"></div>
  <div style="position:absolute;inset:0;background-image:url(&quot;data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter2'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter2)' opacity='1'/%3E%3C/svg%3E&quot;);background-size:100px 100px;filter:contrast(180%) brightness(40%);opacity:0.20;mix-blend-mode:multiply;pointer-events:none;z-index:11;"></div>
  <div style="position:relative;z-index:20;max-width:800px;margin:0 auto;padding:0 24px;">
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(2rem,4vw,3rem);color:#020202;text-align:center;margin-bottom:56px;" class="reveal">domande frequenti</h2>
    <div class="faq-item reveal" style="border-bottom:1px solid rgba(0,0,0,0.1);overflow:hidden;">
      <button onclick="toggleFaq(this)" style="width:100%;text-align:left;padding:24px 0;font-family:'Inter',sans-serif;font-size:1rem;font-weight:600;color:#020202;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;">il sistema usa framework CSS o JavaScript? <span style="font-size:1.25rem;transition:transform 0.3s;">+</span></button>
      <div style="max-height:0;overflow:hidden;transition:max-height 0.4s ease;"><p style="padding:0 0 24px;color:#374151;font-size:0.9375rem;line-height:1.7;"><strong>zero framework</strong> — output 100% vanilla HTML+CSS+JS. apri nel browser, funziona subito.</p></div>
    </div>
  </div>
</section>""")

    builder.add_divider('lux_v', '#DCD8CF', '#020202')

    # Footer
    builder.add_section("""
<footer style="position:relative;background:#020202;padding:60px 0 40px;border-top:1px solid rgba(227,200,120,0.15);overflow:hidden;">
  <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.35;mix-blend-mode:overlay;pointer-events:none;z-index:10;"></div>
  <div style="position:relative;z-index:20;max-width:1200px;margin:0 auto;padding:0 24px;text-align:center;">
    <div style="font-family:'Cinzel',serif;font-size:1.25rem;color:#E3C878;margin-bottom:16px;">website creator</div>
    <p style="font-size:0.8125rem;color:#374151;">© 2025 digital empire. <strong style="color:#94A3B8;">website creator system</strong> — tutti i diritti riservati.</p>
  </div>
</footer>""")

    output = builder.build("demo-index.html")
    print(f"  Apri nel browser per vedere il risultato: {output}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Site Builder — assembla sezioni HTML in un file finale vanilla',
    )
    parser.add_argument('--demo', action='store_true', help='Genera un sito demo di test')
    parser.add_argument('--assemble', metavar='FOLDER', help='Assembla tutti i file .html da una cartella')
    parser.add_argument('--output', '-o', default='index.html', help='File di output (default: index.html)')
    parser.add_argument('--palette', default='gold', choices=list(PALETTES.keys()), help='Palette colori')
    parser.add_argument('--title', default='landing page', help='Titolo del sito')

    args = parser.parse_args()

    if args.demo:
        build_demo()
        return

    if args.assemble:
        folder = Path(args.assemble)
        if not folder.exists():
            print(f"\n  ❌ Cartella non trovata: {args.assemble}")
            sys.exit(1)

        builder = SiteBuilder(
            site_name=Path(args.output).stem,
            palette=args.palette,
            title=args.title,
        )

        section_files = sorted(folder.glob('*.html'))
        if not section_files:
            print(f"\n  ❌ Nessun file .html trovato in: {args.assemble}")
            sys.exit(1)

        for f in section_files:
            content = f.read_text(encoding='utf-8')
            if 'divider' in f.name.lower():
                builder.add_raw_html(content)
            else:
                builder.add_section(content)
            print(f"  + {f.name}")

        builder.build(args.output)
        return

    # Nessun comando specificato
    parser.print_help()
    print("\n  Esempi:")
    print("    python site_builder.py --demo")
    print("    python site_builder.py --assemble sections/ --output mysite.html --palette blue")


if __name__ == '__main__':
    main()
