# WF-COPY-FULL — Pipeline Copy Completo (A1→A8)
## Reparto: L2.1 — COPYWRITING

## Trigger
Richiesta con formato `full`, `sales-page` (quando non abbastanza complessa per WF-COPY-SALES-PAGE), `vsl`, o progetto complesso che richiede tutto il framework APSOC da zero. Attivato da copy-master dopo routing MKT-Conductor.

## Input
- Handoff contract validato: `{committente, formato, awareness_level, icp, obiettivo, deadline}`
- Materiali opzionali: proof, case study, briefing esistente, brand_kit
- Output di S1/S2/S3 se il progetto richiede strategia preliminare

## Pipeline (passi in sequenza)
1. **A1 — Briefing Analyst:** raccoglie e struttura tutti i requisiti → `briefing-completo.md`
2. **A2 — Target Analyst:** costruisce/recupera avatar ICP + language map → `avatar-{icp}.md`
3. **[Opzionale] S2 — Positioning Strategist:** se il posizionamento non è chiaro → statement + angoli
4. **A3 — Attention Writer:** 3-5 varianti headline/hook con strategia dichiarata → sezione A
5. **A4 — Problem Writer:** agitazione problema + conseguenze + frase-ponte → sezione P
6. **A5 — Solution Writer:** USP + benefits CPB + descrizione del "dopo" → sezione S
7. **A6 — Objections Handler:** 3-7 obiezioni principali in formato CPB → sezione O
8. **A7 — CTA Writer:** CTA principale + micro-copy + urgenza reale + reassurance → sezione C
9. **A8 — Copy Reviewer:** score APSOC 100pt → gate G1 (≥80 standard / ≥85 sales page)
   - Score ≥ soglia → passa a Brand-Voice Sentinel
   - Score < soglia → iterazione mirata sulla sezione diagnosticata (max 3 iterazioni)
10. **SEN-BV — Brand-Voice Sentinel:** checklist Mandato Empire → gate G2 PASS/FAIL
11. **hooks post-task:** `memory_store` score + pattern usati → `wiki/log.md`

## Gate di uscita
G1: score A8 ≥80 (≥85 per sales page)
G2: brand gate SEN-BV PASS
Entrambi obbligatori. Output non esce finché entrambi non sono verdi.

## Output
Handoff response: `{copy_finale, score_A8, qa_report, brand_gate: pass/fail, pattern_usati}`

## Tempo stimato
- Formato standard: 60-90 minuti (pipeline completa senza iterazioni)
- Con iterazioni G1: +20-30 minuti per iterazione
- Con S2 Positioning: +20 minuti aggiuntivi

## Connessioni
- [[L2.1-COPYWRITING]] — reparto di riferimento
- [[copy-workflow-wrapper]] — il motore operativo su cui questo workflow si appoggia
- [[MKT-0-conductor]] — router che attiva questo workflow
