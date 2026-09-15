# -*- coding: utf-8 -*-
"""Il contratto che ogni controllo (gate) di 15-LANCI rispetta. Scritto UNA volta, qui.

Un gate e' un modulo `gate_<sigla>_<n>.py` in questa cartella che espone:

    ID = "GATE-PUB-1"                 # lo stesso id del registro
    ARTEFATTO = "pubblico.json"       # il file che presidia (relativo alla cartella del lancio)
    def esegui(dir_lancio: str, rete: "Rete") -> Verdetto

Tre regole, che valgono per tutti i gate e che il motore (`stato_lancio.avanza`) da' per
scontate:

1. **Ricalcolo, mai fiducia.** Il gate legge i FILE e rifa' il conto. Non legge mai un campo
   dello stato che dice "passato": quello lo scrive il motore DOPO il verdetto, per comodita'
   di lettura, e non e' una fonte (documento 01 §2.3).
2. **Il mondo esterno passa da `Rete`.** Un gate che deve aprire un link (GATE-PRD-1, GATE-INT-1,
   GATE-FNL-1) lo fa attraverso l'oggetto `rete` che riceve, mai con urllib diretto: cosi' nei
   test si inietta `ReteFinta` e il gate resta deterministico, e in produzione `ReteVera` fa la
   chiamata vera. Un gate che nei test "passa" perche' finge la rete dentro di se' e' un gate
   finto (Legge Suprema, emperator.md §3).
3. **Il gate non scrive niente.** Ne' verbali, ne' stato, ne' artefatti. Ritorna un Verdetto e
   basta; a scrivere e' il motore (INV-09 applicato al codice, non solo all'agente lan-gate).
"""
from __future__ import annotations

import hashlib
import importlib
import json
import os
from dataclasses import dataclass, field

QUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(QUI)
ECOSISTEMA = os.path.dirname(os.path.dirname(SCRIPTS))
RADICE = os.path.dirname(os.path.dirname(os.path.dirname(ECOSISTEMA)))
DATI = os.path.join(RADICE, "PIANO-MAESTRO", "29-ECOSISTEMA-LANCI", "dati")
SCHEMI = os.path.join(DATI, "schemi")
REGISTRO = os.path.join(DATI, "registro.yaml")

# artefatto (file nel lancio) -> schema. Copia unica di quella in stato_lancio.ARTEFATTI:
# i gate non importano il motore per non creare un ciclo, il motore importa i gate.
ARTEFATTI = {
    "pubblico.json": "pubblico.schema.json",
    "decisione.json": "decisione.schema.json",
    "certificato.json": "certificato.schema.json",
    "ricerca.json": "ricerca.schema.json",
    "previsione.json": "previsione.schema.json",
    "offerta.json": "offerta.schema.json",
    "copy/manifest.json": "copy.schema.json",
    "funnel.json": "funnel.schema.json",
    "editoriale.json": "editoriale.schema.json",
    "budget.json": "budget.schema.json",
    "apertura.json": "apertura.schema.json",
    "consuntivo.json": "consuntivo.schema.json",
    "debrief.json": "debrief.schema.json",
}


class ErroreArtefatto(Exception):
    """Un artefatto illeggibile: il motore lo traduce in codice 2, senza scrivere nulla."""


@dataclass
class Verdetto:
    gate: str
    passa: bool
    problemi: list[str] = field(default_factory=list)   # vuoto se passa
    dati: dict = field(default_factory=dict)             # i numeri misurati per decidere
    ramo_fallimento: str | None = None                   # stato di destinazione se boccia

    def come_dict(self) -> dict:
        return {"gate": self.gate, "passa": self.passa, "problemi": list(self.problemi),
                "dati": dict(self.dati), "ramo_fallimento": self.ramo_fallimento}


# --------------------------------------------------------------------------
# Rete: il confine col mondo esterno
# --------------------------------------------------------------------------

class Rete:
    """Interfaccia. `codice_http` ritorna il codice (200, 404, ...) oppure None se
    la chiamata non e' riuscita (DNS, timeout). `testo` ritorna il corpo o None."""

    def codice_http(self, url: str, timeout: float = 10.0) -> int | None:
        raise NotImplementedError

    def testo(self, url: str, timeout: float = 10.0) -> str | None:
        raise NotImplementedError


