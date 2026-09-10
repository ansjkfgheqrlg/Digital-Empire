import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import stripe
from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv

import catalogo as cat

load_dotenv()

app = FastAPI()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
SENDER_NAME = os.getenv("SENDER_NAME", "Max")
# I link di download NON stanno qui: ogni prodotto dichiara in prodotti.json
# il NOME della sua variabile .env (campo "download_env").


def invia_email(customer_email: str, oggetto: str, corpo: str):
    """Spedizione pura via Gmail SMTP. Non sa nulla di prodotti."""
    msg = MIMEMultipart()
    msg["From"] = f"{SENDER_NAME} <{GMAIL_ADDRESS}>"
    msg["To"] = customer_email
    msg["Subject"] = oggetto
    msg.attach(MIMEText(corpo, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_ADDRESS, customer_email, msg.as_string())

    print(f"[OK] Email inviata a {customer_email}")


def consegna(chiave_prodotto: str, customer_email: str, customer_name: str = None):
    """Compone la email del prodotto risolto e la spedisce."""
    catalogo = cat.carica_catalogo()
    oggetto, corpo = cat.componi_email(chiave_prodotto, catalogo, customer_name)
    invia_email(customer_email, oggetto, corpo)


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
        dettagli = session.get("customer_details") or {}
        customer_email = dettagli.get("email")
        customer_name = dettagli.get("name", "")
        session_id = session.get("id")

        # Pagamenti asincroni: la sessione puo' completarsi senza essere pagata.
        if session.get("payment_status") == "unpaid":
            cat.logga_fallimento("NON_PAGATO", customer_email,
                                 dettaglio="payment_status=unpaid", session_id=session_id)
            return {"status": "ok"}

        if not customer_email:
            cat.logga_fallimento("EMAIL_CLIENTE_ASSENTE", None,
                                 dettaglio="customer_details senza email",
                                 session_id=session_id)
            return {"status": "ok"}

        catalogo = cat.carica_catalogo()
        chiave, motivo = cat.risolvi_prodotto(session, catalogo)

        # Mai consegnare il prodotto sbagliato: se non e' certo, si logga e basta.
        if not chiave:
            ids = cat.identificatori_sessione(session)
            cat.logga_fallimento(
                cat.NON_RISOLTO, customer_email,
                dettaglio="metadata=%s payment_link=%s price_ids=%s -- aggiungi "
                          "questo identificatore in prodotti.json e rimanda a mano"
                          % (ids["metadata_prodotto"] or "-",
                             ids["payment_link"] or "-",
                             ",".join(ids["price_ids"]) or "-"),
                session_id=session_id,
            )
            print(f"[ATTENZIONE] Prodotto non riconosciuto per {customer_email}: nessun invio")
            return {"status": "ok"}

        print(f"[INFO] Prodotto '{chiave}' riconosciuto via {motivo}")

        try:
            consegna(chiave, customer_email, customer_name)
        except Exception as e:
            print(f"[ERRORE] Invio email fallito per {customer_email}: {e}")
            cat.logga_fallimento("INVIO_FALLITO", customer_email, chiave,
                                 dettaglio=repr(e), session_id=session_id)
            # 500 di proposito: Stripe ritenta la consegna del webhook.
            raise HTTPException(status_code=500, detail="Errore invio email")

    return {"status": "ok"}


@app.get("/health")
def health():
    return {"status": "online"}
