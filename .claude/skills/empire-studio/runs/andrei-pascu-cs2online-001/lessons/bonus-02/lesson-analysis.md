# Bonus 2 — Come facciamo advertising report per tenere cliente in loop

**Corso:** Claude Speedrun 2 | **Sezione:** Lezioni BONUS (2/6)
**URL:** https://www.andrei-copy.com/cs2online/bonus-2-come-facciamo-advertising-report-per-tenere-cliente-in-loop-7j6dx
**Video:** Vimeo `1178254593`, durata 15:17 (917s)
**Tipo:** **PRATICA** — confermata con 25 frame (16 scan + 9 dense).
**Fonte:** panoramica + "Cosa hai imparato" ufficiali (13 bullet), nessuna trascrizione .md.

---

## Mappa timeline (confermata)

| Tempo | Contenuto | Frame |
|---|---|---|
| 0:00–2:00 | Talking head — intro (setup diverso, altra stanza con lavagna) | — |
| 2:00 | **Whiteboard**: grafico "fiducia/percezione nel tempo" con touchpoint — curva che cala senza contatto, sale con touchpoint regolari | `frame-t2m00s...jpg` |
| 4:00–6:00 | Talking head | — |
| 6:00 | **Demo**: Obsidian, file "Contesto per advertising report" con sezione "Che cosa bisogna fare" | `frame-t6m00s...jpg` |
| 8:00–10:00 | Talking head | — |
| 10:00 | **Demo**: repository GitHub "andrei-kanz", file "style-JSON.json" (brand guidelines) | `frame-t10m00s...jpg` |
| 12:00 | **Demo**: Claude Cowork, task "Complete advertising report" — dati reali inseriti (Budget speso 2.500€, Impression 150.000, Click 4.500 CTR 3%, Conversioni 90, CPA 28,60€, ROAS 3,1x) | `frame-t12m00s...jpg` |
| 12:15 | **Demo — IL CUORE TECNICO**: Cowork valida le 4 informazioni richieste (✓), poi genera il PDF installando **reportlab** (libreria Python) via script — mostra esplicitamente il processo agentico: Running skill → Loading tools → Update todo list → Install reportlab → Writing create_report.py. File di contesto usati: Instructions·CLAUDE.md, style-JSON.json, Contesto per advertising report, istruzioni.md.md. Modello: **Opus 4.6**. | `frame-t12m15s...jpg` |
| 13:15 | **Demo**: PDF finale generato — "Advertising_Report_16-22_Marzo.pdf", 7 pagine, copertina brandizzata "AP SALES", pagine: Executive Summary, Confronto Week-over-Week, Analisi per Piattaforma | `frame-t13m15s...jpg` |
| 14:00–15:17 | Talking head, chiusura | — |

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Principio "percezione è realtà" applicato alla gestione clienti: se il cliente percepisce inattività (anche se il lavoro procede), per lui è come se fosse vero — quindi i touchpoint regolari (report settimanali) sono fondamentali indipendentemente dal reale carico di lavoro svolto. | Panoramica + frame t2m00s |
| KA-02 | Regola operativa: non lasciare mai passare più di una settimana senza un touchpoint intenzionale col cliente advertising (email con report). | "Cosa hai imparato" |
| KA-03 | Architettura del sistema: 4 file di contesto persistenti riutilizzati ogni settimana — file "contesto" (cosa deve fare l'AI), file "istruzioni" (step precisi da seguire sempre), "style-JSON.json" (brand guidelines, tenuto su GitHub), e i dati settimanali incollati al momento. | Panoramica + frame t6m00s, t10m00s |
| KA-04 | **Regola anti-hallucination concreta**: le istruzioni sono scritte in modo che l'AI RIFIUTI di procedere se mancano informazioni obbligatorie — 4 dati richiesti: report ultima settimana, report settimana precedente, decisioni prossima settimana, azioni di miglioramento. Osservato a schermo: step "Validate all 4 required information pieces" completato PRIMA di generare il PDF. | "Cosa hai imparato" + frame t12m15s |
| KA-05 | **Dettaglio tecnico osservato (non nel testo ufficiale)**: Claude Cowork genera il PDF non con un semplice export, ma scrivendo ed eseguendo codice Python con la libreria **reportlab**, installata al volo come step del task agentico ("Install reportlab for PDF creation" → script). Il processo è visibile passo-passo: Running skill → Loading tools → Update todo list → Install reportlab → Writing create_report.py. | frame-t12m15s |
| KA-06 | Output finale verificato: PDF a 7 pagine, brandizzato (copertina "AP SALES"), struttura professionale (Executive Summary, Confronto Week-over-Week, Analisi per Piattaforma). | frame-t13m15s |
| KA-07 | Convenzione naming file: usare trattini, non underscore o spazi, nei nomi dei file di contesto. | "Cosa hai imparato" |
| KA-08 | Il sistema costruito (istruzioni + contesto riutilizzabili + workflow ripetibile) viene esplicitamente definito dall'autore come "di fatto una skill di Claude" — anticipazione concettuale del meccanismo Claude Skills (trattato in Bonus 4). | "Cosa hai imparato" |
| KA-09 | Riutilizzo: per i report successivi basta avviare un nuovo task su Cowork, condividere la stessa cartella e incollare solo i dati aggiornati — zero rilavorazione delle istruzioni. | "Cosa hai imparato" |

## Connessione con Knowledge Base esistente

- KA-04 (regola anti-hallucination: AI rifiuta se mancano dati obbligatori) è un pattern di prompt engineering difensivo concreto e riutilizzabile — potenzialmente rilevante per qualunque skill DE che genera output strutturati da dati esterni (report, dashboard). Singola fonte per ora, vedi enrichment-report.
- KA-01 (percezione=realtà, touchpoint) è coerente con la pratica agency generale ma non specifico di una skill DE esistente.

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — 25 frame visionati, dettaglio tecnico reportlab osservato direttamente (non nel testo ufficiale) |
| NO-STUB | PASS — video 15:17 intero mappato |
| P12 traceability | PASS |

**Prossima:** Bonus 3 — "Come collegare Claude a qualsiasi cosa"
