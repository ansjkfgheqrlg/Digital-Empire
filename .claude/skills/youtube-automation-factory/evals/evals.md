# Evals — youtube-automation-factory

> Criteri di accettazione della fabbrica. Coerenti con MBA (verifica come first-class) e con le
> Definition of Done dei workflow.

## E1 — Invarianti rispettati
- [ ] Ogni analisi (F1/F2/F6) dichiara l'uso dell'account neutro.
- [ ] Nessun video fuori nicchia supera `niche-gate`.
- [ ] Nessuna pubblicazione senza `seo-gate` PASS.
- [ ] Ogni decisione A/B cita metriche reali (no numeri inventati).
- [ ] Ogni fase chiusa ha un checkpoint in `memory/`.

## E2 — Gate bloccanti funzionano
- [ ] `niche-gate` FAIL → il flusso torna all'operatore, non prosegue.
- [ ] `seo-gate` ricalcola il punteggio (non eredita) e blocca sotto 70 o sotto il target.
- [ ] Ogni FAIL ha un motivo azionabile registrato in `memory/decisions`.

## E3 — Script conforme alla teoria
- [ ] Hook nei primi 10s (tipo esplicito).
- [ ] Intro con valore proposto.
- [ ] Max 3 CTA distanziate.
- [ ] Errori del video target corretti.

## E4 — Produzione conforme
- [ ] Export ≥1080p MP4, sottotitoli ON, anteprima in checklist.
- [ ] Musica sotto la voce.

## E5 — Tool deterministici
- [ ] `seo_score.py` gira ed è coerente (buoni metadati ≥70; scadenti <40). ✅ testato.
- [ ] `cashcow_check.py` gira e distingue canale costante da virale singolo. ✅ testato.

## E6 — Feedback loop
- [ ] `performance-auditor` produce diagnosi + 1 azione + "cosa replicare".
- [ ] Il feedback è instradato a F1/F2 o applicato su Studio (loop effettivamente chiuso).

## Test negativi (anti-recidiva)
- Metadati senza sottotitoli → `seo-gate` deve dare FAIL.
- Video con argomento fuori nicchia → `niche-gate` FAIL.
- Decisione A/B senza numeri → il conductor deve rifiutare e chiedere il dato.
