# WF-COPY-AD — Ad Copy 3 Varianti
## Reparto: L2.1 — COPYWRITING (serve L2.2 — ADVERTISING)

## Trigger
Richiesta con formato `ad`, `yt-meta`, `listing`, o qualsiasi formato breve per piattaforme paid. Attivato da copy-master. Usato come sub-step interno di WF-ADS-CAMPAIGN (L2.2).

## Input
- Handoff contract: `{committente, formato: "ad", awareness_level, icp, obiettivo, deadline}`
- Piattaforma target: Meta / Google / LinkedIn / TikTok / YouTube (influenza i vincoli di lunghezza)
- Brief varianti: angoli da testare (da S2 se disponibili, altrimenti A3 propone)
- Copy_id precedente se in fase di iterazione (AD2 itera dal winner)

## Pipeline (passi in sequenza)
1. **A2 — Target Analyst:** recupera avatar da memoria o costruisce (se non in cache)
2. **A3 — Attention Writer (parallelo ×3):** 3 varianti hook con strategie diverse (fan-out swarm)
   - Variante 1: hook primario (strategia ad alto CTR atteso per quell'ICP)
   - Variante 2: hook alternativo (strategia diversa — contrarian, proof, curiosity-gap)
   - Variante 3: hook di scoperta (angolo inaspettato per test audience)
3. **A4-A5-A6 condensati:** per il formato ad, le sezioni P/S/O si fondono nel corpo dell'ad (50-150 parole secondo piattaforma) — copy-master gestisce la condensazione
4. **A7 — CTA Writer:** CTA specifica per la piattaforma (character limit rispettato)
5. **A8 — Copy Reviewer:** score ≥80 su tutte e 3 le varianti (o ≥80 su almeno 2, con la terza ≥70 per testing)
6. **SEN-BV — Brand-Voice Sentinel:** gate G2 su ogni variante

## Gate di uscita
Almeno 2 varianti con G1 ≥80 e G2 PASS. 3 varianti ideale per matrice AD2.

## Output
3 varianti ad con: copy completo (headline + corpo + CTA), score A8 per variante, strategia hook dichiarata, note platform-specific

## Tempo stimato
15-20 minuti (3 varianti in parallelo con fan-out swarm)

## Connessioni
- [[L2.1-COPYWRITING]] — reparto di riferimento
- [[WF-ADS-CAMPAIGN]] — questo workflow è un sub-step di WF-ADS-CAMPAIGN
- [[AD2-creative-iterator]] — riceve le varianti copy per costruire la matrice creativa
