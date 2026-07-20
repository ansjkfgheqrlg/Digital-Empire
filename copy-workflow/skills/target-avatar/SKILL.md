# Target Avatar — Skill
> Costruisce un buyer persona completo e operativo per guidare qualsiasi copy

## Invocazione

```
/avatar [prodotto/servizio]
```

Esempi:
- `/avatar "corso di forex trading per principianti"`
- `/avatar "servizio di social media management per PMI"`

---

## Cos'è un Avatar e Perché È Critico

Un avatar è un personaggio inventato che rappresenta il tuo cliente ideale.

**Senza avatar**: scrivi copy per "chiunque" → nessuno si sente capito → non compra.
**Con avatar**: scrivi come se parlassi a una persona specifica → lei si sente capita → compra.

La regola: **più specifico l'avatar, più il copy converte.**

---

## Processo di Costruzione

### Domande Fondamentali (3 round)

**Round 1 — Chi è?**
```
1. Età (specifica, non range) + sesso
2. Professione e situazione lavorativa
3. Dove vive, com'è la sua vita quotidiana?
```

**Round 2 — Qual è il suo problema?**
```
4. Qual è il suo problema principale in relazione al tuo prodotto?
5. Da quanto tempo ce l'ha? Come lo ha già affrontato?
6. Come si sente quando il problema si manifesta?
```

**Round 3 — Cosa lo blocca?**
```
7. Perché non ha già risolto il problema?
8. Cosa pensa dei prodotti simili al tuo?
9. Cosa gli farebbe dire "finalmente"?
```

Se l'utente non ha le risposte → suggerisci defaults plausibili basati sul settore.

---

## Output: Avatar Completo

```markdown
# Buyer Avatar — [Nome Prodotto]
Creato il: [data]

---

## Profilo Base
**Nome**: [nome inventato realistico]
**Età**: [età precisa]
**Sesso**: [M/F]
**Professione**: [titolo + settore]
**Città/Zona**: [specificità geografica]
**Reddito mensile netto**: [range]
**Situazione familiare**: [single/coppia/famiglia]

---

## Vita Quotidiana
[Paragrafo di 5-7 righe che descrive una sua giornata tipo, in terza persona. Include: dove lavora, come si muove, cosa fa la sera, cosa lo stanca, cosa lo fa stare bene. Deve essere così vivido che il copywriter si sente lì con lui.]

---

## Rapporto con il Problema
**Il problema**: [descrizione in 1-2 righe]
**Da quando ce l'ha**: [timeline]
**Come lo describerebbe**: "[citazione diretta in prima persona, con il suo linguaggio]"
**Cosa ha già provato**: [soluzioni precedenti fallite]
**Quanto pesa (1-10)**: [score] — [motivazione]

---

## Mappa Emotiva
| Emozione | Descrizione | Leva nel Copy |
|---|---|---|
| Paura principale | [paura specifica] | [come usarla] |
| Frustrazione | [cosa lo fa incazzare] | [come usarla] |
| Desiderio | [cosa vuole davvero] | [come usarla] |
| Vergogna latente | [cosa non ammetterebbe] | [come usarla] |
| Speranza | [in cosa crede ancora] | [come usarla] |

**Acquista per**: ☐ Rincorsa del piacere  ☐ Fuga dal dolore  ☐ Entrambi

---

## Obiezioni (in ordine di forza)
1. **[Obiezione principale]** — Tipo: [prezzo/fiducia/efficacia/tempo/bisogno]
   → Come gestirla: [approccio in 1 riga]

2. **[Seconda obiezione]**
   → Come gestirla: [...]

3. **[Terza obiezione]**
   → Come gestirla: [...]

---

## Come Parla

### Vocabolario Tipico
- "[Frase che userebbe per descrivere il suo problema]"
- "[Termine tecnico che usa o non conosce]"
- "[Modo di dire tipico del suo ambiente]"

### Cosa Lo Spinge a Leggere
[Tipo di contenuto/copy che cattura la sua attenzione]

### Cosa Lo Fa Andare Via
[Cosa lo allontana — tone of voice sbagliato, promesse irreali, gergo eccessivo]

---

## Social Media e Comportamento Online
| Piattaforma | Frequenza | Come la usa |
|---|---|---|
| [Platform 1] | [ogni giorno/settimanale] | [scroll / crea / interagisce] |
| [Platform 2] | [...] | [...] |

---

## Reference Visivi/Culturali
- Idoli o persone che ammira: [lista]
- Serie TV / Film che guarda: [es. rilevante per metafore nel copy]
- Metafore che funzionano con lui: [es. "come avere un commercialista che lavora 24/7"]
- Esempi di brand/copy che apprezza: [se noti]

---

## Scenario Tipico di Acquisto
[Descrivi il momento e la situazione in cui questo avatar incontrerebbe il tuo prodotto per la prima volta. Dove si trova, cosa sta facendo, come si sente, cosa lo fa fermare. In 3-5 righe.]

---

## Red Flags (Come NON Parlargli)
- ❌ [Tone of voice che lo allontana]
- ❌ [Promessa che suona falsa per lui]
- ❌ [Termine o parola che lo fa sentire giudicato]
- ❌ [Argomento o approccio che genera resistenza]
```

---

## Avatar Quick (versione ridotta)

Per chi ha poco tempo, versione in 5 campi:
```
Nome + età: [...]
Professione: [...]
Problema: "[citazione in prima persona]"
Paura: [...]
Desiderio: [...]
```

---

## Come Usare l'Avatar nel Copy

Una volta creato l'avatar:
1. **Stampa la citazione del problema** — usala come ispirazione per la sezione P
2. **La paura** → usala per la conseguenza del non agire (C in APSOC)
3. **Il desiderio** → usalo per la sezione Soluzione (beneficio principale)
4. **Il vocabolario** → copia le sue parole nel copy (show don't tell)
5. **Le obiezioni** → passale direttamente ad A6 (Objections Handler)

---

## Struttura della Skill

```
target-avatar/
├── SKILL.md                              ← questo file (entry point)
├── references/
│   └── research-methods.md               ← 6 metodi per raccogliere dati reali (Amazon, forum, interviste...)
└── assets/
    ├── templates/
    │   └── avatar-canvas.md              ← canvas completo (10 sezioni) per costruire l'avatar
    └── examples/
        └── avatar-giulia.md              ← avatar annotato con note strategiche (freelance copywriter 27 anni)
```

## Routing Rapido

| Se hai bisogno di... | File |
|---|---|
| Come trovare i dati reali del target (non inventarli) | `references/research-methods.md` |
| Template completo da compilare | `assets/templates/avatar-canvas.md` |
| Vedere come suona un avatar professionale | `assets/examples/avatar-giulia.md` |
| Template avatar base | `../../assets/templates/avatar-template.md` |

## Riferimenti

- Agente completo: `agents/research/target-analyst.md`
- Template avatar: `assets/templates/avatar-canvas.md`
