# Progetto: Dose Mentale Remake (Automated Channel)

## Obiettivo
Creare un ecosistema end-to-end che clona il modello di business e i contenuti del canale "Dose Mentale" (https://www.youtube.com/@dosementale), rielaborandoli per evitare violazioni di copyright e migliorandone le metriche di ritenzione e SEO. I video generati verranno pubblicati automaticamente su un nuovo canale proprietario.

## La Pipeline a 5 Stadi (End-to-End)
1. **Ingestion (yt-ingester):** Monitora `@dosementale`, scarica i video più performanti (o gli ultimi usciti) ed estrae la trascrizione esatta (Transcript).
2. **Analisi (vidiq-seo-analyst):** Estrae i metadati originali (Titolo, Tag, Descrizione, VPH) e progetta il pacchetto SEO per "battere" l'originale.
3. **Riscrittura (script-engineer):** Prende la trascrizione grezza, la RIFÀ da zero (per non infrangere il copyright), inserisce nuovi Ganci (Hook) più potenti e ottimizza la ritenzione.
4. **Produzione (fliki-operator):** Genera il video tramite Fliki con voce neurale, musica in background e B-Roll automatizzati.
5. **Pubblicazione (yt-publisher):** Prende l'MP4 finale e i metadati SEO, caricando e programmando il video sul nuovo canale.

## Sicurezza & Copyright (Pre-Mortem)
- **Rischio:** Copyright Strike.
- **Soluzione:** MAI usare le clip video o l'audio originale. Il sistema estrae solo il *concetto* e il testo, che viene obbligatoriamente riscritto dallo `script-engineer` usando parole e analogie diverse. Il video finale è un'opera derivata 100% originale.
