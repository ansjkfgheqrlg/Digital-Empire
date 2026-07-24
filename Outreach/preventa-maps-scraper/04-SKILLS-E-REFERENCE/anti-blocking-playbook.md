# Playbook Anti-Blocco per Google Maps Scraper

Google Maps ha dei sistemi di protezione anti-bot e anti-scraping che possono attivarsi in presenza di attività insolite. Questo playbook elenca i pattern di mitigazione implementati e le procedure in caso di blocco (Captcha).

## Pattern Anti-Blocco Implementati

1. **Uso di Browser Reale (Playwright headed)**:
   - Di default, lo scraper consiglia la modalità headed (visibile). I browser headless hanno un'impronta di impronta digitale (fingerprint) molto diversa e vengono bloccati più facilmente.
2. **Rimozione del flag di automazione**:
   - Lanciamo Chromium con il flag `--disable-blink-features=AutomationControlled` per impedire ai siti di rilevare l'oggetto `navigator.webdriver`.
3. **User-Agent e Viewport realistici**:
   - Usiamo un User-Agent Windows/Chrome moderno e fisso, accoppiato a una risoluzione viewport comune (1366x850).
4. **Ritardi Casuali (Jitter)**:
   - Lo scraper include pause casuali tra le azioni per simulare il comportamento di un operatore umano:
     - `random_delay(0.6, 1.2)` tra i click dell'elenco.
     - `random_delay(2.0, 3.5)` dopo il caricamento dei dettagli.
     - Pausa di `3.0 - 6.0` secondi tra la ricerca di diverse città.

## Procedura in caso di Blocco (Captcha o Schermata Bianca)

Se lo scraper inizia a produrre screenshot di debug vuoti o se vedi una schermata di Captcha:

1. **Fermare immediatamente lo scraper**: non continuare a fare tentativi consecutivi per evitare il ban dell'indirizzo IP.
2. **Attendere 30-60 minuti**: per consentire il raffreddamento dei limiti di connessione.
3. **Eseguire in modalità headed**: assicurarsi di NON usare `--headless`.
4. **Cambiare indirizzo IP (se possibile)**: riavviare il router se si ha un IP dinamico, o usare una connessione mobile hotspot.
5. **Risolvere manualmente**: se viene presentato un Captcha in modalità headed, puoi risolverlo manualmente direttamente nella finestra del browser aperta da Playwright prima che lo script vada in timeout.
