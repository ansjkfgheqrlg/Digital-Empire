# Bonus 2 — Come facciamo advertising report per tenere cliente in loop (Claude Speedrun 2)

**Fonte:** panoramica ufficiale + "Cosa hai imparato" (13 bullet) + 25 frame video visionati nativamente. Nessuna trascrizione .md.

---

## Panoramica ufficiale

In questa lezione impari a costruire un sistema AI per creare advertising report da inviare ai tuoi clienti di advertising. Andrei spiega perché i touchpoint costanti sono fondamentali per mantenere la fiducia del cliente (percezione = realtà), e poi mostra passo passo come creare una cartella con file di contesto, istruzioni in Markdown e brand guidelines in JSON. Tutto viene dato in pasto a Claude Cowork, che valida i dati ricevuti e genera un report PDF professionale. Il sistema è riutilizzabile all'infinito: crei le istruzioni una volta, le usi ogni settimana.

## "Cosa hai imparato" (ufficiale, integrale)

- Perché i touchpoint costanti con il cliente sono fondamentali per mantenere la fiducia durante una collaborazione di advertising
- Come funziona il concetto "percezione è realtà" applicato alla gestione clienti: se il cliente pensa che non lavori, per lui è come se fosse vero
- Come aggiungere touchpoint intenzionali (email con report) per non lasciare mai più di una settimana senza contatto
- Come usare Obsidian per scrivere file in Markdown (alternativa gratuita a altri editor)
- Come creare un file di contesto (contesto-per-advertising-report.md) che spiega all'AI cosa deve fare
- Come creare un file di istruzioni (istruzioni.md) con step precisi che l'AI deve seguire ogni volta
- Come strutturare le istruzioni in modo che l'AI rifiuti di procedere se mancano informazioni obbligatorie
- Quali sono le 4 informazioni necessarie per compilare un advertising report: report ultima settimana, report settimana precedente, decisioni per la prossima settimana, azioni di miglioramento
- Come scaricare e usare un file brand-guidelines.json da GitHub per mantenere coerenza visiva nel report
- Come usare i trattini (non underscore o spazi) nei nomi dei file
- Come avviare un task su Claude Cowork con cartella condivisa, selezionando Opus 4.6 con Extended Thinking
- Come il sistema appena creato è di fatto una "skill" di Claude (anticipazione della lezione sulle skill)
- Come riutilizzare le istruzioni create: basta avviare un nuovo task su Cowork, condividere la cartella e incollare i dati aggiornati

## Timeline demo (sintesi, vedi lesson-analysis.md per dettaglio)

Whiteboard (grafico fiducia/touchpoint) → Obsidian (file contesto) → GitHub (style-JSON.json) → Claude Cowork (validazione 4 dati obbligatori → generazione PDF via reportlab/Python, osservato passo-passo) → PDF finale verificato (7 pagine, "AP SALES", Executive Summary + Confronto Week-over-Week + Analisi per Piattaforma).

## Dettaglio tecnico osservato solo a schermo (non nel testo ufficiale)

Claude Cowork non si limita a "scrivere" il report: installa la libreria Python `reportlab` come step del task agentico e scrive/esegue codice (`create_report.py`) per generare il PDF. Sequenza osservata: Running skill → Loading tools → Update todo list → Install reportlab for PDF creation → Writing create_report.py.

## Workflow ufficiali citati

1. Creare il sistema di Advertising Report da zero
2. Generare un Advertising Report con Claude Cowork
3. Riutilizzare il sistema per i report successivi

## Link utili

Claude/Claude.ai, Obsidian, GitHub, Gemini (Google).
