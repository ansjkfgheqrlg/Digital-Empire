# ISTRUZIONI PER CLAUDE CODE — CAROUSEL FACTORY

## WORKFLOW PRINCIPALE (nuovo)

L'utente genera le slide con **Gemini AI** a partire da prompt ultra-specifici.
Il mio compito è produrre quei prompt, pronti da copiare uno ad uno.

---

## BRAND ATTIVI

| Brand | Handle | Stile |
|-------|--------|-------|
| `mentalita-brutale` | @mentalita.brutale | Dark, gradiente rosso/argento, Anton font |

---

## QUANDO L'UTENTE CHIEDE UN CAROSELLO

Leggi sempre:
1. `context/SYSTEM.md` — regole strutturali
2. `context/copywriting-rules.md` — tono Mentalità Brutale
3. `context/hook-formulas.md` — tipo di hook da usare
4. `context/cta-formulas.md` — CTA finale
5. `context/PROMPT-SYSTEM.md` — template prompt per Gemini

Poi produci il documento output con questo formato:

---

## FORMATO OUTPUT OBBLIGATORIO

```
═══════════════════════════════════════
CAROSELLO: [titolo]
BRAND: Mentalità Brutale | @mentalita.brutale
STRUTTURA: [N] slide
═══════════════════════════════════════

━━━ SLIDE 01 — [tipo] ━━━

COPY:
• Testo piccolo: "[testo]"
• Testo grande: "[parola1] / [parola2] / [parola accent]"

PROMPT GEMINI:
[prompt ultra-specifico in inglese, completo, pronto da incollare]

━━━ SLIDE 02 — [tipo] ━━━
[...]

━━━ CAPTION ━━━
[caption completa con hashtag]
```

---

## WORKFLOW A — topic fornito dall'utente

Quando l'utente scrive: "Crea carosello su [topic]"

1. Definisci struttura (7-10 slide)
2. Scrivi il copy di ogni slide (tono MB: brutale, diretto, valore puro)
3. Per ogni slide: compila il template prompt da `PROMPT-SYSTEM.md`
4. Personalizza il soggetto fotografico in base al topic
5. Output: documento completo con tutti i prompt

---

## WORKFLOW B — competitor da replicare

Quando l'utente allega un carosello competitor:

1. Analizza struttura, argomento, numero slide
2. Riscrivi il copy completamente nel tono MB (NON copiare)
3. Genera prompt per ogni slide con estetica MB (NON copiare lo stile del competitor)
4. Output: documento completo con tutti i prompt

---

## REGOLE DI COPY — mentalita-brutale

1. Tutto minuscolo nel testo grande
2. Max 3 parole per riga nel testo grande
3. Tono: brutalmente diretto, zero fuffa, verità che fa male
4. Slide 1: sempre hook brutale (vedi hook-formulas.md)
5. Slide finale: sempre CTA verso community (vedi cta-formulas.md)
6. 7-10 slide totali

---

## IDENTITÀ VISIVA (per i prompt)

- Foto: soggetti umani reali (uomini/donne in contesti business/urbani/drammatici)
- Trattamento: darkened 60-85%, red tint blood (#8B0000), film grain 35mm, heavy vignette
- Font: Anton Bold (testo grande), Inter Regular (testo piccolo)
- Gradiente testo: #8B0000 (top) → #C0C0C0 (bottom), per ogni parola individualmente
- Accent: #8B0000 solid + red glow
- Logo: watermark circolare bottom-right (guerriero con corona, sfondo rosso)

---

## NON FARE MAI

- Non scrivere motivazione vuota per MB
- Non usare maiuscole nel testo grande delle slide
- Non usare più di 3 parole per riga
- Non copiare il copy di caroselli competitor
- Non dimenticare il watermark logo in ogni slide
