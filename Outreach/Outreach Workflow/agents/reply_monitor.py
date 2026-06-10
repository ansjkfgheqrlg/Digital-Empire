"""
Reply Monitor Agent — Digital Empire Outreach
=============================================
Controlla Gmail IMAP per rilevare risposte dai lead contattati.

Strategia:
- Cerca nella INBOX messaggi FROM degli indirizzi email nel DB
- Ignora email già registrate in DB (dedup su risposta_ricevuta)
- Restituisce lista di risposte con testo e metadati

Usa le stesse credenziali Gmail (App Password) del sender.
"""

import email as email_lib
import imaplib
import re
import sqlite3
import time
from datetime import datetime
from email.header import decode_header


IMAP_SERVER = "imap.gmail.com"
IMAP_PORT   = 993


def _decodifica_header(valore: str) -> str:
    if not valore:
        return ""
    parti = decode_header(valore)
    risultato = []
    for parte, encoding in parti:
        if isinstance(parte, bytes):
            risultato.append(parte.decode(encoding or "utf-8", errors="replace"))
        else:
            risultato.append(parte)
    return " ".join(risultato)


def _estrai_testo(msg) -> str:
    """Estrae il testo plain dall'email (gestisce multipart)."""
    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            cd = str(part.get("Content-Disposition", ""))
            if ct == "text/plain" and "attachment" not in cd:
                payload = part.get_payload(decode=True)
                charset = part.get_content_charset() or "utf-8"
                if payload:
                    return payload.decode(charset, errors="replace")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            charset = msg.get_content_charset() or "utf-8"
            return payload.decode(charset, errors="replace")
    return ""


def _pulisci_reply(testo: str) -> str:
    """Rimuove il quoted text (righe che iniziano con >) e header vecchi."""
    righe = testo.split("\n")
    pulite = []
    for riga in righe:
        r = riga.strip()
        # Salta righe quote e separatori
        if r.startswith(">"):
            break  # Tutto il quoted text è dopo la prima riga con >
        if re.match(r"^(On .+ wrote:|Il .+ ha scritto:|From:|To:|Subject:|Date:|Da:|A:|Oggetto:|Data:)", r):
            break
        pulite.append(riga)
    testo_pulito = "\n".join(pulite).strip()
    # Se il risultato è vuoto (tutto quoted), restituisce il testo originale troncato
    return testo_pulito if len(testo_pulito) > 10 else testo[:500].strip()


