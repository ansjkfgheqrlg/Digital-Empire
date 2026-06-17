---
Type: WORKFLOW
Status: Active
Tags: #workflow #cmo #brand #apsoc #gate #always-on #bloccante
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-BRAND-GATE — Workflow Gate Voce e APSOC (Always-On)

> **ID:** WF-CMO-002 · **Owner:** cmo-brand-voice-warden · **Trigger:** qualsiasi output di conversione
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CMO.md`
> **Standard:** CF-grade — gate bloccante, log obbligatorio, nessun bypass.

---

## Scopo

Garantire che nessun output di conversione di Digital Empire esca senza soddisfare
simultaneamente: (a) Brand Voice conforme al Mandato Art.2, e (b) score APSOC sopra la soglia
del formato. Il gate è always-on: si attiva su ogni copy, indipendentemente da canale, urgenza,
o chi ha richiesto l'output. Non è un gate "consigliato": è un gate bloccante (Mandato Art.4.1).

---

## Perimetro — cosa passa per questo workflow

Ogni output che contiene testo destinato a un pubblico esterno (o a un cliente) per finalità
di conversione, acquisizione, o vendita:

| Formato | Soglia APSOC | Note |
|---|---|---|
| Cold email | ≥80 | ogni email singola o sequenza |
| DM LinkedIn/Instagram | ≥80 | outreach e follow-up |
| Post social con CTA | ≥80 | non post awareness puri |
| Landing page | ≥80 | entry point campagna |
| Sales page | ≥85 | pagina di vendita prodotto |
| Proposta commerciale | ≥85 | preventivo + offerta cliente |
| Ads copy | ≥80 | headline e body ads |
| Newsletter con offerta | ≥80 | email con CTA di acquisto o lead |

Output esclusi (contenuto puro, nessuna CTA di conversione): post educativi senza CTA,
contenuti interni, documentazione tecnica. Se dubbio → il gate si applica.

---

## Flusso

```
[STEP 1 — RICEZIONE]
  Owner: cmo-brand-voice-warden
  Input: output testuale + metadati (formato, brand_kit, icp, awareness_level, canale)
  Gate immediato: brand_kit dichiarato? NO → FAIL immediato "brand_kit mancante — invalido per Mandato Art.6.1"

[STEP 2 — CPB CHECK (prioritario)]
  Owner: cmo-brand-voice-warden
  Action: scansione di ogni affermazione: ha una Proof? (Claim → Proof → Benefit)
  Regola: anche un solo claim centrale senza proof = FAIL immediato, indipendentemente dal resto
  Output: lista claim senza proof (se presente) | "CPB OK — tutti i claim hanno proof"

[STEP 3 — SCORE APSOC]
  Owner: cmo-brand-voice-warden
  Action: scoring per sezione con pesi standard:
    A (Attenzione): 15 pts — Barnum/Rainbow? Specifico sulla nicchia? No genericità?
    P (Problema): 20 pts — agitazione a 3 livelli? quantificata? P prima di S?
    S (Soluzione): 20 pts — social proof? caso studio? prodotto chiaramente identificato?
    O (Obiezioni): 15 pts — anticipa l'obiezione principale per questo ICP?
    C (CTA): 20 pts — micro-commitment? bassa frizione? un solo invito all'azione?
    Bonus V (Valore concreto): 10 pts — qualcosa applicabile da soli prima della CTA?
  Penalità automatica: P dopo S = −15 (non discrezionale, Mandato Art.4.2)
  Output: score_totale + score_per_sezione

[STEP 4 — BRAND GATE G2 (checklist binaria)]
  Owner: cmo-brand-voice-warden
  Checklist:
    [ ] Voce diretta, provocatoria, trasparente — niente qualificatori molli
    [ ] Ogni claim ha proof (CPB) — già verificato in STEP 2
    [ ] Struttura APSOC rispettata — P prima di S
    [ ] Pricing corretto se presente — one-time, nessun canone implicito (Mandato Art.3.2)
    [ ] Zero AI-slop — niente frasi generiche, aggettivi senza numeri, icebreaker vuoti
    [ ] Autonomia cliente — niente dependency-language (Mandato Art.1.2)
    [ ] brand_kit + icp dichiarati — già verificato in STEP 1
  Tutti e 7: ✓ → G2 PASS | anche uno solo ✗ → G2 FAIL

[STEP 5 — VERDETTO]
  PASS: score ≥ soglia formato AND CPB OK AND G2 tutti ✓
  → output: { gate_pass: true, score: X, sezioni: {...}, feedback: "approvato" }
  → log in board/cmo/brand-gate-log/<copy-id>.json

  FAIL: score < soglia OPPURE CPB violato OPPURE G2 con ✗
  → output: { gate_pass: false, score: X, blocchi: [...], feedback_granulare: {...} }
  → log in board/cmo/brand-gate-log/<copy-id>.json
  → notifica al conductor (non all'ecosistema direttamente)
  → il conductor notifica al liaison che gestisce il canale per il brief di fix

[STEP 6 — BYPASS REQUEST (se arriva)]
  Owner: cmo-brand-voice-warden
  Regola: nessun bypass eseguito. Mai.
  Risposta automatica: "gate non bypassabile — Mandato Art.4.1. Unico sblocco lecito: deroga
  formale del Board via hive-mind raft, depositata in Memory/decisions/."
  Notifica: conductor + CEO (se l'urgenza è dichiarata come critica).
```

---

## State (namespace AgentDB)

```
board/cmo/brand-gate-log/
  ├── <copy-id>.json        — ogni check: input, score, sezioni, G2, esito, timestamp
  └── aggregate-stats.json  — statistiche aggregate: first-pass rate, score medio, sezioni più fallite
```

---

## Gate non bypassabili

- **Nessun output esce con gate FAIL** — punto fermo, non negoziabile (Mandato Art.4.1).
- **Nessun output esce senza log** — ogni check produce un record permanente.
- **brand_kit mancante = FAIL immediato** — non si improvvisa la voce di un cliente o un brand non dichiarato.
- **CPB violato = FAIL bloccante** — indipendentemente dallo score totale.

---

## Connessioni

- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[cmo-conductor]] · `agenti/cmo-conductor.md`
- [[cmo-marketing-liaison]] · `agenti/cmo-marketing-liaison.md`
- [[cmo-content-liaison]] · `agenti/cmo-content-liaison.md`
- [[WF-CAMPAGNA]] · `workflow/WF-CAMPAGNA.md` — STEP 7 di WF-CAMPAGNA è questa WF
- [[WF-LANCIO-COORD]] · `workflow/WF-LANCIO-COORD.md` — gate sales page usa questa WF
- [[MANDATO-EMPIRE]] Art.2.2 (CPB) + Art.4.1 (gate non bypassabili) + Art.4.2 (APSOC) + Art.6.1 (brand_kit)
- [[Framework_Cold_Outreach_APSOC]] · `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`
