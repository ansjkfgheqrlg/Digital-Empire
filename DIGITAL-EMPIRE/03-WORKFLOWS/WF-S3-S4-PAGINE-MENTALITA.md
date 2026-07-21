# WF-S3/S4 — PAGINE LANCIO + MENTALITA.BRUTALE (riattivazione con funnel)
> Stream: S3+S4 · Owner: Gael · Motore: **carousel-factory** (wrap ADR-003, brand mentalita-brutale già configurato)
> Regola cardine: ogni pagina riattivata = UN funnel + UNA metrica. Niente "pubblicare per pubblicare".

## PARTE A — S3 crea.illtuo_impero (22→26/07)

### A1. Audit (21/07 — chiude G-05)
Output: `07-CONTROL/AUDIT-PAGINE-20260721.md` per OGNI pagina: handle · follower · ultimo post · accessi (email/password/2FA ok?) · bio attuale · link attuale · stato (attiva/dormiente).

### A2. Attivazione (22/07)
1. Bio → promessa + link funnel S2 (`link in bio → landing Manuale`).
2. Batch unico 23/07: **7 caroselli** via carousel-factory (1 run, config esistente).
3. Pubblicazione 1/giorno: Meta Graph API → Buffer → manuale (ultima spiaggia).
4. **Rampa anti-ban**: mai più di 1 post/giorno/pagina, zero automation su follow/like/DM.

### A3. Angoli caroselli (batch 1)
1. "Come ho automatizzato X con Claude Code" (caso reale) → CTA: Parte 1 gratis.
2. "5 errori che fanno tutti con Claude Code" → CTA: link in bio.
3. "Da 0 a skill in 1 sessione" (dal Manuale cap. 4) → CTA: Manuale.
4-7. Variazioni hook su 1-3 (riuso pattern vincenti → ReasoningBank in RETRO).

## PARTE B — S4 mentalita.brutale (23→25/07) — HARD RULE
> **Condizione Max (vincolante): riparte SOLO se 100% automatica.** Se il gate E2E non passa entro 24/07 h20:00 → STANDBY dichiarato (`error --wf WF-S4`), nessuna pubblicazione manuale.

### B1. Pipeline target (tutti anelli, nessun buco)
```
batch settimanale caroselli (carousel-factory, brand mentalita-brutale)
  → gate QA automatico (regole copy esistenti: hook, no-claim, CTA)
  → scheduler pubblicazione (Meta Graph API / Buffer)
  → report engagement automatico (settimanale)
  → loop: hook/CTA vincenti → ReasoningBank (WF-*-IMPROVE)
```

### B2. Gate E2E (24/07)
Test dimostrabile: 1 carosello prodotto → QA pass/fail visibile → schedulato → report generato. Esito → `checkpoint --task WF-S4 --note "E2E ok/ko"`.

### B3. Monetizzazione breve (se e solo se ON)
link in bio → lead-magnet → S2 · shoutout a pagamento quando torna trazione · affiliate. Niente piani long-term-only.

## Metriche S3/S4
`s3_caroselli_pubblicati` (≥3) · click bio→landing (diagnostica) · `s4_pipeline_e2e` (0/1) · vendite attribuite via S2 (lagging unico che conta).

---
⛓️ P12: `WF-S3-S4#estate-2026` · trace: F-04, F-07, R-06 · gate: Gate-S4 24/07 h20
