# Workflow Master — Legami d'Amore (canale attivo esclusivo)

> Obiettivo: consolidare in un unico documento leggibile, step-by-step, il flusso reale che la
> fabbrica esegue OGGI per **Legami d'Amore** (`@Legamidiamore`, `CANALI["legamidiamore"]` in
> `apex7_orchestrator.py`) — dal login alla pubblicazione privata e al feedback loop. Non
> ridefinisce le fasi: **rimanda** a [WF1](WF1-niche-discovery.md)…[WF5](WF5-performance-audit.md)
> per il dettaglio di ciascuna e aggiunge solo ciò che è specifico di questo canale (login,
> voce, sottotitoli, skip-thumbnail temporaneo, upload privato). Dettato da Max il 2026-08-13.
>
> Vedi anche: [CALENDARIO-LEGAMIDIAMORE.md](CALENDARIO-LEGAMIDIAMORE.md) (piano contenuti),
> [implementation_plan.md](implementation_plan.md) (stato reale vs simulato dell'orchestratore),
> [SKILL.md](../../.claude/skills/youtube-automation-factory/SKILL.md) (kernel skill),
> [agents/conductor.md](../../.claude/skills/youtube-automation-factory/agents/conductor.md)
> (system prompt del conductor).

---

## ⚠️ Regole permanenti (non negoziabili, valide per OGNI run su questo canale)

1. **Canale attivo esclusivo: Legami d'Amore.** `CANALI["dosementale"]` (Dose Mentale) è **in
   pausa** per ordine esplicito di Max (2026-08-13): la sua configurazione non va toccata, resta
   com'è, ma nessun agente lo sceglie come target né lo modifica senza un nuovo ordine esplicito.
   Nota tecnica: `CANALE_TARGET` resta alias di `CANALI["dosementale"]` per compatibilità con
   codice/test esistenti — ogni run reale su Legami d'Amore **deve** passare `--canale
   legamidiamore` esplicito, altrimenti l'orchestratore lavora sul canale sbagliato in silenzio.
2. **Voce Fliki sempre femminile e realistica.** `CANALI["legamidiamore"]["voice_gender"] =
   "female"`, letto da `fliki_client.py --canale legamidiamore` (`find_italian_voice(...,
   prefer_gender="female")`). Mai voce maschile, mai voce sintetica/robotica per questo canale.
3. **Sottotitoli presenti ma dimensione ridotta.** I sottotitoli restano ON (indicizzabili,
   coerente con l'invariante SEO), ma il font non deve essere grande/invasivo: leggibilità senza
   coprire la scena. Implementato dal 2026-08-15: `CANALI["legamidiamore"]["subtitle_preset"] =
   "builtin-legacy-minimal"` (dosementale resta su `"builtin-legacy-bold"`, config lock di Gael
   invariata). Nessun preset Fliki espone metadati di dimensione via API: "minimal" è la scelta
   più plausibile fra i 30 preset reali, **da confermare visivamente** sul prossimo video generato
   — cambiabile in un solo punto (`CANALI` in `apex7_orchestrator.py`) se non è quello giusto.
   L'effetto karaoke (`highlightSubtitles: True`) resta invariato per tutti i canali (proposta di
   rimuoverlo già respinta da Gael in passato — non riproposta qui).
4. **Modalità video realistica, non stilizzata/cartoon.** Coerente con il tono adulto della
   nicchia (psicologia femminile/maschile, dinamiche relazionali).
5. **⛔ MAI caricare un video senza copertina — regola permanente, capovolta da Max il
   2026-08-18 (annulla la #5 precedente "skippabile temporaneamente").** Nessuna eccezione,
   nessun flag di skip: un video senza copertina reale non si pubblica, punto.
   **Meccanismo (non più AI-prompt con reference):** ogni video ha una cartella dedicata in
   `VIDEO-PRONTI/video-NN/` con dentro `video.mp4`, `copy.md` (titolo/descrizione/tag) e la
   **copertina che Max mette lì a mano** (un solo file immagine, nome libero). L'uploader legge
   la copertina da quella cartella — non da `arena_thumbnail.py`, non da un prompt AI generato
   da Claude. Se la cartella del video non contiene nessuna immagine, l'upload si **rifiuta**
   di procedere invece di caricare senza copertina.
6. **Pubblicazione sempre PRIVATA.** Mai pubblico finché Max non lo chiede esplicitamente.
   `youtube_uploader_playwright.py` già imposta `PRIVATE` come visibilità di default
   (`tp-yt-paper-radio-button[name='PRIVATE']`). L'upload reale è comunque un'azione a parte,
   opt-in con un flag `--upload` previsto sulla Fase 5 dell'orchestratore — non automatico. *Nota
   implementativa: dal 2026-08-15 `--upload` è cablato in `run_phase_5` (richiede anche
   `--video-file <path.mp4>`, perché la produzione reale via `fliki_client.py` resta un comando
   manuale a monte): se attivo, invoca `youtube_uploader_playwright.py` col profilo del canale,
   estrae l'ID/URL reale del video caricato e lo registra in `memory/published_videos.json`. Il
   primo run reale con `--upload` va lanciato manualmente da un operatore umano, non da un agente
   in autonomia.*
7. **Nessun gate esistente viene rimosso.** `niche-gate`, `seo-gate`, `qa-audio-video` e i
   regolatori restano bloccanti come oggi. Questo documento aggiunge regole, non ne toglie.
8. **Nessun run è "fatto" finché non è salvato in memoria** — `memory/` del progetto (checkpoint,
   decision log) **e** checkpoint Digital Empire in `company/Memory/checkpoints/`.

---

## 🔄 I 10 passi del flusso reale (Legami d'Amore)

```
 1. Login/sessione Playwright (persistente, ~1 mese)
        │
 2. Analisi canale + nicchia + competitor
        │
 3. Selezione video da replicare (velocity vs tempo, non valore assoluto)
        │
 4. Estrazione script del video scelto
        │
 5. Riscrittura originale (compliance shield)
        │
 6. Produzione Fliki — voce femminile, sottotitoli ridotti, stile realistico
        │
 7. Copertina/miniatura — SKIP temporaneo disponibile (bassa priorità)
        │            (in parallelo dal punto 6:)
 8. Copy/metadati — tassonomia tag a 4 livelli, ≤500 char totali
        │
 9. Pubblicazione — sempre PRIVATA, upload reale opt-in
        │
10. Audit performance → feedback loop verso 1/2
```

### 1. Login / sessione
- Script: `legamidiamore_login.py`. Profilo Chrome persistente:
  `chrome-profile-legamidiamore/` (`CANALI["legamidiamore"]["chrome_profile_dir"]`).
- Sessione valida ~1 mese: rifare login solo quando scade, non ad ogni run.
- Precondizione dei WF analitici (account "neutro" per lo scouting resta un profilo diverso, vedi
  invariante #1 di [SKILL.md](../../.claude/skills/youtube-automation-factory/SKILL.md) — non va
  confuso con questo profilo autenticato, che serve per Studio/upload).

### 2. Analisi canale + nicchia + competitor
- Copre: [WF1-niche-discovery.md](WF1-niche-discovery.md) (nicchia + cash cow, gate `niche-gate`).
- Script/agenti: `channel_discovery.py`, `copy_study_legamidiamore.py`, agente `niche-scout`.
- Su questo canale la nicchia è già certificata (psicologia femminile/maschile, attrazione,
  segnali, dinamiche relazionali — vedi `CANALI["legamidiamore"]["temi"]`): questo passo mantiene
  il quadro aggiornato (competitor nuovi, schemi che cambiano), non lo rifà da zero ogni volta.

### 3. Selezione del video da replicare
- Copre: [WF2-video-selection.md](WF2-video-selection.md) (`run_phase_2`, agente `video-hunter`).
- Regola già implementata: scarta video **<24h** (velocity troppo rumorosa), richiede **≥3x la
  mediana** del canale (`VIDEO_MULTIPLO_MEDIANA`), pavimento assoluto **2 viste/ora**
  (`VIDEO_VPH_MINIMO`), tie-break sul **più recente** a parità di velocity. Non è un valore
  assoluto di viste che decide, è la crescita relativa al tempo trascorso.

### 4. Estrazione script del video scelto
- Parte di [WF2](WF2-video-selection.md) → [WF3-production.md](WF3-production.md) (handoff).
- Il testo/hook/struttura del video sorgente viene estratto come riferimento analitico, **mai**
  copiato verbatim (vedi regola non negoziabile in
  [CALENDARIO-LEGAMIDIAMORE.md](CALENDARIO-LEGAMIDIAMORE.md)).

### 5. Riscrittura originale
- Copre: [WF3-production.md](WF3-production.md), agente `script-writer`.
- Skill collegata: `youtube-compliance-shield` — garantisce che l'essenza resti ma la forma cambi
  abbastanza da non essere un re-upload/duplicato.
- Passa da `memory/learned_rules.json` prima di scrivere (hook/voci sconsigliate da run passate).

### 6. Produzione Fliki
- Copre: [WF3-production.md](WF3-production.md) (seconda metà), script `fliki_client.py`.
- **Vincoli canale (regola permanente #2-#4):** `--canale legamidiamore` → voce sempre femminile
  e realistica; sottotitoli ON ma piccoli; modalità video realistica, non cartoon/stilizzata.
- Gate a valle: `qa-audio-video` (audio/video/pronuncia) e `niche-gate` (resta in nicchia?).

### 7. Copertina / miniatura
- Script: `arena_thumbnail.py`, agente `thumbnail-designer` — copre parte di
  [WF4-publish-seo.md](WF4-publish-seo.md).
- **Regola permanente #5:** step reale e funzionante, ma **skippabile temporaneamente** con
  `--skip-thumbnail` sulla Fase 5 dell'orchestratore, su richiesta esplicita di Max. Resta nel
  flusso e riattivabile in ogni momento; priorità più bassa rispetto a produzione/pubblicazione
  finché non richiesto di nuovo.

### 8. Copy / metadati (in parallelo alla produzione)
- Copre: [WF4-publish-seo.md](WF4-publish-seo.md), agente `metadata-optimizer`.
- Tassonomia a 4 livelli: (a) tag identici in titolo+descrizione+tag, (b) tag di contesto
  generali/specifici, (c) tag di volume, (d) meta-tag a frase intera.
- Limiti YouTube da rispettare sempre: **≤500 caratteri totali** sui tag, **≤30-40 caratteri per
  singolo tag**. Verificato da `seo_score.py` + `seo-gate` (bloccante, invariante #4 della skill).

### 9. Pubblicazione reale
- Script: `youtube_uploader_playwright.py`, profilo `chrome-profile-legamidiamore`. Copre la
  seconda metà di [WF4-publish-seo.md](WF4-publish-seo.md).
- **Regola permanente #6:** sempre modalità **PRIVATA** per ora, mai pubblico finché Max non lo
  chiede esplicitamente. Attivabile con flag opt-in `--upload` sulla Fase 5 dell'orchestratore
  (l'upload reale non parte mai di default/in automatico).

### 10. Audit performance post-pubblicazione
- Copre: [WF5-performance-audit.md](WF5-performance-audit.md), agente `performance-auditor` +
  `self-improver`.
- Feedback loop verso le Fasi 1/2 (pivot nicchia, scelta video migliore) o correzione diretta di
  metadati/thumbnail post-pubblicazione. Aggiorna `memory/learned_rules.json`.

---

## 🤖 Agenti coinvolti per fase (riepilogo)

| Step | Fase (WF) | Agenti/script principali |
|---|---|---|
| 1 | — (precondizione) | `legamidiamore_login.py` |
| 2 | F1 — [WF1](WF1-niche-discovery.md) | `niche-scout`, `channel_discovery.py`, `copy_study_legamidiamore.py` |
| 3 | F2 — [WF2](WF2-video-selection.md) | `video-hunter`, `seo-analyst` |
| 4-5 | F3 — [WF3](WF3-production.md) | `script-writer` (+ skill `youtube-compliance-shield`) |
| 6 | F4 — [WF3](WF3-production.md) | `video-producer`, `qa-audio-video` (gate), `niche-gate` (gate), `fliki_client.py` |
| 7-8 | F5 — [WF4](WF4-publish-seo.md) | `thumbnail-designer`, `metadata-optimizer`, `seo-gate` (gate) |
| 9 | F5 — [WF4](WF4-publish-seo.md) | `youtube_uploader_playwright.py` |
| 10 | F6 — [WF5](WF5-performance-audit.md) | `performance-auditor`, `self-improver` |

Conductor: unico che parla con l'utente e orchestra tutti gli step sopra — system prompt completo
in [agents/conductor.md](../../.claude/skills/youtube-automation-factory/agents/conductor.md).

---

## Definition of Done (dell'intero ciclo Legami d'Amore)

- [ ] Sessione Playwright valida (login rifatto se scaduto)
- [ ] Nicchia/competitor aggiornati, `niche-gate` PASS
- [ ] Video scelto con regola velocity/tempo (non valore assoluto), non <24h
- [ ] Script riscritto originale, `youtube-compliance-shield` applicata
- [ ] Video Fliki: voce femminile realistica, sottotitoli piccoli, stile realistico
- [ ] Miniatura prodotta OPPURE consapevolmente skippata (`--skip-thumbnail`)
- [ ] Metadati a norma (tassonomia 4 livelli, limiti char rispettati), `seo-gate` PASS
- [ ] Pubblicato in modalità PRIVATA (upload reale solo se `--upload` esplicito)
- [ ] Audit eseguito dopo la finestra minima di dati, feedback instradato
- [ ] Checkpoint salvato in `memory/` **e** in `company/Memory/checkpoints/`
