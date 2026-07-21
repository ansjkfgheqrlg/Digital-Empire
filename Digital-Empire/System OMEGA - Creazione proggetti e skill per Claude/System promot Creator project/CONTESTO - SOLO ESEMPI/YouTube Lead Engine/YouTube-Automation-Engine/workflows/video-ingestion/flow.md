# Workflow: Video Ingestion & Rip-off

## Obiettivo
Monitorare il canale bersaglio (@dosementale), identificare i nuovi video e scaricarne il "codice sorgente" (trascrizione testuale) senza violare il copyright.

## Triggers
- **Webhook/RSS:** Notifica di nuovo video sul canale.
- **Cronjob:** Controllo ogni 24 ore.

## Steps
1. **Rilevamento:** Identificazione del nuovo link YouTube.
2. **Download Metadati:** Salvataggio Titolo e Descrizione originali in JSON.
3. **Scraping Subtitles:** Estrazione dei sottotitoli (VTT/SRT) tramite `yt-dlp` o servizi terzi.
4. **Pulizia Testo:** Rimozione di timestamp e conversione in testo leggibile puro (Raw Transcript).
5. **Handoff:** Invio del Raw Transcript allo `script-engineer` per la totale riscrittura (anti-plagio) e al `vidiq-seo-analyst` per l'estrazione delle keyword.
