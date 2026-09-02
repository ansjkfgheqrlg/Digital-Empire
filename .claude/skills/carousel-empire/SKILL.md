---
name: carousel-empire
description: "Genera caroselli Instagram branded per Digital Empire Agency. Produce 7 PNG 1080x1350 piu caption e hashtag, con identita, positioning e tone of voice DE gia applicati. Usala quando l'utente scrive crea carosello, carousel IG, slide instagram, contenuto per IG, post carosello, o chiede un carosello su un argomento specifico."
---

# Carousel Empire — Generatore Caroselli IG

## Identità DE
- **Handle:** @digitalempireagency.e
- **Prodotti:** Outreach Factory · Content Factory · Second Brain · The Engine Room (bundle)
- **Target:** Creator, Coach, Agency Owner, Business Owner — prodotti/servizi high ticket già sul mercato
- **Positioning:** Zero canoni mensili. Codice tuo per sempre. AI implementations installate in 7 giorni.
- **Tone:** Diretto, pragmatico, bold. Zero fuffa. Zero promesse campate in aria. Dati e meccaniche concrete.
- **Anti-pattern:** Mai "rivoluziona il tuo business", mai emoji spammate, mai vagueness. Parla di operatività, non di sogni.

## Content Pillars (ruota tra questi)
1. **Education AI** — Come funziona X in Y passi concreti
2. **Pain Point Attack** — Il problema operativo specifico che brucia tempo/soldi
3. **Framework** — Metodi DE (APSOC, come vendere AI implementations, come strutturare outreach)
4. **Proof / Social** — Numeri, workflow reali, prima/dopo
5. **Differenziazione** — Perché implementazioni AI > servizi classici (landing page, social management)
6. **CTA Diretta** — Prenota call / Commenta AI / Scrivi in DM

---

## Workflow Completo

### Step 1 — Input
Se il topic non è fornito, chiedi:
- Angolo/topic del carosello (es. "outreach a freddo", "content automation", "vendere AI a coach")
- Prodotto da promuovere (Outreach Factory / Content Factory / Second Brain / General DE)
- Pillar preferito (o sceglilo tu in base al topic)

### Step 2 — Genera carousel_content.json

Crea il file nella cartella output. Rispetta **esattamente** questo schema JSON:

```json
{
  "slug": "slug-kebab-case-del-topic",
  "date": "YYYY-MM-DD",
  "product": "Nome Prodotto o General",
  "pillar": "Nome Pillar",
  "slides": [
    {
      "type": "hook",
      "tag": "⚡ LABEL BREVE",
      "headline": "Max 6 parole. Punch.",
      "subheadline": "Espandi in 90-120 caratteri. Beneficio concreto.",
      "accent_words": ["parola1"]
    },
    {
      "type": "problem",
      "tag": "IL PROBLEMA",
      "headline": "Cosa sta andando storto",
      "items": [
        "Pain point 1 — concreto e specifico",
        "Pain point 2 — concreto e specifico",
        "Pain point 3 — concreto e specifico"
      ]
    },
    {
      "type": "solution",
      "tag": "LA SOLUZIONE",
      "headline": "Nome Prodotto — one liner",
      "subheadline": "Cosa fa in una frase",
      "benefits": [
        {"title": "Beneficio 1", "desc": "Spiegazione breve 10-15 parole"},
        {"title": "Beneficio 2", "desc": "Spiegazione breve 10-15 parole"},
        {"title": "Beneficio 3", "desc": "Spiegazione breve 10-15 parole"}
      ]
    },
    {
      "type": "how_it_works",
      "tag": "COME FUNZIONA",
      "headline": "3 step, zero complessità",
      "steps": [
        {"title": "Step 1", "desc": "Azione → risultato in 15 parole max"},
        {"title": "Step 2", "desc": "Azione → risultato in 15 parole max"},
        {"title": "Step 3", "desc": "Azione → risultato in 15 parole max"}
      ]
    },
    {
      "type": "proof",
      "tag": "I NUMERI",
      "headline": "Cosa ottieni, in cifre",
      "subheadline": "Contesto breve opzionale",
      "stats": [
        {"number": "300+", "label": "email/giorno inviate"},
        {"number": "7gg", "label": "setup completo"},
        {"number": "€0", "label": "canoni mensili"},
        {"number": "100%", "label": "codice tuo"}
      ]
    },
    {
      "type": "differentiator",
      "tag": "PERCHÉ NOI",
      "headline": "Non un'agenzia. Un sistema.",
      "subheadline": "Opzionale — frase di chiusura",
      "items": [
        "Zero canoni mensili — paghi una volta",
        "Codice tuo al 100% — nessun vendor lock",
        "Setup in 7 giorni su server tuoi",
        "Solo costi API OpenAI (pochi centesimi)",
        "Supporto 90 giorni post-consegna"
      ]
    },
    {
      "type": "cta",
      "tag": "PROSSIMO PASSO",
      "headline": "Hai un'operatività da scalare?",
      "action": "Commenta AI",
      "sub": "Ti mando i dettagli in DM"
    }
  ]
}
```

