# WF3 — Production (Fasi 3+4): Script → Video Fliki

> Obiettivo: dal video scelto allo **script** e alla **spec di produzione Fliki**, con gate di nicchia.

## DAG
```
[input: video scelto (A/B) + errori da correggere]
   │
   ▼
script-writer ── script.md  (Hook → Intro[valore] → Corpo → CTA×3, keyword nel parlato, errori corretti)
   │
   ▼
video-producer ── produzione-spec.md  (progetto+formato · voce · musica<voce · scene+durate · transizioni · sottotitoli ON · export 1080p MP4 · anteprima obbligatoria)
   │
   ▼
⟨ niche-gate ⟩  il video resta in nicchia? PASS? ──no──► torna a script/producer
   │ sì
   ▼
[output: video prodotto pronto] → WF4
```

## Passi
1. `script-writer`: struttura narrativa (MKD §4) correggendo gli errori isolati in WF2.
   - Hook (tipo scelto: d'impatto/lento/domanda) nei primi 10s.
   - Intro con **valore proposto**.
   - CTA iniziale + metà + finale (no spam).
2. `video-producer`: mappa script→scene, voce, musica bilanciata, transizioni, sottotitoli, export.
3. `niche-gate`: verifica che il video prodotto sia coerente con la nicchia/format del canale.

## Definition of Done
- [ ] Script con hook nei primi 10s + valore proposto + 3 CTA
- [ ] Errori del target corretti nello script
- [ ] Spec Fliki completa (export ≥1080p MP4, sottotitoli ON, anteprima in checklist)
- [ ] niche-gate PASS
