"""
Test della consegna automatica. Gira OFFLINE:
nessuna chiave Stripe, nessuna rete, nessuna email spedita.

    python test_consegna.py

Non stampa emoji: l'output deve reggere la console Windows cp1252.
"""

import copy
import io
import json
import os
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)

import catalogo as cat  # noqa: E402

FALLITI = []
PASSATI = []


def ascii_safe(testo):
    """Rende stampabile qualunque testo su console cp1252 (emoji comprese)."""
    return str(testo).encode("ascii", "backslashreplace").decode("ascii")


def verifica(nome, condizione, dettaglio=""):
    if condizione:
        PASSATI.append(nome)
        print("  [OK]   %s" % nome)
    else:
        FALLITI.append(nome)
        print("  [FAIL] %s %s" % (nome, ascii_safe(dettaglio)))


def evento_sessione(**campi):
    """checkout.session.completed ridotta ai campi che il webhook legge davvero."""
    sessione = {
        "id": "cs_test_" + campi.pop("id", "0001"),
        "payment_status": "paid",
        "customer_details": {
            "email": campi.pop("email", "cliente@example.com"),
            "name": campi.pop("nome", "Giulia Rossi"),
        },
    }
    sessione.update(campi)
    return sessione


# --------------------------------------------------------------------------
# Riferimento storico: la email che il main.py originale (81 righe) spediva.
# Se questo blocco cambia, il prodotto vecchio non e' piu' identico a se stesso.
# --------------------------------------------------------------------------
LINK_48 = "https://esempio-download/48-leggi.pdf"
OGGETTO_48_ATTESO = u"Ecco il tuo manuale \U0001F4D6"
CORPO_48_ATTESO = (
    u"Ciao Giulia,\n"
    u"\n"
    u"grazie per l'acquisto — apprezzo davvero.\n"
    u"\n"
    u'Ecco il link per scaricare il tuo PDF de "Le 48 Leggi dei Maestri Dimenticati":\n'
    u"\n"
    + LINK_48 + u"\n"
    u"\n"
    u"Leggilo con calma, non è un libro da divorare tutto di un fiato — "
    u"ogni legge merita riflessione.\n"
    u"\n"
    u"Se hai domande o vuoi dirmi com'è andata, rispondi pure a questa email.\n"
    u"\n"
    u"Max"
)

LINK_MANUALE = "https://esempio-download/manuale-claude-code.pdf"


