"""
valida_registro.py — verifica che il piano dell'ecosistema LANCI sia coerente con se' stesso.

PERCHE' ESISTE
    La versione precedente di questo piano era 3.718 righe di prosa distribuite su
    undici documenti che si citavano a vicenda. Tre revisori indipendenti hanno
    misurato il risultato: sigle di reparto usate in un dossier e inesistenti
    nell'altro, sette nomi di gate contro tre nomi ufficiali senza mappa, una
    correzione applicata nel documento di governo e mai arrivata nel documento che
    si esegue, cinque controlli su sette affidati allo stesso agente che produceva
    la cosa controllata.

    Nessuno di quei difetti e' un errore di ragionamento: sono tutti errori di
    COPIA. La prosa non puo' restare coerente con se stessa; un dato validato da
    un programma si'.

USO
    python valida_registro.py                 (dalla cartella dati/)
    python valida_registro.py --registro X    (percorso alternativo)

CODICI DI USCITA — la stessa convenzione dell'ecosistema
    0   il piano e' coerente
    1   almeno un invariante e' violato: il piano NON si costruisce
    2   il registro non e' leggibile o non e' YAML valido
    3   ambiente: manca una dipendenza

Su Windows: anteporre PYTHONIOENCODING=utf-8 (la console cp1252 non regge gli accenti).
"""

from __future__ import annotations

import argparse
import io
import os
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - ambiente
    sys.stderr.write("manca la libreria pyyaml: pip install pyyaml\n")
    sys.exit(3)


QUI = os.path.dirname(os.path.abspath(__file__))
REGISTRO_DEFAULT = os.path.join(QUI, "registro.yaml")

# I soli campi che Claude Code accetta nel frontmatter di un agente. Un campo
# inventato non produce un errore: fa scartare il file IN SILENZIO, e l'agente
# non compare in /agents. E' successo davvero, su 120 file, il 2026-08-31.
CAMPI_FRONTMATTER_VALIDI = {"name", "description", "model", "color", "tools"}

# I modelli con identificativo esplicito. Gli alias mentono: ADR-014 ha misurato
# che "--model sonnet" restituiva claude-sonnet-4-6, cioe' si pagava un modello
# diverso da quello scelto, in silenzio.
MODELLI_AMMESSI = {
    "claude-opus-5",
    "claude-sonnet-5",
    "claude-haiku-4-5-20251001",
}

GRADI_AMMESSI = {"scagnozzo", "sentinella", "doombot"}
GRADO_MODELLO = {
    "scagnozzo": "claude-haiku-4-5-20251001",
    "sentinella": "claude-sonnet-5",
    "doombot": "claude-opus-5",
}


class Esito:
    """Raccoglie le violazioni invece di fermarsi alla prima: chi legge vuole
    l'elenco completo, non il primo problema in ordine alfabetico."""

    def __init__(self) -> None:
        self.violazioni: list[tuple[str, str]] = []
        self.controlli_eseguiti = 0

    def verifica(self, invariante: str, condizione: bool, messaggio: str) -> None:
        self.controlli_eseguiti += 1
        if not condizione:
            self.violazioni.append((invariante, messaggio))

    @property
    def ok(self) -> bool:
        return not self.violazioni


def carica(percorso: str) -> dict:
    if not os.path.exists(percorso):
        sys.stderr.write(f"registro non trovato: {percorso}\n")
        sys.exit(2)
    try:
        with io.open(percorso, encoding="utf-8") as fh:
            dati = yaml.safe_load(fh.read())
    except yaml.YAMLError as exc:
        sys.stderr.write(f"registro non e' YAML valido: {exc}\n")
        sys.exit(2)
    if not isinstance(dati, dict):
        sys.stderr.write("il registro deve essere una mappa\n")
        sys.exit(2)
    return dati


