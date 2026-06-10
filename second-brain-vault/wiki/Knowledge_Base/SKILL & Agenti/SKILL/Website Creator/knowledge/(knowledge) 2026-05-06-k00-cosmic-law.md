# K00-cosmic-law
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Website Creator > knowledge]]

## Content

# K00 — LA LEGGE COSMICA: SILVER MIXING ASSOLUTO

> Questo è il fondamento di tutto il sistema. Ogni agente, ogni skill, ogni sezione HTML prodotta da questo sistema deve rispettare questa legge senza eccezioni.

---

## LA LEGGE

**Non esistono colori puri in questi siti.**

Ogni colore è un colore **argentizzato**. Non "rosso e argento" — ma "rosso argentato". Non "verde e argento" — ma "verde argentato". Il colore diventa silver, non si affianca all'argento. Questa è la differenza tra lusso e kitsch.

L'occhio umano percepisce i colori puri come sintetici, economici, aggressivi. I colori argentizzati sembrano metallici, premium, sofisticati — come le auto di lusso, la gioielleria, i materiali pregiati.

---

## ALGORITMO DI ARGENTIZZAZIONE

Dato qualsiasi colore hex, per ottenere la versione argentizzata:

### Pseudocodice
```
1. Converti hex → HSL
2. Saturazione: S = S - (S × 0.40)   // abbassa del 40%
3. Hue: H = H + (215 - H) × 0.25     // sposta verso 215° (cool silver zone)
4. Lightness: invariata (± 5% per bilanciamento)
5. Blend 35% con #94A3B8 (cool silver base) in modalità normale
6. Risultato: colore mantiene identità ma ha componente metallica fredda
```

### In CSS (tecnica gradient blend)
```css
/* Tecnica 1: gradient con silver overlay */
background: linear-gradient(
  135deg,
  [colore-argentizzato] 0%,
  #94A3B8 50%,
  [colore-argentizzato] 100%
);

/* Tecnica 2: variabile CSS argentizzata */
:root {
  --color-primary: [hex-argentizzato];
  --silver-base: #94A3B8;
  --silver-light: #E2E8F0;
  --silver-dark: #64748B;
}

/* Tecnica 3: mix-blend overlay per aggiungere silver a sezione */
.silver-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(148,163,184,0.15), transparent);
  mix-blend-mode: overlay;
  pointer-events: none;
}
```

---

## TABELLA COLORI: PURO → ARGENTIZZATO

| Colore | Puro (VIETATO) | Argentizzato (APPROVATO) | Note |
|--------|----------------|--------------------------|------|
| Oro | `#FFD700` | `#E3C878` | Freddo, muted, lusso |
| Oro ricco | `#FFC200` | `#D4AF37` | Classico oro moneta |
| Verde | `#00FF00` | `#4A9B7A` | Verde muted argentato |
| Verde deep | `#008000` | `#031c16` | Quasi nero-verde-silver |
| Verde medium | `#006400` | `#2D6A4F` | Forest silver |
| Viola | `#8B00FF` | `#7B6FA8` | Viola desaturato silver |
| Viola medium | `#6600CC` | `#6B5B95` | Iris argentato |
| Rosso | `#FF0000` | `#C0505A` | Rosso muted con grigio-silver |
| Rosso deep | `#CC0000` | `#9B3D45` | Borgogna argentato |
| Blu | `#0000FF` | `#4A7FB5` | Blu freddo argentato |
| Blu scuro | `#003366` | `#0f2e4a` | Navy argentato (Agency) |
| Blu profondo | `#001A33` | `#1a3a5c` | Deep navy silver |
| Cyan | `#00FFFF` | `#4A9DAB` | Cyan muted argentato |
| Rosa | `#FF69B4` | `#C48A9A` | Rosa muted argentato |
| Arancione | `#FF6600` | `#C47A3A` | Terracotta argentata |
| Teal | `#009688` | `#3D7A72` | Teal silver |

---

## COLORI VIETATI (MAI USARE)

```
❌ #FF0000  (rosso puro — saturazione 100%)
❌ #00FF00  (verde puro — saturazione 100%)
❌ #0000FF  (blu puro — saturazione 100%)
❌ #FFFF00  (giallo puro)
❌ #FF00FF  (magenta puro)
❌ #00FFFF  (cyan puro)
❌ #FF6600  (arancione puro)
❌ Qualsiasi colore con saturazione HSL > 70% senza blend silver
```

