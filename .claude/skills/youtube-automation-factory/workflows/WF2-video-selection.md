# WF2 — Video Selection (Fase 2) — il "momento chiave"

> Obiettivo: dai candidati alla **decisione A/B** su quale video replicare. Qui non si sbaglia (MKD §2.3).

## DAG
```
[input: nicchia certificata + canali cash cow]
   │
   ├──► video-hunter ── candidati-video.md (views/ora, lingua, in-nicchia)
   │
   └──► seo-analyst ── seo-report.md (seo_score.py + diagnosi errori + etichetta A/B)
              │
              ▼
   DECISIONE (conductor):
     A-upside     = video forte ma SEO debole  → copiabile MIGLIORANDO la SEO (puoi superarlo)
     B-sicurezza  = video con SEO già buona     → contenuto sicuro, riusi la sua SEO
              │
              ▼
   [output: video scelto + etichetta + lista errori da correggere] → memory-keeper (DEC) → WF3
```

## Regola di decisione (dal caso "Legami d'amore", MKD §2.3)
| Situazione candidato | Scelta | Perché |
|---|---|---|
| SEO assente + molto successo | **A (upside)** | correggendo la SEO puoi fare più dell'originale |
| SEO buona | **B (sicurezza)** | ben posizionato: riusi la SEO chiavi-in-mano |
| Due pari livello | dipende dal livello: **principiante→B**, **esperto con tempo→A** | rischio vs upside |

## Passi
1. `video-hunter`: 5-15 candidati con views/ora reali, lingua, in-nicchia sì/no.
2. `seo-analyst`: punteggio + diagnosi errori (curva performance) + etichetta A/B per ciascuno.
3. Conductor decide A o B citando le metriche.
4. `memory-keeper`: `DEC-video-<slug>.md` (video scelto, etichetta, errori da correggere).

## Definition of Done
- [ ] ≥3 candidati con metriche reali
- [ ] Ogni candidato ha punteggio SEO + diagnosi errori
- [ ] Decisione A/B motivata con numeri
- [ ] DEC salvata con la lista errori per WF3
