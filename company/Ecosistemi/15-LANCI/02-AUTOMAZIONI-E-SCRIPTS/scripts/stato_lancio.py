# -*- coding: utf-8 -*-
"""La macchina a stati di un lancio. Il pezzo centrale dell'ecosistema 15-LANCI.

COS'E' E COSA NON E'. Non e' un motore di orchestrazione, ed e' una scelta
registrata (decisione 5 di ADR-025): il motore canonico ha un tetto di sei
attivita' per piano, cinque nomi di ruolo e non sa chiamare un modello. Qui serve
un'altra cosa, piu' piccola e piu' noiosa:

    leggere un file -> validarlo contro il suo schema -> decidere se si passa
    -> scrivere un verbale

Questo modulo copre lo scaglione **S2a** (micro-task MT-XV6Y): creare, leggere,
elencare, e caricare/validare gli artefatti. Il comando `avanza` con i gate e'
S2b (MT-3XWC) e non sta qui.

DUE REGOLE CHE VALGONO PER TUTTO IL FILE

1. **Un artefatto e' valido solo contro il proprio schema, RICALCOLATO.** Mai
   fidarsi di un campo salvato che dice "valido": un file marcato buono e poi
   modificato a mano resterebbe buono per sempre.

2. **Il lock e' esclusivo e su file.** Due sessioni sullo stesso lancio non si
   sovrascrivono. E' la stessa lezione di B-009 sui checkpoint: la mutua
   esclusione e' un fatto del filesystem, non una buona intenzione.
"""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone

# Percorsi ------------------------------------------------------------------
QUI = os.path.dirname(os.path.abspath(__file__))
ECOSISTEMA = os.path.dirname(os.path.dirname(QUI))
LANCI = os.path.join(ECOSISTEMA, "lanci")
RADICE = os.path.dirname(os.path.dirname(os.path.dirname(ECOSISTEMA)))
SCHEMI = os.path.join(RADICE, "PIANO-MAESTRO", "29-ECOSISTEMA-LANCI", "dati", "schemi")
REGISTRO = os.path.join(RADICE, "PIANO-MAESTRO", "29-ECOSISTEMA-LANCI", "dati", "registro.yaml")

# Stato iniziale e artefatti -------------------------------------------------
STATO_INIZIALE = "IDEA"

# artefatto atteso -> schema che lo valida. La chiave e' il nome del file dentro
# la cartella del lancio; il valore e' lo schema nel pacchetto di piano.
ARTEFATTI = {
    "pubblico.json": "pubblico.schema.json",
    "decisione.json": "decisione.schema.json",
    "certificato.json": "certificato.schema.json",
    "ricerca.json": "ricerca.schema.json",
    "previsione.json": "previsione.schema.json",
    "offerta.json": "offerta.schema.json",
    "funnel.json": "funnel.schema.json",
    "editoriale.json": "editoriale.schema.json",
    "budget.json": "budget.schema.json",
    "apertura.json": "apertura.schema.json",
    "consuntivo.json": "consuntivo.schema.json",
    "debrief.json": "debrief.schema.json",
}


class ErroreLancio(Exception):
    """Qualcosa che l'utente puo' capire e correggere."""


# --------------------------------------------------------------------------
# Lock su file
# --------------------------------------------------------------------------