**Regole contenuto:**
- Headline hook: max 6 parole, punch massimo. Usa cifre se possibile.
- Nessuna slide supera 120 parole di testo totale
- accent_words = max 2 parole che diventeranno rosse (#FF3D00)
- Stat numbers: brevi (300+, €0, 7gg, 100%) — no decimali
- Items differentiator: max 5, max 8 parole ciascuno

### Step 3 — Prepara cartella e installa dipendenze

```bash
# Crea cartella output
mkdir -p "C:/Users/Utente/.claude/skills/carousel-empire/output/YYYY-MM-DD-[slug]"

# Installa dipendenze (solo prima volta)
pip install playwright -q
python -m playwright install chromium --quiet
```

### Step 4 — Esegui lo script

```bash
python "C:/Users/Utente/.claude/skills/carousel-empire/scripts/generate_carousel.py" \
  "C:/Users/Utente/.claude/skills/carousel-empire/output/YYYY-MM-DD-[slug]/carousel_content.json"
```

Lo script:
1. Legge il JSON
2. Genera HTML brandizzato per ogni slide
3. Screenshot con Playwright a 1080×1350
4. Salva `slide-01.png` … `slide-07.png` + file HTML debug

### Step 5 — Self-Check Visivo (OBBLIGATORIO)

Leggi ogni PNG generato con visione nativa. Checklist per ogni slide:
- [ ] Testo non taglia i bordi o overflow
- [ ] Logo "DIGITAL EMPIRE" visibile top-left (EMPIRE in arancione #FF3D00)
- [ ] Counter "N/7" visibile top-right
- [ ] Handle @digitalempireagency.e bottom-left
- [ ] Tag/label visibile se presente
- [ ] Accent words in arancione
- [ ] Stat numbers in arancione/gold
- [ ] Background #0A0A0A (nero profondo)
- [ ] Leggibile simulando visualizzazione mobile (pollice copre 20% bottom)
- [ ] Nessun testo sovrapposto

**Se errori trovati:**
1. Identifica slide e problema
2. Correggi `carousel_content.json` (testo più corto, parole ridotte, etc.)
3. Ri-esegui script per solo quella slide o tutto
4. Re-check

### Step 6 — Genera Caption + Hashtag

**Formato caption:**
```
[HOOK — identica headline slide 1]

[Corpo 3-4 righe: espande il problema + soluzione, tono diretto]

[CTA] → Commenta AI e ti mando [cosa ricevono]

—
[3-4 emoji pertinenti come separatore visivo]
```

**Hashtag (25 totali, mix):**
- Alto volume (5): #intelligenzaartificiale #automazione #marketingdigitale #agenziamarketing #businessonline
- Medio volume (10): #agenziaia #outreachmarketing #contenutoai #digitalmarketing #agenziadigitale #freelanceitalia #coacheitalia #infobusiness #scalabilità #implementazioneai
- Basso/niche (10): #outreachautomation #contentfactory #outreachfactory #digitalempire #aiagency #workflowai #emailmarketing #leadgeneration #automatizzarebusiness #agenziacro

### Step 7 — Report Finale

```
✅ Carousel generato: [topic]
📁 Cartella: [path]
🖼️ Slide: slide-01.png ... slide-07.png
📝 Caption: [caption completa]
#️⃣ Hashtag: [lista 25]
💡 3 varianti hook alternative:
   A) ...
   B) ...
   C) ...
```

---

## Modalità Alternativa — Stile AI-Generativo con Visual Anchor

Il workflow sopra (Step 2-4) usa HTML + Playwright con template fisso: stessa identica composizione grafica ogni volta, cambia solo il testo. Deterministico e brand-safe — resta la modalità di **default** per il 90% dei casi. Per contenuti che richiedono uno stile illustrato/collage (texture, scarabocchi, asset grafici non riproducibili in HTML/CSS) esiste un secondo pattern, validato esternamente, da usare come ramo alternativo allo Step 2 solo su richiesta esplicita.

### Il principio: slide-per-slide, non carosello intero

I modelli di image gen (Gemini/Nano Banana, GPT Image) generano una sola immagine alla volta. Chiedere un carosello intero da 6-8 slide in un solo prompt produce slide incoerenti tra loro, ognuna "inventata da zero" senza consapevolezza delle altre. La soluzione: generare **una slide alla volta**, non l'intero carosello in un colpo solo (fonte: JdAQzAcWR6k — Artem Novitckii, 0:41-1:13).

### Il Visual Anchor

La **slide 1** (hook/cover), una volta generata bene, diventa l'**immagine di riferimento** (visual anchor) allegata a ogni prompt delle slide successive. Ogni nuova slide è vincolata a rispettarne tipografia, colori, texture e mood — è il passo a cui dedicare più tempo (50% del ciclo secondo la fonte), perché definisce lo stile dell'intero carosello (fonte: JdAQzAcWR6k — Artem Novitckii, 1:14-1:29).

### I due prompt master (riusabili, con placeholder)

**Prompt Slide 1 (hook/cover) — integrale:**
```
Create 5 different versions of slide 1 for an Instagram carousel.

Use the attached references as visual inspiration only.

Borrow from the references:
- typography hierarchy
- spacing
- colour treatment
- texture
- visual pacing
- layout logic

Do not copy:
- exact text
- exact branding
- exact compositions

Carousel topic:
[TOPIC]

Slide type:
Cover / hook slide.

Slide goal:
Stop the scroll and make people want to swipe.

Text for slide 1:
[INSERT TEXT HERE]

Visual direction:
[DESCRIBE WHAT SHOULD BE ON THE SLIDE]

Style direction:
Make it feel raw, editorial, clear, useful, and highly readable. It should
feel designed, but not overly polished or corporate.

Format:
4:5 vertical Instagram carousel slide, 1080x1350.

Rules:
- keep the exact text only
- make all text readable
- do not add random words
- do not copy the references directly
- make each version visually distinct
```

**Prompt Slide [X] (tutte le slide dalla 2 in poi, usa la Slide 1 come visual anchor) — integrale:**
```
Create 3 versions of a slide [x] of my Instagram carousel.

Use slide 1 as the visual anchor.

Match slide 1's:
- typography feel
- spacing
- colour treatment
- texture
- raw editorial mood
- utility details
- visual hierarchy
- overall design language

Do not copy the references directly.
Do not make this slide feel like a new carousel.
It must feel like the same visual family as Slide 1.

Carousel topic:
[TOPIC]

Slide type:
[SLIDE TYPE]

Slide goal:
[SLIDE GOAL]

Text on slide:
[SLIDE TEXT]

Visual direction:
[DESCRIBE WHAT SHOULD BE ON THE SLIDE]

Format:
4:5 vertical Instagram carousel slide, 1080x1350.

Rules:
- keep the exact text only
- make all text readable
- do not add random words
- keep it visually consistent with slide 1
- one clear idea only
```

(fonte: JdAQzAcWR6k — Artem Novitckii, 3:34-4:28, prompt master integrali letti da Google Doc)

### Quando usarlo e come

- Genera ogni slide con 3-5 versioni e scegli manualmente la migliore ("pick the best of N") — non affidarti alla prima generazione.
- Il blocco "Do not copy: exact text / exact branding / exact compositions" è disciplina anti-plagio quando usi un'immagine di terzi (es. Pinterest) come riferimento stilistico iniziale — mantienilo sempre nel prompt.
- Applica comunque il Self-Check Visivo dello Step 5 a ogni slide generata con questo metodo, prima di procedere alla successiva.
- Modello consigliato: quello con supporto multi-image reference più solido disponibile nella skill `image` (vedi `image/SKILL.md`, tabella "Model Comparison") — passa la slide 1 generata come immagine allegata ad ogni prompt successivo.

---

## Esempi Contenuto per Prodotto

### Outreach Factory
- Hook: "Stai mandando email a mano nel 2026?"
- Pain: tempo perso, bassa personalizzazione, blocchi Gmail
- Solution: 300+ email/giorno personalizzate, comportamento umano reale, proxy residenziali
- Stats: 300+, €0, 7gg, 100%

### Content Factory
- Hook: "Il tuo competitor posta ogni giorno. Tu?"
- Pain: tempo produzione copy, grafiche, script video
- Solution: copy CRO, grafiche, script video, caroselli in batch → Drive
- Stats dipendono da caso d'uso

### Second Brain
- Hook: "La tua AI non ti conosce. Ecco perché sbaglia."
- Pain: ogni chat ricomincia da zero, brand voice persa, processi dispersi
- Solution: knowledge base semantica, context engineering permanente

### General DE / The Engine Room
- Hook: "Un'agency non vende servizi. Vende sistemi."
- Pain: dipendenza vendor, canoni infiniti, codice non tuo
- Solution: bundle Outreach + Content + Second Brain in 7-10 giorni

---

## Brand Invarianti (MAI cambiare)

| Elemento | Valore |
|---|---|
| Background | #0A0A0A |
| Accent (primario) | #FF3D00 |
| Gold (stat/highlight) | #FFB800 |
| Testo | #FFFFFF |
| Sottotesto | rgba(255,255,255,0.65) |
| Card bg | #141414 |
| Logo | "DIGITAL EMPIRE" — DIGITAL bianco, EMPIRE #FF3D00 |
| Handle | @digitalempireagency.e |
| Font titoli | Space Grotesk 800 |
| Font body | Inter 400 |
| Formato | 1080×1350px (4:5 IG) |
| Numero slide | 7 (max 8) |

---

## Script path
`C:/Users/Utente/.claude/skills/carousel-empire/scripts/generate_carousel.py`
