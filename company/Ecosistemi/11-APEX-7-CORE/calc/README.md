---
Type: TOOL
Status: Active
Tags: #apex7 #calc #probabilita #royalty #ponte
Created: 2026-08-14
Last updated: 2026-08-14
---

# APEX-7 Calc Layer — il calcolatore dell'Impero

Calcola percentuali, probabilità, rendimenti, rischio, royalty e guadagni. È un
**registro di funzioni pure**: ogni calcolo dichiara i parametri che gli servono,
restituisce solo numeri finiti e viaggia in JSON.

Gemello del [orchestration layer](../orchestration/README.md): quello coordina e
certifica, questo calcola.

## Uso

```python
from calc import esegui, catalogo

esegui({"modulo": "royalty_kdp", "prezzo": 4.99, "unita_vendute": 500,
        "costi_fissi": 300, "peso_file_mb": 2})
# -> royalty_per_copia 3.19 · guadagno_netto 1296.50 · copie_per_pareggio 94

esegui({"modulo": "probabilita_soglia", "valore_iniziale": 1000, "soglia": 5000,
        "tasso_atteso": 0.30, "volatilita": 0.5, "periodi": 5})
# -> probabilita_pct 20.46 · mediana 1987 · valore_atteso 3713

catalogo()   # tutto ciò che sa calcolare, in JSON
```

## I 16 moduli

| Categoria | Modulo | Cosa risponde |
|---|---|---|
| **base** | `percentuale` | che % è una parte di un totale |
| | `variazione_percentuale` | di quanto è cambiato un valore |
| | `applica_percentuale` | sconto o aumento su un valore |
| | `crescita_composta` | quanto diventa X che cresce al Y% per N periodi |
| **probabilita** | `probabilita_composta` | che tutti gli eventi accadano (AND) o almeno uno (OR) |
| | `bayes` | probabilità a posteriori data una prova |
| | `probabilita_soglia` | che probabilità ho di superare un obiettivo |
| | `monte_carlo` | distribuzione degli esiti, percentili, prob. di perdita |
| | `scenari_calibrati` | valore atteso su migliore/base/peggiore |
| **denaro** | `rendimento` | quanto vale davvero un capitale, netto di tutto |
| | `costi_invisibili` | quanto si perde per inflazione, commissioni, tasse |
| | `confronto_risk_free` | conviene rischiare o resto sul sicuro |
| | `rischio` | perdita massima, rapporto rischio/rendimento, VaR |
| **guadagni** | `royalty` | guadagno da royalty, margine, unità per il pareggio |
| | `royalty_kdp` | royalty Amazon KDP (ebook 70%/35%, cartaceo 60%) |
| | `prezzo_ottimale` | a che prezzo guadagno di più, data l'elasticità |

## Le tre regole

1. **Nessun numero senza fonte.** Se un calcolo usa un default che non hai
   dichiarato, quel valore esce nella lista `assunzioni` con la sua provenienza.
   Un numero prodotto da un default non è un numero misurato, e chi legge deve
   poterlo distinguere.
2. **Nessuna eccezione oltre il confine.** `esegui` non solleva mai: un errore
   torna come `ok: False` con il motivo. Chi sta dall'altra parte del ponte non
   deve conoscere Python.
3. **I vincoli sono vincoli.** Probabilità fuori da 0-100, distribuzioni che non
   sommano a 100, scenari in ordine incoerente, perdite superiori al capitale,
   elasticità positiva: **rifiutati**, non arrotondati.

## Il ponte verso gli altri layer

`esegui` e `catalogo` parlano solo dict JSON-serializzabili. Un altro
orchestration layer chiede `catalogo()` per scoprire cosa questo sa fare, poi
manda richieste. Nessun oggetto Python attraversa il confine.

**Calcoli in catena** — l'output di uno alimenta l'altro, l'ordine lo risolve il
DAG dell'orchestration layer (cicli e dipendenze inesistenti bloccano *prima* di
eseguire):

```python
from calc import esegui_grafo

esegui_grafo([
    {"nome": "libro", "modulo": "royalty_kdp",
     "parametri": {"prezzo": 4.99, "unita_vendute": 2000, "costi_fissi": 500}},
    {"nome": "investi", "modulo": "rendimento", "dipende_da": ["libro"],
     "parametri": {"anni": 10, "rendimento_annuo": 0.07},
     "prendi": {"capitale": "libro.guadagno_netto"}},
])
```

**Calcolo certificato** — quando il numero diventa una decisione, `esegui_certificato`
lo fa passare dai quality gate e restituisce la scorecard. Gli esiti di
`scenari_calibrati` diventano la distribuzione che il gate L5 verifica.

## Due errori dello zip, corretti qui

Il calcolatore dello zip `apex7_orchestrator` aveva due difetti che **ribaltavano
la conclusione**. Entrambi hanno un test `REGRESSIONE` in `test_calc.py`.

1. **Tassava il rendimento reale invece della plusvalenza nominale.** In Italia
   non c'è indicizzazione all'inflazione: si tassa il guadagno in euro correnti.
   Errore del +2,4% a 10 anni e del −11,4% a 30 — cambiava pure segno.
2. **Confrontava un valore atteso netto con un BTP lordo nominale.** Sul suo
   stesso dossier concludeva che un ETF All-World **perdeva** contro il BTP di
   €10.812. A parità di trattamento fiscale e inflattivo:

   | | zip | qui |
   |---|---|---|
   | premio al rischio (ETF 7,5%, 10 anni) | **−€10.812** | **+€28.023** |

In più: lo zip certificava uno scenario con **capitale finale −€2,92**. Qui una
perdita oltre il 100% viene rifiutata in ingresso.

## Test

```bash
cd company/Ecosistemi/11-APEX-7-CORE
python test_calc.py            # 39 test
python test_orchestration.py   # 49 test
```

## Connessioni

- [[orchestration/README]] — il layer che coordina e certifica
- [[ADR-010-fusione-ruflo-apex7]] — perché sta dentro il motore canonico
- [[ADR-011-quinta-implementazione-apex7]] — nessuna linea nuova fuori di qui
