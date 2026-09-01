# Note Strategiche — Copy Workflow Orchestration Layer

**Build date**: 2026-05-26
**Source**: Il Manuale del Copywriting v1.1 (115 pagine, ~22.700 parole)
**Target content-forge**: orchestration
**File totali**: 22

---

## Decisioni Architetturali

### 1. Perché la separazione A1-A2 prima della scrittura
Il manuale enfatizza che il copy mediocre nasce da una comprensione superficiale del target. A1 e A2 non sono "opzionali" — senza un avatar preciso e una language map reale, A3 produce headline che parlano al marketer, non al target. La separazione in fase 1 (ricerca) e fase 2 (scrittura APSOC) riflette questo principio.

### 2. Perché A4 ha il divieto assoluto di menzionare il prodotto
È la regola più frequentemente violata nel copy amatoriale. Il problema deve essere vissuto dal lettore in modo così completo che la soluzione diventa inevitabile — non "venduta". Se il prodotto appare durante la sezione problema, si interrompe l'immedesimazione. Il blocco è hardcoded nell'agente.

### 3. Perché il framework CPB e non solo "gestione obiezioni"
Il manuale distingue chiaramente tra rispondere a un'obiezione (difensivo, crea resistenza) e gestirla con CPB (proattivo, crea credibilità). Il Claim senza Proof è un'affermazione vuota. Il Proof senza Benefit è informazione morta. La struttura tripartita garantisce che ogni obiezione sia gestita in modo completo.

### 4. Perché il CTA "profondo" vs "superficiale"
"Compra ora" è il CTA più comune e il meno efficace. Il CTA profondo collega l'azione al pain point specifico del target — non chiede di comprare, chiede di smettere di soffrire. Questa distinzione è esplicitata nel manuale come differenza tra copy che informa e copy che converte.

### 5. Perché 4 workflow distinti invece di un unico workflow parametrizzato
Ogni formato (ad, sales page, email, full pipeline) ha esigenze profondamente diverse in termini di lunghezza, struttura APSOC e agenti necessari. Unificarli avrebbe creato un sistema complesso con troppe condizioni. I 4 workflow sono semplici da seguire separatamente.

---

## Framework Estratti dal Manuale

### APSOC
La struttura portante. Ogni copy, di qualsiasi lunghezza, deve seguire A→P→S→O→C in questo ordine. La violazione più grave è S prima di P.

### CPB (Claim → Proof → Benefit)
Il template per gestire ogni singola obiezione. La prova deve essere specifica (numeri, nomi, casi) — mai vaga.

### Pain Point Amplification (4 livelli)
1. Problema nominato
2. Impatto pratico
3. Impatto emotivo
4. Conseguenza esistenziale/identitaria

Il copy amatoriale si ferma al livello 1-2. Il copy che converte sale al 3-4.

### Conseguenza del Non Agire (CNA)
Alternativa all'urgenza temporale quando non c'è una scadenza reale. Non "compra entro mezzanotte" ma "senza risolvere questo problema, tra 6 mesi sarai in questa situazione..."

### Show Don't Tell
Il target non vuole che gli si dica che ha un problema — vuole riconoscersi in uno scenario. La differenza tra "se soffri di stanchezza cronica" (tell) e "se ogni mattina spegni tre volte la sveglia prima di alzarti" (show).

---

## Limitazioni Note

1. **Senza testimonianze reali**: A6 costruisce prove logiche e showoff, ma l'impatto è inferiore. Il sistema segnala sempre quando usa prove ipotetiche.

2. **USP finto vs reale**: A5 include un protocollo per costruire uno pseudo-USP combinando selling points, ma il risultato non sostituisce un differenziatore autentico.

3. **Language map senza ricerca**: quando non ci sono recensioni, forum o interviste disponibili, A2 usa il linguaggio ipotetico. Il copy risultante ha meno "frasi trigger" autentiche.

4. **Validazione pre-lancio**: il sistema produce copy ottimizzato secondo il manuale, ma non sostituisce il test reale con il target. Il QA a 100 punti misura la qualità tecnica, non il conversion rate reale.

---

## Come Usare il Sistema

### Per un progetto nuovo
```
1. Compila templates/briefing-template.md
2. Lancia /copywriting full
3. A1 + A2 in parallelo (fase ricerca)
4. A3 → A7 in sequenza (fase scrittura APSOC)
5. A8 QA — se score < 80, itera sulla sezione più debole
6. Consegna: copy-finale.md + qa-report.md
```

### Per un copy rapido
```
- Ads: /copywriting ad → 15-20 min, 3 varianti
- Headline: /copywriting headline → 10 alternative
- Review copy esistente: /copywriting review
```

### Per un lancio completo
```
1. /copywriting funnel → piano funnel strategico
2. /copywriting full (esteso) → sales page principale
3. /copywriting email (launch sequence) → 7-10 email
4. /copywriting ad → ads di traffico (3 varianti)
```

---

## File Index Completo

```
SKILL.md                                    ← Entry point
orchestrators/
  copy-master.md                            ← Router + state management
agents/research/
  briefing-analyst.md                       ← A1
  target-analyst.md                         ← A2
agents/apsoc/
  attention-writer.md                       ← A3
  problem-writer.md                         ← A4
  solution-writer.md                        ← A5
  objections-handler.md                     ← A6
  cta-writer.md                             ← A7
agents/qa/
  copy-reviewer.md                          ← A8
skills/
  apsoc-builder/SKILL.md
  target-avatar/SKILL.md
  headline-forge/SKILL.md
  objections-forge/SKILL.md
  funnel-designer/SKILL.md
  copy-review/SKILL.md
workflows/
  full-copy-workflow.md
  quick-ad-workflow.md
  sales-page-workflow.md
  email-sequence-workflow.md
templates/
  briefing-template.md
  avatar-template.md
  copy-checklist.md
  cpb-template.md
note-strategiche.md                         ← questo file
```
