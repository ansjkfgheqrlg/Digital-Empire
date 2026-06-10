# K09-category-ebook

> Source: File system (`SKILL & Agenti\SKILL\Website Creator\knowledge\K09-category-ebook.md`)
> Collected: 2026-05-06
> Published: Unknown

# K09 — CATEGORIA: EBOOK / GUIDE / PDF / CORSI DIGITALI

> Struttura, stili, copy e pattern specifici per prodotti digitali scaricabili. Priorità massima — la categoria più comune.

---

## STRUTTURA SEZIONI (ordine ottimale — ricerca su 60+ siti)

```
1. [NAV]           Nav sticky (opzionale, solo se multi-page)
2. [HERO]          Hero — headline + beneficio + CTA + social proof
3. [DIVIDER]       InclinedStrip
4. [NUMBERS]       Social Proof Numbers (opzionale ma efficace)
5. [DIVIDER]       LuxArc (dark → light)
6. [BENEFITS]      Benefits — 3-7 punti cardine del prodotto
7. [DIVIDER]       LuxV (light → dark) se benefits è light
8. [MOCKUP]        Product Mockup 3D — preview del prodotto
9. [DIVIDER]       LuxCurve (sezione successiva curva)
10. [INSIDE]       What's Inside / Indice — cosa troveranno dentro
11. [DIVIDER]      InclinedStrip
12. [AUTHOR]       Author Bio — credenziali + storia + prova autorità
13. [DIVIDER]      LuxArc
14. [TESTIMONIALS] Testimonianze — 2-3 recensioni reali o verosimili
15. [DIVIDER]      LuxV
16. [GUARANTEE]    Garanzia — rimborso 30 giorni, zero rischio
17. [DIVIDER]      InclinedStrip
18. [BONUS]        Bonus (opzionale) — valore aggiunto con countdown
19. [CTA]          CTA Principale — prezzo + bottone + urgency
20. [DIVIDER]      LuxArc
21. [FAQ]          FAQ — 5-7 domande frequenti
22. [FOOTER]       Footer
```

---

## STILI PER SOTTO-CATEGORIA

### Trading / Finanza / Business (PRIORITÀ MASSIMA)
- **Palette:** PALETTE 1 (oro/silver) — `#E3C878`, `#020202`, `#94A3B8`
- **Sfondo dominante:** `#020202` (nero profondo)
- **Interrupts:** `#031c16` (verde ultra-scuro) per sezione Trust/Garanzia
- **Font headline:** Cinzel sempre
- **Tono:** Autoritativo, esclusivo, risultati specifici ("ha guadagnato €47.000 in 8 mesi")
- **Keywords copy:** "insider", "metodo", "sistema", "mercati", "rendimento", "gestione del rischio"

### Fitness / Wellness / Nutrizione
- **Palette:** PALETTE 2 (verde silver) o PALETTE 9 (teal)
- **Sfondo dominante:** scuro con sfumature verdi
- **Interrupts:** beige caldo `#E8E0D0`
- **Tono:** Energico, trasformativo, motivante ("12 settimane per cambiare tutto")
- **Keywords copy:** "trasformazione", "programma", "protocollo", "risultati visibili", "metodo scientifico"

### Educational / How-To / Skill Building
- **Palette:** PALETTE 5 (blu silver) o PALETTE 1 (oro)
- **Sfondo:** Mix light/dark con sezioni chiare più frequenti
- **Tono:** Amichevole, strutturato, passo-passo
- **Keywords copy:** "imparerai", "step-by-step", "anche se parti da zero", "il metodo", "framework"

### Premium Lifestyle / Personal Development
- **Palette:** PALETTE 12 (burgundy) o PALETTE 7 (rosa silver)
- **Sfondo:** Crema + silver, whitespace generoso
- **Tono:** Aspirazionale, intimista, quasi luxury
- **Keywords copy:** "esclusivo", "selezionato", "comunità", "mindset", "lifestyle"

---

## SEZIONI SPECIFICHE — DETTAGLIO

### HERO EBOOK
```
Struttura:
- Eyebrow: "[CATEGORIA] · [ANNO]" o "bestseller · [NICHE]"
- Headline: power word + beneficio + target (max 10 parole)
  Esempio: "il sistema che ha fatto guadagnare 47.000€ a 1.200 trader italiani"
- Subheadline: trasformazione specifica (max 15 parole)
  Esempio: "impara il metodo esatto per operare sui mercati anche con 500€ di capitale"
- CTA primaria: "scarica ora a [PREZZO]" o "ottieni accesso immediato"
- Micro-copy sotto CTA: "oltre [N] lettori · [RATING] stelle · garanzia 30 giorni"
- Elemento visivo: mockup prodotto (cover ebook) a destra o centro floating
```

