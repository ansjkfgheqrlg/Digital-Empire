# YouTube Automation Engine

Questo ecosistema automatizzato è stato architettato utilizzando i principi di `master-build-architecture` e `content-forge2.0`. Si occupa di orchestrare l'analisi SEO dei video di YouTube (tramite VidIQ), la re-ingegnerizzazione degli script e la produzione massiva tramite Fliki, come codificato in `KB_06`.

## Architettura dei File (Master Build Architecture)
- `agents/`: Contiene gli agenti (es. analista-seo, ingegnere-script, operatore-fliki).
- `memory/`: Ecosistema di memoria in due livelli (checkpoints, decisoni, piani).
- `references/`: Collegamenti ai knowledge-base (come KB_06).
- `scripts/`: Strumenti Python per le automazioni di pipeline.
- `workflows/`: I flussi operativi codificati secondo gli standard di *Content Forge*.

## Workflows (Content Forge 2.0 Pipeline)
1. **vidiq-seo-analysis**: Ricerca dei "Cash Cow Channel", analisi VPH, CTR e reverse-engineering degli errori SEO.
2. **script-engineering**: Applicazione della Teoria Narrativa (Gancio d'impatto, Ritenzione, CTA) e riscrittura del contenuto migliorato.
3. **fliki-production**: Text-to-Video automatizzato, bilanciamento audio, generazione e validazione pre-export.
