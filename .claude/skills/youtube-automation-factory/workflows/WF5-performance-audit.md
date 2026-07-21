# WF5 — Performance Audit (Fase 6) + feedback loop

> Obiettivo: misurare il video pubblicato, **diagnosticare l'errore** e **rimettere in moto il loop**.

## DAG
```
[input: video pubblicato (dopo finestra di raccolta dati)]
   │
   ▼
performance-auditor ── legge metriche reali (Video IQ / Studio, account neutro per il confronto)
   │
   ▼
CLASSIFICA la curva:
   picco-poi-calo   → errore SEO (keyword/descr/tag)     → azione: rivedi metadati
   crescita lenta    → errore thumb/titolo/descrizione     → azione: cambia thumb+titolo (post-pubbl.)
   piatta/in salita  → confronta con target + studia i successi (cosa replicare)
   │
   ▼
audit-report.md (diagnosi + azione correttiva + confronto vs target)
   │
   ▼
FEEDBACK:
   pivot nicchia?   → WF1 (niche-scout)
   scelta migliore? → WF2 (video-hunter/seo-analyst)
   metadati/thumb?  → azione diretta su YouTube Studio (aggiornabili post-pubblicazione)
```

## Passi
1. Attendi la finestra minima di dati (non fare audit troppo presto).
2. `performance-auditor`: raccogli views/ora, CTR, retention, watch time; classifica la curva.
3. Diagnosi (MKD §2.2) + **una** azione correttiva specifica.
4. Studia anche **cosa ha funzionato** → da replicare nei prossimi video (coerenza cash cow).
5. Instrada il feedback a WF1/WF2 o applica la correzione diretta.

## Definition of Done
- [ ] Metriche reali raccolte (niente numeri inventati)
- [ ] Curva classificata + diagnosi
- [ ] 1 azione correttiva specifica
- [ ] Sezione "cosa replicare" (successi)
- [ ] Feedback instradato (loop effettivamente chiuso) + DEC in memoria