### BENEFITS (3-7 punti)
```
Struttura per ogni benefit:
- Icona o numero (1, 2, 3...)
- Titolo benefit: conciso, outcome-focused (max 5 parole)
- Descrizione: 2-3 frasi, almeno 1 strong
- (opzionale) Micro-proof: "come ha fatto [NOME] a [RISULTATO]"

Esempi titoli:
✓ "guadagna anche quando dormi"
✓ "zero esperienza richiesta"
✓ "risultati in 30 giorni o rimborso"
✓ "accesso a vita, aggiornamenti inclusi"
```

### PRODUCT MOCKUP 3D
```html
<!-- Cover ebook con effetto 3D CSS -->
<div style="perspective:1000px; width:200px; margin:0 auto; animation:float 6s ease-in-out infinite;">
  <div style="
    position:relative;
    width:200px; height:280px;
    transform:rotateY(-15deg) rotateX(5deg);
    transform-style:preserve-3d;
    filter:drop-shadow(20px 30px 40px rgba(0,0,0,0.7)) drop-shadow(0px 0px 30px rgba(212,175,55,0.2));
  ">
    <!-- Cover frontale -->
    <div style="
      position:absolute; inset:0;
      background:linear-gradient(135deg,[COLORE-PRIMARIO],[COLORE-SECONDARIO]);
      border-radius:4px 0 0 4px;
      display:flex; flex-direction:column; justify-content:flex-end; padding:24px;
      overflow:hidden;
    ">
      <!-- grain sul mockup -->
      <div style="position:absolute;inset:0;background-image:url('https://grainy-gradients.vercel.app/noise.svg');filter:contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%);opacity:0.35;mix-blend-mode:overlay;pointer-events:none;"></div>
      <div style="position:relative;z-index:5;">
        <div style="font-family:'Cinzel',serif;font-size:1.1rem;color:#E3C878;font-weight:700;line-height:1.2;margin-bottom:8px;">[TITOLO EBOOK]</div>
        <div style="font-size:0.6875rem;color:#94A3B8;font-weight:600;letter-spacing:0.1em;">[AUTORE]</div>
      </div>
    </div>
    <!-- Spessore libro (lato destro) -->
    <div style="
      position:absolute; right:-12px; top:4px; bottom:4px; width:16px;
      background:linear-gradient(90deg,#8E9BAF,#CBD5E1);
      border-radius:0 2px 2px 0;
      transform:rotateY(90deg) translateZ(-4px);
    "></div>
  </div>
</div>
```

### WHAT'S INSIDE / INDICE
```
Struttura:
- Titolo sezione: "cosa troverai dentro" o "il contenuto completo"
- Per ogni capitolo/modulo:
  - Numero capitolo (stile Cinzel)
  - Titolo capitolo (outcome, non descrittivo)
  - 2-3 bullet takeaway (cosa impara specificatamente)
  - Badge "BONUS" se capitolo extra

Formato migliore: accordion o grid 2 colonne
```

### AUTHOR BIO
```
Struttura (2 colonne su desktop, stack su mobile):
- Colonna sx: foto autore (placeholder se non disponibile)
- Colonna dx:
  - Nome (font Cinzel)
  - Credenziali specifiche (non generiche: "ex trader Goldman Sachs, +15 anni")
  - Story: "ho perso 23.000€ prima di scoprire questo" — vulnerabilità + soluzione
  - Proof: loghi media, certificazioni, numeri
  - Citazione personale (Playfair Display italic)
```

### GUARANTEE SECTION
```html
<div style="
  background:rgba(74,155,122,0.08);
  border:1px solid rgba(74,155,122,0.25);
  border-radius:4px;
  padding:40px;
  text-align:center;
  max-width:600px;
  margin:0 auto;
">
  <!-- Badge garanzia -->
  <div style="width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,#4A9B7A,#031c16);border:2px solid #4A9B7A;display:flex;align-items:center;justify-content:center;margin:0 auto 24px;font-size:2rem;">🛡️</div>
  <h3 style="font-family:'Cinzel',serif;font-size:1.5rem;color:#E2E8F0;margin-bottom:16px;">garanzia rimborso 30 giorni</h3>
  <p style="color:#94A3B8;line-height:1.7;">
    se entro <strong>30 giorni</strong> non sei soddisfatto al 100%, ti rimborsiamo l'intero importo.
    <strong>zero domande, zero complicazioni</strong> — basta una email.
  </p>
</div>
```