def main():
    print("=" * 70)
    print("TEST CONSEGNA AUTOMATICA -- offline, nessuna email spedita")
    print("=" * 70)

    catalogo_disco = cat.carica_catalogo()
    env_finto = {
        "EBOOK_DOWNLOAD_URL": LINK_48,
        "MANUALE_CC_DOWNLOAD_URL": LINK_MANUALE,
    }

    # ------------------------------------------------------------------
    print("\n[1] Catalogo")
    prodotti = catalogo_disco.get("prodotti", {})
    verifica("prodotti.json ha 48-leggi e manuale-claude-code",
             "48-leggi" in prodotti and "manuale-claude-code" in prodotti,
             str(list(prodotti)))
    crudo = io.open(cat.CATALOGO_PATH, encoding="utf-8").read()
    verifica("nessun link/segreto incollato nel catalogo",
             "http://" not in crudo and "https://" not in crudo and "sk_" not in crudo)
    verifica("ogni prodotto punta a una variabile .env per il download",
             all(p.get("download_env") for p in prodotti.values()))

    # ------------------------------------------------------------------
    print("\n[2] Evento 48 Leggi -- catalogo NON armato (situazione di oggi)")
    sess48 = evento_sessione(id="48leggi", nome="Giulia Rossi")
    chiave, motivo = cat.risolvi_prodotto(sess48, catalogo_disco, env=env_finto)
    verifica("risolve 48-leggi", chiave == "48-leggi", "ha risolto %s" % chiave)
    verifica("motivo = fallback condizionato", motivo == cat.VIA_FALLBACK, motivo)
    if chiave is None:
        print("\n  Risoluzione fallita: il resto del test non ha senso, mi fermo.")
        print("PASSATI: %d   FALLITI: %d\nESITO: FALLITO" % (len(PASSATI), len(FALLITI)))
        return 1

    oggetto, corpo = cat.componi_email(chiave, catalogo_disco, "Giulia Rossi", env=env_finto)
    verifica("oggetto identico a prima", oggetto == OGGETTO_48_ATTESO,
             "ottenuto=%s" % ascii_safe(oggetto))
    verifica("corpo identico a prima", corpo == CORPO_48_ATTESO,
             "\n--- ottenuto ---\n%s\n--- atteso ---\n%s"
             % (ascii_safe(corpo), ascii_safe(CORPO_48_ATTESO)))
    verifica("il link del corpo viene dal .env", LINK_48 in corpo)

    # ------------------------------------------------------------------
    print("\n[3] Evento Manuale Claude Code -- via Payment Link (catalogo armato)")
    armato = copy.deepcopy(catalogo_disco)
    armato["prodotti"]["manuale-claude-code"]["riconoscimento"]["payment_link_ids"] = [
        "plink_TEST_MANUALE"
    ]
    armato["prodotti"]["48-leggi"]["riconoscimento"]["payment_link_ids"] = ["plink_TEST_48"]

    sessM = evento_sessione(id="manuale", nome="Luca Bianchi",
                            payment_link="plink_TEST_MANUALE")
    chiave, motivo = cat.risolvi_prodotto(sessM, armato, env=env_finto)
    verifica("risolve manuale-claude-code", chiave == "manuale-claude-code",
             "ha risolto %s" % chiave)
    verifica("motivo = payment_link", motivo == cat.VIA_PAYMENT_LINK, motivo)

    oggetto_m, corpo_m = cat.componi_email(chiave, armato, "Luca Bianchi", env=env_finto)
    verifica("oggetto del Manuale", oggetto_m == "Il tuo Manuale Claude Code",
             ascii_safe(oggetto_m))
    verifica("il corpo saluta Luca", corpo_m.startswith("Ciao Luca,"),
             ascii_safe(corpo_m[:30]))
    verifica("il corpo porta il link del Manuale", LINK_MANUALE in corpo_m)
    verifica("il Manuale non nomina le 48 Leggi", "48 Leggi" not in corpo_m)

    # ------------------------------------------------------------------
    print("\n[4] Evento Manuale -- via metadata (criterio piu' esplicito)")
    sessMeta = evento_sessione(id="meta", metadata={"prodotto": "manuale-claude-code"})
    chiave, motivo = cat.risolvi_prodotto(sessMeta, armato, env=env_finto)
    verifica("metadata vince e risolve il Manuale",
             chiave == "manuale-claude-code" and motivo == cat.VIA_METADATA,
             "%s / %s" % (chiave, motivo))

    sessPrice = evento_sessione(id="price", line_items={
        "data": [{"price": {"id": "price_TEST_MANUALE"}}]})
    armato["prodotti"]["manuale-claude-code"]["riconoscimento"]["price_ids"] = [
        "price_TEST_MANUALE"]
    chiave, motivo = cat.risolvi_prodotto(sessPrice, armato, env=env_finto)
    verifica("price id risolve il Manuale quando i line_items sono nel payload",
             chiave == "manuale-claude-code" and motivo == cat.VIA_PRICE_ID,
             "%s / %s" % (chiave, motivo))

    # ------------------------------------------------------------------
    print("\n[5] Sicurezza -- sessione ambigua a catalogo armato: NON si consegna")
    sessIgnota = evento_sessione(id="ignota", payment_link="plink_MAI_VISTO")
    chiave, motivo = cat.risolvi_prodotto(sessIgnota, armato, env=env_finto)
    verifica("nessun prodotto scelto", chiave is None, "ha risolto %s" % chiave)
    verifica("motivo = PRODOTTO_NON_RICONOSCIUTO", motivo == cat.NON_RISOLTO, motivo)

    chiave, motivo = cat.risolvi_prodotto(
        sess48, catalogo_disco, env=dict(env_finto, FALLBACK_PRODUCT_KEY="none"))
    verifica("FALLBACK_PRODUCT_KEY=none spegne del tutto il fallback",
             chiave is None, "ha risolto %s" % chiave)

    # Il rischio vero: si arma il Manuale e ci si dimentica delle 48 Leggi.
    mezzo = copy.deepcopy(catalogo_disco)
    mezzo["prodotti"]["manuale-claude-code"]["riconoscimento"]["payment_link_ids"] = [
        "plink_TEST_MANUALE"]
    chiave, motivo = cat.risolvi_prodotto(sess48, mezzo, env=env_finto)
    verifica("armato solo il Manuale: le 48 Leggi non partono piu' alla cieca",
             chiave is None and motivo == cat.NON_RISOLTO, "%s / %s" % (chiave, motivo))

    # ------------------------------------------------------------------
    print("\n[6] Log dei fallimenti")
    tmp = os.path.join(tempfile.gettempdir(), "test-consegne-fallite.log")
    if os.path.exists(tmp):
        os.remove(tmp)
    cat.logga_fallimento(cat.NON_RISOLTO, "cliente@example.com",
                         dettaglio="payment_link=plink_MAI_VISTO",
                         session_id="cs_test_ignota", path=tmp)
    cat.logga_fallimento("INVIO_FALLITO", "cliente@example.com", "48-leggi",
                         dettaglio="SMTPAuthenticationError", path=tmp)
    righe = io.open(tmp, encoding="utf-8").read().strip().split("\n")
    verifica("due righe scritte in append", len(righe) == 2, str(len(righe)))
    verifica("la riga porta data, email, prodotto ed errore",
             "cliente@example.com" in righe[1] and "48-leggi" in righe[1]
             and "SMTPAuthenticationError" in righe[1], ascii_safe(righe[1]))
    os.remove(tmp)

    # ------------------------------------------------------------------
    print("\n[7] Casi limite")
    verifica("nome vuoto -> 'ciao' (resa originale)", cat.primo_nome("") == "ciao")
    verifica("nome di soli spazi non esplode piu'", cat.primo_nome("   ") == "ciao")
    try:
        cat.componi_email("48-leggi", catalogo_disco, "Giulia", env={})
        verifica("link mancante -> errore parlante", False, "non ha sollevato")
    except ValueError as e:
        verifica("link mancante -> errore parlante",
                 "EBOOK_DOWNLOAD_URL" in str(e), str(e))

    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("PASSATI: %d   FALLITI: %d" % (len(PASSATI), len(FALLITI)))
    if FALLITI:
        for nome in FALLITI:
            print("  - %s" % nome)
        print("ESITO: FALLITO")
        return 1
    print("ESITO: TUTTO VERDE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
