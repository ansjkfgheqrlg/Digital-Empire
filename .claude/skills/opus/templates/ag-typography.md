# AG-4 — Typography Deep Dive
> Momento Anti-Gravity #4 | Fase 5.2 — Type Scale & Font Selection
> Usa questo template per scoprire combinazioni tipografiche sorprendenti.

---

## Quando usare questo template

**Fase:** 5.2 — dopo aver definito il type scale, prima di congelare le scelte font
**Obiettivo:** esplorare combinazioni tipografiche insolite e sorprendenti per l'aesthetic scelto

---

## Struttura del Prompt AG-4

```
Sei un tipografo e direttore creativo con una conoscenza enciclopedica dei font.
Sto scegliendo la coppia tipografica per questo progetto:

CONTESTO:
Aesthetic axis: [nome movimento]
Settore: [settore]
Audience: [descrizione]
Brand personality: [5 aggettivi]
Risposta emotiva target: [cosa deve sentire il visitatore]

COPPIA ATTUALE CONSIDERATA:
Font display (headings): [font 1]
Font body (paragrafi): [font 2]
Motivazione: [perché li ho scelti]

TYPE SCALE (Perfect Fourth 1.333):
Hero: 5.61rem | H1: 4.209rem | H2: 2.369rem | H3: 1.777rem | Body: 1rem

---

CHIEDO:
1. VALUTAZIONE COPPIA ATTUALE: La coppia [font1] + [font2] funziona per [aesthetic axis]?
   Dove è forte? Dove è debole? È una scelta "sicura" o "sorprendente"?

2. ALTERNATIVE INSOLITE: Proponi 3 coppie alternative che NON sono le prime che
   vengono in mente per [aesthetic axis]. Per ognuna:
   - Nomi dei font
   - Tensione visiva creata dalla coppia
   - Quale aspetto del brand personality enfatizza
   - Un esempio di headline H1 con questa coppia (solo la descrizione visiva)

3. MICRO-TIPOGRAFIA: Per la coppia che sceglierò, quali sono i 5 valori di
   letter-spacing e line-height non ovvi che la fanno sembrare "hand-crafted"
   invece di "AI-generated"?
   Esempi di risposta attesa: "Con Cormorant Garamond a 90px,
   letter-spacing -0.035em crea una tensione che -0.02em non ha"

4. BOLD WORD SYSTEM: Per [font body scelto] a font-weight 600,
   la differenza visiva rispetto a 400 è abbastanza leggibile?
   Se no, quale peso usare per il bold words nel body text?

5. FLUID SIZING: I valori clamp() standard funzionano per questa coppia
   o ci sono aggiustamenti specifici per questi font a queste dimensioni?
   (Alcuni font necessitano di più o meno spazio a determinate dimensioni)
```

---

## Come usare l'output

1. **Valuta** le 3 alternative — prendi nota delle coppie insolite più interessanti
2. **Aggiorna** TYPOGRAPHY-SYSTEM.md con la scelta finale e motivazione
3. **Applica** i micro-valori di letter-spacing/line-height come token nel CSS
4. **Verifica** visivamente il bold word system in browser con font reali
5. **Documenta** la scelta tipografica in SITE-DESIGN.md con motivazione

Di' a opus-director: "AG-4 completato, font confermati" → procede Fase 5A.
