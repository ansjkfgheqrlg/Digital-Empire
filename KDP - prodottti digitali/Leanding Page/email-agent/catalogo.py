"""
Catalogo prodotti e risoluzione della consegna.

Modulo puro: nessuna rete, nessun invio email, nessun import di FastAPI o Stripe.
Serve a due padroni: main.py (produzione) e test_consegna.py (offline).

REGOLA DI SICUREZZA: meglio non consegnare che consegnare il prodotto sbagliato.
Se la sessione Stripe non porta un identificatore che punta a UN solo prodotto,
la consegna non parte e l'evento finisce in consegne-fallite.log.
"""

import io
import json
import os
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
CATALOGO_PATH = os.path.join(QUI, "prodotti.json")
LOG_FALLIMENTI = os.path.join(QUI, "consegne-fallite.log")

# Motivi di risoluzione (stringhe stabili: le legge il test e le scrive il log)
VIA_METADATA = "metadata.prodotto"
VIA_PAYMENT_LINK = "payment_link"
VIA_PRICE_ID = "price_id"
VIA_FALLBACK = "fallback-catalogo-non-armato"
NON_RISOLTO = "PRODOTTO_NON_RICONOSCIUTO"


# --------------------------------------------------------------------------
# Catalogo
# --------------------------------------------------------------------------

def carica_catalogo(path=None):
    """Legge prodotti.json. UTF-8 esplicito: il catalogo contiene accenti ed emoji."""
    with io.open(path or CATALOGO_PATH, encoding="utf-8") as f:
        return json.load(f)


def _norm(valore):
    return str(valore).strip().lower() if valore is not None else ""


def _riconoscimento(prodotto):
    return prodotto.get("riconoscimento") or {}


def prodotti_armati(catalogo):
    """
    Chiavi dei prodotti che hanno un identificatore REALE di Stripe configurato:
    un payment link id o un price id, cioe' i codici che Max incolla dalla
    dashboard quando accende un rail.

    Gli alias 'metadata_prodotto' NON contano: sono nomi naturali che viaggiano
    sull'evento, non uno stato del catalogo.

    Serve alla regola del fallback: finche' NESSUN rail e' armato esiste di fatto
    un solo prodotto vendibile e sbagliare consegna e' impossibile. Appena Max
    arma il primo rail l'ambiguita' diventa reale e il fallback si spegne da solo
    -- percio' quando si arma un prodotto vanno armati TUTTI (vedi LEGGIMI).
    """
    armati = []
    for chiave, prodotto in catalogo.get("prodotti", {}).items():
        r = _riconoscimento(prodotto)
        if r.get("payment_link_ids") or r.get("price_ids"):
            armati.append(chiave)
    return armati


# --------------------------------------------------------------------------
# Lettura dell'evento Stripe (nessuna chiamata di rete)
# --------------------------------------------------------------------------

def identificatori_sessione(session):
    """
    Estrae dalla checkout.session TUTTO cio' che puo' identificare il prodotto,
    senza mai chiamare l'API Stripe.

    - metadata.prodotto (o 'product' / 'prodotto_key'): il piu' esplicito
    - payment_link: stringa 'plink_...' oppure dict espanso {'id': 'plink_...'}
    - price ids: solo se i line_items sono gia' dentro il payload (non li andiamo
      a cercare: espanderli costerebbe una chiamata di rete dentro il webhook)
    """
    session = session or {}

    metadata = session.get("metadata") or {}
    meta_prodotto = ""
    for campo in ("prodotto", "product", "prodotto_key", "product_key"):
        if metadata.get(campo):
            meta_prodotto = _norm(metadata[campo])
            break

    plink = session.get("payment_link")
    if isinstance(plink, dict):
        plink = plink.get("id")
    plink = _norm(plink)

    price_ids = []
    line_items = session.get("line_items") or {}
    for riga in (line_items.get("data") or []):
        prezzo = riga.get("price") or {}
        pid = prezzo.get("id") if isinstance(prezzo, dict) else prezzo
        if pid:
            price_ids.append(_norm(pid))

    return {
        "metadata_prodotto": meta_prodotto,
        "payment_link": plink,
        "price_ids": price_ids,
    }


