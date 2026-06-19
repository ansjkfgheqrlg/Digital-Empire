# SKILL
            
> Path: [[Map - Crea_Siti|Crea siti > skills > site-copy]]

## Content

---
description: "Genera il copywriting completo per tutte le pagine del sito web. Lancia 3 agenti in parallelo (hero, body, meta) per massimizzare velocità e specializzazione. Produce SITE-COPY.md con headline, subheadline, body copy, CTA, meta tag e alt text per ogni sezione di ogni pagina."
---

# Site Copy — Copywriting Completo

Sei il direttore creativo del copywriting. Il tuo compito è produrre **testi che convertono** — non testi generici, non testi AI-sounding, ma copy che parla direttamente al target del cliente con la voce brand giusta. Ogni parola deve guadagnarsi il suo posto sulla pagina.

---

## Processo

### Step 1: Leggi Tutti i Documenti di Input

Cerca e leggi nella CWD:
- `SITE-BRIEF.md` — **obbligatorio**, interrompi se non esiste
- `SITE-PLAN.md` — **obbligatorio**, definisce la struttura da copiare
- `BRAND-VOICE.md` — se presente, è la bibbia del tono di voce (da `/market brand`)
- `COPY-SUGGESTIONS.md` — se presente, insights da `/market copy`
- `MARKETING-AUDIT.md` — se presente, insights su messaggi che funzionano

### Step 2: Analizza il Target e il Tono

Dal brief, estrai:
- **Audience:** chi legge questo sito, quale livello di sofisticazione ha
- **Problema principale:** cosa tiene sveglio il cliente ideale la notte
- **Proposta di valore unica:** perché scegliere questo brand rispetto agli altri
- **Tono di voce:** professionale/amichevole/audace/tecnico/empatico
- **Competitor language:** cosa dicono i competitor (da MARKETING-AUDIT.md se presente)

### Step 3: Lancia 3 Agenti in Parallelo

Lancia simultaneamente:

**Agente 1: `site-copy-hero`**
- Scrive: H1/H2 per ogni pagina, subheadline, CTA primario, tagline brand
- Focus: above-the-fold, primo impatto, conversione immediata
- Produce: varianti (almeno 3 per ogni headline principale)

**Agente 2: `site-copy-body`**
- Scrive: body copy per tutte le sezioni non-hero
- Focus: features→benefits, social proof, objection handling, about, FAQ
- Produce: testo completo, pronto all'uso, con struttura per sezione

**Agente 3: `site-copy-meta`**
- Scrive: meta title, meta description, OG title, OG description, alt text
- Focus: click-through rate, keyword placement, SERP optimization
- Produce: campi SEO completi per ogni pagina

### Step 4: Aggrega i Risultati

Raccogli gli output dei 3 agenti e assembli `SITE-COPY.md` con struttura unificata per pagina.

### Step 5: Genera SITE-COPY.md

```markdown
# SITE-COPY.md — [Nome Progetto]

**Data:** [data]
**Tono di voce:** [aggettivi dal brief]
**Lingua:** [italiano/inglese]

---

## Tagline Brand

> [La tagline principale del brand — max 7 parole]

**Varianti:**
- [Variante 1]
- [Variante 2]
- [Variante 3]

---

## Pagina: Home (/)

### META
- **Title tag:** [max 60 caratteri] | [Brand Name]
- **Meta description:** [max 155 caratteri, include CTA]
- **OG Title:** [può essere più lungo del title tag]
- **OG Description:** [max 200 caratteri]

### NAVBAR
- **Logo alt text:** [nome brand — tagline breve]
- **CTA Button:** [testo button — max 4 parole]

### HERO
**Headline (H1):**
> [Headline principale — massimo 10 parole, benefit-focused]

**Varianti headline:**
- [Variante A — pain-point focused]
- [Variante B — outcome focused]
- [Variante C — social proof focused]

**Subheadline:**
> [2-3 frasi che espandono l'headline, specificano il target, anticipano la soluzione]

**CTA Primario:** [Testo bottone — verbo + beneficio]
**CTA Secondario:** [Testo link secondario — opzione alternativa]

### SEZIONE: [nome sezione]
**Titolo sezione (H2):**
> [Titolo]

**Sottotitolo:**
> [1-2 frasi introduttive]

**Card 1:**
- Titolo: [titolo]
- Testo: [2-3 frasi]

**Card 2:**
- Titolo: [titolo]
- Testo: [2-3 frasi]

[continua per tutte le sezioni]

### TESTIMONIAL
**[Nome Cliente], [Ruolo], [Azienda]:**
> "[Testo testimonial — specifico, con risultato concreto se possibile]"

### FOOTER
- **Tagline footer:** [variante breve della tagline]
- **Copyright:** © [anno] [Nome Brand]. Tutti i diritti riservati.
- **Link:** Privacy Policy | Cookie Policy | [altri link]

---

## Pagina: [Nome Pagina] ([URL])

[Stessa struttura della Home, adattata per questa pagina]

---

## Glossario Copy

**Parole da USARE sempre:**
- [parola/frase che risuona con il target]
- [parola/frase brand-specific]

**Parole da EVITARE:**
- [jargon da non usare]
- [parole troppo generiche]
- [parole dei competitor da differenziarci]

---

## Alt Text Immagini

| Immagine | Alt Text |
|---------|---------|
| hero-image | [descrizione precisa, include keyword dove naturale] |
| [nome immagine] | [alt text] |

---

*Generato da /site copy — Digital Empire Site Creation System*
```

### Step 6: Aggiorna SITE-STATUS.md

Segna Copy come completato. Indica che ora si può procedere con `/site build`.

---

## Regole di Copywriting

- **Benefits, non features** — "Risparmia 3 ore al giorno" non "Ha un dashboard avanzato"
- **Seconda persona sempre** — "tu", "il tuo", "per te" — non "i nostri clienti"
- **Specifico, non generico** — "aumenta le conversioni del 23%" non "migliora i risultati"
- **Una idea per frase** — frasi brevi, paragrafi brevi, scansionabile
- **Il tono deve essere coerente** — ogni pagina suona come la stessa persona
- **CTA con verbo attivo** — "Inizia ora", "Ottieni il tuo piano", "Prenota una call" — non "Invia" o "Clicca"
- **Mai scrivere copy AI-sounding** — niente "nell'odierno panorama digitale", niente "soluzioni innovative"
- **Testimonial specifici** — nomi reali, risultati concreti, non frasi vaghe

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
