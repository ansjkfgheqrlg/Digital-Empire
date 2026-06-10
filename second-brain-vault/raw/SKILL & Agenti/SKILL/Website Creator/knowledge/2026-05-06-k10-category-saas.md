# K10-category-saas

> Source: File system (`SKILL & Agenti\SKILL\Website Creator\knowledge\K10-category-saas.md`)
> Collected: 2026-05-06
> Published: Unknown

# K10 — CATEGORIA: SaaS / APP / PIATTAFORMA / SOFTWARE

> Struttura, stili e pattern specifici per prodotti software e piattaforme digitali.

---

## STRUTTURA SEZIONI (ordine ottimale — SaaS 2024-2025)

```
1. [NAV]           Nav sticky — logo + link + "start free" button
2. [HERO]          Hero — value prop + screenshot UI + CTA doppia
3. [SOCIAL PROOF]  Loghi clienti / numeri — subito dopo hero
4. [DIVIDER]       InclinedStrip
5. [PROBLEM]       Problem Statement — il dolore che il SaaS risolve
6. [DIVIDER]       LuxCurve (sezione soluzione curva)
7. [SOLUTION]      Solution Overview — il "come" in modo visivo
8. [DIVIDER]       InclinedStrip
9. [FEATURES]      Features (bento grid o alternating) — 6-12 feature
10. [DIVIDER]      LuxArc
11. [HOW IT WORKS] How It Works — 3-4 step del flusso
12. [DIVIDER]      LuxV
13. [TESTIMONIALS] Testimonials + Case Studies
14. [DIVIDER]      LuxArc
15. [PRICING]      Pricing — 3 tier con toggle mensile/annuale
16. [DIVIDER]      InclinedStrip
17. [FAQ]          FAQ
18. [CTA FINAL]    Final CTA — ultima chance
19. [FOOTER]       Footer
```

---

## STILI DOMINANTI SaaS 2024-2025

### Dark Mode (71% dei SaaS top)
- **Sfondo:** `#020202` o `#0a0a0a`
- **Accent:** PALETTE 5 (blu silver) o PALETTE 3 (viola silver)
- **Glassmorphism:** card con `backdrop-filter:blur`, `background:rgba(255,255,255,0.05)`
- **Glow effects:** box-shadow colorato su elementi chiave

### Light Mode (29%)
- **Sfondo:** bianco o `#F8F6F2`
- **Accent:** colore brand argentizzato
- **Cards:** sfondo bianco con bordo sottile

### Layout trend 2024:
- **Bento Grid:** tiles di dimensioni diverse, alcune più grandi
- **Alternating:** feature a sinistra/destra alternati con immagini
- **Sticky Nav** con il prezzo "Start free" sempre visibile

---

## SEZIONI SPECIFICHE — DETTAGLIO

### HERO SaaS
```
Struttura:
- Eyebrow: "nuovo · [ANNO]" o "[NICHE] platform" o badge social proof
- Headline: value prop in < 5 secondi, outcome-focused (non feature-focused)
  Esempio: "chiudi il 3x più deals in meno della metà del tempo"
  Esempio: "automatizza il tuo supporto clienti e riduci i ticket del 78%"
- Subheadline: how (non what): "con [NOME] puoi [PROCESSO SEMPLICE]"
- CTA primaria: "start free trial" o "inizia gratis"
- CTA secondaria: "watch demo" o "guarda come funziona"
- Micro-copy: "no credit card required · setup in 2 minutes · cancel anytime"
- Visual: screenshot UI dentro device frame (laptop/browser mockup)
```

### LOGHI CLIENTI
```html
<!-- Strip loghi subito dopo hero — social proof immediato -->
<section style="background:#0a0a0a;padding:32px 0;border-top:1px solid rgba(255,255,255,0.05);border-bottom:1px solid rgba(255,255,255,0.05);">
  <div style="max-width:1200px;margin:0 auto;padding:0 24px;">
    <p style="text-align:center;font-size:0.75rem;color:#374151;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:24px;">fidato da team in crescita come</p>
    <div style="display:flex;justify-content:center;align-items:center;gap:48px;flex-wrap:wrap;opacity:0.5;filter:grayscale(100%);">
      <!-- Placeholder loghi: usa text come fallback -->
      <span style="font-family:'Cinzel',serif;font-size:1.25rem;color:#94A3B8;">[BRAND 1]</span>
      <span style="font-family:'Cinzel',serif;font-size:1.25rem;color:#94A3B8;">[BRAND 2]</span>
      <span style="font-family:'Cinzel',serif;font-size:1.25rem;color:#94A3B8;">[BRAND 3]</span>
      <span style="font-family:'Cinzel',serif;font-size:1.25rem;color:#94A3B8;">[BRAND 4]</span>
      <span style="font-family:'Cinzel',serif;font-size:1.25rem;color:#94A3B8;">[BRAND 5]</span>
    </div>
  </div>
</section>
```

