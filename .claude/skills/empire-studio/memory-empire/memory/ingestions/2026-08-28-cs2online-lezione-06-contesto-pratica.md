# Ingestion Log — cs2online-lezione-06

**Data:** 2026-08-28
**Lezione:** 6/40 — "Cucinando il tuo contesto"
**Tipo:** **PRATICA** (prima del run cs2online) — video scaricato (277MB, 745s), 43 frame visionati nativamente sui segmenti demo (Excalidraw, Finder, MarkEdit, VS Code, Claude.ai, Gemini).

## Pipeline eseguita

1. Sessione re-autenticata (scratch pulito, storage_state perso — rifatto login).
2. Video scaricato via yt-dlp con header Referer (vimeo privato, accessibile senza cookie grazie a referer check).
3. Scan grezzo 30s (25 frame) per mappare talking-head vs demo schermo.
4. Densificazione mirata (18 frame extra) sui segmenti demo identificati.
5. Trascrizione ufficiale .md scaricata — **errore di mapping rilevato e corretto**: il primo download aveva scambiato "Trascrizione lezione" con l'allegato ".md" di un'altra sezione, per aver fidato l'ordine sequenziale dei link invece del contesto DOM reale.
6. Creato `runs/.../lezione-06/` (ingest.json, lesson-analysis.md, frames/, resources/) + `memory-empire/knowledge/cs2online-lezione-06/`.
7. Enrichment: gap reale trovato (metodologia "documenti di contesto persistenti" non coperta da nessuno skill DE) — proposta registrata, non applicata (fonte singola).

## Esito

7 knowledge atoms, workflow PDF→JSON documentato con frame reali. Gate PASS.

## Lezione operativa per il run

Per lezioni con più allegati Drive: NON fidarsi dell'ordine di apparizione dei link per il mapping file→nome — verificare sempre il contesto/heading più vicino nel DOM (script dedicato scritto: estrae contesto testuale precedente per ogni link).

## Prossimo passo

Lezione 7 — "Diversi tipi di contesto".
