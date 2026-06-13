# WF-COPY-SALES-PAGE — Sales Page (gate ≥85)
## Reparto: L2.1 — COPYWRITING

## Trigger
Richiesta con formato `sales-page` o `landing` (con obiettivo di conversione diretto). Gate A8 elevato a ≥85 invece di ≥80 standard. Committenti tipici: 02-INFO-BUSINESS per lanci corsi/ebook, 01-AGENCY per landing offerte clienti.

## Input
- Handoff contract completo: `{committente, formato: "sales-page", awareness_level, icp, obiettivo: acquisto, deadline}`
- Proof obbligatorie: senza proof (testimonianze, dati, risultati) il workflow segnala blocco preventivo — non si lancia una sales page senza evidenze
- Strategia: S1 funnel map se la sales page è parte di un funnel più ampio; S2 posizionamento se non definito
- Brand_kit specifico se cliente agency

## Pipeline (passi in sequenza)
1. **S2 — Positioning Strategist:** statement di posizionamento + 3 angoli da testare (obbligatorio per sales page)
2. **A1 — Briefing Analyst:** briefing completo con proof classificate per forza probatoria
3. **A2 — Target Analyst:** avatar dettagliato + obiezioni top-5 specifiche per questo prodotto
4. **A3 — Attention Writer:** headline principale + 2 varianti alternative (da testare in A/B post-lancio)
5. **A4 — Problem Writer:** agitazione approfondita (200-400 parole) — il problema deve essere sentito visceralmente
6. **A5 — Solution Writer:** presentazione prodotto con proof integrate in CPB (ogni claim ha la sua proof)
7. **A6 — Objections Handler:** 5-7 obiezioni esplicite (sales page ha lo spazio per trattarle tutte)
8. **A7 — CTA Writer:** CTA principale + CTA di recupero a metà pagina + CTA finale con urgenza
9. **A8 — Copy Reviewer:** score ≥85 obbligatorio. Sotto soglia → diagnosi chirurgica + iterazione mirata. Max 3 iterazioni → escalation umana.
10. **SEN-BV — Brand-Voice Sentinel:** gate G2 con attenzione speciale ai claim di income e promesse specifiche

## Gate di uscita
G1: score A8 ≥85 (soglia elevata per sales page)
G2: brand gate PASS (claim tutti supportati da proof)
Entrambi obbligatori.

## Output
Sales page completa: headline + sezioni APSOC complete + proof integrate + CTA multi-punto + score A8 + qa_report + brand_gate_report

## Tempo stimato
90-120 minuti senza iterazioni. +25-35 min per ogni iterazione G1.

## Note operativa
- Se le proof sono insufficienti → A1 segnala PRIMA di avviare la pipeline. Non si avvia WF-COPY-SALES-PAGE senza material di proof minimo.
- Il gate ≥85 esiste perché la sales page ha il maggior impatto sul revenue: un punto di score si traduce in conversioni mancate.

## Connessioni
- [[L2.1-COPYWRITING]] — reparto di riferimento
- [[WF-COPY-FULL]] — questo workflow estende WF-COPY-FULL con la soglia elevata e i passi aggiuntivi
- [[S2-positioning-strategist]] — obbligatorio per sales page
- [[A8-copy-reviewer]] — gate elevato a ≥85