### BENTO GRID FEATURES
```html
<!-- Bento grid: tile large + tile piccole -->
<div style="display:grid;grid-template-columns:repeat(12,1fr);grid-auto-rows:160px;gap:16px;max-width:1200px;margin:0 auto;">

  <!-- Tile grande (6 colonne, 2 righe) -->
  <div style="grid-column:span 6;grid-row:span 2;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:8px;padding:32px;transition:border-color 0.3s;position:relative;overflow:hidden;" onmouseover="this.style.borderColor='rgba(227,200,120,0.3)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.06)'">
    <div style="font-size:2.5rem;margin-bottom:16px;">[ICONA]</div>
    <h3 style="font-family:'Cinzel',serif;font-size:1.25rem;color:#E2E8F0;margin-bottom:12px;">[FEATURE PRINCIPALE]</h3>
    <p style="font-size:0.9375rem;color:#94A3B8;line-height:1.7;"><strong>[BENEFICIO]</strong> — [DESCRIZIONE DETTAGLIATA].</p>
    <!-- Screenshot/visual feature -->
    <div style="margin-top:20px;background:rgba(255,255,255,0.05);border-radius:4px;height:100px;display:flex;align-items:center;justify-content:center;color:#374151;font-size:0.875rem;">[UI SCREENSHOT PLACEHOLDER]</div>
  </div>

  <!-- Tile media (3 colonne, 1 riga) -->
  <div style="grid-column:span 3;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:8px;padding:24px;transition:border-color 0.3s;" onmouseover="this.style.borderColor='rgba(227,200,120,0.25)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.06)'">
    <div style="font-size:1.75rem;margin-bottom:12px;">[ICONA]</div>
    <h3 style="font-family:'Cinzel',serif;font-size:0.9375rem;color:#E2E8F0;margin-bottom:8px;">[FEATURE]</h3>
    <p style="font-size:0.8125rem;color:#94A3B8;"><strong>[BENEFICIO RAPIDO]</strong></p>
  </div>

  <!-- Ripeti tiles -->
</div>

<!-- Mobile: collassa a lista verticale -->
<style>
@media (max-width:768px) {
  .bento-grid { grid-template-columns:1fr !important; grid-auto-rows:auto !important; }
  .bento-tile-large { grid-column:1 !important; grid-row:auto !important; }
}
</style>
```