class ReteVera(Rete):
    def _apri(self, url, timeout):
        import urllib.request
        import urllib.error
        req = urllib.request.Request(url, headers={"User-Agent": "DigitalEmpire-LANCI/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(200_000).decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            return e.code, None
        except Exception:  # noqa: BLE001 — DNS, timeout, TLS: per il gate e' "non raggiungibile"
            return None, None

    def codice_http(self, url, timeout=10.0):
        return self._apri(url, timeout)[0]

    def testo(self, url, timeout=10.0):
        return self._apri(url, timeout)[1]


class ReteFinta(Rete):
    """SOLO per i test. `risposte` = {url: codice} oppure {url: (codice, testo)}.
    Un url non presente risponde None (irraggiungibile): il default e' il fallimento,
    cosi' un test che dimentica un url non passa per sbaglio."""

    def __init__(self, risposte: dict | None = None):
        self.risposte = dict(risposte or {})
        self.chiamate: list[str] = []

    def _r(self, url):
        self.chiamate.append(url)
        v = self.risposte.get(url)
        if v is None:
            return None, None
        if isinstance(v, tuple):
            return v[0], v[1]
        return v, ""

    def codice_http(self, url, timeout=10.0):
        return self._r(url)[0]

    def testo(self, url, timeout=10.0):
        return self._r(url)[1]


# --------------------------------------------------------------------------
# Lettura e validazione degli artefatti
# --------------------------------------------------------------------------

def percorso_artefatto(dir_lancio: str, nome: str) -> str:
    return os.path.join(dir_lancio, *nome.split("/"))


def leggi_artefatto(dir_lancio: str, nome: str) -> dict | None:
    """None se assente. ErroreArtefatto se il JSON e' rotto. Le chiavi che iniziano
    con `_` sono di servizio e vengono tolte."""
    p = percorso_artefatto(dir_lancio, nome)
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding="utf-8") as f:
            dati = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        raise ErroreArtefatto("%s: JSON non leggibile: %s" % (nome, e))
    if isinstance(dati, dict):
        dati = {k: v for k, v in dati.items() if not k.startswith("_")}
    return dati


def valida_contro_schema(dir_lancio: str, nome: str) -> list[str]:
    """Ricalcola la validita' contro lo schema. ['assente'] se il file non c'e'."""
    if nome not in ARTEFATTI:
        return ["artefatto sconosciuto: %s" % nome]
    dati = leggi_artefatto(dir_lancio, nome)
    if dati is None:
        return ["assente"]
    import jsonschema
    schema_p = os.path.join(SCHEMI, ARTEFATTI[nome])
    if not os.path.exists(schema_p):
        return ["schema mancante: %s" % schema_p]
    with open(schema_p, encoding="utf-8") as f:
        schema = json.load(f)
    problemi = []
    for e in sorted(jsonschema.Draft202012Validator(schema).iter_errors(dati),
                    key=lambda x: list(x.absolute_path)):
        dove = ".".join(str(x) for x in e.absolute_path) or "(radice)"
        problemi.append("%s: %s" % (dove, e.message))
    return problemi


def sha256_file(percorso: str) -> str:
    h = hashlib.sha256()
    with open(percorso, "rb") as f:
        for blocco in iter(lambda: f.read(65536), b""):
            h.update(blocco)
    return h.hexdigest()


# --------------------------------------------------------------------------
# Il registro (fonte di verita') e la scoperta dei gate
# --------------------------------------------------------------------------

_REGISTRO_CACHE: dict | None = None


def registro() -> dict:
    global _REGISTRO_CACHE
    if _REGISTRO_CACHE is None:
        import yaml
        with open(REGISTRO, encoding="utf-8") as f:
            _REGISTRO_CACHE = yaml.safe_load(f)
    return _REGISTRO_CACHE


def voce_gate(gate_id: str) -> dict | None:
    for g in registro()["gate"]:
        if g["id"] == gate_id:
            return g
    return None


def nome_modulo(gate_id: str) -> str:
    """GATE-PUB-1 -> gate_pub_1"""
    return gate_id.lower().replace("-", "_")


def trova_gate(gate_id: str):
    """Il modulo del gate, o None se non e' ancora costruito. Il motore, davanti a None,
    esce 3 e lo dice ("controllo non costruito"), non finge di averlo eseguito."""
    try:
        return importlib.import_module("scripts.gates." + nome_modulo(gate_id))
    except ModuleNotFoundError as e:
        if e.name and e.name.endswith(nome_modulo(gate_id)):
            return None
        raise


def esegui_gate(gate_id: str, dir_lancio: str, rete: Rete | None = None) -> Verdetto:
    """Esegue un gate per id. Se il modulo manca, ritorna un Verdetto che NON passa con
    problema 'controllo non costruito' e ramo_fallimento None: e' il motore a decidere
    che quello e' codice 3, non 1."""
    mod = trova_gate(gate_id)
    if mod is None:
        return Verdetto(gate=gate_id, passa=False,
                        problemi=["controllo non costruito: manca scripts/gates/%s.py"
                                  % nome_modulo(gate_id)],
                        ramo_fallimento=None)
    v = mod.esegui(dir_lancio, rete if rete is not None else ReteVera())
    if v.ramo_fallimento is None and not v.passa:
        # Lo STATO di destinazione (artefatti[].se_fallisce), non la prosa del gate:
        # il motore ha bisogno di uno stato da applicare, non di una frase.
        v.ramo_fallimento = stato_se_fallisce(gate_id)
    return v


def stato_se_fallisce(gate_id: str) -> str | None:
    voce = voce_gate(gate_id)
    if not voce:
        return None
    for a in registro()["artefatti"]:
        if a["id"] == voce.get("presidia"):
            return a.get("se_fallisce")
    return None


def gate_costruiti() -> list[str]:
    ids = []
    for g in registro()["gate"]:
        if trova_gate(g["id"]) is not None:
            ids.append(g["id"])
    return ids
