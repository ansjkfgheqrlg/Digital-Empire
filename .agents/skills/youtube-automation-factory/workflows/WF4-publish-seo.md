# WF4 — Publish + SEO (Fase 5)

> Obiettivo: dai metadati **certificanti** alla pubblicazione, con gate SEO bloccante.

## DAG
```
## DAG
```
[input: video prodotto + errori SEO target + tag alto-valore]
   │
   ▼
thumbnail-designer ── brief-miniatura.md & .json (visual contrast · focus · prompt AI)
   │
   ▼
metadata-optimizer ── metadati.md & .json
     titolo (keyword + veritiero)
     descrizione (prime 2 righe hook+valore · keyword · link+CTA)
     tag (rilevanti + tag alto-valore riusati)
     miniatura (caricata basandosi su brief-miniatura)
     sottotitoli (ON, indicizzati)
   │
   ▼
seo_score.py --json metadati.json ── deve battere il target ed essere ≥ soglia
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
1. `thumbnail-designer`: controlla `memory/learned_rules.json` per evitare stili fallimentari, analizza la copertina del target, progetta il nuovo layout grafico e scrive `brief-miniatura.md` e `brief-miniatura.json`. Esegue `validate_schemas.py brief-miniatura brief-miniatura.json`.
2. `metadata-optimizer`: prepara i 5 elements certificanti (titolo, descrizione, tag riusati, sottotitoli e miniatura) leggendo `brief-miniatura.json` e `learned_rules.json`. Salva `metadati.md` e `metadati.json`. Esegue `validate_schemas.py metadati metadati.json`.
3. `seo-gate`: esegue `seo_score.py --json metadati.json`. Verifica la checklist bloccante e scrive `gate-seo.md` (PASS/FAIL).
4. Upload su YouTube Studio + programmazione oraria (o via `youtube_uploader_playwright.py` tramite browser automation).

## Definition of Done
- [ ] Brief copertina con prompt AI generato in formato MD e JSON
- [ ] Metadati certificanti pronti in formato MD e JSON
- [ ] Punteggio SEO ≥ soglia (70) **e** ≥ punteggio del video target ricalcolato da JSON
- [ ] seo-gate PASS
- [ ] Video pubblicato o programmato in orario ad alto traffico