class Lock:
    """Lock esclusivo su un file, con attesa breve e messaggio utile.

    Perche' non un semplice `if os.path.exists`: fra il controllo e la creazione
    passa del tempo, e in quel tempo l'altra sessione vince. Qui si apre in
    modo esclusivo (`O_CREAT|O_EXCL`), che e' atomico, e si scrive dentro chi
    ha preso il lock e quando: un lock orfano deve poter essere capito, non solo
    trovato.
    """

    def __init__(self, percorso: str, attesa_massima_s: float = 5.0):
        self.percorso = percorso
        self.attesa_massima_s = attesa_massima_s
        self._fd = None

    def __enter__(self):
        scadenza = time.time() + self.attesa_massima_s
        while True:
            try:
                self._fd = os.open(self.percorso, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(self._fd, json.dumps({
                    "pid": os.getpid(),
                    "preso_il": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                }).encode("utf-8"))
                return self
            except FileExistsError:
                if time.time() >= scadenza:
                    raise ErroreLancio(
                        "Il lancio e' occupato da un'altra sessione.\n"
                        "  Lock: %s\n"
                        "  Se sei sicuro che nessuno ci stia lavorando, cancella quel file."
                        % self.percorso)
                time.sleep(0.1)

    def __exit__(self, *_):
        if self._fd is not None:
            os.close(self._fd)
            self._fd = None
        try:
            os.remove(self.percorso)
        except OSError:
            pass
        return False


# --------------------------------------------------------------------------
# Il lancio
# --------------------------------------------------------------------------

class Lancio:
    def __init__(self, slug: str):
        if not slug or not all(c.isalnum() or c in "-_" for c in slug):
            raise ErroreLancio(
                "Identificativo non valido: lettere, cifre, trattini (es. manuale-claude-code)")
        self.slug = slug
        self.dir = os.path.join(LANCI, slug)
        self.path_stato = os.path.join(self.dir, "stato.json")
        self.path_lock = os.path.join(self.dir, ".lock")
        self.dir_verbali = os.path.join(self.dir, "verbali")

    # -- esistenza ---------------------------------------------------------
    @property
    def esiste(self) -> bool:
        return os.path.exists(self.path_stato)

    def _esigi(self):
        if not self.esiste:
            raise ErroreLancio(
                "Lancio '%s' inesistente.\n  Cercato: %s\n  Crealo con:  lancio crea %s --prodotto \"...\""
                % (self.slug, self.path_stato, self.slug))

    # -- stato -------------------------------------------------------------
    def stato(self) -> dict:
        self._esigi()
        return json.load(open(self.path_stato, encoding="utf-8"))

    def _scrivi_stato(self, dati: dict):
        with open(self.path_stato, "w", encoding="utf-8", newline="\n") as f:
            json.dump(dati, f, ensure_ascii=False, indent=2)
            f.write("\n")

    def crea(self, prodotto: str) -> dict:
        if self.esiste:
            raise ErroreLancio(
                "Il lancio '%s' esiste gia' (stato: %s). Non lo sovrascrivo."
                % (self.slug, self.stato()["stato"]))
        os.makedirs(self.dir, exist_ok=True)
        os.makedirs(self.dir_verbali, exist_ok=True)
        adesso = datetime.now(timezone.utc).isoformat(timespec="seconds")
        dati = {
            "schema_version": "1.0.0",
            "lancio_id": self.slug,
            "prodotto": prodotto,
            "stato": STATO_INIZIALE,
            "creato_il": adesso,
            "cambiato_il": adesso,
            "stato_di_partenza": None,
            "storia": [
                {"da": None, "a": STATO_INIZIALE, "il": adesso, "perche": "creazione"}
            ],
        }
        with Lock(self.path_lock):
            self._scrivi_stato(dati)
        self.verbale("creazione", {"prodotto": prodotto, "stato": STATO_INIZIALE})
        return dati

    # -- verbali -----------------------------------------------------------
    def verbale(self, tipo: str, corpo: dict) -> str:
        """Un verbale per ogni cosa che succede, anche quando NON succede.

        Un sistema che scrive solo i successi non ha una storia: ha una vetrina.
        """
        os.makedirs(self.dir_verbali, exist_ok=True)
        adesso = datetime.now(timezone.utc)
        nome = "%s-%s.json" % (adesso.strftime("%Y%m%dT%H%M%S"), tipo)
        percorso = os.path.join(self.dir_verbali, nome)
        with open(percorso, "w", encoding="utf-8", newline="\n") as f:
            json.dump({"tipo": tipo, "il": adesso.isoformat(timespec="seconds"),
                       **corpo}, f, ensure_ascii=False, indent=2)
            f.write("\n")
        return percorso

    # -- artefatti ---------------------------------------------------------
    def artefatti_presenti(self) -> dict:
        """{nome: percorso} per i soli artefatti che esistono davvero sul disco.

        Un file `<nome>.PROPOSTA.json` NON conta come artefatto: e' una proposta,
        e trattarla come artefatto e' esattamente il modo in cui un prezzo non
        firmato finisce per sembrare firmato.
        """
        if not os.path.isdir(self.dir):
            return {}
        return {n: os.path.join(self.dir, n)
                for n in ARTEFATTI if os.path.exists(os.path.join(self.dir, n))}

    def valida_artefatto(self, nome: str) -> list[str]:
        """Ricalcola la validita' contro lo schema. Ritorna la lista dei problemi.

        RICALCOLATA, sempre: non esiste un campo salvato che dica 'questo e' a
        posto'. Un file marcato buono e poi modificato a mano resterebbe buono
        per sempre, ed e' il modo piu' silenzioso di far passare un gate.
        """
        if nome not in ARTEFATTI:
            raise ErroreLancio("Artefatto sconosciuto: %s" % nome)
        percorso = os.path.join(self.dir, nome)
        if not os.path.exists(percorso):
            return ["assente"]

        try:
            import jsonschema
        except ImportError:
            raise ErroreLancio("Manca jsonschema:  py -3 -m pip install jsonschema")

        percorso_schema = os.path.join(SCHEMI, ARTEFATTI[nome])
        if not os.path.exists(percorso_schema):
            return ["schema mancante: %s" % percorso_schema]

        try:
            dati = json.load(open(percorso, encoding="utf-8"))
        except json.JSONDecodeError as e:
            return ["JSON non leggibile: %s" % e]

        # le chiavi di servizio non fanno parte dell'artefatto
        if isinstance(dati, dict):
            dati = {k: v for k, v in dati.items() if not k.startswith("_")}

        schema = json.load(open(percorso_schema, encoding="utf-8"))
        problemi = []
        for e in sorted(jsonschema.Draft202012Validator(schema).iter_errors(dati),
                        key=lambda x: list(x.absolute_path)):
            dove = ".".join(str(x) for x in e.absolute_path) or "(radice)"
            problemi.append("%s: %s" % (dove, e.message))
        return problemi

    def valida_tutti(self) -> dict:
        """{nome: [problemi]} per ogni artefatto presente. Vuoto = tutto valido."""
        return {n: self.valida_artefatto(n) for n in self.artefatti_presenti()}

    # -- lettura -----------------------------------------------------------
    def fermo_da_giorni(self) -> int:
        s = self.stato()
        cambiato = datetime.fromisoformat(s["cambiato_il"])
        if cambiato.tzinfo is None:
            cambiato = cambiato.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - cambiato).days


def elenca() -> list[Lancio]:
    if not os.path.isdir(LANCI):
        return []
    return [Lancio(d) for d in sorted(os.listdir(LANCI))
            if os.path.exists(os.path.join(LANCI, d, "stato.json"))]
