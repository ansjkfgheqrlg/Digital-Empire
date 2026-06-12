> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 AGENT-WORKS · L4 T-org-design

# T-org-design — Funzione L4: Org Design di Team e Reparti

**Ecosistema:** 07-FORGE · **Reparto:** AGENT-WORKS (L2.2) · **Workflow:** WF-TEAM-NEW · WF-ECOSYSTEM-NEW

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Disegnare l'**org chart** di un team L3/L4 o di un ecosistema L1, applicando lo schema
canonico di Content Factory Exponium (coordinator + workers + escalation + shared_state).
Agente operatore: `frg-org-designer` (Opus — il design è una decisione architetturale).

---

## Responsabilità

- Definire il coordinator del team (chi pianifica, distribuisce, aggrega)
- Definire i worker (uno per responsabilità; nessun overlap)
- Definire le dipendenze tra ruoli (chi passa il lavoro a chi)
- Definire l'escalation (a chi va il task se fallisce dopo N tentativi)
- Produrre l'org chart in formato text (ASCII tree + tabella)
- Verificare che i confini siano espliciti (cosa fa ogni ruolo, cosa NON fa)

---

## Schema canonico CF (obbligatorio — non modificabile senza ADR)

```
Team <nome> (L3 o L4)
├── coordinator (<tier>)
│   Responsabilità: riceve task, pianifica, assegna ai worker, aggrega output
│   Escalation: se N fallimenti → segnala a <reparto superiore>
├── worker-1 (<tier>)
│   Responsabilità: [una sola funzione]
│   Input: [da coordinator o da worker precedente]
│   Output: [formato e acceptance]
├── worker-2 (<tier>)
│   ...
└── reviewer (opzionale, <tier>)
    Responsabilità: verifica output workers prima di consegnare al coordinator
```

---

## Principi di org design per EMPIRE OS

1. **Un ruolo = una responsabilità**: i worker non fanno due cose diverse (rischio di bottleneck invisibile)
2. **Tier al ribasso**: ogni ruolo va sul modello più economico che regge il task
3. **Escalation sempre definita**: un team senza protocollo di escalation non è pronto per produzione
4. **Confini con gli altri team**: per ogni team documentare cosa NON fa (anti-overlap con team adiacenti)
5. **Schema fisso, contenuto variabile**: la struttura è identica tra tutti i team; ciò che cambia sono ruoli e responsabilità

---

## Quando si usa per ECOSYSTEM-WORKS

Per un ecosistema intero, T-org-design produce:
- Tutti i reparti L2 con missione
- Tutti i workflow L3 con descrizione
- Tutti i team L4 con org chart
- Il roster L5 completo (N agenti con ID, ruolo, tier)

Output: tabella compatta per ECOSISTEMA.md + file Reparti/Workflow/Funzioni/ per popolare le cartelle

---

## KPI

| Metrica | Target |
|---|---|
| Team con overlap di responsabilità tra worker | 0 |
| Team senza escalation protocol | 0 |
| Team con tier non giustificato (Opus su task Tier 1) | 0 |
| Org chart prodotte conformi allo schema canonico | 100% |
