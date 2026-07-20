# PLAYBOOK — youtube-script-factory (uso operativo nel W7)

## Scenario 1 — Scrivere lo script di un video del batch (felice)
1. Da `/youtube-lead-machine` (o da kit `batch-XX`): arriva titolo-lavoro + tipo video (Anchor/Shift/Conversion/Audit) + ICP di turno.
2. Aprire SEZIONE 6 (cheat sheet) per il tipo giusto → struttura e timing.
3. `python3 tools/genera_script.py` → bozza 7 componenti (hook da formula della categoria giusta).
4. Rivedere a mano con VOCE DE (SEZ 1): ≤15-20 parole/frase, "tu" diretto, zero hype/guru, CTA 3 livelli
   (preview nel setup ~30s · reminder a metà · finale dopo ricap) — varianti finale: Lead Magnet / Call Diretta / Doppia.
5. `python3 tools/checklist_qualita.py` → score 45pt. Fascia 🟡+ necessaria prima di fissare la registrazione.
6. Registrare il video nel backlog (`backlog_manager.py aggiungi_video`) con stato "script pronto".

## Scenario 2 — Variant title/thumbnail per un video già scritto (edge)
`genera_script.py` sezione titoli (6 formule, <60 caratteri, 5 varianti) + quick check thumbnail
(SEZ 6): max 4-5 parole, faccia espressiva, contrasto, 3 concept → sceglie il frontman/Max.

## Scenario 3 — Review settimanale (da ANALYTICS-REVIEW della skill /youtube-lead-machine)
`backlog_manager.py` → `aggiorna_performance` con CTR/retention/lead per video →
l'output alimenta la review della skill madre (regola: la skill madre legge i KPI, questa factory tiene la pila).

## Scenario 4 — Il risultato dello scoring è 🔴 (<20)
PERCORSO FALLIMENTO: NON programmare la registrazione. Riscrittura mirata sulle sezioni carenti report
(il report punta le sezioni), poi re-score. Persistenza del 🔴 2 volte → failure-modes F3/F6 + registro.

## Confini (contratto di delega, da gate skill)
- **Scrive script, non strategia.** Il 70/20/10 del mix, ICP, funnel, hook strategici → `/youtube-lead-machine`.
- **Non fa review APSOC** del copy di marketing → quello è `copy-workflow` (gate L2-1).
- **Non pubblica né misura live** → analytics vere = review settimanale della skill madre.
