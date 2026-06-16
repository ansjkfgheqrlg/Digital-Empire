# T-org-design — Funzione L4: Org Design di Team e Reparti

> **Ecosistema:** Genesi-Core / FORGE · **Reparto:** AGENT-WORKS (L2.2) · **Workflow:** WF-TEAM-NEW · WF-ECOSYSTEM-NEW
> **Motore reale:** `agent-factory/agent-architect` + `architect-agent` + `prd-architect-os` — vedi `Motori/Mappa-Motori.md` #6 #8 #11
> Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]] · [[Motori/Mappa-Motori.md]]

---

## Missione
Disegnare l'**org chart** di un team L3/L4 o di un ecosistema L1, applicando lo schema canonico CF
(coordinator + workers + escalation + shared_state). **Nota di confine:** lo *schema* (forma) è di
ARCHITETTURA (`Schema-Team`, `Schema-Ecosistema`); T-org-design lo *istanzia* col contenuto reale —
ruoli concreti, tier giustificati, responsabilità precise. Agente: `frg-org-designer` (Opus — il design
è una decisione architetturale).

---

## Responsabilità
- Definire il coordinator (chi pianifica, distribuisce, aggrega).
- Definire i worker (uno per responsabilità; nessun overlap).
- Definire le dipendenze tra ruoli (chi passa il lavoro a chi).
- Definire l'escalation (a chi va il task se fallisce dopo N tentativi).
- Produrre l'org chart in formato text (ASCII tree + tabella).
- Verificare che i confini siano espliciti (cosa fa ogni ruolo, cosa NON fa).

---

## Schema canonico CF (obbligatorio — non modificabile senza ADR via ARCHITETTURA)
```
Team <nome> (L3 o L4)
├── coordinator (<tier>)
│   Resp.: riceve task, pianifica, assegna, aggrega · Escalation: N fallimenti → <reparto superiore>
├── worker-1 (<tier>)  Resp.: [una funzione] · Input: [...] · Output: [formato + acceptance]
├── worker-2 (<tier>)  ...
└── reviewer (opzionale, <tier>)  Resp.: verifica output prima della consegna al coordinator
```

---

## Principi di org design per EMPIRE OS
1. **Un ruolo = una responsabilità** (no bottleneck invisibili).
2. **Tier al ribasso** — il modello più economico che regge il task.
3. **Escalation sempre definita** — un team senza escalation non è pronto per produzione.
4. **Confini con team adiacenti** — documentare cosa NON fa (anti-overlap).
5. **Schema fisso, contenuto variabile** — struttura identica tra i team; cambiano ruoli e responsabilità.

---

## Quando si usa per ECOSYSTEM-WORKS
Per un ecosistema intero (WF-ECOSYSTEM-NEW, su `HC-ARCH-FORGE-ECO`), T-org-design produce:
tutti i reparti L2 con missione · tutti i workflow L3 con descrizione · tutti i team L4 con org chart ·
il roster L5 completo (ID, ruolo, tier). Output: tabella per `ECOSISTEMA.md` + file Reparti/Workflow/Funzioni/.

## KPI
| Metrica | Target |
|---|---|
| Team con overlap di responsabilità tra worker | 0 |
| Team senza escalation protocol | 0 |
| Team con tier non giustificato (Opus su task Tier 1) | 0 |
| Org chart conformi allo schema canonico | 100% |