### PRICING (3 TIER)
```html
<div style="max-width:1100px;margin:0 auto;padding:0 24px;">

  <!-- Toggle mensile/annuale -->
  <div style="display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:48px;">
    <span id="toggle-monthly" style="font-size:0.875rem;font-weight:600;color:#E2E8F0;">mensile</span>
    <div id="pricing-toggle" onclick="togglePricing()" style="width:48px;height:26px;background:rgba(227,200,120,0.2);border:1px solid rgba(227,200,120,0.4);border-radius:13px;cursor:pointer;position:relative;transition:all 0.3s;">
      <div id="toggle-dot" style="position:absolute;top:3px;left:3px;width:18px;height:18px;background:#E3C878;border-radius:50%;transition:transform 0.3s;"></div>
    </div>
    <span id="toggle-annual" style="font-size:0.875rem;color:#94A3B8;">annuale <span style="color:#4A9B7A;font-size:0.75rem;font-weight:700;">(-25%)</span></span>
  </div>

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;align-items:start;">

    <!-- Tier STARTER -->
    <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:4px;padding:40px 32px;">
      <div style="font-family:'Cinzel',serif;font-size:0.75rem;letter-spacing:0.2em;text-transform:uppercase;color:#94A3B8;margin-bottom:16px;">starter</div>
      <div style="display:flex;align-items:baseline;gap:4px;margin-bottom:8px;">
        <span id="price-starter" style="font-family:'Cinzel',serif;font-size:2.5rem;font-weight:700;color:#E2E8F0;">[PREZZO]</span>
        <span style="color:#64748B;font-size:0.875rem;">/mese</span>
      </div>
      <p style="font-size:0.875rem;color:#64748B;margin-bottom:32px;">[TAGLINE TIER]</p>
      <ul style="list-style:none;padding:0;margin:0 0 32px;display:flex;flex-direction:column;gap:12px;">
        <li style="font-size:0.875rem;color:#94A3B8;display:flex;gap:10px;"><span style="color:#4A9B7A;">✓</span><span><strong>[FEATURE]</strong></span></li>
        <!-- Ripeti per ogni feature -->
      </ul>
      <button style="width:100%;padding:14px;font-size:0.875rem;font-weight:600;color:#CBD5E1;background:transparent;border:1px solid rgba(148,163,184,0.4);border-radius:2px;cursor:pointer;transition:all 0.3s;" onmouseover="this.style.borderColor='#94A3B8'" onmouseout="this.style.borderColor='rgba(148,163,184,0.4)'">inizia gratis</button>
    </div>

    <!-- Tier PRO (highlighted — MOST POPULAR) -->
    <div style="background:rgba(227,200,120,0.05);border:1px solid rgba(227,200,120,0.3);border-radius:4px;padding:40px 32px;position:relative;transform:scale(1.02);">
      <div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#E3C878,#D4AF37);color:#020202;font-size:0.6875rem;font-weight:700;padding:4px 16px;border-radius:20px;letter-spacing:0.1em;white-space:nowrap;">più scelto</div>
      <div style="font-family:'Cinzel',serif;font-size:0.75rem;letter-spacing:0.2em;text-transform:uppercase;color:#E3C878;margin-bottom:16px;">pro</div>
      <div style="display:flex;align-items:baseline;gap:4px;margin-bottom:8px;">
        <span id="price-pro" style="font-family:'Cinzel',serif;font-size:2.5rem;font-weight:700;color:#E3C878;">[PREZZO]</span>
        <span style="color:#94A3B8;font-size:0.875rem;">/mese</span>
      </div>
      <p style="font-size:0.875rem;color:#94A3B8;margin-bottom:32px;">[TAGLINE TIER PRO]</p>
      <ul style="list-style:none;padding:0;margin:0 0 32px;display:flex;flex-direction:column;gap:12px;">
        <li style="font-size:0.875rem;color:#CBD5E1;display:flex;gap:10px;"><span style="color:#E3C878;">✓</span><span><strong>tutto di starter, più:</strong></span></li>
        <!-- Feature pro -->
      </ul>
      <button style="width:100%;padding:14px;font-size:0.875rem;font-weight:700;color:#020202;background:linear-gradient(135deg,#E3C878,#D4AF37);border:none;border-radius:2px;cursor:pointer;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform=''">inizia con pro</button>
    </div>

    <!-- Tier ENTERPRISE -->
    <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:4px;padding:40px 32px;">
      <!-- Simile a Starter ma con "contattaci" come CTA -->
    </div>

  </div>
</div>

<script>
var isAnnual = false;
var prices = {
  starter: { monthly: '[PM_STARTER]', annual: '[PA_STARTER]' },
  pro:     { monthly: '[PM_PRO]',     annual: '[PA_PRO]' },
  ent:     { monthly: '[PM_ENT]',     annual: '[PA_ENT]' }
};
function togglePricing() {
  isAnnual = !isAnnual;
  document.getElementById('toggle-dot').style.transform = isAnnual ? 'translateX(22px)' : '';
  document.getElementById('toggle-monthly').style.color = isAnnual ? '#94A3B8' : '#E2E8F0';
  document.getElementById('toggle-annual').style.color = isAnnual ? '#E2E8F0' : '#94A3B8';
  var key = isAnnual ? 'annual' : 'monthly';
  document.getElementById('price-starter').textContent = prices.starter[key];
  document.getElementById('price-pro').textContent = prices.pro[key];
}
</script>
```

### TESTIMONIALS SaaS (con ruolo + metriche)
```
Struttura testimonianza SaaS:
- Rating stelle
- Quote: focus su risultato misurabile ("da quando uso [NOME], i miei lead sono aumentati del 340%")
- Nome + foto (o iniziale)
- Ruolo + Azienda + (opzionale) logo azienda
- KPI raggiunto: badge visivo con numero ("[+340% leads]")
```

