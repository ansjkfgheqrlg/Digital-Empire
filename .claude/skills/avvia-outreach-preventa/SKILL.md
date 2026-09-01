---
name: avvia-outreach-preventa
description: Avvia il flusso giornaliero completo di outreach Preventa (scraping concessionari import-focus -> qualifica -> push Areus -> invio WhatsApp reale, fino a 50/giorno). Apre una finestra CMD visibile. Usa quando l'utente scrive /avvia-outreach-preventa o vuole avviare l'outreach Preventa, mandare i messaggi ai concessionari, far partire lo scraping+invio automatico.
metadata:
  version: 1.0.0
---

# Avvia Outreach Preventa (scraping import-focus + invio WhatsApp)

Apri SUBITO una finestra CMD visibile col flusso completo. NESSUNA domanda — esegui direttamente.

## Cosa fa (in automatico, un solo comando)

1. **Scraping** — pesca 6 città/giorno a rotazione da `05-TEMPLATES-E-KIT/cities.txt`,
   cerca su Google Maps con query orientate a concessionari **import** (non genériche).
2. **Qualifica + push Areus** — ogni lead nuovo entra in `EmpireDesk/state/preventa_leads.json`
   con stage `NEW`, classificato mobile/fisso.
3. **Invio WhatsApp reale** — fino a 50 messaggi/giorno ai lead NEW con telefono mobile
   (i lead import passano a qualsiasi priorità sito, gancio dedicato "annunci esteri";
   gli altri solo ALTA/MEDIA). Ritmo umano (45-120s tra invii), si ferma da solo se rileva
   segnali di blocco account WhatsApp. Stage -> `CONTACTED` dopo ogni invio reale.
4. **Report** — scrive log in `preventa-maps-scraper/logs/outreach_YYYY-MM-DD.log`.

**Richiede**: sessione WhatsApp già collegata (`Outreach/WhatsApp Automation/whatsapp-profile/`
già creata da `refresh_session.py` — fatto una tantum). Se il profilo è in uso o mancante,
il flusso si ferma e lo dice chiaro, non manda a vuoto.

## Azione immediata

```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\preventa-maps-scraper" && echo. && echo  ===================================================== && echo   OUTREACH PREVENTA - scraping import + invio WhatsApp (max 50/giorno) && echo  ===================================================== && echo. && python outreach_giornaliero.py'
```

Dopo aver lanciato il comando, di' all'utente:
- "CMD aperto — outreach Preventa avviato (scraping import + invio WhatsApp, max 50 oggi)."
- Ricorda che il run richiede tempo (scraping + pause umane tra invii): tipicamente 1-2 ore.

## Varianti utili (solo se l'utente le chiede esplicitamente)

- Test sicuro (1 città, invio in dry-run, non manda nulla davvero): aggiungi `--test` al comando.
- Cap invii personalizzato: `--daily-cap 20`.
- Solo scraping, senza inviare: `--solo-scraping`.
- Solo invio (Areus già popolato da un run precedente): `--solo-invio`.
