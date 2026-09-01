Devi deployare nel cloud il seguente sistema: $ARGUMENTS

Segui questo protocollo per creare un deployment robusto e production-ready.

---

## FASE 1: PRE-DEPLOYMENT ASSESSMENT

Prima di scrivere qualsiasi codice di deployment, verifica:

### 1.1 Il Sistema e Pronto?

- Tutti gli script funzionano in locale?
- Tutti i test passano?
- Il review (review-and-heal) e stato completato?
- Nessuna credenziale hardcoded?
- Il sistema e stato testato end-to-end almeno una volta?

Se qualsiasi punto e NO, FERMATI.
Non deployare un sistema non testato.
Di all'utente cosa deve fare prima.

### 1.2 Cosa Va nel Cloud e Cosa No

SI CARICA:
- Script di implementation/ (adattati come cloud functions)
- Logica di business
- Templates email/report (embeddati negli script)

NON SI CARICA:
- .env (le variabili vanno nei Secrets della piattaforma)
- credentials/ (le credenziali vanno nei Secrets)
- CLAUDE.md (e per il workspace locale)
- L'LLM stesso (Claude Code non gira nel cloud)
- Contesto conversazionale

IMPLICAZIONE CRITICA:
Nel cloud NON c'e self-healing.
Gli script sono deterministici.
Se qualcosa si rompe serve intervento umano.
Quindi: TESTA TUTTO prima di deployare.

## FASE 2: DETERMINA IL TIPO DI TRIGGER

Per ogni workflow da deployare, determina il trigger corretto:

EVENT-DRIVEN (webhook):
- QUANDO USARLO: il sistema deve reagire IMMEDIATAMENTE a un evento
- ESEMPI: lead cambia stato nel CRM, form submission, pagamento ricevuto
- LATENZA: secondi
- IMPLEMENTAZIONE: endpoint web che riceve una richiesta POST

SCHEDULE-DRIVEN (cron):
- QUANDO USARLO: il sistema deve eseguire controlli periodici
- ESEMPI: controllo fatture giornaliero, scraping settimanale, report mensile
- LATENZA: dipende dalla frequenza del cron
- IMPLEMENTAZIONE: funzione schedulata

MANUALE:
- QUANDO USARLO: l'utente decide quando eseguire
- ESEMPI: estrazione lead su richiesta, invio campagna email
- LATENZA: istantanea (su richiesta)
- IMPLEMENTAZIONE: endpoint callable o CLI

REGOLA: MAI usare polling (check ogni X minuti) quando serve event-driven. Il polling spreca risorse e introduce latenza che puo costare conversioni.

## FASE 3: STRUTTURA CLOUD FUNCTION (Modal)

### 3.1 Struttura Base

import modal
import os
import logging
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# === APP MODAL ===
app = modal.App("[nome-progetto]-[nome-workflow]")

# === IMMAGINE (dipendenze) ===
image = modal.Image.debian_slim(python_version="3.11").pip_install(
    "requests",
    "gspread",
    "google-auth",
    # [aggiungi tutte le dipendenze necessarie]
)

# === SECRETS ===
# Configurati nella dashboard Modal, NON nel codice
secrets = [modal.Secret.from_name("[nome-secrets]")]

### 3.2 Per Trigger Event-Driven (Webhook)

@app.function(image=image, secrets=secrets)
@modal.web_endpoint(method="POST")
def webhook_handler(request_data: dict):
    """
    Riceve webhook e esegue il workflow.
    URL generato da Modal al deploy.
    """
    try:
        # 1. Valida il payload
        # 2. Estrai i dati rilevanti
        # 3. Esegui la logica di business
        # 4. Rispondi con status

        return {"status": "success", "message": "Processato"}

    except Exception as e:
        # Invia alert email
        send_alert_email(f"Webhook fallito: {e}")
        return {"status": "error", "message": str(e)}

### 3.3 Per Trigger Schedule (Cron)

@app.function(
    image=image,
    secrets=secrets,
    schedule=modal.Cron("0 9 * * 1-5")  # Lun-Ven 9:00 UTC
)
def daily_check():
    """
    Controllo giornaliero schedulato.
    """
    try:
        # 1. Connettiti ai servizi necessari
        # 2. Esegui i controlli
        # 3. Esegui le azioni necessarie
        # 4. Logga i risultati

        send_summary_email("Daily check completato: ...")

    except Exception as e:
        send_alert_email(f"Daily check fallito: {e}")
        raise

### 3.4 Funzione di Alert (Sempre Presente)

def send_alert_email(error_message):
    """Invia email di alert quando qualcosa fallisce."""
    sender = os.environ["GMAIL_SENDER_EMAIL"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    owner = os.environ["OWNER_EMAIL"]

    msg = MIMEText(
        f"ALERT SISTEMA AUTOMATICO\n\n"
        f"Errore: {error_message}\n"
        f"Timestamp: {datetime.now().isoformat()}\n\n"
        f"Intervieni appena possibile."
    )
    msg['Subject'] = f"Alert: {error_message[:50]}"
    msg['From'] = sender
    msg['To'] = owner

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)
    except:
        pass  # Se anche l'alert fallisce il log di Modal lo cattura

## FASE 4: CRON SYNTAX REFERENCE

FORMATO: minuto ora giorno_mese mese giorno_settimana

ESEMPI UTILI:
"0 9 * * 1-5"    = Lun-Ven alle 9:00
"0 8 * * 1"      = Ogni lunedi alle 8:00
"0 9,14 * * 1-5" = Lun-Ven alle 9:00 e 14:00
"0 */2 * * *"    = Ogni 2 ore
"30 8 1 * *"     = Il primo del mese alle 8:30

NOTA: gli orari sono in UTC.
Italia = UTC+1 (inverno) / UTC+2 (estate)
Quindi "9:00 Italia" = "0 7 * * *" in inverno
                     = "0 8 * * *" in estate

## FASE 5: DEPLOYMENT STEP-BY-STEP

### 5.1 Configura i Secrets su Modal
1. Vai su modal.com, Dashboard, Secrets
2. Crea nuovo secret: "[nome]-secrets"
3. Aggiungi TUTTE le variabili dal .env
4. Per Gmail nel cloud: usa GMAIL_APP_PASSWORD (non OAuth, che richiede browser)

### 5.2 Dry Run
modal run deployment/[file].py
Verifica che funzioni senza errori.

### 5.3 Deploy
modal deploy deployment/[file].py
Salva l'URL del webhook (se event-driven).

### 5.4 Configura il Trigger Esterno
Per webhook: configura il servizio esterno (ClickUp, Stripe, ecc.) per chiamare l'URL di Modal.

### 5.5 Test Post-Deploy
1. Triggera il workflow (manualmente o simulando l'evento)
2. Verifica che il risultato sia corretto
3. Verifica i log su Modal dashboard
4. Verifica che l'alert email funzioni (testa forzando un errore)

## FASE 6: MONITORING

Dopo il deploy, configura:
- Alert email per run falliti (gia implementato nel codice con send_alert_email)
- Check settimanale della dashboard Modal
- Report mensile di: run totali, costi, errori
- Se un workflow non gira per 48h+ investigare (potrebbe essere down)

## FASE 7: ROLLBACK

Se qualcosa va storto dopo il deploy:

# Stoppa il deployment
modal app stop [nome-app]

# Correggi in locale
# Testa in locale
# Ri-deploya
modal deploy deployment/[file].py

Presenta all'utente:
- URL webhook (se event-driven)
- Schedule configurato (se cron)
- Come verificare che funziona
- Come fermare in caso di emergenza
- Costo stimato mensile