# Lezione 8 — Context engineering

**Corso:** Claude Speedrun 2 | **Sezione:** AI – Le basi (8/9)
**URL:** https://www.andrei-copy.com/cs2online/lezione-8-context-engineering-y8leg
**Video:** Vimeo `1174236344`, durata 11:36 (696s)
**Tipo:** TEORIA — confermato con 8 frame (talking-head + whiteboard illustrativo).
**Fonte:** trascrizione ufficiale .md integrale (53 righe) + "Cosa hai imparato" (17 bullet).

---

## Tesi centrale

"Non puoi usare l'AI se non conosci ciò che gli dai da fare, perché non sai giudicare l'**input**" — estensione del principio comune ("non puoi giudicare l'output senza essere esperto") spostando il focus dall'output all'input.

## Composizione dell'input per un LLM (fonte primaria)

1. Prompt (la richiesta)
2. Contesto (file allegati, info extra)
3. RAG (contesto tecnico avanzato — fuori scope corso)
4. Training dell'AI
5. System prompt (istruzioni nascoste del provider)

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Riformulazione del principio "expertise per giudicare l'AI": non serve essere esperti solo per giudicare l'OUTPUT, serve esserlo per costruire un buon INPUT — se correggi sempre l'output, l'uso dell'AI perde senso. | Trascrizione |
| KA-02 | Definizione operativa di context engineering: concentrarsi nel costruire le informazioni contestuali che accompagnano il messaggio, per permettere all'AI di prendere decisioni migliori — distinto dal prompt engineering (2022-2023), che si concentrava solo sul testo della richiesta. | Trascrizione |
| KA-03 | Principio "non esiste troppo contesto": più informazioni contestuali dai, migliore è l'output — nessun limite superiore dichiarato (a differenza di altri consigli su sintesi/compressione visti altrove nel corso). | "Cosa hai imparato" |
| KA-04 | L'AI non è progettata per investigare attivamente sull'utente — è programmata per rispondere subito. La responsabilità di fornire il contesto è sempre dell'utente, mai dell'AI. | Trascrizione + "Cosa hai imparato" |
| KA-05 | La memory delle chat passate (feature nativa Claude) NON sostituisce un buon contesto esplicito — "non puoi affidarti al fatto che l'AI si ricordi cose dette prima". | "Cosa hai imparato" |
| KA-06 | Aneddoto personale: i prompt dell'autore sono "fatti in modo molto informale" via dictation vocale Mac (10 minuti di parlato) — perché il lavoro pesante lo fa il contesto pre-costruito, non la forma del prompt. | Trascrizione |
| KA-07 | Il contesto varia per tipo di AI: documenti Markdown per LLM testuali; immagini stesse come contesto per generatori di immagini (es. Flux). | Trascrizione |

## Connessione con Knowledge Base esistente

- KA-01/KA-02 sono la 6a variante del principio cardine del corso (garbage in garbage out / responsabilità umana nel contesto) — nessuna nuova azione, pattern ormai maturo e ben documentato nel run.
- KA-03 ("non esiste troppo contesto") è in leggera tensione apparente con la regola di lezione 6 ("editing manuale per non sprecare contesto, togliere parti inutili") — non è una contraddizione reale (qui si parla di rilevanza dell'informazione, lì di compressione/pulizia editoriale), ma vale la pena notare la sfumatura per accuratezza.

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — trascrizione ufficiale + 8 frame confermano classificazione |
| NO-STUB | PASS — trascrizione intera (53 righe) |
| P12 traceability | PASS |

**Prossima lezione:** Lezione 9 — "Come dare contesto alle AI" (ultima lezione sezione "AI – Le basi")
