> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.2 (Team L4) + sez. 4b (WF-LANCIO)

# T-CALENDARIO — Team Calendario Lancio

> Funzione L4 · Reparto: IB-R2-LANCI · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Costruire e mantenere la **timeline T-30→T+7** per ogni lancio: dipendenze tra task,
owner per ciascun deliverable, milestone di gate, slot dry-run. La timeline è il
contratto operativo del lancio — ogni scostamento deve essere dichiarato a
`ib-lanci-coordinator` entro 24h dal rilevamento.

---

## Agente proprietario

`ib-launch-planner` (worker, tier Sonnet)

---

## Output: timeline lancio (struttura)

```
T-30  Calendario completo + dipendenze → approvato da ib-lanci-coordinator
T-28  HANDOFF → 08-INTELLIGENCE (customer research, angoli)
T-21  HANDOFF → 03-CONTENT-FACTORY (contenuti organici pre-lancio)
T-14  HANDOFF → 04-MARKETING (sales page + sequenza pre-lancio)
T-7   Verifica rientro email cart open/close da MARKETING (ib-copy-liaison)
T-3   Checklist asset 100% (T-asset-lancio)
T-1   DRY-RUN completo → Cost-Sentinel stima costi
T-0-ε GO/NO-GO (hive-mind consensus)
T0    CART OPEN
T+1..n Monitoraggio conversioni (ib-tracking-analyst ogni 24h)
CART CLOSE (ultime 48h) — scarcity REALE
T+1→T+7 Post: onboarding + debrief + crosssell scout
```

---

## Skill da usare

`launch-runbook` (da creare via 07-FORGE): genera automaticamente la timeline con dipendenze,
checklist asset, gate, dry-run e go/no-go a partire dalla data T0 dichiarata.

---

## Connessioni

- [[IB-R2-LANCI]] — reparto di appartenenza
- [[T-COPY-LIAISON]] — dipendente: riceve dal calendario le deadline per i copy da richiedere
- [[T-ASSET-LANCIO]] — dipendente: usa il calendario per la checklist
- [[WF-LANCIO]] — workflow che include questa funzione
