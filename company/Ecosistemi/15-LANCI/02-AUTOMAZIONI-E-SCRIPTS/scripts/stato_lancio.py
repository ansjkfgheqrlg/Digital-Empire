# -*- coding: utf-8 -*-
"""La macchina a stati di un lancio. Il pezzo centrale dell'ecosistema 15-LANCI.

COS'E' E COSA NON E'. Non e' un motore di orchestrazione, ed e' una scelta
registrata (decisione 5 di ADR-025): il motore canonico ha un tetto di sei
attivita' per piano, cinque nomi di ruolo e non sa chiamare un modello. Qui serve
un'altra cosa, piu' piccola e piu' noiosa:

    leggere un file -> validarlo contro il suo schema -> decidere se si passa
    -> scrivere un verbale

Questo modulo copre lo scaglione **S2a** (micro-task MT-XV6Y): creare, leggere,
elencare, e caricare/validare gli artefatti; e lo scaglione **S2b** (MT-3XWC):
`avanza` con i gate, i comandi umani (`sospendi`, `riprendi`, `abbandona`,
`firma`, `via_libera`) e i punti umani. Il contratto dei campi e' in
`CONTRATTO-STATO.md`, che e' legge; il registro decide sopra tutto.

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
import shutil
import time
from datetime import date, datetime, timedelta, timezone

try:  # importato come pacchetto (python -m scripts.lancio, pytest)
    from .gates import _comune as gates
except ImportError:  # pragma: no cover - importato a mano da un altro cwd
    from scripts.gates import _comune as gates  # type: ignore

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
    "copy/manifest.json": "copy.schema.json",
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


    # ======================================================================
    # S2b (MT-3XWC): avanza, punti umani, comandi umani. Le costanti e le
    # funzioni di supporto stanno in fondo al modulo (si risolvono a runtime).
    # ======================================================================


    # -- stato completo e transizioni --------------------------------------
    def _stato_completo(self) -> dict:
        """Lo stato con i campi del contratto riempiti se mancano (mai errore)."""
        dati = self.stato()
        for k, v in CAMPI_DEFAULT.items():
            if k not in dati or (dati[k] is None and isinstance(v, (list, dict))):
                dati[k] = json.loads(json.dumps(v))
        return dati

    def _transizione(self, dati: dict, a: str, perche: str, scrivi: bool = True) -> None:
        da = dati["stato"]
        adesso = _iso(_adesso())
        dati["stato"] = a
        dati["cambiato_il"] = adesso
        dati["storia"].append({"da": da, "a": a, "il": adesso, "perche": perche})
        dati["bloccato_da"] = None
        print("  -> %s -> %s  (%s)" % (da, a, perche))
        if scrivi:
            self._scrivi_stato(dati)
            self.verbale("transizione", {"da": da, "a": a, "perche": perche})

    # -- verbali idempotenti -------------------------------------------------
    def verbale_idempotente(self, tipo: str, chiave: dict, corpo: dict) -> str:
        """Un verbale-evento che NON si duplica: se l'ultimo verbale dello stesso
        tipo ha la stessa `chiave`, si aggiorna `ultimo_controllo_il` invece di
        creare un file nuovo. Serve all'idempotenza di `avanza` (due giri
        identici, zero file nuovi) per i verbali `ambiente`."""
        os.makedirs(self.dir_verbali, exist_ok=True)
        candidati = sorted(n for n in os.listdir(self.dir_verbali)
                           if n.endswith("-%s.json" % tipo) or ("-%s-" % tipo) in n)
        for nome in reversed(candidati):
            p = os.path.join(self.dir_verbali, nome)
            try:
                vecchio = json.load(open(p, encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if vecchio.get("tipo") == tipo and all(vecchio.get(k) == v for k, v in chiave.items()):
                vecchio["ultimo_controllo_il"] = _iso(_adesso())
                with open(p, "w", encoding="utf-8", newline="\n") as f:
                    json.dump(vecchio, f, ensure_ascii=False, indent=2)
                    f.write("\n")
                return p
            break  # solo l'ultimo conta: un evento diverso in mezzo riapre la serie
        return self.verbale(tipo, {**chiave, **corpo, "ultimo_controllo_il": _iso(_adesso())})

    def _verbali_gate(self, gate_id: str) -> list[tuple[int, str]]:
        """[(tentativo, percorso)] dei verbali gate-<ID>-t<n>.json, in ordine."""
        if not os.path.isdir(self.dir_verbali):
            return []
        prefisso = "gate-%s-t" % gate_id
        trovati = []
        for n in os.listdir(self.dir_verbali):
            if n.startswith(prefisso) and n.endswith(".json"):
                try:
                    trovati.append((int(n[len(prefisso):-5]), os.path.join(self.dir_verbali, n)))
                except ValueError:
                    continue
        return sorted(trovati)

    def impronte_ingresso(self, gate_id: str) -> dict:
        """{file: sha256 | None} dell'artefatto presidiato e dei suoi ingressi."""
        nome = file_di_gate(gate_id)
        if not nome:
            return {}
        risultato = {}
        for f in [nome] + dipendenze_di_file(nome):
            p = os.path.join(self.dir, *f.split("/"))
            risultato[f] = gates.sha256_file(p) if os.path.exists(p) else None
        return risultato

    def verbale_gate(self, verdetto, ingresso: dict) -> tuple[str, int]:
        """Chiave (controllo, tentativo). Stesse impronte d'ingresso dell'ultimo
        verbale -> si aggiorna quello (ultimo_controllo_il); ingressi cambiati ->
        tentativo+1 e file nuovo."""
        os.makedirs(self.dir_verbali, exist_ok=True)
        adesso = _iso(_adesso())
        precedenti = self._verbali_gate(verdetto.gate)
        if precedenti:
            tentativo, percorso = precedenti[-1]
            try:
                vecchio = json.load(open(percorso, encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                vecchio = {}
            if vecchio.get("impronte_ingresso") == ingresso:
                vecchio.update({"passa": verdetto.passa, "problemi": list(verdetto.problemi),
                                "dati": dict(verdetto.dati),
                                "ramo_fallimento": verdetto.ramo_fallimento,
                                "ultimo_controllo_il": adesso})
                with open(percorso, "w", encoding="utf-8", newline="\n") as f:
                    json.dump(vecchio, f, ensure_ascii=False, indent=2)
                    f.write("\n")
                return percorso, tentativo
            tentativo += 1
        else:
            tentativo = 1
        percorso = os.path.join(self.dir_verbali, "gate-%s-t%d.json" % (verdetto.gate, tentativo))
        corpo = {"tipo": "gate", "gate": verdetto.gate, "tentativo": tentativo,
                 "passa": verdetto.passa, "problemi": list(verdetto.problemi),
                 "dati": dict(verdetto.dati), "ramo_fallimento": verdetto.ramo_fallimento,
                 "impronte_ingresso": ingresso, "il": adesso, "ultimo_controllo_il": adesso}
        with open(percorso, "w", encoding="utf-8", newline="\n") as f:
            json.dump(corpo, f, ensure_ascii=False, indent=2)
            f.write("\n")
        return percorso, tentativo

    # -- punti umani ---------------------------------------------------------
    def come_si_esce_da(self, pu_id: str) -> str:
        """SEMPRE un comando eseguibile, mai una descrizione."""
        return {
            "PU-PREZZO": "lancio firma %s --prezzo N --data gg/mm/aaaa" % self.slug,
            "PU-RUOLO": "lancio firma %s --prezzo N --data gg/mm/aaaa "
                        "--ruolo vendita|acquisizione-contatti" % self.slug,
            "PU-APERTURA": "lancio via-libera %s" % self.slug,
            "PU-SPESA": "lancio riprendi %s" % self.slug,
        }.get(pu_id, "lancio stato %s" % self.slug)

    def apri_punto_umano(self, dati: dict, pu_id: str) -> dict:
        """Idempotente: se e' gia' aperto ritorna quello (aperto_il non si azzera)."""
        for p in dati["punti_umani_aperti"]:
            if p["id"] == pu_id:
                return p
        voce = voce_punto_umano(pu_id) or {}
        adesso = _adesso()
        giorni = voce.get("scadenza_giorni")
        punto = {"id": pu_id, "aperto_il": _iso(adesso),
                 "scadenza_il": _iso(adesso + timedelta(days=giorni)) if giorni else None,
                 "domanda": voce.get("domanda", pu_id),
                 "come_si_esce": self.come_si_esce_da(pu_id)}
        dati["punti_umani_aperti"].append(punto)
        print("  punto umano aperto: %s — %s" % (pu_id, punto["domanda"]))
        print("     per uscirne:  %s" % punto["come_si_esce"])
        return punto

    def chiudi_punto_umano(self, dati: dict, pu_id: str) -> bool:
        prima = len(dati["punti_umani_aperti"])
        dati["punti_umani_aperti"] = [p for p in dati["punti_umani_aperti"] if p["id"] != pu_id]
        return len(dati["punti_umani_aperti"]) != prima

    def _leggi(self, nome: str):
        """Artefatto o proposta letti col lettore dei gate (ErroreArtefatto se rotto)."""
        return gates.leggi_artefatto(self.dir, nome)

    def _causa_sparita(self, dati: dict, pu_id: str) -> bool:
        if pu_id == "PU-PREZZO":
            off = self._leggi("offerta.json")
            return isinstance(off, dict) and isinstance(off.get("firma"), dict)
        if pu_id == "PU-RUOLO":
            if os.path.exists(os.path.join(self.dir, "offerta.json")):
                return True
            prop = self._leggi("offerta.PROPOSTA.json")
            return isinstance(prop, dict) and prop.get("ruolo_prodotto") in RUOLI_AMMESSI
        if pu_id == "PU-APERTURA":
            ape = self._leggi("apertura.json")
            return isinstance(ape, dict) and isinstance(ape.get("via_libera"), dict)
        return False

    def _applica_default(self, dati: dict, punto: dict, voce: dict, scrivi: bool) -> None:
        """PU con default scaduto: si procede col default, si marca scelto_per_silenzio."""
        default = voce["default"]
        if punto["id"] == "PU-RUOLO":
            p = os.path.join(self.dir, "offerta.PROPOSTA.json")
            if os.path.exists(p):
                prop = self._leggi("offerta.PROPOSTA.json")
                if isinstance(prop, dict):
                    prop["ruolo_prodotto"] = default
                    prop["ruolo_scelto_per_silenzio"] = True
                    prop["ruolo_revisione_il"] = (_adesso() + timedelta(days=7)).date().isoformat()
                    if scrivi:
                        with open(p, "w", encoding="utf-8", newline="\n") as f:
                            json.dump(prop, f, ensure_ascii=False, indent=2)
                            f.write("\n")
        self.chiudi_punto_umano(dati, punto["id"])
        print("  punto umano %s scaduto: si procede col default '%s' (scelto per silenzio)"
              % (punto["id"], default))
        if scrivi:
            self.verbale("punto-umano", {"punto": punto["id"], "esito": "default",
                                         "valore": default, "scelto_per_silenzio": True})

    def _sospendi_dati(self, dati: dict, motivo: str, revisione: date, scrivi: bool) -> None:
        adesso = _adesso()
        dati["sospensione"] = {
            "stato_di_partenza": dati["stato"],
            "dal": _iso(adesso),
            "revisione_il": _iso(datetime.combine(revisione, datetime.min.time(), timezone.utc)),
            "motivo": motivo,
            "come_si_esce": "lancio riprendi %s" % self.slug,
            "orologi_congelati": {p["id"]: p["scadenza_il"]
                                  for p in dati["punti_umani_aperti"] if p.get("scadenza_il")},
        }
        dati["stato_di_partenza"] = dati["stato"]
        self._transizione(dati, "SOSPESO", motivo, scrivi=False)
        if scrivi:
            self._scrivi_stato(dati)
            s = dati["sospensione"]
            self.verbale("sospensione", {"da": s["stato_di_partenza"], "motivo": motivo,
                                         "revisione_il": s["revisione_il"],
                                         "come_si_esce": s["come_si_esce"],
                                         "orologi_congelati": s["orologi_congelati"]})
        print("  SOSPESO. Revisione il %s. Per uscirne:  %s"
              % (dati["sospensione"]["revisione_il"][:10], dati["sospensione"]["come_si_esce"]))

    def _controlla_scadenze(self, dati: dict, scrivi: bool) -> bool:
        """Chiude i punti la cui causa e' sparita; applica i default scaduti;
        True se il lancio e' finito in SOSPESO (chi chiama esce 1)."""
        adesso = _adesso()
        for punto in list(dati["punti_umani_aperti"]):
            if self._causa_sparita(dati, punto["id"]):
                self.chiudi_punto_umano(dati, punto["id"])
                print("  punto umano %s chiuso: la causa e' sparita" % punto["id"])
        for punto in list(dati["punti_umani_aperti"]):
            if not punto.get("scadenza_il") or _da_iso(punto["scadenza_il"]) > adesso:
                continue
            voce = voce_punto_umano(punto["id"]) or {}
            if voce.get("default"):
                self._applica_default(dati, punto, voce, scrivi)
                continue
            self._sospendi_dati(dati, "punto umano %s scaduto senza default" % punto["id"],
                                (adesso + timedelta(days=7)).date(), scrivi)
            return True
        return False

    # -- impronte e da_rivedere ---------------------------------------------
    def _ricalcola_impronte(self, dati: dict) -> None:
        """Un artefatto il cui gate e' passato (sta in `impronte`) e che e' cambiato:
        lui e tutto cio' che dipende da lui finiscono in `da_rivedere`."""
        for nome, sha_passato in list(dati["impronte"].items()):
            p = os.path.join(self.dir, *nome.split("/"))
            sha_ora = gates.sha256_file(p) if os.path.exists(p) else None
            if sha_ora == sha_passato:
                continue
            print("  %s e' cambiato dopo il suo gate: si rivede lui e cio' che ne dipende" % nome)
            for f in [nome] + dipendenti_transitivi(nome):
                if f in dati["impronte"] and f not in dati["da_rivedere"]:
                    dati["da_rivedere"].append(f)
            dati["impronte"].pop(nome)

    # -- esecuzione di un gate ----------------------------------------------
    def _esegui(self, gate_id: str, dati: dict, scrivi: bool, rete):
        """Esegue un gate, scrive il suo verbale (idempotente) e la comodita' in
        stato.gate. Solleva _NonCostruito se il modulo manca (codice 3)."""
        v = gates.esegui_gate(gate_id, self.dir, rete)
        if not v.passa and any("controllo non costruito" in p for p in v.problemi):
            raise _NonCostruito(v)
        ingresso = self.impronte_ingresso(gate_id)
        if scrivi:
            _, tentativo = self.verbale_gate(v, ingresso)
        else:
            prec = self._verbali_gate(gate_id)
            tentativo = prec[-1][0] if prec else 1
        dati["gate"][gate_id] = {"passa": v.passa, "il": _iso(_adesso()), "tentativo": tentativo}
        print("  %-11s %s%s" % (gate_id, "passa" if v.passa else "BOCCIA",
                                 "" if v.passa else " — " + "; ".join(v.problemi)[:200]))
        if v.passa:
            nome = file_di_gate(gate_id)
            p = os.path.join(self.dir, *nome.split("/")) if nome else None
            if p and os.path.exists(p):
                dati["impronte"][nome] = gates.sha256_file(p)
            if nome in dati["da_rivedere"]:
                dati["da_rivedere"].remove(nome)
            if dati.get("bloccato_da") and dati["bloccato_da"].get("gate") == gate_id:
                dati["bloccato_da"] = None
        return v

    def _blocca(self, dati: dict, v, scrivi: bool) -> int:
        """Un gate ha bocciato: bloccato_da, ramo di fallimento se il registro ne
        ha uno, punto umano se il blocco dipende da una firma. Ritorna 1."""
        prec = dati.get("bloccato_da") or {}
        dati["bloccato_da"] = {"gate": v.gate,
                               "dal": prec["dal"] if prec.get("gate") == v.gate else _iso(_adesso()),
                               "problemi": list(v.problemi)}
        ramo = RAMI_FALLIMENTO.get((dati["stato"], v.gate))
        if ramo and ramo != dati["stato"]:
            bloccato = dati["bloccato_da"]
            self._transizione(dati, ramo, "%s boccia" % v.gate, scrivi=scrivi)
            dati["bloccato_da"] = bloccato  # la causa del ramo resta leggibile
        pu = PUNTO_UMANO_DEL_GATE.get(v.gate)
        if pu:
            self.apri_punto_umano(dati, pu)
        if scrivi:
            self._scrivi_stato(dati)
        return 1

    def _ambiente(self, dati: dict, problema: str, scrivi: bool, gate_id=None) -> int:
        print("  AMBIENTE: %s" % problema)
        if scrivi:
            self.verbale_idempotente("ambiente", {"problema": problema},
                                     {"gate": gate_id, "stato": dati.get("stato")})
            self._scrivi_stato(dati)
        return 3

    def _rinomina_rotto(self, nome: str, scrivi: bool, errore) -> int:
        p = os.path.join(self.dir, *nome.split("/"))
        if scrivi and os.path.exists(p):
            os.replace(p, p + ".rotto")
            print("  %s\n  -> rinominato %s.rotto (non cancellato)" % (errore, nome))
        else:
            print("  %s" % errore)
        return 2

    def _dentro_avanza(self, solo_gate, a_vuoto, rete) -> int:
        scrivi = not a_vuoto
        dati = self._stato_completo()
        if a_vuoto:
            print("  (a vuoto: calcolo e stampo, non scrivo niente)")

        # 0. JSON rotti -> 2, nessun'altra scrittura, il file si rinomina .rotto
        for nome in sorted(list(self.artefatti_presenti()) + ["offerta.PROPOSTA.json"]):
            try:
                self._leggi(nome)
            except gates.ErroreArtefatto as e:
                return self._rinomina_rotto(nome, scrivi, e)

        # --solo-gate: un controllo, il suo verbale, niente altro
        if solo_gate:
            if not gates.voce_gate(solo_gate):
                raise ErroreLancio("Gate sconosciuto: %s" % solo_gate)
            try:
                v = self._esegui(solo_gate, dati, scrivi, rete)
            except _NonCostruito as e:
                return self._ambiente(dati, e.verdetto.problemi[0], scrivi, solo_gate)
            return 0 if v.passa else 1

        # 1. punti umani: cause sparite, scadenze (default o SOSPESO)
        if self._controlla_scadenze(dati, scrivi):
            return 1
        # 2. impronte cambiate a monte -> da_rivedere a valle
        self._ricalcola_impronte(dati)

        # 3. il giro
        giri = 0
        while True:
            giri += 1
            if giri > 30:  # nessuna catena di stati e' lunga 30: e' un difetto, non un lancio
                raise RuntimeError("avanza: piu' di 30 giri senza fermarsi")
            stato = dati["stato"]
            print("  stato: %s" % stato)
            if stato == "SOSPESO":
                s = dati.get("sospensione") or {}
                print("  Sospeso dal %s (%s). Per uscirne:  %s"
                      % (str(s.get("dal", "?"))[:10], s.get("motivo", "?"),
                         s.get("come_si_esce", "lancio riprendi %s" % self.slug)))
                if scrivi:
                    self._scrivi_stato(dati)
                return 1
            if stato in STATI_FINALI:
                print("  stato finale: niente da fare")
                if scrivi:
                    self._scrivi_stato(dati)
                return 0

            try:
                # 3a. cio' che va rivisto perche' i suoi ingressi sono cambiati
                for nome in list(dati["da_rivedere"]):
                    gid = gate_di_file(nome)
                    if not gid:
                        dati["da_rivedere"].remove(nome)
                        continue
                    v = self._esegui(gid, dati, scrivi, rete)
                    if not v.passa:
                        return self._blocca(dati, v, scrivi)
                # 3b. gate continui dello stato
                for gid in GATE_CONTINUI.get(stato, []):
                    v = self._esegui(gid, dati, scrivi, rete)
                    if not v.passa:
                        return self._blocca(dati, v, scrivi)
                    if gid == "GATE-TSR-2":
                        self.chiudi_punto_umano(dati, "PU-SPESA")
                # 3c. transizione di sistema
                if stato in TRANSIZIONI_SISTEMA:
                    t = TRANSIZIONI_SISTEMA[stato]
                    for gid in t["gate"]:
                        v = self._esegui(gid, dati, scrivi, rete)
                        if not v.passa:
                            return self._blocca(dati, v, scrivi)
                    self._transizione(dati, t["a"], "%s passano" % ", ".join(t["gate"]), scrivi)
                    continue
                # 3d. transizioni che richiedono una persona
                if stato == "ISTRUITO":
                    prop = self._leggi("offerta.PROPOSTA.json")
                    if (isinstance(prop, dict) and prop.get("ruolo_prodotto") not in RUOLI_AMMESSI
                            and not os.path.exists(os.path.join(self.dir, "offerta.json"))):
                        self.apri_punto_umano(dati, "PU-RUOLO")
                        if scrivi:
                            self._scrivi_stato(dati)
                        return 1
                    v = self._esegui("GATE-OFF-1", dati, scrivi, rete)
                    if not v.passa:
                        return self._blocca(dati, v, scrivi)
                    self.chiudi_punto_umano(dati, "PU-PREZZO")
                    self._transizione(dati, "DATATO", "GATE-OFF-1 passa con firma umana", scrivi)
                    continue
                if stato == "PRONTO":
                    if self._causa_sparita(dati, "PU-APERTURA"):
                        self.chiudi_punto_umano(dati, "PU-APERTURA")
                        self._transizione(dati, "APERTO", "via libera firmato", scrivi)
                        continue
                    self.apri_punto_umano(dati, "PU-APERTURA")
                    if scrivi:
                        self._scrivi_stato(dati)
                    return 0  # avanzato fin dove poteva: PU-APERTURA non ha default, mai
                if stato == "APERTO":
                    off = self._leggi("offerta.json") or {}
                    chiusura = off.get("data_chiusura") if isinstance(off, dict) else None
                    if chiusura and _adesso().date() >= date.fromisoformat(chiusura):
                        self._transizione(dati, "CHIUSO", "data di chiusura raggiunta", scrivi)
                        continue
                    print("  in vendita fino al %s" % (chiusura or "?"))
                    if scrivi:
                        self._scrivi_stato(dati)
                    return 0
                raise RuntimeError("stato senza transizione nel motore: %s" % stato)
            except _NonCostruito as e:
                return self._ambiente(dati, e.verdetto.problemi[0], scrivi, e.verdetto.gate)

    # -- comandi umani -------------------------------------------------------
    def sospendi(self, motivo: str, revisione: date, chi: str | None = None) -> dict:
        self._esigi()
        with Lock(self.path_lock):
            dati = self._stato_completo()
            if dati["stato"] == "SOSPESO":
                raise ErroreLancio("Il lancio e' gia' SOSPESO (dal %s)."
                                   % str(dati["sospensione"]["dal"])[:10])
            if dati["stato"] in STATI_FINALI:
                raise ErroreLancio("Il lancio e' in %s: uno stato finale non si sospende."
                                   % dati["stato"])
            if revisione < _adesso().date():
                raise ErroreLancio("La data di revisione e' nel passato: %s" % revisione)
            self._sospendi_dati(dati, motivo, revisione, scrivi=True)
            return dati

    def riprendi(self, chi: str | None = None) -> dict:
        self._esigi()
        with Lock(self.path_lock):
            dati = self._stato_completo()
            if dati["stato"] != "SOSPESO":
                raise ErroreLancio("Il lancio non e' SOSPESO (e' %s): niente da riprendere."
                                   % dati["stato"])
            s = dati["sospensione"] or {}
            partenza = s.get("stato_di_partenza") or dati.get("stato_di_partenza")
            if not partenza:
                raise ErroreLancio("Sospensione senza stato_di_partenza: non so dove riportarlo.")
            adesso = _adesso()
            dal = _da_iso(s["dal"]) if s.get("dal") else adesso
            # gli orologi ripartono dal valore che avevano all'ingresso in SOSPESO
            for punto in dati["punti_umani_aperti"]:
                congelato = s.get("orologi_congelati", {}).get(punto["id"])
                if congelato:
                    residuo = _da_iso(congelato) - dal
                    punto["scadenza_il"] = _iso(adesso + max(residuo, timedelta(0)))
            dati["sospensione"] = None
            dati["stato_di_partenza"] = None
            self._transizione(dati, partenza, "ripresa: la causa e' rimossa", scrivi=False)
            self._scrivi_stato(dati)
            self.verbale("ripresa", {"a": partenza, "chi": chi or _git_user_name(),
                                     "orologi_ripartiti": {p["id"]: p.get("scadenza_il")
                                                           for p in dati["punti_umani_aperti"]}})
            return dati

    def abbandona(self, motivo: str, chi: str | None = None) -> dict:
        self._esigi()
        with Lock(self.path_lock):
            dati = self._stato_completo()
            if dati["stato"] == "ABORTITO":
                raise ErroreLancio("Il lancio e' gia' ABORTITO.")
            si_salva = sorted(n for n, problemi in self.valida_tutti().items() if not problemi)
            dati["punti_umani_aperti"] = []
            dati["sospensione"] = None
            self._transizione(dati, "ABORTITO", motivo, scrivi=False)
            self._scrivi_stato(dati)
            self.verbale("abbandono", {"motivo": motivo, "chi": chi or _git_user_name(),
                                       "si_salva": si_salva})
            print("  ABORTITO. Si salva: %s" % (", ".join(si_salva) or "niente"))
            return dati

    def firma(self, prezzo: float, data_apertura: date, *, chi: str | None = None,
              ruolo: str | None = None, durata_gg: int | None = None) -> dict:
        """offerta.json = proposta + prezzo/data/durata/data_chiusura + firma.
        NON tocca la PROPOSTA. E' l'unico posto che scrive il sotto-oggetto `firma`."""
        self._esigi()
        p_prop = os.path.join(self.dir, "offerta.PROPOSTA.json")
        if not os.path.exists(p_prop):
            raise ErroreLancio("Manca %s: non c'e' niente da firmare. La proposta la scrive "
                               "lan-off-conductor, la firma la mette una persona." % p_prop)
        if isinstance(prezzo, bool) or not isinstance(prezzo, (int, float)) or prezzo <= 0:
            raise ErroreLancio("Prezzo non valido: %r (serve un numero > 0)" % (prezzo,))
        if data_apertura < _adesso().date():
            raise ErroreLancio("Data di apertura nel passato: %s" % data_apertura)
        if ruolo is not None and ruolo not in RUOLI_AMMESSI:
            raise ErroreLancio("Ruolo non ammesso: %s (vendita | acquisizione-contatti)" % ruolo)
        prop = self._leggi("offerta.PROPOSTA.json")
        if not isinstance(prop, dict):
            raise ErroreLancio("offerta.PROPOSTA.json non e' un oggetto JSON")
        durata = durata_gg if durata_gg is not None else prop.get("durata_carrello_gg")
        if isinstance(durata, bool) or not isinstance(durata, int) or durata <= 0:
            raise ErroreLancio("Durata carrello non valida (%r): passa --durata N" % (durata,))
        with Lock(self.path_lock):
            offerta = dict(prop)
            offerta["lancio_id"] = self.slug
            offerta["prezzo"] = prezzo
            offerta["durata_carrello_gg"] = durata
            offerta["data_apertura"] = data_apertura.isoformat()
            offerta["data_chiusura"] = (data_apertura + timedelta(days=durata)).isoformat()
            if ruolo:
                offerta["ruolo_prodotto"] = ruolo
            offerta["firma"] = {"chi": chi or _git_user_name(), "canale": "comando-utente",
                                "riferimento": "lancio firma",
                                "proposta_impronta": gates.sha256_file(p_prop),
                                "il": _iso(_adesso())}
            with open(os.path.join(self.dir, "offerta.json"), "w",
                      encoding="utf-8", newline="\n") as f:
                json.dump(offerta, f, ensure_ascii=False, indent=2)
                f.write("\n")
            self.verbale("firma", {"chi": offerta["firma"]["chi"], "canale": "comando-utente",
                                   "prezzo": prezzo, "data_apertura": offerta["data_apertura"],
                                   "data_chiusura": offerta["data_chiusura"],
                                   "ruolo_prodotto": offerta.get("ruolo_prodotto"),
                                   "proposta_impronta": offerta["firma"]["proposta_impronta"]})
        return offerta

    def via_libera(self, chi: str | None = None) -> dict:
        self._esigi()
        p = os.path.join(self.dir, "apertura.json")
        if not os.path.exists(p):
            raise ErroreLancio("Manca %s: il via libera si mette su una lista di "
                               "sincronizzazione che esiste, non nel vuoto." % p)
        ape = self._leggi("apertura.json")
        if not isinstance(ape, dict):
            raise ErroreLancio("apertura.json non e' un oggetto JSON")
        with Lock(self.path_lock):
            ape["via_libera"] = {"chi": chi or _git_user_name(), "canale": "comando-utente",
                                 "riferimento": "lancio via-libera", "il": _iso(_adesso())}
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                json.dump(ape, f, ensure_ascii=False, indent=2)
                f.write("\n")
            self.verbale("via-libera", {"chi": ape["via_libera"]["chi"],
                                        "canale": "comando-utente"})
        return ape

    def copia_esempio(self, cartella: str) -> list[str]:
        """Copia i file di un kit d'esempio dentro il lancio, riscrivendo `lancio_id`
        nei JSON. Non tocca stato.json, .lock, verbali/. Ritorna i file copiati."""
        copiati = []
        if not os.path.isdir(cartella):
            return copiati
        for radice, cartelle, file in os.walk(cartella):
            cartelle[:] = [c for c in cartelle if c != "verbali"]
            for nome in file:
                if nome in ("stato.json", ".lock"):
                    continue
                src = os.path.join(radice, nome)
                rel = os.path.relpath(src, cartella)
                dst = os.path.join(self.dir, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if nome.endswith(".json"):
                    try:
                        dati = json.load(open(src, encoding="utf-8"))
                    except json.JSONDecodeError:
                        shutil.copyfile(src, dst)
                    else:
                        if isinstance(dati, dict) and "lancio_id" in dati:
                            dati["lancio_id"] = self.slug
                        with open(dst, "w", encoding="utf-8", newline="\n") as f:
                            json.dump(dati, f, ensure_ascii=False, indent=2)
                            f.write("\n")
                else:
                    shutil.copyfile(src, dst)
                copiati.append(rel.replace(os.sep, "/"))
        return sorted(copiati)


def elenca() -> list[Lancio]:
    if not os.path.isdir(LANCI):
        return []
    return [Lancio(d) for d in sorted(os.listdir(LANCI))
            if os.path.exists(os.path.join(LANCI, d, "stato.json"))]


# ==========================================================================
# S2b (MT-3XWC) — `avanza`, punti umani, comandi umani
# ==========================================================================
#
# CAMPI DI STATO (CONTRATTO-STATO.md). Se un campo manca nel file, il lettore lo
# tratta come vuoto, mai come errore: i lanci creati prima del contratto restano
# leggibili.

CAMPI_DEFAULT = {
    "bloccato_da": None,
    "punti_umani_aperti": [],
    "sospensione": None,
    "impronte": {},
    "da_rivedere": [],
    "gate": {},
}

STATI_FINALI = ("APPRESO", "ARCHIVIATO", "ABORTITO")

# La tabella delle transizioni `autorizza: sistema` (CONTRATTO-STATO.md, tabella
# "Quale gate in quale transizione"). E' un dict e non una lettura del registro
# perche' l'ordine di esecuzione dei gate e' una scelta del motore; un test
# (`test_tabella_transizioni_coerente_col_registro`) verifica che non diverga dal
# registro in silenzio.
TRANSIZIONI_SISTEMA = {
    "IDEA": {"a": "VALUTATO", "gate": ["GATE-PUB-1", "GATE-STR-1"]},
    "VALUTATO": {"a": "ISTRUITO", "gate": ["GATE-PRD-1", "GATE-INT-1", "GATE-PRV-1"]},
    "DATATO": {"a": "IN_PRODUZIONE", "gate": ["GATE-TSR-1"]},
    "IN_PRODUZIONE": {"a": "PRONTO",
                      "gate": ["GATE-CPY-1", "GATE-FNL-1", "GATE-EDT-1", "GATE-REG-1"]},
    "CHIUSO": {"a": "APPRESO", "gate": ["GATE-CNS-1", "GATE-MEM-1"]},
}

# Transizioni `autorizza: persona`: il motore le esegue solo se la firma umana e'
# gia' dentro l'artefatto (messa da `lancio firma` / `lancio via-libera`).
TRANSIZIONI_PERSONA = {
    "ISTRUITO": {"a": "DATATO", "gate": ["GATE-OFF-1"], "punto_umano": "PU-PREZZO"},
    "PRONTO": {"a": "APERTO", "gate": [], "punto_umano": "PU-APERTURA"},
    "APERTO": {"a": "CHIUSO", "gate": [], "punto_umano": None},
}

# Un gate che boccia lascia lo stato dov'e', SALVO i rami scritti nel registro
# come transizione a se' ("GATE-X boccia"): (stato, gate) -> stato di arrivo.
RAMI_FALLIMENTO = {
    ("IDEA", "GATE-STR-1"): "ARCHIVIATO",
    ("IN_PRODUZIONE", "GATE-TSR-2"): "DATATO",
}

# Gate "continui": si rieseguono a ogni giro finche' il lancio sta in quello stato.
GATE_CONTINUI = {"IN_PRODUZIONE": ["GATE-TSR-2"]}

# Quando il blocco di un gate dipende da una firma/decisione umana, il motore apre
# il punto umano corrispondente.
PUNTO_UMANO_DEL_GATE = {"GATE-OFF-1": "PU-PREZZO", "GATE-TSR-2": "PU-SPESA"}

RUOLI_AMMESSI = ("vendita", "acquisizione-contatti")


def _adesso() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")


def _da_iso(s: str) -> datetime:
    dt = datetime.fromisoformat(s)
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def data_italiana(s: str) -> date:
    """gg/mm/aaaa -> date. Errore chiaro se non torna."""
    try:
        return datetime.strptime(s.strip(), "%d/%m/%Y").date()
    except (ValueError, AttributeError):
        raise ErroreLancio("Data non valida: '%s' (serve gg/mm/aaaa)" % s)


# -- il registro, letto una volta -------------------------------------------

def _registro() -> dict:
    return gates.registro()


def _artefatti_registro() -> list[dict]:
    return _registro().get("artefatti", [])


def file_di_art(art_id: str) -> str | None:
    for a in _artefatti_registro():
        if a["id"] == art_id:
            return a["file"]
    return None


def gate_di_file(nome: str) -> str | None:
    for a in _artefatti_registro():
        if a["file"] == nome:
            return a.get("gate")
    return None


def file_di_gate(gate_id: str) -> str | None:
    """Il file che un gate presidia (registro gate[].presidia -> artefatti[].file)."""
    voce = gates.voce_gate(gate_id)
    if not voce:
        return None
    return file_di_art(voce.get("presidia"))


def dipendenze_di_file(nome: str) -> list[str]:
    for a in _artefatti_registro():
        if a["file"] == nome:
            return [f for f in (file_di_art(d) for d in a.get("dipende_da", [])) if f]
    return []


def dipendenti_transitivi(nome: str) -> list[str]:
    """Tutti i file che dipendono da `nome`, direttamente o attraverso altri."""
    trovati: list[str] = []
    coda = [nome]
    while coda:
        corrente = coda.pop(0)
        for a in _artefatti_registro():
            if corrente in dipendenze_di_file(a["file"]) and a["file"] not in trovati:
                trovati.append(a["file"])
                coda.append(a["file"])
    return trovati


def voce_punto_umano(pu_id: str) -> dict | None:
    for p in _registro().get("punti_umani", []):
        if p["id"] == pu_id:
            return p
    return None


def _git_user_name() -> str:
    try:
        import subprocess
        out = subprocess.run(["git", "config", "user.name"], capture_output=True,
                             text=True, encoding="utf-8", timeout=5).stdout.strip()
        if out:
            return out
    except Exception:  # noqa: BLE001 - git assente: si ripiega sull'utente di sistema
        pass
    return os.environ.get("USERNAME") or os.environ.get("USER") or "sconosciuto"


class _NonCostruito(Exception):
    """Un gate il cui modulo non esiste: per il motore e' codice 3, non 1."""

    def __init__(self, verdetto):
        super().__init__(verdetto.problemi[0] if verdetto.problemi else verdetto.gate)
        self.verdetto = verdetto


# -- la firma pubblica -------------------------------------------------------

def avanza(lancio_id: str, *, solo_gate: str | None = None, a_vuoto: bool = False,
           rete=None) -> int:
    """Fa avanzare un lancio finche' un controllo non lo ferma.

    Ritorna il codice di uscita (0 avanzato, 1 bloccato, 2 ingresso non valido,
    3 ambiente). Non solleva eccezioni verso il chiamante: un errore imprevisto
    diventa 3 con il verbale `ambiente` scritto, mai un traceback.
    """
    try:
        lancio = Lancio(lancio_id)
        lancio._esigi()
    except ErroreLancio as e:
        print("  %s" % e)
        return 2

    lock = Lock(lancio.path_lock, attesa_massima_s=1.0)
    try:
        lock.__enter__()
    except ErroreLancio:
        chi = {}
        try:
            chi = json.load(open(lancio.path_lock, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
        print("  Il lancio '%s' e' occupato da un'altra sessione: pid %s, dal %s.\n"
              "  Lock: %s" % (lancio_id, chi.get("pid", "?"), chi.get("preso_il", "?"),
                              lancio.path_lock))
        return 1
    try:
        return lancio._dentro_avanza(solo_gate, a_vuoto, rete)
    except ErroreLancio as e:
        print("  %s" % e)
        return 2
    except gates.ErroreArtefatto as e:
        print("  %s" % e)
        return 2
    except Exception as e:  # noqa: BLE001 - mai un traceback verso l'utente
        problema = "%s: %s" % (type(e).__name__, e)
        print("  Errore di sistema: %s" % problema)
        if not a_vuoto:
            try:
                lancio.verbale_idempotente("ambiente", {"problema": problema}, {"gate": None})
            except Exception:  # noqa: BLE001
                pass
        return 3
    finally:
        lock.__exit__(None, None, None)