**Perché sono vietati:** I colori puri a saturazione massima sembrano plastici, economici, da sito anni 2000. Distruggono l'estetica premium in un millisecondo.

---

## PALETTE AGENCY (FONTE DI VERITÀ)

Questi sono i colori esatti estratti dal sito Agency — il benchmark minimo di qualità:

```css
/* Oro argentato */
--gold-primary: #E3C878;   /* oro principale, caldo ma muted */
--gold-rich: #D4AF37;      /* oro classico, moneta */
--gold-bright: #FFD700;    /* SOLO per gradient midpoint, mai solido */

/* Silver */
--silver-cool: #94A3B8;    /* argento freddo base */
--silver-light: #E2E8F0;   /* argento chiaro */
--silver-medium: #CBD5E1;  /* argento medio */
--silver-dark: #64748B;    /* argento scuro */

/* Sfondi scuri */
--bg-black: #020202;       /* nero base */
--bg-screen: #000000;      /* nero assoluto */
--bg-near-black: #0a0a0a;  /* quasi nero */

/* Verdi argentati */
--green-deep: #031c16;     /* verde quasi nero */
--green-emerald: #026c4a;  /* verde smeraldo argentato */

/* Blu argentati */
--blue-deep: #0f2e4a;      /* blu profondo argentato */
--blue-darkest: #020617;   /* blu quasi nero */

/* Neutri chiari */
--beige: #DCD8CF;          /* beige argentato per sezioni chiare */
--white-warm: #F8F6F2;     /* bianco caldo */
```

---

## GRADIENT METALLIC STANDARD

Questo gradient è condiviso da tutti i divisori SVG e da molte decorazioni:

```css
--gradient-metallic: linear-gradient(
  90deg,
  #94A3B8 0%,
  #E2E8F0 20%,
  #E3C878 45%,
  #FFFFFF 50%,
  #E3C878 55%,
  #E2E8F0 80%,
  #94A3B8 100%
);
```

Usalo per: bordi SVG dei divisori, separatori decorativi, highlight su card.

---

## ESEMPI CSS GRADIENT ARGENTIZZATI PER CATEGORIA COLORE

### Oro (default Agency — qualsiasi sito luxury)
```css
background: linear-gradient(135deg, #E3C878 0%, #94A3B8 50%, #D4AF37 100%);
color: #E3C878;
border-color: rgba(227, 200, 120, 0.3);
```

### Verde argentato (wellness, finanza, natura)
```css
background: linear-gradient(135deg, #031c16 0%, #4A9B7A 50%, #2D6A4F 100%);
color: #4A9B7A;
border-color: rgba(74, 155, 122, 0.3);
```

### Viola argentato (tech, creatività, premium)
```css
background: linear-gradient(135deg, #2D1B4E 0%, #7B6FA8 50%, #6B5B95 100%);
color: #7B6FA8;
border-color: rgba(123, 111, 168, 0.3);
```

### Rosso argentato (urgency, salute, energia)
```css
background: linear-gradient(135deg, #2D0A0F 0%, #C0505A 50%, #9B3D45 100%);
color: #C0505A;
border-color: rgba(192, 80, 90, 0.3);
```

### Blu argentato (tech, finanza, SaaS)
```css
background: linear-gradient(135deg, #0f2e4a 0%, #4A7FB5 50%, #3D6E9E 100%);
color: #4A7FB5;
border-color: rgba(74, 127, 181, 0.3);
```

---

## VERIFICA RAPIDA

Prima di consegnare qualsiasi codice HTML, scansiona tutti i `color:`, `background:`, `border-color:`, `fill:`, `stroke:` e chiediti:

1. Questo hex ha saturazione HSL > 70%? → ARGENTIZZALO
2. Questo colore è uno dei 6 colori primari puri? → VIETATO, cambia
3. Sento il "plastico" guardando il colore? → Non è abbastanza argentizzato

**La Legge Cosmica non ha eccezioni.** Nemmeno per un singolo elemento.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Saas|Saas Area]]
