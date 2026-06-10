import smtplib
print("Testing SMTP connection...")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as srv:
        srv.login("max.infoproducer@gmail.com", "kkgj pnsh vupw rily")
        print("LOGIN OK")
except Exception as e:
    print(f"ERRORE: {e}")
