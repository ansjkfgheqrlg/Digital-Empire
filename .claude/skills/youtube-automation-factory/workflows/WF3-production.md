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
video-producer ── produzione-spec.md & .json (progetto+formato · voce · musica<voce · scene+durate · transizioni · sottotitoli ON · export 1080p MP4)
   │
   ▼
[Video MP4 Esportato da Fliki]
   │
   ▼
⟨ qa-audio-video ⟩  qualità audio/video e pronunce OK? PASS? ──no──► torna a video-producer
   │ sì
   ▼
⟨ niche-gate ⟩  il video resta in nicchia? PASS? ──no──► torna a script/producer
   │ sì
   ▼
[output: video prodotto pronto] → WF4
```

## Passi
1. `script-writer`: controlla `memory/learned_rules.json` per evitare hook/voci sconsigliate, poi scrive lo script correggendo gli errori isolati in WF2. Salva `script.md`.
2. `video-producer`: mappa script→scene, definisce voce e musica (seguendo `references/fliki-avanzato.md` e `learned_rules.json`), salva `produzione-spec.md` e `produzione-spec.json`. Esegue `validate_schemas.py produzione-spec produzione-spec.json`.
3. L'utente esporta il video MP4 da Fliki.
4. `qa-audio-video`: esegue il controllo di qualità audio/video e pronuncia fonetica. Genera `gate-qa.md` (PASS/FAIL).
5. `niche-gate`: verifica che il video sia coerente con la nicchia del canale. Genera `gate-niche.md` (PASS/FAIL).

## Definition of Done
- [ ] Script con hook coerente e valorizzato + 3 CTA
- [ ] Spec Fliki completa in formato MD e JSON
- [ ] Video MP4 esportato ad almeno 1080p
- [ ] qa-audio-video PASS
- [ ] niche-gate PASS
