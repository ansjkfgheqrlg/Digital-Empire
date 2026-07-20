# EVALS — youtube-script-factory (retrofit MIR-5 sprint 1)

Casi di attivazione/uso atteso (criterio skill-creator: attiva corretta? output al livello DE? deleghe rispettate?).

| # | Scenario (input utente) | Atteso | Tipo |
|---|---|---|---|
| E1 | "Devo scrivere lo script di V07 (Anchor) su 'ads senza richieste'" | Follow playbook Scenario 1: struttura Anchor 70% (SEZ 6), hook categoria PROBLEMA RICONOSCIBILE, 7 componenti completi, CTA 3 livelli | happy |
| E2 | "Fammi 5 titoli per il video audit dal vivo" | 6 formule titolo, <60 car, 5 varianti; ricorda thumbnail 3 concept (SEZ 6) | happy |
| E3 | "Questo script è pronto da registrare?" | Esegue checkpoint: non decide a sentimento — `checklist_qualita.py` 45pt, riporta fascia; 🔴<20 → riscrittura sezioni carenti | gate |
| E4 | "Perché questo mese usciranno 3 video Anchor e 1 Shift?" | Risponde dal mix target 70/20/10 del backlog manager, non inventa strategia (delega a /youtube-lead-machine) | boundary |
| E5 | "Scrivimi una review APSOC della landing page" | **RIFIUTA/delega**: APSOC = `copy-workflow` (skill diversa). Questa factory = solo script video | boundary (anti-sconfinamento) |
| E6 | "Qual è la strategia del canale?" | Rimanda a `Formazzione/Youtube/STRATEGIA-YOUTUBE-LEAD-MAGNET.md` e a `/youtube-lead-machine` — non la reinventa | boundary |
| E7 | "Aggiungi il video 'Sito bello ≠ vende' al backlog e segna score 38/45" | `backlog_manager.py` aggiungi_video + aggiorna_quality_score; mix counting aggiornato | ops |

**Esito atteso al retrofit (gate):** un operatore nuovo trova in ≤2 minuti: cosa fa la factory,
come invocare i 3 tool, dove sono le regole VOCE/CTA/scoring, e cosa NON fa (deleghe). Se cerca nel
markdown 5.166 righe senza indice → wrap fallito (E7-pratica).
