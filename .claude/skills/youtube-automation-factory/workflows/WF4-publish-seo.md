# WF4 — Publish + SEO (Fase 5)

> Obiettivo: dai metadati **certificanti** alla pubblicazione, con gate SEO bloccante.

## DAG
```
[input: video prodotto + errori SEO target + tag alto-valore]
   │
   ▼
metadata-optimizer ── metadati.md
     titolo (keyword + veritiero)
     descrizione (prime 2 righe hook+valore · keyword · link+CTA)
     tag (rilevanti + tag alto-valore riusati)
     miniatura (brief; migliorata se target aveva thumb debole)
     sottotitoli (ON, indicizzati)
   │
   ▼
seo_score.py (ricalcolo) ── deve battere il target ed essere ≥ soglia
   │
   ▼
⟨ seo-gate ⟩  PASS? ──no──► torna a metadata-optimizer (motivi)
   │ sì
   ▼
PUBBLICA / PROGRAMMA su YouTube Studio (programma quando il pubblico è attivo)
   │
   ▼
[output: video pubblicato] → WF5 (dopo la finestra di raccolta dati)
```

## Passi
1. `metadata-optimizer`: 5 elementi certificanti (MKD §2.4) + ripunteggio con `seo_score.py`.
2. `seo-gate`: **ricalcola** il punteggio (non si fida), checklist bloccante, PASS/FAIL.
3. Upload su YouTube Studio + programmazione oraria.

## Definition of Done
- [ ] 5 elementi SEO presenti (titolo/descr/tag/thumb/sottotitoli)
- [ ] Punteggio SEO ≥ soglia (70) **e** ≥ punteggio del video target
- [ ] seo-gate PASS
- [ ] Video pubblicato o programmato in orario ad alto traffico
