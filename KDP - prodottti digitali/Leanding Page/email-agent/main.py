import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import stripe
from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
SENDER_NAME = os.getenv("SENDER_NAME", "Max")
EBOOK_DOWNLOAD_URL = os.getenv("EBOOK_DOWNLOAD_URL")


def send_ebook(customer_email: str, customer_name: str = None):
    nome = customer_name.split()[0] if customer_name else "ciao"

    body = f"""Ciao {nome},

grazie per l'acquisto — apprezzo davvero.

Ecco il link per scaricare il tuo PDF de "Le 48 Leggi dei Maestri Dimenticati":

{EBOOK_DOWNLOAD_URL}

Leggilo con calma, non è un libro da divorare tutto di un fiato — ogni legge merita riflessione.

Se hai domande o vuoi dirmi com'è andata, rispondi pure a questa email.

Max"""

    msg = MIMEMultipart()
    msg["From"] = f"{SENDER_NAME} <{GMAIL_ADDRESS}>"
    msg["To"] = customer_email
    msg["Subject"] = "Ecco il tuo manuale 📖"
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_ADDRESS, customer_email, msg.as_string())

    print(f"[OK] Email inviata a {customer_email}")


@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Firma webhook non valida")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session.get("customer_details", {}).get("email")
        customer_name = session.get("customer_details", {}).get("name", "")

        if customer_email:
            try:
                send_ebook(customer_email, customer_name)
            except Exception as e:
                print(f"[ERRORE] Invio email fallito per {customer_email}: {e}")
                raise HTTPException(status_code=500, detail="Errore invio email")

    return {"status": "ok"}


@app.get("/health")
def health():
    return {"status": "online"}
