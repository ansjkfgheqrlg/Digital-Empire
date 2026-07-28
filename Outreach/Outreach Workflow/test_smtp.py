import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

print("Testing SMTP connection...")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as srv:
        srv.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        print("LOGIN OK")
except Exception as e:
    print(f"ERRORE: {e}")