---

## COPY RULES SAAS

### Headline (outcome-focused, non feature)
```
❌ "la piattaforma con 50+ funzionalità di automazione"
✓  "automatizza il 80% del tuo supporto clienti in 10 minuti"

❌ "software CRM completo"
✓  "chiudi il doppio dei deals senza assumere un singolo venditore"
```

### CTA Labels
```
Primarie:
✓ "start free trial"
✓ "inizia gratis — nessuna carta richiesta"
✓ "prova gratis per 14 giorni"

Secondarie:
✓ "guarda una demo di 3 minuti"
✓ "vedi come funziona"
```

### Micro-copy rassicurante (obbligatorio vicino ogni CTA)
```
✓ "no credit card required"
✓ "setup in 2 minutes"
✓ "cancel anytime, no questions"
✓ "free forever plan available"
```

---

## MICRO-ANIMAZIONI SPECIFICHE SAAS

### Tab switcher features per use-case
```html
<div style="display:flex;gap:8px;margin-bottom:32px;justify-content:center;flex-wrap:wrap;">
  <button onclick="switchTab('marketing')" id="tab-marketing" style="padding:10px 20px;font-size:0.875rem;border-radius:20px;border:1px solid rgba(227,200,120,0.5);background:rgba(227,200,120,0.1);color:#E3C878;cursor:pointer;transition:all 0.3s;">marketing</button>
  <button onclick="switchTab('sales')" id="tab-sales" style="padding:10px 20px;font-size:0.875rem;border-radius:20px;border:1px solid rgba(255,255,255,0.1);background:transparent;color:#94A3B8;cursor:pointer;transition:all 0.3s;">sales</button>
  <button onclick="switchTab('support')" id="tab-support" style="padding:10px 20px;font-size:0.875rem;border-radius:20px;border:1px solid rgba(255,255,255,0.1);background:transparent;color:#94A3B8;cursor:pointer;transition:all 0.3s;">support</button>
</div>

<div id="content-marketing" class="tab-content"><!-- contenuto --></div>
<div id="content-sales"    class="tab-content" style="display:none;"><!-- contenuto --></div>
<div id="content-support"  class="tab-content" style="display:none;"><!-- contenuto --></div>

<script>
function switchTab(name) {
  document.querySelectorAll('.tab-content').forEach(function(el){el.style.display='none';});
  document.getElementById('content-'+name).style.display = 'block';
  ['marketing','sales','support'].forEach(function(t){
    var btn = document.getElementById('tab-'+t);
    if(t===name){
      btn.style.background='rgba(227,200,120,0.1)';
      btn.style.borderColor='rgba(227,200,120,0.5)';
      btn.style.color='#E3C878';
    } else {
      btn.style.background='transparent';
      btn.style.borderColor='rgba(255,255,255,0.1)';
      btn.style.color='#94A3B8';
    }
  });
}
</script>
```

---

## DEVICE FRAME MOCKUP (UI Screenshot)

```html
<!-- Browser frame per screenshot UI -->
<div style="border-radius:8px;overflow:hidden;box-shadow:0 40px 80px rgba(0,0,0,0.8);border:1px solid rgba(255,255,255,0.1);">
  <!-- Browser chrome -->
  <div style="background:#1a1a1a;padding:12px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);">
    <div style="width:12px;height:12px;border-radius:50%;background:#C0505A;"></div>
    <div style="width:12px;height:12px;border-radius:50%;background:#D4AF37;"></div>
    <div style="width:12px;height:12px;border-radius:50%;background:#4A9B7A;"></div>
    <div style="flex:1;background:rgba(255,255,255,0.05);border-radius:4px;padding:4px 12px;font-size:0.75rem;color:#374151;margin:0 16px;">[URL PLACEHOLDER]</div>
  </div>
  <!-- Screenshot UI (div placeholder con colore brand) -->
  <div style="background:linear-gradient(135deg,[COLORE-BG-APP],[COLORE-BG-APP-ALT]);height:300px;display:flex;align-items:center;justify-content:center;">
    <span style="color:#374151;font-size:0.875rem;">[UI SCREENSHOT / SCHERMATA APP]</span>
  </div>
</div>
```
