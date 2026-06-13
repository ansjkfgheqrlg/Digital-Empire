# WF-ADS-CAMPAIGN — Campagna Ads End-to-End
## Reparto: L2.2 — ADVERTISING

## Trigger
Richiesta campagna paid con budget approvato dall'utente. Committenti tipici: 04-MARKETING (campagne DE), 02-INFO-BUSINESS (ads lancio), 01-AGENCY (ads per clienti). VINCOLO ASSOLUTO: il workflow non procede oltre il dry-run senza approvazione umana esplicita sulla spesa.

## Input
- Brief campagna: obiettivo + piattaforme target + prodotto/offerta + ICP
- Budget approvato dall'utente (cifra assoluta dichiarata nella conversazione)
- Funnel esistente (da S1) o da costruire
- Timeline: date di lancio e durata campagna

## Pipeline (passi in sequenza)
1. **S3 — Campaign Strategist:** strategic brief campagna (obiettivo SMART, canali, struttura, KPI target, budget allocation %)
2. **AD1 — Audience Analyst:** targeting brief per piattaforma (segmenti primari, test, esclusioni, lookalike)
   - In parallelo con step 3
3. **WF-COPY-AD (L2.1):** 3+ varianti copy APSOC per le ads (fan-out swarm con AD1)
4. **Handoff a 03-CONTENT-FACTORY:** brief visual per ogni variante (formato, dimensioni, stile, elemento focal)
   - AD2 prepara il brief visual standardizzato
5. **AD2 — Creative Iterator:** costruisce matrice copy × visual × audience (quando i visual arrivano da 03-CF)
6. **AD4 — Ad Compliance Checker:** pre-flight policy check su ogni variante → PASS/FAIL/WARN
   - Varianti FAIL → ritorno ad AD2 per modifica minima → re-check
7. **AN1 — Tracking Engineer:** genera UTM codes per ogni variante; verifica pixel/eventi configurati
8. **AD3 — Media Buyer:** setup campagna documentato in DRY-RUN (non live)
   - Documento include: struttura campagna, ad set per audience, naming convention, budget per ad set, bid strategy, regole di stop automatico
9. **Review umana:** il dry-run viene presentato all'utente per approvazione
10. **LANCIO (solo con ok esplicito utente):** AD3 implementa il setup; AN1 verifica il tracking live nelle prime 24h

## Gate di uscita
Pre-lancio: AD4 PASS + AN1 UTM completi + AD3 dry-run approvato dall'utente
Post-lancio (48-72h): AN2 verifica che i dati fluiscano correttamente → se anomalie → escalation

## Output
Campagna live (post-approvazione) + dry-run document + matrice creativa + UTM scheme + piano di monitoraggio AN2

## Tempo stimato
- Fase setup (S3→AD3 dry-run): 2-4 ore
- Lancio reale: richiede review umana (variabile)
- Prima ottimizzazione (AN2 diagnosi): 48-72h post-lancio

## Connessioni
- [[L2.2-ADVERTISING]] — reparto di riferimento
- [[WF-COPY-AD]] — sub-step obbligatorio per il copy delle varianti
- [[WF-OPTIMIZATION-LOOP]] — il loop si avvia dopo il lancio
- [[S3-campaign-strategist]] — primo passo del workflow
