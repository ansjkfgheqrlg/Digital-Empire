# Workflow: Channel Publishing (Upload)

## Obiettivo
Prendere gli artefatti finiti dalla fabbrica di automazione e caricarli sul canale proprietario clone.

## Triggers
- **Event-based:** Completamento dell'esportazione Fliki e approvazione della miniatura.

## Steps
1. **Raccolta Asset:** Il workflow recupera l'MP4 finale (da Fliki) e il file SEO JSON (dal VidIQ SEO Analyst).
2. **API Upload (o Automazione Browser):** Caricamento del file video tramite YouTube Data API v3 (o script Puppeteer/Playwright se le API sono limitate).
3. **Iniezione Metadati:**
   - Inserimento Titolo SEO.
   - Inserimento Descrizione (con CTA e link in alto).
   - Inserimento Tag "certificati".
4. **Safety Gate (Gate di sicurezza):** Impostazione dello stato su **Unlisted (Non in elenco)** o **Programmato**.
5. **Notifica:** Invio di un messaggio (Slack/Discord) all'operatore umano: "Video pronto per la revisione finale prima della pubblicazione pubblica".
