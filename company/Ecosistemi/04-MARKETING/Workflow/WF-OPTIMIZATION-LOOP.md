# WF-OPTIMIZATION-LOOP — Loop Ottimizzazione Data-Driven
## Reparto: L2.4 — ANALYTICS & OTTIMIZZAZIONE

## Trigger
Dati di performance disponibili su copy o campagna attiva. Il loop parte automaticamente 48-72 ore dopo ogni lancio/invio significativo. Non richiede intervento umano per i passi 1-4; intervento umano per decidere se approvare la revisione e il test successivo.

## Input
- Dati performance: metriche per copy_id e canale (CTR, reply rate, opt-in, conversioni, per piattaforma)
- Copy_id delle varianti misurate con sezioni APSOC identificabili
- Score A8 precedenti correlati con i copy_id
- Baseline storica (o "primo ciclo" se non esiste ancora baseline)

## Pipeline (passi in sequenza)
1. **RACCOLTA — AN1/AN2:**
   AN1 estrae i dati dal tracking (GA4, Meta Ads Manager, ESP) con UTM codes.
   AN2 struttura i dati per copy_id + canale + segmento.
   Output: tabella performance `{copy_id, canale, CTR, conversioni, data}`.

2. **DIAGNOSI — AN2 + A8:**
   AN2 mappa la performance sulla struttura APSOC:
   - Alto impression/basso CTR → problema in A (hook non funziona)
   - Alto CTR/bassa permanenza su pagina → problema in P (agitazione problema non convincente)
   - Alta permanenza/bassa conversione → problema in O o C (obiezioni non gestite, CTA debole)
   AN2 dichiara LA sezione diagnosticata, non "migliora tutto".

3. **DISTILLA — AN4 — Insight Distiller:**
   Performance negativa → anti-pattern in `marketing/copy/antipatterns/{icp}`
   Performance positiva → pattern in `marketing/copy/patterns/{icp}`
   Schema record obbligatorio: `{icp, formato, sezione_APSOC, pattern, evidenza, data, confidenza}`
   Pattern ad alta confidenza → entry wiki + `wiki/log.md`

4. **REVISIONE — copy-master:**
   Apre il copy SOLO sulla sezione diagnosticata da AN2.
   Riscrittura chirurgica: A3 se sezione A, A4 se sezione P, A6 se sezione O, A7 se sezione C.
   REGOLA: mai riscrittura totale di un copy che performa parzialmente.

5. **TEST — AN3 + WF-AB-TEST:**
   AN3 progetta il test: ipotesi, campione dimensionato, criteri di stop pre-dichiarati.
   Variante vecchia vs variante nuova (a parità di tutto il resto).
   Raccolta dati → verdetto (conclusivo o inconclusivo — mai forzato).

6. **CONSOLIDA — AN4:**
   Winner → pattern library aggiornata.
   Loser → anti-pattern (se non già presente).
   `wiki/log.md` aggiornato.
   Torna a passo 1 (loop continuo).

## Gate di uscita
Ogni ciclo si chiude con: pattern aggiornato in namespace + report AN2 per committente (T-REPORT) + raccomandazioni next iteration

## Output
Per ogni ciclo: diagnosi APSOC specifica + pattern/anti-pattern aggiornati + copy rivisto sulla sezione diagnosticata + piano test successivo + report committente

## Tempo stimato
- Raccolta + diagnosi: 30-60 minuti (dipende dalla quantità di dati)
- Distillazione pattern: 15-20 minuti
- Revisione chirurgica copy: 20-40 minuti
- Test design (AN3): 20 minuti
- Ciclo completo raccolta→test: 2-4 settimane (dipende dal volume di traffico per raccogliere dati significativi)

## Regola anti-deriva
Nessuna revisione basata su opinioni. Solo su dati del loop o su score A8. Sotto soglia statistica minima → "inconclusivo", non si conclude nulla. I pattern si consolidano solo con evidenza ripetuta.

## Connessioni
- [[L2.4-ANALYTICS]] — reparto di riferimento
- [[AN2-attribution-analyst]] — diagnosi APSOC (step 2)
- [[AN3-experiment-designer]] — progettazione test (step 5)
- [[AN4-insight-distiller]] — distillazione e consolidamento pattern (step 3 + 6)
- [[WF-ADS-CAMPAIGN]] e [[WF-EMAIL-LAUNCH]] — i workflow che alimentano il loop con dati
