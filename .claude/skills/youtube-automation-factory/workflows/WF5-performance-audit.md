# WF5 — Performance Audit (Fase 6) + feedback loop

> Obiettivo: misurare il video pubblicato, **diagnosticare l'errore** e **rimettere in moto il loop**.

## DAG
```
[input: video pubblicato (dopo finestra di raccolta dati)]
   │
   ▼
performance-auditor ── legge metriche reali (Video IQ / Studio) ──► scrive audit-report.md & memory/performance_logs.json
   │
   ▼
CLASSIFICA la curva:
   picco-poi-calo   → errore SEO (keyword/descr/tag)     → azione: rivedi metadati
   crescita lenta    → errore thumb/titolo/descrizione     → azione: cambia thumb+titolo (post-pubbl.)
   piatta/in salita  → confronta con target + studia i successi (cosa replicare)
   │
   ▼
self-improver ──► esegue scripts/self_improve.py ──► aggiorna memory/learned_rules.json
   │
   ▼
FEEDBACK AL LOOP:
   pivot nicchia?   → WF1 (niche-scout)
   scelta migliore? → WF2 (video-hunter/seo-analyst)
   metadati/thumb?  → azione diretta su YouTube Studio (aggiornabili post-pubblicazione)
```

## Passi
1. Attendi la finestra minima di dati (non fare audit troppo presto).
2. `performance-auditor`: raccogli views/ora, CTR, retention, watch time; classifica la curva. Scrive `audit-report.md` ed effettua il log strutturato in `memory/performance_logs.json`. Esegue `validate_schemas.py performance-logs memory/performance_logs.json`.
3. `self-improver`: esegue `self_improve.py` per ricalcolare e aggiornare `memory/learned_rules.json` sulla base del log aggiornato. Esegue `validate_schemas.py learned-rules memory/learned_rules.json`.
4. Studia anche **cosa ha funzionato** (da replicare).
5. Instrada il feedback a WF1/WF2 o applica la correzione diretta.

## Definition of Done
- [ ] Metriche reali raccolte ed esportate in `performance_logs.json`
- [ ] Curva classificata + diagnosi in `audit-report.md`
- [ ] Script `self_improve.py` eseguito con successo
- [ ] `memory/learned_rules.json` aggiornato con le nuove blacklist/preferenze
- [ ] Feedback instradato + DEC salvata in memoria
