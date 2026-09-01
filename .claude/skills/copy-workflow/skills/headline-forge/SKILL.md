# Headline Forge — Skill
> Genera 10+ headline con formule APSOC per qualsiasi prodotto o contesto

## Invocazione

```
/headline [prodotto] [target] [strategia opzionale]
```

Esempi:
- `/headline "corso di copywriting" "freelance italiani"`
- `/headline "integratore sportivo" "uomini 30-45 che vanno in palestra" curiosità`
- `/headline "software gestionale" "PMI italiane" urgenza`

---

## Le 9 Strategie Headline

| # | Strategia | Quando Usarla | Efficacia |
|---|---|---|---|
| 1 | Curiosità sul pain point | Target consapevole del problema | ⭐⭐⭐⭐⭐ |
| 2 | Pain point diretto | Ads breve, target saturo | ⭐⭐⭐⭐ |
| 3 | USP nell'headline | Feature genuinamente unica | ⭐⭐⭐⭐ |
| 4 | Urgenza / Allarmismo | Mercati in cambiamento | ⭐⭐⭐ |
| 5 | Controversia | Mercati affollati | ⭐⭐⭐⭐ |
| 6 | Semplicità diretta | Brand noti, prodotti semplici | ⭐⭐⭐ |
| 7 | Domanda che fa specchio | Sales page, lungo copy | ⭐⭐⭐⭐ |
| 8 | CTA nell'headline | Email marketing | ⭐⭐⭐ |
| 9 | Promessa specifica + timeframe | Prodotti con risultati misurabili | ⭐⭐⭐⭐⭐ |

---

## Output — 10 Headline per Ogni Run

```markdown
# 10 Headline — [Prodotto]
Target: [...]
Data: [...]

---

### 🥇 TOP PICKS (usa queste per primo test)

**#1 — [Strategia: Curiosità sul Pain Point]**
> "[HEADLINE]"
💡 Perché funziona: [spiegazione 1 frase]
📊 Quando testare: [contesto ideale]

**#2 — [Strategia: Pain Point Diretto]**
> "[HEADLINE]"
💡 Perché funziona: [...]
📊 Quando testare: [...]

**#3 — [Strategia: Promessa Specifica]**
> "[HEADLINE]"
💡 Perché funziona: [...]
📊 Quando testare: [...]

---

### 🔄 ALTERNATIVE

**#4 — [Strategia: USP]**
> "[HEADLINE]"

**#5 — [Strategia: Controversia]**
> "[HEADLINE]"

**#6 — [Strategia: Urgenza]**
> "[HEADLINE]"

**#7 — [Strategia: Domanda]**
> "[HEADLINE]"

**#8 — [Strategia: Semplicità]**
> "[HEADLINE]"

---

### 🎯 VARIANTI FORMULE

**#9 — Formula "Come X senza Y"**
> "[HEADLINE]"

**#10 — Formula "Se [condizione], leggi questo"**
> "[HEADLINE]"

---

## Sottotitoli (3 opzioni)
[Sottotitolo 1 — complementa headline 1]
[Sottotitolo 2 — complementa headline 2]
[Sottotitolo 3 — generico per qualsiasi headline]

## Hook di Apertura (per la headline #1)
[Prime 2-3 righe di corpo copy che seguono la headline principale]
```

---

## Le 10 Formule Headline (Template Riempibili)

```
F1. "Se [problema diffuso], [conseguenza inaspettata]"
    → "Se non fai ADS nel 2024, stai regalando clienti alla concorrenza"

F2. "Cosa [autorità] non ti dice su [argomento]"
    → "Cosa il tuo commercialista non ti dice sulle spese deducibili"

F3. "Come [risultato desiderato] senza [sacrificio odiato]"
    → "Come perdere 10kg senza rinunciare alla pasta"

F4. "Il primo/unico [prodotto] che [USP]"
    → "Il primo corso di copywriting in italiano davvero utilizzabile come manuale"

F5. "Dammi [tempo minimo] e ti [risultato specifico]"
    → "Dammi 20 minuti e ti mostro come scrivere un'ad che vende da sola"

F6. "[Numero] modi per [risultato] che [la maggior parte ignora]"
    → "7 strategie di copy che il 90% degli imprenditori italiani ignora"

F7. "Stai ancora [azione sbagliata comune]? Ecco perché devi smettere"
    → "Stai ancora sperando che il tuo prodotto si venda da solo? Ecco perché devi smettere"

F8. "[Affermazione audace] — ecco la prova"
    → "Ho triplicato il fatturato senza aumentare il budget ads — ecco esattamente come"

F9. "Il problema non è [causa ovvia]. Il problema è [causa nascosta]"
    → "Il problema non è il prezzo. Il problema è che nessuno capisce il valore di quello che vendi"

F10. "[Target specifico], questo è per te"
     → "Freelance italiani che fatturano meno di 2.000€/mese: questo è per voi"
```

---

## Headline per Tipo di Copy

### Per ADS (corte, massimo 10 parole)
Focus su: curiosità, pain point, USP in poche parole
- Evita: headline troppo elaborate che non si leggono in 2 secondi

### Per Sales Page (più lunghezza permessa)
Focus su: promessa specifica, storytelling, domanda profonda
- Puoi usare headline + sottotitolo combinati

### Per Email (oggetto email)
Focus su: curiosità, urgenza, personalizzazione
- Lunghezza ideale: 40-50 caratteri (per non essere tagliato in mobile)
- Usa: numeri, domande, urgenza soft

### Per Social Media Post
Focus on: controversia, curiosità, hook che ferma lo scroll
- Prima riga = headline
- Deve fermare il pollice in 0.3 secondi

---

## Struttura della Skill

```
headline-forge/
├── SKILL.md                              ← questo file (entry point)
├── references/
│   ├── formule-espanse.md                ← 10 formule con 4+ esempi ciascuna su settori diversi
│   └── headline-per-contesto.md          ← strategie per formato (ad/SP/email/social) e awareness level
└── assets/
    └── templates/
        └── headline-batch.md             ← template per generare 10+ headline sistematicamente
```

## Routing Rapido

| Se hai bisogno di... | File |
|---|---|
| Esempi multipli per ogni formula | `references/formule-espanse.md` |
| Quale formula usare per ads vs sales page vs email | `references/headline-per-contesto.md` |
| Template per generare un set completo | `assets/templates/headline-batch.md` |

---

## Analisi Competitor Headline (Opzionale)

Se fornisci headline di competitor, analizzo:
1. Quale strategia stanno usando
2. Perché funziona o non funziona
3. Come differenziarti mantenendo la stessa efficacia

---

## A/B Test Setup

Per ogni run di headline, suggerisco automaticamente:
- **Headline da testare per prima**: [perché]
- **Headline da testare per seconda**: [contro-ipotesi]
- **Metrica per decretare il winner**: [CTR / CVR / aperture email]
- **Durata consigliata del test**: [giorni / impression]
