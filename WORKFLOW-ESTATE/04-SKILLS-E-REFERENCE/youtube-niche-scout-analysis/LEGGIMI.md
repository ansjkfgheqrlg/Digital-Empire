# Integrazione con `youtube-automation-factory`

Questo pacchetto di dati fornisce la conoscenza verticale e reale sulla nicchia "AI, Claude e Automazioni in Italiano", alimentando la skill `.claude/skills/youtube-automation-factory` senza doverne modificare la logica interna o gli agenti.

---

## 🛠️ Come Funziona l'Integrazione (Data Ingestion)

Gli agenti operativi e di controllo definiti nella `youtube-automation-factory` possono utilizzare questi file come **base di conoscenza pre-validata** per saltare la fase di scouting a freddo e accelerare la produzione di script ed elementi visivi.

Ecco come i singoli agenti utilizzano questo pacchetto:

### 1. `niche-scout` & `video-hunter` (Fase 1 e Fase 2)
*   **Problema originario:** L'agente deve cercare competitor su YouTube da zero da un account neutro, il che richiede tempo o chiamate API esterne.
*   **Integrazione:** L'agente legge [01_MAPPA_CANALI.md](01_MAPPA_CANALI.md) come database di riferimento. Quando riceve il comando `/yt-factory scouting`, carica la mappa dei 20 canali italiani per estrarre direttamente i competitor da monitorare e da cui trarre ispirazione.

### 2. `script-writer` (Fase 3)
*   **Problema originario:** L'agente scrive script generici focalizzati sulla monetizzazione AdSense (ritenzione pura) senza una strategia di vendita strutturata.
*   **Integrazione:** L'agente legge [02_PATTERN_VINCENTI.md](02_PATTERN_VINCENTI.md) (principi dell'AP Video System, 12-15 minuti) e [03_20_IDEE_VIDEO.md](03_20_IDEE_VIDEO.md). Quando scrive lo script, seleziona una delle 20 idee o ne modella una nuova seguendo gli stessi angoli di vendita e applicando la transizione di chiusura verso il Manuale di Claude Code a €67.

### 3. `thumbnail-designer` & `metadata-optimizer` (Fase 5)
*   **Problema originario:** I metadati e le indicazioni per le copertine vengono generati in modo generico e non allineati alla nicchia specifica B2B/Dev.
*   **Integrazione:**
    *   `thumbnail-designer` utilizza le indicazioni grafiche (sfondo scuro VS Code, logo Claude, accenti arancioni `#fb4604`, testo max 4 parole) descritte in [02_PATTERN_VINCENTI.md](02_PATTERN_VINCENTI.md) per scrivere prompt precisi di generazione immagini o bozze di layout.
    *   `metadata-optimizer` utilizza il template strutturato e la lista di tag forniti in [04_TEMPLATE_DESCRIZIONE_SEO.md](04_TEMPLATE_DESCRIZIONE_SEO.md) per confezionare i metadati finali del video prima del `seo-gate`.

---

## 📂 Posizionamento consigliato nel Monorepo

Per garantire che la skill `youtube-automation-factory` trovi sempre questi dati, questo pacchetto può essere posizionato in due modi:

1.  **Come Reference Esterna (Default attivo):**
    Resta all'interno di `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/`. Gli agenti vi fanno riferimento leggendo la mappa delle skill (`company/skills-map.yaml`).
2.  **Come Memoria di Run o Reference Interna della Skill:**
    Copia i file `.md` all'interno della directory della skill:
    *   `youtube-automation-factory/references/` (per i pattern, i tag e le idee video).
    *   `youtube-automation-factory/memory/workflow-state/youtube/` (per il database dei competitor `01_MAPPA_CANALI.md`).
