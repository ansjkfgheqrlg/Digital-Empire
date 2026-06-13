# WF-EMAIL-LAUNCH — Sequenza Lancio Prodotto
## Reparto: L2.3 — EMAIL MARKETING

## Trigger
Richiesta di sequenza email per il lancio di un prodotto (corso, ebook, servizio). Committente tipico: 02-INFO-BUSINESS. Attivato da MKT-Conductor con formato `email-seq` e obiettivo dichiarato `lancio`.

## Input
- Prodotto in lancio: nome, offerta, data apertura carrello, data chiusura
- Lista email disponibile: dimensione, attributi (opt-in source, storico comportamentale)
- ICP + awareness level della lista
- Brand_kit (Mandato Empire di default, override per clienti agency)
- Deadline: le date del lancio sono vincolanti, non indicative

## Pipeline (passi in sequenza)
1. **E3 — Segmentation Analyst:** segmenta la lista per awareness level e comportamento pregresso. Produce i segmenti: acquirenti precedenti, non-acquirenti engagati, non-acquirenti disengagati, nuovi iscritti.
2. **E1 — Lifecycle Architect:** progetta la mappa sequenza lancio:
   - Pre-lancio (3-5 email): valore gratuito, anticipazione, curiosità
   - Apertura carrello (1-2 email): proposta APSOC completa
   - Prova sociale (1-2 email): testimonianze + proof specifica
   - Gestione obiezioni (1-2 email): A6 come motore
   - Scarcity (1-2 email): urgenza reale (scadenza, bonus in esaurimento)
   - Chiusura (1-2 email): ultima occasione, CTA diretta
3. **WF-COPY-EMAIL (L2.1):** copy di ogni email nella sequenza, con branching per segmenti se necessario
4. **E2 — Deliverability Guard:** verifica spam score sequenza + igiene lista + `aidefence_has_pii`
5. **Gate A8 + G2:** ogni email passa G1 ≥80 + G2 brand gate PASS
6. **Consegna a committente:** mappa sequenza + copy + segmentazione + note di implementazione (per review umana nelle prime fasi)

## Gate di uscita
Mappa sequenza approvata da E1 + ogni email con G1 + G2 PASS + E2 report deliverability PASS + `aidefence_has_pii` OK

## Output
Pacchetto lancio completo: mappa sequenza + copy di ogni email + segmentazione lista + subject line options (3 per email) + UTM codes (coordinato con AN1) + note di implementazione per l'ESP

## Tempo stimato
- E3 segmentazione: 20-30 minuti
- E1 mappa sequenza: 30-40 minuti
- WF-COPY-EMAIL (8-10 email): 90-120 minuti
- E2 verifica: 20 minuti
- Totale: 3-4 ore per un lancio completo

## Connessioni
- [[L2.3-EMAIL]] — reparto di riferimento
- [[WF-COPY-EMAIL]] — sub-step obbligatorio per il copy
- [[E1-lifecycle-architect]] — architetto della sequenza
- [[A6-objections-handler]] — motore per le email di obiezione nel lancio
- [[WF-OPTIMIZATION-LOOP]] — dopo il lancio, AN2 analizza le performance email
