---
name: build-implementation
description: "Builder per Context Engineering. Scrive codice Python di automazione robusto e production-ready. Attiva per implementazione codice, build di automazioni, sviluppo software."
model: sonnet
---

Devi scrivere codice Python di automazione robusto e production-ready per: $ARGUMENTS

Segui RIGOROSAMENTE questi pattern. Non prendere scorciatoie.

---

## PATTERN 1: STRUTTURA DI OGNI SCRIPT

Ogni script Python che crei DEVE avere questa struttura:

import os
import logging
import time
from datetime import datetime
from dotenv import load_dotenv

# === CONFIGURAZIONE ===
load_dotenv()

# Logging strutturato
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('logs/activity_log.csv'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Variabili da .env
# [CARICA QUI TUTTE LE VARIABILI NECESSARIE]

# === FUNZIONI ===

def main():
    """Funzione principale."""
    logger.info("START: [nome operazione]")
    try:
        # [LOGICA PRINCIPALE]
        pass
    except Exception as e:
        logger.error(f"ERRORE CRITICO: {e}")
        raise
    finally:
        logger.info("END: [nome operazione]")

if __name__ == "__main__":
    main()

## PATTERN 2: CHIAMATE API

OGNI chiamata a un'API esterna DEVE seguire questo pattern con retry e backoff esponenziale:

import requests
import time

def call_api_with_retry(url, method="GET", headers=None,
                         data=None, json_data=None,
                         max_retries=3, base_delay=1):
    """
    Chiama un'API con retry e backoff esponenziale.

    Args:
        url: endpoint URL
        method: GET, POST, PUT, DELETE
        headers: dict di headers
        data: form data
        json_data: JSON body
        max_retries: tentativi massimi
        base_delay: delay iniziale in secondi

    Returns:
        Response object se successo

    Raises:
        Exception dopo max_retries falliti
    """
    for attempt in range(max_retries):
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                json=json_data,
                timeout=30
            )
            response.raise_for_status()
            logger.info(
                f"API OK: {method} {url} "
                f"[{response.status_code}]"
            )
            return response

        except requests.exceptions.Timeout:
            delay = base_delay * (2 ** attempt)
            logger.warning(
                f"API TIMEOUT: {url} "
                f"Tentativo {attempt+1}/{max_retries} "
                f"Retry tra {delay}s"
            )
            time.sleep(delay)

        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                delay = base_delay * (2 ** attempt) * 2
                logger.warning(
                    f"RATE LIMIT: {url} "
                    f"Retry tra {delay}s"
                )
                time.sleep(delay)
            elif response.status_code >= 500:
                delay = base_delay * (2 ** attempt)
                logger.warning(
                    f"SERVER ERROR {response.status_code}: "
                    f"{url} Retry tra {delay}s"
                )
                time.sleep(delay)
            else:
                logger.error(
                    f"API ERROR {response.status_code}: "
                    f"{url} - {e}"
                )
                raise

        except requests.exceptions.ConnectionError:
            delay = base_delay * (2 ** attempt)
            logger.warning(
                f"CONNECTION ERROR: {url} "
                f"Retry tra {delay}s"
            )
            time.sleep(delay)

    raise Exception(
        f"API FALLITA dopo {max_retries} tentativi: "
        f"{method} {url}"
    )

## PATTERN 3: GESTIONE CREDENZIALI

import os
from dotenv import load_dotenv

load_dotenv()

def get_required_env(var_name):
    """Carica una variabile d'ambiente obbligatoria."""
    value = os.getenv(var_name)
    if not value:
        raise EnvironmentError(
            f"Variabile d'ambiente mancante: {var_name}. "
            f"Aggiungila al file .env"
        )
    return value

def get_optional_env(var_name, default=None):
    """Carica una variabile d'ambiente opzionale."""
    return os.getenv(var_name, default)

REGOLA ASSOLUTA: MAI scrivere una API key, password, token o qualsiasi credenziale direttamente nel codice. SEMPRE da .env.

## PATTERN 4: RATE LIMITING

import time

class RateLimiter:
    """Limita la frequenza delle operazioni."""

    def __init__(self, min_interval_seconds=2):
        self.min_interval = min_interval_seconds
        self.last_call = 0

    def wait(self):
        """Aspetta se necessario per rispettare il rate limit."""
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            sleep_time = self.min_interval - elapsed
            time.sleep(sleep_time)
        self.last_call = time.time()

# USO:
limiter = RateLimiter(min_interval_seconds=2)
for item in items:
    limiter.wait()
    result = call_api(item)

## PATTERN 5: COST GUARD

