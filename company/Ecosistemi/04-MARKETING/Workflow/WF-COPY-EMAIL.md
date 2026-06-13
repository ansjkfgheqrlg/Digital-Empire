# WF-COPY-EMAIL — Copy Sequenze Email
## Reparto: L2.1 — COPYWRITING (eseguito per conto di L2.3 — EMAIL MARKETING)

## Trigger
Richiesta di copy per sequenza email (lancio, nurture, win-back, onboarding). Formato `email-seq` nel contratto. Attivato da copy-master su richiesta di E1 (Lifecycle Architect) dopo che la mappa sequenza è approvata.

## Input
- Mappa sequenza da E1: numero email, trigger per email, timing, obiettivo per email, awareness level di ogni step, branching condizionale
- Avatar ICP da A2 (con language map e obiezioni specifiche)
- Brand_kit + vincoli piattaforma (ESP: caratteri subject, preheader, ecc.)
- Segmentazione da E3 (quali segmenti ricevono quale email)

## Pipeline (passi in sequenza)
Per ogni email della sequenza (eseguite in serie o in parallelo per email indipendenti):

1. **Subject line + preheader** (T-HEADLINE come motore): 3-5 opzioni subject con strategia dichiarata (curiosity, benefit, social proof, urgency) per testing futuro via WF-AB-TEST
2. **Corpo email** — struttura APSOC adattata al formato email:
   - Email di valore/nurture: A + P condensati, S con proof, CTA leggera
   - Email di obiezione (nella sequenza lancio): A6 come motore centrale
   - Email di scarcity/chiusura: A (urgenza), S (reminder promessa), C (CTA diretta)
   - Email win-back: A (riconoscimento dell'abbandono), P (obiezione non risolta = motivo del churn), S (nuova proof o offerta), C (CTA win-back)
3. **A8 — Copy Reviewer:** score ≥80 per ogni email individualmente. La soglia si applica a ogni email come unità, non alla sequenza nel suo insieme.
4. **SEN-BV — Brand-Voice Sentinel:** gate G2 su ogni email.

## Gate di uscita
G1: score A8 ≥80 per ogni email della sequenza
G2: brand gate PASS per ogni email
E2 Deliverability Guard verifica la sequenza completa prima della consegna finale (spam score, link, unsubscribe).

## Output
Sequenza email completa: per ogni email → subject options + preheader + corpo + CTA + score A8 + note di timing/trigger per implementazione

## Tempo stimato
10-15 minuti per email. Una sequenza lancio di 6-8 email: 60-90 minuti totali (con parallelismo per email indipendenti).

## Connessioni
- [[L2.1-COPYWRITING]] — reparto che esegue questo workflow
- [[L2.3-EMAIL]] — reparto richiedente, fornisce la mappa sequenza via E1
- [[E1-lifecycle-architect]] — fornisce la struttura della sequenza
- [[E2-deliverability-guard]] — gate finale pre-consegna
- [[WF-EMAIL-LAUNCH]] — workflow di L2.3 che include questo come sub-step
