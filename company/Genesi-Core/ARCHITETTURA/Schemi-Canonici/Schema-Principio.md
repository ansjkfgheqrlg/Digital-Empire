# SCHEMA CANONICO — Principio

> Forma LEGGERA (knowledge layer). Una regola-guida che orienta decisioni, NON un eseguibile.
> Motore/esempio: i file `P01..P15` di `Skill Master Architecture` (1 principio per file, ~50–170 righe).

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando hai una verità operativa che deve guidare scelte ricorrenti (es. "no riassunti,
  sempre espandere"; "progressive disclosure"; "scegli la forma giusta"). È sapere, non automazione.
- **NO se** è una regola visiva/di voce di un brand → **Stile**. NO se è un processo a passi
  eseguibile → **Workflow**. NO se va eseguito da un'entità → **Agente/Skill**. NO se è un corpo di
  conoscenza ampio e atomizzato → **Documento/MKD**.
- **Trattamento LEGGERO**: un principio NON riceve org chart, KPI di reparto o I/O JSON. Sarebbe spreco.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Enunciato** (1 frase, grassetto): la regola in forma memorabile e azionabile.
2. **Perché funziona / perché esiste**: la ragione, idealmente con il costo del NON rispettarlo.
3. **Quando si applica** (e quando NO): confini espliciti — un principio senza confini è dogma.
4. **Test di rispetto**: domande binarie verificabili ("come faccio a sapere se l'ho rispettato?").
5. **Esempi + anti-esempi**: ≥1 caso conforme e ≥1 violazione concreta.
6. **Connessioni**: principi/forme correlate.

## Template vuoto (copiabile)
```markdown
# <PNN> — <Nome Principio>
> **Enunciato**: <la regola in una frase>.
## Perché
<ragione + costo del non rispettarlo>
## Quando si applica (e quando NO)
- Applica quando: ...
- NON applicare quando: ...
## Test di rispetto
- [ ] <domanda binaria 1>
- [ ] <domanda binaria 2>
## Esempi
- ✅ Conforme: <caso>
- ❌ Violazione: <caso> → conseguenza
## Connessioni
- Combina con: [[...]] · In tensione con: [[...]]
```

## Checklist di completezza (per struct-gate)
- [ ] **Enunciato** in una sola frase, azionabile (non un titolo generico).
- [ ] **Perché** presente, con il costo del non rispettarlo.
- [ ] **Quando si applica E quando NO** entrambi esplicitati.
- [ ] **Test di rispetto** con ≥2 domande binarie verificabili.
- [ ] ≥1 **esempio conforme** E ≥1 **anti-esempio** concreti.
- [ ] **Connessioni** ≥2.
- [ ] NESSUN apparato pesante improprio (no org chart/KPI di reparto/I-O JSON).

## Esempio minimo compilato
**P03 — No-Summary, Always Expand.** Enunciato: *"L'output rispetta o supera la lunghezza del
sorgente; espandere, mai riassumere."* Perché: riassumere perde atomi informativi → l'artefatto
diventa inutilizzabile (costo: rilavoro). Applica a: trasformazione di materiale grezzo. NON
applica a: TL;DR esplicitamente richiesti. Test: [ ] output ≥ sorgente? [ ] ogni atomo presente?
✅ MKD che espande ogni concetto con esempi. ❌ bullet list che taglia il 70% → fail. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- Enunciato vago ("sii bravo") non azionabile → non orienta nessuna decisione.
- Manca "quando NON applicare" → diventa dogma applicato fuori contesto.
- Test non binari → impossibile verificare il rispetto (alimenterebbe male lo struct-gate).
- Nessun anti-esempio → si capisce la teoria ma non si riconosce la violazione.
- Gonfiare un principio con apparato da ecosistema → spreco, contro il principio della FORMA GIUSTA.

## Connessioni
- [[Schema-Stile]] — forma leggera sorella (regole visive/voce)
- [[Schema-Documento-MKD]] — quando il sapere è ampio, non una singola regola
- [[README]] — il principio madre: scegli la forma giusta, leggera dove serve leggera
