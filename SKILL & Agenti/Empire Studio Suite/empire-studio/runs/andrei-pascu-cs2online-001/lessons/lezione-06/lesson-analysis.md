# Lezione 6 — Cucinando il tuo contesto

**Corso:** Claude Speedrun 2 | **Sezione:** AI – Le basi (6/9)
**URL:** https://www.andrei-copy.com/cs2online/lezione-6-cucinando-il-tuo-contesto-83c7l
**Video:** Vimeo `1172331550`, durata 12:25 (745s)
**Tipo:** **PRATICA** — prima lezione del corso con demo schermo reali confermate da visione diretta.
**Metodo:** trascrizione ufficiale .md integrale + 43 frame estratti e visionati nativamente (25 scan a 30s per mappare la timeline, 18 dense nei segmenti demo identificati). Frame-by-frame applicato solo dove il video mostra effettivamente lo schermo (non sui tratti puramente talking-head, per bilanciare fedeltà/costo).

---

## Mappa timeline (confermata con visione diretta)

| Tempo | Contenuto | Frame |
|---|---|---|
| 0:00–0:25 | Talking head, intro | — |
| 0:25–1:15 | Excalidraw: diagramma "input → Claude → out" (garbage in garbage out) | `frame-t0m45s-whiteboard-gigo.jpg` |
| 1:15–1:45 | Talking head | — |
| 1:45–2:15 | Excalidraw: icona cartella disegnata (introduce concetto "cartella di contesto") | `frame-t2m00s-whiteboard-folder-icon.jpg` |
| 2:15–3:45 | Talking head (Markdown vs PDF, MarkEdit) | — |
| 3:45–5:30 | **Demo schermo**: editor tipo MarkEdit con esempio "- ho 24 anni / - abito in Italia / - lavoro in marketing" + Finder con cartella "AI Contexting"-style, sottocartella "Business planning" con file reali (Business plan for sharing, Business planning.md, Business Roadmap.md, RAG and Knowledge...md, Piano Strategico 2026.pptx, Systems and SOPs.md, What skills strength...md, what tools does AP Sales use.md) | `frame-t4m15s...jpg`, `frame-t4m45s...jpg` |
| 5:30–6:00 | Talking head | — |
| 6:00–6:15 | **Demo schermo**: cartella "Claude Speedrun" (contesto dedicato al corso stesso) — file "Target e avatar Claude Speedrun", "What Claude Speedrun...", cartelle "Claude Speedrun Product Logo", "other assets", "Claude Speedrun Brand Guidelines" | `frame-t6m00s...jpg` |
| 6:15–7:00 | Talking head | — |
| 7:00–7:15 | **Demo schermo**: interfaccia Gemini (chat history reale) + interfaccia Claude.ai con saluto personalizzato "andrei returns!" (feature memory) | `frame-t7m15s...jpg` |
| 7:15–9:00 | Talking head | — |
| 9:00–11:00 | **Demo schermo — IL WORKFLOW CENTRALE**: chat Claude con PDF "brand guidelines" allegato, prompt scritto identico a quello raccomandato nella trascrizione ("Queste sono brand guidelines di un corso che sto lanciando. Voglio che tu crei un JSON prompt di circa 300-400 righe, dettagliato e moderno..."), modello **Opus 4.6 con Extended thinking** selezionato, output JSON reale con palette colori (#fb4904 arancione, ecc.) | `frame-t9m15s...jpg` |
| 10:00–10:30 | **Demo schermo**: VS Code aperto, file "brand file" nell'Explorer | `frame-t10m15s...jpg` |
| 10:30–11:00 | **Demo schermo**: Finder "Cartella contesto" con 2 file salvati (`claude-speedrun-brand-p...mpt.json`, `json prompt brand guidelines`) — chiusura del workflow PDF→JSON | `frame-t10m45s...jpg` |
| 11:00–12:25 | Excalidraw: diagramma "4 livelli di informazioni nei prompt" costruito progressivamente (1: richiesta → 2: livello settimanale → 3: livello trimestrale → 4: non cambia praticamente mai) | `frame-t12m00s...jpg` |

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Principio "garbage in, garbage out": input scarso a Claude = output scarso. Soluzione: creare documenti di contesto riutilizzabili da allegare a ogni prompt, invece di riscrivere tutto da zero ogni volta. | Trascrizione + frame t0m45s (diagramma) |
| KA-02 | Formato consigliato per documenti di contesto: **Markdown (.md)**, non PDF ("il peggior formato per leggere le cose"). Tool consigliato: **MarkEdit**. | Trascrizione + frame t4m15s |
| KA-03 | 4 documenti di contesto core usati dall'autore: brand guidelines (JSON), business plan, lista strumenti aziendali, skill/pregi/difetti. Struttura reale osservata su schermo: cartella "Claude" > sottocartelle per progetto/cliente (es. "Business planning", "b2b Client work", "week 1", "Skills per claude", "Claude Speedrun") — tag Finder dedicato "AI contexting" (verde). | Trascrizione + frame t4m15s, t4m45s |
| KA-04 | Workflow concreto PDF→JSON (osservato per intero su schermo): allegare il PDF di brand guidelines a una chat Claude nuova, prompt "Voglio che tu crei un JSON prompt di circa 300-400 righe, dettagliato e moderno, per indicare a un LLM come fare il design" — **usare Opus con Extended Thinking** perché è un documento riusato indefinitamente ("se lo fai male, lo paghi ogni volta che lo usi"). Salvare il JSON risultante con VS Code o Cursor. | Trascrizione + frame t9m15s, t10m15s, t10m45s |
| KA-05 | Framework "4 livelli di contesto" per frequenza di aggiornamento: Livello 1 = la richiesta stessa (cambia sempre, nessun documento); Livello 2 = obiettivi settimanali (aggiornare ogni settimana); Livello 3 = business planning/risultati trimestrali (aggiornare ogni trimestre); Livello 4 = identità/professione/business (quasi mai). Si creano documenti solo per i livelli 2-4. | Trascrizione + frame t12m00s |
| KA-06 | Feature "memory" di Claude osservata dal vivo: saluto personalizzato "andrei returns!" all'apertura di una nuova chat — riconoscimento cross-sessione dell'utente. | Frame t7m15s |
| KA-07 | Esempio reale non dichiarato esplicitamente nel testo ma osservato sullo schermo: le chat recenti di Claude dell'autore includono titoli di produzione del corso stesso ("10 livelli di utilizzo dell'AI", "Course launch timeline and task p...", "Linee guida per registrare lezioni...") — prova diretta (non auto-dichiarata) che l'autore usa lo stesso workflow per produrre il corso che sta insegnando. | Frame t7m15s |

## Connessione con Knowledge Base esistente

- KA-01/KA-02 confermano e specificano ulteriormente il concetto "Context Engineering" già visto in lezione 2 (glossario) e lezione 3 (muro 3→4) — terza occorrenza nello stesso corso, ma sempre stessa fonte/autore (non conta come conferma indipendente esterna per regola anti-overfitting DE).
- KA-04 (workflow PDF→JSON con Opus Extended Thinking per documenti riusati) è un pattern operativo concreto, osservato per intero (non solo raccontato) — vedi enrichment-report per valutazione applicabilità DE.

## Gate di qualità

| Check | Status | Note |
|---|---|---|
| NO-FINTO | PASS | 43 frame visionati nativamente, non inferiti. Ogni demo descritta corrisponde a un frame realmente osservato. |
| NO-STUB | PASS | Intera timeline di 745s mappata (coverage dichiarata: campionamento 30s + densificazione mirata su segmenti demo, non 100% a 2s per costo — dichiarato esplicitamente, non nascosto) |
| P12 traceability | PASS | Ogni atom ha riferimento a timestamp + frame file |
| Correzione errore proprio | PASS | Mismatch iniziale nel mapping risorse (.md scambiati) rilevato e corretto prima di procedere — vedi ingest.json nota_correzione |

**Prossima lezione:** Lezione 7 — "Diversi tipi di contesto"
