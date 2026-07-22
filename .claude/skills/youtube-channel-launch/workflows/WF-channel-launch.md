# WF-CHANNEL-LAUNCH — dal nulla al canale pronto a pubblicare

> **Quando:** apertura di un canale nuovo, o riposizionamento di uno esistente che non cresce.
> **Esito:** `launch-verdict.md` VERDE → si passa a `youtube-automation-factory` per il primo video.

---

## DAG

```
INPUT: nicchia validata (da niche-scout) + lingua + mercato
   │
   ▼
[L1] channel-architect      → nome, handle, posizionamento, FORMAT ripetibile, pilastri
   │        (blocca tutto il resto: gli altri dipendono dalla scheda-canale)
   ├──────────────┬──────────────────┐        ← L2, L3, L4 in PARALLELO
   ▼              ▼                  ▼
[L2]            [L3]               [L4]
brand-designer  channel-seo        monetization-planner
(brand-kit)     (channel-seo.md)   (piano-monetizzazione)
   │              │                  │
   └──────────────┴──────────────────┘
                  ▼
            ⟨launch-gate⟩            ← 8 requisiti, tutti VERI o ROSSO
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   🟢 VERDE              🔴 ROSSO
   → factory F1          → torna all'agente che deve completare
   (primo video)
```

**Nota sull'ordine:** `channel-architect` è sequenziale (produce la scheda da cui dipendono gli
altri tre). L2-L3-L4 sono aree disgiunte → parallelizzabili in swarm.

---

## Passi

| # | Chi | Fa | Output |
|---|---|---|---|
| 1 | conductor | raccoglie nicchia validata, lingua, mercato, cadenza sostenibile | input |
| 2 | `channel-architect` | promessa, format (test della frase), pilastri, nome+handle | `scheda-canale.md` |
| 3 | `brand-designer` | palette, tipografia, logo/banner brief, **template miniature** | `brand-kit.md` |
| 4 | `channel-seo` | descrizione, keyword canale, playlist per pilastro, trailer | `channel-seo.md` |
| 5 | `monetization-planner` | progresso YPP, collo di bottiglia, scenari, break-even | `piano-monetizzazione.md` |
| 6 | `policy-checker` (compliance-shield) | nicchia sensibile? disclaimer? | `policy-report.md` |
| 7 | `launch-gate` | 8 requisiti → verdetto | `launch-verdict.md` |
| 8 | conductor | VERDE → handoff factory F1 · ROSSO → riassegna | decisione |

---

## Precondizioni
- La nicchia è già stata validata (non si lancia su un'intuizione: serve il `niche-scout`).
- L'utente ha dichiarato una **cadenza sostenibile** reale (non quella ideale): entra nei conti di
  monetizzazione ed è la prima cosa che salta.

## Criteri di uscita
- 4 artefatti + report policy prodotti.
- Verdetto verde motivato requisito per requisito.
- Scheda canale salvata come fonte di verità per il `niche-gate` della factory.

## Errori tipici
| Errore | Conseguenza | Prevenzione |
|---|---|---|
| Lanciare senza format ripetibile | ogni video è un progetto, non scali | requisito 1 del gate |
| Miniature improvvisate video per video | il canale non si riconosce nel feed | template miniature obbligatorio |
| Piano solo ottimista | si molla al terzo mese | scenario pessimista obbligatorio |
| Nicchia sensibile senza disclaimer | monetizzazione limitata | passo 6 obbligatorio |
