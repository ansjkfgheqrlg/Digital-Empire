# Reference — Produzione con Fliki (testo → video)

> Conoscenza on-demand per `video-producer`. Fonte: MKD §3. Sito: fliki.ai.

> ## ⚠️ LEGGI QUESTO PRIMA DEL RESTO (A4-L04-03 · 2026-09-05)
>
> **Tutto ciò che segue descrive Fliki usato A MANO nell'interfaccia. La nostra fabbrica non usa
> l'interfaccia.** Genera **via API** (`02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py`), con
> `shouldExport: True`: nessun browser aperto, nessuna anteprima, nessun clic.
>
> **Cosa imposta davvero la nostra catena (via API):**
> `aspectRatio` (oggi `16:9` fisso) · `resolution: 1080p` · `voiceId` · `visuals` (ai/stock) ·
> `sceneBreakdown: lineBreak` · `subtitlePresetId` + `highlightSubtitles` · `aiVideoModel` +
> `aiVideoClipPercentage` + `imageAnimationPreset` · `duration` (1-15 minuti, campo inerte sulla
> durata finale) · `fileName`.
>
> **Cosa esiste in Fliki ma la nostra catena NON tocca** (verificato sul payload il 2026-09-05):
> musica di sottofondo e suo volume · transizioni fra scene · durata della singola scena ·
> pause (`Add pause`) · velocità e intonazione (`Tune → Rate`) · mappa delle pronunce
> (`More → Pronunciation map`) · anteprima prima dell'export · caricamento di clip proprie.
>
> **Regola d'uso di questa scheda:** i passaggi qui sotto valgono per capire *lo strumento* e per
> un eventuale intervento manuale straordinario. **Non sono istruzioni per la catena**, e non
> vanno copiati in una spec di produzione. Le pronunce si correggono nel testo dello script, con
> `references/lessico-pronuncia.md`.

## Setup (registrazione)
1. fliki.ai → "Get Started".
2. Registrati con **email valida** (arriva mail di conferma) o Google/Facebook.
3. Conferma l'email (controlla spam se non arriva).
4. Dashboard: progetti recenti · "Create New Project" · menù a sinistra.

## Creazione video (pipeline)
1. **Nuovo progetto**: nome + **formato** — 16:9 YouTube · 1:1 Instagram · 9:16 short/TikTok.
2. **Contenuti**: carica testo/documento/audio → Fliki converte in video con immagini/clip pertinenti
   (oppure scegli dall'archivio Fliki).
3. **Personalizzazione**:
   - **Musica** di sottofondo a tono, **volume sotto la voce**.
   - **Testi/titoli/sottotitoli** (rende il video accessibile e coinvolgente).
   - **Durata scene** regolata per uno scorrimento fluido.
4. **Voce narrante**: scegli voce/lingua/accento (usa l'anteprima), incolla lo script → Fliki
   sincronizza voce↔immagini. Rivedi il testo (grammatica/sintassi).
5. **Modifica avanzata**:
   - **Transizioni** tra scene, con cura (influenzano la qualità percepita).
   - **Bilancia i volumi** (musica sotto la narrazione).
   - **Anteprima obbligatoria** prima di esportare (non saltarla mai).
6. **Export**: risoluzione **≥1080p** per YouTube · formato **MP4** (più versatile) · "Export" →
   rendering (**non chiudere il browser** durante l'export).

## Upload + ottimizzazione su YouTube (aggancio a WF4)
- YouTube Studio → "Carica video" → seleziona l'MP4.
- Titolo + descrizione (prime 2 righe decisive) + tag + miniatura + sottotitoli → vedi
  `references/seo-certificazione.md`.
- **Pubblica o programma** (programma in orario di massimo traffico → più views iniziali).
- Poi: **analizza e ottimizza** (WF5) — il successo è un processo continuo.

## Checklist produzione (per video-producer)
- [ ] Formato corretto per la piattaforma
- [ ] Voce scelta con anteprima, tono coerente col canale
- [ ] Musica a tono, sotto la voce
- [ ] Scene mappate dallo script, durate fluide, transizioni curate
- [ ] Sottotitoli ON
- [ ] Anteprima fatta prima dell'export
- [ ] Export ≥1080p MP4, browser non chiuso durante il rendering