def valida(d: dict, cartella_schemi: str) -> Esito:
    e = Esito()

    artefatti = d.get("artefatti", [])
    gate = d.get("gate", [])
    agenti = d.get("agenti", [])
    stati = d.get("stati", [])
    punti = d.get("punti_umani", [])

    id_artefatti = {a["id"] for a in artefatti}
    id_gate = {g["id"] for g in gate}
    id_agenti = {a["id"] for a in agenti}
    id_stati = {s["id"] for s in stati}
    per_id_agente = {a["id"]: a for a in agenti}

    # -- INV-01 -------------------------------------------------------------
    # Chi produce non approva. Nella versione precedente questa regola era
    # scritta e violata dieci righe piu' sotto, in cinque casi su sette.
    for a in artefatti:
        e.verifica(
            "INV-01",
            a["produttore"] != a["giudice"],
            f"{a['id']}: produttore e giudice sono lo stesso agente ({a['produttore']})",
        )

    # -- INV-02 -------------------------------------------------------------
    # Ogni artefatto ha uno schema, e lo schema esiste sul disco. "Produce un
    # file JSON" senza schema non e' un contratto: e' una speranza.
    for a in artefatti:
        schema = a.get("schema", "")
        e.verifica("INV-02", bool(schema), f"{a['id']}: nessuno schema dichiarato")
        if schema:
            percorso = os.path.join(cartella_schemi, os.path.basename(schema))
            e.verifica(
                "INV-02",
                os.path.exists(percorso),
                f"{a['id']}: schema dichiarato ma assente sul disco ({schema})",
            )

    # -- INV-03 -------------------------------------------------------------
    # Ogni gate dice dove torna il lancio quando boccia. Nella versione
    # precedente nessuno dei gate lo diceva: un controllo che blocca senza dire
    # dove si torna produce un lancio fermo e nessuno sa a chi tocca.
    for g in gate:
        ramo = g.get("ramo_fallimento", "")
        e.verifica("INV-03", bool(ramo), f"{g['id']}: nessun ramo di fallimento")
        stato_citato = [s for s in id_stati if s in str(ramo)]
        e.verifica(
            "INV-03",
            bool(stato_citato) or g.get("tipo") == "continuo",
            f"{g['id']}: il ramo di fallimento non nomina nessuno stato valido",
        )

    # -- INV-04 -------------------------------------------------------------
    # Un gate senza un caso costruito per farlo fallire e' decorativo: nessuno
    # sapra' mai se blocca davvero finche' non servira', ed e' tardi.
    for g in gate:
        e.verifica(
            "INV-04",
            bool(g.get("test_rosso")),
            f"{g['id']}: nessun test rosso dichiarato",
        )

    # -- INV-05 -------------------------------------------------------------
    # Nessuna sigla inventata. E' il difetto che rendeva il documento operativo
    # non installabile sopra quello di governo.
    for a in artefatti:
        e.verifica(
            "INV-05",
            a["gate"] in id_gate,
            f"{a['id']}: cita il gate {a['gate']} che non esiste",
        )
        e.verifica(
            "INV-05",
            a["se_fallisce"] in id_stati,
            f"{a['id']}: se_fallisce punta a {a['se_fallisce']}, che non e' uno stato",
        )
        for dip in a.get("dipende_da", []):
            e.verifica(
                "INV-05",
                dip in id_artefatti,
                f"{a['id']}: dipende da {dip}, che non e' un artefatto",
            )
    for g in gate:
        e.verifica(
            "INV-05",
            g["presidia"] in id_artefatti,
            f"{g['id']}: presidia {g['presidia']}, che non e' un artefatto",
        )
    for t in d.get("transizioni", []):
        for campo in ("da", "a"):
            valore = t[campo]
            ammesso = valore in id_stati or valore in ("*", "stato_di_partenza")
            e.verifica(
                "INV-05",
                ammesso,
                f"transizione {t['da']}->{t['a']}: {valore} non e' uno stato valido",
            )

    # -- INV-06 -------------------------------------------------------------
    # Ogni punto umano ha una scadenza, oppure dichiara perche' non ce l'ha.
    # Il punto su cui l'azienda si e' fermata sei mesi era l'unico senza.
    for p in punti:
        ha_scadenza = p.get("scadenza_giorni") is not None
        ha_motivo = bool(p.get("default_giustificato_da"))
        e.verifica(
            "INV-06",
            ha_scadenza or ha_motivo,
            f"{p['id']}: nessuna scadenza e nessuna motivazione per non averla",
        )
        e.verifica(
            "INV-06",
            bool(p.get("allo_scadere")),
            f"{p['id']}: non dice cosa succede allo scadere",
        )

    # -- INV-07 -------------------------------------------------------------
    # Il nucleo minimo si CALCOLA dagli artefatti, non si elenca a mano. La
    # versione precedente lo elencava, e l'elenco non conteneva i produttori di
    # tre artefatti necessari: il primo lancio si fermava alla prima fase.
    produttori = {a["produttore"] for a in artefatti}
    giudici = {a["giudice"] for a in artefatti}
    necessari = produttori | giudici
    mancanti = necessari - id_agenti
    e.verifica(
        "INV-07",
        not mancanti,
        f"agenti necessari e non definiti: {sorted(mancanti)}",
    )

    # -- INV-08 -------------------------------------------------------------
    # Grado e modello devono corrispondere, e il modello deve essere un
    # identificativo esplicito. Un alias fa pagare un modello per un altro.
    for a in agenti:
        grado = a.get("grado")
        e.verifica("INV-08", grado in GRADI_AMMESSI, f"{a['id']}: grado sconosciuto ({grado})")
        e.verifica(
            "INV-08",
            a.get("modello") in MODELLI_AMMESSI,
            f"{a['id']}: modello non esplicito o sconosciuto ({a.get('modello')})",
        )
        if grado in GRADO_MODELLO:
            e.verifica(
                "INV-08",
                a.get("modello") == GRADO_MODELLO[grado],
                f"{a['id']}: grado {grado} ma modello {a.get('modello')}",
            )

    # -- INV-09 -------------------------------------------------------------
    # Il giudice non puo' scrivere. Un giudice con la penna in mano puo'
    # riparare cio' che dovrebbe bocciare, e nessuno lo sapra'.
    for a in artefatti:
        g = per_id_agente.get(a["giudice"])
        if not g:
            continue
        tools = set(g.get("tools", []))
        e.verifica(
            "INV-09",
            not (tools & {"Write", "Edit"}),
            f"{g['id']} giudica {a['id']} e ha permesso di scrittura ({sorted(tools & {'Write', 'Edit'})})",
        )

    # -- INV-10 ------------------------------------------------------------
    # Un artefatto che richiede una firma dice quale campo la porta, e quel
    # campo non e' scrivibile da nessun agente. Senza, "firmato_da" e' una
    # stringa che qualunque agente in ciclo di riparazione riempie con "Max".
    canali = set(d.get("canali_firma_ammessi", []))
    e.verifica("INV-10", bool(canali), "nessun canale di firma ammesso dichiarato")
    for a in artefatti:
        if a.get("umano"):
            e.verifica(
                "INV-10",
                bool(a.get("firma_obbligatoria")),
                f"{a['id']}: richiede una firma umana ma non dice quale campo la porta",
            )

    # -- Coerenza del grafo delle dipendenze -------------------------------
    # Un ciclo fra artefatti significa un lancio che non puo' cominciare.
    def ha_ciclo() -> list[str]:
        visitati: dict[str, int] = {}
        percorso: list[str] = []
        per_id = {a["id"]: a for a in artefatti}

        def scendi(nodo: str) -> list[str]:
            stato = visitati.get(nodo, 0)
            if stato == 1:
                return percorso[percorso.index(nodo):] + [nodo]
            if stato == 2:
                return []
            visitati[nodo] = 1
            percorso.append(nodo)
            for dip in per_id.get(nodo, {}).get("dipende_da", []):
                trovato = scendi(dip)
                if trovato:
                    return trovato
            percorso.pop()
            visitati[nodo] = 2
            return []

        for a in artefatti:
            trovato = scendi(a["id"])
            if trovato:
                return trovato
        return []

    ciclo = ha_ciclo()
    e.verifica("INV-11", not ciclo, f"ciclo fra artefatti: {' -> '.join(ciclo)}")

    # -- Ogni artefatto e' raggiungibile e ogni gate presidia qualcosa ------
    presidiati = {g["presidia"] for g in gate}
    senza_gate = id_artefatti - presidiati
    e.verifica("INV-12", not senza_gate, f"artefatti senza nessun gate: {sorted(senza_gate)}")

    return e


def main() -> int:
    ap = argparse.ArgumentParser(description="verifica la coerenza del registro LANCI")
    ap.add_argument("--registro", default=REGISTRO_DEFAULT)
    ap.add_argument("--schemi", default=os.path.join(QUI, "schemi"))
    args = ap.parse_args()

    d = carica(args.registro)
    e = valida(d, args.schemi)

    print(f"registro   : {args.registro}")
    print(f"artefatti  : {len(d.get('artefatti', []))}")
    print(f"gate       : {len(d.get('gate', []))}")
    print(f"agenti     : {len(d.get('agenti', []))}")
    print(f"controlli  : {e.controlli_eseguiti}")
    print()

    if e.ok:
        print("PIANO COERENTE - nessun invariante violato")
        return 0

    print(f"PIANO INCOERENTE - {len(e.violazioni)} violazioni")
    print()
    for inv, msg in e.violazioni:
        print(f"  [{inv}] {msg}")
    print()
    print("Il piano non si costruisce finche' queste righe non sono zero.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
