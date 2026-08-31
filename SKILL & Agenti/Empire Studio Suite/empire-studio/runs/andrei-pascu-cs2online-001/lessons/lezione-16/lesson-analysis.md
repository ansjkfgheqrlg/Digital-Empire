# Lezione 16 — Copy per primary text (ads) con Claude

**Corso:** Claude Speedrun 2 | **Sezione:** AI – per copywriting (4/4, ultima)
**URL:** https://www.andrei-copy.com/cs2online/lezione-16-copy-per-primary-text-ads-con-claude-wspxy
**Video:** Vimeo `1174238441`, durata 13:20 (800s)
**Tipo:** **PRATICA** — confermato con 40 frame visionati (27 scan 30s + 13 dense mirati).
**Metodo:** panoramica + "Cosa hai imparato" ufficiali (nessuna risorsa Drive) + frame video.

---

## Mappa timeline (confermata)

| Tempo | Contenuto | Frame |
|---|---|---|
| 0:00–3:00 | Talking head — intro, quando ha senso il copy "fast" (budget cliente basso) | — |
| 3:00 | **Demo**: DaVinci Resolve, progetto con 4 clip video ad importati in timeline | `frame-t3m00s...jpg` |
| 3:15 | **Demo**: export settings DaVinci — H.264, timeline unica 3:29 min (audio unificato dei 4 video) | `frame-t3m15s...jpg` |
| 7:15 | **Demo — PROMPT ESATTO**: Claude.ai, file allegato "_contestoi_per_cliente_per_fare_primary_text_pu...txt" (25 righe, trascrizione ElevenLabs), prompt: *"Ciao Claude, come stai, amore? Senti, sto facendo le ad per questo mio cliente e vorrei che tu scrivessi per me le primary text headline e description per le pubblicità su Meta. Voglio che tu segua le linee guida Meta e voglio che tu le scriva 5 versioni per ogni una."* Modello: **Opus 4.6 Extended**. | `frame-t7m15s...jpg` |
| 9:00 | **Demo**: sales page reale usata come esempio ("Funnel Operator", corso terzi) | `frame-t9m00s...jpg` |
| 9:15 | **Demo**: sales page propria dell'autore (Corso Copywriting Online, andrei-copy.com) — usata per dimostrare il metodo di estrazione testo | `frame-t9m15s...jpg` |
| 11:00 | **Demo**: estensione Chrome GoFullPage in azione ("Screen capture in progress... verrà divisa in 2 immagini") | `frame-t11m00s...jpg` |
| 12:00 | **Demo**: menu MarkEdit aperto, output GoFullPage visibile a fianco | `frame-t12m00s...jpg` |
| 12:30–13:20 | Talking head, chiusura | — |

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Criterio esplicito per scegliere copy "fast" vs "perfetto": valutare il budget ads del cliente — se spende 10-20€/giorno, non ha senso passare un'ora sui primary text. | "Cosa hai imparato" |
| KA-02 | Workflow completo per creative multiple: scaricare i video ad (anche da TikTok via SnapTik.app senza watermark) → unirli in un'unica timeline (DaVinci Resolve o altro editor) → esportare SOLO l'audio in MP3 → trascrivere con ElevenLabs (Speech to Text, togliendo timestamp/speaker) → un unico file di contesto invece di trascrivere ogni video separatamente. Alternativa senza editor: converter online "video to MP3". | Trascrizione ufficiale + frame t3m00s, t3m15s |
| KA-02b | Struttura prompt raccomandata quando il contesto è limitato: **contesto → problema → richiesta**. Specificare sempre il numero di versioni desiderate (Meta permette più varianti nella stessa ad). | Panoramica ufficiale |
| KA-03 | Prompt esatto osservato a schermo (verbatim) — nota di stile: tono colloquiale/informale ("come stai, amore?") anche in un contesto di lavoro reale con cliente pagante. | frame-t7m15s |
| KA-04 | Regola esplicita e ripetuta: NON delegare la strategia a Claude — inserire nel prompt USP, CTA desiderata ed elementi strategici specifici. Claude va usato "solo per la forma", non per decidere cosa dire. | "Cosa hai imparato" |
| KA-05 | 3 modi per passare una sales page a Claude (in ordine di preferenza implicito): (1) link diretto, (2) copia-incolla manuale del testo (selezione completa Ctrl+C/V), (3) tool online (totheweb.com) per convertire HTML in testo puro. **GoFullPage** (screenshot PDF pagina intera) è un'alternativa ma con limite dichiarato: "il PDF a volte non viene letto bene da Claude, meglio testo o markdown". | Panoramica + "Cosa hai imparato" + frame t11m00s |
| KA-06 | Dare un nome descrittivo al file allegato (es. "Copywriting Mentorship Sales Page Copy") per aiutare Claude a capire il contesto senza doverlo spiegare a parole. | "Cosa hai imparato" |
| KA-07 | Possibilità di arricchire ulteriormente il contesto oltre alla sales page: recensioni, sito personale, brand guide, file da GitHub. | "Cosa hai imparato" |
| KA-08 | Se l'output non piace nel formato, chiedere esplicitamente la riformattazione (es. "mettimelo come markdown") invece di rifare il prompt da zero. | "Cosa hai imparato" |
| KA-09 | Nota tecnica: Arc (browser) supporta le estensioni Chrome perché gira su Chromium — permette di usare GoFullPage anche fuori da Chrome stesso. | "Cosa hai imparato" |

## Connessione con Knowledge Base esistente

- KA-04 (mai delegare strategia, solo forma) è la stessa regola già vista in lezione 1 (KA-08, run cs2online) e coerente con `cro-copy-architect` — quarta occorrenza dello stesso principio nel corso, ulteriore consolidamento ma stessa fonte/autore.
- KA-02 (workflow SnapTik→DaVinci→ElevenLabs→Claude) è un pattern operativo tecnico specifico, di dominio "produzione ads/video", non copywriting puro — vedi enrichment-report per valutazione.

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — 40 frame visionati, prompt trascritto verbatim da screenshot |
| NO-STUB | PASS — video 13:20 intero mappato |
| P12 traceability | PASS |

**Prossima:** Bonus 1 — "Automatizzare processi"
