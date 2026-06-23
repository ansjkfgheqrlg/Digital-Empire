---
Type: PRINCIPI
Status: Active
Tags: #principi #content-factory #CF-R7 #pubblicazione #review-umana #orchestratori #ADR-003
Created: 2026-06-23
Last updated: 2026-06-23
---

# Principi Operativi — CF-R7 Pubblicazione & Distribuzione

> **Reparto:** CF-R7 · **Area:** Post-Produzione
> **[WRAPPA] orchestratori Python ATTIVI — runtime NON modificato (ADR-003)**

---

## Principio 1 — Nessuna pubblicazione senza review umana e gate verdi (NON NEGOZIABILE)

Prima di ogni pubblicazione social devono essere soddisfatte **contemporaneamente** tre condizioni:
1. Gate verdi CF-R6 in `state.json` (gate_formato + gate_brand + gate_copy + gate_mandato: tutti PASS).
2. Review umana documentata (`review_umana.eseguita: true, ts: "...", nome: "..."`).
3. Token canale validi per ogni piattaforma target.

Manca anche una sola condizione → BLOCCO automatico. Non si negozia, non si fa eccezione.
La review umana è policy Board (V2): non può essere rimossa né bypassata da alcun agente.

Ogni prodotto pubblicato rappresenta il brand del committente. Un errore visibile è
un danno reputazionale reale. Il gate manuale esiste perché la macchina non vede il contesto.

---

## Principio 2 — Gli orchestratori Python si wrappano, non si riscrivono (ADR-003 SUPREMA)

I file `main_orchestrator.py` e `mentalita_orchestrator.py` in
`SKILL & Agenti/Workflow pubblicazione automatica/` sono motori di pubblicazione ATTIVI in
produzione. Non si toccano, non si modificano, non si riscrivono per nessuna ragione.

Il reparto CF-R7 interagisce con essi ESCLUSIVAMENTE tramite i wrapper dichiarati
in `scripts/README.md`. Ogni file che li utilizza dichiara esplicitamente:
`[WRAPPA] orchestratore Python — runtime non modificato`.

Modificare un orchestratore attivo = rischio pubblicazione su canali reali non controllata.
ADR-003 è suprema in tutta la gerarchia CF-DE.

---

## Principio 3 — Token scaduti = blocco immediato

Un token canale scaduto non è un problema minore da gestire "nel frattempo". È un BLOCCO.
CF-R7-QA rileva il token scaduto e ferma la pipeline. CF-R7-COORD notifica il committente.
Nessun agente tenta di pubblicare con credenziali invalide: il risultato sarebbe un errore
silenzioso o una pubblicazione parziale non tracciabile.

Il rinnovo token è operazione umana: il committente rinnova; CF-R7-QA ricontrolla; si riparte.

---

## Principio 4 — Dry-run prima di ogni pubblicazione ad alto rischio

Per ogni primo ciclo publish su un brand o canale non recentemente testato: eseguire il
dry-run (WF-PUBLISH-SOCIAL passo 0) e leggere il piano prima di procedere. Il dry-run
produce il piano completo (asset, canali, caption adattate, orchestratore) senza toccare
i canali. È la base per la review umana strutturata.

Il dry-run non è un passo opzionale "per chi ha tempo": è il modo in cui la review umana
funziona in modo informato. Chi approva deve sapere cosa viene pubblicato, dove e quando.

---

## Principio 5 — Metriche reali, non stime (Mandato Art.2 — "prove non promesse")

CF-R7-FEEDBACK raccoglie metriche dalle API delle piattaforme. Non stima, non interpola,
non usa dati proxy. Se un'API non restituisce dati → si registra "non disponibile" con motivo.

Nessuna analisi di pattern su n < 5 pezzi dello stesso tipo/brand: dati insufficienti non
portano a conclusioni, portano a rumore. I dati si accumulano in `cf/patterns`; CF-R8 analizza
quando il corpus è sufficiente. La velocità non giustifica conclusioni false.

---

## Principio 6 — Tracciabilità completa: ogni azione in trace.jsonl

Ogni evento della pipeline publish — check pre-publish, adattamento, publish, verifica URL,
ricezione conferma — produce una riga append-only in `orders/<id>/trace.jsonl`. Non si
cancella, non si sovrascrive, non si omette.

L'URL definitivo di ogni post pubblicato è registrato in `trace.jsonl` e in `state.json`.
In caso di problema post-publish, il trace è l'unica fonte di verità.

---

## Connessioni

- [[CF-R7-Pubblicazione/ARCHITETTURA]] · `ARCHITETTURA.md` — architettura gate e pipeline
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R7`
- [[company/Memory/decisions/ADR-003]] · ADR-003 — wrap senza modifica runtime
