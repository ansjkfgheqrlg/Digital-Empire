# AG-3 — Token Review
> Momento Anti-Gravity #3 | Fase 4.7 — Design Tokens Lock
> Usa questo template per far fare ad AG una review critica dei design token prima del freeze.

---

## Quando usare questo template

**Fase:** 4.7 — prima di congelare i design token e iniziare il build
**Obiettivo:** identificare token che sembrano ancora generici/AI e raffinarli

---

## Struttura del Prompt AG-3

Copia il tuo `design-tokens.css` completo e usa questo template:

```
Sei un direttore creativo con 15 anni di esperienza in design systems di lusso.
Fai una review critica di questi design token per un sito [tipo sito] nel settore [settore].

CONTESTO:
Aesthetic axis: [nome movimento]
Audience: [descrizione]
Brand feeling target: [cosa deve trasmettere — es. "autorevolezza tranquilla"]

DESIGN TOKENS:
[incolla qui il contenuto di design-tokens.css]

---

CHIEDO:
1. IDENTIFICAZIONE: Quali token sembrano ancora "AI-generic"? Sii specifico:
   - Nome del token
   - Valore attuale
   - Perché sembra generico
   - Valore alternativo più caratterizzato

2. COLORI: Il colore accent trasmette davvero [brand feeling]?
   Proponi 3 varianti alternative silver-mixed con HSL values e descrivi
   la differenza di percezione tra le 3.

3. TIPOGRAFIA: Il type scale ha personalità sufficiente per [aesthetic axis]?
   Se usiamo [font display] + [font body], c'è qualcosa nei token
   (letter-spacing, line-height, weight strategy) che lo rende ancora troppo neutro?

4. SPACING: Lo spacing system comunica lusso?
   Identifica dove aggiungere più "aria" rispetto ai valori standard.
   Un sito $50k ha section padding diverso da un sito $5k — dove siamo noi?

5. MOTION: I motion token (easing, duration) hanno una personalità?
   --ease-out-expo è tecnicamente corretto ma è usato da milioni di siti.
   C'è una curva di Bezier più caratterizzata per [aesthetic axis]?

6. HOLISTIC CHECK: Se descrivi l'intera palette in 3 parole — quali sono?
   Sono le parole giuste per [brand feeling target]? Se no, cosa manca?
```

---

## Come usare l'output

1. **Aggiorna** design-tokens.css con i token raffinati
2. **Documenta** le scelte nella sezione "Token Decisions" di SITE-DESIGN.md
3. **Valida** che il colore accent rimanga <5% dell'area visiva
4. **Controlla** che tutti i colori restino silver-mixed (saturazione ≤65%)
5. **Congela** i token dopo l'update — nessuna modifica durante il build

Di' a opus-director: "AG-3 completato, token aggiornati" → Freeze tokens → Fase 5.
