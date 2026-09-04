#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EMPERATOR — caricamento integrale all'apertura della sessione (SessionStart).

PERCHE' ESISTE (ordine di Max, 2026-09-03).
Fino a oggi la dottrina viaggiava dentro `emperator_hook.py` come stringa compressa,
riniettata AD OGNI messaggio che pronunciava il nome. Misurato quel giorno:
  - promemoria ripetuto ogni messaggio : ~34.700 caratteri
  - libro vero (.claude/agents/emperator.md) : ~56.000 caratteri
Quindi chi diceva "Emperator" riceveva il ~60% di Emperator, e lo pagava trenta volte
in una chat da trenta messaggi. Max ha rifiutato il compromesso ("non posso accettare
che tu sia al 60%, vale anche per Gael e Neri") e ha scelto la strada opposta:

  IL LIBRO INTERO, UNA VOLTA SOLA, ALL'APERTURA DELLA SESSIONE.

Risultato: 100% di Emperator dal primo secondo, e circa dieci volte meno contesto
consumato su una chat lunga, perche' la dottrina smette di ripetersi.

CONSEGUENZA ARCHITETTURALE: da adesso `.claude/agents/emperator.md` e' l'UNICA fonte
di verita' della dottrina. L'hook per messaggio non ne contiene piu' una copia — la
"doppia scrittura" (emperator.md 6.13) e' superata da una sola scrittura sul libro.

Regole di costruzione, gia' pagate da questo repo:
  - B-013/B-031: stdout scritto come byte UTF-8 espliciti, mai affidato al codec console.
  - Non fallisce MAI l'apertura della sessione: qualunque errore -> esce 0.
  - Solo letture di file su disco + un paio di comandi git: nessuna scansione del monorepo.
"""

import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import emperator_hook as eh  # noqa: E402  (helpers condivisi: una sola implementazione)

LIBRO = os.path.join(eh.ROOT, ".claude", "agents", "emperator.md")


def marcatore_path(sessione=""):
    """File-spia che dice all'hook per messaggio se IL LIBRO E' ARRIVATO IN QUESTA SESSIONE.

    Vive nella cartella temporanea di sistema, MAI nel repo: non deve sporcare git
    ne' finire in un push (ADR-013, e la ferita di B-008).

    LA CHIAVE DI SESSIONE E' OBBLIGATORIA, ed e' una correzione pagata: nella prima
    versione (2026-09-03) il file era uno solo per repo. Risultato misurato lo stesso
    giorno: una chat aperta PRIMA che il caricamento esistesse si vedeva scritto
    "dottrina caricata" perche' un'altra sessione (o una prova) aveva scritto il file.
    Un successo dichiarato e non verificato — esattamente cio' che la Legge Suprema
    vieta. Adesso ogni sessione ha il suo file e nessuno risponde per gli altri.
    """
    import hashlib
    import tempfile
    # normcase PRIMA dell'impronta: su Windows lo stesso percorso arriva ora come
    # "C:\..." ora come "c:\..." a seconda di chi lancia il processo, e due impronte
    # diverse per la STESSA cartella facevano cercare all'hook un file-spia che non
    # esisteva -> "NON RISULTA CARICATA" falso -> potere 60% falso e rilettura inutile
    # di 73.000 caratteri a spese di Max. Misurato il 2026-09-04: a1ed15b24c vs 23b0de640a.
    firma = hashlib.md5(os.path.normcase(eh.ROOT).encode("utf-8", "replace")).hexdigest()[:10]
    sess = "".join(c for c in str(sessione) if c.isalnum() or c in "-_")[:64] or "senza-sessione"
    return os.path.join(tempfile.gettempdir(), "emperator-boot-%s-%s.json" % (firma, sess))


def scrivi_marcatore(caratteri, sessione=""):
    try:
        import datetime
        with io.open(marcatore_path(sessione), "w", encoding="utf-8") as f:
            json.dump({
                "quando": datetime.datetime.now().isoformat(timespec="seconds"),
                "caratteri": caratteri,
                "libro": LIBRO,
                # Contatore delle sveglie dall'ultimo caricamento. Serve alla rilettura
                # periodica: il libro caricato all'apertura si allontana man mano che la
                # conversazione cresce, e a un certo punto va riaperto (dottrina 6.14).
                "sveglie": 0,
            }, f)
    except Exception:
        pass


def leggi_libro():
    try:
        with io.open(LIBRO, encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""


TESTATA = """\
=== EMPERATOR — DOTTRINA INTEGRALE CARICATA (apertura della sessione) ===

Da questo momento, e per TUTTA questa sessione, TU SEI EMPERATOR.
Non Claude. Non un assistente. EMPERATOR: il direttore di Digital Empire, che sta
sopra ogni reparto, ogni ecosistema, ogni agente.

CHI HAI DAVANTI: __PERSONA__. Ti rivolgi a __PERSONA__ per nome, sempre.
  Max e' il PROPRIETARIO dell'Impero e resta lui a decidere, chiunque ti stia parlando.
  Ma l'interlocutore di ADESSO e' __PERSONA__, e le regole di tono, misura e verita'
  valgono identiche verso di lui. Non reciti un personaggio scritto per un altro:
  sei Emperator davvero, con chiunque ti chiami.

QUI SOTTO C'E' LA TUA DOTTRINA COMPLETA — il file `.claude/agents/emperator.md`,
integrale, non un riassunto. E' TE STESSO AL 100%. Vale per ogni messaggio di questa
sessione: non ti verra' ripetuta, perche' ripeterla trenta volte costerebbe a Max
dieci volte tanto senza aggiungere una virgola.

Se piu' avanti in questa conversazione non la vedi piu' (contesto compattato), il
promemoria per messaggio te lo dira': allora la riapri e la rileggi, subito, prima
di rispondere. Non si lavora a memoria su cio' che si puo' leggere.

--------------------------------------------------------------------------------
"""

CODA = """
--------------------------------------------------------------------------------
FINE DELLA DOTTRINA INTEGRALE.

Da qui in avanti, ad ogni messaggio che pronuncia il tuo nome, ricevi solo una sveglia
corta con la fotografia aggiornata dell'Impero. La dottrina e' questa, quella qui sopra,
e resta valida per tutta la sessione.
"""


def riletto(sessione):
    """Azzera il contatore: il libro e' stato riaperto e riletto ADESSO.

    Lo invoca Emperator stesso dopo una rilettura (il comando esatto glielo passa la
    sveglia, gia' compilato col session_id). Serve perche' il potere torni a 100 su una
    misura vera — un contatore azzerato senza aver letto sarebbe una bugia, e le bugie
    sui numeri sono la cosa che la Legge Suprema vieta (dottrina §3).
    """
    libro = leggi_libro()
    scrivi_marcatore(len(libro), sessione)
    print("EMPERATOR: rilettura registrata — potere 100%%, %d caratteri." % len(libro))
    return 0


def main():
    # Claude Code passa session_id nel payload del hook. Senza, si ricade su una
    # chiave generica: meglio un segnale grezzo che nessun segnale.
    sessione = ""
    try:
        grezzo = sys.stdin.buffer.read().decode("utf-8", "replace")
        if grezzo:
            sessione = json.loads(grezzo).get("session_id") or ""
    except Exception:
        sessione = ""

    persona = eh.chi_parla()
    libro = leggi_libro()

    if not libro:
        # Guasto grave e DICHIARATO: senza il libro, Emperator non e' Emperator.
        # Si urla, non si tace: la finzione e' l'unica cosa vietata (dottrina §3).
        contesto = (
            "=== EMPERATOR — GUASTO ===\n"
            "Il file della dottrina non e' leggibile: %s\n"
            "NON sei caricato al 100%%. Dillo a %s prima di qualunque altra cosa e non\n"
            "fingere di avere la dottrina: senza quel file sei una sintesi di te stesso.\n"
            % (LIBRO, persona)
        )
        scrivi_marcatore(0, sessione)
    else:
        contesto = "%s%s%s\n%s\n%s" % (
            TESTATA.replace("__PERSONA__", persona),
            eh.oscura(libro, persona),
            CODA,
            eh.oscura(eh.ANCORAGGI, persona),
            eh.dottrina_riservata(persona).strip(),
        )
        scrivi_marcatore(len(libro), sessione)

    risposta = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": contesto,
        }
    }
    sys.stdout.buffer.write(json.dumps(risposta, ensure_ascii=False).encode("utf-8"))
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    try:
        # `--riletto <session_id>`: non e' un avvio di sessione, e' la registrazione
        # di una rilettura fatta a mano dentro la conversazione.
        if len(sys.argv) >= 2 and sys.argv[1] == "--riletto":
            sys.exit(riletto(sys.argv[2] if len(sys.argv) > 2 else ""))
        sys.exit(main())
    except Exception as exc:  # non si rompe MAI l'apertura della sessione
        eh._log_guasto(exc)
        sys.exit(0)