class CostGuard:
    """Monitora e limita i costi delle API."""

    def __init__(self, max_cost_usd=5.0):
        self.max_cost = max_cost_usd
        self.current_cost = 0.0
        self.alert_threshold = max_cost_usd * 0.8
        self.alerted = False

    def add_cost(self, amount):
        """Registra un costo. Blocca se supera il limite."""
        self.current_cost += amount

        if not self.alerted and self.current_cost >= self.alert_threshold:
            logger.warning(
                f"COST ALERT: ${self.current_cost:.2f} / "
                f"${self.max_cost:.2f} (80% raggiunto)"
            )
            self.alerted = True

        if self.current_cost >= self.max_cost:
            raise Exception(
                f"COST LIMIT RAGGIUNTO: "
                f"${self.current_cost:.2f} >= "
                f"${self.max_cost:.2f}. "
                f"Operazione bloccata."
            )

        logger.info(
            f"Costo corrente: ${self.current_cost:.2f} / "
            f"${self.max_cost:.2f}"
        )

    def get_remaining(self):
        return self.max_cost - self.current_cost

## PATTERN 6: VALIDAZIONE INPUT

import re

def validate_email(email):
    """Valida formato email."""
    if not email:
        return False, "Email vuota"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, f"Formato email non valido: {email}"
    return True, "OK"

def validate_required_fields(data, required_fields):
    """Verifica che tutti i campi obbligatori siano presenti."""
    missing = []
    for field in required_fields:
        if field not in data or not data[field]:
            missing.append(field)
    if missing:
        return False, f"Campi mancanti: {', '.join(missing)}"
    return True, "OK"

def sanitize_string(text):
    """Pulisce una stringa da caratteri problematici."""
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r'[<>{}]', '', text)
    return text

## PATTERN 7: LOGGING STRUTTURATO IN CSV

import csv
from datetime import datetime

def log_to_csv(log_file, data_dict):
    """
    Aggiunge una riga a un file CSV di log.
    Crea il file con header se non esiste.
    """
    file_exists = os.path.exists(log_file)

    with open(log_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data_dict.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data_dict)

# USO:
log_to_csv('logs/outreach_log.csv', {
    'timestamp': datetime.now().isoformat(),
    'tipo': 'email_inviata',
    'destinatario': 'marco@test.it',
    'stato': 'successo',
    'errore': ''
})

## PATTERN 8: INVIO EMAIL (SMTP - per cloud)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_smtp(to_email, subject, body_html,
                     sender_email=None, app_password=None):
    """
    Invia email via Gmail SMTP.
    Per uso in cloud (Modal) dove OAuth non e possibile.
    """
    sender = sender_email or get_required_env("GMAIL_SENDER_EMAIL")
    password = app_password or get_required_env("GMAIL_APP_PASSWORD")

    msg = MIMEMultipart('alternative')
    msg['From'] = sender
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body_html, 'html'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        logger.info(f"Email inviata a {to_email}: {subject}")
        return True
    except Exception as e:
        logger.error(f"Invio email fallito a {to_email}: {e}")
        return False

## PATTERN 9: GOOGLE SHEETS

import gspread
from google.oauth2.service_account import Credentials

def get_google_sheet(sheet_id, credentials_path=None):
    """Connessione a Google Sheets."""
    creds_path = credentials_path or get_required_env(
        "GOOGLE_CREDENTIALS_PATH"
    )

    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = Credentials.from_service_account_file(
        creds_path, scopes=scopes
    )
    client = gspread.authorize(credentials)

    return client.open_by_key(sheet_id)

def append_rows_to_sheet(sheet_id, worksheet_name, rows_data):
    """
    Aggiunge righe a un foglio Google Sheets.
    rows_data = lista di dizionari
    """
    sheet = get_google_sheet(sheet_id)
    worksheet = sheet.worksheet(worksheet_name)

    if not rows_data:
        return 0

    headers = list(rows_data[0].keys())

    existing = worksheet.get_all_values()
    if not existing:
        worksheet.append_row(headers)

    for row in rows_data:
        values = [str(row.get(h, '')) for h in headers]
        worksheet.append_row(values)
        time.sleep(1)

    logger.info(
        f"Aggiunte {len(rows_data)} righe "
        f"a {worksheet_name}"
    )
    return len(rows_data)

## REGOLE FINALI

1. OGNI funzione ha un docstring
2. OGNI operazione esterna e in un try/except
3. OGNI azione significativa viene loggata
4. NESSUNA credenziale nel codice
5. NESSUN magic number - tutto in variabili o .env
6. I file vengono creati con encoding='utf-8'
7. I path usano os.path.join() per compatibilita cross-platform
8. Lo script e eseguibile standalone (if __name__ == "__main__")