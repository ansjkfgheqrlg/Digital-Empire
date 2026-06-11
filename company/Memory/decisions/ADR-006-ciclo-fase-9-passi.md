# ADR-006 — Il Ciclo di Fase Empire a 9 passi sostituisce "fase→controllo→avanti"

- **Data:** 2026-06-11
- **Stato:** ATTIVO
- **Decisori:** Max (direttiva: "il metodo va arricchito e reso molto migliore, chirurgico")

## Contesto
"Fase → controllo → avanti" è troppo povero: non copre coordinamento a 2 persone su account
condiviso, morte degli agenti (rete/limiti), review indipendente, budget, retro. Le lezioni
reali lo confermano: scritture concorrenti su wiki/log (CP-001), 6 agenti swarm morti su
session limit a metà fase (CP-005).

## Decisione
1. Ogni fase segue il **Ciclo di Fase Empire a 9 passi**: 0 RECALL → 1 SPEC → 2 PRE-MORTEM →
   3 BUILD → 4 GATE automatico → 5 REVIEW indipendente → 6 TEST funzionale/amnesia →
   7 COMMIT → 8 RETRO. Documento canonico: `PIANO-MAESTRO/10-METODO-CICLO-FASE.md`.
2. **Swarm obbligatorio per TUTTI** (Max e Gael): lavoro su ≥2 aree disgiunte → agenti
   paralleli, mai un agente solo. Gael ha le stesse identiche capacità (stesso account
   Claude, stesso repo, stesse skill/CLAUDE.md condivisi): lo swarm lo lancia Claude Code,
   non la persona.
3. Regole trasversali non negoziabili: prompt idempotenti, coordinamento via STATO-EMPIRE
   pushato PRIMA del build, budget-guard al 20%, gate mai bypassabili, una fase per ciclo.
4. Il metodo è codificato anche nel CLAUDE.md del progetto (eredità automatica per Gael)
   e nella skill `empire-context`.

## Alternative scartate
- Tenere il metodo semplice — già fallito due volte (CP-001, CP-005).
- Processo diverso per Max e per Gael — account e repo condivisi: un metodo solo.

## Conseguenze
- Ogni CP di fase include la mini-checklist dei 9 passi compilata.
- Le fasi costano un filo di più in setup (SPEC+PRE-MORTEM ≈ 10 min) e molto meno in disastri.

## Contradiction-check
Estende ADR-002 (il passo 0/7 È memory-first) e ADR-005 (passo 1: minori→BACKLOG).
Nessun conflitto.