def risolvi_prodotto(session, catalogo, env=None):
    """
    Ritorna (chiave_prodotto | None, motivo).

    Ordine: metadata -> payment_link -> price_id -> fallback condizionato.
    Nessun criterio basato sull'importo pagato: due prodotti possono costare uguale.
    """
    env = os.environ if env is None else env
    ids = identificatori_sessione(session)
    prodotti = catalogo.get("prodotti", {})

    # 1) metadata.prodotto: accetta sia la chiave del catalogo sia gli alias
    if ids["metadata_prodotto"]:
        for chiave, prodotto in prodotti.items():
            alias = [_norm(a) for a in _riconoscimento(prodotto).get("metadata_prodotto", [])]
            if ids["metadata_prodotto"] == _norm(chiave) or ids["metadata_prodotto"] in alias:
                return chiave, VIA_METADATA

    # 2) id del Payment Link
    if ids["payment_link"]:
        for chiave, prodotto in prodotti.items():
            noti = [_norm(p) for p in _riconoscimento(prodotto).get("payment_link_ids", [])]
            if ids["payment_link"] in noti:
                return chiave, VIA_PAYMENT_LINK

    # 3) price id (solo se i line_items erano gia' nel payload)
    if ids["price_ids"]:
        for chiave, prodotto in prodotti.items():
            noti = [_norm(p) for p in _riconoscimento(prodotto).get("price_ids", [])]
            if any(pid in noti for pid in ids["price_ids"]):
                return chiave, VIA_PRICE_ID

    # 4) fallback CONDIZIONATO: vale solo finche' il catalogo non e' armato
    forzata = _norm(env.get("FALLBACK_PRODUCT_KEY", ""))
    if forzata in ("none", "nessuno", "off"):
        return None, NON_RISOLTO

    chiave_fallback = forzata or next(
        (k for k, p in prodotti.items() if p.get("fallback")), None
    )
    if chiave_fallback and chiave_fallback in prodotti and not prodotti_armati(catalogo):
        return chiave_fallback, VIA_FALLBACK

    return None, NON_RISOLTO


# --------------------------------------------------------------------------
# Composizione della email
# --------------------------------------------------------------------------

def primo_nome(customer_name):
    """
    Stessa resa del codice originale ("ciao" quando il nome manca), ma senza
    l'IndexError che il codice originale aveva su un nome fatto di soli spazi.
    """
    if customer_name:
        pezzi = str(customer_name).split()
        if pezzi:
            return pezzi[0]
    return "ciao"


def link_prodotto(chiave, catalogo, env=None):
    """Il link di download vive SOLO nel .env. Qui si legge il nome della variabile."""
    env = os.environ if env is None else env
    prodotto = catalogo.get("prodotti", {}).get(chiave) or {}
    nome_var = prodotto.get("download_env")
    if not nome_var:
        return None
    return (env.get(nome_var) or "").strip() or None


def componi_email(chiave, catalogo, customer_name=None, link=None, env=None):
    """Ritorna (oggetto, corpo). Solleva ValueError se il link di download manca."""
    prodotto = catalogo.get("prodotti", {}).get(chiave)
    if not prodotto:
        raise ValueError("Prodotto '%s' assente dal catalogo" % chiave)

    url = link if link is not None else link_prodotto(chiave, catalogo, env)
    if not url:
        raise ValueError(
            "Link di download mancante per '%s': valorizza %s nel .env"
            % (chiave, prodotto.get("download_env", "?"))
        )

    corpo = prodotto["corpo"].replace("{nome}", primo_nome(customer_name)).replace("{link}", url)
    return prodotto["oggetto"], corpo


# --------------------------------------------------------------------------
# Log dei fallimenti (append, una riga per evento)
# --------------------------------------------------------------------------

def logga_fallimento(motivo, customer_email=None, prodotto=None, dettaglio=None,
                     session_id=None, path=None):
    """
    Scrive una riga in consegne-fallite.log cosi' che una consegna mancata si
    possa rifare a mano. Non solleva mai: un log rotto non deve mangiare l'evento.
    """
    riga = " | ".join([
        datetime.now().isoformat(timespec="seconds"),
        str(motivo or "-"),
        str(customer_email or "-"),
        str(prodotto or "-"),
        str(session_id or "-"),
        str(dettaglio or "-").replace("\n", " "),
    ])
    try:
        with io.open(path or LOG_FALLIMENTI, "a", encoding="utf-8") as f:
            f.write(riga + "\n")
    except Exception as e:  # pragma: no cover
        print("[ATTENZIONE] Log fallimenti non scrivibile: %s" % e)
    return riga