### BONUS SECTION
```
Struttura:
- Titolo: "bonus esclusivi inclusi" o "ottieni anche questi bonus"
- Timer countdown se offerta limitata
- Per ogni bonus:
  - Icona/immagine
  - Titolo bonus
  - Valore indicato: "valore: €[X]" (barrato)
  - Breve descrizione (1 riga)
- Totale valore bonus vs prezzo finale
```

---

## REGOLE COPY PER EBOOK

### Formula Headline (AIDA adattata)
```
[Power Word] + [Beneficio Specifico] + [Target/Condizione]

Esempi:
"il metodo che ha trasformato 2.300 persone in investitori profittevoli"
"come guadagnare 5.000€ al mese trading anche con un lavoro a tempo pieno"
"la guida definitiva per perdere 10kg in 12 settimane senza rinunciare al cibo"
```

### Formula Subheadline
```
"impara [AZIONE SPECIFICA] per [RISULTATO MISURABILE] anche se [OBIEZIONE PRINCIPALE]"

Esempi:
"impara a operare sui futures per generare 500-1.500€ al mese anche se non hai mai fatto trading"
"scopri il protocollo nutrizionale per perdere 1kg a settimana senza fare cardio o eliminare i carboidrati"
```

### CTA Labels (mai generiche)
```
✓ "scarica subito il tuo accesso"
✓ "ottieni accesso immediato per [PREZZO]"
✓ "inizia la trasformazione oggi"
✓ "sì, voglio [BENEFICIO PRINCIPALE]"
✗ "compra ora" (troppo generico)
✗ "clicca qui" (nessun valore)
✗ "acquista" (solo transazionale)
```

### Social Proof Quantificato
```
Usa sempre numeri specifici (credibili):
✓ "oltre 12.847 lettori soddisfatti"
✓ "4.8 stelle su 5 (847 recensioni verificate)"
✓ "usato da trader in 47 paesi"
✗ "migliaia di clienti" (vago, non credibile)
✗ "ottima valutazione" (non quantificato)
```

---

## PATTERN PSICOLOGICI — EBOOK

### Urgency
```html
<!-- Timer countdown -->
<div id="countdown" style="font-family:'Cinzel',serif;font-size:2rem;color:#E3C878;text-align:center;letter-spacing:0.1em;"></div>
<p style="font-size:0.8125rem;color:#64748B;text-align:center;">il prezzo scontato scade tra</p>

<script>
(function(){
  function updateTimer(){
    var end = new Date();
    end.setHours(23,59,59,999); // scade a mezzanotte
    var now = new Date();
    var diff = end - now;
    var h = Math.floor(diff/3600000);
    var m = Math.floor((diff%3600000)/60000);
    var s = Math.floor((diff%60000)/1000);
    document.getElementById('countdown').textContent =
      pad(h) + ':' + pad(m) + ':' + pad(s);
  }
  function pad(n){ return n < 10 ? '0'+n : n; }
  updateTimer();
  setInterval(updateTimer, 1000);
})();
</script>
```

### Scarcity
```html
<p style="color:#C0505A;font-size:0.875rem;text-align:center;margin-top:8px;">
  ⚠ <strong>attenzione:</strong> questo prezzo speciale è garantito solo per le prossime [N] copie
</p>
```

### Reciprocity
```html
<!-- Preview primo capitolo -->
<div style="background:rgba(227,200,120,0.05);border:1px dashed rgba(227,200,120,0.3);padding:32px;border-radius:4px;">
  <p style="font-size:0.75rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:#E3C878;margin-bottom:12px;">anteprima gratuita — capitolo 1</p>
  <p style="color:#CBD5E1;font-size:0.9375rem;line-height:1.8;">[TESTO PRIMO PARAGRAFO DEL CAPITOLO 1]...</p>
  <button style="margin-top:20px;font-size:0.8125rem;color:#E3C878;background:none;border:1px solid rgba(227,200,120,0.3);padding:10px 24px;border-radius:2px;cursor:pointer;">leggi il capitolo completo →</button>
</div>
```

---

## MOBILE-SPECIFIC (ebook)

```css
@media (max-width: 768px) {
  /* Mockup più piccolo */
  .book-mockup { transform: scale(0.8); }

  /* Benefits in lista verticale */
  .benefits-grid { grid-template-columns: 1fr; }

  /* CTA full-width sticky bottom */
  .cta-sticky-mobile {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    padding: 12px 16px;
    background: rgba(2,2,2,0.95);
    border-top: 1px solid rgba(227,200,120,0.2);
    z-index: 90;
    display: flex;
    gap: 12px;
    align-items: center;
    justify-content: space-between;
  }
}
```
