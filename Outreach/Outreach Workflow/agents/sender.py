"""
Email Sender Agent — Digital Empire Outreach
Invia email via Gmail SMTP usando App Password.

Gratuito — usa il tuo account Gmail personale.
Limite Gmail: 500 email/giorno (free tier), 2000/giorno (Google Workspace).

IMPORTANTE: usa App Password (16 caratteri), NON la password normale del tuo account.
Setup in 2 minuti: vedi SETUP.md sezione 3.
"""

import csv
import os
import smtplib
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


class EmailSenderAgent:
    """
    Agente di invio email via Gmail SMTP.

    Pattern Anthropic: Worker agent di esecuzione (deterministico, no Claude).
    Input:  lista di {email, oggetto, corpo, page_name, ...}
    Output: stessa lista con 'stato' (inviata/errore) e 'timestamp'
    """

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    DELAY_TRA_INVII = float(os.environ.get("EMAIL_DELAY_SECONDS", "3.5"))  # secondi tra invii
    MAX_PER_BATCH   = int(os.environ.get("EMAIL_DAILY_LIMIT", "500"))      # max giornaliero (500 = sicuro Gmail singolo)
    HOURLY_LIMIT    = int(os.environ.get("EMAIL_HOURLY_LIMIT", "100"))     # cap orario anti-spam (drip)

    def __init__(self, gmail_user: str, app_password: str):
        self.mittente = gmail_user
        self.password = app_password
        self._connessione = None

    # ────────────────────────────────────────────────────────────────────────
    # Gestione connessione SMTP (riusa la connessione per efficienza)
    # ────────────────────────────────────────────────────────────────────────

    def _apri_connessione(self) -> smtplib.SMTP:
        """Apre connessione SMTP Gmail."""
        server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT, timeout=30)
        server.ehlo()
        server.starttls()
        server.login(self.mittente, self.password)
        return server

    def _verifica_credenziali(self):
        """Verifica che le credenziali Gmail siano corrette prima di iniziare."""
        try:
            server = self._apri_connessione()
            server.quit()
            print("[SENDER] ✓ Credenziali Gmail verificate")
            return True
        except smtplib.SMTPAuthenticationError:
            print(
                "\n[SENDER] ERRORE AUTENTICAZIONE Gmail.\n"
                "Verifica che GMAIL_APP_PASSWORD sia un'App Password (16 caratteri).\n"
                "Leggi SETUP.md sezione 3 per generarla in 2 minuti.\n"
            )
            return False
        except Exception as e:
            print(f"[SENDER] Errore connessione Gmail: {e}")
            return False

    # ────────────────────────────────────────────────────────────────────────
    # Invio singolo
    # ────────────────────────────────────────────────────────────────────────

    def _invia_singola(self, server: smtplib.SMTP, destinatario: str,
                       oggetto: str, corpo: str) -> bool:
        """Invia una singola email. Restituisce True se successo."""
        msg = MIMEMultipart("alternative")
        msg["Subject"] = oggetto
        msg["From"] = self.mittente
        msg["To"] = destinatario
        msg["Reply-To"] = self.mittente

        # Aggiungi il corpo come testo plain
        msg.attach(MIMEText(corpo, "plain", "utf-8"))

        try:
            server.sendmail(self.mittente, destinatario, msg.as_string())
            return True
        except smtplib.SMTPRecipientsRefused:
            return False  # Email non valida
        except Exception as e:
            print(f"[SENDER] Errore invio a {destinatario}: {e}")
            return False

    # ────────────────────────────────────────────────────────────────────────
    # Anteprima
    # ────────────────────────────────────────────────────────────────────────

    def mostra_anteprima(self, emails: list, prime_n: int = 5):
        """Mostra le prime N email senza inviarle."""
        print(f"\n{'='*70}")
        print(f"ANTEPRIMA — prime {min(prime_n, len(emails))} email su {len(emails)}")
        print(f"{'='*70}")

        for i, email in enumerate(emails[:prime_n], 1):
            print(f"\n[{i}/{len(emails)}]")
            print(f"  A:        {email['email']}")
            print(f"  Business: {email.get('page_name', '?')}")
            print(f"  Settore:  {email.get('settore', '?')} — {email.get('citta', '?')}")
            print(f"  OGGETTO:  {email['oggetto']}")
            print(f"  CORPO:")
            for linea in email["corpo"].split("\n"):
                print(f"    {linea}")

        if len(emails) > prime_n:
            print(f"\n  ... e altre {len(emails) - prime_n} email.")

    # ────────────────────────────────────────────────────────────────────────
    # Interfaccia pubblica dell'agente
    # ────────────────────────────────────────────────────────────────────────

    def run(self, emails: list, anteprima: bool = False,
            output_dir: str = "output") -> list:
        """
        Invia tutte le email o mostra anteprima.

        Args:
            emails:      Lista di dict {email, oggetto, corpo, ...}
            anteprima:   Se True, mostra senza inviare
            output_dir:  Cartella per salvare il log invii

        Returns:
            Lista di dict con 'stato' e 'timestamp' aggiunti
        """
        if anteprima:
            self.mostra_anteprima(emails)
            return []

        if not emails:
            print("[SENDER] Nessuna email da inviare.")
            return []

        # Verifica credenziali prima di iniziare
        if not self._verifica_credenziali():
            return []

        # Limita al massimo sicuro
        if len(emails) > self.MAX_PER_BATCH:
            print(f"[SENDER] Limite giornaliero: taglio a {self.MAX_PER_BATCH}")
            emails = emails[: self.MAX_PER_BATCH]

        risultati = []
        inviati = 0
        errori = 0
        timestamp_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        _blocco_inizio = time.monotonic()   # inizio finestra oraria
        _inviati_blocco = 0                 # contatore nella finestra oraria

        print(f"\n[SENDER] Avvio invio — {len(emails)} email da {self.mittente}")

        try:
            server = self._apri_connessione()

            for i, email in enumerate(emails, 1):
                dest = email["email"]
                oggetto = email["oggetto"]
                corpo = email["corpo"]

                successo = self._invia_singola(server, dest, oggetto, corpo)

                stato = "inviata" if successo else "errore"
                risultati.append({
                    **email,
                    "stato": stato,
                    "timestamp": timestamp_run,
                })

                if successo:
                    inviati += 1
                    print(f"[SENDER] {i}/{len(emails)} ✓ {dest[:45]}")
                else:
                    errori += 1
                    print(f"[SENDER] {i}/{len(emails)} ✗ {dest[:45]}")

                # Pausa tra invii (evita blocco Gmail)
                if i < len(emails):
                    time.sleep(self.DELAY_TRA_INVII)

                # Cap orario: max HOURLY_LIMIT email/ora (drip anti-spam)
                _inviati_blocco += 1
                if _inviati_blocco >= self.HOURLY_LIMIT and i < len(emails):
                    _attesa = 3600 - (time.monotonic() - _blocco_inizio)
                    if _attesa > 0:
                        print(f"[SENDER] Cap orario {self.HOURLY_LIMIT}/h raggiunto — "
                              f"pausa {_attesa/60:.0f} min prima del prossimo blocco")
                        time.sleep(_attesa)
                    _blocco_inizio = time.monotonic()
                    _inviati_blocco = 0

                # Riapri connessione ogni 50 email (keepalive con retry)
                if i % 50 == 0 and i < len(emails):
                    try:
                        server.quit()
                    except Exception:
                        pass
                    for _retry in range(3):
                        try:
                            server = self._apri_connessione()
                            break
                        except Exception as _re:
                            if _retry == 2:
                                raise
                            time.sleep(5)

            server.quit()

        except smtplib.SMTPAuthenticationError:
            print("\n[SENDER] ERRORE: credenziali Gmail non valide. Controlla .env")
        except Exception as e:
            print(f"\n[SENDER] Errore connessione: {e}")

        # Salva log invii
        self._salva_log(risultati, output_dir)

        print(f"\n[SENDER] Completato: {inviati} inviate, {errori} errori")
        return risultati

    def _salva_log(self, risultati: list, output_dir: str):
        """Salva log CSV degli invii."""
        if not risultati:
            return
        Path(output_dir).mkdir(exist_ok=True)
        oggi = datetime.now().strftime("%Y-%m-%d")
        path = Path(output_dir) / f"{oggi}_invio_log.csv"

        campi = ["timestamp", "page_name", "email", "settore", "citta",
                 "oggetto", "stato"]
        esiste = path.exists()

        with open(path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
            if not esiste:
                writer.writeheader()
            writer.writerows(risultati)

        print(f"[SENDER] Log salvato: {path}")