class ReplyMonitorAgent:
    """
    Team Supplementare — Reply Monitor: rileva risposte Gmail dai lead.

    Input:  Gmail credentials + DB path
    Output: Lista di dict {email, reply_text, reply_date, reply_subject, page_name}
    """

    def __init__(self, gmail_user: str, app_password: str, db_path: str):
        self.gmail_user  = gmail_user
        self.app_password = app_password
        self.db_path     = db_path

    def _carica_lead_contattati(self) -> dict:
        """Carica dal DB tutti gli indirizzi email contattati (email → lead dict)."""
        leads = {}
        try:
            with sqlite3.connect(self.db_path) as conn:
                rows = conn.execute("""
                    SELECT email, page_name, settore, citta, oggetto, corpo,
                           f1_inviata, f2_inviata, risposta_ricevuta
                    FROM leads_contattati
                    WHERE stato IN ('inviata', 'f1_inviata', 'f2_inviata')
                    AND risposta_ricevuta IS NULL
                """).fetchall()
            for r in rows:
                leads[r[0].lower().strip()] = {
                    "email": r[0], "page_name": r[1], "settore": r[2],
                    "citta": r[3], "oggetto": r[4], "corpo": r[5],
                    "f1_inviata": r[6], "f2_inviata": r[7],
                }
        except Exception as e:
            print(f"[REPLY-MONITOR] Errore lettura DB: {e}")
        return leads

    def _connetti_imap(self) -> imaplib.IMAP4_SSL | None:
        """Apre connessione IMAP Gmail."""
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
            mail.login(self.gmail_user, self.app_password)
            return mail
        except imaplib.IMAP4.error as e:
            print(f"[REPLY-MONITOR] Errore login IMAP: {e}")
            print("  Verifica GMAIL_APP_PASSWORD nel .env (deve essere App Password 16 char).")
            return None
        except Exception as e:
            print(f"[REPLY-MONITOR] Errore connessione IMAP: {e}")
            return None

    def _cerca_risposte(self, mail: imaplib.IMAP4_SSL, lead_emails: set) -> list:
        """Cerca in INBOX email FROM i lead contattati."""
        risposte = []
        try:
            mail.select("INBOX")
            # Cerca nelle ultime 30 giorni per efficienza
            _, msgnums = mail.search(None, "ALL")
            if not msgnums or not msgnums[0]:
                return []

            ids = msgnums[0].split()
            # Leggi solo le ultime 200 email per non sovraccaricare
            ids_da_leggere = ids[-200:]

            for num in reversed(ids_da_leggere):
                try:
                    _, data = mail.fetch(num, "(RFC822.HEADER)")
                    if not data or not data[0]:
                        continue
                    raw_header = data[0][1]
                    msg_header = email_lib.message_from_bytes(raw_header)
                    from_raw = msg_header.get("From", "")
                    # Estrai indirizzo email dal From header
                    match = re.search(r"[\w.+-]+@[\w.-]+\.\w+", from_raw)
                    if not match:
                        continue
                    from_email = match.group(0).lower().strip()

                    if from_email not in lead_emails:
                        continue

                    # Leggi l'email completa solo se è un lead
                    _, full_data = mail.fetch(num, "(RFC822)")
                    if not full_data or not full_data[0]:
                        continue
                    raw_email = full_data[0][1]
                    msg = email_lib.message_from_bytes(raw_email)

                    subject  = _decodifica_header(msg.get("Subject", ""))
                    date_str = msg.get("Date", "")
                    testo    = _estrai_testo(msg)
                    testo    = _pulisci_reply(testo)

                    if not testo or len(testo.strip()) < 5:
                        continue

                    risposte.append({
                        "email":         from_email,
                        "reply_subject": subject,
                        "reply_date":    date_str,
                        "reply_text":    testo.strip()[:2000],
                    })

                except Exception:
                    continue

        except Exception as e:
            print(f"[REPLY-MONITOR] Errore ricerca INBOX: {e}")

        return risposte

    def run(self) -> list:
        """
        Controlla Gmail INBOX per risposte dai lead contattati.

        Returns:
            Lista di dict {email, page_name, settore, citta, reply_text,
                          reply_date, reply_subject, oggetto_originale, corpo_originale}
        """
        print("\n[REPLY-MONITOR] Controllo risposte in Gmail...")

        leads_db = self._carica_lead_contattati()
        if not leads_db:
            print("[REPLY-MONITOR] Nessun lead da monitorare nel DB.")
            return []

        print(f"[REPLY-MONITOR] Monitoring {len(leads_db)} lead senza risposta...")

        mail = self._connetti_imap()
        if not mail:
            return []

        try:
            lead_emails = set(leads_db.keys())
            risposte_raw = self._cerca_risposte(mail, lead_emails)
        finally:
            try:
                mail.logout()
            except Exception:
                pass

        # Arricchisci con dati dal DB
        risposte = []
        for r in risposte_raw:
            email_lead = r["email"]
            if email_lead in leads_db:
                lead = leads_db[email_lead]
                risposte.append({
                    **lead,
                    "reply_text":         r["reply_text"],
                    "reply_date":         r["reply_date"],
                    "reply_subject":      r["reply_subject"],
                    "oggetto_originale":  lead.get("oggetto", ""),
                    "corpo_originale":    lead.get("corpo", ""),
                })

        # Dedup per email (prendi solo la prima risposta per lead)
        visti = set()
        risposte_uniche = []
        for r in risposte:
            if r["email"] not in visti:
                visti.add(r["email"])
                risposte_uniche.append(r)

        print(f"[REPLY-MONITOR] Risposte trovate: {len(risposte_uniche)}")
        for r in risposte_uniche:
            print(f"  ↩  {r['email'][:40]} — {r.get('page_name','?')[:30]}")

        return risposte_uniche
